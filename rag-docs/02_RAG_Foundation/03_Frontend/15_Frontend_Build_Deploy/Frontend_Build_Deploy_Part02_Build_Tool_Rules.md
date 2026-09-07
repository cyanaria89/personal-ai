# Frontend Build & Deploy Part02 - Build Tool Rules

---

# 1. Build Tool Core

## 1.1 Build Tool Definition

### [개념]

Build Tool은 프론트엔드 소스 코드를 개발 서버에서 실행하거나 운영 배포용 정적 파일로 변환하는 도구다.

대표 Build Tool:

```text
Vite
CRA
Next.js
Vue CLI
Webpack
Rollup
Parcel
```

React SPA 기준 주요 대상:

```text
Vite
CRA
```

---

### [핵심]

Build Tool 핵심 역할:

- Development Server 제공
- JSX / TSX 변환
- TypeScript 변환
- CSS 처리
- JavaScript Bundling
- Asset 처리
- Environment Variable 주입
- Production Build 생성
- File Hash 적용
- Build Output Directory 생성

---

### [실무]

2026 실무 기준으로 신규 React SPA 프로젝트는 Vite 사용 비중이 높다.

기존 학원 / 레거시 / 교육용 프로젝트에서는 CRA도 여전히 사용될 수 있다.

Agent 판단 기준:

```text
package.json scripts 확인
→ dependency 확인
→ config file 확인
→ build command 확인
→ output directory 확인
→ env prefix 확인
→ deployment setting 확인
```

Build Tool 식별 기준:

```text
vite.config.js 존재
→ Vite 가능성 높음

react-scripts dependency 존재
→ CRA 가능성 높음

next dependency 존재
→ Next.js 가능성 높음
```

---

### [FAQ]

Q. Build Tool은 무엇인가?
A. 프론트엔드 소스를 개발 실행하거나 운영 배포용 정적 파일로 변환하는 도구다.

Q. React 프로젝트에서 대표 Build Tool은 무엇인가?
A. Vite와 CRA가 대표적이다.

Q. 신규 React 프로젝트에서는 무엇을 많이 사용하는가?
A. 2026 기준으로는 Vite 사용이 일반적이다.

Q. 기존 프로젝트에서 CRA를 만나도 이상한가?
A. 아니다. 교육용, 레거시, 기존 팀 프로젝트에서는 CRA가 여전히 사용될 수 있다.

---

## 1.2 Build Tool Identification

### [개념]

Build Tool Identification은 프로젝트가 어떤 빌드 도구를 사용하는지 판단하는 과정이다.

---

### [핵심]

식별 대상 파일:

```text
package.json
vite.config.js
vite.config.ts
webpack.config.js
next.config.js
package-lock.json
yarn.lock
pnpm-lock.yaml
```

식별 대상 dependency:

```text
vite
@vitejs/plugin-react
react-scripts
next
webpack
```

---

### [실무]

2026 실무 기준으로 Agent는 사용자의 말만 믿지 않고 프로젝트 파일 기준으로 Build Tool을 판단해야 한다.

Vite 식별 예:

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build"
  },
  "dependencies": {
    "@vitejs/plugin-react": "^latest",
    "vite": "^latest"
  }
}
```

CRA 식별 예:

```json
{
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build"
  },
  "dependencies": {
    "react-scripts": "5.x"
  }
}
```

판단 Flow:

```text
package.json 확인
→ scripts 확인
→ dependency 확인
→ config file 확인
→ output directory 추정
→ env prefix 결정
```

---

### [FAQ]

Q. Build Tool은 어디서 확인하는가?
A. `package.json`의 scripts와 dependencies를 먼저 확인한다.

Q. vite.config.js가 있으면 Vite인가?
A. 대부분 Vite 가능성이 높지만 package.json도 함께 확인해야 한다.

Q. react-scripts가 있으면 무엇인가?
A. 일반적으로 CRA 프로젝트다.

Q. 사용자가 CRA라고 했지만 vite.config.js가 있으면 어떻게 판단하는가?
A. 프로젝트 파일 기준으로 다시 확인한다. scripts와 dependency가 최종 판단 기준이다.

---

# 2. Vite Build Rules

## 2.1 Vite Core

### [개념]

Vite는 빠른 Development Server와 Rollup 기반 Production Build를 제공하는 프론트엔드 Build Tool이다.

---

### [핵심]

Vite 기준:

- Development Command: `npm run dev`
- Build Command: `npm run build`
- Preview Command: `npm run preview`
- Build Output: `dist`
- Environment Prefix: `VITE_`
- Environment Access: `import.meta.env`
- Config File: `vite.config.js` 또는 `vite.config.ts`
- Production Build 내부는 Rollup 기반

---

### [실무]

2026 실무 기준으로 Vite는 React SPA 신규 프로젝트의 기본 선택지에 가깝다.

Vite 기본 scripts 예:

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

Vite Build Flow:

```text
npm run dev
→ local development

npm run build
→ dist 생성

npm run preview
→ dist 결과물을 로컬에서 preview
```

Agent 확인 항목:

```md
- [ ] `vite` dependency 존재
- [ ] `vite.config.js` 또는 `vite.config.ts` 존재
- [ ] `npm run build`가 `vite build`인지 확인
- [ ] output directory가 `dist`인지 확인
- [ ] env prefix가 `VITE_`인지 확인
- [ ] `import.meta.env` 사용 여부 확인
```

---

### [FAQ]

Q. Vite는 무엇인가?
A. 빠른 개발 서버와 Production Build를 제공하는 프론트엔드 Build Tool이다.

Q. Vite의 build output은 어디인가?
A. 기본적으로 `dist` 폴더다.

Q. Vite 개발 명령은 무엇인가?
A. 보통 `npm run dev`다.

Q. Vite 배포 전 preview는 어떻게 하는가?
A. `npm run build` 후 `npm run preview`로 확인한다.

---

## 2.2 Vite Environment Variable Rules

### [개념]

Vite 환경 변수는 클라이언트 코드에서 사용할 경우 `VITE_` prefix를 가져야 한다.

---

### [핵심]

Vite 환경 변수 규칙:

- 클라이언트 노출 변수는 `VITE_`로 시작해야 한다.
- 코드에서는 `import.meta.env`로 접근한다.
- `.env` 수정 후 개발 서버 재시작이 필요하다.
- Production Build에서는 build 시점 값이 들어간다.
- Secret Key를 저장하면 안 된다.

---

### [실무]

Vite `.env` 예:

```env
VITE_API_BASE_URL=http://localhost:8080
VITE_APP_ENV=local
VITE_KAKAO_JS_KEY=public-key
```

사용 예:

```js
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
```

잘못된 예:

```env
REACT_APP_API_BASE_URL=http://localhost:8080
```

```js
const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;
```

Agent 검토 기준:

```text
Vite Project
→ VITE_ prefix 확인
→ import.meta.env 사용 확인
→ REACT_APP_ 혼용 여부 확인
→ secret key 노출 여부 확인
```

---

### [FAQ]

Q. Vite 환경 변수 prefix는 무엇인가?
A. `VITE_`다.

Q. Vite에서 환경 변수는 어떻게 읽는가?
A. `import.meta.env.VITE_API_BASE_URL`처럼 읽는다.

Q. Vite에서 process.env를 사용해도 되는가?
A. 일반적인 클라이언트 코드에서는 `import.meta.env`를 사용해야 한다.

Q. Vite에서 REACT*APP* 변수를 써도 되는가?
A. 일반적으로 안 된다. Vite는 `VITE_` prefix를 사용한다.

---

## 2.3 Vite Config Rules

### [개념]

Vite Config는 Vite 프로젝트의 plugin, base path, build option, dev server proxy 등을 설정하는 파일이다.

대표 파일:

```text
vite.config.js
vite.config.ts
```

---

### [핵심]

Vite Config에서 자주 확인하는 항목:

- `plugins`
- `base`
- `server.proxy`
- `build.outDir`
- `resolve.alias`
- `define`
- `preview`
- `assetsDir`

---

### [실무]

기본 Vite Config 예:

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

Output Directory 변경 예:

```js
export default defineConfig({
  build: {
    outDir: "build",
  },
});
```

Agent 검토 Flow:

```text
vite.config 확인
→ base 설정 확인
→ outDir 변경 여부 확인
→ proxy 설정 확인
→ alias 설정 확인
→ 배포 경로와 일치 여부 확인
```

---

### [FAQ]

Q. Vite에서 base는 무엇인가?
A. 배포 시 정적 asset이 로드될 기본 경로다.

Q. Vite base 설정이 틀리면 어떻게 되는가?
A. JS, CSS, 이미지 asset 404 또는 흰 화면이 발생할 수 있다.

Q. Vite output directory를 바꿀 수 있는가?
A. 가능하다. `build.outDir`로 변경할 수 있다.

Q. Vite proxy는 운영 배포에도 적용되는가?
A. 일반적으로 개발 서버용이다. 운영에서는 Nginx proxy나 백엔드 설정을 별도로 구성해야 한다.

---

## 2.4 Vite Preview Rules

### [개념]

Vite Preview는 Production Build 결과물인 `dist`를 로컬에서 정적 서버로 확인하는 기능이다.

---

### [핵심]

Preview 목적:

- Production Build 결과 확인
- asset path 확인
- runtime error 확인
- 환경 변수 반영 확인
- routing 동작 확인
- 배포 전 흰 화면 여부 확인

---

### [실무]

Vite Preview 명령:

```bash
npm run build
npm run preview
```

검증 항목:

```md
- [ ] 메인 페이지 정상 표시
- [ ] Console error 없음
- [ ] JS / CSS asset 404 없음
- [ ] API 요청 URL 정상
- [ ] 환경 변수 값 정상
- [ ] 라우팅 이동 정상
- [ ] 직접 URL 접근은 hosting fallback 별도 검토
```

주의:

```text
Vite Preview 정상
≠
운영 서버 fallback 정상
```

---

### [FAQ]

Q. Vite Preview는 왜 필요한가?
A. Production Build 결과물을 배포 전에 로컬에서 확인하기 위해 필요하다.

Q. npm run dev가 되면 npm run preview도 볼 필요 없는가?
A. 아니다. dev server와 production build 결과는 다를 수 있다.

Q. Vite Preview가 정상인데 운영에서 새로고침 404가 날 수 있는가?
A. 가능하다. 운영 서버의 SPA fallback 설정은 별도로 필요하다.

---

# 3. CRA Build Rules

## 3.1 CRA Core

### [개념]

CRA(Create React App)는 `react-scripts` 기반 React 프로젝트 생성 및 Build Tool이다.

---

### [핵심]

CRA 기준:

- Development Command: `npm start`
- Build Command: `npm run build`
- Test Command: `npm test`
- Build Output: `build`
- Environment Prefix: `REACT_APP_`
- Environment Access: `process.env.REACT_APP_*`
- Config는 react-scripts 내부에 숨겨져 있음

---

### [실무]

2026 실무 기준으로 CRA는 신규 프로젝트에서는 감소 추세지만 기존 교육용 / 레거시 프로젝트에서는 여전히 사용된다.

CRA 기본 scripts 예:

```json
{
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test"
  }
}
```

CRA Build Flow:

```text
npm start
→ local development

npm run build
→ build 폴더 생성

build 내부 파일
→ static hosting 대상
```

Agent 확인 항목:

```md
- [ ] `react-scripts` dependency 존재
- [ ] `npm start`가 `react-scripts start`인지 확인
- [ ] `npm run build`가 `react-scripts build`인지 확인
- [ ] output directory가 `build`인지 확인
- [ ] env prefix가 `REACT_APP_`인지 확인
- [ ] `process.env.REACT_APP_` 사용 여부 확인
```

---

### [FAQ]

Q. CRA는 무엇인가?
A. `react-scripts` 기반 React 프로젝트 Build Tool이다.

Q. CRA의 build output은 어디인가?
A. 기본적으로 `build` 폴더다.

Q. CRA 개발 명령은 무엇인가?
A. 보통 `npm start`다.

Q. CRA는 신규 프로젝트에도 권장되는가?
A. 2026 기준 신규 프로젝트에서는 Vite 사용이 더 일반적이고 CRA는 기존 프로젝트에서 자주 만난다.

---

## 3.2 CRA Environment Variable Rules

### [개념]

CRA 환경 변수는 클라이언트 코드에서 사용할 경우 `REACT_APP_` prefix를 가져야 한다.

---

### [핵심]

CRA 환경 변수 규칙:

- 클라이언트 노출 변수는 `REACT_APP_`로 시작해야 한다.
- 코드에서는 `process.env.REACT_APP_*`로 접근한다.
- `.env` 수정 후 개발 서버 재시작이 필요하다.
- Production Build에서는 build 시점 값이 들어간다.
- Secret Key를 저장하면 안 된다.

---

### [실무]

CRA `.env` 예:

```env
REACT_APP_API_BASE_URL=http://localhost:8080
REACT_APP_APP_ENV=local
REACT_APP_KAKAO_JS_KEY=public-key
```

사용 예:

```js
const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;
```

잘못된 예:

```env
VITE_API_BASE_URL=http://localhost:8080
```

```js
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
```

Agent 검토 기준:

```text
CRA Project
→ REACT_APP_ prefix 확인
→ process.env.REACT_APP_ 사용 확인
→ VITE_ 혼용 여부 확인
→ secret key 노출 여부 확인
```

---

### [FAQ]

Q. CRA 환경 변수 prefix는 무엇인가?
A. `REACT_APP_`다.

Q. CRA에서 환경 변수는 어떻게 읽는가?
A. `process.env.REACT_APP_API_BASE_URL`처럼 읽는다.

Q. CRA에서 import.meta.env를 사용해도 되는가?
A. 일반적으로 안 된다. CRA에서는 `process.env.REACT_APP_*` 방식을 사용한다.

Q. CRA에서 VITE* 변수를 써도 되는가?
A. 일반적으로 안 된다. CRA는 `REACT_APP*` prefix를 사용한다.

---

## 3.3 CRA Homepage Rules

### [개념]

CRA의 `homepage` 설정은 Build 결과물의 asset 경로와 배포 base path에 영향을 준다.

---

### [핵심]

`homepage`가 필요한 경우:

- GitHub Pages 배포
- 하위 경로 배포
- 루트가 아닌 path에서 앱 제공
- asset path를 특정 base path 기준으로 생성해야 하는 경우

---

### [실무]

루트 배포 예:

```json
{
  "homepage": "."
}
```

또는 설정 생략 가능.

하위 경로 배포 예:

```json
{
  "homepage": "/my-app"
}
```

GitHub Pages 예:

```json
{
  "homepage": "https://username.github.io/repository-name"
}
```

React Router와 함께 확인:

```text
CRA homepage
→ React Router basename
→ 배포 서버 base path
```

---

### [FAQ]

Q. CRA에서 homepage는 무엇인가?
A. Build 결과물의 asset 경로 기준을 정하는 설정이다.

Q. CRA homepage가 틀리면 어떻게 되는가?
A. JS, CSS asset 404 또는 흰 화면이 발생할 수 있다.

Q. 루트 도메인에 배포하면 homepage가 항상 필요한가?
A. 대부분 필요 없지만 배포 구조에 따라 설정할 수 있다.

Q. 하위 경로 배포에서는 무엇을 함께 확인해야 하는가?
A. `homepage`, React Router `basename`, 서버 base path를 함께 확인해야 한다.

---

## 3.4 CRA Static Serve Rules

### [개념]

CRA Build 결과물은 `build` 폴더에 생성되며 정적 서버로 제공해야 한다.

---

### [핵심]

CRA Build 결과 구조:

```text
build/
├ index.html
├ static/
│  ├ js/
│  └ css/
├ favicon.ico
└ manifest.json
```

정적 제공 대상:

```text
build 내부 파일 전체
```

---

### [실무]

정적 서버 preview 예:

```bash
npm run build
npx serve -s build
```

Spring Boot 통합 배포 시:

```text
frontend/build/*
→ backend/src/main/resources/static/
```

주의:

```text
backend/src/main/resources/static/build/index.html
```

위 구조가 되면 루트에서 index.html을 못 찾을 수 있다.

권장:

```text
backend/src/main/resources/static/index.html
backend/src/main/resources/static/static/js
backend/src/main/resources/static/static/css
```

---

### [FAQ]

Q. CRA build 폴더를 그대로 서버에 올리면 되는가?
A. 정적 서버 root 기준에 맞게 build 내부 파일들이 제공되어야 한다.

Q. Spring Boot static에 build 폴더 자체를 넣어도 되는가?
A. 대부분 권장하지 않는다. build 내부 파일이 static root에 위치해야 한다.

Q. CRA build 결과를 파일로 직접 열어도 되는가?
A. 권장하지 않는다. 정적 서버로 제공해서 확인해야 한다.

---

# 4. Vite vs CRA Comparison

## 4.1 Build Tool Comparison

### [개념]

Vite와 CRA는 React 프로젝트를 개발하고 Build하는 도구지만 명령어, output directory, env 규칙이 다르다.

---

### [핵심]

| 항목                 | Vite              | CRA                       |
| -------------------- | ----------------- | ------------------------- |
| 개발 명령            | `npm run dev`     | `npm start`               |
| Build 명령           | `npm run build`   | `npm run build`           |
| Preview              | `npm run preview` | 별도 serve 필요           |
| Output Directory     | `dist`            | `build`                   |
| Env Prefix           | `VITE_`           | `REACT_APP_`              |
| Env Access           | `import.meta.env` | `process.env.REACT_APP_*` |
| Config               | `vite.config.js`  | react-scripts 내부        |
| 신규 프로젝트 적합성 | 높음              | 낮아지는 추세             |
| 기존 교육 프로젝트   | 가능              | 많음                      |

---

### [실무]

Agent 판단 기준:

```text
Vite Project
→ dist 확인
→ VITE_ 확인
→ import.meta.env 확인
→ vite.config 확인

CRA Project
→ build 확인
→ REACT_APP_ 확인
→ process.env 확인
→ react-scripts 확인
```

혼동 위험:

```text
Vite에서 REACT_APP_ 사용
→ env undefined 가능

CRA에서 VITE_ 사용
→ env undefined 가능

Vite dist 대신 build 배포
→ 파일 없음 가능

CRA build 대신 dist 배포
→ 파일 없음 가능
```

---

### [FAQ]

Q. Vite와 CRA의 가장 중요한 차이는 무엇인가?
A. output directory와 환경 변수 규칙이 다르다. Vite는 `dist` / `VITE_`, CRA는 `build` / `REACT_APP_`를 사용한다.

Q. Vite 프로젝트인데 build 폴더가 없으면 문제인가?
A. 아니다. Vite 기본 output은 `dist`다.

Q. CRA 프로젝트인데 dist 폴더가 없으면 문제인가?
A. 아니다. CRA 기본 output은 `build`다.

Q. Vite와 CRA 환경 변수를 섞어도 되는가?
A. 권장하지 않는다. 빌드 도구별 prefix와 접근 방식이 다르다.

---

## 4.2 Migration Awareness

### [개념]

Migration Awareness는 CRA에서 Vite로 전환하거나 Build Tool을 변경할 때 필요한 차이를 인지하는 것이다.

---

### [핵심]

CRA → Vite 전환 시 주요 변경:

- `react-scripts` 제거
- `vite` 추가
- `@vitejs/plugin-react` 추가
- `public/index.html` 구조 변경 가능
- env prefix 변경
- env access 변경
- output directory 변경
- dev command 변경
- import 경로 문제 확인
- polyfill 차이 확인

---

### [실무]

CRA → Vite 변경 예:

```text
REACT_APP_API_BASE_URL
→ VITE_API_BASE_URL

process.env.REACT_APP_API_BASE_URL
→ import.meta.env.VITE_API_BASE_URL

build/
→ dist/

npm start
→ npm run dev
```

Agent 주의:

```text
Build Tool 변경
→ env 전체 점검 필요
→ CI/CD command 변경 필요
→ deploy output directory 변경 필요
→ static hosting path 변경 필요
```

---

### [FAQ]

Q. CRA에서 Vite로 바꾸면 env도 바꿔야 하는가?
A. 바꿔야 한다. `REACT_APP_`에서 `VITE_`로 prefix와 접근 방식을 변경해야 한다.

Q. CRA에서 Vite로 바꾸면 배포 설정도 바뀌는가?
A. 가능성이 높다. output directory가 `build`에서 `dist`로 바뀌기 때문이다.

Q. Migration 후 API가 undefined가 되는 이유는?
A. env prefix 또는 접근 방식이 기존 CRA 방식으로 남아 있을 수 있다.

---

# 5. Package Manager and Lock File

## 5.1 Package Manager Decision

### [개념]

Package Manager는 프로젝트 의존성을 설치하고 Build Script를 실행하는 도구다.

---

### [핵심]

대표 Package Manager:

```text
npm
yarn
pnpm
```

판단 기준:

```text
package-lock.json
→ npm

yarn.lock
→ yarn

pnpm-lock.yaml
→ pnpm
```

---

### [실무]

2026 실무 기준으로 팀 프로젝트에서는 Package Manager를 하나로 통일해야 한다.

명령어 예:

```bash
# npm
npm ci
npm run build

# yarn
yarn install --frozen-lockfile
yarn build

# pnpm
pnpm install --frozen-lockfile
pnpm build
```

Agent 검토 항목:

```md
- [ ] lock file 하나만 사용하는가?
- [ ] package manager가 팀 기준과 일치하는가?
- [ ] CI/CD 명령이 lock file과 일치하는가?
- [ ] package.json scripts와 실행 명령이 일치하는가?
```

---

### [FAQ]

Q. package manager는 어떻게 결정하는가?
A. lock file 기준으로 판단한다.

Q. npm과 yarn을 섞어 써도 되는가?
A. 권장하지 않는다. 의존성 버전 차이와 lock file 충돌이 생길 수 있다.

Q. 팀 프로젝트에서 package manager 통일이 중요한가?
A. 중요하다. 개발자마다 설치 결과가 달라지는 문제를 줄일 수 있다.

---

## 5.2 Lock File Rules

### [개념]

Lock File은 의존성의 정확한 버전을 고정해 재현 가능한 Build를 보장하는 파일이다.

---

### [핵심]

Lock File 역할:

- dependency version 고정
- install 결과 재현
- CI/CD build 안정화
- 팀원 간 환경 차이 감소
- 배포 결과 예측 가능성 증가

---

### [실무]

권장:

```text
package-lock.json
yarn.lock
pnpm-lock.yaml
```

중 하나만 사용한다.

금지 또는 비권장:

```text
package-lock.json + yarn.lock 동시 사용
package manager 변경 후 lock file 미정리
CI에서 lock file과 다른 package manager 사용
```

Agent 판단 Flow:

```text
lock file 확인
→ package manager 결정
→ install command 결정
→ CI command 확인
→ 중복 lock file 제거 권장
```

---

### [FAQ]

Q. Lock File은 Git에 올려야 하는가?
A. 일반적으로 올려야 한다. 재현 가능한 Build를 위해 필요하다.

Q. package-lock.json과 yarn.lock이 같이 있으면 어떻게 해야 하는가?
A. 팀에서 사용할 package manager를 정하고 하나만 남기는 것이 좋다.

Q. Lock File이 없으면 어떤 문제가 있는가?
A. 의존성 버전이 달라져 개발자나 CI 환경마다 Build 결과가 달라질 수 있다.

---

# 6. Build Tool Config Risk

## 6.1 Base Path Risk

### [개념]

Base Path는 배포 경로 기준으로 JS, CSS, 이미지 asset을 어디서 불러올지 결정하는 설정이다.

---

### [핵심]

Base Path 관련 설정:

```text
Vite base
CRA homepage
React Router basename
Nginx root / alias
Spring Boot context path
GitHub Pages repository path
```

위험 상황:

```text
루트가 아닌 하위 경로 배포
→ base path 설정 필요

base path 불일치
→ JS / CSS asset 404

Router basename 불일치
→ 라우팅 실패
```

---

### [실무]

Vite 하위 경로 예:

```js
export default defineConfig({
  base: "/my-app/",
});
```

CRA 하위 경로 예:

```json
{
  "homepage": "/my-app"
}
```

React Router basename 예:

```jsx
<BrowserRouter basename="/my-app">
  <App />
</BrowserRouter>
```

Agent 검토 Flow:

```text
배포 URL 확인
→ root 배포인지 하위 경로 배포인지 확인
→ Build Tool base 설정 확인
→ Router basename 확인
→ asset 404 여부 확인
```

---

### [FAQ]

Q. Base Path가 틀리면 어떤 문제가 생기는가?
A. JS, CSS, 이미지 asset 404 또는 흰 화면이 발생할 수 있다.

Q. 루트 도메인에 배포하면 base path가 필요한가?
A. 대부분 기본값 `/`로 충분하다.

Q. 하위 경로 배포에서는 무엇을 함께 맞춰야 하는가?
A. Build Tool base path, Router basename, 서버 경로를 함께 맞춰야 한다.

---

## 6.2 Dev Proxy Risk

### [개념]

Dev Proxy는 개발 서버에서 API 요청을 백엔드로 우회시키는 설정이다.

---

### [핵심]

Dev Proxy 특징:

- 개발 서버 전용인 경우가 많다.
- 운영 Build 결과물에는 적용되지 않는다.
- 운영에서는 Nginx Proxy, Backend CORS, API Gateway 설정이 별도로 필요하다.
- 개발에서 API가 되는데 배포 후 실패하는 원인이 될 수 있다.

---

### [실무]

Vite dev proxy 예:

```js
export default defineConfig({
  server: {
    proxy: {
      "/api": "http://localhost:8080",
    },
  },
});
```

CRA package proxy 예:

```json
{
  "proxy": "http://localhost:8080"
}
```

주의:

```text
dev proxy 정상
≠
production proxy 정상
```

운영 대응:

```text
Nginx location /api/
→ backend proxy

또는

Frontend API URL
→ https://api.example.com
```

---

### [FAQ]

Q. 개발에서 proxy가 되면 운영에서도 자동 적용되는가?
A. 아니다. Dev Proxy는 보통 개발 서버 전용이다.

Q. 배포 후 API가 안 되는 이유가 proxy 때문일 수 있는가?
A. 가능하다. 운영 서버에 proxy 설정이 없으면 `/api` 요청이 실패할 수 있다.

Q. 운영에서는 proxy를 어디서 설정하는가?
A. Nginx, Backend, API Gateway, Hosting Platform rewrite 등에서 설정한다.

---

# 7. Build Tool Troubleshooting

## 7.1 Wrong Build Tool Assumption

### [개념]

Wrong Build Tool Assumption은 프로젝트 빌드 도구를 잘못 판단해 명령, env, output directory를 틀리게 적용하는 문제다.

---

### [핵심]

대표 실수:

- Vite 프로젝트에 CRA env 적용
- CRA 프로젝트에 Vite env 적용
- Vite output을 build로 찾음
- CRA output을 dist로 찾음
- `npm start`와 `npm run dev` 혼동
- `process.env`와 `import.meta.env` 혼동
- dev proxy를 production proxy로 착각

---

### [실무]

Troubleshooting Flow:

```text
package.json 확인
→ scripts 확인
→ dependency 확인
→ config file 확인
→ env prefix 확인
→ output directory 확인
→ build 재실행
```

오류 예:

```text
API Base URL undefined
→ env prefix / access 방식 확인

build folder 없음
→ Vite 프로젝트인지 확인

dist folder 없음
→ CRA 프로젝트인지 확인

dev에서는 API OK, build 후 API fail
→ dev proxy 의존 여부 확인
```

---

### [FAQ]

Q. API URL이 undefined인 이유는?
A. 빌드 도구에 맞지 않는 env prefix나 접근 방식을 사용했을 수 있다.

Q. build 폴더가 없으면 Build 실패인가?
A. Vite 프로젝트라면 정상이다. Vite는 기본 output이 `dist`다.

Q. dist 폴더가 없으면 Build 실패인가?
A. CRA 프로젝트라면 정상이다. CRA는 기본 output이 `build`다.

---

## 7.2 Build Tool Error Checklist

### [개념]

Build Tool Error Checklist는 빌드 도구 관련 장애를 빠르게 분류하기 위한 검토 목록이다.

---

### [핵심]

검토 항목:

```md
- [ ] package.json scripts 확인
- [ ] dependency 확인
- [ ] build tool config 확인
- [ ] output directory 확인
- [ ] env prefix 확인
- [ ] env access 방식 확인
- [ ] base path 확인
- [ ] dev proxy 의존 여부 확인
- [ ] CI/CD command 확인
- [ ] deployment output path 확인
```

---

### [실무]

Agent 판단 Flow:

```text
프로젝트 유형 판단
→ Build Tool 판단
→ Env 규칙 판단
→ Output Directory 판단
→ Config Risk 판단
→ Build 실행
→ Preview 또는 정적 서버 검증
```

Build Tool별 핵심 확인:

```text
Vite
→ vite.config
→ dist
→ VITE_
→ import.meta.env

CRA
→ react-scripts
→ build
→ REACT_APP_
→ process.env
```

---

### [FAQ]

Q. Build Tool 문제는 무엇부터 확인해야 하는가?
A. `package.json`의 scripts와 dependencies를 먼저 확인한다.

Q. env 문제가 의심되면 무엇을 확인하는가?
A. 빌드 도구별 prefix와 접근 방식을 확인한다.

Q. asset 404가 발생하면 무엇을 확인하는가?
A. base path, homepage, output directory, 서버 root를 확인한다.

---

# 8. Agent Decision Rules

## 8.1 PM Agent Rules

### [개념]

PM Agent는 Build Tool에 따라 배포 전략, 명령어, output directory, 환경 변수 규칙을 정리해야 한다.

---

### [핵심]

PM Agent 확인 항목:

- Build Tool
- Package Manager
- Build Command
- Dev Command
- Preview Command
- Output Directory
- Env Prefix
- Deployment Target
- Base Path 필요 여부
- Dev Proxy 사용 여부

---

### [실무]

PM Agent 산출물 예:

```text
Build Tool: Vite
Package Manager: yarn
Dev Command: yarn dev
Build Command: yarn build
Output Directory: dist
Env Prefix: VITE_
Deploy Target: Spring Boot static or Vercel
Risk: SPA fallback, API URL, base path
```

PM Agent 판단 Flow:

```text
프로젝트 파일 확인
→ Build Tool 확정
→ 명령어 확정
→ output directory 확정
→ env 규칙 확정
→ 배포 전략과 연결
```

---

### [FAQ]

Q. PM Agent는 Build Tool에서 무엇을 판단해야 하는가?
A. 빌드 도구, 명령어, 결과 폴더, env 규칙, 배포 방식과 위험 요소를 정리해야 한다.

Q. PM Agent가 Build Tool을 잘못 판단하면 어떤 문제가 생기는가?
A. env undefined, output directory 오류, 배포 파일 누락, CI/CD 실패가 발생할 수 있다.

---

## 8.2 Frontend Agent Rules

### [개념]

Frontend Agent는 선택된 Build Tool 규칙에 맞춰 프로젝트 코드를 작성하고 설정을 유지해야 한다.

---

### [핵심]

Frontend Agent 필수 기준:

- Vite / CRA 규칙 구분
- env prefix 준수
- env access 방식 준수
- build script 유지
- dev proxy와 production proxy 구분
- base path 필요 여부 반영
- output directory 변경 시 배포 설정과 공유
- localhost 하드코딩 방지

---

### [실무]

Vite 코드 기준:

```js
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
```

CRA 코드 기준:

```js
const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;
```

Frontend Agent 금지:

```text
Vite에서 process.env.REACT_APP_* 사용
CRA에서 import.meta.env.VITE_* 사용
Secret Key를 frontend env에 저장
운영 API URL을 코드에 직접 하드코딩
```

---

### [FAQ]

Q. Frontend Agent가 Vite에서 지켜야 할 env 규칙은?
A. `VITE_` prefix와 `import.meta.env` 접근 방식을 사용해야 한다.

Q. Frontend Agent가 CRA에서 지켜야 할 env 규칙은?
A. `REACT_APP_` prefix와 `process.env.REACT_APP_*` 접근 방식을 사용해야 한다.

Q. Dev Proxy에 의존해 구현해도 되는가?
A. 개발 중에는 가능하지만 운영 배포에서는 별도 proxy 또는 운영 API URL 설정이 필요하다.

---

## 8.3 Review Agent Rules

### [개념]

Review Agent는 Build Tool과 실제 설정이 일치하는지 검토해야 한다.

---

### [핵심]

Review Agent Checklist:

```md
- [ ] Build Tool 식별 완료
- [ ] package manager 일치
- [ ] build command 정상
- [ ] output directory 정상
- [ ] env prefix 정상
- [ ] env access 방식 정상
- [ ] base path 배포 경로와 일치
- [ ] dev proxy 운영 의존 없음
- [ ] secret key 노출 없음
- [ ] localhost 하드코딩 없음
- [ ] CI/CD command 일치
```

---

### [실무]

Review Agent 판단 Flow:

```text
package.json 확인
→ Build Tool 확정
→ config file 확인
→ env 사용 방식 확인
→ build 실행
→ output directory 확인
→ preview 확인
→ 배포 위험 판단
```

승인 기준:

```text
Build Tool 규칙 일치
Env 규칙 일치
Output Directory 정상
Base Path 정상
Secret 미노출
Production Build 성공
```

---

### [FAQ]

Q. Review Agent는 Build Tool에서 무엇을 가장 먼저 보는가?
A. `package.json`의 scripts와 dependencies를 먼저 본다.

Q. Vite 프로젝트에서 REACT*APP* env를 쓰면 승인 가능한가?
A. 일반적으로 승인하면 안 된다. env가 undefined 될 수 있다.

Q. CRA 프로젝트에서 VITE* env를 쓰면 승인 가능한가?
A. 일반적으로 승인하면 안 된다. CRA는 `REACT_APP*` prefix를 사용한다.

---

# 9. Common Mistakes

## 9.1 Build Tool Common Mistakes

### [개념]

Build Tool Common Mistakes는 빌드 도구별 규칙을 혼동해 발생하는 반복 장애다.

---

### [핵심]

자주 발생하는 실수:

- Vite와 CRA 명령어 혼동
- Vite에서 `REACT_APP_` 사용
- CRA에서 `VITE_` 사용
- Vite에서 `process.env` 사용
- CRA에서 `import.meta.env` 사용
- Vite output을 `build`로 배포
- CRA output을 `dist`로 배포
- Dev Proxy를 운영 Proxy로 착각
- base path 설정 누락
- 하위 경로 배포에서 Router basename 누락
- lock file과 package manager 혼용
- CI/CD working-directory 누락
- Build Tool 변경 후 배포 설정 미수정

---

### [실무]

실수별 해결 Flow:

```text
env undefined
→ Build Tool 확인
→ env prefix 확인
→ env access 방식 확인

JS / CSS 404
→ output directory 확인
→ base path 확인
→ server root 확인

API 개발에서는 OK, 배포 후 fail
→ dev proxy 사용 여부 확인
→ production proxy/API URL 확인

CI build fail
→ package manager 확인
→ lock file 확인
→ working-directory 확인
```

---

### [FAQ]

Q. Build Tool 관련 가장 흔한 실수는 무엇인가?
A. Vite와 CRA의 env prefix, output directory, 명령어를 혼동하는 것이다.

Q. Dev Proxy가 있으면 운영 API 설정이 필요 없는가?
A. 아니다. Dev Proxy는 개발 서버용이고 운영에서는 별도 설정이 필요하다.

Q. Build Tool 변경 후 가장 먼저 확인할 것은?
A. env 규칙, output directory, CI/CD command, 배포 경로를 확인해야 한다.

---

# 10. Part02 Quality Checklist

## 10.1 Document Quality

### [개념]

이 문서는 Frontend Build & Deploy Domain의 Part02이며 Build Tool Rules Retrieval에 최적화되어야 한다.

---

### [핵심]

문서 품질 기준:

- Build Tool 식별 기준 포함
- Vite 규칙 포함
- CRA 규칙 포함
- Vite / CRA 비교 포함
- Environment Variable prefix 차이 포함
- Output Directory 차이 포함
- Base Path 위험 포함
- Dev Proxy 위험 포함
- Agent별 판단 기준 포함
- FAQ는 실제 사용자 질문 형태
- Retrieval Queries 포함

---

### [실무]

Part02는 다음 문서와 연결된다.

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

Q. Part02의 핵심 목적은 무엇인가?
A. Vite와 CRA 같은 Build Tool을 Agent가 정확히 식별하고 규칙에 맞게 판단하도록 하는 것이다.

Q. Part02에서 환경 변수를 자세히 다루는가?
A. Build Tool별 prefix와 접근 방식만 다루고, 환경 변수 세부 전략은 Part03에서 다룬다.

Q. Part02에서 배포 서버 설정까지 자세히 다루는가?
A. 아니다. Build Tool이 배포 설정에 미치는 영향만 다루고 서버 설정은 후속 Part에서 분리한다.

---

# Retrieval Queries

### [FAQ]

Q. Build Tool이란 무엇인가?
A. 프론트엔드 소스를 개발 실행하거나 운영 배포용 정적 파일로 변환하는 도구다.

Q. React 프로젝트의 대표 Build Tool은 무엇인가?
A. Vite와 CRA가 대표적이다.

Q. Build Tool은 어디서 확인하는가?
A. `package.json`의 scripts와 dependencies를 먼저 확인한다.

Q. Vite 프로젝트는 어떻게 식별하는가?
A. `vite` dependency, `vite.config.js`, `vite build`, `npm run dev` scripts를 확인한다.

Q. CRA 프로젝트는 어떻게 식별하는가?
A. `react-scripts` dependency, `react-scripts start`, `react-scripts build` scripts를 확인한다.

Q. Vite 개발 명령은 무엇인가?
A. 보통 `npm run dev`다.

Q. CRA 개발 명령은 무엇인가?
A. 보통 `npm start`다.

Q. Vite Build 명령은 무엇인가?
A. 보통 `npm run build`이며 내부적으로 `vite build`를 실행한다.

Q. CRA Build 명령은 무엇인가?
A. 보통 `npm run build`이며 내부적으로 `react-scripts build`를 실행한다.

Q. Vite output directory는 어디인가?
A. 기본적으로 `dist` 폴더다.

Q. CRA output directory는 어디인가?
A. 기본적으로 `build` 폴더다.

Q. Vite 환경 변수 prefix는 무엇인가?
A. `VITE_`다.

Q. CRA 환경 변수 prefix는 무엇인가?
A. `REACT_APP_`다.

Q. Vite 환경 변수는 어떻게 읽는가?
A. `import.meta.env.VITE_API_BASE_URL`처럼 읽는다.

Q. CRA 환경 변수는 어떻게 읽는가?
A. `process.env.REACT_APP_API_BASE_URL`처럼 읽는다.

Q. Vite에서 REACT*APP* 변수를 사용해도 되는가?
A. 일반적으로 안 된다. Vite는 `VITE_` prefix를 사용한다.

Q. CRA에서 VITE* 변수를 사용해도 되는가?
A. 일반적으로 안 된다. CRA는 `REACT_APP*` prefix를 사용한다.

Q. Vite에서 process.env를 사용해도 되는가?
A. 일반적인 클라이언트 코드에서는 `import.meta.env`를 사용해야 한다.

Q. CRA에서 import.meta.env를 사용해도 되는가?
A. 일반적으로 안 된다. CRA에서는 `process.env.REACT_APP_*` 방식을 사용한다.

Q. Vite Preview는 무엇인가?
A. Production Build 결과물인 `dist`를 로컬 정적 서버로 확인하는 기능이다.

Q. Vite Preview 명령은 무엇인가?
A. `npm run build` 후 `npm run preview`를 실행한다.

Q. CRA Build 결과는 어떻게 preview하는가?
A. `npm run build` 후 `npx serve -s build` 같은 정적 서버로 확인할 수 있다.

Q. Vite Config 파일은 무엇인가?
A. `vite.config.js` 또는 `vite.config.ts`다.

Q. Vite base 설정은 무엇인가?
A. 배포 시 정적 asset을 불러올 기본 경로를 설정한다.

Q. CRA homepage 설정은 무엇인가?
A. Build 결과물의 asset 경로 기준을 정하는 설정이다.

Q. Base Path가 틀리면 어떤 문제가 생기는가?
A. JS, CSS, 이미지 asset 404 또는 흰 화면이 발생할 수 있다.

Q. 하위 경로 배포 시 무엇을 확인해야 하는가?
A. Vite `base`, CRA `homepage`, React Router `basename`, 서버 경로를 함께 확인해야 한다.

Q. Dev Proxy는 운영에서도 적용되는가?
A. 아니다. Dev Proxy는 보통 개발 서버 전용이다.

Q. Vite dev proxy는 어디에 설정하는가?
A. `vite.config.js`의 `server.proxy`에 설정한다.

Q. CRA proxy는 어디에 설정하는가?
A. `package.json`의 `proxy` 또는 별도 proxy setup에서 설정할 수 있다.

Q. 개발에서는 API가 되는데 배포 후 안 되는 이유는?
A. Dev Proxy에 의존했지만 운영 proxy나 API URL 설정이 없을 수 있다.

Q. Vite 프로젝트인데 build 폴더가 없으면 문제인가?
A. 아니다. Vite 기본 output은 `dist`다.

Q. CRA 프로젝트인데 dist 폴더가 없으면 문제인가?
A. 아니다. CRA 기본 output은 `build`다.

Q. package manager는 어떻게 판단하는가?
A. `package-lock.json`은 npm, `yarn.lock`은 yarn, `pnpm-lock.yaml`은 pnpm 기준으로 판단한다.

Q. lock file은 왜 필요한가?
A. 의존성 버전을 고정해 재현 가능한 Build를 보장하기 위해 필요하다.

Q. package-lock.json과 yarn.lock을 같이 써도 되는가?
A. 권장하지 않는다. 팀 기준 package manager를 정하고 lock file 하나만 사용하는 것이 좋다.

Q. CRA에서 Vite로 전환하면 무엇을 바꿔야 하는가?
A. env prefix, env access 방식, output directory, scripts, CI/CD command, 배포 경로를 확인해야 한다.

Q. CRA에서 Vite로 전환 후 API URL이 undefined인 이유는?
A. `REACT_APP_` 또는 `process.env` 방식이 남아 있을 가능성이 있다.

Q. Build Tool 문제는 무엇부터 확인하는가?
A. `package.json`의 scripts와 dependencies를 먼저 확인한다.

Q. env undefined 문제는 무엇을 확인하는가?
A. Build Tool별 env prefix와 접근 방식을 확인한다.

Q. JS asset 404 문제는 무엇을 확인하는가?
A. output directory, base path, homepage, server root를 확인한다.

Q. PM Agent는 Build Tool에서 무엇을 정리해야 하는가?
A. Build Tool, package manager, build command, output directory, env prefix, deployment target을 정리해야 한다.

Q. Frontend Agent는 Build Tool에서 무엇을 지켜야 하는가?
A. 빌드 도구별 env 규칙, output directory, base path, dev proxy와 production proxy 구분을 지켜야 한다.

Q. Review Agent는 Build Tool에서 무엇을 확인해야 하는가?
A. Build Tool 식별, env 규칙, output directory, base path, dev proxy 의존 여부, secret 노출 여부를 확인해야 한다.

Q. Part02 다음 문서는 무엇인가?
A. Part03 Environment Variable Rules로 이어지는 것이 적합하다.
