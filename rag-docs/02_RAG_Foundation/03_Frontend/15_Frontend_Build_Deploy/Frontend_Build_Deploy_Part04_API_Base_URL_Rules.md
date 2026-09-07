# Frontend Build & Deploy Part04 - API Base URL Rules

---

# 1. API Base URL Core

## 1.1 API Base URL Definition

### [개념]

API Base URL은 프론트엔드가 백엔드 API를 호출할 때 사용하는 기본 주소다.

대표 형태:

```text
http://localhost:8080
https://api.example.com
/api
https://example.com/api
```

API Request 조합 예:

```text
baseURL: https://api.example.com
path: /festivals
result: https://api.example.com/festivals
```

---

### [핵심]

API Base URL 핵심 규칙:

- 환경별로 분리해야 한다.
- 코드에 직접 하드코딩하지 않는다.
- 운영 Build에 `localhost`가 남으면 안 된다.
- HTTPS 프론트엔드에서는 HTTPS API를 사용해야 한다.
- Same Origin Proxy 구조에서는 `/api`를 사용할 수 있다.
- baseURL과 요청 path의 `/api` 중복을 피해야 한다.
- CORS / Cookie / Authorization 방식과 함께 검토해야 한다.
- 배포 후 Network 탭에서 실제 Request URL을 확인해야 한다.

---

### [실무]

2026 실무 기준으로 API Base URL은 배포 장애의 핵심 점검 대상이다.

환경별 예:

```text
Local
→ http://localhost:8080

Development
→ https://dev-api.example.com

Staging
→ https://staging-api.example.com

Production
→ https://api.example.com

Same Origin Proxy
→ /api
```

Agent 판단 Flow:

```text
Build Tool 확인
→ Env Prefix 확인
→ API Base URL 값 확인
→ localhost 여부 확인
→ HTTP/HTTPS 확인
→ Proxy 구조 확인
→ Request Path 중복 확인
→ Network Request URL 확인
```

---

### [FAQ]

Q. API Base URL은 무엇인가?
A. 프론트엔드가 백엔드 API를 호출할 때 사용하는 기본 주소다.

Q. API Base URL은 왜 환경 변수로 분리하는가?
A. 로컬, 개발, 스테이징, 운영 환경의 백엔드 주소가 다르기 때문이다.

Q. 운영 API Base URL에 localhost를 사용해도 되는가?
A. 안 된다. 사용자 브라우저 기준 localhost는 사용자 자신의 PC를 의미한다.

Q. API Base URL은 어디서 최종 확인하는가?
A. 브라우저 개발자 도구 Network 탭의 실제 Request URL에서 확인한다.

---

## 1.2 API URL Composition

### [개념]

API URL Composition은 `baseURL`과 개별 API path가 결합되어 최종 Request URL을 만드는 방식이다.

---

### [핵심]

구성 요소:

```text
Protocol
→ http / https

Host
→ localhost / domain / IP

Port
→ 8080 / 3000 / 443

Base Path
→ /api

Endpoint Path
→ /users /festivals /auth/login
```

올바른 조합 예:

```text
baseURL = https://api.example.com
path = /festivals
result = https://api.example.com/festivals
```

```text
baseURL = /api
path = /festivals
result = /api/festivals
```

잘못된 조합 예:

```text
baseURL = https://api.example.com/api
path = /api/festivals
result = https://api.example.com/api/api/festivals
```

---

### [실무]

2026 실무 기준으로 `baseURL`과 path 규칙은 팀에서 하나로 통일해야 한다.

권장 패턴 1:

```js
const api = axios.create({
  baseURL: "/api",
});

api.get("/festivals");
```

결과:

```text
/api/festivals
```

권장 패턴 2:

```js
const api = axios.create({
  baseURL: "https://api.example.com",
});

api.get("/api/festivals");
```

결과:

```text
https://api.example.com/api/festivals
```

비권장:

```text
baseURL에도 /api
endpoint에도 /api
```

Agent 검토 기준:

```text
baseURL 확인
→ API client path 확인
→ /api prefix 위치 확인
→ 중복 /api 여부 확인
→ Network Request URL 확인
```

---

### [FAQ]

Q. API URL에 /api가 두 번 붙는 이유는?
A. baseURL과 개별 endpoint path 양쪽에 `/api`가 중복되었기 때문이다.

Q. baseURL에 /api를 넣는 것이 좋은가?
A. 팀 규칙에 따라 가능하다. 단, endpoint path에는 다시 `/api`를 붙이지 않아야 한다.

Q. endpoint path에 /api를 넣는 것이 좋은가?
A. 가능하다. 단, baseURL에는 `/api`를 중복해서 넣지 않아야 한다.

Q. 최종 API URL은 어디서 확인하는가?
A. Network 탭의 Request URL에서 확인한다.

---

# 2. Environment-based API URL

## 2.1 Local API URL

### [개념]

Local API URL은 개발자 PC에서 실행 중인 백엔드 서버를 호출하기 위한 주소다.

대표 예:

```text
http://localhost:8080
http://127.0.0.1:8080
```

---

### [핵심]

Local API URL 특징:

- 로컬 개발 전용이다.
- 운영 Build에 포함되면 안 된다.
- 포트는 백엔드 서버 설정에 따라 다르다.
- 프론트엔드 개발 서버와 백엔드 포트가 다르면 CORS 또는 dev proxy가 필요할 수 있다.
- Docker 환경에서는 브라우저 기준 localhost와 컨테이너 기준 localhost를 구분해야 한다.

---

### [실무]

Local `.env` 예:

Vite:

```env
VITE_API_BASE_URL=http://localhost:8080
```

CRA:

```env
REACT_APP_API_BASE_URL=http://localhost:8080
```

Local 개발 Flow:

```text
Frontend Dev Server
→ http://localhost:3000 or 5173

Backend Server
→ http://localhost:8080

Browser Request
→ http://localhost:8080/api/...
```

주의:

```text
Localhost in local development
→ 정상 가능

Localhost in production
→ 장애 가능성 높음
```

---

### [FAQ]

Q. 로컬 개발에서는 localhost API를 사용해도 되는가?
A. 가능하다. 단, 운영 Build에는 localhost가 남지 않아야 한다.

Q. 프론트엔드와 백엔드 포트가 다르면 문제인가?
A. 다른 Origin이므로 CORS 또는 dev proxy 설정이 필요할 수 있다.

Q. localhost와 127.0.0.1은 같은가?
A. 대부분 로컬 머신을 가리키지만 브라우저, 쿠키, CORS 관점에서는 Origin이 달라질 수 있어 통일하는 것이 좋다.

Q. 운영에서 localhost API가 실패하는 이유는?
A. 사용자 브라우저의 localhost로 요청하기 때문에 실제 백엔드 서버에 도달하지 못한다.

---

## 2.2 Production API URL

### [개념]

Production API URL은 실제 사용자에게 배포된 프론트엔드가 호출하는 운영 백엔드 API 주소다.

대표 예:

```text
https://api.example.com
https://example.com/api
/api
```

---

### [핵심]

Production API URL 기준:

- HTTPS 사용 권장
- 운영 백엔드 도메인 사용
- `localhost` 금지
- Mixed Content 금지
- CORS 허용 Origin 확인
- Cookie 인증 시 SameSite / Secure / Domain 확인
- Authorization Header 인증 시 token 전송 확인
- 배포 후 Network Request URL 검증

---

### [실무]

Production `.env` 예:

Vite:

```env
VITE_API_BASE_URL=https://api.example.com
```

CRA:

```env
REACT_APP_API_BASE_URL=https://api.example.com
```

Same Origin Proxy 예:

```env
VITE_API_BASE_URL=/api
```

Production 검증 Flow:

```text
Production URL 접속
→ Network 탭 열기
→ API Request URL 확인
→ status code 확인
→ CORS error 확인
→ Authorization / Cookie 확인
→ Response Body 확인
```

---

### [FAQ]

Q. 운영 API URL은 어떤 형태가 좋은가?
A. `https://api.example.com` 또는 같은 도메인 proxy 구조의 `/api`가 일반적이다.

Q. 운영 API URL에 HTTP를 써도 되는가?
A. HTTPS 프론트엔드에서는 HTTP API가 Mixed Content로 차단될 수 있으므로 HTTPS를 사용해야 한다.

Q. 운영에서 baseURL을 /api로 써도 되는가?
A. 가능하다. 단, Nginx나 서버가 `/api` 요청을 백엔드로 proxy해야 한다.

Q. 운영 API URL 설정 후 무엇을 확인해야 하는가?
A. Network 탭에서 실제 Request URL과 status code를 확인해야 한다.

---

## 2.3 Staging API URL

### [개념]

Staging API URL은 운영 배포 전 검증 환경에서 사용하는 백엔드 API 주소다.

대표 예:

```text
https://staging-api.example.com
https://staging.example.com/api
```

---

### [핵심]

Staging API URL 목적:

- 운영 전 최종 검증
- 운영 데이터 보호
- 배포 파이프라인 테스트
- CORS / Cookie / HTTPS 설정 검증
- 실제 도메인 기반 통합 테스트
- 운영과 유사한 환경에서 QA 수행

---

### [실무]

Vite staging 예:

```env
VITE_API_BASE_URL=https://staging-api.example.com
VITE_APP_ENV=staging
```

Build script 예:

```json
{
  "scripts": {
    "build:staging": "vite build --mode staging",
    "build:prod": "vite build --mode production"
  }
}
```

검증 기준:

```md
- [ ] staging 화면이 staging API를 호출하는가?
- [ ] staging에서 production API를 호출하지 않는가?
- [ ] staging CORS origin이 허용되어 있는가?
- [ ] staging Cookie Domain이 올바른가?
- [ ] test data와 production data가 분리되어 있는가?
```

---

### [FAQ]

Q. Staging API URL은 왜 필요한가?
A. 운영 전 실제 배포와 유사한 환경에서 API 연동을 검증하기 위해 필요하다.

Q. staging 화면이 production API를 호출하면 안 되는가?
A. 안 된다. 테스트 중 운영 데이터가 변경될 수 있다.

Q. staging env는 어떻게 분리하는가?
A. Vite에서는 `.env.staging`과 `vite build --mode staging`을 사용할 수 있다.

Q. staging에서도 CORS를 확인해야 하는가?
A. 해야 한다. staging 도메인도 백엔드 CORS 허용 목록에 포함되어야 한다.

---

# 3. Same Origin Proxy

## 3.1 Same Origin Proxy Concept

### [개념]

Same Origin Proxy는 프론트엔드와 백엔드를 같은 Origin처럼 보이게 하고 `/api` 요청을 백엔드로 전달하는 구조다.

예:

```text
Browser
→ https://example.com/api/festivals

Nginx or Server
→ http://backend:8080/api/festivals
```

---

### [핵심]

Same Origin Proxy 장점:

- CORS 복잡도 감소
- 프론트엔드 baseURL을 `/api`로 단순화 가능
- 운영 도메인 하나로 관리 가능
- Cookie 인증 설정이 단순해질 수 있음
- Nginx / Spring Boot / API Gateway와 잘 맞음

주의:

- `/api` proxy 설정이 실제로 존재해야 한다.
- SPA fallback이 `/api`를 index.html로 보내면 안 된다.
- proxy path slash 처리에 주의해야 한다.
- WebSocket은 별도 upgrade header가 필요할 수 있다.
- 백엔드 API prefix와 일치해야 한다.

---

### [실무]

Frontend env:

```env
VITE_API_BASE_URL=/api
```

Axios:

```js
export const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
});
```

Request Flow:

```text
Browser Request /api/festivals
→ Nginx receives /api/festivals
→ Nginx proxy_pass backend
→ Backend handles /api/festivals
→ Response returns through Nginx
```

Agent 검토 기준:

```text
baseURL이 /api
→ 운영 proxy 존재 확인
→ /api location 우선순위 확인
→ SPA fallback 제외 확인
→ Network에서 index.html 반환 여부 확인
```

---

### [FAQ]

Q. baseURL을 /api로 쓰는 구조는 무엇인가?
A. 같은 도메인에서 `/api` 요청을 백엔드로 proxy하는 Same Origin Proxy 구조다.

Q. /api를 쓰면 CORS가 필요 없는가?
A. 같은 Origin처럼 구성하면 CORS 문제가 줄어든다. 단, 실제 구조에 따라 백엔드 설정이 필요할 수 있다.

Q. /api 요청이 index.html을 반환하는 이유는?
A. SPA fallback 설정이 API 경로까지 잡고 있을 가능성이 높다.

Q. Same Origin Proxy에서 가장 중요한 것은?
A. `/api` 요청이 React fallback이 아니라 백엔드로 전달되어야 한다.

---

## 3.2 Nginx API Proxy

### [개념]

Nginx API Proxy는 Nginx가 `/api` 요청을 백엔드 서버로 전달하는 방식이다.

---

### [핵심]

Nginx API Proxy 기준:

- `/api/` location을 별도로 둔다.
- SPA fallback보다 API location이 우선되어야 한다.
- `proxy_pass` 경로 slash 처리를 확인한다.
- `Host`, `X-Forwarded-*` header를 전달한다.
- WebSocket 사용 시 upgrade header가 필요하다.
- timeout 설정이 필요할 수 있다.

---

### [실무]

기본 Nginx Proxy 예:

```nginx
server {
  listen 80;
  server_name example.com;

  root /usr/share/nginx/html;
  index index.html;

  location /api/ {
    proxy_pass http://backend:8080/api/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
  }

  location / {
    try_files $uri $uri/ /index.html;
  }
}
```

주의:

```text
location /api/
→ backend로 proxy

location /
→ React SPA fallback
```

Agent 검토 Flow:

```text
Nginx config 확인
→ /api location 확인
→ proxy_pass target 확인
→ fallback location 확인
→ Network Request URL 확인
→ Backend log 확인
```

---

### [FAQ]

Q. Nginx에서 /api proxy는 왜 필요한가?
A. 같은 도메인에서 API 요청을 백엔드로 전달해 CORS 복잡도를 줄이기 위해 사용한다.

Q. /api location과 / location 중 무엇이 먼저 중요한다?
A. `/api` 요청이 fallback에 잡히지 않도록 API location을 명확히 분리해야 한다.

Q. proxy_pass 경로에서 slash가 중요한가?
A. 중요하다. slash 처리에 따라 백엔드로 전달되는 path가 달라질 수 있다.

Q. Nginx proxy 후 API 404가 나면 무엇을 확인하는가?
A. Request URL, proxy_pass path, 백엔드 controller path, `/api` 중복 여부를 확인한다.

---

## 3.3 Spring Boot Proxy or Integrated API Path

### [개념]

Spring Boot 통합 배포에서는 같은 서버가 React 정적 파일과 API를 함께 제공할 수 있다.

구조:

```text
Spring Boot
→ static/index.html 제공
→ /api/** 요청은 Controller 처리
→ 그 외 SPA route는 index.html fallback
```

---

### [핵심]

Spring Boot 통합 API 기준:

- API 경로는 `/api` prefix 권장
- React route와 API route 충돌 방지
- SPA fallback이 API 경로를 잡으면 안 됨
- Security 설정에서 API와 static resource를 구분
- React build output이 static root에 위치해야 함

---

### [실무]

권장 경로:

```text
Frontend Route
→ /festival/detail/1

Backend API
→ /api/festivals/1
```

비권장 경로:

```text
Frontend Route
→ /festival/detail/1

Backend API
→ /festival/detail/1
```

Fallback 주의:

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

Agent 확인:

```text
API prefix 확인
→ fallback mapping 확인
→ API가 index.html 반환하는지 확인
→ Security permit/static 설정 확인
```

---

### [FAQ]

Q. Spring Boot 통합 배포에서도 /api prefix가 필요한가?
A. 강력히 권장된다. React route와 백엔드 API 충돌을 줄일 수 있다.

Q. API 호출했는데 index.html이 반환되는 이유는?
A. SPA fallback controller가 API 경로까지 잡고 있을 가능성이 있다.

Q. React route와 API path가 같아도 되는가?
A. 권장하지 않는다. `/api` prefix로 API를 분리하는 것이 안전하다.

Q. Spring Boot 통합 배포의 장점은 무엇인가?
A. 서버 하나로 프론트엔드와 백엔드를 제공할 수 있어 학원 프로젝트나 소규모 데모에 단순하다.

---

# 4. CORS and Origin

## 4.1 Origin Definition

### [개념]

Origin은 브라우저 보안 정책에서 사용하는 출처 기준이며 protocol, host, port 조합으로 결정된다.

예:

```text
http://localhost:3000
https://localhost:3000
http://localhost:8080
https://example.com
https://api.example.com
```

---

### [핵심]

Origin 판단 기준:

```text
Protocol
+ Host
+ Port
= Origin
```

다른 Origin 예:

```text
http://localhost:3000
http://localhost:8080
→ port가 다르므로 다른 Origin

http://example.com
https://example.com
→ protocol이 다르므로 다른 Origin

https://example.com
https://api.example.com
→ host가 다르므로 다른 Origin
```

---

### [실무]

2026 실무 기준으로 CORS 오류를 판단하려면 먼저 Origin을 정확히 구분해야 한다.

Local 개발 예:

```text
Frontend: http://localhost:3000
Backend: http://localhost:8080
Result: Cross-Origin
```

운영 분리 배포 예:

```text
Frontend: https://example.com
Backend: https://api.example.com
Result: Cross-Origin
```

Same Origin Proxy 예:

```text
Frontend: https://example.com
API Request: https://example.com/api
Result: Same-Origin
```

---

### [FAQ]

Q. Origin은 무엇으로 결정되는가?
A. protocol, host, port 조합으로 결정된다.

Q. localhost에서 포트만 달라도 Cross-Origin인가?
A. 그렇다. 포트가 다르면 다른 Origin이다.

Q. example.com과 api.example.com은 같은 Origin인가?
A. 아니다. host가 다르므로 다른 Origin이다.

Q. /api proxy를 쓰면 Origin이 어떻게 되는가?
A. 브라우저 기준으로 같은 도메인의 `/api`를 호출하므로 Same-Origin처럼 동작할 수 있다.

---

## 4.2 CORS Core Rules

### [개념]

CORS는 브라우저가 다른 Origin으로 API 요청을 보낼 때 적용하는 보안 정책이다.

---

### [핵심]

CORS가 필요한 상황:

- 프론트엔드와 백엔드 도메인이 다름
- 포트가 다름
- protocol이 다름
- Authorization Header 사용
- Cookie 인증 사용
- Custom Header 사용
- Preflight 요청 발생

CORS 설정 주체:

```text
대부분 Backend Server
Nginx
API Gateway
```

프론트엔드만으로 CORS를 근본 해결하기 어렵다.

---

### [실무]

백엔드 CORS 허용 예:

```text
Access-Control-Allow-Origin: https://frontend.example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
Access-Control-Allow-Headers: Authorization, Content-Type
```

CORS Troubleshooting Flow:

```text
Console CORS Error 확인
→ Request Origin 확인
→ API URL 확인
→ Backend CORS allowed origins 확인
→ allowed headers 확인
→ allowed methods 확인
→ credentials 여부 확인
```

Agent 판단:

```text
CORS error 발생
→ 프론트 코드 수정만 제안하지 않음
→ 백엔드 CORS 설정 확인 필요
```

---

### [FAQ]

Q. CORS는 프론트엔드에서 해결하는가?
A. 대부분 백엔드 서버에서 허용 Origin, Method, Header를 설정해야 해결된다.

Q. CORS는 왜 로컬에서 자주 발생하는가?
A. 프론트엔드와 백엔드가 서로 다른 포트에서 실행되어 다른 Origin이 되기 때문이다.

Q. Authorization Header를 쓰면 CORS에 영향이 있는가?
A. 있다. Preflight 요청과 allowed headers 설정이 필요할 수 있다.

Q. /api Same Origin Proxy를 쓰면 CORS가 줄어드는가?
A. 줄어들 수 있다. 브라우저 기준 같은 Origin 요청이 되기 때문이다.

---

## 4.3 Credentials and CORS

### [개념]

Credentials는 브라우저 요청에 Cookie, Authorization 정보, 인증 관련 정보를 포함하는 방식이다.

프론트엔드에서 Cookie 인증을 사용할 때는 `withCredentials` 설정이 필요할 수 있다.

---

### [핵심]

Cookie 인증 조건:

```js
axios.create({
  baseURL: "https://api.example.com",
  withCredentials: true,
});
```

백엔드 필요 설정:

```text
Access-Control-Allow-Origin: https://frontend.example.com
Access-Control-Allow-Credentials: true
```

중요 제한:

```text
Credentials 사용 시
Access-Control-Allow-Origin: *
사용 불가
```

JWT Authorization Header 방식:

```text
Authorization: Bearer token
```

이 방식은 보통 `withCredentials`가 필요하지 않다.

---

### [실무]

Cookie 인증 Troubleshooting Flow:

```text
Network Request 확인
→ withCredentials 확인
→ Response Set-Cookie 확인
→ Access-Control-Allow-Credentials 확인
→ Access-Control-Allow-Origin 확인
→ SameSite / Secure / Domain 확인
→ Application Cookies 확인
```

Authorization Header 인증 Troubleshooting Flow:

```text
localStorage/sessionStorage token 확인
→ Request Headers Authorization 확인
→ Bearer prefix 확인
→ 401 response 확인
→ refresh flow 확인
```

---

### [FAQ]

Q. withCredentials는 언제 필요한가?
A. 쿠키 기반 인증을 사용할 때 필요하다.

Q. JWT를 Authorization Header로 보내도 withCredentials가 필요한가?
A. 보통 필요하지 않다. 쿠키 인증과 Header 인증을 구분해야 한다.

Q. Credentials 사용 시 CORS에서 \*를 써도 되는가?
A. 안 된다. 명시적인 Origin을 지정해야 한다.

Q. 로그인 응답에 Set-Cookie가 있는데 쿠키가 저장되지 않는 이유는?
A. withCredentials, SameSite, Secure, Domain, CORS credentials 설정을 확인해야 한다.

---

# 5. HTTPS and Mixed Content

## 5.1 HTTPS API Requirement

### [개념]

HTTPS API Requirement는 운영 프론트엔드가 HTTPS로 제공될 때 API도 HTTPS로 호출해야 한다는 기준이다.

---

### [핵심]

문제 상황:

```text
Frontend: https://example.com
API: http://api.example.com
Result: Mixed Content Blocked
```

정상 상황:

```text
Frontend: https://example.com
API: https://api.example.com
Result: Allowed
```

운영 기준:

- 프론트엔드 HTTPS
- 백엔드 API HTTPS
- 이미지 / 폰트 / 스크립트 HTTPS
- WebSocket은 `wss://`
- Cookie Secure 설정 검토

---

### [실무]

배포 전 확인:

```md
- [ ] 프론트엔드 URL이 HTTPS인가?
- [ ] API Base URL이 HTTPS인가?
- [ ] 이미지 URL이 HTTPS인가?
- [ ] WebSocket URL이 wss인가?
- [ ] Cookie Secure 설정이 필요한가?
- [ ] Reverse Proxy에서 X-Forwarded-Proto가 전달되는가?
```

Mixed Content Troubleshooting Flow:

```text
Console Mixed Content 확인
→ Request URL 확인
→ API Base URL 확인
→ env 값 수정
→ HTTPS 인증서 적용
→ rebuild/redeploy
```

---

### [FAQ]

Q. HTTPS 사이트에서 HTTP API를 호출하면 왜 안 되는가?
A. 브라우저가 Mixed Content로 차단할 수 있다.

Q. 운영 API는 반드시 HTTPS여야 하는가?
A. 운영에서는 HTTPS를 사용하는 것이 기본 기준이다.

Q. WebSocket도 HTTPS 영향을 받는가?
A. 받는다. HTTPS 페이지에서는 `ws://` 대신 `wss://`를 사용해야 한다.

Q. Mixed Content는 어디서 확인하는가?
A. 브라우저 Console과 Network 탭에서 확인한다.

---

## 5.2 Reverse Proxy HTTPS Awareness

### [개념]

Reverse Proxy HTTPS Awareness는 Nginx나 Load Balancer 뒤의 백엔드가 원래 요청이 HTTPS였는지 인식하도록 설정하는 것이다.

---

### [핵심]

필요한 Header:

```text
X-Forwarded-Proto
X-Forwarded-Host
X-Forwarded-For
X-Real-IP
```

문제 상황:

```text
Browser → HTTPS → Nginx → HTTP → Backend
Backend가 HTTP 요청으로 인식
→ redirect URL / cookie Secure / callback URL 문제 가능
```

---

### [실무]

Nginx 예:

```nginx
location /api/ {
  proxy_pass http://backend:8080/api/;
  proxy_set_header Host $host;
  proxy_set_header X-Real-IP $remote_addr;
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  proxy_set_header X-Forwarded-Proto $scheme;
}
```

Spring Boot 설정 검토:

```properties
server.forward-headers-strategy=framework
```

Agent 확인 Flow:

```text
HTTPS Reverse Proxy 여부 확인
→ X-Forwarded-Proto 전달 확인
→ Backend forward header 처리 확인
→ Cookie Secure / redirect URL 확인
```

---

### [FAQ]

Q. Nginx 뒤에서 백엔드가 HTTP로 인식하는 이유는?
A. Nginx와 백엔드 사이 통신이 HTTP이고 forwarded header 처리가 없을 수 있다.

Q. X-Forwarded-Proto는 왜 필요한가?
A. 원래 클라이언트 요청이 HTTPS였는지 백엔드가 알기 위해 필요하다.

Q. HTTPS인데 쿠키나 redirect가 이상한 이유는?
A. Reverse Proxy header와 백엔드 forward header 설정을 확인해야 한다.

Q. Spring Boot에서 forwarded header 처리가 필요한가?
A. Reverse Proxy 뒤에서 HTTPS, redirect, cookie 문제가 있으면 필요할 수 있다.

---

# 6. Authentication API URL

## 6.1 Authorization Header API

### [개념]

Authorization Header API는 JWT 같은 토큰을 HTTP Header에 포함해 API를 호출하는 방식이다.

형식:

```text
Authorization: Bearer <accessToken>
```

---

### [핵심]

Authorization Header 방식 기준:

- Axios interceptor에서 token 추가 가능
- `withCredentials`는 보통 필요하지 않음
- CORS allowed headers에 Authorization 필요
- Token 저장 위치 확인 필요
- 401 발생 시 refresh flow 확인
- API Base URL이 정확해야 token 전송도 의미가 있음

---

### [실무]

Axios 예:

```js
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("accessToken");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});
```

검증 Flow:

```text
Network Request 선택
→ Request Headers 확인
→ Authorization 존재 확인
→ Bearer prefix 확인
→ API URL 확인
→ Response 401 확인
```

CORS 확인:

```text
Access-Control-Allow-Headers에 Authorization 포함 여부
```

---

### [FAQ]

Q. JWT Authorization Header 방식에서 withCredentials가 필요한가?
A. 보통 필요하지 않다. Cookie 인증과 구분해야 한다.

Q. Authorization Header가 안 붙는 이유는?
A. token 저장 위치, interceptor 등록, api instance 사용 여부, 요청 시점 token 존재 여부를 확인해야 한다.

Q. Authorization Header 때문에 CORS 문제가 생길 수 있는가?
A. 가능하다. 백엔드 CORS allowed headers에 Authorization이 필요할 수 있다.

Q. API Base URL이 틀리면 인증도 실패하는가?
A. 그렇다. 잘못된 서버로 요청하면 token이 있어도 정상 인증되지 않는다.

---

## 6.2 Cookie Authentication API

### [개념]

Cookie Authentication API는 인증 정보를 Cookie로 주고받는 방식이며, 배포 환경에서는 CORS, SameSite, Secure 설정이 중요하다.

---

### [핵심]

Cookie 인증 프론트엔드 기준:

```js
axios.create({
  baseURL: "https://api.example.com",
  withCredentials: true,
});
```

Cookie 인증 백엔드 기준:

```text
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: https://frontend.example.com
Set-Cookie: ...; SameSite=None; Secure
```

Same Origin Proxy 구조에서는 설정이 단순해질 수 있다.

---

### [실무]

Cookie 인증 배포 점검:

```md
- [ ] API Base URL이 정확한가?
- [ ] withCredentials가 필요한 구조인가?
- [ ] CORS credentials 허용이 있는가?
- [ ] Access-Control-Allow-Origin이 \*가 아닌가?
- [ ] Set-Cookie가 응답에 있는가?
- [ ] SameSite 설정이 도메인 구조와 맞는가?
- [ ] Secure 설정과 HTTPS가 맞는가?
- [ ] Domain / Path가 맞는가?
- [ ] Application 탭에 Cookie가 저장되는가?
```

Troubleshooting Flow:

```text
Login Request 확인
→ Response Headers Set-Cookie 확인
→ Application Cookies 확인
→ SameSite / Secure / Domain 확인
→ 이후 API Request Cookie 포함 확인
```

---

### [FAQ]

Q. Cookie 인증에서 withCredentials는 왜 필요한가?
A. Cross-Origin 요청에 쿠키를 포함하거나 응답 쿠키를 저장하려면 필요할 수 있다.

Q. Set-Cookie가 있는데 브라우저에 저장되지 않는 이유는?
A. SameSite, Secure, Domain, CORS credentials, HTTPS 설정이 맞지 않을 수 있다.

Q. Cookie 인증에서 Access-Control-Allow-Origin을 \*로 써도 되는가?
A. Credentials 사용 시에는 안 된다. 명시적인 Origin을 지정해야 한다.

Q. Same Origin Proxy를 쓰면 Cookie 설정이 쉬워지는가?
A. 같은 도메인 구조가 되면 CORS와 Cookie 설정이 단순해질 수 있다.

---

# 7. WebSocket API URL

## 7.1 WebSocket URL Rules

### [개념]

WebSocket URL은 실시간 통신을 위해 사용하는 연결 주소이며 HTTP API URL과 protocol이 다르다.

대표 protocol:

```text
ws://
wss://
```

---

### [핵심]

WebSocket URL 기준:

- HTTP 페이지에서는 `ws://` 가능
- HTTPS 페이지에서는 `wss://` 필요
- 운영에서는 `wss://` 권장
- API Base URL과 WebSocket Base URL을 분리할 수 있다.
- Nginx proxy 시 Upgrade header 필요
- 인증 방식은 query parameter, header, cookie, subprotocol 등 구조에 따라 다름

---

### [실무]

환경 변수 예:

Vite:

```env
VITE_API_BASE_URL=https://api.example.com
VITE_WS_BASE_URL=wss://api.example.com/ws
```

WebSocket 생성 예:

```js
const socket = new WebSocket(import.meta.env.VITE_WS_BASE_URL);
```

Nginx proxy 예:

```nginx
location /ws/ {
  proxy_pass http://backend:8080/ws/;
  proxy_http_version 1.1;
  proxy_set_header Upgrade $http_upgrade;
  proxy_set_header Connection "upgrade";
  proxy_set_header Host $host;
}
```

---

### [FAQ]

Q. HTTPS 사이트에서 ws://를 써도 되는가?
A. 안 된다. HTTPS 페이지에서는 `wss://`를 사용해야 한다.

Q. WebSocket URL도 env로 분리해야 하는가?
A. 권장된다. 로컬과 운영 WebSocket 주소가 다를 수 있기 때문이다.

Q. Nginx에서 WebSocket proxy는 일반 API proxy와 같은가?
A. 유사하지만 Upgrade header와 HTTP/1.1 설정이 필요하다.

Q. WebSocket 연결 실패는 어디서 확인하는가?
A. Browser DevTools Network 탭의 WS 항목과 Console을 확인한다.

---

# 8. API URL Troubleshooting

## 8.1 API Request Failed

### [개념]

API Request Failed는 프론트엔드가 백엔드 API 호출에 실패하는 상태다.

---

### [핵심]

대표 원인:

- API Base URL 오류
- endpoint path 오류
- `/api` 중복
- 운영 env 누락
- localhost 잔존
- CORS 오류
- Mixed Content
- Authorization Header 누락
- Cookie 미포함
- 백엔드 서버 미실행
- proxy 설정 오류
- backend route 불일치

---

### [실무]

Troubleshooting Flow:

```text
Network Request URL 확인
→ Status Code 확인
→ Response Body 확인
→ Console Error 확인
→ API Base URL 확인
→ Env 값 확인
→ Proxy 설정 확인
→ Auth Header / Cookie 확인
→ Backend Log 확인
```

Status별 1차 판단:

```text
404
→ URL path / proxy / backend route 확인

401
→ token / cookie / auth flow 확인

403
→ 권한 / CORS / CSRF / security config 확인

500
→ backend log 확인

CORS Error
→ backend CORS allowed origin/header/method 확인

Mixed Content
→ HTTPS API 사용 확인
```

---

### [FAQ]

Q. 배포 후 API가 안 되면 무엇을 먼저 봐야 하는가?
A. Network 탭에서 Request URL, Status Code, Response Body를 먼저 확인한다.

Q. API 404는 무엇을 의미하는가?
A. API URL path, proxy 경로, backend route가 맞지 않을 가능성이 높다.

Q. API 401은 무엇을 확인해야 하는가?
A. Authorization Header, token 저장, refresh flow, cookie 포함 여부를 확인해야 한다.

Q. API 500은 프론트엔드 문제인가?
A. 보통 백엔드 내부 오류 가능성이 높으므로 backend log를 확인해야 한다.

---

## 8.2 Localhost After Deploy

### [개념]

Localhost After Deploy는 운영 배포 후 API 요청이 여전히 `localhost`로 나가는 문제다.

---

### [핵심]

대표 원인:

- `.env.production` 누락
- CI/CD env 설정 누락
- Hosting Platform env 누락
- 코드에 localhost 하드코딩
- env fallback이 localhost
- Build 시 local env 사용
- 재빌드 없이 배포
- 브라우저/CDN 캐시

---

### [실무]

위험 코드:

```js
const baseURL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8080";
```

운영 안전 코드:

```js
const baseURL = import.meta.env.VITE_API_BASE_URL;

if (!baseURL) {
  throw new Error("VITE_API_BASE_URL is required");
}
```

Troubleshooting Flow:

```text
Network에서 localhost 확인
→ source code에서 localhost 검색
→ env 파일 확인
→ CI/CD env 확인
→ platform env 확인
→ rebuild 여부 확인
→ cache 확인
```

---

### [FAQ]

Q. 배포 후 API가 localhost로 호출되는 이유는?
A. 운영 env가 누락되었거나 코드에 localhost fallback이 남아 있기 때문이다.

Q. localhost fallback은 편리한데 왜 위험한가?
A. 운영 env 누락을 숨기고 사용자 브라우저에서 잘못된 요청을 만들 수 있다.

Q. localhost를 어디에서 검색해야 하는가?
A. `.env`, API client, axios instance, config file, CI/CD workflow, 배포 플랫폼 env를 확인한다.

Q. env를 수정했는데도 localhost로 호출되는 이유는?
A. 재빌드 누락 또는 브라우저/CDN 캐시 문제일 수 있다.

---

## 8.3 API Returns index.html

### [개념]

API Returns index.html은 API 요청에 JSON이 아니라 React의 `index.html`이 응답되는 문제다.

---

### [핵심]

대표 원인:

- SPA fallback이 API 경로까지 처리
- Nginx `/api` proxy location 누락
- Spring Boot fallback controller가 API 경로를 잡음
- API prefix 미분리
- Hosting Platform rewrite가 API 요청까지 index.html로 보냄
- proxy 설정 순서 오류

---

### [실무]

증상:

```text
API 요청 응답 Content-Type: text/html
Response Body: <!doctype html><html...
JSON parse error 발생
Unexpected token '<'
```

Troubleshooting Flow:

```text
Network Response 확인
→ Content-Type 확인
→ Response Body가 index.html인지 확인
→ 요청 URL이 /api인지 확인
→ Nginx /api location 확인
→ Spring Boot fallback 확인
→ Hosting rewrite 확인
```

Nginx 올바른 구조:

```text
/api/*
→ backend proxy

/*
→ index.html fallback
```

---

### [FAQ]

Q. API 응답으로 index.html이 오는 이유는?
A. SPA fallback 설정이 API 요청까지 index.html로 보내고 있을 가능성이 높다.

Q. Unexpected token '<' 에러는 무엇인가?
A. JSON을 기대했지만 HTML 문서가 응답되어 파싱에 실패한 경우가 많다.

Q. 이 문제는 프론트엔드 코드 문제인가?
A. 대부분 서버 routing, proxy, fallback 설정 문제다.

Q. 어떻게 해결하는가?
A. `/api` 경로를 SPA fallback에서 제외하고 백엔드로 proxy하거나 Controller가 처리하게 해야 한다.

---

## 8.4 API Path Duplication

### [개념]

API Path Duplication은 baseURL과 endpoint path에 같은 prefix가 중복되어 잘못된 API URL이 만들어지는 문제다.

---

### [핵심]

문제 예:

```text
baseURL = /api
path = /api/festivals
result = /api/api/festivals
```

```text
baseURL = https://api.example.com/api
path = /api/users
result = https://api.example.com/api/api/users
```

증상:

- API 404
- proxy route mismatch
- backend route mismatch
- 특정 API만 실패
- 환경별로 다르게 실패

---

### [실무]

해결 기준:

Pattern A:

```text
baseURL = /api
endpoint = /festivals
```

Pattern B:

```text
baseURL = https://api.example.com
endpoint = /api/festivals
```

팀 규칙 문서화:

```md
- API Base URL에 `/api` 포함 여부를 명시한다.
- endpoint path에는 `/api`를 중복 작성하지 않는다.
- Axios instance 기준으로 API path를 통일한다.
```

---

### [FAQ]

Q. API 경로에 /api가 두 번 붙는 이유는?
A. baseURL과 endpoint path 양쪽에 `/api`가 들어갔기 때문이다.

Q. /api 중복은 어떻게 방지하는가?
A. baseURL에 `/api`를 넣을지 endpoint에 넣을지 팀 규칙을 하나로 정한다.

Q. 특정 API만 404가 나는 이유가 path 중복일 수 있는가?
A. 가능하다. 해당 API method의 path 작성 방식을 확인해야 한다.

Q. path 중복은 어디서 확인하는가?
A. Network Request URL과 API client 코드를 함께 확인한다.

---

# 9. Agent Decision Rules

## 9.1 PM Agent Rules

### [개념]

PM Agent는 API Base URL 전략, 배포 방식, proxy 구조, 인증 방식, 환경별 API 주소를 결정해야 한다.

---

### [핵심]

PM Agent 확인 항목:

- Local API URL
- Staging API URL
- Production API URL
- Same Origin Proxy 사용 여부
- `/api` prefix 위치
- CORS 필요 여부
- HTTPS 적용 여부
- Auth 방식
- Cookie 사용 여부
- WebSocket 사용 여부
- 배포 플랫폼
- API URL 검증 범위

---

### [실무]

PM Agent 산출물 예:

```text
API Strategy: Same Origin Proxy
Frontend Base URL: /api
Backend API Prefix: /api
Proxy: Nginx /api → backend:8080/api
Auth: Authorization Header JWT
CORS: Same Origin 구조로 최소화
HTTPS: Required
Verification: Network Request URL / Status Code / Auth Header
```

PM Agent 판단 Flow:

```text
배포 방식 확인
→ API URL 전략 선택
→ /api prefix 규칙 정의
→ 인증 방식 확인
→ CORS/HTTPS 필요 여부 정리
→ 검증 체크리스트 전달
```

---

### [FAQ]

Q. PM Agent는 API URL에서 무엇을 정해야 하는가?
A. 환경별 API URL, `/api` prefix 위치, proxy 구조, CORS 필요 여부, 인증 방식을 정해야 한다.

Q. PM Agent가 /api prefix 규칙을 정해야 하는 이유는?
A. baseURL과 endpoint path 중복을 방지하기 위해 필요하다.

Q. PM Agent가 인증 방식도 확인해야 하는가?
A. 그렇다. Cookie 인증인지 Authorization Header 인증인지에 따라 API 설정이 달라진다.

Q. PM Agent가 WebSocket URL도 관리해야 하는가?
A. 실시간 기능이 있다면 API URL과 별도로 WebSocket URL 전략도 정리해야 한다.

---

## 9.2 Frontend Agent Rules

### [개념]

Frontend Agent는 API Base URL을 환경 변수로 분리하고, API client에서 일관된 요청 경로를 사용해야 한다.

---

### [핵심]

Frontend Agent 필수 기준:

- API Base URL env 사용
- 운영 localhost 하드코딩 금지
- `/api` prefix 중복 금지
- Axios instance 중앙화
- Authorization Header 처리 일관성
- Cookie 인증 시 `withCredentials` 설정
- WebSocket URL env 분리
- API error response 확인 로직
- Network 검증 기준 제공

---

### [실무]

Vite API client 예:

```js
import axios from "axios";

const baseURL = import.meta.env.VITE_API_BASE_URL;

if (!baseURL) {
  throw new Error("VITE_API_BASE_URL is required");
}

export const api = axios.create({
  baseURL,
  timeout: 10000,
});
```

Authorization Header 예:

```js
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("accessToken");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});
```

Cookie 인증 예:

```js
export const api = axios.create({
  baseURL,
  withCredentials: true,
  timeout: 10000,
});
```

---

### [FAQ]

Q. Frontend Agent는 API Base URL을 어떻게 관리해야 하는가?
A. 환경 변수로 분리하고 Axios instance 같은 중앙 API client에서 사용해야 한다.

Q. API URL을 컴포넌트마다 직접 작성해도 되는가?
A. 권장하지 않는다. API client를 중앙화해야 변경과 검토가 쉽다.

Q. Authorization Header는 어디서 처리하는 것이 좋은가?
A. Axios interceptor 같은 공통 요청 처리 계층에서 처리하는 것이 좋다.

Q. Cookie 인증이면 Frontend Agent가 무엇을 추가해야 하는가?
A. `withCredentials: true`와 CORS/Cookie 설정 검증 기준을 함께 고려해야 한다.

---

## 9.3 Review Agent Rules

### [개념]

Review Agent는 API Base URL, path 조합, CORS, HTTPS, 인증 헤더, Cookie, proxy 설정을 검토해야 한다.

---

### [핵심]

Review Agent Checklist:

```md
- [ ] API Base URL이 env로 분리되어 있는가?
- [ ] 운영 API URL에 localhost가 없는가?
- [ ] HTTPS 프론트엔드에서 HTTPS API를 호출하는가?
- [ ] baseURL과 endpoint path에 /api 중복이 없는가?
- [ ] Same Origin Proxy 사용 시 /api proxy가 존재하는가?
- [ ] SPA fallback이 /api 요청을 잡지 않는가?
- [ ] CORS allowed origin이 맞는가?
- [ ] Authorization Header가 필요한 경우 전송되는가?
- [ ] Cookie 인증 시 withCredentials가 맞는가?
- [ ] Set-Cookie / SameSite / Secure / Domain이 맞는가?
- [ ] WebSocket 사용 시 ws/wss가 맞는가?
- [ ] Network Request URL과 Status Code를 확인했는가?
```

---

### [실무]

Review Agent 판단 Flow:

```text
env 확인
→ API client 확인
→ /api prefix 규칙 확인
→ build 실행
→ 배포 또는 preview 실행
→ Network Request URL 확인
→ Status Code 확인
→ Auth Header / Cookie 확인
→ Console Error 확인
```

Critical Issue:

```text
Production API URL이 localhost
HTTPS 페이지에서 HTTP API 호출
API 응답이 index.html
Secret Key가 frontend env에 존재
Cookie 인증인데 credentials 설정 불일치
/api path 중복
```

승인 기준:

```text
API URL 정상
CORS 위험 대응 가능
HTTPS 정상
Auth 전송 정상
Proxy/Fallback 충돌 없음
Network 검증 완료
```

---

### [FAQ]

Q. Review Agent는 API URL에서 무엇을 가장 먼저 확인해야 하는가?
A. 운영 API URL에 localhost가 남아 있는지와 실제 Network Request URL을 먼저 확인해야 한다.

Q. API 응답이 index.html이면 승인 가능한가?
A. 아니다. API와 SPA fallback 경로가 충돌하는 치명적 문제다.

Q. HTTPS 페이지에서 HTTP API를 호출하면 승인 가능한가?
A. 아니다. Mixed Content로 차단될 수 있다.

Q. /api 중복이 있으면 어떤 문제가 생기는가?
A. API 404, proxy route mismatch, backend route mismatch가 발생할 수 있다.

---

# 10. Common Mistakes

## 10.1 API Base URL Common Mistakes

### [개념]

API Base URL Common Mistakes는 프론트엔드 배포 후 API 호출 실패로 이어지는 반복 실수다.

---

### [핵심]

자주 발생하는 실수:

- 운영 API URL에 localhost 사용
- API URL을 코드에 직접 하드코딩
- env 누락 시 localhost fallback 사용
- baseURL과 endpoint path에 `/api` 중복
- Vite / CRA env prefix 혼동
- `.env.production` 누락
- CI/CD env 설정 누락
- dev proxy를 운영 proxy로 착각
- Nginx `/api` location 누락
- SPA fallback이 API 요청을 index.html로 반환
- HTTPS 페이지에서 HTTP API 호출
- CORS를 프론트엔드만으로 해결하려고 함
- Cookie 인증에서 `withCredentials` 누락
- Credentials 사용 시 `Access-Control-Allow-Origin: *` 사용
- Authorization Header가 CORS allowed headers에 없음
- WebSocket에서 HTTPS 페이지에 `ws://` 사용
- Docker 내부 service name을 브라우저 API URL로 사용

---

### [실무]

실수별 판단:

```text
API localhost 호출
→ production env / fallback / rebuild 확인

/api/api 호출
→ baseURL과 endpoint path 확인

Unexpected token '<'
→ API가 index.html 반환하는지 확인

CORS error
→ backend allowed origin/header/method 확인

Mixed Content
→ HTTPS API URL 확인

Cookie 저장 안 됨
→ withCredentials / SameSite / Secure / Domain 확인
```

---

### [FAQ]

Q. API URL 관련 가장 흔한 배포 실수는 무엇인가?
A. 운영 Build에 localhost API URL이 남는 것이다.

Q. API URL 관련 가장 헷갈리는 문제는 무엇인가?
A. `/api` prefix를 baseURL과 endpoint에 중복 작성하는 문제다.

Q. API 요청에 HTML이 돌아오면 무엇을 의심해야 하는가?
A. SPA fallback이 API 요청을 index.html로 처리하고 있는지 확인해야 한다.

Q. 개발에서는 API가 되는데 배포 후 실패하는 이유는?
A. dev proxy, CORS, 운영 API URL, HTTPS, Cookie 설정이 운영과 다르기 때문이다.

---

# 11. Part04 Quality Checklist

## 11.1 Document Quality

### [개념]

이 문서는 Frontend Build & Deploy Domain의 Part04이며 API Base URL Rules Retrieval에 최적화되어야 한다.

---

### [핵심]

문서 품질 기준:

- API Base URL 정의 포함
- API URL Composition 포함
- Local / Staging / Production API URL 구분
- Same Origin Proxy 포함
- Nginx API Proxy 포함
- Spring Boot 통합 API Path 포함
- Origin / CORS 기준 포함
- Credentials / Authorization Header 구분
- HTTPS / Mixed Content 포함
- Reverse Proxy HTTPS Awareness 포함
- WebSocket URL 기준 포함
- Troubleshooting Flow 포함
- Agent별 판단 기준 포함
- Common Mistakes 포함
- Retrieval Queries 포함

---

### [실무]

Part04는 다음 문서와 연결된다.

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

Q. Part04의 핵심 목적은 무엇인가?
A. 프론트엔드가 백엔드 API를 호출할 때 API Base URL, proxy, CORS, HTTPS, 인증 문제를 Agent가 정확히 판단하게 하는 것이다.

Q. Part04에서 배포 서버 전체를 다루는가?
A. 아니다. API 요청 관점의 URL, proxy, CORS, HTTPS 문제에 집중한다.

Q. Part04에서 Spring Boot 통합 배포를 자세히 다루는가?
A. API 경로 충돌과 fallback 위험만 다루고 세부 통합 배포는 후속 Part에서 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. API Base URL이란 무엇인가?
A. 프론트엔드가 백엔드 API를 호출할 때 사용하는 기본 주소다.

Q. API Base URL은 왜 환경 변수로 분리하는가?
A. 로컬, 개발, 스테이징, 운영 환경의 백엔드 주소가 다르기 때문이다.

Q. 운영 API URL에 localhost를 사용해도 되는가?
A. 안 된다. 사용자 브라우저 기준 localhost는 사용자 자신의 PC를 의미한다.

Q. API Base URL은 어디서 최종 확인하는가?
A. 브라우저 개발자 도구 Network 탭의 실제 Request URL에서 확인한다.

Q. API URL에 /api가 두 번 붙는 이유는?
A. baseURL과 endpoint path 양쪽에 `/api`가 중복되었기 때문이다.

Q. /api 중복은 어떻게 방지하는가?
A. baseURL에 `/api`를 넣을지 endpoint에 넣을지 팀 규칙을 하나로 정해야 한다.

Q. baseURL을 /api로 써도 되는가?
A. 가능하다. 같은 도메인에서 Nginx나 서버가 `/api` 요청을 백엔드로 proxy해야 한다.

Q. Same Origin Proxy란 무엇인가?
A. 프론트엔드와 백엔드를 같은 Origin처럼 보이게 하고 `/api` 요청을 백엔드로 전달하는 구조다.

Q. Same Origin Proxy의 장점은 무엇인가?
A. CORS 복잡도를 줄이고 프론트엔드 baseURL을 `/api`로 단순화할 수 있다.

Q. /api 요청이 index.html을 반환하는 이유는?
A. SPA fallback 설정이 API 요청까지 index.html로 보내고 있을 가능성이 높다.

Q. Nginx에서 /api proxy는 왜 필요한가?
A. 같은 도메인에서 API 요청을 백엔드로 전달해 CORS 복잡도를 줄이기 위해 사용한다.

Q. Nginx proxy 설정에서 중요한 것은 무엇인가?
A. `/api` location을 SPA fallback과 분리하고 proxy_pass 경로를 정확히 설정해야 한다.

Q. Spring Boot 통합 배포에서 API prefix는 무엇이 좋은가?
A. `/api` prefix를 사용하는 것이 React route와 API route 충돌을 줄이는 데 안전하다.

Q. API 호출했는데 index.html이 오는 이유는?
A. Spring Boot fallback controller나 Nginx fallback이 API 경로를 잡고 있을 수 있다.

Q. Origin은 무엇으로 결정되는가?
A. protocol, host, port 조합으로 결정된다.

Q. localhost에서 포트만 달라도 Cross-Origin인가?
A. 그렇다. 포트가 다르면 다른 Origin이다.

Q. CORS는 프론트엔드에서 해결하는가?
A. 대부분 백엔드 서버에서 허용 Origin, Method, Header를 설정해야 해결된다.

Q. Authorization Header를 쓰면 CORS 설정이 필요한가?
A. Cross-Origin 요청이면 allowed headers에 Authorization이 필요할 수 있다.

Q. withCredentials는 언제 필요한가?
A. 쿠키 기반 인증을 사용할 때 필요하다.

Q. JWT Authorization Header 방식에서도 withCredentials가 필요한가?
A. 보통 필요하지 않다. Cookie 인증과 Header 인증을 구분해야 한다.

Q. Credentials 사용 시 Access-Control-Allow-Origin을 \*로 써도 되는가?
A. 안 된다. 명시적인 Origin을 지정해야 한다.

Q. HTTPS 사이트에서 HTTP API를 호출하면 왜 안 되는가?
A. 브라우저가 Mixed Content로 차단할 수 있다.

Q. 운영 API는 HTTPS를 사용해야 하는가?
A. 운영에서는 HTTPS 사용이 기본 기준이다.

Q. WebSocket은 HTTPS 배포에서 어떻게 해야 하는가?
A. HTTPS 페이지에서는 `ws://` 대신 `wss://`를 사용해야 한다.

Q. Reverse Proxy 뒤에서 X-Forwarded-Proto가 필요한 이유는?
A. 백엔드가 원래 클라이언트 요청이 HTTPS였는지 알기 위해 필요하다.

Q. JWT Authorization Header는 어떻게 전송하는가?
A. `Authorization: Bearer <accessToken>` 형태로 요청 Header에 포함한다.

Q. Authorization Header가 안 붙는 이유는?
A. token 저장 위치, interceptor 등록, api instance 사용 여부, 요청 시점 token 존재 여부를 확인해야 한다.

Q. Cookie 인증에서 쿠키가 저장되지 않는 이유는?
A. withCredentials, SameSite, Secure, Domain, CORS credentials 설정이 맞지 않을 수 있다.

Q. Set-Cookie가 있는데 브라우저에 저장되지 않는 이유는?
A. SameSite, Secure, Domain, CORS credentials, HTTPS 설정을 확인해야 한다.

Q. WebSocket URL도 env로 분리해야 하는가?
A. 권장된다. 로컬과 운영 WebSocket 주소가 다를 수 있기 때문이다.

Q. API 요청 실패 시 무엇을 먼저 확인하는가?
A. Network 탭에서 Request URL, Status Code, Response Body를 먼저 확인한다.

Q. API 404는 무엇을 확인해야 하는가?
A. URL path, proxy 경로, backend route, `/api` 중복 여부를 확인해야 한다.

Q. API 401은 무엇을 확인해야 하는가?
A. Authorization Header, token 저장, refresh flow, cookie 포함 여부를 확인해야 한다.

Q. API 500은 무엇을 확인해야 하는가?
A. 백엔드 내부 오류 가능성이 높으므로 backend log를 확인해야 한다.

Q. Unexpected token '<' 에러는 무엇인가?
A. JSON을 기대했지만 index.html 같은 HTML이 응답되어 파싱에 실패한 경우가 많다.

Q. 배포 후 API가 localhost로 호출되는 이유는?
A. 운영 env가 누락되었거나 코드에 localhost fallback이 남아 있기 때문이다.

Q. localhost fallback은 왜 위험한가?
A. 운영 env 누락을 숨기고 사용자 브라우저에서 잘못된 요청을 만들 수 있다.

Q. 개발에서는 API가 되는데 배포 후 실패하는 이유는?
A. dev proxy, CORS, 운영 API URL, HTTPS, Cookie 설정이 운영과 다르기 때문이다.

Q. Docker 내부 service name을 브라우저 API URL로 써도 되는가?
A. 안 된다. 브라우저는 Docker 내부 네트워크 service name을 알 수 없다.

Q. PM Agent는 API URL에서 무엇을 정해야 하는가?
A. 환경별 API URL, `/api` prefix 위치, proxy 구조, CORS 필요 여부, 인증 방식을 정해야 한다.

Q. Frontend Agent는 API Base URL을 어떻게 관리해야 하는가?
A. 환경 변수로 분리하고 Axios instance 같은 중앙 API client에서 사용해야 한다.

Q. Review Agent는 API URL에서 무엇을 가장 먼저 확인해야 하는가?
A. 운영 API URL에 localhost가 남아 있는지와 실제 Network Request URL을 먼저 확인해야 한다.

Q. Part04 다음 문서는 무엇인가?
A. Part05 Static File Hosting Rules로 이어지는 것이 적합하다.
