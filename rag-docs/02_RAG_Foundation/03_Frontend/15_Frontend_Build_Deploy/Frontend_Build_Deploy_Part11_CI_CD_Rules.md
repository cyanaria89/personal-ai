# Frontend Build & Deploy Part11 - CI/CD Rules

---

# 1. CI/CD Core

## 1.1 CI/CD Definition

### [개념]

CI/CD는 코드 변경 이후 Build, Test, 검증, 배포를 자동화하는 프로세스다.

Frontend Build & Deploy에서 CI/CD는 프론트엔드 프로젝트가 배포 가능한 상태인지 자동으로 확인하고, 정적 Build 결과물을 배포 대상 환경에 전달하는 역할을 한다.

대표 흐름:

```text
Git Push
→ CI Pipeline Trigger
→ Install Dependencies
→ Lint / Test
→ Build
→ Artifact 생성
→ Deploy
→ Smoke Test
```

---

### [핵심]

Frontend CI/CD 핵심 규칙:

- `npm run build`가 자동으로 실행되어야 한다.
- 의존성 설치는 lock file 기준으로 재현 가능해야 한다.
- Build 전 Lint / Test를 실행할 수 있다.
- Build Output Directory를 정확히 지정해야 한다.
- 환경 변수는 CI/CD에서 안전하게 주입해야 한다.
- Secret을 frontend build에 주입하면 안 된다.
- 배포 후 최소 smoke test가 필요하다.
- 실패한 build를 배포하면 안 된다.
- Preview / Staging / Production 배포를 구분해야 한다.
- Rollback 가능한 구조를 고려해야 한다.

---

### [실무]

2026 실무 기준으로 프론트엔드 CI/CD는 GitHub Actions, GitLab CI, Jenkins, Vercel, Netlify, Cloudflare Pages 같은 도구를 통해 자동화된다.

기본 CI/CD Flow:

```text
Checkout
→ Setup Node
→ Dependency Install
→ Static Analysis
→ Test
→ Production Build
→ Upload Artifact
→ Deploy
→ Verify
```

Agent 판단 Flow:

```text
Repository 구조 확인
→ package manager 확인
→ Node version 확인
→ build command 확인
→ output directory 확인
→ env 주입 방식 확인
→ deploy target 확인
→ verification step 확인
```

---

### [FAQ]

Q. CI/CD란 무엇인가?
A. 코드 변경 후 Build, Test, 배포 과정을 자동화하는 프로세스다.

Q. 프론트엔드 CI/CD에서 가장 중요한 단계는 무엇인가?
A. 의존성 설치, Build, 환경 변수 주입, 배포 결과 검증이다.

Q. Build가 실패했는데 배포해도 되는가?
A. 안 된다. 실패한 Build Output은 배포 대상이 될 수 없다.

Q. 프론트엔드 CI/CD에서도 Secret 관리가 중요한가?
A. 중요하다. Secret을 frontend build에 주입하면 브라우저에 노출될 수 있다.

---

## 1.2 CI vs CD

### [개념]

CI는 Continuous Integration이며 코드가 정상적으로 통합 가능한지 자동 검증하는 단계다.

CD는 Continuous Delivery 또는 Continuous Deployment이며 검증된 결과물을 배포 가능한 상태로 만들거나 실제 배포하는 단계다.

---

### [핵심]

CI 주요 작업:

```text
Checkout
Install
Lint
Test
Build
Type Check
Artifact 생성
```

CD 주요 작업:

```text
Deploy to Hosting
Upload to S3
Deploy to Vercel / Netlify
Docker Image Push
Server Restart
Smoke Test
Rollback 준비
```

구분 기준:

```text
CI
→ 배포 가능한지 검증

CD
→ 실제 배포 또는 배포 준비
```

---

### [실무]

Frontend 프로젝트에서 CI만 있는 경우:

```text
PR 생성
→ lint
→ test
→ build
→ merge 가능 여부 판단
```

CI/CD 모두 있는 경우:

```text
main push
→ lint
→ test
→ build
→ deploy
→ smoke test
```

Agent 판단 기준:

```text
PR workflow
→ CI 중심

main push workflow
→ CI + CD 가능성

release tag workflow
→ Production CD 가능성
```

---

### [FAQ]

Q. CI와 CD는 무엇이 다른가?
A. CI는 코드 통합 검증이고, CD는 검증된 결과물을 배포하는 과정이다.

Q. PR에서는 배포까지 해야 하는가?
A. 보통 PR에서는 CI 검증을 하고, 필요하면 Preview Deploy를 만든다.

Q. main branch push에서는 무엇을 하는가?
A. CI 검증 후 staging 또는 production 배포를 실행할 수 있다.

Q. CI만 있어도 충분한가?
A. 프로젝트 규모와 배포 방식에 따라 충분할 수 있지만 반복 배포가 많다면 CD 자동화가 유리하다.

---

# 2. Pipeline Structure

## 2.1 Frontend Pipeline Steps

### [개념]

Frontend Pipeline Steps는 프론트엔드 프로젝트를 자동 검증하고 배포하기 위한 단계 목록이다.

---

### [핵심]

권장 Pipeline:

```text
1. Checkout
2. Setup Node
3. Install Dependencies
4. Lint
5. Test
6. Build
7. Upload Artifact
8. Deploy
9. Smoke Test
```

선택 단계:

```text
Type Check
Format Check
Bundle Analyze
Security Audit
E2E Test
Lighthouse Check
Docker Build
Image Push
Cache Invalidation
```

---

### [실무]

React SPA 기본 Pipeline 예:

```text
checkout
→ setup-node 20
→ npm ci
→ npm run lint
→ npm test
→ npm run build
→ deploy dist/build
```

학원 프로젝트 최소 Pipeline:

```text
checkout
→ setup-node
→ npm ci
→ npm run build
```

운영 프로젝트 권장 Pipeline:

```text
checkout
→ install
→ lint
→ test
→ type-check
→ build
→ deploy
→ smoke test
```

---

### [FAQ]

Q. 프론트엔드 CI/CD Pipeline의 기본 단계는 무엇인가?
A. checkout, setup node, install, lint/test, build, deploy, smoke test다.

Q. 학원 프로젝트에서도 모든 단계를 다 해야 하는가?
A. 필수는 아니다. 최소한 install과 build 자동화는 하는 것이 좋다.

Q. TypeScript 프로젝트에서는 어떤 단계가 추가되는가?
A. type-check 단계를 추가하는 것이 좋다.

Q. 운영 프로젝트에서 smoke test가 필요한 이유는?
A. 배포 성공 후 실제 URL, asset, API 요청이 정상인지 확인하기 위해 필요하다.

---

## 2.2 Branch-based Pipeline

### [개념]

Branch-based Pipeline은 branch 종류에 따라 CI/CD 동작을 다르게 구성하는 방식이다.

---

### [핵심]

대표 branch 전략:

```text
feature/*
develop
main
release/*
hotfix/*
```

Branch별 Pipeline 예:

```text
feature/*
→ lint / test / build

develop
→ lint / test / build / staging deploy

main
→ lint / test / build / production deploy

release tag
→ production deploy / versioning
```

---

### [실무]

GitHub Actions trigger 예:

```yaml
on:
  pull_request:
    branches: [develop, main]

  push:
    branches: [develop, main]
```

Branch 판단 Flow:

```text
PR to develop
→ CI 검증

push to develop
→ staging deploy

push to main
→ production deploy
```

주의:

```text
모든 branch에서 production deploy 금지
```

---

### [FAQ]

Q. Branch-based Pipeline이란 무엇인가?
A. branch 종류에 따라 build, test, staging deploy, production deploy를 다르게 실행하는 방식이다.

Q. feature branch에서 production 배포해도 되는가?
A. 일반적으로 안 된다. feature branch는 CI 검증 중심이 적합하다.

Q. develop branch는 어디에 배포하는가?
A. 보통 staging 또는 development 환경에 배포한다.

Q. main branch는 어디에 배포하는가?
A. 보통 production 배포 기준 branch로 사용한다.

---

## 2.3 Environment-based Pipeline

### [개념]

Environment-based Pipeline은 development, staging, production 같은 배포 환경별로 다른 설정과 검증 단계를 사용하는 방식이다.

---

### [핵심]

환경별 기준:

```text
Development
→ 빠른 검증

Staging
→ 운영 전 검증

Production
→ 실제 사용자 대상
```

환경별 차이:

- API Base URL
- Environment Variables
- Build Mode
- Deployment Target
- Secret Scope
- Approval 필요 여부
- Cache Invalidation 여부
- Smoke Test 범위

---

### [실무]

GitHub Actions environment 예:

```yaml
environment: production
```

Staging env:

```text
VITE_API_BASE_URL=https://staging-api.example.com
```

Production env:

```text
VITE_API_BASE_URL=https://api.example.com
```

검증 Flow:

```text
branch 확인
→ target environment 결정
→ environment variables 주입
→ build
→ deploy target 선택
→ smoke test
```

---

### [FAQ]

Q. Environment-based Pipeline이란 무엇인가?
A. 개발, 스테이징, 운영 환경별로 다른 설정과 배포 대상을 사용하는 pipeline이다.

Q. staging과 production은 왜 분리하는가?
A. 운영 배포 전 실제와 유사한 환경에서 검증하기 위해 분리한다.

Q. 환경별로 가장 중요한 차이는 무엇인가?
A. API Base URL, env 변수, 배포 대상, 승인 절차가 다르다.

Q. production 배포에는 approval을 둘 수 있는가?
A. 가능하다. 운영 배포 실수를 줄이기 위해 승인 단계를 둘 수 있다.

---

# 3. Dependency Install Rules

## 3.1 Package Manager Rules

### [개념]

Package Manager Rules는 CI/CD에서 어떤 package manager로 의존성을 설치할지 정하는 규칙이다.

대표 package manager:

```text
npm
yarn
pnpm
```

---

### [핵심]

판단 기준:

```text
package-lock.json
→ npm

yarn.lock
→ yarn

pnpm-lock.yaml
→ pnpm
```

권장 명령:

```bash
npm ci
```

```bash
yarn install --frozen-lockfile
```

```bash
pnpm install --frozen-lockfile
```

주의:

- package manager를 혼용하지 않는다.
- lock file을 Git에 포함한다.
- CI와 로컬 package manager를 일치시킨다.
- lock file 없는 install은 재현성이 떨어진다.

---

### [실무]

npm GitHub Actions 예:

```yaml
- name: Install dependencies
  run: npm ci
```

yarn 예:

```yaml
- name: Install dependencies
  run: yarn install --frozen-lockfile
```

pnpm 예:

```yaml
- name: Setup pnpm
  uses: pnpm/action-setup@v4

- name: Install dependencies
  run: pnpm install --frozen-lockfile
```

Agent 검토 Flow:

```text
lock file 확인
→ package manager 결정
→ CI install command 확인
→ cache 설정 확인
→ build log 확인
```

---

### [FAQ]

Q. CI에서 npm install보다 npm ci가 좋은 이유는?
A. lock file 기준으로 재현 가능한 설치를 수행하기 때문이다.

Q. yarn.lock이 있는데 npm ci를 써도 되는가?
A. 권장하지 않는다. package manager와 lock file을 일치시켜야 한다.

Q. lock file은 Git에 올려야 하는가?
A. 일반적으로 올려야 한다. CI 재현성을 위해 필요하다.

Q. package manager 혼용은 왜 위험한가?
A. 의존성 버전과 lock file이 달라져 로컬과 CI 결과가 달라질 수 있다.

---

## 3.2 Dependency Cache Rules

### [개념]

Dependency Cache는 CI/CD에서 의존성 설치 속도를 높이기 위해 npm, yarn, pnpm cache를 재사용하는 방식이다.

---

### [핵심]

Cache 기준:

- package manager별 cache 경로가 다르다.
- lock file이 cache key에 포함되어야 한다.
- dependency가 바뀌면 cache가 갱신되어야 한다.
- cache가 깨졌을 때 재설치 가능해야 한다.
- cache는 속도 최적화이지 correctness 보장이 아니다.

---

### [실무]

GitHub Actions npm cache 예:

```yaml
- uses: actions/setup-node@v4
  with:
    node-version: 20
    cache: npm
    cache-dependency-path: frontend/package-lock.json
```

Monorepo에서는 cache path 확인:

```yaml
cache-dependency-path: frontend/package-lock.json
```

Troubleshooting Flow:

```text
install이 느림
→ cache 설정 확인

cache 후 build 이상
→ lock file 확인
→ clean install 재현
```

---

### [FAQ]

Q. Dependency Cache는 왜 사용하는가?
A. CI에서 의존성 설치 시간을 줄이기 위해 사용한다.

Q. cache key에 lock file이 중요한 이유는?
A. 의존성 변경 시 cache가 적절히 갱신되어야 하기 때문이다.

Q. cache가 있으면 npm ci가 필요 없는가?
A. 아니다. cache는 다운로드 속도 최적화이고 설치 명령은 여전히 필요하다.

Q. cache 때문에 문제가 생기면 어떻게 하는가?
A. cache를 무시하고 clean install로 재현해 확인한다.

---

# 4. Build Rules in CI/CD

## 4.1 CI Build Command Rules

### [개념]

CI Build Command는 pipeline에서 배포 가능한 정적 파일을 생성하기 위해 실행하는 build 명령이다.

---

### [핵심]

기본 Build Command:

```bash
npm run build
```

Build Tool별 결과:

```text
Vite
→ dist

CRA
→ build
```

중요 확인:

- build script 존재 여부
- env variable 주입 여부
- build mode
- output directory
- TypeScript / ESLint 실패 여부
- memory limit
- working-directory

---

### [실무]

Vite CI Build 예:

```yaml
- name: Build
  working-directory: ./frontend
  env:
    VITE_API_BASE_URL: ${{ vars.VITE_API_BASE_URL }}
  run: npm run build
```

CRA CI Build 예:

```yaml
- name: Build
  working-directory: ./frontend
  env:
    REACT_APP_API_BASE_URL: ${{ vars.REACT_APP_API_BASE_URL }}
  run: npm run build
```

검증 Flow:

```text
build log 확인
→ output directory 생성 확인
→ index.html 존재 확인
→ artifact path 확인
```

---

### [FAQ]

Q. CI에서 Build Command는 무엇인가?
A. 배포 가능한 정적 파일을 생성하기 위해 실행하는 명령이다.

Q. Vite와 CRA의 CI Build Command는 같은가?
A. 보통 `npm run build`로 같지만 결과 폴더는 Vite `dist`, CRA `build`로 다르다.

Q. CI Build에서 env가 필요한 이유는?
A. API Base URL 같은 Build-time 설정이 필요하기 때문이다.

Q. Build는 성공했는데 배포 파일이 없으면 무엇을 확인하는가?
A. output directory와 artifact path를 확인해야 한다.

---

## 4.2 Type Check and Lint Rules

### [개념]

Type Check and Lint Rules는 CI에서 코드 품질과 타입 오류를 배포 전에 확인하는 규칙이다.

---

### [핵심]

확인 대상:

```text
TypeScript type error
ESLint rule violation
unused import
format issue
accessibility lint
import path error
```

일반 명령:

```bash
npm run lint
npm run type-check
```

package.json 예:

```json
{
  "scripts": {
    "lint": "eslint src",
    "type-check": "tsc --noEmit",
    "build": "vite build"
  }
}
```

---

### [실무]

CI 예:

```yaml
- name: Lint
  working-directory: ./frontend
  run: npm run lint

- name: Type Check
  working-directory: ./frontend
  run: npm run type-check
```

주의:

```text
CRA / Vite / TypeScript 설정에 따라
build 단계에서 일부 오류가 함께 잡힐 수 있다.
```

Agent 판단 기준:

```text
TypeScript 프로젝트
→ type-check 권장

협업 프로젝트
→ lint 권장

학원 발표 최소 구성
→ build 성공 우선
```

---

### [FAQ]

Q. CI에서 lint는 왜 실행하는가?
A. 코드 품질과 잠재 오류를 배포 전에 잡기 위해 실행한다.

Q. TypeScript 프로젝트에서 type-check가 필요한가?
A. 권장된다. 타입 오류를 build 또는 배포 전에 발견할 수 있다.

Q. lint 실패 시 배포해도 되는가?
A. 팀 정책에 따라 다르지만 운영 배포에서는 실패로 처리하는 것이 일반적이다.

Q. 학원 프로젝트에서도 lint/type-check가 필수인가?
A. 필수는 아니지만 협업 품질을 높이는 데 도움이 된다.

---

## 4.3 Test Rules

### [개념]

Test Rules는 CI에서 단위 테스트, 컴포넌트 테스트, E2E 테스트를 실행해 배포 전 기능 안정성을 확인하는 규칙이다.

---

### [핵심]

테스트 종류:

```text
Unit Test
Component Test
Integration Test
E2E Test
Smoke Test
```

대표 도구:

```text
Vitest
Jest
React Testing Library
Cypress
Playwright
```

기본 원칙:

- 빠른 테스트는 CI 초반에 실행한다.
- 느린 E2E는 staging 이후 실행할 수 있다.
- 실패한 테스트가 있으면 production 배포를 막을 수 있다.
- 테스트 데이터와 운영 데이터를 분리한다.

---

### [실무]

CI test 예:

```yaml
- name: Test
  working-directory: ./frontend
  run: npm test -- --watch=false
```

Vitest 예:

```yaml
- name: Test
  working-directory: ./frontend
  run: npm run test
```

E2E는 별도 job으로 분리 가능:

```text
build job 성공
→ deploy staging
→ e2e test
→ production deploy approval
```

---

### [FAQ]

Q. 프론트엔드 CI에서 테스트는 왜 필요한가?
A. 배포 전에 기능 오류를 자동으로 발견하기 위해 필요하다.

Q. 모든 테스트를 production 배포 전에 실행해야 하는가?
A. 이상적이지만 프로젝트 규모에 따라 빠른 테스트와 느린 테스트를 분리할 수 있다.

Q. E2E 테스트는 언제 실행하는가?
A. staging 배포 후 실제 브라우저 환경에서 실행하는 것이 좋다.

Q. 테스트가 없으면 CI/CD를 만들 수 없는가?
A. 만들 수 있다. 최소한 build 검증부터 시작할 수 있다.

---

# 5. Artifact and Output Rules

## 5.1 Build Artifact Rules

### [개념]

Build Artifact는 CI에서 생성된 배포 가능한 결과물이다.

Frontend에서는 보통 `dist` 또는 `build` 폴더가 Artifact가 된다.

---

### [핵심]

Artifact 대상:

```text
Vite
→ dist

CRA
→ build

Docker
→ image

Spring Boot 통합 배포
→ JAR

S3 배포
→ uploaded static files
```

중요 규칙:

- Artifact는 Build 이후 생성되어야 한다.
- Output Directory가 정확해야 한다.
- Artifact에 `index.html`이 있어야 한다.
- Artifact를 다음 deploy job에서 사용할 수 있어야 한다.
- Artifact retention 기간을 설정할 수 있다.
- Secret 파일이 artifact에 포함되면 안 된다.

---

### [실무]

GitHub Actions artifact upload 예:

```yaml
- name: Upload frontend artifact
  uses: actions/upload-artifact@v4
  with:
    name: frontend-dist
    path: frontend/dist
```

CRA 예:

```yaml
path: frontend/build
```

download 예:

```yaml
- name: Download frontend artifact
  uses: actions/download-artifact@v4
  with:
    name: frontend-dist
    path: dist
```

검증 Flow:

```text
build 완료
→ artifact path 확인
→ index.html 확인
→ deploy job에서 artifact download
→ deploy target에 업로드
```

---

### [FAQ]

Q. Build Artifact란 무엇인가?
A. CI에서 생성된 배포 가능한 결과물이다.

Q. 프론트엔드 Artifact는 보통 무엇인가?
A. Vite는 `dist`, CRA는 `build` 폴더다.

Q. Artifact에 Secret이 포함되어도 되는가?
A. 안 된다. 배포 결과물은 외부에 노출될 수 있다.

Q. Artifact path가 틀리면 어떻게 되는가?
A. deploy job이 배포할 파일을 찾지 못하거나 빈 배포가 될 수 있다.

---

## 5.2 Deploy Output Verification

### [개념]

Deploy Output Verification은 배포 전에 Build Output 또는 Artifact가 실제로 올바른 정적 파일을 포함하는지 확인하는 단계다.

---

### [핵심]

검증 항목:

```md
- [ ] index.html 존재
- [ ] JS bundle 존재
- [ ] CSS bundle 존재
- [ ] asset directory 존재
- [ ] favicon / manifest 필요 시 존재
- [ ] config.json 필요 시 존재
- [ ] source code나 .env가 포함되지 않음
- [ ] output directory가 비어 있지 않음
```

---

### [실무]

CI 검증 명령 예:

```yaml
- name: Verify build output
  working-directory: ./frontend
  run: |
    test -f dist/index.html
    test -d dist/assets
```

CRA:

```yaml
- name: Verify build output
  working-directory: ./frontend
  run: |
    test -f build/index.html
    test -d build/static
```

Agent 판단 기준:

```text
Build 성공
≠
Output path 정확

Output 검증 단계 필요
```

---

### [FAQ]

Q. Build가 성공했는데 output 검증이 필요한가?
A. 필요하다. 배포 설정이 잘못된 경로를 참조할 수 있기 때문이다.

Q. Vite output 검증은 무엇을 확인하는가?
A. `dist/index.html`과 `dist/assets`를 확인한다.

Q. CRA output 검증은 무엇을 확인하는가?
A. `build/index.html`과 `build/static`을 확인한다.

Q. output에 .env가 들어가면 되는가?
A. 안 된다. 환경 변수 파일은 배포 artifact에 포함되면 안 된다.

---

# 6. Deployment Target Rules

## 6.1 Platform Deploy Pipeline

### [개념]

Platform Deploy Pipeline은 Vercel, Netlify, Cloudflare Pages 같은 플랫폼으로 Build 결과를 배포하는 CI/CD 방식이다.

---

### [핵심]

플랫폼 배포 방식:

```text
1. 플랫폼 자체 Git 연동 자동 배포
2. GitHub Actions에서 플랫폼 CLI/API 호출
3. Artifact upload 방식
```

확인 대상:

- project id
- auth token
- org/team id
- production flag
- preview deploy flag
- env variable
- build command 중복 여부

---

### [실무]

플랫폼 자체 배포를 쓰는 경우:

```text
Git push
→ Platform build/deploy
→ Platform dashboard에서 log 확인
```

GitHub Actions에서 CLI를 쓰는 경우:

```text
checkout
→ install
→ build
→ platform deploy command
```

Agent 판단 기준:

```text
플랫폼 자동 build 사용
→ GitHub Actions에서 중복 build 필요성 검토

CI에서 build 후 deploy
→ artifact/output path 정확성 확인
```

---

### [FAQ]

Q. 플랫폼 배포는 CI/CD가 따로 필요 없는가?
A. 플랫폼 자체가 CI/CD 역할을 할 수 있다. 별도 GitHub Actions는 필요에 따라 추가한다.

Q. Vercel/Netlify 자동 배포와 GitHub Actions 배포를 동시에 써도 되는가?
A. 가능하지만 중복 배포와 설정 충돌을 주의해야 한다.

Q. 플랫폼 deploy token은 어디에 저장해야 하는가?
A. GitHub Secrets나 플랫폼 Secret 저장소에 저장해야 한다.

Q. 플랫폼 배포 후 log는 어디서 확인하는가?
A. 플랫폼 dashboard의 deploy log에서 확인한다.

---

## 6.2 S3 CloudFront Deploy Pipeline

### [개념]

S3 CloudFront Deploy Pipeline은 Build Output을 S3에 업로드하고 CloudFront cache를 무효화하는 배포 방식이다.

---

### [핵심]

배포 단계:

```text
Build
→ Verify Output
→ aws s3 sync
→ CloudFront invalidation
→ Smoke Test
```

필요 Secret / Variable:

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
S3_BUCKET
CLOUDFRONT_DISTRIBUTION_ID
```

주의:

- AWS Secret은 frontend build env에 주입하지 않는다.
- CI deploy step에서만 사용한다.
- `--delete` 사용 시 주의한다.
- index.html cache와 invalidation을 고려한다.

---

### [실무]

GitHub Actions 예:

```yaml
- name: Configure AWS credentials
  uses: aws-actions/configure-aws-credentials@v4
  with:
    aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    aws-region: ap-northeast-2

- name: Deploy to S3
  run: aws s3 sync frontend/dist/ s3://${{ vars.S3_BUCKET }} --delete

- name: Invalidate CloudFront
  run: |
    aws cloudfront create-invalidation \
      --distribution-id ${{ vars.CLOUDFRONT_DISTRIBUTION_ID }} \
      --paths "/index.html" "/config.json"
```

CRA:

```text
frontend/build/
```

---

### [FAQ]

Q. S3 CloudFront CI/CD는 어떤 순서로 진행하는가?
A. Build, output 검증, S3 sync, CloudFront invalidation, smoke test 순서로 진행한다.

Q. AWS Secret을 frontend env에 넣어도 되는가?
A. 안 된다. AWS Secret은 deploy step에서만 사용해야 한다.

Q. CloudFront invalidation은 항상 전체 /\*로 해야 하는가?
A. 아니다. index.html과 config.json 중심으로 최소화할 수 있다.

Q. S3 sync --delete는 왜 주의해야 하는가?
A. 로컬 output에 없는 파일을 S3에서 삭제하므로 필요한 파일까지 삭제될 수 있다.

---

## 6.3 Docker Image Deploy Pipeline

### [개념]

Docker Image Deploy Pipeline은 frontend Docker image를 build하고 registry에 push한 뒤 서버에서 pull하여 실행하는 배포 방식이다.

---

### [핵심]

Pipeline 단계:

```text
Checkout
→ Build Docker Image
→ Tag Image
→ Push Registry
→ Server Pull
→ Container Recreate
→ Smoke Test
```

확인 대상:

- Dockerfile
- build context
- image tag
- registry auth
- frontend env strategy
- runtime config
- docker compose update
- rollback image tag

---

### [실무]

GitHub Container Registry 예:

```yaml
- name: Login to GHCR
  uses: docker/login-action@v3
  with:
    registry: ghcr.io
    username: ${{ github.actor }}
    password: ${{ secrets.GITHUB_TOKEN }}

- name: Build and push
  uses: docker/build-push-action@v6
  with:
    context: ./frontend
    push: true
    tags: ghcr.io/org/app-frontend:${{ github.sha }}
```

Server deploy 예:

```bash
docker compose pull frontend
docker compose up -d frontend
```

Review 기준:

```md
- [ ] image tag가 latest만이 아닌가?
- [ ] build context가 맞는가?
- [ ] Secret이 image에 포함되지 않는가?
- [ ] 서버에서 새 image로 container가 recreate 되었는가?
```

---

### [FAQ]

Q. Docker Image Deploy Pipeline은 무엇인가?
A. Docker image를 build/push하고 서버에서 pull하여 컨테이너를 재실행하는 배포 방식이다.

Q. image tag는 무엇을 쓰는 것이 좋은가?
A. commit sha, semantic version, release tag를 사용하는 것이 추적과 rollback에 좋다.

Q. docker build만 하면 서버 배포가 완료되는가?
A. 아니다. registry push, 서버 pull, container recreate가 필요하다.

Q. latest만 쓰면 어떤 문제가 있는가?
A. 현재 실행 중인 버전 추적과 rollback이 어려워진다.

---

## 6.4 Spring Boot Integrated Deploy Pipeline

### [개념]

Spring Boot Integrated Deploy Pipeline은 React Build Output을 Spring Boot static resource에 복사한 뒤 Spring Boot JAR를 build하고 배포하는 CI/CD 방식이다.

---

### [핵심]

Pipeline 단계:

```text
Checkout
→ Setup Node
→ Frontend Install
→ Frontend Build
→ Copy Output to Backend Static
→ Setup Java
→ Backend Test
→ Spring Boot Build
→ Deploy JAR
→ Smoke Test
```

중요 확인:

- Vite `dist` / CRA `build` 구분
- static directory clean
- copy target
- JAR에 static resource 포함
- API prefix / fallback / security
- deploy server restart

---

### [실무]

CI 예:

```yaml
- name: Build Frontend
  working-directory: ./frontend
  env:
    REACT_APP_API_BASE_URL: /api
  run: |
    npm ci
    npm run build

- name: Copy Frontend to Backend Static
  run: |
    rm -rf backend/src/main/resources/static/*
    cp -r frontend/build/* backend/src/main/resources/static/

- name: Build Backend
  working-directory: ./backend
  run: ./gradlew clean build
```

Vite라면:

```bash
cp -r frontend/dist/* backend/src/main/resources/static/
```

---

### [FAQ]

Q. Spring Boot 통합 배포 CI/CD는 어떤 순서로 진행하는가?
A. Frontend build, static 복사, backend build, JAR 배포 순서로 진행한다.

Q. static 폴더를 비우고 복사해야 하는가?
A. 권장된다. 이전 asset이 남아 충돌할 수 있다.

Q. JAR 배포 전 무엇을 확인해야 하는가?
A. JAR에 최신 index.html과 JS/CSS가 포함되었는지 확인해야 한다.

Q. 통합 배포에서 API Base URL은 무엇이 적합한가?
A. 같은 서버에서 API를 제공한다면 `/api`가 단순하다.

---

# 7. Secrets and Variables

## 7.1 CI/CD Secret Rules

### [개념]

CI/CD Secret은 deploy token, cloud credential, registry password 같은 민감 정보를 CI/CD 도구의 Secret 저장소에 보관하는 방식이다.

---

### [핵심]

Secret 예:

```text
AWS_SECRET_ACCESS_KEY
VERCEL_TOKEN
NETLIFY_AUTH_TOKEN
DOCKER_REGISTRY_PASSWORD
SSH_PRIVATE_KEY
SENTRY_AUTH_TOKEN
```

중요 규칙:

- Secret을 repository에 commit하지 않는다.
- Secret을 frontend build env에 주입하지 않는다.
- log에 Secret을 출력하지 않는다.
- 최소 권한을 부여한다.
- 노출되면 즉시 폐기하고 재발급한다.
- PR from fork에서는 Secret 접근 제한을 고려한다.

---

### [실무]

GitHub Actions Secret 사용 예:

```yaml
env:
  DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

금지:

```yaml
env:
  VITE_AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```

위 값은 frontend bundle에 노출될 수 있다.

Secret Review Flow:

```text
workflow env 확인
→ frontend build step에 secret 주입 여부 확인
→ deploy step secret과 구분
→ log 출력 여부 확인
```

---

### [FAQ]

Q. CI/CD Secret은 무엇인가?
A. deploy token, cloud credential, registry password 같은 민감 정보를 저장하는 값이다.

Q. Secret을 frontend build env에 넣어도 되는가?
A. 안 된다. frontend build 결과물에 포함되어 브라우저에 노출될 수 있다.

Q. Secret은 어디에 저장해야 하는가?
A. GitHub Secrets, GitLab CI variables, 플랫폼 Secret 저장소 등에 저장해야 한다.

Q. Secret이 노출되면 어떻게 해야 하는가?
A. 즉시 폐기하고 새로 발급해야 한다.

---

## 7.2 Variables vs Secrets

### [개념]

Variables는 공개 가능하거나 민감하지 않은 설정값이고, Secrets는 노출되면 안 되는 민감 정보다.

---

### [핵심]

Variables 예:

```text
VITE_API_BASE_URL
REACT_APP_APP_ENV
S3_BUCKET
AWS_REGION
PUBLIC_MAP_KEY
```

Secrets 예:

```text
AWS_SECRET_ACCESS_KEY
OPENAI_API_KEY
JWT_SECRET
TOSS_SECRET_KEY
SSH_PRIVATE_KEY
DOCKER_PASSWORD
```

주의:

- `VITE_`, `REACT_APP_`로 시작하는 값은 브라우저에 노출될 수 있다.
- public key도 도메인 제한과 사용량 제한이 필요하다.
- deploy에 필요한 Secret과 frontend runtime config를 구분한다.

---

### [실무]

GitHub Actions 예:

```yaml
env:
  VITE_API_BASE_URL: ${{ vars.VITE_API_BASE_URL }}
  AWS_REGION: ${{ vars.AWS_REGION }}
```

Secret 사용:

```yaml
with:
  aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
  aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```

Agent 판단 기준:

```text
브라우저에 노출되어도 되는가?
→ Variable 가능

노출되면 비용/권한/보안 문제인가?
→ Secret

frontend build에 들어가는가?
→ Secret 금지
```

---

### [FAQ]

Q. Variables와 Secrets는 무엇이 다른가?
A. Variables는 민감하지 않은 설정값이고 Secrets는 노출되면 안 되는 값이다.

Q. API Base URL은 Secret인가?
A. 보통 Secret은 아니다. 공개 가능한 설정값이다.

Q. AWS Secret Access Key는 Variable인가?
A. 아니다. 반드시 Secret으로 관리해야 한다.

Q. Public Map Key는 Secret인가?
A. 브라우저용 public key일 수 있지만 도메인 제한과 사용량 제한이 필요하다.

---

# 8. Deployment Verification

## 8.1 Smoke Test Rules

### [개념]

Smoke Test는 배포 직후 서비스가 최소한의 핵심 기능을 정상 수행하는지 빠르게 확인하는 테스트다.

---

### [핵심]

Frontend Smoke Test 항목:

```md
- [ ] 메인 페이지 접속
- [ ] JS / CSS asset 200
- [ ] React route 직접 접근
- [ ] 새로고침 정상
- [ ] API health check
- [ ] API 응답 JSON
- [ ] 로그인 페이지 접근
- [ ] 인증 필요 API 401 정상
- [ ] HTTPS 정상
- [ ] Console Critical Error 없음
```

---

### [실무]

curl 기반 smoke test 예:

```bash
curl -I https://example.com/
curl -I https://example.com/login
curl -I https://example.com/assets/index.js
curl -I https://example.com/api/health
```

주의:

```text
SPA route /login은 200 text/html 가능
API /api/health는 JSON 또는 API status가 나와야 함
```

Browser 기반 확인:

```text
Console
→ runtime error 확인

Network
→ asset/API status 확인
```

---

### [FAQ]

Q. Smoke Test란 무엇인가?
A. 배포 직후 핵심 기능이 최소한 정상인지 빠르게 확인하는 테스트다.

Q. 프론트엔드 Smoke Test에서 가장 중요한 것은 무엇인가?
A. 메인 접속, asset 로드, route 새로고침, API 요청 확인이다.

Q. Smoke Test는 자동화할 수 있는가?
A. 가능하다. curl, Playwright, Cypress 등을 사용할 수 있다.

Q. Smoke Test 실패 시 어떻게 해야 하는가?
A. 배포 중단, rollback, log 확인을 진행해야 한다.

---

## 8.2 Post-deploy Network Verification

### [개념]

Post-deploy Network Verification은 배포 후 브라우저 Network 탭에서 실제 요청 URL, status, content-type을 확인하는 검증이다.

---

### [핵심]

확인 대상:

```md
- [ ] index.html status
- [ ] JS bundle status
- [ ] CSS bundle status
- [ ] image/font status
- [ ] API Request URL
- [ ] API Status Code
- [ ] API Content-Type
- [ ] Authorization Header
- [ ] Cookie
- [ ] CORS error
- [ ] Mixed Content
```

---

### [실무]

판단 기준:

```text
JS/CSS 404
→ output/base/hosting 문제

API localhost
→ production env 문제

API text/html
→ fallback/rewrite 문제

API 401
→ auth token/cookie 문제

Mixed Content
→ HTTP API 문제
```

Review Agent Flow:

```text
Production URL 접속
→ DevTools Network 열기
→ hard reload
→ asset 요청 확인
→ API 요청 확인
→ response body 확인
```

---

### [FAQ]

Q. 배포 후 Network 검증은 왜 필요한가?
A. 실제 브라우저가 어떤 파일과 API를 요청하는지 확인할 수 있기 때문이다.

Q. API 응답 Content-Type이 text/html이면 무엇을 의심하는가?
A. API 요청이 SPA fallback에 잡혀 index.html을 반환하는 문제를 의심한다.

Q. API Request URL이 localhost면 무엇이 문제인가?
A. Production env에 localhost가 남아 있거나 build env가 잘못된 것이다.

Q. JS/CSS 404는 무엇을 확인해야 하는가?
A. Output Directory, base path, hosting root, cache를 확인해야 한다.

---

# 9. Rollback Rules

## 9.1 Rollback Definition

### [개념]

Rollback은 배포 후 장애가 발생했을 때 이전 정상 버전으로 되돌리는 절차다.

---

### [핵심]

Rollback 대상:

```text
Platform previous deploy
S3 previous artifact
CloudFront cache
Docker previous image
Spring Boot previous JAR
Nginx previous static files
```

Rollback이 필요한 상황:

- Production White Screen
- API 전체 실패
- 로그인 불가
- Critical JS error
- 잘못된 API URL
- Secret 노출
- 데이터 손상 위험
- 배포 후 핵심 기능 장애

---

### [실무]

Docker rollback:

```text
previous image tag 확인
→ compose image tag 변경
→ docker compose up -d
→ smoke test
```

Platform rollback:

```text
platform dashboard
→ previous successful deploy 선택
→ rollback
→ smoke test
```

S3 rollback:

```text
previous artifact 복원
→ S3 sync
→ CloudFront invalidation
→ smoke test
```

---

### [FAQ]

Q. Rollback이란 무엇인가?
A. 장애가 발생한 배포를 이전 정상 버전으로 되돌리는 절차다.

Q. Rollback은 언제 필요한가?
A. 운영 장애, 흰 화면, API 전체 실패, 로그인 불가 같은 치명적 문제가 있을 때 필요하다.

Q. Docker rollback에는 무엇이 필요한가?
A. 이전 image tag가 필요하다.

Q. Rollback 후에도 무엇을 해야 하는가?
A. smoke test와 원인 분석을 해야 한다.

---

## 9.2 Rollback Readiness

### [개념]

Rollback Readiness는 장애 발생 시 빠르게 이전 버전으로 돌아갈 수 있도록 배포 전 준비해두는 기준이다.

---

### [핵심]

준비 항목:

```md
- [ ] 이전 정상 artifact 보관
- [ ] Docker image tag 기록
- [ ] 플랫폼 previous deploy 접근 가능
- [ ] S3 previous version 또는 artifact 보관
- [ ] DB migration rollback 전략 확인
- [ ] env 변경 이력 기록
- [ ] 배포 담당자와 절차 명확화
- [ ] smoke test 기준 존재
```

주의:

- 프론트엔드 rollback은 쉬운 편이다.
- DB schema 변경이 포함되면 rollback이 어려워질 수 있다.
- API contract 변경은 FE/BE 버전 호환성을 고려해야 한다.
- env 변경도 rollback 대상이다.

---

### [실무]

배포 기록 예:

```text
Release: 2026-07-07-01
Frontend Image: app-frontend:abc1234
Backend Image: app-backend:abc1234
API URL: https://api.example.com
Deploy Target: production
Smoke Test: pass
```

Agent 판단 기준:

```text
production deploy
→ rollback plan 필요

학원 demo deploy
→ 최소 previous build 보관 권장

DB migration 포함
→ backend rollback 전략 필수
```

---

### [FAQ]

Q. Rollback 준비는 왜 필요한가?
A. 장애가 발생했을 때 빠르게 이전 정상 상태로 돌아가기 위해 필요하다.

Q. 프론트엔드 rollback은 항상 쉬운가?
A. 정적 파일만 바뀐 경우 비교적 쉽지만 API contract나 DB 변경이 함께 있으면 어려울 수 있다.

Q. image tag 기록이 중요한 이유는?
A. 이전 정상 버전으로 정확히 되돌리기 위해 필요하다.

Q. env 변경도 rollback 대상인가?
A. 그렇다. 잘못된 env 값으로 장애가 발생할 수 있다.

---

# 10. CI/CD Troubleshooting

## 10.1 CI Build Failure

### [개념]

CI Build Failure는 pipeline에서 의존성 설치, lint, test, build 단계 중 실패가 발생하는 문제다.

---

### [핵심]

대표 원인:

- Root Directory 오류
- package manager 불일치
- lock file 누락
- Node version mismatch
- env 누락
- TypeScript error
- ESLint error
- test failure
- Linux 대소문자 문제
- memory 부족
- build script 없음

---

### [실무]

Troubleshooting Flow:

```text
CI log 첫 번째 error 확인
→ 실패 step 확인
→ root directory 확인
→ node version 확인
→ package manager 확인
→ env 확인
→ local clean build 재현
```

로컬 재현:

```bash
rm -rf node_modules
npm ci
npm run build
```

Linux 대소문자 예:

```text
import Header from "./Header";
actual file: header.jsx

Windows local
→ 동작 가능

Linux CI
→ 실패 가능
```

---

### [FAQ]

Q. CI Build Failure가 발생하면 무엇을 먼저 확인하는가?
A. CI log에서 첫 번째 실제 error와 실패 step을 확인한다.

Q. 로컬에서는 되는데 CI에서 실패하는 이유는?
A. Node version, Linux 대소문자, env, lock file, clean install 차이 때문일 수 있다.

Q. package manager 불일치는 어떻게 확인하는가?
A. lock file과 CI install command가 일치하는지 확인한다.

Q. CI에서만 import 오류가 나면 무엇을 확인하는가?
A. 파일명 대소문자 불일치를 확인해야 한다.

---

## 10.2 CI Env Failure

### [개념]

CI Env Failure는 CI/CD pipeline에서 필요한 환경 변수가 누락되거나 잘못된 값으로 주입되어 Build 또는 배포가 실패하는 문제다.

---

### [핵심]

대표 원인:

- env variable 이름 오타
- Vite / CRA prefix 불일치
- GitHub vars와 secrets 혼동
- environment scope 오류
- production env 누락
- preview env 누락
- Secret을 build step에 잘못 주입
- env 변경 후 pipeline 재실행 누락

---

### [실무]

Troubleshooting Flow:

```text
CI env 설정 확인
→ workflow env 이름 확인
→ Build Tool prefix 확인
→ environment scope 확인
→ build log 확인
→ 배포 후 Network API URL 확인
```

주의:

```yaml
env:
  VITE_API_BASE_URL: ${{ secrets.API_BASE_URL }}
```

API Base URL은 보통 secret일 필요가 없고 variable로 관리 가능하다.

금지:

```yaml
env:
  VITE_OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

---

### [FAQ]

Q. CI Env Failure란 무엇인가?
A. CI/CD 환경 변수 누락이나 오타로 build 또는 배포가 실패하는 문제다.

Q. Vite env가 CI에서 undefined인 이유는?
A. `VITE_` prefix가 없거나 workflow env 설정이 누락되었을 수 있다.

Q. CRA env가 CI에서 undefined인 이유는?
A. `REACT_APP_` prefix가 없거나 workflow env 설정이 누락되었을 수 있다.

Q. Secret을 frontend build step에 넣어도 되는가?
A. 안 된다. 브라우저 bundle에 노출될 수 있다.

---

## 10.3 Deployment Failure

### [개념]

Deployment Failure는 Build는 성공했지만 실제 배포 대상에 업로드, 실행, 반영, 검증이 실패하는 문제다.

---

### [핵심]

대표 원인:

- artifact path 오류
- output directory 오류
- deploy credential 오류
- cloud permission 부족
- S3 bucket 이름 오류
- Docker registry auth 실패
- server SSH 실패
- container recreate 누락
- platform deploy token 만료
- CloudFront invalidation 실패
- 배포 후 cache 문제

---

### [실무]

Troubleshooting Flow:

```text
Deploy step log 확인
→ credential 확인
→ target path 확인
→ artifact 존재 확인
→ permission 확인
→ deploy target 상태 확인
→ smoke test 확인
```

S3 실패:

```text
AccessDenied
→ IAM permission 확인

NoSuchBucket
→ bucket 이름/region 확인
```

Docker 실패:

```text
unauthorized
→ registry login 확인

old version running
→ container recreate 확인
```

---

### [FAQ]

Q. Build는 성공했는데 배포가 실패하면 무엇을 확인하는가?
A. deploy step log, artifact path, credential, target 권한을 확인한다.

Q. S3 AccessDenied는 무엇을 의미하는가?
A. CI credential에 S3 upload 권한이 부족하다는 의미다.

Q. Docker image push unauthorized는 무엇을 확인하는가?
A. registry login token과 repository 권한을 확인해야 한다.

Q. 배포 성공인데 이전 버전이 보이면 무엇을 확인하는가?
A. cache, container recreate, artifact path, CDN invalidation을 확인해야 한다.

---

## 10.4 Post-deploy Failure

### [개념]

Post-deploy Failure는 CI/CD는 성공했지만 실제 서비스 접속 후 화면, API, 라우팅, 인증 문제가 발생하는 상태다.

---

### [핵심]

대표 증상:

- Production White Screen
- JS / CSS 404
- Refresh 404
- API localhost 호출
- API CORS error
- API HTML response
- Mixed Content
- Login failure
- Cookie not saved
- Old version displayed

---

### [실무]

Troubleshooting Flow:

```text
Production URL 접속
→ Console 확인
→ Network 확인
→ asset status 확인
→ API URL 확인
→ API response 확인
→ cache 확인
→ rollback 여부 판단
```

판단 기준:

```text
White Screen
→ asset/runtime/env 확인

Refresh 404
→ fallback 확인

API localhost
→ production env 확인

API HTML
→ fallback/rewrite 확인

Mixed Content
→ HTTPS API 확인

Old version
→ cache/CDN/artifact 확인
```

---

### [FAQ]

Q. CI/CD가 성공했는데 서비스가 안 되면 무엇을 먼저 확인하는가?
A. 실제 Production URL에서 Console과 Network를 먼저 확인한다.

Q. Post-deploy Failure는 CI 문제인가 배포 문제인가?
A. 둘 다 가능하다. Build는 성공했지만 env, routing, cache, API 설정이 잘못될 수 있다.

Q. Post-deploy 문제가 심각하면 어떻게 해야 하는가?
A. rollback 기준에 따라 이전 정상 버전으로 되돌리고 원인을 분석해야 한다.

Q. API가 HTML을 반환하면 무엇을 확인해야 하는가?
A. SPA fallback 또는 platform rewrite가 API 요청을 잡고 있는지 확인해야 한다.

---

# 11. Agent Decision Rules

## 11.1 PM Agent Rules

### [개념]

PM Agent는 CI/CD 목적, branch 전략, deploy target, env 전략, 검증 기준, rollback 기준을 정의해야 한다.

---

### [핵심]

PM Agent 확인 항목:

- CI/CD 목적
- Branch Strategy
- Target Environment
- Build Tool
- Package Manager
- Node Version
- Test / Lint 범위
- Build Command
- Output Directory
- Deploy Target
- Environment Variables
- Secrets Scope
- Smoke Test 기준
- Rollback 기준

---

### [실무]

PM Agent 산출물 예:

```text
CI/CD Target: Frontend Deploy
Branch:
- PR to develop: lint/test/build
- push develop: staging deploy
- push main: production deploy

Build Tool: Vite
Package Manager: npm
Node: 20
Build Command: npm run build
Output: dist

Env:
- staging VITE_API_BASE_URL
- production VITE_API_BASE_URL

Deploy Target: Netlify
Verification:
- /
- /login refresh
- API health
- Network asset 200

Rollback:
- previous platform deploy
```

PM Agent 판단 Flow:

```text
프로젝트 배포 목적 확인
→ branch/environment 전략 정의
→ pipeline 단계 정의
→ env/secret 분리
→ deploy target 정의
→ verification/rollback 기준 작성
```

---

### [FAQ]

Q. PM Agent는 CI/CD에서 무엇을 정해야 하는가?
A. branch 전략, pipeline 단계, deploy target, env, secret, 검증, rollback 기준을 정해야 한다.

Q. PM Agent가 production 배포 조건을 정해야 하는가?
A. 그렇다. main branch, tag, manual approval 같은 기준이 필요하다.

Q. PM Agent가 rollback 기준도 정해야 하는가?
A. 그렇다. 장애 발생 시 빠르게 복구하려면 기준과 절차가 필요하다.

Q. PM Agent가 smoke test 항목을 작성해야 하는가?
A. 그렇다. 배포 후 최소 검증 범위를 명확히 해야 한다.

---

## 11.2 Frontend Agent Rules

### [개념]

Frontend Agent는 CI/CD에서 안정적으로 build/test가 가능하도록 package scripts, env validation, output 구조를 관리해야 한다.

---

### [핵심]

Frontend Agent 필수 기준:

- `npm run build` 정상화
- lint / test / type-check scripts 관리
- Build Tool별 output directory 명확화
- env validation 구현
- 운영 localhost fallback 금지
- Secret을 frontend env에 요구하지 않음
- Linux 대소문자 import 오류 방지
- CI에서 동작 가능한 test command 제공
- build warning / error 관리

---

### [실무]

package.json 예:

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint src",
    "type-check": "tsc --noEmit",
    "test": "vitest run"
  }
}
```

Frontend Agent 검증 기준:

```text
local clean install
→ npm ci
→ npm run lint
→ npm run test
→ npm run build
```

주의:

```text
로컬 dev server 정상
≠
CI production build 정상
```

---

### [FAQ]

Q. Frontend Agent는 CI/CD를 위해 무엇을 준비해야 하는가?
A. build, lint, test, type-check scripts와 env validation을 준비해야 한다.

Q. 로컬 dev server가 되면 CI build도 된다고 볼 수 있는가?
A. 아니다. production build는 더 엄격한 오류를 잡을 수 있다.

Q. CI에서 파일명 대소문자 오류가 나는 이유는?
A. Linux 환경은 파일명 대소문자를 구분하기 때문이다.

Q. Frontend Agent가 Secret을 요구하면 되는가?
A. 안 된다. frontend build에는 Secret을 요구하면 안 된다.

---

## 11.3 DevOps Agent Rules

### [개념]

DevOps Agent는 CI/CD workflow, secret 관리, deploy command, artifact, cache, rollback 절차를 구현해야 한다.

---

### [핵심]

DevOps Agent 필수 기준:

- GitHub Actions / CI workflow 작성
- checkout / setup-node / install / build 단계 구성
- package manager와 lock file 일치
- dependency cache 설정
- env / secrets 분리
- artifact upload / download
- deploy target 설정
- Docker image build/push
- S3 sync / CloudFront invalidation
- platform deploy command
- smoke test 자동화
- rollback 절차 문서화

---

### [실무]

DevOps Agent 구현 Flow:

```text
workflow trigger 정의
→ Node/Java/Docker 환경 설정
→ install/build/test 단계 작성
→ artifact 처리
→ deploy step 작성
→ smoke test 작성
→ rollback 절차 기록
```

기본 검증:

```text
CI log 확인
→ deploy log 확인
→ production URL smoke test
→ rollback 가능 여부 확인
```

---

### [FAQ]

Q. DevOps Agent는 CI/CD에서 무엇을 구현해야 하는가?
A. workflow, env/secret 관리, artifact, deploy, smoke test, rollback 절차를 구현해야 한다.

Q. DevOps Agent가 cache를 설정해야 하는가?
A. 가능하다. dependency install 속도를 줄이기 위해 cache를 설정할 수 있다.

Q. DevOps Agent가 rollback도 문서화해야 하는가?
A. 운영 배포라면 반드시 문서화하는 것이 좋다.

Q. DevOps Agent가 deploy log를 확인해야 하는가?
A. 해야 한다. build와 deploy 실패 원인을 확인하는 핵심 자료다.

---

## 11.4 Review Agent Rules

### [개념]

Review Agent는 CI/CD pipeline이 재현 가능하고 안전하며 배포 후 검증 가능한지 검토해야 한다.

---

### [핵심]

Review Agent Checklist:

```md
- [ ] trigger가 적절한가?
- [ ] branch별 동작이 명확한가?
- [ ] package manager와 lock file이 일치하는가?
- [ ] Node version이 명시되어 있는가?
- [ ] install command가 재현 가능한가?
- [ ] lint/test/build 단계가 있는가?
- [ ] Build Tool별 output directory가 맞는가?
- [ ] env prefix가 맞는가?
- [ ] Secret이 frontend build에 주입되지 않는가?
- [ ] artifact path가 맞는가?
- [ ] deploy target이 맞는가?
- [ ] production deploy 조건이 안전한가?
- [ ] smoke test가 있는가?
- [ ] rollback 전략이 있는가?
```

---

### [실무]

Review Agent 판단 Flow:

```text
workflow 파일 확인
→ trigger 확인
→ install/build step 확인
→ env/secret 확인
→ artifact/deploy path 확인
→ deploy condition 확인
→ log 기반 실패 가능성 검토
```

Critical Issue:

```text
Secret이 VITE_/REACT_APP_로 주입됨
production env에 localhost
output directory 오류
main 외 branch에서 production deploy
artifact path 없음
deploy credential 노출
rollback 불가
```

승인 기준:

```text
재현 가능한 install
Build 성공
Env 안전
Artifact 정확
Deploy 조건 명확
Smoke Test 가능
Rollback 가능
```

---

### [FAQ]

Q. Review Agent는 CI/CD에서 무엇을 가장 먼저 확인해야 하는가?
A. trigger, package manager, build command, env/secret, output directory를 먼저 확인해야 한다.

Q. Secret이 VITE*나 REACT_APP*로 주입되면 승인 가능한가?
A. 아니다. 브라우저 bundle에 노출될 수 있다.

Q. production deploy가 모든 branch에서 실행되면 승인 가능한가?
A. 아니다. production deploy 조건을 제한해야 한다.

Q. artifact path가 틀리면 어떤 문제가 생기는가?
A. 잘못된 파일을 배포하거나 빈 배포가 발생할 수 있다.

---

# 12. Common Mistakes

## 12.1 CI/CD Common Mistakes

### [개념]

CI/CD Common Mistakes는 프론트엔드 자동 Build와 배포 과정에서 반복적으로 발생하는 설정, env, artifact, 검증 실수다.

---

### [핵심]

자주 발생하는 실수:

- Root Directory 미설정
- working-directory 누락
- package manager와 lock file 불일치
- `npm install`과 lock file 재현성 혼동
- Node version 미명시
- Vite `dist` 대신 CRA `build` 사용
- CRA `build` 대신 Vite `dist` 사용
- env prefix 불일치
- production env에 localhost 사용
- Secret을 frontend build env에 주입
- deploy token을 log에 출력
- artifact path 오류
- build success만 믿고 output 검증 없음
- 모든 branch에서 production deploy
- Preview가 Production API 호출
- smoke test 없음
- CloudFront invalidation 누락
- Docker image build 후 container recreate 누락
- `latest` tag만 사용
- rollback plan 없음
- CI log의 첫 번째 error를 보지 않음

---

### [실무]

실수별 판단:

```text
CI package.json not found
→ Root Directory / working-directory 확인

Build success but deploy fail
→ artifact path / deploy target 확인

API localhost
→ production env 확인

Secret 노출
→ workflow env와 frontend prefix 확인

Old version
→ cache / invalidation / container recreate 확인

Production 장애
→ smoke test / rollback 기준 확인
```

---

### [FAQ]

Q. CI/CD에서 가장 흔한 실수는 무엇인가?
A. Root Directory, package manager, output directory, env 설정을 잘못하는 것이다.

Q. CI/CD에서 가장 치명적인 실수는 무엇인가?
A. Secret을 frontend build에 주입하거나 production env에 localhost를 남기는 것이다.

Q. Build 성공인데 배포가 실패하는 이유는?
A. artifact path, output directory, deploy credential, deploy target이 잘못되었을 수 있다.

Q. CI/CD에서 rollback plan이 왜 필요한가?
A. 배포 후 장애 발생 시 빠르게 이전 정상 버전으로 복구하기 위해 필요하다.

---

# 13. Part11 Quality Checklist

## 13.1 Document Quality

### [개념]

이 문서는 Frontend Build & Deploy Domain의 Part11이며 CI/CD Rules Retrieval에 최적화되어야 한다.

---

### [핵심]

문서 품질 기준:

- CI/CD 정의 포함
- CI와 CD 구분 포함
- Frontend Pipeline Steps 포함
- Branch-based Pipeline 포함
- Environment-based Pipeline 포함
- Package Manager Rules 포함
- Dependency Cache Rules 포함
- CI Build Command Rules 포함
- Type Check / Lint Rules 포함
- Test Rules 포함
- Build Artifact Rules 포함
- Deploy Output Verification 포함
- Platform Deploy Pipeline 포함
- S3 CloudFront Deploy Pipeline 포함
- Docker Image Deploy Pipeline 포함
- Spring Boot Integrated Deploy Pipeline 포함
- Secrets and Variables 포함
- Smoke Test Rules 포함
- Rollback Rules 포함
- CI/CD Troubleshooting 포함
- Agent별 판단 기준 포함
- Common Mistakes 포함
- Retrieval Queries 포함

---

### [실무]

Part11은 다음 문서와 연결된다.

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

Q. Part11의 핵심 목적은 무엇인가?
A. 프론트엔드 Build와 Deploy 자동화에서 pipeline, env, artifact, secret, smoke test, rollback 문제를 Agent가 정확히 판단하게 하는 것이다.

Q. Part11에서 특정 플랫폼의 상세 설정만 다루는가?
A. 아니다. 플랫폼, S3/CloudFront, Docker, Spring Boot 통합 배포의 CI/CD 공통 원칙을 다룬다.

Q. Part11 다음 문서는 무엇인가?
A. Part12 Deployment Verification & Troubleshooting으로 이어지는 것이 적합하다.

---

# Retrieval Queries

### [FAQ]

Q. CI/CD란 무엇인가?
A. 코드 변경 후 Build, Test, 배포 과정을 자동화하는 프로세스다.

Q. 프론트엔드 CI/CD에서 가장 중요한 단계는 무엇인가?
A. 의존성 설치, Build, 환경 변수 주입, 배포 결과 검증이다.

Q. CI와 CD는 무엇이 다른가?
A. CI는 코드 통합 검증이고, CD는 검증된 결과물을 배포하는 과정이다.

Q. PR에서는 배포까지 해야 하는가?
A. 보통 PR에서는 CI 검증을 하고, 필요하면 Preview Deploy를 만든다.

Q. 프론트엔드 CI/CD Pipeline의 기본 단계는 무엇인가?
A. checkout, setup node, install, lint/test, build, deploy, smoke test다.

Q. Branch-based Pipeline이란 무엇인가?
A. branch 종류에 따라 build, test, staging deploy, production deploy를 다르게 실행하는 방식이다.

Q. feature branch에서 production 배포해도 되는가?
A. 일반적으로 안 된다. feature branch는 CI 검증 중심이 적합하다.

Q. Environment-based Pipeline이란 무엇인가?
A. 개발, 스테이징, 운영 환경별로 다른 설정과 배포 대상을 사용하는 pipeline이다.

Q. staging과 production은 왜 분리하는가?
A. 운영 배포 전 실제와 유사한 환경에서 검증하기 위해 분리한다.

Q. CI에서 npm install보다 npm ci가 좋은 이유는?
A. lock file 기준으로 재현 가능한 설치를 수행하기 때문이다.

Q. package manager는 어떻게 결정하는가?
A. package-lock.json은 npm, yarn.lock은 yarn, pnpm-lock.yaml은 pnpm 기준으로 판단한다.

Q. lock file은 Git에 올려야 하는가?
A. 일반적으로 올려야 한다. CI 재현성을 위해 필요하다.

Q. Dependency Cache는 왜 사용하는가?
A. CI에서 의존성 설치 시간을 줄이기 위해 사용한다.

Q. cache가 있으면 npm ci가 필요 없는가?
A. 아니다. cache는 다운로드 속도 최적화이고 설치 명령은 여전히 필요하다.

Q. CI에서 Build Command는 무엇인가?
A. 배포 가능한 정적 파일을 생성하기 위해 실행하는 명령이다.

Q. Vite와 CRA의 CI Build Command는 같은가?
A. 보통 `npm run build`로 같지만 결과 폴더는 Vite `dist`, CRA `build`로 다르다.

Q. CI Build에서 env가 필요한 이유는?
A. API Base URL 같은 Build-time 설정이 필요하기 때문이다.

Q. CI에서 lint는 왜 실행하는가?
A. 코드 품질과 잠재 오류를 배포 전에 잡기 위해 실행한다.

Q. TypeScript 프로젝트에서 type-check가 필요한가?
A. 권장된다. 타입 오류를 build 또는 배포 전에 발견할 수 있다.

Q. 프론트엔드 CI에서 테스트는 왜 필요한가?
A. 배포 전에 기능 오류를 자동으로 발견하기 위해 필요하다.

Q. 테스트가 없으면 CI/CD를 만들 수 없는가?
A. 만들 수 있다. 최소한 build 검증부터 시작할 수 있다.

Q. Build Artifact란 무엇인가?
A. CI에서 생성된 배포 가능한 결과물이다.

Q. 프론트엔드 Artifact는 보통 무엇인가?
A. Vite는 `dist`, CRA는 `build` 폴더다.

Q. Artifact에 Secret이 포함되어도 되는가?
A. 안 된다. 배포 결과물은 외부에 노출될 수 있다.

Q. Build가 성공했는데 output 검증이 필요한가?
A. 필요하다. 배포 설정이 잘못된 경로를 참조할 수 있기 때문이다.

Q. Vite output 검증은 무엇을 확인하는가?
A. `dist/index.html`과 `dist/assets`를 확인한다.

Q. CRA output 검증은 무엇을 확인하는가?
A. `build/index.html`과 `build/static`을 확인한다.

Q. 플랫폼 배포는 CI/CD가 따로 필요 없는가?
A. 플랫폼 자체가 CI/CD 역할을 할 수 있다. 별도 GitHub Actions는 필요에 따라 추가한다.

Q. S3 CloudFront CI/CD는 어떤 순서로 진행하는가?
A. Build, output 검증, S3 sync, CloudFront invalidation, smoke test 순서로 진행한다.

Q. AWS Secret을 frontend env에 넣어도 되는가?
A. 안 된다. AWS Secret은 deploy step에서만 사용해야 한다.

Q. Docker Image Deploy Pipeline은 무엇인가?
A. Docker image를 build/push하고 서버에서 pull하여 컨테이너를 재실행하는 배포 방식이다.

Q. image tag는 무엇을 쓰는 것이 좋은가?
A. commit sha, semantic version, release tag를 사용하는 것이 추적과 rollback에 좋다.

Q. Spring Boot 통합 배포 CI/CD는 어떤 순서로 진행하는가?
A. Frontend build, static 복사, backend build, JAR 배포 순서로 진행한다.

Q. CI/CD Secret은 무엇인가?
A. deploy token, cloud credential, registry password 같은 민감 정보를 저장하는 값이다.

Q. Secret을 frontend build env에 넣어도 되는가?
A. 안 된다. frontend build 결과물에 포함되어 브라우저에 노출될 수 있다.

Q. Variables와 Secrets는 무엇이 다른가?
A. Variables는 민감하지 않은 설정값이고 Secrets는 노출되면 안 되는 값이다.

Q. API Base URL은 Secret인가?
A. 보통 Secret은 아니다. 공개 가능한 설정값이다.

Q. Smoke Test란 무엇인가?
A. 배포 직후 핵심 기능이 최소한 정상인지 빠르게 확인하는 테스트다.

Q. 프론트엔드 Smoke Test에서 가장 중요한 것은 무엇인가?
A. 메인 접속, asset 로드, route 새로고침, API 요청 확인이다.

Q. 배포 후 Network 검증은 왜 필요한가?
A. 실제 브라우저가 어떤 파일과 API를 요청하는지 확인할 수 있기 때문이다.

Q. API 응답 Content-Type이 text/html이면 무엇을 의심하는가?
A. API 요청이 SPA fallback에 잡혀 index.html을 반환하는 문제를 의심한다.

Q. Rollback이란 무엇인가?
A. 장애가 발생한 배포를 이전 정상 버전으로 되돌리는 절차다.

Q. Rollback은 언제 필요한가?
A. 운영 장애, 흰 화면, API 전체 실패, 로그인 불가 같은 치명적 문제가 있을 때 필요하다.

Q. Rollback 준비는 왜 필요한가?
A. 장애가 발생했을 때 빠르게 이전 정상 상태로 돌아가기 위해 필요하다.

Q. CI Build Failure가 발생하면 무엇을 먼저 확인하는가?
A. CI log에서 첫 번째 실제 error와 실패 step을 확인한다.

Q. 로컬에서는 되는데 CI에서 실패하는 이유는?
A. Node version, Linux 대소문자, env, lock file, clean install 차이 때문일 수 있다.

Q. CI Env Failure란 무엇인가?
A. CI/CD 환경 변수 누락이나 오타로 build 또는 배포가 실패하는 문제다.

Q. Vite env가 CI에서 undefined인 이유는?
A. `VITE_` prefix가 없거나 workflow env 설정이 누락되었을 수 있다.

Q. CRA env가 CI에서 undefined인 이유는?
A. `REACT_APP_` prefix가 없거나 workflow env 설정이 누락되었을 수 있다.

Q. Build는 성공했는데 배포가 실패하면 무엇을 확인하는가?
A. deploy step log, artifact path, credential, target 권한을 확인한다.

Q. CI/CD가 성공했는데 서비스가 안 되면 무엇을 먼저 확인하는가?
A. 실제 Production URL에서 Console과 Network를 먼저 확인한다.

Q. PM Agent는 CI/CD에서 무엇을 정해야 하는가?
A. branch 전략, pipeline 단계, deploy target, env, secret, 검증, rollback 기준을 정해야 한다.

Q. Frontend Agent는 CI/CD를 위해 무엇을 준비해야 하는가?
A. build, lint, test, type-check scripts와 env validation을 준비해야 한다.

Q. DevOps Agent는 CI/CD에서 무엇을 구현해야 하는가?
A. workflow, env/secret 관리, artifact, deploy, smoke test, rollback 절차를 구현해야 한다.

Q. Review Agent는 CI/CD에서 무엇을 가장 먼저 확인해야 하는가?
A. trigger, package manager, build command, env/secret, output directory를 먼저 확인해야 한다.

Q. CI/CD에서 가장 흔한 실수는 무엇인가?
A. Root Directory, package manager, output directory, env 설정을 잘못하는 것이다.

Q. CI/CD에서 가장 치명적인 실수는 무엇인가?
A. Secret을 frontend build에 주입하거나 production env에 localhost를 남기는 것이다.

Q. Part11 다음 문서는 무엇인가?
A. Part12 Deployment Verification & Troubleshooting으로 이어지는 것이 적합하다.
