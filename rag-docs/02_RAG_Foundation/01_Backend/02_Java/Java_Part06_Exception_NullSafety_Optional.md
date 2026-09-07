# Java Part06 — Exception, Null Safety, Optional

---

# 1. Exception Handling Foundation

## 1.1 Exception Purpose

### [개념]

Exception은 Java 프로그램 실행 중 발생한 비정상 상황을 표현하는 객체다.

Exception Handling은 오류 상황을 숨기는 것이 아니라, 오류 원인을 명확히 표현하고 적절한 계층에서 처리하기 위한 기준이다.

Backend Agent / Review Agent는 Exception을 기준으로 Service 실패 흐름, Domain Rule 위반, API Error Response, GlobalExceptionHandler 연결을 검토한다.

```java
throw new IllegalArgumentException("userId must not be null");
```

---

### [핵심]

Exception 핵심:

- Exception
- Error
- Checked Exception
- Unchecked Exception
- RuntimeException
- try-catch
- throws
- finally
- Custom Exception
- GlobalExceptionHandler
- Error Response
- Exception Message

Exception 처리 목적:

```text
오류 상황 명확화
실패 흐름 분리
비즈니스 규칙 위반 표현
복구 가능 여부 판단
API Error Response 변환
로그와 디버깅 지원
정상 흐름 가독성 유지
```

---

### [실무]

2026 백엔드 실무에서 Exception은 단순 오류 출력이 아니라 API 계약과 도메인 규칙의 일부다.

Exception 판단 Flow:

```text
Error Situation 발생
→ 복구 가능한가?
→ 호출자가 처리해야 하는가?
→ 현재 계층에서 처리할 것인가?
→ Custom Exception이 필요한가?
→ Log가 필요한가?
→ API Response로 변환할 것인가?
```

Spring Boot 연결:

```text
Controller
→ 요청 수신

Service
→ 비즈니스 예외 발생

Domain / Entity
→ 상태 규칙 위반 예외 발생

Repository
→ 조회 결과 없음 Optional 반환

GlobalExceptionHandler
→ Exception을 Error Response로 변환
```

주의:

- Exception을 삼키지 않는다.
- catch 후 빈 블록 금지.
- Exception Message는 원인 파악 가능하게 작성한다.
- 민감정보를 Exception Message나 Log에 포함하지 않는다.
- Controller에서 모든 예외를 직접 처리하지 않는다.
- 반복되는 오류 응답은 GlobalExceptionHandler로 통합한다.

---

### [FAQ]

Q. Exception Handling은 왜 중요해?
A. 오류 상황을 명확히 표현하고 API 실패 응답과 디버깅 품질을 높이기 위해 중요하다.

Q. Exception은 어디서 처리하는 게 좋아?
A. 비즈니스 오류는 Service나 Domain에서 발생시키고 API 응답 변환은 GlobalExceptionHandler에서 처리하는 것이 좋다.

Q. catch 후 아무것도 안 해도 돼?
A. 안 된다. 원인이 사라지지 않고 디버깅이 어려워진다.

---

## 1.2 Exception Hierarchy Rules

### [개념]

Java Exception 계층은 Throwable을 최상위로 Error와 Exception으로 나뉜다.

Application Code에서는 보통 Exception과 RuntimeException 계열을 다룬다.

```text
Throwable
├ Error
└ Exception
  ├ Checked Exception
  └ RuntimeException
```

---

### [핵심]

Exception 계층 핵심:

- Throwable
- Error
- Exception
- RuntimeException
- Checked Exception
- Unchecked Exception
- IOException
- SQLException
- IllegalArgumentException
- IllegalStateException
- NullPointerException

분류:

```text
Error
→ JVM 수준 심각한 오류
→ 일반 Application에서 복구 대상 아님

Checked Exception
→ 컴파일 시 처리 강제
→ IOException 등

Unchecked Exception
→ RuntimeException 계열
→ 비즈니스 예외와 프로그래밍 오류에 자주 사용
```

---

### [실무]

Spring Boot 백엔드에서는 비즈니스 예외를 RuntimeException 기반 Custom Exception으로 정의하는 경우가 많다.

예:

```java
public class UserNotFoundException extends RuntimeException {
    public UserNotFoundException(Long userId) {
        super("User not found. userId=" + userId);
    }
}
```

실무 기준:

- 복구 가능한 외부 I/O 오류는 Checked Exception 또는 명확한 RuntimeException 변환 검토.
- 비즈니스 규칙 위반은 Custom RuntimeException 검토.
- 프로그래밍 오류는 IllegalArgumentException / IllegalStateException 사용 가능.
- Error는 catch하지 않는 것이 일반적.
- Framework 예외는 GlobalExceptionHandler에서 필요한 것만 변환한다.

주의:

- RuntimeException만 무분별하게 던지지 않는다.
- Exception Type이 오류 의미를 표현해야 한다.
- 모든 예외를 Exception으로 뭉뚱그려 catch하지 않는다.
- Checked Exception을 RuntimeException으로 감쌀 때 원인 예외를 보존한다.

---

### [FAQ]

Q. Checked Exception과 Unchecked Exception 차이는?
A. Checked Exception은 컴파일 시 처리 강제가 있고 Unchecked Exception은 RuntimeException 계열로 컴파일 시 처리 강제가 없다.

Q. Error도 catch해야 해?
A. 일반 Application Code에서는 보통 catch하지 않는다. JVM 수준 심각한 오류인 경우가 많다.

Q. 비즈니스 예외는 Checked Exception으로 만들어야 해?
A. Spring Boot 실무에서는 RuntimeException 기반 Custom Exception으로 처리하는 경우가 많다.

---

## 1.3 Checked Exception Rules

### [개념]

Checked Exception은 컴파일 시점에 처리 또는 전파가 강제되는 Exception이다.

대표적으로 IOException, SQLException 등이 있다.

```java
public String readFile(Path path) throws IOException {
    return Files.readString(path);
}
```

---

### [핵심]

Checked Exception 핵심:

- Checked Exception
- Compile Time Check
- throws
- try-catch
- IOException
- SQLException
- Recoverable Error
- Exception Propagation

사용 의미:

```text
호출자가 오류를 인지해야 한다.
복구 가능성이 있다.
외부 자원 접근 실패 가능성이 있다.
API 계약상 실패를 명시한다.
```

---

### [실무]

Checked Exception 처리 예:

```java
public String loadTemplate(Path path) {
    try {
        return Files.readString(path);
    } catch (IOException e) {
        throw new TemplateLoadException("failed to load template", e);
    }
}
```

실무 기준:

- 외부 I/O 실패는 원인 예외를 보존한다.
- Service 계층에서는 도메인 의미가 있는 Custom Exception으로 변환할 수 있다.
- 단순히 throws를 계속 전파하면 호출부가 복잡해질 수 있다.
- catch 후 RuntimeException으로 감쌀 때 cause를 반드시 포함한다.
- 복구 로직이 가능하면 catch에서 복구한다.

주의:

- Checked Exception을 무조건 나쁜 것으로 보지 않는다.
- 의미 없는 try-catch로 코드만 감싸지 않는다.
- IOException 메시지에 경로 등 민감정보가 포함될 수 있는지 확인한다.
- SQLException을 Controller까지 그대로 노출하지 않는다.

---

### [FAQ]

Q. Checked Exception은 왜 불편해?
A. 호출자가 반드시 처리하거나 전파해야 해서 코드가 길어질 수 있다.

Q. Checked Exception을 RuntimeException으로 바꿔도 돼?
A. 가능하지만 도메인 의미가 있는 Custom Exception으로 감싸고 원인 예외를 보존하는 것이 좋다.

Q. catch에서 cause를 왜 넣어야 해?
A. 원래 오류 원인을 추적할 수 있어 디버깅에 필요하기 때문이다.

---

## 1.4 Unchecked Exception Rules

### [개념]

Unchecked Exception은 RuntimeException 계열로 컴파일 시점에 처리 강제가 없는 Exception이다.

비즈니스 규칙 위반, 잘못된 입력, 잘못된 상태, 프로그래밍 오류에 자주 사용된다.

---

### [핵심]

Unchecked Exception 핵심:

- Unchecked Exception
- RuntimeException
- IllegalArgumentException
- IllegalStateException
- NullPointerException
- Custom RuntimeException
- Business Exception
- Programming Error

대표 사용:

```text
잘못된 Parameter → IllegalArgumentException
잘못된 객체 상태 → IllegalStateException
리소스 없음 → Custom NotFoundException
중복 데이터 → Custom DuplicateException
권한 없음 → Custom ForbiddenException
```

---

### [실무]

잘못된 입력:

```java
public void changeEmail(String email) {
    if (email == null || email.isBlank()) {
        throw new IllegalArgumentException("email must not be blank");
    }

    this.email = email;
}
```

잘못된 상태:

```java
public void publish() {
    if (this.status != PostStatus.DRAFT) {
        throw new IllegalStateException("only draft post can be published");
    }

    this.status = PostStatus.PUBLISHED;
}
```

실무 기준:

- 입력값 오류와 상태 오류를 구분한다.
- 비즈니스 의미가 중요하면 Custom Exception을 만든다.
- Unchecked Exception도 문서화와 테스트가 필요하다.
- GlobalExceptionHandler에서 API Error Response로 변환한다.
- Domain Method에서 상태 규칙 위반을 표현할 수 있다.

주의:

- RuntimeException만 던지면 오류 의미가 약하다.
- 모든 오류를 IllegalArgumentException으로 처리하지 않는다.
- NPE를 의도적으로 비즈니스 예외처럼 사용하지 않는다.
- 예외 메시지에 비밀번호, 토큰, 개인정보를 포함하지 않는다.

---

### [FAQ]

Q. IllegalArgumentException은 언제 써?
A. Method에 전달된 인자가 잘못되었을 때 사용한다.

Q. IllegalStateException은 언제 써?
A. 객체 상태가 현재 작업을 수행하기에 부적절할 때 사용한다.

Q. RuntimeException은 처리하지 않아도 돼?
A. 컴파일 강제는 없지만 API 응답과 로그 정책상 적절히 처리해야 한다.

---

# 2. Custom Exception Rules

## 2.1 Custom Exception Purpose

### [개념]

Custom Exception은 도메인이나 비즈니스 상황을 명확히 표현하기 위해 직접 정의하는 Exception이다.

기본 Exception만으로 오류 의미가 부족할 때 사용한다.

```java
public class UserNotFoundException extends RuntimeException {
    public UserNotFoundException(Long userId) {
        super("User not found. userId=" + userId);
    }
}
```

---

### [핵심]

Custom Exception 핵심:

- Custom Exception
- Domain Exception
- Business Exception
- NotFoundException
- DuplicateException
- InvalidStateException
- ForbiddenException
- ErrorCode
- Error Response

사용 대상:

```text
리소스 없음
중복 값
권한 없음
인증 실패
비즈니스 규칙 위반
지원하지 않는 상태
외부 API 실패
도메인 상태 전이 실패
```

---

### [실무]

Custom Exception 예:

```java
public class DuplicateEmailException extends RuntimeException {
    public DuplicateEmailException(String email) {
        super("Duplicate email. email=" + email);
    }
}
```

상태 예외:

```java
public class InvalidPostStateException extends RuntimeException {
    public InvalidPostStateException(String message) {
        super(message);
    }
}
```

실무 기준:

- Exception 이름은 상황을 명확히 표현한다.
- 메시지는 원인 식별에 필요한 최소 정보를 포함한다.
- 민감정보는 포함하지 않는다.
- 반복적으로 처리할 오류는 ErrorCode와 연결 가능.
- API 응답 변환은 GlobalExceptionHandler에서 처리한다.
- Service / Domain 계층에서 발생 가능하다.

주의:

- 모든 오류마다 Custom Exception을 만들 필요는 없다.
- 단순 입력값 오류는 IllegalArgumentException으로 충분할 수 있다.
- Custom Exception이 너무 많으면 관리 비용이 증가한다.
- Exception 계층 구조는 단순하게 유지한다.

---

### [FAQ]

Q. Custom Exception은 언제 만들어?
A. 기본 Exception만으로 비즈니스 오류 의미가 명확하지 않을 때 만든다.

Q. 모든 오류마다 Custom Exception을 만들어야 해?
A. 아니다. 의미 있는 도메인 오류나 반복적으로 처리할 오류에 우선 적용한다.

Q. Custom Exception 이름은 어떻게 지어?
A. UserNotFoundException, DuplicateEmailException처럼 오류 상황이 드러나게 짓는다.

---

## 2.2 ErrorCode Based Exception Rules

### [개념]

ErrorCode 기반 Exception은 오류 유형을 코드로 관리하고 API Error Response와 연결하는 방식이다.

Spring Boot API에서 일관된 오류 응답을 만들 때 사용한다.

---

### [핵심]

ErrorCode 핵심:

- ErrorCode
- Error Response
- HTTP Status
- Error Message
- Business Error
- GlobalExceptionHandler
- API Contract
- Client Handling

구성 예:

```text
ErrorCode
→ code
→ message
→ HTTP status
→ Exception
→ ErrorResponse
```

---

### [실무]

ErrorCode 예:

```java
public enum ErrorCode {
    USER_NOT_FOUND("USER_NOT_FOUND", "User not found"),
    DUPLICATE_EMAIL("DUPLICATE_EMAIL", "Duplicate email"),
    INVALID_REQUEST("INVALID_REQUEST", "Invalid request");

    private final String code;
    private final String message;

    ErrorCode(String code, String message) {
        this.code = code;
        this.message = message;
    }
}
```

BusinessException 예:

```java
public class BusinessException extends RuntimeException {
    private final ErrorCode errorCode;

    public BusinessException(ErrorCode errorCode) {
        super(errorCode.name());
        this.errorCode = errorCode;
    }

    public ErrorCode getErrorCode() {
        return errorCode;
    }
}
```

사용:

```java
throw new BusinessException(ErrorCode.USER_NOT_FOUND);
```

주의:

- ErrorCode 메시지와 사용자 노출 메시지를 분리할 수 있다.
- ErrorCode가 너무 세분화되면 관리가 어려워진다.
- HTTP Status와 비즈니스 코드 기준을 일관되게 유지한다.
- ErrorCode 이름은 API 클라이언트가 이해 가능한 수준으로 작성한다.

---

### [FAQ]

Q. ErrorCode는 왜 써?
A. API 오류 응답을 일관되게 만들고 클라이언트가 오류 유형을 구분할 수 있게 하기 위해 사용한다.

Q. 모든 Exception에 ErrorCode가 필요해?
A. API 응답으로 노출되는 반복적인 비즈니스 오류에는 유용하지만 모든 내부 오류에 필요하지는 않다.

Q. ErrorCode 메시지를 그대로 사용자에게 보여줘도 돼?
A. 서비스 정책에 따라 다르며 내부 메시지와 사용자 노출 메시지를 분리하는 것이 안전할 수 있다.

---

## 2.3 Exception Message Rules

### [개념]

Exception Message는 오류 원인을 사람이 추적할 수 있도록 제공하는 설명이다.

Message는 디버깅에 도움이 되어야 하지만 민감정보를 노출하면 안 된다.

---

### [핵심]

Exception Message 핵심:

- Clear Message
- Cause Identification
- Safe Information
- No Sensitive Data
- Context
- Debugging
- Error Log

좋은 메시지 조건:

```text
오류 원인이 드러난다.
필요한 식별자가 있다.
민감정보가 없다.
너무 길지 않다.
일관된 형식이다.
```

---

### [실무]

좋은 예:

```java
throw new UserNotFoundException("User not found. userId=" + userId);
```

나쁜 예:

```java
throw new RuntimeException("error");
```

민감정보 위험:

```java
throw new LoginFailedException("password=" + rawPassword);
```

권장:

```java
throw new LoginFailedException("Login failed. email=" + email);
```

주의:

- Password, Token, Authorization Header, 주민번호, 카드번호 등은 메시지에 포함하지 않는다.
- 외부 API 원문 응답을 그대로 노출하지 않는다.
- 사용자에게 노출되는 메시지와 내부 로그 메시지를 구분한다.
- 너무 상세한 내부 구조를 API 응답에 드러내지 않는다.

---

### [FAQ]

Q. Exception Message에는 무엇을 넣어야 해?
A. 오류 원인을 식별할 수 있는 최소 정보와 안전한 식별자를 넣는다.

Q. 비밀번호나 토큰을 Exception Message에 넣어도 돼?
A. 안 된다. 민감정보는 메시지와 로그에 포함하지 않아야 한다.

Q. RuntimeException("error")처럼 써도 돼?
A. 권장하지 않는다. 원인 파악이 어려워진다.

---

# 3. try-catch Rules

## 3.1 try-catch Purpose

### [개념]

try-catch는 예외가 발생할 수 있는 코드를 감싸고 예외 발생 시 대체 흐름을 실행하는 문법이다.

try-catch는 오류를 숨기기 위한 도구가 아니라 복구, 변환, 로깅, 자원 정리를 위한 도구다.

---

### [핵심]

try-catch 핵심:

- try
- catch
- finally
- try-with-resources
- Exception Conversion
- Recovery
- Logging
- Resource Cleanup
- Cause Preservation

사용 목적:

```text
복구 가능한 오류 처리
외부 예외를 도메인 예외로 변환
자원 정리
로그 기록
fallback 처리
```

---

### [실무]

Exception 변환 예:

```java
public PaymentResult approve(PaymentCommand command) {
    try {
        return paymentClient.approve(command);
    } catch (ExternalApiException e) {
        throw new PaymentApproveFailedException("payment approve failed", e);
    }
}
```

복구 예:

```java
public String getDisplayName(User user) {
    try {
        return profileClient.getDisplayName(user.getId());
    } catch (ProfileUnavailableException e) {
        return user.getNickname();
    }
}
```

주의:

- catch 후 아무것도 하지 않는다.
- 너무 넓은 Exception을 catch하지 않는다.
- 원인 예외를 잃어버리지 않는다.
- 복구 불가능한 예외를 억지로 복구하지 않는다.
- catch에서 또 다른 예외가 발생할 가능성을 검토한다.

---

### [FAQ]

Q. try-catch는 언제 써?
A. 복구, 예외 변환, 로깅, 자원 정리가 필요한 경우 사용한다.

Q. catch에서 아무것도 안 하면 안 돼?
A. 안 된다. 오류 원인이 사라지지 않고 추적이 어려워진다.

Q. 모든 예외를 Exception으로 catch해도 돼?
A. 권장하지 않는다. 필요한 구체 예외를 처리하는 것이 좋다.

---

## 3.2 finally and try-with-resources Rules

### [개념]

finally는 예외 발생 여부와 관계없이 실행되는 블록이다.

try-with-resources는 AutoCloseable 자원을 자동으로 닫아주는 문법이다.

---

### [핵심]

자원 정리 핵심:

- finally
- try-with-resources
- AutoCloseable
- Resource Cleanup
- File Stream
- Connection
- Close
- Suppressed Exception

---

### [실무]

try-with-resources 예:

```java
public String read(Path path) {
    try (BufferedReader reader = Files.newBufferedReader(path)) {
        return reader.readLine();
    } catch (IOException e) {
        throw new FileReadException("failed to read file", e);
    }
}
```

finally 예:

```java
Lock lock = new ReentrantLock();

lock.lock();
try {
    process();
} finally {
    lock.unlock();
}
```

실무 기준:

- Close가 필요한 자원은 try-with-resources 우선.
- Lock 해제는 finally 사용.
- finally에서 예외가 발생하지 않게 주의.
- DB Connection은 보통 DataSource / Transaction Manager가 관리한다.
- 직접 자원 관리가 필요한지 먼저 확인한다.

주의:

- finally에서 return 하지 않는다.
- finally에서 원래 예외를 덮어쓸 수 있다.
- AutoCloseable 구현체는 close 동작을 확인한다.
- Spring 환경에서는 Framework가 관리하는 자원을 직접 닫지 않는다.

---

### [FAQ]

Q. try-with-resources는 언제 써?
A. 파일, 스트림, Reader처럼 close가 필요한 AutoCloseable 자원을 사용할 때 쓴다.

Q. finally는 언제 필요해?
A. 예외 발생 여부와 관계없이 반드시 실행해야 하는 정리 작업이 있을 때 사용한다.

Q. finally에서 return 해도 돼?
A. 권장하지 않는다. 예외 흐름을 숨길 수 있다.

---

# 4. Layered Exception Handling

## 4.1 Controller Exception Rules

### [개념]

Controller는 HTTP 요청과 응답의 진입점이다.

Controller에서 비즈니스 예외를 직접 try-catch로 반복 처리하기보다 GlobalExceptionHandler에 위임하는 것이 일반적이다.

---

### [핵심]

Controller Exception 핵심:

- Controller
- Request Validation
- Binding Error
- MethodArgumentNotValidException
- GlobalExceptionHandler
- Error Response
- HTTP Status
- API Boundary

Controller 역할:

```text
요청 수신
입력 DTO Validation 연결
Service 호출
성공 응답 반환
예외 직접 처리 최소화
```

---

### [실무]

나쁜 예:

```java
@GetMapping("/users/{userId}")
public ApiResponse<UserResponse> getUser(@PathVariable Long userId) {
    try {
        return ApiResponse.success(userService.getUser(userId));
    } catch (UserNotFoundException e) {
        return ApiResponse.fail("not found");
    }
}
```

좋은 예:

```java
@GetMapping("/users/{userId}")
public ApiResponse<UserResponse> getUser(@PathVariable Long userId) {
    return ApiResponse.success(userService.getUser(userId));
}
```

예외 변환:

```text
UserNotFoundException
→ GlobalExceptionHandler
→ 404 ErrorResponse
```

주의:

- Controller마다 같은 try-catch를 반복하지 않는다.
- Binding / Validation 오류는 별도 Handler에서 처리한다.
- 인증 / 인가 예외는 Security Handler와 역할을 구분한다.
- Controller에 비즈니스 예외 변환 로직을 넣지 않는다.

---

### [FAQ]

Q. Controller에서 try-catch를 많이 써도 돼?
A. 권장하지 않는다. 반복되는 예외 변환은 GlobalExceptionHandler로 처리하는 것이 좋다.

Q. Controller는 예외를 어디까지 처리해?
A. 보통 직접 처리하지 않고 Service 예외를 전파해 GlobalExceptionHandler가 응답으로 변환하게 한다.

Q. Validation Error는 어디서 처리해?
A. MethodArgumentNotValidException 등을 GlobalExceptionHandler에서 처리할 수 있다.

---

## 4.2 Service Exception Rules

### [개념]

Service는 비즈니스 흐름과 Transaction 단위를 담당하며, 비즈니스 실패 상황을 명확한 Exception으로 표현한다.

Repository 조회 실패, 권한 부족, 중복, 잘못된 상태는 Service에서 예외로 변환될 수 있다.

---

### [핵심]

Service Exception 핵심:

- Service
- Business Exception
- Transaction
- Repository Result
- Optional orElseThrow
- Authorization Check
- Duplicate Check
- Invalid State
- External Failure

---

### [실무]

조회 실패:

```java
public User getUserOrThrow(Long userId) {
    return userRepository.findById(userId)
        .orElseThrow(() -> new UserNotFoundException(userId));
}
```

중복 확인:

```java
public void register(RegisterCommand command) {
    if (userRepository.existsByEmail(command.email())) {
        throw new DuplicateEmailException(command.email());
    }

    User user = User.create(command.email());
    userRepository.save(user);
}
```

권한 확인:

```java
public void updatePost(Long postId, Long userId, UpdatePostCommand command) {
    Post post = getPostOrThrow(postId);

    if (!post.isOwner(userId)) {
        throw new ForbiddenPostAccessException(postId, userId);
    }

    post.update(command.title(), command.content());
}
```

주의:

- Service에서 null 반환으로 실패를 표현하지 않는다.
- Optional.get 직접 호출 금지.
- Repository 결과 없음은 orElseThrow로 명확히 변환.
- Transaction Rollback 대상 예외인지 확인.
- 외부 API 실패와 DB 상태 변경 순서를 주의한다.

---

### [FAQ]

Q. Service에서 조회 결과가 없으면 어떻게 해?
A. Optional.orElseThrow로 명확한 Custom Exception으로 변환하는 것이 좋다.

Q. Service에서 null을 반환해도 돼?
A. 권장하지 않는다. 실패 상황은 Optional, Exception, Result Object 중 하나로 명확히 표현한다.

Q. 비즈니스 규칙 위반은 어디서 예외를 던져?
A. Service나 Domain Method에서 던지고 GlobalExceptionHandler에서 응답으로 변환한다.

---

## 4.3 Domain Exception Rules

### [개념]

Domain Exception은 Entity나 Domain Object가 자신의 상태 규칙을 위반했을 때 발생시키는 예외다.

Domain Method는 객체 Invariant를 보호하기 위해 예외를 사용할 수 있다.

---

### [핵심]

Domain Exception 핵심:

- Domain Exception
- Entity Method
- Invariant
- State Transition
- Invalid State
- Business Rule
- IllegalStateException
- Custom Domain Exception

---

### [실무]

상태 전이 예:

```java
public void publish() {
    if (this.status != PostStatus.DRAFT) {
        throw new InvalidPostStateException("only draft post can be published");
    }

    if (this.content == null || this.content.isBlank()) {
        throw new InvalidPostStateException("content must not be blank");
    }

    this.status = PostStatus.PUBLISHED;
}
```

포인트 검증:

```java
public void addPoint(int point) {
    if (point <= 0) {
        throw new IllegalArgumentException("point must be positive");
    }

    this.point += point;
}
```

실무 기준:

- 객체 자신의 상태 규칙은 Domain Method에서 검증.
- 상태 전이 실패는 IllegalStateException 또는 Custom Domain Exception.
- 입력값 자체 오류는 IllegalArgumentException 가능.
- Domain Exception도 API 응답 변환 정책과 연결.
- DTO Validation과 Domain Validation을 분리한다.

주의:

- Entity에서 Repository나 외부 API를 호출하지 않는다.
- Domain Exception 메시지에 내부 민감정보를 넣지 않는다.
- 복잡한 여러 Entity 협력 규칙은 Domain Service 검토.
- 예외를 사용하지 않고 boolean만 반환하면 실패 이유가 약해질 수 있다.

---

### [FAQ]

Q. Entity Method에서 Exception을 던져도 돼?
A. 객체 상태 규칙을 위반한 경우 가능하다.

Q. Domain Exception과 Service Exception 차이는?
A. Domain Exception은 객체 상태 규칙 위반이고 Service Exception은 Use Case 흐름 실패를 표현한다.

Q. DTO Validation이 있으면 Domain Exception은 필요 없어?
A. 아니다. 입력 검증과 도메인 상태 보호는 목적이 다르다.

---

## 4.4 GlobalExceptionHandler Rules

### [개념]

GlobalExceptionHandler는 Spring Boot에서 여러 Controller에 공통으로 적용되는 예외 처리 계층이다.

Exception을 일관된 API Error Response로 변환한다.

---

### [핵심]

GlobalExceptionHandler 핵심:

- @RestControllerAdvice
- @ExceptionHandler
- ErrorResponse
- HTTP Status
- Validation Error
- Business Exception
- Common Error Format
- API Contract

---

### [실무]

예:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleUserNotFound(UserNotFoundException e) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
            .body(ErrorResponse.of("USER_NOT_FOUND", e.getMessage()));
    }

    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<ErrorResponse> handleIllegalArgument(IllegalArgumentException e) {
        return ResponseEntity.badRequest()
            .body(ErrorResponse.of("INVALID_REQUEST", e.getMessage()));
    }
}
```

ErrorResponse 예:

```java
public record ErrorResponse(
    String code,
    String message
) {
    public static ErrorResponse of(String code, String message) {
        return new ErrorResponse(code, message);
    }
}
```

실무 기준:

- 예외별 HTTP Status를 명확히 매핑.
- Validation Error는 Field Error를 포함 가능.
- 내부 서버 오류는 상세 메시지 노출 제한.
- 공통 Error Response 구조를 유지.
- Logging Level을 오류 유형별로 구분.
- Security Exception은 Security Handler와 역할 구분.

주의:

- 모든 Exception을 500으로 처리하지 않는다.
- Exception Message를 그대로 사용자에게 노출할지 검토한다.
- Throwable 전체를 무분별하게 잡지 않는다.
- Handler 순서와 예외 상속 관계를 고려한다.

---

### [FAQ]

Q. GlobalExceptionHandler는 왜 필요해?
A. 여러 Controller의 예외 응답을 일관된 형식으로 변환하기 위해 필요하다.

Q. 모든 예외를 500으로 보내도 돼?
A. 안 된다. 비즈니스 오류, 입력 오류, 인증 오류, 서버 오류를 구분해야 한다.

Q. Exception Message를 API 응답에 그대로 넣어도 돼?
A. 민감정보와 내부 구조 노출 가능성을 검토해야 한다.

---

# 5. Null Safety Foundation

## 5.1 Null Safety Purpose

### [개념]

Null Safety는 null로 인해 발생하는 NullPointerException을 예방하고 값 부재를 명확히 표현하는 기준이다.

Java Reference Type은 null을 가질 수 있으므로 Backend 코드에서 항상 null 가능성을 검토해야 한다.

---

### [핵심]

Null Safety 핵심:

- null
- NullPointerException
- Reference Type
- Required Value
- Optional Value
- Null Check
- Guard Clause
- Objects.requireNonNull
- Empty Collection
- Optional
- Validation

Null 발생 위치:

```text
Request DTO Field 누락
Repository 조회 결과 없음
외부 API 응답 누락
Entity Field nullable
Map.get 결과 없음
Optional.get 직접 호출
Method Chain 중간값 null
Collection 반환 null
```

---

### [실무]

Null Safety Flow:

```text
값이 필수인가?
→ 생성자 / Validation에서 검증

값이 없을 수 있는가?
→ Optional / nullable 정책 명확화

Collection인가?
→ null보다 empty collection 반환

Repository 조회인가?
→ Optional.orElseThrow 사용

외부 API 응답인가?
→ null-safe mapping 검토
```

필수 값 검증:

```java
public User(String email) {
    this.email = Objects.requireNonNull(email, "email must not be null");
}
```

Guard Clause:

```java
public void updateEmail(String email) {
    if (email == null || email.isBlank()) {
        throw new IllegalArgumentException("email must not be blank");
    }

    this.email = email;
}
```

주의:

- null 가능성을 오래 전달하지 않는다.
- null 반환 정책을 숨기지 않는다.
- null check를 반복하면 설계 개선 후보일 수 있다.
- Collection은 null보다 empty collection을 우선 검토.
- Optional을 모든 null 문제 해결 도구로 오해하지 않는다.

---

### [FAQ]

Q. NullPointerException은 왜 생겨?
A. 참조 변수가 null인 상태에서 Method나 Field에 접근하기 때문이다.

Q. NPE를 줄이려면 어떻게 해?
A. 필수 값 검증, Optional 반환 처리, empty collection 반환, DTO Validation을 적용한다.

Q. null check가 많으면 좋은 코드야?
A. 반드시 그렇지는 않다. null 가능성이 너무 넓게 퍼진 설계일 수 있다.

---

## 5.2 Required Value Rules

### [개념]

Required Value는 객체나 Method가 정상 동작하기 위해 반드시 필요한 값이다.

Required Value는 가능한 초기에 검증해 null 상태가 내부로 퍼지지 않게 해야 한다.

---

### [핵심]

Required Value 핵심:

- Required Value
- Non Null
- Precondition
- Constructor Validation
- Method Parameter Validation
- Guard Clause
- Objects.requireNonNull
- Fail Fast

검증 위치:

```text
Constructor
Static Factory Method
Service Method 초반
Domain Method 초반
DTO Validation
```

---

### [실무]

Constructor 검증:

```java
public Email(String value) {
    this.value = Objects.requireNonNull(value, "email must not be null");
}
```

Parameter 검증:

```java
public User getUser(Long userId) {
    if (userId == null) {
        throw new IllegalArgumentException("userId must not be null");
    }

    return userRepository.findById(userId)
        .orElseThrow(() -> new UserNotFoundException(userId));
}
```

DTO Validation:

```java
public record CreateUserRequest(
    @NotBlank String email,
    @NotBlank String password
) {
}
```

주의:

- Required Value를 null로 허용하지 않는다.
- 필수값 검증을 나중으로 미루면 오류 위치가 흐려진다.
- `Objects.requireNonNull` 메시지는 명확히 작성한다.
- DTO Validation과 Service 검증의 중복 기준을 팀에서 정한다.

---

### [FAQ]

Q. 필수 값 null 검증은 어디서 해?
A. 생성자, Factory Method, Service Method 초반, DTO Validation에서 빠르게 처리하는 것이 좋다.

Q. Objects.requireNonNull은 언제 써?
A. 필수 Reference 값이 null이면 즉시 실패시켜야 할 때 사용한다.

Q. 필수값 검증을 늦게 하면 뭐가 문제야?
A. 오류 발생 위치가 멀어져 원인 추적이 어려워진다.

---

## 5.3 Optional Value Rules

### [개념]

Optional Value는 값이 있을 수도 있고 없을 수도 있는 값이다.

Optional Value는 nullable Field, 외부 응답 누락, 검색 결과 없음, 선택 입력값 등에서 발생한다.

---

### [핵심]

Optional Value 핵심:

- Optional Value
- Nullable Value
- Absent Value
- Default Value
- Optional
- Null Policy
- orElse
- orElseGet
- orElseThrow

표현 방식:

```text
Method 반환 → Optional<T> 가능
Collection 반환 → empty collection 권장
DTO Field → null 허용 가능
Entity Field → DB nullable 정책과 일치
내부 계산 → 기본값 또는 명확한 검증
```

---

### [실무]

Default Value:

```java
String nickname = request.nickname() == null
    ? "anonymous"
    : request.nickname();
```

Optional 반환:

```java
public Optional<User> findByEmail(String email) {
    return userRepository.findByEmail(email);
}
```

Service 변환:

```java
public User getByEmail(String email) {
    return userRepository.findByEmail(email)
        .orElseThrow(() -> new UserNotFoundException(email));
}
```

주의:

- 값이 없을 수 있다는 사실을 숨기지 않는다.
- Optional Value를 null과 섞어 사용하지 않는다.
- Optional Field는 일반적으로 지양.
- 빈 문자열과 null의 의미를 구분한다.
- DB nullable과 Java 타입 정책을 일관되게 유지한다.

---

### [FAQ]

Q. 값이 없을 수 있으면 무조건 Optional을 써?
A. 아니다. 단일 반환에는 Optional이 적합할 수 있지만 Collection은 empty collection이 보통 더 좋다.

Q. DTO Field는 null이어도 돼?
A. 선택 입력값이라면 가능하지만 Validation과 기본값 정책을 명확히 해야 한다.

Q. null과 empty string은 같아?
A. 아니다. null은 값 없음이고 empty string은 길이 0인 문자열이다.

---

## 5.4 Empty Collection Rules

### [개념]

Collection 반환에서 값이 없음을 null로 표현하지 않고 빈 Collection으로 표현하는 것이 일반적으로 안전하다.

Empty Collection은 호출자의 null check 부담을 줄인다.

---

### [핵심]

Empty Collection 핵심:

- Empty List
- Empty Set
- Empty Map
- Null Safety
- No Result
- List.of
- Set.of
- Map.of
- Collections.emptyList

권장:

```text
조회 결과 없음 → empty List
중복 집합 없음 → empty Set
Key-Value 결과 없음 → empty Map
Collection Parameter null → 검증 또는 empty 변환
```

---

### [실무]

좋은 예:

```java
public List<UserResponse> getUsers() {
    return List.of();
}
```

Repository 결과 변환:

```java
public List<UserResponse> getActiveUsers() {
    return userRepository.findByActiveTrue().stream()
        .map(UserResponse::from)
        .toList();
}
```

주의:

- 반환은 empty collection 권장.
- 입력 Parameter가 null이면 필수 여부에 따라 예외 또는 empty 변환.
- `List.of()`는 수정 불가 List다.
- 호출자가 수정해야 하면 new ArrayList<>()가 필요할 수 있다.
- null Collection 반환은 NPE 위험을 높인다.

---

### [FAQ]

Q. Collection 반환값은 null이 좋아 empty collection이 좋아?
A. 대부분 empty collection이 좋다.

Q. List.of()는 수정 가능해?
A. 아니다. 수정 불가 List다.

Q. 입력 Collection이 null이면 어떻게 해?
A. 필수 입력이면 예외를 던지고 선택 입력이면 empty collection으로 변환할 수 있다.

---

# 6. Optional Foundation

## 6.1 Optional Purpose

### [개념]

Optional은 값이 있을 수도 없을 수도 있음을 반환 타입에서 명시하기 위한 Container다.

Optional은 null을 완전히 없애는 도구가 아니라 값 부재를 명확히 표현하는 도구다.

```java
Optional<User> user = userRepository.findById(userId);
```

---

### [핵심]

Optional 핵심:

- Optional
- Optional.empty
- Optional.of
- Optional.ofNullable
- isPresent
- ifPresent
- map
- flatMap
- filter
- orElse
- orElseGet
- orElseThrow

사용 목적:

```text
단일 반환값 부재 표현
Repository 조회 결과 표현
null 반환 대체
호출자에게 값 없음 가능성 명시
orElseThrow로 예외 변환
```

---

### [실무]

Repository 조회:

```java
User user = userRepository.findById(userId)
    .orElseThrow(() -> new UserNotFoundException(userId));
```

Optional 생성:

```java
Optional<String> nickname = Optional.ofNullable(request.nickname());
```

값 변환:

```java
String displayName = userRepository.findById(userId)
    .map(User::getNickname)
    .orElse("anonymous");
```

권장:

- Method 반환 타입에 사용.
- Repository find 결과에 사용.
- `get()` 직접 호출 지양.
- `orElseThrow()`로 명확한 예외 변환.
- Optional 내부에 null을 넣지 않는다.

주의:

- Field에 Optional 저장 지양.
- Parameter로 Optional 받기 지양.
- Collection 반환에 Optional<List<T>> 지양.
- Optional이 복잡한 흐름을 만들면 일반 if문이 더 낫다.
- Optional은 직렬화 DTO Field로 부적합한 경우가 많다.

---

### [FAQ]

Q. Optional은 언제 써?
A. 값이 없을 수 있는 단일 반환 결과를 명시할 때 사용한다.

Q. Optional은 null을 완전히 없애는 도구야?
A. 아니다. 값 부재를 명확히 표현하는 도구다.

Q. Optional을 Entity Field로 써도 돼?
A. 권장하지 않는다. Optional은 주로 반환 타입에 사용하는 것이 적합하다.

---

## 6.2 Optional Creation Rules

### [개념]

Optional 생성은 값의 null 가능성에 따라 `of`, `ofNullable`, `empty`를 선택한다.

잘못 선택하면 NullPointerException이 발생할 수 있다.

---

### [핵심]

Optional 생성 Method:

```text
Optional.of(value)
→ value가 null이면 NPE

Optional.ofNullable(value)
→ value가 null이면 Optional.empty

Optional.empty()
→ 빈 Optional 생성
```

---

### [실무]

null 불가능 값:

```java
Optional<String> email = Optional.of("user@example.com");
```

null 가능 값:

```java
Optional<String> nickname = Optional.ofNullable(request.nickname());
```

빈 결과:

```java
return Optional.empty();
```

실무 기준:

- null 가능성이 있으면 ofNullable 사용.
- null 불가능이 보장되면 of 사용 가능.
- Optional을 반환하는 Method에서 null을 반환하지 않는다.
- Optional.empty()로 값 없음을 표현한다.

나쁜 예:

```java
public Optional<User> findUser(Long userId) {
    return null;
}
```

좋은 예:

```java
public Optional<User> findUser(Long userId) {
    return Optional.empty();
}
```

주의:

- Optional.of(null)은 NPE 발생.
- Optional 자체를 null로 반환하면 Optional 사용 의미가 사라진다.
- Optional 생성 남용으로 코드가 복잡해지지 않게 한다.

---

### [FAQ]

Q. Optional.of와 ofNullable 차이는?
A. of는 null이면 NPE가 발생하고 ofNullable은 null이면 Optional.empty를 반환한다.

Q. Optional을 반환하는 Method에서 null을 반환해도 돼?
A. 안 된다. 값이 없으면 Optional.empty를 반환해야 한다.

Q. Optional.empty는 언제 써?
A. 값이 없음을 명시적으로 반환할 때 사용한다.

---

## 6.3 Optional Retrieval Rules

### [개념]

Optional Retrieval은 Optional 내부 값을 안전하게 꺼내거나 값이 없을 때 대체 흐름을 처리하는 방식이다.

`get()` 직접 호출은 값이 없을 때 예외가 발생하므로 지양한다.

---

### [핵심]

Optional Retrieval 핵심:

- get
- isPresent
- ifPresent
- orElse
- orElseGet
- orElseThrow
- NoSuchElementException
- Default Value
- Exception Conversion

권장 우선순위:

```text
값 없으면 예외 → orElseThrow
기본값 필요 → orElse / orElseGet
값 있을 때만 실행 → ifPresent
값 변환 → map
직접 get → 지양
```

---

### [실무]

orElseThrow:

```java
User user = userRepository.findById(userId)
    .orElseThrow(() -> new UserNotFoundException(userId));
```

orElse:

```java
String nickname = optionalNickname.orElse("anonymous");
```

orElseGet:

```java
String nickname = optionalNickname.orElseGet(() -> createDefaultNickname());
```

ifPresent:

```java
optionalUser.ifPresent(user -> notificationService.send(user));
```

나쁜 예:

```java
User user = userRepository.findById(userId).get();
```

주의:

- `get()` 직접 호출 금지에 가깝게 검토.
- orElse는 값이 있어도 인자가 먼저 평가될 수 있다.
- 비용 있는 기본값은 orElseGet 사용.
- isPresent 후 get 패턴은 orElseThrow / map으로 개선 가능.
- Optional 흐름이 복잡하면 일반 if문이 더 명확할 수 있다.

---

### [FAQ]

Q. Optional.get()을 바로 써도 돼?
A. 권장하지 않는다. 값이 없으면 NoSuchElementException이 발생한다.

Q. orElse와 orElseGet 차이는?
A. orElse는 기본값 표현식이 즉시 평가될 수 있고 orElseGet은 값이 없을 때 Supplier가 실행된다.

Q. Repository findById 후에는 보통 어떻게 해?
A. Service에서 orElseThrow로 명확한 NotFound Exception으로 변환한다.

---

## 6.4 Optional map and flatMap Rules

### [개념]

Optional map은 Optional 내부 값이 있을 때 값을 변환한다.

Optional flatMap은 변환 결과가 다시 Optional일 때 중첩 Optional을 펼친다.

---

### [핵심]

Optional 변환 핵심:

- map
- flatMap
- filter
- Transformation
- Nested Optional
- Optional Chaining
- Null Safe Transform

차이:

```text
map
→ T를 R로 변환
→ Optional<R>

flatMap
→ T를 Optional<R>로 변환
→ Optional<R>
```

---

### [실무]

map 예:

```java
String email = userRepository.findById(userId)
    .map(User::getEmail)
    .orElse("unknown");
```

flatMap 예:

```java
Optional<Address> address = userRepository.findById(userId)
    .flatMap(User::getAddressOptional);
```

filter 예:

```java
User activeUser = userRepository.findById(userId)
    .filter(User::isActive)
    .orElseThrow(() -> new UserNotFoundException(userId));
```

주의:

- Optional Chain이 길어지면 가독성이 떨어질 수 있다.
- Domain 예외 메시지가 약해질 수 있다.
- 복잡한 조건은 if문과 Guard Clause가 더 명확할 수 있다.
- Optional 내부에서 side effect를 많이 수행하지 않는다.

---

### [FAQ]

Q. Optional map은 언제 써?
A. Optional 내부 값이 있을 때 다른 값으로 변환하고 싶을 때 사용한다.

Q. Optional flatMap은 언제 써?
A. 변환 결과가 다시 Optional일 때 중첩 Optional을 피하기 위해 사용한다.

Q. Optional filter는 언제 써?
A. 값이 있을 때 조건을 만족하는 경우만 유지하고 싶을 때 사용한다.

---

## 6.5 Optional Anti Pattern Rules

### [개념]

Optional Anti Pattern은 Optional을 반환값 부재 표현 목적을 넘어 Field, Parameter, Collection, 복잡한 제어 흐름에 남용하는 문제다.

---

### [핵심]

Optional Anti Pattern:

- Optional Field
- Optional Parameter
- Optional<List<T>>
- Optional.get 직접 호출
- Optional 자체를 null로 반환
- isPresent 후 get 반복
- 복잡한 Optional Chain
- Side Effect 중심 Optional 사용

---

### [실무]

나쁜 예:

```java
public class User {
    private Optional<String> nickname;
}
```

권장:

```java
public class User {
    private String nickname;
}
```

나쁜 예:

```java
public void update(Optional<String> nickname) {
}
```

권장:

```java
public void updateNickname(String nickname) {
}
```

나쁜 예:

```java
public Optional<List<User>> findUsers() {
}
```

권장:

```java
public List<User> findUsers() {
}
```

주의:

- Optional은 주로 Method 반환 타입에 사용.
- Entity Field, DTO Field, Parameter에는 일반적으로 부적합.
- Collection은 empty collection으로 값 없음 표현.
- Optional을 쓰는 목적은 호출자에게 값 없음 가능성을 명확히 알리는 것이다.

---

### [FAQ]

Q. Optional을 Field로 써도 돼?
A. 권장하지 않는다. Optional은 주로 반환 타입에 사용하는 것이 적합하다.

Q. Optional을 Parameter로 받아도 돼?
A. 일반적으로 지양한다. Method Overloading이나 null 정책을 명확히 하는 것이 좋다.

Q. Optional<List<T>>는 좋은가?
A. 대부분 불필요하다. 결과가 없으면 empty List를 반환하는 것이 좋다.

---

# 7. NullPointerException Troubleshooting

## 7.1 NPE Cause Rules

### [개념]

NullPointerException은 null 참조에 Method 호출, Field 접근, 배열 접근 등을 수행할 때 발생하는 Runtime Exception이다.

NPE는 Java 백엔드에서 가장 흔한 오류 중 하나다.

---

### [핵심]

NPE 원인:

- 초기화되지 않은 Field
- Repository 조회 결과 없음
- Optional.get 직접 호출
- DTO Field null
- Map.get 결과 null
- 외부 API 응답 null
- Method Chain 중간값 null
- null Collection 반환
- Wrapper Type unboxing
- Boolean null 비교

---

### [실무]

NPE 예:

```java
String email = user.getEmail().toLowerCase();
```

user 또는 email이 null이면 NPE 발생 가능.

Wrapper unboxing 예:

```java
Boolean active = null;

if (active) {
    return true;
}
```

안전한 비교:

```java
if (Boolean.TRUE.equals(active)) {
    return true;
}
```

Debug Flow:

```text
Stack Trace 발생 라인 확인
→ null인 변수 확인
→ 값 생성 위치 확인
→ Repository / DTO / Mapping 확인
→ 필수 값 검증 추가
→ Optional / empty collection / default 처리 적용
```

주의:

- NPE를 catch해서 무시하지 않는다.
- 발생 라인을 정확히 확인한다.
- Method Chain은 중간 null을 추적하기 어렵다.
- null이 허용되는 값인지 먼저 정책을 정한다.

---

### [FAQ]

Q. NullPointerException이 나면 뭐부터 봐?
A. 스택트레이스의 발생 라인에서 어떤 참조가 null인지 먼저 확인한다.

Q. Boolean에서 NPE가 날 수 있어?
A. Boolean이 null인데 boolean으로 unboxing되면 NPE가 발생할 수 있다.

Q. NPE를 catch해서 처리하면 돼?
A. 보통은 원인 null 정책을 수정하는 것이 좋고 NPE를 흐름 제어로 사용하지 않는다.

---

## 7.2 NPE Prevention Rules

### [개념]

NPE Prevention은 null이 발생할 수 있는 경계를 명확히 하고 내부 코드로 null이 퍼지지 않도록 설계하는 것이다.

---

### [핵심]

NPE 예방 기준:

- Constructor Validation
- DTO Validation
- Guard Clause
- Optional orElseThrow
- Empty Collection
- Default Value
- Objects.requireNonNull
- Boolean.TRUE.equals
- Null Safe Mapping

---

### [실무]

DTO Validation:

```java
public record CreatePostRequest(
    @NotBlank String title,
    @NotBlank String content
) {
}
```

Repository Optional:

```java
Post post = postRepository.findById(postId)
    .orElseThrow(() -> new PostNotFoundException(postId));
```

Empty Collection:

```java
public List<CommentResponse> getComments(Long postId) {
    return commentRepository.findByPostId(postId).stream()
        .map(CommentResponse::from)
        .toList();
}
```

Null-safe equals:

```java
if (Objects.equals(request.userId(), post.getUserId())) {
    return true;
}
```

주의:

- 필수값은 가장 가까운 경계에서 검증.
- 외부 API 응답은 항상 신뢰하지 않는다.
- Mapper에서 null 정책을 명확히 한다.
- Optional을 Field로 확산하지 않는다.
- Collection을 null로 반환하지 않는다.

---

### [FAQ]

Q. NPE를 예방하는 가장 좋은 방법은?
A. 필수 값 검증, Optional 처리, empty collection 반환, null-safe 비교를 적용하는 것이다.

Q. 외부 API 응답은 null 체크해야 해?
A. 해야 한다. 외부 시스템 응답은 누락 가능성을 고려해야 한다.

Q. Method Chain이 길면 왜 위험해?
A. 중간 객체가 null일 때 어느 지점에서 NPE가 나는지 추적이 어려워진다.

---

# 8. Validation Connection

## 8.1 DTO Validation and Null Safety

### [개념]

DTO Validation은 API 요청 경계에서 잘못된 입력과 null 값을 차단하는 검증이다.

DTO Validation은 Bean Validation Annotation과 Controller 검증으로 연결된다.

---

### [핵심]

DTO Validation 핵심:

- DTO Validation
- Bean Validation
- @NotNull
- @NotBlank
- @NotEmpty
- @Size
- @Email
- @Valid
- Binding Error
- MethodArgumentNotValidException

Annotation 기준:

```text
@NotNull → null 금지
@NotBlank → null, 빈 문자열, 공백 문자열 금지
@NotEmpty → null, empty collection/string 금지
@Size → 길이 / 크기 제한
@Email → 이메일 형식 검증
```

---

### [실무]

Request DTO 예:

```java
public record CreateUserRequest(
    @NotBlank @Email String email,
    @NotBlank String password,
    @NotBlank String nickname
) {
}
```

Controller 예:

```java
@PostMapping("/users")
public ApiResponse<UserResponse> createUser(@Valid @RequestBody CreateUserRequest request) {
    return ApiResponse.success(userService.createUser(request));
}
```

실무 기준:

- Request DTO에서 입력 형식과 필수 여부 검증.
- Service에서 비즈니스 규칙 검증.
- Entity에서 도메인 상태 규칙 검증.
- Validation Error는 GlobalExceptionHandler에서 변환.
- `@NotBlank`와 `@NotNull` 차이를 구분한다.

주의:

- DTO Validation만으로 도메인 규칙을 모두 대체하지 않는다.
- `@NotBlank`는 String 전용에 가깝게 사용한다.
- Collection은 `@NotEmpty`나 `@Size` 검토.
- Nested DTO 검증에는 `@Valid` 필요.

---

### [FAQ]

Q. @NotNull과 @NotBlank 차이는?
A. @NotNull은 null만 금지하고 @NotBlank는 null, 빈 문자열, 공백 문자열을 금지한다.

Q. DTO Validation이 있으면 Service 검증은 필요 없어?
A. 아니다. DTO는 입력 형식 검증이고 Service는 비즈니스 규칙 검증을 담당한다.

Q. Validation Error는 어디서 응답으로 바꿔?
A. GlobalExceptionHandler에서 MethodArgumentNotValidException 등을 처리한다.

---

## 8.2 Service Validation Rules

### [개념]

Service Validation은 Use Case 실행에 필요한 비즈니스 조건을 검증하는 작업이다.

DTO Validation이 형식 검증이라면 Service Validation은 상태, 권한, 중복, 존재 여부를 검증한다.

---

### [핵심]

Service Validation 핵심:

- Business Validation
- Existence Check
- Duplicate Check
- Permission Check
- State Check
- Ownership Check
- Repository Query
- Custom Exception

검증 대상:

```text
사용자 존재 여부
게시글 존재 여부
이메일 중복 여부
권한 보유 여부
소유자 여부
현재 상태가 작업 가능한지
외부 API 처리 가능 여부
```

---

### [실무]

존재 검증:

```java
User user = userRepository.findById(userId)
    .orElseThrow(() -> new UserNotFoundException(userId));
```

중복 검증:

```java
if (userRepository.existsByEmail(command.email())) {
    throw new DuplicateEmailException(command.email());
}
```

소유자 검증:

```java
if (!post.isOwner(userId)) {
    throw new ForbiddenPostAccessException(postId, userId);
}
```

상태 검증은 Entity Method로 위임:

```java
post.publish();
```

주의:

- Service Validation을 Controller에 넣지 않는다.
- Repository가 비즈니스 판단을 담당하지 않게 한다.
- 검증 로직이 반복되면 private Method, Validator, Domain Service 검토.
- 존재 확인 후 저장 사이 Race Condition 가능성을 고려한다.
- DB Unique Constraint와 Application 중복 검증을 함께 검토한다.

---

### [FAQ]

Q. Service Validation은 무엇을 검증해?
A. 존재 여부, 중복, 권한, 소유자, 상태 같은 비즈니스 조건을 검증한다.

Q. 중복 검증은 Application에서만 하면 충분해?
A. 중요한 유일성은 DB Unique Constraint도 함께 검토해야 한다.

Q. 상태 검증은 Service와 Entity 중 어디가 좋아?
A. 객체 자신의 상태 전이 규칙이면 Entity Method로 표현하는 것이 좋다.

---

# 9. Exception and Optional Anti Pattern

## 9.1 Exception Anti Pattern

### [개념]

Exception Anti Pattern은 예외를 무시하거나, 흐름 제어에 남용하거나, 오류 의미를 불명확하게 만들어 유지보수성과 디버깅을 어렵게 하는 패턴이다.

---

### [핵심]

Exception Anti Pattern:

- catch 후 무시
- 빈 catch 블록
- RuntimeException만 무분별하게 사용
- Exception Message가 "error"
- 민감정보 메시지 포함
- 모든 예외를 Exception으로 catch
- Stack Trace만 출력하고 계속 진행
- 예외를 정상 흐름 제어에 남용
- 원인 예외 cause 누락
- Controller try-catch 반복
- 모든 API 오류를 500으로 반환

---

### [실무]

나쁜 예:

```java
try {
    process();
} catch (Exception e) {
}
```

나쁜 예:

```java
try {
    process();
} catch (Exception e) {
    e.printStackTrace();
}
```

좋은 예:

```java
try {
    process();
} catch (ExternalApiException e) {
    throw new ExternalServiceFailedException("external service failed", e);
}
```

검토 기준:

```text
catch가 필요한가?
복구 가능한가?
원인 예외를 보존했는가?
적절한 Exception Type인가?
민감정보가 없는가?
GlobalExceptionHandler와 연결되는가?
```

---

### [FAQ]

Q. 빈 catch 블록은 왜 안 좋아?
A. 오류가 사라진 것처럼 보여 실제 문제를 추적하기 어려워진다.

Q. e.printStackTrace만 하면 충분해?
A. 아니다. 운영 로그 정책과 예외 처리 흐름에 맞게 처리해야 한다.

Q. 모든 예외를 RuntimeException으로 바꿔도 돼?
A. 권장하지 않는다. 오류 의미가 명확한 Custom Exception이나 적절한 예외 타입을 사용해야 한다.

---

## 9.2 Null Safety Anti Pattern

### [개념]

Null Safety Anti Pattern은 null 가능성을 숨기거나 null을 흐름 제어로 남용해 NPE 위험과 코드 복잡도를 높이는 패턴이다.

---

### [핵심]

Null Safety Anti Pattern:

- null 반환 남용
- null Collection 반환
- Optional 대신 null 반환
- null check 반복
- Method Chain 중간 null 방치
- Boolean null unboxing
- Map.get null 처리 누락
- DTO Field 검증 누락
- Entity 필수 Field null 허용
- null 의미 불명확

---

### [실무]

나쁜 예:

```java
public List<User> findUsers() {
    return null;
}
```

좋은 예:

```java
public List<User> findUsers() {
    return List.of();
}
```

나쁜 예:

```java
public Optional<User> findUser(Long userId) {
    return null;
}
```

좋은 예:

```java
public Optional<User> findUser(Long userId) {
    return Optional.empty();
}
```

주의:

- null 의미를 문서 없이 숨기지 않는다.
- 필수값은 null 허용하지 않는다.
- Optional 자체를 null로 반환하지 않는다.
- 빈 결과는 empty collection으로 표현한다.
- Boolean은 `Boolean.TRUE.equals()`로 null-safe 비교 가능.

---

### [FAQ]

Q. null 반환은 무조건 나쁜가?
A. 항상은 아니지만 호출자 부담과 NPE 위험이 커져 Optional, empty collection, 명확한 예외를 우선 검토한다.

Q. Optional을 쓰면서 null을 반환하면 왜 문제야?
A. Optional의 목적이 값 없음 표현인데 null을 반환하면 호출자가 다시 NPE 위험에 노출된다.

Q. Boolean null은 어떻게 비교해?
A. `Boolean.TRUE.equals(value)`를 사용하면 null-safe하다.

---

## 9.3 Optional Anti Pattern

### [개념]

Optional Anti Pattern은 Optional을 부재 표현에 맞지 않게 사용하거나 Optional 사용으로 코드 가독성을 오히려 떨어뜨리는 패턴이다.

---

### [핵심]

Optional Anti Pattern:

- Optional.get 직접 호출
- Optional Field
- Optional Parameter
- Optional<List<T>>
- Optional 자체 null 반환
- isPresent 후 get 반복
- 복잡한 Optional Chain
- Optional로 Side Effect 처리 남용
- DTO Field Optional 사용

---

### [실무]

나쁜 예:

```java
if (optionalUser.isPresent()) {
    User user = optionalUser.get();
}
```

개선:

```java
User user = optionalUser
    .orElseThrow(() -> new UserNotFoundException(userId));
```

나쁜 예:

```java
optionalUser.ifPresent(user -> {
    user.updateName(name);
    userRepository.save(user);
    notificationService.send(user);
});
```

개선:

```java
User user = optionalUser
    .orElseThrow(() -> new UserNotFoundException(userId));

user.updateName(name);
userRepository.save(user);
notificationService.send(user);
```

주의:

- Optional은 흐름 제어 만능 도구가 아니다.
- 복잡한 비즈니스 흐름은 명시적 코드가 더 좋다.
- Side Effect가 많은 로직은 Optional Chain보다 Service 흐름으로 작성한다.
- Optional을 사용해도 예외 메시지와 실패 이유가 명확해야 한다.

---

### [FAQ]

Q. isPresent 후 get은 왜 안 좋아?
A. 더 안전하고 의도가 명확한 orElseThrow, map, ifPresent 등으로 표현할 수 있기 때문이다.

Q. Optional Chain이 길면 좋은 코드야?
A. 아니다. 길고 복잡하면 일반 if문이나 Guard Clause가 더 읽기 쉽다.

Q. Optional로 DB 저장 같은 Side Effect를 처리해도 돼?
A. 가능은 하지만 복잡한 비즈니스 흐름은 명시적으로 작성하는 것이 좋다.

---

# 10. Review Checklist

## 10.1 Exception Null Safety Optional Checklist

### [개념]

이 Checklist는 Backend Agent / Review Agent가 Java Exception, Null Safety, Optional 사용 품질을 검토하기 위한 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] Exception Type이 오류 의미를 명확히 표현하는가?
- [ ] Checked Exception과 Unchecked Exception 선택이 적절한가?
- [ ] Custom Exception이 필요한 비즈니스 오류를 명확히 표현하는가?
- [ ] 모든 오류에 불필요하게 Custom Exception을 만들지 않았는가?
- [ ] Exception Message가 원인 파악에 충분한가?
- [ ] Exception Message에 민감정보가 포함되지 않았는가?
- [ ] catch 후 빈 블록으로 예외를 무시하지 않는가?
- [ ] cause를 보존해야 하는 예외 변환에서 원인 예외를 포함했는가?
- [ ] Controller에서 반복 try-catch를 하지 않는가?
- [ ] GlobalExceptionHandler로 Error Response를 일관되게 변환하는가?
- [ ] 모든 API 오류를 500으로 처리하지 않는가?
- [ ] Required Value는 초기에 검증하는가?
- [ ] null 가능성이 내부 코드로 넓게 퍼지지 않는가?
- [ ] Collection 반환값으로 null을 반환하지 않는가?
- [ ] Optional 자체를 null로 반환하지 않는가?
- [ ] Optional.get 직접 호출을 피하는가?
- [ ] Optional Field를 사용하지 않는가?
- [ ] Optional Parameter를 사용하지 않는가?
- [ ] Optional<List<T>> 대신 empty List를 검토했는가?
- [ ] Boolean nullable 값 비교에 Boolean.TRUE.equals를 검토했는가?
- [ ] Map.get null 가능성을 처리했는가?
- [ ] DTO Validation과 Service Validation 역할이 분리되어 있는가?
- [ ] Entity / Domain Method가 자신의 상태 규칙을 보호하는가?
- [ ] NPE 발생 가능 Method Chain을 줄였는가?
- [ ] 외부 API 응답 null 가능성을 검토했는가?
```

---

### [실무]

Review Flow:

```text
Exception Type Review
→ Custom Exception Review
→ Message / Sensitive Data Review
→ try-catch Review
→ Layered Exception Review
→ Required Value Review
→ Optional Value Review
→ Empty Collection Review
→ Optional Usage Review
→ NPE Risk Review
→ Validation Role Review
→ Anti Pattern Review
```

리팩터링 후보:

```text
null 반환 → Optional / empty collection / Exception
Optional.get → orElseThrow
Optional<List<T>> → List<T>
Controller try-catch → GlobalExceptionHandler
RuntimeException("error") → 명확한 Custom Exception
빈 catch → 복구 / 변환 / 로깅
Boolean unboxing → Boolean.TRUE.equals
Map.get 미검증 → containsKey / null check / Optional 변환
```

---

### [FAQ]

Q. Exception 검수에서 가장 먼저 볼 것은?
A. Exception Type이 오류 의미를 명확히 표현하는지 먼저 확인한다.

Q. Null Safety 검수에서 가장 중요한 것은?
A. 필수 값 검증, null 반환 방지, Optional 처리, empty collection 반환 여부다.

Q. Optional 검수에서 가장 위험한 것은?
A. Optional.get 직접 호출, Optional 자체 null 반환, Optional Field / Parameter 남용이다.

---

# 11. Backend Integration

## 11.1 Spring Boot Exception Null Safety Integration

### [개념]

Exception, Null Safety, Optional은 Spring Boot Backend의 실패 흐름, 조회 결과 처리, 입력 검증, API Error Response, Domain Rule 보호와 직접 연결된다.

이 파트는 Java Foundation과 Spring Boot Domain Rules 사이의 오류 처리 기준 역할을 한다.

---

### [핵심]

Spring Boot 연결:

```text
Request DTO Validation
→ 입력 null / 형식 오류 차단

Service
→ Optional.orElseThrow
→ Business Exception 발생

Domain / Entity
→ State Rule 위반 예외 발생

Repository
→ Optional<Entity>
→ List<Entity>

GlobalExceptionHandler
→ ErrorResponse 변환

API Client
→ 외부 API 실패 예외 변환
```

---

### [실무]

전체 흐름 예:

```java
@PostMapping("/posts")
public ApiResponse<PostResponse> createPost(@Valid @RequestBody CreatePostRequest request) {
    return ApiResponse.success(postService.createPost(request));
}
```

Service:

```java
@Transactional
public PostResponse publishPost(Long postId, Long userId) {
    Post post = postRepository.findById(postId)
        .orElseThrow(() -> new PostNotFoundException(postId));

    if (!post.isOwner(userId)) {
        throw new ForbiddenPostAccessException(postId, userId);
    }

    post.publish();

    return PostResponse.from(post);
}
```

Domain:

```java
public void publish() {
    if (this.status != PostStatus.DRAFT) {
        throw new InvalidPostStateException("only draft post can be published");
    }

    this.status = PostStatus.PUBLISHED;
}
```

Exception Handler:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(PostNotFoundException.class)
    public ResponseEntity<ErrorResponse> handlePostNotFound(PostNotFoundException e) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
            .body(ErrorResponse.of("POST_NOT_FOUND", e.getMessage()));
    }
}
```

검토 기준:

- Request DTO에서 null / blank 입력을 차단하는가?
- Service에서 Optional.get을 직접 호출하지 않는가?
- 조회 실패가 명확한 NotFound Exception으로 변환되는가?
- 권한 / 소유자 / 중복 / 상태 오류가 명확한 Exception으로 표현되는가?
- Domain Method가 상태 규칙을 보호하는가?
- GlobalExceptionHandler가 HTTP Status와 ErrorCode를 일관되게 반환하는가?
- 민감정보가 ErrorResponse에 노출되지 않는가?

주의:

- Security 인증 / 인가 예외는 Security Handler와 구분한다.
- Validation Error 응답 포맷은 API Design Rules와 맞춘다.
- Transaction Rollback 정책은 Spring Boot / JPA Rules에서 추가 검토한다.
- 외부 API 실패는 재시도, 보상 트랜잭션, 로그 정책과 연결될 수 있다.

---

### [FAQ]

Q. Spring Boot에서 Optional은 어디서 많이 써?
A. Repository 단일 조회 결과와 Service의 orElseThrow 처리에서 많이 사용한다.

Q. Spring Boot에서 Custom Exception은 어디서 발생시켜?
A. Service, Domain Method, 외부 Client Adapter에서 상황에 맞게 발생시킬 수 있다.

Q. GlobalExceptionHandler는 어떤 역할을 해?
A. Exception을 일관된 HTTP Status와 ErrorResponse로 변환한다.

---

# Retrieval Queries

### [FAQ]

Q. Exception은 뭐야?
A. Java 프로그램 실행 중 발생한 비정상 상황을 표현하는 객체다.

Q. Exception Handling은 왜 중요해?
A. 오류 상황을 명확히 표현하고 API 실패 응답과 디버깅 품질을 높이기 위해 중요하다.

Q. Checked Exception과 Unchecked Exception 차이는?
A. Checked Exception은 컴파일 시 처리 강제가 있고 Unchecked Exception은 RuntimeException 계열로 컴파일 시 처리 강제가 없다.

Q. RuntimeException은 언제 써?
A. 비즈니스 규칙 위반, 잘못된 입력, 잘못된 상태, 프로그래밍 오류에 자주 사용한다.

Q. IllegalArgumentException은 언제 써?
A. Method에 전달된 인자가 잘못되었을 때 사용한다.

Q. IllegalStateException은 언제 써?
A. 객체 상태가 현재 작업을 수행하기에 부적절할 때 사용한다.

Q. Custom Exception은 언제 만들어?
A. 기본 Exception만으로 비즈니스 오류 의미가 명확하지 않을 때 만든다.

Q. 모든 오류마다 Custom Exception을 만들어야 해?
A. 아니다. 의미 있는 도메인 오류나 반복적으로 처리할 오류에 우선 적용한다.

Q. ErrorCode는 왜 써?
A. API 오류 응답을 일관되게 만들고 클라이언트가 오류 유형을 구분할 수 있게 하기 위해 사용한다.

Q. Exception Message에는 무엇을 넣어야 해?
A. 오류 원인을 식별할 수 있는 최소 정보와 안전한 식별자를 넣는다.

Q. 비밀번호나 토큰을 Exception Message에 넣어도 돼?
A. 안 된다. 민감정보는 메시지와 로그에 포함하지 않아야 한다.

Q. try-catch는 언제 써?
A. 복구, 예외 변환, 로깅, 자원 정리가 필요한 경우 사용한다.

Q. catch에서 아무것도 안 하면 안 돼?
A. 안 된다. 오류 원인이 사라지지 않고 추적이 어려워진다.

Q. try-with-resources는 언제 써?
A. 파일, 스트림, Reader처럼 close가 필요한 AutoCloseable 자원을 사용할 때 쓴다.

Q. finally에서 return 해도 돼?
A. 권장하지 않는다. 예외 흐름을 숨길 수 있다.

Q. Controller에서 try-catch를 많이 써도 돼?
A. 권장하지 않는다. 반복되는 예외 변환은 GlobalExceptionHandler로 처리하는 것이 좋다.

Q. Service에서 조회 결과가 없으면 어떻게 해?
A. Optional.orElseThrow로 명확한 Custom Exception으로 변환하는 것이 좋다.

Q. Service에서 null을 반환해도 돼?
A. 권장하지 않는다. 실패 상황은 Optional, Exception, Result Object 중 하나로 명확히 표현한다.

Q. Entity Method에서 Exception을 던져도 돼?
A. 객체 상태 규칙을 위반한 경우 가능하다.

Q. GlobalExceptionHandler는 왜 필요해?
A. 여러 Controller의 예외 응답을 일관된 형식으로 변환하기 위해 필요하다.

Q. 모든 예외를 500으로 보내도 돼?
A. 안 된다. 비즈니스 오류, 입력 오류, 인증 오류, 서버 오류를 구분해야 한다.

Q. NullPointerException은 왜 생겨?
A. 참조 변수가 null인 상태에서 Method나 Field에 접근하기 때문이다.

Q. NPE를 줄이려면 어떻게 해?
A. 필수 값 검증, Optional 반환 처리, empty collection 반환, DTO Validation을 적용한다.

Q. null check가 많으면 좋은 코드야?
A. 반드시 그렇지는 않다. null 가능성이 너무 넓게 퍼진 설계일 수 있다.

Q. 필수 값 null 검증은 어디서 해?
A. 생성자, Factory Method, Service Method 초반, DTO Validation에서 빠르게 처리하는 것이 좋다.

Q. Objects.requireNonNull은 언제 써?
A. 필수 Reference 값이 null이면 즉시 실패시켜야 할 때 사용한다.

Q. 값이 없을 수 있으면 무조건 Optional을 써?
A. 아니다. 단일 반환에는 Optional이 적합할 수 있지만 Collection은 empty collection이 보통 더 좋다.

Q. Collection 반환값은 null이 좋아 empty collection이 좋아?
A. 대부분 empty collection이 좋다.

Q. Optional은 언제 써?
A. 값이 없을 수 있는 단일 반환 결과를 명시할 때 사용한다.

Q. Optional은 null을 완전히 없애는 도구야?
A. 아니다. 값 부재를 명확히 표현하는 도구다.

Q. Optional을 Entity Field로 써도 돼?
A. 권장하지 않는다. Optional은 주로 반환 타입에 사용하는 것이 적합하다.

Q. Optional.of와 ofNullable 차이는?
A. of는 null이면 NPE가 발생하고 ofNullable은 null이면 Optional.empty를 반환한다.

Q. Optional을 반환하는 Method에서 null을 반환해도 돼?
A. 안 된다. 값이 없으면 Optional.empty를 반환해야 한다.

Q. Optional.get()을 바로 써도 돼?
A. 권장하지 않는다. 값이 없으면 NoSuchElementException이 발생한다.

Q. orElse와 orElseGet 차이는?
A. orElse는 기본값 표현식이 즉시 평가될 수 있고 orElseGet은 값이 없을 때 Supplier가 실행된다.

Q. Optional map은 언제 써?
A. Optional 내부 값이 있을 때 다른 값으로 변환하고 싶을 때 사용한다.

Q. Optional flatMap은 언제 써?
A. 변환 결과가 다시 Optional일 때 중첩 Optional을 피하기 위해 사용한다.

Q. Optional Field는 왜 지양해?
A. Optional은 주로 반환 타입을 위한 도구이고 Field나 직렬화 구조에는 부적합한 경우가 많다.

Q. Optional Parameter는 왜 지양해?
A. 호출자가 Optional을 만들어야 해서 API가 불편해지고 null 정책이 오히려 불명확해질 수 있다.

Q. Optional<List<T>>는 좋은가?
A. 대부분 불필요하다. 결과가 없으면 empty List를 반환하는 것이 좋다.

Q. NullPointerException이 나면 뭐부터 봐?
A. 스택트레이스의 발생 라인에서 어떤 참조가 null인지 먼저 확인한다.

Q. Boolean에서 NPE가 날 수 있어?
A. Boolean이 null인데 boolean으로 unboxing되면 NPE가 발생할 수 있다.

Q. Boolean null은 어떻게 비교해?
A. `Boolean.TRUE.equals(value)`를 사용하면 null-safe하다.

Q. 외부 API 응답은 null 체크해야 해?
A. 해야 한다. 외부 시스템 응답은 누락 가능성을 고려해야 한다.

Q. @NotNull과 @NotBlank 차이는?
A. @NotNull은 null만 금지하고 @NotBlank는 null, 빈 문자열, 공백 문자열을 금지한다.

Q. DTO Validation이 있으면 Service 검증은 필요 없어?
A. 아니다. DTO는 입력 형식 검증이고 Service는 비즈니스 규칙 검증을 담당한다.

Q. Service Validation은 무엇을 검증해?
A. 존재 여부, 중복, 권한, 소유자, 상태 같은 비즈니스 조건을 검증한다.

Q. 중복 검증은 Application에서만 하면 충분해?
A. 중요한 유일성은 DB Unique Constraint도 함께 검토해야 한다.

Q. 빈 catch 블록은 왜 안 좋아?
A. 오류가 사라진 것처럼 보여 실제 문제를 추적하기 어려워진다.

Q. Optional Chain이 길면 좋은 코드야?
A. 아니다. 길고 복잡하면 일반 if문이나 Guard Clause가 더 읽기 쉽다.

Q. Exception 검수에서 가장 먼저 볼 것은?
A. Exception Type이 오류 의미를 명확히 표현하는지 먼저 확인한다.

Q. Null Safety 검수에서 가장 중요한 것은?
A. 필수 값 검증, null 반환 방지, Optional 처리, empty collection 반환 여부다.

Q. Spring Boot에서 Optional은 어디서 많이 써?
A. Repository 단일 조회 결과와 Service의 orElseThrow 처리에서 많이 사용한다.

Q. GlobalExceptionHandler는 어떤 역할을 해?
A. Exception을 일관된 HTTP Status와 ErrorResponse로 변환한다.

Q. Java Part06 다음 문서는 뭐야?
A. Java Part07 — Lambda, Stream, Immutability 문서로 이어지는 것이 좋다.
