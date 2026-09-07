# 01. PM Agent RAG Map

## 1. 목적

PM Agent는 사용자 요청을 분석하고, 작업 범위를 분해하며, DB / Backend / Frontend / Review Agent의 호출 여부와 순서를 결정한다.

PM Agent는 세부 구현보다 전체 흐름, 역할 분배, 우선순위, 작업 전달 형식에 집중한다.

## 2. Required Master Documents

```text
01_Master/Agent_Build_Context.md
01_Master/Master_RAG_Rules.md
01_Master/Project_Progress.md
01_Master/RAG_Document_Operation_Rules_Addendum.md
```

## 3. Required Agent Documents

```text
Agent_Rules_v1/00_Common_Agent_Rules.md
Agent_Rules_v1/01_PM_Agent_Rules.md
Agent_System_Prompts_v1/00_Common_System_Prompt.md
Agent_System_Prompts_v1/01_PM_Agent_System_Prompt.md
```

## 4. Primary Domain Rules

PM Agent는 특정 기술 구현보다 전체 Agent 운영과 RAG 운영을 판단해야 하므로 AI/Agent 계열 문서를 우선 참조한다.

```text
02_AI/09_Agent_Workflow_Design_Domain_Rules.md
02_AI/10_Multi_Agent_System_Domain_Rules.md
02_AI/11_Agent_Memory_State_Management_Domain_Rules.md
02_AI/12_Agent_Evaluation_Guardrails_Domain_Rules.md
02_AI/02_Prompt_Engineering_Domain_Rules.md
```

## 5. Secondary Domain Rules

작업 범위를 판단할 때 필요한 수준으로만 참조한다.

```text
01_Backend/01_SQL_Domain_Rules.md
01_Backend/02_Java_Domain_Rules.md
01_Backend/03_Spring_Boot_Domain_Rules.md
01_Backend/04_JPA_Advanced_Domain_Rules.md
01_Backend/12_API_Design_Domain_Rules.md
03_Frontend/04_React_Core_Domain_Rules.md
03_Frontend/08_Data_Fetching_REST_API_Integration_Domain_Rules.md
```

## 6. Reference-only Domain Rules

아래 문서는 PM Agent가 직접 구현 판단을 할 때가 아니라 작업 범위 확인용으로만 참조한다.

```text
01_Backend/05_Security_Advanced_Domain_Rules.md
01_Backend/07_Testing_Domain_Rules.md
01_Backend/10_Git_GitHub_Domain_Rules.md
01_Backend/11_Docker_Domain_Rules.md
03_Frontend/13_Frontend_Testing_Domain_Rules.md
03_Frontend/15_Frontend_Build_Deploy_Domain_Rules.md
03_Frontend/16_Frontend_Code_Review_Domain_Rules.md
```

## 7. Routing 판단 기준

| 사용자 요청 유형 | 호출 순서 |
|---|---|
| 신규 기능 + 데이터 저장 필요 | PM → DB → Backend → Frontend → Review |
| DB 설계/ERD/SQL 요청 | PM → DB → Review |
| Backend 구현/수정 요청 | PM → Backend → Review |
| API 변경 + 화면 영향 있음 | PM → Backend → Frontend → Review |
| Frontend 화면/컴포넌트 요청 | PM → Frontend → Review |
| 전체 설계 검토 요청 | PM → DB → Backend → Frontend → Review |
| 코드 리뷰/품질 검토 요청 | PM → Review |
| RAG 문서 보강 요청 | PM → Review 또는 RAG Update Candidate 생성 |

## 8. PM Output Handoff Format

```text
[PM Analysis]
- User Request Summary:
- Goal:
- Required Agents:
- Execution Order:
- DB Impact: Yes / No / Unknown
- Backend Impact: Yes / No / Unknown
- Frontend Impact: Yes / No / Unknown
- Review Required: Yes

[Task Breakdown]
1.
2.
3.

[Handoff]
- To DB Agent:
- To Backend Agent:
- To Frontend Agent:
- To Review Agent:

[RAG Update Candidate]
- 필요한 경우에만 작성
```

## 9. Future Split Support

PM Agent에서 추후 분리될 수 있는 영역은 다음과 같다.

| 분리 후보 | 분리 기준 |
|---|---|
| RAG Update Agent | Update Candidate가 반복적으로 많아질 때 |
| Planning Agent | 작업 계획/일정/우선순위가 복잡해질 때 |
| Orchestration Agent | LangGraph 등 실제 라우팅 자동화가 필요할 때 |

