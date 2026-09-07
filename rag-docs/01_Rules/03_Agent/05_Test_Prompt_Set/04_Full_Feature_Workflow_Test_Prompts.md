# 04. 전체 기능 Workflow 테스트 프롬프트

## FULL-01. 신규 기능 전체 설계 요청

### 테스트 프롬프트

```text
게시글 작성 기능을 DB부터 Backend API, Frontend 화면까지 순서대로 설계해줘.
작성자, 제목, 내용, 작성일, 수정일이 필요하고 목록 조회와 상세 조회도 필요해.
```

### 기대 Workflow

```text
PM → DB → Backend → Frontend → Review
```

### 기대 동작

- PM Agent가 전체 기능 요청으로 분류해야 함
- DB Agent가 posts 테이블과 작성자 관계를 먼저 설계해야 함
- Backend Agent가 DB 결과를 기반으로 Entity/Repository/Service/Controller/DTO를 설계해야 함
- Frontend Agent가 API 구조를 기준으로 화면을 설계해야 함
- Review Agent가 DB-Backend-Frontend 연결 누락을 검토해야 함

### 검증 체크리스트

```text
[ ] DB부터 순차 진행했는가?
[ ] Backend가 DB Agent 결과를 반영했는가?
[ ] Frontend가 Backend API 결과를 반영했는가?
[ ] Review가 전체 연결성을 검토했는가?
[ ] 각 단계의 산출물이 다음 단계로 전달되었는가?
```

---

## FULL-02. 기존 기능 확장 요청

### 테스트 프롬프트

```text
기존 게시글 기능에 댓글 기능을 추가하려고 해.
댓글은 게시글에 속하고, 작성자와 작성일을 가져야 해.
DB, Backend, Frontend 순서로 필요한 변경사항을 정리해줘.
```

### 기대 Workflow

```text
PM → DB → Backend → Frontend → Review
```

### 기대 동작

- DB Agent가 comments 테이블과 posts/users 관계를 설계해야 함
- Backend Agent가 댓글 CRUD 또는 필요한 API 범위를 설계해야 함
- Frontend Agent가 댓글 목록/작성 UI를 설계해야 함
- Review Agent가 삭제 정책, N+1, 권한, 화면 상태 등을 검토해야 함

### 검증 체크리스트

```text
[ ] comments 테이블 관계가 명확한가?
[ ] Backend API가 DB 구조와 일치하는가?
[ ] Frontend가 API 흐름과 일치하는가?
[ ] Review가 누락 가능성을 지적했는가?
```
