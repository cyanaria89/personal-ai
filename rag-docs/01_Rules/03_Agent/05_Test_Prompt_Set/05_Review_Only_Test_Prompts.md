# 05. Review 전용 테스트 프롬프트

## RV-01. 설계안 검토 요청

### 테스트 프롬프트

```text
아래 설계안에 문제가 있는지 리뷰해줘.
- users 테이블에 roleName 문자열을 직접 저장
- 게시글 목록 API에서 Entity를 그대로 반환
- React 화면에서 API 에러 처리를 하지 않음
```

### 기대 Workflow

```text
PM → Review
```

또는 Review가 필요 시 하위 검토 관점으로만 분리:

```text
PM → Review
```

### 기대 동작

- PM Agent가 신규 설계가 아니라 검토 요청으로 분류해야 함
- Review Agent가 DB/Backend/Frontend 관점 문제를 나눠서 검토해야 함
- 필요한 경우 RAG Update Candidate가 아니라 수정 권장사항을 제시해야 함

### 검증 체크리스트

```text
[ ] Review 중심으로 처리했는가?
[ ] roleName 직접 저장 문제를 지적했는가?
[ ] Entity 직접 반환 문제를 지적했는가?
[ ] Frontend 에러 처리 누락을 지적했는가?
[ ] 개선 방향을 구체적으로 제시했는가?
```

---

## RV-02. Agent 산출물 통합 검토 요청

### 테스트 프롬프트

```text
DB Agent가 작성한 테이블 설계와 Backend Agent가 작성한 Entity 설계가 서로 맞는지 검토해줘.
컬럼명, 타입, 관계, null 허용 여부, DTO 응답 구조까지 확인해줘.
```

### 기대 Workflow

```text
PM → Review
```

### 기대 동작

- Review Agent가 산출물 간 일치성 검토에 집중해야 함
- 새로운 설계를 추가하기보다 불일치/누락/위험을 찾아야 함

### 검증 체크리스트

```text
[ ] DB와 Entity 매핑 일치성을 확인했는가?
[ ] nullable/타입/관계 불일치를 확인했는가?
[ ] DTO 응답 구조까지 검토했는가?
```
