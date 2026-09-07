# Frontend Testing Part17 - Final Frontend Testing Rules

---

# 1. Final Frontend Testing Overview

## 1.1 Final Rules Definition

### [개념]

Final Frontend Testing Rules는 Frontend Testing 전체 문서의 최종 통합 규칙이다.

이 문서는 Frontend Agent가 테스트 전략, React Testing Library, Query Rules, userEvent, Unit Test, Component Test, Form Test, API Mocking, Loading/Error/Empty, Router/Auth, TanStack Query, Accessibility, Snapshot Caution, Test Structure, Troubleshooting, Review 기준을 하나의 판단 체계로 적용하기 위한 최종 기준이다.

### [핵심]

- Final Frontend Testing Rules
- Frontend Testing Strategy
- React Testing Library
- Query Priority
- userEvent
- Unit Test
- Component Test
- Form Test
- API Mocking
- Loading Error Empty
- Router Auth Testing
- TanStack Query Testing
- Accessibility Testing
- Snapshot Caution
- Test Structure
- Troubleshooting
- Test Review
- Agent Decision Rule

### [실무]

Frontend Agent는 테스트 요청을 받으면 다음 순서로 판단한다.

```text
Test Request
→ Identify Test Target
→ Select Test Level
→ Select Query Strategy
→ Select Interaction Strategy
→ Select Mock Strategy
→ Setup Providers
→ Write User-centered Assertions
→ Add Error/Empty/Loading Cases
→ Check Accessibility
→ Check Isolation
→ Review Anti Patterns
```

최종 원칙:

```text
사용자 관점 테스트가 우선이다.
구현 세부사항 테스트는 지양한다.
role / label 기반 Query를 우선한다.
userEvent로 실제 사용자 행동을 재현한다.
비동기 UI는 findBy로 기다린다.
API는 실제 호출하지 않고 mock한다.
Loading / Error / Empty 상태를 검증한다.
Router/Auth는 Page 결과로 검증한다.
TanStack Query는 새 QueryClient와 retry false를 사용한다.
접근성은 테스트 가능성의 핵심 기준이다.
Snapshot은 보조 수단이다.
테스트는 독립적이고 deterministic 해야 한다.
```

### [FAQ]

Q. Final Frontend Testing Rules는 뭐야?
A. Frontend Testing 전체 문서의 최종 통합 규칙으로, Agent가 테스트를 작성하고 검토할 때 따르는 최종 판단 기준이다.

Q. Frontend Testing에서 가장 중요한 원칙은 뭐야?
A. 사용자가 실제로 보고 행동하는 결과를 검증하는 것이다.

Q. 테스트가 통과하면 충분해?
A. 아니다. 사용자 관점, 접근성, 안정성, 독립성, mock 정확성까지 만족해야 좋은 테스트다.

## 1.2 Final Agent Responsibility

### [개념]

Final Agent Responsibility는 Frontend Agent가 테스트 코드를 작성할 때 반드시 책임져야 하는 범위다.

Agent는 단순히 테스트 코드를 생성하는 것이 아니라 테스트 목적, 테스트 수준, mock 구조, 접근성, 실패 상태, 유지보수성까지 판단해야 한다.

### [핵심]

Agent 책임:

- 테스트 대상 식별
- 테스트 수준 선택
- 사용자 시나리오 정의
- Query 선택
- userEvent 사용
- Provider 구성
- API mock 구성
- mock response shape 검증
- async 대기 처리
- Loading/Error/Empty 검증
- 접근성 검토
- 테스트 독립성 보장
- Anti Pattern 제거
- 리뷰 가능한 테스트 작성

### [실무]

Agent가 해야 하는 것:

```text
테스트 이름을 사용자 시나리오로 작성
필요한 Provider만 구성
실제 API 호출 방지
실제 DTO와 일치하는 mock 작성
사용자 visible result 검증
실패 상태와 edge case 고려
접근성 Query 우선 사용
테스트 간 상태 공유 방지
```

Agent가 피해야 하는 것:

```text
renders / works 같은 이름 사용
getByTestId 우선 사용
container.querySelector 남용
Snapshot-only Test 작성
실제 token 사용
전역 QueryClient 재사용
waitFor 남용
실제 API 호출
mock shape 임의 작성
구현 내부 state 직접 검증
```

### [FAQ]

Q. Frontend Agent는 테스트 코드만 만들면 돼?
A. 아니다. 테스트 목적, mock, Provider, 접근성, 상태 분기, 독립성까지 함께 판단해야 한다.

Q. Agent가 가장 피해야 할 테스트는 뭐야?
A. 사용자 기능을 보장하지 않는 Snapshot-only Test, renders Test, 구현 세부사항 Test다.

Q. Agent가 테스트 작성 전에 먼저 판단할 것은 뭐야?
A. 테스트 대상이 Unit, Component, Integration, Router/Auth, Query 중 어디에 해당하는지 판단해야 한다.

# 2. Final Test Level Decision Rules

## 2.1 Test Level Selection Rule

### [개념]

Test Level Selection Rule은 테스트 대상에 따라 Unit Test, Component Test, Integration Test, E2E Test 중 적절한 수준을 선택하는 규칙이다.

Frontend Agent는 무조건 큰 테스트를 작성하지 않고 테스트 목적에 맞는 최소 수준을 선택해야 한다.

### [핵심]

테스트 수준:

- Unit Test
- Component Test
- Integration Test
- E2E Test
- Pure Function Test
- Page Test
- Flow Test
- User Journey Test

선택 기준:

```text
순수 함수
→ Unit Test

단일 UI Component
→ Component Test

Form interaction
→ Component 또는 Integration Test

API 상태 UI
→ Component/Page Test + API Mock

Router/Auth 흐름
→ Integration Test

여러 Page를 넘나드는 실제 사용자 journey
→ E2E Test
```

### [실무]

판단표:

| 테스트 대상                    | 권장 수준               | 핵심 검증                             |
| ------------------------------ | ----------------------- | ------------------------------------- |
| formatter / mapper / validator | Unit Test               | 입력과 출력                           |
| Button / Modal / Dropdown      | Component Test          | role, interaction, state              |
| LoginForm                      | Component / Integration | input, validation, submit             |
| FestivalListPage               | Page Test               | loading, success, empty, error        |
| ProtectedRoute                 | Integration Test        | auth state, redirect result           |
| TanStack Query mutation        | Component / Integration | pending, success, error, invalidation |
| 결제 전체 흐름                 | E2E Test                | 실제 브라우저 journey                 |

권장:

- 테스트 목적을 먼저 정함
- 가장 작은 수준에서 충분히 검증 가능하면 작은 테스트 선택
- 사용자 흐름이 중요하면 Integration 이상 선택
- 실제 브라우저 동작은 E2E로 분리
- Unit Test로 사용자 Flow를 억지로 검증하지 않음

### [FAQ]

Q. 테스트 수준은 어떻게 정해?
A. 테스트 대상이 순수 로직인지, UI Component인지, 여러 Provider와 Route가 필요한 흐름인지에 따라 정한다.

Q. 모든 것을 Integration Test로 하면 안 돼?
A. 가능은 하지만 느리고 유지보수가 어려워질 수 있다. 목적에 맞는 최소 수준이 좋다.

Q. E2E Test는 언제 필요해?
A. 실제 브라우저에서 여러 Page와 외부 흐름이 연결되는 핵심 사용자 journey에 필요하다.

## 2.2 Unit vs Component Final Rule

### [개념]

Unit vs Component Final Rule은 순수 로직은 Unit Test로, 사용자 UI와 상호작용은 Component Test로 검증하는 기준이다.

Frontend Agent는 DOM이 필요 없는 로직을 Component Test로 끌어올리지 않고, 사용자 UI를 Unit Test로만 끝내지 않는다.

### [핵심]

Unit Test 적합:

- pure function
- formatter
- validator
- mapper
- filter
- sorting
- DTO transformer
- error mapper
- option mapper

Component Test 적합:

- props rendering
- conditional rendering
- user interaction
- form input
- modal open/close
- dropdown select
- loading/error/empty UI
- accessibility role/label

### [실무]

Unit Test 예:

```ts
test("축제 기간을 yyyy.MM.dd 형식으로 변환한다", () => {
  expect(formatFestivalDate("2026-04-01")).toBe("2026.04.01");
});
```

Component Test 예:

```tsx
test("축제 카드는 축제 제목과 지역을 표시한다", () => {
  render(
    <FestivalCard
      festival={{
        festivalId: 1,
        title: "봄꽃 축제",
        regionName: "서울",
      }}
    />,
  );

  expect(screen.getByText("봄꽃 축제")).toBeInTheDocument();
  expect(screen.getByText("서울")).toBeInTheDocument();
});
```

권장:

- 로직은 가능한 순수 함수로 분리해 Unit Test
- UI는 사용자 visible result로 Component Test
- mapper와 Component 테스트를 섞지 않음
- Component 내부 구현 함수 직접 테스트 지양
- 중요한 formatter/validator는 edge case 포함

### [FAQ]

Q. Unit Test와 Component Test를 어떻게 나눠?
A. DOM 없이 입력/출력만 검증하면 Unit Test, 화면과 사용자 행동을 검증하면 Component Test다.

Q. Component 내부 함수를 직접 테스트해도 돼?
A. 지양한다. 내부 함수는 분리해 Unit Test하거나 Component 결과로 검증한다.

Q. validator는 Component Test로만 하면 부족해?
A. 핵심 validator는 Unit Test로 edge case를 검증하고 Form에서는 사용자 오류 메시지를 검증하는 것이 좋다.

# 3. Final Query Rules

## 3.1 Query Priority Final Rule

### [개념]

Query Priority Final Rule은 테스트에서 요소를 찾을 때 사용자 접근성 기준에 가까운 Query를 우선 사용하는 규칙이다.

Frontend Testing의 기본 Query 기준은 React Testing Library의 사용자 관점 철학을 따른다.

### [핵심]

최종 Query 우선순위:

1. `getByRole`
2. `getByLabelText`
3. `getByPlaceholderText`
4. `getByText`
5. `getByDisplayValue`
6. `getByAltText`
7. `getByTitle`
8. `getByTestId`

판단 기준:

```text
button / link / heading / dialog / alert
→ getByRole

input / textarea / select
→ getByLabelText 또는 getByRole name

비동기 등장
→ findByRole / findByText

없음 검증
→ queryByRole / queryByText

최후 수단
→ getByTestId
```

### [실무]

좋은 Query:

```tsx
screen.getByRole("button", { name: "로그인" });
screen.getByLabelText("이메일");
screen.getByRole("heading", { name: "축제 목록", level: 1 });
screen.getByRole("dialog", { name: "삭제 확인" });
screen.getByRole("alert");
```

지양:

```tsx
screen.getByTestId("login-button");
container.querySelector(".login-button");
document.querySelector("#email");
```

권장:

- role/name으로 찾을 수 있게 Component를 개선
- getByTestId는 접근성 정보가 없는 특수 영역에만 사용
- Query 실패를 테스트 수정으로만 해결하지 않음
- Query 자체가 접근성 검증 역할을 함
- Testing Playground로 Query 후보 확인 가능

### [FAQ]

Q. 최종 Query 우선순위는 뭐야?
A. getByRole, getByLabelText, getByPlaceholderText, getByText, getByDisplayValue, getByAltText, getByTitle, getByTestId 순이다.

Q. getByTestId는 언제 써?
A. 사용자 관점 Query로 찾기 어렵고 접근성 의미가 없는 특수 요소에만 최후 수단으로 사용한다.

Q. getByRole이 실패하면?
A. 먼저 semantic HTML과 accessible name이 올바른지 확인한다.

## 3.2 getBy findBy queryBy Final Rule

### [개념]

getBy/findBy/queryBy Final Rule은 요소의 존재 시점과 기대 상태에 따라 Query 계열을 선택하는 규칙이다.

### [핵심]

- getBy
- findBy
- queryBy
- getAllBy
- findAllBy
- queryAllBy
- immediate existence
- async appearance
- absence check
- thrown error
- null return

선택 기준:

| Query      | 사용 상황                 | 실패 동작        |
| ---------- | ------------------------- | ---------------- |
| getBy      | 즉시 있어야 함            | 없으면 throw     |
| findBy     | 비동기로 나타남           | timeout 후 throw |
| queryBy    | 없어야 함                 | 없으면 null      |
| getAllBy   | 여러 개가 즉시 있어야 함  | 없으면 throw     |
| findAllBy  | 여러 개가 비동기로 나타남 | timeout 후 throw |
| queryAllBy | 여러 개가 없거나 0개 가능 | 없으면 []        |

### [실무]

즉시 존재:

```tsx
expect(screen.getByRole("button", { name: "검색" })).toBeInTheDocument();
```

비동기 등장:

```tsx
expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
```

없음 검증:

```tsx
expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
```

여러 항목:

```tsx
expect(await screen.findAllByRole("article")).toHaveLength(3);
```

권장:

- API 응답 후 UI는 findBy 사용
- 사라짐 검증은 queryBy 또는 waitFor 조합
- 없음 검증에 getBy 사용 금지
- findBy를 무조건 쓰지 않고 즉시 UI는 getBy 사용
- Query 선택만으로 테스트 의도가 드러나야 함

### [FAQ]

Q. getBy와 findBy 차이는 뭐야?
A. getBy는 즉시 존재해야 하는 요소, findBy는 비동기로 나타나는 요소에 사용한다.

Q. 없음 검증에는 뭘 써?
A. queryBy를 사용한다.

Q. API 응답 후 표시되는 데이터는 뭘 써?
A. findBy를 사용하는 것이 안전하다.

# 4. Final Interaction Rules

## 4.1 userEvent Final Rule

### [개념]

userEvent Final Rule은 사용자 interaction을 실제 사용자 행동에 가깝게 테스트하기 위해 `userEvent`를 우선 사용하는 규칙이다.

### [핵심]

- userEvent
- userEvent.setup
- await user.click
- await user.type
- await user.clear
- await user.selectOptions
- await user.upload
- await user.keyboard
- await user.tab
- fireEvent caution
- real user interaction

### [실무]

기본 구조:

```tsx
test("검색어를 입력하고 검색하면 검색 결과를 표시한다", async () => {
  const user = userEvent.setup();

  render(<FestivalSearchPage />);

  await user.type(screen.getByLabelText("검색어"), "봄꽃");
  await user.click(screen.getByRole("button", { name: "검색" }));

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

최종 규칙:

```text
interaction이 있으면 userEvent.setup을 test 내부에 생성한다.
userEvent 동작에는 await를 붙인다.
일반 click/type/change는 fireEvent보다 userEvent를 우선한다.
keyboard 흐름은 user.keyboard / user.tab으로 검증한다.
disabled 요소에 상태 변화를 기대하지 않는다.
```

fireEvent 허용:

```text
custom event
low-level event
userEvent가 지원하지 않는 특수 상황
legacy code 테스트
```

### [FAQ]

Q. userEvent는 왜 우선 사용해?
A. 실제 사용자 interaction에 더 가깝고 React 상태 업데이트 흐름도 더 자연스럽게 테스트할 수 있기 때문이다.

Q. userEvent에 항상 await를 붙여?
A. click, type, keyboard, tab 등 interaction에는 await를 붙이는 것이 안전하다.

Q. fireEvent는 쓰면 안 돼?
A. 일반 interaction에는 지양하지만 특수 event에는 사용할 수 있다.

## 4.2 Form Interaction Final Rule

### [개념]

Form Interaction Final Rule은 Form 테스트에서 사용자가 실제로 입력하고 제출하는 흐름을 기준으로 검증하는 규칙이다.

### [핵심]

Form 테스트 대상:

- input typing
- textarea typing
- select option
- checkbox
- radio
- file upload
- validation error
- submit success
- submit loading
- server field error
- global error
- accessibility error

### [실무]

Form 테스트 기본 흐름:

```text
Render Form
→ Fill Inputs
→ Select Options
→ Submit
→ Assert Validation / Success / Error Result
```

예:

```tsx
test("리뷰 내용을 입력하고 등록하면 성공 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(createReview).mockResolvedValue({
    reviewId: 1,
  });

  render(<ReviewForm festivalId={1} />);

  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(await screen.findByText("리뷰가 등록되었습니다.")).toBeInTheDocument();
});
```

권장:

- input은 label로 찾음
- submit button은 role/name으로 찾음
- client validation과 server validation 분리
- submit loading과 disabled 상태 검증
- field error는 aria-invalid / aria-describedby 검토
- 실제 비밀번호나 개인정보 사용 금지

### [FAQ]

Q. Form 테스트에서 가장 중요한 건 뭐야?
A. 사용자가 입력하고 제출했을 때 오류나 성공 결과가 화면에 올바르게 표시되는지 검증하는 것이다.

Q. input value만 확인하면 충분해?
A. 단순 입력 Component는 가능하지만 Form에서는 validation과 submit 결과까지 보는 것이 좋다.

Q. 서버 field error도 테스트해야 해?
A. 중요한 Form에서는 테스트하는 것이 좋다.

# 5. Final Mocking Rules

## 5.1 API Mocking Final Rule

### [개념]

API Mocking Final Rule은 Frontend 테스트에서 실제 Backend 서버를 호출하지 않고 API 성공, 실패, 빈 데이터, 네트워크 오류를 제어하는 규칙이다.

### [핵심]

- API Mocking
- mockResolvedValue
- mockRejectedValue
- Mock Function
- MSW
- Axios Error Shape
- Success Response
- Error Response
- Empty Response
- Network Error
- Actual API Call Forbidden

### [실무]

Module Mock 예:

```tsx
import { getFestivals } from "@/features/festival/api/festivalApi";

vi.mock("@/features/festival/api/festivalApi", () => ({
  getFestivals: vi.fn(),
}));

vi.mocked(getFestivals).mockResolvedValue([
  {
    festivalId: 1,
    title: "봄꽃 축제",
  },
]);
```

Error Mock 예:

```tsx
vi.mocked(getFestivals).mockRejectedValue({
  response: {
    status: 500,
    data: {
      message: "Internal Server Error",
    },
  },
});
```

최종 규칙:

```text
실제 API 호출 금지
mock path는 실제 import path와 일치
mock response shape는 실제 API wrapper 반환값과 일치
error shape는 실제 error handler와 일치
empty response와 error response를 구분
network error는 response 없는 케이스로 테스트 가능
```

### [FAQ]

Q. API Mocking의 최종 원칙은 뭐야?
A. 실제 API 호출 없이 실제 response shape와 error shape를 mock으로 재현하는 것이다.

Q. mock 데이터가 실제 DTO와 조금 달라도 돼?
A. 안 된다. 실제 연동과 다른 테스트가 되어 신뢰도가 낮아진다.

Q. Empty와 Error는 어떻게 구분해?
A. Empty는 성공 응답의 빈 데이터이고 Error는 요청 실패다.

## 5.2 MSW Final Rule

### [개념]

MSW Final Rule은 HTTP 요청 레벨에서 API를 mock할 때 handler, server lifecycle, response shape, override 규칙을 정의한다.

MSW는 API 함수 mock보다 실제 요청 흐름에 가까운 Integration Style Test에 적합하다.

### [핵심]

- MSW
- setupServer
- handlers
- server.listen
- server.resetHandlers
- server.close
- http.get
- http.post
- HttpResponse
- handler override
- unhandled request

### [실무]

기본 구조:

```ts
beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

handler:

```ts
http.get("/api/festivals", () => {
  return HttpResponse.json([
    {
      festivalId: 1,
      title: "봄꽃 축제",
    },
  ]);
});
```

최종 규칙:

```text
handler URL과 실제 request URL 일치
HTTP method 일치
response body는 실제 DTO와 일치
테스트별 error/empty는 server.use로 override
afterEach에서 resetHandlers
unhandled request warning 방치 금지
```

### [FAQ]

Q. MSW는 언제 써?
A. API 함수 mock보다 실제 HTTP 요청 흐름에 가까운 Integration Test를 작성할 때 사용한다.

Q. MSW handler에서 가장 중요한 것은?
A. 실제 요청 URL, method, response shape와 일치하는 것이다.

Q. unhandled request는 무시해도 돼?
A. 권장하지 않는다. handler 누락이나 URL 불일치 신호다.

# 6. Final Async and State Rules

## 6.1 Loading Error Empty Final Rule

### [개념]

Loading Error Empty Final Rule은 서버 상태 UI에서 Loading, Success, Empty, Error 상태를 명확히 분리해 테스트하는 규칙이다.

### [핵심]

상태 구분:

- Loading: 요청 중
- Success: 성공 데이터 표시
- Empty: 성공했지만 데이터 없음
- Error: 요청 실패
- Network Error: 응답 없음
- Retry: 실패 후 재요청
- Submit Loading: mutation 진행 중

### [실무]

상태 테스트 조합:

```text
List Page
→ Loading
→ Success
→ Empty
→ Error
→ Network Error
→ Retry Success
```

Loading:

```tsx
vi.mocked(getFestivals).mockReturnValue(new Promise(() => {}));

render(<FestivalListPage />);

expect(screen.getByRole("status")).toHaveTextContent("불러오는 중입니다.");
```

Empty:

```tsx
vi.mocked(getFestivals).mockResolvedValue([]);

expect(await screen.findByText("표시할 축제가 없습니다.")).toBeInTheDocument();
```

Error:

```tsx
vi.mocked(getFestivals).mockRejectedValue({
  response: {
    status: 500,
  },
});

expect(await screen.findByRole("alert")).toHaveTextContent(
  "서버 오류가 발생했습니다.",
);
```

최종 규칙:

```text
성공 상태만 테스트하지 않는다.
Loading과 Empty를 혼동하지 않는다.
Error와 Empty를 구분한다.
Network Error와 Server Error를 구분할 수 있다.
Retry 버튼이 있으면 회복 결과를 검증한다.
Submit Loading은 button disabled와 중복 요청 방지를 검증한다.
```

### [FAQ]

Q. Loading/Error/Empty 중 무엇이 가장 중요해?
A. 데이터 요청이 핵심인 화면에서는 세 상태 모두 중요하다.

Q. Empty는 Error와 달라?
A. 다르다. Empty는 성공 응답의 빈 데이터이고 Error는 요청 실패다.

Q. Loading 테스트에는 어떤 mock을 써?
A. pending promise를 사용하면 안정적으로 검증할 수 있다.

## 6.2 Async Waiting Final Rule

### [개념]

Async Waiting Final Rule은 비동기 UI 업데이트를 기다릴 때 `findBy`, `waitFor`, `queryBy`를 올바르게 사용하는 규칙이다.

### [핵심]

최종 기준:

```text
요소가 비동기로 나타남
→ findBy

callback 호출을 기다림
→ waitFor

요소가 없어야 함
→ queryBy

요소가 사라짐
→ waitFor + queryBy 또는 waitForElementToBeRemoved

고정 시간 대기
→ 지양
```

### [실무]

좋은 예:

```tsx
expect(await screen.findByText("저장되었습니다.")).toBeInTheDocument();
```

callback:

```tsx
await waitFor(() => {
  expect(onSubmit).toHaveBeenCalledWith(expectedPayload);
});
```

지양:

```tsx
await new Promise((resolve) => setTimeout(resolve, 1000));
```

최종 규칙:

```text
waitFor 안에서 userEvent 실행 금지
findBy로 충분한 경우 waitFor 지양
timeout 증가보다 원인 분석 우선
act warning은 userEvent await와 findBy 대기부터 확인
```

### [FAQ]

Q. 비동기 요소는 무엇으로 기다려?
A. findBy를 사용한다.

Q. waitFor는 언제 써?
A. callback 호출이나 특정 조건 변화를 기다릴 때 사용한다.

Q. setTimeout으로 기다려도 돼?
A. 지양한다. 테스트가 느리고 불안정해진다.

# 7. Final Router Auth Rules

## 7.1 Router Testing Final Rule

### [개념]

Router Testing Final Rule은 React Router 기반 Page 이동, Route Parameter, Query String, Not Found Route를 테스트하는 최종 규칙이다.

### [핵심]

- MemoryRouter
- initialEntries
- Routes
- Route
- Link
- useNavigate
- useParams
- useSearchParams
- NotFound
- Page UI Result

### [실무]

최종 규칙:

```text
Router 테스트는 MemoryRouter 사용
시작 경로는 initialEntries로 지정
useParams 테스트는 Route path와 initialEntry 모두 필요
useNavigate는 호출 여부보다 이동 결과 UI 검증
Link 클릭 후 목적지 Page UI 검증
Query String은 initialEntries에 포함
Not Found Route는 path="*"로 검증
```

예:

```tsx
render(
  <MemoryRouter initialEntries={["/festivals/1"]}>
    <Routes>
      <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
    </Routes>
  </MemoryRouter>,
);
```

검증:

```tsx
expect(
  await screen.findByRole("heading", { name: "봄꽃 축제" }),
).toBeInTheDocument();
```

### [FAQ]

Q. Router Test에서 가장 중요한 설정은 뭐야?
A. MemoryRouter와 initialEntries, 필요한 Route path 구성이다.

Q. URL만 확인하면 충분해?
A. 보통은 부족하다. 이동 후 Page UI 결과를 검증해야 한다.

Q. useParams는 직접 mock해?
A. 일반적으로는 Route path와 initialEntry로 실제 Router 흐름을 재현한다.

## 7.2 Auth Testing Final Rule

### [개념]

Auth Testing Final Rule은 로그인 상태, 비로그인 상태, Auth Loading, Protected Route, Role Based Access, Login/Logout Flow를 검증하는 최종 규칙이다.

### [핵심]

- Auth State
- Auth Loading
- Protected Route
- Login Redirect
- Previous Location
- Logout
- ROLE_USER
- ROLE_ADMIN
- Forbidden
- Login Required
- MockAuthProvider

### [실무]

최종 규칙:

```text
Auth 상태는 MockAuthProvider 또는 render option으로 명확히 주입
실제 token 사용 금지
비로그인과 로그인 case 모두 테스트
authLoading과 unauthenticated 구분
401 Login Required와 403 Forbidden 구분
ROLE_USER / ROLE_ADMIN 실제 권한명 사용
로그인 성공 후 Page 결과 검증
로그아웃 후 보호 Page 접근 차단 검증
```

Protected Route:

```tsx
renderWithProviders(<AppRoutes />, {
  initialEntries: ["/mypage"],
  authenticated: false,
});

expect(screen.getByRole("heading", { name: "로그인" })).toBeInTheDocument();
```

Role:

```tsx
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
```

### [FAQ]

Q. Auth Test에서 실제 token을 써야 해?
A. 아니다. 더미 token 또는 MockAuthProvider 상태를 사용한다.

Q. 401과 403은 어떻게 구분해?
A. 401은 비로그인, 403은 로그인했지만 권한이 부족한 상태다.

Q. Protected Route는 무엇을 검증해야 해?
A. 비로그인 접근 시 로그인 Page, 로그인 접근 시 보호 Page가 표시되는지 검증한다.

# 8. Final TanStack Query Rules

## 8.1 QueryClient Final Rule

### [개념]

QueryClient Final Rule은 TanStack Query 테스트에서 QueryClientProvider와 QueryClient를 안정적으로 구성하는 최종 규칙이다.

### [핵심]

- QueryClient
- QueryClientProvider
- createTestQueryClient
- retry false
- cache isolation
- new client per test
- renderWithQueryClient
- renderWithProviders

### [실무]

최종 설정:

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

최종 규칙:

```text
useQuery/useMutation Component는 QueryClientProvider로 감쌈
테스트마다 새 QueryClient 생성
queries retry false
mutations retry false
전역 QueryClient 재사용 금지
같은 테스트 안의 관련 Component는 같은 QueryClient 공유
테스트 간 Query Cache 공유 금지
```

### [FAQ]

Q. TanStack Query 테스트의 핵심 설정은 뭐야?
A. QueryClientProvider와 테스트마다 새 QueryClient, retry false 설정이다.

Q. QueryClient를 전역으로 재사용해도 돼?
A. 권장하지 않는다. cache 공유로 flaky test가 발생할 수 있다.

Q. retry false는 왜 필요해?
A. 실패 테스트가 느려지거나 불안정해지는 것을 막기 위해 필요하다.

## 8.2 useQuery useMutation Final Rule

### [개념]

useQuery useMutation Final Rule은 서버 상태 조회와 변경 작업을 테스트하는 최종 규칙이다.

### [핵심]

useQuery 테스트:

- loading
- success
- empty
- error
- enabled false
- queryKey change
- refetch

useMutation 테스트:

- pending
- success
- error
- variables
- invalidation result
- optimistic update
- rollback

### [실무]

최종 규칙:

```text
useQuery는 Loading / Success / Empty / Error를 분리 테스트
enabled false는 API 미호출 검증 가능
queryKey 변경은 새 UI 결과로 검증
useMutation은 Pending / Success / Error를 분리 테스트
mutation variables는 request DTO 기준 검증
invalidateQueries 호출보다 UI 갱신 결과 검증
Optimistic Update는 실패 rollback 검증
```

Mutation 예:

```tsx
expect(createReview).toHaveBeenCalledWith({
  festivalId: 1,
  rating: 5,
  content: "좋았어요",
});
```

Invalidation 결과:

```tsx
expect(await screen.findByText("좋았어요")).toBeInTheDocument();
```

### [FAQ]

Q. useQuery는 어떤 상태를 테스트해야 해?
A. Loading, Success, Empty, Error 상태를 우선 테스트한다.

Q. useMutation은 무엇을 테스트해야 해?
A. Pending, Success, Error, variables, mutation 후 UI 갱신을 테스트한다.

Q. invalidateQueries 호출만 확인하면 충분해?
A. 부족하다. 실제 UI가 갱신되는지 검증해야 한다.

# 9. Final Accessibility Rules

## 9.1 Accessibility Final Rule

### [개념]

Accessibility Final Rule은 Frontend 테스트에서 semantic HTML, role, label, accessible name, keyboard, focus, ARIA 상태를 검증하는 최종 규칙이다.

접근성은 테스트 선택 기준이자 Component 품질 기준이다.

### [핵심]

- Semantic HTML
- Accessible Name
- Label
- Keyboard
- Focus
- Dialog
- aria-expanded
- aria-selected
- aria-current
- aria-invalid
- aria-describedby
- role alert
- role status
- Image alt
- axe

### [실무]

최종 규칙:

```text
interactive element는 native button/link/input 우선
button/link는 accessible name 필요
icon button은 aria-label 필요
input은 label과 연결
Form error는 aria-invalid / aria-describedby 연결
Loading은 role status 또는 accessible label 제공
Error는 role alert 또는 명확한 안내 제공
Modal은 dialog role, accessible name, focus trap, focus restore 검증
keyboard 흐름은 user.tab / user.keyboard 사용
ARIA 상태는 시각 상태와 동기화되어야 함
의미 있는 이미지는 alt 제공
장식용 이미지는 alt="" 사용
```

예:

```tsx
expect(screen.getByRole("button", { name: "검색" })).toBeInTheDocument();
expect(screen.getByLabelText("이메일")).toBeInTheDocument();
expect(screen.getByRole("dialog", { name: "삭제 확인" })).toBeInTheDocument();
```

### [FAQ]

Q. 접근성 테스트의 핵심은 뭐야?
A. role, label, accessible name, keyboard, focus로 사용자가 접근 가능한 UI인지 검증하는 것이다.

Q. 접근성 테스트는 axe만 있으면 돼?
A. 아니다. axe는 보조 도구이고 role/label/keyboard/focus 테스트가 필요하다.

Q. 접근성 Query가 실패하면?
A. 테스트를 우회하기보다 Component의 semantic HTML과 accessible name을 개선한다.

## 9.2 Keyboard Focus Final Rule

### [개념]

Keyboard Focus Final Rule은 사용자가 마우스 없이 UI를 조작할 수 있는지, UI 상태 변화 후 focus가 적절히 유지되는지 검증하는 최종 규칙이다.

### [핵심]

- user.tab
- user.keyboard
- toHaveFocus
- Enter
- Space
- Escape
- focus trap
- focus restore
- error focus
- keyboard-only flow

### [실무]

최종 규칙:

```text
Form은 Tab 순서 검증 가능
Modal은 open focus와 close focus restore 검증
Dropdown/Menu는 keyboard open/close 검증
Escape로 overlay 닫힘 검증
오류 발생 시 첫 오류 field 또는 summary focus 검토
disabled 요소는 focus되지 않아야 함
custom interactive element는 keyboard 지원 필요
```

예:

```tsx
await user.tab();
expect(screen.getByLabelText("이메일")).toHaveFocus();

await user.keyboard("{Escape}");
expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
```

### [FAQ]

Q. Keyboard Focus 테스트는 언제 필요해?
A. Form, Modal, Dropdown, Menu, Navigation처럼 조작 흐름이 중요한 UI에서 필요하다.

Q. 모든 Component에 focus 테스트가 필요해?
A. 아니다. 핵심 interactive component를 우선한다.

Q. Modal focus restore는 왜 중요해?
A. 닫힌 후 사용자가 원래 위치를 잃지 않게 하기 위해 중요하다.

# 10. Final Snapshot Rules

## 10.1 Snapshot Final Rule

### [개념]

Snapshot Final Rule은 Snapshot Test를 제한적 보조 수단으로만 사용하는 최종 규칙이다.

Snapshot은 사용자 행동, 접근성, 비동기 상태 테스트를 대체하지 않는다.

### [핵심]

허용 가능:

- small object snapshot
- inline snapshot
- stable config snapshot
- small presentational component snapshot

지양:

- snapshot-only test
- full page snapshot
- large DOM snapshot
- interaction snapshot
- async snapshot
- accessibility snapshot
- className snapshot
- dynamic value snapshot
- unreviewed update

### [실무]

최종 규칙:

```text
Snapshot은 보조 수단
Snapshot-only Test 금지
Behavior Test 우선
큰 DOM Snapshot 지양
동적 값 포함 금지
generated className 중심 Snapshot 지양
Snapshot diff는 반드시 리뷰
민감정보 포함 금지
접근성은 Snapshot이 아니라 role/label/keyboard/focus로 검증
```

좋은 대체:

```tsx
expect(screen.getByRole("heading", { name: "축제 목록" })).toBeInTheDocument();
expect(screen.getByRole("button", { name: "검색" })).toBeInTheDocument();
```

### [FAQ]

Q. Snapshot Test는 아예 쓰면 안 돼?
A. 아니다. 작고 안정적인 구조에는 보조적으로 사용할 수 있다.

Q. Snapshot-only Test는 왜 안 좋아?
A. 사용자 기능이 실제로 보장되는지 알기 어렵기 때문이다.

Q. Snapshot 실패 시 바로 업데이트해도 돼?
A. 아니다. diff를 확인하고 의도된 변경인지 검토해야 한다.

# 11. Final Test Structure Rules

## 11.1 Structure Final Rule

### [개념]

Structure Final Rule은 테스트 파일 위치, naming, render utility, fixture, setup, reset, isolation을 일관되게 구성하는 최종 규칙이다.

### [핵심]

- co-located test
- feature **tests**
- src/test
- renderWithProviders
- fixture
- factory
- setupTests
- mock reset
- test isolation
- deterministic test

### [실무]

최종 구조 예:

```text
src/
├ features/
│ └ festival/
│   ├ components/
│   │ ├ FestivalCard.tsx
│   │ └ FestivalCard.test.tsx
│   └ __tests__/
│     └ FestivalSearchFlow.test.tsx
└ test/
  ├ setupTests.ts
  ├ renderWithProviders.tsx
  ├ createTestQueryClient.ts
  ├ msw/
  └ factories/
```

최종 규칙:

```text
Component 테스트는 대상 파일 근처
Page/Flow 테스트는 feature __tests__
공통 utility는 src/test
파일명은 .test.tsx / .test.ts로 통일
test 이름은 조건/행동/기대 결과 중심
userEvent.setup은 test 내부
QueryClient는 테스트마다 새로 생성
fixture/factory는 실제 API shape와 일치
afterEach에서 mock/storage/MSW reset
테스트는 실행 순서에 의존하지 않음
```

### [FAQ]

Q. 테스트 파일은 어디에 둬?
A. 단일 Component는 대상 파일 근처, Page/Flow 테스트는 feature `__tests__` 폴더가 적합하다.

Q. 공통 테스트 유틸은 어디에 둬?
A. `src/test` 같은 테스트 전용 폴더에 두는 것이 좋다.

Q. 테스트 이름은 어떻게 써?
A. 조건, 사용자 행동, 기대 결과가 드러나도록 쓴다.

## 11.2 Test Isolation Final Rule

### [개념]

Test Isolation Final Rule은 각 테스트가 다른 테스트의 상태와 실행 순서에 영향을 받지 않도록 만드는 최종 규칙이다.

### [핵심]

격리 대상:

- QueryClient cache
- Auth Store
- localStorage
- sessionStorage
- mock call history
- mock implementation
- MSW override handler
- Date mock
- fake timer
- random value

### [실무]

최종 규칙:

```text
테스트마다 필요한 상태를 직접 Arrange
전역 QueryClient 재사용 금지
Auth 상태는 test option으로 주입
localStorage/sessionStorage clear
MSW resetHandlers
vi.clearAllMocks 또는 resetAllMocks
fake timer 사용 후 restore
날짜/랜덤 값 고정
실제 API 호출 금지
```

예:

```ts
afterEach(() => {
  vi.clearAllMocks();
  localStorage.clear();
  sessionStorage.clear();
  server.resetHandlers();
  vi.useRealTimers();
});
```

### [FAQ]

Q. Test Isolation이 왜 중요해?
A. 테스트 순서에 따라 결과가 달라지는 flaky test를 막기 위해 중요하다.

Q. 가장 흔한 공유 상태는 뭐야?
A. QueryClient cache, Auth Store, localStorage, mock call history다.

Q. 테스트가 단독 실행은 되는데 전체 실행에서 실패해.
A. 상태 공유나 reset 누락 가능성이 높다.

# 12. Final Troubleshooting Rules

## 12.1 Troubleshooting Final Decision Rule

### [개념]

Troubleshooting Final Decision Rule은 테스트 실패를 해결할 때 우회하지 않고 원인 기반으로 분석하는 최종 규칙이다.

### [핵심]

점검 순서:

1. 에러 메시지 확인
2. screen.debug 확인
3. Query 선택 확인
4. 비동기 대기 확인
5. userEvent await 확인
6. Provider 확인
7. Mock path 확인
8. Mock response shape 확인
9. Test Isolation 확인
10. jsdom 환경 확인

### [실무]

최종 Debug Flow:

```text
Test Failure
→ Read Error
→ Inspect DOM
→ Check Query
→ Check Async
→ Check Provider
→ Check Mock
→ Check State Isolation
→ Check Environment
→ Fix Root Cause
→ Remove Anti Pattern
```

우회 금지:

```text
getByRole 실패 → 바로 testId 사용 금지
findBy timeout → 바로 timeout 증가 금지
act warning → 무조건 act로 감싸기 금지
Snapshot 실패 → 무검토 update 금지
CI 실패 → rerun만 반복 금지
```

### [FAQ]

Q. 테스트 실패 시 최종 점검 순서는 뭐야?
A. 에러, DOM, Query, Async, Provider, Mock, Isolation, Environment 순서로 본다.

Q. timeout을 늘리면 해결돼?
A. 대부분 근본 해결이 아니다. mock, async, retry, pending promise를 먼저 확인한다.

Q. testId로 바꾸면 빠르게 해결되지 않아?
A. 접근성 문제를 숨길 수 있으므로 최후 수단으로만 사용한다.

# 13. Final Review Rules

## 13.1 Test Review Final Rule

### [개념]

Test Review Final Rule은 작성된 테스트가 좋은 테스트인지 최종 검수하는 기준이다.

테스트는 통과 여부보다 사용자에게 중요한 동작을 의미 있게 보장하는지가 중요하다.

### [핵심]

리뷰 기준:

- test name clarity
- user scenario
- user-visible assertion
- Query priority
- userEvent usage
- async correctness
- mock shape correctness
- provider correctness
- test isolation
- accessibility
- security data
- maintainability
- risk based coverage

### [실무]

최종 리뷰 Checklist:

```md
- [ ] 테스트 이름이 조건/행동/기대 결과를 설명하는가?
- [ ] 사용자 visible result를 검증하는가?
- [ ] role/label 기반 Query를 우선 사용하는가?
- [ ] userEvent와 await를 사용하는가?
- [ ] 비동기 UI에 findBy를 사용하는가?
- [ ] Loading/Error/Empty 상태를 고려했는가?
- [ ] API mock shape가 실제와 일치하는가?
- [ ] Provider 구성이 적절한가?
- [ ] QueryClient가 테스트마다 독립적인가?
- [ ] 테스트 간 상태 공유가 없는가?
- [ ] 접근성 기준을 고려했는가?
- [ ] Snapshot-only Test가 아닌가?
- [ ] 실제 token/secret/개인정보가 없는가?
- [ ] 실패했을 때 원인을 이해하기 쉬운가?
```

리뷰 등급:

```text
A급
→ 사용자 시나리오 명확, assertion 강함, mock 안정, 접근성 고려, 독립적

B급
→ 핵심은 검증하지만 일부 상태나 접근성 보완 필요

C급
→ 통과는 하지만 약한 assertion, 구현 세부사항 의존, 불안정성 존재

D급
→ 목적 불명확, snapshot-only, 실제 API 의존, mock shape 불일치
```

### [FAQ]

Q. 좋은 테스트의 최종 기준은 뭐야?
A. 사용자에게 중요한 동작을 명확하고 안정적으로 검증하며 실패 원인을 이해하기 쉬운 테스트다.

Q. 커버리지가 높으면 좋은 테스트야?
A. 항상 그렇지는 않다. 의미 있는 사용자 시나리오를 검증해야 한다.

Q. 테스트 리뷰에서 가장 중요한 것은?
A. 테스트가 통과하는지가 아니라 실제 사용자 기능을 보장하는지 확인하는 것이다.

# 14. Final Anti Pattern Rules

## 14.1 Global Anti Pattern Rule

### [개념]

Global Anti Pattern Rule은 Frontend Testing 전체에서 반드시 피해야 하는 잘못된 패턴을 통합한 규칙이다.

### [핵심]

금지 또는 지양 패턴:

- renders / works 테스트
- Snapshot-only Test
- 실제 API 호출
- 실제 token 사용
- getByTestId 우선 사용
- container.querySelector 남용
- className 기반 테스트
- implementation detail test
- 내부 state 직접 검증
- useNavigate mock만 검증
- API 호출 여부만 검증
- waitFor 남용
- waitFor 안에서 userEvent 실행
- userEvent await 누락
- 전역 QueryClient 재사용
- 테스트 간 Auth/Storage 공유
- mock response shape 불일치
- Error와 Empty 혼동
- Loading 상태 누락
- 접근성 문제를 테스트로 우회
- Snapshot diff 무검토 update

### [실무]

나쁜 테스트 특징:

```text
테스트 이름이 모호함
사용자 결과가 없음
구현 내부만 확인함
실제 API에 의존함
비동기 대기를 운에 맡김
통과는 하지만 회귀 방지 가치가 낮음
```

좋은 테스트 특징:

```text
사용자 시나리오가 명확함
role/label Query 사용
userEvent로 행동
findBy로 비동기 결과 대기
mock이 실제 shape와 일치
Provider와 cache가 격리됨
실패 시 원인을 알 수 있음
```

### [FAQ]

Q. Frontend Testing 전체에서 가장 위험한 Anti Pattern은 뭐야?
A. 사용자 결과를 검증하지 않는 Snapshot-only Test와 실제 API 호출에 의존하는 테스트다.

Q. 구현 세부사항 테스트는 왜 위험해?
A. 사용자는 문제가 없는데 테스트가 깨지거나, 실제 사용자 문제를 놓칠 수 있기 때문이다.

Q. Anti Pattern을 발견하면 어떻게 해?
A. 사용자 시나리오, role/label Query, userEvent, visible assertion 중심으로 수정한다.

# 15. Final Agent Workflow

## 15.1 Test Generation Workflow

### [개념]

Test Generation Workflow는 Frontend Agent가 테스트 코드를 생성할 때 따라야 하는 최종 작업 순서다.

### [핵심]

Workflow:

```text
1. 테스트 대상 식별
2. 테스트 목적 정의
3. 테스트 수준 선택
4. 필요한 Provider 확인
5. API Mock 방식 선택
6. 사용자 시나리오 작성
7. role/label Query 선택
8. userEvent interaction 작성
9. async 대기 작성
10. 사용자 결과 assertion 작성
11. 실패/빈/로딩 상태 추가
12. 접근성 검토
13. 테스트 독립성 확인
14. Anti Pattern 제거
15. 최종 리뷰
```

### [실무]

Agent Prompt 내부 판단 예:

```text
대상: LoginForm
수준: Component / Integration
Provider: Auth optional, Router if redirect
Mock: login API mock
시나리오:
- 입력창 렌더링
- 필수값 오류
- 로그인 성공
- 로그인 실패
- submit loading
접근성:
- email/password label
- error alert
- button disabled
```

테스트 생성 기준:

```text
작게 시작한다.
핵심 사용자 흐름을 먼저 테스트한다.
실패 상태를 추가한다.
접근성 Query를 우선한다.
중복은 utility로 줄이되 의도를 숨기지 않는다.
```

### [FAQ]

Q. Agent가 테스트 생성 시 가장 먼저 할 일은?
A. 테스트 대상과 목적, 테스트 수준을 식별하는 것이다.

Q. 테스트는 성공 case부터 쓰면 돼?
A. 일반적으로 성공 case를 먼저 쓰고 중요한 validation/error/loading case를 추가한다.

Q. Agent가 모든 case를 다 써야 해?
A. 핵심 사용자 흐름과 위험도가 높은 실패 상태를 우선 작성한다.

## 15.2 Test Fix Workflow

### [개념]

Test Fix Workflow는 실패하는 테스트를 Agent가 수정할 때 따르는 최종 작업 순서다.

### [핵심]

Workflow:

```text
1. 실패 메시지 읽기
2. 실패한 Query/Assertion 확인
3. 현재 DOM 확인
4. 비동기 여부 확인
5. Provider 누락 확인
6. Mock 적용 여부 확인
7. Mock shape 확인
8. 상태 공유 확인
9. 환경 API 확인
10. 최소 수정 적용
11. Anti Pattern 여부 확인
```

### [실무]

수정 원칙:

```text
테스트를 약하게 만들지 않는다.
사용자 관점 Query를 유지한다.
Component 접근성 문제가 있으면 Component 개선을 제안한다.
mock shape가 틀렸으면 실제 DTO에 맞춘다.
timeout 증가보다 원인을 해결한다.
Snapshot 업데이트로 실패를 덮지 않는다.
```

좋은 수정:

```text
getByText 실패
→ 실제로 alert role이 있으므로 findByRole("alert")로 변경

findBy timeout
→ mock response shape를 실제 data.content 구조에 맞춤

No QueryClient set
→ renderWithQueryClient 적용

getByRole button 실패
→ icon button에 aria-label 추가
```

### [FAQ]

Q. 실패 테스트를 고칠 때 가장 중요한 원칙은?
A. 테스트를 약하게 만들지 않고 원인을 해결하는 것이다.

Q. getByRole 실패를 testId로 바꿔도 돼?
A. 최후 수단이다. 먼저 접근성 구조를 개선해야 한다.

Q. timeout이 나면 어떻게 고쳐?
A. mock, Provider, async 대기, retry, pending promise를 확인한다.

# 16. Final Checklist

## 16.1 Final Frontend Testing Checklist

### [개념]

Final Frontend Testing Checklist는 Frontend Agent가 테스트 작성, 수정, 리뷰 전에 확인해야 하는 최종 체크리스트다.

### [핵심]

Checklist:

```md
- [ ] 테스트 대상과 수준이 명확한가?
- [ ] 테스트 이름이 조건/행동/기대 결과를 설명하는가?
- [ ] 사용자 visible result를 검증하는가?
- [ ] getByRole / getByLabelText를 우선 사용하는가?
- [ ] getByTestId를 불필요하게 사용하지 않았는가?
- [ ] userEvent.setup을 test 내부에서 생성했는가?
- [ ] userEvent에 await를 붙였는가?
- [ ] 비동기 UI에는 findBy를 사용하는가?
- [ ] waitFor를 남용하지 않는가?
- [ ] 실제 API 호출을 하지 않는가?
- [ ] API mock path가 실제 import path와 일치하는가?
- [ ] mock response shape가 실제 API와 일치하는가?
- [ ] error response shape가 실제 error handler와 일치하는가?
- [ ] Loading 상태를 검증했는가?
- [ ] Success 상태를 검증했는가?
- [ ] Empty 상태를 검증했는가?
- [ ] Error 상태를 검증했는가?
- [ ] Retry가 있으면 회복 결과를 검증했는가?
- [ ] Form validation과 server error를 구분했는가?
- [ ] Router 테스트에 MemoryRouter와 initialEntries가 있는가?
- [ ] Auth 상태를 명확히 주입했는가?
- [ ] 401과 403을 구분했는가?
- [ ] QueryClientProvider가 필요한 곳에 있는가?
- [ ] QueryClient를 테스트마다 새로 생성했는가?
- [ ] retry false를 설정했는가?
- [ ] mutation variables를 실제 DTO 기준으로 검증했는가?
- [ ] invalidate 결과를 UI 갱신으로 검증했는가?
- [ ] 접근성 role/name/label을 고려했는가?
- [ ] keyboard/focus가 중요한 UI를 테스트했는가?
- [ ] Snapshot-only Test가 아닌가?
- [ ] 테스트 간 상태 공유가 없는가?
- [ ] localStorage/sessionStorage/mock/MSW가 reset되는가?
- [ ] 날짜/랜덤/타이머 의존이 제어되는가?
- [ ] 실제 token/secret/개인정보가 없는가?
- [ ] 실패했을 때 원인을 이해하기 쉬운가?
```

### [실무]

Agent 최종 검수 Flow:

```text
Generated Test
→ Run Final Checklist
→ Remove Anti Pattern
→ Strengthen User Assertion
→ Check Mock Shape
→ Check Provider Isolation
→ Check Accessibility
→ Check Security Data
→ Finalize
```

### [FAQ]

Q. Final Checklist의 핵심은 뭐야?
A. 사용자 결과, 접근성 Query, async 처리, mock 정확성, Provider 격리, 보안 데이터를 최종 확인하는 것이다.

Q. 모든 항목을 항상 만족해야 해?
A. 테스트 유형에 따라 다르지만 핵심 원칙인 사용자 결과, 안정성, 독립성은 반드시 지켜야 한다.

Q. Checklist가 너무 길면 어떻게 써?
A. Agent 내부 검수 기준으로 사용하고, 테스트 유형에 맞는 항목을 우선 적용한다.

# 17. Part17 Summary

## 17.1 Final Frontend Testing Rules Summary

### [개념]

Frontend Testing Part17은 Frontend Testing 전체 문서의 최종 통합본이다.

이 Part의 목적은 Agent가 Frontend 테스트를 작성, 수정, 리뷰할 때 모든 세부 문서를 하나의 판단 체계로 연결해 적용하게 만드는 것이다.

### [핵심]

최종 통합 규칙:

- 테스트는 사용자 관점이 우선이다.
- 테스트는 구현 세부사항보다 사용자 결과를 검증한다.
- Query는 getByRole / getByLabelText 우선이다.
- userEvent로 실제 사용자 행동을 재현한다.
- 비동기 UI는 findBy로 기다린다.
- API는 실제 호출하지 않고 mock한다.
- mock response shape는 실제 API와 일치해야 한다.
- Loading / Error / Empty / Success 상태를 구분한다.
- Router는 MemoryRouter와 Page UI 결과로 테스트한다.
- Auth는 로그인/비로그인/권한 부족을 구분한다.
- TanStack Query는 새 QueryClient와 retry false를 사용한다.
- Mutation은 pending/success/error/variables/invalidation 결과를 검증한다.
- 접근성은 role/name/label/keyboard/focus 기준으로 검증한다.
- Snapshot은 보조 수단이며 Snapshot-only Test는 금지한다.
- 테스트 구조는 일관되고 독립적이어야 한다.
- 테스트 데이터에는 실제 token/secret/개인정보를 사용하지 않는다.
- Troubleshooting은 원인 기반으로 수행한다.
- Review는 통과 여부보다 의미 있는 사용자 보장 여부를 본다.

### [실무]

Frontend Agent 최종 판단 Flow:

```text
Frontend Test Task
→ Apply Strategy Rules
→ Apply Query Rules
→ Apply userEvent Rules
→ Apply Test Level Rules
→ Apply Mocking Rules
→ Apply State Rules
→ Apply Router/Auth Rules
→ Apply TanStack Query Rules
→ Apply Accessibility Rules
→ Apply Structure Rules
→ Apply Troubleshooting Rules
→ Apply Review Rules
→ Final Output
```

최종 산출물 기준:

```text
읽으면 사용자 시나리오가 보이는 테스트
실패하면 원인을 추적할 수 있는 테스트
실제 API shape와 맞는 테스트
접근 가능한 UI를 유도하는 테스트
테스트 간 독립적인 테스트
Agent가 신뢰하고 재사용할 수 있는 테스트
```

### [FAQ]

Q. Part17의 최종 목적은 뭐야?
A. Frontend Testing 전체 기준을 하나로 통합해 Agent가 테스트 작성, 수정, 리뷰에 일관되게 적용하도록 하는 것이다.

Q. Frontend Testing 전체에서 가장 중요한 한 문장은 뭐야?
A. 사용자가 실제로 보고 행동하는 결과를 안정적으로 검증하라.

Q. 이 문서 이후 Frontend Agent는 무엇을 해야 해?
A. 테스트 요청마다 이 최종 규칙을 기준으로 테스트 수준, Query, mock, Provider, 접근성, 상태 검증을 선택해야 한다.

# Retrieval Queries

### [FAQ]

Q. Final Frontend Testing Rules는 뭐야?
A. Frontend Testing 전체 문서의 최종 통합 규칙으로, Agent가 테스트를 작성하고 검토할 때 따르는 최종 판단 기준이다.

Q. Frontend Testing에서 가장 중요한 원칙은 뭐야?
A. 사용자가 실제로 보고 행동하는 결과를 검증하는 것이다.

Q. 테스트가 통과하면 충분해?
A. 아니다. 사용자 관점, 접근성, 안정성, 독립성, mock 정확성까지 만족해야 좋은 테스트다.

Q. Frontend Agent는 테스트 코드만 만들면 돼?
A. 아니다. 테스트 목적, mock, Provider, 접근성, 상태 분기, 독립성까지 함께 판단해야 한다.

Q. Agent가 테스트 작성 전에 먼저 판단할 것은 뭐야?
A. 테스트 대상이 Unit, Component, Integration, Router/Auth, Query 중 어디에 해당하는지 판단해야 한다.

Q. 테스트 수준은 어떻게 정해?
A. 테스트 대상이 순수 로직인지, UI Component인지, 여러 Provider와 Route가 필요한 흐름인지에 따라 정한다.

Q. 모든 것을 Integration Test로 하면 안 돼?
A. 가능은 하지만 느리고 유지보수가 어려워질 수 있다. 목적에 맞는 최소 수준이 좋다.

Q. Unit Test와 Component Test를 어떻게 나눠?
A. DOM 없이 입력/출력만 검증하면 Unit Test, 화면과 사용자 행동을 검증하면 Component Test다.

Q. Component 내부 함수를 직접 테스트해도 돼?
A. 지양한다. 내부 함수는 분리해 Unit Test하거나 Component 결과로 검증한다.

Q. 최종 Query 우선순위는 뭐야?
A. getByRole, getByLabelText, getByPlaceholderText, getByText, getByDisplayValue, getByAltText, getByTitle, getByTestId 순이다.

Q. getByTestId는 언제 써?
A. 사용자 관점 Query로 찾기 어렵고 접근성 의미가 없는 특수 요소에만 최후 수단으로 사용한다.

Q. getByRole이 실패하면?
A. 먼저 semantic HTML과 accessible name이 올바른지 확인한다.

Q. getBy와 findBy 차이는 뭐야?
A. getBy는 즉시 존재해야 하는 요소, findBy는 비동기로 나타나는 요소에 사용한다.

Q. 없음 검증에는 뭘 써?
A. queryBy를 사용한다.

Q. API 응답 후 표시되는 데이터는 뭘 써?
A. findBy를 사용하는 것이 안전하다.

Q. userEvent는 왜 우선 사용해?
A. 실제 사용자 interaction에 더 가깝고 React 상태 업데이트 흐름도 더 자연스럽게 테스트할 수 있기 때문이다.

Q. userEvent에 항상 await를 붙여?
A. click, type, keyboard, tab 등 interaction에는 await를 붙이는 것이 안전하다.

Q. fireEvent는 쓰면 안 돼?
A. 일반 interaction에는 지양하지만 특수 event에는 사용할 수 있다.

Q. Form 테스트에서 가장 중요한 건 뭐야?
A. 사용자가 입력하고 제출했을 때 오류나 성공 결과가 화면에 올바르게 표시되는지 검증하는 것이다.

Q. input value만 확인하면 충분해?
A. 단순 입력 Component는 가능하지만 Form에서는 validation과 submit 결과까지 보는 것이 좋다.

Q. API Mocking의 최종 원칙은 뭐야?
A. 실제 API 호출 없이 실제 response shape와 error shape를 mock으로 재현하는 것이다.

Q. mock 데이터가 실제 DTO와 조금 달라도 돼?
A. 안 된다. 실제 연동과 다른 테스트가 되어 신뢰도가 낮아진다.

Q. Empty와 Error는 어떻게 구분해?
A. Empty는 성공 응답의 빈 데이터이고 Error는 요청 실패다.

Q. MSW는 언제 써?
A. API 함수 mock보다 실제 HTTP 요청 흐름에 가까운 Integration Test를 작성할 때 사용한다.

Q. unhandled request는 무시해도 돼?
A. 권장하지 않는다. handler 누락이나 URL 불일치 신호다.

Q. Loading/Error/Empty 중 무엇이 가장 중요해?
A. 데이터 요청이 핵심인 화면에서는 세 상태 모두 중요하다.

Q. Loading 테스트에는 어떤 mock을 써?
A. pending promise를 사용하면 안정적으로 검증할 수 있다.

Q. 비동기 요소는 무엇으로 기다려?
A. findBy를 사용한다.

Q. waitFor는 언제 써?
A. callback 호출이나 특정 조건 변화를 기다릴 때 사용한다.

Q. setTimeout으로 기다려도 돼?
A. 지양한다. 테스트가 느리고 불안정해진다.

Q. Router Test에서 가장 중요한 설정은 뭐야?
A. MemoryRouter와 initialEntries, 필요한 Route path 구성이다.

Q. useParams는 직접 mock해?
A. 일반적으로는 Route path와 initialEntry로 실제 Router 흐름을 재현한다.

Q. Auth Test에서 실제 token을 써야 해?
A. 아니다. 더미 token 또는 MockAuthProvider 상태를 사용한다.

Q. 401과 403은 어떻게 구분해?
A. 401은 비로그인, 403은 로그인했지만 권한이 부족한 상태다.

Q. Protected Route는 무엇을 검증해야 해?
A. 비로그인 접근 시 로그인 Page, 로그인 접근 시 보호 Page가 표시되는지 검증한다.

Q. TanStack Query 테스트의 핵심 설정은 뭐야?
A. QueryClientProvider와 테스트마다 새 QueryClient, retry false 설정이다.

Q. QueryClient를 전역으로 재사용해도 돼?
A. 권장하지 않는다. cache 공유로 flaky test가 발생할 수 있다.

Q. useQuery는 어떤 상태를 테스트해야 해?
A. Loading, Success, Empty, Error 상태를 우선 테스트한다.

Q. useMutation은 무엇을 테스트해야 해?
A. Pending, Success, Error, variables, mutation 후 UI 갱신을 테스트한다.

Q. invalidateQueries 호출만 확인하면 충분해?
A. 부족하다. 실제 UI가 갱신되는지 검증해야 한다.

Q. 접근성 테스트의 핵심은 뭐야?
A. role, label, accessible name, keyboard, focus로 사용자가 접근 가능한 UI인지 검증하는 것이다.

Q. 접근성 테스트는 axe만 있으면 돼?
A. 아니다. axe는 보조 도구이고 role/label/keyboard/focus 테스트가 필요하다.

Q. Keyboard Focus 테스트는 언제 필요해?
A. Form, Modal, Dropdown, Menu, Navigation처럼 조작 흐름이 중요한 UI에서 필요하다.

Q. Snapshot Test는 아예 쓰면 안 돼?
A. 아니다. 작고 안정적인 구조에는 보조적으로 사용할 수 있다.

Q. Snapshot-only Test는 왜 안 좋아?
A. 사용자 기능이 실제로 보장되는지 알기 어렵기 때문이다.

Q. 테스트 파일은 어디에 둬?
A. 단일 Component는 대상 파일 근처, Page/Flow 테스트는 feature `__tests__` 폴더가 적합하다.

Q. 테스트 이름은 어떻게 써?
A. 조건, 사용자 행동, 기대 결과가 드러나도록 쓴다.

Q. Test Isolation이 왜 중요해?
A. 테스트 순서에 따라 결과가 달라지는 flaky test를 막기 위해 중요하다.

Q. 가장 흔한 공유 상태는 뭐야?
A. QueryClient cache, Auth Store, localStorage, mock call history다.

Q. 테스트 실패 시 최종 점검 순서는 뭐야?
A. 에러, DOM, Query, Async, Provider, Mock, Isolation, Environment 순서로 본다.

Q. timeout을 늘리면 해결돼?
A. 대부분 근본 해결이 아니다. mock, async, retry, pending promise를 먼저 확인한다.

Q. 좋은 테스트의 최종 기준은 뭐야?
A. 사용자에게 중요한 동작을 명확하고 안정적으로 검증하며 실패 원인을 이해하기 쉬운 테스트다.

Q. 커버리지가 높으면 좋은 테스트야?
A. 항상 그렇지는 않다. 의미 있는 사용자 시나리오를 검증해야 한다.

Q. Frontend Testing 전체에서 가장 위험한 Anti Pattern은 뭐야?
A. 사용자 결과를 검증하지 않는 Snapshot-only Test와 실제 API 호출에 의존하는 테스트다.

Q. Agent가 테스트 생성 시 가장 먼저 할 일은?
A. 테스트 대상과 목적, 테스트 수준을 식별하는 것이다.

Q. 실패 테스트를 고칠 때 가장 중요한 원칙은?
A. 테스트를 약하게 만들지 않고 원인을 해결하는 것이다.

Q. Final Checklist의 핵심은 뭐야?
A. 사용자 결과, 접근성 Query, async 처리, mock 정확성, Provider 격리, 보안 데이터를 최종 확인하는 것이다.

Q. Part17 Final Frontend Testing Rules의 최종 목표는 뭐야?
A. Frontend Testing 전체 기준을 하나로 통합해 Agent가 테스트 작성, 수정, 리뷰에 일관되게 적용하도록 하는 것이다.
