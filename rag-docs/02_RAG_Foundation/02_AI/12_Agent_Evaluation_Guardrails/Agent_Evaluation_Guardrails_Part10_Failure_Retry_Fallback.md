# Agent Evaluation & Guardrails Part10 - Failure, Retry & Fallback

---

# 1. Failure Classification

## 1.1 Failure Classification Core

### [개념]

Failure Classification은 Agent가 실패했을 때 실패 원인을 유형별로 분류하는 기준이다.

Failure Classification의 목적은 실패를 막연히 “오류”로 처리하지 않고, 다음 행동을 결정할 수 있게 만드는 것이다.

Failure Classification은 Troubleshooting 전체를 자세히 설명하는 문서가 아니다.

이 문서의 초점은 **실패 유형 분류, Retry 가능 여부, Fallback 전환, Stop 판단**이다.

Agent 실패는 다음 영역에서 발생할 수 있다.

- Requirement
- Retrieval
- Grounding
- Format
- Code
- Tool
- Safety
- Memory
- Workflow
- Review

---

### [핵심]

주요 Failure 유형:

| Failure Type         | 의미                                | 기본 처리               |
| -------------------- | ----------------------------------- | ----------------------- |
| Requirement Failure  | 사용자 요구사항 누락 / 위반         | Fix                     |
| Retrieval Failure    | 필요한 문서 검색 실패               | Retry Query / Fallback  |
| Grounding Failure    | 근거 없는 답변 생성                 | Fix / Stop              |
| Faithfulness Failure | Context 왜곡 / 과장                 | Fix                     |
| Format Failure       | 출력 형식 위반                      | Retry / Fix             |
| Code Failure         | 코드 문법 / 프로젝트 규칙 오류      | Fix                     |
| Tool Failure         | Tool 선택 / 인자 / 실행 실패        | Retry / Fallback / Stop |
| Safety Failure       | 위험 작업 / 승인 누락 / Secret 노출 | Stop / Block            |
| Memory Failure       | 오래된 Memory / 충돌 Memory 사용    | Fix                     |
| Workflow Failure     | Routing / Handoff / State 문제      | Fix / Stop              |
| Review Failure       | False Positive / False Negative     | Review Fix              |

Failure Classification Flow:

```text
Failure Detected
→ Identify Failure Type
→ Check Severity
→ Check Retryable
→ Check Fallback
→ Fix / Retry / Fallback / Stop
```

Failure 처리 방향:

```text
Fix:
- 요구사항 누락
- 형식 오류
- 일부 Grounding 문제
- 코드 수정 가능

Retry:
- Timeout
- Rate Limit
- 일시적 Tool 오류
- Query 부정확
- Format 재생성 가능

Fallback:
- Retry 반복 실패
- Retrieval 부족
- Tool 권한 없음
- 대체 방법 필요

Stop:
- Safety Failure
- High Risk 승인 없음
- 핵심 정보 부족
- Tool 실패 후 대안 없음

Block:
- Secret 전체 출력
- 악성 행위
- 안전상 허용 불가 작업
```

---

### [실무]

개인 AI 개발팀 구조에서는 여러 Agent가 순차적으로 작업한다.

따라서 실패 유형을 명확히 분류하지 않으면 다음 Agent가 잘못된 복구 전략을 선택할 수 있다.

실무 적용 순서:

```text
1. 실패 증상 확인
2. 실패 발생 위치 확인
3. Failure Type 분류
4. Severity 판단
5. Retry 가능 여부 판단
6. Fallback 가능 여부 판단
7. Final Handling 결정
```

예시:

```text
Problem:
Agent가 문서에 없는 Repository 메서드를 제안함.

Failure Type:
- Grounding Failure
- Code Hallucination

Handling:
- Unsupported Claim 제거
- 실제 Repository Context 기준으로 수정
```

예시:

```text
Problem:
파일 검색 Tool이 Timeout 발생.

Failure Type:
- Tool Failure
- Timeout

Handling:
- 제한적 Retry
- 반복 실패 시 범위 축소 또는 Fallback
```

예시:

```text
Problem:
사용자 승인 없이 DB DELETE 실행 시도.

Failure Type:
- Safety Failure
- Human Confirmation Failure

Handling:
- Stop
- Action Preview 작성
- 사용자 승인 전 실행 금지
```

Failure Report 예시:

```md
| Failure Type        | Evidence                    | Severity | Handling             |
| ------------------- | --------------------------- | -------- | -------------------- |
| Requirement Failure | Retrieval Queries 누락      | Major    | Fix                  |
| Grounding Failure   | 문서에 없는 API 생성        | Major    | Fix                  |
| Tool Failure        | Search Timeout              | Major    | Retry with Limit     |
| Safety Failure      | DB DELETE 승인 없음         | Critical | Stop                 |
| Memory Failure      | 오래된 Open WebUI 상태 사용 | Major    | Current Context 우선 |
```

---

### [주의]

Failure Classification 주의사항:

- 실패를 성공처럼 포장하지 않는다.
- 하나의 실패가 여러 Failure Type에 걸칠 수 있다.
- Retrieval Failure와 Grounding Failure를 구분한다.
- Tool Failure와 Tool Result 해석 실패를 구분한다.
- Safety Failure는 Retry보다 Stop / Block이 우선이다.
- 반복 실패는 Retry보다 Fallback 또는 Stop이 적절할 수 있다.
- Review Agent의 실패도 평가 대상이다.

---

### [Best Practice]

Failure Classification Best Practice:

- Failure Type을 명시적으로 기록한다.
- Severity와 Evidence를 함께 기록한다.
- Retryable / Non-Retryable을 구분한다.
- Safety Failure는 즉시 Stop 또는 Block 처리한다.
- Grounding Failure는 Unsupported Claim 제거로 처리한다.
- Format Failure는 Schema 단순화 또는 재생성으로 처리한다.
- Tool Failure는 Tool Result를 Evidence로 사용한다.
- 반복 Failure는 Workflow 개선 대상으로 기록한다.

---

### [FAQ]

Q. Failure Classification이 뭐야?
A. Agent 실패 원인을 유형별로 분류해 Fix, Retry, Fallback, Stop 중 적절한 처리를 선택하는 기준이다.

Q. Failure Classification은 왜 필요해?
A. 실패 원인을 알아야 같은 실패를 반복하지 않고 올바른 복구 전략을 선택할 수 있기 때문이다.

Q. Requirement Failure는 뭐야?
A. 사용자 요구사항을 누락하거나 금지 조건을 위반한 실패다.

Q. Grounding Failure는 뭐야?
A. Retrieved Context나 제공 문서에 근거하지 않은 답변을 생성한 실패다.

Q. Tool Failure는 뭐야?
A. Tool 선택, 인자, 실행, 결과 처리에서 발생한 실패다.

Q. Safety Failure는 어떻게 처리해?
A. Retry하지 말고 Stop 또는 Block으로 처리해야 한다.

---

# 2. Retry Rules

## 2.1 Retry Core

### [개념]

Retry는 실패한 작업을 제한된 횟수 안에서 다시 시도하는 복구 전략이다.

Retry는 모든 실패에 적용하면 안 된다.

Retry는 일시적 오류, 검색 Query 문제, 수정 가능한 Format 오류처럼 다시 시도할 의미가 있는 경우에만 사용한다.

Retry에는 반드시 Retry Limit이 있어야 한다.

---

### [핵심]

Retry 가능 상황:

| Failure             | Retry 가능성 | 처리                   |
| ------------------- | ------------ | ---------------------- |
| Timeout             | 가능         | 제한적 Retry           |
| Rate Limit          | 가능         | 빈도 조절 후 Retry     |
| Network Error       | 가능         | 제한적 Retry           |
| Temporary API Error | 가능         | 제한적 Retry           |
| Format Failure      | 가능         | Schema 기준 재생성     |
| Search Miss         | 가능         | Query 변형             |
| Argument Error      | 수정 후 가능 | Arguments Fix 후 Retry |

Retry 부적합 상황:

| Failure                      | 이유                   | 처리            |
| ---------------------------- | ---------------------- | --------------- |
| Safety Failure               | 위험 반복 가능         | Stop / Block    |
| Permission Error             | 권한 없이 해결 불가    | Ask / Stop      |
| Human Confirmation Required  | 승인 전 실행 불가      | Stop            |
| Secret Exposure              | 차단 필요              | Block           |
| Missing Critical Information | 정보 없이 Retry 무의미 | Ask / Stop      |
| Unsupported Core Claim       | 근거 재확보 필요       | Fallback / Stop |

Retry Flow:

```text
Failure
→ Is Retryable?
→ Fix Input if Needed
→ Retry with Limit
→ Success / Fail
→ Fallback or Stop
```

Retry Limit 기준:

```text
Tool Timeout:
- 1~2회

Format Regeneration:
- 1~2회

Search Query Variation:
- 2~3회

High Risk Action:
- 승인 전 Retry 금지
```

---

### [실무]

Retry는 같은 입력을 반복하는 것이 아니다.

실패 원인을 반영해 입력, Query, Prompt, Arguments를 바꿔야 한다.

나쁜 Retry 예시:

```text
JSON 파싱 실패
→ 같은 Prompt로 계속 재생성
→ 계속 실패
```

좋은 Retry 예시:

```text
JSON 파싱 실패
→ 실패 원인 확인
→ Schema 단순화
→ 순수 JSON만 출력하도록 재시도
→ Retry Limit 적용
```

검색 Retry 예시:

```text
Retrieval Failure:
- Query가 너무 좁음

Retry:
- 핵심 키워드로 Query 확장
- 한국어 / 영어 용어 병행
- Domain Rule 문서 우선 검색
```

Tool Retry 예시:

```text
Tool Failure:
- Timeout

Retry:
- 범위 축소
- max_results 감소
- 1회 재시도
- 실패 반복 시 Fallback
```

Retry Report 예시:

```md
| Failure           | Retryable | Retry Strategy   | Limit | Next         |
| ----------------- | --------- | ---------------- | ----- | ------------ |
| JSON Format Error | Yes       | Schema 단순화    | 2     | Fallback     |
| Search Miss       | Yes       | Query 변형       | 3     | Missing 표시 |
| Permission Error  | No        | 사용자 승인 필요 | 0     | Stop         |
| Safety Failure    | No        | 실행 차단        | 0     | Block        |
```

---

### [주의]

Retry 주의사항:

- 무제한 Retry는 금지한다.
- 같은 입력으로 반복 실패하면 입력이나 전략을 바꿔야 한다.
- 위험 작업 Retry는 중복 실행 위험이 있다.
- Non-idempotent 작업은 Retry하면 중복 생성, 중복 발송, 중복 결제가 발생할 수 있다.
- Permission Error는 단순 Retry로 해결되지 않을 수 있다.
- Safety Failure는 Retry 대상이 아니다.
- Retry 실패 후 성공처럼 답변하면 안 된다.

---

### [Best Practice]

Retry Best Practice:

- Retry 전에 Failure Type을 분류한다.
- Retryable Failure만 재시도한다.
- Retry Limit을 명시한다.
- 같은 실패가 반복되면 Fallback으로 전환한다.
- Retry 전 Prompt, Query, Arguments를 수정한다.
- Tool Retry는 Side Effect와 Idempotency를 확인한다.
- High Risk Tool은 승인 없이 Retry하지 않는다.
- Retry 결과를 Evaluation Report에 기록한다.

---

### [FAQ]

Q. Retry가 뭐야?
A. 실패한 작업을 제한된 횟수 안에서 다시 시도하는 복구 전략이다.

Q. 모든 실패는 Retry하면 돼?
A. 아니다. Retry는 일시적 오류나 수정 가능한 오류에만 제한적으로 사용해야 한다.

Q. Retry Limit은 왜 필요해?
A. 무한 반복과 중복 실행 위험을 막기 위해 필요하다.

Q. Safety Failure도 Retry해도 돼?
A. 안 된다. Safety Failure는 Stop 또는 Block 대상이다.

Q. 같은 Prompt로 계속 Retry해도 돼?
A. 안 된다. 같은 실패가 반복되면 Prompt, Query, Arguments를 수정해야 한다.

Q. Non-idempotent 작업은 왜 Retry가 위험해?
A. 중복 생성, 중복 발송, 중복 결제처럼 되돌리기 어려운 문제가 발생할 수 있기 때문이다.

---

# 3. Fallback Rules

## 3.1 Fallback Core

### [개념]

Fallback은 기존 방식이 실패하거나 사용할 수 없을 때 다른 안전한 방식으로 전환하는 복구 전략이다.

Fallback은 Retry와 다르다.

Retry는 같은 작업을 제한적으로 다시 시도하는 것이다.

Fallback은 다른 방법, 다른 Tool, 축소된 범위, Partial Answer, 사용자 확인으로 전환하는 것이다.

---

### [핵심]

Fallback 필요 상황:

| 상황                | Fallback 예시                       |
| ------------------- | ----------------------------------- |
| Retrieval 결과 부족 | Partial Answer, Missing Information |
| Tool 권한 없음      | 사용자에게 파일 요청                |
| Tool 실패 반복      | 수동 확인 안내, 범위 축소           |
| Format 반복 실패    | Schema 단순화                       |
| Code Context 부족   | 일반 기준만 제공                    |
| 위험 작업 승인 없음 | Action Preview 후 Stop              |
| Memory 충돌         | 현재 문서 기준 사용                 |
| API 사용 불가       | 대체 데이터 소스 사용               |

Fallback Flow:

```text
Failure
→ Retryable?
→ Retry Limit Reached?
→ Check Alternative
→ Fallback Method
→ Partial / Ask / Stop
```

Fallback 결과:

| 결과             | 의미                                |
| ---------------- | ----------------------------------- |
| Partial Answer   | 제공된 Context 범위 안에서 답변     |
| Ask              | 사용자 확인 또는 추가 정보 필요     |
| Alternative Tool | 더 안전하거나 접근 가능한 Tool 사용 |
| Manual Step      | 자동 실행 불가 시 수동 절차 제공    |
| Stop             | 안전하거나 정확한 대안 없음         |

---

### [실무]

Retrieval Fallback 예시:

```text
Failure:
관련 문서 검색 실패

Fallback:
- 답변 가능한 일반 기준만 제공
- 프로젝트 고유 정보는 확정하지 않음
- 필요한 문서 이름을 명시
```

Tool Fallback 예시:

```text
Failure:
Build Tool 실행 실패

Fallback:
- 에러 메시지 기반 분석
- 실제 빌드 성공 여부는 확정하지 않음
- 필요 시 수동 실행 명령 제공
```

Format Fallback 예시:

```text
Failure:
JSON Schema 반복 실패

Fallback:
- Required Field 축소
- 중첩 구조 제거
- 단순 배열 또는 표로 변경
```

Safety Fallback 예시:

```text
Failure:
DB DELETE 승인 없음

Fallback:
- 실행하지 않음
- SQL Preview 제공
- 백업 필요성 안내
- Human Confirmation 요청
```

Fallback Report 예시:

```md
| Failure             | Fallback         | Result                  |
| ------------------- | ---------------- | ----------------------- |
| Retrieval 실패      | Partial Answer   | 프로젝트 고유 정보 제외 |
| Tool 권한 없음      | 사용자 파일 요청 | Ask / Stop              |
| JSON 반복 실패      | Schema 단순화    | Fix 가능                |
| High Risk 승인 없음 | Action Preview   | Ask / Stop              |
```

---

### [주의]

Fallback 주의사항:

- Fallback은 실패를 숨기는 것이 아니다.
- Partial Answer는 한계를 명확히 표시해야 한다.
- 프로젝트 고유 정보는 근거 없이 Fallback으로 생성하지 않는다.
- 안전 실패는 Fallback으로 우회하면 안 된다.
- 대체 Tool도 Risk Evaluation이 필요하다.
- Fallback이 사용자 요구사항을 완전히 만족하지 못할 수 있다.
- Fallback 후 Final Decision을 명확히 표시해야 한다.

---

### [Best Practice]

Fallback Best Practice:

- Retry 실패 후 Fallback을 고려한다.
- Fallback 방식의 범위와 한계를 표시한다.
- Partial Answer는 제공된 Context 범위로 제한한다.
- 대체 Tool 사용 전 Risk Level을 다시 평가한다.
- 사용자 확인이 필요한 경우 Ask로 전환한다.
- 안전상 대안이 없으면 Stop 또는 Block한다.
- Fallback 결과를 Evaluation Report에 기록한다.
- Fallback으로도 해결 불가하면 Missing Information을 명확히 표시한다.

---

### [FAQ]

Q. Fallback이 뭐야?
A. 기존 방식이 실패하거나 사용할 수 없을 때 다른 안전한 방식으로 전환하는 복구 전략이다.

Q. Retry와 Fallback 차이는?
A. Retry는 같은 작업을 다시 시도하는 것이고, Fallback은 다른 방법이나 축소된 범위로 전환하는 것이다.

Q. Fallback은 언제 필요해?
A. Retry가 실패했거나 Tool 권한 없음, Retrieval 부족, 위험 작업 승인 없음 같은 상황에서 필요하다.

Q. Partial Answer도 Fallback이야?
A. 맞다. 제공된 Context 범위 안에서만 답하는 Fallback 방식이다.

Q. Safety Failure를 Fallback으로 우회해도 돼?
A. 안 된다. 안전상 차단된 작업은 우회하면 안 된다.

---

# 4. Stop / Ask / Block Rules

## 4.1 Stop Rule

### [개념]

Stop Rule은 Agent가 더 이상 안전하거나 정확하게 진행할 수 없을 때 작업을 중단하는 기준이다.

Stop은 실패를 숨기는 것이 아니라 현재 진행 불가 상태를 명확히 표시하는 안전한 동작이다.

Stop은 항상 실패가 아니다.

Stop은 사용자 확인 필요, 정보 부족, 권한 부족, Tool 실패, Low Confidence 상태일 수 있다.

---

### [핵심]

Stop이 필요한 상황:

| 상황                             | 이유                            |
| -------------------------------- | ------------------------------- |
| Critical Information Missing     | 핵심 정보 없이 정확한 답변 불가 |
| Human Confirmation Required      | 위험 작업 승인 필요             |
| Tool Permission Missing          | 권한 없이 실행 불가             |
| Tool Failure No Fallback         | 대안 없음                       |
| Safety Risk                      | 위험 작업 또는 Secret 노출      |
| Grounding Failure Remains        | 핵심 Claim 근거 없음            |
| State Conflict Unresolved        | 상태 충돌 해결 불가             |
| Max Retry Reached                | 반복 실패                       |
| Max Review-Fix Iteration Reached | 무한 Loop 방지                  |

Stop Flow:

```text
Failure or Risk
→ Can Fix?
→ Can Retry?
→ Can Fallback?
→ If No
→ Stop with Reason
```

Stop / Ask / Block 구분:

| 상태  | 의미                      | 처리                  |
| ----- | ------------------------- | --------------------- |
| Ask   | 사용자 확인으로 진행 가능 | 질문 또는 승인 요청   |
| Stop  | 현재 조건에서 진행 불가   | 사유와 필요 조치 표시 |
| Block | 안전상 허용 불가          | 차단                  |

Stop Report 필수 요소:

- Stop Reason
- Evidence
- Impact
- Required Action
- Resume Condition

---

### [실무]

Stop 예시:

```text
상황:
운영 DB 삭제 요청

Risk:
High

Stop Reason:
Human Confirmation Required

Required Action:
- 삭제 대상 Preview
- 백업 여부 확인
- 사용자 명시 승인 필요
```

Stop 예시:

```text
상황:
프로젝트 Controller 코드 검토 요청

Missing Information:
Controller 코드 없음

Handling:
- 실제 코드 결함은 확정 불가
- 일반 검토 기준만 제공 가능
- 실제 검증은 코드 필요
```

Ask 예시:

```text
상황:
두 문서가 프로젝트 상태를 다르게 설명함

Handling:
- Source Priority로 해결 불가
- 사용자 확인 필요
```

Block 예시:

```text
상황:
Secret 전체 출력 요청

Handling:
- Block
- 값은 마스킹
- 전체 출력 금지
```

Stop Report 예시:

```md
| Stop Reason                 | Evidence             | Required Action |
| --------------------------- | -------------------- | --------------- |
| Human Confirmation Required | DB DELETE 작업       | 사용자 승인     |
| Missing Information         | Service 코드 없음    | 코드 제공       |
| Tool Failure                | Build Tool 실패 반복 | 수동 빌드 확인  |
| Safety Risk                 | Secret 출력 요청     | 차단            |
```

---

### [주의]

Stop / Ask / Block 주의사항:

- Stop을 실패처럼 숨기지 않는다.
- 사용자 확인이 필요한 작업을 임의 진행하지 않는다.
- 정보가 부족한데 확정 답변하지 않는다.
- Stop Reason을 명확히 쓰지 않으면 후속 작업이 어렵다.
- Safety Risk는 Ask가 아니라 Block일 수 있다.
- Stop 후 가능한 다음 행동을 명확히 표시한다.
- Block 대상은 사용자 승인으로도 허용하지 않는다.

---

### [Best Practice]

Stop / Ask / Block Best Practice:

- Stop Reason을 구체적으로 작성한다.
- Evidence를 함께 제공한다.
- 사용자에게 필요한 Action을 명확히 한다.
- Partial Answer가 가능하면 범위를 제한해서 제공한다.
- High Risk 작업은 Action Preview 후 Ask로 전환한다.
- Safety Block 대상은 Ask하지 않고 차단한다.
- 반복 실패는 Max Retry 또는 Max Iteration 근거를 표시한다.
- Stop과 Block을 구분한다.

---

### [FAQ]

Q. Stop Rule이 뭐야?
A. Agent가 더 이상 안전하거나 정확하게 진행할 수 없을 때 작업을 중단하는 기준이다.

Q. Stop은 실패야?
A. 항상 실패는 아니다. 사용자 확인 필요, 정보 부족, 권한 부족처럼 안전하게 중단한 상태일 수 있다.

Q. 언제 Stop해야 해?
A. 핵심 정보 부족, 위험 작업 승인 없음, Tool 실패 후 대안 없음, Safety Risk, Max Retry 도달 시 Stop해야 한다.

Q. Ask와 Stop은 어떻게 달라?
A. Ask는 사용자 확인으로 진행 가능성이 있는 상태이고, Stop은 현재 조건에서 더 진행하지 않는 상태다.

Q. Block은 Stop과 어떻게 달라?
A. Block은 안전상 허용하면 안 되는 작업을 차단하는 것이고, Stop은 진행 조건이 충족되지 않아 중단하는 것이다.

---

# 5. Max Iteration Rules

## 5.1 Retry Limit & Review-Fix Limit

### [개념]

Max Iteration Rules는 Retry, Review-Fix Loop, Tool 재시도, Format 재생성의 최대 반복 횟수를 제한하는 기준이다.

Max Iteration이 없으면 Agent Workflow는 같은 실패를 반복할 수 있다.

Max Iteration은 무한 루프 방지와 품질 안정화를 위한 Stop Condition이다.

---

### [핵심]

반복 제한 대상:

| 대상                   | 권장 제한        |
| ---------------------- | ---------------- |
| Tool Timeout Retry     | 1~2회            |
| Search Query Retry     | 2~3회            |
| Format Regeneration    | 1~2회            |
| Review-Fix Loop        | 1~3회            |
| Code Fix Attempt       | 1~3회            |
| Same Error Retry       | 1회 후 전략 변경 |
| High Risk Action Retry | 승인 전 금지     |

Max Iteration Flow:

```text
Attempt
→ Failure
→ Count Attempt
→ Same Failure?
→ Change Strategy or Stop
→ Max Reached?
→ Fallback / Stop
```

반복 결과 판단:

```text
Continue:
- Retry Limit 미도달
- 전략 변경 가능
- 위험도 낮음

Fallback:
- Retry 반복 실패
- 대체 방식 있음

Stop:
- Max Iteration 도달
- 대체 방식 없음
- 위험도 높음
```

---

### [실무]

Review-Fix Loop 예시:

```text
Draft
→ Review
→ Fix
→ Review
→ Fix
→ Review
→ Max Iteration Reached
→ Stop and Report Remaining Issues
```

Format 반복 실패 예시:

```text
Problem:
JSON 파싱 실패 반복

Attempt 1:
Schema 유지 후 재생성 실패

Attempt 2:
Schema 단순화 후 성공

If Fail Again:
Fallback to Markdown Table 또는 Stop
```

Search 반복 실패 예시:

```text
Problem:
문서 검색 실패

Retry 1:
한국어 키워드

Retry 2:
영어 키워드

Retry 3:
Domain 키워드

Still Fail:
Missing Information 표시
```

Max Iteration Report 예시:

```md
| Loop Type    | Attempt | Result     | Next                |
| ------------ | ------: | ---------- | ------------------- |
| Format Retry |       1 | Fail       | Schema 단순화       |
| Format Retry |       2 | Fail       | Fallback            |
| Review-Fix   |       3 | Same Issue | Stop                |
| Search Retry |       3 | No Context | Missing Information |
```

---

### [주의]

Max Iteration 주의사항:

- 같은 실패를 같은 방식으로 반복하지 않는다.
- 반복 횟수만 세고 전략을 바꾸지 않으면 의미가 없다.
- High Risk 작업은 반복 시 Side Effect가 누적될 수 있다.
- Non-idempotent 작업은 Retry 자체가 위험할 수 있다.
- Minor Issue 때문에 무한 Review-Fix를 돌리지 않는다.
- Max Iteration 도달 후 성공처럼 답변하지 않는다.
- Stop 시 남은 문제를 명확히 표시한다.

---

### [Best Practice]

Max Iteration Best Practice:

- 반복 가능한 작업에는 Limit을 둔다.
- 같은 오류가 반복되면 전략을 바꾼다.
- Retry와 Review-Fix Loop를 구분한다.
- High Risk 작업은 승인 전 반복하지 않는다.
- Max 도달 시 Fallback 또는 Stop으로 전환한다.
- 남은 문제를 Evaluation Report에 기록한다.
- 반복 Failure는 Guardrails 개선 대상으로 반영한다.

---

### [FAQ]

Q. Max Iteration Rule이 뭐야?
A. Retry, Review-Fix Loop, Tool 재시도, Format 재생성의 최대 반복 횟수를 제한하는 기준이다.

Q. 왜 Max Iteration이 필요해?
A. 무한 반복과 같은 실패 반복을 막기 위해 필요하다.

Q. Review-Fix Loop는 몇 번까지가 좋아?
A. 작업 복잡도에 따라 다르지만 보통 1~3회로 제한한다.

Q. Max Iteration에 도달하면 어떻게 해?
A. Fallback이 가능하면 전환하고, 불가능하면 Stop해야 한다.

Q. 같은 실패가 반복되면 어떻게 해?
A. 같은 방식으로 다시 시도하지 말고 Prompt, Query, Arguments, Schema를 바꿔야 한다.

---

# 6. Recovery Decision Matrix

## 6.1 Fix / Retry / Fallback / Stop Matrix

### [개념]

Recovery Decision Matrix는 Failure Type에 따라 Fix, Retry, Fallback, Stop, Block 중 어떤 복구 방식을 선택할지 정리한 기준이다.

Recovery Decision Matrix는 PM Agent, Review Agent, Safety Agent, Orchestrator가 복구 전략을 일관되게 선택하도록 돕는다.

---

### [핵심]

Recovery Decision Matrix:

| Failure Type          | Fix | Retry | Fallback | Stop | Block |
| --------------------- | --: | ----: | -------: | ---: | ----: |
| Requirement Failure   |   O |     △ |        △ |    △ |     X |
| Retrieval Failure     |   △ |     O |        O |    △ |     X |
| Grounding Failure     |   O |     △ |        O |    △ |     X |
| Faithfulness Failure  |   O |     △ |        △ |    △ |     X |
| Format Failure        |   O |     O |        O |    △ |     X |
| Code Failure          |   O |     △ |        △ |    △ |     X |
| Tool Timeout          |   X |     O |        O |    △ |     X |
| Tool Permission Error |   X |     X |        O |    O |     X |
| Safety Failure        |   X |     X |        X |    O |     O |
| Secret Exposure       |   X |     X |        X |    O |     O |
| Memory Failure        |   O |     X |        △ |    △ |     X |
| Workflow Failure      |   O |     △ |        O |    O |     X |
| Review Failure        |   O |     △ |        △ |    △ |     X |

기호 의미:

```text
O:
- 기본적으로 적합

△:
- 상황에 따라 가능

X:
- 부적합
```

Decision Flow:

```text
Failure Type
→ Severity
→ Safety Risk?
→ Retryable?
→ Alternative Exists?
→ Fix / Retry / Fallback / Stop / Block
```

---

### [실무]

예시 1:

```text
Failure:
Retrieval Failure

Decision:
- Query Retry 가능
- 그래도 실패하면 Partial Answer 또는 Missing Information
```

예시 2:

```text
Failure:
Tool Permission Error

Decision:
- Retry 부적합
- 사용자 승인 또는 권한 필요
- Fallback으로 수동 절차 제공 가능
```

예시 3:

```text
Failure:
Secret Exposure

Decision:
- Retry 부적합
- 즉시 마스킹
- 전체 출력 요청은 Block
```

예시 4:

```text
Failure:
Format Failure

Decision:
- Schema 단순화
- 1~2회 Retry
- 반복 실패 시 Markdown Table로 Fallback
```

Recovery Report 예시:

```md
| Failure               | Severity | Decision         | Reason                |
| --------------------- | -------- | ---------------- | --------------------- |
| Retrieval Failure     | Major    | Retry → Fallback | Query 변형 가능       |
| Tool Permission Error | Major    | Ask / Stop       | 권한 없이는 해결 불가 |
| Secret Exposure       | Critical | Block            | 안전상 허용 불가      |
| Format Failure        | Major    | Fix / Retry      | 구조 단순화 가능      |
```

---

### [주의]

Recovery Decision 주의사항:

- Matrix는 기준이며 상황별 Risk를 추가 판단해야 한다.
- Safety Failure는 다른 복구보다 Stop / Block이 우선이다.
- Retry 가능해도 Side Effect가 있으면 제한해야 한다.
- Fallback은 요구사항을 완전히 만족하지 못할 수 있다.
- Stop은 실패 은폐가 아니라 안전한 중단이다.
- Block 대상은 사용자 승인으로도 허용하지 않는다.
- 복구 결정에는 Evidence가 필요하다.

---

### [Best Practice]

Recovery Decision Best Practice:

- Failure Type을 먼저 분류한다.
- Severity와 Safety Risk를 확인한다.
- Retryable 여부를 판단한다.
- Alternative 존재 여부를 확인한다.
- Fix / Retry / Fallback / Stop / Block 중 하나를 명확히 선택한다.
- Decision Reason을 짧게 기록한다.
- Recovery 후 Re-evaluation을 수행한다.
- 반복되는 실패는 Guardrail 강화 대상으로 기록한다.

---

### [FAQ]

Q. Recovery Decision Matrix가 뭐야?
A. Failure Type에 따라 Fix, Retry, Fallback, Stop, Block 중 어떤 복구 방식을 선택할지 정리한 기준이다.

Q. Matrix만 보고 결정하면 돼?
A. 아니다. Severity, Safety Risk, Side Effect, 사용자 승인 여부를 함께 판단해야 한다.

Q. Safety Failure는 어떻게 복구해?
A. 일반적인 Retry나 Fallback이 아니라 Stop 또는 Block으로 처리해야 한다.

Q. Format Failure는 어떻게 복구해?
A. Schema 단순화, Required Field 명확화, 제한적 Retry, Fallback을 사용할 수 있다.

Q. Tool Permission Error는 Retry하면 돼?
A. 아니다. 권한 또는 사용자 승인이 필요하므로 Ask, Fallback, Stop이 적절하다.

---

# 7. Failure, Retry & Fallback Checklist

## 7.1 Checklist

### [개념]

Failure, Retry & Fallback Checklist는 Agent 실패를 안전하게 분류하고 복구 전략을 선택하기 위한 최소 검증 목록이다.

이 Checklist는 PM Agent, Review Agent, Safety Agent, Tool Agent, Orchestrator가 공통으로 사용할 수 있다.

---

### [핵심]

Failure Classification Checklist:

```md
### [Checklist]

- [ ] 실패 증상을 확인했는가?
- [ ] 실패 발생 지점을 확인했는가?
- [ ] Failure Type을 분류했는가?
- [ ] Severity를 판단했는가?
- [ ] Evidence를 기록했는가?
- [ ] Safety Failure 여부를 확인했는가?
- [ ] Tool Failure 여부를 확인했는가?
- [ ] Grounding Failure 여부를 확인했는가?
- [ ] Format Failure 여부를 확인했는가?
- [ ] Memory / Workflow Failure 여부를 확인했는가?
```

Retry Checklist:

```md
### [Checklist]

- [ ] Retry 가능한 실패인가?
- [ ] Retry Limit이 있는가?
- [ ] 같은 입력을 반복하지 않는가?
- [ ] Prompt / Query / Arguments를 수정했는가?
- [ ] Side Effect가 없는가?
- [ ] Non-idempotent 작업이 아닌가?
- [ ] High Risk 작업이 아닌가?
- [ ] Retry 결과를 기록했는가?
```

Fallback Checklist:

```md
### [Checklist]

- [ ] Retry가 실패했거나 부적합한가?
- [ ] 안전한 대체 방법이 있는가?
- [ ] Partial Answer가 가능한가?
- [ ] 사용자 확인이 필요한가?
- [ ] 대체 Tool의 위험도를 평가했는가?
- [ ] Fallback 한계를 명확히 표시했는가?
- [ ] Fallback 후에도 해결 불가하면 Stop했는가?
```

Stop / Block Checklist:

```md
### [Checklist]

- [ ] Stop Reason이 명확한가?
- [ ] Evidence가 있는가?
- [ ] Required Action이 명확한가?
- [ ] Human Confirmation 필요 여부를 표시했는가?
- [ ] Missing Information을 표시했는가?
- [ ] Safety Block 여부를 확인했는가?
- [ ] Stop과 Block을 구분했는가?
```

최소 Pass 기준:

```text
- Failure Type 분류
- Retryable 여부 판단
- Retry Limit 적용
- Fallback 가능성 확인
- Stop Reason 명확화
- Safety Failure 우선 처리
```

---

### [실무]

실무 적용 Flow:

```text
Failure Detected
→ Failure Classification Checklist
→ Retry Checklist
→ Fallback Checklist
→ Stop / Block Checklist
→ Evaluation Report 기록
```

Checklist Result 예시:

```md
| Category | Item             | Result | Handling   |
| -------- | ---------------- | ------ | ---------- |
| Failure  | Tool Timeout     | Pass   | Retry 가능 |
| Retry    | Limit 존재       | Pass   | 1회 재시도 |
| Fallback | 대체 방법 있음   | Pass   | 범위 축소  |
| Stop     | Stop Reason 명확 | Pass   | 결과 보고  |
```

---

### [주의]

Checklist 주의사항:

- Checklist는 최소 기준이다.
- Safety Failure는 Retry보다 Stop / Block이 우선이다.
- Retry Limit 없이 반복하지 않는다.
- Fallback은 실패를 숨기는 용도가 아니다.
- Partial Answer는 범위와 한계를 표시해야 한다.
- Stop Reason이 없으면 사용자가 다음 행동을 알 수 없다.
- Evidence 없는 Failure 분류는 신뢰도가 낮다.

---

### [Best Practice]

Checklist Best Practice:

- Failure 발생 즉시 Type을 분류한다.
- Retry 전에 입력을 수정한다.
- Retry Limit을 작게 유지한다.
- Fallback은 안전한 대안만 사용한다.
- Stop Report에는 Reason, Evidence, Required Action을 포함한다.
- Safety Failure는 Critical로 처리한다.
- 반복 실패는 Workflow 개선 대상으로 기록한다.
- Evaluation Report와 연결해 추적 가능하게 만든다.

---

### [FAQ]

Q. Failure, Retry & Fallback Checklist는 뭐야?
A. Agent 실패를 분류하고 Retry, Fallback, Stop 중 적절한 복구 전략을 선택하기 위한 최소 검증 목록이다.

Q. 실패하면 가장 먼저 뭘 해야 해?
A. Failure Type과 Severity를 분류해야 한다.

Q. Retry 전에 확인할 것은 뭐야?
A. Retry 가능한 실패인지, Retry Limit이 있는지, Side Effect가 없는지 확인해야 한다.

Q. Fallback 전에 확인할 것은 뭐야?
A. Retry가 실패했거나 부적합한지, 안전한 대체 방법이 있는지 확인해야 한다.

Q. Stop 전에 확인할 것은 뭐야?
A. Stop Reason, Evidence, Required Action, Human Confirmation 필요 여부를 확인해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Failure Classification이 뭐야?
A. Agent 실패 원인을 유형별로 분류해 Fix, Retry, Fallback, Stop 중 적절한 처리를 선택하는 기준이다.

Q. Agent Failure에는 어떤 유형이 있어?
A. Requirement Failure, Retrieval Failure, Grounding Failure, Faithfulness Failure, Format Failure, Code Failure, Tool Failure, Safety Failure, Memory Failure, Workflow Failure, Review Failure가 있다.

Q. Requirement Failure는 뭐야?
A. 사용자 요구사항을 누락하거나 금지 조건을 위반한 실패다.

Q. Retrieval Failure는 뭐야?
A. 필요한 문서나 Context를 검색하지 못한 실패다.

Q. Grounding Failure는 뭐야?
A. Retrieved Context나 제공 문서에 근거하지 않은 답변을 생성한 실패다.

Q. Format Failure는 뭐야?
A. JSON, Markdown, Required Section, Output Wrapper 같은 출력 형식을 위반한 실패다.

Q. Tool Failure는 뭐야?
A. Tool 선택, 인자, 실행, 결과 처리에서 발생한 실패다.

Q. Safety Failure는 뭐야?
A. 위험 작업, 승인 누락, Secret 노출, 정책 위반 같은 안전 실패다.

Q. Memory Failure는 뭐야?
A. 오래된 Memory나 충돌 Memory를 현재 사실처럼 사용한 실패다.

Q. Workflow Failure는 뭐야?
A. Routing, Handoff, State, Review / Fix 과정에서 발생한 실패다.

Q. Review Failure는 뭐야?
A. Review Agent가 중요한 문제를 놓치거나 문제가 아닌 것을 문제로 지적한 실패다.

Q. Retry가 뭐야?
A. 실패한 작업을 제한된 횟수 안에서 다시 시도하는 복구 전략이다.

Q. Retry 가능한 실패는 뭐야?
A. Timeout, Rate Limit, Network Error, Temporary API Error, Format Failure, Search Miss, 수정 가능한 Argument Error다.

Q. Retry하면 안 되는 실패는 뭐야?
A. Safety Failure, Permission Error, Human Confirmation Required, Secret Exposure, Missing Critical Information이다.

Q. Retry Limit은 왜 필요해?
A. 무한 반복과 중복 실행 위험을 막기 위해 필요하다.

Q. 같은 Prompt로 계속 Retry해도 돼?
A. 안 된다. 같은 실패가 반복되면 Prompt, Query, Arguments를 수정해야 한다.

Q. Non-idempotent 작업은 왜 Retry가 위험해?
A. 중복 생성, 중복 발송, 중복 결제처럼 되돌리기 어려운 문제가 발생할 수 있기 때문이다.

Q. Fallback이 뭐야?
A. 기존 방식이 실패하거나 사용할 수 없을 때 다른 안전한 방식으로 전환하는 복구 전략이다.

Q. Retry와 Fallback 차이는?
A. Retry는 같은 작업을 다시 시도하는 것이고, Fallback은 다른 방법이나 축소된 범위로 전환하는 것이다.

Q. Fallback은 언제 필요해?
A. Retry가 실패했거나 Tool 권한 없음, Retrieval 부족, 위험 작업 승인 없음 같은 상황에서 필요하다.

Q. Partial Answer도 Fallback이야?
A. 맞다. 제공된 Context 범위 안에서만 답하는 Fallback 방식이다.

Q. Safety Failure를 Fallback으로 우회해도 돼?
A. 안 된다. 안전상 차단된 작업은 우회하면 안 된다.

Q. Stop Rule이 뭐야?
A. Agent가 더 이상 안전하거나 정확하게 진행할 수 없을 때 작업을 중단하는 기준이다.

Q. Stop은 항상 실패야?
A. 아니다. 사용자 확인 필요, 정보 부족, 권한 부족처럼 안전하게 중단한 상태일 수 있다.

Q. 언제 Stop해야 해?
A. 핵심 정보 부족, 위험 작업 승인 없음, Tool 실패 후 대안 없음, Safety Risk, Max Retry 도달 시 Stop해야 한다.

Q. Ask와 Stop은 어떻게 달라?
A. Ask는 사용자 확인으로 진행 가능성이 있는 상태이고, Stop은 현재 조건에서 더 진행하지 않는 상태다.

Q. Block은 Stop과 어떻게 달라?
A. Block은 안전상 허용하면 안 되는 작업을 차단하는 것이고, Stop은 진행 조건이 충족되지 않아 중단하는 것이다.

Q. Max Iteration Rule이 뭐야?
A. Retry, Review-Fix Loop, Tool 재시도, Format 재생성의 최대 반복 횟수를 제한하는 기준이다.

Q. Review-Fix Loop는 몇 번까지가 좋아?
A. 작업 복잡도에 따라 다르지만 보통 1~3회로 제한한다.

Q. Max Iteration에 도달하면 어떻게 해?
A. Fallback이 가능하면 전환하고, 불가능하면 Stop해야 한다.

Q. Recovery Decision Matrix가 뭐야?
A. Failure Type에 따라 Fix, Retry, Fallback, Stop, Block 중 어떤 복구 방식을 선택할지 정리한 기준이다.

Q. Matrix만 보고 결정하면 돼?
A. 아니다. Severity, Safety Risk, Side Effect, 사용자 승인 여부를 함께 판단해야 한다.

Q. Tool Permission Error는 Retry하면 돼?
A. 아니다. 권한 또는 사용자 승인이 필요하므로 Ask, Fallback, Stop이 적절하다.

Q. Failure, Retry & Fallback Checklist는 언제 써?
A. Agent 실패를 발견한 직후 복구 전략을 선택할 때 사용한다.

Q. Failure, Retry & Fallback의 최종 목표는 뭐야?
A. Agent 실패를 안전하게 분류하고, 제한적 Retry와 Fallback을 통해 복구하거나, 필요하면 명확히 Stop하도록 만드는 것이다.
