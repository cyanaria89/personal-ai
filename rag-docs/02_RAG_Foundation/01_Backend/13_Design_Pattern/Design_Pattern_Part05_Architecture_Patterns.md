# Design Pattern Part05 - Architecture Patterns

---

# 1. Architecture Pattern Overview

## 1.1 Architecture Pattern

### [개념]

Architecture Pattern은 애플리케이션 전체 구조, 책임 분리, 의존성 방향, 계층 간 협력 방식을 설계하는 대규모 Design Pattern이다.

Architecture Pattern은 Class 단위 Pattern보다 큰 범위에서 시스템 구조를 결정한다.

```text
Requirement
→ Architecture Boundary
→ Dependency Direction
→ Module Responsibility
→ Maintainable System
```

---

### [핵심]

- Architecture Pattern은 시스템 전체 구조를 설계한다.
- Architecture Pattern은 계층, 모듈, 의존성 방향을 정의한다.
- Architecture Pattern은 유지보수성, 확장성, 테스트 용이성에 직접 영향을 준다.
- Architecture Pattern은 Layered Architecture, Hexagonal Architecture, Clean Architecture가 핵심이다.
- Architecture Pattern은 Domain Isolation과 Dependency Rule이 중요하다.
- Architecture Pattern은 프로젝트 규모와 복잡도에 맞게 선택해야 한다.

---

### [실무]

2026 실무 기준 Java 21, Spring Boot 3.x Backend에서는 대부분 Layered Architecture를 기본으로 시작한다.

복잡한 Domain, 외부 시스템 연동, 테스트 격리, 장기 유지보수성이 중요해지면 Hexagonal Architecture 또는 Clean Architecture 성격을 부분 적용한다.

실무 선택 기준:

| 상황                                             | 우선 구조              |
| ------------------------------------------------ | ---------------------- |
| 단순 CRUD 프로젝트                               | Layered Architecture   |
| Controller-Service-Repository 중심               | Layered Architecture   |
| 외부 API 연동이 많음                             | Hexagonal Architecture |
| Domain Rule 보호가 중요함                        | Clean Architecture     |
| 결제, 알림, 파일, 메시지 브로커 교체 가능성 높음 | Hexagonal Architecture |
| 대규모 서비스와 장기 유지보수                    | Clean Architecture     |
| 학습/소규모 프로젝트                             | Layered + 일부 Adapter |

---

### [주의]

- Architecture Pattern은 프로젝트 규모에 맞게 적용한다.
- 단순 CRUD에 Clean Architecture 전체를 강제하면 Over Engineering이 된다.
- Layered Architecture도 책임 분리를 잘하면 충분히 실무적이다.
- Hexagonal Architecture는 Port와 Adapter가 많아져 구조 복잡도가 증가한다.
- Clean Architecture는 Dependency Rule을 지키지 않으면 의미가 약해진다.
- Architecture Pattern은 폴더 구조가 아니라 의존성 방향과 책임 분리가 핵심이다.

---

### [FAQ]

Q. Architecture Pattern은 무엇인가?

A. 애플리케이션 전체 구조, 책임 분리, 의존성 방향을 설계하는 대규모 Design Pattern이다.

Q. Architecture Pattern은 Class Design Pattern과 무엇이 다른가?

A. Class Design Pattern은 객체 단위 문제를 해결하고 Architecture Pattern은 시스템 구조 문제를 해결한다.

Q. Spring Boot에서 기본으로 많이 쓰는 구조는?

A. Controller, Service, Repository 중심의 Layered Architecture를 많이 사용한다.

Q. Architecture Pattern 선택 기준은?

A. 프로젝트 규모, Domain 복잡도, 외부 시스템 연동, 테스트 격리, 유지보수 기간을 기준으로 선택한다.

---

## 1.2 Architecture Pattern Selection

### [개념]

Architecture Pattern Selection은 시스템의 복잡도, 변경 가능성, 외부 의존성, Domain 중요도를 기준으로 적절한 Architecture Pattern을 선택하는 과정이다.

```text
Project Context
→ Complexity Review
→ Dependency Review
→ Domain Importance Review
→ Architecture Selection
```

---

### [핵심]

- 단순하면 Layered Architecture를 우선 검토한다.
- 외부 시스템 교체 가능성이 높으면 Hexagonal Architecture를 검토한다.
- Domain Rule 보호가 중요하면 Clean Architecture를 검토한다.
- Architecture Pattern은 처음부터 완전 적용보다 점진 적용이 안전하다.
- 핵심은 Package 이름보다 Dependency Direction이다.
- Architecture Pattern은 Team Skill과 일정도 고려해야 한다.

---

### [실무]

선택 질문:

| 질문                                               | 선택 방향                         |
| -------------------------------------------------- | --------------------------------- |
| 대부분 CRUD인가?                                   | Layered Architecture              |
| Service가 외부 API Client에 직접 의존하는가?       | Hexagonal Architecture 부분 적용  |
| Domain Rule이 Infrastructure에 오염되고 있는가?    | Clean Architecture 검토           |
| 테스트에서 외부 시스템 대체가 어려운가?            | Port / Adapter 적용               |
| Controller가 여러 Service를 복잡하게 조합하는가?   | Facade / Application Service 검토 |
| Repository와 Entity 중심으로 모든 로직이 흐르는가? | Domain Service / Policy 분리 검토 |
| 기능이 작고 일정이 짧은가?                         | 단순 Layered 유지                 |

---

### [예제]

```text
학원 팀 프로젝트
→ Spring Boot CRUD + 일부 외부 API
→ Layered Architecture 기본
→ 외부 API 영역만 Adapter 적용
```

```text
결제, 알림, 파일 저장소가 교체될 수 있음
→ Port Interface 정의
→ TossPaymentAdapter, EmailNotificationAdapter, S3FileStorageAdapter
→ Hexagonal Architecture 부분 적용
```

```text
Domain Rule이 복잡한 주문 시스템
→ Entity / Domain Service / Use Case / Adapter 분리
→ Clean Architecture 검토
```

---

### [주의]

- Architecture Pattern을 너무 빨리 복잡하게 만들지 않는다.
- 모든 기능에 Port를 만들면 코드량이 급증한다.
- 단순 Repository까지 무조건 Adapter로 감싸는 것은 과할 수 있다.
- 팀원이 구조를 이해하지 못하면 유지보수성이 오히려 낮아진다.
- Architecture는 문서화와 Naming Rule이 함께 필요하다.

---

### [FAQ]

Q. Architecture Pattern은 언제 바꿔야 하는가?

A. 기존 구조로 변경, 테스트, 외부 시스템 교체가 어려워질 때 검토한다.

Q. 처음부터 Clean Architecture로 시작해야 하는가?

A. 반드시 그럴 필요는 없다. 프로젝트 규모와 복잡도에 맞게 점진 적용하는 것이 안전하다.

Q. Layered Architecture는 나쁜 구조인가?

A. 아니다. 책임 분리와 의존성 관리가 잘 되면 충분히 좋은 구조이다.

Q. Architecture Pattern에서 가장 중요한 것은?

A. 의존성 방향과 책임 분리이다.

---

# 2. Layered Architecture

## 2.1 Layered Architecture

### [개념]

Layered Architecture는 애플리케이션을 계층별 책임으로 분리하는 Architecture Pattern이다.

Spring Boot Backend에서는 일반적으로 Controller, Service, Repository, Entity 계층으로 구성한다.

```text
Controller
→ Service
→ Repository
→ Database
```

---

### [핵심]

- Layered Architecture는 가장 흔한 Spring Boot 구조이다.
- 각 Layer는 고유한 책임을 가진다.
- Controller는 HTTP 요청과 응답을 처리한다.
- Service는 Use Case와 비즈니스 흐름을 처리한다.
- Repository는 Persistence 접근을 처리한다.
- Entity는 Domain Data와 일부 Domain Behavior를 가진다.
- 단순 CRUD와 학습 프로젝트에 적합하다.

---

### [실무]

기본 Package 구조:

```text
com.example.project
├ controller
├ service
├ repository
├ entity
├ dto
├ exception
└ config
```

Layer 책임:

| Layer      | 책임                                              |
| ---------- | ------------------------------------------------- |
| Controller | Request Mapping, Parameter Binding, Response 반환 |
| Service    | Transaction, Use Case Flow, Business Logic        |
| Repository | DB 접근, Query Method, JPQL, QueryDSL             |
| Entity     | Table Mapping, Domain State, Domain Method        |
| DTO        | Request / Response Data Transfer                  |
| Exception  | Error Handling                                    |
| Config     | Spring Configuration                              |

---

### [예제]

Controller:

```java
@RestController
@RequestMapping("/orders")
public class OrderController {
    private final OrderService orderService;

    public OrderController(OrderService orderService) {
        this.orderService = orderService;
    }

    @PostMapping
    public OrderResponse create(@RequestBody OrderCreateRequest request) {
        return orderService.create(request);
    }
}
```

Service:

```java
@Service
public class OrderService {
    private final OrderRepository orderRepository;

    @Transactional
    public OrderResponse create(OrderCreateRequest request) {
        Order order = Order.create(request.userId(), request.totalPrice());
        Order savedOrder = orderRepository.save(order);

        return OrderResponse.from(savedOrder);
    }
}
```

Repository:

```java
public interface OrderRepository extends JpaRepository<Order, Long> {
}
```

---

### [Best Practice]

- Controller는 Service를 호출하고 HTTP 처리에 집중한다.
- Service는 Use Case 단위로 작성한다.
- Repository는 DB 접근 책임만 가진다.
- DTO와 Entity를 분리한다.
- Transaction은 Service 계층에 둔다.
- 복잡한 정책은 Policy, Strategy, Domain Service로 분리한다.
- 외부 API 호출은 Adapter 성격 Class로 분리한다.

---

### [주의]

- Service가 모든 책임을 가지면 God Service가 된다.
- Controller에 비즈니스 로직을 넣지 않는다.
- Repository에 비즈니스 정책을 넣지 않는다.
- Entity를 Controller Response로 직접 반환하지 않는다.
- DTO 변환 위치를 일관되게 관리한다.
- Layered Architecture는 외부 시스템 교체에는 약할 수 있다.

---

### [FAQ]

Q. Layered Architecture는 무엇인가?

A. 애플리케이션을 Controller, Service, Repository 같은 계층별 책임으로 분리하는 구조이다.

Q. Spring Boot에서 Layered Architecture는 어떻게 구성하는가?

A. 일반적으로 Controller, Service, Repository, Entity, DTO, Config, Exception 계층으로 구성한다.

Q. Layered Architecture의 장점은?

A. 단순하고 이해하기 쉬우며 Spring Boot CRUD 프로젝트에 적합하다.

Q. Layered Architecture의 단점은?

A. Service가 비대해지기 쉽고 외부 시스템 교체나 Domain Isolation에는 약할 수 있다.

---

## 2.2 Layer Responsibility

### [개념]

Layer Responsibility는 각 계층이 담당해야 할 역할과 담당하지 말아야 할 역할을 명확히 구분하는 설계 기준이다.

Layered Architecture의 품질은 Layer Responsibility가 결정한다.

```text
Request
→ Controller Responsibility
→ Service Responsibility
→ Repository Responsibility
→ Database
```

---

### [핵심]

- Controller는 HTTP Adapter 역할이다.
- Service는 Application Use Case 역할이다.
- Repository는 Persistence Access 역할이다.
- Entity는 Domain State와 Domain Behavior를 가진다.
- DTO는 계층 간 데이터 전달 역할이다.
- Layer 간 책임이 섞이면 유지보수성이 떨어진다.

---

### [실무]

Controller가 해야 할 일:

- URL Mapping
- Request Parameter Binding
- Request Body 검증 트리거
- 인증 사용자 정보 추출
- Service 호출
- Response 반환

Controller가 하지 말아야 할 일:

- 할인 계산
- 주문 상태 변경 정책
- DB 직접 접근
- 외부 API 직접 호출
- 복잡한 조건 처리

Service가 해야 할 일:

- Use Case Flow
- Transaction Boundary
- Domain Object 호출
- Repository 조합
- 외부 Port 또는 Adapter 호출
- 결과 DTO 변환

Repository가 해야 할 일:

- Entity 저장
- Entity 조회
- Query Method
- JPQL / QueryDSL
- Persistence 관련 처리

---

### [예제]

나쁜 예:

```java
@PostMapping("/orders")
public OrderResponse create(@RequestBody OrderCreateRequest request) {
    if (request.totalPrice() < 0) {
        throw new IllegalArgumentException();
    }

    Order order = new Order(request.userId(), request.totalPrice());
    orderRepository.save(order);

    return OrderResponse.from(order);
}
```

문제:

- Controller가 검증, 생성, 저장까지 처리한다.
- Layer Responsibility가 깨진다.

좋은 방향:

```text
OrderController
→ OrderService
→ OrderValidator
→ OrderRepository
```

---

### [Best Practice]

- Controller는 얇게 유지한다.
- Service는 Use Case 중심으로 작성한다.
- 복잡한 정책은 별도 Domain Service 또는 Policy로 분리한다.
- Repository는 Query와 Persistence에 집중한다.
- Entity 상태 변경은 의미 있는 Domain Method로 처리한다.
- DTO 변환은 Service 또는 Mapper에서 일관되게 처리한다.

---

### [주의]

- Service가 너무 많은 Repository와 외부 Client를 직접 조합하면 비대해진다.
- DTO 변환 위치가 섞이면 코드 일관성이 깨진다.
- Entity에 모든 로직을 넣으면 Persistence Model과 Domain Model이 강하게 결합될 수 있다.
- Repository에 정책 조건이 과도하게 들어가면 Query와 Business Rule이 섞인다.

---

### [FAQ]

Q. Controller에는 어떤 로직을 넣어야 하는가?

A. HTTP 요청 처리, Parameter Binding, Service 호출, Response 반환에 집중해야 한다.

Q. Service의 핵심 책임은 무엇인가?

A. Use Case 흐름, Transaction, 비즈니스 로직 조합을 담당한다.

Q. Repository에 비즈니스 로직을 넣어도 되는가?

A. 권장하지 않는다. Repository는 Persistence 접근 책임에 집중해야 한다.

Q. Layer Responsibility가 중요한 이유는?

A. 책임이 섞이면 변경 영향이 커지고 테스트와 유지보수가 어려워지기 때문이다.

---

## 2.3 God Service Problem

### [개념]

God Service Problem은 하나의 Service Class가 너무 많은 책임을 담당하여 변경, 테스트, 이해가 어려워지는 문제이다.

Layered Architecture에서 가장 자주 발생하는 Architecture Smell이다.

```text
Large Service
→ Validation
→ Calculation
→ External API
→ Persistence
→ Notification
→ Report
```

---

### [핵심]

- God Service는 SRP 위반 가능성이 높다.
- Service가 커질수록 테스트 단위가 커진다.
- 변경 이유가 여러 개가 된다.
- 외부 시스템과 Domain Logic이 섞인다.
- Policy, Strategy, Validator, Adapter, Facade로 분리할 수 있다.
- 모든 분리가 정답은 아니며 변경 가능성을 기준으로 판단한다.

---

### [실무]

God Service 신호:

- Service 코드가 수백 줄 이상이다.
- Method 하나가 너무 길다.
- 여러 Repository를 과도하게 직접 사용한다.
- 외부 API Client 호출이 Service 내부에 섞여 있다.
- if / switch 정책 분기가 많다.
- 검증, 계산, 저장, 알림이 한 Method에 있다.
- 테스트 작성이 어렵다.

분리 후보:

| 문제                | 분리 후보                    |
| ------------------- | ---------------------------- |
| 검증 로직 증가      | Validator                    |
| 할인/정책 분기 증가 | Strategy / Policy            |
| 외부 API 호출       | Adapter                      |
| 객체 생성 조건 복잡 | Factory                      |
| 여러 후속 작업      | Event / Observer             |
| 여러 Service 조합   | Facade / Application Service |
| 공통 흐름 반복      | Template Method              |

---

### [Troubleshooting]

문제:

- `OrderService`가 주문 생성, 결제, 재고, 알림, 통계를 모두 처리한다.

원인:

- Use Case 흐름과 세부 정책이 한 Class에 섞였다.
- 외부 시스템 Adapter가 없다.
- 후속 작업을 직접 호출로 연결했다.
- 정책 변경 지점을 분리하지 않았다.

해결:

```text
OrderService
→ OrderValidator
→ PaymentPort
→ StockService
→ OrderCompletedEvent
→ NotificationListener
→ StatisticsListener
```

---

### [주의]

- God Service를 한 번에 너무 잘게 쪼개면 구조가 복잡해진다.
- 먼저 변경 이유가 다른 책임부터 분리한다.
- 외부 API 호출, 정책 알고리즘, 이벤트 후속 작업을 우선 분리한다.
- 단순 CRUD Service는 어느 정도 큰 것이 문제가 아닐 수 있다.
- Refactoring은 테스트와 함께 진행한다.

---

### [FAQ]

Q. God Service란 무엇인가?

A. 하나의 Service가 너무 많은 책임을 담당하여 변경과 테스트가 어려운 상태이다.

Q. God Service는 왜 문제인가?

A. SRP 위반, 변경 영향 증가, 테스트 어려움, 코드 이해 비용 증가를 만든다.

Q. God Service는 어떻게 분리하는가?

A. Validator, Policy, Strategy, Adapter, Event Listener, Facade 등으로 책임을 분리한다.

Q. Service가 크면 무조건 God Service인가?

A. 아니다. 변경 이유가 여러 개이고 책임이 섞여 있을 때 God Service로 본다.

---

# 3. Hexagonal Architecture

## 3.1 Hexagonal Architecture

### [개념]

Hexagonal Architecture는 Application Core를 중심에 두고 외부 시스템을 Port와 Adapter로 분리하는 Architecture Pattern이다.

Hexagonal Architecture는 Ports and Adapters Architecture라고도 부른다.

```text
External Actor
→ Inbound Adapter
→ Inbound Port / Use Case
→ Application Core
→ Outbound Port
← Outbound Adapter
← External System
```

---

### [핵심]

- Hexagonal Architecture는 Domain 중심 설계이다.
- Application Core는 외부 기술에 직접 의존하지 않는다.
- Port는 내부가 외부와 통신하기 위해 정의한 Interface이다.
- Adapter는 실제 외부 기술 구현이다.
- 의존성 방향은 Adapter가 Core를 향해야 한다.
- DIP를 Architecture 수준에서 적용한다.
- 외부 시스템 교체와 테스트 격리에 유리하다.

---

### [실무]

Spring Boot에서 Hexagonal Architecture는 다음 영역에 유용하다.

- Payment Provider 교체
- Notification Channel 교체
- File Storage 교체
- External API 연동
- Message Broker 연동
- AI API Provider 교체
- Search Engine 교체
- Cache Provider 교체

기본 구조:

```text
application
├ port
│ ├ in
│ └ out
├ service
domain
├ model
├ policy
adapter
├ in
│ └ web
└ out
  ├ persistence
  ├ payment
  └ notification
```

---

### [예제]

Outbound Port:

```java
public interface PaymentPort {
    PaymentResult pay(PaymentCommand command);
}
```

Application Service:

```java
@Service
public class OrderUseCase {
    private final PaymentPort paymentPort;

    public OrderUseCase(PaymentPort paymentPort) {
        this.paymentPort = paymentPort;
    }

    public void order(OrderCommand command) {
        PaymentResult result = paymentPort.pay(command);
        // order process
    }
}
```

Outbound Adapter:

```java
@Component
public class TossPaymentAdapter implements PaymentPort {
    private final TossPaymentClient tossPaymentClient;

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

---

### [Best Practice]

- Port 이름은 외부 기술이 아니라 Use Case 필요 기준으로 작성한다.
- `TossPaymentPort`보다 `PaymentPort`가 적절하다.
- Adapter 이름에는 외부 기술명을 포함할 수 있다.
- Application Core는 외부 DTO를 알지 않는다.
- Adapter는 외부 DTO를 내부 Result로 변환한다.
- 테스트에서는 Port의 Fake 구현체를 사용한다.
- 모든 기능에 강제 적용하지 말고 외부 연동 영역부터 적용한다.

---

### [주의]

- Port와 Adapter가 많아져 코드 구조가 복잡해질 수 있다.
- 단순 CRUD Repository까지 모두 Port로 감싸면 과할 수 있다.
- Package 구조만 Hexagonal로 만들고 의존성 방향을 지키지 않으면 의미가 없다.
- Adapter에 비즈니스 로직을 넣으면 Core Isolation이 깨진다.
- Port가 외부 API 스펙을 따라가면 내부가 외부에 종속된다.

---

### [FAQ]

Q. Hexagonal Architecture는 무엇인가?

A. Application Core를 중심에 두고 외부 시스템을 Port와 Adapter로 분리하는 Architecture Pattern이다.

Q. Port와 Adapter는 무엇인가?

A. Port는 Core가 필요로 하는 Interface이고 Adapter는 실제 외부 기술 구현체이다.

Q. Hexagonal Architecture의 장점은?

A. 외부 시스템 교체, 테스트 격리, Domain Isolation에 유리하다.

Q. Hexagonal Architecture는 언제 적용하는가?

A. 외부 API, 결제, 알림, 파일 저장소, 메시지 브로커처럼 교체 가능성이 높은 영역에 적용한다.

---

## 3.2 Port

### [개념]

Port는 Application Core가 외부 세계와 상호작용하기 위해 정의하는 Interface이다.

Port는 외부 기술이 아니라 내부 Use Case가 필요로 하는 기능을 기준으로 정의한다.

```text
Application Core
→ Port Interface
← Adapter Implementation
```

---

### [핵심]

- Port는 내부 중심 Interface이다.
- Port는 Dependency Inversion을 가능하게 한다.
- Port는 Inbound Port와 Outbound Port로 나눌 수 있다.
- Inbound Port는 외부가 Application을 호출하는 Use Case Interface이다.
- Outbound Port는 Application이 외부 시스템을 호출하는 Interface이다.
- Port는 외부 기술 이름에 종속되지 않는 것이 좋다.

---

### [실무]

Inbound Port 예:

```java
public interface CreateOrderUseCase {
    OrderResult createOrder(CreateOrderCommand command);
}
```

Outbound Port 예:

```java
public interface PaymentPort {
    PaymentResult pay(PaymentCommand command);
}
```

좋은 Port 이름:

- `PaymentPort`
- `NotificationPort`
- `FileStoragePort`
- `FestivalExternalPort`
- `AiSummaryPort`
- `MessagePublisherPort`

나쁜 Port 이름:

- `TossPaymentPort`
- `KakaoMapApiPort`
- `S3UploadPort`
- `OpenAiGptPort`

외부 기술명이 들어간 이름은 Adapter에 더 적합하다.

---

### [Best Practice]

- Port는 내부 Use Case 언어로 작성한다.
- Port Method는 Application이 필요한 결과를 반환한다.
- 외부 API DTO를 Port에 노출하지 않는다.
- Port는 최소 기능만 가진다.
- Port가 커지면 역할별로 분리한다.
- Port 테스트는 Fake 구현체로 대체 가능해야 한다.

---

### [주의]

- Port를 외부 API 스펙에 맞추면 Adapter 격리 효과가 사라진다.
- Port가 너무 많으면 구조가 복잡해진다.
- Repository Port 적용은 프로젝트 규모를 고려한다.
- Port에 너무 일반적인 메서드를 넣으면 의미가 흐려진다.
- Port는 Interface 분리 원칙 ISP를 고려해야 한다.

---

### [FAQ]

Q. Port는 무엇인가?

A. Application Core가 외부 시스템과 상호작용하기 위해 정의하는 Interface이다.

Q. Inbound Port와 Outbound Port의 차이는?

A. Inbound Port는 외부가 Application을 호출하는 Use Case Interface이고 Outbound Port는 Application이 외부 시스템을 호출하는 Interface이다.

Q. Port 이름에 외부 기술명을 넣어도 되는가?

A. 권장하지 않는다. Port는 내부 기능 기준으로 이름을 짓고 외부 기술명은 Adapter 이름에 둔다.

Q. Port에 외부 API Response DTO를 반환해도 되는가?

A. 권장하지 않는다. 내부 Result 객체로 변환해서 반환해야 한다.

---

## 3.3 Adapter

### [개념]

Adapter는 Port를 구현하거나 외부 요청을 Application Core로 전달하는 기술 구현체이다.

Adapter는 외부 시스템, Framework, Database, API, Message Broker와 Application Core 사이의 경계이다.

```text
External System
→ Adapter
→ Port
→ Application Core
```

---

### [핵심]

- Adapter는 외부 기술 세부사항을 담당한다.
- Adapter는 Port를 구현한다.
- Adapter는 외부 DTO와 내부 모델을 변환한다.
- Adapter는 외부 예외를 내부 예외로 변환한다.
- Adapter는 Infrastructure Layer에 위치한다.
- Adapter는 Domain Rule을 가지면 안 된다.

---

### [실무]

Inbound Adapter 예:

- REST Controller
- GraphQL Resolver
- Message Consumer
- Batch Scheduler
- CLI Command

Outbound Adapter 예:

- JPA Repository Adapter
- TossPaymentAdapter
- KakaoMapAdapter
- S3FileStorageAdapter
- RedisCacheAdapter
- KafkaMessagePublisherAdapter
- OpenAiSummaryAdapter

Adapter 책임:

| Adapter Type         | 책임                                            |
| -------------------- | ----------------------------------------------- |
| Web Adapter          | HTTP Request 변환, Use Case 호출, Response 변환 |
| Persistence Adapter  | DB 접근, Entity Mapping                         |
| External API Adapter | 외부 API 호출, 응답 변환                        |
| Message Adapter      | Message 발행/구독                               |
| File Adapter         | 파일 저장소 연동                                |

---

### [예제]

```java
@Component
public class KakaoMapAdapter implements LocationPort {
    private final KakaoMapClient kakaoMapClient;

    @Override
    public LocationResult search(String keyword) {
        KakaoMapResponse response = kakaoMapClient.search(keyword);

        return new LocationResult(
                response.firstLongitude(),
                response.firstLatitude()
        );
    }
}
```

---

### [Best Practice]

- Adapter는 외부 기술명을 포함해도 된다.
- 외부 DTO는 Adapter 내부에서 끝낸다.
- Adapter는 Port Interface를 구현한다.
- Adapter는 기술 예외를 Application Exception으로 변환한다.
- Adapter 단위 Integration Test를 작성한다.
- Adapter는 Config, Client, Mapper와 분리할 수 있다.

---

### [주의]

- Adapter가 비즈니스 로직을 가지면 Core Isolation이 깨진다.
- Adapter에서 외부 API DTO를 그대로 반환하지 않는다.
- Adapter가 커지면 Client, Mapper, ErrorHandler로 분리한다.
- Adapter가 Port 없이 Service에 직접 주입되면 Hexagonal 구조가 약해진다.
- Adapter가 Domain Entity를 외부로 직접 노출하지 않게 한다.

---

### [FAQ]

Q. Adapter는 무엇인가?

A. Port와 외부 기술을 연결하는 구현체이다.

Q. Adapter에는 어떤 로직을 넣는가?

A. 외부 호출, 요청 변환, 응답 변환, 예외 변환, 기술 설정 처리를 넣는다.

Q. Adapter에 비즈니스 로직을 넣어도 되는가?

A. 권장하지 않는다. 비즈니스 로직은 Application Core 또는 Domain에 둔다.

Q. Adapter 이름에는 외부 기술명을 넣어도 되는가?

A. 가능하다. 예를 들어 `TossPaymentAdapter`, `KakaoMapAdapter`는 적절하다.

---

## 3.4 Hexagonal Package Structure

### [개념]

Hexagonal Package Structure는 Port, Adapter, Application, Domain을 명확히 분리하여 의존성 방향을 관리하는 Package 구조이다.

Package 구조는 의존성 방향을 보조하는 수단이다.

```text
adapter
→ application
→ domain
```

---

### [핵심]

- Package 구조는 책임 분리를 명확히 한다.
- Application은 Use Case와 Port를 가진다.
- Domain은 핵심 비즈니스 모델과 규칙을 가진다.
- Adapter는 외부 기술 구현을 가진다.
- 의존성은 외부 Adapter에서 내부 Application/Domain으로 향한다.
- 내부 Core는 Adapter를 알지 않는다.

---

### [실무]

예시 구조:

```text
com.example.order
├ application
│ ├ port
│ │ ├ in
│ │ │ └ CreateOrderUseCase.java
│ │ └ out
│ │   └ PaymentPort.java
│ └ service
│   └ OrderApplicationService.java
├ domain
│ ├ model
│ │ └ Order.java
│ ├ policy
│ │ └ DiscountPolicy.java
│ └ event
│   └ OrderCompletedEvent.java
└ adapter
  ├ in
  │ └ web
  │   └ OrderController.java
  └ out
    ├ persistence
    │ └ OrderPersistenceAdapter.java
    └ payment
      └ TossPaymentAdapter.java
```

의존성 방향:

```text
OrderController
→ CreateOrderUseCase
→ OrderApplicationService
→ PaymentPort
← TossPaymentAdapter
```

---

### [Best Practice]

- Package는 기능 단위 또는 Domain 단위로 묶는다.
- Port는 Application Layer에 둔다.
- Adapter는 `adapter.in`, `adapter.out`으로 구분한다.
- Domain은 Spring Annotation 의존을 최소화한다.
- Application Service는 Use Case 중심으로 작성한다.
- 외부 기술 Config는 Adapter 영역에 둔다.

---

### [주의]

- Package 구조만 만들고 의존성 방향을 지키지 않으면 의미가 없다.
- Domain이 Adapter Class를 import하면 구조가 깨진다.
- Application Service가 외부 API Client를 직접 import하면 Port가 무력화된다.
- 지나치게 깊은 Package 구조는 탐색 비용을 높인다.
- 팀 내 Naming Convention이 없으면 혼란이 생긴다.

---

### [FAQ]

Q. Hexagonal Package Structure의 핵심은?

A. Application, Domain, Adapter를 분리하고 의존성 방향을 내부 Core로 향하게 하는 것이다.

Q. Port는 어느 Package에 두는가?

A. 일반적으로 Application Layer의 `port.in`, `port.out`에 둔다.

Q. Adapter는 어느 Package에 두는가?

A. 외부 입력은 `adapter.in`, 외부 출력은 `adapter.out`에 둔다.

Q. Package 구조만 Hexagonal이면 충분한가?

A. 아니다. 의존성 방향과 책임 분리를 실제 코드에서 지켜야 한다.

---

# 4. Clean Architecture

## 4.1 Clean Architecture

### [개념]

Clean Architecture는 핵심 비즈니스 규칙을 Framework, Database, UI, External System으로부터 독립시키는 Architecture Pattern이다.

Clean Architecture의 핵심은 Dependency Rule이다.

```text
Framework / UI / DB
→ Interface Adapter
→ Use Case
→ Entity / Domain
```

---

### [핵심]

- Clean Architecture는 Domain Isolation을 목표로 한다.
- Dependency Rule은 의존성이 바깥에서 안쪽으로만 향해야 한다는 규칙이다.
- 내부 계층은 외부 계층을 알면 안 된다.
- Entity와 Use Case가 핵심이다.
- Framework와 Database는 세부사항으로 취급한다.
- 테스트 가능한 구조를 만든다.
- 대규모 장기 유지보수 프로젝트에 적합하다.

---

### [실무]

Clean Architecture 계층:

| Layer                  | 역할                                   |
| ---------------------- | -------------------------------------- |
| Entity / Domain        | 핵심 비즈니스 규칙                     |
| Use Case / Application | 애플리케이션 유스케이스                |
| Interface Adapter      | Controller, Presenter, Gateway, Mapper |
| Framework / Driver     | Spring, DB, Web, External API          |

Spring Boot에서는 완전한 Clean Architecture보다 핵심 원칙을 부분 적용하는 경우가 많다.

적용 예:

- Domain이 Spring Web을 모르게 한다.
- Use Case가 외부 API Client를 직접 모르게 한다.
- Controller DTO와 Domain Model을 분리한다.
- DB Entity와 Domain Model을 분리할지 검토한다.
- 외부 시스템은 Adapter와 Port로 격리한다.

---

### [예제]

의존성 방향:

```text
OrderController
→ CreateOrderUseCase
→ OrderDomainService
→ Order

TossPaymentAdapter
→ PaymentPort
← CreateOrderUseCase
```

Use Case Interface:

```java
public interface CreateOrderUseCase {
    OrderResult create(CreateOrderCommand command);
}
```

Use Case Implementation:

```java
@Service
public class CreateOrderService implements CreateOrderUseCase {
    private final OrderRepositoryPort orderRepositoryPort;
    private final PaymentPort paymentPort;

    public OrderResult create(CreateOrderCommand command) {
        Order order = Order.create(command.userId(), command.amount());
        PaymentResult paymentResult = paymentPort.pay(command.toPaymentCommand());

        order.completePayment(paymentResult.paymentKey());
        orderRepositoryPort.save(order);

        return OrderResult.from(order);
    }
}
```

---

### [Best Practice]

- Domain은 Framework 의존을 최소화한다.
- Use Case는 Application 정책과 흐름을 담당한다.
- 외부 시스템은 Interface Adapter로 격리한다.
- DTO와 Domain Model을 구분한다.
- Dependency Rule을 Code Review 기준으로 사용한다.
- 테스트에서 외부 DB/API 없이 Use Case를 검증할 수 있게 한다.
- Clean Architecture는 핵심 Domain부터 점진 적용한다.

---

### [주의]

- 모든 프로젝트에 완전한 Clean Architecture가 필요한 것은 아니다.
- DB Entity와 Domain Model을 완전히 분리하면 Mapping 비용이 증가한다.
- 계층이 많아져 단순 기능 개발 속도가 느려질 수 있다.
- Framework를 완전히 배제하려다 실무 생산성이 떨어질 수 있다.
- Clean Architecture의 핵심은 폴더명이 아니라 Dependency Rule이다.

---

### [FAQ]

Q. Clean Architecture는 무엇인가?

A. 핵심 비즈니스 규칙을 Framework, Database, UI, External System으로부터 독립시키는 Architecture Pattern이다.

Q. Clean Architecture의 핵심 규칙은?

A. Dependency Rule이다. 의존성은 바깥 계층에서 안쪽 계층으로만 향해야 한다.

Q. Clean Architecture는 언제 적합한가?

A. Domain이 복잡하고 장기 유지보수와 테스트 격리가 중요한 프로젝트에 적합하다.

Q. Spring Boot에서 Clean Architecture를 완전히 적용해야 하는가?

A. 반드시 그렇지는 않다. 필요한 영역에 핵심 원칙을 부분 적용하는 방식도 실무적이다.

---

## 4.2 Dependency Rule

### [개념]

Dependency Rule은 Clean Architecture에서 의존성이 외부 계층에서 내부 계층으로만 향해야 한다는 규칙이다.

내부 Domain과 Use Case는 Framework, Database, UI, 외부 API를 직접 알면 안 된다.

```text
Outer Layer
→ Inner Layer

Inner Layer
X Outer Layer
```

---

### [핵심]

- Dependency Rule은 Clean Architecture의 핵심이다.
- Domain은 Application, Adapter, Framework를 몰라야 한다.
- Use Case는 Controller나 DB 구현체를 몰라야 한다.
- Adapter는 Use Case Interface를 호출하거나 Port를 구현한다.
- 외부 기술 변경이 내부 정책으로 전파되지 않아야 한다.
- DIP를 사용해 의존성 방향을 제어한다.

---

### [실무]

위반 예:

```java
public class OrderService {
    private final TossPaymentClient tossPaymentClient;
}
```

문제:

- Use Case가 외부 결제 Client를 직접 안다.
- 결제 Provider 변경 시 Use Case 수정이 필요하다.

개선:

```java
public class OrderService {
    private final PaymentPort paymentPort;
}
```

```text
OrderService
→ PaymentPort
← TossPaymentAdapter
→ TossPaymentClient
```

---

### [Best Practice]

- 내부 계층은 Interface에 의존한다.
- 외부 구현체는 내부 Interface를 구현한다.
- Domain에는 Spring Web, HTTP, DB Client 의존을 넣지 않는다.
- Use Case에는 외부 API DTO를 넣지 않는다.
- Adapter에서 외부 기술과 내부 모델을 변환한다.
- Dependency Direction을 Package Import 기준으로 검수한다.

---

### [주의]

- DI를 사용한다고 자동으로 Dependency Rule이 지켜지는 것은 아니다.
- 구현체에 직접 의존하면 DI를 써도 위반이다.
- Domain Entity가 JPA Annotation을 가지는 것이 항상 금지는 아니지만 순수 Domain 모델과는 거리가 있다.
- 실무에서는 순수성보다 비용 대비 효과를 판단한다.
- Dependency Rule 위반은 시간이 지날수록 변경 비용을 키운다.

---

### [FAQ]

Q. Dependency Rule은 무엇인가?

A. 의존성이 바깥 계층에서 안쪽 계층으로만 향해야 한다는 Clean Architecture의 핵심 규칙이다.

Q. Domain이 외부 기술을 알면 왜 문제인가?

A. 외부 기술 변경이 핵심 비즈니스 규칙 변경으로 전파되기 때문이다.

Q. DI를 쓰면 Dependency Rule이 자동으로 지켜지는가?

A. 아니다. Interface가 아니라 구현체에 직접 의존하면 위반이다.

Q. Dependency Rule은 어떻게 검수하는가?

A. 내부 계층의 import가 외부 Adapter, Web, DB, API 구현체를 참조하는지 확인한다.

---

## 4.3 Domain Isolation

### [개념]

Domain Isolation은 핵심 Domain Model과 Domain Rule을 외부 기술, Framework, UI, Database 변경으로부터 보호하는 설계 원칙이다.

Domain Isolation은 Clean Architecture와 Hexagonal Architecture의 핵심 목표이다.

```text
Domain Rule
→ Protected From
→ Web / DB / External API / Framework
```

---

### [핵심]

- Domain은 핵심 비즈니스 의미와 규칙을 가진다.
- Domain은 외부 API DTO에 의존하지 않는다.
- Domain은 Controller Request DTO에 의존하지 않는다.
- Domain Rule은 Service나 Controller에 흩어지면 안 된다.
- Domain Isolation은 테스트와 유지보수성을 높인다.
- Domain이 단순하면 과도한 분리가 필요하지 않을 수 있다.

---

### [실무]

Domain Rule 예:

- 주문은 결제 완료 전 배송 시작할 수 없다.
- 완료된 주문은 취소할 수 없다.
- 축제 종료일은 시작일보다 빠를 수 없다.
- 리뷰 평점은 0~5 범위를 가진다.
- 후원 금액은 0보다 커야 한다.
- 알림 예약 시간은 현재보다 미래여야 한다.

나쁜 예:

```java
if (festival.getEndDate().isBefore(festival.getStartDate())) {
    throw new IllegalArgumentException();
}
```

위 검증이 Controller, Service, DTO Mapper에 흩어져 있으면 Domain Rule 추적이 어렵다.

좋은 방향:

```java
public class Festival {
    public Festival(LocalDate startDate, LocalDate endDate) {
        validatePeriod(startDate, endDate);
        this.startDate = startDate;
        this.endDate = endDate;
    }

    private void validatePeriod(LocalDate startDate, LocalDate endDate) {
        if (endDate.isBefore(startDate)) {
            throw new IllegalArgumentException("축제 종료일은 시작일보다 빠를 수 없습니다.");
        }
    }
}
```

---

### [Best Practice]

- Domain Rule은 Domain Entity, Value Object, Domain Service에 둔다.
- 외부 DTO는 Application Layer에서 Domain Command로 변환한다.
- Domain 객체는 의미 있는 Method로 상태를 변경한다.
- Setter 남용을 줄인다.
- Domain Test는 Spring 없이 실행 가능하게 설계한다.
- 핵심 Domain부터 Isolation을 적용한다.

---

### [주의]

- JPA Entity를 Domain Model로 사용하는 경우 Persistence Annotation 의존이 생긴다.
- 순수 Domain Model과 JPA Entity를 분리하면 Mapping 비용이 증가한다.
- 단순 CRUD에서는 Domain Isolation을 과하게 적용하지 않아도 된다.
- 모든 검증을 Domain에 넣으면 외부 입력 검증과 Domain Rule이 섞일 수 있다.
- Request 형식 검증은 DTO, 핵심 규칙 검증은 Domain으로 구분한다.

---

### [FAQ]

Q. Domain Isolation은 무엇인가?

A. 핵심 Domain Model과 Domain Rule을 외부 기술과 UI, DB 변경으로부터 보호하는 설계 원칙이다.

Q. Domain Rule은 어디에 두는 것이 좋은가?

A. Domain Entity, Value Object, Domain Service에 두는 것이 좋다.

Q. DTO 검증과 Domain Rule 검증은 어떻게 다른가?

A. DTO 검증은 입력 형식 검증이고 Domain Rule 검증은 비즈니스 불변식 검증이다.

Q. JPA Entity를 Domain Model로 써도 되는가?

A. 가능하다. 다만 순수 Domain Isolation은 약해질 수 있으므로 프로젝트 규모에 맞게 판단한다.

---

# 5. Architecture Pattern Comparison

## 5.1 Layered vs Hexagonal vs Clean Architecture

### [개념]

Layered Architecture, Hexagonal Architecture, Clean Architecture는 모두 시스템 구조를 설계하지만 목적과 복잡도가 다르다.

- Layered Architecture는 계층별 책임 분리에 집중한다.
- Hexagonal Architecture는 Port와 Adapter로 외부 시스템을 격리한다.
- Clean Architecture는 Dependency Rule로 핵심 Domain을 보호한다.

---

### [핵심]

| Architecture           | 핵심 목적        | 주요 키워드                       | 적합 상황                         |
| ---------------------- | ---------------- | --------------------------------- | --------------------------------- |
| Layered Architecture   | 계층 분리        | Controller, Service, Repository   | 단순 CRUD, 일반 Spring Boot       |
| Hexagonal Architecture | 외부 시스템 격리 | Port, Adapter                     | 외부 API, 결제, 알림, 저장소 교체 |
| Clean Architecture     | Domain Isolation | Dependency Rule, Use Case, Entity | 복잡한 Domain, 장기 유지보수      |

---

### [Comparison]

```text
Layered
→ Controller → Service → Repository

Hexagonal
→ Adapter → Port → Application Core

Clean
→ Framework → Interface Adapter → Use Case → Domain
```

선택 기준:

| 질문                                          | 적합 구조         |
| --------------------------------------------- | ----------------- |
| 단순 CRUD인가?                                | Layered           |
| 외부 시스템 교체 가능성이 큰가?               | Hexagonal         |
| Domain Rule이 복잡한가?                       | Clean             |
| 테스트에서 외부 API를 쉽게 대체해야 하는가?   | Hexagonal         |
| Framework 변경과 무관한 핵심 정책이 중요한가? | Clean             |
| 팀원이 단순 구조를 선호하는가?                | Layered           |
| 장기 유지보수 시스템인가?                     | Clean / Hexagonal |

---

### [실무]

현실적인 Spring Boot 적용 방식:

```text
기본 구조
→ Layered Architecture

외부 API 연동 영역
→ Adapter 적용

교체 가능성이 높은 의존성
→ Port 적용

복잡한 Domain Rule
→ Domain Entity / Value Object / Domain Service 분리

대규모 확장
→ Hexagonal / Clean Architecture 점진 적용
```

---

### [주의]

- Architecture는 한 번에 완벽하게 적용하지 않아도 된다.
- Layered에서 Hexagonal로 부분 전환할 수 있다.
- Clean Architecture를 적용해도 Framework를 완전히 제거할 필요는 없다.
- 계층이 많아질수록 개발 속도와 이해 비용이 증가한다.
- 단순한 기능에는 단순한 구조가 더 좋다.

---

### [FAQ]

Q. Layered와 Hexagonal의 차이는?

A. Layered는 계층 분리에 집중하고 Hexagonal은 Port와 Adapter로 외부 시스템을 격리한다.

Q. Hexagonal과 Clean Architecture의 차이는?

A. Hexagonal은 외부 입출력 경계 분리에 집중하고 Clean Architecture는 Dependency Rule과 Domain Isolation에 더 집중한다.

Q. Spring Boot에서는 어떤 Architecture가 가장 현실적인가?

A. 기본은 Layered로 시작하고 외부 연동과 핵심 Domain에 Hexagonal 또는 Clean 원칙을 부분 적용하는 방식이 현실적이다.

Q. Architecture Pattern을 섞어도 되는가?

A. 가능하다. 실무에서는 Layered 기반에 Adapter, Port, Domain Isolation을 점진적으로 섞는 경우가 많다.

---

# 6. Architecture Review Checklist

## 6.1 Architecture Review

### [개념]

Architecture Review는 시스템 구조가 책임 분리, 의존성 방향, 외부 시스템 격리, Domain Isolation을 적절히 만족하는지 검수하는 과정이다.

Review Agent는 Architecture Pattern 문서를 기준으로 구조 문제를 찾고 개선 방향을 제안한다.

```text
Code Structure
→ Layer Responsibility Review
→ Dependency Direction Review
→ External Dependency Review
→ Domain Isolation Review
→ Refactoring Suggestion
```

---

### [핵심]

- Layer Responsibility가 지켜지는지 확인한다.
- Service가 God Service가 되었는지 확인한다.
- 외부 API Client가 Service에 직접 들어왔는지 확인한다.
- Domain이 외부 DTO에 의존하는지 확인한다.
- Port와 Adapter가 내부 요구사항 기준으로 설계되었는지 확인한다.
- Dependency Rule 위반을 import 기준으로 검수한다.
- Over Engineering 여부도 함께 검수한다.

---

### [Checklist]

Layered Architecture Checklist:

- Controller가 얇은가?
- Controller가 Repository를 직접 호출하지 않는가?
- Service가 Use Case 중심인가?
- Repository에 비즈니스 정책이 들어가지 않았는가?
- DTO와 Entity가 분리되었는가?
- Transaction Boundary가 적절한가?

God Service Checklist:

- 하나의 Service에 변경 이유가 여러 개인가?
- 검증, 계산, 외부 호출, 저장, 알림이 한 Method에 섞였는가?
- if / switch 정책 분기가 과도한가?
- 외부 API Client를 직접 호출하는가?
- 테스트 단위가 너무 큰가?

Hexagonal Checklist:

- 외부 시스템 호출이 Adapter로 분리되었는가?
- Application Service가 Port에 의존하는가?
- Adapter가 Port를 구현하는가?
- Port 이름이 외부 기술에 종속되지 않는가?
- 외부 DTO가 Application Core로 침투하지 않는가?
- Adapter에 비즈니스 로직이 들어가지 않았는가?

Clean Architecture Checklist:

- 의존성이 내부 방향으로 향하는가?
- Domain이 Framework, Web, DB 구현체를 모르는가?
- Use Case가 Controller DTO를 직접 사용하지 않는가?
- Domain Rule이 Controller나 Adapter에 흩어져 있지 않은가?
- 외부 기술 변경이 Domain Rule 변경으로 이어지지 않는가?

Over Engineering Checklist:

- 단순 CRUD에 Port와 Adapter가 과도하게 많지 않은가?
- Interface가 실제 교체 가능성 없이 만들어졌는가?
- Package 구조가 팀 이해도를 넘어서 복잡하지 않은가?
- 테스트 가치보다 구조 비용이 더 크지 않은가?

---

### [실무]

Review 결과 형식:

```text
문제:
OrderService가 TossPaymentClient에 직접 의존한다.

원인:
Application Service가 Infrastructure 구현체를 직접 참조하여 DIP와 Dependency Rule을 위반한다.

해결:
PaymentPort를 정의하고 TossPaymentAdapter가 이를 구현하도록 분리한다.

관련 Pattern:
Hexagonal Architecture, Adapter Pattern, DIP
```

```text
문제:
단순 조회 API에 Repository Port, Persistence Adapter, Mapper가 과도하게 분리되어 있다.

원인:
변경 가능성이 낮은 단순 CRUD에 Hexagonal 구조를 과도하게 적용했다.

해결:
단순 조회는 Layered 구조로 유지하고 외부 연동 또는 핵심 Domain에만 Port를 적용한다.

관련 문제:
Over Engineering
```

---

### [FAQ]

Q. Architecture Review는 무엇을 확인하는가?

A. 책임 분리, 의존성 방향, 외부 시스템 격리, Domain Isolation, Over Engineering 여부를 확인한다.

Q. Review Agent는 무엇을 우선 검수해야 하는가?

A. God Service, 외부 Client 직접 의존, Domain Rule 분산, Dependency Rule 위반을 우선 검수한다.

Q. Architecture Review 결과는 어떤 형식이 좋은가?

A. 문제, 원인, 해결, 관련 Pattern 형식이 좋다.

Q. Over Engineering도 Architecture 문제인가?

A. 그렇다. 구조가 과도하면 유지보수성과 개발 속도를 해칠 수 있다.

---

# 7. Troubleshooting

## 7.1 Layer Violation

### [개념]

Layer Violation은 각 계층이 자신의 책임을 벗어나 다른 계층의 책임을 수행하거나 잘못된 방향으로 의존하는 문제이다.

---

### [핵심]

- Controller가 Repository를 직접 호출하면 Layer Violation이다.
- Repository가 비즈니스 정책을 판단하면 Layer Violation 가능성이 있다.
- Entity가 외부 API DTO를 알면 Layer Violation이다.
- Service가 HTTP Request 객체에 강하게 의존하면 Layer 경계가 흐려진다.
- Layer Violation은 변경 영향과 테스트 어려움을 증가시킨다.

---

### [Troubleshooting]

문제:

- Controller에서 DB 저장을 직접 수행한다.
- Repository Query에 할인 정책이 들어간다.
- Service가 `HttpServletRequest`를 깊게 사용한다.
- Entity가 Response DTO를 생성한다.
- Domain 객체가 외부 API Client를 호출한다.

원인:

- Layer Responsibility가 정의되지 않았다.
- 빠른 구현을 위해 가까운 위치에 로직을 넣었다.
- DTO, Mapper, Service 책임 구분이 없다.
- 외부 연동 경계가 없다.

해결:

- Controller 로직을 Service로 이동한다.
- 비즈니스 정책은 Domain Service 또는 Policy로 분리한다.
- 외부 의존은 Adapter로 분리한다.
- DTO 변환 위치를 일관되게 정한다.
- Layer Responsibility 문서를 기준으로 Code Review한다.

---

### [FAQ]

Q. Layer Violation은 무엇인가?

A. 계층이 자신의 책임을 벗어나 다른 계층의 역할을 수행하거나 잘못된 방향으로 의존하는 문제이다.

Q. Controller가 Repository를 직접 호출하면 왜 문제인가?

A. HTTP 처리 계층이 Persistence 계층에 직접 결합되어 Use Case 책임이 사라지기 때문이다.

Q. Repository에 비즈니스 정책을 넣어도 되는가?

A. 권장하지 않는다. Repository는 Persistence 접근에 집중해야 한다.

Q. Layer Violation을 줄이는 방법은?

A. Layer Responsibility를 명확히 하고 Controller, Service, Repository, Domain 책임을 분리한다.

---

## 7.2 Broken Dependency Direction

### [개념]

Broken Dependency Direction은 의존성이 내부 핵심 정책에서 외부 기술 구현체로 향하여 Dependency Rule 또는 DIP가 깨지는 문제이다.

---

### [핵심]

- Application Core가 Adapter를 직접 import하면 의존성 방향이 깨진다.
- Domain이 Framework 또는 External API를 알면 Domain Isolation이 깨진다.
- 구현체 직접 의존은 교체 가능성과 테스트 용이성을 낮춘다.
- Port와 Adapter를 사용해 의존성 방향을 역전할 수 있다.
- Broken Dependency Direction은 장기 유지보수 비용을 증가시킨다.

---

### [Troubleshooting]

문제:

- Use Case가 `TossPaymentClient`를 직접 사용한다.
- Domain Service가 `RestTemplate`, `WebClient`를 직접 사용한다.
- Domain Entity가 외부 API Response DTO를 필드로 가진다.
- Application Service가 Adapter Package Class를 import한다.
- 테스트에서 외부 API 없이 Use Case를 검증할 수 없다.

원인:

- DIP를 적용하지 않았다.
- Port Interface가 없다.
- 외부 기술 경계를 Adapter로 분리하지 않았다.
- 내부 요구사항보다 외부 API 스펙을 기준으로 설계했다.

해결:

- 내부가 필요로 하는 Port를 정의한다.
- 외부 구현체는 Adapter로 분리하고 Port를 구현한다.
- Application Service는 Port에만 의존한다.
- 외부 DTO는 Adapter 내부에서 내부 모델로 변환한다.
- Package Import 기준으로 의존성 방향을 검수한다.

---

### [FAQ]

Q. Broken Dependency Direction은 무엇인가?

A. 내부 핵심 정책이 외부 기술 구현체에 직접 의존하여 의존성 방향이 깨진 문제이다.

Q. Broken Dependency Direction은 왜 위험한가?

A. 외부 기술 변경이 핵심 비즈니스 코드 변경으로 전파되고 테스트 격리가 어려워지기 때문이다.

Q. 해결 방법은?

A. Port를 정의하고 Adapter가 Port를 구현하도록 하여 내부가 외부 구현체에 직접 의존하지 않게 한다.

Q. DI를 쓰면 Broken Dependency Direction이 해결되는가?

A. 아니다. 구현체에 직접 의존하면 DI를 사용해도 의존성 방향은 깨질 수 있다.

---

## 7.3 Over Engineering Architecture

### [개념]

Over Engineering Architecture는 프로젝트 복잡도에 비해 과도한 Architecture Pattern, 계층, Interface, Adapter를 적용하여 개발 속도와 유지보수성을 떨어뜨리는 문제이다.

---

### [핵심]

- Architecture는 문제 해결을 위한 수단이다.
- 단순 기능에 과도한 계층을 만들면 이해 비용이 증가한다.
- Interface와 Port는 실제 교체 가능성 또는 테스트 가치가 있을 때 유용하다.
- Clean Architecture 전체 적용은 비용이 크다.
- 단순한 구조가 더 좋은 설계일 수 있다.

---

### [Troubleshooting]

문제:

- 단순 조회 API에 UseCase, Port, Adapter, Mapper가 과도하게 많다.
- 구현체가 하나뿐인데 Interface가 모든 Service마다 있다.
- Package 구조가 깊어 파일 탐색이 어렵다.
- 기능 추가보다 구조 수정에 시간이 더 걸린다.
- 팀원이 Architecture를 이해하지 못한다.

원인:

- Pattern을 학습 목적으로 과도하게 적용했다.
- 미래 확장을 과도하게 예측했다.
- 프로젝트 규모와 일정, 팀 역량을 고려하지 않았다.
- Layered Architecture를 나쁜 구조로 오해했다.
- 모든 외부 의존성을 동일한 수준으로 추상화했다.

해결:

- 단순 CRUD는 Layered Architecture로 유지한다.
- 외부 시스템, 핵심 Domain, 교체 가능성이 높은 영역에만 Port를 적용한다.
- Interface는 변경 가능성, 테스트 필요성, 구현체 다양성이 있을 때 만든다.
- Package Depth를 줄인다.
- Architecture Decision Record로 적용 이유를 남긴다.
- 불필요한 Abstraction을 제거한다.

---

### [FAQ]

Q. Over Engineering Architecture는 무엇인가?

A. 프로젝트 문제에 비해 과도한 계층, Interface, Architecture Pattern을 적용해 복잡도를 높이는 문제이다.

Q. 모든 Service에 Interface를 만들어야 하는가?

A. 아니다. 교체 가능성, 테스트 필요성, 구현체 다양성이 있을 때 우선 검토한다.

Q. 단순 CRUD에도 Clean Architecture가 필요한가?

A. 보통은 필요하지 않다. Layered Architecture가 더 적합할 수 있다.

Q. Over Engineering을 줄이는 기준은?

A. 현재 문제, 변경 가능성, 테스트 가치, 팀 이해도, 일정 비용을 기준으로 판단한다.

---

## 7.4 Domain Leakage

### [개념]

Domain Leakage는 핵심 Domain Rule과 Domain Model이 Controller, DTO, Repository, Adapter, 외부 API 구조에 흩어져 Domain Isolation이 깨지는 문제이다.

---

### [핵심]

- Domain Rule은 한 곳에서 추적 가능해야 한다.
- Controller에 Domain Rule이 있으면 재사용과 테스트가 어렵다.
- 외부 API DTO가 Domain으로 침투하면 외부 변경에 취약하다.
- Repository Query에 정책이 과도하게 들어가면 Domain 의미가 흐려진다.
- Domain Leakage는 Clean Architecture와 Hexagonal Architecture에서 중요한 검수 대상이다.

---

### [Troubleshooting]

문제:

- 축제 기간 검증이 Controller, Service, DTO Mapper에 흩어져 있다.
- 외부 API의 `mapX`, `mapY` 이름이 Domain Model까지 들어온다.
- Order 상태 전이 규칙이 여러 Service에 중복된다.
- Review 평점 범위 검증이 DB Constraint에만 의존한다.
- Domain Entity가 Response DTO 생성 책임을 가진다.

원인:

- Domain Rule 위치를 정하지 않았다.
- 빠른 구현을 위해 입력 계층에 규칙을 넣었다.
- DTO와 Domain Model을 구분하지 않았다.
- 외부 API 응답 구조를 내부 모델로 변환하지 않았다.
- Domain Method를 만들지 않고 Setter로 상태를 변경했다.

해결:

- 핵심 Domain Rule은 Entity, Value Object, Domain Service로 이동한다.
- 외부 DTO는 Adapter에서 내부 모델로 변환한다.
- 상태 변경은 의미 있는 Domain Method로 캡슐화한다.
- DTO 검증과 Domain Rule 검증을 구분한다.
- 중복된 Domain Rule을 하나의 정책 객체로 통합한다.

---

### [FAQ]

Q. Domain Leakage는 무엇인가?

A. 핵심 Domain Rule과 Domain Model이 외부 계층이나 DTO, Adapter에 흩어져 Domain Isolation이 깨지는 문제이다.

Q. Domain Leakage는 왜 문제인가?

A. 핵심 규칙 추적이 어렵고 외부 변경이 Domain 변경으로 전파되기 때문이다.

Q. Domain Rule은 어디에 둬야 하는가?

A. Entity, Value Object, Domain Service, Policy 객체에 두는 것이 좋다.

Q. 외부 API 필드명이 Domain에 들어오면 왜 문제인가?

A. 외부 API 스펙 변경이 내부 Domain Model 변경으로 이어질 수 있기 때문이다.

---

# Retrieval Queries

### [FAQ]

Q. Architecture Pattern이란?
A. 애플리케이션 전체 구조, 책임 분리, 의존성 방향을 설계하는 대규모 Design Pattern이다.

Q. Architecture Pattern은 Class Design Pattern과 무엇이 다른가?
A. Class Design Pattern은 객체 단위 문제를 해결하고 Architecture Pattern은 시스템 구조 문제를 해결한다.

Q. Spring Boot에서 기본으로 많이 쓰는 구조는?
A. Controller, Service, Repository 중심의 Layered Architecture를 많이 사용한다.

Q. Architecture Pattern 선택 기준은?
A. 프로젝트 규모, Domain 복잡도, 외부 시스템 연동, 테스트 격리, 유지보수 기간을 기준으로 선택한다.

Q. Layered Architecture란?
A. 애플리케이션을 Controller, Service, Repository 같은 계층별 책임으로 분리하는 구조이다.

Q. Layered Architecture의 장점은?
A. 단순하고 이해하기 쉬우며 Spring Boot CRUD 프로젝트에 적합하다.

Q. Layered Architecture의 단점은?
A. Service가 비대해지기 쉽고 외부 시스템 교체나 Domain Isolation에는 약할 수 있다.

Q. Controller의 책임은?
A. HTTP 요청 처리, Parameter Binding, Service 호출, Response 반환이다.

Q. Service의 책임은?
A. Use Case 흐름, Transaction, 비즈니스 로직 조합을 담당한다.

Q. Repository의 책임은?
A. Entity 저장, 조회, Query Method, JPQL, QueryDSL 등 Persistence 접근이다.

Q. Controller가 Repository를 직접 호출하면 왜 문제인가?
A. HTTP 처리 계층이 Persistence 계층에 직접 결합되어 Use Case 책임이 사라지기 때문이다.

Q. God Service란?
A. 하나의 Service가 너무 많은 책임을 담당하여 변경과 테스트가 어려운 상태이다.

Q. God Service는 어떻게 분리하는가?
A. Validator, Policy, Strategy, Adapter, Event Listener, Facade 등으로 책임을 분리한다.

Q. Hexagonal Architecture란?
A. Application Core를 중심에 두고 외부 시스템을 Port와 Adapter로 분리하는 Architecture Pattern이다.

Q. Hexagonal Architecture의 다른 이름은?
A. Ports and Adapters Architecture이다.

Q. Hexagonal Architecture의 장점은?
A. 외부 시스템 교체, 테스트 격리, Domain Isolation에 유리하다.

Q. Hexagonal Architecture는 언제 적용하는가?
A. 외부 API, 결제, 알림, 파일 저장소, 메시지 브로커처럼 교체 가능성이 높은 영역에 적용한다.

Q. Port란?
A. Application Core가 외부 시스템과 상호작용하기 위해 정의하는 Interface이다.

Q. Adapter란?
A. Port와 외부 기술을 연결하는 구현체이다.

Q. Inbound Port와 Outbound Port의 차이는?
A. Inbound Port는 외부가 Application을 호출하는 Use Case Interface이고 Outbound Port는 Application이 외부 시스템을 호출하는 Interface이다.

Q. Port 이름에 외부 기술명을 넣어도 되는가?
A. 권장하지 않는다. Port는 내부 기능 기준으로 이름을 짓고 외부 기술명은 Adapter 이름에 둔다.

Q. Adapter 이름에는 외부 기술명을 넣어도 되는가?
A. 가능하다. `TossPaymentAdapter`, `KakaoMapAdapter`, `S3FileStorageAdapter`는 적절하다.

Q. Port에 외부 API Response DTO를 반환해도 되는가?
A. 권장하지 않는다. 내부 Result 객체로 변환해서 반환해야 한다.

Q. Adapter에 비즈니스 로직을 넣어도 되는가?
A. 권장하지 않는다. 비즈니스 로직은 Application Core 또는 Domain에 둔다.

Q. Hexagonal Package Structure의 핵심은?
A. Application, Domain, Adapter를 분리하고 의존성 방향을 내부 Core로 향하게 하는 것이다.

Q. Clean Architecture란?
A. 핵심 비즈니스 규칙을 Framework, Database, UI, External System으로부터 독립시키는 Architecture Pattern이다.

Q. Clean Architecture의 핵심 규칙은?
A. Dependency Rule이다. 의존성은 바깥 계층에서 안쪽 계층으로만 향해야 한다.

Q. Clean Architecture는 언제 적합한가?
A. Domain이 복잡하고 장기 유지보수와 테스트 격리가 중요한 프로젝트에 적합하다.

Q. Dependency Rule이란?
A. 의존성이 바깥 계층에서 안쪽 계층으로만 향해야 한다는 Clean Architecture의 핵심 규칙이다.

Q. DI를 쓰면 Dependency Rule이 자동으로 지켜지는가?
A. 아니다. Interface가 아니라 구현체에 직접 의존하면 위반이다.

Q. Domain Isolation이란?
A. 핵심 Domain Model과 Domain Rule을 외부 기술과 UI, DB 변경으로부터 보호하는 설계 원칙이다.

Q. Domain Rule은 어디에 두는 것이 좋은가?
A. Domain Entity, Value Object, Domain Service, Policy 객체에 두는 것이 좋다.

Q. DTO 검증과 Domain Rule 검증은 어떻게 다른가?
A. DTO 검증은 입력 형식 검증이고 Domain Rule 검증은 비즈니스 불변식 검증이다.

Q. Layered와 Hexagonal의 차이는?
A. Layered는 계층 분리에 집중하고 Hexagonal은 Port와 Adapter로 외부 시스템을 격리한다.

Q. Hexagonal과 Clean Architecture의 차이는?
A. Hexagonal은 외부 입출력 경계 분리에 집중하고 Clean Architecture는 Dependency Rule과 Domain Isolation에 더 집중한다.

Q. Spring Boot에서는 어떤 Architecture가 현실적인가?
A. 기본은 Layered로 시작하고 외부 연동과 핵심 Domain에 Hexagonal 또는 Clean 원칙을 부분 적용하는 방식이 현실적이다.

Q. Architecture Pattern을 섞어도 되는가?
A. 가능하다. 실무에서는 Layered 기반에 Adapter, Port, Domain Isolation을 점진적으로 섞는 경우가 많다.

Q. Architecture Review는 무엇을 확인하는가?
A. 책임 분리, 의존성 방향, 외부 시스템 격리, Domain Isolation, Over Engineering 여부를 확인한다.

Q. Review Agent는 무엇을 우선 검수해야 하는가?
A. God Service, 외부 Client 직접 의존, Domain Rule 분산, Dependency Rule 위반을 우선 검수한다.

Q. Layer Violation이란?
A. 계층이 자신의 책임을 벗어나 다른 계층의 역할을 수행하거나 잘못된 방향으로 의존하는 문제이다.

Q. Broken Dependency Direction이란?
A. 내부 핵심 정책이 외부 기술 구현체에 직접 의존하여 의존성 방향이 깨진 문제이다.

Q. Over Engineering Architecture란?
A. 프로젝트 문제에 비해 과도한 계층, Interface, Architecture Pattern을 적용해 복잡도를 높이는 문제이다.

Q. 모든 Service에 Interface를 만들어야 하는가?
A. 아니다. 교체 가능성, 테스트 필요성, 구현체 다양성이 있을 때 우선 검토한다.

Q. Domain Leakage란?
A. 핵심 Domain Rule과 Domain Model이 외부 계층이나 DTO, Adapter에 흩어져 Domain Isolation이 깨지는 문제이다.

Q. 외부 API 필드명이 Domain에 들어오면 왜 문제인가?
A. 외부 API 스펙 변경이 내부 Domain Model 변경으로 이어질 수 있기 때문이다.

Q. Backend Agent는 Architecture Pattern을 어떻게 사용해야 하는가?
A. 요구사항의 복잡도와 외부 의존성을 분석해 Layered, Hexagonal, Clean 원칙을 적절히 선택해야 한다.

Q. Review Agent는 Architecture Pattern을 어떻게 검수해야 하는가?
A. 계층 책임, 의존성 방향, Port/Adapter 설계, Domain Isolation, Over Engineering을 검수해야 한다.

Q. PM Agent는 Architecture Pattern 요구사항을 어떻게 분류해야 하는가?
A. 단순 CRUD, 외부 연동, Domain 복잡도, 장기 유지보수, Multi-Agent Workflow 관점으로 구조 요구를 분류해야 한다.
