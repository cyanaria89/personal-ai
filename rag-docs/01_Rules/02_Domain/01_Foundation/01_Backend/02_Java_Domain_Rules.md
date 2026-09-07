# Java Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

Java Domain Rules 문서는 Backend Agent / Review Agent / PM Agent가 Java 기반 백엔드 코드를 작성, 분석, 검토, 리팩터링하기 위한 RAG 문서 제작 규칙이다.

이 문서는 Java 문법 단순 요약이 아니라 AI Agent가 Spring Boot / JPA / Security / QueryDSL / Testing 문서와 연결해 안정적인 Java 코드를 생성하고 검토할 수 있도록 지원하는 규칙 문서다.

목적:

- Java 기본 문법 판단 기준 제공
- 객체지향 설계 기준 제공
- Class / Object / Method / Constructor 사용 기준 제공
- Encapsulation / Inheritance / Polymorphism / Abstraction 이해 지원
- Interface / Abstract Class 선택 기준 제공
- Collection Framework 사용 기준 제공
- Generic / Optional / Stream / Lambda 사용 기준 제공
- Exception Handling 기준 제공
- Immutability / Null Safety / Type Safety 기준 제공
- Java Backend Code Review 기준 제공
- Java Anti Pattern 검출 지원
- Spring Boot 코드 작성 전 Foundation 역할 수행

---

### [핵심]

우선순위:

1. Java Syntax
2. Object Oriented Programming
3. Class and Object
4. Method Design
5. Encapsulation
6. Inheritance
7. Polymorphism
8. Interface
9. Abstract Class
10. Collection Framework
11. Generic
12. Exception Handling
13. Optional
14. Stream API
15. Lambda
16. Immutability
17. Null Safety
18. Type Safety
19. Code Style
20. Java Anti Pattern

---

### [실무]

Java 문서는 아래 작업을 지원하도록 작성한다.

- 요구사항을 Java Class / Method로 변환
- 객체 책임과 협력 관계 설계
- DTO / Entity / Service / Utility 코드 기초 검토
- Collection 선택 기준 판단
- Exception 처리 위치 판단
- NullPointerException 위험 감지
- Optional 오남용 검토
- Stream / for-loop 선택 기준 판단
- Generic 타입 안정성 검토
- 불필요한 상속 / 과도한 static / 거대한 Class 감지
- Java 코드 가독성 / 유지보수성 검토
- Spring Boot 코드 생성 전 Java Foundation 검증

---

### [FAQ]

Q. Java Domain Rules는 Java 문법 공부용 문서야?

A.
아니다. Backend Agent가 Java 코드를 생성하고 검토할 때 참조하는 실무형 RAG 제작 규칙이다.

Q. Java 문서에서 가장 중요한 기준은 뭐야?

A.
객체 책임, Method 설계, Collection 선택, 예외 처리, Null Safety, Type Safety, 유지보수성이다.

Q. Java Domain Rules는 Spring Boot 문서와 분리해야 해?

A.
기본 Java 언어 규칙은 분리하되 Service, DTO, Entity, Repository 코드와 연결되는 실무 기준은 포함한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Java Domain Rules는 Java 기반 백엔드 개발에 필요한 Foundation 범위를 포함한다.

포함 범위:

- Java 기본 문법
- 변수 / 타입 / 연산자
- 조건문 / 반복문
- Method
- Class
- Object
- Constructor
- Access Modifier
- Encapsulation
- Inheritance
- Polymorphism
- Abstract Class
- Interface
- Overloading / Overriding
- Static
- Final
- Enum
- Package
- Collection Framework
- List / Set / Map
- Generic
- Wrapper Type
- Autoboxing / Unboxing
- String / StringBuilder
- Date / Time API 기초
- Exception Handling
- Checked Exception / Unchecked Exception
- Optional
- Lambda
- Stream API
- Functional Interface 기초
- Immutability
- Null Safety
- Type Safety
- Java Code Style
- Java Common Mistakes

---

### [핵심]

반드시 포함:

- Java는 객체지향 언어임
- Class는 상태와 행위를 묶는 설계 단위
- Method는 하나의 책임을 명확히 가져야 함
- Field는 가능한 private으로 보호
- 상속보다 조합을 우선 검토
- Interface는 역할과 계약을 표현
- Collection은 데이터 특성에 따라 선택
- Generic으로 타입 안정성 확보
- Exception은 무조건 삼키지 않음
- Optional은 반환값 부재 표현에 사용
- Stream은 가독성이 좋아질 때 사용
- NullPointerException 위험을 항상 검토
- mutable state 남용 금지
- static 남용 금지

---

### [실무]

Java는 Backend Foundation에서 Spring Boot, JPA, Security 코드의 기반이다.

실무 연결:

```text
Java Foundation
→ Object Oriented Design
→ DTO / Entity / Service Code
→ Spring Boot Layered Architecture
→ JPA Entity Behavior
→ Security Authentication Flow
→ Testing and Refactoring
```

---

### [FAQ]

Q. Java 문서에서 Spring Annotation을 깊게 다뤄?

A.
아니다. Annotation 자체의 Java 개념은 다루되 Spring 전용 Annotation은 Spring Boot Domain Rules에서 다룬다.

Q. Stream API를 깊게 다뤄?

A.
Foundation 수준의 사용 기준과 주의점은 포함하고 복잡한 병렬 처리나 고급 함수형 패턴은 제외한다.

Q. JVM 내부 구조도 포함해?

A.
기초적인 메모리 개념은 가능하지만 JVM 튜닝과 GC 심화는 Expert 또는 Performance 문서에서 다룬다.

---

## 2.2 Excluded Scope

### [개념]

Java Domain Rules에서는 Foundation 범위를 넘어서는 고급 JVM, 프레임워크 심화, 빌드 도구 심화를 제외한다.

제외 범위:

- JVM GC Tuning 심화
- Java Memory Model 심화
- Bytecode Engineering
- Reflection 심화
- Annotation Processor 심화
- Reactive Programming 심화
- Virtual Thread 운영 심화
- Advanced Concurrency
- Netty 심화
- Maven / Gradle 심화
- Spring Boot Annotation 상세
- JPA Entity Mapping 상세
- Security 인증인가 상세
- QueryDSL 상세
- Testing Framework 상세
- Performance Profiling 심화

---

### [핵심]

제외 이유:

- Foundation 범위 초과
- Spring Boot / JPA / Security / Testing 문서와 분리 필요
- Agent Retrieval 혼선 방지
- Java 언어 기초와 객체지향 코드 품질에 집중

---

### [실무]

고급 주제는 별도 Domain Rules에서 관리한다.

예:

```text
Java Domain Rules
→ Spring Boot Domain Rules
→ JPA Advanced Domain Rules
→ Testing Domain Rules
→ Performance Tuning Domain Rules
→ Advanced Spring Architecture Domain Rules
```

---

### [FAQ]

Q. Thread와 동시성은 여기서 다뤄?

A.
기초 개념과 주의점은 포함할 수 있지만 고급 동시성 제어는 Expert 문서에서 다루는 것이 적합하다.

Q. Reflection은 여기서 다뤄?

A.
Framework가 내부적으로 사용한다는 수준은 가능하지만 직접 활용 심화는 제외한다.

Q. Gradle 설정도 Java 문서에 넣어?

A.
아니다. 빌드 도구 설정은 Spring Boot 또는 Build / Deploy 관련 문서에서 다룬다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

Java RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

Required:

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

### [핵심]

필수 Section 목적:

- [개념]: Java 문법과 객체지향 정의
- [핵심]: 검색 친화 키워드
- [실무]: Backend 코드 작성 기준
- [FAQ]: 사용자 질문 매칭 강화

---

### [실무]

각 문서는 아래 구조를 기본으로 한다.

```md
# Topic

## Sub Topic

### [개념]

### [핵심]

### [실무]

### [FAQ]
```

---

### [FAQ]

Q. Java 문서에도 FAQ가 필요해?

A.
필요하다. FAQ는 사용자 질문과 RAG 검색 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

Java 문서에는 코드 작성 판단과 오류 검토를 위해 추가 Section을 포함할 수 있다.

Strongly Recommended:

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

### [핵심]

추천 Section 사용 기준:

- 객체지향 설명 → [Flow], [예제]
- Interface / Abstract Class 비교 → [Comparison]
- Collection 선택 → [Comparison], [Checklist]
- Exception 처리 → [Flow], [주의]
- Stream API 설명 → [예제], [주의]
- Null Safety 설명 → [Troubleshooting]
- Anti Pattern 설명 → [Troubleshooting], [Checklist]

---

### [실무]

예시:

```md
### [Flow]

Requirement
→ Identify Responsibility
→ Design Class
→ Design Method
→ Choose Type / Collection
→ Handle Exception
→ Review Null Safety
```

---

### [FAQ]

Q. Java 문서에 Comparison이 중요한 이유는?

A.
Interface와 Abstract Class, List와 Set, Optional과 null처럼 자주 헷갈리는 선택 기준을 구분해야 하기 때문이다.

Q. Java 문서에 Troubleshooting이 필요한 이유는?

A.
NullPointerException, ClassCastException, ConcurrentModificationException, 과도한 static, mutable state 문제가 자주 발생하기 때문이다.

---

# 4. Java Syntax Rules

## 4.1 Variable and Type Rules

### [개념]

Java Variable은 값을 저장하는 이름 있는 공간이며 Type은 값의 종류와 사용 가능한 연산을 결정한다.

---

### [핵심]

필수 키워드:

- primitive type
- reference type
- int / long / double / boolean / char
- String
- Wrapper Type
- type conversion
- casting
- autoboxing
- unboxing
- null

---

### [실무]

타입 선택 기준:

```text
정수 ID → Long
작은 정수 계산 → int
금액 / 정밀 계산 → BigDecimal 검토
참/거짓 → boolean / Boolean
문자열 → String
날짜 / 시간 → LocalDate / LocalDateTime
DB nullable 값 → Wrapper Type 검토
```

주의:

- Entity ID는 보통 Long 사용
- null 가능성이 있으면 primitive 대신 Wrapper Type 검토
- 금액 계산에 double 사용 주의
- 형변환 시 데이터 손실 확인
- `==`와 `equals()` 차이 주의

---

### [FAQ]

Q. int와 Integer 차이는?

A.
int는 primitive type이고 Integer는 null을 가질 수 있는 Wrapper Type이다.

Q. Long은 언제 써?

A.
Entity ID, 큰 정수 값, DB BIGINT와 매핑되는 값에 주로 사용한다.

Q. 금액 계산에 double을 써도 돼?

A.
정밀도 문제가 생길 수 있으므로 금액 계산은 BigDecimal을 검토하는 것이 좋다.

---

## 4.2 Condition and Loop Rules

### [개념]

조건문은 실행 흐름을 분기하고 반복문은 같은 작업을 반복 수행한다.

---

### [핵심]

사용 대상:

- if
- else if
- else
- switch
- for
- enhanced for
- while
- break
- continue
- guard clause

---

### [실무]

권장:

- 복잡한 중첩 if는 guard clause로 줄임
- 조건식은 읽기 쉽게 분리
- 반복 중 Collection 수정 주의
- null check는 초기에 처리
- enum 분기는 switch 사용 가능

예:

```java
public void validateUser(User user) {
    if (user == null) {
        throw new IllegalArgumentException("user must not be null");
    }

    if (!user.isActive()) {
        throw new IllegalStateException("inactive user");
    }
}
```

---

### [FAQ]

Q. 중첩 if가 많으면 어떻게 해?

A.
guard clause, Method 분리, 조건 객체화, enum 전략 등을 검토한다.

Q. for문과 Stream 중 뭐가 좋아?

A.
단순 반복이나 제어 흐름이 복잡하면 for문이 좋고, 변환/필터/집계가 명확하면 Stream이 좋다.

---

# 5. Object Oriented Rules

## 5.1 Class and Object Rules

### [개념]

Class는 상태와 행위를 정의하는 설계도이고 Object는 Class를 기반으로 생성된 실제 인스턴스다.

---

### [핵심]

Class 구성:

- field
- constructor
- method
- access modifier
- responsibility
- invariant
- object state
- object behavior

---

### [실무]

Class 설계 기준:

```text
요구사항 분석
→ 책임 식별
→ 상태 Field 정의
→ 생성 시 유효성 검토
→ 행위 Method 정의
→ 외부 공개 API 최소화
```

권장:

- Class는 하나의 명확한 책임을 가짐
- Field는 private 우선
- 외부 변경은 Method를 통해 제어
- 생성자에서 필수 값 검증
- Getter / Setter 자동 생성 남용 주의

---

### [FAQ]

Q. Class는 어떻게 나누는 게 좋아?

A.
책임 기준으로 나눈다. 하나의 Class가 너무 많은 이유로 변경된다면 분리 후보다.

Q. Field는 왜 private으로 둬?

A.
객체 상태를 보호하고 변경 규칙을 Method 안에 모으기 위해서다.

---

## 5.2 Method Design Rules

### [개념]

Method는 객체나 Class가 수행하는 하나의 작업 단위다.

---

### [핵심]

Method 설계 기준:

- single responsibility
- clear name
- parameter
- return type
- side effect
- validation
- exception
- readability
- testability

---

### [실무]

권장:

- Method 이름은 동작을 표현
- 하나의 Method는 하나의 책임
- Parameter가 많으면 객체로 묶기 검토
- boolean flag parameter 남용 주의
- return null 지양
- 예외 발생 조건 명확화
- 너무 긴 Method는 분리

예:

```java
public boolean canPublish(Post post) {
    return post != null && post.isDraft() && post.hasContent();
}
```

---

### [FAQ]

Q. Method는 얼마나 짧아야 해?

A.
정해진 줄 수보다 하나의 책임을 명확히 수행하고 읽기 쉬운지가 중요하다.

Q. Parameter가 많으면 어떻게 해?

A.
Request DTO, Command 객체, Value Object로 묶는 것을 검토한다.

---

## 5.3 Encapsulation Rules

### [개념]

Encapsulation은 객체 내부 상태를 숨기고 정해진 Method를 통해서만 변경하게 하는 객체지향 원칙이다.

---

### [핵심]

목적:

- state protection
- invariant preservation
- controlled mutation
- business rule location
- maintainability

---

### [실무]

나쁜 예:

```java
user.setPoint(user.getPoint() + 100);
```

좋은 예:

```java
user.addPoint(100);
```

권장:

- Setter 남용 금지
- 상태 변경 Method에 비즈니스 규칙 포함
- Entity 상태 변경은 의미 있는 Method로 표현
- 외부에서 내부 Collection 직접 수정 금지

---

### [FAQ]

Q. Setter를 쓰면 안 돼?

A.
무조건 금지는 아니지만 비즈니스 상태 변경은 의미 있는 Method로 표현하는 것이 좋다.

Q. Encapsulation은 왜 중요해?

A.
객체 상태 변경 규칙을 한곳에 모아 데이터 불일치와 잘못된 변경을 줄이기 위해서다.

---

## 5.4 Inheritance and Composition Rules

### [개념]

Inheritance는 부모 Class의 속성과 동작을 자식 Class가 물려받는 방식이다.

Composition은 다른 객체를 Field로 가지고 협력하는 방식이다.

---

### [핵심]

상속 사용 조건:

- is-a relationship
- 공통 동작 재사용
- 다형성 필요
- 부모와 자식의 의미적 일관성

조합 사용 조건:

- has-a relationship
- 역할 위임
- 변경에 유연한 구조
- 불필요한 계층 방지

---

### [실무]

기본 판단:

```text
정말 is-a 관계인가?
→ 부모 변경이 자식에 영향을 줘도 괜찮은가?
→ 다형성이 필요한가?
→ 아니면 Composition 우선 검토
```

주의:

- 코드 재사용만을 위한 상속 지양
- 깊은 상속 계층 지양
- 부모 Class의 protected 상태 남용 주의
- Composition이 테스트와 변경에 더 유리한 경우가 많음

---

### [FAQ]

Q. 상속은 언제 써?

A.
명확한 is-a 관계와 다형성이 필요할 때 사용한다.

Q. 상속보다 조합을 우선하라는 말은 뭐야?

A.
기능 재사용만 목적이라면 상속보다 객체를 포함하고 위임하는 방식이 더 유연하다는 뜻이다.

---

## 5.5 Polymorphism Rules

### [개념]

Polymorphism은 같은 Interface나 부모 타입으로 여러 구현 객체를 다룰 수 있는 객체지향 특성이다.

---

### [핵심]

사용 대상:

- interface-based design
- strategy pattern
- dependency inversion
- method overriding
- runtime dispatch
- extension without modification

---

### [실무]

예:

```java
public interface DiscountPolicy {
    int discount(int price);
}

public class FixedDiscountPolicy implements DiscountPolicy {
    public int discount(int price) {
        return 1000;
    }
}
```

권장:

- 변하는 정책은 Interface로 분리
- if-else 분기가 늘어나면 다형성 검토
- 구현체 교체 가능성을 고려
- Spring Bean 주입과 연결 가능

---

### [FAQ]

Q. 다형성은 왜 써?

A.
구현체가 바뀌어도 사용하는 쪽 코드를 크게 바꾸지 않고 확장하기 위해 사용한다.

Q. if-else가 많으면 무조건 다형성으로 바꿔?

A.
무조건은 아니다. 정책이 계속 늘어나거나 변경 가능성이 크면 다형성을 검토한다.

---

# 6. Interface and Abstract Class Rules

## 6.1 Interface Rules

### [개념]

Interface는 구현 Class가 따라야 할 역할과 계약을 정의한다.

---

### [핵심]

사용 대상:

- role
- contract
- abstraction
- polymorphism
- dependency inversion
- implementation replacement
- testing mock

---

### [실무]

Interface 적합 상황:

```text
구현체가 바뀔 수 있음
여러 구현체가 존재함
테스트에서 Mock 대체 필요
외부 의존성을 추상화해야 함
정책 / 전략을 분리해야 함
```

예:

```java
public interface PasswordEncoder {
    String encode(String rawPassword);
    boolean matches(String rawPassword, String encodedPassword);
}
```

주의:

- 구현체가 하나이고 교체 가능성도 없으면 무조건 Interface를 만들 필요는 없음
- Interface 이름은 역할 중심
- 구현 상세를 Interface에 드러내지 않음

---

### [FAQ]

Q. Interface는 언제 만들어?

A.
역할을 추상화하거나 구현체 교체, 테스트 대체, 다형성이 필요할 때 만든다.

Q. Service마다 Interface를 꼭 만들어야 해?

A.
필수는 아니다. 구현체가 하나뿐이고 교체 가능성이 낮으면 과한 추상화가 될 수 있다.

---

## 6.2 Abstract Class Rules

### [개념]

Abstract Class는 공통 상태와 공통 동작을 일부 구현하면서 하위 Class에 구체 구현을 위임하는 Class다.

---

### [핵심]

사용 대상:

- shared state
- shared behavior
- template method
- partial implementation
- inheritance hierarchy

---

### [실무]

Abstract Class 적합 상황:

- 공통 Field가 필요
- 공통 구현 Method가 필요
- 하위 Class가 일부 Method만 구현
- Template Method Pattern 사용

주의:

- Java는 Class 다중 상속 불가
- 깊은 추상 Class 계층 지양
- 역할 추상화만 필요하면 Interface 우선 검토

---

### [FAQ]

Q. Interface와 Abstract Class 차이는?

A.
Interface는 역할과 계약 중심이고 Abstract Class는 공통 상태와 구현을 함께 제공할 수 있다.

Q. 둘 중 무엇을 먼저 검토해?

A.
역할 추상화는 Interface를 먼저 검토하고 공통 상태와 구현 공유가 필요하면 Abstract Class를 검토한다.

---

# 7. Collection Framework Rules

## 7.1 Collection Selection Rules

### [개념]

Collection Framework는 여러 데이터를 저장하고 탐색하기 위한 Java 표준 자료구조 API다.

---

### [핵심]

주요 Collection:

- List
- ArrayList
- LinkedList
- Set
- HashSet
- LinkedHashSet
- TreeSet
- Map
- HashMap
- LinkedHashMap
- TreeMap
- Queue
- Deque

---

### [실무]

선택 기준:

```text
순서가 중요하고 중복 허용 → List
중복 제거가 중요 → Set
Key-Value 조회가 중요 → Map
삽입 순서 유지 Set → LinkedHashSet
정렬된 Set → TreeSet
빠른 Key 조회 → HashMap
삽입 순서 유지 Map → LinkedHashMap
정렬된 Key → TreeMap
```

주의:

- List.contains는 데이터가 많으면 비용 증가
- 중복 제거는 Set 검토
- Key 기반 조회는 Map 검토
- null 허용 여부 확인
- equals / hashCode 구현 중요

---

### [FAQ]

Q. List와 Set 차이는?

A.
List는 순서와 중복을 허용하고 Set은 중복을 허용하지 않는다.

Q. Map은 언제 써?

A.
Key로 값을 빠르게 찾거나 그룹핑 결과를 저장할 때 사용한다.

Q. 중복 제거는 어떻게 해?

A.
Set을 사용하거나 Stream distinct를 사용할 수 있다. 객체 중복 기준은 equals와 hashCode에 따라 달라진다.

---

## 7.2 equals and hashCode Rules

### [개념]

equals와 hashCode는 객체 동등성 비교와 Hash 기반 Collection 동작에 사용된다.

---

### [핵심]

중요 대상:

- HashSet
- HashMap
- contains
- distinct
- object equality
- value object
- entity identity caution

---

### [실무]

규칙:

- equals를 override하면 hashCode도 함께 override
- 값 객체는 의미 있는 Field 기준 비교
- Entity는 식별자 생성 시점과 영속성 상태 주의
- mutable Field를 hashCode 기준으로 쓰면 위험

예:

```java
@Override
public boolean equals(Object o) {
    if (this == o) return true;
    if (!(o instanceof Email email)) return false;
    return value.equals(email.value);
}

@Override
public int hashCode() {
    return value.hashCode();
}
```

---

### [FAQ]

Q. equals만 override하면 안 돼?

A.
안 된다. HashSet, HashMap 같은 Hash 기반 Collection에서 문제가 생길 수 있으므로 hashCode도 함께 override해야 한다.

Q. 객체 중복 제거가 안 되는 이유는?

A.
equals와 hashCode가 원하는 기준으로 구현되어 있지 않을 수 있다.

---

# 8. Generic Rules

## 8.1 Generic Basics

### [개념]

Generic은 Class, Interface, Method에서 사용할 타입을 외부에서 지정해 타입 안정성을 높이는 기능이다.

---

### [핵심]

키워드:

- Generic Type
- Type Parameter
- Type Safety
- Compile Time Check
- Raw Type
- Wildcard
- Generic Method

---

### [실무]

좋은 예:

```java
List<String> names = new ArrayList<>();
```

나쁜 예:

```java
List names = new ArrayList();
```

권장:

- Raw Type 사용 금지
- Collection에는 Generic Type 명시
- API 응답 Wrapper에 Generic 활용
- Method 반환 타입 명확화
- 불필요한 Object 반환 지양

---

### [FAQ]

Q. Generic은 왜 써?

A.
컴파일 시점에 타입 오류를 잡고 형변환 코드를 줄이기 위해 사용한다.

Q. Raw Type은 왜 안 좋아?

A.
타입 검사가 약해져 ClassCastException 위험이 커진다.

---

## 8.2 Wildcard Rules

### [개념]

Wildcard는 Generic에서 구체 타입을 유연하게 받기 위한 표현이다.

---

### [핵심]

주요 형태:

- `<?>`
- `<? extends T>`
- `<? super T>`
- producer extends
- consumer super

---

### [실무]

기본 기준:

```text
읽기 중심 Producer → ? extends T
쓰기 중심 Consumer → ? super T
정확한 타입 필요 → T
알 수 없는 타입 → ?
```

주의:

- Wildcard를 과도하게 사용하면 읽기 어려움
- API 경계에서 유연성이 필요할 때 사용
- 내부 구현에서는 명확한 타입이 더 좋을 수 있음

---

### [FAQ]

Q. ? extends T는 언제 써?

A.
T의 하위 타입들을 읽기 중심으로 받을 때 사용한다.

Q. ? super T는 언제 써?

A.
T 또는 그 상위 타입 Collection에 값을 넣어야 할 때 사용한다.

---

# 9. Exception Handling Rules

## 9.1 Exception Classification

### [개념]

Exception은 프로그램 실행 중 발생한 비정상 상황을 표현한다.

Java Exception은 Checked Exception과 Unchecked Exception으로 나눌 수 있다.

---

### [핵심]

분류:

- Checked Exception
- Unchecked Exception
- RuntimeException
- Error
- try-catch
- throws
- finally
- custom exception
- exception message

---

### [실무]

Exception 처리 Flow:

```text
Error Situation 발생
→ 복구 가능한가?
→ 호출자가 처리해야 하는가?
→ 현재 계층에서 처리할 것인가?
→ Custom Exception 필요 여부 판단
→ Log / Message / Response 변환
```

권장:

- 예외를 무시하지 않음
- catch 후 빈 블록 금지
- 의미 있는 Exception Type 사용
- 메시지는 원인 파악 가능하게 작성
- Backend에서는 GlobalExceptionHandler와 연결
- 비즈니스 예외는 Custom Exception 검토

---

### [FAQ]

Q. Checked Exception과 Unchecked Exception 차이는?

A.
Checked Exception은 컴파일 시 처리 강제가 있고 Unchecked Exception은 RuntimeException 계열로 컴파일 시 처리 강제가 없다.

Q. Exception을 catch만 하고 아무것도 안 해도 돼?

A.
안 된다. 원인이 사라지지 않고 디버깅이 어려워진다.

---

## 9.2 Custom Exception Rules

### [개념]

Custom Exception은 도메인이나 비즈니스 상황을 명확히 표현하기 위해 직접 정의하는 Exception이다.

---

### [핵심]

사용 대상:

- business rule violation
- resource not found
- duplicate value
- invalid state
- unauthorized action
- domain error

---

### [실무]

예:

```java
public class UserNotFoundException extends RuntimeException {
    public UserNotFoundException(Long userId) {
        super("User not found. userId=" + userId);
    }
}
```

권장:

- Exception 이름은 상황을 명확히 표현
- 메시지에 원인 식별 정보 포함
- 민감정보는 메시지에 포함하지 않음
- Controller가 아니라 Service / Domain 계층에서 발생 가능
- 응답 변환은 GlobalExceptionHandler에서 처리

---

### [FAQ]

Q. Custom Exception은 언제 만들어?

A.
기본 Exception만으로 비즈니스 오류 의미가 명확하지 않을 때 만든다.

Q. 모든 오류마다 Custom Exception을 만들어야 해?

A.
아니다. 의미 있는 도메인 오류나 반복적으로 처리할 오류에 우선 적용한다.

---

# 10. Null Safety and Optional Rules

## 10.1 Null Safety Rules

### [개념]

Null Safety는 null로 인해 발생하는 NullPointerException을 예방하고 값 부재를 명확히 표현하는 기준이다.

---

### [핵심]

확인 대상:

- null check
- required value
- optional value
- default value
- empty collection
- NullPointerException
- Objects.requireNonNull
- validation

---

### [실무]

권장:

- 필수 값은 생성 시점에 검증
- Collection 반환은 null보다 empty collection 권장
- null 가능성 있는 값은 이름과 문서로 명확히 표현
- Service 내부에서 null을 오래 전달하지 않음
- DTO validation과 연결

예:

```java
public User(String email) {
    this.email = Objects.requireNonNull(email, "email must not be null");
}
```

---

### [FAQ]

Q. NullPointerException은 왜 자주 발생해?

A.
참조 변수가 null인 상태에서 Method나 Field에 접근하기 때문이다.

Q. Collection 반환값은 null이 좋아 empty list가 좋아?

A.
대부분 empty list가 좋다. 호출자가 null check를 덜 해도 된다.

---

## 10.2 Optional Rules

### [개념]

Optional은 값이 있을 수도 없을 수도 있음을 반환 타입에서 명시하기 위한 Container다.

---

### [핵심]

사용 대상:

- possible absent return
- repository find result
- orElse
- orElseGet
- orElseThrow
- map
- flatMap
- ifPresent

---

### [실무]

권장:

- Method 반환 타입에 사용
- Field에 Optional 저장 지양
- Parameter로 Optional 받기 지양
- `get()` 직접 호출 지양
- `orElseThrow()`로 예외 변환

예:

```java
User user = userRepository.findById(userId)
    .orElseThrow(() -> new UserNotFoundException(userId));
```

주의:

- Optional은 null을 완전히 없애는 도구가 아님
- Optional 내부에 null 넣지 않음
- 단순 null check보다 복잡해지면 사용 재검토

---

### [FAQ]

Q. Optional은 언제 써?

A.
값이 없을 수 있는 반환 결과를 명시할 때 사용한다.

Q. Optional.get()을 바로 써도 돼?

A.
권장하지 않는다. 값이 없으면 예외가 발생하므로 orElse, orElseGet, orElseThrow 등을 사용한다.

Q. Optional을 Entity Field로 써도 돼?

A.
권장하지 않는다. Optional은 주로 반환 타입에 사용하는 것이 적합하다.

---

# 11. Stream and Lambda Rules

## 11.1 Lambda Rules

### [개념]

Lambda는 익명 함수를 간결하게 표현하는 Java 문법이다.

Functional Interface를 구현할 때 사용한다.

---

### [핵심]

키워드:

- lambda expression
- functional interface
- Predicate
- Function
- Consumer
- Supplier
- method reference

---

### [실무]

예:

```java
List<String> activeNames = users.stream()
    .filter(User::isActive)
    .map(User::getName)
    .toList();
```

권장:

- 짧고 명확한 로직에 사용
- 복잡한 로직은 Method로 분리
- Side Effect 최소화
- Method Reference로 가독성 개선 가능

---

### [FAQ]

Q. Lambda는 언제 써?

A.
짧은 함수형 동작을 전달하거나 Stream API와 함께 사용할 때 쓴다.

Q. Lambda 안에 긴 로직을 넣어도 돼?

A.
권장하지 않는다. 긴 로직은 별도 Method로 분리하는 것이 좋다.

---

## 11.2 Stream API Rules

### [개념]

Stream API는 Collection 데이터를 선언형으로 필터링, 변환, 집계할 수 있는 Java API다.

---

### [핵심]

주요 연산:

- stream
- filter
- map
- flatMap
- sorted
- distinct
- limit
- collect
- toList
- anyMatch
- allMatch
- noneMatch
- findFirst
- reduce

---

### [실무]

Stream 적합 상황:

```text
Collection 데이터
→ 조건 필터링
→ 값 변환
→ 정렬
→ 수집
```

예:

```java
List<PostResponse> responses = posts.stream()
    .filter(Post::isPublished)
    .map(PostResponse::from)
    .toList();
```

주의:

- Stream은 원본 Collection을 직접 변경하지 않음
- 중간 연산은 lazy evaluation
- terminal operation 필요
- side effect 있는 Stream 지양
- 복잡한 흐름은 for문이 더 읽기 쉬울 수 있음

---

### [FAQ]

Q. Stream은 언제 쓰는 게 좋아?

A.
Collection을 필터링, 변환, 집계하는 흐름이 명확할 때 좋다.

Q. Stream이 for문보다 항상 좋아?

A.
아니다. 복잡한 제어 흐름, break/continue가 중요한 경우 for문이 더 읽기 쉽다.

Q. Stream에서 map과 flatMap 차이는?

A.
map은 값을 1:1로 변환하고 flatMap은 중첩된 Stream이나 Collection을 펼쳐서 변환한다.

---

# 12. Immutability and Mutability Rules

## 12.1 Immutability Rules

### [개념]

Immutability는 객체 생성 후 상태가 변경되지 않는 성질이다.

불변 객체는 예측 가능성과 안전성을 높인다.

---

### [핵심]

사용 대상:

- value object
- DTO response
- configuration value
- thread-safe data
- defensive copy
- final field
- record

---

### [실무]

권장:

- 가능한 Field를 final로 선언
- Setter 제거
- 생성자에서 값 검증
- Collection Field는 방어적 복사
- Java record는 단순 불변 데이터에 적합

예:

```java
public record UserSummary(Long userId, String nickname) {
}
```

주의:

- final은 참조 재할당을 막지만 내부 객체 변경까지 막지는 않음
- mutable Collection 노출 주의
- Entity는 JPA 요구사항 때문에 완전 불변 설계가 어려울 수 있음

---

### [FAQ]

Q. final을 붙이면 완전 불변이야?

A.
아니다. 참조 재할당은 막지만 참조 대상 객체 내부 상태가 바뀔 수 있다.

Q. record는 언제 써?

A.
단순한 불변 데이터 전달 객체에 적합하다. JPA Entity에는 일반적으로 적합하지 않다.

---

# 13. Enum Rules

## 13.1 Enum Usage Rules

### [개념]

Enum은 정해진 상수 집합을 타입 안전하게 표현하는 Java 타입이다.

---

### [핵심]

사용 대상:

- status
- role
- category
- type
- state
- fixed option
- switch
- behavior enum

---

### [실무]

예:

```java
public enum PostStatus {
    DRAFT,
    PUBLISHED,
    DELETED
}
```

권장:

- 문자열 상수보다 Enum 사용
- DB 저장 값과 이름 변경 영향 주의
- 화면 표시명은 별도 Field로 관리 가능
- 상태 전이 규칙을 Method로 둘 수 있음

주의:

- Enum 이름 변경은 DB 데이터와 충돌 가능
- 복잡한 권한 매트릭스는 Enum만으로 부족할 수 있음

---

### [FAQ]

Q. 문자열 대신 Enum을 쓰는 이유는?

A.
오타를 줄이고 컴파일 시점 타입 검사를 받을 수 있기 때문이다.

Q. Enum에 Method를 넣어도 돼?

A.
가능하다. 상태별 동작이나 표시명 같은 고정 규칙을 표현할 수 있다.

---

# 14. Static and Final Rules

## 14.1 Static Rules

### [개념]

static은 객체 인스턴스가 아니라 Class 자체에 속하는 Field나 Method를 정의할 때 사용한다.

---

### [핵심]

사용 대상:

- constant
- utility method
- factory method
- shared class-level value

---

### [실무]

적합:

```java
public static final int DEFAULT_PAGE_SIZE = 20;
```

주의:

- mutable static field 지양
- static Method 남용 시 객체지향 설계 약화
- 테스트 대체 어려움
- 상태를 가진 static은 동시성 문제 가능

---

### [FAQ]

Q. static은 언제 써?

A.
상수, 순수 Utility Method, Factory Method처럼 객체 상태에 의존하지 않는 경우 사용한다.

Q. static을 많이 쓰면 왜 안 좋아?

A.
객체 책임이 흐려지고 테스트 대체와 확장이 어려워질 수 있다.

---

## 14.2 Final Rules

### [개념]

final은 변수 재할당, Method Override, Class 상속을 제한하는 키워드다.

---

### [핵심]

사용 위치:

- final variable
- final field
- final method
- final class
- constant
- immutability support

---

### [실무]

권장:

- 변경되지 않는 지역 변수 / Field에 final 검토
- 상수는 `static final`
- 불변 객체 설계에 final Field 활용
- 확장을 막아야 하는 Class에 final 사용 가능

주의:

- final Field라도 참조 객체 내부는 변경 가능
- 무조건 final을 강제하면 코드 작성이 불편해질 수 있음

---

### [FAQ]

Q. final 변수는 값을 바꿀 수 없어?

A.
재할당할 수 없다. 단, 참조형 객체 내부 상태 변경까지 막는 것은 아니다.

Q. static final은 뭐야?

A.
Class 단위 상수를 표현할 때 자주 사용하는 조합이다.

---

# 15. Backend Integration Rules

## 15.1 Java to Spring Boot Connection

### [개념]

Java Domain Rules는 Spring Boot 코드를 작성하기 전 언어와 객체지향 기반을 제공한다.

---

### [핵심]

연결 대상:

- Controller Method
- Service Method
- DTO
- Entity
- Repository Return Type
- Custom Exception
- Enum
- Validation
- Collection Response
- Optional Handling

---

### [실무]

Spring Boot 코드 검토 시 Java 기준:

```text
Controller
→ Parameter / Return Type 명확성
→ DTO 사용 여부

Service
→ Method 책임
→ Transaction 경계
→ Exception 처리

Entity
→ Encapsulation
→ Meaningful Method
→ Setter 남용 여부

Repository
→ Optional 반환 처리
→ Collection 반환 null 여부
```

주의:

- Controller에 비즈니스 로직 과다 작성 금지
- Service Method가 너무 커지면 분리
- DTO와 Entity 역할 혼동 금지
- Entity 상태 변경은 의미 있는 Method로 표현

---

### [FAQ]

Q. Java Domain Rules가 Spring Boot 코드 검토에도 필요해?

A.
필요하다. Spring Boot 코드도 결국 Java Class와 Method로 작성되므로 객체 책임과 타입 안정성 기준이 중요하다.

Q. Entity에 Setter를 많이 둬도 돼?

A.
권장하지 않는다. 상태 변경 의미를 드러내는 Method를 제공하는 것이 좋다.

---

# 16. Troubleshooting Rules

## 16.1 NullPointerException Troubleshooting

### [개념]

NullPointerException은 null 참조에 접근할 때 발생하는 Java의 대표적인 Runtime Exception이다.

---

### [핵심]

원인:

- 초기화되지 않은 Field
- Repository 조회 결과 없음
- DTO Field 누락
- Optional.get 직접 호출
- null Collection 반환
- Method Chain 중간값 null

해결:

- 필수 값 검증
- Optional orElseThrow 사용
- empty collection 반환
- DTO Validation 적용
- null 가능성 명확화
- guard clause 사용

---

### [실무]

Debug Flow:

```text
Exception Line 확인
→ null인 변수 확인
→ 값 생성 위치 확인
→ 입력 / 조회 / Mapping 확인
→ 필수 값 검증 추가
→ 반환 정책 정리
```

---

### [FAQ]

Q. NullPointerException이 나면 뭐부터 봐?

A.
스택트레이스의 발생 라인에서 어떤 참조가 null인지 먼저 확인한다.

Q. NPE를 줄이려면?

A.
필수 값 검증, Optional 반환 처리, empty collection 반환, DTO Validation을 적용한다.

---

## 16.2 ClassCastException Troubleshooting

### [개념]

ClassCastException은 실제 객체 타입과 다른 타입으로 강제 형변환할 때 발생한다.

---

### [핵심]

원인:

- Raw Type 사용
- Object 반환 남용
- 잘못된 casting
- Generic Type 누락
- Collection 내부 타입 혼합

해결:

- Generic 사용
- Object 반환 지양
- 타입 분기 전 instanceof 확인
- API 반환 타입 명확화

---

### [실무]

Debug Flow:

```text
Casting Line 확인
→ 실제 Runtime Type 확인
→ Generic 누락 여부 확인
→ Object 반환 위치 확인
→ 타입 안정성 개선
```

---

### [FAQ]

Q. ClassCastException은 왜 생겨?

A.
실제 객체 타입과 다른 타입으로 강제 형변환했기 때문이다.

Q. 어떻게 줄여?

A.
Generic을 사용하고 Object 반환과 Raw Type 사용을 피한다.

---

## 16.3 ConcurrentModificationException Troubleshooting

### [개념]

ConcurrentModificationException은 Collection을 순회하는 중 구조를 변경할 때 자주 발생한다.

---

### [핵심]

원인:

- for-each 중 remove
- Iterator 외부에서 Collection 변경
- Stream 처리 중 원본 변경
- 동시 접근 Collection 수정

해결:

- Iterator remove 사용
- removeIf 사용
- 새 Collection으로 필터링
- 동시성 Collection 검토

---

### [실무]

나쁜 예:

```java
for (User user : users) {
    if (!user.isActive()) {
        users.remove(user);
    }
}
```

좋은 예:

```java
users.removeIf(user -> !user.isActive());
```

---

### [FAQ]

Q. 반복문에서 remove하면 왜 오류가 나?

A.
Collection을 순회하는 Iterator와 실제 Collection 구조가 달라져 오류가 발생할 수 있다.

Q. 조건에 맞는 요소를 삭제하려면?

A.
removeIf를 사용하거나 새 Collection으로 필터링하는 방식이 좋다.

---

## 16.4 Overused Static Problem

### [개념]

Overused Static Problem은 객체가 가져야 할 책임과 상태를 static Field나 static Method에 과도하게 몰아넣는 문제다.

---

### [핵심]

문제:

- 객체지향 설계 약화
- 테스트 대체 어려움
- 전역 상태 증가
- 동시성 문제 가능
- 의존성 주입 어려움

해결:

- 객체 책임 재분리
- Spring Bean으로 관리
- Interface 추상화
- Utility와 Domain Service 구분
- mutable static 제거

---

### [실무]

검토 Flow:

```text
static Field / Method 확인
→ 객체 상태 의존 여부 확인
→ 외부 의존성 여부 확인
→ 테스트 대체 필요 확인
→ Bean / 객체 Method 전환 검토
```

---

### [FAQ]

Q. static Utility는 써도 돼?

A.
순수 함수처럼 상태와 외부 의존성이 없으면 가능하다.

Q. static 상태가 위험한 이유는?

A.
전역으로 공유되어 예측하기 어렵고 동시성 문제나 테스트 오염을 만들 수 있다.

---

# 17. Comparison Rules

## 17.1 Required Comparisons

### [개념]

Java 문서는 자주 헷갈리는 문법과 설계 선택을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- primitive type vs wrapper type
- `==` vs `equals()`
- String vs StringBuilder
- List vs Set
- HashMap vs TreeMap
- Interface vs Abstract Class
- Inheritance vs Composition
- Overloading vs Overriding
- Checked Exception vs Unchecked Exception
- Optional vs null
- Stream vs for-loop
- final vs immutability
- static method vs instance method
- ArrayList vs LinkedList
- enum vs String constant

---

### [실무]

예시:

| 비교      | Interface           | Abstract Class               |
| --------- | ------------------- | ---------------------------- |
| 성격      | 역할 / 계약         | 공통 상태 + 공통 구현        |
| 다중 구현 | 가능                | Class 다중 상속 불가         |
| 적합      | 구현체 교체, 다형성 | 공통 Field / Template Method |
| 주의      | 과도한 추상화       | 깊은 상속 구조               |

---

### [FAQ]

Q. Java 비교 표는 왜 필요해?

A.
사용자가 자주 헷갈리는 선택 질문에서 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. 가장 중요한 비교는 뭐야?

A.
Interface vs Abstract Class, List vs Set, Optional vs null, Stream vs for-loop, Inheritance vs Composition이다.

---

# 18. Checklist Rules

## 18.1 Java Code Review Checklist

### [개념]

Java 문서 검수 시 코드 품질 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] Class 책임이 명확한가?
- [ ] Method가 하나의 책임을 가지는가?
- [ ] Method 이름이 동작을 명확히 표현하는가?
- [ ] Field 접근 제어자가 적절한가?
- [ ] Setter를 과도하게 사용하지 않는가?
- [ ] 상속보다 조합을 먼저 검토했는가?
- [ ] Interface / Abstract Class 선택이 적절한가?
- [ ] Collection 선택이 데이터 특성에 맞는가?
- [ ] Generic을 사용해 타입 안정성을 확보했는가?
- [ ] Raw Type을 사용하지 않는가?
- [ ] equals / hashCode가 필요한 곳에 구현되었는가?
- [ ] null 반환을 피하고 있는가?
- [ ] Optional을 적절히 사용하는가?
- [ ] Optional.get 직접 호출을 피하는가?
- [ ] Exception을 무시하지 않는가?
- [ ] Custom Exception 이름과 메시지가 명확한가?
- [ ] Stream이 가독성을 높이는가?
- [ ] Lambda 내부 로직이 과도하게 길지 않은가?
- [ ] mutable static 상태가 없는가?
- [ ] 민감정보가 로그나 예외 메시지에 포함되지 않는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 기준:

```text
Draft
→ Responsibility Check
→ Method Check
→ Type Safety Check
→ Null Safety Check
→ Exception Check
→ Collection Check
→ OOP Check
→ Anti Pattern Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. Java 코드 검수에서 가장 중요한 것은?

A.
Class 책임, Method 책임, Null Safety, Type Safety, Exception Handling, Collection 선택, 객체지향 설계다.

---

# 19. Retrieval Optimization Rules

## 19.1 Keyword Rules

### [개념]

Java 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- Java
- Java Syntax
- Object Oriented Programming
- OOP
- Class
- Object
- Method
- Constructor
- Field
- Encapsulation
- Inheritance
- Composition
- Polymorphism
- Interface
- Abstract Class
- Overloading
- Overriding
- Access Modifier
- private
- protected
- public
- static
- final
- enum
- Collection Framework
- List
- Set
- Map
- ArrayList
- HashSet
- HashMap
- Generic
- Raw Type
- Type Safety
- equals
- hashCode
- Exception Handling
- Checked Exception
- Unchecked Exception
- RuntimeException
- Custom Exception
- NullPointerException
- Optional
- Stream API
- Lambda
- Functional Interface
- Immutability
- Mutable State
- String
- StringBuilder
- Java Anti Pattern

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- Java Class는 어떻게 나눠?
- Method는 어떻게 설계해?
- Interface와 Abstract Class 차이는?
- List와 Set 차이는?
- Map은 언제 써?
- Optional은 언제 써?
- NullPointerException은 왜 생겨?
- Stream과 for문 중 뭐가 좋아?
- static은 언제 써?
- final은 불변이야?
- equals와 hashCode는 왜 같이 구현해?
- Java에서 Setter를 많이 써도 돼?
- 상속보다 조합이 좋다는 게 뭐야?

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. FAQ 질문은 어떤 스타일이 좋아?

A.
실제 사용자가 검색하거나 질문할 법한 문장형 질문이 좋다.

---

# 20. Version Rules

## 20.1 Modern Java 기준

### [개념]

Java 문서는 Modern Java와 Spring Boot 백엔드 개발 기준으로 작성한다.

---

### [핵심]

기준:

- Java 17+
- Java 21 호환 고려
- OOP Foundation
- Functional Style 기초
- Stream API
- Optional
- Record 기초
- Modern Date Time API
- Generic Type Safety
- Spring Boot 3.x 연결 가능성
- Jakarta EE 전환 고려

Legacy 제외:

- Vector / Hashtable 중심 설명
- Date / Calendar 중심 신규 코드
- Raw Type 사용 권장
- Thread 직접 생성 중심 설명
- XML 기반 Java EE 중심 설명
- 과도한 Getter / Setter Bean 스타일만 강조

---

### [실무]

실무 기준:

```text
Modern Java
→ Clear Responsibility
→ Type Safety
→ Null Safety
→ Readable Method
→ Collection Fit
→ Exception Clarity
→ Spring Boot Ready Code
```

---

### [FAQ]

Q. Java 8 문법도 다뤄?

A.
Lambda, Stream, Optional처럼 현재도 중요한 Java 8 이후 문법은 다룬다.

Q. Date와 Calendar를 써야 해?

A.
신규 코드는 LocalDate, LocalDateTime 같은 java.time API를 우선 검토한다.

---

# 21. Common Mistakes

## 21.1 Java Common Mistakes

### [개념]

Java 문서는 자주 발생하는 문법 / 객체지향 / 백엔드 코드 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

- 모든 Field에 public 사용
- 모든 Field에 Setter 생성
- Class 하나에 책임을 과도하게 몰아넣음
- Method가 너무 길고 여러 일을 함
- null 반환 남용
- Optional.get 직접 호출
- Optional을 Field나 Parameter로 남용
- Exception을 catch 후 무시
- RuntimeException만 무분별하게 사용
- Raw Type 사용
- Object 반환 남용
- equals만 override하고 hashCode 누락
- String 비교에 `==` 사용
- 금액 계산에 double 사용
- Collection 선택 기준 없이 List만 사용
- 반복 중 Collection 수정
- Stream 내부 Side Effect 남용
- static mutable state 사용
- 상속을 코드 재사용 목적으로만 사용
- Interface를 의미 없이 과도하게 생성
- Entity에 Setter 남용
- DTO와 Entity 역할 혼동

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: user 조회 후 NPE 발생
원인: repository 결과가 없는데 Optional.get 직접 호출
해결: orElseThrow로 명확한 Custom Exception 변환
```

---

### [FAQ]

Q. Java 초보가 가장 많이 하는 실수는?

A.
null 처리 누락, String 비교에 == 사용, Setter 남용, Collection 선택 기준 부족, Exception 무시가 많다.

Q. Java 코드 문제는 어떻게 찾는 게 좋아?

A.
Class 책임, Method 책임, Type Safety, Null Safety, Exception Handling, Collection 선택을 순서대로 확인한다.

---

# 22. Final Goal

## 22.1 Domain Final Goal

### [개념]

Java RAG 문서는 Backend Agent가 Java 언어와 객체지향 원칙을 기준으로 안정적이고 유지보수 가능한 백엔드 코드를 작성하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- Java Syntax 판단
- Class / Object 설계
- Method 책임 분리
- Encapsulation 적용
- Inheritance / Composition 판단
- Polymorphism 적용 판단
- Interface / Abstract Class 선택
- Collection Framework 선택
- Generic Type Safety 확보
- Exception Handling 설계
- Null Safety 검토
- Optional 사용 판단
- Stream / Lambda 사용 판단
- Immutability 검토
- Static / Final 사용 판단
- Enum 사용 판단
- Java Code Review 수행
- Java Anti Pattern 탐지
- Spring Boot 코드 작성 전 Foundation 제공

---

### [실무]

Agent 수행 가능 작업:

```text
User Java Backend Request
→ Identify Responsibility
→ Design Class / Method
→ Choose Type / Collection
→ Apply OOP Rule
→ Handle Exception
→ Check Null Safety
→ Check Type Safety
→ Review Anti Patterns
→ Java Code Output
```

---

### [FAQ]

Q. Java Domain Rules의 최종 목적은 뭐야?

A.
Backend Agent가 Java 문법을 넘어서 객체 책임, 타입 안정성, 예외 처리, Null Safety를 기준으로 실무 코드를 작성하고 검토하게 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
Spring Boot Domain Rules, JPA Advanced Domain Rules, Security Advanced Domain Rules, Testing Domain Rules 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Java Domain Rules는 왜 필요해?
A. Backend Agent가 Java 기반 백엔드 코드를 작성하고 검토할 때 언어와 객체지향 기준이 필요하기 때문이다.

Q. Java 문서에서 가장 중요한 기준은 뭐야?
A. Class 책임, Method 책임, 객체지향 설계, Collection 선택, Exception Handling, Null Safety, Type Safety다.

Q. Java Class는 어떻게 나눠?
A. 책임 기준으로 나눈다. 하나의 Class가 너무 많은 이유로 변경된다면 분리 후보다.

Q. Method는 어떻게 설계해?
A. 하나의 Method는 하나의 책임을 가지고 이름은 동작을 명확히 표현해야 한다.

Q. Field는 왜 private으로 둬?
A. 객체 상태를 보호하고 변경 규칙을 Method 안에 모으기 위해서다.

Q. Setter를 많이 써도 돼?
A. 권장하지 않는다. 비즈니스 상태 변경은 의미 있는 Method로 표현하는 것이 좋다.

Q. Encapsulation은 왜 중요해?
A. 객체 상태 변경 규칙을 한곳에 모아 데이터 불일치와 잘못된 변경을 줄이기 위해서다.

Q. 상속은 언제 써?
A. 명확한 is-a 관계와 다형성이 필요할 때 사용한다.

Q. 상속보다 조합을 우선하라는 말은 뭐야?
A. 기능 재사용만 목적이라면 상속보다 객체를 포함하고 위임하는 방식이 더 유연하다는 뜻이다.

Q. 다형성은 왜 써?
A. 구현체가 바뀌어도 사용하는 쪽 코드를 크게 바꾸지 않고 확장하기 위해 사용한다.

Q. Interface는 언제 만들어?
A. 역할을 추상화하거나 구현체 교체, 테스트 대체, 다형성이 필요할 때 만든다.

Q. Service마다 Interface를 꼭 만들어야 해?
A. 필수는 아니다. 구현체가 하나뿐이고 교체 가능성이 낮으면 과한 추상화가 될 수 있다.

Q. Interface와 Abstract Class 차이는?
A. Interface는 역할과 계약 중심이고 Abstract Class는 공통 상태와 구현을 함께 제공할 수 있다.

Q. List와 Set 차이는?
A. List는 순서와 중복을 허용하고 Set은 중복을 허용하지 않는다.

Q. Map은 언제 써?
A. Key로 값을 빠르게 찾거나 그룹핑 결과를 저장할 때 사용한다.

Q. 중복 제거는 어떻게 해?
A. Set을 사용하거나 Stream distinct를 사용할 수 있다. 객체 중복 기준은 equals와 hashCode에 따라 달라진다.

Q. equals와 hashCode는 왜 같이 구현해?
A. HashSet, HashMap 같은 Hash 기반 Collection에서 객체 동등성 기준을 일관되게 유지하기 위해서다.

Q. String 비교에 ==를 써도 돼?
A. 문자열 내용 비교는 equals를 사용해야 한다. ==는 참조 비교다.

Q. int와 Integer 차이는?
A. int는 primitive type이고 Integer는 null을 가질 수 있는 Wrapper Type이다.

Q. Long은 언제 써?
A. Entity ID, 큰 정수 값, DB BIGINT와 매핑되는 값에 주로 사용한다.

Q. 금액 계산에 double을 써도 돼?
A. 정밀도 문제가 생길 수 있으므로 금액 계산은 BigDecimal을 검토하는 것이 좋다.

Q. Generic은 왜 써?
A. 컴파일 시점에 타입 오류를 잡고 형변환 코드를 줄이기 위해 사용한다.

Q. Raw Type은 왜 안 좋아?
A. 타입 검사가 약해져 ClassCastException 위험이 커진다.

Q. Checked Exception과 Unchecked Exception 차이는?
A. Checked Exception은 컴파일 시 처리 강제가 있고 Unchecked Exception은 RuntimeException 계열로 컴파일 시 처리 강제가 없다.

Q. Exception을 catch만 하고 아무것도 안 해도 돼?
A. 안 된다. 원인이 사라지지 않고 디버깅이 어려워진다.

Q. Custom Exception은 언제 만들어?
A. 기본 Exception만으로 비즈니스 오류 의미가 명확하지 않을 때 만든다.

Q. NullPointerException은 왜 생겨?
A. 참조 변수가 null인 상태에서 Method나 Field에 접근하기 때문이다.

Q. NullPointerException이 나면 뭐부터 봐?
A. 스택트레이스의 발생 라인에서 어떤 참조가 null인지 먼저 확인한다.

Q. Collection 반환값은 null이 좋아 empty list가 좋아?
A. 대부분 empty list가 좋다. 호출자가 null check를 덜 해도 된다.

Q. Optional은 언제 써?
A. 값이 없을 수 있는 반환 결과를 명시할 때 사용한다.

Q. Optional.get()을 바로 써도 돼?
A. 권장하지 않는다. 값이 없으면 예외가 발생하므로 orElse, orElseGet, orElseThrow 등을 사용한다.

Q. Optional을 Entity Field로 써도 돼?
A. 권장하지 않는다. Optional은 주로 반환 타입에 사용하는 것이 적합하다.

Q. Lambda는 언제 써?
A. 짧은 함수형 동작을 전달하거나 Stream API와 함께 사용할 때 쓴다.

Q. Stream은 언제 쓰는 게 좋아?
A. Collection을 필터링, 변환, 집계하는 흐름이 명확할 때 좋다.

Q. Stream이 for문보다 항상 좋아?
A. 아니다. 복잡한 제어 흐름, break/continue가 중요한 경우 for문이 더 읽기 쉽다.

Q. Stream에서 map과 flatMap 차이는?
A. map은 값을 1:1로 변환하고 flatMap은 중첩된 Stream이나 Collection을 펼쳐서 변환한다.

Q. final을 붙이면 완전 불변이야?
A. 아니다. 참조 재할당은 막지만 참조 대상 객체 내부 상태가 바뀔 수 있다.

Q. record는 언제 써?
A. 단순한 불변 데이터 전달 객체에 적합하다. JPA Entity에는 일반적으로 적합하지 않다.

Q. 문자열 대신 Enum을 쓰는 이유는?
A. 오타를 줄이고 컴파일 시점 타입 검사를 받을 수 있기 때문이다.

Q. static은 언제 써?
A. 상수, 순수 Utility Method, Factory Method처럼 객체 상태에 의존하지 않는 경우 사용한다.

Q. static을 많이 쓰면 왜 안 좋아?
A. 객체 책임이 흐려지고 테스트 대체와 확장이 어려워질 수 있다.

Q. Java Domain Rules가 Spring Boot 코드 검토에도 필요해?
A. 필요하다. Spring Boot 코드도 결국 Java Class와 Method로 작성되므로 객체 책임과 타입 안정성 기준이 중요하다.

Q. Java 초보가 가장 많이 하는 실수는?
A. null 처리 누락, String 비교에 == 사용, Setter 남용, Collection 선택 기준 부족, Exception 무시가 많다.

Q. Java 코드 문제는 어떻게 찾는 게 좋아?
A. Class 책임, Method 책임, Type Safety, Null Safety, Exception Handling, Collection 선택을 순서대로 확인한다.

Q. Java 다음 문서는 뭐가 좋아?
A. Spring Boot Domain Rules, JPA Advanced Domain Rules, Security Advanced Domain Rules, Testing Domain Rules 순서가 좋다.
