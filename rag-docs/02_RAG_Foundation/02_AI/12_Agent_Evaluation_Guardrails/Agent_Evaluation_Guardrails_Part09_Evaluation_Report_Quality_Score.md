# Agent Evaluation & Guardrails Part09 - Evaluation Report & Quality Score

---

# 1. Evaluation Report

## 1.1 Evaluation Report Core

### [개념]

Evaluation Report는 Agent Output, Tool Calling, Workflow, Review, Fix 결과를 구조화해서 평가하는 리포트 형식이다.

Evaluation Report의 목적은 Agent 결과가 요구사항, 근거, 형식, 안전 기준을 만족하는지 추적 가능하게 기록하는 것이다.

Evaluation Report는 단순 감상문이 아니다.

Evaluation Report는 다음 판단에 사용된다.

- Pass
- Fix
- Stop
- Retry
- Fallback
- Human Confirmation
- Workflow 개선

Evaluation Report는 Evidence와 Fix Recommendation을 포함해야 한다.

---

### [핵심]

Evaluation Report 필수 요소:

- Evaluation Target
- Evaluation Scope
- User Requirement
- Evaluation Criteria
- Result
- Findings
- Severity
- Evidence
- Fix Recommendation
- Final Decision

Evaluation Report 기본 Flow:

```text
Agent Output
→ Extract Requirements
→ Apply Evaluation Criteria
→ Identify Findings
→ Assign Severity
→ Add Evidence
→ Recommend Fix
→ Decide Pass / Fix / Stop
```

Evaluation Report 기본 Format:

```md
# Evaluation Report

## Summary

- Target:
- Scope:
- Result:
- Final Decision:

## Requirement Compliance

| Requirement | Result | Evidence | Fix |
| ----------- | ------ | -------- | --- |

## Findings

| Severity | Category | Issue | Evidence | Fix Recommendation |
| -------- | -------- | ----- | -------- | ------------------ |

## Final Decision

Pass / Fix / Stop
```

Evaluation Report 결과:

```text
Pass:
- Critical / Major Finding 없음
- 요구사항 충족
- 근거 충분
- 형식 정상
- 안전 문제 없음

Fix:
- Major 또는 Minor Finding 존재
- 수정 후 재검토 필요

Stop:
- Critical Finding 존재
- 정보 부족
- 위험 작업 승인 필요
- Tool 실패 후 Fallback 없음
```

---

### [실무]

2026 실무 기준 Evaluation Report는 Multi-Agent Workflow의 품질 기록이다.

개인 AI 개발팀에서는 PM Agent, Review Agent, Safety Agent, Fix Agent가 Evaluation Report를 공유할 수 있다.

실무 사용 위치:

```text
Specialist Agent Output
→ Evaluation Report
→ Fix Agent
→ Re-evaluation
→ Final Output
```

Agent Output Evaluation Report 예시:

```md
# Evaluation Report

## Summary

- Target: Backend Agent Output
- Scope: Notification Service Review
- Result: Fix Required
- Final Decision: Fix

## Requirement Compliance

| Requirement                 | Result | Evidence                       | Fix                    |
| --------------------------- | ------ | ------------------------------ | ---------------------- |
| Java 21 기준                | Pass   | 코드 문법 호환                 | 없음                   |
| Spring Boot 3.x 기준        | Pass   | Jakarta 기반 사용              | 없음                   |
| 실제 Repository 메서드 사용 | Fail   | findUnreadByUserId() 근거 없음 | 실제 메서드명으로 수정 |

## Findings

| Severity | Category           | Issue                                | Evidence                          | Fix Recommendation                         |
| -------- | ------------------ | ------------------------------------ | --------------------------------- | ------------------------------------------ |
| Major    | Code Hallucination | 존재하지 않는 Repository 메서드 사용 | Repository Context에 없음         | countByUsers_UserIdAndReadStatusFalse 사용 |
| Minor    | Naming Consistency | DTO 이름 혼용                        | UserResDto / UserResponseDto 혼용 | UserResDto로 통일                          |

## Final Decision

Fix
```

Safety Evaluation Report 예시:

```md
# Safety Evaluation Report

## Summary

- Target: DB Delete Tool Call
- Result: Stop
- Final Decision: Human Confirmation Required

## Findings

| Severity | Category | Issue                    | Evidence       | Fix Recommendation                 |
| -------- | -------- | ------------------------ | -------------- | ---------------------------------- |
| Critical | Safety   | DB DELETE 작업 승인 없음 | High Risk 작업 | Action Preview 후 사용자 승인 필요 |
```

---

### [주의]

Evaluation Report 주의사항:

- Evidence 없는 Finding은 신뢰도가 낮다.
- Severity 기준이 없으면 Fix 우선순위가 흐려진다.
- 취향과 결함을 구분해야 한다.
- Critical Finding을 Minor처럼 처리하면 안 된다.
- Pass / Fix / Stop 판정을 모호하게 쓰지 않는다.
- Tool Failure를 숨기면 안 된다.
- Unsupported Claim을 일반 개선사항처럼 낮게 처리하면 안 된다.
- Evaluation Report 자체도 Format Compliance 대상이다.

---

### [Best Practice]

Evaluation Report Best Practice:

- Summary에서 최종 판정을 먼저 제시한다.
- Requirement Compliance를 별도 표로 분리한다.
- Finding마다 Severity, Category, Evidence, Fix를 포함한다.
- Evidence는 실제 Output, Retrieved Context, Tool Result 기준으로 작성한다.
- Fix Recommendation은 실행 가능하게 작성한다.
- Pass / Fix / Stop을 명확히 표시한다.
- Critical Issue는 Stop 또는 즉시 Fix로 처리한다.
- Minor Issue는 Workflow를 과도하게 막지 않는다.
- Report는 후속 Fix Agent가 바로 사용할 수 있게 구조화한다.

---

### [FAQ]

Q. Evaluation Report가 뭐야?
A. Agent Output, Tool Calling, Workflow, Review, Fix 결과를 구조화해서 평가하는 리포트다.

Q. Evaluation Report에는 뭐가 들어가?
A. Evaluation Target, User Requirement, Evaluation Criteria, Result, Findings, Severity, Evidence, Fix Recommendation, Final Decision이 들어간다.

Q. Evaluation Report는 왜 필요해?
A. Agent 결과의 문제와 수정 방향을 추적 가능하게 만들기 위해 필요하다.

Q. Evidence가 없는 Finding도 괜찮아?
A. 좋지 않다. Evidence 없는 Finding은 근거 없는 지적이 될 수 있다.

Q. Evaluation Report 결과는 어떻게 나눠?
A. Pass, Fix, Stop으로 나눈다.

---

# 2. Finding & Severity

## 2.1 Finding Classification

### [개념]

Finding은 Evaluation 과정에서 발견된 문제, 누락, 위험, 개선 필요 사항이다.

Finding Classification은 발견된 문제를 유형별로 분류해 Fix 방향을 명확히 하는 기준이다.

Finding은 반드시 Evidence와 연결되어야 한다.

---

### [핵심]

Finding 주요 유형:

| Finding Type         | 의미                                       |
| -------------------- | ------------------------------------------ |
| Requirement Finding  | 요구사항 누락 또는 위반                    |
| Grounding Finding    | 근거 부족 또는 Unsupported Claim           |
| Faithfulness Finding | Context 왜곡 또는 과장                     |
| Format Finding       | 출력 형식 위반                             |
| Code Finding         | 코드 문법, 구조, 프로젝트 규칙 문제        |
| Tool Finding         | Tool 선택, Arguments, 실행 결과 문제       |
| Safety Finding       | 위험 작업, 승인 누락, Secret 노출          |
| Workflow Finding     | Routing, Handoff, State, Review / Fix 문제 |
| Memory Finding       | 오래된 Memory, 충돌 Memory 사용            |

Severity 기준:

| Severity | 의미                                                         | 처리               |
| -------- | ------------------------------------------------------------ | ------------------ |
| Critical | 안전 문제, 데이터 손실, 핵심 요구 위반, 치명적 Hallucination | Stop 또는 즉시 Fix |
| Major    | 주요 요구사항 누락, 근거 부족, 코드 오류, Workflow 결함      | Fix                |
| Minor    | 작은 형식 오류, 표현 문제, 일부 개선 필요                    | 가능하면 Fix       |
| Info     | 참고 사항, 선택적 개선                                       | 보고만 가능        |

Finding Evaluation Flow:

```text
Detected Issue
→ Classify Finding Type
→ Assign Severity
→ Attach Evidence
→ Add Fix Recommendation
```

---

### [실무]

실무에서는 Finding을 단순 나열하지 않고 Severity와 Fix 가능성 기준으로 정리한다.

Finding 예시:

```md
| Severity | Type      | Issue                     | Evidence                 | Fix                    |
| -------- | --------- | ------------------------- | ------------------------ | ---------------------- |
| Critical | Safety    | Secret 전체 출력          | API Key 값 노출          | 즉시 마스킹            |
| Major    | Grounding | 문서에 없는 API 생성      | Retrieved Context에 없음 | API Claim 제거         |
| Major    | Code      | 존재하지 않는 메서드 사용 | Repository에 없음        | 실제 메서드명으로 수정 |
| Minor    | Format    | Header 계층 일부 불일치   | H2 다음 H4 사용          | H3로 수정              |
| Info     | Style     | 표 설명 추가 가능         | 비교 기준 보강 가능      | 선택                   |
```

Severity 판단 예시:

```text
Critical:
- 운영 DB DELETE 승인 없음
- Secret 노출
- 위험 Tool 자동 실행
- 핵심 프로젝트 API Hallucination

Major:
- Required Section 누락
- Retrieval Queries 누락
- 존재하지 않는 클래스 사용
- Review Finding 미반영

Minor:
- FAQ 답변 일부 장문
- Table 정렬 불일치
- 용어 일부 혼용

Info:
- 예시 추가 가능
- Checklist 확장 가능
```

Severity Decision Rule:

```text
If Safety Risk or Data Loss:
→ Critical

If Requirement Failure or Grounding Failure:
→ Major or Critical

If Format affects parser / RAG indexing:
→ Major

If cosmetic only:
→ Minor or Info
```

---

### [주의]

Finding & Severity 주의사항:

- 모든 Finding을 동일한 중요도로 처리하지 않는다.
- 취향을 Critical로 과장하지 않는다.
- Safety Finding은 낮게 평가하지 않는다.
- Unsupported Claim이 핵심 결론이면 Major 이상이다.
- Secret 노출은 Critical 또는 Block이다.
- Evidence 없는 Finding은 보완하거나 제외한다.
- Fix 불필요한 Info를 Workflow Blocker로 만들지 않는다.

---

### [Best Practice]

Finding & Severity Best Practice:

- Finding마다 Type을 지정한다.
- Finding마다 Severity를 지정한다.
- Finding마다 Evidence를 포함한다.
- Finding마다 Fix Recommendation을 작성한다.
- Critical / Major를 우선 수정한다.
- Minor / Info는 작업 목표에 따라 처리한다.
- False Positive는 Finding에서 제거하거나 별도 표시한다.
- Severity 기준을 문서화해 Review Agent 일관성을 높인다.

---

### [FAQ]

Q. Finding이 뭐야?
A. Evaluation 과정에서 발견된 문제, 누락, 위험, 개선 필요 사항이다.

Q. Severity는 왜 필요해?
A. 문제의 우선순위와 Fix 필요성을 판단하기 위해 필요하다.

Q. Critical Finding은 뭐야?
A. 안전 문제, 데이터 손실, 핵심 요구 위반, 치명적 Hallucination처럼 즉시 중단 또는 수정해야 하는 문제다.

Q. Major Finding은 뭐야?
A. 주요 요구사항 누락, 근거 부족, 코드 오류, Workflow 결함처럼 Fix가 필요한 문제다.

Q. Minor Finding은 뭐야?
A. 작은 형식 오류나 표현 문제처럼 가능하면 수정하는 문제다.

Q. Info Finding도 Fix해야 해?
A. 필수는 아니다. 참고 또는 선택적 개선 사항으로 볼 수 있다.

---

# 3. Evidence & Fix Recommendation

## 3.1 Evidence in Evaluation Report

### [개념]

Evidence는 Evaluation Report의 Finding을 뒷받침하는 근거다.

Evidence가 없으면 Review Finding은 신뢰하기 어렵다.

Evidence는 Agent Output, Retrieved Context, Tool Result, 사용자 요구사항, 코드, 설정 파일, 로그, Project Progress, Domain Rules에서 가져올 수 있다.

---

### [핵심]

Evidence 유형:

| Evidence Type     | 예시                              |
| ----------------- | --------------------------------- |
| User Requirement  | 사용자가 명시한 조건              |
| Agent Output      | Agent가 실제 작성한 문장 / 코드   |
| Retrieved Context | RAG 검색 문서 Chunk               |
| Tool Result       | 파일 검색, 테스트 실행, 빌드 결과 |
| Code Evidence     | 실제 클래스, 메서드, 필드         |
| Config Evidence   | 설정 파일 값                      |
| Log Evidence      | 오류 로그                         |
| Progress Evidence | Completed / Planned 상태          |
| Rule Evidence     | Master Rules / Domain Rules       |

Evidence 작성 기준:

```text
Good Evidence:
- 구체적
- Finding과 직접 연결
- 출처가 명확
- 검증 가능

Bad Evidence:
- 막연함
- 느낌 중심
- Finding과 연결 약함
- 출처 없음
```

Fix Recommendation 기준:

| 기준       | 의미                          |
| ---------- | ----------------------------- |
| Specific   | 수정 대상과 방법이 구체적인가 |
| Actionable | 실제 실행 가능한가            |
| Scoped     | 요청 범위 안인가              |
| Safe       | 위험 작업을 유발하지 않는가   |
| Grounded   | 근거 기반인가                 |
| Testable   | 수정 후 검증 가능한가         |

---

### [실무]

좋은 Evidence 예시:

```md
| Finding                   | Evidence                                            |
| ------------------------- | --------------------------------------------------- |
| Retrieval Queries 누락    | 문서 마지막에 `# Retrieval Queries` 섹션이 없음     |
| 존재하지 않는 메서드 사용 | Repository Context에 `findUnreadByUserId()` 없음    |
| Safety 승인 누락          | Action이 DB DELETE인데 Human Confirmation 기록 없음 |
```

나쁜 Evidence 예시:

```text
- 뭔가 이상함
- 코드가 별로임
- 문서가 약함
```

좋은 Fix Recommendation 예시:

```text
Issue:
Retrieval Queries 누락

Fix:
문서 마지막에 `# Retrieval Queries`를 추가하고, 실제 사용자 검색 질문 표현을 Q/A 형식으로 10개 이상 작성한다.
```

나쁜 Fix Recommendation 예시:

```text
더 좋게 고치기.
```

Evidence & Fix Report 예시:

```md
| Severity | Issue             | Evidence                      | Fix Recommendation               |
| -------- | ----------------- | ----------------------------- | -------------------------------- |
| Major    | [FAQ] 누락        | Required Section에 [FAQ] 없음 | 각 주요 섹션에 Q/A 형식 FAQ 추가 |
| Major    | Unsupported Claim | API 경로 근거 없음            | Claim 제거 또는 Assumption 표시  |
| Critical | Secret 노출       | API Key 전체 출력             | 즉시 마스킹하고 Memory 저장 금지 |
```

---

### [주의]

Evidence & Fix 주의사항:

- Evidence 없는 Fix는 임의 수정이 될 수 있다.
- Fix Recommendation이 추상적이면 Fix Agent가 적용하기 어렵다.
- Fix가 요청 범위를 벗어나면 Scope Violation이다.
- Fix가 새로운 위험 작업을 요구하면 Safety Evaluation이 필요하다.
- Evidence가 약하면 Severity를 낮추거나 Assumption으로 처리한다.
- Tool Result가 실패한 경우 성공 Evidence로 사용하지 않는다.

---

### [Best Practice]

Evidence & Fix Best Practice:

- Finding마다 Evidence를 1개 이상 연결한다.
- Evidence는 가능한 직접 근거를 사용한다.
- Fix는 구체적인 작업 단위로 작성한다.
- Fix는 사용자 요청 범위 안에서 제안한다.
- 안전 위험이 있는 Fix는 Human Confirmation 필요 여부를 표시한다.
- 수정 후 검증 방법을 포함한다.
- Evidence가 부족하면 Missing Information으로 표시한다.

---

### [FAQ]

Q. Evidence는 왜 필요해?
A. Review Finding이 실제 근거에 기반하는지 확인하기 위해 필요하다.

Q. 좋은 Evidence 조건은 뭐야?
A. 구체적이고, Finding과 직접 연결되며, 출처가 명확하고 검증 가능해야 한다.

Q. Fix Recommendation은 어떻게 써야 해?
A. 수정 대상과 방법을 구체적으로 쓰고 실제 적용 가능해야 한다.

Q. Evidence가 약하면 어떻게 해?
A. 확정적으로 판단하지 말고 Assumption, Unknown, Missing Information으로 처리해야 한다.

Q. Fix가 위험 작업이면 어떻게 해?
A. Safety Evaluation과 Human Confirmation 필요 여부를 표시해야 한다.

---

# 4. Quality Score

## 4.1 Quality Score Core

### [개념]

Quality Score는 Agent Output 품질을 여러 평가 항목별 점수로 표현하는 보조 기준이다.

Quality Score는 단일 총점으로 Agent 품질을 확정하기 위한 도구가 아니다.

Quality Score는 어떤 영역이 약한지 확인하고 Fix 우선순위를 정하는 데 사용한다.

---

### [핵심]

Quality Score 기본 항목:

| 항목                   | 점수 |
| ---------------------- | ---- |
| Requirement Compliance | 0~5  |
| Correctness            | 0~5  |
| Completeness           | 0~5  |
| Groundedness           | 0~5  |
| Faithfulness           | 0~5  |
| Format Compliance      | 0~5  |
| Safety                 | 0~5  |
| Actionability          | 0~5  |

점수 의미:

| Score | 의미                       |
| ----- | -------------------------- |
| 5     | 요구 기준 충족, 문제 없음  |
| 4     | 작은 개선 필요             |
| 3     | 일부 문제 있음, Fix 권장   |
| 2     | 주요 문제 있음, Fix 필요   |
| 1     | 치명적 문제에 가까움       |
| 0     | 기준 미충족 또는 평가 불가 |

Quality Score Flow:

```text
Agent Output
→ Evaluate Each Dimension
→ Assign Score
→ Identify Low Score Areas
→ Add Findings
→ Decide Pass / Fix / Stop
```

Quality Score 사용 원칙:

```text
- 항목별 점수를 분리한다.
- 총점보다 낮은 항목을 우선 확인한다.
- Safety 0~1이면 Stop 가능성이 높다.
- Groundedness 0~2이면 RAG 답변 Fix 필요.
- Format 0~2이면 Parser / RAG Indexing 실패 가능.
```

---

### [실무]

실무에서는 Quality Score를 Evaluation Report의 Summary에 포함할 수 있다.

Quality Score 예시:

```md
## Quality Score

| Criteria               | Score | Note                |
| ---------------------- | ----: | ------------------- |
| Requirement Compliance |     5 | 요구사항 모두 반영  |
| Correctness            |     4 | 일부 표현 보완 가능 |
| Completeness           |     5 | 필수 섹션 포함      |
| Groundedness           |     5 | Domain Rules 기반   |
| Faithfulness           |     5 | Context 왜곡 없음   |
| Format Compliance      |     5 | Markdown 구조 정상  |
| Safety                 |     5 | 위험 작업 없음      |
| Actionability          |     4 | 예시 추가 가능      |
```

Quality Decision 예시:

```text
Pass:
- 모든 핵심 항목 4 이상
- Safety 5
- Critical Finding 없음

Fix:
- 하나 이상의 핵심 항목 2~3
- Major Finding 존재

Stop:
- Safety 0~1
- Groundedness 0~1
- Critical Finding 존재
```

RAG 문서 품질 기준 예시:

```text
Target:
- Minimum 95/100
- Target 97+/100

Evaluation:
- 필수 섹션 포함
- Chunk 품질
- FAQ 강화
- Retrieval Queries 포함
- 용어 통일
- 중복 최소화
- 오타 최소화
```

---

### [주의]

Quality Score 주의사항:

- 단일 총점만으로 판단하지 않는다.
- 점수가 높아도 Critical Safety Issue가 있으면 Stop이다.
- 점수 기준이 모호하면 Review 일관성이 낮아진다.
- 자동 점수는 보조 지표다.
- Evidence 없는 점수는 신뢰하기 어렵다.
- Format 점수가 높아도 Groundedness가 낮을 수 있다.
- 답변이 길다고 Completeness 점수가 높아지는 것은 아니다.

---

### [Best Practice]

Quality Score Best Practice:

- 항목별 점수를 사용한다.
- 점수마다 짧은 Note를 붙인다.
- 낮은 점수 항목은 Finding으로 연결한다.
- Safety와 Groundedness는 높은 우선순위로 본다.
- 총점보다 Critical / Major Finding 여부를 우선한다.
- RAG 문서는 Retrieval 최적화 기준을 별도로 점검한다.
- 점수 기준을 Agent별로 고정한다.
- 반복 평가 결과를 Workflow 개선에 사용한다.

---

### [FAQ]

Q. Quality Score가 뭐야?
A. Agent Output 품질을 여러 평가 항목별 점수로 표현하는 보조 기준이다.

Q. Quality Score만 보면 돼?
A. 아니다. 점수보다 Findings, Evidence, Fix Recommendation이 더 중요하다.

Q. 단일 총점으로 판단해도 돼?
A. 안 된다. 항목별 점수를 분리해야 개선 방향이 명확하다.

Q. Safety 점수가 낮으면 어떻게 해?
A. Stop 또는 즉시 Fix 대상이다.

Q. Groundedness 점수가 낮으면 어떻게 해?
A. Unsupported Claim을 제거하고 Evidence 기반으로 다시 작성해야 한다.

---

# 5. Pass / Fix / Stop Decision

## 5.1 Final Decision Rule

### [개념]

Pass / Fix / Stop Decision은 Evaluation 결과를 바탕으로 Agent Output을 통과시킬지, 수정할지, 중단할지 결정하는 기준이다.

Final Decision은 Findings, Severity, Quality Score, Safety, Grounding, Requirement Compliance를 종합해 판단한다.

---

### [핵심]

Decision 기준:

| Decision | 조건                                                        |
| -------- | ----------------------------------------------------------- |
| Pass     | 요구사항 충족, Critical / Major 없음, 안전 문제 없음        |
| Fix      | Major / Minor Finding 존재, 수정 가능                       |
| Stop     | Critical Finding, 정보 부족, 위험 작업 승인 필요, Tool 실패 |
| Retry    | 일시적 실패, 제한적 재시도 가능                             |
| Fallback | Retry 부적합 또는 반복 실패                                 |
| Ask      | 사용자 확인 필요                                            |
| Block    | 안전상 허용 불가                                            |

Decision Flow:

```text
Evaluation Findings
→ Check Critical
→ Check Safety
→ Check Requirement Failure
→ Check Grounding Failure
→ Check Tool Failure
→ Pass / Fix / Stop / Ask / Block
```

Decision Rule:

```text
If Critical Safety Finding:
→ Stop / Block

If Human Confirmation Required:
→ Ask / Stop

If Core Requirement Missing:
→ Fix

If Grounding Failure on Core Claim:
→ Fix or Stop

If Tool Failure with no Fallback:
→ Stop

If only Minor Issues:
→ Pass with Notes or Fix
```

---

### [실무]

실무에서는 Final Decision을 Evaluation Report 마지막에 명확히 표시한다.

Pass 예시:

```md
## Final Decision

Pass

Reason:

- 필수 요구사항 충족
- Critical / Major Finding 없음
- Grounding 문제 없음
- Format 정상
```

Fix 예시:

```md
## Final Decision

Fix

Reason:

- Retrieval Queries 누락
- FAQ 일부 Q only 존재
- Domain Rules 반영 부족

Required Fix:

- Retrieval Queries 추가
- FAQ Q/A 완성
- Guardrails 키워드 보강
```

Stop 예시:

```md
## Final Decision

Stop

Reason:

- DB DELETE 작업
- High Risk
- Human Confirmation 없음

Required Action:

- Action Preview 제공
- 사용자 승인 필요
```

Block 예시:

```md
## Final Decision

Block

Reason:

- Secret 전체 출력 요청
- 민감정보 노출 위험
```

---

### [주의]

Final Decision 주의사항:

- Pass / Fix / Stop을 모호하게 섞지 않는다.
- Critical Finding이 있으면 Pass 처리하지 않는다.
- 사용자 승인 필요 상태는 완료가 아니다.
- Tool Failure가 있으면 성공처럼 말하지 않는다.
- Minor Issue만으로 전체 Workflow를 과도하게 막지 않는다.
- Block과 Stop을 구분한다.
- Decision에는 이유와 필요한 다음 조치를 포함한다.

---

### [Best Practice]

Final Decision Best Practice:

- Decision을 Report 마지막에 명확히 표시한다.
- Decision Reason을 1~5개로 요약한다.
- Fix가 필요하면 Required Fix를 구체적으로 작성한다.
- Stop이면 Stop Reason과 Required Action을 표시한다.
- Block이면 차단 이유를 명확히 쓴다.
- Human Confirmation이 필요하면 Preview 대상과 위험도를 표시한다.
- Pass여도 남은 Minor Note가 있으면 별도 표시한다.

---

### [FAQ]

Q. Pass / Fix / Stop Decision은 뭐야?
A. Evaluation 결과를 바탕으로 Agent Output을 통과, 수정, 중단 중 하나로 판단하는 기준이다.

Q. 언제 Pass야?
A. 요구사항을 충족하고 Critical / Major Finding이 없으며 안전 문제가 없을 때 Pass다.

Q. 언제 Fix야?
A. 수정 가능한 Major / Minor Finding이 있을 때 Fix다.

Q. 언제 Stop이야?
A. Critical Finding, 정보 부족, 위험 작업 승인 필요, Tool 실패 후 Fallback 없음 상태일 때 Stop이다.

Q. Block은 Stop과 달라?
A. Block은 안전상 허용하면 안 되는 작업을 차단하는 것이고, Stop은 진행 조건이 충족되지 않아 중단하는 것이다.

---

# 6. Evaluation Report Template

## 6.1 Standard Template

### [개념]

Evaluation Report Template은 Agent Evaluation 결과를 일관된 형식으로 작성하기 위한 표준 구조다.

Template을 사용하면 Review Agent, Fix Agent, PM Agent가 평가 결과를 쉽게 처리할 수 있다.

---

### [핵심]

Standard Evaluation Report Template:

```md
# Evaluation Report

## 1. Summary

- Evaluation Target:
- Evaluation Scope:
- Result:
- Final Decision:

---

## 2. Requirement Compliance

| Requirement | Result | Evidence | Fix |
| ----------- | ------ | -------- | --- |

---

## 3. Quality Score

| Criteria               | Score | Note |
| ---------------------- | ----: | ---- |
| Requirement Compliance |   0~5 |      |
| Correctness            |   0~5 |      |
| Completeness           |   0~5 |      |
| Groundedness           |   0~5 |      |
| Faithfulness           |   0~5 |      |
| Format Compliance      |   0~5 |      |
| Safety                 |   0~5 |      |
| Actionability          |   0~5 |      |

---

## 4. Findings

| Severity | Category | Issue | Evidence | Fix Recommendation |
| -------- | -------- | ----- | -------- | ------------------ |

---

## 5. Unsupported Claims

| Claim | Evidence Status | Handling |
| ----- | --------------- | -------- |

---

## 6. Safety Check

| Item                        | Result                      | Note |
| --------------------------- | --------------------------- | ---- |
| Risk Level                  | Low / Medium / High / Block |      |
| Human Confirmation Required | Yes / No                    |      |
| Secret Exposure             | Yes / No                    |      |
| Side Effect                 | Yes / No                    |      |

---

## 7. Final Decision

Pass / Fix / Stop / Ask / Block

## Reason:
```

---

### [실무]

작업 유형별 Template 축소 버전:

RAG 문서 검수 Template:

```md
# RAG Document Evaluation Report

## Summary

- Target:
- Result:
- Final Decision:

## Required Section Check

| Section | Result | Fix |
| ------- | ------ | --- |

## Retrieval Optimization Check

| Item | Result | Fix |
| ---- | ------ | --- |

## Findings

| Severity | Issue | Evidence | Fix |
| -------- | ----- | -------- | --- |

## Final Decision

Pass / Fix / Stop
```

Code Review Template:

```md
# Code Evaluation Report

## Summary

- Target:
- Result:
- Final Decision:

## Code Check

| Criteria | Result | Evidence | Fix |
| -------- | ------ | -------- | --- |

## Project Symbol Check

| Symbol | Type | Evidence | Result |
| ------ | ---- | -------- | ------ |

## Findings

| Severity | Issue | Evidence | Fix |
| -------- | ----- | -------- | --- |

## Final Decision

Pass / Fix / Stop
```

Tool Calling Template:

```md
# Tool Calling Evaluation Report

## Summary

- Tool:
- Action:
- Risk Level:
- Final Decision:

## Pre-Execution Check

| Item | Result | Note |
| ---- | ------ | ---- |

## Post-Execution Check

| Item | Result | Note |
| ---- | ------ | ---- |

## Final Decision

Allow / Ask / Block / Stop
```

---

### [주의]

Template 사용 주의사항:

- Template이 너무 복잡하면 Agent Output 품질이 낮아질 수 있다.
- 모든 작업에 Full Template을 강제할 필요는 없다.
- Parser가 필요한 경우 Field 이름을 고정한다.
- 사람이 읽는 장문보다 구조화된 표를 우선한다.
- Evidence 없는 Finding을 Template에 넣지 않는다.
- Safety Check는 위험 작업에서 생략하면 안 된다.
- Final Decision은 반드시 포함한다.

---

### [Best Practice]

Template Best Practice:

- 작업 유형별 축소 Template을 사용한다.
- Required Field를 최소화한다.
- Finding Table에는 Severity와 Evidence를 반드시 포함한다.
- Safety 관련 작업은 Risk Level과 Human Confirmation을 포함한다.
- RAG 문서 검수는 Retrieval Optimization Check를 포함한다.
- Code 검수는 Project Symbol Check를 포함한다.
- Tool 검수는 Pre / Post Execution Check를 분리한다.
- Final Decision은 고정된 enum처럼 사용한다.

---

### [FAQ]

Q. Evaluation Report Template은 왜 필요해?
A. Agent Evaluation 결과를 일관된 형식으로 작성하고 후속 Fix Agent가 처리하기 쉽게 만들기 위해 필요하다.

Q. 모든 작업에 Full Template을 써야 해?
A. 아니다. 작업 유형에 맞는 축소 Template을 사용할 수 있다.

Q. Template에서 꼭 필요한 항목은 뭐야?
A. Summary, Requirement Compliance, Findings, Evidence, Fix Recommendation, Final Decision이다.

Q. RAG 문서 검수 Template에는 뭐가 필요해?
A. Required Section Check, Retrieval Optimization Check, FAQ, Retrieval Queries 검증이 필요하다.

Q. Tool Calling Template에는 뭐가 필요해?
A. Risk Level, Pre-Execution Check, Post-Execution Check, Human Confirmation 여부가 필요하다.

---

# 7. Evaluation Report Checklist

## 7.1 Checklist

### [개념]

Evaluation Report Checklist는 평가 리포트가 요구사항, 근거, 형식, 안전 기준을 충족하는지 확인하는 최소 검증 목록이다.

이 Checklist는 Review Agent와 PM Agent가 Evaluation Report 자체를 검수할 때 사용한다.

---

### [핵심]

Evaluation Report Checklist:

```md
### [Checklist]

- [ ] Evaluation Target이 명확한가?
- [ ] Evaluation Scope가 명확한가?
- [ ] User Requirement가 반영되었는가?
- [ ] Evaluation Criteria가 명시되었는가?
- [ ] Requirement Compliance가 검증되었는가?
- [ ] Findings가 유형별로 분류되었는가?
- [ ] Severity가 지정되었는가?
- [ ] Evidence가 포함되었는가?
- [ ] Fix Recommendation이 구체적인가?
- [ ] Unsupported Claim이 별도 확인되었는가?
- [ ] Safety Check가 필요한 경우 포함되었는가?
- [ ] Quality Score가 필요한 경우 항목별로 작성되었는가?
- [ ] Final Decision이 명확한가?
- [ ] Pass / Fix / Stop 기준이 일관되는가?
```

최소 Pass 기준:

```text
- Target 명확
- Requirement Compliance 확인
- Finding + Evidence + Fix 포함
- Severity 포함
- Final Decision 포함
- Critical Issue 숨김 없음
```

---

### [실무]

Evaluation Report 자체도 Format Compliance와 Groundedness 평가 대상이다.

Report 검수 예시:

```md
| Checklist Item | Result | Issue                  | Fix                    |
| -------------- | ------ | ---------------------- | ---------------------- |
| Target 명확성  | Pass   | 없음                   | 없음                   |
| Evidence 포함  | Fix    | 일부 Finding 근거 없음 | Evidence 추가          |
| Severity 지정  | Pass   | Critical / Major 구분  | 없음                   |
| Final Decision | Fail   | 결론 없음              | Pass / Fix / Stop 추가 |
```

잘못된 Evaluation Report 예시:

```text
대체로 괜찮습니다. 조금 수정하면 좋습니다.
```

문제:

- Target 없음
- Criteria 없음
- Finding 없음
- Evidence 없음
- Final Decision 없음

좋은 Evaluation Report 요약 예시:

```text
Result:
Fix

Reason:
- Retrieval Queries 누락
- FAQ 일부 A 누락
- Unsupported Claim 1개 존재

Required Fix:
- Retrieval Queries 추가
- FAQ Q/A 완성
- Unsupported Claim 제거
```

---

### [주의]

Evaluation Report Checklist 주의사항:

- Report가 길어도 핵심 항목이 빠지면 실패다.
- Evidence 없는 Finding은 신뢰도가 낮다.
- Final Decision이 없으면 후속 Agent가 판단하기 어렵다.
- Quality Score만 있고 Findings가 없으면 수정 방향이 부족하다.
- Safety Check가 필요한 작업에서 Safety 항목을 생략하면 안 된다.
- Report 자체의 Format이 깨지면 Workflow 처리에 문제가 생긴다.

---

### [Best Practice]

Evaluation Report Checklist Best Practice:

- Summary를 먼저 작성한다.
- Requirement Compliance를 독립적으로 검증한다.
- Findings Table을 사용한다.
- Severity 기준을 일관되게 적용한다.
- Evidence를 Claim 단위로 연결한다.
- Fix Recommendation을 실행 가능한 형태로 작성한다.
- Final Decision을 명확히 끝에 둔다.
- 필요 시 Quality Score는 보조 지표로만 사용한다.

---

### [FAQ]

Q. Evaluation Report Checklist는 뭐야?
A. Evaluation Report가 요구사항, 근거, 형식, 안전 기준을 충족하는지 확인하는 최소 검증 목록이다.

Q. Evaluation Report 자체도 검수해야 해?
A. 해야 한다. Report에 Evidence나 Final Decision이 없으면 후속 Workflow가 실패할 수 있다.

Q. Evaluation Report에서 가장 중요한 항목은 뭐야?
A. Evaluation Target, Requirement Compliance, Findings, Evidence, Fix Recommendation, Final Decision이다.

Q. Quality Score만 있으면 충분해?
A. 아니다. Findings와 Evidence, Fix Recommendation이 함께 있어야 한다.

Q. Final Decision이 없으면 어떤 문제가 생겨?
A. 후속 Agent가 Pass, Fix, Stop 중 무엇을 해야 하는지 판단하기 어렵다.

---

# Retrieval Queries

### [FAQ]

Q. Evaluation Report가 뭐야?
A. Agent Output, Tool Calling, Workflow, Review, Fix 결과를 구조화해서 평가하는 리포트다.

Q. Evaluation Report에는 뭐가 들어가?
A. Evaluation Target, Evaluation Scope, User Requirement, Evaluation Criteria, Result, Findings, Severity, Evidence, Fix Recommendation, Final Decision이 들어간다.

Q. Evaluation Report는 왜 필요해?
A. Agent 결과의 문제와 수정 방향을 추적 가능하게 만들고 후속 Fix Agent가 처리하기 쉽게 하기 위해 필요하다.

Q. Evaluation Report 기본 Flow는 어떻게 돼?
A. Agent Output → Extract Requirements → Apply Evaluation Criteria → Identify Findings → Assign Severity → Add Evidence → Recommend Fix → Decide Pass / Fix / Stop 순서다.

Q. Finding이 뭐야?
A. Evaluation 과정에서 발견된 문제, 누락, 위험, 개선 필요 사항이다.

Q. Finding Type에는 뭐가 있어?
A. Requirement, Grounding, Faithfulness, Format, Code, Tool, Safety, Workflow, Memory Finding이 있다.

Q. Severity는 왜 필요해?
A. 문제의 우선순위와 Fix 필요성을 판단하기 위해 필요하다.

Q. Critical Finding은 뭐야?
A. 안전 문제, 데이터 손실, 핵심 요구 위반, 치명적 Hallucination처럼 즉시 중단 또는 수정해야 하는 문제다.

Q. Major Finding은 뭐야?
A. 주요 요구사항 누락, 근거 부족, 코드 오류, Workflow 결함처럼 Fix가 필요한 문제다.

Q. Minor Finding은 뭐야?
A. 작은 형식 오류나 표현 문제처럼 가능하면 수정하는 문제다.

Q. Info Finding도 Fix해야 해?
A. 필수는 아니다. 참고 또는 선택적 개선 사항으로 볼 수 있다.

Q. Evidence는 왜 필요해?
A. Review Finding이 실제 근거에 기반하는지 확인하기 위해 필요하다.

Q. 좋은 Evidence 조건은 뭐야?
A. 구체적이고, Finding과 직접 연결되며, 출처가 명확하고 검증 가능해야 한다.

Q. Evidence Type에는 뭐가 있어?
A. User Requirement, Agent Output, Retrieved Context, Tool Result, Code Evidence, Config Evidence, Log Evidence, Progress Evidence, Rule Evidence가 있다.

Q. Fix Recommendation은 어떻게 써야 해?
A. 수정 대상과 방법을 구체적으로 쓰고 실제 적용 가능해야 한다.

Q. Evidence가 약하면 어떻게 해?
A. 확정적으로 판단하지 말고 Assumption, Unknown, Missing Information으로 처리해야 한다.

Q. Quality Score가 뭐야?
A. Agent Output 품질을 여러 평가 항목별 점수로 표현하는 보조 기준이다.

Q. Quality Score 항목에는 뭐가 있어?
A. Requirement Compliance, Correctness, Completeness, Groundedness, Faithfulness, Format Compliance, Safety, Actionability가 있다.

Q. Quality Score만 보면 돼?
A. 아니다. 점수보다 Findings, Evidence, Fix Recommendation이 더 중요하다.

Q. 단일 총점으로 판단해도 돼?
A. 안 된다. 항목별 점수를 분리해야 개선 방향이 명확하다.

Q. Safety 점수가 낮으면 어떻게 해?
A. Stop 또는 즉시 Fix 대상이다.

Q. Groundedness 점수가 낮으면 어떻게 해?
A. Unsupported Claim을 제거하고 Evidence 기반으로 다시 작성해야 한다.

Q. Pass / Fix / Stop Decision은 뭐야?
A. Evaluation 결과를 바탕으로 Agent Output을 통과, 수정, 중단 중 하나로 판단하는 기준이다.

Q. 언제 Pass야?
A. 요구사항을 충족하고 Critical / Major Finding이 없으며 안전 문제가 없을 때 Pass다.

Q. 언제 Fix야?
A. 수정 가능한 Major / Minor Finding이 있을 때 Fix다.

Q. 언제 Stop이야?
A. Critical Finding, 정보 부족, 위험 작업 승인 필요, Tool 실패 후 Fallback 없음 상태일 때 Stop이다.

Q. Block은 Stop과 달라?
A. Block은 안전상 허용하면 안 되는 작업을 차단하는 것이고, Stop은 진행 조건이 충족되지 않아 중단하는 것이다.

Q. Evaluation Report Template은 왜 필요해?
A. Agent Evaluation 결과를 일관된 형식으로 작성하고 후속 Fix Agent가 처리하기 쉽게 만들기 위해 필요하다.

Q. 모든 작업에 Full Template을 써야 해?
A. 아니다. 작업 유형에 맞는 축소 Template을 사용할 수 있다.

Q. RAG 문서 검수 Template에는 뭐가 필요해?
A. Required Section Check, Retrieval Optimization Check, FAQ, Retrieval Queries 검증이 필요하다.

Q. Code Review Template에는 뭐가 필요해?
A. Code Check, Project Symbol Check, Findings, Evidence, Fix Recommendation이 필요하다.

Q. Tool Calling Template에는 뭐가 필요해?
A. Risk Level, Pre-Execution Check, Post-Execution Check, Human Confirmation 여부가 필요하다.

Q. Evaluation Report Checklist는 뭐야?
A. Evaluation Report가 요구사항, 근거, 형식, 안전 기준을 충족하는지 확인하는 최소 검증 목록이다.

Q. Evaluation Report 자체도 검수해야 해?
A. 해야 한다. Report에 Evidence나 Final Decision이 없으면 후속 Workflow가 실패할 수 있다.

Q. Evaluation Report의 최종 목표는 뭐야?
A. Agent Output의 품질 문제를 근거 기반으로 식별하고, Fix 또는 Stop 여부를 일관되게 판단하도록 만드는 것이다.
