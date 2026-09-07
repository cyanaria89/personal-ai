# 90. 테스트 결과 기록 템플릿

## 테스트 ID

예: DB-01

## 테스트 프롬프트

```text
여기에 입력한 프롬프트를 붙여넣기
```

## 기대 Workflow

```text
예: PM → DB → Review
```

## 실제 Workflow

```text
실제 Agent가 수행한 흐름 기록
```

## 결과 판정

```text
PASS / PARTIAL / FAIL
```

## 검증 체크리스트

```text
[ ] PM 라우팅이 정확했는가?
[ ] 필요한 Agent만 호출했는가?
[ ] RAG 참조가 적절했는가?
[ ] Handoff 정보가 누락되지 않았는가?
[ ] Review가 실제 검토를 수행했는가?
[ ] RAG Update Candidate가 필요한 경우 생성되었는가?
```

## 문제점

```text
발견된 문제 작성
```

## 수정 대상

```text
[ ] PM System Prompt
[ ] Agent Rules
[ ] RAG Mapping
[ ] Workflow
[ ] Review Prompt
[ ] Foundation RAG
[ ] Expert RAG 필요
```

## 수정 메모

```text
다음 튜닝 시 반영할 내용 작성
```
