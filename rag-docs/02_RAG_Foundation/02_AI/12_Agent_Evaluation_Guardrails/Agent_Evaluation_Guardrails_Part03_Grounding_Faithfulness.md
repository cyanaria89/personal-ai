# Agent Evaluation & Guardrails Part03 - Grounding & Faithfulness

---

# 1. Grounding Evaluation

## 1.1 Groundedness

### [개념]

Groundedness는 Agent Output의 주요 주장이 Retrieved Context, RAG 문서, 사용자 제공 정보, Tool Result 같은 근거에 기반하는지 평가하는 기준이다.

Groundedness는 RAG 기반 Agent Evaluation의 핵심이다.

Agent가 문서에 없는 내용을 확정적으로 말하면 Grounding Failure로 분류한다.

Groundedness 평가 대상:

- Answer Claim
- Code Claim
- Project-specific Fact
- API Path
- Class / Method / Field Name
- Configuration Value
- Tool Result Interpretation
- Citation / Source

---

### [핵심]

Grounding Evaluation 기본 Flow:

```text
Answer Claim
→ Match with Retrieved Context
→ Supported / Unsupported / Unknown
→ Mark Issue
→ Fix or Remove Unsupported Claim
```

Grounding 판단 기준:

| 기준              | 의미                                              |
| ----------------- | ------------------------------------------------- |
| Supported Claim   | Retrieved Context나 제공 문서로 확인 가능한 주장  |
| Unsupported Claim | 근거 문서에 없는 주장                             |
| Missing Evidence  | 주장에 필요한 근거가 부족한 상태                  |
| Assumption        | 근거가 부족하지만 명시적으로 가정으로 표시한 내용 |
| Contradiction     | Output이 Context와 충돌하는 상태                  |
| Wrong Citation    | Citation이 있지만 실제 내용과 맞지 않는 상태      |

Groundedness 결과:

```text
Pass:
- 주요 Claim이 Context에 근거함
- 프로젝트 고유 정보가 문서와 일치함
- 부족한 정보는 Missing Information으로 표시함

Fix:
- 일부 Claim 근거 부족
- Citation과 Claim 연결 약함
- Assumption 표시 누락

Fail:
- 핵심 Claim이 근거 없음
- 문서에 없는 프로젝트 사실 생성
- Context와 충돌
- 잘못된 Citation 사용
```

---

### [실무]

2026 실무 기준 RAG 기반 Agent는 Retrieved Context 우선 원칙을 따라야 한다.

개인 AI 개발팀 구조에서는 Backend Agent, Frontend Agent, Review Agent, PM Agent가 RAG 문서를 기반으로 코드를 생성하거나 검토한다.

Grounding Evaluation은 Agent가 실제 프로젝트 문서에 없는 내용을 만들어내지 않도록 검증한다.

실무 검증 순서:

```text
1. Agent Output에서 주요 Claim 추출
2. Claim을 Project Fact / General Knowledge / Assumption으로 분류
3. Project Fact는 Retrieved Context와 대조
4. 근거 없는 Claim은 Unsupported Claim으로 표시
5. Context 부족 시 Missing Information으로 처리
6. 필요하면 Assumption으로 낮춰서 표현
```

예시:

```text
Agent Claim:
NotificationRepository에는 findUnreadByUserId()가 있다.

Retrieved Context:
NotificationRepository에는 countByUsers_UserIdAndReadStatusFalse(Long userId)가 있다.

Evaluation:
- findUnreadByUserId()는 문서 근거 없음
- Unsupported Claim
- Fix 필요
```

Grounding Report 예시:

```md
### Grounding Check

| Claim                                      | Evidence                       | Result      | Fix                    |
| ------------------------------------------ | ------------------------------ | ----------- | ---------------------- |
| countByUsers_UserIdAndReadStatusFalse 사용 | Repository 문서에 존재         | Supported   | 없음                   |
| findUnreadByUserId 사용                    | 근거 없음                      | Unsupported | 실제 메서드명으로 수정 |
| 알림 읽음 처리는 Service에서 수행          | 구조상 가능하나 문서 근거 부족 | Assumption  | Assumption 표시        |
```

RAG 문서 작성 시 Grounding 강화 방법:

```text
- Section 제목에 핵심 키워드 포함
- FAQ에 실제 질문 표현 포함
- Retrieval Queries에 Claim 검증 질문 포함
- 코드 예시는 짧고 정확하게 작성
- 프로젝트 고유 명칭은 용어 통일
```

---

### [주의]

Grounding Evaluation 주의사항:

- Citation이 있다고 Groundedness가 자동으로 보장되지 않는다.
- 문서와 무관한 Citation은 Wrong Citation이다.
- 일반 개발 지식과 프로젝트 고유 사실을 구분해야 한다.
- 문서에 없는 API 경로, 클래스명, 메서드명 생성은 Hallucination이다.
- Retrieved Context가 부족하면 확정하지 않는다.
- 근거 없는 내용을 자신 있게 말하면 False Confidence가 된다.
- 문서 간 충돌이 있으면 Source Priority를 확인해야 한다.

---

### [Best Practice]

Grounding Evaluation Best Practice:

- 주요 Claim을 문장 단위로 분해한다.
- 프로젝트 고유 정보는 반드시 Retrieved Context와 대조한다.
- Supported / Unsupported / Unknown을 명확히 구분한다.
- Unsupported Claim은 제거하거나 근거 있는 표현으로 수정한다.
- Assumption은 명시적으로 표시한다.
- Missing Information을 임의 생성으로 채우지 않는다.
- Citation은 실제 Claim을 뒷받침하는 위치에 연결한다.
- Groundedness와 Correctness를 분리해서 평가한다.

---

### [FAQ]

Q. Groundedness가 뭐야?
A. Agent Output의 주요 주장이 Retrieved Context나 제공 문서에 근거하는지 확인하는 기준이다.

Q. RAG 답변에서 Groundedness가 왜 중요해?
A. RAG Agent는 문서 기반으로 답해야 하므로 근거 없는 답변은 신뢰도를 떨어뜨린다.

Q. Supported Claim은 뭐야?
A. Retrieved Context나 제공 문서에서 확인 가능한 주장이다.

Q. Unsupported Claim은 뭐야?
A. 문서나 Context에 근거가 없는 주장이다.

Q. Citation이 있으면 Groundedness는 통과야?
A. 아니다. Citation이 실제 Claim을 뒷받침해야 한다.

Q. 문서에 없는 프로젝트 정보를 말하면 어떻게 돼?
A. Unsupported Claim 또는 Hallucination으로 처리해야 한다.

Q. 근거가 부족하면 어떻게 답해야 해?
A. Missing Information으로 표시하거나 Assumption으로 낮춰서 표현해야 한다.

---

# 2. Evidence Evaluation

## 2.1 Evidence

### [개념]

Evidence는 Agent Output의 Claim을 뒷받침하는 근거 정보다.

Evidence는 RAG 문서, 사용자 제공 코드, Tool Result, 로그, 설정 파일, 테스트 결과, 공식 문서, 검색 결과 등이 될 수 있다.

Evidence Evaluation은 Claim과 Evidence가 실제로 연결되는지 확인한다.

---

### [핵심]

Evidence 유형:

| Evidence Type         | 예시                                   |
| --------------------- | -------------------------------------- |
| Retrieved Context     | RAG 검색으로 가져온 문서 Chunk         |
| User Provided Context | 사용자가 업로드한 코드, 문서, 요구사항 |
| Tool Result           | 파일 검색, 테스트 실행, 빌드 결과      |
| Source Citation       | 출처가 명시된 문서나 웹 자료           |
| Runtime Evidence      | 로그, 에러 메시지, 실행 결과           |
| Code Evidence         | 실제 클래스, 메서드, 필드, 설정        |

Evidence Evaluation Flow:

```text
Claim
→ Identify Required Evidence
→ Check Evidence Exists
→ Check Evidence Matches Claim
→ Supported / Weak / Missing
```

Evidence 강도:

| 강도                 | 의미                         |
| -------------------- | ---------------------------- |
| Strong Evidence      | Claim을 직접 뒷받침          |
| Weak Evidence        | 관련은 있으나 직접 근거 부족 |
| Missing Evidence     | 근거 없음                    |
| Conflicting Evidence | Claim과 반대되는 근거 존재   |

---

### [실무]

실무에서는 Evidence를 Claim 단위로 연결해야 한다.

좋은 Evidence 연결 예시:

```text
Claim:
RAG 문서에는 [FAQ]와 Retrieval Queries가 필요하다.

Evidence:
Master Rules에서 Required Section과 Retrieval Queries Block을 요구한다.

Result:
Supported
```

나쁜 Evidence 연결 예시:

```text
Claim:
프로젝트는 Kafka를 사용 중이다.

Evidence:
Project Progress의 Expert Planned 목록에 Kafka가 있다.

Result:
Unsupported
Reason:
Planned 목록은 현재 사용 중이라는 근거가 아니다.
```

Evidence Table 예시:

```md
| Claim                                                | Evidence Type | Evidence                   | Result      |
| ---------------------------------------------------- | ------------- | -------------------------- | ----------- |
| Agent Evaluation은 Requirement Compliance를 평가한다 | Domain Rules  | Evaluation Dimensions 포함 | Supported   |
| 모든 Tool은 자동 실행 가능하다                       | 없음          | 근거 없음                  | Unsupported |
| High Risk 작업은 사용자 승인 필요                    | Domain Rules  | Human Confirmation Rule    | Supported   |
```

Evidence 판단 기준:

```text
Direct Evidence:
- 문서에 명시됨
- 코드에 실제 존재함
- Tool 결과로 확인됨

Indirect Evidence:
- 구조상 추론 가능
- 일반 개발 지식으로 가능
- Assumption 표시 필요

No Evidence:
- 문서에 없음
- 코드에 없음
- Tool 결과 없음
```

---

### [주의]

Evidence Evaluation 주의사항:

- 관련 있어 보이는 문서가 실제 근거가 아닐 수 있다.
- Planned 상태를 Completed로 해석하면 안 된다.
- 예시 코드를 실제 프로젝트 코드로 착각하면 안 된다.
- Tool 결과가 실패했는데 성공 Evidence로 쓰면 안 된다.
- Evidence 없이 확정 표현을 쓰면 안 된다.
- 오래된 Memory는 현재 Evidence보다 약하다.

---

### [Best Practice]

Evidence Evaluation Best Practice:

- Claim마다 Evidence를 연결한다.
- Evidence가 직접 근거인지 간접 근거인지 구분한다.
- Weak Evidence는 확정 표현을 피한다.
- Missing Evidence는 Missing Information으로 표시한다.
- Conflicting Evidence가 있으면 Source Priority를 적용한다.
- Tool Result는 성공 여부와 한계를 함께 확인한다.
- 프로젝트 고유 사실은 실제 파일, 코드, 문서 근거를 우선한다.

---

### [FAQ]

Q. Evidence는 뭐야?
A. Agent Output의 Claim을 뒷받침하는 근거 정보다.

Q. Evidence Evaluation은 왜 필요해?
A. Agent가 근거 없는 주장을 하지 않았는지 확인하기 위해 필요하다.

Q. Strong Evidence는 뭐야?
A. Claim을 직접 뒷받침하는 명시적 근거다.

Q. Weak Evidence는 어떻게 처리해?
A. 확정 표현을 피하고 Assumption 또는 가능성으로 표시해야 한다.

Q. Planned 목록은 현재 사용 중이라는 Evidence야?
A. 아니다. Planned는 계획 상태일 뿐 현재 사용 중이라는 직접 근거가 아니다.

Q. Tool 실패 결과를 Evidence로 쓸 수 있어?
A. 쓸 수 있지만 성공 Evidence가 아니라 실패 Evidence로 해석해야 한다.

---

# 3. Faithfulness Evaluation

## 3.1 Faithfulness

### [개념]

Faithfulness는 Agent Output이 제공된 Context를 왜곡하거나 과장하지 않고 충실히 반영하는지 평가하는 기준이다.

Faithfulness는 Groundedness와 다르다.

Groundedness는 근거가 있는지 확인한다.

Faithfulness는 근거 내용을 정확하게 반영했는지 확인한다.

---

### [핵심]

Faithfulness 검증 항목:

| 항목                       | 의미                                 |
| -------------------------- | ------------------------------------ |
| Context Consistency        | Output이 Context와 일치하는가        |
| Contradiction              | Context와 반대되는 내용이 있는가     |
| Overstatement              | 조건부 내용을 절대 규칙처럼 말했는가 |
| Omission                   | 중요한 조건이나 예외를 누락했는가    |
| Misinterpretation          | Context 의미를 잘못 해석했는가       |
| Unsupported Generalization | 일부 사례를 일반 규칙으로 확대했는가 |

Faithfulness Evaluation Flow:

```text
Retrieved Context
→ Agent Summary / Answer
→ Check Meaning Preservation
→ Faithful / Distorted / Overstated
```

Faithfulness 판단:

```text
Faithful:
- Context 의미를 그대로 반영
- 조건과 예외 유지
- 과장 없음

Distorted:
- Context 의미 변경
- 조건 누락
- 반대로 해석

Overstated:
- 가능성을 확정으로 표현
- 일부 사례를 전체 규칙처럼 표현
```

---

### [실무]

실무에서는 Faithfulness를 요약, 코드 리뷰, RAG 답변에서 반드시 확인한다.

예시 1:

```text
Context:
ResponseEntity<ApiResponse<T>>도 사용할 수 있지만 프로젝트 규칙은 ApiResponse<T> 직접 반환이다.

Unfaithful Output:
ResponseEntity<ApiResponse<T>>는 사용하면 안 된다.

Issue:
조건과 맥락을 왜곡함.
프로젝트 규칙상 직접 반환이 우선이라는 의미이지, 모든 상황에서 금지는 아니다.
```

예시 2:

```text
Context:
Level 2 AI 문서 중 Agent Evaluation & Guardrails는 Planned 상태다.

Unfaithful Output:
Agent Evaluation & Guardrails는 이미 완료됐다.

Issue:
Planned 상태를 Completed로 왜곡함.
```

예시 3:

```text
Context:
High Risk 작업은 사용자 승인 필요.

Faithful Output:
삭제, DB 변경, 배포, 이메일 발송처럼 위험도가 높은 작업은 실행 전 사용자 승인이 필요하다.
```

Faithfulness Report 예시:

```md
| Context             | Output Claim   | Result        | Issue          | Fix                  |
| ------------------- | -------------- | ------------- | -------------- | -------------------- |
| Planned ⬜          | 완료됨         | Unfaithful    | 상태 왜곡      | Planned로 수정       |
| High Risk 승인 필요 | 자동 실행 가능 | Contradiction | 안전 규칙 반대 | 승인 필요로 수정     |
| 가능                | 항상 가능      | Overstatement | 조건 누락      | 조건부 표현으로 수정 |
```

---

### [주의]

Faithfulness 주의사항:

- 요약 과정에서 조건을 제거하면 의미가 바뀔 수 있다.
- “가능하다”를 “항상 된다”로 바꾸면 Overstatement다.
- “계획”을 “완료”로 바꾸면 상태 왜곡이다.
- 예시를 규칙처럼 일반화하면 안 된다.
- Context의 일부만 보고 전체를 단정하지 않는다.
- 문서 간 충돌이 있으면 우선순위를 명시한다.

---

### [Best Practice]

Faithfulness Best Practice:

- Context의 조건, 예외, 상태 표현을 유지한다.
- 요약 시 의미를 축소하거나 확대하지 않는다.
- 가능성, 권장, 필수, 금지를 구분한다.
- Completed / Planned / In Progress 상태를 정확히 반영한다.
- “일반적으로”와 “프로젝트 기준”을 구분한다.
- 문서 내용을 바꿔 말할 때 핵심 의미가 유지되는지 확인한다.
- 불확실하면 확정 표현을 피한다.

---

### [FAQ]

Q. Faithfulness가 뭐야?
A. Agent Output이 제공된 Context를 왜곡하거나 과장하지 않고 충실히 반영하는지 평가하는 기준이다.

Q. Groundedness와 Faithfulness 차이는?
A. Groundedness는 근거가 있는지 확인하고, Faithfulness는 근거 내용을 정확히 반영했는지 확인한다.

Q. Overstatement는 뭐야?
A. 조건부 내용이나 가능성을 절대 규칙처럼 과장해서 표현하는 것이다.

Q. Omission도 Faithfulness 문제야?
A. 맞다. 중요한 조건이나 예외를 누락하면 Context 의미가 바뀔 수 있다.

Q. Planned를 Completed로 말하면 어떤 문제야?
A. Context 상태를 왜곡한 Faithfulness Failure다.

Q. 요약할 때 Faithfulness를 지키려면 어떻게 해?
A. 조건, 예외, 상태, 범위를 유지하고 의미를 과장하지 않아야 한다.

---

# 4. Hallucination Detection

## 4.1 Hallucination

### [개념]

Hallucination은 Agent가 실제 근거가 없는 정보를 그럴듯하게 생성하는 실패 유형이다.

Hallucination은 RAG 기반 Agent, 코드 생성 Agent, 프로젝트 분석 Agent에서 특히 위험하다.

Hallucination은 Unsupported Claim의 한 형태이며, 프로젝트 고유 정보에서 치명적인 오류를 만들 수 있다.

---

### [핵심]

Hallucination 유형:

| 유형              | 예시                                |
| ----------------- | ----------------------------------- |
| Fabricated Fact   | 문서에 없는 사실 생성               |
| Fabricated File   | 존재하지 않는 파일명 생성           |
| Fabricated API    | 문서에 없는 API 경로 생성           |
| Fabricated Class  | 존재하지 않는 클래스명 생성         |
| Fabricated Method | 존재하지 않는 메서드명 생성         |
| Unsupported Code  | 프로젝트 구조와 맞지 않는 코드 생성 |
| Wrong Citation    | Citation이 Claim을 뒷받침하지 않음  |
| False Confidence  | 불확실한 내용을 확정적으로 말함     |

Hallucination Detection Flow:

```text
Agent Output
→ Extract Project-specific Claims
→ Match with Context / Code / Tool Result
→ Unsupported Claim Check
→ Hallucination Mark
→ Fix / Remove / Ask
```

Hallucination 판단:

```text
High Risk Hallucination:
- 존재하지 않는 API / 클래스 / 메서드 생성
- 잘못된 보안 정책 설명
- 위험 Tool 실행 근거 조작
- 프로젝트 상태 왜곡

Low Risk Hallucination:
- 일반 설명의 작은 부정확성
- 예시 명칭 혼동
- 영향이 적은 표현 오류
```

---

### [실무]

실무에서는 Hallucination을 프로젝트 고유 Claim 중심으로 탐지한다.

프로젝트 고유 Claim:

```text
- 파일명
- 패키지명
- 클래스명
- 메서드명
- 필드명
- API Endpoint
- DB Table
- 설정 Key
- 배포 환경
- 현재 진행 상태
```

예시:

```text
Agent Output:
FestivalController에는 /festival/popular API가 이미 있다.

Context:
제공된 API 목록에는 /festival, /festival/search, /festival/detail/{id}, /festival/location/{id}만 있음.

Evaluation:
- /festival/popular 근거 없음
- Fabricated API
- Hallucination
```

Hallucination Report 예시:

```md
| Claim                  | Type            | Evidence              | Result        | Fix                       |
| ---------------------- | --------------- | --------------------- | ------------- | ------------------------- |
| /festival/popular 존재 | Fabricated API  | API 목록에 없음       | Hallucination | 제거 또는 Assumption 처리 |
| UserResDto 존재        | Supported       | DTO 목록에 있음       | Pass          | 없음                      |
| Kafka 사용 중          | Fabricated Fact | Planned 목록에만 있음 | Hallucination | 계획 상태로 수정          |
```

Hallucination 수정 방법:

```text
- 문서에 없는 Claim 제거
- 실제 Context에 있는 명칭으로 수정
- 검증 불가 내용은 Assumption 표시
- 필요한 경우 사용자에게 파일 / 코드 확인 요청
- Tool 검색으로 실제 존재 여부 확인
```

---

### [주의]

Hallucination Detection 주의사항:

- Agent가 자신 있게 말해도 근거가 없을 수 있다.
- 일반 개발 지식으로 프로젝트 고유 사실을 채우면 안 된다.
- 예시 코드를 실제 코드처럼 설명하면 안 된다.
- Planned를 Completed로 말하는 것도 Hallucination이 될 수 있다.
- 파일명이나 메서드명은 작은 오타도 큰 오류가 될 수 있다.
- Wrong Citation은 Hallucination을 숨길 수 있다.

---

### [Best Practice]

Hallucination Detection Best Practice:

- 프로젝트 고유 명칭을 우선 검증한다.
- 문서에 없는 API / 클래스 / 메서드를 자동 생성하지 않는다.
- 근거 없는 확정 표현을 제거한다.
- 불확실하면 Assumption 또는 Missing Information으로 표시한다.
- Tool 검색 결과가 없으면 없는 것으로 확정하지 않고 “제공된 Context에는 없음”으로 표현한다.
- Review Agent는 Unsupported Claim 목록을 별도로 작성한다.
- Hallucination은 Severity를 높게 평가한다.

---

### [FAQ]

Q. Hallucination이 뭐야?
A. Agent가 실제 근거가 없는 정보를 그럴듯하게 생성하는 실패 유형이다.

Q. Hallucination과 Unsupported Claim은 같은 거야?
A. Hallucination은 Unsupported Claim의 한 형태다. 특히 없는 정보를 만들어낸 경우를 말한다.

Q. 프로젝트 분석에서 Hallucination은 왜 위험해?
A. 존재하지 않는 API, 클래스, 메서드 기준으로 코드를 만들면 컴파일 오류나 설계 오류가 발생한다.

Q. Fabricated API는 뭐야?
A. 실제 문서나 코드에 없는 API 경로를 만들어낸 것이다.

Q. Fabricated Class는 뭐야?
A. 실제 프로젝트에 없는 클래스명을 생성한 것이다.

Q. Hallucination은 어떻게 잡아?
A. 프로젝트 고유 Claim을 Context, 코드, Tool Result와 대조해서 근거 없는 항목을 찾는다.

Q. 근거가 없지만 가능해 보이면 말해도 돼?
A. 확정하면 안 된다. Assumption으로 표시하거나 Missing Information으로 처리해야 한다.

---

# 5. Unsupported Claim Check

## 5.1 Unsupported Claim

### [개념]

Unsupported Claim은 Agent Output 안에서 제공된 Context나 Evidence로 뒷받침되지 않는 주장이다.

Unsupported Claim은 Hallucination보다 넓은 개념이다.

모든 Hallucination은 Unsupported Claim이지만, 모든 Unsupported Claim이 Hallucination은 아니다.

---

### [핵심]

Unsupported Claim 유형:

| 유형                  | 의미                                      |
| --------------------- | ----------------------------------------- |
| No Evidence Claim     | 근거가 전혀 없는 주장                     |
| Weak Evidence Claim   | 근거가 약한데 확정한 주장                 |
| Out-of-Scope Claim    | 제공 범위를 벗어난 주장                   |
| Overgeneralized Claim | 일부 근거를 전체 규칙으로 확대한 주장     |
| Mis-cited Claim       | Citation이 있지만 실제 근거가 아닌 주장   |
| Stale Memory Claim    | 오래된 Memory를 현재 사실처럼 사용한 주장 |

Unsupported Claim Check Flow:

```text
Output Claim
→ Evidence Exists?
→ Evidence Strong Enough?
→ Scope Valid?
→ Supported / Unsupported / Assumption
```

Unsupported Claim 처리:

```text
Remove:
- 근거 없는 내용 제거

Revise:
- 근거 있는 표현으로 수정

Downgrade:
- 확정 표현을 Assumption / 가능성으로 변경

Ask:
- 필요한 정보가 없으면 사용자 확인

Stop:
- 핵심 Claim 근거가 없고 안전 위험이 있으면 중단
```

---

### [실무]

실무에서는 Unsupported Claim을 평가 Report에 명시적으로 기록한다.

예시:

```text
Output Claim:
Docker 문서는 완료되지 않았다.

Project Progress:
Docker (Part01 ~ Part04) Completed ✅

Evaluation:
- Context와 충돌
- Unsupported Claim
- Fix: Docker 완료 상태로 수정
```

Unsupported Claim Table:

```md
| Claim                      | Evidence Status      | Issue                        | Fix                           |
| -------------------------- | -------------------- | ---------------------------- | ----------------------------- |
| Docker 미완료              | Conflicting Evidence | Completed와 충돌             | 완료로 수정                   |
| Agent Evaluation 이미 완료 | Conflicting Evidence | Planned 상태                 | Planned 또는 작성 중으로 수정 |
| Tool 자동 실행 가능        | No Evidence          | Human Confirmation Rule 위반 | 위험도별 승인 필요로 수정     |
```

Claim 분류 예시:

```text
Supported:
문서에 명시된 내용

Unsupported:
문서에 없는 프로젝트 사실

Assumption:
명시 근거는 없지만 추론이며 Assumption으로 표시한 내용

Unknown:
현재 Context로 판단 불가
```

---

### [주의]

Unsupported Claim Check 주의사항:

- 확신 있는 문체가 근거를 대체하지 않는다.
- 일부 근거가 있어도 Claim 범위가 넓으면 Unsupported일 수 있다.
- 오래된 Memory는 현재 문서와 충돌할 수 있다.
- 공식처럼 보이는 문서 제목도 실제 내용을 확인해야 한다.
- 프로젝트 고유 정보는 일반 지식으로 보완하지 않는다.
- Unsupported Claim이 핵심 결론이면 Output 전체가 Fix 대상이다.

---

### [Best Practice]

Unsupported Claim Check Best Practice:

- Claim을 작은 단위로 분해한다.
- 프로젝트 고유 Claim을 우선 검증한다.
- Evidence Status를 Supported / Unsupported / Assumption / Unknown으로 표시한다.
- 근거가 약하면 표현 강도를 낮춘다.
- Missing Information을 명확히 보고한다.
- Unsupported Claim 목록을 Review Report에 포함한다.
- 핵심 Unsupported Claim은 Major 또는 Critical로 분류한다.

---

### [FAQ]

Q. Unsupported Claim은 뭐야?
A. 제공된 Context나 Evidence로 뒷받침되지 않는 주장이다.

Q. Hallucination과 Unsupported Claim 차이는?
A. Hallucination은 없는 정보를 생성한 경우이고, Unsupported Claim은 근거가 부족한 모든 주장을 포함한다.

Q. Unsupported Claim은 모두 삭제해야 해?
A. 아니다. 제거, 수정, Assumption 처리, 사용자 확인 중 적절한 방식으로 처리한다.

Q. Weak Evidence Claim은 뭐야?
A. 근거가 약한데 확정적으로 표현한 주장이다.

Q. 오래된 Memory를 현재 사실처럼 쓰면 Unsupported Claim이야?
A. 현재 Context와 맞지 않거나 최신성 검증이 없으면 Unsupported Claim이 될 수 있다.

Q. Unsupported Claim이 핵심 결론이면 어떻게 해?
A. Output은 Fix 또는 Stop 대상이다.

---

# 6. Missing Information Rule

## 6.1 Missing Information

### [개념]

Missing Information은 Agent가 정확한 답변이나 안전한 실행을 위해 필요한 정보가 부족한 상태다.

Missing Information Rule은 정보가 부족할 때 Agent가 임의로 생성하지 않고 부족한 정보를 명확히 표시하도록 하는 규칙이다.

---

### [핵심]

Missing Information 발생 상황:

| 상황                | 예시                          |
| ------------------- | ----------------------------- |
| Context 없음        | 프로젝트 파일이 제공되지 않음 |
| Evidence 부족       | API 존재 여부 확인 불가       |
| Requirement 불명확  | 출력 범위가 정의되지 않음     |
| Tool 실패           | 파일 검색 또는 실행 실패      |
| Permission 부족     | 실행 권한 없음                |
| Conflicting Context | 문서 간 내용 충돌             |
| Low Confidence      | 검증 불가한 상태              |

Missing Information Flow:

```text
Need Information
→ Check Context / Evidence / Tool Result
→ Missing?
→ Mark Missing Information
→ Ask / Assumption / Stop
```

처리 방식:

```text
Ask:
- 사용자 확인이 필요한 경우

Assumption:
- 낮은 위험도에서 가정 가능하고 명시 가능한 경우

Stop:
- 핵심 정보가 없거나 위험 작업인 경우

Partial Answer:
- 제공된 Context 범위 내에서만 답변 가능한 경우
```

---

### [실무]

실무에서는 Missing Information을 확정 답변으로 대체하지 않는다.

예시:

```text
상황:
Repository 코드가 제공되지 않음.

나쁜 답변:
UserRepository에는 existsByEmail()이 있으니 사용하면 됩니다.

좋은 답변:
제공된 Context에는 UserRepository 메서드 정보가 없다.
existsByEmail() 사용은 일반적인 구현 Assumption이며, 실제 메서드 존재 여부 확인이 필요하다.
```

RAG 답변 예시:

```text
상황:
Retrieved Context에 API 경로가 없음.

좋은 처리:
제공된 문서에서는 해당 API 경로를 확인할 수 없다.
프로젝트 고유 API로 확정하지 않고, 필요한 파일은 Controller 코드다.
```

Missing Information Report:

```md
| Missing Information         | Impact                  | Handling                  |
| --------------------------- | ----------------------- | ------------------------- |
| Controller 실제 코드 없음   | API 존재 여부 검증 불가 | Missing으로 표시          |
| Repository 메서드 목록 없음 | 코드 생성 위험          | Assumption 또는 확인 필요 |
| 배포 환경 정보 없음         | 배포 명령 제안 위험     | Stop                      |
```

---

### [주의]

Missing Information 주의사항:

- 정보가 부족한데 확정하면 Hallucination이 된다.
- 위험 작업에서는 Assumption으로 진행하면 안 된다.
- 프로젝트 고유 정보는 일반 지식으로 채우지 않는다.
- 질문이 불명확해도 핵심 요구사항은 임의 변경하지 않는다.
- Tool 실패를 무시하고 완료 처리하지 않는다.
- Missing Information을 숨기면 Review 품질이 낮아진다.

---

### [Best Practice]

Missing Information Best Practice:

- 부족한 정보를 구체적으로 표시한다.
- 부족한 정보가 결과에 미치는 영향을 설명한다.
- 가능한 범위와 불가능한 범위를 분리한다.
- 낮은 위험도에서는 Assumption을 명시한다.
- 높은 위험도에서는 Stop 또는 Human Confirmation으로 처리한다.
- Partial Answer는 제공된 Context 범위로 제한한다.
- 필요한 추가 파일, 코드, 설정을 명확히 적는다.

---

### [FAQ]

Q. Missing Information은 뭐야?
A. Agent가 정확한 답변이나 안전한 실행을 위해 필요한 정보가 부족한 상태다.

Q. 정보가 부족하면 어떻게 해야 해?
A. 부족한 정보를 표시하고 Ask, Assumption, Stop, Partial Answer 중 적절한 방식으로 처리해야 한다.

Q. Missing Information을 임의로 채워도 돼?
A. 안 된다. 임의로 채우면 Hallucination이나 Unsupported Claim이 될 수 있다.

Q. 언제 Assumption으로 처리해도 돼?
A. 위험도가 낮고 가정임을 명확히 표시할 수 있을 때만 가능하다.

Q. 위험 작업에서 정보가 부족하면 어떻게 해?
A. Stop하거나 Human Confirmation을 요구해야 한다.

Q. Partial Answer는 언제 가능해?
A. 제공된 Context 범위 안에서만 답변할 수 있을 때 가능하다.

---

# 7. RAG Grounding Checklist

## 7.1 Grounding Checklist

### [개념]

RAG Grounding Checklist는 RAG 기반 Agent Output이 문서 근거를 충실히 따르는지 확인하는 최소 검증 목록이다.

Review Agent와 RAG Evaluation Agent는 이 Checklist를 사용해 Grounding Failure, Hallucination, Unsupported Claim을 탐지한다.

---

### [핵심]

RAG Grounding Checklist:

```md
### [Checklist]

- [ ] 주요 Claim을 문장 단위로 추출했는가?
- [ ] 각 Claim에 Evidence가 연결되는가?
- [ ] 프로젝트 고유 정보가 Retrieved Context와 일치하는가?
- [ ] 문서에 없는 API / 클래스 / 메서드를 생성하지 않았는가?
- [ ] Citation이 실제 Claim을 뒷받침하는가?
- [ ] Context의 조건과 예외를 유지했는가?
- [ ] Planned / Completed / In Progress 상태를 정확히 반영했는가?
- [ ] Weak Evidence를 확정 표현으로 쓰지 않았는가?
- [ ] Missing Information을 명확히 표시했는가?
- [ ] Assumption을 명시했는가?
- [ ] Unsupported Claim을 제거하거나 수정했는가?
- [ ] Conflicting Evidence가 있으면 Source Priority를 적용했는가?
```

최소 Pass 기준:

```text
- 핵심 Claim이 Evidence에 근거함
- 프로젝트 고유 정보 Hallucination 없음
- Wrong Citation 없음
- Context 왜곡 없음
- Missing Information 숨김 없음
```

---

### [실무]

실무에서는 RAG Grounding Checklist를 Agent Output Review 단계에 적용한다.

적용 위치:

```text
Retrieved Context
→ Agent Draft
→ RAG Grounding Checklist
→ Unsupported Claim Fix
→ Faithfulness Check
→ Final Output
```

RAG 문서 생성 시 적용:

```text
Draft RAG Document
→ Domain Rules 확인
→ Required Section 확인
→ FAQ / Retrieval Queries 확인
→ 용어 통일 확인
→ Grounding / Faithfulness 확인
```

RAG 답변 생성 시 적용:

```text
User Query
→ Retrieve Documents
→ Answer Generate
→ Claim-Evidence Match
→ Unsupported Claim Remove
→ Missing Information 표시
```

Checklist 결과 예시:

```md
### RAG Grounding Result

| Item                     | Result | Evidence                    | Fix  |
| ------------------------ | ------ | --------------------------- | ---- |
| 핵심 Claim Evidence 연결 | Pass   | Domain Rules와 일치         | 없음 |
| Fabricated API 없음      | Fail   | /festival/popular 근거 없음 | 제거 |
| Missing Information 표시 | Pass   | Controller 코드 없음 표시   | 없음 |
```

---

### [주의]

RAG Grounding Checklist 주의사항:

- Checklist는 최소 기준이다.
- Claim 수가 많으면 핵심 Claim부터 검증한다.
- 문서에 있는 단어가 Claim 전체를 뒷받침하는 것은 아니다.
- 일반 개발 지식은 프로젝트 고유 정보의 Evidence가 아니다.
- Citation 형식만 맞아도 Wrong Citation일 수 있다.
- Retrieval 실패를 답변 성공으로 포장하면 안 된다.

---

### [Best Practice]

RAG Grounding Checklist Best Practice:

- Claim-Evidence 표를 사용한다.
- 프로젝트 고유 명칭을 우선 검증한다.
- Unsupported Claim을 Review Findings에 포함한다.
- Faithfulness Check를 Grounding Check와 함께 수행한다.
- Missing Information은 숨기지 않는다.
- Weak Evidence는 표현 강도를 낮춘다.
- Final Output 전에 핵심 Claim만이라도 재검증한다.

---

### [FAQ]

Q. RAG Grounding Checklist는 뭐야?
A. RAG 기반 Agent Output이 문서 근거에 기반하는지 확인하는 최소 검증 목록이다.

Q. RAG Grounding Checklist는 언제 써?
A. Agent Draft 생성 후 Final Output 전에 사용한다.

Q. Checklist에서 가장 중요한 항목은 뭐야?
A. 핵심 Claim이 Evidence에 근거하는지와 프로젝트 고유 정보 Hallucination이 없는지다.

Q. Citation 형식이 맞으면 통과야?
A. 아니다. Citation이 실제 Claim을 뒷받침해야 한다.

Q. Retrieved Context가 부족하면 어떻게 해?
A. Missing Information으로 표시하고 프로젝트 고유 정보를 확정하지 않는다.

Q. Grounding Checklist만 있으면 충분해?
A. 아니다. Requirement Compliance, Format Compliance, Safety Evaluation도 함께 필요하다.

---

# Retrieval Queries

### [FAQ]

Q. Groundedness가 뭐야?
A. Agent Output의 주요 주장이 Retrieved Context나 제공 문서에 근거하는지 확인하는 기준이다.

Q. Grounding Evaluation은 어떻게 해?
A. Answer Claim을 추출하고 Retrieved Context와 대조해 Supported, Unsupported, Unknown으로 분류한다.

Q. RAG 답변에서 Groundedness가 중요한 이유는?
A. RAG Agent는 문서 기반 답변을 해야 하므로 근거 없는 답변은 신뢰도와 정확성을 떨어뜨린다.

Q. Supported Claim은 뭐야?
A. Retrieved Context나 제공 문서에서 직접 확인 가능한 주장이다.

Q. Unsupported Claim은 뭐야?
A. 제공된 Context나 Evidence로 뒷받침되지 않는 주장이다.

Q. Missing Evidence는 뭐야?
A. Claim을 검증하기에 필요한 근거가 부족한 상태다.

Q. Assumption은 언제 써?
A. 근거가 부족하지만 낮은 위험도에서 가정이 가능하고 이를 명시할 수 있을 때 사용한다.

Q. Evidence Evaluation은 뭐야?
A. Agent Output의 Claim을 뒷받침하는 근거가 실제로 존재하고 Claim과 연결되는지 평가하는 과정이다.

Q. Strong Evidence는 뭐야?
A. Claim을 직접 뒷받침하는 명시적 근거다.

Q. Weak Evidence는 어떻게 처리해?
A. 확정 표현을 피하고 Assumption이나 가능성으로 낮춰 표현해야 한다.

Q. Faithfulness가 뭐야?
A. Agent Output이 제공된 Context를 왜곡하거나 과장하지 않고 충실히 반영하는지 평가하는 기준이다.

Q. Groundedness와 Faithfulness 차이는?
A. Groundedness는 근거 존재 여부를 보고, Faithfulness는 근거 내용을 정확히 반영했는지 본다.

Q. Overstatement는 뭐야?
A. 조건부 내용이나 가능성을 절대 규칙처럼 과장해서 표현하는 것이다.

Q. Omission은 왜 Faithfulness 문제야?
A. 중요한 조건이나 예외를 누락하면 Context 의미가 바뀔 수 있기 때문이다.

Q. Hallucination이 뭐야?
A. Agent가 실제 근거가 없는 정보를 그럴듯하게 생성하는 실패 유형이다.

Q. Hallucination은 어떻게 탐지해?
A. 프로젝트 고유 Claim을 Context, 코드, Tool Result와 대조해 근거 없는 항목을 찾는다.

Q. Fabricated API는 뭐야?
A. 실제 문서나 코드에 없는 API 경로를 만들어낸 것이다.

Q. Fabricated Class는 뭐야?
A. 실제 프로젝트에 없는 클래스명을 만들어낸 것이다.

Q. Wrong Citation은 뭐야?
A. Citation은 있지만 실제로 Claim을 뒷받침하지 않는 경우다.

Q. False Confidence는 뭐야?
A. 불확실하거나 근거 없는 내용을 확정적으로 말하는 것이다.

Q. Unsupported Claim은 모두 Hallucination이야?
A. 아니다. Hallucination은 Unsupported Claim의 한 형태지만, Unsupported Claim은 근거가 약하거나 범위를 벗어난 주장도 포함한다.

Q. Missing Information은 뭐야?
A. 정확한 답변이나 안전한 실행을 위해 필요한 정보가 부족한 상태다.

Q. 정보가 부족하면 어떻게 해야 해?
A. Missing Information으로 표시하고 Ask, Assumption, Stop, Partial Answer 중 적절한 방식으로 처리해야 한다.

Q. RAG Grounding Checklist는 뭐야?
A. RAG 기반 Agent Output이 문서 근거를 충실히 따르는지 확인하는 최소 검증 목록이다.

Q. RAG Grounding Checklist 핵심 항목은 뭐야?
A. Claim-Evidence 연결, 프로젝트 고유 정보 검증, Citation 정확성, Context 왜곡 여부, Missing Information 표시다.

Q. Retrieved Context가 없으면 프로젝트 정보를 답해도 돼?
A. 프로젝트 고유 정보는 확정하면 안 된다. 제공된 Context에는 없다고 표시해야 한다.

Q. Planned를 Completed로 말하면 어떤 문제야?
A. Context 상태를 왜곡한 Faithfulness Failure이며 Unsupported Claim이 될 수 있다.

Q. 문서에 없는 클래스명을 코드에 사용하면 어떤 문제야?
A. Fabricated Class이며 Hallucination으로 분류해야 한다.

Q. Grounding Evaluation 결과는 어떻게 나눠?
A. Supported, Unsupported, Unknown, Assumption, Contradiction으로 나눌 수 있다.

Q. Grounding Failure는 어떻게 수정해?
A. Unsupported Claim을 제거하거나 Evidence 기반으로 수정하고, 검증 불가 내용은 Assumption 또는 Missing Information으로 표시한다.
