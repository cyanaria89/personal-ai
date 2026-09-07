# Agent Rules v1 Package

## 구성

```text
Agent_Rules_v1
├ 00_Common_Agent_Rules.md
├ 01_PM_Agent_Rules.md
├ 02_DB_Agent_Rules.md
├ 03_Backend_Agent_Rules.md
├ 04_Frontend_Agent_Rules.md
├ 05_Review_Agent_Rules.md
└ 99_Agent_Future_Split_Roadmap.md
```

## 제작 기준

참조 입력:

- 01_Master.zip
  - Agent System Prompt 제작 요청.txt
  - Agent_Build_Context.md
  - Master_RAG_Rules.md
  - Project_Progress.md
  - RAG_Document_Operation_Rules_Addendum.md
- 01_Foundation.zip
  - Backend Foundation Domain Rules
  - AI Foundation Domain Rules
  - Frontend Foundation Domain Rules

## 현재 Agent 구조

```text
PM / DB / Backend / Frontend / Review
```

## 설계 방향

- 초기에는 5개 Agent로 단순하게 시작한다.
- Test, Security, DevOps, Docs, RAG Update 역할은 현재 각 Agent의 Secondary Responsibility 또는 Review Agent 내부 섹션으로 둔다.
- 추후 Expert 문서 제작 후 섹션 단위로 쉽게 분리할 수 있도록 `Future Split`, `Delegation`, `Out of Scope` 항목을 포함했다.

## 사용 방법

1. `00_Common_Agent_Rules.md`를 모든 Agent 공통 규칙으로 둔다.
2. 각 Agent에는 해당 Agent Rules를 System Prompt 또는 운영 규칙으로 반영한다.
3. PM Agent가 작업 라우팅을 담당한다.
4. Review Agent가 초기 품질 게이트와 RAG Update Candidate 수집을 담당한다.
5. Expert RAG 문서가 준비되면 `99_Agent_Future_Split_Roadmap.md` 기준으로 Agent를 분리한다.
