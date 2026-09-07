# Testing Part 07 - Testcontainers

---

# 1. Testcontainers Core

## 1.1 Testcontainers Overview

### [개념]

Testcontainers는 Docker Container 기반 Integration Test Framework다.

테스트 실행 시 실제 Infrastructure Container를 동적으로 생성한다.

주요 목적:

- Real Infrastructure Validation
- Production-like Environment
- Database Compatibility Validation
- External Dependency Validation

---

### [핵심]

검증 대상:

- MySQL
- PostgreSQL
- Redis
- Kafka
- Elasticsearch
- LocalStack

---

### [실무]

2026 Spring Boot 실무 기준 Testcontainers는 운영 환경과 최대한 유사한 테스트를 위해 사용된다.

대표 사용 사례:

- H2 대체
- MySQL 검증
- Redis 검증
- Kafka Event 검증

---

### [FAQ]

Q. Testcontainers란?
A. Docker 기반 Integration Test Framework다.

Q. Testcontainers 핵심 목적은?
A. 운영 환경과 유사한 테스트 환경 제공이다.

---

# 2. Why Testcontainers

## 2.1 Need

### [개념]

In-memory DB는 운영 환경과 차이가 있다.

---

### [핵심]

문제 상황:

- SQL Dialect 차이
- JSON Column 차이
- Index Behavior 차이
- Lock Behavior 차이

---

### [Comparison]

| Category              | H2   | Testcontainers |
| --------------------- | ---- | -------------- |
| Speed                 | Fast | Slower         |
| Cost                  | Low  | Higher         |
| Production Similarity | Low  | High           |

---

### [FAQ]

Q. 왜 H2만으로 부족한가?
A. 운영 DB와 동작 차이로 실제 장애를 놓칠 수 있다.

---

# 3. Core Annotation

## 3.1 @Testcontainers

### [개념]

Testcontainers 사용 선언.

---

### [예제]

```java
@Testcontainers
@SpringBootTest
class RepositoryIntegrationTest {
}
```

---

### [FAQ]

Q. @Testcontainers 역할은?
A. Container Lifecycle 관리를 담당한다.

---

## 3.2 @Container

### [개념]

테스트에서 사용할 Container 선언.

---

### [예제]

```java
@Container
static MySQLContainer<?> mysql =
        new MySQLContainer<>("mysql:8.0");
```

---

### [Flow]

```text
Container Start
→ Test Execute
→ Container Stop
```

---

### [FAQ]

Q. @Container 역할은?
A. 테스트 실행 전 Container를 시작한다.

---

# 4. Database Containers

## 4.1 MySQL Container

### [예제]

```java
@Container
static MySQLContainer<?> mysql =
        new MySQLContainer<>("mysql:8.0")
                .withDatabaseName("testdb")
                .withUsername("test")
                .withPassword("test");
```

---

### [FAQ]

Q. MySQLContainer는 언제 사용하는가?
A. 운영 DB가 MySQL일 때 사용한다.

---

## 4.2 PostgreSQL Container

### [예제]

```java
@Container
static PostgreSQLContainer<?> postgres =
        new PostgreSQLContainer<>("postgres:16");
```

---

### [FAQ]

Q. PostgreSQL도 동일한 방식인가?
A. 그렇다. Container 타입만 다르다.

---

# 5. Infrastructure Containers

## 5.1 Redis Container

### [개념]

Redis 연동 검증.

---

### [핵심]

검증 대상:

- Cache
- Pub/Sub
- Session
- Distributed Lock

---

### [FAQ]

Q. Redis 테스트에도 Testcontainers가 좋은가?
A. 매우 좋다. 실제 Redis 동작 검증이 가능하다.

---

## 5.2 Kafka Container

### [개념]

Kafka Event Flow 검증.

---

### [핵심]

검증 대상:

- Producer
- Consumer
- Publish
- Consume

---

### [FAQ]

Q. Kafka 테스트도 가능한가?
A. 가능하다. Event Flow 검증에 유용하다.

---

# 6. DynamicPropertySource

## 6.1 Dynamic Configuration

### [개념]

Container 정보를 Spring Environment에 동적으로 주입한다.

---

### [예제]

```java
@DynamicPropertySource
static void configure(DynamicPropertyRegistry registry) {
    registry.add("spring.datasource.url",
            mysql::getJdbcUrl);
}
```

---

### [핵심]

주입 대상:

- datasource.url
- datasource.username
- datasource.password
- redis.host
- redis.port

---

### [FAQ]

Q. DynamicPropertySource가 필요한 이유는?
A. Container Runtime 정보를 Spring 설정에 연결하기 위해서다.

---

# 7. Testcontainers Flow

## 7.1 Standard Flow

### [Flow]

```text
Start Container
→ Inject Properties
→ Load Spring Context
→ Execute Test
→ Cleanup
```

---

### [FAQ]

Q. Testcontainers 실행 흐름은?
A. Container 시작 후 Spring과 연결하여 테스트를 수행한다.

---

# 8. Testcontainers Rules

## 8.1 Best Practice

### [Best Practice]

권장:

- 운영 DB와 동일 버전 사용
- 핵심 Flow 검증
- Integration Test와 함께 사용

---

### [주의]

금지:

- 모든 테스트에 적용
- 불필요한 Container 다중 실행
- 무거운 테스트 남용

---

### [Checklist]

- Container 정상 실행
- Dynamic Property 설정
- Integration 검증 완료
- 운영 환경 유사성 확보

---

# 9. Common Mistakes

## 9.1 Frequent Issues

### [Troubleshooting]

문제:

Container Start Failed

원인:

Docker 미실행

해결:

Docker 상태 확인

---

문제:

Connection Refused

원인:

Property 설정 누락

해결:

DynamicPropertySource 확인

---

문제:

테스트 느림

원인:

Container Startup Cost

해결:

핵심 테스트만 적용

---

# 10. Agent Decision Rules

## 10.1 Test Routing

### [Flow]

```text
Complex DB Validation
→ Testcontainers

Redis Validation
→ Testcontainers

Kafka Validation
→ Testcontainers

Simple Query Validation
→ Repository Test
```

---

### [핵심]

Backend Agent Routing 기준.

---

### [FAQ]

Q. 언제 Testcontainers를 사용해야 하는가?
A. 운영 환경과 유사한 Infrastructure 검증이 필요할 때다.

---

# Retrieval Queries

### [FAQ]

Q. Testcontainers란?
A. Docker 기반 Integration Test Framework다.

Q. Testcontainers 핵심 대상은?
A. MySQL, PostgreSQL, Redis, Kafka.

Q. 왜 Testcontainers를 사용하는가?
A. 운영 환경과 유사한 테스트를 위해 사용한다.

Q. H2보다 좋은 점은?
A. Production Similarity가 훨씬 높다.

Q. 언제 Testcontainers를 사용하는가?
A. Complex Infrastructure 검증이 필요할 때.
