# Frontend Build & Deploy Part10 - Platform Deployment Rules

---

# 1. Platform Deployment Core

## 1.1 Platform Deployment Definition

### [개념]

Platform Deployment는 Vercel, Netlify, Cloudflare Pages, AWS S3, CloudFront, GitHub Pages 같은 배포 플랫폼을 사용해 React Build 결과물을 정적 파일로 제공하는 배포 방식이다.

대표 플랫폼:

```text
Vercel
Netlify
Cloudflare Pages
AWS S3
AWS CloudFront
GitHub Pages
Firebase Hosting
AWS Amplify
Render Static Site
```

---

### [핵심]

Platform Deployment 핵심 규칙:

- Source Code가 아니라 Build Output이 배포 대상이다.
- 플랫폼마다 Build Command와 Output Directory 설정이 필요하다.
- Vite 기본 Output Directory는 `dist`다.
- CRA 기본 Output Directory는 `build`다.
- 환경 변수는 플랫폼 Dashboard 또는 CI/CD에서 설정한다.
- React SPA BrowserRouter 사용 시 fallback / rewrite 설정이 필요하다.
- API Base URL이 운영 환경에 맞아야 한다.
- 운영 Build에 `localhost`가 남으면 안 된다.
- HTTPS와 Mixed Content를 확인해야 한다.
- Cache와 CDN 반영 지연을 고려해야 한다.
- 배포 후 직접 URL 접근, 새로고침, API 요청을 검증해야 한다.

---

### [실무]

2026 실무 기준으로 React SPA의 빠른 배포는 Vercel / Netlify / Cloudflare Pages가 단순하고, 정적 파일 + CDN 제어가 필요하면 S3 + CloudFront를 고려한다.

기본 Flow:

```text
Git Push
→ Platform detects project
→ Install dependencies
→ Run Build Command
→ Collect Output Directory
→ Deploy Static Files
→ Serve via CDN / Edge
→ Browser loads React App
```

Agent 판단 Flow:

```text
Platform 확인
→ Build Tool 확인
→ Build Command 확인
→ Output Directory 확인
→ Env 설정 확인
→ SPA fallback 확인
→ API Base URL 확인
→ HTTPS / Cache 확인
→ 배포 후 Network 검증
```

---

### [FAQ]

Q. Platform Deployment란 무엇인가?
A. Vercel, Netlify, S3, CloudFront 같은 플랫폼을 사용해 React Build 결과물을 배포하는 방식이다.

Q. 플랫폼 배포에서도 Build가 필요한가?
A. 필요하다. 플랫폼은 보통 `npm run build`를 실행하고 결과 폴더를 배포한다.

Q. 플랫폼 배포에서 가장 중요한 설정은 무엇인가?
A. Build Command, Output Directory, Environment Variables, SPA fallback 설정이다.

Q. 플랫폼 배포 후 가장 먼저 확인할 것은 무엇인가?
A. 메인 접속, JS/CSS 로드, 새로고침, 직접 URL 접근, API 요청 URL을 확인해야 한다.

---

## 1.2 Platform Selection Criteria

### [개념]

Platform Selection Criteria는 프로젝트 목적, 운영 요구사항, 비용, 난이도에 따라 적절한 정적 배포 플랫폼을 선택하는 기준이다.

---

### [핵심]

Vercel / Netlify가 적합한 경우:

```text
빠른 배포
Git 연동 자동 배포
Preview Deploy 필요
프론트엔드 단독 배포
서버 관리 최소화
개인 프로젝트 / 포트폴리오
```

S3 + CloudFront가 적합한 경우:

```text
AWS 기반 운영
CDN cache 정책 세밀 제어
Custom Domain / TLS 제어
대규모 정적 파일 배포
운영 인프라를 직접 관리
```

GitHub Pages가 적합한 경우:

```text
간단한 정적 페이지
문서 / 데모 사이트
무료 GitHub 기반 배포
API 없는 프론트엔드 샘플
```

Spring Boot 통합 배포가 더 적합한 경우:

```text
학원 발표용 단일 서버
백엔드와 프론트엔드 함께 배포
CORS 최소화
서버 하나로 빠른 시연
```

---

### [실무]

선택 Flow:

```text
프론트만 빠르게 배포
→ Vercel / Netlify / Cloudflare Pages

AWS 운영 경험 필요
→ S3 + CloudFront

문서 / 간단 데모
→ GitHub Pages

FE/BE 단일 JAR 발표
→ Spring Boot 통합 배포

FE/BE/DB 컨테이너 운영
→ Docker + Nginx
```

PM Agent 판단 기준:

```text
배포 목적
→ 데모 / 포트폴리오 / 운영

백엔드 위치
→ 같은 서버 / 별도 API / 서버리스

라우팅 방식
→ BrowserRouter fallback 가능 여부

환경 변수
→ 플랫폼 env 설정 가능 여부

운영 난이도
→ 서버 관리 가능 여부
```

---

### [FAQ]

Q. React 포트폴리오 배포는 어떤 플랫폼이 쉬운가?
A. Vercel, Netlify, Cloudflare Pages가 비교적 쉽다.

Q. AWS 기반 운영이면 어떤 방식을 고려하는가?
A. S3 + CloudFront를 고려할 수 있다.

Q. GitHub Pages는 언제 적합한가?
A. 간단한 정적 페이지나 문서, 데모 사이트에 적합하다.

Q. 학원 프로젝트 발표용으로 플랫폼 배포가 항상 좋은가?
A. 아니다. 백엔드와 함께 시연한다면 Spring Boot 통합 배포가 더 단순할 수 있다.

---

# 2. Common Platform Settings

## 2.1 Build Command Rules

### [개념]

Build Command는 플랫폼이 배포 전에 실행하는 프론트엔드 Build 명령이다.

대표 명령:

```bash
npm run build
yarn build
pnpm build
```

---

### [핵심]

Build Command 확인 항목:

- package manager
- lock file
- `package.json` scripts
- frontend 하위 폴더 여부
- Node.js version
- env 변수
- build mode
- CI/CD와 플랫폼 설정 일치 여부

Vite 예:

```json
{
  "scripts": {
    "build": "vite build"
  }
}
```

CRA 예:

```json
{
  "scripts": {
    "build": "react-scripts build"
  }
}
```

---

### [실무]

플랫폼 설정 예:

```text
Vite
Build Command: npm run build
Output Directory: dist

CRA
Build Command: npm run build
Output Directory: build
```

Monorepo 예:

```text
Root Directory: frontend
Build Command: npm run build
Output Directory: dist or build
```

Agent 검토 Flow:

```text
package.json 확인
→ scripts.build 확인
→ package manager 확인
→ platform build command 확인
→ root directory 확인
→ build log 확인
```

---

### [FAQ]

Q. 플랫폼 배포에서 Build Command는 무엇인가?
A. 배포 전에 프론트엔드 정적 파일을 생성하기 위해 실행하는 명령이다.

Q. Vite와 CRA의 Build Command는 같은가?
A. 보통 둘 다 `npm run build`지만 내부 실행 도구와 Output Directory가 다르다.

Q. frontend가 하위 폴더에 있으면 무엇을 설정해야 하는가?
A. Root Directory 또는 working directory를 `frontend`로 설정해야 한다.

Q. Build Command가 실패하면 무엇을 확인하는가?
A. build log, Node version, env, package manager, lock file, TypeScript / ESLint error를 확인한다.

---

## 2.2 Output Directory Rules

### [개념]

Output Directory는 플랫폼이 배포할 정적 파일 결과 폴더다.

---

### [핵심]

기본 Output Directory:

```text
Vite
→ dist

CRA
→ build
```

중요 규칙:

- 실제 생성된 폴더와 플랫폼 설정이 일치해야 한다.
- Output Directory 안에 `index.html`이 있어야 한다.
- Output Directory는 source directory가 아니다.
- Monorepo에서는 root directory 기준 상대 경로를 확인해야 한다.
- 잘못 설정하면 배포가 성공해도 빈 화면 또는 404가 발생할 수 있다.

---

### [실무]

플랫폼 설정:

```text
Vite:
Build Command = npm run build
Output Directory = dist

CRA:
Build Command = npm run build
Output Directory = build
```

잘못된 예:

```text
Vite Project
Output Directory = build

CRA Project
Output Directory = dist
```

검증 Flow:

```text
로컬 npm run build 실행
→ 생성 폴더 확인
→ index.html 확인
→ 플랫폼 output directory와 비교
→ deploy log 확인
```

---

### [FAQ]

Q. Output Directory란 무엇인가?
A. Build 후 생성되어 플랫폼이 실제로 배포하는 정적 파일 폴더다.

Q. Vite Output Directory는 무엇인가?
A. 기본적으로 `dist`다.

Q. CRA Output Directory는 무엇인가?
A. 기본적으로 `build`다.

Q. Output Directory를 잘못 설정하면 어떤 문제가 생기는가?
A. index.html을 찾지 못하거나 JS/CSS asset 404가 발생할 수 있다.

---

## 2.3 Root Directory Rules

### [개념]

Root Directory는 플랫폼이 프로젝트의 기준 폴더로 사용하는 경로다.

Monorepo 또는 frontend/backend 분리 구조에서 중요하다.

예:

```text
project-root/
├ frontend/
│  ├ package.json
│  └ src/
├ backend/
└ README.md
```

이 경우 Root Directory는 보통 다음과 같다.

```text
frontend
```

---

### [핵심]

Root Directory 확인 기준:

- `package.json`이 있는 위치
- frontend source가 있는 위치
- lock file이 있는 위치
- build command를 실행할 위치
- output directory 기준 위치
- env 파일 위치
- platform dashboard 설정

---

### [실무]

플랫폼 설정 예:

```text
Root Directory: frontend
Build Command: npm run build
Output Directory: dist
```

또는 CRA:

```text
Root Directory: frontend
Build Command: npm run build
Output Directory: build
```

문제 예:

```text
Root Directory: project-root
Build Command: npm run build
→ root에 package.json 없음
→ build 실패
```

Agent 검토 Flow:

```text
프로젝트 구조 확인
→ frontend package.json 위치 확인
→ platform root directory 확인
→ build command 기준 위치 확인
→ output directory 기준 위치 확인
```

---

### [FAQ]

Q. Root Directory란 무엇인가?
A. 플랫폼이 build command를 실행하고 프로젝트를 인식하는 기준 폴더다.

Q. frontend 폴더 안에 package.json이 있으면 Root Directory는 무엇인가?
A. 보통 `frontend`로 설정해야 한다.

Q. Root Directory가 틀리면 어떤 문제가 생기는가?
A. package.json을 못 찾거나 build command가 실패할 수 있다.

Q. Output Directory는 Root Directory 기준인가?
A. 플랫폼마다 표현은 다르지만 대부분 Root Directory 기준으로 해석되므로 확인이 필요하다.

---

## 2.4 Node Version Rules

### [개념]

Node Version Rules는 플랫폼 Build 환경에서 사용하는 Node.js 버전을 프로젝트와 맞추는 규칙이다.

---

### [핵심]

Node Version 확인 위치:

```text
package.json engines
.nvmrc
.node-version
platform dashboard setting
CI/CD setup-node
```

문제 원인:

- 로컬과 플랫폼 Node version 차이
- dependency가 특정 Node version 요구
- 최신 문법 지원 차이
- npm version 차이
- lock file과 install 결과 차이

---

### [실무]

package.json 예:

```json
{
  "engines": {
    "node": ">=20"
  }
}
```

`.nvmrc` 예:

```text
20
```

Agent 검토 Flow:

```text
로컬 Node version 확인
→ package.json engines 확인
→ .nvmrc 확인
→ platform build log Node version 확인
→ 필요 시 platform setting 수정
```

---

### [FAQ]

Q. 플랫폼 배포에서 Node version이 중요한 이유는?
A. 로컬에서는 성공한 build가 플랫폼 Node version 차이로 실패할 수 있기 때문이다.

Q. Node version은 어디에 명시하는가?
A. `package.json engines`, `.nvmrc`, 플랫폼 설정에서 명시할 수 있다.

Q. Build log에서 Node version을 확인해야 하는가?
A. 해야 한다. 플랫폼이 실제로 어떤 Node version을 쓰는지 확인해야 한다.

Q. Node version mismatch 증상은 무엇인가?
A. dependency install 실패, syntax error, build tool 실행 실패가 발생할 수 있다.

---

# 3. Platform Environment Variables

## 3.1 Platform Env Core

### [개념]

Platform Env는 배포 플랫폼 Dashboard 또는 설정 파일에서 Build 시점에 주입하는 환경 변수다.

---

### [핵심]

Platform Env 핵심 규칙:

- React SPA env는 대부분 Build 시점에 주입된다.
- env 변경 후 재배포가 필요할 수 있다.
- Vite는 `VITE_` prefix가 필요하다.
- CRA는 `REACT_APP_` prefix가 필요하다.
- 프론트엔드 env에 Secret을 넣으면 안 된다.
- Production / Preview / Development env를 구분할 수 있다.
- 운영 API URL에 `localhost`가 없어야 한다.

---

### [실무]

Vite platform env 예:

```text
VITE_API_BASE_URL=https://api.example.com
VITE_APP_ENV=production
```

CRA platform env 예:

```text
REACT_APP_API_BASE_URL=https://api.example.com
REACT_APP_APP_ENV=production
```

검증 Flow:

```text
platform env 설정 확인
→ prefix 확인
→ production API URL 확인
→ redeploy
→ Network Request URL 확인
```

Review 기준:

```md
- [ ] Production env가 설정되어 있는가?
- [ ] Preview env와 Production env가 구분되어 있는가?
- [ ] env prefix가 Build Tool과 맞는가?
- [ ] Secret이 포함되지 않았는가?
- [ ] env 변경 후 redeploy 되었는가?
```

---

### [FAQ]

Q. Platform Env란 무엇인가?
A. 배포 플랫폼에서 Build 시점에 주입하는 환경 변수다.

Q. 플랫폼 env를 바꾸면 즉시 반영되는가?
A. Build-time env라면 재배포가 필요할 수 있다.

Q. Vite platform env prefix는 무엇인가?
A. `VITE_`다.

Q. CRA platform env prefix는 무엇인가?
A. `REACT_APP_`다.

---

## 3.2 Production and Preview Env

### [개념]

Production and Preview Env는 실제 운영 배포와 Pull Request / branch preview 배포에서 서로 다른 환경 변수를 사용하는 방식이다.

---

### [핵심]

환경 구분:

```text
Development
→ local dev

Preview
→ PR / branch deploy

Staging
→ QA / pre-production

Production
→ real users
```

중요 규칙:

- Preview가 Production API를 호출하지 않도록 주의한다.
- Production이 dev/staging API를 호출하지 않도록 주의한다.
- 테스트 데이터와 운영 데이터를 분리한다.
- OAuth redirect URI도 환경별로 분리해야 한다.
- Cookie Domain과 CORS Origin도 환경별로 맞춰야 한다.

---

### [실무]

Preview env 예:

```text
VITE_API_BASE_URL=https://dev-api.example.com
VITE_APP_ENV=preview
```

Production env 예:

```text
VITE_API_BASE_URL=https://api.example.com
VITE_APP_ENV=production
```

검증 Flow:

```text
Preview URL 접속
→ Network API URL 확인
→ dev/staging API인지 확인

Production URL 접속
→ Network API URL 확인
→ production API인지 확인
```

---

### [FAQ]

Q. Preview Env는 무엇인가?
A. PR이나 branch preview 배포에서 사용하는 환경 변수다.

Q. Preview 배포가 Production API를 호출해도 되는가?
A. 권장하지 않는다. 테스트 중 운영 데이터가 변경될 수 있다.

Q. Production 배포가 dev API를 호출하면 어떤 문제가 생기는가?
A. 실제 사용자가 테스트 서버 데이터를 보거나 기능이 실패할 수 있다.

Q. 환경별 API URL은 어디서 검증하는가?
A. 브라우저 Network 탭의 실제 Request URL에서 검증한다.

---

## 3.3 Secret Exposure Risk

### [개념]

Secret Exposure Risk는 플랫폼 환경 변수에 저장한 값이 프론트엔드 Build 결과물에 포함되어 브라우저에 노출되는 위험이다.

---

### [핵심]

Frontend env에 금지:

```text
DB_PASSWORD
JWT_SECRET
OPENAI_API_KEY
AWS_SECRET_ACCESS_KEY
TOSS_SECRET_KEY
PRIVATE_KEY
SMTP_PASSWORD
ADMIN_PASSWORD
```

Frontend env에 가능:

```text
API_BASE_URL
APP_ENV
PUBLIC_MAP_KEY
OAUTH_CLIENT_ID
SENTRY_DSN_PUBLIC
ANALYTICS_ID
```

중요 기준:

- 플랫폼 Dashboard에 Secret으로 저장해도 프론트엔드 Build에 주입하면 노출될 수 있다.
- `VITE_`, `REACT_APP_` prefix가 붙은 값은 클라이언트 bundle에 포함될 수 있다.
- Secret은 백엔드 또는 서버리스 함수에서 사용해야 한다.
- 이미 노출된 Secret은 폐기하고 재발급해야 한다.

---

### [실무]

잘못된 예:

```text
VITE_OPENAI_API_KEY=sk-xxxx
REACT_APP_TOSS_SECRET_KEY=test_sk_xxxx
VITE_JWT_SECRET=my-secret
```

올바른 구조:

```text
Frontend
→ /api/ai/recommend 요청

Backend
→ OPENAI_API_KEY 사용
→ 외부 API 호출
→ 결과 반환
```

Review Flow:

```text
platform env 목록 확인
→ prefix 붙은 Secret 확인
→ frontend bundle 노출 가능성 판단
→ backend env로 이동 권장
→ 노출된 key 폐기
```

---

### [FAQ]

Q. 플랫폼 env에 Secret을 넣으면 안전한가?
A. 백엔드용이면 가능하지만 프론트엔드 Build에 주입하면 브라우저에 노출될 수 있다.

Q. VITE_OPENAI_API_KEY를 써도 되는가?
A. 안 된다. OpenAI API Key는 백엔드에서 사용해야 한다.

Q. REACT_APP_TOSS_SECRET_KEY를 써도 되는가?
A. 안 된다. Toss Secret Key는 백엔드에서 사용해야 한다.

Q. Secret을 실수로 배포했다면 어떻게 해야 하는가?
A. 해당 Secret을 폐기하고 새로 발급해야 한다.

---

# 4. Vercel Deployment Rules

## 4.1 Vercel Core Rules

### [개념]

Vercel은 Git 연동 기반으로 프론트엔드 프로젝트를 자동 Build하고 Edge Network로 배포하는 플랫폼이다.

React SPA 배포에서는 Build Command, Output Directory, Environment Variables, Rewrite 설정이 핵심이다.

---

### [핵심]

Vercel 설정 항목:

- Framework Preset
- Root Directory
- Build Command
- Output Directory
- Install Command
- Environment Variables
- Rewrites
- Redirects
- Custom Domain
- Preview Deploy
- Production Deploy

Vite 기준:

```text
Build Command: npm run build
Output Directory: dist
```

CRA 기준:

```text
Build Command: npm run build
Output Directory: build
```

SPA fallback 주의:

- BrowserRouter 사용 시 직접 URL 접근과 새로고침을 검증해야 한다.
- Vercel preset이 SPA fallback을 처리할 수 있지만, 프로젝트 설정에 따라 rewrite가 필요할 수 있다.
- 모든 요청을 `/index.html`로 보내는 rewrite는 단독 SPA에서는 유효할 수 있다.
- `/api` rewrite 또는 Vercel Serverless Function을 사용하는 경우 SPA fallback보다 API 규칙을 먼저 분리해야 한다.
- `/api` 요청이 `/index.html`로 rewrite되면 API 응답이 HTML로 반환되는 문제가 발생한다.

---

### [실무]

Monorepo 설정 예:

```text
Root Directory: frontend
Framework Preset: Vite or Create React App
Build Command: npm run build
Output Directory: dist or build
```

단독 SPA fallback 예:

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

단독 SPA fallback 예시는 API rewrite가 없는 단순 정적 SPA에서만 사용한다.

외부 Backend API를 `/api`로 proxy하는 경우:

```json
{
  "rewrites": [
    {
      "source": "/api/(.*)",
      "destination": "https://api.example.com/api/$1"
    },
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

Vercel Serverless Function을 사용하는 경우:

```text
/api/**
→ Vercel Function

/(.*)
→ SPA fallback
```

검증 Flow:

```text
Vercel deploy log 확인
→ Root Directory 확인
→ Build Command 확인
→ Output Directory 확인
→ Environment Variables 확인
→ Production URL 접속
→ 직접 route 새로고침
→ /api 요청 Content-Type 확인
```

Review 기준:

```md
- [ ] Vite output directory가 `dist`인가?
- [ ] CRA output directory가 `build`인가?
- [ ] Root Directory가 frontend 위치와 맞는가?
- [ ] Production env가 설정되어 있는가?
- [ ] SPA route 직접 접근이 정상인가?
- [ ] `/api` 요청이 `index.html`로 rewrite되지 않는가?
- [ ] API 응답 Content-Type이 JSON인가?
- [ ] 운영 API URL에 localhost가 없는가?
```

---

### [FAQ]

Q. Vercel은 무엇인가?
A. Git 연동으로 프론트엔드 프로젝트를 자동 Build하고 배포하는 플랫폼이다.

Q. Vercel에서 Vite Output Directory는 무엇인가?
A. 기본적으로 `dist`다.

Q. Vercel에서 CRA Output Directory는 무엇인가?
A. 기본적으로 `build`다.

Q. Vercel에서 React 새로고침 404는 어떻게 해결하는가?
A. 필요한 경우 `vercel.json` rewrites로 frontend route를 `index.html`로 보낸다.

Q. 모든 요청을 `/index.html`로 보내도 되는가?
A. 단독 SPA에서는 가능하지만 `/api` rewrite나 Serverless Function이 있으면 API 규칙을 먼저 분리해야 한다.

Q. Vercel에서 `/api` 요청이 HTML을 반환하면 무엇을 확인하는가?
A. `/api` rewrite 또는 function routing이 SPA fallback보다 먼저 처리되는지 확인해야 한다.

Q. Vercel rewrite에서 API와 SPA fallback 순서가 중요한가?
A. 중요하다. `/api` 요청이 `index.html`로 rewrite되면 안 된다.

Q. Vercel 배포 후 무엇을 검증해야 하는가?
A. Production URL, 직접 route 접근, 새로고침, JS/CSS asset, API 요청 Content-Type을 확인해야 한다.

---

## 4.2 Vercel API Proxy and Env

### [개념]

Vercel API Proxy and Env는 Vercel 배포에서 프론트엔드가 백엔드 API를 호출할 때 API URL과 rewrite를 설정하는 규칙이다.

---

### [핵심]

API 연동 방식:

```text
1. 외부 API 도메인 사용
→ VITE_API_BASE_URL=https://api.example.com

2. Same Path Rewrite 사용
→ /api 요청을 외부 backend로 rewrite

3. Vercel Serverless Function 사용
→ /api/*를 Vercel function으로 처리
```

주의:

- React SPA fallback rewrite와 API rewrite가 충돌하면 안 된다.
- `/api`를 `index.html`로 보내면 안 된다.
- CORS는 백엔드 설정과 함께 검토한다.
- Cookie 인증은 Domain / SameSite / Secure를 확인한다.

---

### [실무]

외부 API env 예:

```text
VITE_API_BASE_URL=https://api.example.com
```

Vercel rewrite 예:

```json
{
  "rewrites": [
    {
      "source": "/api/(.*)",
      "destination": "https://api.example.com/api/$1"
    },
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

검증 Flow:

```text
Production URL 접속
→ Network /api 요청 확인
→ API 응답이 JSON인지 확인
→ fallback이 /api를 잡지 않는지 확인
```

---

### [FAQ]

Q. Vercel에서 API Base URL은 어떻게 설정하는가?
A. 외부 API 도메인을 env로 설정하거나 `/api` rewrite를 사용할 수 있다.

Q. Vercel rewrite에서 /api와 SPA fallback 순서가 중요한가?
A. 중요하다. `/api` 요청이 `index.html`로 rewrite되면 안 된다.

Q. Vercel에서 CORS 문제가 사라지는가?
A. API rewrite를 사용하면 줄어들 수 있지만 백엔드 구조에 따라 여전히 확인이 필요하다.

Q. Vercel Serverless Function에 Secret을 둘 수 있는가?
A. 가능하다. 단, 프론트엔드 Build에 주입하지 말고 서버리스 함수 런타임에서 사용해야 한다.

---

# 5. Netlify Deployment Rules

## 5.1 Netlify Core Rules

### [개념]

Netlify는 Git 연동 기반으로 정적 사이트를 Build하고 CDN으로 배포하며 redirect / rewrite 설정을 제공하는 플랫폼이다.

---

### [핵심]

Netlify 설정 항목:

- Base Directory
- Build Command
- Publish Directory
- Environment Variables
- Redirects
- Rewrites
- Functions
- Deploy Preview
- Production Deploy
- Custom Domain

Vite 기준:

```text
Publish Directory: dist
```

CRA 기준:

```text
Publish Directory: build
```

---

### [실무]

Netlify 설정 예:

```text
Base Directory: frontend
Build Command: npm run build
Publish Directory: dist
```

CRA:

```text
Base Directory: frontend
Build Command: npm run build
Publish Directory: build
```

SPA redirect:

```text
/* /index.html 200
```

`netlify.toml` 예:

```toml
[build]
  base = "frontend"
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

---

### [FAQ]

Q. Netlify는 무엇인가?
A. 정적 사이트를 Build하고 CDN으로 배포하는 플랫폼이다.

Q. Netlify에서 Vite publish directory는 무엇인가?
A. 기본적으로 `dist`다.

Q. Netlify에서 CRA publish directory는 무엇인가?
A. 기본적으로 `build`다.

Q. Netlify에서 React 새로고침 404는 어떻게 해결하는가?
A. `_redirects` 또는 `netlify.toml`에 `/* /index.html 200`을 설정한다.

---

## 5.2 Netlify Redirect and API Proxy

### [개념]

Netlify Redirect and API Proxy는 Netlify에서 SPA fallback과 API proxy를 redirect 규칙으로 처리하는 방식이다.

---

### [핵심]

중요 원칙:

- API proxy 규칙이 SPA fallback보다 먼저 있어야 한다.
- SPA fallback은 frontend route만 처리해야 한다.
- `_redirects` 파일은 build output에 포함되어야 한다.
- Netlify Functions 경로와 충돌하지 않아야 한다.
- API rewrite 대상이 HTTPS인지 확인한다.

---

### [실무]

`public/_redirects` 예:

```text
/api/* https://api.example.com/api/:splat 200
/* /index.html 200
```

`netlify.toml` 예:

```toml
[[redirects]]
  from = "/api/*"
  to = "https://api.example.com/api/:splat"
  status = 200
  force = true

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

검증 Flow:

```text
배포 후 /api/health 호출
→ JSON 응답 확인
→ /login 직접 접근
→ index.html fallback 확인
```

---

### [FAQ]

Q. Netlify에서 API proxy와 SPA fallback 순서가 중요한가?
A. 중요하다. API proxy가 fallback보다 먼저 처리되어야 한다.

Q. \_redirects 파일은 어디에 둬야 하는가?
A. Build output에 포함되도록 보통 public 폴더에 둔다.

Q. Netlify에서 /api 요청이 index.html을 반환하면 무엇을 확인하는가?
A. `_redirects` 또는 `netlify.toml`에서 API proxy 규칙 순서를 확인한다.

Q. Netlify Functions와 API proxy가 충돌할 수 있는가?
A. 가능하다. functions path와 redirect path를 명확히 분리해야 한다.

---

# 6. Cloudflare Pages Rules

## 6.1 Cloudflare Pages Core

### [개념]

Cloudflare Pages는 Git 연동 기반으로 정적 프론트엔드 프로젝트를 Build하고 Cloudflare Edge Network로 배포하는 플랫폼이다.

---

### [핵심]

Cloudflare Pages 설정 항목:

- Framework Preset
- Build Command
- Build Output Directory
- Root Directory
- Environment Variables
- Preview Deploy
- Production Deploy
- Custom Domain
- Redirects
- Functions

Vite 기준:

```text
Build Command: npm run build
Output Directory: dist
```

CRA 기준:

```text
Build Command: npm run build
Output Directory: build
```

---

### [실무]

설정 예:

```text
Framework Preset: Vite
Root Directory: frontend
Build Command: npm run build
Build Output Directory: dist
```

SPA fallback은 플랫폼 설정 또는 `_redirects` 파일을 사용한다.

`_redirects` 예:

```text
/* /index.html 200
```

검증 Flow:

```text
Production URL 접속
→ route 직접 접근
→ 새로고침
→ API Request URL 확인
→ env 값 확인
```

---

### [FAQ]

Q. Cloudflare Pages는 무엇인가?
A. 정적 프론트엔드 프로젝트를 Cloudflare Edge Network로 배포하는 플랫폼이다.

Q. Cloudflare Pages에서 Vite output directory는 무엇인가?
A. 기본적으로 `dist`다.

Q. Cloudflare Pages에서 SPA fallback이 필요한가?
A. BrowserRouter 사용 시 필요할 수 있으며 직접 URL 접근으로 검증해야 한다.

Q. Cloudflare Pages에서도 env 변경 후 재배포가 필요한가?
A. Build-time env라면 재배포가 필요할 수 있다.

---

# 7. S3 CloudFront Deployment Rules

## 7.1 S3 Static Hosting Core

### [개념]

S3 Static Hosting은 AWS S3 Bucket에 React Build 결과물을 업로드해 정적 파일로 제공하는 방식이다.

CloudFront와 함께 사용하면 CDN, HTTPS, Custom Domain, Cache 제어가 가능하다.

---

### [핵심]

S3 + CloudFront 구성:

```text
React Build Output
→ S3 Bucket
→ CloudFront Distribution
→ User Browser
```

핵심 설정:

- S3 bucket
- Build Output upload
- CloudFront origin
- Default root object: `index.html`
- Custom error response
- Cache policy
- HTTPS certificate
- Custom domain
- Invalidation

---

### [실무]

배포 Flow:

```text
npm run build
→ dist or build 생성
→ aws s3 sync
→ CloudFront invalidation
→ HTTPS domain 접속
→ route refresh 검증
```

S3 sync 예:

```bash
aws s3 sync dist/ s3://my-bucket --delete
```

CRA:

```bash
aws s3 sync build/ s3://my-bucket --delete
```

주의:

```text
--delete 사용 시 S3에서 사라진 파일도 삭제
old asset 정리 가능
잘못 사용하면 필요한 파일도 삭제 가능
```

---

### [FAQ]

Q. S3 Static Hosting이란 무엇인가?
A. React Build 결과물을 S3 Bucket에 업로드해 정적 파일로 제공하는 방식이다.

Q. S3만으로 HTTPS와 CDN을 제공하기 쉬운가?
A. 보통 CloudFront와 함께 사용해 HTTPS, CDN, Custom Domain을 구성한다.

Q. S3에 무엇을 업로드해야 하는가?
A. Vite는 `dist` 내부 파일, CRA는 `build` 내부 파일을 업로드한다.

Q. S3 sync에서 --delete는 무엇인가?
A. 로컬에 없는 파일을 S3에서도 삭제해 이전 asset을 정리하는 옵션이다.

---

## 7.2 CloudFront SPA Fallback

### [개념]

CloudFront SPA Fallback은 React Router 직접 URL 접근 시 S3에 실제 파일이 없어도 `index.html`을 반환하도록 CloudFront error response를 설정하는 방식이다.

---

### [핵심]

필요 설정:

```text
Default Root Object: index.html

Custom Error Response:
403 → /index.html → 200
404 → /index.html → 200
```

주의:

- API 요청까지 index.html로 fallback하지 않도록 origin/path 구조를 분리한다.
- CloudFront cache 때문에 fallback 변경 반영이 늦을 수 있다.
- S3 권한 구조에 따라 403 또는 404가 발생할 수 있다.
- route refresh 테스트가 필수다.

---

### [실무]

검증 대상:

```text
/
/login
/detail/1
/assets/index.js
/api/health
```

정상 기준:

```text
/login
→ index.html

/assets/index.js
→ JavaScript file

/api/health
→ API JSON or separate API domain
```

Invalidation 예:

```bash
aws cloudfront create-invalidation \
  --distribution-id DISTRIBUTION_ID \
  --paths "/index.html" "/config.json"
```

---

### [FAQ]

Q. CloudFront에서 React 새로고침 404는 어떻게 해결하는가?
A. 403 또는 404 error response를 `/index.html`로 보내고 response code를 200으로 설정한다.

Q. S3/CloudFront에서 403을 fallback 대상으로 잡는 이유는?
A. S3 권한 구조에 따라 없는 route가 403으로 반환될 수 있기 때문이다.

Q. CloudFront fallback이 API 요청까지 잡으면 어떻게 되는가?
A. API 요청에 index.html이 반환될 수 있으므로 API origin/path를 분리해야 한다.

Q. CloudFront invalidation은 언제 필요한가?
A. 새 배포 후 이전 index.html이나 config.json이 계속 제공될 때 필요하다.

---

## 7.3 S3 CloudFront Cache Rules

### [개념]

S3 CloudFront Cache Rules는 정적 파일별 Cache-Control과 CloudFront cache 정책을 구분하는 규칙이다.

---

### [핵심]

권장 기준:

```text
index.html
→ no-cache 또는 짧은 cache

hashed JS/CSS
→ long cache

config.json
→ no-store 또는 짧은 cache

image/font hashed assets
→ long cache
```

주의:

- index.html 장기 캐시는 새 배포 반영을 방해한다.
- hashed asset은 장기 캐시가 가능하다.
- CloudFront invalidation 비용과 범위를 고려한다.
- Runtime Config는 캐시를 짧게 잡아야 한다.

---

### [실무]

S3 sync with cache 예:

```bash
aws s3 sync dist/ s3://my-bucket \
  --exclude "index.html" \
  --cache-control "public,max-age=31536000,immutable"

aws s3 cp dist/index.html s3://my-bucket/index.html \
  --cache-control "no-cache"
```

Runtime Config:

```bash
aws s3 cp dist/config.json s3://my-bucket/config.json \
  --cache-control "no-store"
```

검증 Flow:

```text
Network Response Headers 확인
→ Cache-Control 확인
→ CloudFront cache status 확인
→ 새 배포 반영 확인
```

---

### [FAQ]

Q. S3/CloudFront에서 index.html은 왜 짧게 캐시해야 하는가?
A. 새 배포 시 최신 JS/CSS hash를 참조해야 하기 때문이다.

Q. hashed asset은 왜 길게 캐시해도 되는가?
A. 내용이 바뀌면 파일명이 바뀌기 때문이다.

Q. config.json은 왜 no-store가 필요한가?
A. Runtime Config 값 변경이 즉시 반영되어야 할 수 있기 때문이다.

Q. CloudFront cache 문제는 어디서 확인하는가?
A. Network Response Headers와 CloudFront cache status를 확인한다.

---

# 8. GitHub Pages Rules

## 8.1 GitHub Pages Core

### [개념]

GitHub Pages는 GitHub Repository 기반으로 정적 파일을 무료 또는 간단하게 배포할 수 있는 서비스다.

---

### [핵심]

GitHub Pages 특징:

- 정적 파일 배포에 적합
- repository path 하위 경로 배포가 흔함
- 서버 rewrite 설정 제한
- BrowserRouter 새로고침 처리에 제약
- HashRouter가 단순한 해결책일 수 있음
- Vite `base` 또는 CRA `homepage` 설정이 중요
- API backend가 필요한 경우 별도 API 서버 필요

---

### [실무]

배포 URL 예:

```text
https://username.github.io/repository-name/
```

Vite base:

```js
export default defineConfig({
  base: "/repository-name/",
});
```

CRA homepage:

```json
{
  "homepage": "https://username.github.io/repository-name"
}
```

React Router basename:

```jsx
<BrowserRouter basename="/repository-name">
  <App />
</BrowserRouter>
```

HashRouter:

```jsx
<HashRouter>
  <App />
</HashRouter>
```

---

### [FAQ]

Q. GitHub Pages는 무엇인가?
A. GitHub Repository 기반 정적 파일 배포 서비스다.

Q. GitHub Pages에서 React Router 새로고침이 어려운 이유는?
A. 서버 rewrite 설정이 제한적이기 때문이다.

Q. GitHub Pages에서 가장 쉬운 라우팅 해결책은 무엇인가?
A. HashRouter 사용이 가장 단순할 수 있다.

Q. GitHub Pages 배포에서 base path가 중요한 이유는?
A. 보통 repository-name 하위 경로에서 앱이 제공되기 때문이다.

---

## 8.2 GitHub Pages Build Output

### [개념]

GitHub Pages Build Output은 GitHub Actions 또는 배포 도구가 React Build 결과물을 Pages artifact로 업로드하는 대상이다.

---

### [핵심]

기본 기준:

```text
Vite
→ dist

CRA
→ build
```

중요 확인:

- GitHub Actions artifact path
- base path
- router basename
- environment variables
- Pages source branch 또는 Actions 설정
- build output에 index.html 존재 여부

---

### [실무]

GitHub Actions Pages 예:

```yaml
name: Deploy Pages

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install
        working-directory: ./frontend
        run: npm ci

      - name: Build
        working-directory: ./frontend
        run: npm run build

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./frontend/dist
```

CRA라면:

```yaml
path: ./frontend/build
```

검증 Flow:

```text
Actions build log 확인
→ artifact path 확인
→ Pages URL 접속
→ asset 404 확인
→ route 새로고침 확인
```

---

### [FAQ]

Q. GitHub Pages에서 Vite artifact path는 무엇인가?
A. 보통 `dist`다.

Q. GitHub Pages에서 CRA artifact path는 무엇인가?
A. 보통 `build`다.

Q. GitHub Pages 배포 후 asset 404가 나면 무엇을 확인하는가?
A. Vite base, CRA homepage, artifact path, repository path를 확인한다.

Q. GitHub Pages에서 API 서버도 함께 실행되는가?
A. 아니다. GitHub Pages는 정적 파일 hosting이므로 API는 별도 서버가 필요하다.

---

# 9. Platform Troubleshooting

## 9.1 Platform Build Failure

### [개념]

Platform Build Failure는 Vercel, Netlify, Cloudflare Pages, GitHub Actions 같은 플랫폼에서 Build Command 실행 중 실패하는 문제다.

---

### [핵심]

대표 원인:

- Root Directory 오류
- Build Command 오류
- Output Directory 오류
- Node version mismatch
- package manager mismatch
- lock file 불일치
- env 누락
- TypeScript error
- ESLint error
- import path 대소문자 오류
- memory limit
- dependency install 실패

---

### [실무]

Troubleshooting Flow:

```text
Build Log 확인
→ 첫 번째 error 확인
→ Root Directory 확인
→ Node version 확인
→ package manager 확인
→ env 확인
→ local production build 재현
```

로컬 재현:

```bash
npm ci
npm run build
```

또는 yarn:

```bash
yarn install --frozen-lockfile
yarn build
```

Review 기준:

```md
- [ ] 로컬 clean install build가 성공하는가?
- [ ] 플랫폼 Node version이 맞는가?
- [ ] Root Directory가 맞는가?
- [ ] env가 설정되어 있는가?
- [ ] Linux 대소문자 import 문제가 없는가?
```

---

### [FAQ]

Q. 플랫폼 Build가 실패하면 무엇을 먼저 확인하는가?
A. Build Log의 첫 번째 실제 error를 먼저 확인한다.

Q. 로컬에서는 되는데 플랫폼에서 실패하는 이유는?
A. Node version, env, Linux 대소문자, lock file, Root Directory 차이 때문일 수 있다.

Q. package.json을 못 찾는 이유는?
A. Root Directory가 잘못 설정되었을 가능성이 높다.

Q. 플랫폼 Build 실패를 로컬에서 어떻게 재현하는가?
A. `npm ci` 후 `npm run build`로 clean build를 실행한다.

---

## 9.2 Platform Blank Page

### [개념]

Platform Blank Page는 플랫폼 배포는 성공했지만 브라우저에서 화면이 흰색으로 표시되는 문제다.

---

### [핵심]

대표 원인:

- JS bundle 404
- CSS 404
- Output Directory 오류
- base path 오류
- Vite `base` 오류
- CRA `homepage` 오류
- env undefined
- runtime error
- API 초기화 실패
- BrowserRouter fallback 문제
- 이전 cache

---

### [실무]

Troubleshooting Flow:

```text
Console Error 확인
→ Network JS/CSS 확인
→ asset 404 확인
→ Output Directory 확인
→ base/homepage 확인
→ env 값 확인
→ cache 확인
```

증상별 판단:

```text
JS 404
→ output/base path 문제

Unexpected token '<'
→ JS/API 요청이 index.html 반환

env undefined
→ platform env prefix/설정 문제

새로고침만 404
→ SPA fallback 문제
```

---

### [FAQ]

Q. 플랫폼 배포 후 흰 화면이면 무엇을 먼저 확인하는가?
A. Browser Console Error와 Network의 JS/CSS 요청 상태를 확인한다.

Q. 배포 성공인데 JS 404가 나는 이유는?
A. Output Directory, base path, asset 경로 설정이 잘못되었을 수 있다.

Q. env undefined가 플랫폼에서만 발생하는 이유는?
A. 플랫폼 환경 변수 설정이나 prefix가 잘못되었을 수 있다.

Q. 이전 화면이 계속 보이는 이유는?
A. 브라우저 캐시, CDN 캐시, Service Worker 문제가 있을 수 있다.

---

## 9.3 Platform Refresh 404

### [개념]

Platform Refresh 404는 플랫폼 배포 후 React route에서 새로고침하거나 직접 URL 접근 시 404가 발생하는 문제다.

---

### [핵심]

대표 원인:

- SPA fallback rewrite 누락
- Netlify `_redirects` 누락
- Vercel `rewrites` 누락
- CloudFront custom error response 누락
- GitHub Pages rewrite 제약
- sub path base / basename 불일치
- HashRouter 미사용

---

### [실무]

Troubleshooting Flow:

```text
메인 접속 확인
→ /login 직접 접근
→ /detail/1 새로고침
→ platform fallback 설정 확인
→ API path 제외 확인
→ 재배포
```

플랫폼별 해결:

```text
Vercel
→ vercel.json rewrites

Netlify
→ _redirects or netlify.toml

CloudFront
→ custom error response

GitHub Pages
→ HashRouter or 404 fallback workaround
```

---

### [FAQ]

Q. 플랫폼 배포 후 새로고침 404는 왜 발생하는가?
A. 플랫폼이 React route를 실제 파일로 찾고 fallback 설정이 없기 때문이다.

Q. Vercel에서 새로고침 404는 어떻게 해결하는가?
A. 필요한 경우 `vercel.json` rewrites를 설정한다.

Q. Netlify에서 새로고침 404는 어떻게 해결하는가?
A. `_redirects` 또는 `netlify.toml` redirect를 설정한다.

Q. GitHub Pages에서 새로고침 404는 어떻게 해결하는가?
A. HashRouter를 사용하거나 404 fallback workaround를 구성한다.

---

## 9.4 Platform API Failure

### [개념]

Platform API Failure는 플랫폼에 배포된 프론트엔드가 백엔드 API 호출에 실패하는 문제다.

---

### [핵심]

대표 원인:

- API Base URL이 localhost
- Production env 누락
- Preview env가 production API 호출
- HTTP API 호출로 Mixed Content 발생
- CORS allowed origin 누락
- Cookie Domain / SameSite / Secure 문제
- API rewrite가 SPA fallback과 충돌
- `/api` 요청이 index.html 반환
- 백엔드 서버 미배포
- 백엔드 HTTPS 인증서 문제

---

### [실무]

Troubleshooting Flow:

```text
Network Request URL 확인
→ API host 확인
→ status code 확인
→ CORS/Mixed Content 확인
→ platform env 확인
→ rewrite/proxy 규칙 확인
→ backend log 확인
```

증상별 판단:

```text
Request URL localhost
→ production env 누락

CORS error
→ backend allowed origin 확인

Mixed Content
→ API HTTPS 확인

Unexpected token '<'
→ API 요청이 index.html 반환

401
→ auth header/cookie 확인
```

---

### [FAQ]

Q. 플랫폼 배포 후 API가 localhost로 호출되는 이유는?
A. Production env가 누락되었거나 local env로 Build되었기 때문이다.

Q. 플랫폼 배포 후 CORS 에러가 나는 이유는?
A. 백엔드 CORS allowed origin에 플랫폼 도메인이 없을 수 있다.

Q. /api 요청이 index.html을 반환하면 무엇을 확인하는가?
A. platform rewrite/proxy와 SPA fallback 규칙 순서를 확인해야 한다.

Q. Preview 배포에서 운영 데이터가 바뀌면 무엇이 문제인가?
A. Preview env가 Production API를 호출하고 있을 가능성이 있다.

---

# 10. Agent Decision Rules

## 10.1 PM Agent Rules

### [개념]

PM Agent는 플랫폼 선택, Build 설정, 환경 변수, SPA fallback, API 연결, 검증 기준을 정의해야 한다.

---

### [핵심]

PM Agent 확인 항목:

- Deployment Platform
- Build Tool
- Root Directory
- Build Command
- Output Directory
- Node Version
- Production Env
- Preview Env
- API Base URL
- SPA Fallback 방식
- Custom Domain
- HTTPS
- Cache / CDN
- 배포 후 검증 route
- Rollback 필요 여부

---

### [실무]

PM Agent 산출물 예:

```text
Platform: Netlify
Root Directory: frontend
Build Tool: Vite
Build Command: npm run build
Publish Directory: dist
Env:
- VITE_API_BASE_URL=https://api.example.com
SPA Fallback:
- /* /index.html 200
API Strategy:
- external API domain
Verification:
- /
- /login refresh
- /api health call
- Network API URL
```

PM Agent 판단 Flow:

```text
배포 목적 확인
→ 플랫폼 선택
→ Build 설정 정의
→ env 분리
→ fallback/API 전략 정의
→ 검증 체크리스트 작성
```

---

### [FAQ]

Q. PM Agent는 플랫폼 배포에서 무엇을 정해야 하는가?
A. 플랫폼, root directory, build command, output directory, env, fallback, API 전략을 정해야 한다.

Q. PM Agent가 Preview Env도 정해야 하는가?
A. 그렇다. Preview가 운영 API를 호출하지 않도록 분리해야 한다.

Q. PM Agent가 플랫폼 선택 기준을 정해야 하는가?
A. 그렇다. 프로젝트 목적과 운영 요구사항에 맞는 플랫폼을 선택해야 한다.

Q. PM Agent가 배포 후 검증 route를 작성해야 하는가?
A. 그렇다. 직접 URL 접근, 새로고침, API 요청 검증이 필요하다.

---

## 10.2 Frontend Agent Rules

### [개념]

Frontend Agent는 플랫폼 배포에 맞게 Build Tool 설정, env prefix, base path, Router basename, API Base URL을 구성해야 한다.

---

### [핵심]

Frontend Agent 필수 기준:

- `npm run build` 성공
- Vite / CRA output directory 명확화
- env prefix 준수
- 운영 localhost 하드코딩 금지
- API Base URL env 분리
- GitHub Pages / sub path 배포 시 base path 설정
- BrowserRouter fallback 필요성 전달
- HashRouter 선택 시 이유 명확화
- env validation 적용
- asset path 확인

---

### [실무]

Vite env 예:

```env
VITE_API_BASE_URL=https://api.example.com
```

CRA env 예:

```env
REACT_APP_API_BASE_URL=https://api.example.com
```

GitHub Pages Vite base 예:

```js
export default defineConfig({
  base: "/repository-name/",
});
```

Frontend Agent 검증 기준:

```text
local build
→ output 확인
→ platform deploy
→ Console 확인
→ Network asset/API 확인
→ route refresh 확인
```

---

### [FAQ]

Q. Frontend Agent는 플랫폼 배포에서 무엇을 준비해야 하는가?
A. Build 성공, env 설정, base path, Router basename, API URL 분리를 준비해야 한다.

Q. 플랫폼 배포에서도 localhost API URL을 써도 되는가?
A. 운영에서는 안 된다. 실제 접근 가능한 API 도메인 또는 proxy path를 사용해야 한다.

Q. GitHub Pages 배포에서는 Frontend Agent가 무엇을 주의해야 하는가?
A. repository path에 맞는 base path와 Router 전략을 확인해야 한다.

Q. env validation은 플랫폼 배포에서도 필요한가?
A. 필요하다. env 누락으로 잘못된 API 요청이 발생하는 것을 막을 수 있다.

---

## 10.3 DevOps Agent Rules

### [개념]

DevOps Agent는 플랫폼 배포 설정, DNS, HTTPS, cache, rewrite, CI/CD 연결을 구현하고 검증해야 한다.

---

### [핵심]

DevOps Agent 필수 기준:

- Platform project 설정
- Root Directory 설정
- Build Command 설정
- Output Directory 설정
- Node Version 설정
- Environment Variables 설정
- SPA fallback 설정
- API rewrite/proxy 설정
- Custom Domain 연결
- HTTPS 인증서 확인
- Cache policy 확인
- Deploy log 확인
- Rollback 절차 확인

---

### [실무]

DevOps Agent 구현 Flow:

```text
Platform project 생성
→ Git repository 연결
→ root/build/output 설정
→ env 설정
→ fallback/rewrite 설정
→ deploy
→ custom domain 연결
→ HTTPS 확인
→ smoke test
```

Smoke Test:

```text
/ 접속
/login 직접 접근
/detail/1 새로고침
API 요청
asset 404
Console error
HTTPS
```

---

### [FAQ]

Q. DevOps Agent는 플랫폼 배포에서 무엇을 구현해야 하는가?
A. 플랫폼 프로젝트 설정, env, fallback, API rewrite, DNS, HTTPS, cache를 구현해야 한다.

Q. 플랫폼 배포 후 Deploy Log를 봐야 하는가?
A. 봐야 한다. Build Command, Output Directory, Node version 문제를 확인할 수 있다.

Q. Custom Domain 설정 후 무엇을 확인해야 하는가?
A. DNS 전파, HTTPS 인증서, API CORS origin을 확인해야 한다.

Q. rollback은 플랫폼에서 가능한가?
A. 대부분 이전 deploy로 rollback 기능을 제공하지만 플랫폼별 확인이 필요하다.

---

## 10.4 Review Agent Rules

### [개념]

Review Agent는 플랫폼 배포 결과가 Build, Output, Env, Routing, API, HTTPS, Cache 관점에서 정상인지 검토해야 한다.

---

### [핵심]

Review Agent Checklist:

```md
- [ ] Build Command가 맞는가?
- [ ] Output Directory가 맞는가?
- [ ] Root Directory가 맞는가?
- [ ] Node Version이 맞는가?
- [ ] Production Env가 설정되어 있는가?
- [ ] Preview Env가 Production API를 호출하지 않는가?
- [ ] Secret이 frontend env에 노출되지 않는가?
- [ ] 운영 API URL에 localhost가 없는가?
- [ ] SPA fallback이 있는가?
- [ ] API rewrite가 fallback보다 우선되는가?
- [ ] 직접 URL 접근이 정상인가?
- [ ] 새로고침이 정상인가?
- [ ] JS/CSS asset이 200인가?
- [ ] API 응답이 JSON인가?
- [ ] HTTPS와 Mixed Content가 정상인가?
- [ ] cache 문제로 이전 배포가 보이지 않는가?
```

---

### [실무]

Review Agent 판단 Flow:

```text
Deploy log 확인
→ Build 설정 확인
→ Env 확인
→ Production URL 접속
→ Console 확인
→ Network asset 확인
→ route refresh 확인
→ API request 확인
→ cache/header 확인
```

Critical Issue:

```text
Output Directory 오류
Production API URL localhost
Secret frontend env 노출
SPA fallback 누락
API 요청에 index.html 반환
HTTPS에서 HTTP API 호출
Preview가 Production API 호출
```

승인 기준:

```text
Build 성공
정적 파일 정상
Routing 정상
API 정상
Env 정상
Secret 미노출
HTTPS 정상
Critical Console Error 없음
```

---

### [FAQ]

Q. Review Agent는 플랫폼 배포에서 무엇을 가장 먼저 확인해야 하는가?
A. Deploy log와 실제 Production URL의 Console / Network 상태를 먼저 확인해야 한다.

Q. Output Directory가 틀리면 승인 가능한가?
A. 아니다. 정적 파일이 잘못 배포되어 화면이 깨질 수 있다.

Q. Preview가 Production API를 호출하면 승인 가능한가?
A. 아니다. 운영 데이터 오염 위험이 있다.

Q. API 요청에 index.html이 반환되면 승인 가능한가?
A. 아니다. fallback과 API rewrite가 충돌한 치명적 문제다.

---

# 11. Common Mistakes

## 11.1 Platform Deployment Common Mistakes

### [개념]

Platform Deployment Common Mistakes는 플랫폼 배포에서 Build 설정, env, fallback, API 연결, cache를 혼동해 발생하는 반복 실수다.

---

### [핵심]

자주 발생하는 실수:

- Root Directory 미설정
- Build Command 오류
- Vite `dist` 대신 `build` 지정
- CRA `build` 대신 `dist` 지정
- Node version mismatch
- package manager 혼용
- 플랫폼 env 누락
- env 변경 후 redeploy 누락
- Secret을 frontend env에 저장
- 운영 API URL에 localhost 사용
- Preview env가 Production API 호출
- BrowserRouter 사용 후 fallback 미설정
- Netlify `_redirects` 누락
- Vercel rewrites 누락
- CloudFront custom error response 누락
- GitHub Pages에서 base path 누락
- GitHub Pages에서 BrowserRouter rewrite 제약 무시
- API rewrite가 SPA fallback보다 뒤에 있음
- `/api` 요청이 index.html 반환
- HTTPS 페이지에서 HTTP API 호출
- CORS allowed origin에 플랫폼 도메인 누락
- CDN cache 때문에 이전 배포 표시
- config.json 장기 캐시

---

### [실무]

실수별 판단:

```text
Build fail
→ root/build/node/env 확인

흰 화면
→ output/base/asset/env/runtime 확인

새로고침 404
→ fallback/rewrite 확인

API localhost
→ production env 확인

API HTML 응답
→ rewrite/fallback 순서 확인

CORS error
→ backend allowed origin 확인

이전 화면
→ CDN/browser cache 확인
```

---

### [FAQ]

Q. 플랫폼 배포에서 가장 흔한 실수는 무엇인가?
A. Root Directory, Output Directory, 환경 변수 설정을 잘못하는 것이다.

Q. 플랫폼 배포에서 가장 치명적인 실수는 무엇인가?
A. Secret을 frontend env에 넣거나 운영 API URL이 localhost로 남는 것이다.

Q. 플랫폼 배포에서 새로고침 404가 흔한 이유는?
A. BrowserRouter를 사용하는데 SPA fallback/rewrite 설정이 없기 때문이다.

Q. 플랫폼 배포에서 API가 HTML을 반환하는 이유는?
A. API rewrite보다 SPA fallback이 먼저 적용되거나 API path가 fallback에 잡혔기 때문이다.

---

# 12. Part10 Quality Checklist

## 12.1 Document Quality

### [개념]

이 문서는 Frontend Build & Deploy Domain의 Part10이며 Platform Deployment Rules Retrieval에 최적화되어야 한다.

---

### [핵심]

문서 품질 기준:

- Platform Deployment 정의 포함
- Platform 선택 기준 포함
- Build Command Rules 포함
- Output Directory Rules 포함
- Root Directory Rules 포함
- Node Version Rules 포함
- Platform Env Core 포함
- Production / Preview Env 구분 포함
- Secret Exposure Risk 포함
- Vercel Deployment Rules 포함
- Netlify Deployment Rules 포함
- Cloudflare Pages Rules 포함
- S3 / CloudFront Rules 포함
- GitHub Pages Rules 포함
- Platform Troubleshooting 포함
- Agent별 판단 기준 포함
- Common Mistakes 포함
- Retrieval Queries 포함

---

### [실무]

Part10은 다음 문서와 연결된다.

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

Q. Part10의 핵심 목적은 무엇인가?
A. Vercel, Netlify, S3, CloudFront, GitHub Pages 같은 플랫폼 배포에서 Build, Output, Env, Routing, API 문제를 Agent가 정확히 판단하게 하는 것이다.

Q. Part10에서 Nginx나 Docker 상세 설정을 다루는가?
A. 아니다. 플랫폼 배포 중심으로 다루고 Nginx / Docker 상세는 이전 Part에서 분리한다.

Q. Part10에서 CI/CD 전체를 다루는가?
A. 아니다. 플랫폼 배포 설정만 다루고 CI/CD 상세 전략은 후속 Part에서 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. Platform Deployment란 무엇인가?
A. Vercel, Netlify, S3, CloudFront 같은 플랫폼을 사용해 React Build 결과물을 배포하는 방식이다.

Q. 플랫폼 배포에서도 Build가 필요한가?
A. 필요하다. 플랫폼은 보통 `npm run build`를 실행하고 결과 폴더를 배포한다.

Q. 플랫폼 배포에서 가장 중요한 설정은 무엇인가?
A. Build Command, Output Directory, Environment Variables, SPA fallback 설정이다.

Q. React 포트폴리오 배포는 어떤 플랫폼이 쉬운가?
A. Vercel, Netlify, Cloudflare Pages가 비교적 쉽다.

Q. AWS 기반 운영이면 어떤 방식을 고려하는가?
A. S3 + CloudFront를 고려할 수 있다.

Q. GitHub Pages는 언제 적합한가?
A. 간단한 정적 페이지나 문서, 데모 사이트에 적합하다.

Q. 플랫폼 배포에서 Build Command는 무엇인가?
A. 배포 전에 프론트엔드 정적 파일을 생성하기 위해 실행하는 명령이다.

Q. frontend가 하위 폴더에 있으면 무엇을 설정해야 하는가?
A. Root Directory 또는 working directory를 `frontend`로 설정해야 한다.

Q. Output Directory란 무엇인가?
A. Build 후 생성되어 플랫폼이 실제로 배포하는 정적 파일 폴더다.

Q. Vite Output Directory는 무엇인가?
A. 기본적으로 `dist`다.

Q. CRA Output Directory는 무엇인가?
A. 기본적으로 `build`다.

Q. Output Directory를 잘못 설정하면 어떤 문제가 생기는가?
A. index.html을 찾지 못하거나 JS/CSS asset 404가 발생할 수 있다.

Q. Root Directory란 무엇인가?
A. 플랫폼이 build command를 실행하고 프로젝트를 인식하는 기준 폴더다.

Q. frontend 폴더 안에 package.json이 있으면 Root Directory는 무엇인가?
A. 보통 `frontend`로 설정해야 한다.

Q. Root Directory가 틀리면 어떤 문제가 생기는가?
A. package.json을 못 찾거나 build command가 실패할 수 있다.

Q. 플랫폼 배포에서 Node version이 중요한 이유는?
A. 로컬에서는 성공한 build가 플랫폼 Node version 차이로 실패할 수 있기 때문이다.

Q. Node version은 어디에 명시하는가?
A. `package.json engines`, `.nvmrc`, 플랫폼 설정에서 명시할 수 있다.

Q. Platform Env란 무엇인가?
A. 배포 플랫폼에서 Build 시점에 주입하는 환경 변수다.

Q. 플랫폼 env를 바꾸면 즉시 반영되는가?
A. Build-time env라면 재배포가 필요할 수 있다.

Q. Vite platform env prefix는 무엇인가?
A. `VITE_`다.

Q. CRA platform env prefix는 무엇인가?
A. `REACT_APP_`다.

Q. Preview Env는 무엇인가?
A. PR이나 branch preview 배포에서 사용하는 환경 변수다.

Q. Preview 배포가 Production API를 호출해도 되는가?
A. 권장하지 않는다. 테스트 중 운영 데이터가 변경될 수 있다.

Q. 플랫폼 env에 Secret을 넣으면 안전한가?
A. 백엔드용이면 가능하지만 프론트엔드 Build에 주입하면 브라우저에 노출될 수 있다.

Q. VITE_OPENAI_API_KEY를 써도 되는가?
A. 안 된다. OpenAI API Key는 백엔드에서 사용해야 한다.

Q. Vercel은 무엇인가?
A. Git 연동으로 프론트엔드 프로젝트를 자동 Build하고 배포하는 플랫폼이다.

Q. Vercel에서 Vite Output Directory는 무엇인가?
A. 기본적으로 `dist`다.

Q. Vercel에서 CRA Output Directory는 무엇인가?
A. 기본적으로 `build`다.

Q. Vercel에서 React 새로고침 404는 어떻게 해결하는가?
A. 필요한 경우 `vercel.json` rewrites로 route를 `index.html`로 보낸다.

Q. Vercel에서 API Base URL은 어떻게 설정하는가?
A. 외부 API 도메인을 env로 설정하거나 `/api` rewrite를 사용할 수 있다.

Q. Vercel rewrite에서 /api와 SPA fallback 순서가 중요한가?
A. 중요하다. `/api` 요청이 `index.html`로 rewrite되면 안 된다.

Q. Netlify는 무엇인가?
A. 정적 사이트를 Build하고 CDN으로 배포하는 플랫폼이다.

Q. Netlify에서 Vite publish directory는 무엇인가?
A. 기본적으로 `dist`다.

Q. Netlify에서 CRA publish directory는 무엇인가?
A. 기본적으로 `build`다.

Q. Netlify에서 React 새로고침 404는 어떻게 해결하는가?
A. `_redirects` 또는 `netlify.toml`에 `/* /index.html 200`을 설정한다.

Q. Netlify에서 API proxy와 SPA fallback 순서가 중요한가?
A. 중요하다. API proxy가 fallback보다 먼저 처리되어야 한다.

Q. Cloudflare Pages는 무엇인가?
A. 정적 프론트엔드 프로젝트를 Cloudflare Edge Network로 배포하는 플랫폼이다.

Q. Cloudflare Pages에서 Vite output directory는 무엇인가?
A. 기본적으로 `dist`다.

Q. Cloudflare Pages에서도 env 변경 후 재배포가 필요한가?
A. Build-time env라면 재배포가 필요할 수 있다.

Q. S3 Static Hosting이란 무엇인가?
A. React Build 결과물을 S3 Bucket에 업로드해 정적 파일로 제공하는 방식이다.

Q. S3에 무엇을 업로드해야 하는가?
A. Vite는 `dist` 내부 파일, CRA는 `build` 내부 파일을 업로드한다.

Q. CloudFront에서 React 새로고침 404는 어떻게 해결하는가?
A. 403 또는 404 error response를 `/index.html`로 보내고 response code를 200으로 설정한다.

Q. S3/CloudFront에서 index.html은 왜 짧게 캐시해야 하는가?
A. 새 배포 시 최신 JS/CSS hash를 참조해야 하기 때문이다.

Q. GitHub Pages는 무엇인가?
A. GitHub Repository 기반 정적 파일 배포 서비스다.

Q. GitHub Pages에서 React Router 새로고침이 어려운 이유는?
A. 서버 rewrite 설정이 제한적이기 때문이다.

Q. GitHub Pages에서 가장 쉬운 라우팅 해결책은 무엇인가?
A. HashRouter 사용이 가장 단순할 수 있다.

Q. GitHub Pages에서 Vite artifact path는 무엇인가?
A. 보통 `dist`다.

Q. GitHub Pages에서 CRA artifact path는 무엇인가?
A. 보통 `build`다.

Q. 플랫폼 Build가 실패하면 무엇을 먼저 확인하는가?
A. Build Log의 첫 번째 실제 error를 먼저 확인한다.

Q. 로컬에서는 되는데 플랫폼에서 실패하는 이유는?
A. Node version, env, Linux 대소문자, lock file, Root Directory 차이 때문일 수 있다.

Q. 플랫폼 배포 후 흰 화면이면 무엇을 먼저 확인하는가?
A. Browser Console Error와 Network의 JS/CSS 요청 상태를 확인한다.

Q. 플랫폼 배포 후 새로고침 404는 왜 발생하는가?
A. 플랫폼이 React route를 실제 파일로 찾고 fallback 설정이 없기 때문이다.

Q. 플랫폼 배포 후 API가 localhost로 호출되는 이유는?
A. Production env가 누락되었거나 local env로 Build되었기 때문이다.

Q. 플랫폼 배포 후 CORS 에러가 나는 이유는?
A. 백엔드 CORS allowed origin에 플랫폼 도메인이 없을 수 있다.

Q. /api 요청이 index.html을 반환하면 무엇을 확인하는가?
A. platform rewrite/proxy와 SPA fallback 규칙 순서를 확인해야 한다.

Q. PM Agent는 플랫폼 배포에서 무엇을 정해야 하는가?
A. 플랫폼, root directory, build command, output directory, env, fallback, API 전략을 정해야 한다.

Q. Frontend Agent는 플랫폼 배포에서 무엇을 준비해야 하는가?
A. Build 성공, env 설정, base path, Router basename, API URL 분리를 준비해야 한다.

Q. DevOps Agent는 플랫폼 배포에서 무엇을 구현해야 하는가?
A. 플랫폼 프로젝트 설정, env, fallback, API rewrite, DNS, HTTPS, cache를 구현해야 한다.

Q. Review Agent는 플랫폼 배포에서 무엇을 가장 먼저 확인해야 하는가?
A. Deploy log와 실제 Production URL의 Console / Network 상태를 먼저 확인해야 한다.

Q. 플랫폼 배포에서 가장 흔한 실수는 무엇인가?
A. Root Directory, Output Directory, 환경 변수 설정을 잘못하는 것이다.

Q. Part10 다음 문서는 무엇인가?
A. Part11 CI/CD Rules로 이어지는 것이 적합하다.
