# Frontend Build & Deploy Part12 - Deployment Verification & Troubleshooting

---

# 1. Deployment Verification Core

## 1.1 Deployment Verification Definition

### [개념]

Deployment Verification은 프론트엔드 배포 후 실제 사용 환경에서 화면, 정적 파일, 라우팅, API, 인증, 캐시, HTTPS가 정상 동작하는지 확인하는 절차다.

검증 대상:

```text
Frontend Page
Static Assets
SPA Routing
API Request
Authentication
Authorization
Cookie / Token
HTTPS
WebSocket
Cache
Runtime Config
```

---

### [핵심]

Deployment Verification 핵심 규칙:

- Build 성공만으로 배포 성공을 판단하지 않는다.
- 배포 플랫폼의 Success 표시만 믿지 않는다.
- 실제 Production URL에서 검증한다.
- Browser DevTools Console과 Network를 반드시 확인한다.
- JS / CSS / API 요청의 status code를 확인한다.
- API Request URL에 `localhost`가 없는지 확인한다.
- API 응답이 JSON인지 HTML인지 확인한다.
- React route 새로고침과 직접 URL 접근을 확인한다.
- HTTPS 환경에서 Mixed Content가 없는지 확인한다.
- 인증 / 권한 흐름을 실제 사용자 시나리오로 확인한다.

---

### [실무]

2026 실무 기준으로 프론트엔드 배포 검증은 다음 순서로 진행한다.

```text
Production URL 접속
→ Console Error 확인
→ Network hard reload
→ index.html 확인
→ JS/CSS asset 확인
→ React route 확인
→ API request 확인
→ Auth flow 확인
→ HTTPS/Mixed Content 확인
→ Cache 확인
```

최소 검증 URL:

```text
/
/login
/signup
/mypage
/detail/1
/api/health
/api/auth/me
/assets/index.[hash].js
/static/js/main.[hash].js
```

Agent 판단 Flow:

```text
배포 방식 확인
→ 핵심 URL 목록 작성
→ Browser 검증
→ Network 검증
→ API 검증
→ 인증 검증
→ 문제 분류
→ 원인 후보 매핑
→ 수정 방향 결정
```

---

### [FAQ]

Q. Deployment Verification이란 무엇인가?
A. 배포 후 실제 URL에서 화면, asset, route, API, 인증, HTTPS, cache가 정상인지 확인하는 절차다.

Q. Build 성공이면 배포 성공인가?
A. 아니다. 실제 브라우저에서 정적 파일, API, 라우팅이 정상인지 확인해야 한다.

Q. 배포 검증에서 가장 먼저 확인할 것은 무엇인가?
A. Production URL의 Console Error와 Network 요청 상태를 먼저 확인한다.

Q. 배포 검증은 로컬이 아니라 어디서 해야 하는가?
A. 실제 배포 URL과 실제 사용자 브라우저 조건에서 해야 한다.

---

## 1.2 Verification Priority

### [개념]

Verification Priority는 배포 후 장애 영향도가 큰 항목부터 우선 확인하는 순서다.

---

### [핵심]

우선순위:

```text
1. 페이지 진입 가능 여부
2. JS bundle 로드 여부
3. CSS 로드 여부
4. Console Critical Error
5. SPA route 직접 접근 / 새로고침
6. API Request URL
7. API Status / Response Body
8. Auth Token / Cookie
9. HTTPS / Mixed Content
10. Cache / Old Version
```

치명도 높은 문제:

```text
White Screen
JS bundle 404
API 전체 실패
API localhost 호출
API HTML response
Refresh 404
Login impossible
Mixed Content Blocked
Secret exposed
```

---

### [실무]

장애 판단 기준:

```text
화면 자체가 안 뜸
→ Static File / JS / Runtime Error 우선 확인

화면은 뜨는데 데이터 없음
→ API URL / CORS / Auth 우선 확인

새로고침만 실패
→ SPA Fallback 우선 확인

로그인만 실패
→ Auth Header / Cookie / CORS Credentials 우선 확인

일부 사용자만 이전 화면
→ Cache / CDN / Service Worker 우선 확인
```

Review Agent는 치명도 순서대로 판단해야 한다.

```text
Critical
→ 배포 승인 불가

Major
→ 핵심 기능 영향 시 승인 보류

Minor
→ 사용자 영향 낮으면 후속 수정 가능
```

---

### [FAQ]

Q. 배포 검증 우선순위는 어떻게 잡는가?
A. 화면 진입, JS/CSS 로드, Console Error, 라우팅, API, 인증, HTTPS, 캐시 순서로 확인한다.

Q. 가장 치명적인 프론트엔드 배포 장애는 무엇인가?
A. White Screen, JS bundle 404, API 전체 실패, API localhost 호출이다.

Q. 화면은 뜨는데 데이터가 없으면 무엇을 먼저 확인하는가?
A. Network 탭에서 API Request URL, status, response body를 확인한다.

Q. 새로고침만 실패하면 무엇을 확인하는가?
A. SPA fallback 또는 platform rewrite 설정을 확인한다.

---

# 2. Browser Verification

## 2.1 Console Verification

### [개념]

Console Verification은 브라우저 개발자 도구 Console에서 JavaScript runtime error, Mixed Content, CORS, MIME type error를 확인하는 절차다.

---

### [핵심]

Console에서 확인할 오류:

```text
Uncaught TypeError
ReferenceError
Cannot read properties of undefined
Unexpected token '<'
Failed to load module script
MIME type error
Mixed Content
CORS policy error
ChunkLoadError
WebSocket connection failed
```

오류별 의미:

```text
Unexpected token '<'
→ HTML을 JSON/JS로 파싱하려고 함

Failed to load module script
→ JS 파일 Content-Type 문제

ChunkLoadError
→ lazy chunk 404 또는 cache mismatch

Mixed Content
→ HTTPS 페이지에서 HTTP 리소스 호출

CORS error
→ backend allowed origin/header/method 문제
```

---

### [실무]

Console 검증 Flow:

```text
Production URL 접속
→ DevTools Console 열기
→ Hard Reload
→ 첫 번째 Error 확인
→ Error stack 확인
→ Network 요청과 연결
→ 원인 분류
```

주의:

```text
Console Error 하나가 여러 후속 오류를 만들 수 있다.
항상 첫 번째 실제 error를 우선 분석한다.
```

Agent 판단 기준:

```text
Console Critical Error 존재
→ Network와 source map 여부 확인
→ build/env/asset/API 문제로 분류
```

---

### [FAQ]

Q. Console Verification이란 무엇인가?
A. 브라우저 Console에서 runtime error, CORS, Mixed Content, MIME type 문제를 확인하는 절차다.

Q. Console에서 가장 먼저 봐야 하는 것은?
A. 첫 번째 실제 error를 우선 확인해야 한다.

Q. Unexpected token '<'는 무엇을 의미하는가?
A. JSON이나 JS를 기대했지만 HTML이 응답되어 파싱에 실패한 경우가 많다.

Q. ChunkLoadError는 무엇을 의심해야 하는가?
A. lazy chunk 404, 이전 cache, 배포 artifact mismatch를 의심해야 한다.

---

## 2.2 Network Verification

### [개념]

Network Verification은 브라우저 Network 탭에서 실제 요청 URL, status code, response header, response body를 확인하는 절차다.

---

### [핵심]

Network 확인 대상:

```md
- [ ] document 요청
- [ ] JS bundle 요청
- [ ] CSS bundle 요청
- [ ] image/font 요청
- [ ] API 요청
- [ ] WebSocket 연결
- [ ] request URL
- [ ] status code
- [ ] response content-type
- [ ] response body
- [ ] request header
- [ ] response header
```

상태 코드 판단:

```text
200
→ 성공이지만 body/content-type 확인 필요

301/302
→ redirect 확인

304
→ cache 사용

401
→ 인증 필요 / token 문제

403
→ 권한 / CORS / CSRF / Security 문제

404
→ path / route / asset / API mapping 문제

413
→ upload body size 문제

500
→ backend error

502
→ proxy upstream 연결 실패

504
→ gateway timeout
```

---

### [실무]

Network 검증 Flow:

```text
Disable Cache 체크
→ Hard Reload
→ Preserve Log 필요 시 체크
→ document 요청 확인
→ JS/CSS 요청 확인
→ API 요청 확인
→ status/content-type/body 확인
```

판단 예:

```text
API status 200 + content-type text/html
→ API가 index.html 반환

JS status 200 + content-type text/html
→ JS 요청이 fallback됨

API Request URL localhost
→ production env 문제

API 401
→ Authorization Header / Cookie 확인

API CORS error
→ backend CORS 설정 확인
```

---

### [FAQ]

Q. Network Verification이란 무엇인가?
A. 브라우저가 실제 요청한 URL, status, header, body를 확인하는 절차다.

Q. API status 200이면 무조건 정상인가?
A. 아니다. response body와 content-type이 JSON인지 확인해야 한다.

Q. API 응답이 text/html이면 무엇을 의심해야 하는가?
A. SPA fallback이 API 요청을 index.html로 반환했을 가능성이 높다.

Q. JS 요청이 text/html이면 무엇을 의심해야 하는가?
A. asset path 오류 또는 fallback이 JS 요청을 index.html로 반환한 문제를 의심해야 한다.

---

## 2.3 Application Tab Verification

### [개념]

Application Tab Verification은 브라우저 Application 탭에서 Local Storage, Session Storage, Cookie, Service Worker, Cache Storage를 확인하는 절차다.

---

### [핵심]

확인 대상:

```text
Local Storage
Session Storage
Cookies
Service Workers
Cache Storage
IndexedDB
Manifest
```

사용 시나리오:

- JWT accessToken 저장 확인
- refresh token cookie 저장 확인
- Cookie SameSite / Secure / Domain 확인
- Service Worker가 이전 파일을 제공하는지 확인
- Cache Storage에 이전 asset이 남아 있는지 확인
- PWA manifest 로드 확인

---

### [실무]

인증 검증:

```text
Login 요청
→ Response Set-Cookie 확인
→ Application Cookies 확인
→ 이후 API Request Cookie 포함 확인
```

Token 검증:

```text
Login 요청
→ accessToken 저장 확인
→ API Request Authorization Header 확인
```

Cache 검증:

```text
Application → Service Workers
→ 등록된 worker 확인
→ Cache Storage 확인
→ 필요 시 unregister / clear storage 테스트
```

---

### [FAQ]

Q. Application 탭에서는 무엇을 확인하는가?
A. token, cookie, service worker, cache storage 같은 브라우저 저장 상태를 확인한다.

Q. 로그인 후 쿠키가 저장되지 않으면 어디를 보는가?
A. Network Set-Cookie와 Application Cookies를 함께 확인한다.

Q. 배포 후 이전 화면이 계속 보이면 무엇을 확인하는가?
A. Service Worker와 Cache Storage를 확인해야 한다.

Q. JWT token이 저장되었는데 API가 401이면 무엇을 확인하는가?
A. Request Header에 Authorization이 실제로 포함되는지 확인해야 한다.

---

# 3. Static Asset Troubleshooting

## 3.1 White Screen

### [개념]

White Screen은 배포 후 브라우저에 빈 화면만 표시되고 React 앱이 정상 렌더링되지 않는 문제다.

---

### [핵심]

대표 원인:

```text
JS bundle 404
CSS 404
JS MIME type error
Runtime JavaScript error
Environment variable undefined
API initialization failure
Router basename mismatch
Vite base / CRA homepage 오류
ChunkLoadError
Browser cache mismatch
Service Worker cache
```

---

### [실무]

Troubleshooting Flow:

```text
Console 첫 번째 error 확인
→ Network JS bundle status 확인
→ JS content-type 확인
→ CSS status 확인
→ env 값 확인
→ route basename/base path 확인
→ cache 확인
```

원인별 판단:

```text
JS 404
→ output directory / hosting root / base path 확인

JS text/html
→ fallback이 asset 요청 처리

Runtime TypeError
→ 코드 / env / API response 구조 확인

ChunkLoadError
→ cache mismatch / old index.html 확인
```

Critical 기준:

```text
Production White Screen
→ 배포 승인 불가
→ rollback 고려
```

---

### [FAQ]

Q. White Screen이란 무엇인가?
A. 배포 후 React 앱이 렌더링되지 않고 빈 화면만 표시되는 문제다.

Q. White Screen이면 무엇을 먼저 확인하는가?
A. Console 첫 번째 error와 Network의 JS bundle 로드 상태를 확인한다.

Q. JS bundle 404는 무엇을 확인해야 하는가?
A. Build Output, hosting root, base path, output directory를 확인해야 한다.

Q. White Screen은 rollback 대상인가?
A. 운영 핵심 화면에서 발생하면 rollback 대상이다.

---

## 3.2 JS CSS 404

### [개념]

JS CSS 404는 배포 후 브라우저가 JavaScript 또는 CSS 파일을 찾지 못하는 문제다.

---

### [핵심]

대표 원인:

- Output Directory 오류
- Build Output 복사 누락
- Vite `base` 오류
- CRA `homepage` 오류
- Nginx root 오류
- Spring Boot static 위치 오류
- S3 upload 누락
- GitHub Pages base path 오류
- 파일명 대소문자 오류
- 이전 `index.html`이 이전 hash asset 참조

---

### [실무]

Troubleshooting Flow:

```text
Network 404 asset path 확인
→ index.html script/link src 확인
→ Build Output에 파일 존재 확인
→ Hosting target에 파일 존재 확인
→ base/homepage 확인
→ cache 확인
```

Vite:

```text
/assets/index.[hash].js
```

CRA:

```text
/static/js/main.[hash].js
```

판단 기준:

```text
Vite인데 /static/js 요청
→ CRA/Vite 설정 혼동 가능

CRA인데 /assets 요청
→ Vite/CRA 설정 혼동 가능
```

---

### [FAQ]

Q. JS CSS 404란 무엇인가?
A. 브라우저가 React 실행에 필요한 JS 또는 CSS 파일을 찾지 못하는 문제다.

Q. JS 404가 발생하면 무엇을 확인해야 하는가?
A. index.html이 참조하는 script 경로와 실제 배포된 파일 위치를 비교해야 한다.

Q. Vite asset 경로는 보통 무엇인가?
A. 보통 `/assets/...` 형태다.

Q. CRA asset 경로는 보통 무엇인가?
A. 보통 `/static/js/...`, `/static/css/...` 형태다.

---

## 3.3 MIME Type Error

### [개념]

MIME Type Error는 브라우저가 JS, CSS 파일을 기대했지만 서버가 HTML이나 잘못된 Content-Type을 반환해 실행을 거부하는 문제다.

---

### [핵심]

대표 메시지:

```text
Failed to load module script:
Expected a JavaScript module script
but the server responded with a MIME type of "text/html"
```

대표 원인:

- JS 요청이 index.html로 fallback
- CSS 요청이 index.html로 fallback
- asset file missing
- server mime.types 설정 문제
- base path 오류
- fallback이 asset 요청까지 처리

---

### [실무]

Troubleshooting Flow:

```text
Network에서 JS/CSS 요청 선택
→ Response Headers Content-Type 확인
→ Response Body 확인
→ body가 index.html인지 확인
→ asset 실제 존재 확인
→ fallback 설정 확인
```

판단 기준:

```text
Content-Type text/html + index.html body
→ fallback / asset path 문제

Content-Type text/plain
→ server mime 설정 문제 가능성

Status 404
→ asset path / upload / copy 문제
```

---

### [FAQ]

Q. MIME Type Error란 무엇인가?
A. JS/CSS 요청에 잘못된 Content-Type이 반환되어 브라우저가 실행을 거부하는 문제다.

Q. JS 요청에 text/html이 오면 무엇을 의미하는가?
A. JS 파일 대신 index.html이 반환되었을 가능성이 높다.

Q. MIME Type Error는 프론트 코드 문제인가?
A. 대부분 hosting root, asset path, fallback, server MIME 설정 문제다.

Q. MIME Type Error는 어디서 확인하는가?
A. Console Error와 Network Response Headers에서 확인한다.

---

## 3.4 ChunkLoadError

### [개념]

ChunkLoadError는 Code Splitting 또는 Lazy Loading으로 분리된 JavaScript chunk 파일을 브라우저가 로드하지 못할 때 발생하는 문제다.

---

### [핵심]

대표 원인:

- lazy chunk 404
- 이전 index.html이 새 chunk를 참조하지 못함
- 새 index.html이 이전 chunk를 참조
- CDN cache mismatch
- 브라우저 cache mismatch
- Service Worker가 이전 asset 제공
- 배포 중 일부 파일만 업로드
- old asset 삭제 타이밍 문제

---

### [실무]

Troubleshooting Flow:

```text
Console ChunkLoadError 확인
→ Network chunk 요청 404 확인
→ index.html cache 확인
→ CDN cache 확인
→ Service Worker 확인
→ artifact upload completeness 확인
```

해결 방향:

```text
index.html no-cache
hashed assets long-cache
배포 시 artifact 전체 업로드
CloudFront invalidation
Service Worker update 전략
사용자 refresh 안내 또는 자동 reload 처리
```

주의:

```text
ChunkLoadError가 대량 발생하면
cache 전략 또는 배포 artifact mismatch 가능성이 높다.
```

---

### [FAQ]

Q. ChunkLoadError란 무엇인가?
A. lazy loading chunk 파일을 브라우저가 로드하지 못할 때 발생하는 오류다.

Q. ChunkLoadError의 대표 원인은 무엇인가?
A. cache mismatch, chunk 404, 배포 artifact mismatch가 대표 원인이다.

Q. ChunkLoadError는 어디서 확인하는가?
A. Console Error와 Network chunk 요청 status에서 확인한다.

Q. ChunkLoadError를 줄이려면 어떻게 해야 하는가?
A. index.html cache를 짧게 하고 artifact 전체 업로드와 CDN invalidation을 관리해야 한다.

---

# 4. SPA Routing Troubleshooting

## 4.1 Refresh 404

### [개념]

Refresh 404는 React route에서 새로고침하거나 직접 URL 접근 시 서버가 404를 반환하는 문제다.

---

### [핵심]

대표 원인:

```text
BrowserRouter 사용
SPA fallback 없음
Nginx try_files 누락
Spring Boot fallback 누락
Netlify _redirects 누락
Vercel rewrite 누락
CloudFront custom error response 누락
GitHub Pages rewrite 제약
Sub Path fallback 오류
```

---

### [실무]

Troubleshooting Flow:

```text
메인 페이지 접속
→ 내부 링크 이동
→ 이동한 route 새로고침
→ 404 확인
→ hosting 방식 확인
→ fallback 설정 확인
→ API path 제외 확인
```

플랫폼별 수정:

```text
Nginx
→ try_files $uri $uri/ /index.html

Spring Boot
→ SpaController forward:/index.html

Netlify
→ /* /index.html 200

Vercel
→ rewrites to /index.html

CloudFront
→ 403/404 custom error response to /index.html

GitHub Pages
→ HashRouter or 404 workaround
```

---

### [FAQ]

Q. Refresh 404란 무엇인가?
A. React route에서 새로고침하거나 직접 URL 접근 시 서버가 404를 반환하는 문제다.

Q. 클릭 이동은 되는데 새로고침이 안 되는 이유는?
A. 클릭 이동은 React Router가 처리하지만 새로고침은 서버가 먼저 URL을 처리하기 때문이다.

Q. Refresh 404는 React 코드 문제인가?
A. 대부분 hosting fallback 설정 문제다.

Q. Refresh 404 해결 핵심은 무엇인가?
A. frontend route 요청에 `index.html`을 반환하도록 서버 fallback을 설정하는 것이다.

---

## 4.2 API Returns index.html

### [개념]

API Returns index.html은 API 요청에 JSON이 아니라 React `index.html` HTML 문서가 반환되는 문제다.

---

### [핵심]

대표 증상:

```text
API Response Content-Type: text/html
Response Body: <!doctype html>
Console: Unexpected token '<'
Status: 200
Backend log에 요청 없음
```

대표 원인:

- SPA fallback이 API path까지 처리
- Nginx `/api` location 누락
- Vercel / Netlify rewrite 순서 오류
- Spring Boot fallback이 API path를 잡음
- CloudFront fallback이 API path까지 처리
- API prefix 미분리
- API Base URL이 frontend domain을 잘못 호출

---

### [실무]

Troubleshooting Flow:

```text
Network API response body 확인
→ content-type 확인
→ request URL 확인
→ backend log 확인
→ fallback/rewrite/proxy 설정 확인
→ API prefix 확인
```

수정 원칙:

```text
API path
→ backend/proxy/function으로 전달

Frontend route
→ index.html fallback

Static asset
→ actual file
```

검증:

```text
GET /api/health
→ JSON

GET /login
→ index.html

GET /assets/index.js
→ JavaScript
```

---

### [FAQ]

Q. API Returns index.html이란 무엇인가?
A. API 요청에 JSON이 아니라 React index.html이 반환되는 문제다.

Q. API 요청에 index.html이 오면 무엇을 확인해야 하는가?
A. fallback, rewrite, proxy, API prefix 설정을 확인해야 한다.

Q. status 200인데 API가 실패할 수 있는가?
A. 가능하다. 200이어도 body가 HTML이면 JSON 파싱이 실패한다.

Q. Backend log에 API 요청이 없으면 무엇을 의심해야 하는가?
A. Nginx나 플랫폼이 API 요청을 백엔드로 보내지 않고 index.html을 반환했을 가능성이 있다.

---

## 4.3 Sub Path Routing Failure

### [개념]

Sub Path Routing Failure는 앱을 `/my-app` 같은 하위 경로에 배포했을 때 asset 또는 route가 깨지는 문제다.

---

### [핵심]

대표 원인:

- Vite `base` 누락
- CRA `homepage` 누락
- React Router `basename` 누락
- Nginx location path 오류
- Spring Boot context path 불일치
- GitHub Pages repository path 불일치
- CloudFront behavior path 오류

증상:

```text
JS/CSS 404
route match 실패
메인만 표시
새로고침 404
링크 클릭 시 루트로 이동
이미지 깨짐
```

---

### [실무]

검증 Flow:

```text
배포 URL 확인
→ sub path 여부 확인
→ asset path 확인
→ router basename 확인
→ server fallback path 확인
→ 직접 URL 접근 확인
```

하위 경로 예:

```text
Deploy URL:
https://example.com/admin-app/

Vite base:
"/admin-app/"

Router basename:
"/admin-app"
```

구분:

```text
Asset 404
→ Vite base / CRA homepage

Route mismatch
→ Router basename

Refresh 404
→ server fallback path
```

---

### [FAQ]

Q. Sub Path Routing Failure란 무엇인가?
A. 앱을 하위 경로에 배포했을 때 asset, route, fallback 경로가 맞지 않아 발생하는 문제다.

Q. 하위 경로 배포에서 Vite base는 무엇을 담당하는가?
A. JS/CSS asset이 로드될 기준 경로를 담당한다.

Q. 하위 경로 배포에서 Router basename은 무엇을 담당하는가?
A. React Router가 route를 해석하는 기준 경로를 담당한다.

Q. 하위 경로에서 새로고침 404가 나면 무엇을 확인하는가?
A. 서버 fallback이 하위 경로 기준으로 설정되어 있는지 확인한다.

---

# 5. API Troubleshooting

## 5.1 API URL Failure

### [개념]

API URL Failure는 프론트엔드가 잘못된 API 주소로 요청을 보내 데이터 호출에 실패하는 문제다.

---

### [핵심]

대표 원인:

```text
Production env 누락
API Base URL localhost
Docker service name 사용
/api prefix 중복
/api prefix 누락
http/https mismatch
staging/production env 혼동
runtime config cache
```

---

### [실무]

Troubleshooting Flow:

```text
Network Request URL 확인
→ localhost 여부 확인
→ backend service name 여부 확인
→ /api 중복 여부 확인
→ protocol 확인
→ env 값 확인
→ build-time/runtime config 구분
```

위험 URL:

```text
http://localhost:8080
http://backend:8080
https://example.com/api/api
http://api.example.com
```

권장 URL:

```text
/api
https://api.example.com
https://example.com/api
```

---

### [FAQ]

Q. API URL Failure란 무엇인가?
A. 프론트엔드가 잘못된 API 주소로 요청을 보내 API 호출에 실패하는 문제다.

Q. 운영에서 API URL이 localhost면 왜 문제인가?
A. 사용자 브라우저의 localhost로 요청하기 때문에 실제 백엔드에 도달하지 못한다.

Q. API URL이 backend:8080이면 왜 문제인가?
A. 브라우저는 Docker 내부 service name을 알 수 없기 때문이다.

Q. /api/api가 생기면 무엇을 확인하는가?
A. baseURL과 endpoint path에 `/api`가 중복되었는지 확인한다.

---

## 5.2 CORS Failure

### [개념]

CORS Failure는 브라우저가 다른 Origin의 API 요청을 보낼 때 백엔드가 해당 Origin, Header, Method를 허용하지 않아 차단되는 문제다.

---

### [핵심]

대표 원인:

- 백엔드 allowed origin 누락
- staging / production domain 누락
- Authorization header 미허용
- Content-Type header 미허용
- OPTIONS preflight 미처리
- Credentials 사용 시 wildcard origin 사용
- Cookie 인증인데 credentials 설정 불일치
- HTTPS / HTTP Origin 불일치

---

### [실무]

Troubleshooting Flow:

```text
Console CORS error 확인
→ Request Origin 확인
→ Request Method 확인
→ Request Headers 확인
→ Preflight OPTIONS 확인
→ Backend CORS 설정 확인
→ credentials 여부 확인
```

Credentials 주의:

```text
Access-Control-Allow-Credentials: true
+
Access-Control-Allow-Origin: *
→ 불가
```

확인 대상:

```md
- [ ] Origin이 정확히 허용되어 있는가?
- [ ] Authorization header가 허용되어 있는가?
- [ ] Content-Type이 허용되어 있는가?
- [ ] OPTIONS 요청이 정상 처리되는가?
- [ ] credentials 설정이 일치하는가?
```

---

### [FAQ]

Q. CORS Failure란 무엇인가?
A. 브라우저가 다른 Origin API 요청을 백엔드 허용 정책 때문에 차단하는 문제다.

Q. CORS는 프론트엔드에서 해결하는가?
A. 대부분 백엔드에서 allowed origin, method, header를 설정해야 해결된다.

Q. Authorization Header가 있으면 CORS에 영향이 있는가?
A. 있다. allowed headers에 Authorization이 포함되어야 할 수 있다.

Q. Credentials 사용 시 wildcard origin을 써도 되는가?
A. 안 된다. 명시적인 Origin을 사용해야 한다.

---

## 5.3 Mixed Content Failure

### [개념]

Mixed Content Failure는 HTTPS 페이지에서 HTTP API, 이미지, WebSocket 등을 호출해 브라우저가 차단하는 문제다.

---

### [핵심]

대표 문제:

```text
Frontend: https://example.com
API: http://api.example.com
Result: Blocked
```

대상:

```text
HTTP API
HTTP image
HTTP script
HTTP stylesheet
HTTP font
ws:// WebSocket
```

---

### [실무]

Troubleshooting Flow:

```text
Console Mixed Content 확인
→ Network blocked request 확인
→ API Base URL 확인
→ asset external URL 확인
→ WebSocket protocol 확인
→ HTTPS URL로 수정
→ rebuild/redeploy
```

정상 기준:

```text
Frontend HTTPS
→ API HTTPS
→ WebSocket WSS
→ External assets HTTPS
```

---

### [FAQ]

Q. Mixed Content Failure란 무엇인가?
A. HTTPS 페이지에서 HTTP 리소스를 호출해 브라우저가 차단하는 문제다.

Q. HTTPS 페이지에서 HTTP API를 호출해도 되는가?
A. 안 된다. Mixed Content로 차단될 수 있다.

Q. WebSocket도 Mixed Content 영향을 받는가?
A. 받는다. HTTPS 페이지에서는 `wss://`를 사용해야 한다.

Q. Mixed Content는 어디서 확인하는가?
A. Console과 Network 탭에서 확인한다.

---

## 5.4 Backend 500 Failure

### [개념]

Backend 500 Failure는 프론트엔드 API 요청은 백엔드에 도달했지만 백엔드 내부 오류로 실패하는 상태다.

---

### [핵심]

특징:

```text
Request URL 정상
CORS 아님
Proxy 도달 성공
Backend log에 요청 있음
Response status 500
```

대표 원인:

- backend exception
- DB 연결 실패
- query error
- validation 누락
- null pointer
- external API failure
- env 누락
- file upload path 오류

---

### [실무]

Troubleshooting Flow:

```text
Network API status 500 확인
→ Response body 확인
→ Backend log 확인
→ request payload 확인
→ backend env 확인
→ DB / external dependency 확인
```

Frontend 판단:

```text
500 error
→ 프론트엔드 URL 문제보다 backend log 확인 우선
```

단, 다음은 예외:

```text
잘못된 payload
잘못된 API path
잘못된 content-type
필수 header 누락
```

---

### [FAQ]

Q. Backend 500 Failure란 무엇인가?
A. API 요청이 백엔드에 도달했지만 백엔드 내부 오류로 실패한 상태다.

Q. 500 에러는 프론트엔드 문제인가?
A. 대부분 백엔드 문제지만 잘못된 payload나 header가 원인일 수도 있다.

Q. 500 에러는 어디서 확인해야 하는가?
A. 브라우저 Network와 백엔드 서버 로그를 함께 확인해야 한다.

Q. 500 에러가 나면 CORS 설정을 먼저 봐야 하는가?
A. 아니다. 요청이 백엔드에 도달했다면 백엔드 로그를 먼저 봐야 한다.

---

# 6. Authentication Troubleshooting

## 6.1 Login Failure

### [개념]

Login Failure는 배포 후 로그인 요청, token 저장, cookie 저장, 인증 상태 복원 중 하나가 실패하는 문제다.

---

### [핵심]

대표 원인:

```text
API Base URL 오류
CORS credentials 오류
withCredentials 누락
Set-Cookie 누락
SameSite / Secure / Domain 오류
Authorization Header 누락
Token storage 오류
HTTPS 미적용
Spring Security redirect
Response body 구조 변경
```

---

### [실무]

Login Troubleshooting Flow:

```text
Login API Request 확인
→ Request URL 확인
→ Request Payload 확인
→ Response Status 확인
→ Response Body 확인
→ Set-Cookie / Token 확인
→ Storage 확인
→ 이후 /me API 확인
```

Cookie 인증:

```text
Set-Cookie 확인
→ Application Cookies 확인
→ 이후 Request Cookie 포함 확인
```

JWT Header 인증:

```text
accessToken response 확인
→ storage 저장 확인
→ Authorization Header 확인
```

---

### [FAQ]

Q. Login Failure란 무엇인가?
A. 로그인 요청, token 저장, cookie 저장, 인증 상태 복원 중 하나가 실패하는 문제다.

Q. 로그인 API는 성공인데 로그인 상태가 유지되지 않으면 무엇을 확인하는가?
A. token 저장 또는 cookie 저장 여부와 이후 API 요청에 인증 정보가 포함되는지 확인한다.

Q. Cookie 인증에서 로그인 유지가 안 되면 무엇을 확인하는가?
A. Set-Cookie, withCredentials, SameSite, Secure, Domain, CORS credentials를 확인한다.

Q. JWT 인증에서 로그인 유지가 안 되면 무엇을 확인하는가?
A. accessToken 저장 위치와 Authorization Header 전송 여부를 확인한다.

---

## 6.2 Authorization Header Failure

### [개념]

Authorization Header Failure는 JWT 같은 인증 token이 API 요청 Header에 포함되지 않거나 형식이 잘못되어 인증에 실패하는 문제다.

---

### [핵심]

대표 원인:

- token 저장 안 됨
- interceptor 미등록
- 다른 axios instance 사용
- Bearer prefix 누락
- token 만료
- refresh flow 실패
- Authorization header가 CORS allowed headers에 없음
- logout 후 stale state
- API 요청 시점에 token loading 전

---

### [실무]

검증 Flow:

```text
Application Storage token 확인
→ Network Request Headers 확인
→ Authorization 존재 확인
→ Bearer prefix 확인
→ Response 401 확인
→ refresh API 확인
```

정상 Header:

```text
Authorization: Bearer eyJ...
```

주의:

```text
token이 Storage에 있음
≠
Request Header에 포함됨
```

---

### [FAQ]

Q. Authorization Header Failure란 무엇인가?
A. 인증 token이 API 요청 Header에 포함되지 않거나 형식이 잘못되어 인증에 실패하는 문제다.

Q. token은 있는데 API가 401이면 무엇을 확인하는가?
A. Request Header에 Authorization이 실제로 포함되는지 확인해야 한다.

Q. Bearer prefix가 필요한가?
A. 백엔드가 Bearer token 방식을 기대한다면 필요하다.

Q. Authorization Header 때문에 CORS가 날 수 있는가?
A. 가능하다. 백엔드 allowed headers에 Authorization이 필요할 수 있다.

---

## 6.3 Cookie Failure

### [개념]

Cookie Failure는 로그인 응답에서 쿠키가 저장되지 않거나 이후 요청에 쿠키가 포함되지 않는 문제다.

---

### [핵심]

대표 원인:

```text
withCredentials 누락
Access-Control-Allow-Credentials 누락
Access-Control-Allow-Origin wildcard 사용
SameSite 설정 오류
Secure 설정 오류
Domain 설정 오류
Path 설정 오류
HTTP 환경에서 Secure cookie 사용
third-party cookie 제한
```

---

### [실무]

Troubleshooting Flow:

```text
Login Response Set-Cookie 확인
→ Application Cookies 확인
→ Cookie Domain/Path 확인
→ SameSite/Secure 확인
→ 다음 API Request Cookie 포함 확인
→ CORS credentials 확인
```

Cross-Origin Cookie 조건:

```text
Frontend axios withCredentials: true
Backend Access-Control-Allow-Credentials: true
Backend Access-Control-Allow-Origin: explicit origin
Cookie SameSite=None; Secure
HTTPS 필요
```

Same-Origin Proxy 구조:

```text
Frontend and API same origin
→ cookie 설정 복잡도 감소 가능
```

---

### [FAQ]

Q. Cookie Failure란 무엇인가?
A. 쿠키가 저장되지 않거나 이후 요청에 포함되지 않아 인증이 실패하는 문제다.

Q. Set-Cookie가 있는데 쿠키가 저장되지 않는 이유는?
A. SameSite, Secure, Domain, CORS credentials, HTTPS 조건이 맞지 않을 수 있다.

Q. Cookie 인증에서 withCredentials가 필요한가?
A. Cross-Origin Cookie 인증에서는 필요할 수 있다.

Q. Credentials 사용 시 Access-Control-Allow-Origin을 \*로 해도 되는가?
A. 안 된다. 명시적인 Origin을 사용해야 한다.

---

## 6.4 Redirect Loop

### [개념]

Redirect Loop는 인증 또는 권한 판단 로직이 반복적으로 페이지 이동을 발생시켜 사용자가 화면에 접근하지 못하는 문제다.

---

### [핵심]

대표 원인:

- auth loading 상태 없음
- token 복원 전에 redirect
- login route도 protected 처리
- 401 interceptor와 route guard 동시 redirect
- refresh token 실패 반복
- redirect target이 다시 protected route
- role check 조건 오류
- `/403` page가 다시 guard 대상

---

### [실무]

Troubleshooting Flow:

```text
URL 변화 확인
→ route guard 조건 확인
→ auth loading 상태 확인
→ token restore timing 확인
→ 401 interceptor 확인
→ redirect target 확인
→ Network 반복 요청 확인
```

안전 기준:

```text
auth loading 중
→ redirect하지 않음

login route
→ protected에서 제외

401 처리
→ 한 번만 redirect

권한 없음
→ /403 또는 안전 route로 이동
```

---

### [FAQ]

Q. Redirect Loop란 무엇인가?
A. 인증 또는 권한 로직이 반복 redirect를 발생시켜 페이지에 접근하지 못하는 문제다.

Q. 로그인 페이지로 계속 튕기면 무엇을 확인하는가?
A. auth loading, token restore, route guard, 401 interceptor를 확인한다.

Q. auth loading은 왜 필요한가?
A. 인증 상태 복원 전에 잘못된 redirect를 막기 위해 필요하다.

Q. 401 interceptor가 redirect loop를 만들 수 있는가?
A. 가능하다. route guard와 동시에 redirect하면 반복 이동이 발생할 수 있다.

---

# 7. WebSocket Troubleshooting

## 7.1 WebSocket Connection Failure

### [개념]

WebSocket Connection Failure는 배포 환경에서 실시간 연결이 열리지 않거나 연결 직후 끊기는 문제다.

---

### [핵심]

대표 원인:

```text
ws/wss protocol mismatch
Nginx Upgrade header 누락
WebSocket proxy location 누락
/ws path가 SPA fallback에 잡힘
Spring allowed origin 오류
인증 token 전달 실패
HTTPS 페이지에서 ws:// 사용
proxy timeout
backend WebSocket endpoint 오류
```

---

### [실무]

Troubleshooting Flow:

```text
Network WS 탭 확인
→ WebSocket Request URL 확인
→ status 101 확인
→ Console error 확인
→ Nginx /ws location 확인
→ Backend WebSocket log 확인
→ allowed origin 확인
```

정상 기준:

```text
HTTPS page
→ wss://example.com/ws

Nginx
→ proxy_set_header Upgrade
→ proxy_set_header Connection "upgrade"

Response
→ 101 Switching Protocols
```

---

### [FAQ]

Q. WebSocket Connection Failure란 무엇인가?
A. 배포 환경에서 WebSocket 연결이 열리지 않거나 연결 직후 끊기는 문제다.

Q. WebSocket 정상 연결 status는 무엇인가?
A. 일반적으로 101 Switching Protocols가 정상이다.

Q. HTTPS 페이지에서 ws://를 사용해도 되는가?
A. 안 된다. `wss://`를 사용해야 한다.

Q. Nginx WebSocket proxy에서 무엇이 중요한가?
A. Upgrade header와 `/ws` location 분리가 중요하다.

---

## 7.2 STOMP SockJS Failure

### [개념]

STOMP SockJS Failure는 STOMP 또는 SockJS 기반 실시간 통신에서 endpoint, fallback transport, CORS, proxy 설정이 맞지 않아 연결이 실패하는 문제다.

---

### [핵심]

대표 원인:

- endpoint path 불일치
- SockJS 하위 path proxy 누락
- allowed origin 불일치
- STOMP destination 오류
- broker prefix 오류
- token 전달 방식 오류
- fallback XHR 요청이 CORS 차단
- `/ws/**`가 index.html 반환

---

### [실무]

Troubleshooting Flow:

```text
Frontend endpoint URL 확인
→ Spring endpoint 확인
→ Nginx /ws/ proxy 확인
→ Network WS/XHR 확인
→ allowed origin 확인
→ STOMP destination 확인
```

구분:

```text
Endpoint
→ 연결 URL

Destination
→ 메시지 routing path

Subscribe path
→ 구독 대상

Publish path
→ 전송 대상
```

검증 기준:

```text
/ws 연결 요청
→ backend 도달

/ws/** SockJS 요청
→ index.html 반환 금지
```

---

### [FAQ]

Q. STOMP SockJS Failure란 무엇인가?
A. STOMP/SockJS 연결에서 endpoint, proxy, CORS, destination 설정이 맞지 않아 실패하는 문제다.

Q. SockJS를 쓰면 Nginx에서 무엇을 주의해야 하는가?
A. `/ws/**` 하위 요청 전체를 백엔드로 proxy해야 한다.

Q. endpoint와 destination은 같은가?
A. 아니다. endpoint는 연결 URL이고 destination은 메시지 routing 경로다.

Q. SockJS 요청이 index.html을 반환하면 무엇이 문제인가?
A. `/ws/**` 요청이 SPA fallback에 잡히고 있는 것이다.

---

# 8. Cache Troubleshooting

## 8.1 Old Version Displayed

### [개념]

Old Version Displayed는 새로 배포했는데 사용자 브라우저에서 이전 화면이나 이전 JavaScript가 계속 표시되는 문제다.

---

### [핵심]

대표 원인:

```text
Browser cache
CDN cache
CloudFront cache
Service Worker cache
index.html long cache
config.json long cache
old container still running
old Docker image
artifact path 오류
static folder 미정리
```

---

### [실무]

Troubleshooting Flow:

```text
Hard Reload
→ Disable Cache 테스트
→ Network Response Headers 확인
→ index.html cache 확인
→ CDN cache 확인
→ Service Worker 확인
→ deployed artifact 확인
```

배포 방식별 확인:

```text
S3/CloudFront
→ invalidation 확인

Docker
→ running container image 확인

Spring Boot 통합
→ JAR 재빌드 확인

Nginx
→ root 파일 timestamp 확인

Platform
→ previous deploy / CDN cache 확인
```

---

### [FAQ]

Q. Old Version Displayed란 무엇인가?
A. 새로 배포했는데 이전 화면이나 이전 JavaScript가 계속 표시되는 문제다.

Q. 이전 화면이 보이면 무엇을 먼저 확인하는가?
A. Browser cache, CDN cache, Service Worker, 실제 배포 artifact를 확인한다.

Q. index.html을 오래 캐시하면 왜 위험한가?
A. 이전 JS/CSS hash를 계속 참조해 새 배포가 반영되지 않을 수 있다.

Q. Docker에서 이전 화면이 보이면 무엇을 확인하는가?
A. 새 image로 container가 recreate 되었는지 확인해야 한다.

---

## 8.2 CDN Cache Failure

### [개념]

CDN Cache Failure는 CDN이 이전 파일을 계속 제공하거나 잘못된 Cache-Control로 새 배포 반영이 지연되는 문제다.

---

### [핵심]

대표 원인:

- index.html 장기 캐시
- CloudFront invalidation 누락
- config.json 장기 캐시
- cache policy 오류
- CDN edge propagation 지연
- old asset cleanup 오류
- service worker와 CDN cache 복합 문제

---

### [실무]

Troubleshooting Flow:

```text
Network Response Headers 확인
→ Cache-Control 확인
→ Age / cache status 확인
→ CDN invalidation 확인
→ origin file 확인
→ edge cache refresh
```

권장 Cache:

```text
index.html
→ no-cache

hashed assets
→ public, max-age=31536000, immutable

config.json
→ no-store
```

CloudFront Invalidation:

```text
/index.html
/config.json
```

---

### [FAQ]

Q. CDN Cache Failure란 무엇인가?
A. CDN이 이전 파일을 계속 제공하거나 캐시 정책 때문에 새 배포가 늦게 반영되는 문제다.

Q. CloudFront invalidation은 언제 필요한가?
A. 이전 index.html이나 config.json이 계속 제공될 때 필요하다.

Q. 모든 asset을 invalidation해야 하는가?
A. hash asset 전략을 사용하면 보통 index.html과 config.json 중심으로 처리한다.

Q. CDN cache는 어디서 확인하는가?
A. Network Response Headers의 Cache-Control, Age, cache status를 확인한다.

---

## 8.3 Service Worker Cache Failure

### [개념]

Service Worker Cache Failure는 PWA 또는 service worker가 이전 정적 파일을 계속 제공해 새 배포가 반영되지 않는 문제다.

---

### [핵심]

대표 증상:

- Hard Reload 후에도 이전 화면
- offline cache가 계속 사용됨
- 새 JS bundle 요청이 발생하지 않음
- 일부 사용자만 이전 버전
- Cache Storage에 이전 asset 존재
- unregister 후 정상화

---

### [실무]

Troubleshooting Flow:

```text
Application 탭 확인
→ Service Workers 확인
→ Cache Storage 확인
→ unregister 테스트
→ Clear site data 테스트
→ service worker update 전략 확인
```

검토 기준:

```md
- [ ] service worker를 실제로 사용하는가?
- [ ] update prompt가 있는가?
- [ ] skipWaiting / clientsClaim 전략이 필요한가?
- [ ] old cache cleanup이 있는가?
- [ ] 배포 후 cache version이 갱신되는가?
```

주의:

```text
Service Worker 문제는 브라우저 cache보다 더 오래 지속될 수 있다.
```

---

### [FAQ]

Q. Service Worker Cache Failure란 무엇인가?
A. Service Worker가 이전 파일을 계속 제공해 새 배포가 반영되지 않는 문제다.

Q. Service Worker 문제는 어디서 확인하는가?
A. DevTools Application 탭의 Service Workers와 Cache Storage에서 확인한다.

Q. unregister 후 정상화되면 무엇을 의미하는가?
A. Service Worker cache가 문제였을 가능성이 높다.

Q. PWA에서 새 배포 반영을 안정화하려면 무엇이 필요한가?
A. update prompt, old cache cleanup, cache version 관리가 필요하다.

---

# 9. Environment Troubleshooting

## 9.1 Env Undefined

### [개념]

Env Undefined는 배포 후 프론트엔드 코드에서 환경 변수가 `undefined`로 평가되는 문제다.

---

### [핵심]

대표 원인:

- Vite에서 `VITE_` prefix 누락
- CRA에서 `REACT_APP_` prefix 누락
- 플랫폼 env 설정 누락
- CI env 주입 누락
- env 이름 오타
- env 변경 후 재빌드 누락
- Build-time env를 Runtime env로 착각
- Docker run environment만 설정

---

### [실무]

Troubleshooting Flow:

```text
Build Tool 확인
→ env prefix 확인
→ platform/CI env 이름 확인
→ build log 확인
→ rebuild 여부 확인
→ runtime config 사용 여부 확인
```

Vite:

```text
import.meta.env.VITE_API_BASE_URL
```

CRA:

```text
process.env.REACT_APP_API_BASE_URL
```

금지:

```text
VITE 없이 import.meta.env.API_BASE_URL 접근
REACT_APP 없이 process.env.API_BASE_URL 접근
```

---

### [FAQ]

Q. Env Undefined란 무엇인가?
A. 배포 후 환경 변수가 `undefined`로 평가되는 문제다.

Q. Vite env가 undefined인 이유는?
A. `VITE_` prefix가 없거나 build 시점 env가 주입되지 않았을 수 있다.

Q. CRA env가 undefined인 이유는?
A. `REACT_APP_` prefix가 없거나 build 시점 env가 주입되지 않았을 수 있다.

Q. env 수정 후에도 반영되지 않으면 무엇을 확인하는가?
A. 재빌드 / 재배포 여부와 Build-time env / Runtime env 차이를 확인한다.

---

## 9.2 Wrong Env After Deploy

### [개념]

Wrong Env After Deploy는 환경 변수는 존재하지만 production이 staging API를 호출하거나 preview가 production API를 호출하는 등 잘못된 값이 들어간 문제다.

---

### [핵심]

대표 원인:

```text
Production env와 Preview env 혼동
CI environment scope 오류
branch 조건 오류
local .env.production 사용
platform dashboard env 잘못 설정
Docker build-arg 잘못 전달
Runtime config cache
```

---

### [실무]

Troubleshooting Flow:

```text
Production URL 접속
→ Network API Request URL 확인
→ env source 확인
→ CI/Platform environment 확인
→ branch/deploy target 확인
→ rebuild/redeploy
```

위험 상황:

```text
Preview deploy
→ Production API 호출

Production deploy
→ Staging API 호출

Production deploy
→ localhost 호출
```

검증 기준:

```md
- [ ] Production은 production API를 호출하는가?
- [ ] Staging은 staging API를 호출하는가?
- [ ] Preview는 test/dev API를 호출하는가?
- [ ] localhost가 없는가?
```

---

### [FAQ]

Q. Wrong Env After Deploy란 무엇인가?
A. 배포 환경에 맞지 않는 API URL이나 설정값이 들어간 문제다.

Q. Production이 staging API를 호출하면 무엇이 문제인가?
A. 실제 사용자가 테스트 데이터를 보거나 기능이 실패할 수 있다.

Q. Preview가 production API를 호출하면 무엇이 문제인가?
A. 테스트 중 운영 데이터가 변경될 수 있다.

Q. 잘못된 env는 어디서 확인하는가?
A. Browser Network Request URL과 CI/Platform env 설정에서 확인한다.

---

## 9.3 Secret Exposure

### [개념]

Secret Exposure는 프론트엔드 Build 결과물이나 배포 설정에 Secret Key가 포함되어 브라우저 사용자에게 노출되는 문제다.

---

### [핵심]

노출 금지:

```text
DB_PASSWORD
JWT_SECRET
OPENAI_API_KEY
AWS_SECRET_ACCESS_KEY
TOSS_SECRET_KEY
SMTP_PASSWORD
PRIVATE_KEY
ADMIN_PASSWORD
```

노출 가능성이 있는 위치:

```text
frontend env
JS bundle
source map
build artifact
Docker image layer
CI log
platform dashboard public config
config.json
```

---

### [실무]

대응 Flow:

```text
Secret 노출 의심
→ 배포 중단
→ key 폐기
→ 새 key 발급
→ frontend env 제거
→ backend/serverless로 이동
→ commit history 확인
→ 재배포
```

검토 Flow:

```text
env 목록 확인
→ VITE_/REACT_APP_ prefix secret 확인
→ build artifact 검색
→ JS bundle 검색
→ CI log 검색
```

금지 예:

```text
VITE_OPENAI_API_KEY
REACT_APP_AWS_SECRET_ACCESS_KEY
VITE_TOSS_SECRET_KEY
```

---

### [FAQ]

Q. Secret Exposure란 무엇인가?
A. Secret Key가 프론트엔드 배포 결과물이나 로그에 포함되어 외부에 노출되는 문제다.

Q. Secret이 노출되면 어떻게 해야 하는가?
A. 즉시 폐기하고 새로 발급해야 한다.

Q. 프론트엔드 env에 Secret을 넣으면 왜 위험한가?
A. JS bundle이나 config 파일을 통해 브라우저 사용자에게 노출될 수 있기 때문이다.

Q. OpenAI API Key는 프론트엔드에 넣어도 되는가?
A. 안 된다. 백엔드나 서버리스 함수에서 사용해야 한다.

---

# 10. Deployment Mode Troubleshooting

## 10.1 Spring Boot Integrated Deployment Issues

### [개념]

Spring Boot Integrated Deployment Issues는 React Build Output을 Spring Boot static resource에 포함했을 때 발생하는 배포 문제다.

---

### [핵심]

대표 문제:

```text
Whitelabel Error
static root에 index.html 없음
build/dist 폴더 자체를 static에 넣음
Spring Boot fallback 누락
API 요청에 index.html 반환
Spring Security가 static asset 차단
JAR 재빌드 누락
이전 static file 잔존
```

---

### [실무]

Troubleshooting Flow:

```text
src/main/resources/static 확인
→ index.html 위치 확인
→ JS/CSS 폴더 확인
→ JAR build output 확인
→ / 접속
→ /login 직접 접근
→ /api/health 확인
→ Security 설정 확인
```

정상 구조:

```text
backend/src/main/resources/static/index.html
backend/src/main/resources/static/assets/
```

또는 CRA:

```text
backend/src/main/resources/static/index.html
backend/src/main/resources/static/static/js/
```

---

### [FAQ]

Q. Spring Boot 통합 배포에서 Whitelabel Error가 나오면 무엇을 확인하는가?
A. static root에 index.html이 있는지와 fallback controller가 있는지 확인한다.

Q. Spring Boot 통합 배포에서 API가 HTML을 반환하면 무엇을 확인하는가?
A. fallback mapping이 API path를 잡는지 확인한다.

Q. JS/CSS가 401 또는 403이면 무엇을 확인하는가?
A. Spring Security가 static resource를 막고 있는지 확인한다.

Q. React 수정 후 반영이 안 되면 무엇을 확인하는가?
A. React rebuild, static copy, Spring Boot JAR rebuild, browser cache를 확인한다.

---

## 10.2 Nginx Deployment Issues

### [개념]

Nginx Deployment Issues는 Nginx static hosting, SPA fallback, API reverse proxy, HTTPS, cache 설정에서 발생하는 문제다.

---

### [핵심]

대표 문제:

```text
Nginx 404
Nginx 403
502 Bad Gateway
504 Gateway Timeout
API index.html response
JS MIME type error
try_files 누락
proxy_pass slash 오류
X-Forwarded-Proto 누락
client_max_body_size 부족
```

---

### [실무]

Troubleshooting Flow:

```text
nginx -t
→ Nginx access log 확인
→ Nginx error log 확인
→ root/index.html 확인
→ /api proxy 확인
→ backend log 확인
→ HTTPS/Mixed Content 확인
```

Status별 판단:

```text
/ 404
→ root/index.html 문제

/login 404
→ try_files fallback 문제

/api 502
→ backend upstream 연결 실패

/api 404
→ proxy_pass slash / backend route 문제

JS text/html
→ asset fallback 문제
```

---

### [FAQ]

Q. Nginx 배포에서 502는 무엇을 의미하는가?
A. Nginx가 backend upstream에 연결하지 못했다는 의미다.

Q. Nginx에서 /login만 404면 무엇을 확인하는가?
A. SPA fallback `try_files` 설정을 확인한다.

Q. Nginx에서 API가 index.html을 반환하면 무엇을 확인하는가?
A. `/api` location과 fallback 우선순위를 확인해야 한다.

Q. Nginx 설정 변경 후 무엇을 해야 하는가?
A. `nginx -t`로 검증하고 reload해야 한다.

---

## 10.3 Docker Deployment Issues

### [개념]

Docker Deployment Issues는 Dockerfile, Compose, network, env, image cache, Nginx proxy에서 발생하는 문제다.

---

### [핵심]

대표 문제:

```text
Docker build failure
container crash loop
frontend port 미공개
React env에 backend service name 사용
docker run env가 React bundle에 반영되지 않음
backend DB URL localhost 사용
Nginx와 backend network 불일치
old image/container 실행
502 Bad Gateway
```

---

### [실무]

Troubleshooting Flow:

```text
docker compose ps
→ docker compose logs
→ frontend container 파일 확인
→ nginx -t 확인
→ browser request URL 확인
→ Docker network 확인
→ backend health 확인
```

명령:

```bash
docker compose ps
docker compose logs frontend
docker compose logs backend
docker compose exec frontend nginx -t
docker compose exec frontend wget -qO- http://backend:8080/api/health
```

핵심 구분:

```text
Browser URL
→ /api or public domain

Container URL
→ backend:8080
```

---

### [FAQ]

Q. Docker 배포에서 API가 안 되면 무엇을 먼저 확인하는가?
A. 브라우저 Network Request URL이 `/api`인지 `backend:8080`인지 확인한다.

Q. Docker에서 backend:8080은 누가 사용할 수 있는가?
A. 같은 Docker network 안의 컨테이너가 사용할 수 있다.

Q. 브라우저에서 backend:8080을 호출하면 왜 안 되는가?
A. 브라우저는 Docker 내부 DNS를 알 수 없기 때문이다.

Q. docker build 후 변경사항이 반영되지 않으면 무엇을 확인하는가?
A. 새 image로 container가 recreate 되었는지 확인해야 한다.

---

## 10.4 Platform Deployment Issues

### [개념]

Platform Deployment Issues는 Vercel, Netlify, Cloudflare Pages, S3/CloudFront, GitHub Pages 배포에서 발생하는 Build, Env, Routing, Cache 문제다.

---

### [핵심]

대표 문제:

```text
Root Directory 오류
Output Directory 오류
Node version mismatch
Platform env 누락
SPA fallback 누락
API rewrite 순서 오류
GitHub Pages base path 오류
CloudFront invalidation 누락
Preview가 Production API 호출
Secret frontend env 노출
```

---

### [실무]

Troubleshooting Flow:

```text
Deploy log 확인
→ Root Directory 확인
→ Build Command 확인
→ Output Directory 확인
→ Env 확인
→ Production URL Network 확인
→ Fallback/API rewrite 확인
→ Cache 확인
```

플랫폼별 핵심:

```text
Vercel
→ vercel.json rewrites / env

Netlify
→ _redirects / netlify.toml

Cloudflare Pages
→ output directory / redirects

S3 CloudFront
→ error response / cache / invalidation

GitHub Pages
→ base path / HashRouter
```

---

### [FAQ]

Q. 플랫폼 배포에서 Build 실패는 무엇을 확인하는가?
A. Deploy log, Root Directory, Node version, env, package manager를 확인한다.

Q. 플랫폼 배포에서 새로고침 404는 무엇을 확인하는가?
A. SPA fallback 또는 rewrite 설정을 확인한다.

Q. 플랫폼 배포에서 API가 HTML을 반환하면 무엇을 확인하는가?
A. API rewrite가 SPA fallback보다 먼저 적용되는지 확인한다.

Q. 플랫폼 배포에서 이전 화면이 보이면 무엇을 확인하는가?
A. CDN cache, browser cache, Service Worker, previous deploy를 확인한다.

---

# 11. Critical Issue Matrix

## 11.1 Critical Issue Classification

### [개념]

Critical Issue Classification은 배포 후 발생한 문제를 승인 불가, 승인 보류, 후속 개선 대상으로 분류하는 기준이다.

배포 장애 등급은 단순 오류 종류만으로 판단하지 않고, 사용자 영향도, 보안 영향도, 데이터 영향도, 핵심 기능 영향도를 함께 기준으로 삼는다.

---

### [핵심]

Critical:

```text
Production White Screen
JS bundle 404
API 전체 실패
API localhost 호출
API가 index.html 반환
로그인 불가
회원가입 불가
관리자 API 권한 실패
Secret 노출
HTTPS Mixed Content blocking 핵심 기능
DB/API 운영 데이터 오염 위험
결제 / 주문 / 저장 / 삭제 핵심 기능 실패
```

Major:

```text
특정 route 새로고침 404
일부 이미지 깨짐
일부 비핵심 API 500
WebSocket 실패
Preview env 오류
캐시로 일부 사용자 이전 화면
성능 심각 저하
비핵심 기능 일시 실패
```

Minor:

```text
favicon 누락
일부 console warning
비핵심 이미지 alt 누락
소규모 layout 깨짐
비핵심 analytics 실패
문구 / 스타일 일부 오류
```

API 500 등급 판단:

```text
일부 API 500
→ 비핵심 기능이면 Major
→ 로그인 / 회원가입 / 결제 / 핵심 조회 / 저장 / 수정 / 삭제 API면 Critical
```

인증 / 권한 등급 판단:

```text
로그인 전체 실패
→ Critical

일부 권한 화면 접근 실패
→ 핵심 관리자 기능이면 Critical
→ 비핵심 사용자 기능이면 Major

인증 상태 유지 실패
→ 핵심 서비스 사용 불가이면 Critical
```

Cache 등급 판단:

```text
일부 사용자 이전 화면
→ Major

대부분 사용자 이전 bundle로 White Screen
→ Critical

config.json cache로 API URL 오류
→ Critical 가능
```

---

### [실무]

승인 판단:

```text
Critical 존재
→ 배포 승인 불가 / rollback 고려

Major 존재
→ 영향 범위 확인 후 승인 보류 또는 hotfix

Minor 존재
→ 기록 후 후속 개선 가능
```

Agent 판단 Flow:

```text
문제 확인
→ 사용자 영향도 판단
→ 보안 영향도 판단
→ 데이터 영향도 판단
→ 핵심 기능 영향도 판단
→ 재현 범위 판단
→ Critical/Major/Minor 분류
```

배포 승인 기준:

```text
Critical 0개
Major 영향 범위 확인 완료
Minor 후속 처리 가능
Rollback 필요성 없음
```

Rollback 고려 기준:

```text
Critical 발생
→ 즉시 rollback 검토

Secret 노출
→ rollback + key 폐기 + 재발급

운영 데이터 오염 위험
→ rollback + backend/log/db 확인

API URL 오류
→ env 수정 + rebuild/redeploy 또는 rollback
```

---

### [FAQ]

Q. Critical Issue란 무엇인가?
A. 운영 사용자에게 핵심 장애, 보안 위험, 데이터 위험을 만드는 배포 문제다.

Q. White Screen은 Critical인가?
A. 운영 핵심 화면에서 발생하면 Critical이다.

Q. Secret 노출은 Critical인가?
A. Critical이다. 즉시 폐기와 재발급이 필요하다.

Q. 일부 API 500은 항상 Critical인가?
A. 아니다. 비핵심 API면 Major일 수 있지만 로그인, 결제, 핵심 조회, 저장 API면 Critical이다.

Q. 일부 이미지 깨짐은 Critical인가?
A. 보통 Major 또는 Minor지만 핵심 기능에 따라 달라질 수 있다.

Q. 캐시 문제는 Minor인가?
A. 단순 이전 화면이면 Major일 수 있고, 대부분 사용자에게 White Screen이나 API URL 오류를 만들면 Critical이다.

Q. 배포 승인 불가 기준은 무엇인가?
A. White Screen, JS 404, API 전체 실패, 로그인 불가, Secret 노출 같은 Critical 문제가 있으면 승인 불가다.

---

## 11.2 Error to Cause Mapping

### [개념]

Error to Cause Mapping은 화면에 보이는 오류 메시지나 증상을 가능한 원인과 연결하는 판단표다.

---

### [핵심]

매핑:

```text
White Screen
→ JS 404 / Runtime Error / Env Undefined / MIME Error

Unexpected token '<'
→ API or JS request returned HTML

Failed to load module script
→ JS Content-Type text/html / MIME Error

Refresh 404
→ SPA fallback missing

API localhost
→ Production env missing

CORS Error
→ Backend allowed origin/header/method issue

Mixed Content
→ HTTPS page calling HTTP resource

502 Bad Gateway
→ Nginx upstream backend connection failure

413 Request Entity Too Large
→ Nginx body size limit

ChunkLoadError
→ Cache mismatch / lazy chunk 404

Cookie not saved
→ SameSite / Secure / Domain / credentials issue

Redirect Loop
→ auth guard / interceptor conflict
```

---

### [실무]

Agent 사용 방식:

```text
증상 수집
→ Console message 확인
→ Network status 확인
→ Mapping 적용
→ 가장 가능성 높은 원인부터 검증
```

주의:

```text
하나의 증상이 여러 원인에서 발생할 수 있다.
Network의 Request URL, Status, Content-Type, Body를 함께 확인해야 한다.
```

---

### [FAQ]

Q. Unexpected token '<'는 무엇을 의미하는가?
A. JSON이나 JS를 기대했지만 HTML이 반환되었을 가능성이 높다.

Q. 502 Bad Gateway는 무엇을 의미하는가?
A. Nginx나 proxy가 backend upstream에 연결하지 못했다는 의미다.

Q. Cookie not saved는 무엇을 확인해야 하는가?
A. Set-Cookie, SameSite, Secure, Domain, withCredentials, CORS credentials를 확인해야 한다.

Q. ChunkLoadError는 무엇을 확인해야 하는가?
A. lazy chunk 404, cache mismatch, CDN invalidation, service worker를 확인해야 한다.

---

# 12. Verification Checklist

## 12.1 Pre-deploy Checklist

### [개념]

Pre-deploy Checklist는 배포 전에 Build, env, output, security, routing 설정이 준비되었는지 확인하는 목록이다.

---

### [핵심]

Pre-deploy:

```md
- [ ] package manager와 lock file이 일치하는가?
- [ ] clean install이 성공하는가?
- [ ] npm run build가 성공하는가?
- [ ] output directory가 맞는가?
- [ ] index.html이 output에 존재하는가?
- [ ] JS/CSS asset이 output에 존재하는가?
- [ ] production env가 설정되어 있는가?
- [ ] production API URL에 localhost가 없는가?
- [ ] frontend env에 Secret이 없는가?
- [ ] Router fallback 설정이 준비되었는가?
- [ ] API path와 frontend route가 분리되어 있는가?
- [ ] HTTPS API를 사용하는가?
- [ ] rollback 가능한 이전 버전이 있는가?
```

---

### [실무]

Pre-deploy Flow:

```text
local clean build
→ output 확인
→ env 확인
→ deploy config 확인
→ security review
→ rollback readiness 확인
```

Agent 승인 기준:

```text
Pre-deploy checklist 통과
→ deploy 진행 가능

Critical 항목 실패
→ deploy 보류
```

---

### [FAQ]

Q. Pre-deploy Checklist란 무엇인가?
A. 배포 전에 Build, env, output, routing, security 설정을 확인하는 목록이다.

Q. 배포 전 가장 중요한 env 검사는 무엇인가?
A. production API URL에 localhost가 없는지와 Secret이 frontend env에 없는지 확인하는 것이다.

Q. output directory 검증은 왜 필요한가?
A. 배포 대상 폴더가 틀리면 빈 화면이나 404가 발생할 수 있기 때문이다.

Q. rollback 준비는 배포 전에 해야 하는가?
A. 운영 배포라면 배포 전에 준비해야 한다.

---

## 12.2 Post-deploy Checklist

### [개념]

Post-deploy Checklist는 배포 직후 실제 URL에서 화면, 정적 파일, 라우팅, API, 인증, WebSocket, HTTPS, Cache가 정상 동작하는지 확인하는 목록이다.

Build 성공 또는 Deploy Success 상태만으로는 실제 사용자 환경에서 정상 동작한다고 판단할 수 없으므로, 반드시 브라우저 기준 검증을 수행한다.

---

### [핵심]

Post-deploy:

```md
- [ ] Production URL 접속 성공
- [ ] Console Critical Error 없음
- [ ] index.html 200
- [ ] JS bundle 200
- [ ] CSS bundle 200
- [ ] 이미지 / 폰트 핵심 asset 200
- [ ] JS / CSS 응답 Content-Type 정상
- [ ] React route 직접 접근 성공
- [ ] React route 새로고침 성공
- [ ] API Request URL 정상
- [ ] API Request URL에 localhost 없음
- [ ] API Request URL에 Docker service name 없음
- [ ] API 응답 Status 정상
- [ ] API 응답 Content-Type이 `application/json` 계열인가?
- [ ] API 응답 Body가 `index.html`이 아닌가?
- [ ] API 응답이 `text/html`로 반환되지 않는가?
- [ ] CORS Error 없음
- [ ] Mixed Content 없음
- [ ] 로그인 성공
- [ ] 인증 상태 유지
- [ ] Authorization Header 또는 Cookie 전송 정상
- [ ] 권한 필요한 API 정상 제어
- [ ] WebSocket 사용 시 101 연결 성공
- [ ] 이전 화면 cache 문제 없음
- [ ] Service Worker가 이전 asset을 제공하지 않음
```

---

### [실무]

Post-deploy Flow:

```text
Production URL 접속
→ DevTools open
→ Disable Cache 체크
→ Hard Reload
→ Console 첫 번째 error 확인
→ asset 요청 확인
→ route 직접 접근 확인
→ route 새로고침 확인
→ API request 확인
→ API content-type/body 확인
→ auth 확인
→ WebSocket 확인
→ cache 확인
```

Smoke Test 최소 기준:

```text
/ 접속
/login 직접 접근
/detail/1 새로고침
/api/health 호출
로그인 시도
인증 필요 API 호출
```

API 응답 검증 기준:

```text
GET /api/health
→ 200
→ Content-Type: application/json
→ Body: JSON

GET /login
→ 200
→ Content-Type: text/html
→ Body: index.html

GET /assets/index.[hash].js
→ 200
→ Content-Type: application/javascript 또는 text/javascript
→ Body: JavaScript
```

오류 판단:

```text
API 200 + text/html
→ API 요청이 SPA fallback에 잡힘

API 200 + index.html body
→ rewrite/proxy/fallback 오류

JS 200 + text/html
→ asset 요청이 SPA fallback에 잡힘

API localhost
→ production env 오류

API backend:8080
→ Docker internal URL을 browser에 노출한 오류
```

Review Agent 승인 기준:

```text
Post-deploy checklist Critical 항목 모두 통과
→ 승인 가능

API Content-Type / Body 검증 실패
→ 승인 보류

White Screen / API HTML / Login Failure
→ rollback 고려
```

---

### [FAQ]

Q. Post-deploy Checklist란 무엇인가?
A. 배포 직후 실제 URL에서 화면, asset, route, API, 인증, cache를 확인하는 목록이다.

Q. Post-deploy에서 가장 중요한 도구는 무엇인가?
A. Browser DevTools의 Console과 Network 탭이다.

Q. API 응답 JSON 확인이 왜 필요한가?
A. status 200이어도 HTML index.html이 반환될 수 있기 때문이다.

Q. API 응답 Content-Type이 text/html이면 무엇을 의미하는가?
A. API 요청이 SPA fallback이나 잘못된 rewrite에 잡혀 index.html이 반환되었을 가능성이 높다.

Q. API 응답 Body가 index.html인지 왜 확인해야 하는가?
A. status가 200이어도 실제 API가 아니라 React HTML 문서일 수 있기 때문이다.

Q. JS 응답 Content-Type도 확인해야 하는가?
A. 확인해야 한다. JS 요청에 text/html이 오면 MIME Type Error가 발생할 수 있다.

Q. Post-deploy 실패 시 어떻게 해야 하는가?
A. 문제를 Critical/Major/Minor로 분류하고 필요하면 rollback한다.

Q. API Request URL에 backend:8080이 있으면 왜 문제인가?
A. 브라우저는 Docker 내부 service name을 알 수 없으므로 실제 사용자 환경에서 실패한다.

---

## 12.3 Agent Review Checklist

### [개념]

Agent Review Checklist는 PM Agent, Frontend Agent, DevOps Agent, Review Agent가 배포 검증에서 각자 확인해야 할 책임 범위다.

---

### [핵심]

PM Agent:

```md
- [ ] 배포 목적 정의
- [ ] 배포 방식 정의
- [ ] 환경별 API URL 정의
- [ ] 검증 route 목록 정의
- [ ] rollback 기준 정의
```

Frontend Agent:

```md
- [ ] build 성공
- [ ] env prefix 준수
- [ ] localhost 하드코딩 없음
- [ ] Secret 요구 없음
- [ ] Router basename/base path 확인
- [ ] API client 정상
```

DevOps Agent:

```md
- [ ] hosting root 정상
- [ ] fallback 정상
- [ ] API proxy 정상
- [ ] HTTPS 정상
- [ ] cache 정책 정상
- [ ] logs 확인 가능
```

Review Agent:

```md
- [ ] Console / Network 검증
- [ ] asset / route / API / auth 검증
- [ ] Critical issue 분류
- [ ] 승인 / 보류 / rollback 판단
```

---

### [실무]

Agent Workflow:

```text
PM Agent
→ 검증 기준 제공

Frontend Agent
→ build/env/router/API 준비

DevOps Agent
→ 배포/hosting/proxy/cache 준비

Review Agent
→ 실제 URL 검증 및 승인 판단
```

---

### [FAQ]

Q. Agent Review Checklist란 무엇인가?
A. 배포 검증에서 각 Agent가 확인해야 할 책임 범위다.

Q. PM Agent는 무엇을 검증하는가?
A. 배포 목적, 방식, 환경, 검증 기준, rollback 기준을 정의한다.

Q. Frontend Agent는 무엇을 검증하는가?
A. build, env, router, API client, Secret 미노출을 검증한다.

Q. Review Agent는 무엇을 최종 판단하는가?
A. 실제 배포 URL 기준으로 승인, 보류, rollback 여부를 판단한다.

---

# 13. Agent Decision Rules

## 13.1 PM Agent Rules

### [개념]

PM Agent는 배포 검증 범위, 장애 기준, rollback 기준, 사용자 영향도를 정의해야 한다.

---

### [핵심]

PM Agent 확인 항목:

- 배포 대상 환경
- 배포 방식
- 핵심 사용자 시나리오
- 검증 route 목록
- 검증 API 목록
- 인증 시나리오
- Critical Issue 기준
- rollback 기준
- 담당 Agent 배정
- 배포 승인 조건

---

### [실무]

PM Agent 산출물 예:

```text
Deploy Target: Production
Deploy Type: Nginx + Docker Compose
Critical Routes:
- /
- /login
- /mypage
- /detail/1

Critical APIs:
- /api/health
- /api/auth/login
- /api/users/me

Critical Criteria:
- White Screen 없음
- API localhost 없음
- API HTML response 없음
- Login 성공
- Refresh 404 없음

Rollback:
- Critical issue 발생 시 이전 image tag로 rollback
```

PM Agent 판단 Flow:

```text
배포 목적 확인
→ 핵심 기능 정의
→ 검증 목록 작성
→ Critical 기준 정의
→ rollback 기준 정의
→ Review Agent에 전달
```

---

### [FAQ]

Q. PM Agent는 배포 검증에서 무엇을 정해야 하는가?
A. 핵심 route, API, 인증 시나리오, Critical 기준, rollback 기준을 정해야 한다.

Q. PM Agent가 rollback 기준을 정해야 하는 이유는?
A. 장애 발생 시 지연 없이 이전 정상 버전으로 복구하기 위해 필요하다.

Q. PM Agent가 사용자 영향도를 판단해야 하는가?
A. 그렇다. Critical/Major/Minor 분류에 필요하다.

Q. PM Agent의 최종 산출물은 무엇인가?
A. 검증 범위와 승인 기준이다.

---

## 13.2 Frontend Agent Rules

### [개념]

Frontend Agent는 배포 후 발생한 화면, route, env, API client, auth state 문제를 분석하고 수정해야 한다.

---

### [핵심]

Frontend Agent 확인 항목:

- build output 정상 여부
- env access 정상 여부
- API client baseURL
- Authorization Header
- Cookie credentials 설정
- Router basename
- Protected Route guard
- lazy chunk loading
- runtime error
- error boundary
- fallback UI
- console error source

---

### [실무]

Frontend Agent 판단 Flow:

```text
Console error 확인
→ source 위치 확인
→ env 값 확인
→ API client 확인
→ Router 설정 확인
→ auth flow 확인
→ 수정 후 build
```

Frontend Agent 수정 대상:

```text
env validation
API client baseURL
interceptor
Protected Route loading
Router basename
lazy import path
fallback UI
error boundary
```

---

### [FAQ]

Q. Frontend Agent는 배포 장애에서 무엇을 확인해야 하는가?
A. runtime error, env, API client, router, auth state, lazy chunk를 확인해야 한다.

Q. API localhost 문제는 Frontend Agent도 확인해야 하는가?
A. 그렇다. API client와 env 설정을 확인해야 한다.

Q. Redirect Loop는 Frontend Agent 문제인가?
A. route guard, auth loading, interceptor 문제일 수 있으므로 Frontend Agent가 확인해야 한다.

Q. lazy chunk 404는 Frontend Agent만의 문제인가?
A. 아니다. build output, cache, hosting 문제와 함께 봐야 한다.

---

## 13.3 DevOps Agent Rules

### [개념]

DevOps Agent는 배포 서버, hosting root, proxy, fallback, TLS, cache, logs, CI/CD 환경 문제를 분석하고 수정해야 한다.

---

### [핵심]

DevOps Agent 확인 항목:

- hosting root
- output directory
- Nginx config
- Spring Boot static resource
- platform build setting
- API proxy
- SPA fallback
- WebSocket proxy
- TLS certificate
- X-Forwarded headers
- cache headers
- CDN invalidation
- Docker network
- container logs
- CI/CD deploy logs

---

### [실무]

DevOps Agent 판단 Flow:

```text
Deploy log 확인
→ server/container status 확인
→ static file 위치 확인
→ proxy/fallback 확인
→ HTTPS 확인
→ cache 확인
→ logs 확인
```

DevOps Agent 수정 대상:

```text
Nginx root
try_files
proxy_pass
CloudFront error response
Netlify redirects
Vercel rewrites
Docker compose network
CI/CD artifact path
Cache-Control
```

---

### [FAQ]

Q. DevOps Agent는 배포 장애에서 무엇을 확인해야 하는가?
A. hosting, proxy, fallback, HTTPS, cache, Docker, CI/CD log를 확인해야 한다.

Q. API가 index.html을 반환하면 DevOps Agent가 확인할 것은?
A. fallback/rewrite/proxy 우선순위를 확인해야 한다.

Q. 502 Bad Gateway는 DevOps Agent 문제인가?
A. 대부분 proxy upstream, backend 상태, network 문제이므로 DevOps Agent가 확인해야 한다.

Q. 이전 화면이 계속 보이면 DevOps Agent가 무엇을 확인하는가?
A. cache header, CDN invalidation, container image, artifact 배포 상태를 확인한다.

---

## 13.4 Review Agent Rules

### [개념]

Review Agent는 실제 배포 URL 기준으로 장애를 재현하고 원인을 분류하며 승인, 보류, rollback을 판단하는 Agent다.

---

### [핵심]

Review Agent 필수 기준:

- 실제 Production URL에서 검증
- Console 첫 번째 error 확인
- Network request URL 확인
- asset status 확인
- API content-type 확인
- auth flow 확인
- route refresh 확인
- HTTPS / Mixed Content 확인
- cache 상태 확인
- Critical issue classification
- 승인 / 보류 / rollback 판단

---

### [실무]

Review Agent 판단 Flow:

```text
Production URL 접속
→ Console 확인
→ Network 확인
→ 문제 재현
→ 원인 후보 분류
→ 담당 Agent 지정
→ Critical/Major/Minor 분류
→ 승인/보류/rollback 판단
```

승인 기준:

```text
No White Screen
No Critical Console Error
No JS/CSS 404
No API localhost
No API HTML response
No Refresh 404
No Login Critical Failure
No Secret Exposure
No Mixed Content Blocking
```

---

### [FAQ]

Q. Review Agent는 배포 검증에서 무엇을 가장 먼저 확인해야 하는가?
A. 실제 배포 URL의 Console과 Network를 먼저 확인해야 한다.

Q. Review Agent는 무엇을 기준으로 승인하는가?
A. White Screen, asset, route, API, auth, HTTPS, secret, cache의 Critical 문제가 없는지 기준으로 승인한다.

Q. Review Agent가 rollback을 판단할 수 있는가?
A. Critical issue가 운영에 영향을 주면 rollback을 권고해야 한다.

Q. Review Agent는 문제를 직접 수정하는가?
A. 보통 원인 분류와 담당 Agent 지정, 승인 판단을 수행한다.

---

# 14. Common Mistakes

## 14.1 Deployment Verification Common Mistakes

### [개념]

Deployment Verification Common Mistakes는 배포 성공 표시만 보고 실제 사용자 환경 검증을 생략할 때 반복적으로 발생하는 실수다.

---

### [핵심]

자주 발생하는 실수:

- Build 성공만 보고 배포 완료로 판단
- 플랫폼 Deploy Success만 보고 실제 URL 미확인
- Console Error 미확인
- Network Request URL 미확인
- API status만 보고 body/content-type 미확인
- API 200 HTML response를 정상으로 착각
- 새로고침 / 직접 URL 접근 미검증
- 로그인 / 인증 상태 유지 미검증
- 권한 API 미검증
- 운영 API URL localhost 확인 누락
- CORS와 Mixed Content를 같은 문제로 착각
- Cookie와 Authorization Header 인증 방식 혼동
- Cache 문제를 코드 문제로 오해
- Service Worker 확인 누락
- WebSocket Network 탭 미확인
- backend log 없이 500 원인 추측
- Nginx/Platform fallback이 API를 잡는지 확인 안 함
- rollback 기준 없이 production 배포

---

### [실무]

실수별 판단:

```text
Deploy success but blank page
→ 실제 URL 검증 누락

API status 200 but error
→ response body/content-type 미확인

Local works but production fails
→ env/CORS/HTTPS/fallback/cache 차이

Login success but session lost
→ cookie/token persistence 미확인

New deploy but old screen
→ cache/service worker/invalidation 미확인
```

---

### [FAQ]

Q. 배포 검증에서 가장 흔한 실수는 무엇인가?
A. Build 성공이나 Deploy Success만 보고 실제 브라우저 검증을 하지 않는 것이다.

Q. API status 200이면 body를 안 봐도 되는가?
A. 아니다. index.html이 반환될 수도 있으므로 content-type과 body를 확인해야 한다.

Q. 로컬에서 되면 운영에서도 된다고 봐도 되는가?
A. 아니다. 운영은 env, HTTPS, CORS, fallback, cache 조건이 다르다.

Q. 배포 검증에서 rollback 기준이 필요한 이유는?
A. Critical 장애 발생 시 빠르게 복구하기 위해 필요하다.

---

# 15. Part12 Quality Checklist

## 15.1 Document Quality

### [개념]

이 문서는 Frontend Build & Deploy Domain의 Part12이며 Deployment Verification & Troubleshooting Retrieval에 최적화되어야 한다.

---

### [핵심]

문서 품질 기준:

- Deployment Verification 정의 포함
- Verification Priority 포함
- Console Verification 포함
- Network Verification 포함
- Application Tab Verification 포함
- White Screen Troubleshooting 포함
- JS/CSS 404 포함
- MIME Type Error 포함
- ChunkLoadError 포함
- Refresh 404 포함
- API Returns index.html 포함
- Sub Path Routing Failure 포함
- API URL Failure 포함
- CORS Failure 포함
- Mixed Content Failure 포함
- Backend 500 Failure 포함
- Login Failure 포함
- Authorization Header Failure 포함
- Cookie Failure 포함
- Redirect Loop 포함
- WebSocket / STOMP / SockJS Troubleshooting 포함
- Cache / CDN / Service Worker Troubleshooting 포함
- Env Undefined / Wrong Env / Secret Exposure 포함
- Spring Boot / Nginx / Docker / Platform 배포 문제 포함
- Critical Issue Matrix 포함
- Pre-deploy / Post-deploy Checklist 포함
- Agent별 판단 기준 포함
- Common Mistakes 포함
- Retrieval Queries 포함

---

### [실무]

Part12는 Frontend Build & Deploy Domain의 마지막 검증 문서다.

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

이 문서는 전체 Part의 최종 Review 기준으로 사용한다.

---

### [FAQ]

Q. Part12의 핵심 목적은 무엇인가?
A. 프론트엔드 배포 후 실제 장애를 Console, Network, API, Auth, Cache 기준으로 진단하고 승인/보류/rollback을 판단하게 하는 것이다.

Q. Part12는 개발 방법 문서인가?
A. 아니다. 배포 검증과 장애 원인 분류에 집중하는 Review / Troubleshooting 문서다.

Q. Part12 이후에는 무엇을 해야 하는가?
A. Frontend Build & Deploy Domain 전체를 Project Progress에 Completed로 반영하고, Frontend Code Review 또는 Styling Architecture 문서로 이어질 수 있다.

---

# Retrieval Queries

### [FAQ]

Q. Deployment Verification이란 무엇인가?
A. 배포 후 실제 URL에서 화면, asset, route, API, 인증, HTTPS, cache가 정상인지 확인하는 절차다.

Q. Build 성공이면 배포 성공인가?
A. 아니다. 실제 브라우저에서 정적 파일, API, 라우팅이 정상인지 확인해야 한다.

Q. 배포 검증에서 가장 먼저 확인할 것은 무엇인가?
A. Production URL의 Console Error와 Network 요청 상태를 먼저 확인한다.

Q. 배포 검증 우선순위는 어떻게 잡는가?
A. 화면 진입, JS/CSS 로드, Console Error, 라우팅, API, 인증, HTTPS, 캐시 순서로 확인한다.

Q. 가장 치명적인 프론트엔드 배포 장애는 무엇인가?
A. White Screen, JS bundle 404, API 전체 실패, API localhost 호출이다.

Q. Console Verification이란 무엇인가?
A. 브라우저 Console에서 runtime error, CORS, Mixed Content, MIME type 문제를 확인하는 절차다.

Q. Console에서 가장 먼저 봐야 하는 것은?
A. 첫 번째 실제 error를 우선 확인해야 한다.

Q. Unexpected token '<'는 무엇을 의미하는가?
A. JSON이나 JS를 기대했지만 HTML이 응답되어 파싱에 실패한 경우가 많다.

Q. Network Verification이란 무엇인가?
A. 브라우저가 실제 요청한 URL, status, header, body를 확인하는 절차다.

Q. API status 200이면 무조건 정상인가?
A. 아니다. response body와 content-type이 JSON인지 확인해야 한다.

Q. API 응답이 text/html이면 무엇을 의심해야 하는가?
A. SPA fallback이 API 요청을 index.html로 반환했을 가능성이 높다.

Q. JS 요청이 text/html이면 무엇을 의심해야 하는가?
A. asset path 오류 또는 fallback이 JS 요청을 index.html로 반환한 문제를 의심해야 한다.

Q. Application 탭에서는 무엇을 확인하는가?
A. token, cookie, service worker, cache storage 같은 브라우저 저장 상태를 확인한다.

Q. 로그인 후 쿠키가 저장되지 않으면 어디를 보는가?
A. Network Set-Cookie와 Application Cookies를 함께 확인한다.

Q. 배포 후 이전 화면이 계속 보이면 무엇을 확인하는가?
A. Service Worker와 Cache Storage를 확인해야 한다.

Q. White Screen이란 무엇인가?
A. 배포 후 React 앱이 렌더링되지 않고 빈 화면만 표시되는 문제다.

Q. White Screen이면 무엇을 먼저 확인하는가?
A. Console 첫 번째 error와 Network의 JS bundle 로드 상태를 확인한다.

Q. JS bundle 404는 무엇을 확인해야 하는가?
A. Build Output, hosting root, base path, output directory를 확인해야 한다.

Q. JS CSS 404란 무엇인가?
A. 브라우저가 React 실행에 필요한 JS 또는 CSS 파일을 찾지 못하는 문제다.

Q. JS 404가 발생하면 무엇을 확인해야 하는가?
A. index.html이 참조하는 script 경로와 실제 배포된 파일 위치를 비교해야 한다.

Q. MIME Type Error란 무엇인가?
A. JS/CSS 요청에 잘못된 Content-Type이 반환되어 브라우저가 실행을 거부하는 문제다.

Q. JS 요청에 text/html이 오면 무엇을 의미하는가?
A. JS 파일 대신 index.html이 반환되었을 가능성이 높다.

Q. ChunkLoadError란 무엇인가?
A. lazy loading chunk 파일을 브라우저가 로드하지 못할 때 발생하는 오류다.

Q. ChunkLoadError의 대표 원인은 무엇인가?
A. cache mismatch, chunk 404, 배포 artifact mismatch가 대표 원인이다.

Q. Refresh 404란 무엇인가?
A. React route에서 새로고침하거나 직접 URL 접근 시 서버가 404를 반환하는 문제다.

Q. 클릭 이동은 되는데 새로고침이 안 되는 이유는?
A. 클릭 이동은 React Router가 처리하지만 새로고침은 서버가 먼저 URL을 처리하기 때문이다.

Q. API Returns index.html이란 무엇인가?
A. API 요청에 JSON이 아니라 React index.html이 반환되는 문제다.

Q. API 요청에 index.html이 오면 무엇을 확인해야 하는가?
A. fallback, rewrite, proxy, API prefix 설정을 확인해야 한다.

Q. status 200인데 API가 실패할 수 있는가?
A. 가능하다. 200이어도 body가 HTML이면 JSON 파싱이 실패한다.

Q. Sub Path Routing Failure란 무엇인가?
A. 앱을 하위 경로에 배포했을 때 asset, route, fallback 경로가 맞지 않아 발생하는 문제다.

Q. 하위 경로 배포에서 Vite base는 무엇을 담당하는가?
A. JS/CSS asset이 로드될 기준 경로를 담당한다.

Q. 하위 경로 배포에서 Router basename은 무엇을 담당하는가?
A. React Router가 route를 해석하는 기준 경로를 담당한다.

Q. API URL Failure란 무엇인가?
A. 프론트엔드가 잘못된 API 주소로 요청을 보내 API 호출에 실패하는 문제다.

Q. 운영에서 API URL이 localhost면 왜 문제인가?
A. 사용자 브라우저의 localhost로 요청하기 때문에 실제 백엔드에 도달하지 못한다.

Q. API URL이 backend:8080이면 왜 문제인가?
A. 브라우저는 Docker 내부 service name을 알 수 없기 때문이다.

Q. CORS Failure란 무엇인가?
A. 브라우저가 다른 Origin API 요청을 백엔드 허용 정책 때문에 차단하는 문제다.

Q. CORS는 프론트엔드에서 해결하는가?
A. 대부분 백엔드에서 allowed origin, method, header를 설정해야 해결된다.

Q. Authorization Header가 있으면 CORS에 영향이 있는가?
A. 있다. allowed headers에 Authorization이 포함되어야 할 수 있다.

Q. Mixed Content Failure란 무엇인가?
A. HTTPS 페이지에서 HTTP 리소스를 호출해 브라우저가 차단하는 문제다.

Q. HTTPS 페이지에서 HTTP API를 호출해도 되는가?
A. 안 된다. Mixed Content로 차단될 수 있다.

Q. Backend 500 Failure란 무엇인가?
A. API 요청이 백엔드에 도달했지만 백엔드 내부 오류로 실패한 상태다.

Q. 500 에러는 프론트엔드 문제인가?
A. 대부분 백엔드 문제지만 잘못된 payload나 header가 원인일 수도 있다.

Q. Login Failure란 무엇인가?
A. 로그인 요청, token 저장, cookie 저장, 인증 상태 복원 중 하나가 실패하는 문제다.

Q. Cookie 인증에서 로그인 유지가 안 되면 무엇을 확인하는가?
A. Set-Cookie, withCredentials, SameSite, Secure, Domain, CORS credentials를 확인한다.

Q. JWT 인증에서 로그인 유지가 안 되면 무엇을 확인하는가?
A. accessToken 저장 위치와 Authorization Header 전송 여부를 확인한다.

Q. Authorization Header Failure란 무엇인가?
A. 인증 token이 API 요청 Header에 포함되지 않거나 형식이 잘못되어 인증에 실패하는 문제다.

Q. token은 있는데 API가 401이면 무엇을 확인하는가?
A. Request Header에 Authorization이 실제로 포함되는지 확인해야 한다.

Q. Cookie Failure란 무엇인가?
A. 쿠키가 저장되지 않거나 이후 요청에 포함되지 않아 인증이 실패하는 문제다.

Q. Set-Cookie가 있는데 쿠키가 저장되지 않는 이유는?
A. SameSite, Secure, Domain, CORS credentials, HTTPS 조건이 맞지 않을 수 있다.

Q. Redirect Loop란 무엇인가?
A. 인증 또는 권한 로직이 반복 redirect를 발생시켜 페이지에 접근하지 못하는 문제다.

Q. 로그인 페이지로 계속 튕기면 무엇을 확인하는가?
A. auth loading, token restore, route guard, 401 interceptor를 확인한다.

Q. WebSocket Connection Failure란 무엇인가?
A. 배포 환경에서 WebSocket 연결이 열리지 않거나 연결 직후 끊기는 문제다.

Q. WebSocket 정상 연결 status는 무엇인가?
A. 일반적으로 101 Switching Protocols가 정상이다.

Q. STOMP SockJS Failure란 무엇인가?
A. STOMP/SockJS 연결에서 endpoint, proxy, CORS, destination 설정이 맞지 않아 실패하는 문제다.

Q. SockJS를 쓰면 Nginx에서 무엇을 주의해야 하는가?
A. `/ws/**` 하위 요청 전체를 백엔드로 proxy해야 한다.

Q. Old Version Displayed란 무엇인가?
A. 새로 배포했는데 이전 화면이나 이전 JavaScript가 계속 표시되는 문제다.

Q. 이전 화면이 보이면 무엇을 먼저 확인하는가?
A. Browser cache, CDN cache, Service Worker, 실제 배포 artifact를 확인한다.

Q. CDN Cache Failure란 무엇인가?
A. CDN이 이전 파일을 계속 제공하거나 캐시 정책 때문에 새 배포가 늦게 반영되는 문제다.

Q. Service Worker Cache Failure란 무엇인가?
A. Service Worker가 이전 파일을 계속 제공해 새 배포가 반영되지 않는 문제다.

Q. Env Undefined란 무엇인가?
A. 배포 후 환경 변수가 `undefined`로 평가되는 문제다.

Q. Vite env가 undefined인 이유는?
A. `VITE_` prefix가 없거나 build 시점 env가 주입되지 않았을 수 있다.

Q. CRA env가 undefined인 이유는?
A. `REACT_APP_` prefix가 없거나 build 시점 env가 주입되지 않았을 수 있다.

Q. Wrong Env After Deploy란 무엇인가?
A. 배포 환경에 맞지 않는 API URL이나 설정값이 들어간 문제다.

Q. Preview가 production API를 호출하면 무엇이 문제인가?
A. 테스트 중 운영 데이터가 변경될 수 있다.

Q. Secret Exposure란 무엇인가?
A. Secret Key가 프론트엔드 배포 결과물이나 로그에 포함되어 외부에 노출되는 문제다.

Q. Secret이 노출되면 어떻게 해야 하는가?
A. 즉시 폐기하고 새로 발급해야 한다.

Q. Spring Boot 통합 배포에서 Whitelabel Error가 나오면 무엇을 확인하는가?
A. static root에 index.html이 있는지와 fallback controller가 있는지 확인한다.

Q. Nginx 배포에서 502는 무엇을 의미하는가?
A. Nginx가 backend upstream에 연결하지 못했다는 의미다.

Q. Docker 배포에서 API가 안 되면 무엇을 먼저 확인하는가?
A. 브라우저 Network Request URL이 `/api`인지 `backend:8080`인지 확인한다.

Q. 플랫폼 배포에서 Build 실패는 무엇을 확인하는가?
A. Deploy log, Root Directory, Node version, env, package manager를 확인한다.

Q. Critical Issue란 무엇인가?
A. 운영 사용자에게 핵심 장애, 보안 위험, 데이터 위험을 만드는 배포 문제다.

Q. White Screen은 Critical인가?
A. 운영 핵심 화면에서 발생하면 Critical이다.

Q. Secret 노출은 Critical인가?
A. Critical이다. 즉시 폐기와 재발급이 필요하다.

Q. Pre-deploy Checklist란 무엇인가?
A. 배포 전에 Build, env, output, routing, security 설정을 확인하는 목록이다.

Q. Post-deploy Checklist란 무엇인가?
A. 배포 직후 실제 URL에서 화면, asset, route, API, 인증, cache를 확인하는 목록이다.

Q. PM Agent는 배포 검증에서 무엇을 정해야 하는가?
A. 핵심 route, API, 인증 시나리오, Critical 기준, rollback 기준을 정해야 한다.

Q. Frontend Agent는 배포 장애에서 무엇을 확인해야 하는가?
A. runtime error, env, API client, router, auth state, lazy chunk를 확인해야 한다.

Q. DevOps Agent는 배포 장애에서 무엇을 확인해야 하는가?
A. hosting, proxy, fallback, HTTPS, cache, Docker, CI/CD log를 확인해야 한다.

Q. Review Agent는 배포 검증에서 무엇을 가장 먼저 확인해야 하는가?
A. 실제 배포 URL의 Console과 Network를 먼저 확인해야 한다.

Q. 배포 검증에서 가장 흔한 실수는 무엇인가?
A. Build 성공이나 Deploy Success만 보고 실제 브라우저 검증을 하지 않는 것이다.

Q. Part12 이후에는 무엇을 해야 하는가?
A. Frontend Build & Deploy Domain 전체를 Project Progress에 Completed로 반영하고 다음 Frontend Domain 문서로 이어갈 수 있다.
