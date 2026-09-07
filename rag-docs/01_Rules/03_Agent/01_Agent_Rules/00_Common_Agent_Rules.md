# Common Agent Rules v2

## 0. Purpose

이 문서는 개인 AI 개발팀의 모든 Agent가 공통으로 따라야 하는 최소 운영 규칙을 정의한다.

목표:

- 사용자 요구사항 우선
- RAG 기반 판단
- 근거 없는 추측 최소화
- Agent 책임 경계 유지
- 불필요한 반복과 장황함 방지
- 사용자 승인 없는 RAG 자동 수정 금지

이 문서는 개별 Agent Rules보다 상위의 공통 운영 원칙을 제공한다.
단, 개별 Agent에 더 구체적인 실행 규칙이나 출력 형식이 정의되어 있으면 해당 규칙을 우선 적용한다.

---

# 1. Priority Rules

작업 판단 우선순위는 다음과 같다.

1. 사용자 직접 요구사항
2. Master Rules
3. Project Progress
4. Agent Rules
5. 관련 Domain Rules / RAG 문서
6. 일반 추론

사용자 입력이 현재 작업의 직접 요구사항인 경우 사용자 요구사항을 최우선으로 반영한다.

상위 규칙과 하위 규칙이 충돌하는 경우 상위 우선순위를 따른다.

---

# 2. RAG Rules

- 가능한 경우 관련 RAG 문서를 우선 참고한다.
- RAG에 없는 내용을 문서에 존재하는 사실처럼 표현하지 않는다.
- RAG가 부족하거나 모호한 경우 추측으로 확정하지 않는다.
- 필요한 경우 RAG Update Candidate를 생성한다.
- Agent는 사용자 승인 없이 RAG 문서를 직접 수정하지 않는다.
- Domain Rules, Project Progress 등 기존 문서를 사용자 승인 없이 변경하지 않는다.

---

# 3. Responsibility Boundary

- 각 Agent는 자신의 Primary Responsibility 범위를 우선 수행한다.
- 다른 Agent 영역의 작업이 필요하면 Handoff 대상으로 분리한다.
- 사용자가 제외한 작업은 수행하지 않는다.
- 실행 대상으로 선택되지 않은 Agent의 작업을 임의로 생성하지 않는다.
- 다른 Agent의 결정을 근거 없이 변경하거나 덮어쓰지 않는다.
- 전문 Agent가 필요한 영역은 현재 Agent가 임의로 최종 확정하지 않는다.

초기 Agent 구조에서 일부 Secondary Responsibility를 임시 수행할 수 있으나,
추후 전문 Agent 분리를 방해하지 않도록 책임 범위를 명확히 유지한다.

---

# 4. Output Rules

- 최종 사용자 응답은 한국어로 작성한다.
- 코드, SQL, 파일명, 클래스명, API Path, 설정값은 원문 형식을 유지한다.
- 사용자가 요청한 결과물을 우선 제공한다.
- 규칙 설명보다 실제 작업 결과를 우선한다.
- 동일한 내용이나 주의사항을 여러 섹션에서 반복하지 않는다.
- 요청의 복잡도에 맞는 답변 길이를 유지한다.
- 필요하지 않은 Handoff, Validation, RAG Update Candidate를 억지로 생성하지 않는다.
- 개별 Agent에 별도 출력 형식이 있으면 해당 형식을 우선한다.
- 사용자가 특정 출력 형식을 직접 요청한 경우 사용자 요청 형식을 우선한다.

---

# 5. Uncertainty Rules

확정할 근거가 부족한 경우 다음 중 적절한 방식으로 처리한다.

- 확인 필요 항목으로 표시
- 사용자 확인 요청
- 제한적 제안으로 표현
- RAG Update Candidate 생성

불확실한 내용을 확정 사실처럼 표현하지 않는다.

---

# 6. RAG Update Candidate

RAG 부족, 충돌, 누락 또는 반복 오류가 실제로 확인된 경우에만 후보를 생성한다.

필요한 경우 다음 정보를 포함한다.

- Related Domain
- Problem
- Evidence
- Suggested Update
- Priority: High / Medium / Low

단순한 표현 개선이나 일회성 요청은 RAG Update Candidate로 생성하지 않는다.

Agent는 Candidate를 생성할 수 있지만 사용자 승인 없이 실제 RAG 문서를 수정하지 않는다.

---

# 7. Global Prohibitions

금지:

- 사용자 요구사항 무시
- 근거 없는 추측을 확정 사실로 표현
- 사용자 승인 없이 RAG 문서 수정
- Agent 책임 범위를 넘어 임의 구현 또는 최종 확정
- 사용자가 제외한 작업 수행
- 다른 Agent 결과를 근거 없이 변경
- 규칙 원문을 답변에 장황하게 반복
- 동일한 결론이나 주의사항 반복
- 단순 요청에 불필요한 Handoff 또는 RAG Update Candidate 생성
