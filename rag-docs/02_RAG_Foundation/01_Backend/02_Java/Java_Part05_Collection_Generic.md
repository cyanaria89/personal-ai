# Java Part05 — Collection and Generic

---

# 1. Collection Framework Foundation

## 1.1 Collection Framework Purpose

### [개념]

Collection Framework는 여러 데이터를 저장, 조회, 순회, 변환, 삭제하기 위한 Java 표준 자료구조 API다.

Collection Framework는 Backend Agent / Review Agent가 Java 백엔드 코드에서 데이터 특성에 맞는 자료구조를 선택하고 검토하기 위한 핵심 기준이다.

Spring Boot, JPA, DTO, API Response, Service Logic, Stream API는 Collection Framework와 자주 연결된다.

```java
List<String> names = new ArrayList<>();
Set<Long> userIds = new HashSet<>();
Map<Long, User> userMap = new HashMap<>();
```

---

### [핵심]

Collection Framework 핵심:

- Collection Framework
- Collection
- List
- Set
- Map
- Queue
- Deque
- ArrayList
- LinkedList
- HashSet
- LinkedHashSet
- TreeSet
- HashMap
- LinkedHashMap
- TreeMap
- Iterator
- Iterable
- Generic
- equals
- hashCode

기본 선택 기준:

```text
순서가 중요하고 중복 허용 → List
중복 제거가 중요 → Set
Key-Value 조회가 중요 → Map
삽입 순서 유지 Set → LinkedHashSet
정렬된 Set → TreeSet
빠른 Key 조회 → HashMap
삽입 순서 유지 Map → LinkedHashMap
정렬된 Key → TreeMap
FIFO 처리 → Queue
양방향 삽입 / 삭제 → Deque
```

---

### [실무]

2026 백엔드 실무에서 Collection 선택은 성능, 가독성, 중복 처리, API 응답 구조, DB 조회 결과 처리에 직접 영향을 준다.

Collection 선택 Flow:

```text
데이터가 여러 개인가?
→ 순서가 중요한가?
→ 중복을 허용하는가?
→ Key 기반 조회가 필요한가?
→ 정렬이 필요한가?
→ 삽입 순서 유지가 필요한가?
→ 수정 가능해야 하는가?
→ Thread Safety가 필요한가?
→ Collection 선택
```

Spring Boot 연결:

```text
Repository 조회 결과 → List<Entity>
API 목록 응답 → List<ResponseDto>
중복 제거 ID 목록 → Set<Long>
조회 최적화용 캐시 Map → Map<Long, Entity>
Enum별 전략 조회 → Map<Enum, Strategy>
Queue 기반 작업 처리 → Queue<Task>
```

주의:

- 모든 목록을 무조건 List로 처리하지 않는다.
- 중복 제거 목적이면 Set을 검토한다.
- Key 조회가 반복되면 Map 변환을 검토한다.
- Collection 반환은 null보다 empty collection을 권장한다.
- JPA Entity Collection은 Lazy Loading, Cascade, orphanRemoval을 함께 고려한다.
- equals / hashCode 구현은 Hash 기반 Collection 동작에 직접 영향을 준다.

---

### [FAQ]

Q. Collection Framework는 왜 중요해?
A. 여러 데이터를 다루는 Java 백엔드 코드에서 자료구조 선택, 중복 처리, 조회 성능, API 응답 구조에 직접 영향을 주기 때문이다.

Q. List, Set, Map 중 무엇을 써야 해?
A. 순서와 중복이 필요하면 List, 중복 제거가 필요하면 Set, Key 기반 조회가 필요하면 Map을 사용한다.

Q. Collection 반환값은 null이 좋아 empty collection이 좋아?
A. 대부분 empty collection이 좋다. 호출자가 null check를 덜 해도 된다.

---

## 1.2 Collection Interface Hierarchy

### [개념]

Collection Framework는 Interface와 구현 Class로 구성된다.

Interface는 사용 목적을 표현하고 구현 Class는 실제 저장 방식과 성능 특성을 결정한다.

---

### [핵심]

주요 구조:

```text
Iterable
└ Collection
  ├ List
  ├ Set
  └ Queue

Map
└ Key-Value 구조
```

주요 Interface:

- Iterable
- Collection
- List
- Set
- Queue
- Deque
- Map

주요 구현체:

- ArrayList
- LinkedList
- HashSet
- LinkedHashSet
- TreeSet
- HashMap
- LinkedHashMap
- TreeMap
- ArrayDeque
- PriorityQueue

---

### [실무]

변수 선언은 구현체보다 Interface 타입을 우선 사용한다.

좋은 예:

```java
List<User> users = new ArrayList<>();
Set<Long> userIds = new HashSet<>();
Map<Long, User> userMap = new HashMap<>();
```

나쁜 예:

```java
ArrayList<User> users = new ArrayList<>();
HashMap<Long, User> userMap = new HashMap<>();
```

Interface 타입 사용 장점:

```text
구현체 교체 쉬움
Method 의도 명확
API 결합도 감소
테스트와 리팩터링 유리
```

주의:

- 구현체 고유 Method가 필요하면 구현체 타입 선언이 필요할 수 있다.
- API Return Type은 가능한 넓은 Interface로 반환한다.
- 내부 구현은 요구사항에 맞는 구현체를 선택한다.
- Map은 Collection을 상속하지 않는 별도 구조다.

---

### [FAQ]

Q. 변수 타입은 ArrayList로 써야 해 List로 써야 해?
A. 대부분 List 같은 Interface 타입으로 선언하고 구현체는 ArrayList 등으로 선택하는 것이 좋다.

Q. Map은 Collection이야?
A. Java 구조상 Map은 Collection Interface를 상속하지 않는 별도 Key-Value 구조다.

Q. 구현체 타입을 직접 써야 하는 경우도 있어?
A. 구현체 고유 기능이 필요하면 사용할 수 있지만 일반적으로 Interface 타입을 우선 검토한다.

---

# 2. List Rules

## 2.1 List Purpose

### [개념]

List는 순서가 있고 중복을 허용하는 Collection이다.

인덱스 기반 접근이 가능하며 API 목록 응답, Repository 조회 결과, 정렬된 데이터 처리에 자주 사용된다.

```java
List<String> names = new ArrayList<>();
names.add("java");
names.add("spring");
names.add("java");
```

---

### [핵심]

List 핵심:

- List
- Ordered Collection
- Duplicate Allowed
- Index Access
- ArrayList
- LinkedList
- get
- add
- remove
- contains
- sort
- iteration

List 적합 상황:

```text
순서가 중요하다.
중복 데이터가 허용된다.
API 목록 응답이 필요하다.
정렬된 결과를 유지해야 한다.
인덱스 기반 접근이 필요하다.
Repository 조회 결과를 담는다.
```

---

### [실무]

Spring Boot 실무 사용 예:

```java
List<UserResponse> responses = users.stream()
    .map(UserResponse::from)
    .toList();
```

Repository 결과:

```java
List<Post> posts = postRepository.findByUserId(userId);
```

권장:

- 목록 응답은 List<ResponseDto> 사용.
- 순서가 중요한 데이터는 List 사용.
- 정렬은 DB Order By 또는 Java sort 기준 명확화.
- 중복 제거가 필요하면 Set 전환 검토.
- 읽기 전용 반환은 unmodifiable list 검토.

주의:

- List.contains는 데이터가 많으면 비용 증가.
- 중복 제거 목적에 List만 사용하지 않는다.
- 인덱스 접근이 많으면 LinkedList보다 ArrayList가 보통 적합.
- JPA Repository에서 List 반환은 empty List 가능성이 일반적이다.

---

### [FAQ]

Q. List는 언제 써?
A. 순서가 중요하고 중복을 허용하는 목록 데이터에 사용한다.

Q. List는 중복을 허용해?
A. 허용한다. 같은 값이나 객체가 여러 번 들어갈 수 있다.

Q. API 목록 응답은 보통 어떤 타입이 좋아?
A. 보통 List<ResponseDto>를 사용한다.

---

## 2.2 ArrayList Rules

### [개념]

ArrayList는 내부적으로 배열 기반으로 동작하는 List 구현체다.

인덱스 조회가 빠르고 일반적인 목록 처리에 가장 많이 사용된다.

---

### [핵심]

ArrayList 핵심:

- ArrayList
- Dynamic Array
- Index Access
- Fast Read
- Append
- Resize
- Random Access
- List Implementation

성능 특성:

```text
인덱스 조회 → 빠름
끝에 추가 → 보통 빠름
중간 삽입 / 삭제 → 비용 발생
contains → 순차 탐색
```

---

### [실무]

기본 List 구현체로 ArrayList를 우선 검토한다.

예:

```java
List<Long> userIds = new ArrayList<>();
```

적합:

```text
일반 목록 저장
API 응답 목록 생성
조회 위주 목록
Stream 결과 수집
DTO List 생성
```

주의:

- 중간 삽입 / 삭제가 매우 많으면 비용이 커질 수 있다.
- contains가 반복되면 Set 전환을 검토한다.
- 대량 데이터 처리 시 초기 용량 설정을 검토할 수 있다.
- Thread Safe하지 않다.

초기 용량 예:

```java
List<UserResponse> responses = new ArrayList<>(users.size());
```

---

### [FAQ]

Q. ArrayList는 언제 써?
A. 일반적인 목록 저장과 조회 위주 처리에 기본 선택지로 많이 사용한다.

Q. ArrayList는 조회가 빠른가?
A. 인덱스 기반 조회는 빠르다.

Q. ArrayList에서 중간 삭제가 많으면 어때?
A. 뒤 요소들을 이동해야 하므로 비용이 커질 수 있다.

---

## 2.3 LinkedList Rules

### [개념]

LinkedList는 노드가 앞뒤로 연결된 구조의 List 구현체다.

Java LinkedList는 List와 Deque를 모두 구현한다.

---

### [핵심]

LinkedList 핵심:

- LinkedList
- Node
- List
- Deque
- Sequential Access
- Add First
- Add Last
- Remove First
- Remove Last

특성:

```text
인덱스 조회 → 느릴 수 있음
앞 / 뒤 삽입 삭제 → 가능
메모리 오버헤드 → 노드 참조로 증가
Deque 기능 → 사용 가능
```

---

### [실무]

LinkedList는 일반 List 기본 선택지로는 신중하게 사용한다.

적합 가능 상황:

```text
Deque 기능이 필요하다.
앞 / 뒤에서 삽입 삭제가 많다.
Queue처럼 사용한다.
```

하지만 Queue / Deque 목적이면 ArrayDeque가 더 적합한 경우가 많다.

주의:

- 일반 목록 조회에는 ArrayList가 보통 더 적합하다.
- 인덱스 접근이 많은 코드에서 LinkedList는 비효율적일 수 있다.
- 메모리 오버헤드가 있다.
- 단순히 삽입 / 삭제가 많다는 이유만으로 LinkedList를 선택하지 않는다.
- 실제 병목과 접근 패턴을 기준으로 판단한다.

---

### [FAQ]

Q. LinkedList는 언제 써?
A. 앞 / 뒤 삽입 삭제나 Deque 기능이 필요한 경우 검토할 수 있다.

Q. 일반 List는 ArrayList와 LinkedList 중 뭐가 좋아?
A. 대부분 ArrayList가 기본 선택지로 적합하다.

Q. LinkedList는 인덱스 조회가 빠른가?
A. 아니다. 노드를 순차적으로 찾아야 하므로 느릴 수 있다.

---

## 2.4 List Anti Pattern Rules

### [개념]

List Anti Pattern은 모든 다중 데이터를 List로만 처리해 중복, 조회 성능, 의미 표현 문제가 생기는 패턴이다.

---

### [핵심]

List Anti Pattern:

- 모든 Collection을 List로 처리
- 중복 제거가 필요한데 List 사용
- contains 반복 호출
- Key 조회를 List 순회로 처리
- null List 반환
- 내부 mutable List 직접 노출
- for-each 중 remove
- 정렬 기준 불명확

---

### [실무]

나쁜 예:

```java
for (Long id : ids) {
    if (allowedIds.contains(id)) {
        result.add(id);
    }
}
```

개선:

```java
Set<Long> allowedIdSet = new HashSet<>(allowedIds);

for (Long id : ids) {
    if (allowedIdSet.contains(id)) {
        result.add(id);
    }
}
```

Key 조회 나쁜 예:

```java
public User findUser(List<User> users, Long userId) {
    return users.stream()
        .filter(user -> Objects.equals(user.getId(), userId))
        .findFirst()
        .orElseThrow();
}
```

Map 변환 개선:

```java
Map<Long, User> userMap = users.stream()
    .collect(Collectors.toMap(User::getId, Function.identity()));
```

주의:

- 중복 제거는 Set.
- Key 조회 반복은 Map.
- 목록 순서가 중요하면 정렬 기준 명시.
- 내부 List를 그대로 반환하지 않는다.
- List 반환은 empty List 권장.

---

### [FAQ]

Q. 모든 목록을 List로 처리하면 안 돼?
A. List가 적합한 경우도 많지만 중복 제거는 Set, Key 조회는 Map이 더 적합하다.

Q. List.contains를 반복하면 왜 문제야?
A. List는 순차 탐색이라 데이터가 많으면 비용이 커질 수 있다.

Q. List 반환값이 없으면 null을 반환해도 돼?
A. 대부분 empty List를 반환하는 것이 좋다.

---

# 3. Set Rules

## 3.1 Set Purpose

### [개념]

Set은 중복을 허용하지 않는 Collection이다.

데이터의 유일성이 중요하거나 중복 제거가 필요한 경우 사용한다.

```java
Set<Long> userIds = new HashSet<>();
userIds.add(1L);
userIds.add(1L);
userIds.add(2L);
```

---

### [핵심]

Set 핵심:

- Set
- Unique Element
- Duplicate Not Allowed
- HashSet
- LinkedHashSet
- TreeSet
- equals
- hashCode
- contains
- distinct

Set 적합 상황:

```text
중복 제거가 필요하다.
유일한 ID 목록이 필요하다.
포함 여부를 빠르게 확인해야 한다.
중복 입력을 방지해야 한다.
객체 동등성 기준이 명확하다.
```

---

### [실무]

ID 중복 제거:

```java
Set<Long> userIds = new HashSet<>(request.userIds());
```

포함 여부 확인:

```java
if (userIds.contains(targetUserId)) {
    return true;
}
```

Stream distinct 대안:

```java
List<Long> distinctIds = ids.stream()
    .distinct()
    .toList();
```

실무 기준:

- 중복 제거 목적이면 Set 우선 검토.
- contains 반복 조회는 Set이 List보다 적합한 경우가 많다.
- 객체 Set은 equals / hashCode 기준을 확인한다.
- 순서 유지가 필요하면 LinkedHashSet 검토.
- 정렬이 필요하면 TreeSet 검토.

주의:

- HashSet은 순서를 보장하지 않는다.
- 객체 중복 기준은 equals / hashCode에 의존한다.
- mutable Field를 equals / hashCode 기준으로 쓰면 위험하다.
- JPA Entity를 Set에 넣을 때 식별자 생성 시점과 동등성 기준을 주의한다.

---

### [FAQ]

Q. Set은 언제 써?
A. 중복 제거나 유일한 값 집합이 필요할 때 사용한다.

Q. Set은 순서를 보장해?
A. HashSet은 순서를 보장하지 않는다. 순서 유지가 필요하면 LinkedHashSet을 검토한다.

Q. 객체 Set에서 중복 기준은 뭐야?
A. equals와 hashCode 구현 기준에 따라 중복 여부가 결정된다.

---

## 3.2 HashSet Rules

### [개념]

HashSet은 Hash 기반으로 중복을 제거하는 Set 구현체다.

빠른 contains, add, remove를 제공하지만 순서를 보장하지 않는다.

---

### [핵심]

HashSet 핵심:

- HashSet
- Hash Table
- hashCode
- equals
- Unique Element
- Fast Lookup
- No Ordering
- Contains

특성:

```text
중복 제거 → 좋음
포함 여부 조회 → 빠름
순서 보장 → 없음
동등성 기준 → equals / hashCode
```

---

### [실무]

예:

```java
Set<String> tags = new HashSet<>();
tags.add("java");
tags.add("spring");
tags.add("java");
```

실무 적용:

```text
권한 코드 중복 제거
사용자 ID 중복 제거
이미 처리한 ID 기록
허용 목록 포함 여부 확인
태그 중복 제거
```

주의:

- 순서가 필요한 API 응답에 HashSet 직접 사용 주의.
- equals / hashCode가 잘못되면 중복 제거가 실패한다.
- mutable 객체를 HashSet에 넣은 뒤 hashCode 기준 Field를 바꾸면 검색 실패 가능.
- null 허용 여부는 구현체별 특성을 확인한다.

---

### [FAQ]

Q. HashSet은 순서를 보장해?
A. 아니다. 순서가 필요하면 LinkedHashSet이나 List 정렬을 검토한다.

Q. HashSet이 중복 제거를 어떻게 판단해?
A. hashCode와 equals 결과를 기준으로 판단한다.

Q. HashSet에 mutable 객체를 넣어도 돼?
A. 가능하지만 equals / hashCode 기준 Field가 바뀌면 문제가 생길 수 있어 주의해야 한다.

---

## 3.3 LinkedHashSet and TreeSet Rules

### [개념]

LinkedHashSet은 삽입 순서를 유지하는 Set이다.

TreeSet은 정렬된 순서를 유지하는 Set이다.

---

### [핵심]

LinkedHashSet 핵심:

- LinkedHashSet
- Insertion Order
- Unique Element
- Predictable Iteration

TreeSet 핵심:

- TreeSet
- Sorted Set
- Natural Ordering
- Comparator
- Comparable
- Unique Element

---

### [실무]

LinkedHashSet 예:

```java
Set<Long> ids = new LinkedHashSet<>();
ids.add(3L);
ids.add(1L);
ids.add(2L);
```

TreeSet 예:

```java
Set<String> names = new TreeSet<>();
names.add("kim");
names.add("lee");
names.add("park");
```

선택 기준:

```text
중복 제거만 필요 → HashSet
중복 제거 + 삽입 순서 유지 → LinkedHashSet
중복 제거 + 정렬 순서 유지 → TreeSet
```

주의:

- TreeSet은 정렬 기준이 필요하다.
- TreeSet의 중복 판단은 정렬 비교 결과와 관련된다.
- Comparator가 equals와 일관되지 않으면 혼란이 생길 수 있다.
- 정렬 비용이 필요 없는 경우 TreeSet은 과할 수 있다.

---

### [FAQ]

Q. LinkedHashSet은 언제 써?
A. 중복을 제거하면서 입력 순서를 유지해야 할 때 사용한다.

Q. TreeSet은 언제 써?
A. 중복을 제거하면서 정렬된 순서가 필요할 때 사용한다.

Q. TreeSet은 equals로 중복을 판단해?
A. 정렬 비교 기준에 의해 동일하다고 판단되면 중복으로 처리될 수 있어 Comparator 일관성을 주의해야 한다.

---

# 4. Map Rules

## 4.1 Map Purpose

### [개념]

Map은 Key와 Value를 한 쌍으로 저장하는 자료구조다.

Key를 통해 Value를 빠르게 조회할 수 있다.

```java
Map<Long, User> userMap = new HashMap<>();
userMap.put(1L, user);
User found = userMap.get(1L);
```

---

### [핵심]

Map 핵심:

- Map
- Key
- Value
- Entry
- HashMap
- LinkedHashMap
- TreeMap
- get
- put
- containsKey
- keySet
- values
- entrySet
- Duplicate Key
- Key Lookup

Map 적합 상황:

```text
Key 기반 조회가 필요하다.
ID로 Entity를 빠르게 찾는다.
Enum으로 Strategy를 찾는다.
그룹핑 결과를 저장한다.
캐시 구조가 필요하다.
중복 Key 처리 기준이 있다.
```

---

### [실무]

List를 Map으로 변환:

```java
Map<Long, User> userMap = users.stream()
    .collect(Collectors.toMap(User::getId, Function.identity()));
```

Enum 전략 Map:

```java
Map<DiscountType, DiscountPolicy> policyMap = policies.stream()
    .collect(Collectors.toMap(DiscountPolicy::type, Function.identity()));
```

조회:

```java
User user = userMap.get(userId);

if (user == null) {
    throw new UserNotFoundException(userId);
}
```

실무 기준:

- 반복적인 Key 조회는 Map 변환 검토.
- 중복 Key 가능성을 반드시 확인.
- Key는 불변이거나 변경되지 않는 값이 적합.
- Enum Key는 EnumMap 검토 가능.
- 순서가 필요하면 LinkedHashMap.
- 정렬 Key가 필요하면 TreeMap.

주의:

- Map.get 결과는 null일 수 있다.
- Key가 없어서 null인지 Value가 null인지 구분이 필요할 수 있다.
- Collectors.toMap은 중복 Key 발생 시 예외가 발생한다.
- mutable 객체를 Key로 쓰는 것은 위험하다.

---

### [FAQ]

Q. Map은 언제 써?
A. Key로 값을 빠르게 찾거나 그룹핑 결과를 저장할 때 사용한다.

Q. List를 Map으로 바꾸는 이유는?
A. 반복적인 검색을 줄이고 Key 기반 조회를 빠르게 하기 위해서다.

Q. Map.get 결과가 null이면 무조건 값이 없는 거야?
A. 보통은 그렇지만 Value 자체가 null일 수도 있어 containsKey가 필요한 경우가 있다.

---

## 4.2 HashMap Rules

### [개념]

HashMap은 Hash 기반 Key-Value 저장 구조다.

Key 기반 조회가 빠르고 가장 일반적으로 사용하는 Map 구현체다.

---

### [핵심]

HashMap 핵심:

- HashMap
- Hash Table
- Key
- Value
- hashCode
- equals
- Fast Lookup
- No Ordering
- Duplicate Key Override

특성:

```text
Key 조회 → 빠름
순서 보장 → 없음
중복 Key → 기존 Value 대체
Key 동등성 → equals / hashCode
```

---

### [실무]

예:

```java
Map<Long, String> nicknameMap = new HashMap<>();
nicknameMap.put(1L, "kim");
nicknameMap.put(2L, "lee");
```

중복 Key 처리:

```java
nicknameMap.put(1L, "park");
```

Stream toMap 중복 Key 처리:

```java
Map<Long, User> userMap = users.stream()
    .collect(Collectors.toMap(
        User::getId,
        Function.identity(),
        (existing, replacement) -> existing
    ));
```

주의:

- 순서가 필요한 응답에는 HashMap 직접 순회 주의.
- Key 객체의 equals / hashCode가 중요하다.
- Key로 mutable 객체 사용 금지에 가깝게 검토.
- Thread Safe하지 않다.
- null Key / null Value 허용 여부는 코드 정책상 제한할 수 있다.

---

### [FAQ]

Q. HashMap은 순서를 보장해?
A. 아니다. 순서가 필요하면 LinkedHashMap이나 TreeMap을 검토한다.

Q. 같은 Key로 put하면 어떻게 돼?
A. 기존 Value가 새 Value로 대체된다.

Q. HashMap Key는 어떤 값이 좋아?
A. 불변이고 equals / hashCode 기준이 안정적인 값이 좋다.

---

## 4.3 LinkedHashMap and TreeMap Rules

### [개념]

LinkedHashMap은 삽입 순서를 유지하는 Map이다.

TreeMap은 Key 정렬 순서를 유지하는 Map이다.

---

### [핵심]

LinkedHashMap 핵심:

- LinkedHashMap
- Insertion Order
- Predictable Iteration
- Ordered Response

TreeMap 핵심:

- TreeMap
- Sorted Key
- Natural Ordering
- Comparator
- NavigableMap

---

### [실무]

LinkedHashMap 예:

```java
Map<String, Integer> scores = new LinkedHashMap<>();
scores.put("java", 10);
scores.put("spring", 20);
```

TreeMap 예:

```java
Map<LocalDate, List<Event>> eventsByDate = new TreeMap<>();
```

선택 기준:

```text
Key 조회만 필요 → HashMap
삽입 순서 유지 필요 → LinkedHashMap
Key 정렬 필요 → TreeMap
Enum Key → EnumMap 검토
```

주의:

- TreeMap은 Key 정렬 비용이 있다.
- TreeMap Key는 Comparable이거나 Comparator가 필요하다.
- LinkedHashMap은 API 응답 순서 유지에 유용할 수 있다.
- 정렬은 DB에서 하는 것이 더 적합한 경우도 많다.

---

### [FAQ]

Q. LinkedHashMap은 언제 써?
A. Key-Value 구조에서 삽입 순서를 유지해야 할 때 사용한다.

Q. TreeMap은 언제 써?
A. Key 기준 정렬 순서가 필요한 경우 사용한다.

Q. API 응답 순서를 유지하려면 어떤 Map이 좋아?
A. 삽입 순서가 중요하면 LinkedHashMap을 검토한다.

---

## 4.4 Map Anti Pattern Rules

### [개념]

Map Anti Pattern은 Key-Value 구조를 잘못 사용해 타입 안정성 저하, 중복 Key 오류, 의미 불명확 문제가 발생하는 패턴이다.

---

### [핵심]

Map Anti Pattern:

- Map<String, Object> 남용
- Object Value Casting
- 중복 Key 처리 누락
- mutable Key 사용
- 순서가 필요한데 HashMap 사용
- get null 처리 누락
- 복잡한 도메인 객체를 Map으로 대체
- Magic String Key 사용
- DTO 대신 Map 반환

---

### [실무]

나쁜 예:

```java
Map<String, Object> response = new HashMap<>();
response.put("userId", 1L);
response.put("email", "user@example.com");
```

좋은 예:

```java
public record UserResponse(
    Long userId,
    String email
) {
}
```

나쁜 예:

```java
String email = (String) data.get("email");
```

주의:

- API Response는 DTO 우선.
- Map<String, Object>는 타입 안정성이 낮다.
- Magic String Key는 오타에 취약하다.
- 복잡한 구조는 Class / DTO / Value Object로 표현한다.
- 중복 Key 가능성은 merge function으로 명시한다.

---

### [FAQ]

Q. Map<String, Object>로 응답을 만들어도 돼?
A. 가능하지만 타입 안정성이 낮아 DTO를 우선 검토하는 것이 좋다.

Q. Map에서 Object Value를 꺼내 캐스팅하면 왜 위험해?
A. 실제 타입이 다르면 ClassCastException이 발생할 수 있다.

Q. 중복 Key가 있는 Stream toMap은 어떻게 처리해?
A. merge function을 명시하거나 사전에 중복을 제거해야 한다.

---

# 5. Queue and Deque Rules

## 5.1 Queue Purpose

### [개념]

Queue는 먼저 들어온 요소를 먼저 처리하는 FIFO 구조를 표현하는 Collection이다.

작업 대기열, 순차 처리, 탐색 알고리즘 등에 사용할 수 있다.

```java
Queue<Task> queue = new ArrayDeque<>();
queue.offer(task);
Task next = queue.poll();
```

---

### [핵심]

Queue 핵심:

- Queue
- FIFO
- offer
- poll
- peek
- ArrayDeque
- PriorityQueue
- Task Queue
- Processing Order

주요 Method:

```text
offer → 추가
poll → 제거하면서 반환
peek → 제거하지 않고 확인
```

---

### [실무]

Queue 적합 상황:

```text
작업 순차 처리
BFS 탐색
이벤트 임시 대기
메시지 처리 전 임시 Buffer
우선순위 처리
```

예:

```java
Queue<Task> queue = new ArrayDeque<>();

while (!queue.isEmpty()) {
    Task task = queue.poll();
    process(task);
}
```

주의:

- 서버 간 메시징은 Java Queue보다 Message Queue 시스템 검토.
- 대규모 비동기 처리는 Kafka, RabbitMQ, Redis Stream 등 별도 도구 고려.
- Thread Safe Queue가 필요한지 확인.
- poll 결과는 null일 수 있다.
- 우선순위가 필요하면 PriorityQueue 검토.

---

### [FAQ]

Q. Queue는 언제 써?
A. 먼저 들어온 작업을 먼저 처리하는 FIFO 구조가 필요할 때 사용한다.

Q. poll과 peek 차이는?
A. poll은 요소를 제거하면서 반환하고 peek은 제거하지 않고 확인한다.

Q. 서버 메시징도 Java Queue로 처리하면 돼?
A. 단일 프로세스 내부 임시 처리에는 가능하지만 분산 메시징은 전용 Message Queue를 검토해야 한다.

---

## 5.2 Deque Rules

### [개념]

Deque는 양쪽 끝에서 삽입과 삭제가 가능한 자료구조다.

Queue와 Stack 양쪽 용도로 사용할 수 있다.

---

### [핵심]

Deque 핵심:

- Deque
- Double Ended Queue
- ArrayDeque
- addFirst
- addLast
- pollFirst
- pollLast
- Stack Replacement
- FIFO
- LIFO

---

### [실무]

ArrayDeque 사용 예:

```java
Deque<String> stack = new ArrayDeque<>();
stack.push("A");
stack.push("B");

String value = stack.pop();
```

Queue처럼 사용:

```java
Deque<Task> queue = new ArrayDeque<>();
queue.offerLast(task);
Task next = queue.pollFirst();
```

실무 기준:

- Stack 대신 ArrayDeque 검토.
- Queue 구현체로 ArrayDeque 검토.
- 양방향 처리 필요 시 Deque 사용.
- null 요소 사용은 피한다.

주의:

- Stack Class는 Legacy 성격이 강해 신규 코드에서는 ArrayDeque를 우선 검토.
- Thread Safe하지 않다.
- Deque 사용 목적이 Queue인지 Stack인지 이름으로 명확히 표현한다.

---

### [FAQ]

Q. Deque는 언제 써?
A. 양쪽 끝에서 삽입 / 삭제가 필요하거나 Stack / Queue 용도로 사용할 때 쓴다.

Q. Stack 대신 뭘 쓰는 게 좋아?
A. 신규 코드는 Stack보다 ArrayDeque를 우선 검토한다.

Q. ArrayDeque는 Thread Safe해?
A. 아니다. 동시성 환경에서는 별도 동시성 Collection을 검토해야 한다.

---

# 6. equals and hashCode Rules

## 6.1 equals and hashCode Purpose

### [개념]

equals와 hashCode는 객체 동등성 비교와 Hash 기반 Collection 동작에 사용된다.

HashSet, HashMap, distinct, contains 같은 동작은 equals와 hashCode 구현에 영향을 받는다.

---

### [핵심]

equals / hashCode 핵심:

- equals
- hashCode
- Object Equality
- Logical Equality
- HashSet
- HashMap
- contains
- distinct
- Value Object
- Entity Identity
- Contract

규칙:

```text
equals를 override하면 hashCode도 함께 override한다.
equals가 true인 객체는 hashCode도 같아야 한다.
hashCode가 같아도 equals가 true일 필요는 없다.
동등성 기준 Field는 가능하면 변경되지 않아야 한다.
```

---

### [실무]

Value Object 예:

```java
public final class Email {
    private final String value;

    public Email(String value) {
        this.value = Objects.requireNonNull(value, "value must not be null");
    }

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
}
```

record 활용:

```java
public record Email(String value) {
}
```

주의:

- equals만 override하고 hashCode를 누락하면 HashSet / HashMap에서 문제가 생긴다.
- mutable Field를 hashCode 기준으로 사용하면 위험하다.
- Entity의 equals / hashCode는 식별자 생성 전후를 고려해야 한다.
- Lombok @EqualsAndHashCode 사용 시 포함 Field를 검토한다.

---

### [FAQ]

Q. equals와 hashCode는 왜 같이 구현해?
A. HashSet, HashMap 같은 Hash 기반 Collection에서 객체 동등성 기준을 일관되게 유지하기 위해서다.

Q. equals만 override하면 안 돼?
A. 안 된다. Hash 기반 Collection에서 같은 객체로 인식되지 않는 문제가 생길 수 있다.

Q. record는 equals와 hashCode를 자동으로 만들어?
A. 그렇다. record component 기준으로 equals와 hashCode를 자동 생성한다.

---

## 6.2 Value Object Equality Rules

### [개념]

Value Object는 식별자보다 값 자체가 중요한 객체다.

Value Object는 모든 의미 있는 Field가 같으면 같은 객체로 취급한다.

---

### [핵심]

Value Object Equality 핵심:

- Value Object
- Value Equality
- Immutable
- equals
- hashCode
- record
- Defensive Copy
- No Identity

Value Object 예:

```text
Email
Money
Period
Address
PhoneNumber
Coordinate
```

---

### [실무]

Value Object는 불변으로 설계하고 값 기준 equals / hashCode를 구현한다.

예:

```java
public record Period(LocalDate startDate, LocalDate endDate) {
    public Period {
        if (startDate.isAfter(endDate)) {
            throw new IllegalArgumentException("startDate must be before endDate");
        }
    }
}
```

Set 사용 예:

```java
Set<Email> emails = new HashSet<>();
emails.add(new Email("a@example.com"));
emails.add(new Email("a@example.com"));
```

실무 기준:

- 값이 같으면 같은 객체로 판단.
- 불변 객체로 설계.
- record 사용 검토.
- Collection Field가 있으면 방어적 복사 필요.
- 도메인 의미와 검증을 함께 보유.

주의:

- Entity와 Value Object 동등성 기준을 혼동하지 않는다.
- mutable Value Object는 Hash 기반 Collection에서 위험하다.
- JPA Embeddable과 연결할 경우 기본 생성자 등 제약 확인.

---

### [FAQ]

Q. Value Object의 equals 기준은 뭐야?
A. 식별자가 아니라 객체가 가진 값이 같으면 같은 것으로 본다.

Q. Value Object는 왜 불변이 좋아?
A. 값 기준 동등성이 안정적으로 유지되고 Hash 기반 Collection에서 안전하기 때문이다.

Q. Value Object에 record를 써도 돼?
A. 단순 불변 값 객체라면 record가 적합할 수 있다.

---

## 6.3 Entity Equality Rules

### [개념]

Entity는 식별자를 기준으로 구분되는 객체다.

JPA Entity의 equals / hashCode는 ID 생성 시점, 영속성 상태, Proxy를 고려해야 한다.

---

### [핵심]

Entity Equality 핵심:

- Entity
- Identity
- ID
- Persistence Context
- JPA Proxy
- Generated ID
- equals
- hashCode
- Lifecycle
- Transient Entity

검토 기준:

```text
ID가 언제 생성되는가?
영속화 전 객체 비교가 필요한가?
Proxy Class와 비교가 가능한가?
Set에 Entity를 넣는가?
equals / hashCode 기준 Field가 변경될 수 있는가?
```

---

### [실무]

주의 대상:

```java
@Entity
public class User {
    @Id
    @GeneratedValue
    private Long id;
}
```

ID 기반 equals는 영속화 전 id가 null일 수 있다.

실무 기준:

- Entity equals / hashCode는 팀 기준을 통일한다.
- Set 연관관계 사용 시 동등성 기준을 특히 주의한다.
- 식별자 생성 전 객체를 HashSet에 넣는 것은 위험할 수 있다.
- 비즈니스 키 기반 동등성은 변경 가능성 확인.
- Lombok @EqualsAndHashCode를 Entity에 무분별하게 사용하지 않는다.

주의:

- 모든 Field를 equals에 포함하면 Lazy Loading, 순환 참조, 성능 문제가 생길 수 있다.
- Entity는 Value Object와 다르다.
- JPA Proxy와 Class 비교 방식에 주의한다.
- Entity 동등성은 JPA Domain Rules에서 더 자세히 다룬다.

---

### [FAQ]

Q. Entity equals는 Value Object처럼 모든 Field로 비교해도 돼?
A. 권장하지 않는다. Entity는 식별자와 영속성 생명주기를 고려해야 한다.

Q. JPA Entity에 Lombok @EqualsAndHashCode를 써도 돼?
A. 무분별하게 사용하면 Lazy Loading, 순환 참조, 식별자 문제를 만들 수 있어 주의해야 한다.

Q. Entity를 HashSet에 넣을 때 뭐가 위험해?
A. hashCode 기준 값이 나중에 바뀌면 Set에서 객체를 찾지 못할 수 있다.

---

# 7. Generic Foundation

## 7.1 Generic Purpose

### [개념]

Generic은 Class, Interface, Method에서 사용할 타입을 외부에서 지정해 타입 안정성을 높이는 Java 기능이다.

Generic은 Compile Time Type Check를 강화하고 불필요한 Casting을 줄인다.

```java
List<String> names = new ArrayList<>();
```

---

### [핵심]

Generic 핵심:

- Generic
- Type Parameter
- Type Argument
- Type Safety
- Compile Time Check
- Raw Type
- Generic Class
- Generic Method
- Wildcard
- Bounded Type

목적:

```text
타입 안정성 확보
Casting 감소
ClassCastException 예방
API 반환 타입 명확화
Collection 요소 타입 명확화
재사용 가능한 타입 구조 작성
```

---

### [실무]

좋은 예:

```java
List<UserResponse> responses = new ArrayList<>();
Map<Long, User> userMap = new HashMap<>();
ApiResponse<UserResponse> response = ApiResponse.success(userResponse);
```

나쁜 예:

```java
List responses = new ArrayList();
Map userMap = new HashMap();
```

실무 기준:

- Collection에는 Generic Type 명시.
- API Response Wrapper에 Generic 사용.
- Repository / Service Return Type을 명확히 한다.
- Object 반환보다 Generic을 검토.
- Raw Type 사용 금지에 가깝게 검토.

주의:

- Generic은 Runtime Type 정보를 완전히 보존하지 않는다.
- Type Erasure로 인해 런타임 타입 확인에 제한이 있다.
- Wildcard를 과도하게 쓰면 읽기 어려워진다.
- Generic 이름은 관례를 따른다.

---

### [FAQ]

Q. Generic은 왜 써?
A. 컴파일 시점에 타입 오류를 잡고 형변환 코드를 줄이기 위해 사용한다.

Q. Raw Type은 왜 안 좋아?
A. 타입 검사가 약해져 ClassCastException 위험이 커진다.

Q. Generic을 쓰면 Runtime Type Error가 완전히 없어져?
A. 아니다. 대부분의 타입 오류를 컴파일 시 줄이지만 Type Erasure 등 한계가 있다.

---

## 7.2 Generic Type Parameter Rules

### [개념]

Type Parameter는 Generic Class, Interface, Method에서 사용할 타입의 자리표시자다.

대표 관례는 T, E, K, V, R이다.

---

### [핵심]

Type Parameter 관례:

```text
T → Type
E → Element
K → Key
V → Value
R → Return
N → Number
```

예:

```java
public class Box<T> {
    private T value;

    public T getValue() {
        return value;
    }
}
```

Map 예:

```java
Map<K, V>
```

---

### [실무]

Generic Class 예:

```java
public class ApiResponse<T> {
    private final boolean success;
    private final T data;

    private ApiResponse(boolean success, T data) {
        this.success = success;
        this.data = data;
    }

    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(true, data);
    }
}
```

사용:

```java
ApiResponse<UserResponse> response = ApiResponse.success(userResponse);
```

실무 기준:

- 단일 타입은 T 사용.
- Collection 요소는 E 사용.
- Map Key / Value는 K / V 사용.
- 반환 타입 의미가 강하면 R 사용.
- 도메인 의미가 필요하면 명확한 이름도 가능.

주의:

- Type Parameter 이름이 너무 많으면 읽기 어려움.
- Generic 구조가 복잡하면 설계 단순화 검토.
- API 응답 Generic은 직렬화 구조와도 연결된다.

---

### [FAQ]

Q. Generic에서 T는 뭐야?
A. Type을 의미하는 타입 파라미터 관례다.

Q. K와 V는 언제 써?
A. Key와 Value를 표현할 때 사용한다.

Q. Type Parameter 이름은 꼭 한 글자여야 해?
A. 아니다. 복잡한 도메인 의미가 있으면 더 명확한 이름을 사용할 수 있다.

---

## 7.3 Generic Method Rules

### [개념]

Generic Method는 Method 자체에 Type Parameter를 선언해 다양한 타입에 재사용할 수 있는 Method다.

```java
public static <T> T requireNonNull(T value) {
    return Objects.requireNonNull(value);
}
```

---

### [핵심]

Generic Method 핵심:

- Generic Method
- Method Type Parameter
- Static Generic Method
- Type Inference
- Reusable Method
- Return Type
- Compile Time Check

형식:

```text
접근제어자 <T> 반환타입 methodName(Parameter)
```

---

### [실무]

DTO 변환 보조 예:

```java
public static <T> List<T> emptyIfNull(List<T> values) {
    return values == null ? List.of() : values;
}
```

ApiResponse 예:

```java
public static <T> ApiResponse<T> success(T data) {
    return new ApiResponse<>(true, data);
}
```

실무 기준:

- 입력 타입과 반환 타입 관계가 있을 때 적합.
- Casting을 줄일 수 있을 때 사용.
- Utility Method에서 자주 사용.
- Static Factory Method와 함께 자주 사용.
- 타입 추론이 명확해야 한다.

주의:

- Generic Method가 복잡하면 호출자가 이해하기 어렵다.
- Object 반환 후 Casting보다 Generic Method가 안전하다.
- 불필요한 Generic은 오히려 가독성을 해친다.
- 타입 관계가 없다면 Generic이 필요 없을 수 있다.

---

### [FAQ]

Q. Generic Method는 언제 써?
A. Method 입력과 반환 타입 관계를 타입 안전하게 표현하고 재사용해야 할 때 사용한다.

Q. static Method도 Generic을 쓸 수 있어?
A. 가능하다. Method 선언부에 Type Parameter를 선언하면 된다.

Q. Generic Method가 Object 반환보다 좋은 이유는?
A. 호출자가 Casting하지 않아도 되고 컴파일 시 타입 검사를 받을 수 있기 때문이다.

---

## 7.4 Raw Type Rules

### [개념]

Raw Type은 Generic Type Argument를 지정하지 않고 사용하는 방식이다.

Raw Type은 타입 안정성을 약화시키고 ClassCastException 위험을 높인다.

```java
List names = new ArrayList();
```

---

### [핵심]

Raw Type 핵심:

- Raw Type
- Missing Generic
- Type Safety Loss
- ClassCastException
- Unchecked Warning
- Object Casting
- Legacy Code

위험:

```text
서로 다른 타입이 섞일 수 있음
컴파일 시 타입 오류를 잡기 어려움
조회 시 Casting 필요
Runtime ClassCastException 가능
IDE Warning 발생
```

---

### [실무]

나쁜 예:

```java
List values = new ArrayList();
values.add("java");
values.add(1);

String value = (String) values.get(1);
```

좋은 예:

```java
List<String> values = new ArrayList<>();
values.add("java");
```

Map 나쁜 예:

```java
Map data = new HashMap();
```

Map 좋은 예:

```java
Map<String, Object> data = new HashMap<>();
```

더 좋은 API 응답:

```java
UserResponse response = new UserResponse(userId, email);
```

주의:

- Legacy Library와 연동할 때 Raw Type이 보일 수 있다.
- Warning을 무시하지 않는다.
- Raw Type을 발견하면 Generic Type을 명시한다.
- Map<String, Object>도 타입 안정성이 완전하지 않으므로 DTO를 우선 검토한다.

---

### [FAQ]

Q. Raw Type은 뭐야?
A. Generic Type을 지정하지 않고 List, Map처럼 사용하는 방식이다.

Q. Raw Type은 왜 위험해?
A. 타입 검사가 약해져 Runtime ClassCastException이 발생할 수 있기 때문이다.

Q. Raw Type Warning은 무시해도 돼?
A. 권장하지 않는다. 가능한 Generic Type을 명시해야 한다.

---

# 8. Wildcard Rules

## 8.1 Wildcard Purpose

### [개념]

Wildcard는 Generic에서 구체 타입을 유연하게 받기 위한 표현이다.

`?`, `? extends T`, `? super T` 형태가 있다.

```java
List<? extends Number> numbers;
List<? super Integer> integers;
```

---

### [핵심]

Wildcard 핵심:

- Wildcard
- ?
- ? extends T
- ? super T
- Upper Bound
- Lower Bound
- PECS
- Producer Extends
- Consumer Super
- Generic Flexibility

기본 기준:

```text
읽기 중심 Producer → ? extends T
쓰기 중심 Consumer → ? super T
정확한 타입 필요 → T
알 수 없는 타입 → ?
```

---

### [실무]

읽기 중심 예:

```java
public double sum(List<? extends Number> numbers) {
    double total = 0;

    for (Number number : numbers) {
        total += number.doubleValue();
    }

    return total;
}
```

쓰기 중심 예:

```java
public void addIntegers(List<? super Integer> numbers) {
    numbers.add(1);
    numbers.add(2);
}
```

실무 기준:

- API 경계에서 유연성이 필요할 때 사용.
- 내부 구현에서는 명확한 Generic Type이 더 좋을 수 있다.
- 읽기만 하면 extends.
- 쓰기만 하면 super.
- 읽고 쓰기 모두 정확히 필요하면 T.

주의:

- Wildcard를 과도하게 사용하면 가독성이 떨어진다.
- `? extends T`에는 T 하위 값을 안전하게 add하기 어렵다.
- `? super T`에서 꺼낸 값은 Object로 취급될 수 있다.
- 복잡한 Wildcard는 Method Generic으로 바꾸는 것이 나을 수 있다.

---

### [FAQ]

Q. Wildcard는 왜 써?
A. Generic 타입을 더 유연하게 받아 API 사용성을 높이기 위해 사용한다.

Q. ? extends T는 언제 써?
A. T의 하위 타입들을 읽기 중심으로 받을 때 사용한다.

Q. ? super T는 언제 써?
A. T 또는 그 상위 타입 Collection에 값을 넣어야 할 때 사용한다.

---

## 8.2 PECS Rules

### [개념]

PECS는 Producer Extends, Consumer Super의 약자다.

Generic Collection이 값을 생산하면 extends를 쓰고, 값을 소비하면 super를 쓰라는 규칙이다.

---

### [핵심]

PECS 핵심:

```text
Producer Extends
Consumer Super
```

판단:

```text
Collection에서 값을 읽어온다 → Producer → ? extends T
Collection에 값을 넣는다 → Consumer → ? super T
읽고 쓰기 모두 필요하다 → 명확한 T
```

---

### [실무]

Producer 예:

```java
public void printNumbers(List<? extends Number> numbers) {
    for (Number number : numbers) {
        System.out.println(number);
    }
}
```

Consumer 예:

```java
public void addDefaultUsers(List<? super User> users) {
    users.add(new User("user@example.com"));
}
```

정확한 타입 예:

```java
public void replaceUsers(List<User> users) {
    users.clear();
    users.add(new User("user@example.com"));
}
```

주의:

- PECS는 Collection 중심 판단에 유용하다.
- 복잡한 도메인 API에서는 너무 일반화하지 않는다.
- Wildcard보다 명확한 Method 이름과 타입이 더 중요할 수 있다.
- 실무 코드에서는 필요할 때만 사용한다.

---

### [FAQ]

Q. PECS는 뭐야?
A. Producer Extends, Consumer Super의 약자로 Generic Wildcard 사용 기준이다.

Q. 값을 읽기만 하면 뭘 써?
A. `? extends T`를 사용한다.

Q. 값을 넣어야 하면 뭘 써?
A. `? super T`를 사용한다.

---

## 8.3 Bounded Type Parameter Rules

### [개념]

Bounded Type Parameter는 Generic Type Parameter가 특정 타입의 하위 타입이어야 한다고 제한하는 방식이다.

```java
public <T extends Number> double sum(List<T> numbers) {
    return 0;
}
```

---

### [핵심]

Bounded Type 핵심:

- Bounded Type Parameter
- extends
- Upper Bound
- Type Constraint
- Comparable
- Number
- Interface Bound
- Multiple Bound

사용 목적:

```text
특정 Method 사용 가능성 보장
타입 범위 제한
API 안정성 향상
Generic 내부 로직 안전화
```

---

### [실무]

Number 제한 예:

```java
public <T extends Number> double sum(List<T> numbers) {
    return numbers.stream()
        .mapToDouble(Number::doubleValue)
        .sum();
}
```

Comparable 제한 예:

```java
public <T extends Comparable<T>> T max(T first, T second) {
    return first.compareTo(second) >= 0 ? first : second;
}
```

다중 Bound 예:

```java
public <T extends Identifiable & Auditable> void audit(T target) {
    target.getId();
    target.getCreatedAt();
}
```

주의:

- Bound가 복잡하면 Generic 설계가 어려워진다.
- 하위 타입 제한이 실제로 필요한지 확인한다.
- 단순 Object 처리라면 Bound가 불필요할 수 있다.
- Domain Interface를 Bound로 사용할 때 책임이 명확해야 한다.

---

### [FAQ]

Q. Bounded Type Parameter는 언제 써?
A. Generic 타입이 특정 부모 Class나 Interface 기능을 반드시 가져야 할 때 사용한다.

Q. T extends Number는 무슨 뜻이야?
A. T가 Number 또는 Number의 하위 타입이어야 한다는 뜻이다.

Q. Generic Bound를 여러 개 걸 수 있어?
A. 가능하다. Class는 하나만 가능하고 Interface는 여러 개 조합할 수 있다.

---

# 9. Collection and Generic with Stream

## 9.1 Collection to Stream Rules

### [개념]

Stream API는 Collection 데이터를 필터링, 변환, 정렬, 그룹핑, 수집하기 위한 선언형 처리 API다.

Collection과 Generic은 Stream API의 타입 안정성과 결과 타입에 직접 연결된다.

---

### [핵심]

Collection Stream 핵심:

- stream
- filter
- map
- flatMap
- sorted
- distinct
- collect
- toList
- Collectors.toMap
- Collectors.groupingBy
- Generic Type Inference

---

### [실무]

List 변환:

```java
List<UserResponse> responses = users.stream()
    .map(UserResponse::from)
    .toList();
```

Set 수집:

```java
Set<Long> userIds = users.stream()
    .map(User::getId)
    .collect(Collectors.toSet());
```

Map 수집:

```java
Map<Long, User> userMap = users.stream()
    .collect(Collectors.toMap(User::getId, Function.identity()));
```

Grouping:

```java
Map<UserStatus, List<User>> usersByStatus = users.stream()
    .collect(Collectors.groupingBy(User::getStatus));
```

주의:

- toMap은 중복 Key에 주의.
- distinct는 equals / hashCode 기준.
- Stream 결과 Collection 타입이 필요한 경우 collect 사용.
- toList 결과 수정 가능 여부는 Java 버전에 따라 주의.
- 복잡한 Stream은 for문이 더 읽기 쉬울 수 있다.

---

### [FAQ]

Q. Stream에서 List를 DTO List로 바꾸려면?
A. map으로 DTO 변환 후 toList를 사용한다.

Q. Stream으로 Map을 만들 때 주의할 점은?
A. 중복 Key가 있으면 예외가 발생할 수 있어 merge function을 검토해야 한다.

Q. distinct는 어떤 기준으로 중복을 제거해?
A. equals와 hashCode 기준으로 중복을 판단한다.

---

## 9.2 Collectors.toMap Rules

### [개념]

Collectors.toMap은 Stream 요소를 Key-Value 구조의 Map으로 수집하는 Collector다.

Key 중복 가능성을 반드시 검토해야 한다.

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

기본 형식:

```java
Collectors.toMap(keyMapper, valueMapper)
```

중복 처리 형식:

```java
Collectors.toMap(keyMapper, valueMapper, mergeFunction)
```

Map 구현체 지정:

```java
Collectors.toMap(keyMapper, valueMapper, mergeFunction, LinkedHashMap::new)
```

---

### [실무]

기본 예:

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

LinkedHashMap 수집:

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

- 중복 Key가 없다는 보장이 없으면 merge function을 명시한다.
- Value가 null이면 NPE가 발생할 수 있어 주의한다.
- Key가 null인 경우 정책을 명확히 한다.
- 순서가 필요하면 LinkedHashMap supplier 사용.
- 복잡한 merge 규칙은 별도 Method로 분리한다.

---

### [FAQ]

Q. Collectors.toMap에서 중복 Key가 있으면 어떻게 돼?
A. merge function이 없으면 예외가 발생한다.

Q. toMap에서 순서를 유지하려면?
A. LinkedHashMap::new 같은 Map Supplier를 지정한다.

Q. Function.identity는 뭐야?
A. 입력 값을 그대로 반환하는 Function이다.

---

## 9.3 groupingBy Rules

### [개념]

Collectors.groupingBy는 Stream 요소를 특정 Key 기준으로 그룹화해 Map으로 수집하는 Collector다.

---

### [핵심]

groupingBy 핵심:

- Collectors.groupingBy
- Classifier
- Grouping Key
- Map<K, List<T>>
- Downstream Collector
- Counting
- Mapping
- Summarizing

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

DTO만 그룹핑:

```java
Map<UserStatus, List<UserResponse>> responsesByStatus = users.stream()
    .collect(Collectors.groupingBy(
        User::getStatus,
        Collectors.mapping(UserResponse::from, Collectors.toList())
    ));
```

주의:

- 그룹 Key가 null일 수 있는지 확인한다.
- 결과 Map 순서가 필요하면 Map Supplier 검토.
- 그룹핑 후 데이터가 너무 커지면 메모리 사용량을 확인한다.
- DB에서 group by 하는 것이 더 적합한 경우도 많다.

---

### [FAQ]

Q. groupingBy는 언제 써?
A. Collection 데이터를 특정 기준으로 묶어 Map<K, List<T>> 형태로 만들 때 사용한다.

Q. 그룹별 개수만 필요하면?
A. groupingBy와 counting을 함께 사용한다.

Q. 그룹핑은 Java에서 하는 게 좋아 DB에서 하는 게 좋아?
A. 데이터가 많거나 집계 목적이면 DB group by가 더 적합한 경우가 많다.

---

# 10. Null Safety and Immutability in Collection

## 10.1 Empty Collection Rules

### [개념]

Empty Collection은 데이터가 없음을 null이 아니라 빈 Collection으로 표현하는 방식이다.

Collection 반환에서 null보다 empty collection이 호출자에게 안전하다.

---

### [핵심]

Empty Collection 핵심:

- Empty List
- Empty Set
- Empty Map
- Null Safety
- No Result
- Collections.emptyList
- List.of
- Set.of
- Map.of

권장:

```text
List 결과 없음 → empty List
Set 결과 없음 → empty Set
Map 결과 없음 → empty Map
Collection Parameter null → early validation or empty conversion
```

---

### [실무]

좋은 예:

```java
public List<UserResponse> getUsers() {
    return List.of();
}
```

null 방지:

```java
public List<UserResponse> getUsersByStatus(UserStatus status) {
    List<User> users = userRepository.findByStatus(status);

    return users.stream()
        .map(UserResponse::from)
        .toList();
}
```

방어 처리:

```java
public List<String> normalize(List<String> values) {
    if (values == null) {
        return List.of();
    }

    return values.stream()
        .filter(Objects::nonNull)
        .toList();
}
```

주의:

- 반환은 empty collection이 좋지만 입력 Parameter null은 명확히 검증하는 것이 좋다.
- Empty Collection이 수정 가능한지 여부를 확인한다.
- `List.of()`는 수정 불가 List다.
- 호출자가 수정해야 한다면 new ArrayList<>() 반환 검토.

---

### [FAQ]

Q. Collection 반환값은 null이 좋아 empty collection이 좋아?
A. 대부분 empty collection이 좋다.

Q. List.of()로 만든 List는 수정 가능해?
A. 아니다. 수정 불가 List다.

Q. Parameter로 null Collection이 들어오면 어떻게 해?
A. 필수 값이면 예외를 던지고 선택 값이면 empty collection으로 변환할 수 있다.

---

## 10.2 Unmodifiable Collection Rules

### [개념]

Unmodifiable Collection은 외부에서 Collection을 수정하지 못하도록 제한하는 Collection이다.

객체 내부 Collection 보호와 불변 DTO 설계에 사용된다.

---

### [핵심]

Unmodifiable Collection 핵심:

- Unmodifiable List
- Unmodifiable Set
- Unmodifiable Map
- Defensive Copy
- List.copyOf
- Collections.unmodifiableList
- Immutable Collection
- Encapsulation

---

### [실무]

방어적 복사 예:

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

수정 불가 View 예:

```java
public List<Comment> getComments() {
    return Collections.unmodifiableList(comments);
}
```

차이:

```text
List.copyOf → 복사본 생성
Collections.unmodifiableList → 원본을 감싼 수정 불가 View
```

주의:

- Unmodifiable은 Collection 구조 변경을 막지만 요소 객체가 mutable이면 내부 상태는 바뀔 수 있다.
- 방어적 복사가 필요한지 확인한다.
- JPA Entity Collection에는 무조건 copyOf를 적용하기 어렵다.
- API Response DTO에는 불변 Collection이 적합할 수 있다.

---

### [FAQ]

Q. List.copyOf와 Collections.unmodifiableList 차이는?
A. List.copyOf는 복사본을 만들고 unmodifiableList는 원본 Collection을 감싼 수정 불가 View를 만든다.

Q. Unmodifiable List면 완전 불변이야?
A. 아니다. List 구조 변경은 막지만 내부 요소 객체가 mutable이면 상태는 바뀔 수 있다.

Q. 내부 Collection을 보호하려면 어떻게 해?
A. 방어적 복사나 unmodifiable view를 제공하고 add/remove Method로 변경을 제어한다.

---

# 11. Collection and Generic Anti Pattern

## 11.1 Collection Anti Pattern

### [개념]

Collection Anti Pattern은 데이터 특성에 맞지 않는 자료구조를 선택하거나 Collection을 잘못 다뤄 성능, 안정성, 가독성 문제가 생기는 패턴이다.

---

### [핵심]

Collection Anti Pattern:

- 모든 데이터를 List로 처리
- 중복 제거에 List 사용
- Key 조회를 List 순회로 반복
- null Collection 반환
- 내부 mutable Collection 직접 노출
- for-each 중 remove
- HashSet에 mutable 객체 저장
- HashMap Key로 mutable 객체 사용
- 순서 필요한데 HashSet / HashMap 사용
- Stream toMap 중복 Key 미처리
- Map<String, Object> 남용
- Collection Parameter null 정책 없음

---

### [실무]

검토 Flow:

```text
데이터 특성 확인
→ 순서 필요 여부 확인
→ 중복 허용 여부 확인
→ Key 조회 필요 여부 확인
→ 정렬 필요 여부 확인
→ null 반환 여부 확인
→ mutable 노출 여부 확인
→ equals / hashCode 확인
→ Stream 수집 오류 확인
```

개선 후보:

```text
List.contains 반복 → HashSet
List 검색 반복 → HashMap
중복 제거 → Set
순서 유지 중복 제거 → LinkedHashSet
정렬된 Key → TreeMap
Map<String, Object> 응답 → DTO
null List 반환 → empty List
내부 List 반환 → unmodifiable / copy
```

---

### [FAQ]

Q. Collection Anti Pattern 중 가장 흔한 것은?
A. 모든 데이터를 List로 처리하고 contains나 검색을 반복하는 패턴이 흔하다.

Q. Map<String, Object>는 왜 조심해야 해?
A. 타입 안정성이 낮고 Magic String Key와 Casting 오류가 생기기 쉽다.

Q. 내부 Collection을 그대로 반환하면 왜 문제야?
A. 외부에서 객체 내부 상태를 직접 변경할 수 있기 때문이다.

---

## 11.2 Generic Anti Pattern

### [개념]

Generic Anti Pattern은 Generic을 사용하지 않거나 과도하게 사용해 타입 안정성, 가독성, 유지보수성을 떨어뜨리는 패턴이다.

---

### [핵심]

Generic Anti Pattern:

- Raw Type 사용
- Object 반환 남용
- Casting 반복
- Map<String, Object>로 도메인 구조 대체
- Wildcard 과다 사용
- Generic Type Parameter 이름 불명확
- 불필요한 Generic Method
- 복잡한 Bound 남용
- unchecked warning 무시

---

### [실무]

나쁜 예:

```java
public Object getData() {
    return userResponse;
}
```

좋은 예:

```java
public UserResponse getUserResponse() {
    return userResponse;
}
```

나쁜 예:

```java
public List getUsers() {
    return users;
}
```

좋은 예:

```java
public List<UserResponse> getUsers() {
    return users;
}
```

검토 기준:

- Raw Type Warning 제거.
- Object 반환을 구체 타입 또는 Generic으로 변경.
- Casting이 반복되면 Generic 설계 검토.
- Wildcard가 읽기 어렵다면 Method Type Parameter 검토.
- DTO로 표현할 수 있는 구조는 DTO 사용.

---

### [FAQ]

Q. Generic Anti Pattern 중 가장 위험한 것은?
A. Raw Type과 Object 반환 남용이다. Runtime ClassCastException을 만들 수 있다.

Q. unchecked warning은 무시해도 돼?
A. 권장하지 않는다. 타입 안정성 문제가 숨어 있을 수 있다.

Q. Wildcard를 많이 쓰면 좋은 Generic 설계야?
A. 아니다. 필요한 곳에만 사용하고 가독성이 떨어지면 구조를 단순화해야 한다.

---

# 12. Review Checklist

## 12.1 Collection and Generic Review Checklist

### [개념]

Collection and Generic Review Checklist는 Backend Agent / Review Agent가 Java Collection과 Generic 사용 품질을 검토하기 위한 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] 데이터 특성에 맞는 Collection을 선택했는가?
- [ ] 순서가 필요하면 List 또는 LinkedHash 계열을 검토했는가?
- [ ] 중복 제거가 필요하면 Set을 검토했는가?
- [ ] Key 기반 조회가 반복되면 Map을 검토했는가?
- [ ] List.contains 반복 호출을 Set으로 개선할 수 있는가?
- [ ] List 순회 검색 반복을 Map으로 개선할 수 있는가?
- [ ] HashSet / HashMap 사용 시 equals / hashCode가 적절한가?
- [ ] mutable 객체를 HashSet 요소나 HashMap Key로 사용하지 않는가?
- [ ] 순서가 필요한데 HashSet / HashMap을 사용하지 않는가?
- [ ] TreeSet / TreeMap 사용 시 정렬 기준이 명확한가?
- [ ] Collection 반환값으로 null을 반환하지 않는가?
- [ ] 내부 mutable Collection을 그대로 노출하지 않는가?
- [ ] for-each 순회 중 원본 Collection을 직접 수정하지 않는가?
- [ ] Stream toMap에서 중복 Key 가능성을 검토했는가?
- [ ] groupingBy 결과 크기와 DB 처리 가능성을 검토했는가?
- [ ] Map<String, Object> 대신 DTO를 검토했는가?
- [ ] Raw Type을 사용하지 않는가?
- [ ] Generic Type을 명확히 지정했는가?
- [ ] Object 반환과 Casting을 남용하지 않는가?
- [ ] Generic Method 사용 이유가 명확한가?
- [ ] Wildcard 사용이 PECS 기준에 맞는가?
- [ ] Bounded Type Parameter가 실제 제약을 표현하는가?
- [ ] unchecked warning을 방치하지 않는가?
- [ ] Unmodifiable Collection과 방어적 복사 필요성을 검토했는가?
```

---

### [실무]

Review Flow:

```text
Collection 목적 확인
→ List / Set / Map 선택 검토
→ 구현체 선택 검토
→ 중복 / 순서 / 정렬 기준 검토
→ equals / hashCode 검토
→ null 반환 검토
→ mutable 노출 검토
→ Stream 수집 검토
→ Generic Type Safety 검토
→ Wildcard / Bound 검토
→ Anti Pattern 확인
```

리팩터링 후보:

```text
List 검색 반복 → Map 변환
List contains 반복 → Set 변환
String 상태 목록 → Enum Set
Map<String, Object> → DTO
Raw Type → Generic Type 명시
Object 반환 → 구체 타입 / Generic 반환
mutable Collection 노출 → unmodifiable / copy
toMap 중복 Key 오류 → merge function 추가
```

---

### [FAQ]

Q. Collection 검수에서 가장 먼저 볼 것은?
A. 데이터 특성이 순서, 중복, Key 조회 중 무엇을 요구하는지 먼저 확인한다.

Q. Generic 검수에서 가장 먼저 볼 것은?
A. Raw Type 사용 여부와 Object 반환 / Casting 남용 여부를 먼저 확인한다.

Q. equals와 hashCode 검수는 언제 중요해?
A. HashSet, HashMap, distinct, contains에서 객체 동등성을 사용할 때 중요하다.

---

# 13. Backend Integration

## 13.1 Spring Boot Collection and Generic Integration

### [개념]

Collection과 Generic은 Spring Boot Backend의 Repository 결과, Service 처리, DTO 변환, API 응답, Strategy 조회, Validation 결과 처리에 사용된다.

Collection 선택과 Generic 타입 안정성은 API 안정성과 코드 리뷰 품질에 직접 연결된다.

---

### [핵심]

Spring Boot 연결:

```text
Repository
→ List<Entity>
→ Optional<Entity>

Service
→ List / Set / Map 처리
→ Entity 조회 결과 변환
→ 중복 제거
→ Key 조회 최적화

DTO
→ List<ResponseDto>
→ Generic ApiResponse<T>

Strategy
→ Map<Enum, Policy>

Validation
→ Set<Violation>
→ List<ErrorResponse>
```

---

### [실무]

Repository 결과 변환:

```java
public List<UserResponse> getUsers() {
    return userRepository.findAll().stream()
        .map(UserResponse::from)
        .toList();
}
```

ID Set 활용:

```java
Set<Long> userIds = new HashSet<>(request.userIds());
```

Strategy Map:

```java
@Component
public class PaymentProcessorResolver {
    private final Map<PaymentType, PaymentProcessor> processorMap;

    public PaymentProcessorResolver(List<PaymentProcessor> processors) {
        this.processorMap = processors.stream()
            .collect(Collectors.toMap(PaymentProcessor::type, Function.identity()));
    }

    public PaymentProcessor resolve(PaymentType type) {
        PaymentProcessor processor = processorMap.get(type);

        if (processor == null) {
            throw new IllegalArgumentException("unsupported payment type");
        }

        return processor;
    }
}
```

Generic API Response:

```java
public class ApiResponse<T> {
    private final boolean success;
    private final T data;

    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(true, data);
    }
}
```

검토 기준:

- Repository List 결과를 null로 가정하지 않는가?
- API 응답은 DTO List로 변환하는가?
- 중복 ID는 Set으로 처리하는가?
- 반복 조회는 Map 변환을 검토했는가?
- Strategy 구현체는 Map<Enum, Strategy>로 조회 가능한가?
- Generic ApiResponse<T>가 타입 안정성을 제공하는가?
- Map<String, Object> 응답을 남용하지 않는가?

주의:

- JPA Entity Collection은 Lazy Loading과 Transaction 범위를 확인한다.
- Stream 처리 중 N+1 조회가 발생하지 않는지 확인한다.
- API 응답 순서가 필요하면 정렬 기준을 명확히 한다.
- Generic Response는 JSON 직렬화 구조를 함께 확인한다.

---

### [FAQ]

Q. Spring Boot API 목록 응답은 어떤 Collection이 좋아?
A. 보통 List<ResponseDto>를 사용한다.

Q. Repository 조회 결과를 Set으로 받아도 돼?
A. 가능하지만 일반적으로 Repository 목록 조회는 List가 많고 중복 제거가 필요하면 Service에서 Set으로 변환할 수 있다.

Q. Strategy 구현체 선택에는 어떤 Collection이 좋아?
A. Enum이나 Type을 Key로 하는 Map<Enum, Strategy> 구조가 적합한 경우가 많다.

---

# Retrieval Queries

### [FAQ]

Q. Collection Framework는 뭐야?
A. 여러 데이터를 저장, 조회, 순회, 변환, 삭제하기 위한 Java 표준 자료구조 API다.

Q. Collection Framework는 왜 중요해?
A. Java 백엔드 코드에서 자료구조 선택, 중복 처리, 조회 성능, API 응답 구조에 직접 영향을 주기 때문이다.

Q. List, Set, Map 중 무엇을 써야 해?
A. 순서와 중복이 필요하면 List, 중복 제거가 필요하면 Set, Key 기반 조회가 필요하면 Map을 사용한다.

Q. 변수 타입은 ArrayList로 써야 해 List로 써야 해?
A. 대부분 List 같은 Interface 타입으로 선언하고 구현체는 ArrayList 등으로 선택하는 것이 좋다.

Q. Map은 Collection이야?
A. Java 구조상 Map은 Collection Interface를 상속하지 않는 별도 Key-Value 구조다.

Q. List는 언제 써?
A. 순서가 중요하고 중복을 허용하는 목록 데이터에 사용한다.

Q. List는 중복을 허용해?
A. 허용한다. 같은 값이나 객체가 여러 번 들어갈 수 있다.

Q. API 목록 응답은 보통 어떤 타입이 좋아?
A. 보통 List<ResponseDto>를 사용한다.

Q. ArrayList는 언제 써?
A. 일반적인 목록 저장과 조회 위주 처리에 기본 선택지로 많이 사용한다.

Q. ArrayList는 조회가 빠른가?
A. 인덱스 기반 조회는 빠르다.

Q. LinkedList는 언제 써?
A. 앞 / 뒤 삽입 삭제나 Deque 기능이 필요한 경우 검토할 수 있다.

Q. 일반 List는 ArrayList와 LinkedList 중 뭐가 좋아?
A. 대부분 ArrayList가 기본 선택지로 적합하다.

Q. 모든 목록을 List로 처리하면 안 돼?
A. List가 적합한 경우도 많지만 중복 제거는 Set, Key 조회는 Map이 더 적합하다.

Q. List.contains를 반복하면 왜 문제야?
A. List는 순차 탐색이라 데이터가 많으면 비용이 커질 수 있다.

Q. Set은 언제 써?
A. 중복 제거나 유일한 값 집합이 필요할 때 사용한다.

Q. Set은 순서를 보장해?
A. HashSet은 순서를 보장하지 않는다. 순서 유지가 필요하면 LinkedHashSet을 검토한다.

Q. 객체 Set에서 중복 기준은 뭐야?
A. equals와 hashCode 구현 기준에 따라 중복 여부가 결정된다.

Q. HashSet은 순서를 보장해?
A. 아니다. 순서가 필요하면 LinkedHashSet이나 List 정렬을 검토한다.

Q. HashSet이 중복 제거를 어떻게 판단해?
A. hashCode와 equals 결과를 기준으로 판단한다.

Q. LinkedHashSet은 언제 써?
A. 중복을 제거하면서 입력 순서를 유지해야 할 때 사용한다.

Q. TreeSet은 언제 써?
A. 중복을 제거하면서 정렬된 순서가 필요할 때 사용한다.

Q. Map은 언제 써?
A. Key로 값을 빠르게 찾거나 그룹핑 결과를 저장할 때 사용한다.

Q. List를 Map으로 바꾸는 이유는?
A. 반복적인 검색을 줄이고 Key 기반 조회를 빠르게 하기 위해서다.

Q. Map.get 결과가 null이면 무조건 값이 없는 거야?
A. 보통은 그렇지만 Value 자체가 null일 수도 있어 containsKey가 필요한 경우가 있다.

Q. HashMap은 순서를 보장해?
A. 아니다. 순서가 필요하면 LinkedHashMap이나 TreeMap을 검토한다.

Q. 같은 Key로 put하면 어떻게 돼?
A. 기존 Value가 새 Value로 대체된다.

Q. HashMap Key는 어떤 값이 좋아?
A. 불변이고 equals / hashCode 기준이 안정적인 값이 좋다.

Q. LinkedHashMap은 언제 써?
A. Key-Value 구조에서 삽입 순서를 유지해야 할 때 사용한다.

Q. TreeMap은 언제 써?
A. Key 기준 정렬 순서가 필요한 경우 사용한다.

Q. Map<String, Object>로 응답을 만들어도 돼?
A. 가능하지만 타입 안정성이 낮아 DTO를 우선 검토하는 것이 좋다.

Q. Map에서 Object Value를 꺼내 캐스팅하면 왜 위험해?
A. 실제 타입이 다르면 ClassCastException이 발생할 수 있다.

Q. Queue는 언제 써?
A. 먼저 들어온 작업을 먼저 처리하는 FIFO 구조가 필요할 때 사용한다.

Q. poll과 peek 차이는?
A. poll은 요소를 제거하면서 반환하고 peek은 제거하지 않고 확인한다.

Q. Deque는 언제 써?
A. 양쪽 끝에서 삽입 / 삭제가 필요하거나 Stack / Queue 용도로 사용할 때 쓴다.

Q. Stack 대신 뭘 쓰는 게 좋아?
A. 신규 코드는 Stack보다 ArrayDeque를 우선 검토한다.

Q. equals와 hashCode는 왜 같이 구현해?
A. HashSet, HashMap 같은 Hash 기반 Collection에서 객체 동등성 기준을 일관되게 유지하기 위해서다.

Q. equals만 override하면 안 돼?
A. 안 된다. Hash 기반 Collection에서 같은 객체로 인식되지 않는 문제가 생길 수 있다.

Q. Value Object의 equals 기준은 뭐야?
A. 식별자가 아니라 객체가 가진 값이 같으면 같은 것으로 본다.

Q. Entity equals는 Value Object처럼 모든 Field로 비교해도 돼?
A. 권장하지 않는다. Entity는 식별자와 영속성 생명주기를 고려해야 한다.

Q. JPA Entity에 Lombok @EqualsAndHashCode를 써도 돼?
A. 무분별하게 사용하면 Lazy Loading, 순환 참조, 식별자 문제를 만들 수 있어 주의해야 한다.

Q. Generic은 왜 써?
A. 컴파일 시점에 타입 오류를 잡고 형변환 코드를 줄이기 위해 사용한다.

Q. Raw Type은 왜 안 좋아?
A. 타입 검사가 약해져 ClassCastException 위험이 커진다.

Q. Generic에서 T는 뭐야?
A. Type을 의미하는 타입 파라미터 관례다.

Q. Generic Method는 언제 써?
A. Method 입력과 반환 타입 관계를 타입 안전하게 표현하고 재사용해야 할 때 사용한다.

Q. Raw Type은 뭐야?
A. Generic Type을 지정하지 않고 List, Map처럼 사용하는 방식이다.

Q. Raw Type Warning은 무시해도 돼?
A. 권장하지 않는다. 가능한 Generic Type을 명시해야 한다.

Q. Wildcard는 왜 써?
A. Generic 타입을 더 유연하게 받아 API 사용성을 높이기 위해 사용한다.

Q. ? extends T는 언제 써?
A. T의 하위 타입들을 읽기 중심으로 받을 때 사용한다.

Q. ? super T는 언제 써?
A. T 또는 그 상위 타입 Collection에 값을 넣어야 할 때 사용한다.

Q. PECS는 뭐야?
A. Producer Extends, Consumer Super의 약자로 Generic Wildcard 사용 기준이다.

Q. Bounded Type Parameter는 언제 써?
A. Generic 타입이 특정 부모 Class나 Interface 기능을 반드시 가져야 할 때 사용한다.

Q. Stream에서 List를 DTO List로 바꾸려면?
A. map으로 DTO 변환 후 toList를 사용한다.

Q. Stream으로 Map을 만들 때 주의할 점은?
A. 중복 Key가 있으면 예외가 발생할 수 있어 merge function을 검토해야 한다.

Q. distinct는 어떤 기준으로 중복을 제거해?
A. equals와 hashCode 기준으로 중복을 판단한다.

Q. Collectors.toMap에서 중복 Key가 있으면 어떻게 돼?
A. merge function이 없으면 예외가 발생한다.

Q. toMap에서 순서를 유지하려면?
A. LinkedHashMap::new 같은 Map Supplier를 지정한다.

Q. groupingBy는 언제 써?
A. Collection 데이터를 특정 기준으로 묶어 Map<K, List<T>> 형태로 만들 때 사용한다.

Q. Collection 반환값은 null이 좋아 empty collection이 좋아?
A. 대부분 empty collection이 좋다.

Q. List.of()로 만든 List는 수정 가능해?
A. 아니다. 수정 불가 List다.

Q. List.copyOf와 Collections.unmodifiableList 차이는?
A. List.copyOf는 복사본을 만들고 unmodifiableList는 원본 Collection을 감싼 수정 불가 View를 만든다.

Q. Unmodifiable List면 완전 불변이야?
A. 아니다. List 구조 변경은 막지만 내부 요소 객체가 mutable이면 상태는 바뀔 수 있다.

Q. Collection Anti Pattern 중 가장 흔한 것은?
A. 모든 데이터를 List로 처리하고 contains나 검색을 반복하는 패턴이 흔하다.

Q. Generic Anti Pattern 중 가장 위험한 것은?
A. Raw Type과 Object 반환 남용이다. Runtime ClassCastException을 만들 수 있다.

Q. Collection 검수에서 가장 먼저 볼 것은?
A. 데이터 특성이 순서, 중복, Key 조회 중 무엇을 요구하는지 먼저 확인한다.

Q. Generic 검수에서 가장 먼저 볼 것은?
A. Raw Type 사용 여부와 Object 반환 / Casting 남용 여부를 먼저 확인한다.

Q. Spring Boot API 목록 응답은 어떤 Collection이 좋아?
A. 보통 List<ResponseDto>를 사용한다.

Q. Strategy 구현체 선택에는 어떤 Collection이 좋아?
A. Enum이나 Type을 Key로 하는 Map<Enum, Strategy> 구조가 적합한 경우가 많다.

Q. Java Part05 다음 문서는 뭐야?
A. Java Part06 — Exception, Null Safety, Optional 문서로 이어지는 것이 좋다.
