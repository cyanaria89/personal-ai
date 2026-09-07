# Testing Part 02 - Mockito

---

# 1. Mockito Core

## 1.1 Mockito Overview

### [개념]

Mockito는 Java Unit Test에서 사용하는 Mock Framework다.

주요 목적:

- Dependency Isolation
- Mock Object Creation
- Stubbing
- Interaction Verification

---

### [핵심]

Mockito 핵심 기능:

- Mock 생성
- Stub 설정
- Method Call 검증
- Argument 검증

---

### [실무]

2026 Spring Boot 실무 기준 Mockito는 Service Test에서 가장 많이 사용된다.

주요 사용 대상:

- Repository
- External API Client
- Redis Client
- Kafka Producer
- Payment Client

---

### [FAQ]

Q. Mockito란?
A. Java Unit Test용 Mock Framework다.

Q. Mockito는 왜 사용하는가?
A. 외부 의존성을 제거하고 Unit Logic만 독립 검증하기 위해 사용한다.

---

# 2. Mock Object

## 2.1 Mock Basics

### [개념]

Mock Object는 실제 객체 대신 사용하는 가짜 객체다.

---

### [Flow]

```text
Real Dependency 제거
→ Mock Object 생성
→ Test Isolation
```

---

### [핵심]

Mock 목적:

- 외부 의존 제거
- 테스트 속도 향상
- 독립 실행 보장

---

### [FAQ]

Q. Mock Object란?
A. 실제 객체 대신 사용하는 테스트용 가짜 객체다.

---

# 3. Core Annotation

## 3.1 @Mock

### [개념]

@Mock은 Mock 객체를 생성한다.

---

### [예제]

```java
@Mock
private UserRepository userRepository;
```

---

### [FAQ]

Q. @Mock 대상은?
A. 외부 의존 객체가 대상이다.

---

## 3.2 @InjectMocks

### [개념]

@InjectMocks는 Mock 객체를 테스트 대상 객체에 주입한다.

---

### [예제]

```java
@InjectMocks
private UserService userService;
```

---

### [FAQ]

Q. @InjectMocks 역할은?
A. Mock 객체를 자동 주입해 테스트 대상을 생성한다.

---

## 3.3 MockitoExtension

### [개념]

JUnit 5 환경에서 Mockito 초기화용 Extension.

---

### [예제]

```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
}
```

---

### [FAQ]

Q. MockitoExtension이 필요한가?
A. 필요하다. Mock 초기화를 담당한다.

---

# 4. Stubbing

## 4.1 Stubbing Overview

### [개념]

Stubbing은 특정 호출에 대한 반환값을 미리 설정하는 작업이다.

---

### [Flow]

```text
Method Call
→ Stub Match
→ Return Value
```

---

### [핵심]

핵심 API:

- given
- willReturn
- when
- thenReturn

---

### [FAQ]

Q. Stubbing이란?
A. Mock 호출 시 반환값을 미리 정의하는 것이다.

---

## 4.2 BDD Style

### [예제]

```java
given(userRepository.findById(1L))
        .willReturn(Optional.of(user));
```

---

### [Best Practice]

BDDMockito 스타일 권장.

이유:

- Given / When / Then 구조와 자연스럽게 연결

---

### [FAQ]

Q. given과 when 차이는?
A. 기능은 같고 스타일만 다르다.

---

## 4.3 Exception Stubbing

### [예제]

```java
given(userRepository.findById(1L))
        .willThrow(new RuntimeException());
```

---

### [FAQ]

Q. Exception도 Stubbing 가능한가?
A. 가능하다.

---

# 5. Verify

## 5.1 Verify Basics

### [개념]

verify는 Mock 객체 메서드 호출 여부를 검증한다.

---

### [핵심]

- verify
- times
- never
- atLeastOnce

---

### [예제]

```java
verify(userRepository)
        .findById(1L);
```

---

### [FAQ]

Q. verify 목적은?
A. 의존 객체 호출 여부 검증이다.

---

## 5.2 Verify Count

### [예제]

```java
verify(userRepository, times(1))
        .findById(1L);
```

---

### [예제]

```java
verify(userRepository, never())
        .save(any());
```

---

### [FAQ]

Q. verify(times(1))는 생략 가능한가?
A. 가능하다. 기본값이 1회다.

---

# 6. Argument Matching

## 6.1 Matcher

### [개념]

Argument Matcher는 입력값 매칭 조건을 정의한다.

---

### [핵심]

- any()
- anyLong()
- eq()

---

### [예제]

```java
verify(userRepository)
        .findById(anyLong());
```

---

### [FAQ]

Q. any()는 언제 사용하는가?
A. 특정 값보다 타입 중심 검증이 필요할 때 사용한다.

---

# 7. ArgumentCaptor

## 7.1 Captor

### [개념]

ArgumentCaptor는 전달된 인자를 캡처해서 검증한다.

---

### [Flow]

```text
Method Call
→ Capture Argument
→ Validate Object State
```

---

### [예제]

```java
ArgumentCaptor<User> captor =
        ArgumentCaptor.forClass(User.class);

verify(userRepository).save(captor.capture());
```

---

### [FAQ]

Q. ArgumentCaptor는 언제 사용하는가?
A. 메서드 인자로 전달된 객체 상태 검증 시 사용한다.

---

# 8. Mockito Rules

## 8.1 Best Practice

### [Best Practice]

권장:

- 필요한 객체만 Mock
- 핵심 Interaction만 verify
- Mock 최소화

---

### [주의]

금지:

- 모든 객체 Mock
- 과도한 verify
- 구현 세부사항 검증

---

### [Checklist]

- Mock 최소화
- Stub 명확성
- Verify 과도 여부 확인

---

# 9. Common Mistakes

## 9.1 Frequent Issues

### [Troubleshooting]

문제:

Mock NullPointerException

원인:

MockitoExtension 누락

해결:

```java
@ExtendWith(MockitoExtension.class)
```

---

문제:

Stub ignored

원인:

Matcher 불일치

해결:

Argument 확인

---

문제:

Verify 실패

원인:

호출 횟수 불일치

해결:

Interaction 재검토

---

# 10. Agent Decision Rules

## 10.1 Mockito Usage Routing

### [Flow]

```text
External Dependency Exists
→ Mockito Required

Pure Logic Only
→ Mockito Optional
```

---

### [핵심]

Backend Agent 판단 기준.

---

### [FAQ]

Q. 언제 Mockito를 사용해야 하는가?
A. 외부 의존성이 존재할 때 사용한다.

---

# Retrieval Queries

### [FAQ]

Q. Mockito란?
A. Java Unit Test용 Mock Framework다.

Q. Mockito 핵심 기능은?
A. Mock, Stubbing, Verify.

Q. @Mock 역할은?
A. Mock 객체 생성.

Q. @InjectMocks 역할은?
A. Mock 객체 자동 주입.

Q. 언제 Mockito를 사용하는가?
A. 외부 의존성 격리가 필요할 때.
