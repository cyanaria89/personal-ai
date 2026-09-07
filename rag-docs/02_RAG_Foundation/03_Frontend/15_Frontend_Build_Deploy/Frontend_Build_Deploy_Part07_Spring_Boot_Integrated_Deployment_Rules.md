# Frontend Build & Deploy Part07 - Spring Boot Integrated Deployment Rules

---

# 1. Spring Boot Integrated Deployment Core

## 1.1 Spring Boot Integrated Deployment Definition

### [개념]

Spring Boot Integrated Deployment는 React Build 결과물을 Spring Boot 애플리케이션의 static resource로 포함하여 하나의 Spring Boot 서버가 프론트엔드 정적 파일과 백엔드 API를 함께 제공하는 배포 방식이다.

기본 구조:

```text
React Source Code
→ npm run build
→ build or dist 생성
→ Spring Boot static resource 경로에 복사
→ Spring Boot JAR build
→ Server run
→ Browser receives index.html
→ Browser calls Backend API
```

---

### [핵심]

Spring Boot 통합 배포 핵심 규칙:

- React Build Output을 Spring Boot static resource 경로에 복사한다.
- CRA는 `build` 내부 파일을 사용한다.
- Vite는 `dist` 내부 파일을 사용한다.
- `index.html`은 static root에서 제공되어야 한다.
- API path와 React route path를 분리해야 한다.
- React Router BrowserRouter 사용 시 SPA fallback이 필요할 수 있다.
- Spring Security가 static resource 접근을 막지 않아야 한다.
- API 요청이 `index.html`로 fallback되면 안 된다.
- 정적 asset 요청이 `index.html`로 fallback되면 안 된다.
- 통합 배포는 학원 프로젝트 / 데모 / 소규모 서비스에 단순하다.

---

### [실무]

2026 실무 기준으로 학원 프로젝트나 빠른 시연 목적에서는 Spring Boot 통합 배포가 실용적이다.

장점:

```text
서버 하나로 배포 가능
CORS 복잡도 감소
도메인 관리 단순
발표 / 데모 환경 구성 쉬움
프론트엔드와 백엔드 버전 동기화 쉬움
```

단점:

```text
프론트엔드 독립 배포 어려움
프론트 수정만으로도 백엔드 재배포 필요 가능
CDN 최적화 제한
대규모 운영에는 분리 배포가 더 적합할 수 있음
배포 파이프라인 결합
```

Agent 판단 Flow:

```text
프로젝트 목적 확인
→ React Build Tool 확인
→ Build Output 확인
→ Spring Boot static path 확인
→ API prefix 확인
→ SPA fallback 필요 여부 확인
→ Security static 허용 확인
→ 통합 배포 적합성 판단
```

---

### [FAQ]

Q. Spring Boot Integrated Deployment란 무엇인가?
A. React Build 결과물을 Spring Boot static resource에 포함해 하나의 Spring Boot 서버에서 프론트엔드와 백엔드를 함께 제공하는 방식이다.

Q. 학원 프로젝트에서 Spring Boot 통합 배포를 써도 되는가?
A. 괜찮다. 발표와 데모 목적에서는 서버 하나로 관리할 수 있어 단순하고 실용적이다.

Q. 실무에서도 Spring Boot 통합 배포를 사용하는가?
A. 소규모 서비스에서는 가능하다. 규모가 커지면 프론트엔드와 백엔드를 분리 배포하는 경우가 많다.

Q. Spring Boot 통합 배포에서 가장 중요한 것은 무엇인가?
A. Build Output 위치, SPA fallback, API path 분리, Security static 허용을 정확히 설정하는 것이다.

---

## 1.2 Integrated Deployment Decision Criteria

### [개념]

Integrated Deployment Decision Criteria는 Spring Boot 통합 배포가 적합한지 판단하는 기준이다.

---

### [핵심]

통합 배포가 적합한 경우:

```text
학원 프로젝트
포트폴리오 데모
소규모 서비스
단일 서버 운영
CORS 설정 최소화 필요
빠른 발표 / 시연
프론트엔드와 백엔드 배포 주기 동일
```

통합 배포가 부적합한 경우:

```text
프론트엔드 독립 배포 필요
프론트엔드만 자주 수정
CDN 최적화 필요
대규모 트래픽
여러 프론트엔드 앱 운영
Blue-Green / Canary 배포 필요
프론트엔드와 백엔드 배포 주기 다름
```

---

### [실무]

2026 실무 기준으로 통합 배포는 단순성과 운영 편의성이 장점이고, 확장성과 독립 배포성이 약점이다.

선택 Flow:

```text
발표 / 데모 / 소규모
→ Spring Boot 통합 배포 가능

프론트엔드 독립 운영 / CDN 필요
→ Nginx / Vercel / Netlify / S3 + CloudFront 고려

컨테이너 기반 단일 배포
→ Docker + Nginx 또는 Spring Boot 통합 배포 비교
```

PM Agent 판단 기준:

```text
배포 목적
→ 데모인가 운영인가

운영 규모
→ 소규모인가 대규모인가

배포 주기
→ FE/BE 함께 배포 가능한가

인프라 역량
→ 별도 Nginx/CDN 운영 가능한가
```

---

### [FAQ]

Q. Spring Boot 통합 배포는 언제 적합한가?
A. 학원 프로젝트, 데모, 소규모 서비스, 단일 서버 운영처럼 단순성이 중요한 경우 적합하다.

Q. Spring Boot 통합 배포가 부적합한 경우는?
A. 프론트엔드 독립 배포, CDN 최적화, 대규모 운영, 배포 주기 분리가 필요한 경우 부적합할 수 있다.

Q. 발표용 프로젝트에서는 통합 배포가 좋은가?
A. 좋다. CORS와 서버 구성이 단순해져 시연 안정성을 확보하기 쉽다.

Q. 운영 서비스는 무조건 분리 배포해야 하는가?
A. 아니다. 규모와 요구사항에 따라 통합 배포도 가능하지만 확장성과 독립 배포성을 고려해야 한다.

---

# 2. Static Resource Path

## 2.1 Spring Boot Static Resource Path

### [개념]

Spring Boot Static Resource Path는 Spring Boot가 HTML, CSS, JavaScript, 이미지 같은 정적 파일을 제공하는 기본 경로다.

대표 경로:

```text
src/main/resources/static
src/main/resources/public
src/main/resources/resources
src/main/resources/META-INF/resources
```

React 통합 배포에서는 보통 다음 경로를 사용한다.

```text
src/main/resources/static
```

---

### [핵심]

Spring Boot static resource 핵심 규칙:

- `index.html`은 static root에 있어야 한다.
- JS / CSS / asset 폴더 구조를 유지해야 한다.
- Build Output 폴더 자체를 한 단계 더 넣지 않도록 주의한다.
- Spring Boot JAR build 시 static resource가 포함되어야 한다.
- `target/classes/static` 또는 `build/resources/main/static`에 복사되는지 확인한다.
- Security 설정이 static resource 요청을 막지 않아야 한다.

---

### [실무]

정상 구조:

```tex
backend/
└─ src/main/resources/static/
   ├─ index.html
   ├─ assets/
   └─ favicon.ico
```

CRA 정상 구조:

```text
backend/
└─ src/main/resources/static/
   ├─ index.html
   ├─ static/
   │  ├─ js/
   │  └─ css/
   ├─ favicon.ico
   └─ manifest.json
```

비정상 구조:

```text
backend/
└─ src/main/resources/static/
   └─ build/
      ├─ index.html
      └─ static/
```

위 구조는 `/` 요청에서 `index.html`을 찾지 못할 수 있다.

검증 Flow:

```text
React build output 확인
→ static root 확인
→ index.html 위치 확인
→ assets/static 폴더 확인
→ Spring Boot run
→ / 접속 확인
```

---

### [FAQ]

Q. Spring Boot static resource 기본 경로는 어디인가?
A. 일반적으로 `src/main/resources/static`을 사용한다.

Q. React index.html은 어디에 있어야 하는가?
A. 보통 `src/main/resources/static/index.html` 위치에 있어야 한다.

Q. build 폴더 자체를 static 안에 넣어도 되는가?
A. 대부분 권장하지 않는다. build 또는 dist 내부 파일이 static root에 위치해야 한다.

Q. static 파일이 JAR에 포함되었는지는 어떻게 확인하는가?
A. build 후 `target/classes/static` 또는 `build/resources/main/static`에 파일이 있는지 확인한다.

---

## 2.2 Vite Dist Copy Rules

### [개념]

Vite Dist Copy Rules는 Vite Build 결과물인 `dist` 내부 파일을 Spring Boot static root로 복사하는 규칙이다.

---

### [핵심]

Vite 기준:

```text
Build Command: npm run build
Output Directory: dist
Copy Source: frontend/dist/*
Copy Target: backend/src/main/resources/static/
```

복사 후 구조:

```text
backend/src/main/resources/static/index.html
backend/src/main/resources/static/assets/
```

주의:

- `dist` 폴더 자체를 static 내부에 넣지 않는다.
- `dist` 내부 파일을 static root로 복사한다.
- Vite `base` 설정이 `/`인지 확인한다.
- 하위 경로 배포면 `base`와 Router `basename`을 함께 검토한다.
- 기존 static 파일과 충돌 가능성을 확인한다.

---

### [실무]

수동 복사 예:

```bash
cd frontend
npm run build

rm -rf ../backend/src/main/resources/static/*
cp -r dist/* ../backend/src/main/resources/static/
```

Windows PowerShell 예:

```powershell
cd frontend
npm run build

Remove-Item -Recurse -Force ..\backend\src\main\resources\static\*
Copy-Item -Recurse .\dist\* ..\backend\src\main\resources\static\
```

검증 Flow:

```text
npm run build
→ dist/index.html 확인
→ dist/assets 확인
→ static root로 복사
→ Spring Boot 실행
→ / 접속
→ /assets/*.js 200 확인
```

---

### [FAQ]

Q. Vite Build 결과물은 Spring Boot 어디에 복사하는가?
A. `frontend/dist/*` 내부 파일을 `backend/src/main/resources/static/`로 복사한다.

Q. dist 폴더 자체를 static에 넣어도 되는가?
A. 권장하지 않는다. `dist/index.html`이 아니라 `static/index.html` 구조가 되어야 한다.

Q. Vite 통합 배포에서 asset 404가 나면 무엇을 확인하는가?
A. `dist/assets` 복사 여부, Vite `base`, static root 위치를 확인한다.

Q. Vite base는 Spring Boot 통합 배포에서 어떻게 설정하는가?
A. 루트 배포라면 보통 `base: "/"`가 적합하다.

---

## 2.3 CRA Build Copy Rules

### [개념]

CRA Build Copy Rules는 CRA Build 결과물인 `build` 내부 파일을 Spring Boot static root로 복사하는 규칙이다.

---

### [핵심]

CRA 기준:

```text
Build Command: npm run build
Output Directory: build
Copy Source: frontend/build/*
Copy Target: backend/src/main/resources/static/
```

복사 후 구조:

```text
backend/src/main/resources/static/index.html
backend/src/main/resources/static/static/js/
backend/src/main/resources/static/static/css/
```

주의:

- `build` 폴더 자체를 static 내부에 넣지 않는다.
- `build` 내부 파일을 static root로 복사한다.
- CRA `homepage` 설정이 배포 경로와 맞는지 확인한다.
- 기존 static 파일과 충돌 가능성을 확인한다.
- manifest, favicon, asset-manifest 파일 복사 여부를 확인한다.

---

### [실무]

수동 복사 예:

```bash
cd frontend
npm run build

rm -rf ../backend/src/main/resources/static/*
cp -r build/* ../backend/src/main/resources/static/
```

Windows PowerShell 예:

```powershell
cd frontend
npm run build

Remove-Item -Recurse -Force ..\backend\src\main\resources\static\*
Copy-Item -Recurse .\build\* ..\backend\src\main\resources\static\
```

검증 Flow:

```text
npm run build
→ build/index.html 확인
→ build/static 확인
→ Spring Boot static root로 복사
→ Spring Boot 실행
→ / 접속
→ /static/js/*.js 200 확인
```

---

### [FAQ]

Q. CRA Build 결과물은 Spring Boot 어디에 복사하는가?
A. `frontend/build/*` 내부 파일을 `backend/src/main/resources/static/`로 복사한다.

Q. build 폴더 자체를 static에 넣어도 되는가?
A. 권장하지 않는다. `static/build/index.html` 구조가 되면 루트 요청에서 index.html을 못 찾을 수 있다.

Q. CRA 통합 배포에서 CSS가 안 먹으면 무엇을 확인하는가?
A. `build/static/css` 복사 여부, CRA `homepage`, static root 위치를 확인한다.

Q. CRA 통합 배포에서 homepage 설정은 언제 필요한가?
A. 루트가 아닌 하위 경로 배포일 때 필요할 수 있다.

---

# 3. Build Pipeline Integration

## 3.1 Manual Build and Copy Flow

### [개념]

Manual Build and Copy Flow는 프론트엔드 Build를 수동 실행한 뒤 결과물을 Spring Boot static resource에 복사하는 가장 단순한 통합 배포 방식이다.

---

### [핵심]

Manual Flow:

```text
Frontend npm/yarn install
→ npm run build
→ dist/build 생성
→ backend static root 정리
→ Build Output 내부 파일 복사
→ Spring Boot build
→ JAR 실행
```

장점:

- 이해하기 쉽다.
- 학원 프로젝트에 적합하다.
- 문제 발생 지점을 직접 확인하기 쉽다.
- 자동화 없이 빠르게 시연 가능하다.

단점:

- 사람이 복사를 빼먹을 수 있다.
- 오래된 Build Output이 남을 수 있다.
- 팀원마다 방식이 달라질 수 있다.
- CI/CD에는 자동화가 필요하다.

---

### [실무]

수동 통합 배포 Flow:

```bash
# 1. frontend build
cd frontend
npm install
npm run build

# 2. copy build output to backend static
rm -rf ../backend/src/main/resources/static/*
cp -r build/* ../backend/src/main/resources/static/

# 3. backend build
cd ../backend
./gradlew clean build

# 4. run jar
java -jar build/libs/app.jar
```

Vite라면:

```bash
cp -r dist/* ../backend/src/main/resources/static/
```

CRA라면:

```bash
cp -r build/* ../backend/src/main/resources/static/
```

Review 기준:

```md
- [ ] 복사 전 기존 static 파일을 정리했는가?
- [ ] 올바른 output directory를 복사했는가?
- [ ] index.html이 static root에 있는가?
- [ ] Spring Boot build 후 static resource가 포함되었는가?
```

---

### [FAQ]

Q. Manual Build and Copy Flow란 무엇인가?
A. React Build 결과물을 수동으로 Spring Boot static 폴더에 복사한 뒤 Spring Boot를 빌드하는 방식이다.

Q. 수동 복사 방식은 학원 프로젝트에서 괜찮은가?
A. 괜찮다. 단순하고 문제 원인을 직접 확인하기 쉽다.

Q. 수동 복사 방식의 위험은 무엇인가?
A. 복사 누락, 오래된 파일 잔존, output directory 착각이 대표 위험이다.

Q. 복사 전에 static 폴더를 비워야 하는가?
A. 권장된다. 이전 hash 파일이나 오래된 asset이 남아 혼선을 만들 수 있다.

---

## 3.2 Gradle Integrated Build Flow

### [개념]

Gradle Integrated Build Flow는 Spring Boot Gradle build 과정에서 프론트엔드 install, build, copy 작업을 자동으로 연결하는 방식이다.

---

### [핵심]

자동화 목적:

- 수동 복사 실수 방지
- CI/CD에서 일관된 Build 수행
- 프론트엔드와 백엔드 Build 순서 보장
- JAR 안에 최신 React Build 포함
- 팀원 간 배포 절차 통일

주의:

- Node.js 설치 필요
- npm/yarn/pnpm 명령 일치 필요
- frontend 경로 설정 필요
- OS별 명령 호환성 주의
- Build 시간이 증가할 수 있음

---

### [실무]

Gradle task 예:

```gradle
tasks.register("frontendBuild", Exec) {
    workingDir "../frontend"
    commandLine "npm", "run", "build"
}

tasks.register("copyFrontendBuild", Copy) {
    dependsOn "frontendBuild"
    from "../frontend/build"
    into "src/main/resources/static"
}

processResources {
    dependsOn "copyFrontendBuild"
}
```

Vite라면:

```gradle
tasks.register("copyFrontendBuild", Copy) {
    dependsOn "frontendBuild"
    from "../frontend/dist"
    into "src/main/resources/static"
}
```

권장 개선:

```text
clean static directory
→ frontend build
→ copy output
→ processResources
→ bootJar
```

Agent 검토 기준:

```text
Gradle task 확인
→ frontend workingDir 확인
→ package manager 확인
→ output directory 확인
→ copy target 확인
→ task dependency 확인
```

---

### [FAQ]

Q. Gradle에서 프론트엔드 Build를 자동화할 수 있는가?
A. 가능하다. Exec task와 Copy task를 사용해 frontend build와 static 복사를 연결할 수 있다.

Q. Gradle 자동화에서 가장 주의할 것은 무엇인가?
A. frontend 경로, package manager, output directory, task dependency가 맞아야 한다.

Q. Vite와 CRA에서 Gradle copy source가 다른가?
A. 다르다. Vite는 `dist`, CRA는 `build`를 복사한다.

Q. Gradle 자동화는 반드시 필요한가?
A. 아니다. 학원 프로젝트에서는 수동 복사도 가능하지만 CI/CD에서는 자동화가 유리하다.

---

## 3.3 CI/CD Integrated Build Flow

### [개념]

CI/CD Integrated Build Flow는 GitHub Actions 같은 자동화 환경에서 프론트엔드 Build, static 복사, Spring Boot Build를 순서대로 실행하는 방식이다.

---

### [핵심]

CI/CD 통합 Build 순서:

```text
Checkout
→ Setup Node
→ Frontend Install
→ Frontend Build
→ Copy Build Output to Backend Static
→ Setup Java
→ Backend Test
→ Spring Boot Build
→ Artifact Upload or Deploy
```

중요 확인:

- frontend working-directory
- backend working-directory
- Node.js version
- Java version
- package manager
- output directory
- env 변수
- static copy path
- artifact 경로

---

### [실무]

GitHub Actions 예:

```yaml
name: Integrated Build

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
          cache-dependency-path: frontend/package-lock.json

      - name: Frontend Install
        working-directory: ./frontend
        run: npm ci

      - name: Frontend Build
        working-directory: ./frontend
        env:
          REACT_APP_API_BASE_URL: /api
        run: npm run build

      - name: Copy Frontend Build
        run: |
          rm -rf backend/src/main/resources/static/*
          cp -r frontend/build/* backend/src/main/resources/static/

      - name: Setup Java
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: 17

      - name: Backend Build
        working-directory: ./backend
        run: ./gradlew clean build
```

Vite라면:

```yaml
env:
  VITE_API_BASE_URL: /api

run: |
  rm -rf backend/src/main/resources/static/*
  cp -r frontend/dist/* backend/src/main/resources/static/
```

---

### [FAQ]

Q. CI/CD 통합 Build는 어떤 순서로 실행해야 하는가?
A. Frontend install/build 후 static 복사, 그 다음 Spring Boot build 순서가 일반적이다.

Q. GitHub Actions에서 frontend 폴더가 하위에 있으면 어떻게 하는가?
A. `working-directory: ./frontend`를 설정해야 한다.

Q. CI에서 env 설정이 필요한 이유는?
A. Production Build 시점에 API Base URL 같은 값이 주입되기 때문이다.

Q. CI에서 CRA와 Vite의 복사 경로가 다른가?
A. 다르다. CRA는 `frontend/build/*`, Vite는 `frontend/dist/*`를 복사한다.

---

# 4. API Path Separation

## 4.1 API Prefix Rules

### [개념]

API Prefix Rules는 Spring Boot 통합 배포에서 React route와 Backend API route가 충돌하지 않도록 API에 공통 prefix를 붙이는 규칙이다.

권장 prefix:

```text
/api
```

---

### [핵심]

권장 구조:

```text
Frontend Route
→ /festival/detail/1
→ /login
→ /mypage

Backend API
→ /api/festivals/1
→ /api/auth/login
→ /api/users/me
```

비권장 구조:

```text
Frontend Route
→ /festival/detail/1

Backend API
→ /festival/detail/1
```

장점:

- SPA fallback 제외 처리 쉬움
- Security 설정 명확
- API와 화면 route 구분
- Nginx proxy 전환 쉬움
- Review Agent 검토 쉬움

---

### [실무]

Spring Controller 예:

```java
@RestController
@RequestMapping("/api/festivals")
public class FestivalController {

  @GetMapping("/{id}")
  public FestivalResponse getFestival(@PathVariable Long id) {
    return festivalService.getFestival(id);
  }
}
```

React route 예:

```jsx
<Route path="/festival/detail/:id" element={<FestivalDetailPage />} />
```

Agent 검토 Flow:

```text
Controller RequestMapping 확인
→ Frontend route 목록 확인
→ /api prefix 사용 여부 확인
→ fallback mapping과 충돌 확인
→ Security matcher 확인
```

---

### [FAQ]

Q. Spring Boot 통합 배포에서 API prefix가 필요한가?
A. 강력히 권장된다. React route와 API route 충돌을 줄일 수 있다.

Q. API prefix는 무엇을 많이 사용하는가?
A. 보통 `/api`를 사용한다.

Q. API prefix가 없으면 어떤 문제가 생기는가?
A. SPA fallback, Security, route mapping에서 프론트엔드 route와 충돌할 수 있다.

Q. API prefix를 쓰면 나중에 Nginx 분리 배포도 쉬운가?
A. 그렇다. `/api` proxy 규칙을 만들기 쉽다.

---

## 4.2 API and SPA Fallback Collision

### [개념]

API and SPA Fallback Collision은 Spring Boot fallback 설정이 API 요청까지 `index.html`로 보내 API 응답이 깨지는 문제다.

---

### [핵심]

문제 상황:

```text
Request /api/festivals
→ SpaController catches request
→ forward:/index.html
→ Frontend expects JSON
→ Unexpected token '<'
```

정상 상황:

```text
Request /api/festivals
→ FestivalController handles request
→ JSON response
```

대표 증상:

- API 응답 Content-Type이 `text/html`
- Response Body가 `<!doctype html>`
- JSON parse error
- Unexpected token `<`
- 200인데 데이터 파싱 실패
- API가 아니라 React 화면 HTML이 반환됨

---

### [실무]

Fallback Controller는 API path를 잡지 않도록 설계해야 한다.

주의할 mapping:

```java
@RequestMapping(value = {
    "/",
    "/{path:[^\\.]*}",
    "/**/{path:[^\\.]*}"
})
```

검증 Flow:

```text
GET /api/health
→ JSON인지 확인

GET /api/festivals
→ Content-Type application/json 확인

GET /login
→ index.html 반환 확인
```

Agent 판단 기준:

```text
API 요청에 HTML 응답
→ fallback collision 의심

API 200 + JSON parse error
→ response body 확인

API path에 /api 없음
→ route collision 위험 증가
```

---

### [FAQ]

Q. API 요청에 index.html이 반환되는 이유는?
A. SPA fallback mapping이 API 요청까지 잡고 있을 가능성이 높다.

Q. Unexpected token '<' 에러는 왜 발생하는가?
A. JSON을 기대했지만 HTML index.html이 응답되었기 때문이다.

Q. API와 fallback 충돌을 막으려면 어떻게 해야 하는가?
A. API path를 `/api`로 분리하고 fallback이 API path를 제외하도록 설정해야 한다.

Q. API 200인데 프론트에서 실패하면 무엇을 확인해야 하는가?
A. Response Body가 JSON인지 HTML인지 확인해야 한다.

---

# 5. Spring Boot SPA Fallback

## 5.1 Fallback Controller Rules

### [개념]

Fallback Controller는 Spring Boot 통합 배포에서 React Router route 요청을 `index.html`로 forward하는 Controller다.

---

### [핵심]

Fallback Controller 역할:

- `/login`, `/mypage`, `/detail/1` 같은 frontend route 처리
- React Router가 현재 URL을 읽을 수 있도록 `index.html` 반환
- 직접 URL 접근 지원
- 새로고침 404 방지

Fallback Controller가 처리하면 안 되는 것:

```text
/api/**
/assets/**
/static/**
/favicon.ico
/manifest.json
/*.js
/*.css
/*.png
/*.svg
```

---

### [실무]

기본 예:

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

이 패턴의 의도:

```text
점(.)이 없는 경로
→ frontend route로 간주

점(.)이 있는 경로
→ static asset으로 간주
```

검토 필요:

```text
API path가 점(.) 없는 경로일 경우 fallback에 잡히지 않는가?
/api prefix를 Controller가 우선 처리하는가?
Security 설정이 forward를 막지 않는가?
```

---

### [FAQ]

Q. Fallback Controller는 무엇인가?
A. Spring Boot에서 React route 요청을 `index.html`로 forward하는 Controller다.

Q. Fallback Controller는 왜 필요한가?
A. BrowserRouter 사용 시 직접 URL 접근과 새로고침 404를 막기 위해 필요하다.

Q. Fallback Controller가 API 요청을 처리하면 안 되는 이유는?
A. API 요청에는 JSON이 반환되어야 하며 index.html이 반환되면 프론트엔드 파싱이 실패한다.

Q. 점이 없는 경로만 fallback하는 이유는?
A. `.js`, `.css`, `.png` 같은 정적 파일 요청을 피하기 위한 패턴이다.

---

## 5.2 Fallback Test Rules

### [개념]

Fallback Test Rules는 Spring Boot 통합 배포 후 React route, API, static asset이 올바르게 분리되어 응답하는지 검증하는 규칙이다.

---

### [핵심]

테스트 대상:

```text
/
/login
/festival/detail/1
/api/health
/api/festivals
/assets/index.[hash].js
/static/js/main.[hash].js
/favicon.ico
```

정상 응답:

```text
/login
→ text/html
→ index.html

/api/health
→ application/json
→ API response

/assets/index.js
→ application/javascript
→ JS file
```

---

### [실무]

브라우저 Network 검증:

```text
Frontend route 직접 접근
→ status 200
→ Response index.html
→ React screen render

API request
→ status 200/401/403/404
→ JSON response

Asset request
→ status 200
→ JS/CSS/Image response
```

curl 검증 예:

```bash
curl -I http://localhost:8080/login
curl -I http://localhost:8080/api/health
curl -I http://localhost:8080/assets/index.js
```

Review 기준:

```md
- [ ] frontend route가 index.html을 반환하는가?
- [ ] API route가 JSON을 반환하는가?
- [ ] asset route가 실제 파일을 반환하는가?
- [ ] API route가 index.html을 반환하지 않는가?
- [ ] asset route가 index.html을 반환하지 않는가?
```

---

### [FAQ]

Q. Spring Boot fallback은 어떻게 테스트하는가?
A. frontend route, API route, static asset route를 각각 직접 요청해 응답 타입을 확인한다.

Q. /login은 어떤 응답이어야 하는가?
A. React route라면 `index.html`이 반환되고 React가 login 화면을 렌더링해야 한다.

Q. /api/health는 어떤 응답이어야 하는가?
A. API 응답이어야 하며 JSON 또는 지정된 API response가 반환되어야 한다.

Q. JS asset 요청이 text/html이면 무엇이 문제인가?
A. asset 요청이 fallback에 잡혀 index.html이 반환되고 있는 것이다.

---

# 6. Spring Security Integration

## 6.1 Static Resource Security Rules

### [개념]

Static Resource Security Rules는 Spring Security가 React 정적 파일, JS, CSS, 이미지 요청을 막지 않도록 허용하는 규칙이다.

---

### [핵심]

허용 대상:

```text
/
/index.html
/assets/**
/static/**
/favicon.ico
/manifest.json
/*.js
/*.css
/*.png
/*.svg
/*.ico
```

주의:

- 정적 리소스를 인증 필요로 막으면 로그인 화면 자체가 로드되지 않을 수 있다.
- API 보안과 static resource 허용을 분리해야 한다.
- SPA fallback forward가 Security에 막히지 않아야 한다.
- 관리자 route 보안은 프론트엔드 route가 아니라 백엔드 API에서 보장해야 한다.

---

### [실무]

Spring Security 예:

```java
@Bean
SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
  http
      .authorizeHttpRequests(auth -> auth
          .requestMatchers(
              "/",
              "/index.html",
              "/assets/**",
              "/static/**",
              "/favicon.ico",
              "/manifest.json"
          ).permitAll()
          .requestMatchers("/api/admin/**").hasRole("ADMIN")
          .requestMatchers("/api/**").authenticated()
          .anyRequest().permitAll()
      );

  return http.build();
}
```

주의:

```text
Frontend route /admin
→ permitAll 가능

Backend API /api/admin/**
→ hasRole("ADMIN") 필수
```

---

### [FAQ]

Q. Spring Security가 static resource를 막으면 어떻게 되는가?
A. index.html, JS, CSS가 로드되지 않아 화면이 뜨지 않을 수 있다.

Q. 프론트엔드 /admin route를 permitAll로 두면 보안 문제가 되는가?
A. 프론트엔드 route 자체는 화면 로딩 경로다. 실제 보안은 `/api/admin/**` 같은 백엔드 API에서 보장해야 한다.

Q. static resource와 API 보안은 어떻게 분리하는가?
A. 정적 파일은 permitAll, 민감 API는 authenticated 또는 role 기반으로 제한한다.

Q. SPA fallback route도 Security에서 허용해야 하는가?
A. BrowserRouter 직접 접근을 위해 frontend route는 index.html을 받을 수 있어야 한다.

---

## 6.2 Authentication Flow in Integrated Deployment

### [개념]

Authentication Flow in Integrated Deployment는 같은 Spring Boot 서버가 React 정적 파일과 인증 API를 함께 제공할 때의 인증 흐름이다.

---

### [핵심]

통합 배포 인증 특징:

- 같은 Origin이면 CORS 복잡도가 줄어든다.
- API Base URL을 `/api`로 둘 수 있다.
- JWT Authorization Header 방식 사용 가능
- Cookie 인증 방식 사용 가능
- Spring Security와 React Router 역할을 구분해야 한다.
- Frontend route guard는 UX 보조이고 실제 권한은 Backend API에서 검증한다.

---

### [실무]

JWT Header 방식 Flow:

```text
Browser loads React
→ User login form submit
→ POST /api/auth/login
→ Backend returns accessToken
→ Frontend stores token
→ API request with Authorization Header
→ Spring Security validates token
```

Cookie 방식 Flow:

```text
Browser loads React
→ POST /api/auth/login
→ Backend Set-Cookie
→ Browser stores cookie
→ API request includes cookie
→ Spring Security validates session/token
```

통합 배포 API client 예:

```js
export const api = axios.create({
  baseURL: "/api",
  timeout: 10000,
});
```

Review 기준:

```md
- [ ] login page static resource 접근 가능
- [ ] /api/auth/login 접근 가능
- [ ] 인증 후 /api/\*\* 요청 정상
- [ ] 관리자 API는 ROLE_ADMIN 필요
- [ ] frontend route guard와 backend security 구분
```

---

### [FAQ]

Q. 통합 배포에서는 CORS가 필요 없는가?
A. 같은 Origin으로 제공하면 CORS 문제가 줄어든다. 단, 구조에 따라 필요할 수 있다.

Q. 통합 배포에서 API Base URL을 /api로 써도 되는가?
A. 가능하다. 같은 서버의 `/api` endpoint를 호출하는 구조에 적합하다.

Q. React route guard만으로 인증이 충분한가?
A. 아니다. 실제 권한 검증은 Spring Security가 백엔드 API에서 수행해야 한다.

Q. 로그인 화면이 안 뜨면 무엇을 확인해야 하는가?
A. index.html, JS/CSS static resource가 Security에 막히지 않는지 확인해야 한다.

---

# 7. Build Output Cache and Old Files

## 7.1 Old Static File Risk

### [개념]

Old Static File Risk는 이전 React Build 결과물이 Spring Boot static directory에 남아 새 Build 결과와 충돌하는 문제다.

---

### [핵심]

문제 원인:

- static 폴더를 비우지 않고 새 파일만 덮어씀
- 이전 hash JS/CSS 파일 잔존
- 이전 index.html이 새 asset과 mismatch
- 브라우저 cache가 이전 asset을 참조
- JAR에 이전 static resource 포함
- build artifact가 갱신되지 않음

증상:

- 이전 화면 표시
- 새 코드 반영 안 됨
- chunk load error
- JS 404
- CSS mismatch
- 배포했는데 변경 없음

---

### [실무]

권장 복사 전 처리:

```bash
rm -rf backend/src/main/resources/static/*
cp -r frontend/dist/* backend/src/main/resources/static/
```

CRA:

```bash
rm -rf backend/src/main/resources/static/*
cp -r frontend/build/* backend/src/main/resources/static/
```

Gradle / CI에서도 동일 원칙:

```text
clean static
→ copy fresh build output
→ backend build
```

검증 Flow:

```text
static 폴더 정리 여부 확인
→ 새 index.html timestamp 확인
→ 새 asset hash 확인
→ JAR 재빌드 확인
→ browser hard reload
```

---

### [FAQ]

Q. static 폴더를 비우고 복사해야 하는가?
A. 권장된다. 이전 hash 파일이나 오래된 asset이 남아 문제를 만들 수 있다.

Q. 배포했는데 이전 화면이 보이는 이유는?
A. 이전 static 파일, 브라우저 캐시, JAR 재빌드 누락이 원인일 수 있다.

Q. chunk load error는 왜 발생하는가?
A. index.html과 JS chunk 파일의 버전이 맞지 않거나 이전 asset이 캐시되었을 수 있다.

Q. Spring Boot JAR을 다시 빌드해야 하는가?
A. static resource를 변경했다면 JAR에 포함되도록 다시 빌드해야 한다.

---

## 7.2 Browser Cache in Integrated Deployment

### [개념]

Browser Cache in Integrated Deployment는 Spring Boot가 제공하는 React 정적 파일이 브라우저에 캐시되어 새 배포가 바로 반영되지 않는 문제다.

---

### [핵심]

캐시 기준:

```text
index.html
→ 짧은 cache 또는 no-cache 권장

hashed JS/CSS
→ long cache 가능

config.json
→ no-store 또는 짧은 cache 권장
```

통합 배포 위험:

- index.html이 오래 캐시됨
- 이전 JS hash 참조
- Service Worker cache 잔존
- 사용자별로 다른 버전 표시
- 새 JAR 배포 후에도 브라우저가 이전 파일 사용

---

### [실무]

Spring Boot cache 설정은 프로젝트 방식에 따라 달라질 수 있다.

검토 항목:

```md
- [ ] index.html cache가 너무 길지 않은가?
- [ ] hashed asset은 장기 캐시 가능한가?
- [ ] Service Worker를 사용하고 있는가?
- [ ] 배포 후 Hard Reload로 정상 확인되는가?
- [ ] cache-control header가 의도대로 설정되어 있는가?
```

문제 해결 Flow:

```text
Hard Reload
→ Disable Cache 테스트
→ Response Headers 확인
→ Service Worker 확인
→ static resource cache policy 조정
```

---

### [FAQ]

Q. Spring Boot 통합 배포 후 이전 화면이 계속 보이는 이유는?
A. 브라우저 캐시, Service Worker, 이전 static 파일, JAR 재빌드 누락이 원인일 수 있다.

Q. index.html은 왜 길게 캐시하면 위험한가?
A. 이전 JS hash를 참조해 새 배포와 mismatch가 발생할 수 있기 때문이다.

Q. hashed JS/CSS는 장기 캐시해도 되는가?
A. 가능하다. 내용이 바뀌면 파일명이 바뀌기 때문이다.

Q. 캐시 문제는 어디서 확인하는가?
A. Network Response Headers, Disable Cache, Hard Reload, Application 탭의 Service Worker를 확인한다.

---

# 8. Integrated Deployment Troubleshooting

## 8.1 Spring Boot Shows Whitelabel Error

### [개념]

Spring Boot Whitelabel Error는 React 화면 대신 Spring Boot 기본 오류 페이지가 표시되는 문제다.

---

### [핵심]

대표 원인:

- static root에 index.html 없음
- Build Output 복사 위치 오류
- build 폴더 자체를 static에 넣음
- SPA fallback 없음
- 요청 route를 Spring MVC가 처리하지 못함
- Security가 요청을 차단
- JAR에 static resource가 포함되지 않음

---

### [실무]

Troubleshooting Flow:

```text
GET / 확인
→ static/index.html 존재 확인
→ target/classes/static/index.html 확인
→ Spring Boot log 확인
→ fallback controller 확인
→ Security 설정 확인
```

확인 명령 예:

```bash
ls backend/src/main/resources/static
ls backend/build/resources/main/static
```

또는 Maven/Gradle 결과 경로:

```text
target/classes/static
build/resources/main/static
```

판단 기준:

```text
루트 / 에서 Whitelabel
→ index.html 위치 문제 가능성 높음

특정 route에서 Whitelabel
→ SPA fallback 누락 가능성 높음
```

---

### [FAQ]

Q. Spring Boot에서 React 화면 대신 Whitelabel Error가 나오는 이유는?
A. index.html 위치 오류, fallback 누락, Security 차단, static resource 미포함이 원인일 수 있다.

Q. 루트 / 에서 Whitelabel이 나오면 무엇을 확인해야 하는가?
A. `src/main/resources/static/index.html`이 존재하는지 확인해야 한다.

Q. 특정 React route에서만 Whitelabel이 나오면 무엇을 확인해야 하는가?
A. SPA fallback controller가 있는지 확인해야 한다.

Q. JAR에 static 파일이 포함되었는지 어떻게 확인하는가?
A. build output의 `classes/static` 경로 또는 JAR 내부를 확인한다.

---

## 8.2 React White Screen in Spring Boot

### [개념]

React White Screen in Spring Boot는 Spring Boot 통합 배포 후 `index.html`은 제공되지만 React 화면이 렌더링되지 않는 문제다.

---

### [핵심]

대표 원인:

- JS bundle 404
- CSS 404
- asset path 오류
- Vite `base` 또는 CRA `homepage` 오류
- JS 요청에 index.html 반환
- MIME type error
- env undefined
- API 초기화 runtime error
- React Router basename 오류
- 이전 cache mismatch

---

### [실무]

Troubleshooting Flow:

```text
Browser Console 확인
→ Network JS/CSS 확인
→ JS response Content-Type 확인
→ index.html script src 확인
→ static resource 파일 존재 확인
→ base/homepage 확인
→ cache 확인
```

Vite 확인:

```text
/assets/index.[hash].js
→ 200이어야 함
```

CRA 확인:

```text
/static/js/main.[hash].js
→ 200이어야 함
```

Critical 판단:

```text
JS 요청에 text/html
→ fallback이 asset 요청을 잡음

JS 404
→ static 복사 또는 base path 문제

API localhost 호출
→ env production 문제
```

---

### [FAQ]

Q. Spring Boot 통합 배포 후 흰 화면이 나오면 무엇을 먼저 확인해야 하는가?
A. Console Error와 Network의 JS/CSS 요청 상태를 먼저 확인해야 한다.

Q. index.html은 200인데 화면이 안 뜨는 이유는?
A. JS bundle 404, MIME type error, runtime error, env undefined가 원인일 수 있다.

Q. Vite 통합 배포에서 /assets JS가 404면 무엇을 확인하는가?
A. `dist/assets` 복사 여부와 Vite `base` 설정을 확인한다.

Q. CRA 통합 배포에서 /static/js가 404면 무엇을 확인하는가?
A. `build/static` 복사 여부와 CRA `homepage` 설정을 확인한다.

---

## 8.3 API Returns HTML in Integrated Deployment

### [개념]

API Returns HTML in Integrated Deployment는 Spring Boot 통합 배포에서 API 요청에 JSON 대신 React `index.html`이 반환되는 문제다.

---

### [핵심]

대표 증상:

```text
Response Content-Type: text/html
Response Body: <!doctype html>
Console Error: Unexpected token '<'
API status: 200
Data parsing failure
```

대표 원인:

- SPA fallback이 API 요청을 잡음
- API prefix 미분리
- Controller RequestMapping 경로 오류
- Security redirect가 HTML login page 반환
- 프론트엔드 API Base URL 오류
- endpoint path 오타

---

### [실무]

Troubleshooting Flow:

```text
Network API response 확인
→ Content-Type 확인
→ Response Body 확인
→ API URL 확인
→ Controller mapping 확인
→ fallback mapping 확인
→ Security redirect 확인
```

구분:

```text
index.html 반환
→ fallback collision 가능성

login page HTML 반환
→ Security redirect 가능성

Whitelabel HTML 반환
→ backend error route 가능성
```

해결 기준:

```text
API path를 /api로 분리
fallback에서 /api 제외
Security unauthorized 응답을 JSON/401로 처리
API Base URL과 endpoint path 수정
```

---

### [FAQ]

Q. API 요청에 React index.html이 오는 이유는?
A. SPA fallback이 API 요청까지 잡고 있을 가능성이 높다.

Q. API 요청에 login HTML이 오는 이유는?
A. Spring Security가 인증되지 않은 요청을 로그인 페이지로 redirect했을 수 있다.

Q. Unexpected token '<'는 무엇을 의미하는가?
A. JSON을 기대했지만 HTML 응답이 와서 파싱에 실패한 경우가 많다.

Q. API HTML 응답 문제는 어디서 확인하는가?
A. Network 탭에서 API Response Body와 Content-Type을 확인한다.

---

## 8.4 Static Resource Blocked by Security

### [개념]

Static Resource Blocked by Security는 Spring Security 설정 때문에 React 정적 파일 접근이 차단되는 문제다.

---

### [핵심]

대표 증상:

- `/` 요청이 401 / 403
- `index.html` 접근 차단
- JS / CSS 요청 401 / 403
- 로그인 화면도 로드되지 않음
- redirect loop 발생
- Spring Security login page 표시

대표 원인:

- static resource permitAll 누락
- `anyRequest().authenticated()`가 정적 파일까지 적용
- Security matcher 순서 오류
- fallback route가 인증 필요로 처리
- `/assets/**`, `/static/**` 허용 누락

---

### [실무]

잘못된 예:

```java
.authorizeHttpRequests(auth -> auth
    .requestMatchers("/api/**").authenticated()
    .anyRequest().authenticated()
)
```

개선 예:

```java
.authorizeHttpRequests(auth -> auth
    .requestMatchers(
        "/",
        "/index.html",
        "/assets/**",
        "/static/**",
        "/favicon.ico",
        "/manifest.json"
    ).permitAll()
    .requestMatchers("/api/admin/**").hasRole("ADMIN")
    .requestMatchers("/api/**").authenticated()
    .anyRequest().permitAll()
)
```

검증 Flow:

```text
GET /
→ 200 text/html

GET /assets/index.js
→ 200 application/javascript

GET /api/users/me without token
→ 401 JSON
```

---

### [FAQ]

Q. Spring Security가 static resource를 막으면 어떤 문제가 생기는가?
A. index.html, JS, CSS가 로드되지 않아 React 앱이 뜨지 않을 수 있다.

Q. anyRequest().authenticated()를 쓰면 왜 문제가 될 수 있는가?
A. 정적 파일과 frontend route까지 인증을 요구할 수 있기 때문이다.

Q. static resource는 모두 permitAll 해도 되는가?
A. 일반적으로 React 정적 파일은 공개되어야 한다. 실제 보안은 API에서 처리한다.

Q. 관리자 화면 route도 permitAll이면 위험한가?
A. 프론트엔드 route는 공개될 수 있다. 관리자 API를 반드시 권한으로 보호해야 한다.

---

# 9. Agent Decision Rules

## 9.1 PM Agent Rules

### [개념]

PM Agent는 Spring Boot 통합 배포의 적합성, Build Output, API prefix, fallback, Security 기준, 검증 범위를 정의해야 한다.

---

### [핵심]

PM Agent 확인 항목:

- 통합 배포 목적
- Build Tool
- Output Directory
- Static Resource Path
- 수동 복사 또는 자동화 여부
- API Prefix
- SPA Fallback 필요 여부
- Spring Security static 허용
- 인증 방식
- 배포 후 검증 route
- JAR build 방식
- CI/CD 자동화 필요 여부

---

### [실무]

PM Agent 산출물 예:

```text
Deployment Type: Spring Boot Integrated
Build Tool: CRA
Frontend Output: frontend/build
Static Target: backend/src/main/resources/static
API Prefix: /api
SPA Fallback: required
Security:
- static permitAll
- /api/** authenticated
- /api/admin/** ROLE_ADMIN
Verification:
- /
- /login refresh
- /api/health JSON
- /static/js/main.js 200
```

PM Agent 판단 Flow:

```text
배포 목적 확인
→ 통합 배포 적합성 판단
→ Build Tool 확정
→ static 복사 방식 결정
→ API prefix 확정
→ fallback/security 검증 범위 작성
```

---

### [FAQ]

Q. PM Agent는 Spring Boot 통합 배포에서 무엇을 정해야 하는가?
A. 통합 배포 적합성, output directory, static path, API prefix, fallback, Security 기준을 정해야 한다.

Q. PM Agent가 API prefix를 정해야 하는 이유는?
A. React route와 API route 충돌을 막고 fallback 제외를 쉽게 하기 위해 필요하다.

Q. PM Agent가 수동 복사와 자동화 여부도 정해야 하는가?
A. 그렇다. 프로젝트 규모와 CI/CD 필요성에 따라 선택해야 한다.

Q. PM Agent가 검증 route 목록을 만들어야 하는가?
A. 그렇다. 배포 후 `/`, React route, API, asset 요청을 함께 검증해야 한다.

---

## 9.2 Frontend Agent Rules

### [개념]

Frontend Agent는 Spring Boot 통합 배포에 맞게 Build Output, API Base URL, Router 설정, asset path를 안정적으로 구성해야 한다.

---

### [핵심]

Frontend Agent 필수 기준:

- Build Tool별 output directory 준수
- API Base URL을 `/api` 또는 통합 배포 기준으로 설정
- 운영 localhost 하드코딩 금지
- Vite `base` 또는 CRA `homepage` 확인
- BrowserRouter 사용 시 fallback 필요성 인지
- Sub Path 배포 시 basename 확인
- env validation 적용
- Build 후 static preview 또는 Spring Boot 실행 검증

---

### [실무]

통합 배포 API client 예:

```js
export const api = axios.create({
  baseURL: "/api",
  timeout: 10000,
});
```

Vite env 예:

```env
VITE_API_BASE_URL=/api
```

CRA env 예:

```env
REACT_APP_API_BASE_URL=/api
```

Frontend Agent 검증 기준:

```text
npm run build 성공
→ output directory 확인
→ static 복사 후 Spring Boot 실행
→ / 접속
→ React route 이동
→ API request URL 확인
```

---

### [FAQ]

Q. Frontend Agent는 통합 배포에서 API Base URL을 어떻게 잡는가?
A. 같은 서버에서 API를 제공한다면 `/api`를 사용하는 방식이 단순하다.

Q. Spring Boot 통합 배포에서 localhost API URL을 써도 되는가?
A. 운영에서는 쓰면 안 된다. 같은 서버 API라면 `/api`를 사용하는 것이 적합하다.

Q. Frontend Agent가 fallback Controller를 구현해야 하는가?
A. 일반적으로 Backend Agent가 구현하지만 Frontend Agent도 BrowserRouter 사용 시 필요성을 전달해야 한다.

Q. Vite base와 CRA homepage는 통합 배포에서도 확인해야 하는가?
A. 해야 한다. asset path가 Spring Boot static resource 경로와 맞아야 한다.

---

## 9.3 Backend Agent Rules

### [개념]

Backend Agent는 Spring Boot 통합 배포에서 static resource 제공, API prefix, SPA fallback, Security 설정을 구현해야 한다.

---

### [핵심]

Backend Agent 필수 기준:

- `src/main/resources/static` 정적 파일 제공
- API Controller는 `/api` prefix 권장
- SPA fallback Controller 구현
- fallback이 API path를 잡지 않도록 검토
- static resource Security permitAll
- API Security 인증 / 권한 적용
- 인증 실패 시 API는 JSON/401 응답 기준 검토
- JAR build에 static resource 포함 확인

---

### [실무]

Backend Agent 구현 항목:

```text
Static Resource Path
→ src/main/resources/static

API Prefix
→ /api/**

Fallback Controller
→ frontend route만 index.html forward

Security
→ static permitAll
→ /api/** authenticated
→ /api/admin/** role check
```

검증 Flow:

```text
GET /
→ index.html

GET /login
→ index.html

GET /api/health
→ API response

GET /assets/index.js
→ JS file
```

---

### [FAQ]

Q. Backend Agent는 통합 배포에서 무엇을 구현해야 하는가?
A. static resource 제공, `/api` prefix, SPA fallback, Spring Security 설정을 구현해야 한다.

Q. Backend Agent가 fallback에서 가장 주의할 것은 무엇인가?
A. API 요청과 static asset 요청을 index.html로 보내지 않는 것이다.

Q. Backend Agent가 static resource를 보호해야 하는가?
A. 일반적으로 정적 파일은 공개하고 실제 보안은 API에서 처리한다.

Q. API 인증 실패 시 HTML login page를 반환해도 되는가?
A. SPA API 구조에서는 보통 401 JSON 응답이 더 적합하다.

---

## 9.4 Review Agent Rules

### [개념]

Review Agent는 Spring Boot 통합 배포 결과가 정적 파일, API, fallback, Security 관점에서 정상인지 검토해야 한다.

---

### [핵심]

Review Agent Checklist:

```md
- [ ] React Build가 성공했는가?
- [ ] 올바른 output directory를 복사했는가?
- [ ] static root에 index.html이 있는가?
- [ ] JS / CSS asset이 static root 기준으로 존재하는가?
- [ ] Spring Boot JAR에 static resource가 포함되었는가?
- [ ] API path가 `/api`로 분리되어 있는가?
- [ ] SPA fallback이 direct route를 처리하는가?
- [ ] API path가 fallback에 잡히지 않는가?
- [ ] asset path가 fallback에 잡히지 않는가?
- [ ] Spring Security가 static resource를 허용하는가?
- [ ] 민감 API는 인증 / 권한이 적용되는가?
- [ ] API 응답이 HTML이 아닌 JSON인가?
- [ ] 배포 후 Network에서 JS/CSS/API status를 확인했는가?
```

---

### [실무]

Review Agent 판단 Flow:

```text
Frontend Build 확인
→ static 복사 구조 확인
→ Spring Boot build/run
→ / 접속
→ React route direct access
→ asset request 확인
→ API request 확인
→ Security response 확인
→ cache 문제 확인
```

Critical Issue:

```text
static root에 index.html 없음
API 요청에 index.html 반환
JS 요청에 index.html 반환
Spring Security가 JS/CSS 차단
운영 API URL이 localhost
fallback 없음으로 refresh 404
```

승인 기준:

```text
index.html 정상
JS/CSS asset 정상
React route refresh 정상
API JSON 응답 정상
Security static/API 분리 정상
Critical Console Error 없음
```

---

### [FAQ]

Q. Review Agent는 통합 배포에서 무엇을 가장 먼저 확인해야 하는가?
A. static root에 `index.html`이 있고 JS/CSS asset이 정상 로드되는지 확인해야 한다.

Q. API 요청에 index.html이 반환되면 승인 가능한가?
A. 아니다. fallback과 API path가 충돌하는 치명적 문제다.

Q. Spring Security가 static resource를 막으면 승인 가능한가?
A. 아니다. React 앱 자체가 로드되지 않을 수 있다.

Q. 통합 배포 Review에서 Network 탭은 왜 중요한가?
A. 실제 JS/CSS/API 요청 URL, status, Content-Type을 확인할 수 있기 때문이다.

---

# 10. Common Mistakes

## 10.1 Spring Boot Integrated Deployment Common Mistakes

### [개념]

Spring Boot Integrated Deployment Common Mistakes는 React Build 결과물을 Spring Boot에 포함할 때 자주 발생하는 구조, fallback, security, cache 실수다.

---

### [핵심]

자주 발생하는 실수:

- React Source Code를 static에 복사
- `npm run build` 없이 복사
- Vite `dist` 대신 `build` 복사
- CRA `build` 대신 `dist` 복사
- `dist` 또는 `build` 폴더 자체를 static에 넣음
- static root에 `index.html`이 없음
- 기존 static 파일을 지우지 않고 덮어씀
- Spring Boot JAR 재빌드 누락
- API prefix 없이 React route와 API 충돌
- SPA fallback 누락
- fallback이 `/api` 요청을 index.html로 보냄
- fallback이 JS/CSS asset 요청을 index.html로 보냄
- Spring Security가 static resource 차단
- API 인증 실패 시 HTML login page 반환
- 운영 API URL이 localhost로 남음
- Vite `base` 또는 CRA `homepage` 오류
- Browser cache 때문에 이전 화면 표시

---

### [실무]

실수별 판단:

```text
Whitelabel Error
→ index.html 위치 / fallback 확인

White Screen
→ JS/CSS 404 / MIME type / env 확인

API Unexpected token '<'
→ API가 HTML 반환하는지 확인

401/403 on JS/CSS
→ Spring Security static permitAll 확인

변경사항 미반영
→ static clean / JAR rebuild / browser cache 확인

Refresh 404
→ SPA fallback 확인
```

---

### [FAQ]

Q. Spring Boot 통합 배포에서 가장 흔한 실수는 무엇인가?
A. build 또는 dist 폴더 자체를 static에 넣어 index.html 위치가 한 단계 밀리는 실수다.

Q. 통합 배포에서 가장 치명적인 실수는 무엇인가?
A. API 요청이나 JS 요청에 index.html이 반환되는 fallback 충돌이다.

Q. Spring Security 관련 흔한 실수는 무엇인가?
A. 정적 파일까지 인증 대상으로 설정해 JS/CSS가 로드되지 않는 것이다.

Q. 변경사항이 반영되지 않는 이유는?
A. static 폴더 미정리, JAR 재빌드 누락, 브라우저 캐시가 원인일 수 있다.

---

# 11. Part07 Quality Checklist

## 11.1 Document Quality

### [개념]

이 문서는 Frontend Build & Deploy Domain의 Part07이며 Spring Boot Integrated Deployment Rules Retrieval에 최적화되어야 한다.

---

### [핵심]

문서 품질 기준:

- Spring Boot 통합 배포 정의 포함
- 통합 배포 적합성 판단 기준 포함
- Spring Boot static resource path 포함
- Vite dist copy 규칙 포함
- CRA build copy 규칙 포함
- Manual Build and Copy Flow 포함
- Gradle Integrated Build Flow 포함
- CI/CD Integrated Build Flow 포함
- API Prefix Rules 포함
- API and SPA Fallback Collision 포함
- Fallback Controller Rules 포함
- Spring Security static resource 규칙 포함
- Authentication Flow 포함
- Old Static File Risk 포함
- Troubleshooting Flow 포함
- Agent별 판단 기준 포함
- Common Mistakes 포함
- Retrieval Queries 포함

---

### [실무]

Part07은 다음 문서와 연결된다.

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

Q. Part07의 핵심 목적은 무엇인가?
A. React Build 결과물을 Spring Boot static resource에 통합 배포할 때 파일 위치, fallback, API path, Security 문제를 Agent가 정확히 판단하게 하는 것이다.

Q. Part07에서 Nginx 배포 전체를 다루는가?
A. 아니다. Spring Boot 통합 배포에 집중하고 Nginx 배포는 후속 Part에서 다룬다.

Q. Part07에서 CI/CD 전체를 다루는가?
A. 아니다. 통합 Build Flow만 다루고 CI/CD 상세 전략은 후속 Part에서 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. Spring Boot Integrated Deployment란 무엇인가?
A. React Build 결과물을 Spring Boot static resource에 포함해 하나의 Spring Boot 서버에서 프론트엔드와 백엔드를 함께 제공하는 방식이다.

Q. 학원 프로젝트에서 Spring Boot 통합 배포를 써도 되는가?
A. 괜찮다. 발표와 데모 목적에서는 서버 하나로 관리할 수 있어 단순하고 실용적이다.

Q. Spring Boot 통합 배포의 장점은 무엇인가?
A. 서버 하나로 배포 가능하고 CORS 복잡도가 줄며 발표와 데모 환경 구성이 쉽다.

Q. Spring Boot 통합 배포의 단점은 무엇인가?
A. 프론트엔드 독립 배포가 어렵고 프론트 수정만으로도 백엔드 재배포가 필요할 수 있다.

Q. Spring Boot static resource 기본 경로는 어디인가?
A. 일반적으로 `src/main/resources/static`을 사용한다.

Q. React index.html은 Spring Boot 어디에 있어야 하는가?
A. 보통 `src/main/resources/static/index.html` 위치에 있어야 한다.

Q. Vite Build 결과물은 Spring Boot 어디에 복사하는가?
A. `frontend/dist/*` 내부 파일을 `backend/src/main/resources/static/`로 복사한다.

Q. CRA Build 결과물은 Spring Boot 어디에 복사하는가?
A. `frontend/build/*` 내부 파일을 `backend/src/main/resources/static/`로 복사한다.

Q. dist 폴더 자체를 static에 넣어도 되는가?
A. 권장하지 않는다. `static/index.html` 구조가 되도록 dist 내부 파일을 복사해야 한다.

Q. build 폴더 자체를 static에 넣어도 되는가?
A. 권장하지 않는다. `static/index.html` 구조가 되도록 build 내부 파일을 복사해야 한다.

Q. Spring Boot 통합 배포에서 static 폴더를 비우고 복사해야 하는가?
A. 권장된다. 이전 hash 파일이나 오래된 asset이 남아 문제를 만들 수 있다.

Q. Manual Build and Copy Flow란 무엇인가?
A. React Build 결과물을 수동으로 Spring Boot static 폴더에 복사한 뒤 Spring Boot를 빌드하는 방식이다.

Q. Gradle에서 프론트엔드 Build를 자동화할 수 있는가?
A. 가능하다. Exec task와 Copy task를 사용해 frontend build와 static 복사를 연결할 수 있다.

Q. Gradle 자동화에서 가장 주의할 것은 무엇인가?
A. frontend 경로, package manager, output directory, task dependency가 맞아야 한다.

Q. CI/CD 통합 Build는 어떤 순서로 실행해야 하는가?
A. Frontend install/build 후 static 복사, 그 다음 Spring Boot build 순서가 일반적이다.

Q. GitHub Actions에서 frontend 폴더가 하위에 있으면 어떻게 하는가?
A. `working-directory: ./frontend`를 설정해야 한다.

Q. Spring Boot 통합 배포에서 API prefix가 필요한가?
A. 강력히 권장된다. React route와 API route 충돌을 줄일 수 있다.

Q. API prefix는 무엇을 많이 사용하는가?
A. 보통 `/api`를 사용한다.

Q. API 요청에 index.html이 반환되는 이유는?
A. SPA fallback mapping이 API 요청까지 잡고 있을 가능성이 높다.

Q. Unexpected token '<' 에러는 왜 발생하는가?
A. JSON을 기대했지만 HTML index.html이 응답되었기 때문이다.

Q. Fallback Controller는 무엇인가?
A. Spring Boot에서 React route 요청을 `index.html`로 forward하는 Controller다.

Q. Fallback Controller는 왜 필요한가?
A. BrowserRouter 사용 시 직접 URL 접근과 새로고침 404를 막기 위해 필요하다.

Q. Fallback Controller가 API 요청을 처리하면 안 되는 이유는?
A. API 요청에는 JSON이 반환되어야 하며 index.html이 반환되면 프론트엔드 파싱이 실패한다.

Q. Spring Boot fallback은 어떻게 테스트하는가?
A. frontend route, API route, static asset route를 각각 직접 요청해 응답 타입을 확인한다.

Q. /login은 어떤 응답이어야 하는가?
A. React route라면 `index.html`이 반환되고 React가 login 화면을 렌더링해야 한다.

Q. /api/health는 어떤 응답이어야 하는가?
A. API 응답이어야 하며 JSON 또는 지정된 API response가 반환되어야 한다.

Q. JS asset 요청이 text/html이면 무엇이 문제인가?
A. asset 요청이 fallback에 잡혀 index.html이 반환되고 있는 것이다.

Q. Spring Security가 static resource를 막으면 어떻게 되는가?
A. index.html, JS, CSS가 로드되지 않아 화면이 뜨지 않을 수 있다.

Q. 프론트엔드 /admin route를 permitAll로 두면 보안 문제가 되는가?
A. 프론트엔드 route 자체는 화면 로딩 경로다. 실제 보안은 `/api/admin/**` 같은 백엔드 API에서 보장해야 한다.

Q. 통합 배포에서는 CORS가 필요 없는가?
A. 같은 Origin으로 제공하면 CORS 문제가 줄어든다. 단, 구조에 따라 필요할 수 있다.

Q. 통합 배포에서 API Base URL을 /api로 써도 되는가?
A. 가능하다. 같은 서버의 `/api` endpoint를 호출하는 구조에 적합하다.

Q. React route guard만으로 인증이 충분한가?
A. 아니다. 실제 권한 검증은 Spring Security가 백엔드 API에서 수행해야 한다.

Q. Spring Boot 통합 배포 후 이전 화면이 계속 보이는 이유는?
A. 브라우저 캐시, Service Worker, 이전 static 파일, JAR 재빌드 누락이 원인일 수 있다.

Q. Spring Boot에서 React 화면 대신 Whitelabel Error가 나오는 이유는?
A. index.html 위치 오류, fallback 누락, Security 차단, static resource 미포함이 원인일 수 있다.

Q. 루트 / 에서 Whitelabel이 나오면 무엇을 확인해야 하는가?
A. `src/main/resources/static/index.html`이 존재하는지 확인해야 한다.

Q. 특정 React route에서만 Whitelabel이 나오면 무엇을 확인해야 하는가?
A. SPA fallback controller가 있는지 확인해야 한다.

Q. Spring Boot 통합 배포 후 흰 화면이 나오면 무엇을 먼저 확인해야 하는가?
A. Console Error와 Network의 JS/CSS 요청 상태를 먼저 확인해야 한다.

Q. Vite 통합 배포에서 /assets JS가 404면 무엇을 확인하는가?
A. `dist/assets` 복사 여부와 Vite `base` 설정을 확인한다.

Q. CRA 통합 배포에서 /static/js가 404면 무엇을 확인하는가?
A. `build/static` 복사 여부와 CRA `homepage` 설정을 확인한다.

Q. API 요청에 login HTML이 오는 이유는?
A. Spring Security가 인증되지 않은 요청을 로그인 페이지로 redirect했을 수 있다.

Q. Static Resource Blocked by Security란 무엇인가?
A. Spring Security 설정 때문에 React 정적 파일 접근이 차단되는 문제다.

Q. anyRequest().authenticated()를 쓰면 왜 문제가 될 수 있는가?
A. 정적 파일과 frontend route까지 인증을 요구할 수 있기 때문이다.

Q. PM Agent는 Spring Boot 통합 배포에서 무엇을 정해야 하는가?
A. 통합 배포 적합성, output directory, static path, API prefix, fallback, Security 기준을 정해야 한다.

Q. Frontend Agent는 통합 배포에서 API Base URL을 어떻게 잡는가?
A. 같은 서버에서 API를 제공한다면 `/api`를 사용하는 방식이 단순하다.

Q. Backend Agent는 통합 배포에서 무엇을 구현해야 하는가?
A. static resource 제공, `/api` prefix, SPA fallback, Spring Security 설정을 구현해야 한다.

Q. Review Agent는 통합 배포에서 무엇을 가장 먼저 확인해야 하는가?
A. static root에 `index.html`이 있고 JS/CSS asset이 정상 로드되는지 확인해야 한다.

Q. Spring Boot 통합 배포에서 가장 흔한 실수는 무엇인가?
A. build 또는 dist 폴더 자체를 static에 넣어 index.html 위치가 한 단계 밀리는 실수다.

Q. Part07 다음 문서는 무엇인가?
A. Part08 Nginx Deployment Rules로 이어지는 것이 적합하다.
