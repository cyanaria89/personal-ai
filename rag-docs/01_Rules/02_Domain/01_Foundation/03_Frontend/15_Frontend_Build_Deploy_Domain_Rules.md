# Frontend Build & Deploy Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

Frontend Build & Deploy Domain Rules 문서는 Frontend Agent / Review Agent / PM Agent가 프론트엔드 프로젝트의 빌드, 배포, 운영 환경 구성, 정적 파일 제공, SPA 라우팅, 환경 변수, 배포 후 검증을 판단하기 위한 RAG Retrieval 최적화 문서이다.

목적:

- React / Vite / CRA 프로젝트 빌드 방식 이해
- Development Server와 Production Build 차이 판단
- `.env` 환경 변수 처리 규칙 판단
- API Base URL 운영 환경 분리 지원
- 정적 파일 배포 구조 이해
- SPA 새로고침 404 문제 해결
- Spring Boot + React 통합 배포 판단
- Nginx 정적 파일 배포 판단
- Docker 기반 프론트엔드 배포 판단
- Vercel / Netlify / S3 / CloudFront 배포 판단
- CI/CD 파이프라인 기초 검토
- 배포 후 Console / Network / Routing / Cache 문제 분석
- Review Agent의 배포 전후 체크리스트 제공

---

### [핵심]

Frontend Build & Deploy에서 가장 중요한 기준:

1. Source Code와 Build Output 구분
2. Development Server와 Production Server 구분
3. 환경 변수는 빌드 시점 주입 여부 확인
4. 운영 API 주소와 개발 API 주소 분리
5. SPA 라우팅 fallback 설정 필요
6. 정적 파일 경로와 base path 확인
7. 브라우저 캐시와 파일 해시 전략 확인
8. HTTPS / CORS / Cookie / Authorization 설정 확인
9. 배포 후 Network / Console / Application 탭 검증
10. CI/CD는 install → test → build → deploy 순서 유지

---

### [실무]

Frontend Agent는 사용자의 배포 관련 질문을 받으면 다음 순서로 판단한다.

```text
Project Type 확인
→ Build Tool 확인
→ Environment Variable 확인
→ API Base URL 확인
→ Router 방식 확인
→ Static File Hosting 방식 확인
→ Backend 통합 여부 확인
→ Deployment Target 확인
→ Build Command 확인
→ 배포 후 검증 항목 제시
```

---

### [FAQ]

Q. Frontend Build & Deploy 문서는 사람 공부용이야?

A.
아니다. Frontend Agent / Review Agent / PM Agent가 배포 구조를 판단하고 문제를 해결하기 위한 RAG 문서다.

Q. 프론트엔드 빌드는 서버를 만드는 거야?

A.
대부분 아니다. React / Vite / CRA 빌드는 HTML, CSS, JS, assets 같은 정적 파일 결과물을 만든다.

Q. 개발 서버에서 잘 되는데 배포하면 안 되는 이유는?

A.
환경 변수, API URL, SPA fallback, CORS, HTTPS, cache, base path 문제가 대표 원인이다.

Q. 배포 문제를 볼 때 가장 먼저 확인할 것은?

A.
브라우저 개발자 도구의 Console과 Network 탭, 빌드 결과물, 환경 변수, API 요청 URL을 먼저 확인한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Frontend Build & Deploy 문서는 프론트엔드 운영 배포에 필요한 실무 범위를 포함한다.

포함 범위:

- Build 개념
- Production Build
- Development Server
- Static File Hosting
- React Build
- Vite Build
- CRA Build
- `.env` 환경 변수
- API Base URL
- SPA Routing
- Refresh 404
- Nginx Static Hosting
- Spring Boot Static Resource 통합 배포
- Docker Build
- Docker Nginx Serve
- Vercel Deploy
- Netlify Deploy
- AWS S3 Static Hosting
- CloudFront CDN
- HTTPS
- CORS
- Cookie / SameSite / Secure
- Browser Cache
- Source Map
- CI/CD Pipeline
- GitHub Actions 기초
- Build Error Troubleshooting
- Deploy Error Troubleshooting
- Deployment Checklist

---

### [핵심]

반드시 포함:

- 빌드는 정적 파일 생성 과정
- 배포는 정적 파일을 사용자에게 제공하는 과정
- React Router는 서버 fallback 설정 필요
- `.env` 값은 브라우저에 노출될 수 있음
- 프론트엔드 환경 변수에 비밀키 저장 금지
- API URL은 환경별로 분리
- 운영에서는 HTTPS 기준으로 판단
- 정적 파일 캐시는 hash 기반으로 관리
- 배포 후에는 Network 요청 URL을 반드시 확인

---

### [실무]

Frontend Build & Deploy는 Backend / DevOps와 연결된다.

```text
Frontend Source Code
→ Build
→ Static Files
→ Hosting Server
→ Browser
→ Backend API Request
```

Backend 통합 배포 Flow:

```text
React Build
→ build or dist 생성
→ Spring Boot static 폴더로 복사
→ Spring Boot Build
→ 단일 서버에서 index.html 제공
```

Nginx 단독 배포 Flow:

```text
React Build
→ dist 생성
→ Nginx html directory 복사
→ Nginx fallback 설정
→ API Proxy 설정
```

---

### [FAQ]

Q. 배포 문서에 CORS도 포함해야 해?

A.
포함해야 한다. 프론트엔드 배포 후 API 호출 실패의 대표 원인이 CORS와 인증 쿠키 설정이다.

Q. Docker는 이 문서 범위야?

A.
프론트엔드 빌드 결과물을 Nginx로 제공하는 기초 Docker 배포는 포함한다. Docker 심화는 별도 DevOps 문서로 분리한다.

Q. AWS 심화도 포함해?

A.
S3, CloudFront, 정적 호스팅 개념은 포함한다. VPC, ECS, EKS 같은 심화 인프라는 DevOps 문서 범위다.

---

## 2.2 Excluded Scope

### [개념]

Frontend Build & Deploy 문서는 프론트엔드 배포 기초와 실무 판단에 집중한다.

제외 범위:

- Kubernetes 심화
- Terraform 심화
- Advanced CI/CD 전략
- Blue-Green Deployment 심화
- Canary Deployment 심화
- Micro Frontend 심화
- Next.js SSR / SSG / ISR 심화
- Server Component 배포 심화
- Edge Runtime 심화
- Observability 심화
- Performance Profiling 심화
- Webpack Plugin 심화 개발
- Rollup Plugin 심화 개발

---

### [핵심]

제외 이유:

- Level 3 Frontend Foundation 범위 초과
- DevOps Expert / Frontend Expert 문서와 분리 필요
- RAG Retrieval 혼선 방지
- Chunk 품질 유지

---

### [실무]

배포 문서는 실무 프론트엔드 개발자가 자주 겪는 문제를 우선한다.

우선순위:

```text
Build Error
→ Environment Variable
→ API URL
→ SPA Routing
→ Static File Path
→ CORS
→ Cache
→ Deploy Verification
```

---

### [FAQ]

Q. Next.js 배포도 여기서 자세히 다뤄?

A.
아니다. React SPA 중심으로 다루고 Next.js SSR / SSG / ISR은 Frontend Expert 문서에서 다룬다.

Q. Kubernetes 배포도 여기서 다뤄?

A.
아니다. 프론트엔드 Docker 이미지 기초까지만 다루고 Kubernetes는 DevOps Expert 범위다.

---

# 3. Build Core Rules

## 3.1 Build Definition

### [개념]

Build는 프론트엔드 소스 코드를 브라우저가 실행할 수 있는 정적 파일로 변환하는 과정이다.

예:

```text
src/
public/
package.json
vite.config.js
↓
npm run build
↓
dist/
index.html
assets/index.[hash].js
assets/index.[hash].css
```

---

### [핵심]

Build 과정에서 수행되는 작업:

- JSX 변환
- TypeScript 변환
- JavaScript 번들링
- CSS 번들링
- 코드 압축
- Tree Shaking
- Asset 경로 처리
- 파일명 hash 적용
- 환경 변수 주입
- Production Mode 최적화

---

### [실무]

React 프로젝트에서 빌드 결과물은 보통 다음 폴더에 생성된다.

| Tool     | Build Command   | Output Directory |
| -------- | --------------- | ---------------- |
| Vite     | `npm run build` | `dist`           |
| CRA      | `npm run build` | `build`          |
| Next.js  | `next build`    | `.next`          |
| Vue Vite | `npm run build` | `dist`           |

---

### [FAQ]

Q. npm run build 하면 서버가 실행돼?

A.
아니다. 일반 React / Vite / CRA에서는 정적 파일이 생성될 뿐이다. 별도 웹 서버가 필요하다.

Q. build 폴더와 dist 폴더 차이는?

A.
빌드 도구별 기본 출력 폴더 차이다. CRA는 보통 build, Vite는 보통 dist를 사용한다.

Q. 빌드 결과물을 직접 브라우저로 열어도 돼?

A.
권장하지 않는다. 라우팅과 asset 경로 문제를 피하려면 정적 서버로 제공해야 한다.

---

## 3.2 Development Server vs Production Build

### [개념]

Development Server는 개발 중 확인용 서버이고, Production Build는 실제 배포용 결과물이다.

---

### [Comparison]

| 구분       | Development Server         | Production Build     |
| ---------- | -------------------------- | -------------------- |
| 목적       | 개발 중 빠른 확인          | 실제 사용자 배포     |
| 명령어     | `npm run dev`, `npm start` | `npm run build`      |
| 최적화     | 낮음                       | 높음                 |
| Hot Reload | 있음                       | 없음                 |
| Source Map | 자세함                     | 제한 또는 비활성     |
| 파일 해시  | 보통 없음                  | 있음                 |
| 서버       | 개발 서버 내장             | 별도 정적 서버 필요  |
| 환경       | local                      | staging / production |

---

### [실무]

개발 서버에서 정상 동작했지만 배포 후 실패하는 대표 원인:

- API URL이 `localhost`로 남아 있음
- `.env.production` 값이 반영되지 않음
- React Router fallback 설정 없음
- asset base path가 잘못됨
- CORS 설정이 운영 도메인을 허용하지 않음
- HTTPS 페이지에서 HTTP API 호출
- 쿠키 Secure / SameSite 설정 문제
- 브라우저 캐시 문제

---

### [FAQ]

Q. npm start로 실행되는 화면을 그대로 배포하면 안 돼?

A.
운영 배포에는 적합하지 않다. 개발 서버는 개발 편의용이고 운영은 build 결과물을 정적 서버로 제공해야 한다.

Q. 개발에서는 API가 되는데 배포하면 안 되는 이유는?

A.
운영 도메인, CORS, HTTPS, Cookie, 환경 변수, API Base URL이 달라지기 때문이다.

---

## 3.3 Build Command Rules

### [개념]

Build Command는 프로젝트를 운영 배포용 파일로 변환하는 명령이다.

예:

```bash
npm run build
```

---

### [핵심]

Agent가 확인해야 할 항목:

- `package.json`의 scripts
- build script 존재 여부
- Node.js 버전
- package manager
- lock file
- 환경 변수
- TypeScript compile error
- ESLint error
- output directory
- base path 설정

---

### [예제]

package.json 예:

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

CRA 예:

```json
{
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build"
  }
}
```

---

### [실무]

Build 실패 시 우선 확인:

```text
Error Message 확인
→ package.json scripts 확인
→ Node Version 확인
→ npm install 재수행
→ TypeScript Error 확인
→ ESLint Error 확인
→ Environment Variable 확인
→ Build Tool Config 확인
```

---

### [FAQ]

Q. build 명령어가 없으면 어떻게 해?

A.
package.json의 scripts를 확인하고 사용하는 빌드 도구에 맞게 build script를 추가해야 한다.

Q. npm run build에서 TypeScript 에러가 나면 배포해도 돼?

A.
권장하지 않는다. TypeScript 에러는 운영 장애로 이어질 수 있으므로 해결 후 배포한다.

Q. npm run dev는 되는데 npm run build는 실패할 수 있어?

A.
가능하다. Production Build에서는 타입 검사, 최적화, 환경 변수 처리 방식이 더 엄격하게 적용될 수 있다.

---

# 4. Build Tool Rules

## 4.1 Vite Build Rules

### [개념]

Vite는 빠른 개발 서버와 Rollup 기반 Production Build를 제공하는 프론트엔드 빌드 도구다.

---

### [핵심]

Vite 기준:

- 개발 명령: `npm run dev`
- 빌드 명령: `npm run build`
- 미리보기: `npm run preview`
- 기본 출력: `dist`
- 환경 변수 prefix: `VITE_`
- 환경 변수 접근: `import.meta.env`

---

### [예제]

Vite 환경 변수:

```env
VITE_API_BASE_URL=https://api.example.com
```

사용 예:

```js
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
```

---

### [실무]

Vite 배포 검토 항목:

```md
- [ ] `npm run build` 성공 여부
- [ ] `dist` 폴더 생성 여부
- [ ] `VITE_` prefix 사용 여부
- [ ] `import.meta.env` 사용 여부
- [ ] `base` 설정 필요 여부
- [ ] React Router fallback 설정 여부
- [ ] API Base URL 운영 값 확인
```

---

### [FAQ]

Q. Vite에서 process.env를 써도 돼?

A.
일반적으로 Vite 클라이언트 코드에서는 `import.meta.env`를 사용한다.

Q. Vite 환경 변수는 왜 VITE\_로 시작해야 해?

A.
클라이언트 코드에 노출할 환경 변수를 명시적으로 제한하기 위한 규칙이다.

Q. Vite build 결과물은 어디에 생겨?

A.
기본적으로 `dist` 폴더에 생성된다.

---

## 4.2 CRA Build Rules

### [개념]

CRA(Create React App)는 React 프로젝트의 기존 표준 도구 중 하나이며, build 결과물은 보통 `build` 폴더에 생성된다.

---

### [핵심]

CRA 기준:

- 개발 명령: `npm start`
- 빌드 명령: `npm run build`
- 기본 출력: `build`
- 환경 변수 prefix: `REACT_APP_`
- 환경 변수 접근: `process.env.REACT_APP_NAME`

---

### [예제]

CRA 환경 변수:

```env
REACT_APP_API_BASE_URL=https://api.example.com
```

사용 예:

```js
const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;
```

---

### [실무]

CRA 배포 검토 항목:

```md
- [ ] `npm run build` 성공 여부
- [ ] `build` 폴더 생성 여부
- [ ] `REACT_APP_` prefix 사용 여부
- [ ] `homepage` 설정 필요 여부
- [ ] React Router fallback 설정 여부
- [ ] API Base URL 운영 값 확인
```

---

### [FAQ]

Q. CRA에서 환경 변수가 안 읽혀?

A.
변수명이 `REACT_APP_`로 시작하는지 확인해야 한다. `.env` 수정 후 개발 서버 재시작도 필요하다.

Q. CRA build 폴더를 Spring Boot에 넣어도 돼?

A.
가능하다. `build` 결과물을 Spring Boot의 static resource 경로에 복사하는 방식으로 통합 배포할 수 있다.

Q. CRA는 Vite와 뭐가 달라?

A.
CRA는 react-scripts 기반이고 Vite는 더 빠른 개발 서버와 Rollup 기반 빌드를 제공한다. 신규 프로젝트는 Vite를 많이 사용한다.

---

## 4.3 Build Tool Comparison

### [Comparison]

| 항목                 | Vite              | CRA                       |
| -------------------- | ----------------- | ------------------------- |
| 개발 서버            | 빠름              | 상대적으로 느림           |
| 빌드 결과            | `dist`            | `build`                   |
| 환경 변수 prefix     | `VITE_`           | `REACT_APP_`              |
| 환경 변수 접근       | `import.meta.env` | `process.env`             |
| 설정 파일            | `vite.config.js`  | 숨겨진 react-scripts 중심 |
| 신규 프로젝트 적합성 | 높음              | 낮아지는 추세             |

---

### [실무]

Agent 판단 기준:

```text
Vite Project
→ dist 확인
→ import.meta.env 확인
→ VITE_ prefix 확인

CRA Project
→ build 확인
→ process.env 확인
→ REACT_APP_ prefix 확인
```

---

### [FAQ]

Q. Vite 프로젝트인데 REACT*APP* 환경 변수를 써도 돼?

A.
일반적으로 안 된다. Vite에서는 `VITE_` prefix를 사용해야 한다.

Q. CRA 프로젝트인데 import.meta.env를 써도 돼?

A.
일반적으로 안 된다. CRA에서는 `process.env.REACT_APP_...` 방식을 사용한다.

---

# 5. Environment Variable Rules

## 5.1 Frontend Environment Variable

### [개념]

Frontend Environment Variable은 빌드 시점에 클라이언트 코드에 주입되는 환경별 설정 값이다.

---

### [핵심]

중요 규칙:

- 프론트엔드 환경 변수는 브라우저에 노출될 수 있음
- 비밀키 저장 금지
- API Base URL 같은 공개 가능한 설정만 사용
- 빌드 시점에 값이 결정되는 경우가 많음
- `.env` 수정 후 개발 서버 재시작 필요
- 배포 환경에서는 플랫폼 설정값과 빌드 시점 확인 필요

---

### [주의]

프론트엔드 `.env`에 넣으면 안 되는 값:

```text
DB_PASSWORD
JWT_SECRET
OPENAI_API_KEY
AWS_SECRET_ACCESS_KEY
TOSS_SECRET_KEY
PRIVATE_KEY
ADMIN_PASSWORD
```

넣을 수 있는 값:

```text
API_BASE_URL
PUBLIC_KAKAO_JS_KEY
PUBLIC_MAP_KEY
APP_ENV
SENTRY_DSN_PUBLIC
```

단, public key도 도메인 제한과 사용량 제한을 설정해야 한다.

---

### [FAQ]

Q. 프론트엔드 .env에 API Secret Key를 넣어도 돼?

A.
안 된다. 프론트엔드 코드는 브라우저에서 볼 수 있으므로 Secret Key는 백엔드에 보관해야 한다.

Q. .env를 수정했는데 값이 안 바뀌어?

A.
개발 서버를 재시작하고, 배포 환경에서는 다시 빌드해야 한다.

Q. 환경 변수는 런타임에 바뀌어?

A.
일반 React SPA에서는 대부분 빌드 시점에 주입된다. 런타임 변경이 필요하면 별도 config 파일 전략이 필요하다.

---

## 5.2 Environment File Rules

### [개념]

환경별 `.env` 파일은 개발, 테스트, 운영 설정을 분리하기 위해 사용한다.

예:

```text
.env
.env.local
.env.development
.env.production
```

---

### [핵심]

권장 분리:

```text
Local Development → .env.local
Development → .env.development
Production → .env.production
```

환경별 API URL 예:

```env
VITE_API_BASE_URL=http://localhost:8080
```

```env
VITE_API_BASE_URL=https://api.example.com
```

---

### [실무]

환경 변수 관리 원칙:

```md
- [ ] Secret Key를 프론트엔드 env에 넣지 않는다.
- [ ] 개발 API와 운영 API를 분리한다.
- [ ] 환경 변수 prefix를 빌드 도구에 맞춘다.
- [ ] `.env.local`은 Git에 올리지 않는다.
- [ ] `.env.example`은 제공한다.
- [ ] 배포 플랫폼 환경 변수 설정과 로컬 env를 구분한다.
```

---

### [예제]

`.env.example` 예:

```env
VITE_API_BASE_URL=
VITE_KAKAO_JS_KEY=
VITE_APP_ENV=
```

---

### [FAQ]

Q. .env 파일을 GitHub에 올려도 돼?

A.
Secret이 없다면 가능하지만 보통 `.env.example`만 올리고 실제 `.env.local`은 제외한다.

Q. 운영 API 주소는 어디에 넣어?

A.
Vite는 `VITE_API_BASE_URL`, CRA는 `REACT_APP_API_BASE_URL`처럼 빌드 도구 규칙에 맞게 넣는다.

Q. .env.production을 만들면 자동으로 운영에 적용돼?

A.
빌드 명령과 모드에 따라 적용된다. 배포 플랫폼의 환경 변수 설정이 우선될 수도 있으므로 확인해야 한다.

---

## 5.3 Runtime Config Rules

### [개념]

Runtime Config는 빌드 후에도 설정 값을 바꿀 수 있도록 외부 설정 파일을 읽는 방식이다.

일반 React SPA의 환경 변수는 보통 빌드 시점에 고정된다.

---

### [핵심]

Runtime Config가 필요한 상황:

- 동일 빌드 파일을 여러 환경에 배포
- API URL을 배포 후 변경해야 함
- Docker 이미지 하나로 dev / staging / production 대응
- 빌드 없이 설정만 교체하고 싶음

---

### [예제]

public config 예:

```json
{
  "apiBaseUrl": "https://api.example.com"
}
```

앱 시작 시 로드:

```js
async function loadConfig() {
  const response = await fetch("/config.json");
  return response.json();
}
```

---

### [실무]

Runtime Config 주의:

- Secret 저장 금지
- 앱 초기화 전 config loading 필요
- config fetch 실패 fallback 필요
- 캐시 정책 주의
- TypeScript 타입 정의 권장

---

### [FAQ]

Q. React에서 env 값을 배포 후 바꿀 수 없어?

A.
일반적으로 build 시점에 들어가기 때문에 배포 후 변경하려면 재빌드가 필요하다. Runtime Config를 쓰면 일부 설정은 재빌드 없이 바꿀 수 있다.

Q. Runtime Config에 secret을 넣어도 돼?

A.
안 된다. public config 파일도 브라우저에서 접근 가능하다.

---

# 6. API Base URL Rules

## 6.1 API Base URL

### [개념]

API Base URL은 프론트엔드가 백엔드 API를 호출할 때 사용하는 기본 주소다.

예:

```text
http://localhost:8080
https://api.example.com
/api
```

---

### [핵심]

환경별 API URL:

```text
Local Frontend → http://localhost:8080
Production Frontend → https://api.example.com
Same Origin Proxy → /api
```

---

### [예제]

Axios instance 예:

```js
import axios from "axios";

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 10000,
});
```

---

### [실무]

API Base URL 검토 항목:

```md
- [ ] localhost가 운영 빌드에 남아 있지 않은가?
- [ ] HTTPS 페이지에서 HTTP API를 호출하지 않는가?
- [ ] 백엔드 CORS 허용 도메인에 프론트엔드 운영 도메인이 있는가?
- [ ] 인증 쿠키 사용 시 credentials 설정이 맞는가?
- [ ] JWT 사용 시 Authorization header가 포함되는가?
- [ ] 프록시 경로 `/api`와 실제 백엔드 경로가 충돌하지 않는가?
```

---

### [FAQ]

Q. 배포했는데 API 요청이 localhost로 가?

A.
운영 환경 변수 설정이 잘못되었거나 build 시점에 개발용 API URL이 들어간 것이다.

Q. API Base URL을 하드코딩해도 돼?

A.
권장하지 않는다. 환경 변수 또는 config로 분리해야 개발 / 운영 환경을 안전하게 전환할 수 있다.

Q. baseURL을 `/api`로 써도 돼?

A.
가능하다. 같은 도메인에서 Nginx나 백엔드 프록시가 `/api`를 백엔드로 전달하는 구조일 때 적합하다.

---

## 6.2 CORS and Credentials

### [개념]

CORS는 브라우저가 다른 Origin으로 API 요청을 보낼 때 적용하는 보안 정책이다.

Origin은 protocol, domain, port 조합이다.

예:

```text
http://localhost:3000
https://example.com
https://api.example.com
```

---

### [핵심]

CORS 문제 발생 조건:

- 프론트엔드와 백엔드 도메인이 다름
- 포트가 다름
- HTTP / HTTPS가 다름
- Authorization Header 사용
- Cookie 인증 사용
- Preflight 요청 필요

---

### [실무]

Cookie 인증 시 필요한 조건:

```js
axios.create({
  baseURL: "https://api.example.com",
  withCredentials: true,
});
```

백엔드도 다음을 허용해야 한다.

```text
Access-Control-Allow-Origin: https://frontend.example.com
Access-Control-Allow-Credentials: true
```

주의:

```text
Credentials 사용 시 Access-Control-Allow-Origin: * 사용 불가
```

---

### [FAQ]

Q. CORS는 프론트엔드에서 해결하는 거야?

A.
대부분 백엔드 서버에서 허용 Origin, Method, Header, Credentials를 설정해야 해결된다.

Q. withCredentials는 언제 써?

A.
쿠키 기반 인증을 사용할 때 필요하다. JWT를 Authorization Header로 보내는 구조에서는 보통 필요하지 않다.

Q. 운영에서만 CORS 에러가 나는 이유는?

A.
운영 프론트엔드 도메인이 백엔드 CORS 허용 목록에 없거나 HTTPS / Cookie 설정이 다르기 때문이다.

---

## 6.3 HTTPS Mixed Content

### [개념]

Mixed Content는 HTTPS 페이지에서 HTTP 리소스나 API를 호출할 때 발생하는 보안 문제다.

---

### [핵심]

문제 상황:

```text
Frontend: https://example.com
API: http://api.example.com
Result: Mixed Content Blocked
```

해결:

```text
Frontend: https://example.com
API: https://api.example.com
```

---

### [실무]

운영 배포 기준:

```md
- [ ] 프론트엔드가 HTTPS인가?
- [ ] 백엔드 API도 HTTPS인가?
- [ ] 이미지 / script / font도 HTTPS인가?
- [ ] WebSocket 사용 시 wss인가?
- [ ] Cookie Secure 설정이 필요한가?
```

---

### [FAQ]

Q. HTTPS 사이트에서 HTTP API를 호출하면 왜 안 돼?

A.
브라우저가 보안상 Mixed Content로 차단할 수 있다.

Q. WebSocket도 HTTPS 영향을 받아?

A.
받는다. HTTPS 페이지에서는 `ws://` 대신 `wss://`를 사용해야 한다.

---

# 7. Static File Hosting Rules

## 7.1 Static File Hosting

### [개념]

Static File Hosting은 빌드된 HTML, CSS, JS, 이미지 파일을 웹 서버가 그대로 제공하는 방식이다.

---

### [핵심]

정적 파일 예:

```text
index.html
assets/index.abc123.js
assets/index.def456.css
favicon.ico
logo.png
manifest.json
```

정적 호스팅 대상:

- Nginx
- Apache
- Spring Boot static
- Vercel
- Netlify
- AWS S3
- CloudFront
- GitHub Pages

---

### [실무]

정적 파일 제공 Flow:

```text
Browser Request
→ Web Server
→ index.html
→ JS/CSS Assets Load
→ React App Boot
→ API Request
```

---

### [FAQ]

Q. React 빌드 결과물은 어디에 올려야 해?

A.
Nginx, Spring Boot static, Vercel, Netlify, S3 같은 정적 파일 제공 환경에 올리면 된다.

Q. 정적 파일 서버와 백엔드 서버는 같아야 해?

A.
같을 수도 있고 다를 수도 있다. 같으면 CORS가 단순해지고, 다르면 배포와 확장이 유연해진다.

---

## 7.2 Asset Path Rules

### [개념]

Asset Path는 빌드된 JS, CSS, 이미지 파일을 브라우저가 불러오는 경로다.

---

### [핵심]

문제 상황:

```text
index.html은 열리지만 JS/CSS가 404
이미지가 깨짐
배포 경로 하위 디렉토리에서 assets 경로가 틀어짐
```

원인:

- base path 설정 오류
- homepage 설정 오류
- public path 오류
- 상대 경로 / 절대 경로 혼동
- 서버 location 설정 오류

---

### [실무]

Vite base 설정 예:

```js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  base: "/",
});
```

하위 경로 배포 예:

```js
export default defineConfig({
  base: "/my-app/",
});
```

CRA homepage 예:

```json
{
  "homepage": "/my-app"
}
```

---

### [FAQ]

Q. 배포 후 화면이 하얗고 JS 파일이 404야?

A.
asset base path가 잘못되었을 가능성이 높다. Vite의 `base`, CRA의 `homepage`, 서버 정적 경로를 확인한다.

Q. 루트가 아닌 `/app` 경로에 배포하면 설정이 필요해?

A.
필요할 수 있다. 빌드 도구의 base path와 React Router basename 설정을 함께 검토해야 한다.

---

## 7.3 Cache Rules

### [개념]

브라우저 캐시는 정적 파일을 저장해 재방문 시 빠르게 로드하도록 하는 기능이다.

---

### [핵심]

운영 캐시 전략:

- hash가 있는 JS/CSS는 장기 캐시 가능
- `index.html`은 짧은 캐시 권장
- 새 배포 후 이전 JS 파일 참조 문제 주의
- Service Worker 사용 시 캐시 무효화 주의

---

### [실무]

권장:

```text
index.html → no-cache 또는 짧은 cache
assets/*.hash.js → long cache
assets/*.hash.css → long cache
```

문제 상황:

```text
배포했는데 사용자 화면이 예전 버전
새 코드 반영 안 됨
JS chunk load error 발생
```

해결:

```text
Hard Reload
Cache-Control 확인
index.html 캐시 정책 수정
Service Worker 제거 또는 업데이트
CDN invalidation 수행
```

---

### [FAQ]

Q. 배포했는데 예전 화면이 계속 보여?

A.
브라우저 캐시, CDN 캐시, Service Worker 캐시 문제일 수 있다.

Q. index.html은 왜 장기 캐시하면 안 좋아?

A.
index.html이 예전 hash 파일을 참조하면 새 배포 파일과 mismatch가 발생할 수 있다.

---

# 8. SPA Routing Rules

## 8.1 SPA Routing Concept

### [개념]

SPA는 브라우저에서 JavaScript가 라우팅을 처리하는 애플리케이션이다.

React Router를 사용하는 경우 서버는 실제 `/login`, `/mypage`, `/detail/1` 파일을 갖고 있지 않다.

---

### [핵심]

SPA 라우팅 핵심:

```text
Browser Request /login
→ Server는 /login 파일을 찾음
→ 파일 없음
→ 404 발생 가능
```

해결:

```text
모든 프론트엔드 라우트 요청
→ index.html 반환
→ React Router가 화면 결정
```

---

### [Flow]

정상 SPA fallback:

```text
User Refresh /festival/10
→ Server receives /festival/10
→ Server returns index.html
→ React App loads
→ React Router renders FestivalDetail
```

---

### [FAQ]

Q. React에서 새로고침하면 404가 나는 이유는?

A.
서버가 `/detail/1` 같은 프론트엔드 라우트를 실제 파일 경로로 찾기 때문이다. fallback 설정이 필요하다.

Q. 개발 서버에서는 새로고침이 되는데 운영에서 안 되는 이유는?

A.
개발 서버는 SPA fallback을 기본 지원하지만 운영 서버에는 직접 설정해야 하는 경우가 많다.

---

## 8.2 Nginx SPA Fallback

### [개념]

Nginx에서 React SPA를 제공할 때는 존재하지 않는 경로를 `index.html`로 fallback해야 한다.

---

### [예제]

Nginx SPA fallback 예:

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

---

### [핵심]

중요 설정:

```nginx
try_files $uri $uri/ /index.html;
```

의미:

```text
요청 파일이 있으면 제공
→ 디렉토리가 있으면 제공
→ 없으면 index.html 반환
```

---

### [실무]

Nginx + API Proxy 예:

```nginx
server {
  listen 80;
  server_name example.com;

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

주의:

- `/api` 요청을 index.html로 보내면 안 됨
- API location이 SPA fallback보다 우선되어야 함
- 정적 asset 경로가 정상인지 확인

---

### [FAQ]

Q. Nginx에서 React 새로고침 404는 어떻게 해결해?

A.
`location /`에 `try_files $uri $uri/ /index.html;` 설정을 추가한다.

Q. API 요청도 index.html이 반환돼?

A.
Nginx location 설정이 잘못되면 그럴 수 있다. `/api` proxy location을 별도로 분리해야 한다.

---

## 8.3 Spring Boot SPA Fallback

### [개념]

Spring Boot에 React 빌드 파일을 포함해 배포할 때도 SPA fallback 설정이 필요할 수 있다.

---

### [핵심]

통합 배포 구조:

```text
React Build Output
→ Spring Boot static directory
→ Spring Boot serves index.html
→ React Router handles route
```

---

### [예제]

Spring Boot fallback controller 예:

```java
@Controller
public class SpaController {

  @RequestMapping(value = {
      "/",
      "/{path:[^\\.]*}",
      "/**/{path:[^\\.]*}"
  })
  public String forward() {
    return "forward:/index.html";
  }
}
```

---

### [주의]

API 경로와 충돌 금지:

```text
/api/**
/auth/**
/users/**
/festivals/**
```

위와 같은 백엔드 API 경로는 SPA fallback 대상에서 제외되어야 한다.

---

### [실무]

Spring Boot 통합 배포 검토 항목:

```md
- [ ] React build 결과물이 static 경로에 복사되었는가?
- [ ] index.html이 제공되는가?
- [ ] 정적 JS/CSS 경로가 정상인가?
- [ ] React Router 새로고침이 가능한가?
- [ ] API 경로가 fallback에 먹히지 않는가?
- [ ] Security 설정에서 static resource 허용 여부가 맞는가?
```

---

### [FAQ]

Q. Spring Boot에 React를 넣었는데 새로고침하면 메인으로 가?

A.
fallback이 모든 경로를 index.html로 보내고 React Router가 현재 URL을 제대로 처리해야 한다. 라우터 설정과 fallback 충돌을 확인한다.

Q. Spring Boot fallback 때문에 API가 안 불려?

A.
가능하다. API 경로가 fallback controller에 잡히지 않도록 RequestMapping과 Security 설정을 분리해야 한다.

Q. React build 폴더 전체를 static에 넣으면 돼?

A.
CRA는 build 안의 내용을, Vite는 dist 안의 내용을 static 리소스 경로에 맞게 복사해야 한다.

---

## 8.4 Router Basename Rules

### [개념]

Router basename은 React 앱이 루트(`/`)가 아닌 하위 경로에서 동작할 때 사용하는 기본 경로다.

예:

```text
https://example.com/my-app/
```

---

### [예제]

React Router basename 예:

```jsx
import { BrowserRouter } from "react-router-dom";

function App() {
  return (
    <BrowserRouter basename="/my-app">
      <Routes />
    </BrowserRouter>
  );
}
```

---

### [핵심]

하위 경로 배포 시 함께 확인:

- Vite `base`
- CRA `homepage`
- React Router `basename`
- Nginx root / alias
- Spring Boot context path

---

### [FAQ]

Q. `/my-app` 경로에 배포했는데 라우팅이 깨져?

A.
빌드 도구 base path와 React Router basename이 맞지 않을 가능성이 있다.

Q. 루트 도메인에 배포하면 basename이 필요해?

A.
대부분 필요 없다. 하위 경로 배포 시에만 설정한다.

---

# 9. Spring Boot Integrated Deployment Rules

## 9.1 React + Spring Boot 통합 배포

### [개념]

React + Spring Boot 통합 배포는 프론트엔드 빌드 결과물을 Spring Boot 애플리케이션 내부 정적 리소스로 포함하는 방식이다.

---

### [핵심]

장점:

- 서버 하나로 배포 가능
- CORS 문제가 줄어듦
- 학원 프로젝트 / 소규모 프로젝트에서 단순
- 프론트엔드와 백엔드 도메인 동일
- 운영 환경 구성 단순

단점:

- 프론트엔드만 독립 배포 어려움
- 백엔드 재배포 없이 프론트만 수정하기 어려움
- CDN 최적화가 제한될 수 있음
- 빌드 파이프라인이 결합됨

---

### [Flow]

```text
Frontend npm run build
→ build or dist 생성
→ Spring Boot resources/static에 복사
→ ./gradlew build
→ JAR 생성
→ Server 실행
→ index.html 제공
```

---

### [실무]

적합한 상황:

```text
학원 프로젝트
소규모 서비스
프론트엔드 / 백엔드 같은 서버 운영
CORS 설정 최소화 필요
빠른 발표 / 데모 배포
```

부적합한 상황:

```text
프론트엔드와 백엔드 독립 배포 필요
대규모 트래픽
CDN 최적화 필요
여러 프론트엔드 앱 운영
배포 주기가 서로 다름
```

---

### [FAQ]

Q. 학원 프로젝트에서는 통합 배포가 괜찮아?

A.
괜찮다. 발표와 데모 목적에서는 Spring Boot에 React 빌드 파일을 넣는 통합 배포가 단순하고 관리하기 쉽다.

Q. 실무에서도 통합 배포를 써?

A.
소규모 서비스에서는 쓸 수 있다. 규모가 커지면 프론트엔드와 백엔드를 분리 배포하는 경우가 많다.

---

## 9.2 Static Resource Path

### [개념]

Spring Boot는 기본적으로 `src/main/resources/static` 아래의 정적 파일을 제공할 수 있다.

---

### [핵심]

일반 구조:

```text
backend/
└─ src/main/resources/static/
   ├─ index.html
   ├─ assets/
   └─ favicon.ico
```

CRA 복사:

```text
frontend/build/* → backend/src/main/resources/static/
```

Vite 복사:

```text
frontend/dist/* → backend/src/main/resources/static/
```

---

### [실무]

주의:

- `build` 폴더 자체를 static 안에 넣지 말고 내부 파일을 복사해야 하는 경우가 많음
- `index.html`이 static root에 있어야 함
- assets 경로가 index.html 기준으로 맞아야 함
- 기존 static 파일과 충돌 주의
- API Controller 경로와 static fallback 충돌 주의

---

### [FAQ]

Q. React build 폴더를 static 안에 통째로 넣었는데 화면이 안 떠?

A.
`static/build/index.html` 구조가 되어 서버 root에서 index.html을 못 찾을 수 있다. build 내부 파일을 static root로 복사해야 한다.

Q. Spring Boot에서 index.html은 어디에 있어야 해?

A.
일반적으로 `src/main/resources/static/index.html` 위치에 있어야 루트 요청에서 제공된다.

---

## 9.3 API Path Collision

### [개념]

API Path Collision은 프론트엔드 라우트와 백엔드 API 경로가 충돌하는 문제다.

---

### [핵심]

위험한 구조:

```text
Frontend Route: /festival/detail/1
Backend API: /festival/detail/1
```

권장 구조:

```text
Frontend Route: /festival/detail/1
Backend API: /api/festivals/1
```

---

### [실무]

권장 API prefix:

```text
/api
/api/auth
/api/users
/api/festivals
/api/reviews
/api/notifications
```

장점:

- SPA fallback과 API 구분 쉬움
- Nginx proxy 설정 쉬움
- Security 설정 쉬움
- Review Agent가 경로 충돌 검토 가능

---

### [FAQ]

Q. 백엔드 API와 React 라우트가 같은 경로여도 돼?

A.
권장하지 않는다. `/api` prefix로 백엔드 API를 분리하는 것이 안전하다.

Q. React 새로고침 문제 해결하려다 API가 index.html을 반환해?

A.
fallback 설정이 API 경로까지 잡고 있을 가능성이 높다. API prefix와 fallback 제외 처리가 필요하다.

---

# 10. Nginx Deployment Rules

## 10.1 Nginx Static Deployment

### [개념]

Nginx는 React 빌드 결과물을 정적 파일로 제공하는 대표적인 웹 서버다.

---

### [핵심]

기본 구조:

```text
React Build
→ dist or build
→ /usr/share/nginx/html
→ Nginx Serve
```

---

### [예제]

기본 Nginx 설정:

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

---

### [실무]

Nginx 검토 항목:

```md
- [ ] root 경로가 빌드 결과물 위치와 맞는가?
- [ ] index.html이 root에 있는가?
- [ ] React Router fallback이 있는가?
- [ ] API proxy가 필요한가?
- [ ] 정적 asset cache 설정이 적절한가?
- [ ] HTTPS 설정이 필요한가?
- [ ] gzip / brotli 압축이 필요한가?
```

---

### [FAQ]

Q. Nginx는 왜 프론트엔드 배포에 많이 써?

A.
정적 파일 제공이 빠르고 reverse proxy, cache, gzip, HTTPS 설정에 적합하기 때문이다.

Q. Nginx root와 alias 차이도 알아야 해?

A.
기초 배포에서는 root 중심으로 충분하지만 하위 경로 배포나 복잡한 location에서는 alias 차이를 주의해야 한다.

---

## 10.2 Nginx API Proxy

### [개념]

Nginx API Proxy는 같은 도메인에서 `/api` 요청을 백엔드 서버로 전달하는 방식이다.

---

### [Flow]

```text
Browser → https://example.com/api/festivals
Nginx → http://backend:8080/api/festivals
Backend → Response
Nginx → Browser
```

---

### [예제]

```nginx
location /api/ {
  proxy_pass http://backend:8080/api/;
  proxy_set_header Host $host;
  proxy_set_header X-Real-IP $remote_addr;
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  proxy_set_header X-Forwarded-Proto $scheme;
}
```

---

### [실무]

장점:

- 프론트엔드와 API가 같은 Origin처럼 동작
- CORS 복잡도 감소
- 프론트엔드 baseURL을 `/api`로 단순화 가능
- HTTPS termination을 Nginx에서 처리 가능

주의:

- proxy_pass 경로 slash 처리 주의
- WebSocket 사용 시 upgrade header 필요
- API location이 SPA fallback보다 우선 필요
- timeout 설정 필요 가능

---

### [FAQ]

Q. baseURL을 `/api`로 쓰려면 Nginx 설정이 필요해?

A.
운영에서 `/api` 요청을 백엔드로 전달하는 proxy 설정이 필요하다.

Q. Nginx proxy를 쓰면 CORS가 필요 없어?

A.
같은 Origin으로 보이게 구성하면 CORS 문제가 줄어든다. 단, 구조에 따라 백엔드 CORS가 여전히 필요할 수 있다.

---

# 11. Docker Deployment Rules

## 11.1 Frontend Docker Build

### [개념]

Frontend Docker 배포는 Node 환경에서 빌드한 뒤 Nginx 이미지로 정적 파일을 제공하는 방식이 일반적이다.

---

### [핵심]

권장 구조:

```text
Build Stage: Node
→ npm install
→ npm run build
Serve Stage: Nginx
→ build output copy
→ Nginx serve
```

---

### [예제]

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

---

### [실무]

Docker 배포 검토 항목:

```md
- [ ] multi-stage build를 사용하는가?
- [ ] `npm ci` 또는 lock file 기반 설치를 사용하는가?
- [ ] output directory가 정확한가?
- [ ] Nginx fallback 설정이 포함되었는가?
- [ ] 환경 변수 주입 시점이 빌드 시점인지 런타임인지 확인했는가?
- [ ] container port와 host port가 맞는가?
```

---

### [FAQ]

Q. Docker에서 React 앱을 node 서버로 실행해야 해?

A.
일반 SPA는 빌드 후 Nginx로 정적 파일을 제공하는 방식이 일반적이다.

Q. Docker 이미지에 node_modules가 들어가도 돼?

A.
최종 Nginx 이미지는 정적 파일만 포함하는 것이 좋다. multi-stage build를 사용하면 이미지가 작아진다.

Q. Docker에서 env를 바꿨는데 React 앱 값이 안 바뀌어?

A.
일반 React 환경 변수는 빌드 시점에 주입된다. 컨테이너 실행 시점 env 변경만으로는 반영되지 않을 수 있다.

---

## 11.2 Docker Compose Frontend Backend

### [개념]

Docker Compose는 프론트엔드, 백엔드, DB를 함께 실행하기 위한 로컬 또는 배포용 구성 방식이다.

---

### [예제]

예시 구조:

```yaml
services:
  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend

  backend:
    build: ./backend
    ports:
      - "8080:8080"
```

---

### [핵심]

주의:

- 브라우저는 Docker 내부 service name을 직접 알 수 없음
- 프론트엔드 코드의 API URL에 `http://backend:8080`을 넣으면 브라우저에서 실패 가능
- Nginx proxy 또는 외부 접근 가능한 도메인 사용 필요
- 서버 내부 통신과 브라우저 통신 구분 필요

---

### [실무]

잘못된 예:

```env
VITE_API_BASE_URL=http://backend:8080
```

브라우저에서 `backend`라는 host를 찾지 못할 수 있다.

권장 예:

```env
VITE_API_BASE_URL=/api
```

그리고 Nginx가 `/api`를 `http://backend:8080`으로 proxy한다.

---

### [FAQ]

Q. Docker Compose에서 frontend가 backend service name으로 API 호출하면 돼?

A.
브라우저에서 실행되는 프론트엔드 코드는 사용자의 브라우저 기준으로 요청한다. service name은 컨테이너 내부 네트워크에서만 유효하다.

Q. Compose에서는 API URL을 어떻게 잡는 게 좋아?

A.
Nginx proxy를 두고 프론트엔드에서는 `/api`를 사용하는 방식이 단순하다.

---

# 12. Platform Deployment Rules

## 12.1 Vercel Deployment

### [개념]

Vercel은 프론트엔드 정적 사이트와 프레임워크 앱 배포에 특화된 플랫폼이다.

---

### [핵심]

React SPA 배포 기준:

- Build Command: `npm run build`
- Output Directory: Vite `dist`, CRA `build`
- Environment Variables: Vercel Project Settings에서 설정
- SPA fallback rewrite 필요 가능
- API URL 운영 값 확인 필요

---

### [예제]

Vercel SPA rewrite 예:

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

---

### [실무]

Vercel 검토 항목:

```md
- [ ] Framework preset이 맞는가?
- [ ] build command가 맞는가?
- [ ] output directory가 맞는가?
- [ ] 환경 변수가 dashboard에 설정되었는가?
- [ ] 운영 API URL이 맞는가?
- [ ] React Router 새로고침이 되는가?
```

---

### [FAQ]

Q. Vercel에 React SPA를 배포할 수 있어?

A.
가능하다. 빌드 명령과 output directory를 맞추고 SPA rewrite를 확인해야 한다.

Q. Vercel 환경 변수는 .env 파일을 올려야 해?

A.
보통 Vercel dashboard의 Environment Variables에서 설정한다.

---

## 12.2 Netlify Deployment

### [개념]

Netlify는 정적 프론트엔드 배포에 많이 사용하는 플랫폼이다.

---

### [핵심]

Netlify 기준:

- Build Command: `npm run build`
- Publish Directory: Vite `dist`, CRA `build`
- Environment Variables 설정 필요
- SPA redirect 설정 필요

---

### [예제]

`public/_redirects` 예:

```text
/* /index.html 200
```

또는 `netlify.toml`:

```toml
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

---

### [실무]

Netlify 검토 항목:

```md
- [ ] publish directory가 맞는가?
- [ ] `_redirects` 또는 `netlify.toml`이 있는가?
- [ ] 환경 변수가 설정되었는가?
- [ ] API URL이 운영 값인가?
- [ ] 배포 후 새로고침 404가 없는가?
```

---

### [FAQ]

Q. Netlify에서 React 새로고침 404는 어떻게 해결해?

A.
`/* /index.html 200` redirect 설정을 추가한다.

Q. Netlify publish directory는 뭘로 해야 해?

A.
Vite는 `dist`, CRA는 `build`가 일반적이다.

---

## 12.3 AWS S3 and CloudFront

### [개념]

AWS S3는 정적 파일 저장과 웹 사이트 호스팅에 사용할 수 있고, CloudFront는 CDN으로 전 세계 사용자에게 빠르게 제공할 수 있다.

---

### [핵심]

기본 구조:

```text
React Build
→ S3 Bucket Upload
→ CloudFront Distribution
→ User Access
```

---

### [실무]

검토 항목:

```md
- [ ] S3에 index.html과 assets가 업로드되었는가?
- [ ] CloudFront origin이 S3를 바라보는가?
- [ ] SPA fallback을 위한 error response가 설정되었는가?
- [ ] index.html cache가 너무 길지 않은가?
- [ ] 배포 후 invalidation이 필요한가?
- [ ] HTTPS 인증서가 연결되었는가?
```

SPA fallback:

```text
403 or 404 → /index.html → 200
```

---

### [FAQ]

Q. S3에 React를 올렸는데 새로고침하면 404야?

A.
SPA fallback 설정이 필요하다. CloudFront custom error response로 index.html을 반환하도록 설정할 수 있다.

Q. CloudFront invalidation은 언제 해?

A.
새 배포 후 캐시된 index.html이나 asset 참조 문제를 해결해야 할 때 수행한다.

Q. S3만 써도 돼?

A.
가능하지만 운영에서는 HTTPS, CDN, 캐시 제어를 위해 CloudFront와 함께 쓰는 경우가 많다.

---

## 12.4 GitHub Pages

### [개념]

GitHub Pages는 정적 사이트를 GitHub 저장소에서 직접 호스팅하는 방식이다.

---

### [핵심]

주의:

- 하위 경로 배포가 많음
- base path 설정 필요
- React Router fallback 제약 있음
- BrowserRouter보다 HashRouter가 단순할 수 있음
- 민감 정보 저장 금지

---

### [실무]

하위 경로 예:

```text
https://username.github.io/repository-name/
```

필요 설정:

```text
Vite base: /repository-name/
React Router basename: /repository-name
```

---

### [FAQ]

Q. GitHub Pages에서 React Router 새로고침이 안 돼?

A.
GitHub Pages는 서버 rewrite 설정이 제한적이라 HashRouter를 쓰거나 별도 fallback 우회가 필요할 수 있다.

Q. GitHub Pages는 실무 운영에 적합해?

A.
문서, 포트폴리오, 데모에는 적합하지만 복잡한 운영 서비스에는 제한이 있다.

---

# 13. CI/CD Rules

## 13.1 CI/CD Basic Flow

### [개념]

CI/CD는 코드 변경 후 테스트, 빌드, 배포를 자동화하는 흐름이다.

---

### [Flow]

기본 프론트엔드 CI/CD:

```text
Push or Pull Request
→ Install Dependencies
→ Lint
→ Test
→ Build
→ Deploy
→ Smoke Test
```

---

### [핵심]

권장 단계:

```md
- [ ] checkout
- [ ] setup node
- [ ] install dependencies
- [ ] lint
- [ ] test
- [ ] build
- [ ] deploy
```

---

### [실무]

최소 검증:

```bash
npm ci
npm run lint
npm test
npm run build
```

프로젝트에 따라 test가 없을 수 있으나 Review Agent는 최소 build 성공 여부를 필수로 본다.

---

### [FAQ]

Q. CI/CD에서 build만 성공하면 충분해?

A.
최소 조건은 될 수 있지만 lint, test, type check를 함께 수행하는 것이 좋다.

Q. 배포 전에 꼭 테스트를 돌려야 해?

A.
권장된다. 테스트가 없더라도 최소한 lint와 build는 수행해야 한다.

---

## 13.2 GitHub Actions Basic

### [개념]

GitHub Actions는 GitHub 저장소에서 CI/CD workflow를 실행하는 자동화 도구다.

---

### [예제]

기초 workflow 예:

```yaml
name: Frontend CI

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm

      - name: Install
        run: npm ci

      - name: Build
        run: npm run build
```

---

### [실무]

GitHub Actions 검토 항목:

```md
- [ ] Node.js version이 프로젝트와 맞는가?
- [ ] package manager가 맞는가?
- [ ] working-directory가 맞는가?
- [ ] env 설정이 필요한가?
- [ ] secret은 GitHub Secrets에 저장했는가?
- [ ] build output 경로가 맞는가?
```

---

### [FAQ]

Q. GitHub Actions에서 npm ci가 실패해?

A.
package-lock.json과 package.json 불일치, Node 버전 차이, private package 권한 문제를 확인한다.

Q. frontend 폴더가 하위에 있으면 어떻게 해?

A.
workflow에서 `working-directory: ./frontend`를 설정해야 한다.

---

# 14. Source Map Rules

## 14.1 Source Map

### [개념]

Source Map은 압축된 운영 JS 코드와 원본 소스 코드를 연결해 디버깅을 가능하게 하는 파일이다.

---

### [핵심]

장점:

- 운영 오류 위치 추적 가능
- 에러 모니터링 도구와 연동 가능
- 디버깅 편의성 증가

주의:

- 원본 코드 노출 가능
- 내부 로직 노출 가능
- 운영 공개 여부 결정 필요

---

### [실무]

운영 Source Map 전략:

```text
Small project or demo → source map 허용 가능
Public production → source map 비공개 또는 에러 모니터링 도구에만 업로드
Sensitive code → source map 공개 금지
```

---

### [FAQ]

Q. 운영에서 source map을 켜도 돼?

A.
가능하지만 원본 코드가 노출될 수 있으므로 서비스 성격에 따라 신중하게 결정해야 한다.

Q. source map이 없으면 운영 에러 추적이 어려워?

A.
어려워질 수 있다. 대신 에러 모니터링 도구에 비공개 업로드하는 전략을 사용할 수 있다.

---

# 15. Deployment Verification Rules

## 15.1 Deploy Verification

### [개념]

배포 후 검증은 운영 환경에서 실제 사용자가 겪을 문제를 사전에 확인하는 과정이다.

---

### [핵심]

배포 후 필수 확인:

```md
- [ ] 메인 페이지 접속 가능
- [ ] 새로고침 시 404 없음
- [ ] 직접 URL 접근 가능
- [ ] JS / CSS asset 404 없음
- [ ] Console error 없음
- [ ] API 요청 URL 정상
- [ ] API 응답 정상
- [ ] 로그인 / 로그아웃 정상
- [ ] 인증 토큰 저장 / 전송 정상
- [ ] 이미지 / 폰트 로드 정상
- [ ] 모바일 화면 정상
- [ ] HTTPS 적용
- [ ] Mixed Content 없음
- [ ] 캐시 문제 없음
```

---

### [Flow]

배포 후 점검 Flow:

```text
Open Production URL
→ Console Check
→ Network Check
→ Refresh Route Check
→ API Request Check
→ Auth Flow Check
→ Mobile View Check
→ Cache Check
```

---

### [실무]

브라우저 개발자 도구 기준:

```text
Console → JS error 확인
Network → API URL / status / response 확인
Application → localStorage / sessionStorage / cookies 확인
Elements → asset path / DOM 확인
Lighthouse → 성능 / 접근성 기초 확인
```

---

### [FAQ]

Q. 배포 후 제일 먼저 확인할 것은?

A.
Console error와 Network 요청 URL, status code를 확인한다.

Q. 화면이 흰색이면 뭘 봐야 해?

A.
Console JS error, JS asset 404, base path, 환경 변수, 라우터 설정을 확인한다.

Q. 배포 후 로그인만 안 돼?

A.
API URL, CORS, Cookie SameSite/Secure, Authorization header, HTTPS 여부를 확인한다.

---

# 16. Troubleshooting Rules

## 16.1 Build Error Troubleshooting

### [개념]

Build Error는 운영 배포용 파일 생성 과정에서 발생하는 오류다.

---

### [핵심]

대표 원인:

- TypeScript error
- ESLint error
- dependency 설치 실패
- Node.js version mismatch
- 환경 변수 누락
- import 경로 오류
- 파일명 대소문자 문제
- memory 부족
- package-lock 불일치

---

### [Flow]

```text
Build Log 확인
→ 첫 번째 Error 확인
→ Node Version 확인
→ Dependency 재설치
→ Type Error 수정
→ Import Path 확인
→ Env 확인
→ Rebuild
```

---

### [FAQ]

Q. 로컬 Windows에서는 되는데 Linux 배포에서 import 에러가 나?

A.
파일명 대소문자 문제일 가능성이 있다. Linux는 대소문자를 구분한다.

Q. npm install은 되는데 npm ci가 실패해?

A.
package.json과 package-lock.json이 일치하지 않을 수 있다. lock file을 갱신해야 한다.

Q. build 중 메모리 부족이 나?

A.
의존성 크기, 번들 크기, Node memory option, 빌드 서버 사양을 확인한다.

---

## 16.2 White Screen Troubleshooting

### [개념]

White Screen은 배포 후 화면이 흰색으로만 보이는 문제다.

---

### [핵심]

대표 원인:

- JS bundle 로드 실패
- asset path 404
- JavaScript runtime error
- 환경 변수 undefined
- Router basename 오류
- API 초기화 실패
- Suspense fallback 누락
- React root mount 실패

---

### [Flow]

```text
Console Error 확인
→ Network JS/CSS 404 확인
→ index.html asset path 확인
→ Environment Variable 확인
→ Router basename 확인
→ Runtime Error 수정
```

---

### [실무]

우선 확인:

```md
- [ ] `main.js` 또는 `index.js`가 200으로 로드되는가?
- [ ] CSS 파일이 로드되는가?
- [ ] Console에 Cannot read properties of undefined가 있는가?
- [ ] API Base URL이 undefined인가?
- [ ] 배포 경로와 base path가 일치하는가?
```

---

### [FAQ]

Q. 배포했는데 흰 화면만 나와?

A.
대부분 JS 로드 실패, base path 오류, runtime error, 환경 변수 누락 중 하나다.

Q. Network에서 JS가 404면 어떻게 해?

A.
빌드 도구 base 설정, 서버 root 설정, 배포 경로를 확인한다.

---

## 16.3 Refresh 404 Troubleshooting

### [개념]

Refresh 404는 SPA 라우트에서 새로고침하거나 직접 URL 접근 시 서버가 404를 반환하는 문제다.

---

### [핵심]

원인:

- 서버가 SPA fallback을 지원하지 않음
- Nginx `try_files` 누락
- Netlify redirect 누락
- Vercel rewrite 누락
- Spring Boot fallback 누락
- API 경로와 SPA 경로 충돌

---

### [Flow]

```text
Direct URL Access Test
→ Server 404 확인
→ Hosting Platform 확인
→ Fallback 설정 추가
→ API 경로 제외 확인
→ Re-test
```

---

### [FAQ]

Q. React에서 링크 이동은 되는데 새로고침하면 404야?

A.
Client-side routing은 되지만 서버 fallback이 없기 때문이다.

Q. HashRouter를 쓰면 해결돼?

A.
해결될 수 있지만 URL에 `#`가 붙는다. 가능하면 서버 fallback 설정을 우선 고려한다.

---

## 16.4 API Call Failed After Deploy

### [개념]

배포 후 API 호출 실패는 프론트엔드 배포에서 가장 흔한 문제 중 하나다.

---

### [핵심]

대표 원인:

- API URL이 localhost
- 운영 백엔드 서버 미실행
- CORS 미설정
- HTTPS / HTTP mixed content
- Authorization header 누락
- Cookie 설정 오류
- 프록시 경로 오류
- 서버 응답 500

---

### [Flow]

```text
Network Request URL 확인
→ Status Code 확인
→ Response Body 확인
→ CORS Error 확인
→ Auth Header 확인
→ Cookie 확인
→ Backend Log 확인
```

---

### [FAQ]

Q. 배포 후 API가 404야?

A.
baseURL, proxy path, 백엔드 API prefix, 서버 라우팅을 확인한다.

Q. 배포 후 API가 CORS 에러야?

A.
백엔드 CORS 허용 Origin에 프론트엔드 운영 도메인을 추가해야 한다.

Q. 배포 후 401이 나와?

A.
Authorization header, token 저장 위치, refresh flow, cookie 설정을 확인한다.

---

## 16.5 Static Asset 404

### [개념]

Static Asset 404는 JS, CSS, 이미지, 폰트 파일을 서버가 찾지 못하는 문제다.

---

### [핵심]

대표 원인:

- 배포 경로 오류
- base path 오류
- 파일 복사 누락
- 서버 root 오류
- 하위 경로 배포 설정 누락
- 대소문자 문제

---

### [Flow]

```text
Network 404 File 확인
→ index.html 참조 경로 확인
→ Server Root 확인
→ Build Output 확인
→ Base Path 설정 확인
→ Redeploy
```

---

### [FAQ]

Q. index.html은 뜨는데 CSS가 안 먹어?

A.
CSS asset 파일이 404인지 확인하고 base path와 서버 root를 점검한다.

Q. 이미지가 배포 후 깨져?

A.
public asset 경로, import 경로, 대소문자, 배포 누락을 확인한다.

---

# 17. Security Rules

## 17.1 Frontend Deploy Security

### [개념]

프론트엔드 배포 보안은 브라우저에 노출되는 코드와 설정을 전제로 관리해야 한다.

---

### [핵심]

금지:

- Secret Key 프론트엔드 저장
- 관리자 비밀번호 하드코딩
- JWT Secret 노출
- Toss Secret Key 노출
- OpenAI API Key 노출
- AWS Secret Key 노출
- `.env` 파일 무분별한 공개
- Source Map 공개로 민감 로직 노출

---

### [실무]

배포 보안 체크:

```md
- [ ] `.env`에 secret이 없는가?
- [ ] public key는 도메인 제한이 되어 있는가?
- [ ] API Secret은 백엔드에서만 사용하는가?
- [ ] 운영 로그에 token이 노출되지 않는가?
- [ ] localStorage 사용 시 XSS 위험을 고려했는가?
- [ ] HTTPS를 사용하는가?
- [ ] CSP 적용을 고려했는가?
```

---

### [FAQ]

Q. Kakao JavaScript Key는 프론트엔드에 있어도 돼?

A.
브라우저에서 사용해야 하는 public key는 가능하지만 반드시 허용 도메인 제한을 설정해야 한다.

Q. 결제 Secret Key를 프론트엔드에 넣어도 돼?

A.
안 된다. 결제 Secret Key는 반드시 백엔드에서만 사용해야 한다.

Q. JWT를 localStorage에 저장해도 돼?

A.
가능은 하지만 XSS 위험이 있다. 프로젝트 보안 요구사항에 따라 httpOnly cookie 방식도 검토해야 한다.

---

## 17.2 Cookie Deploy Rules

### [개념]

운영 배포에서 쿠키 인증을 사용할 경우 SameSite, Secure, Domain 설정이 중요하다.

---

### [핵심]

운영 쿠키 체크:

```text
SameSite=None 사용 시 Secure 필요
HTTPS 환경 필요
프론트엔드와 백엔드 도메인 관계 확인
withCredentials 필요
CORS credentials 허용 필요
```

---

### [실무]

문제 상황:

```text
로컬 로그인 OK
운영 로그인 실패
응답 Set-Cookie 있음
하지만 브라우저에 쿠키 저장 안 됨
```

확인:

```text
Application → Cookies
Network → Response Headers → Set-Cookie
SameSite / Secure / Domain / Path 확인
```

---

### [FAQ]

Q. 운영에서 쿠키가 저장되지 않아?

A.
SameSite, Secure, Domain, HTTPS, CORS credentials 설정을 확인한다.

Q. SameSite=None이면 뭐가 필요해?

A.
대부분 Secure가 필요하고 HTTPS 환경이어야 한다.

---

# 18. Performance Build Rules

## 18.1 Bundle Size

### [개념]

Bundle Size는 브라우저가 다운로드하고 실행해야 하는 JavaScript / CSS 파일 크기다.

---

### [핵심]

번들이 커지는 원인:

- 큰 라이브러리 전체 import
- 사용하지 않는 코드 포함
- 이미지 최적화 누락
- code splitting 미적용
- 중복 dependency
- source map 공개
- polyfill 과다

---

### [실무]

최적화 방향:

```md
- [ ] 필요한 함수만 import
- [ ] lazy loading 적용
- [ ] route-based code splitting
- [ ] image compression
- [ ] tree shaking 가능한 import 사용
- [ ] bundle analyzer 사용
```

---

### [예제]

Route lazy loading 예:

```jsx
import { lazy, Suspense } from "react";

const DetailPage = lazy(() => import("./pages/DetailPage"));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <DetailPage />
    </Suspense>
  );
}
```

---

### [FAQ]

Q. 빌드 파일이 너무 크면 뭐가 문제야?

A.
초기 로딩이 느려지고 모바일 환경에서 사용자 경험이 나빠질 수 있다.

Q. lazy loading은 언제 써?

A.
초기 화면에 필요하지 않은 페이지나 무거운 컴포넌트에 적용한다.

---

## 18.2 Compression and CDN

### [개념]

Compression은 JS/CSS/Text 파일을 gzip 또는 brotli로 압축해 전송하는 방식이고, CDN은 사용자와 가까운 서버에서 정적 파일을 제공하는 방식이다.

---

### [핵심]

성능 개선:

- gzip
- brotli
- CDN
- Cache-Control
- HTTP/2 or HTTP/3
- 이미지 최적화
- font preload

---

### [실무]

Nginx gzip 예:

```nginx
gzip on;
gzip_types text/plain text/css application/javascript application/json image/svg+xml;
```

주의:

- 이미지 파일은 이미 압축된 경우가 많음
- CDN 캐시 무효화 전략 필요
- index.html 캐시와 assets 캐시를 분리

---

### [FAQ]

Q. gzip을 켜면 무조건 좋아?

A.
대부분 text 기반 리소스에는 좋지만, 이미 압축된 파일에는 효과가 제한적이다.

Q. CDN은 언제 필요해?

A.
사용자가 많거나 지역이 분산되어 있거나 정적 파일 로딩 성능이 중요할 때 필요하다.

---

# 19. Deployment Strategy Comparison

## 19.1 Deployment Options

### [Comparison]

| 방식                  | 장점                      | 단점             | 적합 상황             |
| --------------------- | ------------------------- | ---------------- | --------------------- |
| Spring Boot 통합 배포 | 단순함, CORS 감소         | 독립 배포 어려움 | 학원 프로젝트, 소규모 |
| Nginx 정적 배포       | 빠름, proxy 가능          | 서버 설정 필요   | 일반 운영             |
| Vercel                | 간편함, 자동 배포         | 백엔드 별도 필요 | 프론트 단독           |
| Netlify               | 간편함, SPA redirect 쉬움 | 백엔드 별도 필요 | 정적 사이트           |
| S3 + CloudFront       | 확장성, CDN               | AWS 설정 필요    | 운영 서비스           |
| Docker + Nginx        | 환경 일관성               | 이미지 빌드 필요 | 서버 배포             |
| GitHub Pages          | 무료, 간단                | 라우팅 제약      | 포트폴리오, 데모      |

---

### [핵심]

선택 기준:

```text
학원 발표 / 빠른 데모 → Spring Boot 통합 배포
프론트엔드 단독 배포 → Vercel / Netlify
운영 정적 사이트 → S3 + CloudFront
서버 직접 운영 → Nginx
컨테이너 환경 → Docker + Nginx
```

---

### [FAQ]

Q. 학원 프로젝트는 어떤 배포가 좋아?

A.
빠른 시연과 단순 운영이 목적이면 Spring Boot 통합 배포가 쉽고, 프론트 단독 시연이면 Vercel / Netlify도 좋다.

Q. 실무에서는 어떤 방식이 많아?

A.
서비스 규모와 인프라에 따라 다르지만 정적 프론트엔드는 CDN 또는 Nginx 기반으로 분리 배포하는 경우가 많다.

---

# 20. PM Agent Rules

## 20.1 PM Agent Build Deploy Planning

### [개념]

PM Agent는 배포 목표, 환경, 일정, 책임 범위를 명확히 정의해야 한다.

---

### [핵심]

PM Agent 확인 질문:

```md
- [ ] 배포 대상은 데모인가 운영인가?
- [ ] 프론트엔드와 백엔드를 통합 배포하는가?
- [ ] 프론트엔드 단독 배포인가?
- [ ] API 서버 주소는 무엇인가?
- [ ] HTTPS가 필요한가?
- [ ] 로그인 / 결제가 포함되는가?
- [ ] 도메인이 있는가?
- [ ] 배포 후 테스트 범위는 무엇인가?
```

---

### [실무]

PM Agent 산출물:

```text
Deployment Target
→ Build Tool
→ Hosting Method
→ API Base URL
→ Environment Variables
→ Route Fallback
→ Test Checklist
→ Release Note
```

---

### [FAQ]

Q. PM Agent는 배포에서 뭘 판단해야 해?

A.
배포 방식, 환경 변수, API 주소, 도메인, HTTPS, 일정, 검증 범위를 정리해야 한다.

Q. 발표용 배포와 운영 배포는 다르게 봐야 해?

A.
다르다. 발표용은 단순성과 안정적 시연이 우선이고 운영 배포는 보안, 성능, 모니터링, 확장성을 더 봐야 한다.

---

# 21. Frontend Agent Rules

## 21.1 Frontend Agent Build Deploy Implementation

### [개념]

Frontend Agent는 빌드 가능한 코드, 환경 변수 분리, 운영 API 연동, 라우팅 fallback 대응을 고려해 구현해야 한다.

---

### [핵심]

Frontend Agent 필수 작업:

```md
- [ ] build script 유지
- [ ] API Base URL 환경 변수화
- [ ] localhost 하드코딩 제거
- [ ] public key와 secret 구분
- [ ] Router basename 필요 여부 확인
- [ ] lazy loading fallback 제공
- [ ] asset 경로 검토
- [ ] 배포 후 Network 확인 기준 제공
```

---

### [실무]

API 설정 예:

```js
const baseURL = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8080";

export const api = axios.create({
  baseURL,
  timeout: 10000,
});
```

운영에서는 fallback으로 localhost가 들어가지 않도록 Review Agent가 검토해야 한다.

---

### [FAQ]

Q. Frontend Agent가 배포를 고려해 코드를 짜려면 뭐가 중요해?

A.
환경 변수, API URL, 라우팅, asset 경로, 인증 저장 방식, build 성공 여부가 중요하다.

Q. 코드에 localhost가 남아 있으면 안 돼?

A.
운영 빌드에 남아 있으면 안 된다. 개발용 기본값과 운영 환경 설정을 분리해야 한다.

---

# 22. Review Agent Rules

## 22.1 Build Deploy Review

### [개념]

Review Agent는 배포 전후로 장애를 만들 수 있는 설정과 코드를 검토해야 한다.

---

### [Checklist]

배포 전 Review Checklist:

```md
- [ ] `npm run build`가 성공하는가?
- [ ] TypeScript error가 없는가?
- [ ] ESLint error가 없는가?
- [ ] 운영 API URL이 설정되어 있는가?
- [ ] localhost 하드코딩이 없는가?
- [ ] secret key가 프론트엔드 코드에 없는가?
- [ ] React Router fallback 설정이 준비되어 있는가?
- [ ] 하위 경로 배포 시 base / basename이 맞는가?
- [ ] 인증 토큰 처리 방식이 운영 환경과 맞는가?
- [ ] HTTPS / CORS / Cookie 설정을 확인했는가?
- [ ] 빌드 결과물 경로가 배포 설정과 맞는가?
- [ ] 배포 후 테스트 시나리오가 있는가?
```

배포 후 Review Checklist:

```md
- [ ] 메인 페이지 정상
- [ ] 직접 URL 접근 정상
- [ ] 새로고침 정상
- [ ] API 요청 정상
- [ ] 로그인 정상
- [ ] 로그아웃 정상
- [ ] 이미지 로드 정상
- [ ] 모바일 화면 정상
- [ ] Console error 없음
- [ ] Network 404 / 401 / 403 / 500 확인
```

---

### [실무]

Review Agent 판단 Flow:

```text
Build Result
→ Env Check
→ API URL Check
→ Router Check
→ Static Asset Check
→ Auth Check
→ Browser Verification
→ Final Deploy Approval
```

---

### [FAQ]

Q. Review Agent가 배포 전 가장 먼저 봐야 할 것은?

A.
`npm run build` 성공 여부와 운영 환경 변수, localhost 하드코딩 여부를 먼저 확인한다.

Q. 배포 후 검증에서 Console error가 있으면 실패야?

A.
대부분 실패로 본다. 특히 runtime error, asset 404, API error는 반드시 수정해야 한다.

---

# 23. Common Mistakes

## 23.1 Frontend Build Deploy Common Mistakes

### [개념]

Frontend Build & Deploy에서 자주 발생하는 실수를 문서에 명확히 포함해야 한다.

---

### [핵심]

자주 발생하는 실수:

- `npm start`를 운영 서버처럼 사용
- `npm run build` 결과물을 서버에 올리지 않음
- API URL이 localhost로 남아 있음
- Vite에서 `REACT_APP_` 환경 변수 사용
- CRA에서 `VITE_` 환경 변수 사용
- `.env` 수정 후 서버 재시작 안 함
- secret key를 프론트엔드 env에 저장
- React Router fallback 누락
- Nginx `try_files` 누락
- Spring Boot fallback이 API 경로와 충돌
- build 폴더 자체를 static 안에 잘못 복사
- asset base path 설정 누락
- HTTPS 페이지에서 HTTP API 호출
- CORS 운영 도메인 누락
- Cookie SameSite / Secure 설정 누락
- Docker 내부 service name을 브라우저 API URL로 사용
- index.html 장기 캐시
- CloudFront invalidation 누락
- Linux 배포에서 파일명 대소문자 문제 발생
- Source Map으로 원본 코드 노출

---

### [Troubleshooting]

실수별 판단:

```text
흰 화면
→ Console / JS 404 / base path / env 확인

새로고침 404
→ SPA fallback 확인

API localhost 호출
→ 환경 변수 / build 시점 확인

로그인 실패
→ CORS / Cookie / Authorization / HTTPS 확인

배포 반영 안 됨
→ Browser cache / CDN cache / Service Worker 확인
```

---

### [FAQ]

Q. 배포 초보가 가장 많이 하는 실수는?

A.
개발 서버와 운영 빌드를 혼동하고, API URL을 localhost로 둔 채 배포하는 경우가 많다.

Q. React 새로고침 404는 코드 문제가 아니야?

A.
대부분 React 코드 문제가 아니라 서버 fallback 설정 문제다.

Q. Docker에서 backend라는 주소로 API 요청하면 왜 안 돼?

A.
브라우저는 Docker 내부 네트워크를 모른다. backend service name은 컨테이너 간 통신에서만 유효하다.

---

# 24. Document Quality Rules

## 24.1 RAG Quality Checklist

### [개념]

Frontend Build & Deploy 문서는 RAG Retrieval에 적합하도록 Chunk 단위 의미가 독립적이어야 한다.

---

### [Checklist]

문서 품질 체크:

```md
- [ ] [개념], [핵심], [실무], [FAQ]가 포함되었는가?
- [ ] Build와 Deploy 차이를 설명했는가?
- [ ] Vite / CRA 차이를 설명했는가?
- [ ] 환경 변수 prefix를 설명했는가?
- [ ] API Base URL 운영 분리를 설명했는가?
- [ ] SPA fallback을 설명했는가?
- [ ] Nginx fallback 예제를 포함했는가?
- [ ] Spring Boot 통합 배포를 포함했는가?
- [ ] Docker + Nginx 배포를 포함했는가?
- [ ] Vercel / Netlify / S3 배포를 포함했는가?
- [ ] CORS / HTTPS / Cookie 문제를 포함했는가?
- [ ] 배포 후 검증 Checklist가 있는가?
- [ ] Troubleshooting Flow가 있는가?
- [ ] FAQ가 실제 사용자 질문 형태인가?
- [ ] Retrieval Queries가 마지막에 있는가?
```

---

### [실무]

문서 작성 우선순위:

```text
실제 문제 해결성
→ Retrieval Query Matching
→ 짧은 예제
→ Agent 판단 기준
→ Checklist
→ FAQ
```

---

### [FAQ]

Q. Build Deploy 문서에서 가장 중요한 품질 기준은?

A.
Agent가 배포 문제를 빠르게 분류하고 해결 Flow를 제시할 수 있어야 한다.

Q. 예제 코드는 길어야 해?

A.
아니다. RAG 문서에서는 짧고 직접적인 예제가 더 좋다.

---

# 25. Final Goal

## 25.1 Domain Final Goal

### [개념]

Frontend Build & Deploy Domain Rules의 최종 목적은 Frontend Agent / Review Agent / PM Agent가 프론트엔드 배포 구조를 정확히 판단하고, 운영 장애를 사전에 예방하며, 배포 후 문제를 빠르게 해결하도록 지원하는 것이다.

---

### [핵심]

최종 수행 가능 작업:

- 빌드 결과물 구조 판단
- Vite / CRA 환경 변수 구분
- 운영 API URL 설정 검토
- React Router 새로고침 404 해결
- Nginx 정적 배포 설정 제안
- Spring Boot 통합 배포 구조 판단
- Docker + Nginx 배포 구조 제안
- Vercel / Netlify / S3 배포 방식 선택
- CORS / HTTPS / Cookie 문제 분석
- 배포 후 Console / Network 검증
- 배포 전 Review Checklist 수행
- 배포 오류 Troubleshooting 수행

---

### [실무]

최종 Agent Flow:

```text
User Deploy Request
→ Project Type Identify
→ Build Tool Identify
→ Build Command Check
→ Env Variable Check
→ API URL Check
→ Hosting Strategy Select
→ SPA Fallback Configure
→ Security Check
→ Deploy Verification Checklist
→ Troubleshooting Guide
```

---

### [FAQ]

Q. 이 문서의 최종 목적은 뭐야?

A.
프론트엔드 빌드와 배포 과정에서 Agent가 정확히 판단하고 실무 문제를 해결하도록 만드는 것이다.

Q. 이 문서 다음에 이어질 문서는 뭐야?

A.
Frontend Code Review Domain Rules, Styling Architecture Domain Rules, Design System Domain Rules로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Build & Deploy 문서는 왜 필요해?

A.
Frontend Agent / Review Agent / PM Agent가 빌드, 배포, 환경 변수, API URL, SPA 라우팅 문제를 정확히 판단하기 위해 필요하다.

Q. 프론트엔드 빌드란 뭐야?

A.
React / JavaScript / CSS 소스 코드를 브라우저가 실행할 수 있는 HTML, CSS, JS 정적 파일로 변환하는 과정이다.

Q. npm run build는 서버를 실행하는 명령이야?

A.
아니다. 일반 React / Vite / CRA에서는 정적 파일 결과물을 생성하는 명령이다.

Q. React build 결과물은 어디에 생겨?

A.
CRA는 보통 `build`, Vite는 보통 `dist` 폴더에 생성된다.

Q. Development Server와 Production Build 차이는?

A.
Development Server는 개발 편의용이고 Production Build는 실제 배포용으로 최적화된 정적 파일 결과물이다.

Q. 개발 서버에서는 되는데 배포하면 안 되는 이유는?

A.
API URL, 환경 변수, SPA fallback, CORS, HTTPS, Cookie, cache 설정이 운영 환경과 다르기 때문이다.

Q. Vite build output은 어디야?

A.
기본적으로 `dist` 폴더다.

Q. CRA build output은 어디야?

A.
기본적으로 `build` 폴더다.

Q. Vite 환경 변수 prefix는 뭐야?

A.
`VITE_` prefix를 사용한다.

Q. CRA 환경 변수 prefix는 뭐야?

A.
`REACT_APP_` prefix를 사용한다.

Q. Vite에서 환경 변수는 어떻게 읽어?

A.
`import.meta.env.VITE_API_BASE_URL`처럼 읽는다.

Q. CRA에서 환경 변수는 어떻게 읽어?

A.
`process.env.REACT_APP_API_BASE_URL`처럼 읽는다.

Q. .env 수정했는데 값이 안 바뀌어?

A.
개발 서버를 재시작하거나 운영에서는 다시 빌드해야 한다.

Q. 프론트엔드 .env에 Secret Key를 넣어도 돼?

A.
안 된다. 프론트엔드 환경 변수는 브라우저에 노출될 수 있다.

Q. API Secret Key는 어디에 둬야 해?

A.
백엔드 서버 환경 변수나 Secret Manager에 보관해야 한다.

Q. 운영 API URL은 어떻게 관리해?

A.
환경 변수 또는 runtime config로 분리하고, 운영 빌드 시 운영 API URL이 들어가도록 설정한다.

Q. 배포했는데 API가 localhost로 호출돼?

A.
운영 환경 변수 설정이 누락되었거나 빌드 시점에 개발용 API URL이 들어간 것이다.

Q. API baseURL을 `/api`로 써도 돼?

A.
가능하다. Nginx나 백엔드가 `/api` 요청을 실제 백엔드 서버로 proxy하는 구조라면 적합하다.

Q. CORS는 프론트엔드에서 해결해?

A.
대부분 백엔드에서 허용 Origin, Header, Method, Credentials를 설정해야 해결된다.

Q. withCredentials는 언제 필요해?

A.
쿠키 기반 인증을 사용할 때 필요하다.

Q. Authorization Header 방식에도 withCredentials가 필요해?

A.
보통 JWT를 Authorization Header로 보내는 방식에서는 필요하지 않다.

Q. HTTPS 페이지에서 HTTP API를 호출하면 왜 안 돼?

A.
브라우저가 Mixed Content로 차단할 수 있다.

Q. WebSocket도 HTTPS 배포에서 바뀌어야 해?

A.
HTTPS 페이지에서는 `ws://` 대신 `wss://`를 사용해야 한다.

Q. React 새로고침 404는 왜 발생해?

A.
서버가 `/login`, `/detail/1` 같은 프론트엔드 라우트를 실제 파일 경로로 찾기 때문이다.

Q. React Router 새로고침 404는 어떻게 해결해?

A.
서버에서 존재하지 않는 프론트엔드 경로를 `index.html`로 fallback하도록 설정한다.

Q. Nginx에서 SPA fallback은 어떻게 설정해?

A.
`try_files $uri $uri/ /index.html;` 설정을 사용한다.

Q. Netlify에서 React 새로고침 404는 어떻게 해결해?

A.
`/* /index.html 200` redirect 설정을 추가한다.

Q. Vercel에서 SPA rewrite는 왜 필요해?

A.
직접 URL 접근이나 새로고침 시 React Router가 처리할 수 있도록 index.html로 보내기 위해 필요하다.

Q. Spring Boot에 React를 통합 배포할 수 있어?

A.
가능하다. React build 또는 dist 내부 파일을 Spring Boot static resource 경로에 복사하면 된다.

Q. Spring Boot static 경로는 어디야?

A.
일반적으로 `src/main/resources/static`이다.

Q. React build 폴더 자체를 static 안에 넣으면 돼?

A.
대부분 build 폴더 내부 파일이 static root에 위치해야 한다. `static/build/index.html` 구조가 되면 루트에서 못 찾을 수 있다.

Q. Spring Boot fallback 때문에 API가 안 불려?

A.
가능하다. API 경로가 fallback controller에 잡히지 않도록 `/api` prefix와 fallback 제외 처리가 필요하다.

Q. 프론트엔드 라우트와 API 경로가 같아도 돼?

A.
권장하지 않는다. 백엔드 API는 `/api` prefix로 분리하는 것이 안전하다.

Q. Nginx로 React를 배포하는 기본 구조는?

A.
빌드 결과물을 `/usr/share/nginx/html`에 복사하고 Nginx가 정적 파일로 제공한다.

Q. Nginx에서 API proxy는 왜 써?

A.
같은 도메인에서 `/api` 요청을 백엔드로 전달해 CORS 복잡도를 줄이고 배포 구조를 단순화하기 위해 사용한다.

Q. Docker로 React를 배포할 때 Node 서버가 필요해?

A.
일반 SPA는 Node로 실행하지 않고 build 후 Nginx로 정적 파일을 제공하는 방식이 일반적이다.

Q. Docker multi-stage build는 왜 써?

A.
Node로 빌드하고 최종 이미지는 Nginx와 정적 파일만 포함해 이미지 크기를 줄이기 위해 사용한다.

Q. Docker Compose에서 API URL을 `http://backend:8080`으로 써도 돼?

A.
브라우저는 Docker 내부 service name을 알 수 없으므로 보통 실패한다. Nginx proxy와 `/api` 경로를 사용하는 것이 좋다.

Q. Vercel에 React SPA를 배포할 수 있어?

A.
가능하다. build command, output directory, environment variables, SPA rewrite를 확인해야 한다.

Q. Netlify publish directory는 뭘로 설정해?

A.
Vite는 `dist`, CRA는 `build`가 일반적이다.

Q. S3에 React를 올렸는데 새로고침 404가 나?

A.
SPA fallback 설정이 필요하다. CloudFront custom error response로 index.html을 반환하도록 설정할 수 있다.

Q. CloudFront invalidation은 언제 필요해?

A.
새 배포 후 CDN 캐시 때문에 이전 index.html이나 asset이 계속 제공될 때 필요하다.

Q. GitHub Pages에서 React Router가 안 돼?

A.
GitHub Pages는 rewrite 설정이 제한적이라 HashRouter 또는 별도 fallback 우회가 필요할 수 있다.

Q. CI/CD 기본 순서는 뭐야?

A.
Install Dependencies → Lint → Test → Build → Deploy 순서가 기본이다.

Q. GitHub Actions에서 frontend 폴더가 하위에 있으면 어떻게 해?

A.
workflow에 `working-directory: ./frontend`를 설정한다.

Q. npm ci가 실패하는 이유는?

A.
package.json과 package-lock.json이 불일치하거나 Node 버전, private package 권한 문제가 있을 수 있다.

Q. 배포 후 흰 화면이 나와?

A.
JS asset 404, base path 오류, runtime error, 환경 변수 누락, Router basename 오류를 확인한다.

Q. 배포 후 CSS가 안 먹어?

A.
CSS 파일이 404인지, asset path와 서버 root가 맞는지 확인한다.

Q. 배포 후 이미지가 깨져?

A.
public asset 경로, import 경로, 파일명 대소문자, 배포 누락을 확인한다.

Q. 로컬에서는 되는데 Linux 배포에서 import 에러가 나?

A.
파일명 대소문자 문제일 가능성이 있다. Linux는 대소문자를 구분한다.

Q. 배포했는데 이전 화면이 계속 보여?

A.
브라우저 캐시, CDN 캐시, Service Worker 캐시 문제일 수 있다.

Q. index.html은 왜 장기 캐시하면 안 돼?

A.
예전 index.html이 이전 hash 파일을 참조하면 새 배포와 mismatch가 발생할 수 있기 때문이다.

Q. Source Map을 운영에 공개해도 돼?

A.
가능하지만 원본 코드가 노출될 수 있으므로 서비스 성격에 따라 비공개 처리하거나 에러 모니터링 도구에만 업로드한다.

Q. Bundle Size가 크면 뭐가 문제야?

A.
초기 로딩이 느려지고 모바일 사용자 경험이 나빠질 수 있다.

Q. lazy loading은 언제 적용해?

A.
초기 화면에 필요하지 않은 페이지나 무거운 컴포넌트에 적용한다.

Q. gzip은 왜 사용해?

A.
JS, CSS, JSON 같은 text 기반 리소스를 압축해 전송량을 줄이기 위해 사용한다.

Q. 학원 프로젝트 배포는 어떤 방식이 좋아?

A.
빠른 발표와 데모 목적이면 Spring Boot 통합 배포가 단순하고, 프론트 단독 시연이면 Vercel이나 Netlify도 적합하다.

Q. 운영 서비스에서는 어떤 배포가 좋아?

A.
규모와 인프라에 따라 다르지만 정적 프론트엔드는 Nginx, S3 + CloudFront, Vercel 같은 분리 배포가 많이 사용된다.

Q. 배포 전 Review Agent가 확인할 것은?

A.
build 성공, 환경 변수, localhost 하드코딩, secret 노출, SPA fallback, API URL, HTTPS, CORS, Cookie 설정을 확인한다.

Q. 배포 후 Review Agent가 확인할 것은?

A.
메인 접속, 새로고침, 직접 URL 접근, API 요청, 로그인, 이미지 로드, 모바일 화면, Console error, Network status를 확인한다.

Q. PM Agent는 배포에서 무엇을 정리해야 해?

A.
배포 대상, 배포 방식, API URL, 환경 변수, 도메인, HTTPS, 검증 범위, 일정과 책임을 정리해야 한다.

Q. Frontend Agent는 배포를 고려해 무엇을 구현해야 해?

A.
환경 변수 기반 API URL, 라우팅 대응, build 가능한 코드, secret 미노출, asset path 안정성을 고려해야 한다.

Q. Frontend Build Deploy 문서 다음은 뭐야?

A.
Frontend Code Review Domain Rules, Styling Architecture Domain Rules, Design System Domain Rules로 이어지는 것이 좋다.
