# Agent Evaluation & Guardrails Part04 - Format & Code Evaluation

---

# 1. Format Compliance Evaluation

## 1.1 Format Compliance

### [개념]

Format Compliance는 Agent Output이 사용자가 요구한 출력 형식, 문서 구조, 데이터 스키마, Markdown 규칙, JSON 규칙, 코드 블록 규칙을 지켰는지 평가하는 기준이다.

Format Compliance는 Agent Workflow에서 중요하다.

출력 형식이 깨지면 후속 Agent, Tool, Parser, RAG Indexer가 결과를 안정적으로 처리하기 어렵다.

Format Compliance 평가 대상:

- Markdown Format
- JSON Format
- Checklist Format
- Table Format
- Code Block Format
- Required Section
- Field Schema
- File Naming
- Document Structure
- Output Wrapper

---

### [핵심]

Format Compliance 검증 항목:

| 항목               | 검증 내용                          |
| ------------------ | ---------------------------------- |
| Required Section   | 필수 섹션이 있는가                 |
| Header Hierarchy   | Header 계층이 일관되는가           |
| JSON Validity      | JSON이 파싱 가능한가               |
| Markdown Validity  | Markdown 구조가 깨지지 않았는가    |
| Code Block         | 코드 블록 언어와 범위가 적절한가   |
| Table Structure    | Table 컬럼과 행이 깨지지 않았는가  |
| Output Wrapper     | 요구된 Wrapper 형식을 지켰는가     |
| Field Schema       | Required Field가 누락되지 않았는가 |
| Naming Consistency | 파일명과 제목이 일관되는가         |

Format Compliance 기본 Flow:

```text
User Output Format
→ Agent Output
→ Check Required Structure
→ Check Syntax / Schema
→ Pass / Fix / Fail
```

Format Compliance 결과:

```text
Pass:
- 요구 형식 준수
- 필수 섹션 포함
- Parser 처리 가능
- Markdown / JSON 구조 정상

Fix:
- 일부 섹션 누락
- Header 계층 오류
- Table 일부 깨짐
- Code Block 범위 오류

Fail:
- JSON 파싱 불가
- 필수 Wrapper 누락
- Required Field 누락
- 사용자가 요구한 형식 전체 위반
```

---

### [실무]

2026 실무 기준 Format Compliance는 Agent Output 자동 처리 안정성과 연결된다.

특히 Multi-Agent Workflow에서는 PM Agent, Review Agent, Fix Agent, Tool Agent가 서로 결과를 전달한다.

형식이 깨지면 후속 단계가 실패한다.

실무 적용 예시:

```text
User Requirement:
- Markdown 문서
- [개념], [핵심], [실무], [FAQ] 포함
- Retrieval Queries 포함
- writing block 사용
- 중간 응답 금지

Format Evaluation:
- writing block 존재 여부 확인
- Markdown Header 계층 확인
- Required Section 포함 여부 확인
- FAQ Q/A 형식 확인
- Retrieval Queries 위치 확인
```

JSON Format 예시:

```json
{
  "status": "pass",
  "findings": [],
  "requiresFix": false
}
```

JSON Format 검증 기준:

```text
- 설명 문장이 JSON 바깥에 섞이지 않았는가
- trailing comma가 없는가
- Required Field가 있는가
- boolean / string / array 타입이 맞는가
- downstream parser가 처리 가능한가
```

Markdown RAG 문서 Format 검증 기준:

```text
- # FileName 존재
- # Document Title 존재
- --- 구분선 사용 일관성
- Required Section 존재
- FAQ는 Q + A 형식
- Retrieval Queries는 문서 마지막에 위치
- 장문 Plain Text보다 구조화된 Bullet / Table 중심
```

Format Compliance Report 예시:

```md
### Format Compliance Report

| Item              | Result | Evidence                           | Fix         |
| ----------------- | ------ | ---------------------------------- | ----------- |
| Required Section  | Pass   | [개념], [핵심], [실무], [FAQ] 존재 | 없음        |
| Retrieval Queries | Pass   | 문서 마지막 포함                   | 없음        |
| JSON Validity     | Fail   | 설명 문장이 JSON 내부 포함         | JSON만 출력 |
| Header Hierarchy  | Fix    | H2 다음 H4 사용                    | H3로 수정   |
```

---

### [주의]

Format Compliance 주의사항:

- 형식이 맞아도 내용이 맞는 것은 아니다.
- 내용이 좋아도 요구 형식을 위반하면 Agent Workflow에서 실패할 수 있다.
- JSON 출력에 설명 문장이 섞이면 파싱 실패가 발생한다.
- Markdown Header 계층이 깨지면 Chunk 분리가 불안정해질 수 있다.
- FAQ에서 Q만 있고 A가 없으면 Retrieval 품질이 낮아진다.
- Table이 깨지면 Review Agent가 구조를 잘못 해석할 수 있다.
- 사용자가 지정한 Output Wrapper를 누락하면 Format Failure다.

---

### [Best Practice]

Format Compliance Best Practice:

- 사용자 요구 형식을 먼저 추출한다.
- Required Field / Required Section을 Checklist로 만든다.
- JSON은 순수 JSON만 출력한다.
- Markdown은 Header 계층을 단순하게 유지한다.
- RAG 문서는 Chunk 단위로 검색 가능한 구조를 사용한다.
- FAQ는 Q + A를 반드시 함께 작성한다.
- 형식 검증과 내용 검증을 분리한다.
- Parser가 필요한 출력은 예시 Schema를 고정한다.
- Final Output 전에 Format Check를 수행한다.

---

### [FAQ]

Q. Format Compliance가 뭐야?
A. Agent Output이 요구된 출력 형식, 문서 구조, JSON Schema, Markdown 규칙을 지켰는지 평가하는 기준이다.

Q. Format Compliance는 왜 중요해?
A. 형식이 깨지면 후속 Agent, Tool, Parser, RAG Indexer가 결과를 안정적으로 처리하기 어렵기 때문이다.

Q. 형식이 맞으면 내용도 맞는 거야?
A. 아니다. Format Compliance와 Content Quality는 별도로 평가해야 한다.

Q. JSON 출력에서 가장 중요한 것은 뭐야?
A. 파싱 가능한 순수 JSON이어야 하고 Required Field가 누락되지 않아야 한다.

Q. RAG 문서 Format에서 중요한 것은 뭐야?
A. Required Section, FAQ Q/A, Retrieval Queries, Header 계층, Chunk 구조다.

Q. FAQ에 질문만 있고 답변이 없으면 문제야?
A. 문제다. FAQ는 반드시 Q + A 형식이어야 Retrieval에 유리하다.

---

# 2. Markdown Format Evaluation

## 2.1 Markdown Format

### [개념]

Markdown Format Evaluation은 Agent가 작성한 Markdown 문서가 RAG Retrieval, Chunk 분리, Semantic Search, Human Review에 적합한 구조인지 평가하는 기준이다.

RAG 문서에서 Markdown은 단순 표시 형식이 아니다.

Markdown Header, Table, Code Block, FAQ 구조는 Retrieval 품질에 직접 영향을 준다.

---

### [핵심]

Markdown Format 필수 검증 항목:

| 항목              | 기준                  |
| ----------------- | --------------------- |
| Header            | 검색 가능한 제목 구조 |
| Section           | Required Section 포함 |
| Chunk Boundary    | 개념 단위로 분리      |
| Code Block        | 짧고 직접적인 예시    |
| Table             | 비교와 기준 정리      |
| Bullet            | 핵심 정보 분리        |
| FAQ               | Q + A 완성            |
| Retrieval Queries | 문서 마지막 포함      |

Markdown RAG 문서 기본 구조:

```md
# FileName

# Document Title

---

# 1. Main Section

## 1.1 Sub Section

### [개념]

내용

---

### [핵심]

- 핵심 포인트

---

### [실무]

실무 기준

---

### [FAQ]

Q. 질문
A. 답변

---

# Retrieval Queries

### [FAQ]

Q. 질문
A. 답변
```

Markdown Evaluation Flow:

```text
Markdown Output
→ Check Header
→ Check Required Section
→ Check Chunk Boundary
→ Check FAQ
→ Check Retrieval Queries
→ Pass / Fix
```

---

### [실무]

2026 실무 기준 RAG Markdown은 사람이 읽기 위한 에세이보다 Agent Retrieval에 최적화되어야 한다.

좋은 Markdown RAG Chunk:

```md
## 2.1 Tool Guardrails

### [개념]

Tool Guardrails는 외부 Tool 실행을 통제하는 규칙이다.

---

### [핵심]

- Tool Choice 검증
- Arguments 검증
- Permission 확인
- Risk Level 분류
- Human Confirmation 적용
```

나쁜 Markdown RAG Chunk:

```md
Tool Guardrails는 굉장히 중요하다. 왜냐하면 현대 AI 시스템에서는 여러 도구를 사용하고...
```

나쁜 이유:

- 제목 검색성이 낮음
- 핵심 키워드 분리 부족
- Chunk Boundary 불명확
- Retrieval Hit 품질 낮음

Markdown Format Report 예시:

```md
| Item              | Result | Issue                     | Fix         |
| ----------------- | ------ | ------------------------- | ----------- |
| Header            | Pass   | 명확한 제목 사용          | 없음        |
| Required Section  | Fail   | [FAQ] 누락                | FAQ 추가    |
| Chunk Size        | Fix    | 한 Chunk에 여러 개념 혼합 | 개념별 분리 |
| Retrieval Queries | Pass   | 문서 마지막 포함          | 없음        |
```

---

### [주의]

Markdown Format 주의사항:

- Header가 모호하면 검색 정확도가 낮아진다.
- 한 Chunk에 여러 개념을 섞으면 Retrieval 품질이 낮아진다.
- Code Block이 너무 길면 핵심 검색성이 떨어진다.
- Table은 비교 기준이 명확할 때만 사용한다.
- FAQ 내부에 과도한 구분선을 넣으면 구조가 불안정해질 수 있다.
- Retrieval Queries가 없으면 사용자 질문 매칭이 약해진다.
- Plain Text 장문은 RAG 문서에 불리하다.

---

### [Best Practice]

Markdown Format Best Practice:

- Section 제목에 핵심 키워드를 포함한다.
- [개념], [핵심], [실무], [FAQ] 구조를 유지한다.
- Bullet과 Table로 검색 가능한 단위를 만든다.
- Code Block은 짧고 직접적으로 작성한다.
- FAQ는 실제 사용자 질문 표현으로 작성한다.
- Retrieval Queries는 문서 마지막에 배치한다.
- 문서 전체 용어를 통일한다.
- Chunk는 하나의 개념만 포함한다.

---

### [FAQ]

Q. Markdown Format Evaluation은 뭐야?
A. Markdown 문서가 RAG Retrieval과 Chunk 분리에 적합한 구조인지 평가하는 기준이다.

Q. RAG 문서에서 Markdown 구조가 중요한 이유는?
A. Header, FAQ, Code Block, Table이 Retrieval Hit와 Chunk 품질에 영향을 주기 때문이다.

Q. 좋은 RAG Markdown Chunk 조건은 뭐야?
A. 하나의 개념, 명확한 제목, 짧은 예제, FAQ, 독립 검색 가능성이 있는 Chunk다.

Q. Plain Text 장문은 왜 안 좋아?
A. 검색 키워드가 묻히고 Chunk 의미가 흐려져 Retrieval 품질이 낮아진다.

Q. Retrieval Queries는 어디에 둬야 해?
A. 문서 마지막에 둬야 한다.

---

# 3. JSON / Schema Format Evaluation

## 3.1 JSON Format

### [개념]

JSON Format Evaluation은 Agent Output이 JSON Schema, Required Field, 데이터 타입, Parser 요구사항을 만족하는지 평가하는 기준이다.

JSON Format은 Tool Calling, Agent Handoff, Evaluation Report, Automation Workflow에서 중요하다.

---

### [핵심]

JSON Format 검증 항목:

| 항목              | 검증 내용                    |
| ----------------- | ---------------------------- |
| Parse Validity    | JSON 파싱이 가능한가         |
| Required Field    | 필수 필드가 있는가           |
| Field Type        | 타입이 맞는가                |
| Field Name        | 필드명이 Schema와 일치하는가 |
| Enum Value        | 허용된 값만 사용하는가       |
| No Extra Text     | JSON 외부 설명이 없는가      |
| No Trailing Comma | trailing comma가 없는가      |
| Escaping          | 문자열 Escape가 올바른가     |

JSON Evaluation Flow:

```text
JSON Output
→ Parse Check
→ Schema Check
→ Required Field Check
→ Type Check
→ Pass / Fix / Fail
```

좋은 JSON 예시:

```json
{
  "result": "fix",
  "requiresFix": true,
  "findings": [
    {
      "severity": "major",
      "issue": "Required section missing",
      "fix": "Add [FAQ] section"
    }
  ]
}
```

나쁜 JSON 예시:

```text
아래는 평가 결과입니다:
{
  "result": "pass",
}
```

문제:

- JSON 외부 설명 문장 포함
- trailing comma 존재
- Parser 실패 가능

---

### [실무]

실무에서는 JSON Schema를 Agent Output 계약으로 사용한다.

Evaluation Report JSON Schema 예시:

```json
{
  "target": "Agent Output",
  "result": "pass | fix | stop",
  "requiresFix": true,
  "findings": [
    {
      "severity": "critical | major | minor | info",
      "issue": "string",
      "evidence": "string",
      "fixRecommendation": "string"
    }
  ]
}
```

Tool Calling JSON 평가 예시:

```json
{
  "tool": "file_write",
  "riskLevel": "medium",
  "requiresHumanConfirmation": false,
  "argumentsValid": true
}
```

검증 기준:

```text
- tool 값이 허용된 Tool 이름인가
- riskLevel 값이 enum 범위인가
- requiresHumanConfirmation 타입이 boolean인가
- argumentsValid 타입이 boolean인가
- 위험 작업인데 requiresHumanConfirmation=false가 아닌가
```

---

### [주의]

JSON Format 주의사항:

- JSON 안에 주석을 넣으면 표준 JSON이 아니다.
- Markdown code fence가 필요한지 순수 JSON만 필요한지 구분해야 한다.
- Enum 값 오타는 Parser 또는 후속 Agent 오류를 만든다.
- Required Field 누락은 Format Failure다.
- Type이 틀리면 Tool 실행 오류가 발생할 수 있다.
- JSON 형식이 맞아도 위험한 값이면 Safety Evaluation이 필요하다.

---

### [Best Practice]

JSON Format Best Practice:

- Schema를 먼저 정의한다.
- Required Field를 최소화하고 명확히 한다.
- Enum 값은 고정한다.
- JSON 출력에는 불필요한 설명을 섞지 않는다.
- Parser가 필요한 경우 순수 JSON만 출력한다.
- Validation 실패 시 재생성 규칙을 둔다.
- Format Compliance와 Safety Compliance를 함께 확인한다.

---

### [FAQ]

Q. JSON Format Evaluation은 뭐야?
A. Agent Output이 JSON Schema, 필수 필드, 타입, Parser 요구사항을 만족하는지 평가하는 기준이다.

Q. JSON 외부에 설명을 붙여도 돼?
A. Parser가 순수 JSON을 요구하면 붙이면 안 된다.

Q. JSON에서 trailing comma는 문제야?
A. 표준 JSON에서는 문제다. Parser 실패가 발생할 수 있다.

Q. Required Field가 없으면 어떻게 돼?
A. Format Failure로 처리하고 Fix해야 한다.

Q. JSON 형식이 맞으면 Tool 실행해도 돼?
A. 아니다. Tool 실행 전 Safety, Permission, Risk Level 검증이 필요하다.

---

# 4. Code Evaluation

## 4.1 Code Evaluation Core

### [개념]

Code Evaluation은 Agent가 생성한 코드가 문법적으로 맞고, 프로젝트 구조와 버전 기준에 맞으며, 런타임 위험과 보안 위험을 최소화하는지 평가하는 기준이다.

Code Evaluation은 코드가 “그럴듯한지” 보는 것이 아니다.

실제 적용 가능성, 유지보수성, 테스트 가능성, 프로젝트 규칙 준수 여부를 검증한다.

Code Evaluation 평가 대상:

- Syntax Correctness
- Compile 가능성
- Runtime Risk
- Project Convention
- Version Compatibility
- Error Handling
- Security
- Testability
- Maintainability
- Performance Risk

---

### [핵심]

Code Evaluation 검증 항목:

| 항목                  | 검증 내용                    |
| --------------------- | ---------------------------- |
| Syntax Correctness    | 문법 오류가 없는가           |
| Compile Possibility   | 컴파일 가능한가              |
| Runtime Risk          | 실행 시 오류 가능성이 있는가 |
| Project Convention    | 프로젝트 규칙과 맞는가       |
| Version Compatibility | 기술 버전과 호환되는가       |
| Error Handling        | 예외 처리 구조가 적절한가    |
| Security              | 보안 위험이 없는가           |
| Testability           | 테스트 가능한 구조인가       |
| Maintainability       | 유지보수 가능한가            |

Code Evaluation Flow:

```text
Generated Code
→ Syntax Check
→ Project Context Check
→ Version Check
→ Runtime Risk Check
→ Security Check
→ Testability Check
→ Pass / Fix / Stop
```

Code Evaluation 결과:

```text
Pass:
- 문법 정상
- 프로젝트 구조와 일치
- 버전 호환
- 주요 런타임 위험 없음
- 보안 문제 없음

Fix:
- 일부 구조 개선 필요
- 예외 처리 보완 필요
- 테스트 가능성 낮음
- 프로젝트 규칙 일부 불일치

Stop:
- 존재하지 않는 클래스 / 메서드 사용
- 컴파일 불가 가능성 높음
- 보안상 위험
- 요구사항과 충돌
```

---

### [실무]

2026 실무 기준 Code Evaluation은 프로젝트 Context와 버전 기준을 함께 본다.

Backend Code Review 기준:

```text
- Java 21 기준인가?
- Spring Boot 3.x 기준인가?
- Entity / DTO / Repository 이름이 실제 존재하는가?
- Repository Query Method가 Entity 필드명과 일치하는가?
- Controller 응답 규칙이 프로젝트 규칙과 맞는가?
- Service Transaction Boundary가 적절한가?
- 예외는 GlobalExceptionHandler와 연결되는가?
- DTO / Entity 책임이 분리되는가?
- N+1 위험이 있는가?
- 테스트 작성이 가능한 구조인가?
```

Frontend Code Review 기준:

```text
- React 버전과 문법이 맞는가?
- API 경로가 실제 Backend와 일치하는가?
- 인증 필요 API와 public API가 분리되는가?
- Loading / Error 상태가 처리되는가?
- 상태 관리가 과도하지 않은가?
- 컴포넌트 책임이 분리되는가?
```

Code Evaluation Report 예시:

```md
### Code Evaluation Report

| Severity | Issue                                | Evidence                          | Fix                           |
| -------- | ------------------------------------ | --------------------------------- | ----------------------------- |
| Critical | 존재하지 않는 Repository 메서드 사용 | findUnreadByUserId() 근거 없음    | 실제 메서드명으로 수정        |
| Major    | 예외 처리 중복                       | Controller try-catch 사용         | GlobalExceptionHandler로 이동 |
| Minor    | DTO 이름 불일치                      | UserResponseDto / UserResDto 혼용 | 용어 통일                     |
```

---

### [주의]

Code Evaluation 주의사항:

- 코드 일부만 보고 전체 시스템을 단정하지 않는다.
- 존재하지 않는 클래스, 메서드, 필드는 Hallucination이다.
- 일반적으로 좋은 코드가 프로젝트 규칙과 맞지 않을 수 있다.
- 컴파일 오류와 설계 개선점을 구분해야 한다.
- 취향과 결함을 구분해야 한다.
- 보안 문제는 일반 리팩토링보다 높은 Severity다.
- 실제 실행 검증이 필요한 경우 Tool Result가 필요할 수 있다.

---

### [Best Practice]

Code Evaluation Best Practice:

- 프로젝트 버전과 컨벤션을 먼저 확인한다.
- 실제 존재하는 파일, 클래스, 메서드 기준으로 평가한다.
- Compile 가능성과 Runtime Risk를 분리한다.
- Security, Error Handling, Transaction Boundary를 별도 항목으로 본다.
- 결함과 개선 제안을 구분한다.
- Severity를 Critical / Major / Minor / Info로 나눈다.
- Fix Recommendation은 구체적으로 작성한다.
- 검증 불가 항목은 Assumption 또는 Missing Information으로 표시한다.

---

### [FAQ]

Q. Code Evaluation이 뭐야?
A. Agent가 생성한 코드가 문법, 컴파일, 프로젝트 구조, 버전, 보안, 테스트 기준을 만족하는지 평가하는 과정이다.

Q. 코드가 그럴듯하면 통과야?
A. 아니다. 실제 프로젝트 구조와 버전 기준에 맞고 컴파일 가능해야 한다.

Q. Code Evaluation에서 가장 위험한 문제는 뭐야?
A. 존재하지 않는 클래스, 메서드, 필드 사용과 보안 취약점이다.

Q. 취향과 결함은 어떻게 구분해?
A. 결함은 요구사항, 컴파일, 런타임, 보안, 프로젝트 규칙을 위반하는 것이고 취향은 대안 가능한 스타일 차이다.

Q. 검증할 코드 Context가 부족하면 어떻게 해?
A. Missing Information 또는 Assumption으로 표시하고 확정적으로 평가하지 않는다.

---

# 5. Backend Code Evaluation

## 5.1 Backend Code Review Criteria

### [개념]

Backend Code Evaluation은 Backend Agent가 생성한 Controller, Service, Repository, DTO, Entity, Config 코드가 프로젝트 규칙과 Spring Boot 실무 기준에 맞는지 평가하는 기준이다.

Backend Code Evaluation은 단순 문법 검사가 아니라 Layer 책임, Transaction, 예외 처리, 보안, 성능, 테스트 가능성을 함께 검토한다.

---

### [핵심]

Backend Code Evaluation 필수 기준:

| 기준                    | 검증 내용                                           |
| ----------------------- | --------------------------------------------------- |
| Layer Responsibility    | Controller / Service / Repository 책임이 분리되는가 |
| DTO / Entity Separation | Entity를 직접 노출하지 않는가                       |
| Transaction Boundary    | 변경 작업에 Transaction이 적절한가                  |
| Exception Handling      | GlobalExceptionHandler 구조와 맞는가                |
| Response Format         | 프로젝트 응답 규칙과 맞는가                         |
| Repository Method       | Entity 필드와 Query Method가 일치하는가             |
| Security                | 인증 / 인가 검증이 적절한가                         |
| Validation              | Request Validation이 있는가                         |
| N+1 Risk                | Lazy Loading / 조회 최적화 위험이 있는가            |
| Testability             | 단위 테스트 작성이 가능한가                         |

Backend Code Review Flow:

```text
Backend Code
→ Layer Check
→ Entity / DTO Check
→ Transaction Check
→ Exception Check
→ Repository Check
→ Security Check
→ Performance Check
→ Testability Check
```

---

### [실무]

2026 Spring Boot 실무 기준 Backend Agent Output은 프로젝트 규칙과 실제 코드 Context를 우선해야 한다.

Controller 평가 기준:

```text
- RequestMapping 경로가 실제 API 설계와 맞는가?
- ApiResponse<T> 직접 반환 규칙을 따르는가?
- Controller에서 비즈니스 로직을 처리하지 않는가?
- 예외를 try-catch로 중복 처리하지 않는가?
- 인증 필요 API와 공개 API가 구분되는가?
```

Service 평가 기준:

```text
- 비즈니스 로직이 Service에 있는가?
- Transaction Boundary가 적절한가?
- 중복 검증과 상태 변경이 일관되는가?
- Entity 상태 변경 메서드를 적절히 사용하는가?
- 예외 타입이 프로젝트 규칙과 맞는가?
```

Repository 평가 기준:

```text
- Query Method 이름이 Entity 필드명과 일치하는가?
- Slice / Page / List 선택이 요구사항과 맞는가?
- N+1 위험이 있는 조회에 fetch join 또는 EntityGraph가 필요한가?
- exists / count 메서드를 적절히 사용하는가?
```

DTO 평가 기준:

```text
- Request DTO와 Response DTO가 분리되는가?
- Entity를 직접 반환하지 않는가?
- Validation Annotation이 필요한 위치에 있는가?
- 민감정보가 Response에 포함되지 않는가?
```

Backend Evaluation Report 예시:

```md
| Severity | Layer      | Issue                                | Evidence                                 | Fix                             |
| -------- | ---------- | ------------------------------------ | ---------------------------------------- | ------------------------------- |
| Major    | Controller | ResponseEntity 사용                  | 프로젝트 규칙은 ApiResponse<T> 직접 반환 | ApiResponse<T>로 수정           |
| Critical | Repository | 존재하지 않는 필드 기반 Query Method | usersId 필드 없음                        | 실제 Entity 연관 필드 기준 수정 |
| Major    | Service    | Transaction 누락                     | 상태 변경 로직 존재                      | @Transactional 추가             |
| Minor    | DTO        | Response DTO 이름 혼용               | UserResponseDto / UserResDto             | 명칭 통일                       |
```

---

### [주의]

Backend Code Evaluation 주의사항:

- Spring 일반 관례와 프로젝트 규칙이 다를 수 있다.
- Entity 필드명을 확인하지 않고 Query Method를 만들면 컴파일 실패한다.
- Controller에서 예외를 직접 처리하면 GlobalExceptionHandler 구조와 충돌할 수 있다.
- ResponseEntity 사용 여부는 프로젝트 규칙에 따라 판단해야 한다.
- DTO 없이 Entity를 반환하면 보안과 결합도 문제가 생길 수 있다.
- 테스트 없는 코드는 동작 확신이 낮다.
- 보안 검증 누락은 Critical로 볼 수 있다.

---

### [Best Practice]

Backend Code Evaluation Best Practice:

- 실제 Entity / DTO / Repository 목록을 근거로 평가한다.
- Controller, Service, Repository 책임을 분리해서 검토한다.
- Transaction, Exception, Response Format을 별도 항목으로 본다.
- 존재하지 않는 메서드나 필드는 Hallucination으로 분류한다.
- 프로젝트 응답 규칙을 우선한다.
- 성능 이슈는 N+1, 불필요한 전체 조회, 페이징 누락 중심으로 본다.
- Fix는 실제 코드 위치와 방향을 함께 제시한다.

---

### [FAQ]

Q. Backend Code Evaluation은 뭐야?
A. Backend Agent가 만든 코드가 Layer 책임, Transaction, 예외 처리, 보안, 성능, 테스트 기준을 만족하는지 평가하는 과정이다.

Q. Controller에서 가장 먼저 볼 것은 뭐야?
A. API 경로, 응답 규칙, 비즈니스 로직 포함 여부, 예외 처리 중복 여부다.

Q. Service에서 중요한 검토 기준은 뭐야?
A. Transaction Boundary, 비즈니스 로직 위치, 상태 변경 일관성, 예외 처리다.

Q. Repository Query Method는 어떻게 검증해?
A. Entity 필드명과 연관관계 이름을 기준으로 실제 컴파일 가능한지 확인한다.

Q. Entity를 Response로 직접 반환해도 돼?
A. 일반적으로 피해야 한다. DTO로 변환해 민감정보 노출과 결합도를 줄여야 한다.

Q. ResponseEntity 사용은 항상 잘못이야?
A. 아니다. 프로젝트 규칙이 ApiResponse<T> 직접 반환이라면 그 규칙을 우선한다.

---

# 6. Code Hallucination Evaluation

## 6.1 Code Hallucination

### [개념]

Code Hallucination은 Agent가 실제 프로젝트에 존재하지 않는 클래스, 메서드, 필드, API, 설정, 라이브러리를 기준으로 코드를 생성하는 실패 유형이다.

Code Hallucination은 컴파일 오류, 런타임 오류, 잘못된 설계, 보안 문제로 이어질 수 있다.

---

### [핵심]

Code Hallucination 유형:

| 유형                  | 예시                                        |
| --------------------- | ------------------------------------------- |
| Fabricated Class      | 존재하지 않는 UserResponseDto 사용          |
| Fabricated Method     | Repository에 없는 findUnreadByUserId() 사용 |
| Fabricated Field      | Entity에 없는 status 필드 사용              |
| Fabricated API        | 존재하지 않는 /api/popular 경로 호출        |
| Fabricated Config     | 설정 파일에 없는 key 사용                   |
| Fabricated Dependency | build.gradle에 없는 라이브러리 사용         |
| Version Mismatch Code | 현재 버전에서 지원하지 않는 API 사용        |

Code Hallucination Detection Flow:

```text
Generated Code
→ Extract Project-specific Symbols
→ Match with Context / Files
→ Existing / Missing / Unknown
→ Fix or Mark Assumption
```

검증 대상 Symbol:

```text
- Package Name
- Class Name
- Method Name
- Field Name
- Enum Value
- API Endpoint
- Config Key
- Table Name
- Dependency Name
```

---

### [실무]

실무에서는 코드 생성 전후로 Project Symbol Check를 수행한다.

Project Symbol Check 예시:

```md
| Symbol                                | Type              | Evidence          | Result   | Fix                |
| ------------------------------------- | ----------------- | ----------------- | -------- | ------------------ |
| UserResDto                            | DTO               | DTO 목록에 존재   | Existing | 없음               |
| UserResponseDto                       | DTO               | 근거 없음         | Missing  | UserResDto로 수정  |
| countByUsers_UserIdAndReadStatusFalse | Repository Method | Repository에 존재 | Existing | 없음               |
| findUnreadByUserId                    | Repository Method | 근거 없음         | Missing  | 실제 메서드명 사용 |
```

Code Hallucination 예시:

```java
long unreadCount = notificationRepository.findUnreadByUserId(userId).size();
```

문제:

```text
- findUnreadByUserId() 근거 없음
- Method Hallucination
- countByUsers_UserIdAndReadStatusFalse(userId) 사용이 실제 Context와 일치
```

수정 예시:

```java
long unreadCount = notificationRepository.countByUsers_UserIdAndReadStatusFalse(userId);
```

---

### [주의]

Code Hallucination 주의사항:

- 일반적으로 자주 쓰는 메서드라도 프로젝트에 없으면 사용할 수 없다.
- DTO 이름 한 글자 차이도 컴파일 오류가 된다.
- Query Method는 Entity 필드명과 정확히 맞아야 한다.
- API 경로는 Controller 실제 경로와 일치해야 한다.
- build.gradle에 없는 라이브러리를 임의로 사용하면 안 된다.
- Version Mismatch도 Code Hallucination처럼 동작할 수 있다.
- 검증 불가 Symbol은 Existing으로 확정하지 않는다.

---

### [Best Practice]

Code Hallucination 방지 Best Practice:

- 코드 생성 전 제공된 파일 구조와 Symbol을 확인한다.
- 실제 존재하는 Entity / DTO / Repository 기준으로 작성한다.
- 없는 메서드는 새로 만들지 말고 Assumption으로 표시한다.
- Query Method는 Entity 필드명을 기준으로 생성한다.
- API 호출 코드는 Controller 경로와 대조한다.
- 설정 Key와 Dependency는 실제 파일 기준으로 확인한다.
- Review Agent는 Fabricated Symbol 목록을 작성한다.

---

### [FAQ]

Q. Code Hallucination이 뭐야?
A. Agent가 실제 프로젝트에 없는 클래스, 메서드, 필드, API, 설정을 기준으로 코드를 생성하는 실패 유형이다.

Q. Code Hallucination은 왜 위험해?
A. 컴파일 오류, 런타임 오류, 잘못된 설계, 보안 문제로 이어질 수 있기 때문이다.

Q. Fabricated Method는 뭐야?
A. 실제 Repository나 Service에 없는 메서드를 만들어 사용하는 것이다.

Q. Fabricated Field는 뭐야?
A. 실제 Entity에 없는 필드를 기준으로 코드를 작성하는 것이다.

Q. Code Hallucination은 어떻게 탐지해?
A. 생성 코드의 클래스명, 메서드명, 필드명, API 경로를 실제 Context와 대조한다.

Q. 검증할 수 없는 메서드는 어떻게 처리해?
A. Existing으로 확정하지 말고 Assumption 또는 Missing Information으로 표시해야 한다.

---

# 7. Format & Code Evaluation Checklist

## 7.1 Checklist

### [개념]

Format & Code Evaluation Checklist는 Agent Output의 형식 안정성과 코드 적용 가능성을 빠르게 검증하기 위한 최소 평가 목록이다.

이 Checklist는 Review Agent, Backend Agent, Frontend Agent, PM Agent가 공통으로 사용할 수 있다.

---

### [핵심]

Format Checklist:

```md
### [Checklist]

- [ ] 사용자가 요구한 출력 형식을 지켰는가?
- [ ] Required Section 또는 Required Field가 누락되지 않았는가?
- [ ] Markdown Header 계층이 일관되는가?
- [ ] FAQ가 Q + A 형식인가?
- [ ] Retrieval Queries가 필요한 경우 포함되었는가?
- [ ] JSON이 필요한 경우 파싱 가능한가?
- [ ] Code Block 범위가 올바른가?
- [ ] Table 구조가 깨지지 않았는가?
- [ ] Output Wrapper가 요구사항과 일치하는가?
```

Code Checklist:

```md
### [Checklist]

- [ ] 코드 문법이 올바른가?
- [ ] 프로젝트 버전과 호환되는가?
- [ ] 실제 존재하는 클래스 / 메서드 / 필드를 사용하는가?
- [ ] Layer 책임이 분리되는가?
- [ ] 예외 처리 구조가 프로젝트 규칙과 맞는가?
- [ ] Transaction Boundary가 적절한가?
- [ ] 보안 위험이 없는가?
- [ ] N+1 또는 성능 위험이 없는가?
- [ ] 테스트 가능한 구조인가?
- [ ] 검증 불가 항목은 Assumption으로 표시했는가?
```

최소 Pass 기준:

```text
Format Pass:
- 필수 형식 준수
- Parser 처리 가능
- Required Section / Field 누락 없음

Code Pass:
- 컴파일 가능성 높음
- 프로젝트 Symbol과 일치
- Critical Security Issue 없음
- 핵심 요구사항 충족
```

---

### [실무]

실무에서는 Format Check와 Code Check를 분리해서 수행한다.

평가 순서:

```text
1. Format Compliance Check
2. Requirement Compliance Check
3. Code Symbol Check
4. Version Compatibility Check
5. Runtime / Security Risk Check
6. Testability Check
7. Final Pass / Fix / Stop
```

Checklist Result 예시:

```md
### Format & Code Evaluation Result

| Category | Item              | Result | Fix                                    |
| -------- | ----------------- | ------ | -------------------------------------- |
| Format   | Required Section  | Pass   | 없음                                   |
| Format   | JSON Validity     | Fail   | trailing comma 제거                    |
| Code     | Repository Method | Fail   | 실제 메서드명으로 수정                 |
| Code     | Transaction       | Fix    | 상태 변경 메서드에 @Transactional 추가 |
| Code     | Security          | Pass   | 없음                                   |
```

---

### [주의]

Checklist 주의사항:

- Checklist는 최소 기준이다.
- Format Pass가 Code Pass를 의미하지 않는다.
- Code Pass가 Requirement Pass를 의미하지 않는다.
- Symbol 검증 없이 코드 Correctness를 확정하지 않는다.
- 보안 문제는 다른 Minor Issue보다 우선한다.
- 검증 불가한 코드는 Pass가 아니라 Unknown 또는 Assumption이다.

---

### [Best Practice]

Checklist Best Practice:

- Format Check를 먼저 수행한다.
- Parser가 필요한 Output은 실제 파싱 가능성을 우선한다.
- 코드에서는 실제 프로젝트 Symbol을 우선 검증한다.
- Critical Issue는 즉시 Stop 또는 Fix로 처리한다.
- Minor Format Issue는 Fix하되 Workflow를 과도하게 막지 않는다.
- Evaluation Report에 Evidence와 Fix를 함께 기록한다.
- 반복되는 Format Failure는 Schema를 단순화한다.

---

### [FAQ]

Q. Format & Code Evaluation Checklist는 뭐야?
A. Agent Output의 형식 안정성과 코드 적용 가능성을 빠르게 검증하기 위한 최소 평가 목록이다.

Q. Format Check와 Code Check는 같이 해도 돼?
A. 함께 할 수 있지만 기준은 분리해야 한다.

Q. Format Pass면 코드도 괜찮은 거야?
A. 아니다. Format Compliance와 Code Correctness는 별도 평가 기준이다.

Q. Code Pass 최소 기준은 뭐야?
A. 컴파일 가능성이 높고, 실제 프로젝트 Symbol과 일치하며, Critical Security Issue가 없어야 한다.

Q. 검증 불가한 코드는 Pass로 처리해도 돼?
A. 안 된다. Unknown, Assumption, Missing Information으로 표시해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Format Compliance가 뭐야?
A. Agent Output이 요구된 출력 형식, 문서 구조, JSON Schema, Markdown 규칙을 지켰는지 평가하는 기준이다.

Q. Format Compliance는 왜 중요해?
A. 형식이 깨지면 후속 Agent, Tool, Parser, RAG Indexer가 결과를 안정적으로 처리하기 어렵기 때문이다.

Q. Format Compliance와 Content Quality는 달라?
A. 다르다. 형식이 맞아도 내용이 틀릴 수 있고, 내용이 좋아도 형식 위반이면 Workflow가 실패할 수 있다.

Q. Markdown Format Evaluation은 뭐야?
A. Markdown 문서가 RAG Retrieval과 Chunk 분리에 적합한 구조인지 평가하는 기준이다.

Q. RAG Markdown 문서에서 중요한 구조는 뭐야?
A. Header, Required Section, FAQ, Code Block, Table, Retrieval Queries, Chunk Boundary다.

Q. 좋은 RAG Chunk 조건은 뭐야?
A. 하나의 개념만 포함하고 제목이 명확하며 짧은 예제와 FAQ를 포함해 독립 검색이 가능한 Chunk다.

Q. FAQ 형식은 어떻게 해야 해?
A. 반드시 Q + A 형식이어야 하며 답변은 짧고 명확해야 한다.

Q. Retrieval Queries는 어디에 둬야 해?
A. 문서 마지막에 둬야 한다.

Q. JSON Format Evaluation은 뭐야?
A. Agent Output이 JSON Schema, 필수 필드, 타입, Parser 요구사항을 만족하는지 평가하는 기준이다.

Q. JSON 출력에서 설명 문장을 섞어도 돼?
A. Parser가 순수 JSON을 요구하면 설명 문장을 섞으면 안 된다.

Q. JSON Required Field가 누락되면 어떻게 돼?
A. Format Failure로 처리하고 Fix해야 한다.

Q. JSON 형식이 맞으면 Tool 실행해도 돼?
A. 아니다. Tool 실행 전 Safety, Permission, Risk Level 검증이 필요하다.

Q. Code Evaluation이 뭐야?
A. Agent가 생성한 코드가 문법, 컴파일, 프로젝트 구조, 버전, 보안, 테스트 기준을 만족하는지 평가하는 과정이다.

Q. Code Evaluation에서 무엇을 확인해?
A. Syntax Correctness, Compile 가능성, Runtime Risk, Project Convention, Version Compatibility, Error Handling, Security, Testability를 확인한다.

Q. 코드가 그럴듯하면 통과야?
A. 아니다. 실제 프로젝트 구조와 버전 기준에 맞고 컴파일 가능해야 한다.

Q. Backend Code Evaluation은 뭐야?
A. Backend Agent 코드가 Layer 책임, Transaction, 예외 처리, 보안, 성능, 테스트 기준을 만족하는지 평가하는 과정이다.

Q. Controller 코드 평가는 어떻게 해?
A. API 경로, 응답 규칙, 비즈니스 로직 포함 여부, 예외 처리 중복 여부, 인증 필요 여부를 확인한다.

Q. Service 코드 평가는 어떻게 해?
A. Transaction Boundary, 비즈니스 로직 위치, 상태 변경 일관성, 예외 처리 구조를 확인한다.

Q. Repository Query Method는 어떻게 검증해?
A. 실제 Entity 필드명과 연관관계 이름을 기준으로 컴파일 가능한지 확인한다.

Q. Entity를 Response로 직접 반환해도 돼?
A. 일반적으로 피해야 한다. DTO로 변환해 민감정보 노출과 결합도를 줄여야 한다.

Q. ResponseEntity 사용은 항상 잘못이야?
A. 아니다. 프로젝트 규칙이 ApiResponse<T> 직접 반환이라면 그 규칙을 우선한다.

Q. Code Hallucination이 뭐야?
A. Agent가 실제 프로젝트에 없는 클래스, 메서드, 필드, API, 설정을 기준으로 코드를 생성하는 실패 유형이다.

Q. Fabricated Method는 뭐야?
A. 실제 Repository나 Service에 없는 메서드를 만들어 사용하는 것이다.

Q. Fabricated Field는 뭐야?
A. 실제 Entity에 없는 필드를 기준으로 코드를 작성하는 것이다.

Q. Code Hallucination은 어떻게 탐지해?
A. 생성 코드의 클래스명, 메서드명, 필드명, API 경로를 실제 Context와 대조한다.

Q. 검증할 수 없는 코드는 어떻게 처리해?
A. Pass로 처리하지 않고 Unknown, Assumption, Missing Information으로 표시해야 한다.

Q. Format & Code Evaluation Checklist는 언제 써?
A. Agent Output의 형식 안정성과 코드 적용 가능성을 빠르게 검증할 때 사용한다.

Q. Format Pass가 Code Pass를 의미해?
A. 아니다. Format Compliance와 Code Correctness는 별도로 평가해야 한다.

Q. Code Pass 최소 기준은 뭐야?
A. 컴파일 가능성이 높고 실제 프로젝트 Symbol과 일치하며 Critical Security Issue가 없어야 한다.
