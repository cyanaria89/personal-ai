# Frontend Testing Part09 - Loading Error Empty

---

# 1. UI State Testing Overview

## 1.1 UI State Testing Definition

### [개념]

UI State Testing은 Frontend 화면이 데이터 요청, 사용자 입력, API 응답, 오류, 빈 데이터 상태에 따라 적절한 UI를 표시하는지 검증하는 테스트다.

Frontend Testing에서 Loading, Error, Empty, Success 상태는 핵심 사용자 경험 상태다.

---

### [핵심]

- UI State Testing
- Loading State
- Error State
- Empty State
- Success State
- Pending State
- Fetching State
- Refetching State
- Submit Loading
- API Error
- Network Error
- Empty Response
- No Result
- Retry Action
- User-visible State
- React Testing Library
- API Mocking

---

### [실무]

2026 실무 기준에서 Frontend 화면은 데이터 상태별 UI를 명확히 제공해야 한다.

기본 상태 흐름:

```text
Initial Render
→ Loading
→ Success
→ Empty
→ Error
→ Retry
```

Form 상태 흐름:

```text
Idle
→ Validating
→ Submitting
→ Success
→ Error
→ Retry / Edit
```

좋은 상태 테스트:

```text
요청 중 Loading 표시
성공 시 데이터 표시
빈 데이터 시 EmptyState 표시
실패 시 ErrorState 표시
다시 시도 버튼 동작 검증
상태 UI가 동시에 충돌하지 않는지 검증
```

나쁜 상태 테스트:

```text
API 호출 여부만 검증
Loading UI 미검증
Error message 미검증
EmptyState 미검증
getBy로 비동기 결과 검증
Error와 Empty를 혼동
```

---

### [FAQ]

Q. UI State Testing은 뭐야?
A. Loading, Error, Empty, Success 같은 화면 상태가 데이터 흐름에 따라 올바르게 표시되는지 검증하는 테스트다.

Q. Loading, Error, Empty 상태를 모두 테스트해야 해?
A. 핵심 화면에서는 테스트하는 것이 좋다. 사용자가 가장 많이 체감하는 실패와 대기 상태이기 때문이다.

Q. Success 상태만 테스트하면 부족해?
A. 부족하다. 실제 서비스에서는 실패, 빈 데이터, 로딩 상태가 자주 발생한다.

---

## 1.2 State Priority

### [개념]

State Priority는 여러 UI 상태가 동시에 가능할 때 어떤 상태를 우선 표시할지 정하는 기준이다.

Loading, Error, Empty, Success 상태가 충돌하지 않도록 명확한 우선순위가 필요하다.

---

### [핵심]

일반 우선순위:

1. Loading
2. Error
3. Empty
4. Success

상황별 예외:

- Initial Loading 우선
- Submit Loading은 Form disabled 우선
- Background Refetch는 기존 데이터 유지 가능
- Error with stale data는 기존 데이터 + error toast 가능
- Empty는 success response 이후 판단

---

### [실무]

목록 화면 상태 판단 예:

```text
isLoading true
→ LoadingState

isError true
→ ErrorState

data.length === 0
→ EmptyState

data.length > 0
→ DataList
```

주의:

```text
Loading과 Empty를 동시에 표시하지 않음
Error와 Empty를 혼동하지 않음
초기 요청 실패를 빈 데이터로 처리하지 않음
빈 배열 응답은 Error가 아님
```

테스트 케이스:

```text
loading이면 spinner 표시
error이면 error message 표시
success + empty array이면 EmptyState 표시
success + data이면 list 표시
```

---

### [FAQ]

Q. Loading과 Empty 중 무엇이 우선이야?
A. 초기 요청 중이면 Loading이 우선이고, 요청 성공 후 데이터가 없을 때 EmptyState를 표시한다.

Q. Error와 Empty는 어떻게 구분해?
A. Error는 요청 실패이고 Empty는 요청 성공 후 데이터가 없는 상태다.

Q. 상태 우선순위를 테스트해야 해?
A. 핵심 화면에서는 Loading, Error, Empty, Success가 서로 충돌하지 않는지 테스트하는 것이 좋다.

---

# 2. Loading State Test

## 2.1 Loading State Definition

### [개념]

Loading State는 데이터 요청이나 작업 처리가 아직 완료되지 않은 상태를 사용자에게 알리는 UI다.

Loading State Test는 요청 중 spinner, skeleton, loading message, disabled state가 올바르게 표시되는지 검증한다.

---

### [핵심]

Loading UI:

- spinner
- skeleton
- loading text
- role status
- aria-busy
- disabled button
- pending label
- progress indicator
- initial loading
- submit loading
- refetching indicator

---

### [실무]

목록 Loading 예:

```tsx
test("축제 목록을 불러오는 동안 loading 메시지를 표시한다", () => {
  vi.mocked(getFestivals).mockReturnValue(new Promise(() => {}));

  render(<FestivalListPage />);

  expect(screen.getByRole("status")).toHaveTextContent("불러오는 중입니다.");
});
```

Submit Loading 예:

```tsx
test("리뷰 등록 중에는 등록 버튼이 비활성화된다", async () => {
  const user = userEvent.setup();

  vi.mocked(createReview).mockReturnValue(new Promise(() => {}));

  render(<ReviewForm />);

  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(screen.getByRole("button", { name: "처리 중..." })).toBeDisabled();
});
```

권장:

- 초기 loading은 즉시 표시되므로 getBy 사용 가능
- API pending 상태는 pending promise mock 사용
- loading message는 사용자에게 의미 있는 문구
- spinner만 있으면 aria-label 또는 role status 제공
- loading 중 중복 액션 방지 확인

---

### [FAQ]

Q. Loading State는 어떻게 테스트해?
A. API mock을 pending 상태로 두고 loading text, spinner, skeleton, disabled 상태를 검증한다.

Q. Loading UI는 어떤 role이 좋아?
A. 사용자에게 로딩 상태를 알리는 경우 `status` role을 사용할 수 있다.

Q. Loading 테스트에서 findBy를 써야 해?
A. 초기 loading이 즉시 표시되면 getBy를 사용할 수 있다. 비동기로 나타나면 findBy를 사용한다.

---

## 2.2 Initial Loading Test

### [개념]

Initial Loading Test는 화면이 처음 렌더링되고 데이터를 처음 불러오는 동안 Loading UI가 표시되는지 검증하는 테스트다.

목록, 상세, 마이페이지, 대시보드 화면에서 중요하다.

---

### [핵심]

Initial Loading 대상:

- page loading
- list loading
- detail loading
- profile loading
- dashboard loading
- skeleton
- spinner
- loading message
- no premature empty
- no premature error

---

### [실무]

예:

```tsx
test("상세 정보를 불러오는 동안 loading 상태를 표시한다", () => {
  vi.mocked(getFestivalDetail).mockReturnValue(new Promise(() => {}));

  render(<FestivalDetailPage festivalId={1} />);

  expect(screen.getByRole("status")).toHaveTextContent(
    "상세 정보를 불러오는 중입니다.",
  );
});
```

Skeleton 예:

```tsx
test("초기 로딩 중에는 skeleton을 표시한다", () => {
  vi.mocked(getFestivals).mockReturnValue(new Promise(() => {}));

  render(<FestivalListPage />);

  expect(screen.getByLabelText("축제 목록 로딩 중")).toBeInTheDocument();
});
```

상태 충돌 검증:

```tsx
expect(screen.queryByText("표시할 축제가 없습니다.")).not.toBeInTheDocument();
expect(screen.queryByText("서버 오류가 발생했습니다.")).not.toBeInTheDocument();
```

권장:

- 초기 로딩과 빈 데이터 상태 구분
- loading 중 EmptyState 미표시 확인 가능
- loading UI가 접근 가능해야 함
- skeleton은 aria-label 또는 text로 식별 가능하게 설계

---

### [FAQ]

Q. Initial Loading Test는 왜 필요해?
A. 사용자가 데이터 로딩 중 빈 화면을 보지 않도록 적절한 대기 UI를 제공하는지 확인하기 위해 필요하다.

Q. loading 중 EmptyState가 보이면 안 돼?
A. 일반적으로 요청이 완료되기 전에는 EmptyState를 표시하지 않는 것이 좋다.

Q. skeleton은 어떻게 테스트해?
A. accessible label, status role, loading text 등을 제공하고 해당 요소가 표시되는지 확인한다.

---

## 2.3 Submit Loading Test

### [개념]

Submit Loading Test는 Form 제출, 저장, 삭제, 좋아요, 찜하기 같은 mutation 작업 중 버튼 비활성화와 처리 중 UI가 표시되는지 검증하는 테스트다.

중복 요청 방지에 중요하다.

---

### [핵심]

Submit Loading 대상:

- form submit
- save button
- delete button
- like button
- favorite button
- payment button
- processing text
- disabled button
- duplicate submit prevention
- pending mutation

---

### [실무]

예:

```tsx
test("저장 요청 중에는 저장 버튼을 비활성화한다", async () => {
  const user = userEvent.setup();

  vi.mocked(updateProfile).mockReturnValue(new Promise(() => {}));

  render(<ProfileForm />);

  await user.type(screen.getByLabelText("닉네임"), "tester");
  await user.click(screen.getByRole("button", { name: "저장" }));

  expect(screen.getByRole("button", { name: "저장 중..." })).toBeDisabled();
});
```

중복 클릭 방지:

```tsx
test("요청 중 중복 클릭해도 API는 한 번만 호출된다", async () => {
  const user = userEvent.setup();

  vi.mocked(createReview).mockReturnValue(new Promise(() => {}));

  render(<ReviewForm />);

  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");

  await user.click(screen.getByRole("button", { name: "등록" }));
  await user.click(screen.getByRole("button", { name: "처리 중..." }));

  expect(createReview).toHaveBeenCalledTimes(1);
});
```

권장:

- 버튼 disabled 검증
- 처리 중 문구 검증
- 중복 요청 방지 검증
- 실패 후 버튼 상태 복구는 Error State Test에서 검증
- pending promise는 테스트 종료 조건 주의

---

### [FAQ]

Q. Submit Loading은 왜 테스트해?
A. 중복 제출과 중복 API 요청을 막고 사용자에게 처리 중 상태를 알려주는지 확인하기 위해 필요하다.

Q. 요청 중 버튼은 disabled 되는 게 좋아?
A. 일반적으로 mutation 중복 실행을 막기 위해 disabled 처리하는 것이 좋다.

Q. 중복 클릭 방지는 어떻게 테스트해?
A. 요청 중 버튼을 다시 클릭한 뒤 API 함수가 한 번만 호출되었는지 확인한다.

---

## 2.4 Background Refetch Test

### [개념]

Background Refetch Test는 이미 데이터가 표시된 상태에서 백그라운드로 재조회가 발생할 때 기존 데이터를 유지하면서 refetching 상태를 적절히 표시하는지 검증하는 테스트다.

TanStack Query 기반 화면에서 중요하다.

---

### [핵심]

Background Refetch 대상:

- refetching
- stale data
- keep previous data
- small loading indicator
- refresh button
- pull to refresh
- no full page loading
- existing data preserved
- isFetching
- isRefetching

---

### [실무]

상태 기준:

```text
initial loading
→ 전체 LoadingState 가능

background refetch
→ 기존 데이터 유지
→ 작은 refetch indicator 표시 가능
```

예:

```tsx
test("재조회 중에도 기존 목록을 유지한다", async () => {
  vi.mocked(getFestivals).mockResolvedValue([
    { festivalId: 1, title: "봄꽃 축제" },
  ]);

  render(<FestivalListPage />);

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();

  await user.click(screen.getByRole("button", { name: "새로고침" }));

  expect(screen.getByText("봄꽃 축제")).toBeInTheDocument();
});
```

권장:

- initial loading과 refetching 구분
- 기존 데이터가 사라지지 않는지 검증
- 작은 status indicator가 있으면 검증
- refetch 실패 시 기존 데이터 유지 정책 확인
- TanStack Query Part와 연계

---

### [FAQ]

Q. Background Refetch는 initial loading과 달라?
A. 다르다. initial loading은 데이터가 없고, background refetch는 기존 데이터가 있는 상태에서 다시 요청하는 것이다.

Q. 재조회 중 기존 데이터를 숨겨야 해?
A. 대부분의 UX에서는 기존 데이터를 유지하고 작은 로딩 표시만 제공하는 것이 좋다.

Q. 이 테스트는 항상 필요해?
A. 서버 상태 관리와 refetch UX가 중요한 화면에서 필요하다.

---

# 3. Error State Test

## 3.1 Error State Definition

### [개념]

Error State는 API 요청 실패, 권한 부족, 네트워크 오류, 서버 오류, 데이터 파싱 실패 등으로 정상 화면을 표시할 수 없을 때 사용자에게 안내하는 UI다.

Error State Test는 오류 메시지, retry action, safe fallback, 접근성 role을 검증한다.

---

### [핵심]

Error UI:

- error message
- role alert
- ErrorState component
- retry button
- forbidden message
- not found message
- network message
- server fallback
- safe error message
- error boundary fallback
- button enabled after error

---

### [실무]

API Error 예:

```tsx
test("축제 목록 조회 실패 시 ErrorState를 표시한다", async () => {
  vi.mocked(getFestivals).mockRejectedValue({
    response: {
      status: 500,
    },
  });

  render(<FestivalListPage />);

  expect(
    await screen.findByText(
      "서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.",
    ),
  ).toBeInTheDocument();
});
```

Retry 예:

```tsx
test("다시 시도 버튼을 클릭하면 목록을 다시 요청한다", async () => {
  const user = userEvent.setup();

  vi.mocked(getFestivals)
    .mockRejectedValueOnce({ response: { status: 500 } })
    .mockResolvedValueOnce([{ festivalId: 1, title: "봄꽃 축제" }]);

  render(<FestivalListPage />);

  await screen.findByText("서버 오류가 발생했습니다.");

  await user.click(screen.getByRole("button", { name: "다시 시도" }));

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

권장:

- 오류 메시지는 사용자 친화적 문구
- 서버 내부 상세 메시지 노출 금지
- retry 버튼이 있으면 동작 검증
- error 상태는 EmptyState와 구분
- 비동기 오류 UI는 findBy 사용

---

### [FAQ]

Q. Error State는 어떻게 테스트해?
A. API mock을 실패 상태로 만들고 오류 메시지, alert, retry 버튼, 상태 복구를 검증한다.

Q. 서버 내부 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 안전하고 일반적인 사용자 메시지로 변환해 표시한다.

Q. ErrorState는 EmptyState와 어떻게 달라?
A. ErrorState는 요청 실패이고 EmptyState는 요청 성공 후 데이터가 없는 상태다.

---

## 3.2 HTTP Status Error Test

### [개념]

HTTP Status Error Test는 401, 403, 404, 409, 500 등 상태 코드별로 적절한 UI가 표시되는지 검증하는 테스트다.

상태 코드별 UX 정책을 명확히 해야 한다.

---

### [핵심]

Status별 UI:

- 400 Validation Error
- 401 Login Required
- 403 Forbidden
- 404 Not Found
- 409 Conflict
- 500 Server Error
- Network Error
- Timeout Error

---

### [실무]

401 예:

```tsx
test("401 오류이면 로그인 필요 메시지를 표시한다", async () => {
  vi.mocked(getMyPage).mockRejectedValue({
    response: {
      status: 401,
    },
  });

  render(<MyPage />);

  expect(await screen.findByText("로그인이 필요합니다.")).toBeInTheDocument();
});
```

403 예:

```tsx
test("403 오류이면 접근 권한 없음 메시지를 표시한다", async () => {
  vi.mocked(getAdminData).mockRejectedValue({
    response: {
      status: 403,
    },
  });

  render(<AdminPage />);

  expect(await screen.findByText("접근 권한이 없습니다.")).toBeInTheDocument();
});
```

404 예:

```tsx
test("404 오류이면 Not Found 메시지를 표시한다", async () => {
  vi.mocked(getFestivalDetail).mockRejectedValue({
    response: {
      status: 404,
    },
  });

  render(<FestivalDetailPage festivalId={999} />);

  expect(
    await screen.findByText("요청한 정보를 찾을 수 없습니다."),
  ).toBeInTheDocument();
});
```

권장:

- 실제 코드에서 분기하는 status 우선 테스트
- 401과 403 구분
- 404는 Not Found UI 검증
- 409는 중복 / 충돌 메시지 검증
- 500은 fallback message 검증

---

### [FAQ]

Q. HTTP Status Error Test는 왜 필요해?
A. 상태 코드별로 로그인 필요, 권한 없음, Not Found, 서버 오류 안내가 달라지기 때문이다.

Q. 401과 403은 어떻게 다르게 테스트해?
A. 401은 로그인 필요 또는 redirect, 403은 권한 없음 메시지를 검증한다.

Q. 모든 status code를 다 테스트해야 해?
A. 아니다. 실제 서비스에서 분기하는 주요 status를 우선 테스트한다.

---

## 3.3 Network Error Test

### [개념]

Network Error Test는 서버 응답을 받지 못한 상태에서 네트워크 오류 안내와 retry action이 표시되는지 검증하는 테스트다.

Network Error는 HTTP 500과 다르다.

---

### [핵심]

Network Error 상황:

- no response
- offline
- timeout
- connection refused
- request failed
- error.request
- fallback message
- retry button
- network recovery

---

### [실무]

예:

```tsx
test("네트워크 오류이면 연결 확인 메시지를 표시한다", async () => {
  vi.mocked(getFestivals).mockRejectedValue({
    request: {},
    message: "Network Error",
  });

  render(<FestivalListPage />);

  expect(
    await screen.findByText("네트워크 연결을 확인해 주세요."),
  ).toBeInTheDocument();
});
```

Retry 예:

```tsx
test("네트워크 오류 후 다시 시도할 수 있다", async () => {
  const user = userEvent.setup();

  vi.mocked(getFestivals)
    .mockRejectedValueOnce({ request: {}, message: "Network Error" })
    .mockResolvedValueOnce([{ festivalId: 1, title: "봄꽃 축제" }]);

  render(<FestivalListPage />);

  await screen.findByText("네트워크 연결을 확인해 주세요.");

  await user.click(screen.getByRole("button", { name: "다시 시도" }));

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

권장:

- response 없는 error case 테스트
- network error와 server error 메시지 구분
- retry action 검증
- offline 상태 문구 검토
- 사용자에게 기술적 메시지 노출 지양

---

### [FAQ]

Q. Network Error와 500 Error는 달라?
A. 다르다. Network Error는 서버 응답 자체를 받지 못한 상태이고 500은 서버가 오류 응답을 반환한 상태다.

Q. Network Error mock에는 response가 없어도 돼?
A. 그렇다. 실제 네트워크 오류에서는 response가 없을 수 있다.

Q. Network Error UI는 무엇을 보여줘야 해?
A. 네트워크 연결 확인 안내와 다시 시도 버튼이 적합하다.

---

## 3.4 Retry Action Test

### [개념]

Retry Action Test는 오류 발생 후 사용자가 다시 시도 버튼을 눌렀을 때 API 요청이 재실행되고 상태가 회복되는지 검증하는 테스트다.

---

### [핵심]

Retry 검증 대상:

- retry button
- refetch
- API called again
- error to loading
- error to success
- retry disabled while pending
- retry failure again
- user-visible recovery

---

### [실무]

성공 복구 예:

```tsx
test("다시 시도 후 성공하면 데이터를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(getFestivals)
    .mockRejectedValueOnce({ response: { status: 500 } })
    .mockResolvedValueOnce([{ festivalId: 1, title: "봄꽃 축제" }]);

  render(<FestivalListPage />);

  expect(
    await screen.findByText("서버 오류가 발생했습니다."),
  ).toBeInTheDocument();

  await user.click(screen.getByRole("button", { name: "다시 시도" }));

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

재실패 예:

```tsx
test("다시 시도해도 실패하면 오류 메시지를 유지한다", async () => {
  const user = userEvent.setup();

  vi.mocked(getFestivals)
    .mockRejectedValueOnce({ response: { status: 500 } })
    .mockRejectedValueOnce({ response: { status: 500 } });

  render(<FestivalListPage />);

  await screen.findByText("서버 오류가 발생했습니다.");

  await user.click(screen.getByRole("button", { name: "다시 시도" }));

  expect(
    await screen.findByText("서버 오류가 발생했습니다."),
  ).toBeInTheDocument();
});
```

권장:

- retry 버튼은 role button으로 찾음
- retry 후 성공 UI 검증
- retry 중 버튼 disabled 검증 가능
- API 호출 횟수보다 사용자 회복 결과 우선
- 재실패 case도 필요 시 테스트

---

### [FAQ]

Q. Retry Action Test는 왜 필요해?
A. 사용자가 오류 상태에서 직접 회복할 수 있는지 검증하기 위해 필요하다.

Q. retry 버튼 클릭 후 무엇을 확인해?
A. API 재요청 후 성공 데이터가 표시되거나 오류 상태가 유지되는지 확인한다.

Q. API 호출 횟수만 확인하면 충분해?
A. 부족할 수 있다. 사용자가 보는 회복 결과를 검증하는 것이 좋다.

---

# 4. Empty State Test

## 4.1 Empty State Definition

### [개념]

Empty State는 API 요청은 성공했지만 표시할 데이터가 없을 때 사용자에게 안내하는 UI다.

Empty State Test는 빈 목록, 검색 결과 없음, 알림 없음, 리뷰 없음, 찜 목록 없음 같은 상태를 검증한다.

---

### [핵심]

Empty UI:

- empty message
- no data message
- no result message
- no review
- no notification
- no favorite
- no search result
- reset filter button
- create button
- first use guide
- success with empty data

---

### [실무]

빈 목록 예:

```tsx
test("축제 목록이 비어 있으면 EmptyState를 표시한다", async () => {
  vi.mocked(getFestivals).mockResolvedValue([]);

  render(<FestivalListPage />);

  expect(
    await screen.findByText("표시할 축제가 없습니다."),
  ).toBeInTheDocument();
});
```

검색 결과 없음:

```tsx
test("검색 결과가 없으면 안내 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(searchFestivals).mockResolvedValue([]);

  render(<FestivalSearchPage />);

  await user.type(screen.getByLabelText("검색어"), "없는축제");
  await user.click(screen.getByRole("button", { name: "검색" }));

  expect(await screen.findByText("검색 결과가 없습니다.")).toBeInTheDocument();
});
```

권장:

- empty response는 mockResolvedValue([]) 사용
- EmptyState는 ErrorState와 구분
- 검색 결과 없음과 최초 데이터 없음 메시지 구분
- action이 있으면 callback 또는 UI 결과 검증
- loading 중 EmptyState 미표시 검증 가능

---

### [FAQ]

Q. Empty State는 뭐야?
A. API 요청은 성공했지만 표시할 데이터가 없을 때 보여주는 안내 UI다.

Q. Empty State는 Error State와 달라?
A. 다르다. Empty State는 성공 응답의 빈 데이터이고 Error State는 요청 실패다.

Q. Empty State는 왜 테스트해야 해?
A. 빈 화면 대신 사용자에게 현재 상태와 다음 행동을 안내하는지 확인하기 위해 필요하다.

---

## 4.2 No Result Test

### [개념]

No Result Test는 사용자가 검색이나 필터를 실행했지만 결과가 없을 때 적절한 안내 메시지와 필터 초기화 action이 표시되는지 검증하는 테스트다.

---

### [핵심]

No Result 대상:

- search no result
- filter no result
- keyword no result
- category no result
- region no result
- date range no result
- reset filter
- change keyword guide
- no result message

---

### [실무]

검색 결과 없음:

```tsx
test("키워드 검색 결과가 없으면 검색 결과 없음 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(searchFestivals).mockResolvedValue([]);

  render(<FestivalSearchPage />);

  await user.type(screen.getByLabelText("검색어"), "없는축제");
  await user.click(screen.getByRole("button", { name: "검색" }));

  expect(await screen.findByText("검색 결과가 없습니다.")).toBeInTheDocument();
});
```

필터 초기화:

```tsx
test("검색 결과 없음 상태에서 필터 초기화를 실행한다", async () => {
  const user = userEvent.setup();

  vi.mocked(searchFestivals).mockResolvedValue([]);

  render(<FestivalSearchPage />);

  await user.selectOptions(
    screen.getByRole("combobox", { name: "지역" }),
    "seoul",
  );
  await user.click(screen.getByRole("button", { name: "검색" }));

  expect(await screen.findByText("검색 결과가 없습니다.")).toBeInTheDocument();

  await user.click(screen.getByRole("button", { name: "필터 초기화" }));

  expect(screen.getByRole("combobox", { name: "지역" })).toHaveValue("");
});
```

권장:

- 검색 결과 없음 문구 검증
- 필터 초기화 action 검증
- keyword / filter 조건이 화면에 반영되는지 검증 가능
- 빈 결과와 API 실패 구분
- no result 상태에서도 검색 Form은 유지

---

### [FAQ]

Q. No Result Test는 Empty State Test와 같아?
A. 비슷하지만 No Result는 검색이나 필터 조건 때문에 결과가 없는 상태에 초점을 둔다.

Q. 검색 결과 없음 상태에서 무엇을 보여줘야 해?
A. 결과 없음 메시지와 검색어 변경 또는 필터 초기화 action이 좋다.

Q. 필터 초기화 버튼도 테스트해야 해?
A. 제공한다면 클릭 후 필터 값이 초기화되는지 테스트하는 것이 좋다.

---

## 4.3 First Use Empty State Test

### [개념]

First Use Empty State Test는 사용자가 아직 데이터를 생성하거나 활동하지 않은 상태에서 안내 메시지와 시작 action이 표시되는지 검증하는 테스트다.

찜 목록 없음, 작성한 리뷰 없음, 알림 없음, 저장된 주소 없음 같은 상태에 사용한다.

---

### [핵심]

First Use Empty 대상:

- no favorite
- no review
- no notification
- no post
- no history
- no saved item
- create first item
- start guide
- call to action

---

### [실무]

찜 목록 없음:

```tsx
test("찜한 축제가 없으면 첫 사용 안내를 표시한다", async () => {
  vi.mocked(getFavorites).mockResolvedValue([]);

  render(<FavoriteFestivalPage />);

  expect(
    await screen.findByText("아직 찜한 축제가 없습니다."),
  ).toBeInTheDocument();
  expect(
    screen.getByRole("link", { name: "축제 둘러보기" }),
  ).toBeInTheDocument();
});
```

리뷰 없음:

```tsx
test("작성한 리뷰가 없으면 리뷰 없음 메시지를 표시한다", async () => {
  vi.mocked(getMyReviews).mockResolvedValue([]);

  render(<MyReviewPage />);

  expect(
    await screen.findByText("작성한 리뷰가 없습니다."),
  ).toBeInTheDocument();
});
```

권장:

- first use message는 사용자가 다음 행동을 알 수 있어야 함
- action link / button 검증
- 검색 결과 없음과 문구 구분
- 빈 데이터가 정상 상태임을 사용자에게 안내

---

### [FAQ]

Q. First Use Empty State는 뭐야?
A. 사용자가 아직 데이터를 만들거나 활동하지 않아 목록이 비어 있는 정상 상태를 안내하는 UI다.

Q. 검색 결과 없음과 First Use Empty는 달라?
A. 다르다. 검색 결과 없음은 조건에 맞는 결과가 없는 상태이고 First Use Empty는 아직 데이터 자체가 없는 상태다.

Q. EmptyState에 action을 넣어야 해?
A. 사용자가 다음 행동을 할 수 있도록 link나 button을 제공하는 것이 좋다.

---

# 5. Success State Test

## 5.1 Success State Definition

### [개념]

Success State는 API 요청이나 사용자 작업이 성공했을 때 사용자에게 결과를 명확히 보여주는 UI 상태다.

목록 표시, 상세 표시, 성공 메시지, toast, redirect, form reset, modal close가 포함된다.

---

### [핵심]

Success UI:

- data list
- detail data
- success message
- toast
- redirect result
- form reset
- modal close
- updated list
- created item
- deleted item removed
- optimistic result

---

### [실무]

목록 성공:

```tsx
test("축제 목록 조회 성공 시 목록을 표시한다", async () => {
  vi.mocked(getFestivals).mockResolvedValue([
    { festivalId: 1, title: "봄꽃 축제" },
  ]);

  render(<FestivalListPage />);

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

Mutation 성공:

```tsx
test("리뷰 등록 성공 시 성공 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(createReview).mockResolvedValue({
    reviewId: 1,
    content: "좋았어요",
  });

  render(<ReviewForm />);

  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(await screen.findByText("리뷰가 등록되었습니다.")).toBeInTheDocument();
});
```

권장:

- 성공 후 사용자에게 보이는 결과 검증
- 단순 API 호출 여부보다 UI 결과 우선
- 목록 갱신 / redirect / reset / close 정책 검증
- 비동기 success UI는 findBy 사용
- success와 loading/error/empty 충돌 방지

---

### [FAQ]

Q. Success State는 뭐야?
A. API 요청이나 사용자 작업이 성공했을 때 데이터, 성공 메시지, 이동 결과 등을 표시하는 상태다.

Q. Success Test에서 API 호출 여부만 확인하면 돼?
A. 부족하다. 사용자가 보는 성공 결과를 검증해야 한다.

Q. 성공 메시지는 어떻게 테스트해?
A. 비동기 작업 후 표시되면 `await screen.findByText`로 검증한다.

---

## 5.2 Mutation Success Test

### [개념]

Mutation Success Test는 생성, 수정, 삭제, 좋아요, 찜하기 같은 변경 작업이 성공했을 때 UI가 올바르게 갱신되는지 검증하는 테스트다.

---

### [핵심]

Mutation 성공 대상:

- create success
- update success
- delete success
- like success
- favorite success
- review create
- profile update
- toast message
- list update
- item removed
- button state changed
- cache invalidation result

---

### [실무]

찜하기 성공:

```tsx
test("찜하기 성공 시 버튼 문구가 찜 해제로 변경된다", async () => {
  const user = userEvent.setup();

  vi.mocked(addFavorite).mockResolvedValue({
    favorite: true,
  });

  render(<FavoriteButton festivalId={1} initialFavorite={false} />);

  await user.click(screen.getByRole("button", { name: "찜하기" }));

  expect(
    await screen.findByRole("button", { name: "찜 해제" }),
  ).toBeInTheDocument();
});
```

삭제 성공:

```tsx
test("삭제 성공 시 목록에서 항목이 제거된다", async () => {
  const user = userEvent.setup();

  vi.mocked(deleteReview).mockResolvedValue(undefined);

  render(
    <ReviewList initialReviews={[{ reviewId: 1, content: "좋았어요" }]} />,
  );

  await user.click(screen.getByRole("button", { name: "삭제" }));

  expect(await screen.findByText("리뷰가 삭제되었습니다.")).toBeInTheDocument();
  expect(screen.queryByText("좋았어요")).not.toBeInTheDocument();
});
```

권장:

- 버튼 상태 변경 검증
- 성공 메시지 검증
- 목록 갱신 검증
- 삭제 후 항목 제거 검증
- cache invalidation은 사용자 결과 중심으로 검증

---

### [FAQ]

Q. Mutation Success Test는 뭘 확인해?
A. 생성, 수정, 삭제, 좋아요, 찜하기 성공 후 UI가 올바르게 바뀌는지 확인한다.

Q. invalidateQueries 호출 여부를 테스트해야 해?
A. 보통 직접 호출 여부보다 목록이 갱신되는 사용자 결과를 검증하는 것이 좋다.

Q. 삭제 성공은 어떻게 테스트해?
A. 삭제 후 성공 메시지와 해당 항목이 목록에서 사라졌는지 확인한다.

---

# 6. Combined State Flow Test

## 6.1 Loading To Success Test

### [개념]

Loading To Success Test는 요청 중 Loading UI가 표시되고 요청 성공 후 데이터 UI로 전환되는지 검증하는 테스트다.

상태 전환을 검증할 때 사용한다.

---

### [핵심]

Flow:

- loading visible
- resolve API
- loading removed
- data visible
- no error
- no empty
- async transition
- controlled promise

---

### [실무]

예:

```tsx
test("loading 후 성공 데이터를 표시한다", async () => {
  const request = deferred<Array<{ festivalId: number; title: string }>>();

  vi.mocked(getFestivals).mockReturnValue(request.promise);

  render(<FestivalListPage />);

  expect(screen.getByRole("status")).toHaveTextContent("불러오는 중입니다.");

  request.resolve([{ festivalId: 1, title: "봄꽃 축제" }]);

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
  expect(screen.queryByRole("status")).not.toBeInTheDocument();
});
```

권장:

- controlled promise 사용 가능
- loading 표시와 제거 모두 확인
- success data 표시 검증
- setTimeout 고정 대기 지양
- 상태 전환이 중요한 화면에 적용

---

### [FAQ]

Q. Loading To Success Test는 언제 필요해?
A. Loading UI가 실제 데이터 표시로 전환되는 흐름을 보장해야 할 때 필요하다.

Q. loading 제거도 확인해야 해?
A. 중요한 화면에서는 확인하는 것이 좋다. loading이 계속 남는 버그를 잡을 수 있다.

Q. controlled promise는 왜 써?
A. 테스트에서 API 응답 시점을 직접 제어해 상태 전환을 안정적으로 검증할 수 있기 때문이다.

---

## 6.2 Loading To Error Test

### [개념]

Loading To Error Test는 요청 중 Loading UI가 표시되고 요청 실패 후 Error UI로 전환되는지 검증하는 테스트다.

---

### [핵심]

Flow:

- loading visible
- reject API
- loading removed
- error visible
- retry available
- no empty
- no success data
- async transition

---

### [실무]

예:

```tsx
test("loading 후 오류 메시지를 표시한다", async () => {
  const request = deferred<Array<{ festivalId: number; title: string }>>();

  vi.mocked(getFestivals).mockReturnValue(request.promise);

  render(<FestivalListPage />);

  expect(screen.getByRole("status")).toHaveTextContent("불러오는 중입니다.");

  request.reject({
    response: {
      status: 500,
    },
  });

  expect(
    await screen.findByText("서버 오류가 발생했습니다."),
  ).toBeInTheDocument();
  expect(screen.queryByRole("status")).not.toBeInTheDocument();
});
```

deferred helper는 reject도 제공하도록 작성한다.

```ts
function deferred<T>() {
  let resolve!: (value: T) => void;
  let reject!: (reason?: unknown) => void;

  const promise = new Promise<T>((res, rej) => {
    resolve = res;
    reject = rej;
  });

  return { promise, resolve, reject };
}
```

권장:

- loading → error 전환 검증
- error message 표시 검증
- loading 제거 검증
- retry button이 있으면 검증
- Error와 Empty가 동시에 나오지 않는지 확인 가능

---

### [FAQ]

Q. Loading To Error Test는 왜 필요해?
A. 요청 실패 시 Loading이 사라지고 사용자에게 오류 안내가 표시되는지 확인하기 위해 필요하다.

Q. reject 이후에는 어떤 Query를 써?
A. 오류 UI가 비동기로 표시되므로 findBy를 사용한다.

Q. Error와 Empty가 동시에 나오면 안 돼?
A. 일반적으로 요청 실패에서는 ErrorState만 표시해야 한다.

---

## 6.3 Error To Success Retry Test

### [개념]

Error To Success Retry Test는 첫 요청 실패 후 사용자가 다시 시도하여 성공 데이터가 표시되는 회복 흐름을 검증하는 테스트다.

---

### [핵심]

Flow:

- first request error
- error message visible
- retry click
- second request success
- data visible
- error removed
- recovery result
- user-visible retry

---

### [실무]

예:

```tsx
test("오류 후 다시 시도에 성공하면 데이터를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(getFestivals)
    .mockRejectedValueOnce({ response: { status: 500 } })
    .mockResolvedValueOnce([{ festivalId: 1, title: "봄꽃 축제" }]);

  render(<FestivalListPage />);

  expect(
    await screen.findByText("서버 오류가 발생했습니다."),
  ).toBeInTheDocument();

  await user.click(screen.getByRole("button", { name: "다시 시도" }));

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
  expect(
    screen.queryByText("서버 오류가 발생했습니다."),
  ).not.toBeInTheDocument();
});
```

권장:

- mockRejectedValueOnce / mockResolvedValueOnce 활용
- retry 버튼 클릭은 userEvent 사용
- error 제거와 data 표시 검증
- API 호출 횟수보다 회복 UI 결과 우선
- retry 중 loading indicator 검증 가능

---

### [FAQ]

Q. Error To Success Retry Test는 뭐야?
A. 첫 요청은 실패하고 다시 시도 후 성공하는 회복 흐름을 검증하는 테스트다.

Q. retry 성공 후 오류 메시지가 사라지는지도 확인해야 해?
A. 중요하다. 성공 데이터와 이전 오류 메시지가 동시에 보이면 혼란스럽다.

Q. mockResolvedValueOnce는 왜 써?
A. 첫 요청과 두 번째 요청의 응답을 다르게 제어하기 위해 사용한다.

---

# 7. Accessibility State Test

## 7.1 Loading Accessibility Test

### [개념]

Loading Accessibility Test는 로딩 상태가 보조기술 사용자에게도 전달될 수 있도록 role, aria-busy, accessible name이 제공되는지 검증하는 테스트다.

---

### [핵심]

Loading 접근성:

- role status
- aria-busy
- aria-live
- accessible loading text
- spinner aria-label
- skeleton label
- progressbar
- screen reader announcement

---

### [실무]

role status 예:

```tsx
test("로딩 상태를 status role로 제공한다", () => {
  render(<LoadingState message="불러오는 중입니다." />);

  expect(screen.getByRole("status")).toHaveTextContent("불러오는 중입니다.");
});
```

aria-busy 예:

```tsx
test("목록 영역이 로딩 중이면 aria-busy를 true로 표시한다", () => {
  render(<FestivalList loading festivals={[]} />);

  expect(screen.getByRole("region", { name: "축제 목록" })).toHaveAttribute(
    "aria-busy",
    "true",
  );
});
```

권장:

- spinner만 있는 경우 accessible name 제공
- loading text가 시각적으로 숨겨져도 보조기술에 전달되도록 설계
- 긴 작업은 progressbar 고려
- aria-live 사용 시 과도한 알림 주의

---

### [FAQ]

Q. Loading 접근성은 왜 테스트해?
A. 보조기술 사용자도 화면이 데이터를 불러오는 중임을 알아야 하기 때문이다.

Q. spinner만 있으면 충분해?
A. 충분하지 않을 수 있다. role status나 aria-label을 제공하는 것이 좋다.

Q. aria-busy는 언제 써?
A. 특정 영역이 업데이트 중임을 나타낼 때 사용할 수 있다.

---

## 7.2 Error Accessibility Test

### [개념]

Error Accessibility Test는 오류 메시지가 보조기술 사용자에게 즉시 전달될 수 있도록 role alert, aria-describedby, focus management가 적용되는지 검증하는 테스트다.

---

### [핵심]

Error 접근성:

- role alert
- aria-live
- aria-describedby
- aria-invalid
- error summary
- focus to error
- retry button accessible name
- safe message

---

### [실무]

alert 예:

```tsx
test("오류 메시지를 alert role로 제공한다", async () => {
  vi.mocked(getFestivals).mockRejectedValue({
    response: {
      status: 500,
    },
  });

  render(<FestivalListPage />);

  expect(await screen.findByRole("alert")).toHaveTextContent(
    "서버 오류가 발생했습니다.",
  );
});
```

retry button 접근성:

```tsx
expect(screen.getByRole("button", { name: "다시 시도" })).toBeInTheDocument();
```

권장:

- 중요한 오류 메시지는 role alert 고려
- Form field error는 input과 연결
- retry action은 명확한 accessible name 제공
- 오류 발생 후 focus 이동 정책이 있으면 테스트
- 기술적 error detail 대신 사용자 메시지 제공

---

### [FAQ]

Q. Error 접근성은 왜 테스트해?
A. 오류가 시각 사용자뿐 아니라 보조기술 사용자에게도 전달되어야 하기 때문이다.

Q. role alert는 언제 사용해?
A. 사용자가 즉시 알아야 하는 중요한 오류 메시지에 사용할 수 있다.

Q. retry 버튼 이름은 중요해?
A. 중요하다. 보조기술 사용자가 버튼의 목적을 이해할 수 있어야 한다.

---

## 7.3 Empty State Accessibility Test

### [개념]

Empty State Accessibility Test는 데이터가 없는 상태의 안내 메시지와 다음 action이 명확한 semantic structure로 제공되는지 검증하는 테스트다.

---

### [핵심]

Empty 접근성:

- visible message
- heading
- description
- action button
- action link
- region label
- no result announcement
- semantic structure
- focusable action

---

### [실무]

예:

```tsx
test("검색 결과 없음 상태에 안내와 필터 초기화 버튼을 제공한다", async () => {
  vi.mocked(searchFestivals).mockResolvedValue([]);

  render(<FestivalSearchPage />);

  expect(
    await screen.findByRole("heading", { name: "검색 결과가 없습니다." }),
  ).toBeInTheDocument();

  expect(
    screen.getByRole("button", { name: "필터 초기화" }),
  ).toBeInTheDocument();
});
```

권장:

- EmptyState에 heading 또는 명확한 message 제공
- 다음 action은 button/link로 제공
- 클릭 가능한 div 지양
- 검색 결과 없음은 사용자가 조건을 바꿀 수 있게 안내
- 시각적 아이콘만으로 empty 상태 전달 금지

---

### [FAQ]

Q. EmptyState에도 접근성이 필요해?
A. 필요하다. 사용자는 왜 데이터가 없는지와 다음에 무엇을 할 수 있는지 알아야 한다.

Q. EmptyState action은 어떤 요소가 좋아?
A. 실제 동작에 맞게 button 또는 link를 사용하는 것이 좋다.

Q. 아이콘만 있는 EmptyState는 괜찮아?
A. 권장하지 않는다. 텍스트 안내가 필요하다.

---

# 8. State Test Troubleshooting

## 8.1 Loading Not Showing

### [개념]

Loading Not Showing은 테스트에서 loading 상태를 기대했지만 화면에 표시되지 않는 상황이다.

API mock이 즉시 resolve되거나 loading 조건이 너무 짧거나 Query 선택이 잘못되었을 수 있다.

---

### [핵심]

원인:

- mockResolvedValue 즉시 완료
- pending promise 미사용
- loading UI 조건 누락
- initial data 존재
- stale data 유지
- isLoading / isFetching 혼동
- query retry timing
- wrong query
- hidden loading text

---

### [실무]

Debug Flow:

```text
Loading 안 보임
→ API mock이 즉시 resolve되는지 확인
→ pending promise 사용 여부 확인
→ loading 조건 확인
→ isLoading / isFetching 구분 확인
→ screen.debug 확인
→ loading text / role 확인
```

수정 예:

```tsx
vi.mocked(getFestivals).mockReturnValue(new Promise(() => {}));

render(<FestivalListPage />);

expect(screen.getByRole("status")).toHaveTextContent("불러오는 중입니다.");
```

권장:

- Loading 검증에는 pending promise 사용
- 즉시 resolve mock으로 loading 검증하지 않음
- refetch loading은 initial loading과 다르게 테스트
- 로딩 표시 시간이 너무 짧으면 UX 정책 검토

---

### [FAQ]

Q. Loading UI가 테스트에서 안 보여.
A. API mock이 즉시 resolve되어 loading 상태가 지나갔을 수 있다. pending promise를 사용한다.

Q. mockResolvedValue로 loading 테스트가 가능해?
A. 어려울 수 있다. loading 상태를 안정적으로 보려면 pending promise가 적합하다.

Q. isLoading과 isFetching은 달라?
A. 다르다. initial loading과 background fetching을 구분해야 한다.

---

## 8.2 Error Not Showing

### [개념]

Error Not Showing은 API 실패 mock을 설정했지만 오류 메시지가 표시되지 않는 상황이다.

mockRejectedValue shape, error handling 코드, async 대기, Query 선택을 확인해야 한다.

---

### [핵심]

원인:

- mockRejectedValue shape 불일치
- error.response.status 누락
- catch 처리 누락
- ErrorBoundary 필요
- retry 중 상태
- async result에 getBy 사용
- error message mapping 불일치
- mock path mismatch
- actual API called

---

### [실무]

Debug Flow:

```text
Error 안 보임
→ mockRejectedValue가 적용되는지 확인
→ error shape 확인
→ error handling 코드 분기 확인
→ findBy 사용 여부 확인
→ screen.debug 확인
→ mock path 확인
```

수정 예:

```tsx
vi.mocked(getFestivals).mockRejectedValue({
  response: {
    status: 500,
    data: {
      message: "Internal Server Error",
    },
  },
});

expect(
  await screen.findByText("서버 오류가 발생했습니다."),
).toBeInTheDocument();
```

권장:

- 실제 코드가 참조하는 error shape와 일치
- 비동기 오류 UI는 findBy 사용
- error mapper 테스트와 연결
- 서버 내부 메시지를 그대로 찾지 않음
- 사용자 메시지를 검증

---

### [FAQ]

Q. mockRejectedValue를 했는데 오류 메시지가 안 보여.
A. error shape가 실제 코드와 다르거나 findBy로 기다리지 않았을 수 있다.

Q. Error UI 테스트에서 getBy를 쓰면 안 돼?
A. API 실패 후 비동기로 표시되는 오류는 findBy를 사용하는 것이 안전하다.

Q. 서버 메시지를 그대로 테스트해야 해?
A. 보통은 사용자에게 표시되는 mapping된 안전한 메시지를 테스트한다.

---

## 8.3 Empty Not Showing

### [개념]

Empty Not Showing은 빈 배열 또는 빈 데이터 응답을 mock했지만 EmptyState가 표시되지 않는 상황이다.

data shape, empty 판단 조건, loading/error 상태 우선순위, query timing을 확인해야 한다.

---

### [핵심]

원인:

- response shape 불일치
- content array 위치 불일치
- empty condition 오류
- loading 상태 유지
- error 상태로 처리됨
- initial data 존재
- queryBy / findBy 선택 오류
- mock path mismatch

---

### [실무]

Debug Flow:

```text
EmptyState 안 보임
→ mock response shape 확인
→ 실제 data path 확인
→ empty 판단 조건 확인
→ loading/error 상태 확인
→ findBy 사용
→ screen.debug 확인
```

배열 응답:

```tsx
vi.mocked(getFestivals).mockResolvedValue([]);
```

Page 응답:

```tsx
vi.mocked(getFestivals).mockResolvedValue({
  content: [],
  page: 0,
  size: 10,
  totalElements: 0,
});
```

주의:

```text
Component가 data.content.length를 확인하는데 mock을 []로 주면
shape 불일치로 EmptyState가 표시되지 않을 수 있음
```

---

### [FAQ]

Q. 빈 배열을 mock했는데 EmptyState가 안 보여.
A. Component가 기대하는 response shape가 배열인지 page object인지 확인해야 한다.

Q. EmptyState는 findBy로 찾아야 해?
A. API 성공 후 비동기로 표시되면 findBy를 사용하는 것이 안전하다.

Q. EmptyState 대신 ErrorState가 나와.
A. mock shape 불일치로 코드가 오류를 내고 있을 수 있다.

---

# 9. UI State Anti Pattern

## 9.1 Common UI State Testing Anti Patterns

### [개념]

UI State Testing Anti Pattern은 Loading, Error, Empty 상태를 실제 사용자 흐름과 다르게 검증하거나 상태 충돌을 놓치는 잘못된 테스트 방식이다.

---

### [핵심]

Anti Pattern:

- success state만 테스트
- loading state 미검증
- error state 미검증
- empty state 미검증
- empty와 error 혼동
- loading 중 empty 표시 방치
- API 호출 여부만 검증
- 실제 API 호출
- error detail 직접 노출 테스트
- mock shape 불일치
- async UI에 getBy 사용
- pending promise 테스트 hang
- retry action 미검증
- accessibility role 누락

---

### [실무]

나쁜 예:

```tsx
test("API를 호출한다", () => {
  render(<FestivalListPage />);

  expect(getFestivals).toHaveBeenCalled();
});
```

좋은 예:

```tsx
test("축제 목록 조회 성공 시 목록을 표시한다", async () => {
  vi.mocked(getFestivals).mockResolvedValue([
    { festivalId: 1, title: "봄꽃 축제" },
  ]);

  render(<FestivalListPage />);

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

나쁜 예:

```tsx
vi.mocked(getFestivals).mockRejectedValue(new Error("Internal Server Error"));

expect(await screen.findByText("Internal Server Error")).toBeInTheDocument();
```

좋은 예:

```tsx
vi.mocked(getFestivals).mockRejectedValue({
  response: {
    status: 500,
  },
});

expect(
  await screen.findByText("서버 오류가 발생했습니다."),
).toBeInTheDocument();
```

---

### [FAQ]

Q. UI State Test에서 가장 흔한 실수는 뭐야?
A. 성공 상태만 테스트하고 Loading, Error, Empty 상태를 놓치는 것이다.

Q. Error message로 서버 내부 문구를 테스트해도 돼?
A. 권장하지 않는다. 사용자에게 표시하는 안전한 메시지를 테스트한다.

Q. API 호출 여부만 확인하면 왜 부족해?
A. 사용자가 실제로 보는 화면 상태가 올바른지 검증하지 못하기 때문이다.

---

# 10. UI State Testing Checklist

## 10.1 Loading Error Empty Checklist

### [개념]

Loading Error Empty Checklist는 화면 상태 테스트가 대기, 실패, 빈 데이터, 성공, 접근성, retry 기준을 만족하는지 확인하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] 초기 Loading State를 검증했는가?
- [ ] Submit Loading State를 검증했는가?
- [ ] loading 중 button disabled를 검증했는가?
- [ ] loading 중 EmptyState가 표시되지 않는지 확인했는가?
- [ ] Success State를 사용자 UI로 검증했는가?
- [ ] Empty Response를 테스트했는가?
- [ ] 검색 결과 없음 상태를 테스트했는가?
- [ ] First Use EmptyState를 테스트했는가?
- [ ] API Error State를 테스트했는가?
- [ ] HTTP status별 주요 Error를 테스트했는가?
- [ ] Network Error를 테스트했는가?
- [ ] Retry Action을 테스트했는가?
- [ ] Error와 Empty를 구분했는가?
- [ ] 비동기 상태는 findBy로 기다렸는가?
- [ ] Loading에는 role status 또는 accessible label이 있는가?
- [ ] Error에는 role alert 또는 명확한 안내가 있는가?
- [ ] EmptyState에는 다음 action이 있는가?
- [ ] 서버 내부 error detail을 노출하지 않는가?
```

---

### [실무]

Agent UI State Test 작성 Flow:

```text
Identify Data Source
→ Mock Loading
→ Mock Success
→ Mock Empty
→ Mock Error
→ Mock Network Error
→ Test Retry
→ Assert User-visible UI
→ Check State Conflict
→ Check Accessibility
```

예:

```text
Festival List Page
→ getFestivals pending
→ loading status 표시
→ getFestivals success
→ festival cards 표시
→ getFestivals empty
→ EmptyState 표시
→ getFestivals 500
→ ErrorState 표시
→ retry success
→ list 회복
```

---

### [FAQ]

Q. Loading Error Empty Checklist의 핵심은 뭐야?
A. Loading, Success, Empty, Error, Retry 상태를 각각 사용자 UI 기준으로 검증하는 것이다.

Q. 상태 테스트를 모두 작성하기 부담되면 뭐부터 해야 해?
A. 핵심 화면의 Loading, Error, Empty, Success를 우선 작성한다.

Q. UI State Test 작성 전 무엇을 정해야 해?
A. API 응답 shape, 상태 우선순위, Error message 정책, Retry action 여부를 정해야 한다.

---

# 11. Part09 Summary

## 11.1 Loading Error Empty Final Rule

### [개념]

Frontend Testing Part09는 Loading, Error, Empty, Success 상태 UI 테스트 기준을 정의한다.

이 Part의 목적은 Agent가 API 상태와 사용자 작업 상태에 따라 올바른 UI를 검증하고, 상태 충돌과 비동기 오류를 방지하게 만드는 것이다.

---

### [핵심]

최종 기준:

- Loading / Error / Empty / Success 상태를 분리해 테스트
- Loading은 pending promise로 안정적으로 검증
- Initial Loading과 Background Refetch 구분
- Submit Loading은 button disabled와 중복 제출 방지 검증
- Error State는 mockRejectedValue와 사용자 메시지로 검증
- HTTP status별 error UX 검증
- Network Error와 Server Error 구분
- Retry Action은 사용자 회복 결과 검증
- EmptyState는 success response의 빈 데이터로 검증
- No Result와 First Use EmptyState 구분
- Success State는 사용자에게 보이는 결과 검증
- 상태 전환은 controlled promise로 검증 가능
- Error / Empty / Loading 충돌 방지
- Loading role status, Error role alert 등 접근성 고려
- 서버 내부 error detail 노출 금지

---

### [실무]

Agent 작업 Flow:

```text
State Test Request
→ Identify UI State
→ Prepare API Mock
→ Pending for Loading
→ Resolve for Success
→ Resolve Empty for EmptyState
→ Reject for ErrorState
→ Test Retry if Provided
→ Assert Accessible UI
→ Check State Priority
→ Review Anti Pattern
```

Part10 이후 연결:

```text
Part09 Loading Error Empty
→ Part10 Router Auth Testing
→ Part11 TanStack Query Testing
→ Part12 Accessibility Testing
→ Part13 Snapshot Test Caution
→ Part14 Test Structure
```

---

### [FAQ]

Q. Part09의 최종 목적은 뭐야?
A. Frontend Agent가 Loading, Error, Empty, Success 상태를 사용자 UI 기준으로 안정적으로 테스트하게 만드는 것이다.

Q. Loading Error Empty에서 가장 중요한 규칙은 뭐야?
A. 각 상태를 API mock으로 분리하고 사용자가 보는 UI 결과를 검증하는 것이다.

Q. Part09 다음에는 어떤 내용이 이어져야 해?
A. Router, Protected Route, Auth State, Login Redirect를 검증하는 Router Auth Testing 기준이 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. UI State Testing은 뭐야?
A. Loading, Error, Empty, Success 같은 화면 상태가 데이터 흐름에 따라 올바르게 표시되는지 검증하는 테스트다.

Q. Loading, Error, Empty 상태를 모두 테스트해야 해?
A. 핵심 화면에서는 테스트하는 것이 좋다. 사용자가 가장 많이 체감하는 실패와 대기 상태이기 때문이다.

Q. Success 상태만 테스트하면 부족해?
A. 부족하다. 실제 서비스에서는 실패, 빈 데이터, 로딩 상태가 자주 발생한다.

Q. Loading과 Empty 중 무엇이 우선이야?
A. 초기 요청 중이면 Loading이 우선이고, 요청 성공 후 데이터가 없을 때 EmptyState를 표시한다.

Q. Error와 Empty는 어떻게 구분해?
A. Error는 요청 실패이고 Empty는 요청 성공 후 데이터가 없는 상태다.

Q. Loading State는 어떻게 테스트해?
A. API mock을 pending 상태로 두고 loading text, spinner, skeleton, disabled 상태를 검증한다.

Q. Loading UI는 어떤 role이 좋아?
A. 사용자에게 로딩 상태를 알리는 경우 `status` role을 사용할 수 있다.

Q. Loading 테스트에서 findBy를 써야 해?
A. 초기 loading이 즉시 표시되면 getBy를 사용할 수 있다. 비동기로 나타나면 findBy를 사용한다.

Q. Initial Loading Test는 왜 필요해?
A. 사용자가 데이터 로딩 중 빈 화면을 보지 않도록 적절한 대기 UI를 제공하는지 확인하기 위해 필요하다.

Q. loading 중 EmptyState가 보이면 안 돼?
A. 일반적으로 요청이 완료되기 전에는 EmptyState를 표시하지 않는 것이 좋다.

Q. skeleton은 어떻게 테스트해?
A. accessible label, status role, loading text 등을 제공하고 해당 요소가 표시되는지 확인한다.

Q. Submit Loading은 왜 테스트해?
A. 중복 제출과 중복 API 요청을 막고 사용자에게 처리 중 상태를 알려주는지 확인하기 위해 필요하다.

Q. 요청 중 버튼은 disabled 되는 게 좋아?
A. 일반적으로 mutation 중복 실행을 막기 위해 disabled 처리하는 것이 좋다.

Q. 중복 클릭 방지는 어떻게 테스트해?
A. 요청 중 버튼을 다시 클릭한 뒤 API 함수가 한 번만 호출되었는지 확인한다.

Q. Background Refetch는 initial loading과 달라?
A. 다르다. initial loading은 데이터가 없고, background refetch는 기존 데이터가 있는 상태에서 다시 요청하는 것이다.

Q. 재조회 중 기존 데이터를 숨겨야 해?
A. 대부분의 UX에서는 기존 데이터를 유지하고 작은 로딩 표시만 제공하는 것이 좋다.

Q. Error State는 어떻게 테스트해?
A. API mock을 실패 상태로 만들고 오류 메시지, alert, retry 버튼, 상태 복구를 검증한다.

Q. 서버 내부 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 안전하고 일반적인 사용자 메시지로 변환해 표시한다.

Q. ErrorState는 EmptyState와 어떻게 달라?
A. ErrorState는 요청 실패이고 EmptyState는 요청 성공 후 데이터가 없는 상태다.

Q. HTTP Status Error Test는 왜 필요해?
A. 상태 코드별로 로그인 필요, 권한 없음, Not Found, 서버 오류 안내가 달라지기 때문이다.

Q. 401과 403은 어떻게 다르게 테스트해?
A. 401은 로그인 필요 또는 redirect, 403은 권한 없음 메시지를 검증한다.

Q. 404 오류는 어떻게 테스트해?
A. API mock을 404로 실패시키고 Not Found 메시지 또는 Not Found 화면을 검증한다.

Q. 500 error는 어떻게 검증해?
A. 서버 내부 상세가 아니라 안전한 fallback message가 표시되는지 확인한다.

Q. Network Error와 500 Error는 달라?
A. 다르다. Network Error는 서버 응답 자체를 받지 못한 상태이고 500은 서버가 오류 응답을 반환한 상태다.

Q. Network Error mock에는 response가 없어도 돼?
A. 그렇다. 실제 네트워크 오류에서는 response가 없을 수 있다.

Q. Network Error UI는 무엇을 보여줘야 해?
A. 네트워크 연결 확인 안내와 다시 시도 버튼이 적합하다.

Q. Retry Action Test는 왜 필요해?
A. 사용자가 오류 상태에서 직접 회복할 수 있는지 검증하기 위해 필요하다.

Q. retry 버튼 클릭 후 무엇을 확인해?
A. API 재요청 후 성공 데이터가 표시되거나 오류 상태가 유지되는지 확인한다.

Q. API 호출 횟수만 확인하면 충분해?
A. 부족할 수 있다. 사용자가 보는 회복 결과를 검증하는 것이 좋다.

Q. Empty State는 뭐야?
A. API 요청은 성공했지만 표시할 데이터가 없을 때 보여주는 안내 UI다.

Q. Empty State는 왜 테스트해야 해?
A. 빈 화면 대신 사용자에게 현재 상태와 다음 행동을 안내하는지 확인하기 위해 필요하다.

Q. No Result Test는 Empty State Test와 같아?
A. 비슷하지만 No Result는 검색이나 필터 조건 때문에 결과가 없는 상태에 초점을 둔다.

Q. 검색 결과 없음 상태에서 무엇을 보여줘야 해?
A. 결과 없음 메시지와 검색어 변경 또는 필터 초기화 action이 좋다.

Q. 필터 초기화 버튼도 테스트해야 해?
A. 제공한다면 클릭 후 필터 값이 초기화되는지 테스트하는 것이 좋다.

Q. First Use Empty State는 뭐야?
A. 사용자가 아직 데이터를 만들거나 활동하지 않아 목록이 비어 있는 정상 상태를 안내하는 UI다.

Q. 검색 결과 없음과 First Use Empty는 달라?
A. 다르다. 검색 결과 없음은 조건에 맞는 결과가 없는 상태이고 First Use Empty는 아직 데이터 자체가 없는 상태다.

Q. Success State는 뭐야?
A. API 요청이나 사용자 작업이 성공했을 때 데이터, 성공 메시지, 이동 결과 등을 표시하는 상태다.

Q. Success Test에서 API 호출 여부만 확인하면 돼?
A. 부족하다. 사용자가 보는 성공 결과를 검증해야 한다.

Q. 성공 메시지는 어떻게 테스트해?
A. 비동기 작업 후 표시되면 `await screen.findByText`로 검증한다.

Q. Mutation Success Test는 뭘 확인해?
A. 생성, 수정, 삭제, 좋아요, 찜하기 성공 후 UI가 올바르게 바뀌는지 확인한다.

Q. invalidateQueries 호출 여부를 테스트해야 해?
A. 보통 직접 호출 여부보다 목록이 갱신되는 사용자 결과를 검증하는 것이 좋다.

Q. 삭제 성공은 어떻게 테스트해?
A. 삭제 후 성공 메시지와 해당 항목이 목록에서 사라졌는지 확인한다.

Q. Loading To Success Test는 언제 필요해?
A. Loading UI가 실제 데이터 표시로 전환되는 흐름을 보장해야 할 때 필요하다.

Q. loading 제거도 확인해야 해?
A. 중요한 화면에서는 확인하는 것이 좋다. loading이 계속 남는 버그를 잡을 수 있다.

Q. controlled promise는 왜 써?
A. 테스트에서 API 응답 시점을 직접 제어해 상태 전환을 안정적으로 검증할 수 있기 때문이다.

Q. Loading To Error Test는 왜 필요해?
A. 요청 실패 시 Loading이 사라지고 사용자에게 오류 안내가 표시되는지 확인하기 위해 필요하다.

Q. reject 이후에는 어떤 Query를 써?
A. 오류 UI가 비동기로 표시되므로 findBy를 사용한다.

Q. Error To Success Retry Test는 뭐야?
A. 첫 요청은 실패하고 다시 시도 후 성공하는 회복 흐름을 검증하는 테스트다.

Q. retry 성공 후 오류 메시지가 사라지는지도 확인해야 해?
A. 중요하다. 성공 데이터와 이전 오류 메시지가 동시에 보이면 혼란스럽다.

Q. Loading 접근성은 왜 테스트해?
A. 보조기술 사용자도 화면이 데이터를 불러오는 중임을 알아야 하기 때문이다.

Q. spinner만 있으면 충분해?
A. 충분하지 않을 수 있다. role status나 aria-label을 제공하는 것이 좋다.

Q. Error 접근성은 왜 테스트해?
A. 오류가 시각 사용자뿐 아니라 보조기술 사용자에게도 전달되어야 하기 때문이다.

Q. role alert는 언제 사용해?
A. 사용자가 즉시 알아야 하는 중요한 오류 메시지에 사용할 수 있다.

Q. EmptyState에도 접근성이 필요해?
A. 필요하다. 사용자는 왜 데이터가 없는지와 다음에 무엇을 할 수 있는지 알아야 한다.

Q. EmptyState action은 어떤 요소가 좋아?
A. 실제 동작에 맞게 button 또는 link를 사용하는 것이 좋다.

Q. Loading UI가 테스트에서 안 보여.
A. API mock이 즉시 resolve되어 loading 상태가 지나갔을 수 있다. pending promise를 사용한다.

Q. mockRejectedValue를 했는데 오류 메시지가 안 보여.
A. error shape가 실제 코드와 다르거나 findBy로 기다리지 않았을 수 있다.

Q. 빈 배열을 mock했는데 EmptyState가 안 보여.
A. Component가 기대하는 response shape가 배열인지 page object인지 확인해야 한다.

Q. UI State Test에서 가장 흔한 실수는 뭐야?
A. 성공 상태만 테스트하고 Loading, Error, Empty 상태를 놓치는 것이다.

Q. Loading Error Empty Checklist의 핵심은 뭐야?
A. Loading, Success, Empty, Error, Retry 상태를 각각 사용자 UI 기준으로 검증하는 것이다.

Q. Part09 Loading Error Empty의 최종 목표는 뭐야?
A. Frontend Agent가 Loading, Error, Empty, Success 상태를 사용자 UI 기준으로 안정적으로 테스트하게 만드는 것이다.
