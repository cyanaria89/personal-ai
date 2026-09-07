# Design Pattern Part02 - Creational Patterns

---

# 1. Creational Pattern Overview

## 1.1 Creational Pattern

### [개념]

Creational Pattern은 객체 생성 책임을 분리하고 객체 생성 과정을 캡슐화하는 Design Pattern이다.

Creational Pattern은 `new` 키워드 사용 자체를 금지하는 것이 아니다.

Creational Pattern은 객체 생성 로직이 복잡하거나 변경 가능성이 높을 때 생성 책임을 별도 구조로 분리한다.

```text
Client
→ Creation Abstraction
→ Object Creation
→ Created Object
```

---

### [핵심]

- Creational Pattern은 객체 생성 문제를 해결한다.
- Creational Pattern은 생성 책임을 Client 코드에서 분리한다.
- Creational Pattern은 객체 생성 조건, 생성 순서, 생성 복잡도를 캡슐화한다.
- Creational Pattern은 Factory, Singleton, Builder가 핵심이다.
- Creational Pattern은 OCP, SRP, DIP와 관련이 깊다.
- Creational Pattern은 과도하게 적용하면 불필요한 추상화가 된다.

---

### [실무]

2026 실무 기준 Java 21, Spring Boot 3.x Backend에서는 객체 생성 대부분을 Spring Container가 담당한다.

하지만 다음 상황에서는 Creational Pattern을 직접 검토한다.

- 생성 조건이 복잡한 객체
- 생성자 파라미터가 많은 DTO
- 요청 타입에 따라 구현체가 달라지는 객체
- 외부 API 요청 객체 생성
- 테스트용 Fake 객체 생성
- Domain 객체 생성 규칙 보호
- Strategy 구현체 선택
- Adapter 구현체 선택

Spring 환경에서는 다음 방식이 자주 사용된다.

- Spring Bean 등록
- Constructor Injection
- Factory Component
- Static Factory Method
- Lombok `@Builder`
- Java Record DTO
- Enum-based Factory
- Map 기반 Strategy Factory

---

### [주의]

- 단순 DTO 생성에 Factory를 과도하게 만들 필요는 없다.
- Spring Bean은 기본적으로 Singleton Scope이므로 Singleton Pattern 직접 구현이 불필요한 경우가 많다.
- Builder는 필드가 적은 객체에는 과할 수 있다.
- Factory는 객체 생성 책임이 실제로 복잡할 때 사용한다.
- 객체 생성과 비즈니스 로직을 Factory에 섞으면 Factory가 비대해진다.

---

### [FAQ]

Q. Creational Pattern은 무엇인가?

A. 객체 생성 책임과 생성 과정을 분리하고 캡슐화하는 Design Pattern이다.

Q. Creational Pattern은 `new`를 없애기 위한 패턴인가?

A. 아니다. 핵심은 `new` 제거가 아니라 생성 책임과 생성 복잡도 분리이다.

Q. Spring Boot에서도 Creational Pattern이 필요한가?

A. 필요할 수 있다. Spring Bean 생성은 Container가 담당하지만 조건별 객체 생성과 복잡한 생성 규칙은 별도 Pattern이 유용하다.

Q. Creational Pattern의 대표 패턴은?

A. Singleton, Factory, Builder가 대표적이다.

---

# 2. Singleton Pattern

## 2.1 Singleton

### [개념]

Singleton Pattern은 애플리케이션에서 특정 Class의 인스턴스를 하나만 생성하고 전역적으로 접근할 수 있도록 제한하는 Creational Pattern이다.

Singleton은 “Single Instance”를 보장하기 위한 패턴이다.

```text
Application
→ Singleton Access
→ Same Instance
```

---

### [핵심]

- Singleton은 하나의 인스턴스만 유지한다.
- Singleton은 상태 공유가 필요한 객체에 사용할 수 있다.
- Singleton은 객체 생성 비용이 크거나 전역 설정 객체에 사용할 수 있다.
- Spring Bean은 기본 Scope이 Singleton이다.
- Spring Singleton은 Container 단위 Singleton이다.
- Singleton은 상태를 가지면 동시성 문제가 발생할 수 있다.

---

### [실무]

Spring Boot 3.x에서는 직접 Singleton Pattern을 구현하기보다 Spring Bean Singleton Scope을 사용하는 것이 일반적이다.

```java
@Service
public class OrderService {
    public void order() {
        // order process
    }
}
```

Spring Container는 기본적으로 `OrderService` Bean을 하나만 생성하고 재사용한다.

```text
Spring Container
→ Create OrderService Bean Once
→ Inject Same Bean
→ Reuse
```

Singleton Bean은 무상태 Stateless로 설계하는 것이 안전하다.

좋은 예:

```java
@Service
public class DiscountService {
    public int discount(int price, int discountAmount) {
        return price - discountAmount;
    }
}
```

위 객체는 요청별 상태를 필드에 저장하지 않으므로 Singleton Bean으로 안전하다.

---

### [예제]

직접 구현 예시는 다음과 같다.

```java
public class AppConfig {
    private static final AppConfig INSTANCE = new AppConfig();

    private AppConfig() {
    }

    public static AppConfig getInstance() {
        return INSTANCE;
    }
}
```

하지만 Spring Boot 애플리케이션에서는 대부분 다음 방식이 더 적절하다.

```java
@Configuration
public class PaymentConfig {
}
```

```java
@Component
public class PaymentClient {
}
```

---

### [주의]

- Singleton 객체에 요청별 상태를 저장하면 위험하다.
- Singleton은 전역 상태를 만들 수 있다.
- Singleton은 테스트 격리를 어렵게 만들 수 있다.
- 직접 구현한 Singleton은 DI, Mocking, Lifecycle 관리가 어렵다.
- Spring에서는 직접 Singleton 구현보다 Bean Scope을 우선 사용한다.

---

### [FAQ]

Q. Singleton Pattern은 무엇인가?

A. 특정 Class의 인스턴스를 하나만 생성하고 재사용하도록 제한하는 Creational Pattern이다.

Q. Spring Bean은 Singleton인가?

A. 기본 Scope 기준으로 Spring Bean은 Singleton이다. 단, JVM 전체가 아니라 Spring Container 단위 Singleton이다.

Q. Spring Boot에서 Singleton Pattern을 직접 구현해야 하는가?

A. 대부분 필요 없다. Spring Bean으로 등록하면 Container가 Singleton처럼 관리한다.

Q. Singleton의 가장 큰 위험은?

A. 공유 상태로 인한 동시성 문제와 테스트 어려움이다.

---

## 2.2 Singleton and Stateless Design

### [개념]

Stateless Design은 Singleton Bean이 요청별 상태를 내부 필드에 저장하지 않도록 설계하는 방식이다.

Singleton Bean은 여러 요청에서 동시에 사용될 수 있으므로 상태를 필드에 저장하면 안 된다.

```text
Multiple Requests
→ Same Singleton Bean
→ Shared Field Risk
```

---

### [핵심]

- Singleton Bean은 여러 Thread가 공유할 수 있다.
- 요청별 데이터는 Method Parameter, Local Variable, DTO로 처리한다.
- Singleton Bean 필드에는 불변 의존성만 두는 것이 안전하다.
- Mutable Field는 동시성 문제를 만들 수 있다.
- Stateless Service는 테스트와 운영 안정성이 좋다.

---

### [실무]

나쁜 예:

```java
@Service
public class OrderService {
    private Long currentUserId;

    public void order(Long userId) {
        this.currentUserId = userId;
        process();
    }

    private void process() {
        // currentUserId 사용
    }
}
```

문제:

- `currentUserId`가 여러 요청에서 공유된다.
- 동시에 요청이 들어오면 다른 사용자의 값으로 덮어쓰기 될 수 있다.

좋은 예:

```java
@Service
public class OrderService {
    public void order(Long userId) {
        process(userId);
    }

    private void process(Long userId) {
        // userId 사용
    }
}
```

---

### [Best Practice]

- Service Field에는 Repository, Client, Policy 등 의존성만 둔다.
- 요청별 값은 Local Variable로 유지한다.
- 상태가 필요한 경우 DB, Cache, Session, Request Scope을 검토한다.
- 공유 상태가 필요하면 Thread Safety를 반드시 검토한다.
- Singleton Bean은 기본적으로 Stateless로 설계한다.

---

### [주의]

- `static` 필드에 요청별 상태를 저장하면 더 위험하다.
- Singleton Bean에서 `List`, `Map` 등 Mutable Collection을 공유할 때 주의한다.
- Cache 용도 상태는 Concurrent Collection, TTL, 동시성 제어를 고려한다.
- EntityManager, Transaction, SecurityContext는 Spring이 Context 단위로 관리한다.

---

### [FAQ]

Q. Singleton Bean은 왜 Stateless로 만들어야 하는가?

A. 여러 요청이 같은 Bean 인스턴스를 공유하므로 요청별 상태가 섞일 수 있기 때문이다.

Q. Singleton Bean 필드에는 무엇을 둬도 되는가?

A. 주입받은 의존성, 불변 설정값, Thread-safe 객체는 가능하다.

Q. 요청별 데이터는 어디에 저장해야 하는가?

A. Method Parameter, Local Variable, DTO, Request Scope, DB, Cache 등을 사용한다.

Q. Singleton과 동시성 문제는 어떤 관계인가?

A. Singleton 객체의 Mutable Field를 여러 Thread가 동시에 접근하면 데이터 오염이 발생할 수 있다.

---

# 3. Factory Pattern

## 3.1 Factory Pattern

### [개념]

Factory Pattern은 객체 생성 책임을 Client 코드에서 분리하여 Factory 객체 또는 Factory Method가 담당하도록 만드는 Creational Pattern이다.

Factory는 Object Creation Delegation 구조이다.

```text
Request
→ Factory
→ Concrete Object
```

---

### [핵심]

- Factory는 생성 책임을 분리한다.
- Factory는 조건에 따라 적절한 객체를 생성하거나 선택한다.
- Factory는 Client가 Concrete Class를 직접 알지 않게 만든다.
- Factory는 OCP, SRP, DIP와 관련이 깊다.
- Factory는 Strategy 선택과 함께 자주 사용된다.
- Factory는 생성 조건이 복잡할수록 유용하다.

---

### [실무]

Factory Pattern은 다음 상황에서 자주 사용한다.

- 결제 타입별 PaymentProcessor 선택
- 알림 타입별 NotificationSender 선택
- 파일 타입별 FileParser 선택
- 외부 API Provider별 Adapter 선택
- 사용자 Role별 Policy 선택
- 요청 Command별 Handler 선택

나쁜 예:

```java
@Service
public class PaymentService {
    public void pay(String type, PaymentRequest request) {
        if (type.equals("CARD")) {
            new CardPaymentProcessor().pay(request);
        }

        if (type.equals("TOSS")) {
            new TossPaymentProcessor().pay(request);
        }
    }
}
```

문제:

- PaymentService가 Concrete Class를 직접 생성한다.
- 결제 수단 추가 시 PaymentService 수정이 필요하다.
- 테스트와 확장이 어렵다.

좋은 방향:

```text
PaymentService
→ PaymentProcessorFactory
→ PaymentProcessor
→ CardPaymentProcessor / TossPaymentProcessor
```

---

### [예제]

```java
public interface PaymentProcessor {
    boolean supports(PaymentType paymentType);
    void pay(PaymentRequest request);
}
```

```java
@Component
public class CardPaymentProcessor implements PaymentProcessor {
    @Override
    public boolean supports(PaymentType paymentType) {
        return paymentType == PaymentType.CARD;
    }

    @Override
    public void pay(PaymentRequest request) {
        // card payment
    }
}
```

```java
@Component
public class TossPaymentProcessor implements PaymentProcessor {
    @Override
    public boolean supports(PaymentType paymentType) {
        return paymentType == PaymentType.TOSS;
    }

    @Override
    public void pay(PaymentRequest request) {
        // toss payment
    }
}
```

```java
@Component
public class PaymentProcessorFactory {
    private final List<PaymentProcessor> processors;

    public PaymentProcessorFactory(List<PaymentProcessor> processors) {
        this.processors = processors;
    }

    public PaymentProcessor getProcessor(PaymentType paymentType) {
        return processors.stream()
                .filter(processor -> processor.supports(paymentType))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("지원하지 않는 결제 타입입니다."));
    }
}
```

```java
@Service
public class PaymentService {
    private final PaymentProcessorFactory paymentProcessorFactory;

    public PaymentService(PaymentProcessorFactory paymentProcessorFactory) {
        this.paymentProcessorFactory = paymentProcessorFactory;
    }

    public void pay(PaymentType paymentType, PaymentRequest request) {
        PaymentProcessor processor = paymentProcessorFactory.getProcessor(paymentType);
        processor.pay(request);
    }
}
```

---

### [Best Practice]

- Factory는 객체 생성 또는 객체 선택 책임만 가진다.
- Factory 내부에 복잡한 비즈니스 로직을 넣지 않는다.
- Spring에서는 구현체 List Injection을 활용할 수 있다.
- 타입 선택 기준은 Enum, Key, Provider Name 등 명확한 값으로 관리한다.
- 지원하지 않는 타입은 명확한 예외로 처리한다.
- Factory와 Strategy를 함께 사용하면 조건문 증가를 줄일 수 있다.

---

### [주의]

- 단순한 객체 생성에는 Factory가 불필요할 수 있다.
- Factory가 모든 객체를 생성하는 God Factory가 되면 안 된다.
- Factory가 비즈니스 정책까지 판단하면 책임이 커진다.
- Factory 내부 if / switch가 계속 증가하면 Map 기반 구조를 검토한다.
- Factory 적용 후 추적이 더 어려워졌다면 단순화가 필요하다.

---

### [FAQ]

Q. Factory Pattern은 무엇인가?

A. 객체 생성 책임을 Client에서 분리하여 Factory가 담당하도록 만드는 Creational Pattern이다.

Q. Factory Pattern은 언제 사용하는가?

A. 생성 조건이 복잡하거나 요청 타입에 따라 다른 객체를 선택해야 할 때 사용한다.

Q. Factory와 Strategy는 어떤 관계인가?

A. Strategy는 알고리즘 교체 구조이고 Factory는 적절한 Strategy 구현체를 선택하는 역할로 함께 사용될 수 있다.

Q. Factory는 객체를 항상 새로 생성해야 하는가?

A. 아니다. Spring Bean처럼 이미 생성된 객체를 선택해서 반환할 수도 있다.

---

## 3.2 Static Factory Method

### [개념]

Static Factory Method는 생성자 대신 의미 있는 이름의 static method로 객체를 생성하는 방식이다.

Static Factory Method는 GoF Factory Pattern과 다르지만 객체 생성 의도를 명확히 표현하는 데 유용하다.

```text
Client
→ Class.staticFactoryMethod()
→ New Object
```

---

### [핵심]

- Static Factory Method는 생성자보다 의미 있는 이름을 제공한다.
- 생성 로직을 메서드 내부에 캡슐화할 수 있다.
- 반환 타입을 유연하게 설계할 수 있다.
- DTO, Value Object, Domain Object 생성에 자주 사용된다.
- 복잡한 의존성 주입이 필요한 객체에는 적합하지 않을 수 있다.

---

### [실무]

나쁜 예:

```java
UserResponse response = new UserResponse(user.getId(), user.getEmail(), user.getNickname());
```

좋은 예:

```java
UserResponse response = UserResponse.from(user);
```

```java
public record UserResponse(
        Long userId,
        String email,
        String nickname
) {
    public static UserResponse from(User user) {
        return new UserResponse(
                user.getUserId(),
                user.getEmail(),
                user.getNickname()
        );
    }
}
```

Static Factory Method 이름 예:

| Method Name      | 의미                        |
| ---------------- | --------------------------- |
| `from()`         | 하나의 객체를 변환하여 생성 |
| `of()`           | 여러 값을 받아 생성         |
| `create()`       | 일반 생성                   |
| `ofNullable()`   | null 허용 생성              |
| `empty()`        | 빈 객체 생성                |
| `defaultValue()` | 기본값 객체 생성            |

---

### [예제]

Domain Event 생성:

```java
public record OrderCreatedEvent(
        Long orderId,
        Long userId
) {
    public static OrderCreatedEvent of(Order order) {
        return new OrderCreatedEvent(
                order.getOrderId(),
                order.getUserId()
        );
    }
}
```

Value Object 생성:

```java
public class Money {
    private final int amount;

    private Money(int amount) {
        if (amount < 0) {
            throw new IllegalArgumentException("금액은 음수일 수 없습니다.");
        }

        this.amount = amount;
    }

    public static Money of(int amount) {
        return new Money(amount);
    }
}
```

---

### [주의]

- Static Factory Method가 복잡해지면 별도 Factory Class를 검토한다.
- 외부 의존성이 필요한 생성은 Spring Bean Factory가 더 적합하다.
- Static Method는 Mocking과 확장성 측면에서 제약이 있을 수 있다.
- 단순 생성자보다 과하게 감싸면 코드가 장황해질 수 있다.

---

### [FAQ]

Q. Static Factory Method는 무엇인가?

A. 생성자 대신 의미 있는 이름의 static method로 객체를 생성하는 방식이다.

Q. Static Factory Method와 Factory Pattern은 같은가?

A. 아니다. Static Factory Method는 생성 메서드 기법이고, Factory Pattern은 생성 책임을 별도 객체나 구조로 분리하는 패턴이다.

Q. DTO 변환에는 어떤 이름을 쓰는가?

A. 보통 Entity에서 DTO로 변환할 때 `from()`을 많이 사용한다.

Q. Static Factory Method는 언제 피해야 하는가?

A. 외부 의존성 주입이 필요하거나 생성 로직이 매우 복잡하면 별도 Factory Bean을 사용하는 것이 좋다.

---

## 3.3 Enum Factory

### [개념]

Enum Factory는 Enum 값과 생성 대상 또는 Strategy 구현체를 연결하여 객체 선택 로직을 단순화하는 Factory 방식이다.

Enum Factory는 타입 안정성과 명확한 분기 기준을 제공한다.

```text
Enum Type
→ Factory Mapping
→ Concrete Object
```

---

### [핵심]

- Enum Factory는 문자열 분기보다 안전하다.
- 지원 타입을 Enum으로 제한할 수 있다.
- 조건문 분기 오류를 줄일 수 있다.
- PaymentType, NotificationType, FileType 등에 적합하다.
- 구현체가 많아지면 Map 기반 Factory가 더 적합할 수 있다.

---

### [실무]

Enum 타입 정의:

```java
public enum NotificationType {
    EMAIL,
    SMS,
    PUSH
}
```

Factory에서 Enum으로 구현체 선택:

```java
@Component
public class NotificationSenderFactory {
    private final List<NotificationSender> senders;

    public NotificationSenderFactory(List<NotificationSender> senders) {
        this.senders = senders;
    }

    public NotificationSender getSender(NotificationType notificationType) {
        return senders.stream()
                .filter(sender -> sender.supports(notificationType))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("지원하지 않는 알림 타입입니다."));
    }
}
```

구현체:

```java
public interface NotificationSender {
    boolean supports(NotificationType notificationType);
    void send(NotificationRequest request);
}
```

---

### [Best Practice]

- 외부 요청 문자열은 Controller 또는 Request DTO에서 Enum으로 변환한다.
- Factory 내부는 String보다 Enum을 기준으로 판단한다.
- 지원하지 않는 Enum 값은 명확한 예외로 처리한다.
- Enum에 과도한 비즈니스 로직을 넣지 않는다.
- 복잡한 정책은 Enum이 아니라 Strategy 구현체로 분리한다.

---

### [주의]

- Enum이 너무 많은 책임을 가지면 유지보수가 어려워진다.
- Enum에 외부 의존성이 필요한 로직을 넣으면 안 된다.
- Enum 변경은 전역 영향이 있을 수 있다.
- 문자열과 Enum 변환 시 대소문자, 잘못된 값 처리를 명확히 해야 한다.

---

### [FAQ]

Q. Enum Factory는 무엇인가?

A. Enum 값을 기준으로 적절한 객체나 Strategy 구현체를 선택하는 Factory 방식이다.

Q. Factory에서 String보다 Enum이 좋은 이유는?

A. 타입 안정성이 높고 오타로 인한 분기 오류를 줄일 수 있기 때문이다.

Q. Enum에 비즈니스 로직을 넣어도 되는가?

A. 단순한 값 기반 판단은 가능하지만 복잡한 정책이나 외부 의존 로직은 Strategy로 분리하는 것이 좋다.

Q. Enum Factory는 어떤 상황에 적합한가?

A. 결제 타입, 알림 타입, 파일 타입처럼 선택 기준이 명확한 경우에 적합하다.

---

## 3.4 Map-Based Factory

### [개념]

Map-Based Factory는 Key와 구현체를 Map으로 매핑하여 조건문 없이 적절한 객체를 선택하는 Factory 방식이다.

구현체가 많거나 선택 로직이 자주 확장될 때 유용하다.

```text
Key
→ Map<Key, Implementation>
→ Selected Implementation
```

---

### [핵심]

- Map-Based Factory는 if / switch 증가를 줄인다.
- 구현체 검색 성능이 단순하다.
- Key 기반 Strategy 선택에 적합하다.
- Spring Bean 이름 또는 지원 Key를 활용할 수 있다.
- 초기화 시 중복 Key 검증이 중요하다.

---

### [실무]

```java
public interface PaymentProcessor {
    PaymentType getPaymentType();
    void pay(PaymentRequest request);
}
```

```java
@Component
public class PaymentProcessorFactory {
    private final Map<PaymentType, PaymentProcessor> processorMap;

    public PaymentProcessorFactory(List<PaymentProcessor> processors) {
        this.processorMap = processors.stream()
                .collect(Collectors.toMap(
                        PaymentProcessor::getPaymentType,
                        Function.identity()
                ));
    }

    public PaymentProcessor getProcessor(PaymentType paymentType) {
        PaymentProcessor processor = processorMap.get(paymentType);

        if (processor == null) {
            throw new IllegalArgumentException("지원하지 않는 결제 타입입니다.");
        }

        return processor;
    }
}
```

---

### [Best Practice]

- Key는 String보다 Enum 사용을 우선 검토한다.
- Factory 생성 시 중복 Key를 검증한다.
- 지원하지 않는 Key는 명확한 예외로 처리한다.
- 구현체 추가 시 Factory 수정 없이 Bean 추가만으로 확장되게 설계한다.
- Map은 외부에서 수정되지 않도록 불변 구조로 보관한다.

---

### [주의]

- Key 충돌이 발생하면 애플리케이션 시작 시 실패하도록 처리하는 것이 좋다.
- Map 초기화 로직이 복잡해지면 별도 Config를 검토한다.
- 구현체가 적으면 List Stream 방식도 충분하다.
- 런타임 동적 등록이 필요한 경우 동시성 제어를 고려한다.

---

### [FAQ]

Q. Map-Based Factory는 무엇인가?

A. Key와 구현체를 Map으로 매핑하여 조건문 없이 객체를 선택하는 Factory 방식이다.

Q. Map-Based Factory는 언제 좋은가?

A. 구현체가 많고 선택 로직이 자주 확장될 때 좋다.

Q. Map-Based Factory의 장점은?

A. if / switch 증가를 줄이고 구현체 추가 시 기존 Factory 수정을 최소화할 수 있다.

Q. Map-Based Factory에서 주의할 점은?

A. Key 중복, 미지원 Key, Map 변경 가능성을 관리해야 한다.

---

# 4. Builder Pattern

## 4.1 Builder Pattern

### [개념]

Builder Pattern은 복잡한 객체 생성을 단계적으로 구성하고 최종적으로 객체를 생성하는 Creational Pattern이다.

Builder는 생성자 파라미터가 많거나 선택 필드가 많은 객체 생성 문제를 해결한다.

```text
Builder
→ Set Required Fields
→ Set Optional Fields
→ Build Object
```

---

### [핵심]

- Builder는 복잡한 객체 생성을 단순화한다.
- Builder는 생성자 폭발 문제를 해결한다.
- Builder는 선택 필드가 많은 객체에 유용하다.
- Builder는 가독성 높은 객체 생성을 돕는다.
- Builder는 불변 객체 생성과 잘 어울린다.
- Builder는 필수값 검증을 함께 고려해야 한다.

---

### [실무]

나쁜 예:

```java
User user = new User("test@email.com", "nickname", "ROLE_USER", true, null, null);
```

문제:

- 파라미터 의미를 알기 어렵다.
- 순서가 바뀌면 오류가 발생한다.
- 선택 필드가 많아질수록 생성자가 복잡해진다.

좋은 예:

```java
User user = User.builder()
        .email("test@email.com")
        .nickname("nickname")
        .role(Role.ROLE_USER)
        .active(true)
        .build();
```

---

### [예제]

Lombok Builder 예:

```java
@Getter
@Builder
public class UserCreateRequest {
    private final String email;
    private final String nickname;
    private final String password;
}
```

Domain 객체 Builder 예:

```java
@Getter
public class Order {
    private final Long userId;
    private final int totalPrice;
    private final OrderStatus status;

    @Builder
    private Order(Long userId, int totalPrice, OrderStatus status) {
        if (userId == null) {
            throw new IllegalArgumentException("userId는 필수입니다.");
        }

        if (totalPrice < 0) {
            throw new IllegalArgumentException("totalPrice는 음수일 수 없습니다.");
        }

        this.userId = userId;
        this.totalPrice = totalPrice;
        this.status = status == null ? OrderStatus.CREATED : status;
    }
}
```

---

### [Best Practice]

- 필드가 많고 선택값이 많은 DTO에 Builder를 사용한다.
- Domain 객체는 Builder 내부 또는 생성자에서 필수값 검증을 수행한다.
- 불변 객체와 Builder를 함께 사용하면 안전하다.
- 테스트 데이터 생성에는 Builder가 편리하다.
- Entity Builder 사용 시 연관관계와 필수값을 주의한다.

---

### [주의]

- 필드가 1~2개인 객체에 Builder는 과할 수 있다.
- Builder는 필수값 누락을 컴파일 타임에 막기 어렵다.
- JPA Entity에 `@Builder`를 무분별하게 사용하면 불완전한 Entity가 생성될 수 있다.
- Builder로 생성해도 Domain Invariant 검증은 필요하다.
- Lombok `@Builder`는 편하지만 생성 규칙이 숨겨질 수 있다.

---

### [FAQ]

Q. Builder Pattern은 무엇인가?

A. 복잡한 객체 생성을 단계적으로 구성하고 최종 객체를 생성하는 Creational Pattern이다.

Q. Builder는 언제 사용하는가?

A. 생성자 파라미터가 많거나 선택 필드가 많아 생성자 가독성이 떨어질 때 사용한다.

Q. Builder는 생성자 폭발을 어떻게 해결하는가?

A. 여러 생성자를 만들지 않고 필요한 필드를 이름 기반으로 설정해 객체를 생성한다.

Q. Builder의 단점은?

A. 필수값 누락을 놓칠 수 있고 단순 객체에는 구조가 과할 수 있다.

---

## 4.2 Lombok Builder

### [개념]

Lombok `@Builder`는 Builder Pattern 코드를 자동 생성해주는 Lombok 기능이다.

Java Backend에서 DTO, Command, Response, Test Fixture 생성에 자주 사용된다.

```text
@Builder
→ Generated Builder Class
→ Object Creation
```

---

### [핵심]

- Lombok `@Builder`는 반복 코드를 줄인다.
- DTO 생성 가독성을 높인다.
- 테스트 데이터 생성에 편리하다.
- 생성자 접근 제어와 함께 사용하면 안전하다.
- Entity에는 신중하게 적용해야 한다.
- 필수값 검증은 별도로 처리해야 한다.

---

### [실무]

DTO Builder 예:

```java
@Getter
@Builder
public class FestivalResponse {
    private Long festivalId;
    private String title;
    private String address;
    private String imageUrl;
}
```

사용 예:

```java
FestivalResponse response = FestivalResponse.builder()
        .festivalId(festival.getFestivalId())
        .title(festival.getTitle())
        .address(festival.getAddress())
        .imageUrl(festival.getImageUrl())
        .build();
```

JPA Entity에서는 다음처럼 생성자에 Builder를 붙이는 방식이 더 안전하다.

```java
@Entity
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Festival {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long festivalId;

    private String title;

    private LocalDate eventStartDate;

    @Builder
    private Festival(String title, LocalDate eventStartDate) {
        if (title == null || title.isBlank()) {
            throw new IllegalArgumentException("title은 필수입니다.");
        }

        this.title = title;
        this.eventStartDate = eventStartDate;
    }
}
```

---

### [Best Practice]

- DTO에는 Class Level `@Builder`를 사용할 수 있다.
- Entity에는 Constructor Level `@Builder`를 우선 검토한다.
- `@NoArgsConstructor(access = AccessLevel.PROTECTED)`로 JPA 기본 생성자를 보호한다.
- 필수값과 Domain Rule은 생성자 내부에서 검증한다.
- 테스트 Fixture 전용 Builder는 별도 Fixture Class로 분리할 수 있다.

---

### [주의]

- Entity 전체에 `@Builder`를 붙이면 모든 필드를 외부에서 설정할 수 있다.
- 연관관계 필드를 Builder로 무분별하게 열면 객체 무결성이 깨질 수 있다.
- `@Builder.Default`를 모르면 기본값이 무시될 수 있다.
- Builder는 Setter 대체 수단이 아니며 생성 시점 전용으로 사용하는 것이 좋다.

---

### [FAQ]

Q. Lombok `@Builder`는 무엇인가?

A. Builder Pattern 구현 코드를 자동으로 생성해주는 Lombok 기능이다.

Q. Entity에 `@Builder`를 붙여도 되는가?

A. 가능하지만 Class Level보다 생성자에 붙이고 필수값 검증을 함께 처리하는 것이 안전하다.

Q. `@Builder.Default`는 언제 필요한가?

A. Builder 사용 시 필드 기본값을 유지해야 할 때 필요하다.

Q. Builder는 Setter를 대체할 수 있는가?

A. 생성 시점에는 대체할 수 있지만 객체 상태 변경 메서드를 대체하는 용도는 아니다.

---

## 4.3 Builder and Immutable Object

### [개념]

Immutable Object는 생성 후 상태가 변경되지 않는 객체이다.

Builder는 Immutable Object를 읽기 쉽고 안전하게 생성하는 데 유용하다.

```text
Builder
→ Constructor
→ Final Fields
→ Immutable Object
```

---

### [핵심]

- Immutable Object는 생성 후 상태 변경이 없다.
- Immutable Object는 Thread Safety에 유리하다.
- Builder는 많은 필드를 가진 Immutable Object 생성에 유용하다.
- DTO, Value Object, Command 객체에 적합하다.
- Entity는 JPA 특성상 완전한 Immutable 설계가 어렵다.

---

### [실무]

```java
@Getter
public class PaymentCommand {
    private final Long userId;
    private final int amount;
    private final PaymentType paymentType;

    @Builder
    private PaymentCommand(Long userId, int amount, PaymentType paymentType) {
        if (userId == null) {
            throw new IllegalArgumentException("userId는 필수입니다.");
        }

        if (amount <= 0) {
            throw new IllegalArgumentException("amount는 0보다 커야 합니다.");
        }

        this.userId = userId;
        this.amount = amount;
        this.paymentType = paymentType;
    }
}
```

사용 예:

```java
PaymentCommand command = PaymentCommand.builder()
        .userId(1L)
        .amount(10000)
        .paymentType(PaymentType.CARD)
        .build();
```

---

### [Best Practice]

- Command 객체는 Immutable로 만든다.
- DTO는 Java Record를 우선 검토한다.
- Value Object는 필드를 `final`로 유지한다.
- Collection 필드는 방어적 복사 또는 불변 Collection으로 처리한다.
- 생성 시점에 유효성 검증을 수행한다.

---

### [주의]

- JPA Entity는 Proxy, 기본 생성자, Dirty Checking 때문에 완전한 Immutable과 충돌할 수 있다.
- Mutable Collection을 그대로 노출하면 Immutable이 깨진다.
- Builder로 객체를 만들더라도 내부 필드가 Mutable이면 주의가 필요하다.
- 불변 객체는 상태 변경 대신 새 객체 생성 방식이 필요하다.

---

### [FAQ]

Q. Immutable Object는 무엇인가?

A. 생성 후 내부 상태가 변경되지 않는 객체이다.

Q. Builder와 Immutable Object는 왜 잘 어울리는가?

A. 복잡한 생성 과정을 읽기 쉽게 만들면서 생성 후 상태 변경을 막을 수 있기 때문이다.

Q. DTO는 Immutable로 만드는 것이 좋은가?

A. 가능하면 좋다. Java Record 또는 final field 기반 DTO가 안전하다.

Q. JPA Entity도 Immutable로 만들 수 있는가?

A. 일부 제한적으로 가능하지만 JPA 특성상 완전한 Immutable 설계는 어렵다.

---

# 5. Creational Pattern Comparison

## 5.1 Singleton vs Factory vs Builder

### [개념]

Singleton, Factory, Builder는 모두 Creational Pattern이지만 해결하는 문제가 다르다.

- Singleton은 인스턴스 개수 제어 문제를 해결한다.
- Factory는 객체 생성 책임 분리 문제를 해결한다.
- Builder는 복잡한 객체 생성 과정 문제를 해결한다.

---

### [핵심]

| Pattern   | 해결 문제                  | 핵심 키워드             | Spring 실무                 |
| --------- | -------------------------- | ----------------------- | --------------------------- |
| Singleton | Single Instance            | Instance Control        | Spring Bean 기본 Scope      |
| Factory   | Object Creation Delegation | Creation Responsibility | Strategy 선택, Adapter 선택 |
| Builder   | Complex Object Creation    | Constructor Explosion   | DTO, Command, Test Fixture  |

---

### [실무]

Pattern 선택 기준:

```text
하나의 인스턴스만 필요한가?
→ Singleton / Spring Bean

객체 선택 조건이 복잡한가?
→ Factory

생성자 파라미터가 많고 선택 필드가 많은가?
→ Builder
```

예:

| 상황                       | 적합한 Pattern                    |
| -------------------------- | --------------------------------- |
| Service Bean 하나를 재사용 | Singleton                         |
| 결제 타입별 Processor 선택 | Factory                           |
| 응답 DTO 필드가 많음       | Builder                           |
| 알림 채널별 Sender 선택    | Factory                           |
| 테스트 데이터 생성         | Builder                           |
| 전역 설정 객체 관리        | Singleton 또는 Configuration Bean |

---

### [주의]

- Singleton은 상태 공유 위험을 검토한다.
- Factory는 God Factory가 되지 않게 한다.
- Builder는 필수값 검증을 놓치지 않는다.
- 세 Pattern을 한 객체에 억지로 모두 적용하지 않는다.
- 문제 유형을 먼저 판단하고 Pattern을 선택한다.

---

### [FAQ]

Q. Singleton과 Factory의 차이는?

A. Singleton은 인스턴스 개수 제어가 목적이고 Factory는 생성 책임 분리가 목적이다.

Q. Factory와 Builder의 차이는?

A. Factory는 어떤 객체를 만들지 선택하고 Builder는 객체 생성 과정을 단계적으로 구성한다.

Q. Builder와 생성자의 차이는?

A. Builder는 필드 이름 기반으로 객체를 생성해 가독성을 높이고 생성자 폭발을 줄인다.

Q. Spring Bean은 Singleton Pattern인가?

A. 유사하지만 정확히는 Spring Container가 관리하는 Singleton Scope Bean이다.

---

# 6. Troubleshooting

## 6.1 Wrong Creation Responsibility

### [개념]

Wrong Creation Responsibility는 객체 생성 책임이 잘못된 Class에 위치하여 결합도와 변경 비용이 증가하는 문제이다.

---

### [핵심]

- Client가 Concrete Class를 직접 생성하면 결합도가 높아진다.
- Service가 객체 생성 조건을 모두 가지면 SRP 위반 가능성이 높다.
- 생성 조건이 바뀌면 Use Case 코드까지 수정된다.
- Factory로 생성 책임을 분리할 수 있다.
- 단순 생성은 분리하지 않는 것이 더 좋을 수 있다.

---

### [Troubleshooting]

문제:

- Service 내부에 `new ConcreteClass()`가 반복된다.
- 객체 생성 조건 if / switch가 증가한다.
- 구현체 추가 시 기존 Service를 수정해야 한다.
- 테스트에서 Fake 구현체로 대체하기 어렵다.

원인:

- 객체 생성 책임이 Use Case Service에 섞여 있다.
- Concrete Class 의존이 강하다.
- Abstraction 없이 구현체를 직접 선택한다.
- Factory 또는 DI 구조가 없다.

해결:

- Factory로 생성 책임을 분리한다.
- Interface 또는 Port를 도입한다.
- Spring Bean List Injection으로 구현체를 선택한다.
- 변경 가능성이 낮은 단순 생성은 유지한다.

---

### [FAQ]

Q. Wrong Creation Responsibility는 무엇인가?

A. 객체 생성 책임이 잘못된 Class에 있어 결합도와 변경 비용이 증가하는 문제이다.

Q. Service 안에서 `new`를 쓰면 무조건 나쁜가?

A. 아니다. 단순 Value Object 생성은 괜찮지만 외부 의존 구현체나 교체 가능한 객체 생성은 주의해야 한다.

Q. 객체 생성 조건문이 많으면 어떻게 해야 하는가?

A. Factory, Strategy, Map-Based Factory 적용을 검토한다.

Q. 생성 책임 분리는 어떤 원칙과 관련 있는가?

A. SRP, OCP, DIP와 관련이 깊다.

---

## 6.2 Builder Misuse

### [개념]

Builder Misuse는 Builder를 부적절하게 사용하여 객체 무결성, 필수값 검증, 코드 단순성을 해치는 문제이다.

---

### [핵심]

- Builder는 필수값 누락을 숨길 수 있다.
- Builder는 모든 필드를 외부에서 설정 가능하게 만들 수 있다.
- Entity Builder 남용은 Domain Invariant를 깨뜨릴 수 있다.
- 단순 객체에 Builder를 적용하면 코드가 장황해진다.
- Builder 사용 시 생성자 검증이 중요하다.

---

### [Troubleshooting]

문제:

- 필수값이 null인 객체가 생성된다.
- Entity 상태가 잘못된 조합으로 생성된다.
- Builder로 연관관계가 무분별하게 설정된다.
- 단순 DTO에도 Builder가 과도하게 사용된다.
- 기본값이 Builder 사용 시 적용되지 않는다.

원인:

- Class Level `@Builder`를 무분별하게 사용했다.
- 생성자 내부 검증이 없다.
- `@Builder.Default`를 누락했다.
- 필수값과 선택값 기준이 없다.
- Domain 생성 규칙을 Builder에 맡겼다.

해결:

- Entity는 Constructor Level `@Builder`를 사용한다.
- 생성자에서 필수값과 Domain Rule을 검증한다.
- 기본값이 필요하면 `@Builder.Default`를 검토한다.
- 단순 DTO는 생성자 또는 Record를 사용한다.
- Test Fixture Builder와 Production Builder를 구분한다.

---

### [FAQ]

Q. Builder Misuse는 무엇인가?

A. Builder를 잘못 사용해 필수값 검증과 객체 무결성을 해치는 문제이다.

Q. Entity에 Builder를 쓰면 위험한 이유는?

A. 모든 필드와 연관관계를 외부에서 임의로 설정할 수 있어 Domain Rule이 깨질 수 있기 때문이다.

Q. Builder 사용 시 필수값 검증은 어디서 하는가?

A. Builder가 호출하는 생성자 내부에서 검증하는 것이 안전하다.

Q. 단순 DTO에도 Builder가 필요한가?

A. 필드가 적고 선택값이 없다면 생성자나 Record가 더 단순할 수 있다.

---

## 6.3 Singleton State Bug

### [개념]

Singleton State Bug는 Singleton 객체가 요청별 상태를 필드에 저장하여 사용자 간 데이터가 섞이거나 동시성 오류가 발생하는 문제이다.

---

### [핵심]

- Singleton Bean은 여러 요청이 공유한다.
- Mutable Field는 요청 간 데이터 오염을 만들 수 있다.
- Thread Safety를 고려하지 않은 공유 상태는 위험하다.
- Stateless Service 설계가 기본이다.
- 요청별 데이터는 Local Variable 또는 Context에 둔다.

---

### [Troubleshooting]

문제:

- A 사용자의 데이터가 B 사용자 요청에서 보인다.
- 동시 요청 시 값이 랜덤하게 바뀐다.
- 테스트에서는 통과하지만 운영에서 간헐적 오류가 발생한다.
- Service 필드에 요청 데이터를 저장한다.

원인:

- Singleton Bean에 요청별 상태를 저장했다.
- `static` Mutable Field를 사용했다.
- 공유 Collection을 동기화 없이 수정했다.
- Thread Safety 설계가 없다.

해결:

- Service를 Stateless로 변경한다.
- 요청별 값은 Method Parameter로 전달한다.
- 공유 Cache는 Thread-safe 구조를 사용한다.
- 필요 시 Request Scope 또는 DB/Cache 저장소를 사용한다.

---

### [FAQ]

Q. Singleton State Bug는 무엇인가?

A. Singleton 객체가 요청별 상태를 공유 필드에 저장해 데이터가 섞이는 문제이다.

Q. Spring Service에 필드를 두면 안 되는가?

A. 의존성 필드는 괜찮지만 요청별 변경 데이터 필드는 위험하다.

Q. Singleton Bean에서 안전한 필드는?

A. 불변 의존성, 설정값, Thread-safe 객체이다.

Q. Singleton State Bug를 예방하는 기본 원칙은?

A. Singleton Bean은 Stateless로 설계한다.

---

# Retrieval Queries

### [FAQ]

Q. Creational Pattern이란?
A. 객체 생성 책임과 생성 과정을 분리하고 캡슐화하는 Design Pattern이다.

Q. Creational Pattern은 언제 사용하는가?
A. 객체 생성 조건이 복잡하거나 생성 책임을 Client에서 분리해야 할 때 사용한다.

Q. Creational Pattern의 대표 패턴은?
A. Singleton, Factory, Builder가 대표적이다.

Q. Singleton Pattern이란?
A. 특정 Class의 인스턴스를 하나만 생성하고 재사용하도록 제한하는 패턴이다.

Q. Spring Bean은 Singleton인가?
A. 기본 Scope 기준으로 Spring Container 단위 Singleton이다.

Q. Spring Boot에서 Singleton Pattern을 직접 구현해야 하는가?
A. 대부분 필요 없다. Spring Bean 기본 Scope을 사용하면 된다.

Q. Singleton의 위험은?
A. 공유 상태로 인한 동시성 문제와 테스트 격리 어려움이다.

Q. Singleton Bean은 왜 Stateless여야 하는가?
A. 여러 요청이 같은 인스턴스를 공유하므로 요청별 상태가 섞일 수 있기 때문이다.

Q. Singleton Bean 필드에는 무엇을 둘 수 있는가?
A. 주입받은 의존성, 불변 설정값, Thread-safe 객체를 둘 수 있다.

Q. 요청별 데이터는 Singleton Bean에서 어떻게 처리하는가?
A. Method Parameter, Local Variable, DTO, Request Scope, DB, Cache 등을 사용한다.

Q. Factory Pattern이란?
A. 객체 생성 또는 선택 책임을 Client에서 분리하여 Factory가 담당하도록 만드는 패턴이다.

Q. Factory Pattern은 언제 사용하는가?
A. 요청 타입이나 조건에 따라 다른 객체를 생성하거나 선택해야 할 때 사용한다.

Q. Factory Pattern은 어떤 원칙과 관련 있는가?
A. SRP, OCP, DIP와 관련이 깊다.

Q. Factory와 Strategy는 어떤 관계인가?
A. Strategy는 알고리즘 교체 구조이고 Factory는 적절한 Strategy 구현체를 선택할 수 있다.

Q. Factory는 객체를 항상 새로 생성하는가?
A. 아니다. Spring Bean처럼 이미 생성된 객체를 선택해 반환할 수도 있다.

Q. Static Factory Method란?
A. 생성자 대신 의미 있는 이름의 static method로 객체를 생성하는 방식이다.

Q. Static Factory Method와 Factory Pattern은 같은가?
A. 아니다. Static Factory Method는 생성 메서드 기법이고 Factory Pattern은 생성 책임 분리 패턴이다.

Q. DTO 변환 Static Factory Method 이름은?
A. Entity나 객체 하나에서 DTO를 만들 때 보통 `from()`을 사용한다.

Q. 여러 값을 받아 객체를 만들 때 Static Factory Method 이름은?
A. 보통 `of()`를 사용한다.

Q. Enum Factory란?
A. Enum 값을 기준으로 적절한 객체나 Strategy 구현체를 선택하는 Factory 방식이다.

Q. Factory에서 String보다 Enum이 좋은 이유는?
A. 타입 안정성이 높고 오타로 인한 분기 오류를 줄일 수 있기 때문이다.

Q. Map-Based Factory란?
A. Key와 구현체를 Map으로 매핑하여 조건문 없이 객체를 선택하는 Factory 방식이다.

Q. Map-Based Factory는 언제 좋은가?
A. 구현체가 많고 선택 로직이 자주 확장될 때 좋다.

Q. Builder Pattern이란?
A. 복잡한 객체 생성을 단계적으로 구성하고 최종 객체를 생성하는 패턴이다.

Q. Builder Pattern은 어떤 문제를 해결하는가?
A. 생성자 파라미터가 많거나 선택 필드가 많은 생성자 폭발 문제를 해결한다.

Q. Lombok `@Builder`란?
A. Builder Pattern 구현 코드를 자동 생성해주는 Lombok 기능이다.

Q. Entity에 `@Builder`를 붙여도 되는가?
A. 가능하지만 Class Level보다 Constructor Level `@Builder`가 더 안전하다.

Q. `@Builder.Default`는 언제 필요한가?
A. Builder 사용 시 필드 기본값을 유지해야 할 때 필요하다.

Q. Builder와 Immutable Object는 왜 잘 어울리는가?
A. 복잡한 생성 과정을 읽기 쉽게 만들고 생성 후 상태 변경을 막을 수 있기 때문이다.

Q. Singleton과 Factory의 차이는?
A. Singleton은 인스턴스 개수 제어가 목적이고 Factory는 생성 책임 분리가 목적이다.

Q. Factory와 Builder의 차이는?
A. Factory는 어떤 객체를 만들지 선택하고 Builder는 객체 생성 과정을 단계적으로 구성한다.

Q. Wrong Creation Responsibility란?
A. 객체 생성 책임이 잘못된 Class에 있어 결합도와 변경 비용이 증가하는 문제이다.

Q. Service 내부 `new`는 무조건 나쁜가?
A. 아니다. 단순 Value Object 생성은 괜찮지만 교체 가능한 구현체 생성은 주의해야 한다.

Q. Builder Misuse란?
A. Builder를 잘못 사용해 필수값 검증과 객체 무결성을 해치는 문제이다.

Q. Singleton State Bug란?
A. Singleton 객체가 요청별 상태를 공유 필드에 저장해 데이터가 섞이는 문제이다.

Q. Backend Agent는 Creational Pattern을 어떻게 사용해야 하는가?
A. 객체 생성 조건과 변경 가능성을 분석해 Factory, Builder, Spring Bean 구조를 선택해야 한다.

Q. Review Agent는 Creational Pattern을 어떻게 검수해야 하는가?
A. 생성 책임 위치, Singleton 상태 공유, Builder 필수값 검증, Factory 과도화를 검수해야 한다.

Q. PM Agent는 Creational Pattern 요구사항을 어떻게 분류해야 하는가?
A. 생성 조건 복잡도, 구현체 선택 가능성, DTO 생성 복잡도, 인스턴스 공유 필요성을 기준으로 분류해야 한다.
