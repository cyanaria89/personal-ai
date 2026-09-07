# 02. DB Agent RAG Map

## 1. 목적

DB Agent는 데이터 모델링, 테이블 설계, 관계, 제약조건, 인덱스, SQL, ERD 관점 검토를 담당한다.

Backend Agent와 밀접하게 연결되지만, DB Agent의 1차 책임은 데이터 구조의 일관성과 안정성이다.

## 2. Required Master Documents

```text
01_Master/Agent_Build_Context.md
01_Master/Master_RAG_Rules.md
01_Master/Project_Progress.md
01_Master/RAG_Document_Operation_Rules_Addendum.md
```

## 3. Required Agent Documents

```text
Agent_Rules_v1/00_Common_Agent_Rules.md
Agent_Rules_v1/02_DB_Agent_Rules.md
Agent_System_Prompts_v1/00_Common_System_Prompt.md
Agent_System_Prompts_v1/02_DB_Agent_System_Prompt.md
```

## 4. Primary Domain Rules

```text
01_Backend/01_SQL_Domain_Rules.md
01_Backend/04_JPA_Advanced_Domain_Rules.md
01_Backend/06_QueryDSL_Practical_Domain_Rules.md
```

## 5. Secondary Domain Rules

```text
01_Backend/03_Spring_Boot_Domain_Rules.md
01_Backend/12_API_Design_Domain_Rules.md
01_Backend/13_Design_Pattern_Domain_Rules.md
01_Backend/07_Testing_Domain_Rules.md
```

## 6. Reference-only Domain Rules

```text
01_Backend/05_Security_Advanced_Domain_Rules.md
01_Backend/08_Redis_Domain_Rules.md
01_Backend/11_Docker_Domain_Rules.md
03_Frontend/08_Data_Fetching_REST_API_Integration_Domain_Rules.md
```

## 7. 작업 유형별 참조

| 작업 유형 | 우선 참조 |
|---|---|
| 테이블 설계 | SQL Domain Rules |
| PK/FK/관계 검토 | SQL + JPA Advanced |
| Entity 매핑 영향 검토 | JPA Advanced |
| 동적 조회 조건 | QueryDSL Practical |
| API 응답 구조와 데이터 구조 연결 | API Design |
| 테스트 데이터/검증 쿼리 | SQL + Testing |
| 캐시 영향 | Redis Reference-only |

## 8. DB Agent Output Handoff Format

```text
[DB Analysis]
- Request Summary:
- Data Model Impact:
- New Tables:
- Modified Tables:
- Relationships:
- Constraints:
- Index Candidates:

[DDL Draft]
```sql
-- SQL here
```

[Entity Mapping Notes]
- Backend Agent가 참고해야 할 Entity/JPA 매핑 주의사항

[Query Notes]
- 주요 조회/집계/동적 조건

[Risk / Review Points]
- 정규화/중복/성능/무결성 위험

[Handoff to Backend Agent]
- 구현 시 필요한 내용

[RAG Update Candidate]
- 필요한 경우에만 작성
```

## 9. Backend Agent로 넘길 때 필수 정보

```text
- 테이블명
- 컬럼명
- 타입
- nullable 여부
- PK/FK
- unique 여부
- enum/code table 여부
- createdAt/updatedAt 등 감사 컬럼 여부
- JPA 연관관계 주의사항
- cascade/orphanRemoval 사용 금지 또는 허용 여부
```

## 10. Future Split Support

| 분리 후보 | 현재 위치 | 분리 기준 |
|---|---|---|
| Performance Agent | 인덱스/쿼리 성능 검토 | 쿼리 튜닝 문서가 Expert로 확장될 때 |
| Data Migration Agent | DDL 변경/마이그레이션 | Flyway/Liquibase/운영 DB 변경이 중요해질 때 |
| NoSQL Agent | Redis/NoSQL 참조 | NoSQL Expert 문서 제작 후 |

