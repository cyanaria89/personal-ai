# Prompt Engineering Part04 Context Prompt, RAG Prompt, Few-Shot Prompt

---

# 1. Context Prompt

## 1.1 Context Prompt Definition

### [개념]

Context Prompt는 LLM이 답변할 때 참고해야 하는 배경 정보와 판단 근거를 제공하는 Prompt다.

Context는 단순 설명이 아니라 답변 정확도를 결정하는 입력 정보다.

Context Prompt에는 아래 정보가 포함될 수 있다.

```text
Project Context
→ Domain Context
→ Code Context
→ Business Rule
→ Environment
→ Constraint
→ Existing Decision
→ Retrieved Context
```

Context Prompt의 목적은 LLM이 일반론이 아니라 제공된 상황과 규칙에 맞춰 답변하도록 만드는 것이다.

---

### [핵심]

- Context Prompt는 LLM의 판단 근거다.
- Context가 부족하면 답변이 일반론으로 흐른다.
- Context가 부정확하면 잘못된 답변이 생성된다.
- Context와 Task는 분리해서 작성해야 한다.
- RAG 검색 결과는 Context Prompt로 주입된다.
- 프로젝트 고유 규칙은 Context에 명확히 포함해야 한다.
- 오래된 Context와 최신 Context 충돌을 주의해야 한다.
- 관련 없는 Context를 과도하게 넣으면 핵심이 흐려진다.

---

### [실무]

2026 실무 기준 Context Prompt는 작업에 필요한 정보만 구조화해서 제공한다.

좋은 구조:

```text
Task:
Review the provided Spring Boot Service code.

Project Context:
- Java 21
- Spring Boot 3.x
- MySQL
- Spring Data JPA
- ApiResponse<T> is used for response body
- GlobalExceptionHandler handles exceptions

Code Context:
- Entity, DTO, Repository are provided
- Service should handle business logic
- Controller should not contain business logic

Constraints:
- Do not invent missing classes
- Do not change existing API path
- Mark assumptions clearly
```

Context는 LLM이 “무엇을 기준으로 판단해야 하는지”를 제공한다.

Context가 좋을수록 Code Generation, Code Review, RAG Answer, Agent Handoff 품질이 좋아진다.

---

### [FAQ]

Q. Context Prompt가 뭐야?

A. LLM이 답변할 때 참고해야 하는 프로젝트 상황, 코드 구조, 규칙, 검색 문서 같은 배경 정보를 제공하는 Prompt다.

Q. Context Prompt는 왜 중요해?

A. LLM은 제공된 Context를 기준으로 답변하므로 Context가 부족하면 일반론이나 잘못된 답변이 나올 수 있다.

Q. Context와 Task는 분리해야 해?

A. 그렇다. Context는 판단 근거이고 Task는 수행할 작업이므로 분리해야 Prompt가 명확해진다.

Q. RAG 검색 결과도 Context야?

A. 그렇다. RAG에서 검색된 문서는 LLM에게 주입되는 Retrieved Context다.

---

# 2. Context Prompt Components

## 2.1 Project Context

### [개념]

Project Context는 프로젝트의 기술 스택, 아키텍처, 규칙, 기존 결정을 설명하는 Context다.

Project Context는 LLM이 프로젝트 고유 기준을 따르도록 만든다.

---

### [핵심]

- 기술 스택을 명시한다.
- 버전을 명시한다.
- 아키텍처 규칙을 명시한다.
- 응답 형식과 예외 처리 규칙을 명시한다.
- 기존 결정사항을 포함한다.
- 프로젝트 고유 규칙은 일반 지식보다 우선한다.
- 프로젝트 Context가 없으면 모델이 임의 구조를 만들 수 있다.

---

### [실무]

Project Context 예시:

```text
Project Context:
- Java 21
- Spring Boot 3.x
- Spring Data JPA
- MySQL
- Layered Architecture: Controller → Service → Repository
- Controller returns ApiResponse<T> directly
- GlobalExceptionHandler handles exceptions
- Business logic belongs to Service
- Repository uses Spring Data JPA query methods
```

Code Generation에서는 Project Context가 없으면 모델이 프로젝트에 없는 구조를 만들 수 있다.

Code Review에서는 Project Context가 없으면 실제 프로젝트 규칙과 다른 기준으로 리뷰할 수 있다.

---

### [FAQ]

Q. Project Context는 뭐야?

A. 프로젝트의 기술 스택, 버전, 아키텍처, 응답 규칙, 예외 처리 규칙 같은 프로젝트 고유 배경 정보다.

Q. Project Context가 없으면 어떻게 돼?

A. 모델이 일반적인 구조나 존재하지 않는 프로젝트 규칙을 기준으로 답변할 수 있다.

Q. 프로젝트 규칙은 Context야, Constraint야?

A. 참고 정보로 제공하면 Context이고 반드시 지켜야 할 조건이면 Constraint로 명시하는 것이 좋다.

---

## 2.2 Domain Context

### [개념]

Domain Context는 특정 기술 도메인이나 업무 영역에서 적용해야 할 기준이다.

Prompt Engineering, Backend, Frontend, Security, AI Agent, DevOps 같은 도메인별 규칙이 Domain Context가 될 수 있다.

---

### [핵심]

- Domain Context는 도메인별 판단 기준을 제공한다.
- Domain Rules와 연결된다.
- 도메인 키워드를 명확히 포함해야 한다.
- Agent별 Domain Context는 다르게 구성한다.
- Backend Agent와 Frontend Agent의 Context는 분리한다.
- Prompt Engineering 문서는 Prompt, RAG, Agent Workflow 중심으로 구성한다.

---

### [실무]

Prompt Engineering Domain Context 예시:

```text
Domain Context:
- Prompt Engineering
- Instruction Design
- Role Prompt
- System Prompt
- User Prompt
- Context Prompt
- RAG Prompt
- Few-Shot Prompt
- Structured Output
- Hallucination Prevention
- Agent Prompt
- Multi-Agent Workflow
```

Backend Domain Context 예시:

```text
Domain Context:
- REST API Design
- DTO Responsibility
- Transaction Boundary
- Exception Handling
- N+1 Query Risk
- Repository Query Method
- Service Layer Responsibility
```

Domain Context는 RAG 검색 키워드와도 연결되므로 용어 통일이 중요하다.

---

### [FAQ]

Q. Domain Context는 뭐야?

A. 특정 기술 도메인이나 업무 영역에서 적용해야 할 기준과 핵심 용어를 제공하는 Context다.

Q. Domain Context는 왜 필요해?

A. 같은 작업이라도 Backend, Frontend, Prompt Engineering, DevOps마다 판단 기준이 다르기 때문이다.

Q. Domain Context와 Domain Rules는 관련 있어?

A. 관련 있다. Domain Rules는 해당 도메인 문서와 Prompt가 따라야 할 세부 기준을 제공한다.

---

## 2.3 Code Context

### [개념]

Code Context는 LLM이 코드 생성, 코드 리뷰, 리팩토링, 디버깅을 수행할 때 필요한 코드 정보다.

Code Context에는 관련 파일, 클래스, 메서드, DTO, Entity, Repository, 에러 로그가 포함될 수 있다.

---

### [핵심]

- Code Context는 코드 작업의 핵심 입력이다.
- 관련 계층 정보를 함께 제공하면 품질이 높아진다.
- Service 리뷰에는 Entity, DTO, Repository 정보가 유용하다.
- Controller 리뷰에는 Request DTO, Response 규칙, Service 시그니처가 유용하다.
- 디버깅에는 로그, 재현 절차, 최근 변경 사항이 필요하다.
- 보이지 않는 코드는 단정하지 않는다.

---

### [실무]

Code Context 예시:

```text
Code Context:
- AuthController.java
- AuthService.java
- LoginReqDto.java
- LoginResDto.java
- UserRepository.java
- Users Entity
- Error log
- Recent change
```

Code Review Prompt 예시:

```text
Task:
Review AuthService.java.

Code Context:
- AuthService code is provided.
- UserRepository method signatures are provided.
- LoginReqDto and LoginResDto are provided.

Failure Rule:
Do not make claims about unseen Controller or SecurityConfig.
If required code is missing, list it as Missing Information.
```

Code Context는 “보이는 코드 기준 리뷰”와 “전체 구조 추정”을 구분하게 만든다.

---

### [FAQ]

Q. Code Context는 뭐야?

A. 코드 생성, 리뷰, 리팩토링, 디버깅에 필요한 실제 코드와 관련 파일 정보다.

Q. 코드 리뷰에는 어떤 Code Context가 필요해?

A. 대상 코드, 관련 Entity, DTO, Repository, Service, Controller, 에러 로그, 프로젝트 규칙이 있으면 좋다.

Q. 보이지 않는 코드도 리뷰해도 돼?

A. 아니다. 제공되지 않은 코드는 단정하지 말고 Missing Information으로 표시해야 한다.

---

## 2.4 Business Rule Context

### [개념]

Business Rule Context는 프로젝트의 기능 요구사항과 업무 규칙을 설명하는 Context다.

Business Rule은 코드 구조보다 “왜 그렇게 동작해야 하는지”를 설명한다.

---

### [핵심]

- Business Rule은 기능 판단 기준이다.
- 사용자 권한, 상태 전이, 검증 조건을 포함한다.
- 도메인 정책은 코드 생성 전에 제공해야 한다.
- Business Rule이 없으면 모델이 임의 정책을 만들 수 있다.
- Business Rule은 Assumption으로 확정하면 안 된다.
- 부족하면 Missing Information으로 표시한다.

---

### [실무]

Business Rule Context 예시:

```text
Business Rule:
- Only authenticated users can create comments.
- Post owner can delete their post.
- Admin can hide reported posts.
- Deleted posts should not appear in public list.
- Like count cannot be negative.
```

나쁜 Prompt:

```text
댓글 기능 만들어줘.
```

좋은 Prompt:

```text
Comment feature Business Rule:
- Logged-in users can create comments.
- Comment owner can edit and delete comments.
- Admin can delete any comment.
- Deleted comments are soft-deleted.
```

Business Rule은 코드 생성 품질과 예외 처리 품질에 직접 영향을 준다.

---

### [FAQ]

Q. Business Rule Context는 뭐야?

A. 기능이 어떤 업무 규칙과 정책에 따라 동작해야 하는지 설명하는 Context다.

Q. Business Rule이 없으면 어떻게 돼?

A. 모델이 임의로 권한, 상태, 검증 조건을 만들어낼 수 있다.

Q. Business Rule을 Assumption으로 처리해도 돼?

A. 프로젝트 핵심 정책은 임의 가정하면 안 되며, 부족하면 Missing Information으로 표시해야 한다.

---

## 2.5 Environment Context

### [개념]

Environment Context는 실행 환경, 개발 환경, 배포 환경, 라이브러리 버전 정보를 제공하는 Context다.

Environment Context는 코드 호환성과 설정 판단에 중요하다.

---

### [핵심]

- 언어 버전을 명시한다.
- 프레임워크 버전을 명시한다.
- DB, OS, 런타임 환경을 명시한다.
- 빌드 도구와 패키지 매니저를 명시한다.
- 로컬 환경과 배포 환경을 구분한다.
- 최신 라이브러리는 버전 차이에 따라 답변이 달라질 수 있다.

---

### [실무]

Environment Context 예시:

```text
Environment:
- Java 21
- Spring Boot 3.x
- Gradle
- MySQL 8.x
- Ubuntu Server
- Docker
```

Frontend Environment Context 예시:

```text
Environment:
- React
- Vite or CRA
- JavaScript or TypeScript
- Axios
- React Router
```

Environment Context가 없으면 모델이 다른 버전 기준의 설정이나 코드를 제안할 수 있다.

---

### [FAQ]

Q. Environment Context는 뭐야?

A. 코드와 설정이 동작하는 언어, 프레임워크, DB, OS, 빌드 도구, 배포 환경 정보다.

Q. Environment Context는 왜 중요해?

A. 버전이나 실행 환경에 따라 코드와 설정 방식이 달라질 수 있기 때문이다.

Q. 버전을 꼭 적어야 해?

A. 코드 생성, 설정, 디버깅에서는 버전을 적는 것이 좋다.

---

# 3. Context Quality

## 3.1 Context Quality Criteria

### [개념]

Context Quality는 LLM에게 제공된 Context가 답변에 충분하고 정확하며 관련성이 높은지를 평가하는 기준이다.

Context Quality가 높을수록 답변 정확도와 프로젝트 적합도가 올라간다.

---

### [핵심]

좋은 Context 조건:

- 관련성이 높음
- 최신 정보임
- 프로젝트 규칙이 명확함
- 작업 대상과 직접 연결됨
- 중복이 적음
- 충돌이 없음
- 필요한 코드와 규칙이 포함됨
- Missing Information이 구분됨

나쁜 Context 조건:

- 관련 없는 정보가 많음
- 오래된 정보와 최신 정보가 섞임
- 프로젝트 규칙이 모호함
- Task와 직접 관련이 없음
- 핵심 파일이 빠짐
- 서로 충돌하는 규칙이 있음

---

### [실무]

Context Quality 점검 예시:

```md
### [Checklist]

- [ ] Task와 직접 관련 있는 Context인가?
- [ ] 프로젝트 기술 스택과 버전이 포함되었는가?
- [ ] 관련 코드 파일이 제공되었는가?
- [ ] Business Rule이 제공되었는가?
- [ ] 기존 결정사항이 포함되었는가?
- [ ] 오래된 정보와 충돌하지 않는가?
- [ ] 불필요한 배경 설명이 과도하지 않은가?
- [ ] Missing Information이 분리되었는가?
```

RAG 시스템에서는 검색된 Chunk의 품질이 Context Quality를 결정한다.

Chunk가 독립적이고 제목이 명확할수록 Context Quality가 좋아진다.

---

### [FAQ]

Q. Context Quality가 뭐야?

A. LLM에게 제공된 Context가 정확하고 관련성이 높으며 작업 수행에 충분한지를 의미한다.

Q. Context Quality가 낮으면 어떻게 돼?

A. 모델이 일반론으로 답하거나 프로젝트와 맞지 않는 결과를 만들 수 있다.

Q. RAG에서 Context Quality는 무엇에 달려 있어?

A. 검색된 Chunk의 정확도, 관련성, 독립성, 최신성, 용어 일관성에 달려 있다.

---

## 3.2 Context Overload

### [개념]

Context Overload는 너무 많은 정보가 Prompt에 포함되어 핵심 작업이 흐려지는 문제다.

Context는 많을수록 좋은 것이 아니라 작업에 필요한 정보만 있어야 한다.

---

### [핵심]

- 관련 없는 Context는 제거한다.
- 오래된 결정사항과 최신 결정사항을 구분한다.
- 중복 설명을 줄인다.
- 핵심 제약은 Constraint로 분리한다.
- 긴 문서 전체보다 필요한 Chunk가 좋다.
- Context가 많으면 모델이 중요한 조건을 놓칠 수 있다.

---

### [실무]

나쁜 Context:

```text
프로젝트 전체 회의 내용, 모든 기능 설명, 관련 없는 배포 이슈, 오래된 결정사항을 한 번에 제공
```

좋은 Context:

```text
Task:
Review login service.

Relevant Context:
- AuthService.java
- LoginReqDto.java
- UserRepository.java
- JWT authentication rule
- Error handling rule

Excluded:
- Frontend UI
- Deployment pipeline
- Payment module
```

Context가 길어질수록 관련성 기준으로 정리해야 한다.

Agent Workflow에서는 PM Agent가 User Request를 정리해 Domain Agent에게 필요한 Context만 전달하는 것이 좋다.

---

### [FAQ]

Q. Context Overload가 뭐야?

A. 너무 많은 정보가 Prompt에 포함되어 모델이 핵심 작업과 중요한 조건을 놓치는 문제다.

Q. Context는 많을수록 좋아?

A. 아니다. 작업과 직접 관련 있는 정확한 Context가 중요하다.

Q. Context가 너무 길면 어떻게 해?

A. 관련 정보만 선별하고, 핵심 제약은 Constraints로 분리하며, 오래된 정보는 제거해야 한다.

---

# 4. RAG Prompt

## 4.1 RAG Prompt Definition

### [개념]

RAG Prompt는 검색된 문서인 Retrieved Context를 기반으로 답변하도록 설계한 Prompt다.

RAG Prompt의 핵심은 Grounded Answer다.

Grounded Answer는 검색 문서에 근거한 답변이다.

문서에 없는 내용은 지어내지 않고 Missing Information으로 표시한다.

---

### [핵심]

- RAG Prompt는 검색 문서를 우선 사용한다.
- 검색 문서에 없는 내용은 지어내지 않는다.
- Retrieved Context와 일반 지식을 구분한다.
- 검색 실패와 지식 부재를 구분한다.
- 추정은 Assumption으로 표시한다.
- 문서 간 충돌 시 우선순위를 따른다.
- 출력 형식을 명확히 지정한다.
- Hallucination Prevention Rule을 포함한다.

---

### [실무]

RAG Prompt 기본 구조:

```text
You are a RAG Answer Agent.

Task:
Answer the user question using retrieved documents.

Rules:
- Use retrieved context first.
- Do not invent project-specific facts.
- If retrieved context is insufficient, state what is missing.
- Separate confirmed facts, assumptions, and missing information.
- Return the answer in the requested format.

Output Format:
## Answer
## Confirmed by Retrieved Context
## Assumptions
## Missing Information
```

RAG 문서 제작용 Prompt에서는 아래 규칙을 추가한다.

```text
Document Generation Rules:
- Apply MASTER_RAG_RULES.
- Apply DOMAIN_RULES.
- Optimize for retrieval.
- Include [개념], [핵심], [실무], [FAQ].
- Include Retrieval Queries.
```

---

### [FAQ]

Q. RAG Prompt가 뭐야?

A. 검색된 문서를 근거로 답변하도록 설계한 Prompt다.

Q. RAG Prompt의 핵심은 뭐야?

A. Retrieved Context를 우선 사용하고 문서에 없는 내용은 지어내지 않는 것이다.

Q. Grounded Answer는 뭐야?

A. 검색 문서나 제공된 Context에 근거해 작성한 답변이다.

Q. RAG Prompt가 없으면 어떻게 돼?

A. 모델이 검색 문서보다 일반 지식이나 추정을 우선해 답할 수 있다.

---

# 5. RAG Prompt Components

## 5.1 Retrieved Context

### [개념]

Retrieved Context는 RAG 시스템이 검색하여 Prompt에 주입한 문서 Chunk다.

Retrieved Context는 답변의 근거가 되는 핵심 자료다.

---

### [핵심]

- Retrieved Context는 RAG 답변의 근거다.
- Retrieved Context는 일반 지식보다 우선한다.
- 검색된 Chunk가 충분하지 않을 수 있다.
- 검색 결과가 부정확하면 답변 품질이 낮아진다.
- Retrieved Context와 User Task를 연결해야 한다.
- Retrieved Context에 없는 정보는 Missing Information으로 표시한다.

---

### [실무]

Retrieved Context 사용 Instruction:

```text
Use the retrieved context as the primary source.
Do not override retrieved context with general knowledge.
If retrieved context is incomplete, state what is missing.
```

Retrieved Context 기반 출력 구조:

```md
## Answer

## Evidence from Retrieved Context

## Missing Information

## Assumptions
```

RAG Agent는 Retrieved Context를 그대로 복사하는 것이 아니라, User Task에 맞춰 근거 기반으로 재구성해야 한다.

---

### [FAQ]

Q. Retrieved Context가 뭐야?

A. RAG 시스템이 검색해서 LLM Prompt에 주입한 문서 Chunk다.

Q. Retrieved Context는 왜 중요해?

A. RAG 답변의 근거가 되는 자료이기 때문이다.

Q. Retrieved Context에 답이 없으면 어떻게 해?

A. 정보가 부족하다고 표시하고 필요한 추가 정보를 Missing Information으로 작성해야 한다.

---

## 5.2 Source Priority

### [개념]

Source Priority는 여러 근거가 있을 때 어떤 정보를 우선할지 정하는 규칙이다.

RAG 환경에서는 검색 문서, Domain Rules, Project Context, 일반 지식이 충돌할 수 있다.

---

### [핵심]

- Source Priority는 근거 우선순위다.
- 프로젝트 문서는 일반 지식보다 우선한다.
- Domain Rules는 해당 도메인 문서 작성 기준에 우선 적용한다.
- Master Rules는 전체 RAG 문서의 최상위 기준이다.
- 최신 Project Progress는 과거 계획보다 우선한다.
- 충돌이 있으면 충돌 내용을 표시한다.

---

### [실무]

RAG 문서 제작 Source Priority 예시:

```text
Source Priority:
1. MASTER_RAG_RULES
2. DOMAIN_RULES
3. PROJECT_PROGRESS
4. User Request
5. General Prompt Engineering Knowledge
```

RAG Answer Source Priority 예시:

```text
Source Priority:
1. Retrieved project documents
2. Uploaded code/context
3. User-provided requirements
4. General technical knowledge
```

Source Priority가 없으면 모델이 일반 지식을 우선하거나 오래된 정보를 기준으로 답할 수 있다.

---

### [FAQ]

Q. Source Priority가 뭐야?

A. 여러 근거가 있을 때 어떤 정보를 먼저 따를지 정하는 우선순위 규칙이다.

Q. RAG 문서 제작에서는 무엇이 우선이야?

A. MASTER_RAG_RULES, DOMAIN_RULES, PROJECT_PROGRESS, User Request 순서로 우선 적용하는 것이 안정적이다.

Q. 검색 문서와 일반 지식이 다르면 뭘 따라야 해?

A. 프로젝트 RAG 작업에서는 검색 문서와 프로젝트 규칙을 우선해야 한다.

---

## 5.3 Missing Information Rule

### [개념]

Missing Information Rule은 Retrieved Context에 필요한 정보가 없을 때 LLM이 지어내지 않고 부족한 정보를 표시하도록 하는 규칙이다.

RAG Prompt에서 가장 중요한 Hallucination 방지 규칙이다.

---

### [핵심]

- 문서에 없는 내용은 확정하지 않는다.
- 프로젝트 고유 정보를 임의 생성하지 않는다.
- 부족한 정보는 Missing Information으로 표시한다.
- 추정은 Assumption으로 분리한다.
- 검색 실패와 정보 부재를 구분한다.
- Missing Information이 많으면 추가 문서나 코드가 필요하다.

---

### [실무]

Missing Information Rule 예시:

```text
If the retrieved context does not contain the answer:
- State that the context is insufficient.
- List missing information.
- Do not invent unsupported facts.
- Provide a partial answer only if it is safe.
```

RAG Answer 출력 예시:

```md
## Missing Information

- Repository method signatures are not provided.
- Entity field list is not provided.
- SecurityConfig is not provided.
```

Missing Information Rule은 RAG 기반 Code Generation과 Code Review에서 필수다.

---

### [FAQ]

Q. Missing Information Rule이 뭐야?

A. 필요한 정보가 없을 때 지어내지 않고 부족한 정보를 명확히 표시하도록 하는 규칙이다.

Q. RAG에서 Missing Information Rule은 왜 중요해?

A. 검색 문서에 없는 내용을 모델이 만들어내는 Hallucination을 줄이기 위해 중요하다.

Q. 검색 결과가 부족하면 답변을 멈춰야 해?

A. 안전한 범위에서 부분 답변을 제공하고 한계를 명확히 표시할 수 있다.

---

## 5.4 Citation / Reference Rule

### [개념]

Citation / Reference Rule은 RAG 답변에서 어떤 문서나 Context를 근거로 삼았는지 표시하는 규칙이다.

내부 Agent Workflow에서는 Evidence, Source, Reference 섹션으로 근거를 표현할 수 있다.

---

### [핵심]

- 근거 출처를 표시하면 답변 신뢰도가 높아진다.
- RAG Agent는 근거와 추정을 분리해야 한다.
- 문서 ID, 파일명, 섹션명, Chunk 제목을 사용할 수 있다.
- Citation이 불가능하면 근거 기준을 설명한다.
- 근거 없는 확정 표현을 피한다.
- Retrieval 결과가 불충분하면 부족한 근거를 표시한다.

---

### [실무]

Reference Output 예시:

```md
## Evidence

- Source: Prompt_Engineering_Domain_Rules.md
- Section: RAG Prompt Rules
- Key Rule: Use retrieved context first and mark missing information.
```

Agent 내부 Handoff 예시:

```md
## Confirmed by Context

- MASTER_RAG_RULES requires [개념], [핵심], [실무], [FAQ].
- Prompt Engineering Domain Rules require RAG Prompt and Hallucination Prevention sections.

## Assumptions

- Part04 focuses on Context Prompt, RAG Prompt, and Few-Shot Prompt.
```

Reference Rule은 검수 Agent가 결과를 확인할 수 있도록 도와준다.

---

### [FAQ]

Q. Citation / Reference Rule이 뭐야?

A. RAG 답변에서 어떤 문서나 Context를 근거로 삼았는지 표시하는 규칙이다.

Q. 모든 답변에 Citation이 필요해?

A. 시스템 요구사항에 따라 다르지만, RAG Agent 내부에서는 근거와 추정을 구분하는 것이 중요하다.

Q. 근거를 표시하면 뭐가 좋아?

A. 답변 검증이 쉬워지고 Hallucination을 줄일 수 있다.

---

# 6. RAG Prompt Patterns

## 6.1 Grounded Answer Pattern

### [개념]

Grounded Answer Pattern은 검색된 문서에 근거해 답변하고, 문서에 없는 내용은 분리하는 RAG Prompt 패턴이다.

---

### [핵심]

- Retrieved Context 기반으로 답한다.
- Confirmed, Assumption, Missing Information을 분리한다.
- 근거 없는 확정 표현을 피한다.
- 문서 내용과 일반 추론을 구분한다.
- 답변은 요청한 Output Format을 따른다.

---

### [실무]

Grounded Answer Prompt:

```text
Use the retrieved context to answer.
Separate the answer into:
- Confirmed by Context
- Assumptions
- Missing Information
- Final Answer

Do not invent unsupported facts.
```

Grounded Answer Output:

```md
## Confirmed by Context

## Assumptions

## Missing Information

## Final Answer
```

Grounded Answer Pattern은 RAG 기반 QA, 코드 리뷰, 문서 검수에 공통 적용 가능하다.

---

### [FAQ]

Q. Grounded Answer Pattern이 뭐야?

A. 검색 문서에 근거한 내용, 추정, 부족한 정보를 분리해 답변하는 RAG Prompt 패턴이다.

Q. 왜 Confirmed와 Assumption을 분리해야 해?

A. 확정 정보와 추정을 섞으면 사용자가 잘못된 내용을 사실로 이해할 수 있기 때문이다.

Q. Grounded Answer Pattern은 어디에 사용해?

A. RAG QA, 코드 리뷰, 문서 검수, Agent Handoff 검증에 사용할 수 있다.

---

## 6.2 RAG Code Generation Pattern

### [개념]

RAG Code Generation Pattern은 검색된 프로젝트 문서와 코드 Context를 기반으로 코드를 생성하는 Prompt 패턴이다.

핵심은 기존 프로젝트 구조를 우선하고 없는 정보를 만들지 않는 것이다.

---

### [핵심]

- 프로젝트 문서를 우선한다.
- 기존 코드 구조를 따른다.
- 없는 클래스, 필드, API 경로를 임의 생성하지 않는다.
- 필요한 경우 Assumption으로 분리한다.
- 코드 예시는 짧고 직접적으로 작성한다.
- 예외 처리, 트랜잭션, 응답 규칙을 포함한다.
- 테스트 또는 검증 Checklist를 포함한다.

---

### [실무]

RAG Code Generation Prompt:

```text
Generate code based on retrieved project documents and provided code context.

Rules:
- Follow existing project architecture.
- Do not invent missing classes, fields, or API paths.
- Use Java 21 and Spring Boot 3.x if confirmed by context.
- Keep snippets short.
- If required information is missing, list it before code.

Output:
## Missing Information
## Assumptions
## Implementation Plan
## Code Snippet
## Validation Checklist
```

이 패턴은 Backend Agent가 RAG 문서와 업로드 코드를 함께 사용할 때 적합하다.

---

### [FAQ]

Q. RAG Code Generation Pattern이 뭐야?

A. 검색 문서와 제공된 코드 Context를 근거로 기존 프로젝트 구조에 맞는 코드를 생성하는 Prompt 패턴이다.

Q. 코드 생성에서 가장 조심할 점은 뭐야?

A. 없는 클래스명, 필드명, API 경로, 비즈니스 규칙을 임의로 만들지 않는 것이다.

Q. 코드 예시는 길게 작성해도 돼?

A. RAG 문서와 Agent 출력에서는 핵심 로직 중심의 짧은 snippet이 좋다.

---

## 6.3 RAG Code Review Pattern

### [개념]

RAG Code Review Pattern은 검색된 프로젝트 규칙과 제공된 코드를 기준으로 리뷰하는 Prompt 패턴이다.

핵심은 보이는 코드만 검토하고, 보이지 않는 영역은 단정하지 않는 것이다.

---

### [핵심]

- 제공된 코드를 기준으로 검토한다.
- 검색 문서의 프로젝트 규칙을 적용한다.
- 보이지 않는 파일은 단정하지 않는다.
- 문제, 원인, 위험, 수정 방향을 분리한다.
- Severity를 포함한다.
- Missing Information을 표시한다.
- 취향과 결함을 구분한다.

---

### [실무]

RAG Code Review Prompt:

```text
Review the provided code using retrieved project rules.

Review Criteria:
- Architecture consistency
- Transaction boundary
- Exception handling
- DTO responsibility
- N+1 query risk
- API response consistency

Rules:
- Review only visible code.
- Do not claim unseen files are correct or incorrect.
- Mark missing files as Missing Information.

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

이 패턴은 Review Agent의 기본 Code Review Prompt로 사용할 수 있다.

---

### [FAQ]

Q. RAG Code Review Pattern이 뭐야?

A. 검색된 프로젝트 규칙과 제공된 코드를 근거로 코드 품질과 위험을 검토하는 Prompt 패턴이다.

Q. 보이지 않는 파일까지 리뷰해도 돼?

A. 아니다. 보이는 코드만 리뷰하고 필요한 추가 파일은 Missing Information으로 표시해야 한다.

Q. Code Review 출력에는 뭐가 필요해?

A. 문제, 원인, 위험, 수정 방향, Severity, Missing Information, Checklist가 필요하다.

---

## 6.4 RAG Document Generation Pattern

### [개념]

RAG Document Generation Pattern은 Master Rules, Domain Rules, Project Progress를 기반으로 RAG 최적화 문서를 생성하는 Prompt 패턴이다.

이 패턴은 사람용 학습 문서보다 Retrieval 최적화를 우선한다.

---

### [핵심]

- MASTER_RAG_RULES를 적용한다.
- DOMAIN_RULES를 적용한다.
- PROJECT_PROGRESS를 참고한다.
- 문서는 Markdown 기준으로 작성한다.
- `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`를 포함한다.
- Retrieval Queries를 포함한다.
- FAQ를 강화한다.
- Chunk는 독립 검색 가능해야 한다.
- 장문 에세이형 설명을 피한다.
- 용어를 통일한다.

---

### [실무]

RAG Document Generation Prompt:

```text
Create a RAG-optimized Markdown document.

Apply:
- MASTER_RAG_RULES
- DOMAIN_RULES
- PROJECT_PROGRESS

Rules:
- Optimize for retrieval.
- Do not write essay-style content.
- Use [개념], [핵심], [실무], [FAQ].
- Include Retrieval Queries.
- Keep chunks independently searchable.
- Use consistent terminology.
```

RAG 문서 출력은 사람이 처음부터 끝까지 읽는 문서가 아니라 Agent Retrieval, Code Generation, Review, Decision Support를 위한 문서다.

---

### [FAQ]

Q. RAG Document Generation Pattern이 뭐야?

A. Master Rules, Domain Rules, Project Progress를 기반으로 검색 최적화 문서를 만드는 Prompt 패턴이다.

Q. RAG 문서는 사람용 학습 문서야?

A. 아니다. RAG 문서는 AI Agent Retrieval과 Code Generation, Review, Decision Support를 위한 문서다.

Q. RAG 문서에서 FAQ가 중요한 이유는 뭐야?

A. 사용자의 실제 질문 패턴과 문서 Chunk를 연결해 Retrieval Hit를 높이기 위해 중요하다.

---

# 7. Few-Shot Prompt

## 7.1 Few-Shot Prompt Definition

### [개념]

Few-Shot Prompt는 예시 입력과 예시 출력을 제공해 LLM의 출력 패턴과 판단 기준을 안정화하는 Prompt다.

Few-Shot은 모델에게 “이런 입력에는 이런 형식으로 답하라”는 패턴을 보여준다.

---

### [핵심]

- Few-Shot Prompt는 출력 형식을 안정화한다.
- 예시는 짧고 대표적이어야 한다.
- Example Input과 Example Output을 함께 제공한다.
- 실제 Task와 예시 패턴이 일치해야 한다.
- 예시가 너무 많으면 Prompt가 길어진다.
- 잘못된 예시와 올바른 예시를 비교할 수 있다.
- Structured Output 안정화에 유용하다.

---

### [실무]

Few-Shot Prompt 기본 구조:

```text
Pattern:
For each issue, return Problem, Cause, Risk, Fix Direction.

Example Input:
Controller contains business logic.

Example Output:
Problem:
Business logic is inside Controller.

Cause:
Controller handles business decision instead of delegating to Service.

Risk:
Controller becomes hard to test and maintain.

Fix Direction:
Move business logic to Service.
```

Few-Shot은 Code Review, JSON Output, RAG Document Format, Agent Handoff 형식 안정화에 효과적이다.

---

### [FAQ]

Q. Few-Shot Prompt가 뭐야?

A. 예시 입력과 예시 출력을 제공해 LLM의 출력 형식과 판단 기준을 안정화하는 Prompt다.

Q. Few-Shot Prompt는 언제 써?

A. 출력 형식이나 판단 기준을 안정화해야 할 때 사용한다.

Q. Few-Shot 예시는 많을수록 좋아?

A. 아니다. 너무 많으면 Prompt가 길어지고 핵심 Task가 흐려질 수 있다.

---

# 8. Few-Shot Components

## 8.1 Example Input

### [개념]

Example Input은 Few-Shot Prompt에서 모델에게 보여주는 예시 입력이다.

Example Input은 실제 요청과 유사해야 한다.

---

### [핵심]

- Example Input은 짧고 명확해야 한다.
- 실제 Task와 유사해야 한다.
- 하나의 판단 기준을 보여주는 것이 좋다.
- 너무 복잡한 예시는 피한다.
- 예시와 실제 작업이 다르면 품질이 낮아질 수 있다.

---

### [실무]

Code Review Example Input:

```text
Example Input:
Controller directly calls Repository and handles business logic.
```

RAG Answer Example Input:

```text
Example Input:
Retrieved context does not include Repository method signatures.
```

Prompt Review Example Input:

```text
Example Input:
Prompt says "make it good" but does not specify output format.
```

Example Input은 모델이 어떤 상황을 어떤 기준으로 판단해야 하는지 학습시키는 역할을 한다.

---

### [FAQ]

Q. Example Input은 뭐야?

A. Few-Shot Prompt에서 모델에게 보여주는 예시 입력이다.

Q. Example Input은 실제 작업과 비슷해야 해?

A. 그렇다. 실제 Task와 유사해야 출력 패턴이 잘 전이된다.

Q. Example Input이 너무 복잡하면 어떻게 돼?

A. 모델이 핵심 패턴보다 예시 세부사항에 끌려갈 수 있다.

---

## 8.2 Example Output

### [개념]

Example Output은 Example Input에 대해 기대하는 답변 형식과 판단 기준을 보여주는 예시 출력이다.

Example Output은 실제 최종 출력 형식과 일치해야 한다.

---

### [핵심]

- Example Output은 원하는 출력 형식을 보여준다.
- 실제 Output Format과 일치해야 한다.
- 필드명과 섹션명을 고정한다.
- 간결하고 대표적으로 작성한다.
- 잘못된 예시는 피하거나 Anti-Example로 분리한다.
- 후속 Agent가 사용할 구조로 작성한다.

---

### [실무]

Code Review Example Output:

```md
Problem:
Controller contains business logic.

Cause:
Controller is responsible for request handling but also performs business decisions.

Risk:
Low testability and poor separation of concerns.

Fix Direction:
Move business logic to Service layer.

Severity:
Medium
```

JSON Example Output:

```json
{
  "status": "completed",
  "severity": "medium",
  "message": "Controller contains business logic",
  "requiresFollowUp": false
}
```

Example Output은 LLM에게 “내용”보다 “형식과 판단 방식”을 학습시키는 데 중요하다.

---

### [FAQ]

Q. Example Output은 뭐야?

A. Example Input에 대해 원하는 답변 형식과 판단 기준을 보여주는 예시 출력이다.

Q. Example Output은 최종 출력과 같아야 해?

A. 가능하면 최종 Output Format과 동일해야 출력 안정성이 높아진다.

Q. JSON 출력에도 Few-Shot을 쓸 수 있어?

A. 가능하다. JSON Schema와 Example Output을 함께 제공하면 출력 안정성이 좋아진다.

---

## 8.3 Anti-Example

### [개념]

Anti-Example은 잘못된 예시를 보여주고 왜 잘못되었는지 설명하는 Few-Shot 구성 요소다.

Anti-Example은 모델이 피해야 할 출력 패턴을 명확히 이해하도록 돕는다.

---

### [핵심]

- Anti-Example은 피해야 할 패턴을 보여준다.
- 잘못된 이유를 짧게 설명한다.
- 올바른 예시와 함께 사용하면 효과적이다.
- 너무 많은 Anti-Example은 Prompt를 길게 만든다.
- 금지사항이 중요한 작업에 유용하다.

---

### [실무]

Anti-Example:

```text
Bad Output:
Looks fine. You can improve it later.

Why Bad:
- No problem identified.
- No cause.
- No risk.
- No fix direction.
- No severity.
```

Correct Example:

```md
Problem:
Exception handling is inconsistent.

Cause:
Service catches generic Exception and returns null.

Risk:
Error cause is hidden and API behavior becomes unpredictable.

Fix Direction:
Throw a domain exception and handle it in GlobalExceptionHandler.

Severity:
High
```

Anti-Example은 Code Review Prompt, JSON Output Prompt, RAG Answer Prompt에서 형식 실패를 줄이는 데 유용하다.

---

### [FAQ]

Q. Anti-Example이 뭐야?

A. 모델이 피해야 할 잘못된 입력이나 출력 예시를 보여주는 Few-Shot 구성 요소다.

Q. Anti-Example은 언제 유용해?

A. 반복적으로 잘못된 형식이나 일반적인 답변이 나올 때 유용하다.

Q. Anti-Example만 제공하면 돼?

A. 아니다. 올바른 Example Output과 함께 제공해야 효과적이다.

---

# 9. Few-Shot Patterns

## 9.1 Code Review Few-Shot Pattern

### [개념]

Code Review Few-Shot Pattern은 코드 리뷰 결과의 판단 기준과 출력 형식을 안정화하는 예시 패턴이다.

---

### [핵심]

- 문제, 원인, 위험, 수정 방향을 고정한다.
- Severity를 포함한다.
- 취향과 결함을 구분한다.
- 보이는 코드 기준으로 판단한다.
- Missing Information을 표시한다.

---

### [실무]

Code Review Few-Shot:

```text
Example Input:
Service method has no @Transactional while modifying multiple entities.

Example Output:
Problem:
Transaction boundary is unclear.

Cause:
The method modifies multiple entities but does not define a transaction boundary.

Risk:
Partial update can occur if an exception happens during the operation.

Fix Direction:
Add @Transactional at the Service method level and keep database write logic inside the transaction.

Severity:
High
```

이 패턴은 Backend Review Agent가 일관된 리뷰 결과를 생성하는 데 유용하다.

---

### [FAQ]

Q. Code Review Few-Shot Pattern은 뭐야?

A. 코드 리뷰 결과를 문제, 원인, 위험, 수정 방향, Severity 형식으로 안정화하는 예시 패턴이다.

Q. Code Review Few-Shot은 왜 필요해?

A. 리뷰가 단순 감상으로 흐르지 않고 구조화된 검토 결과가 나오도록 하기 위해 필요하다.

Q. Severity는 왜 포함해?

A. 문제의 우선순위를 판단하고 수정 순서를 정하기 위해 필요하다.

---

## 9.2 RAG Answer Few-Shot Pattern

### [개념]

RAG Answer Few-Shot Pattern은 문서 근거, 추정, 부족한 정보를 분리하는 답변 형식을 안정화하는 예시 패턴이다.

---

### [핵심]

- Confirmed by Context를 분리한다.
- Assumptions를 분리한다.
- Missing Information을 표시한다.
- 근거 없는 내용을 확정하지 않는다.
- 문서 기반 답변을 우선한다.

---

### [실무]

RAG Answer Few-Shot:

```text
Example Input:
Question: What Repository methods are required?
Retrieved Context: Service rule exists, but Repository method signatures are not provided.

Example Output:
Confirmed by Context:
- Service should use Repository for persistence operations.

Missing Information:
- Repository method signatures are not provided.
- Entity field names are not provided.

Assumptions:
- Method names can be proposed only as examples.

Final Answer:
Repository methods cannot be confirmed from the current context. Additional Repository and Entity code is required.
```

이 패턴은 RAG Agent가 없는 정보를 지어내지 않도록 돕는다.

---

### [FAQ]

Q. RAG Answer Few-Shot Pattern은 뭐야?

A. 문서 근거, 추정, 부족한 정보를 분리하는 RAG 답변 형식을 예시로 안정화하는 패턴이다.

Q. RAG Answer Few-Shot은 왜 필요해?

A. 모델이 검색 문서에 없는 내용을 확정적으로 말하는 문제를 줄이기 위해 필요하다.

Q. Missing Information을 예시에 넣어야 해?

A. 그렇다. RAG 답변에서는 부족한 정보를 표시하는 패턴이 중요하다.

---

## 9.3 Structured Output Few-Shot Pattern

### [개념]

Structured Output Few-Shot Pattern은 Markdown, JSON, Table, Checklist 같은 고정 출력 형식을 안정화하는 예시 패턴이다.

---

### [핵심]

- 최종 출력 형식과 예시 형식을 일치시킨다.
- 필드명과 섹션명을 고정한다.
- JSON은 유효한 JSON 예시를 제공한다.
- Markdown은 Header 계층을 명확히 한다.
- Checklist는 항목 기준을 명확히 한다.

---

### [실무]

Markdown Few-Shot:

```md
## Summary

## Findings

### 1. Problem

- Cause:
- Risk:
- Fix Direction:
- Severity:

## Checklist
```

JSON Few-Shot:

```json
{
  "status": "completed",
  "summary": "Review completed",
  "findings": [
    {
      "type": "transaction",
      "severity": "high",
      "message": "Transaction boundary is unclear"
    }
  ],
  "requiresFollowUp": false
}
```

Structured Output Few-Shot은 Agent 간 Handoff와 자동 처리에서 중요하다.

---

### [FAQ]

Q. Structured Output Few-Shot Pattern은 뭐야?

A. Markdown, JSON, Checklist 같은 고정 출력 형식을 예시로 보여줘 출력 안정성을 높이는 패턴이다.

Q. JSON Few-Shot에서 중요한 점은 뭐야?

A. 유효한 JSON 예시를 제공하고 부가 설명을 금지하는 제약을 함께 넣는 것이다.

Q. Markdown Few-Shot은 언제 좋아?

A. 코드 리뷰, RAG 문서, 작업 계획, 체크리스트처럼 사람이 읽는 구조화 결과에 좋다.

---

# 10. Context, RAG, Few-Shot Comparison

## 10.1 Context Prompt vs RAG Prompt

### [개념]

Context Prompt와 RAG Prompt는 모두 LLM에게 근거 정보를 제공하지만 역할이 다르다.

Context Prompt는 일반적인 배경 정보 제공 방식이다.

RAG Prompt는 검색된 문서를 우선 근거로 사용하도록 제어하는 Prompt다.

---

### [핵심]

| 비교      | Context Prompt      | RAG Prompt                |
| --------- | ------------------- | ------------------------- |
| 목적      | 배경 정보 제공      | 검색 문서 기반 답변       |
| 근거      | 사용자 제공 Context | Retrieved Context         |
| 핵심 규칙 | 관련 Context 제공   | 문서 근거 우선            |
| 위험      | Context 부족 / 과다 | 검색 실패 / Hallucination |
| 필수 규칙 | Task와 Context 분리 | Missing Information Rule  |
| 사용 예   | 코드 리뷰 배경 제공 | RAG QA, 문서 기반 답변    |

---

### [실무]

Context Prompt는 사용자가 제공한 프로젝트 정보, 코드, 환경을 정리할 때 사용한다.

RAG Prompt는 검색된 문서 Chunk를 근거로 답변해야 할 때 사용한다.

RAG Prompt에는 반드시 아래 규칙이 필요하다.

```text
Use retrieved context first.
Do not invent unsupported facts.
State missing information when context is insufficient.
```

---

### [FAQ]

Q. Context Prompt와 RAG Prompt 차이는 뭐야?

A. Context Prompt는 배경 정보를 제공하고, RAG Prompt는 검색된 문서를 우선 근거로 답변하도록 제어한다.

Q. RAG Prompt에도 Context가 있어?

A. 있다. RAG에서 검색된 문서가 Retrieved Context로 사용된다.

Q. RAG Prompt에서 가장 중요한 규칙은 뭐야?

A. 검색 문서를 우선 사용하고 문서에 없는 내용은 지어내지 않는 것이다.

---

## 10.2 Zero-Shot vs Few-Shot

### [개념]

Zero-Shot은 예시 없이 지시만 제공하는 Prompt 방식이다.

Few-Shot은 예시 입력과 예시 출력을 함께 제공하는 Prompt 방식이다.

---

### [핵심]

| 비교 | Zero-Shot        | Few-Shot                       |
| ---- | ---------------- | ------------------------------ |
| 방식 | 예시 없이 지시   | 예시와 함께 지시               |
| 장점 | 짧고 단순        | 출력 패턴 안정                 |
| 단점 | 형식 흔들림 가능 | Prompt 길어짐                  |
| 적합 | 단순 작업        | 형식과 판단 기준이 중요한 작업 |
| 예시 | “리뷰해줘”       | 문제/원인/수정 예시 제공       |

---

### [실무]

Zero-Shot이 적합한 경우:

- 단순 설명
- 간단한 분류
- 짧은 변환 작업
- 기준이 명확한 단일 질문

Few-Shot이 적합한 경우:

- Code Review
- JSON Output
- Agent Handoff
- RAG Answer
- 문서 형식 고정
- 반복 작업 자동화

Few-Shot은 출력 안정성이 필요할 때 사용한다.

---

### [FAQ]

Q. Zero-Shot과 Few-Shot 차이는 뭐야?

A. Zero-Shot은 예시 없이 지시만 제공하고, Few-Shot은 예시 입력과 예시 출력을 함께 제공한다.

Q. Few-Shot은 언제 써야 해?

A. 출력 형식이나 판단 기준을 안정화해야 할 때 사용한다.

Q. Zero-Shot은 나쁜 방식이야?

A. 아니다. 단순 작업에는 Zero-Shot이 더 짧고 효율적일 수 있다.

---

# 11. Common Mistakes

## 11.1 Context Prompt Mistakes

### [개념]

Context Prompt Mistake는 필요한 Context가 부족하거나 관련 없는 Context가 많거나, Context와 Task가 섞이는 문제다.

---

### [핵심]

자주 발생하는 실수:

- Context 없이 코드 생성 요청
- 기술 스택과 버전 누락
- 관련 코드 파일 누락
- Business Rule 누락
- 오래된 정보와 최신 정보 혼합
- Context와 Task를 한 문단에 섞음
- 관련 없는 전체 프로젝트 설명 과다 제공
- 중요한 제약을 Context에만 넣고 Constraint로 고정하지 않음

---

### [실무]

나쁜 예:

```text
이 프로젝트 로그인 만들어줘.
```

개선 예:

```text
Task:
Create login Service implementation plan.

Project Context:
- Java 21
- Spring Boot 3.x
- JWT authentication
- ApiResponse<T> response rule
- GlobalExceptionHandler exception rule

Input:
- AuthController
- LoginReqDto
- UserRepository

Constraints:
- Do not invent missing classes.
- Mark missing information.
```

Context는 작업에 필요한 정확한 정보만 제공한다.

---

### [FAQ]

Q. Context Prompt에서 가장 흔한 실수는 뭐야?

A. 필요한 프로젝트 정보와 코드 없이 작업을 요청하거나, 관련 없는 정보를 과도하게 넣는 것이다.

Q. Context와 Constraint를 구분해야 해?

A. 그렇다. 참고 정보는 Context이고 반드시 지켜야 하는 조건은 Constraint로 분리하는 것이 좋다.

---

## 11.2 RAG Prompt Mistakes

### [개념]

RAG Prompt Mistake는 검색 문서 우선 규칙이 없거나, 문서에 없는 내용을 지어내도록 방치하는 문제다.

---

### [핵심]

자주 발생하는 실수:

- Retrieved Context 우선 규칙 없음
- Missing Information Rule 없음
- Assumption 표시 없음
- 일반 지식으로 검색 문서 덮어쓰기
- 문서 간 충돌 처리 기준 없음
- 검색 실패와 지식 부재를 구분하지 않음
- 근거 없는 프로젝트 고유 정보 확정
- 출력 형식 없음

---

### [실무]

나쁜 RAG Prompt:

```text
문서 보고 답해줘.
```

개선 RAG Prompt:

```text
Use retrieved documents first.
If the document does not contain the answer, state what is missing.
Do not invent project-specific facts.
Separate confirmed facts, assumptions, and missing information.
Return the answer in Markdown.
```

RAG Prompt는 반드시 Grounded Answer와 Missing Information Rule을 포함해야 한다.

---

### [FAQ]

Q. RAG Prompt에서 가장 흔한 실수는 뭐야?

A. 검색 문서 우선 규칙과 Missing Information Rule을 넣지 않는 것이다.

Q. 검색 문서에 없는 내용을 답하면 안 돼?

A. 프로젝트 고유 정보는 답하면 안 된다. 필요한 경우 Assumption이나 Missing Information으로 분리해야 한다.

---

## 11.3 Few-Shot Prompt Mistakes

### [개념]

Few-Shot Prompt Mistake는 예시가 실제 작업과 맞지 않거나, 예시가 너무 많거나, 최종 출력 형식과 다른 문제다.

---

### [핵심]

자주 발생하는 실수:

- 예시와 실제 Task가 다름
- Example Output과 최종 Output Format이 다름
- 예시가 너무 길고 복잡함
- 예시가 너무 많음
- 잘못된 예시를 Anti-Example 없이 제공
- 예시 필드명이 일관되지 않음
- 예시가 오래된 프로젝트 규칙을 사용함

---

### [실무]

나쁜 Few-Shot:

```text
Example:
좋게 설명해줘.
```

개선 Few-Shot:

```text
Example Input:
Prompt has no output format.

Example Output:
Problem:
Output format is missing.

Cause:
The prompt does not specify Markdown, JSON, Checklist, or required sections.

Risk:
The model may return inconsistent output.

Fix Direction:
Add an explicit Output Format section.

Severity:
Medium
```

Few-Shot은 예시의 양보다 실제 작업과의 일치성이 중요하다.

---

### [FAQ]

Q. Few-Shot Prompt에서 가장 흔한 실수는 뭐야?

A. 예시가 실제 작업과 맞지 않거나 최종 출력 형식과 다르게 작성되는 것이다.

Q. Few-Shot 예시는 길수록 좋아?

A. 아니다. 짧고 대표적인 예시가 더 안정적이다.

Q. Example Output의 필드명은 고정해야 해?

A. 그렇다. 필드명이 흔들리면 출력 형식도 흔들릴 수 있다.

---

# 12. Best Practice

## 12.1 Context Prompt Best Practice

### [개념]

Context Prompt Best Practice는 작업에 필요한 배경 정보를 정확하고 구조적으로 제공하는 방식이다.

---

### [핵심]

- Task와 Context를 분리한다.
- Project Context를 포함한다.
- Domain Context를 포함한다.
- Code Context를 포함한다.
- Business Rule을 명시한다.
- Environment를 명시한다.
- 오래된 정보와 최신 정보를 구분한다.
- 관련 없는 정보는 제거한다.
- 중요한 조건은 Constraint로 분리한다.
- Missing Information을 명확히 표시한다.

---

### [실무]

Context Prompt Template:

```text
Task:
[What to do]

Project Context:
[Stack / architecture / project rules]

Domain Context:
[Domain-specific criteria]

Code Context:
[Files / classes / methods / logs]

Business Rule:
[Policy / validation / state rule]

Environment:
[Version / runtime / DB / framework]

Constraints:
[Must / Must Not]

Missing Information:
[Known missing data]
```

이 Template은 코드 리뷰, 코드 생성, 디버깅, RAG 문서 제작에 공통 적용 가능하다.

---

### [FAQ]

Q. Context Prompt Best Practice는 뭐야?

A. Task와 Context를 분리하고 Project Context, Domain Context, Code Context, Business Rule, Environment를 구조적으로 제공하는 것이다.

Q. Context에서 가장 중요한 것은 뭐야?

A. 현재 작업과 직접 관련 있는 정확한 정보만 제공하는 것이다.

---

## 12.2 RAG Prompt Best Practice

### [개념]

RAG Prompt Best Practice는 검색 문서를 우선 근거로 사용하고, 문서에 없는 내용을 지어내지 않도록 제어하는 방식이다.

---

### [핵심]

- Retrieved Context를 우선 사용한다.
- Source Priority를 명시한다.
- Missing Information Rule을 포함한다.
- Assumption Rule을 포함한다.
- 문서 근거와 일반 추론을 구분한다.
- 출력 형식을 고정한다.
- 문서 간 충돌 시 처리 기준을 명시한다.
- 프로젝트 고유 정보는 임의 생성하지 않는다.
- Grounded Answer 구조를 사용한다.

---

### [실무]

RAG Prompt Template:

```text
You are a RAG Answer Agent.

Task:
[Answer / generate / review using retrieved context]

Retrieved Context:
[Retrieved documents]

Source Priority:
1. Retrieved project documents
2. User-provided context
3. General technical knowledge

Rules:
- Use retrieved context first.
- Do not invent project-specific facts.
- If context is insufficient, state missing information.
- Mark assumptions clearly.
- Separate confirmed facts and assumptions.

Output Format:
[Requested structure]
```

RAG Prompt는 답변보다 근거 사용 규칙이 먼저 설계되어야 한다.

---

### [FAQ]

Q. RAG Prompt Best Practice는 뭐야?

A. Retrieved Context 우선, Missing Information 표시, Assumption 분리, Grounded Answer 구조를 사용하는 것이다.

Q. RAG Prompt에서 가장 중요한 규칙은 뭐야?

A. 검색 문서를 우선 사용하고 문서에 없는 내용은 지어내지 않는 것이다.

---

## 12.3 Few-Shot Prompt Best Practice

### [개념]

Few-Shot Prompt Best Practice는 실제 Task와 같은 형식의 짧고 대표적인 예시를 제공해 출력 안정성을 높이는 방식이다.

---

### [핵심]

- 실제 Task와 유사한 예시를 사용한다.
- Example Input과 Example Output을 함께 제공한다.
- 최종 Output Format과 예시 형식을 일치시킨다.
- 예시는 짧고 대표적으로 작성한다.
- 필드명과 섹션명을 고정한다.
- 필요한 경우 Anti-Example을 사용한다.
- 예시를 너무 많이 넣지 않는다.
- 오래된 프로젝트 규칙이 포함된 예시는 제거한다.

---

### [실무]

Few-Shot Prompt Template:

```text
Output Pattern:
[Required fields or sections]

Example Input:
[Short representative input]

Example Output:
[Expected output format]

Rules:
- Follow the same output structure.
- Do not add extra fields unless requested.
- Keep field names consistent.
```

Few-Shot은 반복 작업, Agent Handoff, Code Review, JSON Output, RAG Answer에서 효과적이다.

---

### [FAQ]

Q. Few-Shot Prompt Best Practice는 뭐야?

A. 실제 작업과 같은 형식의 짧고 대표적인 Example Input과 Example Output을 제공하는 것이다.

Q. Few-Shot에서 가장 중요한 것은 뭐야?

A. 예시와 최종 출력 형식이 일치해야 한다는 점이다.

Q. Anti-Example은 언제 써?

A. 모델이 반복적으로 잘못된 형식이나 일반적인 답변을 낼 때 사용한다.

---

# Retrieval Queries

### [FAQ]

Q. Context Prompt가 뭐야?
A. LLM이 답변할 때 참고해야 하는 프로젝트 상황, 코드 구조, 규칙, 검색 문서 같은 배경 정보를 제공하는 Prompt다.

Q. Context Prompt는 왜 중요해?
A. LLM은 제공된 Context를 기준으로 답변하므로 Context가 부족하면 일반론이나 잘못된 답변이 나올 수 있다.

Q. Context와 Task는 분리해야 해?
A. 그렇다. Context는 판단 근거이고 Task는 수행할 작업이므로 분리해야 Prompt가 명확해진다.

Q. Project Context는 뭐야?
A. 프로젝트의 기술 스택, 버전, 아키텍처, 응답 규칙, 예외 처리 규칙 같은 프로젝트 고유 배경 정보다.

Q. Domain Context는 뭐야?
A. 특정 기술 도메인이나 업무 영역에서 적용해야 할 기준과 핵심 용어를 제공하는 Context다.

Q. Code Context는 뭐야?
A. 코드 생성, 리뷰, 리팩토링, 디버깅에 필요한 실제 코드와 관련 파일 정보다.

Q. Business Rule Context는 뭐야?
A. 기능이 어떤 업무 규칙과 정책에 따라 동작해야 하는지 설명하는 Context다.

Q. Environment Context는 뭐야?
A. 코드와 설정이 동작하는 언어, 프레임워크, DB, OS, 빌드 도구, 배포 환경 정보다.

Q. Context Quality가 뭐야?
A. LLM에게 제공된 Context가 정확하고 관련성이 높으며 작업 수행에 충분한지를 의미한다.

Q. Context Quality가 낮으면 어떻게 돼?
A. 모델이 일반론으로 답하거나 프로젝트와 맞지 않는 결과를 만들 수 있다.

Q. Context Overload가 뭐야?
A. 너무 많은 정보가 Prompt에 포함되어 모델이 핵심 작업과 중요한 조건을 놓치는 문제다.

Q. Context는 많을수록 좋아?
A. 아니다. 작업과 직접 관련 있는 정확한 Context가 중요하다.

Q. RAG Prompt가 뭐야?
A. 검색된 문서를 근거로 답변하도록 설계한 Prompt다.

Q. RAG Prompt의 핵심은 뭐야?
A. Retrieved Context를 우선 사용하고 문서에 없는 내용은 지어내지 않는 것이다.

Q. Grounded Answer는 뭐야?
A. 검색 문서나 제공된 Context에 근거해 작성한 답변이다.

Q. Retrieved Context가 뭐야?
A. RAG 시스템이 검색해서 LLM Prompt에 주입한 문서 Chunk다.

Q. Source Priority가 뭐야?
A. 여러 근거가 있을 때 어떤 정보를 먼저 따를지 정하는 우선순위 규칙이다.

Q. RAG 문서 제작에서는 무엇이 우선이야?
A. MASTER_RAG_RULES, DOMAIN_RULES, PROJECT_PROGRESS, User Request 순서로 우선 적용하는 것이 안정적이다.

Q. Missing Information Rule이 뭐야?
A. 필요한 정보가 없을 때 지어내지 않고 부족한 정보를 명확히 표시하도록 하는 규칙이다.

Q. RAG에서 Missing Information Rule은 왜 중요해?
A. 검색 문서에 없는 내용을 모델이 만들어내는 Hallucination을 줄이기 위해 중요하다.

Q. Citation / Reference Rule이 뭐야?
A. RAG 답변에서 어떤 문서나 Context를 근거로 삼았는지 표시하는 규칙이다.

Q. Grounded Answer Pattern이 뭐야?
A. 검색 문서에 근거한 내용, 추정, 부족한 정보를 분리해 답변하는 RAG Prompt 패턴이다.

Q. RAG Code Generation Pattern이 뭐야?
A. 검색 문서와 제공된 코드 Context를 근거로 기존 프로젝트 구조에 맞는 코드를 생성하는 Prompt 패턴이다.

Q. RAG Code Review Pattern이 뭐야?
A. 검색된 프로젝트 규칙과 제공된 코드를 근거로 코드 품질과 위험을 검토하는 Prompt 패턴이다.

Q. RAG Document Generation Pattern이 뭐야?
A. Master Rules, Domain Rules, Project Progress를 기반으로 검색 최적화 문서를 만드는 Prompt 패턴이다.

Q. RAG 문서는 사람용 학습 문서야?
A. 아니다. RAG 문서는 AI Agent Retrieval과 Code Generation, Review, Decision Support를 위한 문서다.

Q. Few-Shot Prompt가 뭐야?
A. 예시 입력과 예시 출력을 제공해 LLM의 출력 형식과 판단 기준을 안정화하는 Prompt다.

Q. Few-Shot Prompt는 언제 써?
A. 출력 형식이나 판단 기준을 안정화해야 할 때 사용한다.

Q. Few-Shot 예시는 많을수록 좋아?
A. 아니다. 너무 많으면 Prompt가 길어지고 핵심 Task가 흐려질 수 있다.

Q. Example Input은 뭐야?
A. Few-Shot Prompt에서 모델에게 보여주는 예시 입력이다.

Q. Example Output은 뭐야?
A. Example Input에 대해 원하는 답변 형식과 판단 기준을 보여주는 예시 출력이다.

Q. Anti-Example이 뭐야?
A. 모델이 피해야 할 잘못된 입력이나 출력 예시를 보여주는 Few-Shot 구성 요소다.

Q. Code Review Few-Shot Pattern은 뭐야?
A. 코드 리뷰 결과를 문제, 원인, 위험, 수정 방향, Severity 형식으로 안정화하는 예시 패턴이다.

Q. RAG Answer Few-Shot Pattern은 뭐야?
A. 문서 근거, 추정, 부족한 정보를 분리하는 RAG 답변 형식을 예시로 안정화하는 패턴이다.

Q. Structured Output Few-Shot Pattern은 뭐야?
A. Markdown, JSON, Checklist 같은 고정 출력 형식을 예시로 보여줘 출력 안정성을 높이는 패턴이다.

Q. Context Prompt와 RAG Prompt 차이는 뭐야?
A. Context Prompt는 배경 정보를 제공하고, RAG Prompt는 검색된 문서를 우선 근거로 답변하도록 제어한다.

Q. Zero-Shot과 Few-Shot 차이는 뭐야?
A. Zero-Shot은 예시 없이 지시만 제공하고, Few-Shot은 예시 입력과 예시 출력을 함께 제공한다.

Q. Context Prompt에서 가장 흔한 실수는 뭐야?
A. 필요한 프로젝트 정보와 코드 없이 작업을 요청하거나, 관련 없는 정보를 과도하게 넣는 것이다.

Q. RAG Prompt에서 가장 흔한 실수는 뭐야?
A. 검색 문서 우선 규칙과 Missing Information Rule을 넣지 않는 것이다.

Q. Few-Shot Prompt에서 가장 흔한 실수는 뭐야?
A. 예시가 실제 작업과 맞지 않거나 최종 출력 형식과 다르게 작성되는 것이다.

Q. Context Prompt Best Practice는 뭐야?
A. Task와 Context를 분리하고 Project Context, Domain Context, Code Context, Business Rule, Environment를 구조적으로 제공하는 것이다.

Q. RAG Prompt Best Practice는 뭐야?
A. Retrieved Context 우선, Missing Information 표시, Assumption 분리, Grounded Answer 구조를 사용하는 것이다.

Q. Few-Shot Prompt Best Practice는 뭐야?
A. 실제 작업과 같은 형식의 짧고 대표적인 Example Input과 Example Output을 제공하는 것이다.
