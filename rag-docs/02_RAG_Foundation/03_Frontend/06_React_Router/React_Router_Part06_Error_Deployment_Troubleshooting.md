# React Router Part06 Error Deployment Troubleshooting

---

# 1. Error Route and Deployment Troubleshooting

## 1.1 Purpose

### [개념]

React Router Error Deployment Troubleshooting 문서는 Route 오류 처리, Not Found Route, 잘못된 parameter 처리, SPA Refresh 404, Spring Boot Fallback, Nginx Fallback, API Path Collision 문제를 다룬다.

React Router는 브라우저 내부에서 URL과 Component를 매칭하는 Client Side Router이므로 배포 서버 설정과 함께 검토해야 한다.

이 문서는 Frontend Agent와 Review Agent가 React Router 기반 SPA를 구현한 뒤 새로고침 404, API 충돌, 빈 화면, 잘못된 redirect 문제를 검수하도록 지원한다.

---

### [핵심]

- Not Found Route
- Catch All Route
- Route Error Handling
- Invalid Parameter
- API 404
- SPA Refresh 404
- Browser Refresh 404
- Direct URL Access
- SPA Fallback
- Spring Boot Fallback
- Nginx try_files
- Static Hosting Rewrite
- API Path Collision
- index.html fallback
- BrowserRouter
- HashRouter
- Blank Page
- MIME Type Error
- JSON 대신 HTML 응답
- Troubleshooting Flow
- Common Mistakes

핵심 원칙:

```text
React Router
→ Browser Client Side Route Matching

Server
→ Static File Serving / API Routing / SPA Fallback

Deployment Review
→ Frontend Route와 Backend API Route 충돌 방지
```

---

### [실무]

2026 실무 기준에서 React Router 오류 검수는 React 코드만 확인하면 부족하다.

React Router 오류는 아래 영역을 함께 확인해야 한다.

- Route path
- Link / NavLink to
- useParams / useSearchParams
- Outlet
- Protected Route redirect
- Not Found Route
- BrowserRouter wrapping
- build output path
- static resource path
- server fallback
- API prefix
- Backend Controller path
- Axios baseURL
- Network response content-type

Troubleshooting 기본 Flow:

```text
Routing Problem
→ Current URL 확인
→ Route Definition 확인
→ Navigation Target 확인
→ Params 확인
→ Outlet 확인
→ Console Error 확인
→ Network Response 확인
→ Server Fallback 확인
→ API Path Collision 확인
```

---

### [FAQ]

Q. React Router 오류는 React 코드만 보면 돼?
A. 아니다. Route 정의, Navigation, Params, Outlet, Server Fallback, API Path Collision까지 함께 확인해야 한다.

Q. 배포 후 새로고침 404는 왜 중요해?
A. BrowserRouter 기반 SPA는 직접 URL 접근 시 서버가 index.html로 fallback해야 정상 렌더링될 수 있기 때문이다.

Q. API 요청했는데 index.html이 응답되는 이유는?
A. SPA Fallback이 API 요청까지 forward했거나 Frontend Route와 Backend API path가 충돌했을 가능성이 있다.

Q. Part06의 핵심은 뭐야?
A. Not Found Route, Route Error Handling, SPA Refresh 404, Fallback, API Path Collision, Troubleshooting이다.

---

# 2. Not Found Route

## 2.1 Not Found Route Concept

### [개념]

Not Found Route는 어떤 Route와도 매칭되지 않은 URL에 대해 404 화면을 보여주는 React Router Route다.

React Router에서는 `path="*"`를 사용해 Catch All Route를 구성한다.

---

### [핵심]

- Not Found Route
- Catch All Route
- `path="*"`
- NotFoundPage
- invalid URL
- unknown route
- fallback UI
- home link
- back button
- SPA 404
- Server 404 구분

기본 예:

```jsx
<Route path="*" element={<NotFoundPage />} />
```

---

### [실무]

NotFoundPage 예:

```jsx
import { Link, useNavigate } from "react-router";

function NotFoundPage() {
  const navigate = useNavigate();

  return (
    <main>
      <h1>페이지를 찾을 수 없습니다.</h1>
      <p>요청한 주소가 존재하지 않거나 이동되었습니다.</p>

      <Link to="/">메인으로 이동</Link>
      <button type="button" onClick={() => navigate(-1)}>
        이전 페이지
      </button>
    </main>
  );
}

export default NotFoundPage;
```

Route 적용:

```jsx
<Routes>
  <Route path="/" element={<MainPage />} />
  <Route path="/festivals" element={<FestivalListPage />} />
  <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
  <Route path="*" element={<NotFoundPage />} />
</Routes>
```

실무 기준:

- 전체 Route 마지막에 Catch All Route 포함
- 잘못된 URL에서 빈 화면 방지
- 메인 이동 Link 제공
- 이전 페이지 버튼 제공 가능
- 서비스 Layout 포함 여부 결정
- SPA 404와 Server 404 차이 인지
- 중첩 Route에서는 local 404와 global 404 구분 가능
- 잘못된 parameter도 NotFoundPage로 보낼 수 있음

---

### [FAQ]

Q. React Router에서 404 페이지는 어떻게 만들어?
A. `path="*"` Route를 추가하고 NotFoundPage를 렌더링한다.

Q. NotFound Route가 없으면 어떻게 돼?
A. 매칭되지 않는 URL에서 빈 화면처럼 보일 수 있다.

Q. SPA 404와 서버 404는 달라?
A. 다르다. SPA 404는 React Router가 매칭 실패를 처리하는 화면이고 서버 404는 서버가 파일이나 경로를 찾지 못한 응답이다.

Q. NotFoundPage에는 어떤 이동을 넣는 게 좋아?
A. 메인으로 이동하는 Link와 이전 페이지 이동 버튼을 제공할 수 있다.

---

## 2.2 Local Not Found Route

### [개념]

Local Not Found Route는 특정 Nested Route 내부에서만 동작하는 하위 404 Route다.

전체 App NotFoundPage와 다르게 특정 Layout 안에서 잘못된 하위 경로를 처리할 수 있다.

---

### [핵심]

- Local Not Found Route
- Nested Route 404
- Layout 내부 404
- Child Route Catch All
- Global Not Found Route
- Local Error UI
- Admin 404
- MyPage 404
- Detail Tab 404

예:

```jsx
<Route path="/mypage" element={<MyPageLayout />}>
  <Route index element={<MyPageHome />} />
  <Route path="profile" element={<ProfilePage />} />
  <Route path="favorites" element={<FavoritePage />} />
  <Route path="*" element={<MyPageNotFoundPage />} />
</Route>
```

---

### [실무]

MyPage local 404:

```jsx
<Route path="/mypage" element={<MyPageLayout />}>
  <Route index element={<MyPageHome />} />
  <Route path="profile" element={<ProfilePage />} />
  <Route path="favorites" element={<FavoritePage />} />
  <Route path="settings" element={<SettingsPage />} />
  <Route path="*" element={<MyPageNotFoundPage />} />
</Route>
```

동작:

```text
/mypage/unknown
→ MyPageLayout
→ Outlet: MyPageNotFoundPage
```

Admin local 404:

```jsx
<Route path="/admin" element={<AdminLayout />}>
  <Route index element={<AdminDashboardPage />} />
  <Route path="users" element={<AdminUserPage />} />
  <Route path="festivals" element={<AdminFestivalPage />} />
  <Route path="*" element={<AdminNotFoundPage />} />
</Route>
```

실무 기준:

- Layout을 유지한 채 하위 404를 보여주고 싶으면 local 404 사용
- 전체 앱에서 완전히 잘못된 URL은 global 404 사용
- local 404와 global 404 기준 통일
- Protected Route 내부 local 404는 인증 후 표시됨
- Admin local 404는 권한 확인 후 표시됨
- 너무 많은 local 404는 구조 복잡도를 높일 수 있음

---

### [FAQ]

Q. Local Not Found Route는 언제 써?
A. MyPage나 Admin처럼 Layout은 유지하고 하위 잘못된 경로만 404로 처리하고 싶을 때 사용한다.

Q. Global Not Found Route와 Local Not Found Route 차이는?
A. Global은 전체 앱에서 매칭 실패를 처리하고 Local은 특정 부모 Route 내부의 하위 매칭 실패를 처리한다.

Q. Admin 내부 404도 따로 만들 수 있어?
A. 가능하다. `/admin` 부모 Route 아래에 `path="*"` child route를 추가하면 된다.

Q. local 404를 무조건 만들어야 해?
A. 아니다. Layout 내부에서 별도 404 UX가 필요할 때만 사용한다.

---

# 3. Route Error Handling

## 3.1 Route Error Handling Concept

### [개념]

Route Error Handling은 URL 매칭, parameter 검증, 권한 확인, API 응답 오류, Component 렌더링 오류를 화면에서 안정적으로 처리하는 기준이다.

React Router Foundation 문서에서는 일반 SPA Routing 기준의 Error UI와 NotFoundPage 중심으로 다룬다.

---

### [핵심]

처리 대상:

- invalid path
- invalid parameter
- missing parameter
- API 404
- API 401
- API 403
- API 500
- network error
- forbidden route
- unauthenticated route
- blank page
- component error
- data loading error

오류 구분:

| 오류          | 의미                | 처리                    |
| ------------- | ------------------- | ----------------------- |
| Route 404     | Route 매칭 실패     | NotFoundPage            |
| Invalid Param | parameter 형식 오류 | NotFoundPage / Error UI |
| API 404       | 리소스 없음         | Resource Not Found UI   |
| API 401       | 인증 필요           | login redirect          |
| API 403       | 권한 부족           | ForbiddenPage           |
| API 500       | 서버 오류           | Error UI                |
| Network Error | 통신 실패           | Retry UI / Error UI     |

---

### [실무]

상세 페이지 parameter 검증:

```jsx
import { useParams } from "react-router";

function FestivalDetailPage() {
  const { festivalId } = useParams();
  const parsedFestivalId = Number(festivalId);

  if (!festivalId || Number.isNaN(parsedFestivalId) || parsedFestivalId <= 0) {
    return <NotFoundPage />;
  }

  return <FestivalDetail festivalId={parsedFestivalId} />;
}
```

API 응답 처리 기준:

```text
GET /api/festivals/123

200
→ Render Detail

404
→ ResourceNotFound UI

401
→ Redirect /login

403
→ Forbidden UI

500
→ Error UI
```

실무 기준:

- URL parameter는 API 호출 전 기본 검증
- Route 404와 API 404 구분
- 401과 403 구분
- 사용자 메시지와 개발자 로그 구분
- Error UI에 복귀 경로 제공
- 새로고침 404는 Route Error가 아니라 Server Fallback 문제일 수 있음
- Data Router errorElement는 별도 심화 문서에서 다룸

---

### [FAQ]

Q. Route Error Handling은 뭐야?
A. 잘못된 URL, parameter, 인증, 권한, API 오류를 적절한 화면으로 처리하는 기준이다.

Q. 잘못된 URL parameter는 어떻게 처리해?
A. Number 변환 실패나 필수 param 누락을 확인하고 NotFoundPage나 Error UI를 보여준다.

Q. API 404와 Route 404는 어떻게 달라?
A. Route 404는 URL이 Route와 매칭되지 않는 경우이고 API 404는 서버 리소스를 찾지 못한 경우다.

Q. API 401과 403은 어떻게 달라?
A. 401은 인증 필요, 403은 인증은 되었지만 권한이 부족한 상태다.

---

## 3.2 Blank Page After Routing

### [개념]

Blank Page After Routing은 URL은 바뀌었지만 화면이 비어 보이는 문제다.

React Router에서 가장 흔한 오류이며 Route path, element, BrowserRouter, Outlet, import, Console Error를 확인해야 한다.

---

### [핵심]

문제:

- Link 클릭 후 빈 화면
- URL은 바뀌지만 Component가 안 보임
- Nested Route에서 Layout만 보임
- NotFoundPage도 안 보임
- 배포 후 특정 경로에서 빈 화면
- Console Error 발생

원인:

- BrowserRouter 누락
- Route path와 Link to 불일치
- Route element 작성 오류
- Component import 오류
- Outlet 누락
- NotFound Route 누락
- 잘못된 basename
- build asset path 문제
- JavaScript runtime error

---

### [실무]

Debug Flow:

```text
Blank Page
→ Console Error 확인
→ Current URL 확인
→ BrowserRouter 확인
→ Routes / Route 확인
→ Route element 확인
→ Link to 확인
→ Component import 확인
→ Outlet 확인
→ NotFound Route 확인
→ Network asset loading 확인
```

잘못된 element 예:

```jsx
<Route path="/login" element={LoginPage} />
```

권장:

```jsx
<Route path="/login" element={<LoginPage />} />
```

Outlet 누락 예:

```jsx
function MyPageLayout() {
  return (
    <main>
      <Sidebar />
      <section>Content</section>
    </main>
  );
}
```

권장:

```jsx
import { Outlet } from "react-router";

function MyPageLayout() {
  return (
    <main>
      <Sidebar />
      <section>
        <Outlet />
      </section>
    </main>
  );
}
```

---

### [FAQ]

Q. URL은 바뀌는데 화면이 안 나와?
A. Route path와 Link to가 맞는지, element가 JSX인지, BrowserRouter와 Outlet이 있는지 확인한다.

Q. Nested Route에서 Layout만 보이고 자식 화면이 안 나와?
A. 부모 Layout Component에 `<Outlet />`이 없을 가능성이 크다.

Q. 빈 화면이면 제일 먼저 뭘 봐?
A. 브라우저 Console Error와 현재 URL, Route 정의를 먼저 확인한다.

Q. NotFoundPage도 안 나오면?
A. BrowserRouter, Routes 구조, JavaScript runtime error, build asset loading 문제를 확인해야 한다.

---

# 4. SPA Refresh 404

## 4.1 SPA Refresh 404 Concept

### [개념]

SPA Refresh 404는 React Router 내부 이동은 정상인데 새로고침하거나 직접 URL로 접근했을 때 서버가 해당 경로 파일을 찾지 못해 404를 반환하는 문제다.

BrowserRouter 기반 SPA에서 배포 후 자주 발생한다.

---

### [핵심]

문제:

- `/festivals/1` 직접 접근 시 404
- `/mypage` 새로고침 시 404
- `/admin/users` 새로고침 시 404
- 로컬 dev server에서는 정상
- 배포 환경에서만 발생
- React Router 이동은 되지만 refresh 실패

원인:

- React Router는 Client Side Router
- 서버는 `/festivals/1` 파일을 찾으려고 함
- 해당 파일이 없음
- index.html fallback 설정 없음
- API path와 SPA path 구분 부족
- Static hosting rewrite 설정 누락

핵심 Flow:

```text
Browser Request /festivals/1
→ Server checks static file /festivals/1
→ File not found
→ Without fallback: 404
→ With fallback: return index.html
→ React Router renders FestivalDetailPage
```

---

### [실무]

정상 Fallback Flow:

```text
Direct URL Access /festivals/1
→ Server receives request
→ Not API
→ Not static asset
→ Return index.html
→ React App loads
→ BrowserRouter reads /festivals/1
→ Route matches /festivals/:festivalId
→ FestivalDetailPage render
```

실무 기준:

- BrowserRouter 사용 시 server fallback 필요
- 개발 서버는 fallback을 자동 처리하는 경우 많음
- 운영 서버는 직접 설정 필요
- Spring Boot 통합 배포 시 forward controller 필요 가능
- Nginx 배포 시 try_files 설정 필요
- Vercel / Netlify / S3 등 Static Hosting은 rewrite 설정 필요
- API path는 fallback에서 제외
- 정적 asset은 fallback에서 제외
- 새로고침 404는 React Router 코드 문제가 아닐 수 있음

---

### [FAQ]

Q. React Router 새로고침 404는 왜 나?
A. 서버가 `/festivals/1` 같은 SPA 경로를 실제 파일로 찾고 index.html로 fallback하지 않아서 발생할 수 있다.

Q. 로컬에서는 되는데 배포 후 새로고침하면 404가 나?
A. 로컬 dev server는 fallback을 처리하지만 배포 서버에는 fallback 설정이 없을 수 있다.

Q. SPA Refresh 404는 React 코드 문제야?
A. 대부분 React 코드보다 배포 서버 fallback 설정 문제다.

Q. BrowserRouter를 쓰면 fallback이 필요한 이유는?
A. URL이 clean path이므로 서버가 직접 접근 요청을 받았을 때 index.html로 돌려줘야 React Router가 처리할 수 있다.

---

## 4.2 Spring Boot Fallback

### [개념]

Spring Boot Fallback은 React build 파일을 Spring Boot static resources에 포함해 통합 배포할 때 SPA 경로를 `index.html`로 forward하는 설정이다.

API 요청과 정적 리소스 요청은 forward하면 안 된다.

---

### [핵심]

- Spring Boot Fallback
- forward:/index.html
- React build
- static resources
- SPA path
- API 제외
- static asset 제외
- Controller path collision
- Browser Refresh 404
- Direct URL Access

기본 원칙:

```text
Frontend Route
→ forward:/index.html

Backend API Route
→ Controller 처리

Static Asset
→ Static Resource 처리
```

---

### [실무]

Spring Boot Fallback 예:

```java
@Controller
public class SpaForwardController {

  @GetMapping(value = {
      "/",
      "/login",
      "/signup",
      "/festivals",
      "/festivals/{id}",
      "/mypage",
      "/mypage/**",
      "/admin",
      "/admin/**"
  })
  public String forward() {
    return "forward:/index.html";
  }
}
```

API prefix 구조 권장:

```text
Frontend Route
/festivals
/festivals/1
/mypage

Backend API
/api/festivals
/api/festivals/1
/api/users/me
```

주의:

- `/api/**`는 forward 대상 제외
- `/static/**`, `/assets/**`, `/favicon.ico`, JS/CSS 파일 제외
- 실제 Backend Controller path와 충돌 금지
- `/festival`과 `/festivals` 혼동 주의
- 모든 요청을 무조건 index.html로 보내면 API가 깨질 수 있음
- Controller fallback 범위는 프로젝트 Route 목록에 맞게 제한
- 정규식 fallback은 신중하게 사용

---

### [FAQ]

Q. Spring Boot에 React build를 넣으면 새로고침 404는 어떻게 해결해?
A. API와 정적 리소스를 제외한 Frontend Route를 `forward:/index.html`로 보내는 fallback Controller를 구성한다.

Q. 모든 요청을 index.html로 보내도 돼?
A. 안 된다. `/api/**`, 정적 리소스, 실제 Backend Controller 경로는 제외해야 한다.

Q. API 요청했는데 index.html이 응답돼?
A. fallback Controller가 API 요청까지 forward하고 있을 가능성이 있다.

Q. Spring Boot Fallback에서 가장 중요한 것은?
A. Frontend Route만 forward하고 Backend API와 static asset은 제외하는 것이다.

---

## 4.3 Nginx Fallback

### [개념]

Nginx Fallback은 React SPA를 Nginx로 배포할 때 직접 URL 접근과 새로고침을 지원하기 위해 unknown path를 index.html로 돌려주는 설정이다.

BrowserRouter 기반 SPA에서는 `try_files` 설정을 자주 사용한다.

---

### [핵심]

- Nginx Fallback
- try_files
- index.html
- SPA refresh
- static file serving
- API proxy
- location block
- BrowserRouter
- Direct URL Access

기본 예:

```nginx
location / {
  try_files $uri $uri/ /index.html;
}
```

API proxy 예:

```nginx
location /api/ {
  proxy_pass http://backend:8080/api/;
}
```

---

### [실무]

React SPA + Backend API 예:

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

실무 기준:

- `/api/` location을 먼저 분리
- static file은 실제 파일로 제공
- 나머지 SPA route는 index.html fallback
- API proxy와 SPA fallback 순서 확인
- MIME type 오류 발생 시 JS/CSS asset path 확인
- base path 배포 시 basename / public path 확인
- Docker / reverse proxy 환경에서는 backend 주소 확인

주의:

- API 요청이 index.html로 fallback되지 않게 함
- JS/CSS asset이 index.html로 응답되면 MIME type error 발생 가능
- root 경로와 build 파일 위치 확인
- React Router basename 사용 여부 확인

---

### [FAQ]

Q. Nginx에서 React Router 새로고침 404는 어떻게 해결해?
A. `location / { try_files $uri $uri/ /index.html; }` 설정으로 SPA fallback을 구성한다.

Q. Nginx에서 API와 SPA Route는 어떻게 구분해?
A. `/api/` location을 별도로 두고 나머지 요청은 SPA fallback으로 처리한다.

Q. JS 파일 요청에 index.html이 응답돼?
A. static asset 경로, root 설정, try_files 설정을 확인해야 한다.

Q. Nginx Fallback에서 가장 중요한 것은?
A. API 요청은 backend로 보내고 SPA 화면 경로만 index.html로 fallback하는 것이다.

---

## 4.4 Static Hosting Rewrite

### [개념]

Static Hosting Rewrite는 Netlify, Vercel, S3, CloudFront 같은 정적 호스팅 환경에서 SPA 경로를 index.html로 rewrite하는 설정이다.

BrowserRouter를 사용하는 React SPA는 직접 URL 접근 시 rewrite 설정이 필요할 수 있다.

---

### [핵심]

- Static Hosting Rewrite
- SPA Rewrite
- index.html fallback
- Netlify redirect
- Vercel rewrite
- S3 error document
- CloudFront custom error response
- BrowserRouter
- Direct URL Access

예시 개념:

```text
/festivals/1
→ index.html
→ React Router handles /festivals/1
```

---

### [실무]

Netlify `_redirects` 예:

```text
/*    /index.html   200
```

Vercel rewrite 예:

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

S3 / CloudFront 기준:

```text
S3 Static Website
→ Error document index.html 설정 가능

CloudFront
→ 403 / 404 Custom Error Response
→ /index.html
→ 200 or configured status
```

실무 기준:

- 호스팅 플랫폼별 rewrite 방식 확인
- API proxy가 있다면 API path 제외
- static asset이 정상 응답되는지 확인
- React Router basename이 필요한지 확인
- 404 상태 코드와 SPA fallback UX 구분
- SEO가 중요하면 SSR / SSG 전략 검토

---

### [FAQ]

Q. 정적 호스팅에서 React Router 새로고침 404는 어떻게 해결해?
A. 모든 SPA 경로를 index.html로 rewrite하도록 플랫폼별 설정을 추가한다.

Q. Netlify에서는 어떻게 설정해?
A. `_redirects` 파일에 `/* /index.html 200` 형태의 rewrite를 사용할 수 있다.

Q. Vercel에서는 어떻게 설정해?
A. rewrites 설정으로 모든 SPA path를 index.html로 보낼 수 있다.

Q. S3 배포에서도 fallback이 필요해?
A. BrowserRouter를 사용한다면 직접 URL 접근을 위해 error document나 CloudFront custom error response 설정이 필요할 수 있다.

---

# 5. API Path Collision

## 5.1 API Path Collision Concept

### [개념]

API Path Collision은 Frontend Route path와 Backend API path가 겹쳐 요청이 잘못 처리되는 문제다.

React Router SPA와 Backend API를 같은 도메인에서 운영할 때 자주 발생한다.

---

### [핵심]

문제:

- React Route로 이동하려는데 Backend Controller가 잡음
- API 요청이 index.html을 반환함
- JSON을 기대했는데 HTML 응답
- 새로고침 시 잘못된 Controller 매칭
- MIME type error
- 404 또는 500 발생
- `/festival`과 `/festivals` 경로 혼동
- fallback Controller 범위 과다

원인:

- Frontend Route와 Backend API path prefix 혼용
- API prefix 없음
- fallback Controller가 API 요청까지 forward
- Axios baseURL과 React Router path 혼동
- Controller path와 SPA path가 동일
- 정적 리소스 요청까지 fallback 처리

---

### [실무]

권장 구조:

```text
Frontend Route
/
 /login
 /signup
 /festivals
 /festivals/1
 /calendar
 /mypage

Backend API
/api/auth/login
/api/users/me
/api/festivals
/api/festivals/1
/api/calendar/monthly
```

충돌 위험 구조:

```text
Frontend Route
/festival

Backend API
/festival
```

문제:

```text
GET /festival
→ 화면 요청인지 API 요청인지 모호함
```

권장:

```text
GET /festivals
→ Frontend 화면

GET /api/festivals
→ Backend API
```

실무 기준:

- Backend API는 `/api` prefix 권장
- Frontend Route는 화면 URL로 분리
- Axios baseURL은 API 기준으로 설정
- React Router path와 API endpoint를 혼동하지 않음
- fallback 대상에서 `/api/**` 제외
- Network response content-type 확인
- JSON 대신 HTML이 오면 path collision 의심

---

### [FAQ]

Q. API Path Collision은 뭐야?
A. Frontend Route와 Backend API path가 겹쳐 요청이 잘못 처리되는 문제다.

Q. API 요청했는데 index.html이 응답돼?
A. SPA fallback Controller가 API 요청까지 forward하고 있을 가능성이 있다. API path를 fallback에서 제외해야 한다.

Q. Frontend Route와 Backend API 경로는 어떻게 구분해?
A. Backend API는 `/api` prefix를 두고 Frontend Route는 화면 URL로 분리하는 것이 안전하다.

Q. JSON을 기대했는데 HTML이 응답돼?
A. API 요청이 SPA fallback에 걸려 index.html을 받은 것일 수 있다.

---

## 5.2 Axios Path and Router Path Confusion

### [개념]

Axios Path와 Router Path Confusion은 API 요청 URL과 React Router 화면 URL을 혼동하는 문제다.

React Router의 `path`는 화면 경로이고 Axios의 URL은 Backend API 요청 경로다.

---

### [핵심]

- Axios URL
- React Router path
- API endpoint
- Frontend Route
- baseURL
- publicApi
- authApi
- JSON response
- HTML response
- Network tab
- Path confusion

구분:

```text
React Router
→ <Route path="/festivals" element={<FestivalListPage />} />

Axios
→ publicApi.get("/api/festivals")
```

또는 baseURL 사용:

```text
Axios baseURL = /api

publicApi.get("/festivals")
→ GET /api/festivals
```

---

### [실무]

Route 예:

```jsx
<Route path="/festivals" element={<FestivalListPage />} />
```

Axios 예:

```javascript
publicApi.get("/festivals");
```

baseURL이 `/api`라면 실제 요청:

```text
GET /api/festivals
```

혼동 예:

```javascript
navigate("/api/festivals");
```

문제:

```text
API endpoint로 화면 이동 시도
```

혼동 예:

```javascript
publicApi.get("/festivals");
```

주의:

```text
baseURL이 없으면 GET /festivals 요청
Frontend Route와 충돌 가능
```

실무 기준:

- Router path와 API endpoint를 명확히 구분
- Axios instance baseURL 확인
- publicApi / authApi 역할 확인
- API 요청은 Network tab에서 status와 content-type 확인
- React 화면 이동은 Link / navigate 사용
- 데이터 요청은 Axios / fetch 사용
- `/calendar/monthly`가 화면 Route인지 API인지 구분
- API prefix 정책을 프로젝트 전체에서 통일

---

### [FAQ]

Q. React Router path와 Axios URL은 같은 거야?
A. 아니다. React Router path는 화면 URL이고 Axios URL은 Backend API 요청 URL이다.

Q. navigate로 API endpoint에 이동해도 돼?
A. 아니다. API endpoint는 화면 이동 대상이 아니라 데이터 요청 대상이다.

Q. Axios 요청이 Frontend Route로 가는 것 같아?
A. Axios baseURL과 요청 URL, 서버 fallback, Network 응답 content-type을 확인해야 한다.

Q. publicApi.get("/festivals")는 어디로 요청돼?
A. Axios baseURL에 따라 다르다. baseURL이 `/api`면 `/api/festivals`로 요청된다.

---

# 6. BrowserRouter vs HashRouter

## 6.1 BrowserRouter and HashRouter Comparison

### [개념]

BrowserRouter는 History API를 사용해 clean URL을 제공한다.

HashRouter는 URL hash(`#`) 뒤의 경로를 사용하므로 서버 fallback 문제를 줄일 수 있지만 URL 품질이 낮아질 수 있다.

---

### [핵심]

| 비교          | BrowserRouter  | HashRouter                           |
| ------------- | -------------- | ------------------------------------ |
| URL           | `/festivals/1` | `/#/festivals/1`                     |
| 방식          | History API    | URL hash                             |
| 서버 fallback | 필요 가능      | 상대적으로 덜 필요                   |
| URL 품질      | 좋음           | 낮음                                 |
| 실무 권장     | 일반 SPA 권장  | fallback 설정이 어려운 환경에서 고려 |
| SEO           | Hash URL 불리  | 더 불리                              |
| 배포          | 서버 설정 필요 | 단순 정적 배포에 유리할 수 있음      |

선택 기준:

```text
일반 서비스 / 서버 설정 가능
→ BrowserRouter

서버 fallback 설정 불가 / 단순 파일 배포
→ HashRouter 검토
```

---

### [실무]

BrowserRouter 예:

```jsx
import { BrowserRouter } from "react-router";

<BrowserRouter>
  <App />
</BrowserRouter>;
```

HashRouter 예:

```jsx
import { HashRouter } from "react-router";

<HashRouter>
  <App />
</HashRouter>;
```

실무 기준:

- 기본은 BrowserRouter 권장
- 배포 서버 fallback 설정 가능하면 BrowserRouter 사용
- HashRouter는 URL에 `#`이 포함됨
- 외부 공유 URL 품질 고려
- OAuth Redirect URL, Kakao Login Redirect URL 같은 외부 연동 시 URL 정책 확인
- SEO가 중요하면 SSR / SSG 또는 Framework 전략 검토
- HashRouter는 fallback 문제를 회피할 수 있지만 근본적 서버 구성 능력을 대체하지 않음

---

### [FAQ]

Q. BrowserRouter와 HashRouter 차이는?
A. BrowserRouter는 clean URL을 쓰고 서버 fallback이 필요할 수 있으며 HashRouter는 `#` 기반 URL을 써서 fallback 문제를 줄일 수 있다.

Q. BrowserRouter 대신 HashRouter를 쓰면 새로고침 404가 해결돼?
A. 일부 환경에서는 해결될 수 있지만 URL에 `#`이 들어가므로 가능하면 서버 fallback을 설정하는 것이 좋다.

Q. 실무에서는 BrowserRouter와 HashRouter 중 뭐가 좋아?
A. 일반적으로 BrowserRouter가 URL 품질이 좋아 선호된다.

Q. HashRouter는 언제 고려해?
A. 서버 fallback 설정이 불가능한 단순 정적 배포 환경에서 고려할 수 있다.

---

# 7. Data Router Error Awareness

## 7.1 Data Router Error Basics Mention

### [개념]

React Router Data Router는 loader, action, errorElement를 통해 Route 단위 데이터 로딩과 오류 처리를 구조화할 수 있다.

Foundation 문서에서는 개념만 언급하고 심화는 Data Fetching 또는 Advanced React Router 문서에서 다룬다.

---

### [핵심]

- Data Router
- createBrowserRouter
- RouterProvider
- loader
- action
- errorElement
- route object
- data loading error
- submission error
- Error Boundary
- Framework Mode Awareness

기초 예:

```jsx
import { createBrowserRouter, RouterProvider } from "react-router";

const router = createBrowserRouter([
  {
    path: "/",
    element: <MainPage />,
    errorElement: <ErrorPage />,
  },
]);

function App() {
  return <RouterProvider router={router} />;
}
```

---

### [실무]

실무 기준:

- Foundation 단계는 BrowserRouter + Routes + Route 중심
- Data Router는 loader / action 설계가 필요
- 기존 useEffect + Axios 데이터 요청과 역할 구분
- errorElement는 Data Router 오류 처리에 사용 가능
- BrowserRouter 방식과 RouterProvider 방식 혼용 금지
- Framework Mode 심화는 별도 문서로 분리
- 프로젝트 요구사항과 팀 숙련도에 따라 선택

주의:

```text
BrowserRouter 방식
→ <BrowserRouter><App /></BrowserRouter>

Data Router 방식
→ createBrowserRouter + <RouterProvider router={router} />

일반적으로 두 방식을 혼용하지 않음
```

---

### [FAQ]

Q. errorElement는 뭐야?
A. Data Router에서 Route 단위 오류 화면을 지정하는 기능이다.

Q. BrowserRouter와 RouterProvider를 같이 써?
A. 일반적으로 같이 쓰지 않는다. BrowserRouter 방식과 createBrowserRouter / RouterProvider 방식 중 하나를 선택한다.

Q. loader와 action은 여기서 깊게 다뤄?
A. 아니다. Foundation 문서에서는 개념만 다루고 Data Fetching 또는 Advanced 문서에서 심화한다.

Q. 일반 SPA에서는 꼭 Data Router를 써야 해?
A. 아니다. BrowserRouter + Routes + Route 방식으로도 기본 SPA Routing은 충분히 구현할 수 있다.

---

# 8. Troubleshooting Playbook

## 8.1 React Router Debug Flow

### [개념]

React Router Debug Flow는 Routing 문제를 URL, Route 정의, Navigation, Params, Layout, Server Response 순서로 확인하는 절차다.

문제를 영역별로 나누면 원인 추적이 쉬워진다.

---

### [핵심]

검수 순서:

```text
1. URL 확인
2. Route path 확인
3. Link / NavLink / navigate target 확인
4. BrowserRouter 확인
5. Route element 확인
6. useParams / useSearchParams 확인
7. Outlet 확인
8. Protected Route 조건 확인
9. NotFound Route 확인
10. Console Error 확인
11. Network Response 확인
12. Server Fallback 확인
13. API Path Collision 확인
```

---

### [실무]

문제별 빠른 진단:

```text
URL은 바뀌는데 빈 화면
→ Route path / element / Console / Outlet 확인

Nested Route 자식이 안 보임
→ Parent Layout Outlet 확인

useParams undefined
→ Route param name / Link actual URL 확인

검색 조건이 사라짐
→ setSearchParams 기존 params 보존 확인

로그인했는데 login으로 이동
→ auth loading / authenticated 복원 확인

관리자인데 forbidden
→ role naming / role loading 확인

새로고침 404
→ server fallback 확인

API 요청에 index.html 응답
→ API Path Collision / fallback 범위 확인

JS/CSS MIME type error
→ static asset path / fallback 설정 확인
```

실무 기준:

- Console Error와 Network tab을 먼저 확인
- React 코드 문제와 서버 설정 문제를 분리
- API 응답 content-type 확인
- status code와 response body 확인
- 배포 환경에서만 발생하면 fallback / asset path 우선 의심
- Route path와 API endpoint를 별도로 기록

---

### [FAQ]

Q. React Router 문제는 어떤 순서로 디버깅해?
A. URL, Route path, Navigation target, BrowserRouter, element, params, Outlet, Console, Network, Server Fallback 순서로 확인한다.

Q. 배포 환경에서만 문제면 뭘 먼저 봐?
A. 서버 fallback, static asset path, API proxy, Network response를 먼저 확인한다.

Q. Network tab에서는 뭘 봐?
A. 요청 URL, status code, response content-type, response body가 기대한 JSON/JS/CSS/HTML인지 확인한다.

Q. Console Error는 왜 중요해?
A. Component import 오류, runtime error, Router context 오류, MIME type error를 빠르게 확인할 수 있기 때문이다.

---

## 8.2 Common Error Matrix

### [개념]

Common Error Matrix는 React Router에서 자주 발생하는 증상, 원인, 해결 기준을 빠르게 매칭하는 표다.

RAG Retrieval에서 사용자 오류 질문과 해결책을 연결하기 위해 사용한다.

---

### [핵심]

| 증상                     | 가능 원인                            | 확인 / 해결                      |
| ------------------------ | ------------------------------------ | -------------------------------- |
| URL은 바뀌는데 빈 화면   | Route path 불일치, element 오류      | Route / Console 확인             |
| Nested 자식 화면 안 보임 | Outlet 누락                          | 부모 Layout에 Outlet 추가        |
| useParams undefined      | param 이름 불일치                    | Route param과 useParams key 통일 |
| 검색 query 사라짐        | setSearchParams가 기존 params 덮어씀 | URLSearchParams 복사 후 수정     |
| 새로고침 404             | server fallback 없음                 | index.html fallback 설정         |
| API가 HTML 응답          | fallback이 API 가로챔                | `/api/**` 제외                   |
| JS MIME type error       | asset 요청이 index.html 응답         | static path / fallback 확인      |
| 관리자도 forbidden       | role naming 불일치                   | ROLE_ADMIN 기준 통일             |
| login redirect 반복      | auth loading 누락                    | loading 중 redirect 금지         |
| 뒤로가면 login 복귀      | replace 옵션 누락                    | Navigate replace 적용            |
| 외부 링크 이동 이상      | Link로 외부 URL 이동                 | a 태그 사용                      |
| 내부 이동 reload         | a href 사용                          | Link 사용                        |

---

### [실무]

대표 문제 해결 예:

```text
문제: /festivals/1 새로고침 404
원인: 서버가 /festivals/1 파일을 찾음
해결: SPA fallback으로 index.html 반환
```

```text
문제: GET /api/festivals 응답이 index.html
원인: fallback Controller가 /api/**도 forward함
해결: API path를 fallback에서 제외
```

```text
문제: /mypage/profile에서 profile 화면이 안 나옴
원인: MyPageLayout에 Outlet 없음
해결: content 영역에 <Outlet /> 추가
```

```text
문제: 축제 상세 festivalId가 undefined
원인: Route path는 :id인데 useParams는 festivalId
해결: param 이름 통일
```

실무 기준:

- 증상별 가능 원인을 좁혀 확인
- 한 번에 모든 코드를 수정하지 않음
- URL / Console / Network 증거 기반으로 판단
- 배포 문제와 React 코드 문제를 분리
- fallback 수정 후 API 응답도 함께 재검증

---

### [FAQ]

Q. React Router 오류를 빠르게 찾는 방법은?
A. 증상을 먼저 분류하고 URL, Console, Network, Route 정의를 기준으로 원인을 좁힌다.

Q. 새로고침 404와 NotFoundPage는 같은 문제야?
A. 아니다. 새로고침 404는 서버 fallback 문제이고 NotFoundPage는 React Router 매칭 실패 화면이다.

Q. API가 HTML을 반환하면 무슨 문제야?
A. API 요청이 SPA fallback에 걸려 index.html을 받은 것일 가능성이 크다.

Q. Nested Route 문제는 가장 먼저 뭘 봐?
A. 부모 Layout에 Outlet이 있는지 확인한다.

---

# 9. Deployment Review Checklist

## 9.1 SPA Deployment Checklist

### [개념]

SPA Deployment Checklist는 React Router 기반 앱을 배포하기 전 direct URL access, refresh, API 요청, static asset, fallback 설정을 검수하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] BrowserRouter 사용 여부를 확인했는가?
- [ ] 배포 서버에 index.html fallback 설정이 있는가?
- [ ] `/` 직접 접근이 정상인가?
- [ ] `/login` 직접 접근이 정상인가?
- [ ] `/festivals` 직접 접근이 정상인가?
- [ ] `/festivals/1` 직접 접근이 정상인가?
- [ ] `/mypage` 직접 접근이 정상인가?
- [ ] Nested Route 직접 접근이 정상인가?
- [ ] 새로고침 시 404가 발생하지 않는가?
- [ ] `/api/**` 요청이 fallback되지 않는가?
- [ ] API 응답 content-type이 JSON인가?
- [ ] JS/CSS asset 요청이 정상인가?
- [ ] favicon / image asset 요청이 정상인가?
- [ ] Nginx try_files 또는 Spring Boot forward 설정이 적절한가?
- [ ] Static hosting rewrite 설정이 적용되었는가?
- [ ] Frontend Route와 Backend API path가 충돌하지 않는가?
- [ ] Axios baseURL이 운영 환경과 맞는가?
- [ ] Protected Route 새로고침 후 auth state 복원이 되는가?
- [ ] Admin Route 새로고침 후 role loading 문제가 없는가?
- [ ] NotFoundPage가 정상 표시되는가?
```

---

### [실무]

배포 테스트 Flow:

```text
Build
→ Deploy
→ Open Root /
→ Direct Access Deep Link
→ Refresh Deep Link
→ Test API Request
→ Check Static Assets
→ Test Protected Route Refresh
→ Test Admin Route Refresh
→ Test Unknown Route
→ Check Network Content-Type
→ Check Console Error
```

필수 테스트 URL 예:

```text
/
 /login
 /signup
 /festivals
 /festivals/1
 /mypage
 /mypage/profile
 /admin
 /unknown-route
 /api/festivals
```

실무 기준:

- 화면 Route 직접 접근 테스트
- 화면 Route 새로고침 테스트
- API URL 직접 호출 테스트
- Network tab에서 API가 JSON인지 확인
- JS/CSS가 text/html로 응답되지 않는지 확인
- fallback이 너무 넓거나 좁지 않은지 확인
- 배포 서버 로그 확인
- 인증 Route는 새로고침 auth 복원까지 확인

---

### [FAQ]

Q. React Router 앱 배포 후 뭘 테스트해야 해?
A. 직접 URL 접근, 새로고침, API 요청, static asset 응답, NotFoundPage, Protected Route 복원을 테스트해야 한다.

Q. `/festivals/1` 직접 접근 테스트가 왜 필요해?
A. BrowserRouter deep link가 서버 fallback 없이 404가 날 수 있기 때문이다.

Q. API URL도 직접 확인해야 해?
A. 필요하다. API 요청이 index.html로 fallback되지 않고 JSON을 반환하는지 확인해야 한다.

Q. JS/CSS 응답도 확인해야 해?
A. 필요하다. asset 요청이 index.html을 받으면 MIME type error가 발생할 수 있다.

---

# 10. Final React Router Review

## 10.1 Part06 Checklist

### [개념]

Part06 Checklist는 React Router Error Deployment Troubleshooting 문서가 오류 처리와 배포 검수 기준을 충분히 포함했는지 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] Not Found Route 개념이 포함되었는가?
- [ ] Catch All Route 예제가 포함되었는가?
- [ ] Local Not Found Route 기준이 포함되었는가?
- [ ] Route Error Handling 기준이 포함되었는가?
- [ ] API 401 / 403 / 404 / 500 구분이 포함되었는가?
- [ ] Blank Page After Routing이 포함되었는가?
- [ ] SPA Refresh 404 개념이 포함되었는가?
- [ ] BrowserRouter와 server fallback 관계가 포함되었는가?
- [ ] Spring Boot Fallback 예제가 포함되었는가?
- [ ] Nginx Fallback 예제가 포함되었는가?
- [ ] Static Hosting Rewrite 기준이 포함되었는가?
- [ ] API Path Collision이 포함되었는가?
- [ ] Axios Path와 Router Path 구분이 포함되었는가?
- [ ] BrowserRouter vs HashRouter 비교가 포함되었는가?
- [ ] Data Router Error Awareness가 포함되었는가?
- [ ] Troubleshooting Playbook이 포함되었는가?
- [ ] Common Error Matrix가 포함되었는가?
- [ ] Deployment Review Checklist가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Not Found Route Check
→ Route Error Handling Check
→ Blank Page Check
→ SPA Refresh 404 Check
→ Spring Boot Fallback Check
→ Nginx Fallback Check
→ Static Hosting Rewrite Check
→ API Path Collision Check
→ Axios Path Check
→ HashRouter Comparison Check
→ Troubleshooting Matrix Check
→ Deployment Checklist Check
→ FAQ Check
→ Retrieval Queries Check
→ Final Review
```

---

### [FAQ]

Q. Part06 검수에서 가장 중요한 것은?
A. SPA Refresh 404, server fallback, API Path Collision, Network response 검수 기준이다.

Q. Part06에서 Data Router를 깊게 다뤄?
A. 아니다. errorElement 개념만 언급하고 심화는 Data Router 또는 Advanced 문서에서 다룬다.

Q. Part06은 React Router 시리즈의 마지막 파트야?
A. React Router Foundation 기준으로는 마지막 파트이며 이후 State Management, Data Fetching, Authentication Frontend Flow로 이어진다.

---

# 11. React Router Final Common Mistakes

## 11.1 Common Mistakes

### [개념]

React Router 전체에서 자주 발생하는 실수는 Route path 불일치, Router Context 누락, Params 검증 누락, Outlet 누락, Protected Route 오판, Server Fallback 누락이다.

---

### [핵심]

자주 발생:

- BrowserRouter로 App을 감싸지 않음
- Router Hook을 Router 밖에서 사용
- BrowserRouter와 RouterProvider 혼용
- Route element에 JSX Element가 아닌 Component 참조를 잘못 전달
- Route path와 Link to 불일치
- Dynamic Route pattern을 Link to에 그대로 사용
- useParams param 이름 불일치
- useParams 문자열을 숫자로 변환하지 않음
- Query String과 Component State 동기화 실패
- setSearchParams에서 기존 params 삭제
- Nested Route 부모에 Outlet 누락
- Index Route에 path 사용
- Layout Component에 모든 Page 로직 집중
- NotFound Route 누락
- auth loading 없이 Protected Route redirect
- ROLE_ADMIN / ADMIN 혼용
- Frontend Guard만으로 보안이 된다고 착각
- 401과 403 혼동
- BrowserRouter 배포 fallback 누락
- 모든 요청을 index.html로 forward
- API 요청이 index.html 응답
- JS/CSS asset 요청이 index.html 응답
- React Router v5 문법과 v6+ 문법 혼용
- `react-router` / `react-router-dom` import 혼용
- Axios API URL과 React Router path 혼동

---

### [실무]

최종 Review Flow:

```text
React Router Final Review
→ Version / Import Check
→ BrowserRouter Check
→ Route Definition Check
→ Navigation Check
→ Params Check
→ Search Params Check
→ Nested Outlet Check
→ Protected Route Check
→ Not Found Check
→ Error Handling Check
→ Deployment Fallback Check
→ API Collision Check
→ Network Response Check
```

최종 Agent 검수 기준:

```text
Can User Navigate?
Can User Refresh?
Can User Directly Access Deep Link?
Can Route Params Be Read?
Can Search Params Persist?
Can Nested Pages Render?
Can Protected Route Wait For Loading?
Can Admin Route Check ROLE_ADMIN?
Can NotFoundPage Render?
Can API Return JSON?
Can Static Assets Load?
```

---

### [FAQ]

Q. React Router 전체에서 가장 흔한 실수는?
A. BrowserRouter 누락, path 불일치, useParams 이름 불일치, Outlet 누락, 새로고침 404, API Path Collision이다.

Q. 배포 전 최종 검수에서 가장 중요한 것은?
A. deep link 직접 접근, 새로고침, API JSON 응답, static asset 로딩, Protected Route 새로고침 복원이다.

Q. React Router 문제를 해결할 때 가장 중요한 태도는?
A. React 코드 문제와 서버 fallback 문제를 분리해서 확인하는 것이다.

Q. React Router 다음 Domain 문서는 뭐가 좋아?
A. State Management, Data Fetching & REST API Integration, Authentication Frontend Flow, Error Handling & Loading UX 순서가 좋다.

---

# Retrieval Queries

### [FAQ]

Q. React Router Part06은 뭘 다뤄?
A. Not Found Route, Route Error Handling, SPA Refresh 404, Spring Boot Fallback, Nginx Fallback, API Path Collision, Troubleshooting을 다룬다.

Q. Not Found Route는 뭐야?
A. 어떤 Route와도 매칭되지 않은 URL에 대해 404 화면을 보여주는 React Router Route다.

Q. React Router에서 404 페이지는 어떻게 만들어?
A. `path="*"` Route를 추가하고 NotFoundPage를 렌더링한다.

Q. Catch All Route는 뭐야?
A. 매칭되지 않는 모든 Route를 잡아 NotFoundPage 같은 fallback 화면을 보여주는 Route다.

Q. NotFound Route가 없으면 어떻게 돼?
A. 매칭되지 않는 URL에서 빈 화면처럼 보일 수 있다.

Q. SPA 404와 서버 404는 달라?
A. 다르다. SPA 404는 React Router가 매칭 실패를 처리하는 화면이고 서버 404는 서버가 파일이나 경로를 찾지 못한 응답이다.

Q. Local Not Found Route는 언제 써?
A. MyPage나 Admin처럼 Layout은 유지하고 하위 잘못된 경로만 404로 처리하고 싶을 때 사용한다.

Q. Global Not Found Route와 Local Not Found Route 차이는?
A. Global은 전체 앱에서 매칭 실패를 처리하고 Local은 특정 부모 Route 내부의 하위 매칭 실패를 처리한다.

Q. Admin 내부 404도 따로 만들 수 있어?
A. 가능하다. `/admin` 부모 Route 아래에 `path="*"` child route를 추가하면 된다.

Q. Route Error Handling은 뭐야?
A. 잘못된 URL, parameter, 인증, 권한, API 오류를 적절한 화면으로 처리하는 기준이다.

Q. 잘못된 URL parameter는 어떻게 처리해?
A. Number 변환 실패나 필수 param 누락을 확인하고 NotFoundPage나 Error UI를 보여준다.

Q. API 404와 Route 404는 어떻게 달라?
A. Route 404는 URL이 Route와 매칭되지 않는 경우이고 API 404는 서버 리소스를 찾지 못한 경우다.

Q. API 401과 403은 어떻게 달라?
A. 401은 인증 필요, 403은 인증은 되었지만 권한이 부족한 상태다.

Q. URL은 바뀌는데 화면이 안 나와?
A. Route path와 Link to가 맞는지, element가 JSX인지, BrowserRouter와 Outlet이 있는지 확인한다.

Q. Nested Route에서 Layout만 보이고 자식 화면이 안 나와?
A. 부모 Layout Component에 `<Outlet />`이 없을 가능성이 크다.

Q. 빈 화면이면 제일 먼저 뭘 봐?
A. 브라우저 Console Error와 현재 URL, Route 정의를 먼저 확인한다.

Q. NotFoundPage도 안 나오면?
A. BrowserRouter, Routes 구조, JavaScript runtime error, build asset loading 문제를 확인해야 한다.

Q. SPA Refresh 404는 뭐야?
A. React Router 내부 이동은 정상인데 새로고침하거나 직접 URL 접근 시 서버가 해당 경로 파일을 찾지 못해 404를 반환하는 문제다.

Q. React Router 새로고침 404는 왜 나?
A. 서버가 `/festivals/1` 같은 SPA 경로를 실제 파일로 찾고 index.html로 fallback하지 않아서 발생할 수 있다.

Q. 로컬에서는 되는데 배포 후 새로고침하면 404가 나?
A. 로컬 dev server는 fallback을 처리하지만 배포 서버에는 fallback 설정이 없을 수 있다.

Q. SPA Refresh 404는 React 코드 문제야?
A. 대부분 React 코드보다 배포 서버 fallback 설정 문제다.

Q. BrowserRouter를 쓰면 fallback이 필요한 이유는?
A. URL이 clean path이므로 서버가 직접 접근 요청을 받았을 때 index.html로 돌려줘야 React Router가 처리할 수 있다.

Q. Spring Boot에 React build를 넣으면 새로고침 404는 어떻게 해결해?
A. API와 정적 리소스를 제외한 Frontend Route를 `forward:/index.html`로 보내는 fallback Controller를 구성한다.

Q. Spring Boot Fallback은 뭐야?
A. React build를 Spring Boot static resources에 포함해 통합 배포할 때 SPA 경로를 index.html로 forward하는 설정이다.

Q. Spring Boot Fallback에서 모든 요청을 index.html로 보내도 돼?
A. 안 된다. `/api/**`, 정적 리소스, 실제 Backend Controller 경로는 제외해야 한다.

Q. Spring Boot Fallback에서 가장 중요한 것은?
A. Frontend Route만 forward하고 Backend API와 static asset은 제외하는 것이다.

Q. Nginx에서 React Router 새로고침 404는 어떻게 해결해?
A. `location / { try_files $uri $uri/ /index.html; }` 설정으로 SPA fallback을 구성한다.

Q. Nginx에서 API와 SPA Route는 어떻게 구분해?
A. `/api/` location을 별도로 두고 나머지 요청은 SPA fallback으로 처리한다.

Q. JS 파일 요청에 index.html이 응답돼?
A. static asset 경로, root 설정, try_files 설정을 확인해야 한다.

Q. Nginx Fallback에서 가장 중요한 것은?
A. API 요청은 backend로 보내고 SPA 화면 경로만 index.html로 fallback하는 것이다.

Q. 정적 호스팅에서 React Router 새로고침 404는 어떻게 해결해?
A. 모든 SPA 경로를 index.html로 rewrite하도록 플랫폼별 설정을 추가한다.

Q. Netlify에서는 React Router fallback을 어떻게 설정해?
A. `_redirects` 파일에 `/* /index.html 200` 형태의 rewrite를 사용할 수 있다.

Q. Vercel에서는 React Router fallback을 어떻게 설정해?
A. rewrites 설정으로 모든 SPA path를 index.html로 보낼 수 있다.

Q. S3 배포에서도 fallback이 필요해?
A. BrowserRouter를 사용한다면 직접 URL 접근을 위해 error document나 CloudFront custom error response 설정이 필요할 수 있다.

Q. API Path Collision은 뭐야?
A. Frontend Route와 Backend API path가 겹쳐 요청이 잘못 처리되는 문제다.

Q. API 요청했는데 index.html이 응답돼?
A. SPA fallback Controller가 API 요청까지 forward하고 있을 가능성이 있다. API path를 fallback에서 제외해야 한다.

Q. Frontend Route와 Backend API 경로는 어떻게 구분해?
A. Backend API는 `/api` prefix를 두고 Frontend Route는 화면 URL로 분리하는 것이 안전하다.

Q. JSON을 기대했는데 HTML이 응답돼?
A. API 요청이 SPA fallback에 걸려 index.html을 받은 것일 수 있다.

Q. React Router path와 Axios URL은 같은 거야?
A. 아니다. React Router path는 화면 URL이고 Axios URL은 Backend API 요청 URL이다.

Q. navigate로 API endpoint에 이동해도 돼?
A. 아니다. API endpoint는 화면 이동 대상이 아니라 데이터 요청 대상이다.

Q. Axios 요청이 Frontend Route로 가는 것 같아?
A. Axios baseURL과 요청 URL, 서버 fallback, Network 응답 content-type을 확인해야 한다.

Q. publicApi.get("/festivals")는 어디로 요청돼?
A. Axios baseURL에 따라 다르다. baseURL이 `/api`면 `/api/festivals`로 요청된다.

Q. BrowserRouter와 HashRouter 차이는?
A. BrowserRouter는 clean URL을 쓰고 서버 fallback이 필요할 수 있으며 HashRouter는 `#` 기반 URL을 써서 fallback 문제를 줄일 수 있다.

Q. BrowserRouter 대신 HashRouter를 쓰면 새로고침 404가 해결돼?
A. 일부 환경에서는 해결될 수 있지만 URL에 `#`이 들어가므로 가능하면 서버 fallback을 설정하는 것이 좋다.

Q. 실무에서는 BrowserRouter와 HashRouter 중 뭐가 좋아?
A. 일반적으로 BrowserRouter가 URL 품질이 좋아 선호된다.

Q. HashRouter는 언제 고려해?
A. 서버 fallback 설정이 불가능한 단순 정적 배포 환경에서 고려할 수 있다.

Q. errorElement는 뭐야?
A. Data Router에서 Route 단위 오류 화면을 지정하는 기능이다.

Q. BrowserRouter와 RouterProvider를 같이 써?
A. 일반적으로 같이 쓰지 않는다. BrowserRouter 방식과 createBrowserRouter / RouterProvider 방식 중 하나를 선택한다.

Q. loader와 action은 여기서 깊게 다뤄?
A. 아니다. Foundation 문서에서는 개념만 다루고 Data Fetching 또는 Advanced 문서에서 심화한다.

Q. 일반 SPA에서는 꼭 Data Router를 써야 해?
A. 아니다. BrowserRouter + Routes + Route 방식으로도 기본 SPA Routing은 충분히 구현할 수 있다.

Q. React Router 문제는 어떤 순서로 디버깅해?
A. URL, Route path, Navigation target, BrowserRouter, element, params, Outlet, Console, Network, Server Fallback 순서로 확인한다.

Q. 배포 환경에서만 문제면 뭘 먼저 봐?
A. 서버 fallback, static asset path, API proxy, Network response를 먼저 확인한다.

Q. Network tab에서는 뭘 봐?
A. 요청 URL, status code, response content-type, response body가 기대한 JSON/JS/CSS/HTML인지 확인한다.

Q. Console Error는 왜 중요해?
A. Component import 오류, runtime error, Router context 오류, MIME type error를 빠르게 확인할 수 있기 때문이다.

Q. React Router 오류를 빠르게 찾는 방법은?
A. 증상을 먼저 분류하고 URL, Console, Network, Route 정의를 기준으로 원인을 좁힌다.

Q. 새로고침 404와 NotFoundPage는 같은 문제야?
A. 아니다. 새로고침 404는 서버 fallback 문제이고 NotFoundPage는 React Router 매칭 실패 화면이다.

Q. API가 HTML을 반환하면 무슨 문제야?
A. API 요청이 SPA fallback에 걸려 index.html을 받은 것일 가능성이 크다.

Q. Nested Route 문제는 가장 먼저 뭘 봐?
A. 부모 Layout에 Outlet이 있는지 확인한다.

Q. React Router 앱 배포 후 뭘 테스트해야 해?
A. 직접 URL 접근, 새로고침, API 요청, static asset 응답, NotFoundPage, Protected Route 복원을 테스트해야 한다.

Q. `/festivals/1` 직접 접근 테스트가 왜 필요해?
A. BrowserRouter deep link가 서버 fallback 없이 404가 날 수 있기 때문이다.

Q. API URL도 직접 확인해야 해?
A. 필요하다. API 요청이 index.html로 fallback되지 않고 JSON을 반환하는지 확인해야 한다.

Q. JS/CSS 응답도 확인해야 해?
A. 필요하다. asset 요청이 index.html을 받으면 MIME type error가 발생할 수 있다.

Q. React Router 전체에서 가장 흔한 실수는?
A. BrowserRouter 누락, path 불일치, useParams 이름 불일치, Outlet 누락, 새로고침 404, API Path Collision이다.

Q. 배포 전 최종 검수에서 가장 중요한 것은?
A. deep link 직접 접근, 새로고침, API JSON 응답, static asset 로딩, Protected Route 새로고침 복원이다.

Q. React Router 문제를 해결할 때 가장 중요한 태도는?
A. React 코드 문제와 서버 fallback 문제를 분리해서 확인하는 것이다.

Q. React Router 다음 Domain 문서는 뭐가 좋아?
A. State Management, Data Fetching & REST API Integration, Authentication Frontend Flow, Error Handling & Loading UX 순서가 좋다.
