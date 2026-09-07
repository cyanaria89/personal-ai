# QueryDSL Practical Part03 Paging Projection

---

# 1. Pagination Overview

## 1.1 Pagination 개념

### [개념]

Pagination은 대량 데이터를 페이지 단위로 나누어 조회하는 방식이다.

QueryDSL에서는 `offset`, `limit`, `Pageable`을 사용하여 Pagination Query를 작성한다.

Pagination은 검색 API, 관리자 목록, 무한 스크롤, 피드 API, 채팅 목록, 알림 목록에서 필수다.

---

### [핵심]

- Pagination = 페이지 단위 조회
- 대량 데이터 조회 최적화
- QueryDSL + Pageable 조합
- 정렬 기준 필수
- Count Query 비용 고려 필요

주요 방식:

- Page
- Slice
- Cursor Paging

---

### [실무]

2026 실무 기준 Pagination 선택 기준:

```text
Admin Search Page
→ Page

Infinite Scroll
→ Slice

Large Feed / High Traffic
→ Cursor Paging
```

Page는 전체 개수와 전체 페이지 수가 필요할 때 사용한다.

Slice는 다음 페이지 존재 여부만 필요할 때 사용한다.

Cursor Paging은 대량 트래픽과 Deep Paging 성능이 중요할 때 사용한다.

---

### [Flow]

```text
Client Request
→ Pageable
→ Sort Condition
→ QueryDSL offset / limit
→ Content Query
→ Count Query Optional
→ Response Mapping
```

---

### [FAQ]

Q. Pagination이 필요한 이유는?
A. 대량 데이터를 한 번에 조회하지 않고 서버 메모리와 DB 부하를 줄이기 위해서다.

Q. QueryDSL Pagination 핵심은?
A. `offset`, `limit`, `Pageable`, 안정적인 `orderBy` 기준이다.

Q. Page, Slice, Cursor Paging 중 무엇을 선택하는가?
A. 관리자 검색은 Page, 무한 스크롤은 Slice, 대규모 피드는 Cursor Paging이 적합하다.

---

# 2. Offset Pagination

## 2.1 offset / limit

### [개념]

Offset Pagination은 `offset`과 `limit`를 사용하여 특정 구간 데이터를 조회하는 방식이다.

`offset`은 건너뛸 데이터 수이고, `limit`는 조회할 데이터 수이다.

---

### [핵심]

- offset = 조회 시작 위치
- limit = 조회 개수
- Pageable과 호환 쉬움
- SQL LIMIT / OFFSET 변환
- 구현 간단
- Deep Paging 성능 저하 가능

---

### [예제]

```java
public List<User> findUsers(Pageable pageable) {
    return queryFactory
        .selectFrom(user)
        .offset(pageable.getOffset())
        .limit(pageable.getPageSize())
        .orderBy(user.createdAt.desc(), user.id.desc())
        .fetch();
}
```

---

### [실무]

Offset Pagination은 관리자 목록, 일반 검색 페이지에 적합하다.

단, 페이지가 깊어질수록 DB가 많은 Row를 스캔하고 버려야 하므로 성능이 저하될 수 있다.

---

### [주의]

- Deep Paging 비효율
- 안정적인 정렬 기준 필수
- `createdAt` 단독 정렬은 중복 가능
- `createdAt + id` 복합 정렬 권장
- 대규모 피드는 Cursor Paging 검토

---

### [FAQ]

Q. offset이란?
A. 조회 시작 전 건너뛸 데이터 수이다.

Q. limit란?
A. 한 번에 조회할 데이터 수이다.

Q. Offset Pagination 단점은?
A. 페이지가 깊어질수록 성능이 떨어진다.

---

# 3. Page

## 3.1 Page 개념

### [개념]

Page는 Content와 Total Count를 함께 제공하는 Pagination 응답 방식이다.

전체 데이터 수와 전체 페이지 수가 필요한 화면에서 사용한다.

---

### [핵심]

- content 제공
- totalCount 제공
- totalPages 계산 가능
- Count Query 필요
- 관리자 페이지 적합
- 검색 결과 페이지 적합

---

### [예제]

Content Query:

```java
List<User> content = queryFactory
    .selectFrom(user)
    .offset(pageable.getOffset())
    .limit(pageable.getPageSize())
    .orderBy(user.createdAt.desc(), user.id.desc())
    .fetch();
```

Count Query:

```java
Long total = queryFactory
    .select(user.count())
    .from(user)
    .fetchOne();
```

Page 생성:

```java
return new PageImpl<>(content, pageable, total);
```

---

### [실무]

Page는 전체 개수 정보가 필요한 화면에만 사용한다.

무한 스크롤 API에 Page를 사용하는 것은 불필요한 Count Query 때문에 비효율적일 수 있다.

---

### [주의]

- Count Query 비용 큼
- Join이 많은 Count Query는 느릴 수 있음
- 대량 데이터에서는 Slice 또는 Cursor Paging 검토
- Count Query는 Content Query와 분리 권장

---

### [FAQ]

Q. Page 장점은?
A. 전체 데이터 수와 전체 페이지 수를 제공한다.

Q. Page 단점은?
A. Count Query 비용이 크다.

Q. Page는 언제 사용하는가?
A. 관리자 검색 화면처럼 전체 페이지 수가 필요한 경우 사용한다.

---

# 4. PageableExecutionUtils

## 4.1 Count Query 최적화

### [개념]

`PageableExecutionUtils`는 Page 생성 시 불필요한 Count Query 실행을 줄이는 Spring Data 유틸이다.

Content 결과만으로 마지막 페이지 여부를 판단할 수 있으면 Count Query를 생략할 수 있다.

---

### [핵심]

- Count Query Lazy Execute
- 불필요한 Count Query 생략
- Page 성능 최적화
- Spring Data JPA Pagination 최적화

---

### [예제]

Count Query:

```java
JPAQuery<Long> countQuery = queryFactory
    .select(user.count())
    .from(user)
    .where(statusEq(status));
```

PageableExecutionUtils:

```java
return PageableExecutionUtils.getPage(
    content,
    pageable,
    countQuery::fetchOne
);
```

---

### [실무]

Page를 반드시 사용해야 한다면 `PageableExecutionUtils.getPage()`를 우선 고려한다.

단, Count Query 자체가 복잡하면 Count Query에서 불필요한 Join을 제거해야 한다.

---

### [주의]

- PageableExecutionUtils가 모든 Count Query 비용을 제거하는 것은 아니다.
- Count Query가 필요한 상황이면 결국 실행된다.
- Count Query는 Content Query보다 단순하게 작성한다.

---

### [FAQ]

Q. PageableExecutionUtils는 왜 사용하는가?
A. 불필요한 Count Query 실행을 줄이기 위해 사용한다.

Q. Count Query는 완전히 사라지는가?
A. 아니다. 필요한 경우에는 실행된다.

Q. Count Query 최적화 핵심은?
A. Count Query에서 불필요한 Join을 제거하는 것이다.

---

# 5. Slice

## 5.1 Slice 개념

### [개념]

Slice는 전체 개수 없이 다음 페이지 존재 여부만 제공하는 Pagination 방식이다.

Count Query가 필요 없다.

---

### [핵심]

- totalCount 없음
- totalPages 없음
- hasNext 제공
- Count Query 불필요
- 무한 스크롤 적합
- 채팅 / 알림 목록 적합

---

### [예제]

Content Query:

```java
List<User> content = queryFactory
    .selectFrom(user)
    .offset(pageable.getOffset())
    .limit(pageable.getPageSize() + 1)
    .orderBy(user.createdAt.desc(), user.id.desc())
    .fetch();
```

hasNext 처리:

```java
boolean hasNext = false;

if (content.size() > pageable.getPageSize()) {
    hasNext = true;
    content.remove(pageable.getPageSize());
}

return new SliceImpl<>(content, pageable, hasNext);
```

---

### [실무]

Slice는 무한 스크롤 API에 적합하다.

예:

- 채팅 메시지 목록
- 알림 목록
- 댓글 목록
- 실시간 피드 일부
- 모바일 목록 API

---

### [주의]

- 전체 개수 제공 불가
- 전체 페이지 수 제공 불가
- `pageSize + 1` 조회 후 hasNext 판단
- 정렬 기준 안정성 필요

---

### [FAQ]

Q. Slice 장점은?
A. Count Query 없이 다음 페이지 존재 여부만 빠르게 판단할 수 있다.

Q. Slice는 언제 사용하는가?
A. 무한 스크롤, 채팅, 알림 목록처럼 전체 개수가 필요 없는 API에서 사용한다.

Q. Slice에서 hasNext는 어떻게 판단하는가?
A. `pageSize + 1`개를 조회한 뒤 초과 데이터가 있으면 hasNext를 true로 판단한다.

---

# 6. Cursor Paging

## 6.1 Cursor Paging 개념

### [개념]

Cursor Paging은 마지막 조회 데이터의 기준값을 Cursor로 사용하여 다음 데이터를 조회하는 방식이다.

Offset을 사용하지 않기 때문에 Deep Paging에서 성능이 좋다.

---

### [핵심]

- Offset 미사용
- Cursor 기반 조회
- LastId 기반 가능
- createdAt + id 기반 가능
- Deep Paging 성능 우수
- 대규모 트래픽 적합

---

### [예제]

id 기반 Cursor:

```java
queryFactory
    .selectFrom(user)
    .where(user.id.lt(lastId))
    .orderBy(user.id.desc())
    .limit(size)
    .fetch();
```

createdAt + id 기반 Cursor:

```java
queryFactory
    .selectFrom(user)
    .where(
        user.createdAt.lt(lastCreatedAt)
            .or(
                user.createdAt.eq(lastCreatedAt)
                    .and(user.id.lt(lastId))
            )
    )
    .orderBy(user.createdAt.desc(), user.id.desc())
    .limit(size)
    .fetch();
```

---

### [실무]

Cursor Paging은 대규모 피드, 실시간 목록, 트래픽이 많은 API에서 사용한다.

추천 정렬 기준:

```text
createdAt DESC
id DESC
```

`createdAt`만 사용하면 같은 시간에 생성된 데이터의 순서가 흔들릴 수 있다.

`id`를 보조 정렬로 함께 사용하면 안정적인 Cursor Paging이 가능하다.

---

### [주의]

- 구현 복잡도 높음
- 정렬 기준 변경 어려움
- Cursor 값 설계 필요
- createdAt 중복 고려 필요
- id 보조 정렬 권장

---

### [FAQ]

Q. Cursor Paging 장점은?
A. Deep Paging에서도 성능 저하가 적다.

Q. Cursor Paging 정렬 기준은?
A. `createdAt DESC, id DESC`처럼 안정적인 복합 정렬이 권장된다.

Q. createdAt만 Cursor로 쓰면 안 되는가?
A. 같은 createdAt 데이터가 있으면 누락 또는 중복 가능성이 있어 id 보조 조건이 필요하다.

---

# 7. Projection Overview

## 7.1 Projection 개념

### [개념]

Projection은 Query 결과를 Entity가 아닌 DTO 형태로 직접 조회하는 방식이다.

필요한 컬럼만 조회할 수 있어 목록 API와 검색 API 성능 최적화에 유리하다.

---

### [핵심]

- Entity 직접 반환 지양
- DTO 직접 조회
- 필요한 컬럼만 조회
- API 응답 구조 분리
- 목록 API 성능 최적화
- 검색 API 성능 최적화

---

### [실무]

목록 API, 검색 API, 관리자 조회 API는 Projection 사용을 우선 고려한다.

Entity 전체 조회는 불필요한 컬럼, Lazy Loading, N+1, 직렬화 문제를 유발할 수 있다.

---

### [FAQ]

Q. Projection이란?
A. Query 결과를 Entity가 아닌 DTO로 직접 조회하는 방식이다.

Q. Projection을 왜 사용하는가?
A. 필요한 컬럼만 조회하고 API 응답 구조를 Entity와 분리하기 위해서다.

Q. 목록 API에서 Projection이 중요한 이유는?
A. 대량 목록 조회에서 불필요한 Entity 로딩을 줄일 수 있기 때문이다.

---

# 8. Tuple Projection

## 8.1 Tuple

### [개념]

Tuple은 여러 컬럼을 임시로 조회할 때 사용하는 QueryDSL 결과 타입이다.

---

### [핵심]

- 임시 조회
- 테스트 조회
- DTO 없이 다중 컬럼 조회
- 실무 응답에는 비권장

---

### [예제]

```java
List<Tuple> result = queryFactory
    .select(user.id, user.username)
    .from(user)
    .fetch();

Long id = result.get(0).get(user.id);
String username = result.get(0).get(user.username);
```

---

### [실무]

Tuple은 테스트, 내부 확인, 임시 집계 조회에는 사용할 수 있다.

API 응답 구조에는 DTO Projection이 더 적합하다.

---

### [주의]

- 응답 DTO로 직접 사용 비권장
- 가독성 낮음
- 필드 접근이 불편함
- 유지보수성 낮음

---

### [FAQ]

Q. Tuple은 언제 사용하는가?
A. 간단한 테스트나 임시 다중 컬럼 조회에서 사용한다.

Q. Tuple을 API 응답에 사용해도 되는가?
A. 권장하지 않는다. DTO Projection을 사용하는 것이 좋다.

---

# 9. DTO Projection

## 9.1 Constructor Projection

### [개념]

Constructor Projection은 DTO 생성자를 사용하여 Query 결과를 DTO로 매핑하는 방식이다.

---

### [핵심]

- Projections.constructor 사용
- 구현 간단
- DTO 생성자 필요
- 컴파일 시 검증 약함
- 런타임 오류 가능

---

### [예제]

```java
List<UserDto> result = queryFactory
    .select(Projections.constructor(
        UserDto.class,
        user.id,
        user.username
    ))
    .from(user)
    .fetch();
```

---

### [실무]

간단한 DTO 조회에서 많이 사용한다.

단, 생성자 파라미터 순서와 타입이 맞지 않으면 런타임 오류가 발생할 수 있다.

---

### [주의]

- 생성자 파라미터 순서 중요
- 생성자 타입 일치 필요
- 컴파일 시 오류 검출 어려움
- 런타임 오류 가능

---

### [FAQ]

Q. Constructor Projection 장점은?
A. 구현이 간단하고 DTO 생성자를 사용할 수 있다.

Q. Constructor Projection 단점은?
A. 생성자 파라미터 순서나 타입이 틀리면 런타임 오류가 발생할 수 있다.

---

## 9.2 Field Projection

### [개념]

Field Projection은 DTO 필드에 직접 값을 주입하는 Projection 방식이다.

---

### [핵심]

- Projections.fields 사용
- 필드명 매칭 필요
- Setter 불필요
- 기본 생성자 필요 가능
- 필드명 불일치 주의

---

### [예제]

```java
List<UserDto> result = queryFactory
    .select(Projections.fields(
        UserDto.class,
        user.id,
        user.username
    ))
    .from(user)
    .fetch();
```

alias 필요 예:

```java
.select(Projections.fields(
    UserDto.class,
    user.username.as("name")
))
```

---

### [실무]

필드명과 DTO 속성명이 다르면 `as()`로 alias를 맞춘다.

---

### [주의]

- 필드명 불일치 주의
- alias 필요할 수 있음
- DTO 구조 변경 시 오류 가능

---

### [FAQ]

Q. Field Projection 핵심은?
A. Query 결과 필드명과 DTO 필드명을 맞추는 것이다.

Q. 필드명이 다르면 어떻게 하는가?
A. `as()`로 alias를 지정한다.

---

## 9.3 Bean Projection

### [개념]

Bean Projection은 Setter를 통해 DTO 값을 주입하는 방식이다.

---

### [핵심]

- Projections.bean 사용
- Setter 필요
- JavaBean 규칙 기반
- 필드명 매칭 필요

---

### [예제]

```java
List<UserDto> result = queryFactory
    .select(Projections.bean(
        UserDto.class,
        user.id,
        user.username
    ))
    .from(user)
    .fetch();
```

---

### [주의]

- Setter 필요
- 필드명 매칭 필요
- 불변 DTO에는 부적합

---

### [FAQ]

Q. Bean Projection은 언제 사용하는가?
A. Setter 기반 DTO에 사용할 수 있다.

Q. 불변 DTO에 적합한가?
A. 아니다. Setter가 필요하므로 불변 DTO에는 적합하지 않다.

---

## 9.4 QueryProjection

### [개념]

QueryProjection은 `@QueryProjection`을 사용하여 Type-safe DTO Projection을 제공하는 방식이다.

DTO 생성자에 `@QueryProjection`을 붙이면 QDto가 생성된다.

---

### [핵심]

- Type-safe Projection
- Compile-time Validation
- QDto 생성
- 가장 안전한 Projection 방식
- DTO가 QueryDSL 의존성 가짐

---

### [예제]

DTO:

```java
public class UserDto {

    private final Long id;
    private final String username;

    @QueryProjection
    public UserDto(Long id, String username) {
        this.id = id;
        this.username = username;
    }
}
```

Query:

```java
List<UserDto> result = queryFactory
    .select(new QUserDto(
        user.id,
        user.username
    ))
    .from(user)
    .fetch();
```

---

### [실무]

QueryProjection은 가장 안전하지만 DTO가 QueryDSL에 의존한다.

도메인 내부 Query DTO에는 적합하고, 외부 API Response DTO에는 프로젝트 정책에 따라 선택한다.

---

### [주의]

- DTO에 QueryDSL 의존성 생김
- QDto 생성 필요
- DTO가 Query 계층에 묶일 수 있음
- 계층 분리 정책에 따라 사용 결정

---

### [FAQ]

Q. QueryProjection 장점은?
A. 컴파일 시점에 DTO Projection 오류를 검출할 수 있다.

Q. QueryProjection 단점은?
A. DTO가 QueryDSL 의존성을 가진다.

Q. QueryProjection은 언제 사용하는가?
A. Type-safe Projection이 중요하고 DTO 의존성을 허용할 수 있을 때 사용한다.

---

# 10. Projection Selection Guide

## 10.1 Projection 선택 기준

### [개념]

Projection 방식은 DTO 안정성, 개발 속도, 계층 분리 정책을 기준으로 선택한다.

---

### [핵심]

추천 기준:

```text
Simple DTO
→ Constructor Projection

Strict Type Safety
→ QueryProjection

Temporary Query
→ Tuple

Setter DTO
→ Bean Projection

Field Alias Needed
→ Field Projection
```

---

### [Comparison]

| Projection Type | Type-safe | 실무 사용성 | 장점              | 단점             |
| --------------- | --------- | ----------: | ----------------- | ---------------- |
| Tuple           | 낮음      |        낮음 | 빠른 임시 조회    | 유지보수 낮음    |
| Constructor     | 중간      |        높음 | 간단함            | 런타임 오류 가능 |
| Field           | 중간      |        중간 | alias 대응 가능   | 필드명 의존      |
| Bean            | 중간      |        낮음 | JavaBean DTO 대응 | Setter 필요      |
| QueryProjection | 높음      |        높음 | 컴파일 검증       | QueryDSL 의존    |

---

### [실무]

실무 추천:

- 일반 목록 DTO: Constructor Projection
- 엄격한 타입 안정성: QueryProjection
- 임시 확인: Tuple
- Setter DTO: Bean Projection
- 필드명 변환 필요: Field Projection + alias

---

### [FAQ]

Q. 실무에서 가장 많이 쓰는 Projection은?
A. Constructor Projection 또는 QueryProjection이다.

Q. 가장 안전한 Projection은?
A. QueryProjection이다.

Q. 가장 간단한 Projection은?
A. Constructor Projection이다.

---

# 11. Paging + Projection Pattern

## 11.1 목록 API 조회 패턴

### [개념]

실무 목록 API는 Pagination과 Projection을 함께 사용한다.

Entity 전체 조회보다 DTO Projection + Pagination 조합이 성능과 응답 구조 관리에 유리하다.

---

### [핵심]

- Pagination + DTO Projection
- 목록 API 최적화
- 필요한 컬럼만 조회
- API 응답 구조 명확화
- Count Query 분리

---

### [예제]

```java
List<UserListDto> content = queryFactory
    .select(Projections.constructor(
        UserListDto.class,
        user.id,
        user.username,
        user.createdAt
    ))
    .from(user)
    .where(statusEq(status))
    .offset(pageable.getOffset())
    .limit(pageable.getPageSize())
    .orderBy(user.createdAt.desc(), user.id.desc())
    .fetch();

JPAQuery<Long> countQuery = queryFactory
    .select(user.count())
    .from(user)
    .where(statusEq(status));

return PageableExecutionUtils.getPage(
    content,
    pageable,
    countQuery::fetchOne
);
```

---

### [실무]

목록 API에서는 다음 조합을 우선 고려한다.

```text
Search API
→ Dynamic Query
→ DTO Projection
→ Pagination
→ Count Query Optimization
```

---

### [FAQ]

Q. 목록 API 추천 구조는?
A. Dynamic Query, DTO Projection, Pagination, Count Query 분리 조합이다.

Q. Entity 조회 후 DTO 변환보다 Projection이 좋은 이유는?
A. 필요한 컬럼만 조회할 수 있어 목록 조회 성능에 유리하기 때문이다.

---

# 12. Common Mistakes

## 12.1 Paging / Projection 실수

### [핵심]

- Count Query 남발
- Deep Paging 방치
- Entity 직접 반환
- Slice 대신 Page 남발
- Tuple 남용
- Constructor Projection 파라미터 순서 오류
- QueryProjection QDto 생성 누락
- 불안정한 정렬 기준

---

### [Troubleshooting]

문제: Pagination Query가 느림

원인:

- Count Query 비용 큼
- Deep Paging
- Join 많은 Query

해결:

- Slice 사용
- Cursor Paging 검토
- Count Query 분리
- PageableExecutionUtils 사용

---

문제: Projection 런타임 오류 발생

원인:

- Constructor Projection 파라미터 순서 또는 타입 불일치

해결:

- DTO 생성자 확인
- QueryProjection 검토

---

문제: Cursor Paging에서 데이터 누락 발생

원인:

- 정렬 기준 불안정
- createdAt 단독 Cursor 사용

해결:

- createdAt + id 복합 Cursor 사용

---

문제: Slice hasNext가 잘못됨

원인:

- pageSize + 1 조회 누락
- 초과 데이터 제거 누락

해결:

- limit(pageSize + 1)
- content.remove(pageSize)

---

### [FAQ]

Q. Pagination에서 가장 흔한 실수는?
A. 불필요한 Page 사용과 Count Query 남발이다.

Q. Projection에서 가장 흔한 실수는?
A. DTO 생성자 파라미터 순서 오류와 Entity 직접 반환이다.

Q. Cursor Paging에서 흔한 실수는?
A. createdAt 단독 정렬처럼 불안정한 Cursor 기준을 사용하는 것이다.

---

# 13. Related Documents

- QueryDSL_Practical_Part01_Basic.md
- QueryDSL_Practical_Part02_Dynamic_Query.md
- QueryDSL_Practical_Part04_Practical.md

---

# Retrieval Queries

### [FAQ]

Q. QueryDSL Pagination 핵심은?
A. offset, limit, Pageable, 안정적인 orderBy 기준이다.

Q. Page와 Slice 차이는?
A. Page는 total count를 포함하고, Slice는 hasNext만 제공한다.

Q. PageableExecutionUtils란?
A. Page 생성 시 불필요한 Count Query 실행을 줄이는 Spring Data 유틸이다.

Q. Count Query 최적화 핵심은?
A. Count Query에서 불필요한 Join을 제거하고 PageableExecutionUtils를 사용하는 것이다.

Q. Infinite Scroll 추천 방식은?
A. Slice가 적합하다.

Q. Slice hasNext는 어떻게 판단하는가?
A. pageSize + 1개를 조회한 뒤 초과 데이터가 있으면 hasNext를 true로 판단한다.

Q. Cursor Paging 장점은?
A. Deep Paging에서도 성능 저하가 적다.

Q. Cursor Paging 정렬 기준은?
A. createdAt DESC, id DESC 복합 정렬이 권장된다.

Q. Projection이란?
A. Query 결과를 Entity가 아닌 DTO 형태로 직접 조회하는 방식이다.

Q. Projection 종류는?
A. Tuple, Constructor Projection, Field Projection, Bean Projection, QueryProjection이다.

Q. Constructor Projection 단점은?
A. 생성자 파라미터 순서나 타입이 틀리면 런타임 오류가 발생할 수 있다.

Q. QueryProjection 장점은?
A. 컴파일 시점에 Projection 오류를 검출할 수 있다.

Q. QueryProjection 단점은?
A. DTO가 QueryDSL 의존성을 가진다.

Q. 실무 추천 Projection은?
A. Constructor Projection 또는 QueryProjection이다.

Q. 목록 API 추천 QueryDSL 패턴은?
A. Dynamic Query, DTO Projection, Pagination, Count Query 최적화 조합이다.

Q. Entity 조회 후 DTO 변환보다 Projection이 좋은 이유는?
A. 필요한 컬럼만 조회할 수 있어 목록 조회 성능에 유리하기 때문이다.
