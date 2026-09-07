# Docker Part02 Dockerfile

---

# 1. Dockerfile Core

## 1.1 Dockerfile Overview

### [개념]

Dockerfile은 Docker Image를 Build하기 위한 명세 파일이다.

Dockerfile은 Base Image, 작업 디렉터리, 파일 복사, 패키지 설치, 환경변수, 실행 명령, Health Check를 선언한다.

```text
Dockerfile
→ docker build
→ Docker Image
→ docker run
→ Docker Container
```

Dockerfile은 Application Runtime Environment를 코드로 정의하는 Infrastructure as Code 성격을 가진다.

---

### [핵심]

Dockerfile 핵심 목적:

- Image Build 절차 정의
- Application Runtime 표준화
- Dependency 설치 자동화
- 실행 명령 고정
- 배포 환경 재현성 확보
- CI/CD Build 자동화 지원
- Docker Layer Cache 최적화
- Runtime Security 기준 적용

주요 Instruction:

| Instruction | Purpose                                  |
| ----------- | ---------------------------------------- |
| FROM        | Base Image 지정                          |
| WORKDIR     | 작업 디렉터리 지정                       |
| COPY        | Host 파일을 Image로 복사                 |
| ADD         | 파일 복사 + 압축 해제 / URL 처리         |
| RUN         | Build 단계 명령 실행                     |
| ENV         | Runtime Environment Variable 기본값 설정 |
| ARG         | Build Argument 설정                      |
| EXPOSE      | Container Port 문서화                    |
| ENTRYPOINT  | Container 기본 실행 명령                 |
| CMD         | 기본 실행 인자 또는 명령                 |
| USER        | 실행 사용자 지정                         |
| HEALTHCHECK | Container 상태 확인                      |
| LABEL       | Image Metadata 추가                      |

---

### [Flow]

```text
Base Image 선택
→ WORKDIR 설정
→ Dependency 파일 COPY
→ RUN Dependency Install
→ Application 파일 COPY
→ Build Artifact 생성
→ Runtime Image 구성
→ ENTRYPOINT 설정
→ Health Check 설정
```

---

### [실무]

2026 실무 기준 Dockerfile은 짧고 명확하며 재현 가능하게 작성한다.

Spring Boot 기본 Dockerfile:

```dockerfile
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY build/libs/app.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

Build:

```bash
docker build -t spring-app:1.0.0 .
```

Run:

```bash
docker run -p 8080:8080 spring-app:1.0.0
```

Dockerfile 작성 기준:

- Base Image는 명확한 Version Tag 사용
- Build Context 최소화
- `.dockerignore` 사용
- Secret 하드코딩 금지
- Layer Cache 고려
- 운영 Image는 가능한 작게 유지
- Runtime Image와 Build Image 분리 고려
- ENTRYPOINT / CMD 역할 구분
- Non-root User 실행 고려
- Health Check 또는 Compose Health Check 적용

---

### [주의]

Dockerfile에서 자주 발생하는 문제:

| Problem             | Cause                 | Solution                  |
| ------------------- | --------------------- | ------------------------- |
| Image Size 큼       | 불필요 파일 포함      | `.dockerignore` 작성      |
| Build 느림          | Cache 비효율          | COPY 순서 최적화          |
| Secret 노출         | ENV / COPY로 포함     | Runtime Env / Secret 사용 |
| Container 즉시 종료 | ENTRYPOINT 오류       | 실행 명령 확인            |
| Permission Denied   | USER / 파일 권한 문제 | 권한과 소유자 확인        |
| Port 접근 실패      | EXPOSE 오해           | `-p` Port Mapping 사용    |
| Build 실패          | Build Context 오류    | Dockerfile 위치 확인      |
| Health Check 실패   | curl / wget 없음      | Runtime Image 도구 확인   |

---

### [FAQ]

Q. Dockerfile이란?
A. Docker Image를 Build하기 위한 명세 파일이다.

Q. Dockerfile은 왜 필요한가?
A. Application 실행 환경을 코드로 정의하여 Image Build와 배포 재현성을 확보하기 위해 필요하다.

Q. Dockerfile과 Image의 관계는?
A. Dockerfile은 Image를 만드는 설계도이고, Image는 Dockerfile을 Build한 결과물이다.

Q. Dockerfile은 운영 서버에서 직접 수정해도 되는가?
A. 권장하지 않는다. Git에서 관리하고 CI/CD로 Build하는 방식이 적합하다.

---

# 2. FROM

## 2.1 FROM Instruction

### [개념]

`FROM`은 Dockerfile의 Base Image를 지정하는 Instruction이다.

모든 Dockerfile은 일반적으로 `FROM`으로 시작한다.

```dockerfile
FROM eclipse-temurin:21-jre
```

Base Image는 Application Runtime의 기반이 된다.

---

### [핵심]

`FROM` 핵심:

- Dockerfile의 시작점
- Base Image 지정
- OS / Runtime 포함 가능
- Multi-stage Build에서 여러 번 사용 가능
- Image Size와 보안에 큰 영향
- 명확한 Version Tag 사용 권장
- Build Stage와 Runtime Stage 구분 가능

예시:

```dockerfile
FROM ubuntu:24.04
FROM nginx:1.27
FROM node:22
FROM eclipse-temurin:21-jre
FROM eclipse-temurin:21-jdk
```

---

### [실무]

Spring Boot Runtime Image 예시:

```dockerfile
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY build/libs/app.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

Build Stage에서는 JDK 또는 Gradle Image를 사용한다.

```dockerfile
FROM gradle:8.10-jdk21 AS builder
```

Runtime Stage에서는 JRE Image를 사용한다.

```dockerfile
FROM eclipse-temurin:21-jre AS runtime
```

권장 기준:

| Use Case            | Base Image             |
| ------------------- | ---------------------- |
| Spring Boot Build   | gradle:8.x-jdk21       |
| Spring Boot Runtime | eclipse-temurin:21-jre |
| React Build         | node:22                |
| Static Web Runtime  | nginx:1.27             |
| Small Utility       | alpine                 |
| General Linux       | ubuntu:24.04           |

---

### [주의]

`latest` 단독 사용은 운영에서 피한다.

비권장:

```dockerfile
FROM openjdk:latest
```

권장:

```dockerfile
FROM eclipse-temurin:21-jre
```

주의할 점:

- Unknown Image 사용 금지
- 오래된 Runtime Image 사용 금지
- 불필요하게 큰 Base Image 사용 금지
- Build용 Image와 Runtime용 Image 혼동 금지
- 보안 취약점이 많은 Image 사용 금지
- Java Version과 Spring Boot Version 호환성 확인

---

### [FAQ]

Q. FROM은 무엇인가?
A. Docker Image의 기반이 되는 Base Image를 지정하는 Instruction이다.

Q. FROM은 반드시 필요한가?
A. 일반적인 Dockerfile에서는 필수이다. Scratch Image를 사용하는 특수한 경우에도 `FROM scratch`를 사용한다.

Q. JDK Image와 JRE Image 차이는?
A. JDK는 Build와 Compile 도구를 포함하고, JRE는 Java Application 실행에 필요한 Runtime만 포함한다.

Q. 운영에서는 JDK와 JRE 중 무엇이 적합한가?
A. 운영 Runtime에는 보통 JRE Image가 적합하다. Build에는 JDK 또는 Gradle Image를 사용한다.

---

# 3. WORKDIR

## 3.1 WORKDIR Instruction

### [개념]

`WORKDIR`은 Dockerfile 내 명령이 실행될 작업 디렉터리를 지정한다.

```dockerfile
WORKDIR /app
```

`WORKDIR` 이후의 `COPY`, `RUN`, `CMD`, `ENTRYPOINT`는 지정된 디렉터리를 기준으로 동작한다.

---

### [핵심]

`WORKDIR` 핵심:

- Container 내부 작업 경로 지정
- 디렉터리가 없으면 자동 생성
- 상대 경로 기준점 제공
- Dockerfile 가독성 향상
- `cd` 명령 반복 방지
- Application 실행 경로 명확화

예시:

```dockerfile
WORKDIR /app
COPY app.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

---

### [실무]

Spring Boot Dockerfile에서는 `/app`을 자주 사용한다.

```dockerfile
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY build/libs/app.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

React + Nginx Runtime에서는 Nginx Static Directory를 사용한다.

```dockerfile
FROM nginx:1.27
WORKDIR /usr/share/nginx/html
COPY build/ .
```

권장 경로:

| Application    | WORKDIR               |
| -------------- | --------------------- |
| Spring Boot    | /app                  |
| Node.js        | /app                  |
| Python         | /app                  |
| Nginx Static   | /usr/share/nginx/html |
| Utility Script | /workspace            |

---

### [주의]

`RUN cd /app` 방식은 Dockerfile Layer마다 유지되지 않을 수 있다.

비권장:

```dockerfile
RUN cd /app
COPY app.jar app.jar
```

권장:

```dockerfile
WORKDIR /app
COPY app.jar app.jar
```

주의할 점:

- Host 경로와 Container 경로 혼동 금지
- 절대 경로 사용 권장
- 불필요하게 깊은 경로 지양
- Runtime User 권한과 WORKDIR 권한 확인
- Non-root User 사용 시 WORKDIR 소유자 확인

---

### [FAQ]

Q. WORKDIR은 무엇인가?
A. Dockerfile 명령이 실행될 Container 내부 작업 디렉터리를 지정하는 Instruction이다.

Q. WORKDIR 디렉터리가 없으면 어떻게 되는가?
A. Docker Build 과정에서 자동 생성된다.

Q. RUN cd와 WORKDIR 중 무엇을 사용해야 하는가?
A. WORKDIR을 사용하는 것이 권장된다. 명령 간 작업 경로를 명확히 유지할 수 있다.

---

# 4. COPY and ADD

## 4.1 COPY Instruction

### [개념]

`COPY`는 Host Build Context의 파일 또는 디렉터리를 Docker Image 내부로 복사하는 Instruction이다.

```dockerfile
COPY build/libs/app.jar app.jar
```

`COPY`는 Dockerfile에서 Application Artifact를 Image에 포함할 때 가장 많이 사용된다.

---

### [핵심]

`COPY` 핵심:

- Host 파일을 Image Layer에 복사
- Build Context 내부 파일만 복사 가능
- Layer Cache에 영향
- `.dockerignore`의 영향을 받음
- `ADD`보다 명확하고 권장됨
- Dependency Cache 최적화에 중요

예시:

```dockerfile
COPY app.jar /app/app.jar
COPY build/libs/*.jar app.jar
COPY package.json package-lock.json ./
COPY src/ ./src/
```

---

### [실무]

Spring Boot Jar 복사:

```dockerfile
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY build/libs/*.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

Node.js 의존성 Cache 최적화:

```dockerfile
FROM node:22
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
CMD ["npm", "start"]
```

Layer Cache 최적화를 위해 변경이 적은 파일을 먼저 복사한다.

```text
Dependency Manifest COPY
→ Install Dependency
→ Source Code COPY
→ Build
```

---

### [주의]

Build Context 밖의 파일은 `COPY`할 수 없다.

비권장:

```dockerfile
COPY ../secret.env /app/secret.env
```

주의할 점:

- `.env` 복사 금지
- Secret 파일 복사 금지
- `.git` 복사 방지
- `node_modules` 복사 방지
- Build 결과물 경로 확인
- Wildcard 사용 시 결과 파일이 하나인지 확인
- `.dockerignore`로 필요한 파일이 제외되지 않았는지 확인

---

### [FAQ]

Q. COPY는 무엇인가?
A. Host Build Context의 파일을 Docker Image 내부로 복사하는 Instruction이다.

Q. COPY는 Build Context 밖의 파일을 복사할 수 있는가?
A. 불가능하다. Docker Build Context 내부 파일만 복사할 수 있다.

Q. COPY와 ADD 중 무엇을 주로 사용하는가?
A. 일반 파일 복사는 COPY를 권장한다. ADD는 특수 기능이 필요할 때만 사용한다.

---

## 4.2 ADD Instruction

### [개념]

`ADD`는 `COPY`와 유사하게 파일을 Image로 복사하지만 추가 기능을 가진다.

`ADD`는 Tar 압축 파일 자동 해제와 URL 처리 기능을 제공한다.

```dockerfile
ADD app.tar.gz /app/
```

---

### [핵심]

`ADD` 특징:

- 파일 복사 가능
- Tar 압축 자동 해제 가능
- URL에서 파일 다운로드 가능
- 동작이 COPY보다 암묵적
- 일반 복사에는 COPY 권장

`COPY`와 `ADD` 비교:

| Instruction | Purpose              | Recommendation       |
| ----------- | -------------------- | -------------------- |
| COPY        | 단순 파일 복사       | 기본 권장            |
| ADD         | 압축 해제 / URL 처리 | 특수 상황에서만 사용 |

---

### [실무]

압축 파일 자동 해제가 필요한 경우:

```dockerfile
ADD archive.tar.gz /opt/app/
```

일반 Application 복사에는 COPY 사용:

```dockerfile
COPY build/libs/app.jar app.jar
```

운영 Dockerfile에서는 예측 가능한 동작을 위해 `COPY`를 기본으로 사용한다.

---

### [주의]

ADD URL 다운로드는 재현성과 보안 측면에서 주의가 필요하다.

비권장:

```dockerfile
ADD https://example.com/file.tar.gz /app/
```

권장:

```dockerfile
RUN curl -fsSL https://example.com/file.tar.gz -o file.tar.gz
```

주의할 점:

- 자동 압축 해제 동작 오해 가능
- Remote URL 다운로드의 무결성 확인 필요
- Build 재현성 저하 가능
- 일반 복사에는 ADD 사용 지양
- External File Version 고정 필요

---

### [FAQ]

Q. ADD는 무엇인가?
A. 파일을 Image로 복사하고 Tar 압축 해제 또는 URL 처리 기능을 추가로 제공하는 Instruction이다.

Q. COPY 대신 ADD를 사용해도 되는가?
A. 가능하지만 일반 복사에는 COPY가 더 명확하고 권장된다.

Q. ADD를 사용해야 하는 경우는?
A. Tar 압축 파일을 Image 내부에서 자동 해제해야 하는 경우에 사용할 수 있다.

---

# 5. RUN

## 5.1 RUN Instruction

### [개념]

`RUN`은 Docker Image Build 단계에서 명령어를 실행하는 Instruction이다.

```dockerfile
RUN apt-get update && apt-get install -y curl
```

`RUN` 결과는 Image Layer에 저장된다.

---

### [핵심]

`RUN` 핵심:

- Build Time 명령 실행
- Package 설치
- Dependency 설치
- Build 작업 수행
- Layer 생성
- Cache 활용 가능
- Runtime 실행 명령이 아님

예시:

```dockerfile
RUN apt-get update
RUN npm ci
RUN ./gradlew bootJar
RUN chmod +x entrypoint.sh
```

---

### [실무]

Ubuntu Package 설치 예시:

```dockerfile
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*
```

Node.js Dependency 설치:

```dockerfile
COPY package.json package-lock.json ./
RUN npm ci
```

Gradle Build Stage:

```dockerfile
COPY build.gradle settings.gradle ./
COPY src ./src
RUN gradle clean bootJar --no-daemon
```

`RUN`은 가능한 관련 명령을 하나로 묶어 Layer 수와 불필요 파일을 줄인다.

---

### [주의]

`RUN`은 Container 실행 시점이 아니라 Image Build 시점에 실행된다.

오해:

```dockerfile
RUN java -jar app.jar
```

이 방식은 Build 중 Application을 실행하는 것이므로 일반적으로 잘못된 사용이다.

권장:

```dockerfile
ENTRYPOINT ["java", "-jar", "app.jar"]
```

주의할 점:

- `apt-get update`와 `apt-get install`은 같은 RUN에 작성
- 설치 후 Package Cache 제거
- 불필요한 Build Tool을 Runtime Image에 남기지 않기
- Secret을 RUN에서 사용하고 Layer에 남기지 않기
- `RUN cd` 대신 WORKDIR 사용

---

### [FAQ]

Q. RUN은 언제 실행되는가?
A. Docker Image Build 단계에서 실행된다.

Q. RUN과 CMD의 차이는?
A. RUN은 Build Time 명령이고, CMD는 Container Runtime 기본 명령이다.

Q. RUN으로 Application을 실행해도 되는가?
A. 일반적으로 안 된다. Application 실행은 ENTRYPOINT 또는 CMD로 지정해야 한다.

---

# 6. ENV and ARG

## 6.1 ENV Instruction

### [개념]

`ENV`는 Docker Image와 Container Runtime에서 사용할 환경변수를 설정하는 Instruction이다.

```dockerfile
ENV SPRING_PROFILES_ACTIVE=prod
```

`ENV`로 설정한 값은 Image Metadata에 남고 Container 실행 시 기본 환경변수로 사용된다.

---

### [핵심]

`ENV` 핵심:

- Runtime 환경변수 기본값 제공
- Container 내부에서 접근 가능
- Image Metadata에 저장
- `docker run -e`로 Override 가능
- Docker Compose `environment`로 Override 가능
- Secret 저장 용도 부적합

예시:

```dockerfile
ENV APP_HOME=/app
ENV JAVA_OPTS="-Xms256m -Xmx512m"
ENV SPRING_PROFILES_ACTIVE=prod
```

Runtime Override:

```bash
docker run -e SPRING_PROFILES_ACTIVE=dev spring-app:1.0.0
```

---

### [실무]

Spring Boot 환경변수 예시:

```dockerfile
FROM eclipse-temurin:21-jre
WORKDIR /app
ENV SPRING_PROFILES_ACTIVE=prod
COPY build/libs/app.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

Runtime에서 Profile 변경:

```bash
docker run \
  -e SPRING_PROFILES_ACTIVE=prod \
  -e DB_HOST=mysql \
  -p 8080:8080 \
  spring-app:1.0.0
```

Docker Compose에서는 `environment`로 주입한다.

```yaml
services:
  app:
    image: spring-app:1.0.0
    environment:
      SPRING_PROFILES_ACTIVE: prod
      DB_HOST: mysql
```

---

### [주의]

Secret을 `ENV`에 하드코딩하면 안 된다.

비권장:

```dockerfile
ENV JWT_SECRET=my-secret-key
ENV DB_PASSWORD=1234
```

주의할 점:

- ENV 값은 Image inspect로 노출될 수 있음
- Secret은 Docker Secret, CI/CD Secret, Runtime Env, Vault 사용
- 환경별 값은 Runtime에 주입
- Dockerfile에 운영 비밀번호 작성 금지
- ENV 기본값과 운영 Override 값 혼동 금지

---

### [FAQ]

Q. ENV는 무엇인가?
A. Docker Image와 Container에서 사용할 환경변수를 설정하는 Instruction이다.

Q. ENV 값은 Runtime에서 변경할 수 있는가?
A. 가능하다. `docker run -e` 또는 Compose `environment`로 Override할 수 있다.

Q. ENV에 비밀번호를 넣어도 되는가?
A. 안 된다. Dockerfile ENV에 Secret을 하드코딩하면 Image Metadata에 남아 보안 위험이 있다.

---

## 6.2 ARG Instruction

### [개념]

`ARG`는 Docker Image Build 시점에 사용할 Build Argument를 정의하는 Instruction이다.

```dockerfile
ARG APP_VERSION=1.0.0
```

`ARG`는 기본적으로 Build Time에서 사용되며 Runtime 환경변수와 다르다.

---

### [핵심]

`ARG` 핵심:

- Build Time 변수
- `docker build --build-arg`로 값 전달
- Dockerfile Build 과정에서 사용
- Runtime Container 환경변수 아님
- ENV와 목적이 다름
- Image Label이나 Build 경로에 활용 가능

예시:

```dockerfile
ARG JAR_FILE=build/libs/app.jar
COPY ${JAR_FILE} app.jar
```

Build:

```bash
docker build --build-arg JAR_FILE=build/libs/festapick.jar -t app:1.0 .
```

---

### [실무]

Version Label에 ARG 사용:

```dockerfile
ARG APP_VERSION=unknown
LABEL app.version=${APP_VERSION}
```

JAR 파일 경로에 ARG 사용:

```dockerfile
ARG JAR_FILE=build/libs/*.jar
COPY ${JAR_FILE} app.jar
```

Build 명령:

```bash
docker build \
  --build-arg APP_VERSION=1.0.0 \
  -t festapick-api:1.0.0 .
```

---

### [주의]

ARG도 Secret 전달에 안전하지 않다.

비권장:

```dockerfile
ARG DB_PASSWORD=1234
```

주의할 점:

- Build History에 남을 수 있음
- Runtime에서 자동 사용되지 않음
- ENV와 혼동 금지
- Secret 전달 용도로 사용 금지
- ARG 값은 Build 재현성에 영향을 줄 수 있음

---

### [FAQ]

Q. ARG는 무엇인가?
A. Docker Image Build 시점에 사용하는 Build Argument이다.

Q. ARG와 ENV의 차이는?
A. ARG는 Build Time 변수이고 ENV는 Container Runtime 환경변수로 사용할 수 있다.

Q. ARG로 Secret을 전달해도 되는가?
A. 권장하지 않는다. Build History나 Image Metadata에 노출될 수 있다.

---

# 7. EXPOSE

## 7.1 EXPOSE Instruction

### [개념]

`EXPOSE`는 Container가 사용할 Port를 문서화하는 Instruction이다.

```dockerfile
EXPOSE 8080
```

`EXPOSE`는 실제 Host Port를 열지 않는다.

Host Port 연결은 `docker run -p` 또는 Compose `ports`로 설정한다.

---

### [핵심]

`EXPOSE` 핵심:

- Container Port 문서화
- Image Metadata에 기록
- Port Mapping 직접 수행 안 함
- `docker run -p`와 역할 다름
- 협업과 유지보수에 도움
- Reverse Proxy 구성 시 Container Port 확인에 유용

예시:

```dockerfile
EXPOSE 8080
```

실제 Port Mapping:

```bash
docker run -p 8080:8080 spring-app:1.0.0
```

---

### [실무]

Spring Boot Dockerfile:

```dockerfile
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY build/libs/app.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

Nginx Dockerfile:

```dockerfile
FROM nginx:1.27
EXPOSE 80
```

Port Mapping 예시:

```bash
docker run -p 80:80 nginx
docker run -p 8080:8080 spring-app
```

Compose 예시:

```yaml
services:
  app:
    ports:
      - "8080:8080"
```

---

### [주의]

`EXPOSE`만 작성하면 외부에서 접근할 수 없다.

오해:

```dockerfile
EXPOSE 8080
```

위 설정만으로 Host `localhost:8080` 접근은 되지 않는다.

필요:

```bash
docker run -p 8080:8080 app
```

주의할 점:

- EXPOSE는 문서화 목적
- Host Port 충돌 확인
- Container Port와 Host Port 구분
- 방화벽 / 보안 그룹 확인
- Reverse Proxy 사용 시 Port 흐름 확인

---

### [FAQ]

Q. EXPOSE는 무엇인가?
A. Container가 사용하는 Port를 Image Metadata에 문서화하는 Instruction이다.

Q. EXPOSE를 쓰면 Port가 열리는가?
A. 아니다. 실제 Host Port 연결은 `docker run -p` 또는 Compose `ports`로 해야 한다.

Q. Spring Boot 기본 Port는 무엇인가?
A. 기본값은 8080이다. Dockerfile에서는 보통 `EXPOSE 8080`을 작성한다.

---

# 8. ENTRYPOINT and CMD

## 8.1 ENTRYPOINT Instruction

### [개념]

`ENTRYPOINT`는 Container가 시작될 때 실행할 기본 명령을 지정하는 Instruction이다.

```dockerfile
ENTRYPOINT ["java", "-jar", "app.jar"]
```

`ENTRYPOINT`는 Container의 Main Process를 정의한다.

---

### [핵심]

`ENTRYPOINT` 핵심:

- Container 시작 시 실행
- Main Process 지정
- 실행 명령 고정에 적합
- Exec Form 권장
- CMD와 조합 가능
- Container Lifecycle에 직접 영향

Exec Form:

```dockerfile
ENTRYPOINT ["java", "-jar", "app.jar"]
```

Shell Form:

```dockerfile
ENTRYPOINT java -jar app.jar
```

권장:

```dockerfile
ENTRYPOINT ["java", "-jar", "app.jar"]
```

---

### [실무]

Spring Boot 실행:

```dockerfile
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY build/libs/app.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

Java Option 적용:

```dockerfile
ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]
```

Runtime:

```bash
docker run -e JAVA_OPTS="-Xms256m -Xmx512m" spring-app:1.0.0
```

운영에서는 Signal Handling과 종료 처리를 고려해 Exec Form을 우선 사용한다.

---

### [주의]

Shell Form은 Signal 전달과 PID 1 처리에서 불리할 수 있다.

비권장:

```dockerfile
ENTRYPOINT java -jar app.jar
```

권장:

```dockerfile
ENTRYPOINT ["java", "-jar", "app.jar"]
```

주의할 점:

- Main Process가 종료되면 Container도 종료됨
- 잘못된 ENTRYPOINT는 Container Exit 원인
- Shell Script 사용 시 실행 권한 필요
- ENTRYPOINT에 Secret 직접 작성 금지
- Debug 시 `--entrypoint sh`로 Override 가능

---

### [FAQ]

Q. ENTRYPOINT는 무엇인가?
A. Container가 시작될 때 실행할 기본 명령을 지정하는 Instruction이다.

Q. Spring Boot Dockerfile에서 ENTRYPOINT는 어떻게 쓰는가?
A. 보통 `ENTRYPOINT ["java", "-jar", "app.jar"]` 형태로 사용한다.

Q. ENTRYPOINT 오류가 나면 어떻게 확인하는가?
A. `docker logs`와 `docker inspect`로 실행 명령과 오류 메시지를 확인한다.

---

## 8.2 CMD Instruction

### [개념]

`CMD`는 Container 실행 시 사용할 기본 명령 또는 기본 인자를 지정하는 Instruction이다.

```dockerfile
CMD ["--server.port=8080"]
```

`CMD`는 `docker run` 명령에서 전달한 인자로 Override될 수 있다.

---

### [핵심]

`CMD` 핵심:

- Runtime 기본 명령 또는 인자 지정
- Dockerfile에서 하나만 유효
- `docker run` 인자로 Override 가능
- ENTRYPOINT와 조합 가능
- 유연한 Runtime 설정에 적합

예시:

```dockerfile
ENTRYPOINT ["java", "-jar", "app.jar"]
CMD ["--spring.profiles.active=prod"]
```

실행 결과:

```text
java -jar app.jar --spring.profiles.active=prod
```

Override:

```bash
docker run app:1.0 --spring.profiles.active=dev
```

---

### [실무]

Spring Boot CMD 조합:

```dockerfile
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY build/libs/app.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
CMD ["--spring.profiles.active=prod"]
```

기본 명령만 사용하는 경우:

```dockerfile
CMD ["npm", "start"]
```

ENTRYPOINT와 CMD 선택 기준:

| Case                     | Recommended |
| ------------------------ | ----------- |
| 실행 명령 고정           | ENTRYPOINT  |
| 기본 인자 제공           | CMD         |
| 쉽게 Override 필요       | CMD         |
| Application Main Process | ENTRYPOINT  |

---

### [주의]

Dockerfile에 CMD를 여러 개 작성하면 마지막 CMD만 적용된다.

비권장:

```dockerfile
CMD ["echo", "first"]
CMD ["echo", "second"]
```

실제 적용:

```text
CMD ["echo", "second"]
```

주의할 점:

- ENTRYPOINT와 CMD 역할 혼동 금지
- Shell Form보다 Exec Form 권장
- Runtime Override 가능성 고려
- Container Main Process 유지 필요

---

### [FAQ]

Q. CMD는 무엇인가?
A. Container 실행 시 사용할 기본 명령 또는 기본 인자를 지정하는 Instruction이다.

Q. ENTRYPOINT와 CMD 차이는?
A. ENTRYPOINT는 실행 명령을 고정하는 데 적합하고, CMD는 기본 인자나 Override 가능한 명령에 적합하다.

Q. CMD를 여러 개 쓰면 어떻게 되는가?
A. 마지막 CMD만 유효하다.

---

# 9. USER

## 9.1 USER Instruction

### [개념]

`USER`는 Container 내부에서 명령을 실행할 사용자를 지정하는 Instruction이다.

```dockerfile
USER appuser
```

기본적으로 많은 Image는 Root User로 실행될 수 있으므로 운영에서는 Non-root User 실행을 권장한다.

---

### [핵심]

`USER` 핵심:

- Container 실행 사용자 지정
- Root 권한 최소화
- 보안 위험 감소
- 파일 권한과 함께 관리 필요
- Runtime Permission Error와 연관
- Volume Permission과 연관

예시:

```dockerfile
RUN useradd -r -u 1001 appuser
USER appuser
```

---

### [실무]

Spring Boot Non-root Dockerfile 예시:

```dockerfile
FROM eclipse-temurin:21-jre
WORKDIR /app

RUN useradd -r -u 1001 appuser

COPY build/libs/app.jar app.jar

RUN chown -R appuser:appuser /app

USER appuser

ENTRYPOINT ["java", "-jar", "app.jar"]
```

권장 기준:

- 운영 Container는 Non-root User 사용
- Application Directory 권한 부여
- Volume Mount 권한 확인
- Privileged Mode 회피
- Root 권한 필요한 작업은 Build 단계에서 처리

---

### [주의]

USER를 변경하면 파일 접근 권한 문제가 발생할 수 있다.

문제 예시:

```text
Permission denied
Unable to access jarfile app.jar
Cannot write log file
Cannot create directory
```

해결:

```dockerfile
RUN chown -R appuser:appuser /app
USER appuser
```

주의할 점:

- COPY 후 chown 필요 여부 확인
- Volume Mount 권한 확인
- Container 내부 Log File 쓰기 지양
- Root 권한이 필요한 Port 사용 주의
- Debug 목적으로 Root 실행 후 운영 반영 금지

---

### [FAQ]

Q. USER는 무엇인가?
A. Dockerfile에서 이후 명령과 Container 실행 사용자를 지정하는 Instruction이다.

Q. 운영 Container를 Root로 실행해도 되는가?
A. 권장하지 않는다. 보안 위험을 줄이기 위해 Non-root User 실행이 좋다.

Q. USER 변경 후 Permission Denied가 발생하는 이유는?
A. Application 파일이나 작업 디렉터리에 해당 User의 권한이 없기 때문이다.

---

# 10. HEALTHCHECK

## 10.1 HEALTHCHECK Instruction

### [개념]

`HEALTHCHECK`는 Container 내부에서 Application 상태를 확인하는 Instruction이다.

```dockerfile
HEALTHCHECK CMD curl --fail http://localhost:8080/actuator/health || exit 1
```

Health Check는 Container 상태를 `healthy` 또는 `unhealthy`로 판단하는 데 사용된다.

---

### [핵심]

`HEALTHCHECK` 핵심:

- Container 상태 확인
- Application Health Monitoring
- 장애 감지 지원
- Restart 판단 보조
- Orchestrator 연동에 유용
- Spring Boot Actuator와 자주 사용
- Running 상태와 Healthy 상태 구분

상태:

| Status    | Meaning                |
| --------- | ---------------------- |
| starting  | Health Check 초기 상태 |
| healthy   | 정상                   |
| unhealthy | 비정상                 |

---

### [실무]

Spring Boot Actuator Health Check:

```dockerfile
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY build/libs/app.jar app.jar
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget -qO- http://localhost:8080/actuator/health || exit 1
ENTRYPOINT ["java", "-jar", "app.jar"]
```

단, Runtime Image에 `wget` 또는 `curl`이 없으면 실패한다.

Compose Health Check 예시:

```yaml
services:
  app:
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:8080/actuator/health"]
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 30s
```

운영에서는 Dockerfile 또는 Compose 중 한 곳에서 Health Check 정책을 명확히 관리한다.

---

### [주의]

Health Check 명령에 필요한 도구가 Image에 있어야 한다.

자주 발생하는 문제:

| Problem            | Cause                     | Solution                       |
| ------------------ | ------------------------- | ------------------------------ |
| curl not found     | Runtime Image에 curl 없음 | curl 설치 또는 wget 사용       |
| wget not found     | Runtime Image에 wget 없음 | wget 설치 또는 다른 명령 사용  |
| unhealthy          | Endpoint 오류             | Actuator 설정 확인             |
| timeout            | App Startup 느림          | start-period 설정              |
| Connection refused | Port / Context Path 오류  | URL 확인                       |
| 401 Unauthorized   | Security 설정             | Health Endpoint 공개 범위 확인 |

주의할 점:

- Health Check가 너무 잦으면 부하 발생
- Startup 시간이 긴 App은 `--start-period` 설정
- Actuator Endpoint 보안 설정 확인
- Health Check URL과 Server Port 일치 확인
- Container 내부 기준 URL 사용

---

### [FAQ]

Q. HEALTHCHECK는 무엇인가?
A. Container 내부에서 Application 상태를 확인하는 Dockerfile Instruction이다.

Q. Spring Boot Health Check는 무엇을 사용하면 좋은가?
A. Spring Boot Actuator의 `/actuator/health` Endpoint를 자주 사용한다.

Q. curl not found 오류는 왜 발생하는가?
A. Runtime Image에 curl이 설치되어 있지 않기 때문이다. curl 설치 또는 wget 사용이 필요하다.

Q. Container가 Running인데 unhealthy일 수 있는가?
A. 가능하다. Process는 실행 중이지만 Health Check 명령이 실패한 상태이다.

---

# 11. LABEL

## 11.1 LABEL Instruction

### [개념]

`LABEL`은 Docker Image에 Metadata를 추가하는 Instruction이다.

```dockerfile
LABEL version="1.0.0"
LABEL maintainer="team@example.com"
```

LABEL은 Image 관리, 검색, 감사, 배포 추적에 활용된다.

---

### [핵심]

`LABEL` 핵심:

- Image Metadata 추가
- Version 정보 기록
- Maintainer 정보 기록
- Build 정보 기록
- Git Commit 정보 기록
- CI/CD Traceability 향상
- Docker Inspect로 확인 가능

예시:

```dockerfile
LABEL app.name="festapick-api"
LABEL app.version="1.0.0"
LABEL app.description="FestaPick Spring Boot API"
```

확인:

```bash
docker inspect festapick-api:1.0.0
```

---

### [실무]

CI/CD Build Metadata:

```dockerfile
ARG APP_VERSION=unknown
ARG GIT_COMMIT=unknown

LABEL app.name="festapick-api"
LABEL app.version=${APP_VERSION}
LABEL git.commit=${GIT_COMMIT}
```

Build:

```bash
docker build \
  --build-arg APP_VERSION=1.0.0 \
  --build-arg GIT_COMMIT=abc1234 \
  -t festapick-api:1.0.0 .
```

사용 목적:

- 배포 Version 추적
- Image 생성 정보 확인
- 장애 분석 시 Build 식별
- Registry Image 관리
- Security Scan Metadata 제공

---

### [주의]

LABEL에 Secret을 넣으면 안 된다.

비권장:

```dockerfile
LABEL db.password="1234"
```

주의할 점:

- 민감 정보 기록 금지
- 너무 많은 LABEL 남발 금지
- Version / Commit / Service Name 중심 사용
- 조직 Naming Convention 유지
- Label 값과 Image Tag 불일치 주의

---

### [FAQ]

Q. LABEL은 무엇인가?
A. Docker Image에 Version, Maintainer, Commit 등 Metadata를 추가하는 Instruction이다.

Q. LABEL은 어디에 활용되는가?
A. Image 관리, 배포 추적, 감사, CI/CD Traceability에 활용된다.

Q. LABEL에 Secret을 넣어도 되는가?
A. 안 된다. LABEL은 Image Metadata로 노출될 수 있다.

---

# 12. .dockerignore

## 12.1 .dockerignore Concept

### [개념]

`.dockerignore`는 Docker Build Context에 포함하지 않을 파일과 디렉터리를 지정하는 파일이다.

```text
.git
node_modules
.env
*.log
```

`.dockerignore`는 Image Size 감소, Build 속도 개선, Secret 노출 방지에 중요하다.

---

### [핵심]

`.dockerignore` 핵심:

- Build Context 크기 감소
- 불필요 파일 Image 포함 방지
- Secret 노출 방지
- Build 속도 개선
- Cache 효율 개선
- Dockerfile 품질 향상

자주 제외하는 항목:

```text
.git
.github
.vscode
.idea
node_modules
dist
target
.env
*.log
.DS_Store
```

---

### [실무]

Spring Boot `.dockerignore` 예시:

```text
.git
.github
.gradle
.idea
.vscode
out
*.log
.env
```

단, Jar를 Host에서 Build한 뒤 `build/libs/*.jar`를 COPY하는 방식이라면 `build` 전체 제외에 주의해야 한다.

Jar 복사 방식에서는 다음처럼 조정한다.

```text
.git
.github
.gradle
.idea
.vscode
*.log
.env
```

Node.js `.dockerignore` 예시:

```text
.git
node_modules
build
dist
.env
*.log
```

---

### [주의]

`.dockerignore` 설정이 잘못되면 필요한 Build Artifact가 누락될 수 있다.

문제 예시:

```text
COPY build/libs/*.jar app.jar
→ no source files were specified
```

원인:

```text
.dockerignore에서 build 디렉터리 제외
```

해결:

```text
build 제외 제거
또는 Multi-stage Build로 Container 내부에서 Build
```

주의할 점:

- Secret 파일 반드시 제외
- Build Artifact 제외 여부 확인
- `.git` 제외
- `node_modules` 제외
- IDE 설정 파일 제외
- 업로드 파일 / 로그 파일 제외

---

### [FAQ]

Q. .dockerignore는 무엇인가?
A. Docker Build Context에 포함하지 않을 파일과 디렉터리를 지정하는 파일이다.

Q. .dockerignore를 왜 사용하는가?
A. Build 속도 개선, Image Size 감소, Secret 노출 방지를 위해 사용한다.

Q. build 디렉터리를 제외해도 되는가?
A. Host에서 Build한 Jar를 COPY하는 방식이면 제외하면 안 된다. Multi-stage Build 방식이면 제외 가능하다.

---

# 13. Dockerfile Layer and Cache

## 13.1 Layer Cache Optimization

### [개념]

Docker Image는 여러 Layer로 구성된다.

Dockerfile의 각 Instruction은 Layer를 만들 수 있고, Docker는 변경되지 않은 Layer를 Cache로 재사용한다.

```text
FROM
→ COPY dependency files
→ RUN install dependencies
→ COPY source code
→ RUN build
```

Layer Cache는 Build 속도에 직접 영향을 준다.

---

### [핵심]

Layer Cache 핵심:

- Dockerfile Instruction 단위로 Cache 생성
- 상위 Layer 변경 시 하위 Cache 무효화
- 변경이 적은 파일을 먼저 COPY
- Dependency 설치 Layer를 Source Code보다 먼저 배치
- 불필요 파일을 Build Context에서 제외
- RUN 명령은 관련 작업을 묶어 작성
- Secret이 포함된 Layer 생성 금지

Cache 최적화 원칙:

```text
Stable Layer First
→ Frequently Changed Layer Later
```

---

### [실무]

Node.js Cache 최적화:

```dockerfile
FROM node:22
WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build
```

Spring Boot Multi-stage Cache 예시:

```dockerfile
FROM gradle:8.10-jdk21 AS builder
WORKDIR /app

COPY build.gradle settings.gradle ./
COPY gradle ./gradle
RUN gradle dependencies --no-daemon

COPY src ./src
RUN gradle clean bootJar --no-daemon
```

Cache 비효율 예시:

```dockerfile
COPY . .
RUN npm ci
```

Source Code가 조금만 바뀌어도 Dependency 설치 Cache가 무효화된다.

---

### [주의]

Layer Cache만 고려하고 보안을 무시하면 안 된다.

주의할 점:

- Secret이 포함된 Layer는 삭제해도 History에 남을 수 있음
- `RUN rm secret.txt`로 완전 삭제되지 않음
- Package Cache 제거 필요
- Layer 수만 줄이려다 가독성 저하 주의
- Cache Busting이 필요한 경우 명확히 처리

---

### [FAQ]

Q. Docker Layer란?
A. Docker Image를 구성하는 변경 불가능한 파일 시스템 단위이다.

Q. Layer Cache는 왜 중요한가?
A. 변경되지 않은 Build 단계를 재사용하여 Image Build 속도를 높인다.

Q. Dockerfile에서 Cache를 잘 쓰려면 어떻게 해야 하는가?
A. 변경이 적은 Dependency 파일을 먼저 COPY하고, 자주 바뀌는 Source Code는 나중에 COPY한다.

---

# 14. Spring Boot Dockerfile

## 14.1 Simple Spring Boot Dockerfile

### [개념]

Spring Boot Dockerfile은 Boot Jar를 Java Runtime Image에 복사하고 `java -jar`로 실행하는 구조이다.

```text
Spring Boot Source
→ bootJar
→ Dockerfile
→ Java Runtime Image
→ Container Run
```

---

### [핵심]

Spring Boot Dockerfile 핵심:

- Java 21 기준
- Spring Boot 3.x 기준
- Jar Packaging 사용
- Runtime Image는 JRE 사용
- Profile은 Runtime Env로 주입
- Secret은 Dockerfile에 작성 금지
- Actuator Health Check 권장
- Non-root User 고려

기본 구조:

```dockerfile
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY build/libs/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

---

### [실무]

Build:

```bash
./gradlew clean bootJar
```

Docker Build:

```bash
docker build -t festapick-api:1.0.0 .
```

Run:

```bash
docker run \
  --name festapick-api \
  -p 8080:8080 \
  -e SPRING_PROFILES_ACTIVE=prod \
  festapick-api:1.0.0
```

환경변수 주입:

```bash
docker run \
  -e SPRING_DATASOURCE_URL=jdbc:mysql://mysql:3306/festapick \
  -e SPRING_DATASOURCE_USERNAME=app \
  -e SPRING_DATASOURCE_PASSWORD=secret \
  festapick-api:1.0.0
```

---

### [주의]

Host에서 Jar를 Build한 뒤 COPY하는 방식은 단순하지만 Build 환경 의존성이 있다.

주의할 점:

- Jar 파일이 없으면 Docker Build 실패
- `.dockerignore`에서 build 제외 시 COPY 실패
- 로컬 Gradle Version에 영향 받을 수 있음
- 운영 Secret 하드코딩 금지
- DB URL은 Runtime Env로 주입
- Profile은 Runtime Env로 주입
- 운영 배포에는 명확한 Image Tag 사용

---

### [FAQ]

Q. Spring Boot Dockerfile 기본 구조는?
A. Java Runtime Image를 Base로 사용하고 Boot Jar를 복사한 뒤 `java -jar app.jar`로 실행한다.

Q. Spring Boot Profile은 Dockerfile에 고정해야 하는가?
A. 권장하지 않는다. `SPRING_PROFILES_ACTIVE`를 Runtime 환경변수로 주입하는 것이 좋다.

Q. Jar 파일이 없다는 Build 오류는 왜 발생하는가?
A. `./gradlew bootJar`가 실행되지 않았거나 `.dockerignore`에서 build 디렉터리를 제외했을 수 있다.

---

## 14.2 Multi-stage Spring Boot Dockerfile

### [개념]

Multi-stage Dockerfile은 Build Stage와 Runtime Stage를 분리하여 최종 Image를 작게 만드는 방식이다.

```text
Builder Stage
→ Gradle Build
→ Boot Jar
→ Runtime Stage
→ Copy Jar Only
→ Final Image
```

---

### [핵심]

Multi-stage 핵심:

- Build 도구와 Runtime 분리
- 최종 Image Size 감소
- 보안 공격면 감소
- CI/CD 재현성 향상
- Build Artifact만 Runtime Image에 포함
- 운영 Image에 Gradle / Source Code 제거
- Build Stage와 Runtime Stage 책임 분리

---

### [실무]

Spring Boot Multi-stage Dockerfile:

```dockerfile
FROM gradle:8.10-jdk21 AS builder
WORKDIR /app

COPY build.gradle settings.gradle ./
COPY gradle ./gradle
COPY src ./src

RUN gradle clean bootJar --no-daemon

FROM eclipse-temurin:21-jre AS runtime
WORKDIR /app

COPY --from=builder /app/build/libs/*.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
```

Build:

```bash
docker build -t festapick-api:1.0.0 .
```

장점:

- 로컬 Gradle 설치 불필요
- Build 환경 표준화
- Runtime Image 경량화
- CI/CD에 적합

---

### [주의]

Multi-stage Build에서 Gradle Cache를 고려하지 않으면 Build가 느릴 수 있다.

주의할 점:

- `gradle dependencies` Cache 최적화 고려
- Wrapper 사용 여부 결정
- Test 실행 여부 결정
- Build Stage와 Runtime Stage의 Java Version 일치
- 최종 Image에 Source Code 포함 여부 확인
- `.dockerignore`로 불필요 파일 제외
- Runtime Stage에 Build Tool이 남지 않는지 확인

---

### [FAQ]

Q. Multi-stage Build란?
A. Build Stage와 Runtime Stage를 분리하여 최종 Image에 실행에 필요한 파일만 포함하는 Docker Build 방식이다.

Q. Spring Boot에서 Multi-stage Build를 왜 사용하는가?
A. Gradle, JDK, Source Code를 최종 Image에서 제거하여 Image Size와 보안 위험을 줄이기 위해 사용한다.

Q. Multi-stage Build는 CI/CD에 적합한가?
A. 적합하다. Build 환경을 Dockerfile 안에 고정하여 재현성을 높일 수 있다.

---

# 15. Dockerfile Troubleshooting

## 15.1 Common Dockerfile Problems

### [개념]

Dockerfile Troubleshooting은 Build 실패, Runtime 실패, Permission 문제, Port 문제, Secret 문제를 원인별로 분석하는 과정이다.

```text
Problem
→ Dockerfile Check
→ Build Log Check
→ Image Inspect
→ Container Logs
→ Fix
```

---

### [핵심]

대표 문제:

| Problem           | Cause               | Check          |
| ----------------- | ------------------- | -------------- |
| COPY failed       | 파일 경로 오류      | Build Context  |
| Jar not found     | Build Artifact 없음 | build/libs     |
| Permission denied | USER 권한 문제      | chown / chmod  |
| Container exits   | ENTRYPOINT 오류     | docker logs    |
| Port unreachable  | Port Mapping 없음   | docker run -p  |
| curl not found    | Runtime Tool 없음   | Image Package  |
| Secret exposed    | ENV / COPY 사용     | docker history |
| Slow build        | Cache 비효율        | COPY 순서      |
| Large image       | Multi-stage 미사용  | docker images  |

---

### [실무]

Build Context 확인:

```bash
docker build -t app:1.0 .
```

상세 로그:

```bash
docker build --no-cache -t app:1.0 .
```

Container 로그 확인:

```bash
docker logs app
```

Image History 확인:

```bash
docker history app:1.0
```

Container 설정 확인:

```bash
docker inspect app
```

ENTRYPOINT Override Debug:

```bash
docker run --rm -it --entrypoint sh app:1.0
```

---

### [주의]

`--no-cache`는 문제 분석에 유용하지만 항상 사용하는 것은 비효율적이다.

주의할 점:

- Build 실패와 Runtime 실패 구분
- Dockerfile 경로와 Build Context 경로 구분
- `.dockerignore` 영향 확인
- ENV / ARG Secret 노출 확인
- ENTRYPOINT Exec Form 확인
- Container 내부 수동 수정으로 해결하지 않기
- 로그 없이 추측하지 않기

---

### [FAQ]

Q. COPY failed 오류는 왜 발생하는가?
A. 복사하려는 파일이 Build Context에 없거나 `.dockerignore`에 의해 제외되었기 때문이다.

Q. Container가 실행 직후 종료되는 이유는?
A. ENTRYPOINT 또는 CMD로 실행된 Main Process가 종료되었기 때문이다.

Q. Permission denied는 어떻게 해결하는가?
A. 파일 소유자와 권한을 확인하고 `chown`, `chmod`, `USER` 설정을 조정해야 한다.

Q. Port가 열리지 않는 이유는?
A. EXPOSE만 작성하고 `docker run -p` 또는 Compose `ports`를 설정하지 않았을 수 있다.

---

# 16. Dockerfile Best Practice

## 16.1 Dockerfile Best Practice

### [개념]

Dockerfile Best Practice는 Image Size, Build Speed, Security, Reproducibility, Runtime Stability를 개선하기 위한 작성 기준이다.

Dockerfile 품질은 Docker 문서 품질과 DevOps Agent의 Containerization 품질을 결정한다.

---

### [핵심]

Dockerfile Best Practice:

- 명확한 Base Image Version 사용
- `latest` 단독 사용 지양
- `.dockerignore` 작성
- Secret 하드코딩 금지
- Layer Cache 최적화
- Multi-stage Build 사용
- Runtime Image 최소화
- Non-root User 사용
- Exec Form ENTRYPOINT 사용
- EXPOSE로 Port 문서화
- HEALTHCHECK 추가
- LABEL로 Metadata 관리
- 불필요 Package 설치 금지
- Package Cache 정리
- Build Time과 Runtime 구분
- Container 내부 수동 수정 금지

---

### [실무]

권장 Spring Boot Dockerfile:

```dockerfile
FROM gradle:8.10-jdk21 AS builder
WORKDIR /app

COPY build.gradle settings.gradle ./
COPY gradle ./gradle
COPY src ./src

RUN gradle clean bootJar --no-daemon

FROM eclipse-temurin:21-jre AS runtime
WORKDIR /app

RUN useradd -r -u 1001 appuser

COPY --from=builder /app/build/libs/*.jar app.jar

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --retries=3 --start-period=30s \
  CMD wget -qO- http://localhost:8080/actuator/health || exit 1

ENTRYPOINT ["java", "-jar", "app.jar"]
```

실무 Checklist:

- Base Image Version 명확한가?
- Build Stage와 Runtime Stage가 분리되었는가?
- Secret이 Dockerfile에 없는가?
- `.dockerignore`가 있는가?
- Jar / Artifact 경로가 정확한가?
- Non-root User로 실행되는가?
- Port가 문서화되었는가?
- Health Check가 있는가?
- ENTRYPOINT가 Exec Form인가?
- Runtime Env 주입 구조인가?

---

### [주의]

Best Practice는 상황에 따라 조정한다.

예외 가능:

- 학습용 Dockerfile은 단순 구조 가능
- 로컬 개발용은 Root 실행 가능
- Health Check는 Compose 또는 Orchestrator에서 정의 가능
- Multi-stage Build가 항상 필수는 아님
- 작은 개인 프로젝트는 단순 Dockerfile로 시작 가능

그러나 운영 기준에서는 보안, 재현성, 관측 가능성을 우선한다.

---

### [FAQ]

Q. 좋은 Dockerfile의 기준은?
A. 작고, 빠르게 Build되고, Secret을 포함하지 않으며, Runtime이 안정적이고, 재현 가능한 Dockerfile이다.

Q. Dockerfile에서 가장 중요한 Instruction은?
A. FROM, COPY, RUN, ENTRYPOINT가 핵심이며 Spring Boot에서는 Multi-stage Build와 Runtime Env 주입도 중요하다.

Q. 운영 Dockerfile에서 반드시 피해야 할 것은?
A. Secret 하드코딩, latest 단독 사용, Root User 실행, 불필요한 Build Tool 포함, Container 내부 수동 수정이다.

---

# Retrieval Queries

### [FAQ]

Q. Dockerfile이란 무엇인가?
A. Dockerfile은 Docker Image를 Build하기 위한 명세 파일이다.

Q. Dockerfile은 왜 필요한가?
A. Application 실행 환경을 코드로 정의하고 Image Build와 배포 재현성을 확보하기 위해 필요하다.

Q. FROM은 무엇인가?
A. FROM은 Dockerfile의 Base Image를 지정하는 Instruction이다.

Q. WORKDIR은 무엇인가?
A. WORKDIR은 Dockerfile 명령이 실행될 Container 내부 작업 디렉터리를 지정한다.

Q. COPY는 무엇인가?
A. COPY는 Build Context의 파일을 Docker Image 내부로 복사하는 Instruction이다.

Q. ADD와 COPY 차이는 무엇인가?
A. COPY는 단순 파일 복사이고 ADD는 복사 외에 Tar 압축 해제와 URL 처리 기능이 있다.

Q. RUN은 언제 실행되는가?
A. RUN은 Docker Image Build 단계에서 실행된다.

Q. RUN과 CMD 차이는 무엇인가?
A. RUN은 Build Time 명령이고 CMD는 Container Runtime 기본 명령 또는 기본 인자이다.

Q. ENV는 무엇인가?
A. ENV는 Image와 Container에서 사용할 환경변수를 설정하는 Instruction이다.

Q. ARG는 무엇인가?
A. ARG는 Docker Image Build 시점에 사용할 Build Argument이다.

Q. ENV와 ARG 차이는 무엇인가?
A. ENV는 Runtime 환경변수로 사용할 수 있고 ARG는 Build Time 변수이다.

Q. EXPOSE는 Port를 실제로 여는가?
A. 아니다. EXPOSE는 Port를 문서화할 뿐이며 실제 Port Mapping은 docker run -p 또는 Compose ports로 설정한다.

Q. ENTRYPOINT는 무엇인가?
A. ENTRYPOINT는 Container 시작 시 실행할 기본 명령을 지정하는 Instruction이다.

Q. CMD는 무엇인가?
A. CMD는 Container 실행 시 사용할 기본 명령 또는 기본 인자를 지정하는 Instruction이다.

Q. ENTRYPOINT와 CMD 차이는 무엇인가?
A. ENTRYPOINT는 실행 명령 고정에 적합하고 CMD는 Override 가능한 기본 인자 제공에 적합하다.

Q. USER는 무엇인가?
A. USER는 Container 내부에서 명령을 실행할 사용자를 지정하는 Instruction이다.

Q. HEALTHCHECK는 무엇인가?
A. HEALTHCHECK는 Container 내부에서 Application 상태를 확인하는 Instruction이다.

Q. LABEL은 무엇인가?
A. LABEL은 Docker Image에 Version, Commit, Maintainer 같은 Metadata를 추가하는 Instruction이다.

Q. .dockerignore는 무엇인가?
A. .dockerignore는 Docker Build Context에서 제외할 파일과 디렉터리를 지정하는 파일이다.

Q. .dockerignore를 왜 사용하는가?
A. Build 속도 개선, Image Size 감소, Secret 노출 방지를 위해 사용한다.

Q. Docker Layer Cache는 무엇인가?
A. Dockerfile Instruction 결과를 Layer로 저장하고 변경되지 않은 Layer를 재사용하는 Build 최적화 기능이다.

Q. Dockerfile Cache 최적화 방법은?
A. 변경이 적은 Dependency 파일을 먼저 COPY하고 자주 바뀌는 Source Code를 나중에 COPY한다.

Q. Spring Boot Dockerfile 기본 구조는?
A. Java Runtime Image를 Base로 사용하고 Boot Jar를 복사한 뒤 java -jar app.jar로 실행한다.

Q. Spring Boot Profile은 Dockerfile에 고정하는가?
A. 권장하지 않는다. SPRING_PROFILES_ACTIVE를 Runtime 환경변수로 주입하는 것이 좋다.

Q. Multi-stage Build란 무엇인가?
A. Build Stage와 Runtime Stage를 분리하여 최종 Image에 실행에 필요한 파일만 포함하는 Docker Build 방식이다.

Q. Spring Boot에서 Multi-stage Build를 왜 사용하는가?
A. Gradle, JDK, Source Code를 최종 Image에서 제거하여 Image Size와 보안 위험을 줄이기 위해 사용한다.

Q. COPY failed 오류는 왜 발생하는가?
A. 복사하려는 파일이 Build Context에 없거나 .dockerignore에 의해 제외되었기 때문이다.

Q. Container가 바로 종료되는 이유는?
A. ENTRYPOINT 또는 CMD로 실행된 Main Process가 종료되었기 때문이다.

Q. Dockerfile에서 Secret을 어디에 쓰면 안 되는가?
A. ENV, ARG, COPY, LABEL, RUN에 Secret을 하드코딩하면 안 된다.

Q. 좋은 Dockerfile의 기준은 무엇인가?
A. 작고 빠르게 Build되며 Secret을 포함하지 않고 Runtime이 안정적이며 재현 가능한 Dockerfile이다.

Q. 운영 Dockerfile에서 피해야 할 것은?
A. latest 단독 사용, Secret 하드코딩, Root User 실행, 불필요한 Build Tool 포함, Container 내부 수동 수정이다.
