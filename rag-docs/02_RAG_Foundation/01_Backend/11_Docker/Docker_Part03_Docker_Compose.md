# Docker Part03 Docker Compose

---

# 1. Docker Compose Core

## 1.1 Docker Compose Overview

### [개념]

Docker Compose는 여러 Container를 하나의 YAML 파일로 정의하고 실행하는 Multi Container Management Tool이다.

Docker Compose는 `compose.yml` 또는 `docker-compose.yml` 파일을 사용하여 Application, Database, Cache, Reverse Proxy, Message Queue 같은 여러 Service를 함께 관리한다.

```text
Single Container
→ docker run

Multi Container
→ docker compose up
```

Docker Compose는 Docker Compose v2 기준으로 `docker compose` 명령을 사용한다.

---

### [핵심]

Docker Compose 핵심 목적:

- Multi Container 실행
- Service 단위 구성
- Network 자동 생성
- Volume 관리
- Runtime Environment Variable 주입
- Service Dependency 정의
- Local Development Environment 표준화
- Integration Test Environment 구성
- Small Deployment 구성 지원

핵심 구성:

| Key         | Purpose                              |
| ----------- | ------------------------------------ |
| services    | 실행할 Container Service 정의        |
| image       | 사용할 Docker Image 지정             |
| build       | Dockerfile 기반 Image Build          |
| ports       | Host Port와 Container Port Mapping   |
| expose      | 내부 Network Port 노출               |
| environment | Runtime Environment Variable 주입    |
| env_file    | Environment Variable 파일 로드       |
| volumes     | Persistent Storage / Bind Mount 설정 |
| networks    | Container Network 설정               |
| depends_on  | Service 시작 순서 정의               |
| healthcheck | Container 상태 확인                  |
| restart     | Container Restart Policy 설정        |

---

### [Flow]

```text
compose.yml 작성
→ services 정의
→ networks 정의
→ volumes 정의
→ environment 주입
→ docker compose config 검증
→ docker compose up -d 실행
→ logs / healthcheck 확인
```

---

### [실무]

2026 실무 기준 Docker Compose는 로컬 개발 환경, 테스트 환경, 소규모 서버 배포, CI Integration Test 환경에서 많이 사용된다.

Spring Boot + MySQL + Redis Compose 예시:

```yaml
services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      SPRING_PROFILES_ACTIVE: local
      SPRING_DATASOURCE_URL: jdbc:mysql://mysql:3306/appdb
      SPRING_DATASOURCE_USERNAME: app
      SPRING_DATASOURCE_PASSWORD: ${MYSQL_PASSWORD}
      SPRING_DATA_REDIS_HOST: redis
    depends_on:
      mysql:
        condition: service_healthy
      redis:
        condition: service_started

  mysql:
    image: mysql:8.4
    environment:
      MYSQL_DATABASE: appdb
      MYSQL_USER: app
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
    volumes:
      - mysql_data:/var/lib/mysql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 10

  redis:
    image: redis:7.4

volumes:
  mysql_data:
```

실행:

```bash
docker compose config
docker compose up -d
docker compose logs -f
docker compose down
```

---

### [주의]

Docker Compose는 여러 Container를 쉽게 실행하지만 운영 Orchestration 전체를 대체하지는 않는다.

주의할 점:

- `depends_on`은 Application Ready를 완전히 보장하지 않는다.
- Database 연결은 Health Check 또는 Retry Logic이 필요하다.
- Secret을 Compose 파일에 하드코딩하면 안 된다.
- Named Volume 삭제 여부를 주의해야 한다.
- Host Port 충돌을 확인해야 한다.
- 개발용 Bind Mount와 운영용 Image 실행 방식을 구분해야 한다.
- Compose는 Kubernetes와 목적이 다르다.
- 운영 배포에서는 `docker compose config`로 최종 설정을 검증한다.

---

### [FAQ]

Q. Docker Compose란?
A. 여러 Docker Container를 하나의 YAML 파일로 정의하고 실행하는 Multi Container Management Tool이다.

Q. Docker Compose는 언제 사용하는가?
A. Spring Boot, MySQL, Redis, Nginx처럼 여러 Container를 함께 실행해야 할 때 사용한다.

Q. Docker Compose v2 명령어는 무엇인가?
A. `docker compose up`, `docker compose down`, `docker compose logs`처럼 공백이 있는 명령어를 사용한다.

Q. docker run과 docker compose 차이는?
A. `docker run`은 단일 Container 실행에 적합하고, Docker Compose는 여러 Service를 함께 정의하고 실행하는 데 적합하다.

---

# 2. Compose File Structure

## 2.1 compose.yml Structure

### [개념]

Compose File은 Docker Compose가 실행할 Service, Network, Volume, Config를 선언하는 YAML 파일이다.

기본 파일명은 `compose.yml` 또는 `docker-compose.yml`이다.

```text
compose.yml
→ services
→ networks
→ volumes
→ docker compose up
```

---

### [핵심]

기본 구조:

```yaml
services:
  app:
    image: myapp:1.0
    ports:
      - "8080:8080"

networks:
  app_network:

volumes:
  app_data:
```

Compose 주요 Top-level Key:

| Top-level Key | Meaning                      |
| ------------- | ---------------------------- |
| services      | Container Service 정의       |
| networks      | Service 간 통신 Network 정의 |
| volumes       | Persistent Storage 정의      |
| configs       | Config 파일 정의             |
| secrets       | Secret 정의                  |

Service 주요 Key:

| Service Key    | Meaning                       |
| -------------- | ----------------------------- |
| image          | 사용할 Image                  |
| build          | Build Context / Dockerfile    |
| container_name | Container 이름                |
| ports          | Host ↔ Container Port Mapping |
| expose         | Compose 내부 Port 노출        |
| environment    | 환경변수                      |
| env_file       | 환경변수 파일                 |
| volumes        | Volume Mount                  |
| networks       | 연결 Network                  |
| depends_on     | Service 의존 관계             |
| command        | Default Command Override      |
| entrypoint     | Entrypoint Override           |
| restart        | Restart Policy                |
| healthcheck    | Health Check                  |
| logging        | Log Driver 설정               |

---

### [실무]

권장 프로젝트 구조:

```text
project-root
├─ backend
│  ├─ Dockerfile
│  └─ build.gradle
├─ frontend
│  ├─ Dockerfile
│  └─ package.json
├─ compose.yml
├─ .env
└─ .env.example
```

Compose 파일 예시:

```yaml
services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "${BACKEND_PORT}:8080"
    env_file:
      - .env
    networks:
      - app_network

  frontend:
    build:
      context: ./frontend
    ports:
      - "${FRONTEND_PORT}:80"
    networks:
      - app_network

networks:
  app_network:
```

`.env` 예시:

```env
BACKEND_PORT=8080
FRONTEND_PORT=3000
```

`.env.example` 예시:

```env
BACKEND_PORT=
FRONTEND_PORT=
MYSQL_PASSWORD=
JWT_SECRET=
```

---

### [주의]

YAML 들여쓰기가 잘못되면 Compose 파일이 정상 동작하지 않는다.

주의할 점:

- Tab 대신 Space 사용
- Key 들여쓰기 일관성 유지
- 문자열 Port Mapping은 따옴표 권장
- `.env` 파일을 Git에 올리지 않기
- Secret 값을 Compose 파일에 직접 작성하지 않기
- `container_name` 남용 주의
- Compose 파일과 Dockerfile Context 경로 구분
- `docker compose config`로 병합 결과 확인

---

### [FAQ]

Q. Compose 파일 기본 이름은?
A. `compose.yml` 또는 `docker-compose.yml`을 사용한다.

Q. Compose 파일에서 가장 중요한 Top-level Key는?
A. `services`, `networks`, `volumes`가 가장 중요하다.

Q. Compose 파일은 JSON인가?
A. 아니다. YAML 형식이다.

Q. Compose 파일에서 들여쓰기가 중요한가?
A. 중요하다. YAML은 들여쓰기 기반 형식이므로 들여쓰기 오류가 설정 오류로 이어진다.

---

# 3. Services

## 3.1 services Definition

### [개념]

`services`는 Docker Compose에서 실행할 Container 단위를 정의하는 영역이다.

각 Service는 하나의 Container 또는 Scale된 Container 집합으로 실행된다.

```yaml
services:
  app:
    image: myapp:1.0
```

Service 이름은 Compose Network 내부에서 DNS 이름으로 사용된다.

---

### [핵심]

`services` 핵심:

- Multi Container 구성의 중심
- Service 이름은 내부 Hostname 역할
- 각 Service는 Image 또는 Build 설정 필요
- Service별 Port, Env, Volume, Network 설정 가능
- Service 간 통신은 Service Name으로 수행
- Service Name은 Application Config와 연결됨

예시:

```yaml
services:
  app:
    image: spring-app:1.0

  mysql:
    image: mysql:8.4

  redis:
    image: redis:7.4
```

Compose 내부 통신:

```text
app → mysql:3306
app → redis:6379
```

---

### [실무]

Spring Boot에서 MySQL Service 연결:

```yaml
services:
  app:
    image: spring-app:1.0
    environment:
      SPRING_DATASOURCE_URL: jdbc:mysql://mysql:3306/appdb
      SPRING_DATA_REDIS_HOST: redis

  mysql:
    image: mysql:8.4

  redis:
    image: redis:7.4
```

Application 설정:

```properties
spring.datasource.url=jdbc:mysql://mysql:3306/appdb
spring.data.redis.host=redis
```

Service Name 기반 DNS가 가능하므로 `localhost`가 아니라 `mysql`, `redis`를 사용해야 한다.

---

### [주의]

Container 내부에서 `localhost`는 Host PC가 아니라 자기 자신을 의미한다.

잘못된 설정:

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/appdb
```

Compose 내부 권장 설정:

```properties
spring.datasource.url=jdbc:mysql://mysql:3306/appdb
```

주의할 점:

- Service Name과 Container Name 혼동 금지
- 내부 통신은 Host Port가 아니라 Container Port 사용
- `localhost` 오해 주의
- Service 이름 변경 시 Application Config도 변경 필요
- Service 이름은 검색 친화적이고 명확하게 작성
- DB와 Cache는 필요한 Service와 같은 Network에 연결

---

### [FAQ]

Q. Docker Compose Service란?
A. Compose에서 실행할 Container 단위를 정의한 것이다.

Q. Service 이름은 어디에 사용되는가?
A. Compose Network 내부에서 DNS Hostname으로 사용된다.

Q. Compose 내부에서 DB Host를 localhost로 쓰면 되는가?
A. 아니다. Application Container에서 `localhost`는 자기 자신이므로 DB Service 이름을 사용해야 한다.

Q. app Container에서 mysql Container에 접속하려면 Host는 무엇인가?
A. Service 이름인 `mysql`을 Host로 사용한다.

---

# 4. image and build

## 4.1 image

### [개념]

`image`는 Service가 사용할 Docker Image를 지정하는 Compose 설정이다.

```yaml
services:
  redis:
    image: redis:7.4
```

`image`는 이미 존재하는 Image를 Pull하거나 Local Image를 사용한다.

---

### [핵심]

`image` 핵심:

- Service Runtime Image 지정
- Docker Hub 또는 Private Registry Image 사용 가능
- Version Tag 명시 권장
- `latest` 단독 사용 지양
- `build` 없이 빠른 실행 가능
- 배포 추적과 Rollback에 중요

예시:

```yaml
services:
  nginx:
    image: nginx:1.27

  mysql:
    image: mysql:8.4

  redis:
    image: redis:7.4

  app:
    image: registry.example.com/app:1.0.0
```

---

### [실무]

운영 또는 테스트에서 Registry Image 사용:

```yaml
services:
  app:
    image: registry.example.com/festapick-api:1.0.0
    ports:
      - "8080:8080"
```

Infrastructure Service는 공식 Image를 자주 사용한다.

```yaml
services:
  mysql:
    image: mysql:8.4

  redis:
    image: redis:7.4

  nginx:
    image: nginx:1.27
```

운영 배포는 `image` 기반 실행이 명확하다.

```text
CI Build
→ Registry Push
→ Server Compose image Pull
→ Container Recreate
```

---

### [주의]

운영에서 `latest`만 사용하면 배포 추적과 Rollback이 어렵다.

비권장:

```yaml
services:
  app:
    image: myapp:latest
```

권장:

```yaml
services:
  app:
    image: myapp:1.0.0
```

주의할 점:

- Image Tag 명확히 지정
- Public Image 신뢰성 확인
- Private Registry 인증 설정
- Architecture 호환성 확인
- Image Vulnerability Scan 고려
- Rollback용 이전 Image 유지

---

### [FAQ]

Q. Compose의 image는 무엇인가?
A. Service가 사용할 Docker Image를 지정하는 설정이다.

Q. image에 latest를 써도 되는가?
A. 개발용은 가능하지만 운영에서는 명확한 Version Tag 사용을 권장한다.

Q. image는 항상 Docker Hub에서 받는가?
A. 아니다. Local Image, Docker Hub, Private Registry Image를 사용할 수 있다.

---

## 4.2 build

### [개념]

`build`는 Dockerfile을 사용하여 Service Image를 Build하는 Compose 설정이다.

```yaml
services:
  app:
    build: .
```

`build`는 Application Source Code를 Image로 만들 때 사용한다.

---

### [핵심]

`build` 핵심:

- Dockerfile 기반 Image Build
- Build Context 지정
- Dockerfile 경로 지정 가능
- Build Argument 전달 가능
- Local Development에 유용
- CI/CD Build에도 사용 가능
- `.dockerignore`와 함께 사용

기본 예시:

```yaml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
```

Build Argument 예시:

```yaml
services:
  app:
    build:
      context: .
      args:
        APP_VERSION: 1.0.0
```

---

### [실무]

Backend와 Frontend를 각각 Build:

```yaml
services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    image: festapick-backend:local

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    image: festapick-frontend:local
```

실행:

```bash
docker compose build
docker compose up -d
```

Build와 실행을 함께 수행:

```bash
docker compose up -d --build
```

---

### [주의]

`build.context`는 Dockerfile의 `COPY` 기준 범위를 결정한다.

주의할 점:

- Context가 너무 크면 Build가 느려진다.
- Dockerfile 위치와 Context 위치를 구분해야 한다.
- `.dockerignore`를 작성해야 한다.
- Secret 파일이 Context에 포함되지 않도록 해야 한다.
- Build Artifact 경로가 Context 안에 있어야 한다.
- `build`와 `image`를 함께 쓰면 Build 결과 Image 이름을 지정할 수 있다.
- Build ARG에 Secret을 넣지 않는다.

---

### [FAQ]

Q. Compose의 build는 무엇인가?
A. Dockerfile을 기반으로 Service Image를 Build하는 설정이다.

Q. image와 build의 차이는?
A. `image`는 기존 Image를 사용하고, `build`는 Dockerfile로 Image를 생성한다.

Q. build context란?
A. Docker Build가 접근할 수 있는 파일 범위이며 Dockerfile의 COPY 기준이 된다.

Q. docker compose up --build는 무엇인가?
A. Service Image를 다시 Build한 뒤 Container를 실행하는 명령이다.

---

# 5. ports and expose

## 5.1 ports

### [개념]

`ports`는 Host Port와 Container Port를 연결하는 Compose 설정이다.

```yaml
ports:
  - "8080:8080"
```

형식:

```text
HOST_PORT:CONTAINER_PORT
```

---

### [핵심]

`ports` 핵심:

- 외부에서 Container 접근 가능
- Host Port와 Container Port Mapping
- Host Port 충돌 가능
- 개발 환경에서 API / Web 접근에 필수
- 내부 Service 간 통신에는 보통 필요 없음
- 운영에서는 공개 Port 최소화 필요

예시:

```yaml
services:
  app:
    ports:
      - "8080:8080"

  nginx:
    ports:
      - "80:80"

  mysql:
    ports:
      - "3306:3306"
```

---

### [실무]

Spring Boot API 외부 접근:

```yaml
services:
  app:
    ports:
      - "8080:8080"
```

React 또는 Nginx 외부 접근:

```yaml
services:
  frontend:
    ports:
      - "3000:80"
```

MySQL을 Host Tool에서 접근해야 할 때:

```yaml
services:
  mysql:
    ports:
      - "3307:3306"
```

Host에서 접속:

```text
localhost:3307 → mysql container:3306
```

---

### [주의]

Compose 내부 Service 간 통신은 `ports` 없이도 가능하다.

불필요한 Port 공개는 보안 위험이다.

주의할 점:

- Host Port 충돌 확인
- 운영 DB Port 외부 공개 지양
- 내부 통신은 Container Port 사용
- Port 문자열은 따옴표 사용 권장
- 방화벽 / Cloud Security Group 확인
- `8080:8080`에서 왼쪽은 Host Port, 오른쪽은 Container Port

---

### [FAQ]

Q. ports는 무엇인가?
A. Host Port와 Container Port를 연결하여 외부에서 Container에 접근할 수 있게 하는 설정이다.

Q. ports 형식에서 왼쪽과 오른쪽은 무엇인가?
A. 왼쪽은 Host Port이고 오른쪽은 Container Port이다.

Q. Compose 내부 통신에도 ports가 필요한가?
A. 아니다. 같은 Network의 Service끼리는 Service Name과 Container Port로 통신할 수 있다.

Q. DB Port를 운영에서 외부 공개해도 되는가?
A. 권장하지 않는다. Application 내부 Network에서만 접근하도록 제한하는 것이 안전하다.

---

## 5.2 expose

### [개념]

`expose`는 Host에 Port를 공개하지 않고 Compose Network 내부에만 Port를 노출하는 설정이다.

```yaml
expose:
  - "8080"
```

`expose`는 내부 통신 목적이며 Host Port Mapping을 수행하지 않는다.

---

### [핵심]

`expose` 핵심:

- Compose 내부 Network에 Port 노출
- Host 외부 접근 불가
- 문서화 성격 강함
- `ports`와 다름
- 내부 Service 간 통신에 사용 가능
- Reverse Proxy 구조에서 유용

비교:

| Setting | Host Access | Internal Access |
| ------- | ----------- | --------------- |
| ports   | 가능        | 가능            |
| expose  | 불가        | 가능            |

---

### [실무]

Nginx가 App을 Reverse Proxy하고 App은 Host에 직접 공개하지 않는 구조:

```yaml
services:
  nginx:
    image: nginx:1.27
    ports:
      - "80:80"

  app:
    image: spring-app:1.0
    expose:
      - "8080"
```

통신 흐름:

```text
User
→ Host:80
→ nginx:80
→ app:8080
```

---

### [주의]

`expose`만 설정하면 Host에서 접근할 수 없다.

주의할 점:

- 외부 접근이 필요하면 `ports` 사용
- 내부 통신은 Service Name + Container Port 사용
- expose는 보안 경계가 아니라 문서화 / 내부 노출 설정
- Reverse Proxy 구조에서 Port 공개 범위 확인

---

### [FAQ]

Q. expose는 무엇인가?
A. Host에는 공개하지 않고 Compose 내부 Network에만 Port를 노출하는 설정이다.

Q. expose와 ports 차이는?
A. ports는 Host Port와 연결하고 expose는 내부 Network에만 노출한다.

Q. 외부에서 접속하려면 expose만으로 충분한가?
A. 아니다. 외부 접속에는 ports 설정이 필요하다.

---

# 6. Environment Variables

## 6.1 environment

### [개념]

`environment`는 Compose Service에 Runtime Environment Variable을 주입하는 설정이다.

```yaml
environment:
  SPRING_PROFILES_ACTIVE: prod
```

Application은 주입된 환경변수를 Runtime Config로 사용한다.

---

### [핵심]

`environment` 핵심:

- Runtime 환경변수 주입
- Spring Profile 설정
- DB URL 설정
- Redis Host 설정
- 외부 API Endpoint 설정
- Dockerfile ENV Override 가능
- Secret 하드코딩 주의

예시:

```yaml
services:
  app:
    environment:
      SPRING_PROFILES_ACTIVE: local
      SERVER_PORT: 8080
      SPRING_DATASOURCE_URL: jdbc:mysql://mysql:3306/appdb
```

---

### [실무]

Spring Boot Compose 환경변수:

```yaml
services:
  app:
    image: spring-app:1.0
    environment:
      SPRING_PROFILES_ACTIVE: prod
      SPRING_DATASOURCE_URL: jdbc:mysql://mysql:3306/appdb
      SPRING_DATASOURCE_USERNAME: app
      SPRING_DATASOURCE_PASSWORD: ${DB_PASSWORD}
      SPRING_DATA_REDIS_HOST: redis
```

`.env`:

```env
DB_PASSWORD=change-me
```

Spring Boot Relaxed Binding으로 환경변수는 설정 Property에 매핑된다.

```text
SPRING_DATASOURCE_URL
→ spring.datasource.url
```

---

### [주의]

Compose 파일에 Secret을 직접 쓰면 안 된다.

비권장:

```yaml
environment:
  SPRING_DATASOURCE_PASSWORD: real-production-password
```

권장:

```yaml
environment:
  SPRING_DATASOURCE_PASSWORD: ${DB_PASSWORD}
```

주의할 점:

- `.env` 파일 Git Commit 금지
- Secret Manager 사용 고려
- 환경변수 누락 시 Application 실행 실패 가능
- 변수명 오타 확인
- Compose 변수 치환과 Container 내부 환경변수 구분
- `docker compose config`로 최종 값 확인

---

### [FAQ]

Q. environment는 무엇인가?
A. Compose Service에 Runtime Environment Variable을 주입하는 설정이다.

Q. Spring Boot Profile은 Compose에서 어떻게 주입하는가?
A. `SPRING_PROFILES_ACTIVE` 환경변수로 주입한다.

Q. Compose 파일에 DB Password를 직접 써도 되는가?
A. 권장하지 않는다. `.env`, Secret Manager, CI/CD Secret을 사용해야 한다.

---

## 6.2 env_file

### [개념]

`env_file`은 Environment Variable을 별도 파일에서 읽어 Compose Service에 주입하는 설정이다.

```yaml
env_file:
  - .env
```

`env_file`은 환경변수가 많을 때 Compose 파일을 단순하게 유지한다.

---

### [핵심]

`env_file` 핵심:

- 환경변수 파일 로드
- Compose 파일 간결화
- 환경별 설정 분리
- Runtime Config 관리
- Secret 관리 주의
- Service별 Env 파일 분리 가능

예시:

```yaml
services:
  app:
    env_file:
      - .env.local
```

`.env.local`:

```env
SPRING_PROFILES_ACTIVE=local
SPRING_DATASOURCE_URL=jdbc:mysql://mysql:3306/appdb
SPRING_DATASOURCE_USERNAME=app
SPRING_DATASOURCE_PASSWORD=apppass
```

---

### [실무]

환경별 파일 분리:

```text
.env.local
.env.dev
.env.prod
.env.example
```

Compose Override 사용:

```bash
docker compose --env-file .env.local up -d
```

Service env_file 사용:

```yaml
services:
  app:
    image: spring-app:1.0
    env_file:
      - .env.local
```

개발 환경에서는 `.env.local`을 사용하고 운영 환경에서는 CI/CD Secret 또는 서버 환경변수 사용을 권장한다.

---

### [주의]

Compose의 `.env` 변수 치환과 `env_file`은 역할이 다르다.

구분:

| Type         | Purpose                       |
| ------------ | ----------------------------- |
| `.env`       | Compose 파일 변수 치환        |
| `env_file`   | Container 환경변수 주입       |
| `--env-file` | Compose 변수 치환용 파일 지정 |

주의할 점:

- `env_file`에 Secret 저장 시 Git 제외 필수
- 파일 경로는 Compose 파일 기준
- 환경변수 이름 오타 확인
- 운영에서는 Secret Manager 우선 고려
- `.env.example`로 필요한 변수 목록 제공 권장
- `docker compose config`로 치환 결과 확인

---

### [FAQ]

Q. env_file은 무엇인가?
A. 별도 파일에 정의된 환경변수를 Service Container에 주입하는 Compose 설정이다.

Q. env_file과 environment 차이는?
A. `environment`는 Compose 파일에 직접 변수 값을 쓰고, `env_file`은 파일에서 환경변수를 읽어 주입한다.

Q. .env와 env_file은 같은가?
A. 완전히 같지 않다. `.env`는 Compose 변수 치환에도 사용되고, `env_file`은 Container 환경변수 주입에 사용된다.

---

# 7. Volumes

## 7.1 volumes

### [개념]

`volumes`는 Container 데이터 영속성 또는 Host-Container 파일 공유를 설정하는 Compose 기능이다.

Container Writable Layer는 삭제될 수 있으므로 Database, Upload File, Persistent Data는 Volume에 저장해야 한다.

```yaml
volumes:
  mysql_data:
```

---

### [핵심]

Volume 유형:

| Type             | Meaning                           |
| ---------------- | --------------------------------- |
| Named Volume     | Docker가 관리하는 영속 저장소     |
| Bind Mount       | Host 경로를 Container에 직접 연결 |
| Anonymous Volume | 이름 없는 임시성 Volume           |

Named Volume 예시:

```yaml
services:
  mysql:
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```

Bind Mount 예시:

```yaml
services:
  app:
    volumes:
      - ./logs:/app/logs
```

---

### [실무]

MySQL 데이터 영속성:

```yaml
services:
  mysql:
    image: mysql:8.4
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```

Redis 데이터 영속성:

```yaml
services:
  redis:
    image: redis:7.4
    volumes:
      - redis_data:/data

volumes:
  redis_data:
```

개발 환경 Source Bind Mount:

```yaml
services:
  app:
    volumes:
      - ./src:/app/src
```

운영 Application은 Source Bind Mount보다 Image 기반 실행을 권장한다.

---

### [주의]

`docker compose down -v`는 Named Volume도 삭제한다.

주의 명령:

```bash
docker compose down -v
```

주의할 점:

- DB 데이터 Volume 삭제 주의
- Upload File은 Volume 또는 외부 Storage에 저장
- Host Bind Mount 권한 문제 확인
- Windows / Linux 경로 차이 주의
- 운영에서는 Named Volume 또는 외부 Storage 사용
- Container 내부 Log File 저장보다 stdout 로그 권장
- Non-root User 사용 시 Volume 권한 확인

---

### [FAQ]

Q. Compose Volume은 무엇인가?
A. Container 데이터 영속성 또는 Host-Container 파일 공유를 위한 저장소 설정이다.

Q. MySQL Container에 Volume이 필요한 이유는?
A. Container 삭제 후에도 Database 데이터를 유지하기 위해 필요하다.

Q. docker compose down -v는 무엇을 하는가?
A. Container와 Network뿐 아니라 Named Volume도 함께 삭제할 수 있으므로 데이터 손실에 주의해야 한다.

Q. Named Volume과 Bind Mount 차이는?
A. Named Volume은 Docker가 관리하는 저장소이고 Bind Mount는 Host 경로를 Container에 직접 연결한다.

---

# 8. Networks

## 8.1 networks

### [개념]

`networks`는 Docker Compose Service 간 통신을 위한 Container Network를 정의하는 설정이다.

Compose는 기본적으로 Project 단위의 Default Network를 자동 생성한다.

```text
app service
→ compose network
→ mysql service
```

---

### [핵심]

Network 핵심:

- Service 간 통신 제공
- Service Name 기반 DNS 제공
- Project별 Default Network 자동 생성
- Custom Network 정의 가능
- 외부 공개 없이 내부 통신 가능
- Frontend / Backend / DB Network 분리 가능
- Service 접근 범위 제어 가능

기본 예시:

```yaml
services:
  app:
    networks:
      - backend_network

  mysql:
    networks:
      - backend_network

networks:
  backend_network:
```

---

### [실무]

Frontend, Backend, DB Network 분리:

```yaml
services:
  nginx:
    image: nginx:1.27
    ports:
      - "80:80"
    networks:
      - frontend_network

  app:
    image: spring-app:1.0
    networks:
      - frontend_network
      - backend_network

  mysql:
    image: mysql:8.4
    networks:
      - backend_network

networks:
  frontend_network:
  backend_network:
```

통신 구조:

```text
User
→ nginx
→ app
→ mysql

mysql은 nginx와 직접 통신하지 않음
```

---

### [주의]

Network 분리 없이 모든 Service를 하나의 Network에 두면 단순하지만 보안 경계가 약해진다.

주의할 점:

- Service Name 기반 통신 사용
- 내부 통신에는 Host Port가 아니라 Container Port 사용
- Network 이름 충돌 주의
- External Network 사용 시 사전 생성 필요
- DB는 필요한 Service와만 같은 Network에 연결
- `localhost` 오해 금지
- Network 분리 후 필요한 연결 누락 주의

---

### [FAQ]

Q. Compose Network는 무엇인가?
A. Docker Compose Service 간 통신을 제공하는 Container Network이다.

Q. Compose에서 Service끼리 어떻게 통신하는가?
A. 같은 Network에 있으면 Service Name을 Hostname으로 사용해 통신한다.

Q. Compose에서 MySQL Host는 무엇으로 설정해야 하는가?
A. MySQL Service 이름이 `mysql`이면 Host도 `mysql`로 설정한다.

Q. Network를 분리하는 이유는?
A. Service 간 접근 범위를 제한하고 구조를 명확히 하기 위해서이다.

---

# 9. depends_on and Startup Order

## 9.1 depends_on

### [개념]

`depends_on`은 Service 간 시작 순서를 정의하는 Compose 설정이다.

```yaml
depends_on:
  - mysql
```

`depends_on`은 의존 Service를 먼저 시작하지만, Application Ready 상태를 항상 보장하지는 않는다.

---

### [핵심]

`depends_on` 핵심:

- Service 시작 순서 제어
- 의존 Container 먼저 시작
- Application Ready 보장 아님
- Health Check와 함께 사용 권장
- DB 연결 Retry Logic 필요
- Startup Order와 Readiness는 다름

기본 예시:

```yaml
services:
  app:
    depends_on:
      - mysql

  mysql:
    image: mysql:8.4
```

Health Condition 예시:

```yaml
services:
  app:
    depends_on:
      mysql:
        condition: service_healthy
```

---

### [실무]

MySQL Health Check와 depends_on 조합:

```yaml
services:
  app:
    image: spring-app:1.0
    depends_on:
      mysql:
        condition: service_healthy
    environment:
      SPRING_DATASOURCE_URL: jdbc:mysql://mysql:3306/appdb

  mysql:
    image: mysql:8.4
    environment:
      MYSQL_DATABASE: appdb
      MYSQL_ROOT_PASSWORD: rootpass
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 10
```

Spring Boot에서도 DB 연결 실패에 대비해 Connection Pool Retry, Application Retry, Migration Timing을 고려해야 한다.

---

### [주의]

`depends_on`만 믿으면 DB Ready 이전에 App이 시작되어 Connection Failed가 발생할 수 있다.

대표 오류:

```text
Communications link failure
Connection refused
UnknownHostException
Access denied for user
```

해결 방향:

- DB Health Check 추가
- `condition: service_healthy` 사용
- Spring Boot DB Connection Retry 확인
- Flyway / Liquibase 실행 시점 확인
- Application Startup Delay보다 Health 기반 제어 권장

---

### [FAQ]

Q. depends_on은 무엇인가?
A. Service 간 시작 순서를 정의하는 Compose 설정이다.

Q. depends_on은 DB가 준비될 때까지 기다리는가?
A. 기본적으로는 Container 시작 순서만 제어한다. DB Ready 보장은 Health Check와 condition 설정이 필요하다.

Q. DB 연결 실패가 발생하면 무엇을 확인해야 하는가?
A. Service Name, Network, DB Health Check, Port, Username, Password, Database 이름을 확인해야 한다.

---

# 10. healthcheck

## 10.1 Compose Healthcheck

### [개념]

Compose `healthcheck`는 Service Container의 상태를 확인하는 설정이다.

Dockerfile `HEALTHCHECK`와 유사하지만 Compose 파일에서 Service별로 정의할 수 있다.

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8080/actuator/health"]
```

---

### [핵심]

Health Check 핵심:

- Container Health 상태 판단
- `healthy`, `unhealthy`, `starting` 상태 제공
- depends_on condition과 연계 가능
- DB / API / Cache 준비 상태 확인
- 장애 분석에 도움
- Running과 Healthy 구분

주요 옵션:

| Option       | Meaning           |
| ------------ | ----------------- |
| test         | Health Check 명령 |
| interval     | 실행 간격         |
| timeout      | 응답 제한 시간    |
| retries      | 실패 허용 횟수    |
| start_period | 초기 대기 시간    |

---

### [실무]

Spring Boot Actuator Health Check:

```yaml
services:
  app:
    image: spring-app:1.0
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

Redis Health Check:

```yaml
services:
  redis:
    image: redis:7.4
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 5
```

---

### [주의]

Health Check 명령에 필요한 CLI 도구가 Image 내부에 있어야 한다.

자주 발생하는 문제:

| Problem          | Cause                  | Solution                  |
| ---------------- | ---------------------- | ------------------------- |
| curl not found   | Image에 curl 없음      | wget 사용 또는 curl 설치  |
| unhealthy        | Health URL 오류        | Endpoint 확인             |
| timeout          | Startup 느림           | start_period 증가         |
| DB unhealthy     | 인증/권한 문제         | Health Command 수정       |
| Actuator 404     | Dependency / 설정 누락 | Actuator 설정 확인        |
| 401 Unauthorized | Security 설정          | Health Endpoint 공개 설정 |

주의할 점:

- 너무 짧은 interval은 부하 발생
- Health Endpoint 보안 설정 확인
- Application Context Path 확인
- DB Health Check는 인증 조건 고려
- Health Check 실패 원인은 `docker inspect`로 확인
- Container 내부 기준으로 URL을 작성

---

### [FAQ]

Q. Compose healthcheck는 무엇인가?
A. Service Container의 상태를 확인하여 healthy 또는 unhealthy 상태를 판단하는 설정이다.

Q. Spring Boot Health Check는 무엇을 사용하면 좋은가?
A. Spring Boot Actuator의 `/actuator/health` Endpoint를 사용한다.

Q. healthcheck가 unhealthy이면 어떻게 확인하는가?
A. `docker inspect`와 `docker compose logs`로 Health Check 실패 원인과 Application 로그를 확인한다.

---

# 11. restart Policy

## 11.1 restart

### [개념]

`restart`는 Container 종료 시 Docker가 자동으로 재시작할지 결정하는 Compose 설정이다.

```yaml
restart: unless-stopped
```

Restart Policy는 장애 복구와 서버 재부팅 후 자동 실행에 사용된다.

---

### [핵심]

Restart Policy 종류:

| Policy         | Meaning                 |
| -------------- | ----------------------- |
| no             | 자동 재시작 안 함       |
| always         | 항상 재시작             |
| on-failure     | 실패 종료 시 재시작     |
| unless-stopped | 수동 중지 전까지 재시작 |

예시:

```yaml
services:
  app:
    image: spring-app:1.0
    restart: unless-stopped
```

---

### [실무]

운영 또는 개인 서버에서는 `unless-stopped`를 자주 사용한다.

```yaml
services:
  app:
    image: festapick-api:1.0.0
    restart: unless-stopped

  mysql:
    image: mysql:8.4
    restart: unless-stopped

  redis:
    image: redis:7.4
    restart: unless-stopped
```

개발 환경에서는 Restart Loop가 디버깅을 방해할 수 있으므로 필요할 때만 사용한다.

---

### [주의]

Restart Policy는 근본 원인 해결이 아니다.

Restart Loop 예시:

```text
Container Start
→ App Crash
→ Auto Restart
→ Crash Repeat
```

확인:

```bash
docker compose ps
docker compose logs -f app
```

주의할 점:

- 잘못된 Config는 계속 재시작됨
- 로그가 빠르게 쌓일 수 있음
- 개발 중에는 restart를 끄는 것이 디버깅에 유리할 수 있음
- Health Check 실패와 Process Exit는 다름
- Restart Policy가 Application Ready를 보장하지 않음

---

### [FAQ]

Q. restart는 무엇인가?
A. Container 종료 시 자동 재시작 여부를 결정하는 Compose 설정이다.

Q. 운영에서 자주 쓰는 restart 정책은?
A. `unless-stopped`를 많이 사용한다.

Q. restart를 설정하면 장애가 해결되는가?
A. 아니다. Container를 다시 시작할 뿐이며 Config 오류나 Application Bug는 별도로 해결해야 한다.

---

# 12. command and entrypoint

## 12.1 command

### [개념]

`command`는 Image의 기본 CMD를 Compose에서 Override하는 설정이다.

```yaml
command: ["java", "-jar", "app.jar", "--spring.profiles.active=local"]
```

`command`는 Container Runtime 실행 명령 또는 인자를 변경할 때 사용한다.

---

### [핵심]

`command` 핵심:

- Dockerfile CMD Override
- Runtime 명령 변경
- 개발 환경 명령 변경
- Service별 실행 모드 변경
- ENTRYPOINT와 조합 가능
- Container Exit 원인 가능

예시:

```yaml
services:
  app:
    image: spring-app:1.0
    command: ["--spring.profiles.active=local"]
```

Dockerfile:

```dockerfile
ENTRYPOINT ["java", "-jar", "app.jar"]
```

실행 결과:

```text
java -jar app.jar --spring.profiles.active=local
```

---

### [실무]

개발용 Spring Profile Override:

```yaml
services:
  app:
    image: spring-app:1.0
    command: ["--spring.profiles.active=local"]
```

Redis 실행 옵션 지정:

```yaml
services:
  redis:
    image: redis:7.4
    command: ["redis-server", "--appendonly", "yes"]
```

MySQL 옵션 지정:

```yaml
services:
  mysql:
    image: mysql:8.4
    command:
      - "--character-set-server=utf8mb4"
      - "--collation-server=utf8mb4_unicode_ci"
```

---

### [주의]

`command`는 Dockerfile의 CMD를 Override한다.

주의할 점:

- ENTRYPOINT와 CMD 조합 이해 필요
- 잘못된 command는 Container Exit 원인
- Shell Form / Exec Form 구분
- 긴 설정은 environment 또는 config 파일로 분리 고려
- 운영에서 임의 command Override 남발 금지

---

### [FAQ]

Q. Compose command는 무엇인가?
A. Image의 기본 CMD를 Compose에서 Override하는 설정이다.

Q. command는 ENTRYPOINT도 바꾸는가?
A. 아니다. command는 주로 CMD를 Override한다. ENTRYPOINT 변경은 `entrypoint` 설정을 사용한다.

Q. command 오류는 어떻게 확인하는가?
A. `docker compose logs`와 `docker inspect`로 실제 실행 명령을 확인한다.

---

## 12.2 entrypoint

### [개념]

`entrypoint`는 Image의 기본 ENTRYPOINT를 Compose에서 Override하는 설정이다.

```yaml
entrypoint: ["sh", "/entrypoint.sh"]
```

Container 시작 명령 자체를 바꿔야 할 때 사용한다.

---

### [핵심]

`entrypoint` 핵심:

- Dockerfile ENTRYPOINT Override
- Container Main Process 변경
- Debugging에 사용 가능
- Init Script 실행에 사용 가능
- 신중히 사용 필요

Debug 예시:

```bash
docker compose run --entrypoint sh app
```

Compose 예시:

```yaml
services:
  app:
    image: spring-app:1.0
    entrypoint: ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]
```

---

### [실무]

환경변수 기반 Java Option 사용:

```yaml
services:
  app:
    image: spring-app:1.0
    environment:
      JAVA_OPTS: "-Xms256m -Xmx512m"
    entrypoint: ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]
```

일반 운영에서는 Dockerfile의 ENTRYPOINT를 유지하고 Compose에서는 environment만 바꾸는 방식이 더 명확하다.

---

### [주의]

entrypoint Override는 Image의 기본 실행 방식을 바꾸므로 장애 원인이 될 수 있다.

주의할 점:

- Main Process 유지 여부 확인
- Shell Script 실행 권한 확인
- Signal Handling 고려
- PID 1 문제 고려
- Dockerfile ENTRYPOINT와 중복 관리 지양
- Debug용 Override를 운영 Compose에 남기지 않기

---

### [FAQ]

Q. Compose entrypoint는 무엇인가?
A. Image의 기본 ENTRYPOINT를 Compose에서 Override하는 설정이다.

Q. entrypoint와 command 차이는?
A. entrypoint는 실행 명령 자체를 바꾸고 command는 기본 인자 또는 CMD를 바꾼다.

Q. 운영에서 entrypoint Override를 자주 쓰는가?
A. 권장하지 않는다. 특별한 이유가 없으면 Dockerfile ENTRYPOINT를 유지하는 것이 좋다.

---

# 13. profiles and override

## 13.1 profiles

### [개념]

`profiles`는 특정 Service를 선택적으로 실행하기 위한 Compose 설정이다.

```yaml
profiles:
  - dev
```

Profile을 사용하면 개발용 Service, 테스트용 Service, 운영 보조 Service를 분리할 수 있다.

---

### [핵심]

`profiles` 핵심:

- 선택적 Service 실행
- 개발 / 테스트 / 운영 보조 구성 분리
- 불필요한 Service 실행 방지
- Compose 파일 재사용성 향상
- 팀 개발 환경 옵션화

예시:

```yaml
services:
  app:
    image: spring-app:1.0

  adminer:
    image: adminer
    profiles:
      - dev
```

실행:

```bash
docker compose --profile dev up -d
```

---

### [실무]

개발 보조 도구 Profile:

```yaml
services:
  mysql:
    image: mysql:8.4

  redis:
    image: redis:7.4

  adminer:
    image: adminer
    ports:
      - "8081:8080"
    profiles:
      - dev

  redisinsight:
    image: redis/redisinsight:latest
    ports:
      - "5540:5540"
    profiles:
      - dev
```

기본 실행:

```bash
docker compose up -d
```

개발 도구 포함 실행:

```bash
docker compose --profile dev up -d
```

---

### [주의]

Profile Service가 실행되지 않아 의존 Service가 누락될 수 있다.

주의할 점:

- 필수 Service에는 profiles를 설정하지 않기
- Profile 이름 명확히 관리
- 팀원에게 실행 명령 공유
- CI에서 필요한 Profile 명시
- Profile Service Port 충돌 확인

---

### [FAQ]

Q. Compose profiles는 무엇인가?
A. 특정 Service를 선택적으로 실행하기 위한 Compose 설정이다.

Q. profiles는 언제 사용하는가?
A. Adminer, RedisInsight, Mock Server 같은 개발용 보조 Service를 선택적으로 실행할 때 사용한다.

Q. profile Service는 기본 실행에 포함되는가?
A. 아니다. `--profile` 옵션으로 지정해야 실행된다.

---

## 13.2 compose override

### [개념]

Compose Override는 기본 Compose 파일에 환경별 설정 파일을 추가로 적용하는 방식이다.

```text
compose.yml
+ compose.override.yml
+ compose.prod.yml
```

Override를 사용하면 개발, 테스트, 운영 설정을 분리할 수 있다.

---

### [핵심]

Override 핵심:

- 환경별 설정 분리
- 기본 Compose 재사용
- 개발용 Bind Mount 분리
- 운영용 Image Tag 분리
- Local Port 설정 분리
- 최종 Config 검증 필요

명령어:

```bash
docker compose -f compose.yml -f compose.prod.yml up -d
```

---

### [실무]

기본 Compose:

```yaml
services:
  app:
    image: festapick-api:1.0.0
    networks:
      - app_network

networks:
  app_network:
```

개발 Override:

```yaml
services:
  app:
    build:
      context: ./backend
    ports:
      - "8080:8080"
    environment:
      SPRING_PROFILES_ACTIVE: local
```

운영 Override:

```yaml
services:
  app:
    image: registry.example.com/festapick-api:1.0.0
    restart: unless-stopped
    environment:
      SPRING_PROFILES_ACTIVE: prod
```

실행:

```bash
docker compose -f compose.yml -f compose.prod.yml up -d
```

---

### [주의]

Override 파일이 많아지면 실제 적용 설정 파악이 어려워진다.

확인 명령:

```bash
docker compose -f compose.yml -f compose.prod.yml config
```

주의할 점:

- 실제 병합 결과 확인
- 환경별 파일 Naming Convention 유지
- Secret 파일 분리
- 팀원 실행 명령 문서화
- 운영에서 개발 Override 적용하지 않기

---

### [FAQ]

Q. Compose Override란?
A. 기본 Compose 파일에 추가 Compose 파일을 병합하여 환경별 설정을 적용하는 방식이다.

Q. Override 결과는 어떻게 확인하는가?
A. `docker compose config` 명령으로 최종 병합된 설정을 확인한다.

Q. 개발 설정과 운영 설정을 하나의 Compose에 모두 넣어도 되는가?
A. 가능하지만 권장하지 않는다. Override 또는 Profile로 분리하는 것이 유지보수에 좋다.

---

# 14. Logging

## 14.1 Compose Logs

### [개념]

Docker Compose Logging은 Service Container의 stdout / stderr 로그를 조회하고 추적하는 기능이다.

```bash
docker compose logs -f
```

Docker는 Application 로그를 Container 표준 출력으로 수집한다.

---

### [핵심]

주요 명령어:

```bash
docker compose logs
docker compose logs -f
docker compose logs app
docker compose logs -f app
docker compose logs --tail=100 app
```

Logging 핵심:

- Service별 로그 확인
- Multi Container 로그 통합 확인
- stdout / stderr 기반
- 장애 분석 1차 도구
- Restart Loop 확인 가능
- Health Check 실패 원인 확인 가능

---

### [실무]

전체 로그 확인:

```bash
docker compose logs -f
```

App Service 로그만 확인:

```bash
docker compose logs -f app
```

최근 100줄 확인:

```bash
docker compose logs --tail=100 app
```

Spring Boot는 File Log보다 Console Log 중심 구성이 Container 환경에 적합하다.

```properties
logging.file.name=
```

권장 로그 흐름:

```text
Application stdout/stderr
→ Docker Logs
→ Log Driver
→ Centralized Logging System
```

---

### [주의]

Container 내부 파일 로그만 사용하면 로그 수집과 장애 분석이 어려워진다.

주의할 점:

- stdout / stderr 출력 권장
- 민감 정보 로그 출력 금지
- 로그 Rotation 설정 고려
- Restart Loop 시 로그 폭증 주의
- 운영에서는 중앙 로그 시스템 연계 고려
- Docker 로그 파일 용량 관리 필요

Logging 옵션 예시:

```yaml
services:
  app:
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
```

---

### [FAQ]

Q. docker compose logs는 무엇인가?
A. Compose Service Container의 stdout / stderr 로그를 조회하는 명령이다.

Q. 특정 Service 로그만 보려면?
A. `docker compose logs -f app`처럼 Service 이름을 지정한다.

Q. Container 환경에서 파일 로그와 Console 로그 중 무엇이 권장되는가?
A. Console 로그가 권장된다. Docker가 stdout / stderr를 수집하기 때문이다.

---

# 15. Resource Limits

## 15.1 Compose Resource Control

### [개념]

Resource Limit은 Container가 사용할 CPU와 Memory 자원을 제한하는 설정이다.

Docker Compose에서는 Container 리소스 사용량을 제어하여 OOM, Host 자원 고갈, Service 간 간섭을 줄인다.

```yaml
mem_limit: 512m
cpus: 1.0
```

---

### [핵심]

Resource Limit 핵심:

- Memory 사용량 제한
- CPU 사용량 제한
- OOM 방지
- Service 간 자원 격리
- Host 안정성 확보
- JVM Memory 설정과 함께 고려
- 성능 향상보다 장애 확산 방지가 목적

예시:

```yaml
services:
  app:
    image: spring-app:1.0
    mem_limit: 1g
    cpus: 1.0
```

---

### [실무]

Spring Boot Resource 설정:

```yaml
services:
  app:
    image: spring-app:1.0
    mem_limit: 1g
    cpus: 1.0
    environment:
      JAVA_OPTS: "-Xms256m -Xmx768m"
```

MySQL Resource 설정:

```yaml
services:
  mysql:
    image: mysql:8.4
    mem_limit: 1g
    cpus: 1.0
```

JVM Container 환경에서는 Memory Limit과 Heap Size를 함께 고려해야 한다.

```text
Container Memory Limit
→ JVM Heap
→ Metaspace
→ Native Memory
→ Thread Stack
```

---

### [주의]

Memory Limit보다 JVM Heap을 너무 크게 잡으면 OOM이 발생할 수 있다.

주의할 점:

- `-Xmx`는 Container Memory보다 작게 설정
- MySQL / Redis Memory 사용량 별도 고려
- Host 전체 Memory 확인
- OOM 발생 시 `docker compose logs`와 `docker inspect` 확인
- Resource Limit만으로 성능 문제가 해결되지는 않음
- `docker stats`로 실제 사용량 확인

---

### [FAQ]

Q. Compose에서 Memory Limit은 왜 필요한가?
A. Container가 Host Memory를 과도하게 사용하여 OOM이나 전체 서비스 장애를 일으키는 것을 막기 위해 필요하다.

Q. Spring Boot Container에서 JVM Heap은 어떻게 설정해야 하는가?
A. Container Memory Limit보다 작게 설정하고 Native Memory와 Thread Stack 여유를 남겨야 한다.

Q. Resource Limit을 설정하면 성능이 좋아지는가?
A. 성능 향상 목적보다 자원 격리와 장애 확산 방지가 주 목적이다.

---

# 16. Spring Boot Compose Pattern

## 16.1 Spring Boot + MySQL + Redis

### [개념]

Spring Boot Compose Pattern은 Backend Application과 Infrastructure Service를 하나의 Compose 파일로 실행하는 구조이다.

```text
Spring Boot App
→ MySQL
→ Redis
```

개발 환경에서 Backend 실행과 DB / Cache 준비를 자동화한다.

---

### [핵심]

필수 구성:

- app Service
- mysql Service
- redis Service
- App Environment Variable
- MySQL Named Volume
- Compose Network
- Health Check
- depends_on
- Restart Policy
- Logs 확인 구조

---

### [실무]

Spring Boot + MySQL + Redis Compose 예시:

```yaml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    image: festapick-api:local
    ports:
      - "8080:8080"
    environment:
      SPRING_PROFILES_ACTIVE: local
      SPRING_DATASOURCE_URL: jdbc:mysql://mysql:3306/festapick
      SPRING_DATASOURCE_USERNAME: festapick
      SPRING_DATASOURCE_PASSWORD: ${MYSQL_PASSWORD}
      SPRING_DATA_REDIS_HOST: redis
      SPRING_DATA_REDIS_PORT: 6379
    depends_on:
      mysql:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - backend_network

  mysql:
    image: mysql:8.4
    environment:
      MYSQL_DATABASE: festapick
      MYSQL_USER: festapick
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
    volumes:
      - mysql_data:/var/lib/mysql
    ports:
      - "3307:3306"
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 10
    networks:
      - backend_network

  redis:
    image: redis:7.4
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 5
    networks:
      - backend_network

volumes:
  mysql_data:

networks:
  backend_network:
```

`.env`:

```env
MYSQL_PASSWORD=localpass
MYSQL_ROOT_PASSWORD=rootpass
```

---

### [주의]

개발용 Compose와 운영용 Compose는 분리하는 것이 좋다.

주의할 점:

- 운영 DB Port 외부 공개 지양
- `.env` Git Commit 금지
- DB Volume 삭제 주의
- Spring Boot에서 `localhost` 대신 `mysql`, `redis` 사용
- Health Check 없이 depends_on만 사용하지 않기
- 운영 Secret은 Secret Manager 사용 고려
- DB 초기화 Script 사용 시 재실행 조건 확인
- 개발용 Port Mapping을 운영에 그대로 사용하지 않기

---

### [FAQ]

Q. Spring Boot Compose에서 DB Host는 무엇인가?
A. MySQL Service 이름이 `mysql`이면 DB Host는 `mysql`이다.

Q. Spring Boot Compose에서 Redis Host는 무엇인가?
A. Redis Service 이름이 `redis`이면 Redis Host는 `redis`이다.

Q. 개발용 MySQL Port를 3307:3306으로 쓰는 이유는?
A. Host의 기존 MySQL 3306 Port와 충돌을 피하기 위해 Host Port를 3307로 변경할 수 있다.

Q. MySQL Volume은 왜 필요한가?
A. Container 삭제 후에도 Database 데이터를 유지하기 위해 필요하다.

---

# 17. Compose Troubleshooting

## 17.1 Common Compose Problems

### [개념]

Docker Compose Troubleshooting은 Multi Container 실행 중 발생하는 Port, Network, Volume, Environment, Health Check, Startup Order 문제를 분석하는 과정이다.

```text
Problem
→ docker compose ps
→ docker compose logs
→ docker compose config
→ docker inspect
→ Fix Compose
```

---

### [핵심]

대표 문제:

| Problem              | Cause                   | First Check   |
| -------------------- | ----------------------- | ------------- |
| Port Conflict        | Host Port 사용 중       | ports         |
| DB Connection Failed | Hostname 오류           | Service Name  |
| Container Exit       | Command / Env 오류      | logs          |
| Volume Data Missing  | Volume 삭제             | down -v       |
| Env Missing          | .env 경로 / 변수명 오류 | config        |
| Health Unhealthy     | Health Command 오류     | inspect       |
| Build Failed         | Context 오류            | build.context |
| Permission Denied    | Volume 권한 문제        | mount path    |
| Network Error        | Network 분리            | networks      |
| Restart Loop         | App Crash               | logs          |

---

### [실무]

상태 확인:

```bash
docker compose ps
```

로그 확인:

```bash
docker compose logs -f app
```

최종 설정 확인:

```bash
docker compose config
```

Service 재시작:

```bash
docker compose restart app
```

Rebuild 후 실행:

```bash
docker compose up -d --build
```

Volume 포함 전체 삭제:

```bash
docker compose down -v
```

단, `down -v`는 데이터 삭제 위험이 있다.

---

### [주의]

Compose 문제 해결 시 가장 먼저 `logs`와 `config`를 확인한다.

주의할 점:

- `docker compose config`로 변수 치환 결과 확인
- `localhost` 대신 Service Name 사용 여부 확인
- Host Port와 Container Port 방향 확인
- `.env` 위치 확인
- Volume 삭제 여부 확인
- Health Check 명령이 Image 내부에서 실행 가능한지 확인
- Restart Policy로 오류가 가려지지 않는지 확인

---

### [FAQ]

Q. Compose에서 DB 연결이 실패하는 가장 흔한 이유는?
A. Application이 `localhost`로 DB에 접속하려고 하기 때문이다. Compose 내부에서는 Service Name을 사용해야 한다.

Q. Port is already allocated 오류는 왜 발생하는가?
A. Host Port를 다른 Process나 Container가 이미 사용 중이기 때문이다.

Q. 환경변수가 제대로 들어갔는지 어떻게 확인하는가?
A. `docker compose config`로 변수 치환 결과를 확인하고, `docker compose exec app env`로 Container 내부 환경변수를 확인한다.

Q. Volume 데이터가 사라진 이유는?
A. `docker compose down -v`로 Named Volume을 삭제했을 가능성이 있다.

Q. Health Check 실패 원인은 어떻게 확인하는가?
A. `docker inspect`와 `docker compose logs`로 Health Check 결과와 Application 로그를 확인한다.

---

# 18. Compose Best Practice

## 18.1 Docker Compose Best Practice

### [개념]

Docker Compose Best Practice는 Multi Container 환경의 재현성, 보안, 유지보수성, 장애 대응성을 높이기 위한 작성 기준이다.

Compose 문서의 목표는 Agent가 Local Development Environment, Test Stack, Deployment Stack, Troubleshooting Pattern을 생성하고 검토할 수 있게 하는 것이다.

---

### [핵심]

Compose Best Practice:

- Service Name 명확화
- Version Tag 명시
- Secret 하드코딩 금지
- `.env.example` 제공
- DB 데이터는 Named Volume 사용
- 내부 통신은 Service Name 사용
- 외부 공개 Port 최소화
- Health Check 설정
- depends_on condition 사용
- Restart Policy 설정
- Network 분리
- 개발용 / 운영용 Compose 분리
- `docker compose config`로 최종 설정 검증
- 로그는 stdout / stderr 중심
- Resource Limit 고려
- 운영 DB Port 외부 공개 지양

---

### [실무]

권장 Compose Checklist:

```text
[Service]
- app, mysql, redis, nginx Service 이름 명확한가?
- image Tag가 명확한가?
- build context가 정확한가?

[Environment]
- Secret이 하드코딩되지 않았는가?
- .env.example이 있는가?
- SPRING_PROFILES_ACTIVE가 명확한가?

[Network]
- 내부 통신이 Service Name 기반인가?
- DB가 불필요하게 외부 공개되지 않았는가?

[Volume]
- DB / Upload 데이터가 Volume에 저장되는가?
- down -v 위험을 알고 있는가?

[Health]
- DB / Redis / App Health Check가 있는가?
- depends_on condition이 적절한가?

[Operation]
- restart Policy가 설정되었는가?
- logs 확인 방식이 명확한가?
- docker compose config로 검증했는가?
```

---

### [주의]

Compose 파일을 운영 Secret 저장소처럼 사용하면 안 된다.

피해야 할 패턴:

```yaml
environment:
  JWT_SECRET: real-secret
  DB_PASSWORD: real-password
```

권장 패턴:

```yaml
environment:
  JWT_SECRET: ${JWT_SECRET}
  DB_PASSWORD: ${DB_PASSWORD}
```

운영에서는 다음을 고려한다.

- CI/CD Secret
- Cloud Secret Manager
- Docker Secret
- Vault
- Server Environment Variable

---

### [FAQ]

Q. 좋은 Compose 파일의 기준은?
A. Service, Network, Volume, Environment, Health Check가 명확하고 Secret을 하드코딩하지 않으며 재현 가능한 Compose 파일이다.

Q. Compose에서 가장 흔한 실수는?
A. `localhost`로 다른 Container에 접속하려는 것, Port 방향을 헷갈리는 것, Secret을 하드코딩하는 것, Volume을 삭제하는 것이다.

Q. Compose 검증 명령은 무엇인가?
A. `docker compose config`로 최종 병합 및 변수 치환 결과를 확인한다.

Q. 운영에서도 Docker Compose를 사용할 수 있는가?
A. 소규모 서버에서는 가능하지만 대규모 운영과 자동 복구, 스케일링에는 Kubernetes 같은 Orchestrator가 더 적합하다.

---

# Retrieval Queries

### [FAQ]

Q. Docker Compose란 무엇인가?
A. Docker Compose는 여러 Docker Container를 하나의 YAML 파일로 정의하고 실행하는 Multi Container Management Tool이다.

Q. Docker Compose는 언제 사용하는가?
A. Spring Boot, MySQL, Redis, Nginx처럼 여러 Container를 함께 실행해야 할 때 사용한다.

Q. Docker Compose v2 명령어는 무엇인가?
A. Docker Compose v2는 `docker compose up`, `docker compose down`, `docker compose logs`처럼 공백이 있는 명령을 사용한다.

Q. compose.yml은 무엇인가?
A. compose.yml은 Docker Compose가 실행할 Service, Network, Volume을 정의하는 YAML 파일이다.

Q. Docker Compose services는 무엇인가?
A. services는 Compose에서 실행할 Container Service들을 정의하는 영역이다.

Q. Compose Service 이름은 어떤 역할을 하는가?
A. Service 이름은 Compose Network 내부에서 DNS Hostname으로 사용된다.

Q. Compose 내부에서 MySQL Host는 무엇으로 설정해야 하는가?
A. MySQL Service 이름이 `mysql`이면 Host를 `mysql`로 설정해야 한다.

Q. Compose 내부에서 localhost를 쓰면 안 되는 이유는?
A. Container 내부의 localhost는 Host PC가 아니라 자기 자신을 의미하기 때문이다.

Q. Compose image는 무엇인가?
A. image는 Service가 사용할 Docker Image를 지정하는 설정이다.

Q. Compose build는 무엇인가?
A. build는 Dockerfile을 기반으로 Service Image를 Build하는 설정이다.

Q. image와 build 차이는 무엇인가?
A. image는 기존 Image를 사용하고 build는 Dockerfile로 Image를 생성한다.

Q. build context란 무엇인가?
A. build context는 Docker Build가 접근 가능한 파일 범위이며 Dockerfile COPY 기준이 된다.

Q. Compose ports는 무엇인가?
A. ports는 Host Port와 Container Port를 연결하여 외부 접근을 가능하게 하는 설정이다.

Q. ports에서 왼쪽과 오른쪽은 무엇인가?
A. 왼쪽은 Host Port이고 오른쪽은 Container Port이다.

Q. Compose expose는 무엇인가?
A. expose는 Host에는 공개하지 않고 Compose 내부 Network에만 Port를 노출하는 설정이다.

Q. ports와 expose 차이는 무엇인가?
A. ports는 Host 외부 접근을 허용하고 expose는 내부 Network 노출만 수행한다.

Q. Compose environment는 무엇인가?
A. environment는 Service Container에 Runtime Environment Variable을 주입하는 설정이다.

Q. Compose env_file은 무엇인가?
A. env_file은 별도 파일에서 환경변수를 읽어 Service Container에 주입하는 설정이다.

Q. .env와 env_file은 같은가?
A. 완전히 같지 않다. .env는 Compose 변수 치환에 쓰이고 env_file은 Container 환경변수 주입에 쓰인다.

Q. Compose Volume은 무엇인가?
A. Compose Volume은 Container 데이터 영속성 또는 Host-Container 파일 공유를 위한 저장소 설정이다.

Q. MySQL Container에 Volume이 필요한 이유는?
A. Container 삭제 후에도 Database 데이터를 유지하기 위해 필요하다.

Q. docker compose down -v는 왜 위험한가?
A. Named Volume까지 삭제하여 Database 데이터가 사라질 수 있기 때문이다.

Q. Compose Network는 무엇인가?
A. Compose Network는 Service 간 통신을 제공하는 Container Network이다.

Q. Compose에서 Service끼리 어떻게 통신하는가?
A. 같은 Network에 있으면 Service Name을 Hostname으로 사용해 Container Port로 통신한다.

Q. depends_on은 무엇인가?
A. depends_on은 Service 간 시작 순서를 정의하는 Compose 설정이다.

Q. depends_on은 DB Ready를 보장하는가?
A. 기본 depends_on은 Container 시작 순서만 제어하며 DB Ready는 Health Check와 condition이 필요하다.

Q. Compose healthcheck는 무엇인가?
A. healthcheck는 Service Container 상태를 확인하여 healthy 또는 unhealthy 상태를 판단하는 설정이다.

Q. Spring Boot Health Check는 무엇을 사용하는가?
A. Spring Boot Actuator의 `/actuator/health` Endpoint를 자주 사용한다.

Q. Compose restart는 무엇인가?
A. restart는 Container 종료 시 자동 재시작 여부를 결정하는 설정이다.

Q. 운영에서 자주 쓰는 restart 정책은 무엇인가?
A. `unless-stopped`를 많이 사용한다.

Q. Compose command는 무엇인가?
A. command는 Image의 기본 CMD를 Compose에서 Override하는 설정이다.

Q. Compose entrypoint는 무엇인가?
A. entrypoint는 Image의 기본 ENTRYPOINT를 Compose에서 Override하는 설정이다.

Q. command와 entrypoint 차이는 무엇인가?
A. command는 CMD나 기본 인자를 바꾸고 entrypoint는 실행 명령 자체를 바꾼다.

Q. Compose profiles는 무엇인가?
A. profiles는 특정 Service를 선택적으로 실행하기 위한 Compose 설정이다.

Q. Compose Override란 무엇인가?
A. 기본 Compose 파일에 추가 Compose 파일을 병합하여 환경별 설정을 적용하는 방식이다.

Q. Compose 최종 설정은 어떻게 확인하는가?
A. `docker compose config` 명령으로 최종 병합 및 변수 치환 결과를 확인한다.

Q. docker compose logs는 무엇인가?
A. Compose Service Container의 stdout과 stderr 로그를 조회하는 명령이다.

Q. Compose Resource Limit은 왜 필요한가?
A. Container 자원 사용량을 제한하여 OOM, Host 자원 고갈, Service 간 간섭을 줄이기 위해 필요하다.

Q. Spring Boot Compose에서 JVM Heap은 어떻게 설정해야 하는가?
A. Container Memory Limit보다 작게 설정하고 Native Memory와 Thread Stack 여유를 남겨야 한다.

Q. Spring Boot Compose 기본 패턴은 무엇인가?
A. app, mysql, redis Service를 정의하고 환경변수, Volume, Network, Health Check, depends_on을 설정하는 구조이다.

Q. Compose에서 DB 연결 실패가 발생하는 가장 흔한 이유는?
A. Application이 localhost로 DB에 접속하거나 Service Name, Network, Port, 환경변수를 잘못 설정했기 때문이다.

Q. Port is already allocated 오류는 왜 발생하는가?
A. Host Port를 다른 Process나 Container가 이미 사용 중이기 때문이다.

Q. Compose 환경변수는 어떻게 확인하는가?
A. `docker compose config`와 `docker compose exec app env`로 확인한다.

Q. 좋은 Compose 파일의 기준은 무엇인가?
A. Service, Network, Volume, Environment, Health Check가 명확하고 Secret을 하드코딩하지 않으며 재현 가능한 파일이다.

Q. Compose에서 가장 흔한 실수는 무엇인가?
A. localhost 오해, Port 방향 혼동, Secret 하드코딩, Volume 삭제, Health Check 누락이다.
