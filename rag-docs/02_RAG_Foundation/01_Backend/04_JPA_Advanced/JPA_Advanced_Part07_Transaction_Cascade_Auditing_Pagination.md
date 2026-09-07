# JPA Advanced Part07 — Transaction, Cascade, Auditing, Pagination

---

# 1. Transaction Boundary

## 1.1 Transaction Boundary Concept

### [개념]

Transaction Boundary는 DB 작업이 하나의 논리적 작업 단위로 처리되는 범위다.

JPA에서는 Transaction Boundary가 Persistence Context, Dirty Checking, Lazy Loading, Flush, Rollback 동작 범위를 결정한다.

---

### [핵심]

핵심 키워드:

- Transaction
- Transaction Boundary
- `@Transactional`
- Service Layer
- Persistence Context
- Dirty Checking
- Flush
- Commit
- Rollback
- readOnly
- Lazy Loading
- Data Integrity

Transaction Boundary 역할:

- Persistence Context 생명주기 관리
- Managed Entity 변경 감지 범위 제공
- Dirty Checking 동작 범위 제공
- Flush / Commit / Rollback 기준 제공
- Lazy Loading 가능 범위 제공
- 여러 Repository 작업을 하나의 작업 단위로 묶음

---

### [실무]

기본 흐름:

```text
Controller Request
→ Service @Transactional
→ Repository 조회
→ Entity Managed 상태
→ Entity 변경
→ Dirty Checking
→ Flush
→ Commit / Rollback
→ Controller Response
```

SQL Foundation 연결:

```text
SQL Transaction
→ BEGIN / COMMIT / ROLLBACK

JPA Transaction
→ @Transactional
→ Persistence Context
→ Flush
→ Commit / Rollback
```

권장:

- Transaction은 일반적으로 Service public method에 적용
- 조회 전용 Method는 `@Transactional(readOnly = true)`
- 변경 Method는 일반 `@Transactional`
- Entity 변경은 Transaction 안에서 수행
- DTO 변환은 Lazy Loading 필요 여부에 따라 Transaction 안에서 수행
- 여러 Repository 작업이 하나의 비즈니스 작업이면 하나의 Transaction으로 묶음

주의:

- Controller에 Transaction을 두는 것은 일반적으로 권장하지 않는다.
- Repository마다 Transaction을 흩뿌리면 비즈니스 작업 단위가 불명확해진다.
- Transaction이 너무 길면 DB Connection, Lock, 성능 문제가 생길 수 있다.
- 외부 API 호출을 Transaction 안에 오래 두는 것은 위험하다.
- Self Invocation은 `@Transactional`이 적용되지 않을 수 있다.

---

### [FAQ]

Q. Transaction Boundary는 뭐야?
A. DB 작업이 하나의 논리적 작업 단위로 처리되는 범위다.

Q. JPA에서 Transaction Boundary가 중요한 이유는 뭐야?
A. Persistence Context, Dirty Checking, Flush, Rollback, Lazy Loading 동작 범위를 결정하기 때문이다.

Q. `@Transactional`은 어디에 두는 게 좋아?
A. 일반적으로 Service public method에 둔다.

Q. Controller에 `@Transactional`을 둬도 돼?
A. 가능은 하지만 HTTP Layer와 Persistence Layer 책임이 섞이므로 일반적으로 권장하지 않는다.

---

## 1.2 Service Transaction Rule

### [개념]

Service Transaction Rule은 비즈니스 작업 단위에 맞춰 Service Layer에서 Transaction을 시작하고 종료하는 규칙이다.

Service는 Repository 호출, Entity 상태 변경, DTO 변환, 예외 처리 흐름을 조정한다.

---

### [핵심]

Service 책임:

- Transaction Boundary 관리
- 비즈니스 흐름 조정
- Repository 호출
- Entity 조회
- Entity 상태 변경
- 권한 / 상태 검증
- DTO 변환
- Custom Exception 발생
- Rollback 기준 제공

권장 구조:

```text
Controller
→ Request DTO
→ Service @Transactional
→ Repository
→ Entity
→ Response DTO
```

---

### [실무]

조회 예시:

```java
@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    Post post = postRepository.findByIdWithUser(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    return PostResponse.from(post);
}
```

수정 예시:

```java
@Transactional
public void updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    post.update(request.title(), request.content());
}
```

권장:

- 조회 Method는 readOnly 적용
- 수정 Method는 일반 Transaction 적용
- Entity를 조회한 뒤 상태 변경 Method 호출
- Request DTO를 Entity로 직접 받지 않음
- Response DTO를 Service Transaction 안에서 생성
- 권한 검증과 상태 검증을 변경 전에 수행

주의:

- Service 내부 private method에 `@Transactional`을 붙여도 Proxy 기반 AOP가 적용되지 않을 수 있다.
- 같은 Class 내부 Method 호출은 Transaction 적용이 안 될 수 있다.
- readOnly Method에서 Entity 변경을 기대하지 않는다.
- DTO 변환이 Lazy Field를 접근하면 Transaction 범위 안에서 처리해야 한다.
- Transaction 범위 안에서 불필요한 네트워크 호출을 오래 수행하지 않는다.

---

### [FAQ]

Q. Service Layer에 Transaction을 두는 이유는 뭐야?
A. 하나의 비즈니스 작업 단위 안에서 Repository 호출, Entity 변경, Flush, Rollback을 관리하기 위해서다.

Q. 조회 Method에도 Transaction이 필요해?
A. Lazy Loading, 일관된 조회, readOnly 최적화 의도를 위해 `@Transactional(readOnly = true)`를 사용할 수 있다.

Q. 수정 Method에 readOnly를 붙여도 돼?
A. 권장하지 않는다. 변경 작업은 일반 `@Transactional`을 사용해야 한다.

Q. Service에서 DTO 변환을 하는 이유는 뭐야?
A. Lazy Loading 접근 위치를 Transaction 범위 안으로 통제하고 Entity 직접 노출을 막기 위해서다.

---

## 1.3 readOnly Transaction

### [개념]

readOnly Transaction은 조회 전용 Transaction임을 명시하는 설정이다.

JPA와 Hibernate에서는 readOnly Transaction이 Dirty Checking 부담을 줄이고 변경 의도를 차단하는 신호로 사용될 수 있다.

---

### [핵심]

핵심 키워드:

- `@Transactional(readOnly = true)`
- Read-only Query
- 조회 전용
- Dirty Checking 최소화
- Flush 최적화
- Service Query Method
- Intent Declaration

사용 상황:

- 단건 조회
- 목록 조회
- 검색 API
- DTO Projection 조회
- 통계 조회
- 변경이 없는 Service Method

---

### [실무]

예시:

```java
@Transactional(readOnly = true)
public List<PostSummaryResponse> getPostSummaries() {
    return postRepository.findPostSummaries();
}
```

적용 기준:

```text
조회 Method
→ @Transactional(readOnly = true)

변경 Method
→ @Transactional

Bulk Update / Delete
→ @Transactional + @Modifying
```

권장:

- 조회 Service Method에 readOnly 적용
- 변경 없는 Query Method에 적용
- DTO Projection 조회에 적용
- 복잡한 조회에서도 변경이 없으면 readOnly 적용
- Class Level readOnly + Method Level write Transaction 조합 가능

예시:

```java
@Service
@Transactional(readOnly = true)
public class PostService {

    public PostResponse getPost(Long postId) {
        return postRepository.findById(postId)
                .map(PostResponse::from)
                .orElseThrow();
    }

    @Transactional
    public void updatePost(Long postId, PostUpdateRequest request) {
        Post post = postRepository.findById(postId).orElseThrow();
        post.update(request.title(), request.content());
    }
}
```

주의:

- readOnly Transaction에서 Entity 변경을 기대하지 않는다.
- readOnly는 DB 쓰기를 절대적으로 막는 보안 장치가 아니다.
- 변경 Method에 readOnly가 붙어 있으면 Dirty Checking 반영이 기대와 다를 수 있다.
- readOnly 설정은 Provider와 DB에 따라 동작 차이가 있을 수 있다.
- Bulk Query는 readOnly와 충돌하지 않도록 Method Transaction을 명확히 한다.

---

### [FAQ]

Q. readOnly Transaction은 뭐야?
A. 조회 전용 Transaction임을 명시하는 설정이다.

Q. readOnly를 붙이면 쓰기가 완전히 막혀?
A. DB와 Provider에 따라 다르므로 보안 장치처럼 의존하면 안 된다. 변경 의도를 차단하는 설계 신호로 사용한다.

Q. 조회 Method에는 readOnly를 붙이는 게 좋아?
A. 일반적으로 좋다. 조회 전용 의도를 명확히 하고 불필요한 변경 감지 부담을 줄일 수 있다.

Q. readOnly Method에서 Entity를 수정하면 어떻게 돼?
A. 변경 반영을 기대하지 않아야 하며 수정 Method는 일반 Transaction으로 분리해야 한다.

---

# 2. Rollback and Exception Rule

## 2.1 Rollback Rule

### [개념]

Rollback Rule은 Transaction 중 예외가 발생했을 때 DB 변경을 취소할지 결정하는 기준이다.

Spring Transaction은 기본적으로 RuntimeException과 Error에 대해 Rollback을 수행한다.

---

### [핵심]

핵심 키워드:

- Rollback
- RuntimeException
- CheckedException
- `rollbackFor`
- BusinessException
- GlobalExceptionHandler
- Transaction Boundary
- Data Consistency

기본 기준:

| 예외 종류               | 기본 Rollback      |
| ----------------------- | ------------------ |
| RuntimeException        | Rollback           |
| Error                   | Rollback           |
| CheckedException        | 기본 Rollback 아님 |
| Custom RuntimeException | Rollback           |

---

### [실무]

Custom Exception 예시:

```java
public class BusinessException extends RuntimeException {

    private final String code;

    public BusinessException(String code, String message) {
        super(message);
        this.code = code;
    }
}
```

Rollback 예시:

```java
@Transactional
public void createPost(PostCreateRequest request) {
    Post post = Post.create(request.title(), request.content());
    postRepository.save(post);

    throw new BusinessException("CREATE_FAILED", "게시글 생성에 실패했습니다.");
}
```

CheckedException Rollback 예시:

```java
@Transactional(rollbackFor = IOException.class)
public void importData() throws IOException {
    // file read
    // repository save
}
```

권장:

- 비즈니스 예외는 RuntimeException 기반 CustomException 사용 가능
- CheckedException에서 Rollback이 필요하면 `rollbackFor` 명시
- 예외를 catch한 뒤 삼키지 않음
- 실패 응답은 GlobalExceptionHandler에서 처리
- Transaction 실패 정책을 프로젝트 규칙으로 통일

주의:

- 예외를 catch하고 밖으로 던지지 않으면 Rollback되지 않을 수 있다.
- CheckedException은 기본 Rollback 대상이 아니다.
- 외부 API 호출 결과는 DB Rollback으로 되돌릴 수 없다.
- Transaction 안에서 파일, 메시지, 결제 같은 외부 작업과 DB 작업 순서를 신중히 설계한다.
- Rollback이 필요한 예외와 아닌 예외를 구분해야 한다.

---

### [FAQ]

Q. Spring Transaction은 어떤 예외에서 Rollback돼?
A. 기본적으로 RuntimeException과 Error에서 Rollback된다.

Q. CheckedException은 Rollback돼?
A. 기본적으로 Rollback되지 않는다. 필요하면 `rollbackFor`를 명시해야 한다.

Q. 예외를 catch하면 Rollback돼?
A. 예외를 catch하고 다시 던지지 않으면 Rollback이 안 될 수 있다.

Q. Custom BusinessException은 어떻게 설계하는 게 좋아?
A. RuntimeException 기반으로 만들면 기본 Rollback 정책과 잘 맞는다.

---

## 2.2 Exception Handling and Transaction

### [개념]

Exception Handling and Transaction은 예외 처리 방식이 Transaction Commit / Rollback에 어떤 영향을 주는지 관리하는 규칙이다.

JPA Service Method에서는 예외를 숨기지 않고 Transaction 실패 여부가 명확히 드러나도록 처리해야 한다.

---

### [핵심]

예외 처리 기준:

- 실패하면 예외를 던짐
- 비즈니스 실패는 CustomException
- Controller Advice에서 응답 변환
- Service에서 예외를 삼키지 않음
- Rollback 대상 예외 확인
- 외부 시스템 실패 처리 정책 분리

---

### [실무]

비권장 예시:

```java
@Transactional
public void updatePost(Long postId, PostUpdateRequest request) {
    try {
        Post post = postRepository.findById(postId).orElseThrow();
        post.update(request.title(), request.content());
    } catch (Exception e) {
        log.error("update failed", e);
    }
}
```

문제:

```text
예외를 catch 후 삼킴
→ Transaction 정상 종료 가능
→ Commit 가능성
→ 실패가 응답에 반영되지 않음
```

권장 예시:

```java
@Transactional
public void updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    post.update(request.title(), request.content());
}
```

권장:

- Service에서 복구할 수 없는 예외는 던짐
- Controller Advice에서 API Error Response 생성
- Transaction 실패와 API 실패가 일관되게 연결되도록 설계
- catch가 필요하면 Rollback 여부를 명확히 처리
- 외부 API 보상 처리 필요 시 별도 Transaction 전략 검토

주의:

- catch 후 정상 반환하면 Commit될 수 있다.
- `setRollbackOnly` 같은 강제 Rollback은 신중히 사용한다.
- 비즈니스 실패와 시스템 실패를 구분한다.
- 예외 변환 과정에서 원인 예외를 잃지 않도록 한다.
- Transaction 안에서 너무 넓은 try-catch를 사용하지 않는다.

---

### [FAQ]

Q. Service에서 예외를 catch해도 돼?
A. 가능하지만 실패를 정상 처리로 바꾸면 Transaction이 Commit될 수 있어 주의해야 한다.

Q. 예외는 어디서 API 응답으로 바꿔?
A. 일반적으로 GlobalExceptionHandler 또는 Controller Advice에서 처리한다.

Q. Transaction 실패를 숨기면 왜 위험해?
A. DB 변경은 Commit되었는데 API는 실패를 제대로 표현하지 못하거나 반대로 데이터 일관성이 깨질 수 있다.

Q. 외부 API 실패와 DB Rollback은 어떻게 연결해?
A. 외부 작업은 DB Transaction으로 되돌릴 수 없으므로 보상 처리, 순서 조정, 별도 Transaction 전략을 검토해야 한다.

---

# 3. Cascade

## 3.1 Cascade Concept

### [개념]

Cascade는 Parent Entity의 영속성 작업을 Child Entity로 전파하는 JPA 기능이다.

Cascade는 생명주기가 완전히 종속된 관계에서만 신중히 사용해야 한다.

---

### [핵심]

핵심 키워드:

- Cascade
- CascadeType.PERSIST
- CascadeType.MERGE
- CascadeType.REMOVE
- CascadeType.ALL
- Parent Entity
- Child Entity
- Lifecycle Dependency
- Shared Entity Caution

Cascade 종류:

| Type    | 의미          |
| ------- | ------------- |
| PERSIST | 저장 전파     |
| MERGE   | 병합 전파     |
| REMOVE  | 삭제 전파     |
| REFRESH | 새로고침 전파 |
| DETACH  | 분리 전파     |
| ALL     | 전체 전파     |

---

### [실무]

사용 후보:

```text
Order
→ OrderItem

Post
→ Attachment

Parent
→ 완전히 종속된 Child
```

예시:

```java
@OneToMany(mappedBy = "order", cascade = CascadeType.PERSIST)
private List<OrderItem> orderItems = new ArrayList<>();
```

생명주기 판단:

```text
Child가 Parent 없이 의미 없음
→ Cascade 후보

Child가 여러 Parent에서 공유됨
→ Cascade REMOVE 위험

Child가 독립적으로 관리됨
→ Cascade 지양
```

권장:

- Cascade는 생명주기 종속성이 명확할 때만 사용
- 저장 전파와 삭제 전파를 구분
- `CascadeType.ALL`은 신중히 사용
- 공유 Entity에는 REMOVE 전파 금지
- Cascade 적용 후 실제 INSERT / DELETE SQL 확인

주의:

- Cascade는 연관관계 설정을 대신하지 않는다.
- Cascade는 DB Foreign Key Constraint와 다르다.
- Cascade REMOVE는 예상치 못한 삭제를 만들 수 있다.
- ManyToOne에 Cascade REMOVE를 쓰는 것은 매우 위험하다.
- CascadeType.ALL은 편하지만 위험 범위가 넓다.

---

### [FAQ]

Q. Cascade는 뭐야?
A. Parent Entity의 저장, 병합, 삭제 같은 영속성 작업을 Child Entity로 전파하는 기능이다.

Q. Cascade는 언제 써?
A. Child가 Parent 없이는 의미 없고 생명주기가 완전히 종속될 때 사용한다.

Q. Cascade는 연관관계 설정을 자동으로 해줘?
A. 아니다. 객체 참조는 직접 설정해야 하며 Cascade는 영속성 작업만 전파한다.

Q. CascadeType.ALL을 써도 돼?
A. 가능하지만 삭제 전파까지 포함하므로 매우 신중히 사용해야 한다.

---

## 3.2 Cascade Persist

### [개념]

Cascade Persist는 Parent Entity를 저장할 때 Child Entity도 함께 저장되도록 전파하는 기능이다.

신규 Parent와 신규 Child를 함께 생성하는 Aggregate 구조에서 사용할 수 있다.

---

### [핵심]

핵심 키워드:

- CascadeType.PERSIST
- Parent Save
- Child Save
- New Entity
- Aggregate
- Convenience Method
- Relationship Setup

동작 흐름:

```text
Parent 생성
→ Child 생성
→ Parent에 Child 추가
→ Parent save
→ Child persist 전파
→ INSERT Parent / Child
```

---

### [실무]

예시:

```java
@Entity
public class Order {

    @OneToMany(mappedBy = "order", cascade = CascadeType.PERSIST)
    private List<OrderItem> orderItems = new ArrayList<>();

    public void addOrderItem(OrderItem orderItem) {
        orderItems.add(orderItem);
        orderItem.changeOrder(this);
    }
}
```

Service 예시:

```java
@Transactional
public Long createOrder(OrderCreateRequest request) {
    Order order = Order.create(request.userId());

    for (OrderItemRequest itemRequest : request.items()) {
        OrderItem orderItem = OrderItem.create(itemRequest.productId(), itemRequest.quantity());
        order.addOrderItem(orderItem);
    }

    Order savedOrder = orderRepository.save(order);
    return savedOrder.getOrderId();
}
```

권장:

- Parent와 Child를 함께 생성할 때 사용
- 양방향이면 편의 Method로 관계 설정
- Child가 독립 저장되지 않는 구조에서 사용
- Cascade 적용 범위는 최소화
- 테스트로 Child INSERT 확인

주의:

- Cascade Persist는 Child 관계 설정을 대신하지 않는다.
- `orderItems.add(orderItem)`만 하고 Owning Side를 설정하지 않으면 FK 반영이 누락될 수 있다.
- Child가 이미 존재하는 Entity이면 Persist 전파가 부적절할 수 있다.
- 공유 Entity를 새로 persist하려 하면 오류가 발생할 수 있다.
- Cascade Merge와 혼동하지 않는다.

---

### [FAQ]

Q. Cascade Persist는 뭐야?
A. Parent Entity 저장 시 신규 Child Entity 저장도 함께 전파하는 기능이다.

Q. Parent save만 하면 Child도 저장돼?
A. Cascade Persist가 설정되어 있고 관계가 올바르게 설정되어 있으면 Child 저장이 전파될 수 있다.

Q. Cascade Persist가 FK 설정도 해줘?
A. 아니다. Owning Side의 연관관계 Field는 직접 설정해야 한다.

Q. 이미 존재하는 Child에도 Cascade Persist를 쓰면 돼?
A. 주의해야 한다. 이미 존재하는 Entity는 조회 후 연관관계를 설정하는 방식이 더 안전하다.

---

## 3.3 Cascade Remove Caution

### [개념]

Cascade Remove는 Parent Entity 삭제 시 Child Entity 삭제도 전파하는 기능이다.

삭제 전파는 데이터 손실 위험이 크므로 완전 종속 Child에만 제한적으로 사용해야 한다.

---

### [핵심]

핵심 키워드:

- CascadeType.REMOVE
- CascadeType.ALL
- Delete Propagation
- Parent Delete
- Child Delete
- Shared Entity Danger
- Data Loss
- Foreign Key Constraint

위험 상황:

```text
User 삭제
→ User가 작성한 Post 삭제
→ Post의 Comment 삭제
→ 데이터 대량 손실 가능
```

---

### [실무]

위험 예시:

```java
@ManyToOne(cascade = CascadeType.REMOVE)
@JoinColumn(name = "user_id")
private User user;
```

문제:

```text
Post 삭제
→ User 삭제 전파 가능
→ 공유 Parent 삭제 위험
```

사용 후보:

```java
@OneToMany(mappedBy = "order", cascade = CascadeType.REMOVE)
private List<OrderItem> orderItems = new ArrayList<>();
```

검토 기준:

```text
Child가 Parent 없이는 존재 불가
→ REMOVE 후보

Child가 다른 Entity와 공유됨
→ REMOVE 금지

Parent 삭제 시 Child 삭제가 비즈니스 요구사항
→ REMOVE 또는 orphanRemoval 검토
```

권장:

- Cascade REMOVE는 완전 종속 Child에만 사용
- ManyToOne에는 REMOVE 사용 지양
- 공유 Entity에는 REMOVE 전파 금지
- 삭제 전 테스트 데이터로 SQL 확인
- Soft Delete 요구사항과 충돌 여부 확인

주의:

- CascadeType.ALL에는 REMOVE가 포함된다.
- 삭제 전파는 즉각적인 데이터 손실을 만들 수 있다.
- DB FK ON DELETE CASCADE와 JPA Cascade는 별도 개념이다.
- Parent 삭제 API가 호출될 때 영향 범위를 반드시 확인한다.
- 운영 데이터 삭제 정책과 감사 로그 요구사항을 함께 검토한다.

---

### [FAQ]

Q. Cascade Remove는 뭐야?
A. Parent Entity 삭제 시 Child Entity 삭제도 전파하는 기능이다.

Q. ManyToOne에 Cascade REMOVE를 써도 돼?
A. 매우 위험하다. Child 삭제가 Parent 삭제로 전파될 수 있으므로 일반적으로 사용하지 않는다.

Q. CascadeType.ALL은 왜 위험해?
A. 저장뿐 아니라 삭제 전파까지 포함하므로 예상치 못한 데이터 삭제가 발생할 수 있다.

Q. DB ON DELETE CASCADE와 JPA Cascade는 같아?
A. 아니다. DB Constraint 동작과 JPA 영속성 전파는 별도 개념이다.

---

# 4. Orphan Removal

## 4.1 Orphan Removal Concept

### [개념]

orphanRemoval은 Parent Collection에서 Child Entity가 제거되었을 때 해당 Child Row를 삭제하는 JPA 기능이다.

orphanRemoval은 Child 생명주기가 Parent에 완전히 종속될 때만 사용해야 한다.

---

### [핵심]

핵심 키워드:

- orphanRemoval
- Orphan Entity
- Parent Collection
- Child Delete
- Lifecycle Dependency
- OneToMany
- Delete Orphan
- Collection Remove

동작 흐름:

```text
Parent 조회
→ Parent.children에서 Child 제거
→ orphanRemoval = true
→ Flush 시 Child DELETE 가능
```

---

### [실무]

예시:

```java
@OneToMany(mappedBy = "post", orphanRemoval = true)
private List<PostImage> images = new ArrayList<>();

public void removeImage(PostImage image) {
    images.remove(image);
    image.changePost(null);
}
```

사용 후보:

```text
Post
→ PostImage

Order
→ OrderItem

Parent
→ Parent 없이는 의미 없는 Child
```

권장:

- Child가 Parent 없이 의미 없을 때 사용
- Collection 제거가 실제 삭제 요구사항인지 확인
- 편의 Method로 양쪽 관계 정리
- nullable FK와 삭제 정책을 함께 검토
- 테스트로 DELETE SQL 확인

주의:

- Collection에서 remove하면 삭제될 수 있다.
- 단순 관계 해제와 Entity 삭제를 혼동하지 않는다.
- Child가 다른 Parent와 공유되면 사용하면 안 된다.
- orphanRemoval은 Cascade REMOVE와 비슷해 보이지만 동작 조건이 다르다.
- Soft Delete 정책과 충돌할 수 있다.

---

### [FAQ]

Q. orphanRemoval은 뭐야?
A. Parent Collection에서 Child가 제거되면 해당 Child Entity를 삭제하는 기능이다.

Q. orphanRemoval은 언제 써?
A. Child가 Parent 없이는 의미 없고 Collection에서 제거되면 삭제되어야 할 때 사용한다.

Q. Collection에서 remove하면 DB Row도 삭제돼?
A. orphanRemoval이 true이면 Flush 시 DELETE SQL이 실행될 수 있다.

Q. orphanRemoval은 관계 해제야 삭제야?
A. 삭제에 가깝다. 단순 FK null 처리와 다르게 Child Row 제거로 이어질 수 있다.

---

## 4.2 orphanRemoval vs Cascade REMOVE

### [개념]

orphanRemoval과 Cascade REMOVE는 둘 다 Child 삭제와 관련되지만 삭제가 발생하는 조건이 다르다.

Cascade REMOVE는 Parent 삭제가 Child 삭제로 전파되는 기능이고, orphanRemoval은 Parent Collection에서 제거된 Child를 삭제하는 기능이다.

---

### [핵심]

비교:

| 구분      | orphanRemoval             | Cascade REMOVE           |
| --------- | ------------------------- | ------------------------ |
| 삭제 조건 | Collection에서 Child 제거 | Parent Entity 삭제       |
| 주요 목적 | 고아 객체 삭제            | 삭제 작업 전파           |
| 사용 관계 | 주로 OneToMany            | Parent-Child 관계        |
| 위험      | remove가 DELETE로 이어짐  | Parent 삭제 시 대량 삭제 |
| 공통 전제 | Child 생명주기 종속       | Child 생명주기 종속      |

---

### [실무]

orphanRemoval 예시:

```java
post.getImages().remove(image);
```

해석:

```text
images Collection에서 제거
→ image가 고아 객체
→ DELETE 가능
```

Cascade REMOVE 예시:

```java
postRepository.delete(post);
```

해석:

```text
Post 삭제
→ Cascade REMOVE
→ images 삭제 전파 가능
```

선택 기준:

```text
Parent 삭제 시 Child 삭제 필요
→ Cascade REMOVE 검토

Collection에서 Child 제거 시 Child 삭제 필요
→ orphanRemoval 검토

둘 다 필요
→ 둘 다 가능하지만 삭제 범위 테스트 필수
```

권장:

- 삭제 조건을 명확히 구분
- 둘 다 사용할 때 삭제 범위 테스트
- 공유 Child에는 둘 다 사용 지양
- Soft Delete 정책이 있으면 별도 구현 검토
- API 삭제 요구사항과 Mapping 동작을 일치시킴

주의:

- orphanRemoval과 Cascade REMOVE를 같은 기능으로 오해하지 않는다.
- Collection 조작이 실제 DELETE로 이어지는지 확인해야 한다.
- 삭제 전파는 운영 데이터 손실 위험이 있다.
- Bulk Delete와 Cascade / orphanRemoval 동작 차이를 검토해야 한다.
- 복잡한 삭제 정책은 Service에서 명시적으로 처리하는 것이 더 안전할 수 있다.

---

### [FAQ]

Q. orphanRemoval과 Cascade REMOVE는 같은 거야?
A. 아니다. orphanRemoval은 Collection에서 제거된 Child 삭제이고 Cascade REMOVE는 Parent 삭제 시 Child 삭제 전파다.

Q. 둘 다 같이 써도 돼?
A. 가능하지만 Child 생명주기가 완전히 종속된 경우에만 사용하고 삭제 범위를 테스트해야 한다.

Q. 공유 Child에 orphanRemoval을 써도 돼?
A. 안 된다. 다른 Parent에서도 참조할 수 있는 Child가 삭제될 위험이 있다.

Q. Soft Delete에서는 orphanRemoval을 써도 돼?
A. 주의해야 한다. orphanRemoval은 실제 DELETE로 이어질 수 있어 Soft Delete 정책과 충돌할 수 있다.

---

# 5. Auditing

## 5.1 Auditing Concept

### [개념]

Auditing은 Entity의 생성일, 수정일, 생성자, 수정자 같은 메타데이터를 자동으로 관리하는 기능이다.

Spring Data JPA Auditing은 `@CreatedDate`, `@LastModifiedDate`를 통해 공통 시간 Field를 관리할 수 있다.

---

### [핵심]

핵심 키워드:

- Auditing
- CreatedDate
- LastModifiedDate
- CreatedBy
- LastModifiedBy
- BaseTimeEntity
- EntityListeners
- EnableJpaAuditing
- LocalDateTime
- Data Traceability

Auditing 대상:

- createdAt
- updatedAt
- createdBy
- updatedBy
- deletedAt
- deletedBy
- version history candidate

---

### [실무]

BaseTimeEntity 예시:

```java
@Getter
@MappedSuperclass
@EntityListeners(AuditingEntityListener.class)
public abstract class BaseTimeEntity {

    @CreatedDate
    @Column(nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @LastModifiedDate
    @Column(nullable = false)
    private LocalDateTime updatedAt;
}
```

Entity 적용 예시:

```java
@Entity
public class Post extends BaseTimeEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long postId;
}
```

설정 예시:

```java
@EnableJpaAuditing
@SpringBootApplication
public class Application {
}
```

권장:

- 공통 시간 Field는 BaseTimeEntity로 분리
- `createdAt`은 `updatable = false`
- 날짜 / 시간 타입은 `LocalDateTime` 사용 가능
- 모든 주요 Entity에 일관 적용
- 생성자 / 수정자 Auditing은 Security Context와 연결 검토

주의:

- `@EnableJpaAuditing` 누락 시 동작하지 않을 수 있다.
- Auditing은 Entity가 JPA를 통해 저장 / 수정될 때 동작한다.
- Bulk Query에서는 Auditing이 자동 적용되지 않을 수 있다.
- DB Time과 Application Time 기준을 통일해야 한다.
- Time Zone 정책을 명확히 해야 한다.

---

### [FAQ]

Q. Auditing은 뭐야?
A. Entity의 생성일, 수정일, 생성자, 수정자 같은 메타데이터를 자동으로 관리하는 기능이다.

Q. createdAt과 updatedAt은 어떻게 관리해?
A. Spring Data JPA Auditing의 `@CreatedDate`, `@LastModifiedDate`를 사용할 수 있다.

Q. Auditing을 쓰려면 무엇이 필요해?
A. `@EnableJpaAuditing`, `@EntityListeners(AuditingEntityListener.class)`, Auditing Annotation이 필요하다.

Q. Bulk Update에서도 updatedAt이 자동 변경돼?
A. 기대하지 않는 것이 좋다. Bulk Query는 Auditing을 우회할 수 있으므로 직접 갱신을 검토해야 한다.

---

## 5.2 Base Entity Rule

### [개념]

Base Entity Rule은 여러 Entity에서 공통으로 사용하는 Field와 Mapping을 상위 Class로 분리하는 규칙이다.

대표적으로 생성일, 수정일을 가진 BaseTimeEntity가 있다.

---

### [핵심]

공통 Field 후보:

- createdAt
- updatedAt
- createdBy
- updatedBy
- deleted
- deletedAt
- version

Annotation 후보:

- `@MappedSuperclass`
- `@EntityListeners`
- `@CreatedDate`
- `@LastModifiedDate`
- `@Version`

---

### [실무]

BaseTimeEntity 구조:

```java
@Getter
@MappedSuperclass
@EntityListeners(AuditingEntityListener.class)
public abstract class BaseTimeEntity {

    @CreatedDate
    @Column(nullable = false, updatable = false)
    protected LocalDateTime createdAt;

    @LastModifiedDate
    @Column(nullable = false)
    protected LocalDateTime updatedAt;
}
```

Soft Delete Base 후보:

```java
@MappedSuperclass
public abstract class BaseSoftDeleteEntity {

    @Column(nullable = false)
    protected boolean deleted = false;

    protected LocalDateTime deletedAt;
}
```

권장:

- 모든 Entity에 필요한 공통 Field만 Base로 분리
- 너무 많은 기능을 Base Entity에 넣지 않음
- Auditing Base와 Soft Delete Base를 분리 검토
- `@MappedSuperclass`와 `@Entity` 차이를 구분
- 공통 Field 변경 시 전체 Entity 영향 검토

주의:

- Base Entity가 비대해지면 모든 Entity가 불필요한 Field를 가진다.
- Soft Delete는 모든 Entity에 무조건 적용하지 않는다.
- Base Class의 Access Modifier를 일관화한다.
- Auditing Field는 API Response에서 필요한 경우 DTO로 노출한다.
- Base Entity에 비즈니스 로직을 과도하게 넣지 않는다.

---

### [FAQ]

Q. BaseTimeEntity는 뭐야?
A. 여러 Entity에서 공통으로 사용하는 createdAt, updatedAt Field를 모아둔 상위 Class다.

Q. `@MappedSuperclass`는 뭐야?
A. 상위 Class의 Mapping 정보를 하위 Entity에 상속하기 위한 JPA Annotation이다.

Q. 모든 Entity가 BaseTimeEntity를 상속해야 해?
A. 생성일 / 수정일 관리가 필요한 Entity에 적용하면 된다. 모든 Entity에 무조건 적용할 필요는 없다.

Q. Soft Delete Field도 Base Entity에 넣어도 돼?
A. 가능하지만 모든 Entity에 Soft Delete가 필요한지 먼저 검토해야 한다.

---

# 6. Pagination

## 6.1 Page and Slice Rule

### [개념]

Page와 Slice는 Repository Pagination 결과를 표현하는 Spring Data의 Return Type이다.

Page는 전체 Count를 포함하고, Slice는 다음 데이터 존재 여부 중심으로 동작한다.

---

### [핵심]

핵심 키워드:

- Page
- Slice
- Pageable
- Sort
- Count Query
- hasNext
- Infinite Scroll
- Load More
- Offset Pagination
- Stable Sort

비교:

| 구분             | Page           | Slice                |
| ---------------- | -------------- | -------------------- |
| 전체 Count       | 있음           | 없음                 |
| 전체 페이지 수   | 있음           | 없음                 |
| 다음 페이지 여부 | 있음           | 있음                 |
| Count Query 비용 | 있음           | 보통 없음            |
| 사용 상황        | 페이지 번호 UI | 무한 스크롤 / 더보기 |

---

### [실무]

Page 예시:

```java
Page<Post> findByDeletedFalse(Pageable pageable);
```

Slice 예시:

```java
Slice<Comment> findByPost_PostIdOrderByCreatedAtDesc(Long postId, Pageable pageable);
```

Service 예시:

```java
@Transactional(readOnly = true)
public Slice<CommentResponse> getComments(Long postId, Pageable pageable) {
    return commentRepository.findByPost_PostIdOrderByCreatedAtDesc(postId, pageable)
            .map(CommentResponse::from);
}
```

SQL Foundation 연결:

```text
SQL LIMIT / OFFSET
→ Pageable

SQL COUNT
→ Page

No Count + hasNext
→ Slice

ORDER BY
→ Stable Sort
```

권장:

- 전체 페이지 번호가 필요하면 Page
- 무한 스크롤 / 더보기는 Slice
- 대량 목록은 List 대신 Page / Slice
- 정렬 기준은 안정적으로 설정
- `createdAt desc`, `id desc` 보조 정렬 검토
- Entity Page / Slice는 DTO로 변환

주의:

- Page는 Count Query 비용이 발생한다.
- Slice는 전체 페이지 수를 알 수 없다.
- Offset Pagination은 뒤 페이지로 갈수록 느려질 수 있다.
- 정렬 기준이 불안정하면 중복 / 누락이 생길 수 있다.
- DTO 변환 중 Lazy Field 접근으로 N+1이 발생할 수 있다.

---

### [FAQ]

Q. Page와 Slice 차이는 뭐야?
A. Page는 전체 Count와 전체 페이지 수를 제공하고 Slice는 다음 데이터 존재 여부 중심이다.

Q. 무한 스크롤에는 뭐가 좋아?
A. 전체 Count가 필요 없으므로 Slice가 적합한 경우가 많다.

Q. Page는 왜 느릴 수 있어?
A. 전체 Count를 구하기 위한 Count Query가 추가로 실행될 수 있기 때문이다.

Q. Page나 Slice를 그대로 응답해도 돼?
A. 가능하지만 API 응답 구조를 위해 DTO로 변환하거나 별도 Page Response로 감싸는 것이 좋다.

---

## 6.2 Pageable and Sort

### [개념]

Pageable은 Pagination 요청 정보를 담는 객체다.

Pageable은 page, size, sort 정보를 포함하며 Repository Query에 전달된다.

---

### [핵심]

핵심 키워드:

- Pageable
- PageRequest
- Sort
- page
- size
- direction
- order by
- Stable Sort
- Default Sort

Pageable 구성:

```text
page
→ 페이지 번호

size
→ 페이지 크기

sort
→ 정렬 Field와 방향
```

---

### [실무]

Controller 예시:

```java
@GetMapping
public Page<PostResponse> getPosts(Pageable pageable) {
    return postService.getPosts(pageable);
}
```

Service 예시:

```java
@Transactional(readOnly = true)
public Page<PostResponse> getPosts(Pageable pageable) {
    return postRepository.findByDeletedFalse(pageable)
            .map(PostResponse::from);
}
```

Default Pageable 생성 예시:

```java
Pageable pageable = PageRequest.of(
        0,
        20,
        Sort.by(Sort.Direction.DESC, "createdAt")
);
```

권장:

- 기본 size 제한 설정
- 최대 size 제한 설정
- 기본 Sort 제공
- 안정적 정렬 기준 사용
- 사용자 입력 Sort Field 제한
- Page 번호는 0-based / 1-based 변환 기준 명확화

주의:

- 무제한 size 허용 금지
- 사용자 입력 Sort Field를 그대로 허용하면 오류나 보안 문제가 생길 수 있다.
- 정렬 Field는 Entity Field 이름 기준이다.
- Native Query Sort는 DB Column 기준과 충돌할 수 있다.
- createdAt만으로 정렬이 불안정하면 id 보조 정렬 검토

---

### [FAQ]

Q. Pageable은 뭐야?
A. 페이지 번호, 페이지 크기, 정렬 정보를 Repository Query에 전달하는 객체다.

Q. Pageable sort는 Column 이름 기준이야?
A. 일반 JPA Query에서는 Entity Field 이름 기준이다.

Q. page 번호는 0부터 시작해?
A. Spring Data Pageable은 기본적으로 0-based page index를 사용한다.

Q. Pageable size를 제한해야 해?
A. 그렇다. 너무 큰 size는 대량 조회와 성능 문제를 만들 수 있다.

---

## 6.3 Pagination Performance Caution

### [개념]

Pagination Performance Caution은 Count Query, Offset 비용, Collection Fetch Join, N+1, Sort 안정성 문제를 검토하는 기준이다.

Pagination은 단순히 Page나 Slice를 반환하는 것이 아니라 Query 성능과 응답 안정성을 함께 설계해야 한다.

---

### [핵심]

주의 대상:

- Count Query 비용
- Offset Pagination 비용
- Collection Fetch Join
- OneToMany Join 중복
- Page.map N+1
- Sort 안정성
- Index 사용 가능성
- Cursor / Keyset Pagination 후보

---

### [실무]

위험 흐름:

```text
Page<Post> 조회
→ Post.comments Collection Fetch Join
→ Row 중복
→ Pagination 불안정
→ Count Query 복잡
→ 성능 저하
```

권장 후보:

```text
일반 페이지 번호 UI
→ Page

무한 스크롤
→ Slice

대용량 뒤 페이지 조회
→ Keyset / Cursor Pagination 검토

Parent 목록 + Child 일부
→ DTO Projection / 별도 Query

Child 목록
→ Child Repository에서 Parent ID 조건으로 Slice 조회
```

Keyset 후보 기준:

```text
createdAt < lastCreatedAt
or
id < lastId

ORDER BY createdAt DESC, id DESC
LIMIT size
```

권장:

- Page Count Query 비용 확인
- Slice로 충분한지 검토
- 대량 데이터는 Offset 비용 검토
- Sort Field에 Index 필요성 검토
- Collection Fetch Join과 Pageable 조합 피하기
- Page.map 내부 Lazy 접근 확인

주의:

- Pagination은 N+1과 함께 검토해야 한다.
- DTO 변환이 연관 Entity에 접근하면 Page에서도 N+1이 발생한다.
- Offset Pagination은 뒤 페이지로 갈수록 느릴 수 있다.
- Keyset Pagination은 정렬 기준과 커서 값 설계가 필요하다.
- QueryDSL / Native Query와 Pagination 조합은 Count Query를 별도로 검토해야 한다.

---

### [FAQ]

Q. Pagination 성능에서 가장 먼저 볼 것은 뭐야?
A. Count Query 비용, 정렬 기준, N+1 여부, Collection Fetch Join 여부를 확인한다.

Q. Offset Pagination이 느린 이유는 뭐야?
A. 뒤 페이지로 갈수록 DB가 건너뛰어야 하는 Row가 많아질 수 있기 때문이다.

Q. Keyset Pagination은 언제 검토해?
A. 대량 데이터에서 무한 스크롤이나 다음 페이지 조회 성능이 중요할 때 검토한다.

Q. Pagination에서도 N+1이 생겨?
A. 그렇다. Page.map이나 DTO 변환 중 Lazy Association을 접근하면 발생할 수 있다.

---

# 7. Transaction and Pagination Integration

## 7.1 Transaction with Pagination

### [개념]

Transaction with Pagination은 Page / Slice 조회와 DTO 변환을 Transaction 범위 안에서 안전하게 처리하는 규칙이다.

조회 Pagination은 readOnly Transaction 안에서 수행하고, DTO 변환 중 Lazy Loading 발생 여부를 함께 검토한다.

---

### [핵심]

핵심 키워드:

- Pagination
- readOnly Transaction
- DTO Mapping
- Lazy Loading
- N+1
- Page.map
- Slice.map
- Fetch Join
- Projection

조회 흐름:

```text
Service @Transactional(readOnly = true)
→ Repository Page / Slice 조회
→ DTO 변환
→ Lazy Field 접근 여부 확인
→ Response 반환
```

---

### [실무]

예시:

```java
@Transactional(readOnly = true)
public Slice<PostResponse> getPosts(Pageable pageable) {
    return postRepository.findByDeletedFalse(pageable)
            .map(PostResponse::from);
}
```

검토:

```text
PostResponse.from
→ post.getUser().getNickname() 접근 여부 확인
→ 접근한다면 N+1 가능
→ Fetch Join 또는 Projection 검토
```

Projection 대안:

```java
@Transactional(readOnly = true)
public Slice<PostSummaryResponse> getPostSummaries(Pageable pageable) {
    return postRepository.findPostSummaries(pageable);
}
```

권장:

- Pagination 조회는 readOnly Transaction 적용
- DTO 변환을 Transaction 안에서 수행
- DTO 변환 내부 Lazy 접근 확인
- 목록 응답은 Projection 검토
- Page / Slice 자체를 그대로 외부 노출할지 응답 DTO로 감쌀지 결정

주의:

- Transaction 안에서 Lazy Loading이 가능하다고 N+1이 안전한 것은 아니다.
- readOnly Transaction은 조회 의도 표현이지 성능 문제 만능 해결책이 아니다.
- Page.map 변환이 Query를 추가 발생시킬 수 있다.
- Fetch Join Pagination은 Association 종류에 따라 주의가 필요하다.
- Collection Fetch Join은 Pagination과 충돌 가능성이 크다.

---

### [FAQ]

Q. Pagination 조회에도 Transaction을 붙여야 해?
A. readOnly Transaction을 붙이면 조회 의도를 명확히 하고 DTO 변환 중 Lazy Loading 범위를 통제할 수 있다.

Q. Page.map은 Transaction 안에서 하면 안전해?
A. LazyInitializationException은 줄일 수 있지만 N+1 문제는 여전히 발생할 수 있어 Query 수를 확인해야 한다.

Q. Pagination 목록에는 Projection이 좋아?
A. 읽기 전용 목록이고 필요한 Field가 명확하면 Projection이 적합한 경우가 많다.

Q. Slice.map도 N+1이 생길 수 있어?
A. 그렇다. 변환 내부에서 Lazy Association에 접근하면 N+1이 발생할 수 있다.

---

# 8. Transaction, Cascade, Auditing, Pagination Review

## 8.1 Part07 Checklist

### [개념]

Part07 Checklist는 Transaction Boundary, Rollback, Cascade, orphanRemoval, Auditing, Pagination이 실무 기준에 맞는지 검수하는 기준이다.

Review Agent는 Transaction 범위와 삭제 전파, Pagination 성능 문제를 우선 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Transaction Boundary가 Service public method에 있는가?
- [ ] 조회 Method에 readOnly Transaction을 적용했는가?
- [ ] 변경 Method에 일반 Transaction을 적용했는가?
- [ ] Entity 변경이 Transaction 안에서 수행되는가?
- [ ] DTO 변환 위치가 Transaction 범위와 맞는가?
- [ ] Self Invocation으로 Transaction이 누락되지 않는가?
- [ ] 예외 처리 방식이 Rollback을 방해하지 않는가?
- [ ] CheckedException Rollback 필요 시 rollbackFor를 명시했는가?
- [ ] Cascade 사용 이유가 명확한가?
- [ ] CascadeType.ALL을 남용하지 않는가?
- [ ] Cascade REMOVE가 공유 Entity에 적용되지 않는가?
- [ ] ManyToOne에 Cascade REMOVE를 사용하지 않는가?
- [ ] orphanRemoval 사용 대상이 완전 종속 Child인가?
- [ ] Collection remove가 DELETE로 이어지는지 확인했는가?
- [ ] Soft Delete 정책과 orphanRemoval이 충돌하지 않는가?
- [ ] BaseTimeEntity Auditing이 설정되었는가?
- [ ] @EnableJpaAuditing이 적용되었는가?
- [ ] Bulk Query에서 Auditing 누락 가능성을 검토했는가?
- [ ] Page와 Slice 선택 기준이 명확한가?
- [ ] Pageable size 제한과 기본 Sort가 있는가?
- [ ] Pagination Query에서 Count Query 비용을 검토했는가?
- [ ] Collection Fetch Join + Pagination 조합을 피했는가?
- [ ] Page.map / Slice.map에서 N+1 가능성을 검토했는가?
```

---

### [실무]

Review Flow:

```text
Service Method 확인
→ @Transactional 확인
→ readOnly / write 구분
→ Exception Handling 확인
→ Cascade 설정 확인
→ orphanRemoval 설정 확인
→ Auditing 설정 확인
→ Pagination Return Type 확인
→ Pageable Sort / Size 확인
→ SQL Query / Count Query / N+1 확인
```

Common Review Findings:

```text
문제: 수정 Method에 @Transactional 없음
위험: Dirty Checking 미동작
해결: Service public method에 @Transactional 적용

문제: 예외 catch 후 정상 반환
위험: Rollback 없이 Commit 가능
해결: CustomException을 던지고 GlobalExceptionHandler에서 처리

문제: ManyToOne cascade = REMOVE
위험: 공유 Parent Entity 삭제
해결: Cascade REMOVE 제거

문제: orphanRemoval을 공유 Child에 사용
위험: 다른 관계에서 쓰는 Child 삭제
해결: 완전 종속 Child에만 사용

문제: Page.map에서 Lazy Field 접근
위험: Pagination N+1
해결: Fetch Join / DTO Projection 검토
```

---

### [FAQ]

Q. Part07 검수에서 가장 먼저 확인할 것은 뭐야?
A. Service Transaction Boundary와 readOnly / write Transaction 구분을 먼저 확인한다.

Q. Cascade 검수에서 가장 위험한 것은 뭐야?
A. Cascade REMOVE 또는 CascadeType.ALL이 공유 Entity에 적용되는 것이다.

Q. orphanRemoval 검수에서 중요한 것은 뭐야?
A. Child 생명주기가 Parent에 완전히 종속되는지 확인하는 것이다.

Q. Pagination 검수에서 중요한 것은 뭐야?
A. Page / Slice 선택, Count Query 비용, Sort 안정성, N+1 가능성, Collection Fetch Join 여부다.

---

# 9. Common Mistakes

## 9.1 Transaction, Cascade, Pagination Common Mistakes

### [개념]

Transaction, Cascade, Pagination Common Mistakes는 JPA Service Transaction, 삭제 전파, Auditing, Page / Slice 조회에서 자주 발생하는 오류다.

---

### [핵심]

자주 발생하는 실수:

- Service 수정 Method에 `@Transactional` 없음
- 조회 / 수정 Transaction 구분 없음
- readOnly Transaction에서 Entity 수정
- Controller에 Transaction 적용
- Repository에 비즈니스 Transaction 흐름 분산
- Self Invocation으로 Transaction 누락
- 예외를 catch하고 삼켜 Rollback 방해
- CheckedException Rollback 기준 누락
- Transaction 안에서 긴 외부 API 호출
- CascadeType.ALL 남용
- ManyToOne에 Cascade REMOVE 적용
- 공유 Entity에 Cascade REMOVE 적용
- orphanRemoval을 관계 해제로 오해
- orphanRemoval을 공유 Child에 적용
- Soft Delete와 orphanRemoval 충돌
- Auditing 설정 누락
- Bulk Query에서 updatedAt 자동 갱신 기대
- 대량 목록에 List 사용
- Page / Slice 기준 없이 사용
- Pageable size 무제한 허용
- Pagination 정렬 기준 불안정
- Page.map에서 N+1 발생
- Collection Fetch Join과 Pagination 조합

---

### [실무]

Anti Pattern 예시:

```java
public void updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId).orElseThrow();
    post.update(request.title(), request.content());
}
```

개선:

```java
@Transactional
public void updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId).orElseThrow();
    post.update(request.title(), request.content());
}
```

Anti Pattern 예시:

```java
@ManyToOne(cascade = CascadeType.ALL)
@JoinColumn(name = "user_id")
private User user;
```

문제:

```text
Post 저장 / 삭제 작업이 User로 전파 가능
공유 Parent Entity에 위험
예상치 못한 User 삭제 가능
```

개선:

```java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "user_id", nullable = false)
private User user;
```

Anti Pattern 예시:

```java
@Transactional(readOnly = true)
public List<PostResponse> getAllPosts() {
    return postRepository.findAll().stream()
            .map(PostResponse::from)
            .toList();
}
```

개선:

```java
@Transactional(readOnly = true)
public Slice<PostResponse> getPosts(Pageable pageable) {
    return postRepository.findByDeletedFalse(pageable)
            .map(PostResponse::from);
}
```

Review 기준:

```text
Service
→ Transaction 확인

Cascade
→ 삭제 전파 위험 확인

orphanRemoval
→ 완전 종속 Child 확인

Auditing
→ 설정과 Bulk Query 영향 확인

Pagination
→ Page / Slice / Sort / N+1 확인
```

---

### [FAQ]

Q. Transaction에서 가장 흔한 실수는 뭐야?
A. 수정 Method에 `@Transactional`을 붙이지 않거나 readOnly에서 수정하는 것이다.

Q. Cascade에서 가장 흔한 실수는 뭐야?
A. CascadeType.ALL을 편의상 사용해 삭제 전파 위험을 만드는 것이다.

Q. orphanRemoval에서 가장 흔한 오해는 뭐야?
A. 단순 관계 해제로 생각하지만 실제 DELETE로 이어질 수 있다는 점을 놓치는 것이다.

Q. Pagination에서 가장 흔한 실수는 뭐야?
A. 대량 목록을 List로 전부 조회하거나 Page.map에서 N+1을 만드는 것이다.

---

# 10. Part07 Final Goal

## 10.1 Agent Output Goal

### [개념]

JPA Advanced Part07의 최종 목적은 Agent가 Transaction Boundary, Rollback, Cascade, orphanRemoval, Auditing, Pagination 기준을 통해 안전한 Service Layer와 Entity 생명주기 전파, 목록 조회 전략을 설계하도록 만드는 것이다.

Part07은 SQL Foundation의 Transaction, Constraint, Pagination, Backend Integration 기준과 JPA Service Transaction / Lifecycle / Pagination 전략을 연결한다.

---

### [핵심]

Agent가 수행해야 할 작업:

- Service Transaction Boundary 설정
- readOnly / write Transaction 구분
- Entity 변경 Transaction 범위 확인
- Rollback 대상 예외 판단
- Exception Handling과 Transaction 영향 검토
- Cascade 사용 필요성 판단
- CascadeType.ALL 남용 탐지
- Cascade REMOVE 위험 탐지
- orphanRemoval 적용 가능성 판단
- 삭제 전파와 관계 해제 구분
- Auditing Base Entity 설계
- Bulk Query Auditing 누락 검토
- Page / Slice 선택
- Pageable Sort / Size 제한 검토
- Pagination Count Query 비용 검토
- Pagination N+1 탐지
- Collection Fetch Join + Pagination Anti Pattern 탐지

---

### [실무]

Agent 작업 흐름:

```text
User Service Request
→ Identify Read / Write Operation
→ Apply Transaction Boundary
→ Choose readOnly or write Transaction
→ Check Entity Lifecycle Dependency
→ Decide Cascade / orphanRemoval
→ Apply Auditing if Needed
→ Choose Page / Slice
→ Review Pagination Query
→ Check N+1 and SQL Count
→ Return Safe Service Design
```

Troubleshooting 흐름:

```text
Transaction / Cascade / Pagination Problem
→ Service @Transactional 확인
→ Exception Handling 확인
→ Cascade REMOVE 범위 확인
→ orphanRemoval 삭제 조건 확인
→ Auditing 설정 확인
→ Page / Slice Query 확인
→ SQL 로그 확인
```

Part07 이후 연결:

```text
Part07 Transaction / Cascade / Auditing / Pagination
→ Part08 Backend Integration / Performance Review / Troubleshooting / Anti Pattern
```

---

### [FAQ]

Q. JPA Advanced Part07의 목적은 뭐야?
A. Agent가 Service Transaction, Cascade, orphanRemoval, Auditing, Pagination을 안전하게 설계하고 검수하도록 만드는 것이다.

Q. Part07에서 가장 중요한 기준은 뭐야?
A. Service Transaction Boundary, readOnly / write 구분, Cascade 삭제 전파 위험, orphanRemoval 삭제 조건, Pagination N+1 검토다.

Q. Part07은 SQL Foundation 어느 부분과 연결돼?
A. SQL Part04 Transaction / Constraint / Pagination과 SQL Part05 Backend Integration / Troubleshooting과 연결된다.

Q. Part07 다음에는 무엇을 다뤄?
A. Part08에서 Backend Integration, Performance Review, Troubleshooting, Common Mistakes, JPA Anti Pattern을 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. Transaction Boundary는 뭐야?
A. DB 작업이 하나의 논리적 작업 단위로 처리되는 범위다.

Q. JPA에서 Transaction Boundary가 중요한 이유는 뭐야?
A. Persistence Context, Dirty Checking, Flush, Rollback, Lazy Loading 동작 범위를 결정하기 때문이다.

Q. `@Transactional`은 어디에 두는 게 좋아?
A. 일반적으로 Service public method에 둔다.

Q. Controller에 `@Transactional`을 둬도 돼?
A. 가능은 하지만 HTTP Layer와 Persistence Layer 책임이 섞이므로 일반적으로 권장하지 않는다.

Q. Service Layer에 Transaction을 두는 이유는 뭐야?
A. 하나의 비즈니스 작업 단위 안에서 Repository 호출, Entity 변경, Flush, Rollback을 관리하기 위해서다.

Q. 조회 Method에도 Transaction이 필요해?
A. Lazy Loading, 일관된 조회, readOnly 최적화 의도를 위해 `@Transactional(readOnly = true)`를 사용할 수 있다.

Q. 수정 Method에 readOnly를 붙여도 돼?
A. 권장하지 않는다. 변경 작업은 일반 `@Transactional`을 사용해야 한다.

Q. readOnly Transaction은 뭐야?
A. 조회 전용 Transaction임을 명시하는 설정이다.

Q. readOnly를 붙이면 쓰기가 완전히 막혀?
A. DB와 Provider에 따라 다르므로 보안 장치처럼 의존하면 안 된다. 변경 의도를 차단하는 설계 신호로 사용한다.

Q. 조회 Method에는 readOnly를 붙이는 게 좋아?
A. 일반적으로 좋다. 조회 전용 의도를 명확히 하고 불필요한 변경 감지 부담을 줄일 수 있다.

Q. readOnly Method에서 Entity를 수정하면 어떻게 돼?
A. 변경 반영을 기대하지 않아야 하며 수정 Method는 일반 Transaction으로 분리해야 한다.

Q. Spring Transaction은 어떤 예외에서 Rollback돼?
A. 기본적으로 RuntimeException과 Error에서 Rollback된다.

Q. CheckedException은 Rollback돼?
A. 기본적으로 Rollback되지 않는다. 필요하면 `rollbackFor`를 명시해야 한다.

Q. 예외를 catch하면 Rollback돼?
A. 예외를 catch하고 다시 던지지 않으면 Rollback이 안 될 수 있다.

Q. Custom BusinessException은 어떻게 설계하는 게 좋아?
A. RuntimeException 기반으로 만들면 기본 Rollback 정책과 잘 맞는다.

Q. Service에서 예외를 catch해도 돼?
A. 가능하지만 실패를 정상 처리로 바꾸면 Transaction이 Commit될 수 있어 주의해야 한다.

Q. 예외는 어디서 API 응답으로 바꿔?
A. 일반적으로 GlobalExceptionHandler 또는 Controller Advice에서 처리한다.

Q. Cascade는 뭐야?
A. Parent Entity의 저장, 병합, 삭제 같은 영속성 작업을 Child Entity로 전파하는 기능이다.

Q. Cascade는 언제 써?
A. Child가 Parent 없이는 의미 없고 생명주기가 완전히 종속될 때 사용한다.

Q. Cascade는 연관관계 설정을 자동으로 해줘?
A. 아니다. 객체 참조는 직접 설정해야 하며 Cascade는 영속성 작업만 전파한다.

Q. CascadeType.ALL을 써도 돼?
A. 가능하지만 삭제 전파까지 포함하므로 매우 신중히 사용해야 한다.

Q. Cascade Persist는 뭐야?
A. Parent Entity 저장 시 신규 Child Entity 저장도 함께 전파하는 기능이다.

Q. Parent save만 하면 Child도 저장돼?
A. Cascade Persist가 설정되어 있고 관계가 올바르게 설정되어 있으면 Child 저장이 전파될 수 있다.

Q. Cascade Persist가 FK 설정도 해줘?
A. 아니다. Owning Side의 연관관계 Field는 직접 설정해야 한다.

Q. Cascade Remove는 뭐야?
A. Parent Entity 삭제 시 Child Entity 삭제도 전파하는 기능이다.

Q. ManyToOne에 Cascade REMOVE를 써도 돼?
A. 매우 위험하다. Child 삭제가 Parent 삭제로 전파될 수 있으므로 일반적으로 사용하지 않는다.

Q. CascadeType.ALL은 왜 위험해?
A. 저장뿐 아니라 삭제 전파까지 포함하므로 예상치 못한 데이터 삭제가 발생할 수 있다.

Q. DB ON DELETE CASCADE와 JPA Cascade는 같아?
A. 아니다. DB Constraint 동작과 JPA 영속성 전파는 별도 개념이다.

Q. orphanRemoval은 뭐야?
A. Parent Collection에서 Child가 제거되면 해당 Child Entity를 삭제하는 기능이다.

Q. orphanRemoval은 언제 써?
A. Child가 Parent 없이는 의미 없고 Collection에서 제거되면 삭제되어야 할 때 사용한다.

Q. Collection에서 remove하면 DB Row도 삭제돼?
A. orphanRemoval이 true이면 Flush 시 DELETE SQL이 실행될 수 있다.

Q. orphanRemoval은 관계 해제야 삭제야?
A. 삭제에 가깝다. 단순 FK null 처리와 다르게 Child Row 제거로 이어질 수 있다.

Q. orphanRemoval과 Cascade REMOVE는 같은 거야?
A. 아니다. orphanRemoval은 Collection에서 제거된 Child 삭제이고 Cascade REMOVE는 Parent 삭제 시 Child 삭제 전파다.

Q. 둘 다 같이 써도 돼?
A. 가능하지만 Child 생명주기가 완전히 종속된 경우에만 사용하고 삭제 범위를 테스트해야 한다.

Q. 공유 Child에 orphanRemoval을 써도 돼?
A. 안 된다. 다른 Parent에서도 참조할 수 있는 Child가 삭제될 위험이 있다.

Q. Soft Delete에서는 orphanRemoval을 써도 돼?
A. 주의해야 한다. orphanRemoval은 실제 DELETE로 이어질 수 있어 Soft Delete 정책과 충돌할 수 있다.

Q. Auditing은 뭐야?
A. Entity의 생성일, 수정일, 생성자, 수정자 같은 메타데이터를 자동으로 관리하는 기능이다.

Q. createdAt과 updatedAt은 어떻게 관리해?
A. Spring Data JPA Auditing의 `@CreatedDate`, `@LastModifiedDate`를 사용할 수 있다.

Q. Auditing을 쓰려면 무엇이 필요해?
A. `@EnableJpaAuditing`, `@EntityListeners(AuditingEntityListener.class)`, Auditing Annotation이 필요하다.

Q. Bulk Update에서도 updatedAt이 자동 변경돼?
A. 기대하지 않는 것이 좋다. Bulk Query는 Auditing을 우회할 수 있으므로 직접 갱신을 검토해야 한다.

Q. BaseTimeEntity는 뭐야?
A. 여러 Entity에서 공통으로 사용하는 createdAt, updatedAt Field를 모아둔 상위 Class다.

Q. `@MappedSuperclass`는 뭐야?
A. 상위 Class의 Mapping 정보를 하위 Entity에 상속하기 위한 JPA Annotation이다.

Q. 모든 Entity가 BaseTimeEntity를 상속해야 해?
A. 생성일 / 수정일 관리가 필요한 Entity에 적용하면 된다. 모든 Entity에 무조건 적용할 필요는 없다.

Q. Page와 Slice 차이는 뭐야?
A. Page는 전체 Count와 전체 페이지 수를 제공하고 Slice는 다음 데이터 존재 여부 중심이다.

Q. 무한 스크롤에는 뭐가 좋아?
A. 전체 Count가 필요 없으므로 Slice가 적합한 경우가 많다.

Q. Page는 왜 느릴 수 있어?
A. 전체 Count를 구하기 위한 Count Query가 추가로 실행될 수 있기 때문이다.

Q. Page나 Slice를 그대로 응답해도 돼?
A. 가능하지만 API 응답 구조를 위해 DTO로 변환하거나 별도 Page Response로 감싸는 것이 좋다.

Q. Pageable은 뭐야?
A. 페이지 번호, 페이지 크기, 정렬 정보를 Repository Query에 전달하는 객체다.

Q. Pageable sort는 Column 이름 기준이야?
A. 일반 JPA Query에서는 Entity Field 이름 기준이다.

Q. page 번호는 0부터 시작해?
A. Spring Data Pageable은 기본적으로 0-based page index를 사용한다.

Q. Pageable size를 제한해야 해?
A. 그렇다. 너무 큰 size는 대량 조회와 성능 문제를 만들 수 있다.

Q. Pagination 성능에서 가장 먼저 볼 것은 뭐야?
A. Count Query 비용, 정렬 기준, N+1 여부, Collection Fetch Join 여부를 확인한다.

Q. Offset Pagination이 느린 이유는 뭐야?
A. 뒤 페이지로 갈수록 DB가 건너뛰어야 하는 Row가 많아질 수 있기 때문이다.

Q. Keyset Pagination은 언제 검토해?
A. 대량 데이터에서 무한 스크롤이나 다음 페이지 조회 성능이 중요할 때 검토한다.

Q. Pagination에서도 N+1이 생겨?
A. 그렇다. Page.map이나 DTO 변환 중 Lazy Association을 접근하면 발생할 수 있다.

Q. Pagination 조회에도 Transaction을 붙여야 해?
A. readOnly Transaction을 붙이면 조회 의도를 명확히 하고 DTO 변환 중 Lazy Loading 범위를 통제할 수 있다.

Q. Page.map은 Transaction 안에서 하면 안전해?
A. LazyInitializationException은 줄일 수 있지만 N+1 문제는 여전히 발생할 수 있어 Query 수를 확인해야 한다.

Q. Pagination 목록에는 Projection이 좋아?
A. 읽기 전용 목록이고 필요한 Field가 명확하면 Projection이 적합한 경우가 많다.

Q. Part07 검수에서 가장 먼저 확인할 것은 뭐야?
A. Service Transaction Boundary와 readOnly / write Transaction 구분을 먼저 확인한다.

Q. Cascade 검수에서 가장 위험한 것은 뭐야?
A. Cascade REMOVE 또는 CascadeType.ALL이 공유 Entity에 적용되는 것이다.

Q. orphanRemoval 검수에서 중요한 것은 뭐야?
A. Child 생명주기가 Parent에 완전히 종속되는지 확인하는 것이다.

Q. Pagination 검수에서 중요한 것은 뭐야?
A. Page / Slice 선택, Count Query 비용, Sort 안정성, N+1 가능성, Collection Fetch Join 여부다.

Q. Transaction에서 가장 흔한 실수는 뭐야?
A. 수정 Method에 `@Transactional`을 붙이지 않거나 readOnly에서 수정하는 것이다.

Q. Cascade에서 가장 흔한 실수는 뭐야?
A. CascadeType.ALL을 편의상 사용해 삭제 전파 위험을 만드는 것이다.

Q. orphanRemoval에서 가장 흔한 오해는 뭐야?
A. 단순 관계 해제로 생각하지만 실제 DELETE로 이어질 수 있다는 점을 놓치는 것이다.

Q. Pagination에서 가장 흔한 실수는 뭐야?
A. 대량 목록을 List로 전부 조회하거나 Page.map에서 N+1을 만드는 것이다.

Q. JPA Part07에서 가장 중요한 기준은 뭐야?
A. Service Transaction Boundary, readOnly / write 구분, Cascade 삭제 전파 위험, orphanRemoval 삭제 조건, Pagination N+1 검토다.

Q. JPA Part07 다음에는 무엇을 다뤄?
A. Part08에서 Backend Integration, Performance Review, Troubleshooting, Common Mistakes, JPA Anti Pattern을 다룬다.
