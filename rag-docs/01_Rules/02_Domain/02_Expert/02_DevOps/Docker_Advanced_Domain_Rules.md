# Docker Advanced Domain Rules

---

# 1. Domain Purpose

## 1.1 Docker Advanced 문서 목적

### [개념]

Docker Advanced Domain 문서는 DevOps Agent / Backend Agent / Review Agent용 RAG 문서이다.

목적:

- Container Runtime Support
- Dockerfile Optimization Support
- Docker Image Build Support
- Docker Compose Support
- Network / Volume Troubleshooting
- Production Container Deployment Support
- Security Review Support

우선순위:

1. Docker Core Advanced
2. Image / Dockerfile
3. Compose / Runtime
4. Network / Volume
5. Security / Troubleshooting

---

### [핵심]

Docker Advanced 문서는 단순 사용법 문서가 아니다.

Agent가 아래 작업을 수행할 수 있어야 한다.

- Dockerfile 작성
- Multi-stage Build 설계
- Docker Compose 구성
- Container Network 문제 해결
- Volume / Bind Mount 문제 해결
- Image Size 최적화
- Container Security 검토
- CI/CD Pipeline Docker Build 연계
- Kubernetes 전환 전 Container 기준 검증

---

### [실무]

2026 실무 기준 Docker Advanced 문서는 다음 관점으로 작성한다.

- Local Development Containerization
- Build Artifact Containerization
- Docker Compose 기반 개발 환경
- CI/CD Image Build
- Registry Push
- Runtime Environment 분리
- Production-ready Dockerfile
- Security 최소 기준
- Kubernetes 배포 전 사전 단계

Docker Advanced 문서는 CI/CD Domain Rules, Kubernetes Domain Rules와 연계된다.

```text
Source Code
→ Docker Build
→ Docker Image
→ Registry
→ CI/CD Deploy
→ Kubernetes Runtime
```

---

### [FAQ]

Q. Docker Advanced 문서는 누구를 위한 문서인가?

A.
DevOps Agent, Backend Agent, Review Agent가 Docker 기반 빌드, 실행, 배포, 문제 해결을 수행하기 위한 RAG 문서이다.

---

Q. Docker 기초 문서와 Docker Advanced 문서의 차이는?

A.
기초 문서는 Docker 명령어와 기본 개념 중심이다. Advanced 문서는 실무 Dockerfile, Compose, Image 최적화, 보안, 운영 문제 해결 중심이다.

Q. Docker Advanced 문서는 Kubernetes 문서와 겹치는가?

A.
겹치지 않는다. Docker Advanced는 Container Artifact와 Runtime 기초를 다루고, Kubernetes는 Orchestration과 Cluster 운영을 다룬다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Docker Advanced Domain 문서는 Docker를 실무 개발 / 배포 / 운영에 적용하는 범위를 다룬다.

포함 범위:

- Docker Architecture
- Dockerfile
- Multi-stage Build
- Build Context
- Image Layer
- Docker Image Optimization
- Container Lifecycle
- Docker Compose
- Environment Variable
- Secret Handling
- Docker Network
- Docker Volume
- Bind Mount
- Healthcheck
- Logging
- Resource Limit
- Docker Registry
- Docker Hub
- AWS ECR
- GitHub Container Registry
- CI/CD Docker Build
- Production Dockerfile
- Security
- Troubleshooting

---

### [핵심]

반드시 포함할 키워드:

- Docker
- Container
- Image
- Dockerfile
- Layer
- Multi-stage Build
- Compose
- Network
- Volume
- Registry
- Healthcheck
- Security
- Build Cache
- Runtime
- Production

---

### [실무]

Docker Advanced 문서는 아래 상황을 해결할 수 있어야 한다.

- Spring Boot App을 Docker Image로 빌드
- React App을 Nginx Container로 배포
- MySQL / Redis / Backend를 Docker Compose로 구성
- `.env` 기반 실행 환경 분리
- Docker Image Size 최적화
- Build Cache 문제 해결
- Container Port 충돌 해결
- Volume Permission 문제 해결
- Container 간 통신 문제 해결
- CI/CD에서 Image Build 후 Registry Push
- Kubernetes 배포 전 Image 검증

---

### [FAQ]

Q. Docker Advanced 문서에서 Docker Swarm을 다뤄야 하는가?

A.
우선순위는 낮다. 2026 기준 실무 확장 흐름은 Docker Compose → CI/CD → Kubernetes 중심이다.

Q. Docker Advanced 문서에 Kubernetes 내용을 포함해야 하는가?

A.
직접 포함하지 않는다. Kubernetes로 넘어가기 전 Docker Image, Runtime, Registry 기준만 연결한다.

---

# 3. Section Priority

## 3.1 문서 섹션 규칙

### [개념]

Docker Advanced 문서는 MASTER_RAG_RULES의 Required Section 구조를 따른다.

Required:

- [개념]
- [핵심]
- [실무]
- [FAQ]

Strongly Recommended:

- [Flow]
- [예제]
- [주의]
- [Best Practice]

Optional:

- [Checklist]
- [Troubleshooting]
- [Comparison]

---

### [핵심]

Docker Advanced 문서는 실무 검색을 위해 아래 구조를 우선 사용한다.

```text
Concept
→ Rule
→ Flow
→ Example
→ Mistake
→ Troubleshooting
→ FAQ
```

---

### [실무]

각 Part 문서는 독립 검색 가능해야 한다.

권장 Part 구성:

- Docker_Advanced_Part01_Architecture.md
- Docker_Advanced_Part02_Dockerfile.md
- Docker_Advanced_Part03_Multi_Stage_Build.md
- Docker_Advanced_Part04_Image_Optimization.md
- Docker_Advanced_Part05_Docker_Compose.md
- Docker_Advanced_Part06_Network_Volume.md
- Docker_Advanced_Part07_Registry_CI_CD.md
- Docker_Advanced_Part08_Security_Troubleshooting.md

---

### [FAQ]

Q. 모든 Docker 문서에 FAQ가 필요한가?

A.
필수이다. FAQ는 Agent Retrieval Query Matching 성능을 높이는 핵심 섹션이다.

Q. Docker 문서에 긴 설명을 넣어도 되는가?

A.
권장하지 않는다. 짧은 설명, 명확한 Flow, 짧은 예제, 문제 해결 패턴을 우선한다.

---

# 4. Docker Architecture Rules

## 4.1 Docker Architecture 작성 규칙

### [개념]

Docker Architecture 문서는 Docker 동작 구조를 Agent가 이해하도록 작성한다.

필수 포함:

- Docker Client
- Docker Daemon
- Docker Image
- Docker Container
- Docker Registry
- Docker Network
- Docker Volume

---

### [핵심]

Docker Architecture 기본 구조:

```text
Docker Client
→ Docker Daemon
→ Image Pull / Build
→ Container Create
→ Container Run
```

핵심 설명:

- Docker Client는 명령을 전달한다.
- Docker Daemon은 Image와 Container를 관리한다.
- Image는 실행 가능한 Template이다.
- Container는 Image의 실행 Instance이다.
- Registry는 Image 저장소이다.

---

### [실무]

Architecture 문서는 문제 해결과 연결한다.

예:

- `docker ps` 결과 없음 → Container 실행 상태 확인
- `docker images` 결과 없음 → Image Build / Pull 확인
- Registry Push 실패 → Login / Tag / Permission 확인
- Container 실행 실패 → Entrypoint / Command / Environment 확인

---

### [FAQ]

Q. Docker Image와 Container 차이는?

A.
Image는 실행 템플릿이고 Container는 Image를 실행한 프로세스 단위 인스턴스이다.

Q. Docker Daemon은 어떤 역할을 하는가?

A.
Image Build, Container 실행, Network, Volume, Registry 통신을 관리한다.

---

# 5. Dockerfile Rules

## 5.1 Dockerfile 작성 규칙

### [개념]

Dockerfile은 Docker Image를 생성하기 위한 선언형 Build Script이다.

필수 포함:

- FROM
- WORKDIR
- COPY
- RUN
- EXPOSE
- ENV
- ARG
- CMD
- ENTRYPOINT

---

### [핵심]

Dockerfile 작성 우선순위:

1. Base Image 최소화
2. Layer Cache 고려
3. 불필요 파일 제외
4. Build 단계와 Runtime 단계 분리
5. Secret Hardcoding 금지
6. Non-root User 적용 권장
7. Healthcheck 고려

---

### [실무]

Spring Boot Dockerfile 예시:

```dockerfile
FROM eclipse-temurin:21-jre

WORKDIR /app

COPY build/libs/app.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
```

React + Nginx Runtime 예시:

```dockerfile
FROM nginx:alpine

COPY build/ /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

---

### [주의]

Secret Hardcoding 금지.

나쁨:

```dockerfile
ENV DB_PASSWORD=my-password
```

좋음:

```dockerfile
ENV DB_PASSWORD=${DB_PASSWORD}
```

---

### [FAQ]

Q. Dockerfile에서 CMD와 ENTRYPOINT 차이는?

A.
ENTRYPOINT는 Container 실행의 고정 명령이고, CMD는 기본 인자 또는 기본 실행 명령이다.

Q. Dockerfile에 비밀번호를 ENV로 직접 넣어도 되는가?

A.
금지한다. Secret은 Runtime Environment, Secret Manager, CI/CD Secret으로 주입해야 한다.

---

# 6. Multi-stage Build Rules

## 6.1 Multi-stage Build 작성 규칙

### [개념]

Multi-stage Build는 Build 단계와 Runtime 단계를 분리하여 최종 Image를 작게 만드는 Docker Build 방식이다.

---

### [핵심]

필수 포함:

- Builder Stage
- Runtime Stage
- Artifact Copy
- Image Size Reduction
- Build Dependency 제거

---

### [Flow]

```text
Source Code
→ Builder Image
→ Build Artifact
→ Runtime Image
→ Final Image
```

---

### [실무]

Spring Boot Multi-stage Build 예시:

```dockerfile
FROM gradle:8-jdk21 AS builder

WORKDIR /app

COPY . .

RUN gradle clean build -x test

FROM eclipse-temurin:21-jre

WORKDIR /app

COPY --from=builder /app/build/libs/*.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
```

---

### [Best Practice]

- Build Tool은 Builder Stage에만 둔다.
- Runtime Image에는 실행에 필요한 파일만 복사한다.
- `.dockerignore`로 불필요한 Build Context를 줄인다.
- Build Cache를 고려하여 Dependency 파일을 먼저 복사할 수 있다.

---

### [FAQ]

Q. Multi-stage Build를 사용하는 이유는?

A.
Build 도구와 소스 파일을 최종 Image에서 제거하여 Image Size와 보안 위험을 줄이기 위해 사용한다.

Q. Builder Stage와 Runtime Stage는 무엇이 다른가?

A.
Builder Stage는 Artifact를 생성하고, Runtime Stage는 생성된 Artifact만 실행한다.

---

# 7. Build Context Rules

## 7.1 Build Context 작성 규칙

### [개념]

Build Context는 `docker build` 실행 시 Docker Daemon에 전달되는 파일 범위이다.

---

### [핵심]

필수 포함:

- Build Context
- Dockerfile 위치
- COPY 대상
- `.dockerignore`
- Build Cache

---

### [실무]

Build 명령 예시:

```bash
docker build -t my-app:latest .
```

`.`은 현재 디렉터리를 Build Context로 전달한다.

`.dockerignore` 예시:

```text
.git
node_modules
build
target
.env
*.log
```

---

### [주의]

Build Context가 크면 Build가 느려진다.

주의 대상:

- node_modules
- build output
- target
- .git
- local cache
- secret file
- .env

---

### [FAQ]

Q. Docker Build가 느린 이유는?

A.
Build Context가 크거나 Cache가 깨졌거나 Dependency 설치 Layer가 매번 재실행되기 때문이다.

Q. `.dockerignore`는 왜 필요한가?

A.
불필요한 파일을 Build Context에서 제외하여 Build 속도, 보안, Image 관리 품질을 높인다.

---

# 8. Image Layer Rules

## 8.1 Docker Image Layer 작성 규칙

### [개념]

Docker Image는 여러 Layer가 쌓여 구성된다.

각 Dockerfile 명령은 Layer를 생성할 수 있다.

---

### [핵심]

필수 포함:

- Layer
- Cache
- Immutable Image
- Layer Reuse
- Image Size

---

### [Flow]

```text
FROM
→ COPY
→ RUN
→ Layer
→ Image
```

---

### [실무]

Layer Cache 최적화 예시:

```dockerfile
COPY package.json package-lock.json ./

RUN npm ci

COPY . .

RUN npm run build
```

Dependency 파일을 먼저 복사하면 소스 코드 변경 시에도 Dependency 설치 Cache를 재사용할 수 있다.

---

### [주의]

나쁨:

```dockerfile
COPY . .

RUN npm install
```

소스 파일 변경 시 Dependency 설치 Layer Cache가 자주 깨질 수 있다.

---

### [FAQ]

Q. Docker Image Layer는 왜 중요한가?

A.
Layer는 Build Cache와 Image Size에 직접 영향을 준다. Layer 설계가 좋으면 Build가 빨라지고 Image 관리가 쉬워진다.

Q. Docker Build Cache가 자주 깨지는 이유는?

A.
COPY 순서가 비효율적이거나 자주 변경되는 파일이 Dependency 설치 Layer보다 먼저 복사되기 때문이다.

---

# 9. Image Optimization Rules

## 9.1 Docker Image 최적화 규칙

### [개념]

Docker Image Optimization은 Image Size, Build Speed, Security Surface를 줄이는 작업이다.

---

### [핵심]

최적화 기준:

- Small Base Image
- Multi-stage Build
- `.dockerignore`
- 불필요 Package 제거
- Build Dependency 제거
- Layer Cache 최적화
- Runtime 파일 최소화

---

### [실무]

Image 확인 명령:

```bash
docker images
```

Image History 확인:

```bash
docker history my-app:latest
```

불필요 Image 정리:

```bash
docker image prune
```

---

### [Best Practice]

- Production Runtime에는 소스 코드 전체를 넣지 않는다.
- Build Tool은 Runtime Image에 포함하지 않는다.
- Alpine 사용은 호환성 확인 후 적용한다.
- Distroless Image는 운영 난이도와 디버깅 제약을 고려한다.

---

### [FAQ]

Q. Docker Image Size를 줄이는 가장 일반적인 방법은?

A.
Multi-stage Build를 사용하고 Runtime Image에 실행 Artifact만 포함하는 것이다.

Q. Alpine Image는 항상 좋은 선택인가?

A.
아니다. 작지만 라이브러리 호환성 문제가 있을 수 있으므로 Java, Node, Native Dependency 환경에서는 테스트가 필요하다.

---

# 10. Container Lifecycle Rules

## 10.1 Container Lifecycle 작성 규칙

### [개념]

Container Lifecycle은 Container 생성, 실행, 중지, 삭제 흐름이다.

---

### [핵심]

필수 포함:

- create
- start
- run
- stop
- restart
- remove
- logs
- exec

---

### [Flow]

```text
Image
→ Container Create
→ Container Start
→ Running
→ Stop
→ Remove
```

---

### [실무]

주요 명령:

```bash
docker run -d --name my-app -p 8080:8080 my-app:latest
```

```bash
docker ps
```

```bash
docker logs my-app
```

```bash
docker exec -it my-app sh
```

```bash
docker stop my-app
```

```bash
docker rm my-app
```

---

### [FAQ]

Q. `docker run`과 `docker start` 차이는?

A.
`docker run`은 새 Container를 생성하고 실행한다. `docker start`는 이미 생성된 Container를 다시 실행한다.

Q. Container 로그는 어떻게 확인하는가?

A.
`docker logs containerName` 명령으로 확인한다.

---

# 11. Docker Compose Rules

## 11.1 Docker Compose 작성 규칙

### [개념]

Docker Compose는 여러 Container를 하나의 YAML 파일로 정의하고 실행하는 도구이다.

---

### [핵심]

필수 포함:

- services
- image
- build
- ports
- environment
- env_file
- volumes
- networks
- depends_on
- healthcheck

---

### [Flow]

```text
compose.yml
→ services
→ network create
→ volume create
→ container run
```

---

### [실무]

Spring Boot + MySQL Compose 예시:

```yaml
services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      SPRING_DATASOURCE_URL: jdbc:mysql://db:3306/appdb
      SPRING_DATASOURCE_USERNAME: app
      SPRING_DATASOURCE_PASSWORD: password
    depends_on:
      db:
        condition: service_healthy

  db:
    image: mysql:8
    environment:
      MYSQL_DATABASE: appdb
      MYSQL_USER: app
      MYSQL_PASSWORD: password
      MYSQL_ROOT_PASSWORD: root-password
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  db_data:
```

---

### [주의]

Compose의 `depends_on`은 Container 시작 순서를 제어한다.

Application Ready 상태까지 보장하려면 `healthcheck`와 함께 사용한다.

---

### [FAQ]

Q. Docker Compose는 운영 배포에 사용해도 되는가?

A.
소규모 단일 서버 운영에는 가능하다. 대규모 운영, 자동 복구, 확장, 무중단 배포는 Kubernetes 또는 별도 Orchestration이 적합하다.

Q. Compose에서 서비스끼리 통신할 때 localhost를 사용하면 되는가?

A.
아니다. Compose Network 내부에서는 Service Name을 Hostname처럼 사용한다.

---

# 12. Environment Variable Rules

## 12.1 Environment Variable 작성 규칙

### [개념]

Environment Variable은 Container Runtime 설정을 외부에서 주입하는 방식이다.

---

### [핵심]

필수 포함:

- ENV
- ARG
- environment
- env_file
- Runtime Config
- Secret 분리

---

### [실무]

Compose 환경 변수 예시:

```yaml
services:
  app:
    image: my-app:latest
    env_file:
      - .env
```

`.env` 예시:

```text
DB_HOST=db
DB_PORT=3306
DB_NAME=appdb
```

---

### [주의]

`.env`에 Secret이 포함될 수 있다.

반드시 확인:

- Git Commit 제외
- CI/CD Secret 사용
- 운영 서버 권한 제한
- Log 출력 금지

---

### [FAQ]

Q. Dockerfile의 ARG와 ENV 차이는?

A.
ARG는 Build Time 변수이고 ENV는 Image 또는 Container Runtime 환경 변수이다.

Q. `.env` 파일을 Git에 올려도 되는가?

A.
금지한다. `.env`는 Secret 또는 환경별 설정을 포함할 수 있으므로 `.gitignore`에 추가해야 한다.

---

# 13. Docker Network Rules

## 13.1 Docker Network 작성 규칙

### [개념]

Docker Network는 Container 간 통신과 Host 연결을 관리하는 가상 네트워크이다.

---

### [핵심]

필수 포함:

- bridge network
- host network
- none network
- custom network
- service discovery
- container DNS
- port mapping

---

### [Flow]

```text
Container A
→ Docker Network
→ Container B
```

---

### [실무]

Network 생성:

```bash
docker network create app-network
```

Network 지정 실행:

```bash
docker run -d --name app --network app-network my-app:latest
```

Compose 내부 통신:

```text
Backend Container
→ db:3306
→ MySQL Container
```

Host 접근:

```text
Host Browser
→ localhost:8080
→ Container 8080
```

---

### [주의]

Container 내부의 `localhost`는 Host가 아니라 Container 자기 자신이다.

Host에서 Container 접근:

```text
localhost:hostPort
```

Container에서 다른 Container 접근:

```text
serviceName:containerPort
```

---

### [FAQ]

Q. Container에서 DB 연결이 안 되는 이유는?

A.
localhost를 사용했거나 Network가 다르거나 Service Name / Port 설정이 잘못되었을 가능성이 높다.

Q. Docker Compose에서 DB Host는 무엇으로 설정해야 하는가?

A.
Compose Service Name을 사용한다. 예: `jdbc:mysql://db:3306/appdb`

---

# 14. Docker Volume Rules

## 14.1 Docker Volume 작성 규칙

### [개념]

Docker Volume은 Container 삭제 후에도 데이터를 유지하기 위한 Docker 관리 저장소이다.

---

### [핵심]

필수 포함:

- named volume
- bind mount
- anonymous volume
- persistence
- backup
- permission

---

### [Flow]

```text
Container
→ Volume Mount
→ Persistent Data
```

---

### [실무]

Named Volume 예시:

```yaml
services:
  db:
    image: mysql:8
    volumes:
      - db_data:/var/lib/mysql

volumes:
  db_data:
```

Bind Mount 예시:

```yaml
services:
  app:
    image: my-app:latest
    volumes:
      - ./logs:/app/logs
```

---

### [주의]

Volume 삭제 주의:

```bash
docker volume rm volume_name
```

전체 Volume 정리 주의:

```bash
docker volume prune
```

DB Volume 삭제 시 데이터가 손실될 수 있다.

---

### [FAQ]

Q. Volume과 Bind Mount 차이는?

A.
Volume은 Docker가 관리하는 저장소이고, Bind Mount는 Host 경로를 Container에 직접 연결하는 방식이다.

Q. Container를 삭제하면 DB 데이터도 삭제되는가?

A.
Named Volume을 사용하면 Container를 삭제해도 데이터는 유지된다.

---

# 15. Port Mapping Rules

## 15.1 Port Mapping 작성 규칙

### [개념]

Port Mapping은 Host Port와 Container Port를 연결하여 외부 접근을 가능하게 하는 설정이다.

---

### [핵심]

형식:

```text
hostPort:containerPort
```

예:

```bash
docker run -p 8080:8080 my-app:latest
```

---

### [실무]

Compose 예시:

```yaml
services:
  app:
    ports:
      - "8080:8080"
```

Host 접근:

```text
http://localhost:8080
```

Container 내부 App Port:

```text
8080
```

---

### [주의]

Port 충돌이 발생하면 Container 실행이 실패한다.

확인:

```bash
docker ps
```

```bash
netstat -ano
```

```bash
lsof -i :8080
```

---

### [FAQ]

Q. `8080:8080`에서 앞의 8080과 뒤의 8080은 무엇인가?

A.
앞은 Host Port이고 뒤는 Container Port이다.

Q. Port is already allocated 오류는 무엇인가?

A.
Host Port를 이미 다른 Process 또는 Container가 사용 중이라는 뜻이다.

---

# 16. Healthcheck Rules

## 16.1 Healthcheck 작성 규칙

### [개념]

Healthcheck는 Container 내부 Application이 정상 동작하는지 주기적으로 검사하는 설정이다.

---

### [핵심]

필수 포함:

- healthcheck
- interval
- timeout
- retries
- start_period
- healthy
- unhealthy

---

### [실무]

Compose Healthcheck 예시:

```yaml
services:
  app:
    image: my-app:latest
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/actuator/health"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
```

Spring Boot Healthcheck Endpoint:

```text
/actuator/health
```

---

### [주의]

Container Running 상태와 Application Ready 상태는 다르다.

```text
Container Running
≠ Application Ready
```

---

### [FAQ]

Q. Container가 Running인데 서비스 접속이 안 되는 이유는?

A.
Process는 실행 중이지만 Application이 아직 Ready 상태가 아니거나 내부 오류가 발생했을 수 있다.

Q. Healthcheck는 왜 필요한가?

A.
Container 실행 여부가 아니라 Application 정상 동작 여부를 검증하기 위해 필요하다.

---

# 17. Logging Rules

## 17.1 Docker Logging 작성 규칙

### [개념]

Docker Logging은 Container 표준 출력과 표준 에러를 수집하여 확인하는 방식이다.

---

### [핵심]

필수 포함:

- stdout
- stderr
- docker logs
- log driver
- log rotation
- centralized logging

---

### [실무]

로그 확인:

```bash
docker logs app
```

실시간 로그:

```bash
docker logs -f app
```

마지막 로그 확인:

```bash
docker logs --tail 100 app
```

Compose 로그:

```bash
docker compose logs -f app
```

---

### [Best Practice]

Application 로그는 File보다 stdout / stderr로 출력한다.

운영 환경에서는 다음과 연계한다.

- Log Rotation
- Centralized Logging
- Monitoring
- Alerting

---

### [FAQ]

Q. Docker Container 로그는 어디로 출력하는 것이 좋은가?

A.
Container 환경에서는 stdout / stderr 출력이 기본이다. Docker와 운영 로깅 시스템이 이를 수집한다.

Q. 로그 파일을 Container 내부에만 저장해도 되는가?

A.
권장하지 않는다. Container 삭제 시 손실될 수 있으므로 외부 수집 또는 Volume 전략이 필요하다.

---

# 18. Resource Limit Rules

## 18.1 Resource Limit 작성 규칙

### [개념]

Resource Limit은 Container가 사용할 CPU, Memory 자원을 제한하는 설정이다.

---

### [핵심]

필수 포함:

- CPU Limit
- Memory Limit
- OOM
- Restart Policy
- Resource Monitoring

---

### [실무]

Docker Run 예시:

```bash
docker run -d --name app --memory=512m --cpus=1.0 my-app:latest
```

Compose 예시:

```yaml
services:
  app:
    image: my-app:latest
    mem_limit: 512m
    cpus: 1.0
```

상태 확인:

```bash
docker stats
```

---

### [주의]

Memory Limit이 낮으면 OOM Kill이 발생할 수 있다.

Java Application은 Container Memory Limit을 고려해야 한다.

예:

```bash
java -XX:MaxRAMPercentage=75 -jar app.jar
```

---

### [FAQ]

Q. Container가 갑자기 종료되는 이유는?

A.
OOM Kill, Application Crash, Healthcheck 실패, Restart Policy 설정 문제일 수 있다.

Q. Docker Container 자원 사용량은 어떻게 확인하는가?

A.
`docker stats` 명령으로 CPU, Memory, Network, Block I/O 사용량을 확인한다.

---

# 19. Registry Rules

## 19.1 Docker Registry 작성 규칙

### [개념]

Docker Registry는 Docker Image를 저장하고 배포하는 저장소이다.

---

### [핵심]

필수 포함:

- Docker Hub
- GitHub Container Registry
- AWS ECR
- Image Tag
- Push
- Pull
- Login
- Permission

---

### [Flow]

```text
Docker Build
→ Docker Tag
→ Registry Login
→ Docker Push
→ Server Pull
→ Container Run
```

---

### [실무]

Image Tag:

```bash
docker tag my-app:latest username/my-app:1.0.0
```

Docker Hub Push:

```bash
docker push username/my-app:1.0.0
```

Pull:

```bash
docker pull username/my-app:1.0.0
```

---

### [Best Practice]

Tag 전략:

- `latest` 단독 사용 금지
- Semantic Version 사용
- Git Commit SHA 사용
- Environment Tag 사용 가능

예:

```text
my-app:1.0.0
my-app:2026.06.29
my-app:git-a1b2c3d
my-app:prod
```

---

### [FAQ]

Q. Docker Image Tag에 latest만 사용해도 되는가?

A.
권장하지 않는다. latest는 어떤 버전인지 명확하지 않아 Rollback과 추적이 어렵다.

Q. Registry Push가 실패하는 이유는?

A.
Login 실패, Image Tag 오류, 권한 부족, Registry 주소 오류, Network 문제일 수 있다.

---

# 20. CI/CD Docker Build Rules

## 20.1 CI/CD 연계 규칙

### [개념]

CI/CD Docker Build는 Source Code 변경 시 Image를 자동 Build하고 Registry에 Push하는 Pipeline 단계이다.

---

### [핵심]

필수 포함:

- CI Pipeline
- Docker Build
- Image Tag
- Registry Login
- Docker Push
- Deploy Trigger
- Rollback Image

---

### [Flow]

```text
Git Push
→ CI Checkout
→ Test
→ Docker Build
→ Docker Tag
→ Registry Push
→ Deploy
```

---

### [실무]

GitHub Actions Docker Build 예시:

```yaml
name: Docker Build

on:
  push:
    branches:
      - main

jobs:
  docker-build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Build Docker image
        run: docker build -t my-app:${{ github.sha }} .

      - name: Login to registry
        run: echo "${{ secrets.REGISTRY_PASSWORD }}" | docker login -u "${{ secrets.REGISTRY_USERNAME }}" --password-stdin

      - name: Push Docker image
        run: |
          docker tag my-app:${{ github.sha }} username/my-app:${{ github.sha }}
          docker push username/my-app:${{ github.sha }}
```

---

### [주의]

CI/CD에서 Secret Hardcoding 금지.

필수:

- GitHub Secrets
- Jenkins Credentials
- Registry Token
- Least Privilege Permission

---

### [FAQ]

Q. CI/CD에서 Docker Image Tag는 무엇을 쓰는 것이 좋은가?

A.
Git Commit SHA, Semantic Version, Build Number를 사용하면 추적과 Rollback이 쉽다.

Q. CI/CD Docker Build에서 테스트는 언제 실행해야 하는가?

A.
Docker Image Push 전에 실행해야 한다. 실패한 코드는 Image로 배포하지 않는다.

---

# 21. Docker Security Rules

## 21.1 Docker Security 작성 규칙

### [개념]

Docker Security는 Image, Container, Secret, 권한, Runtime 설정의 위험을 줄이는 실무 기준이다.

---

### [핵심]

필수 포함:

- Non-root User
- Secret Hardcoding 금지
- Minimal Base Image
- Image Vulnerability Scan
- Read-only Filesystem
- Least Privilege
- Port Exposure 최소화
- Docker Socket Mount 주의

---

### [실무]

Non-root User 예시:

```dockerfile
FROM eclipse-temurin:21-jre

WORKDIR /app

RUN useradd -r appuser

COPY build/libs/app.jar app.jar

USER appuser

ENTRYPOINT ["java", "-jar", "app.jar"]
```

불필요한 권한 금지:

```yaml
services:
  app:
    image: my-app:latest
    privileged: false
```

---

### [주의]

위험한 설정:

```yaml
services:
  app:
    privileged: true
```

```yaml
services:
  app:
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```

Docker Socket Mount는 Host Docker 제어권 노출 위험이 있다.

---

### [FAQ]

Q. Container를 root로 실행하면 안 되는가?

A.
가능하면 피해야 한다. Container 탈출 또는 권한 상승 사고 시 피해 범위가 커질 수 있다.

Q. Docker Socket Mount는 왜 위험한가?

A.
Container 내부에서 Host Docker Daemon을 제어할 수 있어 Host 장악 위험이 있다.

---

# 22. Production Dockerfile Rules

## 22.1 Production Dockerfile 작성 규칙

### [개념]

Production Dockerfile은 운영 환경에서 안정성, 보안, 재현성, 추적성을 고려한 Dockerfile이다.

---

### [핵심]

필수 포함:

- Fixed Base Image Version
- Multi-stage Build
- Runtime Artifact Only
- Non-root User
- Healthcheck
- Minimal Package
- Secret Exclusion
- Reproducible Build

---

### [실무]

Production Checklist:

- Base Image Version 고정
- `.dockerignore` 적용
- Multi-stage Build 적용
- Runtime Image 최소화
- Secret 미포함
- Non-root User 사용
- Healthcheck 구성
- Image Tag 명확화
- Vulnerability Scan 수행
- Registry Push 전 Test 완료

---

### [주의]

나쁨:

```dockerfile
FROM latest
```

좋음:

```dockerfile
FROM eclipse-temurin:21-jre
```

더 엄격한 운영 기준에서는 digest pinning도 고려한다.

---

### [FAQ]

Q. 운영 Dockerfile에서 latest Tag를 사용해도 되는가?

A.
권장하지 않는다. Build 재현성이 떨어지고 예상치 못한 변경이 운영 장애로 이어질 수 있다.

Q. Production Dockerfile의 핵심 기준은?

A.
작고, 안전하고, 재현 가능하며, 실행에 필요한 파일만 포함하는 것이다.

---

# 23. Troubleshooting Rules

## 23.1 Docker Troubleshooting 작성 규칙

### [개념]

Troubleshooting 문서는 문제, 원인, 해결 형식으로 작성한다.

형식:

```text
문제:
원인:
해결:
```

---

### [핵심]

반드시 포함할 문제:

- Build Failed
- Cache Not Working
- Container Exited
- Port Already Allocated
- DB Connection Failed
- Volume Permission Denied
- Image Pull Failed
- Registry Login Failed
- Healthcheck Failed
- OOM Killed
- Secret Missing
- Network Not Found

---

### [실무]

Container 종료 확인:

```bash
docker ps -a
```

로그 확인:

```bash
docker logs app
```

상세 정보 확인:

```bash
docker inspect app
```

자원 사용량 확인:

```bash
docker stats
```

Network 확인:

```bash
docker network ls
```

Volume 확인:

```bash
docker volume ls
```

---

### [Troubleshooting]

문제:
Container가 바로 종료된다.

원인:

- ENTRYPOINT 오류
- 환경 변수 누락
- Application Crash
- Port Binding 실패
- Permission 문제

해결:

```bash
docker ps -a
docker logs containerName
docker inspect containerName
```

---

문제:
DB 연결 실패.

원인:

- localhost 사용
- Compose Service Name 오류
- Network 분리
- DB Ready 전 App 실행
- Port 오해

해결:

```text
jdbc:mysql://db:3306/appdb
```

Healthcheck와 depends_on 조건을 함께 사용한다.

---

문제:
Volume Permission Denied.

원인:

- Host Directory 권한 문제
- Container User 권한 문제
- root / non-root User 불일치

해결:

```bash
ls -al
chown
chmod
```

운영에서는 권한을 최소 범위로 조정한다.

---

### [FAQ]

Q. Docker 문제 해결의 첫 단계는?

A.
`docker ps -a`로 상태를 보고, `docker logs`로 오류를 확인하는 것이다.

Q. Compose 환경에서 DB 연결 문제의 가장 흔한 원인은?

A.
`localhost`를 DB Host로 사용하는 것이다. Compose 내부에서는 Service Name을 사용해야 한다.

---

# 24. Common Mistakes

## 24.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Review Agent가 Docker 설정을 검토할 때 우선 탐지해야 하는 위험 패턴이다.

---

### [핵심]

자주 발생:

- Dockerfile에 Secret Hardcoding
- `.env` Git Commit
- latest Tag 의존
- Build Context 과다
- `.dockerignore` 누락
- Runtime Image에 Build Tool 포함
- Multi-stage Build 미사용
- Container 내부 localhost 오해
- Volume 데이터 삭제
- Port Mapping 방향 오해
- Healthcheck 미구성
- root User 실행
- Docker Socket Mount 남용
- Rollback 가능한 Image Tag 없음

---

### [실무]

Review Agent 검토 기준:

```text
Dockerfile
→ Image Size
→ Secret
→ User Permission
→ Port
→ Env
→ Volume
→ Network
→ Healthcheck
→ Registry Tag
→ CI/CD Integration
```

---

### [FAQ]

Q. Docker Review에서 가장 먼저 봐야 하는 것은?

A.
Secret Hardcoding, latest Tag, root 실행, Build Context, Multi-stage Build 여부를 먼저 확인한다.

Q. Docker Compose Review에서 가장 중요한 항목은?

A.
Service Name 기반 통신, Volume 데이터 유지, Healthcheck, Environment 분리, Port 충돌 여부이다.

---

# 25. File Relationship Rules

## 25.1 다른 Domain Rules와 연계

### [개념]

Docker Advanced Domain Rules는 DevOps Expert 문서 체계에서 CI/CD, Kubernetes, Linux / Ubuntu Server와 연결된다.

---

### [핵심]

연계 구조:

```text
Docker Advanced
→ CI/CD
→ Registry
→ Kubernetes
→ Monitoring
```

---

### [실무]

파일 간 역할 분리:

| Domain                | 역할                                                     |
| --------------------- | -------------------------------------------------------- |
| Docker Advanced       | Container Image / Runtime / Compose / Docker Security    |
| CI/CD                 | Build / Test / Image Push / Deploy Pipeline              |
| Kubernetes            | Container Orchestration / Deployment / Service / Ingress |
| Linux / Ubuntu Server | Host OS / Process / Permission / Network                 |
| Monitoring & Logging  | Runtime Observability / Alerting                         |

---

### [FAQ]

Q. Docker Advanced와 CI/CD는 어디서 연결되는가?

A.
Docker Image Build, Tag, Registry Push 단계에서 연결된다.

Q. Docker Advanced와 Kubernetes는 어디서 연결되는가?

A.
Kubernetes는 Dockerfile로 만든 Container Image를 Pod로 실행하는 단계에서 연결된다.

---

# 26. Retrieval Optimization Rules

## 26.1 Retrieval 최적화 규칙

### [개념]

Docker Advanced 문서는 Docker 문제 상황 검색에 강해야 한다.

사용자 질문은 대부분 개념보다 문제 형태로 들어온다.

---

### [핵심]

강조 대상:

- Dockerfile
- Docker Build
- Multi-stage Build
- Docker Compose
- Container Network
- Docker Volume
- Port Mapping
- Environment Variable
- Docker Registry
- Image Tag
- Healthcheck
- Docker Security
- Troubleshooting

---

### [실무]

반복 허용 키워드:

- Docker Build 실패
- Dockerfile 최적화
- Docker Compose DB 연결
- Container localhost 문제
- Docker Volume Permission
- Docker Port 충돌
- Docker Image Size 줄이기
- Docker Registry Push 실패
- Container Healthcheck 실패
- Docker Secret 관리
- Docker Production 설정

---

### [FAQ]

Q. Docker RAG 문서에서 FAQ를 강화해야 하는 이유는?

A.
Docker 질문은 오류 메시지와 문제 상황 형태가 많아서 FAQ가 Retrieval Matching 성능을 높인다.

Q. Docker Advanced 문서는 어떤 질문에 강해야 하는가?

A.
Dockerfile 작성, Compose 연결, Network 오류, Volume 오류, Build 실패, Registry Push 실패, 운영 보안 검토 질문에 강해야 한다.

---

# 27. Version Rules

## 27.1 버전 기준

### [개념]

Docker Advanced 문서는 Modern Docker 기준으로 작성한다.

---

### [핵심]

기준:

- Docker Engine
- Docker Compose v2
- BuildKit
- OCI Image
- Modern Registry
- GitHub Actions 연계
- Kubernetes 연계 가능 구조

---

### [실무]

Legacy 표현 주의:

- `docker-compose` 단독 명령보다 `docker compose` 우선
- Swarm 중심 설명 제외
- 오래된 Java / Node Base Image 기준 제외
- Manual Deploy 중심 설명 제외

---

### [FAQ]

Q. Docker Compose 명령은 `docker-compose`와 `docker compose` 중 무엇을 우선하는가?

A.
2026 기준 문서에서는 Docker Compose v2 형식인 `docker compose`를 우선한다.

Q. Docker Swarm을 중심으로 작성해야 하는가?

A.
아니다. Kubernetes 연계 가능성을 고려하여 Docker Image, Compose, Registry, CI/CD 중심으로 작성한다.

---

# 28. Quality Checklist

## 28.1 최종 검수 기준

### [개념]

Docker Advanced RAG 문서는 Agent가 Docker 실무 문제를 해결할 수 있도록 검수한다.

---

### [핵심]

검수 항목:

- MASTER_RAG_RULES 구조 준수
- Docker Advanced Scope 충족
- CI/CD Domain Rules와 충돌 없음
- Kubernetes Domain Rules와 역할 분리
- FAQ 포함
- Retrieval Queries 포함
- Secret Hardcoding 금지 강조
- Dockerfile / Compose 예제 포함
- Troubleshooting 포함
- 용어 통일
- 긴 서술 최소화
- 코드블록 id 제거
- 오타 최소화

---

### [실무]

품질 목표:

- Minimum: 95/100
- Target: 97+/100

---

### [FAQ]

Q. Docker Advanced 문서 품질은 무엇으로 판단하는가?

A.
Agent가 Dockerfile 작성, Compose 구성, Build / Runtime 오류 해결, 보안 검토를 수행할 수 있으면 품질이 높다.

---

# 29. Final Goal

## 29.1 최종 목표

### [개념]

Docker Advanced RAG 문서는 단순 Docker 설명서가 아니다.

DevOps Agent / Backend Agent / Review Agent가 Container 기반 개발과 배포를 수행하기 위한 실행 지식 문서이다.

---

### [핵심]

Agent 수행 목표:

- Retrieve Docker Workflow
- Generate Dockerfile
- Generate Docker Compose
- Optimize Docker Image
- Debug Container Runtime
- Review Docker Security
- Connect Docker with CI/CD
- Prepare Image for Kubernetes

---

### [실무]

최종 연결 흐름:

```text
Backend Application
→ Dockerfile
→ Docker Image
→ Docker Compose Local Test
→ CI/CD Docker Build
→ Registry Push
→ Kubernetes Deploy
```

---

### [FAQ]

Q. Docker Advanced 문서의 최종 목적은?

A.
Agent가 Docker 기반 빌드, 실행, 배포, 문제 해결, 보안 검토를 실무 수준으로 수행하게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Docker Advanced Domain Rules는 무엇인가?
A. DevOps Agent, Backend Agent, Review Agent가 Dockerfile, Compose, Image, Network, Volume, Registry, Security, Troubleshooting을 수행하기 위한 RAG 작성 규칙이다.

Q. Docker Advanced 문서의 핵심 범위는?
A. Dockerfile, Multi-stage Build, Image Optimization, Docker Compose, Network, Volume, Registry, CI/CD Docker Build, Security, Troubleshooting이다.

Q. Dockerfile 작성 시 가장 중요한 기준은?
A. Base Image 최소화, Multi-stage Build, Secret Hardcoding 금지, Non-root User, `.dockerignore`, Runtime Artifact 최소화이다.

Q. Multi-stage Build는 왜 사용하는가?
A. Build 도구와 소스 파일을 Runtime Image에서 제거하여 Image Size와 보안 위험을 줄이기 위해 사용한다.

Q. Docker Build Context는 무엇인가?
A. `docker build` 실행 시 Docker Daemon에 전달되는 파일 범위이다.

Q. `.dockerignore`는 왜 필요한가?
A. 불필요한 파일과 Secret을 Build Context에서 제외하여 Build 속도와 보안을 개선한다.

Q. Docker Image Layer는 왜 중요한가?
A. Layer는 Build Cache와 Image Size에 영향을 주며, Layer 설계가 좋으면 Build가 빨라진다.

Q. Docker Compose는 무엇인가?
A. 여러 Container를 YAML 파일 하나로 정의하고 실행하는 Docker 도구이다.

Q. Docker Compose에서 DB Host는 무엇으로 설정해야 하는가?
A. `localhost`가 아니라 Compose Service Name을 사용해야 한다. 예: `db:3306`

Q. Container 내부 localhost는 무엇을 의미하는가?
A. Host PC가 아니라 Container 자기 자신을 의미한다.

Q. Docker Volume과 Bind Mount 차이는?
A. Volume은 Docker가 관리하는 저장소이고 Bind Mount는 Host 경로를 Container에 직접 연결하는 방식이다.

Q. Container를 삭제하면 Volume 데이터도 삭제되는가?
A. Named Volume을 사용하면 Container 삭제 후에도 데이터가 유지된다.

Q. Docker Port Mapping에서 `8080:8080`은 무슨 뜻인가?
A. 앞의 8080은 Host Port이고 뒤의 8080은 Container Port이다.

Q. Port is already allocated 오류는 무엇인가?
A. Host Port를 이미 다른 Process 또는 Container가 사용 중이라는 뜻이다.

Q. Healthcheck는 왜 필요한가?
A. Container 실행 여부가 아니라 Application 정상 동작 여부를 확인하기 위해 필요하다.

Q. Container가 Running인데 접속이 안 되는 이유는?
A. Application Ready 전이거나, Port Mapping 오류, 내부 Crash, Network 문제일 수 있다.

Q. Docker Registry는 무엇인가?
A. Docker Image를 저장하고 Pull / Push하는 저장소이다.

Q. Docker Image Tag에 latest만 사용해도 되는가?
A. 권장하지 않는다. 버전 추적과 Rollback이 어렵기 때문이다.

Q. CI/CD에서 Docker Build는 언제 수행되는가?
A. Test 통과 후 Image를 Build하고 Tag를 붙인 뒤 Registry에 Push하는 단계에서 수행된다.

Q. Docker Secret Hardcoding은 왜 금지인가?
A. Image Layer, Git, Registry를 통해 Credential이 노출될 수 있기 때문이다.

Q. Docker Container를 root로 실행하면 안 되는 이유는?
A. 권한 상승이나 Container 탈출 사고 시 피해 범위가 커질 수 있기 때문이다.

Q. Docker Socket Mount는 왜 위험한가?
A. Container가 Host Docker Daemon을 제어할 수 있어 Host 장악 위험이 생긴다.

Q. Production Dockerfile의 핵심 기준은?
A. 작고 안전하며 재현 가능하고 실행에 필요한 파일만 포함해야 한다.

Q. Docker 문제 해결 첫 단계는?
A. `docker ps -a`로 상태를 확인하고 `docker logs`로 오류 로그를 확인한다.

Q. Docker Compose에서 DB 연결 실패의 흔한 원인은?
A. `localhost` 사용, Service Name 오류, Network 분리, DB Ready 전 App 실행이다.

Q. Docker Advanced와 CI/CD는 어떻게 연결되는가?
A. Docker Image Build, Tag, Registry Push, Deploy Pipeline 단계에서 연결된다.

Q. Docker Advanced와 Kubernetes는 어떻게 연결되는가?
A. Dockerfile로 만든 Image를 Kubernetes Pod에서 실행하는 단계로 연결된다.

Q. Docker Advanced 문서에서 Swarm을 중심으로 다루는가?
A. 아니다. 2026 기준 Docker Compose, CI/CD, Registry, Kubernetes 연계 중심으로 작성한다.

Q. Docker Advanced 문서의 최종 목적은?
A. Agent가 Docker 기반 빌드, 실행, 배포, 문제 해결, 보안 검토를 수행하도록 만드는 것이다.
