# Spring Boot Part09 - Configuration, Properties, Profile, CORS, External API, Logging

---

# 1. Configuration

## 1.1 Configuration 개념

### [개념]

Configuration은 Spring Boot Application의 동작 방식을 코드와 설정 파일로 분리해 관리하는 구조다.

Spring Boot에서는 `application.yml`, `application.properties`, 환경변수, `@Configuration`, `@Bean`, `@ConfigurationProperties` 등을 사용해 설정을 관리한다.

Configuration의 목적:

- 실행 환경별 설정 분리
- 민감정보 하드코딩 방지
- 외부 API Key 관리
- DB 연결 정보 관리
- CORS 설정 관리
- Logging Level 관리
- Bean 등록 관리
- 테스트 환경 격리
- 운영 환경 안정성 확보

기본 구조:

```text
application.yml
→ Profile 별 설정
→ ConfigurationProperties
→ Configuration Class
→ Bean 등록
→ Service에서 사용
```

---

### [핵심]

Spring Boot Configuration 요소:

- `application.yml`
- `application.properties`
- `application-local.yml`
- `application-dev.yml`
- `application-prod.yml`
- Environment Variable
- `@Configuration`
- `@Bean`
- `@Value`
- `@ConfigurationProperties`
- Profile
- CORS Config
- Logging Config

설정으로 관리할 대상:

- server port
- datasource
- jpa
- logging level
- external api base url
- external api key
- file upload size
- cors allowed origin
- jwt secret
- mail property
- profile active

---

### [실무]

기본 `application.yml` 예:

```yaml
server:
  port: 8080

spring:
  profiles:
    active: local

  datasource:
    url: ${DB_URL}
    username: ${DB_USERNAME}
    password: ${DB_PASSWORD}

logging:
  level:
    root: info
    com.example.project: debug
```

권장:

- 민감정보는 환경변수로 주입
- 실행 환경별 Profile 분리
- 설정 Key naming 통일
- 사용하지 않는 설정 제거
- 설정 값은 Service에 하드코딩하지 않음
- 관련 설정은 `@ConfigurationProperties`로 묶음
- 외부 라이브러리 객체는 `@Bean`으로 등록

---

### [FAQ]

Q. Spring Boot Configuration은 왜 필요해?

A.
DB, 외부 API, CORS, Logging, Profile 같은 실행 환경별 설정을 코드와 분리해 안전하고 유연하게 관리하기 위해 필요하다.

Q. 설정 값을 Java 코드에 직접 써도 돼?

A.
권장하지 않는다. 변경이 어렵고 민감정보가 노출될 수 있으므로 `application.yml`, 환경변수, `ConfigurationProperties`로 분리하는 것이 좋다.

Q. @Configuration은 언제 써?

A.
외부 라이브러리 객체를 Bean으로 등록하거나 Application 설정용 Bean을 구성할 때 사용한다.

---

# 2. application.yml / application.properties

## 2.1 Application Properties 개념

### [개념]

`application.yml` 또는 `application.properties`는 Spring Boot Application의 설정 값을 저장하는 기본 설정 파일이다.

두 형식 모두 사용할 수 있지만 프로젝트에서는 하나의 형식을 일관되게 사용하는 것이 좋다.

---

### [핵심]

관리 대상:

- server 설정
- datasource 설정
- jpa 설정
- logging 설정
- profile 설정
- cors 설정
- external api 설정
- mail 설정
- file upload 설정
- security 관련 설정

`application.properties` 예:

```properties
server.port=8080
spring.datasource.url=${DB_URL}
spring.datasource.username=${DB_USERNAME}
spring.datasource.password=${DB_PASSWORD}
logging.level.root=info
```

`application.yml` 예:

```yaml
server:
  port: 8080

spring:
  datasource:
    url: ${DB_URL}
    username: ${DB_USERNAME}
    password: ${DB_PASSWORD}

logging:
  level:
    root: info
```

---

### [Comparison]

| 구분      | application.properties | application.yml              |
| --------- | ---------------------- | ---------------------------- |
| 형식      | key=value              | 계층형 YAML                  |
| 장점      | 단순함                 | 중첩 구조 가독성 좋음        |
| 단점      | 중첩 설정이 길어짐     | 들여쓰기 오류 주의           |
| 사용 상황 | 간단한 설정            | 설정이 많고 계층이 깊은 경우 |
| 주의      | key 중복 주의          | indentation 주의             |

---

### [실무]

권장 `application.yml` 구조:

```yaml
server:
  port: 8080

spring:
  datasource:
    url: ${DB_URL}
    username: ${DB_USERNAME}
    password: ${DB_PASSWORD}

  jpa:
    hibernate:
      ddl-auto: validate
    properties:
      hibernate:
        format_sql: true

external:
  tour-api:
    base-url: ${TOUR_API_BASE_URL}
    service-key: ${TOUR_API_SERVICE_KEY}

cors:
  allowed-origins:
    - http://localhost:3000
    - http://localhost:5173

logging:
  level:
    root: info
    com.example.project: debug
```

권장:

- 단순 프로젝트는 properties도 가능
- 중첩 설정이 많으면 yml 권장
- 한 프로젝트에서 둘을 혼용하지 않음
- 같은 설정 Key 중복 선언 주의
- 운영 민감정보는 파일에 직접 작성하지 않음

---

### [FAQ]

Q. application.yml과 application.properties 중 뭐가 좋아?

A.
둘 다 가능하다. 설정이 단순하면 properties도 충분하고, 중첩 구조가 많으면 yml이 읽기 쉽다.

Q. yml에서 가장 조심할 점은?

A.
들여쓰기 오류다. YAML은 indentation에 민감하므로 공백을 일관되게 유지해야 한다.

Q. properties와 yml을 같이 써도 돼?

A.
가능은 하지만 혼란이 생길 수 있으므로 하나의 형식으로 통일하는 것이 좋다.

---

## 2.2 Environment Variable

### [개념]

Environment Variable은 운영체제나 실행 환경에서 제공하는 설정 값이다.

Spring Boot에서는 `${ENV_NAME}` 형식으로 환경변수를 설정 파일에 주입할 수 있다.

---

### [핵심]

환경변수로 관리할 대상:

- DB_URL
- DB_USERNAME
- DB_PASSWORD
- JWT_SECRET
- API_KEY
- MAIL_PASSWORD
- OAUTH_CLIENT_SECRET
- CLOUD_ACCESS_KEY
- CLOUD_SECRET_KEY

사용 예:

```yaml
spring:
  datasource:
    url: ${DB_URL}
    username: ${DB_USERNAME}
    password: ${DB_PASSWORD}

jwt:
  secret: ${JWT_SECRET}

tour-api:
  service-key: ${TOUR_API_SERVICE_KEY}
```

---

### [실무]

기본값 지정 예:

```yaml
server:
  port: ${SERVER_PORT:8080}

spring:
  profiles:
    active: ${SPRING_PROFILES_ACTIVE:local}
```

의미:

```text
SERVER_PORT 환경변수가 있으면 해당 값 사용
없으면 8080 사용
```

권장:

- 민감정보는 환경변수 사용
- 기본값은 민감하지 않은 값에만 사용
- 운영 DB password 기본값 지정 지양
- `.env` 파일 사용 시 Git 제외
- 배포 환경별 환경변수 관리 방식 통일

---

### [주의]

환경변수 주의:

- API Key를 Git에 커밋하지 않음
- `.env` 파일을 `.gitignore`에 추가
- 환경변수 이름을 프로젝트 전체에서 통일
- 로컬 실행과 배포 실행 환경변수 차이 확인
- IDE 실행 설정에도 환경변수 필요할 수 있음
- unknown property 경고와 환경변수 미설정 오류를 구분

---

### [FAQ]

Q. API Key를 application.yml에 직접 써도 돼?

A.
권장하지 않는다. API Key, DB Password, JWT Secret 같은 민감정보는 환경변수나 Secret 관리 방식을 사용하는 것이 좋다.

Q. ${DB_URL} 값이 없으면 어떻게 돼?

A.
기본값이 없으면 실행 시 설정 바인딩 오류나 연결 실패가 발생할 수 있다.

Q. 환경변수 기본값은 언제 써?

A.
로컬 개발용 포트나 profile처럼 민감하지 않고 기본값이 있어도 안전한 설정에 사용할 수 있다.

---

# 3. ConfigurationProperties

## 3.1 ConfigurationProperties 개념

### [개념]

`@ConfigurationProperties`는 여러 설정 값을 타입 안전한 객체로 묶어 바인딩하는 방식이다.

`@Value`로 문자열을 하나씩 주입하는 대신 관련 설정을 하나의 Properties 객체로 관리할 수 있다.

---

### [핵심]

사용 대상:

- 외부 API 설정
- CORS 설정
- JWT 설정
- File Upload 설정
- Mail 설정
- OAuth 설정
- 여러 관련 값 묶음
- 테스트에서 주입하기 쉬운 설정

장점:

- 타입 안정성
- 설정 그룹화
- 오타 감소
- 테스트 편의성
- 생성자 주입 가능
- 설정 변경 추적 쉬움

---

### [실무]

`application.yml`:

```yaml
tour-api:
  base-url: ${TOUR_API_BASE_URL}
  service-key: ${TOUR_API_SERVICE_KEY}
  timeout-seconds: 5
```

Properties class:

```java
@ConfigurationProperties(prefix = "tour-api")
public record TourApiProperties(
        String baseUrl,
        String serviceKey,
        int timeoutSeconds
) {
}
```

등록:

```java
@Configuration
@EnableConfigurationProperties(TourApiProperties.class)
public class PropertiesConfig {
}
```

사용:

```java
@Component
@RequiredArgsConstructor
public class TourApiClient {

    private final TourApiProperties properties;

    public TourApiResponse getFestivalInfo(String keyword) {
        String baseUrl = properties.baseUrl();
        String serviceKey = properties.serviceKey();
        ...
    }
}
```

---

### [Comparison]

| 구분          | @Value          | @ConfigurationProperties |
| ------------- | --------------- | ------------------------ |
| 목적          | 단일 값 주입    | 관련 설정 묶음           |
| 타입 안정성   | 낮음            | 높음                     |
| 설정 개수     | 적을 때 적합    | 많을 때 적합             |
| 테스트 편의성 | 상대적으로 낮음 | 좋음                     |
| 구조화        | 어려움          | 좋음                     |

---

### [FAQ]

Q. @Value와 @ConfigurationProperties 중 뭐가 좋아?

A.
단일 값은 `@Value`도 가능하지만 관련 설정이 여러 개면 `@ConfigurationProperties`가 구조화와 타입 안정성 측면에서 좋다.

Q. ConfigurationProperties는 꼭 등록해야 해?

A.
Spring Boot 설정에 따라 자동 스캔을 사용할 수 있지만, 기초 구조에서는 `@EnableConfigurationProperties`로 명시 등록하면 이해하기 쉽다.

Q. 외부 API 설정은 어디에 두는 게 좋아?

A.
`application.yml`에 환경변수 기반으로 작성하고 `@ConfigurationProperties`로 바인딩해 사용하는 것이 좋다.

---

## 3.2 ConfigurationProperties Validation

### [개념]

ConfigurationProperties Validation은 설정 값이 누락되거나 잘못된 상태로 Application이 실행되는 것을 방지하는 방식이다.

설정 값이 필수라면 시작 시점에 검증되도록 구성할 수 있다.

---

### [핵심]

검증 대상:

- baseUrl 누락
- apiKey 누락
- timeout 값 범위 오류
- allowedOrigins 비어 있음
- file size 음수
- mail host 누락
- jwt secret 누락

주요 Annotation:

- `@Validated`
- `@NotBlank`
- `@NotNull`
- `@Positive`
- `@Min`
- `@Max`
- `@NotEmpty`

---

### [실무]

예:

```java
@Validated
@ConfigurationProperties(prefix = "tour-api")
public record TourApiProperties(
        @NotBlank String baseUrl,
        @NotBlank String serviceKey,
        @Positive int timeoutSeconds
) {
}
```

설정 누락 시:

```text
Application startup failure
→ 설정 누락 또는 잘못된 값 확인
→ 환경변수 확인
→ application.yml 확인
```

권장:

- 운영 필수 설정은 시작 시점 검증
- API Key, baseUrl, secret은 빈 값 방지
- timeout, max size는 범위 검증
- 실패를 조기에 발견하도록 구성
- 기본값은 안전한 값만 제공

---

### [주의]

주의:

- 민감정보 기본값을 코드에 넣지 않음
- validation message에 secret 값 노출 금지
- local profile과 prod profile의 필수 설정 차이 확인
- 테스트 실행 시 필요한 설정 mock 또는 test profile 구성
- 설정 오류와 Bean 등록 오류를 구분

---

### [FAQ]

Q. 설정 값도 Validation을 해야 해?

A.
필수 설정이 누락되면 운영 장애로 이어질 수 있으므로 중요한 설정은 시작 시점에 검증하는 것이 좋다.

Q. JWT Secret 기본값을 넣어도 돼?

A.
운영 환경에서는 권장하지 않는다. Secret은 환경변수나 Secret 관리 시스템에서 주입하는 것이 좋다.

---

# 4. Profile

## 4.1 Profile 개념

### [개념]

Profile은 local, dev, test, prod 같은 실행 환경별 설정을 분리하는 Spring Boot 기능이다.

환경마다 DB, Logging, 외부 API, 보안 설정이 다를 때 Profile을 사용한다.

---

### [핵심]

대표 Profile:

- local
- dev
- test
- prod

환경별 차이:

| Profile | 목적             |
| ------- | ---------------- |
| local   | 개발자 로컬 실행 |
| dev     | 개발 서버        |
| test    | 자동 테스트      |
| prod    | 운영 서버        |

Profile로 분리할 대상:

- DB 연결 정보
- JPA ddl-auto
- logging level
- external API mode
- CORS origin
- mail setting
- mock setting
- security option

---

### [실무]

파일 구조:

```text
application.yml
application-local.yml
application-dev.yml
application-test.yml
application-prod.yml
```

공통 설정:

```yaml
spring:
  profiles:
    active: ${SPRING_PROFILES_ACTIVE:local}

server:
  port: 8080
```

local 설정:

```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/app_local
    username: local_user
    password: ${LOCAL_DB_PASSWORD}

logging:
  level:
    com.example.project: debug
```

prod 설정:

```yaml
spring:
  datasource:
    url: ${PROD_DB_URL}
    username: ${PROD_DB_USERNAME}
    password: ${PROD_DB_PASSWORD}

logging:
  level:
    root: info
    com.example.project: info
```

---

### [Best Practice]

Profile Best Practice:

- local / dev / test / prod 분리
- 운영 profile에는 debug logging 지양
- test profile은 테스트 격리용 DB 사용
- prod profile에 ddl-auto create 금지
- 민감정보는 profile 파일에 직접 작성하지 않음
- 배포 환경에서는 `SPRING_PROFILES_ACTIVE` 명시
- Profile별 CORS allowed origin 분리

---

### [FAQ]

Q. Profile은 언제 써?

A.
로컬, 테스트, 운영 환경에서 DB, 로그, 외부 API, CORS 설정이 달라질 때 사용한다.

Q. 운영 profile에는 뭘 조심해야 해?

A.
debug logging, ddl-auto create, local DB, localhost CORS, 테스트 API Key가 섞이지 않도록 주의해야 한다.

Q. active profile은 어떻게 정해?

A.
`spring.profiles.active` 또는 `SPRING_PROFILES_ACTIVE` 환경변수로 지정할 수 있다.

---

## 4.2 Test Profile

### [개념]

Test Profile은 자동 테스트 실행 시 운영 DB나 외부 API에 영향을 주지 않도록 격리된 설정을 제공하는 Profile이다.

---

### [핵심]

Test Profile 목적:

- 테스트 DB 분리
- 외부 API 호출 방지
- 빠른 테스트 실행
- 테스트용 Bean 등록
- logging level 조정
- 데이터 초기화 관리

테스트 설정 대상:

- H2 또는 TestContainer DB
- mock external api
- test jwt secret
- test mail sender
- ddl-auto create-drop
- SQL logging 조정

---

### [실무]

`application-test.yml` 예:

```yaml
spring:
  datasource:
    url: jdbc:h2:mem:testdb
    username: sa
    password:

  jpa:
    hibernate:
      ddl-auto: create-drop

logging:
  level:
    root: warn
    com.example.project: debug

external:
  tour-api:
    base-url: http://localhost:9999
    service-key: test-key
```

테스트 class:

```java
@ActiveProfiles("test")
@SpringBootTest
class UserServiceTest {
}
```

권장:

- 테스트는 반드시 test profile 사용
- 운영 DB 연결 방지
- 외부 API 실제 호출 방지
- 테스트용 secret 사용
- 테스트 데이터 초기화 기준 통일

---

### [주의]

Test Profile 주의:

- test profile 없이 통합 테스트 실행 금지
- 운영 DB URL이 test에서 사용되지 않도록 확인
- 외부 결제 / 메일 / 문자 API 실제 호출 금지
- 테스트용 설정도 민감정보는 Git에 주의
- H2와 MySQL 문법 차이 주의

---

### [FAQ]

Q. 테스트할 때 Profile이 왜 필요해?

A.
운영 DB나 실제 외부 API에 영향을 주지 않고 격리된 환경에서 테스트하기 위해 필요하다.

Q. 테스트에서 외부 API를 실제 호출해도 돼?

A.
권장하지 않는다. Mock, Stub, Test Double, local fake server 등을 사용하는 것이 좋다.

---

# 5. Bean Configuration

## 5.1 @Configuration과 @Bean

### [개념]

`@Configuration`은 설정 클래스임을 나타내고, `@Bean`은 Spring Container가 관리할 객체를 직접 등록하는 Annotation이다.

외부 라이브러리 객체처럼 직접 `@Component`를 붙일 수 없는 객체를 Bean으로 등록할 때 사용한다.

---

### [핵심]

사용 대상:

- ObjectMapper
- RestTemplate
- WebClient
- PasswordEncoder
- CorsConfigurationSource
- 외부 SDK Client
- Mapper
- Clock
- Custom Converter

Annotation:

- `@Configuration`
- `@Bean`

---

### [실무]

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

외부 API Client 설정 예:

```java
@Configuration
@RequiredArgsConstructor
public class ExternalApiConfig {

    private final TourApiProperties properties;

    @Bean
    public RestClient tourApiRestClient() {
        return RestClient.builder()
                .baseUrl(properties.baseUrl())
                .build();
    }
}
```

권장:

- 외부 라이브러리 객체는 `@Bean` 등록
- 직접 만든 Service는 `@Service` 사용
- 설정 클래스는 `config` 패키지에 위치
- Bean 이름 충돌 주의
- Bean 생성 로직에 Business Logic 넣지 않음

---

### [주의]

Bean Configuration Anti Pattern:

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

- Repository 직접 생성 불가 또는 부적절
- Spring Data JPA Repository는 Spring이 생성해야 함
- DI 흐름 깨짐
- 테스트와 유지보수 어려움

권장:

```java
@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
}
```

---

### [FAQ]

Q. @Bean은 언제 써?

A.
외부 라이브러리 객체처럼 클래스에 직접 `@Component`를 붙일 수 없을 때 사용한다.

Q. 직접 만든 Service도 @Bean으로 등록해도 돼?

A.
가능은 하지만 일반적으로 직접 만든 Service는 `@Service`와 생성자 주입을 사용하는 것이 더 명확하다.

Q. @Configuration class에는 비즈니스 로직을 넣어도 돼?

A.
권장하지 않는다. 설정 클래스는 Bean 생성과 설정에 집중해야 한다.

---

# 6. CORS

## 6.1 CORS 개념

### [개념]

CORS는 Cross-Origin Resource Sharing의 약자다.

브라우저에서 다른 Origin의 Frontend가 Backend API에 접근할 수 있는지 결정하는 보안 정책이다.

Origin은 protocol, host, port 조합이다.

예:

```text
http://localhost:3000
http://localhost:8080
https://example.com
```

`http://localhost:3000`에서 `http://localhost:8080` API를 호출하면 서로 다른 Origin이므로 CORS 설정이 필요할 수 있다.

---

### [핵심]

CORS 관련 개념:

- Origin
- Same-Origin Policy
- Cross-Origin Request
- Allowed Origin
- Allowed Method
- Allowed Header
- Credentials
- Preflight
- OPTIONS Request

CORS 설정 대상:

- Frontend 개발 서버
- 운영 Frontend Domain
- 허용 HTTP Method
- Authorization Header
- Cookie / Credentials
- Preflight cache

---

### [실무]

기초 CORS 설정 예:

```java
@Configuration
public class CorsConfig {

    @Bean
    public WebMvcConfigurer corsConfigurer() {
        return new WebMvcConfigurer() {

            @Override
            public void addCorsMappings(CorsRegistry registry) {
                registry.addMapping("/api/**")
                        .allowedOrigins("http://localhost:3000")
                        .allowedMethods("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS")
                        .allowedHeaders("*")
                        .allowCredentials(true);
            }
        };
    }
}
```

권장:

- local과 prod allowed origin 분리
- 운영에서 `*` 남용 금지
- Authorization Header 허용 확인
- Cookie 사용 시 credentials 설정 확인
- Security 사용 시 SecurityFilterChain CORS 설정 확인
- CORS는 인증 / 인가 대체 수단이 아님

---

### [주의]

CORS 주의:

- `allowedOrigins("*")`와 `allowCredentials(true)` 조합 주의
- Frontend URL의 protocol, domain, port 정확히 일치해야 함
- Backend 서버가 정상 응답해도 브라우저가 차단할 수 있음
- Postman에서는 CORS 문제가 재현되지 않을 수 있음
- CORS 에러와 401 / 403 인증 문제를 구분해야 함
- Spring Security 사용 시 WebMvcConfigurer만으로 부족할 수 있음

---

### [FAQ]

Q. CORS 에러는 Backend 에러야?

A.
서버가 정상 응답해도 브라우저 보안 정책 때문에 차단될 수 있다. Origin, Method, Header, Credentials 설정을 확인해야 한다.

Q. Postman에서는 되는데 브라우저에서는 안 되는 이유는?

A.
CORS는 브라우저 보안 정책이므로 Postman에서는 차단되지 않을 수 있다.

Q. CORS를 허용하면 보안 처리가 끝난 거야?

A.
아니다. CORS는 브라우저 접근 정책이고 실제 인증 / 인가는 별도로 처리해야 한다.

---

## 6.2 Spring Security와 CORS

### [개념]

Spring Security를 사용하는 Application에서는 CORS 요청이 Security Filter Chain을 거치므로 Security 설정에서 CORS를 함께 활성화해야 할 수 있다.

---

### [핵심]

확인 대상:

- `SecurityFilterChain`
- `http.cors`
- `CorsConfigurationSource`
- allowed origins
- allowed methods
- allowed headers
- credentials
- preflight OPTIONS
- Authorization header

---

### [실무]

Security CORS 예:

```java
@Configuration
public class CorsConfig {

    @Bean
    public CorsConfigurationSource corsConfigurationSource() {
        CorsConfiguration configuration = new CorsConfiguration();

        configuration.setAllowedOrigins(List.of("http://localhost:3000"));
        configuration.setAllowedMethods(List.of("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"));
        configuration.setAllowedHeaders(List.of("*"));
        configuration.setAllowCredentials(true);

        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/api/**", configuration);

        return source;
    }
}
```

Security 설정 예:

```java
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    return http
            .cors(Customizer.withDefaults())
            .csrf(AbstractHttpConfigurer::disable)
            .authorizeHttpRequests(auth -> auth
                    .requestMatchers("/api/public/**").permitAll()
                    .anyRequest().authenticated()
            )
            .build();
}
```

권장:

- Security 사용 시 `http.cors()` 설정 확인
- OPTIONS preflight 요청 차단 여부 확인
- Authorization Header 허용 확인
- allowed origin을 Profile별로 분리
- Security 심화 내용은 Security Advanced 문서 기준으로 다룸

---

### [Troubleshooting]

문제: CORS 설정했는데 여전히 브라우저에서 차단됨

```text
원인 후보:
- Spring Security에서 CORS 미활성화
- allowed origin 불일치
- credentials 설정 불일치
- Authorization Header 미허용
- OPTIONS 요청이 인증 필터에서 차단됨
- Frontend 요청 URL이 다른 origin 사용
```

확인 순서:

```text
Browser Network 확인
→ Request Origin 확인
→ Preflight OPTIONS 확인
→ SecurityFilterChain CORS 확인
→ Allowed Origin 확인
→ Allowed Header 확인
→ Credentials 설정 확인
```

---

### [FAQ]

Q. Spring Security를 쓰면 CORS 설정 위치가 달라져?

A.
Security Filter Chain에서 CORS 요청을 처리하므로 `CorsConfigurationSource`와 `http.cors()` 설정을 함께 확인해야 한다.

Q. OPTIONS 요청이 401이 나면 뭐가 문제야?

A.
Preflight 요청이 인증 필터에서 차단될 수 있다. Security CORS 설정과 OPTIONS 허용 여부를 확인해야 한다.

---

# 7. External API Integration

## 7.1 External API Integration 개념

### [개념]

External API Integration은 Spring Boot Application이 외부 서버의 API를 호출해 데이터를 조회하거나 전송하는 구조다.

예:

- Tour API
- Kakao Map API
- Toss Payments API
- Mail API
- OAuth Provider API
- Weather API
- AI API

---

### [핵심]

관리 대상:

- baseUrl
- apiKey
- secret
- timeout
- request parameter
- response DTO
- error handling
- logging
- retry
- rate limit
- fallback
- external api client

기본 흐름:

```text
Service
→ ExternalApiClient
→ External API
→ External Response DTO
→ Mapping
→ Service Result
```

---

### [실무]

Properties:

```yaml
tour-api:
  base-url: ${TOUR_API_BASE_URL}
  service-key: ${TOUR_API_SERVICE_KEY}
  timeout-seconds: 5
```

Client:

```java
@Component
@RequiredArgsConstructor
public class TourApiClient {

    private final TourApiProperties properties;

    public TourApiResponse searchFestival(String keyword) {
        try {
            ...
        } catch (Exception exception) {
            throw new ExternalApiException(ErrorCode.EXTERNAL_API_ERROR, exception);
        }
    }
}
```

Service:

```java
@Service
@RequiredArgsConstructor
public class FestivalService {

    private final TourApiClient tourApiClient;

    public FestivalResponse searchFestival(String keyword) {
        TourApiResponse externalResponse = tourApiClient.searchFestival(keyword);

        return FestivalResponse.from(externalResponse);
    }
}
```

권장:

- 외부 API 호출 코드는 별도 Client Component로 분리
- Service는 외부 API 호출 흐름을 조율
- API Key는 환경변수로 관리
- 외부 Response DTO와 내부 Response DTO 분리
- timeout 설정 고려
- 실패 시 내부 ErrorCode로 변환
- 로그에 API Key 노출 금지

---

### [FAQ]

Q. 외부 API 호출 코드는 Service에 바로 넣어도 돼?

A.
작은 프로젝트에서는 가능하지만 ExternalApiClient 같은 별도 Component로 분리하면 테스트와 유지보수가 쉬워진다.

Q. API Key는 어디에 둬?

A.
환경변수와 ConfigurationProperties를 통해 주입하는 것이 좋다.

Q. 외부 API Response DTO와 내부 Response DTO는 분리해야 해?

A.
분리하는 것이 좋다. 외부 API 스펙 변경이 내부 API 응답 구조에 직접 영향을 주지 않게 하기 위해서다.

---

## 7.2 External API Error Handling

### [개념]

External API Error Handling은 외부 API 호출 실패를 Application 내부 예외와 Error Response로 변환하는 구조다.

외부 API의 오류 메시지나 응답을 그대로 Client에 노출하지 않는 것이 좋다.

---

### [핵심]

실패 상황:

- timeout
- connection refused
- 400 / 401 / 403
- 429 rate limit
- 500 external server error
- invalid response
- empty response
- JSON parsing error

내부 ErrorCode 예:

```text
EXTERNAL_API_ERROR
EXTERNAL_API_TIMEOUT
EXTERNAL_API_UNAUTHORIZED
EXTERNAL_API_RATE_LIMIT
EXTERNAL_API_INVALID_RESPONSE
```

---

### [실무]

Exception:

```java
public class ExternalApiException extends RuntimeException {

    private final ErrorCode errorCode;

    public ExternalApiException(ErrorCode errorCode, Throwable cause) {
        super(errorCode.getMessage(), cause);
        this.errorCode = errorCode;
    }

    public ErrorCode getErrorCode() {
        return errorCode;
    }
}
```

Handler:

```java
@ExceptionHandler(ExternalApiException.class)
public ResponseEntity<ApiResponse<Void>> handleExternalApiException(
        ExternalApiException exception
) {
    ErrorCode errorCode = exception.getErrorCode();

    return ResponseEntity
            .status(errorCode.getStatus())
            .body(ApiResponse.fail(errorCode.name(), errorCode.getMessage()));
}
```

권장:

- 외부 예외를 내부 CustomException으로 변환
- 사용자에게 통제된 메시지 반환
- 서버 로그에는 원인 기록
- timeout과 rate limit 구분 가능하면 구분
- 외부 API 실패가 전체 실패인지 부분 실패인지 정책 결정
- 재시도는 멱등성 확인 후 적용

---

### [주의]

주의:

- 외부 API 원문 오류를 그대로 Client에 반환하지 않음
- API Key, Authorization Header 로그 금지
- retry 남용 금지
- 결제 API는 중복 승인 방지 필요
- 외부 API 실패와 DB Transaction rollback 관계 검토
- 장애 시 fallback 데이터가 필요한지 결정

---

### [FAQ]

Q. 외부 API 오류를 그대로 내려도 돼?

A.
권장하지 않는다. 외부 시스템 내부 메시지나 민감정보가 노출될 수 있으므로 내부 ErrorCode와 메시지로 변환하는 것이 좋다.

Q. 외부 API timeout은 어떻게 처리해?

A.
timeout 설정을 적용하고 실패 시 `EXTERNAL_API_TIMEOUT` 같은 ErrorCode로 변환하는 것이 좋다.

Q. retry는 무조건 넣는 게 좋아?

A.
아니다. 결제, 주문, 알림처럼 중복 처리 위험이 있는 API는 멱등성 키와 정책 없이 retry하면 위험하다.

---

# 8. Logging

## 8.1 Logging 개념

### [개념]

Logging은 Application 동작, 오류, 요청 흐름, 외부 API 호출 결과 등을 기록해 문제 분석과 운영 관리를 돕는 작업이다.

Spring Boot에서는 SLF4J 기반 Logger를 사용하는 것이 일반적이다.

---

### [핵심]

Logging 대상:

- Application startup
- 중요 business event
- error
- warning
- external api call result
- security event
- batch result
- configuration summary
- performance issue
- debug information

Log Level:

| Level | 사용 상황                                   |
| ----- | ------------------------------------------- |
| ERROR | 장애, 처리 실패, 예상하지 못한 예외         |
| WARN  | 비정상 가능성, 비즈니스 오류, 외부 API 실패 |
| INFO  | 주요 이벤트, 상태 변경                      |
| DEBUG | 개발 / 디버깅 정보                          |
| TRACE | 매우 상세한 추적                            |

---

### [실무]

Logger 사용:

```java
private static final Logger log = LoggerFactory.getLogger(PostService.class);
```

예:

```java
@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    log.debug("getPost request. postId={}", postId);

    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException(ErrorCode.POST_NOT_FOUND));

    return PostResponse.from(post);
}
```

Lombok 사용 예:

```java
@Slf4j
@Service
@RequiredArgsConstructor
public class PostService {

    public PostResponse getPost(Long postId) {
        log.debug("getPost request. postId={}", postId);
        ...
    }
}
```

권장:

- `System.out.println` 지양
- Logger 사용
- log level 구분
- placeholder `{}` 사용
- 민감정보 로그 금지
- 운영 환경 debug log 주의
- 예외 stack trace는 서버 로그에 기록
- Client 응답과 로그 메시지 구분

---

### [FAQ]

Q. System.out.println으로 로그 찍어도 돼?

A.
개발 중 임시 확인은 가능하지만 실무 코드에서는 Logger를 사용하는 것이 좋다.

Q. log.info와 log.debug는 어떻게 구분해?

A.
운영 중에도 의미 있는 주요 이벤트는 info, 개발 중 상세 추적 정보는 debug가 적합하다.

Q. 로그에 토큰이나 비밀번호를 남겨도 돼?

A.
안 된다. Access Token, Refresh Token, Password, API Key 같은 민감정보는 로그에 남기면 안 된다.

---

## 8.2 Logging Level 설정

### [개념]

Logging Level 설정은 package별로 로그 출력 수준을 조정하는 설정이다.

local 환경에서는 debug를 켜고 prod 환경에서는 info 또는 warn 중심으로 관리할 수 있다.

---

### [핵심]

설정 위치:

- application.yml
- application-local.yml
- application-prod.yml

Level 순서:

```text
TRACE
→ DEBUG
→ INFO
→ WARN
→ ERROR
```

오른쪽으로 갈수록 더 심각한 로그다.

---

### [실무]

local profile:

```yaml
logging:
  level:
    root: info
    com.example.project: debug
    org.hibernate.SQL: debug
```

prod profile:

```yaml
logging:
  level:
    root: info
    com.example.project: info
    org.hibernate.SQL: warn
```

권장:

- local에서는 debug 허용
- prod에서는 debug 남용 금지
- SQL log 운영 노출 주의
- 민감정보 포함 가능 로그 주의
- 장애 분석에 필요한 error stack trace는 보존
- package 단위로 log level 조정

---

### [주의]

운영 Logging 주의:

- SQL parameter 로그에 개인정보가 포함될 수 있음
- debug log 과다 출력은 성능과 비용에 영향
- 로그 파일 용량 관리 필요
- 반복되는 BusinessException을 ERROR로 과도하게 남기지 않음
- API Key, Token, Password 마스킹 필요
- 로그 보관 정책과 개인정보 정책 확인

---

### [FAQ]

Q. 운영에서 debug log를 켜도 돼?

A.
일시적 장애 분석에는 가능하지만 상시 debug는 성능, 비용, 민감정보 노출 위험이 있어 지양한다.

Q. SQL 로그를 운영에서 켜도 돼?

A.
주의해야 한다. SQL과 parameter에 민감정보가 포함될 수 있고 로그량이 많아질 수 있다.

---

## 8.3 Exception Logging

### [개념]

Exception Logging은 예외 발생 시 서버 로그에 원인 추적 정보를 남기는 것이다.

Client에는 안전한 Error Response를 반환하고, 서버 로그에는 stack trace와 context를 남길 수 있다.

---

### [핵심]

Client Response:

- errorCode
- message
- fieldErrors
- stack trace 제외
- 민감정보 제외

Server Log:

- exception stack trace
- errorCode
- request path
- userId
- external api status
- 원인 추적 context

---

### [실무]

BusinessException:

```java
@ExceptionHandler(BusinessException.class)
public ResponseEntity<ApiResponse<Void>> handleBusinessException(
        BusinessException exception
) {
    ErrorCode errorCode = exception.getErrorCode();

    log.warn("BusinessException: errorCode={}, message={}",
            errorCode.name(),
            exception.getMessage());

    return ResponseEntity
            .status(errorCode.getStatus())
            .body(ApiResponse.fail(errorCode.name(), errorCode.getMessage()));
}
```

Unexpected Exception:

```java
@ExceptionHandler(Exception.class)
public ResponseEntity<ApiResponse<Void>> handleException(Exception exception) {
    log.error("Unexpected exception occurred", exception);

    return ResponseEntity
            .status(500)
            .body(ApiResponse.fail("INTERNAL_SERVER_ERROR", "서버 내부 오류가 발생했습니다."));
}
```

권장:

- 예상 가능한 BusinessException은 WARN 또는 INFO 검토
- 예상하지 못한 Exception은 ERROR
- stack trace는 서버 로그에만 기록
- Client에 exception.getMessage() 그대로 반환 금지
- 로그에 request body 전체를 무조건 남기지 않음

---

### [FAQ]

Q. 모든 예외를 ERROR로 남겨야 해?

A.
아니다. Validation 실패나 중복 요청 같은 예상 가능한 오류는 WARN 또는 INFO로 관리할 수 있다.

Q. exception.getMessage()를 Client에 그대로 반환해도 돼?

A.
권장하지 않는다. 내부 정보가 노출될 수 있으므로 통제된 메시지를 반환하는 것이 좋다.

---

# 9. Configuration Troubleshooting

## 9.1 설정 값 주입 실패

### [개념]

설정 값 주입 실패는 `application.yml`, 환경변수, `ConfigurationProperties`, `@Value` 설정이 올바르게 연결되지 않아 발생하는 문제다.

---

### [핵심]

원인 후보:

- 환경변수 미설정
- yml indentation 오류
- prefix 불일치
- property key 오타
- `@ConfigurationProperties` 등록 누락
- Profile 불일치
- IDE 실행 환경변수 누락
- 기본값 없음
- 타입 변환 실패

---

### [Troubleshooting]

Debug Flow:

```text
현재 active profile 확인
→ application.yml / profile yml 확인
→ 환경변수 존재 확인
→ property key 확인
→ prefix 확인
→ ConfigurationProperties 등록 확인
→ 타입 변환 가능 여부 확인
→ startup error message 확인
```

예:

```yaml
tour-api:
  service-key: ${TOUR_API_SERVICE_KEY}
```

Properties:

```java
@ConfigurationProperties(prefix = "tour-api")
public record TourApiProperties(
        String serviceKey
) {
}
```

주의:

```text
tour-api.service-key
→ serviceKey로 relaxed binding 가능
```

---

### [FAQ]

Q. ConfigurationProperties 값이 null이면 뭘 확인해?

A.
prefix, yml key, Profile, 환경변수, `@EnableConfigurationProperties` 또는 scan 등록 여부를 확인한다.

Q. application.yml에서 unknown property 경고가 뜨면 문제야?

A.
반드시 실행 오류는 아니다. 직접 만든 custom property는 IDE가 모를 수 있다. 다만 key 오타인지 확인해야 한다.

Q. 환경변수는 터미널에 있는데 IDE 실행에서는 안 돼?

A.
IDE 실행 설정에는 환경변수가 별도로 필요할 수 있다. Run Configuration의 Environment Variables를 확인한다.

---

## 9.2 Profile 설정 문제

### [개념]

Profile 설정 문제는 기대한 local, dev, test, prod 설정이 적용되지 않아 DB, CORS, Logging, 외부 API 설정이 다르게 동작하는 문제다.

---

### [핵심]

원인 후보:

- active profile 미설정
- Profile 파일 이름 오타
- `application-prod.yml` 위치 오류
- 환경변수 우선순위 오해
- 배포 환경에서 다른 Profile 사용
- 테스트에서 prod 설정 사용
- local 설정이 prod에 포함됨

---

### [Troubleshooting]

Debug Flow:

```text
Application startup log 확인
→ active profile 확인
→ SPRING_PROFILES_ACTIVE 확인
→ application-{profile}.yml 파일명 확인
→ 설정 override 순서 확인
→ 실제 연결된 DB URL 확인
→ CORS origin 확인
→ Logging level 확인
```

Startup log 예:

```text
The following 1 profile is active: "local"
```

---

### [주의]

Profile 문제 주의:

- 운영에서 local profile 실행 금지
- test에서 운영 DB 연결 금지
- prod에서 ddl-auto create 금지
- profile별 CORS origin 혼동 주의
- 환경변수와 yml 값의 우선순위 확인
- 배포 스크립트에 profile 명시

---

### [FAQ]

Q. 지금 어떤 Profile로 실행 중인지 어떻게 알아?

A.
Application startup log에서 active profile을 확인하거나 Environment 설정을 출력해 확인할 수 있다.

Q. prod에서 local DB로 붙으면 뭘 확인해?

A.
`SPRING_PROFILES_ACTIVE`, prod yml, 환경변수, 배포 스크립트, datasource 설정 override 여부를 확인한다.

---

# 10. Common Anti Pattern

## 10.1 Configuration Anti Pattern

### [개념]

Configuration Anti Pattern은 설정 값과 코드가 섞이거나 환경별 설정이 분리되지 않아 유지보수와 운영 안정성을 떨어뜨리는 구조다.

---

### [핵심]

자주 발생:

- API Key 하드코딩
- DB Password Git 커밋
- local 설정을 prod에서 사용
- prod profile에 debug logging
- ddl-auto create를 운영에서 사용
- 설정 key naming 불일치
- `@Value` 남용
- 같은 설정을 여러 곳에 중복 작성
- Configuration class에 Business Logic 작성
- Bean 수동 생성으로 DI 흐름 깨짐
- 환경변수 기본값에 민감정보 작성

---

### [실무]

나쁜 예:

```java
@Service
public class TourApiService {

    private static final String API_KEY = "real-api-key";
    private static final String BASE_URL = "https://api.example.com";
}
```

문제:

- API Key 코드 노출
- Git 유출 위험
- 환경별 변경 어려움
- 테스트 대체 어려움

좋은 예:

```yaml
tour-api:
  base-url: ${TOUR_API_BASE_URL}
  service-key: ${TOUR_API_SERVICE_KEY}
```

```java
@ConfigurationProperties(prefix = "tour-api")
public record TourApiProperties(
        String baseUrl,
        String serviceKey
) {
}
```

---

### [FAQ]

Q. 설정 Anti Pattern 중 가장 위험한 건 뭐야?

A.
API Key, DB Password, JWT Secret 같은 민감정보를 코드나 Git에 남기는 것이 가장 위험하다.

Q. @Value를 많이 쓰면 안 돼?

A.
단일 값은 가능하지만 관련 설정이 많아지면 `@ConfigurationProperties`로 묶는 것이 유지보수에 좋다.

---

## 10.2 CORS Anti Pattern

### [개념]

CORS Anti Pattern은 브라우저 Origin 정책과 인증 / 인가를 혼동하거나 운영 환경에서 과도하게 허용하는 설정이다.

---

### [핵심]

자주 발생:

- 운영에서 모든 origin 허용
- credentials 사용하면서 wildcard origin 사용
- Authorization Header 미허용
- OPTIONS 요청 차단
- local frontend origin만 등록하고 운영 origin 누락
- http / https 혼동
- port 번호 불일치
- CORS를 인증 / 인가로 오해
- Postman 성공을 보고 CORS 문제 없다고 판단

---

### [실무]

나쁜 예:

```java
registry.addMapping("/**")
        .allowedOrigins("*")
        .allowedMethods("*")
        .allowedHeaders("*")
        .allowCredentials(true);
```

문제:

- credentials와 wildcard origin 조합 위험
- 운영에서 과도한 허용
- 보안 정책 불명확

좋은 예:

```java
registry.addMapping("/api/**")
        .allowedOrigins("https://www.example.com")
        .allowedMethods("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS")
        .allowedHeaders("Authorization", "Content-Type")
        .allowCredentials(true);
```

---

### [FAQ]

Q. CORS에서 \*로 다 열면 편하지 않아?

A.
개발 중 임시로는 가능하지만 운영에서는 필요한 origin만 명확히 허용하는 것이 좋다.

Q. Postman에서 되면 CORS 설정은 문제없는 거야?

A.
아니다. CORS는 브라우저 정책이므로 Postman에서는 재현되지 않을 수 있다.

---

## 10.3 Logging Anti Pattern

### [개념]

Logging Anti Pattern은 로그를 남기지 않거나, 반대로 민감정보와 과도한 로그를 남겨 운영 위험을 만드는 구조다.

---

### [핵심]

자주 발생:

- `System.out.println` 사용
- 모든 로그를 info로 남김
- 모든 예외를 error로 남김
- stack trace를 Client에 반환
- Access Token 로그 기록
- Password 로그 기록
- API Key 로그 기록
- Request Body 전체 로그 기록
- 운영에서 debug log 상시 활성화
- SQL parameter 민감정보 노출
- 로그에 context가 없어 원인 추적 불가

---

### [실무]

나쁜 예:

```java
System.out.println("password = " + request.password());
System.out.println("token = " + accessToken);
```

좋은 예:

```java
log.info("User signup requested. emailDomain={}", emailDomain);
log.warn("Duplicated email signup attempt");
log.error("Unexpected exception occurred", exception);
```

권장:

- 민감정보는 마스킹
- 로그 level 기준 통일
- 장애 분석에 필요한 context 포함
- Request Body 전체 로그 지양
- 운영 debug log 제한
- 개인정보 보호 정책 준수

---

### [FAQ]

Q. Request Body를 전부 로그로 남기면 디버깅에 좋지 않아?

A.
디버깅에는 편하지만 개인정보와 민감정보가 노출될 수 있어 운영에서는 지양해야 한다.

Q. System.out.println은 왜 안 좋아?

A.
log level, 출력 형식, 운영 수집, 필터링, 성능 관리가 어렵기 때문이다.

---

# 11. Review Checklist

## 11.1 Configuration / Profile / CORS / External API / Logging Checklist

### [개념]

이 Checklist는 Backend Agent가 Spring Boot 설정, Profile, CORS, 외부 API, Logging 구조를 검수할 때 사용하는 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] application.yml 또는 application.properties 형식을 일관되게 사용하는가?
- [ ] 민감정보가 코드에 하드코딩되어 있지 않은가?
- [ ] API Key, DB Password, JWT Secret이 환경변수로 관리되는가?
- [ ] local / dev / test / prod Profile이 분리되어 있는가?
- [ ] 운영 Profile에 debug logging이 남아 있지 않은가?
- [ ] 운영 Profile에 ddl-auto create가 사용되지 않는가?
- [ ] test Profile이 운영 DB에 연결되지 않는가?
- [ ] 관련 설정을 ConfigurationProperties로 묶었는가?
- [ ] 필수 설정 값에 Validation을 적용했는가?
- [ ] @Configuration class가 config 패키지에 있는가?
- [ ] 외부 라이브러리 객체는 @Bean으로 등록했는가?
- [ ] 직접 만든 Service를 불필요하게 @Bean으로 수동 생성하지 않는가?
- [ ] CORS allowed origin이 환경별로 분리되어 있는가?
- [ ] 운영 CORS에서 wildcard를 남용하지 않는가?
- [ ] Authorization Header와 OPTIONS 요청을 고려했는가?
- [ ] Spring Security 사용 시 SecurityFilterChain CORS를 확인했는가?
- [ ] 외부 API 호출이 ExternalApiClient로 분리되어 있는가?
- [ ] 외부 API Key가 로그에 남지 않는가?
- [ ] 외부 API 실패를 내부 ErrorCode로 변환하는가?
- [ ] timeout과 실패 처리 기준이 있는가?
- [ ] System.out.println 대신 Logger를 사용하는가?
- [ ] log level 기준이 환경별로 적절한가?
- [ ] 민감정보를 로그에 남기지 않는가?
- [ ] 예외 stack trace는 서버 로그에만 남기는가?
```

---

### [실무]

검수 흐름:

```text
application.yml 확인
→ 환경변수 확인
→ Profile 확인
→ ConfigurationProperties 확인
→ Bean Configuration 확인
→ CORS 설정 확인
→ Security CORS 확인
→ ExternalApiClient 확인
→ External API Error Handling 확인
→ Logging Level 확인
→ 민감정보 노출 여부 확인
→ Anti Pattern 확인
```

---

### [FAQ]

Q. 설정 검수에서 가장 먼저 볼 것은?

A.
API Key, DB Password, JWT Secret 같은 민감정보가 코드나 Git에 하드코딩되어 있지 않은지 먼저 확인한다.

Q. CORS 검수에서 가장 중요한 것은?

A.
Frontend Origin이 정확히 등록되어 있는지, credentials와 wildcard를 잘못 조합하지 않았는지, Security CORS 설정이 맞는지 확인하는 것이다.

Q. Logging 검수에서 가장 중요한 것은?

A.
민감정보를 남기지 않고, log level을 환경별로 적절히 구분하며, 예외 원인 추적에 필요한 정보는 서버 로그에 남기는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Spring Boot Configuration은 왜 필요해?
A. DB, 외부 API, CORS, Logging, Profile 같은 실행 환경별 설정을 코드와 분리해 안전하고 유연하게 관리하기 위해 필요하다.

Q. application.yml과 application.properties 중 뭐가 좋아?
A. 둘 다 가능하다. 설정이 단순하면 properties도 충분하고, 중첩 구조가 많으면 yml이 읽기 쉽다.

Q. application.yml에서 가장 조심할 점은?
A. YAML은 들여쓰기에 민감하므로 indentation 오류를 주의해야 한다.

Q. properties와 yml을 같이 써도 돼?
A. 가능은 하지만 혼란이 생길 수 있으므로 하나의 형식으로 통일하는 것이 좋다.

Q. API Key를 application.yml에 직접 써도 돼?
A. 권장하지 않는다. API Key, DB Password, JWT Secret 같은 민감정보는 환경변수나 Secret 관리 방식을 사용하는 것이 좋다.

Q. 환경변수는 Spring Boot에서 어떻게 써?
A. `${ENV_NAME}` 형식으로 application.yml이나 properties에서 참조할 수 있다.

Q. 환경변수 기본값은 어떻게 지정해?
A. `${SERVER_PORT:8080}`처럼 콜론 뒤에 기본값을 지정할 수 있다.

Q. ${DB_URL} 값이 없으면 어떻게 돼?
A. 기본값이 없으면 실행 시 설정 바인딩 오류나 DB 연결 실패가 발생할 수 있다.

Q. @Value와 @ConfigurationProperties 중 뭐가 좋아?
A. 단일 값은 @Value도 가능하지만 관련 설정이 여러 개면 ConfigurationProperties가 구조화와 타입 안정성 측면에서 좋다.

Q. ConfigurationProperties는 언제 써?
A. 외부 API, JWT, CORS, Mail, File Upload처럼 관련 설정이 여러 개일 때 사용한다.

Q. ConfigurationProperties 값이 null이면 뭘 확인해?
A. prefix, yml key, Profile, 환경변수, EnableConfigurationProperties 또는 scan 등록 여부를 확인한다.

Q. ConfigurationProperties에도 Validation을 해야 해?
A. 필수 설정이 누락되면 운영 장애로 이어질 수 있으므로 중요한 설정은 시작 시점에 검증하는 것이 좋다.

Q. unknown property 경고가 뜨면 문제야?
A. 직접 만든 custom property는 IDE가 모를 수 있다. 실행 오류는 아닐 수 있지만 key 오타인지 확인해야 한다.

Q. Profile은 언제 써?
A. 로컬, 테스트, 운영 환경에서 DB, 로그, 외부 API, CORS 설정이 달라질 때 사용한다.

Q. Spring Boot Profile은 어떻게 나눠?
A. local, dev, test, prod처럼 실행 환경별로 나누는 것이 일반적이다.

Q. active profile은 어떻게 정해?
A. spring.profiles.active 설정이나 SPRING_PROFILES_ACTIVE 환경변수로 지정할 수 있다.

Q. 지금 어떤 Profile로 실행 중인지 어떻게 알아?
A. Application startup log에서 active profile을 확인할 수 있다.

Q. 운영 profile에는 뭘 조심해야 해?
A. debug logging, ddl-auto create, local DB, localhost CORS, 테스트 API Key가 섞이지 않도록 주의해야 한다.

Q. 테스트할 때 Profile이 왜 필요해?
A. 운영 DB나 실제 외부 API에 영향을 주지 않고 격리된 환경에서 테스트하기 위해 필요하다.

Q. test profile에서는 뭘 분리해야 해?
A. 테스트 DB, mock external API, test secret, logging level, ddl-auto 설정을 분리해야 한다.

Q. @Configuration은 언제 써?
A. 외부 라이브러리 객체를 Bean으로 등록하거나 Application 설정용 Bean을 구성할 때 사용한다.

Q. @Bean은 언제 써?
A. 외부 라이브러리 객체처럼 클래스에 직접 @Component를 붙일 수 없을 때 사용한다.

Q. 직접 만든 Service도 @Bean으로 등록해도 돼?
A. 가능은 하지만 일반적으로 직접 만든 Service는 @Service와 생성자 주입을 사용하는 것이 더 명확하다.

Q. CORS는 뭐야?
A. 다른 Origin의 Frontend가 Backend API에 접근할 수 있는지 결정하는 브라우저 보안 정책이다.

Q. Origin은 뭐야?
A. protocol, host, port 조합이다. 예를 들어 [http://localhost:3000과](http://localhost:3000과) [http://localhost:8080은](http://localhost:8080은) 서로 다른 Origin이다.

Q. CORS 에러는 Backend 에러야?
A. 서버가 정상 응답해도 브라우저 보안 정책 때문에 차단될 수 있다. Origin, Method, Header, Credentials 설정을 확인해야 한다.

Q. Postman에서는 되는데 브라우저에서는 안 되는 이유는?
A. CORS는 브라우저 보안 정책이므로 Postman에서는 차단되지 않을 수 있다.

Q. CORS를 허용하면 보안 처리가 끝난 거야?
A. 아니다. CORS는 브라우저 접근 정책이고 실제 인증 / 인가는 별도로 처리해야 한다.

Q. Spring Security를 쓰면 CORS 설정 위치가 달라져?
A. Security Filter Chain에서 CORS 요청을 처리하므로 CorsConfigurationSource와 http.cors 설정을 함께 확인해야 한다.

Q. OPTIONS 요청이 401이 나면 뭐가 문제야?
A. Preflight 요청이 인증 필터에서 차단될 수 있다. Security CORS 설정과 OPTIONS 허용 여부를 확인해야 한다.

Q. allowedOrigins("\*")를 써도 돼?
A. 개발 중 임시로는 가능하지만 운영에서는 필요한 origin만 명확히 허용하는 것이 좋다.

Q. credentials와 wildcard origin을 같이 써도 돼?
A. 주의해야 한다. 인증 정보가 포함된 요청에서는 명확한 Origin을 지정하는 것이 좋다.

Q. 외부 API 호출 코드는 Service에 바로 넣어도 돼?
A. 작은 프로젝트에서는 가능하지만 ExternalApiClient 같은 별도 Component로 분리하면 테스트와 유지보수가 쉬워진다.

Q. 외부 API 설정은 어디에 둬?
A. application.yml에 환경변수 기반으로 작성하고 ConfigurationProperties로 바인딩해 사용하는 것이 좋다.

Q. 외부 API Response DTO와 내부 Response DTO는 분리해야 해?
A. 분리하는 것이 좋다. 외부 API 스펙 변경이 내부 API 응답 구조에 직접 영향을 주지 않게 하기 위해서다.

Q. 외부 API 오류를 그대로 내려도 돼?
A. 권장하지 않는다. 외부 시스템 내부 메시지나 민감정보가 노출될 수 있으므로 내부 ErrorCode와 메시지로 변환하는 것이 좋다.

Q. 외부 API timeout은 어떻게 처리해?
A. timeout 설정을 적용하고 실패 시 EXTERNAL_API_TIMEOUT 같은 ErrorCode로 변환하는 것이 좋다.

Q. retry는 무조건 넣는 게 좋아?
A. 아니다. 결제, 주문, 알림처럼 중복 처리 위험이 있는 API는 멱등성 키와 정책 없이 retry하면 위험하다.

Q. Logging은 왜 필요해?
A. Application 동작, 오류, 요청 흐름, 외부 API 호출 결과를 기록해 문제 분석과 운영 관리를 돕기 위해 필요하다.

Q. System.out.println으로 로그 찍어도 돼?
A. 개발 중 임시 확인은 가능하지만 실무 코드에서는 Logger를 사용하는 것이 좋다.

Q. log level은 어떻게 구분해?
A. ERROR는 장애, WARN은 비정상 가능성, INFO는 주요 이벤트, DEBUG는 개발 디버깅 정보에 사용한다.

Q. 운영에서 debug log를 켜도 돼?
A. 일시적 장애 분석에는 가능하지만 상시 debug는 성능, 비용, 민감정보 노출 위험이 있어 지양한다.

Q. SQL 로그를 운영에서 켜도 돼?
A. 주의해야 한다. SQL과 parameter에 민감정보가 포함될 수 있고 로그량이 많아질 수 있다.

Q. 로그에 토큰이나 비밀번호를 남겨도 돼?
A. 안 된다. Access Token, Refresh Token, Password, API Key 같은 민감정보는 로그에 남기면 안 된다.

Q. exception.getMessage()를 Client에 그대로 반환해도 돼?
A. 권장하지 않는다. 내부 정보가 노출될 수 있으므로 통제된 메시지를 반환하는 것이 좋다.

Q. 모든 예외를 ERROR로 남겨야 해?
A. 아니다. Validation 실패나 중복 요청 같은 예상 가능한 오류는 WARN 또는 INFO로 관리할 수 있다.

Q. 설정 검수에서 가장 먼저 볼 것은?
A. API Key, DB Password, JWT Secret 같은 민감정보가 코드나 Git에 하드코딩되어 있지 않은지 먼저 확인한다.

Q. CORS 검수에서 가장 중요한 것은?
A. Frontend Origin이 정확히 등록되어 있는지, credentials와 wildcard를 잘못 조합하지 않았는지, Security CORS 설정이 맞는지 확인하는 것이다.

Q. Logging 검수에서 가장 중요한 것은?
A. 민감정보를 남기지 않고, log level을 환경별로 적절히 구분하며, 예외 원인 추적에 필요한 정보는 서버 로그에 남기는 것이다.
