# Design Pattern Part01 - Core & SOLID

---

# 1. Design Pattern Core

## 1.1 Design Pattern

### [개념]

Design Pattern은 반복적으로 발생하는 Software Design Problem에 대한 재사용 가능한 해결 구조이다.

Design Pattern은 완성된 코드가 아니다.

Design Pattern은 객체 생성, 객체 구조, 객체 행동을 설계하는 방법이다.

Design Pattern은 다음 흐름으로 사용한다.

```text
Problem
→ Pattern Selection
→ Apply
→ Refactor
→ Review
```

---

### [핵심]

- Design Pattern은 재사용 가능한 설계 해법이다.
- Design Pattern은 코드 복사가 아니라 구조 선택이다.
- Design Pattern은 Problem, Pattern, Solution, Trade-off 기준으로 판단한다.
- Design Pattern은 유지보수성, 확장성, 테스트 용이성을 높이기 위해 사용한다.
- Design Pattern은 과도하게 사용하면 Over Engineering이 된다.
- Design Pattern은 SOLID, OOP Principles와 함께 이해해야 한다.

---

### [실무]

2026 실무 기준 Design Pattern은 “패턴을 외워서 적용”하는 방식보다 “문제를 보고 적절한 구조를 선택”하는 방식으로 사용한다.

Spring Boot 3.x, Java 21 Backend에서는 많은 Design Pattern이 Framework 내부에 이미 적용되어 있다.

예:

- Spring Bean Container → Singleton 유사 구조
- Spring Security Filter Chain → Chain / Decorator 성격
- Spring AOP → Proxy
- Spring Event → Observer
- JPA Lazy Loading → Proxy
- Strategy Bean 주입 → Strategy Pattern
- DTO Builder → Builder Pattern

실무에서는 Pattern 이름보다 다음 질문이 중요하다.

- 이 설계가 변경에 강한가?
- 새로운 요구사항 추가 시 기존 코드를 덜 수정하는가?
- 테스트하기 쉬운가?
- 책임이 적절히 분리되었는가?
- 추상화가 과하지 않은가?

---

### [주의]

- Design Pattern을 먼저 정하고 코드를 맞추면 안 된다.
- 작은 CRUD 기능에 과도한 Pattern을 적용하면 복잡도만 증가한다.
- Interface를 무조건 만드는 것은 좋은 설계가 아니다.
- Pattern 적용 후 코드가 더 읽기 어려워졌다면 잘못 적용했을 가능성이 높다.
- Pattern은 정답이 아니라 선택지이다.

---

### [FAQ]

Q. Design Pattern은 무엇인가?

A. 반복되는 설계 문제를 해결하기 위한 재사용 가능한 설계 구조이다.

Q. Design Pattern은 코드인가?

A. 아니다. Design Pattern은 코드가 아니라 설계 방향과 구조이다.

Q. Design Pattern을 왜 사용하는가?

A. 유지보수성, 확장성, 재사용성, 테스트 용이성을 높이기 위해 사용한다.

Q. Design Pattern은 항상 적용해야 하는가?

A. 아니다. 문제에 비해 Pattern이 과하면 Over Engineering이 된다.

Q. Spring Boot에서도 Design Pattern을 직접 써야 하는가?

A. 필요한 경우 사용한다. 다만 많은 Pattern은 Spring Framework 내부에 이미 적용되어 있다.

---

## 1.2 Pattern Selection

### [개념]

Pattern Selection은 현재 문제에 적합한 Design Pattern을 선택하는 과정이다.

Pattern은 문제 유형에 따라 크게 세 가지로 분류한다.

- Creational Pattern
- Structural Pattern
- Behavioral Pattern

```text
Problem Type
→ Creational / Structural / Behavioral
→ Pattern Candidate
→ Trade-off Review
→ Apply
```

---

### [핵심]

- 객체 생성 문제가 있으면 Creational Pattern을 검토한다.
- 객체 관계와 구조 문제가 있으면 Structural Pattern을 검토한다.
- 객체 간 책임, 흐름, 알고리즘 변경 문제가 있으면 Behavioral Pattern을 검토한다.
- Pattern Selection은 Trade-off 검토가 필수이다.
- Pattern 선택 전 현재 코드의 변경 지점을 먼저 찾는다.

---

### [실무]

실무에서 Pattern Selection은 다음 기준으로 판단한다.

| 문제 상황                                      | 우선 검토 Pattern |
| ---------------------------------------------- | ----------------- |
| 생성자가 너무 길다                             | Builder           |
| 객체 생성 조건이 복잡하다                      | Factory           |
| 실행 알고리즘을 교체해야 한다                  | Strategy          |
| 외부 API 인터페이스가 맞지 않는다              | Adapter           |
| 기존 기능에 부가기능을 동적으로 추가해야 한다  | Decorator         |
| 접근 제어, 지연 로딩, 부가기능 삽입이 필요하다 | Proxy             |
| 이벤트 발생 시 여러 객체에 알려야 한다         | Observer          |
| 공통 흐름은 같고 세부 단계만 다르다            | Template Method   |
| 요청을 객체로 저장하거나 큐에 넣어야 한다      | Command           |

---

### [예제]

```text
결제 수단이 카드, 카카오페이, 토스페이로 늘어난다
→ 결제 알고리즘이 교체된다
→ Strategy Pattern 후보
```

```text
외부 지도 API 응답 구조가 내부 DTO와 다르다
→ 인터페이스 변환 필요
→ Adapter Pattern 후보
```

```text
알림 발송 요청을 나중에 실행해야 한다
→ 요청 객체화 필요
→ Command Pattern 후보
```

---

### [주의]

- Pattern 이름만 보고 선택하지 않는다.
- 기존 코드의 실제 변경 지점을 기준으로 선택한다.
- 현재 요구사항이 단순하면 Pattern을 적용하지 않는 선택도 가능하다.
- Pattern 후보가 여러 개면 책임 분리 기준으로 판단한다.

---

### [FAQ]

Q. 어떤 Pattern을 선택해야 하는지 모르겠다면?

A. 먼저 문제가 생성, 구조, 행동 중 어디에 속하는지 분류한다.

Q. Pattern Selection에서 가장 중요한 기준은?

A. 변경 지점과 책임 분리이다.

Q. Pattern 후보가 여러 개면 어떻게 판단하는가?

A. 가장 단순하게 문제를 해결하고 테스트하기 쉬운 구조를 선택한다.

Q. Pattern을 적용하지 않는 것도 좋은 선택인가?

A. 그렇다. 단순한 문제에는 단순한 코드가 더 좋은 설계일 수 있다.

---

# 2. OOP Principles

## 2.1 Object-Oriented Programming

### [개념]

OOP는 객체가 책임과 상태를 가지고 협력하도록 설계하는 프로그래밍 방식이다.

객체지향 설계의 핵심은 Class가 아니라 Responsibility이다.

```text
Object
→ Responsibility
→ Collaboration
→ Message
→ Result
```

---

### [핵심]

- 객체는 상태와 행동을 가진다.
- 객체는 책임을 가져야 한다.
- 객체는 다른 객체와 협력한다.
- 객체 간 협력은 Message 호출로 이루어진다.
- 좋은 객체는 책임이 명확하다.
- 나쁜 객체는 너무 많은 책임을 가진다.

---

### [실무]

Java 21, Spring Boot 3.x Backend에서 OOP는 Entity, Service, Policy, Strategy, Factory, Validator 설계에 직접 영향을 준다.

나쁜 예:

```java
public class OrderService {
    public void order() {
        // 주문 검증
        // 할인 계산
        // 결제 처리
        // 재고 차감
        // 알림 발송
    }
}
```

좋은 방향:

```text
OrderService
→ OrderValidator
→ DiscountPolicy
→ PaymentProcessor
→ StockManager
→ NotificationPublisher
```

실무에서는 객체를 다음 기준으로 분리한다.

- 변경 이유가 다른가?
- 테스트 단위가 다른가?
- 재사용 가능성이 있는가?
- 정책이 교체될 가능성이 있는가?
- 외부 시스템과 연결되는가?

---

### [주의]

- Class를 많이 만든다고 OOP가 아니다.
- Interface를 많이 만든다고 좋은 설계가 아니다.
- Service에 모든 로직이 모이면 Anemic Domain Model 또는 God Service가 될 수 있다.
- Entity에 모든 로직을 넣는 것도 위험하다.
- 책임 분리는 기능 크기와 변경 가능성을 기준으로 판단한다.

---

### [FAQ]

Q. OOP의 핵심은 무엇인가?

A. 객체가 명확한 책임을 가지고 협력하도록 설계하는 것이다.

Q. 좋은 객체란 무엇인가?

A. 책임이 명확하고 변경 이유가 적은 객체이다.

Q. Service에 모든 로직을 넣어도 되는가?

A. 단순 CRUD는 가능하지만 복잡한 정책은 별도 객체로 분리하는 것이 좋다.

Q. Interface는 항상 필요한가?

A. 아니다. 교체 가능성, 테스트 필요성, 외부 의존성 분리가 있을 때 우선 검토한다.

---

## 2.2 Encapsulation

### [개념]

Encapsulation은 객체의 내부 상태와 구현 세부사항을 숨기고 필요한 기능만 외부에 공개하는 원칙이다.

Encapsulation은 데이터 은닉이 아니라 변경 보호이다.

```text
Internal State
→ Private
→ Public Method
→ Controlled Change
```

---

### [핵심]

- 필드는 직접 노출하지 않는다.
- 상태 변경은 의미 있는 메서드로 수행한다.
- 객체 내부 규칙은 객체 내부에서 보호한다.
- Setter 남용은 Encapsulation을 약화시킨다.
- Encapsulation은 유지보수성과 안정성을 높인다.

---

### [실무]

Entity 설계에서 Encapsulation은 매우 중요하다.

나쁜 예:

```java
order.setStatus(OrderStatus.CANCELLED);
order.setCancelledAt(LocalDateTime.now());
```

좋은 예:

```java
order.cancel();
```

```java
public void cancel() {
    if (this.status == OrderStatus.COMPLETED) {
        throw new IllegalStateException("완료된 주문은 취소할 수 없다.");
    }

    this.status = OrderStatus.CANCELLED;
    this.cancelledAt = LocalDateTime.now();
}
```

좋은 Encapsulation은 상태 변경 규칙을 한 곳에 모은다.

---

### [주의]

- 모든 Setter를 열어두면 객체 상태가 어디서든 변경된다.
- DTO에는 Setter가 허용될 수 있지만 Domain Entity에는 신중해야 한다.
- JPA Entity는 기본 생성자가 필요하지만 public으로 열 필요는 없다.
- Lombok `@Setter`를 Entity 전체에 붙이는 것은 주의한다.

---

### [FAQ]

Q. Encapsulation은 단순히 private 필드를 쓰는 것인가?

A. 아니다. 핵심은 상태 변경 규칙을 객체 내부에 보호하는 것이다.

Q. Entity에 Setter를 써도 되는가?

A. 가능은 하지만 무분별한 Setter는 상태 추적을 어렵게 만든다.

Q. 상태 변경 메서드는 왜 필요한가?

A. 객체의 비즈니스 규칙과 상태 변경을 함께 관리하기 위해 필요하다.

Q. DTO도 Encapsulation이 필요한가?

A. DTO는 데이터 전달 목적이 강하므로 Entity보다 완화해서 적용할 수 있다.

---

## 2.3 Abstraction

### [개념]

Abstraction은 복잡한 구현 세부사항을 숨기고 중요한 개념과 역할만 드러내는 설계 원칙이다.

Abstraction은 Interface, Abstract Class, 역할 기반 설계로 구현할 수 있다.

```text
Client
→ Abstraction
→ Implementation
```

---

### [핵심]

- Abstraction은 구현 세부사항을 숨긴다.
- Abstraction은 변경 가능성이 높은 부분을 분리한다.
- Abstraction은 클라이언트 코드가 구현체에 직접 의존하지 않게 만든다.
- Abstraction은 Strategy, Factory, Adapter, Proxy에서 자주 사용된다.
- Abstraction이 과하면 코드 이해가 어려워진다.

---

### [실무]

결제 수단이 여러 개라면 PaymentProcessor Abstraction을 만들 수 있다.

```java
public interface PaymentProcessor {
    void pay(PaymentRequest request);
}
```

```java
@Component
public class CardPaymentProcessor implements PaymentProcessor {
    @Override
    public void pay(PaymentRequest request) {
        // 카드 결제 처리
    }
}
```

```java
@Component
public class TossPaymentProcessor implements PaymentProcessor {
    @Override
    public void pay(PaymentRequest request) {
        // 토스 결제 처리
    }
}
```

Abstraction은 구현체 교체, 테스트 대역 사용, 외부 의존성 분리에 유리하다.

---

### [주의]

- 구현체가 하나뿐이고 변경 가능성이 낮다면 Interface가 불필요할 수 있다.
- Abstraction은 미래 가능성이 아니라 현재 변경 압력 기준으로 판단한다.
- 모든 Service에 Interface를 만드는 방식은 실무에서 과할 수 있다.
- Abstraction은 코드량을 증가시키므로 명확한 이유가 있어야 한다.

---

### [FAQ]

Q. Abstraction은 언제 필요한가?

A. 구현체 교체, 테스트 대역, 외부 의존성 분리, 정책 변경 가능성이 있을 때 필요하다.

Q. Interface는 무조건 만들어야 하는가?

A. 아니다. 변경 가능성이 낮고 구현체가 하나라면 생략할 수 있다.

Q. Abstraction의 단점은 무엇인가?

A. 코드 구조가 복잡해지고 추적할 파일이 늘어난다.

Q. Design Pattern에서 Abstraction은 왜 중요한가?

A. 대부분의 Pattern은 역할과 구현을 분리하기 위해 Abstraction을 사용한다.

---

# 3. SOLID

## 3.1 SOLID Overview

### [개념]

SOLID는 객체지향 설계의 유지보수성, 확장성, 재사용성, 테스트 용이성을 높이기 위한 5가지 원칙이다.

SOLID는 Design Pattern 품질의 기준이다.

SOLID 구성:

- SRP: Single Responsibility Principle
- OCP: Open Closed Principle
- LSP: Liskov Substitution Principle
- ISP: Interface Segregation Principle
- DIP: Dependency Inversion Principle

---

### [핵심]

- SOLID는 객체지향 설계 원칙이다.
- SOLID는 변경에 강한 구조를 만들기 위한 기준이다.
- SOLID는 Pattern 선택과 Code Review의 기준이 된다.
- SOLID는 무조건 적용하는 규칙이 아니라 설계 판단 기준이다.
- SOLID 위반은 Tight Coupling, God Class, Hard Coding, Test Difficulty로 이어진다.

---

### [Flow]

```text
Requirement Change
→ Responsibility Check
→ Dependency Check
→ Interface Check
→ Extension Check
→ SOLID Review
```

---

### [실무]

Spring Boot Backend에서 SOLID는 다음 영역에서 중요하다.

- Service 책임 분리
- Policy 객체 분리
- Repository 의존 방향
- Controller 역할 제한
- External API Adapter 분리
- Payment, Notification, Authentication 전략 분리
- 테스트 가능한 구조 설계

SOLID는 다음 질문으로 검수한다.

- SRP: 이 객체가 변경되는 이유는 하나인가?
- OCP: 새 기능 추가 시 기존 코드를 덜 수정하는가?
- LSP: 하위 타입을 부모 타입으로 바꿔도 정상 동작하는가?
- ISP: 사용하지 않는 메서드에 의존하지 않는가?
- DIP: 고수준 정책이 저수준 구현에 직접 의존하지 않는가?

---

### [주의]

- SOLID를 형식적으로 적용하면 Interface와 Class만 늘어난다.
- SOLID는 단순 CRUD보다 복잡한 비즈니스 규칙에서 더 중요하다.
- SOLID는 Pattern보다 우선되는 설계 기준이다.
- SOLID 위반이 항상 즉시 문제는 아니지만 변경이 반복되면 비용이 커진다.

---

### [FAQ]

Q. SOLID는 무엇인가?

A. 객체지향 설계의 유지보수성과 확장성을 높이기 위한 5가지 설계 원칙이다.

Q. SOLID는 왜 중요한가?

A. 변경에 강하고 테스트하기 쉬운 구조를 만들기 위한 기준이기 때문이다.

Q. Design Pattern과 SOLID는 어떤 관계인가?

A. Design Pattern은 SOLID를 실현하는 구체적인 설계 구조가 될 수 있다.

Q. SOLID는 항상 완벽하게 지켜야 하는가?

A. 아니다. 복잡도와 변경 가능성을 기준으로 실용적으로 적용해야 한다.

---

## 3.2 SRP - Single Responsibility Principle

### [개념]

SRP는 하나의 Class 또는 Module이 하나의 책임만 가져야 한다는 원칙이다.

정확히는 “변경되는 이유가 하나여야 한다”는 의미이다.

```text
One Class
→ One Responsibility
→ One Reason to Change
```

---

### [핵심]

- SRP는 책임 분리 원칙이다.
- 하나의 Class가 여러 변경 이유를 가지면 SRP 위반이다.
- SRP는 유지보수성과 테스트 용이성을 높인다.
- SRP는 Service, Validator, Policy, Adapter 분리의 기준이다.
- SRP 위반은 God Class, God Service로 이어진다.

---

### [실무]

나쁜 예:

```java
public class OrderService {
    public void order(OrderRequest request) {
        validateOrder(request);
        calculateDiscount(request);
        pay(request);
        decreaseStock(request);
        sendNotification(request);
    }
}
```

문제:

- 주문 검증 책임
- 할인 계산 책임
- 결제 책임
- 재고 책임
- 알림 책임

좋은 방향:

```text
OrderService
→ OrderValidator
→ DiscountPolicy
→ PaymentProcessor
→ StockService
→ NotificationPublisher
```

SRP 적용 후 OrderService는 Use Case 흐름 조정에 집중한다.

---

### [Best Practice]

- Controller는 HTTP 요청/응답 처리만 담당한다.
- Service는 Use Case 흐름을 담당한다.
- Policy는 정책 계산을 담당한다.
- Validator는 검증을 담당한다.
- Adapter는 외부 시스템 연결을 담당한다.
- Repository는 Persistence 접근을 담당한다.

---

### [주의]

- 책임을 너무 잘게 나누면 오히려 흐름 추적이 어렵다.
- SRP는 파일 개수를 늘리는 원칙이 아니다.
- 책임 분리는 변경 이유가 실제로 다를 때 적용한다.
- 단순 CRUD에서는 과한 분리가 필요하지 않을 수 있다.

---

### [FAQ]

Q. SRP는 무엇인가?

A. 하나의 Class 또는 Module이 하나의 변경 이유만 가지도록 설계하는 원칙이다.

Q. SRP 위반은 어떻게 찾는가?

A. 한 Class가 검증, 계산, 저장, 알림 등 여러 책임을 동시에 수행하면 의심한다.

Q. Service가 커지면 무조건 SRP 위반인가?

A. 아니다. 하지만 변경 이유가 여러 개라면 분리를 검토해야 한다.

Q. SRP를 적용하면 Class가 많아지지 않는가?

A. 많아질 수 있다. 그래서 실제 변경 가능성과 테스트 필요성을 기준으로 적용해야 한다.

---

## 3.3 OCP - Open Closed Principle

### [개념]

OCP는 소프트웨어 요소가 확장에는 열려 있고 수정에는 닫혀 있어야 한다는 원칙이다.

새로운 기능을 추가할 때 기존 코드를 최소한으로 수정하고 새로운 구현을 추가하는 방식이 좋다.

```text
New Requirement
→ Add New Implementation
→ Existing Code Minimal Change
```

---

### [핵심]

- OCP는 확장 가능성 원칙이다.
- 기존 코드 수정 없이 새로운 기능을 추가하기 쉽게 만든다.
- OCP는 Interface, Strategy, Factory와 자주 연결된다.
- OCP는 변경이 자주 발생하는 영역에 우선 적용한다.
- OCP는 모든 곳에 적용하면 과도한 추상화가 된다.

---

### [실무]

나쁜 예:

```java
public int discount(String type, int price) {
    if (type.equals("NORMAL")) {
        return price;
    }

    if (type.equals("VIP")) {
        return price - 1000;
    }

    if (type.equals("EVENT")) {
        return price - 3000;
    }

    return price;
}
```

문제:

- 할인 정책이 추가될 때마다 기존 메서드를 수정한다.
- 조건문이 계속 증가한다.
- 테스트 범위가 넓어진다.

좋은 방향:

```java
public interface DiscountPolicy {
    int discount(int price);
}
```

```java
public class VipDiscountPolicy implements DiscountPolicy {
    @Override
    public int discount(int price) {
        return price - 1000;
    }
}
```

```java
public class EventDiscountPolicy implements DiscountPolicy {
    @Override
    public int discount(int price) {
        return price - 3000;
    }
}
```

```text
DiscountService
→ DiscountPolicy
→ NormalDiscountPolicy / VipDiscountPolicy / EventDiscountPolicy
```

---

### [Best Practice]

- 변경이 반복되는 조건문은 Strategy 후보이다.
- 객체 생성 조건이 반복되면 Factory 후보이다.
- 외부 API 추가 가능성이 높으면 Adapter 후보이다.
- 알림 채널 추가 가능성이 높으면 Observer 또는 Strategy 후보이다.

---

### [주의]

- OCP를 위해 무조건 Interface를 만들 필요는 없다.
- 변경 가능성이 낮은 영역에 OCP를 적용하면 복잡도만 증가한다.
- OCP는 예측이 아니라 반복되는 변경을 보고 적용하는 것이 안전하다.
- 모든 if 문이 OCP 위반은 아니다.

---

### [FAQ]

Q. OCP는 무엇인가?

A. 기능 확장은 쉽게 하고 기존 코드 수정은 최소화하라는 원칙이다.

Q. OCP는 어떤 Pattern과 관련이 깊은가?

A. Strategy, Factory, Template Method, Adapter와 관련이 깊다.

Q. if 문이 있으면 OCP 위반인가?

A. 아니다. 변경이 반복되어 조건문이 계속 늘어날 때 OCP 위반 가능성이 높다.

Q. OCP를 언제 적용해야 하는가?

A. 정책, 알고리즘, 외부 연동 방식이 자주 바뀌는 영역에 적용한다.

---

## 3.4 LSP - Liskov Substitution Principle

### [개념]

LSP는 하위 타입이 상위 타입을 대체해도 프로그램의 정상 동작이 깨지면 안 된다는 원칙이다.

즉, 부모 타입으로 사용할 수 있다고 선언했다면 모든 자식 타입은 부모의 계약을 지켜야 한다.

```text
Parent Type
→ Child Type Substitution
→ Same Expected Behavior
```

---

### [핵심]

- LSP는 상속과 다형성의 안정성을 위한 원칙이다.
- 하위 타입은 상위 타입의 계약을 깨면 안 된다.
- Override 메서드는 부모의 기대 동작을 위반하면 안 된다.
- LSP 위반은 런타임 오류와 예외 흐름 증가로 이어진다.
- LSP는 상속보다 Composition을 검토하게 만드는 기준이다.

---

### [실무]

나쁜 예:

```java
public class Bird {
    public void fly() {
        // fly
    }
}
```

```java
public class Penguin extends Bird {
    @Override
    public void fly() {
        throw new UnsupportedOperationException();
    }
}
```

문제:

- Penguin은 Bird이지만 fly 계약을 지킬 수 없다.
- Bird 타입으로 Penguin을 사용하면 예외가 발생한다.
- 부모 타입 대체 가능성이 깨진다.

좋은 방향:

```java
public interface Bird {
}
```

```java
public interface Flyable {
    void fly();
}
```

```java
public class Eagle implements Bird, Flyable {
    @Override
    public void fly() {
        // fly
    }
}
```

```java
public class Penguin implements Bird {
}
```

---

### [주의]

- 상속은 “코드 재사용”만 보고 사용하면 위험하다.
- 하위 타입이 부모 메서드를 지원하지 못한다면 잘못된 상속일 가능성이 높다.
- Override에서 예외를 던지는 방식은 LSP 위반 신호일 수 있다.
- 실무에서는 상속보다 Composition이 더 안전한 경우가 많다.

---

### [FAQ]

Q. LSP는 무엇인가?

A. 하위 타입이 상위 타입을 대체해도 정상 동작해야 한다는 원칙이다.

Q. LSP 위반은 언제 발생하는가?

A. 자식 클래스가 부모 클래스의 기대 동작이나 계약을 지키지 못할 때 발생한다.

Q. LSP는 어떤 설계 문제와 관련이 있는가?

A. 잘못된 상속 구조와 관련이 깊다.

Q. LSP 위반을 줄이는 방법은?

A. 무리한 상속을 피하고 Interface 분리 또는 Composition을 사용한다.

---

## 3.5 ISP - Interface Segregation Principle

### [개념]

ISP는 클라이언트가 자신이 사용하지 않는 메서드에 의존하지 않아야 한다는 원칙이다.

큰 Interface 하나보다 역할별로 분리된 작은 Interface가 좋다.

```text
Large Interface
→ Role-Based Interface
→ Client Depends Only Needed Methods
```

---

### [핵심]

- ISP는 Interface 분리 원칙이다.
- 클라이언트는 필요한 기능에만 의존해야 한다.
- 비대한 Interface는 구현체에 불필요한 메서드 구현을 강요한다.
- ISP는 역할 기반 설계에 중요하다.
- ISP는 과도하게 적용하면 Interface가 너무 많아진다.

---

### [실무]

나쁜 예:

```java
public interface NotificationService {
    void sendEmail(String message);
    void sendSms(String message);
    void sendPush(String message);
}
```

```java
public class EmailNotificationService implements NotificationService {
    @Override
    public void sendEmail(String message) {
        // email
    }

    @Override
    public void sendSms(String message) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void sendPush(String message) {
        throw new UnsupportedOperationException();
    }
}
```

좋은 방향:

```java
public interface EmailSender {
    void sendEmail(String message);
}
```

```java
public interface SmsSender {
    void sendSms(String message);
}
```

```java
public interface PushSender {
    void sendPush(String message);
}
```

---

### [Best Practice]

- Interface는 역할 기준으로 나눈다.
- 구현체가 사용하지 않는 메서드를 강제로 구현하면 ISP 위반을 의심한다.
- `UnsupportedOperationException`이 반복되면 Interface 분리를 검토한다.
- Read / Write 책임이 다르면 Interface 분리를 검토한다.

---

### [주의]

- 너무 작은 Interface를 과도하게 만들면 구조가 복잡해진다.
- 구현체가 하나이고 역할이 단순하면 Interface 분리가 불필요할 수 있다.
- ISP는 “무조건 메서드 하나당 Interface 하나”가 아니다.
- 클라이언트 관점에서 필요한 기능 묶음으로 분리한다.

---

### [FAQ]

Q. ISP는 무엇인가?

A. 클라이언트가 사용하지 않는 메서드에 의존하지 않도록 Interface를 분리하는 원칙이다.

Q. ISP 위반은 어떻게 찾는가?

A. 구현체가 필요 없는 메서드를 구현하거나 예외로 막고 있다면 의심한다.

Q. Interface는 작을수록 좋은가?

A. 항상 그렇지는 않다. 역할 단위로 응집력 있게 작아야 한다.

Q. ISP와 SRP는 어떻게 다른가?

A. SRP는 책임 분리, ISP는 Interface 의존성 분리에 초점이 있다.

---

## 3.6 DIP - Dependency Inversion Principle

### [개념]

DIP는 고수준 모듈이 저수준 모듈에 직접 의존하지 않고 Abstraction에 의존해야 한다는 원칙이다.

고수준 정책은 세부 구현에 끌려가면 안 된다.

```text
High-Level Policy
→ Abstraction
← Low-Level Implementation
```

---

### [핵심]

- DIP는 의존성 역전 원칙이다.
- 고수준 정책은 저수준 구현에 직접 의존하지 않는다.
- 둘 다 Abstraction에 의존한다.
- DIP는 테스트 용이성과 교체 가능성을 높인다.
- DIP는 Spring DI, Strategy, Adapter, Hexagonal Architecture와 관련이 깊다.

---

### [실무]

나쁜 예:

```java
public class OrderService {
    private final TossPaymentClient tossPaymentClient;

    public OrderService(TossPaymentClient tossPaymentClient) {
        this.tossPaymentClient = tossPaymentClient;
    }

    public void order(PaymentRequest request) {
        tossPaymentClient.pay(request);
    }
}
```

문제:

- OrderService가 TossPaymentClient에 직접 의존한다.
- 결제사를 바꾸면 OrderService 수정이 필요하다.
- 테스트 시 외부 결제 Client 대체가 어렵다.

좋은 방향:

```java
public interface PaymentPort {
    void pay(PaymentRequest request);
}
```

```java
@Component
public class TossPaymentAdapter implements PaymentPort {
    @Override
    public void pay(PaymentRequest request) {
        // Toss API 호출
    }
}
```

```java
@Service
public class OrderService {
    private final PaymentPort paymentPort;

    public OrderService(PaymentPort paymentPort) {
        this.paymentPort = paymentPort;
    }

    public void order(PaymentRequest request) {
        paymentPort.pay(request);
    }
}
```

```text
OrderService
→ PaymentPort
← TossPaymentAdapter
```

---

### [Best Practice]

- 외부 API Client는 Adapter로 감싼다.
- Service는 외부 구현체보다 Port 또는 Interface에 의존한다.
- 테스트에서는 Fake 또는 Mock 구현체로 대체한다.
- Hexagonal Architecture에서는 DIP가 핵심이다.
- Infrastructure는 Domain 또는 Application 정책에 의존해야 한다.

---

### [주의]

- 모든 의존성을 Interface로 바꾸는 것이 DIP는 아니다.
- 고수준 정책과 저수준 구현의 분리가 필요한 경우에 적용한다.
- 내부 단순 Repository까지 과하게 Port로 감싸면 복잡해질 수 있다.
- DIP는 Architecture 규모와 변경 가능성을 함께 고려한다.

---

### [FAQ]

Q. DIP는 무엇인가?

A. 고수준 모듈이 저수준 구현체가 아니라 Abstraction에 의존해야 한다는 원칙이다.

Q. DIP와 DI는 같은 것인가?

A. 아니다. DIP는 설계 원칙이고 DI는 의존성을 주입하는 구현 방식이다.

Q. Spring DI를 쓰면 자동으로 DIP가 지켜지는가?

A. 아니다. 구현체에 직접 의존하면 DI를 써도 DIP 위반일 수 있다.

Q. DIP는 어떤 상황에서 중요한가?

A. 외부 API, 결제, 알림, 파일 저장소, 메시지 큐처럼 구현체 교체 가능성이 있는 영역에서 중요하다.

---

# 4. SOLID Review Checklist

## 4.1 Code Review Checklist

### [개념]

SOLID Review Checklist는 코드가 유지보수 가능한 구조인지 검수하기 위한 질문 목록이다.

Checklist는 Review Agent가 Code Review, Architecture Review, Refactoring Suggestion에 사용할 수 있다.

---

### [핵심]

- SRP: 변경 이유가 하나인가?
- OCP: 확장 시 기존 코드 수정이 적은가?
- LSP: 하위 타입이 상위 타입을 안전하게 대체하는가?
- ISP: 사용하지 않는 메서드에 의존하지 않는가?
- DIP: 고수준 정책이 저수준 구현체에 직접 의존하지 않는가?

---

### [Checklist]

SRP Checklist:

- Class 이름이 책임을 명확히 표현하는가?
- 하나의 Class가 검증, 계산, 저장, 알림을 모두 처리하지 않는가?
- 변경 이유가 여러 개인가?
- 테스트 단위가 너무 큰가?

OCP Checklist:

- 새로운 정책 추가 시 기존 조건문을 수정해야 하는가?
- if / switch가 계속 증가하는 구조인가?
- Strategy 또는 Factory로 분리할 수 있는가?
- 확장 지점이 명확한가?

LSP Checklist:

- 하위 클래스가 부모 메서드를 예외로 막고 있는가?
- 부모 타입으로 자식 객체를 사용해도 정상 동작하는가?
- 상속보다 Composition이 더 적합한가?
- Override가 부모 계약을 깨지 않는가?

ISP Checklist:

- Interface가 너무 많은 기능을 포함하는가?
- 구현체가 사용하지 않는 메서드를 억지로 구현하는가?
- `UnsupportedOperationException`이 반복되는가?
- 클라이언트가 필요한 메서드에만 의존하는가?

DIP Checklist:

- Service가 외부 API Client에 직접 의존하는가?
- Domain/Application이 Infrastructure 구현체를 직접 알고 있는가?
- Interface 또는 Port로 분리 가능한가?
- 테스트에서 Fake 구현체로 대체 가능한가?

---

### [실무]

Review Agent는 다음 기준으로 판단한다.

```text
Code
→ Responsibility Review
→ Dependency Review
→ Extension Review
→ Interface Review
→ Refactoring Suggestion
```

검수 결과는 다음 형식으로 출력한다.

```text
문제:
OrderService가 결제 Client에 직접 의존한다.

원인:
고수준 Use Case가 저수준 Infrastructure 구현체를 직접 참조한다.

해결:
PaymentPort Interface를 만들고 TossPaymentAdapter가 구현하도록 분리한다.

관련 원칙:
DIP, OCP
```

---

### [FAQ]

Q. SOLID Review는 언제 필요한가?

A. Service가 커지거나 조건문이 늘어나거나 외부 의존성이 많아질 때 필요하다.

Q. SOLID 위반이 있으면 반드시 수정해야 하는가?

A. 아니다. 변경 가능성, 복잡도, 일정, 테스트 위험을 함께 고려해야 한다.

Q. Review Agent는 SOLID를 어떻게 활용해야 하는가?

A. 책임, 확장, 상속, Interface, 의존성 관점으로 코드 구조를 검수한다.

Q. SOLID Review 결과는 어떻게 작성하는가?

A. 문제, 원인, 해결, 관련 원칙 형식으로 작성한다.

---

# 5. Troubleshooting

## 5.1 Pattern Abuse

### [개념]

Pattern Abuse는 필요하지 않은 곳에 Design Pattern을 과도하게 적용하여 코드 복잡도를 증가시키는 문제이다.

---

### [핵심]

- Pattern Abuse는 Over Engineering의 대표 원인이다.
- 단순 문제에 복잡한 Pattern을 적용하면 유지보수가 어려워진다.
- Pattern 이름을 맞추기 위해 구조를 억지로 만들면 안 된다.
- Pattern 적용 전 문제와 변경 가능성을 먼저 확인한다.

---

### [Troubleshooting]

문제:

- Class와 Interface가 지나치게 많다.
- 기능은 단순한데 구조가 복잡하다.
- 코드 흐름 추적이 어렵다.
- Pattern 이름은 있지만 실제 이점이 없다.

원인:

- Pattern을 학습 목적으로 억지 적용했다.
- 미래 확장을 과도하게 예측했다.
- SOLID를 형식적으로만 적용했다.
- Interface 분리를 무조건 좋은 설계로 오해했다.

해결:

- 현재 요구사항 기준으로 단순화한다.
- 실제 변경 가능성이 낮은 Abstraction을 제거한다.
- 중복 조건과 변경 지점이 반복될 때 Pattern을 적용한다.
- Pattern보다 가독성, 테스트 용이성, 변경 비용을 우선한다.

---

### [FAQ]

Q. Pattern Abuse는 무엇인가?

A. 필요하지 않은 곳에 Pattern을 과도하게 적용해 코드 복잡도를 높이는 문제이다.

Q. Pattern Abuse를 어떻게 줄이는가?

A. 현재 문제, 변경 가능성, 테스트 필요성을 기준으로 Pattern 적용 여부를 판단한다.

Q. Interface가 많으면 좋은 설계인가?

A. 아니다. 이유 없는 Interface 증가는 Over Engineering이 될 수 있다.

Q. Pattern을 제거하는 것도 Refactoring인가?

A. 그렇다. 불필요한 추상화를 제거하는 것도 중요한 Refactoring이다.

---

## 5.2 Tight Coupling

### [개념]

Tight Coupling은 객체나 모듈이 서로 강하게 의존하여 변경, 테스트, 확장이 어려운 상태이다.

---

### [핵심]

- Tight Coupling은 변경 전파를 증가시킨다.
- Tight Coupling은 테스트를 어렵게 만든다.
- Tight Coupling은 DIP, OCP 위반과 관련이 깊다.
- 외부 API Client 직접 의존은 Tight Coupling 신호이다.
- Abstraction, Adapter, Port, Strategy로 완화할 수 있다.

---

### [Troubleshooting]

문제:

- 한 Class 수정이 여러 Class 수정으로 이어진다.
- 외부 API 변경 시 Service 코드까지 수정된다.
- Unit Test에서 Mock 대체가 어렵다.
- 구현체 교체가 어렵다.

원인:

- 고수준 정책이 저수준 구현체에 직접 의존한다.
- 외부 시스템 연결 코드가 Service 내부에 섞여 있다.
- Interface 또는 Adapter 경계가 없다.
- 책임 분리가 부족하다.

해결:

- 외부 연동은 Adapter로 분리한다.
- Service는 Port 또는 Interface에 의존하게 한다.
- 변경 가능성이 높은 정책은 Strategy로 분리한다.
- 객체 생성 책임은 Factory로 분리한다.

---

### [FAQ]

Q. Tight Coupling은 무엇인가?

A. 객체나 모듈이 강하게 묶여 변경과 테스트가 어려운 상태이다.

Q. Tight Coupling은 어떤 문제를 만든다?

A. 변경 전파, 테스트 어려움, 구현체 교체 어려움, 유지보수 비용 증가를 만든다.

Q. Tight Coupling을 줄이는 Pattern은?

A. Strategy, Adapter, Factory, Proxy, Observer, Hexagonal Architecture가 도움이 된다.

Q. 모든 의존성을 제거해야 하는가?

A. 아니다. 필요한 의존성은 유지하되 변경 가능성이 높은 의존성을 분리한다.

---

# Retrieval Queries

### [FAQ]

Q. Design Pattern이란?
A. 반복되는 Software Design Problem을 해결하기 위한 재사용 가능한 설계 구조이다.

Q. Design Pattern은 코드인가?
A. 아니다. Design Pattern은 코드가 아니라 객체 생성, 구조, 행동을 설계하는 방법이다.

Q. Design Pattern을 왜 사용하는가?
A. 유지보수성, 확장성, 재사용성, 테스트 용이성을 높이기 위해 사용한다.

Q. Design Pattern을 언제 쓰면 안 되는가?
A. 문제가 단순하고 변경 가능성이 낮으면 Pattern 적용이 Over Engineering이 될 수 있다.

Q. Pattern Selection은 어떻게 하는가?
A. 문제를 생성, 구조, 행동 문제로 분류하고 변경 지점과 Trade-off를 검토한다.

Q. Creational Pattern은 언제 사용하는가?
A. 객체 생성 방식, 생성 책임, 복잡한 생성 과정을 분리해야 할 때 사용한다.

Q. Structural Pattern은 언제 사용하는가?
A. 객체 관계, 인터페이스 변환, 기능 확장, 접근 제어 구조가 필요할 때 사용한다.

Q. Behavioral Pattern은 언제 사용하는가?
A. 알고리즘 교체, 이벤트 전달, 요청 객체화, 공통 흐름 분리가 필요할 때 사용한다.

Q. OOP의 핵심은?
A. 객체가 명확한 책임을 가지고 다른 객체와 협력하도록 설계하는 것이다.

Q. Encapsulation이란?
A. 내부 상태와 구현 세부사항을 숨기고 의미 있는 메서드로 상태 변경을 제어하는 원칙이다.

Q. Abstraction이란?
A. 복잡한 구현 세부사항을 숨기고 중요한 역할과 계약만 드러내는 설계 원칙이다.

Q. SOLID란?
A. 객체지향 설계의 유지보수성, 확장성, 테스트 용이성을 높이는 5가지 원칙이다.

Q. SRP란?
A. 하나의 Class 또는 Module이 하나의 변경 이유만 가지도록 설계하는 원칙이다.

Q. OCP란?
A. 확장에는 열려 있고 기존 코드 수정에는 닫혀 있어야 한다는 원칙이다.

Q. LSP란?
A. 하위 타입이 상위 타입을 대체해도 정상 동작해야 한다는 원칙이다.

Q. ISP란?
A. 클라이언트가 사용하지 않는 메서드에 의존하지 않도록 Interface를 분리하는 원칙이다.

Q. DIP란?
A. 고수준 모듈이 저수준 구현체가 아니라 Abstraction에 의존해야 한다는 원칙이다.

Q. DIP와 DI의 차이는?
A. DIP는 설계 원칙이고 DI는 의존성을 외부에서 주입하는 구현 방식이다.

Q. Spring DI를 쓰면 DIP가 자동으로 지켜지는가?
A. 아니다. 구현체에 직접 의존하면 DI를 사용해도 DIP 위반일 수 있다.

Q. SOLID와 Design Pattern의 관계는?
A. Design Pattern은 SOLID 원칙을 실현하는 구체적인 설계 구조가 될 수 있다.

Q. Service가 커지면 어떤 원칙을 먼저 검토해야 하는가?
A. SRP를 먼저 검토하고 책임 분리 가능성을 확인한다.

Q. if 문이 많으면 어떤 원칙을 검토해야 하는가?
A. OCP를 검토하고 Strategy 또는 Factory 적용 가능성을 확인한다.

Q. 상속 구조가 이상하면 어떤 원칙을 검토해야 하는가?
A. LSP를 검토하고 Interface 분리 또는 Composition 전환을 확인한다.

Q. Interface에 사용하지 않는 메서드가 많으면?
A. ISP 위반 가능성이 있으므로 역할별 Interface 분리를 검토한다.

Q. 외부 API Client를 Service가 직접 사용하면?
A. DIP 위반과 Tight Coupling 가능성이 있으므로 Adapter 또는 Port 분리를 검토한다.

Q. Pattern Abuse란?
A. 필요하지 않은 곳에 Design Pattern을 과도하게 적용하여 복잡도를 높이는 문제이다.

Q. Tight Coupling이란?
A. 객체나 모듈이 강하게 의존하여 변경, 테스트, 확장이 어려운 상태이다.

Q. Review Agent는 Design Pattern 문서를 어떻게 사용해야 하는가?
A. 코드의 책임, 확장성, 의존성, Interface 구조를 검수하고 적절한 Pattern 또는 단순화를 제안해야 한다.

Q. Backend Agent는 Design Pattern 문서를 어떻게 사용해야 하는가?
A. 기능 요구사항의 변경 지점을 분석하고 적절한 객체 구조, Interface, Adapter, Strategy를 생성해야 한다.

Q. PM Agent는 Design Pattern 문서를 어떻게 사용해야 하는가?
A. 요구사항이 어떤 설계 문제를 만들 수 있는지 분류하고 Agent에게 적절한 설계 방향을 지시해야 한다.
