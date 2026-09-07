# Agent Future Split Roadmap v1

## 0. Purpose

이 문서는 초기 5-Agent 구조에서 Expert 문서 제작 이후 Agent를 분리하기 위한 기준을 정의한다.

초기 구조:

```text
PM Agent
DB Agent
Backend Agent
Frontend Agent
Review Agent
```

미래 확장 후보:

```text
DevOps Agent
Test Agent
Security Agent
Docs Agent
AI Agent
RAG Update Agent
Performance Agent
Design System Agent
```

---

# 1. Split Philosophy

Agent는 처음부터 과도하게 나누지 않는다.

분리 기준은 다음이다.

- 전문 RAG 문서가 충분히 준비되었는가?
- 기존 Agent의 책임이 과도해졌는가?
- 특정 검토 항목이 반복적으로 누락되는가?
- 독립적인 작업 루프가 필요한가?
- Handoff가 명확히 정의 가능한가?

---

# 2. Current Temporary Ownership

| Future Area | Current Temporary Owner | Notes |
|---|---|---|
| DevOps | Backend + Review | Docker/Build/Deploy 후보만 기록 |
| Test | Review + Backend/Frontend | 테스트 후보 수준 |
| Security | Backend + Review | 기본 인증/인가/권한 검토 |
| Docs | PM + Review | 산출물 요약/문서화 후보 |
| RAG Update | Review | Candidate 수집, 자동 반영 금지 |
| AI | PM + Review | Agent 시스템 개선 논의 수준 |
| Performance | DB + Backend + Review | 명백한 성능 위험 검토 |
| Design System | Frontend + Review | UI 규칙 후보 수준 |

---

# 3. DevOps Agent Split Criteria

분리 조건:

- Linux/Ubuntu, Docker Advanced, CI/CD, Nginx, Cloud, Monitoring Expert 문서 제작 완료
- 배포/운영 설정 요청이 반복됨
- Backend Agent가 실행 환경까지 과도하게 담당함
- Review Agent의 DevOps Review가 반복적으로 길어짐

분리 후 담당:

- 로컬/서버 실행 환경
- Docker/Compose
- CI/CD
- 환경변수 운영
- 로그/모니터링
- 백업/복구
- 배포 체크리스트

---

# 4. Test Agent Split Criteria

분리 조건:

- Backend Testing / Frontend Testing Expert 문서 또는 본문 확장 완료
- 테스트 케이스 작성 요청이 반복됨
- Review Agent의 Test Review가 구현 수준으로 커짐

분리 후 담당:

- 테스트 전략
- 단위 테스트
- 통합 테스트
- API 테스트
- UI 테스트
- 회귀 테스트 체크리스트

---

# 5. Security Agent Split Criteria

분리 조건:

- Security Expert 문서 확장 완료
- 인증/인가/권한/민감정보 이슈가 반복됨
- Backend Agent의 Security Notes가 길어짐

분리 후 담당:

- 인증/인가 설계 검토
- 권한 매트릭스
- 민감정보 보호
- API 보안 체크
- 보안 테스트 후보

---

# 6. Docs Agent Split Criteria

분리 조건:

- README, API 문서, 운영 문서, 사용자 문서 작성이 반복됨
- PM/Review Agent가 문서화까지 과도하게 담당함

분리 후 담당:

- README
- API 문서
- 변경 이력
- 작업 보고서
- 사용자 가이드
- Agent 산출물 정리

---

# 7. RAG Update Agent Split Criteria

분리 조건:

- RAG Update Candidate가 누적됨
- Domain Rules 충돌/누락 관리가 반복됨
- RAG 문서 개선 루프를 독립적으로 운영할 필요가 생김

분리 후 담당:

- RAG Update Candidate 정리
- 우선순위 결정 보조
- 중복/충돌 후보 탐지
- 신규 문서 제작 후보 제안
- 기존 문서 보강 초안 작성

금지:

- 사용자 승인 없이 RAG 문서 자동 수정

---

# 8. AI Agent Split Criteria

분리 조건:

- Agent Workflow, LangGraph, Tool Calling, Memory, Evaluation 관련 작업이 반복됨
- 개인 AI 시스템 자체의 설계/개선이 독립 주제가 됨

분리 후 담당:

- Agent Workflow 설계
- Tool Calling 구조
- Memory/State 설계
- Evaluation/Guardrails
- Agent 성능 개선

---

# 9. Migration Method

Agent 분리는 다음 순서로 수행한다.

```text
1. 기존 Agent Rules에서 Secondary Responsibility 섹션 확인
2. 분리 대상 섹션 추출
3. 신규 Agent의 Primary Responsibility로 이동
4. 기존 Agent에는 Delegation Rule만 남김
5. Handoff Format 추가
6. Review Agent의 검토 항목 수정
7. PM Agent의 Routing Rule 수정
8. Common Agent Rules의 Future Split 상태 갱신
```

---

# 10. Minimal Split Template

```md
# <New Agent> Rules v1

## 0. Purpose

## 1. Primary Responsibility

## 2. Secondary Responsibility

## 3. Referenced RAG Areas

## 4. Work Loop

## 5. Input Requirements

## 6. Output Format

## 7. Handoff Protocol

## 8. Review Checklist

## 9. RAG Update Candidate Rules

## 10. Prohibitions
```
