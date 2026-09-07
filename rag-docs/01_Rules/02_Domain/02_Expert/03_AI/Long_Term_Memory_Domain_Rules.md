# Long-Term Memory Domain Rules

---

# 1. Domain Purpose

## 1.1 Long-Term Memory 문서 목적

### [개념]

Long-Term Memory Domain 문서는 AI Agent / PM Agent / AI/ML Agent / Backend Agent / Review Agent가 장기 기억 기반 Agent 시스템을 설계, 구현, 검토, 개선할 때 참조하는 RAG 제작 규칙 문서이다.

Long-Term Memory는 Agent가 단일 대화나 단일 작업을 넘어서 사용자 선호, 프로젝트 규칙, 반복 작업 패턴, 장기 목표, 이전 결정 사항을 저장하고 재사용하는 구조이다.

Long-Term Memory는 단순 대화 기록 저장이 아니다.

Agent가 미래 작업에서 재사용할 가치가 있는 정보를 선별하고, 저장하고, 검색하고, 검증하고, 갱신하고, 삭제할 수 있어야 한다.

---

### [핵심]

- Long-Term Memory = 장기 저장 + 검색 + 재사용 + 갱신 + 검증
- 단순 Chat History와 구분 필요
- Short-Term Memory와 구분 필요
- Agent State와 구분 필요
- 저장 기준 필요
- 검색 기준 필요
- 갱신 기준 필요
- 삭제 기준 필요
- Privacy / Safety 기준 필요
- Memory Conflict 해결 기준 필요
- RAG 문서와 Memory 우선순위 필요
- Multi-Agent System과 연결 가능

---

### [실무]

2026 실무 기준 Long-Term Memory 문서는 다음 목적을 우선한다.

- Agent 장기 기억 설계
- 사용자 선호 저장 기준 제공
- 프로젝트 규칙 저장 기준 제공
- 반복 Workflow 재사용 기준 제공
- Memory Retrieval 전략 제공
- Memory Update 기준 제공
- Memory Deletion 기준 제공
- Memory Conflict 해결 기준 제공
- Memory Evaluation 기준 제공
- Privacy / Safety Guardrails 제공
- Multi-Agent Memory 공유 기준 제공

Long-Term Memory 문서는 사람이 기억 이론을 공부하기 위한 문서가 아니라, Agent가 장기적으로 유용한 정보를 안전하게 저장하고 재사용하도록 돕는 운영 지식 문서로 작성한다.

---

### [FAQ]

Q. Long-Term Memory 문서는 무엇을 위한 문서인가?

A. Agent가 장기적으로 재사용 가능한 정보를 저장, 검색, 갱신, 삭제할 수 있도록 기준을 제공하는 문서이다.

Q. Long-Term Memory는 Chat History와 같은가?

A. 아니다. Chat History는 대화 기록이고, Long-Term Memory는 미래 작업에 재사용할 가치가 있는 선별된 정보이다.

Q. Long-Term Memory의 핵심은 무엇인가?

A. 저장할 정보와 저장하지 말아야 할 정보를 구분하고, 필요한 시점에 안전하게 검색해 사용하는 것이다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Long-Term Memory Domain 문서는 Agent가 장기 기억을 안전하고 일관되게 사용하기 위한 개념, 저장 기준, 검색 전략, 갱신 기준, 삭제 기준, 검증 기준을 포함한다.

---

### [핵심]

포함 범위:

- Long-Term Memory
- Short-Term Memory
- Working Memory
- Agent State
- Chat History
- User Preference Memory
- Project Memory
- Semantic Memory
- Episodic Memory
- Procedural Memory
- Tool Result Memory
- Memory Extraction
- Memory Selection
- Memory Retrieval
- Memory Update
- Memory Deletion
- Memory Conflict Resolution
- Memory Freshness
- Memory Confidence
- Privacy Guardrails
- Safety Guardrails
- Multi-Agent Memory Sharing
- Memory Evaluation
- Memory Observability
- Memory Troubleshooting

제외 범위:

- 인간 뇌 과학 상세
- 심리학 중심 기억 이론
- 단순 대화 로그 저장소 설명
- Vector Database 설치 상세
- 특정 Memory Framework API 전체 문서
- 개인정보 수집 확대 전략
- 민감정보 저장 권장
- 무분별한 사용자 프로파일링

---

### [실무]

Long-Term Memory 문서는 아래 질문에 답할 수 있어야 한다.

- 어떤 정보를 장기 기억으로 저장해야 하는가?
- 어떤 정보는 저장하면 안 되는가?
- Memory와 RAG 문서가 충돌하면 무엇을 우선해야 하는가?
- Memory를 언제 검색해야 하는가?
- Memory를 어떻게 갱신해야 하는가?
- 오래된 Memory는 어떻게 처리해야 하는가?
- 사용자 선호는 어떻게 저장해야 하는가?
- 프로젝트 규칙은 어떻게 저장해야 하는가?
- Multi-Agent 구조에서 Memory를 어떻게 공유해야 하는가?
- Memory 사용으로 인한 Hallucination을 어떻게 줄일 것인가?

---

### [FAQ]

Q. Long-Term Memory 문서에 개인정보 저장 예시를 많이 넣어야 하는가?

A. 아니다. 저장 기준과 금지 기준을 명확히 작성하고, 민감정보 저장은 제한해야 한다.

Q. Long-Term Memory는 RAG 문서와 중복되는가?

A. 일부 연결되지만, RAG 문서는 지식 자료이고 Long-Term Memory는 사용자 / 프로젝트 / Workflow 맥락 저장소이다.

Q. Memory는 모든 Agent가 공유해야 하는가?

A. 아니다. 필요한 Agent만 최소 범위로 접근해야 한다.

---

# 3. Section Priority

## 3.1 필수 섹션 규칙

### [개념]

Long-Term Memory 문서는 모든 주요 Chunk에 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`를 우선 적용한다.

저장 판단이 필요한 주제는 `[Checklist]`를 추가한다.

흐름이 필요한 주제는 `[Flow]`를 추가한다.

위험이 있는 주제는 `[주의]`, `[Guardrails]`, `[Troubleshooting]`을 추가한다.

---

### [핵심]

Required:

- [개념]
- [핵심]
- [실무]
- [FAQ]

Strongly Recommended:

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Checklist]
- [Troubleshooting]
- [Comparison]

Optional:

- [Memory Schema]
- [Guardrails]
- [Review Point]
- [Evaluation]
- [Anti-Pattern]

---

### [실무]

Long-Term Memory 문서는 단순 설명보다 저장 / 검색 / 갱신 판단 기준을 우선한다.

각 문서는 아래 정보 중 최소 2개 이상을 포함한다.

- Memory 저장 기준
- Memory 저장 금지 기준
- Memory 검색 기준
- Memory 갱신 기준
- Memory 삭제 기준
- Memory Conflict 해결 기준
- Privacy Guardrails
- Review Checklist
- Evaluation 기준

---

### [FAQ]

Q. Long-Term Memory 문서에 Checklist가 필요한가?

A. 필요하다. Agent가 저장 여부, 검색 여부, 삭제 여부를 판단할 때 사용할 수 있기 때문이다.

Q. Long-Term Memory 문서에 Guardrails가 필요한 이유는?

A. Memory는 사용자 정보와 장기 맥락을 다루므로 Privacy와 Safety 위험을 통제해야 하기 때문이다.

Q. FAQ를 강화해야 하는 이유는?

A. 사용자의 자연어 질문과 Agent의 내부 검색 Query가 FAQ 형태와 잘 매칭되기 때문이다.

---

# 4. Core Concept Rules

## 4.1 Long-Term Memory 핵심 개념 작성 규칙

### [개념]

Long-Term Memory 핵심 개념은 Short-Term Memory, Agent State, Chat History, RAG Document와 구분되도록 작성한다.

Long-Term Memory는 장기적으로 재사용 가능한 정보를 저장하는 구조이다.

대화 중 나온 모든 정보를 저장하는 구조가 아니다.

---

### [핵심]

반드시 포함할 개념:

- Long-Term Memory
- Short-Term Memory
- Working Memory
- Agent State
- Chat History
- User Preference Memory
- Project Memory
- Semantic Memory
- Episodic Memory
- Procedural Memory
- Memory Extraction
- Memory Selection
- Memory Retrieval
- Memory Update
- Memory Deletion
- Memory Confidence
- Memory Freshness
- Privacy Guardrails

용어 통일:

- Long-Term Memory
- Short-Term Memory
- Agent State
- User Preference Memory
- Project Memory
- Semantic Memory
- Episodic Memory
- Procedural Memory
- Memory Retrieval
- Memory Update
- Memory Conflict
- Memory Freshness
- Memory Confidence

---

### [실무]

Long-Term Memory 설명은 아래 구분을 반드시 포함한다.

```text
Chat History
→ 대화 전체 기록

Agent State
→ 현재 작업을 수행하기 위한 임시 상태

Short-Term Memory
→ 현재 대화나 현재 Workflow 안에서 유지되는 정보

Long-Term Memory
→ 미래 작업에서 재사용할 가치가 있는 선별된 장기 정보

RAG Document
→ 외부 지식, 규칙, 기술 문서
```

Long-Term Memory 문서는 “기억한다” 수준에서 멈추면 안 된다.

Agent가 무엇을 저장하고, 언제 검색하고, 언제 갱신하고, 언제 삭제해야 하는지 판단할 수 있어야 한다.

---

### [FAQ]

Q. Long-Term Memory와 Agent State의 차이는?

A. Agent State는 현재 작업 상태이고, Long-Term Memory는 미래 작업에서 재사용할 장기 정보이다.

Q. Long-Term Memory와 RAG Document의 차이는?

A. RAG Document는 지식 자료이고, Long-Term Memory는 사용자 선호, 프로젝트 맥락, 반복 결정 같은 장기 맥락 정보이다.

Q. 모든 대화 내용을 Long-Term Memory로 저장해야 하는가?

A. 아니다. 장기적으로 유용하고 안전하며 재사용 가치가 있는 정보만 저장해야 한다.

---

# 5. Memory Type Rules

## 5.1 Memory 유형 작성 규칙

### [개념]

Memory Type은 저장되는 정보의 성격을 구분하는 기준이다.

Memory Type을 구분해야 저장 위치, 검색 방식, 갱신 기준, 공유 범위를 다르게 관리할 수 있다.

---

### [핵심]

대표 Memory Type:

- User Preference Memory
- Project Memory
- Semantic Memory
- Episodic Memory
- Procedural Memory
- Tool Result Memory
- Conversation Summary Memory
- Constraint Memory
- Decision Memory
- Feedback Memory

Memory Type별 의미:

- User Preference Memory: 출력 스타일, 선호 방식, 반복 요구사항
- Project Memory: 프로젝트 목표, 구조, 진행 상황, 기술 스택
- Semantic Memory: 일반화된 지식과 개념
- Episodic Memory: 과거 특정 작업 / 사건 요약
- Procedural Memory: 반복 Workflow, 작업 절차
- Tool Result Memory: 도구 실행 결과 중 재사용 가치가 있는 정보
- Decision Memory: 과거 확정 결정 사항
- Feedback Memory: 사용자의 수정 요청과 평가

---

### [실무]

Memory Type 예시:

```text
User Preference Memory:
- 사용자는 RAG 문서 출력 시 writing block 형식을 선호한다.

Project Memory:
- 개인 AI 프로젝트는 PM Agent, Backend Agent, Frontend Agent, Review Agent 구조를 목표로 한다.

Procedural Memory:
- RAG 문서 제작 시 초안 작성 → 검수 → 파일 간 연계 확인 → 치명적 문제 확인 → 최종 출력 순서를 따른다.

Decision Memory:
- Graph RAG Domain Rules는 AI Expert Level 문서로 분리한다.
```

Memory Type을 명확히 지정하면 Retrieval과 Review가 쉬워진다.

---

### [FAQ]

Q. Memory Type을 나누는 이유는?

A. 정보 성격에 따라 저장 기준, 검색 방식, 갱신 주기, 공유 범위가 달라지기 때문이다.

Q. User Preference Memory에는 무엇을 저장하는가?

A. 반복적으로 적용해야 하는 출력 형식, 선호 톤, 작업 방식, 금지 사항을 저장한다.

Q. Project Memory에는 무엇을 저장하는가?

A. 프로젝트 목표, 기술 스택, Agent 구조, 문서 진행 상황, 확정된 설계 결정을 저장한다.

---

# 6. Memory Selection Rules

## 6.1 저장 여부 판단 규칙

### [개념]

Memory Selection은 대화나 작업 결과 중 어떤 정보를 Long-Term Memory로 저장할지 판단하는 과정이다.

Long-Term Memory 품질은 많이 저장하는 것이 아니라 올바른 정보를 선별하는 것에서 결정된다.

---

### [핵심]

저장 적합 정보:

- 장기적으로 반복 사용될 사용자 선호
- 프로젝트 목표
- 확정된 기술 스택
- 반복 Workflow 규칙
- 출력 형식 규칙
- 문서 제작 규칙
- Agent 역할 정의
- 장기 결정 사항
- 반복된 피드백
- 명시적으로 저장 요청한 정보

저장 부적합 정보:

- 일회성 감정 표현
- 임시 숫자
- 검증되지 않은 추측
- 오래 유지되지 않을 정보
- 민감정보
- 개인정보 과다
- 사용자가 저장을 원하지 않는 정보
- 맥락 없이 단독으로 의미 없는 정보
- 이미 RAG 문서에 있는 일반 지식

---

### [실무]

Memory Selection Checklist:

```md
### [Checklist]

- 미래 작업에서 반복 사용될 정보인가?
- 사용자가 명시적으로 저장을 요청했는가?
- 프로젝트나 Workflow 품질에 영향을 주는가?
- 시간이 지나도 유효할 가능성이 높은가?
- 민감정보가 아닌가?
- RAG 문서가 아니라 Memory에 저장해야 하는 정보인가?
- 중복 Memory가 아닌가?
- 저장 후 사용자에게 불쾌감을 줄 수 있는 정보가 아닌가?
```

Memory는 “많이 저장”보다 “정확히 저장”을 우선한다.

---

### [FAQ]

Q. 어떤 정보를 Long-Term Memory에 저장해야 하는가?

A. 장기적으로 반복 사용될 사용자 선호, 프로젝트 규칙, 확정 결정, 반복 Workflow를 저장한다.

Q. 저장하지 말아야 할 정보는?

A. 일회성 정보, 검증되지 않은 추측, 민감정보, 오래 유지되지 않을 정보, 일반 지식은 저장하지 않는다.

Q. 사용자가 명시적으로 기억하라고 하면 저장해야 하는가?

A. 저장 가능 범위라면 저장해야 하며, 민감하거나 위험한 정보는 안전 기준을 따른다.

---

# 7. Memory Extraction Rules

## 7.1 Memory Extraction 작성 규칙

### [개념]

Memory Extraction은 대화, 문서, 도구 결과, Agent 출력에서 장기 기억 후보를 추출하는 과정이다.

Memory Extraction은 원문 전체 저장이 아니라 핵심 사실을 구조화하는 작업이다.

---

### [핵심]

Memory Extraction 기준:

- 짧고 명확한 문장으로 추출
- 하나의 Memory에는 하나의 사실만 포함
- 출처나 맥락이 필요한 경우 함께 저장
- 추측을 사실처럼 저장하지 않음
- 시간 기준이 필요한 경우 날짜 포함
- 사용자 선호와 프로젝트 사실 구분
- 민감정보 여부 확인
- 중복 여부 확인

Memory 문장 형식:

```text
User prefers ...
User wants ...
Project uses ...
Project goal is ...
Workflow rule is ...
Decision made: ...
Do not ...
```

한국어 문서에서는 아래 형식도 허용한다.

```text
사용자는 ...
프로젝트는 ...
작업 규칙은 ...
확정 결정은 ...
금지 사항은 ...
```

---

### [실무]

좋은 Memory Extraction 예시:

```text
사용자는 RAG 문서 제작 시 반드시 writing block 형식을 유지하기를 원한다.
```

나쁜 Memory Extraction 예시:

```text
사용자는 꼼꼼한 걸 좋아하고 AI 프로젝트를 많이 한다.
```

좋은 예시는 구체적이고 재사용 가능하다.

나쁜 예시는 추측이 섞이고 범위가 넓다.

---

### [FAQ]

Q. Memory Extraction은 원문을 그대로 저장하는 것인가?

A. 아니다. 장기적으로 유용한 핵심 사실을 짧고 명확하게 구조화하는 것이다.

Q. 하나의 Memory에 여러 사실을 넣어도 되는가?

A. 권장하지 않는다. 하나의 Memory에는 하나의 핵심 사실만 넣는 것이 검색과 갱신에 유리하다.

Q. 추측도 Memory로 저장해도 되는가?

A. 아니다. 사용자가 명시했거나 충분히 확인된 정보만 저장한다.

---

# 8. Memory Schema Rules

## 8.1 Memory Schema 작성 규칙

### [개념]

Memory Schema는 Long-Term Memory를 저장할 때 사용할 구조를 정의하는 규칙이다.

Memory Schema가 명확해야 검색, 갱신, 삭제, 충돌 해결, 감사가 가능하다.

---

### [핵심]

권장 Memory Schema 필드:

- memoryId
- memoryType
- content
- subject
- scope
- source
- createdAt
- updatedAt
- lastUsedAt
- confidence
- freshness
- sensitivity
- owner
- visibility
- relatedProject
- tags
- status

필드 의미:

- memoryType: User Preference, Project, Procedure, Decision 등
- content: 저장된 핵심 내용
- subject: Memory 대상
- scope: 적용 범위
- source: Memory 생성 근거
- confidence: 확신도
- freshness: 최신성
- sensitivity: 민감도
- visibility: 공유 가능 범위
- status: active, outdated, archived, deleted

---

### [실무]

Memory Schema 예시:

```text
memoryType:
- User Preference Memory

content:
- 사용자는 RAG 문서 출력 시 writing block 형식을 유지하기를 원한다.

scope:
- RAG document generation

confidence:
- high

freshness:
- current

sensitivity:
- low

status:
- active
```

초기 시스템에서는 모든 필드를 복잡하게 구현하지 않아도 된다.

하지만 memoryType, content, scope, confidence, status는 최소 기준으로 권장한다.

---

### [FAQ]

Q. Memory Schema는 왜 필요한가?

A. Memory를 검색, 갱신, 삭제, 충돌 해결하기 위해 구조화된 필드가 필요하기 때문이다.

Q. confidence는 왜 필요한가?

A. Memory가 명시된 사실인지 추론된 정보인지 구분하고 사용 우선순위를 정하기 위해 필요하다.

Q. status 필드는 왜 필요한가?

A. 오래된 Memory를 active, outdated, archived, deleted로 관리하기 위해 필요하다.

---

# 9. Memory Retrieval Rules

## 9.1 Memory Retrieval 작성 규칙

### [개념]

Memory Retrieval은 현재 사용자 요청이나 Agent 작업에 필요한 Long-Term Memory를 검색하는 과정이다.

Memory Retrieval은 항상 수행하는 것이 아니라, 현재 작업에 Memory가 의미 있게 영향을 줄 때 수행한다.

---

### [핵심]

Memory Retrieval 필요 상황:

- 사용자가 이전 선호를 언급
- 프로젝트 맥락이 필요한 요청
- 반복 Workflow 수행
- 이전 결정 사항 확인
- 출력 형식 유지 필요
- Agent 역할 / 구조 참고 필요
- 장기 목표와 연결된 요청
- 이전 피드백 반영 필요

Memory Retrieval 불필요 상황:

- 단순 일반 지식 질문
- 일회성 번역
- 제공된 문서만으로 충분한 작업
- 사용자 맥락이 필요 없는 계산
- 민감정보 추정이 필요한 상황

---

### [실무]

Memory Retrieval Flow:

```text
User Request
→ Memory Need Check
→ Query Memory
→ Filter by Scope
→ Filter by Freshness
→ Filter by Sensitivity
→ Select Relevant Memory
→ Apply to Task
→ Validate Against Current Request
```

Memory는 현재 요청보다 우선하지 않는다.

사용자가 현재 요청에서 기존 Memory와 다른 지시를 하면 현재 요청을 우선한다.

---

### [FAQ]

Q. Memory Retrieval은 언제 해야 하는가?

A. 사용자 선호, 프로젝트 맥락, 이전 결정, 반복 Workflow가 현재 작업에 영향을 줄 때 수행한다.

Q. 모든 요청에서 Memory를 검색해야 하는가?

A. 아니다. Memory가 답변 품질에 의미 있게 영향을 줄 때 검색한다.

Q. 현재 사용자 지시와 Memory가 충돌하면 무엇을 우선하는가?

A. 현재 사용자 지시를 우선하고, 필요한 경우 Memory Update 후보로 검토한다.

---

# 10. Memory Update Rules

## 10.1 Memory Update 작성 규칙

### [개념]

Memory Update는 기존 Long-Term Memory가 변경되었거나 더 정확한 정보가 생겼을 때 Memory를 갱신하는 과정이다.

Memory는 한 번 저장하면 끝나는 정적 정보가 아니다.

---

### [핵심]

Memory Update 필요 상황:

- 사용자가 선호를 변경
- 프로젝트 목표 변경
- 기술 스택 변경
- Agent 구조 변경
- 기존 결정 취소
- 이전 Memory가 부정확함
- 더 최신 정보 확인
- 사용자가 정정 요청
- 반복 피드백으로 규칙 변경

Update 방식:

- 기존 Memory 수정
- 기존 Memory outdated 처리
- 새 Memory 추가
- 관련 Memory 병합
- 충돌 Memory 정리
- confidence 갱신
- updatedAt 갱신

---

### [실무]

Memory Update 예시:

```text
기존 Memory:
- 사용자는 RAG 문서에 코드블록 id를 허용한다.

새 지시:
- 코드블록 id="" 제거

Update:
- 기존 Memory를 outdated 처리
- 새 Memory 저장: 사용자는 RAG 문서 코드블록에 id 속성을 넣지 않기를 원한다.
```

Memory Update는 기존 Memory와 새 지시의 충돌을 명확히 처리해야 한다.

---

### [FAQ]

Q. Memory Update는 언제 필요한가?

A. 사용자 선호, 프로젝트 규칙, 기술 스택, 이전 결정이 변경되었을 때 필요하다.

Q. 기존 Memory를 무조건 삭제해야 하는가?

A. 아니다. 변경 이력 관리가 필요하면 outdated 또는 archived 상태로 전환할 수 있다.

Q. 사용자가 정정하면 무엇을 우선하는가?

A. 사용자의 최신 정정을 우선하고 기존 Memory를 갱신한다.

---

# 11. Memory Deletion Rules

## 11.1 Memory Deletion 작성 규칙

### [개념]

Memory Deletion은 사용자가 삭제를 요청하거나, 더 이상 저장하면 안 되는 정보가 된 Memory를 제거하거나 비활성화하는 과정이다.

Long-Term Memory는 저장만큼 삭제가 중요하다.

---

### [핵심]

삭제 필요 상황:

- 사용자가 명시적으로 삭제 요청
- Memory가 부정확함
- Memory가 오래되어 더 이상 유효하지 않음
- 민감정보가 포함됨
- 저장 목적이 사라짐
- 중복 Memory가 많음
- 사용자에게 불리하거나 불쾌감을 줄 수 있음
- 정책상 저장하면 안 되는 정보임

삭제 방식:

- hard delete
- soft delete
- archive
- outdated 처리
- sensitivity escalation
- access 제한

---

### [실무]

Deletion Flow:

```text
Deletion Request
→ Identify Target Memory
→ Check Scope
→ Delete or Archive
→ Remove from Retrieval
→ Confirm Deletion
```

사용자가 “잊어줘”, “기억하지 마”, “삭제해줘”라고 요청하면 해당 Memory를 검색하고 제거해야 한다.

삭제 요청은 임의로 무시하지 않는다.

---

### [FAQ]

Q. Memory Deletion은 왜 중요한가?

A. 오래되거나 부정확하거나 사용자가 원하지 않는 Memory가 계속 사용되면 신뢰와 안전성이 떨어지기 때문이다.

Q. 사용자가 기억을 삭제하라고 하면 어떻게 해야 하는가?

A. 대상 Memory를 확인하고 삭제 또는 비활성화해야 한다.

Q. 오래된 Memory는 무조건 삭제해야 하는가?

A. 아니다. 필요하면 outdated 또는 archived 상태로 전환할 수 있다.

---

# 12. Memory Conflict Rules

## 12.1 Memory Conflict 해결 규칙

### [개념]

Memory Conflict는 서로 다른 Memory, 현재 사용자 지시, RAG 문서, Project Progress가 서로 충돌하는 상황이다.

Long-Term Memory는 항상 최신이 아닐 수 있으므로 충돌 해결 기준이 필요하다.

---

### [핵심]

우선순위:

```text
Current User Request
→ System / Master Rules
→ Project Progress
→ Domain Rules
→ Explicit Recent Memory
→ Older Memory
→ Inferred Memory
```

Conflict 유형:

- 현재 지시와 과거 Memory 충돌
- Project Progress와 Memory 충돌
- Domain Rules와 Memory 충돌
- 두 Memory 간 충돌
- 사용자 선호와 안전 기준 충돌
- 최신 정보와 오래된 Memory 충돌

해결 방식:

- 최신 명시 지시 우선
- 공식 문서 우선
- Domain Rules 우선
- 오래된 Memory outdated 처리
- 불확실성 표시
- 필요 시 사용자 확인
- 안전 기준 우선

---

### [실무]

Memory Conflict 예시:

```text
기존 Memory:
- 사용자는 RAG 문서에 중간 응답을 허용한다.

현재 지시:
- 중간 응답 금지

해결:
- 현재 지시 우선
- 기존 Memory outdated 처리
- 새 출력 규칙 적용
```

Memory Conflict는 조용히 무시하지 않는다.

Agent 내부적으로 어떤 기준이 우선인지 명확히 해야 한다.

---

### [FAQ]

Q. Memory와 현재 사용자 요청이 충돌하면 무엇을 우선하는가?

A. 현재 사용자 요청을 우선한다.

Q. Memory와 Domain Rules가 충돌하면 무엇을 우선하는가?

A. Domain Rules를 우선한다.

Q. 오래된 Memory는 어떻게 처리하는가?

A. outdated 처리하거나 최신 지시에 맞게 갱신한다.

---

# 13. Memory Freshness Rules

## 13.1 Memory Freshness 작성 규칙

### [개념]

Memory Freshness는 Memory가 현재에도 유효한지 판단하는 기준이다.

Long-Term Memory는 시간이 지나면 오래되거나 잘못될 수 있다.

---

### [핵심]

Freshness 확인 대상:

- 프로젝트 진행 상황
- 기술 스택
- 도구 버전
- Agent 구조
- 출력 형식
- 사용자 선호
- 배포 환경
- 파일 구조
- 정책 / 규칙
- 일정 / 계획

Freshness 상태:

- current
- likely_current
- uncertain
- outdated
- deprecated

Freshness 판단 기준:

- 생성일
- 최근 사용일
- 최근 사용자 지시
- Project Progress와 일치 여부
- Domain Rules와 일치 여부
- 변경 가능성
- 외부 최신성 필요 여부

---

### [실무]

Freshness Handling 예시:

```text
Memory:
- 현재 AI Stack은 AnythingLLM + Ollama + Qwen2.5 + BGE-M3이다.

Freshness Check:
- 프로젝트 진행 문서와 일치하면 current
- 최근 변경 언급이 있으면 update 필요
- 오래된 플랫폼 정보와 충돌하면 Project Progress 우선
```

최신성이 중요한 Memory는 사용 전 검증한다.

특히 도구 버전, API 정책, 외부 서비스 가격, 법률, 일정은 Memory만으로 단정하지 않는다.

---

### [FAQ]

Q. Memory Freshness는 왜 필요한가?

A. 오래된 Memory가 현재 상황과 다르면 잘못된 답변이나 작업을 유발할 수 있기 때문이다.

Q. Freshness가 uncertain이면 어떻게 해야 하는가?

A. 최신 문서, 현재 사용자 요청, Project Progress를 확인하고 필요하면 불확실성을 표시한다.

Q. 사용자 선호도 Freshness가 필요한가?

A. 필요하다. 사용자가 출력 형식이나 작업 방식을 바꿀 수 있기 때문이다.

---

# 14. Privacy and Safety Rules

## 14.1 Privacy / Safety Guardrails 작성 규칙

### [개념]

Privacy and Safety Guardrails는 Long-Term Memory가 사용자 정보와 장기 맥락을 다룰 때 안전하게 저장, 검색, 공유되도록 제한하는 규칙이다.

Memory는 개인화에 유용하지만, 과도하게 저장하면 Privacy 위험이 커진다.

---

### [핵심]

주의 대상:

- 민감정보
- 건강 정보
- 정치 성향
- 종교
- 인종 / 민족
- 성적 지향
- 정밀 위치
- 금융 정보
- 신분증 / 인증 정보
- 비밀번호 / API Key
- 개인 연락처
- 범죄 기록
- 사적인 가족 정보
- 불필요한 개인 프로파일링

안전 기준:

- 최소 저장
- 명시적 요청 우선
- 민감정보 저장 제한
- 불필요한 추론 금지
- 사용자에게 불쾌한 프로파일링 금지
- 접근 범위 제한
- 삭제 요청 존중
- 보안 정보 저장 금지

---

### [실무]

저장 금지 예시:

```text
- 사용자의 비밀번호
- API Key
- 주민등록번호
- 상세 주소
- 건강 진단 정보
- 정치 성향
- 종교 정체성
- 민감한 가족사
```

저장 가능 예시:

```text
- 사용자는 RAG 문서 출력 형식을 writing block으로 원한다.
- 사용자는 개인 AI 프로젝트에서 PM Agent 중심 구조를 목표로 한다.
- 사용자는 코드 설명을 초보자도 이해할 수 있게 원한다.
```

Memory는 개인화보다 안전성을 우선한다.

---

### [FAQ]

Q. Long-Term Memory에서 가장 조심해야 하는 것은?

A. 민감정보, 인증정보, 불필요한 개인 프로파일링, 오래된 정보의 자동 사용이다.

Q. API Key나 비밀번호를 Memory에 저장해도 되는가?

A. 안 된다. 보안 인증 정보는 Long-Term Memory에 저장하지 않는다.

Q. 사용자가 명시적으로 저장하라고 하면 민감정보도 저장해도 되는가?

A. 정책과 안전 기준에 따라 제한해야 하며, 위험한 정보는 저장하지 않는 것이 원칙이다.

---

# 15. Multi-Agent Memory Sharing Rules

## 15.1 Multi-Agent Memory 공유 규칙

### [개념]

Multi-Agent Memory Sharing은 여러 Agent가 Long-Term Memory를 사용할 때 접근 범위, 공유 기준, 충돌 해결, 갱신 권한을 관리하는 규칙이다.

모든 Agent가 모든 Memory에 접근하면 Context Noise와 Privacy 위험이 증가한다.

---

### [핵심]

Agent별 Memory 사용 기준:

- PM Agent: Project Memory, User Preference Memory, Decision Memory
- Backend Agent: Project Memory, Technical Decision Memory, Coding Rule Memory
- Frontend Agent: UI Preference Memory, API Contract Memory, Project Memory
- DevOps Agent: Environment Memory, Deployment Decision Memory
- AI/ML Agent: Agent Workflow Memory, RAG Rule Memory, Evaluation Memory
- Review Agent: Domain Rules, Decision Memory, User Preference Memory, Common Mistake Memory

공유 기준:

- 역할에 필요한 Memory만 제공
- 민감정보 최소화
- Shared Memory와 Agent Local Memory 구분
- Memory Update 권한 제한
- 충돌 시 PM Agent 또는 Review Agent 검토
- Final Output에 불필요한 Memory 노출 금지

---

### [실무]

Multi-Agent Memory Flow:

```text
User Request
→ PM Agent Memory Retrieval
→ Relevant Memory Selection
→ Specialist Agent에 최소 Memory 전달
→ Specialist Agent Output
→ Review Agent Memory Conflict 검토
→ 필요 시 Memory Update 후보 생성
```

Specialist Agent에게 전체 Memory를 전달하지 않는다.

작업 수행에 필요한 Memory만 전달한다.

---

### [FAQ]

Q. 모든 Agent가 모든 Memory를 공유해야 하는가?

A. 아니다. 역할에 필요한 최소 Memory만 공유해야 한다.

Q. Memory Update 권한은 모든 Agent에게 있어야 하는가?

A. 권장하지 않는다. PM Agent 또는 Memory Manager Agent가 갱신을 조율하는 것이 좋다.

Q. Review Agent는 Memory를 어떻게 사용해야 하는가?

A. 출력이 사용자 선호, 프로젝트 결정, Domain Rules와 충돌하지 않는지 검토하는 데 사용한다.

---

# 16. Memory Integration with RAG Rules

## 16.1 RAG와 Memory 연계 규칙

### [개념]

Long-Term Memory는 RAG 문서와 함께 Agent Context를 구성하는 보조 정보이다.

RAG 문서는 기술 지식과 규칙을 제공하고, Long-Term Memory는 사용자 선호와 프로젝트 맥락을 제공한다.

---

### [핵심]

RAG와 Memory 역할 구분:

- RAG Document: 기술 지식, Domain Rules, 코드 패턴, Best Practice
- Project Progress: 진행 상황, 문서 Registry, Agent Roadmap
- Long-Term Memory: 사용자 선호, 장기 프로젝트 맥락, 반복 결정
- Agent State: 현재 작업 상태
- Tool Result: 현재 실행 결과

Context 우선순위:

```text
System Instructions
→ Current User Request
→ Master RAG Rules
→ Domain Rules
→ Project Progress
→ Relevant Long-Term Memory
→ Retrieved RAG Context
→ Tool Result
```

---

### [실무]

RAG + Memory 사용 예시:

```text
요청:
다음 Domain Rules 작성

RAG 검색:
- Master RAG Rules
- Project Progress
- 기존 Domain Rules

Memory 검색:
- 사용자의 출력 형식 선호
- 코드블록 id 제거 규칙
- 중간 응답 금지 규칙

출력:
- writing block 형식의 Domain Rules 문서
```

Memory는 RAG 근거를 대체하지 않는다.

기술 판단은 Domain Rules와 RAG 문서를 우선한다.

---

### [FAQ]

Q. Long-Term Memory가 RAG 문서를 대체하는가?

A. 아니다. Memory는 사용자 / 프로젝트 맥락을 제공하고, 기술 지식은 RAG 문서를 우선한다.

Q. RAG 문서와 Memory가 충돌하면 무엇을 우선하는가?

A. Domain Rules, Project Progress, 현재 사용자 요청을 우선한다.

Q. Memory는 Context에 항상 포함해야 하는가?

A. 아니다. 현재 작업에 필요한 Memory만 선택해 포함해야 한다.

---

# 17. Memory Evaluation Rules

## 17.1 Long-Term Memory Evaluation 작성 규칙

### [개념]

Long-Term Memory Evaluation은 Memory가 정확하고, 유용하고, 안전하고, 최신이며, 현재 작업에 적절히 사용되었는지 평가하는 기준이다.

Memory 품질은 Agent 개인화 품질과 안전성에 직접 영향을 준다.

---

### [핵심]

평가 항목:

- Memory Accuracy
- Memory Relevance
- Memory Usefulness
- Memory Freshness
- Memory Safety
- Memory Specificity
- Memory Deduplication
- Memory Retrieval Precision
- Memory Retrieval Recall
- Memory Conflict Handling
- Memory Update Quality
- Memory Deletion Compliance
- User Preference Alignment
- Project Context Alignment

---

### [실무]

Memory Evaluation Checklist:

```md
### [Checklist]

- Memory가 사실에 기반하는가?
- Memory가 장기적으로 재사용 가능한가?
- Memory가 너무 일반적이지 않은가?
- Memory에 민감정보가 포함되지 않았는가?
- Memory가 최신 상태인가?
- 현재 요청과 관련 있는 Memory만 사용했는가?
- 오래된 Memory를 우선하지 않았는가?
- 충돌 Memory를 감지했는가?
- 사용자의 최신 지시를 우선했는가?
- 삭제 요청을 반영했는가?
```

Memory 평가는 저장 단계와 사용 단계 모두에서 수행한다.

---

### [FAQ]

Q. Long-Term Memory 평가는 왜 필요한가?

A. 부정확하거나 오래되거나 불필요한 Memory가 Agent 답변 품질과 안전성을 떨어뜨리기 때문이다.

Q. Memory Retrieval Precision이란?

A. 현재 작업과 실제로 관련 있는 Memory를 정확히 검색하는 정도이다.

Q. Memory Safety는 무엇을 평가하는가?

A. 민감정보, 불필요한 프로파일링, 보안 정보 저장, 삭제 요청 미반영 여부를 평가한다.

---

# 18. Memory Observability Rules

## 18.1 Memory Observability 작성 규칙

### [개념]

Memory Observability는 Long-Term Memory의 생성, 검색, 사용, 갱신, 삭제 과정을 추적하는 구조이다.

Memory가 Agent 답변에 영향을 주기 때문에 어떤 Memory가 언제 사용되었는지 추적 가능해야 한다.

---

### [핵심]

관측 대상:

- memoryId
- memoryType
- createdAt
- updatedAt
- lastUsedAt
- source
- retrievalQuery
- useCase
- agentName
- confidence
- freshness
- conflictDetected
- updateReason
- deletionReason
- finalOutputImpact

Observability 목적:

- 잘못된 Memory 추적
- 오래된 Memory 탐지
- 불필요한 Memory 제거
- Memory Retrieval 품질 개선
- Privacy Risk 점검
- Agent 답변 근거 추적

---

### [실무]

Memory Trace 예시:

```text
memoryId: MEM-001
memoryType: User Preference Memory
agentName: PM Agent
retrievalQuery: RAG document output format
useCase: Domain Rules generation
freshness: current
confidence: high
finalOutputImpact: Applied writing block format
```

Memory Observability는 Agent 내부 품질 개선과 사용자 신뢰 확보에 중요하다.

단, 민감정보를 로그에 과도하게 남기지 않는다.

---

### [FAQ]

Q. Memory Observability는 왜 필요한가?

A. 어떤 Memory가 답변에 영향을 주었는지 추적하고, 잘못된 Memory 사용을 수정하기 위해 필요하다.

Q. 모든 Memory 사용을 기록해야 하는가?

A. 운영 품질을 위해 주요 Memory 사용은 기록하되, 민감정보 로그는 최소화해야 한다.

Q. finalOutputImpact는 무엇인가?

A. 특정 Memory가 최종 출력에 어떤 영향을 주었는지 요약한 정보이다.

---

# 19. Troubleshooting Rules

## 19.1 Long-Term Memory 장애 대응 작성 규칙

### [개념]

Long-Term Memory Troubleshooting 문서는 Memory 저장, 검색, 갱신, 삭제, 충돌 해결 과정에서 발생하는 문제를 해결하기 위한 규칙이다.

---

### [핵심]

자주 발생하는 문제:

- 불필요한 Memory 과다 저장
- Memory Retrieval 실패
- 관련 없는 Memory 사용
- 오래된 Memory 사용
- Memory Conflict 미감지
- 민감정보 저장
- 중복 Memory 증가
- 사용자의 최신 지시 무시
- RAG 문서보다 Memory를 우선
- 삭제 요청 미반영
- Agent 간 Memory 공유 과다
- Memory로 인한 Hallucination

---

### [실무]

Troubleshooting 형식:

```md
문제:
Agent가 오래된 출력 형식을 계속 사용함

원인:

- 기존 User Preference Memory가 outdated 처리되지 않음
- 최신 사용자 지시가 Memory Update에 반영되지 않음
- Memory Retrieval 시 freshness 필터가 없음

해결:

- 기존 Memory를 outdated 처리
- 최신 출력 형식 Memory 저장
- Memory Retrieval 시 freshness=current 우선
- Review Agent가 출력 형식 검증
```

장애 대응 문서는 문제 / 원인 / 해결 형식을 기본으로 한다.

---

### [FAQ]

Q. Long-Term Memory에서 가장 흔한 실패는?

A. 불필요한 저장, 오래된 Memory 사용, Memory Conflict 미감지, 민감정보 저장, 삭제 요청 미반영이다.

Q. 관련 없는 Memory가 답변에 반영되면 어떻게 해야 하는가?

A. Memory Retrieval Query, scope, freshness, relevance filter를 개선해야 한다.

Q. Memory 때문에 Hallucination이 발생하면 어떻게 해야 하는가?

A. Memory confidence를 낮추고, RAG 근거와 현재 사용자 요청을 우선하도록 조정한다.

---

# 20. Common Mistakes

## 20.1 자주 발생하는 작성 오류

### [개념]

Long-Term Memory 문서는 “사용자 정보를 많이 저장하는 방법”을 설명하는 문서가 아니다.

Agent가 장기적으로 필요한 정보를 안전하게 선별하고, 필요한 시점에만 검색하고, 오래된 정보를 갱신하거나 삭제하도록 돕는 기준 문서이다.

---

### [핵심]

금지 또는 주의:

- 모든 대화 내용을 Memory로 저장
- Chat History와 Long-Term Memory 혼동
- Agent State와 Long-Term Memory 혼동
- RAG Document와 Memory 혼동
- 저장 기준 누락
- 저장 금지 기준 누락
- 민감정보 저장 권장
- 사용자 추측 프로파일링
- Memory Update 기준 누락
- Memory Deletion 기준 누락
- Memory Conflict 기준 누락
- Freshness 기준 누락
- Multi-Agent 공유 범위 누락
- Evaluation Checklist 누락
- Troubleshooting 누락
- 장문 이론 설명 중심 작성
- Retrieval Queries 누락

---

### [실무]

나쁜 문서 예시:

```text
Long-Term Memory는 사용자의 모든 대화를 저장해서 더 개인화된 답변을 제공하는 기능이다.
```

좋은 문서 예시:

```text
Long-Term Memory는 미래 작업에서 재사용할 가치가 있는 사용자 선호, 프로젝트 규칙, 반복 Workflow, 확정 결정을 선별 저장하고, 필요할 때 검색해 현재 요청에 적용하는 구조이다.

Flow:
Conversation
→ Memory Candidate Extraction
→ Safety Check
→ Store
→ Retrieve
→ Validate
→ Apply
→ Update or Delete
```

---

### [FAQ]

Q. Long-Term Memory 문서에서 가장 피해야 할 것은?

A. 모든 대화를 저장하는 방식으로 설명하거나, Privacy / Safety 기준 없이 개인화만 강조하는 것이다.

Q. Memory와 RAG 문서를 혼동하면 어떤 문제가 생기는가?

A. 기술 지식과 사용자 맥락이 섞여 잘못된 우선순위와 오래된 판단이 발생할 수 있다.

Q. Memory 문서에 삭제 규칙이 꼭 필요한가?

A. 필요하다. 사용자가 원하지 않는 정보나 오래된 정보는 삭제 또는 비활성화할 수 있어야 한다.

---

# 21. Document Split Rules

## 21.1 Long-Term Memory 문서 분할 기준

### [개념]

Long-Term Memory는 저장 기준, 검색 전략, 갱신, 삭제, 안전성, Multi-Agent 공유, 평가 범위가 넓기 때문에 Part 단위로 분리한다.

각 Part는 독립 검색 가능해야 하며, 하나의 Part는 하나의 핵심 주제를 다룬다.

---

### [핵심]

권장 문서 분할:

```text
Long_Term_Memory_Part01_Core.md
Long_Term_Memory_Part02_Memory_Types.md
Long_Term_Memory_Part03_Memory_Selection_Extraction.md
Long_Term_Memory_Part04_Memory_Schema_Retrieval.md
Long_Term_Memory_Part05_Memory_Update_Deletion.md
Long_Term_Memory_Part06_Conflict_Freshness_Guardrails.md
Long_Term_Memory_Part07_Multi_Agent_Memory_Sharing.md
Long_Term_Memory_Part08_Evaluation_Troubleshooting.md
```

분할 기준:

- 하나의 Part는 하나의 핵심 주제
- 저장 기준과 추출 기준은 함께 작성 가능
- Schema와 Retrieval은 함께 작성 권장
- Update와 Deletion은 함께 작성 권장
- Conflict와 Freshness는 함께 작성 권장
- Guardrails는 반드시 포함
- Evaluation은 Checklist 중심
- Troubleshooting은 문제 / 원인 / 해결 형식
- 각 Part는 FAQ 포함
- 각 Part는 Retrieval Queries 포함

---

### [실무]

Long-Term Memory 문서 Set은 AI Expert Level에서 사용한다.

단, PM Agent와 Review Agent도 참조할 수 있으므로 특정 Memory Framework보다 저장 판단, 검색 판단, 안전 기준, 갱신 기준을 우선한다.

특정 구현 도구는 별도 문서로 분리한다.

예:

```text
Long_Term_Memory_Domain_Rules.md
Vector_Memory_Domain_Rules.md
User_Profile_Memory_Part.md
Agent_State_Memory_Part.md
Memory_Evaluation_Part.md
```

---

### [FAQ]

Q. Long-Term Memory 문서는 몇 개 Part로 나누는 것이 좋은가?

A. 7~8개 Part를 권장한다. Core, Type, Selection, Schema/Retrieval, Update/Delete, Conflict/Guardrails, Multi-Agent Sharing, Evaluation/Troubleshooting으로 분리한다.

Q. Agent State 문서와 합쳐도 되는가?

A. 권장하지 않는다. Agent State는 현재 작업 상태이고 Long-Term Memory는 장기 저장 정보이므로 구분하는 것이 좋다.

Q. 각 Part에도 Retrieval Queries가 필요한가?

A. 필요하다. 각 문서가 독립 검색될 수 있어야 한다.

---

# 22. Agent Usage Rules

## 22.1 Agent별 사용 기준

### [개념]

Long-Term Memory Domain Rules는 여러 Agent가 장기 기억을 안전하게 저장, 검색, 갱신, 삭제하도록 돕는다.

각 Agent는 자신의 역할에 맞는 Memory Chunk를 우선 검색한다.

---

### [핵심]

PM Agent:

- User Preference Memory 검색
- Project Memory 검색
- Decision Memory 검색
- Memory Conflict 조정
- Memory Update 후보 판단

AI/ML Agent:

- Memory Architecture 설계
- Memory Retrieval 전략 설계
- Memory Evaluation 설계
- Memory Guardrails 설계

Backend Agent:

- Memory 저장 구조 구현
- Memory API 구현
- Memory Schema 구현
- Memory 권한 / 삭제 로직 구현

DevOps Agent:

- Memory Store 운영
- Backup / Retention 정책
- Observability 구성
- Access Control 운영

Review Agent:

- Memory 사용 적절성 검토
- 오래된 Memory 검토
- 민감정보 저장 여부 검토
- Memory Conflict 검토
- 출력과 사용자 최신 지시 일치 여부 검토

Architecture Review Agent:

- Memory 경계 검토
- Multi-Agent Memory 공유 구조 검토
- Privacy Risk 검토
- 확장성 검토

---

### [실무]

Agent별 검색 우선순위:

```text
PM Agent
→ User Preference Memory / Project Memory / Decision Memory / Conflict Rules

AI/ML Agent
→ Memory Architecture / Retrieval / Evaluation / Guardrails

Backend Agent
→ Memory Schema / API / Access Control / Deletion

DevOps Agent
→ Memory Store / Backup / Observability / Retention

Review Agent
→ Safety Rules / Conflict Rules / Freshness / Common Mistakes

Architecture Review Agent
→ Multi-Agent Memory Sharing / Privacy Boundary / Scalability
```

Memory는 Agent가 더 개인화된 결과를 만들기 위한 보조 Context이다.

Memory가 Domain Rules나 현재 사용자 요청을 덮어쓰면 안 된다.

---

### [FAQ]

Q. Long-Term Memory Domain Rules는 어떤 Agent가 사용하는가?

A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.

Q. PM Agent는 어떤 Memory를 우선 검색해야 하는가?

A. User Preference Memory, Project Memory, Decision Memory, Workflow Memory를 우선 검색한다.

Q. Review Agent는 무엇을 검토해야 하는가?

A. Memory가 현재 요청에 적절히 사용되었는지, 오래되었는지, 민감정보가 포함되었는지, 최신 지시와 충돌하는지 검토한다.

---

# 23. Final Goal

## 23.1 최종 목표

### [개념]

Long-Term Memory Domain Rules의 최종 목표는 Agent가 장기적으로 유용한 정보를 안전하게 저장하고, 필요한 시점에 검색하고, 최신 상태로 갱신하고, 불필요하거나 위험한 정보를 삭제할 수 있도록 문서 제작 기준을 제공하는 것이다.

---

### [핵심]

최종 목표:

- Long-Term Memory 개념 검색 가능
- Short-Term Memory / Agent State / RAG Document와 구분 가능
- Memory Type 분류 가능
- Memory Selection 가능
- Memory Extraction 가능
- Memory Schema 설계 가능
- Memory Retrieval 가능
- Memory Update 가능
- Memory Deletion 가능
- Memory Conflict 해결 가능
- Memory Freshness 판단 가능
- Privacy / Safety Guardrails 적용 가능
- Multi-Agent Memory Sharing 가능
- Memory Evaluation 가능
- Troubleshooting 가능

---

### [실무]

Long-Term Memory RAG Doc Set은 다음 작업을 지원해야 한다.

```text
User Request
→ Memory Need Check
→ Relevant Memory Retrieval
→ Freshness / Safety Check
→ Current Request와 충돌 확인
→ RAG Context와 결합
→ Agent Output 생성
→ Review Agent 검증
→ 필요 시 Memory Update / Deletion 후보 생성
```

문서 품질은 Memory의 정확성, 재사용성, 최신성, 안전성, 검색 가능성으로 결정된다.

---

### [FAQ]

Q. Long-Term Memory Domain Rules의 최종 목적은?

A. Agent가 장기 기억을 안전하게 저장, 검색, 갱신, 삭제할 수 있도록 문서 제작 기준을 제공하는 것이다.

Q. 이 문서는 사람 학습용인가?

A. 아니다. AI Agent Retrieval과 장기 Memory 운영 품질을 높이기 위한 문서이다.

Q. Long-Term Memory 문서 품질은 무엇으로 판단하는가?

A. Agent가 필요한 Memory를 정확히 검색하고, 최신성과 안전성을 검증한 뒤 현재 작업에 적절히 적용할 수 있는지로 판단한다.

---

# Retrieval Queries

### [FAQ]

Q. Long-Term Memory란?
A. 미래 작업에서 재사용할 가치가 있는 사용자 선호, 프로젝트 규칙, 반복 Workflow, 확정 결정을 장기 저장하는 구조이다.

Q. Long-Term Memory와 Chat History의 차이는?
A. Chat History는 대화 전체 기록이고, Long-Term Memory는 재사용 가치가 있는 선별된 정보이다.

Q. Long-Term Memory와 Agent State의 차이는?
A. Agent State는 현재 작업 상태이고, Long-Term Memory는 장기적으로 재사용할 정보이다.

Q. Long-Term Memory와 RAG Document의 차이는?
A. RAG Document는 기술 지식과 규칙이고, Long-Term Memory는 사용자 선호와 프로젝트 맥락이다.

Q. Long-Term Memory에 무엇을 저장해야 하는가?
A. 장기적으로 반복 사용될 사용자 선호, 프로젝트 목표, 확정 결정, 반복 Workflow, 출력 규칙을 저장한다.

Q. Long-Term Memory에 저장하면 안 되는 것은?
A. 일회성 정보, 검증되지 않은 추측, 민감정보, 보안 인증 정보, 오래 유지되지 않을 정보는 저장하지 않는다.

Q. Memory Selection이란?
A. 대화나 작업 결과 중 어떤 정보를 장기 기억으로 저장할지 판단하는 과정이다.

Q. Memory Extraction이란?
A. 대화, 문서, 도구 결과에서 장기 기억 후보를 짧고 명확한 사실로 추출하는 과정이다.

Q. Memory Schema란?
A. Memory를 저장할 때 memoryType, content, scope, confidence, freshness, status 같은 필드로 구조화하는 규칙이다.

Q. Memory Retrieval은 언제 필요한가?
A. 사용자 선호, 프로젝트 맥락, 이전 결정, 반복 Workflow가 현재 작업에 영향을 줄 때 필요하다.

Q. Memory Update는 언제 필요한가?
A. 사용자 선호, 프로젝트 규칙, 기술 스택, 이전 결정이 변경되었을 때 필요하다.

Q. Memory Deletion은 언제 필요한가?
A. 사용자가 삭제를 요청하거나, Memory가 부정확하거나, 오래되었거나, 민감정보가 포함된 경우 필요하다.

Q. Memory Conflict란?
A. 현재 사용자 지시, RAG 문서, Project Progress, 기존 Memory가 서로 충돌하는 상황이다.

Q. Memory와 현재 사용자 요청이 충돌하면 무엇을 우선하는가?
A. 현재 사용자 요청을 우선한다.

Q. Memory와 Domain Rules가 충돌하면 무엇을 우선하는가?
A. Domain Rules와 Project Progress를 우선한다.

Q. Memory Freshness란?
A. 저장된 Memory가 현재에도 유효한지 판단하는 기준이다.

Q. Long-Term Memory에서 Privacy Guardrails가 중요한 이유는?
A. Memory는 사용자 정보와 장기 맥락을 다루므로 민감정보 저장과 과도한 프로파일링을 방지해야 하기 때문이다.

Q. Multi-Agent Memory Sharing이란?
A. 여러 Agent가 역할에 필요한 최소 Memory만 공유하도록 접근 범위와 갱신 권한을 관리하는 구조이다.

Q. Long-Term Memory와 RAG는 어떻게 함께 사용하는가?
A. RAG는 기술 지식을 제공하고 Memory는 사용자 선호와 프로젝트 맥락을 제공하며, 현재 요청과 Domain Rules를 우선한다.

Q. Memory Evaluation 항목은?
A. Accuracy, Relevance, Usefulness, Freshness, Safety, Specificity, Retrieval Precision, Conflict Handling이다.

Q. Long-Term Memory에서 흔한 실패는?
A. 불필요한 Memory 과다 저장, 오래된 Memory 사용, Memory Conflict 미감지, 민감정보 저장, 삭제 요청 미반영이다.

Q. Long-Term Memory 문서 분할은 어떻게 하는가?
A. Core, Type, Selection, Schema/Retrieval, Update/Delete, Conflict/Guardrails, Multi-Agent Sharing, Evaluation/Troubleshooting으로 분리한다.

Q. Long-Term Memory 문서에서 피해야 할 것은?
A. 모든 대화를 저장하는 방식으로 설명하거나 Privacy / Safety 기준 없이 개인화만 강조하는 것이다.

Q. Long-Term Memory Domain Rules는 어떤 Agent가 사용하는가?
A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.
