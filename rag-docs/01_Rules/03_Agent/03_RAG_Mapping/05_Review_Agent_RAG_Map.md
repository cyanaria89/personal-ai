# 05. Review Agent RAG Map

## 1. 목적

Review Agent는 전체 산출물의 누락, 충돌, 규칙 위반, 품질 문제, Agent 간 전달 오류를 검토한다.

초기 구조에서는 Test / Security / DevOps / Docs / RAG Update 후보 검토를 일부 포함하지만, 추후 Expert 문서 제작 후 별도 Agent로 분리할 수 있어야 한다.

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
Agent_Rules_v1/05_Review_Agent_Rules.md
Agent_Rules_v1/99_Agent_Future_Split_Roadmap.md
Agent_System_Prompts_v1/00_Common_System_Prompt.md
Agent_System_Prompts_v1/05_Review_Agent_System_Prompt.md
Agent_System_Prompts_v1/99_System_Prompt_Usage_Guide.md
```

## 4. Primary Domain Rules

Review Agent는 검토 범위가 넓으므로 핵심 Backend/Frontend/AI 운영 문서를 함께 참조한다.

```text
01_Backend/01_SQL_Domain_Rules.md
01_Backend/02_Java_Domain_Rules.md
01_Backend/03_Spring_Boot_Domain_Rules.md
01_Backend/04_JPA_Advanced_Domain_Rules.md
01_Backend/05_Security_Advanced_Domain_Rules.md
01_Backend/07_Testing_Domain_Rules.md
01_Backend/12_API_Design_Domain_Rules.md
01_Backend/13_Design_Pattern_Domain_Rules.md
03_Frontend/04_React_Core_Domain_Rules.md
03_Frontend/08_Data_Fetching_REST_API_Integration_Domain_Rules.md
03_Frontend/10_Authentication_Frontend_Flow_Domain_Rules.md
03_Frontend/11_Error_Handling_Loading_UX_Domain_Rules.md
03_Frontend/13_Frontend_Testing_Domain_Rules.md
03_Frontend/16_Frontend_Code_Review_Domain_Rules.md
02_AI/12_Agent_Evaluation_Guardrails_Domain_Rules.md
```

## 5. Secondary Domain Rules

```text
01_Backend/06_QueryDSL_Practical_Domain_Rules.md
01_Backend/08_Redis_Domain_Rules.md
01_Backend/10_Git_GitHub_Domain_Rules.md
01_Backend/11_Docker_Domain_Rules.md
03_Frontend/05_React_Component_Design_Domain_Rules.md
03_Frontend/06_React_Router_Domain_Rules.md
03_Frontend/07_State_Management_Domain_Rules.md
03_Frontend/09_Form_Handling_Validation_Domain_Rules.md
03_Frontend/14_Frontend_Accessibility_Domain_Rules.md
03_Frontend/15_Frontend_Build_Deploy_Domain_Rules.md
03_Frontend/18_Design_System_Foundation_Domain_Rules.md
02_AI/06_RAG_Evaluation_Retrieval_Optimization_Domain_Rules.md
02_AI/09_Agent_Workflow_Design_Domain_Rules.md
02_AI/10_Multi_Agent_System_Domain_Rules.md
```

## 6. 검토 유형별 참조

| 검토 유형 | 우선 참조 |
|---|---|
| DB 설계 검토 | SQL + JPA |
| Backend 코드 검토 | Java + Spring Boot + JPA + API Design |
| Security 검토 | Security Advanced |
| Test 검토 | Backend Testing + Frontend Testing |
| Frontend 검토 | React + REST API Integration + Code Review |
| API Contract 검토 | API Design + Frontend REST API Integration |
| Agent 결과물 검토 | Agent Evaluation Guardrails + Common Rules |
| RAG 부족/충돌 검토 | RAG Evaluation + Master Rules |
| 배포/운영 기초 검토 | Docker + Build Deploy |

## 7. Review Agent Output Format

```text
[Review Summary]
- Overall Status: PASS / NEEDS_FIX / BLOCKED
- Scope Reviewed:
- Major Issues:
- Minor Issues:
- RAG Issues:

[Issue List]
1. Severity: Critical / Major / Minor
   - Location:
   - Problem:
   - Reason:
   - Suggested Fix:

[Cross-Agent Consistency]
- DB ↔ Backend:
- Backend ↔ Frontend:
- Security:
- Testing:
- Documentation:

[Final Recommendation]
- Proceed / Fix Required / Need User Decision

[RAG Update Candidate]
- 발견된 문서 부족/충돌/보강 후보
```

## 8. Future Split Support

| 분리 후보 | 현재 Review 내 역할 | 분리 기준 |
|---|---|---|
| Test Agent | 테스트 관점 검토 | 테스트 코드/전략이 반복적으로 복잡해질 때 |
| Security Agent | 보안 관점 검토 | 인증/인가/취약점 검토가 많아질 때 |
| DevOps Agent | Docker/Build Deploy 기초 검토 | CI/CD, 운영, 배포 Expert 문서 제작 후 |
| Docs Agent | 문서화 검토 | 산출물 문서 작성/관리 요구가 많아질 때 |
| RAG Update Agent | RAG Update Candidate 정리 | RAG 보강 루프를 별도 운영할 때 |
| Performance Agent | 성능/쿼리/렌더링 검토 | 성능 Expert 문서 제작 후 |

