# 91. RAG Update Candidate Map

## 1. 목적

이 문서는 Agent 작업 중 발견되는 RAG 문서 보강 후보를 어떤 방식으로 기록하고, 어떤 문서로 연결할지 정의한다.

RAG 문서는 자동 수정하지 않는다. 반드시 사용자 승인 후 반영한다.

## 2. RAG Update Candidate 생성 조건

다음 상황에서 Candidate를 생성한다.

```text
- 필요한 규칙이 RAG 문서에 없음
- Domain Rules 간 내용이 충돌함
- Master Rules와 Domain Rules가 충돌함
- 현재 프로젝트 진행 상태와 문서 내용이 맞지 않음
- 반복적으로 같은 질문/판단이 발생함
- Agent가 추측으로 보완해야 하는 부분이 생김
- Expert 문서로 분리할 만큼 내용이 커짐
```

## 3. Candidate 기본 형식

```text
[RAG Update Candidate]
- Candidate ID:
- 발견 Agent:
- 발견 위치:
- 관련 요청:
- 부족/충돌 내용:
- 필요한 이유:
- 영향 범위:
- 추천 보강 문서:
- 신규 문서 필요 여부: Yes / No
- 우선순위: High / Medium / Low
- 사용자 승인 필요: Yes
```

## 4. Agent별 Candidate 담당 범위

| Agent | Candidate 범위 |
|---|---|
| PM Agent | Agent Routing, Workflow, 역할 경계, 진행 상태 |
| DB Agent | SQL, DB 설계, 관계, 인덱스, 데이터 모델링 |
| Backend Agent | Java, Spring, JPA, Security, API, Testing, Redis |
| Frontend Agent | React, Router, State, API Integration, UX, Testing |
| Review Agent | 전체 충돌, 누락, 품질, RAG 보강 후보 통합 |

## 5. 추천 보강 문서 매핑

| 발견 내용 | 추천 보강 문서 |
|---|---|
| DB 정규화/관계 규칙 부족 | 01_Backend/01_SQL_Domain_Rules.md |
| Entity 매핑 규칙 부족 | 01_Backend/04_JPA_Advanced_Domain_Rules.md |
| API 응답 형식 기준 부족 | 01_Backend/12_API_Design_Domain_Rules.md |
| 인증/인가 규칙 부족 | 01_Backend/05_Security_Advanced_Domain_Rules.md |
| 테스트 기준 부족 | 01_Backend/07_Testing_Domain_Rules.md 또는 03_Frontend/13_Frontend_Testing_Domain_Rules.md |
| React 컴포넌트 기준 부족 | 03_Frontend/05_React_Component_Design_Domain_Rules.md |
| 상태 관리 기준 부족 | 03_Frontend/07_State_Management_Domain_Rules.md |
| API 연동 규칙 부족 | 03_Frontend/08_Data_Fetching_REST_API_Integration_Domain_Rules.md |
| UX 처리 기준 부족 | 03_Frontend/11_Error_Handling_Loading_UX_Domain_Rules.md |
| Agent Workflow 기준 부족 | 02_AI/09_Agent_Workflow_Design_Domain_Rules.md |
| Multi-Agent 책임 경계 부족 | 02_AI/10_Multi_Agent_System_Domain_Rules.md |
| RAG 검색/평가 기준 부족 | 02_AI/06_RAG_Evaluation_Retrieval_Optimization_Domain_Rules.md |
| Guardrails 부족 | 02_AI/12_Agent_Evaluation_Guardrails_Domain_Rules.md |

## 6. Expert 문서 분리 후보 기준

다음 조건 중 하나 이상을 만족하면 Expert 문서 또는 독립 Agent 분리 후보로 표시한다.

```text
- 동일 주제 Candidate가 3회 이상 반복됨
- Foundation 문서에 넣기에는 내용이 너무 깊음
- 독립 Agent가 담당해야 할 만큼 책임이 커짐
- 운영/보안/성능/테스트처럼 독립 검토가 필요한 영역임
- 기존 Agent의 Out of Scope에 해당함
```

## 7. 우선순위 기준

| 우선순위 | 기준 |
|---|---|
| High | 작업 진행을 막거나 잘못된 산출물을 만들 위험이 큼 |
| Medium | 품질 저하 가능성이 있지만 우회 가능함 |
| Low | 개선하면 좋지만 현재 작업에 직접 영향은 작음 |

## 8. 반영 흐름

```text
Agent 작업
↓
RAG Update Candidate 생성
↓
Review Agent가 후보 통합
↓
사용자에게 승인 요청
↓
승인된 항목만 RAG 문서 수정
↓
Project Progress 갱신
↓
Agent-RAG Mapping 필요 시 수정
```

