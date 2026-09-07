# Spring Boot Part01 - Application Structure & Layered Architecture

---

# 1. Spring Boot Application Structure

## 1.1 Spring Boot Application Structure

### [개념]

Spring Boot Application Structure는 Backend Application을 책임 기준으로 나누는 기본 패키지 구조다.

Spring Boot 구조는 단순 폴더 정리가 아니다.

목적:

- Component Scan 안정화
- Layer Responsibility 분리
- Controller / Service / Repository 역할 구분
- DTO / Entity 경계 분리
- Configuration / Exception 관리
- Backend Agent 코드 생성 기준 제공
- Review Agent 구조 검수 기준 제공

Spring Boot Application Structure는 Backend Application의 유지보수성과 테스트 가능성을 결정한다.

---

### [핵심]

기본 패키지 구조:

```text
src/main/java/com/example/project
├ ProjectApplication.java
├ config
├ controller
├ service
├ repository
├ entity
├ dto
│ ├ request
│ └ response
├ exception
├ common
└ util
```

핵심 규칙:

- Main Application Class는 최상위 패키지에 둔다.
- Controller는 HTTP 요청 / 응답을 담당한다.
- Service는 Business Logic과 Transaction Boundary를 담당한다.
- Repository는 Data Access를 담당한다.
- Entity는 Database / Domain Model을 표현한다.
- DTO는 API Request / Response 경계에서 사용한다.
- Configuration Class는 config 패키지에 둔다.
- Exception / ErrorCode / GlobalExceptionHandler는 exception 또는 common 패키지에 둔다.
- Entity를 Controller Response로 직접 반환하지 않는다.
- Controller에서 Repository를 직접 호출하지 않는다.

---

### [실무]

2026 실무 기준 Spring Boot Application은 Layered Architecture를 기본으로 잡고, 규모가 커질수록 Domain Package 또는 Feature Package 구조로 확장한다.

초기 프로젝트 권장 구조:

```text
com.example.project
├ ProjectApplication.java
├ config
│ ├ WebConfig.java
│ └ CorsConfig.java
├ controller
│ └ PostController.java
├ service
│ └ PostService.java
├ repository
│ └ PostRepository.java
├ entity
│ └ Post.java
├ dto
│ ├ request
│ │ └ PostCreateRequest.java
│ └ response
│   └ PostResponse.java
├ exception
│ ├ GlobalExceptionHandler.java
│ ├ BusinessException.java
│ └ ErrorCode.java
└ common
  └ ApiResponse.java
```

권장 판단 기준:

| 규모                 | 추천 구조            | 설명                                 |
| -------------------- | -------------------- | ------------------------------------ |
| 학습 / 소형 프로젝트 | Layer Package        | controller, service, repository 중심 |
| 중형 프로젝트        | Domain + Layer 혼합  | post/controller, post/service 등     |
| 대형 프로젝트        | Domain Package       | domain별 책임 분리                   |
| MSA / Expert         | Bounded Context 기준 | 별도 Expert Rules 참조               |

주의:

- 처음부터 과도한 DDD 구조를 적용하지 않는다.
- Foundation 단계에서는 Layer 구조가 가장 이해하기 쉽다.
- 팀 프로젝트에서는 패키지 규칙을 먼저 정한다.
- 패키지 이름은 소문자 기준으로 통일한다.
- dto.request / dto.response 분리를 우선 적용한다.
- common, util 남용을 피한다.

---

### [FAQ]

Q. Spring Boot 패키지 구조는 어떻게 잡아?
A. 기초 단계에서는 controller, service, repository, entity, dto, config, exception 중심의 Layer 구조가 좋다.

Q. Main Application Class는 어디에 둬야 해?
A. Component Scan을 위해 최상위 패키지에 두는 것이 좋다.

Q. DTO와 Entity는 같은 패키지에 둬도 돼?
A. 가능은 하지만 역할이 다르므로 dto와 entity를 분리하는 것이 유지보수에 좋다.

Q. common 패키지는 언제 써?
A. ApiResponse, 공통 상수, 공통 유틸처럼 여러 계층에서 재사용되는 요소에 사용한다.

Q. util 패키지는 많이 만들어도 돼?
A. 남용하면 책임이 흐려진다. 먼저 Service, Domain, Component 책임으로 둘 수 있는지 검토한다.

---

# 2. Main Application Class

## 2.1 Main Application Class Rules

### [개념]

Main Application Class는 Spring Boot Application의 시작점이다.

`@SpringBootApplication`은 Spring Boot 실행에 필요한 핵심 Annotation이다.

`@SpringBootApplication`은 아래 기능을 포함한다.

- `@SpringBootConfiguration`
- `@EnableAutoConfiguration`
- `@ComponentScan`

Spring Boot는 Main Application Class가 위치한 패키지를 기준으로 하위 패키지를 Component Scan한다.

---

### [핵심]

핵심 키워드:

- Main Application Class
- `@SpringBootApplication`
- `SpringApplication.run`
- Component Scan
- Auto Configuration
- Application Entry Point
- Base Package

기본 코드:

```java
@SpringBootApplication
public class ProjectApplication {

    public static void main(String[] args) {
        SpringApplication.run(ProjectApplication.class, args);
    }
}
```

위치 규칙:

```text
좋음:
com.example.project.ProjectApplication
com.example.project.controller.PostController
com.example.project.service.PostService

나쁨:
com.example.project.app.ProjectApplication
com.example.project.controller.PostController
```

나쁜 구조의 문제:

- controller 패키지가 Component Scan 범위 밖일 수 있음
- Service Bean 등록 실패 가능
- Repository Bean 주입 실패 가능
- `NoSuchBeanDefinitionException` 발생 가능

---

### [실무]

Main Application Class는 프로젝트 Root Package에 둔다.

권장:

```text
com.company.project
├ ProjectApplication.java
├ controller
├ service
├ repository
└ entity
```

비권장:

```text
com.company.project.app
└ ProjectApplication.java

com.company.project.controller
└ PostController.java
```

Component Scan 문제 발생 시 확인 순서:

```text
Bean 등록 오류 발생
→ Main Application Class 위치 확인
→ 대상 Class 패키지 위치 확인
→ Annotation 확인
→ Profile 조건 확인
→ Configuration 확인
```

Main Class 위치가 잘못된 경우 해결:

```java
@SpringBootApplication(scanBasePackages = "com.company.project")
public class ProjectApplication {
}
```

단, Foundation 기준에서는 `scanBasePackages`를 쓰기보다 패키지 구조를 올바르게 잡는 것을 우선한다.

---

### [FAQ]

Q. `@SpringBootApplication`은 뭐야?
A. Spring Boot Application 시작 Annotation이며 Component Scan, Auto Configuration, Configuration 역할을 포함한다.

Q. Main Class 위치가 중요한 이유는?
A. 기본 Component Scan이 Main Class가 있는 패키지 하위 기준으로 동작하기 때문이다.

Q. Bean 등록이 안 되면 Main Class 위치도 확인해야 해?
A. 맞다. 대상 클래스가 Main Class 하위 패키지에 있는지 확인해야 한다.

Q. `scanBasePackages`를 쓰면 되지 않아?
A. 가능하지만 기본 구조를 올바르게 잡는 것이 우선이다. 복잡한 Scan 설정은 구조 문제를 숨길 수 있다.

---

# 3. Layered Architecture

## 3.1 Layered Architecture Overview

### [개념]

Layered Architecture는 Backend Application을 책임별 계층으로 나누는 구조다.

기본 흐름:

```text
Client
→ Controller
→ Service
→ Repository
→ Database
```

Layered Architecture의 목적:

- HTTP 책임과 Business Logic 분리
- Business Logic과 Data Access 분리
- Transaction Boundary 명확화
- DTO와 Entity 경계 분리
- 테스트 가능한 코드 구조 생성
- 변경 영향 범위 축소
- Review Agent가 Anti Pattern을 탐지할 수 있는 기준 제공

---

### [핵심]

Layer 책임:

| Layer      | 주요 책임                                                 | 금지                         |
| ---------- | --------------------------------------------------------- | ---------------------------- |
| Controller | HTTP 요청 / 응답, DTO 수신, Validation Trigger            | Business Logic, DB 직접 접근 |
| Service    | Business Logic, Transaction, Entity 변경, Repository 조합 | HTTP Request 직접 처리       |
| Repository | Entity 저장 / 조회 / 삭제, Query Method                   | Business Decision            |
| Entity     | Domain Data, 상태 변경 메서드                             | API Response 직접 노출       |
| DTO        | Request / Response 데이터 전달                            | Business Logic 과다 포함     |
| Config     | Bean / Web / Security / CORS 설정                         | Business Logic               |
| Exception  | ErrorCode, CustomException, GlobalExceptionHandler        | 정상 로직 처리               |

기본 흐름:

```text
HTTP Request
→ Controller
→ Request DTO
→ Service
→ Repository
→ Entity
→ Service
→ Response DTO
→ Controller
→ ApiResponse
→ HTTP Response
```

---

### [실무]

Controller 예:

```java
@RestController
@RequestMapping("/api/posts")
@RequiredArgsConstructor
public class PostController {

    private final PostService postService;

    @PostMapping
    public ApiResponse<PostResponse> createPost(
            @Valid @RequestBody PostCreateRequest request
    ) {
        return ApiResponse.success(postService.createPost(request));
    }
}
```

Service 예:

```java
@Service
@RequiredArgsConstructor
public class PostService {

    private final PostRepository postRepository;

    @Transactional
    public PostResponse createPost(PostCreateRequest request) {
        Post post = Post.create(request.title(), request.content());
        Post savedPost = postRepository.save(post);

        return PostResponse.from(savedPost);
    }
}
```

Repository 예:

```java
public interface PostRepository extends JpaRepository<Post, Long> {
}
```

권장:

- Controller는 Service만 호출한다.
- Service는 Repository를 조합한다.
- Repository는 Entity 중심으로 동작한다.
- Entity는 내부 Domain Model로 유지한다.
- Response DTO 변환 기준을 통일한다.
- 예외는 Service에서 발생시키고 GlobalExceptionHandler에서 처리한다.

비권장:

```java
@RestController
@RequiredArgsConstructor
public class PostController {

    private final PostRepository postRepository;

    @PostMapping("/posts")
    public Post createPost(@RequestBody Post post) {
        return postRepository.save(post);
    }
}
```

문제:

- Controller에서 Repository 직접 호출
- Entity를 RequestBody로 직접 수신
- Entity를 Response로 직접 반환
- Validation 경계 불명확
- Business Logic 위치 불명확
- Transaction Boundary 불명확

---

### [FAQ]

Q. Layered Architecture는 왜 써?
A. HTTP 처리, 비즈니스 로직, 데이터 접근 책임을 분리해 유지보수와 테스트를 쉽게 하기 위해 사용한다.

Q. Controller에서 Repository를 바로 호출해도 돼?
A. 간단한 예제에서는 가능하지만 실무 구조에서는 Service를 거쳐 비즈니스 로직과 트랜잭션 경계를 관리하는 것이 좋다.

Q. Service는 왜 필요해?
A. 비즈니스 로직, 트랜잭션, 여러 Repository 조합, 예외 처리를 Controller에서 분리하기 위해 필요하다.

Q. Entity를 Controller에서 바로 반환하면 안 돼?
A. Lazy Loading, 순환 참조, 민감정보 노출, API 변경 위험이 생길 수 있으므로 Response DTO로 변환하는 것이 좋다.

---

## 3.2 Request Flow in Layered Architecture

### [개념]

Request Flow는 HTTP 요청이 Spring Boot Application 내부 계층을 거쳐 응답으로 반환되는 흐름이다.

Spring MVC 기반 요청 흐름:

```text
HTTP Request
→ DispatcherServlet
→ HandlerMapping
→ Controller
→ Service
→ Repository
→ Database
→ Repository
→ Service
→ Controller
→ MessageConverter
→ HTTP Response
```

Layered Architecture 내부 흐름:

```text
Client Request
→ Controller
→ Service
→ Repository
→ Database
→ Service
→ Controller
→ Client Response
```

---

### [핵심]

요청 처리 기준:

- URL / HTTP Method는 Controller Mapping에서 처리한다.
- JSON Body는 Request DTO로 Binding한다.
- Request Validation은 Controller 경계에서 Trigger한다.
- Business Validation은 Service에서 처리한다.
- Entity 조회 / 저장은 Repository가 담당한다.
- Transaction Boundary는 Service에서 관리한다.
- Response DTO는 Entity 직접 노출을 방지한다.
- ApiResponse는 응답 형식을 통일한다.
- Exception은 GlobalExceptionHandler에서 처리한다.

오류 분석 순서:

```text
URL / Method 확인
→ Controller Mapping 확인
→ Request Parameter / Body 확인
→ DTO Binding 확인
→ Validation 확인
→ Service Logic 확인
→ Repository Query 확인
→ Exception Handler 확인
→ Response 확인
```

---

### [실무]

404 분석:

```text
Frontend Request URL
→ Axios baseURL
→ Controller @RequestMapping
→ Method Mapping
→ HTTP Method
→ Security 차단 여부
```

400 분석:

```text
Request Body
→ Content-Type
→ @RequestBody
→ DTO Field Name
→ DTO Field Type
→ Validation Annotation
```

500 분석:

```text
Service Logic
→ Repository Query
→ Null Handling
→ Transaction
→ External API
→ GlobalExceptionHandler
→ Server Log
```

401 / 403 분석:

```text
Authorization Header
→ JWT Filter
→ Authentication
→ SecurityContext
→ Authorization Rule
→ Controller Principal
```

Foundation 문서에서는 Security Filter Chain 심화는 다루지 않는다.

Security 심화는 Security Advanced Domain Rules에서 처리한다.

---

### [FAQ]

Q. Spring Boot 요청 흐름은 어떻게 돼?
A. HTTP 요청이 DispatcherServlet을 거쳐 Controller, Service, Repository로 전달되고 다시 응답으로 반환된다.

Q. 404가 나면 뭘 확인해?
A. URL, HTTP Method, Controller prefix, Method Mapping, Frontend baseURL, Security 차단 여부를 확인한다.

Q. 400 Bad Request가 나면 뭘 확인해?
A. Request Body, Content-Type, DTO 필드명, 타입 변환, Validation 실패 여부를 확인한다.

Q. 500 에러가 나면 어디부터 봐?
A. Service Logic, Repository Query, Null 처리, Transaction, External API, Server Log 순서로 확인한다.

---

# 4. Layer Responsibility Rules

## 4.1 Controller Responsibility

### [개념]

Controller는 HTTP 요청과 응답을 처리하는 Layer다.

Controller는 Business Logic을 직접 수행하지 않는다.

Controller의 목적:

- URL Mapping
- HTTP Method Mapping
- Request DTO 수신
- Validation Trigger
- Authentication Principal 수신
- Service 호출
- Response DTO 반환
- ApiResponse 반환

---

### [핵심]

Controller 책임:

- `@RestController`
- `@RequestMapping`
- `@GetMapping`
- `@PostMapping`
- `@PutMapping`
- `@PatchMapping`
- `@DeleteMapping`
- `@RequestBody`
- `@RequestParam`
- `@PathVariable`
- `@ModelAttribute`
- `@Valid`
- Service 호출
- ApiResponse 반환

Controller 금지:

- Repository 직접 호출
- Entity 직접 저장
- Entity 직접 반환
- Business Logic 작성
- 복잡한 조건문 작성
- Transaction 처리
- 외부 API 직접 호출
- try-catch 반복 처리

---

### [실무]

좋은 Controller:

```java
@RestController
@RequestMapping("/api/users")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    @PatchMapping("/{userId}")
    public ApiResponse<UserResponse> updateUser(
            @PathVariable Long userId,
            @Valid @RequestBody UserUpdateRequest request
    ) {
        return ApiResponse.success(userService.updateUser(userId, request));
    }
}
```

나쁜 Controller:

```java
@RestController
@RequiredArgsConstructor
public class UserController {

    private final UserRepository userRepository;

    @PatchMapping("/users/{userId}")
    public User updateUser(
            @PathVariable Long userId,
            @RequestBody UserUpdateRequest request
    ) {
        User user = userRepository.findById(userId).orElseThrow();
        user.setNickname(request.nickname());
        return userRepository.save(user);
    }
}
```

문제:

- Controller에서 Repository 직접 호출
- Business Logic 위치 오류
- Entity 직접 반환
- Transaction Boundary 불명확
- Exception Handling 불명확

---

### [FAQ]

Q. Controller는 어디까지 해야 해?
A. 요청을 받고 검증을 트리거한 뒤 Service를 호출하고 응답을 반환하는 정도가 적합하다.

Q. Controller에 비즈니스 로직이 많으면 왜 문제야?
A. 테스트가 어려워지고 HTTP 책임과 비즈니스 책임이 섞여 유지보수가 어려워진다.

Q. Controller에서 try-catch로 예외 처리해도 돼?
A. 반복 try-catch는 지양하고 GlobalExceptionHandler에서 공통 처리하는 것이 좋다.

Q. Controller에서 Entity를 반환해도 돼?
A. 권장하지 않는다. Response DTO로 변환해 필요한 필드만 반환하는 것이 좋다.

---

## 4.2 Service Responsibility

### [개념]

Service는 Application의 Business Logic과 Transaction Boundary를 담당하는 Layer다.

Service는 Controller와 Repository 사이에서 Use Case를 수행한다.

Service의 목적:

- Business Logic 처리
- Business Validation 처리
- Transaction Boundary 설정
- Repository 조합
- Entity 조회 / 생성 / 변경
- Custom Exception 발생
- DTO 변환 조율
- 외부 시스템 호출 조율

---

### [핵심]

Service 책임:

- Use Case Method 제공
- Business Rule 적용
- `@Transactional`
- Repository 호출
- Entity 상태 변경
- Custom Exception 발생
- Response DTO 생성
- ExternalApiClient 조율

Service 금지:

- HTTP Request 객체 직접 의존
- Controller Mapping 처리
- View 처리
- 단순 Repository 위임만 과도하게 반복
- 너무 많은 책임 집중
- 순환 참조 발생

---

### [실무]

좋은 Service:

```java
@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;

    @Transactional
    public UserResponse updateUser(Long userId, UserUpdateRequest request) {
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new BusinessException(ErrorCode.USER_NOT_FOUND));

        user.updateNickname(request.nickname());

        return UserResponse.from(user);
    }
}
```

Service Method 설계 기준:

```text
public method
→ 하나의 Use Case 표현
→ Transaction Boundary
→ Repository 조합
→ Entity 변경
→ Response DTO 반환
```

권장:

- 생성자 주입 사용
- public method에 `@Transactional` 적용
- 읽기 메서드는 `@Transactional(readOnly = true)` 고려
- Entity 변경은 Entity Method로 표현
- 비즈니스 예외는 CustomException 사용
- Response DTO 변환 위치를 팀 규칙으로 통일

---

### [FAQ]

Q. Service에는 어떤 로직을 넣어?
A. 비즈니스 규칙, 트랜잭션, Repository 조합, Entity 변경, 예외 처리를 넣는다.

Q. Service가 너무 커지면 어떻게 해?
A. 기능별 Service 분리, 도메인 책임 분리, 별도 Component 분리를 검토한다.

Q. Service에서 DTO 변환을 해도 돼?
A. 가능하다. DTO의 static from 메서드를 쓰거나 Service에서 변환하되 팀 규칙으로 일관화한다.

Q. Service에서 외부 API를 바로 호출해도 돼?
A. 작은 프로젝트에서는 가능하지만 ExternalApiClient 같은 별도 Component로 분리하면 테스트와 유지보수가 쉽다.

---

## 4.3 Repository Responsibility

### [개념]

Repository는 Database 접근을 담당하는 Layer다.

Spring Data JPA에서는 Repository Interface를 통해 Entity CRUD와 Query Method를 제공한다.

Repository는 Business Decision을 담당하지 않는다.

---

### [핵심]

Repository 책임:

- Entity 저장
- Entity 조회
- Entity 삭제
- Query Method
- JPQL
- Native Query
- Pagination Query
- Existence Check

Repository 금지:

- Business Logic
- Controller Response 생성
- DTO 변환 책임 과다
- Use Case 전체 처리
- Transaction 전체 흐름 관리
- HTTP 관련 객체 의존

---

### [실무]

Repository 예:

```java
public interface UserRepository extends JpaRepository<User, Long> {

    Optional<User> findByEmail(String email);

    boolean existsByEmail(String email);
}
```

권장:

- 단건 조회 실패 가능성은 Optional로 표현한다.
- 존재 여부는 existsBy를 사용한다.
- 복잡한 동적 쿼리는 QueryDSL을 검토한다.
- Query Method 이름이 너무 길면 JPQL 또는 Custom Repository를 검토한다.
- Repository는 Entity 중심으로 유지한다.

비권장:

```java
public interface UserRepository extends JpaRepository<User, Long> {

    // 지나치게 긴 Query Method
    List<User> findByEmailContainingAndNicknameContainingAndStatusAndCreatedAtAfterAndDeletedFalseOrderByCreatedAtDesc(...);
}
```

대안:

```text
복잡한 조건 검색
→ QueryDSL
→ Specification
→ Custom Repository
→ JPQL
```

---

### [FAQ]

Q. Repository에는 어떤 로직을 넣어?
A. Entity 저장, 조회, 삭제, Query Method처럼 데이터 접근 로직을 넣는다.

Q. Repository에 비즈니스 로직을 넣어도 돼?
A. 권장하지 않는다. Repository는 데이터 접근 책임에 집중하고 비즈니스 판단은 Service나 Domain에서 처리한다.

Q. Repository Query Method 이름이 너무 길면?
A. JPQL, QueryDSL, Custom Repository 구조를 검토하는 것이 좋다.

Q. Repository에서 DTO를 바로 반환해도 돼?
A. Projection 목적이면 가능하지만 Foundation 단계에서는 Entity 조회 후 Service에서 DTO 변환하는 구조가 이해하기 쉽다.

---

# 5. DTO and Entity Boundary

## 5.1 DTO and Entity Separation

### [개념]

DTO와 Entity는 목적이 다르다.

Entity는 Database와 Domain Model을 표현한다.

DTO는 API Request / Response 데이터를 전달한다.

DTO와 Entity를 분리하면 API 변경과 DB 구조 변경의 영향을 줄일 수 있다.

---

### [핵심]

DTO vs Entity:

| 구분       | DTO                             | Entity                  |
| ---------- | ------------------------------- | ----------------------- |
| 목적       | API 입출력                      | DB / Domain Model       |
| 위치       | Controller 경계                 | Persistence / Domain    |
| 변경 기준  | API Spec                        | DB Schema / Domain Rule |
| 외부 노출  | 가능                            | 직접 노출 지양          |
| Validation | Request 검증                    | Domain 무결성           |
| 예시       | UserCreateRequest, UserResponse | User                    |

핵심 규칙:

- RequestBody로 Entity를 받지 않는다.
- Response로 Entity를 직접 반환하지 않는다.
- Request DTO와 Response DTO를 분리한다.
- 민감정보는 Response DTO에 포함하지 않는다.
- Entity 변경은 Service 또는 Entity Method에서 처리한다.
- DTO 변환 규칙을 통일한다.

---

### [실무]

Request DTO:

```java
public record UserCreateRequest(
        @Email String email,
        @NotBlank String password,
        @NotBlank String nickname
) {
}
```

Response DTO:

```java
public record UserResponse(
        Long userId,
        String email,
        String nickname
) {
    public static UserResponse from(User user) {
        return new UserResponse(
                user.getId(),
                user.getEmail(),
                user.getNickname()
        );
    }
}
```

Entity:

```java
@Entity
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String email;
    private String password;
    private String nickname;

    public void updateNickname(String nickname) {
        this.nickname = nickname;
    }
}
```

금지 패턴:

```java
@PostMapping("/users")
public User createUser(@RequestBody User user) {
    return userRepository.save(user);
}
```

문제:

- password 같은 민감정보 노출 가능
- API 입력과 DB 구조 강결합
- Validation 기준 불명확
- Entity 내부 구조 변경 시 API 영향
- Lazy Loading / 순환 참조 위험

---

### [FAQ]

Q. DTO와 Entity 차이는?
A. DTO는 API 입출력 데이터이고 Entity는 DB와 도메인 구조를 표현하는 내부 모델이다.

Q. Entity를 RequestBody로 받아도 돼?
A. 권장하지 않는다. API 입력 구조와 Entity 내부 구조가 강하게 결합되고 보안 문제가 생길 수 있다.

Q. Entity를 그대로 Response로 반환해도 돼?
A. 권장하지 않는다. 민감정보 노출, Lazy Loading 문제, 순환 참조, API 변경 위험이 생길 수 있다.

Q. Request DTO와 Response DTO는 분리해야 해?
A. 요청과 응답의 필드와 검증 기준이 다르면 분리하는 것이 좋다.

---

# 6. Dependency Direction

## 6.1 Layer Dependency Direction

### [개념]

Dependency Direction은 Layer 간 의존 방향을 의미한다.

Foundation Spring Boot에서는 Controller → Service → Repository 방향을 기본으로 한다.

좋은 의존 방향:

```text
Controller
→ Service
→ Repository
→ Entity
```

나쁜 의존 방향:

```text
Repository
→ Service

Entity
→ Controller

Service A
↔ Service B
```

---

### [핵심]

의존 방향 규칙:

- Controller는 Service에 의존한다.
- Service는 Repository에 의존한다.
- Repository는 Entity에 의존한다.
- DTO는 Controller / Service 경계에서 사용한다.
- Entity는 Controller를 몰라야 한다.
- Repository는 Controller를 몰라야 한다.
- 양방향 Service 의존은 피한다.
- 공통 로직은 별도 Component로 분리한다.

순환 참조 예:

```text
UserService
→ PostService
→ UserService
```

문제:

- Bean 생성 실패 가능
- 책임 경계 불명확
- 테스트 어려움
- 변경 영향 증가

---

### [실무]

좋은 구조:

```java
@Service
@RequiredArgsConstructor
public class PostService {

    private final PostRepository postRepository;
    private final UserRepository userRepository;
}
```

비권장 구조:

```java
@Service
@RequiredArgsConstructor
public class UserService {

    private final PostService postService;
}

@Service
@RequiredArgsConstructor
public class PostService {

    private final UserService userService;
}
```

해결 방법:

```text
양방향 Service 의존 발생
→ 책임 재검토
→ 공통 로직 Component 분리
→ Repository 직접 조합 검토
→ Domain Service 분리
→ Event 구조 검토
```

공통 Component 예:

```java
@Component
@RequiredArgsConstructor
public class UserValidator {

    private final UserRepository userRepository;

    public void validateExists(Long userId) {
        if (!userRepository.existsById(userId)) {
            throw new BusinessException(ErrorCode.USER_NOT_FOUND);
        }
    }
}
```

---

### [FAQ]

Q. Controller는 Repository에 의존해도 돼?
A. 실무 구조에서는 Controller가 Service에 의존하고 Service가 Repository를 사용하는 구조가 좋다.

Q. Service끼리 서로 의존해도 돼?
A. 양방향 의존은 순환 참조와 책임 혼란을 만들 수 있으므로 피하는 것이 좋다.

Q. 순환 참조가 생기면 어떻게 해?
A. 의존 방향과 책임을 다시 보고 공통 로직 분리, Service 재분리, 이벤트 구조를 검토한다.

Q. 공통 검증 로직은 어디에 둬?
A. 여러 Service에서 반복된다면 별도 Component나 Domain Service로 분리할 수 있다.

---

# 7. Package Structure Patterns

## 7.1 Layer Package Structure

### [개념]

Layer Package Structure는 controller, service, repository처럼 계층 기준으로 패키지를 나누는 구조다.

Foundation Spring Boot 문서에서는 Layer Package Structure를 기본 구조로 사용한다.

---

### [핵심]

구조:

```text
com.example.project
├ controller
│ ├ UserController.java
│ └ PostController.java
├ service
│ ├ UserService.java
│ └ PostService.java
├ repository
│ ├ UserRepository.java
│ └ PostRepository.java
├ entity
│ ├ User.java
│ └ Post.java
└ dto
  ├ request
  └ response
```

장점:

- 초보자가 이해하기 쉽다.
- Spring Boot Layer 책임이 명확하다.
- 작은 프로젝트에 적합하다.
- Controller / Service / Repository 위치를 찾기 쉽다.

단점:

- 기능이 많아지면 패키지가 커진다.
- 도메인 단위 응집도가 낮아질 수 있다.
- 대형 프로젝트에서는 관리가 어려울 수 있다.

---

### [실무]

Layer Package가 적합한 경우:

- 학습 프로젝트
- 개인 프로젝트 초기 단계
- 팀 프로젝트 Foundation 단계
- Domain 수가 적은 CRUD Application
- RAG 문서에서 구조 기준을 명확히 잡아야 하는 경우

주의:

- service 패키지에 모든 Service가 몰릴 수 있다.
- dto 패키지에 모든 DTO가 몰릴 수 있다.
- 기능이 커지면 domain별 하위 패키지를 검토한다.

확장 예:

```text
dto
├ user
│ ├ request
│ └ response
└ post
  ├ request
  └ response
```

---

### [FAQ]

Q. Layer Package 구조는 언제 좋아?
A. 작은 프로젝트, 학습 프로젝트, Foundation 단계처럼 계층 책임을 명확히 익혀야 할 때 좋다.

Q. Layer Package 구조의 단점은 뭐야?
A. 기능이 많아지면 같은 계층 파일이 많아져 도메인 응집도가 낮아질 수 있다.

Q. 처음부터 Domain Package로 가야 해?
A. 반드시 그럴 필요는 없다. Foundation 단계에서는 Layer 구조로 시작하고 규모가 커지면 전환해도 된다.

---

## 7.2 Domain Package Structure

### [개념]

Domain Package Structure는 user, post, order처럼 기능 또는 도메인 기준으로 패키지를 나누는 구조다.

도메인 응집도를 높이고 기능 단위 변경을 쉽게 만들기 위한 구조다.

---

### [핵심]

구조:

```text
com.example.project
├ domain
│ ├ user
│ │ ├ controller
│ │ ├ service
│ │ ├ repository
│ │ ├ entity
│ │ └ dto
│ └ post
│   ├ controller
│   ├ service
│   ├ repository
│   ├ entity
│   └ dto
├ global
│ ├ config
│ ├ exception
│ └ common
└ ProjectApplication.java
```

장점:

- 도메인 응집도가 높다.
- 기능 단위 변경이 쉽다.
- 대형 프로젝트에 적합하다.
- Agent가 기능 단위 코드를 찾기 쉽다.

단점:

- 초기 학습 난이도가 높다.
- 공통 모듈 분리 기준이 필요하다.
- 도메인 경계 설계가 필요하다.
- 작은 프로젝트에서는 과할 수 있다.

---

### [실무]

Domain Package가 적합한 경우:

- 기능이 많은 프로젝트
- 도메인별 책임이 명확한 프로젝트
- 팀원이 도메인 단위로 작업하는 프로젝트
- 중형 이상 Backend Application
- 추후 MSA 전환 가능성을 고려하는 프로젝트

예:

```text
domain
├ festival
│ ├ controller
│ ├ service
│ ├ repository
│ ├ entity
│ └ dto
├ review
│ ├ controller
│ ├ service
│ ├ repository
│ ├ entity
│ └ dto
└ chat
  ├ controller
  ├ service
  ├ repository
  ├ entity
  └ dto
```

공통 영역:

```text
global
├ config
├ exception
├ security
├ common
└ util
```

주의:

- global 패키지에 비즈니스 로직을 넣지 않는다.
- domain 간 순환 의존을 피한다.
- 공통 DTO와 도메인 DTO를 구분한다.
- domain 내부 구조 이름을 통일한다.

---

### [FAQ]

Q. Domain Package 구조는 언제 좋아?
A. 기능이 많고 도메인별 책임이 명확한 중형 이상 프로젝트에서 좋다.

Q. global 패키지에는 뭘 둬?
A. config, exception, common response, security 설정처럼 전역 공통 요소를 둔다.

Q. Domain Package가 항상 Layer Package보다 좋아?
A. 아니다. 프로젝트 규모와 팀 숙련도에 따라 선택한다.

Q. RAG 문서에서는 어떤 구조를 우선 설명해?
A. Foundation 단계에서는 Layer 구조를 우선하고, 확장 구조로 Domain Package를 함께 설명한다.

---

# 8. Common Mistakes

## 8.1 Application Structure Common Mistakes

### [개념]

Application Structure Common Mistakes는 Spring Boot 초기 설계에서 자주 발생하는 구조 문제다.

구조 문제는 기능 구현 후에 수정 비용이 커진다.

---

### [핵심]

자주 발생하는 실수:

- Main Application Class를 하위 패키지에 둠
- Controller에서 Repository 직접 호출
- Controller에 Business Logic 작성
- Entity를 RequestBody로 직접 사용
- Entity를 Response로 직접 반환
- DTO 없이 API 구성
- Request DTO와 Response DTO 혼용
- Service가 단순 Repository 위임만 반복
- Service 책임이 너무 커짐
- Repository에 Business Logic 작성
- common / util 패키지 남용
- 순환 Service 의존 발생
- config에 Business Logic 작성
- exception 구조 없이 RuntimeException 남발
- 패키지 이름 규칙 불일치
- domain 구조와 layer 구조 혼합 기준 없음

---

### [실무]

문제 예:

```text
문제:
Controller에서 Repository 직접 호출

결과:
Business Logic 위치 불명확
Transaction Boundary 불명확
Test 어려움

해결:
Controller → Service → Repository 구조로 수정
```

문제 예:

```text
문제:
Entity를 Response로 직접 반환

결과:
민감정보 노출
Lazy Loading 오류
순환 참조
API Spec 불안정

해결:
Response DTO 생성 후 필요한 필드만 반환
```

문제 예:

```text
문제:
Main Class가 하위 패키지에 위치

결과:
Bean 등록 실패
NoSuchBeanDefinitionException
Controller Mapping 실패

해결:
Main Class를 Root Package로 이동
```

---

### [FAQ]

Q. Spring Boot 초보가 가장 많이 하는 구조 실수는?
A. Controller에 모든 로직을 넣거나 Entity를 그대로 Request / Response에 사용하는 실수가 많다.

Q. 구조 문제는 언제 잡는 게 좋아?
A. 기능 구현 전 패키지 구조와 Layer 책임을 먼저 정하는 것이 좋다.

Q. common이나 util에 넣으면 편하지 않아?
A. 단기적으로 편하지만 책임이 흐려질 수 있다. 먼저 적절한 Layer나 Domain 책임인지 검토한다.

Q. RuntimeException만 던져도 돼?
A. 가능은 하지만 비즈니스 의미가 있는 예외는 CustomException과 ErrorCode로 명확히 표현하는 것이 좋다.

---

# 9. Review Checklist

## 9.1 Application Structure Checklist

### [개념]

Application Structure Checklist는 Spring Boot Part01 문서와 코드 구조를 검수하기 위한 기준이다.

Backend Agent와 Review Agent는 이 Checklist를 기준으로 구조 문제를 탐지한다.

---

### [핵심]

Checklist:

```md
- [ ] Main Application Class가 Root Package에 있는가?
- [ ] controller / service / repository / entity / dto / config / exception 구조가 있는가?
- [ ] Controller가 Service만 호출하는가?
- [ ] Controller에서 Repository를 직접 호출하지 않는가?
- [ ] Controller에 Business Logic이 없는가?
- [ ] Service가 Business Logic과 Transaction Boundary를 담당하는가?
- [ ] Repository가 Data Access 책임만 담당하는가?
- [ ] Entity를 RequestBody로 직접 받지 않는가?
- [ ] Entity를 Response로 직접 반환하지 않는가?
- [ ] Request DTO와 Response DTO가 분리되어 있는가?
- [ ] ApiResponse 같은 공통 응답 규칙이 있는가?
- [ ] GlobalExceptionHandler 위치가 명확한가?
- [ ] Config Class가 config 패키지에 있는가?
- [ ] common / util 패키지를 남용하지 않는가?
- [ ] Service 간 순환 의존이 없는가?
- [ ] 패키지 이름 규칙이 일관적인가?
- [ ] Layer 구조와 Domain 구조를 혼합할 경우 기준이 명확한가?
```

---

### [실무]

검수 흐름:

```text
Package Structure 확인
→ Main Class 위치 확인
→ Component Scan 범위 확인
→ Controller 책임 확인
→ Service 책임 확인
→ Repository 책임 확인
→ DTO / Entity 경계 확인
→ Dependency Direction 확인
→ Common Mistakes 확인
→ Final Review
```

검수 결과 예:

```text
문제:
PostController가 PostRepository를 직접 호출함

위험:
Controller 책임 초과
Transaction Boundary 불명확
Business Logic 분산

수정:
PostService 생성
PostController → PostService → PostRepository 구조로 변경
```

---

### [FAQ]

Q. Part01에서 가장 먼저 검수할 것은?
A. Main Class 위치, 패키지 구조, Controller / Service / Repository 책임 분리다.

Q. DTO 검수도 Part01에 포함돼?
A. DTO 상세는 별도 Part에서 다루지만, Entity 직접 노출 금지와 DTO 경계는 Part01에서 반드시 확인한다.

Q. Layer 구조와 Domain 구조가 섞여 있으면 무조건 나쁜가?
A. 무조건 나쁘지는 않지만 기준 없이 섞이면 코드 탐색과 유지보수가 어려워진다.

---

# 10. Part01 Final Goal

## 10.1 Application Structure Final Goal

### [개념]

Spring Boot Part01의 최종 목표는 Backend Agent가 Spring Boot Application의 기본 구조와 Layer 책임을 일관되게 설계하도록 만드는 것이다.

Part01은 Spring Boot 전체 문서의 기반이다.

---

### [핵심]

Part01이 지원해야 하는 작업:

- Spring Boot Application Structure 설계
- Main Application Class 위치 판단
- Component Scan 문제 예방
- Layered Architecture 적용
- Controller Responsibility 판단
- Service Responsibility 판단
- Repository Responsibility 판단
- DTO / Entity Boundary 판단
- Dependency Direction 검토
- Layer Package Structure 선택
- Domain Package Structure 확장 판단
- Common Mistakes 탐지
- Review Checklist 수행

---

### [실무]

Backend Agent 수행 흐름:

```text
User Backend Request
→ Identify Domain
→ Choose Package Structure
→ Place Main Application Class
→ Create Controller
→ Create Service
→ Create Repository
→ Create Entity
→ Create Request DTO
→ Create Response DTO
→ Apply ApiResponse
→ Apply Exception Structure
→ Review Layer Responsibility
→ Output Spring Boot Structure
```

Review Agent 수행 흐름:

```text
Input Spring Boot Code
→ Check Package Structure
→ Check Main Class Location
→ Check Controller Thin Rule
→ Check Service Business Logic Rule
→ Check Repository Responsibility
→ Check DTO Entity Separation
→ Check Dependency Direction
→ Detect Anti Pattern
→ Suggest Fix
```

---

### [FAQ]

Q. Spring Boot Part01의 최종 목적은 뭐야?
A. Backend Agent가 Spring Boot Application 구조와 Layer 책임을 일관되게 설계하고 Review Agent가 구조 문제를 탐지하게 만드는 것이다.

Q. Part01 다음에는 어떤 문서가 이어져야 해?
A. Controller & Request Mapping, DTO & ApiResponse, Validation, Service & Transaction 문서로 이어지는 것이 좋다.

Q. Part01만으로 코드 생성을 할 수 있어?
A. 기본 구조 생성은 가능하지만 상세 Controller Mapping, DTO, Validation, Exception, Transaction은 후속 Part와 함께 사용해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Spring Boot Application Structure는 뭐야?
A. Backend Application을 controller, service, repository, entity, dto, config, exception처럼 책임 기준으로 나누는 구조다.

Q. Spring Boot 패키지 구조는 어떻게 잡아?
A. 기초 단계에서는 controller, service, repository, entity, dto, config, exception 중심의 Layer 구조가 좋다.

Q. Spring Boot Main Class는 어디에 둬?
A. Component Scan을 위해 프로젝트 Root Package에 두는 것이 좋다.

Q. `@SpringBootApplication`은 뭐야?
A. Spring Boot Application 시작 Annotation이며 Component Scan, Auto Configuration, Configuration 역할을 포함한다.

Q. Main Class 위치가 중요한 이유는?
A. 기본 Component Scan이 Main Class가 있는 패키지 하위 기준으로 동작하기 때문이다.

Q. Component Scan 문제는 어떻게 확인해?
A. Main Class 위치, 대상 클래스 패키지 위치, Annotation, Profile 조건, Configuration을 확인한다.

Q. Layered Architecture는 뭐야?
A. Controller, Service, Repository, Database처럼 Backend Application을 책임별 계층으로 나누는 구조다.

Q. Spring Boot Layer 구조 기본 흐름은?
A. Client → Controller → Service → Repository → Database → Service → Controller → Client 흐름이다.

Q. Controller Service Repository 차이는?
A. Controller는 HTTP 요청/응답, Service는 비즈니스 로직과 트랜잭션, Repository는 데이터 접근을 담당한다.

Q. Controller는 어떤 책임을 가져?
A. URL Mapping, Request DTO 수신, Validation Trigger, Service 호출, Response 반환을 담당한다.

Q. Controller에서 Repository를 바로 호출해도 돼?
A. 실무 구조에서는 Service를 거쳐 비즈니스 로직과 트랜잭션 경계를 관리하는 것이 좋다.

Q. Controller에 비즈니스 로직을 넣으면 안 되는 이유는?
A. HTTP 책임과 비즈니스 책임이 섞이고 테스트와 유지보수가 어려워지기 때문이다.

Q. Service는 어떤 책임을 가져?
A. Business Logic, Business Validation, Transaction Boundary, Repository 조합, Entity 변경, Custom Exception 발생을 담당한다.

Q. Service는 왜 필요해?
A. 비즈니스 로직, 트랜잭션, 여러 Repository 조합, 예외 처리를 Controller에서 분리하기 위해 필요하다.

Q. Repository는 어떤 책임을 가져?
A. Entity 저장, 조회, 삭제, Query Method, Pagination Query 같은 Data Access를 담당한다.

Q. Repository에 비즈니스 로직을 넣어도 돼?
A. 권장하지 않는다. Repository는 데이터 접근 책임에 집중하고 비즈니스 판단은 Service나 Domain에서 처리한다.

Q. DTO와 Entity 차이는?
A. DTO는 API 입출력 데이터이고 Entity는 DB와 도메인 구조를 표현하는 내부 모델이다.

Q. Entity를 RequestBody로 받아도 돼?
A. 권장하지 않는다. API 입력 구조와 Entity 내부 구조가 강하게 결합되고 보안 문제가 생길 수 있다.

Q. Entity를 Response로 직접 반환해도 돼?
A. 권장하지 않는다. 민감정보 노출, Lazy Loading 문제, 순환 참조, API 변경 위험이 생길 수 있다.

Q. Request DTO와 Response DTO는 분리해야 해?
A. 요청과 응답의 필드와 검증 기준이 다르면 분리하는 것이 좋다.

Q. Layer Dependency Direction은 어떻게 잡아?
A. Controller → Service → Repository → Entity 방향을 기본으로 한다.

Q. Service끼리 서로 의존해도 돼?
A. 양방향 의존은 순환 참조와 책임 혼란을 만들 수 있으므로 피하는 것이 좋다.

Q. 순환 참조가 생기면 어떻게 해?
A. 의존 방향과 책임을 다시 보고 공통 로직 분리, Service 재분리, 이벤트 구조를 검토한다.

Q. Layer Package Structure는 언제 좋아?
A. 작은 프로젝트, 학습 프로젝트, Foundation 단계처럼 계층 책임을 명확히 익혀야 할 때 좋다.

Q. Domain Package Structure는 언제 좋아?
A. 기능이 많고 도메인별 책임이 명확한 중형 이상 프로젝트에서 좋다.

Q. global 패키지에는 뭘 둬?
A. config, exception, common response, security 설정처럼 전역 공통 요소를 둔다.

Q. common 패키지는 언제 써?
A. ApiResponse, 공통 상수, 공통 유틸처럼 여러 계층에서 재사용되는 요소에 사용한다.

Q. util 패키지를 남용하면 왜 안 좋아?
A. 책임이 흐려지고 도메인 로직이 유틸로 흩어져 유지보수가 어려워질 수 있다.

Q. Spring Boot 초보가 가장 많이 하는 구조 실수는?
A. Controller에 모든 로직을 넣거나 Entity를 그대로 Request / Response에 사용하는 실수가 많다.

Q. Bean 등록이 안 되면 뭘 확인해?
A. Main Class 위치, Component Scan 범위, Annotation, Profile 조건, Configuration을 확인한다.

Q. 404가 나면 구조적으로 뭘 확인해?
A. Frontend Request URL, Axios baseURL, Controller @RequestMapping, Method Mapping, HTTP Method, Security 차단 여부를 확인한다.

Q. Part01에서 가장 중요한 검수 기준은?
A. Main Class 위치, 패키지 구조, Controller / Service / Repository 책임 분리, DTO / Entity 경계다.

Q. Spring Boot Part01 다음에는 뭐가 좋아?
A. Controller & Request Mapping, DTO & ApiResponse, Validation, Service & Transaction 문서로 이어지는 것이 좋다.
