# Java Part03 — OOP Core

---

# 1. Object Oriented Programming Foundation

## 1.1 OOP Purpose

### [개념]

Object Oriented Programming은 프로그램을 객체의 책임, 상태, 행위, 협력으로 구성하는 설계 방식이다.

Java는 객체지향 언어이며 Class, Object, Method, Field를 통해 객체지향 구조를 표현한다.

Java OOP 문서는 문법 설명이 아니라 Backend Agent / Review Agent가 Java 기반 백엔드 코드를 객체 책임 중심으로 생성하고 검토하기 위한 RAG 문서다.

---

### [핵심]

OOP 핵심 요소:

- Object Oriented Programming
- OOP
- Object
- Class
- Responsibility
- State
- Behavior
- Encapsulation
- Inheritance
- Composition
- Polymorphism
- Abstraction
- Interface
- Method
- Collaboration
- Dependency

OOP 4대 특성:

```text
Encapsulation
Inheritance
Polymorphism
Abstraction
```

OOP 설계 기준:

- 객체는 명확한 책임을 가진다.
- 객체는 자신의 상태를 보호한다.
- 객체는 Method를 통해 행위를 제공한다.
- 객체 간 협력은 역할과 메시지 중심으로 설계한다.
- 변경 가능성이 큰 부분은 추상화한다.
- 상속보다 조합을 우선 검토한다.

---

### [실무]

2026 백엔드 실무에서 OOP는 Spring Boot Layered Architecture, Domain Model, Service 설계, Entity 상태 변경, Testing 구조의 기반이다.

OOP 설계 Flow:

```text
Requirement
→ Domain Concept 식별
→ Object Responsibility 도출
→ State / Behavior 분리
→ Class 설계
→ Collaboration 설계
→ Encapsulation 적용
→ Inheritance / Composition 판단
→ Polymorphism 적용 여부 판단
→ Review
```

Spring Boot 연결:

```text
Controller
→ Request 수신

Service
→ Use Case 흐름 조정

Entity
→ 도메인 상태와 행위

Repository
→ 데이터 접근 역할

Policy / Strategy
→ 변하는 규칙 추상화

DTO
→ 데이터 전달
```

주의:

- OOP는 Class를 많이 만드는 것이 아니다.
- 객체 책임이 불명확하면 Class가 많아도 좋은 설계가 아니다.
- 모든 로직을 Service에 넣으면 객체지향성이 약해질 수 있다.
- Entity가 Getter / Setter만 가지면 Anemic Domain Model 가능성이 있다.
- OOP 설계는 테스트 가능성과 유지보수성에 직접 영향을 준다.

---

### [FAQ]

Q. OOP는 Class를 많이 만드는 거야?
A. 아니다. 객체 책임과 협력을 명확히 설계하는 것이 핵심이다.

Q. Java에서 OOP가 중요한 이유는?
A. Spring Boot, JPA Entity, Service, DTO, 테스트 코드가 모두 Class와 객체 협력으로 구성되기 때문이다.

Q. OOP 설계에서 가장 먼저 볼 것은?
A. Class가 어떤 책임을 가지는지 먼저 확인하는 것이 좋다.

---

## 1.2 Responsibility Driven Design Rules

### [개념]

Responsibility Driven Design은 객체가 무엇을 알고, 무엇을 수행해야 하는지를 책임 중심으로 설계하는 방식이다.

객체 책임은 Field보다 먼저 판단해야 한다.

---

### [핵심]

책임 중심 설계 키워드:

- Responsibility
- Role
- Collaboration
- Message
- State
- Behavior
- Cohesion
- Coupling
- Change Reason
- Use Case
- Domain Rule

책임 질문:

```text
이 객체는 무엇을 책임지는가?
이 객체가 알아야 하는 정보는 무엇인가?
이 객체가 수행해야 하는 행위는 무엇인가?
이 객체가 협력해야 하는 객체는 무엇인가?
이 책임은 이 객체에 자연스러운가?
```

---

### [실무]

책임 분리 기준:

```text
요청 처리 책임 → Controller
흐름 조정 책임 → Service
상태와 규칙 책임 → Entity
데이터 접근 책임 → Repository
전달 책임 → DTO
외부 시스템 통신 책임 → Client
검증 책임 → Validator
변환 책임 → Mapper
정책 책임 → Policy / Strategy
```

나쁜 예:

```java
public class UserService {
    public void addPoint(User user, int point) {
        if (point <= 0) {
            throw new IllegalArgumentException("point must be positive");
        }

        user.setPoint(user.getPoint() + point);
    }
}
```

좋은 예:

```java
public class User {
    private int point;

    public void addPoint(int point) {
        if (point <= 0) {
            throw new IllegalArgumentException("point must be positive");
        }

        this.point += point;
    }
}
```

Service 역할:

```java
@Transactional
public void rewardUser(Long userId, int point) {
    User user = userRepository.findById(userId)
        .orElseThrow(() -> new UserNotFoundException(userId));

    user.addPoint(point);
}
```

주의:

- 객체가 스스로 처리할 수 있는 규칙을 Service가 대신 처리하는지 확인한다.
- DTO에 도메인 책임을 넣지 않는다.
- Repository에 비즈니스 규칙을 넣지 않는다.
- 책임이 흩어지면 변경 시 여러 Class를 수정해야 한다.

---

### [FAQ]

Q. 객체 책임은 어떻게 찾을 수 있어?
A. 요구사항에서 명사와 동사를 분리하고, 상태와 행위가 자연스럽게 모이는 단위를 찾는다.

Q. Service가 모든 비즈니스 로직을 가져도 돼?
A. 아니다. Service는 흐름을 조정하고 도메인 상태 변경 규칙은 Entity나 Domain Object가 가질 수 있다.

Q. 책임 분리가 잘못되면 뭐가 문제야?
A. 변경 비용이 커지고 테스트가 어려워지며 같은 규칙이 여러 곳에 중복될 수 있다.

---

# 2. Encapsulation Rules

## 2.1 Encapsulation Basics

### [개념]

Encapsulation은 객체 내부 상태를 숨기고 정해진 Method를 통해서만 상태를 조회하거나 변경하게 하는 객체지향 원칙이다.

Encapsulation은 데이터 은닉이 아니라 상태 변경 규칙을 객체 내부에 모으는 설계 기준이다.

---

### [핵심]

Encapsulation 핵심:

- Encapsulation
- Information Hiding
- Private Field
- Public Method
- Controlled Mutation
- State Protection
- Invariant
- Business Rule
- Meaningful Method
- Setter Restriction

목적:

```text
객체 상태 보호
상태 변경 규칙 집중
잘못된 상태 방지
변경 영향 범위 축소
도메인 규칙 위치 명확화
유지보수성 향상
```

---

### [실무]

Encapsulation 기본 규칙:

- Field는 private 우선
- 외부에서 Field 직접 변경 금지
- Setter 남용 금지
- 상태 변경은 의미 있는 Method로 표현
- Method 내부에서 Validation 수행
- 객체 불변 조건을 Method 안에서 보호
- 내부 Collection 직접 노출 금지

나쁜 예:

```java
user.setPoint(user.getPoint() + 100);
```

좋은 예:

```java
user.addPoint(100);
```

좋은 Entity Method:

```java
public void addPoint(int point) {
    if (point <= 0) {
        throw new IllegalArgumentException("point must be positive");
    }

    this.point += point;
}
```

주의:

- Getter가 있다고 Encapsulation이 깨지는 것은 아니다.
- Setter가 많으면 상태 변경 규칙이 외부로 흩어진다.
- public Field는 거의 금지에 가깝게 검토한다.
- Lombok `@Setter` 전체 적용은 신중해야 한다.
- JPA Entity도 캡슐화 기준을 적용할 수 있다.

---

### [FAQ]

Q. Encapsulation은 단순히 Field를 private으로 만드는 거야?
A. 아니다. 상태 변경 규칙을 객체 내부 Method에 모아 객체 일관성을 지키는 것이 핵심이다.

Q. Setter는 무조건 금지야?
A. 무조건 금지는 아니지만 비즈니스 상태 변경은 의미 있는 Method로 표현하는 것이 좋다.

Q. Getter는 써도 돼?
A. 가능하다. 다만 Getter로 꺼낸 값을 외부에서 계산해 다시 Setter로 넣는 패턴은 주의해야 한다.

---

## 2.2 Meaningful Method Rules

### [개념]

Meaningful Method는 단순 Setter 대신 도메인 의미와 상태 변경 규칙을 이름과 내부 로직으로 표현하는 Method다.

객체의 상태 변경은 `setX()`보다 `activate()`, `deactivate()`, `addPoint()`, `publish()`처럼 의미가 드러나야 한다.

---

### [핵심]

Meaningful Method 핵심:

- Meaningful Method
- Domain Method
- Command Method
- State Transition
- Validation
- Business Rule
- Invariant Protection
- Method Naming
- Controlled Mutation

예시 이름:

```text
activate
deactivate
publish
cancel
approve
reject
addPoint
changeEmail
increaseViewCount
markAsRead
completePayment
```

---

### [실무]

나쁜 예:

```java
post.setStatus(PostStatus.PUBLISHED);
```

좋은 예:

```java
post.publish();
```

상태 변경 Method 예:

```java
public void publish() {
    if (this.status != PostStatus.DRAFT) {
        throw new IllegalStateException("only draft post can be published");
    }

    if (this.content == null || this.content.isBlank()) {
        throw new IllegalStateException("content must not be blank");
    }

    this.status = PostStatus.PUBLISHED;
    this.publishedAt = LocalDateTime.now();
}
```

실무 기준:

- Method 이름으로 상태 변경 의도를 드러낸다.
- Method 내부에서 변경 가능 조건을 검증한다.
- 관련 Field 변경은 하나의 Method 안에서 처리한다.
- 외부에서 상태 변경 순서를 알 필요 없게 만든다.
- Service는 Entity Method를 호출해 흐름을 조정한다.

주의:

- 의미 없는 `update()`는 책임이 모호할 수 있다.
- Method 이름과 실제 변경 내용이 다르면 위험하다.
- Method가 너무 많은 상태를 변경하면 책임 분리 검토.
- 시간 값 설정 정책은 도메인 / Auditing 기준을 통일한다.

---

### [FAQ]

Q. Setter 대신 Meaningful Method를 쓰는 이유는?
A. 상태 변경 의도와 비즈니스 규칙을 Method 안에 모아 객체 일관성을 지키기 위해서다.

Q. Entity에 publish 같은 Method를 넣어도 돼?
A. 가능하다. Entity 자신의 상태 전이 규칙이라면 Entity Method로 표현하는 것이 좋다.

Q. update라는 Method 이름은 나쁜가?
A. 무조건 나쁘지는 않지만 무엇을 어떻게 변경하는지 모호하면 더 구체적인 이름이 좋다.

---

## 2.3 Invariant Protection Rules

### [개념]

Invariant는 객체가 항상 지켜야 하는 불변 조건이다.

Encapsulation은 객체의 Invariant를 보호하기 위한 핵심 수단이다.

---

### [핵심]

Invariant 핵심:

- Invariant
- Valid State
- Invalid State
- State Rule
- Validation
- Constructor Validation
- Method Validation
- Domain Constraint
- Consistency

Invariant 예:

```text
email은 null 또는 blank일 수 없다.
point는 0보다 작을 수 없다.
deleted user는 active 상태가 될 수 없다.
endDate는 startDate보다 빠를 수 없다.
published post는 content가 비어 있을 수 없다.
payment amount는 0보다 커야 한다.
```

---

### [실무]

Invariant 보호 위치:

```text
생성 시점 규칙 → Constructor / Static Factory Method
상태 변경 규칙 → Domain Method
입력 형식 검증 → Request DTO Validation
비즈니스 흐름 검증 → Service
DB 무결성 → Constraint
```

예:

```java
public record Period(LocalDate startDate, LocalDate endDate) {
    public Period {
        if (startDate == null || endDate == null) {
            throw new IllegalArgumentException("date must not be null");
        }

        if (startDate.isAfter(endDate)) {
            throw new IllegalArgumentException("startDate must be before endDate");
        }
    }
}
```

Entity 예:

```java
public void changeEmail(String newEmail) {
    if (newEmail == null || newEmail.isBlank()) {
        throw new IllegalArgumentException("email must not be blank");
    }

    this.email = newEmail;
}
```

주의:

- DB Constraint만 믿고 Domain Invariant를 방치하지 않는다.
- DTO Validation과 Domain Validation은 목적이 다르다.
- Setter가 많으면 Invariant 보호가 어려워진다.
- 관련 Field가 따로 변경되면 중간에 잘못된 상태가 생길 수 있다.

---

### [FAQ]

Q. Invariant는 뭐야?
A. 객체가 항상 만족해야 하는 상태 규칙이다.

Q. Invariant는 어디서 검증해?
A. 생성 시점은 Constructor나 Factory Method, 상태 변경 시점은 Domain Method에서 검증하는 것이 좋다.

Q. DTO Validation이 있으면 Entity 검증은 필요 없어?
A. 아니다. DTO Validation은 입력 경계 검증이고 Entity 검증은 도메인 상태 보호다.

---

## 2.4 Collection Encapsulation Rules

### [개념]

Collection Encapsulation은 객체 내부 Collection Field를 외부에서 직접 수정하지 못하게 보호하는 규칙이다.

내부 Collection을 그대로 반환하면 외부에서 객체 상태를 우회 변경할 수 있다.

---

### [핵심]

Collection Encapsulation 핵심:

- Collection Field
- Mutable Collection
- Defensive Copy
- Unmodifiable List
- Add Method
- Remove Method
- State Protection
- Association Method
- Orphan Removal

위험 패턴:

```text
getComments().add(comment)
getItems().clear()
public List field
내부 List 직접 반환
Collection Setter 제공
```

---

### [실무]

나쁜 예:

```java
public List<Comment> getComments() {
    return comments;
}
```

좋은 예:

```java
public List<Comment> getComments() {
    return Collections.unmodifiableList(comments);
}

public void addComment(Comment comment) {
    if (comment == null) {
        throw new IllegalArgumentException("comment must not be null");
    }

    this.comments.add(comment);
}
```

JPA 연관관계 예:

```java
public void addComment(Comment comment) {
    comments.add(comment);
    comment.assignPost(this);
}
```

실무 기준:

- 내부 Collection은 private으로 둔다.
- 외부에는 수정 불가 View 또는 복사본 제공.
- 추가 / 삭제는 의미 있는 Method로 제공.
- 양방향 연관관계는 편의 Method로 일관성 유지.
- Collection Setter는 지양한다.
- orphanRemoval 사용 시 삭제 Method 정책을 명확히 한다.

주의:

- `Collections.unmodifiableList()`는 View라 내부 List 변경은 반영된다.
- 방어적 복사가 필요한지 판단한다.
- JPA Entity에서 완전한 불변 Collection 처리에는 주의가 필요하다.
- 대량 Collection 조회는 성능 문제와 Lazy Loading을 함께 고려한다.

---

### [FAQ]

Q. 내부 List를 그대로 반환하면 왜 위험해?
A. 외부에서 List를 직접 수정해 객체 상태 규칙을 우회할 수 있기 때문이다.

Q. Collection Setter는 써도 돼?
A. 지양한다. add/remove 같은 의미 있는 Method로 변경을 제어하는 것이 좋다.

Q. JPA 양방향 연관관계에서는 무엇을 조심해야 해?
A. 양쪽 객체의 관계가 일관되도록 연관관계 편의 Method를 사용하는 것이 좋다.

---

# 3. Inheritance Rules

## 3.1 Inheritance Basics

### [개념]

Inheritance는 부모 Class의 Field와 Method를 자식 Class가 물려받는 객체지향 기능이다.

Inheritance는 is-a 관계와 다형성이 명확할 때 사용한다.

---

### [핵심]

Inheritance 핵심:

- Inheritance
- Parent Class
- Child Class
- Super Class
- Sub Class
- extends
- is-a relationship
- Method Overriding
- Polymorphism
- Code Reuse
- Fragile Base Class

상속 사용 조건:

```text
명확한 is-a 관계가 있다.
부모 타입으로 자식 객체를 다룰 필요가 있다.
공통 상태나 동작이 자연스럽다.
다형성이 필요하다.
부모 변경이 자식에 미치는 영향을 감당할 수 있다.
```

---

### [실무]

상속 판단 Flow:

```text
정말 is-a 관계인가?
→ 부모 타입으로 사용해야 하는가?
→ 공통 동작이 안정적인가?
→ 하위 Class가 부모 규칙을 깨지 않는가?
→ Composition으로 대체할 수 없는가?
→ 상속 적용
```

예:

```java
public abstract class NotificationSender {
    public abstract void send(String message);
}

public class EmailNotificationSender extends NotificationSender {
    @Override
    public void send(String message) {
        // send email
    }
}
```

주의:

- 코드 재사용만을 위한 상속은 지양한다.
- 깊은 상속 계층은 변경과 이해를 어렵게 만든다.
- 부모 Class의 protected Field 남용은 캡슐화를 약화시킨다.
- 부모 변경이 모든 자식에 영향을 줄 수 있다.
- JPA Entity 상속은 DB 매핑 전략까지 고려해야 한다.

---

### [FAQ]

Q. 상속은 언제 써?
A. 명확한 is-a 관계와 다형성이 필요할 때 사용한다.

Q. 코드 재사용을 위해 상속해도 돼?
A. 코드 재사용만 목적이라면 상속보다 조합을 우선 검토하는 것이 좋다.

Q. 상속이 위험한 이유는?
A. 부모 변경이 자식에 영향을 주고 깊은 계층이 생기면 구조 이해가 어려워지기 때문이다.

---

## 3.2 Is-a Relationship Rules

### [개념]

is-a 관계는 자식 객체가 부모 객체의 한 종류라고 말할 수 있는 관계다.

상속은 is-a 관계가 명확할 때만 자연스럽다.

---

### [핵심]

is-a 판단 기준:

- A is a B
- Semantic Consistency
- Substitution
- Liskov Substitution
- Parent Contract
- Child Behavior
- Polymorphic Use

질문:

```text
EmailSender는 NotificationSender인가?
AdminUser는 User인가?
Car는 Vehicle인가?
DiscountPolicy 구현체는 DiscountPolicy인가?
```

---

### [실무]

좋은 is-a 예:

```text
FixedDiscountPolicy is a DiscountPolicy
RateDiscountPolicy is a DiscountPolicy
EmailNotificationSender is a NotificationSender
SmsNotificationSender is a NotificationSender
```

위험한 is-a 예:

```text
Stack is a List
UserService is a User
PaymentUtil is a Payment
```

검토 기준:

- 부모 타입으로 자식 객체를 대체해도 의미가 깨지지 않는가?
- 부모의 모든 규칙을 자식이 지킬 수 있는가?
- 자식이 부모 Method 일부를 사용하지 못하게 막고 있지 않은가?
- 단순 기능 공유라면 조합이 더 적합하지 않은가?

주의:

- 이름만 비슷하다고 is-a 관계가 아니다.
- 하위 Class가 부모 Method를 예외로 막으면 설계 오류 가능성이 있다.
- Entity 상속은 도메인 의미와 DB 구조를 함께 검토한다.

---

### [FAQ]

Q. is-a 관계는 어떻게 확인해?
A. “A는 B의 한 종류다”라고 자연스럽게 말할 수 있고 부모 타입으로 대체 가능해야 한다.

Q. 부모 Method를 자식이 못 쓰게 막으면 안 좋아?
A. 대체 가능성이 깨지는 신호일 수 있어 상속 구조를 재검토해야 한다.

Q. is-a가 애매하면 어떻게 해?
A. 상속보다 조합이나 Interface를 먼저 검토한다.

---

## 3.3 Inheritance Anti Pattern Rules

### [개념]

Inheritance Anti Pattern은 상속을 잘못 사용해 결합도 증가, 계층 복잡도 증가, 부모-자식 규칙 충돌을 만드는 패턴이다.

---

### [핵심]

상속 Anti Pattern:

- Code Reuse Only Inheritance
- Deep Inheritance Hierarchy
- Fragile Base Class
- Protected Field Abuse
- Override with Empty Method
- Unsupported Operation
- Parent Contract Violation
- Utility Base Class
- God Parent Class

---

### [실무]

나쁜 예:

```java
public class CommonService {
    protected void log() {
    }

    protected void validate() {
    }

    protected void sendMail() {
    }
}

public class UserService extends CommonService {
}
```

개선 방향:

```text
Logging → AOP / Logger
Validation → Validator
Mail Sending → MailClient
공통 흐름 → Template Method 검토
단순 기능 재사용 → Composition
```

검토 Flow:

```text
상속 이유 확인
→ is-a 관계 확인
→ 부모 Method 재사용 목적 확인
→ Override 구조 확인
→ protected Field 확인
→ Composition 대체 가능성 확인
```

주의:

- CommonBaseClass는 God Class가 되기 쉽다.
- 자식 Class가 부모 기능 일부만 필요하면 상속 부적합 가능성이 높다.
- 상속으로 의존성을 숨기면 테스트가 어려워진다.
- Spring Service 상속 구조는 신중하게 사용한다.

---

### [FAQ]

Q. 공통 기능을 부모 Class에 넣고 상속하면 안 돼?
A. 단순 재사용 목적이라면 조합, Utility, Component, AOP 등을 먼저 검토하는 것이 좋다.

Q. 깊은 상속 구조는 왜 문제야?
A. 동작을 이해하려면 여러 부모 Class를 추적해야 하고 부모 변경 영향이 커지기 때문이다.

Q. protected Field는 왜 조심해야 해?
A. 자식 Class가 부모 내부 상태에 직접 의존해 캡슐화가 약해질 수 있다.

---

# 4. Composition Rules

## 4.1 Composition Basics

### [개념]

Composition은 객체가 다른 객체를 Field로 가지고 그 객체에게 작업을 위임하는 설계 방식이다.

Composition은 has-a 관계를 표현하며 상속보다 변경에 유연한 경우가 많다.

---

### [핵심]

Composition 핵심:

- Composition
- has-a relationship
- Delegation
- Collaboration
- Dependency
- Component
- Strategy
- Policy
- Service Dependency
- Flexibility
- Testability

Composition 사용 조건:

```text
has-a 관계다.
역할을 다른 객체에게 위임할 수 있다.
구현체 교체 가능성이 있다.
상속 계층을 만들 필요가 없다.
테스트에서 Mock 대체가 필요하다.
변경에 유연해야 한다.
```

---

### [실무]

Composition 예:

```java
public class OrderService {
    private final DiscountPolicy discountPolicy;

    public OrderService(DiscountPolicy discountPolicy) {
        this.discountPolicy = discountPolicy;
    }

    public int calculateDiscount(int price) {
        return discountPolicy.discount(price);
    }
}
```

Spring Boot 연결:

```text
Service has a Repository
Service has a Policy
Service has a Client
Controller has a Service
Validator has a Rule
```

상속 대신 조합:

```text
UserService extends CommonService

대신

UserService has a MailClient
UserService has a UserValidator
UserService has a PasswordEncoder
```

주의:

- Composition도 의존성이 많아지면 Class 책임 과다 신호다.
- 생성자 주입으로 의존성을 명확히 드러낸다.
- 순환 의존이 생기면 책임 분리 재검토.
- 단순 값 객체와 Service 의존성을 구분한다.

---

### [FAQ]

Q. Composition은 뭐야?
A. 객체가 다른 객체를 포함하고 필요한 작업을 위임하는 설계 방식이다.

Q. 상속보다 조합을 우선하라는 말은 뭐야?
A. 기능 재사용만 목적이라면 상속보다 객체를 포함하고 위임하는 방식이 더 유연하다는 뜻이다.

Q. Composition이 많으면 무조건 좋은가?
A. 아니다. 의존성이 너무 많으면 Class 책임이 커졌다는 신호일 수 있다.

---

## 4.2 Delegation Rules

### [개념]

Delegation은 객체가 자신이 직접 처리하지 않아도 되는 작업을 적절한 협력 객체에게 맡기는 방식이다.

Composition은 Delegation을 통해 객체 협력을 구성한다.

---

### [핵심]

Delegation 핵심:

- Delegation
- Collaboration
- Responsibility Transfer
- Dependency
- Method Call
- Role Separation
- Testability
- Maintainability

Delegation 질문:

```text
이 객체가 직접 해야 하는 일인가?
더 적절한 책임 객체가 있는가?
위임하면 테스트가 쉬워지는가?
위임 대상이 명확한 역할을 가지는가?
```

---

### [실무]

나쁜 예:

```java
public class UserService {
    public void register(String email, String password) {
        if (!email.contains("@")) {
            throw new IllegalArgumentException("invalid email");
        }

        String encodedPassword = hash(password);

        // send email 직접 구현
        // save user 직접 구현
    }
}
```

좋은 예:

```java
public class UserRegistrationService {
    private final UserValidator userValidator;
    private final PasswordEncoder passwordEncoder;
    private final MailClient mailClient;
    private final UserRepository userRepository;

    public void register(RegisterUserCommand command) {
        userValidator.validate(command);
        String encodedPassword = passwordEncoder.encode(command.password());

        User user = User.create(command.email(), encodedPassword);
        userRepository.save(user);

        mailClient.sendWelcomeMail(user.getEmail());
    }
}
```

주의:

- 위임이 과하면 흐름 추적이 어려울 수 있다.
- 단순 한 줄 로직을 무조건 Class로 분리하지 않는다.
- 위임 대상 이름은 책임을 명확히 표현해야 한다.
- Transaction 경계와 외부 호출 분리 기준을 확인한다.

---

### [FAQ]

Q. Delegation은 언제 사용해?
A. 현재 객체의 책임이 아닌 작업을 더 적절한 객체에게 맡길 때 사용한다.

Q. 위임을 많이 하면 좋은 설계야?
A. 무조건은 아니다. 책임이 명확해지는 경우에만 의미가 있다.

Q. Service에서 Validator나 Client로 분리하는 이유는?
A. 검증, 외부 통신 같은 책임을 분리해 테스트와 변경을 쉽게 하기 위해서다.

---

## 4.3 Composition vs Inheritance Rules

### [개념]

Composition과 Inheritance는 코드 재사용과 객체 관계를 표현하는 두 가지 방식이다.

Inheritance는 is-a 관계를 표현하고 Composition은 has-a 관계를 표현한다.

---

### [핵심]

비교:

| 구분        | Inheritance          | Composition           |
| ----------- | -------------------- | --------------------- |
| 관계        | is-a                 | has-a                 |
| 방식        | 부모 기능 상속       | 객체 포함 / 위임      |
| 결합도      | 높아지기 쉬움        | 상대적으로 낮음       |
| 변경 유연성 | 부모 변경 영향 큼    | 구현체 교체 쉬움      |
| 테스트      | 부모 의존 추적 필요  | Mock 대체 쉬움        |
| 적합        | 다형성 + 의미적 계층 | 기능 위임 + 역할 분리 |

---

### [실무]

선택 기준:

```text
A is a B → Inheritance 검토
A has a B → Composition 검토
코드 재사용 목적만 있음 → Composition 우선
구현체 교체 가능성 있음 → Composition + Interface 검토
부모 타입 다형성이 필요함 → Inheritance / Interface 검토
```

상속 지양 예:

```java
public class UserService extends MailSender {
}
```

조합 권장 예:

```java
public class UserService {
    private final MailSender mailSender;
}
```

주의:

- Composition이 항상 정답은 아니다.
- Framework 확장 구조에서는 상속이 자연스러울 수 있다.
- Template Method Pattern은 상속이 적합할 수 있다.
- 도메인 의미가 없는 상속은 피한다.

---

### [FAQ]

Q. Inheritance와 Composition 차이는?
A. Inheritance는 is-a 관계이고 Composition은 has-a 관계다.

Q. 기능 재사용만 필요하면 뭘 써?
A. 상속보다 Composition을 우선 검토한다.

Q. 상속이 더 좋은 경우도 있어?
A. 명확한 계층 관계와 Template Method 같은 구조가 필요하면 상속이 적합할 수 있다.

---

# 5. Polymorphism Rules

## 5.1 Polymorphism Basics

### [개념]

Polymorphism은 같은 Interface나 부모 타입으로 여러 구현 객체를 다룰 수 있는 객체지향 특성이다.

Polymorphism은 변경 가능한 정책과 구현체를 교체 가능하게 만드는 핵심 설계 도구다.

---

### [핵심]

Polymorphism 핵심:

- Polymorphism
- Interface Based Design
- Parent Type
- Implementation Class
- Method Overriding
- Runtime Dispatch
- Strategy Pattern
- Dependency Inversion
- Extension
- Replacement

사용 대상:

```text
할인 정책
결제 수단
알림 발송 방식
인증 방식
파일 저장 방식
검색 전략
정렬 정책
권한 판단 정책
```

---

### [실무]

다형성 예:

```java
public interface DiscountPolicy {
    int discount(int price);
}
```

```java
public class FixedDiscountPolicy implements DiscountPolicy {
    @Override
    public int discount(int price) {
        return 1000;
    }
}
```

```java
public class RateDiscountPolicy implements DiscountPolicy {
    @Override
    public int discount(int price) {
        return price / 10;
    }
}
```

사용 코드:

```java
public class OrderService {
    private final DiscountPolicy discountPolicy;

    public OrderService(DiscountPolicy discountPolicy) {
        this.discountPolicy = discountPolicy;
    }

    public int calculateDiscount(int price) {
        return discountPolicy.discount(price);
    }
}
```

실무 기준:

- 변하는 정책은 Interface로 분리한다.
- 사용하는 쪽은 구현체가 아니라 역할에 의존한다.
- 구현체 추가 시 기존 사용 코드를 덜 수정하게 만든다.
- 테스트에서는 Mock 구현체로 대체 가능하다.
- Spring Bean 주입과 결합하면 확장성이 좋아진다.

주의:

- 구현체가 하나뿐이고 변경 가능성이 낮으면 Interface가 과할 수 있다.
- 다형성은 if-else를 무조건 없애는 도구가 아니다.
- 구현체 선택 기준이 복잡하면 Factory나 Resolver가 필요할 수 있다.

---

### [FAQ]

Q. Polymorphism은 왜 써?
A. 구현체가 바뀌어도 사용하는 쪽 코드를 크게 바꾸지 않고 확장하기 위해 사용한다.

Q. Interface가 하나의 구현체만 있어도 필요해?
A. 항상 필요하지는 않다. 교체 가능성, 테스트 대체, 외부 의존 추상화가 있으면 검토한다.

Q. 다형성은 Spring Boot에서 어떻게 쓰여?
A. Interface 타입으로 Bean을 주입하고 구현체를 교체하는 방식으로 자주 사용된다.

---

## 5.2 Replace Conditional with Polymorphism

### [개념]

Replace Conditional with Polymorphism은 if-else 또는 switch 분기가 정책별로 계속 늘어날 때, 각 정책을 구현체로 분리하는 리팩터링 방식이다.

---

### [핵심]

적용 신호:

- if-else 분기가 계속 증가
- switch가 type / status 기준으로 커짐
- 분기마다 독립 정책 존재
- 새 정책 추가 시 기존 코드 수정 필요
- 테스트 케이스가 분기별로 많음
- Open Closed Principle 위반 가능성

---

### [실무]

나쁜 예:

```java
public int discount(String type, int price) {
    if ("FIXED".equals(type)) {
        return 1000;
    }

    if ("RATE".equals(type)) {
        return price / 10;
    }

    return 0;
}
```

좋은 예:

```java
public interface DiscountPolicy {
    DiscountType type();
    int discount(int price);
}
```

```java
public class FixedDiscountPolicy implements DiscountPolicy {
    @Override
    public DiscountType type() {
        return DiscountType.FIXED;
    }

    @Override
    public int discount(int price) {
        return 1000;
    }
}
```

Resolver 예:

```java
public class DiscountPolicyResolver {
    private final Map<DiscountType, DiscountPolicy> policies;

    public DiscountPolicyResolver(List<DiscountPolicy> policies) {
        this.policies = policies.stream()
            .collect(Collectors.toMap(DiscountPolicy::type, Function.identity()));
    }

    public DiscountPolicy resolve(DiscountType type) {
        DiscountPolicy policy = policies.get(type);

        if (policy == null) {
            throw new IllegalArgumentException("unsupported discount type");
        }

        return policy;
    }
}
```

주의:

- 분기가 2~3개이고 변경 가능성이 낮으면 단순 if가 더 낫다.
- 다형성 적용으로 Class 수가 늘어난다.
- 구현체 탐색 구조가 필요할 수 있다.
- Enum Method가 더 단순한 해결책일 수도 있다.

---

### [FAQ]

Q. if-else가 많으면 무조건 다형성으로 바꿔?
A. 아니다. 정책이 계속 늘어나거나 변경 가능성이 크면 다형성을 검토한다.

Q. switch문은 항상 나쁜가?
A. 아니다. 고정된 Enum 분기처럼 단순한 경우 switch가 더 읽기 좋을 수 있다.

Q. 다형성 적용 기준은 뭐야?
A. 새 정책 추가 시 기존 코드를 자주 수정해야 한다면 다형성을 검토한다.

---

## 5.3 Strategy Pattern Connection

### [개념]

Strategy Pattern은 변하는 알고리즘이나 정책을 Interface로 분리하고 실행 시점에 구현체를 선택하는 설계 패턴이다.

Polymorphism을 실무적으로 적용하는 대표 패턴이다.

---

### [핵심]

Strategy Pattern 핵심:

- Strategy Pattern
- Policy Interface
- Concrete Strategy
- Context
- Runtime Selection
- Replace Conditional
- Open Closed Principle
- Testability

구성:

```text
Strategy Interface
→ Concrete Strategy A
→ Concrete Strategy B
→ Context / Service
→ Resolver / Factory
```

---

### [실무]

결제 수단 전략 예:

```java
public interface PaymentProcessor {
    PaymentType type();
    void pay(PaymentCommand command);
}
```

```java
public class CardPaymentProcessor implements PaymentProcessor {
    @Override
    public PaymentType type() {
        return PaymentType.CARD;
    }

    @Override
    public void pay(PaymentCommand command) {
        // card payment
    }
}
```

```java
public class PaymentService {
    private final PaymentProcessorResolver resolver;

    public void pay(PaymentCommand command) {
        PaymentProcessor processor = resolver.resolve(command.paymentType());
        processor.pay(command);
    }
}
```

실무 적용 대상:

- 할인 정책
- 결제 처리
- 알림 발송
- 파일 업로드 저장소
- 로그인 Provider 처리
- 권한 판단
- 추천 알고리즘
- 검색 정렬 전략

주의:

- 전략이 적으면 과설계가 될 수 있다.
- 전략 선택 기준이 복잡하면 Resolver 책임이 커질 수 있다.
- 공통 전처리 / 후처리는 Context에서 관리한다.
- 전략 구현체가 너무 많은 의존성을 가지면 역할 분리 검토.

---

### [FAQ]

Q. Strategy Pattern은 언제 써?
A. 실행 정책이나 알고리즘이 여러 개이고 교체 가능성이 있을 때 사용한다.

Q. Strategy Pattern과 Polymorphism은 무슨 관계야?
A. Strategy Pattern은 Polymorphism을 정책 교체 구조로 적용한 대표 패턴이다.

Q. 전략 구현체가 하나뿐이어도 Strategy Pattern을 써?
A. 미래 확장 가능성이 명확하지 않다면 과설계일 수 있다.

---

# 6. Abstraction Rules

## 6.1 Abstraction Basics

### [개념]

Abstraction은 복잡한 구현 세부사항을 숨기고 필요한 역할과 계약만 드러내는 객체지향 원칙이다.

Java에서는 Interface, Abstract Class, Method Signature, DTO, Service Boundary 등을 통해 Abstraction을 표현한다.

---

### [핵심]

Abstraction 핵심:

- Abstraction
- Interface
- Contract
- Role
- Implementation Hiding
- Dependency Inversion
- Public API
- Boundary
- Service Boundary
- Stable Contract

추상화 목적:

```text
구현 세부사항 숨김
역할 중심 설계
구현체 교체 가능
테스트 대체 가능
변경 영향 축소
상위 정책 보호
```

---

### [실무]

추상화 적용 대상:

```text
외부 API Client
파일 저장소
결제 Provider
알림 Sender
인증 Provider
할인 정책
검색 엔진
메일 발송
캐시 저장소
```

예:

```java
public interface MailSender {
    void send(String to, String subject, String body);
}
```

구현체:

```java
public class SmtpMailSender implements MailSender {
    @Override
    public void send(String to, String subject, String body) {
        // SMTP implementation
    }
}
```

주의:

- 추상화는 변경 가능성이 있을 때 가치가 크다.
- 모든 Class에 Interface를 만들면 과한 추상화가 될 수 있다.
- 추상화 이름은 구현 기술보다 역할 중심이어야 한다.
- Interface에 구현 상세를 노출하지 않는다.

---

### [FAQ]

Q. Abstraction은 왜 필요해?
A. 구현 세부사항을 숨기고 역할에 의존하게 만들어 변경 영향을 줄이기 위해 필요하다.

Q. 모든 Service에 Interface를 만들어야 해?
A. 아니다. 구현체 교체 가능성이나 테스트 대체 필요성이 낮으면 과한 추상화가 될 수 있다.

Q. Interface 이름은 어떻게 지어?
A. 구현 기술보다 역할과 계약이 드러나도록 짓는 것이 좋다.

---

## 6.2 Dependency Inversion Rules

### [개념]

Dependency Inversion은 상위 정책 코드가 구체 구현체가 아니라 추상화에 의존하도록 만드는 원칙이다.

Spring Boot에서는 Interface 주입과 Bean 구현체 교체로 자주 적용된다.

---

### [핵심]

Dependency Inversion 핵심:

- Dependency Inversion
- Interface Dependency
- Concrete Class
- High Level Policy
- Low Level Detail
- Bean Injection
- Test Double
- Mock
- Replaceable Implementation

원칙:

```text
상위 모듈은 하위 구현체에 직접 의존하지 않는다.
상위 모듈과 하위 모듈 모두 추상화에 의존한다.
구현 상세는 추상화 뒤로 숨긴다.
```

---

### [실무]

나쁜 예:

```java
public class NotificationService {
    private final SmtpMailSender mailSender = new SmtpMailSender();
}
```

좋은 예:

```java
public class NotificationService {
    private final MailSender mailSender;

    public NotificationService(MailSender mailSender) {
        this.mailSender = mailSender;
    }
}
```

테스트 장점:

```java
class FakeMailSender implements MailSender {
    @Override
    public void send(String to, String subject, String body) {
        // test fake
    }
}
```

실무 기준:

- 외부 시스템 구현체는 Interface 뒤에 둔다.
- Service는 구체 Client보다 역할 Interface에 의존한다.
- 테스트에서 Fake / Mock으로 대체 가능하게 한다.
- 구현체 선택은 Configuration 또는 Spring DI에 맡긴다.

주의:

- 단순 내부 Component까지 무조건 Interface를 만들 필요는 없다.
- Interface가 너무 많으면 구조 탐색 비용이 증가한다.
- 추상화가 실제 변경 가능성을 반영해야 한다.
- 순환 의존이 생기면 책임 분리 오류 가능성이 높다.

---

### [FAQ]

Q. Dependency Inversion은 왜 중요해?
A. 구현체 변경이 상위 비즈니스 코드에 영향을 덜 주고 테스트 대체가 쉬워지기 때문이다.

Q. 구체 Class를 직접 new 하면 왜 안 좋아?
A. 구현체 교체와 테스트 대체가 어려워지고 결합도가 높아질 수 있다.

Q. Spring DI는 Dependency Inversion과 관련 있어?
A. 관련 있다. Interface나 역할 타입으로 Bean을 주입받아 구현체 의존을 낮출 수 있다.

---

# 7. Overloading and Overriding Rules

## 7.1 Overloading Rules

### [개념]

Overloading은 같은 Class 안에서 같은 Method 이름을 사용하되 Parameter 목록을 다르게 정의하는 기능이다.

Return Type만 다르게 하는 것은 Overloading이 아니다.

---

### [핵심]

Overloading 핵심:

- Overloading
- Same Method Name
- Different Parameter
- Compile Time Binding
- Method Signature
- Constructor Overloading
- Readability
- Ambiguity

조건:

```text
Method 이름 동일
Parameter 개수 다름
Parameter 타입 다름
Parameter 순서 다름
Return Type만 다른 것은 불가
```

---

### [실무]

좋은 예:

```java
public User findUser(Long userId) {
    return findUserById(userId);
}

public User findUser(String email) {
    return findUserByEmail(email);
}
```

더 명확한 대안:

```java
public User findUserById(Long userId) {
}

public User findUserByEmail(String email) {
}
```

Constructor Overloading 예:

```java
public Post(String title) {
    this(title, PostStatus.DRAFT);
}

public Post(String title, PostStatus status) {
    this.title = title;
    this.status = status;
}
```

주의:

- 같은 타입 Parameter 순서만 다른 Overloading은 혼동 위험이 크다.
- null 전달 시 어떤 Method가 호출될지 모호할 수 있다.
- 의미가 다르면 이름을 분리하는 것이 더 좋다.
- Overloading이 많으면 API 사용성이 떨어질 수 있다.

---

### [FAQ]

Q. Overloading은 뭐야?
A. 같은 이름의 Method를 Parameter 구성을 다르게 해서 여러 개 정의하는 것이다.

Q. Return Type만 다르면 Overloading이 돼?
A. 안 된다. Parameter 목록이 달라야 한다.

Q. Overloading보다 Method 이름을 다르게 하는 게 나을 때는?
A. 동작 의미가 다르거나 호출자가 혼동할 수 있을 때는 이름을 구체화하는 것이 좋다.

---

## 7.2 Overriding Rules

### [개념]

Overriding은 부모 Class나 Interface의 Method를 자식 Class나 구현 Class에서 재정의하는 기능이다.

Overriding은 Polymorphism의 핵심이다.

---

### [핵심]

Overriding 핵심:

- Overriding
- Parent Method
- Child Method
- Interface Method
- Runtime Dispatch
- Polymorphism
- @Override
- Method Contract
- Liskov Substitution

규칙:

```text
Method 이름 동일
Parameter 동일
Return Type 호환
접근 제어자는 더 좁게 불가
부모 계약을 깨지 않아야 함
```

---

### [실무]

예:

```java
public interface NotificationSender {
    void send(String message);
}
```

```java
public class EmailNotificationSender implements NotificationSender {
    @Override
    public void send(String message) {
        // email send
    }
}
```

권장:

- `@Override` Annotation 사용
- 부모 Method 계약을 지킨다.
- 예외 발생 범위를 무리하게 넓히지 않는다.
- 자식 Method가 부모 의미를 바꾸지 않는다.
- 빈 구현이나 UnsupportedOperationException은 설계 재검토.

주의:

- 부모 Method 일부를 자식이 못 쓰면 상속 구조가 잘못됐을 수 있다.
- Overriding으로 Side Effect가 크게 달라지면 호출자가 예측하기 어렵다.
- Interface default Method override 시 기존 구현 의도를 확인한다.

---

### [FAQ]

Q. Overriding은 뭐야?
A. 부모나 Interface의 Method를 자식 Class에서 재정의하는 것이다.

Q. @Override는 꼭 붙여야 해?
A. 권장한다. 컴파일러가 올바른 재정의인지 확인해준다.

Q. Overriding에서 가장 중요한 기준은?
A. 부모 타입으로 사용해도 의미와 계약이 깨지지 않아야 한다.

---

## 7.3 Overloading vs Overriding Comparison

### [개념]

Overloading과 Overriding은 이름이 비슷하지만 목적과 동작 시점이 다르다.

Overloading은 같은 이름의 Method를 여러 입력 형태로 제공하는 것이고, Overriding은 부모 Method를 자식이 재정의하는 것이다.

---

### [핵심]

비교:

| 구분        | Overloading           | Overriding       |
| ----------- | --------------------- | ---------------- |
| 목적        | 다양한 입력 형태 제공 | 부모 동작 재정의 |
| 위치        | 같은 Class 중심       | 상속 / 구현 관계 |
| Parameter   | 달라야 함             | 같아야 함        |
| Return Type | 단독 차이 불가        | 호환 필요        |
| 결정 시점   | Compile Time          | Runtime          |
| 관련 개념   | Method Signature      | Polymorphism     |

---

### [실무]

사용 기준:

```text
입력 형태만 다름 → Overloading 검토
구현체별 동작 다름 → Overriding 검토
동작 의미가 다름 → 이름 분리 검토
부모 계약 재정의 → Overriding + @Override
```

주의:

- Overloading은 API 사용성을 해칠 수 있다.
- Overriding은 부모 계약을 깨면 안 된다.
- 둘 다 Method 이름과 의미가 명확해야 한다.
- 다형성 설계에서는 Overriding 품질이 중요하다.

---

### [FAQ]

Q. Overloading과 Overriding 차이는?
A. Overloading은 같은 이름에 다른 Parameter를 제공하는 것이고 Overriding은 부모 Method를 재정의하는 것이다.

Q. 다형성과 더 관련 깊은 것은?
A. Overriding이 다형성과 직접 관련 있다.

Q. Overloading이 많으면 왜 문제야?
A. 호출자가 어떤 Method가 호출되는지 이해하기 어려워질 수 있다.

---

# 8. Coupling and Cohesion Rules

## 8.1 Coupling Rules

### [개념]

Coupling은 Class나 Module 간 의존 정도를 의미한다.

낮은 Coupling은 변경 영향 범위를 줄이고 테스트를 쉽게 만든다.

---

### [핵심]

Coupling 핵심:

- Coupling
- Dependency
- Tight Coupling
- Loose Coupling
- Concrete Dependency
- Interface Dependency
- Constructor Injection
- Circular Dependency
- Change Impact
- Testability

높은 결합도 신호:

```text
구체 Class 직접 생성
static Method 과다 의존
여러 Layer 직접 접근
순환 의존
내부 Field 직접 접근
외부 구현 상세에 의존
테스트 대체 어려움
```

---

### [실무]

나쁜 예:

```java
public class UserService {
    private final SmtpMailSender mailSender = new SmtpMailSender();
}
```

좋은 예:

```java
public class UserService {
    private final MailSender mailSender;

    public UserService(MailSender mailSender) {
        this.mailSender = mailSender;
    }
}
```

낮은 Coupling 기준:

- Interface 또는 역할 타입에 의존
- 생성자 주입 사용
- 내부 구현 상세 노출 금지
- Layer 의존 방향 유지
- 순환 의존 제거
- 외부 시스템은 Client로 격리
- 테스트 대체 가능성 확보

주의:

- Coupling을 낮춘다고 모든 것을 Interface로 만들 필요는 없다.
- 지나친 추상화는 이해 비용을 높인다.
- Spring Bean 순환 참조는 설계 문제 신호일 수 있다.
- static Utility 의존은 테스트를 어렵게 만들 수 있다.

---

### [FAQ]

Q. Coupling은 뭐야?
A. Class나 Module이 서로 얼마나 강하게 의존하는지를 의미한다.

Q. 낮은 Coupling이 좋은 이유는?
A. 변경 영향이 줄고 테스트 대체가 쉬워지기 때문이다.

Q. 순환 의존은 왜 문제야?
A. 책임 경계가 흐려지고 초기화, 테스트, 유지보수 문제가 생길 수 있다.

---

## 8.2 Cohesion Rules

### [개념]

Cohesion은 하나의 Class나 Module 내부 요소들이 하나의 책임을 위해 얼마나 잘 모여 있는지를 의미한다.

높은 Cohesion은 Class 책임이 명확하다는 신호다.

---

### [핵심]

Cohesion 핵심:

- Cohesion
- Single Responsibility
- Related Field
- Related Method
- Class Purpose
- Change Reason
- Responsibility Focus
- Module Boundary

낮은 Cohesion 신호:

```text
서로 관련 없는 Field가 많음
Method 그룹이 여러 책임으로 나뉨
Class 이름이 모호함
변경 이유가 여러 개
일부 Method만 일부 Field 사용
Manager / Helper / Common 이름 사용
```

---

### [실무]

Cohesion 검토 Flow:

```text
Class 이름 확인
→ Field 그룹 확인
→ Method 그룹 확인
→ 변경 이유 확인
→ 관련 없는 책임 분리
→ Class 재설계
```

나쁜 예:

```text
UserManager
- createUser
- sendMail
- generateReport
- uploadFile
- calculateDiscount
```

분리 예:

```text
UserRegistrationService
MailClient
ReportGenerator
FileStorageClient
DiscountPolicy
```

주의:

- 높은 Cohesion은 Method 수가 적다는 뜻이 아니다.
- 같은 책임에 집중되어 있으면 Method가 많아도 가능하다.
- 낮은 Cohesion은 God Class로 이어질 수 있다.
- RAG 문서와 코드 모두 Cohesion이 높을수록 검색 품질이 좋다.

---

### [FAQ]

Q. Cohesion은 뭐야?
A. Class 내부 요소들이 하나의 책임을 위해 얼마나 잘 모여 있는지를 의미한다.

Q. 높은 Cohesion이 좋은 이유는?
A. Class 목적이 명확하고 변경 범위가 작아지기 때문이다.

Q. 낮은 Cohesion은 어떻게 개선해?
A. 관련 없는 Field와 Method를 책임 단위로 다른 Class로 분리한다.

---

# 9. OOP Anti Pattern Rules

## 9.1 Anemic Domain Model Rules

### [개념]

Anemic Domain Model은 Entity나 Domain Object가 상태만 가지고 행위와 비즈니스 규칙은 Service에 흩어진 구조다.

DTO에는 자연스러울 수 있지만 Entity가 Anemic하면 도메인 규칙 응집도가 낮아진다.

---

### [핵심]

Anemic Domain Model 징후:

- Entity에 Getter / Setter만 있음
- Service에서 Entity Field를 직접 계산
- 상태 변경 규칙이 Service에 흩어짐
- 동일 검증 로직이 여러 Service에 중복
- Entity Method가 거의 없음
- Domain Rule 위치가 불명확

---

### [실무]

나쁜 예:

```java
public void publishPost(Long postId) {
    Post post = postRepository.findById(postId)
        .orElseThrow(() -> new PostNotFoundException(postId));

    if (post.getStatus() != PostStatus.DRAFT) {
        throw new IllegalStateException("only draft can be published");
    }

    post.setStatus(PostStatus.PUBLISHED);
    post.setPublishedAt(LocalDateTime.now());
}
```

좋은 예:

```java
public void publishPost(Long postId) {
    Post post = postRepository.findById(postId)
        .orElseThrow(() -> new PostNotFoundException(postId));

    post.publish();
}
```

Entity Method:

```java
public void publish() {
    if (this.status != PostStatus.DRAFT) {
        throw new IllegalStateException("only draft can be published");
    }

    this.status = PostStatus.PUBLISHED;
    this.publishedAt = LocalDateTime.now();
}
```

주의:

- 모든 비즈니스 로직을 Entity에 넣는 것도 정답은 아니다.
- 여러 Entity가 협력하는 Use Case는 Service나 Domain Service가 필요할 수 있다.
- 단순 CRUD에서는 Anemic 구조가 허용될 수 있다.
- 중요한 것은 규칙 위치가 일관되고 중복되지 않는 것이다.

---

### [FAQ]

Q. Anemic Domain Model은 뭐야?
A. Entity가 상태만 가지고 비즈니스 행위와 규칙은 Service에 흩어진 구조다.

Q. Entity에 Method를 넣으면 좋은 이유는?
A. 상태 변경 규칙을 Entity 내부에 모아 일관성과 응집도를 높일 수 있기 때문이다.

Q. 모든 로직을 Entity에 넣어야 해?
A. 아니다. 여러 객체 협력이 필요한 흐름은 Service나 Domain Service가 담당할 수 있다.

---

## 9.2 God Object Rules

### [개념]

God Object는 하나의 객체가 너무 많은 책임과 상태, 행위를 가진 Anti Pattern이다.

God Object는 낮은 Cohesion과 높은 Coupling을 동시에 만든다.

---

### [핵심]

God Object 징후:

- Field가 너무 많음
- Method가 너무 많음
- 서로 관련 없는 기능 포함
- 이름이 Manager / Processor / Handler로 모호함
- 여러 외부 의존성 보유
- 테스트가 어려움
- 변경 이유가 여러 개
- private Method가 과도하게 많음

---

### [실무]

검토 Flow:

```text
Class 이름 확인
→ 책임 목록 작성
→ Field 그룹 분리
→ Method 그룹 분리
→ 외부 의존성 분리
→ 변경 이유별 Class 분리
```

분리 후보:

```text
Validation → Validator
Mapping → Mapper
External API → Client
Policy → Strategy
Creation → Factory
Complex Rule → Domain Service
Use Case → Application Service
```

주의:

- 단순히 줄 수가 많다고 God Object는 아니다.
- 하나의 응집된 책임이라면 큰 Class도 가능하다.
- 그러나 변경 이유가 여러 개면 분리해야 한다.
- God Object는 RAG Retrieval Chunk 품질도 떨어뜨린다.

---

### [FAQ]

Q. God Object는 뭐야?
A. 하나의 객체가 너무 많은 책임을 가져 변경과 테스트가 어려운 Anti Pattern이다.

Q. God Object는 어떻게 나눠?
A. 검증, 변환, 외부 통신, 정책, 생성, Use Case 같은 책임 단위로 나눈다.

Q. Class가 길면 무조건 God Object야?
A. 아니다. 책임이 응집되어 있으면 가능하지만 변경 이유가 여러 개면 문제다.

---

## 9.3 Primitive Obsession Rules

### [개념]

Primitive Obsession은 도메인 의미가 있는 값을 String, int, Long 같은 primitive 또는 단순 타입으로만 처리하는 Anti Pattern이다.

의미 있는 값은 Value Object로 분리하면 검증과 의미 표현이 좋아질 수 있다.

---

### [핵심]

Primitive Obsession 징후:

- email을 단순 String으로 곳곳에서 검증
- price를 int로 처리
- period를 startDate / endDate 개별 값으로 전달
- status를 String으로 처리
- type code를 문자열로 비교
- 여러 Method에 같은 원시 값 묶음 반복

---

### [실무]

나쁜 예:

```java
public void register(String email) {
    if (email == null || !email.contains("@")) {
        throw new IllegalArgumentException("invalid email");
    }
}
```

Value Object 예:

```java
public record Email(String value) {
    public Email {
        if (value == null || !value.contains("@")) {
            throw new IllegalArgumentException("invalid email");
        }
    }
}
```

Period 예:

```java
public record Period(LocalDate startDate, LocalDate endDate) {
    public Period {
        if (startDate.isAfter(endDate)) {
            throw new IllegalArgumentException("startDate must be before endDate");
        }
    }
}
```

실무 기준:

- 검증이 반복되는 값은 Value Object 검토.
- 여러 값이 항상 함께 움직이면 Value Object 검토.
- 상태 코드 문자열은 Enum 검토.
- 금액은 BigDecimal 또는 Money Value Object 검토.
- 단순 CRUD에서는 과한 Value Object 분리를 피한다.

주의:

- Value Object가 많아지면 구조가 복잡해질 수 있다.
- JPA Embeddable 적용 여부는 별도 검토.
- DTO 경계에서는 primitive / String이 더 단순할 수 있다.
- 도메인 내부에서 의미를 강화할 때 효과적이다.

---

### [FAQ]

Q. Primitive Obsession은 뭐야?
A. 도메인 의미가 있는 값을 단순 String, int, Long 등으로만 처리해 의미와 검증이 흩어지는 문제다.

Q. Value Object는 언제 만들어?
A. 검증이 반복되거나 여러 값이 항상 함께 움직이거나 도메인 의미가 강한 값일 때 검토한다.

Q. 모든 String을 Value Object로 바꿔야 해?
A. 아니다. 도메인 의미와 검증 필요성이 있을 때만 적용한다.

---

# 10. OOP Review Checklist

## 10.1 OOP Code Review Checklist

### [개념]

OOP Code Review Checklist는 Backend Agent / Review Agent가 Java 객체지향 설계 품질을 검토하기 위한 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] Class가 명확한 책임을 가지는가?
- [ ] Object State와 Behavior가 자연스럽게 함께 있는가?
- [ ] Field가 private 중심으로 보호되는가?
- [ ] Setter를 과도하게 사용하지 않는가?
- [ ] 상태 변경이 의미 있는 Method로 표현되는가?
- [ ] 객체 Invariant가 Constructor와 Method에서 보호되는가?
- [ ] 내부 Collection이 외부에서 직접 수정되지 않는가?
- [ ] 상속이 명확한 is-a 관계에 기반하는가?
- [ ] 코드 재사용만을 위한 상속을 사용하지 않는가?
- [ ] 깊은 상속 계층이 없는가?
- [ ] protected Field를 남용하지 않는가?
- [ ] 상속보다 Composition을 먼저 검토했는가?
- [ ] 객체 위임 책임이 명확한가?
- [ ] Polymorphism 적용 대상이 명확한가?
- [ ] if-else / switch 분기가 정책별로 과도하게 늘어나지 않는가?
- [ ] Strategy Pattern이 필요한 정책 변화가 있는가?
- [ ] 추상화가 구현 상세를 숨기고 역할을 표현하는가?
- [ ] 모든 Class에 무분별하게 Interface를 만들지 않았는가?
- [ ] Dependency Inversion이 필요한 외부 구현체를 추상화했는가?
- [ ] Overriding이 부모 계약을 깨지 않는가?
- [ ] Overloading이 호출 혼동을 만들지 않는가?
- [ ] Coupling이 과도하게 높지 않은가?
- [ ] Cohesion이 낮은 Class가 없는가?
- [ ] Anemic Domain Model 징후가 없는가?
- [ ] God Object 징후가 없는가?
- [ ] Primitive Obsession 징후가 없는가?
```

---

### [실무]

Review Flow:

```text
Responsibility Review
→ Encapsulation Review
→ Invariant Review
→ Inheritance Review
→ Composition Review
→ Polymorphism Review
→ Abstraction Review
→ Coupling / Cohesion Review
→ Anti Pattern Review
→ Refactoring Candidate 도출
```

리팩터링 후보:

```text
Setter 남용 → Meaningful Method
Service 규칙 과다 → Entity Method / Domain Service
if-else 정책 분기 → Strategy Pattern
상속 재사용 → Composition
String 상태값 → Enum
반복 검증 원시값 → Value Object
God Object → 책임별 Class 분리
```

---

### [FAQ]

Q. OOP 코드 리뷰에서 가장 먼저 볼 것은?
A. Class 책임과 상태 변경 규칙이 적절한 위치에 있는지 먼저 확인한다.

Q. Encapsulation 검수에서 중요한 것은?
A. Field 보호, Setter 남용 여부, 의미 있는 상태 변경 Method, Invariant 보호 여부다.

Q. Polymorphism은 언제 리뷰 포인트가 돼?
A. if-else나 switch 분기가 정책별로 계속 늘어나는 경우 리뷰 포인트가 된다.

---

# 11. Backend Integration

## 11.1 OOP to Spring Boot

### [개념]

OOP Core는 Spring Boot Backend 코드의 구조적 품질을 결정한다.

Controller, Service, Entity, DTO, Repository, Policy, Client는 객체 책임과 협력으로 설계되어야 한다.

---

### [핵심]

Spring Boot OOP 연결:

```text
Controller
→ HTTP 책임

Service
→ Application Flow 책임

Entity
→ Domain State / Behavior 책임

Repository
→ Persistence 책임

DTO
→ Data Transfer 책임

Policy / Strategy
→ 변하는 규칙 책임

Client
→ External System 책임

Validator
→ Validation 책임

Mapper
→ Conversion 책임
```

---

### [실무]

좋은 Spring Boot OOP 흐름:

```java
@Transactional
public void publishPost(Long postId) {
    Post post = postRepository.findById(postId)
        .orElseThrow(() -> new PostNotFoundException(postId));

    post.publish();
}
```

정책 분리 예:

```java
public class OrderService {
    private final DiscountPolicy discountPolicy;

    public OrderService(DiscountPolicy discountPolicy) {
        this.discountPolicy = discountPolicy;
    }

    public OrderResult order(OrderCommand command) {
        int discountAmount = discountPolicy.discount(command.price());
        return OrderResult.of(discountAmount);
    }
}
```

검토 기준:

- Controller가 비즈니스 규칙을 가지지 않는가?
- Service가 모든 Entity Field를 직접 조작하지 않는가?
- Entity에 의미 있는 상태 변경 Method가 있는가?
- 외부 시스템은 Client로 격리되었는가?
- 변하는 정책은 Policy / Strategy로 분리되었는가?
- DTO와 Entity가 역할을 혼동하지 않는가?
- Repository가 비즈니스 결정을 하지 않는가?

주의:

- 모든 프로젝트에 Rich Domain Model이 필요한 것은 아니다.
- 단순 CRUD는 Service 중심 구조가 더 단순할 수 있다.
- 그러나 상태 전이와 규칙이 많으면 Entity Method와 Policy 분리가 유리하다.
- OOP 설계는 테스트 코드 작성 난이도와 직접 연결된다.

---

### [FAQ]

Q. Spring Boot에서 OOP는 어디에 적용돼?
A. Controller, Service, Entity, DTO, Repository, Policy, Client 등 모든 Class 책임 설계에 적용된다.

Q. Entity에 비즈니스 Method를 넣는 게 좋아?
A. Entity 자신의 상태 변경 규칙이라면 Method로 표현하는 것이 좋다.

Q. 정책이 자주 바뀌면 어떻게 설계해?
A. Interface 기반 Policy나 Strategy Pattern으로 분리하는 것을 검토한다.

---

# Retrieval Queries

### [FAQ]

Q. OOP는 뭐야?
A. 프로그램을 객체의 책임, 상태, 행위, 협력으로 구성하는 설계 방식이다.

Q. Java에서 OOP가 왜 중요해?
A. Spring Boot, JPA Entity, Service, DTO, 테스트 코드가 모두 Class와 객체 협력으로 구성되기 때문이다.

Q. OOP 4대 특성은 뭐야?
A. Encapsulation, Inheritance, Polymorphism, Abstraction이다.

Q. 객체 책임은 어떻게 찾는 게 좋아?
A. 요구사항에서 상태와 행위가 자연스럽게 모이는 단위를 찾고 변경 이유를 기준으로 판단한다.

Q. Responsibility Driven Design은 뭐야?
A. 객체가 무엇을 알고 무엇을 수행해야 하는지를 책임 중심으로 설계하는 방식이다.

Q. Encapsulation은 뭐야?
A. 객체 내부 상태를 숨기고 정해진 Method를 통해 상태 변경 규칙을 보호하는 원칙이다.

Q. Encapsulation은 Field를 private으로 만드는 것만 의미해?
A. 아니다. 상태 변경 규칙을 객체 내부 Method에 모아 일관성을 지키는 것이 핵심이다.

Q. Setter를 많이 써도 돼?
A. 권장하지 않는다. 비즈니스 상태 변경은 의미 있는 Method로 표현하는 것이 좋다.

Q. Meaningful Method는 뭐야?
A. setStatus 같은 단순 Setter 대신 publish, activate, addPoint처럼 도메인 의미를 표현하는 Method다.

Q. Entity에 publish 같은 Method를 넣어도 돼?
A. Entity 자신의 상태 전이 규칙이라면 Entity Method로 표현하는 것이 좋다.

Q. Invariant는 뭐야?
A. 객체가 항상 만족해야 하는 상태 규칙이다.

Q. Invariant는 어디서 검증해?
A. 생성 시점은 Constructor나 Factory Method, 상태 변경 시점은 Domain Method에서 검증하는 것이 좋다.

Q. 내부 Collection을 그대로 반환하면 왜 위험해?
A. 외부에서 Collection을 직접 수정해 객체 상태 규칙을 우회할 수 있기 때문이다.

Q. Collection Setter는 써도 돼?
A. 지양한다. add/remove 같은 의미 있는 Method로 변경을 제어하는 것이 좋다.

Q. Inheritance는 뭐야?
A. 부모 Class의 Field와 Method를 자식 Class가 물려받는 객체지향 기능이다.

Q. 상속은 언제 써?
A. 명확한 is-a 관계와 다형성이 필요할 때 사용한다.

Q. is-a 관계는 어떻게 확인해?
A. “A는 B의 한 종류다”라고 자연스럽게 말할 수 있고 부모 타입으로 대체 가능해야 한다.

Q. 코드 재사용을 위해 상속해도 돼?
A. 코드 재사용만 목적이라면 상속보다 Composition을 우선 검토하는 것이 좋다.

Q. 깊은 상속 구조는 왜 문제야?
A. 동작을 이해하려면 여러 부모 Class를 추적해야 하고 부모 변경 영향이 커지기 때문이다.

Q. Composition은 뭐야?
A. 객체가 다른 객체를 포함하고 필요한 작업을 위임하는 설계 방식이다.

Q. 상속보다 조합을 우선하라는 말은 뭐야?
A. 기능 재사용만 목적이라면 상속보다 객체를 포함하고 위임하는 방식이 더 유연하다는 뜻이다.

Q. Delegation은 뭐야?
A. 객체가 자신이 직접 처리하지 않아도 되는 작업을 적절한 협력 객체에게 맡기는 방식이다.

Q. Inheritance와 Composition 차이는?
A. Inheritance는 is-a 관계이고 Composition은 has-a 관계다.

Q. 기능 재사용만 필요하면 뭘 써?
A. 상속보다 Composition을 우선 검토한다.

Q. Polymorphism은 뭐야?
A. 같은 Interface나 부모 타입으로 여러 구현 객체를 다룰 수 있는 객체지향 특성이다.

Q. Polymorphism은 왜 써?
A. 구현체가 바뀌어도 사용하는 쪽 코드를 크게 바꾸지 않고 확장하기 위해 사용한다.

Q. if-else가 많으면 무조건 다형성으로 바꿔?
A. 아니다. 정책이 계속 늘어나거나 변경 가능성이 크면 다형성을 검토한다.

Q. Replace Conditional with Polymorphism은 뭐야?
A. 조건 분기를 구현체별 다형성 구조로 분리하는 리팩터링 방식이다.

Q. Strategy Pattern은 언제 써?
A. 실행 정책이나 알고리즘이 여러 개이고 교체 가능성이 있을 때 사용한다.

Q. Strategy Pattern과 Polymorphism 관계는?
A. Strategy Pattern은 Polymorphism을 정책 교체 구조로 적용한 대표 패턴이다.

Q. Abstraction은 뭐야?
A. 구현 세부사항을 숨기고 필요한 역할과 계약만 드러내는 객체지향 원칙이다.

Q. 모든 Service에 Interface를 만들어야 해?
A. 아니다. 구현체 교체 가능성이나 테스트 대체 필요성이 낮으면 과한 추상화가 될 수 있다.

Q. Dependency Inversion은 뭐야?
A. 상위 정책 코드가 구체 구현체가 아니라 추상화에 의존하도록 만드는 원칙이다.

Q. 구체 Class를 직접 new 하면 왜 안 좋아?
A. 구현체 교체와 테스트 대체가 어려워지고 결합도가 높아질 수 있다.

Q. Overloading은 뭐야?
A. 같은 이름의 Method를 Parameter 구성을 다르게 해서 여러 개 정의하는 것이다.

Q. Overriding은 뭐야?
A. 부모나 Interface의 Method를 자식 Class에서 재정의하는 것이다.

Q. Overloading과 Overriding 차이는?
A. Overloading은 같은 이름에 다른 Parameter를 제공하는 것이고 Overriding은 부모 Method를 재정의하는 것이다.

Q. @Override는 꼭 붙여야 해?
A. 권장한다. 컴파일러가 올바른 재정의인지 확인해준다.

Q. Coupling은 뭐야?
A. Class나 Module이 서로 얼마나 강하게 의존하는지를 의미한다.

Q. 낮은 Coupling이 좋은 이유는?
A. 변경 영향이 줄고 테스트 대체가 쉬워지기 때문이다.

Q. Cohesion은 뭐야?
A. Class 내부 요소들이 하나의 책임을 위해 얼마나 잘 모여 있는지를 의미한다.

Q. 높은 Cohesion이 좋은 이유는?
A. Class 목적이 명확하고 변경 범위가 작아지기 때문이다.

Q. Anemic Domain Model은 뭐야?
A. Entity가 상태만 가지고 비즈니스 행위와 규칙은 Service에 흩어진 구조다.

Q. God Object는 뭐야?
A. 하나의 객체가 너무 많은 책임을 가져 변경과 테스트가 어려운 Anti Pattern이다.

Q. Primitive Obsession은 뭐야?
A. 도메인 의미가 있는 값을 단순 String, int, Long 등으로만 처리해 의미와 검증이 흩어지는 문제다.

Q. Value Object는 언제 만들어?
A. 검증이 반복되거나 여러 값이 항상 함께 움직이거나 도메인 의미가 강한 값일 때 검토한다.

Q. OOP 코드 리뷰는 어떤 순서로 해?
A. Responsibility, Encapsulation, Invariant, Inheritance, Composition, Polymorphism, Abstraction, Coupling, Cohesion, Anti Pattern 순서로 검토한다.

Q. Java Part03 다음 문서는 뭐야?
A. Java Part04 — Interface, Abstract Class, Enum, Static, Final 문서로 이어지는 것이 좋다.
