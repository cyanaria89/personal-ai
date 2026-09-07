# 99. 테스트 커버리지 맵

## 테스트 범위 요약

| 영역 | 테스트 ID | 목적 |
|---|---|---|
| DB 전용 | DB-01 | DB Agent 라우팅 및 설계 검증 |
| DB 전용 | DB-02 | 기존 테이블 관계 검토 |
| Backend 전용 | BE-01 | DB 생략 후 Backend 설계 검증 |
| Backend 전용 | BE-02 | Service 계층 분리 검증 |
| Frontend 전용 | FE-01 | 기존 API 기준 화면 설계 검증 |
| Frontend 전용 | FE-02 | Frontend validation 검증 |
| 전체 Workflow | FULL-01 | DB → Backend → Frontend 순차 흐름 검증 |
| 전체 Workflow | FULL-02 | 기존 기능 확장 흐름 검증 |
| Review 전용 | RV-01 | 설계 문제 검토 능력 검증 |
| Review 전용 | RV-02 | 산출물 간 일치성 검토 |
| RAG Update | RAG-01 | 문서 부족 감지 검증 |
| RAG Update | RAG-02 | 규칙 충돌 감지 검증 |
| Future Split | SPLIT-01 | DevOps Agent 분리 후보 검증 |
| Future Split | SPLIT-02 | Test Agent 분리 후보 검증 |
| Future Split | SPLIT-03 | Security Agent 분리 후보 검증 |

## 1차 최소 테스트 세트

```text
DB-01
BE-01
FE-01
FULL-01
RAG-01
```

## 전체 안정화 테스트 세트

```text
DB-01, DB-02
BE-01, BE-02
FE-01, FE-02
FULL-01, FULL-02
RV-01, RV-02
RAG-01, RAG-02
SPLIT-01, SPLIT-02, SPLIT-03
```
