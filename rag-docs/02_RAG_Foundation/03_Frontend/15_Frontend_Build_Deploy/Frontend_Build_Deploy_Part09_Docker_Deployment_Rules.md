# Frontend Build & Deploy Part09 - Docker Deployment Rules

---

# 1. Docker Deployment Core

## 1.1 Docker Deployment Definition

### [개념]

Docker Deployment는 프론트엔드 Build 결과물과 배포 서버를 Docker Image로 패키징하거나, Docker Compose로 프론트엔드 / 백엔드 / 프록시 서버를 함께 실행하는 배포 방식이다.

대표 구조:

```text
React Source Code
→ Docker Build
→ Frontend Build Stage
→ Static Hosting Stage
→ Container Run
→ Browser Access
```

또는:

```text
Browser
→ Nginx Container
→ React Static Files

Browser
→ Nginx Container /api
→ Backend Container
→ Database Container
```

---

### [핵심]

Docker 배포 핵심 규칙:

- 브라우저는 Docker 내부 service name을 직접 알 수 없다.
- Docker 내부 service name은 컨테이너끼리 통신할 때 사용한다.
- React SPA 환경 변수는 대부분 Build 시점에 주입된다.
- `docker run -e`만으로 이미 Build된 React JS bundle 값이 바뀌지 않을 수 있다.
- 프론트엔드 컨테이너는 보통 Nginx로 정적 파일을 제공한다.
- `/api` 요청은 Nginx가 backend container로 proxy하는 구조가 일반적이다.
- frontend image build와 container runtime env를 구분해야 한다.
- Docker Compose network 안에서 service name을 proxy target으로 사용할 수 있다.
- 운영에서는 HTTPS, cache, log, restart policy를 함께 고려해야 한다.

---

### [실무]

2026 실무 기준으로 React SPA Docker 배포는 보통 Multi-stage Dockerfile + Nginx static hosting 구조를 사용한다.

기본 Flow:

```text
Docker build stage
→ npm ci
→ npm run build
→ dist/build 생성

Docker runtime stage
→ Nginx image
→ Build Output 복사
→ Nginx로 정적 파일 제공
→ /api proxy
```

Agent 판단 Flow:

```text
Build Tool 확인
→ Output Directory 확인
→ Dockerfile stage 확인
→ Nginx root 확인
→ runtime env 필요 여부 확인
→ /api proxy 확인
→ Docker Compose network 확인
→ browser 기준 URL 확인
```

---

### [FAQ]

Q. Docker Deployment란 무엇인가?
A. 프론트엔드 Build 결과물과 실행 서버를 Docker Image로 패키징하거나 Compose로 여러 서비스를 함께 실행하는 배포 방식이다.

Q. React Docker 배포에서 가장 흔한 구조는 무엇인가?
A. Multi-stage Dockerfile로 React를 Build한 뒤 Nginx로 정적 파일을 제공하는 구조다.

Q. 브라우저에서 Docker service name을 API URL로 써도 되는가?
A. 안 된다. 브라우저는 Docker 내부 service name을 알 수 없다.

Q. Docker 배포에서 가장 중요한 구분은 무엇인가?
A. Build-time env와 Runtime env, 그리고 브라우저 기준 URL과 컨테이너 내부 URL을 구분하는 것이다.

---

## 1.2 Docker Deployment Decision Criteria

### [개념]

Docker Deployment Decision Criteria는 React 프로젝트를 Docker로 배포하는 것이 적합한지 판단하는 기준이다.

---

### [핵심]

Docker 배포가 적합한 경우:

```text
프론트엔드 / 백엔드 / DB를 함께 실행
Docker Compose 기반 개발 / 배포
Nginx reverse proxy 사용
환경 재현성 필요
CI/CD image build 필요
서버 환경 차이 최소화
컨테이너 기반 운영 예정
```

Docker 배포가 과한 경우:

```text
단순 정적 페이지
Vercel / Netlify로 충분한 프로젝트
학원 발표용 단일 Spring Boot 통합 배포가 더 쉬운 경우
Docker / Nginx / network 설정 경험이 부족한 경우
서버 운영이 필요 없는 경우
```

---

### [실무]

2026 실무 기준으로 Docker는 재현성과 서비스 조합에는 강하지만, 단순 프론트엔드 배포만 필요할 때는 Vercel / Netlify가 더 간단할 수 있다.

선택 Flow:

```text
정적 React만 빠르게 배포
→ Vercel / Netlify / S3 고려

React + Spring Boot + MySQL을 한 서버에서 관리
→ Docker Compose 고려

Nginx gateway 필요
→ Docker + Nginx 적합

학원 발표 단순 시연
→ Spring Boot 통합 배포와 비교
```

PM Agent 판단 기준:

```text
운영 목적
→ 데모 / 포트폴리오 / 실제 운영

서비스 구성
→ FE / BE / DB / Nginx 필요 여부

환경 재현성
→ Docker 필요 여부

배포 난이도
→ 팀원이 Docker를 다룰 수 있는가

환경 변수 전략
→ build-time / runtime 구분 가능한가
```

---

### [FAQ]

Q. Docker 배포는 언제 적합한가?
A. 프론트엔드, 백엔드, DB, Nginx를 함께 관리하거나 환경 재현성이 중요할 때 적합하다.

Q. React만 배포하는데 Docker가 꼭 필요한가?
A. 아니다. 단순 정적 배포라면 Vercel, Netlify, S3 같은 플랫폼이 더 간단할 수 있다.

Q. 학원 프로젝트에서 Docker 배포를 써도 되는가?
A. 가능하지만 발표 안정성이 목적이라면 Spring Boot 통합 배포나 플랫폼 배포가 더 단순할 수 있다.

Q. Docker 배포의 가장 큰 장점은 무엇인가?
A. 실행 환경을 이미지로 고정해 서버와 개발 환경 차이를 줄일 수 있다는 점이다.

---

# 2. Frontend Dockerfile

## 2.1 Multi-stage Dockerfile

### [개념]

Multi-stage Dockerfile은 Build 단계와 Runtime 단계를 분리해 최종 이미지에는 Build 결과물과 실행 서버만 포함하는 Dockerfile 작성 방식이다.

---

### [핵심]

Multi-stage 구성:

```text
Stage 1: build
→ Node.js image
→ dependency install
→ npm run build
→ dist/build 생성

Stage 2: runtime
→ Nginx image
→ Build Output 복사
→ Nginx 실행
```

장점:

- 최종 이미지 크기 감소
- Node.js 개발 의존성 제거
- 정적 파일만 Nginx로 제공
- 운영 이미지 단순화
- CI/CD에 적합

---

### [실무]

Vite Dockerfile 예:

```dockerfile
FROM node:20-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

CRA Dockerfile 예:

```dockerfile
FROM node:20-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

Agent 검토 기준:

```md
- [ ] Build stage와 runtime stage가 분리되어 있는가?
- [ ] package lock 기준 install을 사용하는가?
- [ ] Vite는 `/app/dist`를 복사하는가?
- [ ] CRA는 `/app/build`를 복사하는가?
- [ ] Nginx 설정 파일이 포함되는가?
- [ ] 최종 image에 source code와 node_modules가 불필요하게 포함되지 않는가?
```

---

### [FAQ]

Q. Multi-stage Dockerfile이란 무엇인가?
A. Build 단계와 Runtime 단계를 분리해 최종 이미지에는 실행에 필요한 결과물만 포함하는 방식이다.

Q. React Docker Image에 Node.js가 꼭 남아 있어야 하는가?
A. 일반 정적 SPA 배포에서는 필요 없다. Build 후 Nginx만 있어도 된다.

Q. Vite Dockerfile에서 무엇을 복사해야 하는가?
A. Build stage의 `/app/dist`를 Nginx root로 복사한다.

Q. CRA Dockerfile에서 무엇을 복사해야 하는가?
A. Build stage의 `/app/build`를 Nginx root로 복사한다.

---

## 2.2 Docker Build Context

### [개념]

Docker Build Context는 `docker build` 명령 실행 시 Docker Daemon에 전달되는 파일 범위다.

---

### [핵심]

Build Context 기준:

- Dockerfile 위치와 build context를 구분한다.
- frontend 폴더에서 build하면 context는 frontend 기준이다.
- monorepo에서는 context path를 명확히 지정해야 한다.
- `.dockerignore`로 불필요한 파일을 제외한다.
- context가 잘못되면 package.json 또는 source file을 찾지 못한다.
- context가 너무 크면 build가 느려진다.

---

### [실무]

frontend 폴더 내부 Dockerfile:

```bash
cd frontend
docker build -t my-frontend .
```

root에서 frontend Dockerfile 지정:

```bash
docker build -t my-frontend -f frontend/Dockerfile frontend
```

잘못된 예:

```bash
docker build -t my-frontend -f frontend/Dockerfile .
```

위 방식은 context가 project root가 되어 의도하지 않은 파일까지 포함될 수 있다.

Agent 검토 Flow:

```text
Dockerfile 위치 확인
→ package.json 위치 확인
→ build context 확인
→ COPY 경로 확인
→ .dockerignore 확인
```

---

### [FAQ]

Q. Docker Build Context란 무엇인가?
A. Docker build 시 Docker Daemon에 전달되는 파일 범위다.

Q. Dockerfile은 frontend에 있는데 root에서 build해도 되는가?
A. 가능하지만 `-f`와 context path를 정확히 지정해야 한다.

Q. build context가 틀리면 어떤 문제가 생기는가?
A. package.json을 못 찾거나 불필요한 파일이 이미지에 포함될 수 있다.

Q. Docker build가 너무 느리면 무엇을 확인해야 하는가?
A. build context 크기와 `.dockerignore` 설정을 확인해야 한다.

---

## 2.3 Dockerignore Rules

### [개념]

`.dockerignore`는 Docker build context에서 제외할 파일과 폴더를 지정하는 파일이다.

Docker build context에 불필요한 파일이 포함되면 build가 느려지고, 민감 정보나 오래된 Build Output이 image에 포함될 위험이 생긴다.

---

### [핵심]

제외 권장 대상:

```text
node_modules
dist
build
.git
coverage
.env
.env.local
.env.*.local
npm-debug.log
yarn-error.log
pnpm-debug.log
.DS_Store
.vscode
.idea
```

상황에 따라 제외 여부를 판단할 대상:

```text
Dockerfile
docker-compose.yml
README.md
*.md
```

주의:

- `node_modules`는 image 안에서 lock file 기준으로 새로 설치하는 것이 일반적이다.
- 기존 `dist` / `build`를 context에 포함하면 오래된 Build Output이 image에 혼입될 수 있다.
- `.env`는 Secret 노출 위험이 있으므로 build context에서 제외하는 것이 안전하다.
- `.env.example`은 Secret이 없는 템플릿이면 포함 가능하다.
- `Dockerfile`은 build에 직접 복사할 필요가 없는 경우가 많지만, 무조건 제외 대상은 아니다.
- `docker-compose.yml`은 image build에는 보통 필요 없지만, 프로젝트 정책에 따라 제외 여부를 결정한다.
- 문서 파일은 image 크기 최적화 관점에서는 제외 가능하지만, 디버깅 / 추적 정책에 따라 포함할 수도 있다.

---

### [실무]

프론트엔드 `.dockerignore` 기본 예:

```dockerignore
node_modules
dist
build
.git
coverage
.env
.env.local
.env.*.local
npm-debug.log
yarn-error.log
pnpm-debug.log
.DS_Store
.vscode
.idea
```

더 엄격한 image 최적화 예:

```dockerignore
node_modules
dist
build
.git
coverage
.env
.env.local
.env.*.local
npm-debug.log
yarn-error.log
pnpm-debug.log
.DS_Store
.vscode
.idea
README.md
docs
*.md
```

단, 아래 항목은 팀 정책에 따라 결정한다.

```dockerignore
Dockerfile
docker-compose.yml
```

권장 판단 기준:

```text
민감 정보인가?
→ 제외

build 결과물인가?
→ 제외

로컬 의존성인가?
→ 제외

image 실행에 필요 없는 문서인가?
→ 상황에 따라 제외

Docker build 자체에 필요 없는 설정 파일인가?
→ 상황에 따라 제외

추적성 / 디버깅에 도움이 되는 파일인가?
→ 포함 가능
```

Agent 검토 기준:

```md
- [ ] node_modules가 제외되어 있는가?
- [ ] dist/build가 제외되어 있는가?
- [ ] .env 파일이 제외되어 있는가?
- [ ] 불필요한 로그와 coverage가 제외되어 있는가?
- [ ] build context 크기가 과도하지 않은가?
- [ ] Dockerfile / docker-compose.yml 제외 여부가 팀 정책에 맞는가?
- [ ] .env.example에 실제 Secret이 없는가?
```

---

### [FAQ]

Q. .dockerignore는 왜 필요한가?
A. 불필요하거나 민감한 파일이 build context와 image에 포함되는 것을 막기 위해 필요하다.

Q. node_modules를 Docker image에 복사해도 되는가?
A. 권장하지 않는다. image 내부에서 lock file 기준으로 설치하는 것이 재현성에 좋다.

Q. dist나 build 폴더를 .dockerignore에 넣어도 되는가?
A. 보통 넣는 것이 좋다. Docker build 안에서 새로 생성해야 오래된 결과물 혼입을 막을 수 있다.

Q. .env 파일을 Docker build context에 포함해도 되는가?
A. 권장하지 않는다. Secret 노출 위험이 있다.

Q. Dockerfile을 .dockerignore에 반드시 넣어야 하는가?
A. 아니다. image에 복사할 필요는 보통 없지만, 무조건 제외해야 하는 파일은 아니다.

Q. docker-compose.yml을 .dockerignore에 반드시 넣어야 하는가?
A. 아니다. image build에 필요 없는 경우가 많지만, 팀 정책과 디버깅 기준에 따라 결정한다.

Q. README.md나 문서 파일은 제외해야 하는가?
A. image 크기 최적화가 중요하면 제외할 수 있지만, 추적성과 디버깅을 위해 남겨도 된다.

Q. .env.example은 제외해야 하는가?
A. 실제 Secret이 없다면 포함 가능하다. 단, 예시 파일에 실제 key나 password가 들어가면 안 된다.

---

# 3. Docker Environment Variables

## 3.1 Build-time Env in Docker

### [개념]

Build-time Env in Docker는 Docker image를 build하는 시점에 React Build 과정에 주입되는 환경 변수다.

React SPA에서는 Vite / CRA 환경 변수가 대부분 Build 시점에 JS bundle에 포함된다.

---

### [핵심]

Build-time Env 특징:

- `docker build` 시점에 반영된다.
- JS bundle에 값이 포함될 수 있다.
- image build 후 `docker run -e`로 바뀌지 않을 수 있다.
- Secret을 넣으면 image layer 또는 JS bundle에 노출될 수 있다.
- 환경별 image를 따로 build할 때 사용 가능하다.

Dockerfile 관련 문법:

```dockerfile
ARG VITE_API_BASE_URL
ENV VITE_API_BASE_URL=$VITE_API_BASE_URL
RUN npm run build
```

---

### [실무]

Vite Build-time env 예:

```dockerfile
FROM node:20-alpine AS build

WORKDIR /app
COPY package*.json ./
RUN npm ci

COPY . .

ARG VITE_API_BASE_URL
ENV VITE_API_BASE_URL=$VITE_API_BASE_URL

RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
```

Build 명령:

```bash
docker build \
  --build-arg VITE_API_BASE_URL=https://api.example.com \
  -t my-frontend .
```

CRA 예:

```bash
docker build \
  --build-arg REACT_APP_API_BASE_URL=https://api.example.com \
  -t my-frontend .
```

Agent 판단 기준:

```text
React env가 Build-time인지 확인
→ Docker ARG 사용 여부 확인
→ Secret 포함 여부 확인
→ image 재빌드 필요성 확인
```

---

### [FAQ]

Q. Docker에서 React env는 언제 반영되는가?
A. 일반적으로 `npm run build`가 실행되는 Docker build 시점에 반영된다.

Q. docker run -e로 VITE_API_BASE_URL을 바꾸면 React 앱에 반영되는가?
A. Build-time env 방식에서는 이미 생성된 JS bundle 값이 바뀌지 않을 수 있다.

Q. Docker ARG에 Secret을 넣어도 되는가?
A. 안 된다. image layer나 JS bundle에 노출될 수 있다.

Q. API URL이 바뀌면 Docker image를 다시 build해야 하는가?
A. Build-time env 방식이면 다시 build해야 한다.

---

## 3.2 Runtime Config in Docker

### [개념]

Runtime Config in Docker는 Docker container 실행 시점의 환경 변수를 사용해 `config.json` 같은 공개 설정 파일을 생성하고, React 앱이 이를 읽는 방식이다.

---

### [핵심]

Runtime Config가 필요한 상황:

```text
하나의 frontend image를 여러 환경에 배포
실행 시점에 API URL 변경 필요
Docker Compose env로 API URL 제어
재빌드 없이 public config 변경 필요
Kubernetes / cloud runtime env 사용
```

주의:

- Runtime Config도 브라우저에서 접근 가능하다.
- Secret 저장 금지
- 앱 초기화 전에 config를 로드해야 한다.
- `config.json` 캐시를 짧게 설정해야 한다.
- API client 생성 시 config loading 순서를 보장해야 한다.

---

### [실무]

entrypoint script 예:

```sh
#!/bin/sh

cat <<EOF > /usr/share/nginx/html/config.json
{
  "apiBaseUrl": "${API_BASE_URL}",
  "appEnv": "${APP_ENV}"
}
EOF

exec nginx -g "daemon off;"
```

Dockerfile 예:

```dockerfile
FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh

CMD ["/docker-entrypoint.sh"]
```

React config loading 예:

```js
export async function loadRuntimeConfig() {
  const response = await fetch("/config.json", { cache: "no-store" });

  if (!response.ok) {
    throw new Error("Failed to load runtime config");
  }

  return response.json();
}
```

Agent 판단 Flow:

```text
환경별 image 재빌드가 부담인가?
→ Runtime Config 고려

Secret을 넣으려는가?
→ 금지

config.json cache 정책 있는가?
→ no-store 또는 짧은 cache 필요
```

---

### [FAQ]

Q. Runtime Config in Docker란 무엇인가?
A. 컨테이너 실행 시점 env로 config.json을 생성하고 React 앱이 이를 읽는 방식이다.

Q. Runtime Config를 쓰면 image를 다시 build하지 않아도 되는가?
A. public 설정 값만 바꾸는 경우 재빌드 없이 처리할 수 있다.

Q. Runtime Config에 Secret을 넣어도 되는가?
A. 안 된다. config.json은 브라우저에서 접근 가능하다.

Q. Runtime Config 사용 시 가장 주의할 점은 무엇인가?
A. 앱 초기화 전에 config를 로드하고 config.json 캐시를 관리해야 한다.

---

## 3.3 Build-time vs Runtime Env

### [개념]

Build-time Env와 Runtime Env는 환경 변수가 적용되는 시점이 다르다.

---

### [핵심]

비교:

| 구분           | Build-time Env               | Runtime Env              |
| -------------- | ---------------------------- | ------------------------ |
| 적용 시점      | docker build / npm run build | container run            |
| React SPA 반영 | JS bundle에 포함             | 별도 config 필요         |
| 변경 시        | image rebuild 필요           | container restart 가능   |
| Secret 사용    | 금지                         | frontend config에는 금지 |
| 대표 방식      | ARG + npm run build          | config.json 생성         |

핵심 원칙:

```text
React SPA 코드에 직접 들어가는 env
→ Build-time 가능성 높음

Nginx container 실행 env
→ React JS bundle을 자동 변경하지 않음

실행 시점 변경 필요
→ Runtime Config 필요
```

---

### [실무]

오해 예:

```yaml
frontend:
  image: my-frontend
  environment:
    VITE_API_BASE_URL: https://api.example.com
```

위 설정만으로 이미 build된 React bundle의 API URL이 바뀌지 않을 수 있다.

정확한 판단:

```text
VITE_API_BASE_URL을 React 코드에서 import.meta.env로 읽음
→ build 시점 값 필요

API_BASE_URL로 config.json 생성
→ runtime env 반영 가능
```

Agent 검토 기준:

```text
env 이름 확인
→ React 코드 접근 방식 확인
→ Dockerfile RUN npm run build 위치 확인
→ docker-compose environment 의미 확인
→ Runtime Config 사용 여부 확인
```

---

### [FAQ]

Q. Build-time Env와 Runtime Env는 같은가?
A. 아니다. Build-time은 build 시점, Runtime은 container 실행 시점에 적용된다.

Q. docker-compose environment에 VITE_API_BASE_URL을 넣으면 React 코드가 바뀌는가?
A. 일반 Build-time 방식에서는 바뀌지 않을 수 있다.

Q. Docker에서 실행 시점 API URL 변경이 필요하면 어떻게 해야 하는가?
A. Runtime Config 또는 entrypoint에서 config.json 생성 방식을 사용한다.

Q. Build-time Env와 Runtime Config 중 무엇을 선택해야 하는가?
A. 환경별 image를 따로 만들면 Build-time, 하나의 image를 여러 환경에서 쓰면 Runtime Config가 적합하다.

---

# 4. Docker Compose Deployment

## 4.1 Docker Compose Core

### [개념]

Docker Compose는 여러 컨테이너를 하나의 설정 파일로 정의하고 함께 실행하는 도구다.

Frontend Build & Deploy에서는 보통 다음 서비스를 함께 구성한다.

```text
nginx or frontend
backend
database
redis
```

---

### [핵심]

Docker Compose 핵심 규칙:

- service name은 Compose network 내부 DNS 이름이 된다.
- 컨테이너끼리는 service name으로 통신한다.
- 브라우저는 service name을 알 수 없다.
- 외부 공개 port와 내부 container port를 구분한다.
- frontend browser API URL은 `/api` 또는 외부 도메인을 사용한다.
- Nginx proxy target은 `backend:8080` 같은 service name을 사용할 수 있다.
- depends_on은 시작 순서만 보장하고 readiness는 보장하지 않는다.

---

### [실무]

기본 Compose 예:

```yaml
services:
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "80:80"
    depends_on:
      - backend

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    expose:
      - "8080"

  db:
    image: mysql:8
    environment:
      MYSQL_DATABASE: app
      MYSQL_ROOT_PASSWORD: root
```

Nginx proxy:

```nginx
location /api/ {
  proxy_pass http://backend:8080/api/;
}
```

Agent 검토 Flow:

```text
compose services 확인
→ frontend ports 확인
→ backend expose/ports 확인
→ network 확인
→ Nginx proxy_pass service name 확인
→ browser API URL 확인
```

---

### [FAQ]

Q. Docker Compose란 무엇인가?
A. 여러 컨테이너 서비스를 하나의 설정 파일로 정의하고 함께 실행하는 도구다.

Q. Compose service name은 어디서 사용할 수 있는가?
A. 같은 Docker network 안의 컨테이너끼리 통신할 때 사용할 수 있다.

Q. 브라우저에서 backend:8080으로 요청해도 되는가?
A. 안 된다. 브라우저는 Docker 내부 DNS를 알 수 없다.

Q. depends_on은 백엔드 준비 완료까지 보장하는가?
A. 아니다. 시작 순서만 보장하며 readiness는 healthcheck로 별도 처리해야 한다.

---

## 4.2 Frontend Backend Compose Pattern

### [개념]

Frontend Backend Compose Pattern은 Nginx 기반 frontend container가 React 정적 파일을 제공하고 `/api` 요청을 backend container로 proxy하는 구조다.

---

### [핵심]

권장 구조:

```text
Browser
→ http://server

Nginx frontend container
→ static files

Nginx /api
→ backend:8080

Backend
→ db:3306
```

중요 기준:

- Browser API Base URL: `/api`
- Nginx proxy_pass: `http://backend:8080/api/`
- Backend DB URL: `jdbc:mysql://db:3306/app`
- Backend port는 내부 expose만 해도 됨
- 외부에는 frontend Nginx port만 열 수 있음

---

### [실무]

Compose 예:

```yaml
services:
  frontend:
    build:
      context: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend

  backend:
    build:
      context: ./backend
    expose:
      - "8080"
    environment:
      SPRING_DATASOURCE_URL: jdbc:mysql://db:3306/app
      SPRING_DATASOURCE_USERNAME: app
      SPRING_DATASOURCE_PASSWORD: app-password
    depends_on:
      - db

  db:
    image: mysql:8
    environment:
      MYSQL_DATABASE: app
      MYSQL_USER: app
      MYSQL_PASSWORD: app-password
      MYSQL_ROOT_PASSWORD: root-password
```

Frontend env:

```env
VITE_API_BASE_URL=/api
```

---

### [FAQ]

Q. Docker Compose에서 frontend API URL은 무엇이 적합한가?
A. Nginx same-origin proxy를 쓴다면 `/api`가 적합하다.

Q. Nginx proxy_pass에는 backend service name을 써도 되는가?
A. 같은 Compose network 안이라면 `http://backend:8080`처럼 사용할 수 있다.

Q. backend port를 외부에 공개해야 하는가?
A. Nginx가 proxy한다면 외부 공개 없이 `expose`만으로도 가능하다.

Q. DB URL에서 localhost를 써도 되는가?
A. backend container 기준 localhost는 backend 자신이다. DB container는 보통 service name `db`로 접근한다.

---

## 4.3 Compose Ports and Expose

### [개념]

`ports`와 `expose`는 Docker Compose에서 컨테이너 네트워크 접근 범위를 정의하는 설정이다.

---

### [핵심]

`ports`:

```text
host port : container port
외부 브라우저 또는 외부 클라이언트 접근 가능
```

예:

```yaml
ports:
  - "80:80"
```

`expose`:

```text
컨테이너 내부 network에서만 문서화된 port
외부 host에 직접 공개하지 않음
```

예:

```yaml
expose:
  - "8080"
```

---

### [실무]

권장 패턴:

```yaml
frontend:
  ports:
    - "80:80"

backend:
  expose:
    - "8080"

db:
  expose:
    - "3306"
```

의미:

```text
외부 사용자
→ frontend:80 접근

frontend Nginx
→ backend:8080 접근

backend
→ db:3306 접근
```

잘못된 이해:

```text
expose
→ 외부 브라우저 공개 아님
```

---

### [FAQ]

Q. ports와 expose의 차이는 무엇인가?
A. `ports`는 host 외부에 공개하고, `expose`는 Compose network 내부 통신 용도다.

Q. backend를 외부에 공개하지 않아도 frontend에서 호출 가능한가?
A. Nginx가 같은 network 안에서 proxy하면 가능하다.

Q. 브라우저가 expose된 backend port에 접근할 수 있는가?
A. 없다. expose는 외부 공개가 아니다.

Q. ports를 너무 많이 열면 어떤 문제가 있는가?
A. 불필요한 서비스가 외부에 노출되어 보안 위험이 커질 수 있다.

---

## 4.4 Compose Network Rules

### [개념]

Compose Network는 Docker Compose 서비스들이 서로 service name으로 통신할 수 있게 하는 내부 네트워크다.

---

### [핵심]

Network 규칙:

- 같은 Compose project의 서비스는 기본 network에 연결된다.
- service name은 내부 DNS 이름이 된다.
- container name을 고정하지 않아도 service name으로 통신 가능하다.
- 브라우저는 이 network에 접근하지 못한다.
- 여러 network를 나누면 통신 가능 범위를 제한할 수 있다.

---

### [실무]

기본 network 사용:

```yaml
services:
  frontend:
    build: ./frontend

  backend:
    build: ./backend
```

명시적 network:

```yaml
services:
  frontend:
    networks:
      - app-network

  backend:
    networks:
      - app-network
      - db-network

  db:
    networks:
      - db-network

networks:
  app-network:
  db-network:
```

검증 명령:

```bash
docker compose ps
docker compose logs frontend
docker compose exec frontend wget -qO- http://backend:8080/api/health
```

---

### [FAQ]

Q. Compose network에서 service name은 무엇인가?
A. 같은 network 내부에서 다른 컨테이너를 찾는 DNS 이름이다.

Q. service name과 container_name 중 무엇을 사용하는 것이 좋은가?
A. 일반적으로 service name을 사용하는 것이 Compose 관리에 적합하다.

Q. Nginx container에서 backend에 접근이 안 되면 무엇을 확인하는가?
A. 같은 network에 있는지, service name이 맞는지, backend port가 열려 있는지 확인한다.

Q. 브라우저가 Compose network에 직접 접근할 수 있는가?
A. 없다. 브라우저는 host port로 노출된 서비스에만 접근한다.

---

# 5. Docker Nginx Rules

## 5.1 Nginx Config in Docker

### [개념]

Nginx Config in Docker는 Docker image 또는 volume mount를 통해 Nginx 설정 파일을 컨테이너 안에 배치하는 방식이다.

대표 경로:

```text
/etc/nginx/conf.d/default.conf
/etc/nginx/nginx.conf
```

---

### [핵심]

Nginx Docker 설정 기준:

- React static root는 `/usr/share/nginx/html`을 자주 사용한다.
- server block은 보통 `/etc/nginx/conf.d/default.conf`에 둔다.
- Dockerfile에서 config를 COPY할 수 있다.
- 개발 중에는 volume mount로 config를 주입할 수 있다.
- 설정 변경 후 image rebuild 또는 volume reload가 필요하다.
- `nginx -t`로 문법 검증이 필요하다.

---

### [실무]

Dockerfile:

```dockerfile
FROM nginx:alpine

COPY dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
```

nginx.conf:

```nginx
server {
  listen 80;

  root /usr/share/nginx/html;
  index index.html;

  location /api/ {
    proxy_pass http://backend:8080/api/;
  }

  location / {
    try_files $uri $uri/ /index.html;
  }
}
```

검증:

```bash
docker exec -it frontend nginx -t
docker logs frontend
```

---

### [FAQ]

Q. Docker Nginx 설정 파일은 어디에 둘 수 있는가?
A. 보통 `/etc/nginx/conf.d/default.conf`에 둔다.

Q. Dockerfile에서 Nginx 설정을 COPY하면 설정 변경 시 무엇이 필요한가?
A. image rebuild가 필요하다.

Q. volume mount로 Nginx 설정을 넣으면 무엇이 필요한가?
A. 컨테이너 reload 또는 재시작이 필요하다.

Q. Docker Nginx 설정 검증은 어떻게 하는가?
A. 컨테이너 내부에서 `nginx -t`를 실행한다.

---

## 5.2 Docker Nginx SPA and API Config

### [개념]

Docker Nginx SPA and API Config는 React 정적 파일 제공, SPA fallback, backend API proxy를 하나의 Nginx container에서 처리하는 설정이다.

---

### [핵심]

필수 구성:

```text
root /usr/share/nginx/html
location /api/ proxy_pass backend
location / try_files fallback
optional location /ws/ websocket proxy
cache header
```

주의:

- `/api` location이 fallback보다 명확해야 한다.
- proxy_pass target은 Docker 내부 service name을 사용할 수 있다.
- 브라우저 API URL은 `/api`를 사용한다.
- backend container가 같은 network에 있어야 한다.
- API 응답이 index.html인지 반드시 검증한다.

---

### [실무]

기본 config:

```nginx
server {
  listen 80;

  root /usr/share/nginx/html;
  index index.html;

  location /api/ {
    proxy_pass http://backend:8080/api/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
  }

  location /ws/ {
    proxy_pass http://backend:8080/ws/;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
  }

  location / {
    try_files $uri $uri/ /index.html;
  }
}
```

검증 Flow:

```text
docker compose up
→ / 접속
→ /login 새로고침
→ /api/health JSON 확인
→ /assets JS 확인
→ /ws 연결 확인
```

---

### [FAQ]

Q. Docker Nginx에서 /api는 어디로 보내야 하는가?
A. 같은 Compose network의 backend service로 proxy하면 된다.

Q. React Docker 배포에서 Browser API URL은 backend:8080이어야 하는가?
A. 아니다. 브라우저는 `/api` 또는 외부 도메인을 호출하고 Nginx가 backend로 proxy해야 한다.

Q. Docker Nginx에서 API가 index.html을 반환하면 무엇을 확인하는가?
A. `/api` location, proxy_pass, fallback 우선순위, backend route를 확인한다.

Q. Docker Nginx에서 WebSocket을 쓰면 무엇을 추가해야 하는가?
A. `/ws` location과 Upgrade header 설정이 필요하다.

---

# 6. Docker Networking and URL Rules

## 6.1 Browser URL vs Container URL

### [개념]

Browser URL과 Container URL은 서로 다른 관점의 주소다.

브라우저는 사용자의 네트워크에서 접근 가능한 주소만 알 수 있고, 컨테이너는 Docker network 내부 service name으로 통신할 수 있다.

---

### [핵심]

Browser 기준 가능:

```text
https://example.com
https://api.example.com
/api
http://localhost:80
```

Browser 기준 불가능:

```text
http://backend:8080
http://db:3306
http://redis:6379
```

Container 기준 가능:

```text
http://backend:8080
mysql://db:3306
redis://redis:6379
```

---

### [실무]

잘못된 프론트엔드 env:

```env
VITE_API_BASE_URL=http://backend:8080/api
```

브라우저에서 실패한다.

권장:

```env
VITE_API_BASE_URL=/api
```

Nginx:

```nginx
location /api/ {
  proxy_pass http://backend:8080/api/;
}
```

판단 Flow:

```text
이 URL을 누가 호출하는가?
→ Browser인가 Container인가

Browser 호출
→ public domain 또는 /api 사용

Container 호출
→ service name 사용 가능
```

---

### [FAQ]

Q. Browser URL과 Container URL은 왜 구분해야 하는가?
A. 브라우저는 Docker 내부 네트워크를 모르고, 컨테이너끼리는 service name으로 통신할 수 있기 때문이다.

Q. React env에 [http://backend:8080을](http://backend:8080을) 넣으면 왜 안 되는가?
A. 그 값은 브라우저에서 실행되며 브라우저는 backend라는 Docker service name을 알 수 없기 때문이다.

Q. 컨테이너끼리는 backend:8080을 사용할 수 있는가?
A. 같은 Docker network라면 가능하다.

Q. 브라우저 API URL은 무엇을 쓰는 것이 좋은가?
A. Nginx same-origin proxy 구조에서는 `/api`가 적합하다.

---

## 6.2 Localhost in Docker

### [개념]

Localhost in Docker는 `localhost`가 실행 위치에 따라 다른 대상을 의미하는 문제다.

---

### [핵심]

`localhost` 의미:

```text
Browser localhost
→ 사용자 PC 또는 접속한 환경

Frontend container localhost
→ frontend container 자신

Backend container localhost
→ backend container 자신

DB connection localhost inside backend
→ backend container 자신
```

대표 실수:

```text
Backend container에서 DB URL localhost:3306 사용
→ backend container 내부를 찾음
→ DB 연결 실패
```

Docker Compose에서는 service name 사용:

```text
jdbc:mysql://db:3306/app
```

---

### [실무]

잘못된 backend env:

```yaml
SPRING_DATASOURCE_URL: jdbc:mysql://localhost:3306/app
```

올바른 backend env:

```yaml
SPRING_DATASOURCE_URL: jdbc:mysql://db:3306/app
```

Frontend 운영 env에서 localhost 금지:

```env
VITE_API_BASE_URL=http://localhost:8080
```

권장:

```env
VITE_API_BASE_URL=/api
```

---

### [FAQ]

Q. Docker에서 localhost는 무엇을 의미하는가?
A. 실행되는 위치 자신을 의미한다. 컨테이너 안에서는 해당 컨테이너 자신이다.

Q. backend container에서 DB를 localhost로 연결해도 되는가?
A. DB가 같은 backend container 안에 있는 것이 아니라면 안 된다. Compose service name을 사용해야 한다.

Q. frontend env에 localhost를 넣으면 운영에서 왜 위험한가?
A. 사용자 브라우저의 localhost로 요청하므로 실제 backend에 도달하지 못한다.

Q. Docker Compose에서 DB host는 보통 무엇을 쓰는가?
A. DB service name인 `db`, `mysql` 같은 이름을 사용한다.

---

# 7. Docker Healthcheck and Startup

## 7.1 Healthcheck Rules

### [개념]

Healthcheck는 컨테이너가 단순히 실행 중인지가 아니라 실제로 요청을 처리할 준비가 되었는지 확인하는 Docker 설정이다.

---

### [핵심]

Healthcheck가 필요한 이유:

- depends_on은 readiness를 보장하지 않는다.
- DB가 준비되기 전에 backend가 시작될 수 있다.
- backend가 준비되기 전에 Nginx proxy 요청이 실패할 수 있다.
- CI/CD와 운영에서 상태 판단에 필요하다.
- 자동 재시작과 장애 감지에 유리하다.

---

### [실무]

Backend health endpoint 예:

```text
/api/health
/actuator/health
```

Compose healthcheck 예:

```yaml
backend:
  build: ./backend
  healthcheck:
    test: ["CMD", "wget", "-qO-", "http://localhost:8080/actuator/health"]
    interval: 10s
    timeout: 5s
    retries: 5
```

DB healthcheck 예:

```yaml
db:
  image: mysql:8
  healthcheck:
    test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
    interval: 10s
    timeout: 5s
    retries: 10
```

검증 Flow:

```text
docker compose ps
→ health 상태 확인
→ backend log 확인
→ frontend /api 호출 확인
```

---

### [FAQ]

Q. Docker healthcheck는 왜 필요한가?
A. 컨테이너가 실제로 요청을 처리할 준비가 되었는지 확인하기 위해 필요하다.

Q. depends_on만으로 충분한가?
A. 아니다. 시작 순서만 보장하고 서비스 준비 완료는 보장하지 않는다.

Q. backend health endpoint는 무엇을 쓰는가?
A. `/actuator/health` 또는 프로젝트 전용 `/api/health`를 사용할 수 있다.

Q. DB 준비 전에 backend가 시작되면 어떻게 되는가?
A. DB 연결 실패로 backend가 crash되거나 초기 요청이 실패할 수 있다.

---

## 7.2 Restart Policy Rules

### [개념]

Restart Policy는 컨테이너가 종료되었을 때 Docker가 자동으로 다시 시작할지 결정하는 설정이다.

---

### [핵심]

대표 설정:

```text
no
always
unless-stopped
on-failure
```

운영 권장:

```text
restart: unless-stopped
```

주의:

- crash loop를 숨길 수 있다.
- log 확인이 필요하다.
- 애플리케이션 오류 자체를 해결하는 것은 아니다.
- DB migration 실패나 env 오류는 재시작해도 해결되지 않는다.

---

### [실무]

Compose 예:

```yaml
services:
  frontend:
    build: ./frontend
    restart: unless-stopped

  backend:
    build: ./backend
    restart: unless-stopped

  db:
    image: mysql:8
    restart: unless-stopped
```

검증 Flow:

```text
docker compose ps
→ Restarting 상태 여부 확인
→ docker compose logs 확인
→ env / port / dependency 문제 확인
```

---

### [FAQ]

Q. restart policy는 왜 필요한가?
A. 컨테이너가 예기치 않게 종료되었을 때 자동 복구하기 위해 필요하다.

Q. restart: always와 unless-stopped 차이는 무엇인가?
A. `unless-stopped`는 사용자가 명시적으로 중지한 경우 자동 재시작하지 않는다.

Q. 컨테이너가 계속 재시작되면 무엇을 확인해야 하는가?
A. application log, env 누락, port 충돌, DB 연결 실패를 확인해야 한다.

Q. restart policy가 오류를 해결해 주는가?
A. 아니다. 재시작만 할 뿐 근본 원인은 로그로 찾아야 한다.

---

# 8. Docker Image and Build Cache

## 8.1 Docker Layer Cache

### [개념]

Docker Layer Cache는 Dockerfile 각 명령의 결과를 layer로 저장해 다음 build에서 재사용하는 기능이다.

---

### [핵심]

Cache 최적화 원칙:

- package.json과 lock file을 먼저 복사한다.
- dependency install layer를 source copy보다 앞에 둔다.
- source code 변경 시 dependency install이 매번 실행되지 않게 한다.
- `.dockerignore`로 불필요한 파일을 제외한다.
- lock file 변경 시 dependency layer가 갱신된다.

---

### [실무]

권장 구조:

```dockerfile
COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build
```

비권장 구조:

```dockerfile
COPY . .
RUN npm install
RUN npm run build
```

문제:

```text
source code가 조금만 바뀌어도 npm install cache가 깨짐
```

검증 Flow:

```text
docker build log 확인
→ npm ci layer cache 여부 확인
→ COPY 순서 확인
→ .dockerignore 확인
```

---

### [FAQ]

Q. Docker Layer Cache란 무엇인가?
A. Dockerfile 명령 결과를 재사용해 build 속도를 높이는 기능이다.

Q. package.json을 먼저 복사하는 이유는?
A. source code 변경 때마다 dependency install이 다시 실행되는 것을 줄이기 위해서다.

Q. COPY . .를 먼저 하면 왜 비효율적인가?
A. 소스 변경만으로도 dependency install layer cache가 깨질 수 있다.

Q. Docker build가 느리면 무엇을 확인해야 하는가?
A. Dockerfile COPY 순서, `.dockerignore`, lock file 변경 여부를 확인해야 한다.

---

## 8.2 Image Tag Rules

### [개념]

Image Tag는 Docker Image 버전을 구분하기 위한 이름표다.

예:

```text
my-frontend:latest
my-frontend:v1.0.0
my-frontend:2026-07-07
my-frontend:git-sha
```

---

### [핵심]

Tag 전략:

- `latest`만 의존하지 않는다.
- 배포 추적을 위해 git sha 또는 version tag를 사용한다.
- rollback 가능성을 고려한다.
- frontend와 backend image tag 관계를 기록한다.
- CI/CD에서는 commit sha tag가 유용하다.

---

### [실무]

Build 예:

```bash
docker build -t my-frontend:latest .
docker build -t my-frontend:2026-07-07 .
docker build -t my-frontend:abc1234 .
```

CI/CD 예:

```text
frontend:${GITHUB_SHA}
backend:${GITHUB_SHA}
```

Review 기준:

```md
- [ ] latest만 사용하지 않는가?
- [ ] 배포 image tag가 기록되는가?
- [ ] rollback 가능한 이전 tag가 있는가?
- [ ] frontend/backend 호환 tag가 관리되는가?
```

---

### [FAQ]

Q. Docker image tag는 왜 중요한가?
A. 배포 버전을 추적하고 rollback하기 위해 중요하다.

Q. latest만 사용해도 되는가?
A. 가능하지만 운영에서는 추적과 rollback이 어려워질 수 있다.

Q. CI/CD에서는 어떤 tag가 좋은가?
A. commit sha, semantic version, 날짜 tag를 사용할 수 있다.

Q. frontend와 backend tag를 맞춰야 하는가?
A. API 호환성이 중요한 경우 같은 commit sha나 release version으로 관리하는 것이 좋다.

---

# 9. Docker Troubleshooting

## 9.1 Docker Build Failure

### [개념]

Docker Build Failure는 Docker image build 과정에서 dependency install, source copy, frontend build, Nginx config copy 등이 실패하는 문제다.

---

### [핵심]

대표 원인:

- build context 오류
- package.json 위치 오류
- lock file 누락
- Node version mismatch
- npm ci 실패
- env 누락
- TypeScript / ESLint build error
- output directory 불일치
- Dockerfile COPY 경로 오류
- `.dockerignore`가 필요한 파일 제외
- memory 부족

---

### [실무]

Troubleshooting Flow:

```text
docker build log 확인
→ 실패한 Dockerfile line 확인
→ build context 확인
→ COPY 경로 확인
→ package manager 확인
→ npm run build 로그 확인
→ output directory 확인
```

명령 예:

```bash
docker build --no-cache -t my-frontend .
```

주의:

```text
--no-cache는 원인 확인용으로 사용
항상 해결책은 아님
```

---

### [FAQ]

Q. Docker build가 실패하면 무엇을 먼저 봐야 하는가?
A. build log에서 실패한 Dockerfile line과 실제 error message를 먼저 확인한다.

Q. package.json을 못 찾는 이유는?
A. build context 또는 COPY 경로가 잘못되었을 가능성이 높다.

Q. Docker build에서는 실패하는데 로컬 npm run build는 되는 이유는?
A. Node version, env, Linux 대소문자, build context 차이 때문일 수 있다.

Q. --no-cache를 쓰면 문제가 해결되는가?
A. cache 문제 확인에는 도움이 되지만 근본 원인은 build log로 찾아야 한다.

---

## 9.2 Docker Runtime Failure

### [개념]

Docker Runtime Failure는 image build는 성공했지만 container 실행 후 서비스가 정상 동작하지 않는 문제다.

---

### [핵심]

대표 원인:

- Nginx config 오류
- container port 미공개
- backend upstream 연결 실패
- env 누락
- entrypoint script 권한 없음
- config.json 생성 실패
- volume mount 경로 오류
- permission 문제
- container crash loop
- healthcheck 실패

---

### [실무]

Troubleshooting Flow:

```text
docker compose ps
→ container 상태 확인
→ docker compose logs 확인
→ port mapping 확인
→ container 내부 파일 확인
→ nginx -t 확인
→ API proxy 확인
```

명령 예:

```bash
docker compose ps
docker compose logs frontend
docker compose exec frontend nginx -t
docker compose exec frontend ls -al /usr/share/nginx/html
```

상태별 판단:

```text
Exited
→ entrypoint / command / config error

Restarting
→ crash loop

Up but not reachable
→ port mapping / firewall / server binding 확인

Up but API fail
→ proxy / network / backend 확인
```

---

### [FAQ]

Q. Docker container가 실행 중인데 사이트가 안 열리면 무엇을 확인하는가?
A. ports mapping, Nginx log, container 내부 index.html 위치를 확인한다.

Q. container가 계속 재시작되면 무엇을 확인하는가?
A. docker logs로 entrypoint, config, env, permission 오류를 확인한다.

Q. Nginx container가 Up인데 API만 안 되면 무엇을 확인하는가?
A. proxy_pass, Docker network, backend container 상태를 확인한다.

Q. Runtime Config가 생성되지 않으면 무엇을 확인하는가?
A. entrypoint script 실행 권한, env 변수, 파일 쓰기 권한을 확인한다.

---

## 9.3 Docker API Connection Failure

### [개념]

Docker API Connection Failure는 Docker 배포 후 프론트엔드가 백엔드 API를 호출하지 못하는 문제다.

---

### [핵심]

대표 원인:

- React env에 `http://backend:8080` 사용
- 운영 API URL이 localhost
- Nginx `/api` proxy 누락
- backend service name 오류
- Docker network 미연결
- proxy_pass slash 오류
- backend port 오류
- backend container 미실행
- CORS / HTTPS 문제
- API가 index.html 반환

---

### [실무]

Troubleshooting Flow:

```text
Browser Network Request URL 확인
→ 요청 URL이 /api인지 확인
→ Nginx access log 확인
→ Nginx에서 backend 접근 테스트
→ Backend log 확인
→ proxy_pass path 확인
```

Docker 내부 테스트:

```bash
docker compose exec frontend wget -qO- http://backend:8080/api/health
```

Browser 기준 확인:

```text
Request URL: https://example.com/api/health
→ 정상

Request URL: http://backend:8080/api/health
→ 실패 가능성 높음
```

---

### [FAQ]

Q. Docker 배포 후 API가 안 되면 무엇을 먼저 확인하는가?
A. 브라우저 Network 탭의 실제 Request URL을 먼저 확인한다.

Q. Request URL이 [http://backend:8080이면](http://backend:8080이면) 왜 문제인가?
A. 브라우저가 Docker 내부 service name을 알 수 없기 때문이다.

Q. Docker 내부에서는 backend에 접근되는데 브라우저에서는 안 되는 이유는?
A. 내부 URL과 외부 브라우저 URL을 혼동했기 때문이다.

Q. Docker API 문제 해결의 권장 구조는 무엇인가?
A. 브라우저는 `/api`를 호출하고 Nginx가 `backend:8080`으로 proxy하는 구조다.

---

## 9.4 Docker Cache and Old Build

### [개념]

Docker Cache and Old Build는 Docker build cache, browser cache, Nginx cache, image tag 문제로 이전 프론트엔드 코드가 계속 제공되는 문제다.

---

### [핵심]

대표 원인:

- Docker layer cache가 이전 build 사용
- image tag가 latest로 덮여 추적 어려움
- container가 이전 image로 실행 중
- browser cache
- Nginx cache
- config.json cache
- CDN cache
- build context에 오래된 dist/build 포함

---

### [실무]

Troubleshooting Flow:

```text
docker images 확인
→ running container image 확인
→ docker compose build 여부 확인
→ docker compose up -d 재실행 확인
→ browser hard reload
→ cache header 확인
```

명령 예:

```bash
docker compose build --no-cache frontend
docker compose up -d frontend
docker image ls
docker compose ps
```

주의:

```text
image rebuild
≠
running container 자동 교체

container recreate 필요
```

---

### [FAQ]

Q. Docker로 재배포했는데 이전 화면이 보이는 이유는?
A. 이전 image/container, browser cache, Nginx cache, build cache가 원인일 수 있다.

Q. docker build만 하면 실행 중 container가 자동으로 바뀌는가?
A. 아니다. 새 image로 container를 recreate해야 한다.

Q. latest tag만 쓰면 어떤 문제가 있는가?
A. 어떤 버전이 실행 중인지 추적하기 어려워진다.

Q. 오래된 dist/build가 Docker image에 들어갈 수 있는가?
A. 가능하다. `.dockerignore`와 Dockerfile build 순서를 확인해야 한다.

---

# 10. Agent Decision Rules

## 10.1 PM Agent Rules

### [개념]

PM Agent는 Docker 배포 필요성, Compose 구조, API URL 전략, env 주입 방식, 검증 범위를 정의해야 한다.

---

### [핵심]

PM Agent 확인 항목:

- Docker 사용 목적
- Frontend Dockerfile 방식
- Build Tool
- Output Directory
- Nginx 사용 여부
- Docker Compose 사용 여부
- Backend service name
- API Base URL 전략
- Build-time env / Runtime Config 선택
- External ports
- Internal expose
- Healthcheck 필요 여부
- Restart policy
- Image tag 전략
- 검증 URL 목록

---

### [실무]

PM Agent 산출물 예:

```text
Deployment Type: Docker Compose
Frontend: React + Nginx multi-stage image
Build Tool: Vite
Output Directory: dist
Browser API URL: /api
Nginx Proxy: /api/ → backend:8080/api/
Backend DB URL: jdbc:mysql://db:3306/app
Env Strategy: Runtime Config or Build-time Env
Ports:
- frontend 80:80
- backend expose 8080
Healthcheck:
- backend /actuator/health
Verification:
- /
- /login refresh
- /api/health
- /assets/index.js
```

PM Agent 판단 Flow:

```text
배포 목적 확인
→ Docker 필요 여부 판단
→ Compose 서비스 구조 정의
→ API URL 전략 정의
→ env 주입 방식 선택
→ healthcheck/restart/tag 기준 정의
→ Review checklist 작성
```

---

### [FAQ]

Q. PM Agent는 Docker 배포에서 무엇을 정해야 하는가?
A. 서비스 구조, Dockerfile 방식, API URL 전략, env 주입 방식, ports, healthcheck, image tag를 정해야 한다.

Q. PM Agent가 Build-time Env와 Runtime Config를 선택해야 하는가?
A. 그렇다. 환경별 image를 만들지 하나의 image로 여러 환경을 처리할지 결정해야 한다.

Q. PM Agent가 브라우저 URL과 컨테이너 URL을 구분해야 하는가?
A. 반드시 구분해야 한다. API 장애의 주요 원인이다.

Q. PM Agent가 healthcheck를 요구해야 하는가?
A. 운영이나 Compose 안정성이 필요하면 healthcheck를 포함하는 것이 좋다.

---

## 10.2 Frontend Agent Rules

### [개념]

Frontend Agent는 Docker 배포 구조에 맞게 Build Output, env 접근 방식, API Base URL, Runtime Config loading을 구현해야 한다.

---

### [핵심]

Frontend Agent 필수 기준:

- Docker 배포에서도 `npm run build` 성공 유지
- Vite / CRA output directory 명확화
- API Base URL을 `/api` 또는 runtime config 기준으로 설정
- `http://backend:8080`을 브라우저 코드에 넣지 않음
- 운영 localhost fallback 금지
- Build-time env와 Runtime Config 구분
- Runtime Config 사용 시 앱 초기화 순서 보장
- config.json fetch 실패 처리
- WebSocket URL도 Docker/Nginx 구조 반영

---

### [실무]

권장 API Base URL:

```env
VITE_API_BASE_URL=/api
```

금지 예:

```env
VITE_API_BASE_URL=http://backend:8080/api
```

Runtime Config 사용 예:

```js
const config = await loadRuntimeConfig();

export const api = axios.create({
  baseURL: config.apiBaseUrl,
});
```

Frontend Agent 검증 기준:

```text
docker build 성공
→ container 실행
→ Browser Network에서 /api 호출 확인
→ backend service name 노출 여부 확인
→ config.json 로드 확인
```

---

### [FAQ]

Q. Frontend Agent는 Docker 배포에서 API URL을 어떻게 설정해야 하는가?
A. Nginx proxy 구조라면 브라우저 기준 `/api`를 사용하는 것이 안전하다.

Q. React 코드에 [http://backend:8080을](http://backend:8080을) 넣으면 안 되는 이유는?
A. 그 코드는 브라우저에서 실행되며 브라우저는 Docker 내부 service name을 알 수 없기 때문이다.

Q. Runtime Config를 쓰면 Frontend Agent가 무엇을 구현해야 하는가?
A. 앱 초기화 전에 config를 로드하고 API client를 config 기반으로 생성해야 한다.

Q. Docker 배포에서도 env validation이 필요한가?
A. 필요하다. env 누락이나 config 누락을 조기에 발견할 수 있다.

---

## 10.3 DevOps Agent Rules

### [개념]

DevOps Agent는 Dockerfile, Compose, Nginx config, network, healthcheck, image tag, log 확인 절차를 구현해야 한다.

---

### [핵심]

DevOps Agent 필수 기준:

- Multi-stage Dockerfile 작성
- `.dockerignore` 작성
- Nginx static root 설정
- `/api` proxy 설정
- `/ws` proxy 설정
- Docker Compose service 구성
- ports / expose 구분
- network 연결 확인
- healthcheck 작성
- restart policy 설정
- image tag 전략 적용
- Docker log 확인 절차 제공
- build / up / down / restart 명령 정리

---

### [실무]

DevOps Agent 구현 Flow:

```text
Dockerfile 작성
→ .dockerignore 작성
→ nginx.conf 작성
→ docker-compose.yml 작성
→ docker compose build
→ docker compose up -d
→ healthcheck 확인
→ smoke test
→ log 확인
```

기본 명령:

```bash
docker compose build
docker compose up -d
docker compose ps
docker compose logs frontend
docker compose logs backend
```

Smoke test:

```bash
curl -I http://localhost/
curl -I http://localhost/login
curl -I http://localhost/api/health
```

---

### [FAQ]

Q. DevOps Agent는 Docker 배포에서 무엇을 구현해야 하는가?
A. Dockerfile, Compose, Nginx config, network, healthcheck, restart policy, log 확인 절차를 구현해야 한다.

Q. Docker 배포 후 가장 먼저 확인할 명령은 무엇인가?
A. `docker compose ps`와 `docker compose logs`를 확인한다.

Q. DevOps Agent가 Nginx와 backend network를 확인해야 하는가?
A. 반드시 확인해야 한다. API proxy 실패의 핵심 원인이다.

Q. DevOps Agent가 image tag 전략도 관리해야 하는가?
A. 운영과 rollback을 고려하면 관리해야 한다.

---

## 10.4 Review Agent Rules

### [개념]

Review Agent는 Docker 배포 결과가 image build, container runtime, network, API proxy, env, cache 관점에서 정상인지 검토해야 한다.

---

### [핵심]

Review Agent Checklist:

```md
- [ ] Dockerfile이 multi-stage 구조인가?
- [ ] Build Tool에 맞는 output directory를 복사하는가?
- [ ] `.dockerignore`가 있는가?
- [ ] Secret이 image에 포함되지 않는가?
- [ ] Build-time env와 Runtime env가 구분되는가?
- [ ] Runtime Config 사용 시 config.json cache가 적절한가?
- [ ] 브라우저 API URL에 Docker service name이 없는가?
- [ ] Nginx `/api` proxy가 backend service로 연결되는가?
- [ ] Compose service들이 같은 network에 있는가?
- [ ] ports와 expose가 올바른가?
- [ ] backend DB URL이 service name을 사용하는가?
- [ ] healthcheck가 필요한 서비스에 있는가?
- [ ] restart policy가 적절한가?
- [ ] image tag 추적이 가능한가?
- [ ] docker logs에 critical error가 없는가?
- [ ] Browser Network에서 `/api` 요청이 정상인가?
```

---

### [실무]

Review Agent 판단 Flow:

```text
Dockerfile 검토
→ .dockerignore 검토
→ docker compose config 검토
→ docker compose build
→ docker compose up
→ container 상태 확인
→ browser network 확인
→ Nginx/backend logs 확인
→ env 반영 확인
```

Critical Issue:

```text
React env에 http://backend:8080 사용
Production API URL이 localhost
API 요청에 index.html 반환
502 Bad Gateway
Secret이 frontend image에 포함
docker run env가 React bundle을 바꾼다고 착각
backend DB URL이 localhost
container crash loop
```

승인 기준:

```text
Image build 성공
Container 정상 실행
정적 파일 정상
API proxy 정상
Env 전략 명확
Network 정상
Secret 미노출
Critical log 없음
```

---

### [FAQ]

Q. Review Agent는 Docker 배포에서 무엇을 가장 먼저 확인해야 하는가?
A. Dockerfile output directory와 브라우저 API URL이 Docker 내부 service name을 사용하지 않는지 확인해야 한다.

Q. React env에 backend service name이 있으면 승인 가능한가?
A. 아니다. 브라우저에서 해석되지 않는 URL이므로 실패 가능성이 높다.

Q. Docker Compose에서 API 502가 나면 무엇을 확인해야 하는가?
A. Nginx proxy_pass, backend service 상태, Docker network, backend port를 확인해야 한다.

Q. Docker 배포에서 Secret 노출은 어디를 확인해야 하는가?
A. Dockerfile ARG/ENV, `.env`, build logs, image layer, frontend JS bundle을 확인해야 한다.

---

# 11. Common Mistakes

## 11.1 Docker Deployment Common Mistakes

### [개념]

Docker Deployment Common Mistakes는 React Docker 배포에서 Build-time env, Docker network, Nginx proxy, image cache를 혼동해 발생하는 반복 실수다.

---

### [핵심]

자주 발생하는 실수:

- React Source Code를 runtime image에 그대로 넣음
- Multi-stage build 미사용
- Vite `dist` 대신 CRA `build`를 복사
- CRA `build` 대신 Vite `dist`를 복사
- Docker build context 오류
- `.dockerignore` 누락
- node_modules를 image에 복사
- `.env` 파일을 image에 포함
- Secret을 frontend Docker ARG로 주입
- `docker run -e`로 React Build-time env가 바뀐다고 착각
- Runtime Config에 Secret 저장
- React env에 `http://backend:8080` 사용
- React env에 `http://localhost:8080` 사용
- backend DB URL에 `localhost` 사용
- Docker Compose `ports`와 `expose` 혼동
- Nginx와 backend가 다른 network에 있음
- `/api` proxy 누락
- `proxy_pass` slash 오류
- API 요청에 index.html 반환
- 502 Bad Gateway 원인을 frontend 코드로 오해
- image rebuild 후 container recreate 누락
- `latest` tag만 사용해 배포 버전 추적 불가
- healthcheck 없이 depends_on만 믿음
- container crash loop 로그 미확인

---

### [실무]

실수별 판단:

```text
API URL이 backend:8080
→ Browser URL / Container URL 혼동

API URL이 localhost
→ 운영 env 또는 Docker localhost 오해

docker run -e 반영 안 됨
→ Build-time Env와 Runtime Env 혼동

502 Bad Gateway
→ Nginx에서 backend 접근 실패

DB connection fail
→ DB host service name 확인

변경사항 미반영
→ image rebuild / container recreate / cache 확인

container restart 반복
→ docker logs 확인
```

---

### [FAQ]

Q. Docker 배포에서 가장 흔한 실수는 무엇인가?
A. 브라우저에서 Docker 내부 service name을 호출하게 만드는 실수다.

Q. Docker 배포에서 가장 헷갈리는 env 문제는 무엇인가?
A. Build-time Env와 Runtime Env를 혼동하는 문제다.

Q. Docker Compose에서 가장 흔한 network 실수는 무엇인가?
A. 컨테이너끼리는 service name을 쓰고 브라우저는 service name을 쓸 수 없다는 점을 혼동하는 것이다.

Q. Docker 배포에서 변경사항이 반영되지 않는 이유는?
A. image rebuild, container recreate, browser cache, Nginx cache 중 하나가 누락되었을 수 있다.

---

# 12. Part09 Quality Checklist

## 12.1 Document Quality

### [개념]

이 문서는 Frontend Build & Deploy Domain의 Part09이며 Docker Deployment Rules Retrieval에 최적화되어야 한다.

---

### [핵심]

문서 품질 기준:

- Docker Deployment 정의 포함
- Docker 배포 적합성 판단 기준 포함
- Multi-stage Dockerfile 포함
- Vite / CRA Dockerfile 구분 포함
- Docker Build Context 포함
- `.dockerignore` 규칙 포함
- Build-time Env 포함
- Runtime Config 포함
- Build-time vs Runtime Env 비교 포함
- Docker Compose Core 포함
- frontend/backend Compose Pattern 포함
- ports / expose 구분 포함
- Compose Network Rules 포함
- Docker Nginx config 포함
- Browser URL vs Container URL 구분 포함
- Localhost in Docker 포함
- Healthcheck / restart policy 포함
- Docker cache / image tag 포함
- Troubleshooting Flow 포함
- Agent별 판단 기준 포함
- Common Mistakes 포함
- Retrieval Queries 포함

---

### [실무]

Part09는 다음 문서와 연결된다.

```text
Part01 Build Core
→ Part02 Build Tool Rules
→ Part03 Environment Variable Rules
→ Part04 API Base URL Rules
→ Part05 Static File Hosting Rules
→ Part06 SPA Routing Rules
→ Part07 Spring Boot Integrated Deployment Rules
→ Part08 Nginx Deployment Rules
→ Part09 Docker Deployment Rules
→ Part10 Platform Deployment Rules
→ Part11 CI/CD Rules
→ Part12 Deployment Verification & Troubleshooting
```

---

### [FAQ]

Q. Part09의 핵심 목적은 무엇인가?
A. React Docker 배포에서 Dockerfile, Compose, network, env, Nginx proxy 문제를 Agent가 정확히 판단하게 하는 것이다.

Q. Part09에서 Kubernetes까지 다루는가?
A. 아니다. Docker와 Docker Compose 기준으로 제한하고 Kubernetes는 별도 Expert 문서에서 다루는 것이 적합하다.

Q. Part09에서 CI/CD 전체를 다루는가?
A. 아니다. Docker image build와 검증 기준만 다루고 CI/CD 상세 전략은 후속 Part에서 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. Docker Deployment란 무엇인가?
A. 프론트엔드 Build 결과물과 실행 서버를 Docker Image로 패키징하거나 Compose로 여러 서비스를 함께 실행하는 배포 방식이다.

Q. React Docker 배포에서 가장 흔한 구조는 무엇인가?
A. Multi-stage Dockerfile로 React를 Build한 뒤 Nginx로 정적 파일을 제공하는 구조다.

Q. 브라우저에서 Docker service name을 API URL로 써도 되는가?
A. 안 된다. 브라우저는 Docker 내부 service name을 알 수 없다.

Q. Docker 배포에서 가장 중요한 구분은 무엇인가?
A. Build-time env와 Runtime env, 그리고 브라우저 기준 URL과 컨테이너 내부 URL을 구분하는 것이다.

Q. Docker 배포는 언제 적합한가?
A. 프론트엔드, 백엔드, DB, Nginx를 함께 관리하거나 환경 재현성이 중요할 때 적합하다.

Q. React만 배포하는데 Docker가 꼭 필요한가?
A. 아니다. 단순 정적 배포라면 Vercel, Netlify, S3 같은 플랫폼이 더 간단할 수 있다.

Q. Multi-stage Dockerfile이란 무엇인가?
A. Build 단계와 Runtime 단계를 분리해 최종 이미지에는 실행에 필요한 결과물만 포함하는 방식이다.

Q. React Docker Image에 Node.js가 꼭 남아 있어야 하는가?
A. 일반 정적 SPA 배포에서는 필요 없다. Build 후 Nginx만 있어도 된다.

Q. Vite Dockerfile에서 무엇을 복사해야 하는가?
A. Build stage의 `/app/dist`를 Nginx root로 복사한다.

Q. CRA Dockerfile에서 무엇을 복사해야 하는가?
A. Build stage의 `/app/build`를 Nginx root로 복사한다.

Q. Docker Build Context란 무엇인가?
A. Docker build 시 Docker Daemon에 전달되는 파일 범위다.

Q. build context가 틀리면 어떤 문제가 생기는가?
A. package.json을 못 찾거나 불필요한 파일이 이미지에 포함될 수 있다.

Q. .dockerignore는 왜 필요한가?
A. 불필요하거나 민감한 파일이 build context와 image에 포함되는 것을 막기 위해 필요하다.

Q. node_modules를 Docker image에 복사해도 되는가?
A. 권장하지 않는다. 이미지 내부에서 lock file 기준으로 설치하는 것이 재현성에 좋다.

Q. dist나 build 폴더를 .dockerignore에 넣어도 되는가?
A. 보통 넣는 것이 좋다. Docker build 안에서 새로 생성해야 오래된 결과물 혼입을 막을 수 있다.

Q. Docker에서 React env는 언제 반영되는가?
A. 일반적으로 `npm run build`가 실행되는 Docker build 시점에 반영된다.

Q. docker run -e로 VITE_API_BASE_URL을 바꾸면 React 앱에 반영되는가?
A. Build-time env 방식에서는 이미 생성된 JS bundle 값이 바뀌지 않을 수 있다.

Q. Docker ARG에 Secret을 넣어도 되는가?
A. 안 된다. image layer나 JS bundle에 노출될 수 있다.

Q. Runtime Config in Docker란 무엇인가?
A. 컨테이너 실행 시점 env로 config.json을 생성하고 React 앱이 이를 읽는 방식이다.

Q. Runtime Config를 쓰면 image를 다시 build하지 않아도 되는가?
A. public 설정 값만 바꾸는 경우 재빌드 없이 처리할 수 있다.

Q. Runtime Config에 Secret을 넣어도 되는가?
A. 안 된다. config.json은 브라우저에서 접근 가능하다.

Q. Build-time Env와 Runtime Env는 같은가?
A. 아니다. Build-time은 build 시점, Runtime은 container 실행 시점에 적용된다.

Q. docker-compose environment에 VITE_API_BASE_URL을 넣으면 React 코드가 바뀌는가?
A. 일반 Build-time 방식에서는 바뀌지 않을 수 있다.

Q. Docker에서 실행 시점 API URL 변경이 필요하면 어떻게 해야 하는가?
A. Runtime Config 또는 entrypoint에서 config.json 생성 방식을 사용한다.

Q. Docker Compose란 무엇인가?
A. 여러 컨테이너 서비스를 하나의 설정 파일로 정의하고 함께 실행하는 도구다.

Q. Compose service name은 어디서 사용할 수 있는가?
A. 같은 Docker network 안의 컨테이너끼리 통신할 때 사용할 수 있다.

Q. 브라우저에서 backend:8080으로 요청해도 되는가?
A. 안 된다. 브라우저는 Docker 내부 DNS를 알 수 없다.

Q. Docker Compose에서 frontend API URL은 무엇이 적합한가?
A. Nginx same-origin proxy를 쓴다면 `/api`가 적합하다.

Q. Nginx proxy_pass에는 backend service name을 써도 되는가?
A. 같은 Compose network 안이라면 `http://backend:8080`처럼 사용할 수 있다.

Q. backend port를 외부에 공개해야 하는가?
A. Nginx가 proxy한다면 외부 공개 없이 `expose`만으로도 가능하다.

Q. DB URL에서 localhost를 써도 되는가?
A. backend container 기준 localhost는 backend 자신이다. DB container는 보통 service name `db`로 접근한다.

Q. ports와 expose의 차이는 무엇인가?
A. `ports`는 host 외부에 공개하고, `expose`는 Compose network 내부 통신 용도다.

Q. Compose network에서 service name은 무엇인가?
A. 같은 network 내부에서 다른 컨테이너를 찾는 DNS 이름이다.

Q. Browser URL과 Container URL은 왜 구분해야 하는가?
A. 브라우저는 Docker 내부 네트워크를 모르고, 컨테이너끼리는 service name으로 통신할 수 있기 때문이다.

Q. React env에 [http://backend:8080을](http://backend:8080을) 넣으면 왜 안 되는가?
A. 그 값은 브라우저에서 실행되며 브라우저는 backend라는 Docker service name을 알 수 없기 때문이다.

Q. Docker에서 localhost는 무엇을 의미하는가?
A. 실행되는 위치 자신을 의미한다. 컨테이너 안에서는 해당 컨테이너 자신이다.

Q. backend container에서 DB를 localhost로 연결해도 되는가?
A. DB가 같은 backend container 안에 있는 것이 아니라면 안 된다. Compose service name을 사용해야 한다.

Q. Docker healthcheck는 왜 필요한가?
A. 컨테이너가 실제로 요청을 처리할 준비가 되었는지 확인하기 위해 필요하다.

Q. depends_on만으로 충분한가?
A. 아니다. 시작 순서만 보장하고 서비스 준비 완료는 보장하지 않는다.

Q. restart policy는 왜 필요한가?
A. 컨테이너가 예기치 않게 종료되었을 때 자동 복구하기 위해 필요하다.

Q. Docker Layer Cache란 무엇인가?
A. Dockerfile 명령 결과를 재사용해 build 속도를 높이는 기능이다.

Q. package.json을 먼저 복사하는 이유는?
A. source code 변경 때마다 dependency install이 다시 실행되는 것을 줄이기 위해서다.

Q. Docker image tag는 왜 중요한가?
A. 배포 버전을 추적하고 rollback하기 위해 중요하다.

Q. latest만 사용해도 되는가?
A. 가능하지만 운영에서는 추적과 rollback이 어려워질 수 있다.

Q. Docker build가 실패하면 무엇을 먼저 봐야 하는가?
A. build log에서 실패한 Dockerfile line과 실제 error message를 먼저 확인한다.

Q. package.json을 못 찾는 이유는?
A. build context 또는 COPY 경로가 잘못되었을 가능성이 높다.

Q. Docker container가 실행 중인데 사이트가 안 열리면 무엇을 확인하는가?
A. ports mapping, Nginx log, container 내부 index.html 위치를 확인한다.

Q. Docker 배포 후 API가 안 되면 무엇을 먼저 확인하는가?
A. 브라우저 Network 탭의 실제 Request URL을 먼저 확인한다.

Q. Request URL이 [http://backend:8080이면](http://backend:8080이면) 왜 문제인가?
A. 브라우저가 Docker 내부 service name을 알 수 없기 때문이다.

Q. Docker로 재배포했는데 이전 화면이 보이는 이유는?
A. 이전 image/container, browser cache, Nginx cache, build cache가 원인일 수 있다.

Q. docker build만 하면 실행 중 container가 자동으로 바뀌는가?
A. 아니다. 새 image로 container를 recreate해야 한다.

Q. PM Agent는 Docker 배포에서 무엇을 정해야 하는가?
A. 서비스 구조, Dockerfile 방식, API URL 전략, env 주입 방식, ports, healthcheck, image tag를 정해야 한다.

Q. Frontend Agent는 Docker 배포에서 API URL을 어떻게 설정해야 하는가?
A. Nginx proxy 구조라면 브라우저 기준 `/api`를 사용하는 것이 안전하다.

Q. DevOps Agent는 Docker 배포에서 무엇을 구현해야 하는가?
A. Dockerfile, Compose, Nginx config, network, healthcheck, restart policy, log 확인 절차를 구현해야 한다.

Q. Review Agent는 Docker 배포에서 무엇을 가장 먼저 확인해야 하는가?
A. Dockerfile output directory와 브라우저 API URL이 Docker 내부 service name을 사용하지 않는지 확인해야 한다.

Q. Docker 배포에서 가장 흔한 실수는 무엇인가?
A. 브라우저에서 Docker 내부 service name을 호출하게 만드는 실수다.

Q. Part09 다음 문서는 무엇인가?
A. Part10 Platform Deployment Rules로 이어지는 것이 적합하다.
