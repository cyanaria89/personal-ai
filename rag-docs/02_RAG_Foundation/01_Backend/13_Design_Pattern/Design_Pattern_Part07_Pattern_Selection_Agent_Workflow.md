# Design Pattern Part07 - Pattern Selection & Agent Workflow

---

# 1. Pattern Selection Overview

## 1.1 Pattern Selection

### [개념]

Pattern Selection은 요구사항, 코드 구조, 변경 지점, 의존성 문제를 분석하여 적절한 Design Pattern을 선택하는 과정이다.

Pattern Selection은 Pattern 이름을 외워 적용하는 과정이 아니다.

Pattern Selection은 현재 문제가 생성 문제, 구조 문제, 행동 문제, 아키텍처 문제 중 어디에 속하는지 분류하는 과정이다.

```text
Requirement / Code Smell
→ Problem Classification
→ Pattern Candidate
→ Trade-off Review
→ Apply or Keep Simple
```

---

### [핵심]

- Pattern Selection은 문제 분류가 먼저이다.
- Pattern은 코드 구조의 문제를 해결하기 위한 선택지이다.
- Pattern 적용 전 변경 가능성을 확인한다.
- Pattern 적용 전 현재 코드가 단순 구조로 충분한지 확인한다.
- Pattern 적용 후 책임 분리, 테스트 용이성, 확장성이 좋아져야 한다.
- Pattern 적용 후 코드가 더 복잡해지기만 하면 잘못된 선택일 수 있다.
- Pattern을 적용하지 않는 것도 유효한 설계 선택이다.

---

### [실무]

2026 실무 기준 Java 21, Spring Boot 3.x Backend에서 Pattern Selection은 다음 질문으로 시작한다.

```text
1. 이 문제는 객체 생성 문제인가?
2. 이 문제는 객체 관계와 구조 문제인가?
3. 이 문제는 객체 행동과 책임 흐름 문제인가?
4. 이 문제는 시스템 구조와 의존성 방향 문제인가?
5. 이 문제는 단순 CRUD로 해결 가능한가?
6. 이 문제는 반복 변경 가능성이 높은가?
7. 이 문제는 외부 시스템 변경에 영향을 받는가?
8. 이 문제는 테스트 격리가 필요한가?
9. 이 문제는 비동기, 재시도, 실패 처리가 필요한가?
10. Pattern 적용 비용보다 이점이 큰가?
```

---

### [주의]

- Pattern Selection은 “좋아 보이는 Pattern”을 고르는 과정이 아니다.
- Pattern Selection은 문제를 줄이는 방향이어야 한다.
- 모든 조건문은 Strategy 대상이 아니다.
- 모든 외부 호출은 Port 대상이 아니다.
- 모든 객체 생성은 Factory 대상이 아니다.
- 모든 DTO 생성은 Builder 대상이 아니다.
- 모든 후속 작업은 Event 대상이 아니다.

---

### [FAQ]

Q. Pattern Selection은 무엇인가?

A. 요구사항과 코드 문제를 분석해 적절한 Design Pattern 또는 단순 구조를 선택하는 과정이다.

Q. Pattern Selection에서 가장 먼저 해야 할 일은?

A. 문제가 생성, 구조, 행동, 아키텍처 문제 중 어디에 속하는지 분류하는 것이다.

Q. Pattern을 적용하지 않는 것도 좋은 선택인가?

A. 그렇다. 단순한 문제에는 단순한 구조가 더 좋은 설계일 수 있다.

Q. Pattern Selection의 핵심 기준은?

A. 변경 가능성, 책임 분리, 테스트 용이성, 의존성 방향, 적용 비용이다.

---

## 1.2 Problem Classification

### [개념]

Problem Classification은 현재 설계 문제가 어떤 유형인지 분류하는 과정이다.

Design Pattern은 문제 유형별로 다르게 선택한다.

```text
Problem
→ Creational Problem
→ Structural Problem
→ Behavioral Problem
→ Architecture Problem
```

---

### [핵심]

- 객체 생성 책임 문제는 Creational Pattern 후보이다.
- 객체 관계와 호환성 문제는 Structural Pattern 후보이다.
- 객체 행동과 흐름 문제는 Behavioral Pattern 후보이다.
- 시스템 계층과 의존성 문제는 Architecture Pattern 후보이다.
- SOLID 위반은 Pattern 후보를 찾는 중요한 신호이다.
- Over Engineering 위험도 함께 분류한다.

---

### [실무]

| 문제 유형      | 대표 신호                                | 우선 검토 Pattern                    |
| -------------- | ---------------------------------------- | ------------------------------------ |
| 생성 문제      | 생성자 복잡, 객체 선택 조건 증가         | Factory, Builder, Singleton          |
| 구조 문제      | 외부 API 불일치, 접근 제어, 기능 확장    | Adapter, Decorator, Proxy            |
| 행동 문제      | 정책 교체, 이벤트 후속 처리, 요청 재시도 | Strategy, Observer, Command          |
| 공통 흐름 문제 | 처리 순서 반복, 일부 단계만 다름         | Template Method                      |
| 계층 문제      | Controller 비대, Service 비대            | Layered Review, Facade               |
| 의존성 문제    | 외부 Client 직접 의존                    | DIP, Port, Adapter                   |
| Domain 문제    | Domain Rule 분산                         | Domain Isolation, Clean Architecture |
| 과설계 문제    | Interface, Port, Adapter 과다            | Simplification, Pattern Removal      |

---

### [예제]

```text
문제:
PaymentService에 if / switch로 결제 타입별 로직이 계속 증가한다.

분류:
행동 문제 + 정책 교체 문제

후보:
Strategy Pattern + Factory Pattern
```

```text
문제:
FestivalService가 Tour API Response DTO를 직접 사용한다.

분류:
구조 문제 + 외부 시스템 결합 문제

후보:
Adapter Pattern + Port
```

```text
문제:
단순 회원 목록 조회에 UseCase, Port, Adapter가 모두 분리되어 있다.

분류:
과설계 문제

후보:
Layered Architecture 단순화
```

---

### [주의]

- 하나의 문제에 여러 Pattern 후보가 있을 수 있다.
- 문제 분류가 틀리면 Wrong Pattern Choice가 발생한다.
- 문제 유형보다 Pattern 이름을 먼저 떠올리면 과설계로 이어질 수 있다.
- Pattern 후보는 반드시 Trade-off와 함께 검토한다.

---

### [FAQ]

Q. Problem Classification은 무엇인가?

A. 현재 설계 문제가 생성, 구조, 행동, 아키텍처, 과설계 중 어디에 속하는지 분류하는 과정이다.

Q. 객체 생성 문제가 있으면 어떤 Pattern을 검토하는가?

A. Factory, Builder, Singleton 같은 Creational Pattern을 검토한다.

Q. 외부 API 구조가 내부와 다르면 어떤 Pattern을 검토하는가?

A. Adapter Pattern과 Port 분리를 검토한다.

Q. 정책이 계속 추가되면 어떤 Pattern을 검토하는가?

A. Strategy Pattern과 Factory Pattern을 검토한다.

---

# 2. Pattern Selection Matrix

## 2.1 Creational Pattern Selection

### [개념]

Creational Pattern Selection은 객체 생성 책임, 생성 조건, 생성 복잡도, 인스턴스 공유 필요성을 기준으로 Singleton, Factory, Builder를 선택하는 과정이다.

```text
Object Creation Problem
→ Instance Control / Creation Responsibility / Complex Creation
→ Singleton / Factory / Builder
```

---

### [핵심]

- 인스턴스 하나만 유지해야 하면 Singleton 또는 Spring Bean을 검토한다.
- 요청 타입별 객체 선택이 필요하면 Factory를 검토한다.
- 생성자 파라미터가 많으면 Builder를 검토한다.
- DTO 변환은 Static Factory Method를 검토한다.
- Spring 환경에서는 직접 Singleton 구현보다 Bean Scope을 우선 사용한다.
- 생성 책임이 단순하면 Pattern을 적용하지 않는다.

---

### [실무]

| 문제 상황                          | Pattern 후보            | 적용 기준             |
| ---------------------------------- | ----------------------- | --------------------- |
| Service Bean 하나를 재사용         | Singleton / Spring Bean | Stateless Bean        |
| 결제 타입별 Processor 선택         | Factory                 | 구현체 선택 조건 존재 |
| 알림 채널별 Sender 선택            | Factory + Strategy      | 채널 추가 가능        |
| DTO 필드가 많고 선택 필드가 있음   | Builder                 | 생성자 가독성 저하    |
| Entity에서 DTO 변환                | Static Factory Method   | `from()` 사용         |
| 여러 값을 받아 Value Object 생성   | Static Factory Method   | `of()` 사용           |
| 생성자 파라미터가 1~2개            | 생성자 유지             | Pattern 불필요        |
| 구현체 하나뿐이고 교체 가능성 낮음 | 직접 생성 또는 DI       | Factory 불필요        |

---

### [예제]

```text
요구사항:
알림 채널이 EMAIL, SMS, PUSH로 늘어날 수 있다.

분류:
객체 선택 조건 + 정책 확장

선택:
NotificationSenderFactory + NotificationSender Strategy
```

```text
요구사항:
FestivalResponse 필드가 15개이고 선택 값이 많다.

분류:
복잡한 객체 생성

선택:
Builder Pattern 또는 Static Factory Method + Builder
```

---

### [주의]

- Factory는 생성 책임과 선택 책임만 가진다.
- Builder는 필수값 검증을 자동 보장하지 않는다.
- Singleton Bean은 Stateless로 설계한다.
- 단순 DTO에 Builder를 강제하지 않는다.
- 모든 객체 생성에 Factory를 만들지 않는다.

---

### [FAQ]

Q. Factory는 언제 선택하는가?

A. 요청 타입이나 조건에 따라 다른 객체를 생성하거나 선택해야 할 때 선택한다.

Q. Builder는 언제 선택하는가?

A. 생성자 파라미터가 많거나 선택 필드가 많아 객체 생성 가독성이 떨어질 때 선택한다.

Q. Singleton은 언제 선택하는가?

A. 하나의 인스턴스를 공유해야 할 때 선택하지만 Spring Boot에서는 기본적으로 Spring Bean을 우선 사용한다.

Q. Static Factory Method는 언제 선택하는가?

A. 생성자보다 의미 있는 이름으로 객체 생성 의도를 표현하고 싶을 때 선택한다.

---

## 2.2 Structural Pattern Selection

### [개념]

Structural Pattern Selection은 객체 관계, 인터페이스 호환성, 기능 확장, 접근 제어 문제를 기준으로 Adapter, Decorator, Proxy를 선택하는 과정이다.

```text
Structure Problem
→ Compatibility / Extension / Access Control
→ Adapter / Decorator / Proxy
```

---

### [핵심]

- 인터페이스가 맞지 않으면 Adapter를 검토한다.
- 기존 기능 전후에 부가기능을 추가하면 Decorator를 검토한다.
- 실제 객체 접근을 제어해야 하면 Proxy를 검토한다.
- 복잡한 하위 시스템을 단순화하면 Facade를 검토한다.
- 트리 구조를 다루면 Composite를 검토한다.
- 외부 시스템과 내부 Use Case 경계에는 Adapter가 중요하다.

---

### [실무]

| 문제 상황                                | Pattern 후보             | 적용 기준               |
| ---------------------------------------- | ------------------------ | ----------------------- |
| 외부 API Response가 내부 모델과 다름     | Adapter                  | 외부 DTO 격리           |
| Legacy Interface를 내부 Interface에 맞춤 | Adapter                  | Interface Compatibility |
| 기존 기능에 Logging, Metrics 추가        | Decorator / AOP          | 부가기능 확장           |
| HTTP 요청 전후 Security 처리             | Filter Chain / Decorator | 요청 흐름 확장          |
| Transaction 처리                         | Proxy                    | Method 접근 제어        |
| JPA Lazy Loading                         | Proxy                    | 실제 접근 시점 제어     |
| 복잡한 SDK를 단순 API로 감쌈             | Facade                   | 하위 시스템 단순화      |
| 카테고리, 댓글, 메뉴 트리                | Composite                | Tree Structure          |

---

### [예제]

```text
요구사항:
Kakao Map API 응답을 내부 LocationResult로 변환한다.

분류:
외부 인터페이스 호환성 문제

선택:
KakaoMapAdapter implements LocationPort
```

```text
요구사항:
Service 실행 시간을 공통으로 측정한다.

분류:
부가기능 확장 문제

선택:
AOP 또는 Decorator
```

```text
문제:
@Transactional이 같은 Class 내부 호출에서 동작하지 않는다.

분류:
Proxy 동작 이해 문제

선택:
Proxy Troubleshooting
```

---

### [주의]

- Adapter는 인터페이스 변환이 목적이다.
- Decorator는 기능 확장이 목적이다.
- Proxy는 접근 제어가 목적이다.
- 비슷한 Wrapper 구조라도 목적이 다르면 Pattern이 다르다.
- 외부 API DTO를 내부 Service로 넘기지 않는다.

---

### [FAQ]

Q. Adapter는 언제 선택하는가?

A. 외부 API, Legacy System, SDK를 내부 Interface에 맞게 변환해야 할 때 선택한다.

Q. Decorator는 언제 선택하는가?

A. 기존 객체 기능 전후에 로깅, 캐싱, 검증, 보안 같은 부가기능을 추가할 때 선택한다.

Q. Proxy는 언제 선택하는가?

A. 접근 제어, 지연 로딩, Transaction, Security, AOP 같은 대리 호출이 필요할 때 선택한다.

Q. Adapter, Decorator, Proxy 차이는?

A. Adapter는 인터페이스 변환, Decorator는 기능 확장, Proxy는 접근 제어가 목적이다.

---

## 2.3 Behavioral Pattern Selection

### [개념]

Behavioral Pattern Selection은 객체 행동, 책임 흐름, 이벤트 전달, 요청 처리 문제를 기준으로 Strategy, Observer, Template Method, Command를 선택하는 과정이다.

```text
Behavior Problem
→ Algorithm / Event / Flow / Request
→ Strategy / Observer / Template Method / Command
```

---

### [핵심]

- 알고리즘 또는 정책이 교체되면 Strategy를 검토한다.
- 이벤트 후속 작업이 많으면 Observer를 검토한다.
- 공통 흐름은 같고 일부 단계만 다르면 Template Method를 검토한다.
- 요청을 저장, 전달, 재시도해야 하면 Command를 검토한다.
- 여러 Handler가 순차 처리하면 Chain of Responsibility를 검토한다.
- 객체 간 상호작용이 복잡하면 Mediator를 검토한다.

---

### [실무]

| 문제 상황                            | Pattern 후보            | 적용 기준             |
| ------------------------------------ | ----------------------- | --------------------- |
| 결제 수단별 처리 방식 다름           | Strategy                | 알고리즘 교체         |
| 할인 정책이 계속 추가됨              | Strategy + Factory      | OCP 개선              |
| 주문 완료 후 알림, 포인트, 로그 처리 | Observer                | 후속 작업 분리        |
| 채팅 메시지 생성 후 AI 요약          | Observer / Event        | 비동기 후보           |
| 공공 API 동기화 흐름 반복            | Template Method         | Skeleton Flow         |
| 알림 발송 실패 재시도                | Command Queue           | 요청 저장 + 재시도    |
| 여러 검증기 순차 실행                | Chain of Responsibility | 순서 기반 Handler     |
| Multi-Agent 순차 조정                | Mediator                | Workflow Coordination |

---

### [예제]

```text
요구사항:
추천 알고리즘을 인기순, 거리순, 사용자 취향 기반으로 교체한다.

분류:
알고리즘 교체 문제

선택:
RecommendationStrategy + StrategyFactory
```

```text
요구사항:
회원 가입 완료 후 이메일과 앱 알림을 보낸다.

분류:
이벤트 후속 처리 문제

선택:
UserRegisteredEvent + Event Listener
```

```text
요구사항:
알림 발송 실패 시 최대 3회 재시도한다.

분류:
요청 저장 + 재시도 문제

선택:
SendNotificationCommand + Command Queue
```

---

### [주의]

- Strategy는 조건문 제거가 목적이 아니라 변경 지점 분리가 목적이다.
- Observer는 흐름 가시성이 낮아질 수 있다.
- Template Method는 상속 구조가 경직될 수 있다.
- Command Retry는 멱등성이 필수이다.
- Event와 Command는 의미가 다르다.

---

### [FAQ]

Q. Strategy는 언제 선택하는가?

A. 알고리즘, 정책, 처리 방식이 여러 개이고 추가 가능성이 높을 때 선택한다.

Q. Observer는 언제 선택하는가?

A. 하나의 이벤트 후 여러 후속 작업이 필요하고 직접 결합을 줄이고 싶을 때 선택한다.

Q. Template Method는 언제 선택하는가?

A. 여러 기능의 공통 처리 흐름은 같고 일부 단계만 다를 때 선택한다.

Q. Command는 언제 선택하는가?

A. 요청을 객체로 저장, 전달, 재시도, 큐 처리해야 할 때 선택한다.

---

## 2.4 Architecture Pattern Selection

### [개념]

Architecture Pattern Selection은 시스템 규모, Domain 복잡도, 외부 의존성, 유지보수 기간을 기준으로 Layered Architecture, Hexagonal Architecture, Clean Architecture를 선택하는 과정이다.

```text
System Context
→ Complexity / External Dependency / Domain Rule
→ Layered / Hexagonal / Clean
```

---

### [핵심]

- 단순 CRUD는 Layered Architecture를 우선 선택한다.
- 외부 시스템 교체 가능성이 높으면 Hexagonal Architecture를 검토한다.
- Domain Rule 보호가 중요하면 Clean Architecture를 검토한다.
- Architecture Pattern은 전체 적용보다 부분 적용이 현실적일 수 있다.
- 의존성 방향과 책임 분리가 핵심이다.
- 과도한 계층 분리는 Over Engineering이 될 수 있다.

---

### [실무]

| 상황                              | Architecture 후보              | 적용 기준                     |
| --------------------------------- | ------------------------------ | ----------------------------- |
| 학습용 / 단순 CRUD                | Layered Architecture           | 빠른 구현, 낮은 복잡도        |
| 일반 Spring Boot API              | Layered Architecture           | Controller-Service-Repository |
| 외부 API 연동 많음                | Hexagonal Architecture         | Port / Adapter                |
| 결제, 알림, 파일 저장소 교체 가능 | Hexagonal Architecture         | Outbound Port                 |
| 복잡한 Domain Rule                | Clean Architecture             | Domain Isolation              |
| 장기 유지보수 시스템              | Clean / Hexagonal              | Dependency Rule               |
| 단순 조회 API                     | Layered 유지                   | 과설계 방지                   |
| Multi-Agent Workflow              | Mediator + Architecture Review | Agent 간 결합 방지            |

---

### [예제]

```text
요구사항:
단순 게시글 목록 조회 API를 만든다.

분류:
단순 CRUD

선택:
Layered Architecture
주의:
Port, Adapter 과도 적용 금지
```

```text
요구사항:
AI Provider를 OpenAI, Local LLM, Claude로 교체 가능하게 한다.

분류:
외부 Provider 교체 가능성

선택:
AiSummaryPort + OpenAiAdapter + LocalLlmAdapter
```

```text
요구사항:
주문 Domain의 상태 전이와 결제 규칙이 복잡하다.

분류:
Domain Rule 보호 필요

선택:
Domain Model, Domain Service, Clean Architecture 원칙 부분 적용
```

---

### [주의]

- Architecture Pattern은 프로젝트 전체에 일괄 적용하지 않아도 된다.
- 단순 기능에는 단순 구조를 유지한다.
- 핵심 Domain과 외부 연동 영역부터 구조를 강화한다.
- Package 구조보다 의존성 방향이 중요하다.
- 팀 이해도와 Agent 생성 가능성도 고려한다.

---

### [FAQ]

Q. Layered Architecture는 언제 선택하는가?

A. 단순 CRUD, 일반 Spring Boot API, 빠른 구현이 필요한 경우 선택한다.

Q. Hexagonal Architecture는 언제 선택하는가?

A. 외부 API, 결제, 알림, 파일 저장소처럼 교체 가능성이 높은 외부 의존성이 있을 때 선택한다.

Q. Clean Architecture는 언제 선택하는가?

A. Domain Rule이 복잡하고 장기 유지보수와 테스트 격리가 중요한 경우 선택한다.

Q. Architecture Pattern을 섞어도 되는가?

A. 가능하다. 실무에서는 Layered 기반에 Adapter, Port, Domain Isolation을 부분 적용하는 경우가 많다.

---

# 3. Agent Workflow

## 3.1 PM Agent Workflow

### [개념]

PM Agent Workflow는 사용자 요구사항을 기능 요구, 설계 문제, Pattern 후보, Agent 작업 지시로 변환하는 흐름이다.

PM Agent는 직접 구현하지 않고 Backend Agent와 Review Agent가 작업할 수 있도록 요구사항을 구조화한다.

```text
User Request
→ Requirement Analysis
→ Design Problem Classification
→ Pattern Candidate
→ Backend Agent Task
→ Review Agent Checklist
```

---

### [핵심]

- PM Agent는 요구사항의 변경 가능성을 식별한다.
- PM Agent는 외부 시스템 연동 여부를 식별한다.
- PM Agent는 정책 교체 가능성을 식별한다.
- PM Agent는 이벤트 후속 작업을 식별한다.
- PM Agent는 비동기, 재시도, 실패 처리 요구를 식별한다.
- PM Agent는 단순 CRUD에 과설계를 금지한다.
- PM Agent는 Pattern을 확정하기보다 후보와 검수 포인트를 전달한다.

---

### [실무]

PM Agent 요구사항 분석 Template:

```text
요구사항:
...

기능 분류:
단순 CRUD / 외부 연동 / 정책 교체 / 이벤트 후속 처리 / 비동기 작업 / Domain Rule

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

### [예제]

```text
요구사항:
축제 채팅 메시지를 저장한 뒤 AI 요약 후보를 생성한다.

기능 분류:
이벤트 후속 처리 + AI 외부 의존성

Pattern 후보:
Observer Pattern, Adapter Pattern, Port

Backend Agent 지시:
ChatMessageCreatedEvent를 발행하고 AI 요약 처리는 Listener로 분리한다.
AI Provider는 AiSummaryPort와 Adapter로 격리한다.

Review Agent 검수:
Event Flow Hidden Problem, Adapter 외부 DTO 침투, Retry 필요성, Over Engineering 여부를 검수한다.

Over Engineering 주의:
AI Provider가 하나이고 교체 계획이 없다면 Port 적용 범위를 최소화한다.
```

---

### [주의]

- PM Agent는 Pattern을 강제하지 않는다.
- PM Agent는 요구사항의 설계 위험을 명확히 전달한다.
- PM Agent는 단순 기능과 복잡 기능을 구분한다.
- PM Agent는 Agent 간 역할이 겹치지 않게 한다.
- PM Agent는 구현 상세보다 판단 기준을 제공한다.

---

### [FAQ]

Q. PM Agent Workflow는 무엇인가?

A. 사용자 요구사항을 설계 문제와 Pattern 후보로 분류하고 Backend Agent와 Review Agent에게 작업 지시를 전달하는 흐름이다.

Q. PM Agent는 Pattern을 확정해야 하는가?

A. 아니다. Pattern 후보와 검수 포인트를 제시하고 구현과 검수 단계에서 확정하게 한다.

Q. PM Agent가 단순 CRUD를 발견하면?

A. Layered Architecture 기반 단순 구현을 지시하고 과도한 Pattern 적용을 금지한다.

Q. PM Agent가 외부 시스템 연동을 발견하면?

A. Adapter, Port, Timeout, Retry, 예외 변환, 외부 DTO 격리를 검토 지시한다.

---

## 3.2 Backend Agent Workflow

### [개념]

Backend Agent Workflow는 PM Agent가 분류한 요구사항을 기반으로 실제 Spring Boot Backend 코드 구조를 설계하고 구현하는 흐름이다.

Backend Agent는 가장 단순한 구조를 우선하고 변경 가능성이 확인된 지점에 Pattern을 적용한다.

```text
Agent Task
→ Use Case Design
→ Pattern Decision
→ Code Generation
→ Self Review
→ Output
```

---

### [핵심]

- Backend Agent는 Layered Architecture를 기본값으로 사용한다.
- Backend Agent는 외부 시스템 연동에 Adapter를 검토한다.
- Backend Agent는 정책 교체 가능성에 Strategy를 검토한다.
- Backend Agent는 객체 선택 조건에 Factory를 검토한다.
- Backend Agent는 후속 작업 분리에 Event를 검토한다.
- Backend Agent는 재시도와 큐 처리에 Command를 검토한다.
- Backend Agent는 Entity 상태 변경을 의미 있는 Method로 캡슐화한다.
- Backend Agent는 Pattern 남용을 피한다.

---

### [실무]

Backend Agent 구현 순서:

```text
1. Controller / Request / Response 필요 여부 확인
2. Use Case Service 책임 정의
3. Repository / Query 필요 여부 확인
4. Domain Rule 위치 결정
5. 외부 시스템 연동 여부 확인
6. Pattern 적용 여부 결정
7. Transaction Boundary 설정
8. Exception 처리 설계
9. Test 가능 구조 확인
10. Review Agent 검수 포인트 정리
```

---

### [예제]

```text
요구사항:
결제 수단별 결제 처리 구현

Backend Agent 판단:
- 결제 수단별 알고리즘 교체 가능
- 외부 결제 Provider 존재
- 결제 타입별 구현체 선택 필요

구조:
PaymentService
→ PaymentProcessorFactory
→ PaymentProcessor Strategy
→ TossPaymentAdapter / CardPaymentAdapter

주의:
단순 결제 타입 1개만 있으면 Strategy 구조를 보류한다.
```

---

### [주의]

- Backend Agent는 모든 Service에 Interface를 만들지 않는다.
- Backend Agent는 외부 DTO를 Application Service에 노출하지 않는다.
- Backend Agent는 Builder 사용 시 필수값 검증을 포함한다.
- Backend Agent는 Singleton Bean에 요청별 상태를 저장하지 않는다.
- Backend Agent는 `@Transactional` Self Invocation을 피한다.
- Backend Agent는 Event Listener 실패 처리와 Transaction Phase를 고려한다.

---

### [FAQ]

Q. Backend Agent Workflow는 무엇인가?

A. 요구사항을 코드 구조로 변환하고 필요한 경우 Pattern을 적용해 Spring Boot Backend 코드를 생성하는 흐름이다.

Q. Backend Agent의 기본 Architecture는?

A. 단순 기능은 Layered Architecture를 기본으로 사용한다.

Q. Backend Agent는 언제 Adapter를 적용하는가?

A. 외부 API, 결제, 알림, 파일 저장소 등 외부 기술을 내부 Use Case와 분리해야 할 때 적용한다.

Q. Backend Agent는 언제 Pattern 적용을 보류해야 하는가?

A. 변경 가능성이 낮고 단순 구조가 더 명확할 때 Pattern 적용을 보류한다.

---

## 3.3 Review Agent Workflow

### [개념]

Review Agent Workflow는 Backend Agent가 생성한 코드와 구조를 Design Pattern, SOLID, Architecture, Troubleshooting 기준으로 검수하는 흐름이다.

Review Agent는 Pattern 적용 부족과 Pattern 남용을 모두 검수한다.

```text
Generated Code
→ SOLID Review
→ Pattern Fit Review
→ Architecture Review
→ Troubleshooting Review
→ Refactoring Proposal
```

---

### [핵심]

- Review Agent는 먼저 문제를 식별한다.
- Review Agent는 원인을 SOLID와 Pattern 기준으로 분석한다.
- Review Agent는 적절한 Pattern 후보를 제안한다.
- Review Agent는 Pattern 적용 Trade-off를 명시한다.
- Review Agent는 Over Engineering이면 단순화를 제안한다.
- Review Agent는 구체적인 Refactoring 단위를 제시한다.
- Review Agent는 최종 판단을 명확히 한다.

---

### [실무]

Review Agent 검수 순서:

```text
1. Layer Responsibility 위반 확인
2. SRP / OCP / DIP 위반 확인
3. 외부 DTO 침투 확인
4. 외부 Client 직접 의존 확인
5. Strategy / Factory 과도화 확인
6. Builder 필수값 검증 확인
7. Singleton Stateful Field 확인
8. Event Flow와 Transaction Phase 확인
9. Command Retry 멱등성 확인
10. Proxy Self Invocation 확인
11. Domain Rule 분산 확인
12. Over Engineering 확인
```

---

### [Review Output Template]

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

### [예제]

```text
문제:
FestivalService가 TourApiResponse를 직접 사용한다.

원인:
Application Service가 외부 API DTO에 의존한다.
외부 API 변경이 내부 비즈니스 코드로 전파될 수 있다.

관련 원칙:
DIP, SRP

관련 Pattern:
Adapter Pattern, Hexagonal Architecture

해결:
FestivalExternalPort를 정의하고 TourApiFestivalAdapter가 구현하게 한다.
TourApiResponse는 Adapter 내부에서 ExternalFestivalResult로 변환한다.

Trade-off:
외부 API가 하나뿐이고 단순하면 Adapter 계층이 추가 비용이 될 수 있다.

최종 판단:
외부 API 스펙 변경 가능성이 있으므로 Adapter 적용 권장
```

---

### [주의]

- Review Agent는 무조건 Pattern을 추가하지 않는다.
- Review Agent는 단순화도 적극 제안한다.
- Review Agent는 코드 규모와 요구사항 복잡도를 고려한다.
- Review Agent는 Pattern 이름보다 문제 해결 효과를 우선한다.
- Review Agent는 추상적인 조언보다 구체적인 이동, 분리, 제거 대상을 제시한다.

---

### [FAQ]

Q. Review Agent Workflow는 무엇인가?

A. 생성된 코드와 구조를 SOLID, Design Pattern, Architecture 기준으로 검수하고 개선안을 제안하는 흐름이다.

Q. Review Agent는 무엇을 우선 검수하는가?

A. 책임 분리, 의존성 방향, 외부 DTO 침투, Pattern 적합성, Over Engineering을 우선 검수한다.

Q. Review Agent는 Pattern 제거를 제안할 수 있는가?

A. 그렇다. 불필요한 Pattern은 제거하는 것이 더 좋은 Refactoring일 수 있다.

Q. Review Agent 결과는 어떤 형식이 좋은가?

A. 문제, 원인, 관련 원칙, 관련 Pattern, 해결, Trade-off, 최종 판단 형식이 좋다.

---

# 4. Pattern Decision Playbook

## 4.1 If-Then Pattern Decision

### [개념]

If-Then Pattern Decision은 Agent가 요구사항이나 코드 문제를 빠르게 Pattern 후보로 연결하기 위한 Retrieval 최적화 규칙이다.

이 규칙은 Pattern 적용을 확정하지 않고 후보를 빠르게 찾는 데 사용한다.

```text
If Problem Signal
→ Then Pattern Candidate
→ Review Trade-off
```

---

### [핵심]

- If-Then 규칙은 Retrieval Hit를 높인다.
- If-Then 규칙은 Pattern 후보를 빠르게 좁힌다.
- If-Then 규칙은 최종 설계 판단을 대체하지 않는다.
- If-Then 이후 반드시 Trade-off를 검토한다.
- 단순 구조 유지 가능성을 항상 함께 확인한다.

---

### [실무]

```text
If 생성자 파라미터가 많다
Then Builder Pattern 검토
```

```text
If 객체 타입별 생성 조건이 많다
Then Factory Pattern 검토
```

```text
If 정책 또는 알고리즘이 계속 추가된다
Then Strategy Pattern 검토
```

```text
If 외부 API Response DTO가 Service에 들어온다
Then Adapter Pattern 검토
```

```text
If 실제 객체 접근 전후에 부가기능이 필요하다
Then Proxy 또는 Decorator 검토
```

```text
If 이벤트 발생 후 후속 작업이 여러 개다
Then Observer Pattern 또는 Spring Event 검토
```

```text
If 요청을 저장하고 재시도해야 한다
Then Command Pattern 또는 Command Queue 검토
```

```text
If 처리 흐름은 같고 일부 단계만 다르다
Then Template Method Pattern 검토
```

```text
If 외부 시스템 교체 가능성이 높다
Then Port / Adapter / Hexagonal Architecture 검토
```

```text
If Domain Rule이 Controller, Service, DTO에 흩어져 있다
Then Domain Isolation / Clean Architecture 검토
```

```text
If 구현체가 하나뿐이고 변경 가능성이 낮다
Then Interface 제거 또는 단순 구조 유지 검토
```

---

### [주의]

- If-Then 규칙은 자동 적용 규칙이 아니다.
- 단순 문제에는 Pattern 적용을 보류한다.
- Pattern 후보가 여러 개면 가장 단순한 구조를 우선한다.
- Pattern 적용 후 테스트와 변경 용이성이 좋아져야 한다.
- Agent는 If-Then 결과를 Review Agent에게 검수시킨다.

---

### [FAQ]

Q. If-Then Pattern Decision은 무엇인가?

A. 문제 신호를 Pattern 후보로 빠르게 연결하기 위한 Agent용 판단 규칙이다.

Q. If-Then 규칙은 Pattern 적용을 확정하는가?

A. 아니다. 후보를 찾는 규칙이며 Trade-off 검토 후 적용 여부를 결정한다.

Q. If 외부 API DTO가 Service에 들어오면 Then 무엇을 검토하는가?

A. Adapter Pattern, Port, Hexagonal Architecture를 검토한다.

Q. If 구현체가 하나뿐이고 변경 가능성이 낮으면 Then 무엇을 검토하는가?

A. Interface 제거 또는 단순 구조 유지를 검토한다.

---

## 4.2 Pattern Anti-Decision

### [개념]

Pattern Anti-Decision은 Pattern을 적용하지 말아야 하는 상황을 명확히 정의하는 규칙이다.

Pattern Anti-Decision은 Over Engineering을 방지하기 위한 Agent 판단 기준이다.

```text
Pattern Candidate
→ Complexity Check
→ Low Value
→ Do Not Apply
```

---

### [핵심]

- Pattern은 필요할 때만 적용한다.
- Pattern 적용 이유가 설명되지 않으면 적용하지 않는다.
- 구현체가 하나뿐이고 교체 가능성이 낮으면 Interface를 생략할 수 있다.
- 단순 CRUD는 Layered Architecture로 충분할 수 있다.
- 단순 객체 생성은 Factory가 필요하지 않을 수 있다.
- 단순 DTO는 Builder가 필요하지 않을 수 있다.

---

### [실무]

Pattern 적용 보류 기준:

| 상황                               | 보류 대상                    |
| ---------------------------------- | ---------------------------- |
| 구현체 하나, 교체 가능성 낮음      | Interface / Strategy         |
| 생성자 파라미터 1~2개              | Builder                      |
| 단순 Value Object 생성             | Factory                      |
| 단순 CRUD 조회                     | Hexagonal Port / Adapter     |
| 후속 작업 1개, 실패 영향 직접 필요 | Event 분리                   |
| 공통 흐름이 안정적이지 않음        | Template Method              |
| 요청 재시도 필요 없음              | Command Queue                |
| 외부 API가 내부에 거의 영향 없음   | 과도한 Port                  |
| 팀이 구조를 이해하기 어려움        | Clean Architecture 전체 적용 |

---

### [예제]

```text
상황:
UserService 구현체가 하나뿐이고 교체 가능성이 없다.

판단:
UserService Interface와 UserServiceImpl 구조는 생략 가능하다.

이유:
추상화 이점보다 파일 수와 탐색 비용이 더 크다.
```

```text
상황:
공지사항 단순 목록 조회 API이다.

판단:
Controller-Service-Repository 구조 유지.

이유:
Port, UseCase, Adapter 분리는 과도하다.
```

---

### [주의]

- Pattern Anti-Decision은 무조건 단순화를 의미하지 않는다.
- 변경 가능성이 높아지는 순간 Pattern 적용을 재검토한다.
- 보류 사유는 문서화하는 것이 좋다.
- 단순 구조도 책임 분리는 지켜야 한다.
- 단순화와 무질서한 코드는 다르다.

---

### [FAQ]

Q. Pattern Anti-Decision은 무엇인가?

A. Pattern을 적용하지 않는 것이 더 좋은 상황을 정의하는 판단 기준이다.

Q. Pattern 적용을 보류하는 대표 상황은?

A. 구현체가 하나뿐이고 변경 가능성이 낮거나 단순 CRUD처럼 구조 비용이 더 큰 경우이다.

Q. 단순 구조 유지도 설계 판단인가?

A. 그렇다. 현재 문제에 가장 적합한 최소 구조를 선택하는 것도 설계이다.

Q. Pattern 적용을 보류했다가 나중에 적용해도 되는가?

A. 가능하다. 변경 압력이 실제로 생겼을 때 점진적으로 적용하는 것이 안전하다.

---

# 5. Cross-Document Retrieval Map

## 5.1 Design Pattern Document Map

### [개념]

Design Pattern Document Map은 Design Pattern RAG 문서들이 어떤 역할을 가지며 어떤 Agent가 어떤 문서를 우선 참조해야 하는지 정의하는 Retrieval Map이다.

```text
Agent Query
→ Document Part
→ Relevant Section
→ Pattern Decision
```

---

### [핵심]

- Part01은 Design Pattern Core와 SOLID 기준이다.
- Part02는 Creational Pattern 기준이다.
- Part03은 Structural Pattern 기준이다.
- Part04는 Behavioral Pattern 기준이다.
- Part05는 Architecture Pattern 기준이다.
- Part06은 Review와 Troubleshooting 기준이다.
- Part07은 Pattern Selection과 Agent Workflow 기준이다.
- Agent는 질문 유형에 따라 우선 검색 문서를 선택해야 한다.

---

### [실무]

| 문서                            | 주요 역할                                    | 우선 사용 Agent                       |
| ------------------------------- | -------------------------------------------- | ------------------------------------- |
| Part01 Core & SOLID             | 설계 원칙, 책임, 의존성 기준                 | Backend Agent, Review Agent           |
| Part02 Creational               | 객체 생성, Factory, Builder, Singleton       | Backend Agent                         |
| Part03 Structural               | Adapter, Decorator, Proxy, Facade            | Backend Agent, Review Agent           |
| Part04 Behavioral               | Strategy, Observer, Command, Template Method | Backend Agent, PM Agent               |
| Part05 Architecture             | Layered, Hexagonal, Clean Architecture       | PM Agent, Review Agent                |
| Part06 Review & Troubleshooting | 코드 검수, 문제 해결, Anti-pattern           | Review Agent                          |
| Part07 Selection & Workflow     | Pattern 선택, Agent 작업 흐름                | PM Agent, Backend Agent, Review Agent |

---

### [Retrieval Routing]

```text
질문:
Service가 너무 커졌는데 어떻게 나눌까?

우선 검색:
Part01 SRP
Part05 God Service Problem
Part06 SRP Violation
Part07 Pattern Selection
```

```text
질문:
외부 API DTO가 Service에 들어와도 되나?

우선 검색:
Part03 Adapter Pattern
Part05 Hexagonal Architecture
Part06 Adapter Troubleshooting
Part07 Structural Pattern Selection
```

```text
질문:
if 문이 많으면 Strategy로 바꿔야 하나?

우선 검색:
Part01 OCP
Part04 Strategy Pattern
Part06 Strategy Troubleshooting
Part07 Pattern Anti-Decision
```

```text
질문:
@Transactional이 왜 안 먹지?

우선 검색:
Part03 Spring AOP Proxy
Part06 Proxy Troubleshooting
Part07 Structural Pattern Selection
```

---

### [주의]

- Agent는 하나의 문서만 검색하지 않는다.
- Core 원칙과 Pattern 문서를 함께 검색한다.
- Troubleshooting 문서는 Review 단계에서 우선 사용한다.
- Pattern 적용 여부가 애매하면 Part07 Anti-Decision을 함께 검색한다.
- Architecture 변경은 Part05와 Part06을 함께 검색한다.

---

### [FAQ]

Q. Design Pattern 문서 검색은 어떻게 라우팅하는가?

A. 질문 유형을 생성, 구조, 행동, 아키텍처, 리뷰 문제로 분류해 관련 Part를 우선 검색한다.

Q. SOLID 관련 질문은 어느 문서를 먼저 검색하는가?

A. Part01 Core & SOLID와 Part06 Review & Troubleshooting을 우선 검색한다.

Q. 외부 API 연동 질문은 어느 문서를 검색하는가?

A. Part03 Adapter, Part05 Hexagonal, Part06 Adapter Troubleshooting을 우선 검색한다.

Q. Pattern 적용 여부가 애매하면 어느 문서를 검색하는가?

A. Part07 Pattern Selection과 Pattern Anti-Decision을 검색한다.

---

## 5.2 Agent Retrieval Query Routing

### [개념]

Agent Retrieval Query Routing은 PM Agent, Backend Agent, Review Agent가 사용자 질문과 코드 문제를 적절한 RAG 문서로 연결하는 규칙이다.

```text
User Query
→ Query Intent
→ Domain Document
→ Section
→ Answer / Code / Review
```

---

### [핵심]

- Query Intent를 먼저 판단한다.
- 구현 질문은 Backend Agent 중심으로 검색한다.
- 검수 질문은 Review Agent 중심으로 검색한다.
- 요구사항 분류 질문은 PM Agent 중심으로 검색한다.
- Pattern 선택 질문은 Part07을 우선 검색한다.
- 실무 예시가 필요하면 Pattern별 Part를 함께 검색한다.
- 문제 해결 질문은 Part06 Troubleshooting을 함께 검색한다.

---

### [실무]

| Query Intent                      | 우선 검색                                             |
| --------------------------------- | ----------------------------------------------------- |
| “이 구조 괜찮아?”                 | Part06, Part01, Part05                                |
| “어떤 Pattern 써야 해?”           | Part07, 관련 Pattern Part                             |
| “외부 API 연동 어떻게 해?”        | Part03, Part05, Part06                                |
| “if 문 많아졌어”                  | Part04 Strategy, Part01 OCP, Part07                   |
| “객체 생성 복잡해”                | Part02 Factory / Builder                              |
| “Service 너무 커졌어”             | Part01 SRP, Part05 God Service, Part06                |
| “이벤트로 분리할까?”              | Part04 Observer, Part06 Observer Troubleshooting      |
| “재시도 구조 필요해”              | Part04 Command Queue, Part06 Command Retry Bug        |
| “Architecture가 과한가?”          | Part05, Part06 Over Engineering, Part07 Anti-Decision |
| “Agent Workflow에 어떻게 적용해?” | Part07 Agent Workflow                                 |

---

### [예제]

```text
User Query:
결제 수단이 계속 늘어날 거 같은데 if 문으로 처리해도 돼?

Routing:
Part01 OCP
Part04 Strategy
Part02 Factory
Part07 Behavioral Pattern Selection
Part07 Pattern Anti-Decision

Answer Focus:
Strategy + Factory 후보
단순 결제 수단 2개 이하라면 조건문 유지 가능
```

```text
User Query:
외부 API 호출 코드를 Service에 넣었는데 괜찮아?

Routing:
Part03 External API Adapter
Part05 Hexagonal Architecture
Part06 Adapter Troubleshooting
Part07 Structural Pattern Selection

Answer Focus:
Adapter 분리 권장
단순 일회성 호출이면 과설계 주의
```

---

### [주의]

- 검색 결과가 Pattern 적용을 자동 확정하지 않는다.
- Agent는 항상 단순 구조 유지 가능성을 함께 검토한다.
- Review 질문은 Troubleshooting 문서와 함께 검색한다.
- Architecture 질문은 Over Engineering 위험을 반드시 검토한다.
- Agent는 RAG 검색 결과를 현재 프로젝트 문맥에 맞게 적용한다.

---

### [FAQ]

Q. Agent Retrieval Query Routing은 무엇인가?

A. 사용자 질문이나 코드 문제를 적절한 RAG 문서와 Section으로 연결하는 규칙이다.

Q. 구현 질문은 어떤 문서를 우선 검색하는가?

A. 관련 Pattern Part와 Part07 Selection 문서를 우선 검색한다.

Q. 검수 질문은 어떤 문서를 우선 검색하는가?

A. Part06 Review & Troubleshooting을 우선 검색하고 Part01, Part05를 함께 참조한다.

Q. 요구사항 분석 질문은 어떤 문서를 우선 검색하는가?

A. Part07 PM Agent Workflow와 Pattern Selection Matrix를 우선 검색한다.

---

# 6. Final Pattern Selection Checklist

## 6.1 Selection Checklist

### [개념]

Selection Checklist는 Design Pattern 적용 전 최종적으로 확인해야 할 검수 항목이다.

이 Checklist는 Backend Agent, Review Agent, PM Agent가 공통으로 사용한다.

```text
Pattern Candidate
→ Checklist
→ Apply / Simplify / Reject
```

---

### [핵심]

- 문제 유형이 명확한가?
- 변경 가능성이 실제로 있는가?
- Pattern 적용 후 책임이 분리되는가?
- Pattern 적용 후 테스트가 쉬워지는가?
- Pattern 적용 후 의존성이 줄어드는가?
- Pattern 적용 후 코드 이해가 더 쉬워지는가?
- Pattern 적용 비용이 이점보다 크지 않은가?
- 단순 구조로 충분하지 않은가?

---

### [Checklist]

Problem Checklist:

- 해결하려는 문제가 명확한가?
- 문제를 생성, 구조, 행동, 아키텍처 중 하나로 분류했는가?
- 현재 코드에서 실제 불편함이 있는가?
- 변경 요청이 반복될 가능성이 있는가?

Pattern Fit Checklist:

- Pattern 목적과 문제 목적이 일치하는가?
- Pattern 적용 후 기존 코드 수정이 줄어드는가?
- Pattern 적용 후 책임이 명확해지는가?
- Pattern 적용 후 테스트 단위가 작아지는가?
- Pattern 적용 후 외부 의존성이 격리되는가?

Trade-off Checklist:

- Class와 Interface 수가 과도하게 늘어나지 않는가?
- 팀원이 이해할 수 있는 구조인가?
- Agent가 일관되게 생성할 수 있는 구조인가?
- Debugging 흐름이 지나치게 숨겨지지 않는가?
- 단순 구조 유지가 더 낫지 않은가?

Review Checklist:

- SOLID 위반을 개선하는가?
- Tight Coupling을 줄이는가?
- Over Engineering을 만들지 않는가?
- Domain Rule이 더 잘 보호되는가?
- External DTO 침투를 막는가?
- Transaction, Event, Retry, Proxy 제약을 고려했는가?

---

### [실무]

최종 판단 문장 형식:

```text
최종 판단:
Strategy Pattern 적용 권장

이유:
결제 정책이 계속 추가될 가능성이 높고 현재 if / switch 분기가 증가하고 있다.
Strategy와 Factory를 사용하면 OCP를 개선하고 정책별 테스트가 쉬워진다.

주의:
결제 수단이 1~2개로 고정된다면 단순 조건문 유지가 더 적절할 수 있다.
```

```text
최종 판단:
Pattern 적용 보류

이유:
현재 기능은 단순 조회 API이며 외부 의존성, 정책 교체, 재시도 요구가 없다.
Layered Architecture로 충분하다.

주의:
향후 외부 Provider나 복잡한 Domain Rule이 추가되면 Adapter 또는 Domain Service 분리를 재검토한다.
```

---

### [FAQ]

Q. Pattern 적용 전 최종적으로 확인할 것은?

A. 문제 유형, 변경 가능성, 책임 분리 효과, 테스트 용이성, 적용 비용, 단순 구조 가능성을 확인한다.

Q. Pattern 적용이 실패한 신호는?

A. 코드가 더 복잡해졌지만 변경, 테스트, 의존성 문제가 개선되지 않은 경우이다.

Q. Pattern 적용 보류는 어떤 경우에 하는가?

A. 현재 문제가 단순하고 변경 가능성이 낮으며 Pattern 비용이 더 큰 경우 보류한다.

Q. Agent가 최종 판단을 쓸 때 포함해야 할 내용은?

A. 적용 여부, 이유, 관련 Pattern, Trade-off, 주의점을 포함해야 한다.

---

# 7. Final Integration Rules

## 7.1 Design Pattern RAG Integration Rules

### [개념]

Design Pattern RAG Integration Rules는 Design Pattern 문서 세트가 Backend Agent, Review Agent, PM Agent의 코드 생성과 검수에 어떻게 통합되어야 하는지 정의한다.

Design Pattern RAG는 단순 지식 문서가 아니라 Agent 판단 기준이다.

```text
RAG Retrieval
→ Pattern Decision
→ Code Generation
→ Code Review
→ Refactoring
```

---

### [핵심]

- Design Pattern RAG는 Pattern 암기가 아니라 판단 기준이다.
- Backend Agent는 구현 전 Pattern 후보를 검색한다.
- Review Agent는 구현 후 Pattern 적합성과 Over Engineering을 검수한다.
- PM Agent는 요구사항을 Pattern 후보와 위험으로 분류한다.
- 모든 Agent는 단순 구조 유지 가능성을 검토한다.
- Pattern 적용은 SOLID와 Architecture 기준을 함께 사용한다.
- Troubleshooting 문서는 코드 검수 시 우선 검색한다.

---

### [실무]

Agent 통합 흐름:

```text
User Request
→ PM Agent Requirement Classification
→ Design Pattern Retrieval
→ Backend Agent Implementation
→ Review Agent Troubleshooting Review
→ Refactoring Suggestion
→ Final Output
```

Design Pattern 문서 사용 우선순위:

```text
1. Part07 Pattern Selection
2. 관련 Pattern Part
3. Part01 SOLID
4. Part05 Architecture
5. Part06 Troubleshooting
```

Review 단계 우선순위:

```text
1. Part06 Troubleshooting
2. Part01 SOLID
3. Part05 Architecture
4. 관련 Pattern Part
5. Part07 Anti-Decision
```

---

### [주의]

- Agent는 Pattern을 적용하기 전에 검색해야 한다.
- Agent는 Pattern 적용 후 Review 문서를 다시 검색해야 한다.
- Retrieval 결과가 많을수록 단순한 해결책을 우선한다.
- Pattern 적용 이유가 없으면 적용하지 않는다.
- Pattern 적용 결과가 복잡하면 Part07 Anti-Decision을 다시 검토한다.

---

### [FAQ]

Q. Design Pattern RAG는 무엇을 위해 사용하는가?

A. Agent가 Pattern을 검색하고 적절히 적용하며 잘못된 구조를 검수하기 위해 사용한다.

Q. Backend Agent는 Design Pattern RAG를 언제 검색하는가?

A. 요구사항 구현 전 Pattern 후보를 판단할 때 검색한다.

Q. Review Agent는 Design Pattern RAG를 언제 검색하는가?

A. 구현 후 구조 문제, Pattern 오용, Over Engineering을 검수할 때 검색한다.

Q. PM Agent는 Design Pattern RAG를 어떻게 사용하는가?

A. 요구사항을 설계 문제로 분류하고 Pattern 후보와 검수 포인트를 전달하는 데 사용한다.

---

# Retrieval Queries

### [FAQ]

Q. Pattern Selection이란?
A. 요구사항과 코드 문제를 분석해 적절한 Design Pattern 또는 단순 구조를 선택하는 과정이다.

Q. Pattern Selection에서 가장 먼저 해야 할 일은?
A. 문제가 생성, 구조, 행동, 아키텍처 문제 중 어디에 속하는지 분류하는 것이다.

Q. Pattern을 적용하지 않는 것도 좋은 선택인가?
A. 그렇다. 단순한 문제에는 단순한 구조가 더 좋은 설계일 수 있다.

Q. Pattern Selection의 핵심 기준은?
A. 변경 가능성, 책임 분리, 테스트 용이성, 의존성 방향, 적용 비용이다.

Q. Problem Classification이란?
A. 현재 설계 문제가 생성, 구조, 행동, 아키텍처, 과설계 중 어디에 속하는지 분류하는 과정이다.

Q. 객체 생성 문제가 있으면 어떤 Pattern을 검토하는가?
A. Factory, Builder, Singleton 같은 Creational Pattern을 검토한다.

Q. 외부 API 구조가 내부와 다르면 어떤 Pattern을 검토하는가?
A. Adapter Pattern과 Port 분리를 검토한다.

Q. 정책이 계속 추가되면 어떤 Pattern을 검토하는가?
A. Strategy Pattern과 Factory Pattern을 검토한다.

Q. Factory는 언제 선택하는가?
A. 요청 타입이나 조건에 따라 다른 객체를 생성하거나 선택해야 할 때 선택한다.

Q. Builder는 언제 선택하는가?
A. 생성자 파라미터가 많거나 선택 필드가 많아 객체 생성 가독성이 떨어질 때 선택한다.

Q. Singleton은 언제 선택하는가?
A. 하나의 인스턴스를 공유해야 할 때 선택하지만 Spring Boot에서는 기본적으로 Spring Bean을 우선 사용한다.

Q. Static Factory Method는 언제 선택하는가?
A. 생성자보다 의미 있는 이름으로 객체 생성 의도를 표현하고 싶을 때 선택한다.

Q. Adapter는 언제 선택하는가?
A. 외부 API, Legacy System, SDK를 내부 Interface에 맞게 변환해야 할 때 선택한다.

Q. Decorator는 언제 선택하는가?
A. 기존 객체 기능 전후에 로깅, 캐싱, 검증, 보안 같은 부가기능을 추가할 때 선택한다.

Q. Proxy는 언제 선택하는가?
A. 접근 제어, 지연 로딩, Transaction, Security, AOP 같은 대리 호출이 필요할 때 선택한다.

Q. Adapter, Decorator, Proxy 차이는?
A. Adapter는 인터페이스 변환, Decorator는 기능 확장, Proxy는 접근 제어가 목적이다.

Q. Strategy는 언제 선택하는가?
A. 알고리즘, 정책, 처리 방식이 여러 개이고 추가 가능성이 높을 때 선택한다.

Q. Observer는 언제 선택하는가?
A. 하나의 이벤트 후 여러 후속 작업이 필요하고 직접 결합을 줄이고 싶을 때 선택한다.

Q. Template Method는 언제 선택하는가?
A. 여러 기능의 공통 처리 흐름은 같고 일부 단계만 다를 때 선택한다.

Q. Command는 언제 선택하는가?
A. 요청을 객체로 저장, 전달, 재시도, 큐 처리해야 할 때 선택한다.

Q. Layered Architecture는 언제 선택하는가?
A. 단순 CRUD, 일반 Spring Boot API, 빠른 구현이 필요한 경우 선택한다.

Q. Hexagonal Architecture는 언제 선택하는가?
A. 외부 API, 결제, 알림, 파일 저장소처럼 교체 가능성이 높은 외부 의존성이 있을 때 선택한다.

Q. Clean Architecture는 언제 선택하는가?
A. Domain Rule이 복잡하고 장기 유지보수와 테스트 격리가 중요한 경우 선택한다.

Q. Architecture Pattern을 섞어도 되는가?
A. 가능하다. 실무에서는 Layered 기반에 Adapter, Port, Domain Isolation을 부분 적용하는 경우가 많다.

Q. PM Agent Workflow는 무엇인가?
A. 사용자 요구사항을 설계 문제와 Pattern 후보로 분류하고 Backend Agent와 Review Agent에게 작업 지시를 전달하는 흐름이다.

Q. PM Agent는 Pattern을 확정해야 하는가?
A. 아니다. Pattern 후보와 검수 포인트를 제시하고 구현과 검수 단계에서 확정하게 한다.

Q. PM Agent가 단순 CRUD를 발견하면?
A. Layered Architecture 기반 단순 구현을 지시하고 과도한 Pattern 적용을 금지한다.

Q. PM Agent가 외부 시스템 연동을 발견하면?
A. Adapter, Port, Timeout, Retry, 예외 변환, 외부 DTO 격리를 검토 지시한다.

Q. Backend Agent Workflow는 무엇인가?
A. 요구사항을 코드 구조로 변환하고 필요한 경우 Pattern을 적용해 Spring Boot Backend 코드를 생성하는 흐름이다.

Q. Backend Agent의 기본 Architecture는?
A. 단순 기능은 Layered Architecture를 기본으로 사용한다.

Q. Backend Agent는 언제 Adapter를 적용하는가?
A. 외부 API, 결제, 알림, 파일 저장소 등 외부 기술을 내부 Use Case와 분리해야 할 때 적용한다.

Q. Backend Agent는 언제 Pattern 적용을 보류해야 하는가?
A. 변경 가능성이 낮고 단순 구조가 더 명확할 때 Pattern 적용을 보류한다.

Q. Review Agent Workflow는 무엇인가?
A. 생성된 코드와 구조를 SOLID, Design Pattern, Architecture 기준으로 검수하고 개선안을 제안하는 흐름이다.

Q. Review Agent는 무엇을 우선 검수하는가?
A. 책임 분리, 의존성 방향, 외부 DTO 침투, Pattern 적합성, Over Engineering을 우선 검수한다.

Q. Review Agent는 Pattern 제거를 제안할 수 있는가?
A. 그렇다. 불필요한 Pattern은 제거하는 것이 더 좋은 Refactoring일 수 있다.

Q. Review Agent 결과는 어떤 형식이 좋은가?
A. 문제, 원인, 관련 원칙, 관련 Pattern, 해결, Trade-off, 최종 판단 형식이 좋다.

Q. If-Then Pattern Decision은 무엇인가?
A. 문제 신호를 Pattern 후보로 빠르게 연결하기 위한 Agent용 판단 규칙이다.

Q. If-Then 규칙은 Pattern 적용을 확정하는가?
A. 아니다. 후보를 찾는 규칙이며 Trade-off 검토 후 적용 여부를 결정한다.

Q. If 외부 API DTO가 Service에 들어오면 Then 무엇을 검토하는가?
A. Adapter Pattern, Port, Hexagonal Architecture를 검토한다.

Q. If 구현체가 하나뿐이고 변경 가능성이 낮으면 Then 무엇을 검토하는가?
A. Interface 제거 또는 단순 구조 유지를 검토한다.

Q. Pattern Anti-Decision은 무엇인가?
A. Pattern을 적용하지 않는 것이 더 좋은 상황을 정의하는 판단 기준이다.

Q. Pattern 적용을 보류하는 대표 상황은?
A. 구현체가 하나뿐이고 변경 가능성이 낮거나 단순 CRUD처럼 구조 비용이 더 큰 경우이다.

Q. 단순 구조 유지도 설계 판단인가?
A. 그렇다. 현재 문제에 가장 적합한 최소 구조를 선택하는 것도 설계이다.

Q. Pattern 적용을 보류했다가 나중에 적용해도 되는가?
A. 가능하다. 변경 압력이 실제로 생겼을 때 점진적으로 적용하는 것이 안전하다.

Q. Design Pattern 문서 검색은 어떻게 라우팅하는가?
A. 질문 유형을 생성, 구조, 행동, 아키텍처, 리뷰 문제로 분류해 관련 Part를 우선 검색한다.

Q. SOLID 관련 질문은 어느 문서를 먼저 검색하는가?
A. Part01 Core & SOLID와 Part06 Review & Troubleshooting을 우선 검색한다.

Q. 외부 API 연동 질문은 어느 문서를 검색하는가?
A. Part03 Adapter, Part05 Hexagonal, Part06 Adapter Troubleshooting을 우선 검색한다.

Q. Pattern 적용 여부가 애매하면 어느 문서를 검색하는가?
A. Part07 Pattern Selection과 Pattern Anti-Decision을 검색한다.

Q. Agent Retrieval Query Routing은 무엇인가?
A. 사용자 질문이나 코드 문제를 적절한 RAG 문서와 Section으로 연결하는 규칙이다.

Q. 구현 질문은 어떤 문서를 우선 검색하는가?
A. 관련 Pattern Part와 Part07 Selection 문서를 우선 검색한다.

Q. 검수 질문은 어떤 문서를 우선 검색하는가?
A. Part06 Review & Troubleshooting을 우선 검색하고 Part01, Part05를 함께 참조한다.

Q. 요구사항 분석 질문은 어떤 문서를 우선 검색하는가?
A. Part07 PM Agent Workflow와 Pattern Selection Matrix를 우선 검색한다.

Q. Pattern 적용 전 최종적으로 확인할 것은?
A. 문제 유형, 변경 가능성, 책임 분리 효과, 테스트 용이성, 적용 비용, 단순 구조 가능성을 확인한다.

Q. Pattern 적용이 실패한 신호는?
A. 코드가 더 복잡해졌지만 변경, 테스트, 의존성 문제가 개선되지 않은 경우이다.

Q. Pattern 적용 보류는 어떤 경우에 하는가?
A. 현재 문제가 단순하고 변경 가능성이 낮으며 Pattern 비용이 더 큰 경우 보류한다.

Q. Agent가 최종 판단을 쓸 때 포함해야 할 내용은?
A. 적용 여부, 이유, 관련 Pattern, Trade-off, 주의점을 포함해야 한다.

Q. Design Pattern RAG는 무엇을 위해 사용하는가?
A. Agent가 Pattern을 검색하고 적절히 적용하며 잘못된 구조를 검수하기 위해 사용한다.

Q. Backend Agent는 Design Pattern RAG를 언제 검색하는가?
A. 요구사항 구현 전 Pattern 후보를 판단할 때 검색한다.

Q. Review Agent는 Design Pattern RAG를 언제 검색하는가?
A. 구현 후 구조 문제, Pattern 오용, Over Engineering을 검수할 때 검색한다.

Q. PM Agent는 Design Pattern RAG를 어떻게 사용하는가?
A. 요구사항을 설계 문제로 분류하고 Pattern 후보와 검수 포인트를 전달하는 데 사용한다.
