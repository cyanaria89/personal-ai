# Agent Memory & State Management Part01 - State vs Memory Foundation

---

# 1. State vs Memory Foundation

## 1.1 Agent State와 Agent Memory 기본 구분

### [개념]

Agent State는 현재 Workflow가 진행되는 동안 필요한 작업 상태이다.

Agent Memory는 이전 대화, 프로젝트 정보, 사용자 선호, 확정 결정 등을 저장해 이후 작업에서 재사용하는 기억이다.

Agent State와 Agent Memory는 목적, 수명, 위험 요소가 다르다.

```text
State = 현재 작업 진행 상태
Memory = 과거 정보 재사용 저장소
```

기본 구조:

```text
User Request
→ Workflow State 생성
→ Agent 작업 수행
→ 필요한 경우 Memory Retrieval
→ State Update
→ Final Output
→ 필요한 경우 Memory Update
```

---

### [핵심]

- Agent State는 현재 실행 중인 작업의 상태이다.
- Agent Memory는 과거 정보를 재사용하기 위한 저장 정보이다.
- 모든 State가 Memory가 되는 것은 아니다.
- 모든 Memory가 현재 작업에 필요한 것은 아니다.
- 현재 사용자 요청은 기존 Memory보다 우선한다.
- 오래된 Memory는 검증 후 사용해야 한다.
- State와 Memory를 혼동하면 Agent Workflow가 불안정해진다.

---

### [실무]

2026 실무 기준 Multi-Agent System에서는 State와 Memory를 반드시 분리한다.

State는 PM Agent, Backend Agent, Frontend Agent, Review Agent가 같은 Workflow를 이어가기 위한 실행 정보이다.

Memory는 프로젝트 기술 스택, RAG 문서 규칙, 사용자 출력 선호, 과거 결정 사항처럼 반복 재사용 가능한 정보를 저장한다.

예시:

```text
현재 작업:
Agent Memory State Management Part01 문서 작성

State:
- currentTask: Part01 작성
- currentStep: draft_review_final
- constraints: MASTER_RAG_RULES 적용
- outputFormat: writing block

Memory:
- 프로젝트 목표: 개인 AI 개발팀 구축
- RAG 문서 규칙: FAQ 강화, Retrieval Queries 필수
- 사용자 선호: 한국어, RAG 최적화 Markdown
```

State는 작업이 끝나면 요약되거나 폐기될 수 있다.

Memory는 장기적으로 유용할 때만 저장한다.

---

### [FAQ]

Q. Agent State가 뭐야?
A. 현재 Workflow가 어느 단계에 있고 어떤 요구사항, 중간 결과, 오류, 다음 작업을 가지고 있는지 나타내는 현재 작업 상태다.

Q. Agent Memory가 뭐야?
A. 이전 대화, 프로젝트 정보, 사용자 선호, 확정 결정 등을 저장해 이후 작업에서 재사용하는 기억이다.

Q. Agent State와 Agent Memory 차이는?
A. State는 현재 작업 진행 상태이고, Memory는 과거 정보를 재사용하기 위한 저장 정보다.

Q. 모든 State를 Memory에 저장해야 해?
A. 아니다. 현재 작업에만 필요한 임시 상태는 장기 Memory로 저장하지 않는다.

Q. 모든 Memory를 현재 작업에 사용해야 해?
A. 아니다. 현재 요청과 관련 있는 Memory만 검색하고 검증 후 사용한다.

---

# 2. State Core Rules

## 2.1 Agent State 정의

### [개념]

Agent State는 현재 Agent Workflow 실행에 필요한 구조화된 작업 상태이다.

State는 Agent가 다음 작업을 안전하게 이어가기 위해 필요한 정보를 포함한다.

State는 현재 작업 기준이다.

대표 필드:

```json
{
  "currentTask": "string",
  "currentStep": "string",
  "status": "in_progress",
  "requirements": [],
  "constraints": [],
  "decisions": [],
  "assumptions": [],
  "agentOutputs": {},
  "toolResults": {},
  "reviewFindings": [],
  "errors": [],
  "nextAction": "string"
}
```

---

### [핵심]

- State는 현재 Workflow의 진행 정보를 저장한다.
- State는 Agent 간 작업 연속성을 유지한다.
- State는 요구사항, 제약, 결정 사항을 포함한다.
- State는 중간 결과와 검토 결과를 포함할 수 있다.
- State는 실패, 오류, 다음 작업을 명확히 한다.
- State는 너무 커지면 압축해야 한다.
- State는 최신 사용자 요청을 기준으로 갱신해야 한다.

---

### [실무]

Multi-Agent Workflow에서 State는 작업 인계 문서처럼 동작한다.

예시:

```text
PM Agent
→ Shared State 생성
→ Backend Agent 작업 결과 추가
→ Review Agent 검토 결과 추가
→ Fix Agent 수정 결과 반영
→ PM Agent 최종 출력
```

State 예시:

```json
{
  "status": "in_progress",
  "currentStep": "domain_document_review",
  "requirements": [
    "MASTER_RAG_RULES 적용",
    "DOMAIN_RULES 적용",
    "FAQ 포함",
    "Retrieval Queries 포함"
  ],
  "constraints": [
    "사람용 설명보다 Retrieval 최적화 우선",
    "Markdown 구조 유지",
    "용어 통일"
  ],
  "decisions": ["Part01은 State vs Memory Foundation으로 작성"],
  "reviewFindings": [],
  "errors": [],
  "nextAction": "final_output"
}
```

State는 현재 작업의 정확성을 높이는 데 사용한다.

State를 장기 Memory처럼 누적하면 Context Window가 낭비된다.

---

### [FAQ]

Q. Agent State에는 무엇을 넣어?
A. currentTask, currentStep, status, requirements, constraints, decisions, agentOutputs, reviewFindings, errors, nextAction을 넣는다.

Q. State는 왜 필요해?
A. Agent가 현재 작업 위치, 요구사항, 중간 결과, 다음 작업을 잃지 않도록 하기 위해 필요하다.

Q. State가 없으면 어떤 문제가 생겨?
A. Agent가 이전 단계 결과를 잊거나, 검토 결과를 반영하지 못하거나, 같은 작업을 반복할 수 있다.

Q. State는 오래 보관해야 해?
A. 현재 Workflow 중심으로 유지하고, 장기적으로 필요한 결정만 Memory 후보로 분리한다.

Q. State가 너무 커지면 어떻게 해?
A. 완료된 단계는 요약하고, 결정 사항과 열린 이슈 중심으로 State Compression을 적용한다.

---

# 3. Memory Core Rules

## 3.1 Agent Memory 정의

### [개념]

Agent Memory는 장기 또는 단기적으로 재사용할 가치가 있는 정보를 저장하는 기억이다.

Memory는 현재 작업 자체가 아니라 이전 정보의 재사용을 담당한다.

Memory는 최신성, 관련성, 충돌 여부를 확인한 뒤 사용해야 한다.

Memory 유형:

```text
Short-term Memory
Long-term Memory
Project Memory
User Preference Memory
Decision Memory
Conversation Summary
```

---

### [핵심]

- Memory는 과거 정보를 재사용하기 위한 저장 정보이다.
- Memory는 현재 요청과 관련 있을 때만 검색한다.
- Memory는 최신성 검증이 필요하다.
- Memory는 현재 사용자 요청보다 우선하지 않는다.
- 장기적으로 유용한 정보만 Long-term Memory에 저장한다.
- 민감정보, API Key, Token, Password는 Memory에 저장하지 않는다.
- 충돌 Memory는 우선순위 기준으로 해결한다.

---

### [실무]

Memory는 개인 AI 프로젝트처럼 장기 진행되는 작업에서 중요하다.

Project Memory 예시:

```json
{
  "type": "project_memory",
  "key": "personal_ai_project_goal",
  "value": "단순 RAG 챗봇이 아닌 개인 AI 개발팀 Multi-Agent System 구축",
  "updatedAt": "2026-07-01"
}
```

User Preference Memory 예시:

```json
{
  "type": "user_preference",
  "key": "rag_document_output_style",
  "value": "Korean, Markdown, writing block, Retrieval optimized",
  "updatedAt": "2026-07-01"
}
```

Decision Memory 예시:

```json
{
  "type": "decision_memory",
  "key": "state_memory_separation",
  "value": "Agent State와 Agent Memory는 반드시 분리해서 설계한다.",
  "reason": "현재 작업 안정성과 장기 기억 재사용 기준이 다르기 때문",
  "status": "active"
}
```

Memory는 Agent 품질을 높이지만, 오래된 Memory를 검증 없이 사용하면 잘못된 답변을 만든다.

---

### [FAQ]

Q. Agent Memory에는 무엇을 저장해?
A. 프로젝트 목표, 기술 스택, 문서 규칙, 사용자 선호, 확정 결정처럼 반복 재사용할 가치가 있는 정보를 저장한다.

Q. Memory는 언제 검색해?
A. 현재 요청을 처리하는 데 이전 프로젝트 맥락, 사용자 선호, 과거 결정이 필요할 때 검색한다.

Q. Memory를 무조건 믿어도 돼?
A. 아니다. Memory는 오래되었을 수 있으므로 최신성, 관련성, 충돌 여부를 확인해야 한다.

Q. Memory에 저장하면 안 되는 것은?
A. API Key, 비밀번호, 토큰, 주민번호, 계좌번호, 민감한 개인정보는 저장하지 않는다.

Q. Memory가 현재 요청과 충돌하면?
A. 현재 사용자 요청을 우선하고, 명시적 정정과 최신 프로젝트 결정을 기준으로 해결한다.

---

# 4. State vs Memory Comparison

## 4.1 State와 Memory 비교 기준

### [개념]

State와 Memory는 Agent Context Management의 핵심 요소이다.

State는 현재 Workflow 진행에 사용된다.

Memory는 과거 정보 재사용에 사용된다.

둘은 함께 사용되지만 같은 개념이 아니다.

---

### [핵심]

| 구분     | Agent State                         | Agent Memory                             |
| -------- | ----------------------------------- | ---------------------------------------- |
| 목적     | 현재 작업 진행 상태 관리            | 과거 정보 재사용                         |
| 기준     | 현재 Workflow                       | 이전 대화, 프로젝트, 결정                |
| 수명     | 작업 단위                           | 단기 또는 장기                           |
| 예시     | currentStep, status, reviewFindings | project stack, user preference, decision |
| 위험     | 누락 시 Workflow 깨짐               | 오래되면 잘못된 답변 유발                |
| 업데이트 | 작업 중 자주 변경                   | 필요한 경우 신중히 저장                  |
| 우선순위 | 현재 작업에서 높음                  | 검증 후 사용                             |
| 압축     | 완료 단계 요약                      | 오래된 정보 갱신 또는 만료               |

---

### [실무]

실무 설계에서는 아래처럼 분리한다.

```text
Workflow State:
- 현재 요청
- 현재 단계
- 작업 제약
- 중간 결과
- 검토 결과
- 오류
- 다음 작업

Agent Memory:
- 프로젝트 목표
- 기술 스택
- RAG 문서 규칙
- 사용자 출력 선호
- 확정된 Architecture Decision
- 과거 문제 해결 기록
```

나쁜 설계:

```text
모든 대화 내용 → Long-term Memory 저장
모든 Memory → 매 요청마다 Prompt에 삽입
State와 Memory 구분 없음
```

좋은 설계:

```text
현재 작업 정보 → State
반복 재사용 가치 정보 → Memory
현재 요청 관련 정보만 → Retrieval
오래된 Memory → Validation
충돌 정보 → Priority Rule로 해결
```

---

### [FAQ]

Q. State와 Memory를 왜 분리해야 해?
A. State는 현재 작업 안정성, Memory는 과거 정보 재사용이 목적이라 수명과 위험이 다르기 때문이다.

Q. State를 Memory처럼 저장하면 문제야?
A. 완료된 임시 상태까지 장기 저장되면 오래된 정보가 현재 답변을 오염시킬 수 있다.

Q. Memory를 State처럼 사용하면 문제야?
A. 과거 정보를 현재 작업 상태처럼 믿으면 최신 요청과 충돌할 수 있다.

Q. 현재 요청과 Memory 중 무엇이 우선이야?
A. 현재 사용자 요청이 우선이다.

Q. 최신 프로젝트 결정과 오래된 Memory가 다르면?
A. 최신 프로젝트 결정을 우선하고 오래된 Memory는 갱신하거나 무시한다.

---

# 5. Current Request Priority

## 5.1 현재 요청 우선 원칙

### [개념]

Agent는 항상 현재 사용자 요청을 최우선으로 처리해야 한다.

Memory는 현재 요청을 보조하는 자료이다.

Memory가 현재 요청을 덮어쓰면 안 된다.

우선순위:

```text
Current User Request
→ Explicit User Correction
→ Latest Project Decision
→ Recent Conversation
→ Long-term Memory
```

---

### [핵심]

- 현재 요청은 모든 Memory보다 우선한다.
- 사용자의 명시적 정정은 기존 Memory를 덮어쓴다.
- 최신 프로젝트 결정은 오래된 결정 Memory보다 우선한다.
- 최근 대화는 오래된 Long-term Memory보다 우선한다.
- 불확실한 Memory는 단정하지 않는다.
- 충돌이 애매하면 사용자 확인 또는 보수적 사용이 필요하다.

---

### [실무]

예시 상황:

```text
Old Memory:
출력은 일반 Markdown으로 제공

Current Request:
반드시 writing block 형식으로 출력
```

처리:

```text
Current Request 우선
→ writing block 형식 적용
→ 출력 형식 관련 Memory 갱신 후보
```

예시 상황:

```text
Old Memory:
Agent Memory & State Management는 Planned 상태

New Information:
Agent Memory State Management Part01 작업 시작
```

처리:

```text
Project Progress 기준 확인
→ Part01 작성 진행
→ 완료 후 Completed 또는 In Progress 반영 후보
```

현재 요청 우선 원칙은 Multi-Agent System에서 잘못된 자동화를 방지한다.

---

### [FAQ]

Q. 현재 요청 우선 원칙이 뭐야?
A. 과거 Memory보다 지금 사용자가 명시한 요구사항을 우선 처리하는 원칙이다.

Q. 사용자가 이전과 다르게 말하면 어떻게 해?
A. 현재 발언을 우선하고, 기존 Memory는 갱신 후보로 본다.

Q. 오래된 프로젝트 정보는 어떻게 처리해?
A. 최신 진행 상황과 충돌하는지 확인하고, 필요하면 업데이트하거나 무시한다.

Q. Memory가 확실하지 않으면?
A. 단정하지 않고 가정으로 표시하거나 현재 Context만 사용한다.

Q. Agent가 Memory를 과신하면 어떤 문제가 생겨?
A. 현재 요청과 다른 형식, 오래된 구조, 잘못된 프로젝트 상태를 기준으로 답변할 수 있다.

---

# 6. Memory Retrieval Foundation

## 6.1 필요한 Memory만 검색하는 기준

### [개념]

Memory Retrieval은 현재 요청에 필요한 Memory만 검색하고 사용하는 과정이다.

모든 Memory를 불러오는 방식은 Context 오염과 Token 낭비를 만든다.

기본 Flow:

```text
User Request
→ Identify Missing Context
→ Search Relevant Memory
→ Filter by Type
→ Check Recency
→ Check Conflict
→ Use in Response
```

---

### [핵심]

- 현재 요청에 필요한 Memory만 검색한다.
- Memory Type을 구분해 검색한다.
- 관련성 낮은 Memory는 사용하지 않는다.
- 오래된 Memory는 최신성 확인 후 사용한다.
- 충돌 Memory는 우선순위 규칙으로 해결한다.
- Memory Source와 Confidence를 고려한다.

---

### [실무]

Memory Retrieval 대상 예시:

```text
요청:
Agent Memory State Management Part01 작성

검색 대상:
- MASTER_RAG_RULES
- Agent Memory State Management Domain Rules
- Project Progress
- 사용자 출력 형식 선호
```

검색하지 않아도 되는 Memory:

```text
- 이전 웹 프로젝트 구현 세부사항
- 빅데이터 시험 풀이 기록
- 현재 문서와 무관한 하드웨어 설정
- 일회성 대화 내용
```

좋은 Retrieval Query 예시:

```text
Agent State와 Agent Memory 차이
State vs Memory Foundation
Memory Retrieval 기준
현재 요청과 Memory 충돌 처리
Multi-Agent State 기본 구조
```

---

### [FAQ]

Q. Memory Retrieval은 뭐야?
A. 현재 요청을 처리하는 데 필요한 과거 정보만 검색해 사용하는 과정이다.

Q. 모든 Memory를 검색하면 안 돼?
A. 관련 없는 정보가 답변에 섞이고 Context Window를 낭비하므로 좋지 않다.

Q. Memory Retrieval 기준은?
A. 현재 요청 관련성, Memory Type, 최신성, 충돌 여부, 신뢰도를 기준으로 한다.

Q. 검색된 Memory가 많으면?
A. 현재 작업과 직접 관련 있는 정보만 남기고 나머지는 무시한다.

Q. Retrieval Query는 어떻게 작성해?
A. 사용자가 실제로 물어볼 표현과 핵심 용어를 포함해 짧고 명확하게 작성한다.

---

# 7. Memory Update Foundation

## 7.1 장기 저장 후보 판단

### [개념]

Memory Update는 새 정보를 장기적으로 저장할지 판단하는 과정이다.

모든 새 정보가 Memory가 되는 것은 아니다.

장기적으로 반복 재사용할 가치가 있는 정보만 Memory Update 후보가 된다.

기본 Flow:

```text
New Information
→ Check Long-term Usefulness
→ Check Sensitivity
→ Check User Intent
→ Check Conflict
→ Save / Ignore / Update
```

---

### [핵심]

저장 후보:

- 장기 프로젝트 목표
- 기술 스택
- 폴더 구조
- RAG 문서 규칙
- Agent 구조
- 반복 선호
- 확정 결정
- 진행 상태 변화

저장 비추천:

- 일회성 감정
- 임시 농담
- 단기 일정
- 불확실한 추정
- 민감정보
- 사용자가 저장 원치 않는 정보

---

### [실무]

저장 후보 예시:

```text
이 채팅은 RAG 문서 제작/검수 전용
반드시 writing block 형식 유지
MASTER_RAG_RULES 적용
DOMAIN_RULES 적용
FAQ 강화
Retrieval 최적화 우선
```

저장하지 않는 예시:

```text
오늘은 피곤하다
농담성 표현
작업 중 임시 생각
확정되지 않은 아이디어
```

Memory Update는 문서 품질과 Agent 일관성을 높인다.

하지만 과도한 저장은 Memory 품질을 떨어뜨린다.

---

### [FAQ]

Q. Memory Update는 언제 해?
A. 장기적으로 재사용할 프로젝트 규칙, 사용자 선호, 확정 결정, 기술 스택이 새로 생겼을 때 한다.

Q. 모든 정보를 저장하면 안 돼?
A. 불필요한 정보가 많아지면 Retrieval 품질이 떨어지고 잘못된 답변이 나올 수 있다.

Q. 사용자 출력 선호는 저장해도 돼?
A. 반복적으로 사용할 가능성이 높으면 저장 가치가 있다.

Q. 민감정보는 저장해도 돼?
A. API Key, 비밀번호, 토큰, 민감한 개인정보는 저장하지 않는다.

Q. 임시 아이디어는 저장해?
A. 확정 결정이 아니면 저장하지 않거나 draft 상태로 구분한다.

---

# 8. Common Mistakes

## 8.1 State와 Memory 혼동

### [개념]

State와 Memory를 혼동하면 Agent가 현재 작업과 과거 정보를 구분하지 못한다.

이 문제는 Multi-Agent Workflow에서 특히 치명적이다.

---

### [핵심]

자주 발생하는 실수:

- 현재 작업 상태를 Long-term Memory에 모두 저장
- 오래된 Memory를 현재 사실처럼 사용
- 모든 Memory를 매 요청마다 Prompt에 삽입
- State 없이 Agent 간 작업 인계
- Decision Memory 없이 같은 결정을 반복 논의
- Memory Conflict 처리 기준 없음
- 현재 요청보다 오래된 Memory를 우선
- 민감정보를 Memory에 저장

---

### [실무]

문제:

```text
Agent가 오래된 출력 형식을 기준으로 문서를 작성함
```

원인:

```text
현재 요청 우선 원칙 미적용
Memory 최신성 확인 누락
```

해결:

```text
Current User Request 우선
→ Output Format State에 반영
→ 기존 출력 선호 Memory 갱신 후보 처리
```

문제:

```text
Agent가 이전 프로젝트 구조를 현재 프로젝트에 섞음
```

원인:

```text
Memory Retrieval Filter 부족
Project Scope 구분 없음
```

해결:

```text
Project Memory Type 분리
→ 현재 프로젝트 관련 Memory만 검색
→ 무관한 Memory 무시
```

---

### [FAQ]

Q. State와 Memory 혼동의 대표 문제는?
A. Agent가 현재 작업 상태와 과거 정보를 구분하지 못해 오래된 기준으로 답변하는 것이다.

Q. 모든 대화 내용을 Memory에 저장하면 좋아?
A. 아니다. 검색 품질이 떨어지고 오래된 정보가 현재 답변을 오염시킬 수 있다.

Q. State 없이 Multi-Agent를 운영하면?
A. Agent 간 요구사항, 중간 결과, 검토 결과가 누락되어 Workflow가 깨질 수 있다.

Q. Memory Conflict 기준이 없으면?
A. Agent가 서로 충돌하는 기억을 임의로 섞어 잘못된 결론을 낼 수 있다.

Q. 해결 핵심은?
A. State와 Memory를 분리하고, 현재 요청 우선, 최신성 검증, 충돌 처리 기준을 적용하는 것이다.

---

# 9. Best Practice

## 9.1 State와 Memory 설계 원칙

### [개념]

좋은 Agent Context Management는 State와 Memory를 분리하고 필요한 순간에만 연결한다.

State는 현재 작업 안정성을 담당한다.

Memory는 장기 프로젝트 일관성을 담당한다.

---

### [핵심]

Best Practice:

- State와 Memory를 명확히 구분한다.
- 현재 사용자 요청을 Memory보다 우선한다.
- State에는 현재 작업 정보만 유지한다.
- Long-term Memory에는 반복 재사용 가치가 있는 정보만 저장한다.
- Memory Retrieval은 현재 요청 관련 정보만 수행한다.
- Memory 사용 전 Recency Check를 수행한다.
- Memory Conflict는 우선순위 규칙으로 해결한다.
- Decision Memory에는 이유와 날짜를 함께 기록한다.
- 민감정보와 Secret은 Memory에 저장하지 않는다.
- State가 길어지면 Compression을 적용한다.

---

### [실무]

추천 구조:

```text
Current Request
├ Workflow State
│ ├ currentTask
│ ├ currentStep
│ ├ requirements
│ ├ constraints
│ ├ decisions
│ ├ reviewFindings
│ └ nextAction
│
└ Memory Retrieval
  ├ Project Memory
  ├ User Preference Memory
  ├ Decision Memory
  └ Domain Rules
```

추천 우선순위:

```text
1. 현재 사용자 요청 반영
2. Master Rules 적용
3. Domain Rules 적용
4. Project Progress 참고
5. Retrieval Queries 강화
6. Final Quality Review
```

---

### [FAQ]

Q. 좋은 State 설계 기준은?
A. 현재 작업을 이어가는 데 필요한 요구사항, 제약, 단계, 중간 결과, 오류, 다음 작업을 명확히 담는 것이다.

Q. 좋은 Memory 설계 기준은?
A. 장기적으로 반복 재사용할 가치가 있는 프로젝트 정보, 사용자 선호, 확정 결정을 저장하는 것이다.

Q. State와 Memory는 언제 연결돼?
A. 현재 작업에 과거 정보가 필요할 때 Memory Retrieval을 통해 State 보조 자료로 사용한다.

Q. Memory를 사용한 뒤 State에 저장해?
A. 필요한 결과만 요약해 State에 반영하고, 검색 결과 전체를 저장하지 않는다.

Q. 가장 중요한 원칙은?
A. 현재 요청 우선, State와 Memory 분리, 필요한 Memory만 검증 후 사용하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Agent State가 뭐야?
A. 현재 Workflow의 단계, 요구사항, 중간 결과, 오류, 다음 작업을 나타내는 현재 작업 상태다.

Q. Agent Memory가 뭐야?
A. 이전 대화, 프로젝트 정보, 사용자 선호, 확정 결정 등을 저장해 이후 작업에서 재사용하는 기억이다.

Q. Agent State와 Agent Memory 차이는?
A. State는 현재 작업 진행 상태이고, Memory는 과거 정보를 재사용하기 위한 저장 정보다.

Q. State와 Memory를 왜 분리해야 해?
A. State는 현재 작업 안정성, Memory는 장기 정보 재사용이 목적이라 수명과 위험이 다르기 때문이다.

Q. 모든 State를 Long-term Memory에 저장해야 해?
A. 아니다. 현재 작업에만 필요한 임시 상태는 장기 Memory로 저장하지 않는다.

Q. 모든 Memory를 현재 작업에 넣어야 해?
A. 아니다. 현재 요청과 관련 있는 Memory만 검색하고 검증 후 사용한다.

Q. 현재 요청과 Memory가 충돌하면?
A. 현재 사용자 요청을 우선하고 오래된 Memory는 갱신하거나 무시한다.

Q. Agent State에는 어떤 필드가 필요해?
A. currentTask, currentStep, status, requirements, constraints, decisions, agentOutputs, reviewFindings, errors, nextAction이 필요하다.

Q. Agent Memory에는 어떤 정보를 저장해?
A. 프로젝트 목표, 기술 스택, 문서 규칙, 사용자 선호, 확정 결정처럼 반복 재사용할 가치가 있는 정보를 저장한다.

Q. Memory Retrieval은 뭐야?
A. 현재 요청에 필요한 과거 정보만 검색하고 최신성, 관련성, 충돌 여부를 확인해 사용하는 과정이다.

Q. Memory Update는 언제 해?
A. 장기적으로 유용한 프로젝트 규칙, 기술 스택, 사용자 선호, 확정 결정이 새로 생겼을 때 한다.

Q. 오래된 Memory는 어떻게 처리해?
A. Recency Check를 수행하고 현재 요청이나 최신 결정과 충돌하면 업데이트하거나 무시한다.

Q. Memory Conflict 우선순위는?
A. Current User Request, Explicit User Correction, Latest Project Decision, Recent Conversation, Long-term Memory 순서다.

Q. State가 너무 커지면 어떻게 해?
A. 완료된 단계는 요약하고 결정 사항, 열린 이슈, 오류 중심으로 State Compression을 적용한다.

Q. Multi-Agent System에서 State는 왜 중요해?
A. 여러 Agent가 같은 요구사항, 제약, 중간 결과를 기준으로 작업하게 만들어 Workflow 일관성을 유지하기 때문이다.

Q. Project Memory에는 뭘 저장해?
A. 프로젝트 목표, 기술 스택, 폴더 구조, Agent 구조, RAG 문서 규칙, 진행 상황, 확정 결정을 저장한다.

Q. User Preference Memory에는 뭘 저장해?
A. 답변 언어, 톤, 문서 형식, 출력 방식처럼 향후 답변 품질을 높이는 정보를 저장한다.

Q. Decision Memory는 왜 필요해?
A. 프로젝트에서 이미 확정한 방향을 유지하고 같은 논의를 반복하지 않기 위해 필요하다.

Q. Working Memory와 State는 같아?
A. 아니다. Working Memory는 현재 작업 중 임시 정보이고, State는 Workflow 진행 상태를 구조화해 관리하는 정보다.

Q. 민감정보를 Memory에 저장해도 돼?
A. API Key, 비밀번호, 토큰, 민감한 개인정보는 저장하지 않는 것이 원칙이다.
