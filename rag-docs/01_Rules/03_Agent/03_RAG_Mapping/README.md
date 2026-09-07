# Agent-RAG Mapping v1

이 문서는 개인 AI 프로젝트의 초기 5개 Agent 구조에서 각 Agent가 어떤 RAG 문서를 우선 참조해야 하는지 정의한다.

## 적용 대상

- PM Agent
- DB Agent
- Backend Agent
- Frontend Agent
- Review Agent

## 기본 원칙

1. 모든 Agent는 Master 문서를 공통으로 참조한다.
2. 각 Agent는 자신의 Primary Domain Rules를 우선 참조한다.
3. 관련성이 낮은 문서를 무리하게 참조하지 않는다.
4. 문서가 부족하거나 충돌하면 RAG Update Candidate로 기록한다.
5. 추후 Expert 문서가 추가되면 이 Mapping 문서에서 참조 우선순위를 수정한다.

## 파일 구성

```text
Agent_RAG_Mapping_v1
├ 00_Global_RAG_Loading_Policy.md
├ 01_PM_Agent_RAG_Map.md
├ 02_DB_Agent_RAG_Map.md
├ 03_Backend_Agent_RAG_Map.md
├ 04_Frontend_Agent_RAG_Map.md
├ 05_Review_Agent_RAG_Map.md
├ 90_Request_Type_Routing_Map.md
├ 91_RAG_Update_Candidate_Map.md
├ 99_Expert_RAG_Extension_Map.md
└ README.md
```

## 사용 방식

Agent를 설정할 때 다음 조합을 기본으로 사용한다.

```text
Common System Prompt
+ Agent-specific System Prompt
+ Agent Rules
+ Agent RAG Map
+ 필요한 Domain Rules
```

