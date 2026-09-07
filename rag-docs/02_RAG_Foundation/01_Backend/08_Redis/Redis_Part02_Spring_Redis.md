# Redis Part 02 - Spring Redis

---

# 1. Spring Redis Core

## 1.1 Spring Redis Overview

### [개념]

Spring Redis는 Spring Boot에서 Redis를 연동하기 위한 Infrastructure Layer다.

주요 목적:

- Redis Integration
- Cache Management
- Session Management
- Data Access Abstraction

---

### [핵심]

핵심 구성:

- Spring Data Redis
- RedisTemplate
- StringRedisTemplate
- RedisConnectionFactory
- Redis Client

---

### [실무]

2026 Spring Boot 실무 기준 Redis 연동은 대부분 Spring Data Redis 기반이다.

주요 사용 방식:

- RedisTemplate
- StringRedisTemplate
- Spring Cache
- Session Store

---

### [FAQ]

Q. Spring Redis란?
A. Spring Boot에서 Redis를 쉽게 연동하기 위한 기술 스택이다.

Q. Spring Redis 핵심 구성은?
A. Spring Data Redis, RedisTemplate, StringRedisTemplate, Redis Client다.

---

# 2. Redis Client

## 2.1 Redis Client Overview

### [개념]

Spring은 Redis와 통신하기 위해 Redis Client를 사용한다.

---

### [핵심]

대표 Client:

- Lettuce
- Redisson

---

### [실무]

기본 선택:

- Lettuce → Spring Boot 기본 Redis Client
- Redisson → Distributed Lock, Advanced Redis Feature

---

### [Comparison]

| Category            | Lettuce              | Redisson               |
| ------------------- | -------------------- | ---------------------- |
| Main Usage          | General Redis Access | Advanced Redis Feature |
| Spring Boot Default | Yes                  | No                     |
| Distributed Lock    | 직접 구현 필요       | 강력 지원              |
| Common Usage        | RedisTemplate        | RLock                  |

---

### [FAQ]

Q. Spring Boot 기본 Redis Client는?
A. Lettuce다.

Q. Redisson은 언제 사용하는가?
A. Distributed Lock이 중요할 때 사용한다.

---

# 3. Redis Connection

## 3.1 RedisConnectionFactory

### [개념]

RedisConnectionFactory는 Redis Connection 생성을 담당한다.

---

### [핵심]

역할:

- Redis Connection 생성
- Redis Client 연결
- RedisTemplate 기반 연결 제공

---

### [예제]

```java
@Bean
public RedisConnectionFactory redisConnectionFactory() {
    return new LettuceConnectionFactory();
}
```

---

### [FAQ]

Q. RedisConnectionFactory 역할은?
A. Redis Connection 생성을 담당한다.

---

# 4. RedisTemplate

## 4.1 RedisTemplate Overview

### [개념]

RedisTemplate은 Spring Redis에서 Redis 자료구조를 직접 제어하는 핵심 클래스다.

---

### [핵심]

역할:

- Redis Read
- Redis Write
- Serialization
- Data Structure Access
- TTL Control

---

### [예제]

```java
private final RedisTemplate<String, Object> redisTemplate;
```

---

### [실무]

RedisTemplate은 자료구조별 세밀한 제어가 필요할 때 사용한다.

사용 예:

- Object Cache
- Hash Data
- Set Data
- List Queue
- Custom TTL

---

### [FAQ]

Q. RedisTemplate이란?
A. Redis 자료구조를 직접 제어하기 위한 핵심 클래스다.

Q. RedisTemplate은 언제 사용하는가?
A. 자료구조별 직접 제어와 TTL 제어가 필요할 때 사용한다.

---

# 5. StringRedisTemplate

## 5.1 StringRedisTemplate Overview

### [개념]

StringRedisTemplate은 Key와 Value를 String 중심으로 다루는 RedisTemplate 특화 클래스다.

---

### [핵심]

특징:

- String Key
- String Value
- StringRedisSerializer 기본 사용
- 단순 Cache / Counter / Token 처리에 적합

---

### [예제]

```java
private final StringRedisTemplate stringRedisTemplate;
```

---

### [예제]

```java
stringRedisTemplate.opsForValue()
        .set("view_count:post:1", "100");
```

---

### [실무]

StringRedisTemplate은 단순 문자열 기반 Redis 작업에 적합하다.

대표 사용:

- Counter
- Token
- Simple Cache
- Rate Limiting Counter

---

### [Comparison]

| Category   | RedisTemplate         | StringRedisTemplate |
| ---------- | --------------------- | ------------------- |
| Value Type | Object 가능           | String 중심         |
| Serializer | 직접 설정 필요        | String 기본         |
| Use Case   | Object / Complex Data | Simple String Data  |
| Control    | 높음                  | 단순함              |

---

### [FAQ]

Q. StringRedisTemplate은 언제 사용하는가?
A. Key와 Value가 단순 문자열일 때 사용한다.

Q. RedisTemplate과 StringRedisTemplate 차이는?
A. RedisTemplate은 Object 중심, StringRedisTemplate은 String 중심이다.

---

# 6. Value Operations

## 6.1 String Access

### [개념]

ValueOperations는 Redis String 자료구조 접근 방식이다.

---

### [핵심]

- opsForValue()
- ValueOperations
- Simple Cache
- Counter
- Token

---

### [예제]

```java
redisTemplate.opsForValue()
        .set("key", "value");
```

---

### [예제]

```java
stringRedisTemplate.opsForValue()
        .increment("view_count:post:1");
```

---

### [FAQ]

Q. String 접근은 어떻게 하는가?
A. opsForValue()를 사용한다.

---

# 7. Hash Operations

## 7.1 Hash Access

### [개념]

HashOperations는 Redis Hash 자료구조 접근 방식이다.

---

### [핵심]

- opsForHash()
- HashOperations
- Object-like Data
- Partial Update

---

### [예제]

```java
redisTemplate.opsForHash()
        .put("user:1", "name", "jun");
```

---

### [FAQ]

Q. Hash 접근은 어떻게 하는가?
A. opsForHash()를 사용한다.

---

# 8. List Operations

## 8.1 List Access

### [개념]

ListOperations는 Redis List 자료구조 접근 방식이다.

---

### [핵심]

- opsForList()
- ListOperations
- Queue
- Recent History

---

### [예제]

```java
redisTemplate.opsForList()
        .leftPush("queue", "task1");
```

---

### [FAQ]

Q. List 접근은 어떻게 하는가?
A. opsForList()를 사용한다.

---

# 9. Set Operations

## 9.1 Set Access

### [개념]

SetOperations는 Redis Set 자료구조 접근 방식이다.

---

### [핵심]

- opsForSet()
- SetOperations
- Unique Collection
- Membership Check

---

### [예제]

```java
redisTemplate.opsForSet()
        .add("tags", "redis");
```

---

### [FAQ]

Q. Set 접근은 어떻게 하는가?
A. opsForSet()를 사용한다.

---

# 10. Serialization

## 10.1 Serializer

### [개념]

Redis는 Java Object를 그대로 저장하지 않는다.

Serialization 설정이 필요하다.

---

### [핵심]

대표 Serializer:

- StringRedisSerializer
- Jackson2JsonRedisSerializer
- GenericJackson2JsonRedisSerializer

---

### [실무]

실무 권장:

- Key → StringRedisSerializer
- Value → JSON Serializer
- Hash Key → StringRedisSerializer
- Hash Value → JSON Serializer

---

### [주의]

Serializer가 불일치하면 저장은 되었지만 읽지 못하는 문제가 발생할 수 있다.

---

### [FAQ]

Q. Serialization이 필요한 이유는?
A. Redis는 Java Object를 직접 저장하지 않기 때문이다.

Q. Serializer 불일치 문제는?
A. 데이터를 저장했지만 역직렬화 실패로 읽지 못할 수 있다.

---

# 11. TTL with Spring Redis

## 11.1 Expiration

### [개념]

Spring Redis에서 TTL을 설정해 Key 수명을 제어한다.

---

### [핵심]

TTL 설정 방식:

- RedisTemplate set with Duration
- expire()
- Spring Cache TTL 설정

---

### [예제]

```java
redisTemplate.opsForValue()
        .set("key", "value", Duration.ofMinutes(5));
```

---

### [예제]

```java
redisTemplate.expire("key", Duration.ofMinutes(5));
```

---

### [FAQ]

Q. RedisTemplate에서 TTL은 어떻게 설정하는가?
A. set()의 Duration 또는 expire()를 사용한다.

---

# 12. Spring Cache

## 12.1 Cache Abstraction

### [개념]

Spring Cache는 Annotation 기반 선언적 캐싱 기능이다.

Redis를 Cache Backend로 사용할 수 있다.

---

### [핵심]

핵심 Annotation:

- @Cacheable
- @CachePut
- @CacheEvict

---

### [Comparison]

| Category   | RedisTemplate     | Spring Cache |
| ---------- | ----------------- | ------------ |
| Style      | 명령형            | 선언형       |
| Control    | 높음              | 단순함       |
| Use Case   | 복잡한 Redis 제어 | 단순 Cache   |
| Annotation | 없음              | 있음         |

---

### [FAQ]

Q. Spring Cache란?
A. Annotation 기반 캐싱 추상화다.

Q. RedisTemplate과 Spring Cache 차이는?
A. RedisTemplate은 직접 제어, Spring Cache는 선언적 캐싱이다.

---

## 12.2 @Cacheable

### [개념]

@Cacheable은 Cache Hit 시 메서드를 실행하지 않고 Cache 값을 반환한다.

---

### [예제]

```java
@Cacheable(value = "users", key = "#id")
public User findUser(Long id) {
    return userRepository.findById(id)
            .orElseThrow();
}
```

---

### [FAQ]

Q. @Cacheable 역할은?
A. Cache Hit 시 메서드 실행 없이 Cache 값을 반환한다.

---

## 12.3 @CachePut

### [개념]

@CachePut은 메서드를 항상 실행하고 결과를 Cache에 갱신한다.

---

### [예제]

```java
@CachePut(value = "users", key = "#user.id")
public User updateUser(User user) {
    return userRepository.save(user);
}
```

---

### [FAQ]

Q. @CachePut 역할은?
A. 메서드 실행 결과를 Cache에 갱신한다.

---

## 12.4 @CacheEvict

### [개념]

@CacheEvict는 Cache 데이터를 삭제한다.

---

### [예제]

```java
@CacheEvict(value = "users", key = "#id")
public void deleteUser(Long id) {
    userRepository.deleteById(id);
}
```

---

### [FAQ]

Q. @CacheEvict 역할은?
A. Cache 삭제다.

---

# 13. Session Store

## 13.1 Session Management

### [개념]

Redis는 Session Store로 자주 사용된다.

---

### [핵심]

주요 용도:

- Login Session
- Shared Session
- Multi Server Session

---

### [실무]

Multi Server 환경에서 Local Session만 사용하면 서버 간 인증 상태 공유가 어렵다.

Redis Session Store는 여러 서버가 동일 Session을 공유할 수 있게 한다.

---

### [FAQ]

Q. Redis가 Session Store에 좋은 이유는?
A. 빠르고 Multi Server 환경의 Session 공유에 적합하기 때문이다.

---

# 14. Spring Redis Rules

## 14.1 Best Practice

### [Best Practice]

권장:

- 단순 문자열은 StringRedisTemplate 사용
- 복잡한 객체는 RedisTemplate 사용
- Key Serializer 명확히 설정
- TTL 설정
- Cache 전략 분리

---

### [주의]

금지:

- Serialization 무시
- TTL 누락
- 무분별한 Cache 사용
- RedisTemplate과 StringRedisTemplate 용도 혼동

---

### [Checklist]

- Redis Client 선택
- RedisTemplate / StringRedisTemplate 선택
- Serializer 설정
- TTL 설정
- Cache 전략 설정

---

# 15. Common Mistakes

## 15.1 Frequent Issues

### [Troubleshooting]

문제:

Value Read 실패

원인:

Serializer 불일치

해결:

Serializer 통일

---

문제:

Redis Connection 실패

원인:

Host / Port 오류

해결:

Connection 설정 확인

---

문제:

Cache Miss 증가

원인:

TTL 설정 문제

해결:

TTL 조정

---

문제:

StringRedisTemplate으로 Object 저장 실패

원인:

String 중심 Template에 Object 사용

해결:

RedisTemplate 사용 또는 JSON 문자열 변환

---

# 16. Agent Decision Rules

## 16.1 Redis Routing

### [Flow]

```text
Simple String Data
→ StringRedisTemplate

Object / Complex Data
→ RedisTemplate

Simple Declarative Cache
→ Spring Cache

Distributed Lock
→ Redisson
```

---

### [핵심]

Backend Agent Routing 기준.

---

### [FAQ]

Q. 언제 RedisTemplate을 사용하는가?
A. Object 또는 복잡한 Redis 자료구조 제어가 필요할 때다.

Q. 언제 StringRedisTemplate을 사용하는가?
A. 단순 문자열, Counter, Token 처리에 사용한다.

---

# Retrieval Queries

### [FAQ]

Q. Spring Redis란?
A. Spring Boot Redis 연동 기술이다.

Q. RedisTemplate이란?
A. Redis 자료구조 직접 제어용 핵심 클래스다.

Q. StringRedisTemplate이란?
A. String 기반 Redis 작업에 특화된 Template이다.

Q. Spring Boot 기본 Redis Client는?
A. Lettuce다.

Q. Spring Cache 핵심 Annotation은?
A. @Cacheable, @CachePut, @CacheEvict.

Q. 언제 Redisson을 사용하는가?
A. Distributed Lock이 필요할 때다.
