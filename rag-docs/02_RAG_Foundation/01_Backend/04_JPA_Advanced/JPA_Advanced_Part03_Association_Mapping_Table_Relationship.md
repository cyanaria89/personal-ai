# JPA Advanced Part03 — Association Mapping and Table Relationship

---

# 1. Association Mapping Purpose

## 1.1 Association Mapping Concept

### [개념]

Association Mapping은 Entity 간 관계를 Java 객체 참조와 DB Foreign Key로 연결하는 JPA Mapping이다.

SQL Foundation의 Table Relationship은 Primary Key / Foreign Key 기준으로 관계를 표현하고, JPA Association Mapping은 이를 객체 참조로 표현한다.

---

### [핵심]

핵심 키워드:

- Association Mapping
- Table Relationship
- Primary Key
- Foreign Key
- Referential Integrity
- `@ManyToOne`
- `@OneToMany`
- `@OneToOne`
- `@ManyToMany`
- `@JoinColumn`
- `mappedBy`
- Owning Side
- Inverse Side
- Unidirectional
- Bidirectional

Association Mapping 기준:

```text
SQL Table Relationship
→ Primary Key / Foreign Key
→ JPA Association Mapping
→ Entity Reference
→ Owning Side
→ JoinColumn / mappedBy
```

---

### [실무]

JPA 연관관계 설계 흐름:

```text
Requirement 확인
→ SQL Table Relationship 확인
→ Foreign Key 위치 확인
→ Entity 탐색 방향 결정
→ 단방향 / 양방향 결정
→ Owning Side 결정
→ JoinColumn 설정
→ FetchType 설정
→ Cascade 필요 여부 검토
→ N+1 가능성 검토
```

SQL Foundation 연결:

```text
SQL Part01 Table Relationship
→ JPA Association Mapping

SQL Part02 JOIN
→ JPQL Join / Fetch Join

SQL Part04 Foreign Key / Constraint
→ JPA JoinColumn / Referential Integrity

SQL Part05 Backend Integration
→ Repository Query / DTO Mapping / N+1 Review
```

주의:

- JPA Association은 DB Foreign Key를 객체 참조로 표현한다.
- 객체 참조 방향과 DB Foreign Key 위치는 다를 수 있다.
- 연관관계 주인은 DB Foreign Key를 가진 쪽이 기준이다.
- 모든 관계를 양방향으로 만들 필요는 없다.
- Association Mapping은 Query 성능과 N+1 문제에 직접 연결된다.

---

### [FAQ]

Q. Association Mapping은 뭐야?
A. Entity 간 관계를 Java 객체 참조와 DB Foreign Key로 연결하는 JPA Mapping이다.

Q. Table Relationship과 Association Mapping은 같은 거야?
A. 아니다. Table Relationship은 DB PK / FK 관계이고 Association Mapping은 이를 Entity 객체 참조로 표현한 것이다.

Q. JPA 연관관계는 SQL JOIN과 같은 거야?
A. 아니다. 연관관계는 Mapping이고 JOIN은 Query 실행 방식이다. 연관관계가 있다고 항상 JOIN SQL이 실행되는 것은 아니다.

Q. Association Mapping에서 가장 먼저 확인할 것은 뭐야?
A. DB Foreign Key가 어느 Table에 있는지 먼저 확인해야 한다.

---

## 1.2 Table Relationship to Entity Association

### [개념]

Table Relationship은 DB Table 간 Primary Key / Foreign Key 관계다.

Entity Association은 Table Relationship을 Java 객체 참조로 표현한다.

---

### [핵심]

SQL 기준:

```text
users.user_id
← posts.user_id

users: Parent Table
posts: Child Table
posts.user_id: Foreign Key
```

JPA 기준:

```text
Post
→ User user

User
→ List<Post> posts optional
```

관계 변환:

| SQL Relationship           | JPA Association                |
| -------------------------- | ------------------------------ |
| Child Table FK             | `@ManyToOne`                   |
| Parent에서 Child 목록 탐색 | `@OneToMany(mappedBy = "...")` |
| 1:1 FK                     | `@OneToOne`                    |
| N:M 관계                   | 중간 Entity로 분리             |

---

### [실무]

SQL Table 예시:

```sql
create table users (
    user_id bigint primary key
);

create table posts (
    post_id bigint primary key,
    user_id bigint not null,
    foreign key (user_id) references users(user_id)
);
```

JPA Entity 예시:

```java
@Entity
public class Post {

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;
}
```

객체 탐색 기준:

```text
Post에서 작성자 User 필요
→ Post.user

User에서 작성한 Post 목록 필요
→ User.posts optional
```

권장:

- DB Foreign Key 위치를 기준으로 Mapping 시작
- Many 쪽 Entity에 `@ManyToOne` 우선 설계
- Parent에서 Child 목록이 실제로 필요할 때만 `@OneToMany` 추가
- 양방향은 API / Business Requirement가 있을 때만 사용
- JPA Mapping 후 생성 SQL 또는 DB Schema 확인

주의:

- Entity Reference가 있다고 DB FK Constraint가 자동으로 운영 DB에 보장되는 것은 아니다.
- DB FK Constraint와 JPA Association은 역할이 다르다.
- JPA Association이 없어도 Repository Query로 Join 조회는 가능하다.
- 단순 ID 참조만 필요한 경우 객체 연관관계 대신 FK ID만 보관하는 설계도 검토 가능하다.

---

### [FAQ]

Q. DB Foreign Key가 있으면 JPA Association을 반드시 만들어야 해?
A. 반드시 그렇지는 않다. 객체 탐색이 필요하면 Association을 만들고, 단순 ID 참조만 필요하면 FK ID만 관리하는 설계도 가능하다.

Q. Parent Table 쪽에도 항상 List를 만들어야 해?
A. 아니다. Parent에서 Child 목록 탐색이 실제로 필요할 때만 `@OneToMany`를 추가한다.

Q. JPA Association이 있으면 DB FK Constraint도 자동으로 있다고 봐도 돼?
A. 아니다. 운영 DB Schema와 Migration에서 실제 FK Constraint 존재 여부를 확인해야 한다.

Q. Foreign Key 위치와 객체 탐색 방향은 항상 같아?
A. 아니다. Foreign Key는 DB 저장 기준이고 객체 탐색 방향은 Application 사용 기준이다.

---

# 2. Direction Rules

## 2.1 Unidirectional Association

### [개념]

Unidirectional Association은 한 Entity에서 다른 Entity로만 객체 탐색이 가능한 연관관계다.

단방향 연관관계는 구조가 단순하고 유지보수하기 쉽다.

---

### [핵심]

핵심 키워드:

- Unidirectional
- Single Direction Navigation
- Simple Mapping
- Low Coupling
- ManyToOne First
- JoinColumn
- Foreign Key Owner

단방향 예:

```text
Post
→ User

User
X Post 목록 없음
```

---

### [실무]

단방향 `ManyToOne` 예시:

```java
@Entity
public class Post {

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;
}
```

권장:

- 연관관계는 단방향부터 시작
- 실제 반대 방향 탐색 요구가 생기면 양방향 검토
- Many 쪽에서 One 쪽으로 참조하는 `ManyToOne` 단방향이 가장 흔함
- 단방향으로 충분하면 양방향을 만들지 않음
- DTO 응답은 필요한 Query로 구성

주의:

- 단방향이어도 DB Foreign Key는 존재할 수 있다.
- Parent에서 Child 목록이 필요하면 별도 Repository Query로 조회 가능하다.
- 단방향 관계가 성능상 무조건 좋은 것은 아니다.
- 단방향은 객체 탐색 제한이 있지만 구조가 명확하다.

---

### [FAQ]

Q. JPA 연관관계는 단방향으로 시작하는 게 좋아?
A. 그렇다. 단방향으로 충분하면 구조가 단순하고 유지보수하기 좋다.

Q. 단방향이면 반대쪽 조회는 못 해?
A. 객체 탐색은 못 하지만 Repository Query로 반대 방향 조회는 가능하다.

Q. 단방향 `ManyToOne`은 실무에서 많이 써?
A. 많이 사용한다. Foreign Key를 가진 Many 쪽에서 One 쪽을 참조하는 구조가 흔하다.

Q. 단방향이면 mappedBy가 필요해?
A. 아니다. `mappedBy`는 양방향 관계의 반대편에서 사용한다.

---

## 2.2 Bidirectional Association

### [개념]

Bidirectional Association은 두 Entity가 서로를 객체 참조로 탐색할 수 있는 연관관계다.

DB에는 방향이 없지만 JPA 객체 모델에서는 양쪽 참조가 필요할 수 있다.

---

### [핵심]

핵심 키워드:

- Bidirectional
- Owning Side
- Inverse Side
- `mappedBy`
- `@JoinColumn`
- Object State Consistency
- Convenience Method
- Circular Reference Caution

양방향 예:

```text
Post
→ User

User
→ List<Post>
```

---

### [실무]

양방향 예시:

```java
@Entity
public class User {

    @OneToMany(mappedBy = "user")
    private List<Post> posts = new ArrayList<>();
}

@Entity
public class Post {

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;
}
```

편의 Method 예시:

```java
public void changeUser(User user) {
    this.user = user;
    user.getPosts().add(this);
}
```

권장:

- 양방향은 실제 양쪽 탐색이 필요할 때만 사용
- Foreign Key를 가진 쪽을 Owning Side로 설정
- 반대편은 `mappedBy` 사용
- 양쪽 객체 상태를 맞추는 편의 Method 제공
- DTO 변환 시 순환 참조 주의

주의:

- 양방향은 DB 관계가 두 개 생기는 것이 아니다.
- `mappedBy` 쪽은 Foreign Key를 직접 관리하지 않는다.
- 양쪽 객체 상태가 불일치할 수 있다.
- JSON 직렬화 시 순환 참조 문제가 발생할 수 있다.
- 무분별한 양방향은 Entity 복잡도를 높인다.

---

### [FAQ]

Q. 양방향 관계는 DB FK가 두 개 생기는 거야?
A. 아니다. DB FK는 하나이고 객체 참조만 양쪽에 있는 것이다.

Q. 양방향 관계는 언제 써?
A. 양쪽 Entity에서 객체 탐색이 실제로 필요할 때 사용한다.

Q. 양방향 관계에서 mappedBy는 왜 필요해?
A. 반대편 Entity가 연관관계 주인이 아니며 FK를 직접 관리하지 않음을 표시하기 위해 필요하다.

Q. 양방향 관계의 위험은 뭐야?
A. 객체 상태 불일치, 순환 참조, Lazy Loading 문제, Entity 복잡도 증가가 발생할 수 있다.

---

## 2.3 Direction Decision Rule

### [개념]

Direction Decision Rule은 Entity 연관관계를 단방향으로 둘지 양방향으로 둘지 결정하는 기준이다.

기본은 단방향이며, 실제 탐색 요구가 있을 때만 양방향을 추가한다.

---

### [핵심]

판단 기준:

```text
한쪽에서만 탐색 필요
→ 단방향

양쪽에서 객체 탐색 필요
→ 양방향 검토

Parent에서 Child 목록이 크고 페이징 필요
→ 양방향 Collection보다 Repository Query 검토

API 응답만 필요
→ DTO Projection / Query로 해결 가능
```

비교:

| 기준           | 단방향      | 양방향           |
| -------------- | ----------- | ---------------- |
| 구조           | 단순        | 복잡             |
| 객체 탐색      | 한쪽만 가능 | 양쪽 가능        |
| mappedBy       | 없음        | 필요             |
| 객체 상태 관리 | 쉬움        | 양쪽 동기화 필요 |
| 순환 참조 위험 | 낮음        | 높음             |
| 권장           | 기본 선택   | 필요 시 선택     |

---

### [실무]

결정 Flow:

```text
Requirement 확인
→ 객체 탐색 방향 확인
→ 반대 방향 탐색이 실제 필요한지 확인
→ 목록 크기 확인
→ Pagination 필요 여부 확인
→ 단방향 / 양방향 결정
→ DTO 응답 구조 확인
```

예시 판단:

```text
Comment → Post 필요
→ ManyToOne 단방향 가능

Post → Comments 목록 필요하지만 페이징 필요
→ Post.comments보다 CommentRepository 조회 검토

User → Posts가 관리자 화면에서만 필요
→ Repository Query로 해결 가능

Order → OrderItems가 Aggregate 내부에서 항상 함께 필요
→ 양방향 또는 OneToMany 관리 검토
```

권장:

- 단방향으로 시작
- 양방향은 필요가 확인될 때 추가
- 큰 Collection은 Entity Collection보다 Repository Query 우선 검토
- DTO 응답 때문에 양방향을 만들지 않음
- 연관관계 추가 전 N+1 가능성 검토

주의:

- 화면에 필요하다는 이유만으로 양방향을 만들지 않는다.
- 조회 요구사항은 Query로 해결 가능하다.
- 양방향 Collection은 Pagination과 성능 문제를 만들 수 있다.
- Entity 관계는 API 응답 구조와 분리해서 판단한다.

---

### [FAQ]

Q. DTO 응답에 자식 목록이 필요하면 양방향을 만들어야 해?
A. 아니다. Repository Query나 DTO Projection으로 조회할 수 있다.

Q. Parent에서 Child 목록을 자주 조회하면 `@OneToMany`가 필요해?
A. 항상 필요한 것은 아니다. 목록 크기와 Pagination 요구사항을 확인해야 한다.

Q. 양방향을 나중에 추가해도 돼?
A. 가능하다. 처음에는 단방향으로 시작하고 필요가 명확해지면 추가하는 것이 좋다.

Q. 연관관계 방향 결정에서 가장 중요한 기준은 뭐야?
A. 객체 탐색이 실제로 필요한 방향과 Collection 크기, Pagination 필요 여부다.

---

# 3. Owning Side Rules

## 3.1 Owning Side Concept

### [개념]

Owning Side는 JPA 연관관계에서 Foreign Key 값을 실제로 관리하는 쪽이다.

연관관계 주인은 DB Foreign Key를 가진 Entity가 기준이다.

---

### [핵심]

핵심 키워드:

- Owning Side
- Inverse Side
- Foreign Key
- `@JoinColumn`
- `mappedBy`
- Relationship Update
- FK Management

판단 기준:

```text
DB Foreign Key를 가진 쪽
→ Owning Side

@JoinColumn이 있는 쪽
→ Owning Side

mappedBy가 없는 쪽
→ Owning Side

mappedBy가 있는 쪽
→ Inverse Side
```

---

### [실무]

예시:

```java
@Entity
public class Comment {

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "post_id", nullable = false)
    private Post post;
}

@Entity
public class Post {

    @OneToMany(mappedBy = "post")
    private List<Comment> comments = new ArrayList<>();
}
```

해석:

```text
comments table
→ post_id Foreign Key 보유

Comment.post
→ Owning Side

Post.comments
→ Inverse Side
→ mappedBy = "post"
```

권장:

- Foreign Key 위치를 먼저 확인
- FK를 가진 Entity에 `@JoinColumn` 설정
- 반대편 Collection에는 `mappedBy` 설정
- 객체 상태 일관성을 위해 편의 Method 사용
- Review 시 `mappedBy` 값이 상대 Entity Field 이름과 일치하는지 확인

주의:

- Owning Side는 객체 참조 방향이 아니라 DB FK 기준이다.
- `mappedBy` 값은 Column 이름이 아니라 상대 Entity의 Field 이름이다.
- Inverse Side만 변경하면 DB FK가 변경되지 않을 수 있다.
- 양방향 관계에서는 양쪽 객체 상태를 함께 맞춰야 한다.

---

### [FAQ]

Q. 연관관계 주인은 어떻게 정해?
A. DB Foreign Key를 가진 Entity가 연관관계 주인이다.

Q. `mappedBy`가 있는 쪽이 주인이야?
A. 아니다. `mappedBy`가 있는 쪽은 주인이 아니며 FK를 직접 관리하지 않는다.

Q. `mappedBy`에는 DB Column 이름을 써?
A. 아니다. 상대 Entity의 Field 이름을 쓴다.

Q. Owning Side만 설정하면 반대편 객체 상태도 자동으로 맞아?
A. 아니다. DB 반영은 주인 쪽 기준이지만 객체 상태 일관성을 위해 양쪽을 함께 맞추는 것이 좋다.

---

## 3.2 JoinColumn Rule

### [개념]

`@JoinColumn`은 Association Mapping에서 Foreign Key Column을 지정하는 Annotation이다.

Foreign Key를 가진 Owning Side에 주로 사용한다.

---

### [핵심]

핵심 키워드:

- `@JoinColumn`
- Foreign Key Column
- Owning Side
- nullable
- name
- referencedColumnName
- FK Constraint
- Data Integrity

주요 속성:

| 속성                   | 역할                    |
| ---------------------- | ----------------------- |
| `name`                 | FK Column 이름          |
| `nullable`             | FK NULL 허용 여부       |
| `referencedColumnName` | 참조 대상 Column        |
| `foreignKey`           | FK Constraint 이름 지정 |
| `insertable`           | INSERT 포함 여부        |
| `updatable`            | UPDATE 포함 여부        |

---

### [실무]

기본 예시:

```java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "user_id", nullable = false)
private User user;
```

SQL 연결:

```text
posts.user_id
→ users.user_id 참조

@JoinColumn(name = "user_id")
→ posts table의 FK Column 지정
```

권장:

- FK Column 이름을 명확히 지정
- 필수 관계는 `nullable = false`
- Optional 관계는 nullable 허용 여부 명확화
- FK Constraint 이름은 Migration에서 명시 가능
- DB Schema의 Column 이름과 일치 확인

주의:

- `@JoinColumn(name = "user_id")`의 name은 현재 Entity Table의 FK Column 이름이다.
- `referencedColumnName`은 특별한 경우가 아니면 생략 가능하다.
- `@JoinColumn(nullable = false)`와 실제 DB NOT NULL Constraint 일치 여부를 확인해야 한다.
- FK Constraint는 운영 DB Schema에서 실제 존재하는지 확인해야 한다.
- `@Column`이 아니라 `@JoinColumn`으로 Association FK를 Mapping한다.

---

### [FAQ]

Q. `@JoinColumn`은 뭐야?
A. Association Mapping에서 Foreign Key Column을 지정하는 Annotation이다.

Q. `@JoinColumn(name = "user_id")`의 `name`은 어느 Table Column이야?
A. 현재 Entity가 Mapping되는 Table의 Foreign Key Column 이름이다.

Q. Association Field에 `@Column`을 쓰면 돼?
A. 아니다. Entity Association에는 `@JoinColumn`을 사용한다.

Q. `referencedColumnName`은 꼭 써야 해?
A. 보통 Primary Key를 참조하면 생략 가능하다. 특수한 Column을 참조할 때 사용한다.

---

## 3.3 mappedBy Rule

### [개념]

`mappedBy`는 양방향 연관관계에서 현재 쪽이 연관관계 주인이 아님을 표시하는 속성이다.

`mappedBy` 값은 상대 Entity의 Association Field 이름이다.

---

### [핵심]

핵심 키워드:

- `mappedBy`
- Inverse Side
- Owning Side Reference
- Field Name
- Not Column Name
- Bidirectional Association

기준:

```text
Post.comments mappedBy = "post"

의미:
Comment Entity의 post Field가 Owning Side
```

---

### [실무]

예시:

```java
@Entity
public class Post {

    @OneToMany(mappedBy = "post")
    private List<Comment> comments = new ArrayList<>();
}

@Entity
public class Comment {

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "post_id", nullable = false)
    private Post post;
}
```

잘못된 예시:

```java
@OneToMany(mappedBy = "post_id")
private List<Comment> comments = new ArrayList<>();
```

문제:

```text
mappedBy = "post_id"
→ DB Column 이름 사용
→ 잘못된 Mapping
→ 상대 Entity Field 이름인 "post"를 사용해야 함
```

권장:

- `mappedBy`는 상대 Entity Field 이름 사용
- Collection은 빈 컬렉션으로 초기화
- mappedBy 쪽만 변경하지 않음
- 양방향 편의 Method로 양쪽 상태 동기화
- Review 시 mappedBy 오타 확인

주의:

- `mappedBy` 쪽은 FK를 직접 관리하지 않는다.
- `mappedBy` 값 오타는 Mapping Error를 만든다.
- `mappedBy`에는 DB Column 이름을 쓰지 않는다.
- mappedBy Collection을 무분별하게 조회하면 성능 문제가 생길 수 있다.

---

### [FAQ]

Q. `mappedBy`는 뭐야?
A. 양방향 연관관계에서 현재 쪽이 연관관계 주인이 아님을 표시하는 속성이다.

Q. `mappedBy`에는 무엇을 써야 해?
A. 상대 Entity의 Association Field 이름을 써야 한다.

Q. `mappedBy = "post_id"`처럼 Column 이름을 쓰면 돼?
A. 아니다. Column 이름이 아니라 상대 Entity Field 이름을 써야 한다.

Q. `mappedBy` 쪽에서 Collection에 add하면 DB FK가 변경돼?
A. 주인 쪽이 함께 변경되지 않으면 DB FK 반영이 기대와 다를 수 있다.

---

# 4. ManyToOne Rules

## 4.1 ManyToOne Concept

### [개념]

`ManyToOne`은 여러 Entity가 하나의 Entity를 참조하는 관계다.

DB에서는 Many 쪽 Table이 Foreign Key를 가진다.

---

### [핵심]

사용 예:

- Post → User
- Comment → Post
- Review → User
- Favorite → Festival
- OrderItem → Order
- ChatMessage → ChatRoom
- Notification → User

핵심 키워드:

- `@ManyToOne`
- Many Side
- One Side
- Foreign Key
- `@JoinColumn`
- Owning Side
- FetchType.LAZY

---

### [실무]

기본 예시:

```java
@Entity
public class Comment {

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "post_id", nullable = false)
    private Post post;
}
```

SQL 연결:

```text
comments.post_id
→ posts.post_id

Comment
→ Post

Many Comment
→ One Post
```

권장:

- `fetch = FetchType.LAZY` 명시
- `@JoinColumn` 이름 명확화
- 필수 관계는 `nullable = false`
- Many 쪽이 Owning Side
- DTO 변환 시 연관 Entity 접근으로 인한 Lazy Loading 주의
- 목록 조회 시 N+1 가능성 검토

주의:

- `ManyToOne` 기본 Fetch는 EAGER다.
- EAGER 기본값에 의존하지 않는다.
- LAZY로 바꿔도 N+1 문제가 자동 해결되는 것은 아니다.
- Transaction 밖에서 Lazy Field 접근 시 LazyInitializationException 발생 가능
- 연관 Entity를 Response로 직접 노출하지 않는다.

---

### [FAQ]

Q. `ManyToOne`은 언제 써?
A. 여러 Entity가 하나의 Entity를 참조하는 관계에서 사용한다.

Q. `ManyToOne`에서 Foreign Key는 어느 쪽에 있어?
A. Many 쪽 Table에 Foreign Key가 있다.

Q. `ManyToOne`은 왜 LAZY를 명시해?
A. 기본 Fetch가 EAGER라 불필요한 Join과 조회가 발생할 수 있으므로 LAZY를 명시하는 것이 좋다.

Q. `ManyToOne`이 있으면 N+1이 생길 수 있어?
A. 그렇다. 목록 조회 후 연관 Entity getter를 반복 호출하면 N+1 문제가 발생할 수 있다.

---

## 4.2 ManyToOne Review Rule

### [개념]

ManyToOne Review Rule은 Many 쪽 Entity가 Foreign Key와 Association을 올바르게 Mapping했는지 검수하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] Many 쪽 Entity에 @ManyToOne이 있는가?
- [ ] fetch = FetchType.LAZY를 명시했는가?
- [ ] @JoinColumn name이 DB FK Column과 일치하는가?
- [ ] nullable 기준이 관계 필수성과 맞는가?
- [ ] Many 쪽이 Owning Side로 설정되었는가?
- [ ] 연관 Entity를 API Response로 직접 노출하지 않는가?
- [ ] DTO 변환 시 Lazy Loading 발생 가능성을 검토했는가?
- [ ] 목록 조회에서 N+1 가능성을 검토했는가?
```

---

### [실무]

Common Finding:

```text
문제: @ManyToOne에 FetchType.LAZY 누락
위험: 기본 EAGER로 불필요한 조회 발생
해결: @ManyToOne(fetch = FetchType.LAZY)

문제: @JoinColumn 이름 불명확
위험: 예상과 다른 FK Column 생성
해결: @JoinColumn(name = "user_id") 명시

문제: DTO 변환 중 post.getUser().getNickname() 반복
위험: N+1 Query 발생
해결: Fetch Join 또는 DTO Projection 검토
```

좋은 예:

```java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "user_id", nullable = false)
private User user;
```

나쁜 예:

```java
@ManyToOne
private User user;
```

문제:

- 기본 EAGER
- JoinColumn 이름 예측 어려움
- nullable 의도 불명확

---

### [FAQ]

Q. `ManyToOne` 검수에서 가장 중요한 것은 뭐야?
A. FetchType.LAZY, JoinColumn 이름, nullable 기준, N+1 가능성이다.

Q. `ManyToOne`에 `@JoinColumn`을 생략해도 돼?
A. 가능하지만 FK Column 이름을 명확히 하기 위해 명시하는 것이 좋다.

Q. `ManyToOne`의 nullable은 어떻게 정해?
A. 관계가 필수이면 `nullable = false`, 선택이면 nullable 허용 여부를 명확히 한다.

Q. `ManyToOne`이 있으면 항상 Fetch Join해야 해?
A. 아니다. 해당 조회에서 연관 Entity가 실제 필요하고 추가 Query가 문제가 될 때 Fetch Join을 검토한다.

---

# 5. OneToMany Rules

## 5.1 OneToMany Concept

### [개념]

`OneToMany`는 하나의 Entity가 여러 자식 Entity Collection을 참조하는 관계다.

대부분 양방향 관계의 Inverse Side로 사용하며 `mappedBy`를 사용한다.

---

### [핵심]

사용 예:

- User → Posts
- Post → Comments
- Festival → Reviews
- ChatRoom → ChatMessages
- Order → OrderItems

핵심 키워드:

- `@OneToMany`
- Collection
- `mappedBy`
- Inverse Side
- Parent Entity
- Child Entity
- Pagination Caution
- Collection Fetch Join Caution

---

### [실무]

기본 예시:

```java
@Entity
public class Post {

    @OneToMany(mappedBy = "post")
    private List<Comment> comments = new ArrayList<>();
}
```

상대 Entity:

```java
@Entity
public class Comment {

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "post_id", nullable = false)
    private Post post;
}
```

권장:

- `mappedBy`로 Inverse Side 표시
- Collection은 빈 컬렉션으로 초기화
- 큰 Collection을 무분별하게 탐색하지 않음
- 목록 API는 별도 Repository Query 검토
- Pagination이 필요한 자식 목록은 Repository에서 조회
- Cascade / orphanRemoval은 생명주기 종속성이 명확할 때만 사용

주의:

- OneToMany Collection 조회는 성능 문제를 만들 수 있다.
- Collection Fetch Join과 Pagination 조합은 위험하다.
- Entity Collection을 API Response로 직접 반환하지 않는다.
- 큰 Collection은 메모리 사용량과 N+1 문제를 유발할 수 있다.
- 단순 목록 응답 때문에 OneToMany를 추가하지 않는다.

---

### [FAQ]

Q. `OneToMany`는 언제 써?
A. Parent Entity에서 Child Collection을 객체 탐색해야 할 때 사용한다.

Q. `OneToMany`에는 왜 `mappedBy`를 써?
A. 상대 Entity가 Foreign Key를 가진 Owning Side임을 표시하기 위해 사용한다.

Q. `OneToMany` Collection은 꼭 초기화해야 해?
A. 빈 컬렉션으로 초기화하는 것이 NullPointerException을 줄이고 사용이 편하다.

Q. 자식 목록 API는 Entity Collection으로 반환해도 돼?
A. 권장하지 않는다. DTO로 변환하고 큰 목록은 별도 Query와 Pagination을 고려해야 한다.

---

## 5.2 OneToMany Pagination Caution

### [개념]

OneToMany Pagination Caution은 Parent Entity의 Collection을 직접 조회하거나 Fetch Join할 때 Pagination이 깨질 수 있는 문제를 다룬다.

---

### [핵심]

문제 상황:

- Parent 목록 + Child Collection Fetch Join
- Collection 중복 Row 발생
- DB Pagination 적용 어려움
- Memory Pagination 가능성
- N+1 해결 시도 중 과도한 Join 발생

위험 Query 예:

```text
Post 목록 조회
→ comments Collection Fetch Join
→ Post Row 중복
→ Pagination 불안정
```

---

### [실무]

비권장 흐름:

```text
Page<Post> posts 조회
→ posts.comments Fetch Join
→ 중복 Row
→ Pagination 문제
```

권장 후보:

```text
방법 1:
Parent 목록 Page / Slice 조회
→ Child는 필요한 경우 별도 Query

방법 2:
DTO Projection으로 필요한 값만 조회

방법 3:
Batch Size 설정 검토

방법 4:
API 응답 구조 변경
```

Repository Query 예:

```java
Slice<Comment> findByPost_PostIdOrderByCreatedAtDesc(Long postId, Pageable pageable);
```

권장:

- 자식 목록은 Child Repository에서 Pagination 조회
- Parent 상세에서 소량 Child만 필요하면 별도 제한 Query 검토
- Collection Fetch Join과 Pageable 조합 주의
- 목록 화면은 DTO Projection 검토
- SQL 로그로 Query 수와 Row 수 확인

주의:

- `distinct`만으로 Pagination 문제가 완전히 해결되지 않을 수 있다.
- Collection Fetch Join은 단건 상세 또는 제한된 상황에서만 신중히 사용한다.
- 무한 스크롤은 `Slice`가 적합할 수 있다.
- Page는 Count Query 비용을 검토해야 한다.

---

### [FAQ]

Q. `OneToMany` Collection Fetch Join에 Pagination을 같이 써도 돼?
A. 주의해야 한다. DB Pagination이 기대대로 동작하지 않거나 메모리에서 처리될 수 있다.

Q. 자식 목록 Pagination은 어떻게 하는 게 좋아?
A. Child Repository에서 Parent ID 조건으로 `Page`나 `Slice` 조회하는 방식이 안정적이다.

Q. `distinct`를 쓰면 Collection Fetch Join Pagination 문제가 해결돼?
A. 중복 제거에는 도움될 수 있지만 Pagination 문제를 완전히 해결하지 못할 수 있다.

Q. OneToMany N+1은 어떻게 해결해?
A. Fetch Join, Batch Size, 별도 Query, DTO Projection, API 구조 변경 중 상황에 맞게 선택한다.

---

# 6. OneToOne Rules

## 6.1 OneToOne Concept

### [개념]

`OneToOne`은 하나의 Entity가 하나의 Entity와 연결되는 관계다.

DB에서는 한쪽 Table이 Foreign Key를 가지거나 Primary Key를 공유하는 방식으로 표현할 수 있다.

---

### [핵심]

사용 예:

- User → UserProfile
- Order → Payment
- Member → Locker
- User → UserSetting

핵심 키워드:

- `@OneToOne`
- Unique Foreign Key
- Shared Primary Key
- Owning Side
- `@JoinColumn`
- FetchType.LAZY
- Optional Relationship
- Embedded Alternative

---

### [실무]

기본 예시:

```java
@Entity
public class User {

    @OneToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "profile_id")
    private UserProfile profile;
}
```

반대편 예시:

```java
@Entity
public class UserProfile {

    @OneToOne(mappedBy = "profile")
    private User user;
}
```

권장:

- FK 위치를 명확히 결정
- Owning Side 확인
- `FetchType.LAZY` 명시 검토
- 실제로 1:1 분리가 필요한지 검토
- 생명주기가 같으면 Embedded Value Type도 검토
- 관계가 선택인지 필수인지 nullable 기준 설정

주의:

- `OneToOne` 기본 Fetch는 EAGER다.
- LAZY가 기대대로 동작하지 않을 수 있는 상황이 있다.
- 테이블 분리 필요성이 약하면 같은 Entity 또는 Embedded가 더 단순할 수 있다.
- 양방향 OneToOne은 Mapping 복잡도가 올라간다.
- 조회 SQL을 반드시 확인해야 한다.

---

### [FAQ]

Q. `OneToOne`은 언제 써?
A. 두 데이터가 독립 Table로 분리되어야 하고 1:1 관계가 명확할 때 사용한다.

Q. `OneToOne`도 LAZY를 써야 해?
A. 불필요한 즉시 로딩을 막기 위해 LAZY를 고려하지만 구현체 제약으로 기대와 다르게 동작할 수 있어 SQL 확인이 필요하다.

Q. UserProfile은 OneToOne이 좋아?
A. 독립 Table로 분리할 이유가 명확하면 OneToOne을 사용할 수 있고, 단순 값 묶음이면 Embedded도 검토할 수 있다.

Q. `OneToOne`에서 FK는 어느 쪽에 둬야 해?
A. 조회 방향, 생명주기, 필수 관계 여부, DB 제약을 고려해 결정한다.

---

## 6.2 OneToOne Review Rule

### [개념]

OneToOne Review Rule은 1:1 관계가 실제로 필요한지, FK 위치와 Fetch 전략이 적절한지 검수하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] 실제 1:1 Table 분리가 필요한가?
- [ ] Embedded로 대체 가능한 값 객체인가?
- [ ] Foreign Key 위치가 명확한가?
- [ ] Owning Side가 명확한가?
- [ ] @JoinColumn 이름이 명확한가?
- [ ] FetchType.LAZY를 검토했는가?
- [ ] LAZY 동작 여부를 SQL 로그로 확인했는가?
- [ ] 관계가 필수인지 선택인지 nullable 기준이 있는가?
- [ ] 양방향이 꼭 필요한가?
```

---

### [실무]

Review Finding:

```text
문제: 단순 주소 정보를 UserProfile Entity로 OneToOne 분리
위험: 불필요한 Join과 Mapping 복잡도 증가
해결: Address Embedded Value Type 검토

문제: @OneToOne 기본 EAGER 사용
위험: User 조회 시 Profile 즉시 조회
해결: FetchType.LAZY 명시 후 SQL 확인

문제: 양방향 OneToOne 무분별 사용
위험: 객체 순환 참조와 Mapping 복잡도 증가
해결: 단방향 우선 검토
```

Embedded 대안:

```java
@Embedded
private Address address;
```

권장:

- OneToOne은 신중히 사용
- 단순 값 묶음은 Embedded 검토
- 독립 생명주기와 별도 Table 필요성이 있으면 Entity 분리
- 단방향 우선 검토
- SQL 로그로 실제 조회 확인

---

### [FAQ]

Q. OneToOne 검수에서 가장 중요한 것은 뭐야?
A. 실제 Table 분리가 필요한지, Embedded로 대체 가능한지, Fetch 전략이 적절한지 확인하는 것이다.

Q. OneToOne은 성능 문제가 없을까?
A. 기본 EAGER와 불필요한 Join으로 성능 문제가 생길 수 있어 SQL 확인이 필요하다.

Q. OneToOne을 무조건 양방향으로 해야 해?
A. 아니다. 단방향으로 충분하면 단방향이 더 단순하다.

Q. Embedded와 OneToOne은 어떻게 구분해?
A. 독립 식별자가 필요한 Persistence Model이면 OneToOne, 식별자 없는 값 묶음이면 Embedded를 검토한다.

---

# 7. ManyToMany Rules

## 7.1 ManyToMany Caution

### [개념]

`ManyToMany`는 양쪽 Entity가 서로 여러 개를 참조하는 관계다.

실무에서는 `@ManyToMany` 직접 사용보다 중간 Entity를 명시적으로 만들어 `ManyToOne` / `OneToMany`로 풀어내는 것이 일반적이다.

---

### [핵심]

핵심 키워드:

- `@ManyToMany`
- Join Table
- Link Entity
- Middle Entity
- Association Entity
- ManyToOne
- OneToMany
- Extra Column
- Relationship Lifecycle

문제:

- 중간 Table에 추가 Field 넣기 어려움
- 관계 자체를 Entity로 다루기 어려움
- 생성일, 상태, 순서 같은 Column 확장 어려움
- Cascade 위험
- Query 확장 어려움
- 실무 요구사항 변경에 취약

---

### [실무]

비권장 예시:

```java
@ManyToMany
private List<Tag> tags = new ArrayList<>();
```

권장 구조:

```text
Post
→ PostTag
→ Tag
```

중간 Entity 예시:

```java
@Entity
public class PostTag {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long postTagId;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "post_id", nullable = false)
    private Post post;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "tag_id", nullable = false)
    private Tag tag;
}
```

실무 예:

```text
User - Festival
→ Favorite

User - Post
→ Like

Post - Tag
→ PostTag

User - Role
→ UserRole
```

권장:

- ManyToMany 직접 사용 지양
- 중간 Table은 Entity로 승격
- 중간 Entity에 생성일, 상태, 순서 등 확장 가능
- 중복 방지를 위해 복합 Unique Constraint 검토
- 중간 Entity 기준 Repository 설계

주의:

- 좋아요, 찜, 태그는 개념적으로 N:M이지만 중간 Entity가 실무에 적합하다.
- `CascadeType.ALL`을 ManyToMany에 무분별하게 쓰면 위험하다.
- 중간 Entity 없이 시작하면 요구사항 확장 시 리팩토링 비용이 커진다.
- 삭제 정책과 Unique Constraint를 함께 검토해야 한다.

---

### [FAQ]

Q. `ManyToMany`를 바로 쓰면 안 돼?
A. 가능은 하지만 실무에서는 중간 Table에 생성일, 상태 같은 추가 Field가 필요한 경우가 많아 중간 Entity로 풀어내는 것이 좋다.

Q. 좋아요, 찜 같은 관계는 ManyToMany야?
A. 개념적으로는 다대다지만 Like, Favorite 같은 중간 Entity로 표현하는 것이 실무에 적합하다.

Q. Post와 Tag 관계는 어떻게 설계해?
A. `PostTag` 같은 중간 Entity를 만들어 PostTag → Post, PostTag → Tag를 각각 ManyToOne으로 Mapping한다.

Q. ManyToMany에서 Cascade를 써도 돼?
A. 매우 신중해야 한다. 공유 Entity 삭제 전파 위험이 크다.

---

## 7.2 Middle Entity Rule

### [개념]

Middle Entity는 N:M 관계의 중간 Table을 명시적인 Entity로 표현한 것이다.

Middle Entity는 관계 자체의 상태와 메타데이터를 관리할 수 있다.

---

### [핵심]

Middle Entity 사용 상황:

- 관계에 생성일 필요
- 관계에 상태 필요
- 관계에 순서 필요
- 관계에 역할 필요
- 중복 방지 필요
- 관계 삭제 정책 필요
- 관계 자체를 조회해야 함

예시:

| N:M 관계        | Middle Entity |
| --------------- | ------------- |
| User - Festival | Favorite      |
| User - Post     | PostLike      |
| Post - Tag      | PostTag       |
| User - Role     | UserRole      |
| Order - Product | OrderItem     |

---

### [실무]

Favorite 예시:

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

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long favoriteId;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "festival_id", nullable = false)
    private Festival festival;
}
```

Repository 예시:

```java
boolean existsByUser_UserIdAndFestival_FestivalId(Long userId, Long festivalId);

Optional<Favorite> findByUser_UserIdAndFestival_FestivalId(Long userId, Long festivalId);
```

권장:

- Middle Entity에 독립 Primary Key 부여 가능
- user_id + target_id 복합 Unique Constraint 검토
- 생성일 / 수정일 Auditing 적용 가능
- 삭제 정책 명확화
- 중복 생성은 Service 검증 + DB Unique로 방어

주의:

- 중간 Entity도 Entity이므로 DTO 직접 노출 금지
- `ManyToOne`은 LAZY 명시
- 중복 방지는 Repository existsBy만으로 부족하다.
- DB Unique Constraint가 최종 방어선이다.
- 중간 Entity 목록 조회도 N+1 가능성을 검토해야 한다.

---

### [FAQ]

Q. Middle Entity는 뭐야?
A. N:M 관계의 중간 Table을 명시적인 Entity로 표현한 것이다.

Q. Middle Entity에는 ID를 따로 둬도 돼?
A. 가능하다. 실무에서는 단순 관리를 위해 Surrogate Key를 두고 복합 Unique Constraint를 추가하는 경우가 많다.

Q. Favorite이나 Like는 Middle Entity야?
A. 그렇다. User와 대상 Entity 사이의 관계 자체를 표현하는 Middle Entity로 볼 수 있다.

Q. Middle Entity 중복은 어떻게 막아?
A. Service existsBy 검증과 DB 복합 Unique Constraint를 함께 사용한다.

---

# 8. Convenience Method Rules

## 8.1 Bidirectional Convenience Method

### [개념]

Bidirectional Convenience Method는 양방향 연관관계에서 양쪽 객체 참조를 함께 맞추는 Method다.

DB 반영은 Owning Side 기준이지만, 객체 상태 일관성을 위해 양쪽을 함께 설정한다.

---

### [핵심]

핵심 키워드:

- Convenience Method
- Object State Consistency
- Owning Side
- Inverse Side
- Bidirectional Sync
- Add Method
- Change Method
- Remove Method

목적:

- 양쪽 객체 상태 일치
- 연관관계 변경 의도 표현
- 누락 방지
- 테스트 용이성 증가
- Review 가능성 증가

---

### [실무]

Post - Comment 예시:

```java
@Entity
public class Post {

    @OneToMany(mappedBy = "post")
    private List<Comment> comments = new ArrayList<>();

    public void addComment(Comment comment) {
        comments.add(comment);
        comment.changePost(this);
    }
}
```

Comment 예시:

```java
@Entity
public class Comment {

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "post_id", nullable = false)
    private Post post;

    public void changePost(Post post) {
        this.post = post;
    }
}
```

더 안전한 예시:

```java
public void addComment(Comment comment) {
    if (!comments.contains(comment)) {
        comments.add(comment);
    }
    comment.changePost(this);
}
```

권장:

- 편의 Method는 한쪽 Entity에 대표로 둠
- Owning Side 변경을 반드시 포함
- Collection 중복 추가 주의
- remove Method도 필요 시 제공
- Method 이름에 의도 표현

주의:

- 양쪽에 서로 호출하는 Method를 만들면 무한 재귀 위험이 있다.
- `comments.add(comment)`만 하고 `comment.post`를 설정하지 않으면 FK 반영이 누락될 수 있다.
- 편의 Method가 복잡해지면 Aggregate 설계를 검토한다.
- 객체 상태 일관성과 DB 반영 기준을 혼동하지 않는다.

---

### [FAQ]

Q. 양방향 관계에서 편의 Method는 왜 필요해?
A. 양쪽 객체 참조를 함께 맞춰 객체 상태 불일치를 막기 위해 필요하다.

Q. 주인 쪽만 세팅하면 DB에는 반영돼?
A. DB 반영은 주인 쪽 기준이지만 객체 상태 일관성을 위해 반대편도 함께 맞추는 것이 좋다.

Q. 편의 Method는 어느 쪽에 두는 게 좋아?
A. 관계를 관리하는 책임이 자연스러운 Entity 한쪽에 대표로 두는 것이 좋다.

Q. 편의 Method에서 양쪽 Method가 서로 호출해도 돼?
A. 주의해야 한다. 서로 호출하면 무한 재귀가 발생할 수 있다.

---

## 8.2 Association Change and Remove

### [개념]

Association Change and Remove는 Entity 연관관계를 변경하거나 해제할 때 객체 참조와 DB Foreign Key가 일관되도록 처리하는 규칙이다.

---

### [핵심]

연관관계 변경 상황:

- Parent 변경
- Child 추가
- Child 제거
- 관계 해제
- Soft Delete
- Hard Delete
- orphanRemoval 적용 여부
- Cascade REMOVE 적용 여부

---

### [실무]

관계 변경 예시:

```java
public void changePost(Post newPost) {
    this.post = newPost;
}
```

관계 해제 예시:

```java
public void removeComment(Comment comment) {
    comments.remove(comment);
    comment.changePost(null);
}
```

주의:

```text
nullable = false 관계
→ comment.changePost(null) 불가
→ DB Constraint 위반 가능

orphanRemoval = true
→ Collection 제거 시 DELETE 발생 가능

Cascade REMOVE
→ 부모 삭제 시 자식 삭제 전파 가능
```

권장:

- 관계 해제 가능 여부를 nullable 기준과 함께 검토
- 필수 관계는 해제보다 삭제 정책을 명확히 함
- orphanRemoval은 자식 생명주기가 완전히 종속될 때만 사용
- Cascade REMOVE는 공유 Entity에 사용 금지
- 삭제 정책은 Part07 Cascade / Orphan Removal 기준과 연결

주의:

- 관계 해제와 Entity 삭제는 다르다.
- nullable false FK는 null로 관계 해제할 수 없다.
- Collection에서 제거한다고 항상 DB 삭제가 되는 것은 아니다.
- orphanRemoval이 있으면 Collection 제거가 DELETE로 이어질 수 있다.
- 삭제 정책은 API 요구사항과 DB Constraint를 함께 고려해야 한다.

---

### [FAQ]

Q. 연관관계 해제와 Entity 삭제는 같은 거야?
A. 아니다. 관계 해제는 FK를 null로 만들거나 연결을 끊는 것이고, 삭제는 Row를 제거하는 것이다.

Q. nullable false 관계를 null로 바꿔도 돼?
A. 안 된다. DB NOT NULL Constraint 위반이 발생할 수 있다.

Q. Collection에서 자식을 remove하면 DB에서도 삭제돼?
A. orphanRemoval 설정이 있으면 삭제될 수 있고, 없으면 관계 변경만 일어날 수 있다.

Q. Cascade와 orphanRemoval은 어디서 자세히 다뤄?
A. Part07 Transaction, Cascade, Auditing, Pagination에서 상세히 다룬다.

---

# 9. Association and Fetch Strategy Preview

## 9.1 Fetch Strategy Preview

### [개념]

Fetch Strategy는 Association Entity를 언제 조회할지 결정하는 전략이다.

Part03에서는 Association Mapping 시 FetchType을 반드시 고려해야 한다는 기준만 다루고, 상세한 Lazy Loading, Fetch Join, N+1은 Part06에서 다룬다.

---

### [핵심]

핵심 키워드:

- FetchType.LAZY
- FetchType.EAGER
- Lazy Loading
- Eager Loading
- Proxy
- Fetch Join
- N+1 Problem
- LazyInitializationException

기본 Fetch 주의:

| Association   | 기본 Fetch | 권장 검토      |
| ------------- | ---------- | -------------- |
| `@ManyToOne`  | EAGER      | LAZY 명시      |
| `@OneToOne`   | EAGER      | LAZY 명시 검토 |
| `@OneToMany`  | LAZY       | 기본 유지      |
| `@ManyToMany` | LAZY       | 직접 사용 지양 |

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

Association 설계 시 확인:

```text
Association Mapping 작성
→ 기본 Fetch 확인
→ LAZY 명시 여부 확인
→ DTO 변환 위치 확인
→ 목록 조회 N+1 가능성 확인
→ Fetch Join 필요 여부는 Query 단계에서 결정
```

권장:

- `ManyToOne`은 LAZY 명시
- `OneToOne`은 LAZY 명시 검토 후 SQL 확인
- `OneToMany` Collection은 기본 LAZY 유지
- EAGER로 N+1을 해결하려고 하지 않음
- 필요한 조회에서 Fetch Join / DTO Projection 검토

주의:

- LAZY는 N+1을 자동으로 해결하지 않는다.
- EAGER는 불필요한 조회와 복잡한 SQL을 만들 수 있다.
- DTO 변환 중 연관 Field 접근은 추가 Query를 유발할 수 있다.
- Fetch 전략 상세는 Part06에서 다룬다.

---

### [FAQ]

Q. Association Mapping할 때 FetchType도 같이 정해야 해?
A. 그렇다. 특히 `ManyToOne`과 `OneToOne`은 기본 EAGER라 LAZY 명시를 검토해야 한다.

Q. LAZY로 하면 N+1 문제가 없어져?
A. 아니다. LAZY는 조회 시점을 늦출 뿐이고 반복 접근하면 N+1이 발생할 수 있다.

Q. EAGER로 바꾸면 LazyInitializationException이 해결돼?
A. 일부 상황은 피할 수 있지만 불필요한 조회와 성능 문제가 생기므로 권장하지 않는다.

Q. Fetch Join은 어디서 다뤄?
A. Part06 Fetch Strategy, Fetch Join, N+1에서 상세히 다룬다.

---

# 10. Association Mapping Review

## 10.1 Association Mapping Checklist

### [개념]

Association Mapping Checklist는 Entity 간 관계가 SQL Table Relationship, Foreign Key, Owning Side, Fetch Strategy 기준에 맞게 설계되었는지 검수하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] SQL Table Relationship을 먼저 확인했는가?
- [ ] Primary Key / Foreign Key 위치를 확인했는가?
- [ ] Association이 실제 객체 탐색에 필요한가?
- [ ] 단방향으로 충분한가?
- [ ] 양방향이 필요한 이유가 명확한가?
- [ ] Foreign Key를 가진 쪽이 Owning Side인가?
- [ ] Owning Side에 @JoinColumn이 있는가?
- [ ] @JoinColumn name이 DB FK Column과 일치하는가?
- [ ] mappedBy 값이 상대 Entity Field 이름인가?
- [ ] mappedBy에 DB Column 이름을 쓰지 않았는가?
- [ ] ManyToOne에 FetchType.LAZY를 명시했는가?
- [ ] OneToOne에 FetchType.LAZY를 검토했는가?
- [ ] OneToMany Collection을 빈 컬렉션으로 초기화했는가?
- [ ] ManyToMany 직접 사용을 피했는가?
- [ ] N:M 관계를 Middle Entity로 풀었는가?
- [ ] 양방향 관계에 편의 Method가 필요한가?
- [ ] Collection Fetch Join + Pagination 위험을 검토했는가?
- [ ] Entity Association을 API Response로 직접 노출하지 않는가?
- [ ] Cascade / orphanRemoval 필요성을 별도 검토했는가?
- [ ] N+1 가능성을 Query 단계에서 검토할 계획이 있는가?
```

---

### [실무]

Review Flow:

```text
DB Table Relationship 확인
→ FK 위치 확인
→ Entity Association 필요성 확인
→ Direction 결정
→ Owning Side 확인
→ JoinColumn / mappedBy 확인
→ FetchType 확인
→ Collection 크기 확인
→ Pagination 필요성 확인
→ ManyToMany 여부 확인
→ DTO 노출 여부 확인
→ N+1 가능성 기록
```

Common Review Findings:

```text
문제: mappedBy = "post_id"
위험: Column 이름 사용으로 Mapping Error
해결: mappedBy = "post"

문제: @ManyToOne FetchType.LAZY 누락
위험: 기본 EAGER로 불필요한 조회 발생
해결: fetch = FetchType.LAZY 명시

문제: User.posts Collection을 API Response로 직접 반환
위험: Lazy Loading, 순환 참조, N+1
해결: Response DTO와 Repository Query 사용

문제: @ManyToMany 직접 사용
위험: 중간 Table 확장 어려움
해결: PostTag, Favorite, Like 같은 Middle Entity 사용

문제: OneToMany Collection Fetch Join + Pageable
위험: Pagination 불안정
해결: 별도 Query / DTO Projection / Batch Size 검토
```

---

### [FAQ]

Q. Association Mapping 검수에서 가장 먼저 확인할 것은 뭐야?
A. SQL Table Relationship과 Foreign Key 위치를 먼저 확인해야 한다.

Q. mappedBy 검수에서 가장 흔한 오류는 뭐야?
A. 상대 Entity Field 이름이 아니라 DB Column 이름을 쓰는 오류다.

Q. ManyToOne 검수에서 가장 중요한 것은 뭐야?
A. FetchType.LAZY, JoinColumn 이름, nullable 기준, N+1 가능성이다.

Q. ManyToMany가 보이면 어떻게 검토해?
A. 중간 Entity로 풀어낼 수 있는지 먼저 검토한다.

---

# 11. Common Mistakes

## 11.1 Association Mapping Common Mistakes

### [개념]

Association Mapping Common Mistakes는 JPA 연관관계 설계에서 자주 발생하는 방향, 주인, mappedBy, Fetch, Collection, ManyToMany 오류다.

---

### [핵심]

자주 발생하는 실수:

- DB Foreign Key 위치 확인 없이 Mapping
- 모든 연관관계를 양방향으로 설계
- 단방향으로 충분한데 양방향 사용
- `mappedBy`에 Column 이름 사용
- Owning Side와 Inverse Side 혼동
- `@JoinColumn` 생략으로 FK 이름 불명확
- `ManyToOne`에 FetchType.LAZY 누락
- `OneToOne` 기본 EAGER 방치
- `OneToMany` Collection을 API Response로 직접 반환
- 큰 Collection을 Entity에서 직접 탐색
- Collection Fetch Join과 Pagination 무분별 조합
- `ManyToMany` 직접 사용
- Middle Entity에 Unique Constraint 누락
- 양방향 편의 Method 없음
- 주인 쪽이 아닌 반대편만 변경
- Association을 JSON 직렬화에 직접 노출
- Cascade / orphanRemoval 남용
- N+1 가능성 검토 누락

---

### [실무]

Anti Pattern 예시:

```java
@Entity
public class Post {

    @OneToMany(mappedBy = "post_id")
    private List<Comment> comments;
}
```

문제:

```text
mappedBy에 DB Column 이름 사용
Collection 초기화 없음
상대 Entity Field 기준 아님
```

개선:

```java
@Entity
public class Post {

    @OneToMany(mappedBy = "post")
    private List<Comment> comments = new ArrayList<>();
}
```

Anti Pattern 예시:

```java
@ManyToOne
private User user;
```

문제:

```text
기본 FetchType.EAGER
JoinColumn 이름 불명확
nullable 기준 불명확
```

개선:

```java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "user_id", nullable = false)
private User user;
```

Anti Pattern 예시:

```java
@ManyToMany
private List<Festival> favoriteFestivals = new ArrayList<>();
```

개선:

```text
User
→ Favorite
→ Festival
```

Review 기준:

```text
Relationship
→ FK 위치 확인

Direction
→ 단방향 우선

Owning Side
→ FK 가진 쪽

Fetch
→ ManyToOne LAZY

Collection
→ Pagination 주의

N:M
→ Middle Entity
```

---

### [FAQ]

Q. Association Mapping에서 가장 흔한 실수는 뭐야?
A. Foreign Key 위치를 확인하지 않고 양방향 관계를 만들거나 mappedBy를 잘못 쓰는 것이다.

Q. `mappedBy = "user_id"`가 왜 틀려?
A. `mappedBy`는 DB Column 이름이 아니라 상대 Entity Field 이름을 사용해야 하기 때문이다.

Q. 모든 관계에 양방향을 걸면 안 돼?
A. 권장하지 않는다. 객체 상태 관리, 순환 참조, Lazy Loading, N+1 문제가 복잡해진다.

Q. `ManyToMany` 직접 사용은 왜 Anti Pattern이야?
A. 관계에 추가 Field를 넣기 어렵고 요구사항 변경에 취약하기 때문이다.

---

# 12. Part03 Final Goal

## 12.1 Agent Output Goal

### [개념]

JPA Advanced Part03의 최종 목적은 Agent가 SQL Table Relationship과 JPA Association Mapping을 연결하여 안정적인 Entity 관계를 설계하도록 만드는 것이다.

Part03은 Foreign Key, Owning Side, JoinColumn, mappedBy, ManyToOne, OneToMany, OneToOne, ManyToMany Caution, Middle Entity, Direction Decision을 담당한다.

---

### [핵심]

Agent가 수행해야 할 작업:

- SQL Table Relationship 확인
- Primary Key / Foreign Key 위치 확인
- Association 필요성 판단
- 단방향 / 양방향 결정
- Owning Side 판단
- `@JoinColumn` 설정
- `mappedBy` 설정
- `ManyToOne` LAZY 적용
- `OneToMany` Collection 주의
- `OneToOne` 필요성 검토
- `ManyToMany` 직접 사용 방지
- Middle Entity 설계
- 양방향 편의 Method 검토
- Collection Pagination 위험 검토
- N+1 가능성 기록
- Entity 직접 노출 Anti Pattern 탐지

---

### [실무]

Agent 작업 흐름:

```text
User Persistence Request
→ Identify Table Relationship
→ Check Primary Key / Foreign Key
→ Decide Entity Association
→ Choose Direction
→ Decide Owning Side
→ Apply JoinColumn
→ Apply mappedBy if Bidirectional
→ Apply LAZY Strategy
→ Avoid ManyToMany Direct Mapping
→ Check Collection Size
→ Check Pagination Risk
→ Review DTO Exposure
```

Part03 이후 연결:

```text
Part03 Association Mapping / Table Relationship
→ Part04 Persistence Context / Dirty Checking
→ Part05 Repository / JPQL / Native Query
→ Part06 Fetch Strategy / Fetch Join / N+1
→ Part07 Transaction / Cascade / Pagination
→ Part08 Troubleshooting / Anti Pattern
```

---

### [FAQ]

Q. JPA Advanced Part03의 목적은 뭐야?
A. Agent가 SQL Table Relationship과 JPA Association Mapping을 연결해 Foreign Key, Owning Side, Direction, JoinColumn, mappedBy를 올바르게 설계하도록 만드는 것이다.

Q. Part03에서 가장 중요한 기준은 뭐야?
A. Foreign Key 위치, Owning Side, 단방향 우선, ManyToOne LAZY, ManyToMany 직접 사용 지양이다.

Q. Part03에서 Fetch Join을 깊게 다뤄?
A. 아니다. FetchType 기본 주의만 다루고 Fetch Join과 N+1은 Part06에서 상세히 다룬다.

Q. Part03 다음에는 무엇을 다뤄?
A. Part04에서 Persistence Context, Entity Lifecycle, Dirty Checking, Flush, Detached Entity를 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. Association Mapping은 뭐야?
A. Entity 간 관계를 Java 객체 참조와 DB Foreign Key로 연결하는 JPA Mapping이다.

Q. Table Relationship과 Association Mapping은 같은 거야?
A. 아니다. Table Relationship은 DB PK / FK 관계이고 Association Mapping은 이를 Entity 객체 참조로 표현한 것이다.

Q. JPA 연관관계는 SQL JOIN과 같은 거야?
A. 아니다. 연관관계는 Mapping이고 JOIN은 Query 실행 방식이다.

Q. JPA Association Mapping에서 가장 먼저 확인할 것은 뭐야?
A. DB Foreign Key가 어느 Table에 있는지 먼저 확인해야 한다.

Q. Foreign Key는 뭐야?
A. 다른 Table의 Primary Key를 참조해 Table Relationship을 만드는 Column이다.

Q. JPA에서 Foreign Key는 어떻게 표현해?
A. 보통 `@ManyToOne`과 `@JoinColumn`으로 객체 참조와 FK Column을 연결한다.

Q. Entity Association은 반드시 만들어야 해?
A. 아니다. 객체 탐색이 필요하면 만들고, 단순 ID 참조만 필요하면 FK ID만 관리하는 설계도 가능하다.

Q. 단방향 연관관계는 뭐야?
A. 한 Entity에서 다른 Entity로만 객체 탐색이 가능한 연관관계다.

Q. 양방향 연관관계는 뭐야?
A. 두 Entity가 서로를 객체 참조로 탐색할 수 있는 연관관계다.

Q. JPA 연관관계는 단방향으로 시작하는 게 좋아?
A. 그렇다. 단방향으로 충분하면 구조가 단순하고 유지보수하기 좋다.

Q. 양방향 관계는 언제 써?
A. 양쪽 Entity에서 객체 탐색이 실제로 필요할 때 사용한다.

Q. DTO 응답에 자식 목록이 필요하면 양방향을 만들어야 해?
A. 아니다. Repository Query나 DTO Projection으로 조회할 수 있다.

Q. Parent에서 Child 목록이 필요하면 무조건 `@OneToMany`를 만들어야 해?
A. 아니다. 목록 크기와 Pagination 요구사항을 확인하고 별도 Repository Query도 검토해야 한다.

Q. 연관관계 주인은 어떻게 정해?
A. DB Foreign Key를 가진 Entity가 연관관계 주인이다.

Q. Owning Side는 뭐야?
A. JPA 연관관계에서 Foreign Key 값을 실제로 관리하는 쪽이다.

Q. Inverse Side는 뭐야?
A. 양방향 관계에서 연관관계 주인이 아닌 반대편이다.

Q. `mappedBy`가 있는 쪽이 주인이야?
A. 아니다. `mappedBy`가 있는 쪽은 주인이 아니며 FK를 직접 관리하지 않는다.

Q. `mappedBy`에는 무엇을 써야 해?
A. 상대 Entity의 Association Field 이름을 써야 한다.

Q. `mappedBy = "post_id"`처럼 Column 이름을 쓰면 돼?
A. 아니다. Column 이름이 아니라 상대 Entity Field 이름을 써야 한다.

Q. `@JoinColumn`은 뭐야?
A. Association Mapping에서 Foreign Key Column을 지정하는 Annotation이다.

Q. `@JoinColumn(name = "user_id")`의 name은 어느 Table Column이야?
A. 현재 Entity가 Mapping되는 Table의 Foreign Key Column 이름이다.

Q. Entity Association Field에 `@Column`을 써도 돼?
A. 아니다. Entity Association에는 `@JoinColumn`을 사용한다.

Q. `@JoinColumn(nullable = false)`는 무슨 뜻이야?
A. Foreign Key Column이 NULL을 허용하지 않는 필수 관계임을 의미한다.

Q. `ManyToOne`은 언제 써?
A. 여러 Entity가 하나의 Entity를 참조하는 관계에서 사용한다.

Q. `ManyToOne`에서 Foreign Key는 어느 쪽에 있어?
A. Many 쪽 Table에 Foreign Key가 있다.

Q. `ManyToOne`은 왜 LAZY를 명시해?
A. 기본 Fetch가 EAGER라 불필요한 Join과 조회가 발생할 수 있으므로 LAZY를 명시하는 것이 좋다.

Q. `ManyToOne`이 있으면 N+1이 생길 수 있어?
A. 그렇다. 목록 조회 후 연관 Entity getter를 반복 호출하면 N+1 문제가 발생할 수 있다.

Q. `ManyToOne` 검수에서 중요한 것은 뭐야?
A. FetchType.LAZY, JoinColumn 이름, nullable 기준, N+1 가능성이다.

Q. `OneToMany`는 언제 써?
A. Parent Entity에서 Child Collection을 객체 탐색해야 할 때 사용한다.

Q. `OneToMany`에는 왜 `mappedBy`를 써?
A. 상대 Entity가 Foreign Key를 가진 Owning Side임을 표시하기 위해 사용한다.

Q. `OneToMany` Collection은 꼭 초기화해야 해?
A. 빈 컬렉션으로 초기화하는 것이 NullPointerException을 줄이고 사용이 편하다.

Q. 자식 목록 API는 Entity Collection으로 반환해도 돼?
A. 권장하지 않는다. DTO로 변환하고 큰 목록은 별도 Query와 Pagination을 고려해야 한다.

Q. `OneToMany` Collection Fetch Join에 Pagination을 같이 써도 돼?
A. 주의해야 한다. DB Pagination이 기대대로 동작하지 않거나 메모리에서 처리될 수 있다.

Q. 자식 목록 Pagination은 어떻게 하는 게 좋아?
A. Child Repository에서 Parent ID 조건으로 `Page`나 `Slice` 조회하는 방식이 안정적이다.

Q. `OneToOne`은 언제 써?
A. 두 데이터가 독립 Table로 분리되어야 하고 1:1 관계가 명확할 때 사용한다.

Q. `OneToOne`도 LAZY를 써야 해?
A. 불필요한 즉시 로딩을 막기 위해 LAZY를 고려하지만 SQL 확인이 필요하다.

Q. Embedded와 OneToOne은 어떻게 구분해?
A. 독립 식별자가 필요한 Persistence Model이면 OneToOne, 식별자 없는 값 묶음이면 Embedded를 검토한다.

Q. `ManyToMany`를 바로 쓰면 안 돼?
A. 가능은 하지만 실무에서는 중간 Table에 생성일, 상태 같은 추가 Field가 필요한 경우가 많아 중간 Entity로 풀어내는 것이 좋다.

Q. 좋아요, 찜 같은 관계는 ManyToMany야?
A. 개념적으로는 다대다지만 Like, Favorite 같은 중간 Entity로 표현하는 것이 실무에 적합하다.

Q. Middle Entity는 뭐야?
A. N:M 관계의 중간 Table을 명시적인 Entity로 표현한 것이다.

Q. Favorite이나 Like는 Middle Entity야?
A. 그렇다. User와 대상 Entity 사이의 관계 자체를 표현하는 Middle Entity로 볼 수 있다.

Q. Middle Entity 중복은 어떻게 막아?
A. Service existsBy 검증과 DB 복합 Unique Constraint를 함께 사용한다.

Q. 양방향 관계에서 편의 Method는 왜 필요해?
A. 양쪽 객체 참조를 함께 맞춰 객체 상태 불일치를 막기 위해 필요하다.

Q. 주인 쪽만 세팅하면 DB에는 반영돼?
A. DB 반영은 주인 쪽 기준이지만 객체 상태 일관성을 위해 반대편도 함께 맞추는 것이 좋다.

Q. 연관관계 해제와 Entity 삭제는 같은 거야?
A. 아니다. 관계 해제는 FK를 null로 만들거나 연결을 끊는 것이고 삭제는 Row를 제거하는 것이다.

Q. nullable false 관계를 null로 바꿔도 돼?
A. 안 된다. DB NOT NULL Constraint 위반이 발생할 수 있다.

Q. Collection에서 자식을 remove하면 DB에서도 삭제돼?
A. orphanRemoval 설정이 있으면 삭제될 수 있고, 없으면 관계 변경만 일어날 수 있다.

Q. Association Mapping할 때 FetchType도 같이 정해야 해?
A. 그렇다. 특히 `ManyToOne`과 `OneToOne`은 기본 EAGER라 LAZY 명시를 검토해야 한다.

Q. LAZY로 하면 N+1 문제가 없어져?
A. 아니다. LAZY는 조회 시점을 늦출 뿐이고 반복 접근하면 N+1이 발생할 수 있다.

Q. EAGER로 바꾸면 LazyInitializationException이 해결돼?
A. 일부 상황은 피할 수 있지만 불필요한 조회와 성능 문제가 생기므로 권장하지 않는다.

Q. Association Mapping 검수에서 가장 먼저 확인할 것은 뭐야?
A. SQL Table Relationship과 Foreign Key 위치를 먼저 확인해야 한다.

Q. mappedBy 검수에서 가장 흔한 오류는 뭐야?
A. 상대 Entity Field 이름이 아니라 DB Column 이름을 쓰는 오류다.

Q. ManyToMany가 보이면 어떻게 검토해?
A. 중간 Entity로 풀어낼 수 있는지 먼저 검토한다.

Q. JPA Part03에서 가장 중요한 기준은 뭐야?
A. Foreign Key 위치, Owning Side, 단방향 우선, ManyToOne LAZY, ManyToMany 직접 사용 지양이다.

Q. JPA Part03 다음에는 무엇을 다뤄?
A. Part04에서 Persistence Context, Entity Lifecycle, Dirty Checking, Flush, Detached Entity를 다룬다.
