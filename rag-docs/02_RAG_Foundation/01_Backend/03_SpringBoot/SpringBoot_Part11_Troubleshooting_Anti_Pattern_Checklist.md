# Spring Boot Part11 - Troubleshooting, Anti Pattern, Checklist

---

# 1. Troubleshooting

## 1.1 Troubleshooting 개념

### [개념]

Troubleshooting은 Spring Boot Application에서 발생한 오류의 원인을 단계적으로 추적하고 해결하는 과정이다.

Spring Boot 문제는 대부분 아래 흐름 중 한 지점에서 발생한다.

```text
Client Request
→ Frontend URL / Method
→ Controller Mapping
→ Request Binding
→ Validation
→ Service Logic
→ Repository Query
→ Transaction
→ Exception Handler
→ Response
```

Troubleshooting의 목적:

- 오류 원인 빠르게 좁히기
- Layer별 책임 기준으로 문제 분리
- 반복되는 실수 패턴 탐지
- Backend Agent의 코드 검수 정확도 향상
- API 연동 문제 해결
- Spring Boot Anti Pattern 탐지

---

### [핵심]

Spring Boot Troubleshooting 핵심 영역:

- Application Startup Error
- Bean Not Found
- Component Scan 문제
- Mapping Not Found
- Request Binding Error
- Validation Error
- Repository / JPA Error
- Transaction Not Working
- Exception Handling 문제
- CORS Error
- Profile / Properties 문제
- External API Error
- Logging 문제
- Layer Responsibility 위반

기본 Debug 순서:

```text
Error Message 확인
→ 발생 위치 확인
→ Layer 확인
→ 최근 변경 코드 확인
→ 설정 / Profile 확인
→ 요청 / 응답 확인
→ 로그 확인
→ 재현 조건 확인
→ 원인 분리
→ 수정
→ 재검증
```

---

### [실무]

API 오류 추적 흐름:

```text
1. Browser Network 또는 Postman 요청 확인
2. Request URL 확인
3. HTTP Method 확인
4. Controller @RequestMapping 확인
5. PathVariable / RequestParam / RequestBody 확인
6. DTO Field Name / Type 확인
7. Validation Error 확인
8. Service Business Logic 확인
9. Repository Query 확인
10. Transaction / Lazy Loading 확인
11. GlobalExceptionHandler 확인
12. Response 형식 확인
```

실무 기준:

- 404는 URL / Mapping 우선 확인
- 400은 Request Binding / Validation 우선 확인
- 401 / 403은 Security / 인증 / 인가 우선 확인
- 500은 Service / Repository / Exception Handler / 설정 우선 확인
- 브라우저만 실패하면 CORS 가능성 확인
- 로컬과 배포 결과가 다르면 Profile / 환경변수 확인

---

### [FAQ]

Q. Spring Boot 문제는 어디서부터 확인하는 게 좋아?

A.
요청 URL, HTTP Method, Controller Mapping, Request Binding, Validation, Service, Repository, Exception Handler 순서로 확인하는 것이 좋다.

Q. 500 Error가 나면 무조건 서버 코드 문제야?

A.
대부분 서버 내부 예외지만 원인은 설정 누락, DB 연결 실패, DTO 변환 문제, Transaction 문제, 외부 API 실패 등 다양하다.

Q. 브라우저에서는 안 되고 Postman에서는 되면?

A.
CORS, Authorization Header, Cookie / Credentials, Frontend baseURL, Preflight OPTIONS 요청을 확인해야 한다.

---

# 2. Application Startup Troubleshooting

## 2.1 Application 실행 실패

### [개념]

Application Startup Error는 Spring Boot Application이 실행 과정에서 실패하는 문제다.

주로 Bean 등록, 설정 값, DB 연결, Entity Mapping, Profile 문제에서 발생한다.

---

### [핵심]

주요 원인:

- Bean 등록 실패
- NoSuchBeanDefinitionException
- UnsatisfiedDependencyException
- Circular Dependency
- application.yml 오류
- 환경변수 누락
- Profile 설정 오류
- DB 연결 실패
- Entity Mapping 오류
- Repository Query Method 오류
- Port 충돌
- 의존성 누락

---

### [Troubleshooting]

Debug Flow:

```text
Startup Error Message 확인
→ Caused by 확인
→ 가장 아래쪽 원인 확인
→ Bean 이름 / Class 이름 확인
→ 설정 Key 확인
→ Profile 확인
→ DB 연결 확인
→ Repository Method 확인
→ 최근 변경 코드 확인
```

Port 충돌:

```text
문제:
Web server failed to start. Port 8080 was already in use.

원인:
이미 8080 port를 다른 process가 사용 중

해결:
기존 process 종료
또는 server.port 변경
```

환경변수 누락:

```text
문제:
Could not resolve placeholder 'DB_URL'

원인:
DB_URL 환경변수 미설정

해결:
환경변수 등록
또는 안전한 기본값 설정
또는 Profile 설정 확인
```

Repository Query Method 오류:

```text
문제:
No property 'xxx' found for type 'User'

원인:
Repository Query Method의 필드명이 Entity 필드명과 불일치

해결:
Entity 필드명 확인
Query Method 이름 수정
```

---

### [실무]

Startup Error 분석 기준:

- 에러 로그 첫 줄보다 `Caused by`를 우선 확인
- 마지막 `Caused by`가 실제 원인인 경우가 많음
- Bean 생성 실패는 의존성 체인을 따라 확인
- 설정 누락은 active profile과 환경변수 확인
- Repository 오류는 method 이름과 Entity 필드명 확인
- DB 오류는 URL, username, password, driver, DB 서버 상태 확인

---

### [FAQ]

Q. Spring Boot 실행이 안 되면 어디부터 봐?

A.
Console log의 `Caused by`를 확인하고 Bean, 설정, DB, Repository Query Method 순서로 원인을 좁히는 것이 좋다.

Q. Port 8080 충돌은 어떻게 해결해?

A.
기존 process를 종료하거나 `server.port` 설정을 다른 port로 변경한다.

Q. Could not resolve placeholder가 나오면?

A.
환경변수가 없거나 설정 key가 잘못된 것이다. active profile과 환경변수 등록 여부를 확인한다.

---

# 3. Bean / DI Troubleshooting

## 3.1 Bean Not Found

### [개념]

Bean Not Found는 Spring Container가 주입해야 할 Bean을 찾지 못하는 문제다.

주로 Annotation 누락, Component Scan 범위 오류, Profile 조건 불일치, Interface 구현체 누락으로 발생한다.

---

### [핵심]

대표 예외:

- NoSuchBeanDefinitionException
- UnsatisfiedDependencyException
- NoUniqueBeanDefinitionException
- BeanCreationException

원인:

- `@Service`, `@Component`, `@Repository` 누락
- Main Class 하위 패키지 밖에 위치
- `@Bean` 등록 누락
- Interface 구현체 없음
- 같은 타입 Bean이 여러 개
- Profile 조건 불일치
- Configuration class 미등록

---

### [Troubleshooting]

Debug Flow:

```text
필요한 Bean Type 확인
→ Bean으로 등록되어야 하는 class 확인
→ Annotation 확인
→ Package 위치 확인
→ Main Class 위치 확인
→ Profile 조건 확인
→ Interface 구현체 확인
→ 동일 타입 Bean 중복 확인
→ Configuration 확인
```

Annotation 누락:

```java
public class UserService {
}
```

개선:

```java
@Service
@RequiredArgsConstructor
public class UserService {
}
```

Package 위치 문제:

```text
com.example.project.ProjectApplication
com.example.other.UserService

문제:
UserService가 Component Scan 범위 밖일 수 있음

해결:
Main Class 하위 package로 이동
또는 ComponentScan 범위 명시
```

---

### [실무]

Bean 등록 기준:

- 직접 만든 Service는 `@Service`
- 일반 Component는 `@Component`
- 설정 class는 `@Configuration`
- 외부 라이브러리 객체는 `@Bean`
- Repository는 `JpaRepository` 상속
- Main Application Class는 최상위 패키지에 위치
- 생성자 주입으로 의존성 명확화

---

### [FAQ]

Q. NoSuchBeanDefinitionException이 나면 뭘 확인해?

A.
해당 class가 Bean으로 등록되었는지, Component Scan 범위 안에 있는지, 필요한 Profile이 활성화되어 있는지 확인한다.

Q. UnsatisfiedDependencyException은 뭐야?

A.
Bean 생성 중 필요한 의존성을 주입하지 못했다는 의미다. 누락된 Bean이나 순환 참조를 확인해야 한다.

Q. 같은 타입 Bean이 여러 개면 어떻게 해?

A.
`@Qualifier`, `@Primary`, Bean 이름 분리, 의존성 타입 구체화 등을 검토한다.

---

## 3.2 Circular Dependency

### [개념]

Circular Dependency는 Bean들이 서로를 의존해 생성 순환이 발생하는 문제다.

예:

```text
UserService
→ NotificationService
→ UserService
```

---

### [핵심]

문제점:

- Bean 생성 실패
- Service 책임 불명확
- 테스트 어려움
- 변경 영향 범위 증가
- 구조 복잡도 증가

주요 원인:

- Service 간 양방향 호출
- 공통 로직 분리 실패
- 비즈니스 흐름 조율 위치 불명확
- Utility 성격 로직을 Service에 넣음
- 이벤트 / 정책 Component 분리 부족

---

### [Troubleshooting]

Debug Flow:

```text
순환 참조 에러 로그 확인
→ AService와 BService 의존 방향 확인
→ 공통 로직 추출 가능성 확인
→ 책임 재분리
→ 별도 Component / Domain Service 검토
→ 이벤트 기반 분리 검토
→ @Lazy 임시 우회 여부 검토
```

나쁜 예:

```java
@Service
@RequiredArgsConstructor
public class UserService {

    private final NotificationService notificationService;
}
```

```java
@Service
@RequiredArgsConstructor
public class NotificationService {

    private final UserService userService;
}
```

개선 방향:

```text
공통 조회 로직 분리
→ UserReader Component 생성

알림 생성 흐름 분리
→ NotificationService가 UserRepository 직접 조회

후속 작업 분리
→ Domain Event 사용 검토
```

---

### [주의]

주의:

- `spring.main.allow-circular-references=true`로 해결하지 않음
- `@Lazy`는 임시 우회일 뿐 근본 해결 아님
- 순환 참조는 설계 책임 문제 신호로 봐야 함
- Service 간 호출 방향을 단방향으로 유지
- 공통 로직은 별도 Component로 분리

---

### [FAQ]

Q. 순환 참조가 생기면 어떻게 해결해?

A.
의존 방향과 책임을 다시 보고 공통 로직 분리, Service 재분리, 이벤트 구조를 검토하는 것이 좋다.

Q. @Lazy를 붙이면 해결된 거야?

A.
아니다. 일시적으로 Bean 생성을 우회할 수 있지만 설계 책임 문제는 남는다.

Q. 순환 참조를 허용하는 설정을 켜도 돼?

A.
권장하지 않는다. 구조 문제를 숨기기보다 의존 방향을 재설계하는 것이 좋다.

---

# 4. Controller / Mapping Troubleshooting

## 4.1 404 Not Found

### [개념]

404 Not Found는 요청 URL과 HTTP Method에 매칭되는 Controller Method를 찾지 못했거나, Security / Static Resource / SPA Routing 문제로 발생할 수 있다.

---

### [핵심]

원인:

- URL 오타
- HTTP Method 불일치
- `@RequestMapping` prefix 불일치
- Controller Method Mapping 누락
- Controller Bean 등록 실패
- Frontend baseURL 오류
- Axios path 오류
- Context Path 설정
- Security 설정
- SPA Routing과 API Routing 혼동

---

### [Troubleshooting]

Debug Flow:

```text
Frontend Request URL 확인
→ HTTP Method 확인
→ Backend server port 확인
→ Controller @RequestMapping 확인
→ Method Mapping 확인
→ PathVariable 확인
→ API base path 확인
→ Security 설정 확인
→ Controller Bean 등록 확인
```

예:

```java
@RestController
@RequestMapping("/api/festivals")
public class FestivalController {

    @GetMapping("/{festivalId}")
    public ApiResponse<FestivalResponse> getFestival(@PathVariable Long festivalId) {
        ...
    }
}
```

실제 호출 URL:

```text
GET /api/festival/1
```

문제:

```text
/api/festivals 와 /api/festival 불일치
```

해결:

```text
Frontend URL을 /api/festivals/1로 수정
또는 Controller prefix를 프로젝트 규칙에 맞게 통일
```

---

### [주의]

404 확인 시 주의:

- `/festival`과 `/festivals` 혼동
- `/api` prefix 누락
- `GET`과 `POST` Method 불일치
- PathVariable 이름과 URL segment 확인
- Frontend dev server proxy 설정 확인
- React SPA refresh 404와 Backend API 404 구분
- Security에서 차단된 경우 401 / 403 또는 404처럼 보일 수 있음

---

### [FAQ]

Q. 404가 나면 Controller가 없는 거야?

A.
아니다. URL, HTTP Method, prefix, Frontend baseURL, Security, SPA Routing 문제를 함께 확인해야 한다.

Q. Axios URL과 Controller URL은 어떻게 맞춰?

A.
Axios baseURL, Controller `@RequestMapping`, method mapping을 합친 최종 URL을 비교해야 한다.

Q. React 새로고침 404와 API 404는 달라?

A.
다르다. SPA Routing 404는 정적 파일 / index.html forwarding 문제이고 API 404는 Controller Mapping 문제일 수 있다.

---

## 4.2 405 Method Not Allowed

### [개념]

405 Method Not Allowed는 URL은 존재하지만 HTTP Method가 Controller Mapping과 맞지 않을 때 발생한다.

---

### [핵심]

원인:

- GET으로 보내야 하는데 POST로 호출
- POST API를 GET으로 호출
- PUT / PATCH 혼동
- Delete Method 누락
- HTML Form Method 제한
- Frontend Axios method 오류

---

### [Troubleshooting]

Debug Flow:

```text
Request Method 확인
→ Controller Mapping Annotation 확인
→ Frontend Axios method 확인
→ Browser Network 확인
→ API 문서 확인
```

예:

```java
@PostMapping("/posts")
public ApiResponse<PostResponse> createPost(@RequestBody PostCreateRequest request) {
    ...
}
```

잘못된 요청:

```text
GET /posts
```

해결:

```text
POST /posts로 요청
```

---

### [FAQ]

Q. 405는 무슨 뜻이야?

A.
요청 URL은 찾았지만 HTTP Method가 맞지 않는다는 의미다.

Q. 405가 나면 뭘 확인해?

A.
Frontend 요청 method와 Controller의 `@GetMapping`, `@PostMapping`, `@PatchMapping` 등을 비교한다.

---

# 5. Request Binding Troubleshooting

## 5.1 RequestBody 값이 null

### [개념]

RequestBody 값이 null로 들어오는 문제는 Client JSON이 Controller DTO로 제대로 Binding되지 않는 상황이다.

---

### [핵심]

원인:

- `@RequestBody` 누락
- JSON field name 불일치
- DTO field name 불일치
- Content-Type 누락
- JSON 문법 오류
- record / constructor binding 문제
- Getter / Setter 누락
- enum 값 불일치
- 날짜 포맷 불일치

---

### [Troubleshooting]

Debug Flow:

```text
Browser Network Payload 확인
→ Content-Type 확인
→ Controller Parameter Annotation 확인
→ DTO Field Name 확인
→ DTO Type 확인
→ JSON 문법 확인
→ Enum 값 확인
→ 날짜 포맷 확인
→ Validation Error 확인
```

나쁜 예:

```java
@PostMapping("/posts")
public ApiResponse<PostResponse> createPost(PostCreateRequest request) {
    ...
}
```

개선:

```java
@PostMapping("/posts")
public ApiResponse<PostResponse> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    ...
}
```

JSON:

```json
{
  "title": "제목",
  "content": "내용"
}
```

DTO:

```java
public record PostCreateRequest(
        String title,
        String content
) {
}
```

---

### [FAQ]

Q. RequestBody 값이 null이면 뭘 확인해?

A.
`@RequestBody` 누락, JSON 필드명, Content-Type, DTO 구조, Jackson 변환 오류를 확인한다.

Q. Query String을 @RequestBody로 받을 수 있어?

A.
아니다. Query String은 `@RequestParam` 또는 `@ModelAttribute`로 받는다.

Q. JSON 요청에는 Content-Type이 필요해?

A.
일반적으로 `Content-Type: application/json`이 필요하다.

---

## 5.2 RequestParam / PathVariable 혼동

### [개념]

`@RequestParam`은 Query String 값을 받고, `@PathVariable`은 URL 경로 일부를 받는다.

둘을 혼동하면 Binding Error나 400 / 404가 발생할 수 있다.

---

### [핵심]

구분:

| Annotation      | 위치                | 예                        |
| --------------- | ------------------- | ------------------------- |
| @PathVariable   | URL Path            | `/posts/1`                |
| @RequestParam   | Query String        | `/posts?category=NOTICE`  |
| @RequestBody    | JSON Body           | `{ "title": "..." }`      |
| @ModelAttribute | Query / Form Object | `/posts?keyword=a&page=0` |

---

### [실무]

PathVariable:

```java
@GetMapping("/posts/{postId}")
public ApiResponse<PostResponse> getPost(
        @PathVariable Long postId
) {
    ...
}
```

RequestParam:

```java
@GetMapping("/posts")
public ApiResponse<List<PostResponse>> getPosts(
        @RequestParam String category
) {
    ...
}
```

ModelAttribute:

```java
@GetMapping("/posts/search")
public ApiResponse<List<PostResponse>> searchPosts(
        @ModelAttribute PostSearchRequest request
) {
    ...
}
```

---

### [Troubleshooting]

문제: `Required request parameter 'postId' is not present`

```text
원인:
URL path에 있는 값을 @RequestParam으로 받으려 함

해결:
@PathVariable로 변경
또는 요청 URL을 query string으로 변경
```

문제: 404 발생

```text
원인:
Controller는 /posts/{postId}인데 요청은 /posts?postId=1

해결:
요청 URL 또는 Mapping 구조 통일
```

---

### [FAQ]

Q. @RequestParam과 @PathVariable 차이는?

A.
`@PathVariable`은 URL 경로 일부를 받고 `@RequestParam`은 query string 값을 받는다.

Q. 검색 조건 DTO는 뭘로 받아?

A.
Query parameter가 여러 개라면 `@ModelAttribute`로 SearchRequest DTO를 받을 수 있다.

---

# 6. Validation Troubleshooting

## 6.1 @Valid가 동작하지 않음

### [개념]

`@Valid`가 동작하지 않는 문제는 Request DTO에 Validation Annotation이 있어도 검증이 실행되지 않는 상황이다.

---

### [핵심]

원인:

- Controller parameter에 `@Valid` 누락
- Validation 의존성 누락
- Request DTO에 Annotation 누락
- `@RequestBody` 누락
- Parameter Validation에 `@Validated` 누락
- field type과 Annotation 부적합
- Validation Error Handler 없음

---

### [Troubleshooting]

Debug Flow:

```text
build.gradle validation 의존성 확인
→ DTO Validation Annotation 확인
→ Controller @Valid 확인
→ @RequestBody 확인
→ GlobalExceptionHandler 확인
→ MethodArgumentNotValidException 처리 확인
```

DTO:

```java
public record SignUpRequest(
        @Email String email,
        @NotBlank String password
) {
}
```

Controller:

```java
@PostMapping("/signup")
public ApiResponse<UserResponse> signUp(
        @Valid @RequestBody SignUpRequest request
) {
    return ApiResponse.success(userService.signUp(request));
}
```

---

### [주의]

Validation 주의:

- `@NotNull`은 빈 문자열을 막지 못함
- 문자열 필수 값은 `@NotBlank` 고려
- Collection은 `@NotEmpty` 또는 `@Size` 고려
- 숫자 양수는 `@Positive` 고려
- Request DTO와 Entity Validation 책임 구분
- Business Validation은 Service에서 처리

---

### [FAQ]

Q. @Valid가 안 먹으면 뭘 확인해?

A.
Validation 의존성, Controller parameter의 `@Valid`, Request DTO Annotation, `@RequestBody`, Exception Handler를 확인한다.

Q. @NotNull과 @NotBlank 차이는?

A.
`@NotNull`은 null만 막고, `@NotBlank`는 null과 빈 문자열, 공백 문자열을 막는다.

Q. 중복 이메일도 @Valid로 검증해?

A.
기초 구조에서는 Service에서 Repository를 통해 Business Validation으로 처리하는 것이 명확하다.

---

# 7. Repository / JPA Troubleshooting

## 7.1 Repository Query Method 오류

### [개념]

Repository Query Method 오류는 Spring Data JPA가 method 이름으로 Query를 생성하지 못할 때 발생한다.

주로 Entity 필드명 불일치나 Query Method 이름 오류가 원인이다.

---

### [핵심]

원인:

- Entity 필드명 오타
- 존재하지 않는 필드 사용
- 연관 Entity 필드 경로 오류
- Query Method 문법 오류
- 반환 타입 불일치
- Parameter 타입 불일치
- Query Method 이름 과도하게 복잡

---

### [Troubleshooting]

Debug Flow:

```text
에러 로그의 property name 확인
→ Repository method 이름 확인
→ Entity field name 확인
→ 연관 Entity field 확인
→ parameter type 확인
→ 반환 타입 확인
→ Query Method 단순화 검토
```

문제 예:

```java
public interface UserRepository extends JpaRepository<User, Long> {

    Optional<User> findByUserEmail(String email);
}
```

Entity:

```java
private String email;
```

문제:

```text
User Entity에는 userEmail 필드가 없음
```

개선:

```java
Optional<User> findByEmail(String email);
```

---

### [FAQ]

Q. No property found for type 오류는 뭐야?

A.
Repository Query Method에서 사용한 필드명이 Entity에 없다는 의미다.

Q. Query Method가 너무 길면?

A.
JPQL, QueryDSL, Custom Repository, SearchCondition DTO를 검토하는 것이 좋다.

---

## 7.2 LazyInitializationException

### [개념]

LazyInitializationException은 JPA Lazy Loading 대상 연관 Entity를 영속성 컨텍스트 밖에서 접근할 때 발생할 수 있다.

---

### [핵심]

발생 흐름:

```text
Service에서 Entity 조회
→ Transaction 종료
→ Controller에서 Entity 연관 필드 접근
→ LazyInitializationException
```

원인:

- Entity 직접 반환
- DTO 변환을 Transaction 밖에서 수행
- Lazy 연관 필드를 Controller에서 접근
- Open Session In View 의존
- 조회 전략 미설계

---

### [Troubleshooting]

Debug Flow:

```text
Entity 직접 반환 여부 확인
→ DTO 변환 위치 확인
→ Service readOnly Transaction 확인
→ Lazy field 접근 위치 확인
→ 필요한 연관 데이터 조회 전략 확인
→ N+1 문제 여부 확인
```

나쁜 예:

```java
@Transactional(readOnly = true)
public Post getPost(Long postId) {
    return postRepository.findById(postId).orElseThrow();
}
```

개선:

```java
@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException(ErrorCode.POST_NOT_FOUND));

    return PostResponse.from(post);
}
```

---

### [FAQ]

Q. LazyInitializationException은 왜 발생해?

A.
Transaction이나 영속성 컨텍스트가 종료된 뒤 Lazy 연관 필드에 접근하면 발생할 수 있다.

Q. LazyInitializationException은 어떻게 줄여?

A.
Service Transaction 안에서 필요한 데이터를 조회하고 Response DTO로 변환해 Controller에는 DTO만 반환한다.

Q. Entity 직접 반환이 문제야?

A.
그렇다. Lazy Loading, 순환 참조, 민감정보 노출, 응답 구조 불안정 문제가 생길 수 있다.

---

# 8. Transaction Troubleshooting

## 8.1 @Transactional이 동작하지 않음

### [개념]

`@Transactional`이 동작하지 않는 문제는 Transaction Proxy가 적용되지 않거나 rollback 조건이 맞지 않을 때 발생한다.

---

### [핵심]

원인:

- private method에 적용
- self-invocation
- Spring Bean이 아닌 객체 호출
- 예외 catch 후 삼킴
- checked exception rollback 오해
- readOnly Transaction에서 쓰기 시도
- Transaction 밖 Entity 변경
- final method / proxy 제약

---

### [Troubleshooting]

Debug Flow:

```text
@Transactional 위치 확인
→ method public 여부 확인
→ Spring Bean 호출 여부 확인
→ self-invocation 확인
→ Exception Type 확인
→ catch 후 다시 throw 여부 확인
→ rollbackFor 필요 여부 확인
→ Entity 영속 상태 확인
→ readOnly 여부 확인
```

Self-invocation 문제:

```java
public void updatePost(Long postId) {
    changePost(postId);
}

@Transactional
public void changePost(Long postId) {
    ...
}
```

개선 방향:

```text
@Transactional method를 외부 Bean에서 호출되도록 분리
또는 Transaction Boundary를 public Use Case method에 설정
```

---

### [FAQ]

Q. @Transactional이 안 먹는 가장 흔한 이유는?

A.
private method 적용, self-invocation, 예외 catch 후 삼킴, checked exception rollback 오해가 흔하다.

Q. 예외를 catch하면 rollback돼?

A.
catch 후 다시 던지지 않으면 Spring이 정상 종료로 판단할 수 있어 rollback되지 않을 수 있다.

Q. checked exception은 rollback돼?

A.
기본 rollback 대상이 아닐 수 있다. 필요하면 `rollbackFor` 설정을 검토한다.

---

# 9. CORS Troubleshooting

## 9.1 CORS Error

### [개념]

CORS Error는 브라우저가 다른 Origin의 요청을 보안 정책에 따라 차단하는 문제다.

Backend 서버가 정상 응답하더라도 브라우저가 응답을 차단할 수 있다.

---

### [핵심]

원인:

- allowed origin 불일치
- protocol 불일치
- port 불일치
- allowed method 누락
- allowed header 누락
- Authorization Header 미허용
- credentials 설정 불일치
- OPTIONS Preflight 차단
- Spring Security CORS 설정 누락
- Frontend baseURL 오류

---

### [Troubleshooting]

Debug Flow:

```text
Browser Network 확인
→ Request Origin 확인
→ Request URL 확인
→ Preflight OPTIONS 확인
→ Response Header 확인
→ allowed origin 확인
→ allowed method 확인
→ allowed header 확인
→ credentials 확인
→ SecurityFilterChain CORS 확인
```

Security 사용 시 확인:

```text
CorsConfigurationSource Bean 존재 여부
→ http.cors() 활성화 여부
→ OPTIONS 요청 인증 차단 여부
→ Authorization Header 허용 여부
```

---

### [실무]

문제 예:

```text
Frontend:
http://localhost:3000

Backend CORS:
http://localhost:5173
```

해결:

```text
allowedOrigins에 실제 Frontend Origin 등록
```

문제 예:

```text
Request Header:
Authorization: Bearer token

CORS allowed headers:
Content-Type만 허용
```

해결:

```text
Authorization Header 허용
```

---

### [FAQ]

Q. CORS 에러는 왜 Postman에서 안 나?

A.
CORS는 브라우저 보안 정책이므로 Postman에서는 차단되지 않을 수 있다.

Q. OPTIONS 요청이 실패하면?

A.
Preflight 요청이 차단된 것이다. CORS 설정과 SecurityFilterChain에서 OPTIONS 처리 여부를 확인해야 한다.

Q. CORS와 인증 문제는 어떻게 구분해?

A.
Browser Network에서 Preflight, Response Header, 401 / 403 여부를 함께 확인해야 한다.

---

# 10. Profile / Properties Troubleshooting

## 10.1 Profile 적용 오류

### [개념]

Profile 적용 오류는 기대한 환경 설정이 적용되지 않아 DB, CORS, Logging, External API 설정이 다르게 동작하는 문제다.

---

### [핵심]

원인:

- active profile 미설정
- 환경변수 누락
- profile 파일명 오타
- `application-prod.yml` 위치 오류
- 설정 override 순서 오해
- IDE 실행 설정과 터미널 실행 설정 차이
- test에서 prod profile 사용
- 배포 스크립트 profile 누락

---

### [Troubleshooting]

Debug Flow:

```text
Startup log에서 active profile 확인
→ SPRING_PROFILES_ACTIVE 확인
→ application-{profile}.yml 존재 확인
→ 설정 key 중복 확인
→ 실제 DB URL 확인
→ CORS Origin 확인
→ Logging Level 확인
→ IDE Run Configuration 확인
```

확인 로그:

```text
The following 1 profile is active: "local"
```

---

### [FAQ]

Q. 지금 Profile이 뭔지 어떻게 알아?

A.
Application startup log에서 active profile을 확인할 수 있다.

Q. IDE에서는 안 되고 터미널에서는 되면?

A.
IDE Run Configuration의 환경변수와 active profile 설정을 확인해야 한다.

Q. 테스트가 운영 DB에 붙으면?

A.
`@ActiveProfiles("test")`, test yml, datasource 환경변수, CI 설정을 즉시 확인해야 한다.

---

# 11. External API Troubleshooting

## 11.1 External API 호출 실패

### [개념]

External API 호출 실패는 외부 API 서버와 통신하는 과정에서 timeout, 인증 실패, 응답 파싱 실패, rate limit 등이 발생하는 문제다.

---

### [핵심]

원인:

- API Key 누락
- API Key 오타
- baseUrl 오류
- endpoint 오류
- request parameter 오류
- timeout
- network error
- 401 / 403 인증 실패
- 429 rate limit
- 500 external server error
- JSON parsing error
- 외부 API 스펙 변경

---

### [Troubleshooting]

Debug Flow:

```text
baseUrl 확인
→ endpoint 확인
→ API Key 환경변수 확인
→ request parameter 확인
→ 외부 API 문서 확인
→ response status 확인
→ response body 확인
→ timeout 확인
→ parsing DTO 확인
→ ExternalApiException 처리 확인
```

주의:

```text
API Key를 log에 그대로 남기지 않음
Authorization Header를 노출하지 않음
외부 API 원문 오류를 Client에 그대로 반환하지 않음
```

---

### [실무]

실패 처리 흐름:

```text
External API 호출
→ 실패 발생
→ ExternalApiClient에서 ExternalApiException 변환
→ GlobalExceptionHandler 처리
→ 통제된 Error Response 반환
→ 상세 원인은 서버 로그 확인
```

권장:

- 외부 API Client 분리
- timeout 설정
- ErrorCode 분리
- API Key 환경변수 관리
- Response DTO 분리
- 외부 API 스펙 변경 대비
- retry는 멱등성 확인 후 적용

---

### [FAQ]

Q. 외부 API가 실패하면 어디서 처리해?

A.
ExternalApiClient에서 내부 예외로 변환하고 GlobalExceptionHandler에서 통제된 Error Response로 처리하는 것이 좋다.

Q. API Key가 맞는데 401이 나면?

A.
환경변수 적용 여부, 실제 요청 Header / Parameter, API Key 종류, 도메인 제한, 외부 API 활성화 상태를 확인한다.

Q. 외부 API 응답 파싱이 실패하면?

A.
실제 response body와 Response DTO 필드명 / 타입이 일치하는지 확인해야 한다.

---

# 12. Spring Boot Anti Pattern

## 12.1 Layer Anti Pattern

### [개념]

Layer Anti Pattern은 Controller, Service, Repository, Entity, DTO 책임이 섞여 유지보수성과 테스트 가능성을 떨어뜨리는 구조다.

---

### [핵심]

대표 Layer Anti Pattern:

- Controller에 Business Logic 작성
- Controller에서 Repository 직접 호출
- Controller에서 Entity 생성 / 수정
- Service가 HTTP Request 객체에 직접 의존
- Repository에서 ApiResponse 반환
- Entity를 Response로 직접 반환
- Request DTO와 Response DTO 혼용
- DTO 없이 Entity를 API 입출력에 사용
- Repository에 Business Logic 작성
- 모든 기능을 하나의 Service에 몰아넣음

---

### [실무]

나쁜 예:

```java
@RestController
@RequiredArgsConstructor
public class PostController {

    private final PostRepository postRepository;

    @PostMapping("/posts")
    public Post createPost(@RequestBody Post request) {
        return postRepository.save(request);
    }
}
```

문제:

- Controller에서 Repository 직접 호출
- Entity를 RequestBody로 사용
- Entity를 Response로 반환
- Business Logic 없음
- Validation 없음
- Transaction Boundary 불명확

좋은 예:

```java
@PostMapping("/posts")
public ApiResponse<PostResponse> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    return ApiResponse.success(postService.createPost(request));
}
```

---

### [FAQ]

Q. Layer Anti Pattern 중 가장 흔한 것은?

A.
Controller에서 Repository를 직접 호출하고 Entity를 그대로 Request / Response에 사용하는 구조가 가장 흔하다.

Q. Entity를 RequestBody로 받으면 왜 안 좋아?

A.
API 입력 구조와 DB 구조가 강하게 결합되고 민감 필드 변경 위험이 생긴다.

Q. Entity를 Response로 반환하면 왜 안 좋아?

A.
민감정보 노출, Lazy Loading, 순환 참조, API 스펙 불안정 문제가 생길 수 있다.

---

## 12.2 Service Anti Pattern

### [개념]

Service Anti Pattern은 Service가 너무 많은 책임을 가지거나 Transaction, 예외 처리, DTO 변환 기준 없이 작성된 구조다.

---

### [핵심]

대표 Service Anti Pattern:

- method 이름이 process / handle뿐임
- 하나의 Service가 모든 도메인 처리
- 하나의 method가 여러 Use Case 처리
- Service에서 null 반환
- Optional.get 직접 사용
- RuntimeException만 무분별하게 사용
- ErrorCode 없음
- Transaction 없이 Entity 변경
- 외부 API와 DB 작업을 긴 Transaction으로 묶음
- Service 간 순환 참조
- HTTP Request / Response 객체 직접 의존

---

### [실무]

나쁜 예:

```java
public Object process(Long id, Object request) {
    ...
}
```

좋은 예:

```java
@Transactional
public PostResponse updatePost(Long postId, Long userId, PostUpdateRequest request) {
    ...
}
```

Service 개선 기준:

- method 이름은 Use Case 중심
- null 반환 금지
- Optional은 orElseThrow 처리
- CustomException 사용
- Transaction Boundary 명확화
- 책임이 커지면 Service 분리
- 외부 API Client 분리
- 순환 참조 제거

---

### [FAQ]

Q. Service가 너무 커지면 어떻게 해?

A.
Use Case 기준 Service 분리, Query Service 분리, ExternalApiClient 분리, Policy Component 분리를 검토한다.

Q. Service에서 null 반환은 왜 안 좋아?

A.
호출자가 추가 분기를 해야 하고 NPE 위험이 커지며 실패 의미가 명확하지 않다.

---

## 12.3 Configuration / Security / Logging Anti Pattern

### [개념]

Configuration, Security, Logging Anti Pattern은 운영 안정성과 보안을 해치는 설정 실수다.

---

### [핵심]

대표 Anti Pattern:

- API Key 하드코딩
- DB Password Git 커밋
- JWT Secret 기본값 운영 사용
- prod profile에서 ddl-auto create 사용
- 운영에서 debug logging 상시 활성화
- CORS 전체 허용
- credentials와 wildcard origin 조합
- Access Token 로그 기록
- Password 로그 기록
- Stack Trace Client 반환
- Exception message 그대로 Client 반환
- Security를 Frontend 상태에 의존
- RequestBody userId를 인증 사용자로 신뢰

---

### [실무]

나쁜 예:

```yaml
jwt:
  secret: my-real-secret-key

spring:
  jpa:
    hibernate:
      ddl-auto: create

logging:
  level:
    root: debug
```

문제:

- Secret 노출 위험
- 운영 DB schema 손상 위험
- 로그 과다 / 민감정보 노출 위험

좋은 방향:

```yaml
jwt:
  secret: ${JWT_SECRET}

spring:
  jpa:
    hibernate:
      ddl-auto: validate

logging:
  level:
    root: info
```

---

### [FAQ]

Q. 설정 Anti Pattern 중 가장 위험한 것은?

A.
민감정보를 코드나 Git에 남기고 운영 profile에서 위험한 설정을 사용하는 것이다.

Q. CORS를 전부 열면 보안상 안전하지 않아?

A.
운영에서는 필요한 Origin만 명확히 허용해야 한다. CORS는 인증 / 인가를 대체하지 않는다.

Q. 로그에 토큰을 남기면 왜 위험해?

A.
로그 유출 시 계정 탈취나 API 오남용으로 이어질 수 있다.

---

# 13. Troubleshooting Checklist

## 13.1 API Error Checklist

### [개념]

API Error Checklist는 Spring Boot API 호출 실패 시 Controller부터 Response까지 점검하는 기준이다.

---

### [핵심]

API Error Checklist:

```md
- [ ] 요청 URL이 맞는가?
- [ ] HTTP Method가 맞는가?
- [ ] Backend server port가 맞는가?
- [ ] Axios baseURL이 맞는가?
- [ ] Controller @RequestMapping prefix가 맞는가?
- [ ] Method Mapping이 맞는가?
- [ ] PathVariable 이름과 URL이 맞는가?
- [ ] RequestParam 이름이 맞는가?
- [ ] RequestBody에 @RequestBody가 붙어 있는가?
- [ ] Content-Type이 application/json인가?
- [ ] JSON field name이 DTO와 일치하는가?
- [ ] DTO field type이 요청 값과 맞는가?
- [ ] @Valid가 붙어 있는가?
- [ ] Validation Handler가 있는가?
- [ ] Service에서 CustomException을 사용하는가?
- [ ] Repository Optional.get을 직접 쓰지 않는가?
- [ ] Entity를 Response로 직접 반환하지 않는가?
- [ ] GlobalExceptionHandler가 있는가?
- [ ] Error Response 형식이 통일되어 있는가?
- [ ] Browser CORS Error 여부를 확인했는가?
```

---

### [실무]

API 오류 점검 흐름:

```text
Network Tab 확인
→ Request URL / Method 확인
→ Payload 확인
→ Response Status 확인
→ Backend Log 확인
→ Controller Mapping 확인
→ DTO Binding 확인
→ Service / Repository 확인
→ Exception Handler 확인
```

---

### [FAQ]

Q. API가 안 될 때 가장 먼저 확인할 것은?

A.
Browser Network 또는 Postman에서 실제 요청 URL, HTTP Method, Payload, Response Status를 먼저 확인한다.

Q. Backend 코드를 보기 전에 확인할 것은?

A.
Frontend baseURL, 요청 path, method, request body, header를 먼저 확인하는 것이 좋다.

---

## 13.2 Startup Checklist

### [개념]

Startup Checklist는 Spring Boot Application 실행 실패 시 점검하는 기준이다.

---

### [핵심]

Startup Checklist:

```md
- [ ] Console log의 Caused by를 확인했는가?
- [ ] active profile이 맞는가?
- [ ] application.yml indentation이 맞는가?
- [ ] 환경변수가 설정되어 있는가?
- [ ] DB URL / username / password가 맞는가?
- [ ] server port가 충돌하지 않는가?
- [ ] Component Scan 범위가 맞는가?
- [ ] Main Application Class 위치가 적절한가?
- [ ] @Service / @Component / @Configuration 누락이 없는가?
- [ ] Repository가 JpaRepository를 상속하는가?
- [ ] Entity에 @Entity와 @Id가 있는가?
- [ ] Repository Query Method 필드명이 Entity와 일치하는가?
- [ ] 순환 참조가 없는가?
- [ ] 필요한 dependency가 build.gradle에 있는가?
```

---

### [FAQ]

Q. 실행 실패 시 가장 중요한 로그는?

A.
`Caused by`를 확인하는 것이 중요하다. 가장 아래쪽 원인이 실제 문제인 경우가 많다.

Q. 설정 문제인지 코드 문제인지 어떻게 구분해?

A.
placeholder, profile, datasource, port 관련이면 설정 문제 가능성이 크고 Bean, Repository, Entity 관련이면 코드 구조 문제 가능성이 크다.

---

## 13.3 Layer Review Checklist

### [개념]

Layer Review Checklist는 Spring Boot Application이 Controller, Service, Repository, DTO 책임을 제대로 분리했는지 검수하는 기준이다.

---

### [핵심]

Layer Checklist:

```md
- [ ] Controller는 HTTP 요청 / 응답만 담당하는가?
- [ ] Controller에 Business Logic이 없는가?
- [ ] Controller가 Repository를 직접 호출하지 않는가?
- [ ] Service가 Business Logic을 담당하는가?
- [ ] Service method 이름이 Use Case를 표현하는가?
- [ ] Service에 Transaction Boundary가 있는가?
- [ ] Repository는 데이터 접근만 담당하는가?
- [ ] Repository가 ApiResponse를 반환하지 않는가?
- [ ] Entity를 RequestBody로 사용하지 않는가?
- [ ] Entity를 Response로 직접 반환하지 않는가?
- [ ] Request DTO와 Response DTO가 분리되어 있는가?
- [ ] Validation은 Request DTO에 적용되어 있는가?
- [ ] Business Validation은 Service에 있는가?
- [ ] CustomException과 ErrorCode를 사용하는가?
- [ ] GlobalExceptionHandler가 예외를 공통 처리하는가?
- [ ] Configuration 값이 코드에 하드코딩되어 있지 않은가?
- [ ] Logger를 사용하고 System.out.println을 제거했는가?
```

---

### [FAQ]

Q. Layer 검수에서 가장 먼저 볼 것은?

A.
Controller가 Repository를 직접 호출하지 않고 Service를 통해 Use Case를 처리하는지 먼저 확인한다.

Q. Spring Boot 코드 품질의 핵심은?

A.
Layer 책임 분리, DTO 경계, Transaction Boundary, 예외 처리 일관성, 설정 분리, 테스트 가능성이다.

---

# 14. Final Review Checklist

## 14.1 Spring Boot Final Checklist

### [개념]

Spring Boot Final Checklist는 Backend Agent가 Spring Boot 코드를 최종 생성 / 검수할 때 사용하는 종합 기준이다.

---

### [핵심]

Final Checklist:

```md
- [ ] Main Application Class가 최상위 패키지에 있는가?
- [ ] 패키지가 controller / service / repository / entity / dto / config / exception 기준으로 정리되어 있는가?
- [ ] Controller Thin Rule을 지키는가?
- [ ] Service에 Business Logic이 있는가?
- [ ] Repository는 Entity 중심 데이터 접근만 담당하는가?
- [ ] 생성자 주입을 사용하는가?
- [ ] Field Injection을 사용하지 않는가?
- [ ] 순환 참조가 없는가?
- [ ] Request DTO와 Response DTO가 분리되어 있는가?
- [ ] Entity 직접 Request / Response 사용을 피하는가?
- [ ] @Valid와 Validation Annotation이 적절한가?
- [ ] Validation과 Business Validation을 구분하는가?
- [ ] ApiResponse 또는 ErrorResponse Convention이 있는가?
- [ ] GlobalExceptionHandler가 있는가?
- [ ] CustomException과 ErrorCode가 있는가?
- [ ] Optional.get을 직접 사용하지 않는가?
- [ ] Service public method에 @Transactional이 있는가?
- [ ] 조회 method에 readOnly = true를 고려했는가?
- [ ] Transaction self-invocation 문제가 없는가?
- [ ] 외부 API 호출이 긴 Transaction 안에 있지 않은가?
- [ ] Repository Query Method가 과도하게 길지 않은가?
- [ ] Page / Slice 선택 기준이 명확한가?
- [ ] application.yml 또는 properties 설정이 정리되어 있는가?
- [ ] 민감정보가 환경변수로 관리되는가?
- [ ] Profile이 local / test / prod 기준으로 분리되어 있는가?
- [ ] CORS 설정이 Frontend Origin과 일치하는가?
- [ ] Spring Security 사용 시 CORS와 인증 예외 경계를 확인했는가?
- [ ] External API Client가 분리되어 있는가?
- [ ] Logging Level이 환경별로 적절한가?
- [ ] 로그에 민감정보가 남지 않는가?
- [ ] Controller / Service / Repository 테스트가 가능한 구조인가?
- [ ] Common Anti Pattern이 제거되었는가?
```

---

### [실무]

최종 검수 흐름:

```text
Project Structure
→ Layer Responsibility
→ DTO Boundary
→ Validation
→ Service Business Logic
→ Transaction
→ Repository Integration
→ Exception Handling
→ Configuration
→ CORS / Security
→ External API
→ Logging
→ Troubleshooting
→ Anti Pattern
→ Final Output
```

---

### [FAQ]

Q. Spring Boot 최종 검수에서 가장 중요한 것은?

A.
Layer 책임 분리, DTO 분리, Transaction Boundary, GlobalExceptionHandler, 설정 값 관리, Anti Pattern 제거다.

Q. Backend Agent가 Spring Boot 코드를 만들 때 반드시 지켜야 할 것은?

A.
Controller는 얇게, Service는 비즈니스 로직 중심, Repository는 데이터 접근 중심, DTO는 Entity와 분리, 예외와 응답은 일관되게 처리해야 한다.

---

# 15. Final Troubleshooting Flow

## 15.1 통합 Debug Flow

### [개념]

통합 Debug Flow는 Spring Boot 문제를 빠르게 분류하기 위한 최종 점검 흐름이다.

---

### [Flow]

```text
문제 발생
→ Application이 실행되는가?
    → 아니오: Startup Checklist
    → 예: 다음 단계

→ 요청이 Backend까지 도달하는가?
    → 아니오: URL / Port / Proxy / CORS 확인
    → 예: 다음 단계

→ Controller Mapping이 맞는가?
    → 아니오: 404 / 405 Troubleshooting
    → 예: 다음 단계

→ Request Binding이 성공하는가?
    → 아니오: RequestBody / RequestParam / PathVariable 확인
    → 예: 다음 단계

→ Validation을 통과하는가?
    → 아니오: Validation Handler 확인
    → 예: 다음 단계

→ Service Business Logic이 성공하는가?
    → 아니오: BusinessException / ErrorCode 확인
    → 예: 다음 단계

→ Repository Query가 성공하는가?
    → 아니오: Query Method / DB / Entity 확인
    → 예: 다음 단계

→ Transaction이 기대대로 동작하는가?
    → 아니오: @Transactional / rollback / self-invocation 확인
    → 예: 다음 단계

→ Response가 일관적인가?
    → 아니오: DTO / ApiResponse / ExceptionHandler 확인
    → 예: 완료
```

---

### [핵심]

문제별 우선 확인:

| 증상          | 우선 확인                      |
| ------------- | ------------------------------ |
| 실행 실패     | Startup log, Caused by         |
| Bean 오류     | Annotation, Scan 범위, DI      |
| 404           | URL, Method, Mapping           |
| 405           | HTTP Method                    |
| 400           | DTO Binding, Validation        |
| 401           | Authentication                 |
| 403           | Authorization                  |
| 500           | Service, Repository, Exception |
| CORS          | Origin, Header, Preflight      |
| DB 반영 안 됨 | Transaction, Dirty Checking    |
| Lazy 오류     | DTO 변환 위치, Transaction     |
| 설정 누락     | Profile, Environment Variable  |
| 외부 API 실패 | API Key, baseUrl, response     |

---

### [FAQ]

Q. 통합 Debug Flow는 언제 써?

A.
오류 원인이 명확하지 않을 때 실행 여부, 요청 도달, Mapping, Binding, Validation, Service, Repository, Transaction 순서로 원인을 좁힐 때 사용한다.

Q. 에러 코드만 보고 바로 수정해도 돼?

A.
가능하지만 같은 상태 코드라도 원인이 다양하므로 요청, 로그, Layer 흐름을 함께 확인하는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Spring Boot 문제는 어디서부터 확인해?
A. 요청 URL, HTTP Method, Controller Mapping, Request Binding, Validation, Service, Repository, Exception Handler 순서로 확인하는 것이 좋다.

Q. Spring Boot 실행이 안 되면 어디부터 봐?
A. Console log의 Caused by를 확인하고 Bean, 설정, DB, Repository Query Method 순서로 원인을 좁히는 것이 좋다.

Q. Port 8080 충돌은 어떻게 해결해?
A. 기존 process를 종료하거나 server.port 설정을 다른 port로 변경한다.

Q. Could not resolve placeholder가 나오면?
A. 환경변수가 없거나 설정 key가 잘못된 것이다. active profile과 환경변수 등록 여부를 확인한다.

Q. NoSuchBeanDefinitionException이 나면 뭘 확인해?
A. 해당 class가 Bean으로 등록되었는지, Component Scan 범위 안에 있는지, 필요한 Profile이 활성화되어 있는지 확인한다.

Q. UnsatisfiedDependencyException은 뭐야?
A. Bean 생성 중 필요한 의존성을 주입하지 못했다는 의미다. 누락된 Bean이나 순환 참조를 확인해야 한다.

Q. 같은 타입 Bean이 여러 개면 어떻게 해?
A. @Qualifier, @Primary, Bean 이름 분리, 의존성 타입 구체화 등을 검토한다.

Q. 순환 참조가 생기면 어떻게 해결해?
A. 의존 방향과 책임을 다시 보고 공통 로직 분리, Service 재분리, 이벤트 구조를 검토하는 것이 좋다.

Q. @Lazy를 붙이면 순환 참조가 해결된 거야?
A. 아니다. 일시적으로 Bean 생성을 우회할 수 있지만 설계 책임 문제는 남는다.

Q. 404가 나면 Controller가 없는 거야?
A. 아니다. URL, HTTP Method, prefix, Frontend baseURL, Security, SPA Routing 문제를 함께 확인해야 한다.

Q. Axios URL과 Controller URL은 어떻게 맞춰?
A. Axios baseURL, Controller @RequestMapping, method mapping을 합친 최종 URL을 비교해야 한다.

Q. React 새로고침 404와 API 404는 달라?
A. 다르다. SPA Routing 404는 정적 파일 / index.html forwarding 문제이고 API 404는 Controller Mapping 문제일 수 있다.

Q. 405는 무슨 뜻이야?
A. 요청 URL은 찾았지만 HTTP Method가 맞지 않는다는 의미다.

Q. 405가 나면 뭘 확인해?
A. Frontend 요청 method와 Controller의 @GetMapping, @PostMapping, @PatchMapping 등을 비교한다.

Q. RequestBody 값이 null이면 뭘 확인해?
A. @RequestBody 누락, JSON 필드명, Content-Type, DTO 구조, Jackson 변환 오류를 확인한다.

Q. Query String을 @RequestBody로 받을 수 있어?
A. 아니다. Query String은 @RequestParam 또는 @ModelAttribute로 받는다.

Q. JSON 요청에는 Content-Type이 필요해?
A. 일반적으로 Content-Type: application/json이 필요하다.

Q. @RequestParam과 @PathVariable 차이는?
A. @PathVariable은 URL 경로 일부를 받고 @RequestParam은 query string 값을 받는다.

Q. 검색 조건 DTO는 뭘로 받아?
A. Query parameter가 여러 개라면 @ModelAttribute로 SearchRequest DTO를 받을 수 있다.

Q. @Valid가 안 먹으면 뭘 확인해?
A. Validation 의존성, Controller parameter의 @Valid, Request DTO Annotation, @RequestBody, Exception Handler를 확인한다.

Q. @NotNull과 @NotBlank 차이는?
A. @NotNull은 null만 막고, @NotBlank는 null과 빈 문자열, 공백 문자열을 막는다.

Q. 중복 이메일도 @Valid로 검증해?
A. 기초 구조에서는 Service에서 Repository를 통해 Business Validation으로 처리하는 것이 명확하다.

Q. No property found for type 오류는 뭐야?
A. Repository Query Method에서 사용한 필드명이 Entity에 없다는 의미다.

Q. Query Method가 너무 길면?
A. JPQL, QueryDSL, Custom Repository, SearchCondition DTO를 검토하는 것이 좋다.

Q. LazyInitializationException은 왜 발생해?
A. Transaction이나 영속성 컨텍스트가 종료된 뒤 Lazy 연관 필드에 접근하면 발생할 수 있다.

Q. LazyInitializationException은 어떻게 줄여?
A. Service Transaction 안에서 필요한 데이터를 조회하고 Response DTO로 변환해 Controller에는 DTO만 반환한다.

Q. Entity 직접 반환이 문제야?
A. 그렇다. Lazy Loading, 순환 참조, 민감정보 노출, 응답 구조 불안정 문제가 생길 수 있다.

Q. @Transactional이 안 먹는 가장 흔한 이유는?
A. private method 적용, self-invocation, 예외 catch 후 삼킴, checked exception rollback 오해가 흔하다.

Q. 예외를 catch하면 rollback돼?
A. catch 후 다시 던지지 않으면 Spring이 정상 종료로 판단할 수 있어 rollback되지 않을 수 있다.

Q. checked exception은 rollback돼?
A. 기본 rollback 대상이 아닐 수 있다. 필요하면 rollbackFor 설정을 검토한다.

Q. CORS 에러는 왜 Postman에서 안 나?
A. CORS는 브라우저 보안 정책이므로 Postman에서는 차단되지 않을 수 있다.

Q. OPTIONS 요청이 실패하면?
A. Preflight 요청이 차단된 것이다. CORS 설정과 SecurityFilterChain에서 OPTIONS 처리 여부를 확인해야 한다.

Q. CORS와 인증 문제는 어떻게 구분해?
A. Browser Network에서 Preflight, Response Header, 401 / 403 여부를 함께 확인해야 한다.

Q. 지금 Profile이 뭔지 어떻게 알아?
A. Application startup log에서 active profile을 확인할 수 있다.

Q. IDE에서는 안 되고 터미널에서는 되면?
A. IDE Run Configuration의 환경변수와 active profile 설정을 확인해야 한다.

Q. 테스트가 운영 DB에 붙으면?
A. @ActiveProfiles("test"), test yml, datasource 환경변수, CI 설정을 즉시 확인해야 한다.

Q. 외부 API가 실패하면 어디서 처리해?
A. ExternalApiClient에서 내부 예외로 변환하고 GlobalExceptionHandler에서 통제된 Error Response로 처리하는 것이 좋다.

Q. API Key가 맞는데 401이 나면?
A. 환경변수 적용 여부, 실제 요청 Header / Parameter, API Key 종류, 도메인 제한, 외부 API 활성화 상태를 확인한다.

Q. 외부 API 응답 파싱이 실패하면?
A. 실제 response body와 Response DTO 필드명 / 타입이 일치하는지 확인해야 한다.

Q. Layer Anti Pattern 중 가장 흔한 것은?
A. Controller에서 Repository를 직접 호출하고 Entity를 그대로 Request / Response에 사용하는 구조가 가장 흔하다.

Q. Entity를 RequestBody로 받으면 왜 안 좋아?
A. API 입력 구조와 DB 구조가 강하게 결합되고 민감 필드 변경 위험이 생긴다.

Q. Entity를 Response로 반환하면 왜 안 좋아?
A. 민감정보 노출, Lazy Loading, 순환 참조, API 스펙 불안정 문제가 생길 수 있다.

Q. Service가 너무 커지면 어떻게 해?
A. Use Case 기준 Service 분리, Query Service 분리, ExternalApiClient 분리, Policy Component 분리를 검토한다.

Q. Service에서 null 반환은 왜 안 좋아?
A. 호출자가 추가 분기를 해야 하고 NPE 위험이 커지며 실패 의미가 명확하지 않다.

Q. 설정 Anti Pattern 중 가장 위험한 것은?
A. 민감정보를 코드나 Git에 남기고 운영 profile에서 위험한 설정을 사용하는 것이다.

Q. CORS를 전부 열면 보안상 안전하지 않아?
A. 운영에서는 필요한 Origin만 명확히 허용해야 한다. CORS는 인증 / 인가를 대체하지 않는다.

Q. 로그에 토큰을 남기면 왜 위험해?
A. 로그 유출 시 계정 탈취나 API 오남용으로 이어질 수 있다.

Q. API가 안 될 때 가장 먼저 확인할 것은?
A. Browser Network 또는 Postman에서 실제 요청 URL, HTTP Method, Payload, Response Status를 먼저 확인한다.

Q. Backend 코드를 보기 전에 확인할 것은?
A. Frontend baseURL, 요청 path, method, request body, header를 먼저 확인하는 것이 좋다.

Q. 실행 실패 시 가장 중요한 로그는?
A. Caused by를 확인하는 것이 중요하다. 가장 아래쪽 원인이 실제 문제인 경우가 많다.

Q. Layer 검수에서 가장 먼저 볼 것은?
A. Controller가 Repository를 직접 호출하지 않고 Service를 통해 Use Case를 처리하는지 먼저 확인한다.

Q. Spring Boot 코드 품질의 핵심은?
A. Layer 책임 분리, DTO 경계, Transaction Boundary, 예외 처리 일관성, 설정 분리, 테스트 가능성이다.

Q. Spring Boot 최종 검수에서 가장 중요한 것은?
A. Layer 책임 분리, DTO 분리, Transaction Boundary, GlobalExceptionHandler, 설정 값 관리, Anti Pattern 제거다.

Q. Backend Agent가 Spring Boot 코드를 만들 때 반드시 지켜야 할 것은?
A. Controller는 얇게, Service는 비즈니스 로직 중심, Repository는 데이터 접근 중심, DTO는 Entity와 분리, 예외와 응답은 일관되게 처리해야 한다.

Q. 통합 Debug Flow는 언제 써?
A. 오류 원인이 명확하지 않을 때 실행 여부, 요청 도달, Mapping, Binding, Validation, Service, Repository, Transaction 순서로 원인을 좁힐 때 사용한다.

Q. 에러 코드만 보고 바로 수정해도 돼?
A. 가능하지만 같은 상태 코드라도 원인이 다양하므로 요청, 로그, Layer 흐름을 함께 확인하는 것이 좋다.
