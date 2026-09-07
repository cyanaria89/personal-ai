# Prompt Engineering Part06 Code Generation, Code Review, Refactoring, Debugging Prompt

---

# 1. Code Generation Prompt

## 1.1 Code Generation Prompt Definition

### [개념]

Code Generation Prompt는 LLM이 프로젝트 규칙과 기술 스택에 맞는 코드를 생성하도록 지시하는 Prompt다.

Code Generation Prompt는 단순히 “코드 만들어줘”가 아니다.

좋은 Code Generation Prompt는 아래 요소를 포함한다.

```text
Language
→ Framework
→ Version
→ Architecture
→ Existing Code Context
→ Input / Output
→ Constraints
→ Error Handling
→ Test Requirement
→ Validation
```

Code Generation Prompt의 목적은 프로젝트와 맞는 코드, 유지보수 가능한 코드, 검증 가능한 코드를 생성하는 것이다.

---

### [핵심]

- Code Generation Prompt는 기술 스택과 버전을 명확히 포함해야 한다.
- 기존 프로젝트 구조를 제공해야 한다.
- Entity, DTO, Repository, Controller 관계를 명확히 제공해야 한다.
- 존재하지 않는 클래스명, 필드명, API 경로 생성을 금지해야 한다.
- Error Handling 기준을 포함해야 한다.
- Transaction Boundary 기준을 포함해야 한다.
- 출력 범위는 필요한 코드 snippet 중심으로 제한하는 것이 좋다.
- Test Requirement 또는 Validation Checklist를 포함하면 품질이 좋아진다.

---

### [실무]

2026 실무 기준 Code Generation Prompt는 기존 프로젝트와의 정합성이 가장 중요하다.

Spring Boot 코드 생성 Prompt 예시:

```text
You are a Spring Boot Backend Agent.

Task:
Generate a Service implementation plan and code snippets.

Stack:
- Java 21
- Spring Boot 3.x
- Spring Data JPA
- MySQL

Architecture:
- Controller → Service → Repository
- Business logic belongs to Service
- Controller returns ApiResponse<T>
- GlobalExceptionHandler handles exceptions

Context:
- Entity, DTO, Repository code is provided below.

Constraints:
- Do not invent missing classes.
- Do not change existing API paths.
- Do not change Controller signatures.
- Use @Transactional for write operations.
- Keep code snippets short.

Output Format:
## Missing Information
## Assumptions
## Implementation Plan
## Code Snippet
## Validation Checklist
```

Code Generation Prompt는 “전체 구현”보다 “기능 단위 구현”이 안정적이다.

---

### [FAQ]

Q. Code Generation Prompt가 뭐야?

A. LLM이 프로젝트 규칙, 기술 스택, 기존 코드 구조에 맞는 코드를 생성하도록 지시하는 Prompt다.

Q. 코드 생성 Prompt에는 뭐가 필요해?

A. 언어, 프레임워크, 버전, 아키텍처, 기존 코드 Context, 제약, 예외 처리, 검증 기준이 필요하다.

Q. “전체 만들어줘”라고 해도 돼?

A. 가능하지만 오류가 늘 수 있다. 기능 단위, 계층 단위, 메서드 단위로 범위를 제한하는 것이 안정적이다.

Q. 코드 생성에서 가장 위험한 실수는 뭐야?

A. 존재하지 않는 클래스명, 필드명, API 경로, 비즈니스 규칙을 임의로 만드는 것이다.

---

# 2. Code Generation Components

## 2.1 Language and Framework

### [개념]

Language and Framework는 생성할 코드의 기술 기반을 정의하는 요소다.

LLM은 기술 스택이 명확하지 않으면 일반적인 코드나 다른 버전의 코드를 생성할 수 있다.

---

### [핵심]

- Language를 명시한다.
- Framework를 명시한다.
- Version을 명시한다.
- Build Tool을 명시한다.
- Database와 ORM을 명시한다.
- Frontend / Backend / DevOps 영역을 구분한다.
- 기술 스택이 없으면 생성 코드가 프로젝트와 맞지 않을 수 있다.

---

### [실무]

Backend Stack Context 예시:

```text
Stack:
- Java 21
- Spring Boot 3.x
- Spring Data JPA
- Spring Security
- MySQL
- Gradle
```

Frontend Stack Context 예시:

```text
Stack:
- React
- TypeScript
- Vite
- React Router
- Axios
- TanStack Query
```

AI Agent Stack Context 예시:

```text
Stack:
- Python
- LangGraph
- RAG
- Vector Database
- Tool Calling
- Structured Output
```

기술 스택과 버전은 Code Generation Prompt의 기본 Context다.

---

### [FAQ]

Q. 코드 생성 Prompt에 기술 스택을 꼭 넣어야 해?

A. 넣는 것이 좋다. 언어, 프레임워크, 버전이 없으면 프로젝트와 맞지 않는 코드가 생성될 수 있다.

Q. 버전도 중요해?

A. 중요하다. Spring Boot, React, LangChain, LangGraph 같은 기술은 버전에 따라 코드 방식이 달라질 수 있다.

Q. DB나 Build Tool도 적어야 해?

A. 코드와 설정에 영향을 주므로 MySQL, PostgreSQL, Gradle, Maven 같은 정보도 적는 것이 좋다.

---

## 2.2 Architecture Context

### [개념]

Architecture Context는 코드가 따라야 할 프로젝트 구조와 책임 분리 규칙이다.

Architecture Context는 생성 코드가 프로젝트 아키텍처와 일치하도록 만든다.

---

### [핵심]

- Layered Architecture를 명시한다.
- Controller, Service, Repository 책임을 구분한다.
- DTO 변환 책임을 명시한다.
- Transaction Boundary 위치를 명시한다.
- Error Handling 위치를 명시한다.
- API Response 규칙을 명시한다.
- 아키텍처 규칙이 없으면 모델이 임의 구조를 생성할 수 있다.

---

### [실무]

Spring Boot Architecture Context 예시:

```text
Architecture:
- Controller handles HTTP request and response.
- Service handles business logic and transaction boundary.
- Repository handles persistence.
- DTO handles request and response data transfer.
- Entity should not expose unnecessary internal state.
- GlobalExceptionHandler handles exceptions.
```

Code Generation Constraint 예시:

```text
Constraints:
- Do not place business logic in Controller.
- Do not access Repository directly from Controller.
- Do not return Entity directly from public API.
- Use DTO for API response.
```

Architecture Context는 Backend Agent가 프로젝트 구조를 벗어나지 않도록 제어한다.

---

### [FAQ]

Q. Architecture Context가 뭐야?

A. 코드가 따라야 할 계층 구조와 책임 분리 규칙이다.

Q. Architecture Context가 없으면 어떻게 돼?

A. Controller에 비즈니스 로직이 들어가거나 Repository를 직접 호출하는 등 구조가 흐트러질 수 있다.

Q. Spring Boot에서는 어떤 구조를 명시하면 좋아?

A. Controller → Service → Repository 구조, DTO 사용, GlobalExceptionHandler, Transaction Boundary 기준을 명시하면 좋다.

---

## 2.3 Existing Code Context

### [개념]

Existing Code Context는 생성 코드가 연결되어야 하는 기존 코드 정보다.

Existing Code Context에는 Entity, DTO, Repository, Controller, Config, Exception, Response Wrapper가 포함될 수 있다.

---

### [핵심]

- 기존 코드 Context는 코드 생성 정확도를 높인다.
- Entity 필드와 관계가 필요하다.
- DTO 필드와 검증 조건이 필요하다.
- Repository 메서드 시그니처가 필요하다.
- Controller 시그니처가 필요할 수 있다.
- Response Wrapper 규칙이 필요하다.
- 보이지 않는 코드는 단정하지 않는다.

---

### [실무]

Existing Code Context 예시:

```text
Existing Code Context:
- Users Entity
- LoginReqDto
- LoginResDto
- UserRepository
- AuthController login method
- ApiResponse<T>
- GlobalExceptionHandler
```

Missing Information 처리 예시:

```text
If Entity fields or Repository methods are not provided:
- Do not invent them.
- List them under Missing Information.
- Provide only safe implementation direction.
```

기존 코드가 충분하지 않으면 구현 코드보다 구현 계획과 필요한 정보 목록을 먼저 생성하는 것이 안전하다.

---

### [FAQ]

Q. Existing Code Context가 뭐야?

A. 생성 코드가 연결되어야 하는 기존 Entity, DTO, Repository, Controller, Config 같은 코드 정보다.

Q. Existing Code Context가 부족하면 어떻게 해야 해?

A. 부족한 정보를 Missing Information으로 표시하고, 확정 코드 대신 구현 방향을 제공해야 한다.

Q. 보이지 않는 Repository 메서드를 만들어도 돼?

A. 확정하면 안 된다. 필요하면 예시 또는 Assumption으로 분리해야 한다.

---

## 2.4 Error Handling Rule

### [개념]

Error Handling Rule은 코드 생성 시 예외를 어떻게 처리해야 하는지 정하는 규칙이다.

Error Handling Rule이 없으면 LLM이 null 반환, try-catch 남용, RuntimeException 남발 같은 코드를 생성할 수 있다.

---

### [핵심]

- 예외 처리 위치를 명시한다.
- GlobalExceptionHandler 사용 여부를 명시한다.
- Domain Exception 사용 여부를 명시한다.
- null 반환을 피하도록 지시한다.
- 예외 메시지와 상태 코드를 프로젝트 규칙에 맞춘다.
- 보안상 민감한 에러 메시지는 노출하지 않는다.
- try-catch 남용을 피한다.

---

### [실무]

Error Handling Prompt 예시:

```text
Error Handling:
- Do not return null on failure.
- Throw domain-specific exceptions when business rule fails.
- Let GlobalExceptionHandler convert exceptions to API responses.
- Do not expose sensitive internal error details.
```

Spring Boot Service 생성 예시:

```text
If user is not found:
- Throw UserNotFoundException if it exists.
- If exception class is not provided, mark it as Missing Information.
- Do not invent exception class as confirmed project code.
```

Error Handling Rule은 코드 생성 품질과 API 안정성에 직접 영향을 준다.

---

### [FAQ]

Q. Error Handling Rule은 왜 필요해?

A. null 반환, 예외 삼키기, RuntimeException 남발, 민감정보 노출을 막기 위해 필요하다.

Q. GlobalExceptionHandler가 있으면 Prompt에 적어야 해?

A. 적는 것이 좋다. 그래야 Service 코드가 예외를 던지고 Handler가 응답을 처리하는 구조를 따른다.

Q. 예외 클래스가 제공되지 않았으면 만들어도 돼?

A. 확정 코드처럼 만들면 안 된다. Missing Information 또는 Assumption으로 분리해야 한다.

---

## 2.5 Transaction Rule

### [개념]

Transaction Rule은 코드 생성 시 트랜잭션 경계를 어디에 둘지 정하는 규칙이다.

Spring Boot에서는 일반적으로 Service Layer에서 Transaction Boundary를 관리한다.

---

### [핵심]

- 쓰기 작업에는 @Transactional을 고려한다.
- 읽기 전용 작업에는 readOnly=true를 고려한다.
- Controller에 Transaction Boundary를 두지 않는다.
- 여러 Entity 변경은 하나의 트랜잭션으로 묶는다.
- 외부 API 호출과 DB 트랜잭션 결합은 주의한다.
- 트랜잭션 범위가 너무 넓지 않게 한다.

---

### [실무]

Transaction Prompt 예시:

```text
Transaction Rule:
- Use @Transactional for write operations in Service.
- Use @Transactional(readOnly = true) for read queries when appropriate.
- Do not place transaction logic in Controller.
- Keep transaction boundary as small as possible.
```

Code Generation 요청 예시:

```text
Generate Service method code.
Apply transaction boundary:
- Write operation: @Transactional
- Read operation: @Transactional(readOnly = true)
```

Transaction Rule은 데이터 정합성과 런타임 안정성에 중요하다.

---

### [FAQ]

Q. Transaction Rule은 뭐야?

A. 코드 생성 시 트랜잭션 경계를 어디에 둘지 정하는 규칙이다.

Q. Spring Boot에서는 Transaction을 어디에 두는 게 좋아?

A. 일반적으로 Service Layer에 둔다.

Q. 쓰기 작업에는 @Transactional이 필요해?

A. 여러 데이터 변경이나 정합성이 필요한 작업에는 필요하다.

---

## 2.6 Test Requirement

### [개념]

Test Requirement는 생성된 코드가 어떻게 검증되어야 하는지 정의하는 요소다.

Test Requirement는 코드 생성 결과가 실행 가능하고 유지보수 가능한지 확인하는 기준이다.

---

### [핵심]

- 단위 테스트 필요 여부를 명시한다.
- 통합 테스트 필요 여부를 명시한다.
- 테스트 대상 계층을 명시한다.
- 정상 케이스와 실패 케이스를 포함한다.
- Mock 사용 여부를 명시한다.
- Validation Checklist로 대체할 수 있다.
- 테스트 조건이 없으면 검증이 약해질 수 있다.

---

### [실무]

Test Requirement 예시:

```text
Test Requirement:
- Include unit test checklist.
- Cover success case.
- Cover not found case.
- Cover invalid input case.
- Cover authorization failure if applicable.
```

Service Test Prompt 예시:

```text
Return:
## Implementation
## Test Cases
- Success
- Not Found
- Invalid Input
- Permission Denied
## Validation Checklist
```

Code Generation Prompt에서 테스트 코드 전체가 필요하지 않다면 Test Checklist만 요청해도 좋다.

---

### [FAQ]

Q. Test Requirement는 뭐야?

A. 생성된 코드가 어떤 기준과 케이스로 검증되어야 하는지 정의하는 요소다.

Q. 코드 생성할 때 테스트도 요청해야 해?

A. 중요한 기능이면 테스트 코드나 테스트 체크리스트를 함께 요청하는 것이 좋다.

Q. 테스트 코드가 너무 길면 어떻게 해?

A. 전체 테스트 코드 대신 테스트 케이스 목록과 검증 체크리스트를 요청할 수 있다.

---

# 3. Code Generation Prompt Pattern

## 3.1 Service Generation Pattern

### [개념]

Service Generation Pattern은 Service Layer 코드 생성에 특화된 Prompt 패턴이다.

Service는 비즈니스 로직, 트랜잭션, 예외 처리, DTO 변환 흐름과 연결된다.

---

### [핵심]

- Service 책임을 명시한다.
- Transaction Boundary를 명시한다.
- Repository 사용 기준을 명시한다.
- DTO 변환 위치를 명시한다.
- Exception Handling 기준을 명시한다.
- Entity 변경 메서드 사용 여부를 명시한다.
- Controller와 Repository 시그니처 변경 금지를 명시한다.

---

### [실무]

Service Generation Prompt:

```text
You are a Spring Boot Backend Agent.

Task:
Generate Service method plan and code snippet.

Context:
- Java 21
- Spring Boot 3.x
- Controller → Service → Repository
- GlobalExceptionHandler handles exceptions
- DTO is used for API response

Constraints:
- Do not change Controller signature.
- Do not invent Repository methods.
- Do not return Entity directly.
- Use @Transactional for write operation.

Output:
## Service Responsibility
## Method Flow
## Code Snippet
## Missing Information
## Validation Checklist
```

Service Generation은 전체 파일보다 메서드 단위로 요청하는 것이 안정적이다.

---

### [FAQ]

Q. Service Generation Pattern은 뭐야?

A. Service Layer의 책임, 트랜잭션, 예외 처리, DTO 변환 기준을 명시해 코드를 생성하는 Prompt 패턴이다.

Q. Service 코드 생성에서 중요한 것은 뭐야?

A. 비즈니스 로직 위치, Transaction Boundary, Repository 사용, 예외 처리, DTO 변환 책임이다.

Q. Service 전체 파일을 생성해도 돼?

A. 가능하지만 메서드 단위나 기능 단위로 생성하는 것이 오류를 줄인다.

---

## 3.2 Controller Generation Pattern

### [개념]

Controller Generation Pattern은 REST API Controller 코드 생성에 특화된 Prompt 패턴이다.

Controller는 HTTP 요청 처리, 입력 검증 연결, Service 호출, 응답 반환에 집중해야 한다.

---

### [핵심]

- Controller는 비즈니스 로직을 포함하지 않는다.
- Request DTO를 사용한다.
- Response DTO를 반환한다.
- Service를 호출한다.
- ApiResponse<T> 같은 프로젝트 응답 규칙을 따른다.
- Validation Annotation 사용 여부를 명시한다.
- 예외 처리는 GlobalExceptionHandler에 위임한다.

---

### [실무]

Controller Generation Prompt:

```text
Task:
Generate Controller endpoint code.

Rules:
- Controller only handles request mapping and response.
- Delegate business logic to Service.
- Use Request DTO and Response DTO.
- Return ApiResponse<T> directly if this is the project rule.
- Do not catch business exceptions in Controller.

Output:
## Endpoint Summary
## Request / Response
## Controller Code Snippet
## Validation Checklist
```

Controller 생성 시 API 경로와 HTTP Method는 반드시 제공해야 한다.

제공되지 않았다면 Missing Information으로 표시한다.

---

### [FAQ]

Q. Controller Generation Pattern은 뭐야?

A. REST API Controller가 요청 처리, Service 호출, 응답 반환만 담당하도록 생성하는 Prompt 패턴이다.

Q. Controller에 비즈니스 로직을 넣어도 돼?

A. 권장하지 않는다. 비즈니스 로직은 Service Layer에 둔다.

Q. API 경로가 없으면 어떻게 해야 해?

A. 임의로 확정하지 말고 Missing Information으로 표시해야 한다.

---

## 3.3 Repository Generation Pattern

### [개념]

Repository Generation Pattern은 Persistence Layer 코드 생성에 특화된 Prompt 패턴이다.

Repository는 DB 접근을 담당하며 Spring Data JPA Query Method, JPQL, QueryDSL 등을 사용할 수 있다.

---

### [핵심]

- Entity 기준으로 Repository를 작성한다.
- 필요한 Query Method를 명확히 한다.
- 메서드명은 Entity 필드와 일치해야 한다.
- 복잡한 조회는 QueryDSL 또는 Custom Repository를 고려한다.
- 존재하지 않는 필드 기반 메서드를 생성하지 않는다.
- N+1 위험이 있는 조회는 fetch join 또는 EntityGraph를 검토한다.

---

### [실무]

Repository Generation Prompt:

```text
Task:
Generate Repository method suggestions.

Context:
- Entity fields are provided.
- Spring Data JPA is used.
- QueryDSL may be used for complex dynamic queries.

Constraints:
- Do not create methods using fields not present in Entity.
- Mark uncertain methods as assumptions.
- Separate simple query methods and complex query options.

Output:
## Required Queries
## Repository Method Candidates
## QueryDSL Needed
## Missing Information
## Validation Checklist
```

Repository 생성은 Entity 필드 정보가 없으면 확정할 수 없다.

---

### [FAQ]

Q. Repository Generation Pattern은 뭐야?

A. Entity와 조회 요구사항을 기준으로 Repository 메서드나 QueryDSL 구조를 생성하는 Prompt 패턴이다.

Q. Repository 메서드 생성에서 중요한 것은 뭐야?

A. Entity 필드명과 메서드명이 정확히 일치해야 한다는 점이다.

Q. Entity 필드가 없으면 Repository 메서드를 만들 수 있어?

A. 확정할 수 없다. Missing Information으로 표시해야 한다.

---

# 4. Code Review Prompt

## 4.1 Code Review Prompt Definition

### [개념]

Code Review Prompt는 LLM이 코드를 기준에 따라 검토하도록 지시하는 Prompt다.

Code Review Prompt는 단순 감상이 아니라 검증 기준 기반 분석이다.

좋은 Code Review Prompt는 아래 요소를 포함한다.

```text
Review Target
→ Review Criteria
→ Severity
→ Reason
→ Risk
→ Fix Direction
→ Missing Information
→ Checklist
```

---

### [핵심]

- Review Target을 명확히 한다.
- Review Criteria를 명시한다.
- Severity를 포함한다.
- 문제, 원인, 위험, 수정 방향을 분리한다.
- 취향과 결함을 구분한다.
- 보이는 코드와 보이지 않는 코드를 구분한다.
- 프로젝트 규칙을 기준으로 검토한다.
- Missing Information을 표시한다.

---

### [실무]

Code Review Prompt 예시:

```text
You are a Backend Review Agent.

Task:
Review the provided Spring Boot Service code.

Review Criteria:
- Transaction boundary
- N+1 query risk
- Null safety
- Exception handling
- DTO conversion responsibility
- API response consistency
- Maintainability

Rules:
- Review only provided code.
- Do not make claims about unseen files.
- Separate confirmed issues and possible risks.

Output:
## Review Summary
## Findings
### 1. Problem
- Severity:
- Cause:
- Risk:
- Fix Direction:
## Missing Information
## Checklist
```

Code Review Prompt는 “이 코드 괜찮아?”보다 “어떤 기준으로 검토할지”를 명확히 해야 한다.

---

### [FAQ]

Q. Code Review Prompt가 뭐야?

A. LLM이 코드를 정해진 검증 기준에 따라 검토하도록 지시하는 Prompt다.

Q. Code Review Prompt에는 뭐가 필요해?

A. 리뷰 대상, 검증 기준, Severity, 원인, 위험, 수정 방향, Missing Information, Checklist가 필요하다.

Q. 코드 리뷰에서 가장 중요한 규칙은 뭐야?

A. 보이는 코드만 확정적으로 리뷰하고, 보이지 않는 부분은 단정하지 않는 것이다.

Q. “괜찮아?”라고만 물어보면 왜 부족해?

A. 검토 기준이 없어 단순 감상이나 일반적인 조언으로 흐를 수 있다.

---

# 5. Code Review Criteria

## 5.1 Architecture Review Criteria

### [개념]

Architecture Review Criteria는 코드가 프로젝트 아키텍처와 책임 분리 원칙을 지키는지 검토하는 기준이다.

---

### [핵심]

검토 항목:

- Controller에 비즈니스 로직이 있는가?
- Service가 비즈니스 로직을 담당하는가?
- Repository가 Persistence 책임만 가지는가?
- DTO와 Entity 책임이 분리되어 있는가?
- API Response 규칙이 일관적인가?
- Exception Handling 위치가 적절한가?
- Layer 간 의존 방향이 올바른가?

---

### [실무]

Architecture Review Prompt:

```text
Review architecture consistency.

Check:
- Controller responsibility
- Service responsibility
- Repository responsibility
- DTO / Entity separation
- Exception handling flow
- API response consistency

Return:
- Problem
- Cause
- Risk
- Fix Direction
- Severity
```

Architecture Review는 취향이 아니라 유지보수성과 변경 가능성 기준으로 판단한다.

---

### [FAQ]

Q. Architecture Review Criteria는 뭐야?

A. 코드가 프로젝트 계층 구조와 책임 분리 원칙을 지키는지 검토하는 기준이다.

Q. Controller에 비즈니스 로직이 있으면 왜 문제야?

A. 요청 처리와 비즈니스 판단이 섞여 테스트와 유지보수가 어려워지기 때문이다.

Q. DTO와 Entity를 분리해야 하는 이유는 뭐야?

A. API 외부 계약과 내부 도메인 모델을 분리해 변경 영향을 줄이기 위해서다.

---

## 5.2 Transaction Review Criteria

### [개념]

Transaction Review Criteria는 데이터 변경 작업이 적절한 트랜잭션 경계 안에서 수행되는지 검토하는 기준이다.

---

### [핵심]

검토 항목:

- 쓰기 작업에 @Transactional이 있는가?
- 읽기 작업에 readOnly=true가 적절히 사용되는가?
- 여러 Entity 변경이 하나의 트랜잭션으로 묶였는가?
- Transaction Boundary가 Controller에 있지 않은가?
- 외부 API 호출이 트랜잭션 내부에 과도하게 포함되지 않았는가?
- Lazy Loading 접근 위치가 안전한가?

---

### [실무]

Transaction Review Prompt:

```text
Review transaction boundary.

Check:
- Write operations require @Transactional.
- Read operations may use @Transactional(readOnly = true).
- Transaction boundary should be in Service layer.
- Partial update risk should be identified.

Output each finding with severity, cause, risk, and fix direction.
```

Transaction 문제는 런타임 오류와 데이터 정합성 문제로 이어질 수 있으므로 우선순위가 높다.

---

### [FAQ]

Q. Transaction Review Criteria는 뭐야?

A. 데이터 변경 작업이 적절한 트랜잭션 경계 안에서 수행되는지 검토하는 기준이다.

Q. Transaction Boundary는 어디에 두는 게 좋아?

A. 일반적으로 Service Layer에 둔다.

Q. Transaction 문제가 왜 위험해?

A. 예외 발생 시 부분 업데이트나 데이터 정합성 문제가 생길 수 있기 때문이다.

---

## 5.3 N+1 Review Criteria

### [개념]

N+1 Review Criteria는 JPA 조회 코드에서 불필요한 추가 쿼리가 발생할 가능성을 검토하는 기준이다.

N+1 문제는 성능 저하의 대표 원인이다.

---

### [핵심]

검토 항목:

- 반복문 안에서 Lazy Association에 접근하는가?
- 목록 조회 후 연관 Entity를 반복 접근하는가?
- fetch join이 필요한 조회인가?
- EntityGraph가 적합한가?
- DTO Projection이 적합한가?
- QueryDSL로 동적 조회 최적화가 필요한가?
- 페이징과 fetch join 충돌 가능성이 있는가?

---

### [실무]

N+1 Review Prompt:

```text
Review N+1 query risk.

Check:
- Lazy association access inside loops
- List query followed by relation access
- Need for fetch join, EntityGraph, or DTO projection
- Pagination compatibility

Return:
- Confirmed risk
- Possible risk
- Missing information
- Fix direction
```

N+1은 코드 일부만으로 확정하기 어려울 수 있으므로 Entity 연관관계와 조회 흐름이 필요하다.

---

### [FAQ]

Q. N+1 Review Criteria는 뭐야?

A. JPA 조회에서 불필요한 추가 쿼리가 반복 발생할 가능성을 검토하는 기준이다.

Q. N+1은 코드 일부만 보고 확정할 수 있어?

A. 어려울 수 있다. Entity 연관관계, FetchType, 조회 흐름이 필요하다.

Q. N+1 해결 방향은 뭐야?

A. fetch join, EntityGraph, DTO Projection, QueryDSL 최적화 등을 검토할 수 있다.

---

## 5.4 Exception Handling Review Criteria

### [개념]

Exception Handling Review Criteria는 예외 처리 흐름이 프로젝트 규칙에 맞고 안전한지 검토하는 기준이다.

---

### [핵심]

검토 항목:

- null 반환으로 실패를 표현하지 않는가?
- generic Exception을 삼키지 않는가?
- RuntimeException을 무분별하게 던지지 않는가?
- Domain Exception을 사용하는가?
- GlobalExceptionHandler와 연결되는가?
- 민감한 내부 오류 메시지를 노출하지 않는가?
- 예외 상황별 응답이 일관적인가?

---

### [실무]

Exception Handling Review Prompt:

```text
Review exception handling.

Check:
- No null return on failure
- No swallowed exception
- Domain exception usage
- GlobalExceptionHandler consistency
- No sensitive error message exposure
- Consistent API error response
```

Exception Handling은 API 안정성과 디버깅 가능성에 직접 영향을 준다.

---

### [FAQ]

Q. Exception Handling Review Criteria는 뭐야?

A. 예외 처리 방식이 프로젝트 규칙에 맞고 안전한지 검토하는 기준이다.

Q. 실패 시 null을 반환하면 왜 문제야?

A. 호출부에서 NullPointerException이 발생하거나 실패 원인이 숨겨질 수 있다.

Q. 예외는 어디에서 응답으로 변환하는 게 좋아?

A. Spring Boot에서는 GlobalExceptionHandler에서 일관된 API 응답으로 변환하는 구조가 일반적이다.

---

## 5.5 DTO Responsibility Review Criteria

### [개념]

DTO Responsibility Review Criteria는 DTO, Entity, Controller, Service 간 데이터 변환 책임이 적절한지 검토하는 기준이다.

---

### [핵심]

검토 항목:

- Entity를 API 응답으로 직접 반환하지 않는가?
- Request DTO와 Response DTO가 분리되어 있는가?
- DTO 변환 책임이 과도하게 분산되지 않았는가?
- Entity 내부 상태가 외부에 노출되지 않는가?
- Controller가 과도한 변환 로직을 갖지 않는가?
- Service가 필요한 응답 DTO를 적절히 구성하는가?

---

### [실무]

DTO Review Prompt:

```text
Review DTO responsibility.

Check:
- Entity is not returned directly from API.
- Request DTO and Response DTO are separated.
- DTO conversion does not overload Controller.
- Entity internal state is not exposed.
- Response structure follows project rule.
```

DTO 책임은 API 안정성과 변경 영향도를 줄이는 데 중요하다.

---

### [FAQ]

Q. DTO Responsibility Review Criteria는 뭐야?

A. DTO와 Entity, Controller, Service 간 데이터 전달과 변환 책임이 적절한지 검토하는 기준이다.

Q. Entity를 API 응답으로 직접 반환하면 왜 문제야?

A. 내부 도메인 구조가 외부에 노출되고 변경 영향이 커질 수 있기 때문이다.

Q. DTO 변환은 어디서 해야 해?

A. 프로젝트 규칙에 따라 다르지만 Controller에 과도한 변환 로직을 두는 것은 피하는 것이 좋다.

---

# 6. Code Review Output Pattern

## 6.1 Finding Structure

### [개념]

Finding Structure는 Code Review 결과에서 각 문제를 일관된 형식으로 표현하는 구조다.

Finding은 문제만 말하는 것이 아니라 원인, 위험, 수정 방향까지 포함해야 한다.

---

### [핵심]

Finding 필수 요소:

- Problem
- Severity
- Cause
- Risk
- Fix Direction
- Evidence
- Missing Information

Severity 예시:

- Critical
- High
- Medium
- Low
- Info

---

### [실무]

Code Review Finding 구조:

```md
### 1. Transaction Boundary 누락

- Severity: High
- Problem: 쓰기 작업에 트랜잭션 경계가 명확하지 않음
- Cause: Service 메서드에 @Transactional이 없음
- Risk: 예외 발생 시 부분 업데이트 가능성
- Fix Direction: Service 메서드에 @Transactional 적용
- Evidence: 제공된 Service 코드 기준
```

Finding은 Review Agent와 Fix Agent가 바로 사용할 수 있는 구조여야 한다.

---

### [FAQ]

Q. Code Review Finding에는 뭐가 들어가야 해?

A. Problem, Severity, Cause, Risk, Fix Direction, Evidence, Missing Information이 들어가면 좋다.

Q. Severity는 왜 필요해?

A. 문제의 우선순위를 판단하고 수정 순서를 정하기 위해 필요하다.

Q. 문제만 말하면 부족해?

A. 부족하다. 원인과 위험, 수정 방향까지 있어야 실제 수정에 사용할 수 있다.

---

# 7. Refactoring Prompt

## 7.1 Refactoring Prompt Definition

### [개념]

Refactoring Prompt는 기존 기능을 유지하면서 코드 구조를 개선하도록 지시하는 Prompt다.

Refactoring은 기능 변경이 아니다.

Refactoring Prompt는 기능 유지, 변경 범위, 금지 범위, 위험, 테스트 체크를 명확히 해야 한다.

기본 구조:

```text
Preserve Behavior
→ Refactoring Goal
→ Target Scope
→ Before / After
→ Constraint
→ Risk
→ Test Check
```

---

### [핵심]

- 기존 기능을 유지해야 한다.
- Refactoring Goal을 명확히 한다.
- Target Scope를 제한한다.
- 변경 금지 범위를 명시한다.
- API 계약 유지 여부를 명시한다.
- 구조 변경 이유를 설명해야 한다.
- Test Check를 포함한다.
- 기능 개선과 리팩토링을 과도하게 섞지 않는다.

---

### [실무]

Refactoring Prompt 예시:

```text
Task:
Refactor the Service code while preserving behavior.

Goal:
Separate business logic and DTO conversion responsibility.

Constraints:
- Do not change Controller signatures.
- Do not change API paths.
- Do not change Repository method signatures.
- Preserve existing response structure.
- Do not add new business rules.

Output:
## Refactoring Summary
## Before Problem
## After Structure
## Refactored Code Snippet
## Risk
## Test Checklist
```

Refactoring Prompt는 “기능 유지”를 반드시 명시해야 한다.

---

### [FAQ]

Q. Refactoring Prompt가 뭐야?

A. 기존 기능을 유지하면서 코드 구조를 개선하도록 지시하는 Prompt다.

Q. Refactoring과 기능 개선은 달라?

A. 다르다. Refactoring은 외부 동작을 유지하면서 내부 구조를 개선하는 작업이다.

Q. Refactoring Prompt에서 가장 중요한 조건은 뭐야?

A. Preserve Behavior, 변경 범위, 변경 금지 범위, 테스트 체크다.

Q. 리팩토링하면서 API 경로를 바꿔도 돼?

A. 요청이 없다면 바꾸면 안 된다. 기존 API 계약을 유지해야 한다.

---

# 8. Refactoring Prompt Patterns

## 8.1 Service Refactoring Pattern

### [개념]

Service Refactoring Pattern은 Service Layer의 책임과 구조를 개선하는 Prompt 패턴이다.

주로 비즈니스 로직 분리, 트랜잭션 경계 정리, DTO 변환 책임 정리에 사용한다.

---

### [핵심]

- 기존 동작을 유지한다.
- Service 책임을 명확히 한다.
- Transaction Boundary를 정리한다.
- DTO 변환 책임을 정리한다.
- 중복 로직을 제거한다.
- Controller와 Repository 시그니처 변경을 피한다.
- 테스트 체크리스트를 포함한다.

---

### [실무]

Service Refactoring Prompt:

```text
Refactor the Service layer.

Preserve:
- Existing API behavior
- Controller signatures
- Repository signatures
- Response DTO structure

Improve:
- Transaction boundary
- Business logic readability
- Exception handling consistency
- DTO conversion responsibility

Return:
## Refactoring Summary
## Problems
## Refactored Structure
## Code Snippet
## Test Checklist
```

Service Refactoring은 변경 영향이 크므로 Before / After 구조를 함께 요청하는 것이 좋다.

---

### [FAQ]

Q. Service Refactoring Pattern은 뭐야?

A. Service Layer의 비즈니스 로직, 트랜잭션, 예외 처리, DTO 변환 구조를 개선하는 Prompt 패턴이다.

Q. Service 리팩토링에서 바꾸면 안 되는 것은 뭐야?

A. 요청이 없다면 Controller 시그니처, API 경로, Repository 시그니처, 응답 구조를 바꾸면 안 된다.

Q. Refactoring 결과에는 뭐가 있어야 해?

A. 변경 요약, 기존 문제, 개선 구조, 코드 snippet, 테스트 체크리스트가 있어야 한다.

---

## 8.2 Controller Refactoring Pattern

### [개념]

Controller Refactoring Pattern은 Controller의 책임을 HTTP 요청/응답 처리로 제한하도록 개선하는 Prompt 패턴이다.

---

### [핵심]

- 비즈니스 로직을 Service로 이동한다.
- Controller는 Request Mapping과 Service 호출에 집중한다.
- 입력 검증을 DTO Validation과 연결한다.
- 응답 형식을 프로젝트 규칙에 맞춘다.
- 예외 처리는 GlobalExceptionHandler에 위임한다.
- API 경로와 Method는 유지한다.

---

### [실무]

Controller Refactoring Prompt:

```text
Refactor Controller while preserving API contract.

Preserve:
- API path
- HTTP method
- Request DTO
- Response DTO
- Controller method signature if possible

Improve:
- Move business logic to Service
- Remove direct Repository access
- Keep response format consistent
- Delegate exceptions to GlobalExceptionHandler

Output:
## Refactoring Summary
## Moved Responsibility
## Controller Code Snippet
## Required Service Changes
## Test Checklist
```

Controller Refactoring은 API 계약 유지가 중요하다.

---

### [FAQ]

Q. Controller Refactoring Pattern은 뭐야?

A. Controller가 요청 처리와 Service 호출에 집중하도록 책임을 정리하는 Prompt 패턴이다.

Q. Controller에서 제거해야 할 것은 뭐야?

A. 비즈니스 로직, 직접 Repository 접근, 복잡한 DTO 변환, 예외 응답 직접 생성 로직을 줄이는 것이 좋다.

Q. Controller 리팩토링에서 유지해야 할 것은 뭐야?

A. API 경로, HTTP Method, 요청/응답 구조, 기존 외부 동작을 유지해야 한다.

---

# 9. Debugging Prompt

## 9.1 Debugging Prompt Definition

### [개념]

Debugging Prompt는 오류 원인을 찾고 해결 방향을 제시하도록 LLM에 지시하는 Prompt다.

Debugging Prompt는 증상, 에러 메시지, 로그, 환경, 최근 변경, 재현 절차를 포함해야 한다.

기본 구조:

```text
Symptom
→ Error Message
→ Stack Trace
→ Environment
→ Recent Change
→ Reproduction Step
→ Expected Result
→ Actual Result
→ Investigation
→ Fix Direction
```

---

### [핵심]

- 증상을 명확히 작성한다.
- 에러 메시지 원문을 포함한다.
- Stack Trace를 포함한다.
- 실행 환경과 버전을 포함한다.
- 최근 변경 사항을 포함한다.
- 재현 절차를 포함한다.
- 기대 결과와 실제 결과를 구분한다.
- 원인 후보와 확정 원인을 구분한다.
- 임의로 원인을 확정하지 않는다.

---

### [실무]

Debugging Prompt Template:

```text
Task:
Debug the issue.

Symptom:
[What happened]

Error Message:
[Exact error message]

Stack Trace:
[Paste stack trace]

Environment:
- OS:
- Runtime:
- Framework:
- Database:
- Build Tool:

Recent Change:
[What changed recently]

Reproduction Step:
1.
2.
3.

Expected Result:
[Expected behavior]

Actual Result:
[Actual behavior]

Output:
## Likely Causes
## Confirmed Facts
## Missing Information
## Fix Direction
## Verification Steps
```

Debugging Prompt는 “안 돼”가 아니라 “재현 가능한 문제 정보”를 제공해야 한다.

---

### [FAQ]

Q. Debugging Prompt가 뭐야?

A. 오류 원인을 찾고 해결 방향을 제시하도록 증상, 로그, 환경, 재현 절차를 제공하는 Prompt다.

Q. Debugging Prompt에는 뭐가 필요해?

A. 증상, 에러 메시지, Stack Trace, 환경, 최근 변경, 재현 절차, 기대 결과, 실제 결과가 필요하다.

Q. 에러 로그 없이 디버깅 가능해?

A. 가능은 하지만 정확도가 낮다. 에러 메시지와 로그가 가장 중요하다.

Q. 원인을 바로 확정해도 돼?

A. 근거가 충분하지 않으면 원인 후보로 제시하고 Missing Information을 표시해야 한다.

---

# 10. Debugging Prompt Patterns

## 10.1 Backend Debugging Pattern

### [개념]

Backend Debugging Pattern은 Spring Boot, API, DB, Security, JPA 오류 분석에 사용하는 Prompt 패턴이다.

---

### [핵심]

Backend Debugging 주요 Context:

- Error Message
- Stack Trace
- Controller / Service / Repository 코드
- Entity 매핑
- application.properties 또는 application.yml
- DB schema
- Request / Response
- 최근 변경 사항
- 실행 환경

---

### [실무]

Backend Debugging Prompt:

```text
Debug this Spring Boot issue.

Context:
- Java 21
- Spring Boot 3.x
- MySQL
- Spring Data JPA

Symptom:
[Describe symptom]

Error Message:
[Paste exact error]

Related Code:
- Controller:
- Service:
- Repository:
- Entity:

Recent Change:
[Describe recent change]

Output:
## Confirmed Facts
## Likely Causes
## Most Probable Cause
## Fix Direction
## Verification Steps
## Missing Information
```

Backend Debugging에서는 Stack Trace 상단과 Caused by 구간이 중요하다.

---

### [FAQ]

Q. Backend Debugging Pattern은 뭐야?

A. Spring Boot, JPA, Security, API 오류를 분석하기 위한 Debugging Prompt 패턴이다.

Q. Spring Boot 디버깅에서 중요한 정보는 뭐야?

A. 에러 메시지, Stack Trace, 관련 코드, 설정 파일, 최근 변경 사항, 요청 정보다.

Q. Stack Trace에서 어디를 봐야 해?

A. 실제 원인이 담긴 Caused by 구간과 프로젝트 코드가 등장하는 라인을 우선 확인한다.

---

## 10.2 Frontend Debugging Pattern

### [개념]

Frontend Debugging Pattern은 React, API 연동, 라우팅, 상태 관리, 빌드 오류 분석에 사용하는 Prompt 패턴이다.

---

### [핵심]

Frontend Debugging 주요 Context:

- Browser Console Error
- Network Tab Request / Response
- Component Code
- Routing Code
- Axios / Fetch Code
- Environment Variable
- Build Error
- 최근 변경 사항

---

### [실무]

Frontend Debugging Prompt:

```text
Debug this React issue.

Symptom:
[What happened in UI]

Console Error:
[Paste error]

Network:
- Request URL:
- Status Code:
- Response Body:

Related Code:
- Component:
- API Client:
- Router:

Environment:
- React
- Vite or CRA
- Browser

Output:
## Confirmed Facts
## Likely Causes
## Fix Direction
## Verification Steps
## Missing Information
```

Frontend Debugging에서는 Console 탭과 Network 탭 정보를 함께 제공해야 정확도가 높다.

---

### [FAQ]

Q. Frontend Debugging Pattern은 뭐야?

A. React UI, API 연동, 라우팅, 상태 관리, 빌드 오류를 분석하는 Prompt 패턴이다.

Q. Frontend 오류 분석에 필요한 정보는 뭐야?

A. Console Error, Network 요청/응답, 관련 Component 코드, API Client 코드, Router 코드가 필요하다.

Q. 화면만 보고 디버깅 가능해?

A. 가능하지만 정확도는 낮다. Console과 Network 정보를 함께 제공하는 것이 좋다.

---

## 10.3 RAG Debugging Pattern

### [개념]

RAG Debugging Pattern은 RAG 답변 실패, 검색 실패, 문서 미검색, Hallucination, Context 부족 문제를 분석하는 Prompt 패턴이다.

---

### [핵심]

RAG Debugging 주요 원인:

- 문서 Chunk가 너무 큼
- 문서 Chunk가 너무 작음
- Header가 불명확함
- FAQ가 부족함
- Retrieval Queries가 없음
- 용어가 불일치함
- 검색 질문과 문서 용어가 다름
- Top-K가 낮음
- Embedding Model이 도메인에 맞지 않음
- Retrieved Context가 부족함
- RAG Prompt에 Missing Information Rule이 없음

---

### [실무]

RAG Debugging Prompt:

```text
Debug this RAG retrieval issue.

Symptom:
[Example: The answer says "not found in document"]

Question:
[User question]

Retrieved Context:
[Retrieved chunks if available]

Document Context:
- File name:
- Section:
- Keywords:
- FAQ:
- Retrieval Queries:

RAG Settings:
- Chunk size:
- Overlap:
- Top-K:
- Embedding model:
- LLM:

Output:
## Confirmed Facts
## Likely Causes
## Retrieval Issues
## Document Fix Direction
## Prompt Fix Direction
## Validation Query
```

RAG Debugging은 문서 구조 문제와 Prompt 문제를 분리해서 분석해야 한다.

---

### [FAQ]

Q. RAG Debugging Pattern은 뭐야?

A. RAG 검색 실패, 문서 미검색, 답변 품질 저하, Hallucination 문제를 분석하는 Prompt 패턴이다.

Q. RAG가 문서를 못 찾는 이유는 뭐야?

A. Chunk 구조, Header, FAQ, Retrieval Queries, 용어 불일치, Top-K, Embedding 품질 문제일 수 있다.

Q. RAG Debugging에서는 무엇을 확인해야 해?

A. 사용자 질문, 검색된 Chunk, 문서 구조, FAQ, Retrieval Queries, Chunk 설정, RAG Prompt를 확인해야 한다.

---

# 11. Common Mistakes

## 11.1 Code Generation Mistakes

### [개념]

Code Generation Mistake는 Prompt가 불충분해 프로젝트와 맞지 않는 코드가 생성되는 문제다.

대부분 기술 스택, 기존 코드 Context, 제약, 예외 처리 기준이 부족할 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- 기술 스택과 버전 없음
- 기존 코드 Context 없음
- Entity / DTO / Repository 정보 없음
- API 경로 임의 생성
- 클래스명 임의 생성
- DB 필드 임의 생성
- Error Handling 기준 없음
- Transaction Rule 없음
- 테스트 기준 없음
- 전체 코드 생성 범위가 너무 큼

---

### [실무]

나쁜 Prompt:

```text
로그인 기능 만들어줘.
```

개선 Prompt:

```text
Spring Boot 3.x, Java 21 기준으로 Login Service 구현 계획을 작성해줘.

Context:
- AuthController code is provided.
- LoginReqDto code is provided.
- UserRepository code is provided.
- GlobalExceptionHandler handles exceptions.

Constraints:
- Do not invent missing classes.
- Do not change Controller signature.
- Do not create API paths.
- Mark Missing Information.

Output:
## Missing Information
## Method Flow
## Code Snippet
## Validation Checklist
```

Code Generation Prompt는 기존 프로젝트에 맞게 범위를 제한해야 한다.

---

### [FAQ]

Q. Code Generation에서 가장 흔한 실수는 뭐야?

A. 기술 스택, 기존 코드 Context, 제약 없이 코드 생성을 요청하는 것이다.

Q. 모델이 없는 클래스를 만들면 어떻게 해?

A. Missing Information Rule과 “Do not invent missing classes” 제약을 추가해야 한다.

Q. 코드 생성 범위가 너무 크면 어떻게 해?

A. 기능 단위, 계층 단위, 메서드 단위로 나눠 요청해야 한다.

---

## 11.2 Code Review Mistakes

### [개념]

Code Review Mistake는 검토 기준이 없거나 보이지 않는 코드까지 단정하는 문제다.

---

### [핵심]

자주 발생하는 실수:

- Review Criteria 없음
- Severity 없음
- 문제와 취향을 구분하지 않음
- 보이지 않는 코드 단정
- 프로젝트 규칙 미반영
- 원인 없이 문제만 나열
- 수정 방향 없음
- Missing Information 없음
- 런타임 위험과 스타일 선호를 같은 수준으로 취급

---

### [실무]

나쁜 Prompt:

```text
이 코드 괜찮아?
```

개선 Prompt:

```text
이 Service 코드를 리뷰해줘.

Review Criteria:
- Transaction Boundary
- N+1 Query Risk
- Exception Handling
- DTO Conversion Responsibility
- Null Safety

Rules:
- 보이는 코드만 확정적으로 판단해줘.
- 보이지 않는 파일은 Missing Information으로 표시해줘.
- 취향과 결함을 구분해줘.

Output:
문제 / 원인 / 위험 / 수정 방향 / Severity
```

Code Review Prompt는 판단 기준과 출력 구조가 있어야 실무적으로 유용하다.

---

### [FAQ]

Q. Code Review에서 가장 흔한 실수는 뭐야?

A. 검토 기준 없이 “괜찮아?”라고 묻거나 보이지 않는 코드까지 단정하는 것이다.

Q. 취향과 결함은 어떻게 구분해?

A. 런타임, 보안, 데이터 정합성 문제는 결함이고, 스타일 선호는 개선 제안으로 분리한다.

Q. 리뷰 결과에는 수정 방향이 꼭 필요해?

A. 필요하다. 문제만 나열하면 실제 수정에 활용하기 어렵다.

---

## 11.3 Refactoring Mistakes

### [개념]

Refactoring Mistake는 기능 유지 조건 없이 구조 변경을 요청해 외부 동작이 바뀌는 문제다.

---

### [핵심]

자주 발생하는 실수:

- Preserve Behavior 없음
- 변경 범위 없음
- API 계약 유지 조건 없음
- 기존 테스트 기준 없음
- 기능 개선과 리팩토링 혼합
- 불필요한 추상화 추가
- 시그니처 임의 변경
- 기존 호출부 영향 미확인

---

### [실무]

나쁜 Prompt:

```text
이 코드 더 좋게 바꿔줘.
```

개선 Prompt:

```text
기능은 유지하고 Service 내부 구조만 리팩토링해줘.

Constraints:
- Controller 시그니처 유지
- Repository 시그니처 유지
- API 응답 구조 유지
- 새로운 비즈니스 규칙 추가 금지

Output:
## Before Problem
## Refactoring Direction
## Code Snippet
## Behavior Preservation Checklist
```

Refactoring Prompt는 기능 유지와 변경 범위를 명확히 해야 한다.

---

### [FAQ]

Q. Refactoring에서 가장 흔한 실수는 뭐야?

A. 기능 유지 조건과 변경 범위를 명확히 하지 않는 것이다.

Q. 리팩토링 중 기능 개선도 같이 해도 돼?

A. 가능하지만 권장하지 않는다. 기능 개선과 리팩토링은 분리하는 것이 안전하다.

Q. 시그니처를 바꿔도 돼?

A. 요청이 없다면 기존 호출부 영향을 줄이기 위해 유지해야 한다.

---

## 11.4 Debugging Mistakes

### [개념]

Debugging Mistake는 로그, 환경, 재현 절차 없이 문제 해결을 요청하는 문제다.

이 경우 LLM은 원인을 추정할 수밖에 없고 정확도가 낮아진다.

---

### [핵심]

자주 발생하는 실수:

- “안 됨”만 제공
- Error Message 없음
- Stack Trace 없음
- 환경 정보 없음
- 최근 변경 사항 없음
- 재현 절차 없음
- 기대 결과와 실제 결과 구분 없음
- 원인 후보를 확정 원인처럼 받아들임
- 스크린샷만 있고 텍스트 로그 없음

---

### [실무]

나쁜 Prompt:

```text
서버 실행이 안 돼.
```

개선 Prompt:

```text
Spring Boot 서버 실행 오류를 디버깅해줘.

Environment:
- Java 21
- Spring Boot 3.x
- Gradle
- MySQL

Error Message:
[원문 붙여넣기]

Stack Trace:
[Caused by 포함]

Recent Change:
[최근 수정 내용]

Expected Result:
서버 정상 실행

Actual Result:
Application startup failed

Output:
## Confirmed Facts
## Likely Causes
## Fix Direction
## Verification Steps
## Missing Information
```

Debugging Prompt는 확인된 사실과 추정을 반드시 구분해야 한다.

---

### [FAQ]

Q. Debugging에서 가장 흔한 실수는 뭐야?

A. 에러 메시지, 로그, 환경, 재현 절차 없이 “안 된다”고만 요청하는 것이다.

Q. 스크린샷만 보내도 돼?

A. 가능하지만 텍스트 로그가 있어야 정확도가 높다.

Q. 원인 후보와 확정 원인은 구분해야 해?

A. 반드시 구분해야 한다. 근거가 부족하면 원인 후보로 표시해야 한다.

---

# 12. Best Practice

## 12.1 Code Generation Best Practice

### [개념]

Code Generation Best Practice는 프로젝트 구조와 기존 코드에 맞는 코드를 안정적으로 생성하기 위한 Prompt 작성 원칙이다.

---

### [핵심]

- 언어, 프레임워크, 버전을 명시한다.
- Architecture Context를 제공한다.
- Existing Code Context를 제공한다.
- Entity, DTO, Repository 관계를 제공한다.
- 변경 금지 범위를 명시한다.
- Error Handling Rule을 포함한다.
- Transaction Rule을 포함한다.
- Output Scope를 제한한다.
- Missing Information Rule을 포함한다.
- Validation Checklist를 포함한다.

---

### [실무]

Code Generation Best Practice Template:

```text
You are a [Domain] Code Generation Agent.

Task:
[Generate specific code or plan]

Stack:
[Language / Framework / Version]

Architecture:
[Layer / Responsibility / Response Rule]

Existing Code Context:
[Entity / DTO / Repository / Controller]

Constraints:
- Do not invent missing classes.
- Do not change existing signatures.
- Follow project rules.
- Mark missing information.

Output:
## Missing Information
## Assumptions
## Implementation Plan
## Code Snippet
## Validation Checklist
```

이 Template은 Backend, Frontend, AI Agent 코드 생성에 공통 적용 가능하다.

---

### [FAQ]

Q. Code Generation Best Practice는 뭐야?

A. 기술 스택, 아키텍처, 기존 코드, 제약, 예외 처리, 검증 기준을 명확히 제공하는 것이다.

Q. 코드 생성 Prompt에서 가장 먼저 적어야 할 것은 뭐야?

A. Task, 기술 스택, 기존 코드 Context, 변경 금지 조건이다.

Q. Missing Information Rule은 왜 필요해?

A. 부족한 정보를 모델이 임의로 만들지 않도록 막기 위해 필요하다.

---

## 12.2 Code Review Best Practice

### [개념]

Code Review Best Practice는 코드의 결함, 위험, 유지보수 문제를 기준 기반으로 검토하기 위한 Prompt 작성 원칙이다.

---

### [핵심]

- Review Target을 명확히 한다.
- Review Criteria를 명시한다.
- 프로젝트 규칙을 포함한다.
- Severity를 요구한다.
- 문제, 원인, 위험, 수정 방향을 분리한다.
- 보이는 코드만 확정적으로 판단한다.
- Missing Information을 표시한다.
- 취향과 결함을 구분한다.
- 최종 Checklist를 포함한다.

---

### [실무]

Code Review Best Practice Template:

```text
You are a [Domain] Review Agent.

Task:
Review [target code].

Context:
[Project stack and rules]

Review Criteria:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

Rules:
- Review only visible code.
- Do not make claims about unseen layers.
- Separate confirmed issues and possible risks.
- Separate defects and style preferences.

Output:
## Review Summary
## Findings
### 1. Problem
- Severity:
- Cause:
- Risk:
- Fix Direction:
## Missing Information
## Checklist
```

이 Template은 Backend Review Agent, Frontend Review Agent, AI Agent Review에 재사용할 수 있다.

---

### [FAQ]

Q. Code Review Best Practice는 뭐야?

A. 리뷰 대상, 검토 기준, 프로젝트 규칙, Severity, 수정 방향, Missing Information을 명확히 요청하는 것이다.

Q. Code Review에서 가장 중요한 출력 구조는 뭐야?

A. 문제, 원인, 위험, 수정 방향, Severity 구조다.

Q. 보이지 않는 코드는 어떻게 처리해?

A. 단정하지 않고 Missing Information으로 표시한다.

---

## 12.3 Refactoring Best Practice

### [개념]

Refactoring Best Practice는 기존 기능을 유지하면서 구조 개선을 안전하게 수행하기 위한 Prompt 작성 원칙이다.

---

### [핵심]

- Preserve Behavior를 명시한다.
- Refactoring Goal을 명확히 한다.
- Target Scope를 제한한다.
- 변경 금지 범위를 명시한다.
- API 계약 유지 여부를 명시한다.
- 불필요한 추상화를 피한다.
- Before / After 구조를 요청한다.
- Test Checklist를 포함한다.

---

### [실무]

Refactoring Best Practice Template:

```text
Task:
Refactor [target] while preserving behavior.

Goal:
[Refactoring goal]

Target Scope:
[Layer / class / method]

Preserve:
- API path
- Method signature
- Response structure
- Existing business behavior

Do Not:
- Do not add new business rules.
- Do not change external contract.
- Do not modify unrelated layers.

Output:
## Refactoring Summary
## Before Problem
## After Structure
## Code Snippet
## Risk
## Test Checklist
```

Refactoring은 변경 범위를 좁힐수록 안전하다.

---

### [FAQ]

Q. Refactoring Best Practice는 뭐야?

A. 기능 유지, 목표, 범위, 변경 금지 조건, 테스트 체크를 명확히 지정하는 것이다.

Q. 리팩토링 Prompt에서 가장 중요한 문장은 뭐야?

A. “Preserve existing behavior” 또는 “기능은 유지한다”는 조건이다.

Q. Refactoring 결과는 어떻게 검증해?

A. 기존 테스트, API 응답 비교, 주요 성공/실패 케이스 체크리스트로 검증한다.

---

## 12.4 Debugging Best Practice

### [개념]

Debugging Best Practice는 오류 분석에 필요한 증상, 로그, 환경, 재현 절차를 구조적으로 제공하는 Prompt 작성 원칙이다.

---

### [핵심]

- 증상을 명확히 작성한다.
- 에러 메시지 원문을 제공한다.
- Stack Trace를 제공한다.
- 실행 환경을 제공한다.
- 최근 변경 사항을 제공한다.
- 재현 절차를 제공한다.
- 기대 결과와 실제 결과를 구분한다.
- 원인 후보와 확정 사실을 구분한다.
- Verification Steps를 포함한다.

---

### [실무]

Debugging Best Practice Template:

```text
Task:
Debug [issue].

Symptom:
[Observed problem]

Error Message:
[Exact error message]

Stack Trace:
[Full or relevant stack trace]

Environment:
[OS / runtime / framework / DB / build tool]

Recent Change:
[Recent modification]

Reproduction Steps:
1.
2.
3.

Expected Result:
[Expected behavior]

Actual Result:
[Actual behavior]

Output:
## Confirmed Facts
## Likely Causes
## Most Probable Cause
## Fix Direction
## Verification Steps
## Missing Information
```

Debugging Prompt는 “원인 맞히기”가 아니라 “근거 기반 원인 후보 축소”를 목표로 한다.

---

### [FAQ]

Q. Debugging Best Practice는 뭐야?

A. 증상, 에러 메시지, Stack Trace, 환경, 최근 변경, 재현 절차, 기대/실제 결과를 구조적으로 제공하는 것이다.

Q. Debugging Prompt에서 가장 중요한 정보는 뭐야?

A. 에러 메시지 원문과 Stack Trace다.

Q. 디버깅 답변에는 무엇이 있어야 해?

A. 확인된 사실, 원인 후보, 가장 가능성 높은 원인, 수정 방향, 검증 단계, Missing Information이 있어야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Code Generation Prompt가 뭐야?
A. LLM이 프로젝트 규칙, 기술 스택, 기존 코드 구조에 맞는 코드를 생성하도록 지시하는 Prompt다.

Q. 코드 생성 Prompt에는 뭐가 필요해?
A. 언어, 프레임워크, 버전, 아키텍처, 기존 코드 Context, 제약, 예외 처리, 검증 기준이 필요하다.

Q. 코드 생성에서 가장 위험한 실수는 뭐야?
A. 존재하지 않는 클래스명, 필드명, API 경로, 비즈니스 규칙을 임의로 만드는 것이다.

Q. 코드 생성 Prompt에 기술 스택을 꼭 넣어야 해?
A. 넣는 것이 좋다. 언어, 프레임워크, 버전이 없으면 프로젝트와 맞지 않는 코드가 생성될 수 있다.

Q. Architecture Context가 뭐야?
A. 코드가 따라야 할 계층 구조와 책임 분리 규칙이다.

Q. Existing Code Context가 뭐야?
A. 생성 코드가 연결되어야 하는 기존 Entity, DTO, Repository, Controller, Config 같은 코드 정보다.

Q. Error Handling Rule은 왜 필요해?
A. null 반환, 예외 삼키기, RuntimeException 남발, 민감정보 노출을 막기 위해 필요하다.

Q. Transaction Rule은 뭐야?
A. 코드 생성 시 트랜잭션 경계를 어디에 둘지 정하는 규칙이다.

Q. Test Requirement는 뭐야?
A. 생성된 코드가 어떤 기준과 케이스로 검증되어야 하는지 정의하는 요소다.

Q. Service Generation Pattern은 뭐야?
A. Service Layer의 책임, 트랜잭션, 예외 처리, DTO 변환 기준을 명시해 코드를 생성하는 Prompt 패턴이다.

Q. Controller Generation Pattern은 뭐야?
A. REST API Controller가 요청 처리, Service 호출, 응답 반환만 담당하도록 생성하는 Prompt 패턴이다.

Q. Repository Generation Pattern은 뭐야?
A. Entity와 조회 요구사항을 기준으로 Repository 메서드나 QueryDSL 구조를 생성하는 Prompt 패턴이다.

Q. Code Review Prompt가 뭐야?
A. LLM이 코드를 정해진 검증 기준에 따라 검토하도록 지시하는 Prompt다.

Q. Code Review Prompt에는 뭐가 필요해?
A. 리뷰 대상, 검증 기준, Severity, 원인, 위험, 수정 방향, Missing Information, Checklist가 필요하다.

Q. 코드 리뷰에서 가장 중요한 규칙은 뭐야?
A. 보이는 코드만 확정적으로 리뷰하고, 보이지 않는 부분은 단정하지 않는 것이다.

Q. Architecture Review Criteria는 뭐야?
A. 코드가 프로젝트 계층 구조와 책임 분리 원칙을 지키는지 검토하는 기준이다.

Q. Transaction Review Criteria는 뭐야?
A. 데이터 변경 작업이 적절한 트랜잭션 경계 안에서 수행되는지 검토하는 기준이다.

Q. N+1 Review Criteria는 뭐야?
A. JPA 조회에서 불필요한 추가 쿼리가 반복 발생할 가능성을 검토하는 기준이다.

Q. Exception Handling Review Criteria는 뭐야?
A. 예외 처리 방식이 프로젝트 규칙에 맞고 안전한지 검토하는 기준이다.

Q. DTO Responsibility Review Criteria는 뭐야?
A. DTO와 Entity, Controller, Service 간 데이터 전달과 변환 책임이 적절한지 검토하는 기준이다.

Q. Code Review Finding에는 뭐가 들어가야 해?
A. Problem, Severity, Cause, Risk, Fix Direction, Evidence, Missing Information이 들어가면 좋다.

Q. Refactoring Prompt가 뭐야?
A. 기존 기능을 유지하면서 코드 구조를 개선하도록 지시하는 Prompt다.

Q. Refactoring과 기능 개선은 달라?
A. 다르다. Refactoring은 외부 동작을 유지하면서 내부 구조를 개선하는 작업이다.

Q. Refactoring Prompt에서 가장 중요한 조건은 뭐야?
A. Preserve Behavior, 변경 범위, 변경 금지 범위, 테스트 체크다.

Q. Service Refactoring Pattern은 뭐야?
A. Service Layer의 비즈니스 로직, 트랜잭션, 예외 처리, DTO 변환 구조를 개선하는 Prompt 패턴이다.

Q. Controller Refactoring Pattern은 뭐야?
A. Controller가 요청 처리와 Service 호출에 집중하도록 책임을 정리하는 Prompt 패턴이다.

Q. Debugging Prompt가 뭐야?
A. 오류 원인을 찾고 해결 방향을 제시하도록 증상, 로그, 환경, 재현 절차를 제공하는 Prompt다.

Q. Debugging Prompt에는 뭐가 필요해?
A. 증상, 에러 메시지, Stack Trace, 환경, 최근 변경, 재현 절차, 기대 결과, 실제 결과가 필요하다.

Q. Backend Debugging Pattern은 뭐야?
A. Spring Boot, JPA, Security, API 오류를 분석하기 위한 Debugging Prompt 패턴이다.

Q. Frontend Debugging Pattern은 뭐야?
A. React UI, API 연동, 라우팅, 상태 관리, 빌드 오류를 분석하는 Prompt 패턴이다.

Q. RAG Debugging Pattern은 뭐야?
A. RAG 검색 실패, 문서 미검색, 답변 품질 저하, Hallucination 문제를 분석하는 Prompt 패턴이다.

Q. Code Generation에서 가장 흔한 실수는 뭐야?
A. 기술 스택, 기존 코드 Context, 제약 없이 코드 생성을 요청하는 것이다.

Q. Code Review에서 가장 흔한 실수는 뭐야?
A. 검토 기준 없이 “괜찮아?”라고 묻거나 보이지 않는 코드까지 단정하는 것이다.

Q. Refactoring에서 가장 흔한 실수는 뭐야?
A. 기능 유지 조건과 변경 범위를 명확히 하지 않는 것이다.

Q. Debugging에서 가장 흔한 실수는 뭐야?
A. 에러 메시지, 로그, 환경, 재현 절차 없이 “안 된다”고만 요청하는 것이다.

Q. Code Generation Best Practice는 뭐야?
A. 기술 스택, 아키텍처, 기존 코드, 제약, 예외 처리, 검증 기준을 명확히 제공하는 것이다.

Q. Code Review Best Practice는 뭐야?
A. 리뷰 대상, 검토 기준, 프로젝트 규칙, Severity, 수정 방향, Missing Information을 명확히 요청하는 것이다.

Q. Refactoring Best Practice는 뭐야?
A. 기능 유지, 목표, 범위, 변경 금지 조건, 테스트 체크를 명확히 지정하는 것이다.

Q. Debugging Best Practice는 뭐야?
A. 증상, 에러 메시지, Stack Trace, 환경, 최근 변경, 재현 절차, 기대/실제 결과를 구조적으로 제공하는 것이다.
