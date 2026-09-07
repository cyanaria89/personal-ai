# Advanced Spring Architecture Domain Rules

---

# 1. Domain Purpose

Advanced Spring Architecture Domain 문서는 Backend Expert Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- Spring Backend Architecture 개선
- 대규모 Spring Application 구조 설계
- Layered Architecture 고도화
- Hexagonal Architecture / Clean Architecture 적용 판단
- Transaction Boundary 검토
- Package Structure 개선
- Domain 중심 구조 설계
- Refactoring / Review 기준 제공

우선순위:

1. Maintainable Architecture
2. Clear Dependency Direction
3. Transaction Boundary
4. Domain Isolation
5. Testability
6. Scalability

---

# 2. Scope

포함 범위:

- Advanced Spring Architecture
- Layered Architecture
- Package Structure
- Domain 중심 설계
- Application Service
- Domain Service
- Facade
- Transaction Boundary
- DTO Boundary
- Entity Boundary
- Repository Boundary
- Event 기반 Spring 구조
- Spring Application Event
- Spring Modulith
- Hexagonal Architecture
- Clean Architecture
- Dependency Rule
- Architecture Refactoring
- Architecture Troubleshooting

제외 범위:

- Spring Boot 기초 문법
- Controller / Service / Repository 기본 CRUD
- JPA 기초 매핑
- Security 인증/인가 상세
- Kubernetes / CI/CD / 운영 인프라 상세

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

# 4. Architecture Core Rules

Advanced Spring Architecture 문서는 단순 코드 작성법이 아니라 구조 판단 기준 중심으로 작성한다.

반드시 포함:

- 왜 이 구조가 필요한가
- 어떤 문제를 해결하는가
- 언제 적용하는가
- 적용하지 않아도 되는 경우
- 남용 시 문제점
- Spring 프로젝트에서의 실제 적용 방식

핵심 구조:

```text
Problem
→ Architecture Decision
→ Dependency Direction
→ Implementation Structure
→ Review
```

금지:

- 단순 Layer 설명만 반복
- 무조건 Hexagonal Architecture 권장
- 무조건 Clean Architecture 권장
- 과도한 추상화 권장
- 실무 적용 기준 없는 이론 설명

---

# 5. Layered Architecture Rules

Layered Architecture는 Spring Backend 기본 구조로 설명한다.

필수 포함:

- Controller Layer
- Service Layer
- Repository Layer
- Domain / Entity Layer
- DTO Layer
- Infrastructure Layer

기본 Flow:

```text
Request
→ Controller
→ Application Service
→ Domain / Entity
→ Repository
→ Database
→ Response
```

반드시 설명:

- Controller는 HTTP 요청/응답 처리
- Service는 Use Case 흐름 조정
- Repository는 Persistence 접근
- Entity는 Domain 상태와 핵심 행위 보유
- DTO는 외부 입출력 경계

주의:

- Controller에 비즈니스 로직 금지
- Repository에 비즈니스 로직 금지
- Entity를 Response로 직접 반환 금지
- Service가 모든 책임을 독점하는 God Service 금지

---

# 6. Package Structure Rules

Package Structure 문서는 Agent가 프로젝트 구조를 제안할 수 있도록 작성한다.

필수 비교:

- Layer Based Package
- Domain Based Package
- Feature Based Package
- Hexagonal Package

예시:

```text
layer-based
├ controller
├ service
├ repository
└ entity
```

```text
domain-based
├ user
│  ├ controller
│  ├ service
│  ├ repository
│  └ entity
├ order
└ payment
```

반드시 설명:

- 작은 프로젝트는 Layer Based 가능
- 중대형 프로젝트는 Domain Based 선호
- 기능 경계가 명확하면 Feature Based 가능
- 복잡한 외부 연동이 많으면 Hexagonal 구조 고려

Best Practice:

- Domain 단위 응집도 우선
- 변경이 함께 일어나는 코드는 가까이 배치
- 공통 패키지 남용 금지
- util / common에 비즈니스 로직 숨기기 금지

---

# 7. Dependency Direction Rules

의존성 방향은 매우 중요하다.

필수 포함:

- 상위 정책은 하위 구현에 직접 의존하지 않음
- Domain은 Infrastructure에 의존하지 않음
- Application Service는 Use Case를 조정
- Infrastructure는 외부 시스템 연동 담당

권장 방향:

```text
Controller
→ Application Service
→ Domain
→ Repository Interface
← Repository Implementation
```

Hexagonal / Clean Architecture 기준:

```text
External
→ Adapter
→ Application Port
→ Domain
```

주의:

- Domain이 Controller DTO에 의존 금지
- Domain이 JPA Repository에 직접 의존 금지
- Application Service가 외부 API Client 구현체에 강하게 결합되는 것 주의
- 순환 참조 금지

---

# 8. Application Service Rules

Application Service는 Use Case 흐름을 담당한다.

필수 포함:

- Transaction Boundary
- Use Case Orchestration
- DTO 변환
- Repository 호출
- Domain Method 호출
- 외부 시스템 연동 조정

예시 Flow:

```text
Request DTO
→ Application Service
→ Entity 조회
→ Domain Method 실행
→ Repository 저장
→ Response DTO 반환
```

반드시 설명:

- Application Service는 비즈니스 흐름을 조정한다
- 핵심 비즈니스 규칙은 Domain / Entity / Domain Service로 이동 가능
- Application Service가 너무 커지면 Use Case 단위 분리 고려

주의:

- 모든 로직을 Service에 몰아넣는 Anemic Domain 주의
- 하나의 Service가 여러 Domain 책임을 모두 담당하지 않도록 주의
- 트랜잭션 범위를 불필요하게 크게 잡지 말 것

---

# 9. Domain Service Rules

Domain Service는 Entity 하나에 넣기 어려운 Domain 규칙을 담당한다.

필수 포함:

- 여러 Entity가 함께 필요한 Domain Logic
- 특정 Entity 소유로 보기 어려운 계산/정책
- Infrastructure 의존 없는 순수 Domain Logic

예시:

```text
Order
+ Coupon
+ UserGrade
→ DiscountPolicyDomainService
```

반드시 설명:

- Domain Service는 Domain 규칙을 표현한다
- Application Service와 다르다
- 외부 API 호출, DB 접근은 Domain Service에 넣지 않는다

주의:

- Domain Service 남용 금지
- 단순 CRUD를 Domain Service로 분리하지 말 것
- Application Service와 역할 혼동 금지

---

# 10. Facade Rules

Facade는 복잡한 여러 Service 호출을 단순화할 때 사용한다.

필수 포함:

- 복수 Domain Service 조합
- 복수 Application Service 조합
- 외부에 단순한 진입점 제공
- 복잡한 Use Case 조정

예시 Flow:

```text
Controller
→ OrderFacade
→ OrderService
→ PaymentService
→ NotificationService
```

반드시 설명:

- Facade는 복잡도 숨김
- Facade는 책임 분산을 위한 보조 구조
- Facade가 God Object가 되면 안 됨

주의:

- 모든 Controller 앞에 Facade를 두는 방식 금지
- 단순 CRUD에 Facade 사용 금지
- 트랜잭션 경계가 모호해지지 않도록 주의

---

# 11. Transaction Boundary Rules

Transaction Boundary는 매우 중요하다.

필수 포함:

- `@Transactional`
- Read Only Transaction
- Write Transaction
- Transaction Propagation
- Lazy Loading
- Dirty Checking
- External API 호출과 Transaction 분리

기본 규칙:

```text
Controller
→ Transactional Service Method
→ Repository
→ Commit / Rollback
```

Best Practice:

- 쓰기 작업은 Service 계층에서 Transaction 시작
- 조회 작업은 `readOnly = true` 고려
- 외부 API 호출은 DB Transaction 안에 오래 묶지 않음
- Transaction 범위는 Use Case 단위로 설정
- 비동기 이벤트는 Transaction Commit 이후 처리 고려

주의:

- Controller에 `@Transactional` 남용 금지
- Repository 각각에만 Transaction 분산 금지
- 긴 Transaction으로 Connection Pool 고갈 주의
- Transaction 안에서 느린 외부 API 호출 금지

---

# 12. DTO Boundary Rules

DTO Boundary는 계층 간 결합도를 낮추기 위해 중요하다.

필수 포함:

- Request DTO
- Response DTO
- Service Command DTO
- Query DTO
- Entity 변환 기준

규칙:

- Controller는 Request / Response DTO 사용
- Entity를 API Response로 직접 반환 금지
- Domain은 Controller DTO에 의존하지 않음
- Service 내부용 Command 객체 분리 가능

예시:

```text
Request DTO
→ Command
→ Application Service
→ Domain
→ Response DTO
```

주의:

- DTO가 너무 많아지는 경우 Use Case 단위로 정리
- Entity와 DTO 양방향 변환 남용 금지
- Mapper가 복잡한 비즈니스 로직을 가지지 않도록 주의

---

# 13. Entity Boundary Rules

Entity는 DB Table 매핑 객체이면서 Domain 상태를 표현한다.

필수 포함:

- Entity State
- Domain Method
- Invariant
- Association
- Lazy Loading
- Persistence Context

권장:

- 상태 변경은 Entity Method로 표현
- Setter 남용 금지
- 생성 규칙은 생성자 / 정적 팩토리 / Builder로 관리
- 연관관계 편의 메서드 사용
- 불변 조건은 Entity 내부에서 보호

주의:

- Entity에 외부 API 호출 금지
- Entity에 Repository 주입 금지
- Entity를 Response DTO처럼 사용 금지
- 모든 로직을 Entity에 넣는 것도 금지

---

# 14. Repository Boundary Rules

Repository는 Persistence 접근 경계이다.

필수 포함:

- Spring Data JPA Repository
- Custom Repository
- QueryDSL Repository
- Repository Interface
- Persistence Adapter

규칙:

- Repository는 조회/저장 책임
- 복잡한 Query는 Custom Repository / QueryDSL 사용
- 비즈니스 정책 판단은 Service / Domain으로 이동
- Query 최적화는 Performance Tuning 문서와 연결

주의:

- Repository Method 이름이 과도하게 길어지는 경우 QueryDSL 고려
- Repository에서 DTO 조립과 비즈니스 판단을 동시에 하지 말 것
- Controller가 Repository를 직접 호출하지 않도록 주의

---

# 15. Spring Event Rules

Spring Event는 모듈 간 결합도를 낮출 때 사용한다.

필수 포함:

- ApplicationEventPublisher
- Event
- EventListener
- TransactionalEventListener
- AFTER_COMMIT
- 비동기 이벤트 처리

기본 Flow:

```text
Service
→ Publish Event
→ Transaction Commit
→ Event Listener
→ Side Effect Processing
```

적합한 예:

- 알림 발송
- 이메일 발송
- 로그 기록
- 통계 적재
- 외부 시스템 연동
- 후처리 작업

주의:

- 핵심 트랜잭션 성공 전에 실행되면 안 되는 작업은 AFTER_COMMIT 고려
- Event Listener에서 예외 발생 시 영향 범위 확인
- Event 남용 시 흐름 추적이 어려워짐
- 순서가 중요한 핵심 로직을 이벤트로 숨기지 말 것

---

# 16. Spring Modulith Rules

Spring Modulith는 모듈 경계를 명확히 하기 위한 Spring 기반 구조로 설명한다.

필수 포함:

- Module Boundary
- Application Module
- Published Event
- Module Dependency
- Modulith Test

적합한 경우:

- Monolith 유지
- Domain 경계 명확화
- MSA 전환 전 단계
- 모듈 간 의존성 검증 필요

Flow:

```text
Modular Monolith
→ Module Boundary
→ Event-based Communication
→ Dependency Verification
```

주의:

- 작은 프로젝트에 무리하게 적용하지 말 것
- 패키지 구조가 먼저 정리되어야 함
- 모듈 경계 없이 도입하면 효과 낮음

---

# 17. Hexagonal Architecture Rules

Hexagonal Architecture는 외부 시스템과 Domain을 분리할 때 사용한다.

필수 포함:

- Port
- Adapter
- Inbound Adapter
- Outbound Adapter
- Application Port
- Infrastructure Adapter
- Domain Isolation

기본 Flow:

```text
HTTP Request
→ Inbound Adapter
→ Application Port
→ Domain
→ Outbound Port
→ Outbound Adapter
→ External System
```

적합한 경우:

- 외부 API 연동이 많음
- DB / Message Queue / 외부 시스템 교체 가능성이 있음
- 테스트 용이성이 중요함
- Domain 중심 구조가 필요함

주의:

- 단순 CRUD 프로젝트에 과도한 Hexagonal Architecture 금지
- Port / Adapter를 만들기 위한 추상화 금지
- Interface가 실제 교체 가능성을 표현해야 함

---

# 18. Clean Architecture Rules

Clean Architecture는 의존성 방향과 Domain 보호를 중심으로 설명한다.

필수 포함:

- Dependency Rule
- Entity
- Use Case
- Interface Adapter
- Framework & Driver
- Domain Isolation

의존성 규칙:

```text
Framework
→ Adapter
→ Use Case
→ Entity / Domain
```

반드시 설명:

- 안쪽 계층은 바깥 계층을 모른다
- Domain은 Framework에 의존하지 않는다
- Use Case는 Application의 의도를 표현한다
- Framework는 세부 구현이다

주의:

- Clean Architecture를 패키지 이름만으로 흉내 내지 말 것
- 작은 프로젝트에 과도한 계층 분리 금지
- Use Case가 단순 CRUD Wrapper가 되지 않도록 주의

---

# 19. Architecture Decision Rules

Architecture 문서는 선택 기준을 반드시 포함한다.

필수 비교:

| 상황                           | 추천 구조                         |
| ------------------------------ | --------------------------------- |
| 작은 CRUD 프로젝트             | Layered Architecture              |
| 중형 도메인 중심 프로젝트      | Domain Based Layered Architecture |
| 외부 연동이 많음               | Hexagonal Architecture            |
| 장기적으로 복잡도 증가 예상    | Clean Architecture 일부 적용      |
| 모놀리식 유지 + 모듈 경계 필요 | Spring Modulith                   |
| 서비스 분리 필요               | MSA                               |

주의:

- 아키텍처는 유행이 아니라 문제 해결 기준으로 선택
- 복잡도보다 유지보수성이 우선
- 현재 팀 역량과 프로젝트 규모 고려
- 도입 비용과 장기 이점 비교

---

# 20. Refactoring Rules

Architecture Refactoring 문서는 기존 구조를 점진적으로 개선하는 흐름을 포함한다.

기본 Flow:

```text
Current Structure Analysis
→ Responsibility Split
→ Dependency Direction Fix
→ Package Reorganization
→ Transaction Boundary Check
→ Test Coverage
→ Incremental Refactoring
```

대상:

- God Service
- Fat Controller
- Anemic Domain
- Circular Dependency
- Common Package Abuse
- DTO / Entity Boundary Violation
- Transaction Boundary Violation
- Infrastructure Coupling

주의:

- 한 번에 전체 구조 변경 금지
- 테스트 없이 구조 변경 금지
- 기능 변경과 구조 변경을 동시에 크게 진행하지 말 것

---

# 21. Testing Rules

Advanced Spring Architecture 문서는 테스트 가능성을 반드시 고려한다.

필수 포함:

- Unit Test
- Slice Test
- Integration Test
- Architecture Test
- Transaction Test
- Event Test

권장:

- Domain Logic은 Unit Test
- Repository Query는 DataJpaTest
- Controller는 MockMvc
- Service는 Integration Test 또는 Mockito
- Architecture Rule은 ArchUnit 고려
- Event Listener는 Transaction Commit 이후 동작 검증

주의:

- 테스트하기 어려운 구조는 설계 문제일 가능성 높음
- Static Utility 남용은 테스트를 어렵게 함
- 외부 시스템 강결합은 Mocking을 어렵게 함

---

# 22. Troubleshooting Rules

반드시 포함 추천.

형식:

```md
문제:

원인:

해결:
```

자주 발생하는 문제:

## Fat Controller

문제:

- Controller에 비즈니스 로직이 많음

원인:

- Service 책임 분리 부족

해결:

- Controller는 요청 검증과 응답 위임만 담당
- Use Case는 Application Service로 이동

---

## God Service

문제:

- 하나의 Service가 모든 Domain 책임을 가짐

원인:

- Domain 경계 미정의
- Use Case 분리 부족

해결:

- Use Case 단위 Service 분리
- Domain Service / Facade 도입 검토

---

## Transaction Boundary Violation

문제:

- 트랜잭션 범위가 너무 넓거나 좁음

원인:

- 외부 API 호출과 DB 작업이 하나의 Transaction에 묶임
- Repository 단위로 Transaction이 흩어짐

해결:

- Service Use Case 단위 Transaction 설정
- 외부 API 호출은 Transaction 밖으로 분리 검토
- 이벤트 후처리 고려

---

## Circular Dependency

문제:

- Bean 순환 참조 발생

원인:

- Service 간 상호 호출
- Domain 경계 불명확

해결:

- 의존 방향 재정의
- Facade / Event / Domain Service로 흐름 분리

---

## Over Engineering

문제:

- 단순 기능에 과도한 계층과 Interface 사용

원인:

- 패턴/아키텍처를 목적 없이 적용

해결:

- 현재 복잡도 기준으로 구조 선택
- 교체 가능성 없는 Interface 제거
- 단순 CRUD는 Layered Architecture 유지

---

# 23. Best Practice Rules

반드시 포함 추천.

Best Practice:

- 작은 프로젝트는 단순하게 시작
- Domain이 커지면 Domain Based Package로 전환
- Service는 Use Case 중심으로 분리
- Entity는 상태 변경 메서드를 가질 수 있음
- DTO와 Entity 경계 유지
- Transaction은 Service Use Case 단위로 관리
- 외부 시스템 연동은 Adapter / Client로 분리
- 이벤트는 후처리와 결합도 감소에 사용
- 테스트하기 쉬운 구조를 우선
- Architecture 변경은 점진적으로 수행

---

# 24. Comparison Rules

Architecture 비교 문서는 반드시 실무 판단 기준을 포함한다.

필수 비교 대상:

- Layered Architecture vs Hexagonal Architecture
- Layered Architecture vs Clean Architecture
- Domain Service vs Application Service
- Facade vs Service
- DTO vs Entity
- Event vs Direct Call
- Domain Based Package vs Layer Based Package

예시:

| 비교 | Layered Architecture     | Hexagonal Architecture     |
| ---- | ------------------------ | -------------------------- |
| 목적 | 단순 계층 분리           | Domain과 외부 시스템 분리  |
| 장점 | 이해 쉬움                | 테스트/교체 용이           |
| 단점 | 계층 결합 증가 가능      | 구조 복잡도 증가           |
| 적합 | 일반 CRUD, 중소형 서비스 | 외부 연동 많고 Domain 중요 |

---

# 25. Retrieval Optimization Rules

강조 대상 키워드:

- Advanced Spring Architecture
- Layered Architecture
- Domain Based Package
- Application Service
- Domain Service
- Facade
- Transaction Boundary
- DTO Boundary
- Entity Boundary
- Repository Boundary
- Spring Event
- TransactionalEventListener
- Spring Modulith
- Hexagonal Architecture
- Clean Architecture
- Dependency Rule
- Port
- Adapter
- Use Case
- Domain Isolation
- Architecture Refactoring
- God Service
- Fat Controller
- Circular Dependency
- Over Engineering

키워드 반복 허용.

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- Spring 프로젝트 구조 어떻게 나눠?
- Service가 너무 커졌을 때 어떻게 분리해?
- Hexagonal Architecture 언제 써?
- Clean Architecture 꼭 써야 해?
- Transaction은 어디에 걸어야 해?
- DTO랑 Entity 분리해야 해?
- Facade는 언제 써?
- Spring Event는 언제 써?

---

# 26. Version Rules

기준:

- Java 21
- Spring Boot 3.x
- Spring Framework 6.x
- Spring Data JPA
- QueryDSL
- Modern Backend Architecture
- Modular Monolith
- MSA 전환 가능 구조

Legacy 제외:

- Spring XML 설정 중심 구조
- 구형 Servlet/JSP 중심 구조
- Spring Boot 1.x / 2.x 전용 방식
- EJB 중심 구조

---

# 27. Common Mistakes

자주 발생:

- Layer만 나누고 책임은 분리하지 않음
- Controller에 비즈니스 로직 작성
- Service가 모든 로직을 독점
- Entity는 Getter/Setter만 가진 데이터 객체로만 사용
- DTO와 Entity 경계 없음
- Repository에 비즈니스 판단 로직 작성
- Transaction 범위가 불명확
- 외부 API 호출을 긴 Transaction 안에서 수행
- Event로 핵심 흐름을 숨김
- Interface를 이유 없이 과도하게 생성
- Hexagonal Architecture를 모든 프로젝트에 강제
- Clean Architecture를 패키지 이름만으로 적용
- common / util 패키지에 핵심 로직 숨김
- 테스트 불가능한 구조로 설계

---

# 28. Final Goal

Advanced Spring Architecture RAG 문서는 Agent가 아래를 수행 가능해야 한다.

- Spring Backend 구조 설계
- Package Structure 제안
- Service 책임 분리
- Transaction Boundary 검토
- DTO / Entity Boundary 검토
- Domain 중심 구조 개선
- Hexagonal Architecture 적용 여부 판단
- Clean Architecture 적용 여부 판단
- Spring Event 적용 여부 판단
- God Service / Fat Controller 개선
- Architecture Review
- Refactoring Direction 제안

문서 품질이 Backend Architecture 품질을 결정한다.

---

# Retrieval Queries

### [FAQ]

Q. Spring 프로젝트 구조는 어떻게 나눠야 해?

A.
작은 프로젝트는 Layered Architecture로 시작하고, 도메인이 커지면 Domain Based Package로 분리한다.

Q. Layered Architecture는 언제 적합해?

A.
일반적인 CRUD 중심 서비스나 중소형 Spring 프로젝트에 적합하다.

Q. Domain Based Package는 언제 써?

A.
도메인별 변경이 많아지고 기능 경계가 명확해질 때 사용한다.

Q. Service가 너무 커졌을 때 어떻게 분리해?

A.
Use Case 단위로 Application Service를 나누고, 여러 Entity 규칙은 Domain Service로 분리한다.

Q. Application Service와 Domain Service 차이는?

A.
Application Service는 Use Case 흐름을 조정하고, Domain Service는 특정 Entity 하나에 넣기 어려운 Domain 규칙을 담당한다.

Q. Facade는 언제 써?

A.
여러 Service나 Domain 흐름을 조합해야 하는 복잡한 Use Case에서 단순한 진입점을 제공할 때 사용한다.

Q. Transaction은 어디에 걸어야 해?

A.
일반적으로 Service 계층의 Use Case 단위 메서드에 적용한다.

Q. Transaction 안에서 외부 API를 호출해도 돼?

A.
권장하지 않는다. 외부 API 지연이 DB Connection과 Lock 점유 시간을 늘릴 수 있으므로 분리하는 것이 좋다.

Q. DTO와 Entity는 분리해야 해?

A.
API Request / Response에서는 DTO를 사용하고 Entity를 직접 노출하지 않는 것이 좋다.

Q. Entity에 비즈니스 로직을 넣어도 돼?

A.
상태 변경이나 불변 조건을 지키는 Domain Method는 Entity에 둘 수 있다. 단, 외부 API 호출이나 Repository 의존은 넣지 않는다.

Q. Repository에는 어떤 로직을 넣어야 해?

A.
Repository는 조회와 저장 책임을 담당하고, 비즈니스 정책 판단은 Service나 Domain으로 분리한다.

Q. Spring Event는 언제 써?

A.
알림, 이메일, 로그, 통계 적재처럼 핵심 트랜잭션 이후 처리해도 되는 후처리에 적합하다.

Q. TransactionalEventListener는 언제 써?

A.
DB Transaction Commit 이후 이벤트를 처리해야 할 때 사용한다.

Q. Hexagonal Architecture는 언제 써?

A.
외부 API, DB, 메시지 큐 등 외부 시스템 교체 가능성이 크거나 Domain 보호가 중요할 때 사용한다.

Q. Clean Architecture는 꼭 써야 해?

A.
아니다. 단순 CRUD 프로젝트에는 과할 수 있고, 복잡한 Domain과 장기 유지보수가 필요할 때 일부 적용한다.

Q. Spring Modulith는 언제 고려해?

A.
Monolith를 유지하면서 Domain Module 경계를 명확히 하고, MSA 전환 전 단계 구조를 만들고 싶을 때 고려한다.

Q. God Service는 어떻게 개선해?

A.
Use Case 단위로 Service를 분리하고, Domain 규칙은 Entity나 Domain Service로 이동하며, 복잡한 조합은 Facade로 정리한다.

Q. Fat Controller는 어떻게 개선해?

A.
Controller는 요청 검증과 응답 위임만 담당하고, 비즈니스 흐름은 Application Service로 이동한다.

Q. Circular Dependency는 어떻게 해결해?

A.
의존 방향을 재정의하고, 필요하면 Facade, Event, Domain Service로 흐름을 분리한다.

Q. Over Engineering은 어떻게 피해야 해?

A.
프로젝트 규모와 복잡도를 기준으로 구조를 선택하고, 교체 가능성이 없는 Interface나 불필요한 계층을 만들지 않는다.
