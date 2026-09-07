# Agent Evaluation & Guardrails Part11 - Review Agent Evaluation

---

# 1. Review Agent Evaluation

## 1.1 Review Agent Evaluation Core

### [개념]

Review Agent Evaluation은 Review Agent가 다른 Agent의 Output을 정확하게 검토하고, 실제 결함을 찾아내며, 적절한 Severity와 Fix Recommendation을 제시했는지 평가하는 기준이다.

Review Agent도 평가 대상이다.

Review Agent가 부정확하면 Multi-Agent Workflow 전체 품질이 낮아진다.

Review Agent Evaluation의 목적:

- Review Finding 품질 평가
- False Positive 탐지
- False Negative 탐지
- Severity 정확도 평가
- Evidence 품질 평가
- Fix Recommendation 품질 평가
- Requirement Awareness 평가
- Domain Rule Awareness 평가
- Review-Fix Loop 안정성 확보

---

### [핵심]

Review Agent Evaluation 핵심 기준:

| 기준                  | 의미                                    |
| --------------------- | --------------------------------------- |
| Finding Quality       | 실제 문제를 정확히 찾았는가             |
| False Positive        | 문제가 아닌 것을 문제로 지적했는가      |
| False Negative        | 중요한 문제를 놓쳤는가                  |
| Severity Accuracy     | 심각도 판단이 적절한가                  |
| Evidence Quality      | 지적 근거가 충분한가                    |
| Fix Direction Quality | 수정 방향이 구체적인가                  |
| Requirement Awareness | 사용자 요구사항을 기준으로 검토했는가   |
| Domain Rule Awareness | Domain Rules를 반영했는가               |
| Safety Awareness      | 위험 작업과 승인 필요 여부를 확인했는가 |
| Grounding Awareness   | Unsupported Claim을 탐지했는가          |

Review Agent Evaluation Flow:

```text
Agent Output
→ Review Agent Findings
→ Check Findings against Requirements
→ Check Evidence
→ Check Severity
→ Check False Positive / False Negative
→ Check Fix Recommendation
→ Review Pass / Review Fix
```

Review Agent 결과 판단:

```text
Pass:
- 실제 결함 탐지
- Evidence 충분
- Severity 적절
- Fix 구체적
- 사용자 요구사항 반영

Fix:
- 일부 Finding 근거 부족
- Severity 일부 부정확
- Fix Recommendation 추상적
- Minor False Positive 존재

Fail:
- 핵심 결함 누락
- False Positive 다수
- Evidence 없음
- 사용자 요구사항 무시
- Safety / Grounding 문제 미탐지
```

---

### [실무]

2026 실무 기준 Review Agent는 단순 “좋다 / 나쁘다” 평가가 아니라 Evaluation Report를 작성해야 한다.

개인 AI 개발팀 구조에서는 Review Agent가 Backend Agent, Frontend Agent, DevOps Agent, AI/ML Agent, Tool Agent의 산출물을 검증한다.

실무 Review Agent 평가 순서:

```text
1. 원래 User Requirement 확인
2. Agent Output 확인
3. Review Agent Finding 확인
4. 실제 결함과 Finding 매핑
5. 놓친 결함 확인
6. 잘못된 지적 확인
7. Severity 적절성 확인
8. Evidence와 Fix Recommendation 확인
9. Review Agent Pass / Fix 판단
```

좋은 Review Agent Output 예시:

```md
| Severity | Category  | Issue                     | Evidence                     | Fix Recommendation              |
| -------- | --------- | ------------------------- | ---------------------------- | ------------------------------- |
| Major    | Format    | Retrieval Queries 누락    | 문서 마지막에 해당 섹션 없음 | # Retrieval Queries 추가        |
| Major    | Grounding | 문서에 없는 API 경로 생성 | Retrieved Context에 API 없음 | Claim 제거 또는 Assumption 표시 |
| Critical | Safety    | DB DELETE 승인 없음       | High Risk Tool Action        | Human Confirmation 전 Stop      |
```

나쁜 Review Agent Output 예시:

```text
- 전체적으로 괜찮습니다.
- 조금 더 정리하면 좋겠습니다.
- 코드가 약간 별로입니다.
```

문제:

- Finding 불명확
- Severity 없음
- Evidence 없음
- Fix Recommendation 없음
- 사용자 요구사항 기준 없음

Review Agent Evaluation Report 예시:

```md
| Review Criteria       | Result | Evidence                         | Fix           |
| --------------------- | ------ | -------------------------------- | ------------- |
| Finding Quality       | Pass   | 실제 Retrieval Queries 누락 탐지 | 없음          |
| Evidence Quality      | Fix    | 일부 Finding에 근거 없음         | Evidence 추가 |
| Severity Accuracy     | Fix    | Minor를 Major로 과장             | Severity 조정 |
| Fix Direction         | Pass   | 수정 방향 구체적                 | 없음          |
| Requirement Awareness | Pass   | 사용자 출력 형식 기준 반영       | 없음          |
```

---

### [주의]

Review Agent Evaluation 주의사항:

- Review Agent도 Hallucination을 만들 수 있다.
- Review Agent가 취향을 결함처럼 지적할 수 있다.
- Review Agent가 사용자 요구사항보다 일반 관례를 우선할 수 있다.
- Evidence 없는 Finding은 신뢰도가 낮다.
- Severity가 과도하면 Workflow가 불필요하게 느려진다.
- Severity가 낮으면 중요한 결함이 남을 수 있다.
- Review Agent가 너무 엄격해도 문제고 너무 느슨해도 문제다.
- Review Finding은 Fix Agent가 실제로 처리 가능해야 한다.

---

### [Best Practice]

Review Agent Evaluation Best Practice:

- Review Criteria를 고정한다.
- 사용자 요구사항을 Review 기준의 최상위에 둔다.
- Finding마다 Evidence를 요구한다.
- Finding마다 Severity를 요구한다.
- Finding마다 Fix Recommendation을 요구한다.
- False Positive와 False Negative를 추적한다.
- 취향 / 개선 / 결함을 구분한다.
- Safety와 Grounding 문제는 높은 우선순위로 평가한다.
- Review Agent Output도 Format Compliance 대상이다.
- 반복되는 Review Failure는 Review Prompt와 Checklist를 개선한다.

---

### [FAQ]

Q. Review Agent Evaluation이 뭐야?
A. Review Agent가 실제 결함을 정확히 찾고 적절한 Severity, Evidence, Fix Recommendation을 제시했는지 평가하는 기준이다.

Q. Review Agent도 평가해야 해?
A. 해야 한다. Review Agent도 중요한 결함을 놓치거나 근거 없는 지적을 할 수 있다.

Q. Review Agent Evaluation에서 가장 중요한 기준은 뭐야?
A. Finding Quality, Evidence Quality, Severity Accuracy, Fix Direction Quality다.

Q. Review Agent가 “괜찮다”고만 하면 충분해?
A. 아니다. 구체적인 Finding, Evidence, Severity, Fix가 있어야 한다.

Q. Review Agent가 너무 엄격하면 문제야?
A. 문제다. False Positive가 많아져 Workflow가 불필요하게 느려질 수 있다.

---

# 2. Finding Quality Evaluation

## 2.1 Finding Quality

### [개념]

Finding Quality는 Review Agent가 실제 문제를 정확하고 구체적으로 식별했는지 평가하는 기준이다.

좋은 Finding은 문제 위치, 문제 유형, 근거, 영향, 수정 방향이 명확하다.

나쁜 Finding은 추상적이고 근거가 없으며 Fix Agent가 사용할 수 없다.

---

### [핵심]

좋은 Finding 조건:

| 조건               | 의미                         |
| ------------------ | ---------------------------- |
| Specific           | 문제가 구체적인가            |
| Evidence-based     | 근거가 있는가                |
| Requirement-linked | 사용자 요구사항과 연결되는가 |
| Severity-assigned  | 심각도가 지정되었는가        |
| Actionable         | 수정 방향이 실행 가능한가    |
| Scoped             | 요청 범위 안의 문제인가      |
| Non-duplicated     | 중복 지적이 아닌가           |
| Testable           | 수정 후 검증 가능한가        |

Finding Quality Evaluation Flow:

```text
Review Finding
→ Check Specificity
→ Check Evidence
→ Check Requirement Link
→ Check Severity
→ Check Fix Actionability
→ Good / Weak / Invalid
```

Finding 품질 판단:

```text
Good Finding:
- 문제 명확
- 근거 있음
- Severity 적절
- Fix 가능

Weak Finding:
- 문제는 맞지만 근거 부족
- Fix 추상적
- 영향 범위 불명확

Invalid Finding:
- 실제 문제가 아님
- 사용자 요구사항과 충돌
- 근거 없음
- 취향을 결함으로 지적
```

---

### [실무]

실무에서는 Finding을 표준 구조로 작성한다.

Finding Template:

```md
| Severity | Category | Issue | Evidence | Impact | Fix Recommendation |
| -------- | -------- | ----- | -------- | ------ | ------------------ |
```

좋은 Finding 예시:

```md
| Severity | Category | Issue                  | Evidence                               | Impact                  | Fix Recommendation                       |
| -------- | -------- | ---------------------- | -------------------------------------- | ----------------------- | ---------------------------------------- |
| Major    | Format   | Retrieval Queries 누락 | 문서 마지막에 # Retrieval Queries 없음 | RAG 검색 질문 매칭 약화 | 문서 마지막에 Retrieval Queries Q/A 추가 |
```

약한 Finding 예시:

```text
문서가 조금 약합니다.
```

문제:

- 무엇이 약한지 불명확
- Evidence 없음
- Fix 불가능
- Severity 없음

Invalid Finding 예시:

```text
FAQ가 너무 많으니 줄여야 한다.
```

Context:

```text
User Requirement:
FAQ 강화

Domain Rules:
FAQ와 Retrieval Queries에 실제 사용자 질문 표현 포함
```

Evaluation:

```text
- 사용자 요구사항과 Domain Rules에 충돌
- False Positive 가능성 높음
```

---

### [주의]

Finding Quality 주의사항:

- “좋아 보임”, “부족함” 같은 추상 표현은 Finding으로 부족하다.
- Finding은 Evidence 없이 작성하지 않는다.
- 같은 문제를 여러 번 중복 지적하지 않는다.
- 요청 범위 밖 개선사항을 필수 결함처럼 다루지 않는다.
- 취향과 결함을 구분한다.
- Minor Issue를 Critical처럼 과장하지 않는다.
- Finding이 Fix Agent에게 전달 가능한 형태인지 확인한다.

---

### [Best Practice]

Finding Quality Best Practice:

- Finding은 Issue + Evidence + Fix 구조로 작성한다.
- Category를 지정한다.
- Severity를 지정한다.
- 사용자 요구사항과 연결한다.
- Fix Recommendation은 구체적으로 작성한다.
- Impact를 짧게 표시한다.
- 중복 Finding은 통합한다.
- Invalid Finding은 제거하거나 Info로 낮춘다.
- Finding이 실제 결함인지 다시 검증한다.

---

### [FAQ]

Q. Finding Quality가 뭐야?
A. Review Agent가 실제 문제를 정확하고 구체적으로 식별했는지 평가하는 기준이다.

Q. 좋은 Finding 조건은 뭐야?
A. 구체적이고, 근거가 있으며, Severity와 Fix Recommendation이 명확해야 한다.

Q. “문서가 약하다”는 좋은 Finding이야?
A. 아니다. 무엇이 약한지, 근거가 무엇인지, 어떻게 고칠지 구체적으로 써야 한다.

Q. Finding에는 Evidence가 꼭 필요해?
A. 필요하다. Evidence가 없으면 근거 없는 지적이 될 수 있다.

Q. 취향도 Finding으로 적어도 돼?
A. 가능하지만 결함으로 과장하면 안 된다. Info 또는 optional improvement로 분리해야 한다.

---

# 3. False Positive Evaluation

## 3.1 False Positive

### [개념]

False Positive는 Review Agent가 실제 문제가 아닌 것을 문제로 지적하는 오류다.

False Positive가 많으면 Agent Workflow가 느려지고 Fix Agent가 불필요한 수정을 수행하게 된다.

False Positive는 Review Agent 신뢰도를 낮춘다.

---

### [핵심]

False Positive 발생 유형:

| 유형                   | 설명                                   |
| ---------------------- | -------------------------------------- |
| Preference as Defect   | 취향을 결함처럼 지적                   |
| Requirement Conflict   | 사용자 요구사항과 반대되는 지적        |
| Domain Rule Ignored    | Domain Rules를 무시한 지적             |
| Over-severity          | Minor 문제를 Major / Critical로 과장   |
| Out-of-scope Finding   | 요청 범위 밖 문제를 필수 수정으로 지적 |
| Evidence Missing       | 근거 없이 문제라고 주장                |
| Correct Output Misread | 올바른 내용을 잘못 읽고 지적           |

False Positive Evaluation Flow:

```text
Review Finding
→ Check Against User Requirement
→ Check Domain Rules
→ Check Evidence
→ Check Scope
→ Valid Finding / False Positive
```

False Positive 판단:

```text
False Positive:
- 사용자 요구사항과 충돌
- 근거 없음
- 실제 문제 아님
- 요청 범위 밖
- 취향을 결함으로 처리

Valid Finding:
- 요구사항 위반
- 근거 있음
- 수정 필요
```

---

### [실무]

False Positive 예시 1:

```text
Review Finding:
FAQ가 너무 많으므로 줄여야 한다.

User Requirement:
FAQ 강화

Evaluation:
- False Positive
- 사용자 요구사항과 반대
```

False Positive 예시 2:

```text
Review Finding:
ResponseEntity를 반드시 사용해야 한다.

Project Rule:
Controller는 ApiResponse<T> 직접 반환 가능
예외는 GlobalExceptionHandler 처리

Evaluation:
- False Positive
- 프로젝트 규칙과 충돌
```

False Positive 예시 3:

```text
Review Finding:
모든 문서에 긴 서론이 필요하다.

Master Rules:
불필요한 서론 금지
Retrieval 최적화 우선

Evaluation:
- False Positive
- Master Rules 위반
```

False Positive Report 예시:

```md
| Finding             | False Positive Reason     | Decision    |
| ------------------- | ------------------------- | ----------- |
| FAQ 줄이기          | FAQ 강화 요구와 충돌      | 제거        |
| ResponseEntity 필수 | 프로젝트 응답 규칙과 충돌 | 제거        |
| 긴 서론 추가        | Master Rules와 충돌       | 제거        |
| 문장 다듬기         | 선택적 개선               | Info로 낮춤 |
```

---

### [주의]

False Positive 주의사항:

- Review Agent가 일반 관례를 프로젝트 규칙보다 우선하면 False Positive가 발생한다.
- 엄격한 Review가 항상 좋은 것은 아니다.
- False Positive가 많으면 Review-Fix Loop가 불필요하게 반복된다.
- False Positive를 Fix하면 오히려 요구사항 위반이 될 수 있다.
- 취향성 지적은 Info로 분류해야 한다.
- Evidence 없는 지적은 False Positive 후보로 본다.

---

### [Best Practice]

False Positive 방지 Best Practice:

- 사용자 요구사항을 Review 기준의 최상위에 둔다.
- Master Rules와 Domain Rules를 우선한다.
- 프로젝트 규칙과 일반 관례를 구분한다.
- Evidence 없는 Finding은 보류한다.
- 취향성 지적은 Info로 낮춘다.
- Scope 밖 지적은 Optional로 분리한다.
- Severity를 과장하지 않는다.
- Review Agent도 재검토한다.

---

### [FAQ]

Q. False Positive가 뭐야?
A. 실제 문제가 아닌 것을 Review Agent가 문제로 지적하는 오류다.

Q. False Positive가 많으면 왜 문제야?
A. Workflow가 느려지고 Fix Agent가 불필요한 수정을 하게 된다.

Q. 취향성 지적도 False Positive야?
A. 결함처럼 지적하면 False Positive가 될 수 있다. 선택적 개선은 Info로 분리해야 한다.

Q. 사용자 요구사항과 반대되는 Review Finding은 어떻게 처리해?
A. False Positive로 보고 제거하거나 수정해야 한다.

Q. False Positive를 줄이려면 어떻게 해?
A. 사용자 요구사항, Domain Rules, Evidence를 기준으로 Review Finding을 검증해야 한다.

---

# 4. False Negative Evaluation

## 4.1 False Negative

### [개념]

False Negative는 Review Agent가 실제 중요한 문제를 놓치는 오류다.

False Negative는 False Positive보다 더 위험할 수 있다.

특히 Safety Failure, Grounding Failure, Requirement Failure, Code Hallucination을 놓치면 최종 Output에 치명적 문제가 남는다.

---

### [핵심]

False Negative 발생 유형:

| 유형                        | 설명                                  |
| --------------------------- | ------------------------------------- |
| Missing Requirement Failure | 요구사항 누락을 놓침                  |
| Missing Grounding Failure   | Unsupported Claim을 놓침              |
| Missing Safety Failure      | 위험 작업 승인 누락을 놓침            |
| Missing Format Failure      | Required Section / Schema 오류를 놓침 |
| Missing Code Hallucination  | 존재하지 않는 클래스 / 메서드를 놓침  |
| Missing Tool Failure        | Tool 실패를 성공처럼 처리한 것을 놓침 |
| Missing State Conflict      | 상태 충돌을 놓침                      |
| Missing Regression          | Fix 과정에서 새 문제 발생을 놓침      |

False Negative Evaluation Flow:

```text
Agent Output
→ Independent Checklist Review
→ Compare with Review Agent Findings
→ Identify Missed Issues
→ Classify False Negative
→ Improve Review Criteria
```

False Negative 판단:

```text
False Negative:
- 실제 결함이 존재
- Review Agent가 Finding으로 기록하지 않음
- 결함이 최종 Output에 남음

Critical False Negative:
- Safety Failure
- Secret 노출
- 승인 없는 High Risk Tool
- 핵심 Hallucination
- 핵심 요구사항 누락
```

---

### [실무]

False Negative 예시 1:

```text
Agent Output:
Retrieval Queries 없음

Review Agent:
문제 없음

Evaluation:
- Required Section 누락을 놓침
- False Negative
```

False Negative 예시 2:

```text
Agent Output:
findUnreadByUserId() 사용

Context:
해당 Repository 메서드 없음

Review Agent:
코드 구조 괜찮음

Evaluation:
- Code Hallucination을 놓침
- False Negative
```

False Negative 예시 3:

```text
Agent Action:
DB DELETE 실행 제안

Review Agent:
SQL 문법만 검토

Evaluation:
- Human Confirmation 필요성을 놓침
- Safety False Negative
- Critical
```

False Negative Report 예시:

```md
| Missed Issue           | Category           | Severity | Impact             | Review Fix                      |
| ---------------------- | ------------------ | -------- | ------------------ | ------------------------------- |
| Retrieval Queries 누락 | Format             | Major    | RAG 검색 품질 저하 | Required Section Checklist 추가 |
| 존재하지 않는 메서드   | Code Hallucination | Major    | 컴파일 실패        | Symbol Check 추가               |
| DB DELETE 승인 누락    | Safety             | Critical | 데이터 손실 위험   | Human Confirmation Check 추가   |
```

---

### [주의]

False Negative 주의사항:

- Review Agent가 “문제 없음”이라고 해도 실제 문제가 있을 수 있다.
- Safety False Negative는 특히 위험하다.
- Grounding False Negative는 Hallucination을 남긴다.
- Format False Negative는 후속 Tool / Parser 실패로 이어질 수 있다.
- Code False Negative는 컴파일 오류로 이어질 수 있다.
- Fix 후 Regression을 놓치는 것도 False Negative다.
- Checklist 없이 Review하면 False Negative가 증가한다.

---

### [Best Practice]

False Negative 방지 Best Practice:

- Review Checklist를 고정한다.
- Required Section과 Must Requirement를 먼저 확인한다.
- Grounding Checklist를 적용한다.
- Code Symbol Check를 적용한다.
- Safety Checklist를 적용한다.
- Tool Result Validation을 적용한다.
- Fix 후 Regression Check를 수행한다.
- Review Agent가 놓친 문제를 기록해 Prompt를 개선한다.
- Critical False Negative는 Review Agent 규칙을 즉시 보강한다.

---

### [FAQ]

Q. False Negative가 뭐야?
A. 실제 중요한 문제를 Review Agent가 놓치는 오류다.

Q. False Negative가 왜 위험해?
A. 최종 Output에 요구사항 누락, Hallucination, Safety Failure 같은 문제가 그대로 남기 때문이다.

Q. Critical False Negative는 뭐야?
A. Safety Failure, Secret 노출, 승인 없는 High Risk Tool, 핵심 Hallucination을 놓치는 것이다.

Q. False Negative를 줄이려면 어떻게 해?
A. Requirement, Grounding, Format, Code, Tool, Safety Checklist를 고정 적용해야 한다.

Q. Fix 후에도 False Negative가 생길 수 있어?
A. 생길 수 있다. Fix 과정에서 생긴 Regression을 놓치면 False Negative다.

---

# 5. Severity Accuracy Evaluation

## 5.1 Severity Accuracy

### [개념]

Severity Accuracy는 Review Agent가 Finding의 심각도를 적절하게 분류했는지 평가하는 기준이다.

Severity가 정확해야 Fix 우선순위가 맞고 Workflow가 안정적으로 진행된다.

Severity가 과장되면 Workflow가 느려지고, Severity가 낮게 평가되면 치명적 문제가 남는다.

---

### [핵심]

Severity 기준:

| Severity | 의미                                                    | 처리               |
| -------- | ------------------------------------------------------- | ------------------ |
| Critical | 안전 문제, 데이터 손실, Secret 노출, 핵심 요구 위반     | Stop 또는 즉시 Fix |
| Major    | 주요 요구사항 누락, 근거 부족, 코드 오류, Workflow 결함 | Fix                |
| Minor    | 작은 형식 오류, 표현 문제, 일부 개선 필요               | 가능하면 Fix       |
| Info     | 참고 사항, 선택적 개선                                  | 보고만 가능        |

Severity Accuracy 검증 항목:

| 검증 항목            | 의미                                         |
| -------------------- | -------------------------------------------- |
| Impact Match         | 실제 영향도와 Severity가 맞는가              |
| Safety Priority      | 안전 문제를 높게 평가했는가                  |
| Requirement Priority | 필수 요구사항 위반을 높게 평가했는가         |
| Grounding Priority   | 핵심 Unsupported Claim을 높게 평가했는가     |
| Format Impact        | Parser / RAG Indexing 영향 여부를 반영했는가 |
| Overstatement        | Severity를 과장하지 않았는가                 |
| Understatement       | Severity를 낮게 평가하지 않았는가            |

Severity Evaluation Flow:

```text
Finding
→ Check Impact
→ Check Safety / Requirement / Grounding
→ Assign Severity
→ Compare with Review Severity
→ Accurate / Overstated / Understated
```

---

### [실무]

Severity Accuracy 예시:

```md
| Finding                | Review Severity | Correct Severity | Evaluation  |
| ---------------------- | --------------: | ---------------: | ----------- |
| Secret 전체 노출       |           Minor |         Critical | Understated |
| Retrieval Queries 누락 |           Minor |            Major | Understated |
| 문장 표현 어색함       |           Major |            Minor | Overstated  |
| DB DELETE 승인 없음    |           Major |         Critical | Understated |
| Table 정렬 약간 불일치 |        Critical |            Minor | Overstated  |
```

Severity 판단 기준 예시:

```text
Critical:
- Secret 전체 노출
- 승인 없는 DB DELETE
- 운영 배포 자동 실행
- 사용자 핵심 금지 조건 위반

Major:
- Required Section 누락
- 핵심 Unsupported Claim
- 존재하지 않는 클래스 / 메서드
- Tool 실패 은폐

Minor:
- 작은 오타
- Header 계층 일부 개선
- FAQ 답변 일부 장문

Info:
- 예시 추가 가능
- 표 설명 보강 가능
```

Severity Correction Report:

```md
| Issue            | Original Severity | Corrected Severity | Reason                      |
| ---------------- | ----------------- | ------------------ | --------------------------- |
| API Key 노출     | Minor             | Critical           | Secret Exposure             |
| FAQ 문장 약간 김 | Major             | Minor              | 핵심 요구 위반 아님         |
| Fabricated API   | Minor             | Major              | 프로젝트 고유 Hallucination |
```

---

### [주의]

Severity Accuracy 주의사항:

- Safety Finding은 낮게 평가하지 않는다.
- Secret 노출은 Critical 또는 Block이다.
- 핵심 요구사항 누락은 Major 이상이다.
- 작은 표현 문제를 Major로 과장하지 않는다.
- Info를 Fix Blocker로 만들지 않는다.
- Severity는 취향이 아니라 영향 기준으로 정한다.
- Domain Rules의 필수 조건 위반은 높게 평가한다.

---

### [Best Practice]

Severity Accuracy Best Practice:

- Severity 기준표를 고정한다.
- Impact와 Risk를 기준으로 판단한다.
- Safety, Requirement, Grounding 문제는 우선순위를 높게 둔다.
- Cosmetic Issue는 Minor 또는 Info로 분류한다.
- Overstated / Understated Finding을 기록한다.
- Review Agent Prompt에 Severity 기준을 포함한다.
- 반복되는 Severity 오류는 Review Criteria를 보강한다.

---

### [FAQ]

Q. Severity Accuracy가 뭐야?
A. Review Agent가 Finding의 심각도를 실제 영향도에 맞게 분류했는지 평가하는 기준이다.

Q. Severity가 부정확하면 왜 문제야?
A. Fix 우선순위가 틀어지고 치명적 문제가 남거나 불필요한 수정이 반복될 수 있다.

Q. Critical로 봐야 하는 문제는 뭐야?
A. Secret 노출, 데이터 손실, 승인 없는 High Risk Tool, 핵심 금지 조건 위반이다.

Q. Major로 봐야 하는 문제는 뭐야?
A. 주요 요구사항 누락, 핵심 Grounding Failure, 존재하지 않는 코드 Symbol 사용이다.

Q. 표현 문제는 보통 어떤 Severity야?
A. 보통 Minor 또는 Info다.

---

# 6. Review Fix Direction Evaluation

## 6.1 Fix Direction Quality

### [개념]

Fix Direction Quality는 Review Agent가 제시한 수정 방향이 구체적이고 실행 가능하며, 문제를 실제로 해결하는지 평가하는 기준이다.

Review Finding이 맞아도 Fix Recommendation이 추상적이면 Fix Agent가 제대로 수정하기 어렵다.

---

### [핵심]

좋은 Fix Direction 조건:

| 조건                | 의미                            |
| ------------------- | ------------------------------- |
| Specific            | 무엇을 고칠지 명확한가          |
| Actionable          | 실제 적용 가능한가              |
| Grounded            | Evidence 기반인가               |
| Scoped              | 요청 범위 안인가                |
| Safe                | 위험 작업을 유발하지 않는가     |
| Testable            | 수정 후 검증 가능한가           |
| Minimal             | 불필요한 변경을 요구하지 않는가 |
| Requirement-aligned | 사용자 요구사항과 일치하는가    |

Fix Direction Evaluation Flow:

```text
Review Finding
→ Fix Recommendation
→ Check Specificity
→ Check Requirement Alignment
→ Check Safety
→ Check Testability
→ Good / Weak / Unsafe
```

Fix Direction 판단:

```text
Good:
- 수정 대상 명확
- 방법 구체적
- 요구사항과 일치
- 안전함
- 검증 가능

Weak:
- 방향은 맞지만 추상적
- 대상 불명확
- 검증 기준 부족

Unsafe:
- 요청 범위 밖 수정
- 위험 Tool 실행 요구
- 사용자 승인 없는 High Risk Fix
```

---

### [실무]

좋은 Fix Direction 예시:

```text
Issue:
Retrieval Queries 누락

Fix:
문서 마지막에 `# Retrieval Queries` 섹션을 추가하고, 실제 사용자 질문 표현을 Q/A 형식으로 20개 이상 작성한다.
```

나쁜 Fix Direction 예시:

```text
문서를 더 좋게 고치세요.
```

문제:

- 수정 대상 불명확
- 기준 없음
- 검증 불가

Code Fix Direction 예시:

```text
Issue:
NotificationRepository에 없는 findUnreadByUserId() 사용

Fix:
제공된 Repository에 존재하는 countByUsers_UserIdAndReadStatusFalse(Long userId)를 사용하도록 수정한다.
```

Safety Fix Direction 예시:

```text
Issue:
DB DELETE 작업에 Human Confirmation 없음

Fix:
DELETE 실행 전 대상 DB, 테이블, 조건절, 영향 범위, 복구 가능성, 백업 여부를 Preview하고 사용자 명시 승인을 요구한다.
```

Fix Direction Report:

```md
| Finding           | Fix Direction  | Quality | Issue       |
| ----------------- | -------------- | ------- | ----------- |
| FAQ 누락          | FAQ Q/A 추가   | Good    | 없음        |
| 문서 약함         | 더 좋게 수정   | Weak    | 기준 불명확 |
| DB 삭제 승인 없음 | 바로 삭제 실행 | Unsafe  | Safety 위반 |
```

---

### [주의]

Fix Direction 주의사항:

- Fix가 문제를 직접 해결해야 한다.
- Fix가 사용자 요구사항과 충돌하면 안 된다.
- Fix가 요청 범위를 벗어나면 Scope Violation이다.
- Fix가 위험 작업이면 Human Confirmation이 필요하다.
- Fix가 너무 넓으면 새로운 Regression이 생길 수 있다.
- Fix Recommendation에도 Hallucination이 생길 수 있다.
- 검증 불가한 Fix는 Assumption으로 표시해야 한다.

---

### [Best Practice]

Fix Direction Best Practice:

- 문제 위치와 수정 방법을 함께 쓴다.
- Fix 후 검증 기준을 포함한다.
- 최소 변경으로 문제를 해결한다.
- 사용자 요구사항과 Domain Rules에 맞춘다.
- 위험 작업은 Preview와 Human Confirmation을 포함한다.
- 코드 Fix는 실제 Symbol 기준으로 작성한다.
- Format Fix는 Required Section / Schema 기준으로 작성한다.
- Grounding Fix는 Evidence 기반으로 작성한다.

---

### [FAQ]

Q. Fix Direction Quality가 뭐야?
A. Review Agent가 제시한 수정 방향이 구체적이고 실행 가능하며 문제를 실제로 해결하는지 평가하는 기준이다.

Q. “더 좋게 고쳐라”는 좋은 Fix야?
A. 아니다. 수정 대상, 방법, 기준이 구체적이어야 한다.

Q. Fix Direction도 Safety Evaluation이 필요해?
A. 필요하다. Fix가 위험 Tool 실행이나 범위 밖 수정을 요구할 수 있기 때문이다.

Q. 좋은 Code Fix Direction은 뭐야?
A. 실제 존재하는 클래스, 메서드, 필드를 기준으로 구체적인 수정 방법을 제시하는 것이다.

Q. Fix 후 검증 기준도 필요해?
A. 필요하다. 수정이 실제로 문제를 해결했는지 확인해야 한다.

---

# 7. Review Agent Checklist

## 7.1 Checklist

### [개념]

Review Agent Checklist는 Review Agent가 Agent Output을 일관되게 검토하고, Review Agent 자체 품질을 평가하기 위한 최소 검증 목록이다.

이 Checklist는 Review Agent, PM Agent, Orchestrator가 공통으로 사용할 수 있다.

---

### [핵심]

Review Agent Output Checklist:

```md
### [Checklist]

- [ ] 원래 사용자 요구사항을 기준으로 검토했는가?
- [ ] Must Requirement 누락을 확인했는가?
- [ ] Must Not Requirement 위반을 확인했는가?
- [ ] Domain Rules를 반영했는가?
- [ ] MASTER_RAG_RULES를 반영했는가?
- [ ] Grounding / Unsupported Claim을 확인했는가?
- [ ] Format Compliance를 확인했는가?
- [ ] Safety Risk를 확인했는가?
- [ ] Tool Result 실패 여부를 확인했는가?
- [ ] Memory / State 충돌을 확인했는가?
- [ ] Finding마다 Evidence가 있는가?
- [ ] Finding마다 Severity가 있는가?
- [ ] Finding마다 Fix Recommendation이 있는가?
- [ ] 취향과 결함을 구분했는가?
- [ ] False Positive 가능성을 확인했는가?
- [ ] False Negative 가능성을 확인했는가?
```

Review Agent Self-Evaluation Checklist:

```md
### [Checklist]

- [ ] 실제 결함을 찾았는가?
- [ ] 중요한 결함을 놓치지 않았는가?
- [ ] 문제가 아닌 것을 문제로 지적하지 않았는가?
- [ ] Severity가 영향도와 맞는가?
- [ ] Evidence가 직접 근거인가?
- [ ] Fix Recommendation이 실행 가능한가?
- [ ] 사용자 요구사항과 충돌하는 지적이 없는가?
- [ ] Review 결과가 Fix Agent에게 전달 가능한가?
```

최소 Pass 기준:

```text
- Finding이 구체적
- Evidence 포함
- Severity 적절
- Fix Recommendation 실행 가능
- False Positive 낮음
- Critical False Negative 없음
```

---

### [실무]

Review Agent Checklist 적용 Flow:

```text
Agent Output
→ Review Agent Output
→ Review Agent Checklist
→ False Positive Check
→ False Negative Check
→ Severity Check
→ Review Pass / Review Fix
```

Checklist Result 예시:

```md
### Review Agent Evaluation Result

| Item                  | Result | Evidence                      | Fix                         |
| --------------------- | ------ | ----------------------------- | --------------------------- |
| Requirement Awareness | Pass   | 출력 형식 요구 반영           | 없음                        |
| Evidence Quality      | Fix    | 일부 Finding 근거 부족        | Evidence 추가               |
| Severity Accuracy     | Fix    | 표현 문제를 Major로 과장      | Minor로 조정                |
| False Negative        | Fail   | Retrieval Queries 누락 미탐지 | Required Section Check 추가 |
| Fix Direction         | Pass   | 구체적 수정안 포함            | 없음                        |
```

Review Agent 개선 예시:

```text
문제:
Review Agent가 FAQ 강화 요구를 무시하고 FAQ를 줄이라고 지적함.

개선:
- User Requirement Priority 규칙 추가
- Domain Rules 우선 규칙 추가
- False Positive Check 추가
```

---

### [주의]

Review Agent Checklist 주의사항:

- Checklist는 최소 기준이다.
- Review Agent가 Checklist만 기계적으로 채우면 피상적 Review가 될 수 있다.
- Evidence가 약한 Finding은 확정하지 않는다.
- False Positive가 많으면 Fix Loop가 느려진다.
- False Negative가 많으면 최종 Output 품질이 낮아진다.
- Safety / Grounding / Requirement 문제는 반드시 별도 확인한다.
- Review Agent 자체도 Format Compliance 대상이다.

---

### [Best Practice]

Review Agent Checklist Best Practice:

- Review 전 사용자 요구사항을 먼저 추출한다.
- Required / Must Not을 별도 확인한다.
- Domain Rules와 Master Rules를 기준으로 삼는다.
- Finding마다 Evidence를 연결한다.
- Severity 기준을 고정한다.
- Fix Recommendation은 실행 가능하게 작성한다.
- False Positive / False Negative를 별도 검토한다.
- Critical Issue는 즉시 Stop 또는 Fix로 판단한다.
- Review 결과는 Evaluation Report 형식으로 출력한다.

---

### [FAQ]

Q. Review Agent Checklist는 뭐야?
A. Review Agent가 Agent Output을 일관되게 검토하고 Review 자체 품질을 평가하기 위한 최소 검증 목록이다.

Q. Review Agent Checklist에서 가장 중요한 항목은 뭐야?
A. 사용자 요구사항, Domain Rules, Evidence, Severity, Fix Recommendation, Safety, Grounding 검증이다.

Q. Review Agent 자체도 Self-Evaluation 해야 해?
A. 해야 한다. Review Agent도 False Positive와 False Negative를 만들 수 있다.

Q. Review Agent Output 최소 Pass 기준은 뭐야?
A. Finding이 구체적이고 Evidence와 Severity가 있으며 Fix Recommendation이 실행 가능해야 한다.

Q. Critical False Negative가 있으면 어떻게 해?
A. Review Agent Output은 Fail이며 Review Criteria와 Prompt를 보강해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Review Agent Evaluation이 뭐야?
A. Review Agent가 실제 결함을 정확히 찾고 적절한 Severity, Evidence, Fix Recommendation을 제시했는지 평가하는 기준이다.

Q. Review Agent도 평가해야 해?
A. 해야 한다. Review Agent도 중요한 결함을 놓치거나 근거 없는 지적을 할 수 있다.

Q. Review Agent Evaluation 기준은 뭐야?
A. Finding Quality, False Positive, False Negative, Severity Accuracy, Evidence Quality, Fix Direction Quality, Requirement Awareness, Domain Rule Awareness다.

Q. Finding Quality가 뭐야?
A. Review Agent가 실제 문제를 정확하고 구체적으로 식별했는지 평가하는 기준이다.

Q. 좋은 Finding 조건은 뭐야?
A. 구체적이고, 근거가 있으며, Severity와 Fix Recommendation이 명확해야 한다.

Q. Finding에는 Evidence가 꼭 필요해?
A. 필요하다. Evidence가 없으면 근거 없는 지적이 될 수 있다.

Q. 취향도 Finding으로 적어도 돼?
A. 가능하지만 결함으로 과장하면 안 된다. Info 또는 optional improvement로 분리해야 한다.

Q. False Positive가 뭐야?
A. 실제 문제가 아닌 것을 Review Agent가 문제로 지적하는 오류다.

Q. False Positive가 많으면 왜 문제야?
A. Workflow가 느려지고 Fix Agent가 불필요한 수정을 하게 된다.

Q. 사용자 요구사항과 반대되는 Review Finding은 어떻게 처리해?
A. False Positive로 보고 제거하거나 수정해야 한다.

Q. False Positive를 줄이려면 어떻게 해?
A. 사용자 요구사항, Domain Rules, Evidence를 기준으로 Review Finding을 검증해야 한다.

Q. False Negative가 뭐야?
A. 실제 중요한 문제를 Review Agent가 놓치는 오류다.

Q. False Negative가 왜 위험해?
A. 최종 Output에 요구사항 누락, Hallucination, Safety Failure 같은 문제가 그대로 남기 때문이다.

Q. Critical False Negative는 뭐야?
A. Safety Failure, Secret 노출, 승인 없는 High Risk Tool, 핵심 Hallucination을 놓치는 것이다.

Q. False Negative를 줄이려면 어떻게 해?
A. Requirement, Grounding, Format, Code, Tool, Safety Checklist를 고정 적용해야 한다.

Q. Severity Accuracy가 뭐야?
A. Review Agent가 Finding의 심각도를 실제 영향도에 맞게 분류했는지 평가하는 기준이다.

Q. Severity가 부정확하면 왜 문제야?
A. Fix 우선순위가 틀어지고 치명적 문제가 남거나 불필요한 수정이 반복될 수 있다.

Q. Critical로 봐야 하는 문제는 뭐야?
A. Secret 노출, 데이터 손실, 승인 없는 High Risk Tool, 핵심 금지 조건 위반이다.

Q. Major로 봐야 하는 문제는 뭐야?
A. 주요 요구사항 누락, 핵심 Grounding Failure, 존재하지 않는 코드 Symbol 사용이다.

Q. 표현 문제는 보통 어떤 Severity야?
A. 보통 Minor 또는 Info다.

Q. Fix Direction Quality가 뭐야?
A. Review Agent가 제시한 수정 방향이 구체적이고 실행 가능하며 문제를 실제로 해결하는지 평가하는 기준이다.

Q. 좋은 Fix Recommendation은 뭐야?
A. 수정 대상, 방법, 검증 기준이 구체적이고 사용자 요구사항과 일치하는 수정 제안이다.

Q. “더 좋게 고쳐라”는 좋은 Fix야?
A. 아니다. 수정 대상, 방법, 기준이 구체적이어야 한다.

Q. Fix Direction도 Safety Evaluation이 필요해?
A. 필요하다. Fix가 위험 Tool 실행이나 범위 밖 수정을 요구할 수 있기 때문이다.

Q. Review Agent Checklist는 뭐야?
A. Review Agent가 Agent Output을 일관되게 검토하고 Review 자체 품질을 평가하기 위한 최소 검증 목록이다.

Q. Review Agent Checklist에서 가장 중요한 항목은 뭐야?
A. 사용자 요구사항, Domain Rules, Evidence, Severity, Fix Recommendation, Safety, Grounding 검증이다.

Q. Review Agent Output 최소 Pass 기준은 뭐야?
A. Finding이 구체적이고 Evidence와 Severity가 있으며 Fix Recommendation이 실행 가능해야 한다.

Q. Review Agent Evaluation의 최종 목표는 뭐야?
A. Review Agent가 실제 문제를 정확히 찾고, 근거 있는 Severity와 실행 가능한 Fix를 제공해 Multi-Agent Workflow 품질을 안정적으로 높이도록 만드는 것이다.
