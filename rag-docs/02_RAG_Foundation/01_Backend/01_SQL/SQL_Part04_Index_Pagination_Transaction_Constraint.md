# SQL Part04 - Index, Pagination, Transaction, Constraint

---

# 1. Index Foundation

## 1.1 Index Purpose

### [개념]

Index는 Table에서 특정 Column 기준으로 Row를 빠르게 찾기 위한 자료구조다.

SQL Query에서 Index는 WHERE, JOIN, ORDER BY, GROUP BY, Pagination 성능과 직접 연결된다.

Index는 조회 성능을 높일 수 있지만 INSERT, UPDATE, DELETE 비용과 저장 공간 비용을 증가시킬 수 있다.

Index는 Query Purpose와 실제 Query Pattern을 기준으로 설계한다.

---

### [핵심]

Index 사용 후보:

- WHERE Column
- JOIN Column
- ORDER BY Column
- GROUP BY Column
- Foreign Key Column
- Unique Column
- High Selectivity Column
- Pagination Cursor Column
- Search Condition Column
- Soft Delete Filter Column

Index 검토 기준:

- Query Purpose
- Query Frequency
- Selectivity
- Cardinality
- Data Size
- Write Cost
- Composite Index Order
- Execution Plan
- Repository Query Pattern
- JPA / QueryDSL 생성 SQL

---

### [실무]

2026 Backend 실무 기준에서 Index는 Query를 먼저 확인한 뒤 설계한다.

```text
Slow Query
→ Query Purpose 확인
→ WHERE Column 확인
→ JOIN Column 확인
→ ORDER BY / GROUP BY 확인
→ Pagination 방식 확인
→ Cardinality 확인
→ Composite Index 순서 검토
→ Execution Plan 확인
→ Index 추가 여부 결정
```

단일 Index 예시:

```sql
CREATE INDEX idx_favorites_user_id
ON favorites (user_id);
```

복합 Index 예시:

```sql
CREATE INDEX idx_festivals_region_start_date
ON festivals (region_code, event_start_date);
```

JPA / QueryDSL 연계:

```text
Repository Method
→ 생성 SQL 확인
→ WHERE / JOIN / ORDER BY Column 확인
→ Index 후보 검토
→ Execution Plan 확인
```

주의:

- Index는 많을수록 좋은 것이 아님
- 쓰기 성능 저하 가능
- 저장 공간 증가
- 낮은 선택도 Column은 단독 Index 효과 제한
- Query 없이 추측으로 Index 추가 금지
- JPA Repository Method 이름만 보고 Index를 만들지 말고 실제 생성 SQL 확인

---

### [FAQ]

Q. Index는 언제 만들어?
A. 자주 조회 조건, JOIN 조건, 정렬 조건으로 사용되는 Column에 대해 성능 문제가 있거나 예상될 때 검토한다.

Q. Index를 많이 만들면 좋아?
A. 아니다. INSERT, UPDATE, DELETE 비용과 저장 공간이 증가하므로 필요한 Index만 만들어야 한다.

Q. Index는 WHERE에만 관련 있어?
A. 아니다. JOIN, ORDER BY, GROUP BY, Pagination 성능에도 영향을 준다.

Q. JPA를 쓰면 Index를 몰라도 돼?
A. 아니다. JPA도 SQL을 생성하므로 WHERE, JOIN, ORDER BY에 맞는 Index 검토가 필요하다.

---

## 1.2 Index Candidate Rules

### [개념]

Index Candidate는 Index 생성 후보가 되는 Column이다.

모든 Column이 Index 후보가 되는 것은 아니며 Query에서 자주 사용되고 선택도가 의미 있는 Column을 우선 검토한다.

Index 후보는 SQL Query뿐 아니라 Repository Method, JPQL, QueryDSL, Native Query에서 반복 사용되는 조건을 기준으로 판단한다.

---

### [핵심]

Index 후보 Column:

- 자주 검색되는 Column
- JOIN에 사용되는 FK Column
- 정렬에 자주 사용되는 Column
- 범위 검색 Column
- Unique Constraint Column
- Cursor Pagination Column
- 상태 + 날짜 복합 조건 Column
- 권한 범위 조건 Column
- Soft Delete 조건 Column

Index 후보 예시:

- users.email
- posts.user_id
- reviews.festival_id
- favorites.user_id
- favorites.user_id + favorites.festival_id
- festivals.region_code + festivals.event_start_date
- notifications.user_id + read_status + created_at
- posts.user_id + deleted_at + created_at

---

### [실무]

회원 이메일 조회:

```sql
SELECT user_id, email
FROM users
WHERE email = 'user@example.com';
```

Index 후보:

```sql
CREATE UNIQUE INDEX uk_users_email
ON users (email);
```

사용자별 알림 목록:

```sql
SELECT notification_id, title, created_at
FROM notifications
WHERE user_id = 1
ORDER BY created_at DESC
LIMIT 20;
```

Index 후보:

```sql
CREATE INDEX idx_notifications_user_created
ON notifications (user_id, created_at DESC);
```

Soft Delete 목록 조회:

```sql
SELECT post_id, title, created_at
FROM posts
WHERE user_id = 1
  AND deleted_at IS NULL
ORDER BY created_at DESC;
```

Index 후보:

```sql
CREATE INDEX idx_posts_user_deleted_created
ON posts (user_id, deleted_at, created_at DESC);
```

권장:

- Equality 조건 Column 우선
- Range 조건 Column 위치 주의
- ORDER BY와 함께 사용되는 Column 검토
- FK Column Index 검토
- Unique Constraint와 Index 역할 구분
- Soft Delete 조건이 모든 조회에 반복되면 복합 Index 포함 검토
- 실제 Query 빈도 확인

---

### [FAQ]

Q. 어떤 Column이 Index 후보야?
A. WHERE, JOIN, ORDER BY, GROUP BY, Pagination에 자주 사용되는 Column이 후보가 된다.

Q. Boolean Column도 Index 후보야?
A. 단독 Boolean Column은 선택도가 낮아 효과가 제한적일 수 있고 다른 Column과 복합 Index로 검토하는 경우가 많다.

Q. Foreign Key Column에는 Index가 필요해?
A. JOIN과 관계 조회에 자주 사용되므로 Index 후보로 검토하는 것이 좋다.

Q. Soft Delete Column도 Index 후보야?
A. deleted_at, active 같은 조건이 반복 조회에 항상 포함되면 다른 조건 Column과 복합 Index로 검토할 수 있다.

---

## 1.3 Composite Index Rules

### [개념]

Composite Index는 두 개 이상의 Column을 함께 구성한 Index다.

복합 Index는 Column 순서가 중요하며 Query 조건, 정렬, Pagination 패턴에 맞게 설계해야 한다.

Composite Index는 JPA Repository Method, JPQL, QueryDSL이 생성하는 WHERE / ORDER BY 순서와 함께 검토한다.

---

### [핵심]

Composite Index 기준:

- Leftmost Prefix
- Equality First
- Range Later
- Sort Column
- Filter Column
- Join Column
- Selectivity
- Query Pattern
- Pagination Pattern
- Soft Delete Filter

일반 우선순위:

1. Equality Condition Column
2. User Scope / Tenant Scope Column
3. Status / Soft Delete Column
4. Range Condition Column
5. ORDER BY Column
6. Cursor Tie-breaker Column

---

### [실무]

지역 + 기간 검색 Query:

```sql
SELECT festival_id, title, event_start_date
FROM festivals
WHERE region_code = '11'
  AND event_start_date >= '2026-01-01'
  AND event_start_date < '2027-01-01'
ORDER BY event_start_date ASC;
```

Index 후보:

```sql
CREATE INDEX idx_festivals_region_start_date
ON festivals (region_code, event_start_date);
```

사용자별 읽지 않은 알림 최신순:

```sql
SELECT notification_id, title, created_at
FROM notifications
WHERE user_id = 1
  AND read_status = false
ORDER BY created_at DESC
LIMIT 20;
```

Index 후보:

```sql
CREATE INDEX idx_notifications_user_read_created
ON notifications (user_id, read_status, created_at DESC);
```

사용자 게시글 Soft Delete + 최신순:

```sql
SELECT post_id, title, created_at
FROM posts
WHERE user_id = 1
  AND deleted_at IS NULL
ORDER BY created_at DESC, post_id DESC
LIMIT 20;
```

Index 후보:

```sql
CREATE INDEX idx_posts_user_deleted_created_id
ON posts (user_id, deleted_at, created_at DESC, post_id DESC);
```

주의:

- 복합 Index는 Column 순서 중요
- 첫 번째 Column을 사용하지 않으면 Index 활용이 제한될 수 있음
- Range 조건 이후 Column 활용은 DBMS와 Query에 따라 제한 가능
- 단일 Column Index 여러 개가 항상 복합 Index를 대체하지 않음
- Cursor Pagination은 정렬 Column과 Cursor 조건 Column을 함께 검토
- 실제 Execution Plan 확인 필요

---

### [FAQ]

Q. Composite Index에서 Column 순서가 왜 중요해?
A. Index는 왼쪽 Column부터 순서대로 활용되므로 Query 조건과 맞지 않으면 효율이 떨어질 수 있다.

Q. 복합 Index는 어떻게 설계해?
A. Equality 조건 Column을 앞에 두고 Range, ORDER BY, Cursor Column을 Query 패턴에 맞게 배치한다.

Q. 단일 Index 여러 개면 복합 Index가 필요 없어?
A. 아니다. 여러 조건을 함께 사용하는 Query에서는 복합 Index가 더 적합할 수 있다.

Q. Cursor Pagination도 Composite Index와 관련 있어?
A. 관련 있다. Cursor 조건과 ORDER BY Column이 Index 순서와 맞아야 안정적인 성능을 기대할 수 있다.

---

## 1.4 Sargable Query Rules

### [개념]

Sargable Query는 Index를 효율적으로 사용할 수 있는 검색 조건이다.

Column에 함수, 연산, 형변환을 적용하면 Index 사용이 어려워질 수 있다.

Sargable 조건은 SQL, JPQL, QueryDSL, Native Query 모두에서 중요하다.

---

### [핵심]

Sargable 권장:

- Column을 그대로 비교
- 날짜는 Range Condition 사용
- 타입 일치
- Prefix LIKE 사용 가능성 검토
- Index Column에 함수 적용 지양
- 암시적 형변환 방지
- Cursor 조건과 ORDER BY 일치

Non-Sargable 위험:

- YEAR(column)
- DATE(column)
- LOWER(column)
- CAST(column)
- column + 1
- LIKE '%keyword'
- LIKE '%keyword%'
- 타입 불일치 비교

---

### [실무]

비권장:

```sql
SELECT festival_id, title
FROM festivals
WHERE YEAR(event_start_date) = 2026;
```

권장:

```sql
SELECT festival_id, title
FROM festivals
WHERE event_start_date >= '2026-01-01'
  AND event_start_date < '2027-01-01';
```

비권장:

```sql
SELECT user_id, email
FROM users
WHERE CAST(user_id AS CHAR) = '10';
```

권장:

```sql
SELECT user_id, email
FROM users
WHERE user_id = 10;
```

QueryDSL 주의:

```text
festival.title.contains(keyword)
→ LIKE '%keyword%' 형태가 될 수 있음
→ 대량 데이터에서는 Full Text Search 또는 Search Engine 검토
```

주의:

- 조건 Column에 함수 적용 지양
- 비교 값 타입을 Column 타입과 맞춤
- 날짜 검색은 시작 이상, 끝 미만 권장
- 대소문자 무시 검색은 Collation 또는 별도 Search Column 검토
- Contains Search는 Full Text Search 검토

---

### [FAQ]

Q. Sargable Query는 뭐야?
A. Index를 효율적으로 사용할 수 있는 형태의 검색 조건이다.

Q. 날짜 검색에서 YEAR(column)을 쓰면 왜 안 좋아?
A. Column에 함수를 적용하면 Index를 효율적으로 사용하기 어려울 수 있기 때문이다.

Q. LIKE '%keyword%'는 Sargable해?
A. 일반 B-Tree Index 기준으로는 효율적으로 사용하기 어렵다.

Q. QueryDSL을 쓰면 Sargable 문제를 피할 수 있어?
A. 아니다. QueryDSL도 SQL로 변환되므로 생성 SQL이 Sargable한지 확인해야 한다.

---

# 2. Pagination Foundation

## 2.1 Pagination Purpose

### [개념]

Pagination은 목록 데이터를 일정 개수씩 나누어 조회하는 방식이다.

Backend API에서 Pagination은 대량 데이터 응답을 제한하고 화면 목록, 무한 스크롤, 관리자 목록, 검색 결과를 안정적으로 제공하기 위해 사용한다.

Pagination은 SQL ORDER BY, Index, JPA Pageable, Slice, Page, QueryDSL offset / limit와 연결된다.

---

### [핵심]

Pagination 방식:

- OFFSET Pagination
- Cursor Pagination
- Keyset Pagination
- Slice Pagination
- Page Pagination

필수 요소:

- ORDER BY
- LIMIT
- Page Size
- Stable Sort
- Unique Tie-breaker
- Index
- Next Cursor
- Has Next
- Count Query Policy

---

### [실무]

Pagination 설계 Flow:

```text
목록 요구사항 확인
→ 정렬 기준 확인
→ Page 방식 / Cursor 방식 선택
→ Page Size 제한
→ Stable Sort 보장
→ Index 검토
→ JPA Page / Slice 선택
→ 응답 DTO 설계
→ hasNext / totalCount 정책 결정
```

일반 목록:

```text
관리자 목록
→ Page Pagination 가능
→ totalCount 필요할 수 있음
→ Page<T> 검토
```

무한 스크롤:

```text
채팅 / 알림 / 피드
→ Cursor Pagination 또는 Slice Pagination 권장
→ totalCount 불필요 가능
→ Slice<T> 또는 Cursor Response 검토
```

주의:

- ORDER BY 없는 Pagination 금지
- 정렬 기준 중복 시 PK 추가
- 큰 OFFSET은 성능 저하 가능
- totalCount Query 비용 검토
- Fetch Join + Pagination 조합 주의
- 1:N JOIN 결과에 직접 Pagination 적용 주의

---

### [FAQ]

Q. Pagination은 왜 필요해?
A. 대량 데이터를 한 번에 조회하지 않고 일정 개수씩 안정적으로 제공하기 위해 필요하다.

Q. Pagination에서 가장 중요한 것은?
A. ORDER BY와 Stable Sort다. 정렬 기준이 없으면 결과 순서가 흔들릴 수 있다.

Q. 무한 스크롤에는 어떤 Pagination이 좋아?
A. Cursor Pagination 또는 Slice Pagination이 적합한 경우가 많다.

Q. JPA Page와 Slice는 어떻게 골라?
A. totalCount가 필요하면 Page, hasNext만 필요하면 Slice가 적합하다.

---

## 2.2 OFFSET Pagination

### [개념]

OFFSET Pagination은 LIMIT과 OFFSET을 사용해 페이지 번호 기반으로 데이터를 조회하는 방식이다.

구현이 단순하고 관리자 목록, 검색 결과 페이지에 적합하지만 OFFSET이 커질수록 성능이 저하될 수 있다.

JPA Pageable의 Page 방식은 일반적으로 OFFSET Pagination과 Count Query를 함께 사용한다.

---

### [핵심]

OFFSET Pagination 구성:

- LIMIT
- OFFSET
- ORDER BY
- Page Number
- Page Size
- Total Count
- Stable Sort
- Count Query

장점:

- 구현 단순
- 특정 페이지 이동 가능
- 관리자 화면에 적합
- Page UI와 잘 맞음

단점:

- 큰 OFFSET 성능 저하
- 데이터 변경 시 중복 / 누락 가능
- totalCount 비용 발생 가능
- 대량 무한 스크롤에 부적합

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

JPA 연계:

```text
Pageable
→ offset / limit
→ Sort
→ Page<T> 사용 시 Count Query 가능
→ Slice<T> 사용 시 hasNext 중심
```

권장:

- ORDER BY 필수
- 중복 가능한 정렬 Column에는 PK 추가
- Page Size 최대값 제한
- 큰 OFFSET 구간 성능 검토
- 검색 조건 Column과 정렬 Column Index 검토
- Count Query 비용 검토
- 대량 데이터 무한 스크롤은 Cursor Pagination 검토

---

### [FAQ]

Q. OFFSET Pagination은 언제 사용해?
A. 페이지 번호 기반 목록, 관리자 화면, 검색 결과 페이지에 적합하다.

Q. OFFSET Pagination은 언제 문제가 돼?
A. OFFSET 값이 커지면 앞 데이터를 많이 건너뛰어야 해서 성능이 떨어질 수 있다.

Q. ORDER BY 없이 OFFSET을 써도 돼?
A. 안 된다. 정렬 기준이 없으면 페이지 결과가 불안정해질 수 있다.

Q. JPA Page를 쓰면 Count Query도 고려해야 해?
A. 그렇다. Page는 totalCount가 필요하므로 Count Query 비용을 검토해야 한다.

---

## 2.3 Cursor Pagination

### [개념]

Cursor Pagination은 이전 조회 결과의 마지막 값을 기준으로 다음 데이터를 조회하는 방식이다.

무한 스크롤, 채팅, 알림, 피드처럼 순차 조회가 필요한 기능에 적합하다.

Cursor Pagination은 정렬 기준과 Cursor 조건이 반드시 일치해야 한다.

---

### [핵심]

Cursor Pagination 구성:

- Cursor Value
- Last Seen ID
- Last Created At
- Keyset Condition
- LIMIT
- ORDER BY
- hasNext
- Stable Sort
- Tie-breaker Column

장점:

- 큰 OFFSET 성능 문제 완화
- 무한 스크롤에 적합
- 순차 조회 안정성 좋음
- Index 활용 가능성 높음

단점:

- 특정 페이지 번호 이동 어려움
- Cursor 설계 필요
- 복합 정렬 조건 구현 복잡
- 정렬 기준 변경 시 Cursor 정책 필요

---

### [실무]

created_at 기준 Cursor Pagination:

```sql
SELECT notification_id, title, created_at
FROM notifications
WHERE user_id = 1
  AND created_at < '2026-07-03 10:00:00'
ORDER BY created_at DESC
LIMIT 20;
```

created_at + id 안정 정렬:

```sql
SELECT notification_id, title, created_at
FROM notifications
WHERE user_id = 1
  AND (
    created_at < '2026-07-03 10:00:00'
    OR (created_at = '2026-07-03 10:00:00' AND notification_id < 100)
  )
ORDER BY created_at DESC, notification_id DESC
LIMIT 20;
```

QueryDSL 연계:

```text
createdAt DESC, id DESC 정렬
→ lastCreatedAt, lastId Cursor 사용
→ BooleanExpression으로 Cursor 조건 구성
→ pageSize + 1 조회
→ hasNext 판단
```

권장:

- Cursor Column은 정렬 기준과 일치
- 중복 정렬 값에는 PK 포함
- hasNext 판단을 위해 pageSize + 1 조회 가능
- Cursor Column Index 검토
- 삭제 / 추가 데이터에 따른 UX 정책 정의
- Cursor 값은 Response DTO에 포함

---

### [FAQ]

Q. Cursor Pagination은 언제 사용해?
A. 무한 스크롤, 채팅, 알림, 피드처럼 순차적으로 다음 목록을 가져올 때 사용한다.

Q. Cursor Pagination은 OFFSET보다 왜 유리해?
A. 큰 OFFSET을 건너뛰지 않고 마지막으로 본 값을 기준으로 다음 데이터를 찾기 때문에 대량 데이터에 유리하다.

Q. Cursor에 id만 쓰면 돼?
A. 정렬 기준이 id라면 가능하지만 created_at 정렬이면 created_at과 id를 함께 쓰는 것이 안정적이다.

Q. Cursor 조건과 ORDER BY가 왜 맞아야 해?
A. 정렬 기준과 Cursor 조건이 다르면 중복 또는 누락 데이터가 발생할 수 있기 때문이다.

---

## 2.4 Pagination Review Rules

### [개념]

Pagination Review Rules는 목록 Query에서 중복, 누락, 순서 흔들림, 성능 저하를 방지하기 위한 검수 기준이다.

Pagination은 Query 결과 순서, Index 설계, Repository 반환 타입, API Response 정책이 함께 검토되어야 한다.

---

### [핵심]

검토 대상:

- ORDER BY 존재 여부
- Stable Sort 여부
- PK Tie-breaker 여부
- Page Size 제한
- OFFSET 크기
- Cursor Condition
- Index 가능성
- totalCount 필요 여부
- Fetch Join 영향
- 1:N JOIN 중복 Row
- Page / Slice 선택
- Response hasNext 정책

위험 패턴:

- ORDER BY 없는 Pagination
- 중복 정렬 값만 사용
- 큰 OFFSET 무시
- 1:N JOIN 후 Pagination
- Fetch Join + Pagination 남용
- totalCount 무조건 실행
- Cursor 조건과 정렬 조건 불일치

---

### [실무]

잘못된 Pagination:

```sql
SELECT festival_id, title
FROM festivals
LIMIT 20 OFFSET 20;
```

문제:

```text
ORDER BY 없음
→ Page 결과 순서 불안정
→ 중복 / 누락 가능
```

개선:

```sql
SELECT festival_id, title, created_at
FROM festivals
ORDER BY created_at DESC, festival_id DESC
LIMIT 20 OFFSET 20;
```

검수 Flow:

```text
목록 Query 확인
→ ORDER BY 확인
→ 정렬 값 중복 가능성 확인
→ PK Tie-breaker 확인
→ Pagination 방식 확인
→ Index 확인
→ Join 중복 확인
→ Page / Slice 선택 확인
→ Response hasNext / totalCount 확인
```

---

### [FAQ]

Q. Pagination 검수에서 가장 중요한 것은?
A. ORDER BY와 Stable Sort 여부다.

Q. 1:N JOIN 후 Pagination은 왜 위험해?
A. 부모 Row가 자식 Row 수만큼 중복되어 페이지 결과가 왜곡될 수 있기 때문이다.

Q. totalCount Query는 항상 실행해야 해?
A. 아니다. UI 요구사항에 따라 필요할 때만 실행하는 것이 좋다.

Q. Fetch Join과 Pagination은 왜 주의해야 해?
A. ORM 환경에서 메모리 Pagination이나 중복 Row 문제가 발생할 수 있기 때문이다.

---

# 3. Transaction Foundation

## 3.1 Transaction Purpose

### [개념]

Transaction은 여러 데이터 변경 작업을 하나의 작업 단위로 묶어 모두 성공하거나 모두 실패하도록 보장하는 개념이다.

Transaction은 데이터 정합성, 실패 복구, 동시성 제어와 연결된다.

JPA에서는 보통 Service Method 단위에 `@Transactional`을 적용하여 Persistence Context, Dirty Checking, Flush, Commit, Rollback을 관리한다.

---

### [핵심]

Transaction 핵심:

- Atomicity
- Consistency
- Isolation
- Durability
- Commit
- Rollback
- Flush
- Dirty Checking
- Persistence Context
- Lock
- Isolation Level
- Deadlock
- Data Integrity

Transaction 필요 상황:

- 여러 Table 동시 변경
- 결제 / 주문 / 포인트 차감
- 재고 감소
- 회원 탈퇴 처리
- 좋아요 / 찜 카운트 갱신
- 중복 신청 방지
- 데이터 정합성 보장 필요
- 실패 시 Rollback 필요

---

### [실무]

Transaction Flow:

```text
Begin Transaction
→ Persistence Context 생성
→ Validate
→ Entity 조회 / 변경
→ Dirty Checking
→ Flush
→ Commit
→ Error 발생
→ Rollback
```

후원 결제 처리 예시:

```text
결제 성공
→ donation 생성
→ payment 생성
→ festival 후원 금액 증가
→ 모두 성공 시 Commit
→ 하나라도 실패 시 Rollback
```

Spring 기준:

```text
Service Method
→ @Transactional
→ Repository 변경 작업
→ Dirty Checking
→ 정상 종료 Commit
→ RuntimeException 발생 Rollback
```

주의:

- 단순 SELECT는 Transaction이 필요 없을 수 있음
- 긴 Transaction은 Lock 지속 시간 증가
- 외부 API 호출과 DB Transaction 경계 주의
- Transaction 범위를 과도하게 넓히지 않음
- 여러 변경 작업의 성공 / 실패 단위를 명확히 정의
- JPA 변경 감지는 Transaction 안에서 동작해야 함

---

### [FAQ]

Q. Transaction은 언제 필요해?
A. 여러 DB 변경이 하나의 성공 / 실패 단위로 묶여야 할 때 필요하다.

Q. JPA에서 Transaction은 왜 중요해?
A. Persistence Context, Dirty Checking, Flush, Commit, Rollback이 Transaction과 함께 동작하기 때문이다.

Q. 단순 SELECT에도 Transaction이 필요해?
A. 일반적으로 단순 조회에는 필수는 아니지만 일관된 읽기나 Lazy Loading, 읽기 전용 최적화가 필요하면 검토할 수 있다.

Q. Spring에서는 Transaction을 어디에 적용해?
A. 보통 여러 Repository 변경을 묶는 Service Method에 @Transactional을 적용한다.

---

## 3.2 ACID Rules

### [개념]

ACID는 Transaction이 보장해야 하는 핵심 속성이다.

Atomicity, Consistency, Isolation, Durability를 의미한다.

ACID는 SQL Transaction뿐 아니라 JPA Entity 변경, Repository save, Dirty Checking, Constraint 검증과 연결된다.

---

### [핵심]

ACID:

| 속성        | 의미                     | 실무 기준                  |
| ----------- | ------------------------ | -------------------------- |
| Atomicity   | 모두 성공 또는 모두 실패 | 실패 시 Rollback           |
| Consistency | 정합성 유지              | Constraint / Business Rule |
| Isolation   | Transaction 간 격리      | 동시성 제어                |
| Durability  | Commit 결과 영속화       | 장애 후 데이터 보존        |

---

### [실무]

Atomicity 예시:

```text
주문 생성
→ 주문 상품 생성
→ 결제 내역 생성
→ 하나라도 실패하면 전체 Rollback
```

Consistency 예시:

```text
찜 등록
→ favorites insert
→ user_id + festival_id Unique Constraint 유지
→ 중복 요청은 Constraint 위반 예외 처리
```

Isolation 예시:

```text
동시에 같은 쿠폰 발급 요청
→ 중복 발급 방지 필요
→ Unique Constraint / Lock / Transaction 검토
```

Durability 예시:

```text
결제 완료 Commit
→ 서버 장애 후에도 결제 완료 데이터 유지
```

권장:

- Business Rule과 DB Constraint 함께 사용
- Rollback 기준 명확화
- 동시성 요구사항 확인
- Transaction 범위 최소화
- 외부 시스템 호출 결과와 DB 반영 순서 검토
- JPA Entity 상태 변경과 DB Constraint 충돌 가능성 검토

---

### [FAQ]

Q. ACID는 뭐야?
A. Transaction의 Atomicity, Consistency, Isolation, Durability 속성을 의미한다.

Q. Atomicity는 무슨 뜻이야?
A. 여러 작업이 모두 성공하거나 하나라도 실패하면 모두 취소되어야 한다는 뜻이다.

Q. Consistency는 어떻게 보장해?
A. Business Rule, DB Constraint, Transaction을 함께 사용해 데이터 정합성을 유지한다.

Q. JPA에서도 ACID가 중요해?
A. 중요하다. JPA Entity 변경도 Transaction Commit 시 DB에 반영되므로 ACID 기준으로 검토해야 한다.

---

## 3.3 Isolation Level Basics

### [개념]

Isolation Level은 동시에 실행되는 Transaction들이 서로 어떤 수준으로 격리되는지 결정하는 기준이다.

격리 수준이 높을수록 정합성은 강해질 수 있지만 동시성 성능은 낮아질 수 있다.

Isolation Level은 DBMS 기본값, Spring `@Transactional(isolation = ...)`, Lock 전략과 함께 검토한다.

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

비교:

| Level            | Dirty Read | Non-repeatable Read | Phantom Read | 동시성 |
| ---------------- | ---------- | ------------------- | ------------ | ------ |
| READ UNCOMMITTED | 가능       | 가능                | 가능         | 높음   |
| READ COMMITTED   | 방지       | 가능                | 가능         | 높음   |
| REPEATABLE READ  | 방지       | 방지                | DBMS별 차이  | 보통   |
| SERIALIZABLE     | 방지       | 방지                | 방지         | 낮음   |

---

### [실무]

동시성 검토 상황:

```text
동시에 같은 재고 감소
동시에 같은 쿠폰 발급
동시에 같은 좌석 예약
동시에 같은 좋아요 등록
동시에 같은 결제 상태 변경
```

권장:

- Isolation Level을 무조건 높이지 않음
- DB 기본 Isolation Level 확인
- Unique Constraint와 Transaction 함께 사용
- 필요 시 Pessimistic Lock / Optimistic Lock 검토
- 동시성 테스트 작성
- Deadlock 가능성 확인
- JPA @Lock / @Version과 역할 분리

주의:

- SERIALIZABLE은 성능 비용이 큼
- Isolation Level만으로 모든 중복 문제를 해결하지 않음
- Application 검증만으로 동시성 문제를 막기 어려움
- DBMS별 Isolation 구현 차이 확인 필요
- JPA Persistence Context 캐시와 DB Isolation을 혼동하지 않음

---

### [FAQ]

Q. Isolation Level은 항상 높을수록 좋아?
A. 아니다. 격리 수준이 높으면 정합성은 강해질 수 있지만 동시성 성능이 낮아질 수 있다.

Q. Dirty Read는 뭐야?
A. 아직 Commit되지 않은 다른 Transaction의 변경 데이터를 읽는 현상이다.

Q. Non-repeatable Read는 뭐야?
A. 같은 Transaction 안에서 같은 Row를 다시 읽었을 때 값이 달라지는 현상이다.

Q. JPA Persistence Context와 Isolation Level은 같아?
A. 아니다. Persistence Context는 JPA 1차 캐시이고 Isolation Level은 DB Transaction 격리 기준이다.

---

## 3.4 Lock Basics

### [개념]

Lock은 Transaction 중 데이터 정합성을 유지하기 위해 특정 Row, Table, 범위에 대한 접근을 제어하는 장치다.

Lock은 동시성 문제를 막을 수 있지만 성능 저하와 Deadlock 위험을 만들 수 있다.

JPA에서는 Pessimistic Lock은 `@Lock`, Optimistic Lock은 `@Version`과 연결된다.

---

### [핵심]

Lock 유형:

- Shared Lock
- Exclusive Lock
- Row Lock
- Table Lock
- Gap Lock
- Pessimistic Lock
- Optimistic Lock

동시성 위험:

- Lost Update
- Duplicate Insert
- Race Condition
- Deadlock
- Long Transaction
- Lock Wait Timeout

---

### [실무]

비관적 Lock 개념:

```text
조회 시점에 Row Lock 확보
→ 다른 Transaction의 수정 대기
→ 현재 Transaction 완료 후 Lock 해제
```

낙관적 Lock 개념:

```text
version Column 사용
→ 수정 시 version 비교
→ version 불일치 시 충돌 감지
```

사용 상황:

- 재고 감소
- 선착순 신청
- 포인트 차감
- 결제 상태 변경
- 중복 쿠폰 발급
- 동시 좋아요 / 찜 처리

JPA 연계:

```text
Pessimistic Lock
→ @Lock(PESSIMISTIC_WRITE)
→ SELECT FOR UPDATE 계열 SQL 가능

Optimistic Lock
→ @Version
→ UPDATE 시 version 조건 포함
→ 충돌 시 OptimisticLockException
```

권장:

- Unique Constraint로 막을 수 있는 중복은 Constraint 우선 검토
- 상태 변경은 WHERE에 현재 상태 조건 포함
- 긴 Transaction에서 Lock 유지 주의
- Lock 사용 시 Deadlock 가능성 검토
- Lock은 Transaction 내부에서 사용

---

### [FAQ]

Q. Lock은 언제 필요해?
A. 동시에 같은 데이터를 변경할 때 정합성 문제가 발생할 수 있으면 검토한다.

Q. Pessimistic Lock은 뭐야?
A. 데이터를 수정하기 전에 먼저 Lock을 걸어 다른 Transaction의 접근을 제한하는 방식이다.

Q. Optimistic Lock은 뭐야?
A. version 값을 이용해 수정 시점에 충돌 여부를 확인하는 방식이다.

Q. JPA에서 Optimistic Lock은 무엇과 연결돼?
A. Entity의 @Version Column과 연결된다.

---

# 4. Constraint Foundation

## 4.1 Constraint Purpose

### [개념]

Constraint는 Table에 저장되는 데이터의 무결성을 보장하기 위한 제약 조건이다.

Application 검증만으로 데이터 무결성을 완전히 보장하기 어렵기 때문에 중요한 규칙은 DB Constraint로도 보호해야 한다.

Constraint는 JPA Entity Annotation과 DB Schema Constraint가 서로 일치해야 안정적이다.

---

### [핵심]

Constraint 종류:

- Primary Key
- Foreign Key
- Unique
- Not Null
- Check
- Default

Constraint 목적:

- Row 식별
- 관계 무결성
- 중복 방지
- 필수 값 보장
- 허용 값 제한
- 기본값 제공
- Application 오류 방어
- Data Integrity 보장

JPA 연계:

- @Id
- @GeneratedValue
- @Column(nullable = false)
- @Column(unique = true)
- @Table(uniqueConstraints = ...)
- @ManyToOne
- @JoinColumn
- @Enumerated
- @PrePersist
- @PreUpdate

---

### [실무]

favorites Table 예시:

```sql
CREATE TABLE favorites (
  favorite_id BIGINT PRIMARY KEY,
  user_id BIGINT NOT NULL,
  festival_id BIGINT NOT NULL,
  created_at DATETIME NOT NULL,
  UNIQUE (user_id, festival_id)
);
```

검토 기준:

```text
user_id는 필수인가?
festival_id는 필수인가?
같은 사용자가 같은 축제를 중복 찜하면 안 되는가?
users / festivals와 FK 관계가 필요한가?
created_at 기본값은 DB에서 처리할 것인가?
JPA Entity Annotation과 DB Constraint가 일치하는가?
```

권장:

- 중요한 무결성은 DB Constraint 사용
- Application Validation과 DB Constraint 병행
- Unique Constraint로 중복 방지
- Not Null로 필수 값 보장
- FK로 관계 무결성 검토
- Check로 Enum성 값 제한 가능
- JPA Annotation과 실제 DB Schema 불일치 방지

---

### [FAQ]

Q. Constraint는 왜 필요해?
A. 데이터 중복, 누락, 잘못된 관계, 허용되지 않는 값을 DB 수준에서 방지하기 위해 필요하다.

Q. Application에서 검증하면 DB Constraint는 없어도 돼?
A. 아니다. Application 검증은 우회될 수 있으므로 중요한 무결성은 DB Constraint로도 보장하는 것이 좋다.

Q. JPA Annotation만 있으면 DB Constraint는 없어도 돼?
A. 아니다. JPA Annotation과 실제 DB Constraint가 일치해야 운영 데이터 무결성이 안정적으로 보장된다.

Q. Backend Agent는 Constraint를 왜 알아야 해?
A. INSERT, UPDATE, DELETE Query 생성 시 중복, 필수 값, FK 오류를 예측하고 방지해야 하기 때문이다.

---

## 4.2 Primary Key and Foreign Key

### [개념]

Primary Key는 Table의 각 Row를 고유하게 식별하는 Constraint다.

Foreign Key는 다른 Table의 Primary Key를 참조하여 관계 무결성을 보장하는 Constraint다.

Primary Key와 Foreign Key는 SQL JOIN, JPA Entity Relationship, Repository Query의 기준이다.

---

### [핵심]

Primary Key:

- Row 식별
- Unique
- Not Null
- 단건 조회 기준
- 수정 / 삭제 기준
- JOIN 참조 대상
- Entity Identity

Foreign Key:

- Parent Table 참조
- Child Table에 위치
- 관계 무결성 보장
- JOIN 조건 기준
- 삭제 / 수정 영향 발생
- Cascade 정책 검토 필요
- JPA Association 기준

---

### [실무]

PK / FK SQL 예시:

```sql
CREATE TABLE reviews (
  review_id BIGINT PRIMARY KEY,
  user_id BIGINT NOT NULL,
  festival_id BIGINT NOT NULL,
  rating INT NOT NULL,
  content TEXT,
  created_at DATETIME NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (festival_id) REFERENCES festivals(festival_id)
);
```

JOIN 예시:

```sql
SELECT r.review_id, r.content, u.nickname
FROM reviews r
JOIN users u ON r.user_id = u.user_id
WHERE r.festival_id = 10;
```

JPA 연계:

```text
reviews.user_id FK
→ Review Entity @ManyToOne User
→ @JoinColumn(name = "user_id", nullable = false)

reviews.festival_id FK
→ Review Entity @ManyToOne Festival
→ @JoinColumn(name = "festival_id", nullable = false)
```

주의:

- FK 대상 Row가 없으면 INSERT / UPDATE 실패 가능
- Parent Row 삭제 시 Child Row 영향 확인
- Cascade Delete는 신중히 사용
- FK Column은 JOIN 성능을 위해 Index 후보
- JPA Entity 관계와 DB FK 제약이 다를 수 있음
- JPA Cascade와 DB Cascade는 역할이 다름

---

### [FAQ]

Q. Primary Key는 무엇에 사용해?
A. Row 식별, 단건 조회, 수정, 삭제, JOIN 참조, Entity 식별 기준으로 사용한다.

Q. Foreign Key는 왜 중요해?
A. Table 간 관계 무결성을 보장하고 JOIN 조건과 JPA 연관관계의 기준이 되기 때문이다.

Q. FK가 있으면 Parent Row를 마음대로 삭제할 수 있어?
A. 아니다. Child Row가 참조 중이면 삭제가 실패하거나 Cascade 정책에 따라 함께 삭제될 수 있다.

Q. JPA Cascade와 DB Cascade는 같아?
A. 아니다. JPA Cascade는 Entity 상태 전파이고 DB Cascade는 DB Constraint 기반 삭제 / 수정 전파다.

---

## 4.3 Unique and Not Null

### [개념]

Unique Constraint는 특정 Column 또는 Column 조합의 중복 값을 금지한다.

Not Null Constraint는 특정 Column에 NULL 저장을 금지한다.

Unique와 Not Null은 데이터 중복 방지와 필수 값 보장의 핵심 Constraint다.

---

### [핵심]

Unique 사용 상황:

- email
- username
- user_id + festival_id
- user_id + post_id
- order_number
- payment_key
- idempotency_key

Not Null 사용 상황:

- 필수 FK
- 필수 상태값
- 필수 생성일
- 필수 금액
- 필수 제목
- 필수 권한
- 필수 Enum

JPA 연계:

- @Column(nullable = false)
- @Column(unique = true)
- @Table(uniqueConstraints = ...)
- @JoinColumn(nullable = false)

---

### [실무]

email Unique:

```sql
CREATE TABLE users (
  user_id BIGINT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  nickname VARCHAR(100) NOT NULL,
  created_at DATETIME NOT NULL
);
```

Composite Unique:

```sql
CREATE TABLE festival_likes (
  like_id BIGINT PRIMARY KEY,
  user_id BIGINT NOT NULL,
  festival_id BIGINT NOT NULL,
  created_at DATETIME NOT NULL,
  UNIQUE (user_id, festival_id)
);
```

JPA Composite Unique 연계:

```text
@Table(
  uniqueConstraints = {
    @UniqueConstraint(
      name = "uk_festival_likes_user_festival",
      columnNames = {"user_id", "festival_id"}
    )
  }
)
```

권장:

- 중복되면 안 되는 값은 Unique Constraint 사용
- 필수 값은 Not Null 사용
- Application 중복 체크와 DB Unique 병행
- Unique 위반 예외를 비즈니스 예외로 변환
- Soft Delete와 Unique 충돌 검토
- JPA Annotation과 DB Schema 일치 확인

주의:

- Unique는 DBMS별 NULL 처리 차이 가능
- Soft Delete 후 같은 값 재사용 정책 필요
- Composite Unique Column 순서와 Query 패턴 검토
- Unique Constraint도 쓰기 시 검증 비용 발생
- Application exists check만으로 중복 방지하지 않음

---

### [FAQ]

Q. Unique Constraint는 언제 필요해?
A. email, user-festival favorite처럼 중복되면 안 되는 데이터에 필요하다.

Q. Not Null은 언제 사용해?
A. 비즈니스상 반드시 값이 있어야 하는 Column에 사용한다.

Q. Application에서 중복 체크하면 Unique는 없어도 돼?
A. 아니다. 동시 요청에서는 중복이 발생할 수 있으므로 DB Unique Constraint가 필요하다.

Q. Soft Delete와 Unique는 왜 충돌할 수 있어?
A. 삭제 처리된 Row가 DB에 남아 있으면 같은 Unique 값을 다시 사용할 수 없을 수 있기 때문이다.

---

## 4.4 Check and Default

### [개념]

Check Constraint는 Column 값이 특정 조건을 만족하도록 제한한다.

Default Constraint는 INSERT 시 값이 생략되었을 때 기본값을 제공한다.

Check와 Default는 JPA Validation, Entity 초기값, @PrePersist, DB Default 정책과 함께 검토해야 한다.

---

### [핵심]

Check 사용 상황:

- rating between 0 and 5
- amount >= 0
- quantity >= 0
- status in allowed values
- percentage between 0 and 100

Default 사용 상황:

- created_at
- active = true
- read_status = false
- role = ROLE_USER
- count = 0
- status = READY

JPA 연계:

- Entity Field 초기값
- @PrePersist
- @PreUpdate
- @Enumerated
- Bean Validation
- DB Default

---

### [실무]

Check 예시:

```sql
CREATE TABLE reviews (
  review_id BIGINT PRIMARY KEY,
  rating INT NOT NULL,
  content TEXT,
  CHECK (rating >= 0 AND rating <= 5)
);
```

Default 예시:

```sql
CREATE TABLE notifications (
  notification_id BIGINT PRIMARY KEY,
  read_status BOOLEAN NOT NULL DEFAULT false,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

JPA 초기값 연계:

```text
readStatus 기본값
→ DB DEFAULT false 사용 가능
→ Entity field 초기값 사용 가능
→ @PrePersist 사용 가능
→ 프로젝트 기준 통일 필요
```

권장:

- 숫자 범위는 Check 검토
- 상태 기본값은 프로젝트 기준 통일
- Application Enum과 DB 허용 값 일치
- Default를 DB에서 줄지 Application에서 줄지 기준 통일
- Audit Column 처리 기준 통일
- JPA @PrePersist와 DB Default 중복 / 불일치 주의

주의:

- DBMS 버전별 Check 지원 차이 확인
- Default와 Application 초기값 불일치 주의
- Enum 값을 문자열로 저장할 때 Naming 통일
- Default에 의존하면 INSERT Query 의도가 흐려질 수 있음
- DB Default는 JPA Entity 상태와 즉시 동기화되지 않을 수 있음

---

### [FAQ]

Q. Check Constraint는 언제 사용해?
A. rating, amount, quantity처럼 허용 범위가 명확한 값에 사용한다.

Q. Default는 언제 사용해?
A. 생성 시 기본 상태나 기본 값을 자동으로 넣어야 할 때 사용한다.

Q. Default는 DB에서 처리하는 게 좋아?
A. 프로젝트 기준에 따라 다르며 DB Default와 Application 초기값 중 하나로 일관성 있게 관리해야 한다.

Q. DB Default와 JPA 초기값을 동시에 쓰면 안전해?
A. 불일치 위험이 있으므로 하나의 기준으로 통일하는 것이 좋다.

---

# 5. JPA and Constraint Link Rules

## 5.1 Entity Mapping and DB Constraint Consistency

### [개념]

Entity Mapping and DB Constraint Consistency는 JPA Entity Annotation과 실제 DB Schema Constraint가 일치하는지 확인하는 기준이다.

JPA Entity는 Application Layer의 모델이고 DB Constraint는 Database Layer의 무결성 보장 장치다.

둘 중 하나만 의존하면 운영 데이터 무결성이 깨질 수 있다.

---

### [핵심]

일치 확인 대상:

- Entity Field Type
- Column Type
- nullable
- unique
- length
- precision / scale
- Primary Key
- Foreign Key
- Enum Mapping
- Default Value
- Audit Column
- Soft Delete Column

---

### [실무]

검수 Flow:

```text
Entity 설계
→ @Column nullable / unique / length 확인
→ @JoinColumn nullable 확인
→ DB DDL 확인
→ Migration Script 확인
→ Repository Query 확인
→ Integration Test 검증
```

불일치 예시:

```text
Entity:
@Column(nullable = false)
private String title;

DB:
title VARCHAR(255) NULL

문제:
Application에서는 필수로 보이지만 DB는 NULL 허용
외부 SQL 또는 Migration 오류로 NULL 데이터 가능
```

권장:

- Entity Annotation과 DB DDL 일치
- 운영 DB는 Migration Script 기준으로 관리
- Schema 자동 생성에만 의존하지 않음
- Constraint 위반 예외 처리 기준 정의
- Repository Test / Integration Test로 검증

---

### [FAQ]

Q. Entity Annotation과 DB Constraint가 달라도 돼?
A. 권장하지 않는다. 둘이 다르면 Application 기준과 DB 기준이 달라져 데이터 무결성 문제가 생길 수 있다.

Q. JPA nullable=false만 있으면 충분해?
A. 아니다. 실제 DB Column도 NOT NULL로 생성되어야 안정적이다.

Q. Unique는 Entity에만 선언해도 돼?
A. 운영 DB에 실제 Unique Constraint가 존재해야 중복을 확실히 막을 수 있다.

Q. Constraint 검증은 어디서 확인해?
A. Entity, DDL, Migration Script, Integration Test에서 함께 확인한다.

---

## 5.2 Cascade and Orphan Removal Link

### [개념]

Cascade는 부모 Entity의 상태 변화가 자식 Entity로 전파되는 JPA 기능이다.

Orphan Removal은 부모와의 관계가 끊긴 자식 Entity를 삭제 대상으로 처리하는 JPA 기능이다.

DB Cascade는 DB Foreign Key Constraint 수준에서 삭제 또는 수정이 전파되는 기능이다.

JPA Cascade, Orphan Removal, DB Cascade는 역할이 다르므로 혼동하면 안 된다.

---

### [핵심]

구분:

- JPA Cascade
- Orphan Removal
- DB Cascade
- Foreign Key Constraint
- Parent Entity
- Child Entity
- Aggregate Boundary
- Delete Propagation
- Data Integrity

주의 대상:

- 부모 삭제 시 자식 삭제 여부
- 관계 제거 시 자식 삭제 여부
- DB FK 제약과 충돌 여부
- Soft Delete와 Cascade 충돌
- 대량 삭제 성능
- 의도하지 않은 연쇄 삭제

---

### [실무]

역할 분리:

```text
JPA Cascade:
Entity 상태 전파
persist, merge, remove 등 전파

orphanRemoval:
부모 Collection에서 제거된 자식 Entity 삭제

DB Cascade:
DB FK Constraint 기준으로 삭제 / 수정 전파
```

검토 Flow:

```text
Parent / Child 관계 확인
→ 자식 생명주기가 부모에 종속되는지 확인
→ Aggregate Boundary 확인
→ Soft Delete 여부 확인
→ JPA Cascade 필요 여부 확인
→ orphanRemoval 필요 여부 확인
→ DB Cascade 필요 여부 확인
→ 삭제 테스트 수행
```

주의:

- Soft Delete를 사용하는 Entity에 물리 삭제 Cascade를 적용하면 위험
- ManyToOne에 Cascade REMOVE 남용 금지
- 공유 자식 Entity에는 orphanRemoval 주의
- DB Cascade와 JPA Cascade를 중복 적용할 때 동작 확인 필요
- 삭제 전 영향 범위 확인

---

### [FAQ]

Q. JPA Cascade와 DB Cascade는 같아?
A. 아니다. JPA Cascade는 Entity 상태 전파이고 DB Cascade는 DB FK Constraint 기반 삭제 / 수정 전파다.

Q. orphanRemoval은 언제 사용해?
A. 부모와 관계가 끊긴 자식 Entity가 더 이상 독립적으로 존재하면 안 될 때 사용한다.

Q. Soft Delete와 Cascade를 같이 써도 돼?
A. 주의해야 한다. Soft Delete 정책과 물리 삭제 Cascade가 충돌할 수 있다.

Q. Cascade에서 가장 위험한 실수는?
A. 의도하지 않은 연쇄 삭제가 발생하는 것이다.

---

## 5.3 Soft Delete and Constraint Link

### [개념]

Soft Delete는 Row를 실제 삭제하지 않고 삭제 상태를 표시하는 방식이다.

Soft Delete는 Unique Constraint, Index, Repository 기본 조건, JPA Entity 조회 조건과 강하게 연결된다.

Soft Delete 기준이 불명확하면 삭제 데이터 조회, 중복 제약 충돌, Query 누락 문제가 발생한다.

---

### [핵심]

Soft Delete 관련 요소:

- deleted_at
- active
- deleted
- status
- Unique Constraint
- Partial Unique Index
- Composite Unique
- Repository Filter
- QueryDSL Condition
- Index
- Audit Column

---

### [실무]

Soft Delete 조회 조건:

```sql
SELECT post_id, title
FROM posts
WHERE deleted_at IS NULL
ORDER BY created_at DESC;
```

Soft Delete + Unique 충돌 예시:

```text
users.email UNIQUE
→ 회원 탈퇴를 Soft Delete 처리
→ 같은 email로 재가입 필요
→ 기존 deleted_at Row 때문에 Unique 충돌 가능
```

해결 검토:

```text
정책 1:
Soft Delete 후 같은 email 재사용 금지

정책 2:
email + deleted_at 또는 status 기반 Unique 설계 검토

정책 3:
DBMS가 지원하면 Partial Unique Index 검토

정책 4:
탈퇴 계정 anonymization 검토
```

권장:

- Soft Delete 기준을 Domain 전체에서 통일
- 모든 일반 조회에 삭제 제외 조건 포함
- Unique Constraint와 재사용 정책 검토
- deleted_at / active 조건 Index 검토
- JPA @Where, @SQLDelete 같은 기능 사용 시 실제 SQL 확인
- 관리자 조회는 삭제 포함 여부 명확화

---

### [FAQ]

Q. Soft Delete는 Constraint와 왜 연결돼?
A. 삭제된 Row도 DB에 남아 있으므로 Unique Constraint, FK, Index에 계속 영향을 주기 때문이다.

Q. Soft Delete 후 같은 email을 다시 쓸 수 있어?
A. Unique Constraint 정책에 따라 다르며 재사용이 필요하면 별도 설계를 검토해야 한다.

Q. Soft Delete 조회 조건은 어디에 넣어야 해?
A. Repository Query, QueryDSL 조건, JPQL, Native Query 등 모든 일반 조회에 일관되게 포함해야 한다.

Q. JPA @Where를 쓰면 Soft Delete 문제가 완전히 해결돼?
A. 아니다. Native Query, 관리자 조회, Unique Constraint, 연관관계 조회 등은 별도 검토가 필요하다.

---

# 6. Performance Review

## 6.1 Execution Plan Basics

### [개념]

Execution Plan은 DBMS가 SQL Query를 어떻게 실행할지 보여주는 실행 계획이다.

Index 사용 여부, Join 방식, Scan 방식, 정렬 비용, Row 추정치를 확인하는 성능 검토 도구다.

JPA, JPQL, QueryDSL을 사용해도 최종적으로 생성된 SQL의 Execution Plan을 확인해야 한다.

---

### [핵심]

Execution Plan 확인 대상:

- Full Table Scan
- Index Scan
- Index Seek
- Join Order
- Join Type
- Rows Estimate
- Filter Condition
- Sort Operation
- Temporary Table
- Using Filesort
- Using Where

검토 기준:

- 예상 Row 수
- 실제 데이터 크기
- Index 사용 여부
- 정렬 비용
- JOIN 비용
- 조건 적용 순서
- Query Rewrite 가능성
- ORM 생성 SQL 적절성

---

### [실무]

MySQL 기준 예시:

```sql
EXPLAIN
SELECT festival_id, title
FROM festivals
WHERE region_code = '11'
ORDER BY event_start_date ASC
LIMIT 20;
```

검토 Flow:

```text
Slow Query 확인
→ JPA / QueryDSL 생성 SQL 확인
→ EXPLAIN 실행
→ Table 접근 방식 확인
→ possible_keys / key 확인
→ rows 확인
→ Extra 확인
→ Index 또는 Query Rewrite 검토
```

주의:

- Execution Plan은 추정 기반일 수 있음
- 작은 Table의 Full Scan은 자연스러울 수 있음
- Index를 사용해도 항상 빠른 것은 아님
- 대량 정렬 / 임시 Table 발생 여부 확인
- 실제 실행 시간과 함께 판단
- ORM Query는 반드시 생성 SQL 기준으로 판단

---

### [FAQ]

Q. Execution Plan은 뭐야?
A. DBMS가 SQL Query를 어떤 방식으로 실행할지 보여주는 계획이다.

Q. JPA를 쓰는데 Execution Plan이 필요해?
A. 필요하다. JPA가 생성한 SQL도 DB에서 실행되므로 성능 검토는 Execution Plan 기준으로 해야 한다.

Q. Full Table Scan은 항상 나빠?
A. 아니다. 작은 Table이나 대부분의 Row가 필요한 경우에는 Full Scan이 자연스러울 수 있다.

Q. Index를 사용하면 항상 빨라?
A. 아니다. 선택도, 데이터 양, 정렬, JOIN 구조에 따라 Index 사용이 오히려 불리할 수도 있다.

---

## 6.2 Slow Query Review

### [개념]

Slow Query Review는 SQL 실행 시간이 느릴 때 원인을 분석하고 개선 방향을 찾는 과정이다.

Slow Query는 SQL 자체, Index, 데이터 양, JOIN, Pagination, Lock, JPA N+1 문제에서 발생할 수 있다.

---

### [핵심]

Slow Query 원인:

- Missing Index
- Full Table Scan
- Large OFFSET
- Inefficient JOIN
- 1:N Join Explosion
- Function on Indexed Column
- Leading Wildcard LIKE
- Large Sort
- Large Group By
- N+1 Query
- Unnecessary Column
- Unnecessary JOIN
- Lock Wait
- Fetch Join Misuse
- Count Query Cost

---

### [실무]

Slow Query Debug Flow:

```text
Slow Query 확인
→ 실행 빈도 확인
→ Query Purpose 확인
→ 생성 SQL 확인
→ WHERE / JOIN Column 확인
→ Index 존재 확인
→ Execution Plan 확인
→ SELECT Column 축소
→ Pagination 방식 검토
→ JOIN 구조 검토
→ JPA Fetch Strategy 검토
→ Query Rewrite
→ 재측정
```

개선 예시:

```text
문제: 축제 검색이 느림
원인: title LIKE '%keyword%' + 대량 데이터
검토:
- Full Text Search
- 검색 엔진
- prefix 검색 가능성
- 검색 조건 제한
- Pagination Index
```

개선 예시:

```text
문제: 알림 목록이 느림
원인: user_id 조건 + created_at 정렬에 적합한 Index 없음
검토:
- notifications(user_id, created_at DESC) Index
- notifications(user_id, read_status, created_at DESC) Index
- Cursor Pagination
```

JPA 개선 예시:

```text
문제: 목록 조회가 느림
원인 후보:
- Entity 전체 조회
- DTO 변환 중 Lazy Loading
- N+1 Query
- Count Query 과다
- Fetch Join + Pagination

검토:
- DTO Projection
- Fetch Join 제한 사용
- Batch Size
- Slice 사용
- QueryDSL Projection
```

---

### [FAQ]

Q. 쿼리가 느리면 무조건 Index를 추가하면 돼?
A. 아니다. 조건, JOIN, 정렬, 데이터 양, 실행 계획을 먼저 확인한 뒤 필요한 Index만 추가해야 한다.

Q. Slow Query는 SQL만 문제야?
A. 아니다. JPA N+1, Fetch 전략, Lock 대기, 네트워크, 데이터 양도 원인이 될 수 있다.

Q. Large OFFSET은 왜 느려?
A. DB가 앞의 많은 Row를 건너뛴 뒤 필요한 Row를 반환해야 하기 때문이다.

Q. Slow Query 개선 후에는 무엇을 해야 해?
A. 실행 시간과 Execution Plan을 다시 확인해 실제 개선 여부를 검증해야 한다.

---

# 7. Index, Pagination, Transaction, Constraint Review

## 7.1 Review Flow

### [개념]

Index, Pagination, Transaction, Constraint Review는 SQL Query의 성능, 안정성, 정합성을 검수하는 과정이다.

Agent는 Query 생성 후 결과 정확성뿐 아니라 성능, 데이터 무결성, JPA 연계 가능성까지 확인해야 한다.

---

### [핵심]

Review Flow:

```text
Query Purpose 확인
→ WHERE / JOIN / ORDER BY Column 확인
→ Index 후보 검토
→ Pagination 안정성 확인
→ Transaction 필요 여부 확인
→ Constraint 충돌 확인
→ JPA Entity / Repository 연계 확인
→ Execution Plan 필요 여부 확인
→ Final Review
```

검토 대상:

- Index Candidate
- Sargable Condition
- Composite Index
- Pagination Type
- Stable Sort
- Transaction Boundary
- Isolation Requirement
- Lock Requirement
- Constraint
- Entity Mapping
- Cascade
- Soft Delete
- Execution Plan

---

### [실무]

목록 Query 검수:

```text
축제 목록 검색
→ region_code 조건
→ event_start_date 정렬
→ LIMIT / OFFSET
→ region_code + event_start_date Index 검토
→ ORDER BY 안정성 확인
→ JPA Pageable / QueryDSL 적용 가능성 확인
```

변경 Query 검수:

```text
찜 등록
→ favorites INSERT
→ user_id + festival_id Unique Constraint 확인
→ JPA @Table(uniqueConstraints) 확인
→ 동시 요청 중복 가능성 확인
→ Transaction / 예외 처리 검토
```

동시성 Query 검수:

```text
선착순 신청
→ 현재 신청 수 확인
→ 신청 Row INSERT
→ Unique / Lock / Transaction 검토
→ Race Condition 방지 필요
→ JPA @Lock 또는 @Version 검토 가능
```

Soft Delete 검수:

```text
게시글 삭제
→ Physical Delete인지 Soft Delete인지 확인
→ deleted_at 갱신
→ 일반 조회 deleted_at IS NULL 조건 확인
→ Unique Constraint 충돌 확인
→ JPA @Where / @SQLDelete 사용 여부 확인
```

---

### [FAQ]

Q. Part04 검수에서 가장 중요한 것은?
A. Index 가능성, Pagination 안정성, Transaction 필요 여부, Constraint 기반 무결성, JPA 연계 가능성이다.

Q. 성능 검토는 언제 해?
A. Query Purpose와 WHERE, JOIN, ORDER BY가 정해진 뒤 Index와 Execution Plan 기준으로 검토한다.

Q. 정합성 검토는 어디서 해?
A. Transaction, Constraint, Lock, Unique, FK, Cascade, Soft Delete 기준으로 검토한다.

Q. Agent가 SQL을 만들 때 JPA 연계까지 봐야 해?
A. 그렇다. SQL Foundation은 JPA, QueryDSL, Repository 구현으로 연결되어야 한다.

---

## 7.2 Common Mistakes

### [개념]

Common Mistakes는 Index, Pagination, Transaction, Constraint 영역에서 자주 발생하는 실수다.

이 실수들은 Query 성능 저하, 데이터 중복, 정합성 붕괴, JPA Mapping 오류, 운영 장애로 이어질 수 있다.

---

### [핵심]

자주 발생하는 실수:

- Index 없는 대량 검색
- Query 없이 추측으로 Index 추가
- 낮은 선택도 Column 단독 Index 남용
- Composite Index Column 순서 오류
- Column에 함수 적용
- 타입 불일치 비교
- ORDER BY 없는 Pagination
- 큰 OFFSET 무시
- Cursor 조건과 ORDER BY 불일치
- 1:N JOIN 후 Pagination
- totalCount 무조건 실행
- Transaction 누락
- Transaction 범위 과도
- 외부 API 호출을 Transaction 내부에 오래 유지
- Unique Constraint 없이 중복 방지
- FK 영향 미검토
- JPA Annotation과 DB Constraint 불일치
- Soft Delete와 Unique 충돌 미검토
- Cascade / Orphan Removal 오용
- Lock 사용 후 Deadlock 미검토

---

### [실무]

문제와 해결 예시:

```text
문제: 알림 목록 조회가 느림
원인: user_id 조건과 created_at 정렬에 맞는 Index 없음
해결: notifications(user_id, created_at DESC) Index 검토
```

```text
문제: 페이지 이동 시 중복 데이터 발생
원인: ORDER BY created_at만 사용하고 created_at 중복 발생
해결: ORDER BY created_at DESC, id DESC로 Stable Sort 보장
```

```text
문제: 찜 중복 등록 발생
원인: Application exists check만 사용하고 Unique Constraint 없음
해결: UNIQUE(user_id, festival_id) 추가 및 중복 예외 처리
```

```text
문제: JPA Entity는 nullable=false인데 DB에는 NULL 허용
원인: Entity Annotation과 DB Schema 불일치
해결: Migration Script로 DB NOT NULL Constraint 반영
```

```text
문제: Soft Delete 후 같은 email 재가입 실패
원인: deleted_at Row가 Unique Constraint에 계속 영향
해결: 재사용 정책, Partial Unique Index, anonymization 검토
```

---

### [FAQ]

Q. Index에서 가장 흔한 실수는?
A. Query 패턴 없이 Index를 만들거나 Composite Index Column 순서를 잘못 잡는 것이다.

Q. Pagination에서 가장 흔한 실수는?
A. ORDER BY 없이 LIMIT / OFFSET을 사용하거나 Stable Sort를 보장하지 않는 것이다.

Q. Transaction에서 가장 흔한 실수는?
A. 여러 변경 작업을 하나의 Transaction으로 묶지 않거나 Transaction 범위를 너무 넓게 잡는 것이다.

Q. JPA 연계에서 가장 흔한 실수는?
A. Entity Annotation과 실제 DB Constraint가 불일치하는 것이다.

---

## 7.3 Checklist

### [개념]

Checklist는 Index, Pagination, Transaction, Constraint 관련 SQL을 최종 검수하기 위한 기준이다.

Agent는 Query 생성 후 Checklist 기준으로 성능, 데이터 정합성, JPA 연계 문제를 탐지해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Query Purpose가 명확한가?
- [ ] WHERE Column이 Index 후보인지 검토했는가?
- [ ] JOIN Column이 Index 후보인지 검토했는가?
- [ ] ORDER BY Column이 Index와 연결되는가?
- [ ] GROUP BY Column이 성능 검토 대상인가?
- [ ] Composite Index Column 순서가 Query 조건과 맞는가?
- [ ] 조건이 Sargable한가?
- [ ] Column에 함수 / 연산 / 형변환을 적용하지 않았는가?
- [ ] LIKE 검색의 wildcard 위치를 검토했는가?
- [ ] Pagination에 ORDER BY가 있는가?
- [ ] Pagination 정렬이 Stable Sort인가?
- [ ] 중복 정렬 값에 PK Tie-breaker를 추가했는가?
- [ ] OFFSET이 커질 가능성을 검토했는가?
- [ ] Cursor Pagination이 더 적합한지 검토했는가?
- [ ] Cursor 조건과 ORDER BY가 일치하는가?
- [ ] totalCount Query가 정말 필요한가?
- [ ] Page / Slice 선택이 API 요구사항과 일치하는가?
- [ ] 여러 변경 작업에 Transaction이 필요한가?
- [ ] Transaction 범위가 과도하게 넓지 않은가?
- [ ] 외부 API 호출과 DB Transaction 경계를 검토했는가?
- [ ] Isolation Level 변경이 필요한지 검토했는가?
- [ ] Lock이 필요한 동시성 요구사항인가?
- [ ] Deadlock 가능성을 검토했는가?
- [ ] Primary Key가 명확한가?
- [ ] Foreign Key 영향이 검토되었는가?
- [ ] Unique Constraint로 중복 방지를 보장하는가?
- [ ] Not Null로 필수 값을 보장하는가?
- [ ] Check Constraint로 허용 범위를 제한하는가?
- [ ] Default Value 기준이 Application과 충돌하지 않는가?
- [ ] Entity Annotation과 DB Constraint가 일치하는가?
- [ ] JPA Cascade와 DB Cascade를 혼동하지 않았는가?
- [ ] orphanRemoval 적용 대상이 적절한가?
- [ ] Soft Delete와 Unique Constraint 충돌을 검토했는가?
- [ ] Soft Delete 조회 조건이 일반 조회에 포함되었는가?
- [ ] Slow Query는 Execution Plan으로 확인했는가?
- [ ] JPA / QueryDSL 생성 SQL을 확인했는가?
```

---

### [실무]

검수 Flow:

```text
Draft Query
→ Index Review
→ Sargable Review
→ Pagination Review
→ Transaction Review
→ Constraint Review
→ JPA Mapping Review
→ Cascade / Soft Delete Review
→ Lock / Isolation Review
→ Execution Plan Review
→ Final SQL
```

치명적 문제:

- WHERE / JOIN Column Index 미검토
- ORDER BY 없는 Pagination
- Stable Sort 미보장
- Cursor 조건 오류
- 큰 OFFSET 방치
- Transaction 누락
- Unique Constraint 누락
- FK 삭제 영향 미검토
- Entity / DB Constraint 불일치
- Soft Delete 조건 누락
- Non-Sargable 조건
- Lock / Deadlock 미검토

---

### [FAQ]

Q. Part04 Checklist의 핵심은 뭐야?
A. Index, Sargable Query, Pagination 안정성, Transaction 정합성, Constraint 무결성, JPA 연계 검수다.

Q. 치명적인 성능 문제는 뭐야?
A. Index 없는 대량 검색, Non-Sargable 조건, 큰 OFFSET, 불필요한 JOIN, 대량 Sort가 치명적이다.

Q. 치명적인 정합성 문제는 뭐야?
A. Transaction 누락, Unique Constraint 누락, FK 영향 미검토, Entity / DB Constraint 불일치, 동시성 Lock 미검토가 치명적이다.

Q. 최종 SQL 검수는 무엇으로 끝내?
A. Checklist 검토 후 필요한 경우 Execution Plan과 실제 테스트 결과로 검증한다.

---

# Retrieval Queries

### [FAQ]

Q. SQL Part04는 무엇을 다뤄?
A. Index, Pagination, Transaction, Isolation, Lock, Constraint, JPA 연계, Execution Plan, Slow Query Review 기준을 다룬다.

Q. Index는 뭐야?
A. Table에서 특정 Column 기준으로 Row를 빠르게 찾기 위한 자료구조다.

Q. Index는 언제 만들어?
A. 자주 조회 조건, JOIN 조건, 정렬 조건으로 사용되는 Column에 대해 성능 문제가 있거나 예상될 때 검토한다.

Q. JPA를 쓰면 Index를 몰라도 돼?
A. 아니다. JPA도 SQL을 생성하므로 WHERE, JOIN, ORDER BY에 맞는 Index 검토가 필요하다.

Q. 어떤 Column이 Index 후보야?
A. WHERE, JOIN, ORDER BY, GROUP BY, Pagination에 자주 사용되는 Column이 후보가 된다.

Q. Soft Delete Column도 Index 후보야?
A. deleted_at, active 같은 조건이 반복 조회에 항상 포함되면 다른 조건 Column과 복합 Index로 검토할 수 있다.

Q. Composite Index는 뭐야?
A. 두 개 이상의 Column을 함께 구성한 Index다.

Q. Composite Index에서 Column 순서가 왜 중요해?
A. Index는 왼쪽 Column부터 순서대로 활용되므로 Query 조건과 맞지 않으면 효율이 떨어질 수 있다.

Q. Cursor Pagination도 Composite Index와 관련 있어?
A. 관련 있다. Cursor 조건과 ORDER BY Column이 Index 순서와 맞아야 안정적인 성능을 기대할 수 있다.

Q. Sargable Query는 뭐야?
A. Index를 효율적으로 사용할 수 있는 형태의 검색 조건이다.

Q. QueryDSL을 쓰면 Sargable 문제를 피할 수 있어?
A. 아니다. QueryDSL도 SQL로 변환되므로 생성 SQL이 Sargable한지 확인해야 한다.

Q. Pagination은 뭐야?
A. 목록 데이터를 일정 개수씩 나누어 조회하는 방식이다.

Q. Pagination에서 가장 중요한 것은?
A. ORDER BY와 Stable Sort다. 정렬 기준이 없으면 결과 순서가 흔들릴 수 있다.

Q. JPA Page와 Slice는 어떻게 골라?
A. totalCount가 필요하면 Page, hasNext만 필요하면 Slice가 적합하다.

Q. OFFSET Pagination은 언제 사용해?
A. 페이지 번호 기반 목록, 관리자 화면, 검색 결과 페이지에 적합하다.

Q. JPA Page를 쓰면 Count Query도 고려해야 해?
A. 그렇다. Page는 totalCount가 필요하므로 Count Query 비용을 검토해야 한다.

Q. Cursor Pagination은 언제 사용해?
A. 무한 스크롤, 채팅, 알림, 피드처럼 순차적으로 다음 목록을 가져올 때 사용한다.

Q. Cursor 조건과 ORDER BY가 왜 맞아야 해?
A. 정렬 기준과 Cursor 조건이 다르면 중복 또는 누락 데이터가 발생할 수 있기 때문이다.

Q. Fetch Join과 Pagination은 왜 주의해야 해?
A. ORM 환경에서 메모리 Pagination이나 중복 Row 문제가 발생할 수 있기 때문이다.

Q. Transaction은 뭐야?
A. 여러 데이터 변경 작업을 하나의 작업 단위로 묶어 모두 성공하거나 모두 실패하도록 보장하는 개념이다.

Q. JPA에서 Transaction은 왜 중요해?
A. Persistence Context, Dirty Checking, Flush, Commit, Rollback이 Transaction과 함께 동작하기 때문이다.

Q. Spring에서는 Transaction을 어디에 적용해?
A. 보통 여러 Repository 변경을 묶는 Service Method에 @Transactional을 적용한다.

Q. ACID는 뭐야?
A. Transaction의 Atomicity, Consistency, Isolation, Durability 속성을 의미한다.

Q. JPA에서도 ACID가 중요해?
A. 중요하다. JPA Entity 변경도 Transaction Commit 시 DB에 반영되므로 ACID 기준으로 검토해야 한다.

Q. Isolation Level은 뭐야?
A. 동시에 실행되는 Transaction들이 서로 어떤 수준으로 격리되는지 결정하는 기준이다.

Q. JPA Persistence Context와 Isolation Level은 같아?
A. 아니다. Persistence Context는 JPA 1차 캐시이고 Isolation Level은 DB Transaction 격리 기준이다.

Q. Lock은 언제 필요해?
A. 동시에 같은 데이터를 변경할 때 정합성 문제가 발생할 수 있으면 검토한다.

Q. JPA에서 Optimistic Lock은 무엇과 연결돼?
A. Entity의 @Version Column과 연결된다.

Q. Constraint는 뭐야?
A. Table에 저장되는 데이터의 무결성을 보장하기 위한 제약 조건이다.

Q. JPA Annotation만 있으면 DB Constraint는 없어도 돼?
A. 아니다. JPA Annotation과 실제 DB Constraint가 일치해야 운영 데이터 무결성이 안정적으로 보장된다.

Q. Primary Key는 무엇에 사용해?
A. Row 식별, 단건 조회, 수정, 삭제, JOIN 참조, Entity 식별 기준으로 사용한다.

Q. Foreign Key는 왜 중요해?
A. Table 간 관계 무결성을 보장하고 JOIN 조건과 JPA 연관관계의 기준이 되기 때문이다.

Q. JPA Cascade와 DB Cascade는 같아?
A. 아니다. JPA Cascade는 Entity 상태 전파이고 DB Cascade는 DB Constraint 기반 삭제 / 수정 전파다.

Q. Unique Constraint는 언제 필요해?
A. email, user-festival favorite처럼 중복되면 안 되는 데이터에 필요하다.

Q. Application에서 중복 체크하면 Unique는 없어도 돼?
A. 아니다. 동시 요청에서는 중복이 발생할 수 있으므로 DB Unique Constraint가 필요하다.

Q. Soft Delete와 Unique는 왜 충돌할 수 있어?
A. 삭제 처리된 Row가 DB에 남아 있으면 같은 Unique 값을 다시 사용할 수 없을 수 있기 때문이다.

Q. Default는 DB에서 처리하는 게 좋아?
A. 프로젝트 기준에 따라 다르며 DB Default와 Application 초기값 중 하나로 일관성 있게 관리해야 한다.

Q. DB Default와 JPA 초기값을 동시에 쓰면 안전해?
A. 불일치 위험이 있으므로 하나의 기준으로 통일하는 것이 좋다.

Q. Entity Annotation과 DB Constraint가 달라도 돼?
A. 권장하지 않는다. 둘이 다르면 Application 기준과 DB 기준이 달라져 데이터 무결성 문제가 생길 수 있다.

Q. orphanRemoval은 언제 사용해?
A. 부모와 관계가 끊긴 자식 Entity가 더 이상 독립적으로 존재하면 안 될 때 사용한다.

Q. Soft Delete 조회 조건은 어디에 넣어야 해?
A. Repository Query, QueryDSL 조건, JPQL, Native Query 등 모든 일반 조회에 일관되게 포함해야 한다.

Q. JPA @Where를 쓰면 Soft Delete 문제가 완전히 해결돼?
A. 아니다. Native Query, 관리자 조회, Unique Constraint, 연관관계 조회 등은 별도 검토가 필요하다.

Q. JPA를 쓰는데 Execution Plan이 필요해?
A. 필요하다. JPA가 생성한 SQL도 DB에서 실행되므로 성능 검토는 Execution Plan 기준으로 해야 한다.

Q. Slow Query는 SQL만 문제야?
A. 아니다. JPA N+1, Fetch 전략, Lock 대기, 네트워크, 데이터 양도 원인이 될 수 있다.

Q. Part04 검수에서 가장 중요한 것은?
A. Index 가능성, Pagination 안정성, Transaction 필요 여부, Constraint 기반 무결성, JPA 연계 가능성이다.

Q. JPA 연계에서 가장 흔한 실수는?
A. Entity Annotation과 실제 DB Constraint가 불일치하는 것이다.

Q. Part04 Checklist의 핵심은 뭐야?
A. Index, Sargable Query, Pagination 안정성, Transaction 정합성, Constraint 무결성, JPA 연계 검수다.
