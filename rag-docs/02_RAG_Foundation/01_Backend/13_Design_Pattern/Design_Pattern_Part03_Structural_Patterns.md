# Design Pattern Part03 - Structural Patterns

---

# 1. Structural Pattern Overview

## 1.1 Structural Pattern

### [개념]

Structural Pattern은 객체와 Class의 관계를 설계하여 더 유연한 구조를 만드는 Design Pattern이다.

Structural Pattern은 객체를 어떻게 연결하고 조합할지 결정한다.

Structural Pattern은 객체 간 결합도를 낮추고 기능 확장, 인터페이스 변환, 접근 제어를 지원한다.

```text
Object A
→ Structural Pattern
→ Object B
→ Flexible Collaboration
```

---

### [핵심]

- Structural Pattern은 객체 관계 설계에 집중한다.
- Structural Pattern은 객체 조합 Composition을 활용한다.
- Structural Pattern은 기존 코드를 크게 수정하지 않고 구조를 확장한다.
- Structural Pattern은 Adapter, Decorator, Proxy가 핵심이다.
- Structural Pattern은 OCP, DIP, SRP와 관련이 깊다.
- Structural Pattern은 외부 API 연동, 보안 필터, AOP, Lazy Loading에서 자주 사용된다.

---

### [실무]

2026 실무 기준 Java 21, Spring Boot 3.x Backend에서는 Structural Pattern이 Framework 내부와 애플리케이션 경계 설계에 자주 사용된다.

대표 실무 예:

- Adapter Pattern → 외부 API 응답을 내부 Port에 맞게 변환
- Decorator Pattern → 기존 기능에 인증, 로깅, 캐싱, 검증 기능 추가
- Proxy Pattern → Spring AOP, Transaction Proxy, JPA Lazy Loading Proxy
- Facade 성격 구조 → 복잡한 하위 시스템을 단순 Service API로 감싸기
- Composite 성격 구조 → 메뉴, 카테고리, 트리 구조 처리

Spring Boot 실무에서는 다음 영역에서 Structural Pattern을 검토한다.

- External API Integration
- Payment Gateway Adapter
- Notification Adapter
- File Storage Adapter
- Security Filter Chain
- Transaction AOP
- Cache Proxy
- Logging Decorator
- Legacy System Integration
- Clean Architecture Adapter Layer

---

### [주의]

- Structural Pattern은 객체 관계를 단순화하기 위한 것이다.
- 단순 호출 구조에 무리하게 Pattern을 적용하면 복잡도만 증가한다.
- Adapter와 Proxy, Decorator는 구조가 비슷해 보이지만 목적이 다르다.
- Pattern 이름보다 해결하려는 문제가 중요하다.
- 외부 시스템 연동 코드는 Domain Service 내부에 직접 섞지 않는다.

---

### [FAQ]

Q. Structural Pattern은 무엇인가?

A. 객체와 Class의 관계를 설계하여 유연한 구조를 만드는 Design Pattern이다.

Q. Structural Pattern은 언제 사용하는가?

A. 객체 관계, 인터페이스 변환, 기능 확장, 접근 제어, 외부 시스템 연동 구조가 필요할 때 사용한다.

Q. Structural Pattern의 대표 패턴은?

A. Adapter, Decorator, Proxy가 대표적이다.

Q. Structural Pattern은 어떤 원칙과 관련 있는가?

A. OCP, DIP, SRP와 관련이 깊다.

---

## 1.2 Structural Pattern Selection

### [개념]

Structural Pattern Selection은 현재 구조 문제가 인터페이스 불일치, 기능 확장, 접근 제어 중 어디에 속하는지 판단하고 적절한 Pattern을 선택하는 과정이다.

```text
Structure Problem
→ Interface Mismatch / Dynamic Extension / Access Control
→ Adapter / Decorator / Proxy
```

---

### [핵심]

- 인터페이스가 맞지 않으면 Adapter Pattern을 검토한다.
- 기존 객체에 기능을 동적으로 추가해야 하면 Decorator Pattern을 검토한다.
- 접근 제어, 지연 로딩, 부가기능 삽입이 필요하면 Proxy Pattern을 검토한다.
- 복잡한 하위 시스템을 단순하게 노출해야 하면 Facade 성격 구조를 검토한다.
- 객체 관계가 트리 구조라면 Composite 성격 구조를 검토한다.
- Pattern 선택 전 변경 지점과 객체 관계를 먼저 확인한다.

---

### [실무]

| 문제 상황                                                          | 우선 검토 Pattern |
| ------------------------------------------------------------------ | ----------------- |
| 외부 API 응답 구조가 내부 모델과 다르다                            | Adapter           |
| Legacy Interface를 새 Interface에 맞춰야 한다                      | Adapter           |
| 기존 기능 전후에 로깅, 검증, 캐싱을 추가해야 한다                  | Decorator         |
| 여러 Filter가 요청을 순차 처리한다                                 | Decorator / Chain |
| Service 호출 전후에 Transaction, Security, Logging을 삽입해야 한다 | Proxy             |
| JPA 연관 객체를 실제 사용 시점에 로딩해야 한다                     | Proxy             |
| 복잡한 외부 SDK를 단순 API로 감싸야 한다                           | Facade            |
| 카테고리, 댓글, 조직도 같은 계층 구조를 다뤄야 한다                | Composite         |

---

### [예제]

```text
Kakao Map API Response
→ Internal Location DTO Interface와 다름
→ Adapter Pattern 후보
```

```text
PaymentService 실행 전후로 Logging, Validation 추가
→ 기존 기능에 부가기능 확장
→ Decorator Pattern 후보
```

```text
Service Method 실행 전 Transaction 처리
→ 실제 객체 접근 전후 제어
→ Proxy Pattern 후보
```

---

### [주의]

- Adapter는 인터페이스 변환이 목적이다.
- Decorator는 기능 확장이 목적이다.
- Proxy는 접근 제어 또는 대리 호출이 목적이다.
- Pattern 목적이 다르면 비슷한 구조라도 다른 Pattern으로 판단한다.
- Structural Pattern은 객체 조합을 우선하고 무리한 상속을 피한다.

---

### [FAQ]

Q. Adapter와 Decorator는 어떻게 구분하는가?

A. Adapter는 인터페이스 변환이 목적이고 Decorator는 기존 기능 확장이 목적이다.

Q. Decorator와 Proxy는 어떻게 구분하는가?

A. Decorator는 기능 추가가 목적이고 Proxy는 접근 제어, 지연 로딩, 부가기능 삽입이 목적이다.

Q. Structural Pattern 선택 기준은?

A. 구조 문제가 인터페이스 불일치, 기능 확장, 접근 제어 중 어디에 속하는지 판단한다.

Q. Spring에서 Structural Pattern은 어디에 많이 쓰이는가?

A. AOP Proxy, Transaction Proxy, Security Filter Chain, External API Adapter, JPA Lazy Loading에서 자주 쓰인다.

---

# 2. Adapter Pattern

## 2.1 Adapter

### [개념]

Adapter Pattern은 서로 호환되지 않는 인터페이스를 연결하기 위해 중간 변환 객체를 두는 Structural Pattern이다.

Adapter는 Client가 기대하는 Interface와 실제 구현체 또는 외부 시스템의 Interface가 다를 때 사용한다.

```text
Client
→ Target Interface
→ Adapter
→ Adaptee
```

---

### [핵심]

- Adapter는 Interface Compatibility 문제를 해결한다.
- Adapter는 외부 시스템과 내부 도메인 사이의 변환 계층이다.
- Adapter는 Client가 외부 구현체를 직접 알지 않게 만든다.
- Adapter는 DIP, Clean Architecture, Hexagonal Architecture와 관련이 깊다.
- Adapter는 외부 API 변경의 영향을 내부 코드로 전파하지 않게 한다.
- Adapter는 Legacy System Integration에 유용하다.

---

### [실무]

Spring Boot Backend에서 Adapter는 외부 API, 결제, 파일 저장소, 메시징, 지도 API 연동에 자주 사용된다.

나쁜 예:

```java
@Service
public class FestivalService {
    private final KakaoMapClient kakaoMapClient;

    public LocationResponse getLocation(String address) {
        KakaoMapResponse response = kakaoMapClient.search(address);

        return new LocationResponse(
                response.documents().get(0).x(),
                response.documents().get(0).y()
        );
    }
}
```

문제:

- FestivalService가 KakaoMapResponse 구조를 직접 알고 있다.
- 외부 API 응답 변경 시 Service가 수정된다.
- 테스트에서 외부 Client 대체가 어렵다.
- 내부 Use Case와 Infrastructure가 강하게 결합된다.

좋은 방향:

```text
FestivalService
→ LocationPort
← KakaoMapAdapter
→ KakaoMapClient
```

---

### [예제]

Port 정의:

```java
public interface LocationPort {
    LocationResult searchByAddress(String address);
}
```

내부 결과 모델:

```java
public record LocationResult(
        double longitude,
        double latitude
) {
}
```

Adapter 구현:

```java
@Component
public class KakaoMapAdapter implements LocationPort {
    private final KakaoMapClient kakaoMapClient;

    public KakaoMapAdapter(KakaoMapClient kakaoMapClient) {
        this.kakaoMapClient = kakaoMapClient;
    }

    @Override
    public LocationResult searchByAddress(String address) {
        KakaoMapResponse response = kakaoMapClient.search(address);

        KakaoMapDocument document = response.documents().get(0);

        return new LocationResult(
                Double.parseDouble(document.x()),
                Double.parseDouble(document.y())
        );
    }
}
```

Service:

```java
@Service
public class FestivalService {
    private final LocationPort locationPort;

    public FestivalService(LocationPort locationPort) {
        this.locationPort = locationPort;
    }

    public LocationResult getLocation(String address) {
        return locationPort.searchByAddress(address);
    }
}
```

---

### [Best Practice]

- 외부 API DTO를 Domain 또는 Application Service에 직접 노출하지 않는다.
- Adapter는 외부 응답을 내부 모델로 변환한다.
- Adapter는 외부 시스템 예외를 내부 예외로 변환한다.
- Adapter Interface는 Application 또는 Domain이 필요로 하는 형태로 정의한다.
- Adapter 구현체는 Infrastructure Layer에 둔다.
- 테스트에서는 Fake Adapter 또는 Mock Port로 대체한다.

---

### [주의]

- Adapter에 비즈니스 정책을 넣지 않는다.
- Adapter가 외부 API 호출과 내부 정책 판단을 동시에 담당하면 SRP 위반이다.
- Adapter Interface를 외부 API 형태로 만들면 Adapter의 의미가 약해진다.
- 모든 외부 Client에 무조건 Adapter를 만들 필요는 없지만 변경 가능성이 높으면 권장된다.
- Adapter가 너무 많아지면 Layer 구조를 명확히 관리해야 한다.

---

### [FAQ]

Q. Adapter Pattern은 무엇인가?

A. 호환되지 않는 인터페이스를 연결하기 위해 중간 변환 객체를 두는 Structural Pattern이다.

Q. Adapter Pattern은 언제 사용하는가?

A. 외부 API, Legacy System, SDK, 다른 Interface를 내부 코드가 기대하는 형태로 변환해야 할 때 사용한다.

Q. Adapter는 어떤 원칙과 관련 있는가?

A. DIP, SRP, OCP와 관련이 깊다.

Q. Adapter에는 어떤 로직을 넣어야 하는가?

A. 외부 호출, 응답 변환, 예외 변환, 프로토콜 변환을 넣고 핵심 비즈니스 정책은 넣지 않는다.

---

## 2.2 Adapter and Hexagonal Architecture

### [개념]

Hexagonal Architecture에서 Adapter는 Port를 구현하거나 Port를 통해 외부 세계와 연결하는 역할을 한다.

Port는 Application이 필요로 하는 Interface이고 Adapter는 실제 외부 기술 구현이다.

```text
Application Core
→ Port
← Adapter
→ External System
```

---

### [핵심]

- Port는 내부 핵심 로직이 원하는 계약이다.
- Adapter는 외부 기술 세부사항을 담당한다.
- Domain/Application은 Infrastructure에 직접 의존하지 않는다.
- Adapter는 외부 시스템 변경을 내부로부터 격리한다.
- Hexagonal Architecture의 핵심은 Dependency Direction이다.
- Adapter는 DIP를 실현하는 구조이다.

---

### [실무]

결제 연동 구조:

```text
OrderService
→ PaymentPort
← TossPaymentAdapter
→ TossPaymentClient
```

Port:

```java
public interface PaymentPort {
    PaymentResult pay(PaymentCommand command);
}
```

Adapter:

```java
@Component
public class TossPaymentAdapter implements PaymentPort {
    private final TossPaymentClient tossPaymentClient;

    public TossPaymentAdapter(TossPaymentClient tossPaymentClient) {
        this.tossPaymentClient = tossPaymentClient;
    }

    @Override
    public PaymentResult pay(PaymentCommand command) {
        TossPaymentResponse response = tossPaymentClient.pay(command);

        return new PaymentResult(
                response.paymentKey(),
                response.approvedAt()
        );
    }
}
```

Application Service:

```java
@Service
public class OrderService {
    private final PaymentPort paymentPort;

    public OrderService(PaymentPort paymentPort) {
        this.paymentPort = paymentPort;
    }

    public void order(PaymentCommand command) {
        PaymentResult result = paymentPort.pay(command);
        // order process
    }
}
```

---

### [Best Practice]

- Port는 외부 기술 이름을 포함하지 않는다.
- `TossPaymentPort`보다 `PaymentPort`가 일반적으로 더 적절하다.
- Adapter 이름에는 구현 기술명을 포함할 수 있다.
- 외부 DTO는 Adapter 내부에서만 사용한다.
- Application Service는 Port에만 의존한다.
- Adapter는 Infrastructure Package에 둔다.

---

### [주의]

- Port를 외부 API 스펙 그대로 만들면 내부가 외부에 종속된다.
- 모든 Repository를 Port로 감싸는 것은 프로젝트 규모에 따라 과할 수 있다.
- Hexagonal Architecture는 복잡도가 증가하므로 적용 범위를 정해야 한다.
- 단순 CRUD 프로젝트에 모든 Adapter 계층을 강제하면 Over Engineering이 될 수 있다.

---

### [FAQ]

Q. Hexagonal Architecture에서 Adapter는 무엇인가?

A. 내부 Port와 외부 시스템을 연결하는 기술 구현 계층이다.

Q. Port와 Adapter의 차이는?

A. Port는 내부가 요구하는 Interface이고 Adapter는 그 Interface를 구현해 외부 기술과 연결하는 객체이다.

Q. Adapter 이름에 외부 기술명을 넣어도 되는가?

A. Adapter 구현체에는 넣어도 된다. 다만 Port 이름은 외부 기술에 종속되지 않는 것이 좋다.

Q. Adapter는 어디에 위치하는가?

A. 일반적으로 Infrastructure Layer 또는 Adapter Package에 위치한다.

---

## 2.3 External API Adapter

### [개념]

External API Adapter는 외부 REST API, SDK, Message Broker, Storage 등 외부 시스템을 내부 Application Interface에 맞게 변환하는 Adapter이다.

External API Adapter는 외부 변화로부터 내부 코드를 보호한다.

```text
Application Service
→ External Port
← External API Adapter
→ REST API / SDK / Broker / Storage
```

---

### [핵심]

- External API Adapter는 외부 연동 경계이다.
- 외부 Request DTO와 Response DTO를 내부 모델로 변환한다.
- 외부 예외를 내부 예외 체계로 변환한다.
- Retry, Timeout, Circuit Breaker 같은 기술 정책을 포함할 수 있다.
- 핵심 비즈니스 정책은 Adapter가 아니라 Application Service에 둔다.
- 테스트에서는 Fake Adapter로 외부 시스템을 대체할 수 있다.

---

### [실무]

External API Adapter에 포함 가능한 책임:

- HTTP Client 호출
- SDK 호출
- Request Mapping
- Response Mapping
- Error Mapping
- Timeout Handling
- Retry Policy
- Logging
- Observability Tagging
- Rate Limit 대응

External API Adapter에 넣지 않는 책임:

- 주문 상태 결정
- 할인 정책 계산
- 사용자 권한 판단
- 도메인 규칙 검증
- Use Case 흐름 제어

---

### [예제]

```java
@Component
public class TourApiFestivalAdapter implements FestivalExternalPort {
    private final TourApiClient tourApiClient;

    public TourApiFestivalAdapter(TourApiClient tourApiClient) {
        this.tourApiClient = tourApiClient;
    }

    @Override
    public List<ExternalFestivalResult> fetchFestivals(FestivalSearchCondition condition) {
        TourApiResponse response = tourApiClient.search(condition);

        return response.items().stream()
                .map(item -> new ExternalFestivalResult(
                        item.contentId(),
                        item.title(),
                        item.addr1(),
                        item.mapX(),
                        item.mapY()
                ))
                .toList();
    }
}
```

---

### [Best Practice]

- 외부 API 응답을 내부 DTO로 즉시 변환한다.
- 외부 API Key, URL, Timeout은 Configuration으로 분리한다.
- 외부 API 장애는 명확한 Custom Exception으로 변환한다.
- Adapter 단위 Integration Test를 작성한다.
- 외부 시스템이 느리거나 불안정하면 Timeout과 Retry를 설정한다.
- 호출량 제한이 있으면 Rate Limit 전략을 별도로 둔다.

---

### [주의]

- 외부 API DTO를 Controller Response로 그대로 반환하지 않는다.
- Adapter에서 Transaction을 길게 유지하지 않는다.
- 외부 API 장애가 전체 Use Case를 중단해야 하는지 판단한다.
- Retry는 중복 요청과 부작용을 고려해야 한다.
- Adapter가 커지면 Mapper, Client, ErrorHandler로 분리한다.

---

### [FAQ]

Q. External API Adapter는 무엇인가?

A. 외부 시스템을 내부 Application Interface에 맞게 변환하고 격리하는 Adapter이다.

Q. 외부 API DTO를 내부 Service에서 직접 사용하면 안 되는 이유는?

A. 외부 응답 구조 변경이 내부 비즈니스 코드까지 전파되기 때문이다.

Q. External API Adapter에 Retry를 넣어도 되는가?

A. 기술적 재시도 정책은 가능하다. 다만 중복 처리와 부작용을 반드시 고려해야 한다.

Q. External API Adapter 테스트는 어떻게 하는가?

A. Adapter 단위 테스트, Mock Server, Fake Client, Integration Test를 사용한다.

---

# 3. Decorator Pattern

## 3.1 Decorator

### [개념]

Decorator Pattern은 기존 객체를 감싸서 기존 기능은 유지하면서 새로운 기능을 동적으로 추가하는 Structural Pattern이다.

Decorator는 상속 대신 Composition으로 기능을 확장한다.

```text
Client
→ Decorator
→ Target Object
→ Original Behavior + Added Behavior
```

---

### [핵심]

- Decorator는 Dynamic Extension을 지원한다.
- Decorator는 기존 객체를 감싸서 기능을 추가한다.
- Decorator는 상속보다 유연한 기능 확장을 제공한다.
- Decorator는 OCP를 지원한다.
- Decorator는 Logging, Caching, Validation, Security, Metrics에 자주 사용된다.
- Decorator는 여러 개를 조합할 수 있다.

---

### [실무]

Spring Security Filter Chain은 Decorator 성격의 구조로 이해할 수 있다.

```text
Request
→ Filter A
→ Filter B
→ Filter C
→ Controller
```

각 Filter는 요청을 감싸고 전후에 기능을 추가한다.

Decorator는 다음 상황에서 유용하다.

- 기존 Service 기능 전후에 Logging 추가
- 기존 Query 기능에 Cache 추가
- 기존 Sender 기능에 Retry 추가
- 기존 Processor 기능에 Validation 추가
- 기존 API 호출에 Metrics 수집 추가

---

### [예제]

기본 Interface:

```java
public interface MessageSender {
    void send(String message);
}
```

기본 구현체:

```java
@Component
public class EmailMessageSender implements MessageSender {
    @Override
    public void send(String message) {
        // send email
    }
}
```

Logging Decorator:

```java
@Component
public class LoggingMessageSenderDecorator implements MessageSender {
    private final MessageSender messageSender;

    public LoggingMessageSenderDecorator(MessageSender messageSender) {
        this.messageSender = messageSender;
    }

    @Override
    public void send(String message) {
        System.out.println("send message start");
        messageSender.send(message);
        System.out.println("send message end");
    }
}
```

실무에서는 Bean 순환 또는 주입 충돌을 피하기 위해 `@Primary`, `@Qualifier`, Config 등록을 함께 고려한다.

---

### [Best Practice]

- Decorator는 같은 Interface를 구현한다.
- Decorator는 원본 객체를 내부에 가진다.
- Decorator는 핵심 기능보다 부가기능을 추가한다.
- 여러 Decorator가 있으면 순서를 명확히 관리한다.
- Spring에서는 Bean 등록 방식과 주입 대상을 명확히 설정한다.
- 공통 부가기능은 AOP 또는 Filter로 대체 가능한지 검토한다.

---

### [주의]

- Decorator가 너무 많으면 호출 흐름 추적이 어려워진다.
- Decorator 순서가 결과에 영향을 줄 수 있다.
- Decorator에 핵심 비즈니스 로직을 넣으면 책임이 흐려진다.
- Spring Bean 주입 시 자기 자신을 주입하는 순환 참조에 주의한다.
- 단순한 부가기능은 AOP가 더 적합할 수 있다.

---

### [FAQ]

Q. Decorator Pattern은 무엇인가?

A. 기존 객체를 감싸 기존 기능은 유지하면서 새로운 기능을 동적으로 추가하는 Structural Pattern이다.

Q. Decorator Pattern은 언제 사용하는가?

A. 기존 기능 전후에 로깅, 캐싱, 검증, 보안, 메트릭 같은 부가기능을 추가할 때 사용한다.

Q. Decorator와 상속의 차이는?

A. 상속은 정적인 확장이고 Decorator는 Composition을 통한 동적인 기능 확장이다.

Q. Decorator는 어떤 원칙과 관련 있는가?

A. OCP와 SRP와 관련이 깊다.

---

## 3.2 Decorator and Spring Security Filter Chain

### [개념]

Spring Security Filter Chain은 여러 Filter가 Request와 Response를 감싸며 인증, 인가, 예외 처리, 세션, CORS, CSRF 같은 부가기능을 순차적으로 수행하는 구조이다.

Decorator Pattern과 Chain of Responsibility Pattern 성격을 함께 가진다.

```text
Request
→ Security Filter 1
→ Security Filter 2
→ Security Filter 3
→ DispatcherServlet
→ Controller
```

---

### [핵심]

- Filter는 Request 처리 전후에 부가기능을 추가한다.
- Filter Chain은 여러 Filter를 순서대로 실행한다.
- 각 Filter는 다음 Filter로 요청을 넘길 수 있다.
- Security Filter는 인증, 인가, 예외 처리에 사용된다.
- Decorator 관점에서는 요청 처리를 감싸 기능을 추가한다.
- Chain 관점에서는 책임을 순차적으로 전달한다.

---

### [실무]

JWT Authentication Filter 예:

```java
public class JwtAuthenticationFilter extends OncePerRequestFilter {
    @Override
    protected void doFilterInternal(
            HttpServletRequest request,
            HttpServletResponse response,
            FilterChain filterChain
    ) throws ServletException, IOException {
        String token = resolveToken(request);

        if (token != null) {
            Authentication authentication = authenticate(token);
            SecurityContextHolder.getContext().setAuthentication(authentication);
        }

        filterChain.doFilter(request, response);
    }
}
```

흐름:

```text
HTTP Request
→ JwtAuthenticationFilter
→ SecurityContext 설정
→ AuthorizationFilter
→ Controller
```

---

### [Best Practice]

- Filter 순서를 명확히 관리한다.
- 인증 Filter는 SecurityContext 설정 책임에 집중한다.
- 예외 처리는 AuthenticationEntryPoint, AccessDeniedHandler와 분리한다.
- JWT Parsing, Validation은 별도 Provider 또는 Service로 분리한다.
- Filter에 비즈니스 로직을 넣지 않는다.
- Filter는 요청 흐름을 막을지 다음 Filter로 넘길지 명확히 결정한다.

---

### [주의]

- Filter에서 `filterChain.doFilter()` 호출 누락 시 요청이 중단된다.
- Filter 순서가 잘못되면 인증/인가가 정상 동작하지 않는다.
- Filter에서 DB 조회를 과도하게 수행하면 성능 문제가 생긴다.
- Filter는 모든 요청에 영향을 줄 수 있으므로 책임을 작게 유지한다.
- Security Filter Chain은 단순 Decorator보다 Chain of Responsibility 성격이 강하다.

---

### [FAQ]

Q. Spring Security Filter Chain은 Decorator Pattern인가?

A. 요청 처리를 감싸 부가기능을 추가한다는 점에서 Decorator 성격이 있고, 순차 책임 전달 측면에서는 Chain of Responsibility 성격도 있다.

Q. Filter는 어떤 역할을 하는가?

A. Controller 도달 전후에 인증, 인가, 로깅, CORS, 예외 처리 같은 부가기능을 수행한다.

Q. JWT Filter의 핵심 책임은?

A. Token을 검증하고 Authentication을 만들어 SecurityContext에 저장하는 것이다.

Q. Filter에 비즈니스 로직을 넣어도 되는가?

A. 권장하지 않는다. Filter는 요청 전후 처리에 집중하고 비즈니스 로직은 Service에 둔다.

---

## 3.3 Decorator vs AOP

### [개념]

Decorator와 AOP는 모두 기존 기능 전후에 부가기능을 추가할 수 있다.

Decorator는 객체 조합을 통해 기능을 감싸고, AOP는 Proxy 기반으로 Cross-Cutting Concern을 분리한다.

```text
Decorator
→ Object Composition

AOP
→ Proxy + Advice + Pointcut
```

---

### [핵심]

- Decorator는 명시적인 객체 조합이다.
- AOP는 선언적인 부가기능 적용 방식이다.
- Decorator는 특정 Interface 단위 기능 확장에 적합하다.
- AOP는 Logging, Transaction, Security, Metrics 같은 공통 관심사에 적합하다.
- AOP는 Spring Proxy와 관련이 깊다.
- Decorator는 호출 흐름이 코드에 더 명시적으로 보인다.

---

### [실무]

Decorator가 적합한 경우:

- 특정 구현체에만 기능 추가
- Interface 기반 기능 조합 필요
- 런타임 조합 또는 교체 필요
- 테스트에서 Decorator 단위 검증 필요

AOP가 적합한 경우:

- 여러 Service Method에 공통 Logging 적용
- Transaction 처리
- Method 실행 시간 측정
- 권한 검증 Annotation 처리
- 반복되는 Cross-Cutting Concern 분리

---

### [Comparison]

| 기준        | Decorator           | AOP                           |
| ----------- | ------------------- | ----------------------------- |
| 방식        | 객체 조합           | Proxy 기반 관점 분리          |
| 적용 범위   | 특정 객체/Interface | 여러 Join Point               |
| 명시성      | 코드에 명시적       | 설정/Annotation 기반          |
| 적합한 기능 | 기능 조합, Wrapper  | Logging, Transaction, Metrics |
| 주의점      | Decorator 증가      | Proxy 동작 이해 필요          |

---

### [주의]

- AOP는 내부 메서드 호출 Self Invocation에서 동작하지 않을 수 있다.
- Decorator는 Bean 주입 구조가 복잡해질 수 있다.
- 공통 관심사를 Decorator로 모두 처리하면 Wrapper가 많아진다.
- 특정 객체 기능 확장은 Decorator가 더 명확할 수 있다.
- 전역 공통 기능은 AOP가 더 적합할 수 있다.

---

### [FAQ]

Q. Decorator와 AOP의 차이는?

A. Decorator는 객체 조합으로 기능을 감싸고 AOP는 Proxy와 Advice로 공통 관심사를 분리한다.

Q. Logging은 Decorator와 AOP 중 무엇이 좋은가?

A. 전역 공통 Logging은 AOP가 적합하고 특정 객체 Logging은 Decorator가 적합할 수 있다.

Q. Transaction은 Decorator인가 AOP인가?

A. Spring Transaction은 Proxy 기반 AOP로 동작한다.

Q. Decorator 대신 AOP를 써도 되는가?

A. 목적에 따라 가능하다. 공통 관심사는 AOP, 특정 객체 기능 조합은 Decorator를 우선 검토한다.

---

# 4. Proxy Pattern

## 4.1 Proxy

### [개념]

Proxy Pattern은 실제 객체에 대한 접근을 대리 객체가 대신 제어하는 Structural Pattern이다.

Proxy는 Client와 Real Subject 사이에서 접근 제어, 지연 로딩, 캐싱, 로깅, 보안, 트랜잭션 같은 부가기능을 수행한다.

```text
Client
→ Proxy
→ Real Subject
```

---

### [핵심]

- Proxy는 대리 객체이다.
- Proxy는 실제 객체 접근을 제어한다.
- Proxy는 Lazy Loading, Access Control, AOP에 사용된다.
- Proxy는 원본 객체와 같은 Interface를 제공할 수 있다.
- Proxy는 호출 전후에 부가기능을 삽입할 수 있다.
- Spring AOP와 JPA Lazy Loading은 Proxy 이해가 중요하다.

---

### [실무]

Proxy는 Spring Boot Backend에서 매우 자주 등장한다.

대표 예:

- Spring Transaction Proxy
- Spring Security Method Authorization Proxy
- Spring AOP Logging Proxy
- JPA Lazy Loading Proxy
- Hibernate Proxy
- Cache Proxy
- Remote Proxy

Spring Transaction 흐름:

```text
Client
→ Transaction Proxy
→ Transaction Begin
→ Service Method
→ Commit / Rollback
```

---

### [예제]

공통 Interface:

```java
public interface ImageLoader {
    Image load(String path);
}
```

Real Subject:

```java
public class RealImageLoader implements ImageLoader {
    @Override
    public Image load(String path) {
        return loadFromDisk(path);
    }

    private Image loadFromDisk(String path) {
        return new Image(path);
    }
}
```

Proxy:

```java
public class CachedImageLoaderProxy implements ImageLoader {
    private final ImageLoader imageLoader;
    private final Map<String, Image> cache = new HashMap<>();

    public CachedImageLoaderProxy(ImageLoader imageLoader) {
        this.imageLoader = imageLoader;
    }

    @Override
    public Image load(String path) {
        return cache.computeIfAbsent(path, imageLoader::load);
    }
}
```

---

### [Best Practice]

- Proxy는 실제 객체와 동일한 계약을 유지한다.
- Proxy는 접근 제어 또는 부가기능에 집중한다.
- Proxy 내부에 핵심 비즈니스 로직을 넣지 않는다.
- Spring Proxy 동작 방식 JDK Dynamic Proxy, CGLIB Proxy 차이를 이해한다.
- Transaction, Security, AOP는 Proxy 기반 제약을 고려한다.
- JPA Lazy Loading Proxy는 Transaction 범위 안에서 접근한다.

---

### [주의]

- Proxy 내부 호출 Self Invocation은 AOP가 적용되지 않을 수 있다.
- Proxy가 실제 객체를 완전히 대체하려면 계약을 지켜야 한다.
- Lazy Loading Proxy는 Transaction 밖에서 접근하면 LazyInitializationException이 발생할 수 있다.
- Proxy가 너무 많으면 호출 흐름 디버깅이 어려워진다.
- Proxy와 Decorator는 구조가 비슷하지만 목적이 다르다.

---

### [FAQ]

Q. Proxy Pattern은 무엇인가?

A. 실제 객체에 대한 접근을 대리 객체가 대신 제어하는 Structural Pattern이다.

Q. Proxy Pattern은 언제 사용하는가?

A. 접근 제어, 지연 로딩, 캐싱, 로깅, 보안, 트랜잭션 같은 부가기능이 필요할 때 사용한다.

Q. Spring AOP는 Proxy Pattern인가?

A. Spring AOP는 Proxy 기반으로 동작하며 Proxy Pattern의 대표적인 실무 예이다.

Q. JPA Lazy Loading은 Proxy와 관련 있는가?

A. 그렇다. JPA는 연관 객체를 Proxy로 두고 실제 접근 시점에 로딩할 수 있다.

---

## 4.2 Spring AOP Proxy

### [개념]

Spring AOP Proxy는 Target Bean을 감싼 Proxy 객체를 만들어 Method 호출 전후에 Advice를 적용하는 구조이다.

Spring AOP는 Runtime Weaving 방식으로 동작한다.

```text
Client
→ Spring Proxy
→ Advice
→ Target Method
→ Advice
→ Return
```

---

### [핵심]

- Spring AOP는 Proxy 기반이다.
- Advice는 Method 실행 전후에 공통 기능을 수행한다.
- Pointcut은 Advice 적용 대상을 결정한다.
- Target Bean은 Proxy로 감싸져 주입될 수 있다.
- Transaction, Logging, Security, Metrics에 사용된다.
- Self Invocation 문제를 주의해야 한다.

---

### [실무]

Transaction Proxy 예:

```java
@Service
public class OrderService {
    @Transactional
    public void order(OrderCommand command) {
        // business logic
    }
}
```

실제 흐름:

```text
Controller
→ OrderService Proxy
→ Transaction Begin
→ OrderService.order()
→ Commit
```

AOP Logging 예:

```java
@Aspect
@Component
public class LoggingAspect {
    @Around("@annotation(LogExecutionTime)")
    public Object log(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();

        try {
            return joinPoint.proceed();
        } finally {
            long end = System.currentTimeMillis();
            System.out.println("execution time = " + (end - start));
        }
    }
}
```

---

### [Best Practice]

- Transaction Annotation은 외부에서 호출되는 public method에 적용한다.
- 같은 Class 내부 메서드 호출에는 Proxy가 적용되지 않을 수 있다.
- AOP는 공통 관심사에 사용한다.
- 비즈니스 로직을 Aspect에 넣지 않는다.
- Pointcut 범위를 너무 넓게 잡지 않는다.
- AOP 적용 여부는 테스트로 검증한다.

---

### [주의]

- Self Invocation은 Spring Proxy를 거치지 않는다.
- private method에는 일반적인 Spring AOP가 적용되지 않는다.
- final class 또는 final method는 Proxy 방식에 따라 제약이 있을 수 있다.
- AOP가 많아지면 실행 흐름 파악이 어려워진다.
- 예외 처리 Advice가 실제 예외를 숨기지 않게 주의한다.

---

### [FAQ]

Q. Spring AOP Proxy는 무엇인가?

A. Target Bean을 Proxy로 감싸 Method 호출 전후에 Advice를 적용하는 Spring AOP 구조이다.

Q. Self Invocation이란?

A. 같은 Class 내부에서 자기 자신의 메서드를 호출하는 것이다. 이 경우 Proxy를 거치지 않아 AOP가 적용되지 않을 수 있다.

Q. `@Transactional`이 동작하지 않는 흔한 이유는?

A. Self Invocation, private method 적용, Proxy가 아닌 객체 직접 생성, 예외 처리 방식 문제가 흔하다.

Q. AOP에는 어떤 로직을 넣어야 하는가?

A. Logging, Transaction, Security, Metrics 같은 공통 관심사를 넣고 핵심 비즈니스 로직은 넣지 않는다.

---

## 4.3 JPA Lazy Loading Proxy

### [개념]

JPA Lazy Loading Proxy는 연관 Entity를 실제로 즉시 조회하지 않고 Proxy 객체로 대체한 뒤, 해당 연관 객체에 접근하는 시점에 DB에서 조회하는 구조이다.

```text
Entity Load
→ Association Proxy
→ Access Association
→ SQL Select
→ Real Entity
```

---

### [핵심]

- Lazy Loading은 지연 조회이다.
- JPA는 연관 객체를 Proxy로 감쌀 수 있다.
- Proxy는 실제 데이터 접근 시점에 초기화된다.
- Transaction 밖에서 Lazy Proxy 접근 시 LazyInitializationException이 발생할 수 있다.
- Fetch Join, EntityGraph, DTO Projection으로 조회 전략을 제어한다.
- Lazy Loading은 성능 최적화와 N+1 문제 모두와 관련이 있다.

---

### [실무]

Entity 예:

```java
@Entity
public class Review {
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "festival_id")
    private Festival festival;
}
```

흐름:

```text
Review 조회
→ Festival은 Proxy
→ review.getFestival().getTitle()
→ Festival 조회 SQL 실행
```

N+1 문제 예:

```text
Review 목록 10개 조회
→ 각 Review의 Festival 접근
→ Festival 조회 SQL 10번 추가
```

해결 방향:

```java
@Query("""
    select r
    from Review r
    join fetch r.festival
    where r.user.userId = :userId
""")
List<Review> findAllWithFestivalByUserId(Long userId);
```

---

### [Best Practice]

- 연관관계 기본은 `FetchType.LAZY`를 우선 검토한다.
- 화면 응답에 필요한 연관 데이터는 Fetch Join 또는 DTO Projection으로 조회한다.
- Transaction 범위 밖에서 Entity Lazy Field를 접근하지 않는다.
- Controller로 Entity를 직접 반환하지 않는다.
- 조회 전용 API는 DTO Projection을 적극 검토한다.
- N+1 문제는 SQL 로그로 확인한다.

---

### [주의]

- Lazy Loading은 무조건 성능이 좋은 것이 아니다.
- 잘못 사용하면 N+1 문제가 발생한다.
- OSIV 설정에 따라 Lazy Loading 동작 범위가 달라질 수 있다.
- Entity를 JSON 직렬화하면 Lazy Proxy 초기화 문제가 발생할 수 있다.
- `toString()`, `equals()`, `hashCode()`에서 Lazy Field 접근을 주의한다.

---

### [FAQ]

Q. JPA Lazy Loading Proxy는 무엇인가?

A. 연관 Entity를 Proxy로 두고 실제 접근 시점에 DB에서 조회하는 지연 로딩 구조이다.

Q. LazyInitializationException은 왜 발생하는가?

A. 영속성 Context 또는 Transaction이 닫힌 뒤 Lazy Proxy를 초기화하려고 할 때 발생한다.

Q. N+1 문제는 왜 발생하는가?

A. 목록 조회 후 각 Entity의 Lazy 연관 객체를 개별적으로 조회하면서 SQL이 추가로 반복 실행되기 때문이다.

Q. N+1 문제 해결 방법은?

A. Fetch Join, EntityGraph, Batch Size, DTO Projection을 사용한다.

---

# 5. Additional Structural Patterns

## 5.1 Facade Pattern

### [개념]

Facade Pattern은 복잡한 하위 시스템을 단순한 Interface로 감싸 Client가 쉽게 사용할 수 있도록 만드는 Structural Pattern이다.

Facade는 복잡한 내부 흐름을 숨기고 단순한 진입점을 제공한다.

```text
Client
→ Facade
→ Subsystem A
→ Subsystem B
→ Subsystem C
```

---

### [핵심]

- Facade는 복잡한 하위 시스템을 단순화한다.
- Facade는 Client와 하위 시스템 간 결합도를 낮춘다.
- Facade는 여러 Service나 Client 호출을 하나의 API로 제공한다.
- Facade는 Use Case 흐름 조정에 사용될 수 있다.
- Facade는 내부 복잡도를 숨기지만 책임이 과도해질 수 있다.

---

### [실무]

Facade는 다음 상황에서 사용한다.

- 여러 외부 API를 조합하는 기능
- 복잡한 결제 승인 + 저장 + 알림 흐름
- 여러 하위 Service를 조합하는 Application Service
- 복잡한 SDK 호출을 단순 Method로 감싸기
- Controller가 여러 Service를 직접 호출하는 구조 개선

예:

```java
@Service
public class OrderFacade {
    private final OrderService orderService;
    private final PaymentService paymentService;
    private final NotificationService notificationService;

    public OrderFacade(
            OrderService orderService,
            PaymentService paymentService,
            NotificationService notificationService
    ) {
        this.orderService = orderService;
        this.paymentService = paymentService;
        this.notificationService = notificationService;
    }

    public void placeOrder(OrderCommand command) {
        Order order = orderService.createOrder(command);
        paymentService.pay(order);
        notificationService.sendOrderCompleted(order);
    }
}
```

---

### [Best Practice]

- Facade는 하위 시스템 조합과 흐름 제어에 집중한다.
- Controller가 여러 Service를 복잡하게 호출하면 Facade를 검토한다.
- Facade에 세부 비즈니스 계산 로직을 모두 넣지 않는다.
- Facade가 커지면 Use Case별로 분리한다.
- Facade 이름은 목적 중심으로 작성한다.

---

### [주의]

- Facade가 모든 기능을 모으면 God Facade가 된다.
- Facade는 단순 포장만 반복하면 불필요한 계층이 된다.
- Transaction 경계가 Facade에 있어야 하는지 Service에 있어야 하는지 명확히 한다.
- Facade가 Domain Rule을 우회하지 않게 한다.

---

### [FAQ]

Q. Facade Pattern은 무엇인가?

A. 복잡한 하위 시스템을 단순한 Interface로 감싸 Client가 쉽게 사용할 수 있게 하는 Pattern이다.

Q. Facade는 언제 사용하는가?

A. 여러 Service나 외부 시스템 호출을 하나의 단순한 흐름으로 제공해야 할 때 사용한다.

Q. Facade와 Service의 차이는?

A. Service는 특정 비즈니스 책임을 담당하고 Facade는 여러 하위 기능을 조합해 단순 진입점을 제공한다.

Q. Facade의 위험은?

A. 모든 흐름을 한 곳에 모으면 God Facade가 될 수 있다.

---

## 5.2 Composite Pattern

### [개념]

Composite Pattern은 객체를 트리 구조로 구성하여 개별 객체와 객체 그룹을 동일한 방식으로 다룰 수 있게 하는 Structural Pattern이다.

```text
Component
→ Leaf
→ Composite
    → Leaf
    → Composite
```

---

### [핵심]

- Composite는 Tree Structure를 표현한다.
- 개별 객체 Leaf와 그룹 Composite를 동일 Interface로 다룬다.
- 계층형 데이터 처리에 유용하다.
- 카테고리, 메뉴, 댓글, 조직도, 파일 시스템에 적합하다.
- 재귀 구조와 함께 사용된다.

---

### [실무]

댓글 계층 구조 예:

```java
public class CommentNode {
    private Long commentId;
    private String content;
    private List<CommentNode> children = new ArrayList<>();

    public void addChild(CommentNode child) {
        this.children.add(child);
    }
}
```

카테고리 트리 흐름:

```text
Parent Category
→ Child Category
→ Child Category
→ Item
```

Composite는 다음 기능에 사용된다.

- 대댓글 구조
- 메뉴 트리
- 관리자 권한 트리
- 카테고리 구조
- 파일/폴더 구조
- 조직도

---

### [Best Practice]

- 트리 깊이를 제한할지 검토한다.
- 재귀 조회 시 성능을 고려한다.
- DB 저장 구조는 Adjacency List, Closure Table, Nested Set 중 선택한다.
- 응답 DTO는 Tree DTO로 변환한다.
- 무한 순환 참조를 방지한다.
- JSON 직렬화 시 Parent 참조 노출에 주의한다.

---

### [주의]

- Entity 양방향 연관관계로 트리를 만들면 순환 참조가 발생할 수 있다.
- 깊은 트리는 조회 성능 문제가 생길 수 있다.
- 재귀 로직은 Stack Overflow 가능성을 고려한다.
- 삭제 정책 Cascade를 신중히 설정한다.
- 단순 1단계 구조에는 Composite가 과할 수 있다.

---

### [FAQ]

Q. Composite Pattern은 무엇인가?

A. 객체를 트리 구조로 구성하여 개별 객체와 그룹 객체를 동일하게 다루는 Pattern이다.

Q. Composite Pattern은 언제 사용하는가?

A. 메뉴, 카테고리, 댓글, 조직도처럼 계층형 구조가 필요할 때 사용한다.

Q. Composite Pattern의 핵심은?

A. Leaf와 Composite를 동일한 Component Interface로 다루는 것이다.

Q. Composite Pattern의 주의점은?

A. 순환 참조, 재귀 성능, 깊은 트리, 삭제 정책을 주의해야 한다.

---

# 6. Structural Pattern Comparison

## 6.1 Adapter vs Decorator vs Proxy

### [개념]

Adapter, Decorator, Proxy는 모두 객체를 감싸는 Wrapper 구조로 보일 수 있지만 목적이 다르다.

- Adapter는 Interface 변환이 목적이다.
- Decorator는 기능 확장이 목적이다.
- Proxy는 접근 제어가 목적이다.

---

### [핵심]

| Pattern   | 핵심 목적               | 주요 문제                        | 실무 예                        |
| --------- | ----------------------- | -------------------------------- | ------------------------------ |
| Adapter   | Interface Compatibility | 외부 API와 내부 Interface 불일치 | External API Adapter           |
| Decorator | Dynamic Extension       | 기존 기능에 부가기능 추가        | Filter, Logging Wrapper        |
| Proxy     | Access Control          | 실제 객체 접근 제어              | AOP, Transaction, Lazy Loading |

---

### [Comparison]

```text
Adapter
→ 다른 Interface를 맞춘다

Decorator
→ 같은 Interface로 기능을 추가한다

Proxy
→ 같은 Interface로 접근을 제어한다
```

구분 질문:

| 질문                                            | Pattern   |
| ----------------------------------------------- | --------- |
| 인터페이스가 서로 맞지 않는가?                  | Adapter   |
| 기존 기능에 부가기능을 추가하는가?              | Decorator |
| 실제 객체 접근을 대신 제어하는가?               | Proxy     |
| 외부 API 응답을 내부 모델로 바꾸는가?           | Adapter   |
| 로깅, 캐싱, 검증을 감싸는가?                    | Decorator |
| Transaction, Security, Lazy Loading이 필요한가? | Proxy     |

---

### [실무]

예시 판단:

```text
Tour API 응답을 Festival DTO로 변환
→ Adapter
```

```text
MessageSender 실행 전후 Logging 추가
→ Decorator
```

```text
@Transactional Service 호출 전후 Transaction 처리
→ Proxy
```

---

### [주의]

- 세 Pattern은 모두 Wrapper처럼 보일 수 있다.
- 목적이 다르면 Pattern도 다르다.
- Adapter는 보통 다른 Interface를 제공한다.
- Decorator와 Proxy는 보통 같은 Interface를 유지한다.
- Proxy는 접근 시점을 제어하고 Decorator는 기능을 확장한다.

---

### [FAQ]

Q. Adapter, Decorator, Proxy의 가장 큰 차이는?

A. Adapter는 인터페이스 변환, Decorator는 기능 확장, Proxy는 접근 제어가 목적이다.

Q. 외부 API 연동에는 어떤 Pattern이 적합한가?

A. 내부 Interface와 외부 API 구조를 분리하기 위해 Adapter Pattern이 적합하다.

Q. Spring Transaction은 어떤 Pattern인가?

A. Proxy Pattern 기반으로 이해할 수 있다.

Q. Spring Security Filter Chain은 어떤 Pattern인가?

A. Decorator와 Chain of Responsibility 성격을 함께 가진다.

---

# 7. Troubleshooting

## 7.1 Wrong Adapter Design

### [개념]

Wrong Adapter Design은 Adapter가 외부 시스템을 내부에서 격리하지 못하거나 Adapter 책임을 넘어 비즈니스 로직까지 담당하는 문제이다.

---

### [핵심]

- Adapter는 외부 기술을 내부로부터 격리해야 한다.
- 외부 DTO가 내부 Service로 침투하면 Adapter 역할이 실패한 것이다.
- Adapter에 핵심 비즈니스 정책을 넣으면 SRP 위반이다.
- Port가 외부 API 스펙에 종속되면 DIP 효과가 약해진다.
- Adapter는 변환과 외부 호출 경계에 집중해야 한다.

---

### [Troubleshooting]

문제:

- Service가 외부 API Response DTO를 직접 사용한다.
- Adapter Interface 이름에 특정 Vendor가 강하게 드러난다.
- Adapter 내부에 주문 상태 결정, 할인 계산 같은 비즈니스 로직이 있다.
- 외부 API 변경 시 Application Service까지 수정된다.
- 테스트에서 외부 API를 쉽게 대체할 수 없다.

원인:

- Port를 내부 요구사항이 아니라 외부 API 기준으로 설계했다.
- Adapter와 Application Service 책임을 분리하지 않았다.
- 외부 DTO와 내부 DTO 변환 위치가 잘못되었다.
- DIP 방향을 지키지 않았다.

해결:

- Port를 Application이 필요한 기능 기준으로 다시 정의한다.
- 외부 DTO는 Adapter 내부에서 내부 Result 객체로 변환한다.
- 핵심 비즈니스 판단은 Application Service 또는 Domain Service로 이동한다.
- Adapter 구현체는 Infrastructure Layer로 분리한다.
- 테스트용 Fake Adapter를 작성한다.

---

### [FAQ]

Q. Wrong Adapter Design은 무엇인가?

A. Adapter가 외부 시스템을 내부로부터 격리하지 못하거나 비즈니스 책임까지 떠안는 잘못된 설계이다.

Q. 외부 API DTO가 Service에 들어오면 왜 문제인가?

A. 외부 응답 구조 변경이 내부 비즈니스 코드까지 전파되기 때문이다.

Q. Adapter에 비즈니스 로직을 넣어도 되는가?

A. 권장하지 않는다. Adapter는 외부 호출, 변환, 예외 변환에 집중해야 한다.

Q. Port는 어떻게 설계해야 하는가?

A. 외부 API 스펙이 아니라 Application이 필요로 하는 기능과 결과 기준으로 설계한다.

---

## 7.2 Proxy Misunderstanding

### [개념]

Proxy Misunderstanding은 Spring AOP, Transaction, Lazy Loading이 Proxy 기반으로 동작한다는 점을 이해하지 못해 발생하는 설계 및 런타임 문제이다.

---

### [핵심]

- Spring AOP는 Proxy를 통해 적용된다.
- Proxy를 거치지 않는 호출에는 AOP가 적용되지 않을 수 있다.
- `@Transactional`은 Proxy 기반으로 동작한다.
- JPA Lazy Loading은 Proxy 초기화 시점과 Transaction 범위에 영향을 받는다.
- Proxy 구조를 이해하지 못하면 운영 오류가 발생한다.

---

### [Troubleshooting]

문제:

- `@Transactional`이 적용되지 않는다.
- 같은 Class 내부 메서드 호출에서 Transaction이 동작하지 않는다.
- private method에 AOP가 적용되지 않는다.
- LazyInitializationException이 발생한다.
- AOP Logging이 특정 Method에서 누락된다.

원인:

- Self Invocation으로 Proxy를 거치지 않았다.
- Target 객체를 직접 생성했다.
- private/final method에 AOP를 기대했다.
- Transaction 밖에서 Lazy Proxy를 접근했다.
- Proxy Bean이 아닌 실제 객체를 사용했다.

해결:

- Transaction 대상 Method를 외부 Bean에서 호출되게 분리한다.
- `new`로 Service 객체를 직접 생성하지 않는다.
- AOP 대상 Method는 public으로 둔다.
- Lazy Field는 Transaction 안에서 조회하거나 DTO Projection을 사용한다.
- Fetch Join, EntityGraph로 필요한 데이터를 명시적으로 조회한다.

---

### [FAQ]

Q. Proxy Misunderstanding은 무엇인가?

A. Spring AOP, Transaction, JPA Lazy Loading의 Proxy 기반 동작을 이해하지 못해 발생하는 문제이다.

Q. Self Invocation에서 `@Transactional`이 안 되는 이유는?

A. 같은 객체 내부 호출은 Spring Proxy를 거치지 않기 때문이다.

Q. LazyInitializationException의 원인은?

A. Transaction 또는 영속성 Context 밖에서 Lazy Proxy를 초기화하려고 했기 때문이다.

Q. Proxy 문제를 줄이는 방법은?

A. Proxy를 거치는 호출 구조를 만들고, 필요한 조회는 Transaction 안에서 처리하거나 DTO Projection을 사용한다.

---

## 7.3 Decorator Overuse

### [개념]

Decorator Overuse는 부가기능 확장을 위해 Decorator를 과도하게 중첩하여 호출 흐름과 Bean 구조가 복잡해지는 문제이다.

---

### [핵심]

- Decorator는 기능 확장에 유용하지만 중첩이 많아지면 복잡하다.
- Decorator 순서가 결과에 영향을 줄 수 있다.
- 공통 관심사는 AOP 또는 Filter가 더 적합할 수 있다.
- Decorator는 특정 객체 기능 확장에 적합하다.
- Decorator가 핵심 비즈니스 로직을 가지면 책임이 흐려진다.

---

### [Troubleshooting]

문제:

- 하나의 기능 호출에 Decorator가 너무 많이 중첩된다.
- Bean 주입 구조가 복잡하고 순환 참조가 발생한다.
- 어떤 Decorator가 먼저 실행되는지 알기 어렵다.
- 단순 Logging을 위해 Wrapper Class가 과도하게 늘어난다.
- Decorator 안에 핵심 비즈니스 로직이 들어간다.

원인:

- 공통 관심사를 Decorator로만 해결하려 했다.
- Decorator 적용 순서를 관리하지 않았다.
- AOP, Filter, Interceptor 대안을 검토하지 않았다.
- 책임 분리가 명확하지 않았다.

해결:

- 전역 Logging, Metrics는 AOP를 검토한다.
- HTTP 요청 전후 처리는 Filter 또는 Interceptor를 검토한다.
- 특정 객체 기능 조합에만 Decorator를 사용한다.
- Decorator 순서를 명확히 문서화한다.
- 핵심 비즈니스 로직은 Target Service로 이동한다.

---

### [FAQ]

Q. Decorator Overuse는 무엇인가?

A. Decorator를 과도하게 중첩해 호출 흐름과 Bean 구조를 복잡하게 만드는 문제이다.

Q. Decorator 대신 AOP를 써야 하는 경우는?

A. 여러 Method에 반복되는 Logging, Transaction, Metrics 같은 공통 관심사는 AOP가 적합하다.

Q. Decorator 순서는 왜 중요한가?

A. 각 Decorator가 호출 전후에 기능을 추가하므로 실행 순서에 따라 결과가 달라질 수 있기 때문이다.

Q. Decorator에는 어떤 로직을 넣어야 하는가?

A. 핵심 비즈니스가 아니라 기존 기능 전후에 추가되는 부가기능을 넣어야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Structural Pattern이란?
A. 객체와 Class의 관계를 설계하여 유연한 구조를 만드는 Design Pattern이다.

Q. Structural Pattern은 언제 사용하는가?
A. 인터페이스 변환, 기능 확장, 접근 제어, 객체 관계 설계가 필요할 때 사용한다.

Q. Structural Pattern의 대표 패턴은?
A. Adapter, Decorator, Proxy가 대표적이다.

Q. Structural Pattern은 어떤 원칙과 관련 있는가?
A. SRP, OCP, DIP와 관련이 깊다.

Q. Adapter Pattern이란?
A. 호환되지 않는 인터페이스를 연결하기 위해 중간 변환 객체를 두는 Pattern이다.

Q. Adapter Pattern은 언제 사용하는가?
A. 외부 API, Legacy System, SDK를 내부 Interface에 맞게 변환해야 할 때 사용한다.

Q. Adapter는 어떤 문제를 해결하는가?
A. Interface Compatibility 문제와 외부 시스템 결합 문제를 해결한다.

Q. Adapter에는 어떤 책임을 넣는가?
A. 외부 호출, 응답 변환, 요청 변환, 예외 변환, 프로토콜 변환을 넣는다.

Q. Adapter에 비즈니스 로직을 넣어도 되는가?
A. 권장하지 않는다. 핵심 비즈니스 정책은 Application Service 또는 Domain Service에 둔다.

Q. Hexagonal Architecture에서 Adapter란?
A. Port와 외부 시스템을 연결하는 기술 구현 계층이다.

Q. Port와 Adapter의 차이는?
A. Port는 내부가 요구하는 Interface이고 Adapter는 외부 기술과 연결하는 구현체이다.

Q. External API Adapter란?
A. 외부 시스템을 내부 Application Interface에 맞게 변환하고 격리하는 Adapter이다.

Q. 외부 API DTO를 내부 Service에서 직접 사용하면 왜 문제인가?
A. 외부 응답 구조 변경이 내부 비즈니스 코드까지 전파되기 때문이다.

Q. Decorator Pattern이란?
A. 기존 객체를 감싸 기존 기능은 유지하면서 새로운 기능을 동적으로 추가하는 Pattern이다.

Q. Decorator Pattern은 언제 사용하는가?
A. 로깅, 캐싱, 검증, 보안, 메트릭 같은 부가기능을 기존 기능 전후에 추가할 때 사용한다.

Q. Decorator와 상속의 차이는?
A. 상속은 정적 확장이고 Decorator는 Composition을 통한 동적 확장이다.

Q. Spring Security Filter Chain은 Decorator Pattern인가?
A. 요청 처리를 감싸는 Decorator 성격과 순차 책임 전달 Chain of Responsibility 성격을 함께 가진다.

Q. JWT Filter의 핵심 책임은?
A. Token을 검증하고 Authentication을 만들어 SecurityContext에 저장하는 것이다.

Q. Decorator와 AOP의 차이는?
A. Decorator는 객체 조합으로 기능을 감싸고 AOP는 Proxy와 Advice로 공통 관심사를 분리한다.

Q. Logging은 Decorator와 AOP 중 무엇이 적합한가?
A. 전역 공통 Logging은 AOP가 적합하고 특정 객체 Logging은 Decorator가 적합하다.

Q. Proxy Pattern이란?
A. 실제 객체에 대한 접근을 대리 객체가 대신 제어하는 Pattern이다.

Q. Proxy Pattern은 언제 사용하는가?
A. 접근 제어, 지연 로딩, 캐싱, 로깅, 보안, 트랜잭션 같은 부가기능이 필요할 때 사용한다.

Q. Spring AOP는 Proxy Pattern인가?
A. Spring AOP는 Proxy 기반으로 동작하므로 Proxy Pattern의 실무 예로 볼 수 있다.

Q. Spring Transaction은 어떤 구조인가?
A. Transaction Proxy가 Service Method 호출 전후에 Transaction Begin, Commit, Rollback을 처리하는 구조이다.

Q. Self Invocation이란?
A. 같은 Class 내부에서 자기 자신의 메서드를 호출하는 것이다.

Q. Self Invocation에서 `@Transactional`이 안 되는 이유는?
A. 같은 객체 내부 호출은 Spring Proxy를 거치지 않기 때문이다.

Q. JPA Lazy Loading Proxy란?
A. 연관 Entity를 Proxy로 두고 실제 접근 시점에 DB에서 조회하는 지연 로딩 구조이다.

Q. LazyInitializationException은 왜 발생하는가?
A. Transaction 또는 영속성 Context가 닫힌 뒤 Lazy Proxy를 초기화하려고 할 때 발생한다.

Q. N+1 문제는 왜 발생하는가?
A. 목록 조회 후 각 Entity의 Lazy 연관 객체를 개별적으로 조회하면서 추가 SQL이 반복 실행되기 때문이다.

Q. N+1 문제 해결 방법은?
A. Fetch Join, EntityGraph, Batch Size, DTO Projection을 사용한다.

Q. Facade Pattern이란?
A. 복잡한 하위 시스템을 단순한 Interface로 감싸 Client가 쉽게 사용할 수 있게 하는 Pattern이다.

Q. Facade는 언제 사용하는가?
A. 여러 Service나 외부 시스템 호출을 하나의 단순한 흐름으로 제공해야 할 때 사용한다.

Q. Composite Pattern이란?
A. 객체를 트리 구조로 구성하여 개별 객체와 그룹 객체를 동일하게 다루는 Pattern이다.

Q. Composite Pattern은 언제 사용하는가?
A. 메뉴, 카테고리, 댓글, 조직도처럼 계층형 구조가 필요할 때 사용한다.

Q. Adapter, Decorator, Proxy의 차이는?
A. Adapter는 인터페이스 변환, Decorator는 기능 확장, Proxy는 접근 제어가 목적이다.

Q. 외부 API 연동에는 어떤 Pattern이 적합한가?
A. 내부 Interface와 외부 API 구조를 분리하기 위해 Adapter Pattern이 적합하다.

Q. Spring Transaction은 어떤 Pattern으로 이해할 수 있는가?
A. Proxy Pattern으로 이해할 수 있다.

Q. Spring Security Filter Chain은 어떤 Pattern으로 이해할 수 있는가?
A. Decorator와 Chain of Responsibility 성격을 함께 가진다.

Q. Wrong Adapter Design이란?
A. Adapter가 외부 시스템을 내부로부터 격리하지 못하거나 비즈니스 책임까지 떠안는 잘못된 설계이다.

Q. Proxy Misunderstanding이란?
A. Spring AOP, Transaction, JPA Lazy Loading의 Proxy 기반 동작을 이해하지 못해 발생하는 문제이다.

Q. Decorator Overuse란?
A. Decorator를 과도하게 중첩해 호출 흐름과 Bean 구조를 복잡하게 만드는 문제이다.

Q. Backend Agent는 Structural Pattern을 어떻게 사용해야 하는가?
A. 외부 API 연동, 기능 확장, 접근 제어 문제를 구분하고 Adapter, Decorator, Proxy 구조를 선택해야 한다.

Q. Review Agent는 Structural Pattern을 어떻게 검수해야 하는가?
A. 외부 DTO 침투, Proxy 동작 오류, Decorator 과도화, 객체 결합도를 검수해야 한다.

Q. PM Agent는 Structural Pattern 요구사항을 어떻게 분류해야 하는가?
A. 인터페이스 불일치, 기능 확장, 접근 제어, 계층 구조, 복잡한 하위 시스템 단순화 요구로 분류해야 한다.
