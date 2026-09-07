# Agent Memory & State Management Part06 - Memory Retrieval, Memory Update & Memory Validation

---

# 1. Memory Retrieval Foundation

## 1.1 Memory Retrieval 기본 개념

### [개념]

Memory Retrieval은 현재 사용자 요청을 처리하는 데 필요한 Memory만 검색하고 사용하는 과정이다.

Memory Retrieval은 모든 Memory를 불러오는 작업이 아니다.

현재 작업과 관련 있는 Memory를 찾고, 최신성, 신뢰도, 충돌 여부를 확인한 뒤 State에 반영한다.

```text
Memory Retrieval = 현재 요청에 필요한 Memory만 검색하고 검증해 사용하는 과정
```

기본 Flow:

```text
User Request
→ Identify Missing Context
→ Select Memory Type
→ Search Relevant Memory
→ Filter by Relevance
→ Check Recency
→ Check Conflict
→ Use in Current State
```

---

### [핵심]

- Memory Retrieval은 현재 요청 중심으로 수행한다.
- 모든 Memory를 검색하지 않는다.
- 현재 작업에 필요한 Memory Type을 먼저 식별한다.
- 검색된 Memory는 관련성 기준으로 필터링한다.
- 오래된 Memory는 최신성 검증 후 사용한다.
- 충돌 Memory는 우선순위 규칙으로 해결한다.
- Memory는 현재 요청보다 우선하지 않는다.
- Retrieval 결과 전체를 State에 저장하지 않는다.
- 필요한 핵심만 요약해 State에 반영한다.

---

### [실무]

2026 실무 기준 Agent는 Memory Retrieval을 무작위 검색으로 처리하지 않는다.

먼저 현재 요청이 어떤 Memory를 필요로 하는지 분류한다.

예시:

```text
요청:
Agent Memory State Management Part06 작성

필요 Memory Type:
- Project Memory
- Domain Rules
- User Preference Memory
- Conversation Summary
- Decision Memory

필요 Context:
- MASTER_RAG_RULES
- Agent Memory State Management Domain Rules
- Project Progress
- 현재 출력 형식 규칙
- 이전 Part 진행 상태
```

불필요 Memory 예시:

```text
- 웹 프로젝트 코드 세부사항
- 시험 풀이 기록
- 하드웨어 설정 세부사항
- 현재 문서와 무관한 과거 대화
- 일회성 감정 표현
```

Memory Retrieval은 적게 검색하는 것이 아니라 정확하게 검색하는 것이 목표다.

---

### [FAQ]

Q. Memory Retrieval이 뭐야?
A. 현재 요청을 처리하는 데 필요한 과거 정보만 검색하고 검증해 사용하는 과정이다.

Q. 모든 Memory를 검색하면 안 돼?
A. 관련 없는 정보가 현재 답변에 섞이고 Context Window를 낭비하므로 좋지 않다.

Q. Memory Retrieval은 언제 해?
A. 현재 요청을 처리하는 데 프로젝트 맥락, 사용자 선호, 과거 결정, 진행 상태가 필요할 때 수행한다.

Q. Retrieval 결과는 전부 State에 저장해?
A. 아니다. 현재 작업에 필요한 핵심 내용만 요약해 State에 반영한다.

Q. Memory Retrieval의 핵심은?
A. 현재 요청에 필요한 Memory만 찾고 최신성, 관련성, 충돌 여부를 확인하는 것이다.

---

# 2. Retrieval Query Design

## 2.1 Memory 검색 Query 설계

### [개념]

Retrieval Query Design은 Memory 검색에 사용할 Query를 설계하는 기준이다.

좋은 Query는 현재 요청과 관련된 Memory Type, 핵심 키워드, 사용자 표현을 포함한다.

```text
Retrieval Query Design = 필요한 Memory를 정확히 찾기 위한 검색어 설계
```

---

### [핵심]

좋은 Retrieval Query 조건:

- 현재 요청과 직접 관련됨
- 핵심 Domain 용어 포함
- 사용자 실제 질문 표현 포함
- Memory Type을 암시함
- 너무 넓지 않음
- 너무 짧지 않음
- 최신성 확인이 필요한 경우 날짜 또는 진행 상태 포함
- 프로젝트 Scope 포함

나쁜 Query:

```text
Memory
Agent
문서
이전 내용
규칙
```

좋은 Query:

```text
Agent Memory State Management Memory Retrieval Rules
현재 요청에 필요한 Memory만 검색하는 기준
Project Memory와 Decision Memory 검색 기준
Memory Retrieval Recency Conflict Validation
RAG 문서 작성 출력 형식 사용자 선호
```

---

### [실무]

RAG 문서 제작 Query 예시:

```text
MASTER_RAG_RULES FAQ Retrieval Queries 필수 구조
Agent Memory State Management Memory Retrieval Rules
Memory Update 저장 후보 저장 비추천 기준
Memory Validation Recency Check Conflict Check
Project Progress Level 2 Agent Memory State Management 상태
```

Multi-Agent 개발 Query 예시:

```text
PM Agent Shared State current request requirements constraints
Backend Frontend apiContract Decision Memory latest active
Review Agent previous findings unresolved issues
Checkpoint Resume current workflow last valid state
```

User Preference Query 예시:

```text
사용자 RAG 문서 출력 형식 선호
writing block document 출력 규칙
중간 응답 금지 최종 결과만 출력
한국어 실무 중심 RAG Retrieval 최적화 선호
```

Retrieval Query는 검색 대상 Memory를 좁히는 역할을 한다.

---

### [FAQ]

Q. Retrieval Query Design이 뭐야?
A. 필요한 Memory를 정확히 검색하기 위해 Query를 설계하는 기준이다.

Q. 좋은 Retrieval Query는 어떤 Query야?
A. 현재 요청, 핵심 용어, Memory Type, 프로젝트 Scope, 사용자 표현을 포함하는 Query다.

Q. 너무 짧은 Query는 왜 문제야?
A. 관련 없는 Memory까지 많이 검색되어 Retrieval 오염이 발생할 수 있다.

Q. 사용자 표현을 Query에 넣는 이유는?
A. 실제 질문 표현과 Memory의 FAQ 표현이 매칭되어 검색 정확도가 올라가기 때문이다.

Q. Retrieval Query의 목표는?
A. 현재 작업에 필요한 Memory만 빠르게 찾는 것이다.

---

# 3. Memory Type Filtering

## 3.1 Memory Type 기준 필터링

### [개념]

Memory Type Filtering은 검색된 Memory를 유형별로 분류하고 현재 요청에 맞는 Memory만 사용하는 과정이다.

Memory Type을 구분하지 않으면 Project Memory, User Preference Memory, Decision Memory, Working Memory가 섞여 잘못 사용될 수 있다.

```text
Memory Type Filtering = Memory 유형 기준으로 필요한 기억만 선택하는 과정
```

---

### [핵심]

필터링 대상 Memory Type:

- Short-term Memory
- Long-term Memory
- Working Memory
- Project Memory
- User Preference Memory
- Decision Memory
- Conversation Summary

필터링 기준:

- 현재 요청과 직접 관련 있는가?
- 현재 프로젝트 Scope와 일치하는가?
- 장기 Memory인지 임시 Working Memory인지 구분되는가?
- 확정 Decision인지 임시 아이디어인지 구분되는가?
- 사용자 선호가 현재 요청과 충돌하지 않는가?
- 최신성이 필요한 정보인가?

---

### [실무]

Memory Type 선택 예시:

```text
요청:
"다음 Part 작성"

필요:
- Conversation Summary: 이전 Part 진행 상태
- Project Memory: 현재 프로젝트 문서 로드맵
- Domain Rules: 작성 대상 Domain 규칙
- User Preference Memory: 출력 형식
- Decision Memory: Part 구성 결정

불필요:
- Working Memory의 임시 초안
- 무관한 프로젝트 Memory
- 오래된 출력 선호
```

필터링 결과 State 반영 예시:

```json
{
  "retrievedMemorySummary": {
    "projectMemory": [
      "Agent Memory & State Management는 Level 2 AI & Agent AI 문서"
    ],
    "userPreferenceMemory": ["출력은 writing block document 형식"],
    "decisionMemory": ["총 8 Part 구성"],
    "domainRules": ["Memory Retrieval, Update, Validation 포함"]
  }
}
```

Memory Type Filtering은 Retrieval 이후 반드시 수행한다.

---

### [FAQ]

Q. Memory Type Filtering이 뭐야?
A. 검색된 Memory를 유형별로 분류하고 현재 요청에 맞는 Memory만 사용하는 과정이다.

Q. 왜 Memory Type을 필터링해야 해?
A. 임시 정보, 오래된 정보, 프로젝트 결정, 사용자 선호가 섞이면 잘못된 답변이 나올 수 있기 때문이다.

Q. 현재 문서 작성에 필요한 Memory Type은?
A. Project Memory, Domain Rules, User Preference Memory, Decision Memory, Conversation Summary가 주로 필요하다.

Q. Working Memory는 언제 제외해?
A. 임시 후보안이나 검증 전 정보가 현재 작업에 불필요하면 제외한다.

Q. 필터링 후 무엇을 해야 해?
A. 관련 Memory만 요약해 State에 반영하고 최신성 및 충돌 여부를 검증한다.

---

# 4. Relevance Check

## 4.1 Memory 관련성 검증

### [개념]

Relevance Check는 검색된 Memory가 현재 사용자 요청과 실제로 관련 있는지 확인하는 과정이다.

검색되었다고 해서 모두 사용하면 안 된다.

```text
Relevance Check = 검색된 Memory가 현재 요청과 관련 있는지 검증
```

---

### [핵심]

Relevance Check 기준:

- 현재 요청의 Domain과 일치하는가?
- 현재 작업 단계와 관련 있는가?
- 현재 출력 형식에 필요한가?
- 최신 진행 상태 판단에 필요한가?
- 현재 Agent가 수행할 작업에 필요한가?
- 다른 프로젝트 정보가 섞이지 않았는가?
- 단순 키워드 매칭이 아니라 의미상 관련 있는가?

관련성 낮은 Memory:

- 같은 단어가 있지만 다른 프로젝트 정보
- 과거 임시 아이디어
- 완료되어 현재 필요 없는 세부 작업 로그
- 현재 요청과 무관한 기술 스택
- 오래된 진행 상태

---

### [실무]

예시:

```text
현재 요청:
Agent Memory State Management Part06 작성

검색된 Memory:
"FestaPick NotificationRepository 메서드 검토"

판단:
Agent Memory 문서 작성과 직접 관련 없음
→ 사용하지 않음
```

예시:

```text
검색된 Memory:
"RAG 문서 제작/검수 전용, writing block document 출력"

판단:
현재 출력 형식과 직접 관련 있음
→ 사용
```

예시:

```text
검색된 Memory:
"State와 Memory는 반드시 구분"

판단:
Part06 Memory Retrieval / Update / Validation에서도 핵심 원칙
→ 사용
```

Relevance Check는 Retrieval 오염을 줄이는 핵심 단계다.

---

### [FAQ]

Q. Relevance Check가 뭐야?
A. 검색된 Memory가 현재 사용자 요청과 실제로 관련 있는지 확인하는 과정이다.

Q. 검색된 Memory는 모두 사용해도 돼?
A. 아니다. 관련성이 낮은 Memory는 현재 답변을 오염시킬 수 있다.

Q. 관련성 판단 기준은?
A. 현재 요청 Domain, 작업 단계, 프로젝트 Scope, 출력 형식, Agent 작업 필요성과 일치하는지 확인한다.

Q. 같은 키워드가 있으면 관련 Memory야?
A. 아니다. 의미상 현재 작업과 연결되는지 확인해야 한다.

Q. 관련성 낮은 Memory는 어떻게 해?
A. 현재 작업 State에 반영하지 않고 무시한다.

---

# 5. Recency Check

## 5.1 Memory 최신성 검증

### [개념]

Recency Check는 Memory가 현재도 유효한지 확인하는 과정이다.

Memory는 시간이 지나면 프로젝트 진행 상황, 기술 스택, 문서 구조, 사용자 선호와 달라질 수 있다.

```text
Recency Check = Memory가 현재도 유효한지 확인하는 최신성 검증
```

---

### [핵심]

Recency Check 대상:

- Project Progress
- Technical Stack
- Agent Architecture
- Folder Structure
- Roadmap
- Pending Tasks
- Version Information
- User Preference
- Decision Status
- Tool Result
- External Facts

Recency Check 기준:

- updatedAt이 있는가?
- status가 active인가 deprecated인가?
- 현재 사용자 요청과 충돌하지 않는가?
- 최신 Project Progress와 일치하는가?
- 최근 대화에서 정정된 내용이 있는가?
- 기술 버전이 현재 기준으로 유효한가?

---

### [실무]

Recency Check 예시:

```json
{
  "memory": "Agent Memory & State Management는 Planned 상태",
  "updatedAt": "older_project_progress",
  "currentContext": "Part06 작성 진행 중",
  "recencyResult": "outdated",
  "action": "update_to_in_progress_or_completed_parts"
}
```

Recency Check 예시:

```json
{
  "memory": "출력은 writing block document 형식",
  "updatedAt": "current_chat",
  "currentContext": "RAG 문서 제작/검수 전용",
  "recencyResult": "valid",
  "action": "use"
}
```

Recency 위험이 큰 Memory:

```text
- 현재 진행 상태
- 예정 작업
- 프로젝트 파일 구조
- 설치된 모델 버전
- API 사양
- 라이브러리 버전
- 외부 서비스 정책
```

오래된 Memory는 단정하지 않고 현재 요청과 최신 자료 기준으로 검증한다.

---

### [FAQ]

Q. Recency Check가 뭐야?
A. Memory가 현재도 유효한지 확인하는 최신성 검증 과정이다.

Q. 어떤 Memory에 Recency Check가 필요해?
A. 프로젝트 진행 상태, 기술 스택, 문서 구조, 버전 정보, 사용자 선호, 결정 상태에 필요하다.

Q. 오래된 Memory는 사용하면 안 돼?
A. 무조건 금지는 아니지만 현재 요청과 최신 결정과 충돌하는지 확인해야 한다.

Q. updatedAt이 없으면 어떻게 해?
A. 신뢰도를 낮게 보고 현재 Context나 최신 Project Progress로 검증한다.

Q. Recency Check의 핵심은?
A. 오래된 Memory를 현재 사실처럼 사용하지 않는 것이다.

---

# 6. Memory Update Foundation

## 6.1 Memory Update 기본 개념

### [개념]

Memory Update는 새로운 정보가 장기적으로 유용한지 판단하고 저장, 수정, 폐기하는 과정이다.

Memory Update는 모든 대화를 저장하는 작업이 아니다.

```text
Memory Update = 장기적으로 유용한 정보만 저장하거나 갱신하는 과정
```

기본 Flow:

```text
New Information
→ Check Long-term Usefulness
→ Check Sensitivity
→ Check User Intent
→ Check Conflict
→ Save / Update / Ignore / Deprecate
```

---

### [핵심]

- Memory Update는 신중하게 수행한다.
- 장기적으로 반복 재사용할 가치가 있는 정보만 저장한다.
- 사용자 명시 요청은 우선 고려한다.
- 민감정보는 저장하지 않는다.
- 불확실한 추정은 확정 Memory로 저장하지 않는다.
- 임시 아이디어는 Decision Memory로 저장하지 않는다.
- 기존 Memory와 충돌하면 Conflict 처리 후 업데이트한다.
- 오래된 Memory는 deprecated 처리할 수 있다.

---

### [실무]

Memory Update 후보:

```text
- 장기 프로젝트 목표
- 기술 스택
- 폴더 구조
- RAG 문서 규칙
- Agent 구조
- 반복 출력 선호
- 확정 결정
- 진행 상태 변화
- 완료된 문서 목록
```

Memory Update 비추천:

```text
- 일회성 감정
- 임시 농담
- 단기 일정
- 불확실한 추정
- 검증 전 후보안
- 민감정보
- Secret
- API Key
- Password
- Token
```

Memory Update 예시:

```json
{
  "type": "project_memory",
  "scope": "Personal AI Project",
  "key": "agent_memory_state_management_progress",
  "value": "Part01~Part06 작성 진행",
  "status": "active",
  "updatedAt": "2026-07-01",
  "source": "current_chat"
}
```

Memory Update는 품질을 높이지만 과도한 저장은 Retrieval 품질을 낮춘다.

---

### [FAQ]

Q. Memory Update가 뭐야?
A. 새로운 정보가 장기적으로 유용한지 판단하고 저장, 수정, 폐기하는 과정이다.

Q. 모든 새 정보를 Memory에 저장해?
A. 아니다. 반복 재사용 가치가 있는 정보만 저장한다.

Q. 저장 후보는 뭐야?
A. 프로젝트 목표, 기술 스택, 문서 규칙, Agent 구조, 사용자 선호, 확정 결정, 진행 상태 변화다.

Q. 저장하면 안 되는 것은?
A. API Key, 비밀번호, 토큰, 민감정보, 임시 농담, 불확실한 추정, 검증 전 후보안이다.

Q. Memory Update의 핵심은?
A. 장기적으로 유용하고 안전한 정보만 저장하는 것이다.

---

# 7. Memory Update Decision

## 7.1 저장 / 갱신 / 무시 / 만료 판단

### [개념]

Memory Update Decision은 새 정보를 저장할지, 기존 Memory를 갱신할지, 무시할지, 만료 처리할지 결정하는 기준이다.

```text
Memory Update Decision = Save / Update / Ignore / Deprecate 판단 기준
```

---

### [핵심]

Decision 유형:

- Save: 새 Memory로 저장
- Update: 기존 Memory를 최신 정보로 갱신
- Ignore: 장기 가치가 낮아 저장하지 않음
- Deprecate: 오래되거나 더 이상 유효하지 않은 Memory를 비활성화
- Archive: 참고용으로 보관하지만 active로 사용하지 않음
- Delete: 사용자가 잊어달라고 했거나 저장하면 안 되는 정보 제거

판단 기준:

- 장기 재사용 가치가 있는가?
- 현재 프로젝트 Scope와 관련 있는가?
- 사용자가 명시적으로 저장을 원했는가?
- 기존 Memory와 충돌하는가?
- 민감정보가 포함되어 있는가?
- 확정 정보인가 임시 정보인가?
- 현재 요청 이후에도 유용한가?

---

### [실무]

Save 예시:

```json
{
  "decision": "save",
  "reason": "사용자가 이 채팅을 RAG 문서 제작/검수 전용으로 지정",
  "memoryType": "user_preference_memory",
  "status": "active"
}
```

Update 예시:

```json
{
  "decision": "update",
  "oldMemory": "Agent Memory & State Management는 Planned",
  "newMemory": "Agent Memory & State Management Part01~Part06 작성 진행",
  "reason": "현재 진행 상태 변경"
}
```

Ignore 예시:

```json
{
  "decision": "ignore",
  "information": "오늘은 피곤하다",
  "reason": "장기 재사용 가치 낮음"
}
```

Deprecate 예시:

```json
{
  "decision": "deprecate",
  "oldMemory": "출력은 일반 Markdown",
  "reason": "현재 채팅에서는 writing block document 형식으로 변경"
}
```

Delete 예시:

```json
{
  "decision": "delete",
  "information": "API Key",
  "reason": "Secret 저장 금지"
}
```

---

### [FAQ]

Q. Memory Update Decision은 뭐야?
A. 새 정보를 저장, 갱신, 무시, 만료, 삭제할지 결정하는 기준이다.

Q. Save는 언제 해?
A. 장기 재사용 가치가 높고 현재 프로젝트 Scope와 관련 있으며 안전한 정보일 때 한다.

Q. Update는 언제 해?
A. 기존 Memory가 현재 정보와 달라져 최신 상태로 바꿔야 할 때 한다.

Q. Deprecate는 언제 해?
A. 과거에는 맞았지만 현재는 더 이상 active로 사용하면 안 되는 Memory에 적용한다.

Q. Delete는 언제 해?
A. 사용자가 잊어달라고 했거나 Secret, 민감정보처럼 저장하면 안 되는 정보에 적용한다.

---

# 8. Memory Validation Foundation

## 8.1 Memory Validation 기본 개념

### [개념]

Memory Validation은 검색되거나 저장될 Memory가 현재 작업에 안전하고 유효한지 검증하는 과정이다.

Memory는 시간이 지나면 틀릴 수 있고, 현재 요청과 충돌할 수 있다.

```text
Memory Validation = Memory 사용 또는 저장 전 유효성 검증
```

기본 Flow:

```text
Retrieved Memory
→ Relevance Check
→ Recency Check
→ Source Check
→ Conflict Check
→ Sensitivity Check
→ Use / Update / Ignore
```

---

### [핵심]

Memory Validation 필수 요소:

- Relevance Check
- Recency Check
- Source Check
- Conflict Check
- Sensitivity Check
- Confidence Check
- Current Request Priority
- User Correction Check
- Project Scope Check

Validation 결과:

- Use
- Use with Caution
- Update then Use
- Ignore
- Deprecate
- Delete
- Ask if High Risk

---

### [실무]

Memory Validation 예시:

```json
{
  "memory": "Agent 문서와 RAG 문서는 분리 관리",
  "relevance": "high",
  "recency": "valid",
  "source": "user_decision",
  "conflict": false,
  "sensitivity": "safe",
  "confidence": "high",
  "action": "use"
}
```

Memory Validation 예시:

```json
{
  "memory": "Agent Memory & State Management는 Planned",
  "relevance": "high",
  "recency": "outdated",
  "source": "old_project_progress",
  "conflict": true,
  "sensitivity": "safe",
  "confidence": "medium",
  "action": "update_then_use"
}
```

Memory Validation 없이 사용하면 오래된 진행 상태나 잘못된 결정이 현재 결과를 오염시킬 수 있다.

---

### [FAQ]

Q. Memory Validation이 뭐야?
A. 검색되거나 저장될 Memory가 현재 작업에 안전하고 유효한지 검증하는 과정이다.

Q. Memory Validation은 언제 해?
A. Memory를 사용하기 전, 저장하기 전, 갱신하기 전, 충돌이 의심될 때 수행한다.

Q. Memory Validation에서 무엇을 확인해?
A. 관련성, 최신성, 출처, 충돌 여부, 민감정보 여부, 신뢰도, 현재 요청 우선 여부를 확인한다.

Q. Validation 실패한 Memory는 어떻게 해?
A. 무시, 갱신, deprecated 처리, 삭제 중 하나를 선택한다.

Q. Memory Validation의 핵심은?
A. 오래되었거나 무관하거나 위험한 Memory를 현재 답변에 사용하지 않는 것이다.

---

# 9. Source Check

## 9.1 Memory 출처 검증

### [개념]

Source Check는 Memory가 어디서 온 정보인지 확인하는 과정이다.

Memory Source가 명확해야 신뢰도와 우선순위를 판단할 수 있다.

```text
Source Check = Memory 출처와 신뢰도 확인
```

---

### [핵심]

Memory Source 유형:

- Current User Request
- Explicit User Correction
- Latest Project Decision
- Project Progress
- Domain Rules
- Master Rules
- Recent Conversation
- Long-term Memory
- Tool Result
- External Source
- Inferred Summary

Source 우선순위:

```text
Current User Request
→ Explicit User Correction
→ Latest Project Decision
→ Master / Domain Rules
→ Project Progress
→ Recent Conversation
→ Long-term Memory
→ Tool Result
→ Inferred Summary
```

주의:

- 추정 Summary는 확정 사실로 사용하지 않는다.
- Tool Result는 실패 여부를 확인한다.
- 오래된 Project Progress는 현재 진행 상태와 비교한다.
- 사용자의 명시적 정정은 높은 우선순위를 가진다.

---

### [실무]

Source Check 예시:

```json
{
  "memory": "출력은 writing block document 형식",
  "source": "Current User Request",
  "priority": "highest",
  "confidence": "high",
  "action": "use"
}
```

Source Check 예시:

```json
{
  "memory": "Agent Memory & State Management는 Planned",
  "source": "Project Progress",
  "priority": "medium",
  "confidence": "medium",
  "currentConflict": "Part06 진행 중",
  "action": "update"
}
```

Source Check 예시:

```json
{
  "memory": "이전 출력 형식은 일반 Markdown",
  "source": "Long-term Memory",
  "priority": "low_when_conflicting",
  "currentConflict": "current request requires writing block",
  "action": "ignore_or_deprecate"
}
```

출처가 불명확한 Memory는 신뢰도를 낮게 둔다.

---

### [FAQ]

Q. Source Check가 뭐야?
A. Memory가 어디서 온 정보인지 확인해 신뢰도와 우선순위를 판단하는 과정이다.

Q. 가장 우선순위가 높은 Source는?
A. 현재 사용자 요청과 명시적 사용자 정정이다.

Q. Inferred Summary는 신뢰해도 돼?
A. 추정 요약은 확정 사실로 사용하지 않고 낮은 신뢰도로 다룬다.

Q. Tool Result도 Source Check가 필요해?
A. 필요하다. Tool 성공 여부, 최신성, 관련성을 확인해야 한다.

Q. Source가 불명확하면?
A. 신뢰도를 낮게 보고 현재 요청이나 최신 결정으로 검증한다.

---

# 10. Confidence Check

## 10.1 Memory 신뢰도 판단

### [개념]

Confidence Check는 Memory를 얼마나 확신하고 사용할 수 있는지 판단하는 과정이다.

Memory의 신뢰도는 출처, 최신성, 충돌 여부, 명확성에 따라 달라진다.

```text
Confidence Check = Memory 사용 신뢰도 판단
```

---

### [핵심]

Confidence 기준:

- High: 현재 요청, 명시적 정정, 최신 결정, 명확한 Domain Rule
- Medium: 최근 대화, Project Progress, 검증된 Summary
- Low: 오래된 Memory, 출처 불명확, 추정 정보, 충돌 가능 정보
- Invalid: 현재 요청과 충돌, 민감정보, 잘못 저장된 Memory

Confidence에 따른 처리:

| Confidence | 처리                        |
| ---------- | --------------------------- |
| High       | 사용                        |
| Medium     | 검증 후 사용                |
| Low        | 주의 또는 무시              |
| Invalid    | 사용 금지 / 업데이트 / 삭제 |

---

### [실무]

Confidence Check 예시:

```json
{
  "memory": "현재 출력은 writing block document",
  "source": "Current User Request",
  "recency": "current",
  "conflict": false,
  "confidence": "high",
  "action": "use"
}
```

Confidence Check 예시:

```json
{
  "memory": "Agent Memory 문서는 아직 Planned",
  "source": "Project Progress",
  "recency": "outdated",
  "conflict": true,
  "confidence": "low",
  "action": "do_not_use_as_current_fact"
}
```

Confidence Check 예시:

```json
{
  "memory": "사용자는 항상 짧은 답변을 선호",
  "source": "old_preference",
  "currentRequest": "상세 RAG 문서 작성",
  "conflict": true,
  "confidence": "invalid_for_current_task",
  "action": "ignore"
}
```

낮은 Confidence Memory는 단정 표현을 피한다.

---

### [FAQ]

Q. Confidence Check가 뭐야?
A. Memory를 얼마나 확신하고 사용할 수 있는지 판단하는 과정이다.

Q. High Confidence Memory는 뭐야?
A. 현재 요청, 명시적 정정, 최신 결정, 명확한 Domain Rule처럼 신뢰도가 높은 Memory다.

Q. Low Confidence Memory는 어떻게 처리해?
A. 검증하지 못하면 사용하지 않거나 주의해서 사용한다.

Q. Invalid Memory는 뭐야?
A. 현재 요청과 충돌하거나 민감정보이거나 잘못 저장된 Memory다.

Q. Confidence Check의 핵심은?
A. 불확실한 Memory를 확정 사실처럼 사용하지 않는 것이다.

---

# 11. Memory Use in State

## 11.1 검색된 Memory를 State에 반영하는 기준

### [개념]

Memory Use in State는 검증된 Memory를 현재 Workflow State에 어떻게 반영할지 정하는 기준이다.

Memory는 현재 작업을 보조하지만 State 전체를 대체하지 않는다.

```text
Memory Use in State = 검증된 Memory를 현재 State에 요약 반영하는 기준
```

---

### [핵심]

State 반영 대상:

- 현재 작업에 필요한 요구사항
- 출력 형식 제약
- 최신 프로젝트 결정
- Domain Rules 핵심
- 진행 상태 요약
- 관련 Decision
- 중요한 사용자 선호

State에 반영하지 않을 대상:

- 검색 결과 원문 전체
- 무관한 과거 정보
- 임시 Working Memory
- 오래된 Memory
- 충돌 해결 전 Memory
- 민감정보
- 낮은 Confidence Memory

반영 방식:

- requirements에 Merge
- constraints에 Merge
- decisions에 Versioned Update
- retrievedMemorySummary에 요약
- assumptions에 불확실 정보 기록
- reviewCriteria에 검증 기준 반영

---

### [실무]

좋은 State 반영 예시:

```json
{
  "requirements": [
    "MASTER_RAG_RULES 적용",
    "DOMAIN_RULES 적용",
    "FAQ 강화",
    "Retrieval Queries 포함"
  ],
  "constraints": [
    "writing block document 출력",
    "중간 응답 금지",
    "사람용 문서보다 RAG Retrieval 최적화 우선"
  ],
  "decisions": [
    {
      "decision": "Agent Memory & State Management는 총 8 Part 구성",
      "status": "active"
    }
  ],
  "retrievedMemorySummary": [
    "Part01~Part05 완료",
    "Part06은 Memory Retrieval, Update, Validation 중심"
  ]
}
```

나쁜 State 반영 예시:

```text
- 검색된 Memory 원문 전체를 State에 복사
- 오래된 Planned 상태를 현재 상태로 사용
- 충돌하는 선호를 둘 다 적용
- API Key를 State에 저장
```

Memory는 State에 직접 누적하지 않고 요약 반영한다.

---

### [FAQ]

Q. 검색된 Memory를 State에 어떻게 반영해?
A. 검증된 Memory 중 현재 작업에 필요한 핵심만 requirements, constraints, decisions, summary에 반영한다.

Q. Memory 원문 전체를 State에 넣어도 돼?
A. 아니다. Context가 커지고 무관한 정보가 섞일 수 있어 요약 반영해야 한다.

Q. 불확실한 Memory는 어디에 넣어?
A. 필요하면 assumptions에 낮은 확신 정보로 기록하고 단정하지 않는다.

Q. 충돌 Memory는 바로 State에 넣어?
A. 아니다. Conflict 해결 후 active 정보만 반영한다.

Q. Memory Use in State의 핵심은?
A. 검증된 Memory만 현재 작업 State를 보조하도록 요약 반영하는 것이다.

---

# 12. Common Mistakes

## 12.1 Memory Retrieval / Update / Validation 실수

### [개념]

Memory Retrieval, Update, Validation 실수는 오래된 정보 사용, 관련 없는 Memory 오염, 잘못된 장기 저장으로 이어진다.

Memory는 Agent 품질을 높이지만 잘못 쓰면 현재 작업 정확도를 떨어뜨린다.

---

### [핵심]

자주 발생하는 실수:

- 모든 Memory를 검색
- Memory Type을 구분하지 않음
- 검색된 Memory를 모두 사용
- Relevance Check 없이 사용
- Recency Check 없이 오래된 Memory 사용
- 현재 요청보다 Memory를 우선
- Tool Result 전체를 Memory로 저장
- Working Memory를 Long-term Memory로 저장
- 임시 아이디어를 Decision Memory로 저장
- 민감정보를 Memory에 저장
- Source Check 없이 신뢰
- Confidence가 낮은 Memory를 단정
- 충돌 Memory를 임의로 조합
- Memory Update를 과도하게 수행

---

### [실무]

문제:

```text
Agent가 오래된 Project Progress 기준으로 답변함
```

원인:

```text
Recency Check 없이 Project Memory 사용
```

해결:

```text
Project Progress 최신성 확인
→ 현재 요청과 충돌 여부 확인
→ 오래된 Memory는 update 또는 ignore
```

문제:

```text
현재 문서와 무관한 웹 프로젝트 내용이 답변에 섞임
```

원인:

```text
Memory Type Filtering과 Project Scope Filtering 누락
```

해결:

```text
현재 Scope를 Personal AI Project / RAG Document로 제한
→ 무관한 Project Memory 제외
```

문제:

```text
검토 전 후보안이 확정 결정처럼 저장됨
```

원인:

```text
Working Memory와 Decision Memory 혼동
```

해결:

```text
후보안은 Working Memory
→ 확정 후 Decision Memory
→ reason, status, date 기록
```

문제:

```text
사용자 선호보다 현재 요청이 더 구체적인데 과거 선호를 우선함
```

원인:

```text
Current Request Priority 미적용
```

해결:

```text
Current User Request 우선
→ User Preference Memory는 보조 기준으로만 사용
```

---

### [FAQ]

Q. Memory Retrieval에서 가장 흔한 실수는?
A. 모든 Memory를 검색하고 관련성 검증 없이 사용하는 것이다.

Q. Memory Update에서 가장 흔한 실수는?
A. 임시 정보나 검토 전 후보안을 Long-term Memory로 저장하는 것이다.

Q. Memory Validation에서 가장 흔한 실수는?
A. 오래된 Memory를 최신 사실처럼 사용하는 것이다.

Q. 현재 요청보다 Memory를 우선하면?
A. 사용자가 방금 요구한 형식이나 방향과 다른 결과가 나올 수 있다.

Q. 해결 핵심은?
A. 필요한 Memory만 검색하고, 검증 후 사용하며, 장기 가치가 있는 정보만 저장하는 것이다.

---

# 13. Troubleshooting

## 13.1 Memory Retrieval / Update / Validation 문제 해결

### [개념]

Troubleshooting은 Memory 검색, 저장, 검증 과정에서 발생하는 문제를 원인과 해결 기준으로 정리한다.

Memory 문제는 Retrieval 결과보다 먼저 Scope, Type, Recency, Conflict를 확인해야 한다.

---

### [핵심]

Troubleshooting 형식:

```md
문제:

원인:

해결:
```

주요 문제:

- 관련 없는 Memory 검색
- 필요한 Memory 검색 실패
- 오래된 Memory 사용
- Memory 충돌
- 잘못된 Memory 저장
- 민감정보 저장
- 낮은 Confidence Memory 사용
- Memory가 State를 오염

---

### [실무]

문제:

```text
관련 없는 Memory가 너무 많이 검색됨
```

원인:

```text
Retrieval Query가 너무 넓고 Memory Type Filter가 없음
```

해결:

```text
Project Scope 추가
→ Memory Type 명시
→ 핵심 Domain 용어 추가
→ Relevance Check 적용
```

문제:

```text
필요한 과거 결정이 검색되지 않음
```

원인:

```text
Decision Memory에 Query Matching 키워드나 FAQ 표현이 부족함
```

해결:

```text
Decision Memory에 decision, reason, scope, keyword, relatedDocument 추가
→ Retrieval Queries 강화
```

문제:

```text
오래된 Memory가 현재 답변에 반영됨
```

원인:

```text
updatedAt, status, Recency Check 누락
```

해결:

```text
Memory에 updatedAt과 status 추가
→ active / deprecated 구분
→ 현재 요청 기준 검증
```

문제:

```text
잘못된 Memory가 장기 저장됨
```

원인:

```text
Memory Update Decision 없이 자동 저장
```

해결:

```text
Save / Update / Ignore / Deprecate / Delete 기준 적용
→ 민감정보 검사
→ 확정 정보만 저장
```

문제:

```text
Memory가 현재 State를 오염시킴
```

원인:

```text
검색 결과 원문 전체를 State에 복사
```

해결:

```text
retrievedMemorySummary만 State에 반영
→ 무관한 Memory 제거
→ State Validation 수행
```

---

### [FAQ]

Q. 관련 없는 Memory가 많이 검색되면?
A. Query에 Project Scope, Memory Type, 핵심 Domain 용어를 추가하고 Relevance Check를 적용한다.

Q. 필요한 결정 Memory가 검색되지 않으면?
A. Decision Memory에 keyword, scope, reason, relatedDocument, FAQ 표현을 추가한다.

Q. 오래된 Memory가 답변에 섞이면?
A. updatedAt과 status를 확인하고 active / deprecated를 구분한다.

Q. 잘못 저장된 Memory는 어떻게 해?
A. Update, Deprecate, Delete 중 하나를 선택하고 같은 문제가 반복되지 않게 저장 기준을 강화한다.

Q. Memory가 State를 오염시키면?
A. 원문 전체 복사를 중단하고 필요한 요약만 State에 반영한다.

---

# 14. Best Practice

## 14.1 Memory Retrieval, Update, Validation 설계 원칙

### [개념]

좋은 Memory Management는 필요한 Memory만 검색하고, 검증된 Memory만 사용하며, 장기 가치가 있는 Memory만 저장한다.

Memory는 현재 요청을 보조하는 장치이지 현재 요청을 대체하는 기준이 아니다.

---

### [핵심]

Best Practice:

- 현재 사용자 요청을 먼저 분석한다.
- 필요한 Memory Type을 먼저 식별한다.
- Retrieval Query에 Project Scope와 Domain 용어를 포함한다.
- 검색된 Memory는 Relevance Check를 수행한다.
- 오래된 Memory는 Recency Check를 수행한다.
- Source와 Confidence를 확인한다.
- 현재 요청과 충돌하는 Memory는 사용하지 않는다.
- Memory는 현재 요청보다 우선하지 않는다.
- 검증된 Memory만 State에 요약 반영한다.
- 검색 결과 원문 전체를 State에 복사하지 않는다.
- Memory Update는 장기 재사용 가치 기준으로 수행한다.
- Working Memory를 Long-term Memory로 저장하지 않는다.
- Decision Memory에는 reason, date, scope, status를 포함한다.
- 민감정보와 Secret은 저장하지 않는다.
- 잘못된 Memory는 update, deprecate, delete 처리한다.

---

### [실무]

권장 Retrieval Flow:

```text
User Request Analysis
→ Project Scope Detection
→ Required Memory Type Detection
→ Retrieval Query Design
→ Memory Search
→ Relevance Check
→ Recency Check
→ Source Check
→ Conflict Check
→ Confidence Check
→ State Summary Injection
```

권장 Update Flow:

```text
New Information
→ Long-term Usefulness Check
→ Sensitivity Check
→ User Intent Check
→ Conflict Check
→ Save / Update / Ignore / Deprecate / Delete
```

권장 Validation Flow:

```text
Retrieved or New Memory
→ Relevance
→ Recency
→ Source
→ Conflict
→ Sensitivity
→ Confidence
→ Use Decision
```

권장 State 반영:

```json
{
  "retrievedMemorySummary": [],
  "activeRequirements": [],
  "activeConstraints": [],
  "activeDecisions": [],
  "assumptions": [],
  "ignoredMemoryReason": []
}
```

Memory Management의 최종 목표는 현재 작업 정확도와 장기 프로젝트 일관성을 동시에 유지하는 것이다.

---

### [FAQ]

Q. 좋은 Memory Retrieval 기준은?
A. 현재 요청에 필요한 Memory Type만 식별하고 관련성, 최신성, 출처, 충돌 여부를 검증하는 것이다.

Q. 좋은 Memory Update 기준은?
A. 장기 재사용 가치가 있고 안전하며 확정된 정보만 저장하거나 갱신하는 것이다.

Q. 좋은 Memory Validation 기준은?
A. 관련성, 최신성, 출처, 신뢰도, 충돌 여부, 민감정보 여부를 확인하는 것이다.

Q. Memory를 State에 반영할 때 핵심은?
A. 검증된 Memory의 핵심만 요약해 반영하고 원문 전체를 복사하지 않는 것이다.

Q. Memory Retrieval, Update, Validation의 최종 목표는?
A. 오래된 정보와 무관한 정보를 걸러내고 현재 작업에 필요한 기억만 안전하게 재사용하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Memory Retrieval이 뭐야?
A. 현재 요청을 처리하는 데 필요한 과거 정보만 검색하고 검증해 사용하는 과정이다.

Q. Memory Retrieval은 언제 해?
A. 현재 요청 처리에 프로젝트 맥락, 사용자 선호, 과거 결정, 진행 상태가 필요할 때 수행한다.

Q. 모든 Memory를 검색하면 안 되는 이유는?
A. 관련 없는 정보가 현재 답변에 섞이고 Context Window를 낭비하기 때문이다.

Q. Retrieval Query Design이 뭐야?
A. 필요한 Memory를 정확히 검색하기 위해 Query를 설계하는 기준이다.

Q. 좋은 Retrieval Query는 뭐야?
A. 현재 요청, 핵심 용어, Memory Type, 프로젝트 Scope, 사용자 표현을 포함하는 Query다.

Q. Memory Type Filtering이 뭐야?
A. 검색된 Memory를 유형별로 분류하고 현재 요청에 맞는 Memory만 사용하는 과정이다.

Q. Relevance Check가 뭐야?
A. 검색된 Memory가 현재 사용자 요청과 실제로 관련 있는지 확인하는 과정이다.

Q. Recency Check가 뭐야?
A. Memory가 현재도 유효한지 확인하는 최신성 검증 과정이다.

Q. 오래된 Memory는 어떻게 처리해?
A. 현재 요청과 최신 결정과 충돌하는지 확인하고 update, ignore, deprecate 중 하나를 적용한다.

Q. Memory Update가 뭐야?
A. 새로운 정보가 장기적으로 유용한지 판단하고 저장, 수정, 폐기하는 과정이다.

Q. Memory Update는 언제 해?
A. 장기 프로젝트 목표, 기술 스택, 문서 규칙, 사용자 선호, 확정 결정, 진행 상태가 바뀔 때 한다.

Q. Memory에 저장하면 안 되는 것은?
A. API Key, 비밀번호, 토큰, 민감정보, 임시 농담, 불확실한 추정, 검증 전 후보안이다.

Q. Memory Update Decision은 뭐야?
A. 새 정보를 저장, 갱신, 무시, 만료, 삭제할지 결정하는 기준이다.

Q. Save는 언제 해?
A. 장기 재사용 가치가 높고 현재 프로젝트 Scope와 관련 있으며 안전한 정보일 때 한다.

Q. Update는 언제 해?
A. 기존 Memory가 현재 정보와 달라져 최신 상태로 바꿔야 할 때 한다.

Q. Deprecate는 언제 해?
A. 과거에는 맞았지만 현재는 더 이상 active로 사용하면 안 되는 Memory에 적용한다.

Q. Delete는 언제 해?
A. 사용자가 잊어달라고 했거나 Secret, 민감정보처럼 저장하면 안 되는 정보에 적용한다.

Q. Memory Validation이 뭐야?
A. 검색되거나 저장될 Memory가 현재 작업에 안전하고 유효한지 검증하는 과정이다.

Q. Memory Validation에서 무엇을 확인해?
A. 관련성, 최신성, 출처, 충돌 여부, 민감정보 여부, 신뢰도, 현재 요청 우선 여부를 확인한다.

Q. Source Check가 뭐야?
A. Memory가 어디서 온 정보인지 확인해 신뢰도와 우선순위를 판단하는 과정이다.

Q. 가장 우선순위가 높은 Memory Source는?
A. 현재 사용자 요청과 명시적 사용자 정정이다.

Q. Confidence Check가 뭐야?
A. Memory를 얼마나 확신하고 사용할 수 있는지 판단하는 과정이다.

Q. Low Confidence Memory는 어떻게 처리해?
A. 검증하지 못하면 사용하지 않거나 주의해서 사용한다.

Q. 검색된 Memory를 State에 어떻게 반영해?
A. 검증된 Memory 중 현재 작업에 필요한 핵심만 requirements, constraints, decisions, summary에 반영한다.

Q. Memory 원문 전체를 State에 넣어도 돼?
A. 아니다. Context가 커지고 무관한 정보가 섞일 수 있어 요약 반영해야 한다.

Q. Memory Retrieval에서 가장 흔한 실수는?
A. 모든 Memory를 검색하고 관련성 검증 없이 사용하는 것이다.

Q. Memory Update에서 가장 흔한 실수는?
A. 임시 정보나 검토 전 후보안을 Long-term Memory로 저장하는 것이다.

Q. Memory Validation에서 가장 흔한 실수는?
A. 오래된 Memory를 최신 사실처럼 사용하는 것이다.

Q. 필요한 결정 Memory가 검색되지 않으면?
A. Decision Memory에 keyword, scope, reason, relatedDocument, FAQ 표현을 추가한다.

Q. 잘못 저장된 Memory는 어떻게 해?
A. Update, Deprecate, Delete 중 하나를 선택하고 같은 문제가 반복되지 않게 저장 기준을 강화한다.

Q. Memory Retrieval, Update, Validation의 최종 목표는?
A. 오래된 정보와 무관한 정보를 걸러내고 현재 작업에 필요한 기억만 안전하게 재사용하는 것이다.
