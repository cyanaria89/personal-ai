# Design Pattern Domain Rules

---

# 1. Domain Purpose

Design Pattern Domain 문서는 Backend Agent / Review Agent / PM Agent용 RAG 문서이다.

목적:

- Software Design Support
- Architecture Improvement Support
- Refactoring Support
- Code Review Support
- Pattern Troubleshooting

우선순위:

1. Design Pattern Core
2. Creational Patterns
3. Structural Patterns
4. Behavioral Patterns

---

# 2. Scope

포함 범위:

- Design Pattern Core
- SOLID
- OOP Principles
- Creational Pattern
- Structural Pattern
- Behavioral Pattern
- Strategy
- Factory
- Singleton
- Builder
- Adapter
- Decorator
- Proxy
- Observer
- Template Method
- Command
- Architecture Pattern
- Hexagonal Architecture
- Clean Architecture
- Troubleshooting

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

---

## Optional

- [Checklist]
- [Troubleshooting]
- [Comparison]

---

# 4. Design Pattern Core Rules

Design Pattern 문서는 Reusable Software Design 중심으로 작성.

핵심 구조:

- Problem
- Pattern
- Solution
- Trade-off

---

반드시 설명 포함:

- Pattern 역할
- 왜 사용하는가
- 어떤 문제를 해결하는가
- 남용 시 문제점

---

예:

```text
Problem
→ Pattern Selection
→ Apply
→ Refactor
```

---

# 5. SOLID Rules

매우 중요.

필수 포함:

- SRP
- OCP
- LSP
- ISP
- DIP

---

반드시 설명:

- 객체지향 설계 원칙
- 유지보수성 향상

---

중요:

Design Pattern 문서 품질은 SOLID 설명 품질이 결정.

---

# 6. Creational Pattern Rules

필수 포함:

- Object Creation
- Encapsulation

---

포함 패턴:

- Singleton
- Factory
- Builder

---

반드시 설명:

- 객체 생성 제어

---

# 7. Singleton Rules

필수 포함:

- Singleton
- Single Instance

---

반드시 설명:

- 하나의 인스턴스 유지
- Spring Bean과 연관성

---

주의:

과도한 Singleton 사용 금지.

---

# 8. Factory Rules

매우 중요.

필수 포함:

- Factory
- Object Creation Delegation

---

예:

```text
Request
→ Factory
→ Concrete Object
```

---

반드시 설명:

- 생성 책임 분리

---

# 9. Builder Rules

필수 포함:

- Builder
- Complex Object Creation

---

반드시 설명:

- 생성자 폭발 해결

---

예:

- Lombok Builder

---

# 10. Structural Pattern Rules

필수 포함:

- Structure Composition

---

포함 패턴:

- Adapter
- Decorator
- Proxy

---

반드시 설명:

- 객체 관계 설계

---

# 11. Adapter Rules

필수 포함:

- Adapter
- Compatibility

---

반드시 설명:

- 인터페이스 변환

---

# 12. Decorator Rules

매우 중요.

필수 포함:

- Decorator
- Dynamic Extension

---

반드시 설명:

- 기능 확장
- 상속 대체

---

예:

- Spring Security Filter Chain

---

# 13. Proxy Rules

필수 포함:

- Proxy
- Access Control

---

반드시 설명:

- 대리 객체
- Lazy Loading
- AOP

---

# 14. Behavioral Pattern Rules

매우 중요.

필수 포함:

- Behavior Pattern

---

포함 패턴:

- Strategy
- Observer
- Template Method
- Command

---

반드시 설명:

- 객체 간 책임 분리

---

# 15. Strategy Rules

매우 중요.

필수 포함:

- Strategy
- Runtime Behavior Change

---

반드시 설명:

- 알고리즘 교체
- 런타임 전략 변경

---

예:

```text
Context
→ Strategy Interface
→ Concrete Strategy
```

---

# 16. Observer Rules

매우 중요.

필수 포함:

- Observer
- Event Notification

---

반드시 설명:

- Publish / Subscribe
- Event Driven

---

예:

- Event Listener
- Kafka Consumer

---

# 17. Template Method Rules

필수 포함:

- Template Method
- Skeleton Algorithm

---

반드시 설명:

- 공통 흐름 정의
- 세부 구현 분리

---

# 18. Command Rules

필수 포함:

- Command
- Request Encapsulation

---

반드시 설명:

- 요청 객체화
- Queue / Undo

---

# 19. Architecture Pattern Rules

매우 중요.

필수 포함:

- Layered Architecture
- Hexagonal Architecture
- Clean Architecture

---

반드시 설명:

- 대규모 설계 패턴

---

# 20. Hexagonal Rules

필수 포함:

- Port
- Adapter

---

반드시 설명:

- Domain 중심 설계
- Infrastructure 분리

---

# 21. Clean Architecture Rules

필수 포함:

- Dependency Rule
- Domain Isolation

---

반드시 설명:

- 의존성 방향
- 핵심 비즈니스 보호

---

# 22. Troubleshooting Rules

반드시 포함 추천.

예:

- Over Engineering
- Wrong Pattern Choice
- Tight Coupling
- Pattern Abuse
- Excessive Abstraction

---

형식:

문제:

원인:

해결:

---

# 23. Retrieval Optimization Rules

강조 대상:

- Design Pattern
- SOLID
- Strategy
- Factory
- Adapter
- Decorator
- Observer
- Clean Architecture

키워드 반복 허용.

---

# 24. Version Rules

기준:

- Java 21
- Spring Boot 3.x
- Modern Backend Architecture

---

Legacy 제외.

---

# 25. Common Mistakes

자주 발생:

- Pattern 남용
- 불필요한 추상화
- SOLID 오해
- 과도한 Interface 분리
- Over Engineering

---

# 26. Final Goal

Design Pattern RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve Design Pattern
- Suggest Pattern Usage
- Review Architecture
- Improve Code Structure
- Solve Design Problems

문서 품질이 Architecture 품질을 결정한다.
