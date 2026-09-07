# Docker Part04 Deployment and Troubleshooting

---

# 1. Docker Deployment Core

## 1.1 Docker Deployment Overview

### [개념]

Docker Deployment는 Docker Image를 Registry에 저장하고 운영 서버에서 Container로 실행하는 배포 과정이다.

Docker Deployment의 핵심은 동일한 Image를 여러 환경에서 재현 가능하게 실행하는 것이다.

```text
Code
→ Build Image
→ Push Registry
→ Pull Server
→ Run Container
→ Check Logs
→ Check Health
```

Docker는 Application Runtime을 Image로 고정하고, Runtime Config는 Environment Variable, Secret, Volume, Network로 주입한다.

---

### [핵심]

Docker Deployment 핵심 요소:

- Dockerfile
- Docker Image
- Image Tag
- Docker Registry
- Runtime Environment Variable
- Secret Injection
- Volume
- Network
- Port Mapping
- Restart Policy
- Logs
- Health Check
- Rollback
- Backup

배포 원칙:

```text
Build Once
→ Run Anywhere
```

운영 배포에서 Image는 재빌드하지 않고 동일한 Image Tag를 Pull하여 실행한다.

---

### [Flow]

```text
Git Commit
→ CI Test
→ Docker Image Build
→ Image Tagging
→ Registry Push
→ Production Server Pull
→ Container Recreate
→ Health Check
→ Logs Check
→ Deployment Complete
```

---

### [실무]

2026 실무 기준 Docker Deployment는 다음 방식으로 구성된다.

```text
Developer PC / CI Server
→ docker build
→ docker push
→ Production Server
→ docker pull
→ docker compose up -d
```

Spring Boot 배포 예시:

```bash
./gradlew clean bootJar
docker build -t registry.example.com/festapick-api:1.0.0 .
docker push registry.example.com/festapick-api:1.0.0
```

운영 서버 실행:

```bash
docker pull registry.example.com/festapick-api:1.0.0
docker compose up -d
docker compose logs -f app
```

운영 Compose는 Image 기반 실행을 권장한다.

```yaml
services:
  app:
    image: registry.example.com/festapick-api:1.0.0
    ports:
      - "8080:8080"
    environment:
      SPRING_PROFILES_ACTIVE: prod
    restart: unless-stopped
```

---

### [주의]

운영 서버에서 Source Code를 직접 수정하거나 Container 내부를 수동 수정하면 재현성이 깨진다.

비권장 흐름:

```text
Production Server 접속
→ Container 내부 수정
→ 임시 반영
→ 재배포 시 변경 사항 유실
```

권장 흐름:

```text
Git Commit
→ Image Build
→ Registry Push
→ Server Pull
→ Container Recreate
```

주의할 점:

- 운영 Secret 하드코딩 금지
- `latest` 단독 배포 지양
- DB Volume 삭제 주의
- 운영 DB Port 외부 공개 지양
- Health Check 없이 배포 완료 판단 금지
- Logs 확인 없이 배포 종료 금지
- Rollback 가능한 Image Tag 유지

---

### [FAQ]

Q. Docker Deployment란?
A. Docker Image를 Registry에 저장하고 운영 서버에서 Container로 실행하는 배포 과정이다.

Q. Docker 배포의 핵심 원칙은?
A. 동일한 Image를 여러 환경에서 재현 가능하게 실행하는 것이다.

Q. 운영 서버에서 Docker Image를 다시 Build해도 되는가?
A. 가능은 하지만 권장하지 않는다. CI에서 Build한 Image를 Registry에 Push하고 운영 서버에서는 Pull하여 실행하는 방식이 좋다.

Q. Container 내부를 직접 수정해도 되는가?
A. 권장하지 않는다. 변경은 Dockerfile, Compose, Source Code에 반영하고 Image를 다시 Build해야 한다.

---

# 2. Image Tagging Strategy

## 2.1 Image Tag

### [개념]

Image Tag는 Docker Image Version을 식별하는 이름이다.

```text
image-name:tag
```

예:

```text
festapick-api:1.0.0
festapick-api:2026.06.26
festapick-api:git-abc1234
```

Image Tag는 배포 추적, Rollback, 장애 분석에 사용된다.

---

### [핵심]

Image Tag 핵심:

- Image Version 식별
- 배포 이력 추적
- Rollback 기준
- Registry 관리 기준
- CI/CD Build 결과 식별
- `latest` 단독 사용 지양
- Git Commit과 연결 권장

Tag 예시:

| Tag         | Meaning          |
| ----------- | ---------------- |
| latest      | 최신 Image 관례  |
| 1.0.0       | Semantic Version |
| 2026.06.26  | Date Version     |
| git-abc1234 | Git Commit 기반  |
| prod        | 운영 채널        |
| staging     | 스테이징 채널    |

---

### [실무]

권장 Tag 전략:

```text
ServiceName:SemanticVersion
ServiceName:GitCommit
ServiceName:Date-BuildNumber
```

예시:

```bash
docker build -t registry.example.com/festapick-api:1.0.0 .
docker build -t registry.example.com/festapick-api:git-abc1234 .
docker push registry.example.com/festapick-api:1.0.0
docker push registry.example.com/festapick-api:git-abc1234
```

운영 Compose:

```yaml
services:
  app:
    image: registry.example.com/festapick-api:1.0.0
```

Rollback:

```yaml
services:
  app:
    image: registry.example.com/festapick-api:0.9.9
```

---

### [주의]

`latest`는 실제 Version을 설명하지 않는다.

비권장:

```yaml
services:
  app:
    image: festapick-api:latest
```

권장:

```yaml
services:
  app:
    image: festapick-api:1.0.0
```

주의할 점:

- 동일 Tag 덮어쓰기 주의
- 운영 배포 Tag 기록
- Rollback 가능한 이전 Image 유지
- Registry 정리 정책 필요
- Image Tag와 Git Commit 연결 권장
- Compose 파일에 적용된 Tag 확인

---

### [FAQ]

Q. Docker Image Tag란?
A. Docker Image Version을 식별하는 이름이다.

Q. 운영에서 latest만 사용하면 안 되는 이유는?
A. 실제 배포 Version 추적과 Rollback이 어렵기 때문이다.

Q. Rollback을 쉽게 하려면 어떻게 해야 하는가?
A. 명확한 Version Tag를 사용하고 이전 Image를 Registry에 유지해야 한다.

---

# 3. Registry Deployment

## 3.1 Registry Push and Pull

### [개념]

Registry Deployment는 Image를 Docker Registry에 Push하고 서버에서 Pull하여 실행하는 배포 방식이다.

```text
Local / CI Image
→ docker push
→ Registry
→ docker pull
→ Production Server
```

Registry는 Docker Hub, GitHub Container Registry, AWS ECR, Private Registry 등을 사용할 수 있다.

---

### [핵심]

Registry Deployment 핵심:

- Image 중앙 저장
- 서버 간 Image 공유
- CI/CD 연동
- Private Image 권한 관리
- Version Tag 관리
- 배포 서버 Pull 기반 실행
- Rollback Image 유지

기본 명령어:

```bash
docker login registry.example.com
docker tag festapick-api:1.0.0 registry.example.com/festapick-api:1.0.0
docker push registry.example.com/festapick-api:1.0.0
docker pull registry.example.com/festapick-api:1.0.0
```

---

### [실무]

CI/CD 배포 흐름:

```text
Git Push
→ Test
→ Build Jar
→ Build Docker Image
→ Push Registry
→ SSH Server
→ Pull Image
→ Compose Up
→ Health Check
```

운영 서버 Compose:

```yaml
services:
  app:
    image: registry.example.com/festapick-api:1.0.0
    restart: unless-stopped
    env_file:
      - .env.prod
    ports:
      - "8080:8080"
```

서버 반영:

```bash
docker compose pull
docker compose up -d
docker compose ps
docker compose logs --tail=100 app
```

---

### [주의]

Private Registry 인증 정보는 안전하게 관리해야 한다.

주의할 점:

- Registry Credential 노출 금지
- Public Registry에 Secret 포함 Image Push 금지
- Push 전 Image Scan 고려
- 운영 서버에서 `docker login` Credential 관리
- Tag 충돌 방지
- 오래된 Image 정리 정책 필요
- Rollback용 Image 삭제 주의

---

### [FAQ]

Q. Docker Registry Deployment란?
A. Image를 Registry에 Push하고 서버에서 Pull하여 Container로 실행하는 배포 방식이다.

Q. Registry를 사용하는 이유는?
A. Image를 중앙에서 관리하고 여러 서버나 CI/CD Pipeline에서 동일한 Image를 사용할 수 있기 때문이다.

Q. Private Registry 사용 시 주의할 점은?
A. 인증 정보와 Image 접근 권한을 안전하게 관리해야 한다.

---

# 4. Environment and Secret Injection

## 4.1 Runtime Environment

### [개념]

Runtime Environment는 Container 실행 시 주입되는 환경 설정이다.

Docker Image는 환경에 독립적으로 만들고, 환경별 값은 Runtime에 주입한다.

```text
Same Image
+ dev env
→ Dev Container

Same Image
+ prod env
→ Prod Container
```

---

### [핵심]

Runtime Environment 핵심:

- Image와 Config 분리
- Spring Profile 주입
- DB URL 주입
- Redis Host 주입
- External API Endpoint 주입
- Secret은 별도 관리
- 환경별 Compose 분리 가능
- `docker compose config`로 최종 값 확인

Spring Boot 환경변수 예시:

```text
SPRING_PROFILES_ACTIVE
SPRING_DATASOURCE_URL
SPRING_DATASOURCE_USERNAME
SPRING_DATASOURCE_PASSWORD
SPRING_DATA_REDIS_HOST
JWT_SECRET
```

---

### [실무]

Compose Runtime Env:

```yaml
services:
  app:
    image: registry.example.com/festapick-api:1.0.0
    environment:
      SPRING_PROFILES_ACTIVE: prod
      SPRING_DATASOURCE_URL: jdbc:mysql://mysql:3306/festapick
      SPRING_DATASOURCE_USERNAME: festapick
      SPRING_DATASOURCE_PASSWORD: ${DB_PASSWORD}
      JWT_SECRET: ${JWT_SECRET}
```

`.env.prod`:

```env
DB_PASSWORD=change-this
JWT_SECRET=change-this
```

운영에서는 `.env.prod` 대신 다음 방식을 우선 고려한다.

- CI/CD Secret
- Server Environment Variable
- Docker Secret
- Cloud Secret Manager
- Vault

---

### [주의]

Secret을 Image, Dockerfile, Compose File, Git Repository에 직접 작성하면 안 된다.

비권장:

```dockerfile
ENV DB_PASSWORD=real-password
```

비권장:

```yaml
environment:
  JWT_SECRET: real-secret
```

권장:

```yaml
environment:
  JWT_SECRET: ${JWT_SECRET}
```

주의할 점:

- `.env` Git Commit 금지
- `.env.example`만 Commit
- 운영 Secret Rotation 고려
- `docker inspect`로 환경변수가 보일 수 있음
- 민감 값 로그 출력 금지

---

### [FAQ]

Q. Runtime Environment란?
A. Container 실행 시 주입되는 환경 설정이다.

Q. Docker Image에 운영 설정을 포함해도 되는가?
A. 권장하지 않는다. Image는 환경 독립적으로 만들고 운영 설정은 Runtime에 주입해야 한다.

Q. Docker에서 Secret을 어디에 저장하면 안 되는가?
A. Dockerfile, Image, Compose 파일, Git Repository에 하드코딩하면 안 된다.

---

# 5. Volume Deployment

## 5.1 Persistent Data Deployment

### [개념]

Volume Deployment는 Container 삭제 후에도 유지되어야 하는 데이터를 Docker Volume 또는 External Storage에 저장하는 방식이다.

Container 내부 Writable Layer는 Container 삭제 시 사라질 수 있다.

```text
Container Writable Layer
→ Temporary

Docker Volume
→ Persistent
```

---

### [핵심]

Volume이 필요한 데이터:

- Database Data
- Uploaded Files
- Redis Append Only File
- Application Persistent File
- Backup File
- Certificate File

Volume 유형:

| Type             | Usage                        |
| ---------------- | ---------------------------- |
| Named Volume     | Docker 관리 영속 저장소      |
| Bind Mount       | Host 경로 직접 연결          |
| External Storage | Cloud / NFS / Object Storage |

---

### [실무]

MySQL Named Volume:

```yaml
services:
  mysql:
    image: mysql:8.4
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```

Upload File Bind Mount:

```yaml
services:
  app:
    image: festapick-api:1.0.0
    volumes:
      - /srv/festapick/uploads:/app/uploads
```

Backup Flow:

```text
Database Volume
→ Backup Command
→ Backup File
→ External Storage
```

---

### [주의]

`docker compose down -v`는 Volume을 삭제할 수 있다.

위험 명령:

```bash
docker compose down -v
```

주의할 점:

- DB Volume 삭제 주의
- 운영 Upload 경로 백업 필요
- Bind Mount 권한 확인
- Non-root User 사용 시 Volume 권한 확인
- Log File은 Volume보다 stdout / stderr 권장
- Volume 이름과 Project 이름 관계 확인
- Volume 삭제 전 Backup 확인

---

### [FAQ]

Q. Docker Volume Deployment란?
A. Container 삭제 후에도 유지되어야 하는 데이터를 Volume 또는 외부 저장소에 보관하는 배포 방식이다.

Q. Database에 Volume이 필요한 이유는?
A. Container 삭제 또는 재생성 후에도 Database 데이터를 유지하기 위해 필요하다.

Q. docker compose down -v는 왜 위험한가?
A. Named Volume까지 삭제하여 Database 또는 Upload 데이터가 사라질 수 있기 때문이다.

---

# 6. Network Deployment

## 6.1 Deployment Network Pattern

### [개념]

Network Deployment는 Container 간 통신과 외부 접근 경로를 설계하는 과정이다.

Docker 배포에서는 Service Name, Container Port, Host Port, Reverse Proxy, Firewall을 함께 고려한다.

```text
User
→ Host Port
→ Reverse Proxy
→ App Container
→ DB Container
```

---

### [핵심]

Network Deployment 핵심:

- Service Name 기반 내부 통신
- Host Port 최소 공개
- DB Port 외부 공개 지양
- Reverse Proxy 사용
- Frontend Network / Backend Network 분리
- Firewall / Security Group 설정
- Container Port와 Host Port 구분

Port 개념:

| Type           | Meaning                         |
| -------------- | ------------------------------- |
| Host Port      | 외부에서 접근하는 서버 Port     |
| Container Port | Container 내부 Application Port |
| Service Name   | Compose 내부 DNS 이름           |

---

### [실무]

Reverse Proxy 기반 구조:

```yaml
services:
  nginx:
    image: nginx:1.27
    ports:
      - "80:80"
      - "443:443"
    networks:
      - frontend_network

  app:
    image: festapick-api:1.0.0
    expose:
      - "8080"
    networks:
      - frontend_network
      - backend_network

  mysql:
    image: mysql:8.4
    expose:
      - "3306"
    networks:
      - backend_network

networks:
  frontend_network:
  backend_network:
```

통신 흐름:

```text
Client
→ nginx:80/443
→ app:8080
→ mysql:3306
```

---

### [주의]

운영 DB Port를 외부에 공개하면 보안 위험이 증가한다.

비권장:

```yaml
mysql:
  ports:
    - "3306:3306"
```

권장:

```yaml
mysql:
  expose:
    - "3306"
```

주의할 점:

- `localhost`는 Container 자기 자신
- 내부 통신은 Service Name 사용
- Host Port 충돌 확인
- Cloud Firewall 확인
- Nginx Proxy Target은 Service Name 사용
- HTTPS 인증서 관리 필요

---

### [FAQ]

Q. Docker 배포에서 내부 통신은 어떻게 하는가?
A. 같은 Docker Network에 있는 Service끼리는 Service Name과 Container Port로 통신한다.

Q. 운영에서 DB Port를 외부 공개해도 되는가?
A. 권장하지 않는다. DB는 Backend Network 내부에서만 접근하도록 제한하는 것이 좋다.

Q. Reverse Proxy는 Docker 배포에서 어떤 역할을 하는가?
A. 외부 요청을 받아 App Container로 전달하고 HTTPS, Routing, Static File Serving을 처리한다.

---

# 7. Logs and Monitoring

## 7.1 Docker Logs

### [개념]

Docker Logs는 Container의 stdout / stderr 출력을 수집하고 조회하는 기능이다.

Container 환경에서는 Application이 File Log보다 Console Log를 출력하는 방식이 권장된다.

```text
Application stdout/stderr
→ Docker Log Driver
→ docker logs
→ Log Aggregation
```

---

### [핵심]

로그 확인 명령:

```bash
docker logs app
docker logs -f app
docker logs --tail=100 app
docker compose logs -f app
```

Logs 핵심:

- 장애 분석 1차 도구
- Startup Error 확인
- Runtime Exception 확인
- Restart Loop 확인
- Health Check 실패 원인 확인
- stdout / stderr 기반 수집
- 배포 완료 검증에 필수

---

### [실무]

Spring Boot Container 로그 권장:

```properties
logging.file.name=
logging.level.root=INFO
```

Compose Logging Rotation:

```yaml
services:
  app:
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
```

운영 로그 흐름:

```text
Spring Boot Console Log
→ Docker json-file
→ Log Rotation
→ Centralized Logging
```

중앙 로그 시스템 후보:

- Loki
- Elasticsearch
- OpenSearch
- CloudWatch Logs
- Grafana
- Prometheus + Alertmanager

---

### [주의]

로그에 Secret, Token, Password, 개인정보를 출력하면 안 된다.

주의할 점:

- JWT 로그 출력 금지
- DB Password 출력 금지
- API Key 출력 금지
- 너무 큰 로그 파일 방지
- 로그 Rotation 설정
- Container 내부 파일 로그 의존 지양
- Restart Loop 시 로그 폭증 주의

---

### [FAQ]

Q. Docker Logs란?
A. Container의 stdout / stderr 출력을 수집하고 조회하는 기능이다.

Q. Container 환경에서 File Log보다 Console Log가 권장되는 이유는?
A. Docker가 stdout / stderr를 표준 방식으로 수집하고 외부 로그 시스템과 연동하기 쉽기 때문이다.

Q. 운영에서 로그 설정 시 중요한 점은?
A. 민감 정보 출력 금지, 로그 Rotation, 중앙 로그 수집, 장애 분석 가능성이 중요하다.

---

## 7.2 Container Monitoring

### [개념]

Container Monitoring은 Container 상태, Resource Usage, Health Status, Logs를 관찰하는 과정이다.

```text
Container Status
+ CPU
+ Memory
+ Logs
+ Health Check
→ Monitoring
```

---

### [핵심]

Monitoring 항목:

- Container Running Status
- Health Status
- CPU Usage
- Memory Usage
- Restart Count
- Network I/O
- Disk I/O
- Logs
- Application Metrics

기본 명령:

```bash
docker ps
docker stats
docker inspect app
docker compose ps
```

---

### [실무]

상태 확인:

```bash
docker compose ps
```

Resource 확인:

```bash
docker stats
```

Health Check 확인:

```bash
docker inspect app
```

Spring Boot Actuator Metrics:

```text
/actuator/health
/actuator/metrics
/actuator/prometheus
```

운영 확장:

```text
Spring Boot Actuator
→ Prometheus
→ Grafana
→ Alertmanager
```

---

### [주의]

Container가 Running 상태라고 Application이 정상이라는 뜻은 아니다.

구분:

| Status     | Meaning           |
| ---------- | ----------------- |
| Running    | Process 실행 중   |
| Healthy    | Health Check 정상 |
| Unhealthy  | Health Check 실패 |
| Restarting | 반복 재시작       |
| Exited     | Process 종료      |

주의할 점:

- Running만 보고 정상 판단 금지
- Health Check 설정 필요
- Memory 사용량 모니터링
- OOMKilled 확인
- Restart Count 확인
- Application Metrics와 함께 판단

---

### [FAQ]

Q. Docker Monitoring에서 가장 먼저 확인할 것은?
A. `docker compose ps`, `docker logs`, `docker stats`, Health Check 상태를 확인한다.

Q. Running 상태이면 Application이 정상인가?
A. 아니다. Process가 실행 중이라는 뜻일 뿐이며 Health Check와 Application 응답을 확인해야 한다.

Q. docker stats는 무엇인가?
A. Container의 CPU, Memory, Network, Block I/O 사용량을 실시간으로 보여주는 명령이다.

---

# 8. Health Check and Readiness

## 8.1 Health Check

### [개념]

Health Check는 Container 또는 Application이 정상적으로 요청을 처리할 준비가 되었는지 확인하는 메커니즘이다.

Docker에서는 Dockerfile `HEALTHCHECK` 또는 Compose `healthcheck`로 설정한다.

```text
Container Running
→ Health Check
→ healthy / unhealthy
```

---

### [핵심]

Health Check 핵심:

- Process 실행 여부 이상의 상태 확인
- Application Ready 판단
- DB / Redis 연결 상태 확인 가능
- Restart 판단 보조
- Deployment Validation에 사용
- depends_on condition과 연계 가능
- Running과 Healthy 상태 구분

Spring Boot Health Endpoint:

```text
/actuator/health
```

---

### [실무]

Spring Boot Compose Health Check:

```yaml
services:
  app:
    image: festapick-api:1.0.0
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:8080/actuator/health"]
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 30s
```

MySQL Health Check:

```yaml
services:
  mysql:
    image: mysql:8.4
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 10
```

배포 후 검증:

```bash
docker compose ps
curl http://localhost:8080/actuator/health
docker compose logs --tail=100 app
```

---

### [주의]

Health Check 명령에 필요한 도구가 Image 안에 있어야 한다.

자주 발생:

| Problem        | Cause                     | Solution                 |
| -------------- | ------------------------- | ------------------------ |
| curl not found | Runtime Image에 curl 없음 | wget 사용 또는 curl 설치 |
| Actuator 404   | Actuator Dependency 없음  | dependency 추가          |
| unauthorized   | Health Endpoint 보안 설정 | Security 설정 확인       |
| timeout        | Startup 느림              | start_period 증가        |
| unhealthy      | App 내부 장애             | logs 확인                |

주의할 점:

- Health Endpoint 공개 범위 관리
- 너무 잦은 Health Check 지양
- Startup 시간이 긴 App은 start_period 설정
- Running과 Healthy 구분
- Health Check 실패 원인 로그 확인

---

### [FAQ]

Q. Health Check란?
A. Container 또는 Application이 정상적으로 요청을 처리할 준비가 되었는지 확인하는 메커니즘이다.

Q. Spring Boot Docker Health Check는 무엇을 사용하면 좋은가?
A. Spring Boot Actuator의 `/actuator/health` Endpoint를 사용하는 것이 일반적이다.

Q. Container가 Running인데 unhealthy일 수 있는가?
A. 가능하다. Process는 실행 중이지만 Application 상태 점검에 실패한 것이다.

---

# 9. Resource Limit and Performance

## 9.1 Resource Limit

### [개념]

Resource Limit은 Container가 사용할 CPU와 Memory를 제한하는 설정이다.

Resource Limit은 Container 간 자원 간섭을 줄이고 Host 안정성을 높인다.

```text
Host Resource
→ CPU Limit
→ Memory Limit
→ Container Isolation
```

---

### [핵심]

Resource Limit 핵심:

- CPU 제한
- Memory 제한
- OOM 방지
- Host 안정성 확보
- Container 간 영향 감소
- JVM Heap 설정과 연계 필요
- 성능 향상보다 장애 확산 방지 목적

Compose 예시:

```yaml
services:
  app:
    image: festapick-api:1.0.0
    mem_limit: 1g
    cpus: 1.0
```

---

### [실무]

Spring Boot Resource 설정:

```yaml
services:
  app:
    image: festapick-api:1.0.0
    mem_limit: 1g
    cpus: 1.0
    environment:
      JAVA_OPTS: "-Xms256m -Xmx768m"
```

JVM Memory 구조:

```text
Container Memory Limit
→ JVM Heap
→ Metaspace
→ Thread Stack
→ Direct Memory
→ Native Memory
```

성능 점검 명령:

```bash
docker stats
docker inspect app
docker compose logs app
```

---

### [주의]

Container Memory Limit과 JVM Heap을 동일하게 잡으면 OOM 위험이 있다.

비권장:

```text
mem_limit: 1g
JAVA_OPTS: -Xmx1g
```

권장:

```text
mem_limit: 1g
JAVA_OPTS: -Xmx768m
```

주의할 점:

- JVM Heap 외 Memory 여유 필요
- MySQL / Redis Memory 별도 고려
- OOMKilled 여부 확인
- CPU 제한이 너무 낮으면 응답 지연 발생
- Resource Limit은 성능 향상보다 안정성 목적

---

### [FAQ]

Q. Docker Resource Limit이란?
A. Container가 사용할 CPU와 Memory를 제한하는 설정이다.

Q. Spring Boot Container에서 Xmx는 어떻게 설정해야 하는가?
A. Container Memory Limit보다 작게 설정하고 Non-Heap Memory 여유를 남겨야 한다.

Q. OOMKilled는 무엇인가?
A. Container가 Memory Limit을 초과하여 Docker 또는 Kernel에 의해 종료된 상태이다.

---

## 9.2 Docker Performance Optimization

### [개념]

Docker Performance Optimization은 Build Speed, Startup Time, Image Size, Runtime Resource Usage를 개선하는 과정이다.

```text
Build Speed
+ Image Size
+ Startup Time
+ Runtime Memory
→ Docker Performance
```

---

### [핵심]

성능 최적화 대상:

- Image Size
- Build Cache
- Layer Count
- Startup Time
- Memory Usage
- CPU Usage
- Network I/O
- Disk I/O
- Volume Performance

최적화 방법:

- `.dockerignore` 사용
- Multi-stage Build 사용
- 불필요 Package 제거
- Layer Cache 순서 최적화
- 작은 Runtime Image 사용
- Resource Limit 설정
- Application Startup 최적화
- Logs Rotation 설정

---

### [실무]

Image Size 확인:

```bash
docker images
```

Layer 확인:

```bash
docker history festapick-api:1.0.0
```

Build Cache 최적화:

```dockerfile
COPY build.gradle settings.gradle ./
COPY gradle ./gradle
RUN gradle dependencies --no-daemon

COPY src ./src
RUN gradle clean bootJar --no-daemon
```

Runtime 최적화:

```yaml
services:
  app:
    mem_limit: 1g
    cpus: 1.0
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
```

---

### [주의]

무조건 작은 Image가 항상 좋은 것은 아니다.

주의할 점:

- Alpine Image는 일부 Native Library 호환 이슈 가능
- Debug Tool이 없으면 장애 분석이 어려울 수 있음
- 너무 낮은 Resource Limit은 장애 원인
- Cache 최적화와 보안 모두 고려
- Premature Optimization 지양

---

### [FAQ]

Q. Docker 성능 최적화 대상은 무엇인가?
A. Build Speed, Image Size, Startup Time, Runtime CPU / Memory, Logs, Volume I/O가 주요 대상이다.

Q. Image Size를 줄이는 대표 방법은?
A. Multi-stage Build, `.dockerignore`, 작은 Runtime Image, 불필요 Package 제거를 사용한다.

Q. Build 속도를 높이는 대표 방법은?
A. Layer Cache를 활용하도록 변경이 적은 Dependency 파일을 먼저 COPY한다.

---

# 10. Deployment Patterns

## 10.1 Single Server Compose Deployment

### [개념]

Single Server Compose Deployment는 하나의 서버에서 Docker Compose로 Application, Database, Cache, Reverse Proxy를 함께 실행하는 배포 방식이다.

개인 프로젝트, 학습용 서버, 소규모 서비스, 내부 도구에 적합하다.

```text
Single Server
├─ nginx
├─ app
├─ mysql
└─ redis
```

---

### [핵심]

Single Server Compose 구성:

- Nginx Reverse Proxy
- Spring Boot App
- MySQL
- Redis
- Named Volume
- Internal Network
- Health Check
- Restart Policy
- Log Rotation
- Backup Script

---

### [실무]

운영 예시:

```yaml
services:
  nginx:
    image: nginx:1.27
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/conf.d:/etc/nginx/conf.d:ro
      - ./certs:/etc/nginx/certs:ro
    depends_on:
      app:
        condition: service_healthy
    networks:
      - frontend_network
    restart: unless-stopped

  app:
    image: registry.example.com/festapick-api:1.0.0
    env_file:
      - .env.prod
    expose:
      - "8080"
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:8080/actuator/health"]
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 30s
    networks:
      - frontend_network
      - backend_network
    restart: unless-stopped

  mysql:
    image: mysql:8.4
    env_file:
      - .env.mysql
    volumes:
      - mysql_data:/var/lib/mysql
    expose:
      - "3306"
    networks:
      - backend_network
    restart: unless-stopped

  redis:
    image: redis:7.4
    expose:
      - "6379"
    networks:
      - backend_network
    restart: unless-stopped

volumes:
  mysql_data:

networks:
  frontend_network:
  backend_network:
```

---

### [주의]

Single Server 구성은 단순하지만 서버 장애 시 전체 서비스가 중단될 수 있다.

주의할 점:

- DB Backup 필수
- 서버 Disk 사용량 모니터링
- Docker Log Rotation 설정
- TLS 인증서 갱신 관리
- MySQL 외부 공개 금지
- `.env` 권한 관리
- 서버 재부팅 후 자동 실행 확인
- 장애 복구 절차 문서화

---

### [FAQ]

Q. Single Server Compose Deployment란?
A. 하나의 서버에서 Docker Compose로 App, DB, Cache, Reverse Proxy를 함께 실행하는 배포 방식이다.

Q. Single Server Compose는 언제 적합한가?
A. 개인 프로젝트, 학습용 서버, 소규모 서비스, 내부 도구에 적합하다.

Q. Single Server Compose의 가장 큰 단점은?
A. 서버 하나에 장애가 발생하면 전체 서비스가 중단될 수 있다는 점이다.

---

## 10.2 Blue-Green Deployment Concept

### [개념]

Blue-Green Deployment는 기존 버전과 새 버전을 동시에 준비한 뒤 트래픽을 새 버전으로 전환하는 배포 방식이다.

```text
Blue Version: Current
Green Version: New
Traffic Switch
→ Green
```

Docker 환경에서는 App Container를 두 개의 Version으로 실행하고 Reverse Proxy Target을 전환하는 방식으로 구현할 수 있다.

---

### [핵심]

Blue-Green 핵심:

- 무중단 배포에 유리
- 빠른 Rollback 가능
- 두 버전 동시 실행 필요
- Reverse Proxy 전환 필요
- DB Migration 호환성 중요
- Resource 여유 필요
- Health Check 기반 전환 필요

---

### [실무]

개념 구조:

```text
nginx
├─ app-blue:8080
└─ app-green:8080
```

배포 흐름:

```text
Current: app-blue
→ Deploy app-green
→ Health Check app-green
→ Switch nginx upstream to app-green
→ Monitor
→ Remove app-blue later
```

Rollback:

```text
Problem in green
→ Switch nginx upstream back to blue
```

---

### [주의]

Blue-Green Deployment는 DB Schema 변경과 함께 사용할 때 주의가 필요하다.

주의할 점:

- 이전 버전과 새 버전의 DB 호환성 유지
- Migration은 backward compatible하게 설계
- 두 버전 동시 실행 Resource 필요
- Session State 외부화 필요
- Upload File 공유 경로 필요
- Health Check 통과 후 Traffic 전환

---

### [FAQ]

Q. Blue-Green Deployment란?
A. 기존 버전과 새 버전을 동시에 준비한 뒤 트래픽을 새 버전으로 전환하는 배포 방식이다.

Q. Blue-Green Deployment의 장점은?
A. 무중단 배포와 빠른 Rollback이 가능하다는 점이다.

Q. Docker에서 Blue-Green을 구현하려면 무엇이 필요한가?
A. 두 App Container, Reverse Proxy, Health Check, Rollback 절차가 필요하다.

---

# 11. Rollback

## 11.1 Docker Rollback

### [개념]

Docker Rollback은 문제가 발생한 새 배포를 중단하고 이전 정상 Image Version으로 되돌리는 과정이다.

```text
New Version Failed
→ Stop New Container
→ Use Previous Image Tag
→ Recreate Container
→ Health Check
```

---

### [핵심]

Rollback 핵심:

- 이전 Image Tag 유지
- Compose Image Tag 변경
- Container Recreate
- Health Check 확인
- Logs 확인
- DB Migration 영향 확인
- 배포 기록 관리

Rollback 대상:

| Target         | Rollback Method               |
| -------------- | ----------------------------- |
| App Image      | 이전 Image Tag로 변경         |
| Compose Config | 이전 compose 파일 사용        |
| Environment    | 이전 env 값 복구              |
| DB Schema      | 별도 Migration Rollback 필요  |
| Static File    | 이전 Image 또는 Artifact 사용 |

---

### [실무]

현재 Compose:

```yaml
services:
  app:
    image: registry.example.com/festapick-api:1.0.1
```

Rollback Compose:

```yaml
services:
  app:
    image: registry.example.com/festapick-api:1.0.0
```

반영:

```bash
docker compose pull app
docker compose up -d app
docker compose ps
docker compose logs --tail=100 app
curl http://localhost:8080/actuator/health
```

Rollback 전 확인:

```text
- 이전 Image 존재 여부
- DB Migration 호환 여부
- Env 변경 여부
- Volume 변경 여부
- External API 변경 여부
```

---

### [주의]

Application Rollback은 쉽지만 Database Rollback은 어렵다.

주의할 점:

- DB Migration은 backward compatible하게 설계
- Column 삭제보다 단계적 제거 권장
- Data Migration 전 Backup 필수
- 새 Version에서 만든 데이터가 이전 Version과 호환되는지 확인
- Rollback 후 Health Check와 주요 API 테스트 필요
- Rollback Image가 Registry에 남아 있어야 함

---

### [FAQ]

Q. Docker Rollback이란?
A. 문제가 발생한 새 배포를 중단하고 이전 정상 Image Version으로 되돌리는 과정이다.

Q. Docker Rollback을 쉽게 하려면 무엇이 필요한가?
A. 명확한 Image Tag, 이전 Image 보관, Compose Config 이력, Health Check가 필요하다.

Q. DB Migration이 포함된 배포는 왜 Rollback이 어려운가?
A. Application Version만 되돌려도 Database Schema나 Data가 이전 Version과 호환되지 않을 수 있기 때문이다.

---

# 12. Backup and Restore

## 12.1 Backup Strategy

### [개념]

Backup은 Docker Volume, Database, Uploaded File, Configuration, Secret을 장애나 실수로부터 복구하기 위해 보관하는 과정이다.

Docker 배포에서 Container는 재생성 가능하지만 Data는 반드시 백업해야 한다.

```text
Container
→ Recreate Possible

Data Volume
→ Backup Required
```

---

### [핵심]

Backup 대상:

- MySQL Database
- PostgreSQL Database
- Redis Persistent Data
- Uploaded Files
- `.env` Template
- Compose File
- Nginx Config
- SSL Certificate
- Volume Data

Backup 원칙:

- 정기 백업
- 외부 저장소 보관
- 복구 테스트
- 암호화
- 접근 권한 제한
- 백업 보관 주기 관리
- 자동 백업 실패 알림

---

### [실무]

MySQL Dump Backup:

```bash
docker compose exec mysql \
  mysqldump -u root -p appdb > backup.sql
```

MySQL Restore:

```bash
docker compose exec -T mysql \
  mysql -u root -p appdb < backup.sql
```

Upload Directory Backup:

```bash
tar -czf uploads-backup.tar.gz /srv/festapick/uploads
```

Volume 확인:

```bash
docker volume ls
docker volume inspect mysql_data
```

---

### [주의]

Backup은 생성보다 Restore 검증이 더 중요하다.

주의할 점:

- Backup 파일이 실제 복구 가능한지 테스트
- DB Password 노출 주의
- Backup 파일 암호화
- Backup을 같은 서버에만 두지 않기
- Volume 삭제 전 Backup 확인
- 자동 백업 실패 알림 필요
- 개인정보 포함 시 접근 제어 필요

---

### [FAQ]

Q. Docker 배포에서 무엇을 백업해야 하는가?
A. Database, Upload File, Volume Data, Compose 설정, Nginx 설정, 인증서, Secret 관리 정보를 백업해야 한다.

Q. Container 자체를 백업해야 하는가?
A. 일반적으로 아니다. Container는 Image와 Compose로 재생성하고, Data를 백업하는 것이 핵심이다.

Q. Backup에서 가장 중요한 검증은 무엇인가?
A. Restore가 실제로 가능한지 테스트하는 것이다.

---

# 13. Security Deployment Rules

## 13.1 Docker Deployment Security

### [개념]

Docker Deployment Security는 Image, Container, Network, Secret, Volume, Host 권한을 안전하게 관리하는 배포 기준이다.

Docker는 격리를 제공하지만 보안 설정이 없으면 운영 위험이 발생한다.

```text
Secure Image
+ Secure Runtime
+ Secure Network
+ Secure Secret
+ Secure Host
→ Safer Deployment
```

---

### [핵심]

Security 핵심:

- Secret 하드코딩 금지
- Non-root User 실행
- 불필요 Port 공개 금지
- DB 외부 공개 금지
- 최소 Base Image 사용
- Image Vulnerability Scan
- Docker Socket Mount 금지
- Privileged Mode 지양
- Read-only Mount 사용
- Container Capability 최소화
- Log에 민감 정보 출력 금지

---

### [실무]

Non-root User Dockerfile:

```dockerfile
RUN useradd -r -u 1001 appuser
RUN chown -R appuser:appuser /app
USER appuser
```

Read-only Config Mount:

```yaml
services:
  nginx:
    volumes:
      - ./nginx/conf.d:/etc/nginx/conf.d:ro
```

DB 내부 Network 제한:

```yaml
services:
  mysql:
    expose:
      - "3306"
    networks:
      - backend_network
```

Secret Runtime Injection:

```yaml
environment:
  JWT_SECRET: ${JWT_SECRET}
```

---

### [주의]

Docker Socket Mount는 매우 강한 권한을 제공한다.

위험 예시:

```yaml
volumes:
  - /var/run/docker.sock:/var/run/docker.sock
```

주의할 점:

- `/var/run/docker.sock` Mount 금지 또는 최소화
- `privileged: true` 지양
- Root Container 운영 지양
- Public Image 신뢰성 확인
- Image Scan 수행
- 불필요 Linux Capability 제거 고려
- Host Firewall 설정
- Secret Rotation 정책 필요

---

### [FAQ]

Q. Docker 배포 보안에서 가장 중요한 것은?
A. Secret 하드코딩 금지, Non-root 실행, Port 최소 공개, DB 내부망 제한, Docker Socket Mount 회피이다.

Q. Docker Socket Mount가 위험한 이유는?
A. Container가 Host Docker Daemon을 제어할 수 있어 Root 수준 권한으로 이어질 수 있기 때문이다.

Q. 운영 DB Port를 외부 공개하면 안 되는 이유는?
A. 공격면이 증가하고 인증 취약점이나 설정 실수로 데이터 유출 위험이 커지기 때문이다.

---

# 14. Troubleshooting Core

## 14.1 Docker Troubleshooting Flow

### [개념]

Docker Troubleshooting은 Container 실행 실패, Build 실패, Network 오류, Volume 문제, Resource 문제를 원인별로 분석하는 과정이다.

```text
Problem
→ Status Check
→ Logs Check
→ Config Check
→ Inspect
→ Resource Check
→ Fix
```

---

### [핵심]

기본 진단 명령:

```bash
docker ps
docker ps -a
docker logs container_name
docker inspect container_name
docker stats
docker images
docker volume ls
docker network ls
docker compose ps
docker compose logs
docker compose config
```

Troubleshooting 우선순위:

1. Container 상태 확인
2. Logs 확인
3. Compose Config 확인
4. Environment Variable 확인
5. Network / Service Name 확인
6. Volume / Permission 확인
7. Port Conflict 확인
8. Resource / OOM 확인
9. Image / Tag 확인
10. Health Check 확인

---

### [실무]

문제 해결 기본 순서:

```bash
docker compose ps
docker compose logs --tail=100 app
docker compose config
docker inspect app
docker stats
```

Container 내부 확인:

```bash
docker compose exec app sh
env
ls -al
```

Image 확인:

```bash
docker images
docker history festapick-api:1.0.0
```

Network 확인:

```bash
docker network ls
docker network inspect project_backend_network
```

---

### [주의]

Container 내부에서 수동 수정하여 문제를 해결하면 안 된다.

비권장:

```text
docker exec app sh
→ 설정 파일 수정
→ 임시 해결
```

권장:

```text
Dockerfile / Compose / Env 수정
→ Rebuild or Recreate
→ Verify
```

주의할 점:

- 증상과 원인 구분
- Restart로 덮지 않기
- Logs 없이 추측하지 않기
- Compose 변수 치환 결과 확인
- 운영 데이터 삭제 명령 주의
- `docker system prune -a --volumes` 신중 사용

---

### [FAQ]

Q. Docker 문제 해결은 무엇부터 확인해야 하는가?
A. Container 상태, Logs, Compose Config, Inspect 정보를 먼저 확인해야 한다.

Q. docker compose config는 왜 중요한가?
A. 변수 치환과 Override가 적용된 최종 Compose 설정을 확인할 수 있기 때문이다.

Q. Container 내부 수정으로 문제를 해결해도 되는가?
A. 권장하지 않는다. 수정 내용이 재배포 시 사라지므로 Dockerfile, Compose, Env에 반영해야 한다.

---

# 15. Container Exit Troubleshooting

## 15.1 Container Exited

### [개념]

Container Exit는 Container의 Main Process가 종료되어 Container가 멈춘 상태이다.

Container는 VM이 아니라 Process 실행 단위이므로 Main Process가 끝나면 Container도 종료된다.

```text
Container Start
→ Main Process Run
→ Main Process Exit
→ Container Exited
```

---

### [핵심]

Container Exit 주요 원인:

- ENTRYPOINT 오류
- CMD 오류
- Application Startup 실패
- Environment Variable 누락
- DB Connection 실패
- Port Binding 실패
- Permission Denied
- File Not Found
- OOMKilled
- Main Process가 즉시 종료됨

확인 명령:

```bash
docker ps -a
docker logs container_name
docker inspect container_name
```

---

### [실무]

Spring Boot Container 종료 확인:

```bash
docker compose ps
docker compose logs app
```

대표 로그:

```text
Unable to access jarfile app.jar
```

원인:

```text
COPY 경로 오류
Jar 파일 없음
WORKDIR 오류
```

대표 로그:

```text
Communications link failure
```

원인:

```text
DB Host 오류
DB Ready 이전 App 시작
Network 오류
```

---

### [주의]

Restart Policy가 있으면 Container Exit가 반복 재시작으로 가려질 수 있다.

확인:

```bash
docker compose ps
docker inspect app
docker compose logs -f app
```

주의할 점:

- Restart Loop 여부 확인
- Main Process 로그 확인
- Exit Code 확인
- OOMKilled 여부 확인
- ENTRYPOINT / CMD 확인
- Env 누락 확인
- DB 연결 실패 확인

---

### [FAQ]

Q. Container가 바로 종료되는 이유는?
A. Container의 Main Process가 종료되었기 때문이다. 로그와 Exit Code를 확인해야 한다.

Q. Spring Boot Container가 종료될 때 가장 먼저 볼 것은?
A. `docker compose logs app`으로 Startup Error를 확인한다.

Q. Restart Loop란?
A. Container가 실패로 종료되고 Restart Policy에 의해 계속 재시작되는 상태이다.

---

# 16. Port Conflict Troubleshooting

## 16.1 Port Conflict

### [개념]

Port Conflict는 Host Port를 이미 다른 Process 또는 Container가 사용 중일 때 발생하는 문제이다.

Docker Port Mapping은 Host Port와 Container Port를 연결한다.

```text
Host Port 8080
→ Already Used
→ Docker Bind Failed
```

---

### [핵심]

대표 오류:

```text
Bind for 0.0.0.0:8080 failed: port is already allocated
```

원인:

- Host에서 같은 Port 사용 중
- 다른 Container가 Port 사용 중
- 이전 Container가 종료되지 않음
- Compose Project 중복 실행
- 잘못된 Port Mapping

확인 명령:

```bash
docker ps
docker compose ps
lsof -i :8080
ss -tulpn | grep 8080
```

---

### [실무]

해결 방법 1: 기존 Container 중지

```bash
docker ps
docker stop old-container
```

해결 방법 2: Host Port 변경

```yaml
services:
  app:
    ports:
      - "8081:8080"
```

해결 방법 3: DB Port 충돌 회피

```yaml
services:
  mysql:
    ports:
      - "3307:3306"
```

---

### [주의]

Port Mapping 방향을 혼동하면 안 된다.

```yaml
ports:
  - "8081:8080"
```

의미:

```text
Host localhost:8081
→ Container app:8080
```

주의할 점:

- 왼쪽은 Host Port
- 오른쪽은 Container Port
- 내부 통신은 Host Port가 아니라 Container Port 사용
- 운영 DB Port 외부 공개 지양
- 방화벽 / Security Group 확인

---

### [FAQ]

Q. port is already allocated 오류는 왜 발생하는가?
A. Host Port를 다른 Process나 Container가 이미 사용 중이기 때문이다.

Q. ports에서 왼쪽과 오른쪽은 무엇인가?
A. 왼쪽은 Host Port이고 오른쪽은 Container Port이다.

Q. Port 충돌을 해결하려면?
A. 기존 Process를 중지하거나 Host Port를 다른 번호로 변경한다.

---

# 17. Network Troubleshooting

## 17.1 Container Network Error

### [개념]

Network Troubleshooting은 Container 간 통신 실패, Hostname 오류, DNS 오류, Port 오해를 분석하는 과정이다.

Compose 내부 통신은 Service Name과 Container Port를 사용한다.

```text
app container
→ mysql service name
→ mysql container port 3306
```

---

### [핵심]

Network 오류 원인:

- `localhost` 오해
- Service Name 오타
- 서로 다른 Network에 연결
- Host Port와 Container Port 혼동
- DB Ready 이전 연결
- Firewall / Security Group 차단
- Reverse Proxy Target 오류

확인 명령:

```bash
docker network ls
docker network inspect network_name
docker compose exec app env
docker compose exec app ping mysql
```

---

### [실무]

잘못된 DB URL:

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/festapick
```

Compose 내부 권장 DB URL:

```properties
spring.datasource.url=jdbc:mysql://mysql:3306/festapick
```

Nginx Proxy Target:

```nginx
location / {
    proxy_pass http://app:8080;
}
```

Network 확인:

```bash
docker compose exec app sh
getent hosts mysql
```

---

### [주의]

`localhost`는 Container 내부에서 자기 자신을 의미한다.

주의할 점:

- App에서 DB 접속 시 Service Name 사용
- Redis Host도 `redis` 사용
- Nginx Upstream도 Service Name 사용
- 내부 통신은 Container Port 사용
- Host에서 접속할 때만 Host Port 사용
- Network 분리 시 필요한 Service끼리 같은 Network 연결

---

### [FAQ]

Q. Compose 내부에서 localhost로 DB에 연결하면 안 되는 이유는?
A. Container 내부의 localhost는 DB Container가 아니라 자기 자신을 의미하기 때문이다.

Q. Compose 내부에서 DB Host는 무엇을 사용해야 하는가?
A. DB Service 이름을 사용해야 한다. 예를 들어 Service 이름이 `mysql`이면 Host는 `mysql`이다.

Q. Network 문제는 어떻게 확인하는가?
A. `docker network inspect`, `docker compose exec`, `getent hosts`, Application Env를 확인한다.

---

# 18. Volume and Permission Troubleshooting

## 18.1 Volume Issue

### [개념]

Volume Issue는 Container 데이터가 유지되지 않거나 Host-Container Mount 경로, 권한, 소유자 문제로 발생하는 오류이다.

Volume은 Container 삭제와 무관하게 데이터를 유지하기 위해 사용한다.

```text
Container Path
↔ Volume / Bind Mount
↔ Persistent Data
```

---

### [핵심]

대표 문제:

- 데이터가 사라짐
- Permission Denied
- 파일 생성 실패
- Upload 저장 실패
- DB 초기화 반복
- Bind Mount 경로 오류
- Non-root User 권한 부족
- `down -v`로 Volume 삭제

확인 명령:

```bash
docker volume ls
docker volume inspect volume_name
docker inspect container_name
ls -al host_path
```

---

### [실무]

Permission Denied 예시:

```text
java.nio.file.AccessDeniedException: /app/uploads
```

해결:

```bash
sudo chown -R 1001:1001 /srv/festapick/uploads
```

Compose 예시:

```yaml
services:
  app:
    image: festapick-api:1.0.0
    volumes:
      - /srv/festapick/uploads:/app/uploads
```

Non-root User가 `/app/uploads`에 쓸 수 있어야 한다.

MySQL Volume 확인:

```bash
docker volume inspect project_mysql_data
```

---

### [주의]

Volume 삭제 명령은 운영에서 치명적이다.

위험 명령:

```bash
docker compose down -v
docker volume rm volume_name
docker system prune --volumes
```

주의할 점:

- Volume 삭제 전 Backup 확인
- Bind Mount Host 경로 존재 여부 확인
- Non-root UID / GID 확인
- DB Data Directory Mount 경로 확인
- Upload Directory 권한 확인
- SELinux / AppArmor 환경 고려
- Windows / Linux Path 차이 주의

---

### [FAQ]

Q. Volume 데이터가 사라지는 이유는?
A. `docker compose down -v`, `docker volume rm`, `docker system prune --volumes`로 Volume을 삭제했을 수 있다.

Q. Permission Denied는 왜 발생하는가?
A. Container 실행 User가 Volume 또는 Bind Mount 경로에 접근 권한이 없기 때문이다.

Q. Upload File은 어디에 저장해야 하는가?
A. Container 내부 임시 경로가 아니라 Volume 또는 외부 Storage에 저장해야 한다.

---

# 19. Environment Troubleshooting

## 19.1 Environment Variable Issue

### [개념]

Environment Troubleshooting은 Container Runtime에 필요한 환경변수가 누락되거나 잘못 주입되어 발생하는 문제를 분석하는 과정이다.

Spring Boot Docker 배포에서는 환경변수로 Profile, DB URL, Secret, External API Config를 주입한다.

```text
Compose Env
→ Container Env
→ Spring Boot Config
```

---

### [핵심]

대표 문제:

- `SPRING_PROFILES_ACTIVE` 누락
- DB URL 오타
- DB Password 누락
- Redis Host 누락
- JWT Secret 누락
- `.env` 경로 오류
- Compose 변수 치환 실패
- env_file과 `.env` 역할 혼동

확인 명령:

```bash
docker compose config
docker compose exec app env
docker inspect app
```

---

### [실무]

Compose 변수 치환 확인:

```bash
docker compose config
```

Container 내부 환경변수 확인:

```bash
docker compose exec app env | grep SPRING
```

Spring Boot 오류 예시:

```text
Failed to configure a DataSource
```

원인:

```text
SPRING_DATASOURCE_URL 누락
DB Driver 설정 오류
Profile 설정 오류
```

환경변수 주입 예시:

```yaml
services:
  app:
    environment:
      SPRING_DATASOURCE_URL: jdbc:mysql://mysql:3306/festapick
      SPRING_DATASOURCE_USERNAME: ${DB_USER}
      SPRING_DATASOURCE_PASSWORD: ${DB_PASSWORD}
```

---

### [주의]

Compose에서 `${VAR}`가 비어 있으면 빈 값으로 주입될 수 있다.

주의할 점:

- `.env` 파일 위치 확인
- `--env-file` 사용 여부 확인
- 변수명 대소문자 확인
- Secret 로그 출력 금지
- 운영 Secret 파일 권한 제한
- `.env.example`과 실제 `.env` 비교
- `docker compose config`로 최종 값 확인

---

### [FAQ]

Q. Docker 환경변수 문제는 어떻게 확인하는가?
A. `docker compose config`로 Compose 치환 결과를 보고 `docker compose exec app env`로 Container 내부 값을 확인한다.

Q. Spring Boot에서 DB 설정이 적용되지 않는 이유는?
A. 환경변수 이름 오타, Profile 오류, `.env` 경로 오류, Compose 변수 치환 실패가 원인일 수 있다.

Q. `.env`와 env_file 차이를 모르면 어떤 문제가 생기는가?
A. Compose 변수 치환과 Container 환경변수 주입을 혼동하여 필요한 값이 Container에 전달되지 않을 수 있다.

---

# 20. Build Troubleshooting

## 20.1 Build Failed

### [개념]

Build Troubleshooting은 Docker Image Build 과정에서 발생하는 Dockerfile, Build Context, Dependency, Cache, Permission 문제를 분석하는 과정이다.

```text
docker build
→ Dockerfile
→ Build Context
→ Layer
→ Image
```

---

### [핵심]

대표 Build 실패 원인:

- Dockerfile 경로 오류
- Build Context 오류
- COPY 대상 파일 없음
- `.dockerignore`로 파일 제외
- Jar Build 누락
- Dependency Download 실패
- Base Image Pull 실패
- Permission Denied
- Syntax Error
- Cache 오염

확인 명령:

```bash
docker build -t app:1.0 .
docker build --no-cache -t app:1.0 .
docker compose build --no-cache
```

---

### [실무]

COPY Failed 예시:

```text
COPY failed: no source files were specified
```

원인:

```text
build/libs/*.jar 파일 없음
.dockerignore에서 build 제외
Build Context 오류
```

해결:

```bash
./gradlew clean bootJar
ls build/libs
docker build -t app:1.0 .
```

Multi-stage Build에서는 Jar를 Container 내부에서 생성한다.

```dockerfile
FROM gradle:8.10-jdk21 AS builder
WORKDIR /app
COPY . .
RUN gradle clean bootJar --no-daemon
```

---

### [주의]

`--no-cache`는 원인 분석에 유용하지만 항상 사용하면 Build가 느려진다.

주의할 점:

- Build Context와 Dockerfile 경로 구분
- `.dockerignore` 확인
- COPY 경로 확인
- Base Image Tag 확인
- Network / Proxy 문제 확인
- Secret을 Build ARG로 넘기지 않기
- Build Log를 먼저 확인

---

### [FAQ]

Q. Docker Build 실패 시 무엇을 먼저 확인해야 하는가?
A. Build Log, Dockerfile 경로, Build Context, COPY 대상 파일, `.dockerignore`를 확인해야 한다.

Q. COPY failed 오류는 왜 발생하는가?
A. 복사 대상 파일이 Build Context에 없거나 `.dockerignore`에 의해 제외되었기 때문이다.

Q. --no-cache는 언제 사용하는가?
A. Cache로 인해 원인 파악이 어려울 때 일시적으로 사용한다.

---

# 21. Image Size Troubleshooting

## 21.1 Large Image

### [개념]

Large Image 문제는 Docker Image에 불필요한 파일, Build Tool, Cache, Source Code가 포함되어 Image Size가 커지는 문제이다.

Image Size가 크면 Pull, Push, Deploy, Scan 시간이 증가한다.

```text
Large Image
→ Slow Build
→ Slow Push
→ Slow Pull
→ Slow Deploy
→ Larger Attack Surface
```

---

### [핵심]

Large Image 원인:

- 큰 Base Image 사용
- Multi-stage Build 미사용
- Build Tool이 Runtime Image에 남음
- Source Code 전체 포함
- `.dockerignore` 없음
- Package Cache 미삭제
- Log / Upload File 포함
- node_modules 포함
- `.git` 포함

확인 명령:

```bash
docker images
docker history image_name
```

---

### [실무]

비권장:

```dockerfile
FROM gradle:8.10-jdk21
WORKDIR /app
COPY . .
RUN gradle bootJar
ENTRYPOINT ["java", "-jar", "build/libs/app.jar"]
```

문제:

```text
Runtime Image에 Gradle, JDK, Source Code 포함
```

권장:

```dockerfile
FROM gradle:8.10-jdk21 AS builder
WORKDIR /app
COPY . .
RUN gradle clean bootJar --no-daemon

FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=builder /app/build/libs/*.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

`.dockerignore`:

```text
.git
.gradle
.idea
.vscode
*.log
.env
node_modules
```

---

### [주의]

Image Size를 줄이기 위해 무조건 Alpine을 선택하면 호환성 문제가 생길 수 있다.

주의할 점:

- Java Native Library 호환 확인
- Debug 가능성 고려
- Base Image 신뢰성 확인
- Security Patch 업데이트 확인
- Build Tool 제거
- Runtime에 필요한 파일만 포함
- `.dockerignore` 필수

---

### [FAQ]

Q. Docker Image가 큰 이유는?
A. 큰 Base Image, Build Tool, Source Code, Cache, node_modules, `.git`, Log File이 포함되었기 때문이다.

Q. Image Size를 줄이는 가장 대표적인 방법은?
A. Multi-stage Build와 `.dockerignore`를 사용하는 것이다.

Q. Image Size가 크면 어떤 문제가 생기는가?
A. Build, Push, Pull, Deploy 시간이 늘고 보안 공격면이 커질 수 있다.

---

# 22. OOM and Resource Troubleshooting

## 22.1 OOMKilled

### [개념]

OOMKilled는 Container가 Memory Limit을 초과하여 종료된 상태이다.

Docker Container는 제한된 Memory를 초과하면 Kernel 또는 Docker Runtime에 의해 종료될 수 있다.

```text
Container Memory Usage
→ Limit Exceeded
→ OOMKilled
→ Container Exit
```

---

### [핵심]

OOM 원인:

- Memory Limit 너무 낮음
- JVM Heap 너무 큼
- Memory Leak
- 큰 File 처리
- 많은 Thread
- DB / Cache Memory 증가
- Traffic 증가
- Native Memory 증가

확인 명령:

```bash
docker inspect container_name
docker stats
docker compose logs app
```

Inspect 확인 항목:

```text
State.OOMKilled = true
ExitCode = 137
```

---

### [실무]

Compose Resource 설정:

```yaml
services:
  app:
    image: festapick-api:1.0.0
    mem_limit: 1g
    environment:
      JAVA_OPTS: "-Xms256m -Xmx768m"
```

Spring Boot OOM 대응:

```text
- Xmx를 Container Memory보다 작게 설정
- Heap Dump 설정
- Traffic / Batch Job 확인
- Large File 처리 방식 확인
- Thread Pool 크기 확인
- Memory Metrics 확인
```

docker stats:

```bash
docker stats
```

---

### [주의]

Container Memory Limit과 JVM Xmx를 동일하게 설정하면 위험하다.

비권장:

```text
mem_limit: 1g
-Xmx1g
```

권장:

```text
mem_limit: 1g
-Xmx768m
```

주의할 점:

- Heap 외 Memory 고려
- Native Memory 고려
- Thread Stack 고려
- Direct Buffer 고려
- OOMKilled 여부 확인
- 단순 Restart로 해결하지 않기

---

### [FAQ]

Q. OOMKilled란?
A. Container가 Memory Limit을 초과하여 강제로 종료된 상태이다.

Q. OOMKilled는 어떻게 확인하는가?
A. `docker inspect`에서 `State.OOMKilled=true` 또는 Exit Code 137을 확인한다.

Q. Spring Boot Container에서 OOM을 줄이려면?
A. Container Memory Limit보다 작은 Xmx를 설정하고 Heap 외 Memory 여유를 남겨야 한다.

---

# 23. Health Check Troubleshooting

## 23.1 Unhealthy Container

### [개념]

Unhealthy Container는 Container Process는 실행 중이지만 Health Check 명령이 실패한 상태이다.

```text
Container Running
+ Health Check Failed
→ Unhealthy
```

Unhealthy는 Application이 정상 응답하지 못하거나 Health Check 설정이 잘못되었을 때 발생한다.

---

### [핵심]

Unhealthy 원인:

- Health URL 오류
- Application Startup 지연
- curl / wget 없음
- Actuator Dependency 없음
- Health Endpoint 보안 차단
- Context Path 누락
- Port 오류
- DB 연결 실패
- Timeout 너무 짧음

확인 명령:

```bash
docker compose ps
docker inspect container_name
docker compose logs app
```

---

### [실무]

Spring Boot Actuator 확인:

```bash
curl http://localhost:8080/actuator/health
```

Container 내부 확인:

```bash
docker compose exec app sh
wget -qO- http://localhost:8080/actuator/health
```

Compose Health Check 예시:

```yaml
healthcheck:
  test: ["CMD", "wget", "-qO-", "http://localhost:8080/actuator/health"]
  interval: 30s
  timeout: 3s
  retries: 3
  start_period: 30s
```

Startup이 느린 경우:

```yaml
start_period: 60s
```

---

### [주의]

Health Check 실패가 항상 Application 장애를 의미하지는 않는다.

설정 오류 가능성:

- Health Check Tool 없음
- URL 오타
- Port 오타
- Context Path 누락
- Security 인증 필요
- Timeout 너무 짧음

주의할 점:

- Health Check 명령을 Container 내부 기준으로 확인
- `localhost`는 Container 자기 자신
- Actuator 설정 확인
- Health Endpoint 노출 범위 확인
- Startup 시간 반영
- Logs와 Health 결과 함께 확인

---

### [FAQ]

Q. Container가 unhealthy인 이유는?
A. Application Health Check가 실패했거나 Health Check 명령 설정이 잘못되었기 때문이다.

Q. curl not found로 Health Check가 실패하면?
A. Runtime Image에 curl을 설치하거나 wget 등 Image에 존재하는 도구를 사용해야 한다.

Q. Health Check URL은 Host 기준인가 Container 기준인가?
A. Container 내부에서 실행되므로 Container 내부 기준 URL을 사용해야 한다.

---

# 24. Docker Cleanup

## 24.1 Cleanup Commands

### [개념]

Docker Cleanup은 사용하지 않는 Container, Image, Volume, Network, Build Cache를 정리하는 작업이다.

정리는 Disk 사용량을 줄이지만 운영 데이터 삭제 위험이 있다.

```text
Unused Container
+ Unused Image
+ Unused Network
+ Unused Volume
+ Build Cache
→ Cleanup
```

---

### [핵심]

정리 대상:

- Stopped Container
- Dangling Image
- Unused Image
- Unused Network
- Unused Volume
- Build Cache

명령어:

```bash
docker system df
docker container prune
docker image prune
docker network prune
docker volume prune
docker builder prune
docker system prune
```

강력한 정리:

```bash
docker system prune -a
```

Volume 포함 정리:

```bash
docker system prune -a --volumes
```

---

### [실무]

Disk 사용량 확인:

```bash
docker system df
```

중지 Container 삭제:

```bash
docker container prune
```

Dangling Image 삭제:

```bash
docker image prune
```

Build Cache 삭제:

```bash
docker builder prune
```

개발 환경 전체 정리:

```bash
docker system prune -a
```

운영 환경에서는 정리 전 Volume과 Image 사용 여부를 반드시 확인한다.

---

### [주의]

`--volumes` 옵션은 데이터 삭제 위험이 매우 크다.

위험 명령:

```bash
docker system prune -a --volumes
docker volume prune
docker compose down -v
```

주의할 점:

- 운영 DB Volume 삭제 금지
- Upload Volume 삭제 금지
- Rollback용 이전 Image 삭제 주의
- Cleanup 전 `docker system df` 확인
- Volume Backup 확인
- 현재 실행 중 Container에 영향 없는지 확인
- 개발 환경과 운영 환경 Cleanup 정책 구분

---

### [FAQ]

Q. Docker Cleanup은 왜 필요한가?
A. 사용하지 않는 Image, Container, Cache가 Disk를 차지하므로 주기적으로 정리해야 한다.

Q. docker system prune -a는 무엇을 삭제하는가?
A. 사용하지 않는 Container, Network, Image, Build Cache를 삭제한다.

Q. docker system prune -a --volumes는 왜 위험한가?
A. 사용하지 않는 Volume까지 삭제하여 DB나 Upload 데이터가 사라질 수 있기 때문이다.

---

# 25. Final Deployment Checklist

## 25.1 Deployment Checklist

### [개념]

Deployment Checklist는 Docker 배포 전후에 Image, Config, Secret, Volume, Network, Logs, Health, Rollback을 검증하는 기준이다.

Checklist는 배포 실패와 장애 복구 실패를 줄이기 위한 운영 문서이다.

---

### [핵심]

배포 전 Checklist:

```text
[Image]
- Image Build 성공
- Image Tag 명확
- Registry Push 완료
- latest 단독 사용 아님

[Config]
- Compose Config 검증
- Runtime Env 확인
- Secret 하드코딩 없음
- .env 권한 확인

[Network]
- Host Port 충돌 없음
- DB Port 외부 공개 없음
- Service Name 기반 내부 통신

[Volume]
- DB Volume 설정
- Upload Volume 설정
- Backup 확인

[Health]
- Health Check 설정
- Actuator Endpoint 확인
- depends_on condition 확인

[Rollback]
- 이전 Image Tag 존재
- Rollback 절차 확인
- DB Migration 호환성 확인
```

---

### [실무]

배포 명령 순서:

```bash
docker compose config
docker compose pull
docker compose up -d
docker compose ps
docker compose logs --tail=100 app
curl http://localhost:8080/actuator/health
```

문제 발생 시:

```bash
docker compose logs -f app
docker inspect app
docker stats
docker compose config
```

Rollback:

```text
Compose Image Tag 이전 버전으로 변경
→ docker compose pull
→ docker compose up -d
→ Health Check
```

---

### [주의]

배포 완료 기준은 Container Running이 아니라 Application Healthy이다.

배포 완료 판단:

```text
Container Running
+ Health Check Healthy
+ Logs Error 없음
+ 주요 API 정상
→ Deployment Complete
```

주의할 점:

- Running만 보고 배포 완료 판단 금지
- Logs 확인 필수
- Health Check 확인 필수
- 주요 API Smoke Test 권장
- Rollback 가능 상태 유지
- DB Migration 포함 시 추가 검증 필요

---

### [FAQ]

Q. Docker 배포 완료 기준은 무엇인가?
A. Container가 Running이고 Health Check가 정상이며 Logs와 주요 API가 정상이어야 한다.

Q. 배포 전 반드시 확인해야 할 것은?
A. Image Tag, Compose Config, Secret, Volume, Network, Health Check, Rollback 가능성을 확인해야 한다.

Q. 배포 실패 시 가장 먼저 확인할 것은?
A. `docker compose logs`, `docker compose ps`, `docker compose config`, `docker inspect`를 확인한다.

---

# Retrieval Queries

### [FAQ]

Q. Docker Deployment란 무엇인가?
A. Docker Image를 Registry에 저장하고 운영 서버에서 Container로 실행하는 배포 과정이다.

Q. Docker 배포 핵심 원칙은 무엇인가?
A. 동일한 Image를 여러 환경에서 재현 가능하게 실행하는 것이다.

Q. Docker 배포 기본 흐름은 무엇인가?
A. Code를 Build하여 Image를 만들고 Registry에 Push한 뒤 서버에서 Pull하여 Container로 실행한다.

Q. 운영 서버에서 Image를 직접 Build하는 것이 좋은가?
A. 권장하지 않는다. CI에서 Build한 Image를 Registry에 Push하고 운영 서버는 Pull하여 실행하는 것이 좋다.

Q. Image Tag란 무엇인가?
A. Docker Image Version을 식별하는 이름이다.

Q. 운영에서 latest만 사용하면 안 되는 이유는?
A. 배포 Version 추적과 Rollback이 어렵기 때문이다.

Q. Docker Registry Deployment란 무엇인가?
A. Image를 Registry에 Push하고 서버에서 Pull하여 실행하는 배포 방식이다.

Q. Registry를 사용하는 이유는 무엇인가?
A. Image를 중앙 저장소에서 관리하고 여러 서버와 CI/CD Pipeline에서 동일하게 사용하기 위해서이다.

Q. Runtime Environment란 무엇인가?
A. Container 실행 시 주입되는 환경 설정이다.

Q. Docker Image에 운영 설정을 포함해도 되는가?
A. 권장하지 않는다. 운영 설정은 Runtime Environment나 Secret으로 주입해야 한다.

Q. Docker에서 Secret을 어디에 하드코딩하면 안 되는가?
A. Dockerfile, Image, Compose File, Git Repository에 하드코딩하면 안 된다.

Q. Docker Volume Deployment란 무엇인가?
A. Container 삭제 후에도 유지되어야 하는 데이터를 Volume 또는 외부 저장소에 보관하는 배포 방식이다.

Q. Database에 Volume이 필요한 이유는?
A. Container 재생성 후에도 Database 데이터를 유지하기 위해 필요하다.

Q. docker compose down -v는 왜 위험한가?
A. Named Volume까지 삭제하여 Database 또는 Upload 데이터가 사라질 수 있기 때문이다.

Q. Docker 배포에서 내부 통신은 어떻게 하는가?
A. 같은 Docker Network에 있는 Service끼리는 Service Name과 Container Port로 통신한다.

Q. 운영에서 DB Port를 외부 공개해도 되는가?
A. 권장하지 않는다. DB는 Backend Network 내부에서만 접근하도록 제한해야 한다.

Q. Docker Logs란 무엇인가?
A. Container의 stdout과 stderr 출력을 수집하고 조회하는 기능이다.

Q. Container 환경에서 Console Log가 권장되는 이유는?
A. Docker가 stdout과 stderr를 표준 방식으로 수집하고 외부 로그 시스템과 연동하기 쉽기 때문이다.

Q. Docker Monitoring에서 무엇을 확인해야 하는가?
A. Container 상태, Health Status, CPU, Memory, Restart Count, Logs, Application Metrics를 확인해야 한다.

Q. Running 상태이면 Application이 정상인가?
A. 아니다. Running은 Process 실행 상태이고 Application 정상 여부는 Health Check와 API 응답으로 확인해야 한다.

Q. Health Check란 무엇인가?
A. Container 또는 Application이 정상적으로 요청을 처리할 준비가 되었는지 확인하는 메커니즘이다.

Q. Spring Boot Docker Health Check는 무엇을 사용하는가?
A. Spring Boot Actuator의 `/actuator/health` Endpoint를 사용하는 것이 일반적이다.

Q. Resource Limit이란 무엇인가?
A. Container가 사용할 CPU와 Memory를 제한하는 설정이다.

Q. OOMKilled란 무엇인가?
A. Container가 Memory Limit을 초과하여 강제로 종료된 상태이다.

Q. Spring Boot Container에서 Xmx는 어떻게 설정해야 하는가?
A. Container Memory Limit보다 작게 설정하고 Heap 외 Memory 여유를 남겨야 한다.

Q. Docker 성능 최적화 대상은 무엇인가?
A. Build Speed, Image Size, Startup Time, Runtime CPU와 Memory, Logs, Volume I/O가 주요 대상이다.

Q. Image Size를 줄이는 대표 방법은 무엇인가?
A. Multi-stage Build, `.dockerignore`, 작은 Runtime Image, 불필요 Package 제거를 사용한다.

Q. Single Server Compose Deployment란 무엇인가?
A. 하나의 서버에서 Docker Compose로 App, DB, Cache, Reverse Proxy를 함께 실행하는 배포 방식이다.

Q. Blue-Green Deployment란 무엇인가?
A. 기존 버전과 새 버전을 동시에 준비한 뒤 트래픽을 새 버전으로 전환하는 배포 방식이다.

Q. Docker Rollback이란 무엇인가?
A. 문제가 발생한 새 배포를 중단하고 이전 정상 Image Version으로 되돌리는 과정이다.

Q. Docker Rollback을 쉽게 하려면 무엇이 필요한가?
A. 명확한 Image Tag, 이전 Image 보관, Compose Config 이력, Health Check가 필요하다.

Q. Docker 배포에서 무엇을 백업해야 하는가?
A. Database, Upload File, Volume Data, Compose 설정, Nginx 설정, 인증서, Secret 관리 정보를 백업해야 한다.

Q. Container 자체를 백업해야 하는가?
A. 일반적으로 아니다. Container는 Image와 Compose로 재생성하고 Data를 백업하는 것이 핵심이다.

Q. Docker 배포 보안에서 가장 중요한 것은?
A. Secret 하드코딩 금지, Non-root 실행, Port 최소 공개, DB 내부망 제한, Docker Socket Mount 회피이다.

Q. Docker Socket Mount가 위험한 이유는?
A. Container가 Host Docker Daemon을 제어할 수 있어 Root 수준 권한으로 이어질 수 있기 때문이다.

Q. Docker 문제 해결은 무엇부터 확인해야 하는가?
A. Container 상태, Logs, Compose Config, Inspect 정보를 먼저 확인해야 한다.

Q. docker compose config는 왜 중요한가?
A. 변수 치환과 Override가 적용된 최종 Compose 설정을 확인할 수 있기 때문이다.

Q. Container가 바로 종료되는 이유는?
A. Container의 Main Process가 종료되었기 때문이다. Logs와 Exit Code를 확인해야 한다.

Q. Restart Loop란 무엇인가?
A. Container가 실패로 종료되고 Restart Policy에 의해 계속 재시작되는 상태이다.

Q. port is already allocated 오류는 왜 발생하는가?
A. Host Port를 다른 Process나 Container가 이미 사용 중이기 때문이다.

Q. Compose 내부에서 localhost로 DB에 연결하면 안 되는 이유는?
A. Container 내부의 localhost는 DB Container가 아니라 자기 자신을 의미하기 때문이다.

Q. Compose 내부에서 DB Host는 무엇을 사용해야 하는가?
A. DB Service 이름을 사용해야 한다. 예를 들어 Service 이름이 `mysql`이면 Host는 `mysql`이다.

Q. Volume 데이터가 사라지는 이유는?
A. `docker compose down -v`, `docker volume rm`, `docker system prune --volumes`로 Volume을 삭제했을 수 있다.

Q. Permission Denied는 왜 발생하는가?
A. Container 실행 User가 Volume 또는 Bind Mount 경로에 접근 권한이 없기 때문이다.

Q. Docker 환경변수 문제는 어떻게 확인하는가?
A. `docker compose config`와 `docker compose exec app env`로 확인한다.

Q. Docker Build 실패 시 무엇을 먼저 확인해야 하는가?
A. Build Log, Dockerfile 경로, Build Context, COPY 대상 파일, `.dockerignore`를 확인해야 한다.

Q. Docker Image가 큰 이유는?
A. 큰 Base Image, Build Tool, Source Code, Cache, node_modules, `.git`, Log File이 포함되었기 때문이다.

Q. Container가 unhealthy인 이유는?
A. Application Health Check가 실패했거나 Health Check 명령 설정이 잘못되었기 때문이다.

Q. Docker Cleanup은 왜 필요한가?
A. 사용하지 않는 Image, Container, Cache가 Disk를 차지하므로 주기적으로 정리해야 한다.

Q. docker system prune -a --volumes는 왜 위험한가?
A. 사용하지 않는 Volume까지 삭제하여 DB나 Upload 데이터가 사라질 수 있기 때문이다.

Q. Docker 배포 완료 기준은 무엇인가?
A. Container가 Running이고 Health Check가 정상이며 Logs와 주요 API가 정상이어야 한다.

Q. 배포 실패 시 가장 먼저 확인할 것은?
A. `docker compose logs`, `docker compose ps`, `docker compose config`, `docker inspect`를 확인한다.
