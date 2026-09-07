# SQL Part02 - Filtering, JOIN, Aggregation

---

# 1. Advanced Filtering

## 1.1 Filtering Purpose

### [개념]

Filtering은 SQL Query에서 필요한 Row만 선택하기 위해 조건을 적용하는 작업이다.

Filtering은 단순 조건 작성이 아니라 Query Purpose, Table Relationship, Index, Pagination, Backend Search Condition과 연결되는 핵심 설계 기준이다.

Filtering 조건이 잘못되면 결과 누락, 결과 과다, 성능 저하, Index 미사용, Pagination 불안정 문제가 발생할 수 있다.

---

### [핵심]

Filtering 핵심 기준:

- Query Purpose
- WHERE
- Equality Condition
- Range Condition
- LIKE Condition
- IN Condition
- NULL Condition
- AND / OR Combination
- Date Range
- Search Condition
- Index Candidate
- Dynamic Query
- QueryDSL BooleanExpression

Filtering 검토 대상:

- 조건 Column
- 비교 값 타입
- NULL 가능성
- Index 사용 가능성
- AND / OR 우선순위
- LIKE wildcard 위치
- 날짜 범위 조건
- 권한 조건 포함 여부

---

### [실무]

2026 Backend 실무 기준에서 Filtering은 API Search Request와 직접 연결된다.

```text
Search Request
→ Query Purpose
→ Filter Field 확인
→ Equal / Range / LIKE / IN 구분
→ WHERE 조건 구성
→ Index 가능성 검토
→ QueryDSL / JPQL / Native Query 선택
→ Pagination / Sorting 연결
```

예시:

```text
"서울 지역의 진행 중인 축제 목록"
→ 목록 조회
→ festivals
→ region_code = '11'
→ event_start_date <= today
→ event_end_date >= today
→ active = true
→ event_start_date 정렬
```

SQL 예시:

```sql
SELECT festival_id, title, event_start_date, event_end_date
FROM festivals
WHERE region_code = '11'
  AND event_start_date <= CURRENT_DATE
  AND event_end_date >= CURRENT_DATE
  AND active = true
ORDER BY event_start_date ASC, festival_id ASC;
```

---

### [FAQ]

Q. Filtering은 WHERE 조건만 의미해?
A. 아니다. Filtering은 Query Purpose, Search Request, Index, Pagination까지 연결되는 조회 조건 설계 기준이다.

Q. Filtering 조건을 작성할 때 가장 먼저 확인할 것은?
A. Query Purpose와 조건 Column이 어떤 Table에 속하는지 먼저 확인해야 한다.

Q. Filtering 조건이 성능에 영향을 줘?
A. 영향을 준다. WHERE 조건 Column이 Index 사용 가능성과 조회 범위를 결정하기 때문이다.

Q. Backend 검색 API에서 Filtering은 어디와 연결돼?
A. Request DTO, Service 검색 조건, Repository Query, QueryDSL BooleanExpression과 연결된다.

---

## 1.2 Equality and Range Condition

### [개념]

Equality Condition은 특정 값과 정확히 일치하는 Row를 찾는 조건이다.

Range Condition은 숫자, 날짜, 시간, 금액처럼 범위가 있는 값을 기준으로 Row를 찾는 조건이다.

---

### [핵심]

Equality 조건:

- `=`
- `<>`
- `!=`
- Boolean 조건
- Enum 조건
- Status 조건
- PK 조건
- Unique 조건

Range 조건:

- `>`
- `>=`
- `<`
- `<=`
- `BETWEEN`
- Date Range
- Number Range
- Price Range

---

### [실무]

Equality 예시:

```sql
SELECT user_id, email, nickname
FROM users
WHERE email = 'user@example.com';
```

Range 예시:

```sql
SELECT festival_id, title, event_start_date
FROM festivals
WHERE event_start_date >= '2026-01-01'
  AND event_start_date < '2027-01-01';
```

권장:

- PK / Unique 조회는 Equality 조건 우선
- 날짜 검색은 시작 포함, 끝 미포함 범위 권장
- Enum / Status는 허용 값 기준 통일
- Boolean Column은 명확한 true / false 조건 사용
- Range 조건 Column은 Index 후보로 검토

주의:

```sql
-- 비권장: Column에 함수 적용
WHERE YEAR(event_start_date) = 2026;

-- 권장: 범위 조건
WHERE event_start_date >= '2026-01-01'
  AND event_start_date < '2027-01-01';
```

---

### [FAQ]

Q. Equality Condition은 언제 사용해?
A. PK, Unique Column, Status, Enum, Boolean처럼 정확히 일치하는 값을 찾을 때 사용한다.

Q. Range Condition은 언제 사용해?
A. 날짜, 시간, 금액, 점수, 수량처럼 범위 기준으로 검색할 때 사용한다.

Q. 날짜 검색에서 YEAR(column)을 쓰면 왜 주의해야 해?
A. Column에 함수를 적용하면 Index를 효율적으로 사용하기 어려울 수 있기 때문이다.

Q. 날짜 범위 조건은 어떻게 쓰는 게 좋아?
A. 시작일 이상, 다음 기준일 미만 형태가 경계값 오류와 Index 사용 측면에서 좋다.

---

## 1.3 LIKE Search Condition

### [개념]

LIKE는 문자열 Pattern을 기준으로 Row를 검색하는 조건이다.

검색 기능에서 자주 사용하지만 wildcard 위치에 따라 Index 사용 가능성과 성능이 크게 달라진다.

---

### [핵심]

LIKE Pattern:

- `LIKE 'keyword%'`
- `LIKE '%keyword'`
- `LIKE '%keyword%'`
- Prefix Search
- Suffix Search
- Contains Search
- Leading Wildcard
- Full Text Search

---

### [실무]

Prefix Search 예시:

```sql
SELECT user_id, email
FROM users
WHERE email LIKE 'test%';
```

Contains Search 예시:

```sql
SELECT festival_id, title
FROM festivals
WHERE title LIKE '%불꽃%';
```

권장:

- Prefix Search는 일반 Index 활용 가능성 검토
- Contains Search는 데이터 양 증가 시 Full Text Search 검토
- 사용자 입력은 Parameter Binding 사용
- 검색 Keyword는 trim / empty check 처리
- 대소문자 구분은 DB Collation 확인
- 검색 조건이 많으면 QueryDSL 동적 조건 구성

주의:

- `LIKE '%keyword%'`는 일반 B-Tree Index 효율이 낮음
- 검색어가 빈 문자열이면 전체 조회로 변질될 수 있음
- 사용자 입력을 문자열 결합으로 직접 SQL에 넣지 않음
- 검색 조건과 Pagination을 함께 검토

---

### [FAQ]

Q. LIKE '%keyword%'는 왜 주의해야 해?
A. 앞쪽 wildcard가 있으면 일반 B-Tree Index를 효율적으로 사용하기 어렵기 때문이다.

Q. 제목 검색에는 LIKE를 써도 돼?
A. 가능하지만 데이터가 많아지면 Full Text Search나 검색 엔진 도입을 검토해야 한다.

Q. 사용자 검색어는 SQL에 직접 붙여도 돼?
A. 안 된다. SQL Injection 방지를 위해 Parameter Binding을 사용해야 한다.

Q. 빈 검색어는 어떻게 처리해야 해?
A. 전체 조회가 의도인지 확인하고, 필요하면 검색 조건을 제외하거나 요청을 검증해야 한다.

---

## 1.4 NULL Filtering

### [개념]

NULL은 값이 없거나 알 수 없음을 의미한다.

SQL에서 NULL은 일반 비교 연산으로 비교할 수 없으며 `IS NULL`, `IS NOT NULL`을 사용해야 한다.

---

### [핵심]

NULL 조건:

- IS NULL
- IS NOT NULL
- COALESCE
- NULL-safe 처리
- Optional Condition
- Nullable Column
- Soft Delete Column
- Deleted At
- Updated At

---

### [실무]

올바른 NULL 조건:

```sql
SELECT user_id, email
FROM users
WHERE deleted_at IS NULL;
```

잘못된 NULL 조건:

```sql
SELECT user_id, email
FROM users
WHERE deleted_at = NULL;
```

Soft Delete 예시:

```sql
SELECT post_id, title
FROM posts
WHERE deleted_at IS NULL
ORDER BY created_at DESC;
```

권장:

- Nullable Column은 조건 작성 전 의미 확인
- Soft Delete는 `deleted_at IS NULL` 또는 `active = true` 기준 통일
- Optional 검색 조건은 null일 때 Query 조건에서 제외
- COALESCE는 결과 표시용과 조건용을 구분
- NULL이 포함된 NOT IN 조건 주의

주의:

- `= NULL` 사용 금지
- `<> NULL` 사용 금지
- NULL은 UNKNOWN 결과를 만들 수 있음
- LEFT JOIN 결과의 NULL과 실제 Column NULL 구분 필요

---

### [FAQ]

Q. NULL은 = NULL로 비교해도 돼?
A. 안 된다. NULL 비교는 IS NULL 또는 IS NOT NULL을 사용해야 한다.

Q. Soft Delete 조회 조건은 어떻게 작성해?
A. deleted_at IS NULL 또는 active = true처럼 프로젝트 기준을 통일해서 사용한다.

Q. Optional 검색 조건이 null이면 어떻게 해?
A. 해당 조건을 Query에 포함하지 않는 방식으로 동적 Query를 구성하는 것이 일반적이다.

Q. LEFT JOIN 결과의 NULL은 무슨 의미야?
A. 오른쪽 Table에 매칭되는 Row가 없거나 실제 Column 값이 NULL일 수 있으므로 구분해야 한다.

---

# 2. JOIN Foundation

## 2.1 JOIN Purpose

### [개념]

JOIN은 두 개 이상의 Table을 Relationship Column 기준으로 연결해 조회하는 SQL 기능이다.

Backend Agent는 JOIN을 작성하기 전에 기준 Table, Relationship, Row 증가 가능성, 필요한 Column을 먼저 확인해야 한다.

---

### [핵심]

JOIN 핵심 요소:

- Base Table
- Target Table
- Primary Key
- Foreign Key
- Join Condition
- ON
- INNER JOIN
- LEFT JOIN
- 1:1 Relationship
- 1:N Relationship
- N:1 Relationship
- N:M Relationship
- Join Table

JOIN 검토 기준:

- 기준 Table이 명확한가?
- PK / FK 관계가 명확한가?
- JOIN 조건이 누락되지 않았는가?
- 1:N 중복 Row 가능성이 있는가?
- LEFT JOIN 유지 조건이 필요한가?
- 불필요한 JOIN은 없는가?

---

### [실무]

JOIN 설계 Flow:

```text
Requirement
→ Query Purpose
→ Base Table 선택
→ 필요한 Related Table 확인
→ PK / FK 관계 확인
→ INNER JOIN / LEFT JOIN 선택
→ ON 조건 작성
→ Row Count 증가 검토
→ SELECT Column 정리
→ WHERE 조건 검토
```

예시:

```text
"축제 리뷰 목록과 작성자 닉네임 조회"
→ reviews 기준
→ users Join 필요
→ reviews.user_id = users.user_id
→ 작성자가 존재해야 하므로 INNER JOIN 가능
```

SQL 예시:

```sql
SELECT r.review_id, r.content, r.rating, u.nickname
FROM reviews r
JOIN users u ON r.user_id = u.user_id
WHERE r.festival_id = 10
ORDER BY r.created_at DESC;
```

---

### [FAQ]

Q. JOIN을 설계할 때 가장 먼저 볼 것은?
A. ERD에서 PK와 FK 관계를 확인하고 기준 Table과 JOIN 방향을 정해야 한다.

Q. JOIN 조건을 빼면 어떻게 돼?
A. Cartesian Product가 발생해 Row 수가 폭증하고 잘못된 결과가 나올 수 있다.

Q. JOIN은 많을수록 좋아?
A. 아니다. 필요한 Table만 JOIN해야 하며 불필요한 JOIN은 성능 저하와 결과 왜곡을 만들 수 있다.

Q. JOIN 결과가 갑자기 늘어나는 이유는?
A. 1:N 관계 JOIN이거나 JOIN 조건이 잘못되어 하나의 Row가 여러 Row와 매칭되었을 수 있다.

---

## 2.2 INNER JOIN

### [개념]

INNER JOIN은 양쪽 Table에서 JOIN 조건에 매칭되는 Row만 조회한다.

매칭되지 않는 Row는 결과에서 제외된다.

---

### [핵심]

INNER JOIN 특징:

- 양쪽 매칭 필수
- 미매칭 Row 제외
- FK 관계 기반 조회에 자주 사용
- 필수 관계 조회에 적합
- 결과 Row 수는 관계에 따라 증가 가능

사용 상황:

- 작성자가 있는 리뷰
- 회원이 작성한 게시글
- 축제에 연결된 이미지
- 결제에 연결된 주문
- 찜한 축제 목록

---

### [실무]

INNER JOIN 예시:

```sql
SELECT r.review_id, r.content, u.nickname
FROM reviews r
JOIN users u ON r.user_id = u.user_id
WHERE r.festival_id = 10;
```

해석:

```text
reviews 기준
→ users와 user_id로 매칭
→ 작성자가 존재하는 review만 조회
```

권장:

- 필수 관계는 INNER JOIN 우선 검토
- JOIN 조건은 ON에 명확히 작성
- Column 출처는 Table Alias로 명확히 표현
- 1:N 관계에서는 중복 Row 검토
- JOIN Column Index 검토

주의:

- 매칭되지 않는 기준 Table Row는 제외됨
- 선택 관계에 INNER JOIN을 쓰면 결과 누락 가능
- JOIN 조건 누락 금지
- WHERE 조건으로 기준 Row를 과도하게 줄이지 않는지 확인

---

### [FAQ]

Q. INNER JOIN은 언제 사용해?
A. 양쪽 Table에 매칭되는 데이터만 필요한 경우 사용한다.

Q. INNER JOIN을 쓰면 기준 Table Row가 모두 유지돼?
A. 아니다. JOIN 조건에 매칭되지 않는 Row는 결과에서 제외된다.

Q. 선택 관계에 INNER JOIN을 쓰면 어떤 문제가 생겨?
A. 관련 데이터가 없는 기준 Row가 결과에서 누락될 수 있다.

Q. INNER JOIN에서도 Row가 중복될 수 있어?
A. 가능하다. 1:N 관계에서는 부모 Row가 자식 Row 수만큼 반복될 수 있다.

---

## 2.3 LEFT JOIN

### [개념]

LEFT JOIN은 왼쪽 기준 Table의 Row를 모두 유지하고 오른쪽 Table의 매칭 결과를 붙이는 JOIN이다.

오른쪽 Table에 매칭되는 Row가 없으면 오른쪽 Column은 NULL로 표시된다.

---

### [핵심]

LEFT JOIN 특징:

- 왼쪽 Table 유지
- 오른쪽 Table 미매칭 허용
- 오른쪽 Column NULL 가능
- 선택 관계 조회에 적합
- 통계 / 부가 정보 조회에 자주 사용

사용 상황:

- 리뷰가 없어도 축제 조회
- 이미지가 없어도 게시글 조회
- 결제가 없어도 주문 조회
- 댓글이 없어도 게시글 조회
- 알림 설정이 없어도 사용자 조회

---

### [실무]

LEFT JOIN 예시:

```sql
SELECT f.festival_id, f.title, r.review_id
FROM festivals f
LEFT JOIN reviews r ON f.festival_id = r.festival_id;
```

주의 예시:

```sql
-- LEFT JOIN이지만 WHERE 조건 때문에 INNER JOIN처럼 동작 가능
SELECT f.festival_id, f.title
FROM festivals f
LEFT JOIN reviews r ON f.festival_id = r.festival_id
WHERE r.rating >= 4;
```

권장 방식:

```sql
SELECT f.festival_id, f.title
FROM festivals f
LEFT JOIN reviews r
  ON f.festival_id = r.festival_id
 AND r.rating >= 4;
```

권장:

- 기준 Table을 유지해야 하면 LEFT JOIN 사용
- 오른쪽 Table 조건 위치를 ON / WHERE 중 의도에 맞게 선택
- NULL 결과 처리 기준 명확화
- 1:N LEFT JOIN 중복 Row 검토
- 집계 목적이면 GROUP BY 또는 Subquery 검토

---

### [FAQ]

Q. LEFT JOIN은 언제 사용해?
A. 기준 Table의 모든 Row를 유지하면서 관련 Table 데이터를 선택적으로 붙이고 싶을 때 사용한다.

Q. LEFT JOIN을 썼는데 결과가 줄어드는 이유는?
A. WHERE 절에서 오른쪽 Table 조건을 걸면 NULL Row가 제거되어 INNER JOIN처럼 동작할 수 있기 때문이다.

Q. LEFT JOIN의 오른쪽 Column이 NULL이면 무슨 뜻이야?
A. 오른쪽 Table에 매칭되는 Row가 없거나 실제 값이 NULL일 수 있다.

Q. LEFT JOIN 조건은 ON에 써야 해, WHERE에 써야 해?
A. 기준 Row 유지가 필요하면 오른쪽 Table 필터는 ON에 두는 것이 적합한 경우가 많다.

---

## 2.4 INNER JOIN vs LEFT JOIN

### [개념]

INNER JOIN과 LEFT JOIN은 매칭되지 않는 Row를 결과에 포함하는지 여부가 다르다.

JOIN 선택은 Query Purpose와 기준 Table 유지 여부에 따라 결정한다.

---

### [핵심]

비교:

| 비교           | INNER JOIN         | LEFT JOIN            |
| -------------- | ------------------ | -------------------- |
| 기준           | 양쪽 매칭 필수     | 왼쪽 Table 유지      |
| 미매칭 Row     | 제외               | 포함                 |
| 오른쪽 값      | 항상 존재          | NULL 가능            |
| 사용 목적      | 필수 관계 조회     | 선택 관계 조회       |
| 결과 누락 위험 | 선택 관계에서 높음 | WHERE 조건 위치 주의 |
| 대표 예시      | 작성자 있는 리뷰   | 리뷰 없는 축제 포함  |

---

### [실무]

선택 Flow:

```text
관련 데이터가 반드시 있어야 하는가?
→ Yes: INNER JOIN
→ No: LEFT JOIN

기준 Table Row를 모두 유지해야 하는가?
→ Yes: LEFT JOIN
→ No: INNER JOIN 가능

오른쪽 Table 조건이 있는가?
→ 기준 Row 유지 필요: ON 조건 검토
→ 매칭 Row만 필요: WHERE 조건 가능
```

예시:

```text
"리뷰가 있는 축제만 조회"
→ INNER JOIN or EXISTS

"리뷰가 없어도 모든 축제 조회"
→ LEFT JOIN

"별점 4점 이상 리뷰가 있으면 표시하되 축제는 모두 유지"
→ LEFT JOIN + ON rating condition
```

---

### [FAQ]

Q. INNER JOIN과 LEFT JOIN은 어떻게 골라?
A. 매칭되는 데이터만 필요하면 INNER JOIN, 기준 Table의 모든 Row를 유지해야 하면 LEFT JOIN을 사용한다.

Q. 기준 Table을 유지한다는 게 무슨 뜻이야?
A. 오른쪽 Table에 관련 데이터가 없어도 왼쪽 Table의 Row는 결과에 남긴다는 뜻이다.

Q. 리뷰가 없는 축제도 보여야 하면 어떤 JOIN을 써?
A. festivals를 기준으로 reviews를 LEFT JOIN해야 한다.

Q. 리뷰가 있는 축제만 보여야 하면 어떤 JOIN을 써?
A. INNER JOIN 또는 EXISTS를 사용할 수 있다.

---

# 3. JOIN Result Review

## 3.1 1:N JOIN Row Duplication

### [개념]

1:N JOIN에서는 부모 Table의 Row가 자식 Table Row 수만큼 반복될 수 있다.

이 현상은 정상적인 JOIN 결과일 수 있지만, 목록 조회나 집계 Query에서는 중복 데이터 문제로 보일 수 있다.

---

### [핵심]

중복 발생 상황:

- users 1:N posts
- festivals 1:N reviews
- festivals 1:N images
- posts 1:N comments
- orders 1:N order_items
- parent row repeated by child count

위험 상황:

- COUNT 결과 왜곡
- Pagination 중복
- DTO 중복 생성
- 화면 목록 중복
- DISTINCT 남용
- Fetch Join Pagination 문제

---

### [실무]

예시:

```sql
SELECT f.festival_id, f.title, r.review_id
FROM festivals f
JOIN reviews r ON f.festival_id = r.festival_id
WHERE f.festival_id = 10;
```

결과 해석:

```text
festival 1개
reviews 5개
→ 결과 Row 5개
→ festival 정보 5번 반복
```

집계 왜곡 예시:

```sql
SELECT f.festival_id, COUNT(r.review_id) AS review_count
FROM festivals f
JOIN reviews r ON f.festival_id = r.festival_id
JOIN festival_images i ON f.festival_id = i.festival_id
GROUP BY f.festival_id;
```

문제:

```text
reviews 5개
images 3개
→ JOIN 결과 15개
→ review_count가 실제보다 커질 수 있음
```

해결 방향:

- 집계 Subquery 분리
- COUNT(DISTINCT r.review_id) 검토
- 필요한 관계만 JOIN
- 목록 조회와 상세 조회 Query 분리
- Pagination 대상 Table 먼저 제한

---

### [FAQ]

Q. JOIN 후 Row 수가 갑자기 늘어나는 이유는?
A. 1:N 관계 JOIN에서 부모 Row가 자식 Row 수만큼 반복되기 때문이다.

Q. 1:N JOIN 중복은 항상 오류야?
A. 아니다. 관계상 정상 결과일 수 있지만 목록 조회나 집계에서는 문제를 만들 수 있다.

Q. COUNT 결과가 실제보다 크게 나오는 이유는?
A. 여러 1:N Table을 동시에 JOIN하면서 Row가 곱해졌을 가능성이 있다.

Q. DISTINCT를 쓰면 해결돼?
A. 일부 중복은 제거할 수 있지만 원인 해결이 아닐 수 있으므로 JOIN 구조와 집계 기준을 먼저 검토해야 한다.

---

## 3.2 JOIN Condition Safety

### [개념]

JOIN Condition Safety는 JOIN Query에서 ON 조건이 정확하게 작성되었는지 검토하는 기준이다.

JOIN 조건이 누락되거나 잘못되면 Cartesian Product, 잘못된 매칭, 중복 Row, 성능 저하가 발생한다.

---

### [핵심]

검토 대상:

- ON 조건 존재 여부
- PK / FK Column 매칭
- Table Alias 정확성
- Composite Key 조건
- Additional Join Condition
- Logical Relationship
- Data Type Match
- Join Direction

위험 패턴:

- JOIN without ON
- Wrong Column Join
- Non-related Column Join
- Missing Composite Key
- Implicit Join
- Cartesian Product

---

### [실무]

정상 JOIN:

```sql
SELECT fav.favorite_id, f.title
FROM favorites fav
JOIN festivals f ON fav.festival_id = f.festival_id
WHERE fav.user_id = 1;
```

위험 JOIN:

```sql
SELECT fav.favorite_id, f.title
FROM favorites fav
JOIN festivals f
WHERE fav.user_id = 1;
```

잘못된 Column JOIN:

```sql
SELECT fav.favorite_id, f.title
FROM favorites fav
JOIN festivals f ON fav.user_id = f.festival_id;
```

검수 Flow:

```text
JOIN Table 확인
→ ERD PK / FK 확인
→ ON 조건 확인
→ Column 타입 확인
→ Row Count 확인
→ 조건 추가 후 결과 확인
```

---

### [FAQ]

Q. JOIN 조건을 빼면 어떻게 돼?
A. Cartesian Product가 발생해 Row 수가 폭증하고 잘못된 결과가 나올 수 있다.

Q. JOIN 조건은 어떻게 검수해?
A. ERD에서 PK / FK 관계를 확인하고 ON 조건의 Column이 실제 관계와 일치하는지 확인한다.

Q. Composite Key 관계에서는 무엇을 주의해야 해?
A. 복합 키를 구성하는 모든 Column이 JOIN 조건에 포함되어야 한다.

Q. JOIN 조건이 맞는지 빠르게 확인하는 방법은?
A. Base Table 단독 Row 수와 JOIN 후 Row 수를 비교하고 샘플 데이터를 확인한다.

---

## 3.3 Unnecessary JOIN

### [개념]

Unnecessary JOIN은 Query Purpose에 필요하지 않은 Table을 JOIN하는 Anti Pattern이다.

불필요한 JOIN은 성능 저하, Row 중복, Pagination 문제, Query 복잡도 증가를 만든다.

---

### [핵심]

불필요한 JOIN 판단 기준:

- SELECT에 사용하지 않는 Table
- WHERE에 사용하지 않는 Table
- ORDER BY에 사용하지 않는 Table
- 권한 검증에 필요 없는 Table
- 존재 여부만 필요한데 전체 JOIN
- 집계 목적이 아닌데 1:N Table JOIN

위험:

- Query Performance 저하
- 중복 Row
- DTO Mapping 복잡도 증가
- N+1 문제 회피 실패
- Pagination 결과 왜곡

---

### [실무]

불필요한 JOIN 예시:

```sql
SELECT f.festival_id, f.title
FROM festivals f
JOIN reviews r ON f.festival_id = r.festival_id
WHERE f.active = true;
```

문제:

```text
reviews Column을 SELECT하지 않음
reviews 조건도 없음
리뷰 수만큼 festival Row 중복 가능
```

개선:

```sql
SELECT f.festival_id, f.title
FROM festivals f
WHERE f.active = true;
```

존재 여부가 목적이면 EXISTS 검토:

```sql
SELECT f.festival_id, f.title
FROM festivals f
WHERE EXISTS (
  SELECT 1
  FROM reviews r
  WHERE r.festival_id = f.festival_id
);
```

---

### [FAQ]

Q. 불필요한 JOIN은 왜 문제야?
A. 성능 저하, 중복 Row, Pagination 오류, Query 복잡도 증가를 만들 수 있기 때문이다.

Q. JOIN이 필요한지 어떻게 판단해?
A. SELECT, WHERE, ORDER BY, 권한 조건, 집계 목적에 해당 Table이 실제로 필요한지 확인한다.

Q. 존재 여부만 확인하려면 JOIN이 좋아?
A. 관련 Row 존재 여부만 필요하면 EXISTS가 더 명확한 경우가 많다.

Q. JOIN을 줄이면 항상 좋아?
A. 필요한 관계 조회는 유지해야 하지만 Query Purpose와 무관한 JOIN은 제거하는 것이 좋다.

---

# 4. Aggregation Foundation

## 4.1 Aggregation Purpose

### [개념]

Aggregation은 여러 Row를 그룹화하거나 계산하여 COUNT, SUM, AVG, MIN, MAX 같은 집계 결과를 만드는 작업이다.

Backend에서는 통계 API, 관리자 대시보드, 인기순 정렬, 리뷰 수, 평균 평점, 매출 합계 등에 사용된다.

---

### [핵심]

Aggregation 함수:

- COUNT
- SUM
- AVG
- MIN
- MAX

Aggregation 관련 절:

- GROUP BY
- HAVING
- DISTINCT
- ORDER BY Aggregation Result

사용 목적:

- Count
- Total
- Average
- Minimum
- Maximum
- Ranking
- Statistics
- Dashboard
- Popular Score

---

### [실무]

축제별 리뷰 수와 평균 평점:

```sql
SELECT festival_id,
       COUNT(*) AS review_count,
       AVG(rating) AS average_rating
FROM reviews
GROUP BY festival_id
ORDER BY average_rating DESC;
```

월별 가입자 수:

```sql
SELECT DATE_FORMAT(created_at, '%Y-%m') AS signup_month,
       COUNT(*) AS signup_count
FROM users
GROUP BY DATE_FORMAT(created_at, '%Y-%m')
ORDER BY signup_month ASC;
```

권장:

- GROUP BY 기준 명확화
- 집계 결과 Alias 작성
- COUNT(\*)와 COUNT(column) 차이 이해
- JOIN 후 집계 중복 검토
- HAVING과 WHERE 역할 분리
- 통계 Query는 Index와 데이터 양 검토

---

### [FAQ]

Q. Aggregation은 언제 사용해?
A. Row 수, 합계, 평균, 최소값, 최대값, 통계 결과가 필요할 때 사용한다.

Q. GROUP BY는 언제 써?
A. 사용자별 주문 수, 축제별 리뷰 수처럼 특정 기준별 집계 결과가 필요할 때 사용한다.

Q. 집계 결과에는 Alias가 필요해?
A. 권장된다. DTO 매핑과 결과 해석을 명확히 하기 위해 review_count 같은 Alias를 사용한다.

Q. JOIN 후 집계에서 가장 주의할 점은?
A. 1:N JOIN으로 Row가 중복되어 COUNT나 SUM 결과가 왜곡될 수 있다.

---

## 4.2 COUNT, SUM, AVG, MIN, MAX

### [개념]

Aggregation Function은 여러 Row의 값을 계산하여 하나의 결과 또는 그룹별 결과를 반환하는 함수다.

각 함수는 NULL 처리 방식과 사용 목적이 다르다.

---

### [핵심]

집계 함수:

| 함수          | 목적              | NULL 처리 |
| ------------- | ----------------- | --------- |
| COUNT(\*)     | Row 수            | NULL 포함 |
| COUNT(column) | NULL이 아닌 값 수 | NULL 제외 |
| SUM(column)   | 합계              | NULL 제외 |
| AVG(column)   | 평균              | NULL 제외 |
| MIN(column)   | 최소값            | NULL 제외 |
| MAX(column)   | 최대값            | NULL 제외 |

---

### [실무]

COUNT 예시:

```sql
SELECT COUNT(*) AS total_count
FROM reviews
WHERE festival_id = 10;
```

COUNT(column) 예시:

```sql
SELECT COUNT(image_url) AS image_count
FROM festival_images
WHERE festival_id = 10;
```

SUM 예시:

```sql
SELECT festival_id, SUM(amount) AS total_donation_amount
FROM donations
GROUP BY festival_id;
```

AVG 예시:

```sql
SELECT festival_id, AVG(rating) AS average_rating
FROM reviews
GROUP BY festival_id;
```

권장:

- 전체 Row 수는 COUNT(\*)
- NULL 제외 개수는 COUNT(column)
- 금액 합계는 SUM
- 평균 평점은 AVG
- 집계 결과 NULL 가능성 처리
- 소수점 / 반올림 정책은 Application 또는 SQL 기준 통일

---

### [FAQ]

Q. COUNT(_)와 COUNT(column)은 달라?
A. COUNT(_)는 Row 수를 세고 COUNT(column)은 해당 Column이 NULL이 아닌 Row만 센다.

Q. AVG는 NULL을 포함해서 계산해?
A. 아니다. AVG(column)은 NULL 값을 제외하고 평균을 계산한다.

Q. SUM 결과가 NULL이 될 수 있어?
A. 집계 대상 Row가 없거나 값이 모두 NULL이면 NULL이 될 수 있어 COALESCE 처리를 검토한다.

Q. 평균 평점은 SQL에서 계산해도 돼?
A. 가능하다. 다만 반올림, 소수점 자리, 캐싱 기준은 프로젝트 정책으로 통일해야 한다.

---

## 4.3 GROUP BY Rules

### [개념]

GROUP BY는 특정 Column 값을 기준으로 Row를 그룹화하여 그룹별 Aggregation 결과를 만드는 절이다.

GROUP BY Query에서는 SELECT Column과 집계 함수의 관계를 명확히 해야 한다.

---

### [핵심]

GROUP BY 기준:

- Grouping Column
- Aggregation Function
- Group Result
- HAVING
- Aggregation Alias
- Group Sorting

주의 대상:

- SELECT 일반 Column
- GROUP BY 누락
- Non-aggregated Column
- Duplicate Row
- Join Multiplication
- SQL Mode Difference

---

### [실무]

정상 예시:

```sql
SELECT festival_id, COUNT(*) AS review_count
FROM reviews
GROUP BY festival_id;
```

잘못된 예시:

```sql
SELECT festival_id, content, COUNT(*) AS review_count
FROM reviews
GROUP BY festival_id;
```

문제:

```text
festival_id로 그룹화했는데 content는 그룹 기준도 아니고 집계 함수도 아님
DBMS 설정에 따라 오류 또는 예측 어려운 값 반환 가능
```

권장:

- SELECT 일반 Column은 GROUP BY에 포함
- 그룹별 계산 값은 Aggregation Function 사용
- JOIN 후 GROUP BY는 중복 Row 검토
- 집계 결과 정렬은 Alias 사용 가능
- 통계 Query는 요구사항 기준 그룹 단위를 명확히 정의

---

### [FAQ]

Q. GROUP BY에서 SELECT 일반 Column은 어떻게 해야 해?
A. 집계 함수가 아닌 일반 Column은 GROUP BY 기준에 포함해야 한다.

Q. GROUP BY 없이 COUNT만 쓰면 어떻게 돼?
A. 전체 Row를 하나의 그룹처럼 계산하여 전체 집계 결과를 반환한다.

Q. GROUP BY 기준은 어떻게 정해?
A. 사용자별, 축제별, 월별처럼 통계를 나눌 단위를 기준으로 정한다.

Q. GROUP BY 결과가 이상하면 무엇을 확인해?
A. JOIN으로 Row가 중복되었는지, GROUP BY 기준이 맞는지, SELECT Column이 적절한지 확인한다.

---

## 4.4 HAVING Rules

### [개념]

HAVING은 GROUP BY 이후 집계 결과를 필터링하는 절이다.

WHERE가 개별 Row 조건을 처리한다면 HAVING은 그룹 결과 조건을 처리한다.

---

### [핵심]

HAVING 사용 상황:

- COUNT(\*) >= n
- SUM(amount) >= n
- AVG(rating) >= n
- MIN(value) condition
- MAX(value) condition
- Group Result Filtering

WHERE와 차이:

- WHERE: 그룹화 전 Row 필터링
- HAVING: 그룹화 후 집계 결과 필터링

---

### [실무]

예시:

```sql
SELECT festival_id, COUNT(*) AS review_count
FROM reviews
GROUP BY festival_id
HAVING COUNT(*) >= 10;
```

WHERE + HAVING 예시:

```sql
SELECT festival_id, COUNT(*) AS high_rating_count
FROM reviews
WHERE rating >= 4
GROUP BY festival_id
HAVING COUNT(*) >= 10;
```

해석:

```text
rating >= 4 리뷰만 먼저 필터링
→ festival_id별 그룹화
→ 고평점 리뷰가 10개 이상인 축제만 반환
```

권장:

- 개별 Row 조건은 WHERE
- 집계 결과 조건은 HAVING
- 가능한 Row 조건은 WHERE로 먼저 줄임
- HAVING을 WHERE 대체로 남용하지 않음
- 집계 조건은 요구사항 언어와 정확히 매칭

---

### [FAQ]

Q. HAVING은 언제 사용해?
A. GROUP BY 이후 COUNT, SUM, AVG 같은 집계 결과를 조건으로 필터링할 때 사용한다.

Q. WHERE와 HAVING 차이는?
A. WHERE는 그룹화 전 Row 필터링이고 HAVING은 GROUP BY 이후 집계 결과 필터링이다.

Q. 집계 조건은 WHERE에 쓰면 안 돼?
A. 집계 함수 결과 조건은 HAVING에 작성해야 한다.

Q. WHERE와 HAVING을 같이 쓸 수 있어?
A. 가능하다. WHERE로 집계 전 데이터를 줄이고 HAVING으로 집계 결과를 필터링한다.

---

# 5. Aggregation with JOIN

## 5.1 JOIN Aggregation Risk

### [개념]

JOIN Aggregation Risk는 JOIN 후 Aggregation을 수행할 때 Row 중복으로 집계 결과가 왜곡되는 문제다.

특히 여러 1:N Table을 동시에 JOIN하면 Row가 곱해져 COUNT, SUM, AVG 결과가 실제보다 커질 수 있다.

---

### [핵심]

위험 상황:

- 1:N JOIN 후 COUNT
- 여러 1:N Table 동시 JOIN
- Image + Review 동시 JOIN
- Order + OrderItem + Payment JOIN
- Parent Row 중복
- COUNT 중복
- SUM 중복
- AVG 왜곡

검토 기준:

- JOIN 전 Row 수
- JOIN 후 Row 수
- GROUP BY 기준
- DISTINCT 필요 여부
- Subquery 분리 가능성
- Aggregation 대상 Table

---

### [실무]

위험 예시:

```sql
SELECT f.festival_id,
       COUNT(r.review_id) AS review_count,
       COUNT(i.image_id) AS image_count
FROM festivals f
LEFT JOIN reviews r ON f.festival_id = r.festival_id
LEFT JOIN festival_images i ON f.festival_id = i.festival_id
GROUP BY f.festival_id;
```

문제:

```text
reviews 5개
images 3개
→ JOIN 결과 15개
→ review_count와 image_count가 왜곡될 수 있음
```

개선 예시:

```sql
SELECT f.festival_id,
       f.title,
       COALESCE(rc.review_count, 0) AS review_count,
       COALESCE(ic.image_count, 0) AS image_count
FROM festivals f
LEFT JOIN (
  SELECT festival_id, COUNT(*) AS review_count
  FROM reviews
  GROUP BY festival_id
) rc ON f.festival_id = rc.festival_id
LEFT JOIN (
  SELECT festival_id, COUNT(*) AS image_count
  FROM festival_images
  GROUP BY festival_id
) ic ON f.festival_id = ic.festival_id;
```

---

### [FAQ]

Q. JOIN 후 COUNT가 실제보다 크게 나오는 이유는?
A. 여러 1:N Table을 JOIN하면서 Row가 곱해졌을 가능성이 있다.

Q. JOIN Aggregation 문제는 어떻게 해결해?
A. 집계 Subquery를 분리하거나 COUNT(DISTINCT)를 검토하고 JOIN 구조를 단순화한다.

Q. COUNT(DISTINCT)를 쓰면 항상 해결돼?
A. 결과 왜곡은 줄일 수 있지만 성능 비용이 있을 수 있어 Subquery 분리도 함께 검토해야 한다.

Q. 집계 Query에서 JOIN 전후 Row 수를 왜 봐야 해?
A. Row 증가가 집계 결과 왜곡의 핵심 원인이기 때문이다.

---

## 5.2 COUNT DISTINCT

### [개념]

COUNT DISTINCT는 중복을 제거한 고유 값 개수를 계산하는 Aggregation 방식이다.

JOIN으로 인해 중복 Row가 발생할 때 특정 Column 기준의 고유 개수를 구하는 데 사용할 수 있다.

---

### [핵심]

COUNT DISTINCT 사용 상황:

- 중복 JOIN 결과 제거
- 고유 사용자 수
- 고유 리뷰 수
- 고유 주문 수
- 고유 축제 수
- Many-to-Many 집계

주의:

- 성능 비용
- 대상 Column 선택
- NULL 제외
- Composite Distinct DBMS 차이
- 근본 원인 검토 필요

---

### [실무]

예시:

```sql
SELECT f.festival_id,
       COUNT(DISTINCT r.review_id) AS review_count
FROM festivals f
LEFT JOIN reviews r ON f.festival_id = r.festival_id
LEFT JOIN festival_images i ON f.festival_id = i.festival_id
GROUP BY f.festival_id;
```

고유 사용자 수 예시:

```sql
SELECT festival_id,
       COUNT(DISTINCT user_id) AS participant_count
FROM visit_histories
GROUP BY festival_id;
```

권장:

- 중복 제거 기준 Column을 명확히 선택
- COUNT(DISTINCT) 성능 비용 검토
- 대량 데이터에서는 별도 집계 Table / Cache 검토
- 여러 집계를 동시에 하면 Subquery 분리 검토
- Query Purpose가 고유 개수인지 총 Row 수인지 구분

---

### [FAQ]

Q. COUNT(DISTINCT)는 언제 사용해?
A. 중복 Row가 있을 때 특정 Column의 고유 개수를 계산해야 할 때 사용한다.

Q. COUNT(DISTINCT)는 COUNT(_)와 뭐가 달라?
A. COUNT(_)는 전체 Row 수를 세고 COUNT(DISTINCT column)은 중복을 제거한 고유 값 수를 센다.

Q. COUNT(DISTINCT)는 성능에 부담이 있어?
A. 있을 수 있다. 중복 제거 연산이 필요하므로 대량 데이터에서는 실행 계획을 확인해야 한다.

Q. COUNT(DISTINCT)를 쓰기 전에 확인할 것은?
A. 중복이 왜 발생했는지 JOIN 구조와 GROUP BY 기준을 먼저 확인해야 한다.

---

# 6. Filtering, JOIN, Aggregation Review

## 6.1 Query Review Flow

### [개념]

Filtering, JOIN, Aggregation Review는 SQL 결과 정확성과 성능을 검토하기 위한 단계적 점검 과정이다.

Query는 한 번에 완성하기보다 Base Table부터 조건, JOIN, GROUP BY를 순서대로 추가하며 검토한다.

---

### [핵심]

Review Flow:

```text
Expected Result 정의
→ Base Table 확인
→ WHERE 조건 추가
→ JOIN 추가
→ Row Count 확인
→ GROUP BY 추가
→ Aggregation 결과 확인
→ HAVING 조건 확인
→ ORDER BY / Pagination 확인
→ Index 가능성 검토
```

검토 대상:

- Query Purpose
- Base Table
- WHERE Condition
- JOIN Condition
- Row Count
- GROUP BY
- Aggregation Function
- HAVING
- ORDER BY
- Pagination
- Index

---

### [실무]

Debug 예시:

```text
문제: 축제별 리뷰 수가 실제보다 많음

1. reviews 단독 COUNT 확인
2. festivals + reviews JOIN 확인
3. festival_images JOIN 추가 후 Row 증가 확인
4. GROUP BY 기준 확인
5. COUNT(DISTINCT) 또는 Subquery 분리 검토
```

Base Query부터 확인:

```sql
SELECT COUNT(*)
FROM reviews
WHERE festival_id = 10;
```

JOIN 후 확인:

```sql
SELECT f.festival_id, r.review_id, i.image_id
FROM festivals f
LEFT JOIN reviews r ON f.festival_id = r.festival_id
LEFT JOIN festival_images i ON f.festival_id = i.festival_id
WHERE f.festival_id = 10;
```

---

### [FAQ]

Q. SQL 결과가 이상하면 어디서부터 확인해?
A. Base Table 단독 조회부터 시작해 WHERE, JOIN, GROUP BY를 단계적으로 추가하며 Row 수를 확인한다.

Q. JOIN 문제와 Aggregation 문제를 어떻게 구분해?
A. JOIN 직후 Row 수가 증가했는지 확인하고, GROUP BY 이후 집계 결과가 왜곡되는지 확인한다.

Q. Query Debug에서 Row Count가 중요한 이유는?
A. Row Count 변화가 조건 누락, JOIN 중복, 집계 왜곡을 찾는 핵심 단서이기 때문이다.

Q. 복잡한 Query는 어떻게 검수해?
A. 한 번에 보지 말고 Base Query, Filter, Join, Aggregation, Pagination 단계로 나누어 검수한다.

---

## 6.2 Common Mistakes

### [개념]

Common Mistakes는 Filtering, JOIN, Aggregation에서 자주 발생하는 SQL 실수다.

AI Agent는 Query 생성 시 Common Mistakes를 Anti Pattern으로 감지하고 수정 방향을 제안해야 한다.

---

### [핵심]

자주 발생하는 실수:

- WHERE 조건 누락
- NULL을 `= NULL`로 비교
- AND / OR 괄호 누락
- LIKE '%keyword%' 성능 문제 무시
- JOIN 조건 누락
- 잘못된 Column으로 JOIN
- LEFT JOIN 후 WHERE 조건 실수
- 1:N JOIN 중복 Row 미검토
- GROUP BY와 일반 Column 혼용
- COUNT(\*)와 COUNT(column) 차이 오해
- 여러 1:N JOIN 후 COUNT 왜곡
- HAVING을 WHERE처럼 남용
- DISTINCT 남용
- 불필요한 JOIN

---

### [실무]

문제와 해결 예시:

```text
문제: LEFT JOIN인데 기준 Row가 사라짐
원인: WHERE에서 오른쪽 Table 조건 사용
해결: 조건을 ON으로 이동하거나 INNER JOIN 의도인지 재검토
```

```text
문제: 리뷰 수가 실제보다 많음
원인: reviews와 images를 동시에 JOIN하여 Row가 곱해짐
해결: 집계 Subquery 분리 또는 COUNT(DISTINCT review_id) 검토
```

```text
문제: 검색 Query가 느림
원인: LIKE '%keyword%'와 대량 데이터
해결: Full Text Search, Index 전략, 검색 엔진 검토
```

---

### [FAQ]

Q. Filtering에서 가장 흔한 실수는?
A. NULL 비교 오류, AND / OR 괄호 누락, LIKE wildcard 성능 문제 무시가 많다.

Q. JOIN에서 가장 흔한 실수는?
A. JOIN 조건 누락, 잘못된 Column JOIN, LEFT JOIN 후 WHERE 조건 실수, 1:N 중복 미검토가 많다.

Q. Aggregation에서 가장 흔한 실수는?
A. GROUP BY 기준 오류, COUNT 차이 오해, JOIN으로 인한 집계 왜곡이 많다.

Q. DISTINCT는 중복 해결에 항상 좋은 방법이야?
A. 아니다. 원인을 숨길 수 있으므로 JOIN 구조와 Query Purpose를 먼저 검토해야 한다.

---

## 6.3 Checklist

### [개념]

Checklist는 Filtering, JOIN, Aggregation Query를 최종 검수하기 위한 기준이다.

Agent는 Query 생성 후 Checklist를 기준으로 치명적 오류를 탐지해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Query Purpose가 명확한가?
- [ ] Base Table이 요구사항과 일치하는가?
- [ ] WHERE 조건이 필요한 Row만 남기는가?
- [ ] NULL 비교를 IS NULL / IS NOT NULL로 처리했는가?
- [ ] AND / OR 조건에 괄호가 필요한가?
- [ ] LIKE 조건의 wildcard 위치를 검토했는가?
- [ ] 날짜 조건이 Sargable Range 조건인가?
- [ ] JOIN이 실제로 필요한가?
- [ ] JOIN 조건이 PK / FK 관계와 일치하는가?
- [ ] INNER JOIN / LEFT JOIN 선택이 Query Purpose와 일치하는가?
- [ ] LEFT JOIN 후 WHERE 조건으로 기준 Row가 제거되지 않는가?
- [ ] 1:N JOIN으로 Row 중복이 발생하지 않는가?
- [ ] GROUP BY 기준이 명확한가?
- [ ] SELECT 일반 Column이 GROUP BY와 충돌하지 않는가?
- [ ] COUNT(\*)와 COUNT(column)을 구분했는가?
- [ ] JOIN 후 Aggregation 결과가 왜곡되지 않는가?
- [ ] HAVING과 WHERE 역할을 구분했는가?
- [ ] DISTINCT를 원인 분석 없이 남용하지 않았는가?
- [ ] Index 후보 Column을 확인했는가?
- [ ] Pagination과 ORDER BY 연결을 검토했는가?
```

---

### [실무]

검수 Flow:

```text
Draft SQL
→ Filtering Review
→ Join Review
→ Row Count Review
→ Aggregation Review
→ HAVING Review
→ Performance Review
→ Backend Mapping Review
→ Final SQL
```

치명적 문제:

- JOIN 조건 누락
- WHERE 없는 변경 Query
- LEFT JOIN 결과 누락
- GROUP BY 오류
- 집계 결과 왜곡
- NULL 비교 오류
- AND / OR 우선순위 오류
- Pagination 중복 / 누락

---

### [FAQ]

Q. Part02 Query 검수에서 가장 중요한 것은?
A. Filtering 조건 정확성, JOIN 조건 안전성, 1:N 중복 Row, Aggregation 결과 왜곡 여부다.

Q. JOIN Query는 무엇을 먼저 검수해?
A. Base Table과 PK / FK 기반 ON 조건이 정확한지 먼저 확인한다.

Q. Aggregation Query는 무엇을 먼저 검수해?
A. GROUP BY 기준과 JOIN으로 인한 Row 중복 여부를 먼저 확인한다.

Q. SQL Query의 치명적 문제는 뭐야?
A. JOIN 조건 누락, 잘못된 Filtering, GROUP BY 오류, 집계 왜곡, NULL 비교 오류가 치명적이다.

---

# Retrieval Queries

### [FAQ]

Q. SQL Part02는 무엇을 다뤄?
A. Filtering, JOIN, Aggregation, GROUP BY, HAVING, JOIN 결과 중복, 집계 왜곡 검토 기준을 다룬다.

Q. Filtering은 무엇이야?
A. SQL Query에서 필요한 Row만 선택하기 위해 WHERE 조건을 적용하는 작업이다.

Q. Filtering 조건을 작성할 때 가장 먼저 확인할 것은?
A. Query Purpose와 조건 Column이 어떤 Table에 속하는지 먼저 확인해야 한다.

Q. WHERE 조건은 성능에 영향을 줘?
A. 영향을 준다. WHERE 조건 Column이 Index 사용 가능성과 조회 범위를 결정하기 때문이다.

Q. Equality Condition은 언제 사용해?
A. PK, Unique Column, Status, Enum, Boolean처럼 정확히 일치하는 값을 찾을 때 사용한다.

Q. Range Condition은 언제 사용해?
A. 날짜, 시간, 금액, 점수, 수량처럼 범위 기준으로 검색할 때 사용한다.

Q. 날짜 검색에서 YEAR(column)을 쓰면 왜 주의해야 해?
A. Column에 함수를 적용하면 Index를 효율적으로 사용하기 어려울 수 있기 때문이다.

Q. 날짜 조건은 어떻게 쓰는 게 좋아?
A. 시작일 이상, 다음 기준일 미만 형태의 Range Condition이 좋다.

Q. LIKE '%keyword%'는 왜 주의해야 해?
A. 앞쪽 wildcard가 있으면 일반 B-Tree Index를 효율적으로 사용하기 어렵기 때문이다.

Q. 제목 검색에는 LIKE를 써도 돼?
A. 가능하지만 데이터가 많아지면 Full Text Search나 검색 엔진 도입을 검토해야 한다.

Q. 사용자 검색어는 SQL에 직접 붙여도 돼?
A. 안 된다. SQL Injection 방지를 위해 Parameter Binding을 사용해야 한다.

Q. NULL은 = NULL로 비교해도 돼?
A. 안 된다. NULL 비교는 IS NULL 또는 IS NOT NULL을 사용해야 한다.

Q. Soft Delete 조회 조건은 어떻게 작성해?
A. deleted_at IS NULL 또는 active = true처럼 프로젝트 기준을 통일해서 사용한다.

Q. Optional 검색 조건이 null이면 어떻게 해?
A. 해당 조건을 Query에 포함하지 않는 방식으로 동적 Query를 구성하는 것이 일반적이다.

Q. JOIN은 무엇이야?
A. 두 개 이상의 Table을 Relationship Column 기준으로 연결해 조회하는 SQL 기능이다.

Q. JOIN을 설계할 때 가장 먼저 볼 것은?
A. ERD에서 PK와 FK 관계를 확인하고 기준 Table과 JOIN 방향을 정해야 한다.

Q. JOIN 조건을 빼면 어떻게 돼?
A. Cartesian Product가 발생해 Row 수가 폭증하고 잘못된 결과가 나올 수 있다.

Q. INNER JOIN은 언제 사용해?
A. 양쪽 Table에 매칭되는 데이터만 필요한 경우 사용한다.

Q. INNER JOIN을 쓰면 기준 Table Row가 모두 유지돼?
A. 아니다. JOIN 조건에 매칭되지 않는 Row는 결과에서 제외된다.

Q. LEFT JOIN은 언제 사용해?
A. 기준 Table의 모든 Row를 유지하면서 관련 Table 데이터를 선택적으로 붙이고 싶을 때 사용한다.

Q. LEFT JOIN을 썼는데 결과가 줄어드는 이유는?
A. WHERE 절에서 오른쪽 Table 조건을 걸면 NULL Row가 제거되어 INNER JOIN처럼 동작할 수 있기 때문이다.

Q. INNER JOIN과 LEFT JOIN은 어떻게 골라?
A. 매칭되는 데이터만 필요하면 INNER JOIN, 기준 Table의 모든 Row를 유지해야 하면 LEFT JOIN을 사용한다.

Q. 리뷰가 없는 축제도 보여야 하면 어떤 JOIN을 써?
A. festivals를 기준으로 reviews를 LEFT JOIN해야 한다.

Q. JOIN 후 Row 수가 갑자기 늘어나는 이유는?
A. 1:N 관계 JOIN에서 부모 Row가 자식 Row 수만큼 반복되기 때문이다.

Q. 1:N JOIN 중복은 항상 오류야?
A. 아니다. 관계상 정상 결과일 수 있지만 목록 조회나 집계에서는 문제를 만들 수 있다.

Q. JOIN 조건은 어떻게 검수해?
A. ERD에서 PK / FK 관계를 확인하고 ON 조건의 Column이 실제 관계와 일치하는지 확인한다.

Q. 불필요한 JOIN은 왜 문제야?
A. 성능 저하, 중복 Row, Pagination 오류, Query 복잡도 증가를 만들 수 있기 때문이다.

Q. 존재 여부만 확인하려면 JOIN이 좋아?
A. 관련 Row 존재 여부만 필요하면 EXISTS가 더 명확한 경우가 많다.

Q. Aggregation은 언제 사용해?
A. Row 수, 합계, 평균, 최소값, 최대값, 통계 결과가 필요할 때 사용한다.

Q. GROUP BY는 언제 써?
A. 사용자별 주문 수, 축제별 리뷰 수처럼 특정 기준별 집계 결과가 필요할 때 사용한다.

Q. COUNT(_)와 COUNT(column)은 달라?
A. COUNT(_)는 Row 수를 세고 COUNT(column)은 해당 Column이 NULL이 아닌 Row만 센다.

Q. AVG는 NULL을 포함해서 계산해?
A. 아니다. AVG(column)은 NULL 값을 제외하고 평균을 계산한다.

Q. SUM 결과가 NULL이 될 수 있어?
A. 집계 대상 Row가 없거나 값이 모두 NULL이면 NULL이 될 수 있어 COALESCE 처리를 검토한다.

Q. GROUP BY에서 SELECT 일반 Column은 어떻게 해야 해?
A. 집계 함수가 아닌 일반 Column은 GROUP BY 기준에 포함해야 한다.

Q. GROUP BY 결과가 이상하면 무엇을 확인해?
A. JOIN으로 Row가 중복되었는지, GROUP BY 기준이 맞는지, SELECT Column이 적절한지 확인한다.

Q. HAVING은 언제 사용해?
A. GROUP BY 이후 COUNT, SUM, AVG 같은 집계 결과를 조건으로 필터링할 때 사용한다.

Q. WHERE와 HAVING 차이는?
A. WHERE는 그룹화 전 Row 필터링이고 HAVING은 GROUP BY 이후 집계 결과 필터링이다.

Q. JOIN 후 COUNT가 실제보다 크게 나오는 이유는?
A. 여러 1:N Table을 JOIN하면서 Row가 곱해졌을 가능성이 있다.

Q. JOIN Aggregation 문제는 어떻게 해결해?
A. 집계 Subquery를 분리하거나 COUNT(DISTINCT)를 검토하고 JOIN 구조를 단순화한다.

Q. COUNT(DISTINCT)는 언제 사용해?
A. 중복 Row가 있을 때 특정 Column의 고유 개수를 계산해야 할 때 사용한다.

Q. SQL 결과가 이상하면 어디서부터 확인해?
A. Base Table 단독 조회부터 시작해 WHERE, JOIN, GROUP BY를 단계적으로 추가하며 Row 수를 확인한다.

Q. Part02 Query 검수에서 가장 중요한 것은?
A. Filtering 조건 정확성, JOIN 조건 안전성, 1:N 중복 Row, Aggregation 결과 왜곡 여부다.
