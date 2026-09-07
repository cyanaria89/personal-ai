# Frontend Build & Deploy Part05 - Static File Hosting Rules

---

# 1. Static File Hosting Core

## 1.1 Static File Hosting Definition

### [개념]

Static File Hosting은 Build 결과물로 생성된 HTML, CSS, JavaScript, 이미지, 폰트 같은 정적 파일을 웹 서버 또는 배포 플랫폼이 브라우저에 제공하는 방식이다.

대표 정적 파일:

```text
index.html
assets/index.[hash].js
assets/index.[hash].css
static/js/main.[hash].js
static/css/main.[hash].css
favicon.ico
manifest.json
image files
font files
```

대표 Hosting 대상:

```text
Nginx
Apache
Spring Boot static resource
Vercel
Netlify
AWS S3
CloudFront
GitHub Pages
Docker + Nginx
```

---

### [핵심]

Static File Hosting 핵심 규칙:

- Build Output을 정적 파일 서버에 배포한다.
- Source Code를 그대로 배포하지 않는다.
- `index.html`이 hosting root에서 제공되어야 한다.
- JS / CSS / Asset 경로가 서버 root와 일치해야 한다.
- React Router 사용 시 SPA fallback이 필요하다.
- API 요청과 정적 파일 요청을 구분해야 한다.
- Cache 정책은 `index.html`과 hashed assets를 분리한다.
- 배포 후 Network 탭에서 asset 404를 확인해야 한다.

---

### [실무]

2026 실무 기준으로 React SPA 배포는 정적 파일 Hosting 구조를 정확히 이해해야 한다.

기본 Flow:

```text
Frontend Source Code
→ npm run build
→ Build Output 생성
→ Static Hosting Server 업로드
→ Browser requests index.html
→ Browser loads JS / CSS assets
→ React App boot
→ Backend API request
```

Vite Hosting 예:

```text
frontend/dist/*
→ hosting root
```

CRA Hosting 예:

```text
frontend/build/*
→ hosting root
```

Agent 판단 Flow:

```text
Build Tool 확인
→ Output Directory 확인
→ Hosting Root 확인
→ index.html 위치 확인
→ asset 경로 확인
→ SPA fallback 필요 여부 확인
→ API path 충돌 확인
→ cache 정책 확인
```

---

### [FAQ]

Q. Static File Hosting은 무엇인가?
A. Build 결과물인 HTML, CSS, JavaScript, 이미지 파일을 웹 서버나 플랫폼이 브라우저에 제공하는 방식이다.

Q. React Build 결과물은 서버 프로그램인가?
A. 아니다. 일반 React SPA Build 결과물은 정적 파일이며, 별도 정적 파일 서버가 제공해야 한다.

Q. Source Code를 그대로 서버에 올려도 되는가?
A. 아니다. 보통 `npm run build` 결과물인 `dist` 또는 `build` 내부 파일을 올려야 한다.

Q. Static Hosting에서 가장 먼저 확인할 것은 무엇인가?
A. `index.html`이 hosting root에서 정상 제공되는지 확인해야 한다.

---

## 1.2 Static File Request Flow

### [개념]

Static File Request Flow는 브라우저가 정적 파일 서버에서 `index.html`, JavaScript, CSS, Asset을 순서대로 받아 React App을 실행하는 흐름이다.

---

### [핵심]

정상 Flow:

```text
Browser requests /
→ Server returns index.html
→ Browser parses index.html
→ Browser requests JS bundle
→ Browser requests CSS bundle
→ React App boot
→ React Router renders page
→ API client sends request
```

장애 Flow:

```text
Browser requests /
→ Server returns index.html
→ JS bundle request 404
→ React App boot 실패
→ White Screen
```

---

### [실무]

2026 실무 기준으로 흰 화면 문제는 Static File Request Flow에서 JS / CSS asset 로드 실패를 먼저 확인한다.

Network 검증 항목:

```md
- [ ] `/` 또는 배포 base path가 `index.html`을 반환하는가?
- [ ] JS bundle이 200으로 로드되는가?
- [ ] CSS bundle이 200으로 로드되는가?
- [ ] 이미지와 폰트가 200으로 로드되는가?
- [ ] 404 asset이 없는가?
- [ ] Content-Type이 올바른가?
- [ ] API 요청이 index.html을 반환하지 않는가?
```

Content-Type 예:

```text
index.html → text/html
JavaScript → application/javascript 또는 text/javascript
CSS → text/css
JSON API → application/json
```

---

### [FAQ]

Q. 화면이 흰색이면 무엇을 먼저 확인해야 하는가?
A. Network 탭에서 JS bundle과 CSS bundle이 200으로 로드되는지 먼저 확인한다.

Q. index.html은 뜨는데 React 화면이 안 뜨는 이유는?
A. JS bundle 404, runtime error, asset path 오류, 환경 변수 오류가 원인일 수 있다.

Q. API 요청의 Content-Type이 text/html이면 무엇을 의심해야 하는가?
A. API 요청이 SPA fallback에 잡혀 index.html을 반환하고 있을 가능성이 높다.

Q. Static File Request Flow에서 가장 중요한 파일은 무엇인가?
A. `index.html`과 그 안에서 참조하는 JS bundle이다.

---

# 2. Build Output Hosting

## 2.1 Vite Dist Hosting

### [개념]

Vite Dist Hosting은 Vite Build 결과물인 `dist` 폴더 내부 파일을 정적 Hosting Root에 배포하는 방식이다.

---

### [핵심]

Vite Build 기본 구조:

```text
dist/
├ index.html
└ assets/
   ├ index.[hash].js
   ├ index.[hash].css
   └ image.[hash].png
```

Hosting 대상:

```text
dist 내부 파일 전체
```

중요 규칙:

- `dist` 폴더 자체가 아니라 내부 파일이 hosting root 기준으로 제공되는지 확인한다.
- `index.html`이 root에서 접근 가능해야 한다.
- `assets/` 경로가 index.html 기준과 일치해야 한다.
- Vite `base` 설정이 배포 경로와 일치해야 한다.

---

### [실무]

Nginx Hosting 예:

```text
dist/index.html
→ /usr/share/nginx/html/index.html

dist/assets/*
→ /usr/share/nginx/html/assets/*
```

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
```

검증 Flow:

```text
npm run build
→ dist 생성 확인
→ dist/index.html 확인
→ dist/assets 확인
→ 정적 서버 root에 복사
→ Network asset 404 확인
```

---

### [FAQ]

Q. Vite Build 결과물은 어디에 생기는가?
A. 기본적으로 `dist` 폴더에 생성된다.

Q. Vite 배포 시 dist 폴더 자체를 올리는가?
A. Hosting 방식에 따라 다르지만 일반적으로 `dist` 내부 파일이 hosting root에서 제공되어야 한다.

Q. Vite에서 JS/CSS 404가 나면 무엇을 확인해야 하는가?
A. `base` 설정, hosting root, `dist/assets` 복사 여부를 확인해야 한다.

Q. Vite 배포 후 흰 화면이 나오면 무엇을 확인해야 하는가?
A. Network 탭에서 `assets/*.js`, `assets/*.css`가 정상 로드되는지 확인한다.

---

## 2.2 CRA Build Hosting

### [개념]

CRA Build Hosting은 CRA Build 결과물인 `build` 폴더 내부 파일을 정적 Hosting Root에 배포하는 방식이다.

---

### [핵심]

CRA Build 기본 구조:

```text
build/
├ index.html
├ static/
│  ├ js/
│  │  └ main.[hash].js
│  └ css/
│     └ main.[hash].css
├ favicon.ico
└ manifest.json
```

Hosting 대상:

```text
build 내부 파일 전체
```

중요 규칙:

- `build/index.html`이 hosting root에서 제공되어야 한다.
- `build/static/` 경로가 유지되어야 한다.
- CRA `homepage` 설정이 배포 경로와 일치해야 한다.
- React Router 사용 시 SPA fallback이 필요하다.

---

### [실무]

Spring Boot 통합 배포 예:

```text
frontend/build/index.html
→ backend/src/main/resources/static/index.html

frontend/build/static/*
→ backend/src/main/resources/static/static/*
```

비권장 구조:

```text
backend/src/main/resources/static/build/index.html
```

위 구조는 `/` 요청에서 `index.html`을 못 찾을 수 있다.

정적 서버 preview:

```bash
npm run build
npx serve -s build
```

---

### [FAQ]

Q. CRA Build 결과물은 어디에 생기는가?
A. 기본적으로 `build` 폴더에 생성된다.

Q. CRA 배포 시 build 폴더 전체를 static 안에 넣으면 되는가?
A. 대부분 `build` 내부 파일이 hosting root에 위치해야 한다.

Q. CRA에서 JS/CSS 404가 나면 무엇을 확인해야 하는가?
A. `homepage`, hosting root, `build/static` 복사 여부를 확인해야 한다.

Q. CRA Build 결과를 직접 파일로 열어도 되는가?
A. 권장하지 않는다. 정적 서버로 제공해서 확인해야 한다.

---

## 2.3 Output Directory Mismatch

### [개념]

Output Directory Mismatch는 빌드 도구의 결과 폴더와 배포 설정에서 기대하는 폴더가 달라 정적 파일을 찾지 못하는 문제다.

---

### [핵심]

대표 오류:

```text
Vite project
→ output: dist
→ deploy config: build
→ 배포 파일 없음

CRA project
→ output: build
→ deploy config: dist
→ 배포 파일 없음
```

증상:

- 배포 화면 404
- index.html 없음
- JS / CSS asset 404
- 배포 플랫폼에서 output directory error
- CI/CD artifact upload 실패

---

### [실무]

배포 플랫폼 설정 예:

```text
Vite
Build Command: npm run build
Output Directory: dist

CRA
Build Command: npm run build
Output Directory: build
```

GitHub Actions artifact 예:

```yaml
- name: Upload artifact
  uses: actions/upload-pages-artifact@v3
  with:
    path: ./frontend/dist
```

CRA라면:

```yaml
path: ./frontend/build
```

Troubleshooting Flow:

```text
Build Tool 확인
→ npm run build 실행
→ 실제 생성 폴더 확인
→ deploy config output directory 확인
→ hosting root 확인
```

---

### [FAQ]

Q. Vite 프로젝트인데 build 폴더가 없는 것은 문제인가?
A. 아니다. Vite 기본 output은 `dist`다.

Q. CRA 프로젝트인데 dist 폴더가 없는 것은 문제인가?
A. 아니다. CRA 기본 output은 `build`다.

Q. 배포 플랫폼에서 output directory 오류가 나면 무엇을 확인해야 하는가?
A. Build Tool과 실제 생성된 output directory를 확인해야 한다.

Q. Output Directory가 틀리면 어떤 문제가 발생하는가?
A. index.html을 찾지 못하거나 JS/CSS asset 404가 발생할 수 있다.

---

# 3. Hosting Root and Asset Path

## 3.1 Hosting Root

### [개념]

Hosting Root는 웹 서버가 정적 파일을 찾는 기준 디렉토리다.

예:

```text
Nginx root /usr/share/nginx/html;
Spring Boot src/main/resources/static
S3 bucket root
Netlify publish directory
Vercel output directory
```

---

### [핵심]

Hosting Root 기준:

- `index.html`이 root에 있어야 한다.
- JS / CSS asset 경로가 root 기준으로 맞아야 한다.
- 빌드 output 내부 구조를 유지해야 한다.
- root가 한 단계 밀리면 화면이 뜨지 않을 수 있다.
- 하위 경로 배포 시 base path 설정이 필요할 수 있다.

잘못된 구조:

```text
/usr/share/nginx/html/dist/index.html
```

정상 구조:

```text
/usr/share/nginx/html/index.html
/usr/share/nginx/html/assets/index.[hash].js
```

---

### [실무]

Nginx root 예:

```nginx
server {
  root /usr/share/nginx/html;
  index index.html;

  location / {
    try_files $uri $uri/ /index.html;
  }
}
```

검증 Flow:

```text
Hosting Root 확인
→ index.html 위치 확인
→ index.html 내부 script src 확인
→ 실제 asset 파일 위치 확인
→ Browser Network 확인
```

Agent 판단 기준:

```text
index.html 404
→ hosting root 오류 가능성

index.html 200 + JS 404
→ asset path / base path / file copy 오류 가능성

API가 index.html
→ fallback / proxy 경로 오류 가능성
```

---

### [FAQ]

Q. Hosting Root란 무엇인가?
A. 웹 서버가 정적 파일을 찾는 기준 디렉토리다.

Q. index.html은 어디에 있어야 하는가?
A. 일반적으로 hosting root 바로 아래에 있어야 한다.

Q. dist 폴더를 root 안에 통째로 넣으면 안 되는가?
A. 서버 설정에 따라 다르지만 root가 `dist` 내부를 바라보지 않으면 `/dist/index.html` 구조가 되어 문제가 생길 수 있다.

Q. index.html은 200인데 JS가 404면 무엇을 확인해야 하는가?
A. asset path, base path, hosting root, 파일 복사 누락을 확인해야 한다.

---

## 3.2 Asset Path Rules

### [개념]

Asset Path는 `index.html`이 JS, CSS, 이미지, 폰트 같은 정적 파일을 참조하는 경로다.

예:

```html
<script type="module" src="/assets/index.abc123.js"></script>
<link rel="stylesheet" href="/assets/index.def456.css" />
```

---

### [핵심]

Asset Path 문제 원인:

- Vite `base` 설정 오류
- CRA `homepage` 설정 오류
- Hosting Root 오류
- 하위 경로 배포 설정 누락
- 파일 복사 누락
- 대소문자 불일치
- public asset 경로 오류
- CDN 경로 오류

증상:

- 흰 화면
- CSS 미적용
- 이미지 깨짐
- 폰트 미로드
- JS 404
- MIME type error

---

### [실무]

Vite root 배포:

```js
export default defineConfig({
  base: "/",
});
```

Vite 하위 경로 배포:

```js
export default defineConfig({
  base: "/my-app/",
});
```

CRA 하위 경로 배포:

```json
{
  "homepage": "/my-app"
}
```

검증 Flow:

```text
index.html 열기
→ script/link 경로 확인
→ Network에서 asset 404 확인
→ base/homepage 확인
→ hosting root 확인
→ redeploy
```

---

### [FAQ]

Q. Asset Path란 무엇인가?
A. 브라우저가 JS, CSS, 이미지, 폰트 파일을 불러오는 경로다.

Q. 배포 후 CSS가 안 먹는 이유는?
A. CSS asset 경로가 틀렸거나 파일이 hosting root에 없을 수 있다.

Q. 배포 후 이미지가 깨지는 이유는?
A. public path, import path, 파일명 대소문자, asset 복사 누락을 확인해야 한다.

Q. MIME type error가 나면 무엇을 의심해야 하는가?
A. JS 파일 요청에 index.html이 반환되거나 Content-Type이 잘못되었을 가능성이 있다.

---

## 3.3 Sub Path Hosting

### [개념]

Sub Path Hosting은 앱을 도메인 루트(`/`)가 아닌 하위 경로에서 제공하는 배포 방식이다.

예:

```text
https://example.com/my-app/
https://username.github.io/repository-name/
```

---

### [핵심]

Sub Path Hosting 필요 설정:

- Vite `base`
- CRA `homepage`
- React Router `basename`
- Nginx location
- Spring Boot context path
- GitHub Pages repository path
- asset path
- SPA fallback path

---

### [실무]

Vite 예:

```js
export default defineConfig({
  base: "/my-app/",
});
```

React Router 예:

```jsx
<BrowserRouter basename="/my-app">
  <App />
</BrowserRouter>
```

Nginx 예:

```nginx
location /my-app/ {
  alias /usr/share/nginx/html/;
  try_files $uri $uri/ /my-app/index.html;
}
```

Agent 검토 Flow:

```text
배포 URL 확인
→ root 배포인지 sub path 배포인지 확인
→ Build Tool base 설정 확인
→ Router basename 확인
→ server location 확인
→ asset 404 확인
```

---

### [FAQ]

Q. Sub Path Hosting이란 무엇인가?
A. 앱을 `/`가 아니라 `/my-app` 같은 하위 경로에서 제공하는 방식이다.

Q. 하위 경로 배포 시 무엇을 설정해야 하는가?
A. Build Tool base path, Router basename, 서버 location을 함께 맞춰야 한다.

Q. GitHub Pages에서 React가 깨지는 이유는?
A. repository-name 하위 경로 배포인데 base path나 basename이 맞지 않을 수 있다.

Q. 하위 경로 배포에서 새로고침 404가 발생하면 무엇을 확인해야 하는가?
A. SPA fallback이 하위 경로 기준으로 설정되어 있는지 확인해야 한다.

---

# 4. Static Hosting Server Types

## 4.1 Nginx Static Hosting

### [개념]

Nginx Static Hosting은 Nginx가 React Build 결과물을 정적 파일로 제공하는 방식이다.

---

### [핵심]

Nginx 기준:

- 정적 파일 제공에 적합
- reverse proxy 설정 가능
- SPA fallback 설정 가능
- cache header 설정 가능
- gzip / brotli 압축 가능
- HTTPS termination 가능
- Docker 배포와 결합하기 좋음

---

### [실무]

기본 설정:

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

정적 파일 복사:

```text
Vite dist/*
→ /usr/share/nginx/html/

CRA build/*
→ /usr/share/nginx/html/
```

검토 항목:

```md
- [ ] root 경로가 build output과 맞는가?
- [ ] index.html이 root에 있는가?
- [ ] SPA fallback이 있는가?
- [ ] /api proxy가 fallback보다 분리되어 있는가?
- [ ] asset cache 정책이 있는가?
- [ ] gzip 설정이 필요한가?
```

---

### [FAQ]

Q. Nginx는 왜 프론트엔드 배포에 많이 사용하는가?
A. 정적 파일 제공, reverse proxy, cache, HTTPS 설정에 적합하기 때문이다.

Q. Nginx에서 React 새로고침 404는 어떻게 해결하는가?
A. `try_files $uri $uri/ /index.html;` 설정을 사용한다.

Q. Nginx에서 /api 요청이 index.html로 가면 어떻게 해야 하는가?
A. `/api` location을 별도로 분리해 백엔드로 proxy해야 한다.

Q. Nginx root가 틀리면 어떤 문제가 생기는가?
A. index.html 또는 asset 파일을 찾지 못해 404나 흰 화면이 발생한다.

---

## 4.2 Spring Boot Static Resource Hosting

### [개념]

Spring Boot Static Resource Hosting은 React Build 결과물을 Spring Boot의 정적 리소스 경로에 포함해 같은 서버에서 제공하는 방식이다.

---

### [핵심]

기본 경로:

```text
src/main/resources/static
```

통합 배포 구조:

```text
React Build Output
→ Spring Boot static directory
→ Spring Boot JAR build
→ Server run
→ Browser receives index.html
```

장점:

- 서버 하나로 배포 가능
- CORS 문제 감소
- 학원 프로젝트 / 데모 프로젝트에 단순
- 백엔드와 프론트엔드 도메인 통일

주의:

- build output 내부 파일을 static root로 복사해야 한다.
- SPA fallback이 필요할 수 있다.
- API path와 React route 충돌을 피해야 한다.
- Security 설정에서 static resource 접근 허용이 필요할 수 있다.

---

### [실무]

Vite 복사:

```text
frontend/dist/*
→ backend/src/main/resources/static/
```

CRA 복사:

```text
frontend/build/*
→ backend/src/main/resources/static/
```

정상 구조:

```text
backend/src/main/resources/static/index.html
backend/src/main/resources/static/assets/
```

또는 CRA:

```text
backend/src/main/resources/static/index.html
backend/src/main/resources/static/static/
```

검증 Flow:

```text
React build
→ static directory 복사
→ Spring Boot build/run
→ / 접속 확인
→ JS/CSS asset 확인
→ React route 새로고침 확인
→ /api 요청 확인
```

---

### [FAQ]

Q. Spring Boot에서 React Build 파일을 제공할 수 있는가?
A. 가능하다. Build 결과물을 `src/main/resources/static`에 넣으면 정적 파일로 제공할 수 있다.

Q. build 폴더 자체를 static 안에 넣어도 되는가?
A. 대부분 권장하지 않는다. build 또는 dist 내부 파일이 static root에 있어야 한다.

Q. Spring Boot 통합 배포는 언제 적합한가?
A. 학원 프로젝트, 데모, 소규모 서비스처럼 서버 하나로 단순 배포할 때 적합하다.

Q. Spring Boot 통합 배포에서 가장 주의할 점은?
A. React route와 API path 충돌, SPA fallback, static resource 위치를 주의해야 한다.

---

## 4.3 Platform Static Hosting

### [개념]

Platform Static Hosting은 Vercel, Netlify, S3, CloudFront, GitHub Pages 같은 플랫폼이 Build 결과물을 정적 파일로 제공하는 방식이다.

---

### [핵심]

대표 플랫폼:

```text
Vercel
Netlify
AWS S3
CloudFront
GitHub Pages
Cloudflare Pages
Firebase Hosting
```

공통 확인 항목:

- Build Command
- Output Directory
- Environment Variables
- SPA fallback / redirect
- Base Path
- HTTPS
- Cache
- Custom Domain
- API Base URL
- Deploy Preview 여부

---

### [실무]

Vercel / Netlify 설정 예:

```text
Vite
Build Command: npm run build
Output Directory: dist

CRA
Build Command: npm run build
Output Directory: build
```

S3 + CloudFront Flow:

```text
npm run build
→ dist/build upload to S3
→ CloudFront distribution
→ index.html fallback 설정
→ cache invalidation 필요 시 수행
```

GitHub Pages 주의:

```text
Sub Path Hosting 가능성 높음
→ base path 설정 필요
→ BrowserRouter fallback 제약
```

---

### [FAQ]

Q. Vercel이나 Netlify도 Static File Hosting인가?
A. React SPA 기준으로 Build 결과물을 정적 파일로 제공하는 방식이다.

Q. 플랫폼 배포에서 가장 중요한 설정은 무엇인가?
A. Build Command, Output Directory, Environment Variables, SPA fallback이다.

Q. S3에 React를 올리면 새로고침 404가 날 수 있는가?
A. 가능하다. SPA fallback 설정이 필요하다.

Q. GitHub Pages에서 React Router가 어려운 이유는?
A. 서버 rewrite 설정이 제한적이라 새로고침 fallback 처리에 제약이 있다.

---

# 5. SPA Fallback in Static Hosting

## 5.1 SPA Fallback Concept

### [개념]

SPA Fallback은 존재하지 않는 프론트엔드 라우트 요청에 대해 서버가 404를 반환하지 않고 `index.html`을 반환하도록 하는 설정이다.

예:

```text
User refresh /festival/10
→ Server receives /festival/10
→ Server returns index.html
→ React Router renders FestivalDetail
```

---

### [핵심]

SPA Fallback이 필요한 상황:

- React Router BrowserRouter 사용
- 직접 URL 접근
- 새로고침
- 배포 서버가 실제 route 파일을 찾으려 함
- `/login`, `/mypage`, `/detail/1` 같은 route가 서버 파일로 존재하지 않음

주의:

- API 요청까지 fallback하면 안 된다.
- static asset 요청까지 fallback하면 MIME type 문제가 생길 수 있다.
- fallback은 프론트엔드 route에만 적용해야 한다.

---

### [실무]

Nginx:

```nginx
location / {
  try_files $uri $uri/ /index.html;
}
```

Netlify:

```text
/* /index.html 200
```

Vercel:

```json
{
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

검증 Flow:

```text
메인 접속
→ React route 이동
→ 새로고침
→ 직접 URL 접근
→ API 요청이 fallback되지 않는지 확인
```

---

### [FAQ]

Q. SPA Fallback이란 무엇인가?
A. 프론트엔드 route 요청에 대해 서버가 `index.html`을 반환해 React Router가 화면을 렌더링하게 하는 설정이다.

Q. React에서 새로고침하면 404가 나는 이유는?
A. 서버가 `/login` 같은 route를 실제 파일 경로로 찾기 때문이다.

Q. SPA Fallback을 모든 요청에 적용해도 되는가?
A. 아니다. API 요청과 정적 asset 요청은 fallback 대상에서 제외해야 한다.

Q. API 요청에 index.html이 오면 무엇을 의심해야 하는가?
A. SPA fallback이 API 경로까지 잡고 있을 가능성이 높다.

---

## 5.2 Asset Fallback Risk

### [개념]

Asset Fallback Risk는 JS, CSS, 이미지 파일 요청이 실제 asset 파일이 아니라 `index.html`로 fallback되어 발생하는 문제다.

---

### [핵심]

증상:

```text
JS request → index.html response
CSS request → index.html response
MIME type error
Unexpected token '<'
White Screen
```

대표 원인:

- asset 파일 누락
- base path 오류
- 서버 fallback이 asset 요청까지 처리
- 배포 경로 오류
- CDN 캐시 mismatch
- 이전 index.html이 새 asset을 참조

---

### [실무]

MIME type error 예:

```text
Failed to load module script:
Expected a JavaScript module script but the server responded with a MIME type of "text/html"
```

Troubleshooting Flow:

```text
Network에서 JS/CSS 요청 확인
→ Response Content-Type 확인
→ Response Body가 index.html인지 확인
→ asset 파일 실제 존재 확인
→ base path 확인
→ cache 확인
```

Nginx 정적 asset 우선 제공:

```nginx
location / {
  try_files $uri $uri/ /index.html;
}
```

`try_files $uri`가 먼저 있어야 실제 asset을 우선 제공한다.

---

### [FAQ]

Q. JS 파일 요청에 index.html이 반환되면 어떤 문제가 생기는가?
A. 브라우저가 JS 대신 HTML을 받아 MIME type error 또는 흰 화면이 발생한다.

Q. Asset 요청이 fallback되는 이유는?
A. asset 파일이 없거나 경로가 틀렸는데 서버가 index.html로 fallback하기 때문이다.

Q. MIME type error는 무엇을 확인해야 하는가?
A. Network 응답의 Content-Type과 Response Body가 index.html인지 확인해야 한다.

Q. Asset Fallback을 막으려면 어떻게 해야 하는가?
A. 실제 asset 파일을 먼저 제공하고 없을 때만 프론트엔드 route에 fallback해야 한다.

---

# 6. Cache Rules for Static Hosting

## 6.1 Browser Cache Core

### [개념]

Browser Cache는 브라우저가 정적 파일을 저장해 재방문 시 빠르게 로드하도록 하는 기능이다.

---

### [핵심]

정적 파일 캐시 기준:

```text
index.html
→ 짧은 cache 또는 no-cache 권장

assets/*.hash.js
→ long cache 가능

assets/*.hash.css
→ long cache 가능

image/font hash file
→ long cache 가능

config.json
→ no-store 또는 짧은 cache 권장
```

위험:

- `index.html` 장기 캐시
- 이전 JS bundle 참조
- CDN invalidation 누락
- Service Worker 이전 파일 유지
- Runtime Config cache
- chunk load error

---

### [실무]

Nginx Cache 예:

```nginx
location = /index.html {
  add_header Cache-Control "no-cache";
}

location /assets/ {
  add_header Cache-Control "public, max-age=31536000, immutable";
}
```

검증 Flow:

```text
Network 탭 확인
→ Response Headers 확인
→ Cache-Control 확인
→ Disable Cache 테스트
→ Hard Reload 테스트
→ CDN cache 확인
```

---

### [FAQ]

Q. index.html은 왜 장기 캐시하면 안 되는가?
A. 이전 index.html이 이전 hash asset을 참조해 새 배포와 mismatch가 발생할 수 있기 때문이다.

Q. hash가 붙은 JS 파일은 장기 캐시해도 되는가?
A. 가능하다. 내용이 바뀌면 파일명이 바뀌기 때문이다.

Q. 배포했는데 이전 화면이 보이는 이유는?
A. 브라우저 캐시, CDN 캐시, Service Worker 캐시 문제일 수 있다.

Q. config.json은 왜 짧게 캐시해야 하는가?
A. Runtime Config 값 변경이 즉시 반영되어야 할 수 있기 때문이다.

---

## 6.2 CDN Cache

### [개념]

CDN Cache는 CloudFront 같은 CDN이 정적 파일을 사용자 가까운 위치에 저장해 빠르게 제공하는 방식이다.

---

### [핵심]

CDN Cache 장점:

- 정적 파일 로딩 속도 향상
- 원본 서버 부하 감소
- 글로벌 사용자 대응
- HTTPS / Custom Domain 연동 가능

주의:

- 새 배포 후 이전 파일이 제공될 수 있음
- `index.html` 캐시 정책 중요
- invalidation 필요 가능
- Runtime Config cache 주의
- Service Worker와 결합 시 문제 복잡도 증가

---

### [실무]

S3 + CloudFront 배포 Flow:

```text
npm run build
→ S3 upload
→ CloudFront serves files
→ index.html cache 확인
→ 필요한 경우 invalidation
```

Invalidation 대상 예:

```text
/index.html
/config.json
/*
```

권장 전략:

```text
index.html
→ 짧은 cache + 필요 시 invalidation

hashed assets
→ long cache

config.json
→ no-store 또는 짧은 cache
```

---

### [FAQ]

Q. CDN을 쓰면 왜 배포 반영이 늦을 수 있는가?
A. CDN edge cache가 이전 파일을 계속 제공할 수 있기 때문이다.

Q. CloudFront invalidation은 언제 필요한가?
A. 새 배포 후 이전 index.html이나 config.json이 계속 제공될 때 필요하다.

Q. 모든 파일을 매번 invalidation해야 하는가?
A. hash asset 전략을 사용하면 보통 index.html과 config 파일 중심으로 처리한다.

Q. CDN Cache 문제는 어디서 확인하는가?
A. Response Headers, Age header, CloudFront cache status, Network 탭에서 확인한다.

---

# 7. Static Hosting Troubleshooting

## 7.1 White Screen After Deploy

### [개념]

White Screen After Deploy는 정적 배포 후 화면이 흰색으로만 표시되는 문제다.

---

### [핵심]

대표 원인:

- JS bundle 404
- CSS asset 404
- JavaScript runtime error
- 잘못된 asset base path
- 환경 변수 undefined
- Router basename 오류
- API 초기화 실패
- MIME type error
- 이전 index.html cache
- Service Worker cache

---

### [실무]

Troubleshooting Flow:

```text
Console Error 확인
→ Network JS/CSS status 확인
→ Response Content-Type 확인
→ index.html script path 확인
→ asset 실제 존재 확인
→ base/homepage 확인
→ env 확인
→ cache 확인
```

우선순위:

```text
1. Console runtime error
2. JS bundle 404
3. CSS 404
4. MIME type error
5. env undefined
6. Router basename
7. cache mismatch
```

---

### [FAQ]

Q. 배포 후 흰 화면이 나오면 무엇을 먼저 확인해야 하는가?
A. Console Error와 Network 탭의 JS/CSS 로드 상태를 먼저 확인해야 한다.

Q. JS bundle이 404면 무엇을 확인해야 하는가?
A. Build output, hosting root, asset path, base path를 확인해야 한다.

Q. Console에 Unexpected token '<'가 나오면 무엇을 의심해야 하는가?
A. JS나 API 요청이 HTML index.html을 응답받고 있을 가능성이 높다.

Q. 로컬 dev server에서는 되는데 정적 배포에서 흰 화면이 나는 이유는?
A. dev server와 static hosting의 base path, fallback, env, cache 조건이 다르기 때문이다.

---

## 7.2 Static Asset 404

### [개념]

Static Asset 404는 JS, CSS, 이미지, 폰트 파일을 정적 서버가 찾지 못하는 문제다.

---

### [핵심]

원인:

- 파일 복사 누락
- Output Directory mismatch
- Hosting Root 오류
- Vite `base` 오류
- CRA `homepage` 오류
- Sub Path Hosting 설정 누락
- 대소문자 불일치
- public path 오류
- CDN cache mismatch

---

### [실무]

Troubleshooting Flow:

```text
Network 404 file 확인
→ index.html 참조 경로 확인
→ Build Output에 파일 존재 확인
→ Hosting Root에 파일 존재 확인
→ base/homepage 확인
→ 배포 경로 확인
→ Linux 대소문자 확인
→ redeploy
```

대소문자 예:

```text
import Logo from "./Logo.png";
actual file: logo.png

Windows local
→ 동작 가능

Linux server
→ 실패 가능
```

---

### [FAQ]

Q. Static Asset 404란 무엇인가?
A. JS, CSS, 이미지, 폰트 파일을 서버가 찾지 못해 404를 반환하는 문제다.

Q. 이미지가 배포 후 깨지는 이유는?
A. 파일 경로, 대소문자, public path, build output 복사 누락이 원인일 수 있다.

Q. Windows에서는 되는데 Linux 배포에서 이미지가 깨지는 이유는?
A. Linux는 파일명 대소문자를 구분하기 때문이다.

Q. Asset 404는 어디서 확인하는가?
A. Browser DevTools Network 탭에서 404 요청 파일을 확인한다.

---

## 7.3 Wrong Content-Type

### [개념]

Wrong Content-Type은 정적 파일 요청에 대해 서버가 잘못된 MIME type을 반환하는 문제다.

---

### [핵심]

대표 증상:

```text
JS file response Content-Type: text/html
CSS file response Content-Type: text/html
module script MIME type error
font MIME type error
image display error
```

대표 원인:

- JS/CSS 요청이 index.html로 fallback
- Nginx MIME 설정 누락
- 잘못된 server config
- 파일 확장자 오류
- asset 경로 오류

---

### [실무]

Troubleshooting Flow:

```text
Network 요청 선택
→ Response Headers Content-Type 확인
→ Response Body 확인
→ 실제 파일 존재 확인
→ fallback 설정 확인
→ server mime.types 설정 확인
```

Nginx mime include 예:

```nginx
http {
  include /etc/nginx/mime.types;
}
```

판단 기준:

```text
JS 요청에 text/html
→ index.html fallback 가능성 높음

CSS 요청에 text/html
→ asset path/fallback 문제 가능성 높음
```

---

### [FAQ]

Q. MIME type error는 왜 발생하는가?
A. JS나 CSS 파일 요청에 HTML이 반환되거나 서버가 잘못된 Content-Type을 보내기 때문이다.

Q. JS 요청의 Content-Type이 text/html이면 무엇을 의미하는가?
A. JS 파일 대신 index.html이 반환되었을 가능성이 높다.

Q. Nginx에서 MIME type 문제는 무엇을 확인하는가?
A. `mime.types` include 여부와 fallback 설정을 확인해야 한다.

Q. Wrong Content-Type은 프론트엔드 코드 문제인가?
A. 대부분 서버 정적 파일 제공 경로 또는 fallback 설정 문제다.

---

# 8. Agent Decision Rules

## 8.1 PM Agent Rules

### [개념]

PM Agent는 Static File Hosting 방식, Build Output, Hosting Root, SPA fallback, cache 전략을 정리해야 한다.

---

### [핵심]

PM Agent 확인 항목:

- Build Tool
- Output Directory
- Hosting Method
- Hosting Root
- SPA fallback 필요 여부
- API Proxy 필요 여부
- Sub Path Hosting 여부
- Cache 정책
- HTTPS 필요 여부
- 배포 후 검증 범위

---

### [실무]

PM Agent 산출물 예:

```text
Build Tool: Vite
Build Command: npm run build
Output Directory: dist
Hosting Method: Nginx Static Hosting
Hosting Root: /usr/share/nginx/html
SPA Fallback: required
API Proxy: /api → backend:8080
Cache: index.html no-cache, assets long-cache
Verification: Console / Network / Refresh Route / API URL
```

PM Agent 판단 Flow:

```text
배포 목적 확인
→ Hosting 방식 선택
→ Build Output 지정
→ Hosting Root 지정
→ fallback/proxy/cache 요구사항 정의
→ 검증 체크리스트 작성
```

---

### [FAQ]

Q. PM Agent는 Static Hosting에서 무엇을 정해야 하는가?
A. Hosting 방식, output directory, hosting root, SPA fallback, API proxy, cache 정책을 정해야 한다.

Q. PM Agent가 SPA fallback 여부를 판단해야 하는 이유는?
A. React Router 새로고침 404를 예방하기 위해 필요하다.

Q. PM Agent가 cache 전략도 정해야 하는가?
A. 그렇다. 배포 반영 문제와 성능에 직접 영향을 준다.

---

## 8.2 Frontend Agent Rules

### [개념]

Frontend Agent는 Build Output이 Static Hosting에 적합하도록 base path, asset path, router 설정을 고려해 구현해야 한다.

---

### [핵심]

Frontend Agent 필수 기준:

- Build Tool별 output directory 이해
- Vite `base` 필요 여부 확인
- CRA `homepage` 필요 여부 확인
- React Router `basename` 필요 여부 확인
- public asset path 관리
- 파일명 대소문자 일치
- lazy loading chunk 경로 검토
- env 값 undefined 방지
- build preview 확인

---

### [실무]

Frontend Agent 구현 기준:

```text
npm run build 성공
→ output directory 확인
→ local static preview
→ asset path 확인
→ route 이동 확인
→ 직접 URL 접근은 hosting fallback과 연결 검토
```

금지:

```text
절대 경로를 배포 경로와 무관하게 하드코딩
파일명 대소문자 불일치
public asset 경로 임의 사용
하위 경로 배포에서 basename 누락
```

---

### [FAQ]

Q. Frontend Agent는 Static Hosting을 위해 무엇을 고려해야 하는가?
A. output directory, base path, asset path, router basename, 파일명 대소문자, build preview를 고려해야 한다.

Q. public 폴더 asset은 어떻게 참조해야 하는가?
A. 배포 base path와 호스팅 구조를 고려해 참조해야 한다.

Q. 하위 경로 배포에서 Frontend Agent가 확인할 것은?
A. Vite base 또는 CRA homepage와 React Router basename을 확인해야 한다.

---

## 8.3 Review Agent Rules

### [개념]

Review Agent는 Static Hosting 배포 전후로 정적 파일 구조, asset path, fallback, cache, API 충돌을 검토해야 한다.

---

### [핵심]

Review Agent Checklist:

```md
- [ ] Build Output Directory가 맞는가?
- [ ] index.html이 hosting root에 있는가?
- [ ] JS / CSS asset이 존재하는가?
- [ ] asset path가 실제 파일 위치와 맞는가?
- [ ] Vite base 또는 CRA homepage가 배포 경로와 맞는가?
- [ ] Sub Path Hosting이면 Router basename이 맞는가?
- [ ] SPA fallback이 설정되어 있는가?
- [ ] API path가 fallback에 잡히지 않는가?
- [ ] Static asset이 fallback에 잡히지 않는가?
- [ ] index.html cache 정책이 적절한가?
- [ ] hashed asset cache 정책이 적절한가?
- [ ] Network asset 404가 없는가?
- [ ] Console MIME type error가 없는가?
```

---

### [실무]

Review Agent 판단 Flow:

```text
Build 실행
→ Output Directory 확인
→ Hosting Root 확인
→ Static Preview 확인
→ Console Error 확인
→ Network Asset 404 확인
→ Direct Route Refresh 확인
→ API Request 확인
→ Cache Header 확인
```

Critical Issue:

```text
index.html 없음
JS bundle 404
JS 요청에 index.html 반환
API 요청에 index.html 반환
Production White Screen
Sub Path base mismatch
```

승인 기준:

```text
index.html 정상
JS/CSS asset 정상
SPA fallback 정상
API/fallback 충돌 없음
Console Critical Error 없음
Network 404 없음
Cache 정책 적정
```

---

### [FAQ]

Q. Review Agent는 Static Hosting에서 무엇을 가장 먼저 확인해야 하는가?
A. `index.html` 위치와 JS/CSS asset 로드 상태를 먼저 확인해야 한다.

Q. JS 요청에 index.html이 반환되면 승인 가능한가?
A. 아니다. MIME type error와 흰 화면을 유발하는 치명적 문제다.

Q. API 요청에 index.html이 반환되면 승인 가능한가?
A. 아니다. API proxy 또는 fallback 설정이 잘못된 것이다.

Q. Network 404가 하나라도 있으면 무조건 실패인가?
A. 핵심 JS/CSS/API 404는 실패로 봐야 하며 이미지 등도 사용자 경험에 따라 수정 대상이다.

---

# 9. Common Mistakes

## 9.1 Static Hosting Common Mistakes

### [개념]

Static Hosting Common Mistakes는 Build 결과물 배포 후 화면 표시, asset 로드, 라우팅, 캐시 문제를 만드는 반복 실수다.

---

### [핵심]

자주 발생하는 실수:

- Source Code를 그대로 배포
- `npm run build` 없이 배포
- Vite `dist` 대신 `build` 배포
- CRA `build` 대신 `dist` 배포
- output 폴더 자체를 잘못된 depth로 복사
- hosting root에 `index.html`이 없음
- JS / CSS asset 복사 누락
- Vite `base` 설정 누락
- CRA `homepage` 설정 오류
- 하위 경로 배포에서 Router `basename` 누락
- SPA fallback 누락
- SPA fallback이 API 요청까지 처리
- asset 요청이 index.html로 fallback
- `index.html` 장기 캐시
- CDN invalidation 누락
- Service Worker cache 방치
- Linux 배포에서 파일명 대소문자 오류
- public asset 경로 오류
- Content-Type 오류

---

### [실무]

실수별 판단:

```text
흰 화면
→ JS 404 / runtime error / MIME type / env 확인

CSS 미적용
→ CSS asset 404 / base path / hosting root 확인

새로고침 404
→ SPA fallback 확인

API가 HTML 반환
→ fallback과 proxy 충돌 확인

배포 반영 안 됨
→ browser cache / CDN cache / index.html cache 확인
```

---

### [FAQ]

Q. Static Hosting에서 가장 흔한 실수는 무엇인가?
A. Build Output이 아니라 Source Code를 올리거나 output directory를 잘못 지정하는 것이다.

Q. 흰 화면의 가장 흔한 원인은 무엇인가?
A. JS bundle 404, runtime error, MIME type error, asset base path 오류가 대표적이다.

Q. 새로고침 404는 Static Hosting 문제인가?
A. 대부분 서버의 SPA fallback 설정 문제다.

Q. 배포 후 이전 화면이 계속 보이는 이유는?
A. 브라우저 캐시, CDN 캐시, Service Worker 캐시 또는 index.html 장기 캐시 때문이다.

---

# 10. Part05 Quality Checklist

## 10.1 Document Quality

### [개념]

이 문서는 Frontend Build & Deploy Domain의 Part05이며 Static File Hosting Rules Retrieval에 최적화되어야 한다.

---

### [핵심]

문서 품질 기준:

- Static File Hosting 정의 포함
- Static File Request Flow 포함
- Vite Dist Hosting 포함
- CRA Build Hosting 포함
- Output Directory Mismatch 포함
- Hosting Root 포함
- Asset Path 포함
- Sub Path Hosting 포함
- Nginx Static Hosting 포함
- Spring Boot Static Resource Hosting 포함
- Platform Static Hosting 포함
- SPA Fallback 개념 포함
- Cache Rules 포함
- Troubleshooting Flow 포함
- Agent별 판단 기준 포함
- Common Mistakes 포함
- Retrieval Queries 포함

---

### [실무]

Part05는 다음 문서와 연결된다.

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

Q. Part05의 핵심 목적은 무엇인가?
A. Build Output을 정적 파일로 제공할 때 hosting root, asset path, SPA fallback, cache 문제를 Agent가 정확히 판단하게 하는 것이다.

Q. Part05에서 SPA Routing 전체를 다루는가?
A. 아니다. Static Hosting 관점의 fallback만 다루고 상세 SPA Routing은 Part06에서 분리한다.

Q. Part05에서 Nginx 전체 설정을 다루는가?
A. 아니다. Static Hosting과 관련된 핵심만 다루고 Nginx 상세 배포는 후속 Part에서 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. Static File Hosting이란 무엇인가?
A. Build 결과물인 HTML, CSS, JavaScript, 이미지 파일을 웹 서버나 플랫폼이 브라우저에 제공하는 방식이다.

Q. React Build 결과물은 서버 프로그램인가?
A. 아니다. 일반 React SPA Build 결과물은 정적 파일이며 별도 정적 파일 서버가 제공해야 한다.

Q. React Source Code를 그대로 배포해도 되는가?
A. 아니다. 보통 `npm run build` 결과물인 `dist` 또는 `build` 내부 파일을 배포해야 한다.

Q. Static Hosting에서 가장 먼저 확인할 파일은 무엇인가?
A. `index.html`이 hosting root에서 정상 제공되는지 확인해야 한다.

Q. Vite Build 결과물은 어디에 생성되는가?
A. 기본적으로 `dist` 폴더에 생성된다.

Q. CRA Build 결과물은 어디에 생성되는가?
A. 기본적으로 `build` 폴더에 생성된다.

Q. Vite 배포 시 어떤 폴더를 hosting해야 하는가?
A. 일반적으로 `dist` 내부 파일을 hosting root에서 제공해야 한다.

Q. CRA 배포 시 어떤 폴더를 hosting해야 하는가?
A. 일반적으로 `build` 내부 파일을 hosting root에서 제공해야 한다.

Q. Output Directory Mismatch란 무엇인가?
A. 빌드 결과 폴더와 배포 설정에서 기대하는 폴더가 달라 파일을 찾지 못하는 문제다.

Q. Vite 프로젝트인데 build 폴더가 없으면 문제인가?
A. 아니다. Vite 기본 output은 `dist`다.

Q. CRA 프로젝트인데 dist 폴더가 없으면 문제인가?
A. 아니다. CRA 기본 output은 `build`다.

Q. Hosting Root란 무엇인가?
A. 웹 서버가 정적 파일을 찾는 기준 디렉토리다.

Q. index.html은 어디에 있어야 하는가?
A. 일반적으로 hosting root 바로 아래에 있어야 한다.

Q. JS bundle이 404면 무엇을 확인해야 하는가?
A. Build output, hosting root, asset path, base path, 파일 복사 누락을 확인해야 한다.

Q. CSS가 배포 후 적용되지 않는 이유는?
A. CSS asset 경로가 틀렸거나 파일이 hosting root에 없을 수 있다.

Q. 이미지가 배포 후 깨지는 이유는?
A. public path, import path, 파일명 대소문자, asset 복사 누락을 확인해야 한다.

Q. Asset Path란 무엇인가?
A. 브라우저가 JS, CSS, 이미지, 폰트 파일을 불러오는 경로다.

Q. Vite base 설정은 언제 필요한가?
A. 하위 경로 배포 또는 asset 경로 기준을 바꿔야 할 때 필요하다.

Q. CRA homepage 설정은 언제 필요한가?
A. 하위 경로 배포나 GitHub Pages 배포처럼 asset 기준 경로가 필요할 때 사용한다.

Q. Sub Path Hosting이란 무엇인가?
A. 앱을 `/`가 아니라 `/my-app` 같은 하위 경로에서 제공하는 방식이다.

Q. 하위 경로 배포 시 무엇을 함께 맞춰야 하는가?
A. Build Tool base path, Router basename, 서버 location을 함께 맞춰야 한다.

Q. Nginx Static Hosting이란 무엇인가?
A. Nginx가 React Build 결과물을 정적 파일로 제공하는 방식이다.

Q. Nginx에서 React 새로고침 404는 어떻게 해결하는가?
A. `try_files $uri $uri/ /index.html;` 설정을 사용한다.

Q. Spring Boot Static Resource Hosting이란 무엇인가?
A. React Build 결과물을 Spring Boot `src/main/resources/static`에 포함해 같은 서버에서 제공하는 방식이다.

Q. Spring Boot static 경로는 어디인가?
A. 일반적으로 `src/main/resources/static`이다.

Q. Spring Boot static에 build 폴더 자체를 넣어도 되는가?
A. 대부분 권장하지 않는다. build 또는 dist 내부 파일이 static root에 있어야 한다.

Q. Platform Static Hosting에는 무엇이 있는가?
A. Vercel, Netlify, S3, CloudFront, GitHub Pages, Cloudflare Pages 등이 있다.

Q. 플랫폼 배포에서 가장 중요한 설정은 무엇인가?
A. Build Command, Output Directory, Environment Variables, SPA fallback이다.

Q. SPA Fallback이란 무엇인가?
A. 프론트엔드 route 요청에 대해 서버가 `index.html`을 반환해 React Router가 렌더링하게 하는 설정이다.

Q. React에서 새로고침하면 404가 나는 이유는?
A. 서버가 `/login` 같은 route를 실제 파일 경로로 찾기 때문이다.

Q. SPA fallback을 모든 요청에 적용해도 되는가?
A. 아니다. API 요청과 정적 asset 요청은 fallback 대상에서 제외해야 한다.

Q. API 요청에 index.html이 오면 무엇을 의심해야 하는가?
A. SPA fallback이 API 경로까지 잡고 있을 가능성이 높다.

Q. Asset Fallback Risk란 무엇인가?
A. JS, CSS, 이미지 요청이 실제 파일이 아니라 `index.html`로 fallback되어 발생하는 문제다.

Q. MIME type error는 왜 발생하는가?
A. JS나 CSS 파일 요청에 HTML이 반환되거나 서버가 잘못된 Content-Type을 보내기 때문이다.

Q. JS 요청의 Content-Type이 text/html이면 무엇을 의미하는가?
A. JS 파일 대신 index.html이 반환되었을 가능성이 높다.

Q. index.html은 왜 장기 캐시하면 안 되는가?
A. 이전 index.html이 이전 hash asset을 참조해 새 배포와 mismatch가 발생할 수 있기 때문이다.

Q. hash가 붙은 JS 파일은 장기 캐시해도 되는가?
A. 가능하다. 내용이 바뀌면 파일명이 바뀌기 때문이다.

Q. 배포했는데 이전 화면이 보이는 이유는?
A. 브라우저 캐시, CDN 캐시, Service Worker 캐시 문제일 수 있다.

Q. CDN invalidation은 언제 필요한가?
A. 새 배포 후 이전 index.html이나 config.json이 계속 제공될 때 필요하다.

Q. White Screen After Deploy는 무엇을 먼저 확인해야 하는가?
A. Console Error와 Network 탭의 JS/CSS 로드 상태를 먼저 확인해야 한다.

Q. Static Asset 404는 어디서 확인하는가?
A. Browser DevTools Network 탭에서 404 요청 파일을 확인한다.

Q. Windows에서는 되는데 Linux 배포에서 이미지가 깨지는 이유는?
A. Linux는 파일명 대소문자를 구분하기 때문이다.

Q. Wrong Content-Type은 무엇을 확인해야 하는가?
A. Network 응답의 Content-Type과 Response Body가 index.html인지 확인해야 한다.

Q. PM Agent는 Static Hosting에서 무엇을 정해야 하는가?
A. Hosting 방식, output directory, hosting root, SPA fallback, API proxy, cache 정책을 정해야 한다.

Q. Frontend Agent는 Static Hosting을 위해 무엇을 고려해야 하는가?
A. output directory, base path, asset path, router basename, 파일명 대소문자, build preview를 고려해야 한다.

Q. Review Agent는 Static Hosting에서 무엇을 먼저 확인해야 하는가?
A. `index.html` 위치와 JS/CSS asset 로드 상태를 먼저 확인해야 한다.

Q. Static Hosting에서 가장 흔한 실수는 무엇인가?
A. Build Output이 아니라 Source Code를 올리거나 output directory를 잘못 지정하는 것이다.

Q. Part05 다음 문서는 무엇인가?
A. Part06 SPA Routing Rules로 이어지는 것이 적합하다.
