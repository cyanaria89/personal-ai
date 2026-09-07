# 01. DB 전용 테스트 프롬프트

## DB-01. 테이블 설계 요청

### 테스트 프롬프트

```text
회원, 권한, 로그인 이력을 관리할 수 있는 DB 테이블 구조를 설계해줘.
PK, FK, 주요 컬럼, 관계, 인덱스 후보까지 포함해줘.
```

### 기대 Workflow

```text
PM → DB → Review
```

### 기대 동작

- PM Agent가 DB 중심 요청으로 분류해야 함
- Backend / Frontend Agent를 바로 호출하지 않아야 함
- DB Agent가 테이블, 관계, 제약조건, 인덱스 후보를 제시해야 함
- Review Agent가 누락된 관계, 과도한 정규화, 중복 컬럼을 검토해야 함

### 검증 체크리스트

```text
[ ] PM이 DB Agent 호출을 선택했는가?
[ ] Backend/Frontend를 불필요하게 호출하지 않았는가?
[ ] PK/FK/관계가 명확한가?
[ ] 인덱스 후보가 근거 있게 제시되었는가?
[ ] Review가 실제 검토 의견을 냈는가?
```

---

## DB-02. 기존 DB 구조 검토 요청

### 테스트 프롬프트

```text
아래 테이블 구조에서 관계상 문제가 있는지 검토해줘.
users(id, email, password, role_id)
roles(id, role_name)
login_histories(id, user_id, login_at, ip_address)
```

### 기대 Workflow

```text
PM → DB → Review
```

### 기대 동작

- DB Agent가 users-role, users-login_histories 관계를 검토해야 함
- FK, unique, nullability, 인덱스 필요성을 언급해야 함
- Review Agent가 보안/이력 관점의 누락 가능성을 검토해야 함

### 검증 체크리스트

```text
[ ] role_id FK 필요성을 확인했는가?
[ ] email unique 필요성을 언급했는가?
[ ] login_histories.user_id 인덱스 필요성을 언급했는가?
[ ] 비밀번호 저장 방식에 대해 추측하지 않고 보안 후보로만 언급했는가?
```
