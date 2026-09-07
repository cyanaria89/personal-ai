# Agent Evaluation & Guardrails Part12 - Troubleshooting & Best Practices

---

# 1. Troubleshooting Core

## 1.1 Agent Troubleshooting

### [개념]

Agent Troubleshooting은 Agent 운영 중 반복적으로 발생하는 문제를 진단하고 재발 방지 규칙으로 정리하는 과정이다.

Troubleshooting은 Failure / Retry / Fallback 규칙을 반복 설명하는 문서가 아니다.

이 문서의 초점은 **대표 문제 상황, 원인 분석, 해결 방향, 재발 방지 Best Practice**다.

Troubleshooting 대상:

- RAG 검색 실패
- 근거 없는 답변
- 출력 형식 깨짐
- Tool 결과 오해
- Review Agent 오탐 / 누락
- Memory 충돌
- Safety Guardrail 과잉 / 부족
- Workflow 품질 저하
- Fix 후 Regression 발생
- Agent 운영 규칙 불일치

---

### [핵심]

Troubleshooting 기본 구조:

```md
## Problem

문제 설명

## Cause

원인 설명

## Evidence

확인 근거

## Fix

해결 방법

## Prevention

재발 방지 규칙
```

Troubleshooting Flow:

```text
Problem Detected
→ Identify Symptom
→ Collect Evidence
→ Classify Root Cause
→ Apply Fix
→ Add Prevention Rule
→ Re-evaluate
```

대표 문제와 연결되는 영역:

| Problem                   | Related Area              |
| ------------------------- | ------------------------- |
| 문서에 없는 답변 생성     | RAG Guardrails, Grounding |
| 검색 결과 부족            | Retrieval Optimization    |
| JSON / Markdown 깨짐      | Format Compliance         |
| Tool 실패를 성공처럼 답변 | Tool Result Validation    |
| 위험 작업 자동 진행       | Safety Guardrails         |
| Review가 쓸데없는 지적    | False Positive            |
| Review가 중요한 문제 누락 | False Negative            |
| Fix 후 새 문제 발생       | Regression Check          |
| 오래된 정보 사용          | Memory Guardrails         |
| Agent 간 전달 오류        | Workflow Evaluation       |

---

### [실무]

개인 AI 개발팀에서는 Troubleshooting 결과를 다시 Prompt, Domain Rules, Checklist, Retrieval Queries에 반영해야 한다.

실무 적용 순서:

```text
1. 반복 문제를 기록한다.
2. 실제 Evidence를 확인한다.
3. 원인을 Prompt / RAG / Tool / Memory / Workflow / Review 중 하나로 분류한다.
4. 즉시 Fix를 적용한다.
5. 재발 방지 규칙을 추가한다.
6. 관련 RAG 문서나 Checklist를 보강한다.
7. 재검수한다.
```

Troubleshooting Report 예시:

```md
# Troubleshooting Report

## Problem

Agent가 Tool 실패를 성공처럼 답변함.

## Cause

Tool Result Validation 누락.

## Evidence

Tool Result: Permission denied
Final Output: 파일 확인 완료라고 답변

## Fix

파일 확인 실패로 수정하고 검증 불가 범위를 표시한다.

## Prevention

Post-Execution Tool Checklist를 필수 적용한다.
```

---

### [주의]

Troubleshooting 주의사항:

- 증상만 보고 원인을 단정하지 않는다.
- Evidence 없이 원인을 확정하지 않는다.
- Retry만으로 모든 문제가 해결되지 않는다.
- Safety 문제는 일반 품질 문제보다 우선한다.
- Memory 기반 추측으로 Root Cause를 확정하지 않는다.
- Fix 후 Regression을 확인해야 한다.
- 반복 문제는 개별 수정으로 끝내지 말고 Guardrail에 반영한다.

---

### [Best Practice]

Troubleshooting Best Practice:

- Problem / Cause / Evidence / Fix / Prevention 구조를 사용한다.
- Evidence를 먼저 확보한다.
- 즉시 Fix와 재발 방지 규칙을 분리한다.
- 반복 문제는 Checklist에 추가한다.
- Safety 관련 문제는 Critical로 처리한다.
- RAG 검색 실패는 Retrieval Queries 개선으로 연결한다.
- Review 품질 문제는 Review Agent Evaluation으로 연결한다.
- Fix 후 Re-evaluation을 수행한다.
- Troubleshooting 결과를 Domain Rules 개선 후보로 기록한다.

---

### [FAQ]

Q. Agent Troubleshooting이 뭐야?
A. Agent 운영 중 반복적으로 발생하는 문제를 진단하고 해결 및 재발 방지 규칙으로 정리하는 과정이다.

Q. Troubleshooting은 Failure 문서와 뭐가 달라?
A. Failure 문서는 실패 유형과 복구 전략 중심이고, Troubleshooting은 실제 문제 사례와 재발 방지 중심이다.

Q. Troubleshooting에서 가장 먼저 할 일은 뭐야?
A. 문제 증상과 Evidence를 확인하는 것이다.

Q. Evidence 없이 원인을 판단해도 돼?
A. 안 된다. Evidence가 없으면 Assumption 또는 Unknown으로 표시해야 한다.

Q. Troubleshooting 결과는 어디에 반영해?
A. Prompt, Checklist, Domain Rules, Retrieval Queries, Agent Workflow 규칙에 반영한다.

---

# 2. RAG Troubleshooting

## 2.1 Retrieval Failure 개선

### [개념]

Retrieval Failure는 필요한 RAG 문서나 Chunk가 검색되지 않거나, 검색되었지만 질문에 답하기에 부족한 문제다.

Retrieval Failure는 RAG 문서 구조, 용어, FAQ, Retrieval Queries 품질과 직접 연결된다.

---

### [핵심]

Problem:

```text
사용자 질문에 필요한 RAG Context가 검색되지 않음.
```

주요 원인:

| Cause                  | 설명                           |
| ---------------------- | ------------------------------ |
| Query 표현 불일치      | 사용자 질문과 문서 용어가 다름 |
| FAQ 부족               | 실제 질문 표현이 문서에 없음   |
| Retrieval Queries 부족 | 검색용 질문 확장이 부족함      |
| Header 모호            | 섹션 제목에 핵심 키워드 없음   |
| Chunk 혼합             | 한 Chunk에 여러 개념이 섞임    |
| 용어 불일치            | 같은 개념을 여러 이름으로 사용 |
| 문서 누락              | 필요한 Domain 문서가 없음      |

해결 방향:

```text
- 실제 사용자 질문 표현 추가
- FAQ 강화
- Retrieval Queries 강화
- Header에 핵심 키워드 포함
- 하나의 Chunk에 하나의 개념만 유지
- 한국어 / 영어 핵심 용어 병행
- 용어 통일
```

---

### [실무]

예시:

```text
Problem:
“Tool 실행 전 뭐 확인해야 해?” 질문에서 Tool Calling 문서가 검색되지 않음.

Cause:
Retrieval Queries에 실제 질문 표현 부족.

Fix:
다음 FAQ 추가:
- Tool 실행 전 무엇을 확인해야 해?
- Tool Arguments는 어떻게 검증해?
- Tool Calling Risk Level은 어떻게 판단해?
```

문서 개선 예시:

```md
# Retrieval Queries

### [FAQ]

Q. Tool 실행 전 무엇을 확인해야 해?
A. Tool Choice, Arguments, Permission, Risk Level, Side Effect, Human Confirmation을 확인해야 한다.

Q. Tool Arguments 검증은 왜 필요해?
A. 잘못된 인자는 데이터 손실, 보안 문제, 실행 실패를 만들 수 있기 때문이다.
```

Retrieval 개선 Report:

```md
| Problem               | Cause                  | Fix                        |
| --------------------- | ---------------------- | -------------------------- |
| 핵심 문서 미검색      | FAQ 질문 표현 부족     | Retrieval Queries 보강     |
| 관련 없는 Chunk 검색  | Header 모호            | Section 제목에 키워드 추가 |
| 검색 결과 일반론 과다 | Chunk에 여러 개념 혼합 | Chunk 분리                 |
```

---

### [주의]

Retrieval Troubleshooting 주의사항:

- 검색 결과 없음은 정보 부재와 다르다.
- Query 수정으로 해결될 수도 있고 문서 구조 개선이 필요할 수도 있다.
- FAQ 부족은 실제 질문 매칭을 약하게 만든다.
- 너무 긴 Chunk는 핵심 키워드를 묻히게 한다.
- 용어 불일치는 Semantic Search 정확도를 낮춘다.
- Retrieval 실패 상태에서 확정 답변하면 Hallucination 위험이 높다.

---

### [Best Practice]

Retrieval Troubleshooting Best Practice:

- 검색 실패 Query를 기록한다.
- 실패 Query를 Retrieval Queries에 반영한다.
- 문서에 실제 사용자 질문 표현을 추가한다.
- Header를 검색 키워드 중심으로 작성한다.
- FAQ 답변은 짧고 직접적으로 작성한다.
- Chunk당 하나의 핵심 개념을 유지한다.
- 한글 용어와 영어 용어를 함께 넣는다.
- 중복 표현보다 검색 의도 다양성을 우선한다.

---

### [FAQ]

Q. Retrieval Failure는 뭐야?
A. 사용자 질문에 필요한 RAG 문서나 Chunk가 검색되지 않는 문제다.

Q. 검색 결과가 없으면 문서가 없다는 뜻이야?
A. 아니다. Query 표현, 문서 구조, FAQ, Retrieval Queries 문제일 수 있다.

Q. Retrieval Failure를 줄이려면 뭐가 중요해?
A. FAQ, Retrieval Queries, Header, Chunk 구조, 용어 통일이 중요하다.

Q. 실제 사용자 질문 표현은 왜 넣어야 해?
A. 사용자가 검색할 가능성이 높은 문장과 문서 내용을 연결해 검색 성공률을 높이기 때문이다.

Q. Retrieval Troubleshooting 결과는 어디에 반영해?
A. 해당 RAG 문서의 FAQ, Retrieval Queries, Header, Chunk 구조에 반영한다.

---

# 3. Grounding Troubleshooting

## 3.1 Unsupported Claim 개선

### [개념]

Grounding Troubleshooting은 Agent가 문서나 Tool Result에 없는 내용을 사실처럼 답변하는 문제를 해결하는 과정이다.

Grounding Troubleshooting은 RAG Guardrails와 연결된다.

핵심은 Claim을 Evidence와 연결하고, 근거 없는 Claim을 제거하는 것이다.

---

### [핵심]

Problem:

```text
Agent가 Retrieved Context에 없는 내용을 실제 사실처럼 답변함.
```

대표 증상:

- 문서에 없는 API 경로 생성
- 존재하지 않는 클래스 / 메서드 사용
- Project Progress 상태 왜곡
- 일반 지식으로 프로젝트 고유 정보 확정
- Citation이 Claim을 뒷받침하지 않음
- Missing Information을 숨김

원인:

| Cause                          | 설명                         |
| ------------------------------ | ---------------------------- |
| Claim-Evidence Check 없음      | 주장과 근거 연결 검증 누락   |
| Context Sufficiency Check 없음 | 검색 결과 충분성 미확인      |
| Project Symbol Check 없음      | 코드 Symbol 존재 여부 미검증 |
| Missing Information Rule 없음  | 부족한 정보 표시 안 함       |
| False Confidence               | 불확실한 내용을 확정함       |

해결 방향:

```text
- Claim 단위로 분리
- Evidence 확인
- Unsupported Claim 제거
- Weak Evidence는 Assumption 처리
- Missing Information 표시
- Source Priority 적용
```

---

### [실무]

예시:

```text
Problem:
Agent가 `/festival/popular` API가 있다고 답변함.

Evidence:
제공된 Controller API 목록에는 `/festival`, `/festival/search`, `/festival/detail/{id}`, `/festival/location/{id}`만 있음.

Fix:
- `/festival/popular` Claim 제거
- 제공된 Context 기준 API 목록만 답변
- 필요 시 “제공된 Context에는 해당 API가 없음”으로 표시
```

Grounding 개선 Report:

```md
| Claim                   | Evidence Status           | Fix                |
| ----------------------- | ------------------------- | ------------------ |
| /festival/popular 존재  | Unsupported               | 제거               |
| findUnreadByUserId 사용 | Unsupported               | 실제 메서드명 사용 |
| Agent Evaluation 완료   | Current Work 기준 Partial | 표현 제한          |
```

Prevention Rule:

```text
- Project-specific Claim은 반드시 Evidence와 연결한다.
- Retrieved Context가 부족하면 Missing Information으로 표시한다.
- 없는 파일명, API, 클래스, 메서드는 생성하지 않는다.
- Final Output 전 Claim-Evidence Check를 적용한다.
```

---

### [주의]

Grounding Troubleshooting 주의사항:

- 관련 키워드가 검색되었다고 Supported Claim은 아니다.
- Citation이 있어도 Wrong Citation일 수 있다.
- 프로젝트 고유 정보는 일반 지식으로 채우지 않는다.
- “보통은”이라는 표현으로 프로젝트 사실을 확정하지 않는다.
- 검색 결과 없음과 실제 부재를 구분한다.
- 핵심 Claim이 Unsupported이면 Major 이상으로 본다.

---

### [Best Practice]

Grounding Troubleshooting Best Practice:

- Claim을 문장 단위로 분리한다.
- Project-specific Claim을 먼저 검증한다.
- Claim-Evidence 표를 사용한다.
- Unsupported Claim은 제거한다.
- Weak Evidence는 Assumption으로 낮춘다.
- Missing Information을 명시한다.
- Source Priority를 적용한다.
- Review Agent에 Unsupported Claim Check를 필수화한다.

---

### [FAQ]

Q. Grounding Troubleshooting은 뭐야?
A. Agent가 근거 없는 답변을 생성하는 문제를 Claim-Evidence 검증으로 해결하는 과정이다.

Q. Agent가 문서에 없는 API를 만들면 어떻게 해?
A. Fabricated API로 보고 Claim을 제거하거나 실제 Context 기준으로 수정해야 한다.

Q. Citation이 있으면 근거 있는 답변이야?
A. 아니다. Citation이 실제 Claim을 직접 뒷받침해야 한다.

Q. Weak Evidence는 어떻게 처리해?
A. 확정 표현을 피하고 Assumption 또는 Partial로 낮춰야 한다.

Q. Grounding 문제를 예방하려면?
A. Final Output 전 Claim-Evidence Check와 Missing Information Rule을 적용해야 한다.

---

# 4. Format Troubleshooting

## 4.1 Markdown / JSON Format Failure 개선

### [개념]

Format Troubleshooting은 Agent Output이 요구된 Markdown, JSON, Schema, Wrapper, Required Section 형식을 지키지 못하는 문제를 해결하는 과정이다.

Format Troubleshooting은 출력 형식 문제에 집중한다.

내용 정확성은 별도 Evaluation에서 확인한다.

---

### [핵심]

Problem:

```text
Agent Output이 요구된 출력 형식을 반복적으로 위반함.
```

대표 증상:

- JSON 파싱 실패
- Required Field 누락
- Markdown Header 계층 오류
- Required Section 누락
- FAQ Q/A 형식 오류
- Retrieval Queries 누락
- Code Block 미종료
- Output Wrapper 누락
- JSON 밖 설명 문장 포함

원인:

| Cause                   | 설명                           |
| ----------------------- | ------------------------------ |
| Schema 복잡도 과다      | 모델이 구조 유지 실패          |
| Required Field 불명확   | 필수 항목 누락                 |
| Output Example 없음     | 모델이 형식 추측               |
| Format Guardrail 약함   | 출력 규칙 불명확               |
| 내용 과다               | 형식 유지보다 내용 생성에 집중 |
| Final Format Check 없음 | 최종 검증 누락                 |

해결 방향:

```text
- Required Structure를 Checklist로 고정
- Schema 단순화
- Output Example 제공
- JSON은 순수 JSON만 출력
- Markdown Header 계층 단순화
- Final Format Check 적용
```

---

### [실무]

JSON Format Failure 예시:

```text
Problem:
JSON 앞에 “아래는 결과입니다” 문장이 포함됨.

Fix:
- 순수 JSON만 출력하도록 규칙 강화
- 설명은 JSON 필드 내부에 포함하거나 제거
```

Markdown RAG Format Failure 예시:

```text
Problem:
[FAQ]는 있지만 Q/A 형식이 아님.

Fix:
- Q. 질문
- A. 답변
형식으로 수정
```

RAG 문서 Format Checklist:

```md
### [Checklist]

- [ ] # FileName 존재
- [ ] # Document Title 존재
- [ ] [개념] 존재
- [ ] [핵심] 존재
- [ ] [실무] 존재
- [ ] [FAQ] 존재
- [ ] FAQ는 Q/A 형식
- [ ] Retrieval Queries 존재
- [ ] Code Block 닫힘
- [ ] Header 계층 일관
```

Format 개선 Report:

```md
| Failure                | Cause                       | Fix              |
| ---------------------- | --------------------------- | ---------------- |
| JSON 파싱 실패         | 설명 문장 포함              | 순수 JSON만 출력 |
| FAQ A 누락             | FAQ 형식 검증 없음          | Q/A 완성         |
| Retrieval Queries 누락 | Required Section Check 누락 | 문서 마지막 추가 |
```

---

### [주의]

Format Troubleshooting 주의사항:

- 형식이 깨지면 내용이 좋아도 자동 처리에 실패할 수 있다.
- JSON에 주석을 넣으면 표준 JSON이 아니다.
- Markdown code fence 누락은 문서 전체 구조를 깨뜨릴 수 있다.
- FAQ Q/A 누락은 Retrieval 품질을 낮춘다.
- Schema가 너무 복잡하면 반복 실패 가능성이 높다.
- Format Failure와 Content Failure를 분리해서 본다.

---

### [Best Practice]

Format Troubleshooting Best Practice:

- Required Structure를 Checklist로 만든다.
- 복잡한 Schema는 단순화한다.
- Output Example을 제공한다.
- JSON은 순수 JSON만 출력한다.
- Markdown은 Header 계층을 단순하게 유지한다.
- FAQ Q/A 형식을 고정한다.
- Final Output 전 Format Compliance Check를 수행한다.
- 반복 실패 시 더 작은 단위로 나눠 생성한다.

---

### [FAQ]

Q. Format Troubleshooting은 뭐야?
A. Agent Output이 요구된 Markdown, JSON, Schema, Required Section 형식을 지키지 못하는 문제를 해결하는 과정이다.

Q. Format Failure는 왜 문제야?
A. 후속 Agent, Parser, Tool, RAG Indexer가 결과를 처리하지 못할 수 있기 때문이다.

Q. JSON이 자꾸 깨지면 어떻게 해?
A. Schema를 단순화하고 순수 JSON만 출력하도록 하며 Required Field를 명확히 해야 한다.

Q. Markdown RAG 문서는 무엇을 확인해야 해?
A. FileName, Document Title, Required Section, FAQ Q/A, Retrieval Queries, Header 계층을 확인해야 한다.

Q. Format이 맞으면 내용도 맞는 거야?
A. 아니다. Format Compliance와 Content Quality는 별도로 평가해야 한다.

---

# 5. Review Troubleshooting

## 5.1 Review Agent 오탐 / 누락 개선

### [개념]

Review Troubleshooting은 Review Agent가 문제가 아닌 것을 문제로 지적하거나, 실제 중요한 문제를 놓치는 상황을 개선하는 과정이다.

Review Troubleshooting은 Review Agent Evaluation과 연결된다.

핵심은 Review Agent의 False Positive와 False Negative를 줄이는 것이다.

---

### [핵심]

대표 문제:

| Problem             | 의미                         |
| ------------------- | ---------------------------- |
| False Positive      | 문제가 아닌 것을 문제로 지적 |
| False Negative      | 실제 문제를 놓침             |
| Severity Error      | 심각도 과장 또는 축소        |
| Weak Evidence       | 근거 없는 Finding            |
| Weak Fix Direction  | 수정 방향이 추상적           |
| Requirement Ignored | 사용자 요구사항 무시         |
| Domain Rule Ignored | Domain Rules 미반영          |

False Positive 원인:

```text
- 취향을 결함으로 판단
- 일반 관례를 프로젝트 규칙보다 우선
- 사용자 요구사항 무시
- Evidence 없는 지적
- Severity 과장
```

False Negative 원인:

```text
- Checklist 누락
- Required Section 미확인
- Safety Check 미수행
- Grounding Check 미수행
- Code Symbol Check 미수행
```

해결 방향:

```text
- Review Criteria 고정
- Finding마다 Evidence 요구
- Severity 기준표 적용
- False Positive Check 추가
- False Negative Check 추가
- Domain Rules 우선 적용
- 사용자 요구사항 최우선 적용
```

---

### [실무]

False Positive 예시:

```text
Review Finding:
FAQ가 너무 많으니 줄여야 한다.

User Requirement:
FAQ 강화

Decision:
False Positive

Fix:
- Finding 제거
- FAQ 강화 요구를 Review Criteria에 반영
```

False Negative 예시:

```text
Agent Output:
Retrieval Queries 없음.

Review Agent:
문제 없음.

Decision:
False Negative

Fix:
- Required Section Checklist 추가
```

Severity Error 예시:

```text
Finding:
문장 표현이 조금 어색함.

Review Severity:
Critical

Correct Severity:
Minor 또는 Info
```

Review 개선 Report:

```md
| Problem                       | Cause                       | Fix                 |
| ----------------------------- | --------------------------- | ------------------- |
| FAQ 줄이라고 지적             | 사용자 요구사항 무시        | False Positive 제거 |
| Retrieval Queries 누락 미탐지 | Required Section Check 없음 | Checklist 추가      |
| 표현 문제 Critical 처리       | Severity 기준 없음          | Severity Table 적용 |
```

---

### [주의]

Review Troubleshooting 주의사항:

- Review Agent도 Hallucination을 만들 수 있다.
- 취향성 지적을 결함으로 처리하지 않는다.
- 사용자 요구사항과 Domain Rules를 최우선으로 둔다.
- Evidence 없는 Finding은 신뢰도가 낮다.
- False Negative는 최종 Output 품질을 크게 낮출 수 있다.
- Safety False Negative는 Critical로 본다.
- Review Agent가 너무 엄격하면 Workflow가 느려진다.

---

### [Best Practice]

Review Troubleshooting Best Practice:

- Review Agent Output도 평가한다.
- Finding마다 Evidence, Severity, Fix를 요구한다.
- 취향 / 개선 / 결함을 구분한다.
- Required Section Checklist를 사용한다.
- Safety / Grounding / Format / Code Check를 분리한다.
- False Positive와 False Negative를 기록한다.
- 반복 Review Failure는 Review Prompt에 반영한다.
- Fix Direction은 실행 가능하게 작성한다.

---

### [FAQ]

Q. Review Troubleshooting은 뭐야?
A. Review Agent의 오탐, 누락, Severity 오류, 근거 부족 문제를 개선하는 과정이다.

Q. False Positive는 어떻게 줄여?
A. 사용자 요구사항, Domain Rules, Evidence를 기준으로 Finding을 검증해야 한다.

Q. False Negative는 어떻게 줄여?
A. Required Section, Safety, Grounding, Format, Code Checklist를 고정 적용해야 한다.

Q. Review Agent가 취향을 결함처럼 지적하면 어떻게 해?
A. False Positive로 제거하거나 Info로 낮춰야 한다.

Q. Review Troubleshooting 결과는 어디에 반영해?
A. Review Agent Prompt, Checklist, Severity 기준, Domain Rules에 반영한다.

---

# 6. Workflow Troubleshooting

## 6.1 Multi-Agent Workflow 문제 개선

### [개념]

Workflow Troubleshooting은 Multi-Agent Workflow에서 Routing, Handoff, State, Review-Fix 과정이 어긋나는 문제를 개선하는 과정이다.

Workflow Troubleshooting은 개별 Agent 품질뿐 아니라 Agent 간 연결 품질을 다룬다.

---

### [핵심]

대표 문제:

| Problem                    | 의미                       |
| -------------------------- | -------------------------- |
| Wrong Routing              | 잘못된 Agent에게 작업 전달 |
| Weak Handoff               | 필요한 Context 누락        |
| State Conflict             | Agent 간 상태 불일치       |
| Requirement Drift          | 원래 요구사항이 흐려짐     |
| Review-Fix Loop            | 같은 수정 반복             |
| Fix Regression             | Fix 후 새 문제 발생        |
| Stop Condition Missing     | 멈춰야 할 때 계속 진행     |
| Human Confirmation Missing | 위험 작업 승인 누락        |

원인:

```text
- PM Agent Routing Rule 부족
- Handoff Template 없음
- State 기록 없음
- Requirement Preservation 없음
- Stop Condition 없음
- Fix Mapping 없음
- Safety Check 누락
```

해결 방향:

```text
- Routing 기준 고정
- Handoff Template 사용
- State Consistency Check 적용
- User Requirement를 Workflow 전체 기준으로 유지
- Review Finding과 Fix Result 매핑
- Stop Condition과 Max Iteration 설정
- High Risk 작업은 Safety Agent로 Routing
```

---

### [실무]

Wrong Routing 예시:

```text
User Request:
Spring Boot Repository 메서드 검토

Wrong Routing:
Frontend Agent

Fix:
Backend Agent + Review Agent로 Routing
```

Weak Handoff 예시:

```text
Problem:
Backend Agent에게 Service 검토 요청 전달.
하지만 Repository 메서드 목록 누락.

Fix:
Handoff에 관련 Entity, DTO, Repository, 요구사항, Output Format 포함.
```

Fix Regression 예시:

```text
Problem:
FAQ 누락을 고치다가 Retrieval Queries 섹션 삭제.

Fix:
Fix 후 Required Section Checklist 재적용.
```

Workflow 개선 Report:

```md
| Problem              | Cause                 | Fix                   |
| -------------------- | --------------------- | --------------------- |
| 잘못된 Agent Routing | Domain 분류 없음      | Routing Rule 추가     |
| Context 누락         | Handoff Template 없음 | Handoff Template 사용 |
| 같은 Fix 반복        | Max Iteration 없음    | Review-Fix Limit 적용 |
| Fix 후 새 오류       | Regression Check 없음 | Re-evaluation 적용    |
```

---

### [주의]

Workflow Troubleshooting 주의사항:

- 최종 Output만 좋다고 Workflow가 안정적인 것은 아니다.
- Handoff 누락은 다음 Agent의 Hallucination을 유발한다.
- State Conflict는 오래된 Memory와 연결될 수 있다.
- Review-Fix Loop는 Max Iteration이 필요하다.
- 위험 작업은 Specialist Agent만으로 충분하지 않다.
- Safety Agent 또는 Human Confirmation이 필요할 수 있다.
- Fix 후 Re-evaluation을 생략하면 Regression을 놓친다.

---

### [Best Practice]

Workflow Troubleshooting Best Practice:

- User Requirement를 Workflow 전체의 기준으로 유지한다.
- Routing 기준을 Domain / Risk / Output Type으로 정한다.
- Handoff에는 Goal, Context, Constraints, Output Format을 포함한다.
- State를 Completed / In Progress / Planned로 관리한다.
- Review Finding과 Fix Result를 매핑한다.
- Fix 후 Regression Check를 수행한다.
- Stop Condition과 Max Iteration을 둔다.
- 위험 작업은 Safety Agent 또는 Human Confirmation으로 분기한다.

---

### [FAQ]

Q. Workflow Troubleshooting은 뭐야?
A. Multi-Agent Workflow의 Routing, Handoff, State, Review-Fix 문제를 개선하는 과정이다.

Q. Wrong Routing은 어떻게 고쳐?
A. User Request를 Domain, Risk, Output Type으로 분류하고 적절한 Agent로 Routing해야 한다.

Q. Handoff가 약하면 어떤 문제가 생겨?
A. 다음 Agent가 Context 부족으로 잘못된 가정이나 Hallucination을 만들 수 있다.

Q. Fix 후 새 문제가 생기면 어떻게 해?
A. Regression으로 보고 Re-evaluation과 Required Section Checklist를 적용해야 한다.

Q. Workflow 문제를 줄이려면?
A. Routing Rule, Handoff Template, State Check, Stop Condition, Fix Mapping을 사용해야 한다.

---

# 7. Memory Troubleshooting

## 7.1 Memory Conflict 개선

### [개념]

Memory Troubleshooting은 오래된 Memory, 다른 프로젝트 Memory, 현재 요청과 충돌하는 Memory를 잘못 사용하는 문제를 개선하는 과정이다.

Memory는 현재 문서와 Tool Result를 대체하지 않는다.

Memory는 맥락 보조로만 사용해야 한다.

---

### [핵심]

Problem:

```text
Agent가 오래된 Memory나 다른 프로젝트 정보를 현재 프로젝트 사실처럼 사용함.
```

대표 증상:

- 오래된 기술 스택을 현재 사용 중이라고 말함
- 다른 프로젝트 API를 현재 프로젝트에 적용함
- 과거 계획을 현재 완료 상태처럼 설명함
- 사용자가 방금 정정한 내용을 무시함
- 현재 업로드 문서보다 Memory를 우선함

원인:

| Cause                       | 설명                      |
| --------------------------- | ------------------------- |
| Recency Check 없음          | 오래된 정보 사용          |
| Project Boundary Check 없음 | 다른 프로젝트 정보 혼입   |
| Source Priority 없음        | 현재 문서보다 Memory 우선 |
| User Correction 무시        | 최신 사용자 지시 미반영   |
| Memory Validation 없음      | Memory 신뢰도 미검증      |

해결 방향:

```text
- Memory 사용 전 Relevance 확인
- Recency Check 적용
- Project Boundary Check 적용
- 현재 요청과 업로드 문서 우선
- 다른 프로젝트 Memory 제외
- 사용자 정정 우선
- 필요한 경우 Memory Update / Forget
```

---

### [실무]

Memory Conflict 예시:

```text
Old Memory:
Open WebUI + ComfyUI 사용

Current Project Context:
AnythingLLM + Ollama + Qwen2.5 + BGE-M3 사용

Decision:
Old Memory는 Stale
현재 작업에는 AnythingLLM 기준 적용
```

Project Boundary 예시:

```text
Memory:
FestaPick 프로젝트 FestivalController API

Current Request:
개인 AI 프로젝트 Agent Evaluation 문서 작성

Decision:
다른 프로젝트 정보
현재 문서에 사용하지 않음
```

User Correction 예시:

```text
User:
이 채팅은 RAG 문서 제작/검수 전용. 중간 응답 금지.

Memory:
작업 중 진행상황 공유 선호

Decision:
현재 사용자 요청 우선
중간 응답 금지
```

Memory 개선 Report:

```md
| Memory               | Problem            | Decision             |
| -------------------- | ------------------ | -------------------- |
| Open WebUI 현재 사용 | 현재 상태와 충돌   | Ignore               |
| FestaPick API        | 프로젝트 범위 다름 | Ignore               |
| 진행상황 공유        | 현재 요청과 충돌   | Current Request 우선 |
```

---

### [주의]

Memory Troubleshooting 주의사항:

- Memory는 항상 최신이 아니다.
- 현재 사용자 요청은 Memory보다 우선한다.
- 현재 업로드 문서와 Retrieved Context는 Memory보다 우선한다.
- 다른 프로젝트 정보를 섞으면 Hallucination이 된다.
- 오래된 기술 스택을 현재 사실처럼 말하지 않는다.
- 사용자 정정 사항을 무시하지 않는다.
- Memory 충돌이 해결되지 않으면 Ask 또는 Missing Information으로 처리한다.

---

### [Best Practice]

Memory Troubleshooting Best Practice:

- Memory 사용 전 Relevance, Recency, Conflict를 확인한다.
- 현재 요청과 현재 문서를 우선한다.
- 프로젝트 경계를 확인한다.
- 다른 프로젝트 Memory는 제외한다.
- 오래된 Memory는 현재 사실로 확정하지 않는다.
- 사용자 정정은 즉시 우선 적용한다.
- Memory Conflict를 Evaluation Report에 기록한다.
- 장기적으로 틀린 Memory는 Update 또는 Forget 대상으로 관리한다.

---

### [FAQ]

Q. Memory Troubleshooting은 뭐야?
A. 오래된 Memory, 다른 프로젝트 Memory, 현재 요청과 충돌하는 Memory 사용 문제를 개선하는 과정이다.

Q. Memory와 현재 요청이 충돌하면 무엇을 우선해?
A. 현재 사용자 요청을 우선해야 한다.

Q. Memory와 업로드 문서가 충돌하면 무엇을 우선해?
A. 현재 업로드 문서와 Retrieved Context를 우선해야 한다.

Q. 다른 프로젝트 Memory를 현재 프로젝트에 써도 돼?
A. 안 된다. 프로젝트 경계를 지켜야 한다.

Q. 오래된 Memory는 어떻게 처리해?
A. 현재 문서와 대조하고 충돌하면 무시하거나 Stale로 표시해야 한다.

---

# 8. Agent Evaluation Best Practices

## 8.1 Evaluation Operation Best Practices

### [개념]

Agent Evaluation Best Practices는 Agent Output, RAG 답변, Tool Calling, Workflow, Review, Memory, Safety를 일관되게 평가하기 위한 운영 기준이다.

Best Practices의 목적은 Agent Workflow를 반복 가능하고 안전하며 근거 기반으로 유지하는 것이다.

---

### [핵심]

Agent Evaluation Best Practices:

```text
1. User Requirement를 최우선 기준으로 사용한다.
2. Must / Must Not / Constraint를 분리한다.
3. Agent Output은 항상 Evaluation 대상이다.
4. 최종 Output뿐 아니라 중간 Output도 평가한다.
5. 주요 Claim은 Evidence와 연결한다.
6. Project-specific Fact는 Retrieved Context 또는 Tool Result 기준으로 검증한다.
7. Unsupported Claim은 제거하거나 Assumption으로 낮춘다.
8. Format Compliance와 Content Quality를 분리한다.
9. Tool Arguments는 실행 전 검증한다.
10. High Risk Tool은 Human Confirmation 전 실행하지 않는다.
11. Review Finding에는 Evidence와 Severity를 포함한다.
12. Fix 후 Re-evaluation을 수행한다.
13. Retry Limit과 Stop Condition을 둔다.
14. Memory는 Recency와 Conflict를 확인한다.
15. Safety Finding은 우선 처리한다.
```

Evaluation Operation Flow:

```text
Requirement
→ Grounding
→ Format
→ Tool / Safety
→ Review
→ Fix
→ Re-evaluation
→ Final Decision
```

작업 유형별 핵심 Best Practice:

| 영역        | Best Practice                        |
| ----------- | ------------------------------------ |
| Requirement | Must / Must Not 분리                 |
| Grounding   | Claim-Evidence 매핑                  |
| Format      | Required Section Checklist           |
| Code        | Project Symbol Check                 |
| Tool        | Pre / Post Execution Check           |
| Safety      | Risk Classification                  |
| Workflow    | Routing / Handoff / State 검증       |
| Review      | False Positive / False Negative 관리 |
| Fix         | Finding-Fix Mapping                  |
| Memory      | Recency / Conflict Check             |

---

### [실무]

RAG 문서 작성 Workflow:

```text
1. MASTER_RAG_RULES 확인
2. DOMAIN_RULES 확인
3. Required Section 작성
4. FAQ 강화
5. Retrieval Queries 작성
6. Format Compliance Check
7. Grounding / Consistency Check
8. Final Output
```

Code Review Workflow:

```text
1. 사용자 요구사항 확인
2. 실제 코드 Context 확인
3. Project Symbol Check
4. Compile / Runtime Risk 검토
5. Security / Transaction / Exception 검토
6. Findings 작성
7. Fix Recommendation 작성
```

Tool Execution Workflow:

```text
1. Tool 필요성 확인
2. Tool Choice 검증
3. Arguments 검증
4. Risk Level 분류
5. Human Confirmation 필요 여부 확인
6. 실행
7. Tool Result Validation
8. Final Output 반영
```

---

### [주의]

Evaluation Best Practice 주의사항:

- 모든 작업에 Full Evaluation Report를 강제하면 비효율적일 수 있다.
- Safety와 Grounding은 간소화하더라도 생략하지 않는다.
- 사용자 요구사항과 충돌하는 일반 관례를 우선하지 않는다.
- 지나치게 엄격한 Review는 False Positive를 늘릴 수 있다.
- 지나치게 느슨한 Review는 False Negative를 늘릴 수 있다.
- Evidence 없는 점수나 Finding은 신뢰도가 낮다.
- Best Practice는 실제 실패 사례를 반영해 계속 보강한다.

---

### [Best Practice]

Evaluation 운영 Best Practice:

- 작업 유형별 Checklist를 준비한다.
- Evaluation Report Template을 표준화한다.
- Severity 기준을 고정한다.
- Source Priority를 명확히 둔다.
- Guardrails를 Prompt / Tool / RAG / Memory / Workflow로 분리한다.
- Review Agent 자체도 평가한다.
- 반복 Failure는 Troubleshooting 문서에 반영한다.
- 문서 작성 시 Retrieval Queries를 강화한다.
- 위험 작업은 Human Confirmation을 요구한다.
- 완료 전 Final Decision을 명확히 둔다.

---

### [FAQ]

Q. Agent Evaluation Best Practices는 뭐야?
A. Agent Output, RAG, Tool, Workflow, Review, Memory, Safety를 일관되게 평가하기 위한 운영 기준이다.

Q. 가장 중요한 Best Practice는 뭐야?
A. User Requirement 우선, Evidence 기반 검증, Safety 우선, Unsupported Claim 제거다.

Q. 모든 작업에 Full Evaluation Report가 필요해?
A. 아니다. 작업 위험도와 복잡도에 따라 축소 Template을 사용할 수 있다.

Q. Safety와 Grounding은 생략해도 돼?
A. 안 된다. 간소화는 가능하지만 생략하면 Agent 신뢰도가 떨어진다.

Q. Best Practice의 최종 목표는 뭐야?
A. Agent Workflow가 반복 가능하고 안전하며 근거 기반으로 동작하도록 만드는 것이다.

---

# 9. Guardrails Best Practices

## 9.1 Guardrails Design Best Practices

### [개념]

Guardrails Best Practices는 Agent가 요구사항, 근거, 안전, 범위, 출력 형식을 지키도록 제한 규칙을 설계하는 기준이다.

Guardrails는 하나의 Prompt만으로 완성되지 않는다.

Prompt Guardrails, Tool Guardrails, RAG Guardrails, Memory Guardrails, Workflow Guardrails, Safety Guardrails를 함께 설계해야 한다.

---

### [핵심]

Guardrails 구성:

| Guardrail           | 핵심 역할                                           |
| ------------------- | --------------------------------------------------- |
| Prompt Guardrails   | 역할, 범위, 출력 형식, 금지 조건 제한               |
| Tool Guardrails     | Tool 선택, Arguments, Permission, Risk 통제         |
| RAG Guardrails      | Retrieved Context 기반 답변, Unsupported Claim 방지 |
| Memory Guardrails   | 오래된 Memory, 민감정보, 충돌 정보 통제             |
| Workflow Guardrails | Routing, Handoff, Stop Condition 통제               |
| Safety Guardrails   | 위험 작업, Secret, Side Effect 통제                 |

Guardrails Design Flow:

```text
Agent Role
→ Identify Risks
→ Define Scope
→ Define Must / Must Not
→ Define Tool Permissions
→ Define Grounding Rules
→ Define Stop Conditions
→ Test with Failure Cases
```

Guardrails 균형 기준:

```text
Too Weak:
- Hallucination 증가
- 위험 Tool 실행
- Scope Violation
- Secret 노출

Too Strict:
- False Positive 증가
- 정상 작업 진행 불가
- 불필요한 Ask 증가

Balanced:
- Low Risk는 허용
- Medium Risk는 검증
- High Risk는 승인
- Block Risk는 차단
```

---

### [실무]

Agent별 Guardrails 예시:

PM Agent:

```text
- 사용자 요구사항을 임의 변경하지 않는다.
- Domain과 Risk를 분류한다.
- Specialist Agent로 Routing한다.
- Handoff에는 Context와 Constraints를 포함한다.
- 위험 작업은 Safety Agent 또는 Human Confirmation으로 보낸다.
```

Backend Agent:

```text
- Java 21 / Spring Boot 3.x 기준을 따른다.
- 프로젝트에 없는 클래스 / 메서드를 생성하지 않는다.
- 검증 불가 Symbol은 Assumption으로 표시한다.
- Layer 책임을 지킨다.
```

Tool Agent:

```text
- Tool Choice를 검증한다.
- Arguments를 검증한다.
- Risk Level을 분류한다.
- High Risk는 승인 전 실행하지 않는다.
- Tool Result를 Success / Partial / Failure로 분류한다.
```

Review Agent:

```text
- 사용자 요구사항과 Domain Rules 기준으로 검토한다.
- Finding마다 Evidence, Severity, Fix를 포함한다.
- False Positive와 False Negative를 관리한다.
```

Safety Agent:

```text
- Secret 노출을 차단한다.
- 위험 작업은 Human Confirmation을 요구한다.
- Scope와 Side Effect를 검증한다.
- Block 대상은 우회하지 않는다.
```

---

### [주의]

Guardrails Best Practice 주의사항:

- Prompt Guardrails만으로 Tool 안전성이 보장되지 않는다.
- Guardrails가 너무 약하면 위험 작업이 통제되지 않는다.
- Guardrails가 너무 강하면 정상 작업도 수행하지 못한다.
- 모든 위험을 사용자 확인으로 넘기면 자동화 장점이 줄어든다.
- Block 대상과 Ask 대상을 구분해야 한다.
- Guardrails는 실제 실패 사례를 반영해 업데이트해야 한다.
- Memory와 RAG 충돌은 별도 Guardrails가 필요하다.

---

### [Best Practice]

Guardrails Design Best Practice:

- Agent 역할별 Guardrails를 분리한다.
- Must / Must Not을 명확히 작성한다.
- Risk Level 기준을 고정한다.
- Tool Permission Matrix를 만든다.
- Human Confirmation 조건을 명확히 둔다.
- Stop Condition과 Retry Limit을 포함한다.
- RAG Grounding Rule을 포함한다.
- Memory Recency / Conflict Rule을 포함한다.
- 실패 사례 기반으로 Guardrails를 보강한다.
- Guardrails 자체도 Review 대상에 포함한다.

---

### [FAQ]

Q. Guardrails Best Practices는 뭐야?
A. Agent가 요구사항, 근거, 안전, 범위를 지키도록 제한 규칙을 설계하는 기준이다.

Q. Prompt Guardrails만 있으면 충분해?
A. 아니다. Tool, RAG, Memory, Workflow, Safety Guardrails가 함께 필요하다.

Q. Guardrails가 너무 강하면 어떻게 돼?
A. 정상 작업도 진행하지 못하고 False Positive와 불필요한 Ask가 증가할 수 있다.

Q. Guardrails가 너무 약하면 어떻게 돼?
A. Hallucination, 위험 Tool 실행, Scope Violation, Secret 노출 위험이 증가한다.

Q. 좋은 Guardrails는 어떤 상태야?
A. Low Risk는 허용하고, Medium Risk는 검증하며, High Risk는 승인받고, Block Risk는 차단하는 균형 잡힌 상태다.

---

# 10. Troubleshooting Checklist

## 10.1 Checklist

### [개념]

Troubleshooting Checklist는 Agent 문제를 진단하고 개선사항을 재발 방지 규칙으로 연결하기 위한 최소 검증 목록이다.

이 Checklist는 PM Agent, Review Agent, Safety Agent, Orchestrator가 공통으로 사용할 수 있다.

---

### [핵심]

Troubleshooting Checklist:

```md
### [Checklist]

- [ ] Problem이 구체적으로 정의되었는가?
- [ ] Symptom과 Root Cause를 구분했는가?
- [ ] Evidence를 확보했는가?
- [ ] 관련 영역을 분류했는가?
- [ ] 즉시 Fix가 있는가?
- [ ] 재발 방지 Prevention이 있는가?
- [ ] Prompt / Checklist / Domain Rules 중 어디에 반영할지 정했는가?
- [ ] RAG 문제라면 Retrieval Queries 개선이 필요한가?
- [ ] Review 문제라면 False Positive / False Negative를 확인했는가?
- [ ] Safety 문제라면 Critical로 처리했는가?
- [ ] Memory 문제라면 Recency / Project Boundary를 확인했는가?
- [ ] Workflow 문제라면 Routing / Handoff / State를 확인했는가?
- [ ] Fix 후 Re-evaluation을 수행했는가?
```

최소 Pass 기준:

```text
- Problem 명확
- Evidence 있음
- Cause 추정 근거 있음
- Fix 있음
- Prevention 있음
- 관련 Guardrail 또는 Checklist 개선으로 연결됨
```

---

### [실무]

Troubleshooting Result 예시:

```md
| Problem        | Evidence          | Cause                  | Fix          | Prevention                |
| -------------- | ----------------- | ---------------------- | ------------ | ------------------------- |
| 문서 미검색    | Query 실패        | Retrieval Queries 부족 | FAQ 추가     | 실제 질문 표현 추가       |
| Tool 실패 은폐 | Permission denied | Result Validation 없음 | 실패 표시    | Post-Tool Checklist       |
| Review 오탐    | FAQ 줄이라고 지적 | 요구사항 무시          | Finding 제거 | User Requirement Priority |
```

운영 반영 예시:

```text
Problem:
RAG 문서가 검색되지 않음

Immediate Fix:
- 해당 문서에 FAQ와 Retrieval Queries 보강

Prevention:
- 앞으로 모든 문서에 실제 사용자 질문 표현 20개 이상 추가
```

---

### [주의]

Troubleshooting Checklist 주의사항:

- Checklist는 최소 기준이다.
- Evidence가 없으면 원인을 확정하지 않는다.
- 단발성 문제와 반복 문제를 구분한다.
- 반복 문제는 반드시 Prevention으로 연결한다.
- Safety 문제는 일반 개선사항으로 낮추지 않는다.
- Troubleshooting 결과가 실제 문서나 Prompt에 반영되지 않으면 재발한다.
- Fix 후 검수하지 않으면 Regression이 남을 수 있다.

---

### [Best Practice]

Troubleshooting Checklist Best Practice:

- 문제를 짧고 구체적으로 기록한다.
- Evidence를 먼저 적는다.
- Cause는 확정 / 추정 / Unknown으로 구분한다.
- Fix와 Prevention을 분리한다.
- 반복 문제는 Domain Rules 개선 후보로 남긴다.
- Safety 문제는 즉시 Guardrails 강화로 연결한다.
- RAG 문제는 FAQ / Retrieval Queries 개선으로 연결한다.
- Review 문제는 Review Agent Evaluation으로 연결한다.
- Workflow 문제는 Routing / Handoff Template 개선으로 연결한다.

---

### [FAQ]

Q. Troubleshooting Checklist는 뭐야?
A. Agent 문제를 진단하고 개선사항을 재발 방지 규칙으로 연결하기 위한 최소 검증 목록이다.

Q. Troubleshooting에서 Fix와 Prevention은 뭐가 달라?
A. Fix는 현재 문제 해결이고, Prevention은 같은 문제가 다시 생기지 않게 하는 규칙이다.

Q. Evidence가 없으면 어떻게 해?
A. 원인을 확정하지 말고 Assumption 또는 Unknown으로 표시해야 한다.

Q. 반복 문제는 어떻게 처리해?
A. Prompt, Checklist, Domain Rules, Retrieval Queries 중 적절한 곳에 반영해야 한다.

Q. Troubleshooting의 최종 목표는 뭐야?
A. Agent 문제를 단발성 수정으로 끝내지 않고 재발 방지 규칙으로 바꾸는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Agent Troubleshooting이 뭐야?
A. Agent 운영 중 반복적으로 발생하는 문제를 진단하고 해결 및 재발 방지 규칙으로 정리하는 과정이다.

Q. Troubleshooting은 Failure 문서와 뭐가 달라?
A. Failure 문서는 실패 유형과 복구 전략 중심이고, Troubleshooting은 실제 문제 사례와 재발 방지 중심이다.

Q. Troubleshooting 기본 구조는 뭐야?
A. Problem, Cause, Evidence, Fix, Prevention 구조다.

Q. Troubleshooting 결과는 어디에 반영해?
A. Prompt, Checklist, Domain Rules, Retrieval Queries, Agent Workflow 규칙에 반영한다.

Q. Retrieval Failure는 어떻게 개선해?
A. FAQ, Retrieval Queries, Header, Chunk 구조, 용어 통일을 개선한다.

Q. 검색 결과가 없으면 문서가 없다는 뜻이야?
A. 아니다. Query 표현, 문서 구조, FAQ, Retrieval Queries 문제일 수 있다.

Q. Retrieval Queries는 왜 중요해?
A. 실제 사용자 질문 표현과 문서 내용을 연결해 검색 성공률을 높인다.

Q. Grounding Troubleshooting은 뭐야?
A. Agent가 근거 없는 답변을 생성하는 문제를 Claim-Evidence 검증으로 해결하는 과정이다.

Q. Agent가 문서에 없는 API를 만들면 어떻게 해?
A. Fabricated API로 보고 Claim을 제거하거나 실제 Context 기준으로 수정해야 한다.

Q. Weak Evidence는 어떻게 처리해?
A. 확정 표현을 피하고 Assumption 또는 Partial로 낮춰야 한다.

Q. Format Troubleshooting은 뭐야?
A. Agent Output이 요구된 Markdown, JSON, Schema, Required Section 형식을 지키지 못하는 문제를 해결하는 과정이다.

Q. JSON이 자꾸 깨지면 어떻게 해?
A. Schema를 단순화하고 순수 JSON만 출력하도록 하며 Required Field를 명확히 해야 한다.

Q. Markdown RAG 문서는 무엇을 확인해야 해?
A. FileName, Document Title, Required Section, FAQ Q/A, Retrieval Queries, Header 계층을 확인해야 한다.

Q. Review Troubleshooting은 뭐야?
A. Review Agent의 오탐, 누락, Severity 오류, 근거 부족 문제를 개선하는 과정이다.

Q. False Positive는 어떻게 줄여?
A. 사용자 요구사항, Domain Rules, Evidence를 기준으로 Finding을 검증해야 한다.

Q. False Negative는 어떻게 줄여?
A. Required Section, Safety, Grounding, Format, Code Checklist를 고정 적용해야 한다.

Q. Workflow Troubleshooting은 뭐야?
A. Multi-Agent Workflow의 Routing, Handoff, State, Review-Fix 문제를 개선하는 과정이다.

Q. Handoff가 약하면 어떤 문제가 생겨?
A. 다음 Agent가 Context 부족으로 잘못된 가정이나 Hallucination을 만들 수 있다.

Q. Fix 후 새 문제가 생기면 어떻게 해?
A. Regression으로 보고 Re-evaluation과 Required Section Checklist를 적용해야 한다.

Q. Memory Troubleshooting은 뭐야?
A. 오래된 Memory, 다른 프로젝트 Memory, 현재 요청과 충돌하는 Memory 사용 문제를 개선하는 과정이다.

Q. Memory와 현재 요청이 충돌하면 무엇을 우선해?
A. 현재 사용자 요청을 우선해야 한다.

Q. 다른 프로젝트 Memory를 현재 프로젝트에 써도 돼?
A. 안 된다. 프로젝트 경계를 지켜야 한다.

Q. Agent Evaluation Best Practices는 뭐야?
A. Agent Output, RAG, Tool, Workflow, Review, Memory, Safety를 일관되게 평가하기 위한 운영 기준이다.

Q. 가장 중요한 Best Practice는 뭐야?
A. User Requirement 우선, Evidence 기반 검증, Safety 우선, Unsupported Claim 제거다.

Q. Guardrails Best Practices는 뭐야?
A. Agent가 요구사항, 근거, 안전, 범위를 지키도록 제한 규칙을 설계하는 기준이다.

Q. Prompt Guardrails만 있으면 충분해?
A. 아니다. Tool, RAG, Memory, Workflow, Safety Guardrails가 함께 필요하다.

Q. 좋은 Guardrails는 어떤 상태야?
A. Low Risk는 허용하고, Medium Risk는 검증하며, High Risk는 승인받고, Block Risk는 차단하는 균형 잡힌 상태다.

Q. Troubleshooting Checklist는 뭐야?
A. Agent 문제를 진단하고 개선사항을 재발 방지 규칙으로 연결하기 위한 최소 검증 목록이다.

Q. Fix와 Prevention은 뭐가 달라?
A. Fix는 현재 문제 해결이고, Prevention은 같은 문제가 다시 생기지 않게 하는 규칙이다.

Q. Troubleshooting & Best Practices의 최종 목표는 뭐야?
A. Agent 문제를 단발성 수정으로 끝내지 않고 재발 방지 규칙으로 바꿔 Multi-Agent Workflow를 안정적으로 운영하는 것이다.
