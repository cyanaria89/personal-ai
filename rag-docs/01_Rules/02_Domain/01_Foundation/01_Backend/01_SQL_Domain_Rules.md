# SQL Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

SQL Domain Rules 문서는 Backend Agent / Review Agent / PM Agent가 SQL 기반 데이터 조회, 데이터 모델 이해, 쿼리 작성, 성능 검토, 오류 분석을 수행하기 위한 RAG 문서 제작 규칙이다.

이 문서는 SQL 문법 단순 요약이 아니라 AI Agent가 실무 코드 생성과 검토에서 SQL을 올바르게 사용할 수 있도록 지원하는 규칙 문서다.

목적:

- SQL Query 작성 기준 제공
- SELECT / INSERT / UPDATE / DELETE 기본 판단 지원
- JOIN / Subquery / Aggregation 사용 기준 제공
- WHERE / GROUP BY / HAVING / ORDER BY 처리 순서 이해 지원
- Index 기반 성능 판단 지원
- Transaction / Lock / Isolation 기본 개념 지원
- Pagination / Search Query / Filter Query 설계 지원
- SQL Anti Pattern 검출 지원
- Backend Repository / QueryDSL / JPA Native Query 검토 지원
- ERD 기반 데이터 조회 흐름 분석 지원

---

### [핵심]

우선순위:

1. Query Purpose
2. Table Relationship
3. SELECT Query
4. Filtering
5. Join
6. Aggregation
7. Subquery
8. Index
9. Transaction
10. Pagination
11. Search Condition
12. Data Modification
13. Null Handling
14. Performance Review
15. SQL Anti Pattern

---

### [실무]

SQL 문서는 아래 작업을 지원하도록 작성한다.

- 요구사항을 SQL 조회 조건으로 변환
- ERD / Entity 관계를 기준으로 JOIN 설계
- WHERE 조건과 Index 사용 가능성 검토
- GROUP BY / HAVING 기반 통계 쿼리 작성
- 정렬 / 페이징 쿼리 작성
- INSERT / UPDATE / DELETE 영향 범위 검토
- Transaction이 필요한 작업 식별
- N+1 / 불필요한 JOIN / SELECT \* 같은 문제 감지
- JPA / QueryDSL / Native SQL 변환 시 주의점 제공
- 쿼리 성능 개선 방향 제안

---

### [FAQ]

Q. SQL Domain Rules는 SQLD 시험용 문서야?

A.
아니다. 시험용 요약이 아니라 Backend Agent가 실무 쿼리 작성과 검토를 할 수 있도록 만드는 RAG 제작 규칙이다.

Q. SQL 문서에서 가장 중요한 기준은 뭐야?

A.
Query Purpose, Table Relationship, Filtering, Join, Index, Transaction, Performance Review 기준이다.

Q. SQL 문서는 JPA나 QueryDSL과 분리해야 해?

A.
기본 SQL 개념은 분리하되 JPA Repository, JPQL, QueryDSL, Native Query와 연결되는 실무 기준은 포함한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

SQL Domain Rules는 관계형 데이터베이스에서 SQL을 사용해 데이터를 조회, 변경, 집계, 검토하는 데 필요한 Foundation 범위를 포함한다.

포함 범위:

- SQL 기본 구조
- SELECT
- INSERT
- UPDATE
- DELETE
- WHERE
- ORDER BY
- GROUP BY
- HAVING
- JOIN
- INNER JOIN
- LEFT JOIN
- SELF JOIN
- Subquery
- EXISTS
- IN
- Aggregation
- COUNT / SUM / AVG / MIN / MAX
- NULL 처리
- CASE WHEN
- Pagination
- Search Query
- Index Basics
- Execution Plan Basics
- Transaction Basics
- Lock Basics
- Isolation Level Basics
- Constraint Basics
- Primary Key / Foreign Key
- Unique / Not Null
- SQL Performance Basics
- SQL Anti Pattern
- Backend Query Review

---

### [핵심]

반드시 포함:

- SQL 실행 논리 순서
- WHERE와 HAVING 차이
- INNER JOIN과 LEFT JOIN 차이
- JOIN 조건 누락 위험
- NULL 비교 주의
- GROUP BY 사용 기준
- Aggregation 결과 해석
- Subquery와 JOIN 선택 기준
- EXISTS와 IN 차이
- Index 적용 가능 조건
- OFFSET Pagination 한계
- Transaction 적용 기준
- UPDATE / DELETE WHERE 누락 위험
- SELECT \* 지양
- 쿼리 성능 검토 Flow

---

### [실무]

SQL 문서는 Backend 개발 흐름에서 아래 위치에 사용된다.

```text
Requirement
→ ERD / Entity Relationship
→ Query Purpose
→ SQL Query Design
→ Index / Performance Review
→ Repository / QueryDSL / Native Query Mapping
→ Test / Review
```

---

### [FAQ]

Q. SQL Domain Rules에서 DBMS별 문법도 다뤄?

A.
Foundation 문서에서는 표준 SQL과 MySQL 기준 실무 문법을 우선한다. Oracle, PostgreSQL, MariaDB 차이는 필요 시 별도 문서에서 다룬다.

Q. 고급 튜닝도 여기서 다뤄?

A.
아니다. Index와 Execution Plan 기초만 포함하고 고급 튜닝은 Performance Tuning 또는 Database Expert 문서에서 다룬다.

---

## 2.2 Excluded Scope

### [개념]

SQL Domain Rules에서는 DBMS 내부 구조와 고급 운영 튜닝을 제외한다.

제외 범위:

- DBMS Storage Engine 심화
- Query Optimizer 내부 구조 심화
- Partitioning 심화
- Sharding 심화
- Replication 심화
- Backup / Recovery 심화
- HA 구성
- Stored Procedure 심화
- Trigger 심화
- Window Function 심화
- Recursive CTE 심화
- Advanced Lock Tuning
- Advanced Execution Plan Tuning
- NoSQL Query
- OLAP / Data Warehouse 심화

---

### [핵심]

제외 이유:

- Foundation 범위 초과
- Backend Agent의 기본 쿼리 생성 / 검토 목적에 집중
- RAG Retrieval 혼선 방지
- Chunk 품질 유지
- JPA / QueryDSL / Performance Expert 문서와 역할 분리

---

### [실무]

심화 문서는 별도 Domain Rules에서 관리한다.

```text
SQL
→ JPA Advanced
→ QueryDSL Practical
→ Performance Tuning
→ NoSQL
→ Database Expert
```

---

### [FAQ]

Q. Window Function은 SQL 문서에서 다뤄?

A.
기초 언급은 가능하지만 심화 분석 함수는 Advanced SQL 또는 Database Expert 문서에서 다루는 것이 좋다.

Q. Stored Procedure는 포함해?

A.
Foundation 범위에서는 제외한다. 일반 Backend 개발에서는 Application Layer와 Repository 중심 쿼리 설계를 우선한다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

SQL RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

Required:

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

### [핵심]

필수 Section 목적:

- [개념]: SQL 개념과 역할 정의
- [핵심]: 검색 친화 키워드 정리
- [실무]: Backend 개발 기준 적용
- [FAQ]: 사용자 질문 매칭 강화

---

### [실무]

각 문서는 아래 구조를 기본으로 한다.

```md
# Topic

## Sub Topic

### [개념]

### [핵심]

### [실무]

### [FAQ]
```

---

### [FAQ]

Q. SQL 문서에도 FAQ가 필요해?

A.
필요하다. FAQ는 사용자의 자연어 질문과 SQL 개념 Chunk를 연결하는 Retrieval 품질을 높인다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

SQL 문서에는 쿼리 설계와 검증을 위해 추가 Section을 포함할 수 있다.

Strongly Recommended:

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

### [핵심]

추천 Section 사용 기준:

- SQL 실행 순서 → [Flow]
- JOIN 비교 → [Comparison]
- Index 적용 조건 → [주의], [Checklist]
- Transaction 설명 → [Flow]
- Pagination → [Best Practice], [주의]
- Query Error → [Troubleshooting]
- Anti Pattern → [Troubleshooting], [Checklist]

---

### [실무]

예시:

```md
### [Flow]

Requirement
→ Identify Table
→ Identify Relationship
→ Decide Join
→ Apply Filter
→ Apply Sort / Pagination
→ Review Index
```

---

### [FAQ]

Q. SQL 문서에 Flow가 중요한 이유는?

A.
SQL은 작성 순서와 논리 실행 순서가 다르기 때문에 Agent가 쿼리 해석을 안정적으로 하려면 Flow가 필요하다.

Q. SQL 문서에 Comparison이 필요한 이유는?

A.
WHERE와 HAVING, INNER JOIN과 LEFT JOIN, IN과 EXISTS처럼 자주 혼동되는 개념을 구분해야 하기 때문이다.

---

# 4. Query Design Rules

## 4.1 Query Purpose

### [개념]

Query Purpose는 SQL을 작성하기 전에 해당 쿼리가 무엇을 달성해야 하는지 정의하는 기준이다.

SQL은 문법보다 목적이 먼저다.

---

### [핵심]

Query Purpose 유형:

- 단건 조회
- 목록 조회
- 조건 검색
- 통계 조회
- 존재 여부 확인
- 중복 여부 확인
- 데이터 생성
- 데이터 수정
- 데이터 삭제
- 페이징 조회
- 권한 기반 조회
- 기간 조건 조회

---

### [실무]

Query Purpose Flow:

```text
요구사항 확인
→ 조회 / 변경 / 집계 구분
→ 대상 Table 확인
→ 관계 Table 확인
→ 조건 확인
→ 정렬 / 페이징 확인
→ 성능 검토
```

예:

```text
"사용자가 찜한 축제 목록"
→ 목록 조회
→ users, favorites, festivals
→ user_id 조건
→ festival 시작일 정렬
→ user_id index 검토
```

---

### [FAQ]

Q. SQL 작성 전에 가장 먼저 확인할 것은?

A.
쿼리 목적이다. 단건 조회인지 목록 조회인지 집계인지 변경 쿼리인지 먼저 구분해야 한다.

Q. Query Purpose가 불명확하면 어떤 문제가 생겨?

A.
불필요한 JOIN, 잘못된 조건, 과도한 데이터 조회, 성능 저하가 발생할 수 있다.

---

## 4.2 Table Relationship Rules

### [개념]

Table Relationship은 SQL JOIN과 조회 범위를 결정하는 테이블 간 관계다.

ERD의 Primary Key와 Foreign Key를 기준으로 판단한다.

---

### [핵심]

관계 유형:

- 1:1
- 1:N
- N:1
- N:M
- PK
- FK
- Join Table
- Parent Table
- Child Table

---

### [실무]

관계 확인 Flow:

```text
조회 대상 Entity 확인
→ 기준 Table 선택
→ FK 방향 확인
→ JOIN 필요 여부 확인
→ 1:N 중복 row 발생 여부 확인
→ DISTINCT / GROUP BY 필요 여부 검토
```

예:

```sql
SELECT f.festival_id, f.title
FROM favorites fav
JOIN festivals f ON fav.festival_id = f.festival_id
WHERE fav.user_id = 1;
```

주의:

- 1:N JOIN은 row 수가 증가할 수 있음
- N:M 관계는 중간 테이블 확인
- JOIN 조건 누락 시 Cartesian Product 발생
- Entity 관계와 실제 FK 제약이 다를 수 있음

---

### [FAQ]

Q. JOIN을 설계할 때 가장 먼저 볼 것은?

A.
ERD에서 PK와 FK 관계를 확인하고 기준 Table과 JOIN 방향을 정해야 한다.

Q. 1:N JOIN에서 주의할 점은?

A.
부모 row가 자식 수만큼 중복될 수 있으므로 결과 row 수를 반드시 확인해야 한다.

---

# 5. SELECT Query Rules

## 5.1 SELECT Basics

### [개념]

SELECT는 Table에서 필요한 Column과 Row를 조회하는 SQL 명령이다.

실무에서는 필요한 Column만 조회하는 것이 기본이다.

---

### [핵심]

구성 요소:

- SELECT
- FROM
- WHERE
- GROUP BY
- HAVING
- ORDER BY
- LIMIT / OFFSET
- Column Alias
- Table Alias

---

### [실무]

기본 예:

```sql
SELECT user_id, email, nickname
FROM users
WHERE active = true
ORDER BY created_at DESC;
```

권장:

- 필요한 Column만 조회
- Table Alias 명확히 사용
- 검색 조건은 WHERE에 작성
- 정렬 기준 명확화
- 목록 조회는 Pagination 고려

주의:

- `SELECT *` 지양
- 불필요한 Column 조회 금지
- 정렬 없는 Pagination 지양
- 대량 데이터 전체 조회 금지

---

### [FAQ]

Q. SELECT \*를 써도 돼?

A.
테스트나 임시 조회는 가능하지만 실무 쿼리와 RAG 예제에서는 필요한 Column만 명시하는 것이 좋다.

Q. 목록 조회에서 ORDER BY가 필요한 이유는?

A.
정렬 기준이 없으면 페이지 이동 시 결과 순서가 불안정할 수 있기 때문이다.

---

## 5.2 SQL Logical Execution Order

### [개념]

SQL Logical Execution Order는 SQL이 논리적으로 처리되는 순서다.

작성 순서와 실행 논리 순서는 다르다.

---

### [핵심]

논리 순서:

1. FROM
2. JOIN
3. WHERE
4. GROUP BY
5. HAVING
6. SELECT
7. ORDER BY
8. LIMIT / OFFSET

---

### [실무]

Flow:

```text
FROM
→ JOIN
→ WHERE
→ GROUP BY
→ HAVING
→ SELECT
→ ORDER BY
→ LIMIT
```

주의:

- WHERE에서는 SELECT Alias를 직접 사용할 수 없는 경우가 많음
- Aggregation 조건은 HAVING 사용
- GROUP BY 이전에는 집계 결과가 없음
- ORDER BY는 최종 결과 정렬

---

### [FAQ]

Q. SQL은 SELECT부터 실행돼?

A.
논리적으로는 FROM과 JOIN이 먼저 처리되고 WHERE, GROUP BY, HAVING 이후 SELECT가 처리된다.

Q. WHERE와 HAVING은 뭐가 달라?

A.
WHERE는 그룹화 전 row 필터링이고 HAVING은 GROUP BY 이후 집계 결과 필터링이다.

---

## 5.3 Filtering Rules

### [개념]

Filtering은 WHERE 조건을 사용해 필요한 Row만 조회하는 작업이다.

---

### [핵심]

조건 유형:

- Equality
- Range
- LIKE
- IN
- BETWEEN
- IS NULL
- IS NOT NULL
- AND
- OR
- NOT

---

### [실무]

예:

```sql
SELECT festival_id, title, event_start_date
FROM festivals
WHERE region_code = '11'
  AND event_start_date >= '2026-01-01'
  AND event_start_date < '2027-01-01';
```

권장:

- Index Column을 조건에 활용
- 날짜 조건은 범위로 작성
- OR 조건은 성능 영향 검토
- LIKE 앞쪽 wildcard 주의
- NULL 비교는 `IS NULL` 사용

주의:

```sql
-- 잘못된 NULL 비교
WHERE deleted_at = NULL;

-- 올바른 NULL 비교
WHERE deleted_at IS NULL;
```

---

### [FAQ]

Q. NULL은 = NULL로 비교해도 돼?

A.
안 된다. NULL 비교는 `IS NULL` 또는 `IS NOT NULL`을 사용해야 한다.

Q. LIKE '%keyword%'는 왜 주의해야 해?

A.
앞쪽 wildcard가 있으면 일반 B-Tree Index를 효율적으로 사용하기 어렵기 때문이다.

---

# 6. JOIN Rules

## 6.1 JOIN Basics

### [개념]

JOIN은 두 개 이상의 Table을 관계 Column 기준으로 연결해 조회하는 SQL 기능이다.

---

### [핵심]

JOIN 유형:

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- SELF JOIN
- CROSS JOIN
- JOIN Condition
- ON
- FK Relationship

---

### [실무]

기본 예:

```sql
SELECT r.review_id, r.content, u.nickname
FROM reviews r
JOIN users u ON r.user_id = u.user_id
WHERE r.festival_id = 10;
```

권장:

- JOIN 조건은 `ON`에 명확히 작성
- 기준 Table을 먼저 결정
- 1:N 관계의 row 증가 확인
- 필요한 JOIN만 사용
- Alias 사용으로 Column 출처 명확화

주의:

- JOIN 조건 누락 금지
- 불필요한 JOIN 금지
- LEFT JOIN 후 WHERE 조건으로 INNER JOIN처럼 변하는 문제 주의

---

### [FAQ]

Q. JOIN 조건을 빼면 어떻게 돼?

A.
Cartesian Product가 발생해 row 수가 폭증하고 잘못된 결과가 나올 수 있다.

Q. JOIN할 때 Alias를 쓰는 이유는?

A.
Column 출처를 명확히 하고 쿼리 가독성과 유지보수성을 높이기 위해서다.

---

## 6.2 INNER JOIN vs LEFT JOIN

### [개념]

INNER JOIN은 양쪽 Table에 매칭되는 Row만 조회한다.

LEFT JOIN은 왼쪽 Table의 Row를 모두 유지하고 오른쪽 Table 매칭 결과를 붙인다.

---

### [핵심]

비교:

| 비교       | INNER JOIN         | LEFT JOIN               |
| ---------- | ------------------ | ----------------------- |
| 기준       | 양쪽 매칭 필수     | 왼쪽 Table 유지         |
| 미매칭 Row | 제외               | 포함                    |
| 오른쪽 값  | 항상 존재          | NULL 가능               |
| 사용 예    | 작성자 있는 게시글 | 리뷰가 없어도 축제 조회 |

---

### [실무]

LEFT JOIN 예:

```sql
SELECT f.festival_id, f.title, r.review_id
FROM festivals f
LEFT JOIN reviews r ON f.festival_id = r.festival_id;
```

주의:

```sql
-- LEFT JOIN 결과를 WHERE에서 오른쪽 Table 조건으로 필터링하면 INNER JOIN처럼 동작할 수 있음
SELECT f.festival_id, f.title
FROM festivals f
LEFT JOIN reviews r ON f.festival_id = r.festival_id
WHERE r.rating >= 4;
```

필요 시 조건을 ON에 배치:

```sql
SELECT f.festival_id, f.title
FROM festivals f
LEFT JOIN reviews r
  ON f.festival_id = r.festival_id
 AND r.rating >= 4;
```

---

### [FAQ]

Q. INNER JOIN과 LEFT JOIN은 어떻게 골라?

A.
매칭되는 데이터만 필요하면 INNER JOIN, 기준 Table의 모든 Row를 유지해야 하면 LEFT JOIN을 사용한다.

Q. LEFT JOIN을 썼는데 결과가 줄어드는 이유는?

A.
WHERE 절에서 오른쪽 Table 조건을 걸면 NULL Row가 제거되어 INNER JOIN처럼 동작할 수 있기 때문이다.

---

# 7. Aggregation Rules

## 7.1 GROUP BY and Aggregation

### [개념]

Aggregation은 여러 Row를 그룹화해 COUNT, SUM, AVG 같은 집계 결과를 만드는 작업이다.

---

### [핵심]

집계 함수:

- COUNT
- SUM
- AVG
- MIN
- MAX

관련 절:

- GROUP BY
- HAVING
- DISTINCT

---

### [실무]

예:

```sql
SELECT festival_id, COUNT(*) AS review_count, AVG(rating) AS average_rating
FROM reviews
GROUP BY festival_id
HAVING COUNT(*) >= 10
ORDER BY average_rating DESC;
```

권장:

- SELECT에 일반 Column을 쓰면 GROUP BY 포함 여부 확인
- 집계 조건은 HAVING 사용
- COUNT(\*)와 COUNT(column)의 NULL 차이 이해
- 집계 결과 Alias 명확화

주의:

- GROUP BY 없는 Aggregation과 일반 Column 혼용 금지
- 중복 JOIN 후 COUNT 결과 왜곡 주의
- DISTINCT는 원인 해결 없이 남용하지 않음

---

### [FAQ]

Q. GROUP BY는 언제 써?

A.
사용자별 주문 수, 축제별 리뷰 수처럼 특정 기준별 집계 결과가 필요할 때 사용한다.

Q. COUNT(\*)와 COUNT(column)은 달라?

A.
COUNT(\*)는 Row 수를 세고 COUNT(column)은 해당 Column이 NULL이 아닌 Row만 센다.

---

## 7.2 WHERE vs HAVING

### [개념]

WHERE는 그룹화 전 Row를 필터링하고 HAVING은 GROUP BY 이후 집계 결과를 필터링한다.

---

### [핵심]

비교:

| 비교           | WHERE           | HAVING          |
| -------------- | --------------- | --------------- |
| 적용 시점      | GROUP BY 전     | GROUP BY 후     |
| 대상           | 개별 Row        | 집계 결과       |
| 집계 함수 사용 | 일반적으로 불가 | 가능            |
| 예             | rating >= 4     | COUNT(\*) >= 10 |

---

### [실무]

예:

```sql
SELECT festival_id, COUNT(*) AS review_count
FROM reviews
WHERE rating >= 4
GROUP BY festival_id
HAVING COUNT(*) >= 10;
```

해석:

```text
rating이 4 이상인 리뷰만 먼저 선택
→ festival_id별 그룹화
→ 리뷰 수가 10개 이상인 축제만 남김
```

---

### [FAQ]

Q. 집계 조건은 WHERE에 쓰면 안 돼?

A.
집계 함수 결과 조건은 HAVING에 작성해야 한다.

Q. WHERE와 HAVING을 같이 쓸 수 있어?

A.
가능하다. WHERE는 집계 전 데이터 범위를 줄이고 HAVING은 집계 후 결과를 필터링한다.

---

# 8. Subquery and EXISTS Rules

## 8.1 Subquery Basics

### [개념]

Subquery는 SQL 내부에 포함된 또 다른 SELECT 쿼리다.

단건 값, 목록, 존재 여부, 집계 결과를 조건에 사용할 수 있다.

---

### [핵심]

종류:

- Scalar Subquery
- IN Subquery
- EXISTS Subquery
- Correlated Subquery
- Derived Table

---

### [실무]

예:

```sql
SELECT festival_id, title
FROM festivals
WHERE festival_id IN (
  SELECT festival_id
  FROM favorites
  WHERE user_id = 1
);
```

권장:

- EXISTS는 존재 여부 확인에 적합
- IN은 작은 결과 집합에 단순함
- 복잡한 Subquery는 JOIN으로 변경 가능성 검토
- Correlated Subquery 성능 주의

---

### [FAQ]

Q. Subquery는 언제 써?

A.
다른 조회 결과를 조건으로 사용하거나 존재 여부, 집계 결과를 기준으로 필터링할 때 사용한다.

Q. Subquery와 JOIN 중 뭐가 좋아?

A.
목적과 DBMS 최적화에 따라 다르다. 관계 데이터를 함께 조회하면 JOIN, 존재 여부만 확인하면 EXISTS가 적합한 경우가 많다.

---

## 8.2 EXISTS vs IN

### [개념]

EXISTS는 Subquery 결과가 존재하는지 확인한다.

IN은 특정 값이 Subquery 결과 목록에 포함되는지 확인한다.

---

### [핵심]

비교:

| 비교       | EXISTS             | IN                |
| ---------- | ------------------ | ----------------- |
| 기준       | 존재 여부          | 값 포함 여부      |
| NULL 영향  | 상대적으로 안전    | NULL 주의         |
| 사용 예    | 관련 row 존재 확인 | 특정 ID 목록 포함 |
| Correlated | 자주 사용          | 가능              |

---

### [실무]

EXISTS 예:

```sql
SELECT f.festival_id, f.title
FROM festivals f
WHERE EXISTS (
  SELECT 1
  FROM reviews r
  WHERE r.festival_id = f.festival_id
);
```

IN 예:

```sql
SELECT festival_id, title
FROM festivals
WHERE festival_id IN (1, 2, 3);
```

주의:

- `NOT IN`은 NULL이 포함되면 예상과 다른 결과가 나올 수 있음
- 존재 여부 확인은 EXISTS가 명확한 경우가 많음

---

### [FAQ]

Q. EXISTS는 SELECT 1을 쓰는 이유가 뭐야?

A.
존재 여부만 확인하므로 실제 Column 값이 중요하지 않기 때문이다.

Q. NOT IN은 왜 조심해야 해?

A.
Subquery 결과에 NULL이 포함되면 비교 결과가 UNKNOWN이 되어 예상과 다른 결과가 나올 수 있다.

---

# 9. Data Modification Rules

## 9.1 INSERT Rules

### [개념]

INSERT는 Table에 새로운 Row를 추가하는 SQL 명령이다.

---

### [핵심]

확인 대상:

- Required Column
- Default Value
- Not Null
- Unique Constraint
- Foreign Key
- Created At
- Generated Key

---

### [실무]

예:

```sql
INSERT INTO users (email, nickname, role, created_at)
VALUES ('user@example.com', 'tester', 'ROLE_USER', NOW());
```

권장:

- Column 목록 명시
- Not Null Column 확인
- Unique 중복 가능성 확인
- FK 대상 존재 확인
- 기본값과 Application 생성값 기준 통일

---

### [FAQ]

Q. INSERT에서 Column 목록을 생략해도 돼?

A.
가능은 하지만 Table 구조 변경에 취약하므로 실무 예제에서는 Column 목록을 명시하는 것이 좋다.

Q. INSERT 전에 중복 확인이 필요해?

A.
email, username처럼 Unique 제약이 있는 값은 중복 가능성을 고려해야 한다.

---

## 9.2 UPDATE and DELETE Safety Rules

### [개념]

UPDATE는 기존 Row를 수정하고 DELETE는 Row를 삭제한다.

두 명령은 영향 범위를 반드시 제한해야 한다.

---

### [핵심]

필수 확인:

- WHERE 조건
- 대상 Row 수
- FK 영향
- Soft Delete 여부
- Transaction 필요 여부
- Backup / Rollback 가능성
- Audit Column

---

### [실무]

안전한 UPDATE:

```sql
UPDATE users
SET nickname = 'newNickname',
    updated_at = NOW()
WHERE user_id = 1;
```

안전한 DELETE:

```sql
DELETE FROM favorites
WHERE user_id = 1
  AND festival_id = 10;
```

주의:

```sql
-- 위험: 전체 Row 수정
UPDATE users
SET role = 'ROLE_ADMIN';

-- 위험: 전체 Row 삭제
DELETE FROM users;
```

권장:

- 실행 전 SELECT로 대상 확인
- WHERE 없는 UPDATE / DELETE 금지
- 운영 데이터는 Soft Delete 검토
- 여러 Table 영향 시 Transaction 사용

---

### [FAQ]

Q. UPDATE나 DELETE에서 가장 위험한 실수는?

A.
WHERE 조건을 누락해 전체 Row를 수정하거나 삭제하는 것이다.

Q. 삭제는 항상 DELETE로 처리해?

A.
아니다. 복구와 이력 관리가 필요하면 deleted_at이나 active 같은 컬럼을 사용하는 Soft Delete를 검토한다.

---

# 10. Index and Performance Rules

## 10.1 Index Basics

### [개념]

Index는 Table에서 특정 Column 기준으로 데이터를 빠르게 찾기 위한 자료구조다.

조회 성능을 높일 수 있지만 쓰기 비용과 저장 공간 비용이 있다.

---

### [핵심]

Index 사용 후보:

- WHERE 조건 Column
- JOIN Column
- ORDER BY Column
- GROUP BY Column
- Foreign Key Column
- Unique Column
- High Selectivity Column

---

### [실무]

Index 검토 Flow:

```text
Slow Query
→ WHERE Column 확인
→ JOIN Column 확인
→ ORDER BY / GROUP BY 확인
→ Cardinality 확인
→ Composite Index 순서 확인
→ Execution Plan 확인
```

예:

```sql
CREATE INDEX idx_favorites_user_id
ON favorites (user_id);
```

주의:

- Index는 많을수록 좋은 것이 아님
- 쓰기 성능 저하 가능
- 낮은 선택도 Column은 효과 제한
- Column에 함수 적용 시 Index 사용 어려움
- 복합 Index는 Column 순서 중요

---

### [FAQ]

Q. Index는 언제 만들어?

A.
자주 조회 조건, JOIN 조건, 정렬 조건으로 사용되는 Column에 대해 성능 문제가 있거나 예상될 때 검토한다.

Q. Index를 많이 만들면 좋아?

A.
아니다. INSERT / UPDATE / DELETE 비용과 저장 공간이 증가하므로 필요한 Index만 만들어야 한다.

---

## 10.2 Sargable Query Rules

### [개념]

Sargable Query는 Index를 효율적으로 사용할 수 있는 검색 조건이다.

Column에 함수나 연산을 적용하면 Index 사용이 어려워질 수 있다.

---

### [핵심]

나쁜 예:

```sql
WHERE YEAR(created_at) = 2026
```

좋은 예:

```sql
WHERE created_at >= '2026-01-01'
  AND created_at < '2027-01-01'
```

---

### [실무]

권장:

- 날짜는 범위 조건 사용
- Column을 함수로 감싸지 않음
- 앞쪽 wildcard LIKE 지양
- 암시적 형변환 주의
- Index Column 타입과 비교 값 타입 일치

주의:

```sql
-- Index 사용 불리
WHERE CAST(user_id AS CHAR) = '10';

-- 권장
WHERE user_id = 10;
```

---

### [FAQ]

Q. 날짜 검색에서 YEAR(column)을 쓰면 안 좋아?

A.
Column에 함수를 적용하면 Index를 효율적으로 사용하기 어려울 수 있어 날짜 범위 조건이 더 적합하다.

Q. Sargable이 왜 중요해?

A.
Index를 활용할 수 있는 형태로 조건을 작성해야 대량 데이터에서 조회 성능을 확보할 수 있기 때문이다.

---

## 10.3 Pagination Rules

### [개념]

Pagination은 목록 데이터를 일정 개수씩 나누어 조회하는 방식이다.

---

### [핵심]

방식:

- OFFSET Pagination
- Cursor Pagination
- Keyset Pagination
- LIMIT
- OFFSET
- ORDER BY
- Stable Sort

---

### [실무]

OFFSET Pagination 예:

```sql
SELECT festival_id, title, created_at
FROM festivals
ORDER BY created_at DESC, festival_id DESC
LIMIT 20 OFFSET 40;
```

주의:

- ORDER BY 없는 Pagination 금지
- OFFSET이 커질수록 성능 저하 가능
- 중복 정렬 값이 있으면 PK 추가 정렬 권장
- 무한 스크롤은 Cursor Pagination 검토

Cursor Pagination 예:

```sql
SELECT festival_id, title, created_at
FROM festivals
WHERE created_at < '2026-07-01 10:00:00'
ORDER BY created_at DESC
LIMIT 20;
```

---

### [FAQ]

Q. Pagination에서 ORDER BY가 왜 필수야?

A.
정렬 기준이 없으면 페이지마다 결과 순서가 흔들릴 수 있기 때문이다.

Q. OFFSET Pagination은 언제 문제가 돼?

A.
OFFSET 값이 커지면 앞 데이터를 많이 건너뛰어야 해서 성능이 떨어질 수 있다.

---

# 11. Transaction Rules

## 11.1 Transaction Basics

### [개념]

Transaction은 여러 데이터 변경 작업을 하나의 작업 단위로 묶어 모두 성공하거나 모두 실패하도록 보장하는 개념이다.

---

### [핵심]

ACID:

- Atomicity
- Consistency
- Isolation
- Durability

사용 상황:

- 여러 Table 동시 변경
- 결제 / 주문 / 포인트 차감
- 재고 감소
- 회원 탈퇴 처리
- 데이터 정합성 보장 필요
- 실패 시 Rollback 필요

---

### [실무]

Transaction Flow:

```text
Begin Transaction
→ Validate
→ Insert / Update / Delete
→ Commit
→ Error
→ Rollback
```

예:

```text
후원 결제 성공
→ donation 생성
→ payment 생성
→ festival 후원 금액 증가
→ 모두 성공 시 commit
→ 하나라도 실패 시 rollback
```

주의:

- 단순 SELECT는 Transaction이 필요 없을 수 있음
- 긴 Transaction은 Lock 지속 시간이 길어짐
- 외부 API 호출과 DB Transaction 경계 주의
- Spring에서는 @Transactional 적용 범위 확인

---

### [FAQ]

Q. Transaction은 언제 필요해?

A.
여러 DB 변경이 하나의 성공/실패 단위로 묶여야 할 때 필요하다.

Q. Transaction이 길어지면 왜 문제야?

A.
Lock 유지 시간이 길어져 동시성 성능이 떨어지고 Deadlock 가능성이 증가할 수 있다.

---

## 11.2 Isolation and Lock Basics

### [개념]

Isolation은 동시에 실행되는 Transaction들이 서로 어떤 수준으로 격리되는지 결정한다.

Lock은 데이터 정합성을 위해 특정 Row나 범위 접근을 제어하는 장치다.

---

### [핵심]

Isolation 관련 문제:

- Dirty Read
- Non-repeatable Read
- Phantom Read

Isolation Level:

- READ UNCOMMITTED
- READ COMMITTED
- REPEATABLE READ
- SERIALIZABLE

Lock 관련:

- Shared Lock
- Exclusive Lock
- Row Lock
- Gap Lock
- Deadlock

---

### [실무]

주의 상황:

- 동시에 같은 재고 감소
- 동시에 같은 포인트 사용
- 중복 신청 방지
- 선착순 이벤트
- 결제 상태 변경
- 좋아요 / 조회수 카운트 증가

권장:

- 동시성 요구사항 먼저 확인
- DB 제약 조건과 Transaction 함께 사용
- Unique Constraint로 중복 방지
- 필요 시 Pessimistic Lock / Optimistic Lock 검토
- Deadlock 발생 가능성 고려

---

### [FAQ]

Q. Isolation Level은 항상 높을수록 좋아?

A.
아니다. 격리 수준이 높으면 정합성은 강해질 수 있지만 동시성 성능이 낮아질 수 있다.

Q. 중복 신청 방지는 SQL만으로 가능해?

A.
Application 검증만으로는 부족할 수 있고 Unique Constraint와 Transaction을 함께 고려해야 한다.

---

# 12. Constraint and Data Integrity Rules

## 12.1 Constraint Basics

### [개념]

Constraint는 데이터 무결성을 보장하기 위해 Table에 적용하는 제약 조건이다.

---

### [핵심]

종류:

- Primary Key
- Foreign Key
- Unique
- Not Null
- Check
- Default

---

### [실무]

예:

```sql
CREATE TABLE favorites (
  favorite_id BIGINT PRIMARY KEY,
  user_id BIGINT NOT NULL,
  festival_id BIGINT NOT NULL,
  created_at DATETIME NOT NULL,
  UNIQUE (user_id, festival_id)
);
```

권장:

- 중복 방지는 Unique Constraint 사용
- 필수 값은 Not Null 사용
- 관계 무결성은 FK 검토
- Application 검증과 DB 제약을 함께 사용
- Enum 성격 값은 Check 또는 Application Enum 기준 통일

---

### [FAQ]

Q. Application에서 검증하면 DB Constraint는 없어도 돼?

A.
아니다. Application 검증은 우회될 수 있으므로 중요한 무결성은 DB Constraint로도 보장하는 것이 좋다.

Q. Unique Constraint는 언제 필요해?

A.
email, user-festival favorite처럼 중복되면 안 되는 데이터에 필요하다.

---

# 13. Backend Integration Rules

## 13.1 SQL and JPA Repository

### [개념]

SQL Domain Rules는 Backend Repository 설계와 연결되어야 한다.

JPA, JPQL, QueryDSL, Native Query는 모두 SQL 기반 사고가 필요하다.

---

### [핵심]

연결 대상:

- Spring Data JPA Repository
- Derived Query Method
- JPQL
- QueryDSL
- Native Query
- DTO Projection
- Pagination
- Fetch Join
- N+1
- Transaction

---

### [실무]

Repository 검토 Flow:

```text
Service Requirement
→ Query Purpose 확인
→ Entity Relationship 확인
→ JPA Method 가능 여부 확인
→ JPQL / QueryDSL 필요 여부 확인
→ Native Query 필요 여부 확인
→ Pagination / Index 검토
```

주의:

- 복잡한 동적 검색은 QueryDSL 검토
- 단순 CRUD는 Repository Method로 충분
- DB 특화 기능은 Native Query 검토
- Fetch Join과 Pagination 조합 주의
- N+1 발생 가능성 검토

---

### [FAQ]

Q. SQL을 알면 JPA를 안 써도 돼?

A.
아니다. JPA를 쓰더라도 실제 DB에서는 SQL이 실행되므로 SQL 이해가 Repository 설계와 성능 검토에 필요하다.

Q. Native Query는 언제 써?

A.
JPQL이나 QueryDSL로 표현하기 어렵거나 DB 특화 기능이 필요한 경우에 검토한다.

---

# 14. Troubleshooting Rules

## 14.1 Wrong Result Troubleshooting

### [개념]

Wrong Result Troubleshooting은 SQL 결과가 기대와 다를 때 조건, JOIN, 집계, NULL 처리를 점검하는 과정이다.

---

### [핵심]

확인 대상:

- FROM 기준 Table
- JOIN 조건
- WHERE 조건
- NULL 비교
- 1:N JOIN 중복
- GROUP BY 기준
- HAVING 조건
- ORDER BY
- Pagination
- Data Type

---

### [실무]

Debug Flow:

```text
Expected Result 정의
→ Base Table 단독 조회
→ WHERE 조건 하나씩 추가
→ JOIN 하나씩 추가
→ Row Count 확인
→ GROUP BY 결과 확인
→ ORDER BY / LIMIT 확인
```

---

### [FAQ]

Q. JOIN 후 row 수가 갑자기 늘어나는 이유는?

A.
1:N 관계 JOIN이거나 JOIN 조건이 잘못되어 하나의 row가 여러 row와 매칭되었을 수 있다.

Q. 조건을 걸었는데 NULL 데이터가 안 나와?

A.
NULL은 일반 비교 연산으로 처리되지 않으므로 IS NULL 또는 별도 조건이 필요하다.

---

## 14.2 Slow Query Troubleshooting

### [개념]

Slow Query Troubleshooting은 SQL 실행 시간이 느릴 때 조건, Index, JOIN, 정렬, 데이터 양을 점검하는 과정이다.

---

### [핵심]

확인 대상:

- Full Table Scan
- Missing Index
- Inefficient Join
- Large OFFSET
- Function on Indexed Column
- Leading Wildcard LIKE
- Large Sort
- Unnecessary Column
- N+1 Query
- Execution Plan

---

### [실무]

Debug Flow:

```text
Slow Query 확인
→ 실행 빈도 확인
→ WHERE / JOIN Column 확인
→ Index 존재 확인
→ Execution Plan 확인
→ SELECT Column 축소
→ Pagination 방식 검토
→ Query Rewrite
```

권장:

- 먼저 실제 병목 쿼리 확인
- 추측만으로 Index 추가하지 않음
- Execution Plan을 기준으로 판단
- Application N+1과 SQL 단일 쿼리 성능을 함께 확인

---

### [FAQ]

Q. 쿼리가 느리면 무조건 Index를 추가하면 돼?

A.
아니다. 조건, JOIN, 정렬, 데이터 양, 실행 계획을 먼저 확인한 뒤 필요한 Index만 추가해야 한다.

Q. Full Table Scan은 항상 나빠?

A.
항상 나쁘지는 않다. 작은 Table이나 대부분의 Row가 필요한 경우에는 Full Scan이 자연스러울 수 있다.

---

## 14.3 SQL Common Mistakes

### [개념]

SQL Common Mistakes는 실무에서 자주 발생하는 쿼리 작성 실수를 정리한다.

---

### [핵심]

자주 발생:

- SELECT \* 남용
- WHERE 없는 UPDATE / DELETE
- JOIN 조건 누락
- LEFT JOIN 후 WHERE 조건 실수
- NULL을 = NULL로 비교
- GROUP BY와 일반 Column 혼용
- COUNT 결과 중복
- ORDER BY 없는 Pagination
- 큰 OFFSET 남용
- Index Column에 함수 적용
- LIKE '%keyword%' 성능 문제 무시
- OR 조건 성능 문제 무시
- 중복 데이터 방지를 Application에만 의존
- Transaction 범위 과도하게 넓힘
- 외부 API 호출을 Transaction 내부에 오래 유지
- N+1 Query 방치

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: 축제별 리뷰 수가 실제보다 많음
원인: reviews와 images를 동시에 JOIN하면서 row가 곱해짐
해결: 집계 Subquery 분리 또는 COUNT(DISTINCT review_id) 검토
```

---

### [FAQ]

Q. SQL 초보가 가장 많이 하는 실수는?

A.
JOIN 조건 누락, WHERE 없는 UPDATE / DELETE, NULL 비교 오류, SELECT \* 남용, GROUP BY 결과 오해가 많다.

Q. SQL 문제는 어떻게 찾는 게 좋아?

A.
Base Table부터 시작해 WHERE, JOIN, GROUP BY, ORDER BY를 단계적으로 추가하며 row 수와 결과를 확인한다.

---

# 15. Comparison Rules

## 15.1 Required Comparisons

### [개념]

SQL 문서는 자주 혼동되는 개념을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- WHERE vs HAVING
- INNER JOIN vs LEFT JOIN
- JOIN vs Subquery
- IN vs EXISTS
- COUNT(\*) vs COUNT(column)
- DELETE vs Soft Delete
- OFFSET Pagination vs Cursor Pagination
- Primary Key vs Foreign Key
- Unique vs Index
- Transaction vs 단일 Query
- Optimistic Lock vs Pessimistic Lock
- SQL vs JPQL vs QueryDSL vs Native Query

---

### [실무]

예시:

| 비교 | JPQL                  | QueryDSL            | Native Query      |
| ---- | --------------------- | ------------------- | ----------------- |
| 기준 | Entity 중심           | Type-safe 동적 쿼리 | DB SQL 직접 작성  |
| 장점 | JPA와 자연스러움      | 동적 조건에 강함    | DB 특화 기능 가능 |
| 주의 | 복잡한 동적 조건 불편 | 설정 필요           | DB 종속성 증가    |
| 사용 | 단순 Entity 조회      | 검색 조건 조합      | 특수 쿼리         |

---

### [FAQ]

Q. Comparison 섹션은 왜 필요해?

A.
SQL은 비슷해 보이지만 결과와 성능이 다른 개념이 많아 비교가 Retrieval과 답변 정확도를 높인다.

Q. SQL 비교 문서에서 가장 중요한 것은?

A.
결과 차이, 사용 기준, 성능 영향, 실무 주의점을 함께 설명하는 것이다.

---

# 16. Checklist Rules

## 16.1 SQL Document Checklist

### [개념]

SQL 문서 검수 시 쿼리 설계와 성능 검토 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] Query Purpose가 명확한가?
- [ ] 대상 Table과 관계가 명확한가?
- [ ] SELECT Column이 필요한 값만 포함하는가?
- [ ] WHERE 조건이 명확한가?
- [ ] JOIN 조건이 누락되지 않았는가?
- [ ] 1:N JOIN 중복 row 가능성을 검토했는가?
- [ ] WHERE와 HAVING 차이가 반영되었는가?
- [ ] GROUP BY 집계 기준이 명확한가?
- [ ] NULL 처리 기준이 포함되었는가?
- [ ] Subquery / JOIN 선택 기준이 포함되었는가?
- [ ] EXISTS / IN 차이가 포함되었는가?
- [ ] Pagination에 ORDER BY가 포함되었는가?
- [ ] Index 검토 기준이 포함되었는가?
- [ ] UPDATE / DELETE 안전 기준이 포함되었는가?
- [ ] Transaction 적용 기준이 포함되었는가?
- [ ] Backend Repository / QueryDSL 연결 기준이 포함되었는가?
- [ ] Troubleshooting Flow가 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Query Purpose Check
→ Table Relationship Check
→ Join / Filter Check
→ Aggregation Check
→ Index / Performance Check
→ Transaction Check
→ Backend Integration Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. SQL 문서 검수에서 가장 중요한 것은?

A.
Query Purpose, Table Relationship, JOIN 조건, WHERE 조건, Index 가능성, Transaction 필요 여부, Anti Pattern 포함 여부다.

---

# 17. Retrieval Optimization Rules

## 17.1 Keyword Rules

### [개념]

SQL 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- SQL
- Query
- SELECT
- INSERT
- UPDATE
- DELETE
- WHERE
- JOIN
- INNER JOIN
- LEFT JOIN
- GROUP BY
- HAVING
- ORDER BY
- LIMIT
- OFFSET
- Pagination
- Subquery
- EXISTS
- IN
- Aggregation
- COUNT
- SUM
- AVG
- NULL
- CASE WHEN
- Index
- Execution Plan
- Transaction
- Lock
- Isolation Level
- Primary Key
- Foreign Key
- Unique Constraint
- Not Null
- Query Performance
- Slow Query
- N+1 Query
- Repository
- JPQL
- QueryDSL
- Native Query
- SQL Anti Pattern

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- SQL 쿼리는 어떻게 작성해?
- JOIN은 언제 써?
- INNER JOIN과 LEFT JOIN 차이는?
- WHERE와 HAVING 차이는?
- GROUP BY는 언제 써?
- COUNT가 왜 다르게 나와?
- EXISTS와 IN 차이는?
- Index는 언제 만들어?
- 쿼리가 느릴 때 뭘 확인해?
- Pagination 쿼리는 어떻게 작성해?
- UPDATE 전에 뭘 확인해야 해?
- Transaction은 언제 필요해?
- JPA에서 SQL을 왜 알아야 해?
- Native Query는 언제 써?
- NULL 비교는 어떻게 해?

---

### [FAQ]

Q. SQL 문서에서 키워드 반복은 중복이야?

A.
불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. SQL FAQ 질문은 어떤 스타일이 좋아?

A.
사용자가 실제로 물어볼 법한 자연어 질문과 실무 오류 질문을 포함하는 것이 좋다.

---

# 18. Version Rules

## 18.1 Modern SQL 기준

### [개념]

SQL 문서는 Modern Backend 개발 기준으로 작성한다.

---

### [핵심]

기준:

- Standard SQL 기반
- MySQL / MariaDB 실무 호환 우선
- Spring Boot Backend 연결 고려
- JPA / JPQL / QueryDSL 연결 고려
- REST API 목록 조회 / 검색 조회 고려
- Pagination / Sorting 고려
- Index / Transaction 기본 고려
- Soft Delete 고려
- LocalDateTime / created_at / updated_at 기준 고려
- RDBMS 중심

Legacy / 제외:

- 무분별한 SELECT \*
- Application 검증만으로 무결성 처리
- WHERE 없는 UPDATE / DELETE
- Pagination 없는 대량 목록 조회
- JOIN 조건 암묵 처리
- Oracle 전용 문법 중심 구성
- Stored Procedure 중심 Application 설계
- DBMS 내부 구조 중심 설명

---

### [실무]

실무 기준:

```text
Modern Backend SQL
→ Requirement
→ Entity / ERD
→ Query Purpose
→ Join / Filter
→ Pagination / Sort
→ Index
→ Repository Integration
→ Review
```

---

### [FAQ]

Q. SQL 문서는 MySQL 기준으로 작성해?

A.
Foundation 문서는 표준 SQL을 우선하고 실무 예제는 MySQL / MariaDB와 Spring Boot Backend 환경을 고려한다.

Q. Oracle 문법도 같이 넣어야 해?

A.
필요 시 Comparison으로 짧게 언급할 수 있지만 Foundation 문서에서는 DBMS별 문법 혼용을 최소화한다.

---

# 19. Final Goal

## 19.1 Domain Final Goal

### [개념]

SQL RAG 문서는 Backend Agent가 요구사항을 SQL 관점으로 해석하고 안정적인 쿼리를 작성하며 성능과 데이터 정합성 문제를 검토하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- Query Purpose 파악
- Table Relationship 분석
- SELECT Query 작성
- JOIN 설계
- Filtering 설계
- Aggregation 설계
- Subquery / EXISTS 선택
- Pagination 설계
- Index 적용 가능성 검토
- Transaction 필요 여부 판단
- Constraint 기반 무결성 판단
- UPDATE / DELETE 안전성 검토
- Slow Query 원인 분석
- SQL Anti Pattern 탐지
- JPA / QueryDSL / Native Query 연결 판단

---

### [실무]

Agent 수행 가능 작업:

```text
User Backend Data Request
→ Identify Query Purpose
→ Identify Tables
→ Identify Relationships
→ Design SQL Query
→ Check Join / Filter / Aggregation
→ Check Pagination / Sorting
→ Review Index / Transaction
→ Detect Anti Pattern
→ SQL Output
```

---

### [FAQ]

Q. SQL Domain Rules의 최종 목적은 뭐야?

A.
Backend Agent가 SQL 쿼리를 단순히 문법적으로 작성하는 수준을 넘어 결과 정확성, 성능, 정합성까지 검토하도록 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules와 연결돼야 해?

A.
JPA Advanced, QueryDSL Practical, API Design, Performance Tuning 문서와 연결되는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. SQL Domain Rules는 왜 필요해?
A. Backend Agent가 요구사항을 SQL 조회, 변경, 집계, 성능 검토 기준으로 해석해야 하기 때문이다.

Q. SQL 쿼리는 어떻게 작성해?
A. Query Purpose를 먼저 정하고 대상 Table, JOIN 관계, WHERE 조건, 정렬, 페이징, Index 가능성을 순서대로 확인한다.

Q. Query Purpose가 뭐야?
A. 쿼리가 단건 조회, 목록 조회, 집계, 존재 확인, 생성, 수정, 삭제 중 무엇을 수행하는지 정의하는 기준이다.

Q. SQL 작성 전에 가장 먼저 확인할 것은?
A. 쿼리 목적이다. 단건 조회인지 목록 조회인지 집계인지 변경 쿼리인지 먼저 구분해야 한다.

Q. Table Relationship은 왜 중요해?
A. PK와 FK 관계가 JOIN 방향, row 중복 가능성, 조회 결과 정확성을 결정하기 때문이다.

Q. JOIN을 설계할 때 가장 먼저 볼 것은?
A. ERD에서 PK와 FK 관계를 확인하고 기준 Table과 JOIN 방향을 정해야 한다.

Q. SELECT \*를 써도 돼?
A. 테스트나 임시 조회는 가능하지만 실무 쿼리와 RAG 예제에서는 필요한 Column만 명시하는 것이 좋다.

Q. SQL은 SELECT부터 실행돼?
A. 논리적으로는 FROM과 JOIN이 먼저 처리되고 WHERE, GROUP BY, HAVING 이후 SELECT가 처리된다.

Q. SQL 논리 실행 순서는?
A. FROM, JOIN, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT 순서로 이해한다.

Q. WHERE와 HAVING 차이는?
A. WHERE는 그룹화 전 row 필터링이고 HAVING은 GROUP BY 이후 집계 결과 필터링이다.

Q. NULL은 = NULL로 비교해도 돼?
A. 안 된다. NULL 비교는 IS NULL 또는 IS NOT NULL을 사용해야 한다.

Q. LIKE '%keyword%'는 왜 주의해야 해?
A. 앞쪽 wildcard가 있으면 일반 B-Tree Index를 효율적으로 사용하기 어렵기 때문이다.

Q. JOIN 조건을 빼면 어떻게 돼?
A. Cartesian Product가 발생해 row 수가 폭증하고 잘못된 결과가 나올 수 있다.

Q. INNER JOIN과 LEFT JOIN은 어떻게 골라?
A. 매칭되는 데이터만 필요하면 INNER JOIN, 기준 Table의 모든 Row를 유지해야 하면 LEFT JOIN을 사용한다.

Q. LEFT JOIN을 썼는데 결과가 줄어드는 이유는?
A. WHERE 절에서 오른쪽 Table 조건을 걸면 NULL Row가 제거되어 INNER JOIN처럼 동작할 수 있기 때문이다.

Q. GROUP BY는 언제 써?
A. 사용자별 주문 수, 축제별 리뷰 수처럼 특정 기준별 집계 결과가 필요할 때 사용한다.

Q. COUNT(_)와 COUNT(column)은 달라?
A. COUNT(_)는 Row 수를 세고 COUNT(column)은 해당 Column이 NULL이 아닌 Row만 센다.

Q. 집계 조건은 WHERE에 쓰면 안 돼?
A. 집계 함수 결과 조건은 HAVING에 작성해야 한다.

Q. Subquery는 언제 써?
A. 다른 조회 결과를 조건으로 사용하거나 존재 여부, 집계 결과를 기준으로 필터링할 때 사용한다.

Q. Subquery와 JOIN 중 뭐가 좋아?
A. 관계 데이터를 함께 조회하면 JOIN, 존재 여부만 확인하면 EXISTS가 적합한 경우가 많다.

Q. EXISTS와 IN 차이는?
A. EXISTS는 존재 여부를 확인하고 IN은 특정 값이 목록에 포함되는지 확인한다.

Q. EXISTS는 SELECT 1을 쓰는 이유가 뭐야?
A. 존재 여부만 확인하므로 실제 Column 값이 중요하지 않기 때문이다.

Q. NOT IN은 왜 조심해야 해?
A. Subquery 결과에 NULL이 포함되면 예상과 다른 결과가 나올 수 있다.

Q. INSERT에서 Column 목록을 생략해도 돼?
A. 가능은 하지만 Table 구조 변경에 취약하므로 실무 예제에서는 Column 목록을 명시하는 것이 좋다.

Q. UPDATE나 DELETE에서 가장 위험한 실수는?
A. WHERE 조건을 누락해 전체 Row를 수정하거나 삭제하는 것이다.

Q. 삭제는 항상 DELETE로 처리해?
A. 아니다. 복구와 이력 관리가 필요하면 deleted_at이나 active 같은 컬럼을 사용하는 Soft Delete를 검토한다.

Q. Index는 언제 만들어?
A. 자주 조회 조건, JOIN 조건, 정렬 조건으로 사용되는 Column에 대해 성능 문제가 있거나 예상될 때 검토한다.

Q. Index를 많이 만들면 좋아?
A. 아니다. INSERT, UPDATE, DELETE 비용과 저장 공간이 증가하므로 필요한 Index만 만들어야 한다.

Q. 날짜 검색에서 YEAR(column)을 쓰면 안 좋아?
A. Column에 함수를 적용하면 Index를 효율적으로 사용하기 어려울 수 있어 날짜 범위 조건이 더 적합하다.

Q. Sargable이 뭐야?
A. Index를 효율적으로 사용할 수 있는 검색 조건 형태를 의미한다.

Q. Pagination에서 ORDER BY가 왜 필수야?
A. 정렬 기준이 없으면 페이지마다 결과 순서가 흔들릴 수 있기 때문이다.

Q. OFFSET Pagination은 언제 문제가 돼?
A. OFFSET 값이 커지면 앞 데이터를 많이 건너뛰어야 해서 성능이 떨어질 수 있다.

Q. Transaction은 언제 필요해?
A. 여러 DB 변경이 하나의 성공/실패 단위로 묶여야 할 때 필요하다.

Q. Transaction이 길어지면 왜 문제야?
A. Lock 유지 시간이 길어져 동시성 성능이 떨어지고 Deadlock 가능성이 증가할 수 있다.

Q. Isolation Level은 항상 높을수록 좋아?
A. 아니다. 격리 수준이 높으면 정합성은 강해질 수 있지만 동시성 성능이 낮아질 수 있다.

Q. Application에서 검증하면 DB Constraint는 없어도 돼?
A. 아니다. 중요한 무결성은 DB Constraint로도 보장하는 것이 좋다.

Q. Unique Constraint는 언제 필요해?
A. email, user-festival favorite처럼 중복되면 안 되는 데이터에 필요하다.

Q. JPA에서 SQL을 왜 알아야 해?
A. JPA를 쓰더라도 실제 DB에서는 SQL이 실행되므로 SQL 이해가 Repository 설계와 성능 검토에 필요하다.

Q. Native Query는 언제 써?
A. JPQL이나 QueryDSL로 표현하기 어렵거나 DB 특화 기능이 필요한 경우에 검토한다.

Q. JOIN 후 row 수가 갑자기 늘어나는 이유는?
A. 1:N 관계 JOIN이거나 JOIN 조건이 잘못되어 하나의 row가 여러 row와 매칭되었을 수 있다.

Q. 쿼리가 느리면 무조건 Index를 추가하면 돼?
A. 아니다. 조건, JOIN, 정렬, 데이터 양, 실행 계획을 먼저 확인한 뒤 필요한 Index만 추가해야 한다.

Q. Full Table Scan은 항상 나빠?
A. 항상 나쁘지는 않다. 작은 Table이나 대부분의 Row가 필요한 경우에는 Full Scan이 자연스러울 수 있다.

Q. SQL 초보가 가장 많이 하는 실수는?
A. JOIN 조건 누락, WHERE 없는 UPDATE / DELETE, NULL 비교 오류, SELECT \* 남용, GROUP BY 결과 오해가 많다.

Q. SQL 문제는 어떻게 찾는 게 좋아?
A. Base Table부터 시작해 WHERE, JOIN, GROUP BY, ORDER BY를 단계적으로 추가하며 row 수와 결과를 확인한다.

Q. SQL 문서 검수에서 가장 중요한 것은?
A. Query Purpose, Table Relationship, JOIN 조건, WHERE 조건, Index 가능성, Transaction 필요 여부, Anti Pattern 포함 여부다.

Q. SQL Domain Rules 다음 문서는 뭐가 좋아?
A. JPA Advanced, QueryDSL Practical, API Design, Performance Tuning 문서와 연결되는 것이 좋다.
