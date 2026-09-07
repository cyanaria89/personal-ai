# Spring Boot Part08 - Exception Handling & GlobalExceptionHandler

---

# 1. Exception Handling

## 1.1 Exception Handling 개념

### [개념]

Exception Handling은 Application 실행 중 발생하는 오류를 일관된 방식으로 처리하는 구조다.

Spring Boot Backend API에서는 Controller마다 `try-catch`를 반복하지 않고, `GlobalExceptionHandler`에서 예외를 공통 Error Response로 변환하는 방식을 권장한다.

기본 흐름:

```text
Client Request
→ Controller
→ Service
→ Exception 발생
→ GlobalExceptionHandler
→ Error Response
→ Client
```

Exception Handling의 목적:

- API Error Response 일관화
- Controller 코드 단순화
- Business Error 의미 명확화
- Validation Error 응답 통일
- 예상하지 못한 오류 통제
- 내부 예외 메시지 노출 방지
- Frontend Error Handling 안정화
- Logging 기준 통일

---

### [핵심]

Spring Boot 예외 처리 핵심 요소:

- `@RestControllerAdvice`
- `@ExceptionHandler`
- CustomException
- BusinessException
- ErrorCode
- ErrorResponse
- Validation Exception
- MethodArgumentNotValidException
- RuntimeException fallback
- Logging

예외 처리 위치:

| 위치                   | 역할                         |
| ---------------------- | ---------------------------- |
| Service                | Business Exception 발생      |
| Repository             | Optional / DB 예외 발생 가능 |
| Controller             | 예외 직접 처리 지양          |
| GlobalExceptionHandler | 예외를 Error Response로 변환 |
| Filter / Security      | 인증 / 인가 예외 처리        |

---

### [실무]

권장 흐름:

```text
Service에서 BusinessException 발생
→ GlobalExceptionHandler에서 catch
→ ErrorCode와 message 기반 Error Response 생성
→ Client에 일관된 실패 응답 반환
```

예:

```java
@Transactional(readOnly = true)
public UserResponse getUser(Long userId) {
    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    return UserResponse.from(user);
}
```

Handler:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(BusinessException.class)
    public ApiResponse<Void> handleBusinessException(BusinessException exception) {
        return ApiResponse.fail(
                exception.getErrorCode(),
                exception.getMessage()
        );
    }
}
```

권장:

- Controller마다 `try-catch` 반복 금지
- 비즈니스 오류는 CustomException 사용
- ErrorCode를 명확히 작성
- Validation Error는 별도 handler 작성
- 예상하지 못한 Exception은 generic message 반환
- 실제 stack trace는 서버 로그에 기록
- Client 응답에는 내부 구현 정보 노출 금지

---

### [FAQ]

Q. Spring Boot에서 예외 처리는 어디서 해?

A.
Controller마다 처리하지 않고 `@RestControllerAdvice` 기반 GlobalExceptionHandler에서 공통 처리하는 것이 좋다.

Q. Service에서 예외를 던져도 돼?

A.
된다. 사용자 없음, 중복 데이터, 권한 없음 같은 비즈니스 오류는 Service에서 CustomException으로 발생시키는 것이 좋다.

Q. Controller에서 try-catch를 쓰면 안 돼?

A.
특수한 경우가 아니면 지양한다. Controller마다 try-catch를 반복하면 Error Response 일관성이 깨지고 코드가 복잡해진다.

---

# 2. GlobalExceptionHandler

## 2.1 GlobalExceptionHandler 개념

### [개념]

GlobalExceptionHandler는 Application 전역에서 발생한 예외를 잡아 API Error Response로 변환하는 클래스다.

Spring Boot에서는 `@RestControllerAdvice`와 `@ExceptionHandler`를 사용한다.

---

### [핵심]

주요 Annotation:

- `@RestControllerAdvice`
- `@ControllerAdvice`
- `@ExceptionHandler`
- `@ResponseStatus`
- `ResponseEntity`

`@RestControllerAdvice` 특징:

- 전역 Controller 예외 처리
- JSON Response 반환
- `@ResponseBody` 포함
- REST API에 적합

---

### [실무]

기본 구조:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(BusinessException.class)
    public ApiResponse<Void> handleBusinessException(BusinessException exception) {
        return ApiResponse.fail(
                exception.getErrorCode(),
                exception.getMessage()
        );
    }

    @ExceptionHandler(Exception.class)
    public ApiResponse<Void> handleException(Exception exception) {
        return ApiResponse.fail(
                "INTERNAL_SERVER_ERROR",
                "서버 내부 오류가 발생했습니다."
        );
    }
}
```

권장:

- BusinessException handler 작성
- Validation Exception handler 작성
- TypeMismatch / MissingParameter handler 작성
- RuntimeException fallback 작성
- Exception fallback 작성
- 구체적인 예외 handler를 먼저 작성
- 너무 넓은 Exception handler가 구체 예외를 가리지 않도록 주의

---

### [주의]

Handler 작성 순서 자체보다 예외 타입의 구체성이 중요하다.

주의할 점:

- `Exception.class` fallback에서 모든 예외를 같은 메시지로 덮지 않음
- BusinessException을 RuntimeException handler보다 명확히 처리
- Validation Exception을 별도 처리
- 내부 예외 메시지를 그대로 노출하지 않음
- 로그와 Client 응답을 구분
- Security 예외는 Security Filter Chain에서 먼저 처리될 수 있음

---

### [FAQ]

Q. @RestControllerAdvice와 @ControllerAdvice 차이는?

A.
`@RestControllerAdvice`는 `@ControllerAdvice`에 `@ResponseBody` 성격이 포함되어 REST API JSON 응답에 적합하다.

Q. Exception.class handler는 꼭 필요해?

A.
예상하지 못한 예외를 통제하기 위해 fallback으로 두는 것이 좋다. 다만 내부 메시지를 그대로 내려보내면 안 된다.

Q. GlobalExceptionHandler가 모든 예외를 잡아?

A.
Controller 이후 흐름의 예외는 처리할 수 있지만 Filter나 Security 단계 예외는 별도 처리 구조가 필요할 수 있다.

---

# 3. Error Response Convention

## 3.1 Error Response 구조

### [개념]

Error Response Convention은 실패 응답 형식을 일관되게 만드는 규칙이다.

Frontend는 Error Response 형식이 일정해야 ErrorCode, Message, FieldError를 기준으로 안정적으로 처리할 수 있다.

---

### [핵심]

Error Response 구성 요소:

- success
- status
- errorCode
- message
- fieldErrors
- timestamp
- path

기초 구조 예:

```json
{
  "success": false,
  "errorCode": "USER_NOT_FOUND",
  "message": "사용자를 찾을 수 없습니다.",
  "data": null
}
```

Validation Error 예:

```json
{
  "success": false,
  "errorCode": "INVALID_REQUEST",
  "message": "요청 값이 올바르지 않습니다.",
  "fieldErrors": [
    {
      "field": "email",
      "message": "이메일 형식이 올바르지 않습니다."
    }
  ]
}
```

---

### [실무]

ApiResponse 예:

```java
public record ApiResponse<T>(
        boolean success,
        String message,
        T data,
        String errorCode
) {
    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(true, "success", data, null);
    }

    public static <T> ApiResponse<T> fail(String errorCode, String message) {
        return new ApiResponse<>(false, message, null, errorCode);
    }
}
```

별도 ErrorResponse 예:

```java
public record ErrorResponse(
        String errorCode,
        String message
) {
    public static ErrorResponse of(String errorCode, String message) {
        return new ErrorResponse(errorCode, message);
    }
}
```

선택 기준:

| 방식                | 특징                          |
| ------------------- | ----------------------------- |
| ApiResponse fail    | 성공 / 실패 응답 wrapper 통일 |
| ErrorResponse 별도  | 실패 응답 구조를 독립 관리    |
| ResponseEntity 조합 | HTTP Status 세밀 제어 가능    |

---

### [Best Practice]

Error Response Best Practice:

- 성공 응답과 실패 응답 형식 통일
- ErrorCode는 기계가 읽기 쉬운 값 사용
- message는 사용자 또는 Frontend가 이해 가능한 값 사용
- fieldErrors는 Validation 실패 시 선택적으로 포함
- timestamp, path는 필요 시 추가
- 내부 exception class 이름 노출 금지
- stack trace를 Client로 반환 금지

---

### [FAQ]

Q. Error Response에는 무엇이 들어가야 해?

A.
기본적으로 errorCode, message가 필요하고 Validation 실패에는 fieldErrors를 포함할 수 있다.

Q. ApiResponse로 실패 응답까지 감싸도 돼?

A.
가능하다. 프로젝트 규칙이 성공 / 실패 모두 ApiResponse로 통일하는 방식이면 일관성이 좋다.

Q. ErrorCode는 왜 필요해?

A.
Frontend나 Agent가 문자열 메시지가 아니라 안정적인 코드 기준으로 오류를 처리할 수 있기 때문이다.

---

## 3.2 HTTP Status와 ErrorCode

### [개념]

HTTP Status는 HTTP 프로토콜 수준의 결과이고 ErrorCode는 Application 비즈니스 오류를 구분하는 코드다.

둘은 서로 보완 관계다.

---

### [핵심]

자주 쓰는 HTTP Status:

| Status | 의미                  | 예                             |
| ------ | --------------------- | ------------------------------ |
| 400    | Bad Request           | Validation 실패, Type mismatch |
| 401    | Unauthorized          | 인증 필요                      |
| 403    | Forbidden             | 권한 없음                      |
| 404    | Not Found             | 데이터 없음                    |
| 409    | Conflict              | 중복 데이터, 상태 충돌         |
| 500    | Internal Server Error | 예상하지 못한 서버 오류        |

ErrorCode 예:

```text
INVALID_REQUEST
USER_NOT_FOUND
DUPLICATED_EMAIL
NO_PERMISSION
POST_DELETED
ALREADY_LIKED
INTERNAL_SERVER_ERROR
```

---

### [실무]

ErrorCode Enum 예:

```java
public enum ErrorCode {

    USER_NOT_FOUND(404, "사용자를 찾을 수 없습니다."),
    DUPLICATED_EMAIL(409, "이미 사용 중인 이메일입니다."),
    INVALID_REQUEST(400, "요청 값이 올바르지 않습니다."),
    INTERNAL_SERVER_ERROR(500, "서버 내부 오류가 발생했습니다.");

    private final int status;
    private final String message;

    ErrorCode(int status, String message) {
        this.status = status;
        this.message = message;
    }

    public int getStatus() {
        return status;
    }

    public String getMessage() {
        return message;
    }
}
```

BusinessException:

```java
public class BusinessException extends RuntimeException {

    private final ErrorCode errorCode;

    public BusinessException(ErrorCode errorCode) {
        super(errorCode.getMessage());
        this.errorCode = errorCode;
    }

    public ErrorCode getErrorCode() {
        return errorCode;
    }
}
```

Handler:

```java
@ExceptionHandler(BusinessException.class)
public ResponseEntity<ApiResponse<Void>> handleBusinessException(BusinessException exception) {
    ErrorCode errorCode = exception.getErrorCode();

    return ResponseEntity
            .status(errorCode.getStatus())
            .body(ApiResponse.fail(errorCode.name(), errorCode.getMessage()));
}
```

---

### [주의]

HTTP Status와 ErrorCode 주의:

- 모든 실패를 200 OK로 반환할지 여부는 프로젝트 규칙으로 통일
- REST API에서는 HTTP Status를 적절히 사용하는 방식이 명확함
- ErrorCode 없이 message만 내려주면 Frontend 처리 불안정
- HTTP Status만으로 비즈니스 오류를 세분화하기 어려움
- ErrorCode naming은 프로젝트 전체에서 통일

---

### [FAQ]

Q. 실패 응답도 HTTP 200으로 내려도 돼?

A.
프로젝트 규칙에 따라 가능하지만 REST API 관점에서는 오류 상황에 맞는 HTTP Status를 사용하는 방식이 명확하다.

Q. HTTP Status와 ErrorCode 중 뭐가 더 중요해?

A.
둘 다 중요하다. HTTP Status는 프로토콜 수준 결과이고 ErrorCode는 Application 오류를 세부 구분한다.

Q. ErrorCode는 문자열로 해도 돼?

A.
가능하다. 다만 규모가 커지면 Enum으로 관리하는 것이 오타와 중복을 줄이는 데 좋다.

---

# 4. Custom Exception

## 4.1 Custom Exception 개념

### [개념]

Custom Exception은 Application의 비즈니스 오류를 명확하게 표현하기 위해 직접 정의하는 예외다.

Service Layer에서 비즈니스 규칙 위반이 발생하면 Custom Exception을 던지고, GlobalExceptionHandler에서 공통 Error Response로 변환한다.

---

### [핵심]

Custom Exception 사용 상황:

- 사용자 없음
- 게시글 없음
- 중복 이메일
- 권한 없음
- 이미 좋아요 처리됨
- 삭제된 데이터 접근
- 잘못된 상태 전환
- 재고 부족
- 외부 API 실패
- 파일 업로드 실패

구성 요소:

- ErrorCode
- message
- status
- cause
- business meaning

---

### [실무]

기초형:

```java
public class BusinessException extends RuntimeException {

    private final String errorCode;

    public BusinessException(String errorCode, String message) {
        super(message);
        this.errorCode = errorCode;
    }

    public String getErrorCode() {
        return errorCode;
    }
}
```

Enum 기반:

```java
public class BusinessException extends RuntimeException {

    private final ErrorCode errorCode;

    public BusinessException(ErrorCode errorCode) {
        super(errorCode.getMessage());
        this.errorCode = errorCode;
    }

    public BusinessException(ErrorCode errorCode, Throwable cause) {
        super(errorCode.getMessage(), cause);
        this.errorCode = errorCode;
    }

    public ErrorCode getErrorCode() {
        return errorCode;
    }
}
```

Service 사용:

```java
User user = userRepository.findById(userId)
        .orElseThrow(() -> new BusinessException(ErrorCode.USER_NOT_FOUND));
```

---

### [Best Practice]

Custom Exception Best Practice:

- 비즈니스 오류는 RuntimeException 기반 사용 고려
- ErrorCode와 message를 분리
- Controller에서 직접 생성하지 않음
- Service에서 비즈니스 의미에 맞게 발생
- 중복 Exception class를 과도하게 만들지 않음
- ErrorCode Enum으로 관리 가능
- cause가 필요한 경우 원본 예외 보존

---

### [FAQ]

Q. Custom Exception은 언제 만들어?

A.
사용자 없음, 권한 없음, 중복 데이터, 잘못된 상태 전환처럼 비즈니스 의미가 있는 오류에 사용한다.

Q. Custom Exception은 RuntimeException을 상속하는 게 좋아?

A.
비즈니스 오류로 rollback이 필요한 경우 RuntimeException 기반이 Spring Transaction 기본 rollback 규칙과 잘 맞는다.

Q. ErrorCode Enum은 꼭 필요해?

A.
필수는 아니지만 오류 코드가 많아지면 Enum으로 관리하는 것이 오타와 중복을 줄이는 데 좋다.

---

## 4.2 BusinessException과 Domain Exception

### [개념]

BusinessException은 Application 비즈니스 규칙 위반을 표현하는 일반 예외다.

Domain Exception은 특정 도메인에서 발생하는 오류를 더 구체적으로 표현하는 예외다.

---

### [핵심]

BusinessException 예:

```text
USER_NOT_FOUND
DUPLICATED_EMAIL
NO_PERMISSION
INVALID_STATE
```

Domain Exception 예:

```text
OrderNotPayableException
OutOfStockException
PostAlreadyDeletedException
AlreadyLikedException
```

선택 기준:

| 방식                          | 특징                       | 사용 상황        |
| ----------------------------- | -------------------------- | ---------------- |
| BusinessException + ErrorCode | 단순하고 일관됨            | 기초 / 중소 규모 |
| Domain Exception class        | 의미가 강함                | 복잡한 도메인    |
| 혼합 방식                     | ErrorCode와 타입 모두 활용 | 중대형 프로젝트  |

---

### [실무]

기초 프로젝트 권장:

```java
throw new BusinessException(ErrorCode.DUPLICATED_EMAIL);
```

도메인 예외 방식:

```java
public class OutOfStockException extends BusinessException {

    public OutOfStockException() {
        super(ErrorCode.OUT_OF_STOCK);
    }
}
```

사용:

```java
if (!product.hasStock(quantity)) {
    throw new OutOfStockException();
}
```

권장:

- 처음에는 BusinessException + ErrorCode로 단순화
- 도메인 오류가 복잡해지면 개별 Exception class 검토
- Handler는 공통 부모 BusinessException으로 처리 가능
- Exception class 수가 과도하게 늘어나지 않도록 관리

---

### [FAQ]

Q. 예외 클래스를 오류마다 하나씩 만들어야 해?

A.
필수는 아니다. 기초 구조에서는 BusinessException과 ErrorCode 조합으로 충분한 경우가 많다.

Q. Domain Exception은 언제 필요해?

A.
도메인별 예외 의미가 중요하거나 예외 타입별로 다른 처리가 필요할 때 검토한다.

---

# 5. Validation Exception Handling

## 5.1 MethodArgumentNotValidException 처리

### [개념]

`MethodArgumentNotValidException`은 `@Valid @RequestBody` 검증이 실패했을 때 주로 발생하는 예외다.

Request DTO의 Bean Validation 실패를 GlobalExceptionHandler에서 처리해 일관된 Error Response로 변환한다.

---

### [핵심]

발생 상황:

- `@NotBlank` 실패
- `@NotNull` 실패
- `@Email` 실패
- `@Size` 실패
- `@Min`, `@Max` 실패
- Request DTO 검증 실패
- `@Valid @RequestBody` 조합 사용

기본 흐름:

```text
Client JSON Request
→ Controller @Valid @RequestBody
→ DTO Validation 실패
→ MethodArgumentNotValidException
→ GlobalExceptionHandler
→ Validation Error Response
```

---

### [실무]

Request DTO:

```java
public record SignUpRequest(
        @Email(message = "이메일 형식이 올바르지 않습니다.")
        String email,

        @NotBlank(message = "비밀번호는 필수입니다.")
        String password,

        @NotBlank(message = "닉네임은 필수입니다.")
        String nickname
) {
}
```

Controller:

```java
@PostMapping("/signup")
public ApiResponse<UserResponse> signUp(
        @Valid @RequestBody SignUpRequest request
) {
    return ApiResponse.success(userService.signUp(request));
}
```

FieldError DTO:

```java
public record FieldErrorResponse(
        String field,
        String message
) {
}
```

Handler:

```java
@ExceptionHandler(MethodArgumentNotValidException.class)
public ResponseEntity<ApiResponse<List<FieldErrorResponse>>> handleValidationException(
        MethodArgumentNotValidException exception
) {
    List<FieldErrorResponse> fieldErrors = exception.getBindingResult()
            .getFieldErrors()
            .stream()
            .map(error -> new FieldErrorResponse(
                    error.getField(),
                    error.getDefaultMessage()
            ))
            .toList();

    return ResponseEntity
            .badRequest()
            .body(ApiResponse.fail("INVALID_REQUEST", "요청 값이 올바르지 않습니다.", fieldErrors));
}
```

---

### [주의]

Validation Error 처리 주의:

- 모든 field error를 내려줄지 첫 번째 error만 내려줄지 정책 결정
- 사용자 메시지와 개발자 메시지 구분
- 내부 class name 노출 금지
- Validation message를 팀 기준으로 통일
- Request DTO에 Validation Annotation 누락 주의
- `@Valid` 누락 시 검증이 실행되지 않음

---

### [FAQ]

Q. MethodArgumentNotValidException은 언제 발생해?

A.
`@Valid @RequestBody`로 받은 Request DTO의 Bean Validation이 실패했을 때 주로 발생한다.

Q. Validation 실패는 어디서 처리해?

A.
GlobalExceptionHandler에서 MethodArgumentNotValidException을 처리해 공통 Error Response로 변환한다.

Q. @Valid를 안 붙이면 어떻게 돼?

A.
Request DTO에 Validation Annotation이 있어도 검증이 실행되지 않을 수 있다.

---

## 5.2 ConstraintViolationException 처리

### [개념]

`ConstraintViolationException`은 주로 `@RequestParam`, `@PathVariable` 또는 method parameter validation이 실패할 때 발생할 수 있다.

`@Validated`와 함께 사용되는 경우가 많다.

---

### [핵심]

발생 상황:

- `@RequestParam @Min`
- `@PathVariable @Positive`
- method parameter validation
- class level `@Validated`
- Bean Validation 제약 위반

예:

```java
@GetMapping("/posts/{postId}")
public ApiResponse<PostResponse> getPost(
        @PathVariable @Positive Long postId
) {
    return ApiResponse.success(postService.getPost(postId));
}
```

---

### [실무]

Controller:

```java
@Validated
@RestController
@RequestMapping("/api/posts")
@RequiredArgsConstructor
public class PostController {

    private final PostService postService;

    @GetMapping("/{postId}")
    public ApiResponse<PostResponse> getPost(
            @PathVariable @Positive Long postId
    ) {
        return ApiResponse.success(postService.getPost(postId));
    }
}
```

Handler:

```java
@ExceptionHandler(ConstraintViolationException.class)
public ResponseEntity<ApiResponse<Void>> handleConstraintViolationException(
        ConstraintViolationException exception
) {
    return ResponseEntity
            .badRequest()
            .body(ApiResponse.fail("INVALID_PARAMETER", "요청 파라미터가 올바르지 않습니다."));
}
```

권장:

- RequestBody 검증은 `@Valid`
- Parameter 검증은 `@Validated`와 Bean Validation 조합
- ErrorCode를 Request Body 검증과 구분 가능
- 세부 parameter error 포함 여부는 프로젝트 정책으로 결정

---

### [주의]

Parameter Validation 주의:

- Controller class에 `@Validated` 필요할 수 있음
- PathVariable과 RequestParam 검증 실패는 RequestBody 검증과 예외 타입이 다를 수 있음
- 모든 검증 실패를 하나의 handler로 뭉개면 원인 파악이 어려움
- Frontend가 field와 parameter error를 구분할 필요가 있는지 확인

---

### [FAQ]

Q. ConstraintViolationException은 언제 발생해?

A.
`@RequestParam`, `@PathVariable`, method parameter validation이 실패했을 때 발생할 수 있다.

Q. @Valid와 @Validated는 뭐가 달라?

A.
`@Valid`는 Bean Validation 표준이고 `@Validated`는 Spring의 확장 기능이다. method parameter validation에서는 `@Validated`가 필요할 수 있다.

---

## 5.3 BindException과 TypeMismatch 처리

### [개념]

BindException과 TypeMismatch 예외는 요청 parameter나 form/query object binding 과정에서 타입 변환 또는 binding이 실패할 때 발생할 수 있다.

---

### [핵심]

관련 예외:

- BindException
- MethodArgumentTypeMismatchException
- MissingServletRequestParameterException
- HttpMessageNotReadableException

발생 예:

- 숫자 자리에 문자열 전달
- enum 값 불일치
- 날짜 포맷 불일치
- 필수 query parameter 누락
- JSON 문법 오류
- Request Body 타입 불일치

---

### [실무]

TypeMismatch Handler:

```java
@ExceptionHandler(MethodArgumentTypeMismatchException.class)
public ResponseEntity<ApiResponse<Void>> handleTypeMismatchException(
        MethodArgumentTypeMismatchException exception
) {
    return ResponseEntity
            .badRequest()
            .body(ApiResponse.fail("TYPE_MISMATCH", "요청 값의 타입이 올바르지 않습니다."));
}
```

Missing Parameter Handler:

```java
@ExceptionHandler(MissingServletRequestParameterException.class)
public ResponseEntity<ApiResponse<Void>> handleMissingParameterException(
        MissingServletRequestParameterException exception
) {
    return ResponseEntity
            .badRequest()
            .body(ApiResponse.fail("MISSING_PARAMETER", "필수 요청 파라미터가 누락되었습니다."));
}
```

JSON Parse Error Handler:

```java
@ExceptionHandler(HttpMessageNotReadableException.class)
public ResponseEntity<ApiResponse<Void>> handleHttpMessageNotReadableException(
        HttpMessageNotReadableException exception
) {
    return ResponseEntity
            .badRequest()
            .body(ApiResponse.fail("INVALID_JSON", "요청 본문을 읽을 수 없습니다."));
}
```

---

### [Troubleshooting]

문제: `400 Bad Request` 발생

```text
원인 후보:
- JSON 문법 오류
- RequestBody 필드 타입 불일치
- Enum 값 불일치
- 날짜 포맷 불일치
- 필수 RequestParam 누락
- PathVariable 타입 불일치
```

확인 순서:

```text
Request Payload 확인
→ Content-Type 확인
→ Controller Parameter Annotation 확인
→ DTO Field Type 확인
→ Enum 값 확인
→ 날짜 포맷 확인
→ Validation Error 확인
```

---

### [FAQ]

Q. 숫자 id 자리에 문자열을 보내면 어떤 예외가 나?

A.
`MethodArgumentTypeMismatchException`이 발생할 수 있다.

Q. JSON 형식이 깨지면 어떤 예외가 나?

A.
`HttpMessageNotReadableException`이 발생할 수 있다.

Q. 필수 RequestParam이 없으면?

A.
`MissingServletRequestParameterException`이 발생할 수 있다.

---

# 6. Not Found Exception Handling

## 6.1 Resource Not Found 처리

### [개념]

Resource Not Found는 요청한 데이터가 존재하지 않는 상황이다.

Repository 단건 조회 결과가 없을 때 Service에서 CustomException으로 변환하는 것이 좋다.

---

### [핵심]

Not Found 발생 상황:

- 사용자 없음
- 게시글 없음
- 댓글 없음
- 주문 없음
- 알림 없음
- 파일 없음
- 삭제된 데이터 접근
- 잘못된 id 요청

권장 흐름:

```text
Repository Optional.empty
→ Service orElseThrow
→ BusinessException(USER_NOT_FOUND)
→ GlobalExceptionHandler
→ 404 Error Response
```

---

### [실무]

Service:

```java
@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    Post post = postRepository.findByIdAndDeletedFalse(postId)
            .orElseThrow(() -> new BusinessException(ErrorCode.POST_NOT_FOUND));

    return PostResponse.from(post);
}
```

ErrorCode:

```java
public enum ErrorCode {

    POST_NOT_FOUND(404, "게시글을 찾을 수 없습니다."),
    USER_NOT_FOUND(404, "사용자를 찾을 수 없습니다.");

    private final int status;
    private final String message;
}
```

Handler:

```java
@ExceptionHandler(BusinessException.class)
public ResponseEntity<ApiResponse<Void>> handleBusinessException(BusinessException exception) {
    ErrorCode errorCode = exception.getErrorCode();

    return ResponseEntity
            .status(errorCode.getStatus())
            .body(ApiResponse.fail(errorCode.name(), errorCode.getMessage()));
}
```

---

### [주의]

Not Found 처리 Anti Pattern:

```java
User user = userRepository.findById(userId).get();
```

문제:

- NoSuchElementException 발생
- ErrorCode 불명확
- 사용자 메시지 통제 불가
- 404가 아닌 500으로 응답될 수 있음

비권장:

```java
if (userRepository.findById(userId).isEmpty()) {
    return null;
}
```

문제:

- null 반환
- Controller에서 추가 분기 필요
- 실패 의미 불명확
- NPE 가능성 증가

---

### [FAQ]

Q. 데이터가 없으면 null을 반환해도 돼?

A.
권장하지 않는다. Service에서 CustomException을 발생시키고 GlobalExceptionHandler에서 404 응답으로 변환하는 것이 좋다.

Q. findById().get()을 쓰면 왜 안 좋아?

A.
값이 없을 때 NoSuchElementException이 발생하고 ErrorCode와 응답 메시지를 통제하기 어렵다.

Q. 삭제된 데이터는 Not Found로 처리해도 돼?

A.
가능하다. 보안이나 사용자 경험상 삭제된 데이터와 존재하지 않는 데이터를 같은 404로 처리할 수 있다. 프로젝트 정책으로 통일한다.

---

# 7. Authorization / Authentication Exception 기초

## 7.1 인증 / 인가 예외 구분

### [개념]

Authentication Exception은 인증되지 않은 사용자의 요청 오류다.

Authorization Exception은 인증은 되었지만 해당 작업 권한이 없는 경우의 오류다.

Spring Security를 사용하는 경우 많은 인증 / 인가 예외는 Security Filter Chain에서 먼저 처리될 수 있다.

---

### [핵심]

구분:

| 구분                | 의미           | HTTP Status | 예                  |
| ------------------- | -------------- | ----------- | ------------------- |
| Authentication      | 인증 필요      | 401         | 로그인 필요         |
| Authorization       | 권한 없음      | 403         | 작성자 아님         |
| Business Permission | 업무 권한 없음 | 403         | 본인 글만 수정 가능 |

예외 예:

```text
UNAUTHORIZED
FORBIDDEN
NO_PERMISSION
ACCESS_DENIED
INVALID_TOKEN
EXPIRED_TOKEN
```

---

### [실무]

Service 권한 검사:

```java
@Transactional
public PostResponse updatePost(Long postId, Long userId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException(ErrorCode.POST_NOT_FOUND));

    if (!post.isWriter(userId)) {
        throw new BusinessException(ErrorCode.NO_PERMISSION);
    }

    post.update(request.title(), request.content());

    return PostResponse.from(post);
}
```

ErrorCode:

```java
NO_PERMISSION(403, "요청한 작업에 대한 권한이 없습니다.")
```

Handler는 BusinessException 공통 처리 가능.

---

### [주의]

인증 / 인가 예외 주의:

- JWT 만료, 인증 실패는 Security Filter에서 처리될 수 있음
- Service의 권한 검사는 비즈니스 권한 검사로 볼 수 있음
- RequestBody의 userId를 신뢰하지 않음
- 인증 사용자 정보는 SecurityContext / Principal 기준 사용
- Security 심화는 Security Advanced Domain Rules에서 다룸

---

### [FAQ]

Q. 401과 403 차이는?

A.
401은 인증이 필요하거나 인증이 실패한 상태이고, 403은 인증은 되었지만 권한이 없는 상태다.

Q. 게시글 작성자만 수정 가능 검사는 어디서 해?

A.
Service에서 Entity를 조회한 뒤 작성자 여부를 확인하고 권한이 없으면 BusinessException을 발생시키는 것이 좋다.

Q. JWT 만료 예외도 GlobalExceptionHandler에서 처리해?

A.
Security Filter 단계에서 발생한 예외는 GlobalExceptionHandler보다 Security Exception Handler에서 처리될 수 있다.

---

# 8. External API Exception Handling

## 8.1 외부 API 예외 처리

### [개념]

External API Exception Handling은 외부 서버 호출 실패를 Application 내부 오류 응답으로 통제하는 구조다.

외부 API 실패를 그대로 Client에 노출하지 않고, 내부 ErrorCode로 변환하는 것이 좋다.

---

### [핵심]

외부 API 실패 상황:

- timeout
- connection error
- 4xx response
- 5xx response
- invalid response
- rate limit
- authentication failure
- empty response
- parsing error

권장 흐름:

```text
Service
→ ExternalApiClient
→ External API 호출 실패
→ ExternalApiException 발생
→ GlobalExceptionHandler
→ 통제된 Error Response
```

---

### [실무]

ExternalApiException:

```java
public class ExternalApiException extends RuntimeException {

    private final ErrorCode errorCode;

    public ExternalApiException(ErrorCode errorCode, Throwable cause) {
        super(errorCode.getMessage(), cause);
        this.errorCode = errorCode;
    }

    public ErrorCode getErrorCode() {
        return errorCode;
    }
}
```

ExternalApiClient:

```java
@Component
@RequiredArgsConstructor
public class TourApiClient {

    public TourApiResponse getFestivalInfo(String keyword) {
        try {
            ...
        } catch (Exception exception) {
            throw new ExternalApiException(ErrorCode.EXTERNAL_API_ERROR, exception);
        }
    }
}
```

Handler:

```java
@ExceptionHandler(ExternalApiException.class)
public ResponseEntity<ApiResponse<Void>> handleExternalApiException(
        ExternalApiException exception
) {
    ErrorCode errorCode = exception.getErrorCode();

    return ResponseEntity
            .status(errorCode.getStatus())
            .body(ApiResponse.fail(errorCode.name(), errorCode.getMessage()));
}
```

---

### [주의]

외부 API 예외 처리 주의:

- API Key를 로그에 남기지 않음
- 외부 응답 전체를 Client에 그대로 반환하지 않음
- timeout 설정 필요
- 실패 메시지 사용자 친화적으로 변환
- 재시도 정책 필요 여부 검토
- 외부 API 실패가 전체 Use Case 실패인지 부분 실패인지 정책 결정
- Transaction 안에서 장시간 외부 API 호출 지양

---

### [FAQ]

Q. 외부 API 오류 메시지를 그대로 내려도 돼?

A.
권장하지 않는다. 외부 시스템 내부 메시지나 민감정보가 노출될 수 있으므로 내부 ErrorCode와 메시지로 변환하는 것이 좋다.

Q. 외부 API 실패는 500으로 처리하면 돼?

A.
상황에 따라 502, 503, 504 같은 상태를 검토할 수 있다. 기초 프로젝트에서는 EXTERNAL_API_ERROR 같은 ErrorCode로 일관 처리할 수 있다.

---

# 9. Logging in Exception Handling

## 9.1 예외 Logging 기준

### [개념]

예외 Logging은 서버 내부에서 문제 원인을 추적하기 위해 예외 정보를 기록하는 작업이다.

Client 응답과 서버 로그는 목적이 다르다.

---

### [핵심]

Client 응답:

- 간결한 message
- errorCode
- fieldErrors
- 내부 정보 제외
- stack trace 제외

Server log:

- exception stack trace
- request context
- userId
- path
- parameter summary
- external API status
- 원인 추적 정보

Log Level 기준:

| Level | 사용 상황                               |
| ----- | --------------------------------------- |
| ERROR | 예상하지 못한 서버 오류, 장애           |
| WARN  | 비즈니스 오류, 외부 API 실패, 의심 상황 |
| INFO  | 주요 이벤트                             |
| DEBUG | 개발 디버깅                             |

---

### [실무]

Logger:

```java
private static final Logger log = LoggerFactory.getLogger(GlobalExceptionHandler.class);
```

BusinessException:

```java
@ExceptionHandler(BusinessException.class)
public ResponseEntity<ApiResponse<Void>> handleBusinessException(BusinessException exception) {
    log.warn("BusinessException: errorCode={}, message={}",
            exception.getErrorCode().name(),
            exception.getMessage());

    ErrorCode errorCode = exception.getErrorCode();

    return ResponseEntity
            .status(errorCode.getStatus())
            .body(ApiResponse.fail(errorCode.name(), errorCode.getMessage()));
}
```

Unexpected Exception:

```java
@ExceptionHandler(Exception.class)
public ResponseEntity<ApiResponse<Void>> handleException(Exception exception) {
    log.error("Unexpected exception occurred", exception);

    return ResponseEntity
            .status(500)
            .body(ApiResponse.fail("INTERNAL_SERVER_ERROR", "서버 내부 오류가 발생했습니다."));
}
```

---

### [주의]

Logging 주의:

- 비밀번호 로그 금지
- Access Token / Refresh Token 로그 금지
- API Key 로그 금지
- 주민번호 / 전화번호 / 이메일 등 개인정보 로그 주의
- 모든 BusinessException을 ERROR로 남기지 않음
- 예상 가능한 사용자 오류는 WARN 또는 INFO 기준 검토
- stack trace는 Client 응답에 포함하지 않음

---

### [FAQ]

Q. 예외 메시지를 Client와 Log에 똑같이 남기면 돼?

A.
아니다. Client 응답은 안전하고 간결해야 하며, 서버 로그는 원인 추적에 필요한 정보를 포함할 수 있다.

Q. 모든 예외를 ERROR로 찍어야 해?

A.
아니다. Validation 실패나 비즈니스 조건 위반 같은 예상 가능한 오류는 WARN 또는 INFO로 관리할 수 있다.

Q. 로그에 토큰을 남겨도 돼?

A.
안 된다. Access Token, Refresh Token, API Key, Password 같은 민감정보는 로그에 남기면 안 된다.

---

# 10. Exception Handling Anti Pattern

## 10.1 Common Anti Pattern

### [개념]

Exception Handling Anti Pattern은 예외 처리가 분산되거나 내부 오류가 Client에 노출되어 유지보수성과 안정성을 떨어뜨리는 구조다.

---

### [핵심]

자주 발생하는 Anti Pattern:

- Controller마다 try-catch 반복
- Exception.class만 하나로 처리
- 내부 예외 메시지 그대로 반환
- stack trace를 Client에 반환
- ErrorCode 없이 message만 반환
- RuntimeException만 무분별하게 던짐
- Optional.get 사용
- null 반환 후 Controller에서 분기
- Validation Exception 미처리
- TypeMismatch 미처리
- BusinessException과 System Exception 구분 없음
- 모든 오류를 HTTP 200으로 반환하면서 규칙 없음
- 로그 없이 generic response만 반환
- 민감정보를 로그에 기록
- 외부 API 오류를 그대로 노출

---

### [실무]

나쁜 예:

```java
@GetMapping("/users/{userId}")
public ApiResponse<UserResponse> getUser(@PathVariable Long userId) {
    try {
        return ApiResponse.success(userService.getUser(userId));
    } catch (Exception e) {
        return ApiResponse.fail("ERROR", e.getMessage());
    }
}
```

문제:

- Controller마다 예외 처리 중복
- 모든 예외가 같은 ErrorCode
- 내부 메시지 노출 위험
- HTTP Status 통제 어려움
- 로그 누락 가능
- GlobalExceptionHandler 미사용

좋은 예:

```java
@GetMapping("/users/{userId}")
public ApiResponse<UserResponse> getUser(@PathVariable Long userId) {
    return ApiResponse.success(userService.getUser(userId));
}
```

```java
@ExceptionHandler(BusinessException.class)
public ResponseEntity<ApiResponse<Void>> handleBusinessException(BusinessException exception) {
    ErrorCode errorCode = exception.getErrorCode();

    return ResponseEntity
            .status(errorCode.getStatus())
            .body(ApiResponse.fail(errorCode.name(), errorCode.getMessage()));
}
```

---

### [Troubleshooting]

문제: 오류 응답 형식이 API마다 다름

```text
원인:
Controller마다 try-catch로 직접 응답 생성

해결:
GlobalExceptionHandler로 예외 처리 통합
ApiResponse 또는 ErrorResponse Convention 적용
```

문제: 없는 데이터 조회 시 500 발생

```text
원인:
Optional.get 직접 호출
NoSuchElementException 발생

해결:
Service에서 orElseThrow로 BusinessException 발생
ErrorCode는 USER_NOT_FOUND 또는 RESOURCE_NOT_FOUND 사용
```

문제: Validation 실패 응답이 보기 어려움

```text
원인:
MethodArgumentNotValidException handler 없음
FieldError 응답 구조 없음

해결:
Validation Exception Handler 추가
fieldErrors 구조 정의
```

문제: Client에 DB 오류 메시지가 노출됨

```text
원인:
Exception message를 그대로 응답에 포함

해결:
Unexpected Exception은 generic message 반환
상세 원인은 server log에만 기록
```

---

### [FAQ]

Q. Exception Handling에서 가장 흔한 실수는?

A.
Controller마다 try-catch를 반복하고 내부 예외 메시지를 그대로 Client에 반환하는 실수다.

Q. 모든 예외를 Exception.class 하나로 처리해도 돼?

A.
권장하지 않는다. Validation, BusinessException, TypeMismatch, Unexpected Exception은 구분해서 처리하는 것이 좋다.

Q. ErrorCode 없이 message만 반환하면 왜 안 좋아?

A.
Frontend가 안정적으로 분기 처리하기 어렵고 메시지 변경 시 로직이 깨질 수 있다.

---

# 11. GlobalExceptionHandler 구조 예시

## 11.1 Foundation Example

### [개념]

Foundation Example은 Spring Boot 기초 프로젝트에서 사용할 수 있는 GlobalExceptionHandler 구조 예시다.

프로젝트 규모에 따라 ApiResponse, ErrorResponse, ErrorCode 구조는 조정할 수 있다.

---

### [실무]

ErrorCode:

```java
public enum ErrorCode {

    INVALID_REQUEST(400, "요청 값이 올바르지 않습니다."),
    TYPE_MISMATCH(400, "요청 값의 타입이 올바르지 않습니다."),
    MISSING_PARAMETER(400, "필수 요청 파라미터가 누락되었습니다."),
    INVALID_JSON(400, "요청 본문을 읽을 수 없습니다."),

    USER_NOT_FOUND(404, "사용자를 찾을 수 없습니다."),
    POST_NOT_FOUND(404, "게시글을 찾을 수 없습니다."),

    DUPLICATED_EMAIL(409, "이미 사용 중인 이메일입니다."),
    ALREADY_LIKED(409, "이미 좋아요한 게시글입니다."),

    NO_PERMISSION(403, "요청한 작업에 대한 권한이 없습니다."),

    EXTERNAL_API_ERROR(502, "외부 API 호출 중 오류가 발생했습니다."),
    INTERNAL_SERVER_ERROR(500, "서버 내부 오류가 발생했습니다.");

    private final int status;
    private final String message;

    ErrorCode(int status, String message) {
        this.status = status;
        this.message = message;
    }

    public int getStatus() {
        return status;
    }

    public String getMessage() {
        return message;
    }
}
```

BusinessException:

```java
public class BusinessException extends RuntimeException {

    private final ErrorCode errorCode;

    public BusinessException(ErrorCode errorCode) {
        super(errorCode.getMessage());
        this.errorCode = errorCode;
    }

    public BusinessException(ErrorCode errorCode, Throwable cause) {
        super(errorCode.getMessage(), cause);
        this.errorCode = errorCode;
    }

    public ErrorCode getErrorCode() {
        return errorCode;
    }
}
```

FieldErrorResponse:

```java
public record FieldErrorResponse(
        String field,
        String message
) {
}
```

ApiResponse:

```java
public record ApiResponse<T>(
        boolean success,
        String message,
        T data,
        String errorCode
) {
    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(true, "success", data, null);
    }

    public static <T> ApiResponse<T> fail(String errorCode, String message) {
        return new ApiResponse<>(false, message, null, errorCode);
    }

    public static <T> ApiResponse<T> fail(String errorCode, String message, T data) {
        return new ApiResponse<>(false, message, data, errorCode);
    }
}
```

GlobalExceptionHandler:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    private static final Logger log = LoggerFactory.getLogger(GlobalExceptionHandler.class);

    @ExceptionHandler(BusinessException.class)
    public ResponseEntity<ApiResponse<Void>> handleBusinessException(
            BusinessException exception
    ) {
        ErrorCode errorCode = exception.getErrorCode();

        log.warn("BusinessException: errorCode={}, message={}",
                errorCode.name(),
                exception.getMessage());

        return ResponseEntity
                .status(errorCode.getStatus())
                .body(ApiResponse.fail(errorCode.name(), errorCode.getMessage()));
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ApiResponse<List<FieldErrorResponse>>> handleValidationException(
            MethodArgumentNotValidException exception
    ) {
        List<FieldErrorResponse> fieldErrors = exception.getBindingResult()
                .getFieldErrors()
                .stream()
                .map(error -> new FieldErrorResponse(
                        error.getField(),
                        error.getDefaultMessage()
                ))
                .toList();

        return ResponseEntity
                .badRequest()
                .body(ApiResponse.fail(
                        ErrorCode.INVALID_REQUEST.name(),
                        ErrorCode.INVALID_REQUEST.getMessage(),
                        fieldErrors
                ));
    }

    @ExceptionHandler(MethodArgumentTypeMismatchException.class)
    public ResponseEntity<ApiResponse<Void>> handleTypeMismatchException(
            MethodArgumentTypeMismatchException exception
    ) {
        return ResponseEntity
                .badRequest()
                .body(ApiResponse.fail(
                        ErrorCode.TYPE_MISMATCH.name(),
                        ErrorCode.TYPE_MISMATCH.getMessage()
                ));
    }

    @ExceptionHandler(MissingServletRequestParameterException.class)
    public ResponseEntity<ApiResponse<Void>> handleMissingParameterException(
            MissingServletRequestParameterException exception
    ) {
        return ResponseEntity
                .badRequest()
                .body(ApiResponse.fail(
                        ErrorCode.MISSING_PARAMETER.name(),
                        ErrorCode.MISSING_PARAMETER.getMessage()
                ));
    }

    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ResponseEntity<ApiResponse<Void>> handleHttpMessageNotReadableException(
            HttpMessageNotReadableException exception
    ) {
        return ResponseEntity
                .badRequest()
                .body(ApiResponse.fail(
                        ErrorCode.INVALID_JSON.name(),
                        ErrorCode.INVALID_JSON.getMessage()
                ));
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ApiResponse<Void>> handleException(Exception exception) {
        log.error("Unexpected exception occurred", exception);

        return ResponseEntity
                .status(500)
                .body(ApiResponse.fail(
                        ErrorCode.INTERNAL_SERVER_ERROR.name(),
                        ErrorCode.INTERNAL_SERVER_ERROR.getMessage()
                ));
    }
}
```

---

### [핵심]

이 구조가 처리하는 예외:

- BusinessException
- MethodArgumentNotValidException
- MethodArgumentTypeMismatchException
- MissingServletRequestParameterException
- HttpMessageNotReadableException
- Exception fallback

확장 가능 예외:

- ConstraintViolationException
- BindException
- AccessDeniedException
- ExternalApiException
- FileUploadException
- DataIntegrityViolationException

---

### [FAQ]

Q. 이 예시를 그대로 써도 돼?

A.
기초 구조로 사용할 수 있다. 다만 프로젝트의 ApiResponse 형식, HTTP Status 정책, ErrorCode 목록에 맞게 조정해야 한다.

Q. Handler가 너무 많아지면 어떻게 해?

A.
예외 성격별로 method를 나누고 ErrorCode를 정리한다. 규모가 커지면 ErrorResponse Factory나 별도 Mapper를 둘 수 있다.

---

# 12. Exception Handling Checklist

## 12.1 Review Checklist

### [개념]

Exception Handling Checklist는 Backend Agent가 Spring Boot 예외 처리 구조를 생성하거나 검수할 때 사용하는 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] GlobalExceptionHandler가 존재하는가?
- [ ] @RestControllerAdvice를 사용하는가?
- [ ] Controller마다 try-catch를 반복하지 않는가?
- [ ] BusinessException 또는 CustomException이 있는가?
- [ ] ErrorCode 기준이 있는가?
- [ ] Error Response 형식이 통일되어 있는가?
- [ ] Validation Exception을 처리하는가?
- [ ] MethodArgumentNotValidException handler가 있는가?
- [ ] TypeMismatch 예외를 처리하는가?
- [ ] Missing Parameter 예외를 처리하는가?
- [ ] JSON Parse Error를 처리하는가?
- [ ] Repository Optional.empty를 Service에서 CustomException으로 변환하는가?
- [ ] Optional.get을 직접 사용하지 않는가?
- [ ] null 반환으로 오류를 표현하지 않는가?
- [ ] 권한 없음과 인증 실패를 구분하는가?
- [ ] 예상하지 못한 Exception fallback이 있는가?
- [ ] fallback 응답에서 내부 메시지를 노출하지 않는가?
- [ ] stack trace를 Client에 반환하지 않는가?
- [ ] 서버 로그에는 원인 추적 정보가 남는가?
- [ ] 로그에 민감정보를 남기지 않는가?
- [ ] 외부 API 실패를 내부 ErrorCode로 변환하는가?
- [ ] HTTP Status와 ErrorCode 정책이 일관적인가?
- [ ] Frontend가 처리 가능한 errorCode를 제공하는가?
```

---

### [실무]

검수 흐름:

```text
Controller 확인
→ try-catch 반복 여부 확인
→ Service CustomException 확인
→ ErrorCode 확인
→ GlobalExceptionHandler 확인
→ Validation Handler 확인
→ TypeMismatch Handler 확인
→ Not Found 처리 확인
→ Security 예외 경계 확인
→ External API 예외 확인
→ Logging 확인
→ Error Response 형식 확인
```

---

### [FAQ]

Q. Exception Handling 검수에서 가장 먼저 볼 것은?

A.
Controller마다 try-catch를 반복하지 않고 GlobalExceptionHandler로 공통 처리하는지 먼저 확인한다.

Q. 예외 처리 품질의 핵심 기준은?

A.
ErrorCode 일관성, Error Response 통일, CustomException 사용, Validation 처리, 내부 정보 비노출, Logging 분리다.

---

# Retrieval Queries

### [FAQ]

Q. Spring Boot 예외 처리는 어디서 해?
A. Controller마다 처리하지 않고 @RestControllerAdvice 기반 GlobalExceptionHandler에서 공통 처리하는 것이 좋다.

Q. GlobalExceptionHandler는 뭐야?
A. Application 전역에서 발생한 예외를 잡아 일관된 API Error Response로 변환하는 클래스다.

Q. @RestControllerAdvice는 뭐야?
A. REST API Controller 전역 예외를 처리하고 JSON 응답을 반환하기 위한 Spring Annotation이다.

Q. @ExceptionHandler는 뭐야?
A. 특정 예외 타입이 발생했을 때 실행할 handler method를 지정하는 Annotation이다.

Q. Controller에서 try-catch를 쓰면 안 돼?
A. 특수한 경우가 아니면 지양한다. Controller마다 try-catch를 반복하면 Error Response 일관성이 깨진다.

Q. Service에서 예외를 던져도 돼?
A. 된다. 사용자 없음, 중복 데이터, 권한 없음 같은 비즈니스 오류는 Service에서 CustomException으로 발생시키는 것이 좋다.

Q. Custom Exception은 언제 만들어?
A. 사용자 없음, 권한 없음, 중복 데이터, 잘못된 상태 전환처럼 비즈니스 의미가 있는 오류에 사용한다.

Q. BusinessException은 뭐야?
A. Application 비즈니스 규칙 위반을 표현하는 Custom RuntimeException이다.

Q. ErrorCode는 왜 필요해?
A. Frontend나 Agent가 문자열 메시지가 아니라 안정적인 코드 기준으로 오류를 처리할 수 있기 때문이다.

Q. Error Response에는 무엇이 들어가?
A. errorCode, message가 기본이고 Validation 실패에는 fieldErrors를 포함할 수 있다.

Q. HTTP Status와 ErrorCode 차이는?
A. HTTP Status는 프로토콜 수준 결과이고 ErrorCode는 Application 오류를 세부 구분하는 코드다.

Q. 실패 응답도 HTTP 200으로 내려도 돼?
A. 프로젝트 규칙에 따라 가능하지만 REST API 관점에서는 오류 상황에 맞는 HTTP Status를 사용하는 방식이 명확하다.

Q. MethodArgumentNotValidException은 언제 발생해?
A. @Valid @RequestBody로 받은 Request DTO의 Bean Validation이 실패했을 때 주로 발생한다.

Q. Validation 실패는 어디서 처리해?
A. GlobalExceptionHandler에서 MethodArgumentNotValidException을 처리해 공통 Error Response로 변환한다.

Q. @Valid를 안 붙이면 어떻게 돼?
A. Request DTO에 Validation Annotation이 있어도 검증이 실행되지 않을 수 있다.

Q. ConstraintViolationException은 언제 발생해?
A. @RequestParam, @PathVariable, method parameter validation이 실패했을 때 발생할 수 있다.

Q. @Valid와 @Validated 차이는?
A. @Valid는 Bean Validation 표준이고 @Validated는 Spring 확장 기능이다. method parameter validation에서는 @Validated가 필요할 수 있다.

Q. 숫자 id 자리에 문자열을 보내면 어떤 예외가 나?
A. MethodArgumentTypeMismatchException이 발생할 수 있다.

Q. JSON 형식이 깨지면 어떤 예외가 나?
A. HttpMessageNotReadableException이 발생할 수 있다.

Q. 필수 RequestParam이 없으면 어떤 예외가 나?
A. MissingServletRequestParameterException이 발생할 수 있다.

Q. 데이터가 없으면 null을 반환해도 돼?
A. 권장하지 않는다. Service에서 CustomException을 발생시키고 GlobalExceptionHandler에서 404 응답으로 변환하는 것이 좋다.

Q. findById().get()을 쓰면 왜 안 좋아?
A. 값이 없을 때 NoSuchElementException이 발생하고 ErrorCode와 응답 메시지를 통제하기 어렵다.

Q. Optional.empty는 어디서 처리해?
A. Service에서 orElseThrow로 CustomException으로 변환하는 것이 좋다.

Q. 삭제된 데이터는 Not Found로 처리해도 돼?
A. 가능하다. 보안이나 사용자 경험상 삭제된 데이터와 존재하지 않는 데이터를 같은 404로 처리할 수 있다.

Q. 401과 403 차이는?
A. 401은 인증이 필요하거나 인증이 실패한 상태이고, 403은 인증은 되었지만 권한이 없는 상태다.

Q. 게시글 작성자만 수정 가능 검사는 어디서 해?
A. Service에서 Entity를 조회한 뒤 작성자 여부를 확인하고 권한이 없으면 BusinessException을 발생시키는 것이 좋다.

Q. JWT 만료 예외도 GlobalExceptionHandler에서 처리해?
A. Security Filter 단계에서 발생한 예외는 GlobalExceptionHandler보다 Security Exception Handler에서 처리될 수 있다.

Q. 외부 API 오류 메시지를 그대로 내려도 돼?
A. 권장하지 않는다. 외부 시스템 내부 메시지나 민감정보가 노출될 수 있으므로 내부 ErrorCode와 메시지로 변환하는 것이 좋다.

Q. 외부 API 실패는 어떻게 처리해?
A. ExternalApiException이나 BusinessException으로 변환하고 GlobalExceptionHandler에서 통제된 Error Response로 반환한다.

Q. 예외 메시지를 Client와 Log에 똑같이 남기면 돼?
A. 아니다. Client 응답은 안전하고 간결해야 하며 서버 로그는 원인 추적에 필요한 정보를 포함할 수 있다.

Q. 모든 예외를 ERROR로 찍어야 해?
A. 아니다. Validation 실패나 비즈니스 조건 위반 같은 예상 가능한 오류는 WARN 또는 INFO로 관리할 수 있다.

Q. 로그에 토큰을 남겨도 돼?
A. 안 된다. Access Token, Refresh Token, API Key, Password 같은 민감정보는 로그에 남기면 안 된다.

Q. Exception.class handler는 꼭 필요해?
A. 예상하지 못한 예외를 통제하기 위해 fallback으로 두는 것이 좋다. 다만 내부 메시지를 그대로 내려보내면 안 된다.

Q. 모든 예외를 Exception.class 하나로 처리해도 돼?
A. 권장하지 않는다. Validation, BusinessException, TypeMismatch, Unexpected Exception은 구분해서 처리하는 것이 좋다.

Q. ErrorCode 없이 message만 반환하면 왜 안 좋아?
A. Frontend가 안정적으로 분기 처리하기 어렵고 메시지 변경 시 로직이 깨질 수 있다.

Q. stack trace를 Client에 반환해도 돼?
A. 안 된다. stack trace는 서버 로그에만 남기고 Client에는 통제된 메시지를 반환한다.

Q. GlobalExceptionHandler가 모든 예외를 잡아?
A. Controller 이후 흐름의 예외는 처리할 수 있지만 Filter나 Security 단계 예외는 별도 처리 구조가 필요할 수 있다.

Q. Exception Handling Anti Pattern은 뭐가 있어?
A. Controller try-catch 반복, 내부 메시지 노출, ErrorCode 없음, Optional.get 사용, null 반환, Validation 미처리 등이 있다.

Q. Exception Handling 검수에서 가장 먼저 볼 것은?
A. Controller마다 try-catch를 반복하지 않고 GlobalExceptionHandler로 공통 처리하는지 먼저 확인한다.

Q. 예외 처리 품질의 핵심 기준은?
A. ErrorCode 일관성, Error Response 통일, CustomException 사용, Validation 처리, 내부 정보 비노출, Logging 분리다.
