# Agent Evaluation & Guardrails Domain Rules

---

# 1. Domain Purpose

Agent Evaluation & Guardrails Domain 문서는 AI Agent / PM Agent / Review Agent / Safety Agent용 RAG 문서 제작 규칙이다.

목적:

- Agent Output 품질 평가 기준 제공
- Agent Workflow 평가 기준 제공
- Hallucination / Unsupported Claim 검증 기준 제공
- Tool Calling 안전성 검토 기준 제공
- RAG Grounding 검증 기준 제공
- Agent 실패 유형 분석 지원
- Guardrails 설계 기준 제공
- Human Confirmation / Stop Condition 기준 제공
- 개인 AI 개발팀의 안정성과 신뢰도 향상 지원

우선순위:

1. Output Correctness
2. Groundedness
3. Safety
4. Tool Execution Control
5. Requirement Compliance
6. Workflow Reliability
7. Human Oversight

---

# 2. Scope

포함 범위:

- Agent Evaluation Core
- Output Evaluation
- RAG Grounding Evaluation
- Hallucination Detection
- Unsupported Claim Check
- Requirement Compliance
- Format Compliance
- Code Review Evaluation
- Tool Calling Evaluation
- Workflow Evaluation
- Safety Guardrails
- Prompt Guardrails
- Tool Guardrails
- Memory Guardrails
- Human-in-the-loop
- Approval Rule
- Stop Condition
- Retry Limit
- Failure Classification
- Risk Level
- Evaluation Checklist
- Quality Report

제외 범위:

- AI Safety 연구 심화
- 정책/법률 컴플라이언스 상세
- 대규모 Red Team 운영
- Model Alignment 학습 상세
- RLHF 상세
- Fine-Tuning 평가 심화
- MLOps 모니터링 상세
- 보안 관제 시스템 운영 상세

---

# 3. Section Priority

## Required

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

## Strongly Recommended

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

# 4. Agent Evaluation Core Rules

Agent Evaluation 문서는 Agent가 만든 결과가 요구사항, 근거, 형식, 안전 기준을 만족하는지 평가하는 구조 중심으로 작성한다.

핵심 Flow:

```text
Agent Output
→ Requirement Check
→ Grounding Check
→ Format Check
→ Safety Check
→ Tool / State Check
→ Pass or Fix
```

반드시 설명:

- Agent 결과는 항상 검증 대상
- 최종 답변뿐 아니라 중간 산출물도 평가 가능
- RAG 기반 답변은 문서 근거와 일치해야 함
- Tool Calling 결과는 실행 안전성과 결과 정확성을 검증해야 함
- Guardrails는 Agent가 위험하거나 부정확한 행동을 하지 않도록 제한하는 규칙
- 평가 기준이 명확해야 Review Agent가 일관되게 검증 가능

금지:

- Agent 답변을 무조건 신뢰하는 설명
- 최종 답변만 보고 Workflow 품질을 판단하는 방식
- 근거 없는 답변을 허용하는 구조
- 위험 Tool을 자동 실행하는 구조
- 실패 상태를 성공처럼 포장하는 방식

---

# 5. Evaluation Dimensions Rules

Agent 평가 기준은 여러 차원으로 나눈다.

필수 포함:

- Correctness
- Completeness
- Groundedness
- Faithfulness
- Relevance
- Format Compliance
- Requirement Compliance
- Safety
- Consistency
- Actionability

평가 기준:

| 기준              | 의미                                |
| ----------------- | ----------------------------------- |
| Correctness       | 내용이 맞는가                       |
| Completeness      | 필요한 내용을 빠뜨리지 않았는가     |
| Groundedness      | 근거 문서에 기반하는가              |
| Faithfulness      | 제공된 Context를 왜곡하지 않는가    |
| Relevance         | 질문과 관련 있는가                  |
| Format Compliance | 요구 형식을 지켰는가                |
| Safety            | 위험하거나 부적절한 행동을 피했는가 |
| Actionability     | 실행 가능한 결과인가                |

반드시 설명:

- 하나의 점수로 모든 품질을 판단하지 않음
- 작업 유형별 평가 기준이 다름
- RAG 답변은 Groundedness가 중요
- Code Generation은 Correctness와 Consistency가 중요
- Tool Workflow는 Safety와 Permission이 중요

주의:

- 답변이 길다고 Completeness가 높은 것은 아님
- 그럴듯한 답변도 Groundedness가 낮을 수 있음
- 형식은 맞지만 내용이 틀릴 수 있음

---

# 6. Output Evaluation Rules

Output Evaluation은 Agent 산출물 자체를 평가한다.

필수 포함:

- Task Match
- Missing Requirement
- Wrong Assumption
- Unsupported Claim
- Incorrect Format
- Ambiguous Answer
- Actionable Result

기본 Flow:

```text
User Requirement
→ Agent Output
→ Compare Requirement
→ Identify Missing / Wrong / Unsafe Parts
→ Pass or Request Fix
```

반드시 설명:

- 사용자 요청과 결과가 일치하는지 확인
- 누락된 요구사항 확인
- 임의 가정이 있는지 확인
- 실행 가능한 결과인지 확인
- 불확실한 내용은 불확실하다고 표시했는지 확인

주의:

- 요청하지 않은 범위까지 과도하게 확장하지 않기
- 불명확한 요구사항을 임의 확정하지 않기
- 핵심 결론 없이 설명만 길게 작성하지 않기

---

# 7. Requirement Compliance Rules

Requirement Compliance는 사용자 요구사항과 제약 준수 여부를 평가한다.

필수 포함:

- User Request
- Must Requirement
- Must Not Requirement
- Constraint
- Priority
- Acceptance Criteria

예시:

```text
User Requirement:
- Java 21 기준
- Spring Boot 3.x
- ApiResponse<T> 직접 반환
- 예외는 GlobalExceptionHandler 처리

Evaluation:
- Java 21 반영 여부
- ResponseEntity 사용 여부
- 예외 처리 중복 여부
```

반드시 설명:

- 명시 요구사항을 우선 평가
- 금지 조건 위반은 중요한 결함
- 요구사항 간 충돌이 있으면 우선순위 필요
- Acceptance Criteria가 있으면 그 기준으로 Pass / Fail 판단

주의:

- 사용자 요구를 임의로 바꾸지 않기
- 선호사항과 필수사항 구분
- 누락 요구사항을 Minor로만 보지 않기

---

# 8. Grounding Evaluation Rules

Grounding Evaluation은 답변이 근거에 기반하는지 평가한다.

필수 포함:

- Retrieved Context
- Evidence
- Citation / Source
- Supported Claim
- Unsupported Claim
- Missing Evidence
- Assumption

기본 Flow:

```text
Answer Claim
→ Match with Retrieved Context
→ Supported / Unsupported
→ Mark Issue
```

반드시 설명:

- 답변의 주요 주장마다 근거를 확인
- RAG 문서에 없는 내용을 확정적으로 말하면 문제
- 일반 지식으로 보완할 경우 Assumption 표시 필요
- 문서에 정보가 없으면 부족하다고 말해야 함

주의:

- Citation이 있다고 실제 근거가 있는 것은 아님
- 근거 문서를 왜곡하거나 과장하지 않기
- 문서에 없는 클래스명, API, 정책 생성 금지

---

# 9. Hallucination Detection Rules

Hallucination Detection은 Agent가 없는 정보를 만들어냈는지 확인한다.

필수 포함:

- Fabricated Fact
- Fabricated File
- Fabricated API
- Fabricated Class
- Unsupported Code
- Wrong Citation
- False Confidence

Hallucination 예시:

```text
문서에 없는 API 경로를 실제 프로젝트에 있는 것처럼 설명
존재하지 않는 Entity 필드를 기준으로 코드 작성
검색되지 않은 정책을 확정적으로 말함
```

반드시 설명:

- Hallucination은 그럴듯하지만 근거 없는 생성
- 프로젝트 고유 정보에서 특히 위험
- 코드 생성에서는 존재하지 않는 클래스/메서드 생성이 흔함
- RAG 문서 기반 작업에서는 Retrieved Context와 대조 필요

주의:

- 일반 개발 지식과 프로젝트 사실을 구분
- 불확실하면 확인 요청 또는 Assumption 표시
- Review Agent가 Unsupported Claim을 찾아야 함

---

# 10. Faithfulness Rules

Faithfulness는 답변이 제공된 Context를 왜곡하지 않는지 평가한다.

필수 포함:

- Context Consistency
- Contradiction
- Overstatement
- Omission
- Misinterpretation
- Unsupported Generalization

반드시 설명:

- 답변이 Context와 일치하는지 확인
- 문서 내용을 과장하지 않음
- 조건부 설명을 절대 규칙으로 바꾸지 않음
- 예외사항을 누락하면 Faithfulness가 낮아질 수 있음

주의:

- 요약 과정에서 의미가 바뀌지 않도록 함
- 문서 간 충돌이 있으면 우선순위를 표시
- 코드/설정 설명에서 조건 누락 주의

---

# 11. Format Compliance Rules

Format Compliance는 요구한 출력 형식을 지켰는지 평가한다.

필수 포함:

- Markdown Format
- JSON Format
- Checklist
- Table
- Code Block
- Required Section
- Field Schema

예시:

```json
{
  "status": "pass",
  "findings": [],
  "requiresFix": false
}
```

반드시 설명:

- Agent Workflow에서는 출력 형식 준수가 중요
- JSON은 파싱 가능해야 함
- Markdown은 섹션 구조가 명확해야 함
- RAG 문서는 필수 섹션 누락 여부 확인 가능

주의:

- JSON 출력에 설명 문장이 섞이면 파싱 실패
- Required Field 누락 주의
- Markdown Header 계층 혼동 주의
- 형식이 맞아도 내용 검증은 별도 필요

---

# 12. Code Evaluation Rules

Code Evaluation은 Agent가 생성한 코드 품질을 평가한다.

필수 포함:

- Syntax Correctness
- Compile 가능성
- Runtime Risk
- Project Convention
- Version Compatibility
- Error Handling
- Security
- Testability
- Maintainability

Backend Code Review 예시:

```text
검토 기준:
- Java 21 / Spring Boot 3.x 기준인가?
- Transaction Boundary가 적절한가?
- N+1 위험이 있는가?
- 예외 처리 구조가 프로젝트 규칙과 맞는가?
- DTO / Entity 책임이 분리되어 있는가?
```

반드시 설명:

- 코드가 문법적으로 맞는지 확인
- 프로젝트 버전과 구조에 맞는지 확인
- 보안 / 예외 / 테스트 가능성 확인
- 존재하지 않는 클래스나 메서드 생성 여부 확인

주의:

- 일부 코드만 보고 전체 시스템을 단정하지 않기
- 취향과 결함을 구분
- 컴파일 오류와 설계 개선점을 구분
- 실제 실행 검증이 필요할 수 있음

---

# 13. Tool Calling Evaluation Rules

Tool Calling 결과는 별도로 평가한다.

필수 포함:

- Tool Choice Correctness
- Argument Validation
- Permission Check
- Execution Status
- Result Validation
- Side Effect Check
- Error Handling
- Audit Log

기본 Flow:

```text
Tool Call
→ Check Tool Choice
→ Validate Arguments
→ Check Permission
→ Execute
→ Validate Result
→ Continue or Stop
```

반드시 설명:

- 올바른 Tool을 선택했는지 확인
- Tool Arguments가 Schema와 제약을 만족하는지 확인
- 위험 작업은 승인 여부 확인
- Tool Result가 성공인지 실패인지 구분
- 실패 결과를 성공처럼 답변하면 안 됨

주의:

- LLM이 만든 Tool Arguments를 신뢰하지 않기
- 파일 삭제, DB 변경, 이메일 발송, 배포는 승인 필요
- Tool Result에 민감정보가 포함될 수 있음

---

# 14. Workflow Evaluation Rules

Workflow Evaluation은 Agent 전체 실행 흐름을 평가한다.

필수 포함:

- Routing Accuracy
- Handoff Quality
- State Consistency
- Review Effectiveness
- Fix Effectiveness
- Stop Condition
- Failure Handling
- Final Output Quality

기본 Flow:

```text
Workflow Run
→ Check Routing
→ Check Agent Outputs
→ Check Review
→ Check Fix
→ Check Final Answer
→ Record Failure
```

반드시 설명:

- 최종 결과뿐 아니라 중간 Agent 흐름도 평가
- PM Agent가 적절히 라우팅했는지 확인
- Handoff에 필요한 Context가 포함되었는지 확인
- Review가 실제 문제를 찾았는지 확인
- Fix가 Review 내용을 제대로 반영했는지 확인

주의:

- Agent 수가 많다고 Workflow 품질이 좋은 것은 아님
- Review가 형식적으로만 수행될 수 있음
- State 불일치가 최종 오류로 이어질 수 있음

---

# 15. Guardrails Core Rules

Guardrails는 Agent가 위험하거나 부정확한 행동을 하지 않도록 제한하는 규칙이다.

필수 포함:

- Safety Rule
- Scope Limit
- Tool Permission
- Human Confirmation
- Grounding Rule
- Output Validation
- Retry Limit
- Stop Condition

Guardrail Flow:

```text
Agent Action
→ Check Policy / Scope
→ Check Tool Permission
→ Check Risk Level
→ Allow / Ask / Block
```

반드시 설명:

- Guardrails는 Agent의 자유도를 제한해 안정성을 높임
- 모든 작업을 막는 것이 아니라 위험한 행동을 통제
- Prompt Guardrail, Tool Guardrail, Memory Guardrail로 나눌 수 있음
- Guardrails는 Review와 함께 사용할 수 있음

주의:

- Guardrails가 너무 약하면 위험
- Guardrails가 너무 강하면 작업이 진행되지 않음
- 위험도 기반으로 Allow / Ask / Block 구분

---

# 16. Prompt Guardrails Rules

Prompt Guardrails는 Agent가 지시를 따르고 범위를 벗어나지 않도록 하는 규칙이다.

필수 포함:

- Role Boundary
- Scope Boundary
- No Hallucination Rule
- Missing Information Rule
- Output Format Rule
- Assumption Rule
- Refusal / Escalation Rule

예시:

```text
Do not invent project-specific facts.
If required information is missing, ask for clarification or mark assumptions.
Return output in the requested format.
```

반드시 설명:

- Prompt에 역할과 금지 범위를 명확히 포함
- 문서에 없는 내용은 확정하지 않게 함
- 출력 형식을 고정하면 후속 처리 안정성 증가
- 실패 시 행동 규칙 필요

주의:

- Prompt만으로 모든 안전을 보장할 수 없음
- Tool / Runtime Guardrail도 필요
- 너무 많은 규칙은 핵심 지시를 흐릴 수 있음

---

# 17. Tool Guardrails Rules

Tool Guardrails는 외부 도구 실행을 통제한다.

필수 포함:

- Tool Permission
- Risk Level
- Input Validation
- Output Validation
- Human Approval
- Dry Run
- Timeout
- Retry Limit
- Audit Log

Risk Level:

| Risk   | 예시                             | 처리             |
| ------ | -------------------------------- | ---------------- |
| Low    | 검색, 파일 읽기                  | 자동 허용 가능   |
| Medium | 파일 쓰기, 설정 변경             | 검증 + 로그      |
| High   | 삭제, DB 변경, 배포, 이메일 발송 | 사용자 승인 필요 |

반드시 설명:

- Tool은 실제 시스템에 영향을 줄 수 있음
- 위험도에 따라 자동 실행 / 확인 / 차단을 구분
- 입력값 검증과 권한 확인 필수
- Side Effect가 있는 Tool은 Audit Log 필요

주의:

- LLM이 생성한 명령을 그대로 실행하지 않음
- Non-idempotent 작업 재시도 주의
- Secret / 민감정보 로그 금지

---

# 18. Memory Guardrails Rules

Memory Guardrails는 오래된 정보와 민감정보 문제를 줄인다.

필수 포함:

- Memory Validation
- Recency Check
- Conflict Check
- Sensitive Data Filter
- User Correction Priority
- Forget Rule
- Memory Update Rule

반드시 설명:

- Memory는 항상 최신이 아닐 수 있음
- 현재 사용자 요청이 오래된 Memory보다 우선
- 충돌이 있으면 사용자 확인 또는 최신 정보 우선
- 민감정보는 저장하지 않음
- 사용자가 잊어달라고 하면 반영해야 함

주의:

- 오래된 프로젝트 정보를 현재 사실처럼 사용 금지
- 불확실한 Memory를 확정적으로 말하지 않기
- Secret을 Memory에 저장 금지

---

# 19. RAG Guardrails Rules

RAG Guardrails는 검색 문서 기반 답변의 안전장치이다.

필수 포함:

- Retrieved Context Required
- Grounding Rule
- Citation Rule
- Missing Information Rule
- Source Priority
- Conflict Handling
- No Unsupported Claim

기본 규칙:

```text
Use retrieved context first.
If retrieved context is insufficient, say what is missing.
Do not invent project-specific facts.
Mark assumptions clearly.
```

반드시 설명:

- RAG 답변은 검색 문서 우선
- 검색 실패 시 일반 지식으로 확정하지 않음
- 문서 충돌 시 우선순위 필요
- 답변 근거를 추적 가능해야 함

주의:

- 검색 결과와 무관한 답변 생성 금지
- 검색 문서에 없는 API / 파일 / 정책 생성 금지
- 근거 없는 확신 표현 금지

---

# 20. Human Confirmation Rules

Human Confirmation은 Guardrails의 핵심이다.

필수 포함:

- Approval Required
- Risk Summary
- Action Preview
- Affected Target
- Confirm / Cancel
- Dry Run
- Irreversible Action

승인 필요 예시:

```text
파일 삭제
DB 데이터 변경
이메일 발송
배포 실행
결제 요청
대량 API 호출
비용 발생 작업
```

반드시 설명:

- 위험 작업은 실행 전 사용자 승인 필요
- 승인 요청에는 대상과 영향 범위를 명확히 표시
- 되돌릴 수 없는 작업은 특별히 강조
- 승인 범위를 넘는 추가 작업은 금지

주의:

- 모호한 동의로 실행하지 않기
- 사용자 확인 없이 위험 작업 자동화 금지
- Preview와 실제 실행 내용 일치

---

# 21. Stop Condition Rules

Stop Condition은 Agent가 언제 멈출지 정의한다.

필수 포함:

- Task Completed
- Review Passed
- Max Iteration
- Missing Information
- Tool Failure
- Unsafe Action
- User Confirmation Required
- Low Confidence

예시:

```text
Stop if:
- Required information is missing
- Tool call failed and no fallback exists
- Action requires user approval
- Max review-fix iteration is reached
```

반드시 설명:

- Stop Condition은 무한 루프 방지
- 불확실한 상태에서 억지로 완료하지 않음
- 사용자 확인이 필요한 상태는 중단 가능
- 실패와 완료를 명확히 구분

주의:

- 실패를 성공으로 처리하지 않기
- Max Iteration 없이 Review-Fix 반복 금지
- 정보 부족 시 임의 생성 금지

---

# 22. Risk Classification Rules

Risk Classification은 Agent 행동의 위험도를 분류한다.

필수 포함:

- Low Risk
- Medium Risk
- High Risk
- Reversible
- Irreversible
- External Side Effect
- Cost Impact
- Security Impact

분류 예시:

| Risk   | 작업                        | 처리         |
| ------ | --------------------------- | ------------ |
| Low    | 설명, 요약, 검색            | 진행         |
| Medium | 파일 생성, 초안 작성        | 검증 후 진행 |
| High   | 삭제, 배포, DB 변경         | 사용자 승인  |
| Block  | Secret 노출, 위험 명령 실행 | 차단         |

반드시 설명:

- 위험도는 실행 전 판단
- 되돌릴 수 없는 작업은 High Risk
- 외부 시스템에 영향을 주는 작업은 확인 필요
- 보안/비용/데이터 손실 가능성을 고려

주의:

- 위험도 낮아 보여도 대량 작업이면 위험 증가
- 비용 발생 작업은 사용자 확인 가능
- 자동화 범위가 클수록 Guardrail 강화

---

# 23. Failure Classification Rules

Agent 실패는 유형별로 분류한다.

필수 포함:

- Requirement Failure
- Retrieval Failure
- Grounding Failure
- Format Failure
- Tool Failure
- Safety Failure
- Memory Failure
- Workflow Failure

예시:

| Failure             | 의미                       |
| ------------------- | -------------------------- |
| Requirement Failure | 요구사항 누락/위반         |
| Retrieval Failure   | 필요한 문서 검색 실패      |
| Grounding Failure   | 근거 없는 답변             |
| Format Failure      | 출력 형식 위반             |
| Tool Failure        | Tool 실행 실패             |
| Safety Failure      | 위험 행동 발생             |
| Memory Failure      | 오래된/충돌 Memory 사용    |
| Workflow Failure    | Routing/Handoff/State 문제 |

반드시 설명:

- 실패 유형을 알아야 수정 방향이 명확해짐
- Review Agent는 실패 유형을 표시할 수 있음
- 실패 유형별 Fix 전략이 다름
- 반복 실패는 Workflow 개선 대상

---

# 24. Retry / Fallback Rules

Retry와 Fallback은 실패 복구 전략이다.

Retry 가능:

- 일시적 API 오류
- Rate Limit 일부
- Timeout 일부
- 형식 오류 재생성
- 검색 Query 변형

Fallback 필요:

- Retrieval 결과 없음
- Tool 권한 없음
- 사용자 확인 필요
- 모델 출력 반복 실패
- 안전상 실행 불가

기본 Flow:

```text
Failure
→ Check Retryable
→ Retry with Limit
→ Fallback
→ Ask User or Stop
```

주의:

- 무제한 Retry 금지
- 같은 Prompt로 반복 실패하면 Prompt 수정 필요
- 위험 작업 Retry는 특히 주의
- Retry 후에도 실패하면 명확히 보고

---

# 25. Review Agent Evaluation Rules

Review Agent 자체도 평가 대상이다.

필수 포함:

- Finding Quality
- False Positive
- False Negative
- Severity Accuracy
- Fix Direction Quality
- Requirement Awareness
- Domain Rule Awareness

반드시 설명:

- Review Agent가 실제 문제를 잘 찾는지 평가
- 쓸데없는 지적은 False Positive
- 놓친 중요한 문제는 False Negative
- Severity가 적절해야 Fix 우선순위가 맞음
- 수정 방향이 구체적이어야 함

주의:

- Review Agent가 너무 엄격하면 Workflow가 느려짐
- 너무 느슨하면 품질 문제가 남음
- Review 기준을 고정해야 일관성 유지

---

# 26. Evaluation Report Rules

Agent Evaluation 문서에는 평가 리포트 형식을 포함할 수 있다.

필수 포함:

- Evaluation Target
- Evaluation Criteria
- Result
- Findings
- Severity
- Evidence
- Fix Recommendation
- Pass / Fail

예시:

```md
# Agent Evaluation Report

## Summary

- Target:
- Result:
- Pass / Fail:

## Findings

| Severity | Issue | Evidence | Fix |
| -------- | ----- | -------- | --- |
```

반드시 설명:

- 평가 리포트는 후속 Fix와 품질 추적에 사용
- Evidence를 포함해야 신뢰도 높음
- Severity로 우선순위 결정
- Pass / Fail 기준을 명확히 함

---

# 27. Quality Score Rules

필요 시 Agent Output 품질 점수를 사용할 수 있다.

평가 예시:

| 항목                   | 점수 |
| ---------------------- | ---- |
| Requirement Compliance | 0~5  |
| Groundedness           | 0~5  |
| Completeness           | 0~5  |
| Format Compliance      | 0~5  |
| Safety                 | 0~5  |

반드시 설명:

- 점수는 보조 수단
- 점수보다 실패 원인과 수정 방향이 중요
- 항목별 점수를 분리해야 개선 방향이 명확
- 일정 점수 이하면 Fix 또는 Review 필요

주의:

- 단일 총점만으로 판단하지 않기
- 점수 기준이 모호하면 평가 일관성 낮음
- 자동 점수는 사람 검토와 함께 사용 가능

---

# 28. Troubleshooting Rules

반드시 포함 추천.

형식:

```md
문제:

원인:

해결:
```

---

## Agent가 근거 없는 답변을 함

문제:

- 문서에 없는 내용을 확정적으로 답변함

원인:

- RAG Guardrail 부족
- Grounding Evaluation 없음
- Missing Information Rule 없음

해결:

- Retrieved Context 우선 규칙 추가
- Unsupported Claim Check 적용
- 문서에 없으면 없다고 말하게 함
- Assumption 표시 규칙 추가

---

## Review Agent가 쓸데없는 지적을 많이 함

문제:

- 실제 결함이 아닌 취향 문제를 계속 지적함

원인:

- Review Criteria 불명확
- Severity 기준 없음
- Domain Rules와 프로젝트 규칙 구분 부족

해결:

- Review Checklist 정의
- Severity 기준 추가
- 취향 / 개선 / 결함 구분
- Fix 필요 여부 표시

---

## JSON 출력이 자꾸 깨짐

문제:

- Agent Output이 Schema를 따르지 않음

원인:

- Format Guardrail 부족
- Schema가 너무 복잡함
- 출력 예시 없음

해결:

- Schema 단순화
- Required Field 명시
- 예시 출력 추가
- Parse 실패 시 재생성 규칙 추가

---

## 위험 Tool이 승인 없이 실행됨

문제:

- 삭제, 수정, 발송, 배포 같은 작업이 자동 실행됨

원인:

- Tool Guardrail 없음
- Risk Classification 없음
- Human Confirmation Rule 없음

해결:

- Tool Risk Level 정의
- High Risk 작업 승인 필수
- Dry Run 추가
- Agent별 Tool Permission 제한

---

## Agent가 무한 반복함

문제:

- Review / Fix 또는 Retry가 계속 반복됨

원인:

- Stop Condition 없음
- Max Iteration 없음
- Failure Classification 없음

해결:

- Max Iteration 설정
- Stop Condition 정의
- 반복 실패 시 사용자 확인
- Minor Issue는 보고 후 종료 가능

---

## 오래된 Memory를 기준으로 답변함

문제:

- 현재 프로젝트와 맞지 않는 과거 정보를 사용함

원인:

- Memory Guardrail 부족
- Recency Check 없음
- 현재 요청 우선 규칙 없음

해결:

- Memory Validation 적용
- 현재 사용자 요청 우선
- Memory Conflict 규칙 추가
- 불확실하면 사용자 확인

---

# 29. Best Practice Rules

Best Practice:

- Agent Output은 항상 평가 기준을 가진다
- Requirement Compliance를 먼저 확인
- RAG 답변은 Groundedness와 Faithfulness 검증
- Unsupported Claim을 찾아낸다
- JSON / Markdown 형식은 별도로 검증
- Tool Arguments는 실행 전 검증
- 위험 Tool은 Human Confirmation 필수
- Stop Condition과 Max Iteration 설정
- 실패 유형을 분류해 수정 방향 결정
- Review Agent도 평가 대상에 포함
- Memory는 최신성과 충돌 여부 확인
- Guardrails는 Prompt / Tool / Memory / RAG로 나누어 설계
- 평가 리포트에는 Evidence와 Fix Recommendation 포함

---

# 30. Comparison Rules

Agent Evaluation & Guardrails 문서는 비교 기준을 포함한다.

필수 비교 대상:

- Evaluation vs Guardrails
- Correctness vs Groundedness
- Groundedness vs Faithfulness
- Format Compliance vs Content Quality
- Tool Guardrail vs Prompt Guardrail
- Human Confirmation vs Full Automation
- Retry vs Fallback
- False Positive vs False Negative
- Low Risk vs High Risk Action

예시:

| 비교 | Evaluation        | Guardrails            |
| ---- | ----------------- | --------------------- |
| 목적 | 결과를 평가       | 위험 행동을 예방/차단 |
| 시점 | 실행 후 또는 중간 | 실행 전/중/후         |
| 예시 | 답변 검토         | Tool 실행 승인        |
| 결과 | Pass / Fail / Fix | Allow / Ask / Block   |

---

# 31. Checklist Rules

Agent Evaluation & Guardrails 문서에는 Checklist를 포함할 수 있다.

예시:

```md
### [Checklist]

- [ ] 사용자 요구사항을 모두 반영했는가?
- [ ] 금지 조건을 위반하지 않았는가?
- [ ] 답변이 Retrieved Context에 근거하는가?
- [ ] Unsupported Claim이 없는가?
- [ ] 불확실한 내용은 Assumption으로 표시했는가?
- [ ] 출력 형식이 요구사항과 일치하는가?
- [ ] Tool Arguments를 검증했는가?
- [ ] 위험 Tool 실행에 사용자 승인이 있는가?
- [ ] Stop Condition이 정의되어 있는가?
- [ ] 반복 실패 시 Fallback이 있는가?
- [ ] 오래된 Memory를 검증했는가?
```

---

# 32. Retrieval Optimization Rules

강조 대상 키워드:

- Agent Evaluation
- Agent Guardrails
- Output Evaluation
- Requirement Compliance
- Groundedness
- Faithfulness
- Hallucination Detection
- Unsupported Claim
- Format Compliance
- Code Evaluation
- Tool Calling Evaluation
- Workflow Evaluation
- Safety Guardrails
- Prompt Guardrails
- Tool Guardrails
- Memory Guardrails
- RAG Guardrails
- Human Confirmation
- Stop Condition
- Risk Classification
- Failure Classification
- Retry
- Fallback
- Review Agent Evaluation
- Evaluation Report
- Quality Score

키워드 반복 허용.

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- Agent 평가는 어떻게 해?
- Guardrails가 뭐야?
- Groundedness는 어떻게 확인해?
- Hallucination은 어떻게 잡아?
- Tool Guardrail은 어떻게 설계해?
- Human Confirmation은 언제 필요해?
- Stop Condition은 왜 필요해?
- Agent가 무한 반복하면 어떻게 해?
- Review Agent도 평가해야 해?
- Agent 실패 유형은 어떻게 나눠?
- 위험 작업은 어떻게 막아?

---

# 33. Version Rules

기준:

- Modern LLM Agent
- RAG 기반 Agent Evaluation
- Tool Calling 기반 Guardrails
- Multi-Agent Workflow Evaluation
- Human-in-the-loop Safety
- Local LLM 기반 개인 AI 시스템 고려
- Review-Fix Loop 기반 품질 검증
- Agent Memory / State 검증 포함

Legacy 제외:

- Agent Output 무검증 사용
- RAG 근거 없는 답변 허용
- Tool Arguments 검증 없는 실행
- 위험 작업 승인 없는 실행
- Stop Condition 없는 Agent Loop
- Memory 최신성 검증 없는 답변
- Review 기준 없는 “검토해줘” 방식

---

# 34. Common Mistakes

자주 발생:

- 최종 답변만 평가하고 중간 Workflow는 보지 않음
- 요구사항 누락을 놓침
- RAG 답변의 근거 확인을 하지 않음
- Hallucination을 “모델이 그럴 수 있음”으로만 처리
- JSON 형식 검증 없음
- Tool Arguments 검증 없이 실행
- 위험 Tool 승인 절차 없음
- Stop Condition 없음
- Retry가 무한 반복됨
- Review Agent의 False Positive가 많음
- 오래된 Memory 검증 없음
- 평가 리포트에 Evidence가 없음
- Guardrails가 너무 약하거나 너무 강함

---

# 35. Final Goal

Agent Evaluation & Guardrails RAG 문서는 Agent가 아래를 수행 가능해야 한다.

- Agent Output 평가 기준 설명
- Requirement Compliance 검증
- Groundedness / Faithfulness 검증
- Hallucination / Unsupported Claim 탐지
- Format Compliance 검증
- Code Evaluation 기준 제안
- Tool Calling Evaluation 기준 제안
- Workflow Evaluation 기준 제안
- Prompt / Tool / Memory / RAG Guardrails 설계
- Risk Classification 수행
- Human Confirmation 필요 여부 판단
- Stop Condition 정의
- Failure Classification 수행
- Retry / Fallback 기준 제안
- Review Agent 품질 평가
- Evaluation Report 작성
- Agent 안정성 문제 Troubleshooting

문서 품질이 Agent System의 신뢰도와 안전성을 결정한다.

---

# Retrieval Queries

### [FAQ]

Q. Agent Evaluation이 뭐야?

A.
Agent가 만든 결과가 요구사항, 근거, 형식, 안전 기준을 만족하는지 평가하는 과정이다.

Q. Guardrails가 뭐야?

A.
Agent가 위험하거나 부정확한 행동을 하지 않도록 제한하고 통제하는 규칙이다.

Q. Evaluation과 Guardrails 차이는?

A.
Evaluation은 결과를 평가하는 것이고, Guardrails는 위험 행동을 사전에 막거나 실행 중 통제하는 것이다.

Q. Agent Output은 무엇을 기준으로 평가해?

A.
Correctness, Completeness, Groundedness, Format Compliance, Requirement Compliance, Safety를 기준으로 평가한다.

Q. Requirement Compliance는 뭐야?

A.
사용자가 요구한 필수 조건과 금지 조건을 Agent 결과가 지켰는지 확인하는 것이다.

Q. Groundedness는 어떻게 확인해?

A.
답변의 주요 주장이 Retrieved Context나 제공된 문서에 근거하는지 대조한다.

Q. Faithfulness는 뭐야?

A.
답변이 제공된 Context를 왜곡하거나 과장하지 않고 충실히 반영하는지 평가하는 기준이다.

Q. Hallucination은 어떻게 잡아?

A.
문서에 없는 주장, 존재하지 않는 파일명/클래스명/API, 잘못된 Citation을 Unsupported Claim으로 표시한다.

Q. Format Compliance는 왜 중요해?

A.
Agent Workflow에서 JSON, Markdown, Checklist 같은 출력 형식이 깨지면 후속 Agent나 Tool이 처리하기 어렵기 때문이다.

Q. Code Evaluation은 어떻게 해?

A.
문법, 컴파일 가능성, 프로젝트 규칙, 버전 호환성, 예외 처리, 보안, 테스트 가능성을 확인한다.

Q. Tool Calling Evaluation은 어떻게 해?

A.
Tool 선택이 적절한지, 인자가 검증되었는지, 권한이 맞는지, 실행 결과가 유효한지 확인한다.

Q. Tool Guardrails는 왜 필요해?

A.
Tool은 파일 수정, DB 변경, 이메일 발송, 배포처럼 실제 시스템에 영향을 줄 수 있기 때문이다.

Q. Human Confirmation은 언제 필요해?

A.
삭제, DB 변경, 배포, 이메일 발송, 결제, 대량 API 호출처럼 되돌리기 어렵거나 비용/위험이 있는 작업 전에 필요하다.

Q. Stop Condition은 왜 필요해?

A.
Agent가 무한 반복하지 않고 완료, 실패, 사용자 확인 필요 상태를 명확히 판단하기 위해 필요하다.

Q. Risk Classification은 어떻게 해?

A.
작업이 되돌릴 수 있는지, 외부 시스템에 영향을 주는지, 비용이나 보안 위험이 있는지 기준으로 Low / Medium / High / Block으로 나눈다.

Q. Failure Classification은 왜 필요해?

A.
Requirement Failure, Retrieval Failure, Tool Failure, Safety Failure처럼 실패 유형을 알아야 올바른 수정 방향을 정할 수 있기 때문이다.

Q. Retry와 Fallback 차이는?

A.
Retry는 같은 작업을 제한적으로 다시 시도하는 것이고, Fallback은 다른 방법이나 사용자 확인으로 전환하는 것이다.

Q. Review Agent도 평가해야 해?

A.
해야 한다. Review Agent가 False Positive를 많이 내거나 중요한 문제를 놓치면 Workflow 품질이 떨어진다.

Q. Memory Guardrails는 뭐야?

A.
오래된 Memory, 충돌 Memory, 민감정보 저장 문제를 막기 위한 규칙이다.

Q. Agent Evaluation Report에는 뭐가 들어가야 해?

A.
평가 대상, 기준, 결과, Findings, Severity, Evidence, Fix Recommendation, Pass / Fail이 들어가야 한다.

Q. Agent Evaluation & Guardrails의 최종 목표는 뭐야?

A.
Agent가 정확하고 근거 있는 결과를 만들고, 위험한 작업은 통제하며, 실패를 안전하게 처리하도록 만드는 것이다.
