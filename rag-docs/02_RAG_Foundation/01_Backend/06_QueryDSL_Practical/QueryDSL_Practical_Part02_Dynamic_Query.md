# QueryDSL Practical Part02 Dynamic Query

---

# 1. Dynamic Query Overview

## 1.1 Dynamic Query 개념

### [개념]

Dynamic Query는 입력 조건 존재 여부에 따라 Query 조건이 동적으로 변경되는 Query 작성 방식이다.

검색 API, 필터 API, 관리자 검색, 통계 조건 조회에서 핵심이다.

QueryDSL의 가장 강력한 기능 중 하나이다.

---

### [핵심]

- Dynamic Query = 동적 조건 Query
- Optional Filter 핵심
- 검색 API 핵심
- QueryDSL 실무 핵심

대표 구현 방식:

- BooleanBuilder
- BooleanExpression

---

### [실무]

2026 실무 기준 Dynamic Query 구현 방식 선택 기준:

```text
Simple Dynamic Query
→ BooleanExpression

Complex OR Query
→ BooleanBuilder
```

실무 우선순위:

```text
BooleanExpression First
→ Complex OR
→ BooleanBuilder
```

---

### [Flow]

```text
Request Parameter
→ Optional Filter Check
→ Dynamic Condition Build
→ QueryDSL where()
→ SQL
→ Result
```

---

### [FAQ]

Q. Dynamic Query란?
A. 조건값 존재 여부에 따라 Query 조건이 동적으로 변경되는 Query 작성 방식이다.

Q. QueryDSL에서 왜 중요한가?
A. 대부분 검색 API가 Dynamic Query 기반이기 때문이다.

---

# 2. BooleanBuilder

## 2.1 BooleanBuilder 개념

### [개념]

BooleanBuilder는 조건을 누적하며 Query를 작성하는 방식이다.

if문 기반으로 조건을 추가한다.

---

### [핵심]

- 조건 누적 방식
- 직관적
- OR 조건 강함
- 복잡한 Query 적합

---

### [예제]

```java
public List<User> search(String username, Integer age) {
    BooleanBuilder builder = new BooleanBuilder();

    if (username != null) {
        builder.and(user.username.eq(username));
    }

    if (age != null) {
        builder.and(user.age.goe(age));
    }

    return queryFactory
        .selectFrom(user)
        .where(builder)
        .fetch();
}
```

---

### [실무]

적합한 경우:

- OR 조건 많음
- 복잡한 검색 조건
- 관리자 검색

---

### [주의]

단점:

- if문 많아짐
- 코드 길어짐
- 재사용성 낮음

---

### [FAQ]

Q. BooleanBuilder 장점은?
A. 복잡한 조건을 직관적으로 누적할 수 있다.

Q. 언제 사용하는가?
A. 복잡한 OR 조건에서 유리하다.

---

# 3. BooleanExpression

## 3.1 BooleanExpression 개념

### [개념]

BooleanExpression은 조건 메서드를 분리하여 where()에 조합하는 방식이다.

실무 권장 방식이다.

---

### [핵심]

- 실무 권장
- 조건 메서드 분리
- null-safe
- 재사용성 우수
- 유지보수성 우수

---

### [예제]

```java
public List<User> search(String username, Integer age) {
    return queryFactory
        .selectFrom(user)
        .where(
            usernameEq(username),
            ageGoe(age)
        )
        .fetch();
}
```

조건 메서드:

```java
private BooleanExpression usernameEq(String username) {
    return username != null ? user.username.eq(username) : null;
}

private BooleanExpression ageGoe(Integer age) {
    return age != null ? user.age.goe(age) : null;
}
```

---

### [실무]

where()는 null 조건을 자동 무시한다.

이 덕분에 Optional Filter 구현이 매우 깔끔하다.

---

### [Flow]

```text
Parameter
→ Condition Method
→ BooleanExpression Return
→ where(...)
→ null Ignore
```

---

### [FAQ]

Q. BooleanExpression 장점은?
A. 재사용성, 가독성, 유지보수성이 뛰어나다.

Q. 왜 실무에서 선호되는가?
A. 코드 구조가 깔끔하고 테스트가 쉽기 때문이다.

---

# 4. BooleanBuilder vs BooleanExpression

## 4.1 Comparison

| Type              | 장점     | 단점           | 추천       |
| ----------------- | -------- | -------------- | ---------- |
| BooleanBuilder    | 직관적   | 코드 길어짐    | Complex OR |
| BooleanExpression | 재사용성 | 초기 설계 필요 | Most Cases |

---

### [FAQ]

Q. 실무 추천 방식은?
A. 대부분 BooleanExpression이다.

Q. BooleanBuilder는 언제 쓰는가?
A. 복잡한 OR 조건에서 사용한다.

---

# 5. Null-safe Condition

## 5.1 Null-safe 처리

### [개념]

Dynamic Query 핵심은 null-safe Condition 처리다.

조건값이 없으면 Query 조건에서 제외해야 한다.

---

### [핵심]

- null → 조건 제외
- value exists → 조건 적용

---

### [예제]

```java
private BooleanExpression statusEq(UserStatus status) {
    return status != null ? user.status.eq(status) : null;
}
```

---

### [FAQ]

Q. null-safe가 왜 중요한가?
A. 조건값이 없는 경우 Query 조건에서 제외해야 하기 때문이다.

---

# 6. BooleanExpression Composition

## 6.1 Condition 조합

### [개념]

BooleanExpression은 여러 조건 메서드를 조합하여 복합 Query를 만들 수 있다.

---

### [핵심]

- Condition Composition
- Complex Query
- Reusable Pattern

---

### [예제]

```java
private BooleanExpression allConditions(UserSearchDto dto) {
    return usernameEq(dto.username())
        .and(statusEq(dto.status()));
}
```

Query:

```java
queryFactory
    .selectFrom(user)
    .where(allConditions(dto))
    .fetch();
```

---

### [실무]

복잡한 검색 조건을 하나의 Condition Method로 묶을 때 사용한다.

---

### [FAQ]

Q. Condition 조합 장점은?
A. 복잡한 Query를 재사용 가능한 구조로 만들 수 있다.

---

# 7. String Filter Pattern

## 7.1 String 검색

### [개념]

String 조건은 null뿐 아니라 empty, blank도 처리해야 한다.

---

### [핵심]

- null 체크
- empty 체크
- blank 체크
- hasText 권장

---

### [예제]

```java
private BooleanExpression usernameEq(String username) {
    return StringUtils.hasText(username)
        ? user.username.eq(username)
        : null;
}
```

---

### [FAQ]

Q. String 조건 핵심은?
A. null, empty, blank 모두 처리하는 것이다.

---

# 8. Keyword Search Pattern

## 8.1 Multi-field Keyword Search

### [개념]

Keyword Search는 여러 컬럼을 OR 조건으로 검색하는 방식이다.

검색 API에서 매우 자주 사용된다.

---

### [핵심]

- OR Query
- Multi-field Search
- Keyword Search

---

### [예제]

```java
private BooleanExpression keywordSearch(String keyword) {
    if (!StringUtils.hasText(keyword)) {
        return null;
    }

    return user.username.contains(keyword)
        .or(user.email.contains(keyword));
}
```

---

### [실무]

예:

- username + email 검색
- title + content 검색
- festivalName + location 검색

---

### [주의]

contains는 LIKE `%keyword%`로 변환될 수 있다.

Index 효율이 낮을 수 있다.

---

### [FAQ]

Q. Keyword Search는 어떻게 구현하는가?
A. OR 조건으로 여러 컬럼을 검색한다.

---

# 9. Enum Filter Pattern

## 9.1 Enum 조건

### [예제]

```java
private BooleanExpression statusEq(UserStatus status) {
    return status != null
        ? user.status.eq(status)
        : null;
}
```

---

### [FAQ]

Q. Enum 필터는 어디에 많이 쓰는가?
A. 상태 검색 API에서 많이 사용된다.

---

# 10. Date Range Pattern

## 10.1 Date Range 검색

### [개념]

날짜 범위 검색은 실무 검색 API에서 매우 자주 사용된다.

---

### [핵심]

- startDate
- endDate
- between
- goe / loe

---

### [예제]

```java
private BooleanExpression createdAfter(LocalDateTime startDate) {
    return startDate != null
        ? user.createdAt.goe(startDate)
        : null;
}
```

```java
private BooleanExpression createdBefore(LocalDateTime endDate) {
    return endDate != null
        ? user.createdAt.loe(endDate)
        : null;
}
```

---

### [FAQ]

Q. 날짜 검색 구현은?
A. goe, loe, between을 사용한다.

---

# 11. Search DTO Pattern

## 11.1 Search DTO

### [개념]

검색 조건이 많아질수록 Search DTO 사용이 필수다.

---

### [예제]

```java
public record UserSearchDto(
    String keyword,
    UserStatus status,
    LocalDateTime startDate,
    LocalDateTime endDate
) {}
```

---

### [FAQ]

Q. Search DTO를 왜 사용하는가?
A. 검색 조건 관리와 유지보수성을 높이기 위해서다.

---

# 12. Common Mistakes

## 12.1 Dynamic Query 실수

### [핵심]

- if문 남발
- BooleanBuilder 과사용
- null-safe 누락
- empty string 누락
- Search DTO 미사용

---

### [Troubleshooting]

문제: Query가 너무 복잡함

원인:

- if문 남발

해결:

- BooleanExpression 구조로 리팩토링

---

### [FAQ]

Q. 가장 흔한 실수는?
A. if문 남발, null-safe 누락, empty string 처리 누락이다.

---

# 13. Related Documents

- QueryDSL_Practical_Part01_Basic.md
- QueryDSL_Practical_Part03_Paging_Projection.md
- QueryDSL_Practical_Part04_Practical.md

---

# Retrieval Queries

### [FAQ]

Q. Dynamic Query란?
A. 조건값에 따라 Query 조건이 동적으로 변경되는 Query 방식이다.

Q. QueryDSL Dynamic Query 핵심은?
A. BooleanBuilder와 BooleanExpression이다.

Q. 실무 권장 방식은?
A. 대부분 BooleanExpression이다.

Q. BooleanBuilder 장점은?
A. 복잡한 조건을 직관적으로 누적할 수 있다.

Q. BooleanExpression 장점은?
A. 재사용성과 유지보수성이 높다.

Q. Keyword Search는 어떻게 구현하는가?
A. OR 조건으로 여러 컬럼 검색을 수행한다.

Q. Date Range 검색 구현은?
A. goe, loe, between을 사용한다.

Q. Search DTO가 필요한 이유는?
A. 검색 조건 관리와 유지보수성을 높이기 위해서다.
