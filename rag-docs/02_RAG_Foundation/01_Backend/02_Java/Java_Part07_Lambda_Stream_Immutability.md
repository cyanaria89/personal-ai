# Java Part07 — Lambda, Stream, Immutability

---

# 1. Lambda Foundation

## 1.1 Lambda Purpose

### [개념]

Lambda Expression은 익명 함수처럼 동작하는 간결한 함수 표현식이다.

Java Lambda는 Functional Interface의 구현을 짧게 표현하기 위해 사용한다.

Backend Agent / Review Agent는 Lambda를 기준으로 Collection 처리, Stream API, Strategy 전달, Callback, 조건식 추상화의 가독성과 안정성을 검토한다.

```java
Predicate<User> activeUser = user -> user.isActive();
```

---

### [핵심]

Lambda 핵심:

- Lambda Expression
- Functional Interface
- Single Abstract Method
- Predicate
- Function
- Consumer
- Supplier
- Comparator
- Method Reference
- Stream API
- Type Inference

Lambda 형식:

```text
(parameter) -> expression
(parameter) -> { statements; }
```

예:

```java
user -> user.isActive()
```

```java
(user) -> {
    validate(user);
    return user.isActive();
}
```

---

### [실무]

2026 백엔드 실무에서 Lambda는 Collection / Stream 처리에서 가장 자주 사용된다.

사용 위치:

```text
filter 조건
map 변환
sorted 비교
forEach 처리
Optional map
Strategy 전달
Callback 처리
간단한 Validator
```

예:

```java
List<UserResponse> responses = users.stream()
    .filter(user -> user.isActive())
    .map(user -> UserResponse.from(user))
    .toList();
```

권장:

- 짧고 명확한 로직에 사용.
- 한 줄 조건이나 변환에 적합.
- 복잡한 로직은 Method로 분리.
- Side Effect가 많은 Lambda는 피한다.
- Method Reference가 더 읽기 좋으면 Method Reference 사용.

주의:

- Lambda가 길어지면 가독성이 급격히 떨어진다.
- Lambda 내부에서 외부 mutable state를 변경하지 않는다.
- 예외 처리가 복잡하면 일반 Method가 더 적합하다.
- 디버깅이 어려워지는 긴 Stream + Lambda 체인은 피한다.

---

### [FAQ]

Q. Lambda는 언제 써?
A. Functional Interface 구현을 짧게 표현하거나 Stream에서 조건, 변환, 정렬 로직을 전달할 때 사용한다.

Q. Lambda는 Class를 대체하는 거야?
A. 아니다. 단일 행위 구현을 간결하게 표현하는 도구다.

Q. Lambda가 길어지면 어떻게 해?
A. 이름 있는 Method로 분리하거나 일반 반복문으로 바꾸는 것이 좋다.

---

## 1.2 Functional Interface Connection

### [개념]

Lambda는 Functional Interface가 있어야 사용할 수 있다.

Functional Interface는 추상 Method가 하나만 있는 Interface다.

```java
@FunctionalInterface
public interface UserFilter {
    boolean test(User user);
}
```

---

### [핵심]

Functional Interface 핵심:

- Functional Interface
- @FunctionalInterface
- Single Abstract Method
- Lambda Target Type
- Predicate
- Function
- Consumer
- Supplier
- Comparator

대표 표준 타입:

```text
Predicate<T> → T를 받아 boolean 반환
Function<T, R> → T를 받아 R 반환
Consumer<T> → T를 받아 소비
Supplier<T> → 입력 없이 T 반환
Comparator<T> → 두 T를 비교
```

---

### [실무]

Predicate 예:

```java
Predicate<User> activeUser = User::isActive;
```

Function 예:

```java
Function<User, UserResponse> toResponse = UserResponse::from;
```

Consumer 예:

```java
Consumer<User> notifier = user -> notificationService.send(user);
```

Supplier 예:

```java
Supplier<String> defaultName = () -> "anonymous";
```

실무 기준:

- 표준 Functional Interface로 충분하면 표준 타입 사용.
- 도메인 의미가 중요하면 Custom Functional Interface 검토.
- Custom Functional Interface에는 `@FunctionalInterface` 사용 권장.
- Lambda 내부 로직이 복잡하면 구현 Class나 Method로 분리.

주의:

- Functional Interface를 무분별하게 만들지 않는다.
- Predicate, Function 등 표준 타입이 의미를 충분히 표현하는지 확인한다.
- 도메인 정책이 복잡하면 Strategy Interface + 구현 Class가 더 명확할 수 있다.

---

### [FAQ]

Q. Lambda는 왜 Functional Interface가 필요해?
A. Lambda가 어떤 Method 구현인지 판단하려면 대상 타입이 필요하기 때문이다.

Q. Predicate는 언제 써?
A. 입력값이 조건을 만족하는지 boolean으로 판단할 때 사용한다.

Q. Custom Functional Interface는 언제 만들어?
A. 표준 타입보다 도메인 의미를 이름으로 표현하는 것이 중요한 경우 만든다.

---

## 1.3 Method Reference Rules

### [개념]

Method Reference는 이미 존재하는 Method를 Lambda보다 간결하게 참조하는 문법이다.

Method Reference는 Lambda의 의도가 명확할 때 가독성을 높인다.

```java
users.stream()
    .map(UserResponse::from)
    .toList();
```

---

### [핵심]

Method Reference 핵심:

- Method Reference
- ClassName::staticMethod
- object::instanceMethod
- ClassName::instanceMethod
- Constructor Reference
- Readability
- Lambda Alternative

형식:

```text
ClassName::staticMethod
object::instanceMethod
ClassName::instanceMethod
ClassName::new
```

---

### [실무]

Static Method Reference:

```java
List<UserResponse> responses = users.stream()
    .map(UserResponse::from)
    .toList();
```

Instance Method Reference:

```java
List<User> activeUsers = users.stream()
    .filter(User::isActive)
    .toList();
```

Constructor Reference:

```java
Supplier<List<String>> listSupplier = ArrayList::new;
```

Comparator 예:

```java
users.sort(Comparator.comparing(User::getCreatedAt));
```

권장:

- Lambda가 단순 Method 호출이면 Method Reference 검토.
- Method 이름이 의미를 잘 표현할 때 사용.
- 변환 Method는 `from`, `of`, `toResponse` 등 명확한 이름 사용.
- 복잡한 조건은 Method Reference보다 명시적 Lambda가 나을 수 있다.

주의:

- Method Reference가 오히려 의미를 숨기면 Lambda 사용.
- 인자 변환이나 추가 조건이 필요하면 Lambda가 더 명확하다.
- Method 이름이 부정확하면 Method Reference도 읽기 어렵다.

---

### [FAQ]

Q. Method Reference는 언제 써?
A. Lambda가 단순히 기존 Method를 호출하는 형태라면 사용한다.

Q. Lambda와 Method Reference 중 뭐가 좋아?
A. Method 이름만으로 의도가 명확하면 Method Reference가 좋고, 추가 조건이 있으면 Lambda가 좋다.

Q. UserResponse::from은 무슨 뜻이야?
A. UserResponse 클래스의 from Method를 함수처럼 참조한다는 뜻이다.

---

## 1.4 Lambda Variable Capture Rules

### [개념]

Lambda는 외부 지역 변수를 사용할 수 있지만, 해당 변수는 final 또는 effectively final이어야 한다.

effectively final은 명시적으로 final은 아니지만 한 번 할당된 후 변경되지 않는 변수를 의미한다.

---

### [핵심]

Variable Capture 핵심:

- Variable Capture
- final
- effectively final
- Local Variable
- Mutable State
- Closure
- Side Effect
- Thread Safety

규칙:

```text
Lambda 내부에서 외부 지역 변수 읽기 가능
외부 지역 변수는 final 또는 effectively final이어야 함
Lambda 내부에서 외부 지역 변수 재할당 불가
객체 참조가 final이어도 객체 내부 상태 변경은 가능
```

---

### [실무]

가능한 예:

```java
String keyword = "spring";

List<Post> result = posts.stream()
    .filter(post -> post.getTitle().contains(keyword))
    .toList();
```

불가능한 예:

```java
int count = 0;

users.forEach(user -> {
    count++;
});
```

위험한 예:

```java
List<User> result = new ArrayList<>();

users.forEach(user -> {
    if (user.isActive()) {
        result.add(user);
    }
});
```

권장:

```java
List<User> result = users.stream()
    .filter(User::isActive)
    .toList();
```

주의:

- Lambda 내부에서 외부 mutable collection 변경은 Side Effect다.
- 병렬 Stream에서는 mutable state 변경이 더 위험하다.
- count, sum 같은 집계는 Stream Collector나 reduce 사용 검토.
- 복잡한 상태 변경은 일반 for문이 더 명확할 수 있다.

---

### [FAQ]

Q. Lambda에서 외부 변수를 바꿀 수 있어?
A. 지역 변수는 final 또는 effectively final이어야 하므로 재할당할 수 없다.

Q. effectively final은 뭐야?
A. final을 붙이지 않았지만 한 번 할당 후 변경되지 않는 변수다.

Q. Lambda 내부에서 List에 add하는 건 괜찮아?
A. 가능은 하지만 Side Effect가 생기므로 Stream collect나 일반 for문을 검토하는 것이 좋다.

---

# 2. Stream Foundation

## 2.1 Stream Purpose

### [개념]

Stream API는 Collection 데이터를 선언형으로 처리하기 위한 Java API다.

Stream은 데이터를 저장하는 자료구조가 아니라 데이터 흐름을 처리하는 Pipeline이다.

```java
List<UserResponse> responses = users.stream()
    .filter(User::isActive)
    .map(UserResponse::from)
    .toList();
```

---

### [핵심]

Stream 핵심:

- Stream API
- Pipeline
- Source
- Intermediate Operation
- Terminal Operation
- filter
- map
- flatMap
- sorted
- distinct
- limit
- collect
- toList
- forEach
- Lazy Evaluation

Stream 구조:

```text
Source
→ Intermediate Operation
→ Intermediate Operation
→ Terminal Operation
```

---

### [실무]

Stream 적합 상황:

```text
Collection 필터링
DTO 변환
중복 제거
정렬
그룹핑
Map 수집
단순 집계
Optional 처리
```

예:

```java
List<PostResponse> responses = posts.stream()
    .filter(Post::isPublished)
    .sorted(Comparator.comparing(Post::getCreatedAt).reversed())
    .map(PostResponse::from)
    .toList();
```

권장:

- filter / map / collect 흐름이 명확할 때 사용.
- 짧은 Pipeline 유지.
- 각 단계는 하나의 목적만 수행.
- 복잡한 조건은 Method로 분리.
- Side Effect 중심 처리는 Stream보다 for문 검토.

주의:

- Stream은 원본 Collection을 자동으로 변경하지 않는다.
- Terminal Operation이 있어야 실행된다.
- Stream은 재사용할 수 없다.
- 긴 Stream Chain은 디버깅이 어렵다.
- DB에서 처리해야 할 필터 / 정렬을 Java Stream으로 가져오지 않는다.

---

### [FAQ]

Q. Stream은 Collection이야?
A. 아니다. Stream은 데이터를 저장하지 않고 처리 흐름을 표현하는 API다.

Q. Stream은 언제 실행돼?
A. collect, toList, forEach 같은 Terminal Operation이 호출될 때 실행된다.

Q. Stream을 한 번 더 사용할 수 있어?
A. 아니다. Stream은 한 번 소비되면 재사용할 수 없다.

---

## 2.2 Intermediate Operation Rules

### [개념]

Intermediate Operation은 Stream Pipeline 중간에서 데이터를 변환하거나 필터링하는 연산이다.

Intermediate Operation은 Lazy하게 동작하며 Terminal Operation이 호출되기 전까지 실행되지 않는다.

---

### [핵심]

중간 연산:

- filter
- map
- flatMap
- sorted
- distinct
- limit
- skip
- peek

특징:

```text
Stream을 반환한다.
Lazy Evaluation 대상이다.
여러 개 연결할 수 있다.
Terminal Operation 전까지 실제 실행되지 않는다.
```

---

### [실무]

filter:

```java
users.stream()
    .filter(User::isActive)
    .toList();
```

map:

```java
users.stream()
    .map(UserResponse::from)
    .toList();
```

sorted:

```java
posts.stream()
    .sorted(Comparator.comparing(Post::getCreatedAt).reversed())
    .toList();
```

distinct:

```java
ids.stream()
    .distinct()
    .toList();
```

주의:

- distinct는 equals / hashCode 기준이다.
- sorted는 정렬 비용이 있다.
- peek은 디버깅 목적에 가깝고 비즈니스 로직에 사용하지 않는다.
- 중간 연산 순서가 성능과 의미에 영향을 줄 수 있다.
- filter를 먼저 적용하면 이후 처리량을 줄일 수 있다.

---

### [FAQ]

Q. Intermediate Operation은 언제 실행돼?
A. Terminal Operation이 호출될 때 함께 실행된다.

Q. filter와 map 순서는 중요해?
A. 중요할 수 있다. 보통 filter로 대상 수를 줄인 뒤 map을 수행하면 효율적이다.

Q. peek은 써도 돼?
A. 디버깅 용도에 가깝고 비즈니스 로직에는 사용하지 않는 것이 좋다.

---

## 2.3 Terminal Operation Rules

### [개념]

Terminal Operation은 Stream Pipeline을 종료하고 결과를 생성하거나 Side Effect를 수행하는 연산이다.

Terminal Operation이 호출되면 Stream Pipeline이 실행된다.

---

### [핵심]

Terminal Operation:

- toList
- collect
- forEach
- reduce
- count
- anyMatch
- allMatch
- noneMatch
- findFirst
- findAny
- min
- max

특징:

```text
Stream을 소비한다.
Pipeline 실행을 트리거한다.
결과 또는 Side Effect를 만든다.
한 번 실행 후 Stream 재사용 불가.
```

---

### [실무]

toList:

```java
List<UserResponse> responses = users.stream()
    .map(UserResponse::from)
    .toList();
```

count:

```java
long activeCount = users.stream()
    .filter(User::isActive)
    .count();
```

anyMatch:

```java
boolean hasAdmin = users.stream()
    .anyMatch(User::isAdmin);
```

findFirst:

```java
Optional<User> firstActiveUser = users.stream()
    .filter(User::isActive)
    .findFirst();
```

주의:

- forEach는 Side Effect가 필요할 때만 사용.
- findFirst는 순서가 있는 Stream에서 의미가 있다.
- anyMatch / allMatch / noneMatch는 short-circuit 가능.
- toList 결과의 수정 가능 여부를 확인한다.
- Terminal Operation 이후 같은 Stream 재사용 불가.

---

### [FAQ]

Q. Terminal Operation은 뭐야?
A. Stream을 실행하고 결과를 만들거나 Side Effect를 수행하는 마지막 연산이다.

Q. anyMatch는 언제 써?
A. 조건을 만족하는 요소가 하나라도 있는지 확인할 때 사용한다.

Q. findFirst 결과는 뭐야?
A. 조건에 맞는 첫 번째 요소를 Optional로 반환한다.

---

## 2.4 Stream Lazy Evaluation Rules

### [개념]

Lazy Evaluation은 Stream 중간 연산이 즉시 실행되지 않고 Terminal Operation이 호출될 때 필요한 만큼 실행되는 특성이다.

---

### [핵심]

Lazy Evaluation 핵심:

- Lazy Evaluation
- Intermediate Operation
- Terminal Operation
- Short Circuit
- Pipeline Execution
- Performance
- Debugging

---

### [실무]

예:

```java
Stream<User> stream = users.stream()
    .filter(User::isActive)
    .map(user -> {
        System.out.println(user.getEmail());
        return user;
    });
```

위 코드는 Terminal Operation이 없으면 실행되지 않는다.

실행 예:

```java
List<User> result = stream.toList();
```

Short-circuit 예:

```java
boolean exists = users.stream()
    .filter(User::isActive)
    .anyMatch(User::isAdmin);
```

주의:

- 중간 연산에 로그를 넣어도 Terminal Operation 전에는 실행되지 않는다.
- anyMatch, findFirst, limit는 필요한 만큼만 처리할 수 있다.
- Lazy 특성을 모르고 디버깅하면 혼란이 생긴다.
- Stream Pipeline은 선언 시점과 실행 시점이 다를 수 있다.

---

### [FAQ]

Q. Stream filter가 바로 실행되지 않는 이유는?
A. Stream 중간 연산은 Lazy Evaluation으로 Terminal Operation이 호출될 때 실행되기 때문이다.

Q. Stream에서 로그가 안 찍히는 이유는?
A. Terminal Operation이 없으면 Pipeline이 실행되지 않는다.

Q. Short-circuit 연산은 뭐야?
A. 결과가 확정되면 나머지 요소 처리를 중단할 수 있는 연산이다.

---

# 3. Stream Transformation Rules

## 3.1 filter Rules

### [개념]

filter는 Stream 요소 중 조건을 만족하는 요소만 남기는 중간 연산이다.

조건은 Predicate로 표현한다.

```java
users.stream()
    .filter(User::isActive)
    .toList();
```

---

### [핵심]

filter 핵심:

- filter
- Predicate
- Condition
- Selection
- Boolean
- Null Safety
- Method Reference
- Guard Condition

---

### [실무]

활성 사용자 필터:

```java
List<User> activeUsers = users.stream()
    .filter(User::isActive)
    .toList();
```

null 제거:

```java
List<String> names = values.stream()
    .filter(Objects::nonNull)
    .toList();
```

조건 Method 분리:

```java
List<Post> visiblePosts = posts.stream()
    .filter(this::isVisiblePost)
    .toList();
```

권장:

- 조건이 짧으면 Lambda 사용.
- 조건이 복잡하면 Method로 분리.
- null 가능성이 있으면 먼저 `Objects::nonNull` 검토.
- filter 조건은 Side Effect 없이 순수하게 유지.

주의:

- filter 내부에서 상태를 변경하지 않는다.
- 조건이 길어지면 가독성이 떨어진다.
- DB 조회 결과 필터링은 DB Query로 처리 가능한지 검토한다.
- null 요소가 섞인 Collection은 정책을 명확히 한다.

---

### [FAQ]

Q. filter는 언제 써?
A. Collection에서 조건을 만족하는 요소만 남기고 싶을 때 사용한다.

Q. filter 조건이 복잡하면 어떻게 해?
A. 의미 있는 이름의 Method로 분리하는 것이 좋다.

Q. filter에서 null 제거는 어떻게 해?
A. `filter(Objects::nonNull)`을 사용할 수 있다.

---

## 3.2 map Rules

### [개념]

map은 Stream 요소를 다른 값으로 변환하는 중간 연산이다.

Entity를 DTO로 변환하거나 Field만 추출할 때 자주 사용한다.

```java
users.stream()
    .map(UserResponse::from)
    .toList();
```

---

### [핵심]

map 핵심:

- map
- Function
- Transformation
- Entity to DTO
- Field Extraction
- Type Conversion
- Method Reference
- Null Mapping

---

### [실무]

Entity to DTO:

```java
List<UserResponse> responses = users.stream()
    .map(UserResponse::from)
    .toList();
```

Field 추출:

```java
List<Long> userIds = users.stream()
    .map(User::getId)
    .toList();
```

값 변환:

```java
List<String> emails = users.stream()
    .map(User::getEmail)
    .map(String::toLowerCase)
    .toList();
```

권장:

- 한 단계 map은 한 가지 변환만 수행.
- Entity를 API로 반환하기 전 DTO 변환에 사용.
- 변환 로직이 복잡하면 static factory 또는 Mapper로 분리.
- null 결과가 나올 수 있는지 확인.

주의:

- map 내부에서 저장, 알림 발송 같은 Side Effect를 수행하지 않는다.
- map에서 null을 반환하면 이후 연산에서 NPE 가능성이 있다.
- DB 조회가 필요한 변환은 N+1 문제를 검토한다.
- 복잡한 DTO 조립은 Service / Mapper로 분리할 수 있다.

---

### [FAQ]

Q. map은 언제 써?
A. Stream 요소를 다른 값이나 타입으로 변환할 때 사용한다.

Q. Entity를 DTO로 바꿀 때 map을 써도 돼?
A. 가능하다. `map(UserResponse::from)` 형태가 자주 사용된다.

Q. map에서 DB 조회를 해도 돼?
A. 가능은 하지만 N+1이나 성능 문제가 생길 수 있어 주의해야 한다.

---

## 3.3 flatMap Rules

### [개념]

flatMap은 각 요소를 Stream으로 변환한 뒤 하나의 Stream으로 평탄화하는 중간 연산이다.

중첩 Collection을 펼칠 때 사용한다.

```java
List<Comment> comments = posts.stream()
    .flatMap(post -> post.getComments().stream())
    .toList();
```

---

### [핵심]

flatMap 핵심:

- flatMap
- Flatten
- Nested Collection
- Stream of Stream
- One to Many Mapping
- Optional flatMap
- Collection Flattening

---

### [실무]

중첩 List 펼치기:

```java
List<List<String>> nestedNames = List.of(
    List.of("kim", "lee"),
    List.of("park")
);

List<String> names = nestedNames.stream()
    .flatMap(List::stream)
    .toList();
```

Post의 Comment 펼치기:

```java
List<CommentResponse> responses = posts.stream()
    .flatMap(post -> post.getComments().stream())
    .map(CommentResponse::from)
    .toList();
```

Optional flatMap:

```java
Optional<Address> address = userRepository.findById(userId)
    .flatMap(User::getAddressOptional);
```

주의:

- JPA Lazy Collection을 flatMap으로 접근하면 N+1 또는 LazyInitializationException 가능.
- 중첩 구조가 깊으면 가독성이 떨어진다.
- flatMap 내부 Collection이 null이면 NPE 발생 가능.
- 데이터가 많으면 메모리 사용량을 검토한다.

---

### [FAQ]

Q. flatMap은 언제 써?
A. 요소마다 여러 결과가 나오거나 중첩 Collection을 하나로 펼칠 때 사용한다.

Q. map과 flatMap 차이는?
A. map은 요소를 하나의 값으로 변환하고 flatMap은 여러 값을 만든 뒤 하나의 Stream으로 펼친다.

Q. JPA 연관 Collection에 flatMap을 써도 돼?
A. 가능하지만 Lazy Loading, N+1, Transaction 범위를 반드시 검토해야 한다.

---

## 3.4 sorted Rules

### [개념]

sorted는 Stream 요소를 정렬하는 중간 연산이다.

정렬 기준은 Comparable 또는 Comparator로 제공한다.

```java
users.stream()
    .sorted(Comparator.comparing(User::getCreatedAt))
    .toList();
```

---

### [핵심]

sorted 핵심:

- sorted
- Comparator
- Comparable
- comparing
- reversed
- thenComparing
- nullsFirst
- nullsLast
- Sort Order

---

### [실무]

기본 정렬:

```java
List<User> sortedUsers = users.stream()
    .sorted(Comparator.comparing(User::getCreatedAt))
    .toList();
```

내림차순:

```java
List<User> sortedUsers = users.stream()
    .sorted(Comparator.comparing(User::getCreatedAt).reversed())
    .toList();
```

복합 정렬:

```java
List<Post> sortedPosts = posts.stream()
    .sorted(Comparator
        .comparing(Post::getLikeCount, Comparator.nullsLast(Comparator.reverseOrder()))
        .thenComparing(Post::getCreatedAt, Comparator.nullsLast(Comparator.reverseOrder())))
    .toList();
```

권장:

- 정렬 기준을 명확히 작성.
- null 가능성이 있으면 nullsFirst / nullsLast 사용.
- 복합 정렬은 thenComparing 사용.
- 대량 데이터 정렬은 DB 정렬 우선 검토.

주의:

- Java Stream 정렬은 메모리에서 수행된다.
- DB에서 정렬 가능한 데이터는 Repository Query에서 처리하는 것이 좋을 수 있다.
- null 값 정렬 기준이 없으면 NPE 가능성이 있다.
- reversed 위치에 따라 결과가 달라질 수 있다.

---

### [FAQ]

Q. Stream에서 정렬은 어떻게 해?
A. sorted와 Comparator.comparing을 사용한다.

Q. 내림차순 정렬은 어떻게 해?
A. Comparator에 reversed를 적용한다.

Q. null 값이 있는 정렬은 어떻게 해?
A. Comparator.nullsFirst 또는 Comparator.nullsLast를 사용한다.

---

# 4. Collectors Rules

## 4.1 toList and collect Rules

### [개념]

toList와 collect는 Stream 결과를 Collection이나 다른 자료구조로 수집하는 Terminal Operation이다.

Java 16 이후 Stream.toList()를 사용할 수 있다.

---

### [핵심]

수집 핵심:

- toList
- collect
- Collectors.toList
- Collectors.toSet
- Collectors.toMap
- groupingBy
- joining
- Unmodifiable List
- Mutable List

---

### [실무]

toList:

```java
List<UserResponse> responses = users.stream()
    .map(UserResponse::from)
    .toList();
```

Collectors.toList:

```java
List<UserResponse> responses = users.stream()
    .map(UserResponse::from)
    .collect(Collectors.toList());
```

toSet:

```java
Set<Long> userIds = users.stream()
    .map(User::getId)
    .collect(Collectors.toSet());
```

실무 기준:

- 단순 List 수집은 `.toList()` 사용 가능.
- 수정 가능한 List가 필요하면 `Collectors.toCollection(ArrayList::new)` 검토.
- Set 수집은 중복 제거 기준 확인.
- API 응답용은 수정 불가여도 문제 없는 경우가 많다.

주의:

- `Stream.toList()` 결과는 수정 불가 List다.
- `Collectors.toList()`의 구체 구현과 수정 가능성에 과도하게 의존하지 않는다.
- 수집 후 수정해야 하면 명확히 mutable collection 생성.
- 대량 데이터 수집은 메모리 사용량을 고려한다.

---

### [FAQ]

Q. Stream.toList()와 Collectors.toList() 차이는?
A. Stream.toList()는 수정 불가 List를 반환한다. 수정이 필요하면 별도 mutable List 생성을 검토한다.

Q. Set으로 수집하면 중복이 제거돼?
A. 그렇다. equals와 hashCode 기준으로 중복이 제거된다.

Q. 수집 후 add를 해야 하면 어떻게 해?
A. `Collectors.toCollection(ArrayList::new)`처럼 수정 가능한 Collection을 명시한다.

---

## 4.2 toMap Rules

### [개념]

Collectors.toMap은 Stream 요소를 Key-Value 구조의 Map으로 수집하는 Collector다.

중복 Key 가능성을 반드시 검토해야 한다.

---

### [핵심]

toMap 핵심:

- Collectors.toMap
- Key Mapper
- Value Mapper
- Merge Function
- Map Supplier
- Duplicate Key
- Function.identity
- LinkedHashMap
- EnumMap

기본 구조:

```text
toMap(keyMapper, valueMapper)
toMap(keyMapper, valueMapper, mergeFunction)
toMap(keyMapper, valueMapper, mergeFunction, mapSupplier)
```

---

### [실무]

기본:

```java
Map<Long, User> userMap = users.stream()
    .collect(Collectors.toMap(User::getId, Function.identity()));
```

중복 Key 처리:

```java
Map<Long, User> userMap = users.stream()
    .collect(Collectors.toMap(
        User::getId,
        Function.identity(),
        (existing, replacement) -> existing
    ));
```

순서 유지:

```java
Map<Long, User> userMap = users.stream()
    .collect(Collectors.toMap(
        User::getId,
        Function.identity(),
        (existing, replacement) -> existing,
        LinkedHashMap::new
    ));
```

주의:

- 중복 Key가 있으면 merge function 없이는 예외 발생.
- Key가 null일 수 있는지 확인.
- Value가 null일 수 있는지 확인.
- 순서가 필요하면 LinkedHashMap supplier 사용.
- Enum Key는 EnumMap을 검토할 수 있다.

---

### [FAQ]

Q. toMap에서 중복 Key가 있으면 어떻게 돼?
A. merge function이 없으면 예외가 발생한다.

Q. Function.identity()는 뭐야?
A. 입력 값을 그대로 반환하는 Function이다.

Q. toMap 결과 순서를 유지하려면?
A. LinkedHashMap::new 같은 Map Supplier를 지정한다.

---

## 4.3 groupingBy Rules

### [개념]

groupingBy는 Stream 요소를 특정 Key 기준으로 그룹화해 Map으로 수집하는 Collector다.

상태별 목록, 카테고리별 목록, 날짜별 이벤트 묶음 등에 사용한다.

---

### [핵심]

groupingBy 핵심:

- groupingBy
- Classifier
- Group Key
- Map<K, List<T>>
- Downstream Collector
- counting
- mapping
- toSet
- summingInt

---

### [실무]

상태별 그룹핑:

```java
Map<UserStatus, List<User>> usersByStatus = users.stream()
    .collect(Collectors.groupingBy(User::getStatus));
```

개수 집계:

```java
Map<UserStatus, Long> countByStatus = users.stream()
    .collect(Collectors.groupingBy(
        User::getStatus,
        Collectors.counting()
    ));
```

DTO로 그룹핑:

```java
Map<UserStatus, List<UserResponse>> responsesByStatus = users.stream()
    .collect(Collectors.groupingBy(
        User::getStatus,
        Collectors.mapping(UserResponse::from, Collectors.toList())
    ));
```

주의:

- 그룹 Key가 null일 수 있는지 확인.
- 결과 Map 순서가 필요하면 supplier를 사용한다.
- 대량 집계는 DB group by가 더 적합할 수 있다.
- 그룹핑 결과가 너무 커지면 메모리 사용량을 확인한다.

---

### [FAQ]

Q. groupingBy는 언제 써?
A. Collection 요소를 특정 기준으로 묶고 싶을 때 사용한다.

Q. 그룹별 개수만 필요하면 어떻게 해?
A. groupingBy와 Collectors.counting을 함께 사용한다.

Q. 데이터가 많아도 Java groupingBy가 좋아?
A. 데이터가 많으면 DB group by나 QueryDSL 집계를 우선 검토하는 것이 좋다.

---

## 4.4 joining Rules

### [개념]

joining은 Stream의 문자열 요소를 하나의 문자열로 결합하는 Collector다.

로그 메시지, 표시용 텍스트, CSV 형태 조합 등에 사용할 수 있다.

---

### [핵심]

joining 핵심:

- Collectors.joining
- String Join
- Delimiter
- Prefix
- Suffix
- Stream<String>
- Text Formatting

---

### [실무]

쉼표 결합:

```java
String result = names.stream()
    .collect(Collectors.joining(", "));
```

prefix / suffix:

```java
String result = names.stream()
    .collect(Collectors.joining(", ", "[", "]"));
```

DTO Field 결합:

```java
String emails = users.stream()
    .map(User::getEmail)
    .collect(Collectors.joining(", "));
```

주의:

- null 문자열이 있으면 NPE 가능성이 있다.
- 사용자 입력을 그대로 joining해 로그나 응답에 노출하지 않는다.
- 대량 문자열 조합은 메모리 사용량을 고려한다.
- CSV 생성은 escaping 정책이 필요하므로 단순 joining만으로 부족할 수 있다.

---

### [FAQ]

Q. joining은 언제 써?
A. 여러 문자열을 구분자로 연결해 하나의 문자열로 만들 때 사용한다.

Q. joining에서 null 요소가 있으면 어떻게 돼?
A. NullPointerException이 발생할 수 있어 사전에 null 제거나 변환이 필요하다.

Q. CSV 만들 때 joining만 쓰면 돼?
A. 단순한 경우는 가능하지만 쉼표, 줄바꿈, 따옴표 escaping이 필요하면 전용 처리를 검토해야 한다.

---

# 5. Stream Matching and Finding

## 5.1 anyMatch, allMatch, noneMatch Rules

### [개념]

Match 연산은 Stream 요소가 특정 조건을 만족하는지 boolean 결과로 확인하는 Terminal Operation이다.

---

### [핵심]

Match 연산:

- anyMatch
- allMatch
- noneMatch
- Predicate
- Short Circuit
- Boolean Result
- Condition Check

의미:

```text
anyMatch → 하나라도 만족하면 true
allMatch → 모두 만족하면 true
noneMatch → 모두 만족하지 않으면 true
```

---

### [실무]

관리자 존재 여부:

```java
boolean hasAdmin = users.stream()
    .anyMatch(User::isAdmin);
```

모든 사용자 활성 여부:

```java
boolean allActive = users.stream()
    .allMatch(User::isActive);
```

차단 사용자 없음:

```java
boolean noBlockedUser = users.stream()
    .noneMatch(User::isBlocked);
```

주의:

- Match 연산은 short-circuit 가능.
- 빈 Stream에서 allMatch는 true를 반환한다.
- 빈 Stream에서 noneMatch도 true를 반환한다.
- 조건 Method 이름을 명확히 작성한다.
- 복잡한 조건은 Method로 분리한다.

---

### [FAQ]

Q. anyMatch는 언제 써?
A. 조건을 만족하는 요소가 하나라도 있는지 확인할 때 사용한다.

Q. allMatch는 빈 목록에서 true야?
A. 그렇다. 빈 Stream에서는 allMatch가 true를 반환한다.

Q. noneMatch는 무슨 뜻이야?
A. 조건을 만족하는 요소가 하나도 없으면 true를 반환한다.

---

## 5.2 findFirst and findAny Rules

### [개념]

findFirst와 findAny는 조건에 맞는 요소 하나를 Optional로 반환하는 Terminal Operation이다.

findFirst는 Encounter Order가 있는 Stream에서 첫 번째 요소를 반환한다.

---

### [핵심]

Finding 연산:

- findFirst
- findAny
- Optional<T>
- Encounter Order
- Short Circuit
- Parallel Stream

---

### [실무]

첫 번째 활성 사용자:

```java
Optional<User> firstActiveUser = users.stream()
    .filter(User::isActive)
    .findFirst();
```

Service 변환:

```java
User user = users.stream()
    .filter(target -> Objects.equals(target.getId(), userId))
    .findFirst()
    .orElseThrow(() -> new UserNotFoundException(userId));
```

주의:

- findFirst는 순서가 있을 때 의미가 명확하다.
- findAny는 병렬 처리에서 더 자유롭다.
- 결과는 Optional이므로 get 직접 호출 지양.
- Key 조회가 반복되면 Stream findFirst보다 Map 변환 검토.
- DB에서 찾을 수 있는 조건이면 Repository Query를 우선 검토한다.

---

### [FAQ]

Q. findFirst는 무엇을 반환해?
A. 조건에 맞는 첫 번째 요소를 Optional로 반환한다.

Q. findFirst와 findAny 차이는?
A. findFirst는 첫 번째 요소를 보장하고 findAny는 아무 요소나 반환할 수 있다.

Q. findFirst 결과는 바로 get해도 돼?
A. 권장하지 않는다. orElseThrow 등으로 값 없음 상황을 처리해야 한다.

---

# 6. Stream Side Effect Rules

## 6.1 Side Effect in Stream

### [개념]

Side Effect는 Stream 처리 중 외부 상태를 변경하거나 외부 시스템에 영향을 주는 작업이다.

Stream은 데이터 변환과 필터링에 적합하며, Side Effect 중심 흐름에는 신중해야 한다.

---

### [핵심]

Stream Side Effect 예:

- 외부 List에 add
- Entity 상태 변경
- Repository save
- 외부 API 호출
- 알림 발송
- 로그 기록
- 카운터 증가
- mutable state 변경

위험:

```text
가독성 저하
테스트 어려움
순서 의존성 증가
병렬 Stream 위험
디버깅 어려움
예외 처리 복잡
```

---

### [실무]

나쁜 예:

```java
List<UserResponse> responses = new ArrayList<>();

users.stream()
    .filter(User::isActive)
    .forEach(user -> responses.add(UserResponse.from(user)));
```

좋은 예:

```java
List<UserResponse> responses = users.stream()
    .filter(User::isActive)
    .map(UserResponse::from)
    .toList();
```

Side Effect가 명확한 경우:

```java
users.forEach(user -> notificationService.send(user));
```

더 명확한 for문:

```java
for (User user : users) {
    notificationService.send(user);
}
```

주의:

- 변환 목적이면 map + collect 사용.
- 외부 상태 변경이 목적이면 for문이 더 명확할 수 있다.
- Stream 안에서 Repository save 반복은 성능과 Transaction을 검토한다.
- 병렬 Stream에서 Side Effect는 동시성 문제를 만들 수 있다.

---

### [FAQ]

Q. Stream forEach에서 외부 List에 add해도 돼?
A. 가능은 하지만 권장하지 않는다. map과 collect로 수집하는 것이 좋다.

Q. 알림 발송처럼 Side Effect가 목적이면 Stream이 좋아?
A. 단순하면 가능하지만 일반 for문이 더 명확한 경우가 많다.

Q. Stream 안에서 save를 반복해도 돼?
A. 가능은 하지만 성능, Transaction, Batch 처리 가능성을 검토해야 한다.

---

## 6.2 forEach Rules

### [개념]

forEach는 Stream 요소 각각에 대해 작업을 수행하는 Terminal Operation이다.

forEach는 결과를 반환하지 않고 Side Effect를 수행한다.

---

### [핵심]

forEach 핵심:

- forEach
- Terminal Operation
- Consumer
- Side Effect
- Iteration
- No Return
- Ordering
- forEachOrdered

---

### [실무]

단순 출력:

```java
users.forEach(user -> log.info("userId={}", user.getId()));
```

알림 발송:

```java
users.forEach(notificationService::send);
```

순서 보장 필요:

```java
users.stream()
    .forEachOrdered(notificationService::send);
```

권장:

- 단순 Side Effect에 제한적으로 사용.
- 결과 수집 목적이면 collect 사용.
- 복잡한 흐름은 for문 사용.
- 예외 처리와 실패 정책이 필요하면 명시적 반복문 검토.

주의:

- forEach에서 return 값 생성 불가.
- 병렬 Stream의 forEach는 순서 보장이 약할 수 있다.
- forEach 내부에서 외부 mutable state 변경 주의.
- forEach로 비즈니스 흐름을 숨기지 않는다.

---

### [FAQ]

Q. forEach는 언제 써?
A. 각 요소에 대해 로그, 알림, 단순 작업 같은 Side Effect를 수행할 때 사용한다.

Q. forEach로 List를 만들면 안 돼?
A. 가능하지만 map과 collect로 결과를 만드는 것이 더 적합하다.

Q. forEach와 forEachOrdered 차이는?
A. forEachOrdered는 Encounter Order를 유지하려고 한다.

---

# 7. Parallel Stream Rules

## 7.1 Parallel Stream Purpose

### [개념]

Parallel Stream은 Stream 작업을 여러 Thread에서 병렬로 처리할 수 있게 하는 기능이다.

Parallel Stream은 자동 성능 향상 도구가 아니며, 작업 특성과 Thread Safety를 검토해야 한다.

---

### [핵심]

Parallel Stream 핵심:

- parallelStream
- Parallel Processing
- ForkJoinPool
- Thread Safety
- CPU Bound
- Side Effect
- Ordering
- Shared Mutable State
- Performance Overhead

적합 가능 상황:

```text
대량 데이터
CPU 연산 중심
요소 간 독립적
공유 mutable state 없음
순서 중요하지 않음
I/O 대기 중심이 아님
```

---

### [실무]

예:

```java
List<Result> results = inputs.parallelStream()
    .map(this::heavyCalculation)
    .toList();
```

신중해야 하는 예:

```java
users.parallelStream()
    .forEach(user -> userRepository.save(user));
```

주의:

- DB 호출, 외부 API 호출은 parallelStream과 잘 맞지 않는 경우가 많다.
- 공유 mutable state를 변경하면 동시성 문제가 생긴다.
- 작은 데이터에서는 오히려 느릴 수 있다.
- 순서 보장이 필요한 경우 성능 이점이 줄어든다.
- Spring Web Request 처리 Thread와 리소스 사용량을 고려한다.

---

### [FAQ]

Q. parallelStream을 쓰면 항상 빨라져?
A. 아니다. 작업 특성, 데이터 크기, Thread Safety에 따라 오히려 느리거나 위험할 수 있다.

Q. DB 저장을 parallelStream으로 하면 좋아?
A. 권장하지 않는다. Connection Pool, Transaction, 동시성 문제가 생길 수 있다.

Q. parallelStream은 언제 검토해?
A. 요소 간 독립적인 대량 CPU 연산이고 공유 상태가 없을 때 검토한다.

---

## 7.2 Parallel Stream Anti Pattern

### [개념]

Parallel Stream Anti Pattern은 병렬 처리에 적합하지 않은 작업을 parallelStream으로 처리해 동시성 오류, 성능 저하, 리소스 고갈을 만드는 패턴이다.

---

### [핵심]

Anti Pattern:

- Repository 호출 병렬화
- 외부 API 호출 병렬화
- 공유 List에 add
- 공유 Map 변경
- Entity 상태 병렬 변경
- 순서 의존 작업
- 작은 데이터 병렬 처리
- 예외 처리 정책 없음
- Transaction 경계 불명확

---

### [실무]

나쁜 예:

```java
List<UserResponse> responses = new ArrayList<>();

users.parallelStream()
    .forEach(user -> responses.add(UserResponse.from(user)));
```

좋은 예:

```java
List<UserResponse> responses = users.stream()
    .map(UserResponse::from)
    .toList();
```

병렬 처리 검토 Flow:

```text
CPU Bound인가?
→ 데이터가 충분히 큰가?
→ 요소 간 독립적인가?
→ 공유 mutable state가 없는가?
→ 순서가 중요하지 않은가?
→ 예외 처리 정책이 있는가?
→ 성능 측정 후 적용
```

주의:

- 성능 측정 없이 적용하지 않는다.
- parallelStream은 공용 ForkJoinPool을 사용한다.
- 서버 환경에서 다른 작업과 Thread 리소스를 공유할 수 있다.
- I/O Bound 작업은 별도 비동기 / 배치 구조 검토가 더 적합할 수 있다.

---

### [FAQ]

Q. parallelStream에서 외부 List에 add하면 왜 위험해?
A. 여러 Thread가 동시에 수정해 데이터 손상이나 예외가 발생할 수 있다.

Q. parallelStream은 언제 피해야 해?
A. DB, 외부 API, 공유 상태 변경, 순서 의존 작업, 작은 데이터 처리에서는 피하는 것이 좋다.

Q. 병렬 처리는 어떻게 결정해야 해?
A. 작업 특성과 데이터 크기를 확인하고 실제 성능 측정 후 결정해야 한다.

---

# 8. Immutability Foundation

## 8.1 Immutability Purpose

### [개념]

Immutability는 객체 생성 후 상태가 변경되지 않는 성질이다.

불변 객체는 상태 추적이 쉽고 Thread Safety와 테스트 안정성에 유리하다.

---

### [핵심]

Immutability 핵심:

- Immutability
- Immutable Object
- final Field
- No Setter
- Constructor Initialization
- Defensive Copy
- Unmodifiable Collection
- Value Object
- Record
- Thread Safety
- Predictability

불변 객체 조건:

```text
Field를 final로 선언
Setter 없음
생성자에서 모든 값 초기화
내부 mutable 객체 방어적 복사
내부 Collection 직접 노출 금지
상태 변경 Method 없음
Class 상속 제한 검토
```

---

### [실무]

Value Object 예:

```java
public final class Email {
    private final String value;

    public Email(String value) {
        if (value == null || !value.contains("@")) {
            throw new IllegalArgumentException("invalid email");
        }

        this.value = value;
    }

    public String value() {
        return value;
    }
}
```

record 예:

```java
public record Period(LocalDate startDate, LocalDate endDate) {
    public Period {
        if (startDate.isAfter(endDate)) {
            throw new IllegalArgumentException("startDate must be before endDate");
        }
    }
}
```

실무 기준:

- DTO는 record로 불변 구조 검토.
- Value Object는 불변 객체로 설계.
- Entity는 JPA 제약 때문에 완전 불변과 충돌 가능.
- 생성 후 변경되지 않는 의존성 Field는 final 사용.
- Collection Field는 방어적 복사 검토.

주의:

- final만으로 완전 불변이 아니다.
- final List는 참조 재할당만 막고 내부 요소 변경은 가능하다.
- mutable 객체를 Field로 가지면 방어적 복사가 필요하다.
- 불변 객체라도 내부 요소 객체가 mutable이면 완전 불변이 아닐 수 있다.

---

### [FAQ]

Q. Immutability는 뭐야?
A. 객체 생성 후 상태가 변경되지 않는 성질이다.

Q. final Field만 있으면 불변 객체야?
A. 아니다. 내부 객체가 mutable이면 상태가 바뀔 수 있다.

Q. 불변 객체는 왜 좋아?
A. 상태 추적이 쉽고 Thread Safety와 테스트 안정성에 유리하다.

---

## 8.2 Defensive Copy Rules

### [개념]

Defensive Copy는 외부에서 전달받은 mutable 객체나 내부 mutable 객체를 복사해 외부 변경으로부터 객체 상태를 보호하는 방식이다.

---

### [핵심]

Defensive Copy 핵심:

- Defensive Copy
- Mutable Object
- List.copyOf
- Set.copyOf
- Map.copyOf
- Unmodifiable Collection
- Internal State Protection
- Constructor Copy
- Getter Copy

적용 대상:

```text
List
Set
Map
Date
Array
Mutable DTO
Mutable Value Object
```

---

### [실무]

생성자 방어적 복사:

```java
public class Team {
    private final List<String> members;

    public Team(List<String> members) {
        this.members = List.copyOf(members);
    }

    public List<String> members() {
        return members;
    }
}
```

배열 방어적 복사:

```java
public class FileData {
    private final byte[] content;

    public FileData(byte[] content) {
        this.content = Arrays.copyOf(content, content.length);
    }

    public byte[] content() {
        return Arrays.copyOf(content, content.length);
    }
}
```

주의:

- List.copyOf는 null 요소가 있으면 예외가 발생할 수 있다.
- Collections.unmodifiableList는 원본 변경이 반영되는 View다.
- 방어적 복사는 비용이 있으므로 필요한 경계를 판단한다.
- JPA Entity Collection에는 단순 copyOf 적용이 어려울 수 있다.

---

### [FAQ]

Q. Defensive Copy는 왜 필요해?
A. 외부에서 mutable 객체를 변경해 내부 상태가 바뀌는 것을 막기 위해 필요하다.

Q. List.copyOf는 어떤 역할을 해?
A. 전달받은 List를 수정 불가 복사본으로 만든다.

Q. 배열은 왜 복사해야 해?
A. 배열은 mutable이라 그대로 반환하면 외부에서 내부 값을 변경할 수 있기 때문이다.

---

## 8.3 Record Rules

### [개념]

record는 Java에서 불변 데이터 전달 객체를 간결하게 정의하기 위한 문법이다.

record는 component 기반으로 생성자, accessor, equals, hashCode, toString을 자동 생성한다.

```java
public record UserResponse(
    Long userId,
    String email
) {
}
```

---

### [핵심]

record 핵심:

- record
- Immutable Data Carrier
- Component
- Canonical Constructor
- Compact Constructor
- Accessor
- equals
- hashCode
- toString
- DTO
- Value Object

record 특징:

```text
component는 final
setter 없음
equals / hashCode 자동 생성
toString 자동 생성
상속 불가
interface 구현 가능
```

---

### [실무]

Response DTO:

```java
public record UserResponse(
    Long userId,
    String email,
    LocalDateTime createdAt
) {
    public static UserResponse from(User user) {
        return new UserResponse(
            user.getId(),
            user.getEmail(),
            user.getCreatedAt()
        );
    }
}
```

Value Object:

```java
public record Email(String value) {
    public Email {
        if (value == null || !value.contains("@")) {
            throw new IllegalArgumentException("invalid email");
        }
    }
}
```

주의:

- record component가 mutable 객체이면 내부 상태 변경 가능성이 있다.
- JPA Entity에는 record가 일반적으로 적합하지 않다.
- Request DTO로 사용할 때 Framework 직렬화 / 역직렬화 지원 확인.
- 복잡한 도메인 행위가 많은 객체는 일반 Class가 더 적합할 수 있다.

---

### [FAQ]

Q. record는 언제 써?
A. 단순 불변 DTO나 Value Object를 간결하게 표현할 때 사용한다.

Q. record는 완전 불변이야?
A. component 참조는 final이지만 component 객체가 mutable이면 내부 상태는 바뀔 수 있다.

Q. Entity를 record로 만들어도 돼?
A. 일반적으로 JPA Entity에는 적합하지 않다.

---

## 8.4 Mutable State Rules

### [개념]

Mutable State는 객체 생성 후 변경 가능한 상태다.

Mutable State는 필요한 경우가 많지만 변경 규칙, Thread Safety, 캡슐화 기준을 명확히 해야 한다.

---

### [핵심]

Mutable State 핵심:

- Mutable State
- State Change
- Setter
- Command Method
- Encapsulation
- Side Effect
- Consistency
- Thread Safety
- Invariant

---

### [실무]

Entity 상태 변경:

```java
public void changeEmail(String email) {
    if (email == null || email.isBlank()) {
        throw new IllegalArgumentException("email must not be blank");
    }

    this.email = email;
}
```

나쁜 예:

```java
user.setStatus(UserStatus.DELETED);
user.setDeletedAt(LocalDateTime.now());
```

좋은 예:

```java
user.delete();
```

Entity Method:

```java
public void delete() {
    if (this.status == UserStatus.DELETED) {
        throw new IllegalStateException("already deleted user");
    }

    this.status = UserStatus.DELETED;
    this.deletedAt = LocalDateTime.now();
}
```

주의:

- Mutable State는 의미 있는 Method로 변경한다.
- Setter 남용은 상태 일관성을 깨뜨릴 수 있다.
- 관련 Field 변경은 하나의 Method 안에서 처리한다.
- static mutable state는 전역 상태 문제가 생긴다.
- 공유 mutable state는 동시성 문제를 만들 수 있다.

---

### [FAQ]

Q. Mutable State는 나쁜 거야?
A. 아니다. 필요한 경우가 많지만 변경 규칙과 캡슐화가 중요하다.

Q. Setter 대신 의미 있는 Method를 쓰는 이유는?
A. 상태 변경 의도와 검증 규칙을 객체 내부에 모으기 위해서다.

Q. static mutable state는 왜 위험해?
A. 전역 공유 상태가 되어 동시성 문제와 요청 간 데이터 오염을 만들 수 있다.

---

# 9. Stream and Immutability Integration

## 9.1 Immutable Result Collection Rules

### [개념]

Stream 결과 Collection은 이후 수정 여부를 기준으로 mutable 또는 immutable 형태를 선택해야 한다.

불필요한 수정 가능성은 줄이는 것이 안전하다.

---

### [핵심]

Immutable Result 핵심:

- Stream.toList
- Unmodifiable List
- List.copyOf
- Collectors.toUnmodifiableList
- Immutable DTO
- No Post Mutation
- Defensive Copy

---

### [실무]

수정 불필요:

```java
List<UserResponse> responses = users.stream()
    .map(UserResponse::from)
    .toList();
```

수정 필요:

```java
List<UserResponse> responses = users.stream()
    .map(UserResponse::from)
    .collect(Collectors.toCollection(ArrayList::new));

responses.add(defaultResponse);
```

외부 전달 전 복사:

```java
return List.copyOf(responses);
```

주의:

- Stream.toList는 수정 불가 List다.
- 결과를 수정할 계획이 있으면 mutable Collection을 명시한다.
- API Response는 수정 불가 List로 충분한 경우가 많다.
- 내부 Collection을 외부에 줄 때 방어적 복사 검토.
- 불변 Collection이라도 요소 객체가 mutable이면 내부 상태 변경 가능.

---

### [FAQ]

Q. Stream.toList 결과에 add할 수 있어?
A. 아니다. 수정 불가 List라 UnsupportedOperationException이 발생할 수 있다.

Q. 수정 가능한 List가 필요하면 어떻게 해?
A. `Collectors.toCollection(ArrayList::new)`을 사용한다.

Q. API 응답 List는 수정 가능해야 해?
A. 보통 수정 가능할 필요가 없다.

---

## 9.2 Pure Function Style Rules

### [개념]

Pure Function은 같은 입력에 대해 항상 같은 출력을 반환하고 외부 상태를 변경하지 않는 함수다.

Stream과 Lambda는 Pure Function에 가까울수록 읽기 쉽고 테스트하기 쉽다.

---

### [핵심]

Pure Function 핵심:

- Pure Function
- Same Input Same Output
- No Side Effect
- No External State Mutation
- Deterministic
- Testability
- Stream Mapping
- Lambda Safety

---

### [실무]

좋은 예:

```java
public UserResponse toResponse(User user) {
    return new UserResponse(user.getId(), user.getEmail());
}
```

Stream 적용:

```java
List<UserResponse> responses = users.stream()
    .map(this::toResponse)
    .toList();
```

나쁜 예:

```java
public UserResponse toResponse(User user) {
    user.increaseViewCount();
    notificationService.send(user);

    return new UserResponse(user.getId(), user.getEmail());
}
```

권장:

- map에 사용하는 Method는 변환만 수행.
- filter에 사용하는 Method는 조건 판단만 수행.
- Side Effect는 별도 Service 흐름에서 명시.
- 같은 입력에 같은 결과를 반환하도록 설계.
- 테스트 가능한 작은 Method로 분리.

주의:

- 도메인 상태 변경은 Pure Function이 아니다.
- 외부 API 호출은 Pure Function이 아니다.
- 시간, 랜덤, DB 조회에 의존하면 결과가 달라질 수 있다.
- Pure Function이 필요한 곳과 상태 변경이 필요한 곳을 구분한다.

---

### [FAQ]

Q. Pure Function은 뭐야?
A. 같은 입력에 항상 같은 출력을 반환하고 외부 상태를 변경하지 않는 함수다.

Q. Stream map에는 어떤 Method가 좋아?
A. Side Effect 없이 값을 변환하는 Method가 좋다.

Q. 모든 Method가 Pure Function이어야 해?
A. 아니다. 상태 변경이 필요한 Method도 있지만 변환 로직은 Pure Function에 가깝게 유지하는 것이 좋다.

---

# 10. Lambda Stream Anti Pattern

## 10.1 Lambda Anti Pattern

### [개념]

Lambda Anti Pattern은 Lambda를 과도하게 사용하거나 내부 로직을 복잡하게 만들어 가독성, 테스트, 디버깅을 어렵게 만드는 패턴이다.

---

### [핵심]

Lambda Anti Pattern:

- 긴 Lambda
- 중첩 Lambda
- Lambda 내부 try-catch 과다
- Lambda 내부 Side Effect
- 외부 mutable state 변경
- 의미 없는 변수명
- 복잡한 조건식
- Method Reference가 더 명확한데 Lambda 사용
- Lambda가 도메인 규칙을 숨김

---

### [실무]

나쁜 예:

```java
users.stream()
    .filter(u -> u != null && u.getStatus() != null && u.getStatus().equals(UserStatus.ACTIVE) && u.getEmail() != null)
    .map(u -> {
        if (u.getNickname() == null) {
            return new UserResponse(u.getId(), "anonymous");
        }
        return new UserResponse(u.getId(), u.getNickname());
    })
    .toList();
```

개선:

```java
List<UserResponse> responses = users.stream()
    .filter(this::isValidActiveUser)
    .map(UserResponse::from)
    .toList();
```

주의:

- Lambda 내부 로직이 길면 Method로 추출.
- Lambda 안의 조건식은 이름 있는 Method로 분리.
- 복잡한 예외 처리는 Lambda 밖에서 처리.
- 도메인 규칙은 Entity / Service / Policy Method로 표현한다.

---

### [FAQ]

Q. Lambda가 길면 왜 문제야?
A. 의도가 숨겨지고 테스트와 디버깅이 어려워진다.

Q. Lambda 조건식이 복잡하면 어떻게 해?
A. 의미 있는 이름의 Method로 분리한다.

Q. Lambda 내부에서 try-catch를 써도 돼?
A. 가능하지만 복잡해지면 일반 Method로 분리하는 것이 좋다.

---

## 10.2 Stream Anti Pattern

### [개념]

Stream Anti Pattern은 Stream을 데이터 변환이 아닌 복잡한 제어 흐름, Side Effect, DB 작업에 남용하는 문제다.

---

### [핵심]

Stream Anti Pattern:

- Stream 안에서 Repository 호출
- Stream 안에서 save 반복
- Stream 안에서 외부 API 호출 반복
- forEach로 결과 List 생성
- peek으로 비즈니스 로직 수행
- 긴 Stream Chain
- 중첩 Stream 과다
- Optional + Stream 과도한 체인
- DB에서 처리할 필터 / 정렬을 Java에서 처리
- parallelStream 무분별 사용

---

### [실무]

나쁜 예:

```java
List<UserResponse> responses = userIds.stream()
    .map(userId -> userRepository.findById(userId).orElseThrow())
    .map(UserResponse::from)
    .toList();
```

개선 방향:

```java
List<User> users = userRepository.findAllById(userIds);

List<UserResponse> responses = users.stream()
    .map(UserResponse::from)
    .toList();
```

나쁜 예:

```java
posts.stream()
    .peek(Post::publish)
    .forEach(postRepository::save);
```

개선:

```java
for (Post post : posts) {
    post.publish();
}

postRepository.saveAll(posts);
```

주의:

- Stream은 데이터 변환 Pipeline에 적합하다.
- 복잡한 비즈니스 흐름은 명시적 Service 코드가 낫다.
- Repository 호출 반복은 N+1과 성능 문제를 만든다.
- peek은 디버깅 목적에 가깝다.
- save 반복은 saveAll 또는 Batch 처리 검토.

---

### [FAQ]

Q. Stream 안에서 Repository를 호출하면 안 돼?
A. 가능은 하지만 N+1과 성능 문제가 생기기 쉬워 일괄 조회를 우선 검토한다.

Q. peek으로 상태 변경을 해도 돼?
A. 권장하지 않는다. peek은 디버깅 목적에 가깝고 비즈니스 로직은 명시적으로 작성하는 것이 좋다.

Q. Stream이 for문보다 항상 좋아?
A. 아니다. 복잡한 제어 흐름이나 Side Effect 중심 로직은 for문이 더 명확할 수 있다.

---

## 10.3 Immutability Anti Pattern

### [개념]

Immutability Anti Pattern은 final이나 record를 사용하면서 실제로는 mutable 상태를 노출하거나 불변성을 오해하는 문제다.

---

### [핵심]

Immutability Anti Pattern:

- final List를 불변으로 착각
- 내부 mutable Collection 직접 반환
- record component에 mutable 객체 저장
- 방어적 복사 누락
- Setter 없는 mutable 객체 노출
- 불변 DTO 내부 요소가 mutable
- Entity를 억지로 완전 불변으로 만들기
- static mutable state 사용

---

### [실무]

나쁜 예:

```java
public class Team {
    private final List<String> members;

    public Team(List<String> members) {
        this.members = members;
    }

    public List<String> members() {
        return members;
    }
}
```

좋은 예:

```java
public class Team {
    private final List<String> members;

    public Team(List<String> members) {
        this.members = List.copyOf(members);
    }

    public List<String> members() {
        return members;
    }
}
```

record 주의:

```java
public record TeamResponse(List<String> members) {
    public TeamResponse {
        members = List.copyOf(members);
    }
}
```

주의:

- final은 참조 재할당만 막는다.
- mutable 객체는 복사하거나 수정 불가로 감싸야 한다.
- record도 component가 mutable이면 완전 불변이 아니다.
- Entity는 JPA 요구사항 때문에 불변 DTO와 다르게 설계한다.

---

### [FAQ]

Q. final List는 불변이야?
A. 아니다. List 참조 재할당만 막고 내부 요소 추가 / 삭제는 가능할 수 있다.

Q. record는 무조건 불변이야?
A. component 참조는 final이지만 component 객체가 mutable이면 내부 상태는 바뀔 수 있다.

Q. 내부 Collection을 안전하게 보관하려면?
A. 생성자에서 List.copyOf 같은 방어적 복사를 사용한다.

---

# 11. Review Checklist

## 11.1 Lambda Stream Immutability Checklist

### [개념]

Lambda Stream Immutability Checklist는 Backend Agent / Review Agent가 Java Lambda, Stream, 불변성 사용 품질을 검토하기 위한 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] Lambda가 짧고 의도가 명확한가?
- [ ] Lambda 내부 로직이 길면 Method로 분리했는가?
- [ ] Functional Interface 사용 이유가 명확한가?
- [ ] Method Reference가 더 명확한 경우 적용했는가?
- [ ] Lambda 내부에서 외부 mutable state를 변경하지 않는가?
- [ ] Stream Pipeline이 Source → Intermediate → Terminal 구조로 명확한가?
- [ ] Terminal Operation이 있어 실제 실행되는가?
- [ ] filter 조건이 복잡하면 Method로 분리했는가?
- [ ] map은 변환만 수행하고 Side Effect를 만들지 않는가?
- [ ] flatMap 사용 시 중첩 Collection null 가능성을 검토했는가?
- [ ] JPA Lazy Collection에 flatMap 사용 시 N+1과 Transaction 범위를 확인했는가?
- [ ] sorted 정렬 기준과 null 처리 기준이 명확한가?
- [ ] 대량 필터 / 정렬 / 그룹핑을 Java가 아니라 DB에서 처리할 수 있는지 검토했는가?
- [ ] toMap 중복 Key 가능성을 검토했는가?
- [ ] groupingBy 결과 크기와 메모리 사용량을 검토했는가?
- [ ] forEach로 결과 Collection을 만들지 않는가?
- [ ] Stream 안에서 Repository / 외부 API 호출을 반복하지 않는가?
- [ ] peek으로 비즈니스 로직을 수행하지 않는가?
- [ ] parallelStream 사용 전 CPU Bound, 데이터 크기, Thread Safety를 검토했는가?
- [ ] Stream.toList 결과 수정 가능 여부를 확인했는가?
- [ ] 수정 가능한 List가 필요하면 명시적으로 생성했는가?
- [ ] Value Object / DTO는 불변성을 검토했는가?
- [ ] final Field를 불변성과 혼동하지 않는가?
- [ ] 내부 mutable Collection에 방어적 복사를 적용했는가?
- [ ] record component에 mutable 객체가 있으면 copyOf를 검토했는가?
```

---

### [실무]

Review Flow:

```text
Lambda Length Review
→ Functional Interface Review
→ Method Reference Review
→ Stream Pipeline Review
→ Side Effect Review
→ Collector Review
→ Sorting / Grouping Review
→ Parallel Stream Review
→ Immutability Review
→ Defensive Copy Review
→ Anti Pattern Review
```

리팩터링 후보:

```text
긴 Lambda → 이름 있는 Method
복잡한 filter → Predicate Method
map 내부 Side Effect → 변환 Method와 Side Effect 분리
forEach 결과 수집 → map + collect
Stream Repository 반복 호출 → 일괄 조회
peek 상태 변경 → 명시적 for문 / Service 흐름
parallelStream DB 호출 → Batch / Async / Queue 검토
final List 노출 → List.copyOf
mutable record component → Compact Constructor 방어적 복사
```

---

### [FAQ]

Q. Lambda 검수에서 가장 먼저 볼 것은?
A. Lambda가 짧고 의도가 명확한지, 복잡한 로직을 숨기고 있지 않은지 확인한다.

Q. Stream 검수에서 가장 중요한 것은?
A. Stream이 데이터 변환 / 필터링 목적에 맞게 사용되고 Side Effect를 남용하지 않는지 확인한다.

Q. Immutability 검수에서 가장 흔한 실수는?
A. final Field나 record를 완전 불변으로 오해하고 내부 mutable 객체를 그대로 노출하는 것이다.

---

# 12. Backend Integration

## 12.1 Spring Boot Lambda Stream Immutability Integration

### [개념]

Lambda, Stream, Immutability는 Spring Boot Backend에서 DTO 변환, 목록 응답 생성, 정책 적용, 데이터 필터링, 불변 응답 구조 설계에 사용된다.

이 파트는 Java Collection / Generic 문서와 Backend Service / DTO / Entity 설계 사이의 연결 기준이다.

---

### [핵심]

Spring Boot 연결:

```text
Repository List<Entity>
→ Stream filter / map
→ List<ResponseDto>

Service
→ 조건 분리
→ DTO 변환
→ 일괄 처리

DTO
→ record
→ immutable response

Value Object
→ final field
→ defensive copy

Policy
→ Functional Interface / Strategy
```

---

### [실무]

Repository 결과 DTO 변환:

```java
public List<UserResponse> getActiveUsers() {
    return userRepository.findAll().stream()
        .filter(User::isActive)
        .map(UserResponse::from)
        .toList();
}
```

더 좋은 DB 필터링:

```java
public List<UserResponse> getActiveUsers() {
    return userRepository.findByActiveTrue().stream()
        .map(UserResponse::from)
        .toList();
}
```

Response DTO:

```java
public record UserResponse(
    Long userId,
    String email,
    LocalDateTime createdAt
) {
    public static UserResponse from(User user) {
        return new UserResponse(
            user.getId(),
            user.getEmail(),
            user.getCreatedAt()
        );
    }
}
```

Value Object:

```java
public record Period(LocalDate startDate, LocalDate endDate) {
    public Period {
        if (startDate.isAfter(endDate)) {
            throw new IllegalArgumentException("startDate must be before endDate");
        }
    }
}
```

Service 일괄 처리:

```java
@Transactional
public void publishPosts(List<Long> postIds) {
    List<Post> posts = postRepository.findAllById(postIds);

    for (Post post : posts) {
        post.publish();
    }

    postRepository.saveAll(posts);
}
```

검토 기준:

- Repository에서 처리 가능한 필터 / 정렬을 Java Stream으로 처리하지 않는가?
- DTO 변환은 `map(Response::from)`처럼 명확한가?
- Stream 내부에서 Repository를 반복 호출하지 않는가?
- Entity 상태 변경은 Stream보다 명시적 for문이 더 적합한지 검토했는가?
- Response DTO는 record로 표현 가능한가?
- Value Object는 불변성과 검증을 함께 가지는가?
- Collection Response는 외부 수정 가능성이 필요 없는가?

주의:

- Stream으로 작성했다고 무조건 좋은 코드가 아니다.
- Service 흐름이 복잡하면 명시적 반복문이 더 낫다.
- JPA Lazy Loading과 Stream 변환 위치를 확인한다.
- API 응답 DTO의 불변성은 유지보수와 테스트에 유리하다.

---

### [FAQ]

Q. Spring Boot에서 Stream은 어디에 많이 써?
A. Repository 조회 결과를 필터링하거나 DTO List로 변환할 때 많이 사용한다.

Q. Repository에서 필터링할 수 있는데 Service Stream으로 필터링해도 돼?
A. 가능하지만 데이터가 많으면 DB Query에서 처리하는 것이 더 효율적일 수 있다.

Q. Entity 상태 변경을 Stream으로 처리해도 돼?
A. 가능은 하지만 상태 변경과 저장 흐름은 명시적 for문이 더 읽기 쉬운 경우가 많다.

---

# Retrieval Queries

### [FAQ]

Q. Lambda는 뭐야?
A. Functional Interface 구현을 간결하게 표현하는 함수형 문법이다.

Q. Lambda는 언제 써?
A. Functional Interface 구현을 짧게 표현하거나 Stream에서 조건, 변환, 정렬 로직을 전달할 때 사용한다.

Q. Lambda가 길어지면 어떻게 해?
A. 이름 있는 Method로 분리하거나 일반 반복문으로 바꾸는 것이 좋다.

Q. Functional Interface는 뭐야?
A. 추상 Method가 하나만 있는 Interface로 Lambda의 대상 타입이 된다.

Q. Predicate는 언제 써?
A. 입력값이 조건을 만족하는지 boolean으로 판단할 때 사용한다.

Q. Function은 언제 써?
A. 입력값을 다른 결과 타입으로 변환할 때 사용한다.

Q. Consumer는 언제 써?
A. 입력값을 받아 소비하고 반환값이 없을 때 사용한다.

Q. Supplier는 언제 써?
A. 입력 없이 값을 공급할 때 사용한다.

Q. Method Reference는 언제 써?
A. Lambda가 단순히 기존 Method를 호출하는 형태라면 사용한다.

Q. Lambda와 Method Reference 중 뭐가 좋아?
A. Method 이름만으로 의도가 명확하면 Method Reference가 좋고, 추가 조건이 있으면 Lambda가 좋다.

Q. Lambda에서 외부 변수를 바꿀 수 있어?
A. 지역 변수는 final 또는 effectively final이어야 하므로 재할당할 수 없다.

Q. effectively final은 뭐야?
A. final을 붙이지 않았지만 한 번 할당 후 변경되지 않는 변수다.

Q. Stream은 뭐야?
A. 데이터를 저장하지 않고 Collection 데이터를 선언형으로 처리하는 Pipeline API다.

Q. Stream은 Collection이야?
A. 아니다. Stream은 데이터를 저장하지 않고 처리 흐름을 표현하는 API다.

Q. Stream은 언제 실행돼?
A. collect, toList, forEach 같은 Terminal Operation이 호출될 때 실행된다.

Q. Stream을 한 번 더 사용할 수 있어?
A. 아니다. Stream은 한 번 소비되면 재사용할 수 없다.

Q. Intermediate Operation은 뭐야?
A. filter, map, sorted처럼 Stream 중간에서 변환이나 필터링을 수행하고 Stream을 반환하는 연산이다.

Q. Terminal Operation은 뭐야?
A. Stream을 실행하고 결과를 만들거나 Side Effect를 수행하는 마지막 연산이다.

Q. Stream filter가 바로 실행되지 않는 이유는?
A. Stream 중간 연산은 Lazy Evaluation으로 Terminal Operation이 호출될 때 실행되기 때문이다.

Q. filter는 언제 써?
A. Collection에서 조건을 만족하는 요소만 남기고 싶을 때 사용한다.

Q. filter 조건이 복잡하면 어떻게 해?
A. 의미 있는 이름의 Method로 분리하는 것이 좋다.

Q. map은 언제 써?
A. Stream 요소를 다른 값이나 타입으로 변환할 때 사용한다.

Q. Entity를 DTO로 바꿀 때 map을 써도 돼?
A. 가능하다. `map(UserResponse::from)` 형태가 자주 사용된다.

Q. map에서 DB 조회를 해도 돼?
A. 가능은 하지만 N+1이나 성능 문제가 생길 수 있어 주의해야 한다.

Q. flatMap은 언제 써?
A. 요소마다 여러 결과가 나오거나 중첩 Collection을 하나로 펼칠 때 사용한다.

Q. map과 flatMap 차이는?
A. map은 요소를 하나의 값으로 변환하고 flatMap은 여러 값을 만든 뒤 하나의 Stream으로 펼친다.

Q. JPA 연관 Collection에 flatMap을 써도 돼?
A. 가능하지만 Lazy Loading, N+1, Transaction 범위를 반드시 검토해야 한다.

Q. Stream에서 정렬은 어떻게 해?
A. sorted와 Comparator.comparing을 사용한다.

Q. null 값이 있는 정렬은 어떻게 해?
A. Comparator.nullsFirst 또는 Comparator.nullsLast를 사용한다.

Q. Stream.toList()와 Collectors.toList() 차이는?
A. Stream.toList()는 수정 불가 List를 반환한다. 수정이 필요하면 별도 mutable List 생성을 검토한다.

Q. 수집 후 add를 해야 하면 어떻게 해?
A. `Collectors.toCollection(ArrayList::new)`처럼 수정 가능한 Collection을 명시한다.

Q. toMap에서 중복 Key가 있으면 어떻게 돼?
A. merge function이 없으면 예외가 발생한다.

Q. Function.identity()는 뭐야?
A. 입력 값을 그대로 반환하는 Function이다.

Q. groupingBy는 언제 써?
A. Collection 요소를 특정 기준으로 묶고 싶을 때 사용한다.

Q. 그룹별 개수만 필요하면 어떻게 해?
A. groupingBy와 Collectors.counting을 함께 사용한다.

Q. joining은 언제 써?
A. 여러 문자열을 구분자로 연결해 하나의 문자열로 만들 때 사용한다.

Q. anyMatch는 언제 써?
A. 조건을 만족하는 요소가 하나라도 있는지 확인할 때 사용한다.

Q. allMatch는 빈 목록에서 true야?
A. 그렇다. 빈 Stream에서는 allMatch가 true를 반환한다.

Q. noneMatch는 무슨 뜻이야?
A. 조건을 만족하는 요소가 하나도 없으면 true를 반환한다.

Q. findFirst는 무엇을 반환해?
A. 조건에 맞는 첫 번째 요소를 Optional로 반환한다.

Q. findFirst 결과는 바로 get해도 돼?
A. 권장하지 않는다. orElseThrow 등으로 값 없음 상황을 처리해야 한다.

Q. Stream forEach에서 외부 List에 add해도 돼?
A. 가능은 하지만 권장하지 않는다. map과 collect로 수집하는 것이 좋다.

Q. forEach는 언제 써?
A. 각 요소에 대해 로그, 알림, 단순 작업 같은 Side Effect를 수행할 때 사용한다.

Q. Stream 안에서 save를 반복해도 돼?
A. 가능은 하지만 성능, Transaction, Batch 처리 가능성을 검토해야 한다.

Q. parallelStream을 쓰면 항상 빨라져?
A. 아니다. 작업 특성, 데이터 크기, Thread Safety에 따라 오히려 느리거나 위험할 수 있다.

Q. DB 저장을 parallelStream으로 하면 좋아?
A. 권장하지 않는다. Connection Pool, Transaction, 동시성 문제가 생길 수 있다.

Q. parallelStream은 언제 검토해?
A. 요소 간 독립적인 대량 CPU 연산이고 공유 상태가 없을 때 검토한다.

Q. Immutability는 뭐야?
A. 객체 생성 후 상태가 변경되지 않는 성질이다.

Q. final Field만 있으면 불변 객체야?
A. 아니다. 내부 객체가 mutable이면 상태가 바뀔 수 있다.

Q. 불변 객체는 왜 좋아?
A. 상태 추적이 쉽고 Thread Safety와 테스트 안정성에 유리하다.

Q. Defensive Copy는 왜 필요해?
A. 외부에서 mutable 객체를 변경해 내부 상태가 바뀌는 것을 막기 위해 필요하다.

Q. List.copyOf는 어떤 역할을 해?
A. 전달받은 List를 수정 불가 복사본으로 만든다.

Q. record는 언제 써?
A. 단순 불변 DTO나 Value Object를 간결하게 표현할 때 사용한다.

Q. record는 완전 불변이야?
A. component 참조는 final이지만 component 객체가 mutable이면 내부 상태는 바뀔 수 있다.

Q. Mutable State는 나쁜 거야?
A. 아니다. 필요한 경우가 많지만 변경 규칙과 캡슐화가 중요하다.

Q. Setter 대신 의미 있는 Method를 쓰는 이유는?
A. 상태 변경 의도와 검증 규칙을 객체 내부에 모으기 위해서다.

Q. Stream.toList 결과에 add할 수 있어?
A. 아니다. 수정 불가 List라 UnsupportedOperationException이 발생할 수 있다.

Q. Pure Function은 뭐야?
A. 같은 입력에 항상 같은 출력을 반환하고 외부 상태를 변경하지 않는 함수다.

Q. Stream map에는 어떤 Method가 좋아?
A. Side Effect 없이 값을 변환하는 Method가 좋다.

Q. Lambda 조건식이 복잡하면 어떻게 해?
A. 의미 있는 이름의 Method로 분리한다.

Q. Stream 안에서 Repository를 호출하면 안 돼?
A. 가능은 하지만 N+1과 성능 문제가 생기기 쉬워 일괄 조회를 우선 검토한다.

Q. peek으로 상태 변경을 해도 돼?
A. 권장하지 않는다. peek은 디버깅 목적에 가깝고 비즈니스 로직은 명시적으로 작성하는 것이 좋다.

Q. final List는 불변이야?
A. 아니다. List 참조 재할당만 막고 내부 요소 추가 / 삭제는 가능할 수 있다.

Q. 내부 Collection을 안전하게 보관하려면?
A. 생성자에서 List.copyOf 같은 방어적 복사를 사용한다.

Q. Lambda 검수에서 가장 먼저 볼 것은?
A. Lambda가 짧고 의도가 명확한지, 복잡한 로직을 숨기고 있지 않은지 확인한다.

Q. Stream 검수에서 가장 중요한 것은?
A. Stream이 데이터 변환 / 필터링 목적에 맞게 사용되고 Side Effect를 남용하지 않는지 확인한다.

Q. Spring Boot에서 Stream은 어디에 많이 써?
A. Repository 조회 결과를 필터링하거나 DTO List로 변환할 때 많이 사용한다.

Q. Repository에서 필터링할 수 있는데 Service Stream으로 필터링해도 돼?
A. 가능하지만 데이터가 많으면 DB Query에서 처리하는 것이 더 효율적일 수 있다.

Q. Java Part07 다음 문서는 뭐야?
A. Java Part08 — Backend Code Review & Anti Pattern 문서로 이어지는 것이 좋다.
