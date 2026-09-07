# Frontend Build & Deploy Part03 - Environment Variable Rules

---

# 1. Environment Variable Core

## 1.1 Frontend Environment Variable Definition

### [개념]

Frontend Environment Variable은 프론트엔드 애플리케이션이 실행 환경별 설정 값을 사용하기 위해 빌드 시점 또는 런타임에 참조하는 변수다.

대표 사용 대상:

```text
API Base URL
Public App Environment
Public Map Key
Public OAuth Client ID
Public Analytics ID
Feature Flag
Runtime Config Path
```

---

### [핵심]

Frontend Environment Variable 핵심 규칙:

- 프론트엔드 환경 변수는 브라우저에 노출될 수 있다.
- Secret Key를 저장하면 안 된다.
- API Base URL처럼 공개 가능한 설정만 저장한다.
- React SPA 환경 변수는 대부분 Build 시점에 주입된다.
- `.env` 수정 후 개발 서버 재시작이 필요하다.
- 운영 환경 변수는 Production Build 시점에 반영되어야 한다.
- Build Tool별 prefix 규칙을 반드시 지켜야 한다.
- Vite는 `VITE_` prefix를 사용한다.
- CRA는 `REACT_APP_` prefix를 사용한다.

---

### [실무]

2026 실무 기준으로 프론트엔드 환경 변수는 설정 분리 용도이지 보안 저장소가 아니다.

Frontend Environment Variable 판단 Flow:

```text
Build Tool 확인
→ Env Prefix 확인
→ Env File 확인
→ Env Access 방식 확인
→ Secret 포함 여부 확인
→ Build 시점 반영 여부 확인
→ Browser 노출 가능성 검토
→ 배포 환경 변수 설정 확인
```

Agent 판단 기준:

```text
환경 변수에 Secret 포함
→ Critical Issue

환경 변수 prefix 불일치
→ Undefined Risk

운영 API URL 누락
→ Deploy Failure Risk

.env 수정 후 재시작 없음
→ Local Debug Risk

운영 배포 후 값 변경 기대
→ Build-time Env 오해 가능성
```

---

### [FAQ]

Q. 프론트엔드 환경 변수는 무엇인가?
A. API 주소, 앱 환경, public key 같은 환경별 설정 값을 프론트엔드 코드에서 사용하기 위한 변수다.

Q. 프론트엔드 환경 변수는 안전한가?
A. 아니다. 브라우저에 노출될 수 있으므로 Secret Key를 넣으면 안 된다.

Q. 프론트엔드 환경 변수는 언제 반영되는가?
A. 일반 React SPA에서는 대부분 Build 시점에 코드에 주입된다.

Q. .env를 수정했는데 값이 안 바뀌는 이유는?
A. 개발 서버를 재시작하지 않았거나 운영에서는 다시 Build하지 않았기 때문이다.

---

## 1.2 Public Config vs Secret

### [개념]

Public Config는 브라우저에 노출되어도 되는 설정이고, Secret은 서버 내부에서만 보호되어야 하는 민감 정보다.

---

### [핵심]

Frontend에 저장 가능:

```text
API Base URL
APP_ENV
PUBLIC_KAKAO_JS_KEY
PUBLIC_GOOGLE_MAP_KEY
OAUTH_CLIENT_ID
SENTRY_DSN_PUBLIC
ANALYTICS_ID
FEATURE_FLAG
```

Frontend에 저장 금지:

```text
DB_PASSWORD
JWT_SECRET
ACCESS_TOKEN_SECRET
REFRESH_TOKEN_SECRET
OPENAI_API_KEY
AWS_SECRET_ACCESS_KEY
TOSS_SECRET_KEY
PRIVATE_KEY
ADMIN_PASSWORD
DATABASE_URL
SMTP_PASSWORD
```

중요 기준:

- 브라우저에서 필요한 값만 프론트엔드에 둔다.
- Secret은 백엔드 환경 변수 또는 Secret Manager에 둔다.
- Public Key도 도메인 제한과 사용량 제한이 필요하다.
- 이름에 `SECRET`, `PRIVATE`, `PASSWORD`, `TOKEN_SECRET`이 있으면 프론트엔드 저장 금지로 판단한다.

---

### [실무]

2026 실무 기준으로 API Secret, 결제 Secret, AI API Key는 반드시 백엔드에서만 사용한다.

잘못된 예:

```env
VITE_OPENAI_API_KEY=sk-xxxx
VITE_TOSS_SECRET_KEY=test_sk_xxxx
REACT_APP_JWT_SECRET=my-secret
```

올바른 예:

```env
VITE_API_BASE_URL=https://api.example.com
VITE_KAKAO_JS_KEY=public-browser-key
REACT_APP_APP_ENV=production
```

Agent Review 기준:

```text
.env 파일 확인
→ 변수명에 SECRET / PASSWORD / PRIVATE 포함 여부 확인
→ API Key 성격 확인
→ 브라우저에서 필요한 값인지 확인
→ Backend env로 이동 권장
```

---

### [FAQ]

Q. 프론트엔드 .env에 API Secret Key를 넣어도 되는가?
A. 안 된다. 프론트엔드 코드는 브라우저에서 확인될 수 있으므로 Secret Key는 백엔드에 보관해야 한다.

Q. Kakao JavaScript Key는 프론트엔드에 있어도 되는가?
A. 브라우저에서 사용하는 public key는 가능하지만 허용 도메인 제한과 사용량 제한이 필요하다.

Q. OpenAI API Key를 프론트엔드에 넣어도 되는가?
A. 안 된다. API Key가 노출되어 비용과 보안 문제가 발생할 수 있다.

Q. Toss Secret Key를 프론트엔드에 넣어도 되는가?
A. 안 된다. 결제 Secret Key는 반드시 백엔드에서만 사용해야 한다.

---

# 2. Build Tool Env Rules

## 2.1 Vite Environment Variable Rules

### [개념]

Vite 환경 변수는 클라이언트 코드에서 사용하려면 `VITE_` prefix를 가져야 하며 `import.meta.env`로 접근한다.

---

### [핵심]

Vite Env 규칙:

- Prefix: `VITE_`
- Access: `import.meta.env.VITE_*`
- Output: Build 시점에 값 주입
- `.env` 수정 후 dev server 재시작 필요
- `process.env.REACT_APP_*` 사용 금지
- Secret Key 저장 금지

---

### [실무]

Vite `.env.local` 예:

```env
VITE_API_BASE_URL=http://localhost:8080
VITE_APP_ENV=local
VITE_KAKAO_JS_KEY=public-local-key
```

Vite `.env.production` 예:

```env
VITE_API_BASE_URL=https://api.example.com
VITE_APP_ENV=production
VITE_KAKAO_JS_KEY=public-prod-key
```

Vite 사용 예:

```js
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
const appEnv = import.meta.env.VITE_APP_ENV;
```

잘못된 예:

```js
const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;
```

Agent 검토 Flow:

```text
Vite 프로젝트 확인
→ VITE_ prefix 확인
→ import.meta.env 사용 확인
→ undefined fallback 확인
→ secret 노출 확인
→ production env 설정 확인
```

---

### [FAQ]

Q. Vite 환경 변수 prefix는 무엇인가?
A. `VITE_`다.

Q. Vite에서 환경 변수는 어떻게 읽는가?
A. `import.meta.env.VITE_API_BASE_URL`처럼 읽는다.

Q. Vite에서 REACT*APP* 변수를 사용해도 되는가?
A. 일반적으로 안 된다. Vite 클라이언트 env는 `VITE_` prefix를 사용해야 한다.

Q. Vite에서 process.env를 사용해도 되는가?
A. 일반적인 클라이언트 코드에서는 `import.meta.env`를 사용해야 한다.

---

## 2.2 CRA Environment Variable Rules

### [개념]

CRA 환경 변수는 클라이언트 코드에서 사용하려면 `REACT_APP_` prefix를 가져야 하며 `process.env.REACT_APP_*`로 접근한다.

---

### [핵심]

CRA Env 규칙:

- Prefix: `REACT_APP_`
- Access: `process.env.REACT_APP_*`
- Output: Build 시점에 값 주입
- `.env` 수정 후 dev server 재시작 필요
- `import.meta.env.VITE_*` 사용 금지
- Secret Key 저장 금지

---

### [실무]

CRA `.env.local` 예:

```env
REACT_APP_API_BASE_URL=http://localhost:8080
REACT_APP_APP_ENV=local
REACT_APP_KAKAO_JS_KEY=public-local-key
```

CRA `.env.production` 예:

```env
REACT_APP_API_BASE_URL=https://api.example.com
REACT_APP_APP_ENV=production
REACT_APP_KAKAO_JS_KEY=public-prod-key
```

CRA 사용 예:

```js
const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;
const appEnv = process.env.REACT_APP_APP_ENV;
```

잘못된 예:

```js
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
```

Agent 검토 Flow:

```text
CRA 프로젝트 확인
→ REACT_APP_ prefix 확인
→ process.env.REACT_APP_* 사용 확인
→ undefined fallback 확인
→ secret 노출 확인
→ production env 설정 확인
```

---

### [FAQ]

Q. CRA 환경 변수 prefix는 무엇인가?
A. `REACT_APP_`다.

Q. CRA에서 환경 변수는 어떻게 읽는가?
A. `process.env.REACT_APP_API_BASE_URL`처럼 읽는다.

Q. CRA에서 VITE* 변수를 사용해도 되는가?
A. 일반적으로 안 된다. CRA 클라이언트 env는 `REACT_APP*` prefix를 사용해야 한다.

Q. CRA에서 import.meta.env를 사용해도 되는가?
A. 일반적으로 안 된다. CRA에서는 `process.env.REACT_APP_*` 방식을 사용한다.

---

## 2.3 Env Prefix Mismatch

### [개념]

Env Prefix Mismatch는 빌드 도구의 환경 변수 prefix와 코드 접근 방식이 맞지 않아 값이 `undefined`가 되는 문제다.

---

### [핵심]

대표 오류:

```text
Vite Project + REACT_APP_API_BASE_URL
→ undefined 가능

CRA Project + VITE_API_BASE_URL
→ undefined 가능

Vite Project + process.env.REACT_APP_API_BASE_URL
→ undefined 가능

CRA Project + import.meta.env.VITE_API_BASE_URL
→ undefined 가능
```

결과:

- API Base URL undefined
- Axios baseURL 잘못 설정
- API 요청 실패
- 흰 화면
- runtime error
- 운영 배포 실패

---

### [실무]

오류 예:

```js
const api = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
});
```

위 코드가 Vite 프로젝트에 있으면 baseURL이 undefined 될 수 있다.

수정 예:

```js
const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
});
```

Agent Troubleshooting Flow:

```text
API URL undefined 확인
→ Build Tool 확인
→ env prefix 확인
→ env access 방식 확인
→ dev server 재시작
→ rebuild
```

---

### [FAQ]

Q. API Base URL이 undefined가 되는 이유는?
A. Build Tool에 맞지 않는 env prefix나 접근 방식을 사용했을 가능성이 높다.

Q. Vite에서 REACT*APP* env를 쓰면 왜 안 되는가?
A. Vite는 클라이언트 노출 변수로 `VITE_` prefix를 요구하기 때문이다.

Q. CRA에서 VITE* env를 쓰면 왜 안 되는가?
A. CRA는 클라이언트 노출 변수로 `REACT_APP*` prefix를 요구하기 때문이다.

Q. env prefix를 수정한 뒤 무엇을 해야 하는가?
A. 개발 서버를 재시작하고 운영에서는 다시 Build해야 한다.

---

# 3. Environment File Rules

## 3.1 Environment File Types

### [개념]

Environment File은 환경별 설정 값을 분리하기 위한 `.env` 계열 파일이다.

대표 파일:

```text
.env
.env.local
.env.development
.env.production
.env.test
.env.example
```

---

### [핵심]

파일 역할:

| 파일               | 역할             |
| ------------------ | ---------------- |
| `.env`             | 공통 기본값      |
| `.env.local`       | 로컬 개인 설정   |
| `.env.development` | 개발 환경 설정   |
| `.env.production`  | 운영 Build 설정  |
| `.env.test`        | 테스트 환경 설정 |
| `.env.example`     | 공유용 예시 파일 |

중요 규칙:

- 실제 Secret이 있는 env 파일은 Git에 올리지 않는다.
- 프론트엔드 env에는 Secret을 넣지 않는다.
- `.env.example`은 Git에 올려도 된다.
- `.env.local`은 보통 Git에서 제외한다.
- 환경별 API URL을 분리한다.

---

### [실무]

권장 구조:

```text
frontend/
├ .env.example
├ .env.local
├ .env.development
├ .env.production
├ package.json
└ src/
```

Vite `.env.example` 예:

```env
VITE_API_BASE_URL=
VITE_APP_ENV=
VITE_KAKAO_JS_KEY=
```

CRA `.env.example` 예:

```env
REACT_APP_API_BASE_URL=
REACT_APP_APP_ENV=
REACT_APP_KAKAO_JS_KEY=
```

Agent 검토 기준:

```text
.env.example 존재
→ 협업 가능성 좋음

.env.local Git 추적
→ Review 필요

.env.production에 localhost
→ Deploy Risk

Secret 포함
→ Critical Issue
```

---

### [FAQ]

Q. .env.example은 왜 필요한가?
A. 팀원이 필요한 환경 변수 목록을 알 수 있도록 공유하기 위해 필요하다.

Q. .env.local은 Git에 올려도 되는가?
A. 보통 올리지 않는다. 개인 로컬 설정이 포함될 수 있기 때문이다.

Q. .env.production에는 무엇을 넣는가?
A. 운영 API URL, 운영 앱 환경, public key 같은 운영용 공개 설정을 넣는다.

Q. 프론트엔드 .env에 Secret이 없다면 Git에 올려도 되는가?
A. 가능은 하지만 보통 실제 env 파일 대신 `.env.example`만 올리는 것이 안전하다.

---

## 3.2 Git Ignore Rules

### [개념]

Git Ignore Rules는 실제 환경 변수 파일이 저장소에 올라가지 않도록 제어하는 규칙이다.

---

### [핵심]

권장 `.gitignore`:

```gitignore
# env
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# keep example
!.env.example
```

상황별 판단:

- 개인 설정 포함 → ignore
- 운영 값 포함 → ignore
- Secret 포함 → 반드시 ignore 및 키 폐기 검토
- 공유 템플릿 → `.env.example` 사용
- public 값만 포함 → 가능하지만 팀 정책에 맞춰 결정

---

### [실무]

2026 실무 기준으로 env 파일 노출은 즉시 보안 사고로 판단해야 한다.

Review Agent 조치 Flow:

```text
.env Git 추적 여부 확인
→ Secret 포함 여부 확인
→ 노출된 Secret 폐기 필요 여부 판단
→ .gitignore 수정
→ .env.example 생성
→ Git history 노출 여부 확인
```

주의:

```text
Git에서 파일 삭제
≠
Git history에서 Secret 제거
```

Secret이 commit된 경우:

```text
해당 Key 폐기
→ 새 Key 발급
→ Git history 정리 검토
→ 재노출 방지
```

---

### [FAQ]

Q. .env 파일을 GitHub에 올리면 안 되는가?
A. Secret이나 개인 설정이 포함될 수 있으므로 보통 올리지 않는다.

Q. .env.example은 GitHub에 올려도 되는가?
A. 가능하다. 실제 값 없이 변수 목록만 제공하는 용도다.

Q. 실수로 Secret을 commit했다면 파일만 지우면 되는가?
A. 아니다. Secret을 폐기하고 Git history 노출도 검토해야 한다.

Q. 프론트엔드 env에는 Secret이 없는데도 ignore해야 하는가?
A. 팀 정책에 따라 다르지만 일반적으로 실제 env 파일은 제외하고 example만 공유한다.

---

## 3.3 Environment Mode

### [개념]

Environment Mode는 Build Tool이 어떤 환경 설정 파일과 실행 모드를 사용할지 결정하는 기준이다.

---

### [핵심]

대표 Mode:

```text
development
production
test
staging
local
```

중요 포인트:

- `npm run dev`는 보통 development mode
- `npm run build`는 보통 production mode
- Vite는 `--mode`로 mode 지정 가능
- CRA는 mode 제어가 제한적이며 react-scripts 기준 동작
- mode와 env file 적용 순서를 확인해야 한다.

---

### [실무]

Vite staging build 예:

```bash
vite build --mode staging
```

package.json 예:

```json
{
  "scripts": {
    "build": "vite build",
    "build:staging": "vite build --mode staging",
    "build:prod": "vite build --mode production"
  }
}
```

파일 예:

```text
.env.staging
.env.production
```

Agent 판단 Flow:

```text
build script 확인
→ mode 지정 여부 확인
→ 해당 env file 존재 확인
→ API URL 값 확인
→ build 결과에서 값 확인
```

---

### [FAQ]

Q. npm run build는 어떤 mode인가?
A. 일반적으로 production mode다.

Q. staging 환경은 어떻게 분리하는가?
A. Vite에서는 `--mode staging`과 `.env.staging`을 사용할 수 있다.

Q. mode를 바꿨는데 값이 안 바뀌는 이유는?
A. env file 이름, script mode, 변수 prefix, build 재실행 여부를 확인해야 한다.

Q. CRA에서도 mode를 자유롭게 쓸 수 있는가?
A. CRA는 Vite보다 mode 제어가 제한적이므로 react-scripts 동작 기준을 확인해야 한다.

---

# 4. Build-time Env vs Runtime Config

## 4.1 Build-time Environment Variable

### [개념]

Build-time Environment Variable은 Build 시점에 코드에 주입되어 정적 파일 안에 포함되는 환경 변수다.

---

### [핵심]

Build-time Env 특징:

- Build 시점에 값이 고정된다.
- 배포 후 값을 바꾸려면 일반적으로 다시 Build해야 한다.
- React SPA에서 가장 흔한 방식이다.
- 코드 번들에 값이 포함될 수 있다.
- Secret 저장 금지 원칙이 강하게 적용된다.

---

### [실무]

Build-time Env Flow:

```text
.env.production 작성
→ npm run build
→ JS bundle에 값 주입
→ dist/build 배포
→ Browser에서 주입된 값 사용
```

문제 상황:

```text
운영 배포 후 env만 수정
→ 기존 JS bundle 값 유지
→ 변경 반영 안 됨
```

해결:

```text
env 수정
→ rebuild
→ redeploy
→ cache invalidation 필요 시 수행
```

Agent 판단 기준:

```text
"env 바꿨는데 배포 화면이 그대로"
→ Build-time Env 가능성 확인
→ Rebuild 필요 안내
```

---

### [FAQ]

Q. React env는 배포 후 바꿀 수 있는가?
A. 일반적으로 Build 시점에 고정되므로 배포 후 변경하려면 다시 Build해야 한다.

Q. env 파일만 서버에서 바꾸면 화면에 반영되는가?
A. 일반 React SPA에서는 보통 반영되지 않는다.

Q. Build-time Env는 왜 Secret 저장에 위험한가?
A. JS bundle에 포함되어 브라우저에서 확인될 수 있기 때문이다.

Q. API URL을 바꾸려면 무엇을 해야 하는가?
A. env를 수정하고 다시 Build 후 재배포해야 한다.

---

## 4.2 Runtime Config Rules

### [개념]

Runtime Config는 Build 후에도 외부 설정 파일을 통해 일부 설정 값을 변경할 수 있게 하는 방식이다.

---

### [핵심]

Runtime Config가 필요한 상황:

- 동일 Build 결과물을 여러 환경에 배포
- Docker 이미지 하나로 dev / staging / production 대응
- 배포 후 API URL만 변경 필요
- 재빌드 없이 public 설정 변경 필요
- 환경별 config를 서버에서 제공해야 함

주의:

- Runtime Config도 브라우저에서 접근 가능하다.
- Secret 저장 금지
- 앱 초기화 전에 config loading 필요
- config fetch 실패 대응 필요
- cache 설정 주의

---

### [실무]

`public/config.json` 예:

```json
{
  "apiBaseUrl": "https://api.example.com",
  "appEnv": "production"
}
```

로드 예:

```js
async function loadConfig() {
  const response = await fetch("/config.json", { cache: "no-store" });
  return response.json();
}
```

앱 초기화 Flow:

```text
Browser loads index.html
→ App boot before API init
→ fetch /config.json
→ create Axios instance
→ render App
```

Agent 검토 기준:

```text
Runtime Config 사용
→ Secret 포함 여부 확인
→ fetch 실패 fallback 확인
→ cache policy 확인
→ app init 순서 확인
```

---

### [FAQ]

Q. Runtime Config란 무엇인가?
A. Build 후에도 외부 config 파일을 읽어 public 설정을 바꿀 수 있게 하는 방식이다.

Q. Runtime Config에 Secret을 넣어도 되는가?
A. 안 된다. config 파일도 브라우저에서 접근 가능하다.

Q. Runtime Config는 언제 필요한가?
A. 동일 Build 파일을 여러 환경에 배포하거나 Docker 이미지 하나로 환경을 나누고 싶을 때 유용하다.

Q. config.json이 캐시되면 어떤 문제가 생기는가?
A. API URL 같은 설정 변경이 즉시 반영되지 않을 수 있다.

---

## 4.3 Docker Env Misunderstanding

### [개념]

Docker Env Misunderstanding은 컨테이너 실행 시점 env를 바꾸면 React SPA의 Build-time Env도 자동 변경된다고 착각하는 문제다.

---

### [핵심]

문제 원인:

```text
React SPA env
→ Build 시점 주입

Docker container env
→ 실행 시점 주입

Build-time Env ≠ Runtime Env
```

잘못된 기대:

```text
docker run -e VITE_API_BASE_URL=https://api.prod.com frontend
→ 이미 build된 JS bundle 값은 바뀌지 않을 수 있음
```

해결 방법:

- Docker image build 시 env 주입
- 환경별 image를 별도 build
- Runtime Config 사용
- Nginx entrypoint에서 config.json 생성
- 서버에서 `/config.json` 제공

---

### [실무]

Runtime Config 생성 예:

```sh
cat <<EOF > /usr/share/nginx/html/config.json
{
  "apiBaseUrl": "${API_BASE_URL}",
  "appEnv": "${APP_ENV}"
}
EOF
```

Docker 전략 선택:

```text
환경별 빌드 가능
→ Build-time Env 사용 가능

이미지 하나로 여러 환경 배포 필요
→ Runtime Config 권장
```

Agent 판단 Flow:

```text
Docker 배포 여부 확인
→ env 주입 시점 확인
→ React env 방식 확인
→ build-time인지 runtime인지 분류
→ config 전략 제안
```

---

### [FAQ]

Q. Docker run -e로 React env를 바꾸면 화면에 반영되는가?
A. 일반 Build-time Env 방식에서는 반영되지 않을 수 있다.

Q. Docker에서 React API URL을 실행 시점에 바꾸려면 어떻게 하는가?
A. Runtime Config 또는 컨테이너 시작 시 config.json 생성 전략을 사용할 수 있다.

Q. Docker 이미지 하나로 dev와 production을 모두 처리할 수 있는가?
A. Runtime Config를 사용하면 가능하다.

Q. Build-time Env와 Runtime Env는 같은가?
A. 아니다. Build-time Env는 빌드 시점, Runtime Env는 실행 시점 설정이다.

---

# 5. API Base URL Env

## 5.1 API Base URL Separation

### [개념]

API Base URL Separation은 개발, 테스트, 운영 환경별 API 주소를 환경 변수로 분리하는 규칙이다.

---

### [핵심]

환경별 API URL 예:

```text
Local
→ http://localhost:8080

Development Server
→ https://dev-api.example.com

Staging
→ https://staging-api.example.com

Production
→ https://api.example.com

Same Origin Proxy
→ /api
```

중요 규칙:

- 운영 Build에 `localhost`가 남으면 안 된다.
- HTTPS 페이지에서는 HTTPS API를 사용해야 한다.
- Same Origin Proxy 구조에서는 `/api` 사용 가능
- API prefix와 백엔드 path 충돌을 확인해야 한다.
- CORS / Cookie / Authorization 방식과 함께 검토해야 한다.

---

### [실무]

Vite 예:

```env
VITE_API_BASE_URL=/api
```

CRA 예:

```env
REACT_APP_API_BASE_URL=/api
```

Axios 예:

```js
import axios from "axios";

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 10000,
});
```

Review Agent 확인:

```text
Production env 확인
→ API URL이 localhost인지 확인
→ HTTP/HTTPS 확인
→ /api proxy 사용 여부 확인
→ CORS 필요 여부 확인
```

---

### [FAQ]

Q. API Base URL은 왜 환경 변수로 분리하는가?
A. 로컬, 개발, 운영 환경의 백엔드 주소가 다르기 때문이다.

Q. 운영 env에 localhost가 있으면 안 되는가?
A. 안 된다. 사용자 브라우저 기준 localhost는 사용자 자신의 PC를 의미한다.

Q. baseURL을 /api로 써도 되는가?
A. 가능하다. 같은 도메인에서 Nginx나 백엔드가 `/api`를 실제 API 서버로 proxy해야 한다.

Q. HTTPS 사이트에서 HTTP API를 호출해도 되는가?
A. 안 된다. 브라우저가 Mixed Content로 차단할 수 있다.

---

## 5.2 Localhost Risk

### [개념]

Localhost Risk는 운영 Build 결과물에 개발용 `localhost` API 주소가 포함되어 사용자 브라우저에서 API 요청이 실패하는 문제다.

---

### [핵심]

문제 상황:

```text
Frontend: https://example.com
API Base URL: http://localhost:8080
Browser Request: 사용자 PC의 localhost:8080으로 요청
Result: API 실패
```

대표 원인:

- `.env.production` 누락
- production env 설정 실패
- build 시점에 local env 사용
- 코드에 localhost 하드코딩
- fallback 기본값이 localhost
- CI/CD env 미설정

---

### [실무]

위험한 코드:

```js
const baseURL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8080";
```

운영에서 env가 누락되면 localhost로 요청될 수 있다.

개선 예:

```js
const baseURL = import.meta.env.VITE_API_BASE_URL;

if (!baseURL) {
  throw new Error("VITE_API_BASE_URL is required");
}
```

Agent 검토 Flow:

```text
코드에서 localhost 검색
→ env fallback 확인
→ production env 확인
→ build output/API request URL 확인
→ Network 탭에서 실제 요청 확인
```

---

### [FAQ]

Q. 배포했는데 API가 localhost로 호출되는 이유는?
A. 운영 환경 변수 누락 또는 코드에 localhost fallback이 남아 있기 때문이다.

Q. 운영에서 localhost fallback을 둬도 되는가?
A. 권장하지 않는다. 운영 env 누락을 숨겨 장애를 만들 수 있다.

Q. localhost를 어디서 검색해야 하는가?
A. `.env`, axios instance, config 파일, API client, build output, CI/CD env 설정을 확인한다.

Q. localhost가 사용자 브라우저에서 의미하는 것은?
A. 배포 서버가 아니라 사용자의 PC다.

---

# 6. Env Validation

## 6.1 Required Env Validation

### [개념]

Required Env Validation은 필수 환경 변수가 누락되었을 때 조기에 실패하도록 검증하는 방식이다.

---

### [핵심]

검증 대상:

- API Base URL
- App Environment
- Public API Key
- OAuth Client ID
- Feature Flag
- Runtime Config URL

검증 목적:

- undefined API 요청 방지
- localhost fallback 방지
- 배포 환경 설정 누락 조기 발견
- 운영 장애 예방
- Review Agent 판단 기준 제공

---

### [실무]

Vite 검증 예:

```js
const requiredEnv = {
  apiBaseUrl: import.meta.env.VITE_API_BASE_URL,
  appEnv: import.meta.env.VITE_APP_ENV,
};

Object.entries(requiredEnv).forEach(([key, value]) => {
  if (!value) {
    throw new Error(`Missing required env: ${key}`);
  }
});

export const env = requiredEnv;
```

CRA 검증 예:

```js
const requiredEnv = {
  apiBaseUrl: process.env.REACT_APP_API_BASE_URL,
  appEnv: process.env.REACT_APP_APP_ENV,
};

Object.entries(requiredEnv).forEach(([key, value]) => {
  if (!value) {
    throw new Error(`Missing required env: ${key}`);
  }
});

export const env = requiredEnv;
```

Agent 판단 기준:

```text
필수 env 검증 없음
→ Warning

운영 API URL fallback이 localhost
→ High Risk

누락 시 즉시 throw
→ Fail Fast로 긍정적
```

---

### [FAQ]

Q. 필수 env 검증은 왜 필요한가?
A. 환경 변수 누락으로 API 요청 실패나 잘못된 운영 배포가 발생하는 것을 조기에 막기 위해 필요하다.

Q. env가 없을 때 localhost fallback을 주면 안전한가?
A. 운영에서는 위험하다. env 누락을 숨겨 배포 후 장애가 될 수 있다.

Q. env 누락 시 앱을 중단해도 되는가?
A. 필수 설정이라면 조기에 실패시키는 것이 장애 원인 파악에 유리하다.

Q. env validation은 어디에 두는가?
A. API client 초기화 전 또는 앱 초기화 초기에 두는 것이 좋다.

---

## 6.2 Env Type Safety

### [개념]

Env Type Safety는 환경 변수 이름과 값 사용을 타입 또는 중앙 모듈로 관리해 오타와 undefined 문제를 줄이는 방식이다.

---

### [핵심]

Env Type Safety 목적:

- env 이름 오타 방지
- undefined 사용 방지
- API client 설정 일관성 유지
- 앱 전체에서 env 접근 방식 통일
- Review Agent 검토 범위 단순화

---

### [실무]

Vite TypeScript 예:

```ts
interface ImportMetaEnv {
  readonly VITE_API_BASE_URL: string;
  readonly VITE_APP_ENV: string;
  readonly VITE_KAKAO_JS_KEY?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
```

중앙 env 모듈 예:

```ts
export const env = {
  apiBaseUrl: import.meta.env.VITE_API_BASE_URL,
  appEnv: import.meta.env.VITE_APP_ENV,
} as const;
```

권장 사용:

```ts
import { env } from "./env";

api.get(`${env.apiBaseUrl}/health`);
```

비권장:

```ts
import.meta.env.VITE_API_BASE_URL;
process.env.REACT_APP_API_BASE_URL;
```

앱 곳곳에서 직접 반복 사용.

---

### [FAQ]

Q. env 중앙 모듈은 왜 필요한가?
A. 환경 변수 접근을 한 곳에 모아 오타, undefined, 빌드 도구 혼동을 줄이기 위해 필요하다.

Q. TypeScript에서 env 타입을 지정하면 무엇이 좋은가?
A. 변수명 오타를 줄이고 코드 자동완성과 검토가 쉬워진다.

Q. env를 여러 파일에서 직접 읽어도 되는가?
A. 가능하지만 중앙 모듈로 통일하는 것이 유지보수와 검토에 유리하다.

Q. env 타입을 지정해도 실제 값 누락을 막을 수 있는가?
A. 타입만으로는 부족하다. runtime validation도 함께 사용하는 것이 좋다.

---

# 7. Platform Env Rules

## 7.1 CI/CD Environment Variable

### [개념]

CI/CD Environment Variable은 GitHub Actions 같은 자동화 환경에서 Build 시점에 주입하는 환경 변수다.

---

### [핵심]

CI/CD Env 확인 항목:

- Repository Variables
- Repository Secrets
- Environment Variables
- Build Job env
- Working Directory
- Build Mode
- Secret 노출 방지
- Production URL 값 확인

중요 규칙:

- Secret은 GitHub Secrets에 저장한다.
- 프론트엔드에 주입되는 값은 결국 브라우저에 노출될 수 있다.
- `VITE_`, `REACT_APP_` prefix 규칙을 지킨다.
- CI/CD Build 로그에 민감 정보가 출력되지 않게 한다.

---

### [실무]

GitHub Actions Vite 예:

```yaml
- name: Build Frontend
  working-directory: ./frontend
  env:
    VITE_API_BASE_URL: ${{ vars.VITE_API_BASE_URL }}
    VITE_APP_ENV: production
  run: npm run build
```

CRA 예:

```yaml
- name: Build Frontend
  working-directory: ./frontend
  env:
    REACT_APP_API_BASE_URL: ${{ vars.REACT_APP_API_BASE_URL }}
    REACT_APP_APP_ENV: production
  run: npm run build
```

Agent 검토 Flow:

```text
CI workflow 확인
→ working-directory 확인
→ env prefix 확인
→ production API URL 확인
→ secret 노출 여부 확인
→ build log 확인
```

---

### [FAQ]

Q. CI/CD에서 env를 설정해야 하는 이유는?
A. Production Build 시점에 운영 API URL 같은 값이 필요하기 때문이다.

Q. GitHub Secrets에 넣으면 프론트엔드에서 안전한가?
A. Build 결과에 포함되는 값은 브라우저에 노출될 수 있다. Secret 자체를 프론트엔드에 주입하면 안 된다.

Q. GitHub Actions에서 env가 안 들어가는 이유는?
A. workflow env 설정, working-directory, 변수명 prefix, repository variables/secrets 설정을 확인해야 한다.

Q. CI에서 env를 echo로 출력해도 되는가?
A. 민감 정보는 출력하면 안 된다. public 값도 불필요한 로그 노출은 피하는 것이 좋다.

---

## 7.2 Hosting Platform Env

### [개념]

Hosting Platform Env는 Vercel, Netlify, Render, Cloudflare Pages 같은 배포 플랫폼에서 설정하는 환경 변수다.

---

### [핵심]

플랫폼 Env 공통 규칙:

- Dashboard에서 환경별 env 설정
- Production / Preview / Development 분리 가능
- Build 시점에 env 반영
- 변경 후 재배포 필요 가능
- Build Tool prefix 규칙 준수
- Secret을 프론트엔드 env에 주입 금지

대표 플랫폼:

```text
Vercel
Netlify
Cloudflare Pages
Render Static Site
AWS Amplify
```

---

### [실무]

Vercel / Netlify 설정 예:

```text
VITE_API_BASE_URL=https://api.example.com
VITE_APP_ENV=production
```

또는 CRA:

```text
REACT_APP_API_BASE_URL=https://api.example.com
REACT_APP_APP_ENV=production
```

Agent 확인 항목:

```md
- [ ] platform env가 설정되어 있는가?
- [ ] production env와 preview env가 구분되어 있는가?
- [ ] env 변경 후 redeploy 되었는가?
- [ ] API URL이 localhost가 아닌가?
- [ ] prefix가 Build Tool과 맞는가?
- [ ] secret이 포함되어 있지 않은가?
```

---

### [FAQ]

Q. Vercel이나 Netlify에서는 .env 파일을 올려야 하는가?
A. 보통 Dashboard의 Environment Variables에 설정한다.

Q. 플랫폼 env를 바꾸면 즉시 반영되는가?
A. Build-time env라면 보통 재배포가 필요하다.

Q. Preview와 Production env는 다르게 설정할 수 있는가?
A. 대부분의 플랫폼에서 가능하다.

Q. 플랫폼 env에도 Secret을 넣으면 안전한가?
A. 백엔드용 Secret은 안전할 수 있지만 프론트엔드 Build에 주입하면 브라우저에 노출될 수 있다.

---

# 8. Env Troubleshooting

## 8.1 Env Undefined Troubleshooting

### [개념]

Env Undefined는 코드에서 환경 변수를 읽었지만 값이 존재하지 않아 `undefined`가 되는 문제다.

---

### [핵심]

대표 원인:

- prefix 불일치
- access 방식 불일치
- `.env` 파일 위치 오류
- `.env` 파일명 오류
- dev server 재시작 누락
- Build mode 불일치
- CI/CD env 설정 누락
- Hosting Platform env 설정 누락
- 오타
- env 중앙 모듈 미사용

---

### [실무]

Troubleshooting Flow:

```text
Build Tool 확인
→ env prefix 확인
→ env access 방식 확인
→ .env 위치 확인
→ .env 파일명 확인
→ dev server 재시작
→ build mode 확인
→ CI/CD env 확인
→ 배포 플랫폼 env 확인
```

Vite 확인:

```text
VITE_ prefix
import.meta.env
frontend root의 .env
```

CRA 확인:

```text
REACT_APP_ prefix
process.env.REACT_APP_*
frontend root의 .env
```

---

### [FAQ]

Q. env 값이 undefined인 이유는?
A. prefix, 접근 방식, 파일 위치, mode, 서버 재시작, CI/CD 설정 누락 중 하나일 가능성이 높다.

Q. .env 파일은 어디에 있어야 하는가?
A. 보통 해당 프론트엔드 프로젝트의 `package.json`이 있는 루트에 있어야 한다.

Q. .env 수정 후 무엇을 해야 하는가?
A. 개발 서버를 재시작하고 운영에서는 다시 Build해야 한다.

Q. env 이름 오타를 줄이려면 어떻게 하는가?
A. env 중앙 모듈과 TypeScript 타입 정의를 사용하는 것이 좋다.

---

## 8.2 Wrong API URL Troubleshooting

### [개념]

Wrong API URL은 환경 변수 값이 잘못되어 API 요청이 잘못된 서버로 나가는 문제다.

---

### [핵심]

대표 증상:

- API가 localhost로 호출됨
- API가 undefined 경로로 호출됨
- `/api/api` 중복 경로 발생
- HTTPS 페이지에서 HTTP API 호출
- staging 화면이 production API 호출
- production 화면이 dev API 호출
- CORS 에러 발생
- 404 / 401 / 500 발생

---

### [실무]

Network 확인 기준:

```text
Browser DevTools
→ Network
→ Request URL
→ Status Code
→ Response Body
→ Request Headers
→ Authorization / Cookie 확인
```

Troubleshooting Flow:

```text
Network Request URL 확인
→ env 값 확인
→ Axios baseURL 확인
→ API path 조합 확인
→ proxy 설정 확인
→ backend route 확인
→ CORS / HTTPS 확인
```

잘못된 조합 예:

```js
baseURL = "https://api.example.com/api";
api.get("/api/festivals");
```

결과:

```text
https://api.example.com/api/api/festivals
```

---

### [FAQ]

Q. 배포 후 API가 localhost로 호출되는 이유는?
A. 운영 env가 누락되었거나 Build 시점에 local env가 들어갔기 때문이다.

Q. API 경로에 /api가 두 번 붙는 이유는?
A. baseURL과 개별 요청 path 양쪽에 `/api`가 중복되었기 때문이다.

Q. staging에서 production API를 호출하는 이유는?
A. Build mode 또는 플랫폼 env 설정이 잘못되었을 수 있다.

Q. API URL 문제는 어디서 확인하는가?
A. 브라우저 개발자 도구 Network 탭의 Request URL을 확인한다.

---

## 8.3 Env Cache Issue

### [개념]

Env Cache Issue는 env를 수정하고 재빌드했지만 브라우저, CDN, Service Worker 캐시 때문에 이전 설정이 계속 사용되는 문제다.

---

### [핵심]

원인:

- Browser Cache
- CDN Cache
- CloudFront Cache
- Service Worker Cache
- 오래 캐시된 `index.html`
- 이전 JS bundle 참조
- Runtime Config 캐시

증상:

- API URL이 예전 값으로 유지
- 배포했는데 이전 화면 표시
- 새 env가 적용되지 않음
- 일부 사용자만 이전 API 호출
- chunk load error 발생

---

### [실무]

Troubleshooting Flow:

```text
Hard Reload
→ Network Disable Cache 테스트
→ index.html cache-control 확인
→ JS bundle hash 확인
→ CDN invalidation 확인
→ Service Worker 확인
→ config.json cache 확인
```

Runtime Config 사용 시:

```js
fetch("/config.json", { cache: "no-store" });
```

Cache 전략:

```text
index.html
→ no-cache 또는 짧은 cache

assets/*.hash.js
→ long cache 가능

config.json
→ no-store 또는 짧은 cache
```

---

### [FAQ]

Q. env를 바꾸고 재배포했는데 이전 API URL로 호출되는 이유는?
A. 브라우저 캐시, CDN 캐시, Service Worker, index.html 캐시 문제일 수 있다.

Q. index.html을 오래 캐시하면 왜 위험한가?
A. 이전 JS bundle을 참조해 새 배포와 mismatch가 발생할 수 있다.

Q. Runtime Config의 config.json도 캐시 문제가 생기는가?
A. 가능하다. API URL 변경이 필요한 config는 캐시를 짧게 하거나 no-store로 처리해야 한다.

Q. CloudFront 사용 시 env 변경 후 무엇을 확인해야 하는가?
A. 배포 후 invalidation이 필요한지 확인해야 한다.

---

# 9. Agent Decision Rules

## 9.1 PM Agent Rules

### [개념]

PM Agent는 환경 변수의 목적, 범위, 보안 기준, 배포 환경별 값을 정리해야 한다.

---

### [핵심]

PM Agent 확인 항목:

- Build Tool
- Env Prefix
- Required Env List
- Local Env
- Development Env
- Staging Env
- Production Env
- API Base URL
- Public Key 목록
- Secret 분리 여부
- Runtime Config 필요 여부
- CI/CD env 설정 여부
- Hosting Platform env 설정 여부

---

### [실무]

PM Agent 산출물 예:

```text
Build Tool: CRA
Env Prefix: REACT_APP_
Required Env:
- REACT_APP_API_BASE_URL
- REACT_APP_APP_ENV
- REACT_APP_KAKAO_JS_KEY

Production API:
- https://api.example.com

Secret Policy:
- frontend env에 secret 저장 금지
- secret은 backend env 또는 secret manager 사용
```

PM Agent 판단 Flow:

```text
배포 환경 정의
→ 필요한 env 목록 작성
→ public/secret 분류
→ build-time/runtime 방식 결정
→ CI/CD 또는 플랫폼 env 설정 계획
→ Review Checklist 전달
```

---

### [FAQ]

Q. PM Agent는 env에서 무엇을 정리해야 하는가?
A. 필요한 env 목록, 환경별 값, public/secret 구분, Build Tool prefix, 배포 설정 위치를 정리해야 한다.

Q. PM Agent가 Secret 위치도 판단해야 하는가?
A. 그렇다. Secret은 프론트엔드가 아니라 백엔드 또는 Secret Manager에 둬야 한다.

Q. Runtime Config 필요 여부는 누가 판단하는가?
A. PM Agent가 배포 전략에 따라 판단하고 Frontend Agent와 DevOps Agent가 구현한다.

---

## 9.2 Frontend Agent Rules

### [개념]

Frontend Agent는 Build Tool 규칙에 맞게 env를 읽고, API Client와 앱 설정을 안전하게 초기화해야 한다.

---

### [핵심]

Frontend Agent 필수 기준:

- Build Tool별 prefix 준수
- Env Access 방식 통일
- Env 중앙 모듈 사용 권장
- Required Env Validation 적용
- Secret 저장 금지
- API URL 하드코딩 금지
- 운영 localhost fallback 금지
- Runtime Config 사용 시 app initialization 순서 보장
- env 변경 후 rebuild 필요성 인지

---

### [실무]

Vite env module 예:

```js
export const env = {
  apiBaseUrl: import.meta.env.VITE_API_BASE_URL,
  appEnv: import.meta.env.VITE_APP_ENV,
};

Object.entries(env).forEach(([key, value]) => {
  if (!value) {
    throw new Error(`Missing env: ${key}`);
  }
});
```

Axios 사용 예:

```js
import axios from "axios";
import { env } from "./env";

export const api = axios.create({
  baseURL: env.apiBaseUrl,
  timeout: 10000,
});
```

Frontend Agent 금지:

```text
코드에 운영 API URL 직접 하드코딩
코드에 localhost fallback 방치
secret key를 env에 저장
env를 여러 파일에서 무분별하게 직접 접근
```

---

### [FAQ]

Q. Frontend Agent는 env를 어떻게 관리해야 하는가?
A. Build Tool prefix를 지키고 env 중앙 모듈과 필수 값 검증을 사용하는 것이 좋다.

Q. API URL을 코드에 직접 하드코딩해도 되는가?
A. 권장하지 않는다. 환경별 변경을 위해 env로 분리해야 한다.

Q. env 누락 시 localhost fallback을 둬도 되는가?
A. 운영에서는 위험하다. 필수 env는 누락 시 실패시키는 것이 좋다.

Q. Runtime Config를 쓰면 Frontend Agent가 무엇을 주의해야 하는가?
A. 앱 초기화 전에 config를 로드하고 실패 대응과 캐시 정책을 고려해야 한다.

---

## 9.3 Review Agent Rules

### [개념]

Review Agent는 프론트엔드 환경 변수의 보안, prefix, build 반영, 운영 API URL, cache 위험을 검토해야 한다.

---

### [핵심]

Review Agent Checklist:

```md
- [ ] Build Tool에 맞는 env prefix 사용
- [ ] Env Access 방식 정상
- [ ] Required Env Validation 존재
- [ ] API Base URL 환경별 분리
- [ ] 운영 env에 localhost 없음
- [ ] Secret Key 프론트엔드 env에 없음
- [ ] .env.local Git 제외
- [ ] .env.example 존재
- [ ] CI/CD env 설정 확인
- [ ] Hosting Platform env 설정 확인
- [ ] Runtime Config 사용 시 cache 정책 확인
- [ ] Docker 사용 시 env 주입 시점 확인
```

---

### [실무]

Review Agent 판단 Flow:

```text
Build Tool 확인
→ env prefix 확인
→ env 파일 확인
→ env 사용 코드 확인
→ secret 노출 확인
→ production API URL 확인
→ build 실행
→ Network Request URL 확인
```

Critical Issue:

```text
Frontend env에 Secret Key 존재
Production API URL이 localhost
Vite/CRA env prefix 불일치
API URL undefined
Docker runtime env 오해
```

승인 기준:

```text
Secret 미노출
Env prefix 정상
Required Env 검증 가능
Production API URL 정상
Network Request URL 정상
Cache 위험 대응 가능
```

---

### [FAQ]

Q. Review Agent는 env에서 가장 먼저 무엇을 확인하는가?
A. Secret 노출 여부와 Build Tool에 맞는 prefix 사용 여부를 먼저 확인한다.

Q. 운영 env에 localhost가 있으면 승인 가능한가?
A. 아니다. 운영 사용자의 브라우저에서 API 요청이 실패할 수 있다.

Q. env가 Git에 올라간 경우 무엇을 확인해야 하는가?
A. Secret 포함 여부, Git history 노출 여부, key 폐기 필요 여부를 확인해야 한다.

Q. Docker 배포 env는 무엇을 확인해야 하는가?
A. env가 Build 시점에 필요한지 Runtime 시점에 필요한지 확인해야 한다.

---

# 10. Common Mistakes

## 10.1 Environment Variable Common Mistakes

### [개념]

Environment Variable Common Mistakes는 프론트엔드 배포와 API 연동 실패로 이어지는 반복 실수다.

---

### [핵심]

자주 발생하는 실수:

- 프론트엔드 env에 Secret Key 저장
- Vite에서 `REACT_APP_` 사용
- CRA에서 `VITE_` 사용
- Vite에서 `process.env` 사용
- CRA에서 `import.meta.env` 사용
- `.env` 수정 후 dev server 재시작 안 함
- 운영 env 수정 후 rebuild 안 함
- 운영 API URL이 localhost로 남음
- localhost fallback 코드 방치
- `.env.production` 누락
- CI/CD env 설정 누락
- Hosting Platform env 설정 누락
- Docker run env로 Build-time Env가 바뀐다고 착각
- Runtime Config에 Secret 저장
- config.json cache 설정 누락
- `.env.example` 미작성
- `.env.local` Git commit
- API path에 `/api` 중복
- staging과 production env 혼동

---

### [실무]

실수별 판단:

```text
API URL undefined
→ prefix / access 방식 확인

API가 localhost 호출
→ production env / fallback / build 시점 확인

env 수정했는데 반영 안 됨
→ dev server restart / rebuild / cache 확인

Docker env가 반영 안 됨
→ build-time env vs runtime env 확인

Secret 노출
→ key 폐기 / backend 이동 / history 확인
```

---

### [FAQ]

Q. env 관련 가장 위험한 실수는 무엇인가?
A. Secret Key를 프론트엔드 env에 저장하는 것이다.

Q. env 관련 가장 흔한 배포 장애는 무엇인가?
A. 운영 API URL이 localhost로 남거나 env prefix가 틀려 undefined가 되는 문제다.

Q. env 변경이 반영되지 않는 가장 흔한 이유는?
A. 개발 서버 재시작 또는 Production Rebuild를 하지 않았기 때문이다.

Q. Docker에서 env 문제가 많이 나는 이유는?
A. React SPA의 Build-time Env와 컨테이너 Runtime Env를 혼동하기 때문이다.

---

# 11. Part03 Quality Checklist

## 11.1 Document Quality

### [개념]

이 문서는 Frontend Build & Deploy Domain의 Part03이며 Environment Variable Rules Retrieval에 최적화되어야 한다.

---

### [핵심]

문서 품질 기준:

- Frontend Env 개념 포함
- Public Config와 Secret 구분
- Vite Env 규칙 포함
- CRA Env 규칙 포함
- Env Prefix Mismatch 포함
- `.env` 파일 종류 포함
- `.gitignore` 기준 포함
- Build-time Env와 Runtime Config 구분
- Docker Env 오해 포함
- API Base URL 환경별 분리 포함
- Env Validation 포함
- CI/CD와 Hosting Platform Env 포함
- Troubleshooting Flow 포함
- Agent별 판단 기준 포함
- Retrieval Queries 포함

---

### [실무]

Part03은 다음 문서와 연결된다.

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

Q. Part03의 핵심 목적은 무엇인가?
A. 프론트엔드 환경 변수의 prefix, 보안, build 반영, runtime config, 배포 문제를 Agent가 정확히 판단하게 하는 것이다.

Q. Part03에서 API 통신 전체를 다루는가?
A. 아니다. API Base URL의 env 분리는 다루지만 CORS, 인증, proxy 세부는 Part04 이후에서 다룬다.

Q. Part03에서 Docker 배포 전체를 다루는가?
A. 아니다. Docker env 주입 시점 오해만 다루고 Docker 배포 구조는 후속 Part에서 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. 프론트엔드 환경 변수란 무엇인가?
A. API 주소, 앱 환경, public key 같은 환경별 설정 값을 프론트엔드 코드에서 사용하기 위한 변수다.

Q. 프론트엔드 env에 Secret Key를 넣어도 되는가?
A. 안 된다. 프론트엔드 환경 변수는 브라우저에 노출될 수 있다.

Q. 프론트엔드 env에 넣어도 되는 값은 무엇인가?
A. API Base URL, APP_ENV, public map key, OAuth Client ID, public analytics ID 같은 공개 가능한 설정이다.

Q. 프론트엔드 env에 넣으면 안 되는 값은 무엇인가?
A. DB_PASSWORD, JWT_SECRET, OPENAI_API_KEY, AWS_SECRET_ACCESS_KEY, TOSS_SECRET_KEY 같은 Secret이다.

Q. Vite 환경 변수 prefix는 무엇인가?
A. `VITE_`다.

Q. CRA 환경 변수 prefix는 무엇인가?
A. `REACT_APP_`다.

Q. Vite에서 환경 변수는 어떻게 읽는가?
A. `import.meta.env.VITE_API_BASE_URL`처럼 읽는다.

Q. CRA에서 환경 변수는 어떻게 읽는가?
A. `process.env.REACT_APP_API_BASE_URL`처럼 읽는다.

Q. Vite에서 REACT*APP* 변수를 쓰면 어떻게 되는가?
A. 일반적으로 클라이언트 코드에서 값이 undefined 될 수 있다.

Q. CRA에서 VITE\_ 변수를 쓰면 어떻게 되는가?
A. 일반적으로 클라이언트 코드에서 값이 undefined 될 수 있다.

Q. API Base URL이 undefined인 이유는?
A. Build Tool에 맞지 않는 env prefix나 access 방식을 사용했을 가능성이 높다.

Q. .env 파일은 어디에 위치해야 하는가?
A. 보통 해당 프론트엔드 프로젝트의 `package.json`이 있는 루트에 있어야 한다.

Q. .env 수정 후 값이 안 바뀌는 이유는?
A. 개발 서버를 재시작하지 않았거나 운영에서는 다시 Build하지 않았기 때문이다.

Q. .env.example은 왜 필요한가?
A. 팀원이 필요한 환경 변수 목록을 알 수 있도록 공유하기 위해 필요하다.

Q. .env.local은 Git에 올려도 되는가?
A. 보통 올리지 않는다. 개인 로컬 설정이 포함될 수 있기 때문이다.

Q. .env.production에는 무엇을 넣는가?
A. 운영 API URL, 운영 앱 환경, public key 같은 운영용 공개 설정을 넣는다.

Q. .gitignore에 env 파일을 어떻게 설정하는가?
A. 실제 `.env`, `.env.local`, 환경별 local env는 제외하고 `.env.example`은 포함하는 방식이 일반적이다.

Q. 실수로 Secret을 Git에 commit했다면 어떻게 해야 하는가?
A. Secret을 폐기하고 새로 발급하며 Git history 노출 여부도 확인해야 한다.

Q. Build-time Env란 무엇인가?
A. Build 시점에 코드에 주입되어 정적 JS bundle에 포함되는 환경 변수다.

Q. React env는 배포 후 파일만 바꾸면 반영되는가?
A. 일반적으로 아니다. Build-time Env는 다시 Build해야 반영된다.

Q. Runtime Config란 무엇인가?
A. Build 후에도 외부 config 파일을 읽어 public 설정을 변경할 수 있게 하는 방식이다.

Q. Runtime Config에 Secret을 넣어도 되는가?
A. 안 된다. config 파일도 브라우저에서 접근 가능하다.

Q. Runtime Config는 언제 필요한가?
A. 동일 Build 결과물을 여러 환경에 배포하거나 Docker 이미지 하나로 여러 환경을 처리할 때 유용하다.

Q. Docker run -e로 React env를 바꾸면 반영되는가?
A. 일반 Build-time Env 방식에서는 반영되지 않을 수 있다.

Q. Docker에서 실행 시점 API URL을 바꾸려면 어떻게 하는가?
A. Runtime Config 또는 컨테이너 시작 시 config.json 생성 전략을 사용할 수 있다.

Q. API Base URL은 왜 env로 분리하는가?
A. 로컬, 개발, 스테이징, 운영 백엔드 주소가 다르기 때문이다.

Q. 운영 env에 localhost가 있으면 왜 문제인가?
A. 사용자 브라우저 기준 localhost는 배포 서버가 아니라 사용자 PC를 의미하기 때문이다.

Q. baseURL을 /api로 써도 되는가?
A. 가능하다. 같은 도메인에서 Nginx나 백엔드가 `/api` 요청을 실제 API 서버로 proxy해야 한다.

Q. API가 /api/api로 호출되는 이유는?
A. baseURL과 개별 요청 path 양쪽에 `/api`가 중복되었기 때문이다.

Q. 필수 env 검증은 왜 필요한가?
A. 환경 변수 누락으로 잘못된 API 요청이나 운영 장애가 발생하는 것을 조기에 막기 위해 필요하다.

Q. env 누락 시 localhost fallback을 둬도 되는가?
A. 운영에서는 위험하다. 필수 env는 누락 시 실패시키는 것이 좋다.

Q. env 중앙 모듈은 왜 필요한가?
A. env 접근을 한 곳에 모아 오타, undefined, Build Tool 혼동을 줄이기 위해 필요하다.

Q. TypeScript에서 env 타입을 지정하면 무엇이 좋은가?
A. 변수명 오타를 줄이고 코드 자동완성과 검토가 쉬워진다.

Q. CI/CD에서 env를 설정해야 하는 이유는?
A. Production Build 시점에 운영 API URL 같은 값이 필요하기 때문이다.

Q. GitHub Secrets에 넣으면 프론트엔드 env도 안전한가?
A. Build 결과에 포함되는 값은 브라우저에 노출될 수 있으므로 Secret을 프론트엔드에 주입하면 안 된다.

Q. Hosting Platform env를 바꾸면 즉시 반영되는가?
A. Build-time env라면 보통 재배포가 필요하다.

Q. env 변경 후 이전 API URL이 계속 호출되는 이유는?
A. 브라우저 캐시, CDN 캐시, Service Worker, index.html 캐시 문제일 수 있다.

Q. config.json 캐시는 어떻게 관리해야 하는가?
A. Runtime Config라면 `no-store` 또는 짧은 cache를 사용해야 한다.

Q. Review Agent는 env에서 무엇을 먼저 확인해야 하는가?
A. Secret 노출 여부와 Build Tool에 맞는 prefix 사용 여부를 먼저 확인해야 한다.

Q. PM Agent는 env에서 무엇을 정리해야 하는가?
A. 필요한 env 목록, 환경별 값, public/secret 구분, Build Tool prefix, 배포 설정 위치를 정리해야 한다.

Q. Frontend Agent는 env를 어떻게 구현해야 하는가?
A. Build Tool prefix를 지키고 env 중앙 모듈, 필수 값 검증, API URL 환경 분리를 적용해야 한다.

Q. Part03 다음 문서는 무엇인가?
A. Part04 API Base URL Rules로 이어지는 것이 적합하다.
