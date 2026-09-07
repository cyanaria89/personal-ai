# Java Part01 — Syntax & Type Foundation

---

# 1. Java Syntax Foundation

## 1.1 Java Syntax Purpose

### [개념]

Java Syntax Foundation은 Java 코드 작성의 최소 문법 기준이다.

이 문서는 사람 학습용 문법 설명서가 아니라 Backend Agent / Review Agent가 Java 기반 백엔드 코드를 생성하고 검토할 때 참조하는 RAG 문서다.

Java Syntax는 Spring Boot, JPA, Security, QueryDSL, Testing 코드의 기초가 된다.

---

### [핵심]

Java Syntax Foundation 핵심:

- Java는 정적 타입 언어
- Java는 객체지향 언어
- Java 코드는 Class 중심으로 구성
- Method는 실행 단위
- Variable은 값을 저장하는 이름 있는 공간
- Type은 값의 종류와 가능한 연산을 결정
- Statement는 실행 문장
- Block은 `{}`로 묶인 실행 범위
- Scope는 변수 접근 가능 범위
- Compile Time Type Check가 중요
- Runtime Error보다 Compile Error가 빠르게 발견되는 것이 좋음

---

### [실무]

2026 백엔드 실무 기준에서 Java 문법은 단순 암기가 아니라 코드 안정성 기준이다.

실무 판단:

```text
Requirement
→ Type 선택
→ Variable 선언
→ Method 설계
→ Condition / Loop 작성
→ Exception 가능성 확인
→ Null Safety 검토
→ Spring Boot 코드로 연결
```

Spring Boot 코드에서도 Java Syntax 문제가 발생하면 전체 Layer 품질이 떨어진다.

예:

- Controller Parameter Type 오류
- Service Method Return Type 오류
- Entity Field Type 부적절
- DTO Null 처리 누락
- Repository Optional 처리 누락
- 조건문 중첩 과다
- 반복문 중 Collection 수정 오류

---

### [FAQ]

Q. Java Syntax Foundation은 문법 공부용이야?
A. 아니다. Backend Agent가 Java 코드를 안정적으로 생성하고 검토하기 위한 기초 규칙 문서다.

Q. Java 문법에서 가장 중요한 기준은 뭐야?
A. Type Safety, Null Safety, Method 책임, 조건 흐름, 반복 처리 안정성이다.

Q. Spring Boot 개발에도 Java Syntax 문서가 필요해?
A. 필요하다. Spring Boot 코드도 결국 Java Class, Method, Type, Condition, Loop로 작성된다.

---

# 2. Variable and Type Rules

## 2.1 Variable Rules

### [개념]

Variable은 값을 저장하고 참조하기 위한 이름 있는 공간이다.

Java Variable은 반드시 Type을 가진다.

```java
int count = 10;
String name = "user";
Long userId = 1L;
```

Variable은 선언 위치에 따라 Scope와 Lifetime이 달라진다.

---

### [핵심]

Variable 핵심:

- variable
- type
- name
- value
- declaration
- initialization
- assignment
- scope
- lifetime
- local variable
- field
- parameter
- final variable

변수 종류:

- Local Variable
- Instance Field
- Static Field
- Method Parameter

---

### [실무]

실무 변수 작성 기준:

- 변수명은 의미 중심으로 작성
- 축약어 남용 금지
- 하나의 변수에 여러 의미 부여 금지
- 가능한 좁은 Scope에서 선언
- 사용 전 반드시 초기화
- 값이 바뀌지 않으면 `final` 검토
- Type은 데이터 의미와 DB 매핑 기준 고려

좋은 예:

```java
Long userId = request.userId();
String email = request.email();
int pageSize = 20;
```

나쁜 예:

```java
Long id;
String s;
int a;
```

주의:

- Local Variable은 초기화하지 않으면 사용 불가
- Field는 기본값이 있지만 의도 없는 기본값 사용 주의
- Wrapper Type은 null 가능성 검토 필요
- Primitive Type은 null을 가질 수 없음

---

### [FAQ]

Q. Java 변수는 반드시 타입이 있어야 해?
A. 그렇다. Java는 정적 타입 언어라 변수 선언 시 타입이 필요하다.

Q. 변수명은 어떻게 짓는 게 좋아?
A. 데이터 의미가 드러나도록 명확하게 작성한다. `a`, `temp`, `data` 같은 모호한 이름은 피한다.

Q. 변수는 어디에 선언하는 게 좋아?
A. 필요한 가장 좁은 Scope 안에 선언하는 것이 좋다.

---

## 2.2 Primitive Type Rules

### [개념]

Primitive Type은 Java의 기본 값 타입이다.

Primitive Type은 객체가 아니며 null을 가질 수 없다.

대표 Primitive Type:

```text
byte
short
int
long
float
double
char
boolean
```

---

### [핵심]

Primitive Type 핵심:

- primitive type
- int
- long
- double
- boolean
- char
- value type
- cannot be null
- default value
- memory efficient
- arithmetic operation

주요 사용:

```text
작은 정수 계산 → int
큰 정수 계산 → long
참/거짓 → boolean
실수 계산 → double
문자 하나 → char
```

---

### [실무]

백엔드 실무에서 Primitive Type은 null이 불가능한 필수 값에 적합하다.

권장:

- 반드시 값이 있어야 하는 계산 값 → primitive
- true / false가 항상 정해지는 값 → boolean
- 단순 카운트 → int 또는 long
- null 상태가 의미 없는 내부 계산 → primitive

주의:

- DB nullable 컬럼과 직접 매핑 시 primitive 사용 주의
- Entity Field에서는 Wrapper Type이 더 적합한 경우 많음
- `boolean`은 null 불가
- null / true / false 3상태가 필요하면 `Boolean` 검토
- 금액 계산에 `double` 사용 주의

예:

```java
private int viewCount;
private boolean active;
```

DB nullable과 연결되는 경우:

```java
private Long userId;
private Boolean emailVerified;
```

---

### [FAQ]

Q. primitive type은 null을 가질 수 있어?
A. 없다. primitive type은 값 자체를 저장하며 null을 표현할 수 없다.

Q. Entity Field에 int를 써도 돼?
A. 가능하지만 DB nullable 여부를 확인해야 한다. null 가능성이 있으면 Integer를 검토한다.

Q. boolean과 Boolean 차이는?
A. boolean은 null을 가질 수 없고 Boolean은 null을 가질 수 있는 Wrapper Type이다.

---

## 2.3 Reference Type Rules

### [개념]

Reference Type은 객체의 실제 값이 아니라 객체를 가리키는 참조를 저장하는 타입이다.

대표 Reference Type:

```text
String
Array
Class
Interface
Enum
Wrapper Type
Collection
DTO
Entity
```

예:

```java
String email = "user@example.com";
User user = new User(email);
List<String> names = new ArrayList<>();
```

---

### [핵심]

Reference Type 핵심:

- reference type
- object reference
- null
- Class
- Interface
- String
- Wrapper Type
- Collection
- DTO
- Entity
- heap object
- NullPointerException

---

### [실무]

Reference Type은 null 가능성을 반드시 검토한다.

권장:

- 필수 Reference는 생성자 또는 Validation으로 검증
- null 가능성이 있으면 Method 이름이나 반환 타입으로 명확화
- Collection 반환은 null보다 empty collection 권장
- Entity / DTO Field는 null 정책을 명확히 설정
- Repository 조회 결과는 Optional 처리 권장

예:

```java
public User(String email) {
    this.email = Objects.requireNonNull(email, "email must not be null");
}
```

주의:

- Reference Type은 null 가능
- null 상태에서 Method 호출 시 NullPointerException 발생
- Method Chain 중간값 null 주의
- DTO Mapping 시 null Field 확인 필요

---

### [FAQ]

Q. Reference Type은 null을 가질 수 있어?
A. 가능하다. 그래서 NullPointerException 위험을 항상 검토해야 한다.

Q. String은 primitive type이야?
A. 아니다. String은 Reference Type이다.

Q. Collection 반환은 null이 좋아?
A. 대부분 empty collection이 좋다. 호출자가 null check를 덜 해도 된다.

---

## 2.4 Wrapper Type Rules

### [개념]

Wrapper Type은 primitive type을 객체로 감싼 Reference Type이다.

대표 Wrapper Type:

```text
int → Integer
long → Long
double → Double
boolean → Boolean
char → Character
```

---

### [핵심]

Wrapper Type 핵심:

- Wrapper Type
- Integer
- Long
- Double
- Boolean
- Character
- nullable
- autoboxing
- unboxing
- primitive conversion
- Entity Field
- DTO Field

---

### [실무]

백엔드 실무에서 Wrapper Type은 DB nullable 값, Entity ID, DTO Field에 자주 사용된다.

권장:

```text
Entity ID → Long
DB BIGINT → Long
nullable 정수 → Integer / Long
nullable boolean → Boolean
Request DTO optional field → Wrapper Type
```

예:

```java
private Long userId;
private Integer age;
private Boolean active;
```

주의:

- Wrapper Type은 null 가능
- unboxing 시 NullPointerException 발생 가능
- `Integer` 비교에 `==` 사용 주의
- Entity ID는 보통 `Long`
- primitive와 Wrapper 혼용 시 null 정책 명확화

나쁜 예:

```java
Integer count = null;
int result = count; // NullPointerException
```

좋은 예:

```java
Integer count = null;
int result = count == null ? 0 : count;
```

---

### [FAQ]

Q. int와 Integer 차이는?
A. int는 primitive type이고 Integer는 null을 가질 수 있는 Wrapper Type이다.

Q. Entity ID는 왜 Long을 많이 써?
A. DB BIGINT와 매핑하기 좋고 데이터 증가에도 비교적 안전하기 때문이다.

Q. Wrapper Type을 쓰면 안전해?
A. null 표현은 가능하지만 unboxing 시 NullPointerException이 발생할 수 있어 주의해야 한다.

---

# 3. Type Selection Rules

## 3.1 Backend Type Selection

### [개념]

Type Selection은 데이터 의미, null 가능성, DB 매핑, 계산 정확도, API 응답 구조를 기준으로 타입을 선택하는 작업이다.

---

### [핵심]

타입 선택 기준:

```text
정수 ID → Long
작은 정수 계산 → int
큰 정수 계산 → long / Long
금액 / 정밀 계산 → BigDecimal
참/거짓 필수 값 → boolean
참/거짓 nullable 값 → Boolean
문자열 → String
날짜 → LocalDate
날짜 + 시간 → LocalDateTime
순간 시각 → Instant
목록 → List<T>
중복 제거 → Set<T>
Key-Value → Map<K, V>
조회 결과 없음 가능 → Optional<T>
```

---

### [실무]

Spring Boot / JPA 기준 Type Selection:

```text
Request Parameter
→ String / Long / Integer / Enum

DTO Field
→ String / Long / Boolean / LocalDate / LocalDateTime

Entity ID
→ Long

Entity Status
→ Enum

Entity CreatedAt
→ LocalDateTime

Money
→ BigDecimal

Repository findById
→ Optional<Entity>

API List Response
→ List<ResponseDto>
```

예:

```java
public record UserResponse(
    Long userId,
    String email,
    Boolean active,
    LocalDateTime createdAt
) {
}
```

주의:

- 금액 계산에 `double` 사용 금지에 가깝게 검토
- Entity ID에 `String` 사용 시 이유 필요
- 날짜를 문자열로만 관리하지 않음
- Boolean은 null 가능성이 필요한 경우만 사용
- 모든 숫자를 Long으로 통일하는 것도 과할 수 있음

---

### [FAQ]

Q. Entity ID는 보통 어떤 타입을 써?
A. 보통 Long을 사용한다.

Q. 금액은 어떤 타입을 써야 해?
A. 정밀도 문제가 있으므로 BigDecimal을 우선 검토한다.

Q. 날짜는 String으로 저장해도 돼?
A. 신규 백엔드 코드는 LocalDate, LocalDateTime 같은 java.time API를 우선 검토한다.

---

## 3.2 String Rules

### [개념]

String은 문자열을 표현하는 Reference Type이다.

String은 불변 객체다.

```java
String name = "Java";
```

String 값이 변경되는 것처럼 보이는 연산은 실제로 새 String 객체를 만드는 방식이다.

---

### [핵심]

String 핵심:

- String
- Reference Type
- immutable
- text data
- equals
- length
- trim
- isBlank
- isEmpty
- concat
- StringBuilder
- String comparison

---

### [실무]

String 실무 기준:

- 문자열 내용 비교는 `equals()` 사용
- null 가능성이 있으면 `Objects.equals()` 검토
- 빈 문자열과 공백 문자열 구분
- 사용자 입력은 trim / blank 검토
- 반복 결합은 StringBuilder 검토
- 민감정보 문자열 로그 출력 주의

좋은 예:

```java
if ("ACTIVE".equals(status)) {
    return true;
}
```

null-safe 비교:

```java
if (Objects.equals(requestStatus, savedStatus)) {
    return true;
}
```

주의:

- `==`는 문자열 내용 비교가 아니라 참조 비교
- `isEmpty()`는 길이 0만 확인
- `isBlank()`는 공백만 있는 문자열도 확인
- 문자열로 상태값 관리하기보다 Enum 검토

---

### [FAQ]

Q. String 비교에 ==를 써도 돼?
A. 문자열 내용 비교는 equals를 사용해야 한다. ==는 참조 비교다.

Q. isEmpty와 isBlank 차이는?
A. isEmpty는 길이 0만 확인하고 isBlank는 공백만 있는 문자열도 비어 있다고 본다.

Q. String은 변경 가능한 객체야?
A. 아니다. String은 불변 객체다.

---

## 3.3 StringBuilder Rules

### [개념]

StringBuilder는 문자열을 반복적으로 조립할 때 사용하는 mutable 문자열 조립 객체다.

String 반복 결합보다 불필요한 객체 생성을 줄일 수 있다.

---

### [핵심]

StringBuilder 핵심:

- StringBuilder
- mutable
- append
- toString
- repeated concatenation
- performance
- text building

---

### [실무]

StringBuilder 적합 상황:

```text
반복문 안에서 문자열 누적
긴 문자열 단계적 생성
동적 Query 일부 생성
로그 메시지 조립
텍스트 리포트 생성
```

예:

```java
StringBuilder builder = new StringBuilder();

for (String name : names) {
    builder.append(name).append(",");
}

String result = builder.toString();
```

주의:

- 단순 문자열 결합은 `+` 사용해도 충분
- 가독성이 더 중요할 수 있음
- 멀티스레드 공유 상태로 사용하지 않음
- SQL Query 생성은 StringBuilder보다 QueryDSL / PreparedStatement / ORM 기준 검토

---

### [FAQ]

Q. StringBuilder는 언제 써?
A. 반복문에서 문자열을 계속 누적하거나 동적으로 긴 문자열을 조립할 때 쓴다.

Q. 항상 StringBuilder가 좋아?
A. 아니다. 단순 문자열 결합은 `+`가 더 읽기 쉽다.

Q. StringBuilder는 불변 객체야?
A. 아니다. 내부 상태가 변경되는 mutable 객체다.

---

# 4. Type Conversion Rules

## 4.1 Casting Rules

### [개념]

Casting은 값을 다른 타입으로 변환하는 작업이다.

Java Casting은 크게 자동 형변환과 강제 형변환으로 나뉜다.

```java
int count = 10;
long longCount = count; // 자동 형변환

long total = 100L;
int result = (int) total; // 강제 형변환
```

---

### [핵심]

Casting 핵심:

- type conversion
- casting
- implicit casting
- explicit casting
- widening conversion
- narrowing conversion
- data loss
- ClassCastException
- instanceof

---

### [실무]

Casting 실무 기준:

- 작은 범위 → 큰 범위는 비교적 안전
- 큰 범위 → 작은 범위는 데이터 손실 확인
- Object Casting 전 실제 타입 확인
- Raw Type 사용으로 인한 Casting 지양
- DTO Mapping 시 타입 불일치 확인
- API 요청 값 변환 실패 가능성 검토

주의:

```java
long value = 3_000_000_000L;
int converted = (int) value; // 데이터 손실 가능
```

Reference Type Casting:

```java
if (target instanceof User user) {
    return user.getEmail();
}
```

금지에 가까운 패턴:

```java
Object value = getValue();
User user = (User) value; // 실제 타입 불명확
```

---

### [FAQ]

Q. 강제 형변환은 위험해?
A. 데이터 손실이나 ClassCastException이 발생할 수 있어 실제 타입과 범위를 확인해야 한다.

Q. Object를 원하는 타입으로 바로 캐스팅해도 돼?
A. 권장하지 않는다. instanceof 확인이나 Generic 사용으로 타입 안정성을 확보하는 것이 좋다.

Q. 숫자 타입 변환에서 뭘 조심해야 해?
A. 큰 범위 타입을 작은 범위 타입으로 바꿀 때 데이터 손실을 조심해야 한다.

---

## 4.2 Autoboxing and Unboxing Rules

### [개념]

Autoboxing은 primitive type이 Wrapper Type으로 자동 변환되는 것이다.

Unboxing은 Wrapper Type이 primitive type으로 자동 변환되는 것이다.

```java
Integer count = 10; // autoboxing
int value = count;  // unboxing
```

---

### [핵심]

Autoboxing / Unboxing 핵심:

- autoboxing
- unboxing
- primitive type
- wrapper type
- Integer
- Long
- Boolean
- NullPointerException
- performance caution

---

### [실무]

실무 주의점:

- Wrapper Type이 null이면 unboxing 시 NPE 발생
- Entity / DTO nullable 값 계산 전 null check 필요
- Collection은 primitive type을 직접 담을 수 없어 Wrapper 사용
- 반복 계산에서 불필요한 boxing 비용 검토
- Boolean unboxing은 특히 주의

위험 예:

```java
Boolean active = null;

if (active) {
    return true;
}
```

안전 예:

```java
Boolean active = null;

if (Boolean.TRUE.equals(active)) {
    return true;
}
```

Integer 안전 처리:

```java
Integer count = null;
int safeCount = count == null ? 0 : count;
```

---

### [FAQ]

Q. unboxing에서 NullPointerException이 날 수 있어?
A. 가능하다. Wrapper Type이 null인데 primitive로 변환되면 NPE가 발생한다.

Q. Boolean 비교는 어떻게 하는 게 안전해?
A. `Boolean.TRUE.equals(value)` 형태가 null-safe하다.

Q. Collection에는 int를 넣을 수 있어?
A. 직접 넣을 수 없다. List<Integer>처럼 Wrapper Type을 사용한다.

---

# 5. Operator Rules

## 5.1 Arithmetic Operator Rules

### [개념]

Arithmetic Operator는 숫자 값을 계산하는 연산자다.

대표 연산자:

```text
+
-
*
/
%
```

---

### [핵심]

Arithmetic 핵심:

- addition
- subtraction
- multiplication
- division
- modulo
- integer division
- overflow
- precision
- BigDecimal

---

### [실무]

실무 계산 기준:

- 정수 나눗셈은 소수점 버림 주의
- 0으로 나누기 방지
- overflow 가능성 검토
- 금액 / 정밀 계산은 BigDecimal 검토
- 평균 계산 시 double 변환 명확화
- API 응답 계산 값은 단위와 반올림 기준 명확화

정수 나눗셈 주의:

```java
int result = 5 / 2; // 2
```

소수 계산:

```java
double result = 5.0 / 2; // 2.5
```

BigDecimal 예:

```java
BigDecimal price = new BigDecimal("1000.00");
BigDecimal tax = price.multiply(new BigDecimal("0.10"));
```

---

### [FAQ]

Q. Java에서 5 / 2 결과는?
A. int끼리 나누면 결과는 2다. 소수점은 버려진다.

Q. 금액 계산에 double을 써도 돼?
A. 정밀도 문제가 생길 수 있으므로 BigDecimal을 검토하는 것이 좋다.

Q. 나머지 연산자는 언제 써?
A. 짝수/홀수 판단, 주기 계산, 페이징 보조 계산 등에 사용할 수 있다.

---

## 5.2 Comparison Operator Rules

### [개념]

Comparison Operator는 두 값을 비교해 boolean 결과를 반환한다.

대표 연산자:

```text
==
!=
>
<
>=
<=
```

---

### [핵심]

Comparison 핵심:

- comparison
- boolean result
- primitive comparison
- reference comparison
- equals
- Objects.equals
- String comparison
- Wrapper comparison

---

### [실무]

비교 기준:

```text
primitive 값 비교 → ==
String 내용 비교 → equals()
객체 동등성 비교 → equals()
null-safe 객체 비교 → Objects.equals()
Enum 비교 → == 가능
Wrapper 숫자 비교 → equals 또는 값 변환 기준 확인
```

좋은 예:

```java
if (Objects.equals(userId, targetUserId)) {
    return true;
}
```

String 비교:

```java
if ("PUBLISHED".equals(status)) {
    return true;
}
```

Enum 비교:

```java
if (postStatus == PostStatus.PUBLISHED) {
    return true;
}
```

주의:

- Reference Type에 `==` 사용 시 참조 비교
- Wrapper Type `==` 비교는 캐싱 범위 등으로 혼선 가능
- String은 `equals()` 사용
- null 가능성이 있으면 `Objects.equals()` 사용

---

### [FAQ]

Q. 객체 비교에 ==를 쓰면 안 돼?
A. 객체 내용 비교는 equals를 사용해야 한다. ==는 참조가 같은지 비교한다.

Q. Enum 비교에는 ==를 써도 돼?
A. 가능하다. Enum은 정해진 상수 인스턴스라 == 비교가 일반적으로 사용된다.

Q. null-safe 비교는 어떻게 해?
A. Objects.equals(a, b)를 사용하면 null-safe하게 비교할 수 있다.

---

## 5.3 Logical Operator Rules

### [개념]

Logical Operator는 boolean 조건을 조합하는 연산자다.

대표 연산자:

```text
&&
||
!
```

---

### [핵심]

Logical 핵심:

- logical AND
- logical OR
- logical NOT
- short-circuit
- condition combination
- guard clause
- boolean expression

---

### [실무]

실무 조건식 기준:

- 조건식은 읽기 쉽게 작성
- 복잡한 조건은 Method로 분리
- `&&`는 앞 조건이 false면 뒤 조건을 평가하지 않음
- `||`는 앞 조건이 true면 뒤 조건을 평가하지 않음
- null check를 앞에 배치해 NPE 방지
- boolean 변수명은 의미 있게 작성

예:

```java
if (user != null && user.isActive()) {
    return true;
}
```

조건 분리:

```java
public boolean canPublish(Post post) {
    return post != null && post.isDraft() && post.hasContent();
}
```

주의:

- 조건식이 길어지면 가독성 저하
- 부정 조건 `!`가 많으면 이해 어려움
- NPE 가능 조건 순서 주의

---

### [FAQ]

Q. &&와 ||는 뒤 조건을 항상 실행해?
A. 아니다. short-circuit 평가로 결과가 확정되면 뒤 조건을 실행하지 않는다.

Q. null check는 조건식 어디에 둬야 해?
A. null 가능성이 있는 객체를 사용하기 전에 앞쪽에 둬야 한다.

Q. 조건식이 너무 길면 어떻게 해?
A. 의미 있는 Method로 분리하거나 boolean 변수로 나눠서 읽기 쉽게 만든다.

---

# 6. Condition Rules

## 6.1 If Statement Rules

### [개념]

if Statement는 조건에 따라 실행 흐름을 분기하는 문법이다.

```java
if (condition) {
    // execute
}
```

---

### [핵심]

if 핵심:

- if
- else if
- else
- condition
- boolean expression
- branch
- guard clause
- nested if
- validation

---

### [실무]

if 작성 기준:

- 정상 흐름보다 예외 흐름을 먼저 제거하는 guard clause 권장
- 중첩 if는 줄이는 방향 검토
- 조건식은 Method로 분리 가능
- null check는 초기에 처리
- Validation 로직은 명확하게 작성
- 비즈니스 규칙은 의미 있는 Method로 표현

나쁜 예:

```java
public void publish(Post post) {
    if (post != null) {
        if (post.isDraft()) {
            if (post.hasContent()) {
                post.publish();
            }
        }
    }
}
```

좋은 예:

```java
public void publish(Post post) {
    if (post == null) {
        throw new IllegalArgumentException("post must not be null");
    }

    if (!post.isDraft()) {
        throw new IllegalStateException("post must be draft");
    }

    if (!post.hasContent()) {
        throw new IllegalStateException("post must have content");
    }

    post.publish();
}
```

---

### [FAQ]

Q. 중첩 if가 많으면 어떻게 해?
A. guard clause, Method 분리, 정책 객체, enum 전략 등을 검토한다.

Q. if 조건식이 길면 어떻게 해?
A. 의미 있는 이름의 Method로 분리하는 것이 좋다.

Q. null check는 어디서 하는 게 좋아?
A. 객체 사용 전에 최대한 빠르게 처리하는 것이 좋다.

---

## 6.2 Switch Statement Rules

### [개념]

switch Statement는 하나의 값에 따라 여러 실행 경로 중 하나를 선택하는 분기 문법이다.

Java 17+에서는 switch expression도 사용할 수 있다.

---

### [핵심]

switch 핵심:

- switch
- case
- default
- enum switch
- switch expression
- branch selection
- readability
- exhaustiveness

---

### [실무]

switch 적합 상황:

```text
Enum 상태 분기
고정 코드 값 분기
명확한 타입별 처리
상태별 응답 메시지 선택
```

Enum switch 예:

```java
public String getLabel(PostStatus status) {
    return switch (status) {
        case DRAFT -> "Draft";
        case PUBLISHED -> "Published";
        case DELETED -> "Deleted";
    };
}
```

주의:

- 분기가 계속 늘어나면 다형성 검토
- 복잡한 비즈니스 로직을 switch에 몰아넣지 않음
- 문자열 switch보다 Enum 사용 검토
- default로 오류를 숨기지 않음
- 상태별 동작이 많으면 Enum Method 또는 Strategy Pattern 검토

---

### [FAQ]

Q. switch는 언제 쓰는 게 좋아?
A. Enum처럼 정해진 값에 따라 분기할 때 읽기 좋다.

Q. if-else와 switch 중 뭐가 좋아?
A. 범위 조건은 if가 적합하고 고정 값 분기는 switch가 적합하다.

Q. switch 분기가 너무 많으면 어떻게 해?
A. 다형성, Strategy Pattern, Enum Method로 분리하는 것을 검토한다.

---

## 6.3 Guard Clause Rules

### [개념]

Guard Clause는 Method 초반에 예외 조건이나 불가능한 조건을 먼저 처리하고 정상 흐름을 아래로 유지하는 패턴이다.

---

### [핵심]

Guard Clause 핵심:

- early return
- validation
- fail fast
- reduce nested if
- readability
- precondition
- business rule check

---

### [실무]

Guard Clause 적합 상황:

- null 검증
- 권한 검증
- 상태 검증
- 입력값 검증
- 비즈니스 규칙 위반 검증
- 더 이상 진행 불가 조건 처리

예:

```java
public void updateEmail(User user, String newEmail) {
    if (user == null) {
        throw new IllegalArgumentException("user must not be null");
    }

    if (newEmail == null || newEmail.isBlank()) {
        throw new IllegalArgumentException("email must not be blank");
    }

    user.updateEmail(newEmail);
}
```

주의:

- 너무 많은 guard clause는 Method 책임 과다 신호일 수 있음
- 검증 책임을 별도 Validator로 분리할 수 있음
- 예외 메시지는 원인 파악 가능하게 작성
- 민감정보는 예외 메시지에 포함하지 않음

---

### [FAQ]

Q. Guard Clause를 쓰는 이유는?
A. 중첩 if를 줄이고 예외 조건을 빠르게 제거해 정상 흐름을 읽기 쉽게 만들기 위해서다.

Q. Guard Clause는 무조건 좋은가?
A. 아니다. 너무 많으면 Method가 많은 책임을 가진다는 신호일 수 있다.

Q. Guard Clause에서는 return과 throw 중 뭘 써?
A. 검증 실패나 비즈니스 오류는 throw를 쓰고 단순 처리 종료는 return을 사용할 수 있다.

---

# 7. Loop Rules

## 7.1 For Loop Rules

### [개념]

for Loop는 정해진 횟수나 Collection 요소를 반복 처리하는 문법이다.

일반 for문:

```java
for (int i = 0; i < size; i++) {
    // execute
}
```

Enhanced for문:

```java
for (User user : users) {
    // execute
}
```

---

### [핵심]

for Loop 핵심:

- for
- index loop
- enhanced for
- iteration
- collection traversal
- break
- continue
- loop condition
- readability

---

### [실무]

for문 적합 상황:

- index가 필요한 반복
- break / continue 제어가 중요한 반복
- 복잡한 조건 흐름이 있는 반복
- Stream보다 명령형 코드가 더 읽기 쉬운 경우
- 예외 처리나 중간 종료가 필요한 경우

예:

```java
for (User user : users) {
    if (!user.isActive()) {
        continue;
    }

    sendNotification(user);
}
```

주의:

- 반복문 내부에서 원본 Collection 구조 변경 주의
- 중첩 반복문은 성능과 가독성 확인
- 반복문 내부 DB 호출은 N+1 또는 성능 문제 가능
- index 범위 오류 주의
- Collection이 null일 가능성 확인

---

### [FAQ]

Q. for문과 Stream 중 뭐가 좋아?
A. 단순 반복이나 복잡한 제어 흐름이 있으면 for문이 좋고, 필터/변환/집계가 명확하면 Stream이 좋다.

Q. 반복문 안에서 DB 조회해도 돼?
A. 가능은 하지만 성능 문제가 생길 수 있어 Batch 조회나 Join Fetch 등을 검토해야 한다.

Q. for문에서 continue는 언제 써?
A. 현재 요소를 건너뛰고 다음 요소로 넘어가야 할 때 사용한다.

---

## 7.2 While Loop Rules

### [개념]

while Loop는 조건이 true인 동안 반복 실행하는 문법이다.

```java
while (condition) {
    // execute
}
```

---

### [핵심]

while Loop 핵심:

- while
- condition based loop
- unknown iteration count
- infinite loop
- break condition
- state update

---

### [실무]

while문 적합 상황:

- 반복 횟수를 사전에 알기 어려움
- 특정 조건이 만족될 때까지 반복
- Queue 처리
- 입력 스트림 처리
- Polling 구조 일부

예:

```java
while (!queue.isEmpty()) {
    Task task = queue.poll();
    process(task);
}
```

주의:

- 무한 루프 방지
- 반복 조건 변경 여부 확인
- 외부 상태 의존 반복은 Timeout 검토
- 무한 Polling은 시스템 리소스 낭비 가능
- 백엔드 서버에서 while true 사용은 매우 신중해야 함

---

### [FAQ]

Q. while문은 언제 써?
A. 반복 횟수가 정해져 있지 않고 조건이 만족될 때까지 반복해야 할 때 사용한다.

Q. while true는 써도 돼?
A. 특별한 Worker Loop가 아니라면 피하는 것이 좋고 종료 조건과 리소스 제어가 필요하다.

Q. while문에서 가장 조심할 점은?
A. 조건이 바뀌지 않아 무한 루프가 되는 상황이다.

---

## 7.3 Collection Modification During Loop

### [개념]

Collection을 순회하는 중 원본 Collection의 구조를 변경하면 ConcurrentModificationException이 발생할 수 있다.

---

### [핵심]

위험 패턴:

- for-each 중 remove
- Stream 처리 중 원본 Collection 수정
- Iterator 외부에서 구조 변경
- 반복 중 add / remove
- ConcurrentModificationException

안전 대안:

- removeIf
- Iterator remove
- 새 Collection 생성
- Stream filter 후 collect
- 동시성 Collection 검토

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

또 다른 예:

```java
List<User> activeUsers = users.stream()
    .filter(User::isActive)
    .toList();
```

실무 기준:

- 삭제 목적이면 removeIf 우선 검토
- 필터링 결과가 필요하면 새 Collection 생성
- 원본 유지 여부 명확화
- 동시성 환경이면 별도 Collection 또는 Lock 검토
- JPA Entity Collection 변경은 연관관계 편의 Method와 orphanRemoval 정책 확인

---

### [FAQ]

Q. for-each 중 remove하면 왜 위험해?
A. 순회 중 Collection 구조가 바뀌어 ConcurrentModificationException이 발생할 수 있다.

Q. 조건에 맞는 요소를 삭제하려면?
A. removeIf를 사용하거나 Iterator remove를 사용한다.

Q. 원본은 유지하고 필터링 결과만 얻으려면?
A. Stream filter 후 새 List로 수집하는 방식이 좋다.

---

# 8. Scope and Block Rules

## 8.1 Block Scope Rules

### [개념]

Block은 `{}`로 묶인 코드 영역이다.

Block 내부에서 선언된 변수는 해당 Block 안에서만 접근할 수 있다.

```java
if (active) {
    String message = "active user";
}
```

---

### [핵심]

Block Scope 핵심:

- block
- scope
- local variable
- variable lifetime
- access range
- shadowing
- readability

---

### [실무]

Scope 실무 기준:

- 변수는 필요한 가장 좁은 Scope에 선언
- 불필요하게 Method 상단에 모두 선언하지 않음
- 동일 이름 변수로 shadowing 유발 금지
- block이 너무 길면 Method 분리 검토
- 변수 생명주기를 짧게 유지

좋은 예:

```java
if (user.isActive()) {
    String email = user.getEmail();
    sendEmail(email);
}
```

주의:

- Block 내부 변수는 외부에서 접근 불가
- 바깥 Scope 변수 재사용이 많으면 Method 책임 확인
- 긴 Method는 Scope 추적이 어려워짐

---

### [FAQ]

Q. Block 안에서 만든 변수는 밖에서 쓸 수 있어?
A. 없다. Block 내부에서 선언된 변수는 해당 Block 안에서만 접근 가능하다.

Q. 변수는 Method 맨 위에 몰아서 선언하는 게 좋아?
A. 아니다. 필요한 위치와 가장 좁은 Scope에 선언하는 것이 좋다.

Q. Scope가 넓으면 뭐가 문제야?
A. 변수 변경 가능성이 커지고 코드 추적이 어려워진다.

---

## 8.2 Method Scope and Parameter Rules

### [개념]

Method Parameter는 Method 호출 시 외부에서 전달되는 입력 값이다.

Method 내부 Scope에서 사용할 수 있다.

```java
public User findUser(Long userId) {
    // userId is parameter
}
```

---

### [핵심]

Parameter 핵심:

- method parameter
- input value
- scope
- validation
- null check
- parameter count
- DTO
- command object

---

### [실무]

Parameter 실무 기준:

- 필수 Parameter는 null 검증
- Parameter가 많으면 DTO / Command 객체 검토
- boolean flag parameter 남용 금지
- Parameter 재할당 지양
- Method 이름과 Parameter 의미 일치 필요
- Entity와 DTO를 혼동하지 않음

나쁜 예:

```java
public void createUser(String email, String password, String nickname, Boolean active, String role) {
}
```

좋은 예:

```java
public void createUser(CreateUserCommand command) {
}
```

검증 예:

```java
public User findUser(Long userId) {
    if (userId == null) {
        throw new IllegalArgumentException("userId must not be null");
    }

    return userRepository.findById(userId)
        .orElseThrow(() -> new UserNotFoundException(userId));
}
```

---

### [FAQ]

Q. Method Parameter가 많으면 어떻게 해?
A. Request DTO, Command 객체, Value Object로 묶는 것을 검토한다.

Q. Parameter null check는 꼭 해야 해?
A. 필수 값이면 해야 한다. 특히 Service Method 내부에서는 빠르게 실패시키는 것이 좋다.

Q. boolean Parameter는 왜 조심해야 해?
A. 호출 코드만 봐서는 true / false 의미가 불명확해질 수 있다.

---

# 9. Date and Time Foundation Rules

## 9.1 LocalDate and LocalDateTime Rules

### [개념]

Java의 Modern Date Time API는 날짜와 시간을 타입 안정적으로 표현한다.

대표 타입:

```text
LocalDate
LocalTime
LocalDateTime
Instant
ZonedDateTime
```

---

### [핵심]

Date Time 핵심:

- java.time
- LocalDate
- LocalTime
- LocalDateTime
- Instant
- ZonedDateTime
- DateTimeFormatter
- timezone
- createdAt
- updatedAt

---

### [실무]

백엔드 실무 기준:

```text
날짜만 필요 → LocalDate
시간만 필요 → LocalTime
날짜 + 시간 → LocalDateTime
UTC 순간 시각 → Instant
시간대 포함 필요 → ZonedDateTime
```

Spring Boot / JPA 실무:

```java
private LocalDate eventStartDate;
private LocalDateTime createdAt;
private LocalDateTime updatedAt;
```

주의:

- 신규 코드는 Date / Calendar보다 java.time 우선
- 시간대가 중요한 서비스는 LocalDateTime만으로 부족할 수 있음
- API 요청 / 응답 날짜 포맷 명확화
- DB 저장 시간 기준 통일
- createdAt / updatedAt 자동 처리 정책 확인

---

### [FAQ]

Q. 날짜는 String으로 처리해도 돼?
A. 신규 백엔드 코드는 LocalDate, LocalDateTime 같은 java.time API를 우선 검토한다.

Q. LocalDate와 LocalDateTime 차이는?
A. LocalDate는 날짜만 표현하고 LocalDateTime은 날짜와 시간을 함께 표현한다.

Q. 시간대가 중요하면 어떤 타입을 검토해?
A. Instant나 ZonedDateTime을 검토한다.

---

# 10. Syntax Anti Pattern Rules

## 10.1 Common Syntax Mistakes

### [개념]

Java Syntax Anti Pattern은 문법적으로 가능하지만 유지보수성, 안정성, 타입 안정성을 떨어뜨리는 코드 패턴이다.

---

### [핵심]

자주 발생하는 실수:

- String 비교에 `==` 사용
- Wrapper Type unboxing NPE
- 금액 계산에 double 사용
- 변수명 모호함
- Scope 과도하게 넓음
- Method Parameter 과다
- boolean flag Parameter 남용
- 중첩 if 과다
- switch에 비즈니스 로직 과다
- 반복문 중 Collection 수정
- null Collection 반환
- Object 반환 후 Casting
- Raw Type 사용
- 날짜를 String으로만 처리
- 무한 while Loop

---

### [실무]

검토 Flow:

```text
Code Review
→ Type 적절성 확인
→ null 가능성 확인
→ 비교 연산 확인
→ 조건문 중첩 확인
→ 반복문 안전성 확인
→ Scope 확인
→ Parameter 개수 확인
→ Date Time Type 확인
→ Anti Pattern 수정
```

예:

```text
문제: String 비교에 == 사용
원인: 참조 비교와 내용 비교 혼동
해결: equals 또는 Objects.equals 사용
```

예:

```text
문제: Boolean 값 if문에서 NPE 발생
원인: Boolean null 값 unboxing
해결: Boolean.TRUE.equals(value) 사용
```

---

### [FAQ]

Q. Java 문법 실수 중 가장 위험한 건 뭐야?
A. null 처리 누락, String 비교에 == 사용, Wrapper unboxing NPE, 반복 중 Collection 수정이 자주 문제된다.

Q. 문법적으로 맞으면 좋은 코드야?
A. 아니다. 문법적으로 가능해도 유지보수성과 안정성이 낮을 수 있다.

Q. Syntax Review는 어떤 순서로 해?
A. Type, Null Safety, Comparison, Condition, Loop, Scope, Parameter를 순서대로 확인한다.

---

# 11. Java Syntax Checklist

## 11.1 Syntax Review Checklist

### [개념]

Java Syntax Checklist는 Backend Agent / Review Agent가 Java 기초 코드의 오류 가능성을 빠르게 검토하기 위한 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] 변수명이 의미를 명확히 표현하는가?
- [ ] 변수 Scope가 불필요하게 넓지 않은가?
- [ ] primitive type과 Wrapper Type 선택이 적절한가?
- [ ] null 가능성이 있는 Reference Type을 검토했는가?
- [ ] Entity ID는 Long 사용을 우선 검토했는가?
- [ ] 금액 / 정밀 계산에 BigDecimal을 검토했는가?
- [ ] String 내용 비교에 equals를 사용했는가?
- [ ] 객체 null-safe 비교에 Objects.equals를 검토했는가?
- [ ] Boolean nullable 값 비교에 Boolean.TRUE.equals를 검토했는가?
- [ ] 강제 형변환 시 데이터 손실 가능성을 확인했는가?
- [ ] Object Casting 전 실제 타입을 확인했는가?
- [ ] 조건문 중첩이 과도하지 않은가?
- [ ] Guard Clause로 예외 흐름을 먼저 제거했는가?
- [ ] switch 분기가 과도하면 다형성을 검토했는가?
- [ ] 반복문 내부에서 원본 Collection을 직접 수정하지 않는가?
- [ ] while Loop에 종료 조건이 명확한가?
- [ ] Parameter 개수가 과도하지 않은가?
- [ ] boolean flag Parameter를 남용하지 않는가?
- [ ] 날짜 / 시간은 java.time API를 우선 검토했는가?
- [ ] null Collection 반환을 피했는가?
```

---

### [실무]

Review Agent 검토 순서:

```text
Variable Review
→ Type Review
→ Null Safety Review
→ Operator Review
→ Condition Review
→ Loop Review
→ Scope Review
→ Parameter Review
→ Date Time Review
→ Anti Pattern Review
```

---

### [FAQ]

Q. Java Syntax 검수에서 가장 먼저 볼 것은?
A. Type 선택과 null 가능성을 먼저 보는 것이 좋다.

Q. 조건문 검수 기준은?
A. 중첩이 과도하지 않은지, Guard Clause가 가능한지, 조건식 이름이 명확한지 확인한다.

Q. 반복문 검수 기준은?
A. Collection 수정 위험, 종료 조건, 반복문 내부 DB 호출, Stream 전환 가능성을 확인한다.

---

# 12. Backend Integration

## 12.1 Java Syntax to Spring Boot

### [개념]

Java Syntax Foundation은 Spring Boot Layered Architecture의 코드 안정성 기반이다.

Spring Boot 코드의 Controller, Service, Repository, Entity, DTO는 모두 Java Type과 Method로 구성된다.

---

### [핵심]

연결 대상:

- Controller Parameter
- Request DTO
- Response DTO
- Service Method
- Entity Field
- Repository Return Type
- Validation
- Exception Handling
- Optional Handling
- Collection Response
- Date Time Field

---

### [실무]

Spring Boot 연결 기준:

```text
Controller
→ Request Parameter Type 명확화
→ DTO Validation 연결

Service
→ Method Parameter 검증
→ Guard Clause 적용
→ Optional 처리
→ Custom Exception 변환

Entity
→ Field Type 적절성
→ nullable 여부 확인
→ 상태 변경 Method 연결

Repository
→ Optional<T> 처리
→ List<T> empty 반환 기준

DTO
→ String / Long / Boolean / LocalDateTime 타입 적절성
→ null 허용 정책 명확화
```

예:

```java
public UserResponse getUser(Long userId) {
    if (userId == null) {
        throw new IllegalArgumentException("userId must not be null");
    }

    User user = userRepository.findById(userId)
        .orElseThrow(() -> new UserNotFoundException(userId));

    return UserResponse.from(user);
}
```

---

### [FAQ]

Q. Java Syntax가 Spring Boot Service 코드에 어떤 영향을 줘?
A. Method Parameter, Return Type, Optional 처리, null 검증, 조건 흐름이 Service 안정성에 직접 영향을 준다.

Q. DTO Field Type은 어떻게 정해?
A. API 의미, null 허용 여부, 날짜/시간 표현, DB 매핑 기준을 함께 고려한다.

Q. Repository 결과가 없을 수 있으면 어떻게 해?
A. Optional을 사용하고 Service에서 orElseThrow로 명확한 예외로 변환하는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Java Syntax Foundation은 왜 필요해?
A. Backend Agent가 Java 코드를 생성하고 검토할 때 Type Safety, Null Safety, 조건문, 반복문 기준이 필요하기 때문이다.

Q. Java 변수는 어떻게 선언해?
A. Type과 변수명을 함께 선언한다. 예: `Long userId = 1L;`

Q. Java 변수명은 어떻게 짓는 게 좋아?
A. 데이터 의미가 드러나도록 명확하게 작성한다.

Q. primitive type과 reference type 차이는?
A. primitive type은 값 자체를 저장하고 null을 가질 수 없으며 reference type은 객체 참조를 저장하고 null을 가질 수 있다.

Q. int와 Integer 차이는?
A. int는 primitive type이고 Integer는 null을 가질 수 있는 Wrapper Type이다.

Q. long과 Long은 언제 구분해?
A. null이 필요 없는 내부 계산은 long, Entity ID나 nullable 값은 Long을 검토한다.

Q. Entity ID는 어떤 타입이 좋아?
A. 보통 Long을 사용한다.

Q. boolean과 Boolean 차이는?
A. boolean은 null을 가질 수 없고 Boolean은 null을 가질 수 있다.

Q. Boolean null-safe 비교는 어떻게 해?
A. `Boolean.TRUE.equals(value)`를 사용한다.

Q. Wrapper Type unboxing에서 뭐가 위험해?
A. Wrapper Type이 null이면 primitive로 변환될 때 NullPointerException이 발생할 수 있다.

Q. String은 primitive type이야?
A. 아니다. String은 Reference Type이다.

Q. String 비교에 ==를 써도 돼?
A. 문자열 내용 비교는 equals를 사용해야 한다. ==는 참조 비교다.

Q. null-safe 객체 비교는 어떻게 해?
A. `Objects.equals(a, b)`를 사용한다.

Q. isEmpty와 isBlank 차이는?
A. isEmpty는 길이 0만 확인하고 isBlank는 공백 문자열도 비어 있다고 본다.

Q. StringBuilder는 언제 써?
A. 반복문에서 문자열을 계속 누적하거나 동적으로 긴 문자열을 조립할 때 사용한다.

Q. 금액 계산에 double을 써도 돼?
A. 정밀도 문제가 생길 수 있으므로 BigDecimal을 검토하는 것이 좋다.

Q. Java에서 5 / 2 결과는?
A. int끼리 나누면 결과는 2다.

Q. 강제 형변환은 왜 조심해야 해?
A. 데이터 손실이나 ClassCastException이 발생할 수 있기 때문이다.

Q. Object Casting 전에 뭘 확인해야 해?
A. instanceof로 실제 타입을 확인하거나 Generic으로 타입 안정성을 확보해야 한다.

Q. if문 중첩이 많으면 어떻게 해?
A. Guard Clause, Method 분리, 정책 객체, enum 전략 등을 검토한다.

Q. Guard Clause는 왜 써?
A. 예외 조건을 먼저 제거해 정상 흐름을 읽기 쉽게 만들기 위해 사용한다.

Q. switch는 언제 쓰면 좋아?
A. Enum처럼 정해진 값에 따라 분기할 때 좋다.

Q. switch 분기가 많아지면 어떻게 해?
A. 다형성, Strategy Pattern, Enum Method 분리를 검토한다.

Q. for문과 Stream 중 뭐가 좋아?
A. 복잡한 제어 흐름은 for문이 좋고 필터/변환/집계가 명확하면 Stream이 좋다.

Q. 반복문 안에서 Collection remove를 해도 돼?
A. for-each 중 직접 remove는 위험하다. removeIf나 새 Collection 생성을 검토한다.

Q. ConcurrentModificationException은 왜 발생해?
A. Collection을 순회하는 중 구조가 변경되면 발생할 수 있다.

Q. while문에서 가장 조심할 점은?
A. 종료 조건이 없어 무한 루프가 되는 상황이다.

Q. 변수 Scope는 어떻게 잡아?
A. 필요한 가장 좁은 Scope에 선언하는 것이 좋다.

Q. Method Parameter가 많으면 어떻게 해?
A. Request DTO, Command 객체, Value Object로 묶는 것을 검토한다.

Q. boolean flag Parameter는 왜 조심해야 해?
A. 호출 코드에서 true / false 의미가 불명확해질 수 있기 때문이다.

Q. 날짜는 String으로 처리해도 돼?
A. 신규 백엔드 코드는 LocalDate, LocalDateTime 같은 java.time API를 우선 검토한다.

Q. LocalDate와 LocalDateTime 차이는?
A. LocalDate는 날짜만 표현하고 LocalDateTime은 날짜와 시간을 함께 표현한다.

Q. 시간대가 중요하면 어떤 타입을 써?
A. Instant나 ZonedDateTime을 검토한다.

Q. Java Syntax 코드 리뷰는 어떤 순서로 해?
A. Type, Null Safety, Comparison, Condition, Loop, Scope, Parameter, Date Time 순서로 검토한다.

Q. Java Syntax 다음 파트는 뭐야?
A. Java Part02 — Class, Object, Method, Constructor 문서로 이어지는 것이 좋다.
