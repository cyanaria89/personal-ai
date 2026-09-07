# Frontend Testing Part11 - TanStack Query Testing

---

# 1. TanStack Query Testing Overview

## 1.1 TanStack Query Testing Definition

### [개념]

TanStack Query Testing은 `useQuery`, `useMutation`, Query Cache, QueryClientProvider, invalidateQueries, refetch, retry, loading, error, success 상태를 검증하는 테스트다.

Frontend Testing에서 TanStack Query는 서버 상태를 관리하므로 API Mocking, Loading/Error/Empty State Testing, Component Test와 강하게 연결된다.

---

### [핵심]

- TanStack Query Testing
- React Query Testing
- QueryClient
- QueryClientProvider
- useQuery
- useMutation
- queryKey
- queryFn
- mutationFn
- isLoading
- isFetching
- isError
- isSuccess
- invalidateQueries
- refetch
- retry false
- cache isolation
- server state

---

### [실무]

2026 실무 기준에서 TanStack Query를 사용하는 Component는 테스트에서 반드시 QueryClientProvider로 감싸야 한다.

기본 흐름:

```text
Create Test QueryClient
→ Wrap with QueryClientProvider
→ Mock API response
→ Render Component
→ Assert Loading / Success / Error / Empty UI
```

좋은 TanStack Query Test:

```text
테스트마다 새 QueryClient 생성
retry false 설정
API 응답 mock
Loading / Success / Error / Empty 상태 검증
Mutation 성공 후 사용자 결과 검증
Cache 공유 방지
```

나쁜 TanStack Query Test:

```text
전역 QueryClient 재사용
retry 기본값 방치
실제 API 호출
Query Cache가 테스트 간 공유됨
invalidateQueries 호출 여부만 검증
사용자 UI 결과 미검증
```

---

### [FAQ]

Q. TanStack Query Testing은 뭐야?
A. useQuery, useMutation, Query Cache, loading/error/success 상태를 테스트하는 것이다.

Q. TanStack Query Component 테스트에서 가장 중요한 설정은 뭐야?
A. QueryClientProvider로 감싸고 테스트마다 새 QueryClient를 생성하는 것이다.

Q. retry false는 왜 필요해?
A. 실패 테스트가 재시도 때문에 느려지거나 불안정해지는 것을 막기 위해 필요하다.

---

## 1.2 TanStack Query Testing Scope

### [개념]

TanStack Query Testing Scope는 서버 상태를 사용하는 Component에서 무엇을 검증할지 정하는 기준이다.

Query Hook 자체의 내부 구현보다 사용자에게 표시되는 화면 상태와 mutation 이후 결과를 우선 검증한다.

---

### [핵심]

포함 범위:

- QueryClientProvider setup
- query loading
- query success
- query error
- query empty
- query refetch
- mutation pending
- mutation success
- mutation error
- invalidate result
- cache isolation
- retry behavior
- disabled query
- dependent query
- optimistic update caution

분리 권장:

- TanStack Query 라이브러리 내부 동작
- 실제 Backend 통합
- 실제 네트워크 상태
- 복잡한 E2E browser flow
- QueryClient 내부 cache 직접 검증 남용

---

### [실무]

Component Test 적합:

```text
FestivalListPage가 useQuery 성공 후 목록을 표시한다.
FestivalListPage가 useQuery 실패 후 ErrorState를 표시한다.
ReviewForm이 useMutation pending 중 버튼을 disabled 한다.
ReviewForm이 mutation 성공 후 성공 메시지를 표시한다.
FavoriteButton이 mutation 성공 후 버튼 문구를 변경한다.
```

Integration Test 적합:

```text
리뷰 등록 mutation 성공 후 리뷰 목록 Query가 갱신된다.
로그아웃 후 Query Cache가 초기화된다.
필터 변경 후 queryKey가 바뀌어 새 목록을 조회한다.
```

권장:

- API 응답은 mock으로 제어
- QueryClient는 테스트마다 생성
- loading/error/empty/success를 분리 테스트
- invalidateQueries 직접 호출보다 UI 갱신 결과 검증
- queryKey 변경은 API 인자 또는 UI 결과로 검증

---

### [FAQ]

Q. QueryClient 내부 cache를 직접 확인해야 해?
A. 보통은 직접 확인보다 사용자 UI 결과를 검증하는 것이 좋다.

Q. invalidateQueries 호출 여부를 테스트해야 해?
A. 직접 호출 여부보다 목록이 갱신되는 사용자 결과를 검증하는 것이 좋다.

Q. TanStack Query 테스트는 Integration Test에 가까워?
A. QueryClientProvider, API Mock, UI 상태가 함께 엮이면 Integration Test에 가까울 수 있다.

---

# 2. QueryClient Test Setup

## 2.1 Test QueryClient

### [개념]

Test QueryClient는 테스트 환경에서 TanStack Query를 사용하기 위해 생성하는 QueryClient다.

테스트마다 독립적인 QueryClient를 생성해야 cache가 공유되지 않는다.

---

### [핵심]

- QueryClient
- Test QueryClient
- QueryClientProvider
- retry false
- cache isolation
- defaultOptions
- queries retry false
- mutations retry false
- test independence
- new client per test

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

Provider wrapper:

```tsx
function renderWithQueryClient(ui: React.ReactElement) {
  const queryClient = createTestQueryClient();

  return render(
    <QueryClientProvider client={queryClient}>{ui}</QueryClientProvider>,
  );
}
```

권장:

- 테스트마다 `createTestQueryClient()` 호출
- 전역 QueryClient 재사용 금지
- retry false 설정
- 필요한 경우 logger 또는 error boundary 설정 검토
- QueryClientProvider 누락 방지

---

### [FAQ]

Q. Test QueryClient는 왜 필요해?
A. TanStack Query Hook은 QueryClientProvider 안에서 동작하므로 테스트에도 QueryClient가 필요하다.

Q. QueryClient를 전역으로 하나만 만들어도 돼?
A. 권장하지 않는다. cache가 테스트 간 공유되어 불안정해질 수 있다.

Q. mutation에도 retry false가 필요해?
A. 실패 mutation 테스트가 예측 가능하도록 mutations retry도 false로 설정하는 것이 좋다.

---

## 2.2 QueryClientProvider Missing Error

### [개념]

QueryClientProvider Missing Error는 QueryClientProvider 없이 `useQuery`, `useMutation`을 사용하는 Component를 렌더링할 때 발생하는 오류다.

TanStack Query Component는 반드시 QueryClientProvider로 감싸야 한다.

---

### [핵심]

오류 원인:

- QueryClientProvider 누락
- renderWithProviders 미사용
- Provider 순서 문제
- 테스트 utility 누락
- Component 내부 useQuery 사용
- custom hook 내부 useQuery 사용

---

### [실무]

문제 예:

```tsx
render(<FestivalListPage />);
```

`FestivalListPage` 내부에서 useQuery를 사용하면 Provider 오류가 발생할 수 있다.

개선:

```tsx
renderWithQueryClient(<FestivalListPage />);
```

또는:

```tsx
render(
  <QueryClientProvider client={createTestQueryClient()}>
    <FestivalListPage />
  </QueryClientProvider>,
);
```

Debug Flow:

```text
No QueryClient set 오류
→ Component가 useQuery/useMutation 사용 확인
→ QueryClientProvider wrapper 확인
→ renderWithProviders 사용 여부 확인
→ Provider 순서 확인
```

---

### [FAQ]

Q. No QueryClient set 오류는 왜 나?
A. QueryClientProvider 없이 useQuery 또는 useMutation을 사용하는 Component를 렌더링했기 때문이다.

Q. 해결 방법은 뭐야?
A. 테스트에서 QueryClientProvider로 Component를 감싸야 한다.

Q. custom hook 내부에서 useQuery를 써도 Provider가 필요해?
A. 필요하다. hook을 사용하는 Component 또는 hook test 모두 QueryClientProvider가 필요하다.

---

## 2.3 renderWithProviders for Query

### [개념]

renderWithProviders는 QueryClientProvider, Router, AuthProvider, ThemeProvider 같은 Provider를 공통으로 감싸는 테스트 유틸리티다.

TanStack Query 테스트에서는 QueryClientProvider를 포함한 render utility를 사용하는 것이 좋다.

---

### [핵심]

- renderWithProviders
- QueryClientProvider
- MemoryRouter
- AuthProvider
- ThemeProvider
- test utility
- provider composition
- initialEntries
- authenticated option
- queryClient option

---

### [실무]

예:

```tsx
type RenderWithProvidersOptions = {
  initialEntries?: string[];
  authenticated?: boolean;
};

function renderWithProviders(
  ui: React.ReactElement,
  options: RenderWithProvidersOptions = {},
) {
  const queryClient = createTestQueryClient();

  return render(
    <MemoryRouter initialEntries={options.initialEntries ?? ["/"]}>
      <QueryClientProvider client={queryClient}>
        <MockAuthProvider authenticated={options.authenticated ?? false}>
          {ui}
        </MockAuthProvider>
      </QueryClientProvider>
    </MemoryRouter>,
  );
}
```

사용:

```tsx
test("마이페이지 정보를 표시한다", async () => {
  vi.mocked(getMyProfile).mockResolvedValue({
    nickname: "tester",
  });

  renderWithProviders(<MyPage />, {
    authenticated: true,
  });

  expect(await screen.findByText("tester")).toBeInTheDocument();
});
```

권장:

- QueryClient는 utility 내부에서 새로 생성
- 테스트마다 독립 Provider 구성
- Router / Auth가 필요 없는 테스트는 더 작은 wrapper 사용 가능
- utility가 너무 커지면 목적별로 분리

---

### [FAQ]

Q. renderWithProviders에 QueryClientProvider를 넣어도 돼?
A. 좋다. Query를 사용하는 Page 테스트에서 반복 설정을 줄일 수 있다.

Q. 모든 테스트에 큰 renderWithProviders를 써야 해?
A. 아니다. 필요한 Provider만 포함하는 최소 wrapper가 더 좋을 수 있다.

Q. QueryClient를 options로 외부에서 받을 수도 있어?
A. 가능하다. cache 상태를 직접 준비해야 하는 특수 테스트에서 유용하다.

---

# 3. useQuery Test

## 3.1 useQuery Loading Test

### [개념]

useQuery Loading Test는 queryFn이 완료되기 전 Loading UI가 표시되는지 검증하는 테스트다.

pending promise mock을 사용하면 loading 상태를 안정적으로 재현할 수 있다.

---

### [핵심]

- useQuery loading
- isLoading
- isPending
- pending promise
- loading state
- role status
- skeleton
- spinner
- no premature empty
- no premature error

---

### [실무]

예:

```tsx
test("축제 목록 조회 중에는 loading 메시지를 표시한다", () => {
  vi.mocked(getFestivals).mockReturnValue(new Promise(() => {}));

  renderWithQueryClient(<FestivalListPage />);

  expect(screen.getByRole("status")).toHaveTextContent("불러오는 중입니다.");
});
```

상태 충돌 검증:

```tsx
expect(screen.queryByText("표시할 축제가 없습니다.")).not.toBeInTheDocument();
expect(screen.queryByText("서버 오류가 발생했습니다.")).not.toBeInTheDocument();
```

권장:

- loading test는 pending promise 사용
- mockResolvedValue로 loading 검증하지 않음
- loading UI는 status role 또는 accessible label 제공
- initial loading과 background fetching 구분
- retry false 설정

---

### [FAQ]

Q. useQuery Loading은 어떻게 테스트해?
A. queryFn mock을 pending promise로 두고 loading message, spinner, skeleton을 검증한다.

Q. mockResolvedValue로 loading 테스트가 가능해?
A. 응답이 즉시 완료되어 loading이 지나갈 수 있으므로 pending promise가 더 안정적이다.

Q. loading 중 EmptyState가 보이면 안 돼?
A. 일반적으로 initial loading 중에는 EmptyState를 표시하지 않는 것이 좋다.

---

## 3.2 useQuery Success Test

### [개념]

useQuery Success Test는 queryFn이 성공 응답을 반환했을 때 화면에 데이터가 표시되는지 검증하는 테스트다.

---

### [핵심]

- useQuery success
- mockResolvedValue
- data rendering
- list rendering
- detail rendering
- success state
- findBy
- query data
- UI result

---

### [실무]

목록 성공:

```tsx
test("축제 목록 조회 성공 시 축제 제목을 표시한다", async () => {
  vi.mocked(getFestivals).mockResolvedValue([
    { festivalId: 1, title: "봄꽃 축제" },
    { festivalId: 2, title: "음악 축제" },
  ]);

  renderWithQueryClient(<FestivalListPage />);

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
  expect(screen.getByText("음악 축제")).toBeInTheDocument();
});
```

상세 성공:

```tsx
test("축제 상세 조회 성공 시 상세 제목을 표시한다", async () => {
  vi.mocked(getFestivalDetail).mockResolvedValue({
    festivalId: 1,
    title: "봄꽃 축제",
    description: "봄꽃이 피는 축제입니다.",
  });

  renderWithQueryClient(<FestivalDetailPage festivalId={1} />);

  expect(
    await screen.findByRole("heading", { name: "봄꽃 축제" }),
  ).toBeInTheDocument();
  expect(screen.getByText("봄꽃이 피는 축제입니다.")).toBeInTheDocument();
});
```

권장:

- 성공 응답은 실제 API shape와 일치
- 비동기 데이터는 findBy로 검증
- API 호출 여부보다 데이터 UI 검증
- list count / detail field 검증 가능
- nullable field도 필요 시 테스트

---

### [FAQ]

Q. useQuery Success는 어떻게 테스트해?
A. queryFn mockResolvedValue를 설정하고 화면에 데이터가 표시되는지 findBy로 검증한다.

Q. API 함수 호출 여부도 확인해야 해?
A. 필요하면 확인할 수 있지만 사용자에게 보이는 데이터 UI 검증이 우선이다.

Q. success response shape는 실제 API와 같아야 해?
A. 가능하면 실제 API 함수 반환 shape와 맞춰야 한다.

---

## 3.3 useQuery Error Test

### [개념]

useQuery Error Test는 queryFn이 실패했을 때 ErrorState, 오류 메시지, retry action이 표시되는지 검증하는 테스트다.

---

### [핵심]

- useQuery error
- mockRejectedValue
- isError
- ErrorState
- error message
- role alert
- retry button
- HTTP status
- network error
- safe fallback

---

### [실무]

예:

```tsx
test("축제 목록 조회 실패 시 오류 메시지를 표시한다", async () => {
  vi.mocked(getFestivals).mockRejectedValue({
    response: {
      status: 500,
    },
  });

  renderWithQueryClient(<FestivalListPage />);

  expect(
    await screen.findByText("서버 오류가 발생했습니다."),
  ).toBeInTheDocument();
});
```

Network Error:

```tsx
test("네트워크 오류 시 연결 확인 메시지를 표시한다", async () => {
  vi.mocked(getFestivals).mockRejectedValue({
    request: {},
    message: "Network Error",
  });

  renderWithQueryClient(<FestivalListPage />);

  expect(
    await screen.findByText("네트워크 연결을 확인해 주세요."),
  ).toBeInTheDocument();
});
```

권장:

- retry false 설정
- 실제 error handling shape와 mock 일치
- 오류 UI는 findBy 사용
- 서버 내부 error detail 노출 금지
- Retry 버튼이 있으면 별도 테스트

---

### [FAQ]

Q. useQuery Error는 어떻게 테스트해?
A. queryFn mockRejectedValue를 설정하고 ErrorState 또는 오류 메시지가 표시되는지 findBy로 확인한다.

Q. retry false를 설정하지 않으면 어떻게 돼?
A. 실패 테스트가 재시도 때문에 느려지거나 예측하기 어려워질 수 있다.

Q. ErrorState와 EmptyState는 어떻게 구분해?
A. ErrorState는 query 실패이고 EmptyState는 query 성공 후 데이터가 없는 상태다.

---

## 3.4 useQuery Empty Test

### [개념]

useQuery Empty Test는 queryFn이 성공했지만 빈 데이터를 반환했을 때 EmptyState가 표시되는지 검증하는 테스트다.

---

### [핵심]

- useQuery empty
- empty array
- empty content
- null data caution
- EmptyState
- no result
- no data
- success with empty data
- page response
- slice response

---

### [실무]

배열 응답:

```tsx
test("축제 목록이 비어 있으면 EmptyState를 표시한다", async () => {
  vi.mocked(getFestivals).mockResolvedValue([]);

  renderWithQueryClient(<FestivalListPage />);

  expect(
    await screen.findByText("표시할 축제가 없습니다."),
  ).toBeInTheDocument();
});
```

Page 응답:

```tsx
test("page content가 비어 있으면 EmptyState를 표시한다", async () => {
  vi.mocked(getFestivals).mockResolvedValue({
    content: [],
    page: 0,
    size: 10,
    totalElements: 0,
    totalPages: 0,
  });

  renderWithQueryClient(<FestivalListPage />);

  expect(
    await screen.findByText("표시할 축제가 없습니다."),
  ).toBeInTheDocument();
});
```

권장:

- 실제 response shape에 맞는 empty mock 사용
- EmptyState와 ErrorState 구분
- loading 중 empty가 표시되지 않는지 확인 가능
- 검색 결과 없음과 최초 empty 문구 구분
- empty action이 있으면 검증

---

### [FAQ]

Q. useQuery Empty는 어떻게 테스트해?
A. queryFn mockResolvedValue로 빈 배열이나 빈 content를 반환하고 EmptyState를 검증한다.

Q. 빈 배열과 error는 달라?
A. 다르다. 빈 배열은 성공 응답이고 error는 실패 응답이다.

Q. EmptyState가 안 보이면 뭘 확인해?
A. Component가 기대하는 response shape와 mock shape가 일치하는지 확인한다.

---

## 3.5 Disabled Query Test

### [개념]

Disabled Query Test는 `enabled: false` 조건으로 query가 실행되지 않아야 하는 상황을 검증하는 테스트다.

검색 조건이 없거나 필수 parameter가 없거나 인증 상태가 없을 때 사용한다.

---

### [핵심]

- enabled false
- disabled query
- conditional query
- required param
- auth required query
- no API call
- idle state
- search condition
- dependent query

---

### [실무]

검색어 없을 때 query 비활성:

```tsx
test("검색어가 없으면 검색 API를 호출하지 않는다", () => {
  renderWithQueryClient(<FestivalSearchResult keyword="" />);

  expect(searchFestivals).not.toHaveBeenCalled();
});
```

parameter 없을 때:

```tsx
test("festivalId가 없으면 상세 API를 호출하지 않는다", () => {
  renderWithQueryClient(<FestivalDetailPanel festivalId={undefined} />);

  expect(getFestivalDetail).not.toHaveBeenCalled();
});
```

인증 필요 query:

```tsx
test("비로그인 상태이면 내 정보 API를 호출하지 않는다", () => {
  renderWithProviders(<MyProfilePanel />, {
    authenticated: false,
  });

  expect(getMyProfile).not.toHaveBeenCalled();
});
```

권장:

- enabled 조건별 API 호출 여부 검증
- 사용자 안내 UI가 있으면 함께 검증
- enabled true case도 별도 테스트
- queryKey에 undefined가 들어가는지 주의
- 조건이 복잡하면 hook 로직 분리 검토

---

### [FAQ]

Q. enabled false Query는 왜 테스트해?
A. 필수 조건이 없을 때 불필요한 API 호출을 막는지 확인하기 위해 필요하다.

Q. disabled query는 어떤 UI를 보여줘야 해?
A. 상황에 따라 입력 안내, 로그인 필요 메시지, 빈 상태 등을 표시할 수 있다.

Q. API 호출 여부를 확인해도 돼?
A. enabled false 조건에서는 호출되지 않는 것이 핵심이므로 확인해도 좋다.

---

# 4. Query Key Test

## 4.1 Query Key Parameter Test

### [개념]

Query Key Parameter Test는 검색어, 필터, 페이지 번호, id 같은 값이 queryKey와 API 요청에 반영되어 올바른 데이터를 조회하는지 검증하는 테스트다.

---

### [핵심]

- queryKey
- query key parameter
- filter key
- keyword key
- page key
- detail id key
- query invalidation target
- cache separation
- API argument

---

### [실무]

검색 조건 반영:

```tsx
test("검색 조건이 API 요청 인자에 반영된다", async () => {
  const user = userEvent.setup();

  vi.mocked(searchFestivals).mockResolvedValue([]);

  renderWithQueryClient(<FestivalSearchPage />);

  await user.type(screen.getByLabelText("검색어"), "봄꽃");
  await user.selectOptions(
    screen.getByRole("combobox", { name: "지역" }),
    "seoul",
  );
  await user.click(screen.getByRole("button", { name: "검색" }));

  await screen.findByText("검색 결과가 없습니다.");

  expect(searchFestivals).toHaveBeenCalledWith({
    keyword: "봄꽃",
    region: "seoul",
  });
});
```

상세 id 반영:

```tsx
test("festivalId로 상세 정보를 조회한다", async () => {
  vi.mocked(getFestivalDetail).mockResolvedValue({
    festivalId: 1,
    title: "봄꽃 축제",
  });

  renderWithQueryClient(<FestivalDetailPage festivalId={1} />);

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
  expect(getFestivalDetail).toHaveBeenCalledWith(1);
});
```

권장:

- queryKey 내부 직접 검사보다 API 인자 또는 UI 결과 검증
- filter/page/sort 변경 시 새 요청 검증
- undefined parameter 처리 테스트
- queryKey factory를 사용하면 key 일관성 유지 가능

---

### [FAQ]

Q. queryKey 자체를 직접 테스트해야 해?
A. 보통은 API 인자와 UI 결과를 검증하는 것이 더 실용적이다.

Q. 검색 조건이 queryKey에 들어가야 하는 이유는?
A. 조건별 cache를 분리하고 조건 변경 시 새 데이터를 조회하기 위해 필요하다.

Q. queryKey에 object를 넣어도 돼?
A. 가능하지만 안정적인 key 구조와 일관된 query key factory 사용이 좋다.

---

## 4.2 Query Key Change Refetch Test

### [개념]

Query Key Change Refetch Test는 queryKey에 포함된 값이 변경되었을 때 새로운 query가 실행되고 화면 결과가 갱신되는지 검증하는 테스트다.

검색, 필터, 페이지네이션, 정렬에서 중요하다.

---

### [핵심]

- queryKey change
- refetch by key change
- filter change
- page change
- sort change
- search keyword change
- new data rendering
- cache separation
- previous data caution

---

### [실무]

필터 변경:

```tsx
test("지역 필터를 변경하면 새로운 검색 결과를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(searchFestivals)
    .mockResolvedValueOnce([{ festivalId: 1, title: "서울 축제" }])
    .mockResolvedValueOnce([{ festivalId: 2, title: "부산 축제" }]);

  renderWithQueryClient(<FestivalSearchPage />);

  expect(await screen.findByText("서울 축제")).toBeInTheDocument();

  await user.selectOptions(
    screen.getByRole("combobox", { name: "지역" }),
    "busan",
  );
  await user.click(screen.getByRole("button", { name: "검색" }));

  expect(await screen.findByText("부산 축제")).toBeInTheDocument();
});
```

페이지 변경:

```tsx
test("다음 페이지 클릭 시 다음 페이지 데이터를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(getFestivals)
    .mockResolvedValueOnce({ content: [{ title: "1페이지 축제" }], page: 0 })
    .mockResolvedValueOnce({ content: [{ title: "2페이지 축제" }], page: 1 });

  renderWithQueryClient(<FestivalListPage />);

  expect(await screen.findByText("1페이지 축제")).toBeInTheDocument();

  await user.click(screen.getByRole("button", { name: "다음" }));

  expect(await screen.findByText("2페이지 축제")).toBeInTheDocument();
});
```

권장:

- key 변경 후 새 UI 결과 검증
- old data가 남아야 하는지 사라져야 하는지 정책 명확화
- keepPreviousData 사용 시 기존 데이터 유지 테스트 가능
- API 호출 인자 검증 가능
- findBy로 새 결과 대기

---

### [FAQ]

Q. queryKey 변경은 왜 테스트해?
A. 필터나 페이지가 바뀌었는데 이전 cache를 그대로 보여주는 버그를 막기 위해 필요하다.

Q. key 변경 후 기존 데이터가 잠깐 남아도 돼?
A. keep previous data 정책에 따라 가능하다. 프로젝트 UX 정책에 맞게 테스트한다.

Q. queryKey 변경 테스트에서 무엇을 검증해?
A. 새 조건에 맞는 API 요청과 새 UI 결과를 검증한다.

---

# 5. useMutation Test

## 5.1 useMutation Pending Test

### [개념]

useMutation Pending Test는 mutation이 진행 중일 때 버튼 disabled, 처리 중 문구, 중복 요청 방지가 동작하는지 검증하는 테스트다.

---

### [핵심]

- useMutation pending
- isPending
- isLoading
- submit loading
- button disabled
- processing text
- duplicate submit prevention
- mutationFn pending
- userEvent

---

### [실무]

예:

```tsx
test("리뷰 등록 중에는 등록 버튼이 비활성화된다", async () => {
  const user = userEvent.setup();

  vi.mocked(createReview).mockReturnValue(new Promise(() => {}));

  renderWithQueryClient(<ReviewForm />);

  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(screen.getByRole("button", { name: "처리 중..." })).toBeDisabled();
});
```

중복 요청 방지:

```tsx
test("mutation pending 중에는 중복 등록하지 않는다", async () => {
  const user = userEvent.setup();

  vi.mocked(createReview).mockReturnValue(new Promise(() => {}));

  renderWithQueryClient(<ReviewForm />);

  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");

  await user.click(screen.getByRole("button", { name: "등록" }));
  await user.click(screen.getByRole("button", { name: "처리 중..." }));

  expect(createReview).toHaveBeenCalledTimes(1);
});
```

권장:

- pending promise 사용
- button disabled 검증
- 처리 중 문구 검증
- 중복 submit 방지 검증
- pending promise로 테스트가 hang되지 않도록 UI 확인 후 종료

---

### [FAQ]

Q. useMutation Pending은 어떻게 테스트해?
A. mutationFn을 pending promise로 만들고 버튼 disabled와 처리 중 UI를 검증한다.

Q. mutation pending 중 중복 클릭은 테스트해야 해?
A. 중복 요청 방지가 중요한 Form이나 결제, 저장, 삭제에서는 테스트하는 것이 좋다.

Q. pending promise 테스트는 안전해?
A. UI 상태 확인 후 테스트가 종료되도록 작성하면 가능하다.

---

## 5.2 useMutation Success Test

### [개념]

useMutation Success Test는 mutationFn이 성공했을 때 성공 메시지, Form reset, Modal close, 목록 갱신, 버튼 상태 변경 같은 사용자 결과가 나타나는지 검증하는 테스트다.

---

### [핵심]

- useMutation success
- mockResolvedValue
- success message
- form reset
- modal close
- list update
- button state change
- favorite toggle
- delete success
- invalidate result
- user-visible result

---

### [실무]

Form 성공:

```tsx
test("리뷰 등록 성공 시 성공 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(createReview).mockResolvedValue({
    reviewId: 1,
    content: "좋았어요",
  });

  renderWithQueryClient(<ReviewForm />);

  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(await screen.findByText("리뷰가 등록되었습니다.")).toBeInTheDocument();
});
```

버튼 상태 변경:

```tsx
test("찜하기 성공 시 버튼 문구가 찜 해제로 변경된다", async () => {
  const user = userEvent.setup();

  vi.mocked(addFavorite).mockResolvedValue({
    favorite: true,
  });

  renderWithQueryClient(
    <FavoriteButton festivalId={1} initialFavorite={false} />,
  );

  await user.click(screen.getByRole("button", { name: "찜하기" }));

  expect(
    await screen.findByRole("button", { name: "찜 해제" }),
  ).toBeInTheDocument();
});
```

권장:

- mutation 성공 후 사용자 UI 검증
- mutationFn 호출만으로 끝내지 않음
- 성공 메시지 / reset / redirect / close / list update 중 정책에 맞게 검증
- 비동기 결과는 findBy 사용
- 실제 API 호출 금지

---

### [FAQ]

Q. useMutation Success는 어떻게 테스트해?
A. mutationFn mockResolvedValue를 설정하고 성공 후 표시되는 UI 결과를 검증한다.

Q. mutation 함수 호출 여부만 확인하면 돼?
A. 부족할 수 있다. 성공 메시지나 목록 갱신 같은 사용자 결과를 검증해야 한다.

Q. 성공 후 form reset도 테스트해야 해?
A. Form 정책에 포함되어 있다면 테스트하는 것이 좋다.

---

## 5.3 useMutation Error Test

### [개념]

useMutation Error Test는 mutationFn이 실패했을 때 field error, global error, 버튼 상태 복구, retry 가능 상태가 올바른지 검증하는 테스트다.

---

### [핵심]

- useMutation error
- mockRejectedValue
- server validation error
- field error
- global error
- button enabled
- retry possible
- error message
- role alert
- safe fallback

---

### [실무]

Global Error:

```tsx
test("리뷰 등록 실패 시 오류 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(createReview).mockRejectedValue({
    response: {
      status: 500,
    },
  });

  renderWithQueryClient(<ReviewForm />);

  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(await screen.findByRole("alert")).toHaveTextContent(
    "서버 오류가 발생했습니다.",
  );
});
```

Server Field Error:

```tsx
test("서버 field error를 리뷰 내용 오류로 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(createReview).mockRejectedValue({
    response: {
      status: 400,
      data: {
        fieldErrors: {
          content: "부적절한 표현이 포함되어 있습니다.",
        },
      },
    },
  });

  renderWithQueryClient(<ReviewForm />);

  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.type(screen.getByLabelText("리뷰 내용"), "bad word");
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(
    await screen.findByText("부적절한 표현이 포함되어 있습니다."),
  ).toBeInTheDocument();
});
```

버튼 상태 복구:

```tsx
expect(screen.getByRole("button", { name: "등록" })).toBeEnabled();
```

권장:

- 실제 error shape와 mock 일치
- field error와 global error 구분
- 실패 후 버튼이 재활성화되는지 확인
- 서버 내부 메시지 노출 금지
- retry 또는 재제출 가능 상태 검증

---

### [FAQ]

Q. useMutation Error는 어떻게 테스트해?
A. mutationFn mockRejectedValue를 설정하고 오류 메시지나 field error가 표시되는지 검증한다.

Q. mutation 실패 후 버튼은 다시 활성화되어야 해?
A. 일반적으로 재시도를 위해 다시 활성화되는 것이 좋다.

Q. 서버 validation error는 어떻게 테스트해?
A. 실제 error response shape에 맞게 fieldErrors를 mock하고 field error UI를 검증한다.

---

## 5.4 Mutation Variables Test

### [개념]

Mutation Variables Test는 사용자가 입력한 값이나 선택한 값이 mutationFn에 올바른 변수로 전달되는지 검증하는 테스트다.

Form submit, toggle button, delete action에서 사용한다.

---

### [핵심]

- mutation variables
- mutationFn arguments
- form values
- request DTO
- path id
- selected value
- transformed value
- trimmed value
- type conversion
- user action

---

### [실무]

Form variables:

```tsx
test("리뷰 등록 요청에 평점과 내용을 전달한다", async () => {
  const user = userEvent.setup();

  vi.mocked(createReview).mockResolvedValue({
    reviewId: 1,
  });

  renderWithQueryClient(<ReviewForm festivalId={1} />);

  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.type(screen.getByLabelText("리뷰 내용"), " 좋았어요 ");
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(createReview).toHaveBeenCalledWith({
    festivalId: 1,
    rating: 5,
    content: "좋았어요",
  });
});
```

Delete variables:

```tsx
test("삭제 버튼 클릭 시 reviewId로 삭제 요청을 보낸다", async () => {
  const user = userEvent.setup();

  vi.mocked(deleteReview).mockResolvedValue(undefined);

  renderWithQueryClient(
    <ReviewItem review={{ reviewId: 10, content: "좋았어요" }} />,
  );

  await user.click(screen.getByRole("button", { name: "삭제" }));

  expect(deleteReview).toHaveBeenCalledWith(10);
});
```

권장:

- 사용자 행동으로 mutation 실행
- request DTO shape 검증
- trim / type conversion 검증
- path id / body 값 구분
- variables 검증 후 사용자 성공 결과도 함께 검증 가능

---

### [FAQ]

Q. Mutation Variables Test는 언제 필요해?
A. Form 값이나 id가 API 요청에 올바르게 전달되는지 확인해야 할 때 필요하다.

Q. variables만 확인하면 충분해?
A. 단순 Component는 가능하지만 핵심 흐름에서는 성공 UI도 함께 검증하는 것이 좋다.

Q. Form 값 변환도 테스트해야 해?
A. trim, number conversion, DTO mapping이 있다면 테스트하는 것이 좋다.

---

# 6. Invalidation and Refetch Test

## 6.1 invalidateQueries Result Test

### [개념]

invalidateQueries Result Test는 mutation 성공 후 관련 query가 갱신되어 사용자 화면이 최신 데이터로 바뀌는지 검증하는 테스트다.

invalidateQueries 호출 자체보다 결과 UI를 우선 검증한다.

---

### [핵심]

- invalidateQueries
- query invalidation
- refetch after mutation
- list update
- cache refresh
- stale query
- mutation success
- updated UI
- user-visible result

---

### [실무]

리뷰 등록 후 목록 갱신 예:

```tsx
test("리뷰 등록 성공 후 리뷰 목록을 갱신한다", async () => {
  const user = userEvent.setup();

  vi.mocked(getReviews)
    .mockResolvedValueOnce([])
    .mockResolvedValueOnce([{ reviewId: 1, content: "좋았어요" }]);

  vi.mocked(createReview).mockResolvedValue({
    reviewId: 1,
    content: "좋았어요",
  });

  renderWithQueryClient(<ReviewSection festivalId={1} />);

  expect(await screen.findByText("아직 리뷰가 없습니다.")).toBeInTheDocument();

  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(await screen.findByText("좋았어요")).toBeInTheDocument();
});
```

권장:

- invalidateQueries spy보다 UI 갱신 결과 우선
- mutation 전 / 후 mock 응답을 다르게 설정
- refetch 후 새 데이터 표시 검증
- QueryClient cache가 테스트 간 공유되지 않게 설정
- 로딩 / 성공 메시지와 충돌 확인

---

### [FAQ]

Q. invalidateQueries를 직접 spy해야 해?
A. 보통은 직접 호출 여부보다 사용자 화면이 갱신되는지 검증하는 것이 좋다.

Q. mutation 후 목록 갱신은 어떻게 테스트해?
A. 목록 API mock을 첫 번째와 두 번째 응답으로 나누고 mutation 후 새 데이터가 표시되는지 확인한다.

Q. invalidate result 테스트가 실패하면?
A. queryKey가 맞는지, QueryClient가 같은 Provider 안에 있는지, mock 응답 순서를 확인한다.

---

## 6.2 Refetch Button Test

### [개념]

Refetch Button Test는 사용자가 새로고침 또는 다시 시도 버튼을 눌렀을 때 query가 다시 실행되고 화면 결과가 갱신되는지 검증하는 테스트다.

---

### [핵심]

- refetch
- refetch button
- refresh button
- retry button
- manual query
- user click
- new data
- error recovery
- stale data update

---

### [실무]

새로고침 성공:

```tsx
test("새로고침 버튼을 클릭하면 최신 데이터를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(getFestivals)
    .mockResolvedValueOnce([{ festivalId: 1, title: "이전 축제" }])
    .mockResolvedValueOnce([{ festivalId: 2, title: "최신 축제" }]);

  renderWithQueryClient(<FestivalListPage />);

  expect(await screen.findByText("이전 축제")).toBeInTheDocument();

  await user.click(screen.getByRole("button", { name: "새로고침" }));

  expect(await screen.findByText("최신 축제")).toBeInTheDocument();
});
```

오류 후 다시 시도:

```tsx
test("오류 후 다시 시도하면 데이터를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(getFestivals)
    .mockRejectedValueOnce({ response: { status: 500 } })
    .mockResolvedValueOnce([{ festivalId: 1, title: "봄꽃 축제" }]);

  renderWithQueryClient(<FestivalListPage />);

  expect(
    await screen.findByText("서버 오류가 발생했습니다."),
  ).toBeInTheDocument();

  await user.click(screen.getByRole("button", { name: "다시 시도" }));

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

권장:

- userEvent로 refetch trigger 실행
- refetch 후 새 UI 결과 검증
- API 호출 횟수보다 사용자 결과 우선
- refetch 중 기존 데이터 유지 여부 정책 검증 가능
- error recovery 테스트 포함

---

### [FAQ]

Q. Refetch Button은 어떻게 테스트해?
A. 첫 응답과 두 번째 응답을 다르게 mock하고 버튼 클릭 후 새 데이터가 표시되는지 확인한다.

Q. API 호출 횟수도 확인해야 해?
A. 보조적으로 가능하지만 최종 UI 결과가 더 중요하다.

Q. 오류 후 다시 시도도 refetch 테스트야?
A. 그렇다. retry/refetch로 오류 상태에서 성공 상태로 회복되는지 검증한다.

---

# 7. Cache and Isolation Test

## 7.1 Query Cache Isolation

### [개념]

Query Cache Isolation은 테스트 간 Query Cache가 공유되지 않도록 하는 규칙이다.

각 테스트는 독립적인 QueryClient를 사용해야 한다.

---

### [핵심]

- query cache
- cache isolation
- new QueryClient per test
- test independence
- stale data
- shared cache problem
- previous test data leak
- queryClient.clear
- render utility

---

### [실무]

문제 상황:

```text
Test A
→ getFestivals success
→ cache에 "봄꽃 축제" 저장

Test B
→ getFestivals error 기대
→ cache 때문에 success data가 먼저 표시됨
```

권장:

```tsx
function renderWithQueryClient(ui: React.ReactElement) {
  const queryClient = createTestQueryClient();

  return render(
    <QueryClientProvider client={queryClient}>{ui}</QueryClientProvider>,
  );
}
```

필요 시 명시 정리:

```ts
afterEach(() => {
  queryClient.clear();
});
```

하지만 테스트마다 새 client를 생성하는 방식이 더 안전하다.

권장:

- QueryClient 전역 재사용 금지
- 테스트마다 createTestQueryClient 호출
- cacheTime/gcTime 의존 테스트 지양
- 이전 테스트 데이터에 의존하지 않음
- mock reset과 cache isolation을 함께 관리

---

### [FAQ]

Q. Query Cache Isolation은 왜 필요해?
A. 이전 테스트의 cache 데이터가 다음 테스트 결과에 영향을 주는 것을 막기 위해 필요하다.

Q. queryClient.clear만 하면 충분해?
A. 가능하지만 테스트마다 새 QueryClient를 생성하는 방식이 더 안전하고 단순하다.

Q. cache 공유 문제는 어떻게 알아채?
A. mock 응답과 다른 이전 데이터가 화면에 나타나거나 테스트 순서에 따라 결과가 달라질 수 있다.

---

## 7.2 Seed Query Cache Test

### [개념]

Seed Query Cache Test는 테스트 시작 전에 Query Cache에 데이터를 미리 넣어 특정 화면 상태를 검증하는 방식이다.

상세 화면의 초기 데이터, optimistic UI, prefetch 상태 테스트에 사용할 수 있다.

---

### [핵심]

- seed query cache
- setQueryData
- initial cache
- preloaded data
- optimistic state
- detail initial data
- queryKey match
- cache state
- test queryClient option

---

### [실무]

예:

```tsx
test("cache에 있는 사용자 정보를 먼저 표시한다", () => {
  const queryClient = createTestQueryClient();

  queryClient.setQueryData(["myProfile"], {
    nickname: "cached-user",
  });

  render(
    <QueryClientProvider client={queryClient}>
      <MyProfilePanel />
    </QueryClientProvider>,
  );

  expect(screen.getByText("cached-user")).toBeInTheDocument();
});
```

주의:

```text
setQueryData queryKey
→ 실제 Component의 queryKey와 정확히 일치해야 함
```

권장:

- cache seed가 필요한 테스트에만 사용
- queryKey factory 사용 권장
- seed data도 실제 response shape와 일치
- cache 내부를 직접 테스트하기보다 cache 기반 UI 결과 검증
- 테스트마다 새 QueryClient 사용

---

### [FAQ]

Q. Seed Query Cache는 언제 써?
A. preloaded data, optimistic state, cache 기반 초기 표시를 테스트하고 싶을 때 사용한다.

Q. setQueryData의 queryKey는 왜 중요해?
A. Component가 사용하는 queryKey와 일치해야 cache 데이터를 읽을 수 있다.

Q. 모든 Query 테스트에 setQueryData를 써야 해?
A. 아니다. 대부분은 API mock으로 충분하고 cache seed는 특수 상황에 사용한다.

---

# 8. Dependent Query Test

## 8.1 Dependent Query Definition

### [개념]

Dependent Query는 특정 값이나 선행 query 결과가 있어야 실행되는 query다.

예를 들어 로그인 사용자 정보가 있어야 마이페이지 데이터를 조회하거나, festivalId가 있어야 상세 데이터를 조회하는 경우다.

---

### [핵심]

- dependent query
- enabled option
- previous query data
- required id
- authenticated user
- selected value
- conditional fetch
- no premature API call
- chained query

---

### [실무]

예:

```text
useQuery(["festival", festivalId], queryFn, {
  enabled: Boolean(festivalId),
})
```

테스트:

```tsx
test("festivalId가 없으면 상세 query를 실행하지 않는다", () => {
  renderWithQueryClient(<FestivalDetailPanel festivalId={undefined} />);

  expect(getFestivalDetail).not.toHaveBeenCalled();
});
```

festivalId가 있으면 실행:

```tsx
test("festivalId가 있으면 상세 정보를 조회한다", async () => {
  vi.mocked(getFestivalDetail).mockResolvedValue({
    festivalId: 1,
    title: "봄꽃 축제",
  });

  renderWithQueryClient(<FestivalDetailPanel festivalId={1} />);

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
  expect(getFestivalDetail).toHaveBeenCalledWith(1);
});
```

권장:

- enabled false case 테스트
- enabled true case 테스트
- 필수 값 없을 때 안내 UI 검증 가능
- queryKey에 undefined 포함 주의
- 선행 query 실패 case도 필요 시 테스트

---

### [FAQ]

Q. Dependent Query는 뭐야?
A. 특정 값이나 선행 데이터가 있을 때만 실행되는 query다.

Q. dependent query에서 무엇을 테스트해야 해?
A. 조건이 없을 때 API가 호출되지 않고, 조건이 있을 때 정상 조회되는지 테스트한다.

Q. enabled 옵션은 왜 중요해?
A. 필수 값이 없을 때 불필요하거나 잘못된 API 호출을 막기 위해 중요하다.

---

# 9. Infinite Query and Load More Test

## 9.1 Infinite Query Test

### [개념]

Infinite Query Test는 `useInfiniteQuery`를 사용하는 무한 스크롤 또는 더보기 목록이 pageParam과 hasNextPage에 따라 올바르게 동작하는지 검증하는 테스트다.

---

### [핵심]

- useInfiniteQuery
- infinite query
- pageParam
- getNextPageParam
- hasNextPage
- fetchNextPage
- load more
- infinite scroll
- Slice response
- pages
- next cursor
- cursor pagination

---

### [실무]

더보기 예:

```tsx
test("더보기 버튼을 클릭하면 다음 페이지 항목을 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(getNotifications)
    .mockResolvedValueOnce({
      content: [{ notificationId: 1, message: "첫 번째 알림" }],
      nextCursor: 2,
      hasNext: true,
    })
    .mockResolvedValueOnce({
      content: [{ notificationId: 2, message: "두 번째 알림" }],
      nextCursor: null,
      hasNext: false,
    });

  renderWithQueryClient(<NotificationList />);

  expect(await screen.findByText("첫 번째 알림")).toBeInTheDocument();

  await user.click(screen.getByRole("button", { name: "더보기" }));

  expect(await screen.findByText("두 번째 알림")).toBeInTheDocument();
});
```

hasNext false:

```tsx
test("다음 페이지가 없으면 더보기 버튼을 표시하지 않는다", async () => {
  vi.mocked(getNotifications).mockResolvedValue({
    content: [{ notificationId: 1, message: "알림" }],
    nextCursor: null,
    hasNext: false,
  });

  renderWithQueryClient(<NotificationList />);

  expect(await screen.findByText("알림")).toBeInTheDocument();
  expect(
    screen.queryByRole("button", { name: "더보기" }),
  ).not.toBeInTheDocument();
});
```

권장:

- 첫 페이지와 다음 페이지 응답 분리
- hasNextPage true / false 모두 테스트
- 더보기 클릭 후 누적 목록 검증
- cursor 또는 pageParam이 API에 전달되는지 검증 가능
- fetchNextPage pending 상태 검증 가능

---

### [FAQ]

Q. Infinite Query는 어떻게 테스트해?
A. 첫 페이지와 다음 페이지 응답을 mockResolvedValueOnce로 나누고 더보기 클릭 후 누적 목록을 검증한다.

Q. hasNextPage false는 왜 테스트해?
A. 다음 페이지가 없을 때 더보기 버튼이 숨겨지는지 확인하기 위해 중요하다.

Q. pageParam도 검증해야 해?
A. cursor나 page 기반 pagination이 중요하면 API 호출 인자로 검증할 수 있다.

---

# 10. Optimistic Update Caution

## 10.1 Optimistic Update Test

### [개념]

Optimistic Update는 서버 응답을 기다리지 않고 UI를 먼저 갱신하는 패턴이다.

Optimistic Update Test는 성공 시 optimistic UI가 유지되고 실패 시 rollback 되는지 검증한다.

---

### [핵심]

- optimistic update
- optimistic UI
- onMutate
- rollback
- onError
- onSettled
- cache update
- temporary state
- mutation failure
- user-visible result

---

### [실무]

찜하기 optimistic 성공:

```tsx
test("찜하기 클릭 즉시 찜 해제 상태를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(addFavorite).mockReturnValue(new Promise(() => {}));

  renderWithQueryClient(
    <FavoriteButton festivalId={1} initialFavorite={false} />,
  );

  await user.click(screen.getByRole("button", { name: "찜하기" }));

  expect(screen.getByRole("button", { name: "찜 해제" })).toBeInTheDocument();
});
```

실패 rollback:

```tsx
test("찜하기 실패 시 원래 상태로 rollback한다", async () => {
  const user = userEvent.setup();

  vi.mocked(addFavorite).mockRejectedValue({
    response: {
      status: 500,
    },
  });

  renderWithQueryClient(
    <FavoriteButton festivalId={1} initialFavorite={false} />,
  );

  await user.click(screen.getByRole("button", { name: "찜하기" }));

  expect(
    await screen.findByRole("button", { name: "찜하기" }),
  ).toBeInTheDocument();
  expect(screen.getByText("요청에 실패했습니다.")).toBeInTheDocument();
});
```

권장:

- optimistic UI 즉시 반영 테스트
- 실패 rollback 테스트
- 성공 유지 테스트
- rollback은 사용자 결과로 검증
- cache 직접 조작 테스트는 최소화
- 복잡하면 Integration Test로 분리

---

### [FAQ]

Q. Optimistic Update는 뭐야?
A. 서버 응답 전에 UI를 먼저 성공한 것처럼 갱신하는 패턴이다.

Q. Optimistic Update에서 가장 중요한 테스트는 뭐야?
A. 실패 시 rollback되어 사용자가 잘못된 상태를 계속 보지 않도록 하는 테스트다.

Q. cache 값을 직접 확인해야 해?
A. 보통은 cache보다 사용자 UI가 rollback되는지 확인하는 것이 좋다.

---

# 11. TanStack Query Troubleshooting

## 11.1 Query Test Not Updating

### [개념]

Query Test Not Updating은 API mock 응답이 바뀌었는데 화면이 갱신되지 않는 상황이다.

Query cache, queryKey, invalidate, mock 응답 순서, QueryClient 공유 문제를 확인해야 한다.

---

### [핵심]

원인:

- queryKey 불일치
- invalidate target 불일치
- QueryClient가 서로 다름
- cache stale data 유지
- mockResolvedValueOnce 순서 오류
- refetch trigger 없음
- enabled false
- retry delay
- async findBy 누락
- Provider 중첩 문제

---

### [실무]

Debug Flow:

```text
Query UI 갱신 안 됨
→ queryKey 확인
→ API mock 호출 여부 확인
→ mockResolvedValueOnce 순서 확인
→ invalidateQueries target 확인
→ 같은 QueryClientProvider 안에 있는지 확인
→ enabled 조건 확인
→ findBy로 새 UI 대기
```

문제 예:

```text
ReviewForm은 QueryClient A 사용
ReviewList는 QueryClient B 사용
→ invalidateQueries 해도 목록이 갱신되지 않음
```

권장:

- 관련 Component를 같은 QueryClientProvider 안에 렌더링
- queryKey factory 사용
- mutation 후 UI 갱신 결과 검증
- 테스트마다 새 QueryClient 사용하되 한 테스트 안에서는 공유
- screen.debug로 현재 UI 확인

---

### [FAQ]

Q. invalidate 후 화면이 안 바뀌어.
A. queryKey가 맞는지, 같은 QueryClient를 공유하는지, refetch mock 응답이 설정되었는지 확인한다.

Q. mockResolvedValueOnce 순서가 중요한가?
A. 중요하다. 첫 요청과 refetch 요청의 응답 순서를 맞춰야 한다.

Q. QueryClient가 여러 개면 문제가 돼?
A. 한 테스트 안에서 관련 Component가 서로 다른 QueryClient를 쓰면 cache invalidation이 연결되지 않는다.

---

## 11.2 Query Test Slow or Flaky

### [개념]

Query Test Slow or Flaky는 TanStack Query 테스트가 느리거나 간헐적으로 실패하는 상황이다.

retry, cache 공유, 비동기 대기 누락, fake timer 충돌, 실제 API 호출을 확인해야 한다.

---

### [핵심]

원인:

- retry true
- stale cache
- shared QueryClient
- actual API call
- waitFor 남용
- findBy 누락
- fake timer conflict
- unresolved promise
- MSW handler mismatch
- test cleanup 문제

---

### [실무]

Debug Flow:

```text
Query 테스트 느림 / 불안정
→ retry false 확인
→ 실제 API 호출 여부 확인
→ QueryClient 공유 여부 확인
→ mock reset 확인
→ findBy 사용 확인
→ waitFor 남용 확인
→ pending promise 테스트 종료 조건 확인
```

권장 설정:

```tsx
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: false,
    },
    mutations: {
      retry: false,
    },
  },
});
```

권장:

- retry false 설정
- 테스트마다 새 QueryClient
- 실제 API 호출 금지
- 비동기 UI는 findBy 사용
- pending promise는 loading 확인 후 종료
- waitFor 안에서 userEvent 실행 금지

---

### [FAQ]

Q. TanStack Query 테스트가 느린 이유는?
A. retry가 켜져 있거나 실제 API 호출이 발생하거나 비동기 대기가 잘못되었을 수 있다.

Q. flaky test는 어떻게 줄여?
A. retry false, 새 QueryClient, 안정적인 mock, findBy 사용, mock reset을 적용한다.

Q. waitFor를 많이 쓰면 안정적이야?
A. 아니다. 요소 등장에는 findBy가 더 명확하고 waitFor 남용은 실패 원인을 흐릴 수 있다.

---

# 12. TanStack Query Anti Pattern

## 12.1 Common TanStack Query Testing Anti Patterns

### [개념]

TanStack Query Testing Anti Pattern은 QueryClient, cache, retry, API mock, UI state 검증을 잘못 사용해 테스트가 불안정해지는 방식이다.

---

### [핵심]

Anti Pattern:

- QueryClientProvider 누락
- 전역 QueryClient 재사용
- retry true 방치
- 실제 API 호출
- cache 직접 검증 남용
- invalidateQueries 호출 여부만 검증
- 사용자 UI 결과 미검증
- queryKey 불일치 방치
- mock response shape 불일치
- enabled false case 누락
- error / empty / loading state 누락
- waitFor 남용
- test 간 cache 공유
- pending promise로 테스트 hang

---

### [실무]

나쁜 예:

```tsx
const queryClient = new QueryClient();

test("목록을 표시한다", async () => {
  render(
    <QueryClientProvider client={queryClient}>
      <FestivalListPage />
    </QueryClientProvider>,
  );

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

문제:

```text
전역 QueryClient 재사용
retry 기본값 사용
cache가 테스트 간 공유될 수 있음
```

좋은 예:

```tsx
test("목록을 표시한다", async () => {
  vi.mocked(getFestivals).mockResolvedValue([
    { festivalId: 1, title: "봄꽃 축제" },
  ]);

  renderWithQueryClient(<FestivalListPage />);

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

검수 기준:

```text
테스트마다 새 QueryClient인가?
retry false인가?
실제 API 호출이 없는가?
사용자 UI 결과를 검증하는가?
Query 상태별 테스트가 있는가?
```

---

### [FAQ]

Q. TanStack Query 테스트에서 가장 흔한 실수는 뭐야?
A. 전역 QueryClient 재사용, retry false 누락, 실제 API 호출, UI 결과 미검증이다.

Q. cache 직접 검증은 왜 지양해?
A. 사용자가 보는 결과와 직접 연결되지 않으면 구현 세부사항 테스트가 되기 쉽다.

Q. invalidateQueries 호출만 테스트하면 왜 부족해?
A. 호출은 되었지만 실제 UI가 갱신되지 않을 수 있으므로 사용자 결과를 검증해야 한다.

---

# 13. TanStack Query Testing Checklist

## 13.1 TanStack Query Testing Checklist

### [개념]

TanStack Query Testing Checklist는 QueryClient 설정, API Mocking, 상태 UI, mutation 결과, cache isolation 기준을 검수하는 체크리스트다.

---

### [핵심]

Checklist:

```md
- [ ] QueryClientProvider로 감쌌는가?
- [ ] 테스트마다 새 QueryClient를 생성했는가?
- [ ] queries retry false를 설정했는가?
- [ ] mutations retry false를 설정했는가?
- [ ] 실제 API 호출을 피했는가?
- [ ] mock response shape가 실제 API와 일치하는가?
- [ ] useQuery loading 상태를 테스트했는가?
- [ ] useQuery success 상태를 테스트했는가?
- [ ] useQuery error 상태를 테스트했는가?
- [ ] useQuery empty 상태를 테스트했는가?
- [ ] enabled false 조건을 테스트했는가?
- [ ] queryKey 변경 시 refetch를 테스트했는가?
- [ ] useMutation pending 상태를 테스트했는가?
- [ ] useMutation success 상태를 테스트했는가?
- [ ] useMutation error 상태를 테스트했는가?
- [ ] mutation variables가 올바른지 확인했는가?
- [ ] invalidate 결과를 UI 갱신으로 검증했는가?
- [ ] infinite query의 hasNextPage를 테스트했는가?
- [ ] test 간 Query Cache 공유를 방지했는가?
- [ ] 실제 token / secret / 개인정보를 사용하지 않았는가?
```

---

### [실무]

Agent TanStack Query Test 작성 Flow:

```text
Identify Query or Mutation
→ Create Test QueryClient
→ Wrap with QueryClientProvider
→ Mock API Response
→ Test Loading / Success / Error / Empty
→ Test Mutation Pending / Success / Error
→ Test Invalidation Result if Needed
→ Check Query Cache Isolation
→ Review Anti Pattern
```

예:

```text
Review Section
→ getReviews query loading
→ getReviews success
→ getReviews empty
→ createReview mutation pending
→ createReview success
→ getReviews refetch result
→ createReview error
```

---

### [FAQ]

Q. TanStack Query Testing Checklist의 핵심은 뭐야?
A. 새 QueryClient, retry false, API mock, 상태 UI 검증, cache isolation이다.

Q. TanStack Query 테스트 작성 전 무엇을 정해야 해?
A. queryKey, API response shape, loading/error/empty/success UI, mutation 후 갱신 정책을 정해야 한다.

Q. TanStack Query 테스트가 불안정하면 무엇을 확인해?
A. retry false, QueryClient 공유, mock reset, API mock shape, findBy 사용 여부를 확인한다.

---

# 14. Part11 Summary

## 14.1 TanStack Query Testing Final Rule

### [개념]

Frontend Testing Part11은 TanStack Query 기반 서버 상태 테스트 기준을 정의한다.

이 Part의 목적은 Agent가 QueryClient, useQuery, useMutation, queryKey, invalidation, cache isolation을 안정적으로 테스트하고 사용자 UI 결과를 검증하게 만드는 것이다.

---

### [핵심]

최종 기준:

- Query Component는 QueryClientProvider로 감쌈
- 테스트마다 새 QueryClient 생성
- queries / mutations retry false 설정
- 실제 API 호출 금지
- useQuery는 Loading / Success / Error / Empty 상태 테스트
- EmptyState는 성공 응답의 빈 데이터로 검증
- ErrorState는 mockRejectedValue와 사용자 메시지로 검증
- enabled false 조건은 API 미호출 검증
- queryKey 변경은 새 UI 결과와 API 인자로 검증
- useMutation은 Pending / Success / Error 상태 테스트
- mutation variables는 request DTO 기준으로 검증
- invalidateQueries 직접 호출보다 UI 갱신 결과 검증
- Infinite Query는 더보기와 hasNextPage 검증
- Optimistic Update는 성공 유지와 실패 rollback 검증
- Query Cache가 테스트 간 공유되지 않게 관리
- 실제 token / secret / 개인정보 사용 금지

---

### [실무]

Agent 작업 Flow:

```text
TanStack Query Test Request
→ Identify QueryClient Need
→ Create Isolated QueryClient
→ Mock Query or Mutation API
→ Render with QueryClientProvider
→ Assert Loading / Success / Error / Empty
→ Assert Mutation Pending / Success / Error
→ Assert Invalidation Result if Needed
→ Check Cache Isolation
→ Remove Anti Pattern
```

Part12 이후 연결:

```text
Part11 TanStack Query Testing
→ Part12 Accessibility Testing
→ Part13 Snapshot Test Caution
→ Part14 Test Structure
→ Part15 Troubleshooting
→ Part16 Frontend Testing Review
```

---

### [FAQ]

Q. Part11의 최종 목적은 뭐야?
A. Frontend Agent가 TanStack Query 기반 서버 상태를 안정적으로 테스트하고 사용자 UI 결과를 검증하게 만드는 것이다.

Q. TanStack Query Testing에서 가장 중요한 규칙은 뭐야?
A. 테스트마다 새 QueryClient를 만들고 retry false로 설정하며 실제 API 대신 mock 응답으로 UI 상태를 검증하는 것이다.

Q. Part11 다음에는 어떤 내용이 이어져야 해?
A. role, label, keyboard, aria, axe 기반 접근성 테스트 기준이 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. TanStack Query Testing은 뭐야?
A. useQuery, useMutation, Query Cache, loading/error/success 상태를 테스트하는 것이다.

Q. TanStack Query Component 테스트에서 가장 중요한 설정은 뭐야?
A. QueryClientProvider로 감싸고 테스트마다 새 QueryClient를 생성하는 것이다.

Q. retry false는 왜 필요해?
A. 실패 테스트가 재시도 때문에 느려지거나 불안정해지는 것을 막기 위해 필요하다.

Q. QueryClient 내부 cache를 직접 확인해야 해?
A. 보통은 직접 확인보다 사용자 UI 결과를 검증하는 것이 좋다.

Q. invalidateQueries 호출 여부를 테스트해야 해?
A. 직접 호출 여부보다 목록이 갱신되는 사용자 결과를 검증하는 것이 좋다.

Q. Test QueryClient는 왜 필요해?
A. TanStack Query Hook은 QueryClientProvider 안에서 동작하므로 테스트에도 QueryClient가 필요하다.

Q. QueryClient를 전역으로 하나만 만들어도 돼?
A. 권장하지 않는다. cache가 테스트 간 공유되어 불안정해질 수 있다.

Q. No QueryClient set 오류는 왜 나?
A. QueryClientProvider 없이 useQuery 또는 useMutation을 사용하는 Component를 렌더링했기 때문이다.

Q. 해결 방법은 뭐야?
A. 테스트에서 QueryClientProvider로 Component를 감싸야 한다.

Q. renderWithProviders에 QueryClientProvider를 넣어도 돼?
A. 좋다. Query를 사용하는 Page 테스트에서 반복 설정을 줄일 수 있다.

Q. useQuery Loading은 어떻게 테스트해?
A. queryFn mock을 pending promise로 두고 loading message, spinner, skeleton을 검증한다.

Q. mockResolvedValue로 loading 테스트가 가능해?
A. 응답이 즉시 완료되어 loading이 지나갈 수 있으므로 pending promise가 더 안정적이다.

Q. useQuery Success는 어떻게 테스트해?
A. queryFn mockResolvedValue를 설정하고 화면에 데이터가 표시되는지 findBy로 검증한다.

Q. success response shape는 실제 API와 같아야 해?
A. 가능하면 실제 API 함수 반환 shape와 맞춰야 한다.

Q. useQuery Error는 어떻게 테스트해?
A. queryFn mockRejectedValue를 설정하고 ErrorState 또는 오류 메시지가 표시되는지 findBy로 확인한다.

Q. retry false를 설정하지 않으면 어떻게 돼?
A. 실패 테스트가 재시도 때문에 느려지거나 예측하기 어려워질 수 있다.

Q. useQuery Empty는 어떻게 테스트해?
A. queryFn mockResolvedValue로 빈 배열이나 빈 content를 반환하고 EmptyState를 검증한다.

Q. 빈 배열과 error는 달라?
A. 다르다. 빈 배열은 성공 응답이고 error는 실패 응답이다.

Q. enabled false Query는 왜 테스트해?
A. 필수 조건이 없을 때 불필요한 API 호출을 막는지 확인하기 위해 필요하다.

Q. disabled query는 어떤 UI를 보여줘야 해?
A. 상황에 따라 입력 안내, 로그인 필요 메시지, 빈 상태 등을 표시할 수 있다.

Q. queryKey 자체를 직접 테스트해야 해?
A. 보통은 API 인자와 UI 결과를 검증하는 것이 더 실용적이다.

Q. 검색 조건이 queryKey에 들어가야 하는 이유는?
A. 조건별 cache를 분리하고 조건 변경 시 새 데이터를 조회하기 위해 필요하다.

Q. queryKey 변경은 왜 테스트해?
A. 필터나 페이지가 바뀌었는데 이전 cache를 그대로 보여주는 버그를 막기 위해 필요하다.

Q. key 변경 후 기존 데이터가 잠깐 남아도 돼?
A. keep previous data 정책에 따라 가능하다. 프로젝트 UX 정책에 맞게 테스트한다.

Q. useMutation Pending은 어떻게 테스트해?
A. mutationFn을 pending promise로 만들고 버튼 disabled와 처리 중 UI를 검증한다.

Q. mutation pending 중 중복 클릭은 테스트해야 해?
A. 중복 요청 방지가 중요한 Form이나 결제, 저장, 삭제에서는 테스트하는 것이 좋다.

Q. useMutation Success는 어떻게 테스트해?
A. mutationFn mockResolvedValue를 설정하고 성공 후 표시되는 UI 결과를 검증한다.

Q. mutation 함수 호출 여부만 확인하면 돼?
A. 부족할 수 있다. 성공 메시지나 목록 갱신 같은 사용자 결과를 검증해야 한다.

Q. useMutation Error는 어떻게 테스트해?
A. mutationFn mockRejectedValue를 설정하고 오류 메시지나 field error가 표시되는지 검증한다.

Q. mutation 실패 후 버튼은 다시 활성화되어야 해?
A. 일반적으로 재시도를 위해 다시 활성화되는 것이 좋다.

Q. Mutation Variables Test는 언제 필요해?
A. Form 값이나 id가 API 요청에 올바르게 전달되는지 확인해야 할 때 필요하다.

Q. variables만 확인하면 충분해?
A. 단순 Component는 가능하지만 핵심 흐름에서는 성공 UI도 함께 검증하는 것이 좋다.

Q. mutation 후 목록 갱신은 어떻게 테스트해?
A. 목록 API mock을 첫 번째와 두 번째 응답으로 나누고 mutation 후 새 데이터가 표시되는지 확인한다.

Q. Refetch Button은 어떻게 테스트해?
A. 첫 응답과 두 번째 응답을 다르게 mock하고 버튼 클릭 후 새 데이터가 표시되는지 확인한다.

Q. Query Cache Isolation은 왜 필요해?
A. 이전 테스트의 cache 데이터가 다음 테스트 결과에 영향을 주는 것을 막기 위해 필요하다.

Q. queryClient.clear만 하면 충분해?
A. 가능하지만 테스트마다 새 QueryClient를 생성하는 방식이 더 안전하고 단순하다.

Q. Seed Query Cache는 언제 써?
A. preloaded data, optimistic state, cache 기반 초기 표시를 테스트하고 싶을 때 사용한다.

Q. setQueryData의 queryKey는 왜 중요해?
A. Component가 사용하는 queryKey와 일치해야 cache 데이터를 읽을 수 있다.

Q. Dependent Query는 뭐야?
A. 특정 값이나 선행 데이터가 있을 때만 실행되는 query다.

Q. dependent query에서 무엇을 테스트해야 해?
A. 조건이 없을 때 API가 호출되지 않고, 조건이 있을 때 정상 조회되는지 테스트한다.

Q. Infinite Query는 어떻게 테스트해?
A. 첫 페이지와 다음 페이지 응답을 mockResolvedValueOnce로 나누고 더보기 클릭 후 누적 목록을 검증한다.

Q. hasNextPage false는 왜 테스트해?
A. 다음 페이지가 없을 때 더보기 버튼이 숨겨지는지 확인하기 위해 중요하다.

Q. Optimistic Update는 뭐야?
A. 서버 응답 전에 UI를 먼저 성공한 것처럼 갱신하는 패턴이다.

Q. Optimistic Update에서 가장 중요한 테스트는 뭐야?
A. 실패 시 rollback되어 사용자가 잘못된 상태를 계속 보지 않도록 하는 테스트다.

Q. invalidate 후 화면이 안 바뀌어.
A. queryKey가 맞는지, 같은 QueryClient를 공유하는지, refetch mock 응답이 설정되었는지 확인한다.

Q. TanStack Query 테스트가 느린 이유는?
A. retry가 켜져 있거나 실제 API 호출이 발생하거나 비동기 대기가 잘못되었을 수 있다.

Q. flaky test는 어떻게 줄여?
A. retry false, 새 QueryClient, 안정적인 mock, findBy 사용, mock reset을 적용한다.

Q. TanStack Query 테스트에서 가장 흔한 실수는 뭐야?
A. 전역 QueryClient 재사용, retry false 누락, 실제 API 호출, UI 결과 미검증이다.

Q. TanStack Query Testing Checklist의 핵심은 뭐야?
A. 새 QueryClient, retry false, API mock, 상태 UI 검증, cache isolation이다.

Q. Part11 TanStack Query Testing의 최종 목표는 뭐야?
A. Frontend Agent가 TanStack Query 기반 서버 상태를 안정적으로 테스트하고 사용자 UI 결과를 검증하게 만드는 것이다.
