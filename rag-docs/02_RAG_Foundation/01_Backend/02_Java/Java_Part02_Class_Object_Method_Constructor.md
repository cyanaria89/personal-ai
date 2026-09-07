# Java Part02 — Class, Object, Method, Constructor

---

# 1. Class Foundation

## 1.1 Class Rules

### [개념]

Class는 Java에서 상태와 행위를 묶어 표현하는 설계 단위다.

Class는 객체를 생성하기 위한 설계도이며, Java Backend 코드의 기본 구조다.

Spring Boot의 Controller, Service, Repository, Entity, DTO, Config, Utility도 모두 Class 기반으로 작성된다.

```java
public class User {
    private Long userId;
    private String email;

    public boolean isActive() {
        return true;
    }
}
```

---

### [핵심]

Class 핵심 요소:

- Class
- Object
- Field
- Method
- Constructor
- Access Modifier
- Responsibility
- State
- Behavior
- Invariant
- Encapsulation
- Cohesion
- Single Responsibility

Class 설계 기준:

- 하나의 Class는 하나의 명확한 책임을 가진다.
- Field는 객체 상태를 표현한다.
- Method는 객체 행위를 표현한다.
- Constructor는 객체 생성 규칙을 표현한다.
- 외부 공개 API는 최소화한다.
- 내부 상태 변경은 Method로 제어한다.

---

### [실무]

2026 백엔드 실무 기준에서 Class는 단순 코드 묶음이 아니라 책임 단위다.

Class 설계 Flow:

```text
Requirement
→ Responsibility 식별
→ Class 후보 도출
→ Field 정의
→ Constructor 생성 규칙 정의
→ Method 행위 정의
→ Access Modifier 제한
→ Invariant 보호
→ Review
```

Spring Boot Layer별 Class 역할:

```text
Controller Class → HTTP 요청 / 응답 진입점
Service Class → 비즈니스 흐름 조정
Entity Class → 도메인 상태 / 행위 표현
DTO Class → 데이터 전달 구조
Repository Interface → 데이터 접근 추상화
Config Class → 설정 구성
Utility Class → 상태 없는 보조 기능
```

주의:

- 모든 기능을 하나의 Class에 몰아넣지 않는다.
- 단순 데이터 묶음과 도메인 객체를 구분한다.
- Class 이름은 책임을 표현해야 한다.
- Manager, Helper, Util 같은 이름은 책임이 모호할 수 있다.
- 변경 이유가 여러 개라면 Class 분리를 검토한다.

---

### [FAQ]

Q. Java Class는 무엇을 기준으로 나눠?
A. 책임 기준으로 나눈다. 하나의 Class가 너무 많은 이유로 변경된다면 분리 후보로 본다.

Q. Class 이름은 어떻게 짓는 게 좋아?
A. 역할과 책임이 드러나도록 명확하게 작성한다.

Q. Spring Boot에서도 Class 설계가 중요해?
A. 중요하다. Controller, Service, Entity, DTO 모두 Class 책임이 명확해야 유지보수가 쉽다.

---

## 1.2 Class Responsibility Rules

### [개념]

Class Responsibility는 Class가 맡아야 하는 역할과 변경 이유를 의미한다.

좋은 Class는 하나의 중심 책임을 가지며, 책임 밖의 작업을 과도하게 포함하지 않는다.

---

### [핵심]

책임 판단 키워드:

- responsibility
- single responsibility
- cohesion
- change reason
- domain responsibility
- service responsibility
- data responsibility
- validation responsibility
- mapping responsibility

Class 책임 질문:

```text
이 Class는 무엇을 책임지는가?
이 Class가 바뀌는 이유는 하나인가?
이 Method는 이 Class에 속하는 것이 자연스러운가?
이 Field는 이 Class의 상태인가?
이 Class 이름으로 내부 동작을 예측할 수 있는가?
```

---

### [실무]

책임 분리 기준:

```text
HTTP 처리 → Controller
비즈니스 흐름 → Service
도메인 상태 변경 → Entity
데이터 전달 → DTO
데이터 접근 → Repository
공통 검증 → Validator
외부 API 호출 → Client
설정 → Config
```

나쁜 예:

```java
public class UserService {
    public void createUser() {
        // request parsing
        // validation
        // password encryption
        // entity creation
        // database save
        // email sending
        // response mapping
    }
}
```

개선 방향:

```text
UserController → Request 수신
UserService → 가입 흐름 조정
PasswordEncoder → 비밀번호 암호화
User → 도메인 상태 보유
UserRepository → 저장
MailClient → 메일 발송
UserResponse → 응답 전달
```

주의:

- Service가 모든 책임을 흡수하지 않도록 한다.
- Entity가 단순 Getter / Setter 덩어리가 되지 않도록 한다.
- DTO에 비즈니스 로직을 넣지 않는다.
- Utility Class로 도메인 책임을 빼내지 않는다.

---

### [FAQ]

Q. Class 책임이 많다는 건 어떻게 알아?
A. Class 이름으로 설명하기 어렵거나 변경 이유가 여러 개라면 책임이 많은 신호다.

Q. Service Class는 모든 로직을 가져도 돼?
A. 아니다. 흐름 조정은 Service가 담당하지만 도메인 상태 변경은 Entity Method로 표현할 수 있다.

Q. DTO에 로직을 넣어도 돼?
A. 단순 변환이나 생성 보조는 가능하지만 핵심 비즈니스 로직은 DTO에 두지 않는 것이 좋다.

---

## 1.3 Class Naming Rules

### [개념]

Class Naming은 Class의 책임과 역할을 이름으로 표현하는 규칙이다.

Class 이름은 RAG Retrieval과 코드 리뷰 모두에 중요하다.

---

### [핵심]

Class Naming 핵심:

- 명사 중심
- 책임 중심
- 도메인 용어 사용
- 일관된 suffix 사용
- 모호한 이름 지양
- 축약어 남용 금지

자주 쓰는 이름 패턴:

```text
User
Post
Order
Payment

UserService
UserController
UserRepository
UserResponse
CreateUserRequest
UserValidator
PasswordEncoder
PaymentClient
SecurityConfig
```

---

### [실무]

권장:

- Entity는 도메인 명사 사용
- Service는 Use Case 또는 도메인 흐름 기준
- DTO는 Request / Response / Command 등 목적 명시
- Config는 설정 대상 명시
- Client는 외부 시스템 대상 명시
- Exception은 오류 상황 명시

나쁜 예:

```java
public class DataManager {
}

public class CommonUtil {
}

public class ProcessHelper {
}
```

좋은 예:

```java
public class UserRegistrationService {
}

public class PasswordResetTokenValidator {
}

public class TossPaymentClient {
}
```

주의:

- `Manager`는 책임이 모호해지기 쉽다.
- `Util`은 상태 없는 순수 보조 기능에만 제한적으로 사용한다.
- `Common`은 검색성과 책임 명확성이 낮다.
- Class 이름과 실제 책임이 다르면 Review 대상이다.

---

### [FAQ]

Q. Manager라는 이름을 쓰면 안 돼?
A. 무조건 금지는 아니지만 책임이 모호해지기 쉬워 더 구체적인 이름을 우선 검토한다.

Q. Util Class는 언제 써?
A. 상태가 없고 도메인 책임이 아닌 순수 보조 기능일 때 제한적으로 사용한다.

Q. Class 이름이 긴 건 나쁜가?
A. 책임이 명확하다면 긴 이름도 가능하다. 모호한 짧은 이름보다 명확한 이름이 좋다.

---

# 2. Object Foundation

## 2.1 Object Rules

### [개념]

Object는 Class를 기반으로 생성된 실제 인스턴스다.

Object는 상태를 가지고 Method를 통해 행위를 수행한다.

```java
User user = new User("user@example.com");
```

---

### [핵심]

Object 핵심:

- Object
- Instance
- State
- Behavior
- Identity
- Reference
- Heap
- Object Lifecycle
- Method Call
- Encapsulation

Object 구성:

```text
Class Definition
→ Constructor Call
→ Object Creation
→ Field State
→ Method Behavior
→ State Change
→ Garbage Collection 대상
```

---

### [실무]

객체 설계 기준:

- 객체는 자신의 상태를 스스로 보호한다.
- 외부에서 Field를 직접 변경하지 않는다.
- 상태 변경은 의미 있는 Method로 수행한다.
- 생성 시점에 필수 값을 검증한다.
- 객체가 불완전한 상태로 생성되지 않게 한다.

나쁜 예:

```java
User user = new User();
user.setEmail("user@example.com");
user.setStatus(UserStatus.ACTIVE);
```

좋은 예:

```java
User user = User.createActiveUser("user@example.com");
```

주의:

- 객체 생성 후 필수 값이 누락될 수 있는 구조는 위험하다.
- Setter 기반 생성은 불완전 객체를 만들 수 있다.
- Entity 객체는 JPA 요구사항과 도메인 생성 규칙을 함께 고려한다.
- DTO 객체와 Domain Object를 혼동하지 않는다.

---

### [FAQ]

Q. Class와 Object 차이는?
A. Class는 설계도이고 Object는 Class를 기반으로 생성된 실제 인스턴스다.

Q. 객체는 왜 상태를 직접 공개하면 안 돼?
A. 외부에서 상태를 마음대로 변경하면 객체의 규칙과 일관성이 깨질 수 있기 때문이다.

Q. 객체 생성 시 가장 중요한 것은?
A. 필수 값 검증과 불완전한 상태 방지다.

---

## 2.2 Object State Rules

### [개념]

Object State는 객체가 보유한 현재 값의 집합이다.

Java에서는 Field가 객체 상태를 표현한다.

```java
public class User {
    private String email;
    private UserStatus status;
}
```

---

### [핵심]

Object State 핵심:

- state
- field
- invariant
- mutable state
- immutable state
- valid state
- invalid state
- state transition
- encapsulation

상태 설계 질문:

```text
이 Field는 객체의 본질적 상태인가?
이 Field는 null이 될 수 있는가?
이 Field는 변경 가능한가?
이 Field 변경에는 규칙이 필요한가?
이 상태 조합은 유효한가?
```

---

### [실무]

상태 설계 기준:

- 필수 상태는 생성자에서 검증한다.
- 상태 변경은 Method로 제한한다.
- 서로 연관된 상태는 일관성 규칙을 정의한다.
- 외부에서 상태를 직접 바꾸지 못하게 한다.
- 상태 값이 정해진 범위라면 Enum 검토.
- 계산 가능한 값은 Field 저장보다 Method 계산 검토.

예:

```java
public void activate() {
    if (this.status == UserStatus.DELETED) {
        throw new IllegalStateException("deleted user cannot be activated");
    }

    this.status = UserStatus.ACTIVE;
}
```

주의:

- public Field 금지에 가깝게 검토.
- Setter 남용은 상태 규칙 분산을 만든다.
- mutable Collection Field 노출 주의.
- null 상태가 의미 있는지 명확히 판단한다.

---

### [FAQ]

Q. Object State는 무엇이야?
A. 객체가 현재 가지고 있는 Field 값들의 상태를 의미한다.

Q. Field는 무조건 private이어야 해?
A. 대부분 private이 좋다. 상태 변경 규칙을 Method 안에 모으기 위해서다.

Q. 계산 가능한 값도 Field로 저장해야 해?
A. 항상 그렇지 않다. 저장 값과 계산 값의 일관성 문제가 생길 수 있다.

---

## 2.3 Object Behavior Rules

### [개념]

Object Behavior는 객체가 수행할 수 있는 행위다.

Java에서는 Method가 객체 행위를 표현한다.

```java
public void changeEmail(String newEmail) {
    this.email = newEmail;
}
```

---

### [핵심]

Object Behavior 핵심:

- behavior
- method
- command method
- query method
- state change
- validation
- domain rule
- side effect
- return value

Method 유형:

```text
Command Method → 상태 변경
Query Method → 상태 조회
Factory Method → 객체 생성
Validation Method → 규칙 검증
Conversion Method → 다른 표현으로 변환
```

---

### [실무]

행위 설계 기준:

- Method 이름은 행위를 명확히 표현한다.
- 상태 변경 Method에는 비즈니스 규칙을 포함한다.
- 조회 Method는 상태 변경을 하지 않는 것이 좋다.
- Command와 Query를 혼합하지 않는다.
- 외부 객체의 상태를 과도하게 변경하지 않는다.

나쁜 예:

```java
user.setPoint(user.getPoint() + 100);
```

좋은 예:

```java
user.addPoint(100);
```

좋은 예:

```java
public void addPoint(int point) {
    if (point <= 0) {
        throw new IllegalArgumentException("point must be positive");
    }

    this.point += point;
}
```

주의:

- Getter / Setter만 있는 객체는 도메인 행위가 빈약할 수 있다.
- Method가 너무 많은 일을 하면 책임 분리 필요.
- 객체 행위가 Service로 모두 빠져나가면 Anemic Domain Model 가능성 검토.
- DTO는 행위보다 전달 목적이 우선이다.

---

### [FAQ]

Q. Object Behavior는 무엇으로 표현해?
A. Java에서는 Method로 객체 행위를 표현한다.

Q. Setter 대신 의미 있는 Method를 쓰는 이유는?
A. 상태 변경 규칙을 Method 안에 모아 일관성을 지키기 위해서다.

Q. 조회 Method가 상태를 바꿔도 돼?
A. 가능은 하지만 예측 가능성이 떨어지므로 피하는 것이 좋다.

---

# 3. Field Rules

## 3.1 Field Design Rules

### [개념]

Field는 Class 또는 Object가 가지는 상태 값이다.

Instance Field는 객체마다 별도의 값을 가지고, Static Field는 Class 단위로 공유된다.

```java
public class User {
    private Long userId;
    private String email;
}
```

---

### [핵심]

Field 핵심:

- field
- instance field
- static field
- private field
- final field
- mutable field
- nullable field
- default value
- state
- access control

Field 설계 기준:

- 객체의 상태인지 확인
- null 가능성 확인
- 변경 가능성 확인
- 초기화 시점 확인
- 외부 공개 필요성 확인
- DB 매핑 여부 확인

---

### [실무]

권장:

- Field는 private 우선
- 필수 Field는 생성자에서 초기화
- 변경되지 않는 Field는 final 검토
- 상태 변경은 Method로 제어
- nullable Field는 의미를 명확히 함
- Collection Field는 외부 직접 수정 방지
- static mutable Field 지양

좋은 예:

```java
public class User {
    private final String email;
    private UserStatus status;

    public User(String email) {
        this.email = Objects.requireNonNull(email, "email must not be null");
        this.status = UserStatus.ACTIVE;
    }
}
```

주의:

- public Field는 캡슐화 위반 가능성이 높다.
- 모든 Field에 Setter 자동 생성은 지양.
- JPA Entity는 final Field 사용에 제약이 있을 수 있다.
- 기본값에 의존하면 의도와 다른 상태가 생길 수 있다.

---

### [FAQ]

Q. Field는 왜 private으로 둬?
A. 객체 상태를 보호하고 변경 규칙을 Method 안에 모으기 위해서다.

Q. Field에 final을 붙이면 무조건 좋아?
A. 변경 불필요한 값에는 좋지만 JPA Entity 등에서는 제약이 있어 상황에 맞게 판단한다.

Q. Field 기본값에 의존해도 돼?
A. 가능하지만 의도가 명확하지 않으면 생성자나 초기화 Method로 표현하는 것이 좋다.

---

## 3.2 Field Initialization Rules

### [개념]

Field Initialization은 객체가 사용 가능한 상태가 되도록 Field에 초기값을 설정하는 작업이다.

초기화 방법:

```text
Field 선언 시 초기화
Constructor 초기화
Factory Method 초기화
Lifecycle Callback 초기화
```

---

### [핵심]

초기화 핵심:

- initialization
- default value
- constructor
- required field
- optional field
- invariant
- valid object
- null prevention

---

### [실무]

초기화 기준:

- 필수 Field는 생성 시점에 값 설정
- 기본 상태는 명시적으로 설정
- Collection Field는 빈 Collection으로 초기화
- 시간 Field는 정책에 따라 설정
- JPA Entity는 기본 생성자 요구사항 확인
- DTO는 record 또는 생성자 기반 검토

예:

```java
public class Post {
    private String title;
    private PostStatus status;
    private List<Comment> comments = new ArrayList<>();

    public Post(String title) {
        this.title = Objects.requireNonNull(title, "title must not be null");
        this.status = PostStatus.DRAFT;
    }
}
```

주의:

- 필수 Field를 null 상태로 방치하지 않는다.
- Collection Field를 null로 두면 NPE 위험 증가.
- 생성자에서 너무 많은 로직을 수행하지 않는다.
- 시간 생성 정책은 Entity, Auditing, DB 기준을 통일한다.

---

### [FAQ]

Q. Collection Field는 null로 둬도 돼?
A. 대부분 빈 Collection으로 초기화하는 것이 좋다.

Q. 필수 Field는 어디서 검증해?
A. 생성자나 Factory Method에서 빠르게 검증하는 것이 좋다.

Q. Field 초기화가 중요한 이유는?
A. 불완전한 객체 생성을 막고 NullPointerException 위험을 줄이기 위해서다.

---

## 3.3 Mutable Field Rules

### [개념]

Mutable Field는 객체 생성 후 값이 변경될 수 있는 Field다.

Mutable Field는 상태 전이 규칙과 일관성 보호가 필요하다.

---

### [핵심]

Mutable Field 핵심:

- mutable state
- state change
- setter
- command method
- invariant
- validation
- consistency
- side effect

---

### [실무]

Mutable Field 사용 기준:

- 변경이 필요한 상태인지 확인
- 변경 Method에 검증 로직 포함
- Setter보다 의미 있는 Method 우선
- 변경 전후 유효 상태 유지
- 변경 이력이나 이벤트가 필요한지 검토
- 동시성 접근 가능성 확인

나쁜 예:

```java
public void setStatus(UserStatus status) {
    this.status = status;
}
```

좋은 예:

```java
public void deactivate() {
    if (this.status == UserStatus.DELETED) {
        throw new IllegalStateException("deleted user cannot be deactivated");
    }

    this.status = UserStatus.INACTIVE;
}
```

주의:

- Mutable Field가 많으면 객체 추적이 어려워진다.
- 여러 Field가 함께 변경되어야 하면 하나의 Method로 묶는다.
- 외부에서 Field 변경 순서를 강제하게 만들지 않는다.
- static mutable Field는 전역 상태 문제가 생길 수 있다.

---

### [FAQ]

Q. Setter는 쓰면 안 돼?
A. 무조건 금지는 아니지만 비즈니스 상태 변경은 의미 있는 Method로 표현하는 것이 좋다.

Q. Mutable Field가 많으면 뭐가 문제야?
A. 객체 상태 추적이 어려워지고 잘못된 상태 조합이 생길 수 있다.

Q. 상태 변경 Method에는 무엇이 들어가야 해?
A. 변경 가능 여부 검증과 상태 일관성 유지 규칙이 들어가야 한다.

---

# 4. Method Foundation

## 4.1 Method Rules

### [개념]

Method는 객체나 Class가 수행하는 하나의 작업 단위다.

Method는 입력 Parameter를 받고, 작업을 수행하고, 필요하면 Return Value를 반환한다.

```java
public boolean canPublish(Post post) {
    return post != null && post.isDraft() && post.hasContent();
}
```

---

### [핵심]

Method 핵심:

- method
- method name
- parameter
- return type
- method body
- responsibility
- side effect
- validation
- exception
- readability
- testability

Method 설계 기준:

- 하나의 Method는 하나의 책임
- 이름은 동작을 표현
- Parameter는 적을수록 좋음
- Return Type은 명확해야 함
- Side Effect는 예측 가능해야 함
- 예외 발생 조건은 명확해야 함

---

### [실무]

Method 설계 Flow:

```text
Purpose 식별
→ Method 이름 작성
→ Input Parameter 결정
→ Return Type 결정
→ Validation 위치 결정
→ Exception 기준 결정
→ Side Effect 확인
→ Test 가능성 확인
```

권장:

- Method 이름만 보고 목적을 알 수 있어야 한다.
- 긴 Method는 작은 Method로 분리한다.
- 중복 로직은 의미 있는 Method로 추출한다.
- Command Method와 Query Method를 구분한다.
- 비즈니스 규칙은 이름 있는 Method로 표현한다.

나쁜 예:

```java
public void process(User user) {
}
```

좋은 예:

```java
public void activateUser(User user) {
}
```

주의:

- Method 이름이 모호하면 Retrieval 품질도 떨어진다.
- Method가 너무 많은 Parameter를 받으면 Command 객체 검토.
- Method 내부에서 너무 많은 외부 의존성을 직접 다루면 책임 과다.
- private Method 분리는 가독성을 높일 때만 의미가 있다.

---

### [FAQ]

Q. Method는 어떻게 설계해?
A. 하나의 Method는 하나의 책임을 가지며 이름은 동작을 명확히 표현해야 한다.

Q. Method가 너무 길면 어떻게 해?
A. 책임 단위로 분리하고 이름 있는 private Method나 별도 Class로 추출한다.

Q. Method 이름은 왜 중요해?
A. 코드 가독성, 테스트 의도, RAG 검색 매칭에 직접 영향을 준다.

---

## 4.2 Method Naming Rules

### [개념]

Method Naming은 Method가 수행하는 동작과 결과를 이름으로 표현하는 규칙이다.

좋은 Method 이름은 주석 없이 의도를 전달한다.

---

### [핵심]

Method Naming 핵심:

- verb-based name
- action
- intention revealing name
- query method
- command method
- boolean method
- conversion method
- factory method

자주 쓰는 패턴:

```text
createUser
findUser
getUser
updateEmail
deletePost
activate
deactivate
validatePassword
canPublish
isActive
hasPermission
toResponse
from
of
```

---

### [실무]

Naming 기준:

- 상태 변경 Method는 동사 사용
- boolean 반환 Method는 is / has / can / should 사용
- 조회 Method는 find / get 구분
- 검증 Method는 validate 사용
- 변환 Method는 to / from 사용
- 생성 Method는 create / of 사용 가능

예:

```java
public boolean canPublish() {
    return this.status == PostStatus.DRAFT && this.content != null;
}
```

예:

```java
public void changeEmail(String newEmail) {
    validateEmail(newEmail);
    this.email = newEmail;
}
```

주의:

- `process`, `handle`, `doWork`는 의미가 모호할 수 있다.
- `get`은 단순 조회 느낌이 강하다.
- 없을 수 있는 조회는 `find`가 더 적합할 수 있다.
- Method 이름과 실제 Side Effect가 다르면 위험하다.

---

### [FAQ]

Q. boolean Method 이름은 어떻게 짓는 게 좋아?
A. is, has, can, should 같은 접두어를 사용하면 의도가 명확하다.

Q. find와 get 차이는?
A. find는 없을 수 있음을 암시하고 get은 존재한다고 기대하는 느낌이 강하다.

Q. process라는 Method 이름은 왜 안 좋아?
A. 어떤 작업을 하는지 구체적으로 드러나지 않아 책임이 모호하다.

---

## 4.3 Method Parameter Rules

### [개념]

Method Parameter는 Method 실행에 필요한 입력 값이다.

Parameter는 Method 책임과 입력 조건을 드러낸다.

```java
public void changeEmail(String newEmail) {
}
```

---

### [핵심]

Parameter 핵심:

- parameter
- input
- required value
- optional value
- validation
- parameter count
- command object
- request DTO
- value object
- boolean flag

---

### [실무]

Parameter 설계 기준:

- 필수 Parameter는 null 검증
- Parameter 개수는 최소화
- 같은 의미의 값은 객체로 묶기
- boolean flag Parameter 지양
- 순서 혼동 가능한 같은 타입 Parameter 주의
- Collection Parameter는 null보다 empty collection 기대
- Method 내부에서 Parameter 재할당 지양

나쁜 예:

```java
public void register(String email, String password, String nickname, Boolean active, String role) {
}
```

좋은 예:

```java
public void register(RegisterUserCommand command) {
}
```

순서 혼동 위험:

```java
public Period(LocalDate startDate, LocalDate endDate) {
}
```

개선:

```java
public record Period(LocalDate startDate, LocalDate endDate) {
    public Period {
        if (startDate.isAfter(endDate)) {
            throw new IllegalArgumentException("startDate must be before endDate");
        }
    }
}
```

주의:

- Parameter가 많으면 Method 책임이 클 수 있다.
- null 허용 Parameter는 문서나 타입으로 명확히 표현한다.
- Optional을 Parameter로 받는 것은 일반적으로 지양.
- DTO와 Command 객체의 목적을 구분한다.

---

### [FAQ]

Q. Method Parameter는 몇 개까지가 좋아?
A. 정해진 수보다 의미가 중요하지만 많아지면 DTO, Command, Value Object로 묶는 것을 검토한다.

Q. boolean Parameter는 왜 피하는 게 좋아?
A. 호출 코드에서 true / false의 의미가 드러나지 않기 때문이다.

Q. Optional을 Parameter로 받아도 돼?
A. 일반적으로 권장하지 않는다. Optional은 반환 타입에 사용하는 것이 더 적합하다.

---

## 4.4 Return Type Rules

### [개념]

Return Type은 Method가 호출자에게 반환하는 값의 타입이다.

Return Type은 Method의 결과 의미와 실패 가능성을 표현한다.

```java
public Optional<User> findUser(Long userId) {
}
```

---

### [핵심]

Return Type 핵심:

- return type
- void
- primitive return
- object return
- Optional
- List
- empty collection
- null return
- DTO return
- result object

---

### [실무]

Return Type 설계 기준:

```text
결과 없음 가능 → Optional<T>
목록 결과 → List<T>
중복 없는 목록 → Set<T>
성공 / 실패와 데이터 포함 → Result Object 검토
응답 데이터 → Response DTO
상태 변경만 수행 → void 가능
계산 결과 → 명확한 primitive / Wrapper Type
```

권장:

- Collection 반환은 null보다 empty collection
- 단일 조회 결과 없음 가능성은 Optional 검토
- Controller 응답은 DTO 사용
- Entity 직접 반환 지양
- 반환 타입으로 Method 의도 표현

나쁜 예:

```java
public User findUser(Long userId) {
    return null;
}
```

좋은 예:

```java
public Optional<User> findUser(Long userId) {
    return userRepository.findById(userId);
}
```

Service 변환 예:

```java
public User getUser(Long userId) {
    return userRepository.findById(userId)
        .orElseThrow(() -> new UserNotFoundException(userId));
}
```

주의:

- null 반환은 호출자 부담을 늘린다.
- Optional을 Collection에 감싸는 것은 대부분 불필요하다.
- `Optional<List<T>>`보다 empty List 반환이 보통 낫다.
- 반환 타입이 Object이면 타입 안정성이 낮다.

---

### [FAQ]

Q. Method에서 null을 반환해도 돼?
A. 가능하지만 권장하지 않는다. Optional이나 empty collection을 검토하는 것이 좋다.

Q. List 결과가 없으면 null을 반환해?
A. 보통 empty List를 반환하는 것이 좋다.

Q. Optional은 언제 반환해?
A. 단일 결과가 없을 수 있음을 호출자에게 명시할 때 사용한다.

---

## 4.5 Method Side Effect Rules

### [개념]

Side Effect는 Method가 Return Value 외에 외부 상태나 객체 상태를 변경하는 효과다.

예:

```text
Field 변경
DB 저장
외부 API 호출
파일 쓰기
메시지 발행
로그 기록
```

---

### [핵심]

Side Effect 핵심:

- side effect
- state change
- command method
- query method
- database write
- external call
- transaction
- predictability
- testability

---

### [실무]

Side Effect 설계 기준:

- 상태 변경 Method는 이름에 변경 의도를 드러낸다.
- 조회 Method는 상태 변경을 하지 않는다.
- DB 저장은 Transaction 경계를 고려한다.
- 외부 API 호출은 실패 가능성을 고려한다.
- Side Effect가 많으면 Method 분리 검토.
- 테스트에서 Mock / Stub이 필요한지 확인한다.

나쁜 예:

```java
public User getUser(Long userId) {
    User user = findUser(userId);
    user.increaseViewCount();
    userRepository.save(user);
    return user;
}
```

개선 방향:

```java
public User readUserAndIncreaseViewCount(Long userId) {
    User user = getUserOrThrow(userId);
    user.increaseViewCount();
    return user;
}
```

주의:

- Method 이름이 조회인데 상태를 바꾸면 예측이 어렵다.
- Side Effect가 많을수록 테스트가 어려워진다.
- 외부 시스템 Side Effect는 재시도 / 중복 처리 고려.
- Entity 상태 변경과 Repository 저장 시점을 구분한다.

---

### [FAQ]

Q. Side Effect는 나쁜 거야?
A. 아니다. 상태 변경은 필요하지만 Method 이름과 책임 안에서 예측 가능해야 한다.

Q. 조회 Method가 DB를 수정해도 돼?
A. 가능은 하지만 Method 이름에 수정 의도를 드러내는 것이 좋다.

Q. Side Effect가 많은 Method는 어떻게 해?
A. 책임 단위로 분리하고 Transaction, 외부 호출, 상태 변경을 명확히 구분한다.

---

# 5. Constructor Foundation

## 5.1 Constructor Rules

### [개념]

Constructor는 객체 생성 시 호출되는 특별한 Method 형태다.

Constructor는 객체가 유효한 상태로 생성되도록 필수 값을 초기화하고 검증한다.

```java
public class User {
    private final String email;

    public User(String email) {
        this.email = Objects.requireNonNull(email, "email must not be null");
    }
}
```

---

### [핵심]

Constructor 핵심:

- constructor
- object creation
- required field
- initialization
- validation
- invariant
- default constructor
- overloaded constructor
- private constructor
- factory method

Constructor 역할:

- 필수 Field 초기화
- 기본 상태 설정
- 생성 규칙 검증
- 불완전 객체 방지
- Invariant 보호

---

### [실무]

Constructor 설계 기준:

- 필수 값은 Constructor Parameter로 받는다.
- Constructor에서 필수 값 null 검증.
- 기본 상태는 명확히 설정.
- 생성 시점에 불변 조건을 검증.
- 생성 로직이 복잡하면 Static Factory Method 검토.
- JPA Entity는 protected no-args Constructor 고려.

좋은 예:

```java
public class Post {
    private String title;
    private PostStatus status;

    public Post(String title) {
        if (title == null || title.isBlank()) {
            throw new IllegalArgumentException("title must not be blank");
        }

        this.title = title;
        this.status = PostStatus.DRAFT;
    }
}
```

주의:

- Constructor에서 외부 API 호출 지양.
- Constructor에서 DB 접근 금지.
- 너무 많은 Parameter는 객체 분리 또는 Builder 검토.
- Setter로 필수 값을 나중에 채우는 구조 지양.

---

### [FAQ]

Q. Constructor의 가장 중요한 역할은?
A. 객체를 유효한 상태로 생성하고 필수 값을 초기화하는 것이다.

Q. Constructor에서 검증을 해도 돼?
A. 필수 값과 불변 조건 검증은 Constructor에서 하는 것이 좋다.

Q. Constructor에 로직이 많으면 어떻게 해?
A. Static Factory Method, Builder, 별도 Factory Class를 검토한다.

---

## 5.2 Default Constructor Rules

### [개념]

Default Constructor는 Parameter가 없는 생성자다.

Java에서 Constructor를 하나도 작성하지 않으면 컴파일러가 기본 생성자를 자동 생성한다.

하지만 Constructor를 직접 작성하면 기본 생성자는 자동 생성되지 않는다.

---

### [핵심]

Default Constructor 핵심:

- default constructor
- no-args constructor
- compiler generated constructor
- JPA requirement
- object initialization
- incomplete object risk

---

### [실무]

JPA Entity 기준:

```java
protected User() {
}
```

JPA Entity는 프록시 생성과 Reflection 기반 객체 생성을 위해 기본 생성자가 필요하다.

권장:

- 일반 객체는 필수 값을 받는 Constructor 우선.
- JPA Entity 기본 생성자는 protected로 제한.
- public no-args Constructor 남용 지양.
- 기본 생성자 이후 Setter로 필수 값을 채우는 구조 지양.

나쁜 예:

```java
public User() {
}
```

좋은 예:

```java
protected User() {
}
```

주의:

- 기본 생성자는 불완전 객체를 만들 수 있다.
- Framework 요구사항 때문에 필요한 경우 접근 제한을 둔다.
- DTO 역직렬화 구조에서는 기본 생성자가 필요한 경우도 있다.
- record DTO는 기본 생성자와 다른 방식으로 처리된다.

---

### [FAQ]

Q. 기본 생성자는 항상 필요해?
A. 아니다. 일반 객체는 필수 값을 받는 생성자가 더 안전하다.

Q. JPA Entity에는 기본 생성자가 필요해?
A. 필요하다. 보통 protected no-args Constructor를 둔다.

Q. public 기본 생성자는 왜 조심해야 해?
A. 필수 값이 없는 불완전 객체가 외부에서 생성될 수 있기 때문이다.

---

## 5.3 Constructor Overloading Rules

### [개념]

Constructor Overloading은 같은 Class 안에서 Parameter 구성이 다른 여러 Constructor를 정의하는 것이다.

```java
public User(String email) {
    this(email, UserStatus.ACTIVE);
}

public User(String email, UserStatus status) {
    this.email = email;
    this.status = status;
}
```

---

### [핵심]

Constructor Overloading 핵심:

- constructor overloading
- multiple constructors
- this()
- default value
- required parameter
- optional parameter
- readability

---

### [실무]

Overloading 기준:

- 필수 값과 선택 값을 구분할 때 사용.
- 기본값 설정이 명확할 때 사용.
- 중복 초기화 로직은 `this()`로 위임.
- Constructor 조합이 많아지면 Builder 검토.
- Parameter Type이 같아 순서 혼동 가능하면 Value Object 검토.

좋은 예:

```java
public Post(String title) {
    this(title, PostStatus.DRAFT);
}

public Post(String title, PostStatus status) {
    validateTitle(title);
    this.title = title;
    this.status = status;
}
```

주의:

- Overloading이 많으면 생성 의도가 불명확해질 수 있다.
- 같은 타입 Parameter 여러 개는 순서 오류 위험.
- optional 값이 많으면 Builder 또는 Factory Method가 더 명확할 수 있다.

---

### [FAQ]

Q. Constructor Overloading은 언제 써?
A. 필수 값과 기본값 조합을 명확히 표현할 수 있을 때 사용한다.

Q. Constructor가 너무 많으면 어떻게 해?
A. Static Factory Method나 Builder Pattern을 검토한다.

Q. this()는 왜 사용해?
A. Constructor 간 중복 초기화 로직을 줄이기 위해 사용한다.

---

# 6. Static Factory Method Rules

## 6.1 Static Factory Method Basics

### [개념]

Static Factory Method는 Constructor 대신 이름 있는 static Method로 객체를 생성하는 방식이다.

```java
public static User createActiveUser(String email) {
    return new User(email, UserStatus.ACTIVE);
}
```

---

### [핵심]

Static Factory Method 핵심:

- static factory method
- named constructor
- object creation
- readability
- validation
- default value
- domain creation rule
- private constructor

---

### [실무]

Static Factory Method 적합 상황:

- 생성 의도를 이름으로 드러내야 함
- 생성 규칙이 여러 개 있음
- 기본 상태를 명확히 설정해야 함
- Constructor Parameter 의미가 모호함
- 객체 생성 전 검증이 필요함
- 하위 타입이나 캐싱 객체 반환 가능성이 있음

예:

```java
public class User {
    private String email;
    private UserStatus status;

    private User(String email, UserStatus status) {
        this.email = Objects.requireNonNull(email, "email must not be null");
        this.status = Objects.requireNonNull(status, "status must not be null");
    }

    public static User createActiveUser(String email) {
        return new User(email, UserStatus.ACTIVE);
    }

    public static User createPendingUser(String email) {
        return new User(email, UserStatus.PENDING);
    }
}
```

주의:

- static Factory Method가 너무 많으면 생성 정책 분리 검토.
- 이름이 모호하면 Constructor보다 나쁠 수 있다.
- JPA Entity에서는 private Constructor와 Framework 요구사항을 함께 고려.
- 외부 의존성이 필요한 생성은 별도 Factory Bean이 적합할 수 있다.

---

### [FAQ]

Q. Static Factory Method는 왜 써?
A. 객체 생성 의도와 규칙을 Method 이름으로 명확히 표현할 수 있기 때문이다.

Q. Constructor보다 항상 좋아?
A. 아니다. 단순 생성은 Constructor가 충분하고 생성 의도가 여러 개면 Static Factory Method가 좋다.

Q. Static Factory Method 이름은 어떻게 짓는 게 좋아?
A. create, of, from, valueOf처럼 생성 의미가 드러나는 이름을 사용한다.

---

## 6.2 Factory Method Naming Rules

### [개념]

Factory Method Naming은 객체 생성 방식과 입력 의미를 이름으로 표현하는 규칙이다.

---

### [핵심]

주요 이름:

```text
of
from
create
createActiveUser
valueOf
empty
defaultInstance
```

이름별 의미:

```text
of → 여러 값을 조합해 생성
from → 다른 타입에서 변환해 생성
create → 새 객체 생성 의도
valueOf → 값 변환 또는 캐싱 가능성
empty → 빈 객체 생성
```

---

### [실무]

예:

```java
public static Email of(String value) {
    return new Email(value);
}
```

```java
public static UserResponse from(User user) {
    return new UserResponse(user.getId(), user.getEmail());
}
```

```java
public static Order createPendingOrder(User user) {
    return new Order(user, OrderStatus.PENDING);
}
```

주의:

- `from`은 변환 출처가 명확할 때 사용.
- `of`는 값 조합으로 새 객체를 만들 때 적합.
- 도메인 상태가 중요하면 `createActiveUser`처럼 구체화.
- Factory Method 내부에 과도한 비즈니스 흐름을 넣지 않는다.

---

### [FAQ]

Q. of와 from 차이는?
A. of는 값을 조합해 생성하는 느낌이고 from은 다른 객체나 타입에서 변환하는 느낌이다.

Q. create는 언제 써?
A. 새 도메인 객체를 생성하는 의도를 명확히 표현할 때 사용한다.

Q. Factory Method에 비즈니스 로직을 많이 넣어도 돼?
A. 생성 규칙은 가능하지만 전체 비즈니스 흐름은 Service나 Factory Class 분리를 검토한다.

---

# 7. Access Modifier Rules

## 7.1 Access Modifier Basics

### [개념]

Access Modifier는 Class, Field, Method, Constructor에 대한 접근 범위를 제한하는 Java 문법이다.

대표 접근 제어자:

```text
public
protected
default(package-private)
private
```

---

### [핵심]

Access Modifier 핵심:

- public
- protected
- package-private
- private
- encapsulation
- visibility
- API surface
- information hiding
- state protection

접근 범위:

| Modifier  | 접근 범위                 |
| --------- | ------------------------- |
| public    | 모든 곳                   |
| protected | 같은 Package + 하위 Class |
| default   | 같은 Package              |
| private   | 같은 Class 내부           |

---

### [실무]

접근 제어 기준:

- Field는 private 우선
- 외부 API Method만 public
- 내부 보조 Method는 private
- 같은 Package 내부 협력은 package-private 검토
- 상속 확장 지점만 protected
- Constructor 접근 제한으로 생성 규칙 제어

예:

```java
public class User {
    private String email;

    public void changeEmail(String newEmail) {
        validateEmail(newEmail);
        this.email = newEmail;
    }

    private void validateEmail(String email) {
        if (email == null || email.isBlank()) {
            throw new IllegalArgumentException("email must not be blank");
        }
    }
}
```

주의:

- public은 API Surface를 넓힌다.
- protected는 하위 Class 결합도를 높일 수 있다.
- private Method가 많으면 Class 책임 과다일 수 있다.
- 접근 범위는 작게 시작하고 필요할 때 넓힌다.

---

### [FAQ]

Q. 접근 제어자는 기본적으로 어떻게 잡아?
A. 가능한 좁게 잡고 필요한 경우에만 넓힌다.

Q. Field는 왜 public으로 두면 안 좋아?
A. 외부에서 상태를 직접 변경해 객체 규칙이 깨질 수 있기 때문이다.

Q. protected는 언제 써?
A. 상속 구조에서 하위 Class 확장 지점이 명확할 때 제한적으로 사용한다.

---

## 7.2 Public API Rules

### [개념]

Public API는 외부 Class가 호출할 수 있는 공개 Method와 Constructor다.

Public API는 한 번 공개되면 변경 비용이 크다.

---

### [핵심]

Public API 핵심:

- public method
- public constructor
- external usage
- contract
- backward compatibility
- stable interface
- minimal API
- encapsulation

---

### [실무]

Public API 설계 기준:

- 꼭 필요한 Method만 public으로 공개
- Method 이름과 Parameter 의미를 명확히 함
- Return Type을 안정적으로 설계
- 예외 발생 조건을 명확히 함
- 내부 구현 세부사항을 노출하지 않음
- DTO / Interface로 경계를 분리

나쁜 예:

```java
public void validateInternalState() {
}
```

좋은 예:

```java
public boolean canPublish() {
    return this.status == PostStatus.DRAFT && this.content != null;
}
```

주의:

- public Method가 많으면 객체 사용 방식이 복잡해진다.
- public Setter는 상태 변경 규칙을 외부로 흩어지게 한다.
- 내부 구현용 Method는 private 또는 package-private 검토.
- public API 변경은 테스트와 호출부 영향을 확인해야 한다.

---

### [FAQ]

Q. Method는 public으로 많이 열어도 돼?
A. 필요한 것만 public으로 열고 내부 구현은 숨기는 것이 좋다.

Q. public API는 왜 신중해야 해?
A. 외부 호출부와 계약이 되기 때문에 변경 비용이 크다.

Q. public Setter는 왜 조심해야 해?
A. 객체 상태 변경 규칙이 외부로 분산될 수 있기 때문이다.

---

# 8. Package Rules

## 8.1 Package Purpose

### [개념]

Package는 관련 Class를 묶고 이름 충돌을 방지하는 Java의 구조화 단위다.

Spring Boot 프로젝트에서는 Package 구조가 Layer와 Domain 구조를 표현한다.

```java
package com.example.user.service;
```

---

### [핵심]

Package 핵심:

- package
- namespace
- class grouping
- layer package
- domain package
- package-private
- import
- structure
- cohesion

---

### [실무]

Package 설계 기준:

- 관련 Class를 같은 Package로 묶는다.
- Layer 또는 Domain 기준을 일관되게 적용한다.
- Package 이름은 소문자 사용.
- 너무 깊은 Package 구조 지양.
- package-private 접근으로 내부 협력 제한 가능.
- 공통 Package 남용 주의.

Layer 기준 예:

```text
com.example.user.controller
com.example.user.service
com.example.user.repository
com.example.user.dto
com.example.user.entity
```

Domain 기준 예:

```text
com.example.user
com.example.post
com.example.payment
com.example.notification
```

주의:

- `common` Package는 책임이 모호해지기 쉽다.
- 모든 DTO를 한 Package에 몰면 검색성과 응집도가 떨어질 수 있다.
- 순환 의존이 생기면 Package 구조 재검토.
- Package 구조와 Agent Retrieval 구조도 일관되면 좋다.

---

### [FAQ]

Q. Package는 왜 필요해?
A. 관련 Class를 묶고 이름 충돌을 방지하며 구조를 표현하기 위해 필요하다.

Q. Layer 기준 Package와 Domain 기준 Package 중 뭐가 좋아?
A. 프로젝트 규모와 팀 기준에 따라 다르다. 중요한 것은 일관성이다.

Q. common Package는 쓰면 안 돼?
A. 무조건 금지는 아니지만 책임이 모호한 코드가 쌓이기 쉬워 주의해야 한다.

---

# 9. DTO, Entity, Service Class Distinction

## 9.1 DTO Class Rules

### [개념]

DTO는 Layer 간 데이터 전달을 위한 객체다.

DTO는 도메인 상태 변경 책임이 아니라 데이터 입력 / 출력 구조 표현이 목적이다.

```java
public record UserResponse(
    Long userId,
    String email
) {
}
```

---

### [핵심]

DTO 핵심:

- DTO
- Request DTO
- Response DTO
- Command
- data transfer
- API boundary
- validation
- mapping
- immutable data
- record

---

### [실무]

DTO 설계 기준:

- Request DTO는 입력 데이터 구조 표현
- Response DTO는 출력 데이터 구조 표현
- Entity 직접 노출 지양
- DTO에 핵심 비즈니스 로직 지양
- 단순 변환 Method는 허용 가능
- 불변 DTO는 record 검토
- Validation Annotation은 Request DTO에 적용 가능

예:

```java
public record CreateUserRequest(
    String email,
    String password
) {
}
```

```java
public record UserResponse(
    Long userId,
    String email
) {
    public static UserResponse from(User user) {
        return new UserResponse(user.getId(), user.getEmail());
    }
}
```

주의:

- DTO와 Entity 역할 혼동 금지.
- Response DTO에 Entity 내부 구조를 그대로 노출하지 않는다.
- Request DTO를 Entity로 바로 사용하지 않는다.
- DTO가 너무 많은 변환 책임을 가지면 Mapper 분리 검토.

---

### [FAQ]

Q. DTO는 왜 필요해?
A. API 입출력 구조와 Entity 내부 구조를 분리하기 위해 필요하다.

Q. DTO에 비즈니스 로직을 넣어도 돼?
A. 핵심 비즈니스 로직은 넣지 않는 것이 좋고 단순 변환 정도만 허용할 수 있다.

Q. DTO는 record로 만들어도 돼?
A. 단순 불변 데이터 전달 객체라면 record가 적합할 수 있다.

---

## 9.2 Entity Class Rules

### [개념]

Entity Class는 도메인 상태와 식별자를 가지는 객체다.

JPA Entity는 DB Table과 매핑되지만 단순 Table 구조만 표현하는 객체가 아니다.

---

### [핵심]

Entity 핵심:

- Entity
- Identity
- Field
- Domain State
- Domain Behavior
- Encapsulation
- Invariant
- JPA Entity
- Protected Constructor
- Meaningful Method

---

### [실무]

Entity 설계 기준:

- 식별자는 보통 Long ID 사용
- Field는 private
- 기본 생성자는 protected
- Setter 남용 지양
- 상태 변경은 의미 있는 Method로 표현
- 생성 규칙은 Constructor 또는 Factory Method 사용
- 연관관계 변경은 편의 Method 검토
- DB nullable과 Java Type 일치 확인

예:

```java
@Entity
public class User {
    @Id
    @GeneratedValue
    private Long userId;

    private String email;

    @Enumerated(EnumType.STRING)
    private UserStatus status;

    protected User() {
    }

    private User(String email) {
        this.email = Objects.requireNonNull(email, "email must not be null");
        this.status = UserStatus.ACTIVE;
    }

    public static User createActiveUser(String email) {
        return new User(email);
    }

    public void deactivate() {
        if (this.status == UserStatus.DELETED) {
            throw new IllegalStateException("deleted user cannot be deactivated");
        }

        this.status = UserStatus.INACTIVE;
    }
}
```

주의:

- Entity를 Response로 직접 반환하지 않는다.
- 모든 Field Setter 생성 지양.
- JPA 프록시와 기본 생성자 요구사항 고려.
- equals / hashCode는 식별자 생성 시점 문제를 검토.
- Entity에 외부 API 호출 로직을 넣지 않는다.

---

### [FAQ]

Q. Entity는 DB Table이랑 같은 거야?
A. JPA에서는 Table과 매핑되지만 도메인 상태와 행위도 표현할 수 있다.

Q. Entity에 Setter를 많이 둬도 돼?
A. 권장하지 않는다. 상태 변경 의미를 드러내는 Method를 제공하는 것이 좋다.

Q. Entity를 API Response로 바로 반환해도 돼?
A. 지양한다. Response DTO로 변환하는 것이 좋다.

---

## 9.3 Service Class Rules

### [개념]

Service Class는 비즈니스 흐름을 조정하고 Transaction 단위를 구성하는 Class다.

Service는 Controller와 Repository / Entity 사이의 Application Layer 역할을 한다.

---

### [핵심]

Service 핵심:

- Service
- Application Service
- Business Flow
- Transaction Boundary
- Repository Call
- Entity Method Call
- DTO Mapping
- Exception Handling
- Coordination

---

### [실무]

Service 설계 기준:

- 하나의 Method는 하나의 Use Case 중심
- Controller 로직을 Service로 이동
- Repository 조회 결과를 명확히 처리
- Entity 상태 변경 Method 호출
- Transaction 경계 명확화
- DTO 변환 위치 일관성 유지
- 외부 API 호출 실패 처리 검토
- Service가 너무 커지면 도메인 서비스 또는 별도 Component 분리

예:

```java
@Transactional
public void deactivateUser(Long userId) {
    User user = userRepository.findById(userId)
        .orElseThrow(() -> new UserNotFoundException(userId));

    user.deactivate();
}
```

주의:

- Service에 모든 도메인 규칙을 몰아넣지 않는다.
- Controller에 비즈니스 로직을 남기지 않는다.
- Entity를 단순 데이터 객체처럼 다루지 않는다.
- Service Method가 길어지면 Use Case 분리 검토.
- private Method가 과도하면 별도 Class 분리 검토.

---

### [FAQ]

Q. Service Class는 무엇을 담당해?
A. 비즈니스 흐름 조정, Transaction 경계, Repository 조회, Entity 상태 변경 호출을 담당한다.

Q. Service에 모든 비즈니스 로직을 넣어도 돼?
A. 아니다. 도메인 상태 변경 규칙은 Entity Method로 표현할 수 있다.

Q. Service Method는 어떻게 나누는 게 좋아?
A. 하나의 Use Case 또는 하나의 Application Flow 기준으로 나누는 것이 좋다.

---

# 10. Class and Method Anti Pattern

## 10.1 God Class Problem

### [개념]

God Class는 하나의 Class가 너무 많은 책임과 기능을 가지는 Anti Pattern이다.

God Class는 변경 비용을 높이고 테스트와 유지보수를 어렵게 만든다.

---

### [핵심]

God Class 징후:

- Class가 너무 김
- Method가 너무 많음
- Field가 너무 많음
- 여러 도메인 책임 혼합
- 변경 이유가 여러 개
- 이름이 Manager / Processor / Handler로 모호함
- private Method가 과도함
- 테스트 작성이 어려움

---

### [실무]

검토 Flow:

```text
Class 크기 확인
→ 책임 목록 작성
→ 변경 이유 확인
→ Layer 책임 혼합 확인
→ Method 그룹 확인
→ Field 응집도 확인
→ 분리 후보 도출
```

분리 후보:

```text
Validation → Validator
Mapping → Mapper
External API → Client
Complex Domain Rule → Domain Service
Creation Rule → Factory
Use Case → 별도 Service Method / Service Class
```

주의:

- 단순히 줄 수가 길다고 무조건 God Class는 아니다.
- 책임이 응집되어 있으면 큰 Class도 가능하다.
- 그러나 여러 이유로 변경된다면 분리해야 한다.
- RAG Retrieval에서도 God Class는 Chunk 품질을 떨어뜨린다.

---

### [FAQ]

Q. God Class는 뭐야?
A. 하나의 Class가 너무 많은 책임을 가져 변경과 테스트가 어려운 Anti Pattern이다.

Q. God Class는 어떻게 나눠?
A. Validation, Mapping, 외부 API, 생성 규칙, Use Case 등 책임 단위로 분리한다.

Q. Class가 길면 무조건 나쁜가?
A. 아니다. 책임이 응집되어 있으면 가능하지만 변경 이유가 여러 개면 문제다.

---

## 10.2 Long Method Problem

### [개념]

Long Method는 하나의 Method가 너무 많은 작업을 수행해 읽기 어렵고 테스트하기 어려운 상태다.

---

### [핵심]

Long Method 징후:

- 여러 단계 작업 혼합
- 조건문 중첩 과다
- 반복문 중첩 과다
- 변수 수 과다
- 주석 없이는 이해 어려움
- 테스트 포인트가 많음
- 예외 처리와 비즈니스 로직 혼합

---

### [실무]

분리 기준:

```text
Validation 분리
조회 로직 분리
상태 변경 분리
외부 API 호출 분리
DTO Mapping 분리
조건 판단 Method 분리
반복 처리 분리
```

나쁜 흐름:

```text
요청 검증
→ DB 조회
→ 권한 확인
→ 상태 변경
→ 외부 API 호출
→ 알림 발송
→ 응답 변환
```

개선 방향:

```text
Service Method는 흐름 유지
세부 규칙은 이름 있는 Method / Component로 분리
```

예:

```java
public void publishPost(Long postId) {
    Post post = getPostOrThrow(postId);
    validatePublishable(post);
    post.publish();
    notificationService.notifyPublished(post);
}
```

주의:

- private Method로 무조건 쪼개는 것이 답은 아니다.
- 분리 후 이름이 좋아야 한다.
- 서로 다른 책임이면 별도 Class가 더 적합할 수 있다.
- Transaction 경계 변경에 주의한다.

---

### [FAQ]

Q. Long Method는 왜 문제야?
A. 여러 책임이 섞여 읽기 어렵고 테스트와 변경이 어려워진다.

Q. Method는 몇 줄 이하여야 해?
A. 정해진 줄 수보다 하나의 책임을 명확히 수행하는지가 중요하다.

Q. private Method로 나누면 항상 좋아?
A. 아니다. 이름과 책임이 명확해야 하며 별도 Class 분리가 더 적합한 경우도 있다.

---

## 10.3 Data Class Problem

### [개념]

Data Class Problem은 Class가 Field와 Getter / Setter만 가지고 의미 있는 행위가 없는 상태를 말한다.

DTO에는 자연스러울 수 있지만 Entity나 Domain Object에서는 문제가 될 수 있다.

---

### [핵심]

Data Class 징후:

- Getter / Setter만 존재
- 상태 변경 규칙이 외부에 있음
- Service에서 Field 조작
- Entity가 DB Row처럼만 사용됨
- 도메인 Method 없음
- 불완전 상태 가능

---

### [실무]

검토 기준:

```text
이 Class가 DTO인가?
이 Class가 Entity인가?
상태 변경 규칙이 있는가?
Setter 대신 의미 있는 Method가 가능한가?
Service가 객체 상태를 직접 계산하고 있는가?
```

나쁜 예:

```java
user.setStatus(UserStatus.INACTIVE);
user.setDeletedAt(LocalDateTime.now());
```

좋은 예:

```java
user.deactivate();
```

Entity Method:

```java
public void deactivate() {
    if (this.status == UserStatus.DELETED) {
        throw new IllegalStateException("already deleted user");
    }

    this.status = UserStatus.INACTIVE;
    this.deactivatedAt = LocalDateTime.now();
}
```

주의:

- DTO는 Data Class 형태가 자연스러울 수 있다.
- Entity가 Data Class가 되면 도메인 규칙이 Service로 흩어진다.
- 단순 CRUD 프로젝트에서는 일부 허용될 수 있으나 규칙은 명확해야 한다.

---

### [FAQ]

Q. Getter / Setter만 있는 Class는 무조건 나빠?
A. DTO라면 괜찮을 수 있지만 Entity나 Domain Object라면 도메인 행위 부족을 검토해야 한다.

Q. Entity에 Method를 넣는 이유는?
A. 상태 변경 규칙을 Entity 내부에 모아 일관성을 유지하기 위해서다.

Q. Data Class 문제는 어떻게 개선해?
A. Setter를 의미 있는 상태 변경 Method로 바꾸고 규칙을 객체 내부로 이동한다.

---

# 11. Class Review Checklist

## 11.1 Class and Object Checklist

### [개념]

Class and Object Checklist는 Backend Agent / Review Agent가 Java Class 설계 품질을 검토하기 위한 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] Class 이름이 책임을 명확히 표현하는가?
- [ ] Class가 하나의 중심 책임을 가지는가?
- [ ] 변경 이유가 여러 개로 나뉘지 않는가?
- [ ] Field가 객체의 실제 상태를 표현하는가?
- [ ] Field 접근 제어자가 private 중심인가?
- [ ] 필수 Field가 생성 시점에 초기화되는가?
- [ ] null 가능성이 있는 Field가 명확히 관리되는가?
- [ ] Collection Field가 null이 아닌 빈 Collection으로 초기화되는가?
- [ ] Mutable Field 변경 규칙이 Method 안에 있는가?
- [ ] Setter를 과도하게 사용하지 않는가?
- [ ] Method 이름이 동작을 명확히 표현하는가?
- [ ] Method가 하나의 책임을 가지는가?
- [ ] Method Parameter가 과도하지 않은가?
- [ ] boolean flag Parameter를 남용하지 않는가?
- [ ] Return Type이 결과 없음을 명확히 표현하는가?
- [ ] null 반환 대신 Optional 또는 empty collection을 검토했는가?
- [ ] Side Effect가 Method 이름과 일치하는가?
- [ ] Constructor가 유효한 객체 생성을 보장하는가?
- [ ] JPA Entity 기본 생성자 접근 제어가 적절한가?
- [ ] Static Factory Method가 생성 의도를 명확히 표현하는가?
- [ ] Access Modifier가 최소 공개 원칙을 따르는가?
- [ ] DTO / Entity / Service 책임이 분리되어 있는가?
- [ ] God Class 징후가 없는가?
- [ ] Long Method 징후가 없는가?
- [ ] Data Class 문제가 Entity에 발생하지 않는가?
```

---

### [실무]

Review Flow:

```text
Class Name Review
→ Responsibility Review
→ Field Review
→ Constructor Review
→ Method Review
→ Access Modifier Review
→ DTO / Entity / Service Role Review
→ Anti Pattern Review
→ Refactoring Candidate 도출
```

---

### [FAQ]

Q. Class 검수에서 가장 먼저 볼 것은?
A. Class 이름과 책임이 일치하는지 먼저 보는 것이 좋다.

Q. Entity 검수에서 중요한 것은?
A. Field 캡슐화, 기본 생성자 접근 제한, Setter 남용 여부, 의미 있는 상태 변경 Method다.

Q. Method 검수에서 중요한 것은?
A. Method 이름, 하나의 책임, Parameter 수, Return Type, Side Effect 일치 여부다.

---

# 12. Backend Integration

## 12.1 Class Design to Spring Boot

### [개념]

Java Class, Object, Method, Constructor 설계는 Spring Boot Layered Architecture의 기반이다.

Spring Boot 코드 품질은 각 Class의 책임 분리와 Method 설계 품질에 크게 좌우된다.

---

### [핵심]

Spring Boot 연결 기준:

```text
Controller Class
→ Request / Response 책임

Service Class
→ Use Case 흐름 조정

Entity Class
→ 도메인 상태와 행위

DTO Class
→ Layer 간 데이터 전달

Repository Interface
→ 데이터 접근 추상화

Config Class
→ 설정 책임

Client Class
→ 외부 시스템 통신
```

---

### [실무]

Spring Boot 코드 생성 / 검토 기준:

```text
User Request
→ Controller Method
→ Request DTO Validation
→ Service Method
→ Repository 조회
→ Entity Method 호출
→ DTO Mapping
→ Response 반환
```

좋은 흐름:

```java
@Transactional
public void changeEmail(Long userId, String newEmail) {
    User user = userRepository.findById(userId)
        .orElseThrow(() -> new UserNotFoundException(userId));

    user.changeEmail(newEmail);
}
```

검토 포인트:

- Controller가 비즈니스 로직을 가지지 않는가?
- Service Method가 Use Case 중심인가?
- Entity에 의미 있는 상태 변경 Method가 있는가?
- DTO가 Entity 노출을 막는가?
- Constructor가 필수 값 누락을 막는가?
- Method Return Type이 명확한가?
- 예외가 명확한 도메인 상황을 표현하는가?

---

### [FAQ]

Q. Java Class 설계가 Spring Boot에 왜 중요해?
A. Spring Boot 구조도 Class 책임과 Method 협력으로 구성되기 때문이다.

Q. Controller Class는 어디까지 담당해?
A. HTTP 요청 수신, 입력 검증 연결, Service 호출, 응답 반환 정도를 담당한다.

Q. Entity Method와 Service Method는 어떻게 나눠?
A. Service는 흐름을 조정하고 Entity는 자신의 상태 변경 규칙을 담당한다.

---

# Retrieval Queries

### [FAQ]

Q. Java Class는 뭐야?
A. Java에서 상태와 행위를 묶어 객체를 만들기 위한 설계 단위다.

Q. Class와 Object 차이는?
A. Class는 설계도이고 Object는 Class를 기반으로 생성된 실제 인스턴스다.

Q. Java Class는 어떻게 나눠?
A. 책임 기준으로 나눈다. 하나의 Class가 너무 많은 이유로 변경된다면 분리 후보로 본다.

Q. Class 이름은 어떻게 지어?
A. 역할과 책임이 드러나도록 명확하게 작성한다.

Q. Manager라는 Class 이름은 써도 돼?
A. 무조건 금지는 아니지만 책임이 모호해지기 쉬워 더 구체적인 이름을 우선 검토한다.

Q. Object State는 뭐야?
A. 객체가 현재 가지고 있는 Field 값들의 상태를 의미한다.

Q. Object Behavior는 뭐야?
A. 객체가 수행할 수 있는 행위이며 Java에서는 Method로 표현한다.

Q. Field는 왜 private으로 둬?
A. 객체 상태를 보호하고 변경 규칙을 Method 안에 모으기 위해서다.

Q. Field 초기화는 왜 중요해?
A. 불완전 객체 생성을 막고 NullPointerException 위험을 줄이기 위해서다.

Q. Collection Field는 null로 둬도 돼?
A. 대부분 빈 Collection으로 초기화하는 것이 좋다.

Q. Setter를 많이 써도 돼?
A. 권장하지 않는다. 비즈니스 상태 변경은 의미 있는 Method로 표현하는 것이 좋다.

Q. Method는 어떻게 설계해?
A. 하나의 Method는 하나의 책임을 가지며 이름은 동작을 명확히 표현해야 한다.

Q. Method 이름은 어떻게 지어?
A. 동작과 의도가 드러나도록 동사 중심으로 작성한다.

Q. boolean Method 이름은 어떻게 지어?
A. is, has, can, should 같은 접두어를 사용하면 좋다.

Q. find와 get 차이는?
A. find는 없을 수 있음을 암시하고 get은 존재한다고 기대하는 느낌이 강하다.

Q. process라는 Method 이름은 왜 안 좋아?
A. 어떤 작업을 하는지 구체적으로 드러나지 않아 책임이 모호하다.

Q. Method Parameter가 많으면 어떻게 해?
A. Request DTO, Command 객체, Value Object로 묶는 것을 검토한다.

Q. boolean Parameter는 왜 조심해야 해?
A. 호출 코드에서 true / false의 의미가 명확하지 않을 수 있기 때문이다.

Q. Method에서 null을 반환해도 돼?
A. 가능하지만 권장하지 않는다. Optional이나 empty collection을 검토하는 것이 좋다.

Q. List 결과가 없으면 null을 반환해?
A. 보통 empty List를 반환하는 것이 좋다.

Q. Optional은 언제 반환해?
A. 단일 결과가 없을 수 있음을 호출자에게 명시할 때 사용한다.

Q. Side Effect는 뭐야?
A. Method가 반환값 외에 객체 상태, DB, 외부 시스템 등에 변화를 만드는 효과다.

Q. Side Effect가 있는 Method는 어떻게 이름 지어?
A. 상태 변경이나 외부 효과가 드러나도록 이름을 지어야 한다.

Q. Constructor는 뭐야?
A. 객체 생성 시 호출되어 필수 값을 초기화하고 유효한 상태를 만드는 특별한 Method 형태다.

Q. Constructor에서 검증을 해도 돼?
A. 필수 값과 불변 조건 검증은 Constructor에서 하는 것이 좋다.

Q. 기본 생성자는 항상 필요해?
A. 아니다. 일반 객체는 필수 값을 받는 생성자가 더 안전하다.

Q. JPA Entity에는 기본 생성자가 필요해?
A. 필요하다. 보통 protected no-args Constructor를 둔다.

Q. Constructor Overloading은 언제 써?
A. 필수 값과 기본값 조합을 명확히 표현할 수 있을 때 사용한다.

Q. Constructor가 너무 많으면 어떻게 해?
A. Static Factory Method나 Builder Pattern을 검토한다.

Q. Static Factory Method는 왜 써?
A. 객체 생성 의도와 규칙을 Method 이름으로 명확히 표현할 수 있기 때문이다.

Q. of와 from 차이는?
A. of는 값을 조합해 생성하는 느낌이고 from은 다른 객체나 타입에서 변환하는 느낌이다.

Q. Access Modifier는 어떻게 정해?
A. 가능한 좁게 잡고 필요한 경우에만 넓힌다.

Q. public Method는 많이 열어도 돼?
A. 필요한 것만 public으로 열고 내부 구현은 숨기는 것이 좋다.

Q. Package는 왜 필요해?
A. 관련 Class를 묶고 이름 충돌을 방지하며 구조를 표현하기 위해 필요하다.

Q. DTO는 왜 필요해?
A. API 입출력 구조와 Entity 내부 구조를 분리하기 위해 필요하다.

Q. DTO에 비즈니스 로직을 넣어도 돼?
A. 핵심 비즈니스 로직은 넣지 않는 것이 좋고 단순 변환 정도만 허용할 수 있다.

Q. Entity는 DB Table이랑 같은 거야?
A. JPA에서는 Table과 매핑되지만 도메인 상태와 행위도 표현할 수 있다.

Q. Entity에 Setter를 많이 둬도 돼?
A. 권장하지 않는다. 상태 변경 의미를 드러내는 Method를 제공하는 것이 좋다.

Q. Service Class는 무엇을 담당해?
A. 비즈니스 흐름 조정, Transaction 경계, Repository 조회, Entity 상태 변경 호출을 담당한다.

Q. Entity Method와 Service Method는 어떻게 나눠?
A. Service는 흐름을 조정하고 Entity는 자신의 상태 변경 규칙을 담당한다.

Q. God Class는 뭐야?
A. 하나의 Class가 너무 많은 책임을 가져 변경과 테스트가 어려운 Anti Pattern이다.

Q. Long Method는 왜 문제야?
A. 여러 책임이 섞여 읽기 어렵고 테스트와 변경이 어려워진다.

Q. Data Class 문제는 뭐야?
A. Class가 Field와 Getter / Setter만 있고 의미 있는 행위가 없는 상태를 말한다.

Q. Class 검수는 어떤 순서로 해?
A. Class 이름, 책임, Field, Constructor, Method, Access Modifier, 역할 분리, Anti Pattern 순서로 검토한다.

Q. Java Part02 다음 문서는 뭐야?
A. Java Part03 — OOP Core 문서로 이어지는 것이 좋다.
