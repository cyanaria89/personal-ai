# Frontend Build & Deploy Part01 - Build Core

---

# 1. Build Core

## 1.1 Build Definition

### [개념]

Build는 프론트엔드 소스 코드를 브라우저가 실행 가능한 정적 파일로 변환하는 과정이다.

Build 대상:

```text
React Source Code
TypeScript / JavaScript
CSS / SCSS
Image / Font / Asset
Environment Variable
```

Build 결과:

```text
HTML
CSS
JavaScript
Image
Font
Static Asset
```

---

### [핵심]

Build 핵심 포인트:

- Build는 서버 실행이 아니다.
- Build는 정적 파일 생성 과정이다.
- React / Vite / CRA 프로젝트는 Build 후 별도 서버가 정적 파일을 제공해야 한다.
- Build 과정에서 JSX / TypeScript / CSS / Asset이 변환된다.
- Production Build는 Development Server보다 최적화 수준이 높다.
- Build 결과물은 배포 대상이다.
- Source Code와 Build Output은 반드시 구분한다.
- Build Output 폴더는 빌드 도구마다 다르다.

---

### [실무]

2026 실무 기준으로 프론트엔드 배포 전 가장 먼저 확인할 것은 Build 성공 여부다.

기본 Flow:

```text
Source Code
→ Install Dependencies
→ Build Command 실행
→ Build Output 생성
→ Static Hosting Server에 배포
→ Browser에서 index.html 로드
→ JS Bundle 실행
→ API 요청 시작
```

Build 결과물 예:

```text
Vite
→ dist/
   ├ index.html
   └ assets/

CRA
→ build/
   ├ index.html
   └ static/
```

Agent 판단 기준:

```text
npm run build 성공 여부
→ output directory 확인
→ index.html 존재 여부
→ JS / CSS asset 존재 여부
→ 환경 변수 반영 여부
→ 배포 서버 경로와 일치 여부
```

---

### [FAQ]

Q. Build는 프론트엔드 서버를 실행하는 것인가?
A. 아니다. Build는 브라우저가 실행할 수 있는 정적 파일을 생성하는 과정이다.

Q. Build 결과물은 무엇인가?
A. HTML, CSS, JavaScript, 이미지, 폰트 같은 정적 파일이다.

Q. Build 결과물만 있으면 배포가 끝인가?
A. 아니다. Build 결과물을 Nginx, Spring Boot static, Vercel, Netlify, S3 같은 서버나 플랫폼에서 제공해야 한다.

Q. Source Code와 Build Output은 왜 구분해야 하는가?
A. 운영 배포 대상은 보통 Source Code가 아니라 Build Output이기 때문이다.

---

## 1.2 Build Process

### [개념]

Build Process는 프론트엔드 소스 코드가 Production 환경에 맞게 변환되는 내부 흐름이다.

---

### [핵심]

Build 과정에서 수행되는 작업:

- JSX 변환
- TypeScript 변환
- JavaScript Bundling
- CSS Bundling
- Minification
- Tree Shaking
- Code Splitting
- Asset Path 처리
- File Hash 생성
- Environment Variable 주입
- Production Mode 최적화

---

### [실무]

2026 실무 기준으로 Build Process는 단순 변환이 아니라 배포 안정성을 결정하는 단계다.

Build 중 확인해야 할 위험 요소:

```text
Type Error
ESLint Error
Import Path Error
Environment Variable Missing
Asset Path Error
Node Version Mismatch
Package Lock Mismatch
Case-sensitive File Name Error
Memory Error
```

Build Process 판단 Flow:

```text
package.json scripts 확인
→ package manager 확인
→ Node.js version 확인
→ dependency install
→ build command 실행
→ build log 확인
→ output directory 확인
→ production asset 확인
```

---

### [FAQ]

Q. Build 과정에서 TypeScript 에러가 나면 배포해도 되는가?
A. 권장하지 않는다. TypeScript 에러는 운영 장애로 이어질 수 있다.

Q. Build 과정에서 환경 변수가 들어가는가?
A. 일반 React SPA에서는 대부분 Build 시점에 환경 변수가 코드에 주입된다.

Q. Build 후 환경 변수를 바꾸면 바로 반영되는가?
A. 일반적으로 아니다. 다시 Build해야 반영된다.

Q. Build가 성공했으면 운영에서도 무조건 정상인가?
A. 아니다. API URL, SPA fallback, CORS, HTTPS, Cookie, Cache 문제는 배포 후 별도로 검증해야 한다.

---

# 2. Build Command

## 2.1 Build Command Rules

### [개념]

Build Command는 프론트엔드 프로젝트를 운영 배포용 파일로 변환하는 명령이다.

대표 명령:

```bash
npm run build
```

---

### [핵심]

Build Command 확인 항목:

- `package.json`의 `scripts`
- `build` script 존재 여부
- 사용 중인 package manager
- Node.js version
- lock file 존재 여부
- build output directory
- 환경 변수 prefix
- TypeScript compile 여부
- ESLint 실패 여부
- CI/CD에서 실행 가능한 명령인지 여부

---

### [실무]

2026 실무 기준으로 Agent는 사용자의 프로젝트에서 먼저 `package.json`을 확인해야 한다.

Vite 예:

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

Build Command 검토 Flow:

```text
package.json 확인
→ scripts.build 확인
→ package manager 확인
→ lock file 확인
→ Node version 확인
→ npm run build 실행
→ 첫 번째 error 기준으로 수정
```

---

### [FAQ]

Q. build 명령어가 없으면 어떻게 해야 하는가?
A. 사용하는 빌드 도구에 맞게 `package.json`의 `scripts`에 build 명령을 추가해야 한다.

Q. npm run build와 npm start는 같은가?
A. 아니다. `npm start`는 보통 개발 서버 실행이고, `npm run build`는 운영 배포용 정적 파일 생성이다.

Q. build script는 어디서 확인하는가?
A. 프로젝트 루트 또는 frontend 폴더의 `package.json`에서 확인한다.

Q. frontend 폴더가 하위에 있으면 어디서 build를 실행하는가?
A. frontend 프로젝트의 `package.json`이 있는 폴더에서 실행해야 한다.

---

## 2.2 Package Manager Rules

### [개념]

Package Manager는 프론트엔드 의존성을 설치하고 script를 실행하는 도구다.

대표 Package Manager:

```text
npm
yarn
pnpm
```

---

### [핵심]

Package Manager 확인 기준:

- `package-lock.json` → npm
- `yarn.lock` → yarn
- `pnpm-lock.yaml` → pnpm
- lock file과 package manager를 혼용하지 않는다.
- CI/CD에서는 lock file 기반 설치를 우선한다.
- 팀 프로젝트에서는 package manager를 통일한다.

---

### [실무]

2026 실무 기준으로 lock file 혼용은 Build 실패의 주요 원인이다.

권장 명령:

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

Agent 판단 Flow:

```text
lock file 확인
→ package manager 결정
→ install 명령 선택
→ build 명령 선택
→ CI/CD command와 일치 여부 확인
```

---

### [FAQ]

Q. npm과 yarn을 섞어 써도 되는가?
A. 권장하지 않는다. lock file 불일치와 의존성 차이로 Build 결과가 달라질 수 있다.

Q. package-lock.json이 있으면 어떤 명령을 쓰는가?
A. 일반적으로 npm을 사용하고 CI에서는 `npm ci`를 사용한다.

Q. yarn.lock이 있으면 npm install을 해도 되는가?
A. 권장하지 않는다. 팀 프로젝트에서는 yarn 기준으로 통일하는 것이 안전하다.

Q. lock file은 Git에 올려야 하는가?
A. 일반적으로 올린다. 재현 가능한 Build를 위해 필요하다.

---

# 3. Development Server vs Production Build

## 3.1 Development Server

### [개념]

Development Server는 개발 중 화면 확인과 빠른 피드백을 위해 사용하는 서버다.

대표 명령:

```bash
npm start
npm run dev
```

---

### [핵심]

Development Server 특징:

- 개발 편의용이다.
- Hot Reload 또는 Fast Refresh를 제공한다.
- Source Map이 자세하다.
- 최적화 수준이 낮다.
- 파일 해시 전략이 운영과 다를 수 있다.
- 운영 서버로 사용하기에 적합하지 않다.
- 개발 서버에서 정상이어도 Production Build에서 실패할 수 있다.

---

### [실무]

2026 실무 기준으로 Development Server는 로컬 개발 전용으로 판단한다.

Development Server 사용 상황:

```text
컴포넌트 개발
라우팅 확인
API 연동 테스트
UI 수정 확인
브라우저 Console 확인
로컬 디버깅
```

주의:

```text
Development Server 정상
≠
Production Build 정상
≠
Deployment 정상
```

---

### [FAQ]

Q. npm start로 실행되는 화면을 그대로 배포해도 되는가?
A. 아니다. 운영 배포에는 Production Build 결과물을 사용하는 것이 기본이다.

Q. 개발 서버에서는 되는데 운영에서 안 되는 이유는?
A. API URL, 환경 변수, CORS, HTTPS, SPA fallback, Cache 설정이 다르기 때문이다.

Q. Development Server는 실제 사용자에게 제공해도 되는가?
A. 권장하지 않는다. 개발 편의용 서버이며 운영 최적화와 보안 기준에 적합하지 않다.

---

## 3.2 Production Build

### [개념]

Production Build는 실제 사용자에게 배포하기 위한 최적화된 정적 파일 결과물이다.

---

### [핵심]

Production Build 특징:

- 코드 압축 적용
- 번들 최적화 적용
- Tree Shaking 적용
- 파일명 hash 적용
- Production 환경 변수 반영
- Source Map 제한 또는 비활성 가능
- 정적 파일 서버 필요
- 배포 후 검증 필요

---

### [실무]

2026 실무 기준으로 Production Build는 배포 파이프라인의 최소 필수 단계다.

Production Build 검증 항목:

```md
- [ ] build command 성공
- [ ] output directory 생성
- [ ] index.html 생성
- [ ] JS / CSS asset 생성
- [ ] 환경 변수 반영
- [ ] localhost API URL 제거
- [ ] source map 공개 여부 확인
- [ ] 정적 파일 경로 확인
```

Production Build 후 배포 Flow:

```text
npm run build
→ build or dist 생성
→ Static Hosting Server에 업로드
→ index.html 제공
→ Browser에서 JS bundle 실행
→ API 요청 확인
```

---

### [FAQ]

Q. Production Build는 왜 필요한가?
A. 실제 사용자에게 제공할 최적화된 정적 파일을 만들기 위해 필요하다.

Q. Production Build 결과물은 어디에 배포하는가?
A. Nginx, Spring Boot static, Vercel, Netlify, S3, CloudFront 같은 정적 파일 제공 환경에 배포한다.

Q. Production Build 후에도 테스트가 필요한가?
A. 필요하다. Build 성공은 배포 성공을 보장하지 않는다.

---

## 3.3 Comparison

### [개념]

Development Server와 Production Build는 목적과 동작 방식이 다르다.

---

### [핵심]

| 구분       | Development Server         | Production Build     |
| ---------- | -------------------------- | -------------------- |
| 목적       | 개발 중 확인               | 실제 배포            |
| 대표 명령  | `npm start`, `npm run dev` | `npm run build`      |
| 최적화     | 낮음                       | 높음                 |
| Hot Reload | 있음                       | 없음                 |
| 파일 해시  | 보통 없음                  | 있음                 |
| Source Map | 자세함                     | 제한 가능            |
| 서버       | 개발 서버 내장             | 별도 정적 서버 필요  |
| 사용 환경  | local                      | staging / production |

---

### [실무]

Agent는 사용자의 질문에서 다음을 구분해야 한다.

```text
"로컬에서 실행"
→ Development Server 가능성 높음

"배포"
→ Production Build + Static Hosting 필요

"빌드 폴더"
→ Build Output 확인 필요

"새로고침 404"
→ Production Hosting fallback 문제 가능성 높음

"API가 localhost로 감"
→ Production Build 환경 변수 문제 가능성 높음
```

---

### [FAQ]

Q. 개발 서버와 Production Build의 가장 큰 차이는 무엇인가?
A. 개발 서버는 개발 편의용이고 Production Build는 실제 배포용 정적 파일 생성이다.

Q. 개발 서버에서 정상 동작하면 Build도 성공하는가?
A. 반드시 그렇지 않다. Build 단계에서 타입, lint, import, 환경 변수 문제가 드러날 수 있다.

Q. Production Build가 성공하면 운영에서 완전히 안전한가?
A. 아니다. 서버 fallback, API URL, CORS, HTTPS, Cache 검증이 추가로 필요하다.

---

# 4. Build Output

## 4.1 Output Directory

### [개념]

Output Directory는 Build 결과물이 생성되는 폴더다.

---

### [핵심]

대표 Output Directory:

| Tool     | Build Command   | Output Directory |
| -------- | --------------- | ---------------- |
| Vite     | `npm run build` | `dist`           |
| CRA      | `npm run build` | `build`          |
| Next.js  | `next build`    | `.next`          |
| Vue Vite | `npm run build` | `dist`           |

---

### [실무]

2026 실무 기준으로 React SPA 배포에서는 `dist` 또는 `build` 폴더를 정확히 구분해야 한다.

Vite 구조:

```text
dist/
├ index.html
└ assets/
   ├ index.[hash].js
   └ index.[hash].css
```

CRA 구조:

```text
build/
├ index.html
└ static/
   ├ js/
   └ css/
```

Agent 검토 기준:

```text
Build Tool 확인
→ Output Directory 확인
→ index.html 위치 확인
→ asset directory 확인
→ 배포 서버 root와 연결 확인
```

---

### [FAQ]

Q. Vite Build 결과물은 어디에 생성되는가?
A. 기본적으로 `dist` 폴더에 생성된다.

Q. CRA Build 결과물은 어디에 생성되는가?
A. 기본적으로 `build` 폴더에 생성된다.

Q. build 폴더와 dist 폴더는 같은 의미인가?
A. 역할은 유사하지만 빌드 도구별 기본 출력 폴더명이 다르다.

Q. Output Directory를 잘못 배포하면 어떤 문제가 생기는가?
A. index.html이 제공되지 않거나 JS / CSS asset 404가 발생할 수 있다.

---

## 4.2 Build Output Validation

### [개념]

Build Output Validation은 생성된 정적 파일이 실제 배포 가능한 구조인지 확인하는 과정이다.

---

### [핵심]

Build Output 필수 확인:

- `index.html` 존재
- JS bundle 존재
- CSS bundle 존재
- asset path 정상
- 파일 크기 비정상 증가 여부
- source map 공개 여부
- 환경 변수 반영 여부
- 배포 서버 root에 맞는 구조 여부

---

### [실무]

2026 실무 기준으로 Build 성공 로그만 보고 배포하면 안 된다.

검증 Flow:

```text
Output Directory 열기
→ index.html 확인
→ script src 확인
→ CSS link 확인
→ asset path 확인
→ 정적 서버로 preview
→ Browser Console 확인
→ Network 404 확인
```

Vite preview 예:

```bash
npm run build
npm run preview
```

CRA 정적 서버 확인 예:

```bash
npx serve -s build
```

---

### [FAQ]

Q. Build가 성공했는데 흰 화면이 나올 수 있는가?
A. 가능하다. asset path, runtime error, 환경 변수 누락, Router basename 문제가 있을 수 있다.

Q. index.html만 있으면 배포 가능한가?
A. 아니다. JS, CSS, asset 파일이 함께 정상 경로에 있어야 한다.

Q. Build Output을 직접 파일로 열어도 되는가?
A. 권장하지 않는다. 정적 서버로 제공해야 라우팅과 asset 경로 문제를 정확히 확인할 수 있다.

---

# 5. Build Failure

## 5.1 Build Error Categories

### [개념]

Build Error는 운영 배포용 정적 파일 생성 과정에서 발생하는 오류다.

---

### [핵심]

대표 Build Error:

- TypeScript Error
- ESLint Error
- Dependency Install Error
- Node Version Mismatch
- Environment Variable Missing
- Import Path Error
- File Name Case Error
- Package Lock Mismatch
- Memory Error
- Build Tool Config Error

---

### [실무]

2026 실무 기준으로 Build Error는 첫 번째 Error부터 해결해야 한다.

Troubleshooting Flow:

```text
Build Log 확인
→ 첫 번째 Error 확인
→ Error Type 분류
→ Node Version 확인
→ Dependency 재설치
→ Import Path 확인
→ Environment Variable 확인
→ Build Tool Config 확인
→ Rebuild
```

우선순위:

```text
Dependency Error
→ Syntax / Type Error
→ Import Path Error
→ Env Error
→ Build Config Error
→ Memory Error
```

---

### [FAQ]

Q. Build Error는 어디서부터 봐야 하는가?
A. 로그의 첫 번째 실제 Error를 먼저 확인해야 한다.

Q. Warning이 있으면 Build 실패인가?
A. 항상 실패는 아니지만 운영 장애 가능성이 있는 Warning은 검토해야 한다.

Q. Build Error를 무시하고 배포해도 되는가?
A. 권장하지 않는다. Build 실패 상태에서는 배포 가능한 결과물이 생성되지 않을 수 있다.

---

## 5.2 Local vs CI Build Failure

### [개념]

Local Build와 CI Build는 실행 환경이 다르기 때문에 결과가 다를 수 있다.

---

### [핵심]

CI에서만 실패하는 대표 원인:

- Node.js version 차이
- lock file 불일치
- 환경 변수 누락
- Linux 대소문자 구분
- working-directory 오류
- private package 권한 문제
- cache 문제
- memory 제한

---

### [실무]

2026 실무 기준으로 CI Build는 운영 배포 기준에 더 가깝게 판단한다.

CI Build 확인 항목:

```md
- [ ] Node.js version 지정
- [ ] package manager 통일
- [ ] lock file 기준 install
- [ ] working-directory 설정
- [ ] required env 설정
- [ ] secret은 CI Secret에 저장
- [ ] Linux case-sensitive import 확인
```

GitHub Actions 하위 frontend 예:

```yaml
- name: Build Frontend
  working-directory: ./frontend
  run: npm run build
```

---

### [FAQ]

Q. 로컬에서는 되는데 GitHub Actions에서 Build가 실패하는 이유는?
A. Node 버전, lock file, 환경 변수, working-directory, 파일명 대소문자 문제가 대표 원인이다.

Q. Windows에서는 되는데 Linux에서 import 에러가 나는 이유는?
A. Linux는 파일명 대소문자를 구분하므로 import 경로의 대소문자 불일치가 실패할 수 있다.

Q. CI에서 env가 없으면 Build가 실패할 수 있는가?
A. 가능하다. Build 시점에 필요한 환경 변수가 누락되면 실패하거나 잘못된 값이 들어갈 수 있다.

---

# 6. Agent Decision Rules

## 6.1 PM Agent Rules

### [개념]

PM Agent는 Build 단계에서 프로젝트의 배포 가능 상태와 책임 범위를 판단한다.

---

### [핵심]

PM Agent 확인 항목:

- Build Tool
- Package Manager
- Build Command
- Output Directory
- Deployment Target
- Environment Variable
- API Base URL
- CI/CD 필요 여부
- 배포 검증 범위

---

### [실무]

PM Agent 판단 Flow:

```text
프로젝트 구조 확인
→ frontend 위치 확인
→ build command 확인
→ output directory 확인
→ 배포 방식 결정
→ 검증 체크리스트 생성
```

PM Agent 산출물:

```text
Build Command
Output Directory
Deploy Target
Env Required List
Verification Checklist
Risk List
```

---

### [FAQ]

Q. PM Agent는 Build에서 무엇을 정리해야 하는가?
A. 빌드 도구, 빌드 명령, 결과 폴더, 배포 대상, 환경 변수, 검증 범위를 정리해야 한다.

Q. PM Agent가 직접 코드를 수정하는가?
A. 아니다. PM Agent는 계획과 판단 기준을 정리하고 구현은 Frontend Agent가 수행한다.

---

## 6.2 Frontend Agent Rules

### [개념]

Frontend Agent는 Build 가능한 프로젝트 상태를 유지하고 Production Build 기준에 맞는 코드를 작성한다.

---

### [핵심]

Frontend Agent 필수 기준:

- build script 유지
- dependency 정리
- TypeScript / ESLint 오류 제거
- 환경 변수 prefix 준수
- API URL 하드코딩 방지
- asset path 안정화
- Router basename 필요 여부 확인
- Build Output 구조 이해

---

### [실무]

Frontend Agent 구현 기준:

```text
Local Development 동작
→ npm run build 성공
→ Output Directory 확인
→ Production Preview 확인
→ Console / Network 확인
```

배포 고려 코드 기준:

```text
localhost 직접 하드코딩 금지
secret key 프론트엔드 저장 금지
환경 변수 prefix 준수
build 시점 env 반영 인지
```

---

### [FAQ]

Q. Frontend Agent가 Build를 고려해 가장 먼저 지켜야 할 것은?
A. `npm run build`가 항상 성공하는 코드 상태를 유지해야 한다.

Q. 코드에 localhost를 넣어도 되는가?
A. 개발용으로는 가능하지만 운영 Build에 남지 않도록 환경 변수로 분리해야 한다.

Q. Frontend Agent가 secret key를 env에 넣어도 되는가?
A. 안 된다. 프론트엔드 env는 브라우저에 노출될 수 있다.

---

## 6.3 Review Agent Rules

### [개념]

Review Agent는 Build 전후로 운영 장애를 만들 수 있는 설정과 코드를 검토한다.

---

### [핵심]

Review Agent Build Checklist:

```md
- [ ] `npm run build` 성공
- [ ] output directory 생성
- [ ] index.html 존재
- [ ] JS / CSS asset 존재
- [ ] TypeScript error 없음
- [ ] ESLint error 없음
- [ ] localhost 하드코딩 없음
- [ ] secret key 노출 없음
- [ ] 환경 변수 prefix 정상
- [ ] source map 공개 여부 검토
- [ ] asset path 정상
- [ ] Production Preview 정상
```

---

### [실무]

Review Agent 판단 Flow:

```text
Build Command 확인
→ Build 실행 결과 확인
→ Output Directory 확인
→ Env 값 확인
→ Asset Path 확인
→ Browser Preview 확인
→ 배포 가능 여부 판단
```

Build 승인 기준:

```text
Critical Error 없음
Build 성공
Output Directory 정상
운영 API URL 분리 가능
Secret 노출 없음
Preview에서 Console Error 없음
```

---

### [FAQ]

Q. Review Agent가 Build에서 가장 먼저 확인할 것은?
A. `npm run build` 성공 여부와 Build Output 생성 여부다.

Q. Console Error가 있으면 Build 승인 가능한가?
A. Runtime Error나 asset 404라면 승인하면 안 된다.

Q. Warning이 있으면 무조건 실패인가?
A. 아니다. 단, 보안, 성능, 운영 안정성에 영향이 있는 Warning은 수정 대상이다.

---

# 7. Common Mistakes

## 7.1 Build Common Mistakes

### [개념]

Build Common Mistakes는 프론트엔드 배포 실패로 이어지는 반복적인 실수다.

---

### [핵심]

자주 발생하는 실수:

- `npm start`를 운영 배포로 착각
- `npm run build`를 실행하지 않고 배포
- Source Code를 그대로 정적 서버에 업로드
- Vite output을 `build`로 착각
- CRA output을 `dist`로 착각
- Build Output 폴더 자체를 잘못된 위치에 복사
- `.env` 수정 후 재빌드하지 않음
- 운영 API URL이 localhost로 남음
- secret key를 프론트엔드 env에 저장
- Linux 배포에서 파일명 대소문자 import 실패
- lock file과 package manager 혼용
- CI working-directory 누락

---

### [실무]

실수별 판단:

```text
화면이 흰색
→ JS asset 404 / runtime error / env 누락 확인

API가 localhost 호출
→ env / build 시점 / production env 확인

Build는 됐는데 CSS 없음
→ asset path / output directory / static server root 확인

CI에서만 실패
→ Node version / lock file / working-directory / 대소문자 확인
```

---

### [FAQ]

Q. 배포 초보가 가장 많이 하는 Build 실수는?
A. 개발 서버와 Production Build를 혼동하는 것이다.

Q. Build Output이 아니라 Source Code를 올리면 어떻게 되는가?
A. 브라우저가 React 소스 구조를 직접 실행할 수 없으므로 정상 동작하지 않는다.

Q. .env를 수정했는데 왜 운영에 반영되지 않는가?
A. 일반 React SPA에서는 Build 시점에 env가 주입되므로 다시 Build해야 한다.

Q. dist와 build를 헷갈리면 어떤 문제가 생기는가?
A. 배포 서버가 index.html이나 asset을 찾지 못해 404 또는 흰 화면이 발생할 수 있다.

---

# 8. Part01 Quality Checklist

## 8.1 Document Quality

### [개념]

이 문서는 Frontend Build & Deploy Domain의 Part01이며 Build Core Retrieval에 최적화되어야 한다.

---

### [핵심]

문서 품질 기준:

- Build와 Deploy를 혼동하지 않는다.
- Development Server와 Production Build를 구분한다.
- Vite / CRA Output Directory를 명확히 구분한다.
- Build Command와 Package Manager를 연결한다.
- Build Failure 원인을 분류한다.
- PM Agent / Frontend Agent / Review Agent 판단 기준을 포함한다.
- FAQ는 실제 사용자 질문 형태로 작성한다.
- Retrieval Queries를 포함한다.

---

### [실무]

Part01은 다음 문서와 연결된다.

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

Q. Part01의 핵심 목적은 무엇인가?
A. Build 개념, Build Command, Development Server와 Production Build 차이를 Agent가 정확히 판단하게 하는 것이다.

Q. Part01에서 Deploy 설정까지 자세히 다루는가?
A. 아니다. Part01은 Build Core에 집중하고 Deploy 설정은 후속 Part에서 분리한다.

Q. 이 문서는 사람 공부용인가?
A. 아니다. Frontend Agent / Review Agent / PM Agent Retrieval 최적화 문서다.

---

# Retrieval Queries

### [FAQ]

Q. 프론트엔드 Build란 무엇인가?
A. React / JavaScript / CSS 소스 코드를 브라우저가 실행 가능한 정적 파일로 변환하는 과정이다.

Q. Build는 서버 실행인가?
A. 아니다. Build는 HTML, CSS, JavaScript, Asset 같은 정적 파일을 생성하는 과정이다.

Q. npm run build는 무엇을 하는가?
A. 운영 배포용 정적 파일을 생성한다.

Q. npm start와 npm run build는 같은가?
A. 아니다. `npm start`는 보통 개발 서버 실행이고 `npm run build`는 Production Build 명령이다.

Q. Development Server란 무엇인가?
A. 개발 중 화면 확인과 빠른 피드백을 위한 개발용 서버다.

Q. Production Build란 무엇인가?
A. 실제 사용자에게 배포하기 위해 최적화된 정적 파일 결과물이다.

Q. 개발 서버에서 되면 운영에서도 무조건 되는가?
A. 아니다. 환경 변수, API URL, CORS, HTTPS, SPA fallback, Cache 문제가 운영에서 발생할 수 있다.

Q. Build Output이란 무엇인가?
A. Build 후 생성되는 index.html, JS bundle, CSS bundle, asset 파일이다.

Q. Vite Build 결과물은 어디에 생성되는가?
A. 기본적으로 `dist` 폴더에 생성된다.

Q. CRA Build 결과물은 어디에 생성되는가?
A. 기본적으로 `build` 폴더에 생성된다.

Q. Build 결과물을 어디에 배포하는가?
A. Nginx, Spring Boot static, Vercel, Netlify, S3, CloudFront 같은 정적 파일 제공 환경에 배포한다.

Q. Build Output을 직접 브라우저 파일 열기로 실행해도 되는가?
A. 권장하지 않는다. 정적 서버로 제공해야 라우팅과 asset 경로 문제를 정확히 확인할 수 있다.

Q. Build 실패 시 무엇을 먼저 확인하는가?
A. Build Log의 첫 번째 실제 Error를 먼저 확인한다.

Q. Build Error의 대표 원인은 무엇인가?
A. TypeScript Error, ESLint Error, dependency 문제, Node version mismatch, env 누락, import path 오류가 대표 원인이다.

Q. 로컬에서는 되는데 CI에서 Build가 실패하는 이유는?
A. Node version, lock file, working-directory, 환경 변수, Linux 대소문자 문제가 대표 원인이다.

Q. Windows에서는 되는데 Linux에서 import 에러가 나는 이유는?
A. Linux는 파일명 대소문자를 구분하므로 import 경로 대소문자가 다르면 실패할 수 있다.

Q. package manager는 어떻게 판단하는가?
A. `package-lock.json`은 npm, `yarn.lock`은 yarn, `pnpm-lock.yaml`은 pnpm 기준으로 판단한다.

Q. npm과 yarn을 섞어 써도 되는가?
A. 권장하지 않는다. lock file 불일치와 의존성 차이로 Build 실패가 발생할 수 있다.

Q. lock file은 Git에 올려야 하는가?
A. 일반적으로 올린다. 재현 가능한 Build를 위해 필요하다.

Q. Build가 성공했으면 배포도 성공인가?
A. 아니다. Build 성공 후에도 API URL, SPA fallback, CORS, HTTPS, Cache 검증이 필요하다.

Q. Build 후 흰 화면이 나오는 이유는?
A. JS asset 404, runtime error, 환경 변수 누락, Router basename 오류, asset path 문제가 대표 원인이다.

Q. Build 후 CSS가 안 먹는 이유는?
A. CSS asset 404, base path 오류, output directory 배포 오류, 서버 root 오류가 원인일 수 있다.

Q. Build 후 API가 localhost로 호출되는 이유는?
A. Production Build 시점에 개발용 API URL이 들어갔거나 운영 env 설정이 누락된 것이다.

Q. Frontend Agent는 Build에서 무엇을 지켜야 하는가?
A. build script 유지, env prefix 준수, localhost 하드코딩 제거, secret 미노출, asset path 안정화를 지켜야 한다.

Q. Review Agent는 Build에서 무엇을 확인해야 하는가?
A. `npm run build` 성공, output directory, index.html, asset 존재, env, secret 노출, Console Error를 확인해야 한다.

Q. PM Agent는 Build에서 무엇을 정리해야 하는가?
A. Build Tool, Build Command, Output Directory, Package Manager, Deployment Target, 검증 범위를 정리해야 한다.

Q. Part01 다음 문서는 무엇인가?
A. Part02 Build Tool Rules로 이어지는 것이 적합하다.
