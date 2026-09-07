# Spring Boot Part10 - Dependency Injection & Bean Lifecycle

---

# 1. Dependency Injection

## 1.1 Dependency Injection 개념

### [개념]

Dependency Injection은 객체가 필요한 의존 객체를 직접 생성하지 않고 Spring Container로부터 주입받는 방식이다.

Spring Boot에서는 Controller, Service, Repository, Component, Configuration Bean들이 Spring Container에 등록되고 필요한 곳에 주입된다.

Dependency Injection의 목적:

- 객체 생성 책임 분리
- Layer 간 의존성 명확화
- 테스트 가능한 구조 생성
- 구현체 교체 용이성 확보
- 순환 참조 탐지
- Bean Lifecycle 관리
- Backend Agent 코드 생성 기준 제공
- Review Agent DI 구조 검수 기준 제공

기본 흐름:

```text
Spring Container
→ Bean 생성
→ Dependency 주입
→ Bean 초기화
→ Application 실행
→ Bean 사용
→ Application 종료 시 Bean 정리
```

---

### [핵심]

Dependency Injection 핵심 키워드:

- DI
- IoC
- Spring Container
- ApplicationContext
- Bean
- Component Scan
- Constructor Injection
- Field Injection
- Setter Injection
- Circular Dependency
- Bean Lifecycle
- `@Component`
- `@Service`
- `@Repository`
- `@Controller`
- `@RestController`
- `@Configuration`
- `@Bean`

DI 핵심 규칙:

- 직접 `new`로 Service / Repository를 생성하지 않는다.
- Spring Bean은 Spring Container가 생성하고 관리한다.
- 의존성 주입은 생성자 주입을 우선 사용한다.
- 필드는 `final`로 선언한다.
- Field Injection은 지양한다.
- 순환 참조가 생기면 구조 문제로 보고 책임을 재검토한다.
- Bean 등록 방식과 사용 위치를 일관되게 유지한다.

---

### [실무]

권장 구조:

```java
@Service
@RequiredArgsConstructor
public class PostService {

    private final PostRepository postRepository;

    @Transactional(readOnly = true)
    public PostResponse getPost(Long postId) {
        Post post = postRepository.findById(postId)
                .orElseThrow(() -> new BusinessException(ErrorCode.POST_NOT_FOUND));

        return PostResponse.from(post);
    }
}
```

Controller:

```java
@RestController
@RequestMapping("/api/posts")
@RequiredArgsConstructor
public class PostController {

    private final PostService postService;

    @GetMapping("/{postId}")
    public ApiResponse<PostResponse> getPost(@PathVariable Long postId) {
        return ApiResponse.success(postService.getPost(postId));
    }
}
```

의미:

```text
PostController
→ PostService Bean 주입
→ PostService
→ PostRepository Bean 주입
→ Repository를 통해 DB 접근
```

권장:

- 직접 만든 비즈니스 클래스는 `@Service`, `@Component` 등으로 Bean 등록
- 외부 라이브러리 객체는 `@Bean`으로 등록
- 생성자 주입 사용
- Lombok 사용 시 `@RequiredArgsConstructor` 활용 가능
- Service는 Repository Interface에 의존
- Controller는 Service에 의존
- Repository는 Entity 중심으로 동작

---

### [FAQ]

Q. Dependency Injection은 왜 필요해?

A. 객체 생성과 사용 책임을 분리해 코드 결합도를 낮추고 테스트와 유지보수를 쉽게 하기 위해 필요하다.

Q. Spring Bean은 누가 만들어?

A. Spring Container가 Component Scan이나 `@Bean` 설정을 통해 Bean을 생성하고 관리한다.

Q. Service에서 Repository를 `new`로 만들면 안 돼?

A. 권장하지 않는다. Spring Data JPA Repository는 Spring이 Proxy 구현체를 생성하므로 Container를 통해 주입받아야 한다.

---

# 2. IoC Container와 Bean

## 2.1 IoC Container 개념

### [개념]

IoC는 Inversion of Control의 약자다.

객체 생성과 의존성 연결 제어권을 개발자 코드가 아니라 Spring Container가 가지는 구조를 의미한다.

Spring Boot에서 IoC Container는 ApplicationContext로 볼 수 있으며, Application 실행 중 Bean을 생성하고 관리한다.

---

### [핵심]

IoC Container 역할:

- Bean 생성
- Bean 의존성 주입
- Bean 초기화
- Bean Scope 관리
- Bean Lifecycle 관리
- Configuration 적용
- AOP Proxy 적용
- Transaction Proxy 연결

Bean이 되는 대상:

- `@Component`
- `@Service`
- `@Repository`
- `@Controller`
- `@RestController`
- `@Configuration`
- `@Bean` method 반환 객체

---

### [실무]

Spring Boot Application 실행 흐름:

```text
main method 실행
→ SpringApplication.run
→ ApplicationContext 생성
→ Component Scan
→ Bean Definition 등록
→ Bean 생성
→ 의존성 주입
→ 초기화 callback 실행
→ Application 실행 준비 완료
```

예:

```java
@SpringBootApplication
public class ProjectApplication {

    public static void main(String[] args) {
        SpringApplication.run(ProjectApplication.class, args);
    }
}
```

`@SpringBootApplication`은 기본적으로 Main Application Class가 위치한 패키지 하위의 Component를 Scan한다.

권장:

- Main Application Class는 최상위 패키지에 둔다.
- Bean으로 등록해야 하는 클래스는 Component Scan 범위 안에 둔다.
- Bean 등록 실패 시 Main Class 위치와 Annotation을 먼저 확인한다.
- Bean 생성 책임과 비즈니스 로직 책임을 섞지 않는다.

---

### [FAQ]

Q. IoC Container는 뭐야?

A. 객체 생성, 의존성 주입, 생명주기 관리를 담당하는 Spring의 핵심 Container다.

Q. ApplicationContext는 뭐야?

A. Spring Bean을 생성하고 관리하는 대표적인 IoC Container다.

Q. Bean은 일반 객체랑 뭐가 달라?

A. Bean은 Spring Container가 생성하고 관리하는 객체다. 일반 객체는 개발자가 직접 생성하고 관리한다.

---

## 2.2 Bean 등록 방식

### [개념]

Bean 등록 방식은 객체를 Spring Container가 관리하도록 등록하는 방법이다.

Spring Boot에서는 Component Scan 방식과 Java Configuration 방식이 주로 사용된다.

---

### [핵심]

Bean 등록 방식:

| 방식                   | 사용 대상             | 예                          |
| ---------------------- | --------------------- | --------------------------- |
| Component Scan         | 직접 작성한 클래스    | `@Service`, `@Component`    |
| Java Configuration     | 외부 라이브러리 객체  | `@Configuration`, `@Bean`   |
| Spring Data Repository | Repository Interface  | `JpaRepository` 상속        |
| Auto Configuration     | Spring Boot 자동 설정 | DataSource, ObjectMapper 등 |

---

### [실무]

Component Scan 방식:

```java
@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
}
```

Java Configuration 방식:

```java
@Configuration
public class PasswordConfig {

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

Repository Bean:

```java
public interface UserRepository extends JpaRepository<User, Long> {
}
```

권장 기준:

```text
직접 만든 Service / Component
→ @Service / @Component

외부 라이브러리 객체
→ @Configuration + @Bean

Spring Data JPA Repository
→ JpaRepository 상속
```

---

### [주의]

비권장:

```java
@Configuration
public class AppConfig {

    @Bean
    public UserService userService() {
        return new UserService(new UserRepository());
    }
}
```

문제:

- Repository 직접 생성 불가
- Spring Data JPA Proxy 우회
- DI 흐름 깨짐
- 테스트와 유지보수 어려움
- Bean 생성 책임 혼란

---

### [FAQ]

Q. 직접 만든 Service도 `@Bean`으로 등록해도 돼?

A. 가능은 하지만 일반적으로 직접 만든 Service는 `@Service`와 생성자 주입을 사용하는 것이 더 명확하다.

Q. 외부 라이브러리 객체는 어떻게 Bean으로 등록해?

A. `@Configuration` 클래스에서 `@Bean` method를 통해 등록한다.

Q. Repository에 `@Repository`를 붙여야 해?

A. Spring Data JPA Repository는 `JpaRepository`를 상속하면 보통 자동으로 Bean 등록된다.

---

# 3. Component Annotation

## 3.1 Component Annotation 종류

### [개념]

Component Annotation은 클래스를 Spring Bean으로 등록하기 위한 Annotation이다.

Spring은 Component Scan을 통해 해당 Annotation이 붙은 클래스를 찾아 Bean으로 등록한다.

---

### [핵심]

대표 Annotation:

| Annotation        | 역할             | 사용 위치              |
| ----------------- | ---------------- | ---------------------- |
| `@Component`      | 일반 Component   | 공통 기능, 유틸성 Bean |
| `@Service`        | Service Layer    | 비즈니스 로직          |
| `@Repository`     | Repository Layer | 데이터 접근            |
| `@Controller`     | MVC Controller   | View 반환              |
| `@RestController` | REST Controller  | JSON API 응답          |
| `@Configuration`  | 설정 클래스      | Bean 등록, 설정 구성   |

공통점:

```text
모두 Spring Bean 등록 대상
```

차이점:

```text
각 Annotation은 Layer 책임과 의미를 드러낸다.
```

---

### [실무]

Service:

```java
@Service
@RequiredArgsConstructor
public class OrderService {

    private final OrderRepository orderRepository;
}
```

Component:

```java
@Component
public class OrderNumberGenerator {

    public String generate() {
        return UUID.randomUUID().toString();
    }
}
```

Configuration:

```java
@Configuration
public class WebClientConfig {

    @Bean
    public WebClient webClient() {
        return WebClient.builder().build();
    }
}
```

권장:

- Layer 의미에 맞는 Annotation 사용
- 비즈니스 Service에는 `@Service`
- 일반 보조 객체에는 `@Component`
- 설정 클래스에는 `@Configuration`
- REST API Controller에는 `@RestController`
- View Controller에는 `@Controller`

---

### [Comparison]

| 구분      | `@Component`       | `@Service`         | `@Repository`               |
| --------- | ------------------ | ------------------ | --------------------------- |
| 공통점    | Bean 등록          | Bean 등록          | Bean 등록                   |
| 의미      | 일반 Component     | 비즈니스 계층      | 데이터 접근 계층            |
| 주 사용처 | 유틸, 보조 객체    | Use Case 처리      | DAO, Repository             |
| 권장 기준 | 역할이 일반적일 때 | Service Layer일 때 | 직접 Repository 구현체일 때 |

---

### [FAQ]

Q. `@Component`와 `@Service`는 기능적으로 달라?

A. 둘 다 Bean 등록 대상이라는 점은 같지만 `@Service`는 비즈니스 계층이라는 의미를 더 명확히 표현한다.

Q. 아무 클래스에나 `@Component`를 붙여도 돼?

A. 권장하지 않는다. Spring이 관리해야 하는 객체인지 먼저 판단해야 한다.

Q. REST API Controller는 어떤 Annotation을 써?

A. JSON 응답 API라면 `@RestController`를 사용한다.

---

# 4. Constructor Injection

## 4.1 생성자 주입 기준

### [개념]

Constructor Injection은 필요한 의존성을 생성자를 통해 주입받는 방식이다.

Spring Boot에서는 생성자 주입을 가장 권장한다.

---

### [핵심]

생성자 주입 장점:

- 필수 의존성 명확화
- `final` field 사용 가능
- 객체 불변성 향상
- 테스트 코드 작성 쉬움
- 순환 참조를 조기에 발견하기 쉬움
- Field Injection보다 의존성이 명확함

기본 코드:

```java
@Service
public class PostService {

    private final PostRepository postRepository;

    public PostService(PostRepository postRepository) {
        this.postRepository = postRepository;
    }
}
```

Lombok 사용:

```java
@Service
@RequiredArgsConstructor
public class PostService {

    private final PostRepository postRepository;
}
```

---

### [실무]

Controller:

```java
@RestController
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;
}
```

Service:

```java
@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
}
```

테스트에서 의존성 주입:

```java
class UserServiceTest {

    private UserRepository userRepository;
    private PasswordEncoder passwordEncoder;
    private UserService userService;

    @BeforeEach
    void setUp() {
        userRepository = mock(UserRepository.class);
        passwordEncoder = mock(PasswordEncoder.class);
        userService = new UserService(userRepository, passwordEncoder);
    }
}
```

권장:

- 필수 의존성은 생성자 주입
- 주입 필드는 `final`
- Lombok 사용 시 `@RequiredArgsConstructor`
- 테스트에서 Mock 객체 주입 가능하도록 설계
- 의존성이 너무 많으면 Service 책임 과다 여부 검토

---

### [FAQ]

Q. 생성자 주입이 왜 좋아?

A. 필수 의존성을 명확히 표현하고 `final` field를 사용할 수 있어 테스트와 유지보수에 유리하다.

Q. `@Autowired`를 생성자에 붙여야 해?

A. 생성자가 하나뿐이면 Spring이 자동으로 주입하므로 보통 생략할 수 있다.

Q. `@RequiredArgsConstructor`는 뭐야?

A. Lombok이 `final` field를 인자로 받는 생성자를 자동 생성해주는 Annotation이다.

---

## 4.2 Field Injection 지양

### [개념]

Field Injection은 field에 직접 `@Autowired`를 붙여 의존성을 주입받는 방식이다.

간단해 보이지만 의존성이 숨겨지고 테스트가 어려워 실무 코드에서는 지양한다.

---

### [핵심]

Field Injection 예:

```java
@Service
public class PostService {

    @Autowired
    private PostRepository postRepository;
}
```

문제:

- 의존성이 생성자에 드러나지 않음
- `final` 사용 불가
- 테스트에서 직접 주입이 어려움
- 객체가 불완전한 상태로 생성될 수 있음
- 순환 참조 파악이 늦어질 수 있음
- 숨은 의존성이 늘어날 수 있음

---

### [실무]

비권장:

```java
@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;
}
```

권장:

```java
@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
}
```

Review Agent 검수 기준:

```text
@Autowired field 발견
→ Field Injection 가능성 확인
→ 생성자 주입으로 변경 권장
```

---

### [FAQ]

Q. Field Injection은 아예 쓰면 안 돼?

A. 동작은 가능하지만 실무 구조에서는 생성자 주입이 더 명확하고 테스트하기 좋아 권장된다.

Q. 예전 코드에 `@Autowired` field가 많으면?

A. 새 코드부터 생성자 주입으로 작성하고, 리팩토링 시 `final` field와 생성자 주입으로 변경한다.

Q. Field Injection이 테스트에 왜 불리해?

A. 생성자로 의존성을 전달할 수 없어 Reflection이나 Spring Context 의존이 필요해질 수 있다.

---

## 4.3 Setter Injection 사용 기준

### [개념]

Setter Injection은 setter method를 통해 의존성을 주입받는 방식이다.

필수 의존성보다 선택 의존성이나 테스트용 교체가 필요한 경우 제한적으로 사용할 수 있다.

---

### [핵심]

Setter Injection 특징:

- 선택 의존성 표현 가능
- 의존성 변경 가능
- `final` field 사용 어려움
- 객체 생성 후 의존성이 바뀔 수 있음
- 필수 의존성에는 부적합

---

### [실무]

비권장:

```java
@Service
public class OrderService {

    private OrderRepository orderRepository;

    @Autowired
    public void setOrderRepository(OrderRepository orderRepository) {
        this.orderRepository = orderRepository;
    }
}
```

권장:

```java
@Service
@RequiredArgsConstructor
public class OrderService {

    private final OrderRepository orderRepository;
}
```

사용 가능 상황:

```text
선택적 의존성
테스트 전용 설정
Legacy 연동
Bean 초기화 이후 교체가 필요한 특수 상황
```

Foundation 기준:

```text
기본은 생성자 주입
Setter Injection은 특수한 경우에만 사용
```

---

### [FAQ]

Q. Setter Injection은 언제 써?

A. 선택 의존성이나 특수한 교체 가능성이 필요한 경우 제한적으로 사용할 수 있다.

Q. 일반 Service 의존성은 Setter로 받아도 돼?

A. 가능은 하지만 필수 의존성은 생성자 주입을 사용하는 것이 좋다.

---

# 5. Bean Lifecycle

## 5.1 Bean Lifecycle 개념

### [개념]

Bean Lifecycle은 Spring Container가 Bean을 생성하고 초기화하고 사용한 뒤 종료하는 전체 과정이다.

Spring Bean은 단순 객체가 아니라 Container가 생명주기를 관리하는 객체다.

---

### [Flow]

기본 흐름:

```text
Bean Definition 등록
→ Bean 객체 생성
→ 의존성 주입
→ 초기화 callback
→ Bean 사용 가능
→ Application 종료
→ 소멸 callback
```

자세한 흐름:

```text
Component Scan / @Bean
→ Bean Definition 등록
→ Constructor 호출
→ Dependency Injection
→ @PostConstruct
→ InitializingBean / initMethod
→ Application Ready
→ Bean 사용
→ @PreDestroy
→ DisposableBean / destroyMethod
→ 종료
```

---

### [핵심]

Lifecycle 관련 키워드:

- Bean Definition
- Constructor
- Dependency Injection
- `@PostConstruct`
- `@PreDestroy`
- InitializingBean
- DisposableBean
- initMethod
- destroyMethod
- ApplicationRunner
- CommandLineRunner

핵심 규칙:

- 생성자에서는 단순 의존성 주입 중심으로 둔다.
- 초기화 작업은 `@PostConstruct` 또는 Runner를 검토한다.
- 종료 정리 작업은 `@PreDestroy`를 검토한다.
- 무거운 초기화 작업은 Application startup 지연을 고려한다.
- Bean Lifecycle에 Business Use Case를 과도하게 넣지 않는다.

---

### [실무]

초기화 예:

```java
@Component
public class CacheWarmUpComponent {

    @PostConstruct
    public void init() {
        // 초기 캐시 구성
    }
}
```

소멸 예:

```java
@Component
public class ExternalClientHolder {

    @PreDestroy
    public void close() {
        // 외부 연결 정리
    }
}
```

ApplicationRunner 예:

```java
@Component
@RequiredArgsConstructor
public class StartupRunner implements ApplicationRunner {

    @Override
    public void run(ApplicationArguments args) {
        // Application 시작 후 실행할 작업
    }
}
```

권장:

- 가벼운 초기화는 `@PostConstruct`
- Application 시작 후 실행 작업은 `ApplicationRunner`
- 외부 리소스 정리는 `@PreDestroy`
- DB 초기 데이터는 Profile과 환경을 구분
- 운영에서 위험한 초기화 작업 주의

---

### [FAQ]

Q. Bean Lifecycle은 왜 알아야 해?

A. 초기화, 의존성 주입, 종료 정리 시점을 이해해야 Bean 생성 오류와 초기화 문제를 해결할 수 있다.

Q. `@PostConstruct`는 언제 실행돼?

A. Bean 생성과 의존성 주입이 끝난 뒤 초기화 시점에 실행된다.

Q. `@PreDestroy`는 언제 실행돼?

A. Application 종료 시 Bean이 소멸되기 전에 실행된다.

---

## 5.2 `@PostConstruct` 사용 기준

### [개념]

`@PostConstruct`는 Bean 생성과 의존성 주입이 완료된 뒤 실행되는 초기화 method를 지정하는 Annotation이다.

---

### [핵심]

사용 상황:

- 초기 캐시 구성
- 설정 값 검증
- 외부 Client 초기 상태 확인
- 간단한 리소스 준비
- Application 시작 시 필요한 lightweight 작업

주의 상황:

- 오래 걸리는 외부 API 호출
- 대량 DB 처리
- 운영 데이터 변경
- 실패 시 Application 시작 실패 가능 작업
- Transaction이 필요한 복잡한 작업

---

### [실무]

예:

```java
@Component
@RequiredArgsConstructor
public class ApiClientValidator {

    private final TourApiProperties properties;

    @PostConstruct
    public void validate() {
        if (properties.baseUrl() == null || properties.baseUrl().isBlank()) {
            throw new IllegalStateException("Tour API baseUrl is required");
        }
    }
}
```

주의:

```java
@PostConstruct
public void init() {
    externalApiClient.callVerySlowApi();
    orderRepository.updateAllStatus();
}
```

문제:

- Application startup 지연
- 외부 API 실패 시 Application 실행 실패
- 운영 데이터 변경 위험
- Transaction 경계 불명확

---

### [FAQ]

Q. `@PostConstruct`에서 DB 작업을 해도 돼?

A. 가능은 하지만 운영 데이터 변경이나 대량 작업은 위험할 수 있다. Profile과 Transaction, 실패 정책을 명확히 해야 한다.

Q. 초기 데이터 넣기는 `@PostConstruct`가 좋아?

A. 단순 학습용은 가능하지만 실무에서는 migration 도구, SQL init, profile 기반 runner 등을 검토하는 것이 좋다.

---

## 5.3 ApplicationRunner / CommandLineRunner

### [개념]

ApplicationRunner와 CommandLineRunner는 Spring Boot Application 시작 후 특정 코드를 실행할 수 있는 Runner interface다.

Bean 생성과 초기화가 끝난 뒤 실행되므로 startup 작업을 작성할 때 사용할 수 있다.

---

### [핵심]

비교:

| 구분      | ApplicationRunner    | CommandLineRunner   |
| --------- | -------------------- | ------------------- |
| 인자 타입 | ApplicationArguments | String[]            |
| 사용성    | 옵션 인자 처리 편함  | 단순 인자 처리      |
| 실행 시점 | Application 시작 후  | Application 시작 후 |

사용 상황:

- 개발용 초기 데이터 생성
- Profile별 테스트 데이터 준비
- 시작 로그 출력
- 외부 설정 확인
- 간단한 startup task

---

### [실무]

Profile 제한 예:

```java
@Component
@Profile("local")
@RequiredArgsConstructor
public class LocalDataInitializer implements ApplicationRunner {

    private final UserRepository userRepository;

    @Override
    @Transactional
    public void run(ApplicationArguments args) {
        if (!userRepository.existsByEmail("test@example.com")) {
            userRepository.save(User.create("test@example.com", "password", "tester"));
        }
    }
}
```

권장:

- 초기 데이터는 local / test profile로 제한
- prod에서 실행되지 않도록 `@Profile` 사용
- 중복 생성 방지 로직 작성
- Transaction 필요 시 명확히 적용
- 운영 데이터 변경 작업은 신중하게 분리

---

### [주의]

Runner Anti Pattern:

```java
@Component
public class DataInitializer implements CommandLineRunner {

    @Override
    public void run(String... args) {
        userRepository.deleteAll();
        userRepository.save(...);
    }
}
```

문제:

- 모든 Profile에서 실행 가능
- 운영 데이터 삭제 위험
- 중복 실행 위험
- 실패 시 Application 시작 실패 가능

---

### [FAQ]

Q. ApplicationRunner는 언제 써?

A. Application 시작 후 실행해야 하는 초기화 작업이 있을 때 사용한다.

Q. 초기 데이터 생성 Runner는 운영에서도 실행해도 돼?

A. 권장하지 않는다. local 또는 test Profile로 제한하는 것이 안전하다.

---

# 6. Bean Scope

## 6.1 Bean Scope 개념

### [개념]

Bean Scope는 Spring Bean이 생성되고 공유되는 범위를 의미한다.

Spring Boot Web Application에서는 기본적으로 Singleton Scope가 가장 많이 사용된다.

---

### [핵심]

대표 Scope:

| Scope       | 의미                  | 사용 상황                     |
| ----------- | --------------------- | ----------------------------- |
| singleton   | Container당 하나      | 대부분의 Service / Repository |
| prototype   | 요청할 때마다 새 객체 | 상태를 가진 특수 객체         |
| request     | HTTP 요청당 하나      | Web 요청별 상태               |
| session     | HTTP Session당 하나   | Session 상태                  |
| application | ServletContext당 하나 | Web Application 범위          |

기본값:

```text
singleton
```

---

### [실무]

일반 Service:

```java
@Service
public class UserService {
}
```

의미:

```text
기본 singleton Bean
Application 전체에서 하나의 UserService Bean 공유
```

중요 기준:

- Singleton Bean은 공유 상태를 가지면 위험하다.
- Service field에 요청별 데이터를 저장하지 않는다.
- 사용자별 상태는 method parameter, DB, Session, SecurityContext 등을 사용한다.
- 대부분의 Backend Service는 무상태 Stateless로 유지한다.

---

### [주의]

Singleton Bean Anti Pattern:

```java
@Service
public class SearchService {

    private String lastKeyword;

    public List<PostResponse> search(String keyword) {
        this.lastKeyword = keyword;
        return ...;
    }
}
```

문제:

- 여러 요청이 하나의 Bean field를 공유
- 동시 요청 시 값이 덮어써질 수 있음
- Thread Safety 문제
- 사용자 데이터 섞임 가능

개선:

```java
@Service
public class SearchService {

    public List<PostResponse> search(String keyword) {
        return ...;
    }
}
```

---

### [FAQ]

Q. Spring Bean은 기본적으로 몇 개 만들어져?

A. 기본 Scope는 singleton이므로 Container당 하나 만들어진다.

Q. Service에 사용자별 상태를 field로 저장해도 돼?

A. 안 된다. Singleton Bean은 여러 요청이 공유하므로 요청별 상태를 field에 저장하면 위험하다.

Q. 대부분의 Service는 어떤 구조가 좋아?

A. Stateless 구조가 좋다. 요청 값은 method parameter로 받고 상태는 DB나 별도 저장소에 둔다.

---

# 7. Circular Dependency

## 7.1 Circular Dependency 개념

### [개념]

Circular Dependency는 두 개 이상의 Bean이 서로를 의존해 생성 순환이 발생하는 구조다.

예:

```text
UserService
→ NotificationService
→ UserService
```

Circular Dependency는 단순 Bean 오류가 아니라 Service 책임과 의존 방향이 잘못되었다는 신호일 수 있다.

---

### [핵심]

원인:

- Service 간 양방향 의존
- 공통 로직 분리 실패
- 책임 경계 불명확
- 하나의 Use Case 흐름을 여러 Service가 서로 호출
- Helper / Component 분리 부족
- Event 처리 대상 로직을 직접 호출로 연결

문제:

- Bean 생성 실패
- 책임 경계 혼란
- 테스트 어려움
- 변경 영향 증가
- 구조 복잡도 증가

---

### [실무]

나쁜 구조:

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
1. 의존 방향 재검토
2. 공통 조회 로직 Component 분리
3. Repository 직접 조합 검토
4. Domain Service / Policy Component 분리
5. Event 기반 후속 처리 검토
```

공통 Component 예:

```java
@Component
@RequiredArgsConstructor
public class UserReader {

    private final UserRepository userRepository;

    public User getUser(Long userId) {
        return userRepository.findById(userId)
                .orElseThrow(() -> new BusinessException(ErrorCode.USER_NOT_FOUND));
    }
}
```

---

### [주의]

임시 우회:

```java
@Lazy
private final UserService userService;
```

주의:

- `@Lazy`는 근본 해결이 아니다.
- `spring.main.allow-circular-references=true`는 구조 문제를 숨긴다.
- 순환 참조는 의존 방향과 책임을 재설계해야 한다.
- Service 간 호출이 많아지면 Use Case 흐름을 다시 정리한다.

---

### [FAQ]

Q. Circular Dependency가 생기면 어떻게 해?

A. `@Lazy`로 우회하기보다 의존 방향과 책임을 재검토하고 공통 Component나 Event 구조로 분리하는 것이 좋다.

Q. 순환 참조 허용 설정을 켜도 돼?

A. 권장하지 않는다. Bean 생성 오류는 사라질 수 있지만 설계 문제는 남는다.

Q. Service끼리 호출하면 안 돼?

A. 단방향 호출은 가능하지만 양방향 의존이나 복잡한 상호 호출은 구조 개선 신호다.

---

# 8. Bean Conflict

## 8.1 Bean 이름 / 타입 충돌

### [개념]

Bean Conflict는 같은 이름 또는 같은 타입의 Bean이 여러 개 존재해 Spring이 어떤 Bean을 주입해야 할지 결정하지 못하는 문제다.

---

### [핵심]

대표 예외:

- `NoUniqueBeanDefinitionException`
- `BeanDefinitionOverrideException`
- `UnsatisfiedDependencyException`

원인:

- 같은 타입 Bean이 여러 개 존재
- 같은 이름 Bean 중복 등록
- Interface 구현체가 여러 개
- `@Bean` method 이름 중복
- Component Scan과 `@Bean` 수동 등록 중복

---

### [실무]

문제 예:

```java
public interface NotificationSender {
    void send(String message);
}
```

```java
@Component
public class EmailNotificationSender implements NotificationSender {
}
```

```java
@Component
public class SmsNotificationSender implements NotificationSender {
}
```

주입:

```java
@Service
@RequiredArgsConstructor
public class NotificationService {

    private final NotificationSender notificationSender;
}
```

문제:

```text
NotificationSender 타입 Bean이 2개
→ 어떤 구현체를 주입할지 모름
```

해결 1: `@Qualifier`

```java
@Service
public class NotificationService {

    private final NotificationSender notificationSender;

    public NotificationService(
            @Qualifier("emailNotificationSender") NotificationSender notificationSender
    ) {
        this.notificationSender = notificationSender;
    }
}
```

해결 2: `@Primary`

```java
@Primary
@Component
public class EmailNotificationSender implements NotificationSender {
}
```

---

### [주의]

`@Primary`와 `@Qualifier` 기준:

| 방식           | 사용 상황                      |
| -------------- | ------------------------------ |
| `@Primary`     | 기본 구현체 하나를 지정할 때   |
| `@Qualifier`   | 주입 지점에서 명확히 선택할 때 |
| 구체 타입 주입 | 구현체가 고정되어도 되는 경우  |

주의:

- `@Primary` 남용 금지
- Bean 이름에 의존하는 경우 이름 변경 영향 주의
- 구현체가 여러 개면 전략 패턴이나 Map 주입 검토
- 같은 Bean을 Component와 `@Bean`으로 중복 등록하지 않음

---

### [FAQ]

Q. 같은 Interface 구현체가 여러 개면 어떻게 해?

A. `@Primary`, `@Qualifier`, 구체 타입 주입, Map 주입 등을 사용해 명확히 선택해야 한다.

Q. NoUniqueBeanDefinitionException은 왜 발생해?

A. 같은 타입 Bean이 여러 개 있는데 Spring이 어떤 Bean을 주입해야 할지 결정하지 못할 때 발생한다.

---

## 8.2 Bean 이름 기준

### [개념]

Spring Bean은 이름을 가진다.

Component Scan으로 등록되는 Bean 이름은 기본적으로 클래스 이름의 첫 글자를 소문자로 바꾼 형태다.

---

### [핵심]

예:

```java
@Service
public class UserService {
}
```

기본 Bean 이름:

```text
userService
```

`@Bean` method:

```java
@Bean
public PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder();
}
```

Bean 이름:

```text
passwordEncoder
```

---

### [실무]

이름 지정:

```java
@Component("emailSender")
public class EmailNotificationSender implements NotificationSender {
}
```

사용:

```java
public NotificationService(
        @Qualifier("emailSender") NotificationSender notificationSender
) {
    this.notificationSender = notificationSender;
}
```

권장:

- 기본 Bean 이름에 과도하게 의존하지 않음
- `@Qualifier` 사용 시 이름 변경 영향 주의
- Bean 이름은 명확하고 일관되게 작성
- 같은 의미의 Bean 이름 중복 금지

---

### [FAQ]

Q. Bean 이름은 어떻게 정해져?

A. Component Class는 기본적으로 클래스 이름의 첫 글자를 소문자로 바꾼 이름이 사용된다. `@Bean`은 method 이름이 Bean 이름이 된다.

Q. Bean 이름을 직접 지정할 수 있어?

A. 가능하다. `@Component("name")` 또는 `@Bean("name")`처럼 지정할 수 있다.

---

# 9. DI Troubleshooting

## 9.1 Bean Not Found

### [개념]

Bean Not Found는 Spring Container가 주입해야 하는 Bean을 찾지 못하는 문제다.

---

### [핵심]

대표 원인:

- `@Service`, `@Component`, `@Configuration` 누락
- Main Application Class 하위 패키지 밖에 위치
- `@Bean` 등록 누락
- `@ConfigurationProperties` 등록 누락
- Spring Data JPA 의존성 누락
- Repository가 `JpaRepository`를 상속하지 않음
- Profile 조건 불일치
- Interface 구현체 없음

---

### [Troubleshooting]

Debug Flow:

```text
필요한 Bean Type 확인
→ 해당 Class Annotation 확인
→ Component Scan 범위 확인
→ Main Class 위치 확인
→ Profile 조건 확인
→ @Bean 등록 여부 확인
→ Interface 구현체 확인
→ build.gradle 의존성 확인
```

예:

```text
No qualifying bean of type 'TourApiClient'
```

확인:

```text
TourApiClient에 @Component가 있는가?
TourApiClient가 Main Class 하위 패키지에 있는가?
생성자에 필요한 Properties Bean이 등록되어 있는가?
Profile 조건 때문에 제외된 것은 아닌가?
```

---

### [FAQ]

Q. NoSuchBeanDefinitionException이 나면 어디부터 봐?

A. Bean으로 등록될 클래스의 Annotation, 패키지 위치, Profile, `@Bean` 등록 여부를 확인한다.

Q. Main Class 위치도 Bean 문제와 관련 있어?

A. 맞다. 기본 Component Scan은 Main Class 패키지 하위 기준으로 동작한다.

---

## 9.2 Bean Creation Error

### [개념]

Bean Creation Error는 Bean을 생성하는 과정에서 생성자, 설정 값, 의존성, 초기화 로직 등이 실패하는 문제다.

---

### [핵심]

원인:

- 생성자에서 예외 발생
- `@PostConstruct`에서 예외 발생
- 설정 값 누락
- 의존 Bean 생성 실패
- 순환 참조
- `@Bean` method 내부 예외
- 외부 리소스 초기화 실패
- 잘못된 Profile 설정

---

### [Troubleshooting]

Debug Flow:

```text
Startup log 확인
→ BeanCreationException 확인
→ Caused by 확인
→ 실패한 Bean 이름 확인
→ 생성자 / @PostConstruct / @Bean method 확인
→ 설정 값 확인
→ 의존 Bean 확인
```

문제 예:

```java
@PostConstruct
public void init() {
    throw new IllegalStateException("init failed");
}
```

결과:

```text
Application startup failure
```

개선:

```text
초기화 실패 정책 검토
필수 설정은 ConfigurationProperties Validation으로 검증
외부 API 호출은 startup 시점에서 분리 검토
```

---

### [FAQ]

Q. BeanCreationException은 무슨 뜻이야?

A. Spring이 Bean을 생성하는 중 생성자, 의존성, 설정, 초기화 작업에서 실패했다는 의미다.

Q. `@PostConstruct` 실패도 실행 실패 원인이야?

A. 맞다. 초기화 method에서 예외가 발생하면 Application 시작이 실패할 수 있다.

---

## 9.3 NoUniqueBeanDefinitionException

### [개념]

NoUniqueBeanDefinitionException은 같은 타입의 Bean이 여러 개 있어 Spring이 어떤 Bean을 주입해야 할지 결정하지 못할 때 발생한다.

---

### [핵심]

확인 대상:

- 같은 Interface 구현체 개수
- `@Bean` 중복 등록
- Component와 Configuration 중복 등록
- `@Primary` 존재 여부
- `@Qualifier` 사용 여부
- 주입 타입이 너무 추상적인지 여부

---

### [Troubleshooting]

Debug Flow:

```text
에러 메시지의 Bean 후보 목록 확인
→ 주입 대상 타입 확인
→ 구현체 개수 확인
→ 기본 구현체가 필요한지 확인
→ @Primary 또는 @Qualifier 적용
→ 주입 타입 구체화 검토
```

---

### [FAQ]

Q. 같은 타입 Bean이 여러 개면 무조건 문제야?

A. 아니다. 다만 주입 지점에서 어떤 Bean을 사용할지 명확히 지정해야 한다.

Q. `@Primary`와 `@Qualifier` 중 뭐가 좋아?

A. 기본 구현체가 명확하면 `@Primary`, 주입 지점마다 선택해야 하면 `@Qualifier`가 좋다.

---

# 10. Dependency Injection Anti Pattern

## 10.1 Common DI Anti Pattern

### [개념]

Dependency Injection Anti Pattern은 Bean 등록, 주입 방식, 의존 방향을 잘못 설계해 테스트와 유지보수를 어렵게 만드는 구조다.

---

### [핵심]

대표 Anti Pattern:

- Service / Repository를 직접 `new`로 생성
- Field Injection 남용
- Setter Injection으로 필수 의존성 주입
- `final` field 미사용
- 순환 참조 방치
- `@Lazy`로 순환 참조 우회
- 모든 클래스를 무조건 `@Component`로 등록
- Bean 생성 로직에 Business Logic 작성
- Configuration class에서 Service를 직접 조립
- 같은 Bean을 중복 등록
- Interface 구현체가 여러 개인데 선택 기준 없음
- Singleton Bean에 요청별 상태 저장

---

### [실무]

나쁜 예:

```java
@Service
public class PostService {

    private final PostRepository postRepository = new PostRepository();
}
```

문제:

- Repository 직접 생성 불가
- Spring Data JPA Proxy 우회
- 테스트 어려움
- Container 관리 대상 아님

나쁜 예:

```java
@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;
}
```

개선:

```java
@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
}
```

나쁜 예:

```java
@Service
public class RequestStateService {

    private Long currentUserId;
}
```

문제:

- Singleton Bean에 요청별 상태 저장
- 동시 요청 시 데이터 섞임
- Thread Safety 문제

---

### [FAQ]

Q. DI Anti Pattern 중 가장 흔한 것은?

A. Field Injection 남용, Service 간 순환 참조, Singleton Bean에 요청별 상태 저장이 흔하다.

Q. 모든 클래스를 Bean으로 만들면 편하지 않아?

A. 불필요한 Bean이 늘어나고 책임이 흐려질 수 있다. Spring이 관리해야 하는 객체만 Bean으로 등록하는 것이 좋다.

---

# 11. Bean Lifecycle Anti Pattern

## 11.1 Common Lifecycle Anti Pattern

### [개념]

Bean Lifecycle Anti Pattern은 Bean 초기화와 종료 시점에 부적절한 작업을 넣어 Application 실행 안정성을 해치는 구조다.

---

### [핵심]

대표 Anti Pattern:

- 생성자에서 무거운 로직 실행
- `@PostConstruct`에서 외부 API 장시간 호출
- `@PostConstruct`에서 운영 데이터 변경
- Runner를 모든 Profile에서 실행
- 초기 데이터 생성 시 중복 방지 없음
- `@PreDestroy`에서 오래 걸리는 작업 수행
- 초기화 실패 정책 없음
- Bean 초기화 로직에 Business Use Case 포함
- Profile 제한 없이 테스트 데이터 생성

---

### [실무]

나쁜 예:

```java
@Component
@RequiredArgsConstructor
public class InitDataRunner implements ApplicationRunner {

    private final UserRepository userRepository;

    @Override
    public void run(ApplicationArguments args) {
        userRepository.deleteAll();
        userRepository.save(User.create("admin@example.com", "password", "admin"));
    }
}
```

문제:

- 운영에서 실행될 위험
- 데이터 삭제 위험
- 중복 실행 위험
- 테스트 / 운영 환경 분리 없음

개선:

```java
@Component
@Profile("local")
@RequiredArgsConstructor
public class LocalInitDataRunner implements ApplicationRunner {

    private final UserRepository userRepository;

    @Override
    @Transactional
    public void run(ApplicationArguments args) {
        if (!userRepository.existsByEmail("admin@example.com")) {
            userRepository.save(User.create("admin@example.com", "password", "admin"));
        }
    }
}
```

---

### [FAQ]

Q. 초기 데이터 Runner는 위험해?

A. Profile 제한과 중복 방지 없이 작성하면 운영 데이터에 영향을 줄 수 있어 위험하다.

Q. 생성자에서 초기화 로직을 많이 넣어도 돼?

A. 권장하지 않는다. 생성자는 의존성 주입 중심으로 두고 초기화 작업은 적절한 Lifecycle callback을 사용한다.

---

# 12. Final Review Checklist

## 12.1 DI / Bean Final Checklist

### [개념]

DI / Bean Final Checklist는 Backend Agent가 Spring Boot Bean 구조를 생성하거나 검수할 때 사용하는 기준이다.

---

### [핵심]

Final Checklist:

```md
- [ ] Main Application Class가 최상위 패키지에 있는가?
- [ ] Bean 대상 클래스가 Component Scan 범위 안에 있는가?
- [ ] 직접 만든 Service는 @Service로 등록되어 있는가?
- [ ] 일반 Component는 @Component로 등록되어 있는가?
- [ ] 외부 라이브러리 객체는 @Bean으로 등록되어 있는가?
- [ ] Repository는 JpaRepository를 상속하는가?
- [ ] 생성자 주입을 사용하는가?
- [ ] 의존성 field가 final로 선언되어 있는가?
- [ ] Field Injection을 사용하지 않는가?
- [ ] 필수 의존성을 Setter Injection으로 받지 않는가?
- [ ] Service / Repository를 직접 new로 생성하지 않는가?
- [ ] 순환 참조가 없는가?
- [ ] @Lazy로 순환 참조를 숨기지 않는가?
- [ ] 같은 타입 Bean이 여러 개일 때 @Primary 또는 @Qualifier 기준이 있는가?
- [ ] Singleton Bean에 요청별 상태를 저장하지 않는가?
- [ ] @PostConstruct에 무거운 외부 호출이 없는가?
- [ ] Runner가 필요한 Profile에서만 실행되는가?
- [ ] 초기 데이터 생성에 중복 방지 조건이 있는가?
- [ ] @PreDestroy에서 필요한 리소스 정리를 수행하는가?
- [ ] Bean 생성 로직과 Business Logic이 섞이지 않는가?
```

---

### [실무]

검수 흐름:

```text
Bean 등록 여부
→ Component Scan 범위
→ Injection 방식
→ 의존 방향
→ 순환 참조
→ Bean 충돌
→ Bean Scope
→ Lifecycle callback
→ Anti Pattern 제거
```

---

### [FAQ]

Q. DI / Bean 검수에서 가장 중요한 것은?

A. 생성자 주입, Bean 등록 위치, 순환 참조 제거, Singleton 상태 관리, Field Injection 제거가 중요하다.

Q. Backend Agent가 DI 코드를 만들 때 반드시 지켜야 할 것은?

A. Service와 Controller는 생성자 주입을 사용하고, 의존성은 `final` field로 명확히 하며, Spring Bean을 직접 `new`로 생성하지 않아야 한다.

---

# 13. Retrieval Queries

### [FAQ]

Q. Spring Boot Dependency Injection이 뭐야?
A.
Dependency Injection은 객체가 필요한 의존 객체를 직접 생성하지 않고 Spring IoC Container로부터 주입받는 방식이다.
Spring Boot에서는 Service, Repository, Component 간 결합도를 낮추고 테스트하기 쉬운 구조를 만들기 위해 사용한다.

Q. Spring Boot DI는 왜 필요해?
A.
DI는 객체 생성 책임을 Spring Container에 맡기고, 클래스는 자신의 역할에 집중하게 만든다.
이를 통해 코드 결합도가 낮아지고 테스트, 확장, 유지보수가 쉬워진다.

Q. Spring Boot 생성자 주입은 왜 권장해?
A.
생성자 주입은 필수 의존성을 객체 생성 시점에 보장하고 `final` field 사용이 가능하다.
또한 테스트 코드 작성이 쉽고 순환 참조 문제를 더 빠르게 발견할 수 있다.

Q. Spring Boot Field Injection은 왜 지양해?
A.
Field Injection은 의존성이 숨겨져 테스트가 어렵고 `final` field를 사용할 수 없다.
또한 객체 생성 시점에 필수 의존성이 명확히 드러나지 않아 유지보수성이 떨어진다.

Q. Spring Boot @RequiredArgsConstructor는 언제 써?
A.
`final` field나 `@NonNull` field를 대상으로 생성자를 자동 생성할 때 사용한다.
Service, Controller, Component에서 생성자 주입을 간결하게 작성할 때 자주 사용한다.

Q. Spring Boot @Autowired는 언제 생략 가능해?
A.
생성자가 하나뿐인 Spring Bean에서는 생성자에 `@Autowired`를 생략할 수 있다.
Spring이 해당 생성자를 통해 자동으로 의존성을 주입한다.

Q. Spring Boot Bean은 뭐야?
A.
Bean은 Spring IoC Container가 생성하고 관리하는 객체다.
`@Component`, `@Service`, `@Repository`, `@Controller`, `@Configuration`, `@Bean` 등을 통해 등록된다.

Q. Spring Bean과 일반 객체 차이는 뭐야?
A.
Spring Bean은 Container가 생성, 주입, 생명주기를 관리하는 객체다.
일반 객체는 개발자가 직접 `new`로 생성하고 생명주기도 직접 관리한다.

Q. Spring IoC Container는 뭐야?
A.
IoC Container는 Bean을 생성하고 의존성을 주입하며 생명주기를 관리하는 Spring의 핵심 구조다.
대표 구현체로 `ApplicationContext`가 있다.

Q. Spring ApplicationContext는 뭐야?
A.
ApplicationContext는 Spring Bean을 관리하는 IoC Container다.
Bean 조회, 의존성 주입, 이벤트 처리, 환경 설정, 메시지 처리 등을 지원한다.

Q. Spring Boot Component Scan은 어떻게 동작해?
A.
`@SpringBootApplication`이 위치한 package를 기준으로 하위 package의 Component를 탐색한다.
따라서 Main Application Class는 프로젝트 최상위 package에 두는 것이 좋다.

Q. Spring Boot Bean 등록은 어떻게 해?
A.
직접 만든 클래스는 `@Component`, `@Service`, `@Repository`, `@Controller` 등으로 등록한다.
외부 라이브러리 객체나 설정 기반 객체는 `@Configuration` 클래스에서 `@Bean`으로 등록한다.

Q. Spring Boot @Component @Service @Repository 차이는?
A.
`@Component`는 일반 Bean 등록 Annotation이다.
`@Service`는 비즈니스 로직 계층, `@Repository`는 데이터 접근 계층을 나타내며 역할 의미를 명확히 한다.

Q. Spring Boot @Configuration @Bean은 언제 써?
A.
외부 라이브러리 객체나 직접 Annotation을 붙일 수 없는 객체를 Spring Bean으로 등록할 때 사용한다.
예를 들어 `ObjectMapper`, `RestClient`, `PasswordEncoder`, 외부 SDK Client 등록에 사용한다.

Q. Spring Boot 외부 라이브러리 Bean 등록은 어떻게 해?
A.
`@Configuration` 클래스 안에 `@Bean` method를 작성해 외부 객체를 생성하고 반환한다.
이렇게 등록된 객체는 Spring Container가 관리하며 다른 Bean에 주입할 수 있다.

Q. Spring Boot Bean Lifecycle 흐름은?
A.
Bean Lifecycle은 객체 생성, 의존성 주입, 초기화 callback, 사용, 종료 callback 순서로 진행된다.
초기화에는 `@PostConstruct`, 종료에는 `@PreDestroy`를 사용할 수 있다.

Q. Spring Boot @PostConstruct는 언제 써?
A.
Bean 생성과 의존성 주입이 끝난 뒤 초기화 작업이 필요할 때 사용한다.
단, 무거운 작업이나 외부 API 호출은 ApplicationRunner 등으로 분리하는 것이 좋다.

Q. Spring Boot @PreDestroy는 언제 써?
A.
Bean이 종료되기 전에 자원 정리 작업이 필요할 때 사용한다.
예를 들어 connection 종료, buffer 정리, background 작업 정리 등에 사용할 수 있다.

Q. Spring Boot ApplicationRunner는 언제 써?
A.
Application 실행이 완료된 뒤 초기 로직을 실행해야 할 때 사용한다.
초기 데이터 등록, 설정 점검, startup log 출력 같은 작업에 활용할 수 있다.

Q. Spring Boot CommandLineRunner는 언제 써?
A.
Application 실행 후 command line argument 기반 초기 작업을 수행할 때 사용한다.
단순 실행 후 초기화 작업은 ApplicationRunner와 CommandLineRunner 모두 사용할 수 있다.

Q. Spring Boot 초기 데이터는 어떻게 넣어?
A.
개발용 초기 데이터는 ApplicationRunner나 CommandLineRunner에서 등록할 수 있다.
운영에서는 migration tool, SQL script, 관리자 기능 등 더 안전한 방식을 검토하는 것이 좋다.

Q. Spring Boot Runner를 Profile로 제한하는 방법은?
A.
Runner Bean에 `@Profile("local")` 또는 `@Profile("test")`를 적용해 특정 환경에서만 실행되도록 제한할 수 있다.
운영 환경에서 테스트 데이터가 생성되지 않도록 Profile 제한이 중요하다.

Q. Spring Boot Bean Scope는 뭐야?
A.
Bean Scope는 Bean이 생성되고 공유되는 범위를 의미한다.
기본값은 singleton이며, request, session, prototype 같은 scope도 있다.

Q. Spring Boot singleton Bean 주의사항은?
A.
singleton Bean은 Application 전체에서 하나의 인스턴스를 공유한다.
따라서 사용자별 상태나 요청별 변경 값을 field에 저장하면 동시성 문제가 생길 수 있다.

Q. Spring Boot Service에 상태 field를 두면 안 되는 이유는?
A.
Service Bean은 기본적으로 singleton이므로 여러 요청이 같은 인스턴스를 공유한다.
요청별 상태를 field에 저장하면 사용자 데이터가 섞이거나 thread-safety 문제가 발생할 수 있다.

Q. Spring Boot Circular Dependency는 어떻게 해결해?
A.
Service 간 의존 방향을 재검토하고 공통 로직을 별도 Component로 분리한다.
필요하면 이벤트 기반 처리나 책임 재분리를 통해 순환 참조를 제거한다.

Q. Spring Boot 순환 참조가 생기는 이유는?
A.
두 Service가 서로를 직접 호출하거나 공통 책임이 명확히 분리되지 않았을 때 자주 발생한다.
순환 참조는 구조와 책임 분리가 잘못되었다는 신호로 보는 것이 좋다.

Q. Spring Boot @Lazy로 순환 참조 해결해도 돼?
A.
`@Lazy`는 Bean 생성을 지연시켜 순환 참조를 임시로 우회할 수 있다.
하지만 근본 해결은 아니므로 의존 방향과 책임을 재설계하는 것이 좋다.

Q. Spring Boot NoSuchBeanDefinitionException 원인은?
A.
필요한 Bean이 Spring Container에 등록되지 않았을 때 발생한다.
Annotation 누락, Component Scan 범위 밖 위치, Profile 불일치, `@Bean` 등록 누락 등을 확인해야 한다.

Q. Spring Boot BeanCreationException 원인은?
A.
Bean 생성 중 생성자, 설정 값, 의존성, 초기화 로직 등에서 문제가 발생할 때 생긴다.
`Caused by`를 따라가며 실제 원인을 확인하는 것이 중요하다.

Q. Spring Boot NoUniqueBeanDefinitionException 해결 방법은?
A.
같은 타입의 Bean이 여러 개라 주입 대상을 결정하지 못할 때 발생한다.
`@Primary`, `@Qualifier`, Bean 이름 지정, 의존성 타입 구체화로 해결할 수 있다.

Q. Spring Boot @Primary와 @Qualifier 차이는?
A.
`@Primary`는 같은 타입 Bean 중 기본 주입 대상을 지정한다.
`@Qualifier`는 주입 지점에서 특정 Bean 이름이나 qualifier를 명시해 선택한다.

Q. Spring Boot Bean 이름은 어떻게 정해져?
A.
Component 기반 Bean은 기본적으로 class 이름의 첫 글자를 소문자로 바꾼 이름이 사용된다.
`@Component("customName")`이나 `@Bean` method 이름으로 직접 지정할 수도 있다.

Q. Spring Boot DI Anti Pattern은 뭐야?
A.
Field Injection, 직접 `new`로 의존 객체 생성, 순환 참조, Service Locator 남용, `ApplicationContext` 직접 조회 등이 대표적이다.
DI 구조에서는 필요한 의존성을 생성자 주입으로 명확히 드러내는 것이 좋다.

Q. Spring Boot Bean Lifecycle Anti Pattern은 뭐야?
A.
생성자나 `@PostConstruct`에서 무거운 외부 API 호출, DB 대량 작업, 사용자 요청 의존 작업을 수행하는 구조가 대표적이다.
초기화 작업은 가볍고 실패 영향 범위를 명확히 해야 한다.

Q. Spring Boot 생성자에서 무거운 초기화 로직을 피해야 하는 이유는?
A.
생성자는 Bean 생성 단계이므로 무거운 작업이 있으면 Application Startup이 느려지거나 실패할 수 있다.
외부 API 호출, 대량 DB 작업, 파일 처리 등은 Runner나 별도 초기화 흐름으로 분리하는 것이 좋다.

Q. Spring Boot Field Injection을 생성자 주입으로 바꾸는 방법은?
A.
`@Autowired` field를 `private final` field로 바꾸고 생성자를 통해 주입받도록 변경한다.
Lombok을 사용한다면 `@RequiredArgsConstructor`로 생성자 코드를 줄일 수 있다.

Q. Spring Boot Bean 검수 체크리스트는 뭐야?
A.
Bean 등록 Annotation, Component Scan 범위, 생성자 주입, final field, 순환 참조, Bean Scope, 초기화 로직, Profile 조건, `@Primary` / `@Qualifier` 사용 여부를 확인한다.
또한 Service Bean에 요청별 상태 field가 없는지도 함께 검수해야 한다.
