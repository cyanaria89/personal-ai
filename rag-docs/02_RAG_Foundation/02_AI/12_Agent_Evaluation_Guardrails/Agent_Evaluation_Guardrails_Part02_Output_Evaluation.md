# Agent Evaluation & Guardrails Part02 - Output Evaluation

---

# 1. Output Evaluation

## 1.1 Output Evaluation Core

### [개념]

Output Evaluation은 Agent가 생성한 산출물이 사용자 요청과 요구사항을 정확히 반영했는지 평가하는 과정이다.

Output Evaluation은 Agent Output의 품질을 다음 기준으로 검증한다.

- Task Match
- Requirement Compliance
- Completeness
- Correctness
- Groundedness
- Faithfulness
- Format Compliance
- Safety
- Actionability

Output Evaluation은 최종 답변뿐 아니라 중간 산출물, 코드, 문서, 계획, 요약, 리포트, Tool 결과 해석에도 적용된다.

---

### [핵심]

Output Evaluation 기본 Flow:

```text
User Requirement
→ Agent Output
→ Compare Requirement
→ Check Missing / Wrong / Unsupported / Unsafe Parts
→ Pass / Fix / Stop
```

핵심 검증 항목:

| 항목                | 검증 내용                       |
| ------------------- | ------------------------------- |
| Task Match          | 사용자 요청과 결과가 일치하는가 |
| Missing Requirement | 요구사항 누락이 있는가          |
| Wrong Assumption    | 임의 가정이 있는가              |
| Unsupported Claim   | 근거 없는 주장이 있는가         |
| Incorrect Format    | 요구 형식을 위반했는가          |
| Ambiguous Answer    | 모호한 답변이 있는가            |
| Actionable Result   | 실행 가능한 결과인가            |

Output Evaluation 결과:

```text
Pass:
- 요구사항 충족
- 주요 결함 없음
- 근거 충분
- 형식 준수
- 안전 문제 없음

Fix:
- 일부 누락
- 일부 오류
- 근거 부족
- 형식 일부 위반
- 개선 필요

Stop:
- 필수 정보 부족
- 위험 작업 승인 필요
- 근거 없는 핵심 주장
- Tool 실패
- 안전 문제
```

---

### [실무]

2026 실무 기준 Output Evaluation은 Agent Workflow의 품질 보증 단계다.

개인 AI 개발팀 구조에서는 PM Agent, Backend Agent, Frontend Agent, Review Agent, DevOps Agent, AI/ML Agent가 각자 Output을 생성한다.

각 Output은 다음 단계로 전달되기 전에 평가되어야 한다.

실무 평가 순서:

```text
1. User Requirement 추출
2. Must Requirement / Must Not Requirement 분리
3. Agent Output과 요구사항 대조
4. 누락 / 오류 / 임의 가정 확인
5. 근거 문서와 주요 Claim 대조
6. 출력 형식 확인
7. 안전성 확인
8. Pass / Fix / Stop 결정
```

예시:

```text
User Request:
- RAG 문서 작성
- MASTER_RAG_RULES 적용
- DOMAIN_RULES 적용
- FAQ 강화
- Retrieval Queries 포함
- 사람용 문서가 아니라 Retrieval 최적화 문서

Output Evaluation:
- Required Section 존재 여부 확인
- FAQ 형식 확인
- Retrieval Queries 존재 여부 확인
- 장문 에세이형 설명 여부 확인
- 용어 통일 여부 확인
- Domain Rules 반영 여부 확인
```

실무 평가 Matrix:

| Output Type         | 주요 평가 기준                                          |
| ------------------- | ------------------------------------------------------- |
| RAG 문서            | Required Section, Chunk Quality, FAQ, Retrieval Queries |
| Backend Code        | Compile 가능성, 프로젝트 규칙, 예외 처리, 테스트 가능성 |
| Frontend Code       | API 연동, 상태 처리, UX 흐름, 오류 처리                 |
| Review Report       | Finding 정확도, Evidence, Severity, Fix Recommendation  |
| Tool Result Summary | Tool 성공 여부, 결과 검증, Side Effect                  |
| Final Answer        | 요구사항 충족, 근거, 형식, 실행 가능성                  |

---

### [주의]

Output Evaluation 주의사항:

- 설명이 길어도 요구사항을 누락할 수 있다.
- 형식이 맞아도 내용이 틀릴 수 있다.
- 일부 정확한 내용이 있어도 핵심 요구사항을 놓치면 Fail이다.
- 일반 지식과 프로젝트 고유 사실을 구분해야 한다.
- 문서에 없는 프로젝트 파일명, API, 클래스명은 Unsupported Claim이다.
- 불확실한 내용을 확정적으로 말하면 안 된다.
- Tool 실패 결과를 성공처럼 요약하면 안 된다.

---

### [Best Practice]

Output Evaluation Best Practice:

- 사용자 요구사항을 먼저 구조화한다.
- Must Requirement와 Optional Requirement를 구분한다.
- 출력 결과를 요구사항별로 대조한다.
- 핵심 Claim마다 Evidence를 확인한다.
- Unsupported Claim은 명시적으로 표시한다.
- 형식 검증과 내용 검증을 분리한다.
- Safety 위반은 높은 Severity로 처리한다.
- Fix Recommendation은 구체적으로 작성한다.
- 평가 결과는 Pass / Fix / Stop으로 명확히 구분한다.

---

### [FAQ]

Q. Output Evaluation이 뭐야?
A. Agent가 만든 결과가 사용자 요청, 요구사항, 근거, 형식, 안전 기준을 만족하는지 평가하는 과정이다.

Q. Output Evaluation은 최종 답변만 보면 돼?
A. 아니다. 중간 산출물, 코드, Tool 결과, Review 결과도 평가 대상이다.

Q. Output Evaluation에서 가장 먼저 확인할 것은 뭐야?
A. 사용자 요구사항과 Agent Output이 일치하는지 확인하는 Task Match다.

Q. 출력 형식이 맞으면 Pass야?
A. 아니다. Format Compliance는 일부 기준일 뿐이고 내용 정확성, 근거, 안전성도 확인해야 한다.

Q. Agent 답변이 길면 Completeness가 높은 거야?
A. 아니다. 필요한 요구사항을 빠뜨렸다면 길어도 Completeness가 낮다.

Q. Unsupported Claim은 어떻게 처리해?
A. 근거 없는 주장을 표시하고 제거하거나 Evidence 기반으로 수정해야 한다.

---

# 2. Requirement Compliance

## 2.1 User Requirement Evaluation

### [개념]

Requirement Compliance는 Agent Output이 사용자의 요구사항과 제약 조건을 지켰는지 평가하는 기준이다.

Requirement Compliance는 Output Evaluation의 첫 번째 핵심 기준이다.

사용자 요구사항은 다음으로 나눈다.

- Must Requirement
- Must Not Requirement
- Constraint
- Preference
- Output Format
- Acceptance Criteria

---

### [핵심]

Requirement Compliance 검증 대상:

| 구분                 | 의미                    |
| -------------------- | ----------------------- |
| User Request         | 사용자가 요청한 작업    |
| Must Requirement     | 반드시 지켜야 하는 조건 |
| Must Not Requirement | 반드시 피해야 하는 조건 |
| Constraint           | 기술, 형식, 범위 제약   |
| Preference           | 선호사항                |
| Acceptance Criteria  | 완료 판단 기준          |

Requirement Compliance Flow:

```text
User Request
→ Extract Requirements
→ Classify Must / Must Not / Constraint / Preference
→ Compare Output
→ Mark Pass / Missing / Violation
```

요구사항 우선순위:

```text
1. Safety / Policy Constraint
2. Must Not Requirement
3. Must Requirement
4. Output Format
5. Acceptance Criteria
6. Preference
```

평가 결과:

```text
Pass:
- 필수 요구사항 충족
- 금지 조건 위반 없음
- 출력 형식 준수

Fix:
- 일부 요구사항 누락
- 선호사항 미반영
- 형식 일부 위반

Fail / Stop:
- 금지 조건 위반
- 핵심 요구사항 누락
- 위험 작업 승인 누락
```

---

### [실무]

실무에서는 Requirement Compliance를 명시 요구사항 기준으로 먼저 평가한다.

예시 1:

```text
User Requirement:
- Java 21 기준
- Spring Boot 3.x 기준
- ApiResponse<T> 직접 반환
- 예외는 GlobalExceptionHandler 처리

Evaluation:
- Java 21 호환 여부
- Spring Boot 3.x 호환 여부
- ResponseEntity 사용 여부
- Controller 내부 예외 처리 중복 여부
```

예시 2:

```text
User Requirement:
- RAG 문서 제작 전용
- MASTER_RAG_RULES 적용
- DOMAIN_RULES 적용
- PROJECT_PROGRESS 참고
- [FAQ] 강화
- Retrieval Queries 포함
- 중간 응답 금지
- 결과만 출력

Evaluation:
- RAG 문서 구조 준수 여부
- Required Section 포함 여부
- FAQ Q/A 완성 여부
- Retrieval Queries 존재 여부
- 중간 설명 출력 여부
```

Requirement Evaluation Table:

| Requirement            | Output Evidence                    | Result | Fix  |
| ---------------------- | ---------------------------------- | ------ | ---- |
| Required Section 포함  | [개념], [핵심], [실무], [FAQ] 존재 | Pass   | 없음 |
| FAQ 강화               | FAQ 다수 포함                      | Pass   | 없음 |
| Retrieval Queries 포함 | 문서 마지막 포함                   | Pass   | 없음 |
| 중간 응답 금지         | 최종 결과만 출력                   | Pass   | 없음 |

---

### [주의]

Requirement Compliance 주의사항:

- 사용자 요구를 임의로 바꾸지 않는다.
- 선호사항과 필수사항을 구분한다.
- 금지 조건 위반은 높은 Severity로 처리한다.
- 명시 요구사항을 누락하면 전체 품질이 낮아진다.
- 요구사항 간 충돌이 있으면 우선순위를 판단해야 한다.
- 불명확한 요구사항은 확정하지 않고 Assumption으로 표시한다.
- 현재 요청은 오래된 Memory보다 우선한다.

---

### [Best Practice]

Requirement Compliance Best Practice:

- 사용자 요청에서 요구사항을 먼저 추출한다.
- Must / Must Not / Constraint / Preference로 분류한다.
- Output을 요구사항 단위로 평가한다.
- 누락된 요구사항은 Missing Requirement로 표시한다.
- 금지 조건 위반은 Violation으로 표시한다.
- Acceptance Criteria가 있으면 Pass / Fail 기준으로 사용한다.
- 충돌 요구사항은 사용자 요청의 최신 지시를 우선한다.

---

### [FAQ]

Q. Requirement Compliance가 뭐야?
A. Agent Output이 사용자 요구사항과 금지 조건을 지켰는지 확인하는 평가 기준이다.

Q. 왜 Requirement Compliance를 먼저 봐야 해?
A. 사용자가 요청한 조건을 지키지 않으면 내용이 좋아도 작업 성공으로 볼 수 없기 때문이다.

Q. Must Requirement는 뭐야?
A. 반드시 반영해야 하는 사용자 요구사항이다.

Q. Must Not Requirement는 뭐야?
A. 반드시 피해야 하는 금지 조건이다.

Q. Preference와 Requirement는 어떻게 달라?
A. Requirement는 반드시 지켜야 하고 Preference는 가능하면 반영하는 선호사항이다.

Q. 요구사항이 충돌하면 어떻게 해?
A. 안전 기준과 최신 사용자 지시를 우선하고, 필요하면 Assumption 또는 Conflict로 표시한다.

---

# 3. Correctness Evaluation

## 3.1 Correctness

### [개념]

Correctness는 Agent Output의 내용이 사실, 코드, 논리, 요구사항 기준으로 맞는지 평가하는 기준이다.

Correctness는 단순히 자연스러운 문장인지 보는 것이 아니다.

평가 대상:

- 사실 정확성
- 코드 문법 정확성
- 논리 정확성
- 계산 정확성
- API / 클래스 / 메서드 정확성
- 프로젝트 규칙 정확성
- 버전 호환성

---

### [핵심]

Correctness 검증 항목:

| 항목                    | 검증 내용                    |
| ----------------------- | ---------------------------- |
| Factual Correctness     | 사실이 맞는가                |
| Logical Correctness     | 논리 전개가 맞는가           |
| Code Correctness        | 코드가 문법적으로 맞는가     |
| Project Correctness     | 프로젝트 구조와 맞는가       |
| Version Correctness     | 기술 버전과 맞는가           |
| Calculation Correctness | 계산이 맞는가                |
| Dependency Correctness  | 라이브러리 / 의존성이 맞는가 |

Correctness Evaluation Flow:

```text
Agent Claim
→ Check Fact / Logic / Code / Version
→ Compare with Context or Known Rule
→ Correct / Incorrect / Unknown
```

Correctness 결과:

```text
Correct:
- 사실, 코드, 논리, 버전이 맞음

Incorrect:
- 명확한 오류 있음

Unknown:
- 제공된 Context만으로 검증 불가
```

---

### [실무]

실무에서는 작업 유형별 Correctness 기준을 다르게 적용한다.

Backend Code Correctness:

```text
- Java 문법이 맞는가?
- Spring Boot 3.x에서 사용 가능한가?
- Entity / DTO / Repository 이름이 실제 존재하는가?
- Transaction Boundary가 적절한가?
- 예외 처리 구조가 프로젝트 규칙과 맞는가?
- Query Method 이름이 Entity 필드와 일치하는가?
```

RAG Document Correctness:

```text
- Domain Rules와 충돌하지 않는가?
- 용어가 일관되는가?
- 개념 설명이 정확한가?
- FAQ 답변이 핵심 질문과 일치하는가?
- Retrieval Queries가 문서 내용과 연결되는가?
```

Tool Result Correctness:

```text
- Tool 실행 결과를 정확히 해석했는가?
- 실패 메시지를 성공으로 잘못 해석하지 않았는가?
- 결과 데이터의 범위와 한계를 표시했는가?
- 실행 결과가 사용자 요청과 연결되는가?
```

Correctness Report 예시:

```md
### Correctness Check

| Claim                                 | Result    | Evidence             | Fix  |
| ------------------------------------- | --------- | -------------------- | ---- |
| Controller는 ApiResponse<T> 직접 반환 | Correct   | 프로젝트 규칙과 일치 | 없음 |
| ResponseEntity 필수 사용              | Incorrect | 사용자 규칙과 충돌   | 제거 |
```

---

### [주의]

Correctness 주의사항:

- 그럴듯한 코드도 컴파일되지 않을 수 있다.
- 일반적으로 맞는 설명이 프로젝트 규칙과 다를 수 있다.
- 버전이 다르면 올바른 코드도 실패할 수 있다.
- 일부 Claim이 맞아도 핵심 Claim이 틀리면 Output 품질이 낮다.
- Context로 검증 불가능한 내용은 Unknown 또는 Assumption으로 표시해야 한다.
- 존재하지 않는 클래스 / 메서드 / 파일을 생성하면 Hallucination이다.

---

### [Best Practice]

Correctness Best Practice:

- Claim 단위로 검증한다.
- 프로젝트 고유 정보는 제공된 Context 기준으로만 확정한다.
- 코드 Correctness는 문법, 컴파일, 런타임 위험을 분리해서 본다.
- 버전 호환성을 명시한다.
- 검증 불가한 내용은 확정하지 않는다.
- Incorrect Claim은 Fix Recommendation과 함께 표시한다.
- Correctness와 Preference를 혼동하지 않는다.

---

### [FAQ]

Q. Correctness는 뭐야?
A. Agent Output의 사실, 코드, 논리, 버전, 프로젝트 규칙이 맞는지 평가하는 기준이다.

Q. 자연스럽게 보이는 답변이면 Correctness가 높은 거야?
A. 아니다. 자연스러워도 사실이나 코드가 틀릴 수 있다.

Q. 코드 Correctness는 어떻게 확인해?
A. 문법, 컴파일 가능성, 프로젝트 구조, 버전 호환성, 런타임 위험을 확인한다.

Q. 프로젝트 고유 정보는 어떻게 검증해?
A. 제공된 코드, RAG 문서, Retrieved Context에 근거가 있는지 확인한다.

Q. 검증할 수 없는 내용은 어떻게 처리해?
A. Unknown 또는 Assumption으로 표시하고 확정적으로 말하지 않는다.

---

# 4. Completeness Evaluation

## 4.1 Completeness

### [개념]

Completeness는 Agent Output이 사용자 요청을 해결하는 데 필요한 내용을 충분히 포함했는지 평가하는 기준이다.

Completeness는 길이와 같지 않다.

필요한 내용을 빠뜨리지 않고, 불필요하게 범위를 확장하지 않는 것이 중요하다.

---

### [핵심]

Completeness 검증 항목:

| 항목               | 검증 내용                          |
| ------------------ | ---------------------------------- |
| Required Coverage  | 필수 요구사항을 모두 다뤘는가      |
| Step Coverage      | 필요한 절차를 빠뜨리지 않았는가    |
| Edge Case Coverage | 주요 예외 상황을 다뤘는가          |
| Context Coverage   | 제공된 Context를 충분히 반영했는가 |
| Output Coverage    | 요구한 결과물을 완성했는가         |
| Scope Control      | 불필요한 범위 확장을 하지 않았는가 |

Completeness Evaluation Flow:

```text
User Requirement List
→ Output Section Mapping
→ Missing Requirement Check
→ Missing Context Check
→ Complete / Incomplete
```

Completeness 판단:

```text
Complete:
- 필수 요구사항 모두 포함
- 필요한 절차 포함
- 결과물이 사용 가능

Incomplete:
- 핵심 요구사항 누락
- 필요한 조건 누락
- 결과물이 바로 사용 불가

Overextended:
- 요청 범위를 과도하게 확장
- 불필요한 내용이 핵심 Retrieval을 방해
```

---

### [실무]

실무에서는 Completeness를 요구사항 목록과 Output 섹션 매핑으로 평가한다.

예시:

```text
User Request:
Agent Evaluation & Guardrails Part 문서 작성

Required:
- [개념]
- [핵심]
- [실무]
- [FAQ]
- Retrieval Queries
- RAG Retrieval 최적화
- 용어 통일

Completeness Check:
- 모든 Required Section 포함 여부
- FAQ Q/A 포함 여부
- Retrieval Queries 포함 여부
- Domain Rule 키워드 반영 여부
```

Completeness Matrix:

| Requirement       | Output Section    | Result |
| ----------------- | ----------------- | ------ |
| [개념] 포함       | 각 Section        | Pass   |
| [핵심] 포함       | 각 Section        | Pass   |
| [실무] 포함       | 각 Section        | Pass   |
| [FAQ] 포함        | 각 Section        | Pass   |
| Retrieval Queries | 문서 마지막       | Pass   |
| RAG 최적화        | 키워드 반복 / Q&A | Pass   |

Backend Output Completeness 예시:

```text
요청:
Service 코드 검토

Complete Output:
- 트랜잭션 검토
- 예외 처리 검토
- Repository 호출 검토
- DTO 변환 검토
- N+1 위험 검토
- 테스트 가능성 검토
- 수정 제안 포함
```

---

### [주의]

Completeness 주의사항:

- 긴 답변이 Complete를 의미하지 않는다.
- 요구하지 않은 내용을 많이 추가하면 Retrieval 품질이 낮아질 수 있다.
- 핵심 조건 하나를 누락하면 Incomplete가 될 수 있다.
- 과도한 일반론은 실무 적용성을 낮춘다.
- Output이 사용 가능한 형태인지 확인해야 한다.
- 누락된 정보가 있으면 Missing Information으로 표시해야 한다.

---

### [Best Practice]

Completeness Best Practice:

- 요구사항 목록을 먼저 만든다.
- Output 섹션을 요구사항에 매핑한다.
- 누락된 항목은 Missing Requirement로 표시한다.
- 필요한 Edge Case만 포함한다.
- 불필요한 배경 설명은 줄인다.
- 결과물이 바로 사용 가능한지 확인한다.
- RAG 문서는 Retrieval 키워드와 FAQ를 충분히 포함한다.

---

### [FAQ]

Q. Completeness는 뭐야?
A. Agent Output이 사용자 요청을 해결하는 데 필요한 내용을 충분히 포함했는지 평가하는 기준이다.

Q. 답변이 길면 Completeness가 높은 거야?
A. 아니다. 필요한 요구사항을 빠뜨리면 길어도 Incomplete다.

Q. Completeness는 어떻게 확인해?
A. 사용자 요구사항 목록과 Output 섹션을 매핑해서 누락 여부를 확인한다.

Q. 너무 많은 내용을 넣어도 문제야?
A. 문제다. 불필요한 범위 확장은 핵심 Retrieval과 사용성을 떨어뜨릴 수 있다.

Q. 누락된 정보가 있으면 어떻게 해?
A. Missing Requirement 또는 Missing Information으로 표시하고 Fix 방향을 제안한다.

---

# 5. Relevance Evaluation

## 5.1 Relevance

### [개념]

Relevance는 Agent Output이 사용자 질문과 작업 목적에 직접 관련되는지 평가하는 기준이다.

Relevance는 Retrieval 품질과 Agent 답변 품질 모두에 중요하다.

관련 없는 설명이 많으면 Output은 길어져도 품질이 낮아진다.

---

### [핵심]

Relevance 검증 항목:

| 항목              | 검증 내용                            |
| ----------------- | ------------------------------------ |
| Query Match       | 사용자 질문과 직접 관련되는가        |
| Task Focus        | 작업 목적에서 벗어나지 않는가        |
| Domain Match      | 해당 Domain Rules와 일치하는가       |
| Context Match     | 제공된 Context와 연결되는가          |
| Noise Control     | 불필요한 설명이 적은가               |
| Retrieval Utility | 검색될 때 유용한 키워드를 포함하는가 |

Relevance Evaluation Flow:

```text
User Query
→ Identify Intent
→ Compare Output Topic
→ Remove Off-topic Content
→ Improve Retrieval Keywords
```

Relevance 판단:

```text
High Relevance:
- 질문과 직접 연결
- Domain Rule과 일치
- 검색 키워드 명확
- 불필요한 설명 적음

Low Relevance:
- 질문과 무관한 일반론 많음
- Domain 범위 이탈
- 핵심 질문에 답하지 않음
- Retrieval Noise 많음
```

---

### [실무]

실무에서는 Relevance를 RAG Retrieval 최적화 관점에서도 평가한다.

RAG 문서 Relevance 기준:

```text
- 문서 제목과 Section 제목이 검색 의도와 맞는가?
- FAQ가 실제 사용자 질문 표현을 포함하는가?
- 핵심 키워드가 반복되는가?
- 불필요한 장문 서론이 없는가?
- 한 Chunk에 여러 개념이 섞이지 않았는가?
```

Agent Output Relevance 예시:

```text
User Request:
Spring Boot Controller 응답 구조 검토

Relevant Output:
- ApiResponse<T>
- ResponseEntity 사용 여부
- GlobalExceptionHandler
- Controller 책임
- HTTP Status 처리

Irrelevant Output:
- Spring 역사
- MVC 이론 장문 설명
- 프론트엔드 상태관리 일반론
```

Relevance 개선 방법:

```text
- 질문 키워드와 Output 제목 일치
- FAQ에 실제 질문 표현 추가
- Domain 용어 통일
- Off-topic 문단 제거
- Chunk당 하나의 개념 유지
```

---

### [주의]

Relevance 주의사항:

- 일반적으로 유익한 설명도 현재 질문과 무관하면 Noise다.
- RAG 문서에서는 Noise가 Retrieval 성능을 떨어뜨린다.
- 여러 개념을 한 Chunk에 섞으면 검색 정확도가 낮아진다.
- 질문과 다른 Domain 설명을 추가하지 않는다.
- 최신 사용자 요청을 기준으로 Relevance를 판단한다.

---

### [Best Practice]

Relevance Best Practice:

- 사용자 Intent를 먼저 식별한다.
- Output 제목과 Section 제목에 핵심 키워드를 포함한다.
- FAQ에 실제 검색 질문을 넣는다.
- 장문 배경 설명을 줄인다.
- Domain Scope를 벗어나지 않는다.
- Retrieval에 도움 되는 키워드는 반복 허용한다.
- 관련 없는 예시는 제거한다.

---

### [FAQ]

Q. Relevance는 뭐야?
A. Agent Output이 사용자 질문과 작업 목적에 직접 관련되는지 평가하는 기준이다.

Q. Relevance가 낮으면 왜 문제야?
A. 질문에 답하지 못하고 Retrieval Noise가 늘어나 Agent 성능이 떨어진다.

Q. RAG 문서에서 Relevance는 왜 중요해?
A. 관련 없는 내용이 많으면 Semantic Search와 Chunk Retrieval 정확도가 낮아지기 때문이다.

Q. Relevance는 어떻게 높여?
A. 질문 키워드, Domain 용어, FAQ 표현, Section 제목을 검색 의도와 맞춘다.

Q. 좋은 설명도 관련 없으면 빼야 해?
A. 맞다. RAG 문서에서는 유익한 일반론보다 검색 목적에 맞는 정보가 우선이다.

---

# 6. Actionability Evaluation

## 6.1 Actionability

### [개념]

Actionability는 Agent Output이 사용자가 실제로 실행하거나 다음 단계로 활용할 수 있는 결과인지 평가하는 기준이다.

Actionability가 낮은 Output은 설명은 있어도 작업을 진행하기 어렵다.

---

### [핵심]

Actionability 검증 항목:

| 항목              | 검증 내용                        |
| ----------------- | -------------------------------- |
| Clear Next Step   | 다음 행동이 명확한가             |
| Executable Detail | 실행 가능한 수준의 정보가 있는가 |
| Specific Fix      | 수정 방향이 구체적인가           |
| Decision Support  | 판단 기준을 제공하는가           |
| Usable Format     | 바로 복사 / 적용 가능한 형식인가 |
| Risk Notice       | 실행 전 주의사항이 있는가        |

Actionability Evaluation Flow:

```text
Output
→ Check User Can Act
→ Check Missing Steps
→ Check Fix Specificity
→ Actionable / Not Actionable
```

Actionability 판단:

```text
High Actionability:
- 바로 실행 가능
- 수정 위치 명확
- 판단 기준 명확
- 위험 조건 표시

Low Actionability:
- 추상적 설명만 있음
- 다음 단계 불명확
- 수정 방향 없음
- 적용 조건 없음
```

---

### [실무]

실무에서는 Output 유형별 Actionability 기준을 다르게 적용한다.

Code Review Actionability:

```text
Low:
- 이 코드는 개선이 필요합니다.

High:
- UserService.createUser()에서 중복 이메일 검증이 누락됨.
- Repository.existsByEmail(email) 검증 추가 필요.
- 중복 시 DuplicateEmailException 발생.
- GlobalExceptionHandler에서 409 Conflict로 처리.
```

RAG Document Actionability:

```text
Low:
- FAQ를 추가하면 좋다.

High:
- Retrieval Queries에 실제 사용자 질문 표현을 10개 이상 추가한다.
- [FAQ] 답변은 1~4줄로 제한한다.
- Chunk마다 하나의 개념만 포함한다.
```

Tool Calling Actionability:

```text
Low:
- Tool 실행에 주의해야 한다.

High:
- 삭제 작업은 High Risk로 분류한다.
- 대상 파일 목록을 Preview로 표시한다.
- 사용자 승인 전 delete 실행 금지.
```

---

### [주의]

Actionability 주의사항:

- 추상적 조언은 Actionability가 낮다.
- 구체적이어도 근거가 없으면 위험하다.
- 실행 가능한 명령이 위험할 경우 Human Confirmation이 필요하다.
- 적용 위치와 조건이 없으면 사용자가 실행하기 어렵다.
- 코드 수정 제안은 프로젝트 구조와 맞아야 한다.

---

### [Best Practice]

Actionability Best Practice:

- 구체적인 수정 위치를 명시한다.
- 다음 단계가 바로 보이도록 작성한다.
- Fix Recommendation을 실행 가능한 형태로 제공한다.
- 적용 조건과 예외를 함께 표시한다.
- 위험 작업은 승인 필요 여부를 표시한다.
- 코드, 체크리스트, 표를 활용해 실행성을 높인다.
- 불확실한 내용은 Assumption으로 표시한다.

---

### [FAQ]

Q. Actionability는 뭐야?
A. Agent Output이 사용자가 실제로 실행하거나 다음 단계로 활용할 수 있는지 평가하는 기준이다.

Q. 설명이 자세하면 Actionability가 높은 거야?
A. 아니다. 실행 위치, 단계, 조건, 수정 방향이 명확해야 한다.

Q. Code Review에서 Actionability는 어떻게 높여?
A. 문제 위치, 원인, 수정 방법, 기대 결과를 구체적으로 제시한다.

Q. RAG 문서에서 Actionability는 왜 필요해?
A. Agent가 검색한 내용을 기반으로 코드 생성, 검토, 판단을 바로 수행할 수 있어야 하기 때문이다.

Q. 위험한 작업도 실행 가능하게 쓰면 좋은 거야?
A. 아니다. 위험 작업은 Human Confirmation과 Risk Notice를 포함해야 한다.

---

# 7. Output Evaluation Report

## 7.1 Evaluation Report Format

### [개념]

Output Evaluation Report는 Agent Output 평가 결과를 구조화해 기록하는 형식이다.

Evaluation Report는 Review Agent, PM Agent, Safety Agent가 Fix 여부와 다음 단계를 판단하는 데 사용한다.

---

### [핵심]

Evaluation Report 필수 요소:

- Evaluation Target
- User Requirement
- Evaluation Criteria
- Result
- Findings
- Severity
- Evidence
- Fix Recommendation
- Pass / Fix / Stop

기본 Format:

```md
# Output Evaluation Report

## Summary

- Target:
- Result:
- Decision:

## Requirement Compliance

| Requirement | Result | Evidence | Fix |
| ----------- | ------ | -------- | --- |

## Findings

| Severity | Issue | Evidence | Fix |
| -------- | ----- | -------- | --- |

## Final Decision

Pass / Fix / Stop
```

Severity 기준:

| Severity | 의미                                     | 처리               |
| -------- | ---------------------------------------- | ------------------ |
| Critical | 안전 문제, 핵심 요구 위반, 치명적 오류   | Stop 또는 즉시 Fix |
| Major    | 주요 요구사항 누락, 근거 부족, 기능 오류 | Fix                |
| Minor    | 표현, 구조, 작은 누락                    | 가능하면 Fix       |
| Info     | 참고 사항                                | 보고만 가능        |

---

### [실무]

실무에서는 Evaluation Report를 Agent Workflow의 Handoff 자료로 사용한다.

예시:

```md
# Output Evaluation Report

## Summary

- Target: Backend Agent Output
- Result: Fix Required
- Decision: Fix

## Requirement Compliance

| Requirement                 | Result | Evidence                     | Fix                               |
| --------------------------- | ------ | ---------------------------- | --------------------------------- |
| ApiResponse<T> 직접 반환    | Fail   | ResponseEntity 사용          | ApiResponse<T> 직접 반환으로 수정 |
| GlobalExceptionHandler 사용 | Pass   | Controller 내 try-catch 없음 | 없음                              |

## Findings

| Severity | Issue                                | Evidence                          | Fix                           |
| -------- | ------------------------------------ | --------------------------------- | ----------------------------- |
| Major    | 존재하지 않는 Repository 메서드 사용 | findByEmailAndActive() 근거 없음  | 실제 Repository 기준으로 수정 |
| Minor    | DTO 이름 불일치                      | UserResponseDto / UserResDto 혼용 | 용어 통일                     |

## Final Decision

Fix
```

Evaluation Report 사용 위치:

```text
Agent Output
→ Output Evaluation Report
→ Fix Agent
→ Re-evaluation
→ Final Output
```

---

### [주의]

Evaluation Report 주의사항:

- Evidence 없는 지적은 신뢰도가 낮다.
- Severity 기준이 없으면 Fix 우선순위가 흐려진다.
- 취향과 결함을 구분해야 한다.
- 모든 Finding이 Fix 대상은 아니다.
- Critical Finding은 반드시 해결하거나 Stop 처리한다.
- Report 자체도 Format Compliance를 지켜야 한다.

---

### [Best Practice]

Evaluation Report Best Practice:

- Summary에서 전체 판정을 먼저 제시한다.
- Requirement Compliance를 별도 표로 분리한다.
- Findings에는 Severity를 포함한다.
- Evidence는 실제 Output 또는 Context 기준으로 작성한다.
- Fix Recommendation은 구체적으로 작성한다.
- Pass / Fix / Stop을 명확히 표시한다.
- Minor Issue는 과도하게 Workflow를 막지 않는다.
- Critical Issue는 반드시 Stop 또는 Fix로 처리한다.

---

### [FAQ]

Q. Output Evaluation Report는 뭐야?
A. Agent Output 평가 결과를 구조화해 기록하는 리포트다.

Q. Evaluation Report에는 뭐가 들어가야 해?
A. 평가 대상, 요구사항, 평가 기준, 결과, Findings, Severity, Evidence, Fix Recommendation, Pass / Fix / Stop이 들어간다.

Q. Severity는 왜 필요해?
A. 문제의 우선순위를 정하고 Fix 여부를 판단하기 위해 필요하다.

Q. Evidence가 꼭 필요해?
A. 필요하다. Evidence가 없으면 Review Finding이 근거 없는 지적으로 보일 수 있다.

Q. 모든 Finding을 반드시 고쳐야 해?
A. 아니다. Critical과 Major는 우선 수정하고 Minor나 Info는 상황에 따라 처리한다.

---

# Retrieval Queries

### [FAQ]

Q. Output Evaluation이 뭐야?
A. Agent가 만든 결과가 사용자 요청, 요구사항, 근거, 형식, 안전 기준을 만족하는지 평가하는 과정이다.

Q. Agent Output은 무엇을 기준으로 평가해?
A. Task Match, Requirement Compliance, Correctness, Completeness, Groundedness, Format Compliance, Safety, Actionability 기준으로 평가한다.

Q. Output Evaluation Flow는 어떻게 돼?
A. User Requirement → Agent Output → Compare Requirement → Check Missing / Wrong / Unsupported / Unsafe Parts → Pass / Fix / Stop 순서다.

Q. Requirement Compliance는 뭐야?
A. Agent Output이 사용자 요구사항과 금지 조건을 지켰는지 확인하는 평가 기준이다.

Q. Must Requirement는 뭐야?
A. 반드시 반영해야 하는 사용자 요구사항이다.

Q. Must Not Requirement는 뭐야?
A. 반드시 피해야 하는 사용자 금지 조건이다.

Q. Requirement Compliance는 왜 먼저 평가해?
A. 사용자 요구사항을 지키지 않으면 내용이 좋아도 작업 성공으로 볼 수 없기 때문이다.

Q. Correctness는 뭐야?
A. Agent Output의 사실, 코드, 논리, 버전, 프로젝트 규칙이 맞는지 평가하는 기준이다.

Q. Code Correctness는 어떻게 확인해?
A. 문법, 컴파일 가능성, 프로젝트 구조, 버전 호환성, 런타임 위험을 확인한다.

Q. 검증할 수 없는 내용은 어떻게 처리해?
A. Unknown 또는 Assumption으로 표시하고 확정적으로 말하지 않는다.

Q. Completeness는 뭐야?
A. Agent Output이 사용자 요청을 해결하는 데 필요한 내용을 충분히 포함했는지 평가하는 기준이다.

Q. 답변이 길면 Completeness가 높은 거야?
A. 아니다. 필수 요구사항을 빠뜨리면 길어도 Incomplete다.

Q. Completeness는 어떻게 검증해?
A. 사용자 요구사항 목록과 Output 섹션을 매핑해서 누락 여부를 확인한다.

Q. Relevance는 뭐야?
A. Agent Output이 사용자 질문과 작업 목적에 직접 관련되는지 평가하는 기준이다.

Q. RAG 문서에서 Relevance가 중요한 이유는?
A. 관련 없는 내용은 Retrieval Noise를 늘리고 Semantic Search 정확도를 떨어뜨리기 때문이다.

Q. Actionability는 뭐야?
A. Agent Output이 사용자가 실제로 실행하거나 다음 단계로 활용할 수 있는지 평가하는 기준이다.

Q. Actionability를 높이려면 어떻게 해?
A. 수정 위치, 실행 단계, 적용 조건, Fix Recommendation을 구체적으로 작성한다.

Q. Output Evaluation Report는 뭐야?
A. Agent Output 평가 결과를 구조화해 기록하는 리포트다.

Q. Evaluation Report에는 뭐가 들어가?
A. Evaluation Target, User Requirement, Evaluation Criteria, Result, Findings, Severity, Evidence, Fix Recommendation, Pass / Fix / Stop이 들어간다.

Q. Severity는 왜 필요해?
A. 문제의 우선순위를 정하고 Fix 또는 Stop 여부를 판단하기 위해 필요하다.

Q. Evidence 없는 Review Finding은 괜찮아?
A. 좋지 않다. Evidence가 없으면 근거 없는 지적이 되어 Review 신뢰도가 낮아진다.

Q. Output Evaluation 결과는 어떻게 나눠?
A. Pass, Fix, Stop으로 나눈다. 통과 가능하면 Pass, 수정 필요하면 Fix, 진행 불가하면 Stop이다.

Q. 출력 형식만 맞으면 Pass야?
A. 아니다. Format Compliance는 일부 기준이고 Correctness, Completeness, Groundedness, Safety도 평가해야 한다.

Q. Agent Output에서 Unsupported Claim이 있으면 어떻게 해?
A. 근거 없는 주장을 제거하거나 Evidence 기반으로 수정하고, 검증 불가하면 Assumption으로 표시한다.
