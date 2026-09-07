# JPA Advanced Part06 — Fetch Strategy, Fetch Join, N+1

---

# 1. Fetch Strategy Purpose

## 1.1 Fetch Strategy Concept

### [개념]

Fetch Strategy는 JPA Association Entity를 언제 조회할지 결정하는 전략이다.

JPA는 연관 Entity를 즉시 조회하거나, 실제 접근 시점까지 조회를 지연할 수 있다.

Fetch Strategy는 Lazy Loading, Eager Loading, Fetch Join, N+1 Problem, LazyInitializationException과 직접 연결된다.

---

### [핵심]

핵심 키워드:

- Fetch Strategy
- Lazy Loading
- Eager Loading
- FetchType.LAZY
- FetchType.EAGER
- Proxy
- Persistence Context
- Transaction
- Fetch Join
- N+1 Problem
- LazyInitializationException
- DTO Projection

Fetch Strategy 기준:

```text
Entity Association Mapping
→ FetchType 결정
→ Repository Query 실행
→ Persistence Context 관리
→ 연관 Entity 접근
→ 추가 Query 또는 Fetch Join 결과 사용
```

---

### [실무]

SQL Foundation 연결:

```text
SQL JOIN
→ JPQL Join / Fetch Join

SQL SELECT 반복
→ N+1 Problem

SQL Query Count
→ Fetch Strategy Review

SQL Pagination
→ Collection Fetch Join Caution
```

JPA 실무 기준:

```text
Association Mapping
→ 기본 Fetch 확인
→ LAZY 우선 전략 적용
→ API Query 요구사항 확인
→ 연관 Entity 필요 여부 판단
→ Fetch Join / DTO Projection / Batch Size 선택
→ SQL 로그 확인
→ N+1 여부 검수
```

권장:

- 기본은 LAZY 우선 전략
- `ManyToOne`, `OneToOne`은 기본 EAGER이므로 LAZY 명시 검토
- 필요한 조회에서 Fetch Join 적용
- 목록 Read-only 조회는 DTO Projection 검토
- SQL 로그로 실제 Query 수 확인
- Fetch Strategy는 API별 조회 요구사항과 함께 결정

주의:

- LAZY는 N+1 문제를 자동으로 해결하지 않는다.
- EAGER는 N+1 문제를 없애는 만능 해결책이 아니다.
- Fetch Join은 필요한 Query에만 적용한다.
- Collection Fetch Join과 Pagination 조합은 위험하다.
- Entity를 API Response로 직접 반환하면 Lazy Loading 문제가 커진다.

---

### [FAQ]

Q. Fetch Strategy는 뭐야?
A. JPA Association Entity를 언제 조회할지 결정하는 전략이다.

Q. Fetch Strategy가 중요한 이유는 뭐야?
A. 연관 Entity 조회 시점, SQL Query 수, N+1 문제, LazyInitializationException에 직접 영향을 주기 때문이다.

Q. JPA에서 기본 Fetch 전략을 그대로 믿어도 돼?
A. 권장하지 않는다. `ManyToOne`, `OneToOne`은 기본 EAGER라 LAZY 명시를 검토해야 한다.

Q. Fetch Strategy는 어디서 확인해야 해?
A. Entity Association Mapping, Repository Query, DTO 변환 위치, SQL 로그를 함께 확인해야 한다.

---

## 1.2 Default Fetch Type

### [개념]

Default Fetch Type은 JPA Association Annotation별 기본 조회 전략이다.

JPA 기본값은 실무 성능 기준과 다를 수 있으므로 명시적으로 FetchType을 설정하는 것이 좋다.

---

### [핵심]

기본 Fetch Type:

| Association   | Default Fetch | 실무 권장      |
| ------------- | ------------- | -------------- |
| `@ManyToOne`  | EAGER         | LAZY 명시      |
| `@OneToOne`   | EAGER         | LAZY 명시 검토 |
| `@OneToMany`  | LAZY          | 기본 LAZY 유지 |
| `@ManyToMany` | LAZY          | 직접 사용 지양 |

핵심 키워드:

- Default Fetch
- FetchType.LAZY
- FetchType.EAGER
- ManyToOne EAGER Caution
- OneToOne EAGER Caution
- Explicit Fetch Type

---

### [실무]

권장 Mapping:

```java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "user_id", nullable = false)
private User user;
```

```java
@OneToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "profile_id")
private UserProfile profile;
```

```java
@OneToMany(mappedBy = "post")
private List<Comment> comments = new ArrayList<>();
```

Review 기준:

```text
Association 확인
→ Default Fetch 확인
→ ManyToOne / OneToOne EAGER 여부 확인
→ LAZY 명시 여부 확인
→ Query별 Fetch Join 필요성 별도 판단
```

권장:

- `ManyToOne`은 LAZY 명시
- `OneToOne`은 LAZY 명시 후 실제 SQL 확인
- `OneToMany`는 기본 LAZY 유지
- `ManyToMany` 직접 사용은 피하고 Middle Entity 설계
- FetchType은 Entity Mapping 기본 정책이고, 실제 조회 최적화는 Query에서 결정

주의:

- EAGER는 예상치 못한 Join이나 추가 Query를 만들 수 있다.
- LAZY로 바꿔도 DTO 변환 중 연관 Field를 반복 접근하면 N+1이 발생할 수 있다.
- `OneToOne` LAZY는 상황에 따라 기대대로 동작하지 않을 수 있다.
- FetchType은 API 응답 구조를 대신하지 않는다.
- Entity 직접 반환은 Fetch 전략 문제를 악화시킨다.

---

### [FAQ]

Q. `ManyToOne` 기본 Fetch는 뭐야?
A. 기본값은 EAGER다. 실무에서는 `fetch = FetchType.LAZY`를 명시하는 것이 좋다.

Q. `OneToMany` 기본 Fetch는 뭐야?
A. 기본값은 LAZY다.

Q. EAGER가 기본이면 그냥 둬도 돼?
A. 권장하지 않는다. 불필요한 조회와 성능 문제를 만들 수 있어 LAZY 명시를 검토해야 한다.

Q. FetchType을 LAZY로 하면 모든 성능 문제가 해결돼?
A. 아니다. LAZY는 조회 시점을 늦출 뿐이고 N+1 문제는 별도 Query 전략으로 해결해야 한다.

---

# 2. Lazy Loading

## 2.1 Lazy Loading Concept

### [개념]

Lazy Loading은 연관 Entity를 실제 사용하는 시점에 조회하는 전략이다.

JPA는 Lazy Association에 Proxy를 두고, 연관 Field에 접근할 때 필요한 SQL을 실행할 수 있다.

---

### [핵심]

핵심 키워드:

- Lazy Loading
- FetchType.LAZY
- Proxy
- Persistence Context
- Transaction
- LazyInitializationException
- N+1 Problem
- Association Getter
- DTO Mapping

동작 흐름:

```text
Post 조회
→ Post.user는 Proxy 또는 미초기화 상태
→ post.getUser().getNickname() 접근
→ Persistence Context 확인
→ User SELECT 실행 가능
```

---

### [실무]

Mapping 예시:

```java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "user_id", nullable = false)
private User user;
```

문제 발생 예시:

```java
List<Post> posts = postRepository.findAll();

for (Post post : posts) {
    String nickname = post.getUser().getNickname();
}
```

SQL 흐름:

```text
Post 목록 조회 1번
→ 각 Post의 User 접근
→ User 조회 N번
→ 총 1 + N Query 발생
```

권장:

- 기본 Association은 LAZY 우선
- 연관 Entity가 필요한 Query는 Fetch Join 검토
- 목록 Read-only 조회는 DTO Projection 검토
- DTO 변환은 Service Transaction 안에서 처리
- SQL 로그로 Lazy Query 발생 시점 확인

주의:

- LAZY는 추가 Query 발생을 지연할 뿐 제거하지 않는다.
- Transaction 밖 Lazy 접근은 LazyInitializationException을 만들 수 있다.
- DTO 변환 중 Lazy Field 접근으로 N+1이 발생할 수 있다.
- JSON 직렬화 중 Lazy Field 접근은 위험하다.
- Entity를 Response로 직접 반환하지 않는다.

---

### [FAQ]

Q. Lazy Loading은 뭐야?
A. 연관 Entity를 실제 사용하는 시점에 조회하는 전략이다.

Q. LAZY는 무조건 좋아?
A. 아니다. 불필요한 즉시 조회를 줄이지만 잘못 사용하면 N+1이나 LazyInitializationException이 발생할 수 있다.

Q. LAZY에서 SQL은 언제 실행돼?
A. Lazy Association Field에 실제 접근할 때 추가 SELECT가 실행될 수 있다.

Q. LAZY로 하면 N+1이 없어져?
A. 아니다. 반복문에서 Lazy Association을 접근하면 N+1이 발생할 수 있다.

---

## 2.2 Proxy and Initialization

### [개념]

Proxy는 Lazy Loading을 위해 JPA Provider가 실제 Entity 대신 사용하는 대리 객체다.

Proxy는 연관 Entity 접근 시점에 초기화되며, 초기화에는 Persistence Context와 Transaction 범위가 필요하다.

---

### [핵심]

핵심 키워드:

- Proxy
- Lazy Proxy
- Initialization
- Hibernate Proxy
- Persistence Context
- Managed Entity
- Lazy Field Access
- Entity Reference
- Transaction Boundary

Proxy 흐름:

```text
Entity 조회
→ Lazy Association Proxy 설정
→ Association Field 접근
→ Proxy 초기화
→ SQL SELECT 실행
→ 실제 Entity 데이터 사용
```

---

### [실무]

예시:

```java
@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    String nickname = post.getUser().getNickname();

    return new PostResponse(post.getPostId(), post.getTitle(), nickname);
}
```

해석:

```text
postRepository.findById
→ Post 조회

post.getUser()
→ User Proxy 접근

getNickname()
→ Proxy 초기화
→ User SELECT 가능
```

권장:

- Proxy 초기화 위치를 Service Transaction 안으로 제한
- DTO 변환 시 연관 Field 접근을 의도적으로 처리
- 필요한 연관 Entity는 Fetch Join으로 미리 조회
- Proxy 객체를 Controller / Response로 노출하지 않음
- toString / equals / hashCode에서 Lazy Association 접근 금지

주의:

- Proxy 초기화 전 EntityManager가 닫히면 LazyInitializationException 발생 가능
- Proxy Class는 실제 Entity Class와 다를 수 있다.
- Lombok `@ToString`이 Lazy Association을 건드릴 수 있다.
- `equals`, `hashCode`에 Association을 포함하면 Proxy 초기화 문제가 생길 수 있다.
- Debugger에서 Field를 펼치는 것만으로 Lazy Loading이 발생할 수 있다.

---

### [FAQ]

Q. Proxy는 뭐야?
A. Lazy Loading을 위해 실제 Entity 대신 사용되는 대리 객체다.

Q. Proxy는 언제 초기화돼?
A. Lazy Association Field의 실제 값에 접근할 때 초기화될 수 있다.

Q. Proxy 초기화에는 Transaction이 필요해?
A. Persistence Context가 열려 있어야 하며 일반적으로 Transaction 범위 안에서 안전하다.

Q. toString에서 Lazy Field를 출력해도 돼?
A. 권장하지 않는다. Proxy 초기화와 N+1, 순환 참조 문제가 발생할 수 있다.

---

## 2.3 LazyInitializationException

### [개념]

LazyInitializationException은 Persistence Context가 닫힌 뒤 Lazy Association에 접근할 때 발생하는 예외다.

주로 Service Transaction 종료 후 Controller, JSON 직렬화, View Rendering, DTO 변환 중 발생한다.

---

### [핵심]

핵심 키워드:

- LazyInitializationException
- Lazy Loading
- Closed Persistence Context
- Transaction Boundary
- Detached Entity
- DTO Mapping
- Entity Direct Return
- OSIV Caution

발생 흐름:

```text
Service Transaction 시작
→ Entity 조회
→ Transaction 종료
→ Entity Detached
→ Controller에서 Lazy Field 접근
→ LazyInitializationException 발생
```

---

### [실무]

문제 예시:

```java
@GetMapping("/{id}")
public Post getPost(@PathVariable Long id) {
    return postService.getPostEntity(id);
}
```

문제 흐름:

```text
Entity 직접 반환
→ JSON 직렬화 중 post.user 접근
→ Transaction 종료 상태
→ LazyInitializationException 가능
```

권장 예시:

```java
@GetMapping("/{id}")
public PostResponse getPost(@PathVariable Long id) {
    return postService.getPost(id);
}
```

Service:

```java
@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    Post post = postRepository.findByIdWithUser(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    return PostResponse.from(post);
}
```

Repository:

```java
@Query("""
    select p
    from Post p
    join fetch p.user
    where p.postId = :postId
""")
Optional<Post> findByIdWithUser(Long postId);
```

권장 해결:

- Service Transaction 안에서 DTO 변환
- 필요한 연관 Entity를 Fetch Join으로 조회
- DTO Projection 사용
- Entity 직접 반환 금지
- OSIV 의존 지양

주의:

- EAGER로 바꾸는 것은 근본 해결이 아니다.
- OSIV를 켜두면 예외가 늦게 드러나지만 성능 문제가 숨겨질 수 있다.
- Controller에서 Lazy Field 접근을 피한다.
- View / JSON 직렬화에 Entity를 넘기지 않는다.
- 해결 후 SQL Query 수를 확인해야 한다.

---

### [FAQ]

Q. LazyInitializationException은 왜 발생해?
A. Persistence Context가 닫힌 뒤 Lazy Association에 접근했기 때문이다.

Q. LazyInitializationException은 어떻게 해결해?
A. Service Transaction 안에서 DTO 변환하거나 필요한 연관 Entity를 Fetch Join / DTO Projection으로 조회한다.

Q. EAGER로 바꾸면 해결돼?
A. 권장하지 않는다. 불필요한 조회와 N+1 문제가 생길 수 있어 Fetch Join이나 DTO Projection을 우선 검토한다.

Q. Entity 직접 반환이 왜 위험해?
A. JSON 직렬화 중 Lazy Field 접근으로 LazyInitializationException과 순환 참조 문제가 발생할 수 있다.

---

# 3. Eager Loading

## 3.1 Eager Loading Concept

### [개념]

Eager Loading은 Entity 조회 시 연관 Entity를 즉시 함께 조회하는 전략이다.

JPA 기본 Fetch가 EAGER인 Association은 Entity 조회 시 예상보다 많은 데이터를 조회할 수 있다.

---

### [핵심]

핵심 키워드:

- Eager Loading
- FetchType.EAGER
- Immediate Loading
- ManyToOne Default EAGER
- OneToOne Default EAGER
- Unexpected Join
- Additional Select
- N+1 Problem
- Performance Caution

EAGER 문제:

- 불필요한 데이터 조회
- 예상치 못한 Join
- 추가 SELECT 발생 가능
- Query 제어 어려움
- N+1 발생 가능
- 복잡한 SQL 생성
- API별 최적화 어려움

---

### [실무]

비권장 예시:

```java
@ManyToOne
@JoinColumn(name = "user_id")
private User user;
```

문제:

```text
@ManyToOne 기본 FetchType.EAGER
→ Post 조회 시 User도 즉시 조회 가능
→ 목록 조회에서 불필요한 Query 증가
```

권장 예시:

```java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "user_id", nullable = false)
private User user;
```

실무 기준:

```text
Entity Mapping
→ LAZY 기본 설계

API Query
→ 필요한 연관 Entity만 Fetch Join / Projection으로 조회
```

권장:

- EAGER 기본값에 의존하지 않음
- `ManyToOne`, `OneToOne`은 LAZY 명시 검토
- 조회 요구사항은 Repository Query에서 해결
- 필요한 API에만 Fetch Join 적용
- SQL 로그로 즉시 조회 여부 확인

주의:

- EAGER도 N+1을 만들 수 있다.
- EAGER는 연관 Entity 조회를 끄기 어렵다.
- 모든 API에서 동일하게 연관 Entity를 가져오는 것은 비효율적이다.
- EAGER는 Entity Mapping에 박혀 Query별 최적화를 어렵게 만든다.
- EAGER로 LazyInitializationException을 덮지 않는다.

---

### [FAQ]

Q. Eager Loading은 뭐야?
A. Entity 조회 시 연관 Entity를 즉시 함께 조회하는 전략이다.

Q. EAGER는 왜 위험해?
A. 불필요한 Join과 추가 조회가 발생하고 Query별 성능 제어가 어려워질 수 있다.

Q. EAGER면 N+1 문제가 없어져?
A. 아니다. EAGER도 조회 방식에 따라 N+1 문제가 발생할 수 있다.

Q. EAGER는 언제 써도 돼?
A. 연관 Entity가 항상 함께 필요하고 데이터 크기가 작으며 성능 영향이 명확할 때 제한적으로 검토한다.

---

## 3.2 EAGER Anti Pattern

### [개념]

EAGER Anti Pattern은 LazyInitializationException이나 N+1 문제를 피하려고 Association을 EAGER로 바꾸는 잘못된 해결 방식이다.

EAGER는 조회 시점 제어를 어렵게 만들어 성능 문제를 숨기거나 확대할 수 있다.

---

### [핵심]

Anti Pattern 상황:

```text
LazyInitializationException 발생
→ FetchType.EAGER로 변경

N+1 발생
→ FetchType.EAGER로 변경

DTO 변환에서 Lazy Query 발생
→ 모든 Association EAGER 변경
```

문제:

- 모든 조회에서 연관 Entity 강제 로딩
- API별 최적화 불가
- 불필요한 Join 증가
- 예상치 못한 추가 SELECT
- 순환 연관관계에서 성능 악화
- Entity Graph 복잡도 증가

---

### [실무]

비권장 해결:

```java
@ManyToOne(fetch = FetchType.EAGER)
@JoinColumn(name = "user_id")
private User user;
```

권장 해결 후보:

```text
LazyInitializationException
→ Service Transaction 안에서 DTO 변환
→ Fetch Join
→ DTO Projection

N+1 Problem
→ Fetch Join
→ DTO Projection
→ Batch Size
→ Query 구조 변경

목록 Read-only 응답
→ DTO Projection
```

Review 기준:

```text
EAGER 발견
→ 기본값인지 명시인지 확인
→ 항상 필요한 연관 Entity인지 확인
→ Query 수 확인
→ LAZY + Query별 Fetch 전략으로 변경 가능 여부 검토
```

권장:

- EAGER 변경 전 SQL 로그 확인
- 문제 원인이 Lazy 접근 위치인지 N+1인지 구분
- Entity Mapping은 LAZY 중심
- Query별 Fetch Join / Projection으로 해결
- EAGER 사용 이유를 명확히 문서화

주의:

- EAGER는 문제를 해결하지 않고 숨길 수 있다.
- FetchType 변경은 전체 API 조회에 영향을 줄 수 있다.
- 연관관계가 많을수록 EAGER 폭발 위험이 커진다.
- 성능 문제는 SQL 로그 기반으로 검증한다.

---

### [FAQ]

Q. Lazy 예외가 나면 EAGER로 바꾸면 돼?
A. 권장하지 않는다. Service Transaction 안 DTO 변환, Fetch Join, DTO Projection을 우선 검토한다.

Q. N+1이 생기면 EAGER로 바꾸면 돼?
A. 권장하지 않는다. Fetch Join, DTO Projection, Batch Size, API 구조 변경 중 상황에 맞게 선택해야 한다.

Q. EAGER가 이미 있으면 무조건 제거해야 해?
A. 무조건은 아니지만 항상 필요한 관계인지, SQL 비용이 적절한지 검토해야 한다.

Q. EAGER Anti Pattern을 어떻게 찾을까?
A. Entity Association에서 FetchType.EAGER 또는 기본 EAGER를 확인하고 SQL 로그로 불필요한 조회를 확인한다.

---

# 4. N+1 Problem

## 4.1 N+1 Problem Concept

### [개념]

N+1 Problem은 목록 1번 조회 후 각 Row의 연관 Entity를 조회하기 위해 N번 추가 Query가 발생하는 문제다.

JPA에서 Lazy Loading, Eager Loading, DTO 변환, 반복문 내부 연관 Field 접근 중 자주 발생한다.

---

### [핵심]

핵심 키워드:

- N+1 Problem
- Query Count
- List Query
- Association Access
- Lazy Loading
- Eager Loading
- DTO Mapping
- Fetch Join
- DTO Projection
- Batch Size

발생 흐름:

```text
Post 목록 조회 1번
→ posts size = N
→ 각 Post의 User 접근
→ User 조회 N번
→ 총 1 + N Query
```

---

### [실무]

문제 예시:

```java
@Transactional(readOnly = true)
public List<PostResponse> getPosts() {
    return postRepository.findAll().stream()
            .map(post -> new PostResponse(
                    post.getPostId(),
                    post.getTitle(),
                    post.getUser().getNickname()
            ))
            .toList();
}
```

문제 SQL 흐름:

```text
select * from posts;
select * from users where user_id = ?;
select * from users where user_id = ?;
select * from users where user_id = ?;
...
```

SQL Foundation 연결:

```text
SQL SELECT 1번
→ 목록 조회

SQL SELECT N번
→ 연관 Entity 반복 조회

SQL Query Count Review
→ N+1 탐지
```

권장:

- 목록 API는 N+1 검토 필수
- DTO 변환 중 연관 Entity 접근 확인
- SQL 로그로 Query 수 확인
- 필요한 연관 Entity는 Fetch Join 검토
- 읽기 전용 목록은 DTO Projection 검토
- OneToMany는 Batch Size / 별도 Query / API 구조 변경 검토

주의:

- LAZY만 N+1을 만드는 것은 아니다.
- EAGER에서도 Query 방식에 따라 N+1이 발생할 수 있다.
- N+1은 데이터가 적을 때는 잘 드러나지 않는다.
- 운영 데이터 증가 시 급격한 성능 저하를 만든다.
- 단순히 Fetch Join을 남용하면 다른 성능 문제가 생길 수 있다.

---

### [FAQ]

Q. N+1 문제는 뭐야?
A. 목록 1번 조회 후 각 Row의 연관 Entity를 조회하기 위해 N번 추가 Query가 발생하는 문제다.

Q. N+1은 언제 자주 생겨?
A. 목록 조회 후 반복문이나 DTO 변환 과정에서 연관 Entity getter를 호출할 때 자주 생긴다.

Q. N+1은 Lazy 때문에만 생겨?
A. 아니다. Lazy에서 자주 보이지만 EAGER에서도 조회 방식에 따라 발생할 수 있다.

Q. N+1 문제는 어떻게 찾는 게 좋아?
A. SQL 로그를 켜고 API 하나가 실행하는 Query 수를 확인한다.

---

## 4.2 N+1 Detection

### [개념]

N+1 Detection은 API 실행 시 SQL Query 수와 연관 Entity 접근 위치를 확인해 반복 Query를 찾는 과정이다.

Review Agent는 목록 조회 API와 DTO 변환 로직에서 N+1 가능성을 우선 검수해야 한다.

---

### [핵심]

확인 대상:

- Repository 목록 조회
- Service 반복문
- Stream `map`
- DTO `from` Method
- Response DTO 생성자
- Entity getter 호출
- JSON 직렬화
- Page.map
- Query 수
- SQL 로그

Detection Flow:

```text
API 하나 호출
→ SQL 로그 확인
→ 첫 번째 목록 Query 확인
→ 반복 SELECT 확인
→ 반복 SELECT 대상 Entity 확인
→ 연관 Field 접근 위치 추적
→ 해결 전략 선택
```

---

### [실무]

DTO 변환 중 발생 예시:

```java
public static PostResponse from(Post post) {
    return new PostResponse(
            post.getPostId(),
            post.getTitle(),
            post.getUser().getNickname()
    );
}
```

위험:

```text
PostResponse.from(post)
→ post.getUser().getNickname()
→ User Lazy Loading
→ 목록 변환에서 반복 Query 발생 가능
```

Page.map 예시:

```java
Page<PostResponse> responses = postRepository.findByDeletedFalse(pageable)
        .map(PostResponse::from);
```

검토:

```text
PostResponse.from
→ 연관 Entity 접근 여부 확인
→ User / Category / Comments 접근 시 N+1 가능
```

권장:

- DTO `from` Method 내부 연관 접근 확인
- Page.map 변환 시 Lazy Field 접근 확인
- SQL 로그를 API 단위로 확인
- Hibernate Statistics 또는 Query Count 도구 사용 검토
- 테스트 데이터 N개 이상으로 검증

주의:

- 작은 테스트 데이터에서는 N+1이 눈에 띄지 않을 수 있다.
- DTO 변환 코드가 분리되어 있으면 N+1 원인 추적이 어려울 수 있다.
- Entity `toString`, logging, debugger도 Lazy Loading을 유발할 수 있다.
- Query 수뿐 아니라 Row 수와 Join 결과도 확인해야 한다.

---

### [FAQ]

Q. N+1은 어디서 가장 많이 숨어 있어?
A. DTO 변환 Method, Stream map, Page.map, JSON 직렬화, Entity getter 접근에 숨어 있는 경우가 많다.

Q. DTO from Method도 N+1을 만들 수 있어?
A. 그렇다. from Method에서 Lazy Association을 접근하면 목록 변환 중 반복 Query가 발생할 수 있다.

Q. Page.map은 안전해?
A. 변환 내부에서 Lazy Field를 접근하면 N+1이 발생할 수 있어 확인해야 한다.

Q. SQL 로그 말고도 N+1을 확인할 수 있어?
A. Hibernate Statistics, Query Count 도구, 테스트 로그를 활용할 수 있다.

---

## 4.3 N+1 Solution Strategy

### [개념]

N+1 Solution Strategy는 반복 Query 문제를 상황에 맞게 해결하는 선택 기준이다.

N+1은 Fetch Join만으로 해결하는 문제가 아니며 DTO Projection, Batch Size, 별도 Query, API 구조 변경도 함께 검토한다.

---

### [핵심]

해결 후보:

- Fetch Join
- DTO Projection
- Batch Size
- EntityGraph
- Separate Query
- QueryDSL Projection
- API Response 구조 변경
- Pagination 전략 변경

선택 기준:

```text
ManyToOne / OneToOne N+1
→ Fetch Join / DTO Projection

OneToMany Collection N+1
→ Batch Size / 별도 Query / DTO Projection / API 구조 변경

Read-only 목록
→ DTO Projection

수정 대상 Entity
→ Entity 조회 + Fetch Join 제한 검토

Pagination 포함
→ Collection Fetch Join 주의
```

---

### [실무]

ManyToOne 해결 예시:

```java
@Query("""
    select p
    from Post p
    join fetch p.user
    where p.deleted = false
    order by p.createdAt desc
""")
List<Post> findAllWithUser();
```

DTO Projection 해결 예시:

```java
@Query("""
    select new com.example.post.PostSummaryResponse(
        p.postId,
        p.title,
        u.nickname
    )
    from Post p
    join p.user u
    where p.deleted = false
    order by p.createdAt desc
""")
List<PostSummaryResponse> findPostSummaries();
```

OneToMany 별도 Query 예시:

```java
Slice<Comment> findByPost_PostIdOrderByCreatedAtDesc(Long postId, Pageable pageable);
```

권장:

- 연관 Entity 전체가 필요하면 Fetch Join
- 필요한 Field만 있으면 DTO Projection
- Collection 목록은 별도 Pagination Query
- 대량 목록은 Batch Size 검토
- API 응답 구조가 과도하면 구조 변경 검토
- 해결 후 SQL Query 수 재확인

주의:

- Fetch Join 남용은 과도한 데이터 조회를 만든다.
- Collection Fetch Join은 Pagination과 충돌할 수 있다.
- DTO Projection은 Dirty Checking 대상이 아니다.
- Batch Size는 Query 수를 줄일 수 있지만 Query 자체를 제거하지는 않는다.
- N+1 해결 전략은 API별로 다르다.

---

### [FAQ]

Q. N+1은 무조건 Fetch Join으로 해결해?
A. 아니다. Fetch Join, DTO Projection, Batch Size, 별도 Query, API 구조 변경 중 상황에 맞게 선택한다.

Q. ManyToOne N+1은 어떻게 해결해?
A. Fetch Join이나 DTO Projection을 우선 검토한다.

Q. OneToMany N+1은 어떻게 해결해?
A. Batch Size, 별도 Query, DTO Projection, API 구조 변경을 검토한다.

Q. 읽기 전용 목록은 어떤 해결이 좋아?
A. 필요한 Field만 조회하는 DTO Projection이 적합한 경우가 많다.

---

# 5. Fetch Join

## 5.1 Fetch Join Concept

### [개념]

Fetch Join은 JPQL에서 연관 Entity를 함께 조회해 Lazy Loading에 따른 추가 Query를 줄이는 방법이다.

Fetch Join은 SQL JOIN과 달리 연관 Entity를 Persistence Context에 함께 로딩하는 목적을 가진다.

---

### [핵심]

핵심 키워드:

- Fetch Join
- JPQL
- join fetch
- Association Loading
- Lazy Loading 해결
- N+1 Problem 해결 후보
- Persistence Context
- ManyToOne Fetch Join
- Collection Fetch Join Caution

Fetch Join 흐름:

```text
Post 조회 Query
→ join fetch p.user
→ Post와 User를 함께 조회
→ post.getUser() 접근 시 추가 Query 감소
```

---

### [실무]

단건 상세 예시:

```java
@Query("""
    select p
    from Post p
    join fetch p.user
    where p.postId = :postId
""")
Optional<Post> findByIdWithUser(Long postId);
```

목록 예시:

```java
@Query("""
    select p
    from Post p
    join fetch p.user
    where p.deleted = false
    order by p.createdAt desc
""")
List<Post> findPostsWithUser();
```

SQL Foundation 연결:

```text
SQL JOIN
→ DB Row 연결

JPQL Fetch Join
→ DB Join + Entity Association 초기화
```

권장:

- 특정 조회에서 필요한 연관 Entity만 Fetch Join
- ManyToOne / OneToOne Fetch Join은 자주 사용 가능
- 단건 상세 조회에서 필요한 연관 Entity Fetch Join
- 목록 조회에서 N+1이 명확할 때 Fetch Join 검토
- Fetch Join 후 SQL Query 수 확인

주의:

- Fetch Join은 필요한 API Query에만 적용한다.
- Fetch Join은 JPQL에서 조회 대상 Entity와 함께 연관 Entity를 로딩한다.
- Fetch Join 대상에 별칭 사용은 구현체와 용도에 따라 주의한다.
- Collection Fetch Join은 중복 Row와 Pagination 문제를 만든다.
- 여러 Collection Fetch Join은 위험하다.

---

### [FAQ]

Q. Fetch Join은 뭐야?
A. JPQL에서 연관 Entity를 함께 조회해 Lazy Loading에 따른 추가 Query를 줄이는 방법이다.

Q. Fetch Join과 일반 Join은 뭐가 달라?
A. 일반 Join은 조건 필터링 목적일 수 있고 Fetch Join은 연관 Entity를 함께 로딩하는 목적이다.

Q. Fetch Join은 언제 써?
A. 특정 조회에서 연관 Entity가 반드시 필요하고 Lazy Loading으로 추가 Query가 많이 발생할 때 사용한다.

Q. Fetch Join을 쓰면 N+1이 항상 해결돼?
A. ManyToOne / OneToOne에서는 효과적일 수 있지만 Collection과 Pagination에서는 주의가 필요하다.

---

## 5.2 Join vs Fetch Join

### [개념]

Join은 Query 조건이나 결과 필터링을 위해 Table / Entity를 연결하는 방식이다.

Fetch Join은 Join과 동시에 연관 Entity를 로딩하는 JPA 전용 조회 전략이다.

---

### [핵심]

비교:

| 구분               | Join                 | Fetch Join                    |
| ------------------ | -------------------- | ----------------------------- |
| 목적               | 조건 / 필터링        | 연관 Entity 로딩              |
| JPQL               | `join p.user u`      | `join fetch p.user`           |
| 연관 Entity 초기화 | 보장 아님            | 함께 로딩                     |
| N+1 해결           | 직접 해결 아님       | 해결 후보                     |
| DTO Projection     | 가능                 | 보통 Entity 조회 중심         |
| Pagination 주의    | Collection Join 주의 | Collection Fetch Join 더 주의 |

---

### [실무]

일반 Join 예시:

```java
@Query("""
    select p
    from Post p
    join p.user u
    where u.nickname = :nickname
""")
List<Post> findByUserNickname(String nickname);
```

Fetch Join 예시:

```java
@Query("""
    select p
    from Post p
    join fetch p.user
    where p.deleted = false
""")
List<Post> findWithUser();
```

해석:

```text
join p.user
→ User 조건 사용 가능
→ Post.user 초기화 보장 아님

join fetch p.user
→ User를 함께 로딩
→ post.getUser() 추가 Query 감소 가능
```

권장:

- 조건 필터링만 필요하면 일반 Join
- Entity 연관 객체를 이후 사용할 예정이면 Fetch Join
- 응답 Field만 필요하면 DTO Projection도 검토
- Join 결과 중복 여부 확인
- Fetch Join은 과도한 데이터 로딩을 만들지 않는지 확인

주의:

- 일반 Join을 썼다고 Lazy Association이 초기화되는 것은 아니다.
- Fetch Join은 Entity 그래프를 함께 로딩한다.
- DTO Projection에서는 Fetch Join이 부적절할 수 있다.
- Fetch Join은 Count Query와 Pagination에서 제약이 있다.

---

### [FAQ]

Q. 일반 Join과 Fetch Join 차이는 뭐야?
A. 일반 Join은 조건 필터링 목적이고 Fetch Join은 연관 Entity를 함께 로딩하는 목적이다.

Q. 일반 Join으로 N+1이 해결돼?
A. 아니다. 일반 Join만으로 Lazy Association 초기화가 보장되지 않는다.

Q. Fetch Join은 DTO Projection에도 써?
A. 보통 Entity 조회에서 연관 Entity 로딩 목적으로 사용하며 DTO Projection에서는 일반 Join으로 필요한 Field만 조회하는 경우가 많다.

Q. Join을 쓸지 Fetch Join을 쓸지 어떻게 정해?
A. 연관 Entity 자체를 이후 사용할지, 아니면 조건 / Field만 필요한지 기준으로 정한다.

---

## 5.3 ManyToOne Fetch Join

### [개념]

ManyToOne Fetch Join은 Many 쪽 Entity 목록을 조회하면서 One 쪽 Entity를 함께 로딩하는 전략이다.

목록 조회에서 작성자, 카테고리, 상위 Entity 정보가 필요한 경우 N+1 해결에 자주 사용된다.

---

### [핵심]

사용 상황:

- Post 목록 + User 필요
- Comment 목록 + Post 필요
- Review 목록 + User 필요
- Favorite 목록 + Festival 필요
- OrderItem 목록 + Order 필요

장점:

- 1 + N Query 감소
- ManyToOne N+1 해결 후보
- DTO 변환 중 추가 Query 감소
- Entity Graph 로딩 명확화

---

### [실무]

예시:

```java
@Query("""
    select p
    from Post p
    join fetch p.user
    where p.deleted = false
    order by p.createdAt desc
""")
List<Post> findPostsWithUser();
```

Pagination이 필요하면 주의:

```java
@Query("""
    select p
    from Post p
    join fetch p.user
    where p.deleted = false
""")
Page<Post> findPageWithUser(Pageable pageable);
```

검토:

```text
ManyToOne Fetch Join
→ Row 수 증가가 Collection보다 적음
→ Page 사용 가능성 있음
→ Count Query / 생성 SQL 확인 필요
```

권장:

- ManyToOne N+1은 Fetch Join 우선 검토
- Pagination 적용 시 Count Query 확인
- 필요한 연관 Entity만 Fetch Join
- 복수 ManyToOne Fetch Join은 가능하지만 데이터 양 확인
- 목록 Read-only이면 DTO Projection도 비교

주의:

- Fetch Join 대상이 많아지면 Row 데이터가 커진다.
- Page Count Query에서 Fetch Join 제거가 필요할 수 있다.
- Fetch Join과 Entity 반환 후 DTO 변환 시 Lazy 접근 추가 여부 확인
- Fetch Join을 모든 Repository Method에 붙이지 않는다.

---

### [FAQ]

Q. ManyToOne Fetch Join은 언제 써?
A. 목록 조회에서 Many 쪽 Entity마다 One 쪽 Entity 정보가 필요해 N+1이 발생할 때 사용한다.

Q. ManyToOne Fetch Join은 Pagination과 같이 써도 돼?
A. Collection Fetch Join보다 안전할 수 있지만 Count Query와 생성 SQL을 확인해야 한다.

Q. 여러 ManyToOne을 Fetch Join해도 돼?
A. 가능하지만 필요한 연관 Entity인지와 데이터 양을 확인해야 한다.

Q. ManyToOne N+1은 DTO Projection으로도 해결돼?
A. 그렇다. 읽기 전용 목록이면 필요한 Field만 Projection으로 조회하는 것도 좋은 선택이다.

---

## 5.4 Collection Fetch Join Caution

### [개념]

Collection Fetch Join은 OneToMany 같은 Collection Association을 Fetch Join으로 함께 조회하는 방식이다.

Collection Fetch Join은 중복 Row, Pagination 문제, 메모리 사용 증가를 만들 수 있어 신중히 사용해야 한다.

---

### [핵심]

핵심 키워드:

- Collection Fetch Join
- OneToMany
- Row Duplication
- distinct
- Pagination Caution
- Multiple Bag Fetch
- Memory Pagination
- Cartesian Product
- Data Explosion

문제 흐름:

```text
Post 1개
→ Comment 5개

Post Fetch Join Comments
→ SQL Row 5개
→ Post 중복 발생
```

---

### [실무]

예시:

```java
@Query("""
    select distinct p
    from Post p
    join fetch p.comments
    where p.postId = :postId
""")
Optional<Post> findByIdWithComments(Long postId);
```

사용 가능 후보:

```text
단건 상세 조회
→ 제한된 Collection 크기
→ Pagination 필요 없음
→ 중복 Row 감당 가능
```

위험 상황:

```text
목록 조회 + Collection Fetch Join
Pagination + Collection Fetch Join
여러 Collection 동시 Fetch Join
대용량 Collection Fetch Join
```

대안:

```text
Child Repository 별도 조회
DTO Projection
Batch Size
API 응답 구조 변경
두 단계 조회
```

권장:

- Collection Fetch Join은 단건 상세에서 제한적으로 사용
- Pagination이 필요하면 Child Repository 별도 조회 검토
- 여러 Collection Fetch Join 피하기
- `distinct` 사용 시 SQL / JPA 중복 제거 차이 확인
- Row 수 증가를 SQL 로그로 확인

주의:

- `distinct`가 모든 문제를 해결하지 않는다.
- Collection Fetch Join과 Pageable 조합은 위험하다.
- 여러 Collection Fetch Join은 데이터 폭발을 만들 수 있다.
- Parent Entity 중복과 메모리 사용량을 확인해야 한다.
- Collection 크기가 커질 가능성이 있으면 다른 전략이 안전하다.

---

### [FAQ]

Q. Collection Fetch Join은 왜 위험해?
A. Child 수만큼 Parent Row가 중복되어 Pagination과 메모리 사용 문제가 생길 수 있다.

Q. Collection Fetch Join에 Pagination을 같이 써도 돼?
A. 주의해야 한다. DB Pagination이 기대대로 동작하지 않거나 메모리에서 처리될 수 있다.

Q. distinct를 쓰면 Collection Fetch Join 문제가 해결돼?
A. 중복 제거에는 도움될 수 있지만 Pagination과 데이터 폭발 문제를 완전히 해결하지 못할 수 있다.

Q. OneToMany 목록은 어떻게 조회하는 게 좋아?
A. Child Repository에서 Parent ID 조건으로 Page나 Slice 조회하는 방식이 안정적이다.

---

# 6. DTO Projection and Fetch Strategy

## 6.1 DTO Projection as Fetch Strategy

### [개념]

DTO Projection은 필요한 Field만 조회해 DTO로 반환하는 방식이며, 읽기 전용 API에서 Fetch Strategy 대안이 될 수 있다.

Entity 전체와 연관 Entity 전체가 필요하지 않은 목록 조회에서는 Fetch Join보다 DTO Projection이 더 적합할 수 있다.

---

### [핵심]

핵심 키워드:

- DTO Projection
- Read-only Query
- Select Specific Fields
- No Entity Loading
- N+1 Prevention
- Query Optimization
- JPQL Projection
- QueryDSL Projection

사용 후보:

- 목록 화면
- 검색 결과
- 카드 UI
- 통계 응답
- 연관 Entity 일부 Field만 필요
- 수정 불필요한 Read-only API

---

### [실무]

Projection 예시:

```java
@Query("""
    select new com.example.post.PostSummaryResponse(
        p.postId,
        p.title,
        u.nickname,
        p.createdAt
    )
    from Post p
    join p.user u
    where p.deleted = false
    order by p.createdAt desc
""")
List<PostSummaryResponse> findPostSummaries();
```

비교:

```text
Fetch Join
→ Entity + 연관 Entity 로딩
→ 수정 가능 Entity 필요할 때 후보

DTO Projection
→ 필요한 Field만 조회
→ Read-only 응답에 적합
```

권장:

- 목록 Read-only 응답은 Projection 우선 검토
- 필요한 Field만 SELECT
- 연관 Entity 전체가 필요 없으면 Projection 사용
- QueryDSL Projection과 연결 가능
- Projection 결과는 Entity처럼 수정하지 않음

주의:

- Projection DTO는 Managed Entity가 아니다.
- Dirty Checking 대상이 아니다.
- 응답 DTO와 Query DTO 역할을 구분할 수 있다.
- Projection Query가 많아지면 중복 관리가 필요하다.
- 복잡한 동적 Projection은 QueryDSL을 검토한다.

---

### [FAQ]

Q. DTO Projection도 Fetch Strategy야?
A. Entity 전체를 로딩하지 않고 필요한 Field만 조회한다는 점에서 읽기 전용 Fetch 전략 대안으로 볼 수 있다.

Q. Fetch Join과 DTO Projection 중 뭐가 좋아?
A. Entity와 연관 Entity가 필요하면 Fetch Join, 필요한 Field만 있으면 DTO Projection이 적합하다.

Q. Projection 결과를 수정해도 DB에 반영돼?
A. 아니다. Projection DTO는 Managed Entity가 아니며 Dirty Checking 대상이 아니다.

Q. 목록 API에는 Fetch Join과 Projection 중 무엇을 먼저 검토해?
A. Read-only 목록이면 DTO Projection을 먼저 검토하는 것이 좋다.

---

## 6.2 Projection and N+1 Prevention

### [개념]

Projection은 연관 Entity Field를 Query에서 직접 선택하므로 DTO 변환 중 Lazy Loading으로 인한 N+1 문제를 줄일 수 있다.

---

### [핵심]

Projection 장점:

- 필요한 Field만 조회
- Entity Lazy Association 접근 감소
- DTO 변환 중 추가 Query 감소
- 목록 API 성능 예측 가능
- Response 구조에 맞춘 조회 가능

Projection Flow:

```text
Post + User nickname 필요
→ JPQL Join
→ DTO Projection
→ PostSummaryResponse 생성
→ post.getUser() 접근 없음
→ N+1 감소
```

---

### [실무]

N+1 위험 Entity 변환:

```java
return postRepository.findAll().stream()
        .map(PostResponse::from)
        .toList();
```

Projection 개선:

```java
@Query("""
    select new com.example.post.PostResponse(
        p.postId,
        p.title,
        u.nickname
    )
    from Post p
    join p.user u
""")
List<PostResponse> findPostResponses();
```

권장:

- 목록 응답에서 연관 Field가 몇 개만 필요하면 Projection
- DTO `from` 내부 Lazy 접근 제거
- Projection Query SQL 확인
- 필요 Field가 많아지면 응답 구조 재검토
- 동적 조건 + Projection은 QueryDSL 검토

주의:

- Projection은 Entity Lifecycle과 무관하다.
- Projection DTO는 수정 로직에 사용하지 않는다.
- Projection이 너무 많아지면 Repository 복잡도가 증가한다.
- Native Projection은 Alias / Type Mapping을 주의한다.
- Projection으로도 잘못된 Join은 성능 문제를 만들 수 있다.

---

### [FAQ]

Q. Projection으로 N+1을 막을 수 있어?
A. 연관 Field를 Query에서 직접 조회하면 DTO 변환 중 Lazy 접근이 줄어 N+1 방지에 도움이 된다.

Q. Projection을 쓰면 Fetch Join이 필요 없어?
A. 읽기 전용 Field 조회에서는 필요 없을 수 있다. Entity 그래프가 필요한 경우는 Fetch Join을 검토한다.

Q. Projection은 Service에서 DTO 변환하는 것과 달라?
A. Projection은 Query 단계에서 DTO를 만들고, Service 변환은 Entity 조회 후 DTO로 바꾸는 방식이다.

Q. Projection Query도 SQL 로그를 봐야 해?
A. 그렇다. Join, Row 수, Index 사용 가능성을 확인해야 한다.

---

# 7. Batch Size and EntityGraph Preview

## 7.1 Batch Size Basic

### [개념]

Batch Size는 Lazy Loading으로 여러 연관 Entity를 조회할 때 여러 개의 개별 SELECT를 묶어서 조회하도록 도와주는 Hibernate 최적화 방법이다.

Batch Size는 N+1 Query 수를 줄일 수 있지만 Query 자체를 완전히 제거하는 것은 아니다.

---

### [핵심]

핵심 키워드:

- Batch Size
- Hibernate Batch Fetching
- Lazy Loading Optimization
- N+1 Mitigation
- IN Query
- `@BatchSize`
- default_batch_fetch_size

동작 예:

```text
Post 100개 조회
→ 각 Post.user Lazy 접근
→ User를 하나씩 100번 조회하지 않음
→ IN Query로 묶어서 조회 가능
```

---

### [실무]

설정 후보:

```properties
spring.jpa.properties.hibernate.default_batch_fetch_size=100
```

Annotation 후보:

```java
@BatchSize(size = 100)
@OneToMany(mappedBy = "post")
private List<Comment> comments = new ArrayList<>();
```

해결 위치:

```text
Fetch Join이 어려운 Collection
→ Batch Size 검토

Pagination + Collection
→ Fetch Join 대신 Batch Size 검토

Lazy Loading 반복
→ Query 수 완화
```

권장:

- Collection Fetch Join이 위험한 경우 Batch Size 검토
- 전역 설정은 프로젝트 기준으로 통일
- SQL 로그로 IN Query 발생 확인
- Batch Size 값은 데이터 규모에 맞게 조정
- Fetch Join / Projection과 비교 후 선택

주의:

- Batch Size는 N+1을 완전히 없애는 것이 아니라 완화한다.
- IN Query 크기가 너무 커지면 DB 부담이 생길 수 있다.
- 모든 상황에서 Fetch Join보다 좋은 것은 아니다.
- Hibernate 기능이므로 JPA 표준과 구분한다.
- 상세 최적화는 Performance / Expert 문서와 연결 가능하다.

---

### [FAQ]

Q. Batch Size는 뭐야?
A. Lazy Loading 시 여러 연관 Entity 조회를 IN Query 등으로 묶어 Query 수를 줄이는 Hibernate 최적화 방법이다.

Q. Batch Size는 N+1을 완전히 해결해?
A. 아니다. Query 수를 줄여 완화하지만 Fetch Join이나 Projection처럼 Query 구조를 바꾸는 것과 다르다.

Q. Batch Size는 언제 검토해?
A. Collection Fetch Join이 Pagination 문제를 만들 때나 Lazy Loading 반복 Query를 완화하고 싶을 때 검토한다.

Q. Batch Size는 JPA 표준이야?
A. Hibernate 최적화 기능이다. JPA 표준과 구분해야 한다.

---

## 7.2 EntityGraph Basic

### [개념]

EntityGraph는 특정 조회에서 함께 로딩할 연관 Entity를 선언적으로 지정하는 JPA 기능이다.

Fetch Join과 비슷하게 연관 Entity 로딩 전략을 Query별로 제어할 수 있다.

---

### [핵심]

핵심 키워드:

- EntityGraph
- `@EntityGraph`
- Attribute Paths
- Fetch Plan
- Query-specific Loading
- Lazy Override
- Association Loading

사용 후보:

- Repository Query Method에 연관 Entity 로딩 추가
- 간단한 Fetch Plan 제어
- JPQL Fetch Join 대신 선언적 로딩
- 단순 연관 Entity 함께 조회

---

### [실무]

예시:

```java
@EntityGraph(attributePaths = {"user"})
Optional<Post> findWithUserByPostId(Long postId);
```

목록 예시:

```java
@EntityGraph(attributePaths = {"user"})
List<Post> findByDeletedFalseOrderByCreatedAtDesc();
```

Fetch Join과 비교:

```text
Fetch Join
→ JPQL에 join fetch 명시

EntityGraph
→ Repository Method에 로딩 대상 선언
```

권장:

- 단순 연관 Entity 함께 로딩에 사용 가능
- Query Method와 함께 사용할 수 있음
- 복잡한 조건은 JPQL / QueryDSL 검토
- Collection EntityGraph는 Pagination 문제 검토
- SQL 로그로 실제 Join / Select 확인

주의:

- EntityGraph도 과도하게 쓰면 불필요한 로딩이 생긴다.
- Collection 로딩은 Fetch Join과 유사한 주의가 필요하다.
- 복잡한 동적 Fetch Plan은 유지보수성이 떨어질 수 있다.
- QueryDSL과 조합 시 별도 전략 검토가 필요하다.
- Part06에서는 기본 개념만 다루고 심화는 별도 성능 문서에서 다룬다.

---

### [FAQ]

Q. EntityGraph는 뭐야?
A. 특정 조회에서 함께 로딩할 연관 Entity를 선언적으로 지정하는 JPA 기능이다.

Q. EntityGraph와 Fetch Join은 뭐가 달라?
A. Fetch Join은 JPQL에 직접 작성하고 EntityGraph는 Repository Method에 로딩 대상을 선언한다.

Q. EntityGraph도 N+1 해결에 도움이 돼?
A. 필요한 연관 Entity를 함께 로딩할 수 있어 N+1 완화에 도움이 될 수 있다.

Q. EntityGraph를 Collection에 써도 돼?
A. 가능하지만 Collection Fetch Join과 비슷하게 중복 Row와 Pagination 문제를 검토해야 한다.

---

# 8. Fetch Strategy Review

## 8.1 Fetch Strategy Checklist

### [개념]

Fetch Strategy Checklist는 Entity Association과 Repository Query가 Lazy Loading, Eager Loading, Fetch Join, N+1 관점에서 안전한지 검수하는 기준이다.

Review Agent는 목록 API, DTO 변환, Pagination Query에서 Query 수를 반드시 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] ManyToOne에 FetchType.LAZY를 명시했는가?
- [ ] OneToOne에 FetchType.LAZY를 검토했는가?
- [ ] EAGER 기본값을 방치하지 않았는가?
- [ ] Entity를 API Response로 직접 반환하지 않는가?
- [ ] DTO 변환이 Transaction 범위 안에서 수행되는가?
- [ ] DTO from Method에서 Lazy Association에 접근하는가?
- [ ] 목록 조회 API에서 N+1 가능성을 검토했는가?
- [ ] SQL 로그로 Query 수를 확인했는가?
- [ ] Fetch Join이 필요한 Query에만 적용되었는가?
- [ ] 일반 Join과 Fetch Join을 구분했는가?
- [ ] ManyToOne N+1에 Fetch Join / Projection을 검토했는가?
- [ ] OneToMany N+1에 Batch Size / 별도 Query를 검토했는가?
- [ ] Collection Fetch Join과 Pagination 조합을 피했는가?
- [ ] 여러 Collection Fetch Join을 피했는가?
- [ ] Read-only 목록에 DTO Projection을 검토했는가?
- [ ] Page.map 변환 중 Lazy Field 접근을 확인했는가?
- [ ] LazyInitializationException 해결을 EAGER로 덮지 않았는가?
- [ ] Batch Size 적용 시 SQL IN Query를 확인했는가?
- [ ] EntityGraph 사용 시 실제 SQL을 확인했는가?
```

---

### [실무]

Review Flow:

```text
Association Mapping 확인
→ FetchType 확인
→ Repository Query 확인
→ API DTO 변환 확인
→ 연관 Field 접근 확인
→ SQL Query 수 확인
→ N+1 여부 판단
→ Fetch Join / Projection / Batch Size 선택
→ Pagination 충돌 여부 확인
→ 최종 SQL 재확인
```

Common Review Findings:

```text
문제: @ManyToOne FetchType.LAZY 누락
위험: 기본 EAGER로 불필요한 조회
해결: fetch = FetchType.LAZY 명시

문제: DTO from에서 post.getUser().getNickname() 반복
위험: N+1 발생
해결: Fetch Join 또는 DTO Projection

문제: LazyInitializationException 해결로 EAGER 변경
위험: 전체 API 성능 저하
해결: Service Transaction 안 DTO 변환 / Fetch Join

문제: OneToMany Fetch Join + Pageable
위험: Pagination 불안정
해결: Child Repository Slice 조회 또는 Batch Size

문제: Page.map 변환 중 Lazy 접근
위험: Page 목록 N+1
해결: Fetch Join / Projection으로 Query 조정
```

---

### [FAQ]

Q. Fetch Strategy 검수에서 가장 먼저 확인할 것은 뭐야?
A. Association의 FetchType과 목록 API의 DTO 변환 중 Lazy Field 접근 여부를 먼저 확인한다.

Q. SQL 로그에서 무엇을 봐야 해?
A. API 하나가 실행하는 Query 수, 반복 SELECT, Join, Count Query, Row 증가를 확인해야 한다.

Q. Fetch Join이 있으면 무조건 좋은 Query야?
A. 아니다. 필요한 연관 Entity만 가져오는지, Collection과 Pagination 충돌이 없는지 확인해야 한다.

Q. Read-only 목록은 어떤 전략을 먼저 검토해?
A. 필요한 Field만 조회하는 DTO Projection을 먼저 검토하는 것이 좋다.

---

# 9. Troubleshooting

## 9.1 LazyInitializationException Troubleshooting

### [개념]

LazyInitializationException Troubleshooting은 Transaction 밖 Lazy Association 접근 문제를 분석하고 해결하는 절차다.

핵심은 Entity를 외부 계층으로 노출하지 않고 필요한 데이터를 Transaction 안에서 조회 / 변환하는 것이다.

---

### [핵심]

Debug 대상:

- Exception 발생 위치
- Transaction 종료 여부
- Entity 반환 여부
- DTO 변환 위치
- Lazy Field 접근 위치
- Fetch Join 필요 여부
- Projection 가능 여부
- OSIV 의존 여부

Debug Flow:

```text
Exception Stack Trace 확인
→ Lazy Field 확인
→ Entity가 Detached 상태인지 확인
→ DTO 변환 위치 확인
→ Entity 직접 반환 여부 확인
→ Fetch Join / Projection 적용
→ SQL Query 수 확인
```

---

### [실무]

문제 해결 Flow:

```text
Controller에서 Entity 반환
→ Response DTO로 변경

DTO 변환이 Transaction 밖
→ Service @Transactional 안으로 이동

연관 Entity 필요
→ Fetch Join 또는 DTO Projection 적용

OSIV 의존
→ Service Layer에서 필요한 데이터 완성
```

권장 코드:

```java
@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    Post post = postRepository.findByIdWithUser(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    return PostResponse.from(post);
}
```

권장:

- Entity 직접 반환 제거
- DTO 변환 위치를 Service Transaction 안으로 이동
- Fetch Join으로 필요한 연관 Entity 로딩
- Projection으로 필요한 Field 직접 조회
- 해결 후 N+1 여부 재확인

주의:

- EAGER 변경은 최후 선택에 가깝다.
- OSIV가 켜져 있으면 예외가 안 나도 N+1이 숨어 있을 수 있다.
- LazyInitializationException 해결 후 Query 수가 폭증하지 않았는지 확인한다.
- Controller / View에서 Entity 연관 Field 접근 금지

---

### [FAQ]

Q. LazyInitializationException이 나면 첫 번째로 뭘 확인해?
A. Lazy Field 접근 위치와 Transaction이 이미 종료되었는지 확인한다.

Q. Entity 직접 반환을 없애면 Lazy 예외가 줄어들어?
A. 그렇다. Service Transaction 안에서 DTO로 변환하면 Lazy Field 접근 위치를 통제할 수 있다.

Q. Fetch Join을 적용했는데도 Lazy 예외가 나면?
A. 필요한 모든 Lazy Field가 조회되었는지, DTO 변환 위치가 Transaction 안인지 확인해야 한다.

Q. OSIV가 켜져 있으면 괜찮아?
A. 예외는 줄 수 있지만 Controller / View에서 Query가 발생해 성능 문제가 숨겨질 수 있다.

---

## 9.2 N+1 Troubleshooting

### [개념]

N+1 Troubleshooting은 API 호출 시 반복 SQL이 발생하는 원인을 찾고 Query 전략을 수정하는 과정이다.

핵심은 반복 Query가 발생하는 연관 Field와 DTO 변환 위치를 찾는 것이다.

---

### [핵심]

Debug 대상:

- 목록 Repository Method
- DTO 변환 Method
- Stream map
- Page.map
- Entity getter
- SQL 반복 패턴
- Association FetchType
- Fetch Join 적용 여부
- Projection 가능성
- Pagination 여부

Debug Flow:

```text
API 호출
→ SQL 로그 확인
→ 반복 SELECT 대상 Table 확인
→ 연관 Field 접근 위치 찾기
→ ManyToOne / OneToMany 구분
→ 해결 전략 선택
→ SQL Query 수 재확인
```

---

### [실무]

반복 SQL 예시:

```text
select * from posts where deleted = false;
select * from users where user_id = ?;
select * from users where user_id = ?;
select * from users where user_id = ?;
```

원인 추적:

```text
반복 users 조회
→ Post.user 접근 의심
→ PostResponse.from 확인
→ post.getUser().getNickname() 발견
```

해결 선택:

```text
Post.user 필요
→ join fetch p.user

Post.user.nickname만 필요
→ DTO Projection

Post.comments 필요 + Pagination
→ CommentRepository 별도 Slice 조회

여러 Collection 필요
→ API 구조 재검토
```

권장:

- 반복 Query 대상 Table을 먼저 확인
- ManyToOne과 OneToMany를 구분
- Fetch Join 적용 후 Query 수 비교
- Projection 적용 후 SELECT Field 확인
- Collection + Pagination이면 별도 Query 우선

주의:

- N+1 해결 후 데이터 중복이나 Row 폭증이 생길 수 있다.
- Fetch Join으로 Query 수는 줄었지만 데이터 양이 늘 수 있다.
- DTO Projection은 응답 전용이므로 수정 로직에 쓰지 않는다.
- Batch Size는 완화 전략이다.
- SQL Query 수와 전체 실행 시간 모두 확인한다.

---

### [FAQ]

Q. N+1 Troubleshooting에서 가장 먼저 볼 것은 뭐야?
A. SQL 로그에서 반복 SELECT가 발생하는 Table을 먼저 확인한다.

Q. 반복 SELECT 대상이 users면 뭘 의심해?
A. Post.user, Comment.user 같은 ManyToOne Lazy Association 접근을 의심한다.

Q. N+1 해결 후에도 성능이 나쁠 수 있어?
A. 그렇다. Fetch Join으로 데이터 양이 과도하게 늘거나 Pagination 문제가 생길 수 있다.

Q. Collection N+1은 Fetch Join으로 해결하면 돼?
A. 단건 상세에서는 가능할 수 있지만 목록과 Pagination에서는 Batch Size, 별도 Query, API 구조 변경을 검토해야 한다.

---

# 10. Common Mistakes

## 10.1 Fetch Strategy Common Mistakes

### [개념]

Fetch Strategy Common Mistakes는 Lazy Loading, Eager Loading, Fetch Join, N+1, DTO 변환, Pagination에서 자주 발생하는 오류다.

---

### [핵심]

자주 발생하는 실수:

- `ManyToOne` 기본 EAGER 방치
- `OneToOne` 기본 EAGER 방치
- LazyInitializationException을 EAGER로 해결
- N+1 문제를 EAGER로 해결
- LAZY로 바꾸면 N+1이 사라진다고 오해
- Entity를 API Response로 직접 반환
- DTO 변환을 Transaction 밖에서 수행
- DTO `from` Method에서 Lazy Field 반복 접근
- Page.map에서 Lazy Field 접근
- SQL 로그 확인 없이 성능 판단
- 일반 Join과 Fetch Join 혼동
- Fetch Join 남용
- Collection Fetch Join과 Pagination 조합
- 여러 Collection Fetch Join
- `distinct`로 모든 Collection 문제 해결 가능하다고 오해
- Projection DTO를 Entity처럼 수정
- Batch Size를 완전한 N+1 해결로 오해
- OSIV에 의존해 Lazy 문제 숨김

---

### [실무]

Anti Pattern 예시:

```java
@ManyToOne(fetch = FetchType.EAGER)
@JoinColumn(name = "user_id")
private User user;
```

문제:

```text
LazyInitializationException 회피 목적 EAGER
→ 모든 Post 조회에서 User 즉시 조회
→ API별 Fetch 제어 어려움
```

개선:

```java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "user_id", nullable = false)
private User user;
```

Query별 해결:

```java
@Query("""
    select p
    from Post p
    join fetch p.user
    where p.postId = :postId
""")
Optional<Post> findByIdWithUser(Long postId);
```

Anti Pattern 예시:

```java
public static PostResponse from(Post post) {
    return new PostResponse(
            post.getPostId(),
            post.getTitle(),
            post.getUser().getNickname()
    );
}
```

Review 기준:

```text
DTO from Method
→ 연관 Entity 접근 여부 확인
→ 목록 변환에서 호출되는지 확인
→ Fetch Join / Projection 필요성 판단
```

---

### [FAQ]

Q. Fetch Strategy에서 가장 흔한 실수는 뭐야?
A. `ManyToOne` 기본 EAGER를 방치하거나 Lazy 문제를 EAGER로 덮는 것이다.

Q. N+1에서 가장 흔한 실수는 뭐야?
A. SQL 로그를 확인하지 않고 LAZY나 EAGER 설정만 바꾸는 것이다.

Q. Fetch Join에서 가장 흔한 실수는 뭐야?
A. Collection Fetch Join과 Pagination을 함께 사용하는 것이다.

Q. DTO 변환에서 가장 흔한 실수는 뭐야?
A. DTO from Method에서 Lazy Association을 반복 접근해 N+1을 만드는 것이다.

---

# 11. Part06 Final Goal

## 11.1 Agent Output Goal

### [개념]

JPA Advanced Part06의 최종 목적은 Agent가 Fetch Strategy, Lazy Loading, Eager Loading, Fetch Join, N+1 Problem, LazyInitializationException을 기준으로 조회 성능 문제를 탐지하고 해결하도록 만드는 것이다.

Part06은 SQL Foundation의 JOIN, SELECT 반복, Pagination, Backend Troubleshooting 기준과 JPA 연관 Entity 조회 전략을 연결한다.

---

### [핵심]

Agent가 수행해야 할 작업:

- Association FetchType 검토
- `ManyToOne` LAZY 명시 확인
- `OneToOne` LAZY 검토
- EAGER Anti Pattern 탐지
- Lazy Loading 발생 위치 확인
- Proxy 초기화 위치 확인
- LazyInitializationException 원인 분석
- 목록 조회 N+1 탐지
- DTO 변환 N+1 탐지
- Page.map N+1 탐지
- 일반 Join과 Fetch Join 구분
- ManyToOne Fetch Join 적용 판단
- Collection Fetch Join 위험 검토
- DTO Projection 적용 판단
- Batch Size / EntityGraph 기본 검토
- SQL Query Count Review 수행
- Fetch Strategy Checklist 적용

---

### [실무]

Agent 작업 흐름:

```text
User Query / API Requirement
→ Identify Association Access
→ Check FetchType
→ Check DTO Mapping
→ Run Query Count Review
→ Detect N+1
→ Choose Fetch Join / Projection / Batch Size / Separate Query
→ Check Pagination Risk
→ Verify SQL
→ Return Optimized Query Strategy
```

Troubleshooting 흐름:

```text
LazyInitializationException
→ Entity Direct Return 확인
→ Transaction Boundary 확인
→ Lazy Field 확인
→ DTO 변환 위치 수정
→ Fetch Join / Projection 적용
→ SQL Query 수 확인
```

Part06 이후 연결:

```text
Part06 Fetch Strategy / Fetch Join / N+1
→ Part07 Transaction / Cascade / Auditing / Pagination
→ Part08 Backend Integration / Troubleshooting / Anti Pattern
```

---

### [FAQ]

Q. JPA Advanced Part06의 목적은 뭐야?
A. Agent가 Lazy Loading, Eager Loading, Fetch Join, N+1, LazyInitializationException을 분석해 안전한 조회 전략을 선택하도록 만드는 것이다.

Q. Part06에서 가장 중요한 기준은 뭐야?
A. ManyToOne LAZY, EAGER 남용 방지, N+1 SQL 로그 확인, Fetch Join과 Projection 선택, Collection Fetch Join Pagination 주의다.

Q. Part06은 SQL Foundation 어느 부분과 연결돼?
A. SQL Part02 JOIN, SQL Part04 Pagination, SQL Part05 Troubleshooting / Anti Pattern과 연결된다.

Q. Part06 다음에는 무엇을 다뤄?
A. Part07에서 Transaction Boundary, Cascade, orphanRemoval, Auditing, Page, Slice, Pagination을 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. Fetch Strategy는 뭐야?
A. JPA Association Entity를 언제 조회할지 결정하는 전략이다.

Q. Fetch Strategy가 중요한 이유는 뭐야?
A. 연관 Entity 조회 시점, SQL Query 수, N+1 문제, LazyInitializationException에 직접 영향을 주기 때문이다.

Q. `ManyToOne` 기본 Fetch는 뭐야?
A. 기본값은 EAGER다. 실무에서는 `fetch = FetchType.LAZY`를 명시하는 것이 좋다.

Q. `OneToMany` 기본 Fetch는 뭐야?
A. 기본값은 LAZY다.

Q. EAGER가 기본이면 그냥 둬도 돼?
A. 권장하지 않는다. 불필요한 조회와 성능 문제를 만들 수 있어 LAZY 명시를 검토해야 한다.

Q. FetchType을 LAZY로 하면 모든 성능 문제가 해결돼?
A. 아니다. LAZY는 조회 시점을 늦출 뿐이고 N+1 문제는 별도 Query 전략으로 해결해야 한다.

Q. Lazy Loading은 뭐야?
A. 연관 Entity를 실제 사용하는 시점에 조회하는 전략이다.

Q. LAZY는 무조건 좋아?
A. 아니다. 불필요한 즉시 조회를 줄이지만 잘못 사용하면 N+1이나 LazyInitializationException이 발생할 수 있다.

Q. LAZY에서 SQL은 언제 실행돼?
A. Lazy Association Field에 실제 접근할 때 추가 SELECT가 실행될 수 있다.

Q. LAZY로 하면 N+1이 없어져?
A. 아니다. 반복문에서 Lazy Association을 접근하면 N+1이 발생할 수 있다.

Q. Proxy는 뭐야?
A. Lazy Loading을 위해 실제 Entity 대신 사용되는 대리 객체다.

Q. Proxy는 언제 초기화돼?
A. Lazy Association Field의 실제 값에 접근할 때 초기화될 수 있다.

Q. Proxy 초기화에는 Transaction이 필요해?
A. Persistence Context가 열려 있어야 하며 일반적으로 Transaction 범위 안에서 안전하다.

Q. toString에서 Lazy Field를 출력해도 돼?
A. 권장하지 않는다. Proxy 초기화와 N+1, 순환 참조 문제가 발생할 수 있다.

Q. LazyInitializationException은 왜 발생해?
A. Persistence Context가 닫힌 뒤 Lazy Association에 접근했기 때문이다.

Q. LazyInitializationException은 어떻게 해결해?
A. Service Transaction 안에서 DTO 변환하거나 필요한 연관 Entity를 Fetch Join / DTO Projection으로 조회한다.

Q. EAGER로 바꾸면 LazyInitializationException이 해결돼?
A. 권장하지 않는다. 불필요한 조회와 N+1 문제가 생길 수 있어 Fetch Join이나 DTO Projection을 우선 검토한다.

Q. Entity 직접 반환이 왜 위험해?
A. JSON 직렬화 중 Lazy Field 접근으로 LazyInitializationException과 순환 참조 문제가 발생할 수 있다.

Q. Eager Loading은 뭐야?
A. Entity 조회 시 연관 Entity를 즉시 함께 조회하는 전략이다.

Q. EAGER는 왜 위험해?
A. 불필요한 Join과 추가 조회가 발생하고 Query별 성능 제어가 어려워질 수 있다.

Q. EAGER면 N+1 문제가 없어져?
A. 아니다. EAGER도 조회 방식에 따라 N+1 문제가 발생할 수 있다.

Q. Lazy 예외가 나면 EAGER로 바꾸면 돼?
A. 권장하지 않는다. Service Transaction 안 DTO 변환, Fetch Join, DTO Projection을 우선 검토한다.

Q. N+1이 생기면 EAGER로 바꾸면 돼?
A. 권장하지 않는다. Fetch Join, DTO Projection, Batch Size, API 구조 변경 중 상황에 맞게 선택해야 한다.

Q. EAGER Anti Pattern을 어떻게 찾을까?
A. Entity Association에서 FetchType.EAGER 또는 기본 EAGER를 확인하고 SQL 로그로 불필요한 조회를 확인한다.

Q. N+1 문제는 뭐야?
A. 목록 1번 조회 후 각 Row의 연관 Entity를 조회하기 위해 N번 추가 Query가 발생하는 문제다.

Q. N+1은 언제 자주 생겨?
A. 목록 조회 후 반복문이나 DTO 변환 과정에서 연관 Entity getter를 호출할 때 자주 생긴다.

Q. N+1은 Lazy 때문에만 생겨?
A. 아니다. Lazy에서 자주 보이지만 EAGER에서도 조회 방식에 따라 발생할 수 있다.

Q. N+1 문제는 어떻게 찾는 게 좋아?
A. SQL 로그를 켜고 API 하나가 실행하는 Query 수를 확인한다.

Q. N+1은 어디서 가장 많이 숨어 있어?
A. DTO 변환 Method, Stream map, Page.map, JSON 직렬화, Entity getter 접근에 숨어 있는 경우가 많다.

Q. DTO from Method도 N+1을 만들 수 있어?
A. 그렇다. from Method에서 Lazy Association을 접근하면 목록 변환 중 반복 Query가 발생할 수 있다.

Q. Page.map은 안전해?
A. 변환 내부에서 Lazy Field를 접근하면 N+1이 발생할 수 있어 확인해야 한다.

Q. N+1은 무조건 Fetch Join으로 해결해?
A. 아니다. Fetch Join, DTO Projection, Batch Size, 별도 Query, API 구조 변경 중 상황에 맞게 선택한다.

Q. ManyToOne N+1은 어떻게 해결해?
A. Fetch Join이나 DTO Projection을 우선 검토한다.

Q. OneToMany N+1은 어떻게 해결해?
A. Batch Size, 별도 Query, DTO Projection, API 구조 변경을 검토한다.

Q. 읽기 전용 목록은 어떤 N+1 해결이 좋아?
A. 필요한 Field만 조회하는 DTO Projection이 적합한 경우가 많다.

Q. Fetch Join은 뭐야?
A. JPQL에서 연관 Entity를 함께 조회해 Lazy Loading에 따른 추가 Query를 줄이는 방법이다.

Q. Fetch Join과 일반 Join은 뭐가 달라?
A. 일반 Join은 조건 필터링 목적일 수 있고 Fetch Join은 연관 Entity를 함께 로딩하는 목적이다.

Q. Fetch Join은 언제 써?
A. 특정 조회에서 연관 Entity가 반드시 필요하고 Lazy Loading으로 추가 Query가 많이 발생할 때 사용한다.

Q. Fetch Join을 쓰면 N+1이 항상 해결돼?
A. ManyToOne / OneToOne에서는 효과적일 수 있지만 Collection과 Pagination에서는 주의가 필요하다.

Q. 일반 Join으로 N+1이 해결돼?
A. 아니다. 일반 Join만으로 Lazy Association 초기화가 보장되지 않는다.

Q. Fetch Join은 DTO Projection에도 써?
A. 보통 Entity 조회에서 연관 Entity 로딩 목적으로 사용하며 DTO Projection에서는 일반 Join으로 필요한 Field만 조회하는 경우가 많다.

Q. ManyToOne Fetch Join은 언제 써?
A. 목록 조회에서 Many 쪽 Entity마다 One 쪽 Entity 정보가 필요해 N+1이 발생할 때 사용한다.

Q. ManyToOne Fetch Join은 Pagination과 같이 써도 돼?
A. Collection Fetch Join보다 안전할 수 있지만 Count Query와 생성 SQL을 확인해야 한다.

Q. 여러 ManyToOne을 Fetch Join해도 돼?
A. 가능하지만 필요한 연관 Entity인지와 데이터 양을 확인해야 한다.

Q. Collection Fetch Join은 왜 위험해?
A. Child 수만큼 Parent Row가 중복되어 Pagination과 메모리 사용 문제가 생길 수 있다.

Q. Collection Fetch Join에 Pagination을 같이 써도 돼?
A. 주의해야 한다. DB Pagination이 기대대로 동작하지 않거나 메모리에서 처리될 수 있다.

Q. distinct를 쓰면 Collection Fetch Join 문제가 해결돼?
A. 중복 제거에는 도움될 수 있지만 Pagination과 데이터 폭발 문제를 완전히 해결하지 못할 수 있다.

Q. OneToMany 목록은 어떻게 조회하는 게 좋아?
A. Child Repository에서 Parent ID 조건으로 Page나 Slice 조회하는 방식이 안정적이다.

Q. DTO Projection도 Fetch Strategy야?
A. Entity 전체를 로딩하지 않고 필요한 Field만 조회한다는 점에서 읽기 전용 Fetch 전략 대안으로 볼 수 있다.

Q. Fetch Join과 DTO Projection 중 뭐가 좋아?
A. Entity와 연관 Entity가 필요하면 Fetch Join, 필요한 Field만 있으면 DTO Projection이 적합하다.

Q. Projection 결과를 수정해도 DB에 반영돼?
A. 아니다. Projection DTO는 Managed Entity가 아니며 Dirty Checking 대상이 아니다.

Q. Projection으로 N+1을 막을 수 있어?
A. 연관 Field를 Query에서 직접 조회하면 DTO 변환 중 Lazy 접근이 줄어 N+1 방지에 도움이 된다.

Q. Batch Size는 뭐야?
A. Lazy Loading 시 여러 연관 Entity 조회를 IN Query 등으로 묶어 Query 수를 줄이는 Hibernate 최적화 방법이다.

Q. Batch Size는 N+1을 완전히 해결해?
A. 아니다. Query 수를 줄여 완화하지만 Fetch Join이나 Projection처럼 Query 구조를 바꾸는 것과 다르다.

Q. Batch Size는 언제 검토해?
A. Collection Fetch Join이 Pagination 문제를 만들 때나 Lazy Loading 반복 Query를 완화하고 싶을 때 검토한다.

Q. EntityGraph는 뭐야?
A. 특정 조회에서 함께 로딩할 연관 Entity를 선언적으로 지정하는 JPA 기능이다.

Q. EntityGraph와 Fetch Join은 뭐가 달라?
A. Fetch Join은 JPQL에 직접 작성하고 EntityGraph는 Repository Method에 로딩 대상을 선언한다.

Q. EntityGraph도 N+1 해결에 도움이 돼?
A. 필요한 연관 Entity를 함께 로딩할 수 있어 N+1 완화에 도움이 될 수 있다.

Q. Fetch Strategy 검수에서 가장 먼저 확인할 것은 뭐야?
A. Association의 FetchType과 목록 API의 DTO 변환 중 Lazy Field 접근 여부를 먼저 확인한다.

Q. SQL 로그에서 무엇을 봐야 해?
A. API 하나가 실행하는 Query 수, 반복 SELECT, Join, Count Query, Row 증가를 확인해야 한다.

Q. Fetch Join이 있으면 무조건 좋은 Query야?
A. 아니다. 필요한 연관 Entity만 가져오는지, Collection과 Pagination 충돌이 없는지 확인해야 한다.

Q. LazyInitializationException이 나면 첫 번째로 뭘 확인해?
A. Lazy Field 접근 위치와 Transaction이 이미 종료되었는지 확인한다.

Q. N+1 Troubleshooting에서 가장 먼저 볼 것은 뭐야?
A. SQL 로그에서 반복 SELECT가 발생하는 Table을 먼저 확인한다.

Q. 반복 SELECT 대상이 users면 뭘 의심해?
A. Post.user, Comment.user 같은 ManyToOne Lazy Association 접근을 의심한다.

Q. N+1 해결 후에도 성능이 나쁠 수 있어?
A. 그렇다. Fetch Join으로 데이터 양이 과도하게 늘거나 Pagination 문제가 생길 수 있다.

Q. Fetch Strategy에서 가장 흔한 실수는 뭐야?
A. `ManyToOne` 기본 EAGER를 방치하거나 Lazy 문제를 EAGER로 덮는 것이다.

Q. Fetch Join에서 가장 흔한 실수는 뭐야?
A. Collection Fetch Join과 Pagination을 함께 사용하는 것이다.

Q. JPA Part06에서 가장 중요한 기준은 뭐야?
A. ManyToOne LAZY, EAGER 남용 방지, N+1 SQL 로그 확인, Fetch Join과 Projection 선택, Collection Fetch Join Pagination 주의다.

Q. JPA Part06 다음에는 무엇을 다뤄?
A. Part07에서 Transaction Boundary, Cascade, orphanRemoval, Auditing, Page, Slice, Pagination을 다룬다.
