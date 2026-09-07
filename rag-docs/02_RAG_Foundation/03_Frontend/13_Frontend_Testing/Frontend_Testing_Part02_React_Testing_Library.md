# Frontend Testing Part02 - React Testing Library

---

# 1. React Testing Library Overview

## 1.1 React Testing Library Definition

### [개념]

React Testing Library는 React Component를 사용자의 관점에서 테스트하기 위한 테스트 유틸리티다.

React Testing Library는 Component 내부 구현보다 사용자가 실제로 보는 화면, 접근 가능한 요소, 입력, 클릭, 결과 UI를 기준으로 테스트한다.

---

### [핵심]

- React Testing Library
- RTL
- User Behavior Test
- User-visible UI
- DOM Result
- Accessible Query
- render
- screen
- userEvent
- findBy
- waitFor
- Component Test
- Integration Test
- Implementation Detail Test 지양

---

### [실무]

2026 실무 기준에서 React Testing Library는 React Component 테스트의 기본 선택지다.

테스트 기준:

```text
Component 구현 방식
→ 직접 검증하지 않음

사용자 화면
→ 검증함

사용자 입력
→ userEvent로 검증함

사용자 결과
→ DOM / UI 결과로 검증함
```

좋은 테스트 흐름:

```text
render
→ screen query
→ userEvent
→ assert visible result
```

예:

```tsx
test("이메일과 비밀번호를 입력하고 로그인한다", async () => {
  const user = userEvent.setup();
  const onLogin = vi.fn();

  render(<LoginForm onLogin={onLogin} />);

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "password123");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(onLogin).toHaveBeenCalledWith({
    email: "test@example.com",
    password: "password123",
  });
});
```

---

### [FAQ]

Q. React Testing Library는 뭐야?
A. React Component를 사용자 관점에서 테스트하기 위한 테스트 유틸리티다.

Q. React Testing Library의 핵심 철학은 뭐야?
A. 내부 구현보다 사용자가 보는 화면과 조작 결과를 테스트하는 것이다.

Q. React Testing Library는 Unit Test 도구야?
A. 순수 Unit Test보다는 Component Test와 Integration Test에 주로 사용된다.

---

## 1.2 React Testing Library Role

### [개념]

React Testing Library의 역할은 Component를 테스트 DOM에 렌더링하고, 사용자가 인식할 수 있는 방식으로 요소를 찾고, 사용자 행동 후 UI 결과를 검증하도록 지원하는 것이다.

---

### [핵심]

React Testing Library 역할:

- Component render
- DOM query
- Accessible query
- UI result assertion
- Async UI handling
- User behavior verification
- Provider wrapper testing
- Component integration testing
- Implementation detail 방지

---

### [실무]

React Testing Library는 아래 작업에 적합하다.

```text
Button 클릭 테스트
Form 입력 테스트
Modal 열기 / 닫기 테스트
API 응답 후 목록 표시 테스트
Loading / Error / Empty 상태 테스트
Router 화면 전환 테스트
Auth 상태별 UI 테스트
```

React Testing Library가 직접 담당하지 않는 영역:

```text
테스트 실행기
→ Vitest / Jest

Assertion 확장
→ jest-dom

사용자 이벤트 시뮬레이션
→ userEvent

API Mocking
→ vi.mock / jest.mock / MSW
```

---

### [FAQ]

Q. React Testing Library만 설치하면 테스트가 전부 가능해?
A. 아니다. Vitest 또는 Jest, jest-dom, userEvent, 필요 시 MSW와 함께 사용한다.

Q. React Testing Library는 API Mock도 해줘?
A. 아니다. API Mock은 vi.mock, jest.mock, MSW 같은 도구로 처리한다.

Q. React Testing Library는 E2E 테스트 도구야?
A. 아니다. 실제 브라우저 전체 흐름은 Playwright나 Cypress 같은 E2E 도구가 담당한다.

---

# 2. Testing Philosophy

## 2.1 User-Centered Testing

### [개념]

User-Centered Testing은 테스트를 사용자가 실제로 인식하고 수행하는 행동 중심으로 작성하는 원칙이다.

React Testing Library는 사용자가 볼 수 있는 role, label, text, display value를 기준으로 요소를 찾는 방식을 권장한다.

---

### [핵심]

- User-centered testing
- User-visible element
- Accessible role
- Accessible name
- Label text
- Visible text
- Display value
- User action
- UI result
- DOM output

---

### [실무]

권장 기준:

```text
사용자가 버튼을 찾을 수 있는가?
→ getByRole("button", { name: "저장" })

사용자가 입력창을 이해할 수 있는가?
→ getByLabelText("이메일")

사용자가 결과 메시지를 볼 수 있는가?
→ findByText("저장되었습니다.")
```

권장 예:

```tsx
test("저장 버튼을 누르면 성공 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  render(<ProfileForm />);

  await user.click(screen.getByRole("button", { name: "저장" }));

  expect(await screen.findByText("저장되었습니다.")).toBeInTheDocument();
});
```

지양 예:

```tsx
test("save 함수가 실행된다", () => {
  expect(saveProfile).toHaveBeenCalled();
});
```

---

### [FAQ]

Q. 사용자 중심 테스트는 뭐야?
A. 사용자가 보는 요소와 수행하는 행동, 그리고 화면 결과를 기준으로 작성하는 테스트다.

Q. getByRole을 많이 쓰는 이유는 뭐야?
A. 사용자가 보조기술로 인식하는 역할과 이름을 기준으로 찾기 때문에 실제 사용성에 가깝다.

Q. 함수 호출 여부만 확인하면 부족해?
A. 사용자에게 보이는 결과가 검증되지 않으면 실제 기능이 정상인지 판단하기 어렵다.

---

## 2.2 Avoid Implementation Details

### [개념]

React Testing Library는 Component 내부 구현 세부사항을 직접 테스트하지 않는 방식을 권장한다.

내부 state, private function, hook 내부 변수, DOM 구조, className에 의존하는 테스트는 구현 변경에 취약하다.

---

### [핵심]

피해야 할 대상:

- internal state
- private function
- component instance
- hook internal value
- implementation-specific DOM structure
- CSS className 중심 검증
- snapshot-only test
- data-testid 남용
- library internal behavior

---

### [실무]

나쁜 예:

```tsx
test("isOpen state가 true가 된다", () => {
  expect(component.state.isOpen).toBe(true);
});
```

좋은 예:

```tsx
test("열기 버튼을 누르면 모달을 표시한다", async () => {
  const user = userEvent.setup();

  render(<NoticeModal />);

  await user.click(screen.getByRole("button", { name: "열기" }));

  expect(screen.getByRole("dialog")).toBeInTheDocument();
});
```

검수 기준:

```text
테스트가 사용자 결과를 검증하는가?
구현 변경 후에도 사용자 결과가 같으면 유지되는가?
테스트 실패 시 기능 문제가 명확한가?
```

---

### [FAQ]

Q. 내부 state를 테스트하면 왜 안 좋아?
A. 구현 변경만으로 테스트가 깨질 수 있고 사용자 기능 검증과 직접 연결되지 않을 수 있다.

Q. Modal은 내부 open state 대신 뭘 테스트해?
A. 열기 버튼 클릭 후 dialog가 화면에 표시되는지 테스트한다.

Q. hook 내부 값은 테스트하지 않아?
A. 보통은 hook을 사용하는 UI 결과로 검증한다. 공용 hook 자체는 별도 hook test 전략에서 다룬다.

---

## 2.3 Behavior Test vs Implementation Detail Test

### [개념]

Behavior Test는 사용자 행동과 결과를 검증하는 테스트다.

Implementation Detail Test는 내부 구현 방식이 맞는지 검증하는 테스트다.

Frontend Testing에서는 Behavior Test를 우선한다.

---

### [핵심]

| 구분       | Behavior Test           | Implementation Detail Test |
| ---------- | ----------------------- | -------------------------- |
| 기준       | 사용자 행동과 화면 결과 | 내부 state와 구현 방식     |
| 예         | 클릭 후 메시지 표시     | state 값 직접 확인         |
| 안정성     | 높음                    | 낮음                       |
| 유지보수성 | 좋음                    | 취약                       |
| 권장도     | 높음                    | 낮음                       |

---

### [실무]

Behavior Test 예:

```tsx
test("검색어를 입력하고 검색하면 결과 목록을 표시한다", async () => {
  const user = userEvent.setup();

  render(<SearchPage />);

  await user.type(screen.getByLabelText("검색어"), "축제");
  await user.click(screen.getByRole("button", { name: "검색" }));

  expect(await screen.findByText("서울 봄꽃 축제")).toBeInTheDocument();
});
```

Implementation Detail Test 예:

```tsx
test("searchKeyword state가 변경된다", () => {
  expect(searchKeyword).toBe("축제");
});
```

Agent 검수 기준:

```text
사용자 행동이 포함되어 있는가?
화면 결과 assertion이 있는가?
구현 변수명에 의존하지 않는가?
```

---

### [FAQ]

Q. Behavior Test가 뭐야?
A. 사용자가 입력, 클릭, 이동한 뒤 화면에 어떤 결과가 나타나는지 검증하는 테스트다.

Q. Implementation Detail Test는 항상 금지야?
A. 항상 금지는 아니지만 React Component 테스트에서는 대부분 지양한다.

Q. 테스트가 구현 세부사항인지 어떻게 판단해?
A. 사용자가 직접 인식할 수 없는 state, 함수명, className, 내부 구조를 검증하면 구현 세부사항일 가능성이 높다.

---

# 3. Render Rules

## 3.1 render Rules

### [개념]

`render`는 React Component를 테스트용 DOM에 렌더링하는 React Testing Library 함수다.

테스트는 `render`로 Component를 화면에 배치한 뒤 `screen`으로 요소를 찾고 결과를 검증한다.

---

### [핵심]

- render
- test DOM
- jsdom
- React Component
- independent render
- cleanup
- wrapper
- Provider
- custom render
- render result 지양
- screen 사용 권장

---

### [실무]

기본 예:

```tsx
import { render, screen } from "@testing-library/react";

test("제목을 표시한다", () => {
  render(<PageTitle title="축제 목록" />);

  expect(
    screen.getByRole("heading", { name: "축제 목록" }),
  ).toBeInTheDocument();
});
```

권장:

- 테스트마다 독립적으로 `render`
- 이전 테스트의 DOM 상태에 의존하지 않음
- `screen`을 우선 사용
- Provider가 필요한 경우 wrapper 또는 custom render 사용
- 테스트 간 전역 상태 공유 방지

주의:

```text
render result에서 직접 container를 뒤지는 방식
→ 최후 수단

screen query
→ 우선 사용
```

---

### [FAQ]

Q. render는 뭐 하는 함수야?
A. React Component를 테스트 DOM에 렌더링하는 함수다.

Q. 테스트마다 render를 다시 해야 해?
A. 그렇다. 테스트 간 독립성을 유지하기 위해 각 테스트에서 새로 렌더링하는 것이 좋다.

Q. render 결과의 container를 직접 써도 돼?
A. 가능하지만 우선은 screen과 접근성 기반 query를 사용하는 것이 좋다.

---

## 3.2 screen Rules

### [개념]

`screen`은 현재 렌더링된 테스트 화면에서 요소를 찾는 객체다.

React Testing Library에서는 render 결과에서 query를 구조분해하기보다 `screen` 사용을 권장한다.

---

### [핵심]

- screen
- current document
- query object
- getByRole
- getByLabelText
- getByText
- findBy
- queryBy
- readable test
- recommended pattern

---

### [실무]

권장 예:

```tsx
render(<LoginForm />);

expect(screen.getByLabelText("이메일")).toBeInTheDocument();
expect(screen.getByRole("button", { name: "로그인" })).toBeInTheDocument();
```

덜 권장:

```tsx
const { getByText } = render(<LoginForm />);

expect(getByText("로그인")).toBeInTheDocument();
```

`screen` 장점:

```text
현재 화면에서 찾는다는 의미가 명확함
query 출처가 일관됨
테스트 가독성이 좋아짐
React Testing Library 권장 패턴과 맞음
```

---

### [FAQ]

Q. screen은 왜 써?
A. 현재 테스트 화면에서 요소를 찾는 방식이 명확하고 React Testing Library 권장 패턴이기 때문이다.

Q. render에서 getByText를 꺼내 쓰면 안 돼?
A. 가능하지만 screen을 쓰는 방식이 더 일관적이고 가독성이 좋다.

Q. screen은 여러 render가 있으면 어떻게 동작해?
A. 현재 document 전체를 기준으로 query한다. 한 테스트 안에서 불필요한 중복 render는 피하는 것이 좋다.

---

## 3.3 cleanup Rules

### [개념]

`cleanup`은 테스트 DOM에 렌더링된 Component를 정리하는 작업이다.

현대 React Testing Library 환경에서는 대부분 테스트 실행기가 각 테스트 후 자동 cleanup을 수행한다.

---

### [핵심]

- cleanup
- test isolation
- DOM reset
- afterEach
- auto cleanup
- shared DOM 방지
- side effect cleanup
- timer cleanup
- mock cleanup

---

### [실무]

일반적인 환경에서는 별도 cleanup을 직접 호출하지 않아도 된다.

권장:

```text
테스트마다 새 render 사용
mock clear / reset 수행
timer 사용 시 정리
QueryClient 테스트마다 새로 생성
DOM 상태를 테스트 간 공유하지 않음
```

필요 시:

```tsx
import { cleanup } from "@testing-library/react";

afterEach(() => {
  cleanup();
  vi.clearAllMocks();
});
```

주의:

```text
cleanup은 DOM 정리
mock reset은 mock 정리
Query Cache 정리는 QueryClient 분리
```

---

### [FAQ]

Q. cleanup을 직접 호출해야 해?
A. 대부분의 현대 테스트 환경에서는 자동으로 처리된다.

Q. cleanup과 mock reset은 같은 거야?
A. 아니다. cleanup은 DOM 정리이고 mock reset은 mock 함수 상태 정리다.

Q. 테스트 간 상태가 섞이면 뭘 확인해야 해?
A. DOM cleanup, mock reset, QueryClient 분리, 전역 store 초기화를 확인해야 한다.

---

# 4. Custom Render Rules

## 4.1 Provider Wrapper

### [개념]

Provider Wrapper는 Component 테스트에 필요한 Router, QueryClient, Auth, Theme, Store 같은 Provider를 감싸는 테스트 설정이다.

Provider가 필요한 Component는 단독 render 시 오류가 발생할 수 있다.

---

### [핵심]

필요 Provider:

- MemoryRouter
- QueryClientProvider
- AuthProvider
- ThemeProvider
- Store Provider
- Intl Provider
- Toast Provider
- Modal Root
- Error Boundary

---

### [실무]

Provider 필요 상황:

```text
useNavigate 사용
→ Router Provider 필요

useQuery 사용
→ QueryClientProvider 필요

useAuth 사용
→ AuthProvider 필요

theme context 사용
→ ThemeProvider 필요
```

예:

```tsx
function renderWithProviders(ui: React.ReactElement) {
  const queryClient = new QueryClient({
    defaultOptions: {
      queries: {
        retry: false,
      },
    },
  });

  return render(
    <MemoryRouter>
      <QueryClientProvider client={queryClient}>{ui}</QueryClientProvider>
    </MemoryRouter>,
  );
}
```

권장:

- Provider 반복 코드는 custom render로 분리
- 테스트마다 새 QueryClient 생성
- Router initialEntries 주입 가능하게 설계
- Auth state override 가능하게 설계
- Provider가 과도하게 많으면 Component 의존성 검토

---

### [FAQ]

Q. Provider Wrapper는 왜 필요해?
A. Component가 Router, QueryClient, Auth Context 같은 외부 context에 의존할 때 테스트 환경에서도 제공해야 하기 때문이다.

Q. No QueryClient set 오류는 왜 나?
A. QueryClientProvider 없이 TanStack Query Hook을 사용하는 Component를 렌더링했기 때문이다.

Q. useNavigate 오류는 왜 나?
A. Router Provider 없이 useNavigate를 사용하는 Component를 테스트했기 때문이다.

---

## 4.2 Custom Render Utility

### [개념]

Custom Render Utility는 반복되는 Provider 설정을 공통 함수로 분리한 테스트 유틸리티다.

Frontend 프로젝트에서는 `renderWithProviders` 같은 공통 함수를 만들어 테스트 중복을 줄인다.

---

### [핵심]

- custom render
- renderWithProviders
- test utils
- provider setup
- router initialEntries
- auth state override
- query client isolation
- reusable wrapper
- testing consistency

---

### [실무]

예:

```tsx
type RenderOptions = {
  initialEntries?: string[];
  authenticated?: boolean;
};

function renderWithProviders(
  ui: React.ReactElement,
  options: RenderOptions = {},
) {
  const queryClient = createTestQueryClient();

  return render(
    <MemoryRouter initialEntries={options.initialEntries ?? ["/"]}>
      <QueryClientProvider client={queryClient}>
        <AuthProvider initialAuthenticated={options.authenticated ?? false}>
          {ui}
        </AuthProvider>
      </QueryClientProvider>
    </MemoryRouter>,
  );
}
```

사용 예:

```tsx
test("비로그인 사용자가 마이페이지에 접근하면 로그인 페이지를 표시한다", () => {
  renderWithProviders(<AppRoutes />, {
    initialEntries: ["/mypage"],
    authenticated: false,
  });

  expect(screen.getByRole("heading", { name: "로그인" })).toBeInTheDocument();
});
```

권장 파일 위치:

```text
src/test/renderWithProviders.tsx
src/test/createTestQueryClient.ts
src/test/setup.ts
```

---

### [FAQ]

Q. custom render는 언제 만들어?
A. Router, QueryClient, Auth Provider처럼 여러 테스트에서 반복되는 설정이 생기면 만든다.

Q. custom render가 너무 복잡해지면?
A. 테스트 유형별로 renderWithRouter, renderWithQueryClient, renderWithProviders를 분리할 수 있다.

Q. Auth 상태는 custom render에서 어떻게 제어해?
A. options로 authenticated, user, role 같은 초기 상태를 주입할 수 있게 설계한다.

---

## 4.3 Test QueryClient Setup

### [개념]

TanStack Query를 사용하는 Component는 테스트에서 QueryClientProvider와 테스트용 QueryClient가 필요하다.

테스트마다 독립적인 QueryClient를 생성해야 Query Cache가 테스트 간 공유되지 않는다.

---

### [핵심]

- QueryClient
- QueryClientProvider
- retry false
- cache isolation
- staleTime
- gcTime
- mutation test
- query cache
- test independence

---

### [실무]

권장 설정:

```tsx
function createTestQueryClient() {
  return new QueryClient({
    defaultOptions: {
      queries: {
        retry: false,
      },
      mutations: {
        retry: false,
      },
    },
  });
}
```

사용 예:

```tsx
function renderWithQueryClient(ui: React.ReactElement) {
  const queryClient = createTestQueryClient();

  return render(
    <QueryClientProvider client={queryClient}>{ui}</QueryClientProvider>,
  );
}
```

주의:

```text
전역 QueryClient 재사용 금지
실패 테스트에서 retry false 설정
테스트 간 cache 공유 방지
mutation 이후 invalidate 결과는 UI 결과로 검증
```

---

### [FAQ]

Q. 테스트에서 QueryClient를 전역으로 재사용해도 돼?
A. 권장하지 않는다. Query Cache가 테스트 간 공유되어 불안정해질 수 있다.

Q. 테스트에서 retry false를 설정하는 이유는?
A. 실패 테스트가 재시도 때문에 느려지거나 예측하기 어려워지는 것을 막기 위해서다.

Q. invalidateQueries 호출 자체를 테스트해야 해?
A. 보통은 직접 호출 여부보다 화면 데이터가 갱신되는지 사용자 결과로 검증한다.

---

# 5. Assertion Rules

## 5.1 jest-dom Assertion

### [개념]

`jest-dom`은 DOM 테스트에 필요한 custom matcher를 제공한다.

React Testing Library 테스트에서는 `toBeInTheDocument`, `toBeVisible`, `toBeDisabled` 같은 matcher를 자주 사용한다.

---

### [핵심]

자주 쓰는 matcher:

- toBeInTheDocument
- toBeVisible
- toBeDisabled
- toBeEnabled
- toHaveTextContent
- toHaveValue
- toHaveAttribute
- toHaveAccessibleName
- toHaveAccessibleDescription
- toBeChecked
- toHaveFocus

---

### [실무]

예:

```tsx
expect(screen.getByRole("button", { name: "저장" })).toBeEnabled();

expect(screen.getByLabelText("이메일")).toHaveValue("test@example.com");

expect(screen.getByRole("alert")).toHaveTextContent("이메일을 입력해 주세요.");
```

Vitest setup 예:

```ts
import "@testing-library/jest-dom/vitest";
```

Jest setup 예:

```ts
import "@testing-library/jest-dom";
```

권장:

- DOM 상태는 jest-dom matcher로 명확히 검증
- 단순 truthy 검증 지양
- 접근성 관련 matcher 활용
- disabled / checked / value 상태는 전용 matcher 사용

---

### [FAQ]

Q. toBeInTheDocument는 어디서 와?
A. jest-dom이 제공하는 DOM assertion matcher다.

Q. Vitest에서도 jest-dom을 쓸 수 있어?
A. 가능하다. `@testing-library/jest-dom/vitest`를 setup 파일에 import한다.

Q. expect(element).toBeTruthy()는 왜 별로야?
A. 어떤 DOM 상태를 기대하는지 명확하지 않다. toBeInTheDocument 같은 전용 matcher가 더 좋다.

---

## 5.2 Visible Result Assertion

### [개념]

Visible Result Assertion은 사용자가 실제로 볼 수 있는 UI 결과를 검증하는 assertion 방식이다.

React Testing Library 테스트는 함수 호출이나 내부 상태보다 화면 결과 assertion을 우선한다.

---

### [핵심]

검증 대상:

- visible text
- heading
- button state
- input value
- error message
- loading message
- empty message
- success message
- dialog visible
- route result
- auth UI result

---

### [실무]

권장 예:

```tsx
expect(screen.getByRole("heading", { name: "축제 목록" })).toBeVisible();
expect(screen.getByRole("button", { name: "저장" })).toBeDisabled();
expect(await screen.findByText("저장되었습니다.")).toBeInTheDocument();
```

지양 예:

```tsx
expect(saveProfile).toHaveBeenCalled();
```

보완 예:

```tsx
await user.click(screen.getByRole("button", { name: "저장" }));

expect(await screen.findByText("저장되었습니다.")).toBeInTheDocument();
```

기준:

```text
사용자에게 보이는가?
상태가 의미 있게 변했는가?
기능 성공 / 실패가 화면으로 드러나는가?
```

---

### [FAQ]

Q. 화면 결과 assertion은 왜 중요해?
A. 실제 사용자가 체감하는 기능 성공 여부를 검증할 수 있기 때문이다.

Q. callback 호출 검증은 하면 안 돼?
A. 할 수 있다. 다만 가능하면 callback 이후 UI 결과까지 함께 검증하는 것이 좋다.

Q. visible과 inTheDocument는 달라?
A. 다르다. inTheDocument는 DOM 존재 여부이고 visible은 사용자가 볼 수 있는 상태인지 확인한다.

---

# 6. Async UI Rules

## 6.1 Async Rendering with RTL

### [개념]

Async Rendering은 API 응답, 상태 업데이트, timer, userEvent 이후 UI가 나중에 변경되는 렌더링 상황이다.

React Testing Library에서는 비동기 UI를 `findBy` 또는 `waitFor`로 기다린다.

---

### [핵심]

비동기 상황:

- API response
- mutation success
- mutation error
- loading to success
- loading to error
- debounce result
- route transition
- auth initialization
- delayed validation
- toast display

---

### [실무]

권장:

```tsx
expect(await screen.findByText("조회 성공")).toBeInTheDocument();
```

callback 확인:

```tsx
await waitFor(() => {
  expect(onSubmit).toHaveBeenCalledTimes(1);
});
```

주의:

```text
비동기 UI에 getBy 사용 금지
findBy에는 await 필요
userEvent에는 await 필요
waitFor 남용 금지
mockResolvedValue / mockRejectedValue 명확히 설정
```

나쁜 예:

```tsx
expect(screen.getByText("조회 성공")).toBeInTheDocument();
```

좋은 예:

```tsx
expect(await screen.findByText("조회 성공")).toBeInTheDocument();
```

---

### [FAQ]

Q. 비동기 UI는 어떻게 테스트해?
A. 화면 요소가 나중에 나타나면 `await screen.findBy...`를 사용한다.

Q. findBy와 waitFor 중 뭐가 좋아?
A. 요소가 나타나는 것을 기다릴 때는 findBy가 더 간단하고 명확하다.

Q. getBy를 쓰면 왜 실패해?
A. getBy는 즉시 요소를 찾기 때문에 API 응답 후 렌더링되는 요소를 기다리지 못한다.

---

## 6.2 userEvent Await Rule

### [개념]

`userEvent`는 실제 사용자 이벤트 흐름에 가깝게 동작하며 비동기 처리를 포함할 수 있다.

따라서 `user.type`, `user.click`, `user.clear`, `user.selectOptions` 같은 사용자 이벤트에는 `await`를 사용하는 것이 안전하다.

---

### [핵심]

- userEvent.setup
- await user.click
- await user.type
- await user.clear
- await user.selectOptions
- await user.keyboard
- async event flow
- act warning 방지
- stable test

---

### [실무]

권장 예:

```tsx
const user = userEvent.setup();

await user.type(screen.getByLabelText("검색어"), "축제");
await user.click(screen.getByRole("button", { name: "검색" }));

expect(await screen.findByText("검색 결과")).toBeInTheDocument();
```

지양 예:

```tsx
user.type(screen.getByLabelText("검색어"), "축제");
user.click(screen.getByRole("button", { name: "검색" }));
```

주의:

```text
await 누락
→ act warning
→ 비동기 상태 업데이트 누락
→ 테스트 불안정
```

---

### [FAQ]

Q. userEvent에 await가 필요한 이유는?
A. userEvent는 실제 이벤트 흐름을 비동기로 처리할 수 있어 await를 사용하는 것이 안전하다.

Q. click도 await 해야 해?
A. 권장한다. click 이후 상태 업데이트가 발생할 수 있기 때문이다.

Q. await를 빼면 어떤 문제가 생겨?
A. act warning, assertion 타이밍 오류, 불안정한 테스트가 발생할 수 있다.

---

# 7. Debugging Rules

## 7.1 screen.debug Rules

### [개념]

`screen.debug()`는 현재 테스트 DOM 상태를 출력해 query 실패 원인을 확인하는 디버깅 도구다.

요소를 찾지 못하거나 예상 UI가 표시되지 않을 때 사용한다.

---

### [핵심]

사용 상황:

- query failed
- text not found
- role not found
- async UI not rendered
- provider missing
- mock data mismatch
- conditional rendering issue
- unexpected DOM result

---

### [실무]

예:

```tsx
render(<FestivalListPage />);

screen.debug();
```

특정 요소만 출력:

```tsx
const form = screen.getByRole("form");
screen.debug(form);
```

Debug Flow:

```text
query 실패
→ screen.debug 확인
→ 실제 DOM 텍스트 확인
→ role / accessible name 확인
→ 비동기 렌더링 여부 확인
→ Provider 누락 확인
→ mock 응답 확인
```

주의:

```text
screen.debug는 디버깅용
최종 테스트 코드에 남발하지 않음
```

---

### [FAQ]

Q. getByText가 못 찾으면 뭘 먼저 확인해?
A. screen.debug로 현재 DOM에 어떤 텍스트가 있는지 확인한다.

Q. getByRole이 실패하면 screen.debug만 보면 돼?
A. DOM 구조와 함께 accessible role, accessible name도 확인해야 한다.

Q. screen.debug를 테스트 코드에 남겨도 돼?
A. 디버깅 후 제거하는 것이 좋다.

---

## 7.2 Testing Playground

### [개념]

Testing Playground는 현재 DOM에서 어떤 Testing Library query가 적합한지 확인하는 도구다.

query 선택이 어렵거나 getByRole 실패 원인을 찾을 때 유용하다.

---

### [핵심]

- Testing Playground
- query suggestion
- accessible query
- getByRole
- accessible name
- label text
- test query debugging
- query priority

---

### [실무]

사용 상황:

```text
어떤 query를 써야 할지 모름
getByRole이 실패함
accessible name 확인 필요
text query보다 좋은 query 찾기
testId 사용 전 대안 찾기
```

권장:

```text
getByRole
→ getByLabelText
→ getByPlaceholderText
→ getByText
→ getByTestId
```

주의:

- 추천 query를 그대로 쓰기 전에 사용자 관점인지 확인
- testId 추천은 최후 수단인지 검토
- query 실패는 접근성 개선 신호일 수 있음

---

### [FAQ]

Q. Testing Playground는 언제 써?
A. 어떤 query를 써야 할지 모르거나 role/name 기반 query가 실패할 때 사용한다.

Q. Testing Playground가 추천한 query는 무조건 맞아?
A. 아니다. 사용자 관점과 query priority에 맞는지 검토해야 한다.

Q. getByRole이 실패하면 Component 문제일 수 있어?
A. 가능하다. semantic HTML이나 accessible name이 부족할 수 있다.

---

# 8. RTL Anti Pattern

## 8.1 Common RTL Anti Patterns

### [개념]

React Testing Library Anti Pattern은 RTL 철학과 맞지 않아 테스트 유지보수성과 신뢰도를 떨어뜨리는 작성 방식이다.

---

### [핵심]

Anti Pattern:

- container.querySelector 남용
- data-testid 우선 사용
- internal state 검증
- implementation function 직접 호출
- userEvent await 누락
- getBy로 async UI 검증
- waitFor 안에 userEvent 실행
- waitFor 남용
- snapshot-only test
- CSS class 중심 assertion
- Provider 누락
- cleanup과 mock reset 혼동
- 실제 API 호출

---

### [실무]

나쁜 예:

```tsx
const button = container.querySelector(".save-button");
fireEvent.click(button!);
```

좋은 예:

```tsx
await user.click(screen.getByRole("button", { name: "저장" }));
```

나쁜 예:

```tsx
await waitFor(() => {
  user.click(screen.getByRole("button", { name: "저장" }));
});
```

좋은 예:

```tsx
await user.click(screen.getByRole("button", { name: "저장" }));

expect(await screen.findByText("저장되었습니다.")).toBeInTheDocument();
```

검수 기준:

```text
screen query를 사용하는가?
role / label / text 우선인가?
userEvent에 await가 있는가?
비동기 결과는 findBy로 기다리는가?
사용자 결과를 검증하는가?
```

---

### [FAQ]

Q. container.querySelector는 쓰면 안 돼?
A. 최후 수단으로만 사용한다. 먼저 role, label, text 기반 query를 사용한다.

Q. waitFor 안에서 userEvent를 실행해도 돼?
A. 지양한다. 사용자 이벤트를 먼저 실행하고 결과 assertion을 waitFor나 findBy로 기다린다.

Q. snapshot-only test는 왜 문제야?
A. 사용자의 실제 행동과 결과를 명확히 검증하지 못하고 의미 없는 변경에도 자주 깨질 수 있다.

---

# 9. Part02 Summary

## 9.1 React Testing Library Final Rule

### [개념]

Frontend Testing Part02는 React Testing Library의 기본 철학, render, screen, custom render, async UI 처리 기준을 정의한다.

이 Part의 목적은 Agent가 React Component를 사용자 관점으로 테스트하고 구현 세부사항 테스트를 피하도록 만드는 것이다.

---

### [핵심]

최종 기준:

- React Testing Library는 사용자 관점 테스트 도구
- render로 Component 렌더링
- screen으로 현재 화면 query
- role / label / text 기반 query 우선
- 내부 state / private function 테스트 지양
- custom render로 Provider 중복 제거
- QueryClient는 테스트마다 새로 생성
- jest-dom matcher 사용
- 비동기 UI는 findBy / waitFor 사용
- userEvent는 await 사용
- screen.debug는 query 실패 디버깅에 사용
- RTL Anti Pattern 방지

---

### [실무]

Agent 작업 Flow:

```text
Component Test Request
→ Identify User Behavior
→ render Component
→ Use screen Query
→ Use userEvent with await
→ Wait Async UI with findBy
→ Assert Visible Result
→ Check Provider Need
→ Check RTL Anti Pattern
```

Part03 이후 연결:

```text
Part02 React Testing Library
→ Part03 Query Rules
→ Part04 User Event
→ Part05 Unit Test
→ Part06 Component Test
→ Part07 Form Testing
→ Part08 API Mocking
```

---

### [FAQ]

Q. Part02의 최종 목적은 뭐야?
A. Frontend Agent가 React Testing Library로 사용자 관점 Component 테스트를 작성하게 만드는 것이다.

Q. RTL에서 가장 중요한 규칙은 뭐야?
A. 사용자가 인식할 수 있는 요소를 찾고 사용자 행동 후 화면 결과를 검증하는 것이다.

Q. Part02 다음에는 어떤 내용이 이어져야 해?
A. getByRole, getByLabelText, getByText, findBy, queryBy 같은 Query Rules가 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. React Testing Library는 뭐야?
A. React Component를 사용자 관점에서 테스트하기 위한 테스트 유틸리티다.

Q. React Testing Library의 핵심 철학은 뭐야?
A. 내부 구현보다 사용자가 보는 화면과 조작 결과를 테스트하는 것이다.

Q. React Testing Library는 어떤 테스트에 주로 사용해?
A. Component Test와 Integration Test에 주로 사용한다.

Q. React Testing Library만 있으면 테스트가 전부 가능해?
A. 아니다. Vitest 또는 Jest, jest-dom, userEvent, 필요 시 MSW와 함께 사용한다.

Q. React Testing Library는 API Mock도 해줘?
A. 아니다. API Mock은 vi.mock, jest.mock, MSW 같은 도구로 처리한다.

Q. render는 뭐야?
A. React Component를 테스트 DOM에 렌더링하는 React Testing Library 함수다.

Q. screen은 왜 써?
A. 현재 테스트 화면에서 요소를 찾는 방식이 명확하고 React Testing Library 권장 패턴이기 때문이다.

Q. render 결과에서 getByText를 꺼내 쓰면 안 돼?
A. 가능하지만 screen을 사용하는 방식이 더 일관적이고 가독성이 좋다.

Q. cleanup은 직접 해야 해?
A. 대부분의 현대 테스트 환경에서는 각 테스트 후 자동 cleanup이 수행된다.

Q. cleanup과 mock reset은 같은 거야?
A. 아니다. cleanup은 DOM 정리이고 mock reset은 mock 함수 상태 정리다.

Q. Provider Wrapper는 왜 필요해?
A. Component가 Router, QueryClient, Auth Context 같은 외부 context에 의존할 때 테스트 환경에서도 제공해야 하기 때문이다.

Q. custom render는 언제 만들어?
A. Router, QueryClient, Auth Provider처럼 여러 테스트에서 반복되는 설정이 생기면 만든다.

Q. renderWithProviders는 뭐야?
A. 테스트에 필요한 Provider들을 공통으로 감싸는 custom render utility다.

Q. No QueryClient set 오류는 왜 나?
A. QueryClientProvider 없이 TanStack Query Hook을 사용하는 Component를 렌더링했기 때문이다.

Q. useNavigate may be used only in context 오류는 왜 나?
A. Router Provider 없이 useNavigate를 사용하는 Component를 테스트했기 때문이다.

Q. 테스트에서 QueryClient를 전역으로 재사용해도 돼?
A. 권장하지 않는다. Query Cache가 테스트 간 공유되어 불안정해질 수 있다.

Q. 테스트에서 retry false를 설정하는 이유는?
A. 실패 테스트가 재시도 때문에 느려지거나 예측하기 어려워지는 것을 막기 위해서다.

Q. jest-dom은 뭐야?
A. DOM 테스트에 필요한 toBeInTheDocument, toBeVisible, toBeDisabled 같은 custom matcher를 제공한다.

Q. Vitest에서도 jest-dom을 쓸 수 있어?
A. 가능하다. `@testing-library/jest-dom/vitest`를 setup 파일에 import한다.

Q. toBeInTheDocument와 toBeVisible은 달라?
A. 다르다. toBeInTheDocument는 DOM 존재 여부이고 toBeVisible은 사용자가 볼 수 있는 상태인지 확인한다.

Q. 사용자 중심 테스트는 뭐야?
A. 사용자가 보는 요소와 수행하는 행동, 그리고 화면 결과를 기준으로 작성하는 테스트다.

Q. 내부 state를 테스트하면 왜 안 좋아?
A. 구현 변경만으로 테스트가 깨질 수 있고 사용자 기능 검증과 직접 연결되지 않을 수 있다.

Q. Behavior Test가 뭐야?
A. 사용자가 입력, 클릭, 이동한 뒤 화면에 어떤 결과가 나타나는지 검증하는 테스트다.

Q. Implementation Detail Test는 뭐야?
A. 내부 state, private function, className, DOM 구조처럼 사용자가 직접 인식하지 못하는 구현 세부사항을 검증하는 테스트다.

Q. getByRole을 많이 쓰는 이유는 뭐야?
A. 사용자가 보조기술로 인식하는 역할과 이름을 기준으로 찾기 때문에 실제 사용성에 가깝다.

Q. callback 호출 검증은 하면 안 돼?
A. 할 수 있다. 다만 가능하면 callback 이후 UI 결과까지 함께 검증하는 것이 좋다.

Q. 비동기 UI는 어떻게 테스트해?
A. 화면 요소가 나중에 나타나면 `await screen.findBy...`를 사용한다.

Q. findBy와 waitFor 중 뭐가 좋아?
A. 요소가 나타나는 것을 기다릴 때는 findBy가 더 간단하고 명확하다.

Q. userEvent에 await가 필요한 이유는?
A. userEvent는 실제 이벤트 흐름을 비동기로 처리할 수 있어 await를 사용하는 것이 안전하다.

Q. click도 await 해야 해?
A. 권장한다. click 이후 상태 업데이트가 발생할 수 있기 때문이다.

Q. screen.debug는 언제 써?
A. query가 요소를 찾지 못하거나 예상 UI가 표시되지 않을 때 현재 DOM을 확인하기 위해 사용한다.

Q. getByText가 못 찾으면 뭘 먼저 확인해?
A. screen.debug로 현재 DOM에 어떤 텍스트가 있는지 확인한다.

Q. Testing Playground는 언제 써?
A. 어떤 query를 써야 할지 모르거나 role/name 기반 query가 실패할 때 사용한다.

Q. container.querySelector는 써도 돼?
A. 최후 수단으로만 사용한다. 먼저 role, label, text 기반 query를 사용한다.

Q. waitFor 안에서 userEvent를 실행해도 돼?
A. 지양한다. 사용자 이벤트를 먼저 실행하고 결과 assertion을 waitFor나 findBy로 기다린다.

Q. RTL Anti Pattern은 뭐가 있어?
A. container.querySelector 남용, data-testid 우선 사용, internal state 검증, userEvent await 누락, getBy로 async UI 검증, snapshot-only test 등이 있다.

Q. Part02 React Testing Library의 최종 목표는 뭐야?
A. Frontend Agent가 React Testing Library로 사용자 관점 Component 테스트를 작성하게 만드는 것이다.
