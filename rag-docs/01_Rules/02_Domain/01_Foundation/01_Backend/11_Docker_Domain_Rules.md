# Docker Domain Rules

---

# 1. Domain Purpose

Docker Domain 문서는 Backend Agent / DevOps Agent / Review Agent용 RAG 문서이다.

목적:

- Containerization Support
- Deployment Automation Support
- Environment Standardization
- Infrastructure Troubleshooting
- Container Performance Optimization

우선순위:

1. Docker Core
2. Dockerfile
3. Docker Compose
4. Deployment / Troubleshooting

---

# 2. Scope

포함 범위:

- Docker Core
- Container
- Image
- Registry
- Dockerfile
- Layer
- Build Cache
- Volume
- Network
- Environment Variable
- Docker Compose
- Multi-stage Build
- Container Lifecycle
- Logs
- Health Check
- Resource Limit
- Performance
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

# 4. Docker Core Rules

Docker 문서는 Container 기반 Runtime Environment 중심으로 작성.

핵심 구조:

- Image
- Container
- Registry
- Host OS
- Network
- Volume

---

반드시 설명 포함:

- Docker 역할
- 왜 사용하는가
- VM과 차이
- 어떤 문제를 해결하는가

---

예:

```text
Code
→ Build Image
→ Run Container
→ Deploy
```

---

# 5. Container Rules

반드시 설명:

- Container란
- Process Isolation
- Lightweight Runtime

---

핵심:

Container는 Image의 실행 인스턴스.

---

예:

```bash
docker run nginx
```

---

# 6. Image Rules

필수 포함:

- Docker Image
- Immutable
- Layer
- Build

---

반드시 설명:

- Image와 Container 차이
- Layer 구조

---

예:

```text
Image → Blueprint
Container → Running Instance
```

---

# 7. Dockerfile Rules

매우 중요.

필수 포함:

- FROM
- WORKDIR
- COPY
- RUN
- ENV
- EXPOSE
- ENTRYPOINT
- CMD

---

예:

```dockerfile
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY app.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

---

중요:

Docker 문서 품질은 Dockerfile 설명 품질이 결정.

---

# 8. Layer Rules

필수 포함:

- Layer
- Cache
- Immutable Layer

---

반드시 설명:

- Build 속도
- Layer Cache 최적화

---

예:

```text
Base Layer
→ Dependency Layer
→ Application Layer
```

---

# 9. Build Rules

필수 포함:

- docker build
- Tag
- Cache

---

예:

```bash
docker build -t myapp:1.0 .
```

---

반드시 설명:

- Build 과정
- Cache 활용

---

# 10. Multi-stage Build Rules

매우 중요.

필수 포함:

- Builder Stage
- Runtime Stage

---

예:

```dockerfile
FROM gradle AS builder
FROM eclipse-temurin:21-jre
```

---

반드시 설명:

- Image Size 감소
- 보안 향상

---

# 11. Registry Rules

필수 포함:

- Docker Hub
- Private Registry
- Image Push / Pull

---

예:

```bash
docker push myapp:1.0
```

---

# 12. Volume Rules

필수 포함:

- Named Volume
- Bind Mount
- Persistent Storage

---

반드시 설명:

- 데이터 영속성
- Container 삭제와 데이터 관계

---

# 13. Network Rules

필수 포함:

- Bridge
- Host
- Custom Network

---

반드시 설명:

- Container 통신
- Service Discovery

---

# 14. Environment Variable Rules

필수 포함:

- ENV
- Runtime Variable
- Secret Injection

---

예:

```bash
docker run -e SPRING_PROFILES_ACTIVE=prod
```

---

중요:

Secret 하드코딩 금지.

---

# 15. Docker Compose Rules

매우 중요.

필수 포함:

- services
- networks
- volumes
- environment
- depends_on

---

예:

```yaml
services:
  app:
  redis:
  mysql:
```

---

반드시 설명:

- Multi Container 관리

---

# 16. Spring Boot Docker Rules

필수 포함:

- Spring Boot Dockerfile
- Jar Packaging
- Environment Injection
- Profile

---

반드시 설명:

- Spring Boot + Docker 실무 구조

---

Flow:

```text
Spring Boot Build
→ Jar
→ Docker Image
→ Container Run
```

---

# 17. Logs Rules

필수 포함:

- docker logs
- stdout
- stderr

---

예:

```bash
docker logs app
```

---

# 18. Health Check Rules

필수 포함:

- HEALTHCHECK
- Container Status

---

예:

```dockerfile
HEALTHCHECK CMD curl --fail http://localhost:8080/actuator/health
```

---

반드시 설명:

- Health Monitoring
- Restart 판단

---

# 19. Resource Rules

필수 포함:

- CPU Limit
- Memory Limit
- Resource Isolation

---

반드시 설명:

- OOM
- Container Resource Control

---

# 20. Performance Rules

필수 포함:

- Startup Time
- Memory Usage
- Build Speed
- Layer Cache

---

반드시 설명:

- Docker 성능 병목
- Optimization 방법

---

# 21. Troubleshooting Rules

반드시 포함 추천.

예:

- Container Exit
- Port Conflict
- Build Failed
- Volume Issue
- Network Issue
- OOM
- Permission Denied

---

형식:

문제:

원인:

해결:

---

# 22. Retrieval Optimization Rules

강조 대상:

- Docker
- Container
- Image
- Dockerfile
- Docker Compose
- Volume
- Network
- Health Check

키워드 반복 허용.

---

# 23. Version Rules

기준:

- Docker 27+
- Docker Compose v2
- Spring Boot 3.x
- Java 21
- Ubuntu 24/26 LTS

---

Legacy 제외.

---

# 24. Common Mistakes

자주 발생:

- Large Image
- Secret Hardcoding
- Volume 미설정
- Container=VM 오해
- Port 충돌
- Build Cache 비효율
- Root User 실행
- Health Check 없음
- Log 관리 없음

---

# 25. Final Goal

Docker RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve Docker Pattern
- Build Dockerfile
- Build Compose File
- Containerize Application
- Solve Deployment Issues
- Troubleshoot Container Problems

문서 품질이 DevOps Agent 품질을 결정한다.
