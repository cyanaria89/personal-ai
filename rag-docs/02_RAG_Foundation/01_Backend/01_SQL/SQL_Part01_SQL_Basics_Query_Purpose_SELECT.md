# SQL Part01 - SQL Basics, Query Purpose, SELECT

---

# 1. SQL Foundation

## 1.1 SQL Purpose

### [개념]

SQL은 Relational Database에서 데이터를 조회, 생성, 수정, 삭제하기 위한 Query Language다.

Backend 개발에서 SQL은 단순 문법이 아니라 데이터 요구사항을 Table, Column, Relationship, Condition, Transaction 기준으로 변환하는 핵심 기준이다.

SQL 문서는 AI Agent가 아래 작업을 수행할 수 있도록 작성한다.

- 요구사항을 Query Purpose로 변환
- ERD / Entity Relationship 기준으로 Table 관계 파악
- SELECT / INSERT / UPDATE / DELETE 판단
- WHERE / JOIN / GROUP BY / HAVING / ORDER BY 설계
- Index / Transaction / Constraint 검토
- JPA / JPQL / QueryDSL / Native Query 연결 판단
- SQL Anti Pattern 감지

---

### [핵심]

SQL 핵심 목적:

- Data Retrieval
- Data Modification
- Data Aggregation
- Data Filtering
- Data Relationship Analysis
- Query Performance Review
- Data Integrity Review
- Backend Repository Support

SQL 우선순위:

1. Query Purpose
2. Table Relationship
3. Filtering
4. Join
5. Aggregation
6. Pagination
7. Index
8. Transaction
9. Constraint
10. Backend Integration

---

### [실무]

2026 Backend 실무 기준에서 SQL은 아래 흐름으로 사용한다.

```text
Requirement
→ Query Purpose
→ ERD / Entity Relationship
→ Target Table
→ Filtering Condition
→ Join Design
→ Sort / Pagination
→ Index Review
→ Repository / QueryDSL Mapping
→ Test / Review
```

SQL 작성 전 확인:

- 어떤 데이터를 조회 / 변경하는가?
- 기준 Table은 무엇인가?
- 관련 Table 관계는 무엇인가?
- 필요한 Column은 무엇인가?
- WHERE 조건은 무엇인가?
- JOIN이 필요한가?
- 정렬과 페이징이 필요한가?
- Index 사용 가능성이 있는가?
- Transaction이 필요한가?

---

### [FAQ]

Q. SQL은 단순히 DB 문법이야?
A. 아니다. Backend 요구사항을 데이터 조회, 변경, 집계, 성능 검토 기준으로 변환하는 핵심 설계 도구다.

Q. SQL 문서를 RAG용으로 만들 때 가장 중요한 것은?
A. Query Purpose, Table Relationship, Filtering, Join, Index, Transaction 기준을 검색 가능하게 분리하는 것이다.

Q. SQL 문서는 SQLD 시험용 문서야?
A. 아니다. Backend Agent가 실무 쿼리 작성과 검토를 수행하기 위한 RAG Retrieval 문서다.

Q. SQL을 알면 JPA나 QueryDSL은 필요 없어?
A. 아니다. JPA와 QueryDSL을 사용해도 실제 DB에서는 SQL이 실행되므로 SQL 이해가 필요하다.

---

## 1.2 SQL Command Types

### [개념]

SQL Command Type은 SQL 명령을 목적별로 구분하는 기준이다.

Backend Agent는 요구사항을 받으면 먼저 조회, 생성, 수정, 삭제, 집계, 존재 확인 중 어떤 작업인지 판단해야 한다.

---

### [핵심]

주요 SQL 명령:

- SELECT
- INSERT
- UPDATE
- DELETE
- CREATE
- ALTER
- DROP
- COMMIT
- ROLLBACK

Backend 실무 중심 명령:

- SELECT: 데이터 조회
- INSERT: 데이터 생성
- UPDATE: 데이터 수정
- DELETE: 데이터 삭제
- COMMIT: Transaction 확정
- ROLLBACK: Transaction 취소

---

### [실무]

Backend Service 요구사항은 SQL Command Type으로 먼저 분류한다.

```text
회원 상세 조회
→ SELECT

축제 목록 검색
→ SELECT + WHERE + ORDER BY + Pagination

리뷰 작성
→ INSERT

닉네임 변경
→ UPDATE

찜 취소
→ DELETE or Soft Delete

결제 성공 처리
→ INSERT + UPDATE + Transaction
```

권장:

- 조회는 SELECT 중심으로 설계
- 변경은 INSERT / UPDATE / DELETE 영향 범위 확인
- 변경 Query는 WHERE 조건과 Transaction 필요성 검토
- 운영 데이터 삭제는 Soft Delete 우선 검토
- 복수 Table 변경은 Transaction 단위로 판단

---

### [FAQ]

Q. Backend 요구사항을 받으면 SQL에서 가장 먼저 뭘 판단해?
A. SELECT, INSERT, UPDATE, DELETE 중 어떤 Query Purpose인지 먼저 판단한다.

Q. DELETE는 항상 실제 삭제로 처리해?
A. 아니다. 복구와 이력 관리가 필요하면 deleted_at, active 같은 Soft Delete를 검토한다.

Q. 여러 Table을 동시에 변경하면 어떻게 해야 해?
A. 하나의 성공 / 실패 단위로 묶어야 하므로 Transaction 적용을 검토한다.

Q. 조회 Query와 변경 Query는 검토 기준이 달라?
A. 다르다. 조회 Query는 조건, JOIN, Index를 우선 보고 변경 Query는 WHERE, 영향 Row, Transaction을 우선 본다.

---

# 2. Query Purpose

## 2.1 Query Purpose Definition

### [개념]

Query Purpose는 SQL을 작성하기 전에 해당 Query가 달성해야 할 목적을 정의하는 기준이다.

SQL은 문법보다 목적이 먼저다.

Query Purpose가 불명확하면 잘못된 Table 선택, 불필요한 JOIN, 과도한 데이터 조회, 성능 저하가 발생할 수 있다.

---

### [핵심]

Query Purpose 유형:

- 단건 조회
- 목록 조회
- 조건 검색
- 기간 검색
- 통계 조회
- 존재 여부 확인
- 중복 여부 확인
- 데이터 생성
- 데이터 수정
- 데이터 삭제
- 페이징 조회
- 권한 기반 조회
- 정렬 조회

---

### [실무]

Query Purpose 판단 Flow:

```text
요구사항 확인
→ 조회 / 변경 / 집계 구분
→ 단건 / 목록 / 검색 구분
→ 대상 Table 확인
→ 관계 Table 확인
→ 조건 확인
→ 정렬 / 페이징 확인
→ 성능 검토
```

예시:

```text
"사용자가 찜한 축제 목록"
→ 목록 조회
→ users, favorites, festivals
→ user_id 조건
→ festival 시작일 정렬
→ user_id Index 검토
```

예시:

```text
"이 이메일로 가입한 회원이 있는지 확인"
→ 존재 여부 확인
→ users
→ email 조건
→ Unique Constraint 검토
→ exists Query 검토
```

---

### [FAQ]

Q. SQL 작성 전에 가장 먼저 확인할 것은?
A. Query Purpose다. 단건 조회인지 목록 조회인지 집계인지 변경 Query인지 먼저 구분해야 한다.

Q. Query Purpose가 불명확하면 어떤 문제가 생겨?
A. 불필요한 JOIN, 잘못된 조건, 과도한 데이터 조회, 성능 저하가 발생할 수 있다.

Q. 단건 조회와 목록 조회는 왜 구분해야 해?
A. 단건 조회는 PK / Unique 조건이 중요하고 목록 조회는 정렬, 페이징, Index 검토가 중요하기 때문이다.

Q. 존재 여부 확인은 SELECT 목록 조회와 같아?
A. 아니다. 전체 데이터를 가져오기보다 EXISTS 또는 COUNT 기반으로 존재 여부만 확인하는 것이 적합하다.

---

## 2.2 Query Purpose Classification

### [개념]

Query Purpose Classification은 요구사항을 SQL 작성 가능한 유형으로 분류하는 작업이다.

AI Agent는 자연어 요구사항을 그대로 Query로 만들지 않고 목적, Table, 조건, 결과 형태로 분해해야 한다.

---

### [핵심]

분류 기준:

| 요구사항 유형    | Query Purpose | 주요 SQL                   |
| ---------------- | ------------- | -------------------------- |
| 회원 상세 조회   | 단건 조회     | SELECT + WHERE             |
| 축제 목록        | 목록 조회     | SELECT + ORDER BY          |
| 축제 검색        | 조건 검색     | SELECT + WHERE             |
| 월별 축제        | 기간 검색     | SELECT + Date Range        |
| 축제별 리뷰 수   | 통계 조회     | GROUP BY + COUNT           |
| 이메일 중복 확인 | 존재 확인     | EXISTS / COUNT             |
| 리뷰 작성        | 데이터 생성   | INSERT                     |
| 프로필 수정      | 데이터 수정   | UPDATE                     |
| 찜 취소          | 데이터 삭제   | DELETE                     |
| 무한 스크롤      | 페이징 조회   | Cursor / Keyset Pagination |

---

### [실무]

Query Purpose별 확인 항목:

단건 조회:

- PK / Unique 조건 여부
- 결과 Row 1개 보장 여부
- Not Found 처리 여부

목록 조회:

- 정렬 기준
- Pagination 필요 여부
- Filter 조건
- Index 가능성

조건 검색:

- 검색 Column
- LIKE / Equal / Range 조건
- Dynamic Query 필요 여부
- QueryDSL 적용 가능성

통계 조회:

- GROUP BY 기준
- COUNT / SUM / AVG
- HAVING 조건
- 중복 JOIN 여부

변경 Query:

- WHERE 조건
- 영향 Row 수
- Transaction 필요 여부
- Constraint 위반 가능성

---

### [FAQ]

Q. 목록 조회에서 가장 중요한 것은?
A. WHERE 조건, ORDER BY, Pagination, Index 가능성을 함께 검토하는 것이다.

Q. 단건 조회는 무엇으로 찾는 게 좋아?
A. PK 또는 Unique Column 기준으로 조회하는 것이 가장 명확하다.

Q. 검색 Query는 왜 QueryDSL과 연결돼?
A. 검색 조건이 동적으로 조합되는 경우 QueryDSL이 Type-safe 방식으로 조건을 구성하기 좋기 때문이다.

Q. 통계 Query는 무엇을 먼저 정해야 해?
A. 어떤 기준으로 그룹화할지 GROUP BY 기준을 먼저 정해야 한다.

---

# 3. Table Relationship Basics

## 3.1 Table and Column

### [개념]

Table은 관계형 데이터베이스에서 데이터를 저장하는 기본 단위다.

Column은 Table이 저장하는 속성이고 Row는 실제 데이터 한 건이다.

SQL Query는 Table, Column, Row의 구조를 기준으로 작성된다.

---

### [핵심]

기본 용어:

- Table
- Column
- Row
- Primary Key
- Foreign Key
- Unique
- Not Null
- Default
- Index

Table 설계 확인 기준:

- 기준 Table
- 조회 Column
- 조건 Column
- 정렬 Column
- Join Column
- Constraint Column

---

### [실무]

Query 작성 전 Table 구조를 먼저 확인한다.

```text
Requirement
→ Target Data
→ Target Table
→ Required Column
→ Condition Column
→ Relationship Column
→ Output Format
```

예시:

```sql
SELECT user_id, email, nickname
FROM users
WHERE user_id = 1;
```

해석:

```text
Target Table: users
Required Column: user_id, email, nickname
Condition Column: user_id
Query Purpose: 회원 단건 조회
```

주의:

- 필요한 Column만 SELECT
- 조건에 사용하는 Column 확인
- FK 관계 확인 후 JOIN
- Column 타입과 비교 값 타입 일치
- Nullable Column은 NULL 처리 검토

---

### [FAQ]

Q. SQL 작성 전에 Table 구조를 왜 봐야 해?
A. 기준 Table, 필요한 Column, 조건 Column, JOIN 관계가 Query 결과와 성능을 결정하기 때문이다.

Q. Column 타입을 확인해야 하는 이유는?
A. 타입이 맞지 않으면 암시적 형변환이 발생하거나 Index 사용이 어려워질 수 있다.

Q. Nullable Column은 왜 주의해야 해?
A. NULL은 일반 비교 연산으로 처리되지 않으므로 IS NULL 또는 IS NOT NULL 조건이 필요할 수 있다.

Q. 필요한 Column만 SELECT해야 하는 이유는?
A. 불필요한 데이터 전송과 메모리 사용을 줄이고 Query 의도를 명확히 하기 위해서다.

---

## 3.2 Primary Key and Foreign Key

### [개념]

Primary Key는 Table의 각 Row를 고유하게 식별하는 Column이다.

Foreign Key는 다른 Table의 Primary Key를 참조하여 Table 간 Relationship을 표현하는 Column이다.

PK와 FK는 JOIN 설계와 데이터 무결성 검토의 기준이다.

---

### [핵심]

Primary Key:

- Row 식별자
- Unique
- Not Null
- 단건 조회 기준
- JOIN 참조 대상

Foreign Key:

- Table Relationship 표현
- Parent Table 참조
- Child Table에 위치
- JOIN 조건 기준
- 데이터 무결성 기준

---

### [실무]

PK / FK 기반 JOIN 예시:

```sql
SELECT fav.favorite_id, f.festival_id, f.title
FROM favorites fav
JOIN festivals f ON fav.festival_id = f.festival_id
WHERE fav.user_id = 1;
```

해석:

```text
favorites.festival_id
→ festivals.festival_id 참조
→ 사용자가 찜한 축제 목록 조회
```

PK / FK 확인 Flow:

```text
조회 대상 Entity 확인
→ 기준 Table 선택
→ FK 방향 확인
→ Parent / Child Table 구분
→ JOIN 필요 여부 확인
→ 중복 Row 발생 가능성 확인
```

주의:

- FK가 있다고 항상 JOIN이 필요한 것은 아님
- FK가 없더라도 논리적 관계가 있을 수 있음
- 1:N JOIN은 Row 수 증가 가능
- N:M 관계는 Join Table 확인 필요

---

### [FAQ]

Q. JOIN을 설계할 때 가장 먼저 볼 것은?
A. ERD에서 PK와 FK 관계를 확인하고 기준 Table과 JOIN 방향을 정해야 한다.

Q. Primary Key는 언제 주로 사용해?
A. 단건 조회, 수정, 삭제, JOIN 참조 기준으로 사용한다.

Q. Foreign Key는 왜 중요해?
A. Table 간 관계를 나타내며 JOIN 조건과 데이터 무결성 검토 기준이 되기 때문이다.

Q. 1:N JOIN에서 주의할 점은?
A. 부모 Row가 자식 Row 수만큼 중복될 수 있으므로 결과 Row 수를 반드시 확인해야 한다.

---

# 4. SELECT Query Basics

## 4.1 SELECT Structure

### [개념]

SELECT는 Table에서 필요한 Column과 Row를 조회하는 SQL 명령이다.

실무 Query에서는 필요한 Column만 조회하고, WHERE 조건과 ORDER BY 기준을 명확히 작성한다.

---

### [핵심]

SELECT 구성 요소:

- SELECT
- FROM
- WHERE
- GROUP BY
- HAVING
- ORDER BY
- LIMIT
- OFFSET
- Column Alias
- Table Alias

기본 형태:

```sql
SELECT column1, column2
FROM table_name
WHERE condition
ORDER BY column1 DESC;
```

---

### [실무]

기본 예시:

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
- 날짜 조회는 범위 조건 고려
- 조회 목적에 맞는 Column Alias 사용

주의:

- SELECT \* 지양
- 불필요한 Column 조회 금지
- 정렬 없는 Pagination 지양
- 대량 데이터 전체 조회 금지
- WHERE 조건 없는 전체 조회 주의

---

### [FAQ]

Q. SELECT \*를 써도 돼?
A. 테스트나 임시 조회는 가능하지만 실무 Query와 RAG 예제에서는 필요한 Column만 명시하는 것이 좋다.

Q. 목록 조회에서 ORDER BY가 필요한 이유는?
A. 정렬 기준이 없으면 페이지 이동 시 결과 순서가 불안정할 수 있기 때문이다.

Q. SELECT Query에서 FROM은 왜 중요해?
A. 기준 Table을 결정하므로 Query 결과 범위와 JOIN 방향에 영향을 준다.

Q. Column Alias는 언제 사용해?
A. 집계 결과, 계산 결과, DTO Projection처럼 출력 이름을 명확히 해야 할 때 사용한다.

---

## 4.2 SELECT Column Rules

### [개념]

SELECT Column Rules는 Query 결과에 포함할 Column을 선택하는 기준이다.

SELECT Column은 API Response, DTO Projection, 화면 출력, Repository 반환 타입과 연결된다.

---

### [핵심]

Column 선택 기준:

- API Response에 필요한 값
- DTO에 필요한 값
- 검색 결과 목록에 필요한 값
- 상세 화면에 필요한 값
- 정렬 / 필터에 필요한 값
- 집계 결과에 필요한 값

권장:

- 필요한 Column만 명시
- Column 출처 명확화
- Alias 사용
- 민감 정보 제외
- 대용량 Text / Blob Column 제외 검토

---

### [실무]

목록 조회 예시:

```sql
SELECT festival_id, title, event_start_date, event_end_date
FROM festivals
WHERE active = true
ORDER BY event_start_date ASC;
```

상세 조회 예시:

```sql
SELECT festival_id, title, content, address, event_start_date, event_end_date
FROM festivals
WHERE festival_id = 10;
```

DTO Projection 기준:

```text
List Response
→ id, title, thumbnail, summary, startDate

Detail Response
→ id, title, content, images, address, location, startDate, endDate
```

주의:

- 목록 조회에 상세 본문 전체를 포함하지 않음
- password, token, secret 같은 민감 정보 조회 금지
- SELECT Column과 DTO Field 불일치 주의
- JOIN 시 동일 Column 이름은 Alias로 구분

---

### [FAQ]

Q. 목록 조회와 상세 조회의 SELECT Column은 같아야 해?
A. 아니다. 목록 조회는 최소 Column 중심이고 상세 조회는 상세 화면에 필요한 Column을 포함한다.

Q. 민감 정보도 SELECT해서 Service에서 제거하면 돼?
A. 권장하지 않는다. 필요한 Column만 조회하고 password, token, secret은 Query 단계에서 제외하는 것이 좋다.

Q. DTO Projection과 SELECT Column은 왜 연결돼?
A. Query 결과가 DTO 필드에 매핑되므로 필요한 Column과 Alias를 명확히 맞춰야 한다.

Q. JOIN Query에서 Column 이름이 겹치면 어떻게 해?
A. Table Alias와 Column Alias를 사용해 출처와 출력 이름을 명확히 한다.

---

## 4.3 Table Alias and Column Alias

### [개념]

Alias는 SQL에서 Table 또는 Column에 임시 이름을 부여하는 기능이다.

Table Alias는 JOIN Query 가독성을 높이고 Column Alias는 결과 Column 이름을 명확히 한다.

---

### [핵심]

Alias 유형:

- Table Alias
- Column Alias
- Aggregation Alias
- DTO Projection Alias
- Subquery Alias

예시:

```sql
SELECT u.user_id AS userId,
       u.nickname AS nickname
FROM users u
WHERE u.active = true;
```

---

### [실무]

JOIN Query에서는 Table Alias를 적극 사용한다.

```sql
SELECT r.review_id AS reviewId,
       r.content AS content,
       u.nickname AS writerName
FROM reviews r
JOIN users u ON r.user_id = u.user_id
WHERE r.festival_id = 10;
```

권장:

- 짧고 의미 있는 Alias 사용
- 동일 Column 이름 충돌 방지
- DTO Field 이름과 Alias 일치
- Aggregation 결과에는 Alias 필수 권장
- 복잡한 Query에서 Column 출처 명확화

주의:

- 과도하게 짧거나 의미 없는 Alias 지양
- Alias 혼용 금지
- WHERE에서 SELECT Alias 사용 가능 여부는 DBMS별 차이 주의

---

### [FAQ]

Q. Table Alias를 쓰는 이유는?
A. Column 출처를 명확히 하고 JOIN Query의 가독성과 유지보수성을 높이기 위해서다.

Q. Column Alias는 언제 필요해?
A. DTO 매핑, 집계 결과, 동일 Column 이름 충돌 방지, API 응답 이름 정리에 필요하다.

Q. Alias 이름은 어떻게 정하는 게 좋아?
A. Table은 짧고 일관되게, Column은 DTO Field나 의미 중심으로 정하는 것이 좋다.

Q. WHERE에서 SELECT Alias를 사용할 수 있어?
A. DBMS에 따라 제한될 수 있으므로 WHERE에서는 원본 Column 기준으로 작성하는 것이 안전하다.

---

# 5. SQL Logical Execution Order

## 5.1 Logical Execution Order

### [개념]

SQL Logical Execution Order는 SQL이 논리적으로 처리되는 순서다.

SQL 작성 순서와 논리 실행 순서는 다르다.

Agent가 SQL을 해석하거나 검토할 때는 논리 실행 순서 기준으로 조건과 결과를 판단해야 한다.

---

### [핵심]

SQL 작성 순서:

```text
SELECT
FROM
JOIN
WHERE
GROUP BY
HAVING
ORDER BY
LIMIT
```

SQL 논리 실행 순서:

```text
FROM
→ JOIN
→ WHERE
→ GROUP BY
→ HAVING
→ SELECT
→ ORDER BY
→ LIMIT / OFFSET
```

---

### [실무]

논리 실행 순서 기준 해석:

```sql
SELECT festival_id, COUNT(*) AS review_count
FROM reviews
WHERE rating >= 4
GROUP BY festival_id
HAVING COUNT(*) >= 10
ORDER BY review_count DESC;
```

해석:

```text
FROM reviews
→ rating >= 4 Row 필터링
→ festival_id 기준 그룹화
→ COUNT(*) >= 10 그룹 필터링
→ festival_id, review_count 선택
→ review_count 기준 정렬
```

주의:

- WHERE에서는 집계 결과 사용 불가
- HAVING은 GROUP BY 이후 사용
- SELECT Alias는 WHERE에서 직접 사용이 제한될 수 있음
- ORDER BY는 최종 결과 정렬
- LIMIT은 최종 결과 개수 제한

---

### [FAQ]

Q. SQL은 SELECT부터 실행돼?
A. 논리적으로는 FROM과 JOIN이 먼저 처리되고 WHERE, GROUP BY, HAVING 이후 SELECT가 처리된다.

Q. SQL 논리 실행 순서는?
A. FROM, JOIN, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT 순서로 이해한다.

Q. WHERE에서 집계 함수를 쓰면 안 되는 이유는?
A. WHERE는 GROUP BY 이전에 실행되므로 집계 결과가 아직 존재하지 않기 때문이다.

Q. ORDER BY는 언제 처리돼?
A. SELECT 결과가 만들어진 뒤 최종 결과를 정렬하는 단계에서 처리된다.

---

## 5.2 WHERE and HAVING Position

### [개념]

WHERE는 그룹화 전 Row를 필터링하고 HAVING은 GROUP BY 이후 집계 결과를 필터링한다.

WHERE와 HAVING은 SQL Logical Execution Order를 이해해야 정확히 사용할 수 있다.

---

### [핵심]

비교:

| 비교           | WHERE            | HAVING           |
| -------------- | ---------------- | ---------------- |
| 적용 시점      | GROUP BY 전      | GROUP BY 후      |
| 대상           | 개별 Row         | 집계 결과        |
| 집계 함수 조건 | 일반적으로 불가  | 가능             |
| 주요 목적      | 데이터 범위 축소 | 그룹 결과 필터링 |
| 예시           | rating >= 4      | COUNT(\*) >= 10  |

---

### [실무]

예시:

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

권장:

- 개별 Row 조건은 WHERE
- 집계 결과 조건은 HAVING
- 성능상 가능한 조건은 WHERE에서 먼저 줄임
- HAVING을 WHERE 대체용으로 남용하지 않음

---

### [FAQ]

Q. WHERE와 HAVING 차이는?
A. WHERE는 그룹화 전 Row 필터링이고 HAVING은 GROUP BY 이후 집계 결과 필터링이다.

Q. WHERE와 HAVING을 같이 쓸 수 있어?
A. 가능하다. WHERE는 집계 전 데이터 범위를 줄이고 HAVING은 집계 후 결과를 필터링한다.

Q. 집계 조건은 WHERE에 쓰면 안 돼?
A. 집계 함수 결과 조건은 HAVING에 작성해야 한다.

Q. HAVING만 쓰면 안 좋아?
A. Row 조건을 HAVING으로 처리하면 불필요하게 많은 데이터를 그룹화할 수 있어 성능상 불리할 수 있다.

---

# 6. Basic Filtering

## 6.1 WHERE Basics

### [개념]

WHERE는 SELECT, UPDATE, DELETE에서 대상 Row를 제한하는 조건절이다.

Filtering은 필요한 데이터만 조회하거나 변경하기 위한 핵심 작업이다.

---

### [핵심]

WHERE 조건 유형:

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

기본 예시:

```sql
SELECT user_id, email
FROM users
WHERE active = true;
```

---

### [실무]

조건 검색 예시:

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
- NULL 비교는 IS NULL 사용
- OR 조건은 성능 영향 검토
- LIKE 앞쪽 wildcard 주의
- Column 타입과 비교 값 타입 일치

주의:

```sql
-- 잘못된 NULL 비교
WHERE deleted_at = NULL;

-- 올바른 NULL 비교
WHERE deleted_at IS NULL;
```

---

### [FAQ]

Q. WHERE는 언제 사용해?
A. 필요한 Row만 조회, 수정, 삭제하기 위해 조건을 제한할 때 사용한다.

Q. NULL은 = NULL로 비교해도 돼?
A. 안 된다. NULL 비교는 IS NULL 또는 IS NOT NULL을 사용해야 한다.

Q. 날짜 검색은 어떻게 작성하는 게 좋아?
A. YEAR(column) 같은 함수보다 시작일 이상, 다음 기간 미만의 범위 조건을 사용하는 것이 좋다.

Q. WHERE 조건은 성능과 관련 있어?
A. 관련 있다. WHERE 조건 Column이 Index와 연결될 수 있기 때문에 성능 검토의 핵심이다.

---

## 6.2 AND, OR, IN

### [개념]

AND, OR, IN은 WHERE 조건을 조합하는 연산자다.

조건 조합 방식에 따라 Query 결과와 성능이 달라질 수 있다.

---

### [핵심]

조건 연산자:

- AND: 모든 조건 만족
- OR: 하나 이상의 조건 만족
- IN: 목록 중 하나와 일치
- NOT IN: 목록에 포함되지 않음
- Parentheses: 조건 우선순위 명확화

---

### [실무]

AND 예시:

```sql
SELECT festival_id, title
FROM festivals
WHERE region_code = '11'
  AND active = true;
```

OR 예시:

```sql
SELECT festival_id, title
FROM festivals
WHERE region_code = '11'
   OR region_code = '26';
```

IN 예시:

```sql
SELECT festival_id, title
FROM festivals
WHERE region_code IN ('11', '26', '27');
```

권장:

- OR보다 IN이 더 명확한 경우 IN 사용
- AND / OR 혼합 시 괄호 사용
- NOT IN은 NULL 포함 가능성 주의
- 조건 조합이 많으면 Dynamic Query 검토
- QueryDSL BooleanBuilder 또는 BooleanExpression 조합 검토

주의:

```sql
-- 의도 불명확
WHERE active = true
  AND region_code = '11'
   OR region_code = '26';

-- 의도 명확
WHERE active = true
  AND (region_code = '11' OR region_code = '26');
```

---

### [FAQ]

Q. AND와 OR를 같이 쓰면 왜 괄호가 필요해?
A. 조건 우선순위 때문에 의도와 다른 결과가 나올 수 있으므로 괄호로 명확히 표현해야 한다.

Q. OR와 IN은 언제 골라?
A. 같은 Column이 여러 값 중 하나와 일치하는 조건이면 IN이 더 명확한 경우가 많다.

Q. NOT IN은 왜 조심해야 해?
A. 비교 목록이나 Subquery 결과에 NULL이 포함되면 예상과 다른 결과가 나올 수 있다.

Q. 조건이 많아지면 어떻게 관리해?
A. Backend에서는 QueryDSL 같은 동적 Query 도구로 조건 조합을 관리하는 것이 좋다.

---

# 7. Basic Sorting and Limiting

## 7.1 ORDER BY Basics

### [개념]

ORDER BY는 SELECT 결과의 정렬 기준을 지정하는 절이다.

목록 조회와 Pagination에서는 ORDER BY가 결과 안정성을 결정한다.

---

### [핵심]

정렬 방향:

- ASC
- DESC

정렬 기준:

- created_at
- updated_at
- id
- name
- start_date
- count result
- score
- priority

---

### [실무]

기본 정렬:

```sql
SELECT festival_id, title, event_start_date
FROM festivals
WHERE active = true
ORDER BY event_start_date ASC;
```

최신순 정렬:

```sql
SELECT post_id, title, created_at
FROM posts
ORDER BY created_at DESC, post_id DESC;
```

권장:

- 정렬 기준 명확화
- 중복 가능한 정렬 값에는 PK 추가
- Pagination Query는 ORDER BY 필수
- Index와 ORDER BY 연계 검토
- API 정렬 옵션은 허용된 Column만 사용

주의:

- ORDER BY 없는 목록 조회 지양
- 문자열 정렬은 Collation 영향 가능
- 대량 정렬은 성능 비용 발생
- 사용자 입력을 ORDER BY Column에 직접 연결 금지

---

### [FAQ]

Q. ORDER BY는 왜 필요해?
A. 목록 결과 순서를 명확히 하고 Pagination 결과가 흔들리지 않게 하기 위해 필요하다.

Q. created_at만 정렬하면 충분해?
A. created_at이 중복될 수 있으므로 안정적인 정렬을 위해 PK를 추가 정렬 기준으로 두는 것이 좋다.

Q. ORDER BY는 성능에 영향이 있어?
A. 있다. 대량 데이터 정렬은 비용이 크며 Index 설계와 함께 검토해야 한다.

Q. 사용자가 정렬 Column을 직접 보내면 그대로 써도 돼?
A. 안 된다. 허용된 정렬 Column만 매핑해서 SQL Injection과 잘못된 정렬을 방지해야 한다.

---

## 7.2 LIMIT and OFFSET Basics

### [개념]

LIMIT은 조회할 Row 개수를 제한하고 OFFSET은 앞에서 건너뛸 Row 개수를 지정한다.

Pagination은 목록 데이터를 일정 단위로 나누어 조회하는 방식이다.

---

### [핵심]

Pagination 구성:

- LIMIT
- OFFSET
- ORDER BY
- Page Size
- Page Number
- Stable Sort

기본 예시:

```sql
SELECT festival_id, title
FROM festivals
ORDER BY created_at DESC
LIMIT 20 OFFSET 40;
```

---

### [실무]

OFFSET Pagination 예시:

```sql
SELECT festival_id, title, created_at
FROM festivals
WHERE active = true
ORDER BY created_at DESC, festival_id DESC
LIMIT 20 OFFSET 40;
```

해석:

```text
active = true 데이터
→ created_at DESC, festival_id DESC 정렬
→ 앞 40개 건너뜀
→ 20개 조회
```

권장:

- Pagination에는 ORDER BY 필수
- Page Size 제한
- 중복 정렬 값에는 PK 추가
- OFFSET이 커지면 Cursor Pagination 검토
- 무한 스크롤은 Cursor / Keyset Pagination 검토

주의:

- ORDER BY 없는 LIMIT 지양
- 큰 OFFSET은 성능 저하 가능
- 전체 Count Query 비용 검토
- Fetch Join + Pagination 조합 주의

---

### [FAQ]

Q. Pagination에서 ORDER BY가 왜 필수야?
A. 정렬 기준이 없으면 페이지마다 결과 순서가 흔들릴 수 있기 때문이다.

Q. OFFSET Pagination은 언제 문제가 돼?
A. OFFSET 값이 커지면 앞 데이터를 많이 건너뛰어야 해서 성능이 떨어질 수 있다.

Q. 무한 스크롤에는 어떤 Pagination이 좋아?
A. Cursor Pagination 또는 Keyset Pagination을 검토하는 것이 좋다.

Q. LIMIT만 쓰면 안전해?
A. 아니다. ORDER BY 없이 LIMIT만 사용하면 어떤 Row가 선택될지 안정적이지 않을 수 있다.

---

# 8. SQL Basics Review Checklist

## 8.1 Query Review Checklist

### [개념]

SQL Basics Review Checklist는 Part01 수준의 Query를 검토할 때 사용하는 기본 점검 기준이다.

Query Purpose, Table, Column, WHERE, ORDER BY, LIMIT 기준을 먼저 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] Query Purpose가 명확한가?
- [ ] SELECT / INSERT / UPDATE / DELETE 목적이 구분되었는가?
- [ ] 기준 Table이 명확한가?
- [ ] 필요한 Column만 SELECT하는가?
- [ ] 민감 정보 Column을 제외했는가?
- [ ] WHERE 조건이 명확한가?
- [ ] NULL 비교를 IS NULL / IS NOT NULL로 처리했는가?
- [ ] AND / OR 조건에 괄호가 필요한가?
- [ ] ORDER BY 기준이 명확한가?
- [ ] Pagination Query에 ORDER BY가 있는가?
- [ ] LIMIT / OFFSET 사용 시 성능 한계를 고려했는가?
- [ ] PK / FK 관계를 확인했는가?
- [ ] DTO Projection과 Column Alias가 일치하는가?
```

---

### [실무]

검수 Flow:

```text
Draft Query
→ Query Purpose Check
→ Table Check
→ Column Check
→ WHERE Check
→ Sort Check
→ Pagination Check
→ Alias Check
→ Backend DTO Mapping Check
→ Final Review
```

기초 Query에서 치명적 문제:

- Query Purpose 불명확
- SELECT \* 남용
- WHERE 조건 누락
- NULL 비교 오류
- AND / OR 우선순위 오류
- ORDER BY 없는 Pagination
- 민감 정보 조회
- 잘못된 기준 Table 선택

---

### [FAQ]

Q. SQL 기초 Query 검수에서 가장 중요한 것은?
A. Query Purpose, 기준 Table, 필요한 Column, WHERE 조건, ORDER BY, Pagination 안정성을 확인하는 것이다.

Q. SELECT \*는 왜 Checklist에 포함돼?
A. 불필요한 Column 조회와 민감 정보 노출 위험이 있기 때문이다.

Q. ORDER BY 없는 Pagination은 왜 치명적이야?
A. 페이지 이동 시 결과 순서가 불안정해 중복 또는 누락 Row가 발생할 수 있기 때문이다.

Q. SQL Query 검수는 어디서 시작해?
A. Query Purpose와 기준 Table 확인에서 시작한다.

---

# Retrieval Queries

### [FAQ]

Q. SQL Part01은 무엇을 다뤄?
A. SQL 기본 목적, Query Purpose, Table Relationship, SELECT 구조, WHERE 기초, ORDER BY, LIMIT, OFFSET 기준을 다룬다.

Q. SQL은 왜 Backend Agent에게 필요해?
A. Backend Agent가 요구사항을 데이터 조회, 변경, 집계, 성능 검토 기준으로 변환해야 하기 때문이다.

Q. SQL 작성 전에 가장 먼저 확인할 것은?
A. Query Purpose다. 단건 조회, 목록 조회, 검색, 집계, 생성, 수정, 삭제 중 무엇인지 먼저 구분한다.

Q. Query Purpose가 뭐야?
A. Query가 달성해야 할 목적을 정의하는 기준이다.

Q. Query Purpose가 불명확하면 어떤 문제가 생겨?
A. 잘못된 Table 선택, 불필요한 JOIN, 과도한 데이터 조회, 성능 저하가 발생할 수 있다.

Q. SQL Command Type은 뭐가 있어?
A. SELECT, INSERT, UPDATE, DELETE, COMMIT, ROLLBACK 등이 있다.

Q. SELECT는 언제 사용해?
A. Table에서 필요한 Column과 Row를 조회할 때 사용한다.

Q. INSERT는 언제 사용해?
A. Table에 새로운 Row를 생성할 때 사용한다.

Q. UPDATE는 언제 사용해?
A. 기존 Row의 값을 수정할 때 사용한다.

Q. DELETE는 언제 사용해?
A. 기존 Row를 삭제할 때 사용하지만 운영 데이터는 Soft Delete를 우선 검토한다.

Q. Table은 뭐야?
A. 관계형 데이터베이스에서 데이터를 저장하는 기본 단위다.

Q. Column은 뭐야?
A. Table이 저장하는 데이터 속성이다.

Q. Row는 뭐야?
A. Table에 저장된 실제 데이터 한 건이다.

Q. Primary Key는 뭐야?
A. Table의 각 Row를 고유하게 식별하는 Column이다.

Q. Foreign Key는 뭐야?
A. 다른 Table의 Primary Key를 참조하여 Table 간 관계를 표현하는 Column이다.

Q. JOIN을 설계할 때 가장 먼저 볼 것은?
A. ERD에서 PK와 FK 관계를 확인하고 기준 Table과 JOIN 방향을 정해야 한다.

Q. SELECT \*를 써도 돼?
A. 테스트나 임시 조회는 가능하지만 실무 Query와 RAG 예제에서는 필요한 Column만 명시하는 것이 좋다.

Q. 목록 조회와 상세 조회의 SELECT Column은 같아야 해?
A. 아니다. 목록 조회는 최소 Column 중심이고 상세 조회는 상세 화면에 필요한 Column을 포함한다.

Q. 민감 정보도 SELECT해도 돼?
A. 아니다. password, token, secret 같은 민감 정보는 Query 단계에서 제외하는 것이 좋다.

Q. Table Alias는 왜 써?
A. Column 출처를 명확히 하고 JOIN Query 가독성과 유지보수성을 높이기 위해 사용한다.

Q. Column Alias는 왜 써?
A. DTO 매핑, 집계 결과, 동일 Column 이름 충돌 방지, API 응답 이름 정리에 사용한다.

Q. SQL은 SELECT부터 실행돼?
A. 논리적으로는 FROM과 JOIN이 먼저 처리되고 WHERE, GROUP BY, HAVING 이후 SELECT가 처리된다.

Q. SQL 논리 실행 순서는?
A. FROM, JOIN, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT 순서로 이해한다.

Q. WHERE는 언제 사용해?
A. 필요한 Row만 조회, 수정, 삭제하기 위해 조건을 제한할 때 사용한다.

Q. WHERE와 HAVING 차이는?
A. WHERE는 그룹화 전 Row 필터링이고 HAVING은 GROUP BY 이후 집계 결과 필터링이다.

Q. NULL은 = NULL로 비교해도 돼?
A. 안 된다. NULL 비교는 IS NULL 또는 IS NOT NULL을 사용해야 한다.

Q. 날짜 검색은 어떻게 작성하는 게 좋아?
A. YEAR(column)보다 시작일 이상, 다음 기간 미만의 범위 조건을 사용하는 것이 좋다.

Q. AND와 OR를 같이 쓰면 왜 괄호가 필요해?
A. 조건 우선순위 때문에 의도와 다른 결과가 나올 수 있으므로 괄호로 명확히 표현해야 한다.

Q. OR와 IN은 언제 골라?
A. 같은 Column이 여러 값 중 하나와 일치하는 조건이면 IN이 더 명확한 경우가 많다.

Q. ORDER BY는 왜 필요해?
A. 목록 결과 순서를 명확히 하고 Pagination 결과가 흔들리지 않게 하기 위해 필요하다.

Q. Pagination에서 ORDER BY가 왜 필수야?
A. 정렬 기준이 없으면 페이지마다 결과 순서가 흔들릴 수 있기 때문이다.

Q. LIMIT은 뭐야?
A. 조회할 Row 개수를 제한하는 SQL 절이다.

Q. OFFSET은 뭐야?
A. 조회 결과에서 앞의 Row를 일정 개수만큼 건너뛰는 SQL 절이다.

Q. OFFSET Pagination은 언제 문제가 돼?
A. OFFSET 값이 커지면 앞 데이터를 많이 건너뛰어야 해서 성능이 떨어질 수 있다.

Q. 무한 스크롤에는 어떤 Pagination이 좋아?
A. Cursor Pagination 또는 Keyset Pagination을 검토하는 것이 좋다.

Q. SQL 기초 Query 검수에서 가장 중요한 것은?
A. Query Purpose, 기준 Table, 필요한 Column, WHERE 조건, ORDER BY, Pagination 안정성을 확인하는 것이다.
