# Agent Memory & State Management Part02 - Memory Types

---

# 1. Memory Types Foundation

## 1.1 Agent Memory 유형 구분

### [개념]

Agent Memory는 이전 정보의 재사용 목적에 따라 여러 유형으로 나눈다.

Memory Type을 구분하면 Retrieval 정확도, Context 일관성, 장기 프로젝트 관리 품질이 높아진다.

기본 Memory Types:

```text
Short-term Memory
Long-term Memory
Working Memory
Project Memory
User Preference Memory
Decision Memory
Conversation Summary
```

Memory Type은 저장 기간, 사용 목적, 검증 기준이 다르다.

---

### [핵심]

- Short-term Memory는 현재 대화 흐름 유지에 사용한다.
- Long-term Memory는 장기적으로 재사용할 정보를 저장한다.
- Working Memory는 현재 작업 중 임시로 사용하는 정보이다.
- Project Memory는 특정 프로젝트의 지속 맥락을 저장한다.
- User Preference Memory는 사용자 응답 선호를 저장한다.
- Decision Memory는 프로젝트 확정 결정을 저장한다.
- Conversation Summary는 긴 대화를 압축해 Context를 유지한다.
- Memory Type을 구분하지 않으면 Retrieval 오염이 발생한다.

---

### [실무]

2026 실무 기준 Agent Memory는 하나의 저장소로만 설계하지 않는다.

Memory를 유형별로 나누고 Retrieval Query도 유형별로 분리한다.

예시:

```text
요청:
Agent Memory State Management Part02 작성

필요 Memory:
- Master RAG Rules
- Agent Memory Domain Rules
- Project Progress
- 출력 형식 선호
- Part01에서 정한 State vs Memory 구분

불필요 Memory:
- 이전 웹 프로젝트 세부 코드
- 시험 풀이 기록
- 일회성 농담
```

좋은 구조:

```text
User Request
→ Identify Required Memory Type
→ Retrieve Relevant Memory
→ Validate Recency
→ Check Conflict
→ Use in State
→ Final Output
```

---

### [FAQ]

Q. Agent Memory Type이 뭐야?
A. Agent가 저장하고 재사용하는 기억을 목적과 수명에 따라 나눈 분류다.

Q. Memory Type을 왜 나눠야 해?
A. 현재 요청에 필요한 기억만 검색해 Retrieval 정확도를 높이고 Context 오염을 줄이기 위해 필요하다.

Q. 대표 Memory Type은?
A. Short-term Memory, Long-term Memory, Working Memory, Project Memory, User Preference Memory, Decision Memory, Conversation Summary가 있다.

Q. Memory Type을 구분하지 않으면?
A. 오래된 정보, 무관한 정보, 임시 정보가 현재 답변에 섞일 수 있다.

Q. 현재 요청에 필요한 Memory는 어떻게 고르나?
A. 현재 작업 목적, 프로젝트 범위, 최신성, 충돌 여부를 기준으로 고른다.

---

# 2. Short-term Memory

## 2.1 Short-term Memory 기본 규칙

### [개념]

Short-term Memory는 현재 대화나 현재 세션의 문맥을 유지하기 위한 기억이다.

최근 사용자 요청, 수정 사항, 임시 결정, 현재 작업 흐름을 저장한다.

Short-term Memory는 장기 저장을 전제로 하지 않는다.

```text
Short-term Memory = 현재 대화 흐름 유지용 기억
```

---

### [핵심]

Short-term Memory 포함 대상:

- Conversation Context
- Recent User Request
- Recent Decisions
- Recent Corrections
- Session Summary
- Temporary Preference
- Current Output Constraint
- Current Task Direction

Short-term Memory 제외 대상:

- 장기 프로젝트 확정 결정이 아닌 임시 의견
- 일회성 감정
- 농담
- 오래 유지할 필요 없는 작업 중간 표현
- 민감정보

---

### [실무]

현재 대화에서 Short-term Memory 예시:

```json
{
  "type": "short_term_memory",
  "currentTask": "Agent Memory State Management Part02 작성",
  "recentInstruction": "중간 응답 금지, 작업 완료 후 결과만 출력",
  "outputFormat": "writing block document",
  "style": "RAG Retrieval 최적화",
  "status": "active_in_current_chat"
}
```

Short-term Memory는 현재 문서 작성에는 중요하지만, 모든 내용을 Long-term Memory로 저장하지 않는다.

장기적으로 반복될 규칙만 Long-term Memory 후보가 된다.

---

### [FAQ]

Q. Short-term Memory는 뭐야?
A. 현재 대화나 세션 안에서 최근 요청, 수정, 결정 내용을 유지하는 기억이다.

Q. Short-term Memory에는 무엇을 넣어?
A. 최근 사용자 요청, 최근 수정, 현재 출력 형식, 임시 결정, 현재 작업 흐름을 넣는다.

Q. Short-term Memory는 오래 저장해?
A. 아니다. 현재 대화나 현재 작업이 끝나면 사라질 수 있다.

Q. Short-term Memory와 Long-term Memory 차이는?
A. Short-term Memory는 현재 세션 중심이고, Long-term Memory는 장기 재사용 중심이다.

Q. 사용자가 방금 수정한 내용은 어디에 반영해?
A. Short-term Memory에 즉시 반영하고 현재 작업 State에도 반영한다.

---

# 3. Long-term Memory

## 3.1 Long-term Memory 기본 규칙

### [개념]

Long-term Memory는 장기적으로 반복 재사용할 가치가 있는 정보를 저장하는 기억이다.

프로젝트 기술 스택, 문서 규칙, 사용자 선호, 확정 결정처럼 여러 작업에서 반복적으로 필요한 정보를 저장한다.

```text
Long-term Memory = 장기 재사용 가치가 있는 기억
```

---

### [핵심]

Long-term Memory 저장 후보:

- User Preference
- Project Context
- Technical Stack
- Architecture Decision
- Naming Rule
- Workflow Preference
- Persistent Constraint
- Reusable Pattern
- RAG Document Rule
- Agent Structure

Long-term Memory 저장 비추천:

- 임시 감정
- 단기 일정
- 확정되지 않은 아이디어
- 일회성 요청
- 민감정보
- Secret
- API Key
- Password
- Token

---

### [실무]

Long-term Memory 예시:

```json
{
  "type": "long_term_memory",
  "key": "rag_document_output_style",
  "value": "RAG 문서 제작/검수 전용 채팅에서는 writing block document 형식으로 최종 결과만 출력한다.",
  "updatedAt": "2026-07-01",
  "status": "active"
}
```

Long-term Memory는 사용 전 검증이 필요하다.

특히 프로젝트 진행 상태, 기술 버전, 문서 구조는 시간이 지나면 바뀔 수 있다.

검증 기준:

```text
Recency Check
→ Current Request Check
→ Conflict Check
→ Use / Update / Ignore
```

---

### [FAQ]

Q. Long-term Memory는 뭐야?
A. 프로젝트 기술 스택, 사용자 선호, 확정 결정처럼 장기적으로 재사용할 가치가 있는 기억이다.

Q. Long-term Memory에는 무엇을 저장해?
A. 프로젝트 목표, 기술 스택, 문서 규칙, Agent 구조, 사용자 출력 선호, 확정 결정을 저장한다.

Q. Long-term Memory를 무조건 믿어도 돼?
A. 아니다. 최신성, 관련성, 충돌 여부를 확인한 뒤 사용해야 한다.

Q. Long-term Memory에 저장하면 안 되는 것은?
A. API Key, 비밀번호, 토큰, 민감정보, 일회성 감정, 임시 아이디어는 저장하지 않는다.

Q. Long-term Memory가 오래되면?
A. Deprecated 처리하거나 최신 정보로 업데이트해야 한다.

---

# 4. Working Memory

## 4.1 Working Memory 기본 규칙

### [개념]

Working Memory는 Agent가 현재 작업을 수행하는 동안 임시로 사용하는 정보이다.

RAG 검색 결과, Tool Result, 후보 답안, 검증 결과처럼 현재 작업 처리에 필요한 임시 Context가 포함된다.

```text
Working Memory = 현재 작업 중 임시 작업 기억
```

Working Memory는 Long-term Memory가 아니다.

---

### [핵심]

Working Memory 포함 대상:

- Current Prompt Context
- Retrieved Context
- Tool Result
- Temporary Reasoning Data
- Candidate Solution
- Validation Result
- Draft Output
- Review Notes

Working Memory 규칙:

- 현재 작업에만 사용한다.
- 필요한 결과만 State에 요약 반영한다.
- 검색 결과 전체를 장기 저장하지 않는다.
- 임시 추론을 확정 사실처럼 저장하지 않는다.
- Tool 실패 결과와 성공 결과를 구분한다.

---

### [실무]

Working Memory 예시:

```text
현재 작업:
Agent Memory State Management Part02 작성

Working Memory:
- Domain Rules에서 Memory Types 관련 항목 확인
- Master Rules에서 FAQ / Retrieval Queries 구조 확인
- Project Progress에서 Level 2 AI 문서 위치 확인
- Part01과 중복되는 State vs Memory 설명 최소화
- Part02는 Memory Types 중심으로 구성
```

작업 완료 후 반영:

```text
State에 반영:
- Part02 작성 완료
- Memory Types 범위 작성
- 다음 Part 후보: Shared State / Project Memory / Decision Memory

Long-term Memory 후보:
- Part02 완료 상태
```

Working Memory 전체를 Long-term Memory에 저장하지 않는다.

---

### [FAQ]

Q. Working Memory는 뭐야?
A. Agent가 현재 작업 중 임시로 사용하는 RAG 검색 결과, Tool 결과, 후보 답안 같은 정보다.

Q. Working Memory와 Short-term Memory 차이는?
A. Working Memory는 작업 처리용 임시 정보이고, Short-term Memory는 현재 대화 흐름 유지용 기억이다.

Q. Working Memory를 Long-term Memory에 저장해?
A. 아니다. 필요한 결과만 요약하고 임시 정보 전체는 저장하지 않는다.

Q. Tool Result는 Working Memory야?
A. 현재 작업 중 임시로 사용하는 Tool Result는 Working Memory에 해당한다.

Q. Working Memory가 너무 많으면?
A. 현재 답변에 필요한 핵심 정보만 남기고 나머지는 제거하거나 요약한다.

---

# 5. Project Memory

## 5.1 Project Memory 기본 규칙

### [개념]

Project Memory는 특정 프로젝트의 지속적인 맥락을 저장하는 기억이다.

프로젝트 목표, 기술 스택, 폴더 구조, Agent 구조, 진행 상황, 확정 결정을 저장한다.

```text
Project Memory = 특정 프로젝트의 장기 맥락 기억
```

---

### [핵심]

Project Memory 포함 대상:

- Project Goal
- Current Stack
- Hardware Context
- Folder Structure
- Agent Architecture
- RAG Document Rules
- Domain Rules
- Progress Status
- Pending Tasks
- Decisions
- Roadmap

Project Memory 규칙:

- 프로젝트별로 Scope를 분리한다.
- 완료된 작업과 예정 작업을 구분한다.
- 임시 아이디어와 확정 결정을 구분한다.
- 프로젝트 상황이 바뀌면 업데이트한다.
- 다른 프로젝트 Memory를 섞지 않는다.

---

### [실무]

개인 AI 프로젝트 Project Memory 예시:

```json
{
  "type": "project_memory",
  "project": "Personal AI Project",
  "goal": "단순 RAG 챗봇이 아닌 개인 AI 개발팀 Multi-Agent System 구축",
  "stack": ["AnythingLLM", "Ollama", "Qwen2.5", "BGE-M3"],
  "currentLevel": "Level 2 AI & Agent AI",
  "currentDocument": "Agent Memory & State Management",
  "status": "in_progress"
}
```

Project Memory는 Agent Routing과 RAG Scope 결정에 사용한다.

예시:

```text
Backend 요청 → Backend Foundation Memory 검색
Agent 설계 요청 → AI / Agent AI Memory 검색
Frontend 요청 → Frontend Foundation Memory 검색
```

---

### [FAQ]

Q. Project Memory는 뭐야?
A. 특정 프로젝트의 목표, 기술 스택, 문서 구조, Agent 구조, 진행 상황, 확정 결정을 저장하는 기억이다.

Q. Project Memory에는 무엇을 저장해?
A. Project Goal, Current Stack, Folder Structure, Agent Architecture, RAG Document Rules, Progress Status를 저장한다.

Q. Project Memory는 왜 중요해?
A. 장기 프로젝트에서 이전 결정과 현재 진행 상황을 유지해 반복 설명을 줄이고 일관성을 높이기 때문이다.

Q. 프로젝트가 여러 개면 어떻게 해?
A. Project Scope를 분리하고 현재 요청과 관련된 Project Memory만 검색한다.

Q. Project Progress는 Memory로 저장해도 돼?
A. 가능하지만 진행 상황은 자주 바뀌므로 최신성 확인과 갱신이 필요하다.

---

# 6. User Preference Memory

## 6.1 User Preference Memory 기본 규칙

### [개념]

User Preference Memory는 사용자의 응답 선호와 작업 방식을 저장하는 기억이다.

언어, 톤, 출력 형식, 문서 스타일, Follow-up 방식처럼 이후 응답 품질을 높이는 정보를 저장한다.

```text
User Preference Memory = 사용자 응답 선호 기억
```

---

### [핵심]

User Preference Memory 포함 대상:

- Language Preference
- Tone Preference
- Output Format Preference
- Document Style
- Workflow Preference
- Follow-up Preference
- Code Explanation Preference
- Review Style Preference

주의 대상:

- 일시적 기분
- 농담성 표현
- 민감한 개인 속성
- 현재 요청에만 해당하는 임시 선호
- 명확하지 않은 추정 선호

---

### [실무]

User Preference Memory 예시:

```json
{
  "type": "user_preference_memory",
  "language": "Korean",
  "tone": "casual but practical",
  "documentStyle": "RAG optimized Markdown",
  "outputFormat": "writing block document",
  "prefersFinalReadyDraft": true,
  "avoidIntermediateResponse": true
}
```

현재 요청이 User Preference Memory와 다르면 현재 요청을 우선한다.

예시:

```text
기존 선호:
짧게 설명

현재 요청:
상세한 RAG 문서 작성

처리:
현재 요청 우선 → 상세 문서 작성
```

---

### [FAQ]

Q. User Preference Memory는 뭐야?
A. 사용자의 언어, 톤, 출력 형식, 문서 스타일, 작업 방식 선호를 저장하는 기억이다.

Q. User Preference Memory에는 무엇을 저장해?
A. 한국어 선호, 실무 중심 설명, RAG 최적화 Markdown, writing block 출력 같은 반복 선호를 저장한다.

Q. 일시적 기분도 저장해?
A. 아니다. 장기적으로 응답 품질에 도움이 되는 반복 선호만 저장한다.

Q. 현재 요청이 기존 선호와 다르면?
A. 현재 요청을 우선한다.

Q. 민감한 개인 속성도 저장해?
A. 명시 요청이 없으면 저장하지 않는다.

---

# 7. Decision Memory

## 7.1 Decision Memory 기본 규칙

### [개념]

Decision Memory는 프로젝트에서 확정된 결정을 저장하는 기억이다.

결정 내용, 이유, 날짜, 적용 범위, 대안, 상태를 함께 저장한다.

```text
Decision Memory = 프로젝트 확정 결정 기록
```

---

### [핵심]

Decision Memory 필수 요소:

- Decision
- Reason
- Date
- Scope
- Alternatives
- Status
- UpdatedBy
- Related Documents

Decision Memory 규칙:

- 논의 중인 아이디어를 확정 결정처럼 저장하지 않는다.
- 변경 가능한 결정은 status를 표시한다.
- 결정 이유를 함께 저장한다.
- 결정 변경 시 이전 결정과 충돌 처리한다.
- 최신 결정이 오래된 결정 Memory보다 우선한다.

---

### [실무]

Decision Memory 예시:

```json
{
  "type": "decision_memory",
  "decision": "Agent 문서와 RAG 문서는 분리해서 관리한다.",
  "reason": "Agent 실행 구조와 학습/검색용 문서는 역할이 다르기 때문",
  "date": "2026-07-01",
  "scope": "Personal AI Project / RAG Directory",
  "alternatives": ["Agent와 문서를 같은 폴더에 혼합"],
  "status": "active",
  "updatedBy": "user"
}
```

Decision Memory는 같은 논의를 반복하지 않도록 돕는다.

Review Agent는 Decision Memory를 기준으로 문서 일관성을 검토할 수 있다.

---

### [FAQ]

Q. Decision Memory는 뭐야?
A. 프로젝트에서 확정한 결정과 그 이유, 날짜, 범위, 상태를 저장하는 기억이다.

Q. Decision Memory는 왜 필요해?
A. 이전에 정한 방향을 유지하고 같은 논의를 반복하지 않기 위해 필요하다.

Q. Decision Memory에는 무엇을 넣어?
A. Decision, Reason, Date, Scope, Alternatives, Status, UpdatedBy를 넣는다.

Q. 임시 아이디어도 Decision Memory에 저장해?
A. 아니다. 확정되지 않은 아이디어는 Decision Memory로 저장하지 않는다.

Q. 오래된 Decision과 최신 결정이 충돌하면?
A. 최신 프로젝트 결정을 우선하고 오래된 Decision은 deprecated 처리하거나 갱신한다.

---

# 8. Conversation Summary

## 8.1 Conversation Summary 기본 규칙

### [개념]

Conversation Summary는 긴 대화를 압축해 Context를 유지하는 방식이다.

대화 전체를 그대로 유지하지 않고 핵심 사실, 결정, 현재 작업, 열린 질문, 다음 단계를 요약한다.

```text
Conversation Summary = 긴 대화의 핵심 Context 압축
```

---

### [핵심]

Conversation Summary 포함 대상:

- Summary
- Key Decisions
- Current Task
- Open Questions
- Next Step
- Important Constraints
- Updated Context
- Deprecated Context

Conversation Summary 제외 대상:

- 반복 감정 표현
- 불필요한 농담
- 이미 완료되어 필요 없는 중간 과정
- 오래된 오류 세부 로그 전체
- 현재 작업과 무관한 내용

---

### [실무]

Conversation Summary 예시:

```md
## Summary

개인 AI 프로젝트는 AnythingLLM + Ollama + Qwen2.5 + BGE-M3 기반으로 진행한다.

## Key Decisions

- RAG 문서와 Agent 실행 구조는 분리한다.
- Domain Rules는 RAG 문서 제작 기준으로 사용한다.
- 출력은 writing block document 형식을 유지한다.

## Current Task

Agent Memory State Management Part02 작성.

## Next Step

Part03에서 Shared State / Multi-Agent State 구조 작성.
```

Conversation Summary는 Context Window 절약과 장기 작업 이어가기에 유용하다.

다만 요약 과정에서 중요한 제약을 누락하면 같은 오류가 반복된다.

---

### [FAQ]

Q. Conversation Summary는 뭐야?
A. 긴 대화에서 핵심 사실, 결정, 현재 작업, 다음 단계를 압축해 유지하는 요약 기억이다.

Q. Conversation Summary는 언제 필요해?
A. 대화가 길어져 Context Window를 많이 차지하거나 작업을 이어가야 할 때 필요하다.

Q. Conversation Summary에는 무엇을 넣어?
A. Summary, Key Decisions, Current Task, Open Questions, Next Step, Important Constraints를 넣는다.

Q. 요약할 때 주의할 점은?
A. 중요한 제약, 최신 결정, 현재 작업 상태를 누락하지 않아야 한다.

Q. Conversation Summary는 Long-term Memory야?
A. 장기 보관될 수 있지만, 기본 목적은 긴 대화의 Context 압축이다.

---

# 9. Memory Type Comparison

## 9.1 Memory Type 비교 기준

### [개념]

Memory Type 비교는 각 기억의 목적, 수명, 사용 시점, 위험 요소를 구분하기 위해 필요하다.

비교 기준이 명확하면 Agent가 적절한 Memory만 검색하고 사용할 수 있다.

---

### [핵심]

| Memory Type            | 목적                | 수명           | 예시                       | 주의                |
| ---------------------- | ------------------- | -------------- | -------------------------- | ------------------- |
| Short-term Memory      | 현재 대화 유지      | 세션 중심      | 최근 요청, 현재 출력 형식  | 장기 저장 남발 금지 |
| Long-term Memory       | 장기 정보 재사용    | 장기           | 기술 스택, 사용자 선호     | 최신성 검증 필요    |
| Working Memory         | 현재 작업 임시 처리 | 작업 중        | RAG 검색 결과, Tool Result | 전체 저장 금지      |
| Project Memory         | 프로젝트 맥락 유지  | 장기           | 목표, 진행상황, 구조       | 프로젝트 Scope 분리 |
| User Preference Memory | 사용자 선호 반영    | 장기 가능      | 언어, 톤, 문서 스타일      | 현재 요청 우선      |
| Decision Memory        | 확정 결정 유지      | 장기           | 구조 결정, 설계 결정       | 임시 의견 저장 금지 |
| Conversation Summary   | 긴 대화 압축        | 세션 또는 장기 | 핵심 요약, 다음 작업       | 제약 누락 금지      |

---

### [실무]

요청별 Memory Type 선택 예시:

```text
요청: "이전 결정대로 문서 구조 맞춰줘"
→ Decision Memory
→ Project Memory
→ User Preference Memory

요청: "방금 말한 형식으로 다시 작성해줘"
→ Short-term Memory
→ Current State

요청: "현재 프로젝트 진행 상황 기준으로 다음 문서 만들어줘"
→ Project Memory
→ Project Progress
→ Domain Rules

요청: "검색 결과 기반으로 초안 검수해줘"
→ Working Memory
→ Retrieved Context
→ Review Findings
```

Memory Retrieval은 Query보다 먼저 Memory Type을 좁히면 정확도가 올라간다.

---

### [FAQ]

Q. Memory Type 비교가 왜 필요해?
A. 현재 요청에 맞는 기억만 검색하고 오래된 정보나 임시 정보를 잘못 사용하지 않기 위해 필요하다.

Q. Short-term Memory와 Working Memory 차이는?
A. Short-term Memory는 대화 흐름 유지용이고, Working Memory는 현재 작업 처리용 임시 정보다.

Q. Project Memory와 Decision Memory 차이는?
A. Project Memory는 프로젝트 전체 맥락이고, Decision Memory는 확정된 결정 기록이다.

Q. User Preference Memory와 현재 요청 중 무엇이 우선이야?
A. 현재 요청이 우선이다.

Q. Conversation Summary는 어떤 Memory와 가까워?
A. Short-term Memory와 Long-term Memory 사이에 있으며, 긴 대화의 핵심 Context 압축에 사용된다.

---

# 10. Common Mistakes

## 10.1 Memory Type 혼동

### [개념]

Memory Type을 구분하지 않으면 Agent가 임시 정보, 오래된 정보, 프로젝트 결정, 사용자 선호를 같은 수준으로 처리한다.

이로 인해 Retrieval 오염, 잘못된 결정, 불필요한 Context 증가가 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Working Memory를 Long-term Memory에 그대로 저장
- Short-term Memory를 확정 결정으로 오해
- User Preference를 현재 요청보다 우선
- Project Memory Scope를 구분하지 않음
- Decision Memory 없이 프로젝트 방향 변경
- Conversation Summary에서 중요한 제약 누락
- 오래된 Project Progress를 최신 상태로 사용
- 민감정보를 Memory에 저장

---

### [실무]

문제:

```text
Agent가 방금 작업 중 나온 후보안을 확정 결정처럼 사용함
```

원인:

```text
Working Memory와 Decision Memory 구분 실패
```

해결:

```text
Candidate Solution → Working Memory
Confirmed Decision → Decision Memory
Final Output 반영 후 필요한 내용만 Project Memory 후보
```

문제:

```text
Agent가 이전 출력 선호를 현재 요청보다 우선함
```

원인:

```text
User Preference Memory와 Current Request 우선순위 미적용
```

해결:

```text
Current User Request 우선
→ User Preference는 보조 자료로만 사용
→ 반복 선호가 변경되면 Memory Update 후보
```

---

### [FAQ]

Q. Memory Type 혼동의 대표 문제는?
A. 임시 작업 정보가 장기 기억처럼 사용되거나 오래된 정보가 현재 요청을 덮어쓰는 문제다.

Q. Working Memory를 그대로 저장하면 왜 문제야?
A. 임시 후보안, 실패한 Tool Result, 검토 전 정보가 나중에 사실처럼 검색될 수 있다.

Q. Short-term Memory를 Decision Memory처럼 쓰면?
A. 임시 대화 흐름이 프로젝트 확정 결정처럼 오해될 수 있다.

Q. User Preference가 현재 요청과 다르면?
A. 현재 요청을 우선하고 User Preference는 보조 정보로만 사용한다.

Q. Memory Type 혼동을 막는 방법은?
A. 저장 전 type, scope, status, updatedAt, confidence를 명확히 기록한다.

---

# 11. Best Practice

## 11.1 Memory Type 설계 원칙

### [개념]

좋은 Memory 설계는 Memory Type을 명확히 나누고 현재 요청에 필요한 기억만 검색한다.

Memory는 많이 저장하는 것보다 정확하게 저장하고 정확하게 검색하는 것이 중요하다.

---

### [핵심]

Best Practice:

- Memory Type을 명확히 구분한다.
- Memory마다 type, scope, status, updatedAt을 기록한다.
- 현재 요청에 필요한 Memory Type만 검색한다.
- Working Memory 전체를 장기 저장하지 않는다.
- Short-term Memory와 Decision Memory를 구분한다.
- Project Memory는 프로젝트별로 Scope를 나눈다.
- User Preference는 현재 요청보다 우선하지 않는다.
- Decision Memory에는 이유와 날짜를 포함한다.
- Conversation Summary에는 핵심 제약을 반드시 포함한다.
- 오래된 Memory는 Recency Check 후 사용한다.
- 민감정보와 Secret은 Memory에 저장하지 않는다.

---

### [실무]

권장 Memory Schema:

```json
{
  "type": "project_memory",
  "scope": "Personal AI Project",
  "key": "agent_memory_state_management",
  "value": "Agent Memory & State Management 문서 제작 진행 중",
  "status": "active",
  "updatedAt": "2026-07-01",
  "confidence": "high",
  "source": "user_request"
}
```

권장 Retrieval Flow:

```text
User Request
→ Detect Project Scope
→ Detect Required Memory Type
→ Retrieve Relevant Memory
→ Recency Check
→ Conflict Check
→ Apply Current Request Priority
→ Use in Output
```

권장 저장 판단:

```text
현재 작업 임시 정보 → Working Memory
현재 대화 흐름 → Short-term Memory
반복 출력 선호 → User Preference Memory
프로젝트 진행 상태 → Project Memory
확정 결정 → Decision Memory
긴 대화 압축 → Conversation Summary
```

---

### [FAQ]

Q. 좋은 Memory Type 설계 기준은?
A. type, scope, status, updatedAt, confidence를 명확히 기록하고 현재 요청에 필요한 기억만 검색하는 것이다.

Q. Memory를 많이 저장하면 성능이 좋아져?
A. 아니다. 무분별한 저장은 Retrieval 오염을 만들 수 있다.

Q. Memory Retrieval 전에 먼저 할 일은?
A. 현재 요청의 Project Scope와 필요한 Memory Type을 식별한다.

Q. Memory 저장 전 확인할 것은?
A. 장기 유용성, 민감정보 여부, 현재 요청과 충돌 여부, 확정 여부를 확인한다.

Q. 가장 중요한 Memory 원칙은?
A. 필요한 Memory만 저장하고, 필요한 Memory만 검색하며, 현재 요청을 항상 우선하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Agent Memory Type이 뭐야?
A. Agent가 저장하고 재사용하는 기억을 목적과 수명에 따라 나눈 분류다.

Q. Agent Memory에는 어떤 종류가 있어?
A. Short-term Memory, Long-term Memory, Working Memory, Project Memory, User Preference Memory, Decision Memory, Conversation Summary가 있다.

Q. Short-term Memory는 뭐야?
A. 현재 대화나 세션 안에서 최근 요청, 수정, 결정 내용을 유지하는 기억이다.

Q. Long-term Memory는 뭐야?
A. 프로젝트 기술 스택, 사용자 선호, 확정 결정처럼 장기적으로 재사용할 가치가 있는 기억이다.

Q. Working Memory는 뭐야?
A. Agent가 현재 작업 중 임시로 사용하는 RAG 검색 결과, Tool 결과, 후보 답안 같은 정보다.

Q. Project Memory는 뭐야?
A. 특정 프로젝트의 목표, 기술 스택, 문서 구조, Agent 구조, 진행 상황, 확정 결정을 저장하는 기억이다.

Q. User Preference Memory는 뭐야?
A. 사용자의 언어, 톤, 출력 형식, 문서 스타일, 작업 방식 선호를 저장하는 기억이다.

Q. Decision Memory는 뭐야?
A. 프로젝트에서 확정한 결정과 그 이유, 날짜, 범위, 상태를 저장하는 기억이다.

Q. Conversation Summary는 뭐야?
A. 긴 대화에서 핵심 사실, 결정, 현재 작업, 다음 단계를 압축해 유지하는 요약 기억이다.

Q. Short-term Memory와 Long-term Memory 차이는?
A. Short-term Memory는 현재 세션 중심이고, Long-term Memory는 장기 재사용 중심이다.

Q. Working Memory와 Short-term Memory 차이는?
A. Working Memory는 현재 작업 처리용 임시 정보이고, Short-term Memory는 현재 대화 흐름 유지용 기억이다.

Q. Project Memory와 Decision Memory 차이는?
A. Project Memory는 프로젝트 전체 맥락이고, Decision Memory는 확정된 결정 기록이다.

Q. User Preference Memory와 현재 요청 중 무엇이 우선이야?
A. 현재 사용자 요청이 우선이다.

Q. Memory Type을 왜 구분해야 해?
A. 현재 요청에 필요한 기억만 검색해 Retrieval 정확도를 높이고 Context 오염을 줄이기 위해 필요하다.

Q. Memory Type을 구분하지 않으면 어떻게 돼?
A. 오래된 정보, 임시 정보, 무관한 프로젝트 정보가 현재 답변에 섞일 수 있다.

Q. Working Memory를 Long-term Memory에 저장해도 돼?
A. 아니다. 현재 작업에 필요한 결과만 요약하고 임시 정보 전체는 저장하지 않는다.

Q. Decision Memory에는 무엇을 저장해?
A. Decision, Reason, Date, Scope, Alternatives, Status, UpdatedBy를 저장한다.

Q. Project Memory에는 무엇을 저장해?
A. Project Goal, Current Stack, Folder Structure, Agent Architecture, RAG Document Rules, Progress Status를 저장한다.

Q. User Preference Memory에는 무엇을 저장해?
A. Language Preference, Tone Preference, Output Format Preference, Document Style, Workflow Preference를 저장한다.

Q. Conversation Summary에는 무엇을 넣어?
A. Summary, Key Decisions, Current Task, Open Questions, Next Step, Important Constraints를 넣는다.

Q. Memory Retrieval 전에 무엇을 확인해?
A. 현재 요청의 Project Scope와 필요한 Memory Type을 먼저 확인한다.

Q. Memory 저장 전 확인할 것은?
A. 장기 유용성, 민감정보 여부, 확정 여부, 충돌 여부를 확인한다.

Q. 오래된 Memory는 어떻게 처리해?
A. Recency Check를 하고 현재 요청이나 최신 결정과 충돌하면 업데이트하거나 무시한다.

Q. 민감정보를 Memory에 저장해도 돼?
A. API Key, 비밀번호, 토큰, 민감한 개인정보는 저장하지 않는 것이 원칙이다.

Q. Memory Type 설계의 핵심은?
A. 필요한 Memory만 저장하고, 필요한 Memory만 검색하며, 현재 요청을 항상 우선하는 것이다.
