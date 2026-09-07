# Design Pattern Part08 - Final Index & Quality Gate

---

# 1. Final Index Overview

## 1.1 Design Pattern Final Index

### [개념]

Design Pattern Final Index는 Design Pattern RAG 문서 세트 전체를 Agent가 빠르게 검색하고 판단할 수 있도록 연결하는 최종 색인 문서이다.

Final Index는 학습용 목차가 아니다.

Final Index는 PM Agent, Backend Agent, Review Agent가 사용자 질문이나 코드 문제를 적절한 Pattern 문서로 라우팅하기 위한 Retrieval Routing 문서이다.

```text
Agent Query
→ Final Index
→ Relevant Part
→ Pattern Detail
→ Decision / Code / Review
```

---

### [핵심]

- Final Index는 Design Pattern 문서 세트의 검색 허브이다.
- Pattern 상세 설명은 각 Part 문서에서 검색한다.
- Pattern 적용 여부 판단은 Part07을 우선 검색한다.
- Pattern 오용과 구조 문제 검수는 Part06을 우선 검색한다.
- SOLID 판단은 Part01을 우선 검색한다.
- Architecture 판단은 Part05를 우선 검색한다.
- 외부 API, AOP, JPA Proxy 문제는 Part03과 Part06을 함께 검색한다.
- Over Engineering 판단은 Part06과 Part07을 함께 검색한다.

---

### [실무]

Design Pattern 문서 세트:

| Part   | File Name                                                 | Primary Purpose                              |
| ------ | --------------------------------------------------------- | -------------------------------------------- |
| Part01 | Design_Pattern_Part01_Core_SOLID.md                       | Core, OOP, SOLID                             |
| Part02 | Design_Pattern_Part02_Creational_Patterns.md              | Singleton, Factory, Builder                  |
| Part03 | Design_Pattern_Part03_Structural_Patterns.md              | Adapter, Decorator, Proxy                    |
| Part04 | Design_Pattern_Part04_Behavioral_Patterns.md              | Strategy, Observer, Template Method, Command |
| Part05 | Design_Pattern_Part05_Architecture_Patterns.md            | Layered, Hexagonal, Clean Architecture       |
| Part06 | Design_Pattern_Part06_Review_Troubleshooting.md           | Review, Smells, Troubleshooting              |
| Part07 | Design_Pattern_Part07_Pattern_Selection_Agent_Workflow.md | Pattern Selection, Agent Workflow            |
| Part08 | Design_Pattern_Part08_Final_Index_Quality_Gate.md         | Final Index, Quality Gate, Retrieval Routing |

---

### [주의]

- Final Index는 Pattern 상세 설명을 반복하지 않는다.
- Final Index는 어느 문서를 먼저 검색할지 결정하는 용도이다.
- 상세 코드 예제는 각 Pattern Part에서 검색한다.
- 검수와 오류 해결은 Part06을 우선 검색한다.
- 적용 여부가 애매하면 Part07 Anti-Decision을 함께 검색한다.
- Part08이 검색 결과에 과도하게 노출되면 별도 Collection 또는 낮은 우선순위로 분리한다.

---

### [FAQ]

Q. Design Pattern Final Index는 무엇인가?

A. Design Pattern RAG 문서 세트 전체를 Agent가 빠르게 검색하고 연결하기 위한 최종 색인 문서이다.

Q. Final Index는 사람용 목차인가?

A. 아니다. Agent Retrieval Routing과 Pattern Decision을 위한 검색 허브이다.

Q. Pattern 상세 설명은 어디서 찾는가?

A. 각 Pattern이 포함된 Part02, Part03, Part04, Part05 문서에서 찾는다.

Q. Pattern 적용 여부가 애매하면 어디를 검색하는가?

A. Part07 Pattern Selection과 Pattern Anti-Decision을 우선 검색한다.

---

# 2. Document Routing Index

## 2.1 Query Intent Routing

### [개념]

Query Intent Routing은 사용자 질문이나 Agent 내부 질문을 의도별로 분류하고 적절한 Design Pattern 문서로 연결하는 규칙이다.

```text
User Query
→ Intent Classification
→ Document Routing
→ Section Retrieval
→ Answer Generation
```

---

### [핵심]

- 구현 질문은 관련 Pattern Part와 Part07을 함께 검색한다.
- 검수 질문은 Part06을 우선 검색한다.
- 설계 원칙 질문은 Part01을 우선 검색한다.
- 객체 생성 질문은 Part02를 우선 검색한다.
- 외부 연동, Adapter, Proxy 질문은 Part03을 우선 검색한다.
- 이벤트, 정책, 재시도 질문은 Part04를 우선 검색한다.
- 아키텍처 질문은 Part05를 우선 검색한다.
- 적용 여부 판단 질문은 Part07을 우선 검색한다.

---

### [실무]

| Query Intent                     | Primary Search | Secondary Search  |
| -------------------------------- | -------------- | ----------------- |
| SOLID 원칙                       | Part01         | Part06            |
| SRP / OCP / DIP 위반             | Part01         | Part06            |
| 객체 생성 문제                   | Part02         | Part07            |
| Factory / Builder / Singleton    | Part02         | Part06            |
| 외부 API 연동                    | Part03         | Part05, Part06    |
| Adapter / Port                   | Part03         | Part05, Part07    |
| AOP / Transaction / Lazy Loading | Part03         | Part06            |
| Strategy / 정책 교체             | Part04         | Part01, Part07    |
| Spring Event / Kafka             | Part04         | Part06            |
| Command Queue / Retry            | Part04         | Part06            |
| Layered / Hexagonal / Clean      | Part05         | Part06            |
| God Service / Layer Violation    | Part05         | Part06            |
| Pattern Review                   | Part06         | Part01, Part07    |
| Pattern 적용 판단                | Part07         | 관련 Pattern Part |
| Agent Workflow                   | Part07         | Part06            |
| 최종 품질 검수                   | Part08         | Part06            |

---

### [예제]

```text
질문:
외부 API 응답 DTO를 Service에서 바로 써도 돼?

Routing:
Part03 Adapter Pattern
Part05 Hexagonal Architecture
Part06 Adapter Troubleshooting
Part07 Structural Pattern Selection
```

```text
질문:
if 문이 많아졌는데 Strategy로 바꿔야 해?

Routing:
Part01 OCP
Part04 Strategy Pattern
Part06 Strategy Troubleshooting
Part07 Pattern Anti-Decision
```

```text
질문:
Service가 너무 커졌는데 어떻게 나눌까?

Routing:
Part01 SRP
Part05 God Service Problem
Part06 SRP Violation
Part07 Pattern Selection
```

```text
질문:
@Transactional이 왜 안 먹지?

Routing:
Part03 Spring AOP Proxy
Part06 Proxy Troubleshooting
Part07 Structural Pattern Selection
```

---

### [주의]

- Routing 결과는 Pattern 적용 확정이 아니다.
- Routing 이후 현재 프로젝트 문맥을 반드시 반영한다.
- 여러 문서가 검색되면 가장 단순하고 직접적인 해결책을 우선한다.
- Architecture 질문은 Over Engineering 위험을 함께 검색한다.
- Review 질문은 Part06 Troubleshooting을 반드시 포함한다.

---

### [FAQ]

Q. Query Intent Routing은 무엇인가?

A. 사용자 질문이나 Agent 내부 질문을 의도별로 분류해 적절한 RAG 문서로 연결하는 규칙이다.

Q. 검수 질문은 어디를 우선 검색하는가?

A. Part06 Review & Troubleshooting을 우선 검색한다.

Q. 구현 질문은 어디를 우선 검색하는가?

A. 관련 Pattern Part와 Part07 Pattern Selection을 함께 검색한다.

Q. Architecture 질문은 어디를 우선 검색하는가?

A. Part05 Architecture Patterns와 Part06 Troubleshooting을 함께 검색한다.

---

## 2.2 Pattern Name Routing

### [개념]

Pattern Name Routing은 사용자가 특정 Pattern 이름을 언급했을 때 해당 Pattern의 상세 설명, 적용 기준, Troubleshooting 문서로 연결하는 규칙이다.

```text
Pattern Name
→ Pattern Detail Part
→ Troubleshooting Part
→ Selection Part
```

---

### [핵심]

- Pattern 이름이 명시되면 해당 Pattern Part를 우선 검색한다.
- 적용 여부 판단은 Part07을 추가 검색한다.
- 오용 가능성 검수는 Part06을 추가 검색한다.
- 관련 SOLID 원칙은 Part01을 추가 검색한다.
- Architecture Pattern은 Part05와 Part06을 함께 검색한다.
- 사용자가 언급한 Pattern이 실제 문제에 맞는지 다시 검토한다.

---

### [실무]

| Pattern Name            | Detail Search | Review Search                              | Selection Search              |
| ----------------------- | ------------- | ------------------------------------------ | ----------------------------- |
| Singleton               | Part02        | Part06 Singleton State Bug                 | Part07 Creational Selection   |
| Factory                 | Part02        | Part06 Factory Troubleshooting             | Part07 Creational Selection   |
| Builder                 | Part02        | Part06 Builder Troubleshooting             | Part07 Creational Selection   |
| Adapter                 | Part03        | Part06 Adapter Troubleshooting             | Part07 Structural Selection   |
| Decorator               | Part03        | Part06 Decorator Overuse                   | Part07 Structural Selection   |
| Proxy                   | Part03        | Part06 Proxy Troubleshooting               | Part07 Structural Selection   |
| Strategy                | Part04        | Part06 Strategy Troubleshooting            | Part07 Behavioral Selection   |
| Observer                | Part04        | Part06 Observer Troubleshooting            | Part07 Behavioral Selection   |
| Template Method         | Part04        | Part06 Template Method Inheritance Problem | Part07 Behavioral Selection   |
| Command                 | Part04        | Part06 Command Retry Bug                   | Part07 Behavioral Selection   |
| Chain of Responsibility | Part04        | Part03 Security Filter Chain               | Part07 Behavioral Selection   |
| Mediator                | Part04        | Part07 Agent Workflow                      | Part07 Behavioral Selection   |
| Layered Architecture    | Part05        | Part06 Layer Violation                     | Part07 Architecture Selection |
| Hexagonal Architecture  | Part05        | Part06 Dependency Direction                | Part07 Architecture Selection |
| Clean Architecture      | Part05        | Part06 Domain Leakage                      | Part07 Architecture Selection |

---

### [예제]

```text
질문:
Builder를 Entity에 써도 돼?

Routing:
Part02 Lombok Builder
Part06 Builder Troubleshooting
Part07 Creational Pattern Selection
```

```text
질문:
Observer로 알림을 분리할까?

Routing:
Part04 Observer
Part04 Spring Event
Part06 Observer Troubleshooting
Part07 Behavioral Pattern Selection
```

```text
질문:
Clean Architecture로 바꾸는 게 좋을까?

Routing:
Part05 Clean Architecture
Part05 Domain Isolation
Part06 Over Engineering Architecture
Part07 Architecture Pattern Selection
```

---

### [주의]

- Pattern 이름이 언급되어도 실제 문제와 맞는지 재분류한다.
- 사용자가 제시한 Pattern이 Wrong Pattern Choice일 수 있다.
- Pattern Name Routing 후 Problem Classification을 다시 수행한다.
- Pattern 적용 대신 단순 구조 유지가 더 나을 수 있다.

---

### [FAQ]

Q. Pattern Name Routing은 무엇인가?

A. 특정 Pattern 이름이 언급되었을 때 상세 문서, 검수 문서, 선택 문서로 연결하는 규칙이다.

Q. 사용자가 Strategy를 언급하면 바로 Strategy를 적용하는가?

A. 아니다. Part04와 Part07을 검색한 뒤 실제 문제가 알고리즘 교체인지 검토한다.

Q. 사용자가 Adapter를 언급하면 어디를 검색하는가?

A. Part03 Adapter, Part06 Adapter Troubleshooting, Part07 Structural Selection을 검색한다.

Q. 사용자가 Clean Architecture를 언급하면 어디를 검색하는가?

A. Part05 Clean Architecture, Part06 Domain Leakage, Part07 Architecture Selection을 검색한다.

---

# 3. Agent Role Index

## 3.1 PM Agent Index

### [개념]

PM Agent Index는 PM Agent가 사용자 요구사항을 분석할 때 우선 검색해야 하는 Design Pattern 문서와 판단 기준을 정의한다.

PM Agent는 요구사항을 설계 문제와 Agent 작업 지시로 변환한다.

```text
User Requirement
→ PM Agent
→ Requirement Classification
→ Pattern Candidate
→ Backend Task
→ Review Checklist
```

---

### [핵심]

- PM Agent는 구현보다 분류를 우선한다.
- PM Agent는 단순 CRUD와 복잡 Domain을 구분한다.
- PM Agent는 외부 시스템 연동 여부를 식별한다.
- PM Agent는 정책 교체 가능성을 식별한다.
- PM Agent는 이벤트 후속 작업과 비동기 요구를 식별한다.
- PM Agent는 Over Engineering 위험을 표시한다.
- PM Agent는 Backend Agent와 Review Agent에 명확한 지시를 전달한다.

---

### [실무]

PM Agent 우선 검색:

| 상황                 | Search                                |
| -------------------- | ------------------------------------- |
| 요구사항 분류        | Part07 PM Agent Workflow              |
| Pattern 후보 판단    | Part07 Pattern Selection Matrix       |
| Architecture 선택    | Part05 Architecture Pattern Selection |
| 외부 연동 요구       | Part03 Adapter, Part05 Hexagonal      |
| 정책 교체 요구       | Part04 Strategy                       |
| 이벤트 후속 처리     | Part04 Observer                       |
| 재시도 / 비동기 작업 | Part04 Command Queue                  |
| 과설계 위험          | Part07 Pattern Anti-Decision          |
| 검수 포인트 생성     | Part06 Review Agent Rules             |

---

### [PM Agent Output Template]

```text
요구사항:
...

기능 분류:
...

설계 위험:
...

Pattern 후보:
...

Backend Agent 지시:
...

Review Agent 검수:
...

Over Engineering 주의:
...
```

---

### [주의]

- PM Agent는 Pattern을 확정하지 않는다.
- PM Agent는 후보와 위험을 전달한다.
- PM Agent는 단순 기능에 과도한 구조를 요구하지 않는다.
- PM Agent는 실패 처리, 재시도, Timeout, Rate Limit을 놓치지 않는다.
- PM Agent는 Agent 간 역할 중복을 줄인다.

---

### [FAQ]

Q. PM Agent는 Design Pattern 문서를 어떻게 사용하는가?

A. 요구사항을 설계 문제로 분류하고 Pattern 후보와 검수 포인트를 다른 Agent에게 전달한다.

Q. PM Agent는 어느 문서를 우선 검색하는가?

A. Part07 Pattern Selection과 PM Agent Workflow를 우선 검색한다.

Q. PM Agent가 외부 시스템 연동을 발견하면?

A. Adapter, Port, Timeout, Retry, 예외 변환, 외부 DTO 격리를 지시한다.

Q. PM Agent가 단순 CRUD를 발견하면?

A. Layered Architecture 기반 단순 구현을 지시하고 과도한 Pattern 적용을 금지한다.

---

## 3.2 Backend Agent Index

### [개념]

Backend Agent Index는 Backend Agent가 코드 생성 또는 수정 시 우선 검색해야 하는 Design Pattern 문서와 구현 판단 기준을 정의한다.

Backend Agent는 요구사항을 Spring Boot 코드 구조로 변환한다.

```text
Backend Task
→ Pattern Search
→ Simple Design First
→ Code Generation
→ Self Review
```

---

### [핵심]

- Backend Agent는 단순 구조를 기본값으로 사용한다.
- Backend Agent는 변경 지점이 확인된 곳에 Pattern을 적용한다.
- Backend Agent는 Java 21, Spring Boot 3.x 기준으로 작성한다.
- Backend Agent는 외부 API DTO를 내부 Service에 노출하지 않는다.
- Backend Agent는 Entity 상태 변경을 의미 있는 Method로 캡슐화한다.
- Backend Agent는 Transaction, Event, Proxy, Retry 제약을 고려한다.
- Backend Agent는 Review Agent가 검수할 수 있는 구조로 출력한다.

---

### [실무]

Backend Agent 우선 검색:

| 구현 상황                          | Search                                         |
| ---------------------------------- | ---------------------------------------------- |
| Controller-Service-Repository 구현 | Part05 Layered Architecture                    |
| 객체 생성 / DTO 생성               | Part02 Factory, Builder, Static Factory Method |
| 외부 API 연동                      | Part03 Adapter, Part05 Hexagonal               |
| 결제 / 알림 타입별 처리            | Part04 Strategy, Part02 Factory                |
| 후속 작업 분리                     | Part04 Observer, Spring Event                  |
| 재시도 / Queue                     | Part04 Command Queue                           |
| 공통 흐름 반복                     | Part04 Template Method                         |
| AOP / Transaction                  | Part03 Proxy                                   |
| Domain Rule 위치                   | Part05 Domain Isolation                        |
| 최종 자체 검수                     | Part06 Review & Troubleshooting                |

---

### [Backend Agent Self Review]

```text
1. 단순 구조로 충분한가?
2. Pattern 적용 이유가 명확한가?
3. 외부 DTO가 내부로 들어오지 않는가?
4. Service가 비대하지 않은가?
5. Entity 상태 변경이 Setter로 흩어지지 않는가?
6. Strategy / Factory가 과도하지 않은가?
7. Event 처리 실패와 Transaction Phase가 고려되었는가?
8. Command Retry에 멱등성이 있는가?
9. @Transactional Self Invocation 문제가 없는가?
10. Review Agent가 검수할 포인트가 명확한가?
```

---

### [주의]

- Backend Agent는 모든 Service에 Interface를 만들지 않는다.
- Backend Agent는 모든 외부 호출을 무조건 Port로 감싸지 않는다.
- Backend Agent는 단순 DTO에 Builder를 강제하지 않는다.
- Backend Agent는 Event로 분리하면 흐름 가시성과 실패 처리를 함께 고려한다.
- Backend Agent는 Pattern 적용 후 코드가 더 나빠졌는지 자체 검수한다.

---

### [FAQ]

Q. Backend Agent는 Design Pattern 문서를 어떻게 사용하는가?

A. 요구사항 구현 전 Pattern 후보를 검색하고 코드 생성 후 자체 검수에 사용한다.

Q. Backend Agent의 기본 구조는?

A. 단순 기능은 Layered Architecture를 기본으로 한다.

Q. Backend Agent는 외부 API를 어떻게 처리해야 하는가?

A. External API Adapter로 감싸고 외부 DTO를 내부 Result로 변환해야 한다.

Q. Backend Agent는 언제 Pattern 적용을 보류해야 하는가?

A. 변경 가능성이 낮고 단순 구조가 더 명확할 때 보류해야 한다.

---

## 3.3 Review Agent Index

### [개념]

Review Agent Index는 Review Agent가 코드와 구조를 검수할 때 우선 검색해야 하는 Design Pattern 문서와 Review 기준을 정의한다.

Review Agent는 Pattern 누락, Pattern 오용, Over Engineering을 모두 검수한다.

```text
Generated Code
→ Review Agent
→ Smell Detection
→ Pattern Fit Review
→ Troubleshooting
→ Refactoring Proposal
```

---

### [핵심]

- Review Agent는 Part06을 우선 검색한다.
- Review Agent는 SOLID 위반을 Part01로 검수한다.
- Review Agent는 Architecture 위반을 Part05로 검수한다.
- Review Agent는 Pattern 적용 여부를 Part07로 검수한다.
- Review Agent는 구체적인 문제, 원인, 해결, Trade-off를 출력한다.
- Review Agent는 Pattern 추가뿐 아니라 Pattern 제거도 제안한다.
- Review Agent는 Agent 생성 코드의 일관성을 검수한다.

---

### [실무]

Review Agent 우선 검색:

| Review Signal         | Search                                              |
| --------------------- | --------------------------------------------------- |
| 책임 집중             | Part01 SRP, Part06 SRP Violation                    |
| 조건문 증가           | Part01 OCP, Part04 Strategy, Part06 OCP Violation   |
| 외부 Client 직접 의존 | Part01 DIP, Part03 Adapter, Part06 DIP Violation    |
| Controller 비대       | Part05 Layer Responsibility, Part06 Layer Violation |
| Service 비대          | Part05 God Service, Part06 SRP Violation            |
| Entity Builder 문제   | Part02 Builder, Part06 Builder Troubleshooting      |
| Event 흐름 숨김       | Part04 Observer, Part06 Observer Troubleshooting    |
| Command 중복 실행     | Part04 Command, Part06 Command Retry Bug            |
| Transaction 미동작    | Part03 Proxy, Part06 Proxy Troubleshooting          |
| Domain Rule 분산      | Part05 Domain Isolation, Part06 Domain Leakage      |
| 과도한 Interface      | Part06 Excessive Abstraction, Part07 Anti-Decision  |
| Architecture 과설계   | Part06 Over Engineering, Part07 Anti-Decision       |

---

### [Review Agent Output Template]

```text
[Design Pattern Review]

문제:
...

원인:
...

관련 원칙:
...

관련 Pattern:
...

해결:
1. ...
2. ...
3. ...

Trade-off:
...

최종 판단:
적용 권장 / 단순 구조 유지 / Pattern 제거 권장
```

---

### [주의]

- Review Agent는 무조건 Pattern을 추가하지 않는다.
- Review Agent는 현재 요구사항과 코드 규모를 반영한다.
- Review Agent는 적용 비용과 팀 이해도를 고려한다.
- Review Agent는 구체적인 수정 단위를 제시한다.
- Review Agent는 Pattern 이름만으로 정답을 만들지 않는다.

---

### [FAQ]

Q. Review Agent는 어느 문서를 우선 검색하는가?

A. Part06 Review & Troubleshooting을 우선 검색한다.

Q. Review Agent는 Pattern 제거를 제안할 수 있는가?

A. 그렇다. 불필요한 추상화나 Pattern은 제거를 제안해야 한다.

Q. Review Agent는 어떤 형식으로 답변하는가?

A. 문제, 원인, 관련 원칙, 관련 Pattern, 해결, Trade-off, 최종 판단 형식이 적합하다.

Q. Review Agent가 가장 주의해야 할 점은?

A. Pattern 적용을 정답처럼 강제하지 않고 현재 문제에 맞는 최소 구조를 제안하는 것이다.

---

# 4. Quality Gate

## 4.1 RAG Document Quality Gate

### [개념]

RAG Document Quality Gate는 Design Pattern 문서가 Agent Retrieval, Code Generation, Review, Decision Support에 적합한지 최종 검수하는 기준이다.

Quality Gate는 문서 업로드 전 문서 구조와 검색 품질을 점검하기 위한 기준이다.

```text
Draft
→ Structure Check
→ Retrieval Check
→ Consistency Check
→ Agent Usability Check
→ Upload Decision
```

---

### [핵심]

- Markdown 구조가 명확해야 한다.
- `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`가 포함되어야 한다.
- FAQ는 Q + A 구조여야 한다.
- Retrieval Queries가 문서 마지막에 있어야 한다.
- Pattern 이름과 핵심 용어가 일관되어야 한다.
- Java 21, Spring Boot 3.x 기준이어야 한다.
- Legacy 중심 설명을 피해야 한다.
- Agent가 코드 생성과 검수에 사용할 수 있어야 한다.

---

### [Checklist]

Structure Quality:

- 제목과 파일명이 명확한가?
- Section이 Chunk 단위로 나뉘었는가?
- 한 Chunk가 하나의 개념을 중심으로 하는가?
- 긴 문단보다 bullet 중심인가?
- Code Block과 Flow가 검색 친화적인가?

Required Sections:

- [개념] 포함
- [핵심] 포함
- [실무] 포함
- [FAQ] 포함
- Retrieval Queries 포함

Retrieval Quality:

- 핵심 키워드가 반복되는가?
- Pattern 이름 영어 표기가 유지되는가?
- 질문형 FAQ가 충분한가?
- User Query와 Agent Query 모두 매칭 가능한가?
- Troubleshooting Query가 포함되어 있는가?

Technical Quality:

- Java 21 기준인가?
- Spring Boot 3.x 기준인가?
- Spring DI, AOP, Event, Transaction, JPA Proxy 설명이 현재 구조와 맞는가?
- 외부 API, Adapter, Port 설명이 실무 구조와 맞는가?
- 과도한 Legacy 설명이 없는가?

Agent Usability:

- PM Agent가 요구사항 분류에 사용할 수 있는가?
- Backend Agent가 코드 구조 선택에 사용할 수 있는가?
- Review Agent가 구조 검수에 사용할 수 있는가?
- Over Engineering 판단 기준이 있는가?
- Pattern Anti-Decision 기준이 있는가?

---

### [주의]

- 문서가 사람에게 읽기 좋아도 Retrieval에 약하면 실패이다.
- 긴 서론과 장문 설명은 검색 품질을 낮춘다.
- FAQ가 부족하면 실제 질문 매칭률이 낮아진다.
- Troubleshooting이 약하면 Review Agent 성능이 떨어진다.
- Pattern 남용 경고가 없으면 Backend Agent가 과설계할 수 있다.

---

### [FAQ]

Q. RAG Document Quality Gate는 무엇인가?

A. RAG 문서가 Agent 검색, 코드 생성, 검수에 적합한지 최종 검수하는 기준이다.

Q. Quality Gate에서 가장 중요한 항목은?

A. Retrieval Quality, FAQ 품질, Troubleshooting 품질, Agent Usability이다.

Q. RAG 문서에 FAQ가 왜 중요한가?

A. 사용자 질문과 Agent Query가 FAQ 형태로 검색될 가능성이 높기 때문이다.

Q. RAG 문서가 실패하는 대표 원인은?

A. 장문 설명, FAQ 부족, Pattern 적용 기준 부족, Troubleshooting 부족이다.

---

## 4.2 Design Pattern Quality Criteria

### [개념]

Design Pattern Quality Criteria는 Design Pattern RAG 문서의 품질을 구조, 검색성, 실무성, 검수성, Agent 활용성 기준으로 평가하기 위한 기준이다.

Quality Criteria는 확정 점수를 부여하기 위한 문서가 아니라 업로드 전 검수 항목을 명확히 하기 위한 문서이다.

```text
Document
→ Structure
→ Retrieval
→ Technical Accuracy
→ Troubleshooting
→ Agent Usability
```

---

### [핵심]

- 품질 기준은 구조, 검색성, 기술 정확성, Troubleshooting, Agent 활용성, 일관성으로 나눈다.
- 문서가 길어도 검색성이 낮으면 품질이 낮다.
- Code Example이 많아도 적용 기준이 없으면 품질이 낮다.
- FAQ와 Retrieval Queries는 높은 우선순위를 가진다.
- Troubleshooting은 Review Agent 성능에 직접 연결된다.
- 점수보다 실제 Retrieval Test가 중요하다.

---

### [Quality Criteria Table]

| Category               | Priority | Criteria                                 |
| ---------------------- | -------- | ---------------------------------------- |
| Structure              | High     | Header, Section, Chunk 분리              |
| Retrieval Optimization | Critical | FAQ, Keyword, Query Matching             |
| Technical Accuracy     | High     | Java 21, Spring Boot 3.x, Pattern 정확성 |
| Troubleshooting        | Critical | 문제, 원인, 해결 구조                    |
| Agent Usability        | Critical | PM, Backend, Review Agent 활용성         |
| Consistency            | High     | 용어, Naming, 문서 간 연결               |

---

### [감점 기준]

| 문제                       | Risk     |
| -------------------------- | -------- |
| FAQ 부족                   | High     |
| Retrieval Queries 없음     | Critical |
| Pattern 적용 기준 없음     | High     |
| Troubleshooting 없음       | High     |
| 장문 에세이형 설명         | Medium   |
| 용어 혼용                  | Medium   |
| Spring Boot 실무 예시 부족 | Medium   |
| Pattern 남용 주의 없음     | High     |
| Agent별 사용 기준 없음     | Medium   |

---

### [주의]

- Quality Criteria는 문서 개선 기준이다.
- 고정 점수보다 검색 테스트 결과가 중요하다.
- FAQ 반복은 허용되지만 의미 없는 중복은 피한다.
- Chunk가 너무 길면 검색 품질이 떨어진다.
- 문서 간 용어 통일이 중요하다.

---

### [FAQ]

Q. Design Pattern Quality Criteria는 무엇인가?

A. Design Pattern RAG 문서 품질을 구조, 검색성, 기술 정확성, Troubleshooting, Agent 활용성 기준으로 평가하는 기준이다.

Q. 가장 중요한 품질 기준은?

A. Retrieval Optimization, Troubleshooting, Agent Usability이다.

Q. 가장 위험한 품질 문제는?

A. FAQ 부족, Retrieval Queries 없음, Troubleshooting 부족, Pattern 적용 기준 부족이다.

Q. 품질 기준을 통과하면 바로 충분한가?

A. 아니다. 실제 Agent Retrieval Test와 문서 간 연계 검수가 필요하다.

---

# 5. Cross-Part Consistency Gate

## 5.1 Naming Consistency

### [개념]

Naming Consistency는 Design Pattern 문서 전체에서 핵심 용어, Pattern 이름, Agent 이름, Architecture 용어를 일관되게 유지하는 규칙이다.

용어가 흔들리면 Retrieval 품질과 Agent 판단 품질이 떨어진다.

```text
Consistent Naming
→ Better Retrieval
→ Better Agent Reasoning
```

---

### [핵심]

- Pattern 이름은 영어 표기를 유지한다.
- Agent 이름은 PM Agent, Backend Agent, Review Agent로 통일한다.
- Architecture 용어는 Layered Architecture, Hexagonal Architecture, Clean Architecture로 통일한다.
- Port, Adapter, Domain, Use Case 용어를 혼용하지 않는다.
- DTO, Entity, Domain Model 역할을 구분한다.
- Event와 Command를 혼용하지 않는다.

---

### [실무]

권장 용어:

| Concept            | Standard Naming         |
| ------------------ | ----------------------- |
| 설계 패턴          | Design Pattern          |
| 생성 패턴          | Creational Pattern      |
| 구조 패턴          | Structural Pattern      |
| 행동 패턴          | Behavioral Pattern      |
| 전략 패턴          | Strategy Pattern        |
| 관찰자 패턴        | Observer Pattern        |
| 템플릿 메서드 패턴 | Template Method Pattern |
| 명령 패턴          | Command Pattern         |
| 포트               | Port                    |
| 어댑터             | Adapter                 |
| 계층형 아키텍처    | Layered Architecture    |
| 헥사고날 아키텍처  | Hexagonal Architecture  |
| 클린 아키텍처      | Clean Architecture      |
| 의존성 규칙        | Dependency Rule         |
| 도메인 격리        | Domain Isolation        |
| 과설계             | Over Engineering        |

---

### [주의]

- Event와 Command를 같은 의미로 사용하지 않는다.
- Adapter와 Facade를 혼동하지 않는다.
- Decorator와 Proxy를 목적 없이 혼용하지 않는다.
- Service Interface와 Port를 구분한다.
- Domain Entity와 Response DTO를 구분한다.
- Pattern 이름은 가능하면 영어 원문을 유지한다.

---

### [FAQ]

Q. Naming Consistency가 중요한 이유는?

A. 용어가 일관되어야 RAG 검색과 Agent 판단이 안정적으로 동작하기 때문이다.

Q. Pattern 이름은 한글로 번역해야 하는가?

A. 문서에서는 영어 Pattern 이름을 유지하고 필요 시 한글 설명을 덧붙인다.

Q. Command와 Event는 왜 구분해야 하는가?

A. Command는 앞으로 수행할 요청이고 Event는 이미 발생한 사실이기 때문이다.

Q. Port와 Adapter는 왜 구분해야 하는가?

A. Port는 내부 Interface이고 Adapter는 외부 기술 구현체이기 때문이다.

---

## 5.2 Cross-Part Link Consistency

### [개념]

Cross-Part Link Consistency는 Design Pattern 문서 각 Part가 서로 충돌하지 않고 같은 판단 기준을 공유하도록 검수하는 규칙이다.

```text
Part01 SOLID
→ Part02~Part05 Pattern
→ Part06 Troubleshooting
→ Part07 Selection
→ Part08 Index
```

---

### [핵심]

- Part01 SOLID는 모든 Pattern 판단의 기준이다.
- Part02~Part05는 Pattern별 상세 기준이다.
- Part06은 Review와 Troubleshooting 기준이다.
- Part07은 Pattern Selection과 Agent Workflow 기준이다.
- Part08은 최종 Index와 Quality Gate 기준이다.
- 문서 간 설명이 충돌하면 Core 원칙과 Domain Rules를 우선한다.

---

### [실무]

Cross-Part 연결 규칙:

| Source              | Target                              | Link Purpose           |
| ------------------- | ----------------------------------- | ---------------------- |
| Part01 SRP          | Part06 SRP Violation                | 책임 분리 검수         |
| Part01 OCP          | Part04 Strategy                     | 정책 확장 판단         |
| Part01 DIP          | Part03 Adapter, Part05 Hexagonal    | 외부 의존성 격리       |
| Part02 Factory      | Part04 Strategy                     | Strategy 선택 구조     |
| Part03 Proxy        | Part06 Proxy Troubleshooting        | AOP / Transaction 문제 |
| Part04 Observer     | Part06 Observer Troubleshooting     | Event 실패 처리        |
| Part04 Command      | Part06 Command Retry Bug            | 재시도 / 멱등성 검수   |
| Part05 Architecture | Part06 Architecture Troubleshooting | 계층 / 의존성 검수     |
| Part07 Selection    | Part06 Review                       | 적용 전후 검수         |
| Part08 Index        | All Parts                           | Retrieval Routing      |

---

### [주의]

- Part별 내용이 중복되어도 목적이 다르면 허용된다.
- Core 개념은 Part01을 우선 기준으로 한다.
- Troubleshooting은 Part06을 우선 기준으로 한다.
- Selection은 Part07을 우선 기준으로 한다.
- Routing과 Quality Gate는 Part08을 우선 기준으로 한다.

---

### [FAQ]

Q. Cross-Part Link Consistency는 무엇인가?

A. Design Pattern 문서 각 Part가 서로 충돌하지 않고 같은 판단 기준으로 연결되도록 검수하는 규칙이다.

Q. SOLID 판단은 어느 문서를 기준으로 하는가?

A. Part01 Core & SOLID를 기준으로 한다.

Q. Troubleshooting 판단은 어느 문서를 기준으로 하는가?

A. Part06 Review & Troubleshooting을 기준으로 한다.

Q. Pattern Selection 판단은 어느 문서를 기준으로 하는가?

A. Part07 Pattern Selection & Agent Workflow를 기준으로 한다.

---

# 6. Upload Test Guide

## 6.1 Retrieval Test Query

### [개념]

Retrieval Test Query는 Design Pattern 문서 업로드 후 RAG 검색 품질을 확인하기 위한 테스트 질문이다.

테스트 목적은 Agent가 올바른 Part를 검색하고, Pattern 상세 설명과 Troubleshooting 문서를 함께 참조하는지 확인하는 것이다.

```text
Upload Documents
→ Run Test Query
→ Check Retrieved Part
→ Adjust Documents / Retrieval Settings
```

---

### [핵심]

- 업로드 후 반드시 검색 테스트를 수행한다.
- 질문별로 기대 검색 문서를 정한다.
- Part08만 반복 검색되면 검색 노이즈로 판단한다.
- Part06은 Review 질문에서 우선 검색되어야 한다.
- Part07은 Pattern 선택 질문에서 우선 검색되어야 한다.
- Pattern 상세 질문은 Part02~Part05가 우선 검색되어야 한다.

---

### [실무]

업로드 후 테스트 Query:

```text
Service가 너무 커졌는데 어떻게 나눠?
외부 API DTO를 Service에서 바로 써도 돼?
if 문 많으면 Strategy로 바꿔야 해?
@Transactional이 왜 안 먹지?
Entity에 Builder 써도 돼?
단순 CRUD에도 Hexagonal Architecture 써야 해?
Event로 분리하면 뭐가 문제야?
Command 재시도할 때 중복 실행은 어떻게 막아?
Controller에서 Repository 바로 호출해도 돼?
Port랑 Adapter 차이가 뭐야?
```

기대 검색 결과:

| Test Query                                    | Expected Retrieval     |
| --------------------------------------------- | ---------------------- |
| Service가 너무 커졌는데 어떻게 나눠?          | Part01, Part05, Part06 |
| 외부 API DTO를 Service에서 바로 써도 돼?      | Part03, Part05, Part06 |
| if 문 많으면 Strategy로 바꿔야 해?            | Part04, Part07, Part06 |
| @Transactional이 왜 안 먹지?                  | Part03, Part06         |
| Entity에 Builder 써도 돼?                     | Part02, Part06         |
| 단순 CRUD에도 Hexagonal Architecture 써야 해? | Part05, Part07, Part06 |
| Event로 분리하면 뭐가 문제야?                 | Part04, Part06         |
| Command 재시도할 때 중복 실행은 어떻게 막아?  | Part04, Part06         |
| Controller에서 Repository 바로 호출해도 돼?   | Part05, Part06         |
| Port랑 Adapter 차이가 뭐야?                   | Part03, Part05, Part07 |

---

### [주의]

- Part08은 Routing 보조 문서이므로 모든 질문에서 1순위로 잡히면 좋지 않다.
- Part08이 과도하게 검색되면 별도 Collection으로 분리한다.
- Completion Report 같은 메타 문서는 업로드하지 않는다.
- Chunk Size와 Top-K 값에 따라 검색 결과가 달라질 수 있다.
- 검색 결과가 부정확하면 해당 Part의 FAQ와 Retrieval Queries를 보강한다.

---

### [FAQ]

Q. Retrieval Test Query는 무엇인가?

A. RAG 업로드 후 문서 검색 품질을 확인하기 위한 테스트 질문이다.

Q. 업로드 후 무엇을 확인해야 하는가?

A. 질문별로 기대한 Part 문서가 검색되는지 확인해야 한다.

Q. Part08만 계속 검색되면 어떻게 하는가?

A. Part08을 별도 Collection으로 분리하거나 검색 우선순위를 낮춘다.

Q. 검색 결과가 부정확하면 어떻게 하는가?

A. 해당 Part의 FAQ, Retrieval Queries, 핵심 키워드를 보강한다.

---

## 6.2 Upload Set Recommendation

### [개념]

Upload Set Recommendation은 Design Pattern 문서 세트를 RAG 시스템에 업로드할 때 어떤 문서를 포함하고 제외할지 결정하는 기준이다.

```text
Document Set
→ Upload Include / Exclude
→ Retrieval Quality
```

---

### [핵심]

- 기본 업로드 대상은 Part01부터 Part08이다.
- Completion Report는 업로드하지 않는다.
- Part08은 Routing 문서이므로 검색 노이즈 여부를 확인한다.
- Part08이 검색 품질을 방해하면 별도 Collection으로 분리한다.
- Pattern 상세 검색은 Part02~Part05가 우선 잡혀야 한다.
- Review 검색은 Part06이 우선 잡혀야 한다.
- Pattern 선택 검색은 Part07이 우선 잡혀야 한다.

---

### [실무]

권장 업로드 세트:

```text
Upload Include:
Design_Pattern_Part01_Core_SOLID.md
Design_Pattern_Part02_Creational_Patterns.md
Design_Pattern_Part03_Structural_Patterns.md
Design_Pattern_Part04_Behavioral_Patterns.md
Design_Pattern_Part05_Architecture_Patterns.md
Design_Pattern_Part06_Review_Troubleshooting.md
Design_Pattern_Part07_Pattern_Selection_Agent_Workflow.md
Design_Pattern_Part08_Final_Index_Quality_Gate.md
```

업로드 제외:

```text
Upload Exclude:
Design_Pattern_Final_Completion_Report.md
```

검색 노이즈 발생 시 조정:

```text
If Part08 dominates search results:
→ Move Part08 to separate Collection
→ Or lower retrieval priority
→ Or use Part08 only for PM / Routing Agent
```

---

### [주의]

- Completion Report는 메타 정보가 많아 실제 설계 판단 검색에 방해가 될 수 있다.
- Final Index는 유용하지만 Pattern 상세 답변을 대체하면 안 된다.
- Part08은 업로드 후 검색 테스트 결과에 따라 유지 또는 분리한다.
- Part01~Part07은 기본 업로드 대상으로 유지한다.

---

### [FAQ]

Q. Design Pattern 문서 중 어떤 파일을 업로드하는가?

A. Part01부터 Part08까지 업로드한다.

Q. Completion Report는 업로드하는가?

A. 업로드하지 않는다. 보관용 문서로만 유지한다.

Q. Part08은 업로드해야 하는가?

A. 기본적으로 업로드 가능하다. 다만 검색 노이즈가 발생하면 별도 Collection으로 분리한다.

Q. 검색 노이즈가 발생하면 무엇을 조정하는가?

A. Part08 분리, Chunk 설정, Top-K, FAQ 보강, 문서 우선순위를 조정한다.

---

# 7. Final Execution Gate

## 7.1 PM Agent Execution Gate

### [개념]

PM Agent Execution Gate는 PM Agent가 사용자 요구사항을 Backend Agent와 Review Agent에게 전달하기 전에 반드시 확인해야 하는 최종 검수 기준이다.

```text
User Request
→ PM Classification
→ Execution Gate
→ Backend Task / Review Task
```

---

### [핵심]

- 요구사항이 단순 CRUD인지 확인한다.
- 외부 시스템 연동 여부를 확인한다.
- 정책 교체 가능성을 확인한다.
- 이벤트 후속 처리 여부를 확인한다.
- 비동기, 재시도, 실패 처리 여부를 확인한다.
- Domain Rule 위치를 확인한다.
- Over Engineering 위험을 명시한다.

---

### [Checklist]

PM Agent Gate:

- 요구사항을 기능 단위로 분리했는가?
- 단순 CRUD인지 복잡 Domain인지 구분했는가?
- 외부 API, DB, Message Broker, AI Provider가 있는가?
- 정책이나 알고리즘이 교체될 가능성이 있는가?
- 후속 작업이 직접 호출로 결합될 위험이 있는가?
- 재시도, Timeout, Rate Limit, 장애 처리가 필요한가?
- Domain Rule이 명확한가?
- Backend Agent 작업 지시가 구체적인가?
- Review Agent 검수 포인트가 포함되었는가?
- Pattern 과적용 금지 조건이 포함되었는가?

---

### [FAQ]

Q. PM Agent Execution Gate는 무엇인가?

A. PM Agent가 요구사항을 구현 지시로 넘기기 전 설계 위험과 Pattern 후보를 최종 확인하는 기준이다.

Q. PM Agent는 무엇을 반드시 포함해야 하는가?

A. 기능 분류, 설계 위험, Pattern 후보, Backend Agent 지시, Review Agent 검수, Over Engineering 주의를 포함해야 한다.

Q. PM Agent는 Pattern을 확정해야 하는가?

A. 아니다. Pattern 후보와 검수 기준을 전달하고 구현과 Review에서 확정하게 한다.

Q. PM Agent가 가장 주의할 점은?

A. 단순 요구사항에 과도한 Pattern을 강제하지 않는 것이다.

---

## 7.2 Backend Agent Execution Gate

### [개념]

Backend Agent Execution Gate는 Backend Agent가 코드를 생성하거나 수정하기 전에 Pattern 적용 여부와 구조 적합성을 검수하는 기준이다.

```text
Backend Task
→ Design Decision
→ Execution Gate
→ Code Generation
```

---

### [핵심]

- 단순 구조가 가능한지 먼저 확인한다.
- Pattern 적용 이유가 명확해야 한다.
- 외부 DTO가 내부로 침투하지 않아야 한다.
- Service 책임이 과도하지 않아야 한다.
- Transaction Boundary가 명확해야 한다.
- Event, Retry, Proxy 제약을 고려해야 한다.
- 코드 생성 후 Review Agent 검수 포인트를 남겨야 한다.

---

### [Checklist]

Backend Agent Gate:

- Layered Architecture로 충분한가?
- Pattern 적용 이유를 설명할 수 있는가?
- Factory가 생성 또는 선택 책임만 가지는가?
- Builder 사용 시 필수값 검증이 있는가?
- Strategy가 실제 정책 교체 문제를 해결하는가?
- Adapter가 외부 DTO를 내부 Result로 변환하는가?
- Event Listener 실패 처리와 Transaction Phase가 고려되었는가?
- Command Retry에 Idempotency가 있는가?
- `@Transactional` Self Invocation 문제가 없는가?
- Entity에 무분별한 Setter가 없는가?
- Controller가 Repository를 직접 호출하지 않는가?
- Review Agent가 검수할 구조가 명확한가?

---

### [FAQ]

Q. Backend Agent Execution Gate는 무엇인가?

A. Backend Agent가 코드 생성 전 Pattern 적용 여부와 구조 적합성을 검수하는 기준이다.

Q. Backend Agent는 무엇을 먼저 확인해야 하는가?

A. 단순 구조로 충분한지와 Pattern 적용 이유가 명확한지를 먼저 확인해야 한다.

Q. Backend Agent가 외부 API를 사용할 때 필수 검수는?

A. 외부 DTO 격리, Adapter 분리, 예외 변환, Timeout, Retry 필요성을 검수해야 한다.

Q. Backend Agent가 Pattern을 적용하지 않아야 하는 경우는?

A. 현재 문제가 단순하고 변경 가능성이 낮으며 Pattern 비용이 더 클 때이다.

---

## 7.3 Review Agent Execution Gate

### [개념]

Review Agent Execution Gate는 Review Agent가 코드 검수 결과를 출력하기 전에 누락 없이 확인해야 하는 최종 검수 기준이다.

```text
Code Review
→ Issue Detection
→ Execution Gate
→ Final Review Output
```

---

### [핵심]

- 문제를 명확히 설명해야 한다.
- 원인을 SOLID, Pattern, Architecture 기준으로 연결해야 한다.
- 해결책은 구체적이어야 한다.
- 관련 Pattern과 Trade-off를 포함해야 한다.
- Pattern 추가와 Pattern 제거를 모두 검토해야 한다.
- 최종 판단은 적용 권장, 단순 구조 유지, Pattern 제거 권장 중 하나로 명확히 한다.

---

### [Checklist]

Review Agent Gate:

- 문제 위치가 명확한가?
- 문제 원인이 설명되었는가?
- 관련 SOLID 원칙이 있는가?
- 관련 Pattern이 있는가?
- Architecture 위반이 있는가?
- Over Engineering 가능성이 있는가?
- 해결책이 단계별로 구체적인가?
- 적용 Trade-off가 포함되었는가?
- Pattern 적용 보류 가능성을 검토했는가?
- 최종 판단이 명확한가?

---

### [Final Review Format]

```text
[Design Pattern Review]

문제:
...

원인:
...

관련 원칙:
...

관련 Pattern:
...

해결:
1. ...
2. ...
3. ...

Trade-off:
...

최종 판단:
적용 권장 / 단순 구조 유지 / Pattern 제거 권장
```

---

### [FAQ]

Q. Review Agent Execution Gate는 무엇인가?

A. Review Agent가 최종 검수 결과를 출력하기 전에 문제, 원인, 해결, Trade-off를 누락 없이 확인하는 기준이다.

Q. Review Agent는 최종 판단을 어떻게 작성해야 하는가?

A. 적용 권장, 단순 구조 유지, Pattern 제거 권장 중 하나로 명확히 작성해야 한다.

Q. Review Agent는 Over Engineering도 검수해야 하는가?

A. 그렇다. Pattern 누락뿐 아니라 Pattern 남용도 반드시 검수해야 한다.

Q. Review Agent 결과에 Trade-off가 필요한 이유는?

A. Pattern 적용은 항상 비용이 있으므로 현재 문제에서 이점이 비용보다 큰지 판단해야 하기 때문이다.

---

# Retrieval Queries

### [FAQ]

Q. Design Pattern Final Index는 무엇인가?
A. Design Pattern RAG 문서 세트 전체를 Agent가 빠르게 검색하고 연결하기 위한 최종 색인 문서이다.

Q. Final Index는 사람용 목차인가?
A. 아니다. Agent Retrieval Routing과 Pattern Decision을 위한 검색 허브이다.

Q. Pattern 상세 설명은 어디서 찾는가?
A. 각 Pattern이 포함된 Part02, Part03, Part04, Part05 문서에서 찾는다.

Q. Pattern 적용 여부가 애매하면 어디를 검색하는가?
A. Part07 Pattern Selection과 Pattern Anti-Decision을 우선 검색한다.

Q. Query Intent Routing은 무엇인가?
A. 사용자 질문이나 Agent 내부 질문을 의도별로 분류해 적절한 RAG 문서로 연결하는 규칙이다.

Q. 검수 질문은 어디를 우선 검색하는가?
A. Part06 Review & Troubleshooting을 우선 검색한다.

Q. 구현 질문은 어디를 우선 검색하는가?
A. 관련 Pattern Part와 Part07 Pattern Selection을 함께 검색한다.

Q. Architecture 질문은 어디를 우선 검색하는가?
A. Part05 Architecture Patterns와 Part06 Troubleshooting을 함께 검색한다.

Q. Pattern Name Routing은 무엇인가?
A. 특정 Pattern 이름이 언급되었을 때 상세 문서, 검수 문서, 선택 문서로 연결하는 규칙이다.

Q. 사용자가 Strategy를 언급하면 바로 Strategy를 적용하는가?
A. 아니다. Part04와 Part07을 검색한 뒤 실제 문제가 알고리즘 교체인지 검토한다.

Q. 사용자가 Adapter를 언급하면 어디를 검색하는가?
A. Part03 Adapter, Part06 Adapter Troubleshooting, Part07 Structural Selection을 검색한다.

Q. 사용자가 Clean Architecture를 언급하면 어디를 검색하는가?
A. Part05 Clean Architecture, Part06 Domain Leakage, Part07 Architecture Selection을 검색한다.

Q. PM Agent는 Design Pattern 문서를 어떻게 사용하는가?
A. 요구사항을 설계 문제로 분류하고 Pattern 후보와 검수 포인트를 다른 Agent에게 전달한다.

Q. PM Agent는 어느 문서를 우선 검색하는가?
A. Part07 Pattern Selection과 PM Agent Workflow를 우선 검색한다.

Q. PM Agent가 외부 시스템 연동을 발견하면?
A. Adapter, Port, Timeout, Retry, 예외 변환, 외부 DTO 격리를 지시한다.

Q. PM Agent가 단순 CRUD를 발견하면?
A. Layered Architecture 기반 단순 구현을 지시하고 과도한 Pattern 적용을 금지한다.

Q. Backend Agent는 Design Pattern 문서를 어떻게 사용하는가?
A. 요구사항 구현 전 Pattern 후보를 검색하고 코드 생성 후 자체 검수에 사용한다.

Q. Backend Agent의 기본 구조는?
A. 단순 기능은 Layered Architecture를 기본으로 한다.

Q. Backend Agent는 외부 API를 어떻게 처리해야 하는가?
A. External API Adapter로 감싸고 외부 DTO를 내부 Result로 변환해야 한다.

Q. Backend Agent는 언제 Pattern 적용을 보류해야 하는가?
A. 변경 가능성이 낮고 단순 구조가 더 명확할 때 보류해야 한다.

Q. Review Agent는 어느 문서를 우선 검색하는가?
A. Part06 Review & Troubleshooting을 우선 검색한다.

Q. Review Agent는 Pattern 제거를 제안할 수 있는가?
A. 그렇다. 불필요한 추상화나 Pattern은 제거를 제안해야 한다.

Q. Review Agent는 어떤 형식으로 답변하는가?
A. 문제, 원인, 관련 원칙, 관련 Pattern, 해결, Trade-off, 최종 판단 형식이 적합하다.

Q. RAG Document Quality Gate는 무엇인가?
A. RAG 문서가 Agent 검색, 코드 생성, 검수에 적합한지 최종 검수하는 기준이다.

Q. Quality Gate에서 가장 중요한 항목은?
A. Retrieval Quality, FAQ 품질, Troubleshooting 품질, Agent Usability이다.

Q. RAG 문서에 FAQ가 왜 중요한가?
A. 사용자 질문과 Agent Query가 FAQ 형태로 검색될 가능성이 높기 때문이다.

Q. RAG 문서가 실패하는 대표 원인은?
A. 장문 설명, FAQ 부족, Pattern 적용 기준 부족, Troubleshooting 부족이다.

Q. Design Pattern Quality Criteria는 무엇인가?
A. Design Pattern RAG 문서 품질을 구조, 검색성, 기술 정확성, Troubleshooting, Agent 활용성 기준으로 평가하는 기준이다.

Q. 가장 중요한 품질 기준은?
A. Retrieval Optimization, Troubleshooting, Agent Usability이다.

Q. 가장 위험한 품질 문제는?
A. FAQ 부족, Retrieval Queries 없음, Troubleshooting 부족, Pattern 적용 기준 부족이다.

Q. 품질 기준을 통과하면 바로 충분한가?
A. 아니다. 실제 Agent Retrieval Test와 문서 간 연계 검수가 필요하다.

Q. Naming Consistency가 중요한 이유는?
A. 용어가 일관되어야 RAG 검색과 Agent 판단이 안정적으로 동작하기 때문이다.

Q. Pattern 이름은 한글로 번역해야 하는가?
A. 문서에서는 영어 Pattern 이름을 유지하고 필요 시 한글 설명을 덧붙인다.

Q. Command와 Event는 왜 구분해야 하는가?
A. Command는 앞으로 수행할 요청이고 Event는 이미 발생한 사실이기 때문이다.

Q. Port와 Adapter는 왜 구분해야 하는가?
A. Port는 내부 Interface이고 Adapter는 외부 기술 구현체이기 때문이다.

Q. Cross-Part Link Consistency는 무엇인가?
A. Design Pattern 문서 각 Part가 서로 충돌하지 않고 같은 판단 기준으로 연결되도록 검수하는 규칙이다.

Q. SOLID 판단은 어느 문서를 기준으로 하는가?
A. Part01 Core & SOLID를 기준으로 한다.

Q. Troubleshooting 판단은 어느 문서를 기준으로 하는가?
A. Part06 Review & Troubleshooting을 기준으로 한다.

Q. Pattern Selection 판단은 어느 문서를 기준으로 하는가?
A. Part07 Pattern Selection & Agent Workflow를 기준으로 한다.

Q. Retrieval Test Query는 무엇인가?
A. RAG 업로드 후 문서 검색 품질을 확인하기 위한 테스트 질문이다.

Q. 업로드 후 무엇을 확인해야 하는가?
A. 질문별로 기대한 Part 문서가 검색되는지 확인해야 한다.

Q. Part08만 계속 검색되면 어떻게 하는가?
A. Part08을 별도 Collection으로 분리하거나 검색 우선순위를 낮춘다.

Q. 검색 결과가 부정확하면 어떻게 하는가?
A. 해당 Part의 FAQ, Retrieval Queries, 핵심 키워드를 보강한다.

Q. Design Pattern 문서 중 어떤 파일을 업로드하는가?
A. Part01부터 Part08까지 업로드한다.

Q. Completion Report는 업로드하는가?
A. 업로드하지 않는다. 보관용 문서로만 유지한다.

Q. Part08은 업로드해야 하는가?
A. 기본적으로 업로드 가능하다. 다만 검색 노이즈가 발생하면 별도 Collection으로 분리한다.

Q. 검색 노이즈가 발생하면 무엇을 조정하는가?
A. Part08 분리, Chunk 설정, Top-K, FAQ 보강, 문서 우선순위를 조정한다.

Q. PM Agent Execution Gate는 무엇인가?
A. PM Agent가 요구사항을 구현 지시로 넘기기 전 설계 위험과 Pattern 후보를 최종 확인하는 기준이다.

Q. PM Agent는 무엇을 반드시 포함해야 하는가?
A. 기능 분류, 설계 위험, Pattern 후보, Backend Agent 지시, Review Agent 검수, Over Engineering 주의를 포함해야 한다.

Q. Backend Agent Execution Gate는 무엇인가?
A. Backend Agent가 코드 생성 전 Pattern 적용 여부와 구조 적합성을 검수하는 기준이다.

Q. Backend Agent는 무엇을 먼저 확인해야 하는가?
A. 단순 구조로 충분한지와 Pattern 적용 이유가 명확한지를 먼저 확인해야 한다.

Q. Review Agent Execution Gate는 무엇인가?
A. Review Agent가 최종 검수 결과를 출력하기 전에 문제, 원인, 해결, Trade-off를 누락 없이 확인하는 기준이다.

Q. Review Agent는 최종 판단을 어떻게 작성해야 하는가?
A. 적용 권장, 단순 구조 유지, Pattern 제거 권장 중 하나로 명확히 작성해야 한다.

Q. Design Pattern Part08의 목적은?
A. Design Pattern 문서 세트를 검색 라우팅하고 품질 검수와 업로드 후 검색 테스트 기준을 제공하는 것이다.

Q. Part08이 Pattern 상세 설명을 대체하는가?
A. 아니다. Part08은 Routing과 Quality Gate 문서이고 상세 설명은 Part02~Part05를 참조해야 한다.

Q. Design Pattern 문서의 최종 목적은?
A. Agent가 Design Pattern을 적절히 적용하고 잘못된 구조를 검수하며 Over Engineering을 피하도록 지원하는 것이다.
