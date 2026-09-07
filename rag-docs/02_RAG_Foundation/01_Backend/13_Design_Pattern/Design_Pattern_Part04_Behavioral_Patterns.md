# Design Pattern Part04 - Behavioral Patterns

---

# 1. Behavioral Pattern Overview

## 1.1 Behavioral Pattern

### [개념]

Behavioral Pattern은 객체 간 책임 분리, 알고리즘 교체, 이벤트 전달, 요청 처리 흐름을 설계하는 Design Pattern이다.

Behavioral Pattern은 객체가 “무엇을 가지고 있는가”보다 “어떻게 행동하고 협력하는가”에 집중한다.

```text
Object A
→ Message / Event / Command
→ Object B
→ Behavior Execution
```

---

### [핵심]

- Behavioral Pattern은 객체 간 행동과 책임 분리를 설계한다.
- Behavioral Pattern은 알고리즘 교체, 이벤트 알림, 요청 객체화, 공통 흐름 분리에 사용된다.
- Behavioral Pattern은 Strategy, Observer, Template Method, Command가 핵심이다.
- Behavioral Pattern은 OCP, SRP, DIP와 관련이 깊다.
- Behavioral Pattern은 조건문 증가, 책임 집중, 흐름 중복을 줄인다.
- Behavioral Pattern은 Spring Event, Strategy Bean, Template Service, Command Handler에서 자주 사용된다.

---

### [실무]

2026 실무 기준 Java 21, Spring Boot 3.x Backend에서는 Behavioral Pattern이 비즈니스 로직 확장과 이벤트 기반 구조에 자주 사용된다.

대표 실무 예:

- Strategy Pattern → 결제 수단, 할인 정책, 추천 알고리즘 교체
- Observer Pattern → 주문 완료 이벤트, 알림 발송, 로그 기록, Kafka Consumer
- Template Method Pattern → 공통 처리 흐름, 인증/검증/실행/후처리 구조
- Command Pattern → 요청 객체화, 작업 큐, 비동기 실행, Undo/Retry 구조
- Chain of Responsibility → Filter Chain, Handler Chain, Validation Chain

Behavioral Pattern은 다음 상황에서 검토한다.

- if / switch 조건문이 계속 증가한다.
- 알고리즘 또는 정책이 자주 교체된다.
- 하나의 이벤트에 여러 후속 작업이 발생한다.
- 공통 처리 흐름은 같고 세부 구현만 다르다.
- 요청을 저장, 전달, 재시도, 큐 처리해야 한다.
- 객체 간 직접 호출이 많아 결합도가 높다.

---

### [주의]

- Behavioral Pattern은 흐름을 분산시키므로 추적성이 떨어질 수 있다.
- 단순 조건문에 Strategy를 과도하게 적용하면 Over Engineering이 된다.
- Event 기반 구조는 최종 일관성과 실패 처리 전략이 필요하다.
- Template Method는 상속 구조를 만들기 때문에 LSP를 주의해야 한다.
- Command 객체가 너무 많아지면 구조가 복잡해진다.

---

### [FAQ]

Q. Behavioral Pattern은 무엇인가?

A. 객체 간 책임, 행동, 알고리즘, 이벤트, 요청 흐름을 설계하는 Design Pattern이다.

Q. Behavioral Pattern은 언제 사용하는가?

A. 알고리즘 교체, 이벤트 전달, 요청 객체화, 공통 흐름 분리, 조건문 증가 문제가 있을 때 사용한다.

Q. Behavioral Pattern의 대표 패턴은?

A. Strategy, Observer, Template Method, Command가 대표적이다.

Q. Behavioral Pattern은 어떤 원칙과 관련 있는가?

A. SRP, OCP, DIP와 관련이 깊다.

---

## 1.2 Behavioral Pattern Selection

### [개념]

Behavioral Pattern Selection은 현재 문제가 알고리즘 교체, 이벤트 알림, 공통 흐름 분리, 요청 객체화 중 어디에 속하는지 판단하고 적절한 Pattern을 선택하는 과정이다.

```text
Behavior Problem
→ Algorithm Change / Event Notification / Flow Skeleton / Request Encapsulation
→ Strategy / Observer / Template Method / Command
```

---

### [핵심]

- 알고리즘 또는 정책 교체가 필요하면 Strategy Pattern을 검토한다.
- 이벤트 발생 후 여러 후속 작업이 필요하면 Observer Pattern을 검토한다.
- 공통 흐름은 같고 일부 단계만 다르면 Template Method Pattern을 검토한다.
- 요청을 객체로 저장, 전달, 재시도, 큐 처리해야 하면 Command Pattern을 검토한다.
- 여러 Handler가 순차적으로 요청을 처리하면 Chain of Responsibility를 검토한다.
- Pattern 선택 전 변경 지점, 실패 처리, 테스트 단위를 확인한다.

---

### [실무]

| 문제 상황                                               | 우선 검토 Pattern       |
| ------------------------------------------------------- | ----------------------- |
| 결제 수단별 처리 알고리즘이 다르다                      | Strategy                |
| 할인 정책이 자주 추가된다                               | Strategy                |
| 축제 추천 알고리즘을 교체해야 한다                      | Strategy                |
| 주문 완료 후 알림, 로그, 포인트 적립이 필요하다         | Observer                |
| 채팅 메시지 생성 후 AI 요약 이벤트를 발생시킨다         | Observer                |
| 여러 API 호출 흐름이 인증 → 검증 → 실행 → 응답으로 같다 | Template Method         |
| 파일 업로드 작업을 큐에 넣고 나중에 실행한다            | Command                 |
| 알림 발송 실패 시 재시도해야 한다                       | Command                 |
| 여러 검증기를 순차적으로 통과해야 한다                  | Chain of Responsibility |

---

### [예제]

```text
카드 결제, 토스 결제, 카카오페이 결제
→ 결제 알고리즘 교체
→ Strategy Pattern 후보
```

```text
축제 시작 하루 전 알림 발생
→ 이메일, 푸시, 앱 알림 발송
→ Observer Pattern 후보
```

```text
공공 API 동기화 흐름이 반복됨
→ 요청 생성, 호출, 파싱, 저장, 로깅 순서 동일
→ Template Method Pattern 후보
```

```text
알림 발송 요청을 DB에 저장 후 비동기 처리
→ 요청 객체화와 재시도 필요
→ Command Pattern 후보
```

---

### [주의]

- Strategy는 알고리즘 교체가 목적이다.
- Observer는 이벤트 알림과 후속 처리 분리가 목적이다.
- Template Method는 공통 흐름 정의가 목적이다.
- Command는 요청 객체화와 실행 제어가 목적이다.
- Pattern 목적이 다르면 비슷한 구조라도 다른 Pattern으로 판단한다.

---

### [FAQ]

Q. Strategy와 Factory는 어떻게 함께 사용하는가?

A. Strategy는 알고리즘 구현체이고 Factory는 요청 타입에 맞는 Strategy를 선택하는 역할을 한다.

Q. Observer와 Command의 차이는?

A. Observer는 이벤트 발생 후 구독자에게 알리는 구조이고 Command는 실행할 요청 자체를 객체로 캡슐화하는 구조이다.

Q. Template Method와 Strategy의 차이는?

A. Template Method는 상속으로 공통 흐름을 고정하고 일부 단계를 재정의하며, Strategy는 조합으로 알고리즘을 교체한다.

Q. Behavioral Pattern 선택 기준은?

A. 알고리즘 교체, 이벤트 알림, 공통 흐름 분리, 요청 객체화 중 어떤 문제인지 먼저 분류한다.

---

# 2. Strategy Pattern

## 2.1 Strategy

### [개념]

Strategy Pattern은 알고리즘 또는 정책을 객체로 분리하고 Runtime에 교체할 수 있도록 만드는 Behavioral Pattern이다.

Context는 Strategy Interface에 의존하고 실제 알고리즘은 Concrete Strategy가 담당한다.

```text
Context
→ Strategy Interface
→ Concrete Strategy
```

---

### [핵심]

- Strategy는 Runtime Behavior Change를 지원한다.
- Strategy는 알고리즘과 정책을 교체 가능하게 만든다.
- Strategy는 if / switch 조건문 증가를 줄인다.
- Strategy는 OCP와 DIP를 실현하는 대표 Pattern이다.
- Strategy는 Factory 또는 Map-Based Factory와 함께 자주 사용된다.
- Strategy는 구현체가 많아질수록 선택 기준과 등록 방식이 중요해진다.

---

### [실무]

Spring Boot Backend에서 Strategy는 다음 영역에 자주 사용된다.

- Payment Strategy
- Discount Strategy
- Notification Strategy
- Recommendation Strategy
- Search Ranking Strategy
- File Parsing Strategy
- Auth Provider Strategy
- AI Prompt Strategy
- Cache Eviction Strategy

나쁜 예:

```java
@Service
public class DiscountService {
    public int discount(String type, int price) {
        if (type.equals("VIP")) {
            return price - 1000;
        }

        if (type.equals("EVENT")) {
            return price - 3000;
        }

        if (type.equals("NEW_USER")) {
            return price - 5000;
        }

        return price;
    }
}
```

문제:

- 할인 정책이 추가될 때 기존 Service를 수정한다.
- 조건문이 계속 증가한다.
- 각 정책 테스트가 어렵다.
- OCP 위반 가능성이 높다.

좋은 방향:

```text
DiscountService
→ DiscountPolicy
→ VipDiscountPolicy / EventDiscountPolicy / NewUserDiscountPolicy
```

---

### [예제]

Strategy Interface:

```java
public interface DiscountPolicy {
    DiscountType getDiscountType();
    int discount(int price);
}
```

Concrete Strategy:

```java
@Component
public class VipDiscountPolicy implements DiscountPolicy {
    @Override
    public DiscountType getDiscountType() {
        return DiscountType.VIP;
    }

    @Override
    public int discount(int price) {
        return price - 1000;
    }
}
```

```java
@Component
public class EventDiscountPolicy implements DiscountPolicy {
    @Override
    public DiscountType getDiscountType() {
        return DiscountType.EVENT;
    }

    @Override
    public int discount(int price) {
        return price - 3000;
    }
}
```

Strategy Factory:

```java
@Component
public class DiscountPolicyFactory {
    private final Map<DiscountType, DiscountPolicy> policyMap;

    public DiscountPolicyFactory(List<DiscountPolicy> policies) {
        this.policyMap = policies.stream()
                .collect(Collectors.toMap(
                        DiscountPolicy::getDiscountType,
                        Function.identity()
                ));
    }

    public DiscountPolicy getPolicy(DiscountType discountType) {
        DiscountPolicy policy = policyMap.get(discountType);

        if (policy == null) {
            throw new IllegalArgumentException("지원하지 않는 할인 타입입니다.");
        }

        return policy;
    }
}
```

Context:

```java
@Service
public class DiscountService {
    private final DiscountPolicyFactory discountPolicyFactory;

    public DiscountService(DiscountPolicyFactory discountPolicyFactory) {
        this.discountPolicyFactory = discountPolicyFactory;
    }

    public int discount(DiscountType discountType, int price) {
        DiscountPolicy policy = discountPolicyFactory.getPolicy(discountType);
        return policy.discount(price);
    }
}
```

---

### [Best Practice]

- Strategy Interface는 알고리즘 계약만 정의한다.
- Concrete Strategy는 하나의 정책에 집중한다.
- Strategy 선택 책임은 Factory로 분리한다.
- Strategy Key는 String보다 Enum을 우선 검토한다.
- 구현체가 많으면 Map-Based Factory를 사용한다.
- 각 Strategy는 독립 Unit Test를 작성한다.
- Strategy 내부에 서로 다른 책임을 섞지 않는다.

---

### [주의]

- 정책이 2~3개이고 변경 가능성이 낮으면 단순 조건문이 더 나을 수 있다.
- Strategy가 너무 많으면 Package와 Naming 규칙이 중요하다.
- Strategy 선택 기준이 복잡하면 Factory가 비대해질 수 있다.
- Strategy 내부에서 다른 Strategy를 직접 선택하면 책임이 흐려진다.
- Strategy Pattern은 조건문을 없애는 것이 아니라 변경 지점을 분리하는 것이 목적이다.

---

### [FAQ]

Q. Strategy Pattern은 무엇인가?

A. 알고리즘 또는 정책을 객체로 분리하고 Runtime에 교체할 수 있게 하는 Behavioral Pattern이다.

Q. Strategy Pattern은 언제 사용하는가?

A. 알고리즘, 정책, 처리 방식이 여러 개이고 추가될 가능성이 높을 때 사용한다.

Q. Strategy Pattern은 어떤 문제를 해결하는가?

A. 조건문 증가, 정책 변경 시 기존 코드 수정, 알고리즘 결합 문제를 해결한다.

Q. Strategy와 Factory는 어떤 관계인가?

A. Strategy는 실제 알고리즘이고 Factory는 요청 타입에 맞는 Strategy를 선택하는 역할을 한다.

---

## 2.2 Strategy and Spring Bean Injection

### [개념]

Spring Bean Injection을 활용하면 여러 Strategy 구현체를 List 또는 Map으로 주입받아 Runtime에 적절한 구현체를 선택할 수 있다.

Spring Container가 Strategy 객체 생성과 생명주기를 관리한다.

```text
Spring Container
→ List<Strategy>
→ Strategy Factory
→ Selected Strategy
```

---

### [핵심]

- Spring은 같은 Interface 구현체들을 List로 주입할 수 있다.
- Strategy 구현체는 `@Component`로 Bean 등록할 수 있다.
- Factory는 주입받은 Strategy 목록을 Map으로 변환할 수 있다.
- 새로운 Strategy 추가 시 기존 Service 수정이 줄어든다.
- Strategy 선택 기준은 명확한 Key로 관리한다.
- Bean 충돌과 중복 Key 검증이 필요하다.

---

### [실무]

Notification Strategy 예:

```java
public interface NotificationSender {
    NotificationChannel getChannel();
    void send(NotificationCommand command);
}
```

```java
@Component
public class EmailNotificationSender implements NotificationSender {
    @Override
    public NotificationChannel getChannel() {
        return NotificationChannel.EMAIL;
    }

    @Override
    public void send(NotificationCommand command) {
        // email send
    }
}
```

```java
@Component
public class PushNotificationSender implements NotificationSender {
    @Override
    public NotificationChannel getChannel() {
        return NotificationChannel.PUSH;
    }

    @Override
    public void send(NotificationCommand command) {
        // push send
    }
}
```

```java
@Component
public class NotificationSenderFactory {
    private final Map<NotificationChannel, NotificationSender> senderMap;

    public NotificationSenderFactory(List<NotificationSender> senders) {
        this.senderMap = senders.stream()
                .collect(Collectors.toUnmodifiableMap(
                        NotificationSender::getChannel,
                        Function.identity()
                ));
    }

    public NotificationSender getSender(NotificationChannel channel) {
        NotificationSender sender = senderMap.get(channel);

        if (sender == null) {
            throw new IllegalArgumentException("지원하지 않는 알림 채널입니다.");
        }

        return sender;
    }
}
```

---

### [Best Practice]

- Strategy Interface에는 `getType()`, `supports()` 같은 선택 메서드를 둔다.
- 선택 기준은 Enum을 우선 사용한다.
- Factory 초기화 시 중복 Key가 있으면 애플리케이션 시작 실패로 처리한다.
- Strategy Bean 이름에 의존하기보다 명시적 Key를 사용한다.
- Strategy 구현체는 Stateless Bean으로 설계한다.
- `@Primary`와 `@Qualifier`는 단일 구현체 선택 시 사용하고, 다중 전략 선택에는 Factory를 우선 검토한다.

---

### [주의]

- `Map<String, Strategy>` 주입은 Bean 이름에 의존하므로 유지보수성이 떨어질 수 있다.
- 중복 Key가 있으면 Runtime 오류가 발생할 수 있다.
- Strategy 구현체가 상태를 가지면 Singleton Bean 동시성 문제가 생길 수 있다.
- Strategy 선택 로직이 복잡해지면 별도 Resolver로 분리한다.
- Factory가 비즈니스 판단까지 담당하지 않게 한다.

---

### [FAQ]

Q. Spring에서 Strategy 구현체 여러 개를 어떻게 주입받는가?

A. 같은 Interface 구현체들을 `List<Strategy>`로 주입받을 수 있다.

Q. Strategy 선택은 어디서 하는 것이 좋은가?

A. Service가 아니라 Factory 또는 Resolver에서 선택하는 것이 좋다.

Q. Strategy Key는 무엇을 쓰는 것이 좋은가?

A. String보다 Enum을 우선 검토한다.

Q. Strategy Bean은 Stateful이어도 되는가?

A. 권장하지 않는다. Singleton Bean으로 관리되므로 Stateless 설계가 안전하다.

---

## 2.3 Strategy vs State

### [개념]

Strategy Pattern과 State Pattern은 구조가 비슷하지만 목적이 다르다.

Strategy는 알고리즘을 교체하기 위한 Pattern이고 State는 객체의 상태 변화에 따라 행동을 변경하기 위한 Pattern이다.

```text
Strategy
→ Select Algorithm

State
→ Behavior by Object State
```

---

### [핵심]

- Strategy는 외부에서 적절한 알고리즘을 선택한다.
- State는 객체 내부 상태에 따라 행동이 달라진다.
- Strategy는 정책 교체에 적합하다.
- State는 상태 전이와 상태별 행동이 복잡할 때 적합하다.
- 두 Pattern 모두 다형성을 활용한다.
- Spring Backend에서는 Strategy 사용 빈도가 더 높다.

---

### [실무]

Strategy가 적합한 경우:

```text
결제 타입 선택
→ CARD / TOSS / KAKAO_PAY
→ PaymentStrategy
```

State가 적합한 경우:

```text
주문 상태 변화
→ CREATED / PAID / SHIPPED / CANCELLED
→ 상태별 허용 행동 다름
```

State 성격 예:

```java
public enum OrderStatus {
    CREATED {
        @Override
        public boolean canCancel() {
            return true;
        }
    },
    PAID {
        @Override
        public boolean canCancel() {
            return true;
        }
    },
    SHIPPED {
        @Override
        public boolean canCancel() {
            return false;
        }
    };

    public abstract boolean canCancel();
}
```

---

### [Comparison]

| 기준      | Strategy                   | State                        |
| --------- | -------------------------- | ---------------------------- |
| 목적      | 알고리즘 교체              | 상태별 행동 변경             |
| 선택 기준 | 요청 타입, 정책 타입       | 객체 내부 상태               |
| 변경 원인 | 새로운 정책 추가           | 상태 전이 규칙 변경          |
| 예        | 결제 수단, 할인 정책       | 주문 상태, 예약 상태         |
| 제어 주체 | Client / Context / Factory | 상태 객체 또는 Domain Object |

---

### [주의]

- 상태값에 따라 if 문이 많으면 State Pattern을 검토한다.
- 정책 타입에 따라 if 문이 많으면 Strategy Pattern을 검토한다.
- 단순 상태 전이는 Enum Method로 충분할 수 있다.
- State Pattern을 무리하게 Class로 분리하면 복잡도가 증가한다.
- 주문, 결제, 예약처럼 상태 전이가 중요한 Domain에서는 상태 전이 규칙을 명확히 둔다.

---

### [FAQ]

Q. Strategy와 State의 차이는?

A. Strategy는 알고리즘 교체가 목적이고 State는 객체 상태 변화에 따른 행동 변경이 목적이다.

Q. 결제 수단 선택은 Strategy인가 State인가?

A. 결제 처리 알고리즘 선택이므로 Strategy가 적합하다.

Q. 주문 상태별 취소 가능 여부는 Strategy인가 State인가?

A. 객체 상태에 따른 행동 변경이므로 State 성격이 강하다.

Q. State Pattern은 꼭 Class로 분리해야 하는가?

A. 아니다. 단순한 경우 Enum Method로 처리할 수 있다.

---

# 3. Observer Pattern

## 3.1 Observer

### [개념]

Observer Pattern은 Subject의 상태 변화나 Event 발생을 여러 Observer에게 알리는 Behavioral Pattern이다.

Observer는 Publish / Subscribe 구조의 기본 Pattern이다.

```text
Subject
→ Event Notification
→ Observer A
→ Observer B
→ Observer C
```

---

### [핵심]

- Observer는 Event Notification을 처리한다.
- Subject와 Observer의 직접 결합을 낮춘다.
- 하나의 이벤트에 여러 후속 작업을 연결할 수 있다.
- Observer는 Event Driven Architecture의 기초이다.
- Spring ApplicationEvent, Event Listener, Kafka Consumer와 관련이 깊다.
- Observer는 실패 처리와 실행 순서 관리가 중요하다.

---

### [실무]

Spring Boot Backend에서 Observer는 다음 상황에 자주 사용된다.

- 회원 가입 완료 후 이메일 발송
- 주문 완료 후 알림, 포인트 적립, 로그 기록
- 결제 완료 후 영수증 발행, 통계 업데이트
- 축제 시작 전 알림 발송
- 채팅 메시지 생성 후 AI 요약 이벤트 발행
- 리뷰 작성 후 평점 통계 갱신
- 파일 업로드 완료 후 썸네일 생성
- Domain Event 발행

직접 호출 방식:

```text
OrderService
→ EmailService
→ PointService
→ LogService
```

Observer 방식:

```text
OrderService
→ OrderCompletedEvent
→ EmailListener
→ PointListener
→ LogListener
```

---

### [예제]

Event:

```java
public record OrderCompletedEvent(
        Long orderId,
        Long userId
) {
}
```

Publisher:

```java
@Service
public class OrderService {
    private final ApplicationEventPublisher eventPublisher;

    public OrderService(ApplicationEventPublisher eventPublisher) {
        this.eventPublisher = eventPublisher;
    }

    public void completeOrder(Long orderId, Long userId) {
        // order complete logic
        eventPublisher.publishEvent(new OrderCompletedEvent(orderId, userId));
    }
}
```

Listener:

```java
@Component
public class OrderNotificationListener {
    @EventListener
    public void handle(OrderCompletedEvent event) {
        // send notification
    }
}
```

```java
@Component
public class OrderPointListener {
    @EventListener
    public void handle(OrderCompletedEvent event) {
        // add point
    }
}
```

---

### [Best Practice]

- Event 이름은 과거형으로 작성한다.
- Event에는 필요한 최소 데이터만 담는다.
- Event 발행 위치는 Domain 상태 변경 이후로 둔다.
- Listener는 하나의 후속 책임에 집중한다.
- Listener 실패가 원본 Use Case에 영향을 줄지 명확히 결정한다.
- 비동기 Event는 재시도, 중복 처리, 순서 보장 전략을 검토한다.
- 외부 메시지 브로커 사용 시 Outbox Pattern을 검토한다.

---

### [주의]

- Event 기반 구조는 흐름 추적이 어려울 수 있다.
- Listener 실행 순서에 의존하면 위험하다.
- Event에 Entity 객체를 그대로 담으면 Lazy Loading, Serialization 문제가 생길 수 있다.
- Transaction Commit 전 Event 처리와 Commit 후 Event 처리를 구분해야 한다.
- 비동기 Listener는 실패를 호출자에게 바로 전달하지 않을 수 있다.

---

### [FAQ]

Q. Observer Pattern은 무엇인가?

A. Subject의 상태 변화나 Event 발생을 여러 Observer에게 알리는 Behavioral Pattern이다.

Q. Observer Pattern은 언제 사용하는가?

A. 하나의 이벤트 후 여러 후속 작업이 필요하고 직접 결합을 줄이고 싶을 때 사용한다.

Q. Spring에서 Observer Pattern은 어떻게 구현하는가?

A. `ApplicationEventPublisher`와 `@EventListener`를 사용할 수 있다.

Q. Event 이름은 어떻게 짓는가?

A. 이미 발생한 사실을 표현하므로 `OrderCompletedEvent`, `UserRegisteredEvent`처럼 과거형으로 짓는다.

---

## 3.2 Spring Event

### [개념]

Spring Event는 Spring ApplicationContext 내부에서 Event를 발행하고 Listener가 이를 처리하도록 지원하는 기능이다.

Spring Event는 Observer Pattern의 Spring 실무 구현 방식이다.

```text
ApplicationEventPublisher
→ Event
→ @EventListener
```

---

### [핵심]

- Spring Event는 Application 내부 이벤트 처리에 적합하다.
- Event Publisher는 Event를 발행한다.
- `@EventListener`는 Event를 구독한다.
- 기본적으로 동기 실행이다.
- `@Async`를 사용하면 비동기 실행이 가능하다.
- Transaction과 연동하려면 `@TransactionalEventListener`를 사용한다.

---

### [실무]

회원 가입 완료 후 이메일 발송:

```java
public record UserRegisteredEvent(
        Long userId,
        String email
) {
}
```

```java
@Service
public class UserService {
    private final ApplicationEventPublisher eventPublisher;

    public UserService(ApplicationEventPublisher eventPublisher) {
        this.eventPublisher = eventPublisher;
    }

    @Transactional
    public void register(UserRegisterCommand command) {
        User user = createUser(command);
        eventPublisher.publishEvent(new UserRegisteredEvent(user.getUserId(), user.getEmail()));
    }
}
```

```java
@Component
public class WelcomeEmailListener {
    @TransactionalEventListener(phase = TransactionPhase.AFTER_COMMIT)
    public void handle(UserRegisteredEvent event) {
        // send welcome email
    }
}
```

---

### [Best Practice]

- DB Commit 이후 처리해야 하는 작업은 `AFTER_COMMIT`을 사용한다.
- Event에는 Entity 대신 ID와 필요한 값만 담는다.
- 외부 API 호출은 Transaction 내부에서 길게 처리하지 않는다.
- 비동기 Listener는 실패 로깅과 재시도 전략을 별도로 둔다.
- 중요한 이벤트는 DB 저장 또는 Message Broker 발행을 검토한다.
- Listener는 멱등성을 고려한다.

---

### [주의]

- 기본 `@EventListener`는 동기 실행이므로 Listener 실패가 원본 흐름에 영향을 줄 수 있다.
- `@TransactionalEventListener`는 Transaction이 없으면 실행되지 않을 수 있다.
- `@Async` 사용 시 Thread Pool 설정과 예외 처리를 고려해야 한다.
- Event는 내부 결합을 줄이지만 흐름 가시성은 낮아진다.
- 중요한 비즈니스 이벤트는 단순 Spring Event만으로 부족할 수 있다.

---

### [FAQ]

Q. Spring Event는 기본적으로 동기인가?

A. 그렇다. 기본 `@EventListener`는 동기 실행이다.

Q. Transaction Commit 후 Event를 처리하려면?

A. `@TransactionalEventListener(phase = TransactionPhase.AFTER_COMMIT)`을 사용한다.

Q. Event에 Entity를 담아도 되는가?

A. 권장하지 않는다. ID와 필요한 값만 담는 것이 안전하다.

Q. Spring Event와 Kafka의 차이는?

A. Spring Event는 애플리케이션 내부 이벤트이고 Kafka는 외부 메시지 브로커 기반 분산 이벤트이다.

---

## 3.3 Event Driven Design

### [개념]

Event Driven Design은 시스템의 중요한 상태 변화나 사실을 Event로 표현하고, 해당 Event를 기반으로 후속 처리를 분리하는 설계 방식이다.

Observer Pattern은 Event Driven Design의 기초 구조이다.

```text
Business Action
→ Domain Event
→ Event Handler
→ Side Effect
```

---

### [핵심]

- Event는 이미 발생한 사실이다.
- Event Driven Design은 직접 호출 결합을 낮춘다.
- Event Handler는 후속 작업을 독립적으로 수행한다.
- Event는 비동기 처리와 확장에 유리하다.
- Event 기반 구조는 최종 일관성을 고려해야 한다.
- 실패 처리, 재시도, 중복 처리, 순서 보장이 중요하다.

---

### [실무]

Event 후보:

| Domain Action    | Event                     |
| ---------------- | ------------------------- |
| 회원 가입 완료   | UserRegisteredEvent       |
| 주문 완료        | OrderCompletedEvent       |
| 결제 승인        | PaymentApprovedEvent      |
| 리뷰 작성        | ReviewCreatedEvent        |
| 채팅 메시지 생성 | ChatMessageCreatedEvent   |
| 축제 시작 임박   | FestivalStartingSoonEvent |
| 후원 결제 완료   | DonationPaidEvent         |

Event 처리 흐름:

```text
DonationPaidEvent
→ ReceiptListener
→ NotificationListener
→ StatisticsListener
```

---

### [Best Practice]

- Event는 Domain에서 의미 있는 사실을 기준으로 만든다.
- Event 이름은 과거형으로 작성한다.
- Event Handler는 작은 책임 하나만 가진다.
- Handler 실패가 전체 Use Case 실패로 이어져야 하는지 결정한다.
- 외부 시스템 연동 이벤트는 Outbox Pattern을 검토한다.
- 비동기 Event는 Idempotency Key를 고려한다.
- Event Flow는 문서화한다.

---

### [주의]

- Event가 너무 많으면 흐름 추적이 어렵다.
- 중요한 순서가 필요한 작업을 무분별하게 비동기 Event로 분리하면 위험하다.
- Event Handler에서 다시 Event를 과도하게 발행하면 복잡도가 증가한다.
- Event Payload가 너무 크면 결합도가 높아진다.
- Eventual Consistency를 이해하지 못하면 데이터 불일치로 오해할 수 있다.

---

### [FAQ]

Q. Event Driven Design은 무엇인가?

A. 상태 변화나 중요한 사실을 Event로 표현하고 후속 처리를 분리하는 설계 방식이다.

Q. Event는 명령인가 사실인가?

A. Event는 이미 발생한 사실이다. 그래서 보통 과거형으로 이름을 짓는다.

Q. Event Handler는 어떤 책임을 가져야 하는가?

A. 하나의 후속 작업을 독립적으로 처리하는 책임을 가져야 한다.

Q. Event 기반 구조의 주의점은?

A. 실패 처리, 재시도, 중복 처리, 순서 보장, 최종 일관성을 고려해야 한다.

---

## 3.4 Observer and Kafka Consumer

### [개념]

Kafka Consumer는 Kafka Topic에 발행된 Message를 구독하고 처리하는 구조이다.

Observer Pattern 관점에서는 Topic이 Event Stream이고 Consumer가 Observer 역할을 수행한다.

```text
Producer
→ Kafka Topic
→ Consumer A
→ Consumer B
```

---

### [핵심]

- Kafka는 분산 메시지 브로커이다.
- Producer는 Event Message를 Topic에 발행한다.
- Consumer는 Topic을 구독하고 Message를 처리한다.
- Consumer Group은 병렬 처리와 메시지 분산을 지원한다.
- Kafka 기반 Observer는 서비스 간 비동기 통신에 적합하다.
- 중복 처리, 순서 보장, 재처리 전략이 중요하다.

---

### [실무]

Kafka Consumer가 적합한 상황:

- 주문 완료 이벤트를 다른 서비스가 처리
- 결제 승인 후 정산 서비스로 이벤트 전달
- 로그, 통계, 검색 인덱스 비동기 업데이트
- 알림 발송 작업 분리
- AI 분석 작업 비동기 실행
- 대량 이벤트 스트리밍 처리

흐름:

```text
Order Service
→ OrderCompletedEvent Topic
→ Notification Consumer
→ Statistics Consumer
→ Search Index Consumer
```

---

### [Best Practice]

- Message는 명확한 Schema를 가진다.
- Consumer 처리는 멱등성을 보장한다.
- 실패 Message는 Retry Topic 또는 DLQ를 검토한다.
- Consumer Offset Commit 전략을 명확히 한다.
- 순서가 중요한 이벤트는 Partition Key를 설계한다.
- Consumer 처리 시간과 Lag를 모니터링한다.
- Event Versioning을 고려한다.

---

### [주의]

- Kafka Consumer는 단순 Observer보다 운영 복잡도가 높다.
- Message 중복 소비 가능성을 고려해야 한다.
- Consumer 실패 시 재시도와 DLQ 전략이 필요하다.
- 순서 보장은 Partition 단위로 제한된다.
- Event Schema 변경은 하위 호환성을 고려해야 한다.

---

### [FAQ]

Q. Kafka Consumer는 Observer Pattern인가?

A. 분산 환경에서 Topic Event를 구독한다는 관점에서 Observer Pattern 성격을 가진다.

Q. Kafka Consumer와 Spring Event Listener의 차이는?

A. Spring Event Listener는 애플리케이션 내부 이벤트이고 Kafka Consumer는 서비스 간 분산 메시지 이벤트를 처리한다.

Q. Kafka Consumer에서 멱등성이 중요한 이유는?

A. 메시지가 중복 처리될 수 있으므로 같은 메시지를 여러 번 처리해도 결과가 안전해야 하기 때문이다.

Q. Kafka Consumer 실패 처리는 어떻게 하는가?

A. Retry, DLQ, Offset Commit 전략, Idempotency를 함께 설계한다.

---

# 4. Template Method Pattern

## 4.1 Template Method

### [개념]

Template Method Pattern은 상위 Class에서 알고리즘의 Skeleton Flow를 정의하고, 하위 Class에서 일부 세부 단계를 구현하도록 하는 Behavioral Pattern이다.

공통 흐름은 고정하고 변하는 단계만 분리한다.

```text
Abstract Template
→ Step 1 Fixed
→ Step 2 Override
→ Step 3 Fixed
→ Step 4 Override
```

---

### [핵심]

- Template Method는 Skeleton Algorithm을 정의한다.
- 공통 흐름은 상위 Class에 둔다.
- 변하는 단계는 하위 Class에서 구현한다.
- 중복 흐름 제거에 유용하다.
- Template Method는 상속 기반 Pattern이다.
- LSP 위반과 상속 남용을 주의해야 한다.

---

### [실무]

Template Method는 다음 상황에서 사용한다.

- 여러 외부 API 동기화 흐름이 비슷하다.
- 파일 파싱 흐름은 같고 포맷별 파싱만 다르다.
- 검증 → 실행 → 후처리 흐름이 반복된다.
- 결제 승인 흐름은 같고 Provider별 호출만 다르다.
- Batch Job 흐름이 반복된다.
- Test Fixture 생성 흐름이 반복된다.

공통 API Sync 흐름:

```text
Prepare Request
→ Call External API
→ Parse Response
→ Validate Data
→ Save Data
→ Log Result
```

---

### [예제]

Abstract Template:

```java
public abstract class ExternalApiSyncTemplate<T> {
    public final void sync() {
        String request = createRequest();
        String response = callApi(request);
        List<T> items = parse(response);
        validate(items);
        save(items);
        logResult(items);
    }

    protected abstract String createRequest();

    protected abstract String callApi(String request);

    protected abstract List<T> parse(String response);

    protected void validate(List<T> items) {
        if (items.isEmpty()) {
            throw new IllegalStateException("동기화 데이터가 없습니다.");
        }
    }

    protected abstract void save(List<T> items);

    protected void logResult(List<T> items) {
        System.out.println("sync count = " + items.size());
    }
}
```

Concrete Class:

```java
@Component
public class FestivalApiSyncService extends ExternalApiSyncTemplate<FestivalItem> {
    @Override
    protected String createRequest() {
        return "festival request";
    }

    @Override
    protected String callApi(String request) {
        return "festival response";
    }

    @Override
    protected List<FestivalItem> parse(String response) {
        return List.of();
    }

    @Override
    protected void save(List<FestivalItem> items) {
        // save festival
    }
}
```

---

### [Best Practice]

- Template Method는 `final`로 흐름 변경을 막을 수 있다.
- 공통 흐름과 변경 단계를 명확히 분리한다.
- Hook Method는 선택적 확장 지점으로 사용한다.
- 하위 Class가 상위 흐름을 깨지 않게 한다.
- 상속보다 Composition이 더 적합한지 먼저 검토한다.
- Strategy로 대체 가능한 경우를 비교한다.

---

### [주의]

- 상속 구조가 깊어지면 이해하기 어렵다.
- 하위 Class가 부모 흐름을 깨면 LSP 위반이 발생한다.
- Template Method는 Runtime 교체보다 Compile-time 구조에 가깝다.
- Spring Bean에서 추상 Class와 DI 구조를 명확히 관리해야 한다.
- 공통 흐름이 자주 바뀌면 모든 하위 Class에 영향이 간다.

---

### [FAQ]

Q. Template Method Pattern은 무엇인가?

A. 상위 Class에서 공통 알고리즘 흐름을 정의하고 하위 Class에서 세부 단계를 구현하는 Pattern이다.

Q. Template Method Pattern은 언제 사용하는가?

A. 여러 기능의 처리 흐름은 같고 일부 단계만 다를 때 사용한다.

Q. Template Method의 핵심은?

A. 공통 흐름은 고정하고 변하는 단계만 하위 Class로 분리하는 것이다.

Q. Template Method의 단점은?

A. 상속 기반이라 구조가 경직될 수 있고 LSP 위반 위험이 있다.

---

## 4.2 Template Method vs Strategy

### [개념]

Template Method와 Strategy는 모두 변하는 로직을 분리하지만 구조가 다르다.

Template Method는 상속으로 공통 흐름을 정의하고, Strategy는 Composition으로 알고리즘을 교체한다.

```text
Template Method
→ Inheritance
→ Fixed Flow

Strategy
→ Composition
→ Replace Algorithm
```

---

### [핵심]

- Template Method는 상속 기반이다.
- Strategy는 조합 기반이다.
- Template Method는 흐름 전체가 같고 일부 단계만 다를 때 적합하다.
- Strategy는 알고리즘 전체를 교체할 때 적합하다.
- Template Method는 공통 흐름 통제에 강하다.
- Strategy는 런타임 교체와 테스트 유연성에 강하다.

---

### [Comparison]

| 기준         | Template Method | Strategy                |
| ------------ | --------------- | ----------------------- |
| 구조         | 상속            | Composition             |
| 목적         | 공통 흐름 고정  | 알고리즘 교체           |
| 변경 단위    | 일부 단계       | 전체 정책 또는 알고리즘 |
| Runtime 교체 | 어려움          | 쉬움                    |
| 유연성       | 낮음            | 높음                    |
| 위험         | 상속 남용       | 구현체 증가             |

---

### [실무]

Template Method가 적합한 경우:

```text
공공 API 동기화
→ 요청 생성, 호출, 파싱, 저장 흐름 동일
→ Provider별 일부 단계만 다름
```

Strategy가 적합한 경우:

```text
추천 알고리즘
→ 인기순 / 거리순 / 사용자 취향 기반
→ 전체 알고리즘 교체 필요
```

---

### [주의]

- 상속이 불편하면 Strategy를 우선 검토한다.
- 공통 흐름 통제가 중요하면 Template Method가 적합하다.
- 런타임 교체가 중요하면 Strategy가 적합하다.
- Template Method는 하위 Class가 많아지면 구조가 경직된다.
- Strategy는 구현체가 많아지면 Factory와 Naming 규칙이 중요하다.

---

### [FAQ]

Q. Template Method와 Strategy의 차이는?

A. Template Method는 상속으로 공통 흐름을 고정하고 Strategy는 조합으로 알고리즘을 교체한다.

Q. Template Method는 언제 Strategy보다 좋은가?

A. 전체 처리 흐름은 동일하고 일부 단계만 다르며 흐름 통제가 중요할 때 좋다.

Q. Strategy는 언제 Template Method보다 좋은가?

A. 알고리즘 전체를 런타임에 교체하거나 테스트 유연성이 중요할 때 좋다.

Q. 상속이 부담되면 어떤 Pattern을 우선 검토하는가?

A. Strategy Pattern을 우선 검토한다.

---

# 5. Command Pattern

## 5.1 Command

### [개념]

Command Pattern은 요청을 객체로 캡슐화하여 실행, 저장, 전달, 재시도, 취소를 가능하게 만드는 Behavioral Pattern이다.

Command는 Request Encapsulation 구조이다.

```text
Client
→ Command Object
→ Invoker
→ Receiver
```

---

### [핵심]

- Command는 요청을 객체화한다.
- Command는 실행 로직과 요청 정보를 분리한다.
- Command는 Queue, Retry, Undo, Logging에 유용하다.
- Command는 비동기 작업 처리에 적합하다.
- Command는 요청 이력을 저장하기 쉽다.
- Command는 Handler 구조와 함께 자주 사용된다.

---

### [실무]

Command Pattern은 다음 상황에서 사용한다.

- 알림 발송 요청 저장 후 비동기 실행
- 파일 변환 요청 큐 처리
- AI 요약 요청 큐 처리
- 관리자 작업 이력 저장
- 결제 취소 요청 재시도
- 배치 작업 요청 저장
- Undo 가능한 작업
- CQRS Command 객체

Command 객체 예:

```text
SendNotificationCommand
→ userId
→ message
→ channel
→ requestedAt
```

---

### [예제]

Command 객체:

```java
public record SendNotificationCommand(
        Long userId,
        String message,
        NotificationChannel channel
) {
}
```

Command Handler:

```java
public interface CommandHandler<C> {
    void handle(C command);
}
```

Concrete Handler:

```java
@Component
public class SendNotificationCommandHandler
        implements CommandHandler<SendNotificationCommand> {
    private final NotificationSenderFactory senderFactory;

    public SendNotificationCommandHandler(NotificationSenderFactory senderFactory) {
        this.senderFactory = senderFactory;
    }

    @Override
    public void handle(SendNotificationCommand command) {
        NotificationSender sender = senderFactory.getSender(command.channel());
        sender.send(command);
    }
}
```

Invoker:

```java
@Service
public class NotificationCommandService {
    private final SendNotificationCommandHandler handler;

    public NotificationCommandService(SendNotificationCommandHandler handler) {
        this.handler = handler;
    }

    public void send(Long userId, String message, NotificationChannel channel) {
        SendNotificationCommand command =
                new SendNotificationCommand(userId, message, channel);

        handler.handle(command);
    }
}
```

---

### [Best Practice]

- Command 객체는 Immutable로 만든다.
- Command 이름은 명령형으로 작성한다.
- Handler는 하나의 Command 처리 책임만 가진다.
- Command 실행 결과가 필요하면 Result 객체를 반환한다.
- 비동기 Command는 상태, 재시도 횟수, 실패 사유를 저장한다.
- Queue 기반 Command는 Idempotency를 고려한다.
- Command와 Event를 구분한다.

---

### [주의]

- Command는 “실행 요청”이고 Event는 “이미 발생한 사실”이다.
- Command 객체가 너무 많으면 구조가 복잡해진다.
- 단순 Service Method 호출까지 모두 Command로 만들 필요는 없다.
- 비동기 Command는 실패와 재시도 정책이 필요하다.
- Command Handler에 여러 Use Case를 섞으면 SRP 위반이 된다.

---

### [FAQ]

Q. Command Pattern은 무엇인가?

A. 요청을 객체로 캡슐화하여 실행, 저장, 전달, 재시도, 취소를 가능하게 하는 Pattern이다.

Q. Command Pattern은 언제 사용하는가?

A. 요청을 큐에 넣거나 저장하거나 재시도하거나 나중에 실행해야 할 때 사용한다.

Q. Command와 Event의 차이는?

A. Command는 앞으로 수행할 요청이고 Event는 이미 발생한 사실이다.

Q. Command Handler의 책임은?

A. 하나의 Command를 받아 해당 요청을 실행하는 책임이다.

---

## 5.2 Command Queue and Retry

### [개념]

Command Queue는 실행할 Command를 Queue 또는 DB에 저장하고 Worker가 나중에 처리하는 구조이다.

Command Queue는 비동기 실행, 재시도, 실패 복구에 유용하다.

```text
Create Command
→ Save Queue
→ Worker Polling
→ Execute
→ Success / Retry / Fail
```

---

### [핵심]

- Command Queue는 비동기 작업 처리에 적합하다.
- Command를 저장하면 실패 후 재시도할 수 있다.
- Worker는 Command를 읽고 Handler를 실행한다.
- 실패 횟수, 상태, 마지막 오류를 기록할 수 있다.
- 중복 실행에 대비해 멱등성을 설계해야 한다.
- Queue는 DB, Redis, RabbitMQ, Kafka 등으로 구현할 수 있다.

---

### [실무]

알림 발송 Command Queue 예:

```text
User Action
→ SendNotificationCommand 저장
→ Notification Worker 실행
→ Sender Strategy 선택
→ Send
→ SUCCESS / RETRY / FAILED
```

Command 상태:

| Status     | 의미        |
| ---------- | ----------- |
| PENDING    | 실행 대기   |
| PROCESSING | 실행 중     |
| SUCCESS    | 성공        |
| RETRY      | 재시도 대기 |
| FAILED     | 최종 실패   |

저장 필드:

- commandId
- commandType
- payload
- status
- retryCount
- maxRetryCount
- lastErrorMessage
- requestedAt
- processedAt

---

### [Best Practice]

- Command Payload는 Versioning을 고려한다.
- Worker는 같은 Command 중복 실행에 안전해야 한다.
- Retry는 지수 백오프를 검토한다.
- 실패 Command는 DLQ 또는 FAILED 상태로 분리한다.
- 장시간 작업은 Timeout을 설정한다.
- Command 처리 로그를 남긴다.
- 운영 모니터링 지표를 수집한다.

---

### [주의]

- Command 중복 실행이 발생할 수 있다.
- Retry가 외부 API 중복 호출을 만들 수 있다.
- Queue 적체 Lag를 모니터링해야 한다.
- DB Queue는 대량 처리 성능 한계가 있을 수 있다.
- Command Payload에 민감 정보를 그대로 저장하지 않는다.

---

### [FAQ]

Q. Command Queue는 무엇인가?

A. 실행할 Command를 Queue나 DB에 저장하고 Worker가 나중에 처리하는 구조이다.

Q. Command Queue는 언제 사용하는가?

A. 비동기 작업, 재시도, 실패 복구, 작업 이력 저장이 필요할 때 사용한다.

Q. Command Queue에서 멱등성이 왜 중요한가?

A. 같은 Command가 중복 실행될 수 있으므로 결과가 안전해야 하기 때문이다.

Q. Command Queue는 무엇으로 구현할 수 있는가?

A. DB, Redis, RabbitMQ, Kafka 등으로 구현할 수 있다.

---

## 5.3 Command vs Event

### [개념]

Command와 Event는 모두 메시지 객체로 표현될 수 있지만 의미가 다르다.

Command는 앞으로 수행해야 할 요청이고 Event는 이미 발생한 사실이다.

```text
Command
→ Do Something

Event
→ Something Happened
```

---

### [핵심]

- Command는 명령이다.
- Event는 사실이다.
- Command 이름은 명령형으로 작성한다.
- Event 이름은 과거형으로 작성한다.
- Command는 보통 하나의 Handler가 처리한다.
- Event는 여러 Listener가 처리할 수 있다.
- Command는 거부될 수 있고 Event는 이미 발생했으므로 취소할 수 없다.

---

### [Comparison]

| 기준      | Command            | Event               |
| --------- | ------------------ | ------------------- |
| 의미      | 수행 요청          | 발생한 사실         |
| 이름      | SendEmailCommand   | EmailSentEvent      |
| 시점      | 실행 전            | 실행 후             |
| 처리자    | 보통 1개 Handler   | 여러 Listener 가능  |
| 실패 의미 | 요청 실패 가능     | 후속 처리 실패 가능 |
| 예        | CreateOrderCommand | OrderCreatedEvent   |

---

### [실무]

Command 예:

```text
SendFestivalReminderCommand
→ 축제 알림을 보내라
```

Event 예:

```text
FestivalReminderSentEvent
→ 축제 알림이 발송되었다
```

Command Flow:

```text
Controller
→ Command
→ Command Handler
→ Domain Action
```

Event Flow:

```text
Domain Action Completed
→ Event
→ Event Listener
→ Side Effects
```

---

### [주의]

- Command를 Event처럼 이름 짓지 않는다.
- Event를 Command처럼 사용하면 의미가 혼란스러워진다.
- Command Handler는 요청을 거부하거나 실패시킬 수 있다.
- Event Listener는 이미 발생한 사실에 대한 후속 처리를 수행한다.
- 시스템 간 메시지는 Command인지 Event인지 명확히 정의한다.

---

### [FAQ]

Q. Command와 Event의 가장 큰 차이는?

A. Command는 앞으로 수행할 요청이고 Event는 이미 발생한 사실이다.

Q. Command는 몇 개의 Handler가 처리하는가?

A. 보통 하나의 Handler가 처리한다.

Q. Event는 몇 개의 Listener가 처리하는가?

A. 여러 Listener가 처리할 수 있다.

Q. Event를 Command처럼 사용하면 왜 문제인가?

A. 이미 발생한 사실인지 앞으로 수행할 요청인지 의미가 불명확해져 흐름과 실패 처리가 혼란스러워진다.

---

# 6. Additional Behavioral Patterns

## 6.1 Chain of Responsibility

### [개념]

Chain of Responsibility Pattern은 요청을 처리할 수 있는 여러 Handler를 체인으로 연결하고, 각 Handler가 처리하거나 다음 Handler로 넘기는 Behavioral Pattern이다.

```text
Request
→ Handler A
→ Handler B
→ Handler C
→ Result
```

---

### [핵심]

- Handler Chain은 요청 처리 책임을 분산한다.
- 각 Handler는 처리 후 다음 Handler로 넘길 수 있다.
- Filter Chain, Validation Chain, Middleware Chain에 사용된다.
- 요청 처리 순서가 중요하다.
- Handler 추가로 확장할 수 있다.
- Chain이 길어지면 흐름 추적이 어려워진다.

---

### [실무]

Spring Security Filter Chain:

```text
Request
→ CORS Filter
→ JWT Filter
→ Authorization Filter
→ Controller
```

Validation Chain:

```text
OrderCommand
→ StockValidator
→ PaymentValidator
→ CouponValidator
→ OrderExecution
```

Handler Interface:

```java
public interface OrderValidator {
    void validate(OrderCommand command);
}
```

Composite Validator:

```java
@Component
public class OrderValidationChain {
    private final List<OrderValidator> validators;

    public OrderValidationChain(List<OrderValidator> validators) {
        this.validators = validators;
    }

    public void validate(OrderCommand command) {
        for (OrderValidator validator : validators) {
            validator.validate(command);
        }
    }
}
```

---

### [Best Practice]

- Chain 순서를 명확히 정의한다.
- 각 Handler는 하나의 검증 또는 처리 책임만 가진다.
- 실패 시 중단할지 다음 Handler로 넘길지 명확히 한다.
- Spring에서는 `@Order`로 순서를 관리할 수 있다.
- Handler 목록은 테스트로 검증한다.
- 공통 요청 전처리는 Filter 또는 Interceptor를 검토한다.

---

### [주의]

- Chain 순서가 잘못되면 보안 또는 비즈니스 오류가 발생할 수 있다.
- Handler가 너무 많으면 디버깅이 어렵다.
- Handler 간 공유 상태를 두면 결합도가 높아진다.
- 어떤 Handler가 요청을 중단했는지 로깅이 필요할 수 있다.
- 모든 조건문을 Chain으로 바꾸는 것은 과할 수 있다.

---

### [FAQ]

Q. Chain of Responsibility Pattern은 무엇인가?

A. 여러 Handler를 체인으로 연결해 요청을 순차적으로 처리하거나 전달하는 Pattern이다.

Q. Chain of Responsibility는 언제 사용하는가?

A. 여러 검증, 필터, 전처리, 후처리를 순서대로 적용해야 할 때 사용한다.

Q. Spring Security Filter Chain은 어떤 Pattern인가?

A. Chain of Responsibility 성격이 강하고 Decorator 성격도 함께 가진다.

Q. Chain에서 가장 중요한 것은?

A. Handler 책임과 실행 순서이다.

---

## 6.2 Mediator Pattern

### [개념]

Mediator Pattern은 여러 객체가 서로 직접 통신하지 않고 중재자 Mediator를 통해 협력하도록 만드는 Behavioral Pattern이다.

Mediator는 객체 간 복잡한 상호작용을 중앙에서 조정한다.

```text
Object A
→ Mediator
→ Object B
→ Object C
```

---

### [핵심]

- Mediator는 객체 간 직접 결합을 줄인다.
- 복잡한 상호작용을 한 곳에서 조정한다.
- 여러 객체가 서로 참조하는 구조를 단순화한다.
- UI Component, Workflow Coordinator, Use Case Orchestrator에 사용될 수 있다.
- Mediator가 커지면 God Object가 될 수 있다.

---

### [실무]

Mediator 성격이 나타나는 경우:

- 여러 Service 호출 순서를 조정하는 Orchestrator
- Multi-Agent Workflow Coordinator
- 채팅방 메시지 라우팅
- 복잡한 화면 Component 간 이벤트 조정
- Saga Orchestrator
- Use Case Facade

예:

```text
PM Agent
→ Workflow Mediator
→ Backend Agent
→ Review Agent
→ Frontend Agent
```

Spring Service Orchestrator 예:

```java
@Service
public class OrderWorkflowMediator {
    private final OrderService orderService;
    private final PaymentService paymentService;
    private final NotificationService notificationService;

    public void process(OrderCommand command) {
        Order order = orderService.create(command);
        paymentService.pay(order);
        notificationService.send(order);
    }
}
```

---

### [Best Practice]

- Mediator는 흐름 조정에 집중한다.
- 하위 객체의 세부 비즈니스 로직을 가져오지 않는다.
- Mediator가 커지면 Use Case별로 분리한다.
- 객체 간 순환 의존성을 줄이는 데 사용한다.
- Workflow 상태와 실패 처리를 명확히 기록한다.
- Multi-Agent 구조에서는 Agent 간 직접 호출보다 Mediator 또는 Orchestrator를 둔다.

---

### [주의]

- Mediator가 모든 로직을 가지면 God Object가 된다.
- 단순 Service 호출에는 Mediator가 불필요할 수 있다.
- Mediator와 Facade는 비슷해 보일 수 있다.
- Facade는 단순 진입점 제공에 가깝고 Mediator는 객체 간 상호작용 조정에 가깝다.
- Workflow가 복잡하면 상태 관리와 보상 트랜잭션을 고려해야 한다.

---

### [FAQ]

Q. Mediator Pattern은 무엇인가?

A. 객체들이 서로 직접 통신하지 않고 중재자를 통해 협력하도록 만드는 Pattern이다.

Q. Mediator는 언제 사용하는가?

A. 여러 객체 간 상호작용이 복잡하고 직접 의존이 많을 때 사용한다.

Q. Mediator의 위험은?

A. 모든 조정 로직이 한 곳에 모여 God Object가 될 수 있다.

Q. Multi-Agent System에서 Mediator는 어떤 역할인가?

A. Agent 간 직접 결합을 줄이고 Workflow 순서와 상태를 조정하는 역할을 할 수 있다.

---

# 7. Behavioral Pattern Comparison

## 7.1 Strategy vs Observer vs Template Method vs Command

### [개념]

Strategy, Observer, Template Method, Command는 모두 Behavioral Pattern이지만 해결하는 문제가 다르다.

- Strategy는 알고리즘 교체 문제를 해결한다.
- Observer는 이벤트 알림 문제를 해결한다.
- Template Method는 공통 흐름과 세부 단계 분리 문제를 해결한다.
- Command는 요청 객체화와 실행 제어 문제를 해결한다.

---

### [핵심]

| Pattern         | 해결 문제      | 핵심 키워드             | 실무 예                      |
| --------------- | -------------- | ----------------------- | ---------------------------- |
| Strategy        | 알고리즘 교체  | Runtime Behavior Change | 결제, 할인, 추천             |
| Observer        | 이벤트 알림    | Event Notification      | Spring Event, Kafka Consumer |
| Template Method | 공통 흐름 정의 | Skeleton Algorithm      | API Sync, Batch Flow         |
| Command         | 요청 객체화    | Request Encapsulation   | Queue, Retry, Undo           |

---

### [Comparison]

```text
Strategy
→ 어떤 방식으로 처리할 것인가

Observer
→ 무엇이 발생했는가를 누구에게 알릴 것인가

Template Method
→ 공통 흐름은 무엇이고 어떤 단계가 달라지는가

Command
→ 어떤 요청을 객체로 저장하고 실행할 것인가
```

구분 질문:

| 질문                                      | Pattern                 |
| ----------------------------------------- | ----------------------- |
| 정책 또는 알고리즘이 교체되는가?          | Strategy                |
| 이벤트 발생 후 여러 후속 작업이 필요한가? | Observer                |
| 처리 흐름은 같고 일부 단계만 다른가?      | Template Method         |
| 요청을 저장, 전달, 재시도해야 하는가?     | Command                 |
| 여러 Handler가 순차 처리하는가?           | Chain of Responsibility |
| 객체 간 상호작용이 복잡한가?              | Mediator                |

---

### [실무]

예시 판단:

```text
결제 타입별 처리 방식
→ Strategy
```

```text
회원 가입 완료 후 이메일 발송
→ Observer
```

```text
공공 API 동기화 공통 흐름
→ Template Method
```

```text
알림 발송 요청을 큐에 저장 후 재시도
→ Command
```

---

### [주의]

- Strategy는 조건문 제거가 아니라 정책 변경 지점 분리가 목적이다.
- Observer는 흐름 분리와 이벤트 알림이 목적이다.
- Template Method는 상속 기반이라 경직될 수 있다.
- Command는 요청 자체를 저장하거나 제어할 필요가 있을 때 사용한다.
- Pattern 이름보다 해결하려는 행동 문제를 먼저 본다.

---

### [FAQ]

Q. Strategy, Observer, Template Method, Command의 차이는?

A. Strategy는 알고리즘 교체, Observer는 이벤트 알림, Template Method는 공통 흐름 정의, Command는 요청 객체화가 목적이다.

Q. 결제 수단별 처리는 어떤 Pattern인가?

A. Strategy Pattern이 적합하다.

Q. 주문 완료 후 알림 발송은 어떤 Pattern인가?

A. Observer Pattern 또는 Event Driven Design이 적합하다.

Q. 요청을 큐에 저장하고 재시도하려면 어떤 Pattern인가?

A. Command Pattern이 적합하다.

---

# 8. Troubleshooting

## 8.1 Strategy Overuse

### [개념]

Strategy Overuse는 단순 조건문이나 변경 가능성이 낮은 로직에 Strategy Pattern을 과도하게 적용하여 Class와 Interface가 불필요하게 증가하는 문제이다.

---

### [핵심]

- Strategy는 변경 가능성이 높은 알고리즘 분리에 적합하다.
- 단순 조건문은 Strategy보다 읽기 쉬울 수 있다.
- Strategy 구현체가 너무 많으면 관리 비용이 증가한다.
- Factory와 Strategy가 함께 과도해지면 구조가 복잡해진다.
- Strategy는 현재 변경 압력과 테스트 필요성을 기준으로 적용한다.

---

### [Troubleshooting]

문제:

- 구현체가 많지만 실제 로직은 거의 없다.
- 조건이 2개뿐인데 Interface와 Factory가 생겼다.
- 파일 수가 증가해 흐름 추적이 어렵다.
- 새로운 정책 추가보다 현재 코드 이해 비용이 더 크다.
- Strategy 선택 로직이 비즈니스 로직보다 복잡하다.

원인:

- 모든 if 문을 Strategy로 바꾸려 했다.
- 미래 확장을 과도하게 예측했다.
- OCP를 형식적으로 적용했다.
- 단순한 분기를 과도하게 추상화했다.

해결:

- 변경 가능성이 낮은 단순 분기는 조건문으로 유지한다.
- 중복 정책과 반복 변경이 확인되면 Strategy로 전환한다.
- Strategy Interface를 역할 단위로 통합한다.
- Factory 선택 로직을 단순화한다.
- 테스트 가치가 낮은 Strategy는 제거를 검토한다.

---

### [FAQ]

Q. Strategy Overuse는 무엇인가?

A. 단순 로직에 Strategy를 과도하게 적용해 Class와 Interface가 불필요하게 늘어나는 문제이다.

Q. 모든 if 문을 Strategy로 바꿔야 하는가?

A. 아니다. 반복 변경과 정책 확장이 있는 조건문에 우선 적용한다.

Q. Strategy 적용 기준은?

A. 알고리즘 교체 가능성, 정책 추가 빈도, 테스트 필요성, 조건문 증가 여부이다.

Q. Strategy를 제거하는 것도 Refactoring인가?

A. 그렇다. 불필요한 추상화를 제거하는 것도 중요한 Refactoring이다.

---

## 8.2 Event Flow Hidden Problem

### [개념]

Event Flow Hidden Problem은 Event 기반 구조에서 실제 처리 흐름이 코드상 명확히 보이지 않아 디버깅, 장애 분석, 영향 범위 파악이 어려워지는 문제이다.

---

### [핵심]

- Event는 직접 호출 결합을 줄이지만 흐름 가시성을 낮춘다.
- Listener가 많아지면 후속 작업 파악이 어렵다.
- 비동기 Event는 실패가 즉시 드러나지 않을 수 있다.
- Event Flow 문서화와 로깅이 중요하다.
- 중요한 이벤트는 추적 ID와 상태 기록이 필요하다.

---

### [Troubleshooting]

문제:

- Event 발행 후 어떤 Listener가 실행되는지 알기 어렵다.
- 특정 후속 작업이 누락되어도 호출자는 모른다.
- 비동기 Listener 실패가 조용히 묻힌다.
- Event 순서 의존성이 숨겨져 있다.
- 장애 발생 시 원인 추적이 어렵다.

원인:

- Event Flow 문서가 없다.
- Listener 실행 결과를 기록하지 않는다.
- 비동기 실패 처리와 재시도 전략이 없다.
- Event 이름과 책임이 불명확하다.
- 하나의 Event가 너무 많은 Listener를 가진다.

해결:

- Event Publisher와 Listener 목록을 문서화한다.
- Event 처리 로그에 traceId, eventId를 포함한다.
- 비동기 Listener 실패는 Retry 또는 DLQ로 관리한다.
- 중요한 Event는 처리 상태를 DB에 기록한다.
- Event를 역할별로 분리하거나 Listener 책임을 축소한다.

---

### [FAQ]

Q. Event Flow Hidden Problem은 무엇인가?

A. Event 기반 구조에서 실제 후속 처리 흐름이 숨겨져 디버깅과 영향 분석이 어려워지는 문제이다.

Q. Event 기반 구조의 흐름 추적은 어떻게 개선하는가?

A. Event Flow 문서화, traceId 로깅, eventId 기록, 처리 상태 저장으로 개선한다.

Q. Listener 실패가 위험한 이유는?

A. 특히 비동기 Listener는 실패가 원본 호출자에게 바로 드러나지 않을 수 있기 때문이다.

Q. Event Listener가 많아지면 어떻게 해야 하는가?

A. Event 책임을 재검토하고 Listener를 역할별로 정리하며 중요한 흐름은 문서화한다.

---

## 8.3 Command Retry Bug

### [개념]

Command Retry Bug는 Command 재시도 과정에서 같은 작업이 중복 실행되어 외부 API 중복 호출, 중복 결제, 중복 알림, 데이터 중복 저장이 발생하는 문제이다.

---

### [핵심]

- Command 재시도는 중복 실행 가능성을 가진다.
- 외부 API 호출은 멱등성 키가 필요할 수 있다.
- Retry는 실패 원인에 따라 제한해야 한다.
- 모든 실패를 재시도하면 장애가 확대될 수 있다.
- Command 상태와 실행 이력을 기록해야 한다.

---

### [Troubleshooting]

문제:

- 같은 알림이 여러 번 발송된다.
- 결제 취소 요청이 중복 실행된다.
- 동일 파일 변환 작업이 여러 번 생성된다.
- Retry가 계속 반복되어 외부 API 제한에 걸린다.
- 실패 원인이 영구 오류인데 계속 재시도한다.

원인:

- Idempotency Key가 없다.
- Command 실행 상태를 원자적으로 변경하지 않았다.
- Retry 가능한 오류와 불가능한 오류를 구분하지 않았다.
- 최대 재시도 횟수와 Backoff 정책이 없다.
- 외부 API 응답 결과를 기록하지 않았다.

해결:

- Command마다 unique commandId 또는 idempotencyKey를 부여한다.
- 실행 전 상태를 PROCESSING으로 원자적 변경한다.
- Retryable Exception과 Non-Retryable Exception을 구분한다.
- maxRetryCount와 exponential backoff를 적용한다.
- 성공한 외부 요청 결과를 저장하고 재사용한다.
- 최종 실패는 DLQ 또는 FAILED 상태로 이동한다.

---

### [FAQ]

Q. Command Retry Bug는 무엇인가?

A. Command 재시도 중 같은 작업이 중복 실행되어 중복 결제, 중복 알림, 중복 저장이 발생하는 문제이다.

Q. Command Retry에서 멱등성이 왜 중요한가?

A. 같은 Command가 여러 번 실행되어도 결과가 한 번 실행한 것과 같아야 하기 때문이다.

Q. 모든 실패를 재시도해도 되는가?

A. 아니다. 일시적 오류만 재시도하고 영구 오류는 실패 처리해야 한다.

Q. Command 중복 실행은 어떻게 막는가?

A. idempotencyKey, 상태 원자 변경, 실행 이력 저장, 외부 API 결과 저장으로 방지한다.

---

## 8.4 Template Method Inheritance Problem

### [개념]

Template Method Inheritance Problem은 Template Method Pattern의 상속 구조가 경직되거나 하위 Class가 상위 Class의 흐름을 깨뜨려 유지보수가 어려워지는 문제이다.

---

### [핵심]

- Template Method는 상속 기반 Pattern이다.
- 상속 계층이 깊어지면 변경 영향이 커진다.
- 하위 Class가 부모 흐름을 우회하면 LSP 위반 가능성이 있다.
- 공통 흐름 변경은 모든 하위 Class에 영향을 준다.
- Strategy 또는 Composition 전환을 검토할 수 있다.

---

### [Troubleshooting]

문제:

- 하위 Class마다 예외적인 흐름이 많다.
- 부모 Template Method가 계속 수정된다.
- Hook Method가 너무 많아진다.
- 상속 계층이 깊고 이해하기 어렵다.
- 일부 하위 Class가 부모의 공통 흐름을 따르지 못한다.

원인:

- 공통 흐름이 충분히 안정적이지 않았다.
- Template Method 적용 대상이 적절하지 않았다.
- 변하는 부분이 일부 단계가 아니라 전체 알고리즘이었다.
- 상속으로 해결하면 안 되는 문제를 상속으로 해결했다.

해결:

- 공통 흐름이 안정적인지 재검토한다.
- 변하는 부분이 많으면 Strategy로 전환한다.
- Hook Method를 줄이고 명확한 추상 단계만 남긴다.
- 상속 깊이를 줄인다.
- Composition 기반 구조를 검토한다.

---

### [FAQ]

Q. Template Method Inheritance Problem은 무엇인가?

A. Template Method의 상속 구조가 경직되어 하위 Class 확장과 유지보수가 어려워지는 문제이다.

Q. Template Method가 적합하지 않은 신호는?

A. 하위 Class마다 예외 흐름이 많고 Hook Method가 계속 증가하는 경우이다.

Q. Template Method를 Strategy로 바꿔야 하는 경우는?

A. 변하는 부분이 일부 단계가 아니라 알고리즘 전체일 때 Strategy가 더 적합하다.

Q. Template Method에서 LSP가 중요한 이유는?

A. 하위 Class가 부모가 정의한 공통 흐름과 계약을 깨면 대체 가능성이 무너지기 때문이다.

---

# Retrieval Queries

### [FAQ]

Q. Behavioral Pattern이란?
A. 객체 간 책임, 행동, 알고리즘, 이벤트, 요청 흐름을 설계하는 Design Pattern이다.

Q. Behavioral Pattern은 언제 사용하는가?
A. 알고리즘 교체, 이벤트 전달, 요청 객체화, 공통 흐름 분리, 조건문 증가 문제가 있을 때 사용한다.

Q. Behavioral Pattern의 대표 패턴은?
A. Strategy, Observer, Template Method, Command가 대표적이다.

Q. Behavioral Pattern은 어떤 원칙과 관련 있는가?
A. SRP, OCP, DIP와 관련이 깊다.

Q. Strategy Pattern이란?
A. 알고리즘 또는 정책을 객체로 분리하고 Runtime에 교체할 수 있게 하는 Pattern이다.

Q. Strategy Pattern은 언제 사용하는가?
A. 알고리즘, 정책, 처리 방식이 여러 개이고 추가될 가능성이 높을 때 사용한다.

Q. Strategy Pattern은 어떤 문제를 해결하는가?
A. 조건문 증가, 정책 변경 시 기존 코드 수정, 알고리즘 결합 문제를 해결한다.

Q. Strategy와 Factory는 어떤 관계인가?
A. Strategy는 실제 알고리즘이고 Factory는 요청 타입에 맞는 Strategy를 선택하는 역할이다.

Q. Spring에서 Strategy 구현체 여러 개를 어떻게 주입받는가?
A. 같은 Interface 구현체들을 `List<Strategy>`로 주입받을 수 있다.

Q. Strategy 선택은 어디서 하는 것이 좋은가?
A. Service가 아니라 Factory 또는 Resolver에서 선택하는 것이 좋다.

Q. Strategy Key는 무엇을 쓰는 것이 좋은가?
A. String보다 Enum을 우선 검토한다.

Q. Strategy Bean은 Stateful이어도 되는가?
A. 권장하지 않는다. Singleton Bean으로 관리되므로 Stateless 설계가 안전하다.

Q. Strategy와 State의 차이는?
A. Strategy는 알고리즘 교체가 목적이고 State는 객체 상태 변화에 따른 행동 변경이 목적이다.

Q. 결제 수단 선택은 Strategy인가 State인가?
A. 결제 처리 알고리즘 선택이므로 Strategy가 적합하다.

Q. 주문 상태별 취소 가능 여부는 Strategy인가 State인가?
A. 객체 상태에 따른 행동 변경이므로 State 성격이 강하다.

Q. Observer Pattern이란?
A. Subject의 상태 변화나 Event 발생을 여러 Observer에게 알리는 Pattern이다.

Q. Observer Pattern은 언제 사용하는가?
A. 하나의 이벤트 후 여러 후속 작업이 필요하고 직접 결합을 줄이고 싶을 때 사용한다.

Q. Spring에서 Observer Pattern은 어떻게 구현하는가?
A. `ApplicationEventPublisher`와 `@EventListener`를 사용할 수 있다.

Q. Event 이름은 어떻게 짓는가?
A. 이미 발생한 사실을 표현하므로 `OrderCompletedEvent`, `UserRegisteredEvent`처럼 과거형으로 짓는다.

Q. Spring Event는 기본적으로 동기인가?
A. 기본 `@EventListener`는 동기 실행이다.

Q. Transaction Commit 후 Event를 처리하려면?
A. `@TransactionalEventListener(phase = TransactionPhase.AFTER_COMMIT)`을 사용한다.

Q. Event에 Entity를 담아도 되는가?
A. 권장하지 않는다. ID와 필요한 값만 담는 것이 안전하다.

Q. Spring Event와 Kafka의 차이는?
A. Spring Event는 애플리케이션 내부 이벤트이고 Kafka는 외부 메시지 브로커 기반 분산 이벤트이다.

Q. Event Driven Design이란?
A. 상태 변화나 중요한 사실을 Event로 표현하고 후속 처리를 분리하는 설계 방식이다.

Q. Event는 명령인가 사실인가?
A. Event는 이미 발생한 사실이다. 그래서 보통 과거형으로 이름을 짓는다.

Q. Kafka Consumer는 Observer Pattern인가?
A. 분산 환경에서 Topic Event를 구독한다는 관점에서 Observer Pattern 성격을 가진다.

Q. Kafka Consumer에서 멱등성이 중요한 이유는?
A. 메시지가 중복 처리될 수 있으므로 같은 메시지를 여러 번 처리해도 결과가 안전해야 하기 때문이다.

Q. Template Method Pattern이란?
A. 상위 Class에서 공통 알고리즘 흐름을 정의하고 하위 Class에서 세부 단계를 구현하는 Pattern이다.

Q. Template Method Pattern은 언제 사용하는가?
A. 여러 기능의 처리 흐름은 같고 일부 단계만 다를 때 사용한다.

Q. Template Method의 핵심은?
A. 공통 흐름은 고정하고 변하는 단계만 하위 Class로 분리하는 것이다.

Q. Template Method와 Strategy의 차이는?
A. Template Method는 상속으로 공통 흐름을 고정하고 Strategy는 조합으로 알고리즘을 교체한다.

Q. Strategy는 언제 Template Method보다 좋은가?
A. 알고리즘 전체를 런타임에 교체하거나 테스트 유연성이 중요할 때 좋다.

Q. Command Pattern은 무엇인가?
A. 요청을 객체로 캡슐화하여 실행, 저장, 전달, 재시도, 취소를 가능하게 하는 Pattern이다.

Q. Command Pattern은 언제 사용하는가?
A. 요청을 큐에 넣거나 저장하거나 재시도하거나 나중에 실행해야 할 때 사용한다.

Q. Command와 Event의 차이는?
A. Command는 앞으로 수행할 요청이고 Event는 이미 발생한 사실이다.

Q. Command Handler의 책임은?
A. 하나의 Command를 받아 해당 요청을 실행하는 책임이다.

Q. Command Queue는 무엇인가?
A. 실행할 Command를 Queue나 DB에 저장하고 Worker가 나중에 처리하는 구조이다.

Q. Command Queue는 언제 사용하는가?
A. 비동기 작업, 재시도, 실패 복구, 작업 이력 저장이 필요할 때 사용한다.

Q. Command Queue에서 멱등성이 왜 중요한가?
A. 같은 Command가 중복 실행될 수 있으므로 결과가 안전해야 하기 때문이다.

Q. Chain of Responsibility Pattern은 무엇인가?
A. 여러 Handler를 체인으로 연결해 요청을 순차적으로 처리하거나 전달하는 Pattern이다.

Q. Chain of Responsibility는 언제 사용하는가?
A. 여러 검증, 필터, 전처리, 후처리를 순서대로 적용해야 할 때 사용한다.

Q. Spring Security Filter Chain은 어떤 Pattern인가?
A. Chain of Responsibility 성격이 강하고 Decorator 성격도 함께 가진다.

Q. Mediator Pattern은 무엇인가?
A. 객체들이 서로 직접 통신하지 않고 중재자를 통해 협력하도록 만드는 Pattern이다.

Q. Mediator는 언제 사용하는가?
A. 여러 객체 간 상호작용이 복잡하고 직접 의존이 많을 때 사용한다.

Q. Multi-Agent System에서 Mediator는 어떤 역할인가?
A. Agent 간 직접 결합을 줄이고 Workflow 순서와 상태를 조정하는 역할을 할 수 있다.

Q. Strategy, Observer, Template Method, Command의 차이는?
A. Strategy는 알고리즘 교체, Observer는 이벤트 알림, Template Method는 공통 흐름 정의, Command는 요청 객체화가 목적이다.

Q. Strategy Overuse란?
A. 단순 로직에 Strategy를 과도하게 적용해 Class와 Interface가 불필요하게 늘어나는 문제이다.

Q. 모든 if 문을 Strategy로 바꿔야 하는가?
A. 아니다. 반복 변경과 정책 확장이 있는 조건문에 우선 적용한다.

Q. Event Flow Hidden Problem이란?
A. Event 기반 구조에서 실제 후속 처리 흐름이 숨겨져 디버깅과 영향 분석이 어려워지는 문제이다.

Q. Event 기반 구조의 흐름 추적은 어떻게 개선하는가?
A. Event Flow 문서화, traceId 로깅, eventId 기록, 처리 상태 저장으로 개선한다.

Q. Command Retry Bug란?
A. Command 재시도 중 같은 작업이 중복 실행되어 중복 결제, 중복 알림, 중복 저장이 발생하는 문제이다.

Q. Command Retry에서 멱등성이 왜 중요한가?
A. 같은 Command가 여러 번 실행되어도 결과가 한 번 실행한 것과 같아야 하기 때문이다.

Q. Template Method Inheritance Problem이란?
A. Template Method의 상속 구조가 경직되어 하위 Class 확장과 유지보수가 어려워지는 문제이다.

Q. Backend Agent는 Behavioral Pattern을 어떻게 사용해야 하는가?
A. 알고리즘 교체, 이벤트 후속 처리, 공통 흐름 분리, 요청 객체화 문제를 구분해 적절한 Pattern을 선택해야 한다.

Q. Review Agent는 Behavioral Pattern을 어떻게 검수해야 하는가?
A. Strategy 과도화, Event 흐름 숨김, Command 재시도 멱등성, Template Method 상속 문제를 검수해야 한다.

Q. PM Agent는 Behavioral Pattern 요구사항을 어떻게 분류해야 하는가?
A. 정책 교체, 이벤트 알림, 비동기 요청 처리, 공통 흐름 반복, Agent 간 중재 요구로 분류해야 한다.
