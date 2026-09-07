# Context Engineering Domain Rules

---

# 1. Domain Purpose

## 1.1 Context Engineering 문서 목적

### [개념]

Context Engineering Domain 문서는 AI Agent / AI/ML Agent / PM Agent / Backend Agent / Review Agent / Architecture Review Agent가 LLM, RAG, Agentic RAG, Graph RAG, Tool Calling, Long-Term Memory 기반 시스템에서 Context를 설계, 구성, 압축, 검증, 최적화할 때 참조하는 RAG 제작 규칙 문서이다.

Context Engineering은 단순히 Prompt를 잘 쓰는 작업이 아니다.

Context Engineering은 사용자 요청, 시스템 규칙, Domain Rules, 검색 결과, Tool Result, Memory, Agent State, Output Format, Safety Rule을 LLM이 정확히 사용할 수 있도록 입력 Context를 구조화하는 작업이다.

LLM 품질은 모델 성능뿐 아니라 어떤 Context를 어떤 순서와 우선순위로 제공하느냐에 크게 의존한다.

---

### [핵심]

- Context Engineering = Context Selection + Context Assembly + Context Compression + Context Validation
- Prompt Engineering보다 넓은 개념
- RAG 검색 결과를 그대로 넣지 않음
- 필요한 Context만 선택
- Context 우선순위 필요
- 충돌 Context 감지 필요
- Token Budget 관리 필요
- Long Context 품질 저하 주의
- Tool Result와 Memory 사용 기준 필요
- Agent State와 Long-Term Memory 구분 필요
- Grounded Answer 생성을 지원해야 함
- Agentic RAG / Graph RAG / RAG Evaluation과 연결 가능

---

### [실무]

2026 실무 기준 Context Engineering 문서는 다음 목적을 우선한다.

- LLM 입력 Context 설계
- RAG Context Selection 기준 제공
- Context Priority 기준 제공
- Context Compression 기준 제공
- Context Conflict 해결 기준 제공
- Token Budget 관리 기준 제공
- System / Developer / User Instruction 우선순위 제공
- Tool Result 삽입 기준 제공
- Memory 사용 기준 제공
- Agent State 삽입 기준 제공
- Long Context Handling 기준 제공
- Context Evaluation 기준 제공
- Context Failure Troubleshooting 제공

Context Engineering 문서는 사람이 Prompt 작성법을 공부하기 위한 문서가 아니라, Agent가 작업에 필요한 Context를 안정적으로 구성하고 검증할 수 있도록 돕는 운영 지식 문서로 작성한다.

---

### [FAQ]

Q. Context Engineering 문서는 무엇을 위한 문서인가?

A. Agent가 사용자 요청, 검색 결과, Tool Result, Memory, 규칙을 LLM 입력 Context로 안전하게 구성할 수 있도록 기준을 제공하는 문서이다.

Q. Context Engineering은 Prompt Engineering과 같은가?

A. 아니다. Prompt Engineering은 지시문 작성 중심이고, Context Engineering은 입력에 포함할 정보의 선택, 순서, 압축, 검증까지 포함한다.

Q. Context Engineering에서 가장 중요한 것은?

A. 필요한 Context를 정확히 선택하고, 우선순위를 지키며, 충돌과 노이즈를 제거하는 것이다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Context Engineering Domain 문서는 LLM과 Agent 시스템에서 입력 Context를 설계하고 관리하기 위한 개념, 구성 요소, 우선순위, 압축, 검증, 장애 대응 기준을 포함한다.

---

### [핵심]

포함 범위:

- Context Engineering
- Context Window
- Token Budget
- Context Selection
- Context Assembly
- Context Compression
- Context Ordering
- Context Priority
- Context Validation
- Context Conflict
- Context Noise
- Context Drift
- Prompt Context
- RAG Context
- Graph Context
- Tool Result Context
- Memory Context
- Agent State Context
- System Instruction
- Developer Instruction
- User Instruction
- Output Format Instruction
- Safety Instruction
- Long Context Handling
- Context Evaluation
- Context Observability
- Context Troubleshooting

제외 범위:

- Prompt 문장 표현법만 다루는 문서
- LLM 내부 Attention 수학 상세
- Vector Database 설치법
- Tool Calling API 전체 문서
- Memory 저장소 구현 상세
- 특정 프레임워크 API 복붙
- 일반 글쓰기 기법
- 모델별 Context Window 수치 나열 중심 문서

---

### [실무]

Context Engineering 문서는 아래 질문에 답할 수 있어야 한다.

- 현재 요청에 어떤 Context가 필요한가?
- 어떤 Context를 제외해야 하는가?
- Context 우선순위는 어떻게 정하는가?
- RAG 검색 결과 중 어떤 Chunk를 넣어야 하는가?
- Tool Result는 어떻게 삽입해야 하는가?
- Memory는 언제 Context에 포함해야 하는가?
- Context가 너무 길면 어떻게 압축해야 하는가?
- Context 간 충돌이 있으면 무엇을 우선해야 하는가?
- Long Context에서 핵심 정보 손실을 어떻게 줄일 것인가?
- 최종 답변이 Context에 근거했는지 어떻게 검증할 것인가?

---

### [FAQ]

Q. Context Engineering 문서에 Prompt 예시만 넣어도 되는가?

A. 아니다. Context 선택, 우선순위, 압축, 충돌 해결, 검증 기준을 반드시 포함해야 한다.

Q. RAG 문서와 Context Engineering은 어떻게 연결되는가?

A. RAG는 Context 후보를 검색하고, Context Engineering은 검색 결과 중 LLM 입력에 넣을 Context를 선택하고 구성한다.

Q. Context Engineering은 Agentic RAG와 연결되는가?

A. 연결된다. Agent가 Query Planning, Retrieval, Tool Calling, Memory 사용 결과를 Context로 조립해야 하기 때문이다.

---

# 3. Section Priority

## 3.1 필수 섹션 규칙

### [개념]

Context Engineering 문서는 모든 주요 Chunk에 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`를 우선 적용한다.

흐름이 필요한 주제는 `[Flow]`를 추가한다.

우선순위 판단이 필요한 주제는 `[Priority]` 또는 `[Checklist]`를 추가한다.

비교가 필요한 주제는 `[Comparison]`을 추가한다.

장애 대응이 필요한 주제는 `[Troubleshooting]`을 추가한다.

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

- [Priority]
- [Context Schema]
- [Token Budget]
- [Evaluation]
- [Review Point]
- [Anti-Pattern]

---

### [실무]

Context Engineering 문서는 단순 개념 설명보다 Context 구성 판단 기준을 우선한다.

각 문서는 아래 정보 중 최소 2개 이상을 포함한다.

- Context Selection 기준
- Context Priority 기준
- Context Ordering 기준
- Context Compression 기준
- Token Budget 기준
- Conflict Resolution 기준
- Tool Result 삽입 기준
- Memory 삽입 기준
- Evaluation 기준
- Troubleshooting 기준

---

### [FAQ]

Q. Context Engineering 문서에 Flow가 필요한가?

A. 필요하다. Context는 사용자 요청에서 최종 LLM 입력까지 단계적으로 구성되기 때문이다.

Q. Context Engineering 문서에 Priority가 필요한 이유는?

A. 여러 규칙, 검색 결과, Memory, Tool Result가 충돌할 때 무엇을 우선할지 Agent가 판단해야 하기 때문이다.

Q. Context Engineering 문서에 Troubleshooting이 필요한가?

A. 필요하다. Context 누락, Context 과다, 충돌, 오래된 정보 사용, Tool Result 왜곡 문제가 자주 발생한다.

---

# 4. Core Concept Rules

## 4.1 Context Engineering 핵심 개념 작성 규칙

### [개념]

Context Engineering 핵심 개념은 Prompt Engineering, RAG, Memory, Agent State와 구분되도록 작성한다.

Context Engineering은 LLM 입력에 들어가는 전체 정보 구조를 설계하는 작업이다.

이는 지시문 작성뿐 아니라 검색 결과 선택, Memory 선택, Tool Result 삽입, 충돌 제거, Token Budget 관리, 출력 형식 유지까지 포함한다.

---

### [핵심]

반드시 포함할 개념:

- Context Engineering
- Context Window
- Token Budget
- Context Selection
- Context Assembly
- Context Compression
- Context Ordering
- Context Priority
- Context Validation
- Context Conflict
- Context Noise
- Context Drift
- RAG Context
- Graph Context
- Tool Result Context
- Memory Context
- Agent State Context
- System Instruction
- Developer Instruction
- User Instruction
- Output Format Instruction
- Grounded Answer

용어 통일:

- Context Engineering
- Context Window
- Token Budget
- Context Selection
- Context Assembly
- Context Compression
- Context Priority
- Context Conflict
- Context Noise
- Context Validation
- Context Snapshot
- Grounded Answer

---

### [실무]

Context Engineering 설명은 아래 구분을 반드시 포함한다.

```text
Prompt Engineering
→ 모델에게 어떻게 지시할지 설계

RAG
→ 외부 문서를 검색해 Context 후보를 제공

Long-Term Memory
→ 장기적으로 재사용할 사용자 / 프로젝트 맥락 제공

Agent State
→ 현재 Workflow의 상태 정보 제공

Context Engineering
→ Prompt, RAG, Memory, Tool Result, Agent State를 선택 / 정렬 / 압축 / 검증해 LLM 입력 Context로 구성
```

Context Engineering 문서는 “Context를 많이 넣으면 좋다” 수준에서 멈추면 안 된다.

Agent가 무엇을 넣고, 무엇을 제외하고, 어떤 순서로 배치하고, 어떻게 검증해야 하는지 판단할 수 있어야 한다.

---

### [FAQ]

Q. Context Engineering이란?

A. LLM 입력에 포함할 지시문, 검색 결과, Tool Result, Memory, Agent State를 선택, 정렬, 압축, 검증하는 작업이다.

Q. Context Engineering과 Prompt Engineering의 차이는?

A. Prompt Engineering은 지시문 작성 중심이고, Context Engineering은 입력 정보 전체의 구성과 품질 관리까지 포함한다.

Q. Context를 많이 넣으면 항상 좋은가?

A. 아니다. 관련 없는 Context는 노이즈를 만들고 답변 품질과 비용을 악화시킬 수 있다.

---

# 5. Context Source Rules

## 5.1 Context Source 작성 규칙

### [개념]

Context Source는 LLM 입력 Context를 구성할 때 사용할 수 있는 정보 출처이다.

Context Source를 구분해야 우선순위, 신뢰도, 최신성, 사용 범위를 판단할 수 있다.

---

### [핵심]

대표 Context Source:

- System Instruction
- Developer Instruction
- Current User Request
- Conversation Context
- Master RAG Rules
- Domain Rules
- Project Progress
- Retrieved RAG Chunk
- Graph Context
- Tool Result
- Long-Term Memory
- Agent State
- Evaluation Result
- Error Log
- User Feedback
- Output Format Rule

Source별 판단 기준:

- 신뢰도
- 최신성
- 현재 요청 관련성
- 적용 범위
- 충돌 가능성
- 민감정보 여부
- Token 비용
- 검증 가능성

---

### [실무]

Context Source 예시:

```text
현재 요청:
- 다음 Domain Rules 작성

필수 Context:
- Current User Request
- Master RAG Rules
- Domain Rules Style
- Project Progress
- Output Format Rule

선택 Context:
- 관련 기존 Domain Rules
- Long-Term Memory의 사용자 출력 선호

제외 Context:
- 현재 작업과 무관한 과거 프로젝트
- 오래된 지시
- 일반 AI 설명문
```

Context Source는 모두 동일한 우선순위를 가지지 않는다.

Agent는 Source별 우선순위와 현재 작업 관련성을 함께 평가해야 한다.

---

### [FAQ]

Q. Context Source란?

A. LLM 입력 Context를 구성할 때 사용할 수 있는 지시문, 문서, 검색 결과, Tool Result, Memory, Agent State 같은 정보 출처이다.

Q. 모든 Context Source를 입력에 넣어야 하는가?

A. 아니다. 현재 요청에 필요한 Source만 선택해야 한다.

Q. Context Source를 구분해야 하는 이유는?

A. Source마다 신뢰도, 최신성, 우선순위, 적용 범위가 다르기 때문이다.

---

# 6. Context Priority Rules

## 6.1 Context 우선순위 작성 규칙

### [개념]

Context Priority는 여러 Context Source가 동시에 존재하거나 충돌할 때 어떤 정보를 우선 적용할지 정하는 규칙이다.

Context Priority가 없으면 Agent가 오래된 Memory나 낮은 우선순위 문서를 현재 요청보다 우선할 수 있다.

---

### [핵심]

기본 우선순위:

```text
System Instruction
→ Current User Request
→ Master RAG Rules
→ Domain Rules
→ Project Progress
→ Current Uploaded / Retrieved Source
→ Tool Result
→ Relevant Long-Term Memory
→ Conversation Context
→ General Knowledge
```

주의:

- 현재 사용자 요청은 과거 Memory보다 우선
- Domain Rules는 일반 문서보다 우선
- Project Progress는 오래된 Memory보다 우선
- Tool Result는 검증 후 사용
- Memory는 현재 요청과 충돌하면 사용하지 않음
- General Knowledge는 RAG 근거를 대체하지 않음

---

### [실무]

Context Priority 적용 예시:

```text
상황:
기존 Memory에는 "중간 응답 허용"이 저장되어 있음
현재 요청에는 "중간 응답 금지"가 있음

판단:
- Current User Request 우선
- 기존 Memory는 무시 또는 Update 후보
- 최종 출력에는 중간 응답 금지 적용
```

Priority는 단순 정렬이 아니라 충돌 해결 기준이다.

Context 충돌이 발생하면 Agent는 우선순위를 기준으로 적용할 Context를 선택해야 한다.

---

### [FAQ]

Q. Context Priority는 왜 필요한가?

A. 여러 지시, 문서, Memory가 충돌할 때 무엇을 우선할지 결정해야 하기 때문이다.

Q. 현재 사용자 요청과 Memory가 충돌하면 무엇을 우선하는가?

A. 현재 사용자 요청을 우선한다.

Q. Domain Rules와 일반 지식이 충돌하면 무엇을 우선하는가?

A. Domain Rules를 우선한다.

---

# 7. Context Selection Rules

## 7.1 Context Selection 작성 규칙

### [개념]

Context Selection은 Context 후보 중 현재 요청 해결에 필요한 정보만 선택하는 과정이다.

RAG 검색 결과, Memory, Tool Result, Agent State를 모두 넣는 것이 아니라 목적에 맞는 Context를 선별해야 한다.

---

### [핵심]

Context Selection 기준:

- 현재 요청과 직접 관련 있는가?
- 답변 생성에 필요한 근거인가?
- Domain Rules 또는 Project Progress인가?
- 최신 정보인가?
- Source가 신뢰 가능한가?
- 중복되지 않는가?
- 충돌하지 않는가?
- Token Budget 안에 들어가는가?
- 출력 형식 유지에 필요한가?
- Review Agent가 검증할 수 있는가?

제외 기준:

- 관련성 낮음
- 중복
- 오래됨
- 충돌함
- 검증 불가
- 민감정보 포함
- 너무 장황함
- 현재 요청과 무관한 과거 맥락
- 일반론만 포함

---

### [실무]

Context Selection Flow:

```text
Context Candidate 수집
→ Relevance 평가
→ Priority 적용
→ Duplicate 제거
→ Conflict 감지
→ Token Budget 확인
→ Context Selection
→ Context Assembly
```

Selection Checklist:

```md
### [Checklist]

- 현재 요청과 직접 관련 있는 Context인가?
- 핵심 근거가 포함되어 있는가?
- Domain Rules와 Project Progress가 포함되었는가?
- 중복 Context를 제거했는가?
- 오래된 Context를 제외했는가?
- 충돌 Context를 감지했는가?
- Token Budget을 초과하지 않는가?
```

---

### [FAQ]

Q. Context Selection은 왜 중요한가?

A. 잘못된 Context를 넣으면 LLM이 관련 없는 내용에 끌려가거나 충돌된 답변을 만들 수 있기 때문이다.

Q. 검색된 Chunk는 모두 Context에 넣어야 하는가?

A. 아니다. 검색 결과 중 현재 요청에 직접 필요한 Chunk만 선택해야 한다.

Q. Context Selection 실패는 어떤 문제를 만드는가?

A. Hallucination, 답변 누락, 출력 형식 위반, 비용 증가, 긴 응답 지연을 만들 수 있다.

---

# 8. Context Assembly Rules

## 8.1 Context Assembly 작성 규칙

### [개념]

Context Assembly는 선택된 Context를 LLM 입력에 넣기 좋은 구조와 순서로 조립하는 과정이다.

같은 Context라도 배치 순서와 구조가 다르면 모델의 응답 품질이 달라질 수 있다.

---

### [핵심]

Context Assembly 구성 요소:

- Role Instruction
- Task Goal
- Current User Request
- Output Format
- Constraints
- Domain Rules Summary
- Retrieved Evidence
- Tool Result
- Memory Summary
- Agent State
- Validation Checklist
- Final Instruction

권장 순서:

```text
1. Role / Task Instruction
2. Current User Request
3. Non-Negotiable Rules
4. Output Format
5. Domain Rules / Project Rules
6. Retrieved Evidence
7. Tool Result
8. Relevant Memory
9. Agent State
10. Validation Checklist
11. Final Answer Instruction
```

---

### [실무]

Context Assembly 예시:

```text
Task:
- Context Engineering Domain Rules 작성

Rules:
- MASTER_RAG_RULES 적용
- 출력 형식 유지
- 코드블록 id 제거
- 중간 응답 금지

Evidence:
- 기존 Domain Rules 구조
- Project Progress Level 4 AI Expert 목록

Output:
- writing block 형식의 완성 문서
```

Context Assembly는 장문 원문을 무작정 붙이는 작업이 아니다.

Agent가 실행할 수 있는 구조화된 Context로 정리해야 한다.

---

### [FAQ]

Q. Context Assembly는 무엇인가?

A. 선택된 Context를 LLM이 잘 사용할 수 있도록 순서와 구조를 정해 입력으로 조립하는 과정이다.

Q. Context 순서가 중요한가?

A. 중요하다. 핵심 규칙과 현재 요청이 뒤쪽에 묻히면 모델이 덜 따를 수 있다.

Q. Retrieved Evidence는 어디에 배치하는가?

A. 규칙과 출력 형식 뒤에 배치하고, 답변 생성에 필요한 근거로 사용하게 한다.

---

# 9. Token Budget Rules

## 9.1 Token Budget 관리 규칙

### [개념]

Token Budget은 LLM 입력과 출력에 사용할 수 있는 Token 한도이다.

Context Engineering은 제한된 Token Budget 안에서 가장 중요한 정보를 유지하는 작업이다.

---

### [핵심]

Token Budget 구성:

- System Instruction Token
- Developer Instruction Token
- User Request Token
- Retrieved Context Token
- Tool Result Token
- Memory Token
- Agent State Token
- Output Token Reserve
- Safety Margin

Token Budget 관리 기준:

- 출력 Token Reserve 확보
- 높은 우선순위 Context 우선
- 중복 제거
- 긴 Context 압축
- 관련성 낮은 Context 제거
- Tool Result 요약
- Memory 최소화
- Chunk 수 제한
- Context Overflow 방지

---

### [실무]

Token Budget Flow:

```text
Available Context Window 확인
→ 필수 Instruction Token 계산
→ Output Reserve 확보
→ Context 후보 우선순위 정렬
→ 중복 제거
→ Compression 적용
→ 최종 Context 구성
```

Token Budget 예시:

```text
우선 포함:
- 현재 요청
- 출력 형식
- Domain Rules 핵심
- 검색된 핵심 Evidence

압축 또는 제외:
- 장문 설명
- 반복 FAQ
- 낮은 관련 Chunk
- 오래된 Memory
```

Context Window가 크더라도 모든 정보를 넣지 않는다.

Long Context는 비용과 지연을 늘리고, 모델이 핵심 정보를 놓칠 수 있다.

---

### [FAQ]

Q. Token Budget은 왜 중요한가?

A. Context Window는 제한되어 있고, 너무 많은 Context는 비용, 지연, 품질 저하를 만들 수 있기 때문이다.

Q. 출력 Token Reserve는 왜 필요한가?

A. 입력 Context가 너무 길면 모델이 완성된 답변을 출력할 공간이 부족해질 수 있기 때문이다.

Q. Context Window가 크면 Token Budget을 신경 쓰지 않아도 되는가?

A. 아니다. Long Context에서도 핵심 정보 손실과 비용 증가 문제가 발생할 수 있다.

---

# 10. Context Compression Rules

## 10.1 Context Compression 작성 규칙

### [개념]

Context Compression은 선택된 Context를 의미와 근거를 유지하면서 Token 수를 줄이는 과정이다.

Compression은 단순 요약이 아니라 답변 생성에 필요한 핵심 Evidence를 보존하는 작업이다.

---

### [핵심]

보존해야 할 정보:

- 핵심 주장
- Source
- 조건
- 예외
- 숫자
- 날짜
- 버전
- 코드
- 명령어
- API 이름
- Entity / Relation
- User Constraint
- Output Format Rule
- Safety Rule

압축 가능한 정보:

- 반복 설명
- 장문 배경
- 중복 문장
- 일반론
- 예시 과다
- 낮은 관련성 설명
- 과도한 수식어

---

### [실무]

Compression 예시:

```text
원문:
Context Engineering은 LLM 입력을 구성하는 매우 중요한 과정이며, 다양한 요소를 고려해야 한다. 여기에는 Prompt, RAG, Tool Result, Memory 등이 포함된다.

압축:
Context Engineering은 Prompt, RAG, Tool Result, Memory를 선택 / 정렬 / 압축해 LLM 입력을 구성하는 과정이다.
```

Compression Checklist:

```md
### [Checklist]

- 핵심 근거가 유지되었는가?
- Source가 유지되었는가?
- 조건과 예외가 제거되지 않았는가?
- 코드 / 숫자 / 버전이 왜곡되지 않았는가?
- 압축 후 현재 요청 해결에 충분한가?
```

---

### [FAQ]

Q. Context Compression은 단순 요약인가?

A. 아니다. 답변 생성에 필요한 핵심 근거와 조건을 보존하면서 Token을 줄이는 과정이다.

Q. Compression 시 절대 제거하면 안 되는 것은?

A. Source, 조건, 예외, 숫자, 버전, 코드, 사용자 제약, 출력 형식 규칙은 함부로 제거하면 안 된다.

Q. Compression이 잘못되면 어떤 문제가 생기는가?

A. 근거 누락, 조건 왜곡, Hallucination, 잘못된 답변이 발생할 수 있다.

---

# 11. Context Conflict Rules

## 11.1 Context Conflict 해결 규칙

### [개념]

Context Conflict는 입력 Context 안의 규칙, 문서, Memory, Tool Result, 사용자 요청이 서로 다른 내용을 말하는 상황이다.

Context Engineering에서는 Conflict를 감지하고 우선순위에 따라 해결해야 한다.

---

### [핵심]

Conflict 유형:

- 현재 요청과 Memory 충돌
- Domain Rules와 일반 문서 충돌
- Project Progress와 오래된 정보 충돌
- Tool Result와 RAG 문서 충돌
- Retrieved Chunk 간 충돌
- 출력 형식 지시 충돌
- 안전 규칙과 사용자 요청 충돌
- Version 정보 충돌
- Agent Output 간 충돌

해결 기준:

- 현재 사용자 요청 우선
- System / Safety Rule 우선
- Master RAG Rules 우선
- Domain Rules 우선
- 최신 Project Progress 우선
- 검증된 Tool Result 우선
- 오래된 Memory는 낮은 우선순위
- 불확실하면 단정 금지
- 필요 시 Review Agent 검토

---

### [실무]

Conflict 해결 예시:

```text
문제:
검색된 문서 A는 "Part 6개"라고 하고, 최신 Project Progress는 "Part 8개"라고 함

해결:
- 최신 Project Progress 우선
- 문서 A는 오래된 Context로 표시
- 최종 출력은 최신 기준 적용
```

Conflict Checklist:

```md
### [Checklist]

- 충돌하는 Context를 식별했는가?
- 어떤 Source가 더 최신인가?
- 어떤 Source가 더 높은 우선순위인가?
- Tool Result가 검증되었는가?
- 오래된 Memory를 제외했는가?
- 최종 답변에 충돌을 반영했는가?
```

---

### [FAQ]

Q. Context Conflict란?

A. 입력 Context 안의 지시, 문서, Memory, Tool Result가 서로 다른 내용을 말하는 상황이다.

Q. Context Conflict가 발생하면 어떻게 해야 하는가?

A. Context Priority에 따라 우선순위를 적용하고, 낮은 우선순위 Context를 제외하거나 불확실성을 표시한다.

Q. Tool Result와 문서가 충돌하면 무엇을 우선하는가?

A. Tool Result가 현재 상태를 검증한 결과라면 우선할 수 있지만, Tool Result 자체도 검증해야 한다.

---

# 12. Context Noise Rules

## 12.1 Context Noise 제거 규칙

### [개념]

Context Noise는 현재 요청 해결에 직접 도움이 되지 않거나 답변 품질을 방해하는 입력 정보이다.

Context Noise가 많으면 LLM이 핵심 지시를 놓치거나 관련 없는 내용을 생성할 수 있다.

---

### [핵심]

Noise 유형:

- 관련 없는 검색 Chunk
- 중복 Chunk
- 오래된 Memory
- 낮은 신뢰도 정보
- 일반론 과다
- 장문 배경 설명
- 충돌 정보
- 불필요한 Tool Result
- 과도한 대화 이력
- 현재 요청과 무관한 프로젝트 정보
- 출력 형식과 무관한 예시
- Deprecated 문서

Noise 제거 기준:

- Relevance 낮음
- Priority 낮음
- 중복
- 최신성 낮음
- Source 불명확
- 검증 불가
- Token 비용 높음
- 현재 요청 영향 없음

---

### [실무]

Noise 제거 Flow:

```text
Context Candidate
→ Relevance Score 확인
→ Priority 확인
→ Duplicate 제거
→ Freshness 확인
→ Conflict 제거
→ Token Cost 확인
→ Final Context 유지
```

Noise 제거 예시:

```text
요청:
Context Engineering Domain Rules 작성

제거:
- FestaPick 프로젝트 상세 구현 내용
- 일반 LLM 역사 설명
- 현재 Domain과 무관한 Docker 오류 기록
- 오래된 출력 형식 Memory
```

---

### [FAQ]

Q. Context Noise란?

A. 현재 요청 해결에 직접 도움이 되지 않거나 답변 품질을 방해하는 입력 정보이다.

Q. Context Noise가 많으면 어떤 문제가 생기는가?

A. 답변이 산만해지고, 핵심 지시를 놓치고, Hallucination이나 형식 위반이 증가할 수 있다.

Q. 중복 Context도 Noise인가?

A. 그렇다. 중복 정보는 Token을 낭비하고 특정 정보의 가중치를 과도하게 높일 수 있다.

---

# 13. RAG Context Rules

## 13.1 RAG Context 구성 규칙

### [개념]

RAG Context는 Retrieval Pipeline이 검색한 문서 Chunk 중 최종 LLM 입력에 포함되는 근거 Context이다.

RAG Context는 답변의 근거가 되므로 관련성, 신뢰도, Source, Section, 최신성을 함께 고려해야 한다.

---

### [핵심]

RAG Context 포함 기준:

- 질문과 직접 관련
- Expected Context 포함
- Domain Rules 우선
- Project Progress 우선
- FAQ / Checklist / Troubleshooting 우선
- Code Example 보존
- Source Metadata 포함
- 최신 문서 우선
- 중복 제거
- 충돌 제거

RAG Context 제외 기준:

- 낮은 관련성
- 오래된 문서
- Deprecated 문서
- 동일 내용 중복
- 불완전한 Chunk
- Q와 A가 분리된 FAQ
- 코드블록이 잘린 Chunk
- Source 불명확

---

### [실무]

RAG Context Assembly 예시:

```text
Query:
JWT 인증 흐름 검토

Selected RAG Context:
- Security Domain Rules
- JWT Part 문서
- Filter Chain 문서
- Common Mistakes
- Review Checklist

Excluded:
- OAuth2 문서
- 일반 로그인 개념 문서
- 오래된 Security 메모
```

RAG Context는 검색 결과 순서 그대로 넣지 않는다.

Re-Ranking과 Context Selection을 거쳐 답변 생성에 필요한 순서로 재구성한다.

---

### [FAQ]

Q. RAG Context란?

A. 검색된 문서 Chunk 중 최종 LLM 입력에 포함되어 답변 근거로 사용되는 Context이다.

Q. 검색 결과를 그대로 넣으면 안 되는 이유는?

A. 검색 결과에는 노이즈, 중복, 낮은 관련성 Chunk가 섞일 수 있기 때문이다.

Q. RAG Context에는 Source가 필요한가?

A. 필요하다. 답변 근거 검증과 Groundedness 평가를 위해 Source Metadata가 필요하다.

---

# 14. Graph Context Rules

## 14.1 Graph Context 구성 규칙

### [개념]

Graph Context는 Graph RAG에서 Entity, Relation, Path, Community Summary를 LLM 입력에 사용할 수 있도록 정리한 Context이다.

Graph Context는 Node와 Edge를 그대로 나열하는 것이 아니라 질문과 관련된 관계 근거를 구조화해야 한다.

---

### [핵심]

Graph Context 구성 요소:

- Matched Entity
- Related Entity
- Relation
- Path
- Community Summary
- Evidence Chunk
- Source Document
- Confidence
- Conflict Note
- Missing Relation
- Answer Focus

Graph Context 선택 기준:

- 질문 Entity와 직접 관련
- 짧고 설명 가능한 Path
- Evidence가 있는 Edge
- Relation 방향 명확
- Community Summary는 Global 질문에만 사용
- 관련 없는 Node 제거
- 너무 긴 Path 제외

---

### [실무]

Graph Context 예시:

```text
Matched Entity:
- JwtAuthenticationFilter

Path:
- JwtAuthenticationFilter validates Access Token
- JwtAuthenticationFilter writes SecurityContext
- SecurityContext stores Authentication

Evidence:
- Security_Advanced_Part03_Filter_Chain.md
- Security_Advanced_Part04_JWT.md

Answer Focus:
- JWT 검증
- 인증 객체 저장
- Filter Chain 내 위치
```

Graph Context는 Multi-Hop 질문에 유용하지만, Evidence 없는 Relation은 답변 근거로 사용하지 않는다.

---

### [FAQ]

Q. Graph Context란?

A. Graph Search 결과를 LLM이 답변에 사용할 수 있도록 Entity, Relation, Path, Evidence 중심으로 정리한 Context이다.

Q. Graph의 모든 Node와 Edge를 Context에 넣어야 하는가?

A. 아니다. 질문과 직접 관련된 Entity, Relation, Path만 선택해야 한다.

Q. Evidence 없는 Edge를 사용해도 되는가?

A. 권장하지 않는다. 답변 근거로 사용하려면 Source나 Evidence Chunk가 있어야 한다.

---

# 15. Tool Result Context Rules

## 15.1 Tool Result Context 구성 규칙

### [개념]

Tool Result Context는 Agent가 호출한 도구의 결과를 LLM 입력이나 다음 Agent 단계에서 사용할 수 있도록 정리한 Context이다.

Tool Result는 실제 실행 결과일 수 있으므로 중요하지만, 검증 없이 그대로 답변에 사용하면 안 된다.

---

### [핵심]

Tool Result Context 포함 요소:

- toolName
- toolInput
- toolOutput
- executionStatus
- timestamp
- errorMessage
- validationResult
- source
- stateChange
- confidence
- nextAction

Tool Result 사용 기준:

- 현재 요청 해결에 필요한가
- 실행이 성공했는가
- 출력 형식이 유효한가
- 결과가 최신인가
- RAG 문서와 충돌하지 않는가
- 상태 변경이 있었는가
- 재시도 필요성이 있는가

---

### [실무]

Tool Result Context 예시:

```text
Tool:
- file_search

Input:
- Context Engineering Domain Rules

Output:
- 관련 Master Rules와 Project Progress 검색 결과

Validation:
- 현재 문서 작성에 사용 가능

Use:
- Domain Rules 구조와 Retrieval 최적화 기준에 반영
```

Tool Result는 길면 요약해서 넣는다.

단, 숫자, 파일명, 에러 메시지, 실행 결과는 왜곡 없이 유지한다.

---

### [FAQ]

Q. Tool Result Context란?

A. 도구 호출 결과를 다음 LLM 입력이나 Agent 단계에서 사용할 수 있도록 정리한 Context이다.

Q. Tool Result를 그대로 답변에 사용해도 되는가?

A. 아니다. 실행 성공 여부와 결과 유효성을 검증한 뒤 사용해야 한다.

Q. Tool Result가 RAG 문서와 충돌하면 어떻게 해야 하는가?

A. Tool Result의 최신성과 신뢰도를 검증하고, 충돌 내용을 Review Agent가 확인해야 한다.

---

# 16. Memory Context Rules

## 16.1 Memory Context 구성 규칙

### [개념]

Memory Context는 Long-Term Memory 또는 Short-Term Memory에서 현재 요청에 필요한 정보만 선택해 LLM 입력에 포함하는 Context이다.

Memory는 사용자 선호와 프로젝트 맥락을 제공하지만, 기술 근거를 대체하면 안 된다.

---

### [핵심]

Memory Context 사용 상황:

- 사용자 출력 선호가 필요함
- 프로젝트 장기 맥락이 필요함
- 이전 결정 사항 확인 필요
- 반복 Workflow 적용 필요
- Agent 역할 구조 참고 필요
- 사용자가 과거 맥락을 언급함

Memory Context 제외 상황:

- 현재 요청과 무관함
- 오래됨
- 현재 요청과 충돌함
- Domain Rules와 충돌함
- 민감정보 포함
- 추측 기반 Memory
- 일반 지식과 중복

---

### [실무]

Memory Context 예시:

```text
현재 요청:
- 다음 Domain Rules 작성

Memory Context:
- 사용자는 RAG 문서 출력 형식을 writing block으로 원함
- 코드블록 id 속성 제거를 원함
- 중간 응답 금지를 원함

적용:
- 최종 문서 출력 형식에 반영
```

Memory는 최소 요약 형태로 사용한다.

Memory 원문 전체를 Context에 넣지 않는다.

---

### [FAQ]

Q. Memory Context는 언제 사용하는가?

A. 사용자 선호, 프로젝트 맥락, 이전 결정, 반복 Workflow가 현재 요청에 영향을 줄 때 사용한다.

Q. Memory가 Domain Rules를 대체할 수 있는가?

A. 아니다. Memory는 보조 Context이며 Domain Rules와 현재 요청을 우선한다.

Q. 오래된 Memory는 Context에 넣어도 되는가?

A. 권장하지 않는다. Freshness를 확인하고 오래된 Memory는 제외하거나 갱신 후보로 처리한다.

---

# 17. Agent State Context Rules

## 17.1 Agent State Context 구성 규칙

### [개념]

Agent State Context는 현재 Agent Workflow에서 유지되는 작업 상태를 LLM 입력에 포함하는 Context이다.

Agent State는 현재 작업 진행을 위한 임시 정보이며 Long-Term Memory와 구분해야 한다.

---

### [핵심]

Agent State Context 포함 가능 정보:

- taskId
- workflowId
- currentGoal
- taskList
- completedSteps
- pendingSteps
- retrievedContextSummary
- toolCallHistorySummary
- validationResult
- retryCount
- errorState
- nextAction
- finalOutputDraft

State Context 작성 기준:

- 현재 단계에 필요한 정보만 포함
- 장문 Tool History 제외
- 이전 Draft 전체 반복 금지
- 완료 / 미완료 상태 명확화
- 실패 원인 포함
- 다음 Action 포함

---

### [실무]

Agent State Context 예시:

```text
workflowId:
- DOMAIN-RULES-CTX-001

currentGoal:
- Context Engineering Domain Rules 작성

completedSteps:
- 초안 구조 구성
- 기존 Domain Rules 스타일 반영

pendingSteps:
- Retrieval Queries 작성
- 최종 형식 검수
```

Agent State는 Workflow 진행을 돕기 위한 정보이다.

최종 답변에 불필요한 내부 상태를 노출하지 않는다.

---

### [FAQ]

Q. Agent State Context란?

A. 현재 Agent Workflow에서 진행 상황, 완료 단계, 검증 결과, 다음 Action을 나타내는 임시 Context이다.

Q. Agent State와 Long-Term Memory의 차이는?

A. Agent State는 현재 작업 상태이고, Long-Term Memory는 미래 작업에 재사용할 장기 정보이다.

Q. Agent State를 모두 Context에 넣어야 하는가?

A. 아니다. 현재 단계에 필요한 최소 상태만 포함해야 한다.

---

# 18. Long Context Handling Rules

## 18.1 Long Context 처리 규칙

### [개념]

Long Context Handling은 긴 문서, 긴 대화, 많은 검색 결과, 복잡한 Agent State를 LLM Context Window 안에서 안정적으로 처리하는 규칙이다.

Context Window가 커져도 Long Context 품질 문제는 사라지지 않는다.

---

### [핵심]

Long Context 위험:

- 핵심 지시 망각
- 앞부분 정보 손실
- 중간 정보 누락
- 관련 없는 정보에 주의 분산
- 비용 증가
- Latency 증가
- Groundedness 저하
- 출력 형식 위반
- Tool Result 누락
- Memory 충돌 증가

대응 전략:

- Context Selection 강화
- Section Summary 생성
- Hierarchical Context 구성
- 중요 규칙 재배치
- Context Compression
- Chunk Re-Ranking
- Source Priority 적용
- Sliding Window 사용
- Map-Reduce Summary 사용
- Final Validation 수행

---

### [실무]

Long Context 처리 Flow:

```text
Long Context Candidate
→ Topic Segmentation
→ Priority Ranking
→ Section Summary
→ Evidence Selection
→ Compression
→ Final Context Assembly
→ Validation
```

Long Context에서는 핵심 규칙을 처음과 마지막에 명확히 배치한다.

출력 형식, 금지 사항, 사용자 요청은 Context 내에서 묻히지 않게 유지한다.

---

### [FAQ]

Q. Context Window가 크면 Long Context 문제가 해결되는가?

A. 아니다. 긴 Context에서는 핵심 정보 누락, 비용 증가, 지연, 노이즈 문제가 여전히 발생한다.

Q. Long Context에서 가장 중요한 대응은?

A. 관련성 높은 Context만 선택하고, 우선순위를 정하고, 핵심 규칙을 명확히 배치하는 것이다.

Q. 긴 문서를 모두 넣는 것보다 좋은 방법은?

A. Section Summary, Evidence Selection, Context Compression, Hierarchical Context 구성을 사용하는 것이다.

---

# 19. Context Evaluation Rules

## 19.1 Context 품질 평가 규칙

### [개념]

Context Evaluation은 LLM 입력 Context가 현재 요청을 해결하기에 적절한지 평가하는 과정이다.

Context 품질은 최종 답변 품질의 선행 조건이다.

---

### [핵심]

Context Evaluation 항목:

- Context Relevance
- Context Completeness
- Context Precision
- Context Freshness
- Context Consistency
- Context Priority Compliance
- Context Noise Rate
- Context Conflict Rate
- Token Efficiency
- Source Coverage
- Evidence Sufficiency
- Format Instruction Preservation

평가 질문:

- 필요한 근거가 포함되었는가?
- 불필요한 정보가 과도하게 포함되었는가?
- 현재 요청과 직접 관련 있는가?
- 충돌 정보가 제거되었는가?
- 출력 형식 규칙이 유지되었는가?
- Token Budget을 효율적으로 사용했는가?

---

### [실무]

Context Evaluation Checklist:

```md
### [Checklist]

- 현재 요청 해결에 필요한 Context가 포함되었는가?
- 핵심 Domain Rules가 포함되었는가?
- 출력 형식 규칙이 포함되었는가?
- 중복과 노이즈가 제거되었는가?
- 오래된 정보가 제외되었는가?
- 충돌 Context가 해결되었는가?
- Tool Result가 검증되었는가?
- Memory가 현재 요청과 충돌하지 않는가?
- Token Budget이 적절한가?
```

Context Evaluation은 최종 답변 생성 전 수행한다.

Review Agent는 최종 답변뿐 아니라 사용된 Context 품질도 검토할 수 있어야 한다.

---

### [FAQ]

Q. Context Evaluation은 왜 필요한가?

A. 잘못된 Context로는 좋은 모델도 정확한 답변을 만들기 어렵기 때문이다.

Q. Context Relevance란?

A. Context가 현재 사용자 요청과 직접 관련 있는 정도이다.

Q. Context Noise Rate는 무엇인가?

A. 최종 Context 중 현재 요청 해결에 도움이 되지 않는 정보의 비율이다.

---

# 20. Context Observability Rules

## 20.1 Context Trace 작성 규칙

### [개념]

Context Observability는 어떤 Context가 후보로 수집되었고, 어떤 Context가 선택되었으며, 어떤 Context가 제외되었는지 추적하는 구조이다.

AI 시스템의 답변 품질 문제를 분석하려면 Context 구성 과정을 추적해야 한다.

---

### [핵심]

Context Trace 대상:

- contextTraceId
- userRequest
- contextCandidates
- selectedContext
- rejectedContext
- rejectionReason
- sourceType
- sourcePriority
- tokenCount
- compressionApplied
- conflictDetected
- finalContextSnapshot
- outputImpact
- evaluationResult

관측 목적:

- Context 누락 원인 분석
- Noise 증가 원인 분석
- 비용 증가 원인 분석
- Hallucination 원인 분석
- 충돌 Context 확인
- Memory 오용 확인
- Tool Result 누락 확인

---

### [실무]

Context Trace 예시:

```text
contextTraceId: CTX-001
selectedContext:
- Current User Request
- Output Format Rule
- Domain Rules Style
- Project Progress AI Expert List

rejectedContext:
- unrelated project memory

rejectionReason:
- not relevant to current RAG document task

compressionApplied:
- true
```

Context Trace는 원문 전체를 저장하지 않아도 된다.

원인 분석에 필요한 Source, Summary, ID, Token Count, 선택 / 제외 이유를 기록한다.

---

### [FAQ]

Q. Context Observability는 왜 필요한가?

A. 답변 품질 문제의 원인이 Context 누락, 노이즈, 충돌, 잘못된 Memory 사용인지 분석하기 위해 필요하다.

Q. selectedContext와 rejectedContext를 모두 기록해야 하는가?

A. 기록하는 것이 좋다. 왜 특정 Context가 포함되거나 제외되었는지 추적할 수 있기 때문이다.

Q. Context Snapshot은 무엇인가?

A. 최종 LLM 입력에 사용된 Context의 구조화된 기록이다.

---

# 21. Troubleshooting Rules

## 21.1 Context Engineering 장애 대응 작성 규칙

### [개념]

Context Engineering Troubleshooting 문서는 Context 누락, Context 과다, 충돌, Token Overflow, Memory 오용, Tool Result 누락, 출력 형식 위반 같은 문제를 해결하기 위한 규칙이다.

---

### [핵심]

자주 발생하는 문제:

- 핵심 Context 누락
- 관련 없는 Context 과다
- Context Priority 위반
- Token Budget 초과
- 출력 Token 부족
- 오래된 Memory 사용
- Tool Result 미검증
- RAG Chunk 중복
- Graph Path 과다
- Context Conflict 미해결
- Long Context에서 핵심 규칙 누락
- Output Format Instruction 누락
- Safety Instruction 누락
- Groundedness 저하
- Hallucination 증가

---

### [실무]

Troubleshooting 형식:

```md
문제:
최종 답변이 출력 형식을 지키지 않음

원인:

- Output Format Instruction이 Context 뒤쪽에 묻힘
- Retrieved Context가 너무 많아 핵심 지시가 약화됨
- Validation Checklist가 누락됨

해결:

- Output Format Instruction을 높은 우선순위로 배치
- 관련 없는 Retrieved Chunk 제거
- 최종 답변 전 Format Validation 수행
```

문제 / 원인 / 해결 형식을 기본으로 작성한다.

---

### [FAQ]

Q. Context Engineering에서 가장 흔한 실패는?

A. 핵심 Context 누락, 관련 없는 Context 과다, Priority 위반, Token Budget 초과, 충돌 미해결이다.

Q. 답변이 근거 없이 생성되면 무엇을 확인해야 하는가?

A. RAG Context, Source, Context Selection, Groundedness Evaluation, Prompt 지시를 확인해야 한다.

Q. 출력 형식이 자주 깨지면 어떻게 해야 하는가?

A. Output Format Instruction을 높은 우선순위로 배치하고, Context Noise를 줄이며, Format Validation을 수행해야 한다.

---

# 22. Common Mistakes

## 22.1 자주 발생하는 작성 오류

### [개념]

Context Engineering 문서는 “Prompt를 잘 쓰는 방법”만 설명하는 문서가 아니다.

Agent가 Context Source를 선택하고, 우선순위를 정하고, 충돌을 해결하고, Token Budget을 관리하고, 최종 Context를 검증할 수 있도록 작성해야 한다.

---

### [핵심]

금지 또는 주의:

- Prompt Engineering과 동일하게 설명
- Context Source 구분 누락
- Context Priority 누락
- Context Selection 기준 누락
- Context Assembly 기준 누락
- Token Budget 기준 누락
- Context Compression 기준 누락
- Context Conflict 기준 누락
- Context Noise 제거 기준 누락
- RAG Context 기준 누락
- Tool Result 검증 누락
- Memory Context 기준 누락
- Agent State와 Memory 혼동
- Long Context 문제 누락
- Context Evaluation 누락
- Context Observability 누락
- Troubleshooting 누락
- 장문 이론 설명 중심 작성
- Retrieval Queries 누락

---

### [실무]

나쁜 문서 예시:

```text
Context Engineering은 좋은 Prompt와 많은 정보를 넣어서 모델이 답변을 잘하게 만드는 것이다.
```

좋은 문서 예시:

```text
Context Engineering은 사용자 요청, 규칙, RAG 검색 결과, Tool Result, Memory, Agent State를 선택 / 정렬 / 압축 / 검증해 LLM 입력 Context로 구성하는 과정이다.

Flow:
Context Candidate 수집
→ Priority 적용
→ Relevance 평가
→ Conflict 제거
→ Compression
→ Context Assembly
→ Validation
```

---

### [FAQ]

Q. Context Engineering 문서에서 가장 피해야 할 것은?

A. Prompt 작성법만 설명하고 Context 선택, 우선순위, 충돌, Token Budget, 검증 기준을 누락하는 것이다.

Q. Context를 많이 넣으면 좋은 문서인가?

A. 아니다. 필요한 Context를 정확히 선택하고 노이즈를 줄이는 것이 중요하다.

Q. Context Engineering과 Memory를 혼동하면 어떤 문제가 생기는가?

A. 오래된 Memory나 사용자 선호가 현재 요청이나 Domain Rules보다 우선되는 오류가 발생할 수 있다.

---

# 23. Document Split Rules

## 23.1 Context Engineering 문서 분할 기준

### [개념]

Context Engineering은 Context Source, Priority, Selection, Assembly, Compression, RAG Context, Tool Result, Memory, Evaluation 범위가 넓기 때문에 Part 단위로 분리한다.

각 Part는 독립 검색 가능해야 하며, 하나의 Part는 하나의 핵심 주제를 다룬다.

---

### [핵심]

권장 문서 분할:

```text
Context_Engineering_Part01_Core.md
Context_Engineering_Part02_Context_Source_Priority.md
Context_Engineering_Part03_Context_Selection_Assembly.md
Context_Engineering_Part04_Token_Budget_Compression.md
Context_Engineering_Part05_Context_Conflict_Noise.md
Context_Engineering_Part06_RAG_Graph_Context.md
Context_Engineering_Part07_Tool_Memory_Agent_State_Context.md
Context_Engineering_Part08_Long_Context_Evaluation.md
Context_Engineering_Part09_Observability_Troubleshooting.md
```

분할 기준:

- 하나의 Part는 하나의 핵심 주제
- Source와 Priority는 함께 작성 가능
- Selection과 Assembly는 함께 작성 권장
- Token Budget과 Compression은 함께 작성 권장
- Conflict와 Noise는 함께 작성 권장
- RAG Context와 Graph Context는 연결 문서로 작성
- Tool / Memory / Agent State Context는 함께 작성 가능
- Evaluation과 Observability는 반드시 포함
- Troubleshooting은 문제 / 원인 / 해결 형식
- 각 Part는 FAQ 포함
- 각 Part는 Retrieval Queries 포함

---

### [실무]

Context Engineering 문서 Set은 AI Expert Level과 Agentic RAG / RAGOps / AgentOps에서 사용한다.

AI/ML Agent는 Context 설계와 평가 기준을 참조하고, Review Agent는 Context 누락, 충돌, Groundedness 저하를 검토한다.

특정 구현 도구는 별도 문서로 분리한다.

예:

```text
Context_Engineering_Domain_Rules.md
RAG_Context_Selection_Part.md
Long_Context_Optimization_Part.md
Prompt_Context_Template_Part.md
Agent_State_Context_Part.md
```

---

### [FAQ]

Q. Context Engineering 문서는 몇 개 Part로 나누는 것이 좋은가?

A. 8~9개 Part를 권장한다. Core, Source/Priority, Selection/Assembly, Token/Compression, Conflict/Noise, RAG/Graph, Tool/Memory/State, Evaluation, Observability/Troubleshooting으로 분리한다.

Q. Prompt Engineering 문서와 합쳐도 되는가?

A. 권장하지 않는다. Prompt Engineering은 지시문 중심이고 Context Engineering은 입력 정보 전체 구성과 검증 중심이다.

Q. 각 Part에도 Retrieval Queries가 필요한가?

A. 필요하다. 각 문서가 독립 검색될 수 있어야 한다.

---

# 24. Agent Usage Rules

## 24.1 Agent별 사용 기준

### [개념]

Context Engineering Domain Rules는 여러 Agent가 LLM 입력 Context를 동일한 기준으로 구성하고 검증하도록 돕는다.

각 Agent는 자신의 역할에 맞는 Context Engineering Chunk를 우선 검색한다.

---

### [핵심]

PM Agent:

- 사용자 요청에서 필요한 Context 범위 판단
- Context Priority 적용
- Agent별 Context 분배
- Output Format Context 유지
- 최종 통합 Context 검토

AI/ML Agent:

- Context Selection 전략 설계
- RAG / Graph Context 구성
- Token Budget / Compression 설계
- Context Evaluation 기준 설계
- Long Context Handling 설계

Backend Agent:

- Context Assembly Pipeline 구현
- RAG Context API 구현
- Tool Result Context 저장
- Context Trace 저장
- Token Count 관리 구현

DevOps Agent:

- Context Observability 운영
- Token / Cost / Latency 모니터링
- Long Context 비용 관리
- Context Pipeline 장애 대응

Review Agent:

- Context 누락 검토
- Context 충돌 검토
- Context Noise 검토
- Groundedness 검토
- Output Format Context 반영 여부 검토

Architecture Review Agent:

- Context Pipeline 구조 검토
- RAG / Memory / Tool / Agent State 경계 검토
- 확장성 검토
- 비용 / 품질 Trade-off 검토

---

### [실무]

Agent별 검색 우선순위:

```text
PM Agent
→ Context Priority / Context Source / Output Format Context

AI/ML Agent
→ Context Selection / Compression / RAG Context / Long Context

Backend Agent
→ Context Assembly / Token Budget / Context Trace / API Integration

DevOps Agent
→ Context Observability / Cost / Latency / Pipeline Stability

Review Agent
→ Context Evaluation / Conflict / Noise / Groundedness

Architecture Review Agent
→ Context Architecture / Memory Boundary / RAG Pipeline / Scalability
```

Context Engineering은 AI/ML Agent 단독 영역이 아니다.

Backend Agent는 Pipeline 구현을 담당하고, Review Agent는 Context 품질을 검증하며, DevOps Agent는 비용과 관측 가능성을 관리한다.

---

### [FAQ]

Q. Context Engineering Domain Rules는 어떤 Agent가 사용하는가?

A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.

Q. Review Agent는 Context Engineering에서 무엇을 검토해야 하는가?

A. Context 누락, 충돌, 노이즈, Groundedness, 출력 형식 지시 반영 여부를 검토해야 한다.

Q. Backend Agent는 Context Engineering에서 무엇을 구현해야 하는가?

A. Context Assembly Pipeline, Token Count, RAG Context API, Tool Result Context, Context Trace 저장을 구현한다.

---

# 25. Final Goal

## 25.1 최종 목표

### [개념]

Context Engineering Domain Rules의 최종 목표는 Agent가 LLM 입력 Context를 목적에 맞게 선택, 정렬, 압축, 검증하여 정확하고 근거 있는 답변을 생성할 수 있도록 문서 제작 기준을 제공하는 것이다.

---

### [핵심]

최종 목표:

- Context Engineering 개념 검색 가능
- Prompt Engineering과 구분 가능
- Context Source 분류 가능
- Context Priority 적용 가능
- Context Selection 가능
- Context Assembly 가능
- Token Budget 관리 가능
- Context Compression 가능
- Context Conflict 해결 가능
- Context Noise 제거 가능
- RAG Context 구성 가능
- Graph Context 구성 가능
- Tool Result Context 구성 가능
- Memory Context 구성 가능
- Agent State Context 구성 가능
- Long Context Handling 가능
- Context Evaluation 가능
- Context Observability 가능
- Troubleshooting 가능

---

### [실무]

Context Engineering RAG Doc Set은 다음 작업을 지원해야 한다.

```text
User Request
→ Context Need Check
→ Context Source 수집
→ Priority 적용
→ Relevant Context 선택
→ Conflict / Noise 제거
→ Token Budget 확인
→ Compression
→ Context Assembly
→ LLM Output 생성
→ Context Evaluation
→ Review Agent 검토
```

문서 품질은 Agent가 필요한 Context만 선택하고, 충돌과 노이즈를 제거하고, Token Budget 안에서 근거 기반 답변을 만들 수 있는지로 결정된다.

---

### [FAQ]

Q. Context Engineering Domain Rules의 최종 목적은?

A. Agent가 LLM 입력 Context를 선택, 정렬, 압축, 검증해 정확하고 근거 있는 답변을 만들 수 있도록 문서 제작 기준을 제공하는 것이다.

Q. 이 문서는 사람 학습용인가?

A. 아니다. AI Agent Retrieval과 Context 구성 품질을 높이기 위한 문서이다.

Q. Context Engineering 문서 품질은 무엇으로 판단하는가?

A. Agent가 Context Source를 구분하고, 우선순위를 적용하고, 충돌과 노이즈를 제거해 최종 답변 품질을 높일 수 있는지로 판단한다.

---

# Retrieval Queries

### [FAQ]

Q. Context Engineering이란?
A. LLM 입력에 포함할 지시문, 검색 결과, Tool Result, Memory, Agent State를 선택, 정렬, 압축, 검증하는 작업이다.

Q. Context Engineering과 Prompt Engineering의 차이는?
A. Prompt Engineering은 지시문 작성 중심이고, Context Engineering은 입력 정보 전체의 선택, 구성, 압축, 검증까지 포함한다.

Q. Context Source란?
A. LLM 입력 Context를 구성할 때 사용할 수 있는 지시문, 문서, 검색 결과, Tool Result, Memory, Agent State 같은 정보 출처이다.

Q. Context Priority란?
A. 여러 Context Source가 충돌하거나 동시에 존재할 때 어떤 정보를 우선 적용할지 정하는 규칙이다.

Q. Context Priority 기본 순서는?
A. System Instruction → Current User Request → Master RAG Rules → Domain Rules → Project Progress → Retrieved Source → Tool Result → Long-Term Memory 순서이다.

Q. Context Selection이란?
A. Context 후보 중 현재 요청 해결에 필요한 정보만 선택하는 과정이다.

Q. Context Assembly란?
A. 선택된 Context를 LLM이 잘 사용할 수 있도록 순서와 구조를 정해 입력으로 조립하는 과정이다.

Q. Token Budget이란?
A. LLM 입력과 출력에 사용할 수 있는 Token 한도이며 Context 구성 시 반드시 고려해야 하는 제약이다.

Q. Context Compression이란?
A. 의미와 핵심 근거를 유지하면서 Context Token 수를 줄이는 과정이다.

Q. Context Compression 시 보존해야 할 것은?
A. Source, 조건, 예외, 숫자, 날짜, 버전, 코드, 명령어, 사용자 제약, 출력 형식 규칙이다.

Q. Context Conflict란?
A. 입력 Context 안의 지시, 문서, Memory, Tool Result가 서로 다른 내용을 말하는 상황이다.

Q. Context Conflict가 발생하면 어떻게 해야 하는가?
A. Context Priority에 따라 우선순위를 적용하고 낮은 우선순위 Context를 제외하거나 불확실성을 표시한다.

Q. Context Noise란?
A. 현재 요청 해결에 직접 도움이 되지 않거나 답변 품질을 방해하는 입력 정보이다.

Q. RAG Context란?
A. 검색된 문서 Chunk 중 최종 LLM 입력에 포함되어 답변 근거로 사용되는 Context이다.

Q. Graph Context란?
A. Graph Search 결과를 Entity, Relation, Path, Evidence 중심으로 정리한 Context이다.

Q. Tool Result Context란?
A. 도구 호출 결과를 다음 LLM 입력이나 Agent 단계에서 사용할 수 있도록 정리한 Context이다.

Q. Memory Context란?
A. Long-Term Memory 또는 Short-Term Memory에서 현재 요청에 필요한 정보만 선택해 포함하는 Context이다.

Q. Agent State Context란?
A. 현재 Agent Workflow의 진행 상태, 완료 단계, 검증 결과, 다음 Action을 나타내는 임시 Context이다.

Q. Long Context Handling이란?
A. 긴 문서, 많은 검색 결과, 복잡한 Agent State를 Context Window 안에서 안정적으로 처리하는 규칙이다.

Q. Context Evaluation이란?
A. LLM 입력 Context가 현재 요청 해결에 적절한지 관련성, 완전성, 최신성, 충돌 여부, Token 효율성 기준으로 평가하는 과정이다.

Q. Context Observability란?
A. 어떤 Context가 후보로 수집되고, 선택되고, 제외되었는지 추적하는 구조이다.

Q. Context Snapshot이란?
A. 최종 LLM 입력에 사용된 Context의 구조화된 기록이다.

Q. Context Engineering에서 흔한 실패는?
A. 핵심 Context 누락, 관련 없는 Context 과다, Priority 위반, Token Budget 초과, 충돌 미해결이다.

Q. Context Engineering 문서 분할은 어떻게 하는가?
A. Core, Source/Priority, Selection/Assembly, Token/Compression, Conflict/Noise, RAG/Graph, Tool/Memory/State, Evaluation, Observability/Troubleshooting으로 분리한다.

Q. Context Engineering 문서에서 피해야 할 것은?
A. Prompt 작성법만 설명하고 Context 선택, 우선순위, 충돌, Token Budget, 검증 기준을 누락하는 것이다.

Q. Context Engineering Domain Rules는 어떤 Agent가 사용하는가?
A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.
