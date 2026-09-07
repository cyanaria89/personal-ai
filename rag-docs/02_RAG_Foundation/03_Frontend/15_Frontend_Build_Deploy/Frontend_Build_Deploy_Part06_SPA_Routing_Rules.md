# Frontend Build & Deploy Part06 - SPA Routing Rules

---

# 1. SPA Routing Core

## 1.1 SPA Routing Definition

### [개념]

SPA Routing은 서버가 여러 HTML 페이지를 제공하는 방식이 아니라 브라우저에서 JavaScript가 URL에 따라 화면을 전환하는 라우팅 방식이다.

React SPA에서는 보통 React Router가 브라우저 URL을 읽고 어떤 컴포넌트를 렌더링할지 결정한다.

대표 route 예:

```text
/
/login
/signup
/mypage
/festival/10
/admin/dashboard
```

---

### [핵심]

SPA Routing 핵심 규칙:

- 실제 서버 파일 경로와 프론트엔드 route는 다르다.
- `/login` 파일이 서버에 존재하지 않아도 React Router는 `/login` 화면을 렌더링할 수 있다.
- 링크 클릭 이동은 브라우저 내부 라우팅으로 처리된다.
- 새로고침 또는 직접 URL 접근은 서버가 먼저 요청을 받는다.
- 운영 서버는 프론트엔드 route 요청에 `index.html`을 반환해야 한다.
- API path와 frontend route path를 분리해야 한다.
- 정적 asset 요청은 fallback 대상이 아니어야 한다.

---

### [실무]

2026 실무 기준으로 React Router `BrowserRouter`를 사용하는 SPA는 운영 배포 시 SPA fallback 설정이 필수에 가깝다.

SPA 정상 Flow:

```text
User visits /festival/10
→ Server returns index.html
→ Browser loads JS bundle
→ React App boot
→ React Router reads /festival/10
→ FestivalDetail component render
```

SPA 실패 Flow:

```text
User refresh /festival/10
→ Server tries to find /festival/10 file
→ File not found
→ Server returns 404
```

Agent 판단 Flow:

```text
Router Type 확인
→ BrowserRouter 여부 확인
→ 배포 서버 확인
→ fallback 설정 확인
→ API path 제외 여부 확인
→ direct URL access 테스트
→ refresh 테스트
```

---

### [FAQ]

Q. SPA Routing이란 무엇인가?
A. 브라우저에서 JavaScript가 URL에 따라 화면을 전환하는 라우팅 방식이다.

Q. React Router route는 서버 파일 경로인가?
A. 아니다. React Router route는 클라이언트 화면 전환 규칙이다.

Q. 개발 서버에서는 새로고침이 되는데 운영에서 404가 나는 이유는?
A. 개발 서버는 fallback을 제공하지만 운영 서버에는 별도 fallback 설정이 없을 수 있기 때문이다.

Q. SPA Routing 배포에서 가장 중요한 설정은 무엇인가?
A. 프론트엔드 route 요청을 `index.html`로 반환하는 SPA fallback 설정이다.

---

## 1.2 BrowserRouter vs HashRouter

### [개념]

BrowserRouter는 HTML5 History API를 사용해 일반 URL 경로를 사용하고, HashRouter는 URL의 `#` 이후 경로를 사용해 라우팅한다.

예:

```text
BrowserRouter
→ https://example.com/festival/10

HashRouter
→ https://example.com/#/festival/10
```

---

### [핵심]

BrowserRouter 특징:

- 깔끔한 URL
- 실무에서 일반적으로 선호
- 운영 서버 fallback 필요
- 직접 URL 접근과 새로고침 대응 필요

HashRouter 특징:

- 서버 fallback 없이도 동작하기 쉬움
- URL에 `#`가 포함됨
- GitHub Pages 같은 rewrite 제한 환경에서 단순
- SEO / URL 가독성 측면에서 덜 선호될 수 있음

---

### [실무]

2026 실무 기준으로 일반 운영 서비스는 BrowserRouter + 서버 fallback을 우선 고려한다.

GitHub Pages나 rewrite 제약이 강한 정적 호스팅에서는 HashRouter가 빠른 우회책이 될 수 있다.

BrowserRouter 예:

```jsx
import { BrowserRouter } from "react-router-dom";

function Root() {
  return (
    <BrowserRouter>
      <App />
    </BrowserRouter>
  );
}
```

HashRouter 예:

```jsx
import { HashRouter } from "react-router-dom";

function Root() {
  return (
    <HashRouter>
      <App />
    </HashRouter>
  );
}
```

선택 기준:

```text
Nginx / Spring Boot / Vercel / Netlify fallback 가능
→ BrowserRouter 권장

GitHub Pages / fallback 제약 / 빠른 데모
→ HashRouter 고려
```

---

### [FAQ]

Q. BrowserRouter는 무엇인가?
A. HTML5 History API를 사용해 `/login`, `/mypage` 같은 일반 URL을 사용하는 라우터다.

Q. HashRouter는 무엇인가?
A. URL의 `#` 이후 경로를 사용해 서버 fallback 없이 라우팅하기 쉬운 방식이다.

Q. BrowserRouter에서 새로고침 404가 나는 이유는?
A. 서버가 React route를 실제 파일 경로로 찾기 때문이다.

Q. HashRouter를 쓰면 새로고침 404가 해결되는가?
A. 대부분 해결될 수 있지만 URL에 `#`가 붙는다.

---

# 2. Refresh 404

## 2.1 Refresh 404 Definition

### [개념]

Refresh 404는 React SPA에서 링크 이동은 정상인데 새로고침하거나 직접 URL로 접근할 때 서버가 404를 반환하는 문제다.

대표 상황:

```text
Click Link /mypage
→ 정상 표시

Refresh /mypage
→ 404 Not Found
```

---

### [핵심]

Refresh 404 원인:

- BrowserRouter 사용
- 서버에 `/mypage` 실제 파일 없음
- 운영 서버 fallback 설정 없음
- Nginx `try_files` 누락
- Spring Boot fallback 누락
- Vercel rewrite 누락
- Netlify redirect 누락
- S3 / CloudFront error response 누락
- GitHub Pages rewrite 제약
- Sub Path Hosting fallback 경로 오류

---

### [실무]

2026 실무 기준으로 Refresh 404는 React 코드 문제가 아니라 Hosting Server routing 설정 문제인 경우가 대부분이다.

판단 Flow:

```text
메인 페이지 접속 확인
→ 내부 링크 이동 확인
→ 이동한 route에서 새로고침
→ 404 발생 여부 확인
→ hosting server 확인
→ fallback 설정 추가
→ API path 제외 확인
```

해결 원칙:

```text
Frontend Route Request
→ index.html 반환

API Request
→ Backend API 반환

Static Asset Request
→ 실제 asset 반환
```

---

### [FAQ]

Q. Refresh 404란 무엇인가?
A. SPA route에서 새로고침하거나 직접 URL 접근 시 서버가 404를 반환하는 문제다.

Q. 클릭 이동은 되는데 새로고침하면 404가 나는 이유는?
A. 클릭 이동은 React Router가 처리하지만 새로고침은 서버가 먼저 URL을 처리하기 때문이다.

Q. Refresh 404는 React 코드 문제인가?
A. 대부분 서버 fallback 설정 문제다.

Q. Refresh 404를 해결하는 핵심은 무엇인가?
A. 프론트엔드 route 요청에 대해 서버가 `index.html`을 반환하도록 설정하는 것이다.

---

## 2.2 Direct URL Access

### [개념]

Direct URL Access는 사용자가 브라우저 주소창에 `/login`, `/detail/1` 같은 SPA route를 직접 입력해 접속하는 상황이다.

---

### [핵심]

Direct URL Access 문제 조건:

```text
Browser requests /detail/1 directly
→ Server handles request first
→ Server searches /detail/1 file
→ Not found
→ 404
```

정상 조건:

```text
Browser requests /detail/1 directly
→ Server returns index.html
→ React Router renders DetailPage
```

확인 대상:

- 배포 서버 fallback
- route basename
- build base path
- sub path hosting
- auth protected route
- API path 충돌

---

### [실무]

검증해야 할 직접 접근 URL:

```text
/login
/signup
/mypage
/detail/1
/search?keyword=test
/admin
```

검증 Flow:

```text
Production URL 열기
→ route 직접 입력
→ HTTP status 확인
→ index.html 반환 여부 확인
→ React 화면 렌더링 확인
→ Console Error 확인
```

주의:

```text
직접 URL 접근 성공
≠
인증 권한 성공
```

Protected Route는 로그인 여부에 따라 redirect될 수 있다.

---

### [FAQ]

Q. Direct URL Access란 무엇인가?
A. 사용자가 주소창에 SPA route를 직접 입력해 접속하는 상황이다.

Q. 직접 URL 접근에서 404가 나면 무엇을 확인해야 하는가?
A. 서버 SPA fallback 설정과 base path, basename을 확인해야 한다.

Q. 인증이 필요한 route에서 로그인 페이지로 이동하는 것은 404인가?
A. 아니다. Protected Route 로직에 따른 정상 redirect일 수 있다.

Q. 직접 URL 접근 검증은 왜 필요한가?
A. 사용자가 링크 공유, 새로고침, 북마크 접근을 할 수 있기 때문이다.

---

# 3. SPA Fallback Rules

## 3.1 SPA Fallback Definition

### [개념]

SPA Fallback은 서버가 프론트엔드 route 요청에 대해 실제 파일을 찾지 못했을 때 404 대신 `index.html`을 반환하는 설정이다.

---

### [핵심]

Fallback 적용 대상:

```text
/login
/mypage
/festival/10
/search
/admin/dashboard
```

Fallback 제외 대상:

```text
/api/**
/assets/**
/static/**
/favicon.ico
/manifest.json
/robots.txt
/sitemap.xml
```

Fallback 원칙:

- 프론트엔드 route는 `index.html` 반환
- API 요청은 백엔드 API 반환
- 정적 파일 요청은 실제 파일 반환
- 존재하지 않는 asset을 무조건 index.html로 보내면 안 됨
- 서버별 fallback 문법이 다름

---

### [실무]

정상 fallback Flow:

```text
Request /festival/10
→ file not found
→ return index.html
→ React Router render /festival/10
```

비정상 fallback Flow:

```text
Request /api/festivals
→ return index.html
→ frontend expects JSON
→ Unexpected token '<'
```

Agent 검토 기준:

```text
fallback 설정 있음
→ API path 제외 여부 확인
→ asset path 제외 여부 확인
→ direct route refresh 확인
→ API response Content-Type 확인
```

---

### [FAQ]

Q. SPA Fallback이란 무엇인가?
A. 프론트엔드 route 요청에 대해 서버가 `index.html`을 반환하도록 하는 설정이다.

Q. SPA Fallback은 모든 요청에 적용해도 되는가?
A. 아니다. API와 정적 asset 요청은 제외해야 한다.

Q. API 요청에 index.html이 오면 무엇이 문제인가?
A. fallback이 API 요청까지 처리하고 있는 것이다.

Q. 존재하지 않는 JS 파일도 index.html로 보내도 되는가?
A. 안 된다. MIME type error와 흰 화면을 유발할 수 있다.

---

## 3.2 Fallback Priority

### [개념]

Fallback Priority는 서버가 요청을 처리할 때 API, 정적 파일, 프론트엔드 route의 우선순위를 정하는 규칙이다.

---

### [핵심]

권장 우선순위:

```text
1. API Route
2. Static Asset
3. Existing File
4. SPA Route Fallback to index.html
```

잘못된 우선순위:

```text
1. SPA Fallback
2. API Route
3. Static Asset
```

문제 결과:

- API가 index.html 반환
- JS / CSS가 index.html 반환
- MIME type error
- JSON parse error
- 404 원인 파악 어려움

---

### [실무]

Nginx 우선순위 예:

```nginx
location /api/ {
  proxy_pass http://backend:8080/api/;
}

location /assets/ {
  try_files $uri =404;
}

location / {
  try_files $uri $uri/ /index.html;
}
```

Spring Boot 우선순위:

```text
Controller /api/**
→ Static Resource
→ SPA fallback
```

검증 Flow:

```text
API 요청 테스트
→ asset 요청 테스트
→ frontend route 직접 접근 테스트
→ fallback 응답 확인
```

---

### [FAQ]

Q. Fallback Priority는 왜 중요한가?
A. API와 asset 요청이 fallback에 잡히지 않도록 하기 위해 중요하다.

Q. API Route와 SPA Fallback 중 무엇이 우선인가?
A. API Route가 우선이어야 한다.

Q. Static Asset과 SPA Fallback 중 무엇이 우선인가?
A. Static Asset이 우선이어야 한다.

Q. 우선순위가 틀리면 어떤 문제가 생기는가?
A. API나 JS 파일 요청에 index.html이 반환될 수 있다.

---

# 4. Server-specific Fallback Rules

## 4.1 Nginx SPA Fallback

### [개념]

Nginx SPA Fallback은 React route 요청에 대해 `try_files`를 사용해 `index.html`을 반환하는 설정이다.

---

### [핵심]

핵심 설정:

```nginx
try_files $uri $uri/ /index.html;
```

의미:

```text
요청한 파일이 있으면 반환
→ 디렉토리가 있으면 반환
→ 없으면 index.html 반환
```

주의:

- `/api/` location은 별도로 분리한다.
- `/assets/`는 실제 파일 우선 제공한다.
- fallback은 프론트엔드 route에만 적용한다.
- sub path hosting은 fallback 경로가 달라질 수 있다.

---

### [실무]

기본 Nginx 설정:

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

검증 Flow:

```text
Nginx config 확인
→ nginx -t
→ reload
→ / 접속
→ /login 직접 접근
→ /api/health 확인
→ /assets/*.js 확인
```

---

### [FAQ]

Q. Nginx에서 React 새로고침 404는 어떻게 해결하는가?
A. `location /`에 `try_files $uri $uri/ /index.html;`을 설정한다.

Q. Nginx에서 /api 요청이 index.html로 가면 어떻게 해야 하는가?
A. `/api/` location을 별도로 분리해 백엔드로 proxy해야 한다.

Q. try_files $uri가 왜 필요한가?
A. 실제 JS, CSS, 이미지 파일을 우선 제공하기 위해 필요하다.

Q. Nginx 설정 변경 후 무엇을 해야 하는가?
A. `nginx -t`로 문법 확인 후 reload해야 한다.

---

## 4.2 Spring Boot SPA Fallback

### [개념]

Spring Boot SPA Fallback은 React build 파일을 Spring Boot static resource로 제공할 때 프론트엔드 route 요청을 `index.html`로 forward하는 설정이다.

---

### [핵심]

Spring Boot fallback 기준:

- React build output은 static root에 위치
- API 경로는 fallback 대상 제외
- 정적 asset 경로는 fallback 대상 제외
- frontend route만 `index.html`로 forward
- Security 설정에서 static resource 접근 허용 필요 가능

---

### [실무]

Fallback Controller 예:

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

주의:

```text
위 mapping은 점(.)이 없는 경로를 index.html로 forward한다.
API 경로가 유사하게 잡히지 않는지 반드시 확인해야 한다.
```

권장 API 분리:

```text
/api/**
/auth/**
/admin/**
```

더 안전한 구조:

```text
Backend API는 /api prefix 사용
SPA fallback은 /api 제외
```

검증 Flow:

```text
Spring Boot 실행
→ / 접속
→ /login 직접 접근
→ /api/health 호출
→ API 응답이 JSON인지 확인
→ asset 404 확인
```

---

### [FAQ]

Q. Spring Boot 통합 배포에서도 SPA fallback이 필요한가?
A. React Router BrowserRouter를 사용하면 필요할 수 있다.

Q. Spring Boot fallback 때문에 API가 안 불릴 수 있는가?
A. 가능하다. fallback mapping이 API 경로를 잡으면 API 대신 index.html이 반환될 수 있다.

Q. Spring Boot에서 API path는 어떻게 분리하는 것이 좋은가?
A. `/api` prefix를 사용하는 것이 SPA route와 충돌을 줄이는 데 안전하다.

Q. Spring Boot fallback에서 점이 없는 경로만 잡는 이유는?
A. JS, CSS, 이미지 같은 정적 파일 경로에는 확장자 점이 있으므로 asset 요청을 피하기 위한 패턴이다.

---

## 4.3 Netlify SPA Redirect

### [개념]

Netlify SPA Redirect는 Netlify에서 직접 URL 접근과 새로고침 시 `index.html`을 반환하도록 설정하는 redirect 규칙이다.

---

### [핵심]

Netlify 설정 방식:

```text
public/_redirects
netlify.toml
```

기본 규칙:

```text
/* /index.html 200
```

주의:

- API proxy rewrite가 있다면 fallback보다 우선 고려한다.
- `_redirects` 파일이 build output에 포함되어야 한다.
- Vite/CRA public 폴더 위치를 확인한다.
- function path나 API path를 fallback으로 덮지 않게 주의한다.

---

### [실무]

`public/_redirects` 예:

```text
/* /index.html 200
```

`netlify.toml` 예:

```toml
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

검증 Flow:

```text
Build output 확인
→ _redirects 포함 확인
→ Netlify deploy
→ /login 직접 접근
→ 새로고침 확인
→ API path 확인
```

---

### [FAQ]

Q. Netlify에서 React 새로고침 404는 어떻게 해결하는가?
A. `_redirects`에 `/* /index.html 200`을 추가하거나 `netlify.toml` redirect를 설정한다.

Q. \_redirects 파일은 어디에 둬야 하는가?
A. Build output에 포함되도록 보통 public 폴더에 둔다.

Q. Netlify redirect가 API 요청까지 잡을 수 있는가?
A. 설정에 따라 가능하므로 API rewrite와 fallback 우선순위를 확인해야 한다.

Q. Netlify에서 직접 URL 접근 검증은 어떻게 하는가?
A. 배포 URL에서 `/login`, `/detail/1` 같은 route를 직접 입력해 확인한다.

---

## 4.4 Vercel SPA Rewrite

### [개념]

Vercel SPA Rewrite는 Vercel에서 React SPA route 요청을 `index.html`로 rewrite하여 BrowserRouter 새로고침 404를 방지하는 설정이다.

---

### [핵심]

설정 파일:

```text
vercel.json
```

기본 rewrite:

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

주의:

- API route가 있다면 rewrite와 충돌하지 않아야 한다.
- Vercel framework preset에 따라 자동 처리될 수 있다.
- output directory가 맞아야 한다.
- 하위 경로 배포 시 base path를 함께 확인한다.

---

### [실무]

Vercel 검증 항목:

```md
- [ ] Build Command가 맞는가?
- [ ] Output Directory가 맞는가?
- [ ] vercel.json rewrite가 필요한가?
- [ ] 직접 URL 접근이 되는가?
- [ ] API 요청이 index.html로 rewrite되지 않는가?
- [ ] env 값이 production 기준인가?
```

검증 Flow:

```text
Vercel deploy
→ / 접속
→ /login 직접 접근
→ /detail/1 새로고침
→ Network 확인
→ API request 확인
```

---

### [FAQ]

Q. Vercel에서 React SPA 새로고침 404는 어떻게 해결하는가?
A. 필요한 경우 `vercel.json` rewrites로 모든 frontend route를 `index.html`로 보낸다.

Q. Vercel은 SPA fallback을 자동으로 처리하는가?
A. framework preset과 설정에 따라 다를 수 있으므로 직접 URL 접근을 테스트해야 한다.

Q. Vercel rewrite가 API 요청까지 잡으면 어떻게 되는가?
A. API 요청에 index.html이 반환될 수 있으므로 API path를 분리해야 한다.

Q. Vercel 배포 후 무엇을 확인해야 하는가?
A. 직접 URL 접근, 새로고침, API 요청, Console Error를 확인해야 한다.

---

## 4.5 S3 CloudFront SPA Fallback

### [개념]

S3 CloudFront SPA Fallback은 S3와 CloudFront에서 없는 route 요청에 대해 `index.html`을 반환하도록 설정하는 방식이다.

---

### [핵심]

필요 설정:

- S3 static hosting 또는 CloudFront origin 설정
- Default root object: `index.html`
- Custom error response
- 403 또는 404 → `/index.html` → 200
- Cache policy 주의
- CloudFront invalidation 필요 가능

---

### [실무]

CloudFront Custom Error Response 예:

```text
HTTP Error Code: 403
Response Page Path: /index.html
HTTP Response Code: 200
```

또는:

```text
HTTP Error Code: 404
Response Page Path: /index.html
HTTP Response Code: 200
```

검증 Flow:

```text
S3 upload
→ CloudFront distribution 확인
→ Default root object 확인
→ Custom error response 확인
→ /login 직접 접근
→ /assets/*.js 확인
→ invalidation 필요 여부 확인
```

---

### [FAQ]

Q. S3에 React를 올렸는데 새로고침 404가 나는 이유는?
A. SPA fallback을 위한 error response 설정이 없기 때문이다.

Q. CloudFront에서 SPA fallback은 어떻게 설정하는가?
A. 403 또는 404 error response를 `/index.html`로 보내고 응답 코드를 200으로 설정한다.

Q. S3/CloudFront에서 index.html 캐시는 왜 주의해야 하는가?
A. 이전 index.html이 오래 캐시되면 새 배포 asset과 mismatch가 날 수 있다.

Q. S3/CloudFront에서 직접 URL 접근은 꼭 테스트해야 하는가?
A. 해야 한다. fallback 설정이 없으면 route 직접 접근이 실패할 수 있다.

---

## 4.6 GitHub Pages Routing

### [개념]

GitHub Pages Routing은 GitHub Pages의 정적 호스팅 제약 안에서 React Router를 사용하는 방식이다.

---

### [핵심]

GitHub Pages 특징:

- 보통 repository name 하위 경로 배포
- 서버 rewrite 설정 제한
- BrowserRouter 직접 URL 접근에 제약
- HashRouter 사용이 단순할 수 있음
- base path 설정 필요
- 404.html fallback 우회가 가능하지만 복잡도 증가

---

### [실무]

배포 URL 예:

```text
https://username.github.io/repository-name/
```

Vite base 예:

```js
export default defineConfig({
  base: "/repository-name/",
});
```

React Router basename 예:

```jsx
<BrowserRouter basename="/repository-name">
  <App />
</BrowserRouter>
```

간단 우회:

```text
HashRouter 사용
→ https://username.github.io/repository-name/#/login
```

Agent 판단 기준:

```text
GitHub Pages 사용
→ sub path 확인
→ base/homepage 확인
→ BrowserRouter fallback 제약 확인
→ HashRouter 고려
```

---

### [FAQ]

Q. GitHub Pages에서 React Router 새로고침이 안 되는 이유는?
A. GitHub Pages는 서버 rewrite 설정이 제한적이기 때문이다.

Q. GitHub Pages에서 가장 쉬운 라우팅 해결책은 무엇인가?
A. HashRouter를 사용하는 것이 가장 단순한 해결책일 수 있다.

Q. BrowserRouter를 GitHub Pages에서 쓰려면 무엇을 확인해야 하는가?
A. base path, basename, 404 fallback 우회 설정을 확인해야 한다.

Q. GitHub Pages 배포 URL이 하위 경로인 이유는?
A. 보통 repository name이 path에 포함되기 때문이다.

---

# 5. Router Basename Rules

## 5.1 Router Basename Definition

### [개념]

Router Basename은 React 앱이 도메인 루트(`/`)가 아닌 하위 경로에서 동작할 때 사용하는 라우터 기준 경로다.

예:

```text
App URL: https://example.com/my-app/
basename: /my-app
```

---

### [핵심]

Basename이 필요한 상황:

- Sub Path Hosting
- GitHub Pages
- Spring Boot context path
- Nginx 하위 location 배포
- 여러 앱을 하나의 도메인 하위 경로에 배포
- CDN 하위 path 배포

Basename 불일치 증상:

- 링크 클릭 시 잘못된 경로 이동
- 새로고침 404
- route match 실패
- 메인 화면만 보임
- asset path와 router path 혼동

---

### [실무]

React Router 예:

```jsx
import { BrowserRouter } from "react-router-dom";

function Root() {
  return (
    <BrowserRouter basename="/my-app">
      <App />
    </BrowserRouter>
  );
}
```

함께 확인할 것:

```text
Vite base
CRA homepage
React Router basename
Server location
SPA fallback path
```

검증 Flow:

```text
배포 URL 확인
→ root 배포인지 sub path 배포인지 확인
→ basename 설정 확인
→ 링크 이동 확인
→ 직접 URL 접근 확인
→ 새로고침 확인
```

---

### [FAQ]

Q. Router basename이란 무엇인가?
A. React 앱이 하위 경로에서 동작할 때 사용하는 라우터 기준 경로다.

Q. 루트 도메인에 배포하면 basename이 필요한가?
A. 대부분 필요 없다.

Q. 하위 경로 배포에서 basename이 없으면 어떤 문제가 생기는가?
A. 링크 이동, 직접 URL 접근, route matching이 깨질 수 있다.

Q. basename과 Vite base는 같은가?
A. 아니다. basename은 라우팅 기준이고 Vite base는 asset 경로 기준이다.

---

## 5.2 Base Path and Basename Alignment

### [개념]

Base Path and Basename Alignment는 Build Tool의 asset base path와 React Router의 route basename을 배포 경로에 맞춰 일치시키는 규칙이다.

---

### [핵심]

구분:

```text
Vite base
→ JS/CSS asset을 어디서 로드할지 결정

CRA homepage
→ CRA asset 경로 기준 결정

React Router basename
→ route path 기준 결정

Server location
→ 요청 URL을 어떤 파일/앱으로 매핑할지 결정
```

하위 경로 배포에서는 모두 같은 기준을 공유해야 한다.

---

### [실무]

예시:

```text
Deploy URL:
https://example.com/admin-app/
```

Vite:

```js
export default defineConfig({
  base: "/admin-app/",
});
```

React Router:

```jsx
<BrowserRouter basename="/admin-app">
  <App />
</BrowserRouter>
```

Nginx:

```nginx
location /admin-app/ {
  alias /usr/share/nginx/html/;
  try_files $uri $uri/ /admin-app/index.html;
}
```

Agent 검토 기준:

```text
배포 path
→ base/homepage
→ basename
→ server location
→ fallback path
→ Network asset path
```

---

### [FAQ]

Q. Vite base와 Router basename을 둘 다 설정해야 하는가?
A. 하위 경로 배포라면 둘 다 필요할 수 있다. 하나는 asset 경로, 하나는 route 경로를 담당한다.

Q. base는 맞는데 route가 깨지는 이유는?
A. Router basename이 누락되었을 수 있다.

Q. basename은 맞는데 JS가 404인 이유는?
A. Build Tool base path나 hosting root가 잘못되었을 수 있다.

Q. 하위 경로 배포 문제는 어디서 확인하는가?
A. Network asset path와 React route path를 함께 확인해야 한다.

---

# 6. API Path Collision

## 6.1 API Path Collision Definition

### [개념]

API Path Collision은 프론트엔드 route와 백엔드 API route가 같은 경로를 사용해 서버 fallback 또는 Controller routing이 충돌하는 문제다.

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

충돌 증상:

- API 요청에 index.html 반환
- 프론트엔드 route 대신 API JSON 반환
- 새로고침 시 404
- Security filter가 route를 API로 오인
- Nginx location 충돌
- Review 난이도 증가

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

Frontend route 예:

```text
/login
/mypage
/festival/detail/1
/reviews/write
/notifications
```

Agent 검토 Flow:

```text
Frontend route 목록 확인
→ Backend API path 목록 확인
→ prefix 충돌 확인
→ /api 분리 여부 확인
→ fallback 제외 여부 확인
```

---

### [FAQ]

Q. API Path Collision이란 무엇인가?
A. 프론트엔드 route와 백엔드 API route가 같은 경로를 사용해 충돌하는 문제다.

Q. API path는 어떻게 분리하는 것이 좋은가?
A. `/api` prefix를 사용하는 것이 안전하다.

Q. 프론트엔드 route와 API route가 같으면 안 되는가?
A. 권장하지 않는다. fallback, proxy, security 설정에서 충돌 가능성이 커진다.

Q. API Path Collision의 대표 증상은 무엇인가?
A. API 요청에 index.html이 오거나 route 새로고침이 실패하는 것이다.

---

## 6.2 Fallback Exclusion for API

### [개념]

Fallback Exclusion for API는 SPA fallback 설정에서 `/api/**` 같은 백엔드 API 경로를 제외하는 규칙이다.

---

### [핵심]

제외해야 할 경로:

```text
/api/**
/auth/**
/oauth2/**
/login/oauth2/**
/ws/**
/actuator/**
```

단, 프로젝트 API prefix 정책에 따라 달라질 수 있다.

원칙:

- API는 백엔드 Controller 또는 proxy로 이동
- frontend route만 index.html 반환
- WebSocket path도 fallback 대상 아님
- health check path도 fallback 대상 아님

---

### [실무]

Nginx 분리 예:

```nginx
location /api/ {
  proxy_pass http://backend:8080/api/;
}

location /ws/ {
  proxy_pass http://backend:8080/ws/;
  proxy_http_version 1.1;
  proxy_set_header Upgrade $http_upgrade;
  proxy_set_header Connection "upgrade";
}

location / {
  try_files $uri $uri/ /index.html;
}
```

검증 Flow:

```text
GET /api/health
→ JSON 또는 정상 API 응답

GET /login
→ index.html + React login page

GET /assets/index.js
→ JavaScript file
```

---

### [FAQ]

Q. API path를 fallback에서 제외해야 하는 이유는?
A. API 요청에 index.html이 반환되는 문제를 막기 위해 필요하다.

Q. WebSocket path도 fallback에서 제외해야 하는가?
A. 그렇다. `/ws` 같은 실시간 연결 경로는 별도 proxy 또는 backend handler가 처리해야 한다.

Q. API 요청에 HTML이 오면 무엇을 확인해야 하는가?
A. fallback exclusion과 proxy location 설정을 확인해야 한다.

Q. fallback 제외 경로는 모든 프로젝트가 같은가?
A. 아니다. 프로젝트의 API prefix와 인증 path에 맞게 정해야 한다.

---

# 7. Protected Route and Deploy

## 7.1 Protected Route Definition

### [개념]

Protected Route는 로그인 여부나 권한에 따라 접근을 허용하거나 다른 페이지로 redirect하는 프론트엔드 route다.

예:

```text
/mypage
/admin
/orders
/settings
```

---

### [핵심]

Protected Route 특징:

- React Router 내부에서 인증 상태를 검사한다.
- 로그인하지 않으면 `/login`으로 redirect할 수 있다.
- 권한이 부족하면 `/403` 또는 메인으로 이동할 수 있다.
- 새로고침 시 인증 상태 복원 로직이 필요하다.
- 배포 문제와 인증 redirect 문제를 구분해야 한다.

---

### [실무]

Protected Route 예:

```jsx
function ProtectedRoute({ isAuthenticated, children }) {
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return children;
}
```

새로고침 시 주의:

```text
User refresh /mypage
→ Server returns index.html
→ React App boot
→ Auth state restore
→ token check
→ render mypage or redirect login
```

검증 기준:

```md
- [ ] 직접 URL 접근 시 404가 아닌가?
- [ ] 인증 전 redirect가 정상인가?
- [ ] 인증 후 원래 페이지 접근이 가능한가?
- [ ] 새로고침 시 token 복원이 되는가?
- [ ] 401 API 응답 처리와 route redirect가 연결되어 있는가?
```

---

### [FAQ]

Q. Protected Route란 무엇인가?
A. 로그인 여부나 권한에 따라 접근을 제어하는 프론트엔드 route다.

Q. /mypage 직접 접근 시 login으로 이동하면 배포 오류인가?
A. 로그인하지 않은 상태라면 정상 Protected Route 동작일 수 있다.

Q. Protected Route와 Refresh 404는 어떻게 구분하는가?
A. Refresh 404는 서버 404이고 Protected Route redirect는 React App이 로드된 뒤 발생한다.

Q. 새로고침 시 로그인 상태가 풀리는 이유는?
A. 인증 상태 복원 로직이나 token 저장 / refresh flow를 확인해야 한다.

---

## 7.2 Role-based Route

### [개념]

Role-based Route는 사용자 권한에 따라 접근 가능한 화면을 제한하는 프론트엔드 라우팅 방식이다.

예:

```text
ROLE_USER
ROLE_ADMIN
ROLE_MANAGER
```

---

### [핵심]

Role-based Route 기준:

- 프론트엔드 권한 체크는 UX 보조 수단이다.
- 실제 보안은 백엔드 Authorization에서 보장해야 한다.
- 배포 후 route 접근과 API 권한을 모두 검증해야 한다.
- 관리자 route는 직접 URL 접근도 확인해야 한다.
- 권한 부족 시 redirect 또는 403 화면이 필요하다.

---

### [실무]

권한 route 예:

```jsx
function AdminRoute({ user, children }) {
  if (!user?.roles?.includes("ROLE_ADMIN")) {
    return <Navigate to="/403" replace />;
  }

  return children;
}
```

검증 Flow:

```text
ROLE_USER로 /admin 접근
→ frontend redirect 확인
→ admin API 호출 차단 확인

ROLE_ADMIN으로 /admin 접근
→ route render 확인
→ admin API 정상 확인
```

주의:

```text
Frontend Route Guard
≠
Backend Security
```

---

### [FAQ]

Q. Role-based Route는 보안 기능인가?
A. UX 차원의 접근 제어일 뿐이며 실제 보안은 백엔드에서 보장해야 한다.

Q. 관리자 페이지 route만 숨기면 안전한가?
A. 아니다. 사용자가 직접 URL을 입력할 수 있으므로 백엔드 API 권한 검증이 필수다.

Q. 권한 부족 시 어떤 처리가 필요한가?
A. `/403` 페이지 또는 로그인 페이지로 redirect하는 처리가 필요하다.

Q. 배포 후 관리자 route는 어떻게 검증하는가?
A. 일반 사용자와 관리자 계정으로 직접 URL 접근과 API 응답을 모두 확인한다.

---

# 8. Routing Troubleshooting

## 8.1 Route Shows Blank Page

### [개념]

Route Shows Blank Page는 특정 SPA route에 접근했을 때 화면이 흰색으로 표시되는 문제다.

---

### [핵심]

대표 원인:

- JS runtime error
- lazy loaded chunk 404
- route component import error
- Router basename 오류
- route path mismatch
- env undefined
- API 초기화 실패
- Suspense fallback 누락
- Error Boundary 없음

---

### [실무]

Troubleshooting Flow:

```text
Console Error 확인
→ Network chunk 404 확인
→ route component import 확인
→ basename 확인
→ route path 확인
→ API 초기화 에러 확인
→ Error Boundary 확인
```

Lazy route 예:

```jsx
const DetailPage = lazy(() => import("./pages/DetailPage"));

<Suspense fallback={<div>Loading...</div>}>
  <DetailPage />
</Suspense>;
```

검토 기준:

```md
- [ ] lazy component 경로가 맞는가?
- [ ] chunk 파일이 200으로 로드되는가?
- [ ] Suspense fallback이 있는가?
- [ ] Console runtime error가 없는가?
```

---

### [FAQ]

Q. 특정 route에서만 흰 화면이 나오는 이유는?
A. 해당 route component의 runtime error, lazy chunk 404, route path mismatch가 원인일 수 있다.

Q. lazy loading route에서 chunk 404가 나면 무엇을 확인해야 하는가?
A. build output, asset base path, cache mismatch, 배포 누락을 확인해야 한다.

Q. Suspense fallback은 왜 필요한가?
A. lazy loaded component가 로드되는 동안 표시할 UI를 제공하기 위해 필요하다.

Q. Route blank page는 fallback 문제와 같은가?
A. 다를 수 있다. fallback은 서버 routing 문제이고 blank page는 클라이언트 runtime 문제일 수 있다.

---

## 8.2 Route Redirect Loop

### [개념]

Route Redirect Loop는 인증 또는 권한 판단 로직이 반복 redirect를 발생시켜 사용자가 화면에 진입하지 못하는 문제다.

---

### [핵심]

대표 원인:

- 인증 상태 초기값 문제
- token 복원 전 redirect 실행
- `/login`에서도 Protected Route 적용
- 권한 체크 조건 오류
- refresh token API 실패 반복
- 401 interceptor와 route guard 충돌
- redirect target이 다시 guard 대상

---

### [실무]

Troubleshooting Flow:

```text
현재 URL 확인
→ redirect target 확인
→ auth loading 상태 확인
→ token restore 순서 확인
→ route guard 조건 확인
→ 401 interceptor 동작 확인
→ Console/Network 반복 요청 확인
```

안전 패턴:

```jsx
if (authLoading) {
  return <div>Loading...</div>;
}

if (!isAuthenticated) {
  return <Navigate to="/login" replace />;
}
```

검토 기준:

```md
- [ ] auth loading 상태가 있는가?
- [ ] login route는 protected에서 제외되는가?
- [ ] redirect target이 다시 redirect를 유발하지 않는가?
- [ ] 401 interceptor와 route guard가 충돌하지 않는가?
```

---

### [FAQ]

Q. Redirect Loop란 무엇인가?
A. route guard나 인증 로직이 반복 redirect를 발생시켜 페이지에 진입하지 못하는 문제다.

Q. 로그인 페이지로 계속 튕기는 이유는?
A. 인증 상태 복원 전 redirect하거나 token 판단 로직이 잘못되었을 수 있다.

Q. authLoading 상태는 왜 필요한가?
A. token 복원이나 사용자 정보 조회가 끝나기 전 잘못된 redirect를 막기 위해 필요하다.

Q. 401 interceptor가 redirect loop를 만들 수 있는가?
A. 가능하다. route guard와 동시에 redirect하면 반복 이동이 발생할 수 있다.

---

## 8.3 Route Not Found Page

### [개념]

Route Not Found Page는 React Router 내부에서 정의되지 않은 route에 대해 보여주는 404 화면이다.

서버 404와 구분해야 한다.

---

### [핵심]

구분:

```text
Server 404
→ index.html 자체를 받지 못함
→ SPA fallback 문제

React Not Found Page
→ index.html과 JS는 로드됨
→ React Router가 fallback route 렌더링
```

React Router 예:

```jsx
<Route path="*" element={<NotFoundPage />} />
```

---

### [실무]

검증 Flow:

```text
Network에서 index.html 200 확인
→ JS bundle 200 확인
→ React NotFoundPage 표시 확인
→ 서버 404와 구분
```

권장:

```text
알 수 없는 frontend route
→ React NotFoundPage

알 수 없는 API route
→ Backend 404 JSON

알 수 없는 asset
→ Static 404
```

---

### [FAQ]

Q. React Not Found Page와 서버 404는 같은가?
A. 아니다. React Not Found는 앱 내부 화면이고 서버 404는 index.html을 받지 못한 상태다.

Q. path="\*" route는 왜 필요한가?
A. 정의되지 않은 프론트엔드 route에 대해 사용자 친화적인 404 화면을 제공하기 위해 필요하다.

Q. API 404도 React Not Found로 처리해야 하는가?
A. 아니다. API 404는 백엔드 JSON 응답으로 처리되어야 한다.

Q. 서버 404인지 React 404인지 어떻게 구분하는가?
A. Network에서 index.html과 JS가 로드되었는지 확인한다.

---

# 9. Agent Decision Rules

## 9.1 PM Agent Rules

### [개념]

PM Agent는 SPA Routing 배포 전략, Router 종류, Hosting fallback, API route 분리, 검증 범위를 정리해야 한다.

---

### [핵심]

PM Agent 확인 항목:

- Router Type
- BrowserRouter / HashRouter
- Hosting Platform
- SPA Fallback 지원 여부
- Sub Path Hosting 여부
- Router Basename 필요 여부
- API Prefix
- WebSocket Path
- Protected Route 범위
- 직접 URL 접근 테스트 범위
- 새로고침 테스트 범위

---

### [실무]

PM Agent 산출물 예:

```text
Router: BrowserRouter
Hosting: Nginx
SPA Fallback: try_files $uri $uri/ /index.html
API Prefix: /api
WebSocket Path: /ws
Sub Path: none
Protected Routes: /mypage, /admin
Verification:
- /login direct access
- /festival/10 refresh
- /api/health JSON response
- /assets/*.js 200
```

PM Agent 판단 Flow:

```text
Router 확인
→ Hosting 확인
→ fallback 방식 결정
→ API/WebSocket path 분리
→ sub path 여부 확인
→ route 검증 시나리오 작성
```

---

### [FAQ]

Q. PM Agent는 SPA Routing에서 무엇을 정리해야 하는가?
A. Router 종류, fallback 방식, API prefix, sub path, 검증 route 목록을 정리해야 한다.

Q. PM Agent가 BrowserRouter와 HashRouter 선택도 판단해야 하는가?
A. 그렇다. Hosting fallback 지원 여부에 따라 선택이 달라질 수 있다.

Q. PM Agent가 직접 URL 테스트 목록을 만들어야 하는가?
A. 그렇다. 배포 후 route 장애를 빠르게 검증하기 위해 필요하다.

---

## 9.2 Frontend Agent Rules

### [개념]

Frontend Agent는 React Router 설정, route 구조, basename, protected route, not found route를 배포 구조에 맞게 구현해야 한다.

---

### [핵심]

Frontend Agent 필수 기준:

- BrowserRouter / HashRouter 선택 기준 반영
- Sub Path Hosting 시 basename 설정
- Route path 일관성 유지
- Protected Route auth loading 처리
- Role-based Route와 backend security 구분
- `path="*"` NotFound route 제공
- Lazy route Suspense fallback 제공
- API path와 frontend route 충돌 방지
- route 이동 후 새로고침 검증 기준 제공

---

### [실무]

Router 예:

```jsx
<BrowserRouter basename={import.meta.env.VITE_ROUTER_BASENAME || "/"}>
  <Routes>
    <Route path="/" element={<MainPage />} />
    <Route path="/login" element={<LoginPage />} />
    <Route path="/festival/:id" element={<FestivalDetailPage />} />
    <Route path="*" element={<NotFoundPage />} />
  </Routes>
</BrowserRouter>
```

주의:

```text
basename은 route용
Vite base는 asset용
API Base URL은 API 요청용
```

---

### [FAQ]

Q. Frontend Agent는 SPA Routing에서 무엇을 구현해야 하는가?
A. Router 설정, route 목록, basename, protected route, not found route, lazy fallback을 구현해야 한다.

Q. basename을 API Base URL과 같이 써도 되는가?
A. 아니다. basename은 라우터 기준 경로이고 API Base URL은 API 요청 주소다.

Q. Protected Route에서 authLoading이 필요한 이유는?
A. 인증 상태 복원 전에 잘못된 redirect를 막기 위해 필요하다.

Q. NotFound route는 왜 필요한가?
A. 정의되지 않은 프론트엔드 route에 대해 앱 내부 404 화면을 제공하기 위해 필요하다.

---

## 9.3 Review Agent Rules

### [개념]

Review Agent는 SPA Routing 배포에서 직접 URL 접근, 새로고침, fallback 우선순위, API 충돌, basename 설정을 검토해야 한다.

---

### [핵심]

Review Agent Checklist:

```md
- [ ] Router Type이 확인되었는가?
- [ ] BrowserRouter 사용 시 server fallback이 있는가?
- [ ] HashRouter 사용 이유가 명확한가?
- [ ] 직접 URL 접근이 정상인가?
- [ ] 새로고침이 정상인가?
- [ ] API path가 fallback에서 제외되는가?
- [ ] static asset이 fallback에서 제외되는가?
- [ ] Sub Path Hosting 시 base와 basename이 일치하는가?
- [ ] Protected Route redirect가 정상인가?
- [ ] authLoading 없이 redirect loop가 발생하지 않는가?
- [ ] Role-based Route와 backend authorization이 구분되는가?
- [ ] NotFound route가 있는가?
- [ ] API 요청이 index.html을 반환하지 않는가?
```

---

### [실무]

Review Agent 판단 Flow:

```text
Build 실행
→ Static Hosting 실행
→ / 직접 접속
→ /login 직접 접속
→ /detail/1 새로고침
→ /api/health 호출
→ /assets/*.js 확인
→ Protected Route 확인
→ NotFound route 확인
```

Critical Issue:

```text
BrowserRouter인데 fallback 없음
API 요청에 index.html 반환
JS 요청에 index.html 반환
Sub Path base/basename mismatch
Refresh 404
Redirect Loop
```

승인 기준:

```text
직접 URL 접근 정상
새로고침 정상
API/fallback 충돌 없음
Asset/fallback 충돌 없음
Protected Route 정상
Console Critical Error 없음
```

---

### [FAQ]

Q. Review Agent는 SPA Routing에서 무엇을 가장 먼저 확인해야 하는가?
A. 직접 URL 접근과 새로고침이 404 없이 동작하는지 확인해야 한다.

Q. API 요청에 index.html이 오면 승인 가능한가?
A. 아니다. fallback 설정이 잘못된 치명적 문제다.

Q. BrowserRouter인데 fallback이 없으면 승인 가능한가?
A. 아니다. 운영에서 직접 URL 접근과 새로고침 404가 발생할 수 있다.

Q. HashRouter를 쓰면 Review 기준이 달라지는가?
A. fallback 부담은 줄지만 URL 정책과 프로젝트 요구사항에 맞는지 확인해야 한다.

---

# 10. Common Mistakes

## 10.1 SPA Routing Common Mistakes

### [개념]

SPA Routing Common Mistakes는 React SPA 배포 후 새로고침, 직접 URL 접근, route 충돌, fallback 오류를 만드는 반복 실수다.

---

### [핵심]

자주 발생하는 실수:

- BrowserRouter 사용 후 server fallback 미설정
- 개발 서버 정상만 보고 운영 fallback 미검증
- API path와 frontend route path 충돌
- `/api` 요청이 index.html로 fallback
- JS / CSS asset 요청이 index.html로 fallback
- Nginx `try_files` 누락
- Spring Boot fallback이 API path를 잡음
- Netlify `_redirects` 누락
- Vercel rewrite 누락
- S3 / CloudFront custom error response 누락
- GitHub Pages에서 BrowserRouter fallback 제약 무시
- Sub Path Hosting에서 basename 누락
- Vite base와 Router basename 혼동
- Protected Route에서 authLoading 없이 redirect
- 401 interceptor와 route guard redirect 충돌
- NotFound route 미구현
- Role-based Route만 믿고 backend authorization 누락

---

### [실무]

실수별 판단:

```text
새로고침 404
→ server fallback 확인

API가 HTML 반환
→ fallback exclusion / proxy 확인

JS MIME type error
→ asset fallback / base path 확인

하위 경로 route 깨짐
→ base / basename / server location 확인

로그인 페이지 반복 이동
→ authLoading / route guard / interceptor 확인

관리자 URL 직접 접근 가능
→ backend authorization 확인
```

---

### [FAQ]

Q. SPA Routing에서 가장 흔한 배포 실수는 무엇인가?
A. BrowserRouter를 사용하면서 운영 서버 fallback을 설정하지 않는 것이다.

Q. React route와 API route를 같은 경로로 두면 왜 위험한가?
A. fallback, proxy, security 설정에서 충돌해 API가 index.html을 반환할 수 있다.

Q. Vite base와 Router basename을 혼동하면 어떤 문제가 생기는가?
A. asset은 로드되지만 route가 깨지거나 route는 되지만 asset이 404가 될 수 있다.

Q. Protected Route만으로 관리자 보안이 되는가?
A. 아니다. 실제 권한 검증은 백엔드 Authorization에서 반드시 수행해야 한다.

---

# 11. Part06 Quality Checklist

## 11.1 Document Quality

### [개념]

이 문서는 Frontend Build & Deploy Domain의 Part06이며 SPA Routing Rules Retrieval에 최적화되어야 한다.

---

### [핵심]

문서 품질 기준:

- SPA Routing 정의 포함
- BrowserRouter / HashRouter 비교 포함
- Refresh 404 원인 포함
- Direct URL Access 포함
- SPA Fallback 정의 포함
- Fallback Priority 포함
- Nginx fallback 포함
- Spring Boot fallback 포함
- Netlify redirect 포함
- Vercel rewrite 포함
- S3 / CloudFront fallback 포함
- GitHub Pages routing 포함
- Router basename 포함
- Base Path와 Basename 구분 포함
- API Path Collision 포함
- Fallback Exclusion for API 포함
- Protected Route 배포 검증 포함
- Troubleshooting Flow 포함
- Agent별 판단 기준 포함
- Common Mistakes 포함
- Retrieval Queries 포함

---

### [실무]

Part06은 다음 문서와 연결된다.

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

Q. Part06의 핵심 목적은 무엇인가?
A. React SPA 배포에서 새로고침 404, fallback, basename, API path 충돌을 Agent가 정확히 판단하게 하는 것이다.

Q. Part06에서 API 통신 전체를 다루는가?
A. 아니다. API path와 fallback 충돌만 다루고 API Base URL 세부는 Part04에서 다룬다.

Q. Part06에서 Nginx 전체 배포를 다루는가?
A. 아니다. SPA fallback 중심으로 다루고 Nginx 상세 배포는 후속 Part에서 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. SPA Routing이란 무엇인가?
A. 브라우저에서 JavaScript가 URL에 따라 화면을 전환하는 라우팅 방식이다.

Q. React Router route는 서버 파일 경로인가?
A. 아니다. React Router route는 클라이언트 화면 전환 규칙이다.

Q. BrowserRouter란 무엇인가?
A. HTML5 History API를 사용해 `/login`, `/mypage` 같은 일반 URL을 사용하는 라우터다.

Q. HashRouter란 무엇인가?
A. URL의 `#` 이후 경로를 사용해 서버 fallback 없이 라우팅하기 쉬운 방식이다.

Q. BrowserRouter에서 새로고침 404가 나는 이유는?
A. 서버가 React route를 실제 파일 경로로 찾기 때문이다.

Q. HashRouter를 쓰면 새로고침 404가 해결되는가?
A. 대부분 해결될 수 있지만 URL에 `#`가 붙는다.

Q. Refresh 404란 무엇인가?
A. SPA route에서 새로고침하거나 직접 URL 접근 시 서버가 404를 반환하는 문제다.

Q. 클릭 이동은 되는데 새로고침하면 404가 나는 이유는?
A. 클릭 이동은 React Router가 처리하지만 새로고침은 서버가 먼저 URL을 처리하기 때문이다.

Q. Refresh 404는 React 코드 문제인가?
A. 대부분 서버 fallback 설정 문제다.

Q. Direct URL Access란 무엇인가?
A. 사용자가 주소창에 SPA route를 직접 입력해 접속하는 상황이다.

Q. 직접 URL 접근에서 404가 나면 무엇을 확인해야 하는가?
A. 서버 SPA fallback 설정과 base path, basename을 확인해야 한다.

Q. SPA Fallback이란 무엇인가?
A. 프론트엔드 route 요청에 대해 서버가 `index.html`을 반환하도록 하는 설정이다.

Q. SPA Fallback은 모든 요청에 적용해도 되는가?
A. 아니다. API와 정적 asset 요청은 제외해야 한다.

Q. Fallback Priority는 어떤 순서가 좋은가?
A. API Route, Static Asset, Existing File, SPA Route Fallback 순서가 좋다.

Q. API 요청에 index.html이 오면 무엇이 문제인가?
A. fallback이 API 요청까지 처리하고 있는 것이다.

Q. JS 요청에 index.html이 오면 어떤 문제가 생기는가?
A. MIME type error와 흰 화면이 발생할 수 있다.

Q. Nginx에서 React 새로고침 404는 어떻게 해결하는가?
A. `try_files $uri $uri/ /index.html;` 설정을 사용한다.

Q. Nginx에서 /api 요청이 index.html로 가면 어떻게 해야 하는가?
A. `/api/` location을 별도로 분리해 백엔드로 proxy해야 한다.

Q. Spring Boot 통합 배포에서도 SPA fallback이 필요한가?
A. React Router BrowserRouter를 사용하면 필요할 수 있다.

Q. Spring Boot fallback 때문에 API가 안 불릴 수 있는가?
A. 가능하다. fallback mapping이 API 경로를 잡으면 API 대신 index.html이 반환될 수 있다.

Q. Netlify에서 React 새로고침 404는 어떻게 해결하는가?
A. `_redirects`에 `/* /index.html 200`을 추가하거나 `netlify.toml` redirect를 설정한다.

Q. Vercel에서 React SPA 새로고침 404는 어떻게 해결하는가?
A. 필요한 경우 `vercel.json` rewrites로 frontend route를 `index.html`로 보낸다.

Q. S3에 React를 올렸는데 새로고침 404가 나는 이유는?
A. SPA fallback을 위한 error response 설정이 없기 때문이다.

Q. CloudFront에서 SPA fallback은 어떻게 설정하는가?
A. 403 또는 404 error response를 `/index.html`로 보내고 응답 코드를 200으로 설정한다.

Q. GitHub Pages에서 React Router 새로고침이 안 되는 이유는?
A. GitHub Pages는 서버 rewrite 설정이 제한적이기 때문이다.

Q. GitHub Pages에서 가장 쉬운 라우팅 해결책은 무엇인가?
A. HashRouter를 사용하는 것이 가장 단순한 해결책일 수 있다.

Q. Router basename이란 무엇인가?
A. React 앱이 하위 경로에서 동작할 때 사용하는 라우터 기준 경로다.

Q. 루트 도메인에 배포하면 basename이 필요한가?
A. 대부분 필요 없다.

Q. basename과 Vite base는 같은가?
A. 아니다. basename은 라우팅 기준이고 Vite base는 asset 경로 기준이다.

Q. Vite base와 Router basename을 둘 다 설정해야 하는가?
A. 하위 경로 배포라면 둘 다 필요할 수 있다.

Q. API Path Collision이란 무엇인가?
A. 프론트엔드 route와 백엔드 API route가 같은 경로를 사용해 충돌하는 문제다.

Q. API path는 어떻게 분리하는 것이 좋은가?
A. `/api` prefix를 사용하는 것이 안전하다.

Q. API path를 fallback에서 제외해야 하는 이유는?
A. API 요청에 index.html이 반환되는 문제를 막기 위해 필요하다.

Q. WebSocket path도 fallback에서 제외해야 하는가?
A. 그렇다. `/ws` 같은 실시간 연결 경로는 별도 proxy 또는 backend handler가 처리해야 한다.

Q. Protected Route란 무엇인가?
A. 로그인 여부나 권한에 따라 접근을 제어하는 프론트엔드 route다.

Q. /mypage 직접 접근 시 login으로 이동하면 배포 오류인가?
A. 로그인하지 않은 상태라면 정상 Protected Route 동작일 수 있다.

Q. Protected Route와 Refresh 404는 어떻게 구분하는가?
A. Refresh 404는 서버 404이고 Protected Route redirect는 React App이 로드된 뒤 발생한다.

Q. Role-based Route는 보안 기능인가?
A. UX 차원의 접근 제어일 뿐이며 실제 보안은 백엔드에서 보장해야 한다.

Q. 특정 route에서만 흰 화면이 나오는 이유는?
A. 해당 route component의 runtime error, lazy chunk 404, route path mismatch가 원인일 수 있다.

Q. Redirect Loop란 무엇인가?
A. route guard나 인증 로직이 반복 redirect를 발생시켜 페이지에 진입하지 못하는 문제다.

Q. authLoading 상태는 왜 필요한가?
A. token 복원이나 사용자 정보 조회가 끝나기 전 잘못된 redirect를 막기 위해 필요하다.

Q. React Not Found Page와 서버 404는 같은가?
A. 아니다. React Not Found는 앱 내부 화면이고 서버 404는 index.html을 받지 못한 상태다.

Q. path="\*" route는 왜 필요한가?
A. 정의되지 않은 프론트엔드 route에 대해 사용자 친화적인 404 화면을 제공하기 위해 필요하다.

Q. PM Agent는 SPA Routing에서 무엇을 정리해야 하는가?
A. Router 종류, fallback 방식, API prefix, sub path, 검증 route 목록을 정리해야 한다.

Q. Frontend Agent는 SPA Routing에서 무엇을 구현해야 하는가?
A. Router 설정, route 목록, basename, protected route, not found route, lazy fallback을 구현해야 한다.

Q. Review Agent는 SPA Routing에서 무엇을 가장 먼저 확인해야 하는가?
A. 직접 URL 접근과 새로고침이 404 없이 동작하는지 확인해야 한다.

Q. SPA Routing에서 가장 흔한 배포 실수는 무엇인가?
A. BrowserRouter를 사용하면서 운영 서버 fallback을 설정하지 않는 것이다.

Q. Part06 다음 문서는 무엇인가?
A. Part07 Spring Boot Integrated Deployment Rules로 이어지는 것이 적합하다.
