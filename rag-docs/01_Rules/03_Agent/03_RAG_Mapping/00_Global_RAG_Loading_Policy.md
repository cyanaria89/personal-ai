# 00. Global RAG Loading Policy

## 1. 목적

이 문서는 모든 Agent가 RAG 문서를 참조할 때 따르는 공통 로딩 정책을 정의한다.

## 2. 공통 필수 참조 문서

모든 Agent는 아래 Master 계열 문서를 공통 기준으로 삼는다.

```text
01_Master/Agent_Build_Context.md
01_Master/Master_RAG_Rules.md
01_Master/Project_Progress.md
01_Master/RAG_Document_Operation_Rules_Addendum.md
```

### 역할

| 문서 | 역할 |
|---|---|
| Agent_Build_Context.md | Agent 구조, 운영 목적, 기본 방향 |
| Master_RAG_Rules.md | 전체 RAG 운영 원칙 |
| Project_Progress.md | 현재 RAG 제작/운영 진행 상태 |
| RAG_Document_Operation_Rules_Addendum.md | 문서 제작/수정/운영 보조 규칙 |

## 3. 공통 Agent Rules 참조

모든 Agent는 아래 문서를 공통 참조한다.

```text
Agent_Rules_v1/00_Common_Agent_Rules.md
Agent_System_Prompts_v1/00_Common_System_Prompt.md
```

## 4. 참조 우선순위

RAG 문서는 다음 순서로 우선 적용한다.

```text
1순위: Master Rules
2순위: Common Agent Rules / Common System Prompt
3순위: 해당 Agent Rules / 해당 Agent System Prompt
4순위: 해당 Agent Primary Domain Rules
5순위: Secondary Domain Rules
6순위: Reference-only Domain Rules
```

## 5. 충돌 처리 원칙

문서 간 내용이 충돌할 경우 다음 기준을 따른다.

```text
Master Rules > Agent Rules > Domain Rules > 일반 추론
```

단, 기술적으로 명백히 잘못된 내용이 Domain Rules에 있거나 오래된 경우에는 자동 수정하지 않고 `RAG Update Candidate`로 기록한다.

## 6. 문서 부족 처리

Agent가 작업 중 필요한 규칙이나 지식이 RAG에 없다고 판단하면 다음 형식으로 기록한다.

```text
[RAG Update Candidate]
- 발견 위치:
- 부족한 내용:
- 필요한 이유:
- 영향 범위:
- 추천 보강 문서:
- 우선순위: High / Medium / Low
```

## 7. 과도한 참조 금지

Agent는 작업과 직접 관련 없는 Domain Rules를 무리하게 참조하지 않는다.

예시:

```text
Frontend 화면 수정 요청
→ Frontend Rules 중심
→ DB Rules는 데이터 구조 변경이 있을 때만 참조
```

```text
DB 테이블 설계 요청
→ SQL Rules 중심
→ React Rules는 참조하지 않음
```

## 8. 초기 운영 기준

초기에는 모든 작업을 완전 병렬로 실행하지 않는다.

```text
기본값: 순차 실행
예외: PM Agent가 명확히 병렬 가능하다고 판단한 경우만 병렬 후보로 표시
```

