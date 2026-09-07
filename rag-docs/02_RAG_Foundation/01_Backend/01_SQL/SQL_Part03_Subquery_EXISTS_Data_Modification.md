# SQL Part03 - Subquery, EXISTS, Data Modification

---

# 1. Subquery Foundation

## 1.1 Subquery Purpose

### [개념]

Subquery는 SQL 내부에 포함된 또 다른 SELECT Query다.

Subquery는 다른 Query의 결과를 조건, 값, Table처럼 사용하기 위한 SQL 구조다.

Backend Agent는 Subquery를 사용할 때 Query Purpose, 결과 Cardinality, JOIN 대체 가능성, 성능 영향을 함께 검토해야 한다.

---

### [핵심]

Subquery 사용 목적:

- 값 비교
- 목록 조건
- 존재 여부 확인
- 집계 결과 조건
- Derived Table 생성
- Filtering 보조
- Permission Check
- Duplicate Check
- Related Data Check

Subquery 유형:

- Scalar Subquery
- IN Subquery
- EXISTS Subquery
- Correlated Subquery
- Derived Table
- Inline View

---

### [실무]

2026 Backend 실무 기준에서 Subquery는 아래 상황에서 자주 사용한다.

```text
Requirement
→ Query Purpose 확인
→ Main Table 확인
→ 조건에 필요한 보조 Query 확인
→ Subquery / JOIN / EXISTS 중 선택
→ Index 가능성 검토
→ Repository / QueryDSL 변환 가능성 검토
```

예시:

```text
"사용자가 찜한 축제 목록"
→ Main Table: festivals
→ Subquery Table: favorites
→ favorites에 user_id 조건
→ festival_id 목록 기준 필터링
```

SQL 예시:

```sql
SELECT festival_id, title
FROM festivals
WHERE festival_id IN (
  SELECT festival_id
  FROM favorites
  WHERE user_id = 1
);
```

---

### [FAQ]

Q. Subquery는 언제 사용해?
A. 다른 조회 결과를 조건, 값, 목록, 존재 여부 판단에 사용해야 할 때 사용한다.

Q. Subquery는 JOIN보다 항상 느려?
A. 아니다. DBMS Optimizer와 Query 구조에 따라 다르며 목적과 실행 계획 기준으로 판단해야 한다.

Q. Subquery를 쓰기 전에 무엇을 확인해야 해?
A. Subquery 결과가 단건인지 목록인지 존재 여부인지 먼저 확인해야 한다.

Q. Backend Agent는 Subquery를 어떻게 판단해야 해?
A. Query Purpose, Table Relationship, Index 가능성, JOIN 대체 가능성, Repository 구현 가능성을 함께 검토해야 한다.

---

## 1.2 Scalar Subquery

### [개념]

Scalar Subquery는 하나의 값만 반환하는 Subquery다.

SELECT, WHERE, HAVING 절에서 단일 값 비교나 계산 결과로 사용할 수 있다.

Scalar Subquery는 반드시 단일 Row, 단일 Column 결과를 반환해야 한다.

---

### [핵심]

Scalar Subquery 특징:

- 단일 값 반환
- Single Row
- Single Column
- 비교 조건에 사용
- 집계 결과 조건에 사용
- 결과가 여러 Row면 오류 가능
- 반복 실행 비용 주의

사용 상황:

- 평균보다 큰 값 조회
- 최대값 기준 조회
- 특정 사용자 통계 조회
- 전체 집계 기준 비교

---

### [실무]

평균 평점보다 높은 리뷰 조회:

```sql
SELECT review_id, festival_id, rating
FROM reviews
WHERE rating > (
  SELECT AVG(rating)
  FROM reviews
);
```

특정 축제의 평균 평점과 함께 조회:

```sql
SELECT f.festival_id,
       f.title,
       (
         SELECT AVG(r.rating)
         FROM reviews r
         WHERE r.festival_id = f.festival_id
       ) AS average_rating
FROM festivals f;
```

주의:

- Scalar Subquery는 결과가 2개 이상이면 오류 가능
- Row마다 반복 실행되는 Correlated Scalar Subquery는 성능 주의
- 목록 조회에서 반복 계산이 많으면 JOIN + GROUP BY 또는 Derived Table 검토
- 집계 결과 NULL 가능성 처리

---

### [FAQ]

Q. Scalar Subquery는 뭐야?
A. 하나의 값만 반환하는 Subquery다.

Q. Scalar Subquery 결과가 여러 Row면 어떻게 돼?
A. 단일 값이 필요한 위치에서 여러 Row가 반환되면 오류가 발생할 수 있다.

Q. SELECT 절 Scalar Subquery는 성능상 안전해?
A. Row마다 반복 실행될 수 있어 대량 목록에서는 Derived Table이나 JOIN 집계를 검토해야 한다.

Q. 평균보다 큰 값을 조회할 때 Scalar Subquery를 쓸 수 있어?
A. 가능하다. AVG 같은 집계 결과를 단일 값으로 반환해 비교 조건에 사용할 수 있다.

---

## 1.3 IN Subquery

### [개념]

IN Subquery는 특정 값이 Subquery 결과 목록에 포함되는지 확인하는 조건이다.

단순 목록 필터링에 사용하기 쉽지만 Subquery 결과 크기, NULL 포함 여부, Index 사용 가능성을 검토해야 한다.

---

### [핵심]

IN Subquery 특징:

- 목록 포함 여부 확인
- 단일 Column 목록 반환
- 작은 결과 집합에 직관적
- NULL 포함 시 NOT IN 주의
- JOIN 또는 EXISTS로 대체 가능
- Permission / Filter 조건에 자주 사용

사용 상황:

- 특정 사용자가 찜한 축제
- 특정 카테고리에 속한 게시글
- 특정 권한을 가진 사용자
- 조건에 맞는 ID 목록 필터링

---

### [실무]

사용자가 찜한 축제 목록:

```sql
SELECT festival_id, title
FROM festivals
WHERE festival_id IN (
  SELECT festival_id
  FROM favorites
  WHERE user_id = 1
);
```

특정 상태 주문을 가진 사용자 조회:

```sql
SELECT user_id, email
FROM users
WHERE user_id IN (
  SELECT user_id
  FROM orders
  WHERE order_status = 'PAID'
);
```

권장:

- Subquery 반환 Column은 1개로 제한
- IN 목록이 커지는 경우 EXISTS 또는 JOIN 검토
- Subquery 조건 Column Index 검토
- NOT IN 사용 시 NULL 가능성 확인
- Query Purpose가 존재 여부라면 EXISTS 검토

주의:

```sql
-- NULL 포함 시 예상과 다른 결과 가능
SELECT user_id
FROM users
WHERE user_id NOT IN (
  SELECT user_id
  FROM banned_users
);
```

---

### [FAQ]

Q. IN Subquery는 언제 사용해?
A. 특정 값이 Subquery 결과 목록에 포함되는지 확인할 때 사용한다.

Q. IN Subquery는 어떤 결과를 반환해야 해?
A. 비교 대상과 같은 의미의 단일 Column 목록을 반환해야 한다.

Q. IN과 EXISTS 중 뭐가 좋아?
A. 값 목록 포함 여부는 IN, 관련 Row 존재 여부는 EXISTS가 더 명확한 경우가 많다.

Q. NOT IN은 왜 조심해야 해?
A. Subquery 결과에 NULL이 포함되면 비교 결과가 UNKNOWN이 되어 예상과 다른 결과가 나올 수 있다.

---

## 1.4 Derived Table

### [개념]

Derived Table은 FROM 절에서 Subquery 결과를 임시 Table처럼 사용하는 방식이다.

복잡한 집계 결과, 중간 계산 결과, 사전 필터링 결과를 Main Query와 JOIN할 때 사용한다.

---

### [핵심]

Derived Table 특징:

- FROM 절 Subquery
- Inline View
- 반드시 Alias 필요
- 집계 결과 JOIN에 유용
- 중간 결과 분리
- Query 가독성 개선
- DBMS별 최적화 차이 가능

사용 상황:

- 축제별 리뷰 수 집계 후 JOIN
- 사용자별 주문 합계 계산
- 월별 통계 결과 조회
- 여러 1:N 집계 분리
- Pagination 대상 선조회

---

### [실무]

축제별 리뷰 수 Derived Table:

```sql
SELECT f.festival_id,
       f.title,
       COALESCE(rc.review_count, 0) AS review_count
FROM festivals f
LEFT JOIN (
  SELECT festival_id, COUNT(*) AS review_count
  FROM reviews
  GROUP BY festival_id
) rc ON f.festival_id = rc.festival_id;
```

사용자별 주문 합계:

```sql
SELECT u.user_id,
       u.email,
       COALESCE(os.total_amount, 0) AS total_amount
FROM users u
LEFT JOIN (
  SELECT user_id, SUM(amount) AS total_amount
  FROM orders
  WHERE order_status = 'PAID'
  GROUP BY user_id
) os ON u.user_id = os.user_id;
```

권장:

- Derived Table에는 명확한 Alias 부여
- Derived Table 내부 GROUP BY 기준 명확화
- 여러 1:N 집계를 각각 분리
- JOIN 대상 Column Index 검토
- 복잡해지면 CTE 또는 View 검토

---

### [FAQ]

Q. Derived Table은 뭐야?
A. FROM 절에서 Subquery 결과를 임시 Table처럼 사용하는 방식이다.

Q. Derived Table에는 Alias가 필요해?
A. 필요하다. FROM 절 Subquery는 Alias를 지정해야 한다.

Q. Derived Table은 언제 유용해?
A. 집계 결과를 Main Table과 JOIN하거나 중간 결과를 분리해 Query를 명확히 만들 때 유용하다.

Q. 여러 1:N Table 집계는 어떻게 처리해?
A. 각 Table을 Derived Table로 먼저 집계한 뒤 Main Table에 JOIN하면 집계 왜곡을 줄일 수 있다.

---

# 2. EXISTS Foundation

## 2.1 EXISTS Purpose

### [개념]

EXISTS는 Subquery 결과가 하나라도 존재하는지 확인하는 조건이다.

EXISTS는 관련 Row 존재 여부를 판단하는 데 적합하며 실제 Column 값을 가져오는 것이 목적이 아니다.

---

### [핵심]

EXISTS 특징:

- 존재 여부 확인
- TRUE / FALSE 판단
- Correlated Subquery와 자주 사용
- SELECT 1 관례
- 관련 Row 존재 확인에 적합
- JOIN 중복 Row 회피 가능
- Permission / Duplicate Check에 유용

사용 상황:

- 리뷰가 있는 축제 조회
- 찜 여부 확인
- 중복 이메일 존재 확인
- 권한 Row 존재 확인
- 신청 이력 존재 확인
- 결제 이력 존재 확인

---

### [실무]

리뷰가 있는 축제 조회:

```sql
SELECT f.festival_id, f.title
FROM festivals f
WHERE EXISTS (
  SELECT 1
  FROM reviews r
  WHERE r.festival_id = f.festival_id
);
```

사용자가 찜한 축제 여부:

```sql
SELECT f.festival_id, f.title
FROM festivals f
WHERE EXISTS (
  SELECT 1
  FROM favorites fav
  WHERE fav.festival_id = f.festival_id
    AND fav.user_id = 1
);
```

권장:

- 존재 여부가 목적이면 EXISTS 우선 검토
- Subquery 내부는 SELECT 1 사용 가능
- Correlated Column에 Index 검토
- JOIN으로 인한 중복 Row를 피하고 싶을 때 검토
- NOT EXISTS는 미존재 조건에 적합

---

### [FAQ]

Q. EXISTS는 언제 사용해?
A. 관련 Row가 존재하는지만 확인하면 될 때 사용한다.

Q. EXISTS는 SELECT 1을 쓰는 이유가 뭐야?
A. 존재 여부만 확인하므로 실제 Column 값이 중요하지 않기 때문이다.

Q. EXISTS는 JOIN보다 어떤 점이 좋아?
A. 관련 Row 존재 여부만 필요할 때 JOIN으로 인한 중복 Row를 피할 수 있다.

Q. EXISTS Subquery는 Main Query와 어떻게 연결돼?
A. 보통 Subquery 내부에서 Main Query의 Column을 참조하는 Correlated Subquery 형태로 연결된다.

---

## 2.2 NOT EXISTS

### [개념]

NOT EXISTS는 Subquery 결과가 존재하지 않는 Row를 찾는 조건이다.

미신청 사용자, 리뷰가 없는 축제, 찜하지 않은 항목처럼 관련 Row가 없는 대상을 조회할 때 사용한다.

---

### [핵심]

NOT EXISTS 특징:

- 미존재 조건
- Anti Join Pattern
- NULL에 비교적 안전
- NOT IN 대체 가능
- 중복 방지 검토에 유용
- 누락 데이터 조회에 적합

사용 상황:

- 리뷰가 없는 축제
- 주문하지 않은 사용자
- 찜하지 않은 축제
- 중복 신청이 없는 사용자
- 알림이 아직 생성되지 않은 대상

---

### [실무]

리뷰가 없는 축제 조회:

```sql
SELECT f.festival_id, f.title
FROM festivals f
WHERE NOT EXISTS (
  SELECT 1
  FROM reviews r
  WHERE r.festival_id = f.festival_id
);
```

특정 사용자가 아직 찜하지 않은 축제:

```sql
SELECT f.festival_id, f.title
FROM festivals f
WHERE NOT EXISTS (
  SELECT 1
  FROM favorites fav
  WHERE fav.festival_id = f.festival_id
    AND fav.user_id = 1
);
```

중복 알림 생성 방지 대상 조회:

```sql
SELECT f.festival_id, f.title
FROM festivals f
WHERE NOT EXISTS (
  SELECT 1
  FROM notifications n
  WHERE n.reference_type = 'FESTIVAL'
    AND n.reference_id = f.festival_id
    AND n.notification_type = 'START_REMINDER'
);
```

권장:

- 미존재 조건은 NOT EXISTS 우선 검토
- NOT IN의 NULL 문제를 피하고 싶을 때 사용
- 중복 생성 방지는 DB Unique Constraint와 함께 검토
- Correlated Column Index 확인
- Application 검증만으로 중복 방지하지 않음

---

### [FAQ]

Q. NOT EXISTS는 언제 사용해?
A. 관련 Row가 존재하지 않는 대상을 조회할 때 사용한다.

Q. NOT EXISTS와 NOT IN 중 뭐가 안전해?
A. NULL 영향 측면에서는 NOT EXISTS가 더 명확하고 안전한 경우가 많다.

Q. 중복 신청 방지에 NOT EXISTS만 쓰면 충분해?
A. 아니다. 동시성 상황에서는 Unique Constraint와 Transaction도 함께 고려해야 한다.

Q. 리뷰가 없는 축제는 어떻게 조회해?
A. festivals를 기준으로 reviews에 대한 NOT EXISTS 조건을 사용하면 된다.

---

## 2.3 EXISTS vs IN

### [개념]

EXISTS는 Subquery 결과의 존재 여부를 확인한다.

IN은 특정 값이 Subquery 결과 목록에 포함되는지 확인한다.

두 방식은 비슷한 결과를 만들 수 있지만 Query Purpose와 NULL 처리, 성능 특성이 다를 수 있다.

---

### [핵심]

비교:

| 비교      | EXISTS             | IN                   |
| --------- | ------------------ | -------------------- |
| 기준      | 존재 여부          | 값 포함 여부         |
| 반환 의미 | TRUE / FALSE       | 목록 비교            |
| Subquery  | 관련 Row 확인      | 값 목록 반환         |
| NULL 영향 | 상대적으로 안전    | NOT IN에서 NULL 주의 |
| 사용 예   | 리뷰 존재 축제     | 특정 ID 목록 포함    |
| 중복 Row  | 영향 적음          | 목록 중복 가능       |
| 목적      | Related Row Exists | Value In List        |

---

### [실무]

EXISTS 예시:

```sql
SELECT f.festival_id, f.title
FROM festivals f
WHERE EXISTS (
  SELECT 1
  FROM reviews r
  WHERE r.festival_id = f.festival_id
);
```

IN 예시:

```sql
SELECT festival_id, title
FROM festivals
WHERE festival_id IN (
  SELECT festival_id
  FROM reviews
);
```

선택 Flow:

```text
관련 Row 존재 여부만 필요한가?
→ EXISTS

Subquery 결과 목록에 값이 포함되는지 비교하는가?
→ IN

미존재 조건인가?
→ NOT EXISTS 우선 검토

Subquery 결과에 NULL 가능성이 있는가?
→ NOT IN 주의, NOT EXISTS 검토
```

---

### [FAQ]

Q. EXISTS와 IN 차이는?
A. EXISTS는 관련 Row 존재 여부를 확인하고 IN은 값이 목록에 포함되는지 확인한다.

Q. 존재 여부 확인에는 무엇이 더 명확해?
A. EXISTS가 더 명확한 경우가 많다.

Q. 값 목록 비교에는 무엇이 더 직관적이야?
A. IN이 더 직관적인 경우가 많다.

Q. NOT IN보다 NOT EXISTS를 권장하는 이유는?
A. NOT IN은 NULL 포함 시 예상과 다른 결과가 나올 수 있기 때문이다.

---

# 3. Correlated Subquery

## 3.1 Correlated Subquery Purpose

### [개념]

Correlated Subquery는 Subquery가 Main Query의 Column을 참조하는 Subquery다.

Main Query의 각 Row마다 Subquery 조건이 달라질 수 있다.

---

### [핵심]

Correlated Subquery 특징:

- Main Query Column 참조
- Row별 조건 평가
- EXISTS와 자주 사용
- 반복 실행 비용 가능
- Index 중요
- JOIN 또는 Derived Table로 대체 가능

사용 상황:

- Row별 존재 여부 확인
- Row별 집계 결과 계산
- Row별 최신 데이터 조회
- 중복 여부 확인
- 권한 여부 확인

---

### [실무]

축제별 리뷰 존재 여부:

```sql
SELECT f.festival_id, f.title
FROM festivals f
WHERE EXISTS (
  SELECT 1
  FROM reviews r
  WHERE r.festival_id = f.festival_id
);
```

축제별 평균 평점 조회:

```sql
SELECT f.festival_id,
       f.title,
       (
         SELECT AVG(r.rating)
         FROM reviews r
         WHERE r.festival_id = f.festival_id
       ) AS average_rating
FROM festivals f;
```

주의:

- Main Query Row 수가 많으면 반복 평가 비용 증가 가능
- Subquery 조건 Column에 Index 필요
- SELECT 절 Correlated Subquery는 대량 목록에서 주의
- 집계 목적이면 Derived Table + JOIN 검토
- 존재 목적이면 EXISTS 적합

---

### [FAQ]

Q. Correlated Subquery는 뭐야?
A. Subquery가 Main Query의 Column을 참조하는 Subquery다.

Q. Correlated Subquery는 왜 성능 주의가 필요해?
A. Main Query의 Row마다 Subquery가 평가될 수 있기 때문이다.

Q. Correlated Subquery는 언제 많이 사용해?
A. EXISTS를 이용한 관련 Row 존재 여부 확인에서 자주 사용한다.

Q. Correlated Subquery를 줄이는 방법은?
A. JOIN, Derived Table, GROUP BY 집계로 변경 가능한지 검토한다.

---

## 3.2 Subquery Performance Review

### [개념]

Subquery Performance Review는 Subquery가 Query 성능에 미치는 영향을 검토하는 과정이다.

Subquery는 표현력이 좋지만 결과 크기, 반복 실행, Index 미사용, Derived Table Materialization 등으로 성능 문제가 발생할 수 있다.

---

### [핵심]

검토 대상:

- Subquery Result Size
- Correlated Subquery 여부
- Index 사용 가능성
- IN 목록 크기
- EXISTS 조건 Column
- Derived Table 크기
- Aggregation 비용
- Execution Plan
- Query Rewrite 가능성

위험 패턴:

- 대량 IN Subquery
- SELECT 절 반복 Scalar Subquery
- Index 없는 Correlated Subquery
- 불필요한 Subquery 중첩
- Subquery 내부 SELECT \*
- 집계 Subquery 과다 사용

---

### [실무]

검토 Flow:

```text
Subquery 목적 확인
→ 단건 / 목록 / 존재 / 집계 구분
→ Subquery 결과 Row 수 예상
→ Correlated 여부 확인
→ 조건 Column Index 확인
→ JOIN / EXISTS / Derived Table 대체 검토
→ Execution Plan 확인
```

개선 예시:

```sql
-- 반복 Scalar Subquery
SELECT f.festival_id,
       f.title,
       (
         SELECT COUNT(*)
         FROM reviews r
         WHERE r.festival_id = f.festival_id
       ) AS review_count
FROM festivals f;
```

```sql
-- Derived Table로 집계 분리
SELECT f.festival_id,
       f.title,
       COALESCE(rc.review_count, 0) AS review_count
FROM festivals f
LEFT JOIN (
  SELECT festival_id, COUNT(*) AS review_count
  FROM reviews
  GROUP BY festival_id
) rc ON f.festival_id = rc.festival_id;
```

---

### [FAQ]

Q. Subquery가 느릴 때 무엇을 확인해?
A. Subquery 결과 크기, Correlated 여부, Index, 실행 계획, JOIN 대체 가능성을 확인한다.

Q. SELECT 절 Subquery는 왜 주의해야 해?
A. Main Query Row마다 반복 계산될 수 있어 대량 목록에서 성능 문제가 생길 수 있다.

Q. Subquery 내부에서 SELECT \*를 써도 돼?
A. 권장하지 않는다. EXISTS는 SELECT 1, 목록 비교는 필요한 Column만 선택하는 것이 좋다.

Q. Subquery 성능은 어떻게 판단해?
A. 추측보다 Execution Plan과 실제 데이터 양을 기준으로 판단해야 한다.

---

# 4. Data Modification Foundation

## 4.1 Data Modification Purpose

### [개념]

Data Modification은 Table의 데이터를 생성, 수정, 삭제하는 SQL 작업이다.

대표 명령은 INSERT, UPDATE, DELETE다.

Data Modification Query는 조회 Query보다 영향 범위, Constraint, Transaction, Rollback 가능성을 더 엄격히 검토해야 한다.

---

### [핵심]

Data Modification 명령:

- INSERT
- UPDATE
- DELETE

검토 기준:

- Query Purpose
- Target Table
- Required Column
- Constraint
- Unique Constraint
- Foreign Key
- Not Null
- Default Value
- WHERE Condition
- Affected Row
- Transaction
- Rollback
- Audit Column
- Soft Delete

---

### [실무]

Data Modification Flow:

```text
Requirement
→ 생성 / 수정 / 삭제 구분
→ Target Table 확인
→ Constraint 확인
→ 영향 Row 확인
→ Transaction 필요 여부 확인
→ 실행 전 SELECT 검토
→ INSERT / UPDATE / DELETE 실행
→ 결과 검증
```

Backend Service 예시:

```text
리뷰 작성
→ INSERT reviews
→ users / festivals FK 존재 확인
→ rating Check Constraint 확인
→ created_at 설정

프로필 수정
→ UPDATE users
→ user_id WHERE 조건
→ updated_at 설정

찜 취소
→ DELETE favorites
→ user_id + festival_id WHERE 조건
→ 영향 Row 수 확인
```

---

### [FAQ]

Q. Data Modification Query는 무엇을 말해?
A. INSERT, UPDATE, DELETE처럼 Table 데이터를 변경하는 Query를 말한다.

Q. 변경 Query에서 가장 중요한 것은?
A. 영향 범위, WHERE 조건, Constraint, Transaction 필요 여부를 확인하는 것이다.

Q. 변경 Query 실행 전 무엇을 확인해야 해?
A. SELECT로 대상 Row를 확인하고 영향 Row 수와 Rollback 가능성을 검토해야 한다.

Q. Backend Service에서 변경 Query는 어디와 연결돼?
A. Validation, Entity State 변경, Repository save/delete, Transaction, Exception Handling과 연결된다.

---

## 4.2 INSERT Rules

### [개념]

INSERT는 Table에 새로운 Row를 추가하는 SQL 명령이다.

INSERT는 Required Column, Default Value, Not Null, Unique, Foreign Key, Generated Key를 확인해야 한다.

---

### [핵심]

INSERT 검토 대상:

- Target Table
- Column List
- Required Column
- Not Null
- Default Value
- Unique Constraint
- Foreign Key
- Generated Key
- Created At
- Audit Column

권장:

- Column 목록 명시
- 필수 값 누락 방지
- FK 대상 존재 확인
- Unique 중복 가능성 확인
- Default Value 기준 통일
- Application 생성값과 DB 생성값 기준 통일

---

### [실무]

기본 INSERT:

```sql
INSERT INTO users (email, nickname, role, created_at)
VALUES ('user@example.com', 'tester', 'ROLE_USER', NOW());
```

리뷰 작성:

```sql
INSERT INTO reviews (user_id, festival_id, rating, content, created_at)
VALUES (1, 10, 5, '좋은 축제였습니다.', NOW());
```

찜 등록:

```sql
INSERT INTO favorites (user_id, festival_id, created_at)
VALUES (1, 10, NOW());
```

주의:

- Column 목록 생략 지양
- Unique 중복 시 오류 발생 가능
- FK 대상이 없으면 오류 발생 가능
- Not Null Column 누락 금지
- created_at / updated_at 생성 기준 통일
- 동시 중복 등록은 Unique Constraint 필요

---

### [FAQ]

Q. INSERT에서 Column 목록을 생략해도 돼?
A. 가능은 하지만 Table 구조 변경에 취약하므로 실무 예제에서는 Column 목록을 명시하는 것이 좋다.

Q. INSERT 전에 중복 확인이 필요해?
A. email, user-festival favorite처럼 Unique 제약이 있는 값은 중복 가능성을 고려해야 한다.

Q. Foreign Key 대상이 없으면 INSERT가 돼?
A. FK 제약이 있으면 참조 대상 Row가 없을 때 INSERT가 실패한다.

Q. created_at은 SQL에서 넣어야 해, Application에서 넣어야 해?
A. 프로젝트 기준을 통일해야 한다. DB Default 또는 Application @PrePersist 중 하나로 일관되게 관리한다.

---

## 4.3 UPDATE Rules

### [개념]

UPDATE는 기존 Row의 Column 값을 수정하는 SQL 명령이다.

UPDATE는 WHERE 조건을 통해 수정 대상 Row를 명확히 제한해야 한다.

---

### [핵심]

UPDATE 검토 대상:

- Target Table
- SET Column
- WHERE Condition
- Affected Row
- Updated At
- Optimistic Lock
- Constraint
- Business Rule
- Transaction
- Rollback 가능성

필수 기준:

- WHERE 조건 확인
- 수정 대상 SELECT로 사전 확인
- 수정 Column 최소화
- updated_at 갱신 기준 통일
- 영향 Row 수 확인
- 운영 환경 전체 UPDATE 금지

---

### [실무]

안전한 UPDATE:

```sql
UPDATE users
SET nickname = 'newNickname',
    updated_at = NOW()
WHERE user_id = 1;
```

상태 변경:

```sql
UPDATE donations
SET donation_status = 'COMPLETED',
    updated_at = NOW()
WHERE donation_id = 100
  AND donation_status = 'READY';
```

위험한 UPDATE:

```sql
UPDATE users
SET role = 'ROLE_ADMIN';
```

실행 전 확인:

```sql
SELECT user_id, email, role
FROM users
WHERE user_id = 1;
```

권장:

- WHERE 없는 UPDATE 금지
- PK / Unique 조건으로 대상 제한
- 상태 변경은 현재 상태 조건 포함
- 동시성 필요 시 version Column 또는 Lock 검토
- 여러 Table 변경은 Transaction 적용

---

### [FAQ]

Q. UPDATE에서 가장 위험한 실수는?
A. WHERE 조건을 누락해 전체 Row를 수정하는 것이다.

Q. UPDATE 전에 SELECT를 해야 하는 이유는?
A. 수정 대상 Row와 영향 범위를 사전에 확인하기 위해서다.

Q. 상태 변경 UPDATE는 무엇을 주의해야 해?
A. 현재 상태 조건을 WHERE에 포함해 잘못된 상태 전이를 방지해야 한다.

Q. updated_at은 UPDATE마다 갱신해야 해?
A. 변경 이력 추적이 필요하면 updated_at 갱신 기준을 프로젝트 전체에서 통일해야 한다.

---

## 4.4 DELETE Rules

### [개념]

DELETE는 Table에서 Row를 삭제하는 SQL 명령이다.

DELETE는 데이터 복구 가능성, FK 영향, Soft Delete 여부, WHERE 조건을 반드시 검토해야 한다.

---

### [핵심]

DELETE 검토 대상:

- Target Table
- WHERE Condition
- Affected Row
- Foreign Key Impact
- Cascade Delete
- Soft Delete
- Audit Requirement
- Transaction
- Rollback 가능성

삭제 방식:

- Physical Delete
- Soft Delete
- Cascade Delete
- Orphan Removal
- Archive

---

### [실무]

안전한 DELETE:

```sql
DELETE FROM favorites
WHERE user_id = 1
  AND festival_id = 10;
```

위험한 DELETE:

```sql
DELETE FROM users;
```

Soft Delete 예시:

```sql
UPDATE posts
SET deleted_at = NOW(),
    updated_at = NOW()
WHERE post_id = 100;
```

권장:

- WHERE 없는 DELETE 금지
- 운영 데이터는 Soft Delete 우선 검토
- FK 참조 데이터 영향 확인
- 삭제 전 SELECT로 대상 확인
- Cascade Delete는 영향 범위 명확히 확인
- 여러 Table 삭제는 Transaction 적용

---

### [FAQ]

Q. DELETE에서 가장 위험한 실수는?
A. WHERE 조건을 누락해 전체 Row를 삭제하는 것이다.

Q. 삭제는 항상 DELETE로 처리해?
A. 아니다. 복구와 이력 관리가 필요하면 deleted_at이나 active 같은 Column을 사용하는 Soft Delete를 검토한다.

Q. FK가 걸린 Row를 삭제하면 어떻게 돼?
A. 참조 중인 데이터가 있으면 삭제가 실패하거나 Cascade 설정에 따라 관련 데이터가 함께 삭제될 수 있다.

Q. 삭제 전 SELECT를 하는 이유는?
A. 삭제 대상과 영향 Row 수를 확인해 실수를 방지하기 위해서다.

---

# 5. Safe Modification Pattern

## 5.1 WHERE Safety Rules

### [개념]

WHERE Safety Rules는 UPDATE와 DELETE에서 영향 범위를 제한하기 위한 안전 기준이다.

변경 Query에서 WHERE 조건 누락은 운영 데이터 전체 손상으로 이어질 수 있는 치명적 문제다.

---

### [핵심]

필수 확인:

- WHERE 존재 여부
- PK 조건
- Unique 조건
- Composite Key 조건
- User Scope 조건
- Tenant Scope 조건
- Status 조건
- Date Range 조건
- Affected Row Count

위험 패턴:

- UPDATE without WHERE
- DELETE without WHERE
- Broad Range Condition
- 잘못된 User Scope
- Status 조건 누락
- Multi Tenant 조건 누락

---

### [실무]

복합 조건 DELETE:

```sql
DELETE FROM favorites
WHERE user_id = 1
  AND festival_id = 10;
```

상태 조건 UPDATE:

```sql
UPDATE donation_payments
SET payment_status = 'CANCELED',
    updated_at = NOW()
WHERE payment_id = 100
  AND payment_status = 'READY';
```

권한 범위 조건:

```sql
UPDATE posts
SET title = 'updated title',
    updated_at = NOW()
WHERE post_id = 10
  AND user_id = 1;
```

검수 Flow:

```text
Target Row 정의
→ WHERE 조건 확인
→ User Scope 확인
→ Status 조건 확인
→ SELECT로 대상 확인
→ UPDATE / DELETE 실행
→ Affected Row 확인
```

---

### [FAQ]

Q. 변경 Query에서 WHERE가 왜 가장 중요해?
A. WHERE가 없으면 전체 Row가 수정되거나 삭제될 수 있기 때문이다.

Q. user_id 조건은 왜 같이 넣어?
A. 사용자가 소유한 데이터만 변경하도록 권한 범위를 제한하기 위해서다.

Q. 상태 조건은 왜 WHERE에 포함해?
A. 이미 처리된 데이터가 다시 변경되는 잘못된 상태 전이를 막기 위해서다.

Q. Affected Row Count는 왜 확인해?
A. 실제로 의도한 Row만 변경되었는지 검증하기 위해서다.

---

## 5.2 Soft Delete Pattern

### [개념]

Soft Delete는 Row를 실제로 삭제하지 않고 삭제 상태를 표시하는 방식이다.

일반적으로 deleted_at, active, deleted, status Column을 사용한다.

---

### [핵심]

Soft Delete Column:

- deleted_at
- active
- deleted
- status
- updated_at
- deleted_by

Soft Delete 장점:

- 복구 가능
- 이력 유지
- 참조 무결성 유지
- 감사 로그 대응
- 운영 실수 완화

Soft Delete 주의:

- 모든 조회에 삭제 제외 조건 필요
- Unique Constraint 설계 복잡
- 데이터 증가
- Index 설계 필요
- Hard Delete 정책 별도 필요

---

### [실무]

Soft Delete 처리:

```sql
UPDATE reviews
SET deleted_at = NOW(),
    updated_at = NOW()
WHERE review_id = 100
  AND user_id = 1;
```

Soft Delete 조회 제외:

```sql
SELECT review_id, content, rating
FROM reviews
WHERE festival_id = 10
  AND deleted_at IS NULL
ORDER BY created_at DESC;
```

active Column 방식:

```sql
UPDATE festivals
SET active = false,
    updated_at = NOW()
WHERE festival_id = 10;
```

권장:

- 프로젝트 전체 Soft Delete 기준 통일
- Repository 기본 조회 조건에 삭제 제외 포함
- 관리자 조회는 삭제 데이터 포함 여부 명확화
- Unique Constraint와 Soft Delete 충돌 검토
- deleted_at Index 검토

---

### [FAQ]

Q. Soft Delete는 뭐야?
A. Row를 실제 삭제하지 않고 deleted_at, active 같은 Column으로 삭제 상태를 표시하는 방식이다.

Q. Soft Delete를 쓰면 조회 Query는 어떻게 해야 해?
A. 일반 조회에는 deleted_at IS NULL 또는 active = true 조건을 포함해야 한다.

Q. Soft Delete의 단점은 뭐야?
A. 조회 조건 누락 위험, 데이터 증가, Unique Constraint 설계 복잡도가 있다.

Q. 모든 삭제를 Soft Delete로 해야 해?
A. 아니다. 비즈니스 이력과 복구 필요성이 있는 데이터는 Soft Delete를 검토하고 단순 관계 데이터는 Physical Delete도 가능하다.

---

## 5.3 Duplicate Prevention Pattern

### [개념]

Duplicate Prevention Pattern은 중복 데이터 생성을 방지하기 위한 SQL 및 DB Constraint 설계 기준이다.

Application 중복 체크만으로는 동시 요청 상황에서 중복을 완전히 막기 어렵다.

---

### [핵심]

중복 방지 수단:

- Unique Constraint
- Composite Unique Constraint
- EXISTS Check
- INSERT 실패 처리
- Transaction
- Lock
- Upsert
- Idempotency Key

중복 위험 상황:

- 회원 이메일 가입
- 사용자-축제 찜
- 좋아요 중복
- 선착순 신청
- 쿠폰 발급
- 결제 요청
- 알림 중복 생성

---

### [실무]

Composite Unique Constraint 예시:

```sql
CREATE TABLE favorites (
  favorite_id BIGINT PRIMARY KEY,
  user_id BIGINT NOT NULL,
  festival_id BIGINT NOT NULL,
  created_at DATETIME NOT NULL,
  UNIQUE (user_id, festival_id)
);
```

중복 확인:

```sql
SELECT 1
FROM favorites
WHERE user_id = 1
  AND festival_id = 10;
```

중복 방지 INSERT:

```sql
INSERT INTO favorites (user_id, festival_id, created_at)
VALUES (1, 10, NOW());
```

권장:

- 중요한 중복 방지는 DB Unique Constraint 필수
- Application exists check는 UX와 사전 검증 용도
- 동시 요청은 Constraint 위반 예외 처리
- 중복 요청이 가능한 API는 Idempotency 검토
- 좋아요 / 찜은 user_id + target_id Unique 검토

---

### [FAQ]

Q. Application에서 중복 체크하면 Unique Constraint는 없어도 돼?
A. 아니다. 동시 요청에서는 Application 체크만으로 중복을 막기 어려우므로 DB Unique Constraint가 필요하다.

Q. 사용자별 찜 중복은 어떻게 막아?
A. user_id와 festival_id에 Composite Unique Constraint를 설정하는 것이 좋다.

Q. exists check는 왜 필요한데?
A. 사용자에게 중복 상태를 미리 알려주거나 불필요한 INSERT를 줄이는 데 도움이 된다.

Q. Unique Constraint 위반은 어떻게 처리해?
A. Backend에서 DB 예외를 잡아 중복 요청에 맞는 비즈니스 예외로 변환한다.

---

# 6. Data Modification Review

## 6.1 Modification Review Flow

### [개념]

Modification Review Flow는 INSERT, UPDATE, DELETE Query 실행 전후로 데이터 정합성과 영향 범위를 점검하는 과정이다.

변경 Query는 조회 Query보다 더 엄격한 검수 기준이 필요하다.

---

### [핵심]

Review Flow:

```text
Requirement 확인
→ Target Table 확인
→ 변경 유형 확인
→ Constraint 확인
→ WHERE 조건 확인
→ SELECT로 대상 확인
→ Transaction 필요성 검토
→ 실행
→ Affected Row 확인
→ 결과 검증
```

검토 대상:

- Required Column
- Unique Constraint
- Foreign Key
- Check Constraint
- Not Null
- Default Value
- WHERE Condition
- Soft Delete
- Transaction
- Audit Column

---

### [실무]

UPDATE 검수 예시:

```text
문제: 닉네임 변경

1. users Table 확인
2. user_id 기준 대상 확인
3. nickname 중복 정책 확인
4. UPDATE WHERE user_id 조건 확인
5. updated_at 갱신
6. Affected Row 1 확인
```

DELETE 검수 예시:

```text
문제: 찜 취소

1. favorites Table 확인
2. user_id + festival_id 복합 조건 확인
3. DELETE 대상 SELECT 확인
4. DELETE 실행
5. Affected Row 1 또는 0 허용 정책 확인
```

---

### [FAQ]

Q. 변경 Query 검수는 어디서 시작해?
A. 요구사항과 Target Table, 변경 유형을 확인하는 것에서 시작한다.

Q. 변경 전 SELECT는 필수야?
A. 운영 환경이나 수동 SQL 실행에서는 강하게 권장된다.

Q. Affected Row가 0이면 무조건 오류야?
A. 아니다. 멱등 삭제처럼 0을 허용할 수도 있으므로 API 정책에 따라 판단한다.

Q. 변경 Query는 왜 Transaction과 연결돼?
A. 여러 변경 작업이 하나의 성공 / 실패 단위로 묶여야 데이터 정합성을 보장할 수 있기 때문이다.

---

## 6.2 Common Modification Mistakes

### [개념]

Common Modification Mistakes는 INSERT, UPDATE, DELETE에서 자주 발생하는 실수다.

AI Agent는 변경 Query 생성 시 데이터 손상 가능성이 있는 Anti Pattern을 반드시 감지해야 한다.

---

### [핵심]

자주 발생하는 실수:

- INSERT Column 목록 생략
- Required Column 누락
- Unique 중복 미검토
- FK 대상 존재 여부 미확인
- UPDATE WHERE 누락
- DELETE WHERE 누락
- User Scope 조건 누락
- Status 조건 누락
- Soft Delete 기준 혼용
- Transaction 누락
- Affected Row 미확인
- updated_at 누락
- Application 중복 체크만 의존
- Cascade Delete 영향 미확인

---

### [실무]

위험 예시:

```sql
UPDATE users
SET role = 'ROLE_ADMIN';
```

문제:

```text
WHERE 조건 없음
→ 전체 사용자 권한 변경
→ 치명적 운영 사고
```

위험 예시:

```sql
DELETE FROM reviews;
```

문제:

```text
WHERE 조건 없음
→ 전체 리뷰 삭제
→ 복구 필요
```

위험 예시:

```sql
INSERT INTO favorites (user_id, festival_id, created_at)
VALUES (1, 10, NOW());
```

문제 가능성:

```text
Unique Constraint가 없으면 동시 요청으로 중복 찜 생성 가능
```

---

### [FAQ]

Q. 변경 Query에서 가장 치명적인 실수는?
A. UPDATE 또는 DELETE에서 WHERE 조건을 누락하는 것이다.

Q. INSERT에서 가장 흔한 실수는?
A. 필수 Column 누락, Unique 중복 미검토, FK 대상 미확인이 많다.

Q. Soft Delete 기준을 혼용하면 어떤 문제가 생겨?
A. 어떤 Query는 삭제 데이터를 제외하고 어떤 Query는 포함하여 결과 일관성이 깨질 수 있다.

Q. 중복 방지를 Application에만 맡기면 왜 위험해?
A. 동시 요청에서는 두 요청이 동시에 중복 체크를 통과할 수 있기 때문이다.

---

## 6.3 Checklist

### [개념]

Checklist는 Subquery, EXISTS, Data Modification Query를 최종 검수하기 위한 기준이다.

Agent는 Query 생성 후 Checklist 기준으로 치명적 오류를 탐지해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Subquery Purpose가 명확한가?
- [ ] Subquery 결과가 단건 / 목록 / 존재 여부 중 무엇인지 구분했는가?
- [ ] Scalar Subquery가 단일 값만 반환하는가?
- [ ] IN Subquery 결과 Column이 비교 대상과 일치하는가?
- [ ] NOT IN 사용 시 NULL 가능성을 검토했는가?
- [ ] EXISTS가 존재 여부 목적에 사용되었는가?
- [ ] NOT EXISTS가 미존재 조건에 적합하게 사용되었는가?
- [ ] Correlated Subquery의 반복 실행 비용을 검토했는가?
- [ ] Subquery 조건 Column의 Index를 검토했는가?
- [ ] Derived Table에 Alias가 있는가?
- [ ] Derived Table GROUP BY 기준이 명확한가?
- [ ] INSERT Column 목록을 명시했는가?
- [ ] INSERT Required Column을 모두 포함했는가?
- [ ] Unique Constraint 중복 가능성을 검토했는가?
- [ ] Foreign Key 대상 존재 여부를 검토했는가?
- [ ] UPDATE에 WHERE 조건이 있는가?
- [ ] DELETE에 WHERE 조건이 있는가?
- [ ] 변경 Query에 User Scope 조건이 필요한가?
- [ ] 상태 변경 Query에 현재 상태 조건이 포함되었는가?
- [ ] Soft Delete 기준이 프로젝트 전체에서 통일되었는가?
- [ ] Affected Row Count 확인 기준이 있는가?
- [ ] 여러 변경 작업에 Transaction이 필요한가?
```

---

### [실무]

검수 Flow:

```text
Draft SQL
→ Subquery Purpose Review
→ EXISTS / IN 선택 검토
→ Correlated Cost Review
→ Modification Type Review
→ Constraint Review
→ WHERE Safety Review
→ Transaction Review
→ Final SQL
```

치명적 문제:

- Scalar Subquery 다중 Row 반환
- NOT IN NULL 문제
- Index 없는 Correlated Subquery 남용
- UPDATE WHERE 누락
- DELETE WHERE 누락
- Unique Constraint 누락
- FK 영향 미검토
- Soft Delete 조건 누락
- Transaction 누락

---

### [FAQ]

Q. Part03 Query 검수에서 가장 중요한 것은?
A. Subquery 목적, EXISTS / IN 선택, 변경 Query WHERE 안전성, Constraint, Transaction 필요 여부다.

Q. Subquery 검수에서 가장 중요한 것은?
A. 결과가 단건인지 목록인지 존재 여부인지 명확히 구분하는 것이다.

Q. 변경 Query 검수에서 가장 중요한 것은?
A. WHERE 조건, 영향 Row, Constraint, Transaction, Rollback 가능성을 확인하는 것이다.

Q. 치명적 Data Modification 문제는 뭐야?
A. WHERE 없는 UPDATE / DELETE, 중복 방지 Constraint 누락, FK 영향 미검토, Transaction 누락이 치명적이다.

---

# Retrieval Queries

### [FAQ]

Q. SQL Part03은 무엇을 다뤄?
A. Subquery, EXISTS, IN, NOT EXISTS, Derived Table, INSERT, UPDATE, DELETE, Soft Delete, 중복 방지 기준을 다룬다.

Q. Subquery는 뭐야?
A. SQL 내부에 포함된 또 다른 SELECT Query다.

Q. Subquery는 언제 사용해?
A. 다른 조회 결과를 조건, 값, 목록, 존재 여부 판단에 사용해야 할 때 사용한다.

Q. Scalar Subquery는 뭐야?
A. 하나의 값만 반환하는 Subquery다.

Q. Scalar Subquery 결과가 여러 Row면 어떻게 돼?
A. 단일 값이 필요한 위치에서 여러 Row가 반환되면 오류가 발생할 수 있다.

Q. IN Subquery는 언제 사용해?
A. 특정 값이 Subquery 결과 목록에 포함되는지 확인할 때 사용한다.

Q. IN Subquery는 어떤 결과를 반환해야 해?
A. 비교 대상과 같은 의미의 단일 Column 목록을 반환해야 한다.

Q. NOT IN은 왜 조심해야 해?
A. Subquery 결과에 NULL이 포함되면 비교 결과가 UNKNOWN이 되어 예상과 다른 결과가 나올 수 있다.

Q. Derived Table은 뭐야?
A. FROM 절에서 Subquery 결과를 임시 Table처럼 사용하는 방식이다.

Q. Derived Table에는 Alias가 필요해?
A. 필요하다. FROM 절 Subquery는 Alias를 지정해야 한다.

Q. Derived Table은 언제 유용해?
A. 집계 결과를 Main Table과 JOIN하거나 중간 결과를 분리해 Query를 명확히 만들 때 유용하다.

Q. EXISTS는 뭐야?
A. Subquery 결과가 하나라도 존재하는지 확인하는 조건이다.

Q. EXISTS는 언제 사용해?
A. 관련 Row가 존재하는지만 확인하면 될 때 사용한다.

Q. EXISTS는 SELECT 1을 쓰는 이유가 뭐야?
A. 존재 여부만 확인하므로 실제 Column 값이 중요하지 않기 때문이다.

Q. EXISTS는 JOIN보다 어떤 점이 좋아?
A. 관련 Row 존재 여부만 필요할 때 JOIN으로 인한 중복 Row를 피할 수 있다.

Q. NOT EXISTS는 언제 사용해?
A. 관련 Row가 존재하지 않는 대상을 조회할 때 사용한다.

Q. NOT EXISTS와 NOT IN 중 뭐가 안전해?
A. NULL 영향 측면에서는 NOT EXISTS가 더 명확하고 안전한 경우가 많다.

Q. EXISTS와 IN 차이는?
A. EXISTS는 관련 Row 존재 여부를 확인하고 IN은 값이 목록에 포함되는지 확인한다.

Q. 존재 여부 확인에는 무엇이 더 명확해?
A. EXISTS가 더 명확한 경우가 많다.

Q. 값 목록 비교에는 무엇이 더 직관적이야?
A. IN이 더 직관적인 경우가 많다.

Q. Correlated Subquery는 뭐야?
A. Subquery가 Main Query의 Column을 참조하는 Subquery다.

Q. Correlated Subquery는 왜 성능 주의가 필요해?
A. Main Query의 Row마다 Subquery가 평가될 수 있기 때문이다.

Q. Correlated Subquery는 언제 많이 사용해?
A. EXISTS를 이용한 관련 Row 존재 여부 확인에서 자주 사용한다.

Q. Subquery가 느릴 때 무엇을 확인해?
A. Subquery 결과 크기, Correlated 여부, Index, 실행 계획, JOIN 대체 가능성을 확인한다.

Q. SELECT 절 Subquery는 왜 주의해야 해?
A. Main Query Row마다 반복 계산될 수 있어 대량 목록에서 성능 문제가 생길 수 있다.

Q. Data Modification Query는 무엇을 말해?
A. INSERT, UPDATE, DELETE처럼 Table 데이터를 변경하는 Query를 말한다.

Q. 변경 Query에서 가장 중요한 것은?
A. 영향 범위, WHERE 조건, Constraint, Transaction 필요 여부를 확인하는 것이다.

Q. INSERT는 언제 사용해?
A. Table에 새로운 Row를 추가할 때 사용한다.

Q. INSERT에서 Column 목록을 생략해도 돼?
A. 가능은 하지만 Table 구조 변경에 취약하므로 실무 예제에서는 Column 목록을 명시하는 것이 좋다.

Q. INSERT 전에 중복 확인이 필요해?
A. email, user-festival favorite처럼 Unique 제약이 있는 값은 중복 가능성을 고려해야 한다.

Q. Foreign Key 대상이 없으면 INSERT가 돼?
A. FK 제약이 있으면 참조 대상 Row가 없을 때 INSERT가 실패한다.

Q. UPDATE는 언제 사용해?
A. 기존 Row의 Column 값을 수정할 때 사용한다.

Q. UPDATE에서 가장 위험한 실수는?
A. WHERE 조건을 누락해 전체 Row를 수정하는 것이다.

Q. UPDATE 전에 SELECT를 해야 하는 이유는?
A. 수정 대상 Row와 영향 범위를 사전에 확인하기 위해서다.

Q. 상태 변경 UPDATE는 무엇을 주의해야 해?
A. 현재 상태 조건을 WHERE에 포함해 잘못된 상태 전이를 방지해야 한다.

Q. DELETE는 언제 사용해?
A. Table에서 Row를 삭제할 때 사용한다.

Q. DELETE에서 가장 위험한 실수는?
A. WHERE 조건을 누락해 전체 Row를 삭제하는 것이다.

Q. 삭제는 항상 DELETE로 처리해?
A. 아니다. 복구와 이력 관리가 필요하면 deleted_at이나 active 같은 Column을 사용하는 Soft Delete를 검토한다.

Q. Soft Delete는 뭐야?
A. Row를 실제 삭제하지 않고 deleted_at, active 같은 Column으로 삭제 상태를 표시하는 방식이다.

Q. Soft Delete를 쓰면 조회 Query는 어떻게 해야 해?
A. 일반 조회에는 deleted_at IS NULL 또는 active = true 조건을 포함해야 한다.

Q. Application에서 중복 체크하면 Unique Constraint는 없어도 돼?
A. 아니다. 동시 요청에서는 Application 체크만으로 중복을 막기 어려우므로 DB Unique Constraint가 필요하다.

Q. 사용자별 찜 중복은 어떻게 막아?
A. user_id와 festival_id에 Composite Unique Constraint를 설정하는 것이 좋다.

Q. 변경 Query에서 WHERE가 왜 가장 중요해?
A. WHERE가 없으면 전체 Row가 수정되거나 삭제될 수 있기 때문이다.

Q. user_id 조건은 왜 같이 넣어?
A. 사용자가 소유한 데이터만 변경하도록 권한 범위를 제한하기 위해서다.

Q. Affected Row Count는 왜 확인해?
A. 실제로 의도한 Row만 변경되었는지 검증하기 위해서다.

Q. Part03 Query 검수에서 가장 중요한 것은?
A. Subquery 목적, EXISTS / IN 선택, 변경 Query WHERE 안전성, Constraint, Transaction 필요 여부다.
