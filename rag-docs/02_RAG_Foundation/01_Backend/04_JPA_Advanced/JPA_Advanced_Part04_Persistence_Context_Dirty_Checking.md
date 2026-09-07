# JPA Advanced Part04 — Persistence Context and Dirty Checking

---

# 1. Persistence Context Purpose

## 1.1 Persistence Context Concept

### [개념]

Persistence Context는 JPA가 Entity를 관리하는 1차 캐시이자 Entity 상태 추적 공간이다.

JPA는 Persistence Context 안의 Managed Entity를 기준으로 동일성 보장, Dirty Checking, Flush, Lazy Loading을 수행한다.

---

### [핵심]

핵심 키워드:

- Persistence Context
- EntityManager
- Managed Entity
- First Level Cache
- Entity Identity
- Dirty Checking
- Snapshot
- Flush
- Transaction
- Detached Entity
- Lazy Loading

Persistence Context 역할:

- Entity 저장 공간
- 1차 캐시
- 같은 ID Entity 동일성 보장
- Entity 변경 감지
- SQL 쓰기 지연
- Flush 시점 SQL 반영
- Lazy Loading 기반 제공

---

### [실무]

JPA 동작 흐름:

```text
Service Method 호출
→ Transaction 시작
→ Repository 조회
→ Entity가 Persistence Context에 저장
→ Managed Entity 상태 변경
→ Dirty Checking
→ Flush
→ Commit
```

SQL Foundation 연결:

```text
SQL SELECT
→ Repository 조회
→ Managed Entity 등록

SQL INSERT
→ persist / save
→ Flush 시 INSERT SQL

SQL UPDATE
→ Dirty Checking
→ Flush 시 UPDATE SQL

SQL DELETE
→ remove / delete
→ Flush 시 DELETE SQL

SQL Transaction
→ JPA Persistence Context 생명주기와 연결
```

주의:

- Persistence Context는 DB 자체가 아니다.
- Entity를 변경했다고 즉시 SQL이 실행되는 것은 아니다.
- Transaction 범위가 Entity 상태 관리에 중요하다.
- Lazy Loading은 Persistence Context가 닫히면 실패할 수 있다.
- Controller에서 Entity를 다루면 Detached Entity 문제가 생기기 쉽다.

---

### [FAQ]

Q. Persistence Context는 뭐야?
A. JPA가 Entity를 관리하는 공간이며 1차 캐시, 동일성 보장, Dirty Checking, Flush 같은 기능을 제공한다.

Q. Persistence Context는 DB야?
A. 아니다. DB가 아니라 JPA가 Transaction 안에서 Entity 상태를 관리하는 메모리 공간이다.

Q. Entity를 조회하면 어디에 저장돼?
A. 조회된 Entity는 Transaction 안에서 Persistence Context에 Managed Entity로 저장될 수 있다.

Q. Persistence Context가 중요한 이유는 뭐야?
A. Entity 변경 감지, Lazy Loading, Flush, 동일성 보장 같은 JPA 핵심 동작이 Persistence Context를 기준으로 동작하기 때문이다.

---

## 1.2 EntityManager and Persistence Context

### [개념]

EntityManager는 Persistence Context를 통해 Entity를 저장, 조회, 수정, 삭제하는 JPA 핵심 API다.

Spring Data JPA Repository는 내부적으로 EntityManager를 사용해 Entity 작업을 수행한다.

---

### [핵심]

핵심 키워드:

- EntityManager
- persist
- find
- remove
- merge
- flush
- clear
- detach
- Repository
- JpaRepository
- Transaction

EntityManager 주요 작업:

| 작업      | 의미                        |
| --------- | --------------------------- |
| `persist` | Entity 영속화               |
| `find`    | Entity 조회                 |
| `remove`  | Entity 삭제                 |
| `merge`   | Detached Entity 병합        |
| `flush`   | 변경 내용을 DB에 SQL로 반영 |
| `clear`   | Persistence Context 초기화  |
| `detach`  | 특정 Entity 분리            |

---

### [실무]

Spring Data JPA 사용 흐름:

```text
Service
→ Repository
→ EntityManager
→ Persistence Context
→ Hibernate
→ SQL
→ Database
```

Repository 예시:

```java
@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    return PostResponse.from(post);
}
```

EntityManager 직접 사용 후보:

```text
복잡한 영속성 제어
→ flush / clear 필요

대량 처리
→ batch insert / batch update 제어

특수 조회
→ 직접 JPQL 작성

고급 성능 최적화
→ Persistence Context 크기 관리
```

권장:

- 일반 CRUD는 Repository 사용
- EntityManager 직접 사용은 제한적으로 사용
- Persistence Context 제어가 필요한 경우에만 직접 사용
- EntityManager 사용 시 Transaction 범위 명확화
- flush / clear는 의도를 명확히 하고 사용

주의:

- EntityManager 직접 사용은 코드 복잡도를 높인다.
- `merge`는 update와 같은 의미가 아니다.
- `clear` 후 기존 Entity는 Detached 상태가 된다.
- `flush`는 Commit이 아니다.
- Repository와 EntityManager를 섞어 쓸 때 Persistence Context 상태를 주의한다.

---

### [FAQ]

Q. EntityManager는 뭐야?
A. Entity를 Persistence Context를 통해 저장, 조회, 수정, 삭제하는 JPA 핵심 API다.

Q. Repository를 쓰면 EntityManager를 몰라도 돼?
A. 기본 CRUD는 Repository로 충분하지만 Dirty Checking, Flush, Detached 문제를 이해하려면 EntityManager 개념이 필요하다.

Q. EntityManager를 직접 써야 해?
A. 대부분은 Repository로 충분하다. 특수한 영속성 제어가 필요할 때 제한적으로 사용한다.

Q. `flush`와 `clear`는 언제 써?
A. 대량 처리나 테스트에서 SQL 반영 시점과 Persistence Context 상태를 명확히 제어해야 할 때 사용한다.

---

# 2. First Level Cache and Identity

## 2.1 First Level Cache

### [개념]

First Level Cache는 Persistence Context 내부에 존재하는 Entity 캐시다.

같은 Transaction 안에서 같은 Primary Key로 Entity를 다시 조회하면 DB를 다시 조회하지 않고 Persistence Context의 Entity를 반환할 수 있다.

---

### [핵심]

핵심 키워드:

- First Level Cache
- Persistence Context
- Primary Key
- Entity Identity
- Managed Entity
- Repeatable Read in Application Level
- Repository findById
- EntityManager find

동작 기준:

```text
findById(1L)
→ DB SELECT
→ Persistence Context 저장

findById(1L) again
→ Persistence Context 조회
→ DB SELECT 생략 가능
```

---

### [실무]

예시:

```java
@Transactional
public void checkFirstLevelCache(Long postId) {
    Post post1 = postRepository.findById(postId).orElseThrow();
    Post post2 = postRepository.findById(postId).orElseThrow();

    boolean same = post1 == post2;
}
```

실무 의미:

- 같은 Transaction 안에서 같은 Entity ID는 같은 객체일 수 있다.
- Repository를 여러 번 호출해도 1차 캐시가 동작할 수 있다.
- Persistence Context가 닫히면 1차 캐시도 사라진다.
- 대량 조회 시 Persistence Context에 Entity가 많이 쌓일 수 있다.
- 대량 처리에서는 flush / clear를 검토한다.

주의:

- First Level Cache는 Transaction 범위에 종속된다.
- Application 전체 공유 캐시가 아니다.
- 2차 캐시와 다르다.
- Native Query나 Bulk Query 후 Persistence Context 상태 불일치를 주의한다.
- Query Method 결과는 SQL 실행 후 Entity를 Persistence Context에 등록할 수 있다.

---

### [FAQ]

Q. First Level Cache는 뭐야?
A. Persistence Context 내부의 Entity 캐시이며 같은 Transaction 안에서 같은 ID Entity 재조회 시 활용될 수 있다.

Q. 1차 캐시는 Application 전체에서 공유돼?
A. 아니다. 보통 Transaction / Persistence Context 범위 안에서만 유효하다.

Q. 같은 ID로 두 번 조회하면 SQL이 한 번만 나가?
A. 상황에 따라 1차 캐시가 동작하면 두 번째 조회는 DB SELECT 없이 Entity를 반환할 수 있다.

Q. 대량 처리에서 1차 캐시가 문제가 될 수 있어?
A. 그렇다. 많은 Entity가 Persistence Context에 쌓이면 메모리 사용량이 증가하므로 flush / clear를 검토한다.

---

## 2.2 Entity Identity Guarantee

### [개념]

Entity Identity Guarantee는 같은 Persistence Context 안에서 같은 Primary Key를 가진 Entity가 동일한 Java 객체로 관리될 수 있는 특성이다.

JPA는 Primary Key를 기준으로 Entity 동일성을 관리한다.

---

### [핵심]

핵심 키워드:

- Entity Identity
- Object Identity
- Primary Key
- Persistence Context
- Managed Entity
- `==`
- equals
- hashCode
- Detached Entity

구분:

| 개념                 | 기준                                 |
| -------------------- | ------------------------------------ |
| Entity Identity      | DB Primary Key                       |
| Object Identity      | Java Reference                       |
| Persistence Identity | Persistence Context 안의 동일 Entity |
| Business Equality    | 비즈니스 값 기준                     |

---

### [실무]

예시:

```java
@Transactional
public void identityCheck(Long userId) {
    User user1 = userRepository.findById(userId).orElseThrow();
    User user2 = userRepository.findById(userId).orElseThrow();

    boolean result = user1 == user2;
}
```

권장:

- Entity 비교 기준은 프로젝트 규칙으로 통일
- Lombok `@Data` 사용 지양
- Association Field를 equals / hashCode에 포함하지 않음
- Entity ID 생성 전 / 생성 후 상태를 구분
- Detached Entity 비교는 주의

주의:

- Persistence Context 밖에서는 같은 DB Row라도 다른 Java 객체일 수 있다.
- Detached Entity는 JPA가 변경을 추적하지 않는다.
- equals / hashCode에 연관관계를 넣으면 Lazy Loading과 순환 참조 문제가 생길 수 있다.
- 신규 Entity는 ID가 없으므로 동일성 비교가 불안정하다.
- Entity를 HashSet에 넣은 뒤 ID가 생성되면 hashCode 문제가 생길 수 있다.

---

### [FAQ]

Q. 같은 ID Entity는 항상 같은 객체야?
A. 아니다. 같은 Persistence Context 안에서는 같을 수 있지만 Transaction 범위 밖에서는 다른 객체일 수 있다.

Q. Entity Identity는 뭐야?
A. DB Primary Key를 기준으로 Entity를 식별하는 개념이다.

Q. Entity equals / hashCode는 어떻게 해야 해?
A. 프로젝트 규칙으로 통일하고 Association Field 포함은 피하는 것이 좋다.

Q. Lombok `@Data`를 Entity에 쓰면 왜 위험해?
A. equals, hashCode, toString, Setter가 무분별하게 생성되어 Lazy Loading, 순환 참조, 상태 변경 문제가 생길 수 있다.

---

# 3. Entity Lifecycle

## 3.1 Entity State

### [개념]

Entity Lifecycle은 Entity가 JPA에서 어떤 상태로 관리되는지 나타내는 흐름이다.

Entity 상태는 Transient, Managed, Detached, Removed로 구분한다.

---

### [핵심]

Entity 상태:

| 상태      | 의미                                   |
| --------- | -------------------------------------- |
| Transient | JPA가 관리하지 않는 새 객체            |
| Managed   | Persistence Context가 관리하는 Entity  |
| Detached  | 과거에 관리되었지만 현재 분리된 Entity |
| Removed   | 삭제 예정 Entity                       |

핵심 키워드:

- Transient
- Managed
- Detached
- Removed
- Entity Lifecycle
- Persistence Context
- Transaction
- Dirty Checking
- Lazy Loading

---

### [실무]

상태 흐름:

```text
new Entity()
→ Transient

repository.save(entity) / entityManager.persist(entity)
→ Managed

Transaction Commit / EntityManager close / clear
→ Detached

repository.delete(entity) / entityManager.remove(entity)
→ Removed
```

예시:

```java
@Transactional
public Long createPost(PostCreateRequest request) {
    Post post = Post.create(request.title(), request.content());
    Post savedPost = postRepository.save(post);
    return savedPost.getPostId();
}
```

해석:

```text
Post.create()
→ Transient

postRepository.save(post)
→ Managed

Transaction Commit
→ Flush
→ DB INSERT
→ Transaction 종료 후 Detached 가능
```

주의:

- new로 만든 Entity는 DB와 무관하다.
- Managed Entity만 Dirty Checking 대상이다.
- Detached Entity는 변경해도 DB에 자동 반영되지 않는다.
- Removed Entity는 Flush 시 DELETE SQL 대상이다.
- Lazy Loading은 Managed 상태와 Transaction 범위에 영향을 받는다.

---

### [FAQ]

Q. Entity Lifecycle은 뭐야?
A. Entity가 JPA에서 Transient, Managed, Detached, Removed 상태로 관리되는 흐름이다.

Q. new로 만든 Entity는 바로 DB에 저장돼?
A. 아니다. new Entity는 Transient 상태이며 persist 또는 save가 필요하다.

Q. Dirty Checking은 어떤 Entity에 동작해?
A. Persistence Context가 관리하는 Managed Entity에 동작한다.

Q. Transaction이 끝나면 Entity는 어떻게 돼?
A. Persistence Context가 닫히면서 Entity는 Detached 상태가 될 수 있다.

---

## 3.2 Transient and Managed

### [개념]

Transient Entity는 아직 Persistence Context가 관리하지 않는 새 객체다.

Managed Entity는 Persistence Context가 관리하며 Dirty Checking과 Flush 대상이 될 수 있는 Entity다.

---

### [핵심]

Transient 특징:

- `new`로 생성
- DB Row와 연결되지 않음
- Persistence Context가 관리하지 않음
- Dirty Checking 대상 아님
- Lazy Loading 대상 아님

Managed 특징:

- Persistence Context가 관리
- Primary Key 기준 관리
- Dirty Checking 대상
- Flush 대상
- Lazy Loading 가능
- 1차 캐시 대상

---

### [실무]

Transient 예시:

```java
Post post = Post.create("title", "content");
```

Managed 전환 예시:

```java
@Transactional
public Long createPost(PostCreateRequest request) {
    Post post = Post.create(request.title(), request.content());
    Post savedPost = postRepository.save(post);

    savedPost.update("new title", "new content");

    return savedPost.getPostId();
}
```

흐름:

```text
Post.create()
→ Transient

postRepository.save(post)
→ Managed

savedPost.update()
→ Dirty Checking 대상
```

권장:

- Entity 생성은 Factory Method로 명확히 함
- 저장 후 반환 Entity 상태를 이해
- Managed Entity 변경은 의미 있는 Method로 수행
- 생성과 수정 Transaction을 명확히 구분
- 저장 직후 ID 필요 여부를 확인

주의:

- ID 생성 전략에 따라 ID 할당 시점이 다르다.
- `save` 반환 값을 사용할지 원본 객체를 사용할지 프로젝트 기준을 정한다.
- Managed Entity를 Controller로 넘겨 변경하지 않는다.
- Request DTO를 Entity처럼 사용하지 않는다.

---

### [FAQ]

Q. Transient Entity는 뭐야?
A. JPA가 아직 관리하지 않는 새 Entity 객체다.

Q. Managed Entity는 뭐야?
A. Persistence Context가 관리하는 Entity이며 Dirty Checking과 Flush 대상이 될 수 있다.

Q. save하면 Entity는 Managed 상태가 돼?
A. Transaction 안에서 저장된 Entity는 Managed 상태가 될 수 있다.

Q. Managed Entity를 변경하면 바로 UPDATE SQL이 실행돼?
A. 아니다. Flush 시점에 변경 감지가 되어 UPDATE SQL이 실행될 수 있다.

---

## 3.3 Detached and Removed

### [개념]

Detached Entity는 과거에 Persistence Context가 관리했지만 현재는 분리된 Entity다.

Removed Entity는 삭제 대상으로 표시된 Entity이며 Flush 시 DELETE SQL이 실행될 수 있다.

---

### [핵심]

Detached 발생 상황:

- Transaction 종료
- EntityManager close
- EntityManager clear
- EntityManager detach
- Persistence Context 범위 밖으로 Entity 전달

Removed 발생 상황:

- `entityManager.remove(entity)`
- `repository.delete(entity)`
- orphanRemoval에 의한 삭제
- Cascade REMOVE에 의한 삭제

---

### [실무]

Detached 문제 예시:

```java
public void updatePost(Post post) {
    post.update("new title", "new content");
}
```

문제:

```text
post가 Detached 상태일 수 있음
→ Persistence Context가 변경 추적하지 않음
→ Dirty Checking 동작 안 함
```

권장 수정 방식:

```java
@Transactional
public void updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    post.update(request.title(), request.content());
}
```

삭제 예시:

```java
@Transactional
public void deletePost(Long postId) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    postRepository.delete(post);
}
```

주의:

- Detached Entity를 수정해도 DB에 자동 반영되지 않는다.
- 수정 API에서는 Transaction 안에서 Entity를 다시 조회 후 변경한다.
- Detached Entity를 그대로 save하면 의도치 않은 덮어쓰기 위험이 있다.
- Removed Entity를 다시 사용하지 않는다.
- Cascade / orphanRemoval 삭제는 Part07 기준과 연결한다.

---

### [FAQ]

Q. Detached Entity는 뭐야?
A. 한때 Persistence Context가 관리했지만 현재는 분리되어 JPA가 변경을 추적하지 않는 Entity다.

Q. Detached Entity를 수정하면 DB에 반영돼?
A. 아니다. Persistence Context가 관리하지 않으므로 Dirty Checking이 동작하지 않는다.

Q. 수정 API에서 Entity를 새로 만들어 save하면 돼?
A. 가능은 하지만 기존 값 덮어쓰기와 연관관계 손실 위험이 있어 Transaction 안에서 조회 후 변경하는 방식이 안전하다.

Q. Removed Entity는 뭐야?
A. 삭제 대상으로 표시된 Entity이며 Flush 시 DELETE SQL이 실행될 수 있다.

---

# 4. Dirty Checking

## 4.1 Dirty Checking Concept

### [개념]

Dirty Checking은 Transaction 안에서 Managed Entity의 변경을 감지해 Flush 시 UPDATE SQL을 생성하는 JPA 기능이다.

Dirty Checking은 Persistence Context가 Entity의 초기 상태 Snapshot을 보관하고 현재 상태와 비교해서 동작한다.

---

### [핵심]

핵심 키워드:

- Dirty Checking
- Managed Entity
- Snapshot
- Persistence Context
- Transaction
- Flush
- UPDATE SQL
- Entity State Change
- No Explicit Save

동작 조건:

```text
Entity가 Managed 상태
→ Transaction 범위 안
→ Snapshot 존재
→ Entity Field 변경
→ Flush 시 변경 감지
→ UPDATE SQL 생성
```

---

### [실무]

수정 예시:

```java
@Transactional
public void updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    post.update(request.title(), request.content());
}
```

SQL Foundation 연결:

```text
SQL UPDATE 직접 작성
→ JPA Dirty Checking
→ Entity 상태 변경
→ Flush 시 UPDATE SQL 생성
```

권장:

- 수정 작업은 Service `@Transactional` 안에서 처리
- Entity를 먼저 조회해 Managed 상태로 만든 뒤 변경
- Setter보다 의미 있는 상태 변경 Method 사용
- update 후 무조건 save 호출하지 않음
- SQL 로그로 UPDATE 발생 여부 확인

주의:

- Transaction 밖에서는 Dirty Checking이 동작하지 않는다.
- Detached Entity는 Dirty Checking 대상이 아니다.
- `@Transactional(readOnly = true)`에서는 변경 반영을 기대하지 않는다.
- Bulk Update는 Dirty Checking과 다르게 동작한다.
- 변경 Field가 없으면 UPDATE SQL이 발생하지 않을 수 있다.

---

### [FAQ]

Q. Dirty Checking은 뭐야?
A. Transaction 안에서 Managed Entity의 변경을 감지해 Flush 시 UPDATE SQL을 생성하는 기능이다.

Q. JPA update 할 때 save를 꼭 해야 해?
A. Transaction 안에서 조회한 Managed Entity를 변경하면 Dirty Checking으로 반영될 수 있어 save가 필수는 아니다.

Q. Dirty Checking이 동작하려면 무엇이 필요해?
A. Managed Entity, Transaction 범위, Snapshot, Flush 시점이 필요하다.

Q. Dirty Checking은 Detached Entity에도 동작해?
A. 아니다. Detached Entity는 Persistence Context가 관리하지 않으므로 Dirty Checking 대상이 아니다.

---

## 4.2 Dirty Checking Update Pattern

### [개념]

Dirty Checking Update Pattern은 수정 API에서 Entity를 Transaction 안에서 조회하고, 상태 변경 Method를 호출해 변경을 반영하는 방식이다.

---

### [핵심]

권장 Pattern:

```text
Request DTO 수신
→ Service @Transactional
→ Entity 조회
→ 권한 / 상태 검증
→ Entity 상태 변경 Method 호출
→ Dirty Checking
→ Flush
→ Commit
```

비권장 Pattern:

```text
RequestBody로 Entity 수신
→ Entity에 ID 세팅
→ save 호출
→ 기존 값 덮어쓰기 위험
```

---

### [실무]

권장 예시:

```java
@Transactional
public void updateUser(Long userId, UserUpdateRequest request) {
    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    user.updateNickname(request.nickname());
}
```

Entity Method:

```java
public void updateNickname(String nickname) {
    this.nickname = nickname;
}
```

비권장 예시:

```java
@Transactional
public void updateUser(User requestUser) {
    userRepository.save(requestUser);
}
```

문제:

- RequestBody Entity 직접 수신 위험
- Detached Entity save 위험
- 기존 값 null 덮어쓰기 가능
- 권한 검증 / 상태 검증 누락 가능
- 변경 의도 불명확

권장:

- 수정 대상 Entity를 DB에서 조회
- Request DTO 값만 Entity Method에 전달
- 권한 검증은 Service에서 처리
- 상태 변경 규칙은 Entity Method 또는 Domain Method에서 처리
- 변경 후 명시적 save를 반복하지 않음

주의:

- save가 항상 불필요한 것은 아니다.
- 신규 Entity 저장은 save가 필요하다.
- Detached Entity 병합이 필요한 특수 상황은 별도 검토한다.
- Dirty Checking은 Transaction Commit 또는 Flush 시점에 반영된다.

---

### [FAQ]

Q. 수정 API에서 가장 안전한 JPA 패턴은 뭐야?
A. Transaction 안에서 Entity를 조회한 뒤 Entity 상태 변경 Method를 호출하는 방식이다.

Q. update 후 `repository.save(entity)`를 다시 호출하면 안 돼?
A. Managed Entity라면 필수는 아니다. 다만 신규 저장과 Detached Entity 상황은 구분해야 한다.

Q. RequestBody Entity를 save하는 방식은 왜 위험해?
A. 기존 값 덮어쓰기, 연관관계 손실, 보안 문제, API와 Entity 결합 위험이 있다.

Q. 변경 Method를 Entity에 두는 이유는 뭐야?
A. 상태 변경 의도를 명확히 하고 비즈니스 규칙과 Dirty Checking 대상을 통제하기 위해서다.

---

## 4.3 Dirty Checking Failure

### [개념]

Dirty Checking Failure는 Entity 변경이 DB에 반영되지 않는 문제다.

대부분 Transaction 범위, Entity 상태, readOnly 설정, Detached Entity, 변경 Method 호출 누락에서 발생한다.

---

### [핵심]

주요 원인:

- `@Transactional` 없음
- Entity가 Detached 상태
- Transaction 밖에서 Entity 변경
- `@Transactional(readOnly = true)`에서 변경
- Entity를 조회하지 않고 새 객체를 수정
- 변경 Method 호출 누락
- Bulk Query 후 Persistence Context 불일치
- 테스트에서 Commit / Flush 확인 누락

---

### [실무]

Debug Flow:

```text
변경 API 호출
→ @Transactional 확인
→ Entity 조회 위치 확인
→ Entity가 Managed 상태인지 확인
→ readOnly 여부 확인
→ 변경 Method 호출 여부 확인
→ Flush / Commit 여부 확인
→ SQL UPDATE 로그 확인
```

문제 예시:

```java
@Transactional(readOnly = true)
public void updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId).orElseThrow();
    post.update(request.title(), request.content());
}
```

문제:

```text
readOnly = true
→ 변경 작업에 부적합
→ 변경 반영 기대 금지
```

개선:

```java
@Transactional
public void updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId).orElseThrow();
    post.update(request.title(), request.content());
}
```

권장:

- 수정 메서드는 일반 `@Transactional`
- 조회 메서드는 `@Transactional(readOnly = true)`
- SQL 로그로 UPDATE 발생 확인
- 테스트에서 `flush()`로 반영 시점 확인 가능
- Detached Entity를 수정하지 않음

---

### [FAQ]

Q. Dirty Checking이 안 되면 뭘 먼저 확인해?
A. `@Transactional`, Entity Managed 상태, readOnly 설정, 변경 Method 호출 여부, SQL UPDATE 로그를 확인한다.

Q. `readOnly = true`에서 수정하면 반영돼?
A. 기대하지 않는 것이 좋다. 변경 작업은 일반 `@Transactional`에서 수행해야 한다.

Q. SQL UPDATE가 안 나가면 무조건 오류야?
A. 변경된 Field가 없거나 Flush 전일 수 있다. Transaction과 Flush 시점을 확인해야 한다.

Q. 테스트에서 Dirty Checking을 확인하려면 어떻게 해?
A. Transaction 안에서 Entity 변경 후 `flush()`를 호출하거나 SQL 로그를 확인한다.

---

# 5. Flush

## 5.1 Flush Concept

### [개념]

Flush는 Persistence Context의 변경 내용을 DB에 SQL로 반영하는 과정이다.

Flush는 Commit과 같지 않다.

---

### [핵심]

핵심 키워드:

- Flush
- Persistence Context
- SQL Synchronization
- INSERT SQL
- UPDATE SQL
- DELETE SQL
- Commit
- Rollback
- JPQL Before Flush
- Constraint Violation

Flush 발생 시점:

- Transaction Commit 전
- JPQL Query 실행 전
- `entityManager.flush()` 호출
- FlushMode 설정에 따른 시점

---

### [실무]

Flush 흐름:

```text
Managed Entity 변경
→ Persistence Context에 변경 누적
→ Flush
→ SQL INSERT / UPDATE / DELETE 전송
→ Commit 전까지 Rollback 가능
```

SQL Foundation 연결:

```text
Persistence Context 변경
→ Flush
→ SQL 전송
→ DB Constraint 확인 가능
→ Commit
→ Transaction 확정
```

예시:

```java
@Transactional
public void createPost(PostCreateRequest request) {
    Post post = Post.create(request.title(), request.content());
    postRepository.save(post);

    entityManager.flush();
}
```

권장:

- 일반 비즈니스 코드에서는 명시적 flush를 남용하지 않음
- 테스트에서 Constraint 오류를 빨리 확인할 때 flush 사용 가능
- 대량 처리에서 일정 단위 flush / clear 검토
- JPQL 실행 전 자동 Flush 가능성을 이해
- Flush 후에도 Rollback 가능하다는 점을 명확히 함

주의:

- Flush는 Commit이 아니다.
- Flush 후 Transaction Rollback이 가능하다.
- Flush 시 DB Constraint 위반 예외가 발생할 수 있다.
- JPQL 실행 전 Flush로 예상보다 빨리 SQL이 나갈 수 있다.
- Bulk Query 전후 Persistence Context 상태를 주의해야 한다.

---

### [FAQ]

Q. Flush는 뭐야?
A. Persistence Context의 변경 내용을 DB에 SQL로 반영하는 과정이다.

Q. Flush와 Commit은 같은 거야?
A. 아니다. Flush는 SQL을 DB에 보내는 과정이고 Commit은 Transaction을 확정하는 과정이다.

Q. Flush하면 Rollback이 안 돼?
A. 아니다. Flush 후에도 Transaction이 Commit되지 않았다면 Rollback 가능하다.

Q. Flush는 언제 발생해?
A. Transaction Commit 전, JPQL 실행 전, 명시적 `flush()` 호출 시 발생할 수 있다.

---

## 5.2 Flush and JPQL

### [개념]

JPA는 JPQL Query 실행 전 Persistence Context의 변경 내용을 DB Query 결과와 맞추기 위해 Flush를 수행할 수 있다.

이를 통해 Query 결과와 Entity 변경 상태의 불일치를 줄인다.

---

### [핵심]

핵심 키워드:

- JPQL
- Auto Flush
- Query Consistency
- Persistence Context
- Pending Changes
- FlushMode
- SELECT Before Flush
- Constraint Exception

동작 흐름:

```text
Entity 변경
→ JPQL 실행
→ Auto Flush 발생 가능
→ UPDATE / INSERT SQL 전송
→ JPQL SELECT 실행
```

---

### [실무]

예시:

```java
@Transactional
public List<Post> updateAndSearch(Long postId) {
    Post post = postRepository.findById(postId).orElseThrow();
    post.update("updated title", "content");

    return postRepository.searchByKeyword("updated");
}
```

해석:

```text
post.update()
→ 변경 내용 Persistence Context에 존재
→ searchByKeyword JPQL 실행
→ Query 결과 일관성을 위해 Flush 발생 가능
```

권장:

- JPQL 실행 전 Flush 가능성을 이해
- Query 중간에 Constraint 오류가 발생할 수 있음을 인지
- 변경 작업과 조회 작업의 순서를 명확히 설계
- 테스트에서 SQL 실행 순서 확인
- Bulk Query와 Flush 순서 주의

주의:

- JPQL 실행 전 예상치 못한 UPDATE SQL이 나갈 수 있다.
- Auto Flush는 성능과 오류 발생 시점에 영향을 줄 수 있다.
- Native Query와 Flush 동작은 상황에 따라 다르게 느껴질 수 있다.
- FlushMode를 임의 변경하는 것은 신중해야 한다.

---

### [FAQ]

Q. JPQL 전에 Flush가 일어나는 이유는 뭐야?
A. Query 결과가 Persistence Context의 변경 내용과 일치하도록 하기 위해 Flush가 발생할 수 있다.

Q. SELECT Query인데 UPDATE SQL이 먼저 나갈 수 있어?
A. 가능하다. 이전에 변경된 Managed Entity가 있으면 JPQL 실행 전 Flush가 발생할 수 있다.

Q. JPQL 실행 중 Constraint 오류가 날 수 있어?
A. 가능하다. JPQL 전 Flush 과정에서 INSERT / UPDATE SQL이 실행되며 DB Constraint 위반이 드러날 수 있다.

Q. Auto Flush를 막아도 돼?
A. 특수 상황에서는 FlushMode를 조정할 수 있지만 Query 일관성 문제를 만들 수 있어 신중해야 한다.

---

# 6. Commit and Rollback

## 6.1 Commit Concept

### [개념]

Commit은 Transaction의 변경 내용을 최종 확정하는 과정이다.

JPA는 Commit 전에 Flush를 수행해 Persistence Context 변경 내용을 DB에 SQL로 반영할 수 있다.

---

### [핵심]

핵심 키워드:

- Commit
- Transaction
- Flush Before Commit
- Dirty Checking
- SQL Execution
- Data Consistency
- Rollback
- Constraint

Commit 흐름:

```text
Transaction Begin
→ Entity 조회 / 저장 / 변경
→ Dirty Checking
→ Flush
→ DB SQL 실행
→ Commit
→ 변경 확정
```

---

### [실무]

수정 API 흐름:

```text
Controller Request
→ Service @Transactional
→ Repository findById
→ Managed Entity 변경
→ Method 종료
→ Flush
→ Commit
→ Response
```

예시:

```java
@Transactional
public void changeNickname(Long userId, String nickname) {
    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    user.updateNickname(nickname);
}
```

해석:

```text
user.updateNickname()
→ Managed Entity 변경
→ Method 종료
→ Commit 전 Flush
→ UPDATE SQL
→ Commit
```

권장:

- Transaction 범위를 Service Method로 명확히 함
- 변경 작업은 일반 `@Transactional`
- 예외 발생 시 Rollback 기준 확인
- Commit 전 Flush에서 Constraint 오류 발생 가능성 고려
- 외부 API 호출과 Transaction 범위는 신중히 설계

주의:

- Commit 시점에 SQL 오류가 드러날 수 있다.
- Flush가 먼저 성공해도 Commit 전 예외로 Rollback될 수 있다.
- Transaction이 너무 길면 Lock과 Connection 점유 문제가 생길 수 있다.
- 비동기 작업과 Transaction 경계를 혼동하지 않는다.

---

### [FAQ]

Q. Commit은 뭐야?
A. Transaction의 변경 내용을 최종 확정하는 과정이다.

Q. Commit 전에 Flush가 발생해?
A. 일반적으로 Commit 전에 Flush가 발생해 Persistence Context 변경 내용을 DB에 SQL로 반영한다.

Q. Commit 시점에 오류가 날 수 있어?
A. 가능하다. Flush 과정에서 DB Constraint 오류나 SQL 오류가 발생할 수 있다.

Q. Transaction 범위는 어디에 두는 게 좋아?
A. 일반적으로 Service public method에 둔다.

---

## 6.2 Rollback Concept

### [개념]

Rollback은 Transaction 중 발생한 변경을 취소하는 과정이다.

Flush로 SQL이 DB에 전달되었더라도 Commit 전이면 Rollback으로 변경을 취소할 수 있다.

---

### [핵심]

핵심 키워드:

- Rollback
- Transaction
- RuntimeException
- CheckedException
- Flush Before Rollback
- Data Consistency
- Exception Handling
- Transaction Boundary

Rollback 대상:

- RuntimeException 기본 Rollback
- Error 기본 Rollback
- CheckedException은 기본 Rollback 대상 아님
- `rollbackFor`로 조정 가능
- Transaction 설정에 따라 변경 가능

---

### [실무]

예시:

```java
@Transactional
public void createPostAndFail(PostCreateRequest request) {
    Post post = Post.create(request.title(), request.content());
    postRepository.save(post);

    throw new BusinessException("FAIL", "처리 중 오류가 발생했습니다.");
}
```

흐름:

```text
postRepository.save(post)
→ Persistence Context에 저장
→ 예외 발생
→ Transaction Rollback
→ INSERT 취소
```

권장:

- 비즈니스 실패는 RuntimeException 기반 CustomException 사용 가능
- Rollback 대상 예외를 프로젝트 규칙으로 통일
- CheckedException 사용 시 rollbackFor 검토
- 외부 시스템 호출과 DB Transaction 순서 주의
- 테스트에서 Rollback 여부 확인

주의:

- 예외를 catch하고 삼키면 Rollback이 안 될 수 있다.
- Self Invocation은 `@Transactional`이 적용되지 않을 수 있다.
- CheckedException은 기본 Rollback 대상이 아니다.
- Flush 후에도 Rollback 가능하지만 외부 시스템 작업은 되돌릴 수 없다.
- Transaction 안에서 긴 외부 API 호출은 피하는 것이 좋다.

---

### [FAQ]

Q. Rollback은 뭐야?
A. Transaction 중 발생한 변경을 취소하는 과정이다.

Q. Flush 후에도 Rollback돼?
A. Commit 전이면 Flush로 SQL이 나갔더라도 Rollback으로 취소할 수 있다.

Q. 모든 Exception에서 Rollback돼?
A. 아니다. 기본적으로 RuntimeException과 Error는 Rollback되지만 CheckedException은 기본 Rollback 대상이 아니다.

Q. 예외를 catch하면 Rollback돼?
A. 예외를 처리하고 밖으로 던지지 않으면 Rollback이 안 될 수 있다.

---

# 7. Merge and Detached Entity

## 7.1 Merge Concept

### [개념]

Merge는 Detached Entity의 값을 새로운 Managed Entity에 복사하는 JPA 기능이다.

Merge는 Detached Entity 자체를 다시 Managed로 만드는 것이 아니라, 병합 결과로 Managed Entity를 반환한다.

---

### [핵심]

핵심 키워드:

- Merge
- Detached Entity
- Managed Copy
- EntityManager.merge
- Save Detached
- Overwrite Risk
- Update Anti Pattern

Merge 흐름:

```text
Detached Entity 전달
→ merge 호출
→ DB 조회 또는 Managed Entity 확인
→ 값 복사
→ Managed Entity 반환
→ Detached Entity 자체는 그대로 Detached
```

---

### [실무]

비권장 수정 방식:

```java
@Transactional
public void updateUser(User detachedUser) {
    entityManager.merge(detachedUser);
}
```

문제:

- Detached Entity 값 전체 복사
- null 값으로 기존 값 덮어쓰기 가능
- Association 손실 가능
- 변경 의도 불명확
- RequestBody Entity 수신과 결합 위험

권장 수정 방식:

```java
@Transactional
public void updateUser(Long userId, UserUpdateRequest request) {
    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    user.updateNickname(request.nickname());
}
```

권장:

- 일반 수정 API에서는 merge보다 Dirty Checking 우선
- Entity를 Transaction 안에서 다시 조회 후 변경
- Request DTO 값을 필요한 Field에만 반영
- merge는 특수한 Detached Entity 병합 상황에서 제한적으로 사용
- merge 반환 Entity를 사용해야 함

주의:

- merge는 update와 같은 단순 기능이 아니다.
- merge 대상 객체는 여전히 Detached다.
- merge는 의도치 않은 전체 Field 복사를 만들 수 있다.
- Entity Graph가 복잡하면 연관관계 손실 위험이 커진다.
- Review Agent는 merge 남용을 Anti Pattern으로 탐지해야 한다.

---

### [FAQ]

Q. merge는 뭐야?
A. Detached Entity의 값을 Managed Entity에 복사하는 JPA 기능이다.

Q. merge하면 전달한 Entity가 Managed가 돼?
A. 아니다. merge는 Managed 복사본을 반환하며 전달한 Entity 자체는 Detached 상태다.

Q. 수정 API에서 merge를 쓰는 게 좋아?
A. 일반적으로 권장하지 않는다. Transaction 안에서 Entity를 조회한 뒤 Dirty Checking으로 수정하는 방식이 안전하다.

Q. merge가 위험한 이유는 뭐야?
A. null 값 덮어쓰기, 연관관계 손실, 변경 의도 불명확 문제가 생길 수 있다.

---

## 7.2 Detached Entity Problem

### [개념]

Detached Entity Problem은 Persistence Context가 관리하지 않는 Entity를 Managed Entity처럼 수정하거나 저장하면서 발생하는 문제다.

수정 API, Controller Entity 전달, RequestBody Entity 수신, Session 종료 후 Lazy 접근에서 자주 발생한다.

---

### [핵심]

발생 원인:

- Transaction 밖 Entity 수정
- Controller로 Entity 전달 후 변경
- RequestBody로 Entity 직접 수신
- Detached Entity를 save / merge
- OSIV 의존
- Lazy Field를 Transaction 밖에서 접근
- Persistence Context clear 이후 Entity 수정

---

### [실무]

문제 흐름:

```text
Service에서 Entity 조회
→ Transaction 종료
→ Entity Detached
→ Controller 또는 다른 Layer에서 Entity 변경
→ Dirty Checking 동작 안 함
```

비권장 예시:

```java
@GetMapping("/{id}")
public User getUser(@PathVariable Long id) {
    return userService.getUserEntity(id);
}
```

문제:

- Entity 직접 반환
- Transaction 종료 후 Detached 가능
- Lazy Loading 예외 가능
- API와 Persistence Model 결합

권장 예시:

```java
@GetMapping("/{id}")
public UserResponse getUser(@PathVariable Long id) {
    return userService.getUser(id);
}
```

Service:

```java
@Transactional(readOnly = true)
public UserResponse getUser(Long userId) {
    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    return UserResponse.from(user);
}
```

권장:

- Controller에 Entity를 반환하지 않음
- DTO 변환은 Transaction 범위 안에서 수행
- 수정은 Service Transaction 안에서 Entity 재조회 후 처리
- Detached Entity save / merge 지양
- Lazy Loading 필요 데이터는 Fetch Join / DTO Projection으로 조회

---

### [FAQ]

Q. Detached Entity Problem은 뭐야?
A. Persistence Context가 관리하지 않는 Entity를 수정하거나 사용해 변경 반영 실패나 Lazy Loading 예외가 발생하는 문제다.

Q. Detached Entity를 그대로 save하면 안 돼?
A. 가능은 하지만 기존 값 덮어쓰기와 연관관계 손실 위험이 있어 주의해야 한다.

Q. Controller에서 Entity를 반환하면 왜 Detached 문제가 생겨?
A. Service Transaction이 끝난 뒤 Entity가 Detached 상태가 될 수 있고 Lazy Field 접근 시 예외가 발생할 수 있다.

Q. Detached 문제를 피하는 기본 방식은 뭐야?
A. Service Transaction 안에서 Entity를 조회하고 DTO로 변환해 반환하는 방식이다.

---

# 8. Bulk Query and Persistence Context

## 8.1 Bulk Query Concept

### [개념]

Bulk Query는 여러 Row를 한 번에 UPDATE 또는 DELETE하는 Query다.

JPQL Bulk Query나 Native Bulk Query는 Persistence Context를 우회해서 DB에 직접 실행될 수 있다.

---

### [핵심]

핵심 키워드:

- Bulk Update
- Bulk Delete
- JPQL Bulk Query
- Native Query
- Persistence Context Bypass
- Dirty Checking Bypass
- Stale Entity
- flush
- clear

Bulk Query 특징:

- 여러 Row 한 번에 처리
- Dirty Checking 사용 안 함
- Persistence Context 우회 가능
- Managed Entity 상태와 DB 상태 불일치 가능
- 실행 전 Flush / 실행 후 Clear 검토

---

### [실무]

Bulk Update 예시:

```java
@Modifying(clearAutomatically = true, flushAutomatically = true)
@Query("""
    update Post p
    set p.deleted = true
    where p.user.userId = :userId
""")
int softDeleteByUserId(Long userId);
```

문제 흐름:

```text
Post Entity 조회
→ Persistence Context에 Managed 상태
→ Bulk Update로 DB 직접 변경
→ Persistence Context의 Post 상태는 이전 값
→ Stale Entity 문제 가능
```

권장:

- Bulk Query 실행 전 Flush 검토
- Bulk Query 실행 후 Clear 검토
- `@Modifying(clearAutomatically = true, flushAutomatically = true)` 검토
- Bulk Query 후 같은 Transaction에서 Managed Entity 재사용 주의
- 대량 작업은 별도 Transaction 분리 검토

주의:

- Bulk Query는 Dirty Checking을 거치지 않는다.
- Entity Lifecycle 이벤트가 기대대로 동작하지 않을 수 있다.
- Auditing 자동 갱신이 적용되지 않을 수 있다.
- Persistence Context와 DB 상태가 달라질 수 있다.
- Bulk Query는 SQL 로그와 영향 Row 수를 확인해야 한다.

---

### [FAQ]

Q. Bulk Update는 Dirty Checking이야?
A. 아니다. Bulk Query는 Entity 변경 감지를 거치지 않고 DB에 직접 실행될 수 있다.

Q. Bulk Query 후 clear가 필요한 이유는 뭐야?
A. Persistence Context에 남은 Managed Entity 상태가 DB와 달라질 수 있기 때문이다.

Q. `@Modifying`은 언제 써?
A. Repository `@Query`로 UPDATE나 DELETE를 실행할 때 사용한다.

Q. Bulk Query는 언제 사용해?
A. 여러 Row를 한 번에 수정하거나 삭제해야 할 때 사용하지만 Persistence Context 불일치를 주의해야 한다.

---

## 8.2 Bulk Query Review Rule

### [개념]

Bulk Query Review Rule은 대량 UPDATE / DELETE Query가 Persistence Context와 Data Integrity에 문제를 만들지 않는지 검수하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] Bulk Query가 정말 필요한가?
- [ ] Dirty Checking으로 처리 가능한 소량 변경인가?
- [ ] @Modifying이 있는가?
- [ ] flushAutomatically가 필요한가?
- [ ] clearAutomatically가 필요한가?
- [ ] Bulk Query 후 Managed Entity를 재사용하지 않는가?
- [ ] Auditing 자동 갱신 누락 가능성을 검토했는가?
- [ ] Entity Lifecycle 이벤트 누락 가능성을 검토했는가?
- [ ] 영향 Row 수를 확인하는가?
- [ ] Transaction 범위가 적절한가?
```

---

### [실무]

Review Finding:

```text
문제: Bulk Update 후 같은 Transaction에서 기존 Entity 사용
위험: Persistence Context와 DB 상태 불일치
해결: clearAutomatically 적용 또는 Transaction 분리

문제: @Modifying 누락
위험: UPDATE / DELETE Query 실행 오류
해결: @Modifying 추가

문제: Auditing 기대
위험: updatedAt 자동 갱신 누락 가능
해결: Query에서 updatedAt 직접 갱신 또는 Entity 변경 방식 사용
```

권장 예시:

```java
@Modifying(clearAutomatically = true, flushAutomatically = true)
@Query("""
    update Notification n
    set n.readStatus = true
    where n.user.userId = :userId
""")
int markAllAsRead(Long userId);
```

권장:

- Bulk Query는 명확한 목적이 있을 때만 사용
- 영향 Row 수 반환값 확인
- Transaction 범위 명확화
- Persistence Context 불일치 방지
- Auditing / Event 누락 여부 확인

주의:

- Bulk Query는 편하지만 JPA Entity 상태 관리와 분리된다.
- 복잡한 조건 Bulk Update는 QueryDSL 또는 Native Query 검토 가능
- 대량 처리에서 Lock과 Transaction 시간을 주의한다.
- Soft Delete Bulk Update는 조회 조건 누락을 함께 검토해야 한다.

---

### [FAQ]

Q. Bulk Query 검수에서 가장 중요한 것은 뭐야?
A. Persistence Context와 DB 상태 불일치 가능성을 확인하는 것이다.

Q. Bulk Query 후 같은 Entity를 계속 쓰면 안 돼?
A. DB 상태와 Managed Entity 상태가 달라질 수 있어 clear 또는 재조회가 필요할 수 있다.

Q. Bulk Query에서 Auditing이 자동 적용돼?
A. 기대하지 않는 것이 좋다. 필요한 값은 Query에서 직접 갱신하거나 Entity 변경 방식을 사용한다.

Q. Bulk Query는 QueryDSL로도 할 수 있어?
A. 가능하다. 다만 Persistence Context 우회 문제는 동일하게 검토해야 한다.

---

# 9. Persistence Context Review

## 9.1 Persistence Context Checklist

### [개념]

Persistence Context Checklist는 Entity 상태, Dirty Checking, Flush, Detached Entity, Bulk Query 문제가 없는지 검수하는 기준이다.

Review Agent는 수정 API와 조회 API에서 Transaction 범위와 Entity 상태를 우선 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Service Method에 Transaction 범위가 명확한가?
- [ ] 조회 Method는 readOnly Transaction을 사용하는가?
- [ ] 수정 Method는 일반 Transaction을 사용하는가?
- [ ] Entity가 Managed 상태에서 변경되는가?
- [ ] Detached Entity를 수정하지 않는가?
- [ ] RequestBody로 Entity를 직접 받지 않는가?
- [ ] Entity를 Controller에 직접 반환하지 않는가?
- [ ] update 후 불필요한 save를 반복하지 않는가?
- [ ] Entity 상태 변경 Method를 사용하는가?
- [ ] Dirty Checking 동작 조건을 만족하는가?
- [ ] Flush와 Commit 차이를 고려했는가?
- [ ] JPQL 전 Auto Flush 가능성을 고려했는가?
- [ ] Rollback 대상 예외 기준이 명확한가?
- [ ] merge를 update처럼 남용하지 않는가?
- [ ] Bulk Query 후 Persistence Context clear를 검토했는가?
- [ ] SQL 로그로 INSERT / UPDATE / DELETE를 확인했는가?
```

---

### [실무]

Review Flow:

```text
API Method 확인
→ Transaction Annotation 확인
→ Entity 조회 위치 확인
→ Entity 상태 확인
→ 변경 Method 확인
→ Dirty Checking 가능 여부 확인
→ Flush / Commit 시점 확인
→ Detached 전달 여부 확인
→ Bulk Query 여부 확인
→ SQL 로그 확인
```

Common Review Findings:

```text
문제: 수정 Service에 @Transactional 없음
위험: Dirty Checking 미동작
해결: Service public method에 @Transactional 추가

문제: @Transactional(readOnly = true)에서 Entity 수정
위험: 변경 반영 기대 불가
해결: 수정 Method는 일반 @Transactional 사용

문제: Controller에서 Entity 반환
위험: Detached Entity, LazyInitializationException, API 결합
해결: Service Transaction 안에서 DTO 변환

문제: merge로 수정 처리
위험: null 덮어쓰기, 연관관계 손실
해결: Transaction 안에서 조회 후 Dirty Checking

문제: Bulk Update 후 Entity 재사용
위험: Persistence Context와 DB 상태 불일치
해결: clearAutomatically 또는 재조회
```

---

### [FAQ]

Q. Persistence Context 검수에서 가장 먼저 확인할 것은 뭐야?
A. Transaction 범위와 Entity가 Managed 상태에서 변경되는지 먼저 확인한다.

Q. 수정 API에서 `@Transactional`이 없으면 왜 문제야?
A. Persistence Context와 Dirty Checking이 정상 동작하지 않아 변경 반영이 실패할 수 있다.

Q. Entity 직접 반환은 Persistence Context 관점에서 왜 위험해?
A. Transaction 종료 후 Detached 상태가 될 수 있고 Lazy Loading 예외와 API 결합 문제가 생길 수 있다.

Q. Bulk Query 검수는 왜 Persistence Context와 연결돼?
A. Bulk Query는 Persistence Context를 우회해 DB를 직접 수정할 수 있어 Managed Entity 상태와 불일치가 생길 수 있기 때문이다.

---

# 10. Common Mistakes

## 10.1 Persistence Context Common Mistakes

### [개념]

Persistence Context Common Mistakes는 Entity 상태 관리, Dirty Checking, Flush, Transaction, merge, Bulk Query에서 자주 발생하는 JPA 오류다.

---

### [핵심]

자주 발생하는 실수:

- Persistence Context를 DB로 오해
- Transaction 없이 Entity 수정
- Detached Entity 수정 후 DB 반영 기대
- `@Transactional(readOnly = true)`에서 변경 작업 수행
- 수정 API에서 RequestBody Entity 수신
- Detached Entity를 그대로 save / merge
- Dirty Checking 후 불필요한 save 반복
- Flush와 Commit을 같은 것으로 오해
- Flush 후 Rollback 불가능하다고 오해
- JPQL 전 Auto Flush를 모름
- merge를 update로 오해
- Bulk Query 후 Persistence Context clear 누락
- Bulk Query가 Dirty Checking을 탄다고 오해
- Controller에서 Entity 반환
- DTO 변환을 Transaction 밖에서 수행
- Lazy Field를 Transaction 밖에서 접근
- SQL 로그 확인 안 함

---

### [실무]

Anti Pattern 예시:

```java
public void updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId).orElseThrow();
    post.update(request.title(), request.content());
}
```

문제:

```text
@Transactional 없음
→ Entity 상태 관리 불명확
→ Dirty Checking 미동작 가능
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
@Transactional
public void updateUser(@RequestBody User user) {
    userRepository.save(user);
}
```

문제:

```text
RequestBody Entity 직접 수신
Detached Entity save
null 덮어쓰기 위험
연관관계 손실 위험
API와 Entity 결합
```

개선:

```java
@Transactional
public void updateUser(Long userId, UserUpdateRequest request) {
    User user = userRepository.findById(userId).orElseThrow();
    user.updateNickname(request.nickname());
}
```

Review 기준:

```text
Update API
→ @Transactional 확인
→ findById 확인
→ Entity Method 확인
→ Dirty Checking 확인
→ save / merge 남용 확인
```

---

### [FAQ]

Q. Persistence Context에서 가장 흔한 실수는 뭐야?
A. Transaction 밖 Detached Entity를 수정하고 DB에 반영될 것으로 기대하는 것이다.

Q. Dirty Checking에서 가장 흔한 실수는 뭐야?
A. `@Transactional` 없이 Entity를 수정하거나 readOnly Transaction에서 변경하는 것이다.

Q. Flush에서 가장 흔한 오해는 뭐야?
A. Flush를 Commit과 같은 것으로 오해하는 것이다.

Q. merge에서 가장 흔한 오해는 뭐야?
A. merge를 단순 update 기능으로 생각하고 Detached Entity를 그대로 병합하는 것이다.

---

# 11. Part04 Final Goal

## 11.1 Agent Output Goal

### [개념]

JPA Advanced Part04의 최종 목적은 Agent가 Persistence Context, Entity Lifecycle, Dirty Checking, Flush, Commit, Rollback, Detached Entity를 기준으로 안전한 Entity 상태 변경 로직을 설계하도록 만드는 것이다.

Part04는 SQL Foundation의 INSERT / UPDATE / DELETE / Transaction 개념과 JPA Entity 상태 관리를 연결한다.

---

### [핵심]

Agent가 수행해야 할 작업:

- Persistence Context 이해
- EntityManager 역할 구분
- First Level Cache 이해
- Entity Identity 판단
- Entity Lifecycle 구분
- Transient / Managed / Detached / Removed 판단
- Dirty Checking 적용
- 수정 API Dirty Checking Pattern 작성
- Flush와 Commit 차이 구분
- Rollback 기준 확인
- merge 남용 탐지
- Detached Entity Problem 탐지
- Bulk Query Persistence Context 불일치 검토
- Transaction 범위 검토
- SQL 로그로 INSERT / UPDATE / DELETE 확인

---

### [실무]

Agent 작업 흐름:

```text
User Update Request
→ Identify Transaction Boundary
→ Load Entity in Service
→ Confirm Managed State
→ Apply Entity Method
→ Dirty Checking
→ Flush
→ Commit
→ Check SQL UPDATE
```

Troubleshooting 흐름:

```text
Update Not Reflected
→ @Transactional 확인
→ readOnly 여부 확인
→ Managed / Detached 상태 확인
→ 변경 Method 호출 확인
→ Flush / Commit 확인
→ SQL 로그 확인
```

Part04 이후 연결:

```text
Part04 Persistence Context / Dirty Checking
→ Part05 Repository / JPQL / Native Query
→ Part06 Fetch Strategy / Fetch Join / N+1
→ Part07 Transaction / Cascade / Pagination
→ Part08 Troubleshooting / Anti Pattern
```

---

### [FAQ]

Q. JPA Advanced Part04의 목적은 뭐야?
A. Agent가 Persistence Context와 Dirty Checking을 이해하고 안전한 수정, 삭제, 상태 변경 로직을 설계하도록 만드는 것이다.

Q. Part04에서 가장 중요한 기준은 뭐야?
A. Managed Entity, Transaction 범위, Dirty Checking, Flush와 Commit 차이, Detached Entity 문제다.

Q. Part04는 SQL Foundation 어느 부분과 연결돼?
A. SQL Part03의 INSERT / UPDATE / DELETE와 SQL Part04의 Transaction 개념과 연결된다.

Q. Part04 다음에는 무엇을 다뤄?
A. Part05에서 Repository, Query Method, JPQL, Native Query, DTO Projection, QueryDSL 전환 기준을 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. Persistence Context는 뭐야?
A. JPA가 Entity를 관리하는 공간이며 1차 캐시, 동일성 보장, Dirty Checking, Flush 같은 기능을 제공한다.

Q. Persistence Context는 DB야?
A. 아니다. DB가 아니라 JPA가 Transaction 안에서 Entity 상태를 관리하는 메모리 공간이다.

Q. EntityManager는 뭐야?
A. Entity를 Persistence Context를 통해 저장, 조회, 수정, 삭제하는 JPA 핵심 API다.

Q. Repository를 쓰면 EntityManager를 몰라도 돼?
A. 기본 CRUD는 Repository로 충분하지만 Dirty Checking, Flush, Detached 문제를 이해하려면 EntityManager 개념이 필요하다.

Q. First Level Cache는 뭐야?
A. Persistence Context 내부의 Entity 캐시이며 같은 Transaction 안에서 같은 ID Entity 재조회 시 활용될 수 있다.

Q. 1차 캐시는 Application 전체에서 공유돼?
A. 아니다. 보통 Transaction / Persistence Context 범위 안에서만 유효하다.

Q. 같은 ID로 두 번 조회하면 SQL이 한 번만 나가?
A. 상황에 따라 1차 캐시가 동작하면 두 번째 조회는 DB SELECT 없이 Entity를 반환할 수 있다.

Q. Entity Identity는 뭐야?
A. DB Primary Key를 기준으로 Entity를 식별하는 개념이다.

Q. 같은 ID Entity는 항상 같은 객체야?
A. 아니다. 같은 Persistence Context 안에서는 같을 수 있지만 Transaction 범위 밖에서는 다른 객체일 수 있다.

Q. Entity Lifecycle은 뭐야?
A. Entity가 JPA에서 Transient, Managed, Detached, Removed 상태로 관리되는 흐름이다.

Q. Transient Entity는 뭐야?
A. JPA가 아직 관리하지 않는 새 Entity 객체다.

Q. Managed Entity는 뭐야?
A. Persistence Context가 관리하는 Entity이며 Dirty Checking과 Flush 대상이 될 수 있다.

Q. Detached Entity는 뭐야?
A. 한때 Persistence Context가 관리했지만 현재는 분리되어 JPA가 변경을 추적하지 않는 Entity다.

Q. Removed Entity는 뭐야?
A. 삭제 대상으로 표시된 Entity이며 Flush 시 DELETE SQL이 실행될 수 있다.

Q. new로 만든 Entity는 바로 DB에 저장돼?
A. 아니다. new Entity는 Transient 상태이며 persist 또는 save가 필요하다.

Q. save하면 Entity는 Managed 상태가 돼?
A. Transaction 안에서 저장된 Entity는 Managed 상태가 될 수 있다.

Q. Dirty Checking은 뭐야?
A. Transaction 안에서 Managed Entity의 변경을 감지해 Flush 시 UPDATE SQL을 생성하는 기능이다.

Q. Dirty Checking이 동작하려면 무엇이 필요해?
A. Managed Entity, Transaction 범위, Snapshot, Flush 시점이 필요하다.

Q. JPA update 할 때 save를 꼭 해야 해?
A. Transaction 안에서 조회한 Managed Entity를 변경하면 Dirty Checking으로 반영될 수 있어 save가 필수는 아니다.

Q. Dirty Checking은 Detached Entity에도 동작해?
A. 아니다. Detached Entity는 Persistence Context가 관리하지 않으므로 Dirty Checking 대상이 아니다.

Q. 수정 API에서 가장 안전한 JPA 패턴은 뭐야?
A. Transaction 안에서 Entity를 조회한 뒤 Entity 상태 변경 Method를 호출하는 방식이다.

Q. update 후 `repository.save(entity)`를 다시 호출해야 해?
A. Managed Entity라면 필수는 아니다. 신규 저장과 Detached Entity 상황은 구분해야 한다.

Q. RequestBody Entity를 save하는 방식은 왜 위험해?
A. 기존 값 덮어쓰기, 연관관계 손실, 보안 문제, API와 Entity 결합 위험이 있다.

Q. Dirty Checking이 안 되면 뭘 먼저 확인해?
A. `@Transactional`, Entity Managed 상태, readOnly 설정, 변경 Method 호출 여부, SQL UPDATE 로그를 확인한다.

Q. `readOnly = true`에서 수정하면 반영돼?
A. 기대하지 않는 것이 좋다. 변경 작업은 일반 `@Transactional`에서 수행해야 한다.

Q. Flush는 뭐야?
A. Persistence Context의 변경 내용을 DB에 SQL로 반영하는 과정이다.

Q. Flush와 Commit은 같은 거야?
A. 아니다. Flush는 SQL을 DB에 보내는 과정이고 Commit은 Transaction을 확정하는 과정이다.

Q. Flush하면 Rollback이 안 돼?
A. 아니다. Flush 후에도 Transaction이 Commit되지 않았다면 Rollback 가능하다.

Q. Flush는 언제 발생해?
A. Transaction Commit 전, JPQL 실행 전, 명시적 `flush()` 호출 시 발생할 수 있다.

Q. JPQL 전에 Flush가 일어나는 이유는 뭐야?
A. Query 결과가 Persistence Context의 변경 내용과 일치하도록 하기 위해 Flush가 발생할 수 있다.

Q. SELECT Query인데 UPDATE SQL이 먼저 나갈 수 있어?
A. 가능하다. 이전에 변경된 Managed Entity가 있으면 JPQL 실행 전 Flush가 발생할 수 있다.

Q. Commit은 뭐야?
A. Transaction의 변경 내용을 최종 확정하는 과정이다.

Q. Commit 전에 Flush가 발생해?
A. 일반적으로 Commit 전에 Flush가 발생해 Persistence Context 변경 내용을 DB에 SQL로 반영한다.

Q. Rollback은 뭐야?
A. Transaction 중 발생한 변경을 취소하는 과정이다.

Q. Flush 후에도 Rollback돼?
A. Commit 전이면 Flush로 SQL이 나갔더라도 Rollback으로 취소할 수 있다.

Q. 모든 Exception에서 Rollback돼?
A. 아니다. 기본적으로 RuntimeException과 Error는 Rollback되지만 CheckedException은 기본 Rollback 대상이 아니다.

Q. merge는 뭐야?
A. Detached Entity의 값을 Managed Entity에 복사하는 JPA 기능이다.

Q. merge하면 전달한 Entity가 Managed가 돼?
A. 아니다. merge는 Managed 복사본을 반환하며 전달한 Entity 자체는 Detached 상태다.

Q. 수정 API에서 merge를 쓰는 게 좋아?
A. 일반적으로 권장하지 않는다. Transaction 안에서 Entity를 조회한 뒤 Dirty Checking으로 수정하는 방식이 안전하다.

Q. merge가 위험한 이유는 뭐야?
A. null 값 덮어쓰기, 연관관계 손실, 변경 의도 불명확 문제가 생길 수 있다.

Q. Detached Entity Problem은 뭐야?
A. Persistence Context가 관리하지 않는 Entity를 수정하거나 사용해 변경 반영 실패나 Lazy Loading 예외가 발생하는 문제다.

Q. Detached Entity를 그대로 save하면 안 돼?
A. 가능은 하지만 기존 값 덮어쓰기와 연관관계 손실 위험이 있어 주의해야 한다.

Q. Controller에서 Entity를 반환하면 왜 Detached 문제가 생겨?
A. Service Transaction이 끝난 뒤 Entity가 Detached 상태가 될 수 있고 Lazy Field 접근 시 예외가 발생할 수 있다.

Q. Detached 문제를 피하는 기본 방식은 뭐야?
A. Service Transaction 안에서 Entity를 조회하고 DTO로 변환해 반환하는 방식이다.

Q. Bulk Update는 Dirty Checking이야?
A. 아니다. Bulk Query는 Entity 변경 감지를 거치지 않고 DB에 직접 실행될 수 있다.

Q. Bulk Query 후 clear가 필요한 이유는 뭐야?
A. Persistence Context에 남은 Managed Entity 상태가 DB와 달라질 수 있기 때문이다.

Q. `@Modifying`은 언제 써?
A. Repository `@Query`로 UPDATE나 DELETE를 실행할 때 사용한다.

Q. Bulk Query 검수에서 가장 중요한 것은 뭐야?
A. Persistence Context와 DB 상태 불일치 가능성을 확인하는 것이다.

Q. Bulk Query에서 Auditing이 자동 적용돼?
A. 기대하지 않는 것이 좋다. 필요한 값은 Query에서 직접 갱신하거나 Entity 변경 방식을 사용한다.

Q. Persistence Context 검수에서 가장 먼저 확인할 것은 뭐야?
A. Transaction 범위와 Entity가 Managed 상태에서 변경되는지 먼저 확인한다.

Q. 수정 API에서 `@Transactional`이 없으면 왜 문제야?
A. Persistence Context와 Dirty Checking이 정상 동작하지 않아 변경 반영이 실패할 수 있다.

Q. Entity 직접 반환은 Persistence Context 관점에서 왜 위험해?
A. Transaction 종료 후 Detached 상태가 될 수 있고 Lazy Loading 예외와 API 결합 문제가 생길 수 있다.

Q. Persistence Context에서 가장 흔한 실수는 뭐야?
A. Transaction 밖 Detached Entity를 수정하고 DB에 반영될 것으로 기대하는 것이다.

Q. Dirty Checking에서 가장 흔한 실수는 뭐야?
A. `@Transactional` 없이 Entity를 수정하거나 readOnly Transaction에서 변경하는 것이다.

Q. Flush에서 가장 흔한 오해는 뭐야?
A. Flush를 Commit과 같은 것으로 오해하는 것이다.

Q. JPA Part04에서 가장 중요한 기준은 뭐야?
A. Managed Entity, Transaction 범위, Dirty Checking, Flush와 Commit 차이, Detached Entity 문제다.

Q. JPA Part04 다음에는 무엇을 다뤄?
A. Part05에서 Repository, Query Method, JPQL, Native Query, DTO Projection, QueryDSL 전환 기준을 다룬다.
