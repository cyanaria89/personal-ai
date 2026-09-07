# Frontend Testing Part10 - Router Auth Testing

---

# 1. Router Auth Testing Overview

## 1.1 Router Auth Testing Definition

### [개념]

Router Auth Testing은 React Router 기반 화면 이동, Route Parameter, Query String, Protected Route, 로그인 상태, 권한 상태에 따라 올바른 화면이 표시되는지 검증하는 테스트다.

Frontend Testing에서 Router와 Auth는 Page 단위 사용자 흐름과 강하게 연결된다.

---

### [핵심]

- Router Testing
- Auth Testing
- React Router
- MemoryRouter
- Routes
- Route
- Link
- NavLink
- useNavigate
- useParams
- useSearchParams
- Protected Route
- Private Route
- Auth State
- Role Based Route
- Login Redirect
- Forbidden Page
- Not Found Page

---

### [실무]

2026 실무 기준에서 Router Auth Testing은 단순히 URL이 바뀌는지 확인하는 테스트가 아니다.

검증 흐름:

```text
Initial Route
→ Render Route Tree
→ User Navigation
→ Auth State Check
→ Protected Route Decision
→ Page UI Result
```

좋은 Router Auth Test:

```text
Link 클릭 후 목적지 Page 표시
useNavigate 실행 후 이동 결과 표시
Route Parameter 기반 상세 화면 표시
Query String 기반 검색 결과 표시
비로그인 사용자는 로그인 Page로 이동
권한 없는 사용자는 Forbidden Page 표시
로그인 후 원래 접근하려던 Page로 복귀
```

나쁜 Router Auth Test:

```text
window.location 직접 수정만 검증
라우터 Provider 없이 useNavigate 테스트
URL 문자열만 확인하고 Page UI 미검증
Auth Store 내부 state만 직접 확인
실제 API 호출로 로그인 처리
권한 없는 상태 테스트 누락
```

---

### [FAQ]

Q. Router Auth Testing은 뭐야?
A. Route 이동, URL parameter, query string, 로그인 상태, 권한 상태에 따라 올바른 Page UI가 표시되는지 검증하는 테스트다.

Q. Router Test에서 URL만 확인하면 충분해?
A. 부족하다. 사용자가 실제로 보는 Page 결과까지 검증해야 한다.

Q. Auth Test는 무엇을 검증해?
A. 로그인 여부, 권한, 보호 Route 접근, redirect, forbidden UI를 검증한다.

---

## 1.2 Router Auth Testing Scope

### [개념]

Router Auth Testing Scope는 Router와 Auth 관련 테스트에서 Component 단위로 검증할지 Page / Route Flow 단위로 검증할지 정하는 기준이다.

Route Flow는 여러 Component, Provider, Store, API Mock이 엮이는 경우가 많아 Integration Test에 가깝다.

---

### [핵심]

포함 범위:

- Link navigation
- useNavigate result
- Route Parameter
- Query String
- Not Found Route
- Layout Route
- Nested Route
- Protected Route
- Login Redirect
- Logout Redirect
- Auth Loading
- Role Based Access
- Forbidden Page
- Previous Location
- Navigation Menu Active State

분리 권장:

- 실제 Backend Auth 통합
- 실제 token refresh 통합
- 실제 browser history E2E
- OAuth provider 실제 로그인
- 전체 결제 / 외부 인증 흐름

---

### [실무]

Component Test 적합:

```text
NavLink가 active 상태를 표시한다.
LoginButton 클릭 시 onLoginClick callback이 호출된다.
RoleBasedButton이 ADMIN에게만 표시된다.
```

Router Integration Test 적합:

```text
비로그인 사용자가 /mypage 접근 시 /login Page 표시
로그인 후 /mypage Page 표시
ADMIN이 /admin 접근 시 AdminPage 표시
USER가 /admin 접근 시 ForbiddenPage 표시
잘못된 URL 접근 시 NotFoundPage 표시
```

권장:

- Router Provider는 MemoryRouter 사용
- Route Tree를 테스트에 포함
- AuthProvider 또는 Mock Auth Context 사용
- 실제 API 호출 금지
- 최종 검증은 Page UI 중심

---

### [FAQ]

Q. Router Auth Testing은 Integration Test에 가까워?
A. 여러 Route, Provider, Auth State가 엮이면 Integration Test에 가깝다.

Q. Router 테스트에 실제 브라우저가 필요해?
A. 일반 Component / Integration Test에서는 MemoryRouter로 충분하다. 실제 브라우저 흐름은 E2E에서 다룬다.

Q. Auth API까지 실제 호출해야 해?
A. 아니다. Auth 상태나 API 응답은 mock으로 제어한다.

---

# 2. Router Test Setup

## 2.1 MemoryRouter Setup

### [개념]

MemoryRouter는 테스트 환경에서 실제 브라우저 주소창 없이 Route history를 메모리로 관리하는 React Router 도구다.

Router Test에서는 `initialEntries`로 시작 경로를 지정한다.

---

### [핵심]

- MemoryRouter
- initialEntries
- initialIndex
- Routes
- Route
- BrowserRouter 대체
- test route history
- route rendering
- navigation test

---

### [실무]

기본 예:

```tsx
render(
  <MemoryRouter initialEntries={["/festivals"]}>
    <Routes>
      <Route path="/festivals" element={<FestivalListPage />} />
    </Routes>
  </MemoryRouter>,
);

expect(screen.getByRole("heading", { name: "축제 목록" })).toBeInTheDocument();
```

Route 이동 예:

```tsx
test("상세 보기 링크를 클릭하면 상세 Page를 표시한다", async () => {
  const user = userEvent.setup();

  render(
    <MemoryRouter initialEntries={["/festivals"]}>
      <Routes>
        <Route path="/festivals" element={<FestivalListPage />} />
        <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
      </Routes>
    </MemoryRouter>,
  );

  await user.click(screen.getByRole("link", { name: "상세 보기" }));

  expect(
    await screen.findByRole("heading", { name: "축제 상세" }),
  ).toBeInTheDocument();
});
```

권장:

- 테스트 시작 경로는 initialEntries로 지정
- 실제 BrowserRouter 대신 MemoryRouter 사용
- 이동 결과는 URL보다 Page UI로 검증
- 공통 Router 설정은 renderWithRouter로 분리 가능

---

### [FAQ]

Q. MemoryRouter는 뭐야?
A. 테스트에서 메모리 기반 history로 Route를 관리하는 React Router 도구다.

Q. initialEntries는 뭐야?
A. 테스트가 시작할 초기 경로 목록이다.

Q. Router Test에서 BrowserRouter를 써야 해?
A. 일반적으로 테스트에서는 MemoryRouter가 더 적합하다.

---

## 2.2 renderWithRouter Utility

### [개념]

renderWithRouter Utility는 Router Provider와 Route Tree 설정을 반복하지 않도록 분리한 테스트 유틸리티다.

Router Test가 많아지면 `renderWithRouter` 또는 `renderWithProviders`로 공통 설정을 관리한다.

---

### [핵심]

- renderWithRouter
- renderWithProviders
- MemoryRouter wrapper
- initialEntries option
- route tree
- test utility
- provider composition
- reusable setup

---

### [실무]

예:

```tsx
type RenderWithRouterOptions = {
  initialEntries?: string[];
};

function renderWithRouter(
  ui: React.ReactElement,
  options: RenderWithRouterOptions = {},
) {
  return render(
    <MemoryRouter initialEntries={options.initialEntries ?? ["/"]}>
      {ui}
    </MemoryRouter>,
  );
}
```

Route Tree 포함 예:

```tsx
function renderAppRoutes(initialEntries: string[] = ["/"]) {
  return render(
    <MemoryRouter initialEntries={initialEntries}>
      <AppRoutes />
    </MemoryRouter>,
  );
}
```

사용:

```tsx
test("잘못된 경로이면 NotFound Page를 표시한다", () => {
  renderAppRoutes(["/unknown"]);

  expect(
    screen.getByRole("heading", { name: "페이지를 찾을 수 없습니다." }),
  ).toBeInTheDocument();
});
```

권장:

- Router만 필요한 경우 renderWithRouter
- QueryClient / Auth / Theme까지 필요한 경우 renderWithProviders
- initialEntries를 option으로 주입
- 테스트 의도에 맞게 최소 Provider 구성
- utility가 너무 복잡해지면 테스트 유형별로 분리

---

### [FAQ]

Q. renderWithRouter는 왜 만들어?
A. Router Provider 설정 중복을 줄이고 테스트 시작 경로를 쉽게 지정하기 위해 만든다.

Q. renderWithRouter와 renderWithProviders 차이는 뭐야?
A. renderWithRouter는 Router 중심이고 renderWithProviders는 Auth, QueryClient, Theme 같은 Provider까지 포함한다.

Q. 모든 Router Test에 AppRoutes 전체를 넣어야 해?
A. 아니다. 테스트 목적에 따라 필요한 Route만 구성하거나 AppRoutes 전체를 사용할 수 있다.

---

## 2.3 Route Tree Test Setup

### [개념]

Route Tree Test Setup은 실제 App의 Route 구조와 유사하게 테스트용 Routes를 구성하는 방식이다.

Page 이동, Protected Route, Not Found, Layout, Nested Route 테스트에 필요하다.

---

### [핵심]

- Route Tree
- AppRoutes
- Layout Route
- Nested Route
- Index Route
- Dynamic Route
- Catch-all Route
- Protected Route
- Route Composition
- Test Route Scope

---

### [실무]

간단한 Route Tree:

```tsx
render(
  <MemoryRouter initialEntries={["/"]}>
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/mypage" element={<MyPage />} />
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  </MemoryRouter>,
);
```

Nested Route 예:

```tsx
render(
  <MemoryRouter initialEntries={["/settings/profile"]}>
    <Routes>
      <Route path="/settings" element={<SettingsLayout />}>
        <Route path="profile" element={<ProfileSettingsPage />} />
        <Route path="security" element={<SecuritySettingsPage />} />
      </Route>
    </Routes>
  </MemoryRouter>,
);
```

권장:

- 단순 이동 테스트는 최소 Route 구성
- 실제 App 흐름 검증은 AppRoutes 사용
- Not Found catch-all Route 포함
- Protected Route 테스트는 AuthProvider와 함께 구성
- Layout 렌더링 여부도 필요 시 검증

---

### [FAQ]

Q. Route Tree는 왜 테스트에 필요해?
A. 실제 사용자 이동 결과를 확인하려면 관련 Route들이 테스트 환경에 구성되어 있어야 한다.

Q. 최소 Route만 구성해도 돼?
A. 가능하다. 테스트 목적이 단순하면 필요한 Route만 구성하는 것이 더 명확하다.

Q. AppRoutes 전체를 테스트하면 장점은 뭐야?
A. 실제 앱의 Route 연결 문제를 더 잘 잡을 수 있다.

---

# 3. Navigation Test

## 3.1 Link Navigation Test

### [개념]

Link Navigation Test는 사용자가 `<Link>` 또는 `<NavLink>`를 클릭했을 때 올바른 Page가 표시되는지 검증하는 테스트다.

링크는 `getByRole("link", { name })`으로 찾는다.

---

### [핵심]

- Link
- NavLink
- getByRole link
- user.click
- route navigation
- destination page
- accessible link name
- href attribute
- active state

---

### [실무]

예:

```tsx
test("축제 상세 링크를 클릭하면 상세 Page를 표시한다", async () => {
  const user = userEvent.setup();

  render(
    <MemoryRouter initialEntries={["/festivals"]}>
      <Routes>
        <Route path="/festivals" element={<FestivalListPage />} />
        <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
      </Routes>
    </MemoryRouter>,
  );

  await user.click(screen.getByRole("link", { name: "봄꽃 축제 상세 보기" }));

  expect(
    await screen.findByRole("heading", { name: "축제 상세" }),
  ).toBeInTheDocument();
});
```

href 검증:

```tsx
expect(screen.getByRole("link", { name: "상세 보기" })).toHaveAttribute(
  "href",
  "/festivals/1",
);
```

권장:

- 링크는 accessible name을 명확히 제공
- 클릭 후 목적지 Page UI 검증
- href만 검증할지 실제 이동까지 검증할지 목적에 따라 결정
- NavLink active 상태는 별도 테스트 가능

---

### [FAQ]

Q. Link Navigation은 어떻게 테스트해?
A. link role로 찾고 user.click 후 목적지 Page UI가 표시되는지 확인한다.

Q. href만 확인해도 돼?
A. 단순 Link Component는 가능하지만 Route 연결까지 확인하려면 클릭 후 Page UI를 검증한다.

Q. Link는 어떤 Query로 찾아?
A. `getByRole("link", { name: "..." })`를 사용한다.

---

## 3.2 useNavigate Test

### [개념]

useNavigate Test는 버튼 클릭, Form 제출, API 성공 후 `useNavigate`를 통해 이동하는 결과를 검증하는 테스트다.

`useNavigate` 함수 자체를 직접 검증하기보다 이동 후 표시되는 Page UI를 검증한다.

---

### [핵심]

- useNavigate
- programmatic navigation
- button click navigation
- form success navigation
- login redirect
- navigate after submit
- route result
- Page UI assertion

---

### [실무]

버튼 이동 예:

```tsx
test("작성하기 버튼을 클릭하면 작성 Page를 표시한다", async () => {
  const user = userEvent.setup();

  render(
    <MemoryRouter initialEntries={["/posts"]}>
      <Routes>
        <Route path="/posts" element={<PostListPage />} />
        <Route path="/posts/new" element={<PostCreatePage />} />
      </Routes>
    </MemoryRouter>,
  );

  await user.click(screen.getByRole("button", { name: "작성하기" }));

  expect(
    screen.getByRole("heading", { name: "게시글 작성" }),
  ).toBeInTheDocument();
});
```

Form 성공 후 이동:

```tsx
test("로그인 성공 후 마이페이지로 이동한다", async () => {
  const user = userEvent.setup();

  vi.mocked(login).mockResolvedValue({
    accessToken: "test-access-token",
    user: {
      userId: 1,
      role: "ROLE_USER",
      nickname: "tester",
    },
  });

  renderWithProviders(<AppRoutes />, {
    initialEntries: ["/login"],
  });

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "password123");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(
    await screen.findByRole("heading", { name: "마이페이지" }),
  ).toBeInTheDocument();
});
```

권장:

- useNavigate mock보다 Router 결과 검증 우선
- 이동 후 Page heading 검증
- Form submit 성공 후 redirect 테스트
- 실패 시 이동하지 않는 것도 테스트 가능

---

### [FAQ]

Q. useNavigate는 어떻게 테스트해?
A. navigate 함수를 직접 확인하기보다 이동 후 목적지 Page UI가 표시되는지 검증한다.

Q. useNavigate를 mock해야 해?
A. 보통 Router 결과 검증이 더 사용자 관점에 맞다. 특수한 단위 테스트에서는 mock할 수 있다.

Q. API 성공 후 이동은 어떻게 테스트해?
A. API mockResolvedValue 후 submit하고 목적지 Page UI를 findBy로 검증한다.

---

## 3.3 NavLink Active Test

### [개념]

NavLink Active Test는 현재 Route와 일치하는 Navigation Link가 active 상태로 표시되는지 검증하는 테스트다.

Navigation Menu, Sidebar, Tab Navigation에서 사용한다.

---

### [핵심]

- NavLink
- active state
- aria-current
- current page
- navigation menu
- sidebar
- tab navigation
- route match
- accessible current state

---

### [실무]

예:

```tsx
test("현재 경로에 해당하는 메뉴에 aria-current를 표시한다", () => {
  render(
    <MemoryRouter initialEntries={["/mypage"]}>
      <MainNavigation />
    </MemoryRouter>,
  );

  expect(screen.getByRole("link", { name: "마이페이지" })).toHaveAttribute(
    "aria-current",
    "page",
  );
});
```

지양:

```tsx
expect(screen.getByRole("link", { name: "마이페이지" })).toHaveClass("active");
```

가능하지만 우선순위는 낮다.

권장:

- active 상태는 aria-current 우선 검증
- className 검증은 보조적으로만 사용
- 현재 위치를 사용자가 이해할 수 있는지 확인
- Sidebar / Navbar / Tab Navigation에 적용

---

### [FAQ]

Q. NavLink active 상태는 어떻게 테스트해?
A. 현재 Route에서 해당 link에 `aria-current="page"`가 있는지 확인하는 방식이 좋다.

Q. active className을 테스트해도 돼?
A. 가능하지만 접근성 상태인 aria-current 검증이 더 권장된다.

Q. Navigation Menu도 Router Test 대상이야?
A. 그렇다. 현재 경로 표시와 링크 이동을 테스트할 수 있다.

---

# 4. Route Parameter Test

## 4.1 useParams Test

### [개념]

useParams Test는 URL path parameter를 사용하는 Page가 parameter 값을 기반으로 올바른 데이터를 조회하거나 표시하는지 검증하는 테스트다.

상세 Page, 수정 Page, 사용자 Page에서 자주 사용한다.

---

### [핵심]

- useParams
- path parameter
- dynamic route
- festivalId
- postId
- userId
- detail page
- edit page
- param based API
- invalid param

---

### [실무]

상세 Page 예:

```tsx
test("URL의 festivalId로 축제 상세 정보를 조회한다", async () => {
  vi.mocked(getFestivalDetail).mockResolvedValue({
    festivalId: 1,
    title: "봄꽃 축제",
  });

  render(
    <MemoryRouter initialEntries={["/festivals/1"]}>
      <Routes>
        <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
      </Routes>
    </MemoryRouter>,
  );

  expect(
    await screen.findByRole("heading", { name: "봄꽃 축제" }),
  ).toBeInTheDocument();

  expect(getFestivalDetail).toHaveBeenCalledWith(1);
});
```

Invalid Param 예:

```tsx
test("잘못된 id이면 잘못된 요청 메시지를 표시한다", async () => {
  render(
    <MemoryRouter initialEntries={["/festivals/abc"]}>
      <Routes>
        <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
      </Routes>
    </MemoryRouter>,
  );

  expect(await screen.findByText("잘못된 요청입니다.")).toBeInTheDocument();
});
```

권장:

- param 기반 API 호출 인자 검증 가능
- 최종 검증은 상세 UI 중심
- 숫자 변환이 필요한 param은 invalid case 테스트
- 404 응답과 invalid param 구분
- useParams 직접 mock보다 Route로 주입

---

### [FAQ]

Q. useParams는 어떻게 테스트해?
A. MemoryRouter initialEntries와 Route path에 parameter를 설정해 실제 Route로 값을 주입한다.

Q. useParams를 직접 mock해야 해?
A. 보통은 직접 mock하지 않고 Route path와 initialEntries로 테스트하는 것이 좋다.

Q. URL param이 숫자면 테스트에서 뭘 주의해야 해?
A. useParams는 문자열을 반환하므로 숫자 변환과 invalid param 처리를 테스트해야 한다.

---

## 4.2 Invalid Route Parameter Test

### [개념]

Invalid Route Parameter Test는 URL parameter가 잘못된 형식이거나 존재하지 않는 데이터일 때 적절한 Error 또는 Not Found UI가 표시되는지 검증하는 테스트다.

---

### [핵심]

Invalid Param 상황:

- non-numeric id
- negative id
- missing id
- invalid uuid
- not found id
- API 404
- bad request
- invalid request message
- NotFound Page

---

### [실무]

숫자 아님:

```tsx
test("festivalId가 숫자가 아니면 잘못된 요청 메시지를 표시한다", () => {
  render(
    <MemoryRouter initialEntries={["/festivals/abc"]}>
      <Routes>
        <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
      </Routes>
    </MemoryRouter>,
  );

  expect(screen.getByText("잘못된 요청입니다.")).toBeInTheDocument();
});
```

API 404:

```tsx
test("존재하지 않는 festivalId이면 Not Found 메시지를 표시한다", async () => {
  vi.mocked(getFestivalDetail).mockRejectedValue({
    response: {
      status: 404,
    },
  });

  render(
    <MemoryRouter initialEntries={["/festivals/999"]}>
      <Routes>
        <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
      </Routes>
    </MemoryRouter>,
  );

  expect(
    await screen.findByText("요청한 축제를 찾을 수 없습니다."),
  ).toBeInTheDocument();
});
```

권장:

- param 형식 오류와 서버 404 구분
- invalid param이면 API 호출을 막을 수 있음
- 404는 Not Found UI로 안내
- 사용자에게 기술적 오류 대신 안내 메시지 표시

---

### [FAQ]

Q. Invalid Route Parameter는 왜 테스트해?
A. 잘못된 URL 접근 시 앱이 깨지지 않고 적절한 안내를 제공해야 하기 때문이다.

Q. param 형식이 잘못되면 API를 호출해야 해?
A. 보통은 Frontend에서 먼저 검증해 잘못된 요청 메시지를 표시하는 것이 좋다.

Q. 존재하지 않는 id는 어떻게 테스트해?
A. API mock을 404로 실패시키고 Not Found UI를 검증한다.

---

# 5. Query String Test

## 5.1 useSearchParams Test

### [개념]

useSearchParams Test는 URL query string 값을 읽어 검색어, 필터, 정렬, 페이지 번호 등을 화면 상태와 API 요청에 반영하는지 검증하는 테스트다.

---

### [핵심]

- useSearchParams
- query string
- search params
- keyword
- region
- category
- page
- size
- sort
- filter state
- URL state
- query param based API

---

### [실무]

검색어 query string 예:

```tsx
test("query string의 keyword로 검색어 입력값을 초기화한다", () => {
  render(
    <MemoryRouter initialEntries={["/festivals?keyword=봄꽃"]}>
      <Routes>
        <Route path="/festivals" element={<FestivalSearchPage />} />
      </Routes>
    </MemoryRouter>,
  );

  expect(screen.getByLabelText("검색어")).toHaveValue("봄꽃");
});
```

API 호출 인자 검증:

```tsx
test("query string의 필터 조건으로 축제를 검색한다", async () => {
  vi.mocked(searchFestivals).mockResolvedValue([]);

  render(
    <MemoryRouter initialEntries={["/festivals?keyword=봄꽃&region=seoul"]}>
      <Routes>
        <Route path="/festivals" element={<FestivalSearchPage />} />
      </Routes>
    </MemoryRouter>,
  );

  await screen.findByText("검색 결과가 없습니다.");

  expect(searchFestivals).toHaveBeenCalledWith({
    keyword: "봄꽃",
    region: "seoul",
  });
});
```

권장:

- query string 기반 초기 Form 값 검증
- API 요청 인자 검증
- 없는 query param 기본값 테스트
- page / sort / filter 동기화 테스트
- URL state와 Form state 일치 확인

---

### [FAQ]

Q. useSearchParams는 어떻게 테스트해?
A. MemoryRouter initialEntries에 query string을 포함해 시작 경로를 설정한다.

Q. query string 값을 input 초기값으로 쓰면 뭘 테스트해?
A. URL의 값이 Form field에 반영되는지 확인한다.

Q. query param 기반 API 호출도 테스트해야 해?
A. 검색 / 필터 화면에서는 API 함수 인자 검증이 유용하다.

---

## 5.2 Update Search Params Test

### [개념]

Update Search Params Test는 사용자가 검색어나 필터를 변경했을 때 URL query string이 갱신되고 화면 결과가 변경되는지 검증하는 테스트다.

---

### [핵심]

- setSearchParams
- update query string
- search submit
- filter change
- pagination change
- sort change
- URL state sync
- result update
- default param removal

---

### [실무]

검색 submit 후 결과 검증:

```tsx
test("검색어를 입력하고 검색하면 검색 결과를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(searchFestivals).mockResolvedValue([
    { festivalId: 1, title: "봄꽃 축제" },
  ]);

  render(
    <MemoryRouter initialEntries={["/festivals"]}>
      <Routes>
        <Route path="/festivals" element={<FestivalSearchPage />} />
      </Routes>
    </MemoryRouter>,
  );

  await user.type(screen.getByLabelText("검색어"), "봄꽃");
  await user.click(screen.getByRole("button", { name: "검색" }));

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();

  expect(searchFestivals).toHaveBeenCalledWith(
    expect.objectContaining({
      keyword: "봄꽃",
    }),
  );
});
```

URL 표시를 직접 검증해야 하는 경우는 Location Display 유틸리티를 사용할 수 있다.

```tsx
function LocationDisplay() {
  const location = useLocation();

  return <div data-testid="location-display">{location.search}</div>;
}
```

테스트:

```tsx
expect(screen.getByTestId("location-display")).toHaveTextContent(
  "keyword=봄꽃",
);
```

권장:

- 사용자 결과 UI를 우선 검증
- URL string 직접 검증은 필요한 경우에만 사용
- query param 기본값 제거 정책 테스트 가능
- filter reset 시 query string 초기화 검증 가능

---

### [FAQ]

Q. setSearchParams 결과는 어떻게 테스트해?
A. 우선 검색 결과 UI를 검증하고, URL 자체가 중요하면 useLocation 기반 LocationDisplay로 확인할 수 있다.

Q. URL query string 자체를 반드시 테스트해야 해?
A. URL 공유나 새로고침 상태 복원이 중요한 화면이면 테스트하는 것이 좋다.

Q. filter reset 후 query param도 지워야 해?
A. 정책에 따라 다르지만 URL 상태를 Form 상태와 맞추는 것이 좋다.

---

# 6. Protected Route Test

## 6.1 Protected Route Definition

### [개념]

Protected Route는 인증된 사용자만 접근할 수 있는 Route다.

Protected Route Test는 로그인 여부에 따라 허용 Page 또는 Login Page가 표시되는지 검증한다.

---

### [핵심]

- Protected Route
- Private Route
- authenticated user
- unauthenticated user
- login required
- redirect to login
- auth loading
- return path
- previous location
- Outlet
- Navigate

---

### [실무]

ProtectedRoute 예:

```tsx
function ProtectedRoute() {
  const { isAuthenticated, isLoading } = useAuth();

  if (isLoading) {
    return <LoadingState message="인증 정보를 확인하는 중입니다." />;
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return <Outlet />;
}
```

비로그인 테스트:

```tsx
test("비로그인 사용자가 마이페이지에 접근하면 로그인 Page를 표시한다", () => {
  renderWithProviders(<AppRoutes />, {
    initialEntries: ["/mypage"],
    authenticated: false,
  });

  expect(screen.getByRole("heading", { name: "로그인" })).toBeInTheDocument();
});
```

로그인 테스트:

```tsx
test("로그인 사용자가 마이페이지에 접근하면 마이페이지를 표시한다", () => {
  renderWithProviders(<AppRoutes />, {
    initialEntries: ["/mypage"],
    authenticated: true,
  });

  expect(
    screen.getByRole("heading", { name: "마이페이지" }),
  ).toBeInTheDocument();
});
```

권장:

- 인증 상태를 mock AuthProvider로 제어
- 비로그인 / 로그인 케이스 모두 테스트
- redirect 결과는 Login Page UI로 검증
- auth loading 상태 별도 테스트
- 실제 token 사용 금지

---

### [FAQ]

Q. Protected Route는 뭐야?
A. 로그인한 사용자만 접근할 수 있는 보호된 Route다.

Q. Protected Route는 어떻게 테스트해?
A. Auth 상태를 true/false로 설정하고 접근 결과가 Page UI로 올바르게 나타나는지 확인한다.

Q. 비로그인 redirect는 URL을 봐야 해?
A. URL보다 Login Page가 표시되는지 검증하는 것이 사용자 관점에 더 가깝다.

---

## 6.2 Auth Loading Test

### [개념]

Auth Loading Test는 앱이 로그인 상태를 확인하는 동안 Loading UI를 표시하고, 확인 후 적절한 Route 결과로 전환되는지 검증하는 테스트다.

---

### [핵심]

- auth loading
- auth initialization
- token check
- user profile fetch
- loading state
- protected route pending
- no premature redirect
- no flicker
- auth resolved

---

### [실무]

예:

```tsx
test("인증 확인 중에는 loading 메시지를 표시한다", () => {
  renderWithProviders(<AppRoutes />, {
    initialEntries: ["/mypage"],
    authLoading: true,
  });

  expect(screen.getByRole("status")).toHaveTextContent(
    "인증 정보를 확인하는 중입니다.",
  );
});
```

주의:

```text
authLoading true
→ 바로 login redirect 하지 않음

authLoading false + unauthenticated
→ login redirect

authLoading false + authenticated
→ protected page 표시
```

권장:

- auth loading 상태 별도 테스트
- loading 중 Login Page가 먼저 깜빡이지 않도록 검증 가능
- token check / profile fetch mock 필요 시 API Mocking과 연결
- resolve 후 결과는 findBy 사용 가능

---

### [FAQ]

Q. Auth Loading은 왜 테스트해?
A. 인증 상태 확인 전 로그인 페이지로 잘못 redirect되는 깜빡임을 방지하기 위해 중요하다.

Q. authLoading 중에는 어떤 UI가 보여야 해?
A. 인증 정보를 확인 중이라는 Loading UI가 표시되는 것이 좋다.

Q. authLoading과 unauthenticated는 달라?
A. 다르다. authLoading은 아직 확인 중이고 unauthenticated는 확인 후 비로그인 상태다.

---

## 6.3 Previous Location Redirect Test

### [개념]

Previous Location Redirect Test는 비로그인 사용자가 보호 Route에 접근했다가 로그인 후 원래 접근하려던 경로로 돌아가는 흐름을 검증하는 테스트다.

---

### [핵심]

- previous location
- return path
- redirect after login
- location state
- Navigate state
- from path
- login success
- protected page restore

---

### [실무]

흐름:

```text
User accesses /mypage unauthenticated
→ Redirect to /login with from=/mypage
→ User login success
→ Navigate to /mypage
→ MyPage visible
```

테스트 예:

```tsx
test("로그인 후 원래 접근하려던 마이페이지로 이동한다", async () => {
  const user = userEvent.setup();

  vi.mocked(login).mockResolvedValue({
    accessToken: "test-access-token",
    user: {
      userId: 1,
      role: "ROLE_USER",
      nickname: "tester",
    },
  });

  renderWithProviders(<AppRoutes />, {
    initialEntries: ["/mypage"],
    authenticated: false,
  });

  expect(screen.getByRole("heading", { name: "로그인" })).toBeInTheDocument();

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "password123");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(
    await screen.findByRole("heading", { name: "마이페이지" }),
  ).toBeInTheDocument();
});
```

권장:

- 로그인 성공 후 원래 경로 복귀 검증
- previous location이 없으면 기본 경로 이동 테스트
- replace 여부는 필요 시 history 동작으로 검증
- 실제 token 대신 더미 token 사용

---

### [FAQ]

Q. Previous Location Redirect는 뭐야?
A. 보호 페이지 접근 후 로그인하면 원래 가려던 페이지로 돌아가게 하는 흐름이다.

Q. 이 흐름은 왜 테스트해야 해?
A. 로그인 후 사용자가 원래 작업 맥락을 잃지 않도록 하는 중요한 UX이기 때문이다.

Q. previous location이 없으면 어디로 이동해?
A. 보통 메인 페이지나 마이페이지 같은 기본 경로로 이동한다. 프로젝트 정책에 따라 테스트한다.

---

# 7. Role Based Route Test

## 7.1 Role Based Access Test

### [개념]

Role Based Access Test는 사용자 role에 따라 접근 가능한 Route와 표시되는 UI가 달라지는지 검증하는 테스트다.

관리자 Page, 운영자 Page, 사용자 권한 UI에서 중요하다.

---

### [핵심]

- Role Based Access
- ROLE_USER
- ROLE_ADMIN
- ROLE_MANAGER
- admin route
- forbidden route
- permission check
- role based UI
- access denied
- authority

---

### [실무]

Admin 접근 허용:

```tsx
test("ADMIN 사용자는 관리자 Page에 접근할 수 있다", () => {
  renderWithProviders(<AppRoutes />, {
    initialEntries: ["/admin"],
    authenticated: true,
    user: {
      userId: 1,
      role: "ROLE_ADMIN",
    },
  });

  expect(
    screen.getByRole("heading", { name: "관리자 페이지" }),
  ).toBeInTheDocument();
});
```

USER 접근 차단:

```tsx
test("USER 사용자가 관리자 Page에 접근하면 권한 없음 Page를 표시한다", () => {
  renderWithProviders(<AppRoutes />, {
    initialEntries: ["/admin"],
    authenticated: true,
    user: {
      userId: 2,
      role: "ROLE_USER",
    },
  });

  expect(
    screen.getByRole("heading", { name: "접근 권한이 없습니다." }),
  ).toBeInTheDocument();
});
```

권장:

- role 이름은 Backend와 통일
- ROLE_USER / ROLE_ADMIN 같은 실제 권한명 사용
- unauthorized와 forbidden 구분
- 권한 없는 경우 redirect보다 Forbidden UI가 적합한지 정책 확인
- 권한별 메뉴 표시 테스트와 연결 가능

---

### [FAQ]

Q. Role Based Access는 뭐야?
A. 사용자 권한에 따라 접근 가능한 Route와 UI를 다르게 처리하는 방식이다.

Q. USER가 ADMIN Route에 접근하면 어떻게 테스트해?
A. Auth user role을 ROLE_USER로 설정하고 Forbidden Page가 표시되는지 확인한다.

Q. 401과 403은 Role Test에서 어떻게 달라?
A. 401은 비로그인이고 403은 로그인했지만 권한이 부족한 상태다.

---

## 7.2 Role Based UI Test

### [개념]

Role Based UI Test는 같은 Page 안에서도 사용자 role에 따라 버튼, 메뉴, 기능이 표시되거나 숨겨지는지 검증하는 테스트다.

---

### [핵심]

- role based UI
- admin button
- delete button
- edit button
- management menu
- hidden action
- visible action
- permission UI
- queryBy
- conditional rendering

---

### [실무]

ADMIN 버튼 표시:

```tsx
test("ADMIN이면 삭제 버튼을 표시한다", () => {
  renderWithProviders(<PostDetailPage />, {
    authenticated: true,
    user: {
      userId: 1,
      role: "ROLE_ADMIN",
    },
  });

  expect(screen.getByRole("button", { name: "삭제" })).toBeInTheDocument();
});
```

USER 버튼 숨김:

```tsx
test("USER이면 삭제 버튼을 표시하지 않는다", () => {
  renderWithProviders(<PostDetailPage />, {
    authenticated: true,
    user: {
      userId: 2,
      role: "ROLE_USER",
    },
  });

  expect(
    screen.queryByRole("button", { name: "삭제" }),
  ).not.toBeInTheDocument();
});
```

권장:

- 표시되는 경우와 숨겨지는 경우 모두 테스트
- 숨김 검증은 queryBy 사용
- role 조건은 Component props 또는 Auth Context로 제어
- UI 숨김은 보안 대체가 아니며 Backend 권한 검증도 필요
- 테스트에는 실제 개인정보 사용 금지

---

### [FAQ]

Q. Role Based UI는 뭐야?
A. 사용자 권한에 따라 버튼, 메뉴, 기능 표시 여부가 달라지는 UI다.

Q. 숨겨져야 하는 버튼은 어떻게 테스트해?
A. `queryByRole`로 해당 버튼이 문서에 없는지 확인한다.

Q. Frontend에서 버튼을 숨기면 보안이 해결돼?
A. 아니다. Frontend UI 제어는 UX이고 실제 권한 검증은 Backend에서 해야 한다.

---

# 8. Login and Logout Flow Test

## 8.1 Login Flow Test

### [개념]

Login Flow Test는 사용자가 이메일과 비밀번호를 입력하고 로그인했을 때 Auth State가 갱신되고 적절한 Page로 이동하는지 검증하는 테스트다.

실제 token은 사용하지 않고 더미 token과 mock API를 사용한다.

---

### [핵심]

- Login Flow
- Login Form
- login API mock
- accessToken
- Auth State
- redirect
- global error
- invalid credentials
- login success
- login failure

---

### [실무]

로그인 성공:

```tsx
test("로그인 성공 시 마이페이지를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(login).mockResolvedValue({
    accessToken: "test-access-token",
    user: {
      userId: 1,
      email: "test@example.com",
      nickname: "tester",
      role: "ROLE_USER",
    },
  });

  renderWithProviders(<AppRoutes />, {
    initialEntries: ["/login"],
  });

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "password123");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(
    await screen.findByRole("heading", { name: "마이페이지" }),
  ).toBeInTheDocument();
});
```

로그인 실패:

```tsx
test("로그인 실패 시 오류 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(login).mockRejectedValue({
    response: {
      status: 401,
    },
  });

  renderWithProviders(<AppRoutes />, {
    initialEntries: ["/login"],
  });

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "wrong-password");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(await screen.findByRole("alert")).toHaveTextContent(
    "이메일 또는 비밀번호가 올바르지 않습니다.",
  );
});
```

권장:

- 실제 비밀번호 / token 사용 금지
- 로그인 성공 후 Page UI 검증
- 로그인 실패 후 global error 검증
- button loading / disabled 상태 검증 가능
- Auth Store 내부 직접 검증보다 사용자 결과 우선

---

### [FAQ]

Q. Login Flow Test는 무엇을 검증해?
A. 로그인 입력, API 성공/실패, Auth 상태 반영, redirect 또는 오류 메시지를 검증한다.

Q. 실제 token을 사용해야 해?
A. 아니다. `test-access-token` 같은 더미 token을 사용한다.

Q. Auth Store state를 직접 확인해야 해?
A. 보통은 로그인 후 표시되는 Page나 메뉴 같은 사용자 결과로 검증하는 것이 좋다.

---

## 8.2 Logout Flow Test

### [개념]

Logout Flow Test는 사용자가 로그아웃했을 때 Auth State가 초기화되고 보호 Page 접근이 차단되며 로그인 또는 메인 Page로 이동하는지 검증하는 테스트다.

---

### [핵심]

- Logout Flow
- logout button
- token clear
- user state clear
- query cache clear
- redirect after logout
- protected route after logout
- guest UI
- authenticated menu hidden

---

### [실무]

예:

```tsx
test("로그아웃하면 로그인 Page를 표시한다", async () => {
  const user = userEvent.setup();

  renderWithProviders(<AppRoutes />, {
    initialEntries: ["/mypage"],
    authenticated: true,
    user: {
      userId: 1,
      role: "ROLE_USER",
      nickname: "tester",
    },
  });

  await user.click(screen.getByRole("button", { name: "로그아웃" }));

  expect(screen.getByRole("heading", { name: "로그인" })).toBeInTheDocument();
});
```

로그아웃 후 보호 Route 차단:

```tsx
test("로그아웃 후 마이페이지 접근 시 로그인 Page를 표시한다", async () => {
  const user = userEvent.setup();

  renderWithProviders(<AppRoutes />, {
    initialEntries: ["/mypage"],
    authenticated: true,
  });

  await user.click(screen.getByRole("button", { name: "로그아웃" }));
  await user.click(screen.getByRole("link", { name: "마이페이지" }));

  expect(screen.getByRole("heading", { name: "로그인" })).toBeInTheDocument();
});
```

권장:

- 로그아웃 버튼은 role button으로 찾음
- 로그아웃 후 guest UI 표시 검증
- 보호 Route 접근 차단 검증
- token/localStorage 직접 검증보다 사용자 결과 우선
- 필요 시 storage clear는 별도 utility test로 분리

---

### [FAQ]

Q. Logout Flow Test는 뭘 검증해?
A. 로그아웃 후 인증 상태가 해제되고 보호 Page 접근이 막히는지 검증한다.

Q. localStorage token 삭제를 직접 테스트해야 해?
A. UI Flow에서는 사용자 결과를 우선 검증하고, storage utility는 별도 Unit Test로 검증할 수 있다.

Q. 로그아웃 후 어디로 이동해야 해?
A. 프로젝트 정책에 따라 로그인 Page, 메인 Page 등으로 이동한다. 해당 정책을 테스트한다.

---

# 9. Not Found and Forbidden Test

## 9.1 Not Found Route Test

### [개념]

Not Found Route Test는 정의되지 않은 URL에 접근했을 때 Not Found Page 또는 안내 메시지가 표시되는지 검증하는 테스트다.

---

### [핵심]

- Not Found Route
- catch-all route
- path="\*"
- 404 page
- unknown URL
- invalid route
- home link
- back link
- user guidance

---

### [실무]

예:

```tsx
test("존재하지 않는 경로이면 Not Found Page를 표시한다", () => {
  render(
    <MemoryRouter initialEntries={["/unknown-path"]}>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </MemoryRouter>,
  );

  expect(
    screen.getByRole("heading", { name: "페이지를 찾을 수 없습니다." }),
  ).toBeInTheDocument();
  expect(screen.getByRole("link", { name: "홈으로 이동" })).toBeInTheDocument();
});
```

권장:

- catch-all Route 포함
- 안내 heading 검증
- 홈으로 이동 link 검증
- API 404와 Route 404 구분
- 잘못된 URL에서도 앱이 깨지지 않는지 확인

---

### [FAQ]

Q. Not Found Route는 왜 테스트해?
A. 사용자가 잘못된 URL에 접근해도 앱이 깨지지 않고 안내를 제공해야 하기 때문이다.

Q. Route 404와 API 404는 달라?
A. 다르다. Route 404는 정의되지 않은 URL이고 API 404는 요청한 데이터가 없는 상태다.

Q. Not Found Page에는 무엇이 필요해?
A. 안내 메시지와 홈으로 이동 같은 복구 action이 있으면 좋다.

---

## 9.2 Forbidden Route Test

### [개념]

Forbidden Route Test는 로그인은 되었지만 권한이 부족한 사용자가 특정 Route에 접근했을 때 Forbidden Page 또는 권한 없음 메시지가 표시되는지 검증하는 테스트다.

---

### [핵심]

- Forbidden Route
- 403
- access denied
- role mismatch
- authenticated but unauthorized
- ROLE_USER
- ROLE_ADMIN
- permission message
- home link
- back link

---

### [실무]

예:

```tsx
test("권한 없는 사용자가 관리자 Page에 접근하면 Forbidden Page를 표시한다", () => {
  renderWithProviders(<AppRoutes />, {
    initialEntries: ["/admin"],
    authenticated: true,
    user: {
      userId: 1,
      role: "ROLE_USER",
    },
  });

  expect(
    screen.getByRole("heading", { name: "접근 권한이 없습니다." }),
  ).toBeInTheDocument();
  expect(screen.getByRole("link", { name: "홈으로 이동" })).toBeInTheDocument();
});
```

권장:

- 비로그인 401과 권한 부족 403 구분
- Forbidden Page에 복구 action 제공
- role 기반 Route 정책 검증
- 권한 없는 경우 Login Page로 보내는 정책이면 명확히 테스트
- Backend 권한 검증은 별도 영역

---

### [FAQ]

Q. Forbidden Route는 뭐야?
A. 로그인했지만 권한이 부족한 사용자가 접근할 수 없는 Route다.

Q. Forbidden과 Login Required는 달라?
A. 다르다. Login Required는 인증이 없고 Forbidden은 인증은 있지만 권한이 부족하다.

Q. Forbidden Page에는 무엇이 필요해?
A. 권한 없음 안내와 홈으로 이동 또는 이전 페이지 이동 action이 있으면 좋다.

---

# 10. Router Auth Troubleshooting

## 10.1 useNavigate Context Error

### [개념]

useNavigate Context Error는 Router Provider 없이 `useNavigate`, `Link`, `useParams`, `useSearchParams`를 사용하는 Component를 테스트할 때 발생하는 오류다.

Router Hook을 사용하는 Component는 MemoryRouter로 감싸야 한다.

---

### [핵심]

원인:

- MemoryRouter 없음
- Router Provider 없음
- renderWithRouter 미사용
- Route Tree 누락
- useNavigate outside Router
- Link outside Router
- useParams without Route path

---

### [실무]

문제:

```tsx
render(<LoginPage />);
```

`LoginPage` 내부에서 useNavigate를 쓰면 오류가 날 수 있다.

개선:

```tsx
render(
  <MemoryRouter initialEntries={["/login"]}>
    <Routes>
      <Route path="/login" element={<LoginPage />} />
    </Routes>
  </MemoryRouter>,
);
```

Debug Flow:

```text
Router Hook 오류
→ Component가 useNavigate/useParams/Link 사용 확인
→ MemoryRouter wrapper 확인
→ Route path 구성 확인
→ initialEntries 확인
→ renderWithRouter 사용
```

---

### [FAQ]

Q. useNavigate 관련 오류는 왜 나?
A. Router Provider 없이 Router Hook을 사용하는 Component를 렌더링했기 때문이다.

Q. 해결 방법은 뭐야?
A. MemoryRouter와 필요한 Route를 테스트에 추가한다.

Q. Link만 있어도 Router가 필요해?
A. 그렇다. Link도 Router Context 안에서 동작한다.

---

## 10.2 Route Not Rendering

### [개념]

Route Not Rendering은 initialEntries와 Route path가 맞지 않아 예상 Page가 표시되지 않는 상황이다.

경로 문자열, dynamic parameter, nested route, basename, wildcard를 확인해야 한다.

---

### [핵심]

원인:

- initialEntries mismatch
- Route path mismatch
- missing leading slash
- nested route path issue
- index route mismatch
- dynamic param mismatch
- catch-all route intercept
- layout outlet missing
- provider missing

---

### [실무]

Debug Flow:

```text
Route가 렌더링되지 않음
→ initialEntries 확인
→ Route path 확인
→ nested route 구조 확인
→ Layout에 Outlet 있는지 확인
→ dynamic param path 확인
→ screen.debug 확인
```

문제 예:

```tsx
<MemoryRouter initialEntries={["/settings/profile"]}>
  <Routes>
    <Route path="/settings" element={<SettingsLayout />}>
      <Route path="/profile" element={<ProfilePage />} />
    </Route>
  </Routes>
</MemoryRouter>
```

Nested child path가 절대 경로가 되어 예상과 다를 수 있다.

개선:

```tsx
<Route path="/settings" element={<SettingsLayout />}>
  <Route path="profile" element={<ProfilePage />} />
</Route>
```

---

### [FAQ]

Q. Route가 테스트에서 렌더링되지 않아.
A. initialEntries와 Route path가 정확히 맞는지, nested route 구조와 Outlet이 있는지 확인한다.

Q. Nested Route child path에 slash를 붙이면 안 돼?
A. 의도에 따라 다르지만 중첩 경로에서는 보통 상대 경로를 사용한다.

Q. Layout Route에서 하위 Page가 안 보여.
A. Layout Component에 `<Outlet />`이 있는지 확인한다.

---

## 10.3 Auth State Not Applied

### [개념]

Auth State Not Applied는 테스트에서 설정한 인증 상태가 Protected Route나 Auth UI에 반영되지 않는 상황이다.

AuthProvider mock, Provider 순서, initial auth state, async auth loading을 확인해야 한다.

---

### [핵심]

원인:

- AuthProvider 누락
- MockAuthProvider 미사용
- initial auth state 미주입
- Provider order 문제
- authLoading true 유지
- user object 누락
- role field mismatch
- token만 있고 user 없음
- store reset 누락
- test 간 auth state 공유

---

### [실무]

Debug Flow:

```text
Auth 상태 반영 안 됨
→ AuthProvider 포함 여부 확인
→ authenticated 값 확인
→ user object 확인
→ role field 이름 확인
→ authLoading 상태 확인
→ Provider 순서 확인
→ store reset 확인
```

권장 Auth Test Options:

```ts
type AuthTestOptions = {
  authenticated?: boolean;
  authLoading?: boolean;
  user?: {
    userId: number;
    role: "ROLE_USER" | "ROLE_ADMIN";
    nickname?: string;
  };
};
```

사용:

```tsx
renderWithProviders(<AppRoutes />, {
  initialEntries: ["/admin"],
  authenticated: true,
  user: {
    userId: 1,
    role: "ROLE_ADMIN",
  },
});
```

권장:

- Auth state는 test option으로 명시
- role field는 실제 앱 구조와 일치
- 테스트마다 Auth state 초기화
- 실제 token에 의존하지 않음
- authLoading과 authenticated 구분

---

### [FAQ]

Q. 테스트에서 authenticated true인데 보호 Page가 안 보여.
A. AuthProvider에 값이 제대로 주입되는지, authLoading이 true로 남아 있지 않은지 확인한다.

Q. role 기반 테스트가 실패해.
A. user.role 값이 실제 앱에서 사용하는 권한명과 일치하는지 확인한다.

Q. 테스트 간 로그인 상태가 섞이면?
A. Auth Store reset 또는 MockAuthProvider의 독립 상태 생성을 확인한다.

---

# 11. Router Auth Anti Pattern

## 11.1 Common Router Auth Testing Anti Patterns

### [개념]

Router Auth Testing Anti Pattern은 Router와 Auth 테스트가 사용자 흐름을 제대로 검증하지 못하거나 구현 세부사항에 과도하게 의존하는 잘못된 방식이다.

---

### [핵심]

Anti Pattern:

- Router Provider 없이 테스트
- useNavigate만 mock하고 UI 결과 미검증
- URL 문자열만 확인
- Page UI 결과 미검증
- Auth Store 내부 state 직접 검증
- 실제 token 사용
- 실제 login API 호출
- 401 / 403 구분 누락
- authLoading 상태 누락
- Protected Route 비로그인 case 누락
- Role Based Route USER case 누락
- Not Found Route 누락
- query string parsing 미검증
- previous location redirect 미검증

---

### [실무]

나쁜 예:

```tsx
expect(mockNavigate).toHaveBeenCalledWith("/mypage");
```

좋은 예:

```tsx
expect(
  await screen.findByRole("heading", { name: "마이페이지" }),
).toBeInTheDocument();
```

나쁜 예:

```tsx
localStorage.setItem("accessToken", "real-token");
render(<MyPage />);
```

좋은 예:

```tsx
renderWithProviders(<AppRoutes />, {
  initialEntries: ["/mypage"],
  authenticated: true,
  user: {
    userId: 1,
    role: "ROLE_USER",
  },
});
```

검수 기준:

```text
Router Provider가 있는가?
Route 결과 UI를 검증하는가?
비로그인 / 로그인 / 권한 부족을 구분하는가?
실제 token / API에 의존하지 않는가?
```

---

### [FAQ]

Q. Router Auth Test에서 가장 흔한 실수는 뭐야?
A. Router Provider 없이 테스트하거나, URL / navigate 호출만 확인하고 Page UI 결과를 검증하지 않는 것이다.

Q. Auth Store 내부 state를 직접 테스트하면 안 돼?
A. Router Auth Flow에서는 사용자에게 보이는 접근 결과를 우선 검증하는 것이 좋다.

Q. 실제 token을 넣어 테스트하면 안 돼?
A. 안 된다. 테스트는 더미 token과 mock Auth 상태를 사용해야 한다.

---

# 12. Router Auth Testing Checklist

## 12.1 Router Auth Testing Checklist

### [개념]

Router Auth Testing Checklist는 Router, Auth, Protected Route, Role Based Route 테스트가 사용자 흐름과 접근 제어 기준을 만족하는지 확인하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] MemoryRouter 또는 Router Provider를 사용했는가?
- [ ] initialEntries로 시작 경로를 명확히 설정했는가?
- [ ] 필요한 Route Tree를 구성했는가?
- [ ] Link 클릭 후 Page UI를 검증했는가?
- [ ] useNavigate 결과를 Page UI로 검증했는가?
- [ ] Route Parameter를 실제 Route로 주입했는가?
- [ ] Query String 초기값을 테스트했는가?
- [ ] Protected Route의 비로그인 case를 테스트했는가?
- [ ] Protected Route의 로그인 case를 테스트했는가?
- [ ] Auth Loading 상태를 테스트했는가?
- [ ] 로그인 후 previous location 복귀를 테스트했는가?
- [ ] ROLE_USER / ROLE_ADMIN 접근 차이를 테스트했는가?
- [ ] Forbidden Page를 테스트했는가?
- [ ] Not Found Route를 테스트했는가?
- [ ] 실제 token / password / 개인정보를 사용하지 않았는가?
- [ ] 실제 Auth API 호출을 피했는가?
- [ ] AuthProvider state가 테스트마다 독립적인가?
```

---

### [실무]

Agent Router Auth Test 작성 Flow:

```text
Identify Route Scenario
→ Setup MemoryRouter initialEntries
→ Setup Route Tree
→ Setup Auth State
→ Render with Providers
→ Trigger Navigation if Needed
→ Assert Page UI
→ Assert Forbidden / Login / NotFound if Needed
→ Check Security Test Data
```

예:

```text
Admin Route
→ initialEntries /admin
→ authenticated true
→ user role ROLE_USER
→ render AppRoutes
→ Forbidden Page 표시 검증
```

---

### [FAQ]

Q. Router Auth Testing Checklist의 핵심은 뭐야?
A. Router Provider, 시작 경로, Auth 상태, Route 결과 UI, 권한별 접근 결과를 명확히 검증하는 것이다.

Q. Router Auth Test 작성 전 무엇을 정해야 해?
A. 시작 경로, Route Tree, Auth 상태, 사용자 role, 기대 Page 결과를 정해야 한다.

Q. Router Auth Test가 불안정하면 뭘 확인해?
A. Provider 구성, initialEntries, Route path, authLoading 상태, mock Auth state 초기화를 확인한다.

---

# 13. Part10 Summary

## 13.1 Router Auth Testing Final Rule

### [개념]

Frontend Testing Part10은 React Router와 Auth Flow 테스트 기준을 정의한다.

이 Part의 목적은 Agent가 Route 이동, URL parameter, query string, Protected Route, Role Based Route, Login / Logout Flow를 사용자 관점으로 검증하게 만드는 것이다.

---

### [핵심]

최종 기준:

- Router Test는 MemoryRouter 사용
- initialEntries로 시작 경로 지정
- 이동 결과는 Page UI로 검증
- Link는 getByRole("link")로 찾고 user.click 사용
- useNavigate는 호출 여부보다 이동 결과 검증
- useParams는 실제 Route path로 주입
- useSearchParams는 query string initialEntries로 주입
- Protected Route는 로그인 / 비로그인 case 모두 테스트
- Auth Loading 상태를 분리해 테스트
- Previous Location Redirect 검증
- ROLE_USER / ROLE_ADMIN 권한 차이 검증
- Forbidden과 Login Required 구분
- Not Found Route 검증
- Auth State는 Mock Provider 또는 test option으로 제어
- 실제 token / password / Auth API 사용 금지

---

### [실무]

Agent 작업 Flow:

```text
Router Auth Test Request
→ Identify Navigation or Auth Scenario
→ Configure MemoryRouter
→ Configure Route Tree
→ Configure Auth State
→ Mock API if Needed
→ Trigger User Action
→ Assert Page UI Result
→ Assert Access Control Result
→ Review Anti Pattern
```

Part11 이후 연결:

```text
Part10 Router Auth Testing
→ Part11 TanStack Query Testing
→ Part12 Accessibility Testing
→ Part13 Snapshot Test Caution
→ Part14 Test Structure
→ Part15 Troubleshooting
```

---

### [FAQ]

Q. Part10의 최종 목적은 뭐야?
A. Frontend Agent가 Router 이동과 Auth 접근 제어를 사용자 Page 결과 기준으로 테스트하게 만드는 것이다.

Q. Router Auth Testing에서 가장 중요한 규칙은 뭐야?
A. MemoryRouter로 실제 Route 흐름을 구성하고 URL보다 Page UI 결과를 검증하는 것이다.

Q. Part10 다음에는 어떤 내용이 이어져야 해?
A. TanStack Query의 query, mutation, cache, invalidation 테스트 기준이 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Router Auth Testing은 뭐야?
A. Route 이동, URL parameter, query string, 로그인 상태, 권한 상태에 따라 올바른 Page UI가 표시되는지 검증하는 테스트다.

Q. Router Test에서 URL만 확인하면 충분해?
A. 부족하다. 사용자가 실제로 보는 Page 결과까지 검증해야 한다.

Q. Auth Test는 무엇을 검증해?
A. 로그인 여부, 권한, 보호 Route 접근, redirect, forbidden UI를 검증한다.

Q. Router Auth Testing은 Integration Test에 가까워?
A. 여러 Route, Provider, Auth State가 엮이면 Integration Test에 가깝다.

Q. Router 테스트에 실제 브라우저가 필요해?
A. 일반 Component / Integration Test에서는 MemoryRouter로 충분하다. 실제 브라우저 흐름은 E2E에서 다룬다.

Q. MemoryRouter는 뭐야?
A. 테스트에서 메모리 기반 history로 Route를 관리하는 React Router 도구다.

Q. initialEntries는 뭐야?
A. 테스트가 시작할 초기 경로 목록이다.

Q. Router Test에서 BrowserRouter를 써야 해?
A. 일반적으로 테스트에서는 MemoryRouter가 더 적합하다.

Q. renderWithRouter는 왜 만들어?
A. Router Provider 설정 중복을 줄이고 테스트 시작 경로를 쉽게 지정하기 위해 만든다.

Q. renderWithRouter와 renderWithProviders 차이는 뭐야?
A. renderWithRouter는 Router 중심이고 renderWithProviders는 Auth, QueryClient, Theme 같은 Provider까지 포함한다.

Q. Route Tree는 왜 테스트에 필요해?
A. 실제 사용자 이동 결과를 확인하려면 관련 Route들이 테스트 환경에 구성되어 있어야 한다.

Q. 최소 Route만 구성해도 돼?
A. 가능하다. 테스트 목적이 단순하면 필요한 Route만 구성하는 것이 더 명확하다.

Q. Link Navigation은 어떻게 테스트해?
A. link role로 찾고 user.click 후 목적지 Page UI가 표시되는지 확인한다.

Q. href만 확인해도 돼?
A. 단순 Link Component는 가능하지만 Route 연결까지 확인하려면 클릭 후 Page UI를 검증한다.

Q. useNavigate는 어떻게 테스트해?
A. navigate 함수를 직접 확인하기보다 이동 후 목적지 Page UI가 표시되는지 검증한다.

Q. useNavigate를 mock해야 해?
A. 보통 Router 결과 검증이 더 사용자 관점에 맞다. 특수한 단위 테스트에서는 mock할 수 있다.

Q. API 성공 후 이동은 어떻게 테스트해?
A. API mockResolvedValue 후 submit하고 목적지 Page UI를 findBy로 검증한다.

Q. NavLink active 상태는 어떻게 테스트해?
A. 현재 Route에서 해당 link에 `aria-current="page"`가 있는지 확인하는 방식이 좋다.

Q. active className을 테스트해도 돼?
A. 가능하지만 접근성 상태인 aria-current 검증이 더 권장된다.

Q. useParams는 어떻게 테스트해?
A. MemoryRouter initialEntries와 Route path에 parameter를 설정해 실제 Route로 값을 주입한다.

Q. useParams를 직접 mock해야 해?
A. 보통은 직접 mock하지 않고 Route path와 initialEntries로 테스트하는 것이 좋다.

Q. URL param이 숫자면 테스트에서 뭘 주의해야 해?
A. useParams는 문자열을 반환하므로 숫자 변환과 invalid param 처리를 테스트해야 한다.

Q. Invalid Route Parameter는 왜 테스트해?
A. 잘못된 URL 접근 시 앱이 깨지지 않고 적절한 안내를 제공해야 하기 때문이다.

Q. 존재하지 않는 id는 어떻게 테스트해?
A. API mock을 404로 실패시키고 Not Found UI를 검증한다.

Q. useSearchParams는 어떻게 테스트해?
A. MemoryRouter initialEntries에 query string을 포함해 시작 경로를 설정한다.

Q. query string 값을 input 초기값으로 쓰면 뭘 테스트해?
A. URL의 값이 Form field에 반영되는지 확인한다.

Q. query param 기반 API 호출도 테스트해야 해?
A. 검색 / 필터 화면에서는 API 함수 인자 검증이 유용하다.

Q. setSearchParams 결과는 어떻게 테스트해?
A. 우선 검색 결과 UI를 검증하고, URL 자체가 중요하면 useLocation 기반 LocationDisplay로 확인할 수 있다.

Q. Protected Route는 뭐야?
A. 로그인한 사용자만 접근할 수 있는 보호된 Route다.

Q. Protected Route는 어떻게 테스트해?
A. Auth 상태를 true/false로 설정하고 접근 결과가 Page UI로 올바르게 나타나는지 확인한다.

Q. 비로그인 redirect는 URL을 봐야 해?
A. URL보다 Login Page가 표시되는지 검증하는 것이 사용자 관점에 더 가깝다.

Q. Auth Loading은 왜 테스트해?
A. 인증 상태 확인 전 로그인 페이지로 잘못 redirect되는 깜빡임을 방지하기 위해 중요하다.

Q. authLoading 중에는 어떤 UI가 보여야 해?
A. 인증 정보를 확인 중이라는 Loading UI가 표시되는 것이 좋다.

Q. authLoading과 unauthenticated는 달라?
A. 다르다. authLoading은 아직 확인 중이고 unauthenticated는 확인 후 비로그인 상태다.

Q. Previous Location Redirect는 뭐야?
A. 보호 페이지 접근 후 로그인하면 원래 가려던 페이지로 돌아가게 하는 흐름이다.

Q. Previous Location Redirect는 왜 테스트해야 해?
A. 로그인 후 사용자가 원래 작업 맥락을 잃지 않도록 하는 중요한 UX이기 때문이다.

Q. Role Based Access는 뭐야?
A. 사용자 권한에 따라 접근 가능한 Route와 UI를 다르게 처리하는 방식이다.

Q. USER가 ADMIN Route에 접근하면 어떻게 테스트해?
A. Auth user role을 ROLE_USER로 설정하고 Forbidden Page가 표시되는지 확인한다.

Q. 401과 403은 Role Test에서 어떻게 달라?
A. 401은 비로그인이고 403은 로그인했지만 권한이 부족한 상태다.

Q. Role Based UI는 뭐야?
A. 사용자 권한에 따라 버튼, 메뉴, 기능 표시 여부가 달라지는 UI다.

Q. 숨겨져야 하는 버튼은 어떻게 테스트해?
A. `queryByRole`로 해당 버튼이 문서에 없는지 확인한다.

Q. Frontend에서 버튼을 숨기면 보안이 해결돼?
A. 아니다. Frontend UI 제어는 UX이고 실제 권한 검증은 Backend에서 해야 한다.

Q. Login Flow Test는 무엇을 검증해?
A. 로그인 입력, API 성공/실패, Auth 상태 반영, redirect 또는 오류 메시지를 검증한다.

Q. 실제 token을 사용해야 해?
A. 아니다. `test-access-token` 같은 더미 token을 사용한다.

Q. Auth Store state를 직접 확인해야 해?
A. 보통은 로그인 후 표시되는 Page나 메뉴 같은 사용자 결과로 검증하는 것이 좋다.

Q. Logout Flow Test는 뭘 검증해?
A. 로그아웃 후 인증 상태가 해제되고 보호 Page 접근이 막히는지 검증한다.

Q. localStorage token 삭제를 직접 테스트해야 해?
A. UI Flow에서는 사용자 결과를 우선 검증하고, storage utility는 별도 Unit Test로 검증할 수 있다.

Q. Not Found Route는 왜 테스트해?
A. 사용자가 잘못된 URL에 접근해도 앱이 깨지지 않고 안내를 제공해야 하기 때문이다.

Q. Route 404와 API 404는 달라?
A. 다르다. Route 404는 정의되지 않은 URL이고 API 404는 요청한 데이터가 없는 상태다.

Q. Forbidden Route는 뭐야?
A. 로그인했지만 권한이 부족한 사용자가 접근할 수 없는 Route다.

Q. Forbidden과 Login Required는 달라?
A. 다르다. Login Required는 인증이 없고 Forbidden은 인증은 있지만 권한이 부족하다.

Q. useNavigate 관련 오류는 왜 나?
A. Router Provider 없이 Router Hook을 사용하는 Component를 렌더링했기 때문이다.

Q. Route가 테스트에서 렌더링되지 않아.
A. initialEntries와 Route path가 정확히 맞는지, nested route 구조와 Outlet이 있는지 확인한다.

Q. 테스트에서 authenticated true인데 보호 Page가 안 보여.
A. AuthProvider에 값이 제대로 주입되는지, authLoading이 true로 남아 있지 않은지 확인한다.

Q. role 기반 테스트가 실패해.
A. user.role 값이 실제 앱에서 사용하는 권한명과 일치하는지 확인한다.

Q. Router Auth Test에서 가장 흔한 실수는 뭐야?
A. Router Provider 없이 테스트하거나, URL / navigate 호출만 확인하고 Page UI 결과를 검증하지 않는 것이다.

Q. Router Auth Testing Checklist의 핵심은 뭐야?
A. Router Provider, 시작 경로, Auth 상태, Route 결과 UI, 권한별 접근 결과를 명확히 검증하는 것이다.

Q. Part10 Router Auth Testing의 최종 목표는 뭐야?
A. Frontend Agent가 Router 이동과 Auth 접근 제어를 사용자 Page 결과 기준으로 테스트하게 만드는 것이다.
