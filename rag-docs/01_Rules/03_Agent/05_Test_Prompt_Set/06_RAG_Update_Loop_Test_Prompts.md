# 06. RAG Update Loop 테스트 프롬프트

## RAG-01. 문서 부족 감지 테스트

### 테스트 프롬프트

```text
Kafka 기반 이벤트 처리 구조를 Agent Workflow에 추가하려고 해.
현재 Foundation RAG 기준으로 설계 가능 범위와 부족한 문서를 구분해서 알려줘.
```

### 기대 Workflow

```text
PM → Review 또는 PM → RAG Update Candidate 생성
```

### 기대 동작

- 현재 Foundation에 Kafka Expert 문서가 없다면 부족하다고 판단해야 함
- 추측으로 상세 Kafka 설계를 만들지 않아야 함
- RAG Update Candidate를 생성해야 함

### 검증 체크리스트

```text
[ ] 문서 부족을 인정했는가?
[ ] 가능한 범위와 불가능한 범위를 구분했는가?
[ ] Kafka Expert RAG 제작 후보를 제안했는가?
[ ] 자동 반영하지 않고 사용자 승인 필요를 명시했는가?
```

---

## RAG-02. 규칙 충돌 감지 테스트

### 테스트 프롬프트

```text
A 문서에서는 Controller에서 Entity를 직접 반환해도 된다고 하고,
B 문서에서는 반드시 Response DTO를 사용하라고 되어 있어.
이런 충돌이 있으면 Agent는 어떻게 처리해야 해?
```

### 기대 Workflow

```text
PM → Review → RAG Update Candidate
```

### 기대 동작

- 충돌을 무시하지 않아야 함
- 상위 규칙 우선순위 또는 Master Rules 기준으로 판단해야 함
- 충돌 내용을 RAG Update Candidate로 남겨야 함

### 검증 체크리스트

```text
[ ] 규칙 충돌로 인식했는가?
[ ] 임의로 한쪽을 선택하지 않았는가?
[ ] Master Rules 또는 우선순위 기준을 적용했는가?
[ ] 수정 후보를 작성했는가?
```
