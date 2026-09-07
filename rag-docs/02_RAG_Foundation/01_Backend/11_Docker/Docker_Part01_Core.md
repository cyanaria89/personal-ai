# Docker Part01 Core

---

# 1. Docker Core

## 1.1 Docker Overview

### [개념]

Docker는 Application을 Container 단위로 실행하기 위한 Containerization Platform이다.

Docker는 Application Code, Runtime, Library, Dependency, Environment를 하나의 실행 단위로 묶어 동일한 환경에서 실행하도록 지원한다.

Docker의 핵심 목적은 Environment Standardization이다.

```text
Application Code
→ Docker Image Build
→ Docker Container Run
→ Same Runtime Environment
```

Docker는 개발 환경, 테스트 환경, 운영 환경의 차이를 줄이고, 배포 자동화와 인프라 표준화를 지원한다.

---

### [핵심]

- Docker는 Container 기반 Runtime Environment를 제공한다.
- Docker는 Application 실행 환경을 Image로 패키징한다.
- Docker는 Image를 실행하여 Container를 생성한다.
- Docker는 환경 차이로 인한 오류를 줄인다.
- Docker는 배포 자동화, 확장성, 재현성을 높인다.
- Docker는 DevOps Agent가 Containerization, Deployment Automation, Troubleshooting을 수행할 때 핵심 도구이다.

핵심 용어:

| Term           | Meaning                                   |
| -------------- | ----------------------------------------- |
| Docker         | Containerization Platform                 |
| Image          | Container 실행을 위한 Immutable Blueprint |
| Container      | Image의 실행 인스턴스                     |
| Registry       | Image 저장소                              |
| Dockerfile     | Image Build 명세 파일                     |
| Volume         | Container 데이터 영속성 저장소            |
| Network        | Container 간 통신 구성                    |
| Docker Compose | Multi Container 관리 도구                 |

---

### [Flow]

```text
Code
→ Dockerfile
→ docker build
→ Docker Image
→ docker run
→ Docker Container
→ Logs / Health Check
→ Deployment
```

---

### [실무]

2026 실무 기준 Docker는 Spring Boot, React, Redis, MySQL, Nginx, AI Server, Batch Worker를 표준화된 Runtime으로 실행하는 데 사용된다.

Spring Boot 프로젝트에서는 보통 다음 흐름을 사용한다.

```text
Spring Boot Source Code
→ ./gradlew bootJar
→ Dockerfile
→ docker build
→ docker run
→ Production Container
```

Multi Container 환경에서는 Docker Compose를 사용한다.

```text
Spring Boot App
+ MySQL
+ Redis
+ Nginx
→ docker compose up
```

실무에서 Docker를 사용하는 주요 이유:

- 로컬 개발 환경 통일
- CI/CD Build 환경 통일
- 서버 배포 자동화
- Dependency 충돌 감소
- Rollback 단순화
- Cloud / VM / Bare Metal 환경 이식성 확보
- Container 로그 및 상태 관리 단순화

---

### [주의]

Docker는 Application Runtime을 격리하지만 모든 문제를 자동으로 해결하지 않는다.

주의할 점:

- Container는 VM이 아니다.
- Container 내부 데이터는 기본적으로 영속적이지 않다.
- Secret을 Image에 포함하면 안 된다.
- 운영 환경에서는 Root User 실행을 피해야 한다.
- Port Conflict를 확인해야 한다.
- Volume, Network, Health Check를 명시해야 한다.
- Dockerfile Layer Cache를 고려해야 한다.
- Running 상태와 Healthy 상태를 구분해야 한다.

---

### [FAQ]

Q. Docker란?
A. Application 실행 환경을 Image로 패키징하고 Container로 실행하는 Containerization Platform이다.

Q. Docker를 왜 사용하는가?
A. 개발, 테스트, 운영 환경을 표준화하고 배포 자동화와 실행 환경 재현성을 높이기 위해 사용한다.

Q. Docker가 해결하는 핵심 문제는?
A. 환경 차이, Dependency 충돌, 배포 재현성 부족, 서버 설정 불일치 문제를 줄인다.

Q. Docker는 운영 배포에만 필요한가?
A. 아니다. 로컬 개발, 테스트, CI/CD, 운영 배포 모두에서 사용된다.

---

# 2. Docker Architecture

## 2.1 Docker Architecture Components

### [개념]

Docker Architecture는 Docker Client, Docker Daemon, Docker Image, Docker Container, Docker Registry로 구성된다.

```text
Docker Client
→ Docker Daemon
→ Image Build / Pull
→ Container Run
→ Host OS Kernel
```

Docker Client는 사용자의 명령을 전달한다.

Docker Daemon은 Image, Container, Network, Volume을 관리한다.

Docker Registry는 Image를 저장하고 배포한다.

---

### [핵심]

Docker Architecture 핵심 구성:

| Component        | Role                          |
| ---------------- | ----------------------------- |
| Docker Client    | docker 명령어 실행            |
| Docker Daemon    | Container Runtime 관리        |
| Docker Image     | Container 실행 템플릿         |
| Docker Container | 실행 중인 Application Process |
| Docker Registry  | Image 저장소                  |
| Docker Network   | Container 통신                |
| Docker Volume    | 데이터 영속성                 |
| Host OS Kernel   | Container가 공유하는 Kernel   |

Docker 실행 흐름:

```text
docker run nginx
→ Docker Client sends command
→ Docker Daemon checks local image
→ Pull image from Registry if needed
→ Create Container
→ Start Process
```

---

### [실무]

실무에서는 Docker Daemon이 Host OS 위에서 실행되고, Application은 Container Process로 실행된다.

Ubuntu 서버 기준 기본 구조:

```text
Ubuntu Host
├─ Docker Daemon
├─ Docker Network
├─ Docker Volume
└─ Containers
   ├─ spring-app
   ├─ mysql
   ├─ redis
   └─ nginx
```

Spring Boot + MySQL 실행 예시:

```bash
docker run --name mysql -e MYSQL_ROOT_PASSWORD=pass -d mysql:8.4
docker run --name app -p 8080:8080 -d my-spring-app:1.0
```

운영 환경에서는 단일 `docker run`보다 `docker compose` 또는 Kubernetes 기반 구성이 일반적이다.

---

### [주의]

Docker Daemon은 강한 권한을 가진다.

주의할 점:

- Docker Group 권한은 Root 수준 권한과 유사하게 취급해야 한다.
- 운영 서버에서 무분별한 Docker Socket Mount를 피해야 한다.
- `/var/run/docker.sock` 노출은 보안 위험이 크다.
- Docker Host 리소스 부족은 모든 Container에 영향을 준다.
- Docker Daemon 장애는 Container 관리 기능에 영향을 준다.

---

### [FAQ]

Q. Docker Client와 Docker Daemon의 차이는?
A. Docker Client는 명령어를 보내는 도구이고, Docker Daemon은 실제 Image와 Container를 관리하는 백그라운드 서비스이다.

Q. Docker Registry는 무엇인가?
A. Docker Image를 저장하고 Pull / Push 할 수 있는 저장소이다. Docker Hub와 Private Registry가 대표적이다.

Q. Docker Daemon은 무엇을 관리하는가?
A. Image, Container, Network, Volume, Build, Logs 등 Docker Runtime Resource를 관리한다.

---

# 3. Container

## 3.1 Container Concept

### [개념]

Container는 Docker Image를 실행한 Runtime Instance이다.

Container는 Host OS Kernel을 공유하면서 Process, File System, Network, Resource를 격리한다.

```text
Docker Image
→ docker run
→ Docker Container
```

Container는 Application을 독립된 실행 단위로 실행한다.

---

### [핵심]

Container 핵심:

- Container는 Image의 실행 인스턴스이다.
- Container는 Process Isolation을 제공한다.
- Container는 Host OS Kernel을 공유한다.
- Container는 VM보다 가볍다.
- Container는 생성, 시작, 중지, 삭제 Lifecycle을 가진다.
- Container 내부 변경 사항은 기본적으로 영속적이지 않다.
- Container의 Main Process가 종료되면 Container도 종료된다.

Container Lifecycle:

```text
Created
→ Running
→ Paused
→ Stopped
→ Removed
```

기본 명령어:

```bash
docker run nginx
docker ps
docker stop nginx
docker rm nginx
```

---

### [실무]

실무에서는 Container를 Application Process 하나를 실행하는 단위로 보는 것이 좋다.

Spring Boot Container 예시:

```bash
docker run \
  --name spring-app \
  -p 8080:8080 \
  -e SPRING_PROFILES_ACTIVE=prod \
  -d my-spring-app:1.0
```

권장 구조:

```text
1 Container = 1 Main Process
```

예:

| Container  | Main Process        |
| ---------- | ------------------- |
| spring-app | Java Spring Boot    |
| mysql      | MySQL Server        |
| redis      | Redis Server        |
| nginx      | Nginx Reverse Proxy |

---

### [주의]

Container를 VM처럼 사용하면 안 된다.

잘못된 방식:

```text
Container 내부 접속
→ 수동 설정 변경
→ Container를 서버처럼 관리
```

권장 방식:

```text
Dockerfile / Compose 수정
→ Image Rebuild
→ Container Recreate
```

주의할 점:

- Container 삭제 시 내부 Writable Layer 데이터는 삭제될 수 있다.
- 영속 데이터는 Volume을 사용해야 한다.
- 운영 설정은 Environment Variable 또는 Secret으로 주입해야 한다.
- Container 이름, Port, Network를 명확히 관리해야 한다.
- `docker exec`는 디버깅 용도이며 운영 수정 방식이 아니다.

---

### [FAQ]

Q. Container란?
A. Docker Image를 실행한 인스턴스이며, 격리된 Process Runtime이다.

Q. Container는 VM인가?
A. 아니다. Container는 Host OS Kernel을 공유하는 격리된 Process이며 VM보다 가볍다.

Q. Container 안에 저장한 파일은 안전한가?
A. 기본적으로 안전하지 않다. Container 삭제 시 사라질 수 있으므로 Volume을 사용해야 한다.

Q. 하나의 Container에 여러 서비스를 넣어도 되는가?
A. 가능은 하지만 권장하지 않는다. 일반적으로 1 Container는 1 Main Process 원칙을 따른다.

---

# 4. Image

## 4.1 Docker Image Concept

### [개념]

Docker Image는 Container 실행을 위한 Immutable Blueprint이다.

Image는 Application Code, Runtime, Library, Dependency, File System, Metadata를 포함한다.

```text
Dockerfile
→ docker build
→ Docker Image
→ docker run
→ Docker Container
```

Image는 Layer 구조로 구성되며, Build Cache와 재사용성을 제공한다.

---

### [핵심]

Docker Image 핵심:

- Image는 Container 실행 템플릿이다.
- Image는 Immutable하다.
- Image는 Layer로 구성된다.
- Image는 Dockerfile로 Build한다.
- Image는 Tag로 Version을 식별한다.
- Image는 Registry에 Push / Pull 할 수 있다.
- Image는 환경별 Config보다 Runtime 자체를 고정하는 데 사용한다.

Image와 Container 차이:

| 구분 | Image                      | Container        |
| ---- | -------------------------- | ---------------- |
| 의미 | 실행 템플릿                | 실행 인스턴스    |
| 상태 | Immutable                  | Runtime State    |
| 생성 | docker build / docker pull | docker run       |
| 저장 | Registry 가능              | Runtime Host     |
| 비유 | Blueprint                  | Running Instance |

---

### [실무]

Spring Boot Image Build 예시:

```dockerfile
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY build/libs/app.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

Build 명령어:

```bash
docker build -t spring-app:1.0 .
```

Run 명령어:

```bash
docker run -p 8080:8080 spring-app:1.0
```

Tag 전략:

```text
spring-app:1.0.0
spring-app:2026.06.26
spring-app:git-abc1234
spring-app:prod
```

운영에서는 `latest` 단독 사용을 피하고 명확한 Version Tag를 사용하는 것이 좋다.

---

### [주의]

Image에 포함하면 안 되는 것:

- DB Password
- API Key
- JWT Secret
- Private Key
- `.env`
- Local Config
- Build Cache 불필요 파일
- Log File
- Upload File

`.dockerignore` 예시:

```text
.git
node_modules
.env
*.log
```

Image Size 최적화가 중요하다.

```text
Large Image
→ Slow Pull
→ Slow Deploy
→ Larger Attack Surface
```

---

### [FAQ]

Q. Docker Image란?
A. Container를 실행하기 위한 Immutable Blueprint이다.

Q. Image와 Container의 차이는?
A. Image는 실행 템플릿이고 Container는 Image를 실행한 Runtime Instance이다.

Q. Image는 수정 가능한가?
A. Image 자체는 Immutable하다. 변경하려면 Dockerfile을 수정하고 다시 Build해야 한다.

Q. 운영에서 latest 태그를 써도 되는가?
A. 권장하지 않는다. 배포 추적성과 Rollback을 위해 명확한 Version Tag를 사용하는 것이 좋다.

---

# 5. Image Layer and Cache

## 5.1 Layer Concept

### [개념]

Docker Image Layer는 Docker Image를 구성하는 변경 불가능한 파일 시스템 단위이다.

Dockerfile의 Instruction은 Layer를 만들 수 있고, Docker는 변경되지 않은 Layer를 Cache로 재사용한다.

```text
Base Layer
→ Dependency Layer
→ Application Layer
```

Layer 구조는 Image 재사용성, Build 속도, 배포 효율에 영향을 준다.

---

### [핵심]

Layer 핵심:

- Image는 여러 Layer로 구성된다.
- Layer는 Immutable하다.
- Docker는 변경되지 않은 Layer를 Cache로 재사용한다.
- 상위 Layer가 변경되면 하위 Layer Cache가 무효화될 수 있다.
- 변경이 적은 파일을 먼저 COPY하는 것이 좋다.
- Source Code처럼 자주 바뀌는 파일은 나중에 COPY한다.

Cache 최적화 원칙:

```text
Stable Layer First
→ Frequently Changed Layer Later
```

---

### [실무]

비효율 Dockerfile 예시:

```dockerfile
COPY . .
RUN npm ci
```

문제:

```text
Source Code가 조금만 바뀌어도 Dependency Install Cache가 무효화됨
```

권장 Dockerfile 예시:

```dockerfile
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
```

Spring Boot Multi-stage Build에서도 Gradle Dependency Cache를 고려한다.

```dockerfile
COPY build.gradle settings.gradle ./
COPY gradle ./gradle
RUN gradle dependencies --no-daemon
COPY src ./src
RUN gradle clean bootJar --no-daemon
```

---

### [주의]

Layer Cache 최적화와 보안은 함께 고려해야 한다.

주의할 점:

- Secret이 포함된 Layer는 삭제해도 History에 남을 수 있다.
- `RUN rm secret.txt`는 안전한 Secret 제거 방식이 아니다.
- Package Cache 제거가 필요하다.
- `.dockerignore`로 불필요한 Build Context를 줄여야 한다.
- Layer 수만 줄이려다 가독성을 지나치게 해치면 안 된다.

---

### [FAQ]

Q. Docker Layer란?
A. Docker Image를 구성하는 변경 불가능한 파일 시스템 단위이다.

Q. Layer Cache는 왜 중요한가?
A. 변경되지 않은 Build 단계를 재사용하여 Image Build 속도를 높인다.

Q. Dockerfile Cache를 잘 활용하려면?
A. 변경이 적은 Dependency 파일을 먼저 COPY하고 자주 바뀌는 Source Code는 나중에 COPY한다.

---

# 6. Registry

## 6.1 Docker Registry Concept

### [개념]

Docker Registry는 Docker Image를 저장하고 배포하는 저장소이다.

Registry는 Image Pull / Push를 지원한다.

```text
Local Image
→ docker push
→ Docker Registry
→ docker pull
→ Server
```

대표적인 Registry:

- Docker Hub
- GitHub Container Registry
- AWS ECR
- Google Artifact Registry
- Azure Container Registry
- Private Registry

---

### [핵심]

Registry 핵심:

- Image 저장소 역할
- Image Version 관리
- 배포 서버에서 Image Pull
- CI/CD Pipeline과 연동
- Public / Private Registry 구분
- 접근 권한 관리 필요

기본 명령어:

```bash
docker pull nginx:1.27
docker tag myapp:1.0 username/myapp:1.0
docker push username/myapp:1.0
```

---

### [실무]

CI/CD 배포 흐름:

```text
Git Push
→ CI Build
→ Docker Image Build
→ Registry Push
→ Server Pull
→ Container Restart
```

Private Registry 사용 이유:

- 사내 Image 보호
- 배포 권한 관리
- 보안 정책 적용
- Cloud 배포 연동
- Image Version 관리

Spring Boot 배포 예시:

```bash
docker build -t registry.example.com/festapick-api:1.0.0 .
docker push registry.example.com/festapick-api:1.0.0
docker pull registry.example.com/festapick-api:1.0.0
```

---

### [주의]

Registry 사용 시 주의:

- Public Registry에 Secret 포함 Image Push 금지
- Image Tag 충돌 주의
- `latest` 덮어쓰기 주의
- Private Registry 인증 정보 관리
- Image 취약점 스캔 필요
- 오래된 Image 정리 필요
- Rollback용 이전 Image 유지 필요

---

### [FAQ]

Q. Docker Registry란?
A. Docker Image를 저장하고 Pull / Push 할 수 있는 저장소이다.

Q. Docker Hub와 Private Registry의 차이는?
A. Docker Hub는 공개 Registry로 많이 사용되고, Private Registry는 조직 내부 Image와 권한을 관리하는 데 사용된다.

Q. Registry가 없으면 Docker를 못 쓰는가?
A. 아니다. 로컬 Image만으로도 사용할 수 있다. 다만 서버 배포와 CI/CD에서는 Registry가 중요하다.

---

# 7. Docker vs Virtual Machine

## 7.1 Container and VM Comparison

### [개념]

Docker Container와 Virtual Machine은 모두 실행 환경 격리를 제공하지만 구조가 다르다.

VM은 Hypervisor 위에 Guest OS를 실행한다.

Container는 Host OS Kernel을 공유하고 Process 단위로 격리한다.

```text
VM:
Hardware
→ Host OS
→ Hypervisor
→ Guest OS
→ Application

Container:
Hardware
→ Host OS
→ Docker Engine
→ Container Process
→ Application
```

---

### [핵심]

Docker Container와 VM 차이:

| 항목        | Docker Container  | Virtual Machine |
| ----------- | ----------------- | --------------- |
| 격리 단위   | Process           | OS              |
| Kernel      | Host Kernel 공유  | Guest OS Kernel |
| 시작 속도   | 빠름              | 상대적으로 느림 |
| 리소스 사용 | 적음              | 많음            |
| 이미지 크기 | 작음              | 큼              |
| 이식성      | 높음              | 높음            |
| 보안 격리   | Process Isolation | OS Isolation    |
| 사용 목적   | Application 배포  | OS 단위 격리    |

---

### [실무]

Docker가 적합한 경우:

- Web Application 배포
- API Server 배포
- Microservice 실행
- CI/CD 환경
- 개발 환경 표준화
- Redis / MySQL / Nginx 실행
- Batch Worker 실행

VM이 적합한 경우:

- OS Kernel 수준 격리 필요
- 서로 다른 OS Kernel 필요
- 강한 보안 경계 필요
- Legacy System 운영
- 전체 서버 환경 에뮬레이션 필요

실무에서는 VM 위에 Docker를 올리는 구조도 자주 사용한다.

```text
Cloud VM
→ Ubuntu
→ Docker
→ Containers
```

---

### [주의]

Docker는 VM보다 가볍지만 VM을 완전히 대체하지 않는다.

주의할 점:

- Container는 Host Kernel을 공유한다.
- Kernel 수준 취약점은 Container에 영향을 줄 수 있다.
- 강한 멀티테넌트 격리가 필요한 환경에서는 VM 또는 Kubernetes 보안 정책이 필요하다.
- Docker를 OS처럼 관리하지 않는다.
- Container 보안과 Host 보안은 함께 관리해야 한다.

---

### [FAQ]

Q. Docker와 VM의 가장 큰 차이는?
A. Docker는 Host OS Kernel을 공유하는 Process 격리이고, VM은 Guest OS를 실행하는 OS 단위 격리이다.

Q. Docker가 VM보다 항상 좋은가?
A. 아니다. Application 배포에는 Docker가 유리하지만 강한 OS 격리에는 VM이 유리하다.

Q. 실무에서는 Docker와 VM 중 하나만 사용하는가?
A. 아니다. Cloud VM 위에 Docker를 설치하고 Container를 운영하는 구조가 흔하다.

---

# 8. Docker Workflow

## 8.1 Basic Docker Workflow

### [개념]

Docker Workflow는 Code를 Image로 Build하고 Container로 실행하는 흐름이다.

```text
Code
→ Dockerfile
→ Build Image
→ Run Container
→ Deploy
```

Docker는 Application 실행 환경을 Build 단계에서 고정하고, Runtime 단계에서 동일하게 재현한다.

---

### [핵심]

Docker 기본 Workflow:

1. Application Code 작성
2. Dockerfile 작성
3. Docker Image Build
4. Docker Container Run
5. Logs 확인
6. Health Check 확인
7. Registry Push
8. Server Pull
9. Deploy

명령어 흐름:

```bash
docker build -t myapp:1.0 .
docker run -p 8080:8080 myapp:1.0
docker logs myapp
docker push myapp:1.0
```

---

### [실무]

Spring Boot Application Workflow:

```text
Java Source Code
→ Gradle Build
→ bootJar
→ Dockerfile
→ Docker Image
→ Container
→ Server Deploy
```

명령어 예시:

```bash
./gradlew clean bootJar
docker build -t festapick-api:1.0.0 .
docker run --name festapick-api -p 8080:8080 festapick-api:1.0.0
```

Compose 기반 Workflow:

```bash
docker compose build
docker compose up -d
docker compose logs -f
docker compose down
```

---

### [주의]

Docker Workflow에서 자주 발생하는 문제:

| Problem              | Cause                   | Solution                |
| -------------------- | ----------------------- | ----------------------- |
| Build Failed         | Dockerfile 경로 오류    | Build Context 확인      |
| Port Conflict        | Host Port 사용 중       | Port Mapping 변경       |
| Container Exit       | Main Process 종료       | docker logs 확인        |
| Permission Denied    | File 권한 문제          | User / Volume 권한 확인 |
| DB Connection Failed | Network / Hostname 문제 | Service Name 확인       |
| Env Missing          | 환경변수 누락           | environment 설정 확인   |

---

### [FAQ]

Q. Docker 기본 작업 흐름은?
A. Code 작성 후 Dockerfile로 Image를 Build하고, Image를 Container로 실행한 뒤 배포한다.

Q. docker build와 docker run의 차이는?
A. docker build는 Image를 만드는 명령이고, docker run은 Image를 Container로 실행하는 명령이다.

Q. docker compose는 언제 사용하는가?
A. Spring Boot, MySQL, Redis처럼 여러 Container를 함께 실행해야 할 때 사용한다.

---

# 9. Container Lifecycle

## 9.1 Container Lifecycle Management

### [개념]

Container Lifecycle은 Container 생성부터 삭제까지의 상태 흐름이다.

```text
Image
→ Created
→ Running
→ Stopped
→ Removed
```

Container는 실행 중인 Process가 종료되면 Container도 종료된다.

---

### [핵심]

주요 명령어:

```bash
docker create nginx
docker start container_name
docker stop container_name
docker restart container_name
docker rm container_name
```

상태 확인:

```bash
docker ps
docker ps -a
docker inspect container_name
```

Lifecycle 상태:

| State   | Meaning         |
| ------- | --------------- |
| Created | 생성됨, 실행 전 |
| Running | 실행 중         |
| Paused  | 일시 정지       |
| Exited  | 종료됨          |
| Removed | 삭제됨          |

---

### [실무]

운영에서 자주 사용하는 Lifecycle 명령:

```bash
docker ps
docker logs -f app
docker restart app
docker stop app
docker rm app
```

Container 재배포 흐름:

```text
New Image Build
→ Old Container Stop
→ Old Container Remove
→ New Container Run
→ Logs Check
→ Health Check
```

예시:

```bash
docker stop festapick-api
docker rm festapick-api
docker run --name festapick-api -p 8080:8080 -d festapick-api:1.0.1
```

---

### [주의]

Container 삭제 전 확인:

- 필요한 데이터가 Volume에 저장되어 있는가?
- Container 이름이 다른 서비스에서 참조되는가?
- Network 설정이 유지되는가?
- Port Mapping이 동일한가?
- Env 값이 동일한가?
- Logs를 확인했는가?

Container 재시작만으로 해결하면 안 되는 경우:

- Image 변경 필요
- Dockerfile 변경 필요
- Env 구조 변경
- Volume 권한 문제
- Network 설계 문제

---

### [FAQ]

Q. Container가 바로 종료되는 이유는?
A. Container의 Main Process가 종료되었기 때문이다. `docker logs`로 원인을 확인해야 한다.

Q. docker stop과 docker rm의 차이는?
A. docker stop은 Container를 중지하고, docker rm은 Container를 삭제한다.

Q. Container를 삭제하면 Image도 삭제되는가?
A. 아니다. Container 삭제와 Image 삭제는 별개이다.

---

# 10. Docker Command Basics

## 10.1 Essential Docker Commands

### [개념]

Docker Command는 Image, Container, Volume, Network, Logs를 관리하기 위한 CLI 명령어이다.

Docker 명령어는 Docker Client를 통해 Docker Daemon에 전달된다.

```text
docker command
→ Docker Client
→ Docker Daemon
→ Docker Resource Control
```

---

### [핵심]

자주 사용하는 Docker 명령어:

| Command          | Purpose                          |
| ---------------- | -------------------------------- |
| docker build     | Image Build                      |
| docker run       | Container Create + Start         |
| docker ps        | Running Container 조회           |
| docker ps -a     | 전체 Container 조회              |
| docker images    | Image 조회                       |
| docker logs      | Container Logs 조회              |
| docker exec      | Running Container 내부 명령 실행 |
| docker stop      | Container 중지                   |
| docker rm        | Container 삭제                   |
| docker rmi       | Image 삭제                       |
| docker inspect   | 상세 정보 조회                   |
| docker pull      | Image 다운로드                   |
| docker push      | Image 업로드                     |
| docker stats     | Container Resource 조회          |
| docker system df | Docker Disk 사용량 조회          |

---

### [실무]

기본 실행:

```bash
docker run --name nginx-test -p 8080:80 -d nginx:1.27
```

로그 확인:

```bash
docker logs -f nginx-test
```

Container 내부 접속:

```bash
docker exec -it nginx-test sh
```

상세 정보 확인:

```bash
docker inspect nginx-test
```

정리:

```bash
docker stop nginx-test
docker rm nginx-test
```

---

### [주의]

`docker exec`로 Container 내부를 수정하는 것은 임시 디버깅 용도이다.

잘못된 실무 패턴:

```text
docker exec 접속
→ 설정 파일 직접 수정
→ 운영 반영
```

권장 패턴:

```text
Dockerfile / Compose 수정
→ Image Rebuild
→ Container Recreate
```

주의 명령어:

```bash
docker system prune -a
docker system prune -a --volumes
```

`--volumes` 옵션은 사용하지 않는 Volume까지 삭제할 수 있으므로 운영 서버에서는 매우 신중히 사용해야 한다.

---

### [FAQ]

Q. docker run은 무엇을 하는가?
A. Image를 기반으로 Container를 생성하고 실행한다.

Q. docker exec는 언제 쓰는가?
A. 실행 중인 Container 내부에서 디버깅 명령을 실행할 때 사용한다.

Q. docker logs는 무엇을 확인하는가?
A. Container의 stdout / stderr 로그를 확인한다.

Q. docker system prune은 안전한가?
A. 개발 환경에서는 유용하지만 운영 환경에서는 필요한 Image, Cache, Volume이 삭제될 수 있으므로 주의해야 한다.

---

# 11. Docker Core Best Practice

## 11.1 Core Best Practice

### [개념]

Docker Best Practice는 Image Size, Security, Reproducibility, Deployment Stability를 개선하기 위한 운영 기준이다.

Docker 문서의 핵심 목표는 Agent가 Dockerfile 생성, Compose 작성, Container 문제 해결, 배포 이슈 분석을 수행하도록 만드는 것이다.

---

### [핵심]

Docker Core Best Practice:

- Image와 Container 차이를 명확히 구분한다.
- Container는 Stateless하게 설계한다.
- 영속 데이터는 Volume에 저장한다.
- Secret은 Image에 포함하지 않는다.
- Dockerfile Layer Cache를 고려한다.
- `.dockerignore`를 사용한다.
- 운영에서는 Version Tag를 사용한다.
- Container 로그는 stdout / stderr로 출력한다.
- Health Check를 설정한다.
- Resource Limit을 설정한다.
- Root User 실행을 피한다.
- Multi Container는 Docker Compose로 관리한다.
- 운영 DB Port는 외부 공개를 피한다.
- `docker compose config`로 최종 설정을 검증한다.

---

### [실무]

Spring Boot Docker 기본 권장 구조:

```text
Application
├─ Dockerfile
├─ .dockerignore
├─ compose.yml
└─ build/libs/app.jar
```

운영 배포 기준:

```text
Build once
→ Tag clearly
→ Push Registry
→ Pull on Server
→ Run with Env
→ Check Logs
→ Check Health
```

기본 점검 Checklist:

- Dockerfile 존재 여부
- `.dockerignore` 존재 여부
- Image Size 확인
- Secret 포함 여부 확인
- Port Mapping 확인
- Volume 설정 확인
- Network 설정 확인
- Health Check 설정 확인
- Logs 출력 확인
- Restart Policy 확인

---

### [주의]

Docker 초보 단계에서 자주 발생하는 실수:

| Mistake                         | Problem            |
| ------------------------------- | ------------------ |
| Container를 VM처럼 사용         | 재현성 저하        |
| Secret을 Dockerfile에 작성      | 보안 위험          |
| Volume 미설정                   | 데이터 손실        |
| latest만 사용                   | Rollback 어려움    |
| Health Check 없음               | 장애 감지 어려움   |
| Root User 실행                  | 보안 위험          |
| Port 충돌 무시                  | 실행 실패          |
| 로그 파일만 내부 저장           | 로그 유실          |
| Large Image 방치                | 배포 지연          |
| Compose Network 미이해          | 서비스 연결 실패   |
| localhost로 다른 Container 접속 | Network 오류       |
| down -v 무분별 사용             | Volume 데이터 삭제 |

---

### [FAQ]

Q. Docker Core에서 가장 중요한 개념은?
A. Image는 실행 템플릿이고 Container는 실행 인스턴스라는 구분이다.

Q. Docker 운영 안정성을 높이려면 무엇이 필요한가?
A. Version Tag, Volume, Network, Health Check, Logs, Resource Limit, Secret 관리가 필요하다.

Q. Docker 문서에서 가장 먼저 학습해야 하는 순서는?
A. Docker Core, Container, Image, Dockerfile, Volume, Network, Docker Compose 순서가 적합하다.

---

# Retrieval Queries

### [FAQ]

Q. Docker란 무엇인가?
A. Docker는 Application 실행 환경을 Image로 패키징하고 Container로 실행하는 Containerization Platform이다.

Q. Docker를 왜 사용하는가?
A. Docker는 개발, 테스트, 운영 환경을 표준화하고 배포 재현성과 자동화를 높이기 위해 사용한다.

Q. Docker가 해결하는 문제는 무엇인가?
A. Docker는 환경 차이, Dependency 충돌, 서버 설정 불일치, 배포 재현성 부족 문제를 줄인다.

Q. Docker Architecture는 무엇으로 구성되는가?
A. Docker Client, Docker Daemon, Docker Image, Docker Container, Docker Registry, Network, Volume으로 구성된다.

Q. Docker Client와 Docker Daemon 차이는 무엇인가?
A. Docker Client는 명령어를 보내고 Docker Daemon은 Image, Container, Network, Volume을 실제로 관리한다.

Q. Container란 무엇인가?
A. Container는 Docker Image를 실행한 Runtime Instance이며 격리된 Process 실행 단위이다.

Q. Container는 VM인가?
A. 아니다. Container는 Host OS Kernel을 공유하는 격리된 Process이며 VM보다 가볍다.

Q. Image란 무엇인가?
A. Image는 Container 실행을 위한 Immutable Blueprint이며 Dockerfile로 Build한다.

Q. Image와 Container 차이는 무엇인가?
A. Image는 실행 템플릿이고 Container는 Image를 실행한 인스턴스이다.

Q. Docker Layer란 무엇인가?
A. Docker Layer는 Docker Image를 구성하는 변경 불가능한 파일 시스템 단위이다.

Q. Docker Layer Cache는 왜 중요한가?
A. 변경되지 않은 Build 단계를 재사용하여 Image Build 속도를 높이기 때문이다.

Q. Docker Registry란 무엇인가?
A. Docker Registry는 Docker Image를 저장하고 Pull / Push 할 수 있는 저장소이다.

Q. Docker Hub란 무엇인가?
A. Docker Hub는 Public Docker Registry이며 Docker Image를 공유하고 다운로드할 수 있다.

Q. Docker와 VM 차이는 무엇인가?
A. Docker는 Host OS Kernel을 공유하는 Process 격리이고 VM은 Guest OS를 실행하는 OS 단위 격리이다.

Q. Docker는 VM을 대체하는가?
A. Docker는 Application 배포에 적합하지만 VM을 완전히 대체하지는 않는다.

Q. Docker 기본 Workflow는 무엇인가?
A. Code 작성 후 Dockerfile로 Image를 Build하고 Container로 실행한 뒤 Registry와 Server를 통해 배포한다.

Q. docker build는 무엇인가?
A. docker build는 Dockerfile을 기반으로 Docker Image를 생성하는 명령어이다.

Q. docker run은 무엇인가?
A. docker run은 Docker Image를 기반으로 Container를 생성하고 실행하는 명령어이다.

Q. docker ps는 무엇인가?
A. docker ps는 실행 중인 Container 목록을 조회하는 명령어이다.

Q. docker logs는 무엇인가?
A. docker logs는 Container의 stdout / stderr 로그를 확인하는 명령어이다.

Q. docker exec는 무엇인가?
A. docker exec는 실행 중인 Container 내부에서 명령어를 실행하는 디버깅 명령어이다.

Q. docker stats는 무엇인가?
A. docker stats는 Container의 CPU, Memory, Network, Block I/O 사용량을 확인하는 명령어이다.

Q. Container Lifecycle은 무엇인가?
A. Container의 Created, Running, Paused, Exited, Removed 상태 흐름이다.

Q. Container가 바로 종료되는 이유는?
A. Container의 Main Process가 종료되었기 때문이다. docker logs로 원인을 확인해야 한다.

Q. Container 삭제 시 데이터는 유지되는가?
A. Container 내부 Writable Layer 데이터는 삭제될 수 있다. 영속 데이터는 Volume에 저장해야 한다.

Q. Docker에서 Secret을 어디에 저장하면 안 되는가?
A. Secret은 Dockerfile, Image, Git Repository에 하드코딩하면 안 된다.

Q. Docker 운영 Best Practice는 무엇인가?
A. Version Tag, Volume, Network, Health Check, stdout 로그, Resource Limit, Secret 관리, Root User 회피를 적용한다.

Q. Docker Compose는 언제 사용하는가?
A. Spring Boot, MySQL, Redis, Nginx처럼 여러 Container를 함께 실행하고 관리할 때 사용한다.

Q. Docker Core 문서의 핵심 목표는?
A. Agent가 Dockerfile 생성, Compose 작성, Container 실행, 배포 문제 해결을 수행할 수 있도록 Retrieval 품질을 높이는 것이다.
