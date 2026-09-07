# Java Part04 — Interface, Abstract Class, Enum, Static, Final

---

# 1. Interface Foundation

## 1.1 Interface Purpose

### [개념]

Interface는 Java에서 구현 Class가 따라야 할 역할과 계약을 정의하는 추상화 도구다.

Interface는 구현 세부사항보다 “무엇을 할 수 있는가”를 표현한다.

Backend Agent / Review Agent는 Interface를 사용해 역할 분리, 다형성, 테스트 대체, 외부 의존성 추상화를 판단한다.

```java
public interface PasswordEncoder {
    String encode(String rawPassword);
    boolean matches(String rawPassword, String encodedPassword);
}
```

---

### [핵심]

Interface 핵심:

- Interface
- Contract
- Role
- Abstraction
- Polymorphism
- Dependency Inversion
- Implementation Replacement
- Test Double
- Mock
- Strategy Pattern
- Spring Bean Injection

Interface 목적:

```text
역할 정의
구현체 교체
다형성 적용
외부 의존성 숨김
테스트 대체 가능
상위 코드와 구현 세부사항 분리
```

---

### [실무]

2026 백엔드 실무 기준에서 Interface는 무조건 만드는 것이 아니라 변경 가능성과 역할 추상화가 있을 때 사용한다.

Interface 적합 상황:

```text
구현체가 여러 개다.
구현체가 바뀔 수 있다.
테스트에서 Mock / Fake로 대체해야 한다.
외부 시스템 구현을 숨겨야 한다.
정책 / 전략을 교체해야 한다.
상위 Service가 구체 구현체에 의존하면 안 된다.
```

예:

```java
public interface MailSender {
    void send(String to, String subject, String body);
}
```

```java
public class SmtpMailSender implements MailSender {
    @Override
    public void send(String to, String subject, String body) {
        // SMTP send
    }
}
```

사용 코드:

```java
public class NotificationService {
    private final MailSender mailSender;

    public NotificationService(MailSender mailSender) {
        this.mailSender = mailSender;
    }
}
```

주의:

- 구현체가 하나뿐이고 교체 가능성이 낮으면 Interface가 과할 수 있다.
- 모든 Service마다 Interface를 만들 필요는 없다.
- Interface 이름은 구현 기술보다 역할 중심이어야 한다.
- Interface에 구현 상세나 특정 라이브러리 의존을 드러내지 않는다.
- Interface가 너무 많으면 구조 탐색 비용이 증가한다.

---

### [FAQ]

Q. Interface는 언제 만들어?
A. 역할 추상화, 구현체 교체, 테스트 대체, 다형성, 외부 의존성 분리가 필요할 때 만든다.

Q. Service마다 Interface를 꼭 만들어야 해?
A. 필수는 아니다. 구현체가 하나뿐이고 교체 가능성이 낮으면 과한 추상화가 될 수 있다.

Q. Interface 이름은 어떻게 짓는 게 좋아?
A. 구현 기술보다 역할과 계약이 드러나도록 짓는 것이 좋다.

---

## 1.2 Interface Contract Rules

### [개념]

Interface Contract는 구현체가 반드시 지켜야 하는 Method 의미와 입력 / 출력 규칙이다.

Interface는 Method Signature만이 아니라 호출자가 기대하는 동작의 약속이다.

---

### [핵심]

Interface Contract 핵심:

- Method Signature
- Contract
- Precondition
- Postcondition
- Return Type
- Exception Rule
- Null Policy
- Implementation Consistency
- Liskov Substitution

계약 구성:

```text
입력 Parameter 의미
반환값 의미
null 허용 여부
예외 발생 조건
Side Effect 여부
구현체별 공통 보장 조건
```

---

### [실무]

Interface Contract 예:

```java
public interface DiscountPolicy {
    int discount(int price);
}
```

계약:

```text
price는 0 이상이어야 한다.
반환값은 0 이상이어야 한다.
반환값은 price보다 클 수 없다.
구현체는 price를 변경하지 않는다.
지원하지 않는 값은 명확한 예외를 던진다.
```

좋은 구현:

```java
public class FixedDiscountPolicy implements DiscountPolicy {
    @Override
    public int discount(int price) {
        if (price < 0) {
            throw new IllegalArgumentException("price must not be negative");
        }

        return Math.min(1000, price);
    }
}
```

주의:

- 구현체마다 null 처리 방식이 다르면 호출자가 혼란스럽다.
- 구현체마다 예외 정책이 다르면 다형성이 약해진다.
- Interface 계약을 깨는 구현체는 Review 대상이다.
- Interface Method 이름은 계약을 명확히 표현해야 한다.

---

### [FAQ]

Q. Interface는 Method 선언만 있으면 충분해?
A. 아니다. 입력, 출력, 예외, null 정책 같은 계약 의미가 일관되어야 한다.

Q. 구현체마다 다르게 동작해도 돼?
A. 세부 구현은 달라도 Interface 계약은 지켜야 한다.

Q. Interface 계약이 깨지면 뭐가 문제야?
A. 호출자가 Interface 타입만 보고 안전하게 사용할 수 없어 다형성이 약해진다.

---

## 1.3 Interface Segregation Rules

### [개념]

Interface Segregation은 클라이언트가 사용하지 않는 Method에 의존하지 않도록 Interface를 작고 명확한 역할 단위로 나누는 원칙이다.

큰 Interface는 구현체에 불필요한 Method 구현을 강요할 수 있다.

---

### [핵심]

Interface Segregation 핵심:

- Interface Segregation
- Small Interface
- Role Interface
- Client Specific Interface
- Fat Interface
- Unused Method
- UnsupportedOperationException
- Cohesion

나쁜 신호:

```text
Interface Method가 너무 많다.
구현체가 일부 Method를 빈 구현한다.
구현체가 UnsupportedOperationException을 던진다.
클라이언트마다 사용하는 Method 묶음이 다르다.
Interface 이름이 Manager / Handler처럼 모호하다.
```

---

### [실무]

나쁜 예:

```java
public interface UserManager {
    void createUser();
    void deleteUser();
    void sendEmail();
    void uploadProfileImage();
    void generateReport();
}
```

개선 예:

```java
public interface UserCreator {
    void createUser();
}
```

```java
public interface MailSender {
    void sendEmail();
}
```

```java
public interface ReportGenerator {
    void generateReport();
}
```

실무 기준:

- Interface는 역할 단위로 작게 유지한다.
- 구현체가 실제로 수행 가능한 Method만 포함한다.
- 클라이언트 사용 패턴을 기준으로 분리한다.
- Method가 많아지면 책임 분리 검토.
- Interface가 쪼개져도 이름이 명확해야 한다.

주의:

- 너무 작은 Interface를 과도하게 만들면 구조가 복잡해진다.
- 실제 클라이언트 사용 기준 없이 기계적으로 분리하지 않는다.
- 하나의 역할로 응집된 Method 묶음은 같은 Interface에 있어도 된다.

---

### [FAQ]

Q. Interface Segregation은 뭐야?
A. 사용하지 않는 Method에 의존하지 않도록 Interface를 역할 단위로 작게 나누는 원칙이다.

Q. Interface에 Method가 많으면 무조건 나빠?
A. 무조건은 아니지만 서로 다른 책임이 섞였는지 확인해야 한다.

Q. UnsupportedOperationException을 던지는 구현체는 왜 문제야?
A. Interface가 구현체에 맞지 않는 Method를 강요하고 있다는 신호일 수 있다.

---

## 1.4 Functional Interface Rules

### [개념]

Functional Interface는 추상 Method가 하나만 있는 Interface다.

Lambda Expression과 Method Reference의 대상이 될 수 있다.

```java
@FunctionalInterface
public interface Validator<T> {
    boolean isValid(T value);
}
```

---

### [핵심]

Functional Interface 핵심:

- Functional Interface
- Single Abstract Method
- Lambda
- Method Reference
- Predicate
- Function
- Consumer
- Supplier
- Strategy
- Callback

대표 표준 Functional Interface:

```text
Predicate<T> → T를 받아 boolean 반환
Function<T, R> → T를 받아 R 반환
Consumer<T> → T를 받아 소비
Supplier<T> → 입력 없이 T 반환
Comparator<T> → 두 값을 비교
```

---

### [실무]

Lambda 사용 예:

```java
Predicate<User> activeUser = User::isActive;
```

Custom Functional Interface 예:

```java
@FunctionalInterface
public interface DiscountCalculator {
    int calculate(int price);
}
```

사용 예:

```java
DiscountCalculator calculator = price -> price / 10;
```

실무 기준:

- 단일 행위 전달에는 Functional Interface 사용 가능.
- 표준 Functional Interface로 충분하면 표준 타입 우선.
- 도메인 의미가 중요하면 Custom Functional Interface 검토.
- `@FunctionalInterface` Annotation 사용 권장.
- Lambda 내부 로직이 길면 Method로 분리.

주의:

- Functional Interface 이름은 행위를 명확히 표현해야 한다.
- 복잡한 도메인 정책은 일반 Interface + 구현 Class가 더 명확할 수 있다.
- Lambda에 Side Effect가 많으면 가독성과 테스트가 떨어진다.

---

### [FAQ]

Q. Functional Interface는 뭐야?
A. 추상 Method가 하나만 있는 Interface로 Lambda Expression의 대상이 될 수 있다.

Q. @FunctionalInterface는 꼭 붙여야 해?
A. 필수는 아니지만 컴파일러 검사를 받을 수 있어 권장한다.

Q. Predicate와 Function 차이는?
A. Predicate는 boolean을 반환하고 Function은 입력을 다른 결과 타입으로 변환한다.

---

# 2. Abstract Class Foundation

## 2.1 Abstract Class Purpose

### [개념]

Abstract Class는 직접 객체를 생성할 수 없고, 하위 Class가 공통 상태와 공통 동작을 물려받도록 설계된 Class다.

Abstract Class는 일부 구현을 제공하면서 하위 Class에 구체 구현을 위임할 수 있다.

```java
public abstract class NotificationSender {
    public void validateMessage(String message) {
        if (message == null || message.isBlank()) {
            throw new IllegalArgumentException("message must not be blank");
        }
    }

    public abstract void send(String message);
}
```

---

### [핵심]

Abstract Class 핵심:

- Abstract Class
- abstract
- Abstract Method
- Concrete Method
- Shared State
- Shared Behavior
- Template Method
- Inheritance
- Partial Implementation
- Base Class

Abstract Class 적합 상황:

```text
공통 Field가 필요하다.
공통 구현 Method가 필요하다.
하위 Class가 일부 Method만 구현한다.
생성자 기반 공통 초기화가 필요하다.
Template Method Pattern을 사용한다.
```

---

### [실무]

Abstract Class 예:

```java
public abstract class FileStorage {
    protected final String basePath;

    protected FileStorage(String basePath) {
        this.basePath = Objects.requireNonNull(basePath, "basePath must not be null");
    }

    public abstract void upload(String filename, byte[] content);

    protected String resolvePath(String filename) {
        return basePath + "/" + filename;
    }
}
```

주의:

- Java는 Class 다중 상속을 지원하지 않는다.
- Abstract Class를 상속하면 다른 Class를 상속할 수 없다.
- 단순 역할 추상화는 Interface가 더 적합할 수 있다.
- 깊은 Abstract Class 계층은 이해와 변경을 어렵게 만든다.
- protected Field 남용은 캡슐화를 약화시킬 수 있다.

---

### [FAQ]

Q. Abstract Class는 언제 써?
A. 공통 상태와 공통 구현을 제공하면서 일부 동작을 하위 Class에 위임해야 할 때 사용한다.

Q. Abstract Class는 객체 생성이 가능해?
A. 직접 생성할 수 없다. 하위 Class를 통해 객체를 생성해야 한다.

Q. 역할만 정의하면 Abstract Class가 좋아?
A. 역할과 계약만 필요하면 Interface를 먼저 검토하는 것이 좋다.

---

## 2.2 Abstract Method Rules

### [개념]

Abstract Method는 Abstract Class 안에서 선언만 하고 구현은 하위 Class에 맡기는 Method다.

하위 Class는 Abstract Method를 반드시 구현해야 한다.

```java
public abstract void send(String message);
```

---

### [핵심]

Abstract Method 핵심:

- Abstract Method
- No Body
- Subclass Implementation
- Overriding
- Contract
- Template Method
- Polymorphism

규칙:

```text
abstract Method는 body가 없다.
abstract Method를 가진 Class는 abstract Class여야 한다.
하위 Concrete Class는 abstract Method를 구현해야 한다.
abstract Method도 계약을 가진다.
```

---

### [실무]

예:

```java
public abstract class PaymentProcessor {
    public final void process(PaymentCommand command) {
        validate(command);
        pay(command);
        record(command);
    }

    protected abstract void pay(PaymentCommand command);

    private void validate(PaymentCommand command) {
        if (command == null) {
            throw new IllegalArgumentException("command must not be null");
        }
    }

    private void record(PaymentCommand command) {
        // record payment history
    }
}
```

하위 Class:

```java
public class CardPaymentProcessor extends PaymentProcessor {
    @Override
    protected void pay(PaymentCommand command) {
        // card payment logic
    }
}
```

주의:

- Abstract Method가 많으면 Interface와 구현체 분리가 더 나을 수 있다.
- 하위 Class가 구현해야 할 책임이 명확해야 한다.
- protected abstract Method는 Template Method 구조에서 자주 사용된다.
- 하위 Class 구현이 부모 흐름을 깨지 않아야 한다.

---

### [FAQ]

Q. Abstract Method는 뭐야?
A. 선언만 있고 구현은 하위 Class가 담당하는 Method다.

Q. Abstract Method가 하나라도 있으면 Class도 abstract여야 해?
A. 그렇다. Abstract Method를 가진 Class는 abstract Class여야 한다.

Q. Abstract Method와 Interface Method는 비슷해?
A. 역할은 비슷하지만 Abstract Class는 공통 상태와 구현을 함께 가질 수 있다.

---

## 2.3 Template Method Rules

### [개념]

Template Method Pattern은 공통 처리 흐름은 부모 Class에서 정의하고, 일부 세부 단계는 하위 Class가 구현하도록 하는 상속 기반 패턴이다.

Abstract Class의 대표 사용 방식이다.

---

### [핵심]

Template Method 핵심:

- Template Method Pattern
- Fixed Process
- Hook Method
- Abstract Step
- Common Flow
- Subclass Customization
- final Method
- Inheritance

구조:

```text
Parent Abstract Class
→ Template Method defines flow
→ Common Step
→ Abstract Step
→ Hook Step
→ Subclass implements detail
```

---

### [실무]

예:

```java
public abstract class ReportGenerator {
    public final Report generate(ReportCommand command) {
        validate(command);
        List<Data> data = loadData(command);
        return createReport(data);
    }

    private void validate(ReportCommand command) {
        if (command == null) {
            throw new IllegalArgumentException("command must not be null");
        }
    }

    protected abstract List<Data> loadData(ReportCommand command);

    protected abstract Report createReport(List<Data> data);
}
```

구현체:

```java
public class SalesReportGenerator extends ReportGenerator {
    @Override
    protected List<Data> loadData(ReportCommand command) {
        return List.of();
    }

    @Override
    protected Report createReport(List<Data> data) {
        return new Report(data);
    }
}
```

실무 기준:

- 처리 순서가 고정되어 있고 일부 단계만 바뀌는 경우 적합.
- 공통 검증 / 공통 전처리 / 공통 후처리가 있을 때 적합.
- Template Method는 `final`로 고정 가능.
- 하위 Class는 세부 단계만 구현한다.

주의:

- 상속 기반이라 유연성이 낮을 수 있다.
- 단계가 많아지면 하위 Class 부담이 커진다.
- 조합 + Strategy가 더 적합할 수 있는지 검토한다.
- 부모 흐름이 변경되면 모든 하위 Class 영향 확인 필요.

---

### [FAQ]

Q. Template Method Pattern은 언제 써?
A. 처리 흐름은 고정되어 있고 일부 단계만 구현체마다 달라질 때 사용한다.

Q. Template Method를 final로 만드는 이유는?
A. 하위 Class가 전체 처리 흐름을 임의로 바꾸지 못하게 하기 위해서다.

Q. Template Method와 Strategy Pattern 차이는?
A. Template Method는 상속으로 흐름을 고정하고 Strategy는 조합으로 정책을 교체한다.

---

# 3. Interface vs Abstract Class

## 3.1 Interface and Abstract Class Comparison

### [개념]

Interface와 Abstract Class는 모두 추상화를 제공하지만 목적과 사용 기준이 다르다.

Interface는 역할과 계약 중심이고 Abstract Class는 공통 상태와 공통 구현 중심이다.

---

### [핵심]

비교:

| 구분        | Interface                 | Abstract Class                        |
| ----------- | ------------------------- | ------------------------------------- |
| 중심        | 역할 / 계약               | 공통 상태 + 공통 구현                 |
| 다중 적용   | 여러 Interface 구현 가능  | Class 다중 상속 불가                  |
| Field       | 상수 중심                 | Instance Field 가능                   |
| Constructor | 없음                      | 있음                                  |
| 구현 Method | default 가능              | 일반 Method 가능                      |
| 적합        | 역할 추상화, 다형성, 교체 | 공통 흐름, 공통 상태, Template Method |
| 주의        | 과도한 추상화             | 깊은 상속 구조                        |

---

### [실무]

선택 Flow:

```text
역할과 계약만 필요한가?
→ Interface 우선 검토

공통 상태와 공통 구현이 필요한가?
→ Abstract Class 검토

여러 구현체 교체가 필요한가?
→ Interface 검토

처리 흐름을 부모에서 고정해야 하는가?
→ Abstract Class + Template Method 검토

단순 코드 재사용만 목적인가?
→ Composition 우선 검토
```

Interface 적합:

```java
public interface PaymentProcessor {
    void pay(PaymentCommand command);
}
```

Abstract Class 적합:

```java
public abstract class AbstractPaymentProcessor {
    public final void process(PaymentCommand command) {
        validate(command);
        pay(command);
    }

    protected abstract void pay(PaymentCommand command);
}
```

주의:

- Interface와 Abstract Class를 동시에 쓰면 구조가 복잡해질 수 있다.
- 단순 구현체 하나에 Interface + Abstract Class를 모두 붙이는 것은 과설계 가능성.
- Framework 확장을 위해 Abstract Class를 요구하는 경우는 별도 판단.
- 역할 추상화와 구현 공유를 혼동하지 않는다.

---

### [FAQ]

Q. Interface와 Abstract Class 차이는?
A. Interface는 역할과 계약 중심이고 Abstract Class는 공통 상태와 구현을 함께 제공할 수 있다.

Q. 둘 중 무엇을 먼저 검토해?
A. 역할 추상화는 Interface를 먼저 검토하고 공통 상태와 구현 공유가 필요하면 Abstract Class를 검토한다.

Q. 단순 코드 재사용은 Abstract Class가 좋아?
A. 단순 재사용 목적이라면 상속보다 Composition을 우선 검토하는 것이 좋다.

---

## 3.2 Interface Overuse Rules

### [개념]

Interface Overuse는 실제 교체 가능성이나 역할 추상화 필요가 낮은데 모든 Class에 Interface를 기계적으로 만드는 Anti Pattern이다.

---

### [핵심]

Interface Overuse 징후:

- 구현체가 항상 하나뿐이다.
- 테스트에서도 Interface 대체를 쓰지 않는다.
- Interface와 구현 Class 이름만 `Service` / `ServiceImpl`로 반복된다.
- Interface에 구현 상세가 그대로 드러난다.
- 코드 이동만 늘고 역할 추상화가 없다.
- 구조 탐색 비용이 커진다.

---

### [실무]

과한 예:

```java
public interface UserService {
    UserResponse getUser(Long userId);
}
```

```java
public class UserServiceImpl implements UserService {
    @Override
    public UserResponse getUser(Long userId) {
        return null;
    }
}
```

검토 기준:

```text
구현체가 여러 개인가?
변경 가능성이 실제로 있는가?
테스트 대체가 필요한가?
외부 의존성을 숨기고 있는가?
도메인 정책을 분리하고 있는가?
Interface가 역할을 표현하는가?
```

Interface가 유용한 예:

```text
PasswordEncoder
MailSender
PaymentProcessor
FileStorage
DiscountPolicy
AuthenticationProvider
NotificationSender
```

주의:

- 구현체 하나라도 외부 의존성 경계라면 Interface가 유용할 수 있다.
- 구현체 하나라도 정책 확장이 확실하면 Interface가 가능하다.
- 단순 CRUD Service는 Interface 없이 시작해도 된다.
- 나중에 필요해질 때 추출하는 방식도 가능하다.

---

### [FAQ]

Q. ServiceImpl 구조는 나쁜가?
A. 무조건 나쁘지는 않지만 구현체가 하나뿐이고 역할 추상화가 없다면 불필요할 수 있다.

Q. Interface는 나중에 만들어도 돼?
A. 가능하다. 실제 교체 필요가 생겼을 때 추출해도 된다.

Q. 구현체가 하나라도 Interface가 필요한 경우는?
A. 외부 시스템 경계, 테스트 대체, 정책 확장 가능성이 명확한 경우다.

---

# 4. Enum Foundation

## 4.1 Enum Purpose

### [개념]

Enum은 정해진 상수 집합을 타입 안전하게 표현하는 Java 타입이다.

Enum은 문자열 상수보다 오타 위험이 낮고 컴파일 시점 검사가 가능하다.

```java
public enum PostStatus {
    DRAFT,
    PUBLISHED,
    DELETED
}
```

---

### [핵심]

Enum 핵심:

- Enum
- Constant
- Type Safety
- Fixed Option
- Status
- Role
- Category
- State
- Switch
- Enum Method
- Enum Field

Enum 적합 대상:

```text
상태
역할
카테고리
타입
권한
고정 옵션
처리 결과
정책 구분값
```

---

### [실무]

실무 사용 예:

```java
public enum UserStatus {
    ACTIVE,
    INACTIVE,
    DELETED
}
```

JPA Entity 예:

```java
@Enumerated(EnumType.STRING)
private UserStatus status;
```

권장:

- 문자열 상태값보다 Enum 사용.
- DB 저장 시 `EnumType.STRING` 우선 검토.
- 상태 전이 규칙이 있으면 Method로 표현 가능.
- 표시명은 Field로 분리 가능.
- 외부 API 코드값과 내부 Enum을 분리할 수 있음.

주의:

- Enum 이름 변경은 DB 데이터와 충돌할 수 있다.
- `EnumType.ORDINAL`은 순서 변경에 취약하다.
- 복잡한 권한 매트릭스는 Enum만으로 부족할 수 있다.
- 외부 시스템 코드값을 그대로 Enum 이름으로 강제하지 않는다.

---

### [FAQ]

Q. Enum은 왜 써?
A. 정해진 값 집합을 타입 안전하게 표현하고 문자열 오타를 줄이기 위해 사용한다.

Q. 문자열 상태값 대신 Enum을 쓰는 이유는?
A. 컴파일 시점 검사를 받을 수 있고 허용 값 범위가 명확해지기 때문이다.

Q. JPA에서 Enum은 어떻게 저장하는 게 좋아?
A. 보통 `EnumType.STRING`을 우선 검토한다.

---

## 4.2 Enum Field and Method Rules

### [개념]

Enum은 단순 상수 나열뿐 아니라 Field, Constructor, Method를 가질 수 있다.

Enum Field와 Method를 사용하면 고정 코드값, 표시명, 상태별 규칙을 Enum 내부에 모을 수 있다.

---

### [핵심]

Enum 확장 요소:

- Enum Field
- Enum Constructor
- Enum Method
- Display Name
- Code Value
- Behavior Enum
- State Rule
- Static Lookup

---

### [실무]

표시명 예:

```java
public enum UserRole {
    USER("일반 사용자"),
    ADMIN("관리자");

    private final String displayName;

    UserRole(String displayName) {
        this.displayName = displayName;
    }

    public String getDisplayName() {
        return displayName;
    }
}
```

코드값 예:

```java
public enum PaymentStatus {
    READY("R"),
    PAID("P"),
    CANCELED("C");

    private final String code;

    PaymentStatus(String code) {
        this.code = code;
    }

    public String code() {
        return code;
    }
}
```

상태 규칙 예:

```java
public enum PostStatus {
    DRAFT {
        @Override
        public boolean canPublish() {
            return true;
        }
    },
    PUBLISHED {
        @Override
        public boolean canPublish() {
            return false;
        }
    };

    public abstract boolean canPublish();
}
```

주의:

- Enum에 너무 많은 비즈니스 로직을 넣으면 복잡해진다.
- DB 저장 이름과 화면 표시명을 분리한다.
- 외부 코드값 변경 가능성을 고려한다.
- 다국어 표시명은 Enum Field보다 Message Source가 적합할 수 있다.

---

### [FAQ]

Q. Enum에 Field를 넣어도 돼?
A. 가능하다. 코드값, 표시명, 고정 속성을 표현할 수 있다.

Q. Enum에 Method를 넣어도 돼?
A. 가능하다. 상태별 고정 규칙이나 변환 로직을 표현할 수 있다.

Q. Enum에 로직을 많이 넣어도 돼?
A. 간단한 상태 규칙은 가능하지만 복잡한 정책은 별도 Policy나 Strategy를 검토한다.

---

## 4.3 Enum Lookup Rules

### [개념]

Enum Lookup은 문자열 코드나 외부 값으로부터 해당 Enum 상수를 찾는 처리다.

외부 API, DB 코드, Request Parameter를 Enum으로 변환할 때 자주 필요하다.

---

### [핵심]

Enum Lookup 핵심:

- Static Lookup
- from
- fromCode
- valueOf
- IllegalArgumentException
- Unknown Code
- External Code Mapping
- Case Sensitivity
- Null Handling

---

### [실무]

안전한 Lookup 예:

```java
public enum PaymentStatus {
    READY("R"),
    PAID("P"),
    CANCELED("C");

    private final String code;

    PaymentStatus(String code) {
        this.code = code;
    }

    public static PaymentStatus fromCode(String code) {
        return Arrays.stream(values())
            .filter(status -> status.code.equals(code))
            .findFirst()
            .orElseThrow(() -> new IllegalArgumentException("unsupported payment status code"));
    }
}
```

Map 기반 Lookup:

```java
public enum PaymentStatus {
    READY("R"),
    PAID("P"),
    CANCELED("C");

    private static final Map<String, PaymentStatus> CODE_MAP =
        Arrays.stream(values())
            .collect(Collectors.toMap(PaymentStatus::code, Function.identity()));

    private final String code;

    PaymentStatus(String code) {
        this.code = code;
    }

    public String code() {
        return code;
    }

    public static PaymentStatus fromCode(String code) {
        PaymentStatus status = CODE_MAP.get(code);

        if (status == null) {
            throw new IllegalArgumentException("unsupported payment status code");
        }

        return status;
    }
}
```

주의:

- `valueOf()`는 이름이 정확히 일치하지 않으면 예외 발생.
- 외부 코드와 Enum 이름을 직접 묶지 않는 것이 안전할 수 있다.
- null 입력 정책을 명확히 한다.
- 오류 메시지에 민감정보를 포함하지 않는다.
- 대량 호출이면 Map Lookup 검토.

---

### [FAQ]

Q. valueOf를 그대로 써도 돼?
A. 내부적으로 확실한 Enum 이름이면 가능하지만 외부 입력에는 fromCode 같은 안전한 변환 Method가 좋다.

Q. 외부 API 코드값은 Enum 이름과 같게 해야 해?
A. 꼭 그럴 필요 없다. code Field로 분리하는 것이 변경에 더 안전할 수 있다.

Q. Enum 변환 실패는 어떻게 처리해?
A. 명확한 예외를 던지고 GlobalExceptionHandler에서 응답으로 변환하는 것이 좋다.

---

## 4.4 Enum Anti Pattern Rules

### [개념]

Enum Anti Pattern은 Enum을 잘못 사용해 DB 호환성, 확장성, 책임 분리 문제를 만드는 패턴이다.

---

### [핵심]

Enum Anti Pattern:

- EnumType.ORDINAL 남용
- Enum 이름 변경 고려 없음
- 문자열 코드와 Enum 혼용
- Enum에 과도한 비즈니스 로직 집중
- 복잡한 권한 규칙을 Enum만으로 처리
- 외부 API 코드와 내부 이름 강결합
- null Enum 상태 방치
- default case로 오류 숨김

---

### [실무]

위험 예:

```java
@Enumerated(EnumType.ORDINAL)
private UserStatus status;
```

권장:

```java
@Enumerated(EnumType.STRING)
private UserStatus status;
```

문자열 혼용 위험:

```java
if ("ACTIVE".equals(user.getStatus())) {
}
```

권장:

```java
if (user.getStatus() == UserStatus.ACTIVE) {
}
```

실무 기준:

- DB 저장 방식은 명시한다.
- 문자열 상태값과 Enum을 혼용하지 않는다.
- Enum 이름 변경 영향 검토.
- 복잡한 정책은 Strategy Pattern 검토.
- switch default에서 조용히 무시하지 않는다.

---

### [FAQ]

Q. EnumType.ORDINAL은 왜 위험해?
A. Enum 순서가 바뀌면 DB에 저장된 숫자의 의미가 바뀔 수 있기 때문이다.

Q. Enum과 String 상태값을 같이 써도 돼?
A. 혼용하면 오류와 변환 누락이 생기기 쉬워 한 기준으로 통일하는 것이 좋다.

Q. Enum에 복잡한 정책을 모두 넣어도 돼?
A. 간단한 고정 규칙은 가능하지만 복잡한 정책은 별도 Strategy나 Policy를 검토한다.

---

# 5. Static Rules

## 5.1 Static Purpose

### [개념]

static은 객체 인스턴스가 아니라 Class 자체에 속하는 Field나 Method를 정의할 때 사용하는 키워드다.

static Member는 객체를 생성하지 않고 Class 이름으로 접근할 수 있다.

```java
public static final int DEFAULT_PAGE_SIZE = 20;
```

---

### [핵심]

static 핵심:

- static
- Class Level
- Static Field
- Static Method
- Static Final Constant
- Utility Method
- Factory Method
- Shared State
- Global State
- Testability

static 적합 대상:

```text
상수
상태 없는 Utility Method
Static Factory Method
공통 변환 Method
순수 함수형 보조 Method
```

static 주의 대상:

```text
mutable static field
외부 의존성을 가진 static method
전역 상태
테스트 대체가 필요한 기능
동시성 접근 상태
```

---

### [실무]

상수 예:

```java
public static final int DEFAULT_PAGE_SIZE = 20;
```

Factory Method 예:

```java
public static User createActiveUser(String email) {
    return new User(email, UserStatus.ACTIVE);
}
```

Utility Method 예:

```java
public static boolean isBlank(String value) {
    return value == null || value.isBlank();
}
```

주의:

- static Method는 객체 상태에 접근하지 못한다.
- static mutable Field는 전역 상태 문제가 생긴다.
- static 의존은 테스트 대체가 어렵다.
- Spring Bean이 필요한 기능을 static으로 만들지 않는다.
- static Utility가 도메인 책임을 빼앗고 있는지 확인한다.

---

### [FAQ]

Q. static은 언제 써?
A. 상수, 상태 없는 Utility Method, Static Factory Method처럼 객체 상태에 의존하지 않는 경우 사용한다.

Q. static을 많이 쓰면 왜 안 좋아?
A. 객체 책임이 흐려지고 테스트 대체와 확장이 어려워질 수 있다.

Q. Spring Service Method를 static으로 만들어도 돼?
A. 권장하지 않는다. Spring Bean 의존성 주입과 테스트 대체가 어려워진다.

---

## 5.2 Static Field Rules

### [개념]

Static Field는 Class 단위로 공유되는 Field다.

모든 객체 인스턴스가 같은 Static Field를 공유한다.

---

### [핵심]

Static Field 핵심:

- Static Field
- Class Variable
- Shared Value
- Global State
- Constant
- Mutable Static
- Thread Safety
- Memory Lifetime

Static Field 종류:

```text
static final constant → 권장 가능
mutable static field → 주의
static cache → 동시성 / 만료 정책 필요
static config → Spring 설정과 충돌 주의
```

---

### [실무]

좋은 예:

```java
public class PagingConstants {
    public static final int DEFAULT_PAGE_SIZE = 20;
    public static final int MAX_PAGE_SIZE = 100;

    private PagingConstants() {
    }
}
```

위험 예:

```java
public class UserContext {
    public static Long currentUserId;
}
```

문제:

```text
요청 간 데이터 오염
동시성 문제
테스트 오염
예측 어려운 전역 상태
확장성 저하
```

실무 기준:

- 변경되지 않는 값은 `static final` 상수로 사용 가능.
- mutable static Field는 거의 금지에 가깝게 검토.
- 사용자별 / 요청별 상태를 static에 저장하지 않는다.
- Config 값은 Spring Configuration Properties 검토.
- Cache는 전용 Cache 도구나 Concurrent 구조 검토.

---

### [FAQ]

Q. static Field는 모든 객체가 공유해?
A. 그렇다. Class 단위로 하나만 존재한다.

Q. mutable static Field는 왜 위험해?
A. 전역으로 공유되어 동시성 문제, 테스트 오염, 요청 간 데이터 오염이 생길 수 있다.

Q. 상수는 static final로 둬도 돼?
A. 가능하다. 변경되지 않는 공통 상수는 static final이 적합하다.

---

## 5.3 Static Method Rules

### [개념]

Static Method는 객체 인스턴스 없이 Class 이름으로 호출하는 Method다.

Static Method는 객체 상태에 의존하지 않는 기능에 적합하다.

---

### [핵심]

Static Method 핵심:

- Static Method
- Utility Method
- Factory Method
- Stateless Method
- Pure Function
- Class Method
- Test Difficulty
- Dependency Injection Limitation

적합:

```text
순수 계산
문자열 단순 변환
날짜 포맷 단순 변환
Static Factory Method
상태 없는 검증 보조
```

부적합:

```text
DB 접근
외부 API 호출
Spring Bean 의존
사용자 상태 접근
Transaction 필요
테스트 Mock 필요
```

---

### [실무]

적합 예:

```java
public static boolean isPositive(int value) {
    return value > 0;
}
```

부적합 예:

```java
public static User findUser(Long userId) {
    return userRepository.findById(userId).orElseThrow();
}
```

Utility Class 예:

```java
public final class StringUtils {
    private StringUtils() {
    }

    public static boolean isBlank(String value) {
        return value == null || value.isBlank();
    }
}
```

주의:

- static Method가 많으면 객체 책임이 빠져나가고 있는지 확인한다.
- 도메인 규칙은 해당 Domain Object Method로 둘 수 있는지 검토한다.
- 외부 의존이 필요하면 Spring Bean Component로 분리한다.
- 테스트에서 Mock이 필요하면 static Method는 불리하다.

---

### [FAQ]

Q. Static Method는 언제 적합해?
A. 객체 상태나 외부 의존성 없이 입력만으로 결과를 만드는 경우 적합하다.

Q. Static Method로 Repository를 호출해도 돼?
A. 권장하지 않는다. Spring DI, Transaction, 테스트 대체가 어려워진다.

Q. Utility Class는 어떻게 만들어?
A. final Class + private Constructor + static Method 조합으로 만들 수 있다.

---

## 5.4 Static Factory Method Rules

### [개념]

Static Factory Method는 Constructor 대신 이름 있는 static Method로 객체 생성 의도를 표현하는 방식이다.

Part02의 Constructor 설계와 연결된다.

---

### [핵심]

Static Factory Method 핵심:

- Static Factory Method
- Named Constructor
- Object Creation
- Factory
- of
- from
- create
- valueOf
- private Constructor
- Validation

이름 패턴:

```text
of → 값 조합 생성
from → 다른 객체에서 변환
create → 새 도메인 객체 생성
valueOf → 값 변환
empty → 빈 객체 생성
```

---

### [실무]

예:

```java
public class Email {
    private final String value;

    private Email(String value) {
        if (value == null || !value.contains("@")) {
            throw new IllegalArgumentException("invalid email");
        }

        this.value = value;
    }

    public static Email of(String value) {
        return new Email(value);
    }
}
```

DTO 변환 예:

```java
public record UserResponse(Long userId, String email) {
    public static UserResponse from(User user) {
        return new UserResponse(user.getId(), user.getEmail());
    }
}
```

주의:

- Factory Method가 생성 이상의 흐름을 많이 포함하면 Factory Class 검토.
- 이름 없는 Constructor보다 생성 의도를 잘 표현해야 한다.
- JPA Entity에서는 private Constructor 사용에 제약이 있을 수 있다.
- Static Factory Method 내부에서 외부 API나 DB를 호출하지 않는다.

---

### [FAQ]

Q. Static Factory Method는 왜 써?
A. 객체 생성 의도와 규칙을 Method 이름으로 명확히 표현할 수 있기 때문이다.

Q. of와 from 차이는?
A. of는 값을 조합해 생성하고 from은 다른 객체나 타입에서 변환하는 의미가 강하다.

Q. Static Factory Method에서 DB 조회를 해도 돼?
A. 권장하지 않는다. 생성 규칙을 넘는 흐름은 Service나 Factory Bean으로 분리하는 것이 좋다.

---

# 6. Final Rules

## 6.1 Final Purpose

### [개념]

final은 Java에서 재할당, 재정의, 상속을 제한하는 키워드다.

final은 값 변경 가능성을 줄이고 코드 의도를 명확히 표현하는 데 사용된다.

---

### [핵심]

final 적용 위치:

- final variable
- final field
- final parameter
- final method
- final class
- static final constant

효과:

```text
변수 재할당 금지
Field 재할당 금지
Method Overriding 금지
Class 상속 금지
상수 표현
불변성 지원
```

주의:

```text
final은 참조 재할당을 막는다.
final은 참조 대상 객체 내부 변경까지 막지는 않는다.
final만으로 완전한 불변 객체가 되지 않는다.
```

---

### [실무]

final 변수 예:

```java
final Long userId = request.userId();
```

final Field 예:

```java
public class UserResponse {
    private final Long userId;
    private final String email;
}
```

상수 예:

```java
public static final int DEFAULT_PAGE_SIZE = 20;
```

주의:

- 변경되지 않는 의존성 Field는 final 권장.
- 생성자 주입과 final Field는 잘 어울린다.
- JPA Entity Field에는 final 사용이 제한될 수 있다.
- final을 무조건 강제하면 코드 작성 유연성이 떨어질 수 있다.
- final Collection은 참조 재할당만 막고 내부 add/remove는 가능하다.

---

### [FAQ]

Q. final 변수는 값을 바꿀 수 없어?
A. 재할당할 수 없다. 단, 참조형 객체 내부 상태 변경까지 막는 것은 아니다.

Q. final을 붙이면 완전 불변이야?
A. 아니다. 참조 재할당만 막고 내부 객체가 mutable이면 상태는 바뀔 수 있다.

Q. 의존성 Field에 final을 붙이는 이유는?
A. 생성 후 의존성이 바뀌지 않음을 명확히 하고 안정성을 높이기 위해서다.

---

## 6.2 Final Field and Immutability Rules

### [개념]

Final Field는 생성 후 재할당되지 않는 Field다.

Final Field는 불변 객체 설계의 중요한 요소지만, 단독으로 완전한 Immutability를 보장하지 않는다.

---

### [핵심]

Final Field 핵심:

- Final Field
- Immutability
- Constructor Initialization
- Required Field
- Reference Immutability
- Defensive Copy
- Mutable Object
- Record

불변 객체 조건:

```text
Field를 final로 선언
Setter 제거
생성자에서 모든 값 초기화
Mutable Object 방어적 복사
내부 Collection 직접 노출 금지
상태 변경 Method 제거
```

---

### [실무]

불변 객체 예:

```java
public final class Email {
    private final String value;

    public Email(String value) {
        if (value == null || !value.contains("@")) {
            throw new IllegalArgumentException("invalid email");
        }

        this.value = value;
    }

    public String value() {
        return value;
    }
}
```

Mutable Collection 주의:

```java
public class Team {
    private final List<String> members;

    public Team(List<String> members) {
        this.members = List.copyOf(members);
    }

    public List<String> members() {
        return members;
    }
}
```

주의:

- `final List<T>`는 List 참조 재할당만 막는다.
- 내부 List가 mutable이면 add/remove 가능성이 있다.
- 방어적 복사와 수정 불가 Collection을 함께 검토.
- JPA Entity는 완전 불변 설계와 충돌할 수 있다.
- DTO와 Value Object는 불변 설계가 적합한 경우가 많다.

---

### [FAQ]

Q. final Field만 있으면 불변 객체야?
A. 아니다. 참조 대상이 mutable이면 내부 상태는 바뀔 수 있다.

Q. 불변 객체를 만들려면 무엇이 필요해?
A. final Field, Setter 제거, 생성자 초기화, 방어적 복사, 내부 mutable 객체 노출 방지가 필요하다.

Q. JPA Entity도 final Field로 불변 객체처럼 만들 수 있어?
A. 일반적으로 제약이 많다. JPA Entity는 Framework 요구사항을 함께 고려해야 한다.

---

## 6.3 Final Method and Final Class Rules

### [개념]

Final Method는 하위 Class에서 Override할 수 없는 Method다.

Final Class는 상속할 수 없는 Class다.

---

### [핵심]

Final Method / Class 핵심:

- final method
- final class
- prevent overriding
- prevent inheritance
- fixed behavior
- security
- immutability
- template method

사용 상황:

```text
변경되면 안 되는 핵심 흐름
Template Method의 고정 흐름
불변 Value Object
상속을 의도하지 않은 Class
보안상 재정의 방지 필요
```

---

### [실무]

Final Method 예:

```java
public abstract class PaymentProcessor {
    public final void process(PaymentCommand command) {
        validate(command);
        pay(command);
    }

    protected abstract void pay(PaymentCommand command);
}
```

Final Class 예:

```java
public final class Email {
    private final String value;

    public Email(String value) {
        this.value = value;
    }
}
```

주의:

- final Class는 상속 확장을 막는다.
- Mock Framework나 Proxy 생성에 제약이 있을 수 있다.
- Spring AOP / Proxy 구조와 충돌 가능성을 확인한다.
- 무조건 final을 붙이는 정책은 팀 규칙과 Framework 제약을 함께 고려한다.

---

### [FAQ]

Q. final Method는 언제 써?
A. 하위 Class가 변경하면 안 되는 핵심 흐름을 고정할 때 사용한다.

Q. final Class는 언제 써?
A. 상속을 의도하지 않거나 불변 Value Object처럼 확장을 막고 싶을 때 사용한다.

Q. Spring에서 final Class를 조심해야 하는 이유는?
A. Proxy 기반 AOP나 Mock 생성에 제약이 생길 수 있기 때문이다.

---

# 7. Static vs Instance Rules

## 7.1 Static Method vs Instance Method

### [개념]

Static Method는 Class에 속하고 Instance Method는 객체에 속한다.

Static Method는 객체 상태를 사용하지 않고, Instance Method는 객체 상태와 책임을 표현할 수 있다.

---

### [핵심]

비교:

| 구분        | Static Method            | Instance Method           |
| ----------- | ------------------------ | ------------------------- |
| 소속        | Class                    | Object                    |
| 상태 접근   | Instance Field 접근 불가 | Instance Field 접근 가능  |
| 의존성 주입 | 어려움                   | 가능                      |
| 테스트 대체 | 어려움                   | 상대적으로 쉬움           |
| 적합        | 순수 보조 기능, Factory  | 도메인 행위, Service 기능 |
| 위험        | 전역 Utility 남용        | 객체 책임 과다            |

---

### [실무]

선택 기준:

```text
객체 상태를 사용하는가?
→ Instance Method

Spring Bean 의존성이 필요한가?
→ Instance Method

테스트 Mock이 필요한가?
→ Instance Method / Interface

입력만으로 결과가 정해지는가?
→ Static Method 가능

객체 생성 의도를 표현하는가?
→ Static Factory Method 가능
```

나쁜 예:

```java
public static void changeEmail(User user, String email) {
    user.setEmail(email);
}
```

좋은 예:

```java
public void changeEmail(String email) {
    validateEmail(email);
    this.email = email;
}
```

주의:

- 도메인 객체의 행위가 static Utility로 빠져나가면 캡슐화가 약해진다.
- 외부 의존성이 필요한 기능은 static으로 만들지 않는다.
- static Method가 많으면 객체 책임 분리를 재검토한다.
- 순수 함수는 static Method로도 충분할 수 있다.

---

### [FAQ]

Q. Static Method와 Instance Method 차이는?
A. Static Method는 Class에 속하고 Instance Method는 객체 상태와 책임에 속한다.

Q. 도메인 상태 변경을 Static Method로 해도 돼?
A. 권장하지 않는다. 객체 자신의 Instance Method로 표현하는 것이 좋다.

Q. 입력만으로 결과가 정해지는 함수는 static이어도 돼?
A. 가능하다. 상태 없는 순수 보조 기능이면 static Method가 적합할 수 있다.

---

## 7.2 Static Utility vs Spring Bean

### [개념]

Static Utility는 상태 없는 보조 기능을 Class Method로 제공하는 방식이다.

Spring Bean은 의존성 주입, 생명주기 관리, 테스트 대체, AOP 적용이 가능한 객체다.

---

### [핵심]

비교:

| 구분        | Static Utility | Spring Bean         |
| ----------- | -------------- | ------------------- |
| 상태        | 없어야 함      | 상태 없는 Bean 권장 |
| DI          | 불가           | 가능                |
| AOP         | 적용 어려움    | 적용 가능           |
| Mock        | 어려움         | 쉬움                |
| Transaction | 부적합         | 가능                |
| 외부 의존성 | 부적합         | 적합                |
| 사용 대상   | 순수 보조 함수 | 비즈니스 Component  |

---

### [실무]

Static Utility 적합:

```text
문자열 단순 검사
숫자 단순 계산
날짜 포맷 보조
상수 변환
객체 생성 보조
```

Spring Bean 적합:

```text
Repository 호출
외부 API 호출
메일 발송
파일 업로드
암호화 정책
결제 처리
Transaction 필요 로직
설정값 주입 필요 로직
```

나쁜 예:

```java
public class PaymentUtils {
    public static void approvePayment(PaymentCommand command) {
        // external API call
        // repository save
    }
}
```

좋은 예:

```java
@Service
public class PaymentService {
    private final PaymentClient paymentClient;
    private final PaymentRepository paymentRepository;

    public void approvePayment(PaymentCommand command) {
        paymentClient.approve(command);
        paymentRepository.save(command.toEntity());
    }
}
```

주의:

- Utility Class에 비즈니스 로직이 쌓이면 God Utility가 된다.
- static은 Spring 관리 대상이 아니므로 설정 주입이 어렵다.
- 테스트에서 static Mock은 가능하더라도 설계상 비용이 크다.
- 상태 없는 순수 함수만 Utility로 유지한다.

---

### [FAQ]

Q. Utility Class와 Spring Bean은 어떻게 구분해?
A. 외부 의존성, 설정 주입, Transaction, 테스트 대체가 필요하면 Spring Bean이 적합하다.

Q. static Utility에서 Repository를 써도 돼?
A. 권장하지 않는다. Repository 의존은 Spring Bean Service나 Component에서 처리하는 것이 좋다.

Q. Utility Class가 커지면 어떻게 해?
A. 책임 단위로 Validator, Mapper, Service, Client 등으로 분리한다.

---

# 8. Common Patterns

## 8.1 Constant Class Rules

### [개념]

Constant Class는 여러 곳에서 사용하는 상수를 모아두는 Class다.

상수는 `public static final`로 정의할 수 있다.

---

### [핵심]

Constant 핵심:

- Constant
- public static final
- Magic Number
- Magic String
- Naming Convention
- Utility Class
- Private Constructor
- Domain Constant

---

### [실무]

예:

```java
public final class SecurityConstants {
    public static final String AUTHORIZATION_HEADER = "Authorization";
    public static final String BEARER_PREFIX = "Bearer ";

    private SecurityConstants() {
    }
}
```

주의:

- 모든 상수를 하나의 CommonConstants에 몰지 않는다.
- 도메인별 상수 Class로 분리한다.
- 상태값 상수는 Enum이 더 적합할 수 있다.
- 상수 이름은 대문자 + underscore 사용.
- Constant Class는 private Constructor로 객체 생성을 막는다.

나쁜 예:

```java
public class CommonConstants {
    public static final String A = "A";
    public static final String ACTIVE = "ACTIVE";
    public static final int VALUE = 1;
}
```

좋은 분리:

```text
SecurityConstants
PagingConstants
ValidationConstants
CacheConstants
```

---

### [FAQ]

Q. Constant Class는 언제 써?
A. 여러 곳에서 반복되는 고정 문자열이나 숫자를 의미 있게 관리할 때 사용한다.

Q. 모든 상수를 CommonConstants에 넣어도 돼?
A. 권장하지 않는다. 도메인이나 목적별로 분리하는 것이 좋다.

Q. 상태값 상수는 String으로 관리해도 돼?
A. 정해진 값 집합이라면 Enum을 우선 검토한다.

---

## 8.2 Utility Class Rules

### [개념]

Utility Class는 객체 상태 없이 공통 보조 Method를 제공하는 Class다.

Utility Class는 보통 final Class, private Constructor, static Method로 구성한다.

---

### [핵심]

Utility Class 핵심:

- Utility Class
- Stateless
- Static Method
- Private Constructor
- Final Class
- Pure Function
- Helper
- Common Logic

Utility 적합 조건:

```text
객체 상태가 없다.
외부 의존성이 없다.
입력만으로 결과가 결정된다.
도메인 책임이 아니다.
테스트 대체가 필요 없다.
```

---

### [실무]

예:

```java
public final class MaskingUtils {
    private MaskingUtils() {
    }

    public static String maskEmail(String email) {
        if (email == null || !email.contains("@")) {
            return email;
        }

        String[] parts = email.split("@");
        return parts[0].charAt(0) + "***@" + parts[1];
    }
}
```

주의:

- Utility Class에 비즈니스 흐름을 넣지 않는다.
- Repository / Client / Service 의존성을 넣지 않는다.
- `CommonUtils`처럼 이름이 모호하면 책임이 커진다.
- Utility Method가 도메인 객체 Method로 들어가야 하는지 검토한다.
- static mutable state 금지.

---

### [FAQ]

Q. Utility Class는 어떻게 만들어?
A. final Class, private Constructor, static Method 조합으로 만든다.

Q. Utility Class에는 어떤 로직을 넣어?
A. 상태와 외부 의존성이 없는 순수 보조 로직만 넣는 것이 좋다.

Q. CommonUtils는 왜 조심해야 해?
A. 관련 없는 기능이 계속 쌓여 God Utility가 되기 쉽기 때문이다.

---

# 9. Anti Pattern Rules

## 9.1 Interface and Abstract Class Anti Patterns

### [개념]

Interface와 Abstract Class Anti Pattern은 추상화를 잘못 사용해 구조 복잡도와 결합도를 높이는 문제다.

---

### [핵심]

Anti Pattern:

- 의미 없는 Interface
- Service / ServiceImpl 기계적 분리
- Fat Interface
- UnsupportedOperationException 구현체
- Abstract Class 깊은 계층
- CommonBaseClass 남용
- protected Field 남용
- 역할보다 기술명 중심 Interface
- Interface에 구현 상세 노출

---

### [실무]

검토 Flow:

```text
Interface 필요성 확인
→ 구현체 수 확인
→ 교체 가능성 확인
→ 테스트 대체 필요 확인
→ Method 응집도 확인
→ Abstract Class 공통 상태 필요 확인
→ 상속 깊이 확인
→ Composition 대체 가능성 확인
```

개선 방향:

```text
의미 없는 Interface 제거
Fat Interface 분리
CommonBaseClass를 Component로 분리
protected Field를 private + protected Method로 변경
상속 재사용을 Composition으로 전환
ServiceImpl 이름 대신 역할 기반 이름 사용
```

주의:

- 추상화는 변경 가능성을 줄이는 것이 아니라 관리하기 위한 도구다.
- 추상화가 실제 변경 지점을 반영하지 않으면 비용만 증가한다.
- Abstract Class는 상속 결합을 만들기 때문에 신중해야 한다.

---

### [FAQ]

Q. Interface를 많이 만들면 좋은 설계야?
A. 아니다. 실제 역할 추상화와 변경 가능성을 반영해야 좋은 설계다.

Q. Abstract Class 상속이 깊으면 왜 문제야?
A. 동작 추적이 어렵고 부모 변경 영향이 커지기 때문이다.

Q. CommonBaseClass는 왜 위험해?
A. 여러 책임이 쌓여 God Class가 되기 쉽고 상속 결합을 만든다.

---

## 9.2 Enum Anti Patterns

### [개념]

Enum Anti Pattern은 Enum을 문자열 상수처럼만 쓰거나, 반대로 너무 많은 정책을 Enum에 몰아넣는 문제다.

---

### [핵심]

Enum Anti Pattern:

- EnumType.ORDINAL 사용
- String 상태값과 Enum 혼용
- Enum 이름 변경 영향 무시
- valueOf를 외부 입력에 직접 사용
- default case로 오류 숨김
- 복잡한 정책을 Enum에 과도하게 집중
- 다국어 표시명을 Enum에 고정
- 외부 코드값과 내부 Enum 이름 강결합

---

### [실무]

나쁜 예:

```java
UserStatus status = UserStatus.valueOf(request.status());
```

개선 예:

```java
UserStatus status = UserStatus.fromCode(request.statusCode());
```

나쁜 default 예:

```java
switch (status) {
    case ACTIVE -> activate();
    default -> {
    }
}
```

개선:

```java
switch (status) {
    case ACTIVE -> activate();
    case INACTIVE -> deactivate();
    case DELETED -> throw new IllegalStateException("deleted user cannot be activated");
}
```

주의:

- 알 수 없는 값은 조용히 무시하지 않는다.
- 외부 입력은 명확히 검증한다.
- 상태 전이가 복잡하면 State Pattern이나 Policy 검토.
- Enum은 고정 값 집합에 적합하다.

---

### [FAQ]

Q. 외부 입력에 valueOf를 쓰면 왜 위험해?
A. 입력이 Enum 이름과 정확히 일치하지 않으면 예외가 발생하고 오류 처리가 거칠 수 있다.

Q. switch default로 아무것도 안 하면 왜 문제야?
A. 새로운 Enum 값이나 오류 상태를 조용히 무시해 버그를 숨길 수 있다.

Q. 복잡한 상태 정책은 Enum으로 충분해?
A. 간단한 규칙은 가능하지만 복잡하면 State Pattern이나 Policy 분리를 검토한다.

---

## 9.3 Static and Final Anti Patterns

### [개념]

Static and Final Anti Pattern은 static과 final을 잘못 사용해 객체 책임, 테스트 가능성, Framework 호환성을 떨어뜨리는 문제다.

---

### [핵심]

Static Anti Pattern:

- mutable static state
- static service method
- static repository access
- God Utility
- global user context
- hidden dependency
- static config mutation

Final Anti Pattern:

- 무분별한 final Class
- Proxy / Mock 제약 무시
- mutable 객체를 final로 두고 불변 착각
- final 정책 강제 과다

---

### [실무]

위험 예:

```java
public class LoginUserHolder {
    public static Long userId;
}
```

문제:

```text
요청 간 사용자 정보 오염
Thread Safety 문제
테스트 오염
보안 위험
```

위험 예:

```java
public final class PaymentService {
    public void pay() {
    }
}
```

주의:

- Spring AOP / Proxy 대상 Class의 final 사용은 제약이 있을 수 있다.
- static 상태는 요청 기반 서버에서 특히 위험하다.
- static Utility에 비즈니스 로직이 쌓이면 분리한다.
- final은 재할당 제한이지 불변성 전체가 아니다.

---

### [FAQ]

Q. static 상태에 로그인 사용자 정보를 저장해도 돼?
A. 절대 권장하지 않는다. 요청 간 데이터 오염과 보안 문제가 생길 수 있다.

Q. final Class를 많이 쓰면 안전해?
A. 무조건은 아니다. 확장, Proxy, Mock 제약을 함께 고려해야 한다.

Q. final List는 불변 List야?
A. 아니다. 참조 재할당만 막고 내부 List가 mutable이면 요소 변경은 가능하다.

---

# 10. Review Checklist

## 10.1 Interface Abstract Enum Static Final Checklist

### [개념]

이 Checklist는 Backend Agent / Review Agent가 Interface, Abstract Class, Enum, Static, Final 사용 품질을 검토하기 위한 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] Interface가 실제 역할과 계약을 표현하는가?
- [ ] Interface 생성 이유가 구현체 교체, 테스트 대체, 외부 의존성 분리 중 하나인가?
- [ ] 모든 Service에 기계적으로 Interface를 만들지 않았는가?
- [ ] Interface Method 계약이 입력, 출력, 예외, null 정책을 명확히 하는가?
- [ ] Fat Interface가 아닌가?
- [ ] 구현체가 UnsupportedOperationException을 던지지 않는가?
- [ ] Functional Interface는 단일 행위를 명확히 표현하는가?
- [ ] Abstract Class가 공통 상태나 공통 구현을 실제로 필요로 하는가?
- [ ] Abstract Class 상속 계층이 깊지 않은가?
- [ ] protected Field를 남용하지 않는가?
- [ ] Template Method 흐름이 명확한가?
- [ ] Interface와 Abstract Class 선택이 적절한가?
- [ ] Enum이 고정 값 집합을 타입 안전하게 표현하는가?
- [ ] JPA Enum 저장 시 EnumType.STRING을 우선 검토했는가?
- [ ] Enum 이름 변경과 DB 데이터 영향이 검토되었는가?
- [ ] 외부 코드값은 fromCode 같은 안전한 변환을 사용하는가?
- [ ] valueOf를 외부 입력에 직접 사용하지 않는가?
- [ ] Enum에 복잡한 정책을 과도하게 넣지 않았는가?
- [ ] static은 상수, 순수 Utility, Factory Method에 제한되어 있는가?
- [ ] mutable static Field가 없는가?
- [ ] static Method가 Repository, Client, Service 의존을 직접 다루지 않는가?
- [ ] Utility Class가 God Utility가 되지 않았는가?
- [ ] final Field가 불변성을 과장하지 않는가?
- [ ] final Class가 Spring Proxy / Mock 제약을 만들지 않는가?
- [ ] Constant Class가 도메인별로 분리되어 있는가?
```

---

### [실무]

Review Flow:

```text
Interface 필요성 검토
→ Interface 계약 검토
→ Abstract Class 필요성 검토
→ Interface vs Abstract Class 선택 검토
→ Enum 타입 안전성 검토
→ Enum DB 저장 정책 검토
→ Static 사용 범위 검토
→ Final 사용 의도 검토
→ Anti Pattern 확인
→ Refactoring Candidate 도출
```

리팩터링 후보:

```text
의미 없는 Interface → 제거 또는 나중에 추출
Fat Interface → 역할별 Interface 분리
CommonBaseClass → Composition / Component 분리
EnumType.ORDINAL → EnumType.STRING
String 상태값 → Enum
valueOf 외부 입력 → fromCode
mutable static → Bean / ThreadLocal / Request Context 재검토
God Utility → Validator / Mapper / Service / Client 분리
```

---

### [FAQ]

Q. 이 파트에서 가장 중요한 리뷰 기준은?
A. Interface와 Abstract Class는 실제 추상화 필요성, Enum은 타입 안전성, static은 전역 상태 위험, final은 불변성 오해를 중점 검토한다.

Q. Interface 검수에서 가장 먼저 볼 것은?
A. 왜 Interface가 필요한지, 구현체 교체나 테스트 대체 같은 실제 이유가 있는지 확인한다.

Q. static 검수에서 가장 위험한 것은?
A. mutable static Field와 static Method 안의 외부 의존성 사용이다.

---

# 11. Backend Integration

## 11.1 Spring Boot Integration Rules

### [개념]

Interface, Abstract Class, Enum, Static, Final은 Spring Boot Backend 구조에서 역할 분리, 정책 교체, 상태 표현, 상수 관리, 객체 안정성을 담당한다.

잘못 사용하면 과설계, 전역 상태, Proxy 제약, 도메인 규칙 분산 문제가 발생할 수 있다.

---

### [핵심]

Spring Boot 연결:

```text
Interface
→ Policy / Client / Encoder / Sender 추상화

Abstract Class
→ 공통 처리 흐름 / Template Method

Enum
→ Status / Role / Category / Type 표현

Static
→ Constant / Utility / Factory Method

Final
→ Constructor Injection / Value Object / 불변 DTO 지원
```

---

### [실무]

Spring Boot 예:

```java
public interface PaymentClient {
    PaymentResult approve(PaymentCommand command);
}
```

```java
@Component
public class TossPaymentClient implements PaymentClient {
    @Override
    public PaymentResult approve(PaymentCommand command) {
        // Toss API call
        return null;
    }
}
```

Service:

```java
@Service
public class PaymentService {
    private final PaymentClient paymentClient;

    public PaymentService(PaymentClient paymentClient) {
        this.paymentClient = paymentClient;
    }

    public PaymentResult approve(PaymentCommand command) {
        return paymentClient.approve(command);
    }
}
```

Enum:

```java
public enum PaymentStatus {
    READY,
    PAID,
    CANCELED
}
```

Entity:

```java
@Enumerated(EnumType.STRING)
private PaymentStatus status;
```

검토 기준:

- 외부 API Client는 Interface로 추상화 가능한가?
- 정책 변경 가능성이 있는 로직은 Interface / Strategy로 분리했는가?
- 단순 Service에 불필요한 Interface를 만들지 않았는가?
- 공통 흐름은 Abstract Class보다 Composition으로 해결 가능한가?
- Status / Role / Type은 Enum으로 표현했는가?
- static에 요청별 상태를 저장하지 않는가?
- final 사용이 Spring Proxy와 충돌하지 않는가?

주의:

- Spring Bean은 기본적으로 싱글톤이므로 mutable Field를 조심한다.
- static 전역 상태와 Singleton Bean 상태를 혼동하지 않는다.
- Interface가 너무 많으면 Agent Retrieval에서도 구조 탐색 비용이 커진다.
- Enum 변경은 DB 데이터와 API 호환성에 영향을 줄 수 있다.

---

### [FAQ]

Q. Spring Boot에서 Interface는 어디에 쓰는 게 좋아?
A. 외부 API Client, 결제 처리, 알림 발송, 파일 저장, 정책 교체처럼 구현체 변경 가능성이 있는 곳에 적합하다.

Q. Spring Service는 final Class로 만들어도 돼?
A. 가능은 하지만 AOP / Proxy / Mock 제약을 확인해야 한다.

Q. Entity Status는 String과 Enum 중 뭐가 좋아?
A. 정해진 값 집합이면 Enum을 우선 검토하고 JPA 저장은 EnumType.STRING을 주로 검토한다.

---

# Retrieval Queries

### [FAQ]

Q. Interface는 뭐야?
A. 구현 Class가 따라야 할 역할과 계약을 정의하는 Java 추상화 도구다.

Q. Interface는 언제 만들어?
A. 역할 추상화, 구현체 교체, 테스트 대체, 다형성, 외부 의존성 분리가 필요할 때 만든다.

Q. Service마다 Interface를 꼭 만들어야 해?
A. 필수는 아니다. 구현체가 하나뿐이고 교체 가능성이 낮으면 과한 추상화가 될 수 있다.

Q. Interface 이름은 어떻게 짓는 게 좋아?
A. 구현 기술보다 역할과 계약이 드러나도록 짓는 것이 좋다.

Q. Interface Contract는 뭐야?
A. Interface 구현체가 지켜야 하는 입력, 출력, 예외, null 정책, Side Effect에 대한 약속이다.

Q. Interface Segregation은 뭐야?
A. 사용하지 않는 Method에 의존하지 않도록 Interface를 역할 단위로 작게 나누는 원칙이다.

Q. Fat Interface는 뭐야?
A. 서로 다른 책임의 Method가 많이 섞여 구현체에 불필요한 구현을 강요하는 Interface다.

Q. Functional Interface는 뭐야?
A. 추상 Method가 하나만 있는 Interface로 Lambda Expression의 대상이 될 수 있다.

Q. @FunctionalInterface는 꼭 붙여야 해?
A. 필수는 아니지만 컴파일러 검사를 받을 수 있어 권장한다.

Q. Predicate와 Function 차이는?
A. Predicate는 boolean을 반환하고 Function은 입력을 다른 결과 타입으로 변환한다.

Q. Abstract Class는 뭐야?
A. 직접 객체를 생성할 수 없고 공통 상태와 공통 구현을 하위 Class에 제공하는 Class다.

Q. Abstract Class는 언제 써?
A. 공통 상태와 공통 구현을 제공하면서 일부 동작을 하위 Class에 위임해야 할 때 사용한다.

Q. Abstract Method는 뭐야?
A. 선언만 있고 구현은 하위 Class가 담당하는 Method다.

Q. Template Method Pattern은 언제 써?
A. 처리 흐름은 고정되어 있고 일부 단계만 구현체마다 달라질 때 사용한다.

Q. Template Method를 final로 만드는 이유는?
A. 하위 Class가 전체 처리 흐름을 임의로 바꾸지 못하게 하기 위해서다.

Q. Interface와 Abstract Class 차이는?
A. Interface는 역할과 계약 중심이고 Abstract Class는 공통 상태와 구현을 함께 제공할 수 있다.

Q. Interface와 Abstract Class 중 무엇을 먼저 검토해?
A. 역할 추상화는 Interface를 먼저 검토하고 공통 상태와 구현 공유가 필요하면 Abstract Class를 검토한다.

Q. 단순 코드 재사용은 Abstract Class가 좋아?
A. 단순 재사용 목적이라면 상속보다 Composition을 우선 검토하는 것이 좋다.

Q. ServiceImpl 구조는 나쁜가?
A. 무조건 나쁘지는 않지만 구현체가 하나뿐이고 역할 추상화가 없다면 불필요할 수 있다.

Q. 구현체가 하나라도 Interface가 필요한 경우는?
A. 외부 시스템 경계, 테스트 대체, 정책 확장 가능성이 명확한 경우다.

Q. Enum은 뭐야?
A. 정해진 상수 집합을 타입 안전하게 표현하는 Java 타입이다.

Q. Enum은 왜 써?
A. 정해진 값 집합을 타입 안전하게 표현하고 문자열 오타를 줄이기 위해 사용한다.

Q. 문자열 상태값 대신 Enum을 쓰는 이유는?
A. 컴파일 시점 검사를 받을 수 있고 허용 값 범위가 명확해지기 때문이다.

Q. JPA에서 Enum은 어떻게 저장하는 게 좋아?
A. 보통 EnumType.STRING을 우선 검토한다.

Q. EnumType.ORDINAL은 왜 위험해?
A. Enum 순서가 바뀌면 DB에 저장된 숫자의 의미가 바뀔 수 있기 때문이다.

Q. Enum에 Field를 넣어도 돼?
A. 가능하다. 코드값, 표시명, 고정 속성을 표현할 수 있다.

Q. Enum에 Method를 넣어도 돼?
A. 가능하다. 상태별 고정 규칙이나 변환 로직을 표현할 수 있다.

Q. valueOf를 외부 입력에 써도 돼?
A. 권장하지 않는다. fromCode 같은 안전한 변환 Method를 검토하는 것이 좋다.

Q. 외부 API 코드값은 Enum 이름과 같게 해야 해?
A. 꼭 그럴 필요 없다. code Field로 분리하는 것이 변경에 더 안전할 수 있다.

Q. Enum에 복잡한 정책을 모두 넣어도 돼?
A. 간단한 고정 규칙은 가능하지만 복잡한 정책은 별도 Strategy나 Policy를 검토한다.

Q. static은 뭐야?
A. 객체 인스턴스가 아니라 Class 자체에 속하는 Member를 정의하는 키워드다.

Q. static은 언제 써?
A. 상수, 상태 없는 Utility Method, Static Factory Method처럼 객체 상태에 의존하지 않는 경우 사용한다.

Q. static을 많이 쓰면 왜 안 좋아?
A. 객체 책임이 흐려지고 테스트 대체와 확장이 어려워질 수 있다.

Q. static Field는 모든 객체가 공유해?
A. 그렇다. Class 단위로 하나만 존재한다.

Q. mutable static Field는 왜 위험해?
A. 전역으로 공유되어 동시성 문제, 테스트 오염, 요청 간 데이터 오염이 생길 수 있다.

Q. Static Method는 언제 적합해?
A. 객체 상태나 외부 의존성 없이 입력만으로 결과를 만드는 경우 적합하다.

Q. Static Method로 Repository를 호출해도 돼?
A. 권장하지 않는다. Spring DI, Transaction, 테스트 대체가 어려워진다.

Q. Static Factory Method는 왜 써?
A. 객체 생성 의도와 규칙을 Method 이름으로 명확히 표현할 수 있기 때문이다.

Q. final은 뭐야?
A. 변수 재할당, Method Override, Class 상속을 제한하는 Java 키워드다.

Q. final 변수는 값을 바꿀 수 없어?
A. 재할당할 수 없다. 단, 참조형 객체 내부 상태 변경까지 막는 것은 아니다.

Q. final을 붙이면 완전 불변이야?
A. 아니다. 참조 재할당만 막고 내부 객체가 mutable이면 상태는 바뀔 수 있다.

Q. 불변 객체를 만들려면 무엇이 필요해?
A. final Field, Setter 제거, 생성자 초기화, 방어적 복사, 내부 mutable 객체 노출 방지가 필요하다.

Q. final Method는 언제 써?
A. 하위 Class가 변경하면 안 되는 핵심 흐름을 고정할 때 사용한다.

Q. final Class는 언제 써?
A. 상속을 의도하지 않거나 불변 Value Object처럼 확장을 막고 싶을 때 사용한다.

Q. Spring에서 final Class를 조심해야 하는 이유는?
A. Proxy 기반 AOP나 Mock 생성에 제약이 생길 수 있기 때문이다.

Q. Static Method와 Instance Method 차이는?
A. Static Method는 Class에 속하고 Instance Method는 객체 상태와 책임에 속한다.

Q. 도메인 상태 변경을 Static Method로 해도 돼?
A. 권장하지 않는다. 객체 자신의 Instance Method로 표현하는 것이 좋다.

Q. Utility Class와 Spring Bean은 어떻게 구분해?
A. 외부 의존성, 설정 주입, Transaction, 테스트 대체가 필요하면 Spring Bean이 적합하다.

Q. Utility Class는 어떻게 만들어?
A. final Class, private Constructor, static Method 조합으로 만든다.

Q. Constant Class는 언제 써?
A. 여러 곳에서 반복되는 고정 문자열이나 숫자를 의미 있게 관리할 때 사용한다.

Q. 모든 상수를 CommonConstants에 넣어도 돼?
A. 권장하지 않는다. 도메인이나 목적별로 분리하는 것이 좋다.

Q. static 상태에 로그인 사용자 정보를 저장해도 돼?
A. 절대 권장하지 않는다. 요청 간 데이터 오염과 보안 문제가 생길 수 있다.

Q. Interface, Abstract Class, Enum, Static, Final 검수 순서는?
A. Interface 필요성, 계약, Abstract Class 필요성, Enum 타입 안전성, static 전역 상태, final 제약 순서로 검토한다.

Q. Java Part04 다음 문서는 뭐야?
A. Java Part05 — Collection and Generic 문서로 이어지는 것이 좋다.
