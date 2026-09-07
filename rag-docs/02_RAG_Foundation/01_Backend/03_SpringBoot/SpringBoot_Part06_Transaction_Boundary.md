# Spring Boot Part06 - Transaction Boundary

---

# 1. Transaction Boundary

## 1.1 Transaction Boundary 개념

### [개념]

Transaction Boundary는 하나의 비즈니스 작업을 원자적으로 처리하는 범위다.

Spring Boot에서는 일반적으로 Service Layer의 public method에 `@Transactional`을 적용해 Transaction Boundary를 설정한다.

Transaction의 목적:

- 여러 DB 작업을 하나의 작업으로 묶음
- 작업 중 실패하면 rollback 처리
- 작업이 성공하면 commit 처리
- Entity 변경 감지 Dirty Checking 적용
- Lazy Loading 조회 범위 관리
- Use Case 단위 데이터 일관성 보장

기본 흐름:

```text
Client Request
→ Controller
→ Service Method Start
→ Transaction Begin
→ Repository
→ Entity 조회 / 변경
→ Service Method End
→ Transaction Commit
→ Response
```

실패 흐름:

```text
Service Method Start
→ Transaction Begin
→ Entity 변경
→ Exception 발생
→ Transaction Rollback
→ GlobalExceptionHandler
→ Error Response
```

---

### [핵심]

Transaction Boundary 핵심 기준:

- Service public method 기준
- Use Case 단위 기준
- 쓰기 작업에는 `@Transactional`
- 조회 작업에는 `@Transactional(readOnly = true)` 고려
- Controller에는 Transaction 적용 지양
- Repository에는 전체 Use Case Transaction 경계 부여 지양
- 외부 API 호출을 긴 Transaction 안에 포함하지 않도록 주의
- Transaction 범위는 짧고 명확하게 유지

Transaction이 필요한 경우:

- Entity 저장
- Entity 수정
- Entity 삭제
- 여러 Repository 호출 조합
- 여러 Entity 상태 변경
- 실패 시 rollback 필요
- Dirty Checking 필요
- Lazy Loading 조회 범위 필요
- 비즈니스 Use Case 단위 일관성 필요

---

### [실무]

쓰기 Service 예:

```java
@Service
@RequiredArgsConstructor
public class OrderService {

    private final OrderRepository orderRepository;
    private final ProductRepository productRepository;

    @Transactional
    public OrderResponse createOrder(OrderCreateRequest request) {
        Product product = productRepository.findById(request.productId())
                .orElseThrow(() -> new BusinessException("PRODUCT_NOT_FOUND", "상품을 찾을 수 없습니다."));

        if (!product.hasStock(request.quantity())) {
            throw new BusinessException("OUT_OF_STOCK", "재고가 부족합니다.");
        }

        product.decreaseStock(request.quantity());

        Order order = Order.create(product, request.quantity());
        Order savedOrder = orderRepository.save(order);

        return OrderResponse.from(savedOrder);
    }
}
```

이 Transaction Boundary에 포함되는 작업:

```text
상품 조회
→ 재고 검증
→ 상품 재고 감소
→ 주문 생성
→ 주문 저장
→ commit
```

중간에 예외가 발생하면:

```text
재고 감소 취소
주문 저장 취소
rollback
```

---

### [FAQ]

Q. Transaction Boundary는 뭐야?

A.
하나의 비즈니스 작업을 모두 성공하거나 모두 실패하도록 묶는 범위다. Spring Boot에서는 보통 Service public method에 설정한다.

Q. @Transactional은 어디에 붙여?

A.
대부분 Service Layer의 public method에 붙인다. Use Case 단위로 Transaction Boundary를 잡기 좋기 때문이다.

Q. Controller에 @Transactional을 붙이면 안 돼?

A.
권장하지 않는다. HTTP 요청 처리 책임과 비즈니스 Transaction 책임이 섞이기 때문이다.

---

# 2. @Transactional 기본 규칙

## 2.1 @Transactional 적용 위치

### [개념]

`@Transactional`은 Spring이 Transaction Proxy를 통해 method 실행 전후로 Transaction을 시작하고 종료하도록 만드는 Annotation이다.

Spring Boot에서는 Service Layer가 Transaction Boundary의 대표 위치다.

---

### [핵심]

권장 위치:

- Service public method
- Use Case 단위 method
- Command 작업 method
- Entity 변경 method
- 여러 Repository 조합 method

비권장 위치:

- Controller method
- Repository method에 전체 Use Case 경계 부여
- private method
- 단순 util method
- Entity class
- DTO class

---

### [실무]

권장 예:

```java
@Service
@RequiredArgsConstructor
public class PostService {

    private final PostRepository postRepository;

    @Transactional
    public PostResponse updatePost(Long postId, PostUpdateRequest request) {
        Post post = postRepository.findById(postId)
                .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

        post.update(request.title(), request.content());

        return PostResponse.from(post);
    }
}
```

비권장 예:

```java
@RestController
@RequiredArgsConstructor
public class PostController {

    private final PostRepository postRepository;

    @Transactional
    @PatchMapping("/posts/{postId}")
    public PostResponse updatePost(
            @PathVariable Long postId,
            @RequestBody PostUpdateRequest request
    ) {
        Post post = postRepository.findById(postId).orElseThrow();
        post.update(request.title(), request.content());

        return PostResponse.from(post);
    }
}
```

문제:

- Controller가 Repository 직접 호출
- Controller가 Business Logic 처리
- HTTP Layer와 Transaction Boundary 혼합
- 테스트와 유지보수 어려움

---

### [Best Practice]

`@Transactional` 적용 Best Practice:

- Service public method에 적용
- method 하나가 하나의 Use Case를 표현
- 쓰기 작업과 조회 작업 구분
- Transaction 범위 안에서 Entity 조회와 변경 처리
- Transaction 안에서 오래 걸리는 외부 API 호출 최소화
- Transaction 관련 문제는 Proxy 동작 기준으로 검토

---

### [FAQ]

Q. @Transactional은 class에 붙여도 돼?

A.
가능하다. 다만 모든 method에 동일한 Transaction 설정이 적용되므로 쓰기 / 읽기 설정을 구분하기 어렵다. 실무에서는 method 단위로 명확히 지정하는 방식이 자주 사용된다.

Q. private method에 @Transactional을 붙이면 돼?

A.
권장하지 않는다. Spring AOP Proxy 기반에서는 private method에 기대한 Transaction이 적용되지 않을 수 있다.

Q. Repository method에는 @Transactional이 전혀 없어야 해?

A.
Spring Data JPA 내부적으로 기본 Transaction이 적용되는 경우가 있지만, 비즈니스 Use Case의 Transaction Boundary는 Service에서 잡는 것이 좋다.

---

## 2.2 Transaction Begin / Commit / Rollback 흐름

### [개념]

Transaction은 method 시작 시 begin되고 method가 정상 종료되면 commit된다.

RuntimeException 또는 Error가 발생하면 기본적으로 rollback된다.

---

### [Flow]

정상 처리:

```text
Service Method 호출
→ Transaction Begin
→ Repository 조회
→ Entity 변경
→ Service Method 정상 종료
→ Transaction Commit
→ DB 반영
```

예외 처리:

```text
Service Method 호출
→ Transaction Begin
→ Repository 조회
→ Entity 변경
→ RuntimeException 발생
→ Transaction Rollback
→ DB 변경 취소
→ Exception Handler 처리
```

---

### [핵심]

Commit 되는 경우:

- method 정상 종료
- rollback 대상 예외 없음
- Transaction Manager가 commit 수행

Rollback 되는 경우:

- RuntimeException 발생
- Error 발생
- rollbackFor로 지정한 checked exception 발생
- Transaction Manager가 rollback 수행

주의:

- 예외를 catch 후 삼키면 rollback되지 않을 수 있음
- checked exception은 기본 rollback 대상이 아닐 수 있음
- Transaction 밖에서 발생한 예외는 해당 Transaction rollback과 무관할 수 있음

---

### [실무]

나쁜 예:

```java
@Transactional
public void updatePost(Long postId, PostUpdateRequest request) {
    try {
        Post post = postRepository.findById(postId).orElseThrow();
        post.update(request.title(), request.content());
    } catch (Exception e) {
        log.error("게시글 수정 실패", e);
    }
}
```

문제:

- 예외를 catch하고 다시 던지지 않음
- method가 정상 종료된 것으로 판단될 수 있음
- rollback이 되지 않을 수 있음
- 실패 응답이 명확하지 않음

좋은 예:

```java
@Transactional
public void updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    post.update(request.title(), request.content());
}
```

외부에서 처리:

```text
BusinessException 발생
→ Transaction Rollback
→ GlobalExceptionHandler
→ Error Response
```

---

### [FAQ]

Q. @Transactional method 안에서 예외를 catch하면 rollback돼?

A.
예외를 catch한 뒤 다시 던지지 않으면 Spring은 정상 종료로 볼 수 있어 rollback되지 않을 수 있다.

Q. RuntimeException은 rollback돼?

A.
기본적으로 RuntimeException과 Error는 rollback 대상이다.

Q. Checked Exception은 rollback돼?

A.
기본 rollback 대상이 아닐 수 있다. 필요하면 rollbackFor 설정을 검토한다.

---

# 3. Read Transaction

## 3.1 @Transactional(readOnly = true)

### [개념]

`@Transactional(readOnly = true)`는 조회 전용 Transaction을 의미한다.

읽기 작업에서 변경 작업이 필요 없다는 의도를 표현하고, JPA 구현체나 DB에 조회 최적화 힌트를 줄 수 있다.

---

### [핵심]

readOnly 사용 대상:

- 단건 조회
- 목록 조회
- 페이지 조회
- Slice 조회
- 검색 조회
- DTO 조회
- Lazy Loading이 필요한 조회

readOnly 특징:

- 조회 의도 명확화
- 변경 작업 지양
- Dirty Checking 부담 완화 가능
- 읽기 중심 method 구분
- Service method 의미 명확화

주의:

- readOnly가 모든 쓰기를 물리적으로 막는 보안 장치는 아님
- readOnly method 안에서 Entity 변경 지양
- 조회 도중 필요한 Lazy Loading 범위 확보 가능
- 복잡한 조회 성능 문제는 JPA / QueryDSL 문서 기준 참고

---

### [실무]

단건 조회:

```java
@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    return PostResponse.from(post);
}
```

목록 조회:

```java
@Transactional(readOnly = true)
public List<PostResponse> getPosts() {
    return postRepository.findAll().stream()
            .map(PostResponse::from)
            .toList();
}
```

Slice 조회:

```java
@Transactional(readOnly = true)
public Slice<PostResponse> getPosts(Pageable pageable) {
    return postRepository.findAll(pageable)
            .map(PostResponse::from);
}
```

권장:

- 조회 Service method에는 `readOnly = true` 고려
- DTO 변환은 Transaction 안에서 수행
- Lazy Loading 필요한 필드는 Transaction 안에서 접근
- 조회 method에서 Entity 상태 변경 금지

---

### [FAQ]

Q. 조회 method에도 @Transactional이 필요해?

A.
JPA Lazy Loading이나 일관된 읽기 컨텍스트가 필요하면 `@Transactional(readOnly = true)`를 적용하는 것이 좋다.

Q. readOnly = true면 DB 쓰기가 절대 안 돼?

A.
그렇게 이해하면 위험하다. readOnly는 조회 의도와 최적화 힌트 성격이며, 쓰기 방지 보안 장치로 의존하면 안 된다.

Q. DTO 변환은 Transaction 안에서 해야 해?

A.
Lazy Loading이 필요한 필드가 있다면 Transaction 안에서 DTO 변환을 완료하는 것이 안전하다.

---

## 3.2 Read Transaction과 Lazy Loading

### [개념]

Lazy Loading은 연관 Entity를 실제 접근 시점에 조회하는 방식이다.

Lazy Loading은 영속성 컨텍스트와 Transaction 범위 밖에서 접근하면 문제가 발생할 수 있다.

---

### [핵심]

Lazy Loading 문제 발생 흐름:

```text
Service에서 Entity 조회
→ Transaction 종료
→ Controller에서 Entity 연관 필드 접근
→ Lazy Loading 실패 가능
```

안전한 흐름:

```text
Service Transaction 시작
→ Entity 조회
→ 필요한 연관 데이터 접근
→ Response DTO 변환
→ Transaction 종료
→ Controller는 DTO만 반환
```

주의:

- Entity를 Controller로 반환하지 않음
- DTO 변환을 Service Transaction 안에서 수행
- Lazy Loading 문제는 DTO 경계로 줄임
- N+1 문제는 JPA Advanced 기준으로 별도 검토

---

### [실무]

비권장:

```java
@Transactional(readOnly = true)
public Post getPost(Long postId) {
    return postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));
}
```

```java
@GetMapping("/posts/{postId}")
public ApiResponse<Post> getPost(@PathVariable Long postId) {
    return ApiResponse.success(postService.getPost(postId));
}
```

문제:

- Entity 직접 반환
- Lazy Loading 문제 가능
- 순환 참조 가능
- 민감정보 노출 가능

권장:

```java
@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    return PostResponse.from(post);
}
```

---

### [주의]

Lazy Loading 관련 주의:

- Transaction 밖 Entity 연관 필드 접근 지양
- Controller에서 Entity를 JSON으로 변환하지 않음
- DTO 변환 시 필요한 데이터만 포함
- Open Session In View에 의존한 설계 지양
- 조회 성능 문제는 fetch join, EntityGraph, QueryDSL 등 별도 전략 검토

---

### [FAQ]

Q. LazyInitializationException은 왜 발생해?

A.
Transaction 또는 영속성 컨텍스트가 종료된 뒤 Lazy 연관 필드에 접근하면 발생할 수 있다.

Q. Lazy Loading 문제를 Service에서 어떻게 줄여?

A.
Service의 readOnly Transaction 안에서 필요한 데이터를 조회하고 Response DTO로 변환해 Controller에는 DTO만 반환한다.

Q. Entity를 그대로 반환하면 왜 위험해?

A.
Lazy Loading, 순환 참조, 민감정보 노출, API 응답 구조 불안정 문제가 생길 수 있다.

---

# 4. Write Transaction

## 4.1 Create Transaction

### [개념]

Create Transaction은 새로운 Entity를 생성하고 DB에 저장하는 Transaction이다.

회원가입, 게시글 작성, 댓글 등록, 주문 생성 같은 기능이 해당된다.

---

### [핵심]

Create Transaction 흐름:

```text
Request DTO
→ Business Validation
→ Entity 생성
→ Repository save
→ Response DTO
→ Commit
```

주요 처리:

- 중복 검사
- 존재 여부 검사
- Entity 생성
- 연관 Entity 연결
- Repository 저장
- CustomException 발생
- Response DTO 반환

---

### [실무]

회원가입 예:

```java
@Transactional
public UserResponse signUp(SignUpRequest request) {
    if (userRepository.existsByEmail(request.email())) {
        throw new BusinessException("DUPLICATED_EMAIL", "이미 사용 중인 이메일입니다.");
    }

    User user = User.create(
            request.email(),
            request.password(),
            request.nickname()
    );

    User savedUser = userRepository.save(user);

    return UserResponse.from(savedUser);
}
```

댓글 등록 예:

```java
@Transactional
public CommentResponse createComment(Long postId, Long userId, CommentCreateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    Comment comment = Comment.create(post, user, request.content());

    return CommentResponse.from(commentRepository.save(comment));
}
```

권장:

- 생성 전 Business Validation 수행
- 연관 Entity는 Service에서 조회
- Entity 생성은 static factory method 사용 가능
- 저장 후 Response DTO 반환
- 중간 실패 시 전체 rollback

---

### [FAQ]

Q. Entity 생성은 Service에서 해도 돼?

A.
Service에서 생성 흐름을 조율하고 Entity의 static factory method를 호출하는 방식이 좋다.

Q. save 후 반환은 Entity로 해도 돼?

A.
Controller 응답으로 Entity를 직접 반환하는 것은 지양한다. Response DTO로 변환해 반환하는 것이 좋다.

---

## 4.2 Update Transaction

### [개념]

Update Transaction은 기존 Entity를 조회한 뒤 상태를 변경하는 Transaction이다.

JPA에서는 영속 상태 Entity의 값을 변경하면 Transaction commit 시 Dirty Checking으로 DB에 반영될 수 있다.

---

### [핵심]

Update Transaction 흐름:

```text
Entity 조회
→ 존재 여부 확인
→ 권한 / 상태 검사
→ Entity method 호출
→ Dirty Checking
→ Commit
```

주요 처리:

- 수정 대상 조회
- 작성자 / 권한 확인
- 삭제 여부 확인
- 상태 전환 가능 여부 확인
- Entity 상태 변경
- Response DTO 반환

---

### [실무]

게시글 수정 예:

```java
@Transactional
public PostResponse updatePost(Long postId, Long userId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    if (!post.isWriter(userId)) {
        throw new BusinessException("NO_PERMISSION", "게시글 수정 권한이 없습니다.");
    }

    if (post.isDeleted()) {
        throw new BusinessException("POST_DELETED", "삭제된 게시글은 수정할 수 없습니다.");
    }

    post.update(request.title(), request.content());

    return PostResponse.from(post);
}
```

알림 읽음 처리 예:

```java
@Transactional
public NotificationResponse readNotification(Long notificationId, Long userId) {
    Notification notification = notificationRepository.findById(notificationId)
            .orElseThrow(() -> new BusinessException("NOTIFICATION_NOT_FOUND", "알림을 찾을 수 없습니다."));

    if (!notification.isOwner(userId)) {
        throw new BusinessException("NO_PERMISSION", "알림 접근 권한이 없습니다.");
    }

    notification.markAsRead();

    return NotificationResponse.from(notification);
}
```

권장:

- setter 남용 지양
- 의미 있는 Entity method 사용
- 수정 전 권한 / 상태 검사
- Transaction 안에서 상태 변경
- 필요 없는 save 반복 지양
- Dirty Checking 동작 범위 이해

---

### [주의]

Update Transaction Anti Pattern:

```java
public PostResponse updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId).orElseThrow();
    post.setTitle(request.title());
    post.setContent(request.content());
    return PostResponse.from(post);
}
```

문제:

- `@Transactional` 없음
- 조회 실패 예외 불명확
- setter 남용
- 권한 검사 없음
- Dirty Checking 보장 불명확

개선:

```java
@Transactional
public PostResponse updatePost(Long postId, Long userId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    if (!post.isWriter(userId)) {
        throw new BusinessException("NO_PERMISSION", "게시글 수정 권한이 없습니다.");
    }

    post.update(request.title(), request.content());

    return PostResponse.from(post);
}
```

---

### [FAQ]

Q. Entity 수정 후 save를 꼭 호출해야 해?

A.
Transaction 안에서 조회한 영속 상태 Entity라면 Dirty Checking으로 commit 시 반영될 수 있다. 신규 Entity 저장은 save가 필요하다.

Q. Update 작업에 @Transactional이 없으면 어떻게 돼?

A.
Dirty Checking이 기대대로 동작하지 않거나 변경 반영이 불명확해질 수 있다.

Q. setter 대신 Entity method를 쓰는 이유는?

A.
상태 변경 의도를 명확히 하고 변경 규칙을 Entity 내부에 모을 수 있기 때문이다.

---

## 4.3 Delete Transaction

### [개념]

Delete Transaction은 Entity를 삭제하거나 삭제 상태로 변경하는 Transaction이다.

실무에서는 물리 삭제와 논리 삭제를 구분한다.

---

### [핵심]

삭제 방식:

- Physical Delete
- Soft Delete
- Status Change
- deleted flag
- deletedAt timestamp

Delete Transaction 흐름:

```text
Entity 조회
→ 권한 / 상태 검사
→ 삭제 처리
→ Commit
```

---

### [실무]

물리 삭제 예:

```java
@Transactional
public void deleteComment(Long commentId, Long userId) {
    Comment comment = commentRepository.findById(commentId)
            .orElseThrow(() -> new BusinessException("COMMENT_NOT_FOUND", "댓글을 찾을 수 없습니다."));

    if (!comment.isWriter(userId)) {
        throw new BusinessException("NO_PERMISSION", "댓글 삭제 권한이 없습니다.");
    }

    commentRepository.delete(comment);
}
```

논리 삭제 예:

```java
@Transactional
public void deletePost(Long postId, Long userId) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    if (!post.isWriter(userId)) {
        throw new BusinessException("NO_PERMISSION", "게시글 삭제 권한이 없습니다.");
    }

    post.markDeleted();
}
```

권장:

- 삭제 전 권한 검사
- 이미 삭제된 데이터 처리 기준 정의
- 연관 데이터 영향 확인
- 실무에서는 Soft Delete 고려
- 삭제 응답 형식은 API Design 규칙과 통일

---

### [주의]

삭제 처리 주의:

- 물리 삭제는 복구 어려움
- 연관 Entity FK 제약 확인 필요
- Cascade 삭제 범위 주의
- Soft Delete는 조회 조건에 deleted false 반영 필요
- 삭제된 데이터 접근 시 ErrorCode 명확화

---

### [FAQ]

Q. 삭제는 physical delete가 좋아 soft delete가 좋아?

A.
데이터 복구, 감사 로그, 사용자 기록이 필요하면 soft delete를 고려한다. 단순 임시 데이터는 physical delete도 가능하다.

Q. Soft Delete를 쓰면 뭘 주의해야 해?

A.
조회 Query에서 삭제된 데이터를 제외하는 기준을 일관되게 적용해야 한다.

---

# 5. Rollback Rules

## 5.1 Rollback 기본 규칙

### [개념]

Rollback은 Transaction 중 발생한 변경 사항을 취소하는 처리다.

Spring Transaction은 기본적으로 RuntimeException과 Error 발생 시 rollback한다.

---

### [핵심]

기본 rollback 대상:

- RuntimeException
- Error

기본 rollback 대상이 아닐 수 있는 것:

- Checked Exception
- catch 후 다시 던지지 않은 Exception
- Transaction 밖에서 발생한 Exception

Rollback이 필요한 상황:

- 비즈니스 조건 위반
- Entity 저장 실패
- 여러 작업 중 일부 실패
- 외부 연동 결과에 따라 DB 변경 취소 필요
- 데이터 일관성 깨짐 방지

---

### [실무]

RuntimeException 기반 Custom Exception:

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

Service 예:

```java
@Transactional
public PaymentResponse approvePayment(PaymentRequest request) {
    Order order = orderRepository.findById(request.orderId())
            .orElseThrow(() -> new BusinessException("ORDER_NOT_FOUND", "주문을 찾을 수 없습니다."));

    if (!order.isPayable()) {
        throw new BusinessException("ORDER_NOT_PAYABLE", "결제할 수 없는 주문입니다.");
    }

    order.markPaid();

    return PaymentResponse.from(order);
}
```

`BusinessException`이 RuntimeException을 상속하면 기본 rollback 대상이 된다.

---

### [주의]

Rollback 실패 또는 오해 상황:

```text
예외를 catch하고 삼킴
→ method 정상 종료
→ commit 가능
```

```text
checked exception 발생
→ 기본 rollback 대상이 아닐 수 있음
→ rollbackFor 필요 가능
```

```text
self-invocation
→ Transaction Proxy 미적용 가능
→ Transaction 동작 안 할 수 있음
```

```text
Transaction 밖 Entity 변경
→ Dirty Checking 미적용 가능
```

---

### [FAQ]

Q. CustomException은 RuntimeException을 상속하는 게 좋아?

A.
비즈니스 예외로 rollback이 필요한 경우 RuntimeException을 상속하면 Spring 기본 rollback 규칙과 잘 맞는다.

Q. 예외를 catch하면 rollback 안 돼?

A.
catch 후 다시 던지지 않으면 Spring이 정상 종료로 판단할 수 있어 rollback되지 않을 수 있다.

Q. rollbackFor는 언제 써?

A.
Checked Exception에서도 rollback이 필요할 때 `rollbackFor` 설정을 검토한다.

---

## 5.2 Checked Exception Rollback

### [개념]

Checked Exception은 컴파일 시점에 처리 강제를 받는 예외다.

Spring Transaction은 기본적으로 Checked Exception에 대해 rollback하지 않을 수 있다.

---

### [핵심]

Checked Exception 예:

- IOException
- SQLException
- 직접 만든 checked exception

Rollback 설정:

```java
@Transactional(rollbackFor = IOException.class)
```

사용 기준:

- Checked Exception 발생 시 DB 변경을 취소해야 하는 경우
- 파일 처리 / 외부 연동 실패와 DB 작업이 함께 있는 경우
- 업무상 전체 작업 실패로 봐야 하는 경우

---

### [실무]

예:

```java
@Transactional(rollbackFor = IOException.class)
public FileUploadResponse uploadFile(FileUploadRequest request) throws IOException {
    FileMetadata metadata = FileMetadata.create(request.originalFilename());
    fileMetadataRepository.save(metadata);

    fileStorageClient.upload(request.file());

    return FileUploadResponse.from(metadata);
}
```

주의:

- DB 저장 후 파일 업로드 실패 시 DB 저장도 취소해야 한다면 rollbackFor 검토
- 하지만 DB Transaction과 파일 시스템 Transaction은 완전히 동일하지 않음
- 외부 시스템과 DB 일관성은 별도 보상 처리 전략이 필요할 수 있음

---

### [Best Practice]

Checked Exception 처리 기준:

- 가능하면 비즈니스 예외는 RuntimeException 기반으로 통일
- checked exception을 무조건 RuntimeException으로 감싸기 전에 의미 검토
- rollbackFor 사용 시 Transaction 범위와 외부 리소스 영향 검토
- 외부 시스템 작업은 보상 트랜잭션 또는 상태 관리 검토
- 단순 예제보다 실제 실패 시나리오 기준으로 설계

---

### [FAQ]

Q. Checked Exception은 왜 rollback이 안 될 수 있어?

A.
Spring Transaction 기본 rollback 규칙이 RuntimeException과 Error 중심이기 때문이다.

Q. IOException 발생 시 rollback하려면 어떻게 해?

A.
`@Transactional(rollbackFor = IOException.class)`처럼 rollbackFor를 지정할 수 있다.

Q. 외부 API 실패도 rollback하면 끝이야?

A.
DB 변경은 rollback할 수 있지만 외부 시스템에서 이미 수행된 작업은 별도 취소 API나 보상 처리가 필요할 수 있다.

---

# 6. Transaction Proxy

## 6.1 Spring AOP Proxy와 Transaction

### [개념]

Spring의 `@Transactional`은 AOP Proxy 기반으로 동작한다.

외부에서 Bean의 public method를 호출할 때 Proxy가 Transaction을 시작하고 method 종료 후 commit 또는 rollback을 수행한다.

---

### [Flow]

Proxy 기반 흐름:

```text
Controller
→ Transaction Proxy
→ Service Method
→ Repository
→ Service Method 종료
→ Proxy가 commit / rollback
```

Self-invocation 문제 흐름:

```text
Service 내부 method
→ 같은 클래스의 @Transactional method 직접 호출
→ Proxy를 거치지 않음
→ Transaction 적용 안 될 수 있음
```

---

### [핵심]

Proxy 기반 주의점:

- public method 중심으로 적용
- 외부 Bean 호출 시 적용
- private method에는 기대대로 적용되지 않을 수 있음
- 같은 클래스 내부 호출 self-invocation 주의
- final class / final method 환경에 따라 Proxy 제약 가능
- Transaction 동작 문제는 Proxy 통과 여부 확인

---

### [실무]

문제 예:

```java
@Service
@RequiredArgsConstructor
public class PostService {

    public void updatePostStatus(Long postId) {
        changeStatus(postId);
    }

    @Transactional
    public void changeStatus(Long postId) {
        Post post = postRepository.findById(postId).orElseThrow();
        post.changeStatus();
    }
}
```

문제:

- 같은 클래스 내부에서 `changeStatus()` 호출
- Transaction Proxy를 거치지 않을 수 있음
- `@Transactional`이 기대대로 동작하지 않을 수 있음

개선 예:

```java
@Service
@RequiredArgsConstructor
public class PostService {

    private final PostStatusService postStatusService;

    public void updatePostStatus(Long postId) {
        postStatusService.changeStatus(postId);
    }
}
```

```java
@Service
@RequiredArgsConstructor
public class PostStatusService {

    private final PostRepository postRepository;

    @Transactional
    public void changeStatus(Long postId) {
        Post post = postRepository.findById(postId).orElseThrow();
        post.changeStatus();
    }
}
```

---

### [FAQ]

Q. self-invocation이 뭐야?

A.
같은 클래스 안에서 자신의 다른 method를 직접 호출하는 상황이다. 이 경우 Proxy를 거치지 않아 `@Transactional`이 적용되지 않을 수 있다.

Q. private method에 @Transactional을 붙이면 왜 안 좋아?

A.
Spring AOP Proxy가 private method 호출을 가로채기 어렵기 때문에 기대한 Transaction이 적용되지 않을 수 있다.

Q. Transaction이 안 먹는 것 같으면 뭘 확인해?

A.
method가 public인지, 외부 Bean을 통해 호출되는지, self-invocation인지, 예외가 rollback 대상인지 확인한다.

---

## 6.2 Transaction 적용 안 되는 대표 상황

### [개념]

`@Transactional`을 붙였는데 동작하지 않는 문제는 대부분 Proxy 적용 조건, 예외 처리, Entity 상태, Transaction 범위 오해에서 발생한다.

---

### [핵심]

대표 원인:

- private method에 적용
- self-invocation
- final method 문제
- Spring Bean이 아닌 객체에서 호출
- 예외를 catch하고 삼킴
- checked exception rollback 오해
- Transaction 밖 Entity 변경
- readOnly method에서 쓰기 시도
- 테스트 코드 Transaction 오해

---

### [Troubleshooting]

문제: `@Transactional`을 붙였는데 rollback이 안 됨

```text
확인 순서:
1. method가 public인가?
2. Spring Bean으로 등록된 객체인가?
3. 외부 Bean에서 호출되는가?
4. 같은 클래스 내부 호출 self-invocation인가?
5. 발생 예외가 RuntimeException인가?
6. 예외를 catch 후 다시 던지는가?
7. checked exception이면 rollbackFor가 필요한가?
```

문제: Entity 수정이 DB에 반영되지 않음

```text
확인 순서:
1. Service method에 @Transactional이 있는가?
2. Entity가 Repository로 조회된 영속 상태인가?
3. Transaction 안에서 Entity를 변경했는가?
4. method가 정상 commit 되었는가?
5. readOnly Transaction에서 변경하고 있지 않은가?
```

문제: LazyInitializationException 발생

```text
확인 순서:
1. Transaction 안에서 연관 필드에 접근했는가?
2. Controller에서 Entity를 직접 반환하고 있지 않은가?
3. DTO 변환이 Service 안에서 끝났는가?
4. 조회 쿼리에서 필요한 연관 데이터 전략이 있는가?
```

---

### [실무]

검수용 Debug Flow:

```text
@Transactional 위치 확인
→ method 접근 제어자 확인
→ Bean 호출 경로 확인
→ self-invocation 확인
→ Exception Type 확인
→ catch 여부 확인
→ Entity 영속 상태 확인
→ readOnly 여부 확인
→ commit / rollback 로그 확인
```

---

### [FAQ]

Q. @Transactional이 안 먹는 가장 흔한 이유는?

A.
private method 적용, self-invocation, 예외 catch 후 삼킴, checked exception rollback 오해가 흔하다.

Q. Entity 변경이 반영되지 않으면 뭘 봐야 해?

A.
Transaction 안에서 영속 상태 Entity를 변경했는지, method가 commit되었는지, readOnly 설정이 아닌지 확인한다.

---

# 7. Transaction과 외부 API

## 7.1 외부 API 호출과 Transaction 경계

### [개념]

외부 API 호출은 DB Transaction과 같은 방식으로 rollback되지 않는다.

따라서 외부 API 호출과 DB 변경을 하나의 긴 Transaction 안에 무분별하게 묶으면 성능과 일관성 문제가 생길 수 있다.

---

### [핵심]

주의 대상:

- 결제 API
- 메일 발송 API
- 문자 발송 API
- 파일 업로드
- 지도 / 관광 API 호출
- 알림 Push API
- 외부 인증 API

문제:

- 외부 API 응답 지연으로 DB Transaction 길어짐
- DB Lock 유지 시간 증가
- 외부 API는 DB rollback으로 취소되지 않음
- 중간 실패 시 일관성 보상 필요
- 재시도 시 중복 처리 위험

---

### [실무]

비권장 흐름:

```text
Transaction Begin
→ Order 저장
→ 외부 결제 API 호출
→ Payment 저장
→ Transaction Commit
```

문제:

- 결제 API가 느리면 Transaction이 길어짐
- 결제 성공 후 DB 저장 실패 시 보상 필요
- DB rollback이 외부 결제를 취소하지 않음

권장 고려 흐름:

```text
주문 생성 Transaction
→ 결제 요청
→ 결제 승인 결과 수신
→ 결제 결과 저장 Transaction
→ 실패 시 보상 처리
```

예:

```java
@Transactional
public OrderResponse createOrder(OrderCreateRequest request) {
    Order order = Order.create(request);
    return OrderResponse.from(orderRepository.save(order));
}
```

```java
public PaymentResponse approvePayment(PaymentApproveRequest request) {
    PaymentApiResult result = paymentClient.approve(request.paymentKey());

    return savePaymentResult(request.orderId(), result);
}

@Transactional
public PaymentResponse savePaymentResult(Long orderId, PaymentApiResult result) {
    Order order = orderRepository.findById(orderId)
            .orElseThrow(() -> new BusinessException("ORDER_NOT_FOUND", "주문을 찾을 수 없습니다."));

    order.markPaid();

    Payment payment = Payment.create(order, result.amount());

    return PaymentResponse.from(paymentRepository.save(payment));
}
```

---

### [주의]

외부 API Transaction 주의:

- 외부 API는 DB rollback 대상이 아님
- 결제 / 파일 / 메일은 중복 처리 방지 필요
- timeout 설정 필요
- 실패 응답 처리 필요
- 보상 처리 또는 상태 기반 재시도 설계 필요
- Transaction 안에서 장시간 blocking 호출 지양
- API Key, Token은 로그에 남기지 않음

---

### [FAQ]

Q. Transaction 안에서 외부 API를 호출하면 안 돼?

A.
무조건 금지는 아니지만 장시간 호출이나 실패 보상이 필요한 외부 API는 Transaction 경계를 신중히 나눠야 한다.

Q. DB rollback이 되면 결제 API도 자동 취소돼?

A.
아니다. 외부 API 결과는 DB Transaction rollback으로 취소되지 않는다. 별도 취소 API나 보상 처리가 필요할 수 있다.

Q. 메일 발송도 Transaction 안에 넣어도 돼?

A.
메일 발송은 DB rollback으로 취소되지 않는다. 회원가입 저장 성공 후 발송하거나 이벤트 기반 처리를 고려할 수 있다.

---

## 7.2 Transaction과 Event 처리

### [개념]

Event 처리는 핵심 DB Transaction과 부가 작업을 분리하기 위한 방식이다.

예를 들어 회원가입 저장 후 이메일 발송, 주문 완료 후 알림 생성 같은 작업을 분리할 수 있다.

---

### [핵심]

Event 처리 대상:

- 이메일 발송
- 알림 생성
- 로그성 이벤트
- 통계 적재
- 외부 시스템 알림
- 비핵심 후속 작업

장점:

- 핵심 Transaction 단순화
- Service 책임 감소
- 부가 작업 분리
- 장애 영향 범위 축소 가능

주의:

- Event 처리 실패 정책 필요
- Transaction commit 이후 실행 여부 검토
- 재시도 / 중복 방지 필요
- 복잡도가 올라갈 수 있음

---

### [실무]

단순 이벤트 발행 예:

```java
@Transactional
public UserResponse signUp(SignUpRequest request) {
    User user = User.create(request.email(), request.password(), request.nickname());
    User savedUser = userRepository.save(user);

    eventPublisher.publishEvent(new UserSignedUpEvent(savedUser.getId(), savedUser.getEmail()));

    return UserResponse.from(savedUser);
}
```

이벤트 처리 예:

```java
@Component
@RequiredArgsConstructor
public class UserEventHandler {

    private final EmailClient emailClient;

    @EventListener
    public void handleUserSignedUp(UserSignedUpEvent event) {
        emailClient.sendWelcomeEmail(event.email());
    }
}
```

실무 고려:

- 이벤트 발행 시점과 Transaction commit 시점 구분
- 이메일 발송 실패가 회원가입 rollback 조건인지 결정
- 핵심 작업과 부가 작업의 실패 정책 분리
- 단순 프로젝트에서는 Service 분리만으로 충분할 수 있음

---

### [FAQ]

Q. 이벤트를 쓰면 Transaction 문제가 다 해결돼?

A.
아니다. 이벤트는 책임 분리 도구일 뿐이다. 실행 시점, 실패 처리, 재시도, 중복 방지 기준이 필요하다.

Q. 회원가입 후 이메일 발송은 Transaction 안에 넣어야 해?

A.
이메일 발송 실패가 회원가입 실패로 이어져야 하는지 정책을 먼저 정해야 한다. 일반적으로는 회원 저장과 메일 발송을 분리하는 경우가 많다.

---

# 8. Transaction Propagation 기초

## 8.1 Propagation 개념

### [개념]

Transaction Propagation은 이미 Transaction이 존재할 때 새 Transaction method가 호출되면 기존 Transaction을 사용할지, 새 Transaction을 만들지 결정하는 규칙이다.

Foundation 단계에서는 기본값인 `REQUIRED`를 우선 이해한다.

---

### [핵심]

대표 Propagation:

- REQUIRED
- REQUIRES_NEW
- SUPPORTS
- NOT_SUPPORTED
- MANDATORY
- NEVER
- NESTED

기본값:

```text
Propagation.REQUIRED
```

`REQUIRED` 의미:

```text
기존 Transaction 있음 → 기존 Transaction 참여
기존 Transaction 없음 → 새 Transaction 시작
```

---

### [실무]

기본 예:

```java
@Transactional
public void createOrder() {
    saveOrder();
    savePayment();
}
```

```java
@Transactional
public void saveOrder() {
    ...
}
```

```java
@Transactional
public void savePayment() {
    ...
}
```

호출 흐름:

```text
createOrder Transaction 시작
→ saveOrder 기존 Transaction 참여
→ savePayment 기존 Transaction 참여
→ 전체 commit 또는 rollback
```

주의:

- 같은 Bean 내부 self-invocation이면 Propagation도 기대대로 적용되지 않을 수 있음
- Propagation을 무리하게 사용하기보다 Service 책임과 Transaction Boundary를 먼저 정리
- Foundation 단계에서는 REQUIRED 중심으로 설계

---

### [FAQ]

Q. Propagation 기본값은 뭐야?

A.
기본값은 REQUIRED다. 기존 Transaction이 있으면 참여하고 없으면 새로 시작한다.

Q. Propagation을 꼭 알아야 해?

A.
기초 단계에서는 REQUIRED와 REQUIRES_NEW 차이 정도만 알아도 충분하다. 복잡한 전파 전략은 고급 Transaction 설계에서 다룬다.

---

## 8.2 REQUIRES_NEW 주의

### [개념]

`REQUIRES_NEW`는 기존 Transaction을 잠시 중단하고 새로운 Transaction을 시작하는 전파 옵션이다.

로그 저장, 감사 기록, 실패 기록처럼 메인 Transaction rollback과 별개로 저장해야 하는 경우 검토할 수 있다.

---

### [핵심]

REQUIRES_NEW 특징:

```text
기존 Transaction 있음
→ 기존 Transaction suspend
→ 새 Transaction 시작
→ 새 Transaction commit / rollback
→ 기존 Transaction 재개
```

사용 가능 상황:

- 감사 로그 저장
- 실패 이력 저장
- 알림 발송 기록
- 메인 작업 rollback과 분리할 기록

주의:

- 남용 금지
- 데이터 일관성 복잡도 증가
- self-invocation 주의
- 독립 commit이 필요한지 명확히 판단
- 테스트와 장애 시나리오 확인 필요

---

### [실무]

예:

```java
@Service
@RequiredArgsConstructor
public class AuditLogService {

    private final AuditLogRepository auditLogRepository;

    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void saveLog(String message) {
        auditLogRepository.save(AuditLog.create(message));
    }
}
```

사용:

```java
@Transactional
public void approveOrder(Long orderId) {
    try {
        Order order = orderRepository.findById(orderId).orElseThrow();
        order.approve();
    } catch (RuntimeException e) {
        auditLogService.saveLog("주문 승인 실패: " + orderId);
        throw e;
    }
}
```

의미:

```text
approveOrder rollback
→ auditLogService.saveLog는 별도 Transaction으로 commit 가능
```

---

### [주의]

REQUIRES_NEW Anti Pattern:

- 모든 로그 저장에 무분별하게 사용
- 실패해도 되는 부가 작업을 핵심 흐름에 강하게 결합
- 같은 Service 내부 method에 붙이고 self-invocation으로 호출
- 독립 commit이 필요한지 검토하지 않음
- 데이터 정합성 분석 없이 사용

---

### [FAQ]

Q. REQUIRES_NEW는 언제 써?

A.
메인 Transaction이 rollback되어도 반드시 남겨야 하는 감사 로그나 실패 기록이 있을 때 검토한다.

Q. REQUIRES_NEW를 쓰면 안전해져?

A.
무조건 안전해지는 것은 아니다. Transaction이 분리되므로 데이터 일관성과 실패 시나리오가 더 복잡해질 수 있다.

---

# 9. Transaction Isolation 기초

## 9.1 Isolation 개념

### [개념]

Transaction Isolation은 동시에 실행되는 Transaction들이 서로의 데이터를 어느 정도까지 볼 수 있는지 결정하는 격리 수준이다.

Foundation 단계에서는 기본 격리 수준을 그대로 사용하고, 동시성 문제가 발생할 때 검토한다.

---

### [핵심]

대표 Isolation Level:

- READ_UNCOMMITTED
- READ_COMMITTED
- REPEATABLE_READ
- SERIALIZABLE

동시성 문제:

- Dirty Read
- Non-repeatable Read
- Phantom Read
- Lost Update

실무 기준:

- 기본 DB Isolation을 우선 사용
- 무리한 Isolation 상향은 성능 저하 가능
- 재고 감소, 쿠폰 발급, 포인트 차감 등 동시성 이슈는 별도 Lock 전략 검토
- 상세 내용은 JPA Advanced / Database 문서와 연결

---

### [실무]

명시 예:

```java
@Transactional(isolation = Isolation.READ_COMMITTED)
public OrderResponse createOrder(OrderCreateRequest request) {
    ...
}
```

주의:

- 무조건 Isolation을 명시하지 않음
- DB 기본 격리 수준 확인
- 동시성 요구사항이 있을 때만 조정 검토
- Lock, Unique Constraint, Optimistic Lock, Pessimistic Lock과 함께 판단

---

### [FAQ]

Q. Isolation은 꼭 설정해야 해?

A.
대부분 기본 DB Isolation을 사용한다. 동시성 문제가 명확할 때 조정한다.

Q. 재고 감소는 @Transactional만 있으면 안전해?

A.
동시 주문 상황에서는 @Transactional만으로 충분하지 않을 수 있다. Lock, Unique Constraint, 동시성 제어 전략을 함께 검토해야 한다.

---

# 10. Transaction Timeout

## 10.1 Timeout 개념

### [개념]

Transaction Timeout은 Transaction이 너무 오래 유지되지 않도록 제한하는 설정이다.

긴 Transaction은 DB Lock 유지, Connection 점유, 성능 저하를 유발할 수 있다.

---

### [핵심]

긴 Transaction 원인:

- 외부 API 지연
- 대량 데이터 처리
- 복잡한 Query
- 파일 처리 포함
- 사용자 응답 대기
- 반복문 안에서 다수 DB 작업
- Lock 대기

문제:

- DB Lock 장기 유지
- Connection Pool 고갈
- 응답 지연
- Deadlock 가능성 증가
- 장애 전파

---

### [실무]

Timeout 예:

```java
@Transactional(timeout = 5)
public void updateStock(Long productId, int quantity) {
    Product product = productRepository.findById(productId)
            .orElseThrow(() -> new BusinessException("PRODUCT_NOT_FOUND", "상품을 찾을 수 없습니다."));

    product.decreaseStock(quantity);
}
```

권장:

- Transaction 범위를 짧게 유지
- 외부 API 호출을 Transaction 밖으로 분리 검토
- 대량 작업은 Batch / Chunk 처리 검토
- 반복문 안 DB 호출 최적화
- Lock 대기 상황 모니터링
- Timeout은 근본 해결보다 보호 장치로 이해

---

### [FAQ]

Q. Transaction이 길면 왜 문제야?

A.
DB Lock과 Connection을 오래 점유해 성능 저하, Deadlock, 장애 전파를 유발할 수 있다.

Q. Timeout을 설정하면 성능 문제가 해결돼?

A.
Timeout은 보호 장치일 뿐이다. 근본적으로 Transaction 범위, Query, 외부 API 호출 구조를 개선해야 한다.

---

# 11. Transaction Anti Pattern

## 11.1 Common Transaction Anti Pattern

### [개념]

Transaction Anti Pattern은 Transaction 위치, 범위, 예외 처리, 외부 연동을 잘못 설계해 데이터 일관성이나 성능 문제를 만드는 구조다.

---

### [핵심]

대표 Anti Pattern:

- Controller에 `@Transactional`
- private method에 `@Transactional`
- self-invocation
- Transaction 안에서 긴 외부 API 호출
- 예외 catch 후 삼키기
- Checked Exception rollback 오해
- Transaction 없이 Entity 수정
- readOnly Transaction에서 Entity 변경
- 너무 큰 Service method 하나에 Transaction 적용
- 여러 Use Case를 하나의 Transaction으로 묶음
- Entity를 Transaction 밖에서 DTO 변환
- DB 작업과 파일 작업을 단순 rollback으로만 해결하려 함
- REQUIRES_NEW 남용
- Isolation 무리하게 상향

---

### [실무]

Anti Pattern 예:

```java
@Transactional
public void processOrder(OrderRequest request) {
    Order order = orderRepository.save(Order.create(request));

    paymentClient.approve(request.paymentKey());

    emailClient.sendOrderEmail(request.email());

    order.markPaid();
}
```

문제:

- DB Transaction 안에서 결제 API 호출
- DB Transaction 안에서 메일 발송
- 외부 API 성공 후 DB rollback 시 보상 필요
- Transaction 시간이 길어짐
- 장애 영향 범위 커짐

개선 방향:

```text
주문 생성 Transaction
→ 결제 승인 외부 API 호출
→ 결제 결과 저장 Transaction
→ 메일 / 알림은 후속 처리
```

---

### [Troubleshooting]

문제: rollback이 안 됨

```text
원인 후보:
- 예외를 catch 후 삼킴
- checked exception 발생
- self-invocation
- private method 적용
- Transaction Proxy를 거치지 않음

해결:
- RuntimeException 기반 CustomException 사용
- 예외 catch 후 필요 시 다시 throw
- Service public method에 @Transactional 적용
- 외부 Bean 호출 구조로 변경
- rollbackFor 검토
```

문제: LazyInitializationException 발생

```text
원인 후보:
- Transaction 종료 후 Lazy 필드 접근
- Entity를 Controller로 반환
- DTO 변환이 Transaction 밖에서 수행

해결:
- Service readOnly Transaction 안에서 DTO 변환
- Entity 직접 반환 금지
- 필요한 연관 데이터 조회 전략 적용
```

문제: DB 변경이 반영되지 않음

```text
원인 후보:
- @Transactional 없음
- Entity가 영속 상태가 아님
- readOnly Transaction
- method가 rollback됨
- 변경 로직이 Transaction 밖에서 실행됨

해결:
- Service public method에 @Transactional 적용
- Repository 조회 후 영속 상태 Entity 변경
- readOnly 여부 확인
- 예외 발생 여부 확인
```

---

### [FAQ]

Q. Transaction Anti Pattern 중 가장 흔한 것은?

A.
self-invocation, 예외 catch 후 삼키기, Transaction 없이 Entity 수정, Controller에 @Transactional 적용하는 실수가 흔하다.

Q. Transaction 안에서 모든 작업을 처리하면 안전하지 않아?

A.
아니다. 외부 API, 파일, 메일 같은 작업은 DB rollback으로 취소되지 않기 때문에 오히려 일관성 문제가 생길 수 있다.

---

# 12. Transaction Review Checklist

## 12.1 Transaction Boundary Checklist

### [개념]

Transaction Boundary Checklist는 Backend Agent가 Spring Boot Service의 Transaction 설정을 검수할 때 사용하는 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] @Transactional이 Service public method에 적용되어 있는가?
- [ ] Controller에 @Transactional이 붙어 있지 않은가?
- [ ] 쓰기 작업에 @Transactional이 있는가?
- [ ] 조회 작업에 readOnly = true를 고려했는가?
- [ ] 하나의 method가 하나의 Use Case를 표현하는가?
- [ ] Transaction 범위가 너무 길지 않은가?
- [ ] 외부 API 호출이 긴 Transaction 안에 포함되어 있지 않은가?
- [ ] Entity 변경이 Transaction 안에서 수행되는가?
- [ ] Entity 변경 후 Dirty Checking을 기대할 수 있는가?
- [ ] Entity가 영속 상태인가?
- [ ] DTO 변환이 필요한 경우 Transaction 안에서 완료되는가?
- [ ] Lazy Loading 문제 가능성을 확인했는가?
- [ ] RuntimeException 기반 CustomException을 사용하는가?
- [ ] 예외를 catch 후 삼키지 않는가?
- [ ] Checked Exception rollback 필요 시 rollbackFor를 검토했는가?
- [ ] private method에 @Transactional을 붙이지 않았는가?
- [ ] self-invocation 문제가 없는가?
- [ ] readOnly Transaction에서 쓰기를 시도하지 않는가?
- [ ] REQUIRES_NEW를 남용하지 않는가?
- [ ] Isolation 설정을 불필요하게 변경하지 않았는가?
- [ ] 동시성 이슈가 있으면 Lock / Unique Constraint를 검토했는가?
```

---

### [실무]

Transaction 검수 흐름:

```text
Use Case 확인
→ Service method 확인
→ @Transactional 위치 확인
→ readOnly / write 구분 확인
→ Entity 조회 / 변경 위치 확인
→ Exception Type 확인
→ rollback 가능성 확인
→ self-invocation 확인
→ 외부 API 호출 위치 확인
→ Lazy Loading / DTO 변환 확인
→ 동시성 요구사항 확인
```

---

### [FAQ]

Q. Transaction 검수에서 가장 먼저 볼 것은?

A.
`@Transactional`이 Controller가 아니라 Service public method에 적용되어 있는지 먼저 확인한다.

Q. Transaction 설계의 핵심 기준은?

A.
Use Case 단위, 짧은 범위, 명확한 예외 처리, Service Layer 중심, 외부 API 분리, rollback 가능성 확인이다.

---

# Retrieval Queries

### [FAQ]

Q. Transaction Boundary는 뭐야?
A. 하나의 비즈니스 작업을 모두 성공하거나 모두 실패하도록 묶는 범위다. Spring Boot에서는 보통 Service public method에 설정한다.

Q. @Transactional은 어디에 붙여?
A. 대부분 Service Layer의 public method에 붙인다. Use Case 단위로 Transaction Boundary를 잡기 좋기 때문이다.

Q. Controller에 @Transactional을 붙이면 안 돼?
A. 권장하지 않는다. HTTP 요청 처리 책임과 비즈니스 Transaction 책임이 섞이기 때문이다.

Q. Repository에 @Transactional을 붙이면 안 돼?
A. Repository 내부 기본 Transaction은 있을 수 있지만 전체 비즈니스 Use Case의 Transaction Boundary는 Service에서 잡는 것이 좋다.

Q. @Transactional class 단위 적용은 괜찮아?
A. 가능하지만 모든 method에 동일 설정이 적용되므로 읽기와 쓰기 구분이 어려워질 수 있다. method 단위 지정이 명확하다.

Q. Transaction은 언제 commit돼?
A. Transaction method가 정상 종료되고 rollback 대상 예외가 없으면 commit된다.

Q. Transaction은 언제 rollback돼?
A. 기본적으로 RuntimeException이나 Error가 발생하면 rollback된다.

Q. Checked Exception은 rollback돼?
A. 기본 rollback 대상이 아닐 수 있다. 필요하면 rollbackFor 설정을 검토한다.

Q. 예외를 catch하면 rollback 안 돼?
A. catch 후 다시 던지지 않으면 Spring이 정상 종료로 판단할 수 있어 rollback되지 않을 수 있다.

Q. @Transactional(readOnly = true)는 언제 써?
A. 단건 조회, 목록 조회, 검색 조회, 페이지 조회처럼 변경이 없는 조회 Service method에 사용한다.

Q. readOnly = true면 쓰기가 절대 막혀?
A. 아니다. readOnly는 조회 의도와 최적화 힌트 성격이며 쓰기 방지 보안 장치로 의존하면 안 된다.

Q. 조회 method에도 Transaction이 필요해?
A. JPA Lazy Loading이나 일관된 읽기 컨텍스트가 필요하면 readOnly Transaction을 적용할 수 있다.

Q. LazyInitializationException은 왜 발생해?
A. Transaction 또는 영속성 컨텍스트가 종료된 뒤 Lazy 연관 필드에 접근하면 발생할 수 있다.

Q. Lazy Loading 문제는 어떻게 줄여?
A. Service의 readOnly Transaction 안에서 필요한 데이터를 조회하고 Response DTO로 변환해 Controller에는 DTO만 반환한다.

Q. Entity를 Controller로 반환하면 왜 위험해?
A. Lazy Loading, 순환 참조, 민감정보 노출, API 응답 구조 불안정 문제가 생길 수 있다.

Q. Create Transaction 흐름은?
A. Request DTO 수신, Business Validation, Entity 생성, Repository save, Response DTO 반환, commit 순서로 처리한다.

Q. Update Transaction 흐름은?
A. Entity 조회, 존재 여부 확인, 권한 / 상태 검사, Entity method 호출, Dirty Checking, commit 순서로 처리한다.

Q. Delete Transaction 흐름은?
A. Entity 조회, 권한 / 상태 검사, 물리 삭제 또는 논리 삭제 처리, commit 순서로 처리한다.

Q. Entity 수정 후 save를 꼭 호출해야 해?
A. Transaction 안에서 조회한 영속 상태 Entity라면 Dirty Checking으로 commit 시 반영될 수 있다. 신규 Entity 저장은 save가 필요하다.

Q. Dirty Checking은 언제 동작해?
A. Transaction 안에서 영속 상태 Entity의 값이 변경되고 commit될 때 변경 감지가 동작한다.

Q. Transaction 없이 Entity를 수정하면 어떻게 돼?
A. Dirty Checking이 기대대로 동작하지 않거나 변경 반영이 불명확해질 수 있다.

Q. CustomException은 RuntimeException을 상속하는 게 좋아?
A. 비즈니스 예외로 rollback이 필요한 경우 RuntimeException을 상속하면 Spring 기본 rollback 규칙과 잘 맞는다.

Q. rollbackFor는 언제 써?
A. Checked Exception에서도 rollback이 필요할 때 rollbackFor 설정을 검토한다.

Q. self-invocation이 뭐야?
A. 같은 클래스 안에서 자신의 다른 method를 직접 호출하는 상황이다. 이 경우 Proxy를 거치지 않아 @Transactional이 적용되지 않을 수 있다.

Q. private method에 @Transactional을 붙이면 왜 안 좋아?
A. Spring AOP Proxy가 private method 호출을 가로채기 어렵기 때문에 기대한 Transaction이 적용되지 않을 수 있다.

Q. @Transactional이 안 먹는 이유는?
A. private method, self-invocation, Bean이 아닌 객체 호출, 예외 catch, checked exception rollback 오해 등이 흔한 원인이다.

Q. Entity 변경이 DB에 반영되지 않으면 뭘 확인해?
A. @Transactional 위치, Entity 영속 상태, Transaction 안에서 변경했는지, readOnly 여부, commit 여부를 확인한다.

Q. Transaction 안에서 외부 API를 호출해도 돼?
A. 무조건 금지는 아니지만 장시간 호출이나 실패 보상이 필요한 외부 API는 Transaction 경계를 신중히 나눠야 한다.

Q. DB rollback이 되면 외부 API도 취소돼?
A. 아니다. 외부 API 결과는 DB Transaction rollback으로 취소되지 않는다. 별도 취소 API나 보상 처리가 필요할 수 있다.

Q. 결제 API와 Transaction은 어떻게 나눠?
A. 주문 생성 Transaction, 결제 승인 API 호출, 결제 결과 저장 Transaction처럼 경계를 나누고 실패 시 보상 처리를 고려한다.

Q. 메일 발송은 Transaction 안에 넣어도 돼?
A. 메일 발송은 DB rollback으로 취소되지 않는다. 핵심 DB 저장과 메일 발송을 분리하는 경우가 많다.

Q. Event 처리는 왜 써?
A. 회원가입 후 이메일 발송, 주문 완료 후 알림 생성 같은 부가 작업을 핵심 Transaction과 분리하기 위해 사용할 수 있다.

Q. Propagation 기본값은 뭐야?
A. 기본값은 REQUIRED다. 기존 Transaction이 있으면 참여하고 없으면 새로 시작한다.

Q. REQUIRES_NEW는 언제 써?
A. 메인 Transaction이 rollback되어도 반드시 남겨야 하는 감사 로그나 실패 기록이 있을 때 검토한다.

Q. REQUIRES_NEW를 많이 쓰면 좋아?
A. 아니다. Transaction이 분리되어 데이터 일관성과 실패 시나리오가 복잡해질 수 있으므로 남용하면 안 된다.

Q. Isolation은 꼭 설정해야 해?
A. 대부분 기본 DB Isolation을 사용한다. 동시성 문제가 명확할 때 조정한다.

Q. 재고 감소는 @Transactional만 있으면 안전해?
A. 동시 주문 상황에서는 @Transactional만으로 충분하지 않을 수 있다. Lock, Unique Constraint, 동시성 제어 전략을 함께 검토해야 한다.

Q. Transaction Timeout은 왜 필요해?
A. Transaction이 너무 오래 유지되어 DB Lock, Connection 점유, Deadlock 가능성이 커지는 것을 막기 위한 보호 장치다.

Q. Transaction이 길면 왜 문제야?
A. DB Lock과 Connection을 오래 점유해 성능 저하, Deadlock, 장애 전파를 유발할 수 있다.

Q. Transaction Anti Pattern은 뭐가 있어?
A. Controller Transaction, private method Transaction, self-invocation, 외부 API 긴 Transaction 포함, 예외 catch 후 삼키기, Transaction 없는 Entity 수정 등이 있다.

Q. Transaction 검수에서 가장 먼저 볼 것은?
A. @Transactional이 Controller가 아니라 Service public method에 적용되어 있는지 먼저 확인한다.

Q. Transaction 설계 핵심 기준은?
A. Use Case 단위, 짧은 범위, 명확한 예외 처리, Service Layer 중심, 외부 API 분리, rollback 가능성 확인이다.
