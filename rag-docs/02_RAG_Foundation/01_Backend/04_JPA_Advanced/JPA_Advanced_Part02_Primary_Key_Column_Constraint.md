# JPA Advanced Part02 — Primary Key, Column Mapping, Constraint

---

# 1. Primary Key Mapping

## 1.1 Primary Key Purpose

### [개념]

Primary Key는 DB Table Row를 식별하는 고유 식별자다.

JPA Entity는 Primary Key와 Mapping되는 식별자 Field를 반드시 가져야 한다.

JPA는 Entity 식별자를 기준으로 Persistence Context에서 Entity를 관리한다.

---

### [핵심]

핵심 키워드:

- Primary Key
- Entity ID
- `@Id`
- `@GeneratedValue`
- Surrogate Key
- Natural Key
- Entity Identity
- Persistence Context
- First Level Cache
- Data Integrity

Primary Key 역할:

- DB Row 식별
- Entity 식별
- Persistence Context 관리 기준
- Repository `findById` 기준
- Foreign Key 참조 대상
- Entity Association 기준

---

### [실무]

SQL Foundation 연결:

```text
SQL Primary Key
→ JPA @Id
→ Entity Identity
→ Persistence Context 관리 기준
→ Repository findById 기준
→ Foreign Key 참조 대상
```

기본 예시:

```java
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long userId;
```

권장:

- 대부분 `Long` 타입 Surrogate Key 사용
- 비즈니스 값은 Primary Key로 사용 지양
- Primary Key는 변경하지 않음
- Primary Key Field 이름은 일관되게 유지
- `userId`, `postId`, `orderId`처럼 Entity 이름 기반 ID 권장
- DB 생성 전략과 JPA `GenerationType` 일치 확인

주의:

- Primary Key가 없으면 JPA Entity로 관리할 수 없다.
- Primary Key는 Entity 동일성 판단과 Persistence Context 관리에 직접 연결된다.
- Primary Key 변경은 연관관계, Foreign Key, Cache, Audit에 큰 영향을 준다.
- Natural Key는 변경 가능성이 있으면 Primary Key로 부적합하다.

---

### [FAQ]

Q. JPA Entity에는 Primary Key가 꼭 필요해?
A. 필요하다. JPA는 `@Id` 식별자를 기준으로 Entity를 Persistence Context에서 관리한다.

Q. Entity ID는 왜 중요한가?
A. Entity ID는 DB Row 식별, Repository 조회, Foreign Key 참조, Persistence Context 관리 기준이다.

Q. Primary Key는 변경해도 돼?
A. 권장하지 않는다. Primary Key는 Entity 식별성과 연관관계 기준이므로 변경하지 않는 것이 원칙이다.

Q. Entity ID Field 이름은 `id`와 `userId` 중 뭐가 좋아?
A. 둘 다 가능하지만 프로젝트 Convention을 통일해야 한다. RAG 검색과 코드 생성 기준에서는 `userId`, `postId`처럼 명확한 이름이 유리하다.

---

## 1.2 Surrogate Key and Natural Key

### [개념]

Surrogate Key는 비즈니스 의미가 없는 인공 식별자다.

Natural Key는 이메일, 주민번호, 상품코드처럼 비즈니스 의미를 가진 식별자다.

JPA 실무에서는 대부분 Surrogate Key를 Primary Key로 사용하고, Natural Key 후보는 Unique Column으로 관리한다.

---

### [핵심]

비교:

| 구분        | Surrogate Key      | Natural Key                           |
| ----------- | ------------------ | ------------------------------------- |
| 의미        | 비즈니스 의미 없음 | 비즈니스 의미 있음                    |
| 예시        | `userId`, `postId` | `email`, `phoneNumber`, `productCode` |
| 변경 가능성 | 낮음               | 요구사항에 따라 변경 가능             |
| PK 적합성   | 높음               | 신중히 검토                           |
| 권장 사용   | Primary Key        | Unique Column                         |

핵심 기준:

- Primary Key는 안정적이어야 함
- 비즈니스 값은 변경 가능성을 고려
- Natural Key는 Unique Constraint 후보
- Foreign Key 참조 안정성 우선
- Entity Identity와 Business Identity 분리

---

### [실무]

권장 예시:

```java
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long userId;

@Column(nullable = false, unique = true, length = 100)
private String email;
```

비권장 예시:

```java
@Id
private String email;
```

SQL Foundation 연결:

```text
SQL Primary Key
→ Surrogate Key

SQL Unique Constraint
→ Natural Key Candidate

email / phoneNumber / username
→ Unique Column
→ Not Primary Key
```

권장:

- `Long` Surrogate Key를 기본 선택지로 사용
- 이메일, 전화번호, 닉네임은 Unique Column으로 관리
- 외부 시스템 ID는 별도 Unique Column으로 관리 가능
- 비즈니스 식별자는 변경 정책과 중복 정책을 함께 검토
- 회원 탈퇴, 이메일 변경, 통합 계정 같은 요구사항을 고려

주의:

- 이메일은 변경될 수 있다.
- 전화번호는 재사용될 수 있다.
- 상품코드는 정책 변경 가능성이 있다.
- Natural Key를 Primary Key로 쓰면 Foreign Key 전체에 영향이 커진다.
- 비즈니스 값 변경이 곧 PK 변경이 되면 유지보수 난도가 높아진다.

---

### [FAQ]

Q. Surrogate Key는 뭐야?
A. 비즈니스 의미가 없는 인공 식별자이며 보통 `Long userId` 같은 형태로 사용한다.

Q. Natural Key는 뭐야?
A. 이메일, 전화번호, 상품코드처럼 비즈니스 의미를 가진 식별자다.

Q. 이메일을 Primary Key로 써도 돼?
A. 권장하지 않는다. 이메일은 변경될 수 있으므로 Unique Column으로 두는 것이 좋다.

Q. 비즈니스 값에 중복을 막고 싶으면 어떻게 해?
A. Primary Key로 쓰기보다 Unique Constraint를 적용하는 것이 일반적이다.

---

## 1.3 ID Generation Strategy

### [개념]

ID Generation Strategy는 Entity Primary Key 값을 어떻게 생성할지 결정하는 전략이다.

JPA는 `@GeneratedValue`와 `GenerationType`으로 DB ID 생성 방식을 지정한다.

---

### [핵심]

주요 전략:

- `GenerationType.IDENTITY`
- `GenerationType.SEQUENCE`
- `GenerationType.AUTO`
- `GenerationType.TABLE`
- UUID
- DB Auto Increment
- DB Sequence

전략 비교:

| 전략     | 기준               | 사용 상황               |
| -------- | ------------------ | ----------------------- |
| IDENTITY | DB Auto Increment  | MySQL 계열              |
| SEQUENCE | DB Sequence        | PostgreSQL, Oracle 계열 |
| AUTO     | Provider 자동 선택 | 명시성 낮음             |
| TABLE    | 별도 키 테이블     | 거의 비권장             |
| UUID     | Application 생성   | 분산 환경 후보          |

---

### [실무]

IDENTITY 예시:

```java
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long postId;
```

SEQUENCE 예시:

```java
@Id
@GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "post_seq_generator")
@SequenceGenerator(
        name = "post_seq_generator",
        sequenceName = "post_seq",
        allocationSize = 50
)
private Long postId;
```

SQL Foundation 연결:

```text
SQL Auto Increment
→ GenerationType.IDENTITY

SQL Sequence
→ GenerationType.SEQUENCE

Application Generated ID
→ UUID
```

권장:

- MySQL 기반 프로젝트는 `IDENTITY` 사용 가능
- PostgreSQL / Oracle 기반은 `SEQUENCE` 검토
- `AUTO`는 DB별 동작 차이를 확인
- `TABLE` 전략은 성능상 비권장
- UUID는 분산 환경, 외부 노출 ID, 보안 요구사항을 고려해 선택

주의:

- `IDENTITY`는 INSERT 시점에 ID가 생성된다.
- `SEQUENCE`는 Sequence 호출로 ID를 선점할 수 있다.
- ID 생성 전략은 Batch Insert 성능에 영향을 줄 수 있다.
- DB 변경 가능성이 있으면 전략 의존성을 검토해야 한다.
- UUID는 Index 크기와 정렬 성능을 고려해야 한다.

---

### [FAQ]

Q. `GenerationType.IDENTITY`는 언제 써?
A. MySQL Auto Increment처럼 DB가 INSERT 시점에 ID를 생성하는 환경에서 많이 사용한다.

Q. `GenerationType.SEQUENCE`는 언제 써?
A. PostgreSQL, Oracle처럼 DB Sequence를 사용하는 환경에서 적합하다.

Q. `GenerationType.AUTO`를 써도 돼?
A. 가능하지만 DB와 Provider에 따라 동작이 달라질 수 있어 명시적 전략이 더 안전하다.

Q. UUID를 Primary Key로 써도 돼?
A. 가능하지만 Index 크기, 정렬 성능, 저장 공간, 외부 노출 요구사항을 함께 검토해야 한다.

---

# 2. Column Mapping

## 2.1 Column Mapping Purpose

### [개념]

Column Mapping은 Entity Field와 DB Column을 연결하는 규칙이다.

`@Column`은 Column 이름, Null 허용 여부, 길이, Unique 제약, DB 타입 정의를 표현한다.

---

### [핵심]

핵심 키워드:

- Column Mapping
- `@Column`
- `nullable`
- `length`
- `unique`
- `name`
- `columnDefinition`
- `precision`
- `scale`
- Data Integrity
- DB Constraint

주요 속성:

| 속성               | 역할                     |
| ------------------ | ------------------------ |
| `name`             | DB Column 이름 지정      |
| `nullable`         | NULL 허용 여부           |
| `length`           | 문자열 길이              |
| `unique`           | Unique Constraint 후보   |
| `columnDefinition` | DB Column 정의 직접 지정 |
| `precision`        | 숫자 전체 자릿수         |
| `scale`            | 소수 자릿수              |
| `insertable`       | INSERT 포함 여부         |
| `updatable`        | UPDATE 포함 여부         |

---

### [실무]

기본 예시:

```java
@Column(nullable = false, length = 100)
private String title;

@Column(nullable = false, columnDefinition = "TEXT")
private String content;

@Column(nullable = false, unique = true, length = 100)
private String email;
```

SQL Foundation 연결:

```text
SQL Column
→ Entity Field

SQL NOT NULL
→ @Column(nullable = false)

SQL VARCHAR(100)
→ @Column(length = 100)

SQL UNIQUE
→ @Column(unique = true) + DB Unique Constraint

SQL TEXT
→ columnDefinition = "TEXT"
```

권장:

- 필수 Field는 `nullable = false` 명시
- 문자열 Field는 `length` 명시
- 긴 본문은 `TEXT` 전략 검토
- 이름 불일치 시 `name` 명시
- 금액은 `BigDecimal`과 `precision`, `scale` 사용 검토
- DB Constraint와 Application Validation을 함께 설계

주의:

- `@Column`은 Entity Field와 DB Column Mapping 의도를 표현한다.
- 실제 DB Schema 생성 방식은 `ddl-auto`, Migration Tool, 운영 정책에 따라 달라진다.
- `columnDefinition`은 DB 종속성을 높인다.
- `unique = true`는 복합 Unique Constraint에는 적합하지 않다.
- Bean Validation과 DB Constraint는 역할이 다르다.

---

### [FAQ]

Q. `@Column`은 꼭 써야 해?
A. 필수는 아니지만 nullable, length, unique 같은 의도를 명확히 하기 위해 중요한 Field에는 사용하는 것이 좋다.

Q. `@Column(name = "...")`은 언제 써?
A. Entity Field 이름과 DB Column 이름이 다르거나 명시적 Mapping이 필요할 때 사용한다.

Q. `columnDefinition`은 많이 써도 돼?
A. 권장하지 않는다. DB 종속성이 커지므로 필요한 경우에만 제한적으로 사용한다.

Q. `unique = true`만 쓰면 중복 방지가 완벽해?
A. 아니다. 실제 DB Unique Constraint 생성 여부와 예외 처리까지 함께 검토해야 한다.

---

## 2.2 Nullable and Required Field

### [개념]

Nullable Mapping은 Entity Field가 DB에서 NULL을 허용하는지 결정하는 기준이다.

필수 값은 `nullable = false`와 Application Validation을 함께 검토한다.

---

### [핵심]

구분:

| 계층           | 검증 방식                            |
| -------------- | ------------------------------------ |
| Request DTO    | `@NotNull`, `@NotBlank`, `@NotEmpty` |
| Entity Mapping | `@Column(nullable = false)`          |
| Database       | `NOT NULL` Constraint                |
| Service        | 비즈니스 규칙 검증                   |

핵심 기준:

- API 입력 검증과 DB 무결성은 분리
- 필수 값은 DTO Validation과 DB Constraint 모두 고려
- 선택 값은 nullable 허용 가능
- null과 빈 문자열은 다름
- primitive type과 wrapper type 선택 주의

---

### [실무]

Request DTO 예시:

```java
public record PostCreateRequest(
        @NotBlank String title,
        @NotBlank String content
) {
}
```

Entity 예시:

```java
@Column(nullable = false, length = 100)
private String title;

@Column(nullable = false, columnDefinition = "TEXT")
private String content;

@Column(nullable = true, length = 500)
private String imageUrl;
```

SQL Foundation 연결:

```text
Request Validation
→ Application 입력 방어

@Column(nullable = false)
→ JPA Mapping 의도

DB NOT NULL Constraint
→ Data Integrity 최종 방어
```

권장:

- 필수 입력은 Request DTO에서 Validation
- 필수 저장 값은 Entity Column에서 `nullable = false`
- DB Migration에서 실제 NOT NULL Constraint 확인
- 선택 값은 nullable 정책을 명확히 문서화
- Boolean은 `Boolean` vs `boolean` 기준을 프로젝트에서 통일

주의:

- `@NotBlank`는 String 전용이다.
- `@NotNull`은 null만 막고 빈 문자열은 허용한다.
- `nullable = false`만으로 API 입력 검증이 되는 것은 아니다.
- DB Constraint 위반은 Runtime Exception으로 나타날 수 있다.
- 기본값이 필요한 Field는 Entity 생성 시점 또는 DB Default 정책을 통일해야 한다.

---

### [FAQ]

Q. `@NotNull`과 `nullable = false`는 같은 거야?
A. 아니다. `@NotNull`은 Application Validation이고 `nullable = false`는 DB Column 제약과 연결된다.

Q. 필수 값이면 DTO와 Entity 둘 다 검증해야 해?
A. 일반적으로 Request DTO에서 입력을 검증하고 DB Constraint로 Data Integrity를 최종 방어한다.

Q. `@NotBlank`와 `@NotNull`은 뭐가 달라?
A. `@NotNull`은 null만 막고 `@NotBlank`는 null, 빈 문자열, 공백 문자열을 막는다.

Q. 선택 값은 `nullable = true`를 꼭 써야 해?
A. 기본값이 true라 필수는 아니지만 선택 값임을 명확히 하려면 명시할 수 있다.

---

## 2.3 Length and Text Column

### [개념]

Length Mapping은 문자열 Field의 최대 길이를 DB Column과 맞추는 규칙이다.

짧은 문자열은 `VARCHAR`, 긴 본문은 `TEXT` 같은 DB 타입을 검토한다.

---

### [핵심]

문자열 기준:

| 데이터     | 권장 Mapping                 |
| ---------- | ---------------------------- |
| 제목       | `length = 100`               |
| 이메일     | `length = 100~255`           |
| 닉네임     | `length = 20~50`             |
| 이미지 URL | `length = 500~1000`          |
| 본문       | `TEXT`                       |
| 설명       | `TEXT` 또는 충분한 `VARCHAR` |

핵심 키워드:

- String
- VARCHAR
- TEXT
- `length`
- `columnDefinition`
- DB Index
- Data Truncation
- Validation

---

### [실무]

예시:

```java
@Column(nullable = false, length = 100)
private String title;

@Column(nullable = false, length = 50)
private String nickname;

@Column(length = 500)
private String imageUrl;

@Column(nullable = false, columnDefinition = "TEXT")
private String content;
```

SQL Foundation 연결:

```text
SQL VARCHAR Length
→ @Column(length = n)

SQL TEXT
→ @Column(columnDefinition = "TEXT")

Input Length Validation
→ @Size(max = n)
```

Request DTO Validation 예시:

```java
public record UserUpdateRequest(
        @Size(max = 50) String nickname
) {
}
```

권장:

- Column 길이와 DTO `@Size`를 맞춤
- URL은 일반 문자열보다 길게 설정
- 본문성 데이터는 `TEXT` 검토
- Index 대상 문자열은 길이와 DB Index 제한 확인
- 지나치게 큰 VARCHAR 남용 금지

주의:

- `length` 기본값에 의존하지 않는다.
- DB별 TEXT 타입 처리 방식이 다를 수 있다.
- 긴 문자열에 Unique Index를 걸면 DB 제한에 걸릴 수 있다.
- Validation 없이 DB 길이 제한만 있으면 저장 시점에 오류가 발생할 수 있다.
- `columnDefinition = "TEXT"`는 DB 종속성을 높일 수 있다.

---

### [FAQ]

Q. String Field에 length를 꼭 지정해야 해?
A. 필수는 아니지만 제목, 이메일, 닉네임처럼 길이 제한이 있는 값은 명시하는 것이 좋다.

Q. 긴 본문은 어떻게 Mapping해?
A. `columnDefinition = "TEXT"` 또는 프로젝트 DB에 맞는 긴 문자열 타입을 사용한다.

Q. DTO의 `@Size`와 Column length는 맞춰야 해?
A. 맞추는 것이 좋다. 입력 검증과 DB 저장 제한이 다르면 오류나 데이터 잘림이 발생할 수 있다.

Q. 이미지 URL 길이는 얼마나 잡아야 해?
A. 프로젝트 기준에 따라 다르지만 일반 문자열보다 길게 `500` 이상을 검토하는 경우가 많다.

---

# 3. Enum Mapping

## 3.1 EnumType.STRING Rule

### [개념]

Enum Mapping은 Java Enum 값을 DB Column에 저장하는 방식이다.

JPA에서는 `@Enumerated(EnumType.STRING)` 사용을 우선한다.

---

### [핵심]

핵심 키워드:

- Enum Mapping
- `@Enumerated`
- `EnumType.STRING`
- `EnumType.ORDINAL`
- Status Field
- Code Field
- Data Integrity
- State Transition

비교:

| 방식    | 저장 값        | 장점           | 단점                          |
| ------- | -------------- | -------------- | ----------------------------- |
| STRING  | Enum 이름      | 의미 명확      | 저장 공간 증가                |
| ORDINAL | Enum 순서 숫자 | 저장 공간 작음 | 순서 변경 시 데이터 의미 깨짐 |

---

### [실무]

권장 예시:

```java
@Enumerated(EnumType.STRING)
@Column(nullable = false, length = 20)
private PostStatus status;
```

Enum 예시:

```java
public enum PostStatus {
    DRAFT,
    PUBLISHED,
    DELETED
}
```

비권장 예시:

```java
@Enumerated(EnumType.ORDINAL)
private PostStatus status;
```

SQL Foundation 연결:

```text
Java Enum
→ DB VARCHAR Column
→ EnumType.STRING
→ Status Data Integrity
```

권장:

- `EnumType.STRING` 우선 사용
- Enum 이름 변경 시 DB 데이터 영향 검토
- 화면 표시명은 Enum 이름과 분리
- 상태 변경은 Entity Method로 통제
- 상태 값이 정해진 집합이면 String보다 Enum 검토

주의:

- `ORDINAL`은 Enum 순서 변경에 취약하다.
- Enum 이름 변경은 DB 저장 값 변경과 연결된다.
- 화면 표시용 한글명을 DB 저장 값으로 직접 쓰지 않는다.
- 외부 API Code와 내부 Enum 이름은 분리할 수 있다.

---

### [FAQ]

Q. Enum은 어떻게 저장하는 게 좋아?
A. `@Enumerated(EnumType.STRING)`을 우선 사용한다.

Q. `EnumType.ORDINAL`은 왜 위험해?
A. Enum 순서가 바뀌면 기존 DB 숫자 값의 의미가 깨질 수 있다.

Q. 상태값은 String으로 둬도 돼?
A. 가능하지만 정해진 값 집합이면 Enum을 사용해 오타와 잘못된 상태를 줄이는 것이 좋다.

Q. Enum 이름을 바꿔도 돼?
A. DB에 STRING으로 저장 중이면 기존 데이터와 호환성을 반드시 검토해야 한다.

---

## 3.2 Status Enum and State Transition

### [개념]

Status Enum은 Entity의 상태를 제한된 값 집합으로 관리하는 방식이다.

State Transition은 상태 변경 가능 경로를 Entity Method 또는 Service에서 통제하는 규칙이다.

---

### [핵심]

사용 예:

- UserStatus
- PostStatus
- OrderStatus
- PaymentStatus
- CertStatus
- NotificationType
- PostCategory

상태 관리 기준:

- Enum으로 오타 방지
- 상태 변경 Method 제공
- 불가능한 상태 전환 방지
- DB 저장 값 명확화
- Response 표시 값 분리

---

### [실무]

상태 변경 예시:

```java
@Entity
public class Post {

    @Enumerated(EnumType.STRING)
    @Column(nullable = false, length = 20)
    private PostStatus status;

    public void publish() {
        if (this.status != PostStatus.DRAFT) {
            throw new BusinessException("INVALID_STATUS", "작성 중인 게시글만 발행할 수 있습니다.");
        }
        this.status = PostStatus.PUBLISHED;
    }

    public void delete() {
        this.status = PostStatus.DELETED;
    }
}
```

Response 표시 분리 예시:

```java
public enum PostStatus {
    DRAFT("작성중"),
    PUBLISHED("발행됨"),
    DELETED("삭제됨");

    private final String displayName;

    PostStatus(String displayName) {
        this.displayName = displayName;
    }
}
```

권장:

- 상태 Field는 `nullable = false`
- 기본 상태를 생성 시점에 설정
- 상태 변경은 의미 있는 Method로 처리
- 상태 전환 규칙은 테스트 대상
- 외부 응답 값은 Response DTO에서 제어

주의:

- Controller에서 상태 Field를 직접 바꾸지 않는다.
- Request DTO에서 상태 값을 그대로 받아 무검증 반영하지 않는다.
- 상태 전환 규칙이 Service와 Entity에 흩어지지 않도록 기준을 정한다.
- Enum 표시명 변경과 DB 저장 값 변경을 혼동하지 않는다.

---

### [FAQ]

Q. 상태값은 Enum으로 두는 게 좋아?
A. 정해진 상태 집합이면 Enum을 사용하는 것이 오타와 잘못된 상태를 줄이는 데 좋다.

Q. 상태 변경은 Setter로 해도 돼?
A. 권장하지 않는다. `publish`, `cancel`, `delete`처럼 의미 있는 Method로 상태 전환을 통제하는 것이 좋다.

Q. Enum에 화면 표시명을 넣어도 돼?
A. 가능하지만 DB 저장 값과 화면 표시 값의 역할을 분리해서 관리해야 한다.

Q. 상태 기본값은 어디서 설정해?
A. Entity 생성 Method 또는 DB Default 정책 중 하나로 정하고 프로젝트 기준을 통일한다.

---

# 4. Constraint and Data Integrity

## 4.1 Constraint Purpose

### [개념]

Constraint는 DB 데이터 무결성을 보장하기 위한 제약 조건이다.

JPA Mapping은 Constraint 의도를 표현할 수 있지만, 실제 Data Integrity는 DB Constraint와 함께 확인해야 한다.

---

### [핵심]

핵심 키워드:

- Constraint
- Data Integrity
- NOT NULL
- UNIQUE
- Primary Key
- Foreign Key
- Check Constraint
- Validation Constraint
- DB Constraint
- Migration

Constraint 종류:

| Constraint  | 목적                      |
| ----------- | ------------------------- |
| Primary Key | Row 식별                  |
| Foreign Key | Table Relationship 무결성 |
| NOT NULL    | 필수 값 보장              |
| UNIQUE      | 중복 방지                 |
| CHECK       | 값 범위 제한              |
| DEFAULT     | 기본값 설정               |

---

### [실무]

SQL Foundation 연결:

```text
SQL Constraint
→ DB Data Integrity

JPA @Column
→ Mapping 의도

Bean Validation
→ API 입력 검증

Migration Tool
→ 운영 DB Constraint 관리
```

JPA 예시:

```java
@Column(nullable = false, unique = true, length = 100)
private String email;
```

DB 관점:

```sql
email varchar(100) not null unique
```

권장:

- 필수 값은 NOT NULL
- 중복 금지는 UNIQUE
- 관계 무결성은 Foreign Key
- 값 범위는 Application Validation과 DB CHECK 검토
- 운영 환경에서는 Migration Tool로 Constraint 관리
- Constraint 위반 예외 처리 기준을 마련

주의:

- JPA Annotation만으로 운영 DB Constraint가 항상 보장되는 것은 아니다.
- `ddl-auto=update`에 의존한 Constraint 관리는 위험하다.
- 복합 Unique Constraint는 `@Table(uniqueConstraints = ...)` 또는 Migration에서 관리한다.
- Foreign Key Constraint와 JPA Association Mapping은 역할이 다르다.
- Application Validation은 우회될 수 있으므로 DB Constraint가 최종 방어선이다.

---

### [FAQ]

Q. Constraint는 왜 필요해?
A. 잘못된 데이터 저장을 막고 DB Data Integrity를 보장하기 위해 필요하다.

Q. JPA Annotation만 있으면 DB Constraint가 보장돼?
A. 아니다. 운영 DB Schema와 Migration 결과를 함께 확인해야 한다.

Q. Validation과 Constraint는 같은 거야?
A. 아니다. Validation은 Application 입력 검증이고 Constraint는 DB 무결성 보장이다.

Q. `ddl-auto=update`로 Constraint를 관리해도 돼?
A. 운영 환경에서는 권장하지 않는다. Migration Tool로 명시적으로 관리하는 것이 안전하다.

---

## 4.2 Unique Constraint

### [개념]

Unique Constraint는 특정 Column 또는 Column 조합의 중복 값을 방지하는 DB 제약 조건이다.

JPA에서는 단일 Column Unique와 복합 Unique를 구분해서 설계한다.

---

### [핵심]

사용 상황:

- email 중복 방지
- username 중복 방지
- provider + providerId 중복 방지
- userId + postId 좋아요 중복 방지
- referenceType + referenceId + userId 알림 중복 방지

JPA 표현:

- `@Column(unique = true)`
- `@Table(uniqueConstraints = ...)`
- Migration Unique Index
- Repository `existsBy...`
- Service 중복 검증

---

### [실무]

단일 Unique 예시:

```java
@Column(nullable = false, unique = true, length = 100)
private String email;
```

복합 Unique 예시:

```java
@Entity
@Table(
    name = "favorites",
    uniqueConstraints = {
        @UniqueConstraint(
            name = "uk_favorite_user_festival",
            columnNames = {"user_id", "festival_id"}
        )
    }
)
public class Favorite {
}
```

Service 중복 검증 예시:

```java
if (userRepository.existsByEmail(request.email())) {
    throw new BusinessException("EMAIL_DUPLICATED", "이미 사용 중인 이메일입니다.");
}
```

SQL Foundation 연결:

```text
SQL UNIQUE Constraint
→ JPA unique Mapping
→ Repository existsBy
→ Service 중복 검증
→ DB Constraint 최종 방어
```

권장:

- 단일 Unique는 `@Column(unique = true)` 가능
- 복합 Unique는 `@Table(uniqueConstraints = ...)` 또는 Migration 사용
- Service에서 사전 중복 검증
- DB Unique Constraint로 Race Condition 최종 방어
- Unique Constraint 이름을 명확히 지정

주의:

- Service 중복 검증만으로 동시성 중복 저장을 완전히 막을 수 없다.
- DB Unique Constraint가 최종 방어선이다.
- Unique 위반 예외를 사용자 친화적 예외로 변환해야 한다.
- Soft Delete와 Unique Constraint 조합은 별도 전략이 필요하다.
- 대소문자 구분 여부는 DB Collation 영향을 받는다.

---

### [FAQ]

Q. 중복 체크는 `existsByEmail`만 하면 충분해?
A. 아니다. 동시 요청 Race Condition을 막으려면 DB Unique Constraint가 최종 방어선이어야 한다.

Q. 복합 Unique Constraint는 어떻게 설정해?
A. `@Table(uniqueConstraints = ...)` 또는 DB Migration에서 명시적으로 설정한다.

Q. Unique Constraint 위반은 어떻게 처리해?
A. DB 예외를 잡아 CustomException 또는 GlobalExceptionHandler에서 사용자 친화적 응답으로 변환한다.

Q. Soft Delete가 있으면 Unique Constraint는 어떻게 해?
A. 삭제된 Row까지 Unique에 걸릴 수 있으므로 Partial Index, 복합 조건, 별도 정책을 검토해야 한다.

---

## 4.3 Validation Constraint vs DB Constraint

### [개념]

Validation Constraint는 Application Layer에서 입력 값을 검증하는 규칙이다.

DB Constraint는 Database Layer에서 저장 데이터 무결성을 보장하는 규칙이다.

둘은 서로 대체 관계가 아니라 보완 관계다.

---

### [핵심]

비교:

| 구분          | Validation Constraint          | DB Constraint               |
| ------------- | ------------------------------ | --------------------------- |
| 위치          | Application                    | Database                    |
| 예시          | `@NotBlank`, `@Size`, `@Email` | NOT NULL, UNIQUE, FK, CHECK |
| 목적          | 입력 검증                      | 저장 무결성                 |
| 실패 시점     | Controller / Service 진입 전후 | INSERT / UPDATE 시점        |
| 우회 가능성   | 가능                           | 낮음                        |
| 사용자 메시지 | 만들기 쉬움                    | 예외 변환 필요              |

---

### [실무]

Request DTO 예시:

```java
public record SignUpRequest(
        @Email
        @NotBlank
        @Size(max = 100)
        String email,

        @NotBlank
        @Size(min = 8, max = 100)
        String password
) {
}
```

Entity 예시:

```java
@Column(nullable = false, unique = true, length = 100)
private String email;

@Column(nullable = false, length = 100)
private String password;
```

SQL Foundation 연결:

```text
Client Input
→ Request DTO Validation
→ Service Business Validation
→ Entity Mapping
→ DB Constraint
→ Data Integrity
```

권장:

- 입력 형식은 Request DTO Validation
- 비즈니스 규칙은 Service 또는 Domain Method
- 저장 무결성은 DB Constraint
- Entity Mapping은 DB 구조와 일치
- Constraint 위반 예외는 GlobalExceptionHandler에서 처리

주의:

- Request DTO Validation만으로 DB 무결성을 보장할 수 없다.
- DB Constraint만으로 사용자 친화적 오류 메시지를 만들기 어렵다.
- Entity에 Validation을 직접 붙일 수도 있지만 API별 입력 조건이 다르면 DTO Validation이 더 명확하다.
- Validation과 DB Constraint가 서로 다른 기준이면 운영 오류가 발생한다.

---

### [FAQ]

Q. Validation과 DB Constraint 중 하나만 쓰면 안 돼?
A. 권장하지 않는다. Validation은 입력 검증, DB Constraint는 저장 무결성 보장으로 역할이 다르다.

Q. `@Email`을 Entity에 붙여야 해?
A. API 입력 검증은 Request DTO에 두는 것이 일반적이다. Entity에는 DB 저장 기준을 명확히 한다.

Q. DB Constraint 위반 메시지는 어떻게 처리해?
A. Persistence Exception을 GlobalExceptionHandler에서 Custom Error Response로 변환한다.

Q. Validation 기준과 Column length가 다르면 어떻게 돼?
A. 입력은 통과했지만 저장 시 실패하거나 데이터가 잘릴 수 있으므로 기준을 맞추는 것이 좋다.

---

# 5. Foreign Key Column Basics

## 5.1 Foreign Key as Column

### [개념]

Foreign Key는 다른 Table의 Primary Key를 참조하는 Column이다.

JPA Association Mapping은 Foreign Key를 객체 참조로 표현한다.

Part02에서는 Foreign Key Column의 기본 개념만 다루고, Association Mapping은 Part03에서 상세히 다룬다.

---

### [핵심]

핵심 키워드:

- Foreign Key
- Table Relationship
- `@JoinColumn`
- Association Mapping
- ManyToOne
- OneToMany
- Owning Side
- Data Integrity
- Referential Integrity

SQL 기준:

```text
users.user_id
← posts.user_id

Parent Table Primary Key
← Child Table Foreign Key
```

JPA 기준:

```text
Post Entity
→ User user
→ @ManyToOne
→ @JoinColumn(name = "user_id")
```

---

### [실무]

JPA 예시:

```java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "user_id", nullable = false)
private User user;
```

SQL Foundation 연결:

```text
SQL Table Relationship
→ Primary Key / Foreign Key
→ JPA Association Mapping
→ JoinColumn
→ Owning Side
```

권장:

- Foreign Key를 가진 Entity가 연관관계 주인
- `@JoinColumn` 이름은 DB Column과 맞춤
- 필수 관계는 `nullable = false`
- Association Fetch 전략은 Part03 / Part06 기준 적용
- FK Constraint 존재 여부를 DB Schema에서 확인

주의:

- Foreign Key Column과 객체 참조는 같은 개념이 아니다.
- JPA Association을 설정해도 DB FK Constraint가 실제로 있는지 확인해야 한다.
- `@JoinColumn(nullable = false)`는 관계 필수 의도를 표현한다.
- FK가 없는 논리적 관계도 가능하지만 Data Integrity 방어가 약해진다.
- Association Mapping 상세는 Part03에서 다룬다.

---

### [FAQ]

Q. Foreign Key는 뭐야?
A. 다른 Table의 Primary Key를 참조해 Table Relationship을 만드는 Column이다.

Q. JPA에서 Foreign Key는 어떻게 표현해?
A. 보통 `@ManyToOne`과 `@JoinColumn`으로 객체 참조와 FK Column을 연결한다.

Q. Foreign Key를 가진 쪽이 연관관계 주인이야?
A. 일반적으로 그렇다. DB Foreign Key를 가진 Entity가 JPA 연관관계 주인이 된다.

Q. Foreign Key 상세 Mapping은 어디서 다뤄?
A. Part03 Association Mapping and Table Relationship에서 상세히 다룬다.

---

# 6. Column Type Strategy

## 6.1 Date and Time Mapping

### [개념]

Date and Time Mapping은 Java 날짜 / 시간 타입을 DB Column에 저장하는 규칙이다.

Modern Spring Boot + JPA 기준에서는 `LocalDate`, `LocalDateTime` 사용을 우선한다.

---

### [핵심]

주요 타입:

| Java Type       | DB 의미              | 사용 상황          |
| --------------- | -------------------- | ------------------ |
| `LocalDate`     | DATE                 | 날짜만 필요        |
| `LocalTime`     | TIME                 | 시간만 필요        |
| `LocalDateTime` | DATETIME / TIMESTAMP | 날짜와 시간        |
| `Instant`       | TIMESTAMP            | UTC 기준 시점      |
| `ZonedDateTime` | Time Zone 포함       | Time Zone 요구사항 |

핵심 키워드:

- LocalDate
- LocalDateTime
- CreatedDate
- LastModifiedDate
- Auditing
- Time Zone
- UTC
- KST

---

### [실무]

예시:

```java
@Column(nullable = false)
private LocalDate eventStartDate;

@Column(nullable = false)
private LocalDateTime createdAt;
```

Auditing은 Part07에서 상세히 다룬다.

```java
@CreatedDate
private LocalDateTime createdAt;

@LastModifiedDate
private LocalDateTime updatedAt;
```

권장:

- 날짜만 필요하면 `LocalDate`
- 날짜와 시간이 필요하면 `LocalDateTime`
- 생성일 / 수정일은 Auditing 공통화 검토
- 글로벌 서비스는 UTC 저장 정책 검토
- 한국 서비스라도 Time Zone 정책을 명확히 문서화

주의:

- Legacy `Date`, `Calendar` 사용 지양
- Time Zone 요구사항이 있으면 `LocalDateTime`만으로 부족할 수 있다.
- DB Column Type과 Java Type Mapping 확인
- 날짜 검색은 시작 / 종료 범위 Query로 처리하는 것이 일반적이다.
- Auditing 상세 기준은 Part07에서 다룬다.

---

### [FAQ]

Q. 날짜 Field는 어떤 타입을 쓰는 게 좋아?
A. 날짜만 필요하면 `LocalDate`, 날짜와 시간이 필요하면 `LocalDateTime`을 많이 사용한다.

Q. `Date`나 `Calendar`를 써도 돼?
A. Modern JPA 기준에서는 `java.time` 패키지의 `LocalDate`, `LocalDateTime` 사용을 권장한다.

Q. 생성일과 수정일은 직접 넣어야 해?
A. 공통 Base Entity와 Auditing으로 관리할 수 있다. 상세 기준은 Part07에서 다룬다.

Q. Time Zone은 꼭 고려해야 해?
A. 글로벌 서비스나 외부 API 연동이 있으면 UTC 저장 정책과 표시 Time Zone을 검토해야 한다.

---

## 6.2 Numeric and Money Mapping

### [개념]

Numeric Mapping은 숫자 값을 Entity Field와 DB Column에 저장하는 규칙이다.

금액, 비율, 정밀 계산 값은 `BigDecimal` 사용을 우선 검토한다.

---

### [핵심]

타입 기준:

| 데이터   | Java Type                | DB Type 후보     |
| -------- | ------------------------ | ---------------- |
| ID       | `Long`                   | BIGINT           |
| Count    | `Long` / `Integer`       | BIGINT / INT     |
| Quantity | `Integer`                | INT              |
| Money    | `BigDecimal`             | DECIMAL          |
| Rate     | `BigDecimal` / `Double`  | DECIMAL / DOUBLE |
| Score    | `Integer` / `BigDecimal` | INT / DECIMAL    |

핵심 키워드:

- BigDecimal
- Integer
- Long
- precision
- scale
- DECIMAL
- Count Field
- Money Field

---

### [실무]

금액 예시:

```java
@Column(nullable = false, precision = 12, scale = 2)
private BigDecimal price;
```

카운트 예시:

```java
@Column(nullable = false)
private Long viewCount;
```

권장:

- 금액은 `BigDecimal`
- ID와 누적 Count는 `Long`
- 작은 수량은 `Integer`
- 정밀도가 중요한 값에 `double` / `float` 사용 지양
- `precision`과 `scale`을 DB 요구사항에 맞춤
- 기본값 정책을 명확히 설정

주의:

- `BigDecimal` 비교는 `equals`보다 `compareTo` 기준 검토
- primitive type은 null 표현이 불가능하다.
- wrapper type은 null 가능성을 검토해야 한다.
- Count Field는 동시성 증가 문제를 고려해야 한다.
- 금액 계산은 반올림 정책을 명확히 해야 한다.

---

### [FAQ]

Q. 금액은 `int`나 `double`로 저장해도 돼?
A. 권장하지 않는다. 금액은 정밀도가 중요하므로 `BigDecimal`을 사용하는 것이 좋다.

Q. Count Field는 `Integer`와 `Long` 중 뭐가 좋아?
A. 데이터 규모가 커질 수 있으면 `Long`을 사용하는 것이 안전하다.

Q. `precision`과 `scale`은 뭐야?
A. `precision`은 전체 자릿수이고 `scale`은 소수 자릿수다.

Q. 숫자 Field는 primitive와 wrapper 중 뭐가 좋아?
A. null 허용 여부에 따라 선택한다. 필수 값이면 primitive 또는 기본값 정책을 검토하고, 선택 값이면 wrapper를 사용할 수 있다.

---

## 6.3 Boolean Mapping

### [개념]

Boolean Mapping은 true / false 상태를 DB Column에 저장하는 규칙이다.

삭제 여부, 활성 여부, 읽음 여부 같은 Flag Field에 자주 사용한다.

---

### [핵심]

사용 예:

- `deleted`
- `active`
- `readStatus`
- `enabled`
- `verified`
- `publicVisible`

Mapping 기준:

```java
@Column(nullable = false)
private Boolean active;
```

또는:

```java
@Column(nullable = false)
private boolean active;
```

---

### [실무]

Soft Delete 예시:

```java
@Column(nullable = false)
private boolean deleted = false;

public void delete() {
    this.deleted = true;
}
```

Active Flag 예시:

```java
@Column(nullable = false)
private boolean active = true;

public void deactivate() {
    this.active = false;
}
```

권장:

- 필수 Flag는 `nullable = false`
- 기본값을 Entity 생성 시점에 명확히 설정
- Field 이름은 의미가 명확해야 함
- `isDeleted`, `deleted` naming을 프로젝트 기준으로 통일
- 상태 변경 Method 사용

주의:

- `Boolean`은 null 가능성이 있다.
- `boolean`은 기본값이 false다.
- DB Default와 Entity 기본값이 다르면 혼선이 생긴다.
- Soft Delete는 Query 조건 누락 위험이 있다.
- Boolean이 많아지면 Enum 상태값이 더 적합한지 검토한다.

---

### [FAQ]

Q. Boolean Field는 `boolean`과 `Boolean` 중 뭐가 좋아?
A. null이 필요 없으면 `boolean`, null 상태가 의미 있으면 `Boolean`을 사용할 수 있다.

Q. 삭제 여부는 Boolean으로 둬도 돼?
A. 가능하다. 다만 Soft Delete Query 조건 누락과 Unique Constraint 조합을 주의해야 한다.

Q. Boolean 기본값은 어디서 설정해?
A. Entity Field 초기값, 생성 Method, DB Default 중 하나로 정하고 프로젝트 기준을 통일한다.

Q. Boolean 대신 Enum을 써야 하는 경우는 언제야?
A. 상태가 true / false 두 가지를 넘어 여러 단계로 확장될 가능성이 있으면 Enum을 검토한다.

---

# 7. Entity Default Value Strategy

## 7.1 Default Value Rule

### [개념]

Default Value Strategy는 Entity Field의 기본값을 어디에서 설정할지 정하는 규칙이다.

기본값은 Entity 생성 시점, DB Default, Service 로직 중 하나로 관리할 수 있다.

---

### [핵심]

기본값 후보:

- Entity Field 초기값
- Static Factory Method
- Constructor
- Service Layer
- DB Default
- Auditing
- Enum Default

비교:

| 위치           | 장점                   | 주의                         |
| -------------- | ---------------------- | ---------------------------- |
| Entity Field   | 코드에서 명확          | DB 직접 Insert와 불일치 가능 |
| Factory Method | 생성 의도 명확         | 모든 생성 경로 통제 필요     |
| Service        | 요청별 제어 가능       | 로직 분산 가능               |
| DB Default     | DB 직접 Insert 방어    | Entity 상태와 불일치 가능    |
| Auditing       | 생성일 / 수정일 자동화 | 설정 필요                    |

---

### [실무]

Entity Field 기본값 예시:

```java
@Column(nullable = false)
private boolean active = true;

@Enumerated(EnumType.STRING)
@Column(nullable = false, length = 20)
private PostStatus status = PostStatus.DRAFT;
```

Factory Method 기본값 예시:

```java
public static Post create(String title, String content) {
    Post post = new Post();
    post.title = title;
    post.content = content;
    post.status = PostStatus.DRAFT;
    post.deleted = false;
    return post;
}
```

권장:

- Entity 생성 규칙이 중요하면 Factory Method에서 설정
- 단순 Flag는 Field 초기값 가능
- 생성일 / 수정일은 Auditing 검토
- DB Default와 Entity Default 불일치 방지
- 테스트에서 기본값 검증

주의:

- JPA Entity 생성 경로가 여러 개면 기본값 누락 가능
- DB Default는 JPA Insert SQL에 null이 들어가면 기대와 다를 수 있다.
- primitive 기본값 false / 0에 의존하지 않는다.
- 상태 기본값은 비즈니스 의미를 명확히 해야 한다.
- 기본값 정책은 Part07 Auditing과 연결된다.

---

### [FAQ]

Q. 기본값은 Entity에서 설정하는 게 좋아?
A. Entity 생성 규칙과 밀접한 값은 Entity Field 초기값이나 Factory Method에서 설정하는 것이 명확하다.

Q. DB Default만 쓰면 안 돼?
A. 가능하지만 JPA Entity 상태와 DB 저장 값이 불일치할 수 있어 주의해야 한다.

Q. Enum 기본 상태는 어디서 설정해?
A. Entity Field 초기값 또는 Factory Method에서 명확히 설정하는 것이 좋다.

Q. createdAt 기본값은 직접 설정해?
A. 보통 Auditing으로 관리한다. 상세 기준은 Part07에서 다룬다.

---

# 8. Column and Constraint Review

## 8.1 Column Mapping Checklist

### [개념]

Column Mapping Checklist는 Entity Field와 DB Column이 일관되게 Mapping되었는지 검수하는 기준이다.

Review Agent는 Column Mapping, Constraint, Validation, Naming, 기본값 정책을 함께 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] 모든 Entity에 @Id가 있는가?
- [ ] Primary Key 타입이 적절한가?
- [ ] Primary Key 생성 전략이 DB와 맞는가?
- [ ] Surrogate Key와 Natural Key가 구분되는가?
- [ ] 비즈니스 값이 Primary Key로 사용되지 않는가?
- [ ] 필수 Field에 nullable = false가 있는가?
- [ ] 문자열 Field에 length가 명확한가?
- [ ] 긴 문자열에 TEXT 전략을 검토했는가?
- [ ] Unique가 필요한 Field에 Unique Constraint가 있는가?
- [ ] 복합 Unique Constraint가 필요한가?
- [ ] Request DTO Validation과 Column 제약이 일치하는가?
- [ ] Enum Field가 EnumType.STRING을 사용하는가?
- [ ] EnumType.ORDINAL을 사용하지 않는가?
- [ ] 상태값 변경 Method가 있는가?
- [ ] Foreign Key Column 이름이 명확한가?
- [ ] JoinColumn nullable 기준이 관계 필수성과 맞는가?
- [ ] Date / Time 타입이 적절한가?
- [ ] 금액 Field에 BigDecimal을 사용하는가?
- [ ] Boolean Field 기본값이 명확한가?
- [ ] DB Default와 Entity Default가 충돌하지 않는가?
- [ ] Constraint 위반 예외 처리 기준이 있는가?
```

---

### [실무]

Review Flow:

```text
Entity Field 확인
→ Primary Key 확인
→ Column nullable / length 확인
→ Unique Constraint 확인
→ Validation 기준 확인
→ Enum Mapping 확인
→ Numeric / Date Type 확인
→ Default Value 확인
→ DB Schema / Migration 확인
→ Exception Handling 확인
```

Common Review Findings:

```text
문제: email Field에 unique = true 없음
위험: 중복 회원 가입 가능
해결: DB Unique Constraint + existsByEmail 검증

문제: EnumType.ORDINAL 사용
위험: Enum 순서 변경 시 기존 데이터 의미 깨짐
해결: EnumType.STRING 사용

문제: title에 length 미지정
위험: 기본 길이에 의존, Validation 불일치
해결: @Column(length = 100) + @Size(max = 100)

문제: 금액 Field를 double로 사용
위험: 정밀도 손실
해결: BigDecimal + precision / scale 사용

문제: DB Constraint 없이 Service 검증만 존재
위험: 동시성 상황에서 중복 데이터 저장 가능
해결: DB Constraint 추가
```

---

### [FAQ]

Q. Column Mapping 검수에서 가장 먼저 확인할 것은 뭐야?
A. `@Id`, ID 생성 전략, `nullable`, `length`, `unique`, Enum Mapping, Validation 일치 여부를 먼저 확인한다.

Q. Constraint 검수에서 중요한 것은 뭐야?
A. Application Validation과 DB Constraint가 역할에 맞게 함께 존재하는지 확인하는 것이다.

Q. Enum Mapping 검수에서 가장 위험한 것은 뭐야?
A. `EnumType.ORDINAL` 사용이다. Enum 순서 변경 시 기존 데이터 의미가 깨질 수 있다.

Q. Unique 검수에서 Service 중복 검증만 있으면 충분해?
A. 아니다. DB Unique Constraint가 최종 방어선으로 필요하다.

---

# 9. Common Mistakes

## 9.1 Primary Key and Column Common Mistakes

### [개념]

Primary Key and Column Common Mistakes는 Entity 식별자, Column Mapping, Constraint, Data Integrity 설계에서 자주 발생하는 오류다.

---

### [핵심]

자주 발생하는 실수:

- `@Id` 누락
- ID 생성 전략 누락
- DB와 맞지 않는 GenerationType 사용
- 이메일을 Primary Key로 사용
- 비즈니스 값을 Primary Key로 사용
- `nullable = false` 누락
- 문자열 `length` 누락
- DTO `@Size`와 Column length 불일치
- `unique = true`만 믿고 DB 확인 안 함
- 복합 Unique Constraint 누락
- EnumType.ORDINAL 사용
- Boolean 기본값 불명확
- DB Default와 Entity Default 불일치
- 금액을 `double`로 저장
- Foreign Key Constraint 없이 논리 관계만 사용
- Validation만 있고 DB Constraint 없음
- Constraint 위반 예외 처리 없음
- 운영 환경에서 `ddl-auto=update`에 의존
- Column 이름 불일치
- Native Query에서 잘못된 Column 이름 사용

---

### [실무]

Anti Pattern 예시:

```java
@Entity
public class User {

    @Id
    private String email;

    private String nickname;

    @Enumerated(EnumType.ORDINAL)
    private UserStatus status;

    private double point;
}
```

문제:

- 이메일을 Primary Key로 사용
- ID 생성 전략 없음
- nickname length / nullable 불명확
- EnumType.ORDINAL 사용
- point를 double로 사용
- Constraint 기준 불명확

개선 예시:

```java
@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long userId;

    @Column(nullable = false, unique = true, length = 100)
    private String email;

    @Column(nullable = false, length = 50)
    private String nickname;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false, length = 20)
    private UserStatus status;

    @Column(nullable = false, precision = 12, scale = 2)
    private BigDecimal point;
}
```

Review 기준:

```text
Primary Key
→ Surrogate Key 여부 확인

Column
→ nullable / length 확인

Constraint
→ unique / not null / fk 확인

Enum
→ EnumType.STRING 확인

Numeric
→ BigDecimal 필요 여부 확인

Validation
→ DTO Validation과 DB Constraint 일치 확인
```

---

### [FAQ]

Q. Primary Key 설계에서 가장 흔한 실수는 뭐야?
A. 이메일이나 닉네임 같은 변경 가능한 비즈니스 값을 Primary Key로 사용하는 것이다.

Q. Column Mapping에서 가장 흔한 실수는 뭐야?
A. nullable, length, unique 기준을 명확히 하지 않는 것이다.

Q. Constraint에서 가장 흔한 실수는 뭐야?
A. Service 중복 검증만 믿고 DB Unique Constraint를 두지 않는 것이다.

Q. Enum Mapping에서 가장 흔한 실수는 뭐야?
A. `EnumType.ORDINAL`을 사용하는 것이다.

---

# 10. Part02 Final Goal

## 10.1 Agent Output Goal

### [개념]

JPA Advanced Part02의 최종 목적은 Agent가 Entity Field와 DB Column, Primary Key, Constraint, Data Integrity를 안정적으로 설계하도록 만드는 것이다.

Part02는 SQL Foundation의 Primary Key, Constraint, Transaction, Data Integrity 기준과 JPA Entity Mapping을 연결한다.

---

### [핵심]

Agent가 수행해야 할 작업:

- Primary Key Mapping 설계
- Surrogate Key / Natural Key 구분
- ID Generation Strategy 선택
- Column Mapping 설계
- Nullable 기준 설정
- 문자열 length 기준 설정
- EnumType.STRING 적용
- Status Enum 설계
- Unique Constraint 설계
- Validation Constraint와 DB Constraint 분리
- Foreign Key Column 기본 이해
- Date / Time Mapping 선택
- Numeric / Money Mapping 선택
- Boolean 기본값 설정
- Entity Default Value 정책 확인
- Column Mapping Checklist 적용
- Data Integrity Anti Pattern 탐지

---

### [실무]

Agent 작업 흐름:

```text
User Persistence Request
→ Identify Entity Field
→ Decide Primary Key
→ Choose ID Generation Strategy
→ Map Column
→ Apply nullable / length
→ Apply EnumType.STRING
→ Define Constraint
→ Match DTO Validation
→ Check Data Integrity
→ Review DB Schema Impact
```

Part02 이후 연결:

```text
Part02 Primary Key / Column / Constraint
→ Part03 Association Mapping / Table Relationship / Foreign Key
→ Part04 Persistence Context / Dirty Checking
→ Part05 Repository / JPQL / Native Query
→ Part06 Fetch Join / N+1
→ Part07 Transaction / Cascade / Pagination
→ Part08 Troubleshooting / Anti Pattern
```

---

### [FAQ]

Q. JPA Advanced Part02의 목적은 뭐야?
A. Agent가 Primary Key, Column Mapping, Constraint, Data Integrity 기준을 일관되게 설계하도록 만드는 것이다.

Q. Part02에서 연관관계를 깊게 다뤄?
A. 아니다. Foreign Key Column의 기본만 다루고 Association Mapping은 Part03에서 상세히 다룬다.

Q. Part02에서 가장 중요한 Review 기준은 뭐야?
A. Primary Key 안정성, nullable / length 명확성, EnumType.STRING, Unique Constraint, Validation과 DB Constraint 일치 여부다.

Q. Part02는 SQL Foundation 어느 부분과 연결돼?
A. SQL Part04의 Constraint, Transaction, Data Integrity와 연결되고, SQL Part01의 Table Relationship과도 연결된다.

---

# Retrieval Queries

### [FAQ]

Q. JPA Primary Key는 뭐야?
A. JPA Entity의 식별자 Field이며 DB Primary Key와 Mapping되고 Persistence Context 관리 기준이 된다.

Q. JPA Entity에는 `@Id`가 꼭 필요해?
A. 필요하다. JPA는 `@Id` 식별자를 기준으로 Entity를 관리한다.

Q. Entity ID는 어떤 타입이 좋아?
A. 대부분 `Long` 타입의 Surrogate Key를 사용한다.

Q. Surrogate Key는 뭐야?
A. 비즈니스 의미가 없는 인공 식별자이며 보통 `Long userId` 같은 형태로 사용한다.

Q. Natural Key는 뭐야?
A. 이메일, 전화번호, 상품코드처럼 비즈니스 의미를 가진 식별자다.

Q. 이메일을 Primary Key로 써도 돼?
A. 권장하지 않는다. 이메일은 변경될 수 있으므로 Unique Column으로 두는 것이 좋다.

Q. 비즈니스 값은 Primary Key로 쓰면 안 돼?
A. 변경 가능성이 있는 비즈니스 값은 Primary Key로 부적합하다. Unique Column으로 관리하는 것이 일반적이다.

Q. `@GeneratedValue`는 뭐야?
A. Primary Key 값을 자동 생성하기 위한 JPA Annotation이다.

Q. `GenerationType.IDENTITY`는 언제 써?
A. MySQL Auto Increment처럼 DB가 INSERT 시점에 ID를 생성하는 환경에서 많이 사용한다.

Q. `GenerationType.SEQUENCE`는 언제 써?
A. PostgreSQL, Oracle처럼 DB Sequence를 사용하는 환경에서 적합하다.

Q. `GenerationType.AUTO`를 써도 돼?
A. 가능하지만 DB와 Provider에 따라 동작이 달라질 수 있어 명시적 전략이 더 안전하다.

Q. UUID를 Primary Key로 써도 돼?
A. 가능하지만 Index 크기, 정렬 성능, 저장 공간, 외부 노출 요구사항을 함께 검토해야 한다.

Q. Column Mapping은 뭐야?
A. Entity Field와 DB Column을 연결하고 nullable, length, unique 같은 속성을 지정하는 Mapping이다.

Q. `@Column`은 꼭 써야 해?
A. 필수는 아니지만 nullable, length, unique 같은 의도를 명확히 하기 위해 중요한 Field에는 사용하는 것이 좋다.

Q. `@Column(nullable = false)`는 왜 써?
A. 필수 Column 의도를 명확히 하고 DB NOT NULL Constraint와 연결하기 위해 사용한다.

Q. `@NotNull`과 `nullable = false`는 같은 거야?
A. 아니다. `@NotNull`은 Application Validation이고 `nullable = false`는 DB Column 제약과 연결된다.

Q. `@NotBlank`와 `@NotNull`은 뭐가 달라?
A. `@NotNull`은 null만 막고 `@NotBlank`는 null, 빈 문자열, 공백 문자열을 막는다.

Q. String Field에 length를 꼭 지정해야 해?
A. 필수는 아니지만 제목, 이메일, 닉네임처럼 길이 제한이 있는 값은 명시하는 것이 좋다.

Q. 긴 본문은 JPA에서 어떻게 Mapping해?
A. `columnDefinition = "TEXT"` 또는 프로젝트 DB에 맞는 긴 문자열 타입을 사용한다.

Q. DTO의 `@Size`와 Column length는 맞춰야 해?
A. 맞추는 것이 좋다. 입력 검증과 DB 저장 제한이 다르면 오류나 데이터 잘림이 발생할 수 있다.

Q. `columnDefinition`은 언제 써?
A. TEXT, DECIMAL, DB 특화 타입처럼 기본 Mapping만으로 의도가 부족할 때 제한적으로 사용한다.

Q. Enum은 어떻게 저장하는 게 좋아?
A. `@Enumerated(EnumType.STRING)`을 우선 사용한다.

Q. `EnumType.ORDINAL`은 왜 위험해?
A. Enum 순서가 바뀌면 기존 DB 숫자 값의 의미가 깨질 수 있다.

Q. 상태값은 String으로 둬도 돼?
A. 가능하지만 정해진 값 집합이면 Enum을 사용해 오타와 잘못된 상태를 줄이는 것이 좋다.

Q. 상태 변경은 Setter로 해도 돼?
A. 권장하지 않는다. `publish`, `cancel`, `delete`처럼 의미 있는 Method로 상태 전환을 통제하는 것이 좋다.

Q. Constraint는 뭐야?
A. DB 데이터 무결성을 보장하기 위한 Primary Key, Foreign Key, NOT NULL, UNIQUE, CHECK 같은 제약 조건이다.

Q. Data Integrity는 뭐야?
A. DB에 저장되는 데이터가 정확하고 일관된 상태를 유지하는 것을 의미한다.

Q. JPA Annotation만 있으면 DB Constraint가 보장돼?
A. 아니다. 운영 DB Schema와 Migration 결과를 함께 확인해야 한다.

Q. Validation과 DB Constraint는 같은 거야?
A. 아니다. Validation은 Application 입력 검증이고 DB Constraint는 저장 무결성 보장이다.

Q. 중복 체크는 `existsByEmail`만 하면 충분해?
A. 아니다. 동시 요청 Race Condition을 막으려면 DB Unique Constraint가 최종 방어선이어야 한다.

Q. Unique Constraint는 언제 써?
A. 이메일, 닉네임, userId + postId 같은 값이 중복되면 안 될 때 사용한다.

Q. 복합 Unique Constraint는 어떻게 설정해?
A. `@Table(uniqueConstraints = ...)` 또는 DB Migration에서 명시적으로 설정한다.

Q. Unique Constraint 위반은 어떻게 처리해?
A. DB 예외를 잡아 CustomException 또는 GlobalExceptionHandler에서 사용자 친화적 응답으로 변환한다.

Q. Foreign Key는 뭐야?
A. 다른 Table의 Primary Key를 참조해 Table Relationship을 만드는 Column이다.

Q. JPA에서 Foreign Key는 어떻게 표현해?
A. 보통 `@ManyToOne`과 `@JoinColumn`으로 객체 참조와 FK Column을 연결한다.

Q. Foreign Key를 가진 쪽이 연관관계 주인이야?
A. 일반적으로 그렇다. DB Foreign Key를 가진 Entity가 JPA 연관관계 주인이 된다.

Q. 날짜 Field는 어떤 타입을 쓰는 게 좋아?
A. 날짜만 필요하면 `LocalDate`, 날짜와 시간이 필요하면 `LocalDateTime`을 많이 사용한다.

Q. `Date`나 `Calendar`를 써도 돼?
A. Modern JPA 기준에서는 `java.time` 패키지의 `LocalDate`, `LocalDateTime` 사용을 권장한다.

Q. 금액은 `double`로 저장해도 돼?
A. 권장하지 않는다. 금액은 정밀도가 중요하므로 `BigDecimal`을 사용하는 것이 좋다.

Q. Count Field는 `Integer`와 `Long` 중 뭐가 좋아?
A. 데이터 규모가 커질 수 있으면 `Long`을 사용하는 것이 안전하다.

Q. Boolean Field는 `boolean`과 `Boolean` 중 뭐가 좋아?
A. null이 필요 없으면 `boolean`, null 상태가 의미 있으면 `Boolean`을 사용할 수 있다.

Q. Boolean 기본값은 어디서 설정해?
A. Entity Field 초기값, 생성 Method, DB Default 중 하나로 정하고 프로젝트 기준을 통일한다.

Q. 기본값은 Entity에서 설정하는 게 좋아?
A. Entity 생성 규칙과 밀접한 값은 Entity Field 초기값이나 Factory Method에서 설정하는 것이 명확하다.

Q. DB Default만 쓰면 안 돼?
A. 가능하지만 JPA Entity 상태와 DB 저장 값이 불일치할 수 있어 주의해야 한다.

Q. Column Mapping 검수에서 가장 먼저 확인할 것은 뭐야?
A. `@Id`, ID 생성 전략, `nullable`, `length`, `unique`, Enum Mapping, Validation 일치 여부를 먼저 확인한다.

Q. Constraint 검수에서 중요한 것은 뭐야?
A. Application Validation과 DB Constraint가 역할에 맞게 함께 존재하는지 확인하는 것이다.

Q. JPA Part02에서 가장 중요한 기준은 뭐야?
A. Primary Key 안정성, Column Mapping 명확성, EnumType.STRING, Unique Constraint, Validation과 DB Constraint 일치 여부다.

Q. JPA Part02 다음에는 무엇을 다뤄?
A. Part03에서 Association Mapping, Table Relationship, Foreign Key, Owning Side, mappedBy, JoinColumn을 다룬다.
