# Frontend Build & Deploy Part08 - Nginx Deployment Rules

---

# 1. Nginx Deployment Core

## 1.1 Nginx Deployment Definition

### [개념]

Nginx Deployment는 React Build 결과물을 Nginx가 정적 파일로 제공하고, 필요 시 `/api` 요청을 백엔드 서버로 reverse proxy 하는 배포 방식이다.

기본 구조:

```text
Browser
→ Nginx
→ React Static Files

Browser
→ Nginx /api
→ Backend Server
```

대표 구성:

```text
React Build Output
→ Nginx static root

Backend API
→ Nginx reverse proxy

SPA Route
→ Nginx fallback to index.html
```

---

### [핵심]

Nginx 배포 핵심 규칙:

- React Build Output을 Nginx static root에 복사한다.
- Vite는 `dist` 내부 파일을 사용한다.
- CRA는 `build` 내부 파일을 사용한다.
- `index.html`은 Nginx root 기준에서 제공되어야 한다.
- BrowserRouter 사용 시 `try_files` fallback이 필요하다.
- `/api` 요청은 React fallback이 아니라 백엔드로 proxy되어야 한다.
- 정적 asset 요청은 실제 파일로 제공되어야 한다.
- HTTPS 운영 시 TLS 인증서와 `wss://`를 고려해야 한다.
- Cache 정책은 `index.html`과 hashed assets를 분리한다.
- 배포 후 Console / Network / Refresh / API 요청을 검증한다.

---

### [실무]

2026 실무 기준으로 Nginx는 React SPA 정적 배포와 백엔드 API proxy를 함께 처리하는 가장 일반적인 선택지 중 하나다.

Nginx 기본 Flow:

```text
npm run build
→ dist or build 생성
→ Nginx root에 복사
→ Browser requests /
→ Nginx returns index.html
→ Browser loads JS/CSS
→ React Router renders screen
→ Browser requests /api/**
→ Nginx proxies to backend
```

Agent 판단 Flow:

```text
Build Tool 확인
→ Output Directory 확인
→ Nginx root 확인
→ index.html 위치 확인
→ SPA fallback 확인
→ /api proxy 확인
→ cache header 확인
→ HTTPS 여부 확인
→ Network 검증
```

---

### [FAQ]

Q. Nginx Deployment란 무엇인가?
A. React Build 결과물을 Nginx가 정적 파일로 제공하고 API 요청은 백엔드로 proxy하는 배포 방식이다.

Q. React 앱을 Nginx로 배포하려면 무엇을 올려야 하는가?
A. Source Code가 아니라 `dist` 또는 `build` 내부의 Build Output을 올려야 한다.

Q. Nginx 배포에서 가장 중요한 설정은 무엇인가?
A. static root, SPA fallback, `/api` proxy, cache, HTTPS 설정이다.

Q. Nginx 배포 후 가장 먼저 검증할 것은 무엇인가?
A. `/` 접속, JS/CSS asset 로드, route 새로고침, `/api` 요청을 확인해야 한다.

---

## 1.2 Nginx Deployment Decision Criteria

### [개념]

Nginx Deployment Decision Criteria는 React SPA를 Nginx로 배포하는 것이 적합한지 판단하는 기준이다.

---

### [핵심]

Nginx 배포가 적합한 경우:

```text
정적 파일 직접 호스팅 필요
백엔드 API reverse proxy 필요
Same Origin Proxy 구성 필요
Docker 기반 배포 필요
HTTPS termination 필요
Cache header 제어 필요
SPA fallback 제어 필요
운영 서버 직접 관리 가능
```

Nginx 배포가 부적합하거나 부담이 큰 경우:

```text
서버 관리 경험 부족
빠른 정적 배포만 필요
Vercel / Netlify 자동 배포가 충분
CDN 중심 서버리스 배포 선호
Nginx 설정 관리 부담
소규모 과제에서 단일 Spring Boot 통합 배포가 더 단순
```

---

### [실무]

2026 실무 기준으로 Nginx는 Docker, VM, 클라우드 서버에서 React + Spring Boot 구조를 운영할 때 안정적인 선택지다.

선택 Flow:

```text
React 정적 파일만 빠르게 배포
→ Vercel / Netlify / S3 고려

React + Backend API를 같은 도메인으로 제공
→ Nginx reverse proxy 적합

학원 발표용 단일 서버 단순 배포
→ Spring Boot 통합 배포도 가능

Docker Compose 기반 FE/BE 분리
→ Nginx gateway 역할 적합
```

PM Agent 판단 기준:

```text
배포 목적
→ 데모 / 운영 / 포트폴리오

서버 관리 가능 여부
→ Nginx 설정 가능 여부

API 구조
→ same-origin proxy 필요한가

HTTPS 필요성
→ Nginx TLS termination 필요한가

확장성
→ FE/BE 독립 배포가 필요한가
```

---

### [FAQ]

Q. Nginx 배포는 언제 적합한가?
A. React 정적 파일 제공과 백엔드 API proxy를 같은 서버에서 제어해야 할 때 적합하다.

Q. 학원 프로젝트에서도 Nginx 배포가 필요한가?
A. 필수는 아니다. 단순 발표라면 Spring Boot 통합 배포가 더 쉬울 수 있다.

Q. Docker Compose 구조에서는 Nginx가 유용한가?
A. 유용하다. Nginx가 frontend static hosting과 backend proxy gateway 역할을 할 수 있다.

Q. Vercel이나 Netlify를 쓰면 Nginx가 필요 없는가?
A. 대부분 필요 없다. 플랫폼이 정적 hosting과 rewrite 기능을 제공하기 때문이다.

---

# 2. Nginx Static Hosting

## 2.1 Nginx Root Rules

### [개념]

Nginx Root는 Nginx가 정적 파일을 찾는 기준 디렉토리다.

대표 설정:

```nginx
root /usr/share/nginx/html;
index index.html;
```

---

### [핵심]

Nginx Root 핵심 규칙:

- `index.html`은 root 바로 아래에 있어야 한다.
- JS / CSS / asset 폴더는 `index.html`이 참조하는 경로와 일치해야 한다.
- Vite `dist` 내부 파일을 root에 복사한다.
- CRA `build` 내부 파일을 root에 복사한다.
- `dist` 또는 `build` 폴더 자체를 한 단계 더 넣지 않도록 주의한다.
- root와 alias는 동작 방식이 다르므로 혼동하지 않는다.

정상 구조:

```text
/usr/share/nginx/html/index.html
/usr/share/nginx/html/assets/index.[hash].js
```

CRA 정상 구조:

```text
/usr/share/nginx/html/index.html
/usr/share/nginx/html/static/js/main.[hash].js
/usr/share/nginx/html/static/css/main.[hash].css
```

비정상 구조:

```text
/usr/share/nginx/html/dist/index.html
/usr/share/nginx/html/build/index.html
```

---

### [실무]

기본 Nginx static 설정:

```nginx
server {
  listen 80;
  server_name example.com;

  root /usr/share/nginx/html;
  index index.html;

  location / {
    try_files $uri $uri/ /index.html;
  }
}
```

Vite 복사:

```bash
npm run build
cp -r dist/* /usr/share/nginx/html/
```

CRA 복사:

```bash
npm run build
cp -r build/* /usr/share/nginx/html/
```

검증 Flow:

```text
Nginx root 확인
→ index.html 위치 확인
→ JS/CSS asset 위치 확인
→ nginx -t
→ reload
→ Browser Network 확인
```

---

### [FAQ]

Q. Nginx root란 무엇인가?
A. Nginx가 정적 파일을 찾는 기준 디렉토리다.

Q. React index.html은 Nginx 어디에 있어야 하는가?
A. 일반적으로 Nginx root 바로 아래에 있어야 한다.

Q. dist 폴더 자체를 Nginx root에 넣어도 되는가?
A. 보통 권장하지 않는다. `dist` 내부 파일이 root 기준으로 제공되어야 한다.

Q. Nginx root가 틀리면 어떤 문제가 생기는가?
A. index.html 404, JS/CSS 404, 흰 화면이 발생할 수 있다.

---

## 2.2 Vite Dist with Nginx

### [개념]

Vite Dist with Nginx는 Vite Build 결과물인 `dist` 내부 파일을 Nginx root로 제공하는 방식이다.

---

### [핵심]

Vite 기준:

```text
Build Command: npm run build
Output Directory: dist
Nginx Root: /usr/share/nginx/html
Copy Source: dist/*
Copy Target: /usr/share/nginx/html/
```

Vite output 구조:

```text
dist/
├ index.html
└ assets/
   ├ index.[hash].js
   └ index.[hash].css
```

주의:

- Vite `base`가 배포 경로와 맞아야 한다.
- 루트 배포는 보통 `base: "/"`를 사용한다.
- 하위 경로 배포는 `base: "/app/"`와 Nginx location을 함께 맞춘다.
- `/assets` 요청이 200인지 확인한다.

---

### [실무]

Dockerfile 예:

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
```

Nginx 설정:

```nginx
server {
  listen 80;
  root /usr/share/nginx/html;
  index index.html;

  location / {
    try_files $uri $uri/ /index.html;
  }
}
```

검증 Flow:

```text
npm run build
→ dist/assets 확인
→ Nginx root 복사
→ / 접속
→ /assets/index.[hash].js 200 확인
→ route 새로고침 확인
```

---

### [FAQ]

Q. Vite를 Nginx로 배포할 때 어떤 폴더를 복사하는가?
A. `dist` 내부 파일을 Nginx root로 복사한다.

Q. Vite 배포 후 /assets 파일이 404면 무엇을 확인하는가?
A. `dist/assets` 복사 여부, Nginx root, Vite base 설정을 확인한다.

Q. Vite root 배포에서 base는 어떻게 설정하는가?
A. 보통 기본값 `/`를 사용한다.

Q. Vite 하위 경로 배포에서는 무엇을 확인해야 하는가?
A. Vite `base`, React Router `basename`, Nginx location을 함께 확인해야 한다.

---

## 2.3 CRA Build with Nginx

### [개념]

CRA Build with Nginx는 CRA Build 결과물인 `build` 내부 파일을 Nginx root로 제공하는 방식이다.

---

### [핵심]

CRA 기준:

```text
Build Command: npm run build
Output Directory: build
Nginx Root: /usr/share/nginx/html
Copy Source: build/*
Copy Target: /usr/share/nginx/html/
```

CRA output 구조:

```text
build/
├ index.html
├ static/
│  ├ js/
│  └ css/
├ favicon.ico
└ manifest.json
```

주의:

- CRA `homepage`가 배포 경로와 맞아야 한다.
- 루트 배포에서는 homepage 생략 또는 적절한 기본값을 사용한다.
- 하위 경로 배포에서는 homepage와 Router basename을 함께 확인한다.
- `/static/js`와 `/static/css` 요청이 200인지 확인한다.

---

### [실무]

Dockerfile 예:

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
```

Nginx 설정:

```nginx
server {
  listen 80;
  root /usr/share/nginx/html;
  index index.html;

  location / {
    try_files $uri $uri/ /index.html;
  }
}
```

검증 Flow:

```text
npm run build
→ build/static 확인
→ Nginx root 복사
→ / 접속
→ /static/js/main.[hash].js 200 확인
→ route 새로고침 확인
```

---

### [FAQ]

Q. CRA를 Nginx로 배포할 때 어떤 폴더를 복사하는가?
A. `build` 내부 파일을 Nginx root로 복사한다.

Q. CRA 배포 후 /static/js 파일이 404면 무엇을 확인하는가?
A. `build/static` 복사 여부, Nginx root, CRA homepage 설정을 확인한다.

Q. CRA root 배포에서 homepage가 항상 필요한가?
A. 대부분 필요 없지만 배포 구조에 따라 설정할 수 있다.

Q. CRA 하위 경로 배포에서는 무엇을 확인해야 하는가?
A. CRA `homepage`, React Router `basename`, Nginx location을 함께 확인해야 한다.

---

# 3. Nginx SPA Fallback

## 3.1 Try Files Rules

### [개념]

`try_files`는 Nginx가 요청된 파일을 순서대로 찾아보고, 없으면 지정된 fallback 파일을 반환하는 설정이다.

React SPA에서는 BrowserRouter route 새로고침을 처리하기 위해 `index.html` fallback으로 사용한다.

---

### [핵심]

기본 설정:

```nginx
location / {
  try_files $uri $uri/ /index.html;
}
```

동작 의미:

```text
요청한 실제 파일이 있으면 반환
→ 요청한 디렉토리가 있으면 반환
→ 없으면 /index.html 반환
```

중요 규칙:

- `try_files $uri`가 먼저 있어야 asset 파일을 우선 제공한다.
- API 요청은 별도 `location /api/`에서 처리한다.
- 존재하지 않는 JS/CSS가 index.html로 fallback되면 MIME type error가 발생할 수 있다.
- 하위 경로 배포는 fallback 경로가 달라질 수 있다.

---

### [실무]

정상 설정:

```nginx
server {
  listen 80;
  root /usr/share/nginx/html;
  index index.html;

  location / {
    try_files $uri $uri/ /index.html;
  }
}
```

검증 Flow:

```text
GET /
→ index.html

GET /login
→ index.html

GET /assets/index.js
→ actual JS file

GET /not-real.js
→ 404 또는 명확한 처리 필요
```

Review 기준:

```md
- [ ] BrowserRouter 사용 시 fallback이 있는가?
- [ ] actual asset이 fallback보다 우선되는가?
- [ ] API path가 fallback에 잡히지 않는가?
- [ ] 직접 URL 접근과 새로고침이 되는가?
```

---

### [FAQ]

Q. Nginx에서 React 새로고침 404는 어떻게 해결하는가?
A. `try_files $uri $uri/ /index.html;` 설정으로 frontend route를 index.html로 fallback한다.

Q. try_files $uri는 왜 필요한가?
A. 실제 JS, CSS, 이미지 파일을 먼저 제공하기 위해 필요하다.

Q. try_files 설정이 없으면 어떤 문제가 생기는가?
A. `/login`, `/detail/1` 같은 React route 새로고침 시 404가 발생할 수 있다.

Q. 존재하지 않는 JS 파일이 index.html로 반환되면 어떤 문제가 생기는가?
A. MIME type error 또는 JavaScript parse error가 발생할 수 있다.

---

## 3.2 Fallback and API Separation

### [개념]

Fallback and API Separation은 Nginx에서 React route fallback과 Backend API proxy를 서로 분리하는 규칙이다.

---

### [핵심]

권장 우선순위:

```text
1. /api/ → backend proxy
2. /ws/ → websocket proxy
3. static asset → actual file
4. frontend route → index.html fallback
```

잘못된 구조:

```text
/api/festivals
→ location /
→ index.html fallback
```

증상:

- API 응답이 HTML
- Unexpected token `<`
- API 200인데 JSON 파싱 실패
- Backend log에 요청 없음
- Nginx access log에는 요청 있음

---

### [실무]

Nginx 분리 예:

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

  location / {
    try_files $uri $uri/ /index.html;
  }
}
```

검증 Flow:

```text
GET /api/health
→ backend JSON response

GET /login
→ index.html

GET /assets/index.js
→ JavaScript file
```

---

### [FAQ]

Q. Nginx에서 API와 SPA fallback을 왜 분리해야 하는가?
A. API 요청에 index.html이 반환되는 문제를 막기 위해 필요하다.

Q. API 요청에 HTML이 오면 무엇을 확인해야 하는가?
A. `/api/` location과 `proxy_pass`, fallback 우선순위를 확인해야 한다.

Q. Backend log에 요청이 없는데 프론트에서는 API 200이면 무엇을 의심하는가?
A. Nginx가 API 요청을 backend로 보내지 않고 index.html을 반환했을 가능성이 있다.

Q. `/api` path는 location /보다 먼저 처리되는가?
A. Nginx location 매칭 규칙에 따라 더 구체적인 prefix location이 우선될 수 있지만 설정 구조를 명확히 해야 한다.

---

# 4. Nginx API Reverse Proxy

## 4.1 Proxy Pass Rules

### [개념]

`proxy_pass`는 Nginx가 받은 요청을 백엔드 서버로 전달하는 reverse proxy 설정이다.

---

### [핵심]

기본 예:

```nginx
location /api/ {
  proxy_pass http://backend:8080/api/;
}
```

핵심 확인 항목:

- backend host
- backend port
- location path
- proxy_pass path
- slash 처리
- upstream service name
- Docker network 접근 가능성
- backend API prefix
- header 전달
- timeout

---

### [실무]

Docker Compose 내부 서비스 예:

```nginx
location /api/ {
  proxy_pass http://backend:8080/api/;
}
```

VM 또는 같은 서버 백엔드 예:

```nginx
location /api/ {
  proxy_pass http://127.0.0.1:8080/api/;
}
```

원격 백엔드 예:

```nginx
location /api/ {
  proxy_pass https://api.example.com/api/;
}
```

검증 Flow:

```text
Nginx container/server에서 backend 접근 확인
→ proxy_pass host/port 확인
→ /api/health 요청
→ Nginx access log 확인
→ Backend access log 확인
```

---

### [FAQ]

Q. proxy_pass는 무엇인가?
A. Nginx가 받은 요청을 백엔드 서버로 전달하는 reverse proxy 설정이다.

Q. Docker Compose에서 proxy_pass에 backend를 쓸 수 있는가?
A. 같은 Docker network 안에서 service name이 `backend`라면 가능하다.

Q. 브라우저에서 [http://backend:8080을](http://backend:8080을) 호출해도 되는가?
A. 안 된다. 브라우저는 Docker 내부 service name을 알 수 없다. Nginx가 proxy해야 한다.

Q. proxy_pass가 잘못되면 어떤 문제가 생기는가?
A. API 502, 404, index.html 반환, backend 미도달 문제가 발생할 수 있다.

---

## 4.2 Proxy Slash Rules

### [개념]

Proxy Slash Rules는 Nginx `location`과 `proxy_pass`의 trailing slash 및 URI 포함 여부에 따라 백엔드로 전달되는 request path가 달라지는 규칙이다.

Nginx reverse proxy에서 `/api` 중복, `/api` 제거, 특정 API 404 문제는 대부분 `location` path와 `proxy_pass` path 조합에서 발생한다.

---

### [핵심]

주의 대상:

```nginx
location /api/ {
  proxy_pass http://backend:8080/api/;
}
```

```nginx
location /api/ {
  proxy_pass http://backend:8080/;
}
```

```nginx
location /api/ {
  proxy_pass http://backend:8080;
}
```

핵심 규칙:

```text
proxy_pass에 URI path가 포함됨
→ location prefix가 proxy_pass URI로 치환될 수 있음

proxy_pass에 URI path가 없음
→ 원래 request URI가 그대로 전달됨
```

예:

```text
Request: /api/festivals
location: /api/
proxy_pass: http://backend:8080/api/
→ backend receives: /api/festivals
```

```text
Request: /api/festivals
location: /api/
proxy_pass: http://backend:8080/
→ backend receives: /festivals
```

```text
Request: /api/festivals
location: /api/
proxy_pass: http://backend:8080
→ backend receives: /api/festivals
```

잘못된 slash 처리 결과:

- `/api/api` 중복
- `/api` prefix 제거
- backend route mismatch
- 특정 API 404
- local에서는 되는데 Nginx 배포에서 실패
- backend log의 request path가 예상과 다름

---

### [실무]

Backend Controller가 `/api/festivals`를 제공하는 경우 권장 예:

```nginx
location /api/ {
  proxy_pass http://backend:8080/api/;
}
```

또는 URI 없는 방식:

```nginx
location /api/ {
  proxy_pass http://backend:8080;
}
```

두 방식 모두 backend가 `/api/festivals`를 받도록 구성할 수 있지만, 팀에서는 하나의 규칙으로 통일하는 것이 좋다.

Backend Controller가 `/festivals`를 제공하고 Nginx에서 `/api` prefix를 제거하고 싶은 경우:

```nginx
location /api/ {
  proxy_pass http://backend:8080/;
}
```

이 경우:

```text
/api/festivals
→ backend /festivals
```

Agent 검토 Flow:

```text
Frontend Request URL 확인
→ Nginx location 확인
→ proxy_pass URI 포함 여부 확인
→ trailing slash 확인
→ Backend Controller path 확인
→ Backend access log path 확인
→ /api 중복 또는 제거 여부 판단
```

Review 기준:

```md
- [ ] Frontend Request URL이 의도한 path인가?
- [ ] Backend Controller가 `/api/**`를 받는가?
- [ ] Nginx가 `/api` prefix를 유지해야 하는가?
- [ ] Nginx가 `/api` prefix를 제거해야 하는가?
- [ ] `location`과 `proxy_pass` 조합이 팀 규칙과 일치하는가?
- [ ] Backend log에 실제 도달한 path가 예상과 같은가?
```

---

### [FAQ]

Q. proxy_pass에서 slash가 중요한가?
A. 중요하다. `location`과 `proxy_pass` 조합에 따라 백엔드로 전달되는 path가 달라질 수 있다.

Q. proxy_pass에 URI path가 포함된다는 것은 무엇인가?
A. `proxy_pass http://backend:8080/api/;`처럼 host 뒤에 `/api/` 같은 path가 붙은 경우다.

Q. proxy_pass에 URI path가 없으면 어떻게 되는가?
A. `proxy_pass http://backend:8080;`처럼 작성하면 원래 request URI가 그대로 전달된다.

Q. API 404가 Nginx에서만 발생하면 무엇을 확인하는가?
A. `location`, `proxy_pass`, trailing slash, backend controller path, backend access log를 확인해야 한다.

Q. `/api/api`가 생기는 이유는 무엇인가?
A. frontend baseURL, Nginx proxy_pass, backend controller path에 `/api`가 중복되었을 수 있다.

Q. `/api` prefix가 사라지는 이유는 무엇인가?
A. `location /api/`와 `proxy_pass http://backend:8080/;` 조합처럼 prefix가 치환되어 제거될 수 있기 때문이다.

Q. 가장 안전한 방법은 무엇인가?
A. 팀에서 backend API prefix 유지 방식 또는 제거 방식을 하나로 정하고, Network와 backend log로 실제 path를 확인하는 것이다.

---

## 4.3 Proxy Headers

### [개념]

Proxy Headers는 Nginx가 백엔드로 요청을 전달할 때 원래 client, host, protocol 정보를 함께 넘기는 header다.

---

### [핵심]

대표 header:

```nginx
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
```

역할:

```text
Host
→ 원래 요청 host 전달

X-Real-IP
→ 실제 client IP 전달

X-Forwarded-For
→ proxy chain client IP 전달

X-Forwarded-Proto
→ 원래 protocol http/https 전달
```

---

### [실무]

권장 proxy header 설정:

```nginx
location /api/ {
  proxy_pass http://backend:8080/api/;
  proxy_set_header Host $host;
  proxy_set_header X-Real-IP $remote_addr;
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  proxy_set_header X-Forwarded-Proto $scheme;
}
```

Spring Boot reverse proxy 환경:

```properties
server.forward-headers-strategy=framework
```

검증 대상:

```md
- [ ] redirect URL이 https 기준인가?
- [ ] cookie Secure 판단이 정상인가?
- [ ] backend log client IP가 정상인가?
- [ ] OAuth callback URL이 정상인가?
```

---

### [FAQ]

Q. proxy_set_header는 왜 필요한가?
A. 백엔드가 원래 요청의 host, protocol, client IP를 알 수 있게 하기 위해 필요하다.

Q. X-Forwarded-Proto는 왜 중요한가?
A. HTTPS reverse proxy 뒤에서 백엔드가 원래 요청이 HTTPS였는지 판단하는 데 필요하다.

Q. proxy header가 없으면 어떤 문제가 생기는가?
A. redirect URL, cookie secure, OAuth callback, client IP log가 잘못될 수 있다.

Q. Spring Boot에서 forwarded header 설정이 필요한가?
A. Reverse Proxy 뒤에서 HTTPS나 redirect 문제가 있으면 필요할 수 있다.

---

## 4.4 Proxy Timeout and Body Size

### [개념]

Proxy Timeout and Body Size는 Nginx가 백엔드 응답을 기다리는 시간과 요청 body 크기를 제한하는 설정이다.

---

### [핵심]

관련 설정:

```nginx
client_max_body_size 10m;
proxy_connect_timeout 60s;
proxy_send_timeout 60s;
proxy_read_timeout 60s;
```

필요 상황:

- 이미지 업로드
- 파일 업로드
- 긴 API 처리
- AI 응답 대기
- 대용량 JSON 요청
- 느린 백엔드 처리
- WebSocket 장시간 연결

---

### [실무]

업로드가 있는 프로젝트 예:

```nginx
server {
  client_max_body_size 20m;

  location /api/ {
    proxy_pass http://backend:8080/api/;
    proxy_connect_timeout 60s;
    proxy_send_timeout 60s;
    proxy_read_timeout 60s;
  }
}
```

증상별 판단:

```text
413 Request Entity Too Large
→ client_max_body_size 확인

504 Gateway Timeout
→ proxy_read_timeout / backend 처리 시간 확인

502 Bad Gateway
→ backend down / upstream 연결 실패 확인
```

---

### [FAQ]

Q. 413 Request Entity Too Large는 무엇인가?
A. 요청 body가 Nginx의 허용 크기보다 커서 거부된 것이다.

Q. 파일 업로드가 실패하면 Nginx에서 무엇을 확인해야 하는가?
A. `client_max_body_size` 설정을 확인해야 한다.

Q. 504 Gateway Timeout은 무엇을 의미하는가?
A. Nginx가 백엔드 응답을 제한 시간 안에 받지 못한 것이다.

Q. API 처리 시간이 길면 무엇을 조정해야 하는가?
A. `proxy_read_timeout`과 백엔드 처리 성능을 함께 확인해야 한다.

---

# 5. Nginx WebSocket Proxy

## 5.1 WebSocket Proxy Rules

### [개념]

WebSocket Proxy는 Nginx가 `/ws` 같은 WebSocket 연결 요청을 백엔드 WebSocket 서버로 전달하는 설정이다.

---

### [핵심]

WebSocket proxy 필수 설정:

```nginx
proxy_http_version 1.1;
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection "upgrade";
```

주의:

- HTTPS 페이지에서는 `wss://` 사용
- Nginx에서 WebSocket location 별도 분리
- timeout 설정 고려
- 인증 token 전달 방식 확인
- SockJS / STOMP 사용 시 endpoint path 확인
- `/ws` path가 SPA fallback에 잡히면 안 됨

---

### [실무]

Nginx WebSocket 설정:

```nginx
location /ws/ {
  proxy_pass http://backend:8080/ws/;
  proxy_http_version 1.1;
  proxy_set_header Upgrade $http_upgrade;
  proxy_set_header Connection "upgrade";
  proxy_set_header Host $host;
  proxy_read_timeout 3600s;
}
```

Frontend env 예:

```env
VITE_WS_BASE_URL=wss://example.com/ws
```

Same Origin 방식:

```js
const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
const wsUrl = `${protocol}//${window.location.host}/ws`;
```

검증 Flow:

```text
Network WS 탭 확인
→ Status 101 Switching Protocols 확인
→ Nginx access log 확인
→ Backend WebSocket log 확인
```

---

### [FAQ]

Q. Nginx에서 WebSocket proxy는 일반 API proxy와 같은가?
A. 유사하지만 Upgrade header와 HTTP/1.1 설정이 추가로 필요하다.

Q. WebSocket 연결에서 101은 무엇인가?
A. HTTP 연결이 WebSocket으로 전환되었음을 의미하는 정상 상태다.

Q. HTTPS 페이지에서 ws://를 써도 되는가?
A. 안 된다. HTTPS 페이지에서는 `wss://`를 사용해야 한다.

Q. /ws 요청이 index.html로 가면 무엇을 확인해야 하는가?
A. WebSocket location이 SPA fallback보다 명확히 분리되어 있는지 확인해야 한다.

---

## 5.2 STOMP SockJS Proxy Rules

### [개념]

STOMP SockJS Proxy Rules는 Spring WebSocket에서 STOMP 또는 SockJS를 사용할 때 Nginx가 관련 연결 경로를 백엔드로 전달하는 규칙이다.

---

### [핵심]

확인 대상:

```text
WebSocket endpoint path
SockJS fallback path
STOMP broker destination
Allowed Origin
Auth token 전달 방식
Nginx location
```

SockJS는 WebSocket 외에도 여러 HTTP fallback 요청을 사용할 수 있으므로 `/ws/**` 전체를 백엔드로 보내는 것이 안전하다.

---

### [실무]

Nginx 예:

```nginx
location /ws/ {
  proxy_pass http://backend:8080/ws/;
  proxy_http_version 1.1;
  proxy_set_header Upgrade $http_upgrade;
  proxy_set_header Connection "upgrade";
  proxy_set_header Host $host;
  proxy_read_timeout 3600s;
}
```

Spring endpoint 예:

```java
registry.addEndpoint("/ws")
    .setAllowedOriginPatterns("*")
    .withSockJS();
```

검증 Flow:

```text
Frontend WS URL 확인
→ Nginx /ws location 확인
→ Backend endpoint 확인
→ Browser Network WS/XHR 확인
→ 404/403/CORS 확인
```

---

### [FAQ]

Q. SockJS를 쓰면 Nginx에서 무엇을 주의해야 하는가?
A. WebSocket뿐 아니라 `/ws/**` 하위 HTTP fallback 요청도 백엔드로 proxy해야 한다.

Q. STOMP destination과 WebSocket endpoint는 같은가?
A. 아니다. endpoint는 연결 URL이고 destination은 메시지 routing 경로다.

Q. WebSocket 403이 나면 무엇을 확인해야 하는가?
A. Spring allowed origins, 인증 token, Nginx header, HTTPS/wss 설정을 확인해야 한다.

Q. SockJS 요청이 index.html로 반환되면 무엇이 문제인가?
A. `/ws/**` 요청이 SPA fallback에 잡히고 있을 가능성이 높다.

---

# 6. HTTPS and TLS

## 6.1 HTTPS Termination

### [개념]

HTTPS Termination은 Nginx가 TLS 인증서를 사용해 HTTPS 요청을 받고, 내부 백엔드에는 HTTP로 전달하는 구조다.

기본 구조:

```text
Browser
→ HTTPS
→ Nginx
→ HTTP
→ Backend
```

---

### [핵심]

HTTPS 운영 기준:

- `listen 443 ssl`
- TLS certificate 설정
- HTTP → HTTPS redirect
- `X-Forwarded-Proto` 전달
- Secure Cookie 고려
- Mixed Content 방지
- WebSocket은 `wss://`
- 인증서 만료 관리 필요

---

### [실무]

Nginx HTTPS 예:

```nginx
server {
  listen 80;
  server_name example.com;
  return 301 https://$host$request_uri;
}

server {
  listen 443 ssl;
  server_name example.com;

  ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

  root /usr/share/nginx/html;
  index index.html;

  location /api/ {
    proxy_pass http://backend:8080/api/;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-Proto $scheme;
  }

  location / {
    try_files $uri $uri/ /index.html;
  }
}
```

검증 Flow:

```text
https 접속 확인
→ http redirect 확인
→ certificate valid 확인
→ API https 요청 확인
→ Mixed Content 확인
```

---

### [FAQ]

Q. HTTPS Termination이란 무엇인가?
A. Nginx가 HTTPS 요청을 받고 내부 백엔드로는 HTTP로 전달하는 구조다.

Q. HTTPS 페이지에서 HTTP API를 호출하면 어떻게 되는가?
A. Mixed Content로 차단될 수 있다.

Q. HTTPS 운영에서 X-Forwarded-Proto가 왜 필요한가?
A. 백엔드가 원래 요청이 HTTPS였는지 알기 위해 필요하다.

Q. HTTPS 페이지에서 WebSocket은 어떤 protocol을 써야 하는가?
A. `wss://`를 사용해야 한다.

---

## 6.2 Mixed Content Rules

### [개념]

Mixed Content는 HTTPS 페이지에서 HTTP 리소스나 API를 호출해 브라우저가 요청을 차단하는 문제다.

---

### [핵심]

Mixed Content 대상:

```text
HTTP API
HTTP image
HTTP script
HTTP stylesheet
ws:// WebSocket
HTTP font
```

정상 기준:

```text
Frontend: https://example.com
API: https://example.com/api
WebSocket: wss://example.com/ws
Asset: https://example.com/assets/...
```

---

### [실무]

Troubleshooting Flow:

```text
Console Mixed Content 확인
→ Network blocked request 확인
→ API Base URL env 확인
→ image/font URL 확인
→ WebSocket protocol 확인
→ HTTPS 설정 수정
→ rebuild/redeploy
```

Agent 검토 기준:

```md
- [ ] Production API URL이 https인가?
- [ ] 이미지 외부 URL이 https인가?
- [ ] WebSocket URL이 wss인가?
- [ ] OAuth callback이 https인가?
- [ ] cookie Secure 설정과 일치하는가?
```

---

### [FAQ]

Q. Mixed Content란 무엇인가?
A. HTTPS 페이지에서 HTTP 리소스를 호출해 브라우저가 차단하는 문제다.

Q. Mixed Content는 어디서 확인하는가?
A. 브라우저 Console과 Network 탭에서 확인한다.

Q. 이미지도 Mixed Content가 될 수 있는가?
A. 가능하다. HTTP 이미지가 HTTPS 페이지에서 차단될 수 있다.

Q. Mixed Content 해결은 프론트엔드 env와 관련 있는가?
A. 관련 있다. API Base URL이나 asset URL이 HTTP로 설정되어 있으면 수정해야 한다.

---

# 7. Nginx Cache and Compression

## 7.1 Cache Header Rules

### [개념]

Cache Header Rules는 Nginx가 `index.html`, JS, CSS, 이미지 파일에 대해 브라우저 캐시 정책을 설정하는 규칙이다.

---

### [핵심]

권장 기준:

```text
index.html
→ no-cache 또는 짧은 cache

hashed JS/CSS
→ public, max-age=31536000, immutable

config.json
→ no-store 또는 짧은 cache

image/font hashed asset
→ long cache 가능
```

주의:

- `index.html` 장기 캐시는 배포 반영 문제를 만든다.
- hashed asset은 장기 캐시가 가능하다.
- Runtime Config는 장기 캐시하면 안 된다.
- CDN 사용 시 cache header와 invalidation을 함께 고려한다.

---

### [실무]

Nginx cache 예:

```nginx
location = /index.html {
  add_header Cache-Control "no-cache";
}

location /assets/ {
  add_header Cache-Control "public, max-age=31536000, immutable";
}

location = /config.json {
  add_header Cache-Control "no-store";
}
```

CRA 정적 asset 예:

```nginx
location /static/ {
  add_header Cache-Control "public, max-age=31536000, immutable";
}
```

검증 Flow:

```text
Network 요청 선택
→ Response Headers 확인
→ Cache-Control 확인
→ Hard Reload 테스트
→ 새 배포 후 index.html 갱신 확인
```

---

### [FAQ]

Q. index.html은 왜 no-cache가 좋은가?
A. 새 배포 시 최신 JS/CSS hash를 참조해야 하기 때문이다.

Q. hashed JS/CSS는 왜 long cache가 가능한가?
A. 파일 내용이 바뀌면 hash 파일명도 바뀌기 때문이다.

Q. config.json은 왜 no-store가 필요한가?
A. Runtime Config 값은 배포 후 변경될 수 있으므로 오래 캐시하면 안 된다.

Q. 캐시 문제는 어디서 확인하는가?
A. Network Response Headers와 Disable Cache 테스트로 확인한다.

---

## 7.2 Gzip and Brotli Rules

### [개념]

Gzip and Brotli Rules는 Nginx가 JavaScript, CSS, JSON 같은 텍스트 기반 리소스를 압축해 전송하는 성능 최적화 규칙이다.

---

### [핵심]

압축 대상:

```text
text/html
text/css
application/javascript
application/json
image/svg+xml
```

압축 효과:

- JS bundle 전송량 감소
- CSS 전송량 감소
- 초기 로딩 속도 개선
- 네트워크 비용 감소

주의:

- 이미지처럼 이미 압축된 파일은 효과가 작다.
- Brotli는 별도 모듈이나 이미지 설정이 필요할 수 있다.
- 압축 설정보다 bundle size 최적화도 함께 필요하다.

---

### [실무]

Gzip 예:

```nginx
gzip on;
gzip_comp_level 6;
gzip_types
  text/plain
  text/css
  application/json
  application/javascript
  text/xml
  application/xml
  image/svg+xml;
```

검증 Flow:

```text
Network 요청 선택
→ Response Headers 확인
→ Content-Encoding: gzip 또는 br 확인
→ transferred size 확인
```

Agent 판단:

```text
JS bundle이 큰 경우
→ gzip/brotli 확인
→ code splitting / lazy loading도 함께 검토
```

---

### [FAQ]

Q. Nginx gzip은 왜 사용하는가?
A. JS, CSS, JSON 같은 텍스트 파일 전송 크기를 줄이기 위해 사용한다.

Q. Brotli가 항상 필요한가?
A. 필수는 아니지만 정적 파일 성능 최적화에 유리할 수 있다.

Q. 압축이 적용되었는지 어디서 확인하는가?
A. Network Response Headers의 `Content-Encoding`에서 확인한다.

Q. gzip만 켜면 성능 문제가 모두 해결되는가?
A. 아니다. bundle size, code splitting, cache 전략도 함께 봐야 한다.

---

# 8. Nginx Logging and Debugging

## 8.1 Access Log and Error Log

### [개념]

Nginx Log는 요청 처리 상태, proxy 실패, 파일 경로 오류, upstream 연결 문제를 확인하기 위한 기록이다.

대표 로그:

```text
access.log
error.log
```

---

### [핵심]

Access Log에서 확인할 것:

- Request path
- Status code
- Response size
- User agent
- Client IP
- API 요청이 Nginx에 도달했는지
- static asset 요청 status

Error Log에서 확인할 것:

- file not found
- upstream connection failed
- permission denied
- invalid config
- too large body
- timeout

---

### [실무]

Docker Nginx log 확인:

```bash
docker logs nginx
```

Linux server log 확인:

```bash
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

Troubleshooting Flow:

```text
Browser Network 문제 확인
→ Nginx access log 확인
→ Nginx error log 확인
→ Backend log 확인
→ proxy path와 status 비교
```

Status별 판단:

```text
404
→ root/path/fallback 확인

502
→ backend upstream 연결 실패

413
→ client_max_body_size 확인

504
→ proxy timeout/backend 지연 확인
```

---

### [FAQ]

Q. Nginx access log에서는 무엇을 확인하는가?
A. 요청 path, status code, static asset 요청, API 요청 도달 여부를 확인한다.

Q. Nginx error log에서는 무엇을 확인하는가?
A. 파일 없음, upstream 실패, 권한 문제, timeout 같은 서버 오류를 확인한다.

Q. 502 Bad Gateway는 무엇을 의미하는가?
A. Nginx가 backend upstream에 정상 연결하지 못했다는 의미다.

Q. Nginx 문제와 Backend 문제를 어떻게 구분하는가?
A. Nginx access/error log와 Backend log에 요청이 도달했는지 비교한다.

---

## 8.2 Nginx Config Validation

### [개념]

Nginx Config Validation은 Nginx 설정 파일 문법과 로딩 가능 여부를 검증하는 과정이다.

---

### [핵심]

필수 명령:

```bash
nginx -t
```

적용 명령:

```bash
nginx -s reload
```

또는 systemd:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

주의:

- 설정 수정 후 reload 필요
- Docker image에 설정 파일이 복사되었는지 확인
- `conf.d/default.conf` 경로 확인
- server block 중복 확인
- syntax OK여도 logic 오류는 별도 검증 필요

---

### [실무]

검증 Flow:

```text
nginx.conf 수정
→ nginx -t
→ reload
→ curl / 확인
→ curl /api/health 확인
→ Browser Network 확인
```

Docker 내부 검증:

```bash
docker exec -it nginx nginx -t
docker exec -it nginx nginx -s reload
```

Review 기준:

```md
- [ ] nginx -t 통과
- [ ] 설정 파일 경로 정상
- [ ] reload 수행
- [ ] / route 정상
- [ ] /api route 정상
- [ ] direct SPA route 정상
```

---

### [FAQ]

Q. Nginx 설정을 바꾼 뒤 무엇을 해야 하는가?
A. `nginx -t`로 문법 확인 후 reload해야 한다.

Q. nginx -t가 성공하면 배포가 완전히 정상인가?
A. 아니다. 문법만 검증하므로 route, proxy, asset, API는 별도로 테스트해야 한다.

Q. Docker Nginx에서 설정 파일은 어디에 둘 수 있는가?
A. 보통 `/etc/nginx/conf.d/default.conf`에 둔다.

Q. 설정을 바꿨는데 반영되지 않는 이유는?
A. reload 누락, Docker image 재빌드 누락, volume mount 경로 오류를 확인해야 한다.

---

# 9. Nginx Troubleshooting

## 9.1 Nginx 404

### [개념]

Nginx 404는 Nginx가 요청한 파일이나 route를 찾지 못해 404를 반환하는 문제다.

---

### [핵심]

대표 원인:

- root 경로 오류
- index.html 위치 오류
- Build Output 미복사
- Vite `dist` / CRA `build` 혼동
- SPA fallback 누락
- sub path location 오류
- asset path 오류
- 파일명 대소문자 오류

---

### [실무]

Troubleshooting Flow:

```text
Network 404 path 확인
→ Nginx root 확인
→ 실제 파일 존재 확인
→ try_files 확인
→ build output 확인
→ base/homepage 확인
→ access/error log 확인
```

구분:

```text
/ 404
→ index.html 위치 또는 root 문제

/login 404
→ SPA fallback 문제

/assets/index.js 404
→ asset 복사 또는 base path 문제

/api/health 404
→ proxy path 또는 backend route 문제
```

---

### [FAQ]

Q. Nginx에서 / 가 404면 무엇을 확인해야 하는가?
A. root 경로와 `index.html` 위치를 확인해야 한다.

Q. /login만 404면 무엇을 확인해야 하는가?
A. React SPA fallback 설정인 `try_files`를 확인해야 한다.

Q. /assets 파일이 404면 무엇을 확인해야 하는가?
A. Build Output 복사 여부, Vite base, Nginx root를 확인해야 한다.

Q. /api가 404면 무엇을 확인해야 하는가?
A. Nginx proxy path, `proxy_pass`, Backend Controller path를 확인해야 한다.

---

## 9.2 Nginx 502 Bad Gateway

### [개념]

Nginx 502 Bad Gateway는 Nginx가 upstream backend 서버에 정상 연결하지 못할 때 발생하는 오류다.

---

### [핵심]

대표 원인:

- Backend 서버 미실행
- proxy_pass host 오류
- proxy_pass port 오류
- Docker network 미연결
- backend service name 오류
- backend container crash
- firewall 문제
- protocol mismatch
- DNS resolution failure

---

### [실무]

Troubleshooting Flow:

```text
Nginx error log 확인
→ backend 실행 여부 확인
→ backend port 확인
→ Nginx에서 backend 접근 테스트
→ Docker network 확인
→ proxy_pass host 수정
```

Docker Compose 확인:

```bash
docker compose ps
docker compose logs backend
docker exec -it nginx wget -qO- http://backend:8080/api/health
```

VM 확인:

```bash
curl http://127.0.0.1:8080/api/health
sudo ss -tulpn | grep 8080
```

---

### [FAQ]

Q. 502 Bad Gateway는 무엇인가?
A. Nginx가 backend upstream에 연결하지 못했다는 의미다.

Q. 502가 나오면 프론트엔드 문제인가?
A. 대부분 Nginx proxy 또는 backend 실행 상태 문제다.

Q. Docker에서 502가 나오면 무엇을 확인해야 하는가?
A. service name, Docker network, backend container 상태, port를 확인해야 한다.

Q. backend는 정상인데 Nginx만 502면 무엇을 확인해야 하는가?
A. Nginx 컨테이너나 서버에서 backend 주소로 접근 가능한지 확인해야 한다.

---

## 9.3 Nginx MIME Type Error

### [개념]

Nginx MIME Type Error는 JS, CSS 같은 파일 요청에 대해 잘못된 `Content-Type`이 반환되어 브라우저가 실행을 거부하는 문제다.

---

### [핵심]

대표 증상:

```text
Expected a JavaScript module script
but the server responded with a MIME type of text/html
```

대표 원인:

- JS 요청에 index.html 반환
- asset 파일 없음
- fallback이 asset 요청을 처리
- Nginx mime.types 누락
- 잘못된 file extension
- base path 오류

---

### [실무]

Troubleshooting Flow:

```text
Network에서 JS 요청 선택
→ Response Headers Content-Type 확인
→ Response Body 확인
→ 파일 실제 존재 확인
→ fallback 설정 확인
→ mime.types include 확인
```

Nginx mime 설정:

```nginx
http {
  include /etc/nginx/mime.types;
}
```

판단 기준:

```text
Content-Type text/html + body index.html
→ fallback/asset path 문제

Content-Type text/plain
→ mime.types 설정 문제 가능성
```

---

### [FAQ]

Q. MIME Type Error는 왜 발생하는가?
A. JS/CSS 요청에 HTML이 반환되거나 Nginx가 잘못된 Content-Type을 보냈기 때문이다.

Q. JS 요청이 text/html이면 무엇을 의미하는가?
A. JS 파일 대신 index.html이 반환된 것이다.

Q. Nginx에서 mime.types는 왜 필요한가?
A. 파일 확장자에 맞는 Content-Type을 반환하기 위해 필요하다.

Q. MIME Type Error는 어디서 확인하는가?
A. Browser Console과 Network Response Headers에서 확인한다.

---

## 9.4 Nginx Permission Error

### [개념]

Nginx Permission Error는 Nginx 프로세스가 정적 파일을 읽거나 로그를 쓰거나 인증서 파일에 접근할 권한이 없을 때 발생하는 문제다.

---

### [핵심]

대표 원인:

- 정적 파일 권한 부족
- 디렉토리 실행 권한 부족
- Docker volume permission 문제
- SSL certificate 권한 문제
- Nginx worker user와 파일 소유자 불일치
- SELinux/AppArmor 제한

증상:

- 403 Forbidden
- error log permission denied
- SSL 로딩 실패
- 정적 파일 접근 실패

---

### [실무]

확인 명령:

```bash
ls -al /usr/share/nginx/html
namei -l /usr/share/nginx/html/index.html
tail -f /var/log/nginx/error.log
```

일반 권한 기준:

```text
directory
→ execute permission 필요

file
→ read permission 필요
```

Docker 환경:

```text
volume mount 파일 권한
→ nginx user가 읽을 수 있어야 함
```

---

### [FAQ]

Q. Nginx 403 Forbidden은 무엇을 확인해야 하는가?
A. 파일 권한, 디렉토리 권한, root 경로, index.html 존재 여부를 확인해야 한다.

Q. permission denied는 어디서 확인하는가?
A. Nginx error log에서 확인한다.

Q. 디렉토리에 execute 권한이 필요한 이유는?
A. 디렉토리 내부 파일에 접근하려면 디렉토리 실행 권한이 필요하기 때문이다.

Q. Docker volume에서 권한 문제가 생기면 무엇을 확인하는가?
A. host 파일 권한과 컨테이너 내부 Nginx user 권한을 확인해야 한다.

---

# 10. Agent Decision Rules

## 10.1 PM Agent Rules

### [개념]

PM Agent는 Nginx 배포 방식, static root, API proxy, HTTPS, cache, 검증 기준을 정의해야 한다.

---

### [핵심]

PM Agent 확인 항목:

- Nginx 사용 목적
- Build Tool
- Output Directory
- Nginx Root
- SPA Fallback 필요 여부
- API Proxy path
- Backend upstream
- WebSocket path
- HTTPS 필요 여부
- Cache 정책
- Docker 사용 여부
- 검증 URL 목록

---

### [실무]

PM Agent 산출물 예:

```text
Deployment Type: Nginx
Build Tool: Vite
Output Directory: dist
Nginx Root: /usr/share/nginx/html
SPA Fallback: try_files $uri $uri/ /index.html
API Proxy: /api/ → backend:8080/api/
WebSocket Proxy: /ws/ → backend:8080/ws/
HTTPS: required
Cache: index no-cache, assets long-cache
Verification:
- /
- /login refresh
- /api/health
- /assets/index.js
- /ws connection
```

PM Agent 판단 Flow:

```text
배포 목적 확인
→ Nginx 적합성 판단
→ static hosting 구조 정의
→ proxy 구조 정의
→ fallback/cache/https 기준 정의
→ Review Agent 체크리스트 전달
```

---

### [FAQ]

Q. PM Agent는 Nginx 배포에서 무엇을 정해야 하는가?
A. static root, output directory, fallback, API proxy, HTTPS, cache, 검증 범위를 정해야 한다.

Q. PM Agent가 proxy_pass까지 정해야 하는가?
A. 백엔드 upstream과 API prefix 전략을 정리해야 Review와 구현이 안정적이다.

Q. PM Agent가 HTTPS 여부를 판단해야 하는가?
A. 그렇다. 운영 배포라면 HTTPS와 Mixed Content 대응이 필요하다.

Q. PM Agent가 WebSocket proxy도 고려해야 하는가?
A. 실시간 기능이 있다면 `/ws` proxy와 `wss://` 기준을 포함해야 한다.

---

## 10.2 Frontend Agent Rules

### [개념]

Frontend Agent는 Nginx 배포 구조에 맞게 Build Output, API Base URL, WebSocket URL, Router basename, asset base path를 구성해야 한다.

---

### [핵심]

Frontend Agent 필수 기준:

- Build Tool별 output directory 준수
- API Base URL을 `/api` 또는 Nginx proxy 기준으로 설정
- WebSocket URL을 `/ws` 또는 `wss://` 기준으로 설정
- 운영 localhost 하드코딩 금지
- Vite `base` 또는 CRA `homepage` 확인
- BrowserRouter 사용 시 fallback 필요성 전달
- Sub Path Hosting 시 basename 설정
- Build 후 static preview 또는 Nginx 배포 검증

---

### [실무]

API client 예:

```js
export const api = axios.create({
  baseURL: "/api",
  timeout: 10000,
});
```

WebSocket URL 예:

```js
const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
const wsUrl = `${protocol}//${window.location.host}/ws`;
```

Frontend Agent 검증 기준:

```text
npm run build 성공
→ output directory 확인
→ Nginx root 배포
→ / 접속
→ route 새로고침
→ /api 요청
→ /ws 연결
```

---

### [FAQ]

Q. Frontend Agent는 Nginx 배포에서 API Base URL을 어떻게 설정하는가?
A. Same Origin Proxy 구조라면 `/api`를 사용하는 것이 단순하다.

Q. Nginx 배포에서 localhost API URL을 써도 되는가?
A. 운영에서는 쓰면 안 된다. Nginx proxy 기준의 `/api` 또는 운영 API URL을 사용해야 한다.

Q. Frontend Agent가 Nginx 설정을 직접 작성해야 하는가?
A. 보통 DevOps/Backend Agent가 작성하지만 Frontend Agent는 필요한 route, API, WebSocket 경로를 전달해야 한다.

Q. WebSocket URL도 Nginx 구조에 맞춰야 하는가?
A. 그렇다. HTTPS 운영이면 `wss://` 또는 same-origin 기반 protocol 계산을 사용해야 한다.

---

## 10.3 DevOps Agent Rules

### [개념]

DevOps Agent는 Nginx 설정, reverse proxy, HTTPS, cache, Docker 배포, 로그와 reload 절차를 구현해야 한다.

---

### [핵심]

DevOps Agent 필수 기준:

- Nginx root 설정
- Build Output 복사
- SPA fallback 설정
- `/api` reverse proxy 설정
- `/ws` WebSocket proxy 설정
- proxy header 설정
- HTTPS redirect / TLS 설정
- cache header 설정
- gzip 설정
- `nginx -t` 검증
- reload / restart 절차
- access/error log 확인
- Docker network 확인

---

### [실무]

DevOps Agent 구현 Flow:

```text
Build Output 준비
→ Nginx root 배치
→ default.conf 작성
→ API proxy 설정
→ fallback 설정
→ cache/gzip 설정
→ nginx -t
→ reload
→ smoke test
```

기본 smoke test:

```bash
curl -I http://example.com/
curl -I http://example.com/login
curl -I http://example.com/api/health
```

Docker 검증:

```bash
docker compose ps
docker compose logs nginx
docker exec -it nginx nginx -t
```

---

### [FAQ]

Q. DevOps Agent는 Nginx 배포에서 무엇을 구현해야 하는가?
A. static hosting, reverse proxy, fallback, HTTPS, cache, gzip, reload, 로그 확인을 구현해야 한다.

Q. Nginx 설정 후 가장 먼저 할 것은 무엇인가?
A. `nginx -t`로 문법 검증 후 reload해야 한다.

Q. DevOps Agent가 Backend log도 확인해야 하는가?
A. API proxy 문제를 구분하려면 Nginx log와 Backend log를 함께 확인해야 한다.

Q. Docker 배포에서 DevOps Agent가 확인할 것은?
A. Nginx와 backend가 같은 network에 있고 service name으로 접근 가능한지 확인해야 한다.

---

## 10.4 Review Agent Rules

### [개념]

Review Agent는 Nginx 배포 결과가 정적 파일, SPA fallback, API proxy, HTTPS, cache, WebSocket 관점에서 정상인지 검토해야 한다.

---

### [핵심]

Review Agent Checklist:

```md
- [ ] React Build가 성공했는가?
- [ ] 올바른 output directory를 Nginx root에 배치했는가?
- [ ] index.html이 root에 있는가?
- [ ] JS / CSS asset이 200으로 로드되는가?
- [ ] BrowserRouter route 새로고침이 정상인가?
- [ ] `/api` 요청이 backend로 proxy되는가?
- [ ] API 응답이 JSON인가?
- [ ] API 요청이 index.html을 반환하지 않는가?
- [ ] WebSocket 사용 시 `/ws` proxy가 있는가?
- [ ] HTTPS 페이지에서 HTTP API를 호출하지 않는가?
- [ ] X-Forwarded-\* header가 전달되는가?
- [ ] index.html cache가 과도하지 않은가?
- [ ] hashed assets cache가 적절한가?
- [ ] Nginx access/error log에 critical error가 없는가?
- [ ] `nginx -t`가 통과했는가?
```

---

### [실무]

Review Agent 판단 Flow:

```text
Build Output 확인
→ Nginx config 확인
→ nginx -t 확인
→ / 접속
→ route refresh
→ asset Network 확인
→ /api Network 확인
→ /ws 확인
→ HTTPS/Mixed Content 확인
→ log 확인
```

Critical Issue:

```text
index.html 없음
JS/CSS 404
API 요청에 index.html 반환
502 Bad Gateway
HTTPS에서 HTTP API 호출
WebSocket upgrade 실패
Nginx config syntax error
```

승인 기준:

```text
정적 파일 정상
SPA fallback 정상
API proxy 정상
HTTPS 정상
WebSocket 정상
Cache 정책 적정
Critical log 없음
```

---

### [FAQ]

Q. Review Agent는 Nginx 배포에서 무엇을 가장 먼저 확인해야 하는가?
A. index.html 위치와 JS/CSS asset 로드 상태를 먼저 확인해야 한다.

Q. API 요청에 index.html이 반환되면 승인 가능한가?
A. 아니다. fallback과 proxy 분리가 실패한 치명적 문제다.

Q. 502 Bad Gateway가 있으면 승인 가능한가?
A. 아니다. backend upstream 연결 문제를 해결해야 한다.

Q. HTTPS 페이지에서 HTTP API 호출이 있으면 승인 가능한가?
A. 아니다. Mixed Content로 차단될 수 있다.

---

# 11. Common Mistakes

## 11.1 Nginx Deployment Common Mistakes

### [개념]

Nginx Deployment Common Mistakes는 React 정적 배포, SPA fallback, API proxy, HTTPS, cache 설정에서 반복적으로 발생하는 실수다.

---

### [핵심]

자주 발생하는 실수:

- React Source Code를 Nginx root에 배포
- `npm run build` 없이 배포
- Vite `dist` 대신 `build`를 찾음
- CRA `build` 대신 `dist`를 찾음
- `dist` 또는 `build` 폴더 자체를 root에 넣음
- Nginx root에 `index.html`이 없음
- `try_files` fallback 누락
- `/api` 요청이 `index.html`로 fallback
- JS/CSS 요청이 `index.html`로 fallback
- `proxy_pass` slash 처리 오류
- backend service name을 브라우저 API URL로 사용
- Nginx와 backend가 다른 Docker network에 있음
- `X-Forwarded-Proto` 누락
- HTTPS 페이지에서 HTTP API 호출
- `ws://`를 HTTPS 페이지에서 사용
- `client_max_body_size` 부족
- `index.html` 장기 캐시
- Runtime Config `config.json` 장기 캐시
- gzip 미설정
- 설정 수정 후 `nginx -t` / reload 누락
- Nginx log를 확인하지 않음

---

### [실무]

실수별 판단:

```text
루트 404
→ Nginx root / index.html 위치 확인

새로고침 404
→ try_files fallback 확인

API HTML 응답
→ /api location / fallback 분리 확인

502 Bad Gateway
→ backend upstream / Docker network 확인

MIME type error
→ asset 요청이 index.html 반환되는지 확인

413 error
→ client_max_body_size 확인

Mixed Content
→ HTTPS API / wss 확인

변경사항 미반영
→ cache header / browser cache / CDN 확인
```

---

### [FAQ]

Q. Nginx 배포에서 가장 흔한 실수는 무엇인가?
A. Build Output 내부 파일이 아니라 `dist` 또는 `build` 폴더 자체를 잘못된 위치에 넣는 것이다.

Q. Nginx 배포에서 가장 치명적인 실수는 무엇인가?
A. API 요청이나 JS 요청에 index.html이 반환되는 fallback/proxy 충돌이다.

Q. Docker Nginx에서 자주 나는 실수는 무엇인가?
A. 브라우저에서 Docker service name을 직접 호출하거나 Nginx와 backend가 같은 network에 없어서 502가 나는 실수다.

Q. Nginx 설정을 바꿨는데 반영되지 않는 이유는?
A. reload 누락, Docker image 재빌드 누락, volume mount 경로 오류를 확인해야 한다.

---

# 12. Part08 Quality Checklist

## 12.1 Document Quality

### [개념]

이 문서는 Frontend Build & Deploy Domain의 Part08이며 Nginx Deployment Rules Retrieval에 최적화되어야 한다.

---

### [핵심]

문서 품질 기준:

- Nginx Deployment 정의 포함
- Nginx 배포 적합성 판단 기준 포함
- Nginx root rules 포함
- Vite dist with Nginx 포함
- CRA build with Nginx 포함
- try_files SPA fallback 포함
- API/fallback separation 포함
- proxy_pass rules 포함
- proxy slash rules 포함
- proxy headers 포함
- timeout/body size 포함
- WebSocket proxy 포함
- STOMP/SockJS proxy 포함
- HTTPS/TLS 포함
- Mixed Content 포함
- Cache Header 포함
- Gzip/Brotli 포함
- Logging/Debugging 포함
- Troubleshooting Flow 포함
- Agent별 판단 기준 포함
- Common Mistakes 포함
- Retrieval Queries 포함

---

### [실무]

Part08은 다음 문서와 연결된다.

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

Q. Part08의 핵심 목적은 무엇인가?
A. React SPA를 Nginx로 배포할 때 static root, SPA fallback, API proxy, HTTPS, cache 문제를 Agent가 정확히 판단하게 하는 것이다.

Q. Part08에서 Docker 전체 배포를 다루는가?
A. 아니다. Nginx와 Docker가 연결되는 지점만 다루고 Docker 상세 배포는 후속 Part에서 다룬다.

Q. Part08에서 CI/CD 전체를 다루는가?
A. 아니다. Nginx 배포 검증 기준만 다루고 CI/CD 상세 전략은 후속 Part에서 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. Nginx Deployment란 무엇인가?
A. React Build 결과물을 Nginx가 정적 파일로 제공하고 API 요청은 백엔드로 proxy하는 배포 방식이다.

Q. React 앱을 Nginx로 배포하려면 무엇을 올려야 하는가?
A. Source Code가 아니라 `dist` 또는 `build` 내부의 Build Output을 올려야 한다.

Q. Nginx 배포에서 가장 중요한 설정은 무엇인가?
A. static root, SPA fallback, `/api` proxy, cache, HTTPS 설정이다.

Q. Nginx root란 무엇인가?
A. Nginx가 정적 파일을 찾는 기준 디렉토리다.

Q. React index.html은 Nginx 어디에 있어야 하는가?
A. 일반적으로 Nginx root 바로 아래에 있어야 한다.

Q. Vite를 Nginx로 배포할 때 어떤 폴더를 복사하는가?
A. `dist` 내부 파일을 Nginx root로 복사한다.

Q. CRA를 Nginx로 배포할 때 어떤 폴더를 복사하는가?
A. `build` 내부 파일을 Nginx root로 복사한다.

Q. dist 폴더 자체를 Nginx root에 넣어도 되는가?
A. 보통 권장하지 않는다. `dist` 내부 파일이 root 기준으로 제공되어야 한다.

Q. Nginx에서 React 새로고침 404는 어떻게 해결하는가?
A. `try_files $uri $uri/ /index.html;` 설정으로 frontend route를 index.html로 fallback한다.

Q. try_files $uri는 왜 필요한가?
A. 실제 JS, CSS, 이미지 파일을 먼저 제공하기 위해 필요하다.

Q. Nginx에서 API와 SPA fallback을 왜 분리해야 하는가?
A. API 요청에 index.html이 반환되는 문제를 막기 위해 필요하다.

Q. API 요청에 HTML이 오면 무엇을 확인해야 하는가?
A. `/api/` location과 `proxy_pass`, fallback 우선순위를 확인해야 한다.

Q. Backend log에 요청이 없는데 프론트에서는 API 200이면 무엇을 의심하는가?
A. Nginx가 API 요청을 backend로 보내지 않고 index.html을 반환했을 가능성이 있다.

Q. proxy_pass는 무엇인가?
A. Nginx가 받은 요청을 백엔드 서버로 전달하는 reverse proxy 설정이다.

Q. Docker Compose에서 proxy_pass에 backend를 쓸 수 있는가?
A. 같은 Docker network 안에서 service name이 `backend`라면 가능하다.

Q. 브라우저에서 [http://backend:8080을](http://backend:8080을) 호출해도 되는가?
A. 안 된다. 브라우저는 Docker 내부 service name을 알 수 없다. Nginx가 proxy해야 한다.

Q. proxy_pass에서 slash가 중요한가?
A. 중요하다. slash 유무에 따라 백엔드로 전달되는 path가 달라질 수 있다.

Q. API 404가 Nginx에서만 발생하면 무엇을 확인하는가?
A. `location`과 `proxy_pass`의 slash 처리, backend controller path를 확인해야 한다.

Q. /api/api가 생기는 이유는 무엇인가?
A. frontend baseURL, Nginx proxy_pass, backend path에 `/api`가 중복되었을 수 있다.

Q. proxy_set_header는 왜 필요한가?
A. 백엔드가 원래 요청의 host, protocol, client IP를 알 수 있게 하기 위해 필요하다.

Q. X-Forwarded-Proto는 왜 중요한가?
A. HTTPS reverse proxy 뒤에서 백엔드가 원래 요청이 HTTPS였는지 판단하는 데 필요하다.

Q. 413 Request Entity Too Large는 무엇인가?
A. 요청 body가 Nginx의 허용 크기보다 커서 거부된 것이다.

Q. 파일 업로드가 실패하면 Nginx에서 무엇을 확인해야 하는가?
A. `client_max_body_size` 설정을 확인해야 한다.

Q. 504 Gateway Timeout은 무엇을 의미하는가?
A. Nginx가 백엔드 응답을 제한 시간 안에 받지 못한 것이다.

Q. Nginx에서 WebSocket proxy는 일반 API proxy와 같은가?
A. 유사하지만 Upgrade header와 HTTP/1.1 설정이 추가로 필요하다.

Q. WebSocket 연결에서 101은 무엇인가?
A. HTTP 연결이 WebSocket으로 전환되었음을 의미하는 정상 상태다.

Q. HTTPS 페이지에서 ws://를 써도 되는가?
A. 안 된다. HTTPS 페이지에서는 `wss://`를 사용해야 한다.

Q. SockJS를 쓰면 Nginx에서 무엇을 주의해야 하는가?
A. WebSocket뿐 아니라 `/ws/**` 하위 HTTP fallback 요청도 백엔드로 proxy해야 한다.

Q. HTTPS Termination이란 무엇인가?
A. Nginx가 HTTPS 요청을 받고 내부 백엔드로는 HTTP로 전달하는 구조다.

Q. HTTPS 페이지에서 HTTP API를 호출하면 어떻게 되는가?
A. Mixed Content로 차단될 수 있다.

Q. Mixed Content란 무엇인가?
A. HTTPS 페이지에서 HTTP 리소스를 호출해 브라우저가 차단하는 문제다.

Q. index.html은 왜 no-cache가 좋은가?
A. 새 배포 시 최신 JS/CSS hash를 참조해야 하기 때문이다.

Q. hashed JS/CSS는 왜 long cache가 가능한가?
A. 파일 내용이 바뀌면 hash 파일명도 바뀌기 때문이다.

Q. config.json은 왜 no-store가 필요한가?
A. Runtime Config 값은 배포 후 변경될 수 있으므로 오래 캐시하면 안 된다.

Q. Nginx gzip은 왜 사용하는가?
A. JS, CSS, JSON 같은 텍스트 파일 전송 크기를 줄이기 위해 사용한다.

Q. 압축이 적용되었는지 어디서 확인하는가?
A. Network Response Headers의 `Content-Encoding`에서 확인한다.

Q. Nginx access log에서는 무엇을 확인하는가?
A. 요청 path, status code, static asset 요청, API 요청 도달 여부를 확인한다.

Q. Nginx error log에서는 무엇을 확인하는가?
A. 파일 없음, upstream 실패, 권한 문제, timeout 같은 서버 오류를 확인한다.

Q. Nginx 설정을 바꾼 뒤 무엇을 해야 하는가?
A. `nginx -t`로 문법 확인 후 reload해야 한다.

Q. nginx -t가 성공하면 배포가 완전히 정상인가?
A. 아니다. 문법만 검증하므로 route, proxy, asset, API는 별도로 테스트해야 한다.

Q. Nginx에서 / 가 404면 무엇을 확인해야 하는가?
A. root 경로와 `index.html` 위치를 확인해야 한다.

Q. /login만 404면 무엇을 확인해야 하는가?
A. React SPA fallback 설정인 `try_files`를 확인해야 한다.

Q. /assets 파일이 404면 무엇을 확인해야 하는가?
A. Build Output 복사 여부, Vite base, Nginx root를 확인해야 한다.

Q. 502 Bad Gateway는 무엇인가?
A. Nginx가 backend upstream에 연결하지 못했다는 의미다.

Q. Docker에서 502가 나오면 무엇을 확인해야 하는가?
A. service name, Docker network, backend container 상태, port를 확인해야 한다.

Q. MIME Type Error는 왜 발생하는가?
A. JS/CSS 요청에 HTML이 반환되거나 Nginx가 잘못된 Content-Type을 보냈기 때문이다.

Q. Nginx 403 Forbidden은 무엇을 확인해야 하는가?
A. 파일 권한, 디렉토리 권한, root 경로, index.html 존재 여부를 확인해야 한다.

Q. PM Agent는 Nginx 배포에서 무엇을 정해야 하는가?
A. static root, output directory, fallback, API proxy, HTTPS, cache, 검증 범위를 정해야 한다.

Q. Frontend Agent는 Nginx 배포에서 API Base URL을 어떻게 설정하는가?
A. Same Origin Proxy 구조라면 `/api`를 사용하는 것이 단순하다.

Q. DevOps Agent는 Nginx 배포에서 무엇을 구현해야 하는가?
A. static hosting, reverse proxy, fallback, HTTPS, cache, gzip, reload, 로그 확인을 구현해야 한다.

Q. Review Agent는 Nginx 배포에서 무엇을 가장 먼저 확인해야 하는가?
A. index.html 위치와 JS/CSS asset 로드 상태를 먼저 확인해야 한다.

Q. Nginx 배포에서 가장 흔한 실수는 무엇인가?
A. Build Output 내부 파일이 아니라 `dist` 또는 `build` 폴더 자체를 잘못된 위치에 넣는 것이다.

Q. Part08 다음 문서는 무엇인가?
A. Part09 Docker Deployment Rules로 이어지는 것이 적합하다.
