# Frontend Testing Part14 - Test Structure

---

# 1. Test Structure Overview

## 1.1 Test Structure Definition

### [개념]

Test Structure는 Frontend 테스트 파일, 테스트 유틸리티, mock 데이터, setup 파일, Provider wrapper, naming convention을 일관되게 구성하는 기준이다.

Frontend Testing에서 구조가 정리되어 있으면 테스트 작성 속도, 유지보수성, Agent 코드 생성 품질이 크게 좋아진다.

### [핵심]

- Test Structure
- Test File Structure
- Test Naming
- describe
- test
- arrange act assert
- render utility
- renderWithProviders
- test setup
- mock data
- fixture
- factory
- test helper
- mock reset
- Provider wrapper
- QueryClient setup
- Router setup
- Auth setup

### [실무]

좋은 Test Structure는 다음 흐름을 가진다.

```text
Test File
→ imports
→ mocks
→ test data factory
→ render helper
→ describe block
→ test cases
→ assertions
→ cleanup / reset
```

좋은 테스트 구조:

```text
테스트 파일 위치가 예측 가능함
테스트 이름이 사용자 시나리오를 설명함
Provider 설정이 중복되지 않음
Mock 데이터가 실제 API shape와 일치함
테스트 간 상태가 공유되지 않음
공통 유틸리티가 과도하게 숨기지 않음
```

나쁜 테스트 구조:

```text
테스트 파일 위치가 제각각임
render 설정이 모든 파일에 복붙됨
테스트 이름이 renders / works 수준임
큰 fixture가 테스트 의도를 가림
전역 QueryClient나 Auth Store가 테스트 간 공유됨
mock reset이 없어 테스트 순서에 의존함
```

### [FAQ]

Q. Test Structure는 뭐야?
A. 테스트 파일, 유틸리티, mock, fixture, Provider wrapper를 일관되게 구성하는 기준이다.

Q. Test Structure가 왜 중요해?
A. 테스트를 빠르게 작성하고 안정적으로 유지보수하며 Agent가 일관된 테스트 코드를 생성할 수 있게 한다.

Q. 좋은 테스트 구조의 핵심은 뭐야?
A. 위치, 이름, setup, mock 데이터, reset 규칙이 예측 가능하고 테스트 의도가 명확한 것이다.

## 1.2 Test Structure Scope

### [개념]

Test Structure Scope는 Frontend 테스트 프로젝트에서 어떤 구조와 규칙을 표준화할지 정하는 범위다.

테스트 코드 자체뿐 아니라 setup, provider, mock, fixture, naming, cleanup까지 포함한다.

### [핵심]

포함 범위:

- test file location
- test file naming
- describe naming
- test case naming
- arrange act assert
- renderWithProviders
- renderWithRouter
- renderWithQueryClient
- mock data factory
- fixture location
- setupTests
- mock reset
- MSW setup
- QueryClient isolation
- custom matcher setup
- test helper rules

제외 또는 별도 문서 대상:

- E2E 테스트 전체 구조
- CI/CD 테스트 실행 전략
- 브라우저 호환성 테스트
- Visual Regression 전용 구조
- 실제 Backend 통합 테스트 구조

### [실무]

이 문서의 목적:

```text
Frontend Agent가 테스트 코드를 생성할 때
어디에 파일을 만들고
어떤 이름을 쓰고
어떤 Provider를 감싸고
어떤 mock 데이터를 사용하고
어떻게 reset할지 결정하게 한다.
```

테스트 구조의 우선순위:

```text
명확성
→ 독립성
→ 재사용성
→ 유지보수성
→ 속도
```

주의:

```text
재사용성을 과도하게 높이면 테스트 의도가 숨겨질 수 있음
중복 제거보다 읽기 쉬운 테스트가 우선인 경우가 많음
```

### [FAQ]

Q. Test Structure는 테스트 코드 작성법만 말해?
A. 아니다. 파일 위치, provider wrapper, mock data, reset, setup 파일까지 포함한다.

Q. 테스트 유틸리티는 많이 만들수록 좋아?
A. 아니다. 반복을 줄이되 테스트 의도를 숨기지 않는 수준이 좋다.

Q. Test Structure의 우선순위는 뭐야?
A. 명확성, 독립성, 재사용성, 유지보수성 순으로 보는 것이 좋다.

# 2. Test File Location

## 2.1 Co-located Test File

### [개념]

Co-located Test File은 테스트 파일을 테스트 대상 파일 근처에 두는 방식이다.

Component, hook, utility와 테스트를 함께 관리하기 쉬워 Frontend 프로젝트에서 자주 사용된다.

### [핵심]

- colocated test
- adjacent test file
- component test
- hook test
- utility test
- feature folder
- maintainability
- discoverability

### [실무]

예:

```text
src/components/Button/Button.tsx
src/components/Button/Button.test.tsx

src/features/festival/components/FestivalCard.tsx
src/features/festival/components/FestivalCard.test.tsx

src/features/auth/components/LoginForm.tsx
src/features/auth/components/LoginForm.test.tsx
```

장점:

```text
테스트 대상과 테스트 파일을 함께 찾기 쉬움
Component 변경 시 테스트 수정 위치가 명확함
Feature 단위 유지보수가 쉬움
```

주의:

```text
테스트 파일이 너무 많아 폴더가 복잡해질 수 있음
공통 fixture와 helper 위치는 별도 정리 필요
```

권장:

- Component / hook / utility 테스트는 대상 파일 근처 배치
- feature 단위 폴더 구조와 함께 사용
- 테스트 파일명은 `.test.tsx` 또는 `.test.ts`로 통일
- 복잡한 Page Flow 테스트는 별도 `__tests__` 폴더 검토 가능

### [FAQ]

Q. Co-located Test File은 뭐야?
A. 테스트 파일을 테스트 대상 파일 옆에 두는 방식이다.

Q. Component 테스트는 어디에 두는 게 좋아?
A. Component 파일 근처에 `.test.tsx`로 두면 찾고 관리하기 쉽다.

Q. Co-located 방식의 단점은 뭐야?
A. 테스트 파일이 많아지면 폴더가 복잡해질 수 있어 공통 helper 구조를 함께 정리해야 한다.

## 2.2 Feature Test Folder

### [개념]

Feature Test Folder는 특정 feature의 테스트를 `__tests__` 또는 `tests` 폴더에 모아두는 방식이다.

Page Flow, Integration Style Test, 여러 Component가 함께 동작하는 테스트에 적합하다.

### [핵심]

- feature test folder
- **tests**
- integration test
- page test
- route test
- auth flow test
- feature scenario
- test grouping

### [실무]

예:

```text
src/features/festival/
├ api/
├ components/
├ pages/
├ hooks/
└ __tests__/
  ├ FestivalSearchPage.test.tsx
  ├ FestivalDetailPage.test.tsx
  └ FestivalFavoriteFlow.test.tsx
```

적합한 테스트:

```text
FestivalSearchPage의 검색 / 필터 / 결과 표시
ReviewSection의 리뷰 조회 / 등록 / 목록 갱신
Login Flow의 성공 / 실패 / redirect
Protected Route 접근 흐름
```

권장:

- 여러 파일이 함께 동작하는 테스트는 feature `__tests__`에 배치
- 단일 Component 테스트는 Component 옆 배치 가능
- feature test folder는 scenario 중심 naming 사용
- 너무 많은 테스트가 한 폴더에 모이면 하위 폴더 분리

### [FAQ]

Q. Feature Test Folder는 언제 써?
A. 여러 Component, API mock, Provider가 함께 필요한 Page 또는 Flow 테스트에 적합하다.

Q. Component 옆 테스트와 Feature Test Folder 중 뭐가 좋아?
A. 단일 Component는 옆에 두고, Page/Flow 테스트는 feature test folder에 두는 방식이 실무적으로 좋다.

Q. `__tests__` 이름은 필수야?
A. 필수는 아니다. 팀 컨벤션에 따라 `__tests__`, `tests`, `test` 중 하나로 통일하면 된다.

## 2.3 Global Test Utility Folder

### [개념]

Global Test Utility Folder는 여러 테스트에서 공통으로 사용하는 render helper, mock server, fixture factory, setup helper를 모아두는 폴더다.

### [핵심]

- test utils
- renderWithProviders
- createTestQueryClient
- mock server
- MSW handlers
- fixture factory
- setup file
- custom matcher
- shared helper

### [실무]

예:

```text
src/test/
├ setupTests.ts
├ renderWithProviders.tsx
├ createTestQueryClient.ts
├ mockServer.ts
├ handlers/
│ ├ festivalHandlers.ts
│ └ authHandlers.ts
├ factories/
│ ├ festivalFactory.ts
│ ├ userFactory.ts
│ └ reviewFactory.ts
└ utils/
  └ deferred.ts
```

권장:

- 전역 테스트 도구는 `src/test` 또는 `test` 폴더에 모음
- domain별 handler / factory 분리
- render utility는 Provider 조합별로 분리 가능
- 테스트 helper는 작고 명확하게 유지
- 실제 운영 코드와 test helper 의존 방향을 분리

주의:

```text
test utility가 너무 복잡하면 테스트 의도를 숨길 수 있음
필요한 Provider만 감싸는 작은 utility도 함께 제공
```

### [FAQ]

Q. Global Test Utility Folder에는 뭘 둬?
A. renderWithProviders, QueryClient 생성 함수, MSW server, fixture factory, setup 파일 등을 둔다.

Q. test utility를 운영 코드 폴더에 둬도 돼?
A. 가능하지만 `src/test`처럼 테스트 전용 폴더로 분리하는 것이 더 명확하다.

Q. render utility가 너무 커지면?
A. 목적별로 renderWithRouter, renderWithQueryClient, renderWithProviders처럼 분리한다.

# 3. Test File Naming

## 3.1 Test File Naming Rule

### [개념]

Test File Naming Rule은 테스트 파일 이름을 일관되게 작성하는 규칙이다.

파일명만 보고 어떤 대상을 테스트하는지 알 수 있어야 한다.

### [핵심]

- `.test.ts`
- `.test.tsx`
- `.spec.ts`
- `.spec.tsx`
- Component test
- Hook test
- Utility test
- Page test
- Flow test
- naming consistency

### [실무]

권장:

```text
Button.test.tsx
LoginForm.test.tsx
useAuth.test.ts
formatDate.test.ts
FestivalSearchPage.test.tsx
ProtectedRoute.test.tsx
```

피하기:

```text
test.tsx
ButtonTest.tsx
button_test.tsx
Button.check.tsx
festival.test.all.tsx
```

구분:

```text
.tsx
→ React Component / Page 테스트

.ts
→ utility / hook logic / mapper 테스트
```

권장:

- `.test.tsx` 또는 `.test.ts`로 통일
- Component 이름과 테스트 파일 이름 일치
- Flow 테스트는 시나리오 이름 사용
- 파일명에 지나치게 많은 조건을 넣지 않음

### [FAQ]

Q. `.test`와 `.spec` 중 뭐가 좋아?
A. 둘 다 가능하지만 프로젝트에서 하나로 통일하는 것이 중요하다.

Q. Component 테스트 파일은 `.tsx`를 써야 해?
A. JSX를 렌더링하면 `.test.tsx`가 적합하다.

Q. 파일명은 테스트 대상과 같아야 해?
A. 가능하면 같게 맞추는 것이 찾기 쉽다.

## 3.2 Scenario Test Naming

### [개념]

Scenario Test Naming은 Page Flow나 Integration Test 파일명을 사용자 시나리오 중심으로 작성하는 규칙이다.

단일 Component보다 흐름이 중요한 테스트에 사용한다.

### [핵심]

- scenario test
- flow test
- user journey
- page flow
- login flow
- search flow
- protected route flow
- mutation flow

### [실무]

좋은 예:

```text
LoginFlow.test.tsx
ProtectedRouteFlow.test.tsx
FestivalSearchFlow.test.tsx
ReviewCreateFlow.test.tsx
FavoriteToggleFlow.test.tsx
```

나쁜 예:

```text
Flow.test.tsx
Integration.test.tsx
PageTest.test.tsx
TestAll.test.tsx
```

파일명 기준:

```text
어떤 사용 흐름을 테스트하는가?
어떤 feature의 대표 scenario인가?
실패 시 어떤 기능을 봐야 하는가?
```

권장:

- Flow 테스트는 사용자 행동 중심 이름 사용
- 너무 많은 흐름을 한 파일에 넣지 않음
- Page 단위와 Flow 단위를 구분
- 파일명만 보고 테스트 목적이 드러나야 함

### [FAQ]

Q. Scenario Test Naming은 언제 필요해?
A. 여러 Component와 Route, API mock이 함께 동작하는 사용자 흐름 테스트에 필요하다.

Q. Integration.test.tsx 같은 이름은 왜 안 좋아?
A. 어떤 기능과 흐름을 테스트하는지 알기 어렵기 때문이다.

Q. Flow 테스트 파일에는 무엇을 기준으로 이름을 붙여?
A. LoginFlow, SearchFlow, ProtectedRouteFlow처럼 사용자 시나리오 기준으로 붙인다.

# 4. Test Case Naming

## 4.1 Test Name Rule

### [개념]

Test Name Rule은 개별 test 이름을 사용자 상황, 행동, 기대 결과가 드러나도록 작성하는 규칙이다.

좋은 테스트 이름은 실패했을 때 어떤 기능이 깨졌는지 바로 알려준다.

### [핵심]

좋은 test 이름 요소:

- user scenario
- condition
- action
- expected result
- visible UI
- domain term
- Korean test name
- behavior description

나쁜 이름:

- renders
- works
- test1
- should work
- click test
- component test
- state test

### [실무]

좋은 예:

```tsx
test("이메일을 입력하지 않고 로그인하면 이메일 오류 메시지를 표시한다", async () => {});

test("축제 목록 조회 성공 시 축제 제목을 표시한다", async () => {});

test("비로그인 사용자가 마이페이지에 접근하면 로그인 Page를 표시한다", () => {});

test("리뷰 등록 성공 후 리뷰 목록에 새 리뷰를 표시한다", async () => {});
```

나쁜 예:

```tsx
test("renders", () => {});
test("works", () => {});
test("click", () => {});
test("state true", () => {});
```

권장 구조:

```text
[조건] + [사용자 행동] + [기대 결과]
```

예:

```text
비로그인 사용자가 /admin 접근
→ Forbidden 또는 Login Page 표시

검색어를 입력하고 검색 버튼 클릭
→ 검색 결과 표시
```

### [FAQ]

Q. 좋은 테스트 이름은 어떤 이름이야?
A. 조건, 사용자 행동, 기대 결과가 드러나는 이름이다.

Q. test 이름을 한글로 써도 돼?
A. 가능하다. 팀이 한국어를 사용한다면 한글 test name은 의도를 명확히 전달할 수 있다.

Q. renders 같은 이름은 왜 안 좋아?
A. 무엇이 렌더링되어야 하는지 알 수 없어 실패 원인을 파악하기 어렵다.

## 4.2 describe Block Rule

### [개념]

describe Block은 관련 테스트를 그룹화하는 구조다.

Component, hook, utility, feature scenario 단위로 묶되 과도하게 중첩하지 않는다.

### [핵심]

- describe
- test grouping
- component name
- hook name
- utility name
- scenario group
- shallow nesting
- readability

### [실무]

Component 기준:

```tsx
describe("LoginForm", () => {
  test("이메일과 비밀번호 입력창을 표시한다", () => {});
  test("필수값이 없으면 오류 메시지를 표시한다", async () => {});
  test("로그인 성공 시 onLogin이 호출된다", async () => {});
});
```

Scenario 기준:

```tsx
describe("ProtectedRoute", () => {
  test("비로그인 사용자는 로그인 Page를 본다", () => {});
  test("로그인 사용자는 보호 Page를 본다", () => {});
});
```

과도한 중첩 지양:

```tsx
describe("LoginForm", () => {
  describe("when empty", () => {
    describe("when submit", () => {
      test("shows error", () => {});
    });
  });
});
```

권장:

- describe는 테스트 대상명 또는 scenario명 사용
- 중첩은 1~2단계 이내 유지
- test 이름만으로도 의도가 드러나게 작성
- describe에 구현 세부사항 이름을 넣지 않음

### [FAQ]

Q. describe는 꼭 써야 해?
A. 필수는 아니지만 관련 테스트를 묶어 가독성을 높이는 데 유용하다.

Q. describe는 어떤 이름이 좋아?
A. Component, hook, utility, scenario 이름이 좋다.

Q. describe를 많이 중첩하면 좋아?
A. 아니다. 중첩이 깊으면 테스트 이름이 읽기 어려워진다.

# 5. Test Body Structure

## 5.1 Arrange Act Assert Rule

### [개념]

Arrange Act Assert는 테스트 본문을 준비, 실행, 검증 단계로 나누는 구조다.

Frontend 테스트에서는 render와 mock 설정이 Arrange, userEvent가 Act, screen assertion이 Assert에 해당한다.

### [핵심]

- Arrange
- Act
- Assert
- Given When Then
- render
- userEvent
- assertion
- mock setup
- readability
- test flow

### [실무]

예:

```tsx
test("검색어를 입력하고 검색하면 검색 결과를 표시한다", async () => {
  // Arrange
  const user = userEvent.setup();

  vi.mocked(searchFestivals).mockResolvedValue([
    { festivalId: 1, title: "봄꽃 축제" },
  ]);

  render(<FestivalSearchPage />);

  // Act
  await user.type(screen.getByLabelText("검색어"), "봄꽃");
  await user.click(screen.getByRole("button", { name: "검색" }));

  // Assert
  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

주석은 선택:

```text
테스트가 짧으면 주석 생략 가능
테스트가 길면 Arrange / Act / Assert 주석이 가독성에 도움
```

권장:

- 준비와 행동과 검증을 섞지 않음
- userEvent는 Act 단계에 집중
- assertion은 사용자 결과 중심
- 하나의 테스트에는 하나의 핵심 목적
- 너무 긴 테스트는 분리 검토

### [FAQ]

Q. Arrange Act Assert는 뭐야?
A. 테스트를 준비, 실행, 검증 단계로 나누는 구조다.

Q. 주석을 꼭 써야 해?
A. 필수는 아니다. 테스트가 길거나 복잡할 때만 사용해도 된다.

Q. 한 테스트에 여러 assertion을 넣어도 돼?
A. 하나의 사용자 결과를 설명하는 관련 assertion은 괜찮지만 서로 다른 목적이면 분리하는 것이 좋다.

## 5.2 User Event Setup Placement

### [개념]

User Event Setup Placement는 `userEvent.setup()`을 테스트마다 생성하는 기준이다.

사용자 interaction이 있는 테스트에서는 각 test 안에서 user 객체를 생성한다.

### [핵심]

- userEvent.setup
- user object
- per test setup
- async interaction
- user.click
- user.type
- user.keyboard
- user.tab
- test isolation

### [실무]

권장:

```tsx
test("버튼을 클릭하면 모달을 연다", async () => {
  const user = userEvent.setup();

  render(<DeleteButton />);

  await user.click(screen.getByRole("button", { name: "삭제" }));

  expect(screen.getByRole("dialog", { name: "삭제 확인" })).toBeInTheDocument();
});
```

지양:

```tsx
const user = userEvent.setup();

test("...", async () => {
  await user.click(...);
});
```

권장:

- interaction test 안에서 user 생성
- userEvent에는 await 사용
- user 객체를 테스트 간 공유하지 않음
- keyboard / tab 테스트도 userEvent 사용
- fireEvent는 특수 상황에 제한

### [FAQ]

Q. userEvent.setup은 어디에 둬야 해?
A. interaction이 있는 각 test 내부에 두는 것이 좋다.

Q. user 객체를 전역으로 공유해도 돼?
A. 권장하지 않는다. 테스트 독립성을 위해 test마다 생성한다.

Q. userEvent에는 항상 await를 붙여?
A. click, type, keyboard, tab 같은 interaction은 await를 붙이는 것이 안전하다.

## 5.3 Assertion Placement Rule

### [개념]

Assertion Placement Rule은 테스트에서 assertion을 사용자 결과가 발생한 뒤 명확한 위치에 작성하는 규칙이다.

비동기 결과는 `findBy`, 사라짐 검증은 `queryBy`, 즉시 존재 검증은 `getBy`를 사용한다.

### [핵심]

- assertion
- expect
- getBy
- findBy
- queryBy
- waitFor
- toBeInTheDocument
- toHaveTextContent
- toHaveValue
- toBeDisabled
- user-visible result

### [실무]

즉시 존재:

```tsx
expect(screen.getByRole("button", { name: "저장" })).toBeInTheDocument();
```

비동기 등장:

```tsx
expect(await screen.findByText("저장되었습니다.")).toBeInTheDocument();
```

사라짐:

```tsx
expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
```

callback:

```tsx
expect(onSubmit).toHaveBeenCalledWith({
  email: "test@example.com",
});
```

권장:

- assertion은 테스트 마지막에 몰아두되 필요한 중간 상태는 명확히 확인
- 비동기 UI는 findBy
- absence 검증은 queryBy
- callback보다 UI 결과 우선
- waitFor는 필요한 경우에만 사용

### [FAQ]

Q. getBy, findBy, queryBy는 언제 써?
A. getBy는 즉시 존재, findBy는 비동기 등장, queryBy는 없음 검증에 사용한다.

Q. waitFor는 언제 써?
A. 요소 등장보다 callback 호출이나 특정 조건 변화 대기가 필요할 때 사용한다.

Q. assertion은 몇 개가 적당해?
A. 하나의 사용자 시나리오를 설명하는 데 필요한 만큼만 작성한다.

# 6. Render Utility Structure

## 6.1 renderWithProviders Rule

### [개념]

renderWithProviders는 테스트 대상 Component를 필요한 Provider로 감싸 렌더링하는 공통 유틸리티다.

Router, QueryClient, Auth, Theme, i18n 등 앱 공통 환경을 테스트에서 재현한다.

### [핵심]

- renderWithProviders
- Provider wrapper
- QueryClientProvider
- MemoryRouter
- AuthProvider
- ThemeProvider
- i18n Provider
- initialEntries
- authenticated option
- user option
- queryClient option

### [실무]

예:

```tsx
type RenderWithProvidersOptions = {
  initialEntries?: string[];
  authenticated?: boolean;
  user?: {
    userId: number;
    role: "ROLE_USER" | "ROLE_ADMIN";
    nickname?: string;
  };
};

function renderWithProviders(
  ui: React.ReactElement,
  options: RenderWithProvidersOptions = {},
) {
  const queryClient = createTestQueryClient();

  return render(
    <MemoryRouter initialEntries={options.initialEntries ?? ["/"]}>
      <QueryClientProvider client={queryClient}>
        <MockAuthProvider
          authenticated={options.authenticated ?? false}
          user={options.user}
        >
          {ui}
        </MockAuthProvider>
      </QueryClientProvider>
    </MemoryRouter>,
  );
}
```

사용:

```tsx
renderWithProviders(<MyPage />, {
  initialEntries: ["/mypage"],
  authenticated: true,
  user: {
    userId: 1,
    role: "ROLE_USER",
    nickname: "tester",
  },
});
```

권장:

- 테스트마다 새 QueryClient 생성
- initialEntries 옵션 제공
- Auth 상태 옵션 제공
- 필요 없는 Provider까지 과도하게 포함하지 않음
- 큰 renderWithProviders와 작은 render helper를 병행 가능

### [FAQ]

Q. renderWithProviders는 왜 필요해?
A. Router, QueryClient, Auth 같은 Provider 설정을 반복하지 않기 위해 필요하다.

Q. 모든 테스트에 renderWithProviders를 써야 해?
A. 아니다. Provider가 필요 없는 단순 Component는 기본 render가 더 명확하다.

Q. renderWithProviders가 너무 복잡해지면?
A. renderWithRouter, renderWithQueryClient처럼 목적별 utility로 분리한다.

## 6.2 renderWithRouter Rule

### [개념]

renderWithRouter는 Router Context가 필요한 Component를 테스트하기 위한 render utility다.

`Link`, `useNavigate`, `useParams`, `useSearchParams`를 사용하는 Component에 필요하다.

### [핵심]

- renderWithRouter
- MemoryRouter
- initialEntries
- Routes
- Route
- route path
- navigation test
- router context
- location display

### [실무]

간단한 wrapper:

```tsx
function renderWithRouter(
  ui: React.ReactElement,
  initialEntries: string[] = ["/"],
) {
  return render(
    <MemoryRouter initialEntries={initialEntries}>{ui}</MemoryRouter>,
  );
}
```

Route path가 필요한 경우:

```tsx
function renderWithRoute(
  ui: React.ReactElement,
  options: {
    initialEntry: string;
    path: string;
  },
) {
  return render(
    <MemoryRouter initialEntries={[options.initialEntry]}>
      <Routes>
        <Route path={options.path} element={ui} />
      </Routes>
    </MemoryRouter>,
  );
}
```

사용:

```tsx
renderWithRoute(<FestivalDetailPage />, {
  initialEntry: "/festivals/1",
  path: "/festivals/:festivalId",
});
```

권장:

- useParams 테스트는 Route path와 initialEntry 모두 제공
- Link/useNavigate 테스트는 목적지 Route도 함께 구성
- URL 직접 검증이 필요하면 LocationDisplay helper 사용
- Router와 Auth가 함께 필요하면 renderWithProviders 사용

### [FAQ]

Q. renderWithRouter는 언제 써?
A. Router Hook이나 Link를 사용하는 Component를 테스트할 때 사용한다.

Q. useParams 테스트에는 무엇이 필요해?
A. initialEntry와 Route path가 모두 필요하다.

Q. renderWithRouter와 renderWithProviders 중 무엇을 써?
A. Router만 필요하면 renderWithRouter, Auth/QueryClient도 필요하면 renderWithProviders를 쓴다.

## 6.3 renderWithQueryClient Rule

### [개념]

renderWithQueryClient는 TanStack Query를 사용하는 Component를 테스트하기 위한 render utility다.

테스트마다 새 QueryClient를 생성하고 retry false를 설정해야 한다.

### [핵심]

- renderWithQueryClient
- QueryClientProvider
- createTestQueryClient
- retry false
- cache isolation
- useQuery
- useMutation
- server state test

### [실무]

예:

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

function renderWithQueryClient(ui: React.ReactElement) {
  const queryClient = createTestQueryClient();

  return render(
    <QueryClientProvider client={queryClient}>{ui}</QueryClientProvider>,
  );
}
```

queryClient 반환이 필요한 경우:

```tsx
function renderWithQueryClient(ui: React.ReactElement) {
  const queryClient = createTestQueryClient();

  const result = render(
    <QueryClientProvider client={queryClient}>{ui}</QueryClientProvider>,
  );

  return {
    ...result,
    queryClient,
  };
}
```

권장:

- QueryClient 전역 재사용 금지
- retry false 설정
- cache seed가 필요한 경우 queryClient 반환
- Router/Auth가 필요하면 renderWithProviders 사용
- 테스트 간 cache 공유 방지

### [FAQ]

Q. renderWithQueryClient는 언제 써?
A. useQuery나 useMutation을 사용하는 Component를 테스트할 때 사용한다.

Q. QueryClient를 반환해야 해?
A. cache seed나 직접 queryClient 조작이 필요한 특수 테스트에서는 반환하면 유용하다.

Q. retry false는 render utility에 넣어야 해?
A. 테스트 기본 설정으로 넣는 것이 좋다.

# 7. Test Data Structure

## 7.1 Fixture Rule

### [개념]

Fixture는 테스트에서 사용하는 고정 mock 데이터다.

Frontend 테스트 fixture는 실제 API response shape와 일치해야 하며, 테스트 의도를 흐리지 않을 정도로 작아야 한다.

### [핵심]

- fixture
- mock data
- test data
- API response shape
- domain fixture
- small data
- realistic data
- no secret
- no personal data

### [실무]

좋은 fixture:

```ts
export const festivalFixture = {
  festivalId: 1,
  title: "봄꽃 축제",
  regionName: "서울",
  imageUrl: null,
  eventStartDate: "2026-04-01",
  eventEndDate: "2026-04-10",
};
```

나쁜 fixture:

```ts
export const festivalFixture = {
  id: 1,
  name: "축제",
  randomData: "불필요한 값",
};
```

Fixture 위치:

```text
src/test/fixtures/festivalFixture.ts
src/test/fixtures/userFixture.ts
src/test/fixtures/reviewFixture.ts
```

권장:

- Backend DTO와 field 이름 일치
- 테스트에 필요한 field만 포함
- null 가능 field 포함 테스트
- 실제 개인정보 / token / 운영 URL 금지
- 너무 큰 fixture 지양

### [FAQ]

Q. Fixture는 뭐야?
A. 테스트에서 반복적으로 사용하는 고정 mock 데이터다.

Q. Fixture는 실제 API response와 같아야 해?
A. 가능하면 실제 API 함수 반환 shape와 일치해야 한다.

Q. Fixture가 너무 크면 왜 문제야?
A. 테스트 의도를 흐리고 유지보수 비용을 높인다.

## 7.2 Test Data Factory Rule

### [개념]

Test Data Factory는 기본 mock 데이터를 만들고 필요한 field만 override할 수 있게 하는 함수다.

반복되는 fixture를 유연하게 생성할 때 사용한다.

### [핵심]

- test data factory
- factory function
- fixture factory
- override
- default values
- Partial
- domain factory
- mock builder
- readable data

### [실무]

예:

```ts
type FestivalResponse = {
  festivalId: number;
  title: string;
  regionName: string;
  imageUrl: string | null;
  eventStartDate: string;
  eventEndDate: string;
};

export function createFestivalResponse(
  override: Partial<FestivalResponse> = {},
): FestivalResponse {
  return {
    festivalId: 1,
    title: "봄꽃 축제",
    regionName: "서울",
    imageUrl: null,
    eventStartDate: "2026-04-01",
    eventEndDate: "2026-04-10",
    ...override,
  };
}
```

사용:

```tsx
vi.mocked(getFestivals).mockResolvedValue([
  createFestivalResponse({ title: "음악 축제" }),
]);
```

권장:

- 기본값은 정상 케이스
- 테스트별 차이만 override
- factory가 너무 많은 옵션을 숨기지 않게 함
- 실제 DTO 타입 재사용 가능
- 민감정보는 기본값에 넣지 않음

### [FAQ]

Q. Test Data Factory는 언제 써?
A. 같은 도메인 mock 데이터가 여러 테스트에서 반복될 때 사용한다.

Q. Fixture와 Factory 차이는 뭐야?
A. Fixture는 고정 데이터이고 Factory는 기본 데이터를 바탕으로 필요한 값을 바꿔 생성하는 함수다.

Q. Factory가 너무 복잡해지면?
A. 테스트 의도가 숨겨지므로 기본값과 override 중심으로 단순하게 유지한다.

## 7.3 Mock Data Security Rule

### [개념]

Mock Data Security Rule은 테스트 데이터에 실제 token, secret, 개인정보, 운영 URL, 결제 정보가 포함되지 않도록 하는 기준이다.

테스트 데이터도 코드 저장소에 남기 때문에 보안 검토 대상이다.

### [핵심]

금지 대상:

- real access token
- real refresh token
- API key
- OAuth secret
- production secret
- real email
- phone number
- address
- payment card
- real user data
- production URL
- private file path

### [실무]

좋은 예:

```ts
export const userFixture = {
  userId: 1,
  email: "test@example.com",
  nickname: "tester",
  role: "ROLE_USER",
};
```

좋은 token:

```ts
const loginResponse = {
  accessToken: "test-access-token",
};
```

나쁜 예:

```ts
const loginResponse = {
  accessToken: "실제_운영_TOKEN",
  email: "real-person@example.com",
};
```

권장:

- `test@example.com` 사용
- `test-access-token` 사용
- 실제 사용자 데이터 복붙 금지
- 운영 URL 대신 상대 경로 또는 test baseURL 사용
- snapshot과 fixture 모두 보안 검토

### [FAQ]

Q. 테스트 데이터에 실제 token을 넣어도 돼?
A. 절대 안 된다. 더미 token만 사용해야 한다.

Q. 실제 이메일은 괜찮아?
A. 권장하지 않는다. `test@example.com` 같은 테스트용 값을 사용한다.

Q. 테스트 데이터도 보안 검토가 필요해?
A. 필요하다. 코드 저장소에 남고 공유될 수 있기 때문이다.

# 8. Mock Structure

## 8.1 API Mock Module Structure

### [개념]

API Mock Module Structure는 API 함수 mock을 테스트 파일에서 어떻게 선언하고 관리할지 정하는 기준이다.

Mock 경로는 Component가 실제로 import하는 경로와 일치해야 한다.

### [핵심]

- API mock module
- vi.mock
- jest.mock
- import path
- named export
- default export
- mockResolvedValue
- mockRejectedValue
- mock reset

### [실무]

API 모듈:

```ts
export async function getFestivals() {}
export async function createReview() {}
```

테스트 mock:

```tsx
import {
  getFestivals,
  createReview,
} from "@/features/festival/api/festivalApi";

vi.mock("@/features/festival/api/festivalApi", () => ({
  getFestivals: vi.fn(),
  createReview: vi.fn(),
}));
```

사용:

```tsx
vi.mocked(getFestivals).mockResolvedValue([createFestivalResponse()]);
```

권장:

- mock 경로와 import 경로 일치
- named export / default export 구분
- 테스트마다 mockResolvedValue 설정
- afterEach에서 clear/reset
- 실제 API 호출 방지

### [FAQ]

Q. API mock 경로는 어떻게 정해?
A. Component가 실제로 import하는 API 모듈 경로와 일치해야 한다.

Q. mock이 적용되지 않으면 뭘 확인해?
A. import path, named/default export, mock 선언 위치를 확인한다.

Q. API mock은 공통 파일에 다 몰아도 돼?
A. 가능하지만 테스트 의도와 가까운 곳에 필요한 mock을 명확히 선언하는 것이 좋다.

## 8.2 MSW Structure

### [개념]

MSW Structure는 Mock Service Worker handler, test server, setup 파일을 어떻게 구성할지 정하는 기준이다.

MSW는 HTTP 요청 레벨 mock이므로 handler를 domain별로 분리하는 것이 좋다.

### [핵심]

- MSW
- handlers
- setupServer
- mockServer
- domain handler
- server.listen
- server.resetHandlers
- server.close
- unhandled request

### [실무]

폴더 예:

```text
src/test/msw/
├ server.ts
├ handlers.ts
└ handlers/
  ├ festivalHandlers.ts
  ├ authHandlers.ts
  └ reviewHandlers.ts
```

server.ts:

```ts
import { setupServer } from "msw/node";
import { handlers } from "./handlers";

export const server = setupServer(...handlers);
```

handlers.ts:

```ts
import { festivalHandlers } from "./handlers/festivalHandlers";
import { authHandlers } from "./handlers/authHandlers";

export const handlers = [...festivalHandlers, ...authHandlers];
```

setupTests.ts:

```ts
beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

권장:

- domain별 handler 분리
- 기본 handler는 정상 응답 중심
- 테스트별 error/empty는 server.use로 override
- unhandled request warning 방치 금지
- handler URL과 실제 request URL 일치

### [FAQ]

Q. MSW handler는 어디에 둬?
A. `src/test/msw/handlers`처럼 test 전용 폴더에 domain별로 두는 것이 좋다.

Q. server.resetHandlers는 왜 필요해?
A. 테스트별 override handler가 다음 테스트에 영향을 주지 않게 하기 위해 필요하다.

Q. unhandled request warning은 무시해도 돼?
A. 권장하지 않는다. handler 누락이나 URL 불일치 신호일 수 있다.

## 8.3 Mock Reset Structure

### [개념]

Mock Reset Structure는 테스트 간 mock 호출 기록, mock 구현, MSW handler, Query Cache가 공유되지 않도록 정리하는 규칙이다.

테스트 독립성을 위해 필수다.

### [핵심]

- mock reset
- vi.clearAllMocks
- vi.resetAllMocks
- vi.restoreAllMocks
- server.resetHandlers
- queryClient clear
- localStorage clear
- sessionStorage clear
- test isolation

### [실무]

기본 setup:

```ts
afterEach(() => {
  vi.clearAllMocks();
});
```

mock 구현도 초기화해야 하는 경우:

```ts
afterEach(() => {
  vi.resetAllMocks();
});
```

storage 초기화:

```ts
afterEach(() => {
  localStorage.clear();
  sessionStorage.clear();
});
```

MSW:

```ts
afterEach(() => {
  server.resetHandlers();
});
```

권장:

- 호출 기록은 clearAllMocks
- mock 구현까지 초기화가 필요하면 resetAllMocks
- spy 원본 복구는 restoreAllMocks
- storage 사용하는 테스트는 storage clear
- QueryClient는 테스트마다 새로 생성

### [FAQ]

Q. clearAllMocks와 resetAllMocks 차이는 뭐야?
A. clearAllMocks는 호출 기록만 지우고 resetAllMocks는 mock 구현도 초기화한다.

Q. 테스트마다 localStorage를 지워야 해?
A. storage를 사용하는 테스트가 있다면 테스트 간 영향 방지를 위해 지우는 것이 좋다.

Q. QueryClient도 reset해야 해?
A. 보통 테스트마다 새 QueryClient를 생성하는 것이 가장 안전하다.

# 9. Setup File Structure

## 9.1 setupTests Rule

### [개념]

setupTests 파일은 테스트 실행 전에 공통 matcher, mock server, cleanup, global mock을 설정하는 파일이다.

프로젝트 테스트 환경의 공통 진입점이다.

### [핵심]

- setupTests
- setup file
- jest-dom
- custom matcher
- MSW server
- global mock
- cleanup
- afterEach
- beforeAll
- afterAll
- test environment

### [실무]

예:

```ts
import "@testing-library/jest-dom/vitest";
import { server } from "./test/msw/server";

beforeAll(() => server.listen());

afterEach(() => {
  server.resetHandlers();
  vi.clearAllMocks();
});

afterAll(() => server.close());
```

Vitest 설정 예:

```ts
test: {
  environment: "jsdom",
  setupFiles: ["src/setupTests.ts"],
}
```

권장:

- jest-dom matcher 등록
- MSW server lifecycle 설정
- 공통 mock reset 설정
- jsdom 환경 설정 확인
- global mock은 최소화

주의:

```text
setupTests에 너무 많은 domain-specific mock을 넣으면 테스트 의도가 숨겨짐
```

### [FAQ]

Q. setupTests에는 뭘 넣어?
A. jest-dom, MSW server lifecycle, 공통 mock reset, 필요한 global mock을 넣는다.

Q. setupTests에 모든 API mock을 넣어도 돼?
A. 권장하지 않는다. domain-specific mock은 각 테스트나 MSW handler에 두는 것이 명확하다.

Q. jsdom 설정은 왜 필요해?
A. React Component 테스트는 DOM 환경이 필요하므로 jsdom 환경이 필요하다.

## 9.2 Global Mock Rule

### [개념]

Global Mock Rule은 jsdom에서 제공하지 않거나 테스트 환경에서 제어해야 하는 browser API를 전역 mock으로 설정하는 기준이다.

ResizeObserver, IntersectionObserver, matchMedia, scrollTo 등이 대표적이다.

### [핵심]

- global mock
- ResizeObserver
- IntersectionObserver
- matchMedia
- scrollTo
- localStorage
- window API
- browser API
- jsdom limitation

### [실무]

matchMedia mock:

```ts
Object.defineProperty(window, "matchMedia", {
  writable: true,
  value: vi.fn().mockImplementation((query) => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: vi.fn(),
    removeListener: vi.fn(),
    addEventListener: vi.fn(),
    removeEventListener: vi.fn(),
    dispatchEvent: vi.fn(),
  })),
});
```

ResizeObserver mock:

```ts
class ResizeObserverMock {
  observe() {}
  unobserve() {}
  disconnect() {}
}

window.ResizeObserver = ResizeObserverMock;
```

scrollTo mock:

```ts
window.scrollTo = vi.fn();
```

권장:

- jsdom에 없는 browser API만 mock
- global mock은 최소화
- 각 테스트에서 필요한 동작은 개별 mock으로 override
- 실제 브라우저 동작 검증은 E2E로 분리
- mock이 테스트 결과를 왜곡하지 않는지 확인

### [FAQ]

Q. matchMedia mock은 언제 필요해?
A. responsive hook이나 UI library가 matchMedia를 사용할 때 필요할 수 있다.

Q. ResizeObserver mock은 왜 필요해?
A. jsdom 환경에 ResizeObserver가 없어서 UI library나 layout hook 테스트가 실패할 수 있기 때문이다.

Q. global mock을 많이 넣어도 돼?
A. 필요한 것만 최소화하는 것이 좋다.

# 10. Test Helper Rules

## 10.1 Deferred Promise Helper

### [개념]

Deferred Promise Helper는 테스트에서 Promise의 resolve/reject 시점을 직접 제어하기 위한 helper다.

Loading → Success, Loading → Error 상태 전환 테스트에 유용하다.

### [핵심]

- deferred promise
- controlled promise
- resolve control
- reject control
- loading test
- async transition
- pending state

### [실무]

helper:

```ts
export function deferred<T>() {
  let resolve!: (value: T) => void;
  let reject!: (reason?: unknown) => void;

  const promise = new Promise<T>((res, rej) => {
    resolve = res;
    reject = rej;
  });

  return {
    promise,
    resolve,
    reject,
  };
}
```

사용:

```tsx
test("loading 후 성공 데이터를 표시한다", async () => {
  const request = deferred<Array<{ title: string }>>();

  vi.mocked(getFestivals).mockReturnValue(request.promise);

  renderWithQueryClient(<FestivalListPage />);

  expect(screen.getByRole("status")).toHaveTextContent("불러오는 중입니다.");

  request.resolve([{ title: "봄꽃 축제" }]);

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

권장:

- 상태 전환 테스트에 사용
- 일반 success/error 테스트에는 mockResolvedValue/mockRejectedValue가 더 단순
- resolve/reject 후 findBy로 UI 대기
- pending promise가 테스트를 hang시키지 않도록 주의

### [FAQ]

Q. Deferred Promise Helper는 언제 써?
A. loading 상태를 확인한 뒤 success 또는 error로 전환되는 흐름을 테스트할 때 사용한다.

Q. 모든 API 테스트에 deferred를 써야 해?
A. 아니다. 단순 성공/실패는 mockResolvedValue/mockRejectedValue가 더 간단하다.

Q. deferred 테스트가 멈추면?
A. resolve/reject를 호출했는지, 테스트가 기다리는 UI가 실제로 렌더링되는지 확인한다.

## 10.2 Location Display Helper

### [개념]

Location Display Helper는 Router 테스트에서 현재 location pathname이나 search 값을 확인하기 위한 작은 테스트 helper다.

URL 자체가 중요한 기능에서만 사용한다.

### [핵심]

- LocationDisplay
- useLocation
- pathname
- search
- query string
- router test
- URL assertion
- test helper

### [실무]

helper:

```tsx
function LocationDisplay() {
  const location = useLocation();

  return (
    <div data-testid="location-display">
      {location.pathname}
      {location.search}
    </div>
  );
}
```

사용:

```tsx
render(
  <MemoryRouter initialEntries={["/festivals"]}>
    <Routes>
      <Route path="/festivals" element={<FestivalSearchPage />} />
    </Routes>
    <LocationDisplay />
  </MemoryRouter>,
);
```

검증:

```tsx
expect(screen.getByTestId("location-display")).toHaveTextContent(
  "/festivals?keyword=봄꽃",
);
```

권장:

- URL 자체가 기능 요구사항일 때만 사용
- 일반 navigation은 Page UI 결과 검증 우선
- query string 동기화 테스트에 유용
- testId 사용을 helper 내부로 제한

### [FAQ]

Q. LocationDisplay는 언제 필요해?
A. query string이나 pathname 자체가 기능 요구사항일 때 필요하다.

Q. Router 이동 테스트에서 URL을 꼭 확인해야 해?
A. 보통은 목적지 Page UI 확인이 우선이고, URL 동기화가 중요할 때만 확인한다.

Q. data-testid를 써도 돼?
A. LocationDisplay 같은 테스트 전용 helper에서는 괜찮다.

# 11. Test Independence Rules

## 11.1 Test Isolation Rule

### [개념]

Test Isolation Rule은 각 테스트가 다른 테스트 실행 결과에 의존하지 않아야 한다는 규칙이다.

테스트는 어떤 순서로 실행되어도 같은 결과를 내야 한다.

### [핵심]

- test isolation
- independent test
- no shared state
- mock reset
- cache reset
- storage clear
- QueryClient isolation
- Auth state isolation
- deterministic data

### [실무]

공유하면 위험한 것:

```text
QueryClient cache
Auth Store state
localStorage token
mock call history
MSW override handler
global timer
Date mock
random value
DOM focus state
```

권장:

```text
테스트마다 새 QueryClient 생성
테스트마다 AuthProvider 초기 상태 설정
afterEach에서 mock clear
storage clear
MSW resetHandlers
동적 값 고정
```

나쁜 예:

```tsx
let authenticated = false;

test("login", () => {
  authenticated = true;
});

test("mypage", () => {
  expect(authenticated).toBe(true);
});
```

좋은 예:

```tsx
test("로그인 사용자는 마이페이지를 본다", () => {
  renderWithProviders(<MyPage />, {
    authenticated: true,
  });

  expect(
    screen.getByRole("heading", { name: "마이페이지" }),
  ).toBeInTheDocument();
});
```

### [FAQ]

Q. Test Isolation은 왜 중요해?
A. 테스트 순서에 따라 결과가 달라지는 flaky test를 방지하기 위해 중요하다.

Q. 가장 흔한 공유 상태는 뭐야?
A. QueryClient cache, Auth Store, localStorage, mock call history가 흔하다.

Q. 테스트 순서를 바꾸면 실패하는 경우 원인은?
A. 테스트 간 상태가 공유되고 있을 가능성이 높다.

## 11.2 Deterministic Test Rule

### [개념]

Deterministic Test는 같은 입력과 같은 mock 환경에서 항상 같은 결과를 내는 테스트다.

날짜, 랜덤 값, 네트워크, 타이머, locale 차이를 제어해야 한다.

### [핵심]

- deterministic test
- stable input
- fixed date
- fixed random
- no real network
- no actual time dependency
- no flaky timer
- stable order
- repeatable result

### [실무]

불안정한 요소:

```text
Date.now()
new Date()
Math.random()
crypto.randomUUID()
실제 API 호출
현재 timezone
정렬되지 않은 object keys
타이머 대기
외부 서비스 상태
```

개선:

```ts
expect(formatDate("2026-07-06")).toBe("2026.07.06");
```

랜덤 값 주입:

```ts
createTempId(() => "test-id-1");
```

권장:

- 날짜는 고정 입력 사용
- 랜덤 값은 mock 또는 주입
- 실제 네트워크 호출 금지
- list 정렬 결과는 명확히 제어
- 타이머 테스트는 fake timer 사용 시 userEvent와 충돌 주의

### [FAQ]

Q. Deterministic Test는 뭐야?
A. 언제 실행해도 같은 결과를 내는 안정적인 테스트다.

Q. 날짜 때문에 테스트가 실패하면?
A. 현재 날짜 대신 고정 날짜 입력을 사용하거나 Date mock을 사용한다.

Q. 랜덤 id가 있으면 어떻게 해?
A. id 생성 함수를 주입하거나 mock해서 고정 값으로 만든다.

# 12. Test Structure Anti Pattern

## 12.1 Common Test Structure Anti Patterns

### [개념]

Test Structure Anti Pattern은 테스트 파일과 유틸리티 구조가 복잡하거나 불안정해져 유지보수를 어렵게 만드는 잘못된 방식이다.

### [핵심]

Anti Pattern:

- 테스트 파일 위치가 제각각
- renders / works 같은 test name
- describe 과도한 중첩
- 전역 QueryClient 재사용
- userEvent 전역 공유
- fixture가 너무 큼
- mock data shape 불일치
- setupTests에 domain mock 과다
- renderWithProviders가 모든 것을 숨김
- test 간 localStorage 공유
- MSW handler reset 누락
- mock reset 누락
- 테스트가 실행 순서에 의존
- 실제 token / 개인정보 사용

### [실무]

나쁜 예:

```tsx
const queryClient = new QueryClient();
const user = userEvent.setup();

test("works", async () => {
  render(
    <QueryClientProvider client={queryClient}>
      <LoginForm />
    </QueryClientProvider>,
  );

  await user.click(screen.getByText("OK"));
});
```

좋은 예:

```tsx
test("이메일과 비밀번호를 입력하고 로그인하면 마이페이지를 표시한다", async () => {
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

검수 기준:

```text
테스트 이름만 보고 목적을 알 수 있는가?
Provider와 mock이 명확한가?
테스트 간 상태가 공유되지 않는가?
사용자 결과를 검증하는가?
테스트 데이터가 안전한가?
```

### [FAQ]

Q. Test Structure에서 가장 흔한 실수는 뭐야?
A. 전역 QueryClient나 userEvent를 공유하고, 테스트 이름을 모호하게 작성하는 것이다.

Q. renderWithProviders가 너무 많은 걸 숨기면 문제야?
A. 그렇다. 테스트에 필요한 상태와 Provider가 무엇인지 알기 어려워질 수 있다.

Q. fixture가 큰 게 왜 문제야?
A. 테스트 의도를 가리고 실제로 필요한 데이터가 무엇인지 알기 어렵게 만든다.

# 13. Test Structure Checklist

## 13.1 Test Structure Checklist

### [개념]

Test Structure Checklist는 Frontend 테스트 파일과 유틸리티가 일관성, 독립성, 가독성, 보안 기준을 만족하는지 검수하는 기준이다.

### [핵심]

Checklist:

```md
- [ ] 테스트 파일 위치가 프로젝트 컨벤션과 일치하는가?
- [ ] 테스트 파일명이 테스트 대상 또는 scenario를 명확히 나타내는가?
- [ ] `.test.tsx` / `.test.ts` naming이 일관적인가?
- [ ] describe 이름이 테스트 대상 또는 scenario를 나타내는가?
- [ ] test 이름이 조건 / 행동 / 기대 결과를 설명하는가?
- [ ] Arrange / Act / Assert 흐름이 읽히는가?
- [ ] userEvent.setup()을 각 test 내부에서 생성했는가?
- [ ] 필요한 Provider만 감쌌는가?
- [ ] QueryClient는 테스트마다 새로 생성되는가?
- [ ] Router initialEntries가 명확한가?
- [ ] Auth 상태가 test option으로 명확히 주입되는가?
- [ ] mock data shape가 실제 API와 일치하는가?
- [ ] fixture / factory가 과도하게 크지 않은가?
- [ ] mock reset / MSW reset / storage clear가 필요한 곳에 있는가?
- [ ] 테스트 간 상태 공유가 없는가?
- [ ] 실제 token / secret / 개인정보를 사용하지 않았는가?
- [ ] assertion이 사용자 결과 중심인가?
```

### [실무]

Agent Test Structure 작성 Flow:

```text
Identify Test Target
→ Choose Test File Location
→ Choose File Name
→ Prepare Render Utility
→ Prepare Mock Data
→ Write Scenario Test Name
→ Arrange API/Auth/Router State
→ Act with userEvent
→ Assert User-visible Result
→ Reset Shared State
→ Review Structure Checklist
```

예:

```text
Login Flow Test
→ src/features/auth/__tests__/LoginFlow.test.tsx
→ renderWithProviders
→ login API mock
→ test user input
→ assert MyPage heading or login error
→ no real token
```

### [FAQ]

Q. Test Structure Checklist의 핵심은 뭐야?
A. 파일 위치, 이름, Provider, mock data, reset, 사용자 결과 assertion이 일관되고 독립적인지 확인하는 것이다.

Q. 테스트 구조가 복잡해지면 어떻게 해?
A. 목적별 render utility와 fixture factory로 분리하되 테스트 의도가 숨겨지지 않게 한다.

Q. 테스트 구조 작성 전 무엇을 정해야 해?
A. 테스트 대상, 테스트 수준, 필요한 Provider, mock 방식, 파일 위치를 정해야 한다.

# 14. Part14 Summary

## 14.1 Test Structure Final Rule

### [개념]

Frontend Testing Part14는 테스트 파일 구조, naming, render utility, fixture, mock reset, setup file, test isolation 기준을 정의한다.

이 Part의 목적은 Agent가 일관되고 독립적이며 유지보수 가능한 Frontend 테스트 코드를 생성하게 만드는 것이다.

### [핵심]

최종 기준:

- 테스트 파일 위치는 co-located 또는 feature `__tests__`로 일관화
- Component 테스트는 대상 파일 근처 배치
- Page/Flow 테스트는 feature test folder에 배치
- 공통 test utility는 `src/test` 또는 test 전용 폴더에 배치
- 테스트 파일명은 `.test.tsx` / `.test.ts`로 통일
- test 이름은 조건, 행동, 기대 결과 중심
- describe는 테스트 대상 또는 scenario 이름 사용
- 테스트 본문은 Arrange / Act / Assert 흐름 유지
- userEvent.setup은 각 test 내부에서 생성
- renderWithProviders는 필요한 Provider만 감쌈
- QueryClient는 테스트마다 새로 생성
- Router는 MemoryRouter와 initialEntries 사용
- fixture와 factory는 실제 API shape와 일치
- mock reset, MSW reset, storage clear로 테스트 독립성 유지
- setupTests에는 공통 matcher와 최소 global mock만 배치
- 실제 token, secret, 개인정보 사용 금지
- 테스트는 실행 순서에 의존하지 않아야 함

### [실무]

Agent 작업 Flow:

```text
Test Generation Request
→ Select Test Level
→ Select File Location
→ Create Clear Test Name
→ Setup Minimal Providers
→ Create Safe Mock Data
→ Arrange Mock State
→ Act with userEvent
→ Assert User Result
→ Ensure Reset and Isolation
→ Check Test Structure Anti Pattern
```

Part15 이후 연결:

```text
Part14 Test Structure
→ Part15 Troubleshooting
→ Part16 Frontend Testing Review
→ Part17 Final Frontend Testing Rules
```

### [FAQ]

Q. Part14의 최종 목적은 뭐야?
A. Frontend Agent가 테스트 파일, 유틸리티, mock 데이터, setup을 일관되고 독립적으로 구성하게 만드는 것이다.

Q. Test Structure에서 가장 중요한 규칙은 뭐야?
A. 테스트가 명확한 이름과 독립적인 setup을 가지고 사용자 결과를 검증해야 한다는 것이다.

Q. Part14 다음에는 어떤 내용이 이어져야 해?
A. Query 실패, act warning, async timeout, mock 미적용 같은 Frontend Testing Troubleshooting 기준이 이어지는 것이 좋다.

# Retrieval Queries

### [FAQ]

Q. Test Structure는 뭐야?
A. 테스트 파일, 유틸리티, mock, fixture, Provider wrapper를 일관되게 구성하는 기준이다.

Q. Test Structure가 왜 중요해?
A. 테스트를 빠르게 작성하고 안정적으로 유지보수하며 Agent가 일관된 테스트 코드를 생성할 수 있게 한다.

Q. 좋은 테스트 구조의 핵심은 뭐야?
A. 위치, 이름, setup, mock 데이터, reset 규칙이 예측 가능하고 테스트 의도가 명확한 것이다.

Q. Test Structure는 테스트 코드 작성법만 말해?
A. 아니다. 파일 위치, provider wrapper, mock data, reset, setup 파일까지 포함한다.

Q. 테스트 유틸리티는 많이 만들수록 좋아?
A. 아니다. 반복을 줄이되 테스트 의도를 숨기지 않는 수준이 좋다.

Q. Co-located Test File은 뭐야?
A. 테스트 파일을 테스트 대상 파일 옆에 두는 방식이다.

Q. Component 테스트는 어디에 두는 게 좋아?
A. Component 파일 근처에 `.test.tsx`로 두면 찾고 관리하기 쉽다.

Q. Feature Test Folder는 언제 써?
A. 여러 Component, API mock, Provider가 함께 필요한 Page 또는 Flow 테스트에 적합하다.

Q. Component 옆 테스트와 Feature Test Folder 중 뭐가 좋아?
A. 단일 Component는 옆에 두고, Page/Flow 테스트는 feature test folder에 두는 방식이 실무적으로 좋다.

Q. Global Test Utility Folder에는 뭘 둬?
A. renderWithProviders, QueryClient 생성 함수, MSW server, fixture factory, setup 파일 등을 둔다.

Q. render utility가 너무 커지면?
A. 목적별로 renderWithRouter, renderWithQueryClient, renderWithProviders처럼 분리한다.

Q. `.test`와 `.spec` 중 뭐가 좋아?
A. 둘 다 가능하지만 프로젝트에서 하나로 통일하는 것이 중요하다.

Q. Component 테스트 파일은 `.tsx`를 써야 해?
A. JSX를 렌더링하면 `.test.tsx`가 적합하다.

Q. Scenario Test Naming은 언제 필요해?
A. 여러 Component와 Route, API mock이 함께 동작하는 사용자 흐름 테스트에 필요하다.

Q. Integration.test.tsx 같은 이름은 왜 안 좋아?
A. 어떤 기능과 흐름을 테스트하는지 알기 어렵기 때문이다.

Q. 좋은 테스트 이름은 어떤 이름이야?
A. 조건, 사용자 행동, 기대 결과가 드러나는 이름이다.

Q. test 이름을 한글로 써도 돼?
A. 가능하다. 팀이 한국어를 사용한다면 한글 test name은 의도를 명확히 전달할 수 있다.

Q. renders 같은 이름은 왜 안 좋아?
A. 무엇이 렌더링되어야 하는지 알 수 없어 실패 원인을 파악하기 어렵다.

Q. describe는 꼭 써야 해?
A. 필수는 아니지만 관련 테스트를 묶어 가독성을 높이는 데 유용하다.

Q. describe는 어떤 이름이 좋아?
A. Component, hook, utility, scenario 이름이 좋다.

Q. Arrange Act Assert는 뭐야?
A. 테스트를 준비, 실행, 검증 단계로 나누는 구조다.

Q. 한 테스트에 여러 assertion을 넣어도 돼?
A. 하나의 사용자 시나리오를 설명하는 관련 assertion은 괜찮지만 서로 다른 목적이면 분리하는 것이 좋다.

Q. userEvent.setup은 어디에 둬야 해?
A. interaction이 있는 각 test 내부에 두는 것이 좋다.

Q. user 객체를 전역으로 공유해도 돼?
A. 권장하지 않는다. 테스트 독립성을 위해 test마다 생성한다.

Q. userEvent에는 항상 await를 붙여?
A. click, type, keyboard, tab 같은 interaction은 await를 붙이는 것이 안전하다.

Q. getBy, findBy, queryBy는 언제 써?
A. getBy는 즉시 존재, findBy는 비동기 등장, queryBy는 없음 검증에 사용한다.

Q. waitFor는 언제 써?
A. 요소 등장보다 callback 호출이나 특정 조건 변화 대기가 필요할 때 사용한다.

Q. renderWithProviders는 왜 필요해?
A. Router, QueryClient, Auth 같은 Provider 설정을 반복하지 않기 위해 필요하다.

Q. 모든 테스트에 renderWithProviders를 써야 해?
A. 아니다. Provider가 필요 없는 단순 Component는 기본 render가 더 명확하다.

Q. renderWithRouter는 언제 써?
A. Router Hook이나 Link를 사용하는 Component를 테스트할 때 사용한다.

Q. useParams 테스트에는 무엇이 필요해?
A. initialEntry와 Route path가 모두 필요하다.

Q. renderWithQueryClient는 언제 써?
A. useQuery나 useMutation을 사용하는 Component를 테스트할 때 사용한다.

Q. QueryClient를 반환해야 해?
A. cache seed나 직접 queryClient 조작이 필요한 특수 테스트에서는 반환하면 유용하다.

Q. Fixture는 뭐야?
A. 테스트에서 반복적으로 사용하는 고정 mock 데이터다.

Q. Fixture는 실제 API response와 같아야 해?
A. 가능하면 실제 API 함수 반환 shape와 일치해야 한다.

Q. Test Data Factory는 언제 써?
A. 같은 도메인 mock 데이터가 여러 테스트에서 반복될 때 사용한다.

Q. Fixture와 Factory 차이는 뭐야?
A. Fixture는 고정 데이터이고 Factory는 기본 데이터를 바탕으로 필요한 값을 바꿔 생성하는 함수다.

Q. 테스트 데이터에 실제 token을 넣어도 돼?
A. 절대 안 된다. 더미 token만 사용해야 한다.

Q. API mock 경로는 어떻게 정해?
A. Component가 실제로 import하는 API 모듈 경로와 일치해야 한다.

Q. MSW handler는 어디에 둬?
A. `src/test/msw/handlers`처럼 test 전용 폴더에 domain별로 두는 것이 좋다.

Q. server.resetHandlers는 왜 필요해?
A. 테스트별 override handler가 다음 테스트에 영향을 주지 않게 하기 위해 필요하다.

Q. clearAllMocks와 resetAllMocks 차이는 뭐야?
A. clearAllMocks는 호출 기록만 지우고 resetAllMocks는 mock 구현도 초기화한다.

Q. 테스트마다 localStorage를 지워야 해?
A. storage를 사용하는 테스트가 있다면 테스트 간 영향 방지를 위해 지우는 것이 좋다.

Q. setupTests에는 뭘 넣어?
A. jest-dom, MSW server lifecycle, 공통 mock reset, 필요한 global mock을 넣는다.

Q. setupTests에 모든 API mock을 넣어도 돼?
A. 권장하지 않는다. domain-specific mock은 각 테스트나 MSW handler에 두는 것이 명확하다.

Q. matchMedia mock은 언제 필요해?
A. responsive hook이나 UI library가 matchMedia를 사용할 때 필요할 수 있다.

Q. ResizeObserver mock은 왜 필요해?
A. jsdom 환경에 ResizeObserver가 없어서 UI library나 layout hook 테스트가 실패할 수 있기 때문이다.

Q. Deferred Promise Helper는 언제 써?
A. loading 상태를 확인한 뒤 success 또는 error로 전환되는 흐름을 테스트할 때 사용한다.

Q. LocationDisplay는 언제 필요해?
A. query string이나 pathname 자체가 기능 요구사항일 때 필요하다.

Q. Test Isolation은 왜 중요해?
A. 테스트 순서에 따라 결과가 달라지는 flaky test를 방지하기 위해 중요하다.

Q. 가장 흔한 공유 상태는 뭐야?
A. QueryClient cache, Auth Store, localStorage, mock call history가 흔하다.

Q. Deterministic Test는 뭐야?
A. 언제 실행해도 같은 결과를 내는 안정적인 테스트다.

Q. 날짜 때문에 테스트가 실패하면?
A. 현재 날짜 대신 고정 날짜 입력을 사용하거나 Date mock을 사용한다.

Q. Test Structure에서 가장 흔한 실수는 뭐야?
A. 전역 QueryClient나 userEvent를 공유하고, 테스트 이름을 모호하게 작성하는 것이다.

Q. renderWithProviders가 너무 많은 걸 숨기면 문제야?
A. 그렇다. 테스트에 필요한 상태와 Provider가 무엇인지 알기 어려워질 수 있다.

Q. Test Structure Checklist의 핵심은 뭐야?
A. 파일 위치, 이름, Provider, mock data, reset, 사용자 결과 assertion이 일관되고 독립적인지 확인하는 것이다.

Q. Part14 Test Structure의 최종 목표는 뭐야?
A. Frontend Agent가 테스트 파일, 유틸리티, mock 데이터, setup을 일관되고 독립적으로 구성하게 만드는 것이다.
