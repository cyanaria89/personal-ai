# 03. Frontend 전용 테스트 프롬프트

## FE-01. 기존 API 기준 화면 설계 요청

### 테스트 프롬프트

```text
이미 GET /api/users API가 있고 응답은 아래와 같아.
[
  { "id": 1, "email": "a@test.com", "roleName": "ADMIN" }
]
React 기준으로 회원 목록 화면 컴포넌트 구조를 설계해줘.
Backend와 DB는 수정하지 마.
```

### 기대 Workflow

```text
PM → Frontend → Review
```

### 기대 동작

- PM Agent가 Frontend 전용 요청으로 분류해야 함
- Backend / DB Agent를 호출하지 않아야 함
- Frontend Agent가 컴포넌트, API 호출, 로딩/에러 상태를 설계해야 함
- Review Agent가 UX, 상태 관리, API 응답 처리 누락을 검토해야 함

### 검증 체크리스트

```text
[ ] DB/Backend Agent를 생략했는가?
[ ] API 응답 구조를 기준으로 화면을 설계했는가?
[ ] loading/error/empty 상태를 고려했는가?
[ ] 컴포넌트 책임이 분리되었는가?
```

---

## FE-02. Form Validation 요청

### 테스트 프롬프트

```text
React에서 회원 등록 폼을 만들려고 해.
이메일, 비밀번호, 이름 입력값에 대한 기본 validation 구조를 제안해줘.
API 설계나 DB 설계는 제외해줘.
```

### 기대 Workflow

```text
PM → Frontend → Review
```

### 기대 동작

- Frontend Agent가 폼 상태, validation, 에러 메시지 처리 중심으로 답해야 함
- Backend validation이나 DB 제약조건으로 과하게 확장하지 않아야 함

### 검증 체크리스트

```text
[ ] Frontend validation 중심으로 작성했는가?
[ ] 불필요한 DB/API 설계를 하지 않았는가?
[ ] 사용자 입력 오류 표시 방식을 포함했는가?
```
