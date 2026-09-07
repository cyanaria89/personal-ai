# Spring Boot Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

Spring Boot Domain Rules 문서는 Backend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- Spring Boot 기반 Backend Application 구조 설계 지원
- Controller / Service / Repository Layer 분리 기준 제공
- Dependency Injection / Bean 관리 판단 기준 제공
- REST API 구현 규칙 제공
- DTO / Validation / Exception Handling 기준 제공
- Configuration / Properties 관리 기준 제공
- Transaction / Service 책임 분리 지원
- Spring MVC 요청 처리 흐름 이해 지원
- Spring Boot Anti Pattern 검출 지원
- 유지보수 가능한 Backend 구조 설계 지원

---

### [핵심]

우선순위:

1. Spring Boot Application Structure
2. Layered Architecture
3. Controller
4. Service
5. Repository
6. Dependency Injection
7. Bean Lifecycle Basics
8. REST API
9. DTO
10. Validation
11. Exception Handling
12. GlobalExceptionHandler
13. Configuration Properties
14. Transaction Boundary
15. API Response Convention
16. Logging
17. Testing Readiness
18. Anti Pattern Review

---

### [실무]

Spring Boot 문서는 단순 Annotation 목록 문서가 아니다.

Backend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- 프로젝트 구조 설계
- Controller / Service / Repository 책임 분리
- REST API Endpoint 설계
- Request / Response DTO 분리
- Validation 적용 위치 판단
- Business Logic 위치 판단
- Transaction 적용 기준 판단
- Global Exception Handling 구조 설계
- Configuration 분리
- Bean 등록 방식 검토
- 순환 참조 / 과도한 의존성 감지
- 테스트 가능한 코드 구조 검토
- Spring Boot Anti Pattern 탐지

---

### [FAQ]

Q. Spring Boot Domain Rules는 Java Domain Rules와 뭐가 달라?

A.
Java Domain Rules는 언어 문법과 객체지향 기준이고 Spring Boot Domain Rules는 Backend Application 구조, Layer, DI, REST API, 설정, 예외 처리 기준을 다룬다.

Q. Spring Boot 문서에서 가장 중요한 기준은 뭐야?

A.
Layer 책임 분리, Controller 얇게 유지, Service 비즈니스 로직 집중, DTO 분리, 예외 처리 일관성, Transaction 경계 설정이다.

Q. Spring Boot는 Annotation만 외우면 돼?

A.
아니다. Annotation보다 요청 흐름, Bean 관리, Layer 책임, 예외 처리, 트랜잭션 경계 이해가 더 중요하다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Spring Boot 문서는 Backend Foundation에서 Spring Boot Application 개발에 필요한 핵심 범위를 포함한다.

포함 범위:

- Spring Boot Application Structure
- Layered Architecture
- Controller Layer
- Service Layer
- Repository Layer
- Component Scan
- Dependency Injection
- Bean Registration
- Spring MVC Request Flow
- REST API Design Basics
- Request DTO / Response DTO
- Validation
- Exception Handling
- GlobalExceptionHandler
- ApiResponse Convention
- Configuration
- application.yml / application.properties
- Profile
- Transaction Boundary
- Logging
- Environment Variable
- CORS Basics
- Pagination Basics
- Testing Readiness
- Common Anti Patterns

---

### [핵심]

반드시 포함:

- Controller는 HTTP 요청과 응답을 담당
- Service는 비즈니스 로직과 Transaction 경계를 담당
- Repository는 데이터 접근을 담당
- Entity를 Controller Response로 직접 노출하지 않음
- Request DTO와 Response DTO를 분리
- Validation은 Request 경계에서 우선 처리
- 예외 처리는 GlobalExceptionHandler로 일관화
- 설정 값은 코드에 하드코딩하지 않음
- Transaction은 읽기 / 쓰기 기준을 구분
- Bean 의존성은 생성자 주입 우선
- Controller에 비즈니스 로직을 넣지 않음

---

### [실무]

Spring Boot 문서는 Java / SQL / JPA / Security 문서와 함께 사용된다.

실무 연결:

```text
Java
→ Spring Boot
→ JPA
→ Security
→ API Design
→ Testing
```

Backend 개발 흐름:

```text
Requirement
→ API Design
→ DTO Design
→ Controller
→ Service
→ Repository
→ Exception Handling
→ Test
```

---

### [FAQ]

Q. Spring Boot 문서에서 JPA를 깊게 다뤄?

A.
아니다. Repository 연동 기준은 포함하지만 Entity Mapping, 영속성 컨텍스트, N+1 같은 내용은 JPA Domain Rules에서 다룬다.

Q. Security 설정도 여기서 다뤄?

A.
CORS나 인증 연동 위치 정도만 포함하고 Spring Security 필터 체인, JWT, OAuth2는 Security Domain Rules에서 다룬다.

Q. API 설계를 여기서 다뤄?

A.
REST API 구현 기준은 포함하지만 URI 설계, 응답 규칙, 에러 코드 체계 심화는 API Design Domain Rules에서 다룬다.

---

## 2.2 Excluded Scope

### [개념]

Spring Boot Domain Rules에서는 다른 전문 Domain 문서와 겹치는 심화 내용을 제외한다.

제외 범위:

- JPA 영속성 컨텍스트 심화
- QueryDSL 동적 쿼리 심화
- Spring Security Filter Chain 심화
- JWT / OAuth2 심화
- Redis Cache 심화
- WebSocket 심화
- Batch 심화
- Kafka / Message Queue
- MSA / Service Discovery
- Kubernetes / Cloud Deploy
- 고급 Observability
- Native Image
- Spring WebFlux 심화

---

### [핵심]

제외 이유:

- Foundation 범위 유지
- Agent Retrieval 혼선 방지
- JPA / Security / DevOps / Expert Rules와 책임 분리
- Chunk 품질 유지
- Spring Boot Application 기본 구조와 실무 개발 기준에 집중

---

### [실무]

고급 기술은 별도 Domain Rules로 분리한다.

예:

```text
Spring Boot
→ JPA Advanced
→ Security Advanced
→ Redis
→ API Design
→ Testing
→ Advanced Spring Architecture
```

---

### [FAQ]

Q. WebFlux는 여기서 다뤄?

A.
아니다. Foundation Spring Boot 문서는 Spring MVC 기반을 우선한다. WebFlux는 고급 Reactive Stack 문서로 분리하는 것이 좋다.

Q. Spring Batch는 여기서 다뤄?

A.
아니다. Batch는 별도 심화 문서가 적합하다.

Q. MSA 구조도 여기서 다뤄?

A.
아니다. 단일 Spring Boot Application 기본 구조를 우선하고 MSA는 Expert Domain Rules에서 다룬다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

Spring Boot RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

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
- [실무]: 실제 코드 설계 기준
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

Q. Spring Boot 문서에도 FAQ가 필요해?

A.
필요하다. 사용자가 자주 묻는 Controller, Service, DTO, Validation, Exception 질문과 Retrieval 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

Spring Boot 문서에는 요청 흐름과 책임 분리를 명확히 하기 위해 추가 Section을 포함할 수 있다.

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

- Request Flow 설명 → [Flow]
- Layer 책임 설명 → [Comparison], [Checklist]
- DTO 설명 → [예제], [주의]
- Exception Handling 설명 → [Flow], [예제]
- Transaction 설명 → [주의], [Best Practice]
- Anti Pattern 설명 → [Troubleshooting]

---

### [실무]

예시:

```md
### [Flow]

HTTP Request
→ DispatcherServlet
→ Controller
→ Service
→ Repository
→ Service
→ Controller
→ HTTP Response
```

---

### [FAQ]

Q. Spring Boot 문서에 Flow가 중요한 이유는?

A.
요청이 Controller, Service, Repository를 거쳐 응답되는 흐름을 알아야 책임 분리와 오류 추적이 가능하기 때문이다.

Q. Comparison이 필요한 이유는?

A.
Controller와 Service, DTO와 Entity, Component와 Configuration처럼 헷갈리는 개념을 구분해야 하기 때문이다.

---

# 4. Spring Boot Application Structure Rules

## 4.1 Application Structure

### [개념]

Spring Boot Application Structure는 Backend Application을 기능과 책임 기준으로 나누는 패키지 구조다.

---

### [핵심]

기본 구조:

- config
- controller
- service
- repository
- entity
- dto
- exception
- domain
- common
- util

---

### [실무]

권장 구조 예:

```text
src/main/java/com/example/project
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
└ ProjectApplication.java
```

규칙:

- Controller는 controller 패키지에 둠
- Service는 service 패키지에 둠
- Repository는 repository 패키지에 둠
- Entity는 entity 또는 domain 패키지에 둠
- DTO는 request / response로 분리 가능
- 공통 응답, 에러 코드는 common 또는 exception에 둠
- 설정 클래스는 config에 둠

---

### [FAQ]

Q. Spring Boot 패키지 구조는 어떻게 잡아?

A.
기초 단계에서는 controller, service, repository, entity, dto, config, exception 중심의 Layer 기준 구조가 이해하기 쉽다.

Q. Entity와 DTO는 같은 패키지에 둬도 돼?

A.
가능은 하지만 역할이 다르므로 entity와 dto를 분리하는 것이 유지보수에 좋다.

---

## 4.2 Main Application Class Rules

### [개념]

Main Application Class는 Spring Boot Application의 시작점이다.

`@SpringBootApplication`은 Component Scan, Auto Configuration, Configuration을 포함하는 핵심 Annotation이다.

---

### [핵심]

포함 개념:

- @SpringBootApplication
- SpringApplication.run
- Component Scan base package
- Auto Configuration
- Application Entry Point

---

### [실무]

예:

```java
@SpringBootApplication
public class ProjectApplication {

    public static void main(String[] args) {
        SpringApplication.run(ProjectApplication.class, args);
    }
}
```

주의:

- Main Class는 상위 패키지에 위치시키는 것이 좋음
- 하위 패키지가 Component Scan 대상이 됨
- 패키지 구조가 잘못되면 Bean 등록이 안 될 수 있음

---

### [FAQ]

Q. @SpringBootApplication은 뭐야?

A.
Spring Boot Application 시작을 위한 핵심 Annotation이며 Component Scan, Auto Configuration, Configuration 역할을 포함한다.

Q. Main Class 위치가 중요한 이유는?

A.
기본 Component Scan은 Main Class가 있는 패키지 하위 기준으로 동작하기 때문이다.

---

# 5. Layered Architecture Rules

## 5.1 Layer Responsibility

### [개념]

Layered Architecture는 Backend Application을 책임별 계층으로 나누는 구조다.

기본 계층:

```text
Controller
→ Service
→ Repository
→ Database
```

---

### [핵심]

Layer 책임:

| Layer      | 책임                         |
| ---------- | ---------------------------- |
| Controller | HTTP 요청 / 응답 / DTO 수신  |
| Service    | 비즈니스 로직 / 트랜잭션     |
| Repository | 데이터 접근                  |
| Entity     | 도메인 데이터 구조           |
| DTO        | 외부 요청 / 응답 데이터 전달 |

---

### [실무]

요청 흐름:

```text
Client
→ Controller
→ Service
→ Repository
→ Database
→ Repository
→ Service
→ Controller
→ Client
```

권장:

- Controller는 얇게 유지
- Service에 비즈니스 로직 집중
- Repository는 DB 접근만 담당
- Entity는 내부 도메인 모델로 유지
- DTO는 API 경계에서 사용
- Layer를 건너뛰는 직접 접근 지양

---

### [FAQ]

Q. Controller에서 Repository를 바로 호출해도 돼?

A.
간단한 예제에서는 가능하지만 실무 구조에서는 Service를 거쳐 비즈니스 로직과 트랜잭션 경계를 관리하는 것이 좋다.

Q. Service는 왜 필요해?

A.
비즈니스 로직, 트랜잭션, 여러 Repository 조합, 예외 처리를 Controller에서 분리하기 위해 필요하다.

---

## 5.2 Controller Thin Rule

### [개념]

Controller Thin Rule은 Controller에 비즈니스 로직을 넣지 않고 HTTP 요청과 응답 처리에 집중시키는 규칙이다.

---

### [핵심]

Controller 책임:

- URL Mapping
- Request DTO 수신
- Validation Trigger
- Authentication Principal 수신
- Service 호출
- Response DTO 반환
- HTTP 상태 또는 공통 응답 반환

Controller 금지:

- 복잡한 비즈니스 로직
- DB 직접 접근
- Entity 직접 수정
- 긴 조건문 처리
- Transaction 중심 로직
- 외부 API 복잡한 처리

---

### [실무]

좋은 예:

```java
@PostMapping("/posts")
public ApiResponse<PostResponse> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    PostResponse response = postService.createPost(request);
    return ApiResponse.success(response);
}
```

나쁜 예:

```java
@PostMapping("/posts")
public Post createPost(@RequestBody PostCreateRequest request) {
    Post post = new Post();
    post.setTitle(request.getTitle());
    postRepository.save(post);
    return post;
}
```

---

### [FAQ]

Q. Controller는 어디까지 해야 해?

A.
요청을 받고 검증을 트리거한 뒤 Service를 호출하고 응답을 반환하는 정도가 적합하다.

Q. Controller에 비즈니스 로직이 많으면 왜 문제야?

A.
테스트가 어려워지고 코드 중복이 늘며 HTTP 책임과 비즈니스 책임이 섞인다.

---

## 5.3 Service Business Logic Rule

### [개념]

Service Layer는 Application의 비즈니스 로직과 Transaction 경계를 담당한다.

---

### [핵심]

Service 책임:

- Business Logic
- Transaction Boundary
- Entity 조회 / 생성 / 변경
- Repository 조합
- Domain Rule 적용
- 예외 발생
- DTO 변환 조율
- 외부 시스템 호출 조율

---

### [실무]

예:

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

권장:

- 생성자 주입 사용
- public method 단위로 use case 표현
- 쓰기 작업은 @Transactional 적용
- 읽기 작업은 @Transactional(readOnly = true) 고려
- Entity 변경 로직은 Entity 메서드와 조율
- 예외는 명확한 Custom Exception 사용

---

### [FAQ]

Q. Service에는 어떤 로직을 넣어?

A.
비즈니스 규칙, 트랜잭션, Repository 조합, Entity 변경, 예외 처리를 넣는다.

Q. Service가 너무 커지면 어떻게 해?

A.
기능별 Service 분리, 도메인 책임 분리, private method 정리, 별도 Component 분리를 검토한다.

---

## 5.4 Repository Responsibility Rule

### [개념]

Repository Layer는 데이터 저장소 접근을 담당하는 계층이다.

Spring Data JPA에서는 Repository Interface로 기본 CRUD와 Query Method를 제공한다.

---

### [핵심]

Repository 책임:

- Entity 저장
- Entity 조회
- Entity 삭제
- Query Method
- JPQL / Native Query
- Pagination Query
- Existence Check

Repository 금지:

- 비즈니스 의사결정
- Controller Response 생성
- 복잡한 Use Case 처리
- Transaction 전체 흐름 관리

---

### [실무]

예:

```java
public interface PostRepository extends JpaRepository<Post, Long> {

    Optional<Post> findByIdAndDeletedFalse(Long postId);

    boolean existsByTitle(String title);
}
```

권장:

- Optional로 단건 조회 실패 표현
- 존재 여부는 existsBy 사용
- 복잡한 동적 쿼리는 QueryDSL 검토
- Query 이름이 너무 길면 별도 쿼리 전략 검토
- Repository는 Entity 중심으로 유지

---

### [FAQ]

Q. Repository에 비즈니스 로직을 넣어도 돼?

A.
권장하지 않는다. Repository는 데이터 접근 책임에 집중하고 비즈니스 판단은 Service나 Domain에서 처리한다.

Q. Repository Query Method 이름이 너무 길면?

A.
JPQL, QueryDSL, 별도 Repository Custom 구조를 검토하는 것이 좋다.

---

# 6. Dependency Injection and Bean Rules

## 6.1 Dependency Injection Rules

### [개념]

Dependency Injection은 객체가 직접 의존 객체를 생성하지 않고 Spring Container가 의존성을 주입하는 방식이다.

---

### [핵심]

DI 방식:

- Constructor Injection
- Field Injection
- Setter Injection

권장:

- Constructor Injection 우선
- final field 사용
- RequiredArgsConstructor 활용 가능
- 순환 참조 방지
- 테스트 가능성 확보

---

### [실무]

권장 예:

```java
@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
}
```

비권장 예:

```java
@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;
}
```

이유:

- Constructor Injection은 불변성 확보
- 테스트 시 의존성 주입 명확
- 필수 의존성 누락 방지
- 순환 참조를 빠르게 발견 가능

---

### [FAQ]

Q. Spring Boot에서 의존성 주입은 뭘 써야 해?

A.
생성자 주입을 우선한다. final 필드와 함께 쓰면 필수 의존성이 명확해진다.

Q. Field Injection은 왜 비권장이야?

A.
테스트가 어렵고 필수 의존성이 숨겨지며 불변성을 보장하기 어렵다.

---

## 6.2 Bean Registration Rules

### [개념]

Bean은 Spring Container가 생성하고 관리하는 객체다.

Bean 등록은 Annotation 또는 Configuration Method로 수행할 수 있다.

---

### [핵심]

Bean 등록 방식:

- @Component
- @Service
- @Repository
- @Controller
- @RestController
- @Configuration
- @Bean

---

### [실무]

Annotation 선택 기준:

| Annotation      | 사용 대상                 |
| --------------- | ------------------------- |
| @Controller     | View 또는 MVC Controller  |
| @RestController | REST API Controller       |
| @Service        | Business Service          |
| @Repository     | Data Access Layer         |
| @Component      | 일반 Component            |
| @Configuration  | 설정 클래스               |
| @Bean           | 외부 라이브러리 객체 등록 |

예:

```java
@Configuration
public class AppConfig {

    @Bean
    public ObjectMapper objectMapper() {
        return new ObjectMapper();
    }
}
```

주의:

- 직접 만든 Service는 @Service 사용
- 외부 라이브러리 객체는 @Bean 등록
- 의미 없는 @Component 남용 금지
- Bean 이름 충돌 주의

---

### [FAQ]

Q. @Component와 @Service 차이는 뭐야?

A.
기능적으로 Bean 등록은 같지만 @Service는 비즈니스 서비스 계층이라는 의미를 명확히 표현한다.

Q. @Bean은 언제 써?

A.
외부 라이브러리 객체처럼 클래스에 직접 @Component를 붙일 수 없을 때 사용한다.

---

## 6.3 Circular Dependency Rules

### [개념]

Circular Dependency는 Bean들이 서로를 의존해서 생성 순환이 발생하는 문제다.

---

### [핵심]

예:

```text
AService → BService → AService
```

문제:

- 설계 책임 불명확
- 테스트 어려움
- Bean 생성 실패 가능
- 변경 영향 범위 증가

---

### [실무]

해결 기준:

- Service 책임 재분리
- 공통 로직을 별도 Component로 분리
- 이벤트 발행 구조 검토
- 의존 방향 재설계
- Lazy Injection은 임시 우회로만 검토

주의:

- 순환 참조를 설정으로 허용하지 않음
- @Lazy로 숨기기보다 설계를 수정
- 양방향 Service 의존은 대부분 구조 문제 신호

---

### [FAQ]

Q. 순환 참조가 생기면 어떻게 해?

A.
의존 방향과 책임을 다시 보고 공통 로직 분리, Service 재분리, 이벤트 구조를 검토한다.

Q. @Lazy로 해결해도 돼?

A.
임시 우회는 가능하지만 근본 해결은 아니다. 설계 책임을 재검토하는 것이 좋다.

---

# 7. Spring MVC and Request Flow Rules

## 7.1 Spring MVC Request Flow

### [개념]

Spring MVC Request Flow는 HTTP 요청이 Spring Boot Application에서 Controller까지 전달되고 응답되는 과정이다.

---

### [핵심]

흐름:

```text
HTTP Request
→ DispatcherServlet
→ HandlerMapping
→ Controller
→ Service
→ Repository
→ Controller
→ MessageConverter
→ HTTP Response
```

---

### [실무]

Agent는 요청 오류 분석 시 아래 순서로 확인한다.

```text
URL / Method 확인
→ Controller Mapping 확인
→ Request Parameter / Body 확인
→ DTO Binding 확인
→ Validation 확인
→ Service Logic 확인
→ Exception Handler 확인
→ Response 확인
```

주의:

- 404는 Mapping 문제 가능
- 400은 Binding / Validation 문제 가능
- 500은 내부 예외 가능
- 401 / 403은 Security Filter 문제 가능
- JSON 변환 문제는 MessageConverter / DTO 구조 확인

---

### [FAQ]

Q. Spring Boot에서 요청은 어디로 먼저 들어와?

A.
일반적으로 DispatcherServlet이 요청을 받아 적절한 Controller Method로 전달한다.

Q. 400 Bad Request가 나면 뭘 확인해?

A.
Request Body, DTO 필드명, JSON 형식, 타입 변환, Validation 실패 여부를 확인한다.

---

## 7.2 Controller Mapping Rules

### [개념]

Controller Mapping은 HTTP Method와 URL Path를 Controller Method에 연결하는 규칙이다.

---

### [핵심]

Mapping Annotation:

- @RequestMapping
- @GetMapping
- @PostMapping
- @PutMapping
- @PatchMapping
- @DeleteMapping

Parameter Annotation:

- @PathVariable
- @RequestParam
- @RequestBody
- @ModelAttribute
- @RequestHeader

---

### [실무]

예:

```java
@RestController
@RequestMapping("/api/posts")
@RequiredArgsConstructor
public class PostController {

    private final PostService postService;

    @GetMapping("/{postId}")
    public ApiResponse<PostResponse> getPost(
            @PathVariable Long postId
    ) {
        return ApiResponse.success(postService.getPost(postId));
    }
}
```

선택 기준:

| Annotation      | 사용 상황                   |
| --------------- | --------------------------- |
| @PathVariable   | URL 경로 식별자             |
| @RequestParam   | Query String                |
| @RequestBody    | JSON Body                   |
| @ModelAttribute | Form / Query Object Binding |
| @RequestHeader  | Header 값                   |

---

### [FAQ]

Q. @RequestParam과 @PathVariable 차이는?

A.
@PathVariable은 URL 경로 일부를 받고 @RequestParam은 query string 값을 받는다.

Q. JSON 요청은 뭘로 받아?

A.
@RequestBody로 Request DTO를 받는다.

---

# 8. DTO and API Response Rules

## 8.1 Request DTO Rules

### [개념]

Request DTO는 Client가 Server로 보내는 요청 데이터를 표현하는 객체다.

---

### [핵심]

Request DTO 목적:

- API 입력 구조 정의
- Validation 적용
- Entity 직접 노출 방지
- Controller Boundary 명확화
- Request Field Naming 통일

---

### [실무]

예:

```java
public record PostCreateRequest(
        @NotBlank String title,
        @NotBlank String content
) {
}
```

권장:

- Request DTO와 Entity 분리
- Validation Annotation 적용
- API 별 DTO 분리
- 생성 / 수정 DTO 분리 가능
- 민감 필드 수신 주의
- 불필요한 Entity 필드 포함 금지

---

### [FAQ]

Q. Entity를 RequestBody로 받아도 돼?

A.
권장하지 않는다. API 입력 구조와 Entity 내부 구조가 강하게 결합되고 보안 문제가 생길 수 있다.

Q. 생성 DTO와 수정 DTO는 분리해야 해?

A.
필드와 검증 조건이 다르면 분리하는 것이 좋다.

---

## 8.2 Response DTO Rules

### [개념]

Response DTO는 Server가 Client에게 반환하는 응답 데이터를 표현하는 객체다.

---

### [핵심]

Response DTO 목적:

- 응답 필드 통제
- Entity 직접 노출 방지
- 민감정보 제거
- API 응답 형식 안정화
- Frontend 연동 안정성 확보

---

### [실무]

예:

```java
public record PostResponse(
        Long postId,
        String title,
        String content
) {
    public static PostResponse from(Post post) {
        return new PostResponse(
                post.getId(),
                post.getTitle(),
                post.getContent()
        );
    }
}
```

권장:

- Entity를 그대로 반환하지 않음
- 필요한 필드만 포함
- from / of 정적 팩토리 메서드 사용 가능
- 순환 참조 방지
- 민감정보 제외
- 날짜 포맷 기준 통일

---

### [FAQ]

Q. Entity를 그대로 Response로 반환해도 돼?

A.
권장하지 않는다. 민감정보 노출, Lazy Loading 문제, 순환 참조, API 변경 위험이 생길 수 있다.

Q. Response DTO 변환은 어디서 해?

A.
간단한 변환은 DTO의 static from 메서드나 Service에서 처리할 수 있다. 팀 규칙으로 일관화하는 것이 중요하다.

---

## 8.3 ApiResponse Convention Rules

### [개념]

ApiResponse Convention은 API 성공 / 실패 응답 형식을 일관되게 만드는 규칙이다.

---

### [핵심]

공통 응답 요소:

- success
- message
- data
- errorCode
- timestamp
- status

---

### [실무]

예:

```java
public record ApiResponse<T>(
        boolean success,
        String message,
        T data
) {
    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(true, "success", data);
    }
}
```

Controller 예:

```java
@GetMapping("/{postId}")
public ApiResponse<PostResponse> getPost(@PathVariable Long postId) {
    return ApiResponse.success(postService.getPost(postId));
}
```

권장:

- 성공 응답 형식 통일
- 실패 응답은 GlobalExceptionHandler에서 통일
- Error Code 체계 분리
- Frontend가 처리하기 쉬운 구조 유지
- ResponseEntity 사용 여부는 프로젝트 규칙으로 통일

---

### [FAQ]

Q. Controller에서 ApiResponse만 반환해도 돼?

A.
프로젝트 규칙이 성공 응답은 ApiResponse 직접 반환하고 실패는 GlobalExceptionHandler가 처리하는 구조라면 가능하다.

Q. ResponseEntity는 언제 써?

A.
HTTP 상태 코드, Header, Created Location 등 HTTP 응답을 세밀하게 제어해야 할 때 유용하다.

---

# 9. Validation Rules

## 9.1 Request Validation Rules

### [개념]

Validation은 Client 요청 값이 Application 요구 조건에 맞는지 확인하는 과정이다.

Spring Boot에서는 Bean Validation과 `@Valid`를 주로 사용한다.

---

### [핵심]

Validation Annotation:

- @Valid
- @Validated
- @NotNull
- @NotBlank
- @NotEmpty
- @Size
- @Min
- @Max
- @Email
- @Pattern
- @Positive
- @PositiveOrZero

---

### [실무]

예:

```java
public record SignUpRequest(
        @Email String email,
        @NotBlank String password,
        @NotBlank String nickname
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

권장:

- Request DTO에서 기본 검증
- 비즈니스 검증은 Service에서 처리
- Validation Error는 GlobalExceptionHandler에서 응답 통일
- null / blank / size 기준 명확화
- 메시지 관리 기준 통일

---

### [FAQ]

Q. @Valid는 어디에 붙여?

A.
Controller Method에서 Request DTO 앞에 붙여 요청 검증을 트리거한다.

Q. Validation과 비즈니스 검증 차이는?

A.
Validation은 형식과 기본 제약 검증이고 비즈니스 검증은 중복 이메일, 권한, 상태 전환 같은 도메인 규칙 검증이다.

---

## 9.2 Validation Error Handling Rules

### [개념]

Validation Error Handling은 DTO 검증 실패 시 Client에게 일관된 에러 응답을 반환하는 규칙이다.

---

### [핵심]

주요 예외:

- MethodArgumentNotValidException
- ConstraintViolationException
- BindException
- MissingServletRequestParameterException
- MethodArgumentTypeMismatchException

---

### [실무]

예:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ApiResponse<Void> handleValidationException(
            MethodArgumentNotValidException exception
    ) {
        return ApiResponse.fail("INVALID_REQUEST", "요청 값이 올바르지 않습니다.");
    }
}
```

권장:

- Validation Error 응답 형식 통일
- field error 포함 여부 결정
- 사용자 메시지와 개발자 로그 구분
- 민감한 내부 예외 메시지 노출 금지
- Frontend가 처리 가능한 errorCode 제공

---

### [FAQ]

Q. Validation 실패는 어디서 처리해?

A.
GlobalExceptionHandler에서 MethodArgumentNotValidException 등을 처리해 공통 에러 응답으로 변환한다.

Q. Validation 에러 메시지를 그대로 내려도 돼?

A.
가능하지만 내부 정보나 과도한 메시지가 노출되지 않도록 응답 형식을 통제하는 것이 좋다.

---

# 10. Exception Handling Rules

## 10.1 GlobalExceptionHandler Rules

### [개념]

GlobalExceptionHandler는 Application 전역 예외를 일관된 API Error Response로 변환하는 구조다.

Spring Boot에서는 `@RestControllerAdvice`와 `@ExceptionHandler`를 사용한다.

---

### [핵심]

포함 대상:

- CustomException
- Validation Exception
- Authentication / Authorization Exception
- Not Found Exception
- IllegalArgumentException
- RuntimeException fallback
- ErrorResponse
- ErrorCode

---

### [실무]

예:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(CustomException.class)
    public ApiResponse<Void> handleCustomException(CustomException exception) {
        return ApiResponse.fail(
                exception.getErrorCode(),
                exception.getMessage()
        );
    }
}
```

권장:

- 비즈니스 예외는 CustomException 사용
- ErrorCode Enum 사용 가능
- Validation Error 별도 처리
- 예상하지 못한 예외는 generic message 반환
- 실제 예외는 log로 기록
- HTTP status 정책은 프로젝트 규칙으로 통일

---

### [FAQ]

Q. 예외 처리는 어디서 해?

A.
Controller마다 try-catch하지 말고 GlobalExceptionHandler에서 공통 처리하는 것이 좋다.

Q. RuntimeException을 그대로 던져도 돼?

A.
가능은 하지만 비즈니스 의미가 있는 예외는 CustomException과 ErrorCode로 명확히 표현하는 것이 좋다.

---

## 10.2 Custom Exception Rules

### [개념]

Custom Exception은 Application의 비즈니스 오류를 명확히 표현하기 위한 예외다.

---

### [핵심]

구성 요소:

- ErrorCode
- message
- status
- business meaning
- exception hierarchy

---

### [실무]

예:

```java
public class BusinessException extends RuntimeException {

    private final String errorCode;

    public BusinessException(String errorCode, String message) {
        super(message);
        this.errorCode = errorCode;
    }

    public String getErrorCode() {
        return errorCode;
    }
}
```

사용:

```java
User user = userRepository.findById(userId)
        .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));
```

권장:

- 예외 이름은 의미 있게 작성
- ErrorCode와 메시지 분리
- Service에서 비즈니스 예외 발생
- Controller에서 직접 try-catch하지 않음
- 내부 예외와 사용자 응답 메시지 구분

---

### [FAQ]

Q. Custom Exception은 언제 만들어?

A.
사용자 없음, 권한 없음, 중복 데이터, 잘못된 상태 전환처럼 비즈니스 의미가 있는 오류에 사용한다.

Q. 예외 메시지는 어디서 관리해?

A.
간단한 프로젝트는 ErrorCode Enum이나 Exception 내부에서 관리하고, 규모가 커지면 메시지 관리 정책을 별도로 둔다.

---

# 11. Configuration and Properties Rules

## 11.1 Application Properties Rules

### [개념]

Application Properties는 Spring Boot Application 설정 값을 관리하는 파일이다.

`application.properties` 또는 `application.yml`을 사용할 수 있다.

---

### [핵심]

관리 대상:

- server port
- datasource
- jpa
- logging
- external api key
- file upload size
- profile
- cors
- jwt property
- mail property

---

### [실무]

예:

```yaml
server:
  port: 8080

spring:
  datasource:
    url: ${DB_URL}
    username: ${DB_USERNAME}
    password: ${DB_PASSWORD}
```

권장:

- 민감정보 하드코딩 금지
- 환경변수 사용
- profile 별 설정 분리
- 설정 key naming 통일
- 사용하지 않는 설정 제거
- unknown property 경고는 참조 방식 확인

---

### [FAQ]

Q. application.properties와 application.yml 중 뭐가 좋아?

A.
둘 다 가능하다. 중첩 구조가 많으면 yml이 읽기 쉽고 단순 설정은 properties도 충분하다.

Q. API Key를 properties에 직접 써도 돼?

A.
권장하지 않는다. 환경변수나 별도 secret 관리 방식을 사용하는 것이 좋다.

---

## 11.2 ConfigurationProperties Rules

### [개념]

ConfigurationProperties는 설정 값을 타입 안전한 객체로 바인딩하는 방식이다.

---

### [핵심]

사용 대상:

- 외부 API 설정
- JWT 설정
- 파일 업로드 설정
- CORS 설정
- 여러 관련 설정 묶음
- 타입 안정성 필요한 설정

---

### [실무]

예:

```java
@ConfigurationProperties(prefix = "tour-api")
public record TourApiProperties(
        String serviceKey,
        String baseUrl
) {
}
```

사용:

```java
@EnableConfigurationProperties(TourApiProperties.class)
@Configuration
public class AppConfig {
}
```

권장:

- 관련 설정을 객체로 묶음
- 문자열 하드코딩 줄임
- 테스트에서 설정 주입 쉬움
- 민감정보는 환경변수로 공급
- prefix naming 통일

---

### [FAQ]

Q. @Value와 @ConfigurationProperties 중 뭐가 좋아?

A.
단일 값은 @Value도 가능하지만 관련 설정이 여러 개면 @ConfigurationProperties가 구조화와 타입 안정성 측면에서 좋다.

Q. 환경변수는 왜 써?

A.
API Key, DB Password 같은 민감정보를 코드와 Git 저장소에 남기지 않기 위해 사용한다.

---

## 11.3 Profile Rules

### [개념]

Profile은 local, dev, test, prod 같은 실행 환경별 설정을 분리하는 기능이다.

---

### [핵심]

Profile 예:

- local
- dev
- test
- prod

사용 대상:

- DB 연결 정보
- logging level
- external API mode
- security option
- mock setting
- batch setting

---

### [실무]

예:

```yaml
spring:
  profiles:
    active: local
```

파일 구조:

```text
application.yml
application-local.yml
application-dev.yml
application-prod.yml
```

주의:

- prod 설정에 debug logging 남기지 않음
- local 설정을 prod에 섞지 않음
- test profile은 테스트 격리에 활용
- 민감정보는 profile 파일에 직접 커밋하지 않음

---

### [FAQ]

Q. Profile은 언제 써?

A.
로컬, 테스트, 운영 환경에서 DB, 로그, 외부 API 설정이 달라질 때 사용한다.

Q. 운영 설정 파일을 Git에 올려도 돼?

A.
민감정보가 포함될 수 있으므로 주의해야 한다. Secret은 환경변수나 별도 관리 방식을 사용한다.

---

# 12. Transaction Rules

## 12.1 Transaction Boundary Rules

### [개념]

Transaction Boundary는 하나의 비즈니스 작업을 원자적으로 처리하는 범위다.

Spring에서는 주로 Service Method에 `@Transactional`을 적용한다.

---

### [핵심]

적용 기준:

- 쓰기 작업
- 여러 Entity 변경
- 여러 Repository 호출 조합
- 실패 시 rollback 필요
- Lazy Loading 조회 범위
- 비즈니스 Use Case 단위

---

### [실무]

예:

```java
@Transactional
public OrderResponse createOrder(OrderCreateRequest request) {
    Order order = Order.create(request);
    orderRepository.save(order);

    return OrderResponse.from(order);
}
```

읽기 전용:

```java
@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    return PostResponse.from(post);
}
```

권장:

- Service public method에 적용
- 쓰기 작업은 기본 @Transactional
- 조회 작업은 readOnly = true 고려
- Controller에 Transaction 적용 지양
- private method의 @Transactional 동작 주의
- self-invocation 주의

---

### [FAQ]

Q. @Transactional은 어디에 붙여?

A.
대부분 Service의 public method에 붙인다. 비즈니스 작업 단위로 트랜잭션 경계를 잡는 것이 좋다.

Q. 조회 메서드에도 @Transactional이 필요해?

A.
JPA Lazy Loading이나 일관된 읽기 컨텍스트가 필요하면 readOnly = true로 적용할 수 있다.

---

## 12.2 Transaction Caution Rules

### [개념]

Transaction Caution은 Spring AOP 기반 Transaction이 기대와 다르게 동작할 수 있는 상황을 주의하는 규칙이다.

---

### [핵심]

주의 상황:

- private method @Transactional
- self-invocation
- checked exception rollback
- 외부 API 호출 포함
- 긴 Transaction
- readOnly 오해
- 비동기 메서드와 Transaction 경계

---

### [실무]

주의:

```text
Service public method
→ Transaction Proxy 적용
→ 내부 private method 직접 호출에는 별도 Transaction 적용 안 됨
```

권장:

- Transaction 안에서 외부 API 장시간 호출 지양
- DB 변경과 외부 시스템 호출 순서 설계
- RuntimeException rollback 기준 이해
- checked exception rollback 필요 시 rollbackFor 설정 검토
- Transaction 범위를 짧고 명확하게 유지

---

### [FAQ]

Q. 같은 클래스 안에서 @Transactional 메서드를 호출하면 동작해?

A.
Self-invocation 상황에서는 Proxy를 거치지 않아 기대한 Transaction이 적용되지 않을 수 있다.

Q. 모든 예외에서 rollback 돼?

A.
기본적으로 RuntimeException과 Error에서 rollback된다. Checked Exception은 별도 설정이 필요할 수 있다.

---

# 13. REST API Implementation Rules

## 13.1 REST Controller Rules

### [개념]

REST Controller는 JSON 기반 API 요청과 응답을 처리하는 Controller다.

Spring Boot에서는 `@RestController`를 사용한다.

---

### [핵심]

REST Controller 구성:

- @RestController
- @RequestMapping
- HTTP Method Mapping
- Request DTO
- Response DTO
- ApiResponse
- Validation
- Service 호출

---

### [실무]

예:

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

권장:

- URI는 명사 중심
- HTTP Method 의미 준수
- Request / Response DTO 분리
- 성공 응답 형식 통일
- 실패 응답은 예외 처리로 위임
- Controller Method 이름은 use case 표현

---

### [FAQ]

Q. @Controller와 @RestController 차이는?

A.
@Controller는 View 반환에 주로 사용하고 @RestController는 JSON 응답 API에 사용한다.

Q. REST API Controller에서는 뭘 반환해?

A.
프로젝트 규칙에 따라 Response DTO 또는 ApiResponse<Response DTO>를 반환한다.

---

## 13.2 Pagination Rules

### [개념]

Pagination은 목록 데이터를 일정 단위로 나누어 조회하는 방식이다.

Spring Data에서는 Pageable, Page, Slice를 사용할 수 있다.

---

### [핵심]

개념:

- Pageable
- Page
- Slice
- page
- size
- sort
- total count
- hasNext
- infinite scroll

---

### [실무]

예:

```java
@GetMapping
public ApiResponse<Slice<PostResponse>> getPosts(Pageable pageable) {
    return ApiResponse.success(postService.getPosts(pageable));
}
```

선택 기준:

| Type  | 특징                       | 사용 상황            |
| ----- | -------------------------- | -------------------- |
| Page  | total count 포함           | 페이지 번호 UI       |
| Slice | 다음 페이지 여부 중심      | 무한 스크롤 / 더보기 |
| List  | 전체 목록 또는 소량 데이터 | 작은 데이터          |

주의:

- 무한 스크롤은 Slice가 적합할 수 있음
- 대용량 데이터에서 count query 비용 주의
- 정렬 기준 명확화
- Pageable 기본 size 제한 고려

---

### [FAQ]

Q. Page와 Slice 차이는?

A.
Page는 전체 개수를 포함하고 Slice는 다음 페이지 존재 여부 중심이다. 무한 스크롤은 Slice가 적합할 수 있다.

Q. Pageable은 Controller에서 바로 받아도 돼?

A.
가능하다. 다만 기본 size, sort, 최대 size 정책을 정하는 것이 좋다.

---

# 14. Logging Rules

## 14.1 Logging Rules

### [개념]

Logging은 Application 동작, 오류, 요청 흐름을 추적하기 위해 기록을 남기는 작업이다.

---

### [핵심]

Logging 대상:

- Error
- Warning
- Important Business Event
- External API Call Result
- Security Event
- Startup Configuration
- Batch Result
- Debug Information

---

### [실무]

예:

```java
private static final Logger log = LoggerFactory.getLogger(PostService.class);

public PostResponse getPost(Long postId) {
    log.debug("getPost request. postId={}", postId);
    ...
}
```

권장:

- System.out.println 사용 지양
- log level 구분
- 민감정보 로그 금지
- 예외 stack trace는 서버 로그에 기록
- 사용자 응답과 로그 메시지 구분
- 운영 환경 debug log 주의

Log Level:

| Level | 사용 상황        |
| ----- | ---------------- |
| ERROR | 처리 실패 / 장애 |
| WARN  | 비정상 가능성    |
| INFO  | 주요 이벤트      |
| DEBUG | 개발 디버깅      |
| TRACE | 상세 추적        |

---

### [FAQ]

Q. System.out.println으로 로그 찍어도 돼?

A.
개발 중 임시 확인은 가능하지만 실무 코드에서는 Logger를 사용하는 것이 좋다.

Q. 로그에 토큰이나 비밀번호를 남겨도 돼?

A.
안 된다. 민감정보는 로그에 남기지 않는다.

---

# 15. CORS and External Integration Basics

## 15.1 CORS Basics

### [개념]

CORS는 다른 Origin의 Frontend가 Backend API에 접근할 수 있도록 허용할지 결정하는 브라우저 보안 정책이다.

---

### [핵심]

관련 개념:

- Origin
- Allowed Origin
- Allowed Method
- Allowed Header
- Credentials
- Preflight
- OPTIONS Request

---

### [실무]

기초 예:

```java
@Configuration
public class CorsConfig {
    // Security 사용 여부에 따라 설정 위치가 달라질 수 있음
}
```

주의:

- 개발 환경과 운영 환경 Origin 분리
- `*`와 credentials 조합 주의
- Spring Security 사용 시 SecurityFilterChain CORS 설정 확인
- Frontend URL 정확히 등록
- CORS는 인증/인가 대체 수단이 아님

---

### [FAQ]

Q. CORS 에러는 Backend 에러야?

A.
서버가 정상 응답해도 브라우저 보안 정책 때문에 차단될 수 있다. Origin, Method, Header, Credentials 설정을 확인해야 한다.

Q. CORS를 허용하면 보안 처리가 끝난 거야?

A.
아니다. CORS는 브라우저 접근 정책이고 실제 인증/인가는 별도로 처리해야 한다.

---

## 15.2 External API Integration Rules

### [개념]

External API Integration은 외부 API 서버와 통신해 데이터를 조회하거나 전송하는 기능이다.

---

### [핵심]

관리 대상:

- base url
- api key
- timeout
- retry basics
- error handling
- response mapping
- logging
- rate limit
- fallback

---

### [실무]

권장:

- API Key 하드코딩 금지
- 설정 값은 Properties로 분리
- 외부 응답 DTO와 내부 DTO 분리
- timeout 설정 고려
- 실패 응답 처리
- 외부 API 장애 시 사용자 메시지 통제
- 로그에 API Key 노출 금지

Flow:

```text
Service
→ ExternalApiClient
→ External API
→ Response DTO
→ Mapping
→ Service Result
```

---

### [FAQ]

Q. 외부 API 호출 코드는 Service에 바로 넣어도 돼?

A.
작은 프로젝트에서는 가능하지만 ExternalApiClient 같은 별도 Component로 분리하면 테스트와 유지보수가 쉬워진다.

Q. API Key는 어디에 둬?

A.
환경변수와 Configuration Properties를 통해 주입하는 것이 좋다.

---

# 16. Backend Integration Rules

## 16.1 Spring Boot with Java Rules

### [개념]

Spring Boot 코드는 Java 객체지향과 언어 규칙 위에서 작성된다.

Java Domain Rules의 객체지향, 예외, Optional, Stream, Collection 기준을 함께 따른다.

---

### [핵심]

연결 기준:

- Constructor Injection
- final field
- Interface / Implementation
- Optional 처리
- Custom Exception
- Collection return
- Stream mapping
- immutable DTO
- enum status

---

### [실무]

권장:

- Service 의존성은 final 필드
- Optional은 Service에서 처리
- DTO는 record 또는 불변 객체 고려
- 상태 값은 enum으로 표현
- null 반환보다 빈 컬렉션 반환 고려
- 예외는 명확한 타입으로 표현

---

### [FAQ]

Q. Spring Boot에서 Optional을 Controller까지 반환해도 돼?

A.
권장하지 않는다. Service에서 Optional을 처리하고 없으면 예외를 던지거나 명확한 응답으로 변환하는 것이 좋다.

---

## 16.2 Spring Boot with JPA Rules

### [개념]

Spring Boot에서 JPA는 Repository와 Entity를 통해 Database 접근을 추상화한다.

---

### [핵심]

연결 기준:

- Entity
- Repository
- Transaction
- Lazy Loading
- DTO Projection
- N+1 Caution
- Entity 변경 감지
- Dirty Checking

---

### [실무]

Spring Boot 문서에서는 아래 기준만 다룬다.

- Repository는 Entity 중심
- Service에서 Transaction 경계 설정
- Controller에 Entity 직접 반환 금지
- Lazy Loading 문제는 DTO 변환 시 주의
- 복잡한 JPA 이슈는 JPA Domain Rules 참조

---

### [FAQ]

Q. JPA Entity를 Controller에서 바로 반환하면 왜 안 좋아?

A.
Lazy Loading, 순환 참조, 민감정보 노출, API 응답 구조 불안정 문제가 생길 수 있다.

---

## 16.3 Spring Boot with Security Rules

### [개념]

Spring Boot Application은 Security 설정과 연동해 인증 / 인가 흐름을 처리할 수 있다.

---

### [핵심]

연결 기준:

- SecurityFilterChain
- Authentication
- Authorization
- Principal
- JWT
- CORS
- Protected Endpoint
- Role

---

### [실무]

Spring Boot 문서에서는 아래 기준만 포함한다.

- Controller는 인증 사용자 정보를 받을 수 있음
- 실제 인증/인가는 Security Filter에서 처리
- Frontend Auth State는 보안 기준이 아님
- Role 검증은 Backend에서 수행
- Security 심화는 Security Domain Rules 참조

---

### [FAQ]

Q. Controller에서 userId를 RequestBody로 받으면 돼?

A.
인증된 사용자 기준 작업이라면 RequestBody의 userId보다 SecurityContext나 인증 Principal에서 가져오는 것이 안전하다.

---

# 17. Troubleshooting Rules

## 17.1 Bean Not Found Problem

### [개념]

Bean Not Found Problem은 Spring Container가 필요한 Bean을 찾지 못해 Application 실행 또는 주입에 실패하는 문제다.

---

### [핵심]

원인:

- Annotation 누락
- Component Scan 범위 밖
- Interface 구현체 없음
- Bean 이름 충돌
- Profile 조건 불일치
- Configuration 누락

---

### [실무]

Debug Flow:

```text
Error Message 확인
→ 필요한 Bean Type 확인
→ Annotation 확인
→ Package 위치 확인
→ Component Scan 범위 확인
→ Profile 조건 확인
→ Configuration 확인
```

해결:

- @Service / @Component 등 등록 확인
- Main Class 위치 확인
- @Bean 등록 확인
- 구현체 등록 확인
- Profile 활성화 확인

---

### [FAQ]

Q. NoSuchBeanDefinitionException이 나면 뭘 확인해?

A.
해당 클래스가 Bean으로 등록되었는지, Component Scan 범위 안에 있는지, 필요한 Profile이 활성화되어 있는지 확인한다.

---

## 17.2 Mapping Not Found Problem

### [개념]

Mapping Not Found Problem은 요청 URL과 HTTP Method에 맞는 Controller Method를 찾지 못하는 문제다.

---

### [핵심]

원인:

- URL 오타
- HTTP Method 불일치
- @RequestMapping prefix 누락
- Controller Bean 등록 실패
- API base path 불일치
- Frontend Axios URL 불일치

---

### [실무]

Debug Flow:

```text
Frontend Request URL 확인
→ HTTP Method 확인
→ Controller @RequestMapping 확인
→ Method Mapping 확인
→ PathVariable 이름 확인
→ Security 차단 여부 확인
```

주의:

- `/festival`과 `/festivals` 혼동 주의
- Controller prefix와 method path 합쳐서 확인
- Frontend Axios baseURL 확인
- SPA routing 문제와 API mapping 문제 구분

---

### [FAQ]

Q. 404가 나면 무조건 Controller가 없는 거야?

A.
아니다. URL, HTTP Method, prefix, Security, Frontend baseURL, SPA routing 문제를 함께 확인해야 한다.

---

## 17.3 Request Binding Problem

### [개념]

Request Binding Problem은 Client 요청 데이터가 Controller Parameter나 DTO에 제대로 매핑되지 않는 문제다.

---

### [핵심]

원인:

- JSON 필드명 불일치
- 타입 불일치
- 기본 생성자 / record 매핑 문제
- @RequestBody 누락
- @RequestParam / @PathVariable 혼동
- Content-Type 누락
- 날짜 포맷 불일치

---

### [실무]

Debug Flow:

```text
Request Payload 확인
→ Content-Type 확인
→ Controller Parameter Annotation 확인
→ DTO Field Name 확인
→ DTO Type 확인
→ Validation Error 확인
→ Jackson Error 확인
```

---

### [FAQ]

Q. RequestBody 값이 null로 들어오면?

A.
@RequestBody 누락, JSON 필드명 불일치, Content-Type, DTO 구조, Jackson 변환 오류를 확인한다.

Q. Query String은 @RequestBody로 받아?

A.
아니다. Query String은 @RequestParam 또는 @ModelAttribute로 받는다.

---

## 17.4 Transaction Not Working Problem

### [개념]

Transaction Not Working Problem은 `@Transactional`을 붙였지만 rollback, dirty checking, lazy loading이 기대대로 동작하지 않는 문제다.

---

### [핵심]

원인:

- private method에 적용
- self-invocation
- checked exception
- Transaction 밖 Entity 변경
- readOnly 오해
- Proxy 적용 안 됨
- 테스트 환경 오해

---

### [실무]

Debug Flow:

```text
@Transactional 위치 확인
→ public method 여부 확인
→ 외부 Bean 호출 여부 확인
→ Exception Type 확인
→ Entity 영속 상태 확인
→ Transaction 범위 확인
```

---

### [FAQ]

Q. @Transactional을 붙였는데 rollback이 안 돼?

A.
예외 타입, self-invocation, 메서드 접근제어자, rollbackFor 설정, Transaction Proxy 적용 여부를 확인해야 한다.

---

# 18. Comparison Rules

## 18.1 Required Comparisons

### [개념]

Spring Boot 문서는 헷갈리는 개념을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- @Controller vs @RestController
- @Component vs @Service vs @Repository
- @RequestParam vs @PathVariable
- @RequestBody vs @ModelAttribute
- DTO vs Entity
- Controller vs Service
- Service vs Component
- @Value vs @ConfigurationProperties
- Page vs Slice
- Validation vs Business Validation
- Checked Exception vs Runtime Exception
- application.properties vs application.yml
- @Transactional vs no Transaction
- Constructor Injection vs Field Injection

---

### [실무]

예시:

| 비교      | DTO             | Entity           |
| --------- | --------------- | ---------------- |
| 목적      | API 입출력      | DB / Domain 모델 |
| 위치      | Controller 경계 | Persistence 영역 |
| 변경 기준 | API 스펙        | DB / 도메인      |
| 노출      | 외부 노출 가능  | 직접 노출 지양   |
| 검증      | Request 검증    | 도메인 무결성    |

---

### [FAQ]

Q. Comparison은 왜 필요해?

A.
Spring Boot는 Annotation과 Layer 개념이 많아 비슷한 역할을 혼동하기 쉽기 때문이다.

Q. 가장 중요한 비교는 뭐야?

A.
DTO vs Entity, Controller vs Service, @RequestParam vs @PathVariable, Constructor Injection vs Field Injection이다.

---

# 19. Checklist Rules

## 19.1 Spring Boot Checklist

### [개념]

Spring Boot 문서 검수 시 Backend Application 구조 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] Layered Architecture가 포함되었는가?
- [ ] Controller / Service / Repository 책임이 구분되었는가?
- [ ] Controller Thin Rule이 포함되었는가?
- [ ] Service Business Logic Rule이 포함되었는가?
- [ ] Repository Responsibility Rule이 포함되었는가?
- [ ] Dependency Injection 기준이 포함되었는가?
- [ ] Constructor Injection 우선 기준이 포함되었는가?
- [ ] Bean 등록 방식이 포함되었는가?
- [ ] Circular Dependency 주의가 포함되었는가?
- [ ] Spring MVC Request Flow가 포함되었는가?
- [ ] Controller Mapping 기준이 포함되었는가?
- [ ] Request DTO / Response DTO 분리 기준이 포함되었는가?
- [ ] ApiResponse Convention 기준이 포함되었는가?
- [ ] Validation 기준이 포함되었는가?
- [ ] GlobalExceptionHandler 기준이 포함되었는가?
- [ ] Configuration / Properties 기준이 포함되었는가?
- [ ] Profile 기준이 포함되었는가?
- [ ] Transaction Boundary 기준이 포함되었는가?
- [ ] Pagination 기준이 포함되었는가?
- [ ] Logging 기준이 포함되었는가?
- [ ] CORS 기초 기준이 포함되었는가?
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
→ Layer Check
→ DI Check
→ Request Flow Check
→ DTO Check
→ Validation Check
→ Exception Check
→ Transaction Check
→ Configuration Check
→ Troubleshooting Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. Spring Boot 문서 검수에서 가장 중요한 것은?

A.
Layer 책임 분리, DTO 분리, 예외 처리 일관성, Transaction 경계, 설정 값 관리, Anti Pattern 포함 여부다.

---

# 20. Retrieval Optimization Rules

## 20.1 Keyword Rules

### [개념]

Spring Boot 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- Spring Boot
- Spring MVC
- Controller
- RestController
- Service
- Repository
- Layered Architecture
- Dependency Injection
- Bean
- Component Scan
- Constructor Injection
- Field Injection
- DTO
- Request DTO
- Response DTO
- Entity
- ApiResponse
- Validation
- @Valid
- GlobalExceptionHandler
- RestControllerAdvice
- CustomException
- ErrorCode
- Configuration
- application.yml
- application.properties
- Profile
- ConfigurationProperties
- Transaction
- @Transactional
- Pageable
- Page
- Slice
- CORS
- Logging
- Request Mapping
- PathVariable
- RequestParam
- RequestBody
- ModelAttribute
- Backend API
- Anti Pattern

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- Spring Boot 구조는 어떻게 잡아?
- Controller Service Repository 차이는?
- Controller에서 Repository 바로 호출해도 돼?
- DTO와 Entity 차이는?
- Entity를 그대로 반환하면 안 되는 이유는?
- @RequestParam과 @PathVariable 차이는?
- @RequestBody는 언제 써?
- @Valid는 어디에 붙여?
- 예외 처리는 어디서 해?
- GlobalExceptionHandler는 왜 필요해?
- @Transactional은 어디에 붙여?
- 생성자 주입을 왜 써?
- Field Injection은 왜 안 좋아?
- application.yml에 API Key 써도 돼?
- Page와 Slice 차이는?
- 404가 나면 뭘 확인해?
- RequestBody가 null이면 뭘 확인해?
- Bean 등록이 안 되면 뭘 확인해?

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 반복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. Spring Boot FAQ 질문은 어떤 스타일이 좋아?

A.
실제 개발 중 자주 묻는 오류, 구조, Annotation 차이, Layer 책임 질문 형태가 좋다.

---

# 21. Version Rules

## 21.1 Modern Spring Boot 기준

### [개념]

Spring Boot 문서는 Modern Spring Boot 기준으로 작성한다.

---

### [핵심]

기준:

- Spring Boot 3.x
- Java 17+
- Jakarta Namespace
- Spring MVC
- Constructor Injection
- DTO Separation
- Bean Validation
- RestControllerAdvice
- ConfigurationProperties
- Layered Architecture
- Testable Service Design
- API Response Convention

Legacy 제외:

- XML 설정 중심
- Field Injection 중심
- Entity 직접 반환 중심
- Controller 비즈니스 로직 중심
- JSP 중심 설명
- 구형 javax 중심 설명
- 무분별한 static util 남용
- 모든 예외 Controller try-catch 처리
- application 설정에 민감정보 하드코딩

---

### [실무]

실무 기준:

```text
Modern Spring Boot
→ Layer Responsibility
→ Constructor Injection
→ DTO Boundary
→ Validation
→ Global Exception Handling
→ Transaction Boundary
→ Configuration Separation
→ Testable Code
```

---

### [FAQ]

Q. Spring Boot 3에서는 javax를 써?

A.
Spring Boot 3 기준에서는 Jakarta EE 전환으로 jakarta 패키지를 사용하는 경우가 많다.

Q. XML 설정을 배워야 해?

A.
기존 프로젝트 유지보수에서는 볼 수 있지만 신규 Spring Boot Foundation 문서는 Java Config와 Annotation 기반을 우선한다.

---

# 22. Common Mistakes

## 22.1 Spring Boot Common Mistakes

### [개념]

Spring Boot 문서는 자주 발생하는 구조 / 설정 / 요청 처리 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

- Controller에 비즈니스 로직 과다 작성
- Controller에서 Repository 직접 호출
- Entity를 RequestBody로 사용
- Entity를 Response로 직접 반환
- DTO 없이 API 구성
- Request DTO와 Response DTO 혼용
- Validation 누락
- GlobalExceptionHandler 없이 Controller try-catch 반복
- Field Injection 사용
- 순환 참조 발생
- Service 책임 과다
- Transaction 위치 오류
- @Transactional self-invocation 오해
- application.yml에 민감정보 하드코딩
- Profile 설정 혼동
- CORS와 인증 문제 혼동
- URL prefix 불일치
- @RequestParam / @PathVariable 혼동
- @RequestBody 누락
- Page와 Slice 선택 기준 없음
- System.out.println 로그 사용
- Error Response 형식 불일치

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: 프론트에서 API 호출 시 404
원인: Controller @RequestMapping("/festivals")인데 Axios는 "/festival" 호출
해결: Controller prefix와 Frontend URL을 일치시킴
```

예:

```text
문제: RequestBody 값이 null
원인: @RequestBody 누락 또는 JSON 필드명 불일치
해결: Controller Parameter Annotation과 DTO 필드명 확인
```

---

### [FAQ]

Q. Spring Boot 초보가 가장 많이 하는 실수는?

A.
Controller에 모든 로직을 넣거나 Entity를 그대로 Request / Response에 사용하는 실수가 많다.

Q. Spring Boot 문제는 어떻게 찾는 게 좋아?

A.
요청 URL, Controller Mapping, DTO Binding, Validation, Service Logic, Repository Query, Exception Handler 순서로 확인한다.

---

# 23. Final Goal

## 23.1 Domain Final Goal

### [개념]

Spring Boot RAG 문서는 Backend Agent가 Spring Boot Application의 구조를 설계하고 Controller / Service / Repository / DTO / 예외 처리 / 설정 / 트랜잭션을 일관되게 구현하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- Spring Boot Application Structure 설계
- Layered Architecture 적용
- Controller Thin Rule 준수
- Service Business Logic 배치
- Repository Responsibility 분리
- Constructor Injection 적용
- Bean 등록 방식 판단
- Circular Dependency 탐지
- Spring MVC Request Flow 이해
- Controller Mapping 설계
- Request DTO / Response DTO 분리
- ApiResponse Convention 적용
- Validation 적용
- GlobalExceptionHandler 구성
- Custom Exception 설계
- Configuration / Properties 관리
- Profile 분리
- Transaction Boundary 설정
- Pagination 기준 선택
- Logging 기준 적용
- CORS 기초 문제 분석
- Backend Integration 판단
- Spring Boot Anti Pattern 탐지

---

### [실무]

Agent 수행 가능 작업:

```text
User Backend Request
→ Identify API Use Case
→ Design Controller Endpoint
→ Design Request / Response DTO
→ Place Business Logic in Service
→ Use Repository for Data Access
→ Apply Validation
→ Apply Transaction Boundary
→ Apply Exception Handling
→ Review Configuration
→ Check Anti Pattern
→ Spring Boot Output
```

---

### [FAQ]

Q. Spring Boot 문서의 최종 목적은 뭐야?

A.
Backend Agent가 Spring Boot 코드를 단순히 생성하는 것이 아니라 Layer 책임, DTO 경계, 예외 처리, 트랜잭션, 설정 기준까지 검토하면서 안정적인 Backend 구조를 만들게 하는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
JPA Advanced, Security Advanced, API Design, Testing Domain Rules와 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Spring Boot Domain Rules는 왜 필요해?
A. Backend Agent가 Spring Boot Application 구조, Layer 책임, REST API, DTO, 예외 처리, 설정, 트랜잭션을 일관되게 설계해야 하기 때문이다.

Q. Spring Boot 구조는 어떻게 잡아?
A. 기초 단계에서는 controller, service, repository, entity, dto, config, exception 중심의 Layer 구조가 좋다.

Q. Spring Boot 패키지 구조는 어떻게 나눠?
A. Controller, Service, Repository, Entity, DTO, Config, Exception처럼 책임 기준으로 나눈다.

Q. @SpringBootApplication은 뭐야?
A. Spring Boot Application 시작 Annotation이며 Component Scan, Auto Configuration, Configuration 역할을 포함한다.

Q. Main Class 위치가 중요한 이유는?
A. 기본 Component Scan이 Main Class가 있는 패키지 하위 기준으로 동작하기 때문이다.

Q. Controller Service Repository 차이는?
A. Controller는 HTTP 요청/응답, Service는 비즈니스 로직과 트랜잭션, Repository는 데이터 접근을 담당한다.

Q. Controller에서 Repository를 바로 호출해도 돼?
A. 실무 구조에서는 Service를 거쳐 비즈니스 로직과 트랜잭션 경계를 관리하는 것이 좋다.

Q. Service는 왜 필요해?
A. 비즈니스 로직, 트랜잭션, 여러 Repository 조합, 예외 처리를 Controller에서 분리하기 위해 필요하다.

Q. Controller는 어디까지 해야 해?
A. 요청을 받고 검증을 트리거한 뒤 Service를 호출하고 응답을 반환하는 정도가 적합하다.

Q. Controller에 비즈니스 로직이 많으면 왜 문제야?
A. 테스트가 어려워지고 HTTP 책임과 비즈니스 책임이 섞여 유지보수가 어려워진다.

Q. Service에는 어떤 로직을 넣어?
A. 비즈니스 규칙, 트랜잭션, Repository 조합, Entity 변경, 예외 처리를 넣는다.

Q. Service가 너무 커지면 어떻게 해?
A. 기능별 Service 분리, 도메인 책임 분리, 별도 Component 분리를 검토한다.

Q. Repository에는 어떤 로직을 넣어?
A. Entity 저장, 조회, 삭제, Query Method처럼 데이터 접근 로직을 넣는다.

Q. Repository에 비즈니스 로직을 넣어도 돼?
A. 권장하지 않는다. Repository는 데이터 접근 책임에 집중하고 비즈니스 판단은 Service나 Domain에서 처리한다.

Q. Spring Boot에서 의존성 주입은 뭘 써야 해?
A. 생성자 주입을 우선한다. final 필드와 함께 쓰면 필수 의존성이 명확해진다.

Q. Field Injection은 왜 비권장이야?
A. 테스트가 어렵고 필수 의존성이 숨겨지며 불변성을 보장하기 어렵다.

Q. @Component와 @Service 차이는 뭐야?
A. 기능적으로 Bean 등록은 같지만 @Service는 비즈니스 서비스 계층이라는 의미를 명확히 표현한다.

Q. @Bean은 언제 써?
A. 외부 라이브러리 객체처럼 클래스에 직접 @Component를 붙일 수 없을 때 사용한다.

Q. 순환 참조가 생기면 어떻게 해?
A. 의존 방향과 책임을 다시 보고 공통 로직 분리, Service 재분리, 이벤트 구조를 검토한다.

Q. Spring MVC 요청 흐름은?
A. HTTP Request가 DispatcherServlet을 거쳐 Controller, Service, Repository로 전달되고 다시 응답으로 반환된다.

Q. 400 Bad Request가 나면 뭘 확인해?
A. Request Body, DTO 필드명, JSON 형식, 타입 변환, Validation 실패 여부를 확인한다.

Q. 404가 나면 뭘 확인해?
A. URL, HTTP Method, Controller prefix, Method Mapping, Frontend baseURL, Security 차단 여부를 확인한다.

Q. @RequestParam과 @PathVariable 차이는?
A. @PathVariable은 URL 경로 일부를 받고 @RequestParam은 query string 값을 받는다.

Q. @RequestBody는 언제 써?
A. JSON Body 요청을 Request DTO로 받을 때 사용한다.

Q. @ModelAttribute는 언제 써?
A. Query parameter나 form 데이터를 객체로 바인딩할 때 사용할 수 있다.

Q. DTO와 Entity 차이는?
A. DTO는 API 입출력 데이터이고 Entity는 DB와 도메인 구조를 표현하는 내부 모델이다.

Q. Entity를 RequestBody로 받아도 돼?
A. 권장하지 않는다. API 입력 구조와 Entity 내부 구조가 강하게 결합되고 보안 문제가 생길 수 있다.

Q. Entity를 그대로 Response로 반환해도 돼?
A. 권장하지 않는다. 민감정보 노출, Lazy Loading 문제, 순환 참조, API 변경 위험이 생길 수 있다.

Q. Request DTO와 Response DTO는 분리해야 해?
A. 요청과 응답의 필드와 검증 기준이 다르면 분리하는 것이 좋다.

Q. ApiResponse는 왜 써?
A. 성공 / 실패 응답 형식을 통일해 Frontend가 일관되게 처리하도록 하기 위해 사용한다.

Q. Controller에서 ApiResponse만 반환해도 돼?
A. 프로젝트 규칙이 성공 응답은 ApiResponse 직접 반환하고 실패는 GlobalExceptionHandler가 처리하는 구조라면 가능하다.

Q. ResponseEntity는 언제 써?
A. HTTP 상태 코드, Header, Created Location 등 HTTP 응답을 세밀하게 제어해야 할 때 유용하다.

Q. @Valid는 어디에 붙여?
A. Controller Method에서 Request DTO 앞에 붙여 요청 검증을 트리거한다.

Q. Validation과 비즈니스 검증 차이는?
A. Validation은 형식과 기본 제약 검증이고 비즈니스 검증은 중복, 권한, 상태 전환 같은 도메인 규칙 검증이다.

Q. Validation 실패는 어디서 처리해?
A. GlobalExceptionHandler에서 MethodArgumentNotValidException 등을 처리해 공통 에러 응답으로 변환한다.

Q. 예외 처리는 어디서 해?
A. Controller마다 try-catch하지 말고 GlobalExceptionHandler에서 공통 처리하는 것이 좋다.

Q. GlobalExceptionHandler는 왜 필요해?
A. Application 전역 예외를 일관된 API Error Response로 변환하기 위해 필요하다.

Q. Custom Exception은 언제 만들어?
A. 사용자 없음, 권한 없음, 중복 데이터, 잘못된 상태 전환처럼 비즈니스 의미가 있는 오류에 사용한다.

Q. application.properties와 application.yml 중 뭐가 좋아?
A. 둘 다 가능하다. 중첩 구조가 많으면 yml이 읽기 쉽고 단순 설정은 properties도 충분하다.

Q. API Key를 properties에 직접 써도 돼?
A. 권장하지 않는다. 환경변수나 별도 secret 관리 방식을 사용하는 것이 좋다.

Q. @Value와 @ConfigurationProperties 중 뭐가 좋아?
A. 단일 값은 @Value도 가능하지만 관련 설정이 여러 개면 @ConfigurationProperties가 구조화와 타입 안정성 측면에서 좋다.

Q. Profile은 언제 써?
A. 로컬, 테스트, 운영 환경에서 DB, 로그, 외부 API 설정이 달라질 때 사용한다.

Q. @Transactional은 어디에 붙여?
A. 대부분 Service의 public method에 붙인다. 비즈니스 작업 단위로 트랜잭션 경계를 잡는 것이 좋다.

Q. 조회 메서드에도 @Transactional이 필요해?
A. JPA Lazy Loading이나 일관된 읽기 컨텍스트가 필요하면 readOnly = true로 적용할 수 있다.

Q. 같은 클래스 안에서 @Transactional 메서드를 호출하면 동작해?
A. Self-invocation 상황에서는 Proxy를 거치지 않아 기대한 Transaction이 적용되지 않을 수 있다.

Q. 모든 예외에서 rollback 돼?
A. 기본적으로 RuntimeException과 Error에서 rollback된다. Checked Exception은 별도 설정이 필요할 수 있다.

Q. @Controller와 @RestController 차이는?
A. @Controller는 View 반환에 주로 사용하고 @RestController는 JSON 응답 API에 사용한다.

Q. Page와 Slice 차이는?
A. Page는 전체 개수를 포함하고 Slice는 다음 페이지 존재 여부 중심이다. 무한 스크롤은 Slice가 적합할 수 있다.

Q. Pageable은 Controller에서 바로 받아도 돼?
A. 가능하다. 다만 기본 size, sort, 최대 size 정책을 정하는 것이 좋다.

Q. System.out.println으로 로그 찍어도 돼?
A. 개발 중 임시 확인은 가능하지만 실무 코드에서는 Logger를 사용하는 것이 좋다.

Q. 로그에 토큰이나 비밀번호를 남겨도 돼?
A. 안 된다. 민감정보는 로그에 남기지 않는다.

Q. CORS 에러는 Backend 에러야?
A. 서버가 정상 응답해도 브라우저 보안 정책 때문에 차단될 수 있다. Origin, Method, Header, Credentials 설정을 확인해야 한다.

Q. 외부 API 호출 코드는 Service에 바로 넣어도 돼?
A. 작은 프로젝트에서는 가능하지만 ExternalApiClient 같은 별도 Component로 분리하면 테스트와 유지보수가 쉬워진다.

Q. NoSuchBeanDefinitionException이 나면 뭘 확인해?
A. 해당 클래스가 Bean으로 등록되었는지, Component Scan 범위 안에 있는지, 필요한 Profile이 활성화되어 있는지 확인한다.

Q. RequestBody 값이 null로 들어오면?
A. @RequestBody 누락, JSON 필드명 불일치, Content-Type, DTO 구조, Jackson 변환 오류를 확인한다.

Q. @Transactional을 붙였는데 rollback이 안 돼?
A. 예외 타입, self-invocation, 메서드 접근제어자, rollbackFor 설정, Transaction Proxy 적용 여부를 확인해야 한다.

Q. Spring Boot 초보가 가장 많이 하는 실수는?
A. Controller에 모든 로직을 넣거나 Entity를 그대로 Request / Response에 사용하는 실수가 많다.

Q. Spring Boot 문제는 어떻게 찾는 게 좋아?
A. 요청 URL, Controller Mapping, DTO Binding, Validation, Service Logic, Repository Query, Exception Handler 순서로 확인한다.

Q. Spring Boot 다음 문서는 뭐가 좋아?
A. JPA Advanced, Security Advanced, API Design, Testing Domain Rules와 이어지는 것이 좋다.
