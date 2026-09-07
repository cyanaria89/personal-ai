# 90. Request Type Routing Map

## 1. 목적

이 문서는 사용자 요청 유형에 따라 PM Agent가 어떤 Agent를 어떤 순서로 호출해야 하는지 정의한다.

초기 운영에서는 순차 실행을 기본값으로 한다.

## 2. 기본 원칙

```text
1. 모든 요청은 PM Agent가 먼저 분석한다.
2. DB 변경 여부를 먼저 판단한다.
3. DB 변경이 있으면 DB Agent 결과를 Backend Agent에게 전달한다.
4. Backend API 변경이 있으면 Frontend Agent에게 API Contract를 전달한다.
5. 모든 주요 작업은 Review Agent를 거친다.
```

## 3. Routing Table

| 요청 유형 | 실행 순서 | 비고 |
|---|---|---|
| 신규 기능 전체 구현 | PM → DB → Backend → Frontend → Review | 기본 전체 흐름 |
| DB 테이블 설계 | PM → DB → Review | Backend 구현 없음 |
| DB 설계 + Backend 구현 | PM → DB → Backend → Review | 화면 없음 |
| Backend API 구현 | PM → Backend → Review | DB 변경 없을 때 |
| Backend API + Frontend 연동 | PM → Backend → Frontend → Review | 기존 DB 기준 |
| Frontend 화면 구현 | PM → Frontend → Review | API가 이미 있을 때 |
| Frontend 화면 + API 명세 필요 | PM → Backend → Frontend → Review | API Contract 필요 |
| 코드 리뷰 | PM → Review | 범위가 명확하면 직접 Review |
| DB/Backend/Frontend 전체 검토 | PM → DB → Backend → Frontend → Review | 구조 검토 요청 |
| 테스트 케이스 작성 | PM → Review | 초기에는 Review가 Test 관점 포함 |
| 보안 검토 | PM → Backend → Review | 초기에는 Backend + Review가 담당 |
| 배포/운영 간단 검토 | PM → Backend → Review | DevOps Agent 분리 전까지 임시 |
| RAG 문서 보강 후보 정리 | PM → Review | RAG Update Agent 분리 전까지 임시 |
| Agent Rules 수정 | PM → Review | Master/Agent 문서 영향 검토 |
| System Prompt 수정 | PM → Review | Agent 동작 영향 검토 |
| RAG Expert 문서 추가 | PM → Review | Mapping 수정 필요 |

## 4. DB Agent 생략 기준

다음 조건을 모두 만족하면 DB Agent를 생략할 수 있다.

```text
- 신규 테이블 없음
- 기존 테이블 컬럼 변경 없음
- 관계 변경 없음
- 저장 데이터 구조 변경 없음
- 조회 조건/집계 구조가 기존 범위 안에 있음
```

## 5. Backend Agent 생략 기준

다음 조건을 모두 만족하면 Backend Agent를 생략할 수 있다.

```text
- API 변경 없음
- 인증/인가 변경 없음
- 서버 로직 변경 없음
- DB 접근 로직 변경 없음
- 응답 형식 변경 없음
```

## 6. Frontend Agent 생략 기준

다음 조건을 모두 만족하면 Frontend Agent를 생략할 수 있다.

```text
- 화면 변경 없음
- API 호출 방식 변경 없음
- 상태 관리 변경 없음
- 폼/검증 변경 없음
- 사용자 UX 변경 없음
```

## 7. Review Agent 생략 기준

초기 운영에서는 원칙적으로 Review Agent를 생략하지 않는다.

단, 단순 설명/질문 답변처럼 산출물이 없는 경우 PM Agent가 자체 응답할 수 있다.

## 8. 순차 실행 예시

### 신규 기능 전체 구현

```text
User Request
↓
PM Agent: 요구사항 분석 / DB 영향 있음 판단
↓
DB Agent: 테이블/관계/SQL 설계
↓
Backend Agent: Entity/API/Service 구현
↓
Frontend Agent: 화면/API 연동 구현
↓
Review Agent: 전체 검토
↓
Final Answer
```

### 화면만 수정

```text
User Request
↓
PM Agent: DB/Backend 영향 없음 판단
↓
Frontend Agent: 화면 수정
↓
Review Agent: UX/API 영향 검토
↓
Final Answer
```

### 코드 리뷰만 요청

```text
User Request
↓
PM Agent: 리뷰 범위 판단
↓
Review Agent: 검토
↓
Final Answer
```

