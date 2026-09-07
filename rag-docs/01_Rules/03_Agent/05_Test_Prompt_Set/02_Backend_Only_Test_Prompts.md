# 02. Backend 전용 테스트 프롬프트

## BE-01. 기존 테이블 기준 API 구조 요청

### 테스트 프롬프트

```text
이미 users 테이블과 roles 테이블은 있다고 가정하고,
회원 목록 조회 API의 Controller, Service, Repository, DTO 구조를 설계해줘.
DB 테이블 변경은 하지 말고 Backend 구조만 작성해줘.
```

### 기대 Workflow

```text
PM → Backend → Review
```

### 기대 동작

- PM Agent가 DB 변경 불필요로 판단해야 함
- Backend Agent가 Controller / Service / Repository / DTO를 분리해야 함
- DB Agent를 호출하지 않아야 함
- Review Agent가 계층 분리, DTO 사용, 예외/권한 체크 누락을 검토해야 함

### 검증 체크리스트

```text
[ ] DB Agent를 생략했는가?
[ ] Backend 계층 구조가 명확한가?
[ ] Entity를 직접 응답하지 않고 DTO 사용을 권장했는가?
[ ] Review가 권한/예외/페이징 여부를 확인했는가?
```

---

## BE-02. Service 로직 리팩토링 요청

### 테스트 프롬프트

```text
Controller에 비즈니스 로직이 많이 들어가 있는 상황이야.
Spring Boot 기준으로 Service 계층으로 분리하는 리팩토링 방향을 제안해줘.
```

### 기대 Workflow

```text
PM → Backend → Review
```

### 기대 동작

- Backend Agent가 Controller / Service 책임 분리를 설명해야 함
- DB 설계로 흐르지 않아야 함
- Review Agent가 계층 책임 위반 여부를 검토해야 함

### 검증 체크리스트

```text
[ ] Controller 책임을 요청/응답 처리로 제한했는가?
[ ] Service 책임을 비즈니스 로직으로 분리했는가?
[ ] Repository 직접 호출 위치를 올바르게 정리했는가?
[ ] 과도한 설계 확장을 하지 않았는가?
```
