# Prompt Engineering Part11 Safety, Guardrail, Tool Use Prompt

---

# 1. Safety Prompt

## 1.1 Safety Prompt Definition

### [개념]

Safety Prompt는 LLM이 위험하거나 부적절하거나 검증되지 않은 출력을 생성하지 않도록 제어하는 Prompt다.

Safety Prompt는 단순히 “안전하게 답해”가 아니다.

Safety Prompt는 허용 범위, 금지 범위, 거절 기준, 대체 응답, 정보 부족 처리, 정책 우선순위를 포함해야 한다.

기본 구조:

```text
Allowed Scope
→ Disallowed Scope
→ Risk Detection
→ Refusal Rule
→ Safe Alternative
→ Missing Information
→ Verification
```

Safety Prompt의 목적은 사용자의 요청을 가능한 범위에서 돕되, 위험한 출력이나 근거 없는 확정을 방지하는 것이다.

---

### [핵심]

- Safety Prompt는 위험한 출력 생성을 제한한다.
- 허용 가능한 작업과 허용 불가능한 작업을 구분한다.
- 불확실한 정보는 확정하지 않는다.
- 위험한 요청은 거절하거나 안전한 방향으로 전환한다.
- 코드 생성에서는 보안 취약점을 만들지 않도록 제어한다.
- RAG 답변에서는 문서에 없는 내용을 확정하지 않도록 제어한다.
- Tool 사용 결과는 검증 후 사용한다.
- Safety Prompt는 Guardrail Prompt와 함께 사용한다.

---

### [실무]

Safety Prompt 예시:

```text
Safety Rules:
- Do not generate unsafe or harmful instructions.
- Do not expose secrets, tokens, passwords, private keys, or credentials.
- Do not invent project-specific facts.
- If the request is unsafe or outside scope, explain the limitation and provide a safer alternative.
- If required information is missing, state the missing information instead of guessing.
```

개발 Agent Safety Prompt 예시:

```text
Backend Safety Rules:
- Do not expose authentication secrets.
- Do not generate code that logs passwords, tokens, or private keys.
- Do not disable security checks unless explicitly justified and safe.
- Do not bypass authorization logic.
- Mark missing security context as Missing Information.
```

Safety Prompt는 모델의 답변을 막기 위한 장치가 아니라, 안전한 범위에서 유용한 결과를 만들기 위한 제어 장치다.

---

### [FAQ]

Q. Safety Prompt가 뭐야?

A. LLM이 위험하거나 부적절하거나 검증되지 않은 출력을 생성하지 않도록 제어하는 Prompt다.

Q. Safety Prompt는 왜 필요해?

A. 보안 취약 코드, 비밀정보 노출, 위험한 지시, 근거 없는 확정을 줄이기 위해 필요하다.

Q. Safety Prompt와 Guardrail Prompt는 같아?

A. 관련 있지만 다르다. Safety Prompt는 안전 기준 자체이고, Guardrail Prompt는 그 기준을 적용하는 경계와 처리 규칙이다.

Q. 안전하지 않은 요청은 무조건 답하지 않아야 해?

A. 위험한 부분은 거절하고, 가능한 경우 안전한 대체 방향을 제공해야 한다.

---

# 2. Guardrail Prompt

## 2.1 Guardrail Prompt Definition

### [개념]

Guardrail Prompt는 LLM이 정해진 정책, 범위, 출력 형식, 안전 기준을 벗어나지 않도록 경계를 설정하는 Prompt다.

Guardrail은 답변 품질과 안전성을 유지하는 제약 시스템이다.

Guardrail Prompt는 Safety Prompt보다 넓은 개념이다.

Guardrail에는 아래 요소가 포함된다.

```text
Policy Boundary
→ Scope Boundary
→ Output Boundary
→ Tool Boundary
→ Data Boundary
→ Failure Boundary
→ Escalation Rule
```

---

### [핵심]

- Guardrail은 LLM의 행동 경계를 정한다.
- 정책 위반 요청을 제어한다.
- 프로젝트 Scope를 벗어난 작업을 막는다.
- 출력 형식 위반을 줄인다.
- Tool 사용 범위를 제한한다.
- 비밀정보, 개인정보, 인증정보를 보호한다.
- 실패 상황에서 지어내지 않도록 제어한다.
- Agent Workflow에서는 Agent별 책임 경계를 유지한다.

---

### [실무]

Guardrail Prompt 예시:

```text
Guardrails:
- Stay within the assigned role and scope.
- Follow project rules and domain rules.
- Use retrieved context before general knowledge.
- Do not invent missing facts.
- Do not expose sensitive information.
- If the task is outside scope, state the boundary and provide a safe alternative.
- If output format is specified, follow it exactly.
```

Agent Guardrail 예시:

```text
Agent Guardrails:
- PM Agent decomposes tasks but does not implement domain code.
- Backend Agent handles backend output only.
- Review Agent validates but does not silently rewrite the whole implementation.
- Fix Agent applies review findings without adding new requirements.
```

Guardrail Prompt는 Agent가 책임 범위 밖으로 나가지 않도록 만든다.

---

### [FAQ]

Q. Guardrail Prompt가 뭐야?

A. LLM이 정해진 정책, 범위, 출력 형식, 안전 기준을 벗어나지 않도록 경계를 설정하는 Prompt다.

Q. Guardrail은 Safety와 어떻게 달라?

A. Safety는 위험 방지 중심이고, Guardrail은 안전, 범위, 형식, 도구 사용, 실패 처리까지 포함하는 경계 규칙이다.

Q. Agent Workflow에서 Guardrail이 중요한 이유는 뭐야?

A. Agent별 책임 범위를 유지하고 역할 중복, 범위 초과, 잘못된 Handoff를 막기 위해 중요하다.

Q. Guardrail이 너무 많으면 문제야?

A. 그렇다. 너무 많으면 출력이 경직되고 핵심 작업 수행이 어려워질 수 있다.

---

# 3. Refusal and Redirection Rule

## 3.1 Refusal Rule Definition

### [개념]

Refusal Rule은 LLM이 안전하게 수행할 수 없는 요청을 거절하는 기준이다.

Refusal은 단순 거부가 아니라 위험한 부분을 명확히 제한하고, 가능한 경우 안전한 대체 방향을 제공하는 방식이어야 한다.

---

### [핵심]

- 위험한 요청은 수행하지 않는다.
- 거절 이유를 간결하게 설명한다.
- 가능한 경우 안전한 대체 작업을 제안한다.
- 합법적이고 방어적인 목적의 일반 정보는 제공할 수 있다.
- 사용자 의도가 불명확하면 위험한 세부 실행 절차를 제공하지 않는다.
- Refusal은 공격적이거나 비난하는 방식으로 작성하지 않는다.

---

### [실무]

Refusal Rule 예시:

```text
Refusal Rule:
If the request requires unsafe, harmful, illegal, or privacy-invasive instructions:
- Do not provide actionable harmful steps.
- Briefly explain the limitation.
- Provide a safe alternative if possible.
```

Safe Redirection 예시:

```text
Unsafe request:
보안 인증을 우회하는 방법 알려줘.

Safe response direction:
인증 우회 방법은 제공할 수 없음.
대신 안전한 인증 설계, 권한 검증 체크리스트, 취약점 방어 방법을 제공.
```

개발 프로젝트에서는 위험한 구현 대신 방어적 구현 방향으로 전환한다.

---

### [FAQ]

Q. Refusal Rule이 뭐야?

A. LLM이 안전하게 수행할 수 없는 요청을 거절하는 기준이다.

Q. 거절할 때 대체 답변을 줘야 해?

A. 가능하면 안전한 대체 방향을 제공하는 것이 좋다.

Q. 보안 관련 질문은 모두 거절해야 해?

A. 아니다. 공격적 실행 지시는 거절하고, 방어적 설계와 안전 점검은 제공할 수 있다.

Q. Refusal은 길게 설명해야 해?

A. 아니다. 짧게 이유를 말하고 안전한 대안을 제공하는 것이 좋다.

---

# 4. Unsafe Output Prevention

## 4.1 Unsafe Output Prevention Definition

### [개념]

Unsafe Output Prevention은 LLM이 위험한 코드, 보안 취약점, 비밀정보 노출, 개인정보 침해, 검증되지 않은 실행 절차를 출력하지 않도록 막는 Prompt 설계 방식이다.

---

### [핵심]

위험한 출력 예시:

- 인증 우회 코드
- 권한 검증 제거 코드
- 비밀번호 또는 토큰 로그 출력 코드
- 환경변수와 비밀키 노출
- 개인정보 무단 처리
- 악성 자동화 절차
- 검증되지 않은 운영 서버 명령
- 안전장치 제거 지시

방지 규칙:

- 비밀정보를 출력하지 않는다.
- 인증과 권한 검증을 우회하지 않는다.
- 보안 기능을 무력화하지 않는다.
- 위험한 실행 명령은 안전 검토 없이 제공하지 않는다.
- 운영 환경 변경은 검증 단계와 롤백 기준을 포함한다.

---

### [실무]

Unsafe Output Prevention Prompt 예시:

```text
Unsafe Output Prevention:
- Do not generate code that disables authentication or authorization.
- Do not log passwords, tokens, private keys, or session identifiers.
- Do not expose secrets in examples.
- Use placeholder values for credentials.
- Include validation and rollback steps for risky operations.
```

안전한 예시 값:

```text
DB_PASSWORD=<REDACTED>
JWT_SECRET=<REDACTED>
API_KEY=<YOUR_API_KEY>
```

나쁜 예시:

```text
JWT_SECRET=real-secret-value
```

좋은 예시:

```text
JWT_SECRET=<YOUR_JWT_SECRET>
```

---

### [FAQ]

Q. Unsafe Output Prevention이 뭐야?

A. LLM이 위험한 코드, 보안 취약점, 비밀정보 노출, 개인정보 침해 출력을 만들지 않도록 막는 Prompt 설계 방식이다.

Q. 코드 예시에 실제 API Key를 넣어도 돼?

A. 안 된다. `<YOUR_API_KEY>` 또는 `<REDACTED>` 같은 Placeholder를 사용해야 한다.

Q. 인증 검사를 끄는 코드는 생성해도 돼?

A. 일반적으로 안 된다. 테스트 목적이라도 위험성과 범위를 명확히 하고 안전한 대체 방법을 우선해야 한다.

Q. 운영 서버 명령은 어떻게 다뤄야 해?

A. 영향 범위, 백업, 롤백, 검증 단계를 함께 제공해야 한다.

---

# 5. Sensitive Information Handling

## 5.1 Sensitive Information Definition

### [개념]

Sensitive Information은 외부에 노출되면 보안, 개인정보, 계정, 시스템 안전에 문제가 생길 수 있는 정보다.

Prompt는 Sensitive Information을 보호하도록 설계해야 한다.

---

### [핵심]

Sensitive Information 예시:

- Password
- API Key
- Access Token
- Refresh Token
- JWT Secret
- Private Key
- Database Credential
- Session ID
- OAuth Client Secret
- 개인 식별 정보
- 내부 서버 주소
- 운영 배포 정보
- 보안 설정 값

처리 원칙:

- 출력하지 않는다.
- 로그로 남기지 않는다.
- 예시에는 Placeholder를 사용한다.
- 사용자가 제공한 비밀값은 재노출하지 않는다.
- 코드 리뷰에서는 노출 위험을 지적한다.
- 문서화 시 Secret 관리 원칙을 포함한다.

---

### [실무]

Sensitive Information Handling Prompt 예시:

```text
Sensitive Information Handling:
- Never expose secrets, tokens, passwords, private keys, or credentials.
- Replace secrets with placeholders such as <REDACTED>.
- If code logs sensitive data, mark it as a security issue.
- Do not include real secrets in examples.
```

Code Review Finding 예시:

```md
### 1. Secret Logging Risk

- Severity: Critical
- Problem: Token value may be logged.
- Cause: Authentication token is included in log output.
- Risk: Token leakage can allow unauthorized access.
- Fix Direction: Remove token from logs and use masked logging.
```

Sensitive Information은 Prompt, 코드 예시, 로그 분석, 문서 작성에서 모두 보호해야 한다.

---

### [FAQ]

Q. Sensitive Information은 뭐야?

A. 비밀번호, API Key, Token, Private Key, DB 계정처럼 노출되면 보안 문제가 생기는 정보다.

Q. 사용자가 비밀값을 제공하면 다시 출력해도 돼?

A. 안 된다. 필요한 경우 `<REDACTED>`로 마스킹해야 한다.

Q. 코드 리뷰에서 Secret이 보이면 어떻게 해야 해?

A. Critical 또는 High 보안 이슈로 표시하고 제거 또는 Secret Manager 사용을 제안해야 한다.

Q. 예시 코드에는 어떤 값을 써야 해?

A. 실제 값 대신 `<YOUR_API_KEY>`, `<REDACTED>` 같은 Placeholder를 사용한다.

---

# 6. Tool Use Prompt

## 6.1 Tool Use Prompt Definition

### [개념]

Tool Use Prompt는 LLM 또는 Agent가 외부 도구를 언제, 왜, 어떻게 사용할지 정의하는 Prompt다.

Tool은 검색, 파일 조회, 코드 실행, DB 조회, API 호출, 캘린더, 메일, 문서 생성 도구를 포함할 수 있다.

Tool Use Prompt는 도구 사용 조건, 입력, 출력 검증, 실패 처리, 결과 반영 방식을 정의해야 한다.

기본 구조:

```text
Tool Need
→ Tool Selection
→ Tool Input
→ Tool Execution
→ Tool Result Validation
→ Tool Failure Handling
→ Final Answer
```

---

### [핵심]

- 도구가 필요한 상황을 정의한다.
- 어떤 도구를 사용할지 기준을 정한다.
- 도구 입력값을 명확히 한다.
- 도구 결과를 검증한다.
- 도구 실패 시 지어내지 않는다.
- 도구 결과와 모델 추론을 구분한다.
- 최신 정보는 검색 도구가 필요할 수 있다.
- 파일 기반 작업은 제공된 파일을 우선 사용한다.
- 코드 실행 결과는 확인된 사실로 분리한다.

---

### [실무]

Tool Use Prompt 예시:

```text
Tool Use Rule:
- Use uploaded documents as primary context for document tasks.
- Use retrieval tools before general knowledge for project-specific answers.
- Use code execution only when validation or transformation is required.
- Validate tool results before using them.
- If tool output is insufficient or fails, state the limitation and do not invent results.
```

Agent Tool Use Prompt 예시:

```text
Tool Use:
- PM Agent may inspect project documents to create task briefs.
- Backend Agent may inspect uploaded code files before generating code.
- Review Agent must review provided code and retrieved rules before findings.
- If required files are missing, return Missing Information.
```

Tool Use Prompt는 Tool을 무조건 많이 쓰게 하는 것이 아니라, 필요한 경우 정확히 쓰게 하는 규칙이다.

---

### [FAQ]

Q. Tool Use Prompt가 뭐야?

A. LLM 또는 Agent가 외부 도구를 언제, 왜, 어떻게 사용할지 정의하는 Prompt다.

Q. Tool Use Prompt는 왜 필요해?

A. 도구 사용 기준, 결과 검증, 실패 처리를 명확히 해서 잘못된 도구 결과나 추정을 줄이기 위해 필요하다.

Q. 도구 결과를 그대로 믿어도 돼?

A. 아니다. 결과가 충분한지, 요청과 맞는지 검증해야 한다.

Q. 도구 실패 시 어떻게 해야 해?

A. 실패를 명확히 표시하고 결과를 지어내지 않아야 한다.

---

# 7. Tool Selection Rule

## 7.1 Tool Selection Rule Definition

### [개념]

Tool Selection Rule은 여러 도구 중 어떤 상황에서 어떤 도구를 사용할지 정하는 규칙이다.

Tool Selection이 잘못되면 불필요한 도구 호출, 잘못된 근거, 느린 Workflow가 발생할 수 있다.

---

### [핵심]

Tool 선택 기준:

- 최신 정보 필요 여부
- 프로젝트 문서 기반 여부
- 파일 분석 필요 여부
- 코드 실행 필요 여부
- 계산 필요 여부
- 외부 API 조회 필요 여부
- 사용자 데이터 접근 필요 여부
- 출력 파일 생성 필요 여부

도구 선택 원칙:

- 필요한 도구만 사용한다.
- 가장 신뢰할 수 있는 근거를 우선한다.
- 프로젝트 파일이 있으면 파일을 우선한다.
- 최신 정보는 검색 또는 공식 문서를 확인한다.
- 계산은 계산 도구를 사용한다.
- 추정으로 도구 결과를 대체하지 않는다.

---

### [실무]

Tool Selection Rule 예시:

```text
Tool Selection:
- Use file search for uploaded documents.
- Use code execution for validation, parsing, transformation, or file generation.
- Use web search for current, external, or rapidly changing information.
- Use calculator for arithmetic.
- Use document tools when creating downloadable documents.
- Use no tool when the answer is fully covered by provided context.
```

RAG Agent Tool Selection 예시:

```text
If the user asks about uploaded project rules:
- Use retrieved project documents.
- Do not rely only on general knowledge.
- If retrieval is insufficient, mark Missing Information.
```

Tool Selection Rule은 Agent가 언제 내부 지식으로 답하고 언제 도구를 써야 하는지 구분하게 한다.

---

### [FAQ]

Q. Tool Selection Rule이 뭐야?

A. 여러 도구 중 어떤 상황에서 어떤 도구를 사용할지 정하는 규칙이다.

Q. 항상 도구를 쓰는 게 좋아?

A. 아니다. 제공된 Context로 충분하면 도구가 필요하지 않다.

Q. 최신 정보가 필요한 경우는 어떻게 해?

A. 검색 도구나 공식 문서를 확인해야 한다.

Q. 프로젝트 파일이 제공된 경우는 어떻게 해?

A. 일반 지식보다 제공된 파일과 검색된 문서 내용을 우선해야 한다.

---

# 8. Tool Input Rule

## 8.1 Tool Input Rule Definition

### [개념]

Tool Input Rule은 도구에 전달할 입력값을 정확하고 안전하게 구성하는 규칙이다.

Tool Input이 부정확하면 Tool Output도 부정확해진다.

---

### [핵심]

- 도구 입력은 최소 필요 정보로 구성한다.
- 파일 경로나 식별자를 정확히 사용한다.
- 검색 Query는 구체적으로 작성한다.
- 민감정보를 도구 입력에 불필요하게 포함하지 않는다.
- 코드 실행 입력은 안전한 범위로 제한한다.
- 외부 API 호출은 필요한 파라미터를 명확히 한다.
- 모호한 입력은 Missing Information으로 표시한다.

---

### [실무]

검색 Tool Input 예시:

```text
Good Query:
Spring Boot 3.x SecurityFilterChain JWT authentication official docs

Bad Query:
Spring security thing
```

파일 기반 Tool Input 예시:

```text
Use:
- Provided file path
- Target file name
- Specific search keyword
- Relevant section title
```

코드 실행 Tool Input 예시:

```text
Use code execution only for:
- Parsing
- Formatting
- Validation
- File creation
- Safe local transformation
```

Tool Input은 도구가 정확히 처리할 수 있는 형태로 구조화해야 한다.

---

### [FAQ]

Q. Tool Input Rule이 뭐야?

A. 도구에 전달할 입력값을 정확하고 안전하게 구성하는 규칙이다.

Q. Tool Input이 왜 중요해?

A. 입력이 부정확하면 도구 결과도 부정확해지기 때문이다.

Q. 검색 Query는 어떻게 작성해야 해?

A. 핵심 기술명, 버전, 목적, 공식 문서 여부를 포함해 구체적으로 작성해야 한다.

Q. Tool Input에 비밀값을 넣어도 돼?

A. 불필요하게 넣으면 안 된다. 필요한 경우 마스킹하거나 Placeholder를 사용해야 한다.

---

# 9. Tool Result Validation

## 9.1 Tool Result Validation Definition

### [개념]

Tool Result Validation은 도구가 반환한 결과가 요청에 맞고 충분하며 신뢰 가능한지 확인하는 과정이다.

Tool 결과는 항상 완전하거나 정확하다고 가정하면 안 된다.

---

### [핵심]

검증 기준:

- 요청한 정보와 일치하는가?
- 최신성이 필요한 경우 최신 정보인가?
- 출처가 신뢰 가능한가?
- 결과가 충분한가?
- 다른 근거와 충돌하지 않는가?
- 파일 내용과 일치하는가?
- 코드 실행 결과가 재현 가능한가?
- 오류나 실패 메시지가 포함되어 있지 않은가?

---

### [실무]

Tool Result Validation Prompt 예시:

```text
After using a tool:
- Check whether the result directly answers the task.
- Check whether the result is sufficient.
- Check whether the result conflicts with provided context.
- If the result is incomplete, state Missing Information.
- Do not overgeneralize tool results.
```

RAG Tool Result 검증 예시:

```md
## Retrieved Context Validation

- Query matched user question: Yes / No
- Retrieved section relevant: Yes / No
- Context sufficient: Yes / No
- Missing Information:
```

도구 결과가 부족하면 부족하다고 표시하고, 일반 추정으로 메우지 않는다.

---

### [FAQ]

Q. Tool Result Validation이 뭐야?

A. 도구가 반환한 결과가 요청에 맞고 충분하며 신뢰 가능한지 확인하는 과정이다.

Q. Tool 결과는 항상 믿어도 돼?

A. 아니다. 요청과의 관련성, 충분성, 신뢰성, 충돌 여부를 확인해야 한다.

Q. Tool 결과가 부족하면 어떻게 해?

A. Missing Information으로 표시하고 지어내지 않아야 한다.

Q. RAG 검색 결과도 검증해야 해?

A. 그렇다. 검색된 Chunk가 질문과 맞는지, 답변에 충분한지 확인해야 한다.

---

# 10. Tool Failure Handling

## 10.1 Tool Failure Handling Definition

### [개념]

Tool Failure Handling은 도구 호출이 실패하거나 결과가 불완전할 때 LLM이 어떻게 대응해야 하는지 정의하는 규칙이다.

Tool 실패 상황에서 가장 중요한 원칙은 결과를 지어내지 않는 것이다.

---

### [핵심]

Tool Failure 유형:

- 검색 결과 없음
- 파일 조회 실패
- 코드 실행 실패
- API 호출 실패
- 권한 부족
- 잘못된 입력
- 시간 초과
- 결과 불완전
- 형식 오류

대응 원칙:

- 실패를 명확히 표시한다.
- 가능한 원인을 구분한다.
- 안전한 범위에서 부분 결과를 제공한다.
- 필요한 추가 정보를 표시한다.
- Tool 결과를 임의 생성하지 않는다.
- 재시도 가능 조건을 구분한다.

---

### [실무]

Tool Failure Handling Prompt 예시:

```text
Tool Failure Handling:
If a tool fails or returns insufficient results:
- State what failed.
- State what information is missing.
- Do not invent tool results.
- Provide partial output only if safe.
- Mark assumptions clearly.
```

RAG 검색 실패 예시:

```md
## Missing Information

- Retrieved context does not include the requested API rule.
- The target file or section was not found.
- Additional project document is required.
```

코드 실행 실패 예시:

```md
## Tool Failure

- Code execution failed.
- Error message indicates missing dependency.
- Result cannot be confirmed from execution.
```

Tool 실패는 답변 실패가 아니라, 근거 범위 제한으로 처리한다.

---

### [FAQ]

Q. Tool Failure Handling이 뭐야?

A. 도구 호출이 실패하거나 결과가 불완전할 때 어떻게 대응해야 하는지 정의하는 규칙이다.

Q. Tool 실패 시 결과를 추정해도 돼?

A. 확정하면 안 된다. 실패와 부족한 정보를 명확히 표시해야 한다.

Q. Tool 실패 후에도 답변할 수 있어?

A. 안전한 범위에서는 부분 답변을 제공할 수 있지만 한계를 명확히 표시해야 한다.

Q. RAG 검색 실패는 어떻게 처리해?

A. 검색 결과가 부족하다고 표시하고 필요한 문서나 섹션을 Missing Information으로 작성한다.

---

# 11. Function Calling Prompt

## 11.1 Function Calling Prompt Definition

### [개념]

Function Calling Prompt는 LLM이 정해진 함수 Schema에 맞춰 호출 의도를 만들고, 필요한 인자를 구조화하도록 설계하는 Prompt다.

Function Calling은 자연어 답변보다 엄격한 입력 구조와 검증이 중요하다.

기본 구조:

```text
Function Purpose
→ Required Arguments
→ Optional Arguments
→ Argument Validation
→ Tool Execution
→ Result Validation
→ Final Response
```

---

### [핵심]

- 함수 목적을 명확히 한다.
- Required Argument를 명확히 한다.
- Optional Argument를 구분한다.
- Enum 값은 허용된 값만 사용한다.
- 없는 인자는 지어내지 않는다.
- 모호한 값은 Missing Information으로 표시한다.
- 함수 결과와 최종 답변을 분리한다.
- 실패 시 Tool Failure Handling을 적용한다.

---

### [실무]

Function Calling Prompt 예시:

```text
Function Calling Rules:
- Use the function only when it directly supports the task.
- Provide all required arguments.
- Do not invent missing arguments.
- Use only allowed enum values.
- Validate function result before final answer.
- If required argument is missing, state Missing Information.
```

Function Argument 검증 예시:

```md
## Argument Validation

- Required arguments present: Yes / No
- Enum values valid: Yes / No
- Ambiguous values: Yes / No
- Missing Information:
```

Function Calling Prompt는 Agent 자동화와 Tool Calling 안정성에 중요하다.

---

### [FAQ]

Q. Function Calling Prompt가 뭐야?

A. LLM이 정해진 함수 Schema에 맞춰 호출 의도와 인자를 구조화하도록 설계하는 Prompt다.

Q. Function Calling에서 가장 중요한 것은 뭐야?

A. Required Argument, 허용 Enum, 인자 검증, 결과 검증이다.

Q. 인자가 부족하면 어떻게 해?

A. 지어내지 말고 Missing Information으로 표시해야 한다.

Q. 함수 결과를 그대로 답변해도 돼?

A. 결과를 검증한 뒤 사용자 요청에 맞게 정리해야 한다.

---

# 12. Tool Calling Prompt

## 12.1 Tool Calling Prompt Definition

### [개념]

Tool Calling Prompt는 LLM이 외부 Tool을 호출해 정보를 조회하거나 작업을 수행하도록 설계하는 Prompt다.

Function Calling이 정해진 함수 호출 구조에 초점을 둔다면, Tool Calling은 도구 선택, 실행, 결과 검증, 실패 처리까지 포함한다.

---

### [핵심]

- Tool이 필요한지 판단한다.
- 적절한 Tool을 선택한다.
- Tool Input을 구성한다.
- Tool Result를 검증한다.
- Tool Failure를 처리한다.
- Tool 결과와 LLM 추론을 구분한다.
- 최종 답변은 Tool 결과에 근거한다.
- Tool 결과가 부족하면 Missing Information을 표시한다.

---

### [실무]

Tool Calling Prompt 예시:

```text
Tool Calling Workflow:
1. Determine whether a tool is needed.
2. Select the appropriate tool.
3. Prepare safe and precise tool input.
4. Execute the tool.
5. Validate tool result.
6. Handle tool failure if needed.
7. Produce final answer grounded in tool result.
```

Tool Calling Guardrail 예시:

```text
Tool Calling Guardrails:
- Do not call tools unnecessarily.
- Do not invent tool results.
- Do not pass sensitive data unless required and safe.
- Do not treat incomplete tool output as complete.
- Preserve missing information.
```

Tool Calling Prompt는 최신 정보, 파일 분석, 코드 검증, 문서 생성 작업에 필요하다.

---

### [FAQ]

Q. Tool Calling Prompt가 뭐야?

A. LLM이 외부 Tool을 호출해 정보를 조회하거나 작업을 수행하도록 설계하는 Prompt다.

Q. Tool Calling과 Function Calling은 어떻게 달라?

A. Function Calling은 정해진 함수 Schema 호출에 초점이 있고, Tool Calling은 도구 선택, 실행, 결과 검증, 실패 처리까지 포함한다.

Q. Tool Calling에서 가장 중요한 것은 뭐야?

A. Tool 선택 기준, 안전한 입력, 결과 검증, 실패 처리다.

Q. Tool을 많이 쓰면 더 좋은 답변이 나와?

A. 아니다. 필요한 경우에만 정확한 도구를 사용하는 것이 좋다.

---

# 13. Tool Use in Agent Workflow

## 13.1 Agent Tool Use

### [개념]

Agent Tool Use는 Multi-Agent Workflow에서 Agent별로 사용할 수 있는 도구와 사용 기준을 정의하는 방식이다.

모든 Agent가 모든 Tool을 자유롭게 사용하는 구조는 불안정하다.

Agent 역할에 따라 Tool 권한과 사용 목적을 제한해야 한다.

---

### [핵심]

Agent별 Tool Use 기준:

- PM Agent: 문서 조회, 요구사항 정리, Handoff 생성
- Backend Agent: 코드 파일 조회, RAG 문서 조회, 제한적 코드 검증
- Frontend Agent: 컴포넌트 코드 조회, API 스펙 조회
- Review Agent: 산출물 검토, 규칙 조회, 형식 검증
- DevOps Agent: 설정 파일 조회, 배포 규칙 조회
- AI/ML Agent: RAG 설정, Prompt, Agent Workflow 문서 조회
- Fix Agent: Review Findings와 원본 산출물 비교

---

### [실무]

Agent Tool Use Matrix 예시:

```md
| Agent         | Tool Use Purpose           | Restriction              |
| ------------- | -------------------------- | ------------------------ |
| PM Agent      | 문서 조회, Task Brief 생성 | 구현 코드 직접 생성 제한 |
| Backend Agent | 코드/문서 조회, 구현 검증  | Frontend 수정 제한       |
| Review Agent  | 산출물 검수, 규칙 조회     | 임의 전체 재작성 제한    |
| Fix Agent     | Findings 반영              | 새 요구사항 추가 금지    |
```

Agent Tool Use Prompt 예시:

```text
Agent Tool Use:
- Each Agent may use tools only within its responsibility.
- Tool results must be validated before use.
- Missing tool results must be preserved in Handoff.
- Agents must not invent results when tool access fails.
```

Agent Tool Use는 역할 분리와 Handoff 안정성에 중요하다.

---

### [FAQ]

Q. Agent Tool Use가 뭐야?

A. Multi-Agent Workflow에서 Agent별로 사용할 수 있는 도구와 사용 기준을 정의하는 방식이다.

Q. 모든 Agent가 모든 Tool을 써도 돼?

A. 권장하지 않는다. Agent 책임에 맞게 Tool 사용 범위를 제한해야 한다.

Q. Review Agent는 어떤 Tool을 써야 해?

A. 산출물, 프로젝트 규칙, RAG 문서, 형식 검증 도구를 사용할 수 있다.

Q. Tool 결과는 Handoff에 포함해야 해?

A. 필요한 경우 포함해야 하며, 부족하거나 실패한 결과도 Missing Information으로 전달해야 한다.

---

# 14. Policy Priority and Conflict Resolution

## 14.1 Priority Rule Definition

### [개념]

Policy Priority and Conflict Resolution은 Prompt 규칙, 사용자 요청, 프로젝트 규칙, Tool 결과가 충돌할 때 무엇을 우선할지 정하는 규칙이다.

충돌 처리 기준이 없으면 LLM 출력이 일관되지 않거나 안전하지 않을 수 있다.

---

### [핵심]

우선순위 예시:

```text
1. Safety and policy constraints
2. System / Developer rules
3. Project Master Rules
4. Domain Rules
5. Retrieved Context
6. User Request
7. Style Preference
```

원칙:

- 안전 규칙은 사용자 선호보다 우선한다.
- 프로젝트 규칙은 일반 지식보다 우선한다.
- Domain Rules는 해당 도메인 작업에 우선 적용한다.
- Retrieved Context는 RAG 답변에서 일반 지식보다 우선한다.
- Style Preference는 필수 제약보다 낮다.
- 충돌이 있으면 충돌 내용을 명확히 표시한다.

---

### [실무]

Conflict Resolution Prompt 예시:

```text
Conflict Resolution:
- If user request conflicts with safety rules, follow safety rules.
- If general knowledge conflicts with retrieved project documents, follow retrieved project documents.
- If style preference conflicts with required output format, follow required output format.
- If two project documents conflict, follow the higher-priority document and state the conflict.
```

RAG 문서 제작 우선순위:

```text
1. MASTER_RAG_RULES
2. DOMAIN_RULES
3. PROJECT_PROGRESS
4. User Request
5. General Knowledge
```

Policy Priority는 Agent Workflow 전체의 일관성을 유지한다.

---

### [FAQ]

Q. Policy Priority가 뭐야?

A. 여러 Prompt 규칙, 프로젝트 규칙, 사용자 요청, Tool 결과가 충돌할 때 무엇을 우선할지 정하는 기준이다.

Q. 사용자 요청과 안전 규칙이 충돌하면 무엇을 따라야 해?

A. 안전 규칙을 따라야 한다.

Q. 프로젝트 문서와 일반 지식이 다르면 무엇을 따라야 해?

A. 프로젝트 RAG 작업에서는 프로젝트 문서와 Domain Rules를 우선해야 한다.

Q. 충돌이 있으면 어떻게 답해야 해?

A. 어떤 규칙이 충돌하는지 표시하고 우선순위가 높은 규칙을 적용해야 한다.

---

# 15. Safety and Tool Use Prompt Patterns

## 15.1 Safe Code Generation Pattern

### [개념]

Safe Code Generation Pattern은 코드 생성 시 보안, 권한, 비밀정보, 예외 처리, 검증 기준을 함께 적용하는 Prompt 패턴이다.

---

### [핵심]

- 인증과 권한 검증을 우회하지 않는다.
- 비밀정보를 하드코딩하지 않는다.
- 민감정보를 로그로 남기지 않는다.
- 입력 검증을 고려한다.
- 예외 처리 기준을 포함한다.
- 보안 관련 Missing Information을 표시한다.
- 안전한 Placeholder를 사용한다.

---

### [실무]

Safe Code Generation Prompt:

```text
Generate code using the provided project context.

Safety Rules:
- Do not hardcode secrets.
- Do not log passwords, tokens, or private keys.
- Do not bypass authentication or authorization.
- Use placeholders for credentials.
- Mark missing security requirements as Missing Information.

Output:
## Missing Information
## Security Assumptions
## Implementation Plan
## Code Snippet
## Security Checklist
```

Security Checklist 예시:

```md
### [Security Checklist]

- [ ] Secret 하드코딩 없음
- [ ] 민감정보 로그 출력 없음
- [ ] 인증 우회 없음
- [ ] 권한 검증 누락 없음
- [ ] 입력 검증 고려
- [ ] 예외 메시지 민감정보 노출 없음
```

---

### [FAQ]

Q. Safe Code Generation Pattern이 뭐야?

A. 코드 생성 시 보안, 권한, 비밀정보, 예외 처리, 검증 기준을 함께 적용하는 Prompt 패턴이다.

Q. 코드 생성에서 보안상 가장 조심할 점은 뭐야?

A. Secret 하드코딩, 인증 우회, 권한 검증 누락, 민감정보 로그 출력이다.

Q. 보안 요구사항이 없으면 어떻게 해?

A. Missing Information으로 표시하고 안전한 기본 원칙을 적용해야 한다.

---

## 15.2 Safe Tool Calling Pattern

### [개념]

Safe Tool Calling Pattern은 Tool 사용 시 입력, 실행, 결과 검증, 실패 처리를 안전하게 수행하는 Prompt 패턴이다.

---

### [핵심]

- Tool 필요성을 먼저 판단한다.
- 민감정보를 불필요하게 Tool Input에 넣지 않는다.
- Tool Input을 최소화한다.
- Tool Output을 검증한다.
- Tool 실패 시 결과를 지어내지 않는다.
- Tool 결과와 Assumption을 분리한다.
- 최종 답변은 검증된 Tool 결과에 기반한다.

---

### [실무]

Safe Tool Calling Prompt:

```text
Safe Tool Calling:
1. Decide whether a tool is required.
2. Use the minimum necessary input.
3. Do not include secrets unless strictly required and safe.
4. Validate the tool result.
5. If the tool fails, state the failure and missing information.
6. Do not invent tool results.
7. Use validated results in the final answer.
```

Tool Result Output 예시:

```md
## Tool Result Summary

## Confirmed by Tool

## Missing Information

## Assumptions

## Final Answer
```

Safe Tool Calling은 Agent의 신뢰성과 재현성을 높인다.

---

### [FAQ]

Q. Safe Tool Calling Pattern이 뭐야?

A. Tool 사용 시 입력, 실행, 결과 검증, 실패 처리를 안전하게 수행하는 Prompt 패턴이다.

Q. Tool Input은 어떻게 구성해야 해?

A. 목적 달성에 필요한 최소 정보만 포함하고 민감정보는 피해야 한다.

Q. Tool 실패 시 어떻게 해?

A. 실패와 부족한 정보를 표시하고 결과를 지어내지 않아야 한다.

---

## 15.3 Guarded RAG Answer Pattern

### [개념]

Guarded RAG Answer Pattern은 RAG 답변에서 안전 규칙, Grounding Rule, Missing Information Rule, Assumption Rule을 함께 적용하는 Prompt 패턴이다.

---

### [핵심]

- Retrieved Context를 우선 사용한다.
- 문서에 없는 정보는 확정하지 않는다.
- 안전하지 않은 요청은 제한한다.
- 프로젝트 고유 정보는 지어내지 않는다.
- Assumption을 분리한다.
- Missing Information을 표시한다.
- 최종 답변은 근거 기반으로 작성한다.

---

### [실무]

Guarded RAG Answer Prompt:

```text
You are a Guarded RAG Answer Agent.

Rules:
- Use retrieved context first.
- Follow safety and project guardrails.
- Do not invent project-specific facts.
- If retrieved context is insufficient, state Missing Information.
- Mark assumptions clearly.
- If the request is unsafe, provide a safe alternative.

Output:
## Answer
## Confirmed by Context
## Assumptions
## Missing Information
## Safety Notes
```

Guarded RAG Answer는 프로젝트 문서 기반 QA, 코드 리뷰, Agent Output 검증에 적합하다.

---

### [FAQ]

Q. Guarded RAG Answer Pattern이 뭐야?

A. RAG 답변에 Safety, Grounding, Missing Information, Assumption 규칙을 함께 적용하는 Prompt 패턴이다.

Q. RAG 답변에도 Safety가 필요해?

A. 필요하다. 문서 기반 답변이라도 위험한 코드, 비밀정보, 권한 우회 지시가 포함될 수 있기 때문이다.

Q. Guarded RAG Answer에서 가장 중요한 것은 뭐야?

A. Retrieved Context 우선, 안전 경계 준수, Missing Information 표시, Assumption 분리다.

---

# 16. Common Mistakes

## 16.1 Safety Prompt Mistakes

### [개념]

Safety Prompt Mistake는 안전 규칙이 모호하거나, 거절 기준이 없거나, 안전한 대체 방향이 없는 문제다.

---

### [핵심]

자주 발생하는 실수:

- “안전하게 답해”만 작성
- 금지 범위가 없음
- Refusal Rule 없음
- Safe Alternative 없음
- 비밀정보 처리 규칙 없음
- 보안 취약 코드 방지 규칙 없음
- 운영 환경 변경 검증 기준 없음
- 안전 규칙과 사용자 요청 충돌 처리 없음

---

### [실무]

나쁜 Safety Prompt:

```text
Answer safely.
```

개선 Safety Prompt:

```text
Safety Rules:
- Do not expose secrets or credentials.
- Do not generate code that bypasses authentication or authorization.
- If the request is unsafe, explain the limitation briefly.
- Provide a safe alternative such as defensive design, validation checklist, or secure configuration guidance.
```

Safety Prompt는 구체적인 위험 유형과 대응 방식을 포함해야 한다.

---

### [FAQ]

Q. Safety Prompt에서 가장 흔한 실수는 뭐야?

A. “안전하게 답해”처럼 모호하게 작성하고 구체적인 금지 범위와 대체 방향을 넣지 않는 것이다.

Q. Safety Prompt에는 Safe Alternative가 필요해?

A. 필요하다. 위험한 요청을 거절하더라도 안전한 방향으로 도움을 줄 수 있어야 한다.

---

## 16.2 Guardrail Prompt Mistakes

### [개념]

Guardrail Prompt Mistake는 범위, 출력 형식, Tool 사용, 실패 처리 경계가 불명확해 Agent가 책임 밖 작업을 수행하는 문제다.

---

### [핵심]

자주 발생하는 실수:

- Scope Boundary 없음
- Output Boundary 없음
- Tool Boundary 없음
- Failure Boundary 없음
- Agent별 책임 경계 없음
- 충돌 처리 우선순위 없음
- 너무 많은 Guardrail로 작업 수행 방해
- Guardrail과 Task가 충돌함

---

### [실무]

나쁜 Guardrail Prompt:

```text
Always follow all rules and do everything perfectly.
```

개선 Guardrail Prompt:

```text
Guardrails:
- Stay within assigned Agent scope.
- Follow required output format.
- Use tools only when needed.
- Do not invent missing information.
- If rules conflict, follow safety rules and project master rules first.
```

Guardrail은 작업을 막는 장벽이 아니라 작업을 안전하고 일관되게 수행하는 경계다.

---

### [FAQ]

Q. Guardrail Prompt에서 가장 흔한 실수는 뭐야?

A. Scope, Output, Tool, Failure 경계를 명확히 정하지 않는 것이다.

Q. Guardrail이 너무 많으면 어떻게 돼?

A. 모델이 과도하게 방어적으로 답하거나 핵심 작업을 수행하지 못할 수 있다.

---

## 16.3 Tool Use Prompt Mistakes

### [개념]

Tool Use Prompt Mistake는 도구 사용 기준, 입력 규칙, 결과 검증, 실패 처리가 없어 Tool 결과를 잘못 사용하는 문제다.

---

### [핵심]

자주 발생하는 실수:

- 필요 없는 Tool 사용
- 필요한 Tool 미사용
- Tool Input이 모호함
- 민감정보를 Tool Input에 포함
- Tool Output을 검증하지 않음
- Tool 실패 결과를 지어냄
- Tool 결과와 모델 추론을 섞음
- 오래된 Tool 결과를 최신 사실처럼 사용

---

### [실무]

나쁜 Tool Use Prompt:

```text
필요하면 아무 도구나 사용해.
```

개선 Tool Use Prompt:

```text
Tool Use:
- Use tools only when needed.
- Select the tool based on task type.
- Use precise and safe input.
- Validate tool results.
- If the tool fails or result is insufficient, state Missing Information.
- Do not invent tool results.
```

Tool Use Prompt는 Tool 호출 자체보다 Tool 결과 검증이 중요하다.

---

### [FAQ]

Q. Tool Use Prompt에서 가장 흔한 실수는 뭐야?

A. Tool 사용 기준과 결과 검증 기준 없이 도구를 사용하게 하는 것이다.

Q. Tool 결과와 모델 추론을 섞으면 왜 문제야?

A. 확인된 사실과 추정이 구분되지 않아 잘못된 결론을 만들 수 있기 때문이다.

Q. Tool 실패 결과를 추정해도 돼?

A. 확정하면 안 된다. 실패와 부족한 정보를 표시해야 한다.

---

## 16.4 Function Calling Mistakes

### [개념]

Function Calling Mistake는 함수 Schema, Required Argument, Enum, 결과 검증을 제대로 처리하지 않아 잘못된 호출이나 잘못된 후속 답변이 발생하는 문제다.

---

### [핵심]

자주 발생하는 실수:

- Required Argument 누락
- 없는 인자 임의 생성
- 허용되지 않은 Enum 사용
- 모호한 값을 확정
- 함수 호출이 필요 없는 상황에서 호출
- 함수 결과 검증 없음
- 실패 결과를 성공처럼 처리
- 함수 결과와 최종 답변 불일치

---

### [실무]

Function Calling Guardrail 예시:

```text
Function Calling Guardrails:
- Call the function only when required.
- Provide all required arguments.
- Use only allowed enum values.
- Do not invent missing argument values.
- If required information is missing, state Missing Information.
- Validate function result before final response.
```

Function Calling은 엄격한 Schema 준수가 중요하다.

---

### [FAQ]

Q. Function Calling에서 가장 흔한 실수는 뭐야?

A. Required Argument 누락, 허용되지 않은 Enum 사용, 없는 인자 임의 생성이다.

Q. 모호한 인자는 어떻게 처리해야 해?

A. 확정하지 말고 Missing Information으로 표시해야 한다.

Q. 함수 결과가 실패했는데 성공처럼 답하면 안 돼?

A. 안 된다. 실패를 명확히 표시하고 결과를 지어내지 않아야 한다.

---

# 17. Best Practice

## 17.1 Safety and Guardrail Best Practice

### [개념]

Safety and Guardrail Best Practice는 LLM이 안전하고 일관된 범위 안에서 작업하도록 안전 규칙과 행동 경계를 함께 설계하는 원칙이다.

---

### [핵심]

- 허용 범위와 금지 범위를 구분한다.
- Refusal Rule을 포함한다.
- Safe Alternative를 포함한다.
- Sensitive Information Handling을 포함한다.
- 인증, 권한, Secret 관련 위험을 제한한다.
- Scope Boundary를 명시한다.
- Output Boundary를 명시한다.
- Failure Boundary를 명시한다.
- 충돌 처리 우선순위를 포함한다.
- Agent별 책임 경계를 유지한다.

---

### [실무]

Safety and Guardrail Template:

```text
Safety and Guardrails:

Allowed:
- [Allowed task types]

Disallowed:
- [Unsafe or out-of-scope task types]

Sensitive Information:
- Do not expose secrets, tokens, passwords, private keys, or credentials.
- Use placeholders such as <REDACTED>.

Refusal:
- If the request is unsafe, briefly explain the limitation and provide a safe alternative.

Scope:
- Stay within the assigned role and task scope.

Output:
- Follow the requested output format.

Failure:
- If information is missing, state Missing Information and do not invent facts.
```

이 Template은 RAG Agent, Code Agent, Review Agent, Multi-Agent Workflow에 공통 적용 가능하다.

---

### [FAQ]

Q. Safety and Guardrail Best Practice는 뭐야?

A. 허용 범위, 금지 범위, 비밀정보 처리, 거절 규칙, Scope, Output, Failure 경계를 명확히 설계하는 것이다.

Q. Safety와 Guardrail은 함께 써야 해?

A. 함께 쓰는 것이 좋다. Safety는 위험 방지, Guardrail은 범위와 형식 제어까지 담당한다.

---

## 17.2 Tool Use Best Practice

### [개념]

Tool Use Best Practice는 Agent가 필요한 도구를 정확히 선택하고, 안전한 입력을 사용하며, 결과를 검증하고, 실패를 올바르게 처리하도록 설계하는 원칙이다.

---

### [핵심]

- Tool 필요성을 먼저 판단한다.
- 작업 유형에 맞는 Tool을 선택한다.
- Tool Input을 최소화하고 구체화한다.
- 민감정보 입력을 피한다.
- Tool Result를 검증한다.
- Tool Failure를 명확히 처리한다.
- Tool 결과와 Assumption을 분리한다.
- Tool 결과를 과도하게 일반화하지 않는다.
- 최종 답변은 검증된 결과에 근거한다.

---

### [실무]

Tool Use Best Practice Template:

```text
Tool Use Workflow:
1. Determine whether a tool is needed.
2. Select the tool based on task type.
3. Prepare safe and precise input.
4. Execute the tool.
5. Validate the result.
6. Handle failure or insufficient result.
7. Use validated result in final output.

Rules:
- Do not invent tool results.
- Do not pass secrets unnecessarily.
- Preserve Missing Information.
```

Tool Use는 “도구 호출”보다 “도구 결과 검증”이 핵심이다.

---

### [FAQ]

Q. Tool Use Best Practice는 뭐야?

A. Tool 필요성 판단, Tool 선택, 안전한 입력, 결과 검증, 실패 처리를 명확히 하는 것이다.

Q. Tool Use에서 가장 중요한 단계는 뭐야?

A. Tool Result Validation과 Tool Failure Handling이다.

Q. Tool을 사용하지 않아도 되는 경우는 언제야?

A. 제공된 Context만으로 충분히 답변 가능하고 최신 정보나 외부 검증이 필요 없을 때다.

---

## 17.3 Function Calling Best Practice

### [개념]

Function Calling Best Practice는 정해진 함수 Schema를 정확히 따르고, 필요한 인자를 검증하며, 결과를 확인한 뒤 최종 답변에 반영하는 원칙이다.

---

### [핵심]

- 함수 목적을 명확히 이해한다.
- Required Argument를 누락하지 않는다.
- Optional Argument를 구분한다.
- Enum은 허용 값만 사용한다.
- 모호한 인자는 확정하지 않는다.
- 없는 인자를 지어내지 않는다.
- 함수 호출 전 입력을 검증한다.
- 함수 호출 후 결과를 검증한다.
- 실패 시 Tool Failure Handling을 적용한다.

---

### [실무]

Function Calling Best Practice Template:

```text
Function Calling:
- Call the function only if it directly supports the task.
- Validate required arguments before calling.
- Use only allowed enum values.
- Do not invent missing arguments.
- Validate the function result.
- If the function fails, state the failure and missing information.
```

Function Calling은 자동화 Workflow에서 오류 전파를 막기 위해 엄격하게 설계해야 한다.

---

### [FAQ]

Q. Function Calling Best Practice는 뭐야?

A. 함수 Schema, Required Argument, Enum, 입력 검증, 결과 검증, 실패 처리를 정확히 수행하는 것이다.

Q. 인자가 부족하면 함수 호출을 해야 해?

A. 필요한 인자가 없으면 호출하지 않거나 Missing Information을 표시해야 한다.

Q. Function Calling 결과는 어떻게 사용해야 해?

A. 결과를 검증한 뒤 최종 답변에 반영해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Safety Prompt가 뭐야?
A. LLM이 위험하거나 부적절하거나 검증되지 않은 출력을 생성하지 않도록 제어하는 Prompt다.

Q. Safety Prompt는 왜 필요해?
A. 보안 취약 코드, 비밀정보 노출, 위험한 지시, 근거 없는 확정을 줄이기 위해 필요하다.

Q. Guardrail Prompt가 뭐야?
A. LLM이 정해진 정책, 범위, 출력 형식, 안전 기준을 벗어나지 않도록 경계를 설정하는 Prompt다.

Q. Safety Prompt와 Guardrail Prompt는 어떻게 달라?
A. Safety Prompt는 위험 방지 중심이고, Guardrail Prompt는 안전, 범위, 출력, 도구, 실패 처리 경계까지 포함한다.

Q. Refusal Rule이 뭐야?
A. LLM이 안전하게 수행할 수 없는 요청을 거절하는 기준이다.

Q. 안전하지 않은 요청은 어떻게 처리해?
A. 위험한 부분은 거절하고 가능한 경우 안전한 대체 방향을 제공한다.

Q. Unsafe Output Prevention이 뭐야?
A. LLM이 위험한 코드, 보안 취약점, 비밀정보 노출, 개인정보 침해 출력을 만들지 않도록 막는 Prompt 설계 방식이다.

Q. Sensitive Information은 뭐야?
A. 비밀번호, API Key, Token, Private Key, DB 계정처럼 노출되면 보안 문제가 생기는 정보다.

Q. 사용자가 비밀값을 제공하면 다시 출력해도 돼?
A. 안 된다. 필요한 경우 `<REDACTED>`로 마스킹해야 한다.

Q. Tool Use Prompt가 뭐야?
A. LLM 또는 Agent가 외부 도구를 언제, 왜, 어떻게 사용할지 정의하는 Prompt다.

Q. Tool Use Prompt는 왜 필요해?
A. 도구 사용 기준, 결과 검증, 실패 처리를 명확히 해서 잘못된 도구 결과나 추정을 줄이기 위해 필요하다.

Q. Tool Selection Rule이 뭐야?
A. 여러 도구 중 어떤 상황에서 어떤 도구를 사용할지 정하는 규칙이다.

Q. 항상 도구를 쓰는 게 좋아?
A. 아니다. 제공된 Context로 충분하면 도구가 필요하지 않다.

Q. Tool Input Rule이 뭐야?
A. 도구에 전달할 입력값을 정확하고 안전하게 구성하는 규칙이다.

Q. Tool Input에 비밀값을 넣어도 돼?
A. 불필요하게 넣으면 안 된다. 필요한 경우 마스킹하거나 Placeholder를 사용해야 한다.

Q. Tool Result Validation이 뭐야?
A. 도구가 반환한 결과가 요청에 맞고 충분하며 신뢰 가능한지 확인하는 과정이다.

Q. Tool 결과는 항상 믿어도 돼?
A. 아니다. 요청과의 관련성, 충분성, 신뢰성, 충돌 여부를 확인해야 한다.

Q. Tool Failure Handling이 뭐야?
A. 도구 호출이 실패하거나 결과가 불완전할 때 어떻게 대응해야 하는지 정의하는 규칙이다.

Q. Tool 실패 시 결과를 추정해도 돼?
A. 확정하면 안 된다. 실패와 부족한 정보를 명확히 표시해야 한다.

Q. Function Calling Prompt가 뭐야?
A. LLM이 정해진 함수 Schema에 맞춰 호출 의도와 인자를 구조화하도록 설계하는 Prompt다.

Q. Function Calling에서 가장 중요한 것은 뭐야?
A. Required Argument, 허용 Enum, 인자 검증, 결과 검증이다.

Q. Tool Calling Prompt가 뭐야?
A. LLM이 외부 Tool을 호출해 정보를 조회하거나 작업을 수행하도록 설계하는 Prompt다.

Q. Tool Calling과 Function Calling은 어떻게 달라?
A. Function Calling은 정해진 함수 Schema 호출에 초점이 있고, Tool Calling은 도구 선택, 실행, 결과 검증, 실패 처리까지 포함한다.

Q. Agent Tool Use가 뭐야?
A. Multi-Agent Workflow에서 Agent별로 사용할 수 있는 도구와 사용 기준을 정의하는 방식이다.

Q. 모든 Agent가 모든 Tool을 써도 돼?
A. 권장하지 않는다. Agent 책임에 맞게 Tool 사용 범위를 제한해야 한다.

Q. Policy Priority가 뭐야?
A. 여러 Prompt 규칙, 프로젝트 규칙, 사용자 요청, Tool 결과가 충돌할 때 무엇을 우선할지 정하는 기준이다.

Q. 사용자 요청과 안전 규칙이 충돌하면 무엇을 따라야 해?
A. 안전 규칙을 따라야 한다.

Q. 프로젝트 문서와 일반 지식이 다르면 무엇을 따라야 해?
A. 프로젝트 RAG 작업에서는 프로젝트 문서와 Domain Rules를 우선해야 한다.

Q. Safe Code Generation Pattern이 뭐야?
A. 코드 생성 시 보안, 권한, 비밀정보, 예외 처리, 검증 기준을 함께 적용하는 Prompt 패턴이다.

Q. 코드 생성에서 보안상 가장 조심할 점은 뭐야?
A. Secret 하드코딩, 인증 우회, 권한 검증 누락, 민감정보 로그 출력이다.

Q. Safe Tool Calling Pattern이 뭐야?
A. Tool 사용 시 입력, 실행, 결과 검증, 실패 처리를 안전하게 수행하는 Prompt 패턴이다.

Q. Guarded RAG Answer Pattern이 뭐야?
A. RAG 답변에 Safety, Grounding, Missing Information, Assumption 규칙을 함께 적용하는 Prompt 패턴이다.

Q. Safety Prompt에서 가장 흔한 실수는 뭐야?
A. “안전하게 답해”처럼 모호하게 작성하고 구체적인 금지 범위와 대체 방향을 넣지 않는 것이다.

Q. Guardrail Prompt에서 가장 흔한 실수는 뭐야?
A. Scope, Output, Tool, Failure 경계를 명확히 정하지 않는 것이다.

Q. Tool Use Prompt에서 가장 흔한 실수는 뭐야?
A. Tool 사용 기준과 결과 검증 기준 없이 도구를 사용하게 하는 것이다.

Q. Function Calling에서 가장 흔한 실수는 뭐야?
A. Required Argument 누락, 허용되지 않은 Enum 사용, 없는 인자 임의 생성이다.

Q. Safety and Guardrail Best Practice는 뭐야?
A. 허용 범위, 금지 범위, 비밀정보 처리, 거절 규칙, Scope, Output, Failure 경계를 명확히 설계하는 것이다.

Q. Tool Use Best Practice는 뭐야?
A. Tool 필요성 판단, Tool 선택, 안전한 입력, 결과 검증, 실패 처리를 명확히 하는 것이다.

Q. Function Calling Best Practice는 뭐야?
A. 함수 Schema, Required Argument, Enum, 입력 검증, 결과 검증, 실패 처리를 정확히 수행하는 것이다.
