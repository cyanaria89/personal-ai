# Java Part08 — Backend Code Review & Anti Pattern

---

# 1. Java Backend Code Review Overview

## 1.1 Code Review Purpose

### [개념]

Java Backend Code Review는 Java 문법 오류만 찾는 작업이 아니다.

목적은 Backend Agent / Review Agent가 Java 기반 Spring Boot 코드에서 객체 책임, Method 책임, Type Safety, Null Safety, Exception Handling, Collection 선택, Anti Pattern을 검토하는 것이다.

Code Review는 다음 작업을 지원한다.

```text
Java Code
→ Responsibility Review
→ Method Review
→ Type Safety Review
→ Null Safety Review
→ Exception Review
→ Collection Review
→ OOP Review
→ Anti Pattern Detection
→ Refactoring Suggestion
```

---

### [핵심]

Java Backend Code Review 핵심 기준:

- Class 책임 명확성
- Method 단일 책임
- Field 접근 제어
- Setter 남용 여부
- Encapsulation 적용 여부
- Inheritance / Composition 판단
- Interface / Abstract Class 선택
- Collection 선택 적절성
- Generic Type Safety
- Optional 사용 적절성
- Exception Handling 명확성
- Null Safety 확보
- Stream / Lambda 가독성
- Static / Final 사용 적절성
- DTO / Entity 역할 분리
- Backend Anti Pattern 탐지

---

### [실무]

실무 리뷰 순서:

```text
1. 코드가 어떤 Layer인지 확인
2. Class 책임 확인
3. Method 책임 확인
4. 입력값 검증 확인
5. 반환 타입 확인
6. Null 가능성 확인
7. Optional 처리 확인
8. Exception 처리 확인
9. Collection 선택 확인
10. Generic 사용 확인
11. 객체지향 설계 확인
12. Anti Pattern 확인
13. 리팩터링 방향 제안
```

Layer별 핵심 관점:

| Layer      | Review Point                                  |
| ---------- | --------------------------------------------- |
| Controller | DTO 사용, 비즈니스 로직 과다 여부             |
| Service    | Method 책임, Transaction 경계, Exception 처리 |
| Entity     | Encapsulation, Setter 남용, 상태 변경 Method  |
| Repository | Optional 처리, Collection 반환 정책           |
| DTO        | Validation, Entity 노출 여부, 불변성          |
| Utility    | static 남용 여부, 순수 함수 여부              |

---

### [FAQ]

Q. Java Code Review는 문법 오류만 찾는 거야?

A.
아니다. 객체 책임, Method 책임, Null Safety, Type Safety, Exception Handling, Anti Pattern까지 함께 검토한다.

Q. Backend Code Review에서 가장 먼저 볼 것은 뭐야?

A.
해당 Class가 어떤 Layer에 속하는지와 책임이 명확한지를 먼저 확인한다.

Q. Java Review Agent가 가장 자주 찾아야 할 문제는 뭐야?

A.
Setter 남용, null 처리 누락, Optional.get 직접 호출, Exception 무시, Method 과대화, DTO와 Entity 혼동이다.

---

# 2. Responsibility Review

## 2.1 Class Responsibility Review

### [개념]

Class Responsibility Review는 하나의 Class가 하나의 명확한 책임을 가지고 있는지 확인하는 작업이다.

Class는 변경 이유가 너무 많아지면 유지보수성이 떨어진다.

---

### [핵심]

검토 기준:

- Class 이름이 책임을 설명하는가?
- Field와 Method가 같은 목적을 향하는가?
- Controller에 Service 로직이 들어가 있지 않은가?
- Service가 너무 많은 도메인을 처리하지 않는가?
- Utility Class가 비즈니스 로직 저장소가 되지 않았는가?
- Entity가 단순 데이터 덩어리가 되지 않았는가?
- DTO가 비즈니스 판단을 하지 않는가?

---

### [실무]

나쁜 예:

```java
public class UserService {
    public void registerUser(UserRequest request) { }
    public void sendEmail(String email) { }
    public void uploadProfileImage(MultipartFile file) { }
    public void generateMonthlyReport() { }
}
```

문제:

- User 등록
- Email 발송
- File 업로드
- Report 생성

서로 다른 책임이 한 Service에 섞여 있다.

좋은 방향:

```text
UserService
→ User 등록 / 수정 / 조회

EmailService
→ Email 발송

FileStorageService
→ File 저장

ReportService
→ Report 생성
```

---

### [Checklist]

Class Responsibility Checklist:

```md
- [ ] Class 이름이 책임을 명확히 표현하는가?
- [ ] 하나의 Class가 여러 도메인 기능을 처리하지 않는가?
- [ ] Controller에 비즈니스 로직이 들어가 있지 않은가?
- [ ] Service가 외부 API, 파일, 메일, 리포트를 모두 직접 처리하지 않는가?
- [ ] Entity가 의미 있는 상태 변경 Method를 가지는가?
- [ ] DTO가 Entity 책임을 침범하지 않는가?
- [ ] Utility Class에 도메인 로직이 몰려 있지 않은가?
```

---

### [FAQ]

Q. Class가 너무 많은 책임을 가진다는 건 뭐야?

A.
하나의 Class가 여러 이유로 자주 변경된다면 책임이 과도하게 섞여 있다는 뜻이다.

Q. Service Class가 커지면 어떻게 해?

A.
도메인 책임, 외부 연동 책임, 파일 처리 책임, 알림 책임 등을 별도 Service로 분리한다.

---

## 2.2 Method Responsibility Review

### [개념]

Method Responsibility Review는 하나의 Method가 하나의 작업만 수행하는지 확인하는 작업이다.

Method가 입력 검증, 조회, 계산, 저장, 알림, 응답 변환을 모두 처리하면 이해와 테스트가 어려워진다.

---

### [핵심]

검토 기준:

- Method 이름이 동작을 명확히 표현하는가?
- 하나의 Method가 하나의 책임을 가지는가?
- Parameter가 과도하게 많지 않은가?
- boolean flag parameter로 여러 흐름을 처리하지 않는가?
- return null을 사용하지 않는가?
- 예외 발생 조건이 명확한가?
- Method 내부 중첩 if가 과도하지 않은가?
- 테스트하기 쉬운 단위인가?

---

### [실무]

나쁜 예:

```java
public UserResponse process(UserRequest request, boolean sendEmail) {
    if (request == null) {
        return null;
    }

    User user = new User(request.getEmail(), request.getName());
    userRepository.save(user);

    if (sendEmail) {
        emailService.sendWelcomeEmail(user.getEmail());
    }

    return UserResponse.from(user);
}
```

문제:

- Method 이름이 모호함
- null 반환
- 사용자 생성과 이메일 발송 책임 혼합
- boolean flag parameter로 흐름 분기

개선 예:

```java
public UserResponse register(UserRegisterRequest request) {
    validateRegisterRequest(request);

    User user = createUser(request);
    User savedUser = userRepository.save(user);

    emailService.sendWelcomeEmail(savedUser.getEmail());

    return UserResponse.from(savedUser);
}
```

---

### [Best Practice]

Method 분리 기준:

```text
검증 로직 → validateXxx()
생성 로직 → createXxx()
조회 로직 → findXxxOrThrow()
상태 변경 → changeXxx()
응답 변환 → XxxResponse.from()
```

권장 Method 이름:

```text
findUserOrThrow
validateDuplicateEmail
createPost
publishPost
cancelOrder
calculateTotalPrice
```

---

### [FAQ]

Q. Method가 길면 무조건 나눠야 해?

A.
줄 수보다 책임이 섞였는지가 중요하다. 여러 작업이 섞이면 Method 분리를 검토한다.

Q. boolean parameter가 왜 문제야?

A.
하나의 Method가 여러 동작을 하게 만들고 호출부만 봐서는 의미를 알기 어렵게 만든다.

---

# 3. Layer Review

## 3.1 Controller Review

### [개념]

Controller는 HTTP 요청을 받고 DTO로 변환한 뒤 Service에 작업을 위임하는 Layer다.

Controller에 비즈니스 로직이 많으면 테스트, 재사용, 유지보수가 어려워진다.

---

### [핵심]

Controller Review 기준:

- Request DTO를 사용하는가?
- Response DTO를 반환하는가?
- Entity를 직접 반환하지 않는가?
- 비즈니스 로직을 직접 처리하지 않는가?
- Repository를 직접 호출하지 않는가?
- 예외 처리를 Controller마다 반복하지 않는가?
- 인증 사용자 정보 처리 범위가 명확한가?
- Service 호출 후 응답 변환이 명확한가?

---

### [실무]

나쁜 예:

```java
@GetMapping("/users/{id}")
public User getUser(@PathVariable Long id) {
    return userRepository.findById(id).get();
}
```

문제:

- Controller에서 Repository 직접 호출
- Optional.get 직접 호출
- Entity 직접 반환
- 예외 처리 부재

좋은 예:

```java
@GetMapping("/users/{id}")
public ApiResponse<UserResponse> getUser(@PathVariable Long id) {
    UserResponse response = userService.getUser(id);
    return ApiResponse.success(response);
}
```

Service:

```java
public UserResponse getUser(Long userId) {
    User user = userRepository.findById(userId)
        .orElseThrow(() -> new UserNotFoundException(userId));

    return UserResponse.from(user);
}
```

---

### [Checklist]

Controller Review Checklist:

```md
- [ ] Request DTO를 사용하는가?
- [ ] Response DTO를 반환하는가?
- [ ] Entity를 직접 반환하지 않는가?
- [ ] Repository를 직접 호출하지 않는가?
- [ ] 비즈니스 규칙을 직접 처리하지 않는가?
- [ ] Optional.get을 직접 호출하지 않는가?
- [ ] 반복 try-catch가 없는가?
- [ ] 인증 사용자 정보가 필요한 경우 명확히 전달하는가?
```

---

### [FAQ]

Q. Controller에서 Repository를 바로 호출해도 돼?

A.
권장하지 않는다. 비즈니스 로직과 예외 처리는 Service Layer에서 처리하는 것이 좋다.

Q. Controller에서 Entity를 반환해도 돼?

A.
권장하지 않는다. Entity 내부 구조가 API에 노출되므로 Response DTO를 사용하는 것이 좋다.

---

## 3.2 Service Review

### [개념]

Service는 애플리케이션 비즈니스 흐름을 조합하는 Layer다.

Service는 Entity 조회, 검증, 상태 변경, 저장, 외부 연동 호출을 조율하지만 모든 세부 책임을 혼자 가져서는 안 된다.

---

### [핵심]

Service Review 기준:

- Method 책임이 명확한가?
- Transaction 경계가 적절한가?
- Repository 조회 결과를 명확히 처리하는가?
- Optional.get 직접 호출을 피하는가?
- Entity 상태 변경을 의미 있는 Method로 수행하는가?
- 예외 타입이 명확한가?
- Controller DTO와 Entity를 혼동하지 않는가?
- 외부 API / 파일 / 메일 책임을 분리하는가?
- 중복 로직을 private Method 또는 별도 Component로 분리하는가?

---

### [실무]

나쁜 예:

```java
public void updateNickname(Long userId, String nickname) {
    User user = userRepository.findById(userId).get();
    user.setNickname(nickname);
    userRepository.save(user);
}
```

문제:

- Optional.get 직접 호출
- Setter 직접 사용
- 검증 없음
- 상태 변경 의미 불명확

좋은 예:

```java
public void updateNickname(Long userId, String nickname) {
    User user = findUserOrThrow(userId);
    user.changeNickname(nickname);
}

private User findUserOrThrow(Long userId) {
    return userRepository.findById(userId)
        .orElseThrow(() -> new UserNotFoundException(userId));
}
```

Entity:

```java
public void changeNickname(String nickname) {
    if (nickname == null || nickname.isBlank()) {
        throw new IllegalArgumentException("nickname must not be blank");
    }

    this.nickname = nickname;
}
```

---

### [주의]

Service에서 주의할 Anti Pattern:

- God Service
- Transaction Script 과대화
- Repository 결과 Optional.get 직접 호출
- 모든 검증을 Controller에 위임
- Entity를 단순 Setter 대상으로 사용
- 외부 API 호출과 DB 변경 책임 혼합
- 복잡한 if-else 정책 분기 누적
- Duplicate Logic

---

### [FAQ]

Q. Service에서 Entity Setter를 직접 호출해도 돼?

A.
단순 값 변경은 가능하지만 비즈니스 의미가 있는 상태 변경은 Entity Method로 표현하는 것이 좋다.

Q. Service가 너무 커지면 어떻게 해?

A.
도메인 책임별 Service 분리, 정책 객체 분리, 외부 연동 Component 분리를 검토한다.

---

## 3.3 Entity Review

### [개념]

Entity는 DB 테이블 매핑 객체이면서 도메인 상태와 상태 변경 규칙을 담을 수 있는 객체다.

Entity가 모든 Field Setter만 가진 데이터 덩어리가 되면 Encapsulation이 약해진다.

---

### [핵심]

Entity Review 기준:

- Field가 private인가?
- Setter가 과도하지 않은가?
- 생성 시 필수 값 검증이 있는가?
- 상태 변경 Method가 의미를 가지는가?
- Collection Field를 외부에서 직접 수정하지 않는가?
- equals / hashCode 기준이 위험하지 않은가?
- Entity와 DTO 변환 책임이 과도하게 섞이지 않았는가?
- JPA 요구사항과 객체지향 설계가 균형을 이루는가?

---

### [실무]

나쁜 예:

```java
user.setPoint(user.getPoint() + 100);
user.setStatus(UserStatus.ACTIVE);
```

문제:

- 상태 변경 규칙이 외부에 흩어짐
- Point 증가 검증 없음
- Status 전이 규칙 없음

좋은 예:

```java
user.addPoint(100);
user.activate();
```

Entity:

```java
public void addPoint(int amount) {
    if (amount <= 0) {
        throw new IllegalArgumentException("amount must be positive");
    }

    this.point += amount;
}

public void activate() {
    if (this.status == UserStatus.DELETED) {
        throw new IllegalStateException("deleted user cannot be activated");
    }

    this.status = UserStatus.ACTIVE;
}
```

---

### [Checklist]

Entity Review Checklist:

```md
- [ ] Field가 private인가?
- [ ] Setter가 무분별하게 열려 있지 않은가?
- [ ] 생성자 또는 Factory Method에서 필수 값 검증을 하는가?
- [ ] 상태 변경 Method 이름이 비즈니스 의미를 표현하는가?
- [ ] Collection Field를 직접 노출하지 않는가?
- [ ] 외부에서 상태 조합을 직접 만들지 않는가?
- [ ] Entity를 API Response로 직접 반환하지 않는가?
- [ ] Optional을 Entity Field로 사용하지 않는가?
```

---

### [FAQ]

Q. Entity에 Setter가 있으면 무조건 나쁜가?

A.
무조건은 아니지만 비즈니스 상태 변경은 의미 있는 Method로 감싸는 것이 좋다.

Q. Entity는 단순히 DB 데이터만 담으면 돼?

A.
단순 CRUD에서는 가능하지만 도메인 규칙이 있는 경우 상태 변경 Method를 Entity에 둘 수 있다.

---

## 3.4 DTO Review

### [개념]

DTO는 Layer 간 데이터 전달을 위한 객체다.

DTO는 Entity 내부 구조를 API에 직접 노출하지 않고 요청과 응답 형식을 안정적으로 관리하기 위해 사용한다.

---

### [핵심]

DTO Review 기준:

- Request DTO와 Response DTO가 분리되어 있는가?
- Entity를 직접 노출하지 않는가?
- 입력값 Validation 위치가 명확한가?
- DTO에 비즈니스 로직이 과도하지 않은가?
- Response DTO는 필요한 Field만 포함하는가?
- 내부 식별자나 민감정보를 노출하지 않는가?
- 단순 전달 객체는 record 사용을 검토했는가?

---

### [실무]

나쁜 예:

```java
@PostMapping("/users")
public User createUser(@RequestBody User user) {
    return userService.create(user);
}
```

문제:

- Entity를 Request로 직접 사용
- Entity를 Response로 직접 반환
- API 스펙과 DB 구조가 강하게 결합

좋은 예:

```java
@PostMapping("/users")
public ApiResponse<UserResponse> createUser(
        @RequestBody UserCreateRequest request
) {
    return ApiResponse.success(userService.createUser(request));
}
```

DTO:

```java
public record UserCreateRequest(
    String email,
    String nickname
) {
}
```

```java
public record UserResponse(
    Long userId,
    String email,
    String nickname
) {
    public static UserResponse from(User user) {
        return new UserResponse(
            user.getId(),
            user.getEmail(),
            user.getNickname()
        );
    }
}
```

---

### [주의]

DTO Anti Pattern:

- Entity를 Request Body로 직접 받음
- Entity를 Response로 직접 반환
- Request DTO와 Response DTO를 하나로 재사용
- DTO에 Repository 의존성 주입
- DTO에서 비즈니스 상태 변경 수행
- 민감정보 Field 포함
- 사용하지 않는 Field 과다 포함

---

### [FAQ]

Q. DTO와 Entity를 왜 분리해야 해?

A.
API 스펙과 DB 구조의 결합을 줄이고 민감정보 노출과 의도치 않은 변경을 방지하기 위해서다.

Q. Request DTO와 Response DTO를 같은 Class로 써도 돼?

A.
간단한 경우 가능하지만 입력과 출력 요구사항이 달라질 수 있으므로 분리하는 것이 안전하다.

---

# 4. Type Safety Review

## 4.1 Generic Review

### [개념]

Type Safety Review는 컴파일 시점에 타입 오류를 잡을 수 있도록 Generic과 명확한 타입을 사용하는지 확인하는 작업이다.

Raw Type과 Object 반환은 Runtime ClassCastException 위험을 높인다.

---

### [핵심]

검토 대상:

- Raw Type 사용 여부
- Object 반환 남용 여부
- Generic Type 누락 여부
- 강제 Casting 필요 여부
- Collection 내부 타입 혼합 여부
- API Response Wrapper Generic 사용 여부
- Repository / Service 반환 타입 명확성

---

### [실무]

나쁜 예:

```java
public List findAllUsers() {
    return userRepository.findAll();
}
```

문제:

- Raw Type
- 호출부에서 타입 안정성 약화

좋은 예:

```java
public List<UserResponse> findAllUsers() {
    return userRepository.findAll().stream()
        .map(UserResponse::from)
        .toList();
}
```

나쁜 예:

```java
public Object getResult(String type) {
    if ("user".equals(type)) {
        return new UserResponse();
    }

    return new PostResponse();
}
```

개선 방향:

```text
반환 타입 분리
→ getUserResult()
→ getPostResult()

또는 공통 Interface / Generic Wrapper 검토
```

---

### [Checklist]

Type Safety Checklist:

```md
- [ ] Raw Type을 사용하지 않는가?
- [ ] Object 반환을 남용하지 않는가?
- [ ] 강제 Casting이 반복되지 않는가?
- [ ] Collection Generic Type이 명확한가?
- [ ] API 응답 타입이 Generic으로 표현되는가?
- [ ] Optional, List, Map의 내부 타입이 명확한가?
- [ ] instanceof 분기 남용이 없는가?
```

---

### [FAQ]

Q. Raw Type은 왜 문제야?

A.
컴파일 시점 타입 검사가 약해져 Runtime ClassCastException 위험이 커진다.

Q. Object 반환은 왜 피해야 해?

A.
호출부에서 타입을 알기 어렵고 강제 Casting이 필요해 타입 안정성이 떨어진다.

---

## 4.2 Primitive vs Wrapper Review

### [개념]

Primitive Type과 Wrapper Type 선택은 null 가능성과 DB 매핑에 영향을 준다.

Backend 코드에서는 Entity ID, nullable DB Column, 요청 값 검증에서 Wrapper Type 사용 여부를 신중히 판단해야 한다.

---

### [핵심]

선택 기준:

| 상황                    | 권장 타입    |
| ----------------------- | ------------ |
| null 불가능한 단순 계산 | primitive    |
| Entity ID               | Long         |
| DB nullable Column      | Wrapper Type |
| Request optional field  | Wrapper Type |
| Boolean nullable 상태   | Boolean      |
| 필수 boolean flag       | boolean      |
| 금액 / 정밀 계산        | BigDecimal   |

---

### [실무]

주의 예:

```java
private int discountRate;
```

문제 가능성:

- 값이 없음을 0과 구분할 수 없음

개선 예:

```java
private Integer discountRate;
```

단, 필수 값이면 생성자나 Validation으로 null을 막는다.

```java
public Coupon(Integer discountRate) {
    if (discountRate == null) {
        throw new IllegalArgumentException("discountRate must not be null");
    }

    this.discountRate = discountRate;
}
```

---

### [FAQ]

Q. Entity ID는 왜 Long을 많이 써?

A.
DB BIGINT와 매핑하기 쉽고 데이터 증가에도 비교적 안전하기 때문이다.

Q. int와 Integer 중 무엇을 써야 해?

A.
null이 필요 없고 단순 계산이면 int, null 가능성이 있거나 DB nullable 값이면 Integer를 검토한다.

---

# 5. Null Safety Review

## 5.1 Null Return Review

### [개념]

Null Return Review는 Method가 null을 반환해 호출부에 NullPointerException 위험을 전파하지 않는지 확인하는 작업이다.

Backend 코드에서는 null 반환보다 Optional, empty collection, 예외 변환, 기본값 반환을 우선 검토한다.

---

### [핵심]

검토 대상:

- return null 사용 여부
- Collection null 반환 여부
- Repository 결과 처리 여부
- DTO Field null 가능성
- Method Chain 중간 null 가능성
- null check 위치
- guard clause 사용 여부

---

### [실무]

나쁜 예:

```java
public List<PostResponse> getPosts() {
    List<Post> posts = postRepository.findAll();

    if (posts.isEmpty()) {
        return null;
    }

    return posts.stream()
        .map(PostResponse::from)
        .toList();
}
```

좋은 예:

```java
public List<PostResponse> getPosts() {
    return postRepository.findAll().stream()
        .map(PostResponse::from)
        .toList();
}
```

나쁜 예:

```java
public User findUser(Long userId) {
    return userRepository.findById(userId).orElse(null);
}
```

좋은 예:

```java
public User findUserOrThrow(Long userId) {
    return userRepository.findById(userId)
        .orElseThrow(() -> new UserNotFoundException(userId));
}
```

---

### [Best Practice]

Null Safety 기본 정책:

```text
단건 필수 조회 실패 → Custom Exception
단건 선택 조회 실패 → Optional 반환
목록 조회 결과 없음 → empty list
입력 필수 값 누락 → Validation Exception
내부 필수 값 누락 → IllegalArgumentException
```

---

### [FAQ]

Q. return null은 무조건 나빠?

A.
무조건은 아니지만 호출부 NPE 위험이 커지므로 Optional, empty collection, 예외 변환을 우선 검토한다.

Q. 목록 조회 결과가 없으면 null을 반환해야 해?

A.
대부분 empty list를 반환하는 것이 좋다.

---

## 5.2 Optional Review

### [개념]

Optional Review는 Optional을 값 부재 표현에 적절히 사용하는지 확인하는 작업이다.

Optional은 주로 반환 타입에 사용하며 Field, Parameter, Entity 속성으로 사용하는 것은 권장하지 않는다.

---

### [핵심]

검토 기준:

- Optional.get 직접 호출 여부
- Optional 반환 후 즉시 null처럼 처리하는지
- Optional Field 사용 여부
- Optional Parameter 사용 여부
- orElse와 orElseGet 선택 적절성
- orElseThrow로 예외 변환 여부
- Repository Optional 결과 처리 여부

---

### [실무]

나쁜 예:

```java
User user = userRepository.findById(userId).get();
```

좋은 예:

```java
User user = userRepository.findById(userId)
    .orElseThrow(() -> new UserNotFoundException(userId));
```

나쁜 예:

```java
public void update(Optional<String> nickname) {
    if (nickname.isPresent()) {
        this.nickname = nickname.get();
    }
}
```

개선 예:

```java
public void updateNickname(String nickname) {
    if (nickname == null || nickname.isBlank()) {
        throw new IllegalArgumentException("nickname must not be blank");
    }

    this.nickname = nickname;
}
```

---

### [주의]

Optional 오남용:

```text
Optional.get 직접 호출
Optional을 Entity Field로 사용
Optional을 Method Parameter로 사용
Optional 내부에 null 삽입
Optional을 단순 null check보다 복잡하게 사용
Optional 반환 후 다시 null 반환
```

---

### [FAQ]

Q. Optional.get을 바로 쓰면 왜 안 좋아?

A.
값이 없을 때 NoSuchElementException이 발생하므로 orElseThrow, orElse, orElseGet을 사용하는 것이 안전하다.

Q. Optional을 Parameter로 받으면 안 돼?

A.
권장하지 않는다. 호출부가 더 복잡해지고 API 의도가 흐려질 수 있다.

---

# 6. Exception Handling Review

## 6.1 Exception Handling Review Flow

### [개념]

Exception Handling Review는 예외가 발생했을 때 원인이 명확히 표현되고 적절한 계층에서 처리되는지 확인하는 작업이다.

Backend에서는 Service / Domain에서 예외를 발생시키고 GlobalExceptionHandler에서 HTTP 응답으로 변환하는 구조가 일반적이다.

---

### [핵심]

검토 기준:

- catch 후 빈 블록이 없는가?
- Exception을 무시하지 않는가?
- RuntimeException만 무분별하게 던지지 않는가?
- 비즈니스 오류에 Custom Exception을 사용하는가?
- 메시지가 원인 파악에 충분한가?
- 민감정보를 예외 메시지에 포함하지 않는가?
- Controller마다 try-catch를 반복하지 않는가?
- GlobalExceptionHandler와 연결 가능한가?

---

### [실무]

나쁜 예:

```java
try {
    paymentService.pay(orderId);
} catch (Exception e) {
}
```

문제:

- 예외 무시
- 실패 원인 손실
- 후속 로직이 성공으로 오해할 수 있음

개선 예:

```java
try {
    paymentService.pay(orderId);
} catch (PaymentException e) {
    log.warn("Payment failed. orderId={}", orderId, e);
    throw e;
}
```

Custom Exception 예:

```java
public class OrderNotFoundException extends RuntimeException {
    public OrderNotFoundException(Long orderId) {
        super("Order not found. orderId=" + orderId);
    }
}
```

---

### [Flow]

Exception Review Flow:

```text
Exception 발생 위치 확인
→ 복구 가능한 예외인지 판단
→ 현재 계층에서 처리할지 판단
→ 비즈니스 의미가 있는지 판단
→ Custom Exception 필요 여부 확인
→ 로그 필요 여부 확인
→ 응답 변환 위치 확인
```

---

### [FAQ]

Q. catch 하고 아무것도 안 하면 왜 문제야?

A.
오류 원인이 사라지지 않고 실패 사실이 숨겨져 디버깅과 장애 대응이 어려워진다.

Q. 모든 예외를 Custom Exception으로 만들어야 해?

A.
아니다. 비즈니스 의미가 있거나 공통 응답 처리가 필요한 예외에 우선 적용한다.

---

## 6.2 Exception Message Review

### [개념]

Exception Message Review는 예외 메시지가 원인 파악에 충분하면서도 민감정보를 노출하지 않는지 확인하는 작업이다.

---

### [핵심]

좋은 메시지 조건:

- 어떤 리소스가 문제인지 명확함
- 어떤 값 때문에 실패했는지 식별 가능
- 민감정보 미포함
- 로그 검색이 쉬움
- 사용자 응답 메시지와 내부 로그 메시지 분리 가능

---

### [실무]

나쁜 예:

```java
throw new RuntimeException("error");
```

문제:

- 원인 파악 불가

좋은 예:

```java
throw new UserNotFoundException(userId);
```

나쁜 예:

```java
throw new LoginFailedException("password=" + rawPassword);
```

문제:

- 민감정보 노출

좋은 예:

```java
throw new LoginFailedException("Invalid email or password");
```

---

### [주의]

민감정보 예외 메시지 포함 금지:

```text
password
access token
refresh token
resident number
credit card number
secret key
authorization header
private credential
```

---

### [FAQ]

Q. 예외 메시지에 ID를 넣어도 돼?

A.
일반적인 내부 식별자는 원인 파악에 도움이 될 수 있다. 단, 민감정보는 포함하면 안 된다.

Q. 사용자에게 내부 예외 메시지를 그대로 보여줘도 돼?

A.
권장하지 않는다. 내부 로그 메시지와 사용자 응답 메시지는 분리하는 것이 좋다.

---

# 7. Collection Review

## 7.1 Collection Selection Review

### [개념]

Collection Selection Review는 데이터 특성에 맞는 Collection을 선택했는지 확인하는 작업이다.

무조건 List만 사용하면 중복 제거, Key 조회, 정렬 요구사항에서 비효율적이거나 코드가 복잡해질 수 있다.

---

### [핵심]

선택 기준:

| 요구사항             | 적합한 Collection |
| -------------------- | ----------------- |
| 순서 필요, 중복 허용 | List              |
| 중복 제거            | Set               |
| 빠른 Key 조회        | Map               |
| 삽입 순서 유지 Set   | LinkedHashSet     |
| 정렬된 Set           | TreeSet           |
| 삽입 순서 유지 Map   | LinkedHashMap     |
| 정렬된 Key           | TreeMap           |
| Queue 처리           | Queue / Deque     |

---

### [실무]

나쁜 예:

```java
List<Long> userIds = new ArrayList<>();

if (!userIds.contains(userId)) {
    userIds.add(userId);
}
```

문제:

- 중복 제거를 List로 처리
- 데이터가 많아지면 contains 비용 증가

좋은 예:

```java
Set<Long> userIds = new HashSet<>();
userIds.add(userId);
```

나쁜 예:

```java
List<User> users = userRepository.findAll();

for (User user : users) {
    if (user.getId().equals(targetId)) {
        return user;
    }
}
```

좋은 예:

```java
Map<Long, User> userMap = users.stream()
    .collect(Collectors.toMap(User::getId, user -> user));

User user = userMap.get(targetId);
```

---

### [FAQ]

Q. List만 써도 되지 않아?

A.
간단한 경우 가능하지만 중복 제거는 Set, Key 조회는 Map이 더 적합하다.

Q. contains가 느릴 수 있어?

A.
List.contains는 순차 탐색이라 데이터가 많으면 비용이 증가한다. 중복 확인이 중요하면 Set을 검토한다.

---

## 7.2 Collection Mutation Review

### [개념]

Collection Mutation Review는 Collection 순회 중 구조 변경으로 ConcurrentModificationException이 발생할 위험을 확인하는 작업이다.

---

### [핵심]

위험 패턴:

- for-each 중 remove
- Stream 내부에서 원본 Collection 수정
- Iterator 외부에서 Collection 변경
- 공유 mutable Collection 직접 노출
- static mutable Collection 사용

---

### [실무]

나쁜 예:

```java
for (User user : users) {
    if (!user.isActive()) {
        users.remove(user);
    }
}
```

좋은 예:

```java
users.removeIf(user -> !user.isActive());
```

또는:

```java
List<User> activeUsers = users.stream()
    .filter(User::isActive)
    .toList();
```

외부 변경 방지:

```java
public List<Comment> getComments() {
    return List.copyOf(comments);
}
```

---

### [FAQ]

Q. 반복문 안에서 remove하면 왜 위험해?

A.
Iterator가 순회 중인 Collection 구조가 바뀌어 ConcurrentModificationException이 발생할 수 있다.

Q. 내부 Collection을 그대로 반환해도 돼?

A.
권장하지 않는다. 외부에서 내부 상태를 바꿀 수 있으므로 방어적 복사나 읽기 전용 반환을 검토한다.

---

# 8. Stream and Lambda Review

## 8.1 Stream Readability Review

### [개념]

Stream Readability Review는 Stream API가 실제로 가독성을 높이는지 확인하는 작업이다.

Stream은 필터링, 변환, 수집이 명확할 때 유용하지만 복잡한 제어 흐름에서는 for문이 더 읽기 쉬울 수 있다.

---

### [핵심]

Stream 적합:

- filter
- map
- sorted
- distinct
- collect
- grouping
- simple transformation

for-loop 적합:

- break / continue 중요
- 복잡한 분기
- 여러 상태 변경
- 예외 처리 흐름 복잡
- 디버깅 편의성이 중요한 로직

---

### [실무]

좋은 Stream 예:

```java
List<PostResponse> responses = posts.stream()
    .filter(Post::isPublished)
    .map(PostResponse::from)
    .toList();
```

나쁜 Stream 예:

```java
users.stream()
    .map(user -> {
        if (user.isActive()) {
            user.addPoint(10);
            emailService.send(user.getEmail());
            return UserResponse.from(user);
        } else {
            log.info("inactive user");
            return null;
        }
    })
    .filter(Objects::nonNull)
    .toList();
```

문제:

- Side Effect
- 상태 변경
- 외부 서비스 호출
- null 반환
- 복잡한 분기

개선 방향:

```text
복잡한 비즈니스 처리
→ for문 또는 별도 Method 분리
→ 상태 변경과 변환 분리
```

---

### [Checklist]

Stream Review Checklist:

```md
- [ ] Stream이 가독성을 높이는가?
- [ ] Lambda 내부 로직이 짧은가?
- [ ] Stream 내부에서 외부 상태 변경이 없는가?
- [ ] map에서 null을 반환하지 않는가?
- [ ] for문이 더 명확한 상황은 아닌가?
- [ ] collect 결과 타입이 명확한가?
- [ ] distinct 사용 시 equals/hashCode 기준이 올바른가?
```

---

### [FAQ]

Q. Stream이 for문보다 항상 좋아?

A.
아니다. 단순 변환과 필터링에는 좋지만 복잡한 제어 흐름은 for문이 더 명확할 수 있다.

Q. Stream 내부에서 Entity 상태를 바꿔도 돼?

A.
권장하지 않는다. Stream은 변환과 수집 중심으로 사용하고 상태 변경은 명확한 로직으로 분리하는 것이 좋다.

---

## 8.2 Lambda Complexity Review

### [개념]

Lambda Complexity Review는 Lambda 내부 로직이 과도하게 길거나 복잡하지 않은지 확인하는 작업이다.

Lambda는 짧고 명확한 동작을 표현할 때 가장 좋다.

---

### [핵심]

위험 신호:

- Lambda 내부 if-else 중첩
- Lambda 내부 try-catch
- Lambda 내부 외부 API 호출
- Lambda 내부 DB 저장
- Lambda 내부 상태 변경
- Lambda 내부 10줄 이상 복잡한 로직
- Method Reference로 대체 가능한 단순 호출

---

### [실무]

나쁜 예:

```java
List<OrderResponse> responses = orders.stream()
    .map(order -> {
        if (order.isCanceled()) {
            throw new IllegalStateException("canceled order");
        }

        int totalPrice = 0;
        for (OrderItem item : order.getItems()) {
            totalPrice += item.getPrice() * item.getQuantity();
        }

        return new OrderResponse(order.getId(), totalPrice);
    })
    .toList();
```

개선 예:

```java
List<OrderResponse> responses = orders.stream()
    .map(this::toOrderResponse)
    .toList();

private OrderResponse toOrderResponse(Order order) {
    if (order.isCanceled()) {
        throw new IllegalStateException("canceled order");
    }

    int totalPrice = calculateTotalPrice(order);
    return new OrderResponse(order.getId(), totalPrice);
}
```

---

### [FAQ]

Q. Lambda 안에 긴 로직을 넣으면 왜 안 좋아?

A.
읽기 어렵고 테스트하기 어려우며 재사용도 어렵다. 별도 Method로 분리하는 것이 좋다.

Q. Method Reference는 언제 좋아?

A.
이미 의미 있는 Method가 있고 단순 호출만 할 때 가독성을 높일 수 있다.

---

# 9. OOP Anti Pattern Review

## 9.1 Setter Overuse

### [개념]

Setter Overuse는 모든 Field에 Setter를 열어 객체 상태를 외부에서 마음대로 변경하게 만드는 Anti Pattern이다.

Setter Overuse는 Encapsulation을 약화시키고 상태 변경 규칙을 여러 곳에 흩어지게 만든다.

---

### [핵심]

문제:

- 객체 상태 보호 실패
- 비즈니스 규칙 분산
- 잘못된 상태 생성 가능
- 변경 추적 어려움
- Entity가 데이터 덩어리로 전락
- 테스트 시 상태 조합 폭증

---

### [실무]

나쁜 예:

```java
order.setStatus(OrderStatus.CANCELED);
order.setCanceledAt(LocalDateTime.now());
order.setCancelReason(reason);
```

문제:

- 취소 규칙이 외부에 흩어짐
- 일부 Field만 변경된 불완전 상태 가능

좋은 예:

```java
order.cancel(reason);
```

Entity:

```java
public void cancel(String reason) {
    if (this.status == OrderStatus.DELIVERED) {
        throw new IllegalStateException("delivered order cannot be canceled");
    }

    this.status = OrderStatus.CANCELED;
    this.canceledAt = LocalDateTime.now();
    this.cancelReason = reason;
}
```

---

### [Review Signal]

Setter Overuse 감지 신호:

```text
setStatus()
setPoint()
setRole()
setDeleted()
setUpdatedAt()
setCanceledAt()
setApprovedAt()
```

상태 전이가 필요한 Field라면 의미 있는 Method로 변경한다.

---

### [FAQ]

Q. Setter를 전부 없애야 해?

A.
아니다. 하지만 비즈니스 상태 변경은 Setter보다 의미 있는 Method로 표현하는 것이 좋다.

Q. Setter Overuse는 왜 위험해?

A.
객체가 잘못된 상태가 되는 것을 막기 어렵고 상태 변경 규칙이 여러 곳에 흩어진다.

---

## 9.2 God Class / God Service

### [개념]

God Class 또는 God Service는 하나의 Class가 지나치게 많은 책임을 가지고 시스템의 대부분 로직을 처리하는 Anti Pattern이다.

---

### [핵심]

문제:

- 변경 영향 범위 증가
- 테스트 어려움
- 코드 충돌 증가
- Method 길이 증가
- 중복 로직 증가
- 객체 협력 구조 약화
- 유지보수 비용 증가

---

### [실무]

God Service 예:

```text
UserService
→ 회원가입
→ 로그인
→ 이메일 발송
→ 파일 업로드
→ 결제 처리
→ 알림 생성
→ 통계 리포트 생성
```

개선 방향:

```text
UserService
→ 회원 도메인 흐름

AuthService
→ 인증 흐름

EmailService
→ 이메일 발송

FileStorageService
→ 파일 저장

PaymentService
→ 결제 처리

NotificationService
→ 알림 생성

ReportService
→ 통계 리포트
```

---

### [Checklist]

God Class Review Checklist:

```md
- [ ] Class Method 수가 과도하지 않은가?
- [ ] 서로 다른 도메인 기능이 섞여 있지 않은가?
- [ ] 외부 연동 책임을 직접 모두 처리하지 않는가?
- [ ] private Method가 지나치게 많지 않은가?
- [ ] 하나의 변경이 여러 기능에 영향을 주지 않는가?
- [ ] 테스트 대상 범위가 너무 크지 않은가?
```

---

### [FAQ]

Q. Service가 커지는 건 자연스러운 거 아니야?

A.
기능이 늘면 커질 수 있지만 변경 이유가 여러 개라면 책임 분리를 검토해야 한다.

Q. God Service는 어떻게 나눠?

A.
도메인 책임, 외부 연동 책임, 정책 판단 책임, 알림 책임, 파일 처리 책임 등 변경 이유 기준으로 나눈다.

---

## 9.3 Anemic Domain Model

### [개념]

Anemic Domain Model은 Entity가 Field와 Getter / Setter만 가지고 모든 비즈니스 로직이 Service에 몰리는 Anti Pattern이다.

---

### [핵심]

문제:

- Entity가 데이터 구조체가 됨
- 상태 변경 규칙이 Service에 흩어짐
- Encapsulation 약화
- 잘못된 상태 생성 가능
- Service가 비대해짐

---

### [실무]

나쁜 예:

```java
if (post.getStatus() != PostStatus.DRAFT) {
    throw new IllegalStateException("only draft can be published");
}

post.setStatus(PostStatus.PUBLISHED);
post.setPublishedAt(LocalDateTime.now());
```

좋은 예:

```java
post.publish();
```

Entity:

```java
public void publish() {
    if (this.status != PostStatus.DRAFT) {
        throw new IllegalStateException("only draft can be published");
    }

    this.status = PostStatus.PUBLISHED;
    this.publishedAt = LocalDateTime.now();
}
```

---

### [주의]

Anemic Domain Model 판단 기준:

```text
단순 CRUD 중심
→ 허용 가능

상태 전이 / 비즈니스 규칙 많음
→ Entity Method 검토
```

모든 로직을 Entity에 넣는 것도 정답은 아니다.

Service는 흐름 조합, Entity는 상태 변경 규칙을 담당하는 것이 좋다.

---

### [FAQ]

Q. 모든 비즈니스 로직을 Entity에 넣어야 해?

A.
아니다. Entity는 상태 변경 규칙을 담당하고 Service는 애플리케이션 흐름을 조합하는 것이 좋다.

Q. Anemic Domain Model은 항상 나쁜가?

A.
단순 CRUD에서는 큰 문제가 아닐 수 있지만 상태 규칙이 복잡해지면 유지보수 문제가 커진다.

---

## 9.4 Overused Static

### [개념]

Overused Static은 객체가 가져야 할 책임을 static Method나 static Field에 과도하게 몰아넣는 Anti Pattern이다.

---

### [핵심]

문제:

- 객체지향 설계 약화
- 의존성 주입 어려움
- 테스트 대체 어려움
- 전역 상태 증가
- 동시성 문제 가능
- 상태 추적 어려움

---

### [실무]

허용 가능:

```java
public final class DateUtils {
    private DateUtils() {
    }

    public static boolean isPast(LocalDate date) {
        return date.isBefore(LocalDate.now());
    }
}
```

주의 필요:

```java
public class UserContext {
    public static Long currentUserId;
}
```

문제:

- 전역 mutable state
- 요청 간 데이터 오염 위험
- 동시성 문제 가능

개선 방향:

```text
Request Scope
SecurityContext
Method Parameter
Spring Bean
ThreadLocal 신중 사용
```

---

### [Review Signal]

static 사용 검토 질문:

```text
상태를 가지는가?
외부 의존성이 있는가?
테스트에서 대체해야 하는가?
요청마다 값이 달라지는가?
동시에 여러 사용자가 접근하는가?
```

하나라도 해당하면 static 사용을 재검토한다.

---

### [FAQ]

Q. static Utility는 써도 돼?

A.
상태가 없고 외부 의존성이 없는 순수 함수라면 사용할 수 있다.

Q. static Field가 위험한 이유는?

A.
전역으로 공유되어 예측하기 어렵고 동시성 문제나 테스트 오염을 만들 수 있다.

---

## 9.5 Meaningless Interface

### [개념]

Meaningless Interface는 구현체가 하나뿐이고 교체 가능성도 낮은데 관습적으로 Interface를 만드는 Anti Pattern이다.

---

### [핵심]

문제:

- 파일 수 증가
- 탐색 비용 증가
- 추상화 의미 약화
- 코드 이해 어려움
- 실제 확장성 없이 복잡도만 증가

---

### [실무]

불필요할 수 있는 예:

```java
public interface UserService {
    UserResponse getUser(Long userId);
}

@Service
public class UserServiceImpl implements UserService {
    public UserResponse getUser(Long userId) {
        return null;
    }
}
```

Interface가 필요한 경우:

```text
구현체가 여러 개
정책 교체 가능성 있음
테스트 Mock 경계가 필요
외부 시스템 추상화 필요
의존성 역전이 중요
```

예:

```java
public interface NotificationSender {
    void send(NotificationMessage message);
}
```

구현체:

```text
EmailNotificationSender
SmsNotificationSender
PushNotificationSender
```

---

### [FAQ]

Q. Service마다 Interface를 꼭 만들어야 해?

A.
필수는 아니다. 구현체가 하나뿐이고 교체 가능성이 낮으면 과한 추상화일 수 있다.

Q. Interface는 언제 의미가 있어?

A.
역할 추상화, 구현체 교체, 테스트 대체, 정책 분리, 외부 의존성 분리가 필요할 때 의미가 있다.

---

## 9.6 Inheritance for Reuse

### [개념]

Inheritance for Reuse는 단순 코드 재사용을 위해 상속을 사용하는 Anti Pattern이다.

상속은 is-a 관계와 다형성이 명확할 때 사용해야 하며, 재사용만 목적이면 Composition을 우선 검토한다.

---

### [핵심]

문제:

- 부모 변경이 자식에 강하게 영향
- 깊은 계층 구조 생성
- 의미적으로 부정확한 is-a 관계
- 테스트와 변경 어려움
- protected 상태 남용

---

### [실무]

나쁜 판단:

```text
EmailSender와 SmsSender가 sendLog()를 공유해야 함
→ AbstractSender 상속
```

개선 방향:

```text
LogWriter를 별도 Component로 분리
→ EmailSender가 LogWriter를 사용
→ SmsSender가 LogWriter를 사용
```

예:

```java
public class EmailSender {
    private final SendLogWriter sendLogWriter;

    public void send(String email, String message) {
        sendLogWriter.write("email sent");
    }
}
```

---

### [Checklist]

Inheritance Review Checklist:

```md
- [ ] 명확한 is-a 관계인가?
- [ ] 다형성이 필요한가?
- [ ] 부모 변경이 자식에 미치는 영향을 감당할 수 있는가?
- [ ] 코드 재사용만 목적인가?
- [ ] Composition으로 대체 가능한가?
- [ ] 상속 계층이 깊어지지 않는가?
```

---

### [FAQ]

Q. 상속은 언제 써야 해?

A.
명확한 is-a 관계와 다형성이 필요할 때 사용한다.

Q. 코드 재사용 목적이면 상속보다 뭐가 좋아?

A.
Composition을 사용해 필요한 객체를 포함하고 위임하는 방식이 더 유연하다.

---

# 10. Common Java Backend Anti Patterns

## 10.1 Optional.get Direct Call

### [개념]

Optional.get Direct Call은 Optional에 값이 있는지 확인하지 않고 get()을 직접 호출하는 Anti Pattern이다.

값이 없으면 NoSuchElementException이 발생한다.

---

### [핵심]

문제:

- 예외 원인 불명확
- 조회 실패 상황 처리 부재
- Custom Exception 변환 실패
- Controller / Service 장애 발생 가능

---

### [실무]

나쁜 예:

```java
User user = userRepository.findById(userId).get();
```

좋은 예:

```java
User user = userRepository.findById(userId)
    .orElseThrow(() -> new UserNotFoundException(userId));
```

선택 조회라면:

```java
Optional<User> user = userRepository.findByEmail(email);
```

---

### [FAQ]

Q. Optional.get은 절대 쓰면 안 돼?

A.
테스트나 값 존재가 명확히 보장되는 특수 상황을 제외하면 orElseThrow, orElse, orElseGet을 사용하는 것이 좋다.

Q. Repository findById 결과는 어떻게 처리해?

A.
필수 조회면 orElseThrow로 Custom Exception으로 변환하고 선택 조회면 Optional을 반환할 수 있다.

---

## 10.2 Catch and Ignore

### [개념]

Catch and Ignore는 예외를 catch한 뒤 아무 처리도 하지 않는 Anti Pattern이다.

실패가 감춰지고 시스템이 잘못된 상태로 계속 동작할 수 있다.

---

### [핵심]

문제:

- 장애 원인 추적 어려움
- 실패 상태 은닉
- 데이터 불일치 가능
- 잘못된 성공 응답 가능
- 운영 로그 부족

---

### [실무]

나쁜 예:

```java
try {
    notificationSender.send(message);
} catch (Exception e) {
}
```

개선 예:

```java
try {
    notificationSender.send(message);
} catch (NotificationSendException e) {
    log.warn("Notification send failed. userId={}", userId, e);
}
```

또는 실패가 중요한 경우:

```java
try {
    notificationSender.send(message);
} catch (NotificationSendException e) {
    throw new NotificationFailedException(userId, e);
}
```

---

### [FAQ]

Q. 실패해도 무시해도 되는 알림은 catch만 해도 돼?

A.
무시 가능한 실패라도 최소한 로그를 남기거나 의도적으로 무시한다는 구조를 명확히 해야 한다.

Q. Exception을 catch한 뒤 RuntimeException으로 감싸도 돼?

A.
가능하지만 원인 예외를 함께 전달하고 의미 있는 Custom Exception으로 변환하는 것이 좋다.

---

## 10.3 String Comparison with `==`

### [개념]

String Comparison with `==`는 문자열 내용을 비교해야 하는 상황에서 참조 비교 연산자인 `==`를 사용하는 Anti Pattern이다.

문자열 내용 비교는 `equals()`를 사용해야 한다.

---

### [핵심]

문제:

- 같은 내용이어도 false 가능
- JVM String Pool 때문에 테스트에서는 우연히 동작할 수 있음
- 조건 분기 오류 발생
- 인증 / 상태 / 타입 비교 오류 가능

---

### [실무]

나쁜 예:

```java
if (user.getRole() == "ADMIN") {
    grantAdminPermission();
}
```

좋은 예:

```java
if ("ADMIN".equals(user.getRole())) {
    grantAdminPermission();
}
```

더 좋은 방향:

```java
if (user.getRole() == UserRole.ADMIN) {
    grantAdminPermission();
}
```

---

### [FAQ]

Q. String 비교에 ==를 쓰면 왜 안 돼?

A.
==는 참조 비교이고 equals는 문자열 내용 비교이기 때문이다.

Q. Role이나 Status는 String으로 관리해도 돼?

A.
가능하지만 오타와 비교 오류를 줄이려면 Enum 사용을 검토하는 것이 좋다.

---

## 10.4 Double for Money

### [개념]

Double for Money는 금액이나 정밀 계산이 필요한 값에 double / float를 사용하는 Anti Pattern이다.

double은 부동소수점 정밀도 문제로 금액 계산에 적합하지 않을 수 있다.

---

### [핵심]

문제:

- 정밀도 오차
- 누적 계산 오차
- 결제 / 정산 오류 가능
- 비교 연산 불안정

---

### [실무]

나쁜 예:

```java
double totalPrice = price * quantity * discountRate;
```

좋은 예:

```java
BigDecimal totalPrice = price
    .multiply(BigDecimal.valueOf(quantity))
    .multiply(discountRate);
```

또는 최소 단위 정수 사용:

```java
long priceWon = 10000L;
long totalPriceWon = priceWon * quantity;
```

---

### [FAQ]

Q. 금액 계산에 double을 쓰면 안 돼?

A.
정밀도 문제가 생길 수 있으므로 BigDecimal 또는 최소 단위 정수 계산을 검토하는 것이 좋다.

Q. 할인율 계산은 어떻게 해?

A.
BigDecimal을 사용하고 반올림 정책을 명확히 지정하는 것이 좋다.

---

## 10.5 Mutable Static State

### [개념]

Mutable Static State는 static Field에 변경 가능한 상태를 저장하는 Anti Pattern이다.

Backend 서버는 여러 요청을 동시에 처리하므로 static mutable state는 요청 간 데이터 오염과 동시성 문제를 만들 수 있다.

---

### [핵심]

문제:

- 전역 상태 공유
- 요청 간 데이터 오염
- 테스트 순서 의존성
- 동시성 문제
- 서버 재시작 전까지 상태 유지
- 예측 어려운 버그

---

### [실무]

나쁜 예:

```java
public class LoginUserHolder {
    public static Long userId;
}
```

문제:

- 사용자 A 요청의 userId가 사용자 B 요청에 섞일 수 있음

개선 방향:

```text
SecurityContext 사용
Method Parameter로 전달
Request Scope Bean 사용
ThreadLocal은 신중히 사용하고 반드시 clear
```

상수는 가능:

```java
public static final int DEFAULT_PAGE_SIZE = 20;
```

---

### [FAQ]

Q. static final 상수도 위험해?

A.
변경 불가능한 상수는 일반적으로 괜찮다. 문제는 변경 가능한 static 상태다.

Q. 로그인 사용자 정보를 static에 저장하면 왜 안 돼?

A.
여러 사용자의 요청이 동시에 처리되면서 데이터가 섞일 수 있기 때문이다.

---

# 11. Refactoring Review

## 11.1 Refactoring Decision Flow

### [개념]

Refactoring Review는 코드의 외부 동작은 유지하면서 내부 구조를 개선할 필요가 있는지 판단하는 작업이다.

Review Agent는 문제를 지적할 뿐 아니라 안전한 개선 방향을 제시해야 한다.

---

### [핵심]

Refactoring 대상:

- Long Method
- Large Class
- Duplicate Code
- Feature Envy
- Primitive Obsession
- Data Class
- Switch / if-else Explosion
- Magic Number
- Poor Naming
- Tight Coupling
- Inappropriate Static

---

### [Flow]

Refactoring Flow:

```text
Code Smell 발견
→ 외부 동작 유지 가능 여부 확인
→ Test 존재 여부 확인
→ 작은 단위로 변경
→ Method Extract
→ Class Extract
→ Interface / Strategy 검토
→ Null / Exception 정책 정리
→ Review 결과 검증
```

---

### [실무]

Long Method 개선 순서:

```text
1. Method 이름 확인
2. 코드 블록별 의도 주석 없이 이해 가능한지 확인
3. 검증 로직 분리
4. 조회 로직 분리
5. 계산 로직 분리
6. 상태 변경 로직 분리
7. 응답 변환 로직 분리
```

예:

```java
public OrderResponse createOrder(OrderCreateRequest request) {
    validateOrderRequest(request);
    User user = findUserOrThrow(request.userId());
    Order order = Order.create(user, request.items());
    Order savedOrder = orderRepository.save(order);
    return OrderResponse.from(savedOrder);
}
```

---

### [FAQ]

Q. Refactoring은 언제 해야 해?

A.
코드 동작은 맞지만 읽기 어렵고 변경하기 어렵고 테스트하기 어려울 때 검토한다.

Q. Refactoring 전에 가장 중요한 것은 뭐야?

A.
기존 동작을 확인할 수 있는 테스트나 명확한 검증 기준이 있어야 한다.

---

## 11.2 Naming Review

### [개념]

Naming Review는 Class, Method, Variable 이름이 역할과 의도를 명확히 표현하는지 확인하는 작업이다.

좋은 이름은 주석보다 강력한 문서 역할을 한다.

---

### [핵심]

검토 기준:

- Class 이름은 책임을 표현
- Method 이름은 동작을 표현
- boolean Method는 질문 형태 가능
- 변수 이름은 역할을 표현
- 축약어 남용 금지
- 모호한 이름 금지
- Manager / Processor / Handler 남용 주의

---

### [실무]

나쁜 이름:

```java
public void process() { }
public void handle() { }
public void doSomething() { }
User u;
List<User> list;
```

좋은 이름:

```java
public void registerUser() { }
public void cancelOrder() { }
public boolean canPublish() { }
User requestedUser;
List<User> activeUsers;
```

Manager 이름 주의:

```text
UserManager
PostProcessor
DataHandler
```

이름이 모호하면 실제 책임을 기준으로 구체화한다.

```text
UserRegistrationService
PostPublishPolicy
CsvImportHandler
```

---

### [FAQ]

Q. Method 이름은 어떻게 지어야 해?

A.
호출했을 때 어떤 동작이 일어나는지 명확히 드러나야 한다.

Q. Manager, Processor 이름은 쓰면 안 돼?

A.
금지는 아니지만 책임이 모호해지기 쉬우므로 더 구체적인 이름을 먼저 검토한다.

---

# 12. Backend Review Checklist

## 12.1 Full Review Checklist

### [개념]

Backend Review Checklist는 Java 기반 백엔드 코드 검토 시 반복적으로 확인해야 하는 기준이다.

이 Checklist는 Review Agent가 Java Code Review와 Anti Pattern Detection을 수행할 때 사용한다.

---

### [핵심]

Full Checklist:

```md
# Java Backend Code Review Checklist

## Responsibility

- [ ] Class 책임이 명확한가?
- [ ] Method가 하나의 책임을 가지는가?
- [ ] Layer 역할이 분리되어 있는가?
- [ ] Controller에 비즈니스 로직이 과도하지 않은가?
- [ ] Service가 God Service가 되지 않았는가?
- [ ] Entity가 상태 변경 규칙을 적절히 가지는가?

## Method Design

- [ ] Method 이름이 동작을 명확히 표현하는가?
- [ ] Parameter가 과도하게 많지 않은가?
- [ ] boolean flag parameter를 남용하지 않는가?
- [ ] return null을 피하고 있는가?
- [ ] 중첩 if가 과도하지 않은가?
- [ ] guard clause를 적용할 수 있는가?

## Type Safety

- [ ] Raw Type을 사용하지 않는가?
- [ ] Generic Type이 명확한가?
- [ ] Object 반환을 남용하지 않는가?
- [ ] 강제 Casting이 반복되지 않는가?
- [ ] primitive / wrapper 선택이 적절한가?

## Null Safety

- [ ] 필수 값 검증이 있는가?
- [ ] Collection 반환이 null이 아닌가?
- [ ] Optional.get 직접 호출이 없는가?
- [ ] Optional을 Field / Parameter로 남용하지 않는가?
- [ ] Repository 조회 실패를 명확히 처리하는가?

## Exception Handling

- [ ] catch 후 빈 블록이 없는가?
- [ ] Exception을 무시하지 않는가?
- [ ] Custom Exception 이름이 명확한가?
- [ ] 예외 메시지가 원인 파악에 충분한가?
- [ ] 민감정보가 예외 메시지에 포함되지 않는가?
- [ ] Controller마다 try-catch를 반복하지 않는가?

## Collection

- [ ] List / Set / Map 선택이 적절한가?
- [ ] 중복 제거에 Set을 검토했는가?
- [ ] Key 조회에 Map을 검토했는가?
- [ ] Collection 순회 중 구조 변경이 없는가?
- [ ] 내부 Collection을 직접 노출하지 않는가?
- [ ] equals / hashCode가 필요한 곳에 구현되어 있는가?

## Stream / Lambda

- [ ] Stream이 가독성을 높이는가?
- [ ] Lambda 내부 로직이 길지 않은가?
- [ ] Stream 내부 Side Effect가 없는가?
- [ ] map에서 null을 반환하지 않는가?
- [ ] for문이 더 적합한 상황은 아닌가?

## OOP

- [ ] Field 접근 제어자가 적절한가?
- [ ] Setter를 과도하게 사용하지 않는가?
- [ ] Encapsulation이 지켜지는가?
- [ ] 상속보다 조합을 우선 검토했는가?
- [ ] Interface가 의미 있는 추상화인가?
- [ ] Abstract Class 사용 이유가 명확한가?

## Static / Final / Immutability

- [ ] mutable static state가 없는가?
- [ ] static Utility가 순수 함수인가?
- [ ] final을 불변성 보조로 적절히 사용하는가?
- [ ] DTO 불변성을 검토했는가?
- [ ] 내부 mutable Collection 노출을 방지했는가?

## DTO / Entity

- [ ] Entity를 Request DTO로 직접 사용하지 않는가?
- [ ] Entity를 Response로 직접 반환하지 않는가?
- [ ] Request DTO와 Response DTO가 분리되어 있는가?
- [ ] 민감정보가 Response에 포함되지 않는가?
- [ ] DTO에 비즈니스 로직이 과도하지 않은가?

## Anti Pattern

- [ ] God Class / God Service가 없는가?
- [ ] Anemic Domain Model 문제가 심하지 않은가?
- [ ] Setter Overuse가 없는가?
- [ ] Optional.get Direct Call이 없는가?
- [ ] Catch and Ignore가 없는가?
- [ ] String 비교에 ==를 사용하지 않는가?
- [ ] 금액 계산에 double을 사용하지 않는가?
- [ ] Meaningless Interface가 없는가?
- [ ] Inheritance for Reuse가 없는가?
```

---

### [실무]

Review Agent 출력 권장 형식:

```md
# Review Result

## Summary

- 전체 평가:
- 주요 위험:
- 우선 수정 대상:

## Critical Issues

- 문제:
- 이유:
- 개선 방향:

## Suggested Refactoring

- 현재 코드:
- 개선 코드:
- 기대 효과:

## Checklist Result

- Responsibility:
- Null Safety:
- Type Safety:
- Exception:
- Collection:
- Anti Pattern:
```

---

### [FAQ]

Q. Java Backend Code Review는 어떤 순서로 해?

A.
Layer 확인, 책임 확인, Method 확인, Type Safety, Null Safety, Exception Handling, Collection, OOP, Anti Pattern 순서로 보면 좋다.

Q. Review 결과는 어떻게 작성해야 해?

A.
문제점, 이유, 개선 방향, 예시 코드를 함께 제시하는 것이 좋다.

---

# 13. Anti Pattern Detection Map

## 13.1 Problem to Cause Map

### [개념]

Anti Pattern Detection Map은 증상에서 원인을 빠르게 찾기 위한 Review Agent용 검색 기준이다.

사용자가 “코드가 이상해”, “NPE가 나”, “Service가 너무 커”, “중복이 많아”라고 질문할 때 관련 Anti Pattern을 연결한다.

---

### [핵심]

증상별 원인:

| 증상                         | 의심 Anti Pattern                       |
| ---------------------------- | --------------------------------------- |
| NPE 발생                     | null 반환, Optional.get, DTO Field 누락 |
| ClassCastException 발생      | Raw Type, Object 반환, 잘못된 Casting   |
| Service가 너무 큼            | God Service, Long Method, 책임 혼합     |
| Entity가 Setter만 있음       | Anemic Domain Model, Setter Overuse     |
| 테스트가 어려움              | static 남용, tight coupling, God Class  |
| 조건문이 계속 늘어남         | if-else explosion, 다형성 부족          |
| 중복 코드가 많음             | Duplicate Logic, 책임 분리 부족         |
| API 응답에 불필요 Field 노출 | Entity 직접 반환, DTO 분리 부족         |
| Collection 중복 제거가 안 됨 | equals/hashCode 누락                    |
| 반복 중 오류 발생            | ConcurrentModificationException         |
| 금액 계산이 이상함           | double 사용, 반올림 정책 부재           |
| Role 비교가 실패함           | String 비교에 == 사용                   |

---

### [실무]

Review Query Mapping:

```text
"왜 NullPointerException이 나?"
→ Null Safety Review
→ Optional Review
→ Repository Result Handling

"Service가 너무 긴데?"
→ God Service
→ Long Method
→ Responsibility Review

"Entity에 Setter 많아도 돼?"
→ Setter Overuse
→ Encapsulation Review
→ Entity State Method

"Interface 꼭 만들어야 해?"
→ Meaningless Interface
→ Interface Review

"상속으로 공통 코드 빼도 돼?"
→ Inheritance for Reuse
→ Composition Review
```

---

### [FAQ]

Q. Anti Pattern은 어떻게 빨리 찾을 수 있어?

A.
증상을 먼저 보고 책임, null, 타입, 예외, Collection, OOP 기준으로 원인을 좁히면 된다.

Q. NPE가 나면 어떤 Anti Pattern을 의심해?

A.
null 반환, Optional.get 직접 호출, DTO Field 누락, Repository 결과 처리 누락을 먼저 확인한다.

---

# 14. Review Output Template

## 14.1 Java Review Agent Template

### [개념]

Review Output Template은 Review Agent가 Java Backend Code Review 결과를 일관된 형식으로 출력하기 위한 템플릿이다.

---

### [핵심]

출력 원칙:

- 문제만 지적하지 않음
- 왜 문제인지 설명
- 개선 방향 제시
- 필요 시 개선 코드 제공
- 우선순위 표시
- Critical / Major / Minor 구분
- Java Foundation 기준으로 판단
- Spring Boot 세부 Annotation 판단은 별도 Domain Rules로 위임 가능

---

### [실무]

Review Output Template:

````md
# Java Backend Code Review

## 1. Summary

- Overall:
- Main Risk:
- Priority:

---

## 2. Critical Issues

### Issue 1. 문제 제목

#### Problem

문제 설명.

#### Why It Matters

왜 위험한지 설명.

#### Suggested Fix

개선 방향.

#### Example

```java
// 개선 예시
```

---

## 3. Major Issues

### Issue 1. 문제 제목

#### Problem

#### Why It Matters

#### Suggested Fix

---

## 4. Minor Issues

- Naming:
- Style:
- Readability:

---

## 5. Checklist Result

| Area               | Result             | Note |
| ------------------ | ------------------ | ---- |
| Responsibility     | PASS / WARN / FAIL |      |
| Method Design      | PASS / WARN / FAIL |      |
| Type Safety        | PASS / WARN / FAIL |      |
| Null Safety        | PASS / WARN / FAIL |      |
| Exception Handling | PASS / WARN / FAIL |      |
| Collection         | PASS / WARN / FAIL |      |
| OOP                | PASS / WARN / FAIL |      |
| Anti Pattern       | PASS / WARN / FAIL |      |

---

## 6. Final Recommendation

최종 개선 방향.
````

---

### [FAQ]

Q. Review 결과에 코드 예시가 꼭 필요해?

A.
문제가 복잡하거나 수정 방향이 애매하면 개선 코드 예시를 포함하는 것이 좋다.

Q. Review 결과는 길게 써야 해?

A.
문제, 이유, 개선 방향이 명확하면 된다. 불필요한 장문 설명은 피한다.

---

# 15. Final Review Summary

## 15.1 Java Part08 Summary

### [개념]

Java Part08은 Backend Code Review와 Anti Pattern 탐지를 위한 Java Foundation 문서다.

이 문서는 Backend Agent / Review Agent가 Java 기반 백엔드 코드를 검토하고 안전한 리팩터링 방향을 제시하도록 지원한다.

---

### [핵심]

핵심 Review 대상:

- Class Responsibility
- Method Responsibility
- Controller Review
- Service Review
- Entity Review
- DTO Review
- Type Safety
- Null Safety
- Optional Usage
- Exception Handling
- Collection Selection
- Stream Readability
- Lambda Complexity
- Setter Overuse
- God Service
- Anemic Domain Model
- Overused Static
- Meaningless Interface
- Inheritance for Reuse
- Common Java Backend Anti Patterns

---

### [실무]

최종 Review Flow:

```text
Java Backend Code
→ Identify Layer
→ Check Responsibility
→ Check Method Design
→ Check Type Safety
→ Check Null Safety
→ Check Exception Handling
→ Check Collection Usage
→ Check Stream / Lambda
→ Check OOP Principles
→ Detect Anti Patterns
→ Suggest Refactoring
→ Output Review Result
```

---

### [FAQ]

Q. Java Part08의 목적은 뭐야?

A.
Java 기반 백엔드 코드에서 책임 분리, 타입 안정성, Null Safety, 예외 처리, Anti Pattern을 검토하기 위한 기준을 제공하는 것이다.

Q. 이 문서는 Spring Boot 코드 검토에도 사용할 수 있어?

A.
가능하다. Spring Boot 세부 규칙은 별도 문서에서 다루되 Java Class, Method, DTO, Entity, Service 품질 검토에는 이 문서를 사용한다.

Q. Review Agent가 가장 먼저 확인해야 할 것은 뭐야?

A.
Layer 역할과 Class 책임이 명확한지 먼저 확인해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Java Backend Code Review는 무엇을 확인해야 해?
A. Class 책임, Method 책임, Type Safety, Null Safety, Exception Handling, Collection 선택, OOP 설계, Anti Pattern을 확인해야 한다.

Q. Java 코드 리뷰 순서는?
A. Layer 확인, 책임 확인, Method 확인, Type Safety, Null Safety, Exception, Collection, OOP, Anti Pattern 순서가 좋다.

Q. Controller 코드 리뷰에서 중요한 것은?
A. DTO 사용, Entity 직접 반환 금지, Repository 직접 호출 금지, 비즈니스 로직 과다 작성 금지다.

Q. Service 코드 리뷰에서 중요한 것은?
A. Method 책임, Transaction 경계, Repository 결과 처리, Entity 상태 변경, Exception Handling, 외부 의존성 분리다.

Q. Entity 코드 리뷰에서 중요한 것은?
A. Encapsulation, Setter 남용 방지, 의미 있는 상태 변경 Method, 필수 값 검증, 내부 Collection 보호다.

Q. DTO 코드 리뷰에서 중요한 것은?
A. Request DTO와 Response DTO 분리, Entity 직접 노출 방지, 민감정보 노출 방지, Validation 적용이다.

Q. Java에서 Setter를 많이 쓰면 왜 문제야?
A. 객체 상태 변경 규칙이 외부에 흩어지고 잘못된 상태가 만들어질 수 있기 때문이다.

Q. Setter Overuse는 어떻게 고쳐?
A. setStatus 같은 단순 Setter 대신 cancel, publish, activate 같은 의미 있는 상태 변경 Method로 바꾼다.

Q. God Service는 무엇이야?
A. 하나의 Service가 너무 많은 책임을 가지고 여러 도메인 기능과 외부 연동을 모두 처리하는 Anti Pattern이다.

Q. Service가 너무 크면 어떻게 나눠?
A. 도메인 책임, 외부 연동, 파일 처리, 알림, 결제, 리포트 등 변경 이유 기준으로 분리한다.

Q. Anemic Domain Model은 뭐야?
A. Entity가 Getter와 Setter만 가지고 모든 비즈니스 로직이 Service에 몰리는 구조다.

Q. Entity에 비즈니스 로직을 넣어도 돼?
A. 상태 변경 규칙은 Entity Method로 표현할 수 있고 Service는 흐름 조합을 담당하는 것이 좋다.

Q. Optional.get을 바로 쓰면 왜 안 돼?
A. 값이 없으면 NoSuchElementException이 발생하므로 orElseThrow, orElse, orElseGet을 사용하는 것이 좋다.

Q. Repository findById 결과는 어떻게 처리해?
A. 필수 조회라면 orElseThrow로 Custom Exception으로 변환하고 선택 조회라면 Optional 반환을 유지할 수 있다.

Q. return null은 왜 위험해?
A. 호출부에서 NullPointerException이 발생할 수 있으므로 Optional, empty collection, 예외 변환을 검토해야 한다.

Q. 목록 조회 결과가 없으면 null을 반환해도 돼?
A. 대부분 empty list를 반환하는 것이 좋다.

Q. Exception을 catch하고 무시하면 왜 문제야?
A. 실패 원인이 숨겨지고 디버깅과 장애 대응이 어려워진다.

Q. Custom Exception은 언제 사용해?
A. 비즈니스 오류 의미가 명확하거나 공통 응답 처리가 필요한 경우 사용한다.

Q. 예외 메시지에 민감정보를 넣어도 돼?
A. 안 된다. password, token, secret key 같은 민감정보는 예외 메시지나 로그에 포함하면 안 된다.

Q. Raw Type은 왜 문제야?
A. 컴파일 시점 타입 검사가 약해져 ClassCastException 위험이 커진다.

Q. Object 반환은 왜 피해야 해?
A. 호출부에서 타입을 알기 어렵고 강제 Casting이 필요해 Type Safety가 떨어진다.

Q. List와 Set은 어떻게 선택해?
A. 순서와 중복 허용이 필요하면 List, 중복 제거가 중요하면 Set을 사용한다.

Q. Map은 언제 사용해?
A. Key로 값을 빠르게 조회하거나 그룹핑 결과를 저장할 때 사용한다.

Q. 반복문에서 Collection remove하면 왜 오류가 나?
A. 순회 중 Collection 구조가 바뀌면 ConcurrentModificationException이 발생할 수 있다.

Q. Stream은 언제 쓰는 게 좋아?
A. Collection 필터링, 변환, 정렬, 수집 흐름이 명확할 때 좋다.

Q. Stream이 for문보다 항상 좋아?
A. 아니다. 복잡한 분기, break, continue, 상태 변경이 중요하면 for문이 더 명확할 수 있다.

Q. Lambda 안에 긴 로직을 넣어도 돼?
A. 권장하지 않는다. 긴 로직은 별도 Method로 분리하는 것이 좋다.

Q. static Utility는 써도 돼?
A. 상태와 외부 의존성이 없는 순수 함수라면 사용할 수 있다.

Q. mutable static state는 왜 위험해?
A. 전역 공유 상태가 되어 요청 간 데이터 오염, 동시성 문제, 테스트 오염을 만들 수 있다.

Q. Interface는 Service마다 꼭 만들어야 해?
A. 필수는 아니다. 구현체가 하나뿐이고 교체 가능성이 낮으면 과한 추상화일 수 있다.

Q. Meaningless Interface는 뭐야?
A. 구현체 교체 가능성이나 다형성 필요가 없는데 관습적으로 Interface만 추가하는 Anti Pattern이다.

Q. 상속으로 공통 코드를 재사용해도 돼?
A. 명확한 is-a 관계와 다형성이 없다면 Composition을 우선 검토하는 것이 좋다.

Q. String 비교에 ==를 쓰면 왜 안 돼?
A. ==는 참조 비교이고 equals는 문자열 내용 비교이기 때문이다.

Q. Role이나 Status는 String으로 관리해도 돼?
A. 가능하지만 오타와 비교 오류를 줄이려면 Enum 사용을 검토하는 것이 좋다.

Q. 금액 계산에 double을 써도 돼?
A. 정밀도 문제가 생길 수 있으므로 BigDecimal 또는 최소 단위 정수 계산을 검토하는 것이 좋다.

Q. Java Anti Pattern은 어떻게 찾는 게 좋아?
A. 증상을 보고 책임, null, 타입, 예외, Collection, OOP 기준으로 원인을 좁히면 된다.

Q. NPE가 나면 무엇부터 확인해?
A. 발생 라인의 null 참조, Repository 결과 처리, Optional.get, DTO Field 누락, null 반환을 확인한다.

Q. ClassCastException이 나면 무엇을 확인해?
A. Raw Type, Object 반환, 잘못된 Casting, Generic Type 누락을 확인한다.

Q. Review Agent 출력은 어떻게 구성해?
A. Summary, Critical Issues, Major Issues, Minor Issues, Checklist Result, Final Recommendation 형식이 좋다.

Q. Java Part08은 어떤 Agent가 사용해?
A. Backend Agent와 Review Agent가 Java 백엔드 코드 작성, 검토, Anti Pattern 탐지에 사용한다.
