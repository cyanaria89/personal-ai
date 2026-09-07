# Agent Evaluation & Guardrails Part08 - RAG & Memory Guardrails

---

# 1. RAG Guardrails

## 1.1 RAG Guardrails Core

### [개념]

RAG Guardrails는 Agent가 Retrieved Context와 RAG 문서를 우선 사용하고, 근거 없는 프로젝트 고유 정보를 생성하지 않도록 제한하는 규칙이다.

RAG Guardrails는 Grounding Evaluation 자체를 반복 설명하는 문서가 아니다.

RAG Guardrails의 초점은 **RAG 기반 답변을 생성할 때 지켜야 하는 제한 규칙과 안전한 답변 조건**이다.

RAG Guardrails는 다음 문제를 방지한다.

- 문서에 없는 API 생성
- 문서에 없는 클래스 / 메서드 생성
- Retrieved Context 왜곡
- Citation 오용
- Unsupported Claim 생성
- Missing Information 은폐
- 오래된 Memory와 문서 충돌 무시
- 일반 지식으로 프로젝트 고유 사실 확정

---

### [핵심]

RAG Guardrails 핵심 원칙:

- Retrieved Context를 우선 사용한다.
- Project-specific Fact는 Evidence가 있어야 한다.
- 문서에 없는 API / 파일 / 클래스 / 메서드를 만들지 않는다.
- Unsupported Claim은 제거한다.
- Context가 부족하면 Missing Information으로 표시한다.
- Assumption은 사실과 분리한다.
- Citation은 실제 Claim을 뒷받침해야 한다.
- 문서 간 충돌이 있으면 Source Priority를 적용한다.
- Memory는 RAG Context보다 우선하지 않는다.
- Final Output 전 Claim-Evidence Check를 수행한다.

RAG Guardrail Flow:

```text
User Query
→ Retrieve Context
→ Check Context Sufficiency
→ Draft Answer from Context
→ Remove Unsupported Claim
→ Mark Missing Information
→ Apply Source Priority
→ Final Output
```

RAG 답변 판단:

| 상태                | 의미           | 처리                      |
| ------------------- | -------------- | ------------------------- |
| Supported           | 문서 근거 있음 | 답변 가능                 |
| Partially Supported | 일부 근거 있음 | 범위 제한 답변            |
| Unsupported         | 근거 없음      | 제거 또는 Assumption 처리 |
| Conflicting         | 문서 간 충돌   | Source Priority 적용      |
| Insufficient        | 핵심 정보 부족 | Missing Information 표시  |

---

### [실무]

개인 AI 개발팀 구조에서 RAG Guardrails는 PM Agent, Backend Agent, Frontend Agent, Review Agent, DevOps Agent, AI/ML Agent 모두에 적용된다.

실무 적용 예시:

```text
User Query:
NotificationRepository에 읽지 않은 알림 조회 메서드가 뭐야?

Retrieved Context:
countByUsers_UserIdAndReadStatusFalse(Long userId)

Allowed:
읽지 않은 알림 개수 조회는 countByUsers_UserIdAndReadStatusFalse(Long userId)를 사용한다.

Blocked:
findUnreadByUserId()를 사용한다.

Reason:
findUnreadByUserId()는 Retrieved Context에 없음.
```

RAG 답변 생성 기준:

```text
1. 질문에 필요한 Domain 문서를 찾는다.
2. Retrieved Context가 충분한지 확인한다.
3. 프로젝트 고유 Claim을 Evidence와 연결한다.
4. 문서에 없는 Claim은 제거한다.
5. 근거가 약한 내용은 Assumption으로 표시한다.
6. 부족한 정보는 Missing Information으로 남긴다.
7. Final Output에서 확정 표현을 조절한다.
```

RAG Guardrail Report 예시:

```md
| Claim                      | Evidence            | Status      | Handling  |
| -------------------------- | ------------------- | ----------- | --------- |
| Retrieval Queries 필수     | Master Rules        | Supported   | 유지      |
| High Risk 작업 승인 필요   | Domain Rules        | Supported   | 유지      |
| findUnreadByUserId 존재    | Evidence 없음       | Unsupported | 제거      |
| Agent Evaluation 완료 상태 | 현재 작성 흐름 기준 | Partial     | 표현 제한 |
```

---

### [주의]

RAG Guardrails 주의사항:

- 검색된 Chunk가 있어도 Claim과 직접 연결되지 않으면 근거가 아니다.
- 문서 제목만 보고 내용을 확정하지 않는다.
- 일반 개발 지식으로 프로젝트 고유 사실을 보완하지 않는다.
- Citation이 있어도 Wrong Citation일 수 있다.
- 문서에 없는 API, 클래스, 메서드를 만들지 않는다.
- Context가 부족하면 부족하다고 말해야 한다.
- Retrieval Failure를 정보 부재로 단정하지 않는다.
- Memory가 문서보다 오래되었으면 RAG Context를 우선한다.

---

### [Best Practice]

RAG Guardrails Best Practice:

- 주요 Claim을 문장 단위로 분리한다.
- Project-specific Claim을 우선 검증한다.
- Claim-Evidence 매핑을 사용한다.
- Unsupported Claim은 제거한다.
- Weak Evidence는 Assumption으로 낮춘다.
- Missing Information을 숨기지 않는다.
- Source Priority를 적용한다.
- RAG 문서 자체에는 FAQ와 Retrieval Queries를 강화한다.
- Final Output 전 RAG Guardrails Checklist를 적용한다.

---

### [FAQ]

Q. RAG Guardrails가 뭐야?
A. Agent가 Retrieved Context와 RAG 문서를 우선 사용하고 근거 없는 답변을 하지 않도록 제한하는 규칙이다.

Q. RAG Guardrails는 Grounding Evaluation과 같아?
A. 아니다. Grounding Evaluation은 평가 기준이고, RAG Guardrails는 답변 생성 시 지켜야 하는 제한 규칙이다.

Q. Retrieved Context가 있으면 무조건 답해도 돼?
A. 아니다. Retrieved Context가 Claim을 직접 뒷받침하는지 확인해야 한다.

Q. 문서에 없는 프로젝트 정보를 일반 지식으로 보완해도 돼?
A. 안 된다. 프로젝트 고유 정보는 Retrieved Context나 Tool Result에 근거해야 한다.

Q. 근거가 부족하면 어떻게 해?
A. Missing Information으로 표시하거나 Assumption으로 낮춰 표현해야 한다.

---

# 2. Context Sufficiency Rule

## 2.1 Retrieved Context Sufficiency

### [개념]

Context Sufficiency Rule은 검색된 RAG Context가 사용자 질문에 답하기에 충분한지 판단하는 규칙이다.

RAG 검색 결과가 있다고 해서 답변이 가능한 것은 아니다.

Context가 부족한 상태에서 확정 답변을 만들면 Hallucination이 발생한다.

---

### [핵심]

Context Sufficiency 판단 기준:

| 기준         | 설명                                        |
| ------------ | ------------------------------------------- |
| Relevance    | 질문과 직접 관련 있는가                     |
| Sufficiency  | 답변에 필요한 정보가 충분한가               |
| Specificity  | 프로젝트 고유 사실을 검증할 만큼 구체적인가 |
| Completeness | 조건, 예외, 범위를 포함하는가               |
| Consistency  | 다른 문서와 충돌하지 않는가                 |
| Authority    | 우선순위 높은 문서인가                      |
| Freshness    | 현재 상태와 맞는가                          |

Context Sufficiency Flow:

```text
Retrieved Context
→ Relevance Check
→ Sufficiency Check
→ Specificity Check
→ Conflict Check
→ Sufficient / Partial / Insufficient
```

Context 상태:

```text
Sufficient:
- 직접 답변 가능
- 주요 Claim 근거 있음

Partial:
- 일부 답변 가능
- 한계 표시 필요

Insufficient:
- 핵심 정보 부족
- 확정 답변 불가
```

---

### [실무]

충분한 Context 예시:

```text
Question:
Tool Calling Evaluation에서 검증해야 할 항목은?

Context:
Tool Choice, Arguments, Permission, Risk Level, Execution Status, Result Validation 문서 존재

Decision:
Sufficient
```

부분 Context 예시:

```text
Question:
현재 프로젝트 UserService에 Transaction 누락이 있어?

Context:
Backend Code Evaluation 기준만 있음.
실제 UserService 코드 없음.

Decision:
Partial 또는 Insufficient

Safe Answer:
제공된 기준상 Transaction Boundary를 검토해야 한다.
하지만 실제 UserService 코드가 없어 누락 여부는 확정할 수 없다.
```

Context Sufficiency Report 예시:

```md
| Query                  | Context Status | Handling                        |
| ---------------------- | -------------- | ------------------------------- |
| Agent Evaluation 기준  | Sufficient     | 답변 가능                       |
| 특정 Service 코드 결함 | Insufficient   | 코드 필요                       |
| 문서 작성 규칙         | Sufficient     | Master / Domain Rules 기준 답변 |
```

---

### [주의]

Context Sufficiency 주의사항:

- 관련 키워드가 있다고 충분한 Context는 아니다.
- 일반 기준 문서만으로 실제 코드 결함을 확정하지 않는다.
- 검색 결과 없음은 문서 부재와 다를 수 있다.
- Partial Context는 부분 답변만 가능하다.
- Insufficient 상태에서 확정 표현을 쓰면 Hallucination이다.
- Context 충돌은 Source Priority 없이 임의 판단하지 않는다.

---

### [Best Practice]

Context Sufficiency Best Practice:

- 질문에 필요한 Evidence 유형을 먼저 정한다.
- Retrieved Context가 Evidence를 제공하는지 확인한다.
- Sufficient / Partial / Insufficient로 구분한다.
- Partial이면 가능한 범위만 답한다.
- Insufficient이면 Missing Information을 표시한다.
- 프로젝트 고유 정보는 실제 문서, 코드, Tool Result를 우선한다.
- 충돌하는 Context는 Source Priority로 해결한다.

---

### [FAQ]

Q. Context Sufficiency Rule이 뭐야?
A. 검색된 RAG Context가 사용자 질문에 답하기에 충분한지 판단하는 규칙이다.

Q. 검색 결과가 있으면 바로 답해도 돼?
A. 아니다. 검색 결과가 질문에 직접 답할 만큼 충분한지 확인해야 한다.

Q. Partial Context는 어떻게 처리해?
A. 가능한 범위만 답하고 부족한 정보와 한계를 명확히 표시해야 한다.

Q. Insufficient Context에서 답하면 어떻게 돼?
A. 근거 없는 답변이나 Hallucination이 발생할 수 있다.

Q. 실제 코드 결함을 판단하려면 뭐가 필요해?
A. 일반 기준이 아니라 실제 코드, 파일, Tool Result 같은 직접 근거가 필요하다.

---

# 3. Source Priority

## 3.1 Source Priority Rule

### [개념]

Source Priority는 RAG Context, Memory, Project Progress, Domain Rules, Tool Result가 서로 충돌할 때 어떤 근거를 우선할지 정하는 규칙이다.

Agent는 충돌하는 정보를 임의로 섞으면 안 된다.

Source Priority는 RAG Guardrails와 Memory Guardrails를 연결하는 핵심 기준이다.

---

### [핵심]

기본 Source Priority:

```text
1. Current User Request
2. Current Conversation Output / Current Work State
3. Current Uploaded File / Retrieved Context
4. Tool Result
5. Project Progress Document
6. Domain Rules
7. Master Rules
8. Recent Verified Memory
9. General Knowledge
10. Old Memory
```

우선순위 적용 원칙:

| 충돌 상황                         | 우선 기준              |
| --------------------------------- | ---------------------- |
| 현재 요청 vs Memory               | 현재 요청              |
| 현재 작업 결과 vs 오래된 Progress | 현재 작업 결과         |
| 업로드 문서 vs Memory             | 업로드 문서            |
| Tool Result vs 추측               | Tool Result            |
| Project Progress vs 오래된 Memory | Project Progress       |
| Domain Rules vs 일반 관례         | Domain Rules           |
| Master Rules vs Domain Rules      | Master → Domain → Part |
| 근거 불충분                       | Missing Information    |

Source Priority Flow:

```text
Detect Conflict
→ Identify Sources
→ Compare Priority
→ Select Higher Priority Source
→ Mark Conflict if Needed
→ Answer with Limited Confidence
```

---

### [실무]

예시:

```text
Current User Request:
중간 응답 금지, 결과만 출력

General Preference:
작업 중 진행상황 공유

Decision:
Current User Request 우선
중간 응답 금지
```

예시:

```text
Project Progress:
Agent Evaluation & Guardrails Planned

Current Conversation:
Part01~Part08 작성 완료 중

Decision:
Current Work State 우선
현재 작성 진행 상태로 처리
```

예시:

```text
Memory:
Open WebUI 사용 계획

Current Project Context:
AnythingLLM 사용 중

Decision:
현재 프로젝트 상태 우선
Open WebUI는 과거 계획으로만 처리
```

Source Priority Report 예시:

```md
| Conflict              | Higher Priority Source  | Decision       |
| --------------------- | ----------------------- | -------------- |
| 중간 응답 여부        | Current User Request    | 중간 응답 금지 |
| Agent Evaluation 상태 | Current Work State      | 작성 진행 기준 |
| FAQ 개수              | Domain Rules            | FAQ 강화       |
| Open WebUI 현재 사용  | Current Project Context | 사용하지 않음  |
```

---

### [주의]

Source Priority 주의사항:

- 오래된 Memory를 현재 문서보다 우선하지 않는다.
- 현재 사용자 요청은 이전 선호보다 우선한다.
- 일반 지식으로 Domain Rules를 덮어쓰지 않는다.
- 현재 작업 결과가 Project Progress보다 최신일 수 있다.
- Tool Result가 실패한 경우 성공 근거로 쓰면 안 된다.
- 충돌을 숨기고 임의로 결론내면 Faithfulness가 낮아진다.
- 우선순위로 해결되지 않으면 Missing Information 또는 Ask로 처리한다.

---

### [Best Practice]

Source Priority Best Practice:

- 충돌이 의심되면 Source를 분리한다.
- 우선순위 높은 Source를 기준으로 판단한다.
- 낮은 우선순위 Source는 보조 정보로만 사용한다.
- 충돌 해결 근거를 간단히 기록한다.
- 프로젝트 진행 상태는 최신 작업 결과와 Project Progress를 함께 확인한다.
- 문서 작성 규칙은 Master Rules와 Domain Rules를 우선한다.
- 현재 사용자 출력 형식 지시는 항상 반영한다.

---

### [FAQ]

Q. Source Priority가 뭐야?
A. 여러 정보가 충돌할 때 어떤 근거를 우선할지 정하는 규칙이다.

Q. 현재 사용자 요청과 Memory가 충돌하면 무엇을 우선해?
A. 현재 사용자 요청을 우선해야 한다.

Q. 현재 작업 결과와 Project Progress가 충돌하면 어떻게 해?
A. 현재 작업 결과가 더 최신일 수 있으므로 현재 작업 상태를 우선하거나 충돌을 표시한다.

Q. Domain Rules와 일반 지식이 충돌하면 무엇을 우선해?
A. Domain Rules를 우선해야 한다.

Q. 충돌이 해결되지 않으면 어떻게 해?
A. Missing Information으로 표시하거나 사용자 확인이 필요하다.

---

# 4. Memory Guardrails

## 4.1 Memory Guardrails Core

### [개념]

Memory Guardrails는 Agent가 Memory를 사용할 때 최신성, 관련성, 프로젝트 경계, 민감정보 여부를 검증하도록 제한하는 규칙이다.

Memory는 RAG 문서와 Tool Result를 대체하지 않는다.

Memory는 현재 작업을 보조하는 맥락 정보다.

Memory Guardrails는 다음 문제를 방지한다.

- 오래된 기술 스택 사용
- 다른 프로젝트 정보 혼입
- 현재 사용자 요청 무시
- 현재 문서보다 Memory 우선
- 민감정보 저장
- Secret 저장
- Memory 기반 프로젝트 고유 사실 생성
- 사용자의 Forget 요청 무시

---

### [핵심]

Memory 사용 전 검증 항목:

| 항목             | 설명                                 |
| ---------------- | ------------------------------------ |
| Relevance        | 현재 요청과 관련 있는가              |
| Recency          | 최신 정보인가                        |
| Conflict         | 현재 요청이나 문서와 충돌하지 않는가 |
| Project Boundary | 같은 프로젝트 정보인가               |
| Sensitivity      | 민감정보인가                         |
| Secret           | API Key, Token, Password인가         |
| User Correction  | 사용자가 정정했는가                  |
| Forget Request   | 삭제 요청이 있었는가                 |

Memory Guardrail Flow:

```text
Memory Candidate
→ Relevance Check
→ Recency Check
→ Conflict Check
→ Project Boundary Check
→ Sensitive / Secret Check
→ Use / Ignore / Ask / Forget
```

Memory 처리 결과:

| 결과   | 의미                                        |
| ------ | ------------------------------------------- |
| Use    | 관련 있고 최신이며 충돌 없음                |
| Ignore | 관련 없거나 오래되었거나 프로젝트 범위 다름 |
| Ask    | 충돌이 있고 확인 필요                       |
| Update | 사용자가 정정하거나 장기 정보 갱신 필요     |
| Forget | 사용자가 삭제 요청                          |
| Block  | Secret 또는 저장 금지 정보                  |

---

### [실무]

Memory 사용 예시:

```text
Memory:
사용자는 개인 AI 프로젝트에서 AnythingLLM, Ollama, Qwen2.5, BGE-M3를 사용한다.

Current Request:
Agent Evaluation & Guardrails RAG 문서 작성

Decision:
Use

Reason:
- 같은 프로젝트
- 현재 맥락과 관련 있음
```

Memory 무시 예시:

```text
Memory:
Open WebUI + ComfyUI 사용 계획

Current Context:
AnythingLLM 기반으로 진행 중

Decision:
Ignore 또는 과거 기록으로만 처리

Reason:
- 현재 상태와 충돌 가능
```

Project Boundary 예시:

```text
Memory:
FestaPick 프로젝트의 FestivalController API

Current Request:
개인 AI 프로젝트 Agent 문서 작성

Decision:
Ignore

Reason:
- 다른 프로젝트 정보
```

Memory Guardrail Report 예시:

```md
| Memory               | Relevance    | Conflict         | Decision |
| -------------------- | ------------ | ---------------- | -------- |
| AnythingLLM 사용     | Relevant     | 없음             | Use      |
| Open WebUI 현재 사용 | Relevant     | 현재 상태와 충돌 | Ignore   |
| FestaPick API        | Not Relevant | 프로젝트 다름    | Ignore   |
| API Key 값           | Sensitive    | Secret           | Block    |
```

---

### [주의]

Memory Guardrails 주의사항:

- Memory는 항상 최신이 아니다.
- 현재 사용자 요청은 Memory보다 우선한다.
- 현재 문서와 Retrieved Context는 Memory보다 우선한다.
- 다른 프로젝트 Memory를 현재 프로젝트에 섞지 않는다.
- 오래된 계획을 현재 사실처럼 말하지 않는다.
- Memory만으로 프로젝트 고유 API / 클래스 / 파일을 확정하지 않는다.
- Secret은 Memory에 저장하지 않는다.
- Forget 요청은 무시하지 않는다.

---

### [Best Practice]

Memory Guardrails Best Practice:

- Memory 사용 전 Relevance와 Recency를 확인한다.
- 현재 요청과 현재 문서를 우선한다.
- 프로젝트 경계를 확인한다.
- 충돌 Memory는 사용하지 않는다.
- 오래된 Memory는 현재 사실로 확정하지 않는다.
- 사용자 정정은 우선 적용한다.
- Secret과 민감정보는 저장하지 않는다.
- Memory를 근거로 사용할 때 확정 표현을 피한다.
- 프로젝트 상태는 Project Progress 또는 현재 작업 결과를 우선한다.

---

### [FAQ]

Q. Memory Guardrails가 뭐야?
A. Agent가 Memory를 사용할 때 최신성, 관련성, 프로젝트 경계, 민감정보 여부를 검증하도록 제한하는 규칙이다.

Q. Memory는 RAG 문서보다 우선해?
A. 아니다. Memory는 보조 맥락이며 현재 문서와 Retrieved Context가 우선이다.

Q. Memory와 현재 요청이 충돌하면 무엇을 우선해?
A. 현재 사용자 요청을 우선해야 한다.

Q. 다른 프로젝트 Memory를 현재 프로젝트에 써도 돼?
A. 안 된다. 프로젝트 경계를 지켜야 한다.

Q. Secret을 Memory에 저장해도 돼?
A. 안 된다. API Key, Token, Password 같은 Secret은 저장하면 안 된다.

---

# 5. Recency & Project Boundary

## 5.1 Recency Check

### [개념]

Recency Check는 Memory나 Context가 현재 시점과 현재 프로젝트 상태에 맞는지 확인하는 규칙이다.

Project Boundary Check는 다른 프로젝트의 정보를 현재 프로젝트에 섞지 않도록 확인하는 규칙이다.

이 두 규칙은 Memory Guardrails의 핵심이다.

---

### [핵심]

Recency Check 기준:

| 기준               | 설명                                   |
| ------------------ | -------------------------------------- |
| Current Request    | 현재 사용자가 새로 지시했는가          |
| Current Work State | 현재 대화에서 새로 생성한 결과인가     |
| Current File       | 현재 업로드 / 검색된 문서인가          |
| Project Progress   | 진행 상태 문서와 일치하는가            |
| Tool Result        | 방금 실행한 결과인가                   |
| Old Memory         | 과거 대화 기반 정보인가                |
| Stale Status       | 완료 / 진행 / 예정 상태가 오래되었는가 |

Project Boundary Check 기준:

| 기준               | 설명                        |
| ------------------ | --------------------------- |
| Project Name       | 같은 프로젝트인가           |
| Domain             | 같은 Domain 문서인가        |
| Tech Stack         | 현재 프로젝트 기술 스택인가 |
| API / Class        | 현재 프로젝트 소속인가      |
| User Scope         | 현재 요청 범위 안인가       |
| Conversation Scope | 현재 채팅 목적과 일치하는가 |

Recency & Boundary Flow:

```text
Candidate Information
→ Recency Check
→ Project Boundary Check
→ Conflict Check
→ Fresh / Stale / Out of Scope / Unknown
```

---

### [실무]

Recency 예시:

```text
Old Memory:
Open WebUI를 사용한다.

Current Context:
AnythingLLM 사용 중.

Decision:
Stale
현재 답변에서는 AnythingLLM 기준 사용
```

Current Work State 예시:

```text
Project Progress:
Agent Evaluation & Guardrails Planned

Current Conversation:
Part01~Part08 재작업 진행 중

Decision:
현재 작업 상태가 더 최신일 수 있음
문서 상태는 작성 진행 기준으로 처리
```

Project Boundary 예시:

```text
FestaPick:
Spring Boot FestivalController API

Personal AI Project:
Agent Evaluation RAG 문서

Decision:
Out of Scope
현재 문서에 섞지 않음
```

Recency / Boundary Report 예시:

```md
| Information       | Source                  | Status       | Decision |
| ----------------- | ----------------------- | ------------ | -------- |
| AnythingLLM 사용  | Current Project Context | Fresh        | Use      |
| ComfyUI 현재 사용 | Old Memory              | Stale        | Ignore   |
| FestaPick API     | Other Project           | Out of Scope | Ignore   |
| Part08 작성 상태  | Current Work            | Fresh        | Use      |
```

---

### [주의]

Recency & Boundary 주의사항:

- 오래된 Memory를 최신 사실처럼 쓰지 않는다.
- 현재 작업 결과는 Project Progress보다 최신일 수 있다.
- Project Progress가 아직 업데이트되지 않았을 수 있다.
- 다른 프로젝트 API나 규칙을 현재 프로젝트에 적용하지 않는다.
- Stale Memory는 참고만 하고 판단 근거로 쓰지 않는다.
- 최신성 불명확한 정보는 Unknown으로 표시한다.
- 사용자 정정이 있으면 즉시 우선한다.

---

### [Best Practice]

Recency & Boundary Best Practice:

- 현재 사용자 요청을 가장 우선한다.
- 현재 작업 결과와 업로드 문서를 우선한다.
- Project Progress는 기준 문서로 사용하되 최신 작업 상태와 대조한다.
- 오래된 Memory는 최신 Context와 비교한다.
- 다른 프로젝트 Memory는 제외한다.
- 변경 가능성이 큰 정보는 확정 표현을 피한다.
- 진행 상태는 Completed / In Progress / Planned로 명확히 표현한다.
- Boundary가 불명확하면 Ask 또는 Missing Information으로 처리한다.

---

### [FAQ]

Q. Recency Check가 뭐야?
A. Memory나 Context가 현재 시점과 현재 프로젝트 상태에 맞는지 확인하는 규칙이다.

Q. Project Boundary Check가 뭐야?
A. 다른 프로젝트 정보를 현재 프로젝트에 섞지 않도록 확인하는 규칙이다.

Q. 오래된 Memory는 사용하면 안 돼?
A. 현재 문서나 요청과 충돌하지 않을 때만 보조 정보로 사용할 수 있다.

Q. 현재 작업과 Project Progress가 충돌하면 어떻게 해?
A. 현재 작업 결과가 더 최신일 수 있으므로 충돌을 표시하고 현재 작업 기준으로 보완한다.

Q. 다른 프로젝트 정보는 언제 사용할 수 있어?
A. 사용자가 명시적으로 비교하거나 참고하라고 요청한 경우에만 사용할 수 있다.

---

# 6. Memory Update & Forget

## 6.1 Memory Update Rule

### [개념]

Memory Update Rule은 사용자가 장기적으로 유용한 정보를 제공하거나 기존 정보를 수정할 때 Memory를 어떻게 갱신할지 정하는 규칙이다.

Memory Forget Rule은 사용자가 특정 정보를 잊어달라고 요청할 때 해당 정보를 더 이상 사용하지 않도록 처리하는 규칙이다.

Memory Update와 Forget은 사용자 통제권을 우선해야 한다.

---

### [핵심]

Memory Update 판단 기준:

| 정보 유형           | 저장 판단                  |
| ------------------- | -------------------------- |
| 장기 프로젝트 목표  | 저장 가능                  |
| 장기 출력 형식 선호 | 저장 가능                  |
| 장기 기술 스택      | 저장 가능                  |
| 반복 작업 규칙      | 저장 가능                  |
| 현재 작업 임시 상태 | 보통 저장 불필요           |
| 일회성 요청         | 저장 불필요                |
| Secret              | 저장 금지                  |
| 민감정보            | 명시 요청 없으면 저장 금지 |
| 다른 사람 개인정보  | 저장 금지 또는 주의        |

Memory Update Flow:

```text
User Information
→ Long-term Useful?
→ Sensitive / Secret?
→ User Requested Save?
→ Store / Do Not Store / Ask
```

Forget Rule Flow:

```text
User Forget Request
→ Identify Target Memory
→ Remove or Mark Do Not Use
→ Stop Using in Future
```

Memory 처리 결과:

```text
Store:
- 장기적으로 유용
- 민감정보 아님
- 사용자 요청 또는 명확한 장기 선호

Do Not Store:
- 일시적 정보
- Secret
- 불필요한 세부사항

Ask:
- 저장 의도가 모호함
- 민감할 수 있음

Forget:
- 사용자가 삭제 요청
```

---

### [실무]

저장 가능 예시:

```text
User Preference:
이 채팅은 RAG 문서 제작/검수 전용.
지정된 writing block 출력 형식 유지.

Decision:
Store 가능

Reason:
- 장기적으로 반복 적용 가능
- 작업 품질에 영향
```

저장 금지 예시:

```text
User Input:
API_KEY=abc123...

Decision:
Do Not Store

Reason:
- Secret
- 저장 금지
```

저장 불필요 예시:

```text
Current Work:
Part08 재작업 중

Decision:
Do Not Store

Reason:
- 현재 작업 상태
- 장기 Memory보다 현재 채팅 Context로 처리
```

Forget 예시:

```text
User:
이전 Open WebUI 계획은 이제 기억하지 마.

Handling:
- 해당 Memory 삭제 또는 사용 금지
- 이후 현재 AnythingLLM 기준 사용
```

---

### [주의]

Memory Update 주의사항:

- 명시적 저장 요청은 우선 반영한다.
- Secret은 저장하지 않는다.
- 민감정보는 명시 요청 없으면 저장하지 않는다.
- 일시적 작업 상태를 무분별하게 저장하지 않는다.
- 오래된 Memory와 새 정보가 충돌하면 새 정보를 우선한다.
- Forget 요청을 무시하지 않는다.
- Memory 업데이트로 프로젝트 경계를 흐리면 안 된다.

---

### [Best Practice]

Memory Update Best Practice:

- 장기적으로 반복 적용될 정보만 저장한다.
- 사용자의 명시적 “기억해” 요청은 반영한다.
- 민감정보와 Secret은 저장하지 않는다.
- 출력 형식, 프로젝트 범위, 장기 기술 스택은 저장 가치가 높다.
- 일시적 초안 상태는 저장하지 않는다.
- Forget 요청은 즉시 반영한다.
- Memory 변경 후 현재 작업과 충돌이 없는지 확인한다.
- 저장 여부가 애매하면 사용자에게 확인한다.

---

### [FAQ]

Q. Memory Update Rule이 뭐야?
A. 사용자가 제공한 정보를 장기 Memory에 저장할지 판단하는 규칙이다.

Q. 어떤 정보는 저장해도 돼?
A. 장기 프로젝트 목표, 반복 출력 형식, 장기 기술 스택, 지속적인 선호는 저장할 수 있다.

Q. 어떤 정보는 저장하면 안 돼?
A. API Key, Token, Password 같은 Secret과 불필요한 민감정보는 저장하면 안 된다.

Q. 사용자가 잊어달라고 하면 어떻게 해?
A. 해당 Memory를 삭제하거나 더 이상 사용하지 않도록 처리해야 한다.

Q. 일시적 작업 상태도 저장해야 해?
A. 보통 저장하지 않는다. 현재 채팅 Context로 처리하는 것이 적절하다.

---

# 7. RAG & Memory Checklist

## 7.1 RAG & Memory Guardrails Checklist

### [개념]

RAG & Memory Checklist는 Agent가 RAG 문서와 Memory를 안전하고 정확하게 사용했는지 확인하는 최소 검증 목록이다.

이 Checklist는 PM Agent, Review Agent, RAG Evaluation Agent, Safety Agent가 공통으로 사용할 수 있다.

---

### [핵심]

RAG Guardrails Checklist:

```md
### [Checklist]

- [ ] User Query에 필요한 Domain을 식별했는가?
- [ ] Retrieved Context가 질문과 관련 있는가?
- [ ] Retrieved Context가 답변에 충분한가?
- [ ] 주요 Claim이 Evidence와 연결되는가?
- [ ] Project-specific Fact가 문서 근거와 일치하는가?
- [ ] 문서에 없는 API / 클래스 / 메서드를 생성하지 않았는가?
- [ ] Citation이 실제 Claim을 뒷받침하는가?
- [ ] Missing Information을 표시했는가?
- [ ] Assumption을 사실과 구분했는가?
- [ ] Context Conflict가 있으면 Source Priority를 적용했는가?
```

Memory Guardrails Checklist:

```md
### [Checklist]

- [ ] Memory가 현재 요청과 관련 있는가?
- [ ] Memory 최신성을 확인했는가?
- [ ] 현재 요청과 Memory가 충돌하지 않는가?
- [ ] 업로드 문서와 Memory가 충돌하지 않는가?
- [ ] 다른 프로젝트 Memory를 섞지 않았는가?
- [ ] 오래된 Memory를 현재 사실처럼 쓰지 않았는가?
- [ ] Secret / 민감정보를 Memory에 저장하지 않았는가?
- [ ] 사용자의 정정 사항을 우선했는가?
- [ ] Forget 요청을 반영했는가?
```

최소 Pass 기준:

```text
- Retrieved Context 기반 답변
- 주요 Claim Evidence 연결
- Unsupported Claim 없음
- Memory 최신성 검증
- 프로젝트 경계 유지
- Secret 저장 / 출력 없음
```

---

### [실무]

적용 Flow:

```text
User Query
→ Retrieve Context
→ Context Sufficiency Check
→ Memory Relevance Check
→ Source Priority Check
→ Draft Answer
→ Unsupported Claim Remove
→ Final Output
```

Checklist Result 예시:

```md
| Category | Item                | Result | Fix                         |
| -------- | ------------------- | ------ | --------------------------- |
| RAG      | Context Sufficiency | Pass   | 없음                        |
| RAG      | Unsupported Claim   | Fail   | 근거 없는 API 제거          |
| Memory   | Recency             | Fix    | 오래된 Open WebUI 정보 제외 |
| Memory   | Project Boundary    | Pass   | 개인 AI 프로젝트 범위 유지  |
| Safety   | Secret              | Pass   | Secret 없음                 |
```

---

### [주의]

Checklist 주의사항:

- Checklist는 최소 기준이다.
- RAG 문서 검색 결과가 부정확할 수 있다.
- Memory는 유용하지만 근거 문서보다 우선하지 않는다.
- 현재 사용자 요청은 Memory보다 우선한다.
- 다른 프로젝트 Memory를 현재 프로젝트에 섞으면 안 된다.
- Secret이 발견되면 저장하거나 출력하지 않는다.
- Unsupported Claim은 Final Output 전에 제거해야 한다.

---

### [Best Practice]

Checklist Best Practice:

- RAG Check와 Memory Check를 분리한다.
- Source Priority를 명시적으로 적용한다.
- 프로젝트 고유 Claim을 우선 검증한다.
- Memory는 맥락 보조로 사용하고 근거는 문서에서 찾는다.
- 오래된 Memory는 현재 문서와 대조한다.
- Missing Information을 숨기지 않는다.
- Final Output 전 Unsupported Claim을 제거한다.
- 결과는 Pass / Fix / Stop으로 정리한다.

---

### [FAQ]

Q. RAG & Memory Checklist는 뭐야?
A. Agent가 RAG 문서와 Memory를 안전하고 정확하게 사용했는지 확인하는 최소 검증 목록이다.

Q. RAG Check와 Memory Check는 왜 분리해야 해?
A. RAG는 문서 근거 검증이고 Memory는 최신성, 관련성, 충돌 여부 검증이기 때문이다.

Q. Memory가 문서와 충돌하면 어떻게 해?
A. 현재 업로드 문서와 Retrieved Context를 우선해야 한다.

Q. 다른 프로젝트 Memory를 현재 프로젝트에 써도 돼?
A. 안 된다. 프로젝트 경계를 지켜야 한다.

Q. Checklist 최소 Pass 기준은 뭐야?
A. Retrieved Context 기반 답변, 주요 Claim Evidence 연결, Unsupported Claim 없음, Memory 최신성 검증, 프로젝트 경계 유지, Secret 저장 / 출력 없음이다.

---

# Retrieval Queries

### [FAQ]

Q. RAG Guardrails가 뭐야?
A. Agent가 Retrieved Context와 RAG 문서를 우선 사용하고 근거 없는 답변을 하지 않도록 제한하는 규칙이다.

Q. RAG Guardrails는 Grounding Evaluation과 어떻게 달라?
A. Grounding Evaluation은 평가 기준이고, RAG Guardrails는 답변 생성 시 지켜야 하는 제한 규칙이다.

Q. RAG Guardrail Flow는 어떻게 돼?
A. User Query → Retrieve Context → Check Context Sufficiency → Draft Answer from Context → Remove Unsupported Claim → Mark Missing Information → Apply Source Priority 순서다.

Q. Retrieved Context가 있으면 바로 답해도 돼?
A. 아니다. Retrieved Context가 Claim을 직접 뒷받침하는지 확인해야 한다.

Q. 문서에 없는 프로젝트 정보를 일반 지식으로 보완해도 돼?
A. 안 된다. 프로젝트 고유 정보는 Retrieved Context나 Tool Result에 근거해야 한다.

Q. 문서에 없는 API, 클래스, 메서드를 만들어도 돼?
A. 안 된다. 근거 없는 프로젝트 고유 Symbol 생성은 Hallucination이다.

Q. Context Sufficiency Rule이 뭐야?
A. 검색된 RAG Context가 사용자 질문에 답하기에 충분한지 판단하는 규칙이다.

Q. Partial Context는 어떻게 처리해?
A. 가능한 범위만 답하고 부족한 정보와 한계를 명확히 표시해야 한다.

Q. Insufficient Context에서 답하면 어떻게 돼?
A. 근거 없는 답변이나 Hallucination이 발생할 수 있다.

Q. 실제 코드 결함을 판단하려면 뭐가 필요해?
A. 일반 기준이 아니라 실제 코드, 파일, Tool Result 같은 직접 근거가 필요하다.

Q. Source Priority가 뭐야?
A. 여러 정보가 충돌할 때 어떤 근거를 우선할지 정하는 규칙이다.

Q. 현재 사용자 요청과 Memory가 충돌하면 무엇을 우선해?
A. 현재 사용자 요청을 우선해야 한다.

Q. 현재 작업 결과와 Project Progress가 충돌하면 어떻게 해?
A. 현재 작업 결과가 더 최신일 수 있으므로 현재 작업 상태를 우선하거나 충돌을 표시한다.

Q. Domain Rules와 일반 지식이 충돌하면 무엇을 우선해?
A. Domain Rules를 우선해야 한다.

Q. 충돌이 해결되지 않으면 어떻게 해?
A. Missing Information으로 표시하거나 사용자 확인이 필요하다.

Q. Memory Guardrails가 뭐야?
A. Agent가 Memory를 사용할 때 최신성, 관련성, 프로젝트 경계, 민감정보 여부를 검증하도록 제한하는 규칙이다.

Q. Memory는 RAG 문서보다 우선해?
A. 아니다. Memory는 보조 맥락이며 현재 문서와 Retrieved Context가 우선이다.

Q. Memory와 현재 요청이 충돌하면 어떻게 해?
A. 현재 사용자 요청을 우선하고 Memory는 무시하거나 보조 정보로만 사용한다.

Q. 업로드 문서와 Memory가 충돌하면 어떻게 해?
A. 현재 업로드 문서와 Retrieved Context를 우선해야 한다.

Q. 다른 프로젝트 Memory를 현재 프로젝트에 사용해도 돼?
A. 안 된다. 프로젝트 경계를 지켜야 한다.

Q. Recency Check가 뭐야?
A. Memory나 Context가 현재 시점과 현재 프로젝트 상태에 맞는지 확인하는 규칙이다.

Q. Project Boundary Check가 뭐야?
A. 다른 프로젝트 정보를 현재 프로젝트에 섞지 않도록 확인하는 규칙이다.

Q. Stale Memory는 뭐야?
A. 오래되어 현재 상태와 맞지 않을 수 있는 Memory다.

Q. 최신성 불확실하면 어떻게 해?
A. Unknown 또는 Assumption으로 표시하고 확정 표현을 피해야 한다.

Q. Memory Update Rule이 뭐야?
A. 사용자가 제공한 정보를 장기 Memory에 저장할지 판단하는 규칙이다.

Q. 어떤 정보는 Memory에 저장해도 돼?
A. 장기 프로젝트 목표, 반복 출력 형식, 장기 기술 스택, 지속적인 선호는 저장할 수 있다.

Q. 어떤 정보는 Memory에 저장하면 안 돼?
A. API Key, Token, Password 같은 Secret과 불필요한 민감정보는 저장하면 안 된다.

Q. 사용자가 잊어달라고 하면 어떻게 해?
A. 해당 Memory를 삭제하거나 더 이상 사용하지 않도록 처리해야 한다.

Q. RAG & Memory Checklist는 언제 써?
A. RAG 답변 생성 후 Final Output 전에 사용한다.

Q. RAG Check와 Memory Check는 왜 분리해?
A. RAG는 문서 근거 검증이고 Memory는 최신성, 관련성, 충돌 여부 검증이기 때문이다.

Q. RAG & Memory Guardrails 최소 Pass 기준은 뭐야?
A. Retrieved Context 기반 답변, 주요 Claim Evidence 연결, Unsupported Claim 없음, Memory 최신성 검증, 프로젝트 경계 유지, Secret 저장 / 출력 없음이다.

Q. RAG & Memory Guardrails의 최종 목표는 뭐야?
A. Agent가 문서 근거와 검증된 Memory를 안전하게 사용하고, 오래된 정보나 근거 없는 프로젝트 사실을 생성하지 않도록 통제하는 것이다.
