# Agent System Prompts v1

개인 AI 개발팀 초기 5-Agent 구조용 System Prompt 패키지다.

## 포함 파일

```text
00_Common_System_Prompt.md
01_PM_Agent_System_Prompt.md
02_DB_Agent_System_Prompt.md
03_Backend_Agent_System_Prompt.md
04_Frontend_Agent_System_Prompt.md
05_Review_Agent_System_Prompt.md
99_System_Prompt_Usage_Guide.md
```

## 현재 Agent 구조

```text
PM / DB / Backend / Frontend / Review
```

## 제작 기준

- Master Rules
- Project Progress
- RAG Document Operation Rules Addendum
- Agent Build Context
- Agent Rules v1
- Foundation Domain Rules

## 설계 방향

- RAG First
- 추측 금지
- 사용자 승인 없는 RAG 자동 수정 금지
- 한국어 최종 응답
- Agent 간 책임 경계 명확화
- 순차 Workflow 중심
- 추후 Expert Agent 분리 용이성 확보

## 적용 방법

각 Agent에는 다음 조합을 System Prompt로 사용한다.

```text
Common System Prompt + 해당 Agent System Prompt
```

예:

```text
PM Agent = 00_Common_System_Prompt.md + 01_PM_Agent_System_Prompt.md
DB Agent = 00_Common_System_Prompt.md + 02_DB_Agent_System_Prompt.md
Backend Agent = 00_Common_System_Prompt.md + 03_Backend_Agent_System_Prompt.md
Frontend Agent = 00_Common_System_Prompt.md + 04_Frontend_Agent_System_Prompt.md
Review Agent = 00_Common_System_Prompt.md + 05_Review_Agent_System_Prompt.md
```
