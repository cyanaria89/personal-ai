# Design Pattern Part06 - Review & Troubleshooting

---

# 1. Design Pattern Review Overview

## 1.1 Design Pattern Review

### [개념]

Design Pattern Review는 코드와 아키텍처가 적절한 Pattern을 사용하고 있는지, Pattern을 잘못 적용하거나 과도하게 적용하지 않았는지 검수하는 과정이다.

Design Pattern Review는 Pattern 이름을 찾는 작업이 아니다.

Design Pattern Review는 문제, 책임, 변경 지점, 의존성, Trade-off를 기준으로 구조 품질을 판단하는 작업이다.

```text
Code Structure
→ Problem Review
→ Responsibility Review
→ Pattern Fit Review
→ Trade-off Review
→ Refactoring Suggestion
```

---

### [핵심]

- Design Pattern Review는 구조 품질 검수이다.
- Pattern 적용 여부보다 Pattern 적합성이 중요하다.
- Pattern을 사용하지 않는 것이 더 좋은 경우도 있다.
- Review 기준은 Problem, Pattern, Solution, Trade-off이다.
- SOLID 위반은 Pattern 검수의 핵심 신호이다.
- Over Engineering과 Tight Coupling을 함께 검수한다.
- Review Agent는 문제, 원인, 해결, 관련 Pattern 형식으로 결과를 작성한다.

---

### [실무]

2026 실무 기준 Java 21, Spring Boot 3.x Backend에서 Design Pattern Review는 다음 상황에서 수행한다.

- Service가 비대해졌을 때
- if / switch 조건문이 계속 증가할 때
- 외부 API Client가 Service에 직접 들어왔을 때
- Entity 상태 변경이 Setter로 흩어졌을 때
- Controller가 비즈니스 로직을 처리할 때
- Strategy, Factory, Adapter가 과도하게 늘어났을 때
- Transaction, AOP, Lazy Loading이 예상대로 동작하지 않을 때
- Event Listener가 많아져 흐름 추적이 어려울 때
- Architecture Package 구조가 복잡하지만 의존성 방향이 깨졌을 때

---

### [Review Output Format]

```text
문제:
OrderService가 TossPaymentClient에 직접 의존한다.

원인:
Application Service가 외부 Infrastructure 구현체를 직접 참조한다.
DIP와 Dependency Rule 위반 가능성이 있다.

해결:
PaymentPort를 정의하고 TossPaymentAdapter가 PaymentPort를 구현하도록 분리한다.
OrderService는 PaymentPort에만 의존하게 한다.

관련 Pattern:
Adapter Pattern, Hexagonal Architecture, DIP

주의:
단순 일회성 외부 호출이라면 과도한 Port 분리는 필요하지 않을 수 있다.
```

---

### [주의]

- Pattern 이름을 맞추기 위해 코드를 억지로 바꾸지 않는다.
- Review는 문제와 변경 가능성을 기준으로 한다.
- Pattern 적용 제안에는 반드시 Trade-off를 포함한다.
- 단순 CRUD에 복잡한 Architecture Pattern을 강제하지 않는다.
- 모든 if 문을 Strategy로 바꾸지 않는다.
- 모든 외부 의존성을 Port로 감싸지 않는다.

---

### [FAQ]

Q. Design Pattern Review는 무엇인가?

A. 코드 구조가 문제에 맞는 Pattern을 사용하고 있는지, Pattern 남용이나 구조 문제는 없는지 검수하는 과정이다.

Q. Design Pattern Review에서 가장 중요한 기준은?

A. 문제, 책임, 변경 지점, 의존성, Trade-off이다.

Q. Pattern을 사용하지 않는 것도 좋은 Review 결과인가?

A. 그렇다. 단순한 문제에는 단순한 구조가 더 좋은 설계일 수 있다.

Q. Review Agent는 어떤 형식으로 결과를 작성해야 하는가?

A. 문제, 원인, 해결, 관련 Pattern, 주의 형식으로 작성하는 것이 좋다.

---

## 1.2 Review Agent Decision Flow

### [개념]

Review Agent Decision Flow는 코드 구조를 검수할 때 어떤 순서로 판단해야 하는지 정의한 흐름이다.

Review Agent는 Pattern 적용을 바로 제안하지 않고 문제 유형을 먼저 분류해야 한다.

```text
Code Input
→ Responsibility Check
→ Dependency Check
→ Change Point Check
→ Pattern Fit Check
→ Over Engineering Check
→ Final Suggestion
```

---

### [핵심]

- 책임이 섞였는지 먼저 확인한다.
- 의존성 방향이 깨졌는지 확인한다.
- 변경 지점이 반복되는지 확인한다.
- Pattern 후보를 문제 유형별로 선택한다.
- Pattern 적용 비용과 복잡도를 검토한다.
- 기존 구조 유지가 더 나은지 판단한다.
- 최종 제안은 구체적인 Refactoring 단위로 작성한다.

---

### [실무]

Review Agent 판단 순서:

```text
1. 이 코드의 주 책임은 무엇인가?
2. 변경 이유가 몇 개인가?
3. 외부 기술 구현체에 직접 의존하는가?
4. 조건문이 정책 변경 때문에 증가하는가?
5. 객체 생성 책임이 적절한 위치에 있는가?
6. 이벤트 또는 후속 작업이 직접 결합되어 있는가?
7. 공통 흐름 중복이 있는가?
8. 요청을 저장, 재시도, 비동기 처리해야 하는가?
9. Pattern 적용이 현재 문제보다 과한가?
10. 가장 단순한 개선안은 무엇인가?
```

---

### [Pattern Candidate Mapping]

| 신호                                       | 검토 Pattern                         |
| ------------------------------------------ | ------------------------------------ |
| Service가 여러 책임을 가짐                 | SRP, Facade, Policy, Strategy        |
| 조건문으로 정책 선택                       | Strategy, Factory                    |
| 객체 생성 조건 복잡                        | Factory, Builder                     |
| 외부 API DTO가 Service에 침투              | Adapter, Hexagonal Architecture      |
| 기존 기능 전후 부가기능 필요               | Decorator, AOP, Proxy                |
| Transaction / Security / Lazy Loading 문제 | Proxy                                |
| 이벤트 후속 작업 직접 호출                 | Observer, Spring Event               |
| 공통 흐름 반복                             | Template Method                      |
| 요청 저장 / 재시도 / 큐 처리               | Command                              |
| 계층 책임 섞임                             | Layered Architecture Review          |
| 의존성 방향 깨짐                           | DIP, Dependency Rule                 |
| Domain Rule 흩어짐                         | Domain Isolation, Clean Architecture |

---

### [주의]

- Review Agent는 Pattern 후보를 복수로 제안할 수 있다.
- 단, 최종 추천은 현재 문제에 가장 단순한 해결책을 우선한다.
- Pattern을 제안할 때 “왜 이 Pattern인가”를 명확히 설명한다.
- Pattern을 적용하지 않는 선택도 명시할 수 있다.
- 과도한 추상화가 예상되면 단순 구조 유지를 권장한다.

---

### [FAQ]

Q. Review Agent는 무엇을 먼저 확인해야 하는가?

A. 책임 분리와 변경 이유를 먼저 확인해야 한다.

Q. Pattern 후보는 어떻게 선택하는가?

A. 생성, 구조, 행동, 아키텍처 문제 중 어디에 해당하는지 분류한 뒤 선택한다.

Q. Review Agent가 반드시 Pattern을 추천해야 하는가?

A. 아니다. 단순 구조 유지나 불필요한 Pattern 제거를 추천할 수도 있다.

Q. Review Agent가 Over Engineering을 판단하는 기준은?

A. 문제 복잡도보다 Interface, 계층, Adapter, Pattern 비용이 더 큰지 확인한다.

---

# 2. Common Design Smells

## 2.1 Pattern Abuse

### [개념]

Pattern Abuse는 필요하지 않은 곳에 Design Pattern을 과도하게 적용하여 코드 복잡도와 유지보수 비용을 증가시키는 문제이다.

Pattern Abuse는 Design Pattern 학습 초기에 자주 발생한다.

```text
Simple Problem
→ Complex Pattern
→ More Classes
→ Harder Maintenance
```

---

### [핵심]

- Pattern Abuse는 Over Engineering의 대표 원인이다.
- 단순 CRUD에 복잡한 Pattern을 강제하면 생산성이 떨어진다.
- Interface와 Class가 많아도 좋은 설계가 아닐 수 있다.
- Pattern 적용 이유가 설명되지 않으면 Pattern Abuse 가능성이 있다.
- 미래 확장을 과도하게 예측하면 Pattern Abuse가 발생한다.
- 불필요한 Pattern 제거도 Refactoring이다.

---

### [실무]

Pattern Abuse 신호:

- 구현체가 하나뿐인데 모든 Service에 Interface가 있다.
- 단순 조회 API에 UseCase, Port, Adapter, Mapper가 과도하게 분리되어 있다.
- 조건이 2개뿐인데 Strategy, Factory, Resolver가 모두 존재한다.
- DTO 필드가 2개인데 Builder를 강제한다.
- 외부 시스템 교체 가능성이 없는데 모든 Client를 Port로 감싼다.
- Pattern 이름은 있지만 실제 변경 비용 감소 효과가 없다.
- 새 기능 추가보다 구조 이해 시간이 더 오래 걸린다.

---

### [Troubleshooting]

문제:

- 코드 흐름이 파일 여러 개로 과도하게 분산된다.
- Class 수가 많지만 책임 차이가 작다.
- 단순 기능 개발에도 구조 수정이 많다.
- 팀원이 구조를 이해하지 못한다.

원인:

- Pattern을 학습 목적으로 억지 적용했다.
- SOLID를 형식적으로만 적용했다.
- 미래 요구사항을 과도하게 예측했다.
- 단순한 Layered Architecture를 나쁜 구조로 오해했다.

해결:

- 현재 요구사항 기준으로 단순화한다.
- 구현체가 하나이고 교체 가능성이 낮은 Interface를 제거한다.
- 단순 CRUD는 Layered 구조로 유지한다.
- 반복 변경이 확인된 지점에만 Pattern을 적용한다.
- Architecture Decision Record에 Pattern 적용 이유를 남긴다.

---

### [FAQ]

Q. Pattern Abuse는 무엇인가?

A. 필요하지 않은 곳에 Pattern을 과도하게 적용하여 코드 복잡도를 높이는 문제이다.

Q. Pattern Abuse를 줄이는 기준은?

A. 현재 문제, 변경 가능성, 테스트 가치, 팀 이해도, 일정 비용을 기준으로 판단한다.

Q. Pattern을 제거하는 것도 좋은 설계인가?

A. 그렇다. 불필요한 추상화를 제거하면 가독성과 유지보수성이 좋아질 수 있다.

Q. Pattern Abuse와 Over Engineering은 같은가?

A. Pattern Abuse는 Over Engineering의 한 유형이다.

---

## 2.2 Tight Coupling

### [개념]

Tight Coupling은 객체, Module, Layer가 서로 강하게 의존하여 변경, 테스트, 확장이 어려운 상태이다.

Tight Coupling은 Design Pattern이 해결하려는 대표적인 구조 문제이다.

```text
Module A
→ Concrete Module B
→ External System
→ Change Propagation
```

---

### [핵심]

- Tight Coupling은 변경 전파를 증가시킨다.
- Tight Coupling은 테스트 대체를 어렵게 만든다.
- Tight Coupling은 구현체 교체를 어렵게 만든다.
- 외부 API Client 직접 의존은 Tight Coupling 신호이다.
- 순환 의존은 강한 결합의 대표 신호이다.
- Adapter, Strategy, Port, Event로 결합도를 낮출 수 있다.

---

### [실무]

Tight Coupling 신호:

- Service가 외부 API Client를 직접 사용한다.
- Domain이 Controller DTO를 안다.
- Entity가 외부 API Response DTO를 필드로 가진다.
- A Service와 B Service가 서로 호출한다.
- Controller가 여러 Repository를 직접 호출한다.
- 테스트에서 Mock 또는 Fake로 대체하기 어렵다.
- 결제사 변경 시 여러 Use Case가 수정된다.

---

### [Troubleshooting]

문제:

- 외부 API 스펙 변경이 Service, DTO, Controller까지 전파된다.
- 결제 Provider 교체 시 기존 Use Case 수정이 크다.
- Unit Test가 외부 시스템에 의존한다.
- 순환 참조가 발생한다.

원인:

- Abstraction 없이 Concrete Class에 직접 의존한다.
- Port / Adapter 경계가 없다.
- 책임 분리가 부족하다.
- Event로 분리할 후속 작업을 직접 호출한다.

해결:

- 외부 시스템은 Adapter로 격리한다.
- Application Service는 Port에 의존한다.
- 정책 교체 지점은 Strategy로 분리한다.
- 후속 작업은 Observer 또는 Event로 분리한다.
- 순환 의존은 Mediator 또는 Application Service로 조정한다.

---

### [FAQ]

Q. Tight Coupling은 무엇인가?

A. 객체나 모듈이 강하게 의존하여 변경, 테스트, 확장이 어려운 상태이다.

Q. Tight Coupling의 대표 신호는?

A. 외부 Client 직접 의존, 순환 의존, 구현체 교체 어려움, 테스트 대체 어려움이다.

Q. Tight Coupling을 줄이는 Pattern은?

A. Adapter, Strategy, Observer, Mediator, Hexagonal Architecture가 도움이 된다.

Q. 모든 의존성을 제거해야 하는가?

A. 아니다. 변경 가능성이 높은 의존성과 외부 기술 의존성을 우선 분리한다.

---

## 2.3 Excessive Abstraction

### [개념]

Excessive Abstraction은 실제 변경 가능성이나 테스트 가치가 낮은 코드에 Interface, Abstract Class, Port, Adapter를 과도하게 적용하는 문제이다.

Excessive Abstraction은 코드 이해 비용을 높인다.

```text
Low Change Risk
→ Interface
→ Abstract Class
→ Factory
→ Adapter
→ High Complexity
```

---

### [핵심]

- Abstraction은 변경 가능성이 있을 때 가치가 크다.
- 이유 없는 Interface는 유지보수 비용이다.
- Abstract Class는 상속 결합을 만든다.
- Port는 외부 의존성 격리에 유용하지만 모든 객체에 필요하지 않다.
- 추상화는 테스트 가치와 교체 가능성을 기준으로 판단한다.
- 과도한 추상화는 오히려 코드 생성 Agent 성능을 떨어뜨릴 수 있다.

---

### [실무]

Excessive Abstraction 신호:

- Interface 구현체가 항상 하나뿐이다.
- Interface 이름과 구현체 이름이 거의 같다.
- `UserService`와 `UserServiceImpl`만 존재한다.
- Port가 외부 기술 격리가 아니라 형식상 만들어졌다.
- Abstract Class에 Hook Method가 너무 많다.
- Factory가 단순 생성자 호출만 감싼다.
- Adapter가 외부 DTO 변환 없이 단순 위임만 한다.

---

### [Troubleshooting]

문제:

- 파일 수가 많아 탐색 비용이 크다.
- 실제 변경에는 도움이 되지 않는다.
- Interface와 구현체가 1:1로 의미 없이 늘어난다.
- 테스트에서 Interface를 활용하지 않는다.

원인:

- “Interface는 무조건 좋다”는 오해가 있다.
- 미래 요구사항을 과도하게 예측했다.
- Framework 관습을 무비판적으로 적용했다.
- Pattern 적용 목적을 문서화하지 않았다.

해결:

- 구현체가 하나이고 교체 가능성이 낮은 Interface를 제거한다.
- 외부 API, 결제, 알림, 파일 저장소처럼 변경 가능성이 높은 곳에만 Port를 우선 적용한다.
- 단순 생성은 Factory 없이 생성자 또는 Static Factory Method를 사용한다.
- Abstract Class보다 Composition과 Strategy를 검토한다.
- 추상화 적용 이유를 ADR 또는 코드 주석으로 남긴다.

---

### [FAQ]

Q. Excessive Abstraction은 무엇인가?

A. 실제 필요보다 Interface, Abstract Class, Port, Adapter를 과도하게 적용해 복잡도를 높이는 문제이다.

Q. Interface 구현체가 하나뿐이면 나쁜가?

A. 항상 나쁜 것은 아니지만 교체 가능성, 테스트 가치, 외부 의존성 격리 목적이 없으면 불필요할 수 있다.

Q. `Service`와 `ServiceImpl` 구조는 항상 필요한가?

A. 아니다. 구현체가 하나라면 불필요한 추상화일 수 있다.

Q. 추상화 적용 기준은?

A. 변경 가능성, 구현체 다양성, 테스트 대체 필요성, 외부 기술 격리 필요성이다.

---

## 2.4 Wrong Pattern Choice

### [개념]

Wrong Pattern Choice는 실제 문제와 맞지 않는 Design Pattern을 선택하여 구조가 복잡해지거나 문제를 해결하지 못하는 상황이다.

Pattern은 목적이 다르므로 문제 유형과 맞아야 한다.

```text
Wrong Problem Classification
→ Wrong Pattern
→ More Complexity
→ Unsolved Problem
```

---

### [핵심]

- Pattern 선택 전 문제 유형을 분류해야 한다.
- 생성 문제에는 Creational Pattern을 검토한다.
- 구조 문제에는 Structural Pattern을 검토한다.
- 행동 문제에는 Behavioral Pattern을 검토한다.
- 시스템 구조 문제에는 Architecture Pattern을 검토한다.
- 비슷한 구조라도 Pattern 목적이 다르면 다른 Pattern이다.

---

### [실무]

Wrong Pattern Choice 예:

| 잘못된 선택                                      | 문제                     |
| ------------------------------------------------ | ------------------------ |
| 인터페이스 변환 문제에 Decorator 적용            | Adapter가 더 적합        |
| 알고리즘 교체 문제에 Template Method 강제        | Strategy가 더 유연       |
| 단순 객체 생성에 Factory + Abstract Factory 적용 | 과도한 생성 추상화       |
| 이벤트 후속 처리에 직접 Service 호출 유지        | Observer 검토 필요       |
| 외부 API 격리에 단순 Mapper만 적용               | Adapter / Port 검토 필요 |
| 접근 제어 문제에 Adapter 적용                    | Proxy가 더 적합          |
| 요청 재시도 문제에 Event만 사용                  | Command Queue 검토 필요  |

---

### [Troubleshooting]

문제:

- Pattern을 적용했지만 결합도가 줄지 않는다.
- 변경 시 여전히 기존 코드를 많이 수정한다.
- 테스트가 쉬워지지 않는다.
- Class 수만 늘고 문제 해결 효과가 없다.

원인:

- 문제를 잘못 분류했다.
- Pattern 목적을 이름으로만 이해했다.
- Trade-off를 검토하지 않았다.
- 기존 Framework 기능과 중복되는 Pattern을 만들었다.

해결:

- 문제를 생성, 구조, 행동, 아키텍처 문제로 다시 분류한다.
- Pattern 목적을 기준으로 후보를 다시 선택한다.
- 가장 단순한 해결책을 먼저 적용한다.
- Spring AOP, DI, Event, Transaction 등 Framework 기능과 중복되는지 확인한다.

---

### [FAQ]

Q. Wrong Pattern Choice는 무엇인가?

A. 실제 문제와 맞지 않는 Pattern을 선택하여 구조가 복잡해지거나 문제를 해결하지 못하는 상황이다.

Q. Wrong Pattern Choice를 줄이는 방법은?

A. 문제를 생성, 구조, 행동, 아키텍처 문제로 먼저 분류한 뒤 Pattern을 선택한다.

Q. Adapter와 Decorator를 헷갈리면 어떻게 구분하는가?

A. 인터페이스 변환이면 Adapter, 기능 확장이면 Decorator이다.

Q. Strategy와 Template Method를 헷갈리면 어떻게 구분하는가?

A. 알고리즘 전체 교체는 Strategy, 공통 흐름 고정과 일부 단계 변경은 Template Method이다.

---

# 3. SOLID Troubleshooting

## 3.1 SRP Violation

### [개념]

SRP Violation은 하나의 Class 또는 Module이 여러 변경 이유를 가져 책임이 과도하게 집중된 상태이다.

SRP Violation은 God Service, God Class, Fat Controller로 자주 나타난다.

```text
One Class
→ Multiple Responsibilities
→ Multiple Reasons to Change
```

---

### [핵심]

- SRP는 하나의 변경 이유를 가지는 것이 핵심이다.
- SRP 위반은 변경 영향과 테스트 비용을 증가시킨다.
- 검증, 계산, 저장, 알림, 외부 호출이 한 곳에 있으면 SRP 위반 가능성이 높다.
- SRP 위반은 Validator, Policy, Strategy, Adapter, Event로 완화할 수 있다.
- SRP는 Class 수를 늘리기 위한 원칙이 아니다.

---

### [Troubleshooting]

문제:

- `OrderService`가 주문 검증, 할인 계산, 결제 호출, 재고 차감, 알림 발송을 모두 처리한다.
- `FestivalController`가 요청 검증, DB 조회, DTO 변환, 외부 API 호출까지 처리한다.
- `UserService`가 회원, 인증, 이메일, 권한 정책을 모두 가진다.

원인:

- Use Case 흐름과 세부 책임이 분리되지 않았다.
- Layer Responsibility가 불명확하다.
- 빠른 구현을 위해 하나의 Class에 로직을 추가했다.
- 책임별 테스트 단위를 고려하지 않았다.

해결:

- 검증은 Validator로 분리한다.
- 정책 계산은 Policy 또는 Strategy로 분리한다.
- 외부 호출은 Adapter로 분리한다.
- 후속 작업은 Event Listener로 분리한다.
- Controller 로직은 Service로 이동한다.
- Use Case 조합은 Facade 또는 Application Service로 정리한다.

---

### [FAQ]

Q. SRP Violation은 무엇인가?

A. 하나의 Class 또는 Module이 여러 변경 이유를 가져 책임이 과도하게 집중된 상태이다.

Q. SRP Violation을 어떻게 찾는가?

A. 검증, 계산, 저장, 외부 호출, 알림 같은 여러 책임이 한 Class에 섞였는지 확인한다.

Q. SRP Violation 해결에 도움이 되는 Pattern은?

A. Strategy, Adapter, Observer, Facade, Template Method, Policy 객체가 도움이 된다.

Q. SRP를 적용하면 무조건 Class를 많이 나눠야 하는가?

A. 아니다. 변경 이유가 실제로 다른 책임만 분리해야 한다.

---

## 3.2 OCP Violation

### [개념]

OCP Violation은 새로운 기능이나 정책을 추가할 때 기존 코드를 계속 수정해야 하는 구조이다.

OCP Violation은 조건문 증가, 정책 분기, 타입별 처리 로직에서 자주 발생한다.

```text
New Requirement
→ Modify Existing Code
→ More Conditions
→ Higher Regression Risk
```

---

### [핵심]

- OCP는 확장에는 열려 있고 수정에는 닫혀 있어야 한다.
- OCP 위반은 if / switch 증가로 자주 나타난다.
- 정책 추가 시 기존 Service 수정이 반복되면 OCP 위반 가능성이 높다.
- Strategy와 Factory는 OCP 개선에 자주 사용된다.
- 모든 조건문이 OCP 위반은 아니다.

---

### [Troubleshooting]

문제:

- 결제 수단이 추가될 때마다 `PaymentService` if 문을 수정한다.
- 알림 채널이 추가될 때마다 `NotificationService` switch 문을 수정한다.
- 할인 정책이 추가될 때마다 기존 메서드 테스트를 다시 크게 수행해야 한다.

원인:

- 정책별 구현체가 분리되지 않았다.
- 객체 선택 책임과 실행 책임이 같은 Class에 있다.
- 타입 기반 분기가 중앙 Service에 집중되어 있다.
- Factory 또는 Strategy 구조가 없다.

해결:

- 정책별 Strategy 구현체를 만든다.
- 선택 책임은 Factory 또는 Resolver로 분리한다.
- 새로운 구현체 추가로 확장되게 설계한다.
- 조건문이 적고 변경 가능성이 낮으면 유지한다.
- Map-Based Factory로 if / switch 증가를 줄인다.

---

### [FAQ]

Q. OCP Violation은 무엇인가?

A. 새로운 기능 추가 시 기존 코드를 계속 수정해야 하는 구조이다.

Q. if 문이 있으면 무조건 OCP 위반인가?

A. 아니다. 변경이 반복되어 조건문이 계속 증가할 때 OCP 위반 가능성이 높다.

Q. OCP Violation 해결에 적합한 Pattern은?

A. Strategy, Factory, Template Method, Adapter가 자주 사용된다.

Q. OCP 적용 기준은?

A. 정책 추가 빈도, 조건문 증가, 기존 코드 수정 반복 여부를 기준으로 한다.

---

## 3.3 LSP Violation

### [개념]

LSP Violation은 하위 타입이 상위 타입을 대체했을 때 기대 동작이 깨지는 문제이다.

LSP Violation은 잘못된 상속 구조에서 자주 발생한다.

```text
Parent Type
→ Child Type
→ Broken Contract
```

---

### [핵심]

- 하위 타입은 상위 타입의 계약을 지켜야 한다.
- Override 메서드가 부모의 기대 동작을 깨면 LSP 위반이다.
- 지원하지 않는 메서드를 예외로 막는 것은 LSP 위반 신호이다.
- LSP 위반은 상속보다 Composition을 검토하게 만든다.
- Interface 분리로 해결할 수 있다.

---

### [Troubleshooting]

문제:

- 자식 Class가 부모 메서드에서 `UnsupportedOperationException`을 던진다.
- 부모 타입으로 사용할 때 특정 자식만 예외가 발생한다.
- Template Method 하위 Class가 부모 흐름을 따르지 못한다.
- 상속이 코드 재사용 목적으로만 사용되었다.

원인:

- “is-a” 관계가 아닌데 상속을 사용했다.
- 부모 Interface가 너무 많은 책임을 가진다.
- 하위 타입별 행동 차이를 상태나 전략으로 분리하지 않았다.
- 공통 코드 재사용만 보고 상속했다.

해결:

- Interface를 역할별로 분리한다.
- 상속 대신 Composition을 사용한다.
- 공통 기능은 Helper, Component, Strategy로 이동한다.
- Template Method가 맞지 않으면 Strategy로 전환한다.
- 부모 계약을 명확히 문서화한다.

---

### [FAQ]

Q. LSP Violation은 무엇인가?

A. 하위 타입이 상위 타입을 대체했을 때 정상 동작하지 않는 문제이다.

Q. LSP Violation의 대표 신호는?

A. 자식 Class가 부모 메서드에서 `UnsupportedOperationException`을 던지는 경우이다.

Q. LSP Violation 해결 방법은?

A. Interface 분리, Composition 사용, 잘못된 상속 제거, Strategy 전환을 검토한다.

Q. LSP와 Template Method는 어떤 관련이 있는가?

A. Template Method는 상속 기반이므로 하위 Class가 부모 흐름과 계약을 깨지 않도록 LSP를 지켜야 한다.

---

## 3.4 ISP Violation

### [개념]

ISP Violation은 Client가 사용하지 않는 메서드에 의존하거나 구현체가 필요 없는 메서드를 강제로 구현해야 하는 문제이다.

ISP Violation은 비대한 Interface에서 자주 발생한다.

```text
Large Interface
→ Unused Methods
→ Forced Implementation
```

---

### [핵심]

- ISP는 Client가 필요한 메서드에만 의존하게 한다.
- 큰 Interface는 구현체에 불필요한 메서드를 강요한다.
- `UnsupportedOperationException` 반복은 ISP 위반 신호이다.
- Interface는 역할 단위로 나눈다.
- 너무 잘게 나누면 Excessive Abstraction이 될 수 있다.

---

### [Troubleshooting]

문제:

- `NotificationService` Interface가 email, sms, push, slack 발송 메서드를 모두 가진다.
- Email 구현체가 `sendSms()`를 구현하지 못해 예외를 던진다.
- Client가 실제로 쓰지 않는 메서드를 가진 Interface에 의존한다.

원인:

- Interface를 역할이 아니라 기능 묶음 전체로 설계했다.
- 구현체 차이를 고려하지 않았다.
- Client 관점의 필요 기능을 분석하지 않았다.
- Interface 분리 기준이 없다.

해결:

- EmailSender, SmsSender, PushSender처럼 역할별 Interface로 분리한다.
- Client가 필요한 Interface에만 의존하게 한다.
- 공통 계약과 개별 계약을 분리한다.
- 구현체가 모두 지원하지 않는 메서드를 제거한다.
- 너무 작은 Interface가 늘어나지 않게 역할 응집도를 유지한다.

---

### [FAQ]

Q. ISP Violation은 무엇인가?

A. Client가 사용하지 않는 메서드에 의존하거나 구현체가 불필요한 메서드를 강제로 구현하는 문제이다.

Q. ISP Violation의 대표 신호는?

A. 구현체가 사용하지 않는 메서드에서 `UnsupportedOperationException`을 던지는 경우이다.

Q. ISP Violation 해결 방법은?

A. Interface를 Client 역할 기준으로 분리한다.

Q. Interface는 작을수록 좋은가?

A. 항상 그렇지는 않다. 역할 단위로 응집력 있게 작아야 한다.

---

## 3.5 DIP Violation

### [개념]

DIP Violation은 고수준 정책 모듈이 저수준 구현체에 직접 의존하는 문제이다.

DIP Violation은 외부 API, DB, 파일 저장소, 메시지 브로커 연동에서 자주 발생한다.

```text
High-Level Policy
→ Low-Level Implementation
→ Tight Coupling
```

---

### [핵심]

- 고수준 모듈은 저수준 구현체에 직접 의존하지 않아야 한다.
- 둘 다 Abstraction에 의존해야 한다.
- Spring DI를 사용해도 구현체에 직접 의존하면 DIP 위반일 수 있다.
- DIP는 Hexagonal Architecture와 Clean Architecture의 핵심이다.
- DIP는 테스트 대체와 외부 시스템 교체에 유리하다.

---

### [Troubleshooting]

문제:

- `OrderService`가 `TossPaymentClient`를 직접 사용한다.
- `AiSummaryService`가 `OpenAiClient` 구현체를 직접 사용한다.
- `FileService`가 `S3Client`에 직접 의존한다.
- 테스트에서 외부 시스템 없이 Use Case를 검증하기 어렵다.

원인:

- Port Interface가 없다.
- 외부 기술 구현체를 Adapter로 분리하지 않았다.
- 내부 요구사항보다 외부 API 스펙을 기준으로 설계했다.
- DI와 DIP를 같은 개념으로 오해했다.

해결:

- 내부 Use Case 기준의 Port를 정의한다.
- 외부 Client는 Adapter에서만 사용한다.
- Application Service는 Port에 의존한다.
- Adapter가 Port를 구현한다.
- 테스트에서는 Fake Port 구현체를 사용한다.

---

### [FAQ]

Q. DIP Violation은 무엇인가?

A. 고수준 정책 모듈이 저수준 구현체에 직접 의존하는 문제이다.

Q. Spring DI를 쓰면 DIP Violation이 자동으로 해결되는가?

A. 아니다. 구현체에 직접 의존하면 DI를 사용해도 DIP 위반이다.

Q. DIP Violation 해결 Pattern은?

A. Adapter Pattern, Port, Hexagonal Architecture가 도움이 된다.

Q. DIP는 언제 특히 중요한가?

A. 외부 API, 결제, 알림, 파일 저장소, 메시지 브로커처럼 구현체 교체 가능성이 있는 영역에서 중요하다.

---

# 4. Pattern-Specific Troubleshooting

## 4.1 Factory Troubleshooting

### [개념]

Factory Troubleshooting은 Factory Pattern 적용 과정에서 발생하는 생성 책임 오염, God Factory, 조건문 증가, 객체 선택 오류를 검수하는 과정이다.

Factory는 객체 생성 또는 선택 책임에 집중해야 한다.

```text
Request Type
→ Factory
→ Object Selection
→ Concrete Object
```

---

### [핵심]

- Factory는 생성 책임 또는 선택 책임만 가진다.
- Factory에 비즈니스 정책이 들어가면 SRP 위반이다.
- Factory가 모든 객체를 만들면 God Factory가 된다.
- Factory 내부 if / switch가 계속 증가하면 Map-Based Factory를 검토한다.
- Spring Bean 선택에는 List Injection과 Map 매핑을 활용할 수 있다.

---

### [Troubleshooting]

문제:

- Factory가 객체 생성뿐 아니라 결제 승인 정책까지 판단한다.
- 하나의 Factory가 결제, 알림, 파일, AI 요청 객체를 모두 생성한다.
- Factory 내부 조건문이 계속 증가한다.
- 지원하지 않는 타입 처리 예외가 불명확하다.

원인:

- Factory 책임 범위를 정하지 않았다.
- 객체 선택과 비즈니스 정책 판단이 섞였다.
- 타입별 구현체 등록 구조가 없다.
- Factory를 전역 생성 도구처럼 사용했다.

해결:

- Factory를 Domain 또는 기능별로 분리한다.
- 비즈니스 정책은 Strategy 또는 Policy로 이동한다.
- 구현체가 많으면 Map-Based Factory를 사용한다.
- 미지원 타입 예외를 명확히 정의한다.
- Factory 테스트를 작성해 타입별 선택 결과를 검증한다.

---

### [FAQ]

Q. Factory에서 가장 자주 발생하는 문제는?

A. 생성 책임을 넘어 비즈니스 정책까지 담당하거나 God Factory가 되는 문제이다.

Q. Factory 내부 if 문이 많아지면 어떻게 하는가?

A. Strategy와 Map-Based Factory를 검토한다.

Q. Factory는 항상 객체를 새로 생성해야 하는가?

A. 아니다. Spring Bean으로 생성된 구현체를 선택해서 반환할 수도 있다.

Q. Factory에 비즈니스 로직을 넣어도 되는가?

A. 권장하지 않는다. Factory는 생성 또는 선택 책임에 집중해야 한다.

---

## 4.2 Builder Troubleshooting

### [개념]

Builder Troubleshooting은 Builder Pattern 사용 과정에서 발생하는 필수값 누락, Domain Invariant 위반, Entity Builder 남용을 검수하는 과정이다.

Builder는 객체 생성 가독성을 높이지만 객체 무결성을 자동으로 보장하지 않는다.

```text
Builder Input
→ Constructor Validation
→ Valid Object
```

---

### [핵심]

- Builder는 필수값 누락을 컴파일 타임에 막기 어렵다.
- Builder는 모든 필드를 외부에 열어 객체 무결성을 깨뜨릴 수 있다.
- Entity Class Level `@Builder`는 주의해야 한다.
- 생성자 내부 검증이 중요하다.
- `@Builder.Default` 누락은 기본값 오류를 만들 수 있다.

---

### [Troubleshooting]

문제:

- null 필수값을 가진 객체가 생성된다.
- Entity 상태가 잘못된 조합으로 생성된다.
- 연관관계가 Builder로 무분별하게 설정된다.
- 기본값이 Builder 사용 시 적용되지 않는다.
- 테스트용 Builder가 운영 코드에 섞인다.

원인:

- 생성자 검증이 없다.
- Class Level `@Builder`를 무분별하게 사용했다.
- `@Builder.Default`를 누락했다.
- 필수값과 선택값 기준이 없다.
- Domain Rule을 Builder에 맡겼다.

해결:

- Entity는 Constructor Level `@Builder`를 우선 사용한다.
- 생성자에서 필수값과 Domain Rule을 검증한다.
- 기본값이 필요한 필드는 `@Builder.Default`를 검토한다.
- Test Fixture Builder를 별도로 분리한다.
- 단순 DTO는 Record 또는 생성자를 사용한다.

---

### [FAQ]

Q. Builder의 가장 큰 위험은?

A. 필수값 누락과 객체 무결성 위반을 숨길 수 있다는 점이다.

Q. Entity에 `@Builder`를 사용할 때 주의할 점은?

A. Class Level보다 Constructor Level에 적용하고 생성자 검증을 포함하는 것이 안전하다.

Q. `@Builder.Default`는 왜 필요한가?

A. Builder 사용 시 필드 초기 기본값이 무시될 수 있기 때문이다.

Q. Builder는 모든 객체에 필요한가?

A. 아니다. 필드가 적고 선택값이 없는 객체에는 생성자나 Record가 더 단순할 수 있다.

---

## 4.3 Adapter Troubleshooting

### [개념]

Adapter Troubleshooting은 Adapter가 외부 시스템과 내부 Application Core를 제대로 격리하는지 검수하는 과정이다.

Adapter는 외부 기술 변경이 내부 Use Case와 Domain에 전파되지 않도록 해야 한다.

```text
Application Service
→ Port
← Adapter
→ External System
```

---

### [핵심]

- Adapter는 외부 호출과 변환 책임을 가진다.
- 외부 DTO는 Adapter 내부에서 끝나야 한다.
- Adapter는 외부 예외를 내부 예외로 변환한다.
- Adapter에 핵심 비즈니스 정책을 넣으면 안 된다.
- Port는 외부 API 스펙이 아니라 내부 Use Case 기준으로 설계한다.

---

### [Troubleshooting]

문제:

- Service가 외부 API Response DTO를 직접 사용한다.
- Port Method가 외부 API URL, Request Parameter를 그대로 반영한다.
- Adapter가 주문 상태, 할인 정책, 권한 판단까지 수행한다.
- 외부 API 변경 시 Application Service가 수정된다.
- 테스트에서 Fake Adapter로 쉽게 대체할 수 없다.

원인:

- Port를 외부 API 기준으로 설계했다.
- 외부 DTO와 내부 모델 변환 위치가 잘못되었다.
- Adapter 책임과 Application Service 책임이 섞였다.
- DIP 방향을 지키지 않았다.

해결:

- Port를 내부 기능 기준으로 재정의한다.
- 외부 DTO는 Adapter에서 내부 Result로 변환한다.
- 핵심 정책은 Application Service 또는 Domain Service로 이동한다.
- Adapter 구현체는 Infrastructure 영역에 둔다.
- Adapter 단위 Integration Test와 Port Fake Test를 분리한다.

---

### [FAQ]

Q. Adapter Troubleshooting의 핵심 검수 기준은?

A. 외부 DTO 침투, 비즈니스 로직 포함, Port 외부 종속, DIP 위반 여부이다.

Q. 외부 API DTO가 Service에 들어오면 왜 문제인가?

A. 외부 응답 구조 변경이 내부 비즈니스 코드까지 전파되기 때문이다.

Q. Adapter에 Retry를 넣어도 되는가?

A. 기술적 재시도 정책은 가능하지만 중복 처리와 부작용을 고려해야 한다.

Q. Port는 무엇을 기준으로 설계해야 하는가?

A. 외부 API 스펙이 아니라 Application이 필요로 하는 기능과 결과를 기준으로 설계한다.

---

## 4.4 Strategy Troubleshooting

### [개념]

Strategy Troubleshooting은 Strategy Pattern 적용 과정에서 발생하는 과도한 구현체 증가, 선택 책임 오염, Stateful Strategy 문제를 검수하는 과정이다.

Strategy는 알고리즘 또는 정책 교체를 위해 사용한다.

```text
Context
→ Strategy Factory
→ Strategy
→ Algorithm Execution
```

---

### [핵심]

- Strategy는 알고리즘 교체가 목적이다.
- 모든 조건문을 Strategy로 바꾸면 안 된다.
- Strategy 선택 책임은 Factory 또는 Resolver에 둔다.
- Strategy 구현체는 Stateless로 설계한다.
- Strategy Key 중복과 미지원 타입 처리를 검수한다.

---

### [Troubleshooting]

문제:

- Strategy 구현체가 많지만 실제 로직 차이가 거의 없다.
- Strategy 내부에서 다시 다른 Strategy를 선택한다.
- Service가 Strategy 구현체 목록을 직접 순회한다.
- Strategy Bean이 요청별 상태를 필드에 저장한다.
- 지원하지 않는 타입 처리 예외가 불명확하다.

원인:

- Strategy 적용 기준이 불명확하다.
- Factory 책임과 Strategy 책임을 분리하지 않았다.
- Singleton Bean의 Stateless 원칙을 지키지 않았다.
- 정책 차이가 작은데 과도하게 Class를 분리했다.

해결:

- 변경 가능성이 낮은 단순 분기는 조건문으로 유지한다.
- Strategy 선택은 Factory로 이동한다.
- Strategy 구현체는 하나의 정책에 집중한다.
- 요청별 상태는 Method Parameter로 전달한다.
- Strategy Key는 Enum으로 관리하고 중복을 검증한다.

---

### [FAQ]

Q. Strategy Troubleshooting에서 가장 중요한 검수 기준은?

A. 알고리즘 교체 필요성, Strategy 과도화, 선택 책임 위치, Stateless 여부이다.

Q. 모든 조건문을 Strategy로 바꿔야 하는가?

A. 아니다. 반복 변경과 정책 확장이 있는 조건문에 우선 적용한다.

Q. Strategy 선택은 어디에서 해야 하는가?

A. Service보다 Factory 또는 Resolver에서 처리하는 것이 좋다.

Q. Strategy Bean이 상태를 가지면 왜 위험한가?

A. Singleton Bean으로 공유되므로 요청 간 데이터가 섞일 수 있기 때문이다.

---

## 4.5 Observer Troubleshooting

### [개념]

Observer Troubleshooting은 Event 기반 구조에서 흐름 숨김, Listener 실패, Transaction 시점, Event Payload 결합 문제를 검수하는 과정이다.

Observer는 이벤트 후속 처리를 분리하지만 흐름 가시성을 낮출 수 있다.

```text
Publisher
→ Event
→ Listener
→ Side Effect
```

---

### [핵심]

- Observer는 직접 호출 결합을 줄인다.
- Event Flow는 문서화해야 한다.
- Listener 실패가 원본 Use Case에 영향을 줄지 결정해야 한다.
- Transaction Commit 전후 처리 시점을 구분해야 한다.
- Event에는 Entity보다 ID와 필요한 값만 담는다.
- 비동기 Event는 재시도와 멱등성이 필요하다.

---

### [Troubleshooting]

문제:

- Event 발행 후 어떤 Listener가 실행되는지 알기 어렵다.
- Listener 실패가 조용히 묻힌다.
- Transaction Rollback 후에도 외부 알림이 발송된다.
- Event Payload에 Entity가 들어가 Lazy Loading 문제가 발생한다.
- Listener 실행 순서에 숨은 의존성이 있다.

원인:

- Event Flow 문서화가 없다.
- `@EventListener`와 `@TransactionalEventListener` 차이를 고려하지 않았다.
- 비동기 실패 처리 전략이 없다.
- Event Payload가 과도하다.
- Listener 책임이 명확하지 않다.

해결:

- Event Publisher와 Listener 목록을 문서화한다.
- DB Commit 이후 처리해야 하면 `AFTER_COMMIT`을 사용한다.
- 비동기 Listener는 Retry, DLQ, 실패 로그를 둔다.
- Event에는 ID와 필요한 Snapshot 값만 담는다.
- Listener는 하나의 후속 책임만 가지게 한다.

---

### [FAQ]

Q. Observer Troubleshooting의 핵심 검수 기준은?

A. Event Flow 가시성, Listener 실패 처리, Transaction 시점, Payload 크기, 멱등성이다.

Q. `@EventListener`와 `@TransactionalEventListener`의 차이는?

A. `@EventListener`는 기본 동기 실행이고 `@TransactionalEventListener`는 Transaction phase에 맞춰 실행할 수 있다.

Q. Event에 Entity를 담으면 왜 위험한가?

A. Lazy Loading, 직렬화, Transaction 경계, 외부 결합 문제가 발생할 수 있기 때문이다.

Q. 비동기 Event에서 중요한 것은?

A. 실패 처리, 재시도, 멱등성, 추적 로그이다.

---

## 4.6 Proxy Troubleshooting

### [개념]

Proxy Troubleshooting은 Spring AOP, Transaction, Security, JPA Lazy Loading이 Proxy 기반으로 동작하면서 발생하는 문제를 검수하는 과정이다.

Proxy는 실제 객체 접근을 대리하지만 Proxy를 거치지 않으면 부가기능이 적용되지 않을 수 있다.

```text
Client
→ Proxy
→ Target
```

---

### [핵심]

- Spring AOP는 Proxy 기반이다.
- Self Invocation은 Proxy를 거치지 않는다.
- `@Transactional`은 Proxy 호출에서 적용된다.
- private method에는 일반적인 Spring AOP가 적용되지 않는다.
- JPA Lazy Proxy는 Transaction 범위 안에서 초기화해야 한다.
- Proxy 문제는 테스트와 로그로 검증해야 한다.

---

### [Troubleshooting]

문제:

- 같은 Class 내부 메서드 호출에서 `@Transactional`이 적용되지 않는다.
- private method에 AOP Annotation을 붙였지만 동작하지 않는다.
- LazyInitializationException이 발생한다.
- final method에 AOP가 적용되지 않는다.
- `new`로 생성한 객체에는 Spring AOP가 적용되지 않는다.

원인:

- Proxy를 거치지 않는 호출 구조이다.
- Spring Bean이 아닌 객체를 직접 생성했다.
- Transaction 범위 밖에서 Lazy Field에 접근했다.
- AOP 적용 조건을 잘못 이해했다.

해결:

- AOP 대상 메서드는 외부 Bean에서 호출되게 분리한다.
- Service 객체는 Spring Bean으로 주입받는다.
- Transaction 안에서 필요한 Lazy Field를 조회한다.
- Fetch Join, EntityGraph, DTO Projection을 사용한다.
- private/final method에 AOP를 기대하지 않는다.

---

### [FAQ]

Q. Proxy Troubleshooting의 핵심 검수 기준은?

A. Proxy를 거치는 호출인지, Self Invocation이 있는지, Transaction과 Lazy Loading 범위가 맞는지 확인하는 것이다.

Q. Self Invocation에서 `@Transactional`이 안 되는 이유는?

A. 같은 객체 내부 호출은 Spring Proxy를 거치지 않기 때문이다.

Q. `new`로 만든 객체에 AOP가 적용되는가?

A. 아니다. Spring Container가 관리하는 Proxy Bean을 통해 호출해야 한다.

Q. LazyInitializationException 해결 방법은?

A. Transaction 안에서 조회하거나 Fetch Join, EntityGraph, DTO Projection을 사용한다.

---

# 5. Architecture Troubleshooting

## 5.1 Layer Violation Troubleshooting

### [개념]

Layer Violation Troubleshooting은 Controller, Service, Repository, Domain, Adapter 계층의 책임이 섞이거나 잘못된 방향으로 의존하는 문제를 검수하는 과정이다.

```text
Layer
→ Responsibility Check
→ Dependency Check
→ Refactoring
```

---

### [핵심]

- Controller는 HTTP 처리에 집중한다.
- Service는 Use Case와 Transaction을 담당한다.
- Repository는 Persistence 접근을 담당한다.
- Domain은 핵심 규칙과 상태 변경을 담당한다.
- Adapter는 외부 기술 연동을 담당한다.
- Layer 간 책임이 섞이면 테스트와 변경이 어려워진다.

---

### [Troubleshooting]

문제:

- Controller가 Repository를 직접 호출한다.
- Controller에 할인 계산 로직이 있다.
- Repository Query에 비즈니스 정책이 과도하게 들어 있다.
- Domain Entity가 Response DTO를 생성한다.
- Service가 `HttpServletRequest`를 깊게 의존한다.
- 외부 API Client가 Domain Service에 들어와 있다.

원인:

- Layer Responsibility 기준이 없다.
- 빠른 구현을 위해 가까운 곳에 로직을 넣었다.
- DTO와 Domain Model 구분이 없다.
- 외부 연동 경계를 만들지 않았다.

해결:

- Controller 로직은 Service로 이동한다.
- 비즈니스 정책은 Domain, Policy, Strategy로 이동한다.
- 외부 API는 Adapter로 분리한다.
- DTO 변환 위치를 일관되게 정한다.
- Repository는 Persistence 책임만 유지한다.
- Layer Responsibility Checklist로 Code Review한다.

---

### [FAQ]

Q. Layer Violation Troubleshooting은 무엇을 검수하는가?

A. 각 계층이 자신의 책임을 벗어났는지, 잘못된 계층에 의존하는지 검수한다.

Q. Controller가 Repository를 직접 호출하면 왜 문제인가?

A. Use Case 계층이 사라지고 HTTP 계층이 Persistence에 직접 결합되기 때문이다.

Q. Repository에 비즈니스 로직을 넣어도 되는가?

A. 권장하지 않는다. Repository는 DB 접근과 Query 책임에 집중해야 한다.

Q. Layer Violation을 줄이는 방법은?

A. Controller, Service, Repository, Domain, Adapter 책임을 명확히 분리한다.

---

## 5.2 Dependency Direction Troubleshooting

### [개념]

Dependency Direction Troubleshooting은 의존성이 외부에서 내부로 향하지 않고 내부 핵심 정책이 외부 구현체를 직접 참조하는 문제를 검수하는 과정이다.

Clean Architecture와 Hexagonal Architecture에서 핵심 검수 대상이다.

```text
Wrong:
Core → Infrastructure

Correct:
Core → Port ← Infrastructure Adapter
```

---

### [핵심]

- 내부 Core는 외부 Adapter를 몰라야 한다.
- Domain은 Web, DB, External API를 직접 알면 안 된다.
- Application Service는 외부 Client가 아니라 Port에 의존해야 한다.
- Adapter는 Port를 구현한다.
- Package Import 방향으로 의존성 위반을 검수한다.
- DI 사용 여부보다 의존 대상이 중요하다.

---

### [Troubleshooting]

문제:

- Application Service가 `TossPaymentAdapter`를 직접 import한다.
- Domain이 `KakaoMapResponse`를 필드로 가진다.
- Use Case가 `WebClient`를 직접 사용한다.
- AI 요약 Use Case가 특정 `OpenAiClient` 구현체에 직접 의존한다.
- 테스트에서 외부 API 없이 Use Case 실행이 어렵다.

원인:

- Port가 정의되지 않았다.
- Adapter와 Core 책임을 분리하지 않았다.
- 외부 API 스펙을 내부 모델로 사용했다.
- DIP를 적용하지 않았다.

해결:

- Core가 필요한 Interface를 Port로 정의한다.
- 외부 구현체는 Adapter로 이동한다.
- Adapter가 Port를 구현한다.
- 외부 DTO는 Adapter에서 내부 Result로 변환한다.
- Core Package의 import를 검수한다.

---

### [FAQ]

Q. Dependency Direction Troubleshooting은 무엇을 검수하는가?

A. 내부 Core가 외부 구현체에 직접 의존하는지, Port와 Adapter 방향이 올바른지 검수한다.

Q. DI를 쓰면 의존성 방향 문제가 해결되는가?

A. 아니다. 구현체에 직접 의존하면 DI를 사용해도 방향은 깨진다.

Q. 의존성 방향은 어떻게 확인하는가?

A. Package import와 생성자 주입 타입을 기준으로 확인한다.

Q. 해결 방법은?

A. Port를 정의하고 Adapter가 구현하도록 하여 Core가 외부 구현체를 직접 알지 않게 한다.

---

## 5.3 Domain Leakage Troubleshooting

### [개념]

Domain Leakage Troubleshooting은 핵심 Domain Rule과 Domain Model이 Controller, DTO, Repository, Adapter, 외부 API 구조에 흩어지는 문제를 검수하는 과정이다.

Domain Leakage는 Domain Isolation을 약화시킨다.

```text
Domain Rule
→ Controller / DTO / Adapter / Repository
→ Scattered Rule
```

---

### [핵심]

- Domain Rule은 한 곳에서 추적 가능해야 한다.
- 외부 API 필드명이 Domain에 들어오면 위험하다.
- DTO 검증과 Domain Rule 검증은 구분한다.
- 상태 변경은 의미 있는 Domain Method로 캡슐화한다.
- Setter 남용은 Domain Leakage를 악화시킨다.
- Value Object와 Policy 객체로 Domain Rule을 모을 수 있다.

---

### [Troubleshooting]

문제:

- 축제 시작일/종료일 검증이 Controller와 Service에 중복된다.
- 리뷰 평점 0~5 검증이 DB Constraint에만 있다.
- 외부 API의 `mapX`, `mapY` 이름이 Domain Model에 들어온다.
- 주문 상태 변경 규칙이 여러 Service Method에 흩어져 있다.
- Entity 상태를 Setter로 어디서나 변경한다.

원인:

- Domain Rule 위치를 정하지 않았다.
- 입력 검증과 비즈니스 불변식을 구분하지 않았다.
- 외부 DTO를 내부 모델로 변환하지 않았다.
- Domain Method를 만들지 않았다.
- Value Object를 사용하지 않았다.

해결:

- 핵심 규칙은 Entity, Value Object, Domain Service, Policy로 이동한다.
- 외부 API DTO는 Adapter에서 내부 모델로 변환한다.
- 상태 변경은 `cancel()`, `completePayment()`, `changePeriod()` 같은 의미 있는 Method로 처리한다.
- DTO 검증은 형식 검증, Domain 검증은 비즈니스 규칙으로 구분한다.
- 중복된 규칙은 하나의 정책 객체로 통합한다.

---

### [FAQ]

Q. Domain Leakage Troubleshooting은 무엇을 검수하는가?

A. 핵심 Domain Rule이 외부 계층이나 DTO, Adapter에 흩어져 있는지 검수한다.

Q. 외부 API 필드명이 Domain에 들어오면 왜 문제인가?

A. 외부 API 스펙 변경이 내부 Domain Model 변경으로 전파될 수 있기 때문이다.

Q. Domain Rule은 어디에 두는가?

A. Entity, Value Object, Domain Service, Policy 객체에 둔다.

Q. Setter 남용은 왜 위험한가?

A. 상태 변경 규칙이 우회되어 객체 무결성이 깨질 수 있기 때문이다.

---

## 5.4 Over Engineering Architecture Troubleshooting

### [개념]

Over Engineering Architecture Troubleshooting은 프로젝트 규모와 문제 복잡도에 비해 Architecture Pattern, 계층, Interface, Adapter가 과도한지 검수하는 과정이다.

Architecture는 문제 해결 수단이지 목표가 아니다.

```text
Small Feature
→ Too Many Layers
→ Slow Development
→ Hard Maintenance
```

---

### [핵심]

- 단순 CRUD에는 Layered Architecture가 충분할 수 있다.
- 모든 Service에 Interface가 필요한 것은 아니다.
- 모든 Repository를 Port로 감싸는 것은 과할 수 있다.
- Clean Architecture 전체 적용은 비용이 크다.
- 팀 이해도와 일정도 Architecture 선택 기준이다.
- 단순화도 중요한 Architecture Refactoring이다.

---

### [Troubleshooting]

문제:

- 단순 조회 API에 UseCase, Port, Adapter, Mapper, Presenter가 모두 있다.
- 구현체가 하나뿐인데 Interface가 모든 계층에 있다.
- Package Depth가 깊어 파일 탐색이 어렵다.
- 코드 생성 Agent가 구조를 일관되게 따라가지 못한다.
- 기능 추가보다 구조 보일러플레이트 작성 시간이 더 길다.

원인:

- Architecture Pattern을 형식적으로 적용했다.
- 미래 확장을 과도하게 예측했다.
- 프로젝트 규모와 팀 역량을 고려하지 않았다.
- Layered Architecture를 무조건 낮은 수준으로 오해했다.

해결:

- 단순 CRUD는 Layered Architecture로 유지한다.
- 외부 연동과 핵심 Domain에만 Port와 Adapter를 우선 적용한다.
- 구현체가 하나이고 교체 가능성이 낮은 Interface는 제거한다.
- Package Depth를 줄인다.
- Architecture 적용 기준을 문서화한다.
- Agent가 생성할 수 있는 단순하고 일관된 구조를 유지한다.

---

### [FAQ]

Q. Over Engineering Architecture Troubleshooting은 무엇을 검수하는가?

A. 문제 복잡도에 비해 계층, Interface, Port, Adapter가 과도한지 검수한다.

Q. 단순 CRUD에도 Hexagonal Architecture가 필요한가?

A. 보통은 필요하지 않다. Layered Architecture가 더 적합할 수 있다.

Q. 모든 Service에 Interface를 만들어야 하는가?

A. 아니다. 교체 가능성, 테스트 필요성, 구현체 다양성이 있을 때 만든다.

Q. Architecture 단순화도 Refactoring인가?

A. 그렇다. 불필요한 계층과 추상화를 제거하는 것도 중요한 Refactoring이다.

---

# 6. Agent-Specific Review Rules

## 6.1 Backend Agent Review Rules

### [개념]

Backend Agent Review Rules는 Backend Agent가 코드 생성 또는 수정 시 Design Pattern을 어떻게 적용하고 검수해야 하는지 정의한다.

Backend Agent는 기능 구현보다 구조 일관성과 변경 가능성을 함께 고려해야 한다.

```text
Requirement
→ Use Case Analysis
→ Pattern Candidate
→ Simple Implementation
→ Review
```

---

### [핵심]

- Backend Agent는 요구사항의 변경 지점을 먼저 찾는다.
- 단순 CRUD는 Layered Architecture로 구현한다.
- 외부 API 연동은 Adapter 적용을 우선 검토한다.
- 정책 교체 가능성이 있으면 Strategy를 검토한다.
- 객체 생성 조건이 복잡하면 Factory를 검토한다.
- DTO 생성이 복잡하면 Builder 또는 Static Factory Method를 검토한다.
- 후속 작업이 많으면 Event / Observer를 검토한다.
- 요청 저장과 재시도가 필요하면 Command를 검토한다.

---

### [실무]

Backend Agent 적용 기준:

| 요구사항               | 우선 구조                       |
| ---------------------- | ------------------------------- |
| 단순 조회 / 저장       | Controller-Service-Repository   |
| 결제 Provider 연동     | PaymentPort + PaymentAdapter    |
| 알림 채널 선택         | Notification Strategy + Factory |
| 축제 외부 API 동기화   | External API Adapter            |
| 채팅 메시지 후 AI 요약 | Event + Listener                |
| 알림 발송 재시도       | Command Queue                   |
| DTO 변환               | Static Factory Method `from()`  |
| 복잡한 응답 DTO 생성   | Builder                         |
| 공통 Batch Flow        | Template Method                 |
| 계층형 댓글 / 카테고리 | Composite                       |

---

### [주의]

- Backend Agent는 Pattern을 기본값으로 남용하지 않는다.
- 구현체가 하나이고 교체 가능성이 낮으면 Interface를 생략할 수 있다.
- 외부 API DTO를 Service 밖으로 노출하지 않는다.
- Entity에 `@Setter`를 무분별하게 붙이지 않는다.
- Transaction과 Event 처리 시점을 명확히 한다.
- AOP와 Transaction은 Proxy 동작을 고려한다.

---

### [FAQ]

Q. Backend Agent는 언제 Pattern을 적용해야 하는가?

A. 변경 지점, 외부 의존성, 정책 교체, 후속 작업, 재시도 필요성이 있을 때 적용한다.

Q. Backend Agent는 단순 CRUD에 어떤 구조를 써야 하는가?

A. Layered Architecture를 우선 사용한다.

Q. Backend Agent는 외부 API 연동을 어떻게 설계해야 하는가?

A. 외부 API Client를 Adapter로 감싸고 내부 Service는 Port 또는 내부 Result에 의존하게 한다.

Q. Backend Agent는 Pattern 남용을 어떻게 피하는가?

A. 현재 문제, 변경 가능성, 테스트 가치가 명확할 때만 Pattern을 적용한다.

---

## 6.2 Review Agent Review Rules

### [개념]

Review Agent Review Rules는 Review Agent가 Design Pattern 관점에서 코드와 아키텍처를 검수하는 기준이다.

Review Agent는 잘못된 Pattern 적용, Pattern 누락, Over Engineering을 모두 검수해야 한다.

```text
Code
→ Smell Detection
→ Pattern Fit Review
→ SOLID Review
→ Architecture Review
→ Refactoring Proposal
```

---

### [핵심]

- Review Agent는 문제를 먼저 설명한다.
- 원인을 SOLID, Pattern, Architecture 기준으로 분석한다.
- 해결책은 구체적인 Refactoring 단위로 제안한다.
- 관련 Pattern을 명시한다.
- Pattern 적용의 Trade-off도 함께 제시한다.
- 단순화가 필요하면 Pattern 제거를 제안한다.

---

### [실무]

Review Agent 우선 검수 항목:

1. God Service
2. Fat Controller
3. 외부 API Client 직접 의존
4. 외부 DTO 내부 침투
5. Strategy Overuse
6. Factory God Object
7. Builder 필수값 누락
8. Singleton State Bug
9. Event Flow Hidden Problem
10. Command Retry Idempotency 문제
11. Proxy Self Invocation 문제
12. LazyInitializationException 가능성
13. Layer Violation
14. Dependency Direction 위반
15. Domain Leakage
16. Over Engineering Architecture

---

### [Review Template]

```text
[Design Pattern Review]

문제:
...

원인:
...

관련 원칙:
SRP / OCP / DIP / LSP / ISP

관련 Pattern:
Strategy / Factory / Adapter / Observer / Command / Hexagonal Architecture

해결:
1. ...
2. ...
3. ...

Trade-off:
...

최종 판단:
적용 권장 / 단순 구조 유지 / Pattern 제거 권장
```

---

### [주의]

- Review Agent는 무조건 복잡한 구조를 추천하지 않는다.
- Pattern 적용보다 문제 해결을 우선한다.
- 코드 규모, 팀 역량, 현재 요구사항을 고려한다.
- Pattern 이름만으로 정답처럼 판단하지 않는다.
- Refactoring 제안은 단계적으로 작성한다.

---

### [FAQ]

Q. Review Agent는 무엇을 우선 검수해야 하는가?

A. 책임 분리, 의존성 방향, 외부 DTO 침투, Pattern 적합성, Over Engineering을 우선 검수한다.

Q. Review Agent는 Pattern 제거를 제안할 수 있는가?

A. 그렇다. 불필요한 Pattern은 제거하는 것이 더 좋은 Refactoring일 수 있다.

Q. Review Agent 결과 형식은?

A. 문제, 원인, 관련 원칙, 관련 Pattern, 해결, Trade-off, 최종 판단 형식이 좋다.

Q. Review Agent가 가장 주의할 점은?

A. Pattern을 정답처럼 강제하지 않고 현재 문제에 맞는 최소 구조를 제안하는 것이다.

---

## 6.3 PM Agent Review Rules

### [개념]

PM Agent Review Rules는 PM Agent가 요구사항을 분석하여 어떤 설계 문제와 Pattern 후보가 있는지 Backend Agent와 Review Agent에게 전달하는 기준이다.

PM Agent는 구현 코드보다 요구사항의 변경 가능성, 외부 의존성, 후속 작업, 실패 처리 요구를 분류한다.

```text
User Request
→ Requirement Classification
→ Design Risk Detection
→ Agent Task Instruction
```

---

### [핵심]

- PM Agent는 요구사항을 Design Problem으로 분류한다.
- PM Agent는 단순 CRUD와 복잡한 Domain을 구분한다.
- PM Agent는 외부 시스템 연동 여부를 식별한다.
- PM Agent는 정책 교체 가능성을 식별한다.
- PM Agent는 이벤트 후속 작업을 식별한다.
- PM Agent는 비동기, 재시도, 실패 처리 요구를 식별한다.
- PM Agent는 Over Engineering 위험도 함께 표시한다.

---

### [실무]

PM Agent 요구사항 분류 예:

| 요구사항 신호              | 설계 분류          | Agent 지시                     |
| -------------------------- | ------------------ | ------------------------------ |
| 결제 수단 추가 가능        | Strategy / Factory | 결제 타입별 Strategy 구조 검토 |
| Toss API 연동              | Adapter / Port     | 외부 DTO 내부 침투 금지        |
| 회원 가입 후 이메일 발송   | Observer           | Event Listener 분리 검토       |
| 알림 실패 재시도           | Command Queue      | 멱등성, 재시도 횟수 설계       |
| 단순 목록 조회             | Layered            | 과도한 Port 생성 금지          |
| 축제 기간 검증             | Domain Rule        | Entity 또는 Value Object 검증  |
| AI 요약 Provider 교체 가능 | Port / Adapter     | AiSummaryPort 설계             |
| 여러 Agent 순차 실행       | Mediator           | Workflow Orchestrator 검토     |

---

### [Agent Instruction Template]

```text
요구사항:
축제 채팅 메시지 작성 후 AI 요약 후보를 생성한다.

설계 분류:
Event 후속 처리 + AI 외부 의존성

Backend Agent 지시:
ChatMessageCreatedEvent를 발행하고 AI 요약 처리는 Listener로 분리한다.
AI Provider는 AiSummaryPort와 Adapter로 격리한다.

Review Agent 검수:
Event Flow Hidden Problem, Adapter 외부 DTO 침투, Retry 필요성, Over Engineering 여부를 검수한다.
```

---

### [주의]

- PM Agent는 Pattern을 확정하지 않고 후보와 위험을 전달한다.
- PM Agent는 과도한 구조를 요구하지 않는다.
- 요구사항이 단순하면 단순 구현을 명시한다.
- 외부 시스템 연동은 장애, 재시도, Timeout, Rate Limit을 함께 고려한다.
- Agent 간 역할이 겹치지 않게 지시한다.

---

### [FAQ]

Q. PM Agent는 Design Pattern을 어떻게 활용하는가?

A. 요구사항을 설계 문제로 분류하고 적절한 Pattern 후보와 검수 포인트를 다른 Agent에게 전달한다.

Q. PM Agent가 Pattern을 확정해야 하는가?

A. 아니다. 후보와 위험을 제시하고 Backend Agent와 Review Agent가 구현과 검수를 수행하게 한다.

Q. PM Agent가 단순 CRUD를 발견하면 어떻게 해야 하는가?

A. Layered Architecture 기반 단순 구현을 지시하고 과도한 Pattern 적용을 금지한다.

Q. PM Agent가 외부 시스템 연동을 발견하면?

A. Adapter, Port, Timeout, Retry, 예외 변환, 외부 DTO 격리를 검토 지시한다.

---

# 7. Final Quality Checklist

## 7.1 Design Pattern Document Quality Checklist

### [개념]

Design Pattern Document Quality Checklist는 Design Pattern RAG 문서가 Agent Retrieval, Code Generation, Review, Decision Support에 적합한지 검수하는 기준이다.

이 문서는 사람 학습용 문서보다 Agent Retrieval 최적화를 우선한다.

---

### [핵심]

- Pattern 목적이 명확한가?
- Problem, Pattern, Solution, Trade-off가 포함되었는가?
- SOLID와 연결되었는가?
- Spring Boot 3.x, Java 21 기준 실무 예시가 있는가?
- Pattern 남용 주의가 포함되었는가?
- FAQ가 충분한가?
- Retrieval Queries가 포함되었는가?
- 용어가 일관되는가?
- Agent별 사용 기준이 명확한가?
- Troubleshooting이 문제, 원인, 해결 형식인가?

---

### [Checklist]

Document Structure:

- [개념] 포함
- [핵심] 포함
- [실무] 포함
- [FAQ] 포함
- [Flow] 또는 예제 포함
- [주의] 포함
- [Troubleshooting] 포함
- Retrieval Queries 포함

Retrieval Optimization:

- 핵심 키워드 반복 포함
- Pattern 이름 영어 표기 유지
- Spring Boot 실무 키워드 포함
- SOLID 키워드 포함
- Agent 역할 키워드 포함
- 질문형 FAQ 충분히 포함
- Chunk 단위 독립 검색 가능

Content Quality:

- Pattern 목적이 명확함
- Pattern 오용 방지 포함
- Trade-off 포함
- 코드 예제 짧음
- 외부 기술 기준 최신성 유지
- Java 21 / Spring Boot 3.x 기준 유지
- Legacy 중심 설명 제외

Agent Usability:

- Backend Agent가 코드 생성에 사용할 수 있음
- Review Agent가 구조 검수에 사용할 수 있음
- PM Agent가 요구사항 분류에 사용할 수 있음
- Pattern Selection 기준이 있음
- Troubleshooting 기준이 있음
- Over Engineering 방지 기준이 있음

---

### [주의]

- FAQ가 부족하면 Retrieval Hit가 떨어진다.
- 긴 문단은 Chunk 검색 품질을 낮춘다.
- Pattern 이름만 있고 문제 상황이 없으면 Agent가 잘못 적용할 수 있다.
- 좋은 Pattern 설명보다 잘못 쓰는 경우 설명이 더 중요할 수 있다.
- RAG 문서는 사람이 읽는 책이 아니라 Agent가 검색하고 판단하는 기준이다.

---

### [FAQ]

Q. Design Pattern RAG 문서 품질은 무엇으로 결정되는가?

A. Pattern 목적, 문제 상황, 적용 기준, Trade-off, FAQ, Troubleshooting 품질로 결정된다.

Q. Design Pattern 문서에서 FAQ가 중요한 이유는?

A. 사용자 질문과 Agent Query가 FAQ 형태로 검색될 가능성이 높기 때문이다.

Q. Design Pattern 문서에서 Troubleshooting이 중요한 이유는?

A. Review Agent가 실제 코드 문제를 찾고 개선안을 제시하는 데 직접 사용하기 때문이다.

Q. Design Pattern 문서의 최종 목표는?

A. Agent가 Pattern을 검색하고 적절히 적용하며 잘못된 구조를 검수할 수 있게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Design Pattern Review란?
A. 코드 구조가 문제에 맞는 Pattern을 사용하고 있는지, Pattern 남용이나 구조 문제는 없는지 검수하는 과정이다.

Q. Design Pattern Review에서 가장 중요한 기준은?
A. 문제, 책임, 변경 지점, 의존성, Trade-off이다.

Q. Review Agent는 어떤 형식으로 결과를 작성해야 하는가?
A. 문제, 원인, 해결, 관련 Pattern, 주의 형식으로 작성하는 것이 좋다.

Q. Pattern을 사용하지 않는 것도 좋은 Review 결과인가?
A. 그렇다. 단순한 문제에는 단순한 구조가 더 좋은 설계일 수 있다.

Q. Review Agent는 무엇을 먼저 확인해야 하는가?
A. 책임 분리와 변경 이유를 먼저 확인해야 한다.

Q. Pattern 후보는 어떻게 선택하는가?
A. 생성, 구조, 행동, 아키텍처 문제 중 어디에 해당하는지 분류한 뒤 선택한다.

Q. Review Agent가 반드시 Pattern을 추천해야 하는가?
A. 아니다. 단순 구조 유지나 불필요한 Pattern 제거를 추천할 수도 있다.

Q. Pattern Abuse란?
A. 필요하지 않은 곳에 Pattern을 과도하게 적용하여 코드 복잡도를 높이는 문제이다.

Q. Pattern Abuse를 줄이는 기준은?
A. 현재 문제, 변경 가능성, 테스트 가치, 팀 이해도, 일정 비용을 기준으로 판단한다.

Q. Pattern을 제거하는 것도 Refactoring인가?
A. 그렇다. 불필요한 추상화를 제거하는 것도 중요한 Refactoring이다.

Q. Tight Coupling이란?
A. 객체나 모듈이 강하게 의존하여 변경, 테스트, 확장이 어려운 상태이다.

Q. Tight Coupling의 대표 신호는?
A. 외부 Client 직접 의존, 순환 의존, 구현체 교체 어려움, 테스트 대체 어려움이다.

Q. Tight Coupling을 줄이는 Pattern은?
A. Adapter, Strategy, Observer, Mediator, Hexagonal Architecture가 도움이 된다.

Q. Excessive Abstraction이란?
A. 실제 필요보다 Interface, Abstract Class, Port, Adapter를 과도하게 적용해 복잡도를 높이는 문제이다.

Q. Interface 구현체가 하나뿐이면 나쁜가?
A. 항상 나쁜 것은 아니지만 교체 가능성, 테스트 가치, 외부 의존성 격리 목적이 없으면 불필요할 수 있다.

Q. `Service`와 `ServiceImpl` 구조는 항상 필요한가?
A. 아니다. 구현체가 하나라면 불필요한 추상화일 수 있다.

Q. Wrong Pattern Choice란?
A. 실제 문제와 맞지 않는 Pattern을 선택하여 구조가 복잡해지거나 문제를 해결하지 못하는 상황이다.

Q. Wrong Pattern Choice를 줄이는 방법은?
A. 문제를 생성, 구조, 행동, 아키텍처 문제로 먼저 분류한 뒤 Pattern을 선택한다.

Q. Adapter와 Decorator의 차이는?
A. Adapter는 인터페이스 변환이 목적이고 Decorator는 기능 확장이 목적이다.

Q. Strategy와 Template Method의 차이는?
A. Strategy는 알고리즘 전체 교체가 목적이고 Template Method는 공통 흐름 고정과 일부 단계 변경이 목적이다.

Q. SRP Violation이란?
A. 하나의 Class 또는 Module이 여러 변경 이유를 가져 책임이 과도하게 집중된 상태이다.

Q. SRP Violation을 어떻게 찾는가?
A. 검증, 계산, 저장, 외부 호출, 알림 같은 여러 책임이 한 Class에 섞였는지 확인한다.

Q. OCP Violation이란?
A. 새로운 기능 추가 시 기존 코드를 계속 수정해야 하는 구조이다.

Q. OCP Violation 해결에 적합한 Pattern은?
A. Strategy, Factory, Template Method, Adapter가 자주 사용된다.

Q. LSP Violation이란?
A. 하위 타입이 상위 타입을 대체했을 때 정상 동작하지 않는 문제이다.

Q. LSP Violation의 대표 신호는?
A. 자식 Class가 부모 메서드에서 `UnsupportedOperationException`을 던지는 경우이다.

Q. ISP Violation이란?
A. Client가 사용하지 않는 메서드에 의존하거나 구현체가 불필요한 메서드를 강제로 구현하는 문제이다.

Q. DIP Violation이란?
A. 고수준 정책 모듈이 저수준 구현체에 직접 의존하는 문제이다.

Q. Spring DI를 쓰면 DIP Violation이 자동으로 해결되는가?
A. 아니다. 구현체에 직접 의존하면 DI를 사용해도 DIP 위반이다.

Q. Factory Troubleshooting의 핵심 기준은?
A. Factory가 생성 또는 선택 책임만 가지는지, 비즈니스 정책을 포함하지 않는지 검수하는 것이다.

Q. Builder Troubleshooting의 핵심 기준은?
A. 필수값 검증, Domain Invariant 보호, Entity Builder 남용 여부이다.

Q. Adapter Troubleshooting의 핵심 기준은?
A. 외부 DTO 침투, 비즈니스 로직 포함, Port 외부 종속, DIP 위반 여부이다.

Q. Strategy Troubleshooting의 핵심 기준은?
A. 알고리즘 교체 필요성, Strategy 과도화, 선택 책임 위치, Stateless 여부이다.

Q. Observer Troubleshooting의 핵심 기준은?
A. Event Flow 가시성, Listener 실패 처리, Transaction 시점, Payload 크기, 멱등성이다.

Q. Proxy Troubleshooting의 핵심 기준은?
A. Proxy를 거치는 호출인지, Self Invocation이 있는지, Transaction과 Lazy Loading 범위가 맞는지 확인하는 것이다.

Q. Self Invocation에서 `@Transactional`이 안 되는 이유는?
A. 같은 객체 내부 호출은 Spring Proxy를 거치지 않기 때문이다.

Q. `new`로 만든 객체에 AOP가 적용되는가?
A. 아니다. Spring Container가 관리하는 Proxy Bean을 통해 호출해야 한다.

Q. LazyInitializationException 해결 방법은?
A. Transaction 안에서 조회하거나 Fetch Join, EntityGraph, DTO Projection을 사용한다.

Q. Layer Violation Troubleshooting은 무엇을 검수하는가?
A. 각 계층이 자신의 책임을 벗어났는지, 잘못된 계층에 의존하는지 검수한다.

Q. Dependency Direction Troubleshooting은 무엇을 검수하는가?
A. 내부 Core가 외부 구현체에 직접 의존하는지, Port와 Adapter 방향이 올바른지 검수한다.

Q. Domain Leakage Troubleshooting은 무엇을 검수하는가?
A. 핵심 Domain Rule이 외부 계층이나 DTO, Adapter에 흩어져 있는지 검수한다.

Q. Over Engineering Architecture Troubleshooting은 무엇을 검수하는가?
A. 문제 복잡도에 비해 계층, Interface, Port, Adapter가 과도한지 검수한다.

Q. Backend Agent는 Design Pattern을 언제 적용해야 하는가?
A. 변경 지점, 외부 의존성, 정책 교체, 후속 작업, 재시도 필요성이 있을 때 적용한다.

Q. Backend Agent는 단순 CRUD에 어떤 구조를 써야 하는가?
A. Layered Architecture를 우선 사용한다.

Q. Backend Agent는 외부 API 연동을 어떻게 설계해야 하는가?
A. 외부 API Client를 Adapter로 감싸고 내부 Service는 Port 또는 내부 Result에 의존하게 한다.

Q. Review Agent는 무엇을 우선 검수해야 하는가?
A. 책임 분리, 의존성 방향, 외부 DTO 침투, Pattern 적합성, Over Engineering을 우선 검수한다.

Q. Review Agent는 Pattern 제거를 제안할 수 있는가?
A. 그렇다. 불필요한 Pattern은 제거하는 것이 더 좋은 Refactoring일 수 있다.

Q. PM Agent는 Design Pattern을 어떻게 활용하는가?
A. 요구사항을 설계 문제로 분류하고 적절한 Pattern 후보와 검수 포인트를 다른 Agent에게 전달한다.

Q. PM Agent가 단순 CRUD를 발견하면 어떻게 해야 하는가?
A. Layered Architecture 기반 단순 구현을 지시하고 과도한 Pattern 적용을 금지한다.

Q. PM Agent가 외부 시스템 연동을 발견하면?
A. Adapter, Port, Timeout, Retry, 예외 변환, 외부 DTO 격리를 검토 지시한다.

Q. Design Pattern RAG 문서 품질은 무엇으로 결정되는가?
A. Pattern 목적, 문제 상황, 적용 기준, Trade-off, FAQ, Troubleshooting 품질로 결정된다.

Q. Design Pattern 문서에서 FAQ가 중요한 이유는?
A. 사용자 질문과 Agent Query가 FAQ 형태로 검색될 가능성이 높기 때문이다.

Q. Design Pattern 문서에서 Troubleshooting이 중요한 이유는?
A. Review Agent가 실제 코드 문제를 찾고 개선안을 제시하는 데 직접 사용하기 때문이다.

Q. Design Pattern 문서의 최종 목표는?
A. Agent가 Pattern을 검색하고 적절히 적용하며 잘못된 구조를 검수할 수 있게 만드는 것이다.
