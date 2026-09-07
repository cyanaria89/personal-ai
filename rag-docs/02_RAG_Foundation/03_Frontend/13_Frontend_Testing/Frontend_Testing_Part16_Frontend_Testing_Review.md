# Frontend Testing Part16 - Frontend Testing Review

---

# 1. Frontend Testing Review Overview

## 1.1 Frontend Testing Review Definition

### [개념]

Frontend Testing Review는 작성된 테스트 코드가 실제 사용자 관점, 접근성, 비동기 상태, Mock 안정성, 유지보수성 기준을 만족하는지 검토하는 과정이다.

테스트가 단순히 통과하는지 확인하는 것이 아니라 좋은 테스트인지, 의미 있는 회귀를 잡을 수 있는지, Agent가 신뢰할 수 있는 코드로 판단해도 되는지 확인한다.

### [핵심]

- Frontend Testing Review
- Test Code Review
- Test Quality
- User-centric Test
- Behavior Test
- Accessibility Review
- Mock Review
- Async Review
- Provider Review
- Test Isolation Review
- Maintainability Review
- Anti Pattern Review
- Coverage Caution
- Review Checklist

### [실무]

Frontend 테스트 리뷰 기본 흐름:

```text
테스트 목적 확인
→ 사용자 시나리오 확인
→ Query 전략 확인
→ userEvent 흐름 확인
→ async 대기 확인
→ Mock shape 확인
→ Provider 구성 확인
→ 테스트 독립성 확인
→ 유지보수성 확인
→ Anti Pattern 제거
```

좋은 테스트 리뷰 기준:

```text
테스트 이름만 보고 목적을 알 수 있음
사용자 행동과 화면 결과를 검증함
role / label 기반 Query를 우선 사용함
Loading / Error / Empty 상태를 고려함
Mock 데이터가 실제 API shape와 일치함
테스트 간 상태가 공유되지 않음
실패했을 때 원인을 이해하기 쉬움
```

나쁜 테스트 리뷰 신호:

```text
테스트가 통과하지만 무엇을 보장하는지 불명확함
구현 세부사항을 과도하게 검증함
Snapshot만 존재함
실제 API를 호출함
waitFor를 남용함
getByTestId가 기본 Query로 사용됨
Mock 데이터가 실제 DTO와 다름
테스트 순서에 따라 결과가 달라짐
```

### [FAQ]

Q. Frontend Testing Review는 뭐야?
A. 테스트 코드가 사용자 관점, 접근성, 안정성, 유지보수성 기준을 만족하는지 검토하는 과정이다.

Q. 테스트가 통과하면 리뷰가 필요 없어?
A. 아니다. 통과하는 테스트라도 의미가 약하거나 불안정하면 좋은 테스트가 아니다.

Q. 테스트 리뷰에서 가장 먼저 볼 것은 뭐야?
A. 테스트 이름과 목적이 사용자 시나리오와 기대 결과를 명확히 설명하는지 확인한다.

## 1.2 Review Scope

### [개념]

Review Scope는 Frontend 테스트 리뷰에서 어떤 항목을 검토할지 정하는 범위다.

테스트 실행 결과뿐 아니라 테스트의 의도, 사용자 관점, 접근성, Mock, 비동기 처리, 구조, 보안 데이터까지 포함한다.

### [핵심]

포함 범위:

- test name
- test purpose
- user scenario
- query strategy
- userEvent usage
- async handling
- accessibility assertion
- API mock shape
- error mock shape
- Provider setup
- QueryClient isolation
- Router setup
- Auth state setup
- fixture quality
- test independence
- security data
- anti pattern

제외 또는 별도 영역:

- 실제 Backend 통합 품질
- 실제 브라우저 시각 회귀
- E2E 전체 journey 품질
- 성능 측정 전체
- 디자인 QA 전체
- 수동 접근성 인증

### [실무]

Review 대상별 관점:

```text
Unit Test
→ 입력/출력, edge case, pure logic 검증

Component Test
→ props, conditional rendering, interaction, accessibility 검증

Form Test
→ input, validation, submit, field error, server error 검증

API State Test
→ loading, success, empty, error, retry 검증

Router Auth Test
→ route result, protected route, role access, redirect 검증

TanStack Query Test
→ provider, retry false, cache isolation, mutation result 검증
```

권장:

- 테스트 종류에 맞는 리뷰 기준 적용
- 모든 테스트에 같은 체크리스트를 기계적으로 적용하지 않음
- 핵심 사용자 흐름과 실패 상태를 우선 검토
- 커버리지 수치보다 테스트 품질 우선

### [FAQ]

Q. 테스트 리뷰는 무엇까지 봐야 해?
A. 이름, 사용자 시나리오, Query, async, Mock, Provider, 독립성, 보안 데이터를 함께 본다.

Q. 모든 테스트에 같은 기준을 적용해야 해?
A. 아니다. Unit, Component, Integration, Router, Query 테스트마다 중점이 다르다.

Q. 커버리지 수치도 리뷰 대상이야?
A. 참고 대상이지만 품질을 대체하지는 못한다.

# 2. Test Purpose Review

## 2.1 Test Name Review

### [개념]

Test Name Review는 테스트 이름이 조건, 사용자 행동, 기대 결과를 명확히 설명하는지 확인하는 리뷰다.

좋은 테스트 이름은 실패했을 때 어떤 기능이 깨졌는지 바로 알려준다.

### [핵심]

검토 대상:

- condition
- user action
- expected result
- domain term
- user scenario
- readable name
- no vague name
- no implementation-only name

좋은 이름:

```text
이메일을 입력하지 않고 로그인하면 이메일 오류 메시지를 표시한다
비로그인 사용자가 마이페이지에 접근하면 로그인 Page를 표시한다
리뷰 등록 성공 후 리뷰 목록에 새 리뷰를 표시한다
검색 결과가 없으면 검색 결과 없음 메시지를 표시한다
```

나쁜 이름:

```text
renders
works
test login
click button
state true
component test
```

### [실무]

리뷰 질문:

```md
- [ ] 테스트 이름만 보고 테스트 목적을 알 수 있는가?
- [ ] 조건이 드러나는가?
- [ ] 사용자의 행동이 드러나는가?
- [ ] 기대 결과가 드러나는가?
- [ ] 구현 세부사항보다 사용자 결과를 설명하는가?
```

수정 전:

```tsx
test("works", async () => {});
```

수정 후:

```tsx
test("비밀번호가 틀리면 로그인 오류 메시지를 표시한다", async () => {});
```

권장:

- 한글 test name 사용 가능
- user scenario 중심 naming
- 너무 긴 이름은 핵심 조건과 결과만 남김
- 테스트 이름과 실제 assertion이 일치해야 함

### [FAQ]

Q. Test Name Review의 핵심은 뭐야?
A. 테스트 이름만 보고 조건, 행동, 기대 결과를 이해할 수 있어야 한다.

Q. 테스트 이름이 길어도 돼?
A. 길어도 명확하면 괜찮지만 불필요한 구현 설명은 줄이는 것이 좋다.

Q. renders 같은 이름은 왜 안 좋아?
A. 무엇이 렌더링되어야 하는지 알 수 없어 실패 원인을 파악하기 어렵다.

## 2.2 Assertion Purpose Review

### [개념]

Assertion Purpose Review는 테스트의 assertion이 테스트 이름과 목적에 맞는 결과를 검증하는지 확인하는 리뷰다.

테스트 이름은 사용자 결과를 말하지만 assertion은 내부 함수 호출만 확인하는 불일치를 방지한다.

### [핵심]

검토 대상:

- assertion matches test name
- user-visible result
- meaningful assertion
- no weak assertion
- no unrelated assertion
- no implementation-only assertion
- callback assertion caution
- DOM result assertion

### [실무]

문제:

```tsx
test("로그인 성공 시 마이페이지를 표시한다", async () => {
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(login).toHaveBeenCalled();
});
```

이 테스트는 이름과 assertion이 맞지 않는다.

개선:

```tsx
test("로그인 성공 시 마이페이지를 표시한다", async () => {
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(
    await screen.findByRole("heading", { name: "마이페이지" }),
  ).toBeInTheDocument();
});
```

리뷰 질문:

```md
- [ ] assertion이 테스트 이름의 기대 결과를 직접 검증하는가?
- [ ] 사용자에게 보이는 결과를 검증하는가?
- [ ] API 호출 여부만 확인하고 끝나지 않는가?
- [ ] callback 검증이 실제 목적에 필요한가?
- [ ] 관련 없는 assertion이 섞이지 않았는가?
```

권장:

- 테스트 이름과 assertion 일치
- 사용자 결과 우선
- callback은 보조적으로 사용
- 하나의 테스트에는 하나의 핵심 목적
- 불필요한 assertion 제거

### [FAQ]

Q. Assertion Purpose Review는 왜 필요해?
A. 테스트 이름과 실제 검증 내용이 다르면 테스트가 통과해도 기대 기능을 보장하지 못하기 때문이다.

Q. API 호출 여부만 확인하면 부족해?
A. 대부분 부족하다. API 결과로 사용자에게 보이는 UI를 검증해야 한다.

Q. callback assertion은 쓰면 안 돼?
A. 필요한 경우 사용할 수 있지만 사용자 visible result를 대체하지는 않아야 한다.

# 3. User Perspective Review

## 3.1 User-centric Query Review

### [개념]

User-centric Query Review는 테스트가 사용자가 인식하는 방식으로 요소를 찾는지 확인하는 리뷰다.

React Testing Library에서는 `getByRole`, `getByLabelText`, `findByRole`, `queryByRole` 같은 접근성 기반 Query가 우선이다.

### [핵심]

Query 우선순위:

1. getByRole
2. getByLabelText
3. getByPlaceholderText
4. getByText
5. getByDisplayValue
6. getByAltText
7. getByTitle
8. getByTestId

검토 대상:

- role query
- accessible name
- label query
- alt text
- testId last resort
- implementation detail query
- class selector
- container query

### [실무]

나쁜 예:

```tsx
screen.getByTestId("submit-button");
```

좋은 예:

```tsx
screen.getByRole("button", { name: "로그인" });
```

나쁜 예:

```tsx
container.querySelector(".error-message");
```

좋은 예:

```tsx
screen.getByRole("alert");
```

리뷰 질문:

```md
- [ ] getByRole을 사용할 수 있는데 testId를 사용하지 않았는가?
- [ ] input은 label로 찾는가?
- [ ] button/link는 role과 name으로 찾는가?
- [ ] error/loading 상태는 alert/status role을 고려했는가?
- [ ] className이나 DOM 구조에 의존하지 않는가?
```

권장:

- Query 실패 시 접근성 구조 개선 우선
- testId는 최후 수단
- role/name 기반 Query로 테스트 가능하도록 Component 개선
- container.querySelector 지양
- accessible name이 불명확하면 UI 문구 개선 검토

### [FAQ]

Q. User-centric Query Review는 뭐야?
A. 테스트가 사용자가 인식하는 role, label, name 기준으로 요소를 찾는지 검토하는 것이다.

Q. getByTestId는 쓰면 안 돼?
A. 최후 수단으로는 가능하지만 기본 Query로 사용하면 접근성 문제를 숨길 수 있다.

Q. className으로 요소를 찾으면 왜 안 좋아?
A. 사용자 관점이 아니라 구현 세부사항에 의존해 테스트가 쉽게 깨진다.

## 3.2 User Event Review

### [개념]

User Event Review는 테스트가 실제 사용자 행동에 가깝게 interaction을 실행하는지 확인하는 리뷰다.

클릭, 입력, 선택, 키보드 조작은 `userEvent`를 우선 사용하고 `await`를 붙인다.

### [핵심]

검토 대상:

- userEvent.setup
- user.click
- user.type
- user.clear
- user.selectOptions
- user.upload
- user.keyboard
- user.tab
- await userEvent
- fireEvent caution
- real user flow

### [실무]

나쁜 예:

```tsx
fireEvent.change(screen.getByLabelText("이메일"), {
  target: {
    value: "test@example.com",
  },
});
```

좋은 예:

```tsx
await user.type(screen.getByLabelText("이메일"), "test@example.com");
```

나쁜 예:

```tsx
user.click(screen.getByRole("button", { name: "저장" }));
```

좋은 예:

```tsx
await user.click(screen.getByRole("button", { name: "저장" }));
```

리뷰 질문:

```md
- [ ] interaction test에서 userEvent.setup을 test 내부에 생성했는가?
- [ ] userEvent에 await를 붙였는가?
- [ ] fireEvent를 일반 클릭/입력에 남용하지 않았는가?
- [ ] 실제 사용자 흐름과 같은 순서로 행동하는가?
- [ ] disabled/readOnly 요소에 부적절한 interaction을 기대하지 않는가?
```

권장:

- interaction은 userEvent 우선
- fireEvent는 특수 event에 제한
- userEvent는 test마다 생성
- 사용자 행동 순서를 생략하지 않음
- Form 제출은 입력 → 클릭/Enter 순서로 테스트

### [FAQ]

Q. User Event Review의 핵심은 뭐야?
A. 테스트가 실제 사용자 행동에 가깝게 userEvent로 interaction을 실행하는지 확인하는 것이다.

Q. fireEvent는 쓰면 안 돼?
A. 특수 event나 userEvent가 지원하지 않는 상황에서는 가능하지만 일반 클릭/입력은 userEvent가 우선이다.

Q. userEvent에 await를 안 붙이면?
A. 상태 업데이트를 기다리지 못해 act warning이나 flaky test가 발생할 수 있다.

# 4. Async Review

## 4.1 Async Query Review

### [개념]

Async Query Review는 비동기 UI를 올바른 Query와 대기 방식으로 검증하는지 확인하는 리뷰다.

API 응답 후 표시되는 UI는 `findBy`, 사라지는 UI는 `waitForElementToBeRemoved` 또는 `waitFor`, 즉시 없는 상태는 `queryBy`를 사용한다.

### [핵심]

검토 대상:

- getBy vs findBy
- queryBy for absence
- waitFor usage
- waitForElementToBeRemoved
- async UI
- API response
- loading state
- error state
- mutation success
- retry result

### [실무]

나쁜 예:

```tsx
expect(screen.getByText("봄꽃 축제")).toBeInTheDocument();
```

API 응답 후 표시된다면:

```tsx
expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
```

사라짐 검증:

```tsx
await waitFor(() => {
  expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
});
```

callback 대기:

```tsx
await waitFor(() => {
  expect(onSubmit).toHaveBeenCalledWith(expectedPayload);
});
```

리뷰 질문:

```md
- [ ] 비동기 등장 요소에 findBy를 사용했는가?
- [ ] 없음 검증에 queryBy를 사용했는가?
- [ ] waitFor가 필요한 곳에만 사용되었는가?
- [ ] waitFor 안에서 userEvent를 실행하지 않는가?
- [ ] 고정 시간 sleep을 사용하지 않는가?
```

권장:

- 비동기 UI는 findBy 우선
- waitFor 남용 금지
- waitFor 안에서는 assertion만 수행
- setTimeout 기반 대기 지양
- loading → success/error 전환은 controlled promise 고려

### [FAQ]

Q. Async Query Review는 뭐야?
A. 비동기 UI에 getBy/findBy/queryBy/waitFor를 올바르게 사용하는지 검토하는 것이다.

Q. API 결과를 getBy로 찾으면 안 돼?
A. API 응답 후 비동기로 나타나는 UI는 findBy가 안전하다.

Q. waitFor는 언제 쓰는 게 좋아?
A. callback 호출이나 특정 조건 변화처럼 findBy로 표현하기 어려운 경우에 사용한다.

## 4.2 Loading Error Empty Review

### [개념]

Loading Error Empty Review는 서버 상태를 사용하는 화면이 Loading, Success, Empty, Error 상태를 균형 있게 테스트하는지 확인하는 리뷰다.

성공 상태만 테스트하면 실제 서비스에서 중요한 실패 경험을 놓칠 수 있다.

### [핵심]

검토 대상:

- loading state
- success state
- empty state
- error state
- network error
- retry action
- submit loading
- disabled state
- state priority
- no state conflict

### [실무]

리뷰 질문:

```md
- [ ] 초기 Loading 상태를 테스트했는가?
- [ ] 성공 데이터를 표시하는가?
- [ ] 빈 데이터 응답 시 EmptyState를 표시하는가?
- [ ] API 실패 시 ErrorState를 표시하는가?
- [ ] Network Error와 Server Error를 구분하는가?
- [ ] Retry 버튼이 있으면 동작을 테스트했는가?
- [ ] Loading 중 EmptyState가 먼저 표시되지 않는가?
- [ ] Submit 중 버튼 disabled를 테스트했는가?
```

좋은 상태 테스트 조합:

```text
FestivalListPage
→ Loading
→ Success with festivals
→ Empty with []
→ 500 Error
→ Network Error
→ Retry Success
```

Form 상태 테스트 조합:

```text
ReviewForm
→ Client Validation Error
→ Submit Loading
→ Submit Success
→ Server Field Error
→ Server Global Error
```

권장:

- 핵심 Page는 Loading/Error/Empty 테스트 포함
- 모든 작은 Component에 과도하게 상태 테스트를 요구하지 않음
- 상태 우선순위 충돌 확인
- Error와 Empty 구분
- 사용자 메시지 기준 검증

### [FAQ]

Q. Loading Error Empty Review는 왜 필요해?
A. 성공 상태만으로는 실제 사용자가 겪는 대기, 실패, 빈 데이터 상황을 보장할 수 없기 때문이다.

Q. 모든 화면에 Loading/Error/Empty 테스트가 필요해?
A. 데이터 요청이 핵심인 화면에는 필요하고, 작은 정적 Component에는 필요하지 않을 수 있다.

Q. Error와 Empty를 구분해야 해?
A. 반드시 구분해야 한다. Error는 요청 실패이고 Empty는 성공 응답의 빈 데이터다.

# 5. Mock Review

## 5.1 API Mock Review

### [개념]

API Mock Review는 테스트에서 사용하는 API mock이 실제 API 함수, response shape, error shape와 일치하는지 확인하는 리뷰다.

Mock이 실제와 다르면 테스트는 통과해도 실제 서비스는 실패할 수 있다.

### [핵심]

검토 대상:

- mock path
- import path
- named export
- default export
- mockResolvedValue
- mockRejectedValue
- response shape
- error shape
- fieldErrors
- pagination shape
- actual API call prevention

### [실무]

리뷰 질문:

```md
- [ ] vi.mock 경로가 실제 import 경로와 일치하는가?
- [ ] API 함수가 실제로 mock function인가?
- [ ] mockResolvedValue shape가 API wrapper 반환값과 일치하는가?
- [ ] error.response.status 구조가 실제 error handler와 일치하는가?
- [ ] fieldErrors key가 실제 field name과 일치하는가?
- [ ] Page/Slice 응답 구조가 실제와 일치하는가?
- [ ] 실제 API 호출 가능성이 없는가?
```

좋은 mock:

```tsx
vi.mocked(getFestivals).mockResolvedValue([
  {
    festivalId: 1,
    title: "봄꽃 축제",
    regionName: "서울",
    imageUrl: null,
  },
]);
```

나쁜 mock:

```tsx
vi.mocked(getFestivals).mockResolvedValue([
  {
    id: 1,
    name: "축제",
  },
]);
```

권장:

- 실제 Backend DTO 기준 mock
- API wrapper 반환 shape 확인
- error shape는 error mapper 기준
- pagination 응답 구조 구분
- mock이 복잡하면 factory 사용

### [FAQ]

Q. API Mock Review의 핵심은 뭐야?
A. mock 경로와 response/error shape가 실제 코드와 일치하는지 확인하는 것이다.

Q. mock이 실제 API와 조금 달라도 테스트만 통과하면 괜찮아?
A. 아니다. 실제 연동에서 깨질 수 있으므로 mock shape를 실제와 맞춰야 한다.

Q. fieldErrors key도 리뷰해야 해?
A. 해야 한다. field error mapping은 key가 다르면 작동하지 않는다.

## 5.2 Fixture and Factory Review

### [개념]

Fixture and Factory Review는 테스트 데이터가 작고 명확하며 실제 API shape와 일치하고 보안상 안전한지 확인하는 리뷰다.

### [핵심]

검토 대상:

- fixture size
- factory default
- override clarity
- DTO consistency
- null field
- enum value
- date format
- no secret
- no personal data
- readability

### [실무]

리뷰 질문:

```md
- [ ] fixture가 테스트에 필요한 만큼만 작은가?
- [ ] factory 기본값이 정상 케이스인가?
- [ ] override 값이 테스트 의도를 명확히 드러내는가?
- [ ] field 이름과 타입이 실제 API와 일치하는가?
- [ ] null 가능 field를 고려했는가?
- [ ] enum 값이 실제 값과 일치하는가?
- [ ] 실제 token, email, 개인정보가 없는가?
```

좋은 factory:

```ts
createFestivalResponse({
  title: "음악 축제",
  regionName: "부산",
});
```

나쁜 fixture:

```ts
const hugeFestivalFixture = {
  ...수십 개의 테스트와 무관한 필드
};
```

권장:

- 테스트 의도에 필요한 데이터만 사용
- 반복 데이터는 factory 사용
- 실제 개인정보 금지
- default는 정상 케이스
- edge case는 override로 표현

### [FAQ]

Q. Fixture Review에서 가장 중요한 건 뭐야?
A. 실제 API shape와 일치하면서 테스트 의도를 흐리지 않을 만큼 작아야 한다는 것이다.

Q. 큰 fixture는 왜 안 좋아?
A. 테스트가 무엇을 검증하는지 흐리고 유지보수 비용이 커진다.

Q. factory override는 왜 좋아?
A. 기본 데이터는 유지하면서 테스트별 차이를 명확히 드러낼 수 있다.

## 5.3 MSW Review

### [개념]

MSW Review는 handler URL, method, response shape, resetHandlers, unhandled request 정책이 적절한지 확인하는 리뷰다.

MSW는 실제 HTTP 요청 흐름에 가까운 테스트에서 사용하므로 handler 정확성이 중요하다.

### [핵심]

검토 대상:

- handler URL
- HTTP method
- baseURL
- query params
- path params
- response status
- response json
- server.listen
- server.resetHandlers
- server.close
- unhandled request

### [실무]

리뷰 질문:

```md
- [ ] handler URL이 실제 요청 URL과 일치하는가?
- [ ] HTTP method가 일치하는가?
- [ ] response status가 명확한가?
- [ ] response body가 실제 DTO와 일치하는가?
- [ ] 테스트별 override 후 resetHandlers가 실행되는가?
- [ ] unhandled request warning을 방치하지 않는가?
- [ ] query param을 handler 내부에서 올바르게 읽는가?
```

좋은 handler:

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

error override:

```ts
server.use(
  http.get("/api/festivals", () => {
    return HttpResponse.json(
      { message: "Internal Server Error" },
      { status: 500 },
    );
  }),
);
```

권장:

- domain별 handler 관리
- 기본 handler는 정상 케이스
- error/empty는 테스트별 override
- resetHandlers 필수
- unhandled request를 실패로 취급하는 정책 검토

### [FAQ]

Q. MSW Review의 핵심은 뭐야?
A. handler URL/method/response가 실제 요청과 일치하고 테스트별 override가 격리되는지 확인하는 것이다.

Q. unhandled request warning은 리뷰에서 어떻게 봐?
A. mock 누락이나 URL 불일치 신호이므로 방치하면 안 된다.

Q. MSW response도 실제 DTO와 맞아야 해?
A. 맞아야 한다. 그래야 실제 HTTP 흐름에 가까운 테스트가 된다.

# 6. Provider and Environment Review

## 6.1 Provider Setup Review

### [개념]

Provider Setup Review는 테스트 대상이 필요한 Router, QueryClient, Auth, Theme, i18n Provider를 적절히 감싸고 있는지 확인하는 리뷰다.

Provider가 부족하면 테스트가 실패하고, Provider가 과도하면 테스트 의도가 흐려진다.

### [핵심]

검토 대상:

- MemoryRouter
- QueryClientProvider
- AuthProvider
- ThemeProvider
- i18n Provider
- renderWithProviders
- minimal provider
- provider order
- initialEntries
- auth state
- query client

### [실무]

리뷰 질문:

```md
- [ ] Router Hook을 쓰는 Component에 MemoryRouter가 있는가?
- [ ] useQuery/useMutation Component에 QueryClientProvider가 있는가?
- [ ] Auth 상태가 필요한 Component에 AuthProvider가 있는가?
- [ ] QueryClient는 테스트마다 새로 생성되는가?
- [ ] Router initialEntries가 테스트 목적과 맞는가?
- [ ] Auth 상태가 test option으로 명확히 주입되는가?
- [ ] 필요 없는 Provider를 과도하게 감싸지 않았는가?
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

나쁜 예:

```tsx
render(<MyPage />);
```

`MyPage`가 Router, Auth, Query를 모두 필요로 한다면 실패하거나 실제 사용 조건과 다르다.

권장:

- 필요한 Provider만 사용
- render utility 목적별 분리
- provider order 명확화
- QueryClient 전역 재사용 금지
- Auth state를 storage에 의존하지 않음

### [FAQ]

Q. Provider Setup Review의 핵심은 뭐야?
A. 테스트 대상이 실제 동작에 필요한 Provider를 갖고 있고, 불필요한 Provider로 테스트 의도를 숨기지 않는지 확인하는 것이다.

Q. 모든 Provider를 항상 감싸면 편하지 않아?
A. 편하지만 테스트가 무거워지고 어떤 의존성이 필요한지 숨겨질 수 있다.

Q. QueryClient는 왜 매번 새로 만들어야 해?
A. cache가 테스트 간 공유되어 flaky test가 생기는 것을 막기 위해서다.

## 6.2 Environment Setup Review

### [개념]

Environment Setup Review는 jsdom, setupTests, global mock, custom matcher, browser API mock이 테스트 요구사항에 맞게 구성되어 있는지 확인하는 리뷰다.

### [핵심]

검토 대상:

- jsdom environment
- setupTests
- jest-dom
- custom matcher
- matchMedia mock
- ResizeObserver mock
- IntersectionObserver mock
- scrollTo mock
- createObjectURL mock
- cleanup
- fake timer restore

### [실무]

리뷰 질문:

```md
- [ ] 테스트 환경이 jsdom으로 설정되어 있는가?
- [ ] jest-dom matcher가 등록되어 있는가?
- [ ] MSW server lifecycle이 setup에 있는가?
- [ ] 필요한 browser API mock이 있는가?
- [ ] global mock이 과도하지 않은가?
- [ ] fake timer 사용 후 restore하는가?
- [ ] setupTests에 domain-specific mock을 과도하게 넣지 않았는가?
```

좋은 setup:

```ts
import "@testing-library/jest-dom/vitest";
import { server } from "@/test/msw/server";

beforeAll(() => server.listen());

afterEach(() => {
  server.resetHandlers();
  vi.clearAllMocks();
});

afterAll(() => server.close());
```

권장:

- setupTests는 공통 환경만 담당
- domain mock은 각 테스트나 handler에 배치
- browser API mock은 필요한 것만 추가
- 실제 layout 계산이 필요한 테스트는 E2E/visual로 분리
- global mock 변경은 전체 테스트 영향 검토

### [FAQ]

Q. Environment Setup Review는 왜 필요해?
A. 테스트 환경 설정이 잘못되면 많은 테스트가 불안정하거나 실제 브라우저와 다른 결과를 낼 수 있기 때문이다.

Q. setupTests에는 모든 mock을 넣으면 돼?
A. 아니다. 공통 환경만 넣고 domain-specific mock은 테스트 가까이에 둔다.

Q. jsdom 한계는 리뷰에서 어떻게 봐?
A. layout, scroll, media 같은 실제 브라우저 의존 기능은 단위 테스트 대신 E2E/visual 테스트로 보강할지 판단한다.

# 7. Test Isolation Review

## 7.1 Independent Test Review

### [개념]

Independent Test Review는 각 테스트가 다른 테스트의 실행 결과나 순서에 의존하지 않는지 확인하는 리뷰다.

테스트 독립성은 안정적인 테스트 스위트의 핵심이다.

### [핵심]

검토 대상:

- no shared state
- mock reset
- storage clear
- QueryClient isolation
- Auth Store reset
- MSW resetHandlers
- fake timer restore
- Date mock restore
- independent setup
- deterministic data

### [실무]

리뷰 질문:

```md
- [ ] 테스트마다 필요한 상태를 직접 준비하는가?
- [ ] 전역 변수에 테스트 상태를 저장하지 않는가?
- [ ] QueryClient가 테스트 간 공유되지 않는가?
- [ ] localStorage/sessionStorage가 테스트 후 정리되는가?
- [ ] mock call history가 clear되는가?
- [ ] MSW override handler가 reset되는가?
- [ ] Date/fake timer mock이 restore되는가?
- [ ] 테스트 순서를 바꿔도 통과하는가?
```

나쁜 예:

```tsx
let loggedIn = false;

test("로그인한다", () => {
  loggedIn = true;
});

test("마이페이지를 본다", () => {
  expect(loggedIn).toBe(true);
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

권장:

- 각 test가 독립적으로 Arrange 수행
- 전역 상태 공유 금지
- setup은 공통 환경만 제공
- 테스트 순서 의존 발견 시 즉시 구조 개선
- CI 병렬 실행 가능성을 고려

### [FAQ]

Q. Independent Test Review는 왜 중요해?
A. 테스트 순서와 실행 환경에 따라 결과가 달라지는 문제를 막기 위해 중요하다.

Q. 로그인 상태를 테스트 간 공유해도 돼?
A. 안 된다. 각 테스트에서 인증 상태를 직접 준비해야 한다.

Q. 테스트 독립성은 어떻게 확인해?
A. 단독 실행과 전체 실행, 순서 변경 실행에서 같은 결과가 나오는지 확인한다.

## 7.2 Deterministic Review

### [개념]

Deterministic Review는 테스트가 날짜, 랜덤, 네트워크, 타이머, locale 같은 외부 요인에 의존하지 않고 항상 같은 결과를 내는지 확인하는 리뷰다.

### [핵심]

검토 대상:

- fixed input
- fixed date
- fixed random
- no real network
- no real timer wait
- stable sorting
- timezone caution
- locale caution
- deterministic fixture
- repeatable test

### [실무]

리뷰 질문:

```md
- [ ] 현재 날짜에 의존하지 않는가?
- [ ] Math.random / randomUUID 결과에 의존하지 않는가?
- [ ] 실제 API나 외부 서비스 상태에 의존하지 않는가?
- [ ] setTimeout 실제 대기를 사용하지 않는가?
- [ ] 정렬 순서가 안정적인가?
- [ ] timezone / locale에 따라 expected가 달라지지 않는가?
- [ ] 테스트 입력이 고정되어 있는가?
```

나쁜 예:

```ts
expect(formatDate(new Date())).toBe("2026.07.06");
```

좋은 예:

```ts
expect(formatDate("2026-07-06")).toBe("2026.07.06");
```

권장:

- 날짜는 고정 입력 사용
- 랜덤 값은 주입 또는 mock
- 실제 네트워크 금지
- 타이머는 fake timer 또는 로직 분리
- locale/timezone 의존 결과는 명시적으로 처리

### [FAQ]

Q. Deterministic Review는 뭐야?
A. 테스트가 언제 어디서 실행되어도 같은 결과를 내는지 확인하는 리뷰다.

Q. 날짜 테스트는 어떻게 안정화해?
A. 현재 날짜 대신 고정 날짜 입력을 사용하거나 시스템 시간을 mock한다.

Q. 랜덤 id가 필요한 테스트는?
A. id 생성 함수를 mock하거나 주입해 고정 값을 사용한다.

# 8. Accessibility Review

## 8.1 Accessibility Assertion Review

### [개념]

Accessibility Assertion Review는 테스트가 role, accessible name, label, aria state, keyboard, focus 같은 접근성 기준을 검증하는지 확인하는 리뷰다.

접근성은 테스트 가능성과 사용자 경험을 동시에 개선한다.

### [핵심]

검토 대상:

- getByRole
- accessible name
- getByLabelText
- role alert
- role status
- aria-invalid
- aria-describedby
- aria-expanded
- aria-selected
- aria-current
- keyboard navigation
- focus management
- axe

### [실무]

리뷰 질문:

```md
- [ ] 버튼/링크는 role과 accessible name으로 찾는가?
- [ ] input은 label과 연결되어 있는가?
- [ ] icon button은 aria-label이 있는가?
- [ ] error message는 role alert 또는 field 연결이 있는가?
- [ ] loading state는 role status 또는 accessible label이 있는가?
- [ ] Modal은 dialog role과 accessible name이 있는가?
- [ ] keyboard 조작이 중요한 UI는 user.tab/user.keyboard 테스트가 있는가?
- [ ] aria state가 시각 상태와 일치하는가?
```

좋은 예:

```tsx
expect(screen.getByRole("button", { name: "검색" })).toBeInTheDocument();
expect(screen.getByLabelText("이메일")).toBeInTheDocument();
expect(screen.getByRole("dialog", { name: "삭제 확인" })).toBeInTheDocument();
```

권장:

- getByTestId보다 role/label 우선
- 접근성 assertion은 구현 세부사항이 아니라 사용자 접근성 검증
- Modal/Form/Navigation은 접근성 리뷰 우선순위 높음
- axe는 보조 도구
- 접근성 문제를 테스트 수정으로 숨기지 않음

### [FAQ]

Q. Accessibility Assertion Review는 왜 필요해?
A. 테스트가 사용자 관점뿐 아니라 보조기술 사용자 관점에서도 UI를 검증하도록 하기 위해 필요하다.

Q. aria 속성을 모두 테스트해야 해?
A. 아니다. 사용자 상태 전달에 중요한 aria 속성을 우선 테스트한다.

Q. axe가 있으면 role/label 테스트는 없어도 돼?
A. 아니다. axe는 보조 도구이고 role/label/keyboard 테스트가 필요하다.

## 8.2 Keyboard and Focus Review

### [개념]

Keyboard and Focus Review는 사용자가 마우스 없이 주요 UI를 조작할 수 있고, 상태 변화 후 focus가 적절히 이동하는지 검토하는 리뷰다.

### [핵심]

검토 대상:

- user.tab
- user.keyboard
- toHaveFocus
- Enter
- Space
- Escape
- focus trap
- focus restore
- initial focus
- error focus
- keyboard-only flow

### [실무]

리뷰 질문:

```md
- [ ] Form은 Tab 순서로 자연스럽게 이동하는가?
- [ ] 주요 action은 Enter/Space로 실행 가능한가?
- [ ] Modal이 열리면 focus가 내부로 이동하는가?
- [ ] Modal을 닫으면 trigger로 focus가 돌아가는가?
- [ ] Escape로 overlay를 닫을 수 있는가?
- [ ] 오류 발생 시 첫 오류 field 또는 summary로 focus가 이동하는가?
- [ ] custom interactive element가 keyboard로 동작하는가?
```

좋은 예:

```tsx
await user.tab();
expect(screen.getByLabelText("이메일")).toHaveFocus();

await user.keyboard("{Escape}");
expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
```

권장:

- Form, Modal, Dropdown, Navigation 우선 리뷰
- custom component는 keyboard 접근성 확인
- focus trap은 E2E 보강 가능
- disabled/hidden 요소 focus 여부 확인
- keyboard 테스트가 없으면 수동 검수라도 명시

### [FAQ]

Q. Keyboard and Focus Review는 언제 중요해?
A. Form, Modal, Dropdown, Menu, Navigation처럼 조작 흐름이 중요한 UI에서 중요하다.

Q. 모든 컴포넌트에 keyboard 테스트가 필요해?
A. 아니다. 핵심 interactive component를 우선한다.

Q. focus restore는 왜 중요해?
A. Modal이나 overlay가 닫힌 뒤 사용자가 원래 위치를 잃지 않게 하기 위해 중요하다.

# 9. Maintainability Review

## 9.1 Test Readability Review

### [개념]

Test Readability Review는 테스트 코드가 읽기 쉽고 실패 원인을 빠르게 이해할 수 있는지 확인하는 리뷰다.

테스트는 기능 명세처럼 읽힐 수 있어야 한다.

### [핵심]

검토 대상:

- readable test
- clear arrange
- clear act
- clear assert
- small test
- no excessive abstraction
- no hidden setup
- meaningful helper
- local context
- simple fixture

### [실무]

리뷰 질문:

```md
- [ ] 테스트를 위에서 아래로 읽으면 사용자 흐름이 보이는가?
- [ ] setup이 과도하게 helper 안에 숨겨져 있지 않은가?
- [ ] fixture가 테스트 의도를 가리지 않는가?
- [ ] 불필요한 assertion이 없는가?
- [ ] 한 테스트가 너무 많은 시나리오를 다루지 않는가?
- [ ] 실패 메시지를 보고 원인을 추측할 수 있는가?
```

나쁜 예:

```tsx
renderDefault();
await doLogin();
await clickThing();
expectSuccess();
```

좋은 예:

```tsx
renderWithProviders(<LoginPage />, {
  initialEntries: ["/login"],
});

await user.type(screen.getByLabelText("이메일"), "test@example.com");
await user.type(screen.getByLabelText("비밀번호"), "password123");
await user.click(screen.getByRole("button", { name: "로그인" }));

expect(
  await screen.findByRole("heading", { name: "마이페이지" }),
).toBeInTheDocument();
```

권장:

- helper는 반복 setup만 줄임
- 사용자 행동은 테스트 본문에 드러내는 것이 좋음
- assertion은 명확하게 작성
- 테스트가 너무 길면 시나리오 분리
- DRY보다 명확성이 우선인 경우 많음

### [FAQ]

Q. Test Readability Review의 핵심은 뭐야?
A. 테스트가 사용자 흐름과 기대 결과를 명확히 보여주는지 확인하는 것이다.

Q. helper를 많이 만들면 좋은 거 아니야?
A. 반복은 줄지만 테스트 의도를 숨기면 오히려 나쁘다.

Q. 테스트가 길면 무조건 나빠?
A. 아니지만 여러 시나리오가 섞여 있으면 분리하는 것이 좋다.

## 9.2 Abstraction Review

### [개념]

Abstraction Review는 테스트 helper, factory, render utility가 중복을 줄이면서도 테스트 의도를 숨기지 않는지 확인하는 리뷰다.

테스트 코드에서는 과도한 추상화보다 명확성이 중요하다.

### [핵심]

검토 대상:

- render helper
- setup helper
- action helper
- assertion helper
- factory abstraction
- hidden behavior
- over abstraction
- explicit test flow
- helper readability

### [실무]

나쁜 helper:

```tsx
await completeHappyPath();
```

이름만으로 내부 행동이 불명확하다.

좋은 helper:

```tsx
renderLoginPage();
await fillLoginForm({
  email: "test@example.com",
  password: "password123",
});
```

단, 핵심 검증은 본문에 두는 것이 좋다.

```tsx
expect(
  await screen.findByRole("heading", { name: "마이페이지" }),
).toBeInTheDocument();
```

리뷰 질문:

```md
- [ ] helper 이름만 보고 역할을 알 수 있는가?
- [ ] helper가 assertion까지 숨기고 있지 않은가?
- [ ] 사용자 행동이 너무 많이 감춰져 있지 않은가?
- [ ] factory override가 테스트 의도를 드러내는가?
- [ ] render utility가 모든 Provider를 무조건 감싸지 않는가?
```

권장:

- render/setup 반복은 helper화
- 핵심 user action은 본문에 드러내기
- 핵심 assertion은 본문에 드러내기
- helper는 작고 이름이 명확해야 함
- magic helper 지양

### [FAQ]

Q. 테스트 코드에서 추상화는 나쁜 거야?
A. 아니다. 하지만 과도하면 테스트 의도를 숨기므로 조심해야 한다.

Q. 어떤 helper가 좋은 helper야?
A. 반복 setup을 줄이면서 이름만 보고 역할을 알 수 있는 helper다.

Q. assertion helper는 써도 돼?
A. 가능하지만 핵심 기대 결과가 숨겨지지 않게 주의한다.

# 10. Coverage Review

## 10.1 Coverage Caution

### [개념]

Coverage Caution은 테스트 커버리지 수치가 높아도 테스트 품질이 높다는 뜻은 아니라는 규칙이다.

Frontend Testing에서 중요한 것은 몇 줄을 실행했는지가 아니라 사용자에게 중요한 동작과 상태를 보장하는 것이다.

### [핵심]

- test coverage
- line coverage
- branch coverage
- function coverage
- meaningful coverage
- false confidence
- behavior coverage
- scenario coverage
- risk based testing

### [실무]

커버리지가 높아도 부족한 경우:

```text
렌더만 하고 assertion이 약함
Snapshot만 많음
성공 case만 테스트함
Error/Empty/Loading 누락
접근성 검증 없음
중요 사용자 흐름 누락
```

커버리지가 낮아도 중요한 테스트:

```text
로그인 실패 시 오류 메시지
결제 중 중복 클릭 방지
권한 없는 관리자 Page 접근 차단
리뷰 등록 후 목록 갱신
검색 결과 없음 안내
```

리뷰 질문:

```md
- [ ] 커버리지 수치보다 사용자 위험도가 높은 흐름을 테스트했는가?
- [ ] branch coverage가 중요한 분기를 포함하는가?
- [ ] error/empty/loading 분기가 테스트되었는가?
- [ ] 권한/인증 분기가 테스트되었는가?
- [ ] 단순 렌더 테스트로 수치만 채우지 않았는가?
```

권장:

- 커버리지는 참고 지표
- 위험도 높은 기능 우선 테스트
- Branch coverage는 validation/error/auth 분기에 중요
- coverage 증가보다 meaningful assertion 우선
- 숫자를 맞추기 위한 무의미한 테스트 지양

### [FAQ]

Q. 커버리지 100%면 테스트가 충분해?
A. 아니다. 중요한 사용자 시나리오와 실패 상태를 검증하지 못하면 부족하다.

Q. 커버리지는 볼 필요 없어?
A. 참고 지표로는 유용하다. 다만 품질을 대체하지 않는다.

Q. Frontend에서 중요한 커버리지는 뭐야?
A. 사용자 행동, 상태 분기, 오류 처리, 권한 분기, 접근성 관련 흐름을 검증하는 커버리지가 중요하다.

## 10.2 Risk Based Review

### [개념]

Risk Based Review는 모든 코드를 같은 비중으로 테스트하지 않고 사용자 영향과 장애 위험이 큰 부분을 우선 검토하는 방식이다.

### [핵심]

고위험 영역:

- login
- signup
- payment
- auth
- protected route
- admin permission
- form validation
- mutation
- delete action
- data fetching
- error state
- accessibility critical UI

저위험 영역:

- static text
- simple layout
- pure presentational style
- decorative component
- simple wrapper

### [실무]

우선 리뷰 대상:

```text
사용자가 돈을 쓰는 기능
사용자가 데이터를 생성/수정/삭제하는 기능
인증/권한이 필요한 기능
개인정보가 표시되는 기능
오류 발생 시 사용자 피해가 큰 기능
접근성 실패 시 사용이 불가능한 핵심 Form
```

리뷰 질문:

```md
- [ ] 고위험 기능에 성공/실패 테스트가 있는가?
- [ ] 삭제/결제/저장 action에 중복 클릭 방지가 있는가?
- [ ] Auth/Role 분기를 테스트했는가?
- [ ] 서버 오류와 네트워크 오류를 처리하는가?
- [ ] 중요한 Form validation을 테스트했는가?
```

권장:

- 위험도 높은 기능부터 테스트 품질 강화
- 단순 UI보다 mutation/auth/error 우선
- coverage 목표도 위험도 기준으로 해석
- 고위험 기능은 negative case 포함

### [FAQ]

Q. Risk Based Review는 뭐야?
A. 사용자 피해와 장애 위험이 큰 기능을 우선 검토하는 테스트 리뷰 방식이다.

Q. 모든 Component를 같은 수준으로 테스트해야 해?
A. 아니다. 로그인, 결제, 권한, Form, mutation 같은 고위험 기능을 더 강하게 테스트한다.

Q. 단순 Presentational Component는 어떻게 봐?
A. 핵심 텍스트와 role 정도를 확인하고 과도한 테스트는 피할 수 있다.

# 11. Security and Privacy Review

## 11.1 Test Data Security Review

### [개념]

Test Data Security Review는 테스트 코드, fixture, snapshot, mock response에 실제 token, secret, 개인정보, 운영 URL이 포함되지 않았는지 확인하는 리뷰다.

테스트 데이터도 저장소에 남으므로 보안 검토 대상이다.

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
- internal server detail

### [실무]

리뷰 질문:

```md
- [ ] 실제 token이 없는가?
- [ ] 실제 이메일/전화번호/주소가 없는가?
- [ ] 운영 API URL이 없는가?
- [ ] 실제 서버 error detail이 노출되지 않는가?
- [ ] snapshot 파일에 민감정보가 없는가?
- [ ] fixture에 실제 사용자 데이터를 복사하지 않았는가?
```

좋은 예:

```ts
const user = {
  email: "test@example.com",
  nickname: "tester",
};

const loginResponse = {
  accessToken: "test-access-token",
};
```

나쁜 예:

```ts
const loginResponse = {
  accessToken: "실제_운영_TOKEN",
  email: "real-user@example.com",
};
```

권장:

- `test@example.com` 사용
- `test-access-token` 사용
- 실제 운영 응답 복붙 금지
- snapshot diff에서 민감정보 확인
- payment/auth 관련 테스트는 특히 주의

### [FAQ]

Q. Test Data Security Review는 왜 필요해?
A. 테스트 코드와 snapshot도 저장소에 남기 때문에 민감정보가 유출될 수 있다.

Q. 실제 token을 잠깐 넣고 테스트해도 돼?
A. 안 된다. 더미 token만 사용해야 한다.

Q. 실제 API 응답을 fixture로 복사해도 돼?
A. 개인정보와 운영 정보가 제거되지 않았다면 위험하다. 더미 데이터로 재작성해야 한다.

## 11.2 Error Message Security Review

### [개념]

Error Message Security Review는 테스트가 서버 내부 error detail, stack trace, 민감한 인증 정보를 사용자에게 노출하도록 기대하지 않는지 확인하는 리뷰다.

### [핵심]

검토 대상:

- safe error message
- no stack trace
- no internal server detail
- no SQL error
- no token exposure
- no secret exposure
- auth error message
- fallback message
- user-friendly message

### [실무]

나쁜 테스트:

```tsx
expect(
  await screen.findByText("SQLSyntaxErrorException at UserRepository"),
).toBeInTheDocument();
```

좋은 테스트:

```tsx
expect(
  await screen.findByText(
    "서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.",
  ),
).toBeInTheDocument();
```

로그인 실패:

```text
나쁜 문구:
해당 이메일은 존재하지만 비밀번호가 틀렸습니다.

좋은 문구:
이메일 또는 비밀번호가 올바르지 않습니다.
```

리뷰 질문:

```md
- [ ] 서버 내부 오류를 그대로 표시하지 않는가?
- [ ] 인증 실패 메시지가 계정 존재 여부를 과도하게 노출하지 않는가?
- [ ] token, secret, stack trace가 UI에 표시되지 않는가?
- [ ] 사용자 친화적 fallback message를 테스트하는가?
```

권장:

- 오류 메시지는 사용자 친화적이고 안전해야 함
- 서버 detail은 console/logging 정책으로 분리
- 인증 오류는 정보 노출 최소화
- 테스트도 안전한 메시지를 기대해야 함

### [FAQ]

Q. 서버 error message를 그대로 테스트하면 안 돼?
A. 보안상 위험할 수 있다. 사용자에게 표시할 안전한 메시지를 테스트하는 것이 좋다.

Q. 로그인 실패 메시지는 왜 조심해야 해?
A. 계정 존재 여부를 노출하면 보안 위험이 될 수 있다.

Q. stack trace가 UI에 보이면?
A. 보안 문제다. 테스트는 안전한 fallback message를 기대해야 한다.

# 12. Review Anti Pattern

## 12.1 Common Review Anti Patterns

### [개념]

Review Anti Pattern은 테스트 코드 리뷰에서 품질 문제를 놓치거나 통과 여부와 커버리지 숫자만으로 테스트를 판단하는 잘못된 방식이다.

### [핵심]

Anti Pattern:

- 통과 여부만 확인
- coverage 숫자만 확인
- Snapshot update 무검토 승인
- getByTestId 남용 방치
- 실제 API 호출 방치
- mock shape 불일치 방치
- waitFor 남용 방치
- accessibility assertion 누락 방치
- flaky test rerun으로만 해결
- fixture 민감정보 미검토
- Provider 과다/누락 미검토
- 테스트 이름 모호함 방치

### [실무]

나쁜 리뷰:

```text
테스트 통과하네요. OK.
커버리지 올랐네요. OK.
Snapshot 업데이트네요. OK.
```

좋은 리뷰:

```text
테스트 이름이 사용자 결과를 설명하는가?
이 assertion이 실제 기대 결과를 보장하는가?
mock response가 실제 DTO와 맞는가?
비동기 UI에 findBy를 사용하는가?
getByTestId 대신 role/name을 사용할 수 있는가?
Error/Empty 상태가 빠지지 않았는가?
```

리뷰 코멘트 예:

```text
이 테스트는 login 함수 호출만 검증하고 있어서,
로그인 성공 후 사용자가 보는 마이페이지 heading을 함께 검증하는 것이 좋겠습니다.
```

```text
이 mock은 id/name을 사용하지만 실제 응답은 festivalId/title이라
실제 API shape에 맞춰 수정하는 것이 안전합니다.
```

권장:

- 통과 여부보다 의미 있는 assertion 확인
- 커버리지보다 위험 흐름 확인
- snapshot diff 직접 리뷰
- 접근성 Query 우선
- mock shape와 보안 데이터 검토

### [FAQ]

Q. Review Anti Pattern의 대표 사례는 뭐야?
A. 테스트가 통과한다는 이유만으로 품질 검토 없이 승인하는 것이다.

Q. 커버리지가 올랐으면 좋은 테스트야?
A. 항상 그렇지는 않다. 의미 있는 사용자 시나리오를 검증하는지 봐야 한다.

Q. Snapshot 변경은 어떻게 리뷰해야 해?
A. diff를 읽고 의도된 변경인지, 민감정보나 접근성 회귀가 없는지 확인해야 한다.

# 13. Frontend Testing Review Checklist

## 13.1 Review Checklist

### [개념]

Frontend Testing Review Checklist는 테스트 코드가 사용자 관점, 접근성, 안정성, 독립성, 보안 기준을 만족하는지 검토하는 종합 체크리스트다.

### [핵심]

Checklist:

```md
- [ ] 테스트 이름이 조건 / 행동 / 기대 결과를 설명하는가?
- [ ] assertion이 테스트 이름의 기대 결과와 일치하는가?
- [ ] 사용자 visible result를 검증하는가?
- [ ] getByRole / getByLabelText 등 사용자 관점 Query를 우선 사용하는가?
- [ ] getByTestId를 불필요하게 남용하지 않는가?
- [ ] userEvent를 사용하고 await를 붙였는가?
- [ ] fireEvent를 일반 interaction에 남용하지 않는가?
- [ ] 비동기 UI에는 findBy를 사용하는가?
- [ ] waitFor를 필요한 경우에만 사용하는가?
- [ ] waitFor 안에서 userEvent를 실행하지 않는가?
- [ ] Loading / Error / Empty / Success 상태를 적절히 테스트했는가?
- [ ] API mock path가 실제 import path와 일치하는가?
- [ ] mock response shape가 실제 API와 일치하는가?
- [ ] error response shape가 실제 error handler와 일치하는가?
- [ ] Provider 구성이 필요한 만큼만 포함되어 있는가?
- [ ] QueryClient는 테스트마다 새로 생성되는가?
- [ ] Auth state는 명확히 주입되는가?
- [ ] 테스트 간 상태 공유가 없는가?
- [ ] fixture / factory가 작고 명확한가?
- [ ] 실제 token / secret / 개인정보가 없는가?
- [ ] 접근성 role/name/label/focus 기준을 고려했는가?
- [ ] Snapshot-only Test가 아닌가?
- [ ] 테스트가 실패했을 때 원인을 이해하기 쉬운가?
```

### [실무]

Agent Review Flow:

```text
Receive Test Code
→ Identify Test Type
→ Check Test Name and Purpose
→ Check User-visible Assertion
→ Check Query Strategy
→ Check userEvent and Async
→ Check Mock Shape
→ Check Providers
→ Check Isolation
→ Check Accessibility
→ Check Security Data
→ Suggest Minimal Improvements
```

리뷰 등급 기준:

```text
A급 테스트
→ 사용자 시나리오 명확, assertion 강함, mock 안정, 접근성 고려, 독립적

B급 테스트
→ 핵심은 검증하지만 일부 상태나 접근성 보완 필요

C급 테스트
→ 통과는 하지만 구현 세부사항/약한 assertion/불안정성 존재

D급 테스트
→ 목적 불명확, snapshot-only, 실제 API 의존, mock shape 불일치
```

### [FAQ]

Q. Frontend Testing Review Checklist의 핵심은 뭐야?
A. 테스트가 사용자 결과를 명확히 검증하고 안정적이며 실제 API shape와 접근성 기준을 만족하는지 확인하는 것이다.

Q. 좋은 테스트와 나쁜 테스트를 가르는 기준은 뭐야?
A. 통과 여부가 아니라 사용자 시나리오를 의미 있게 보장하는지, 실패했을 때 원인을 알 수 있는지가 중요하다.

Q. 리뷰 후 개선은 어떻게 제안해야 해?
A. 테스트 전체를 갈아엎기보다 Query, assertion, mock shape, async 대기처럼 최소 수정으로 품질을 높이는 방향이 좋다.

# 14. Part16 Summary

## 14.1 Frontend Testing Review Final Rule

### [개념]

Frontend Testing Part16은 작성된 Frontend 테스트 코드를 리뷰하는 기준을 정의한다.

이 Part의 목적은 Agent가 테스트를 단순히 작성하는 것을 넘어 품질, 안정성, 접근성, 유지보수성, 보안 데이터 기준으로 검수할 수 있게 만드는 것이다.

### [핵심]

최종 기준:

- 테스트 통과 여부만으로 품질을 판단하지 않음
- 테스트 이름은 조건 / 행동 / 기대 결과를 설명해야 함
- assertion은 테스트 이름과 일치해야 함
- 사용자 visible result 검증이 우선
- getByRole / getByLabelText 우선
- getByTestId 남용 금지
- userEvent와 await 사용
- 비동기 UI는 findBy 우선
- waitFor 남용 금지
- Loading / Error / Empty / Success 상태 검토
- API mock path와 response shape 검토
- error response shape와 fieldErrors 검토
- Provider 구성과 QueryClient isolation 검토
- 테스트 간 상태 공유 금지
- 접근성 role/name/label/focus 검토
- Snapshot-only Test 금지
- fixture와 snapshot에 민감정보 금지
- 커버리지 숫자보다 위험 기반 테스트 품질 우선
- 리뷰는 최소 수정으로 테스트 신뢰도를 높이는 방향으로 수행

### [실무]

Agent 작업 Flow:

```text
Frontend Test Review Request
→ Classify Test Type
→ Review Purpose and Name
→ Review User Flow
→ Review Assertions
→ Review Query Strategy
→ Review Async Handling
→ Review Mock and Provider
→ Review Accessibility and Security
→ Identify Anti Pattern
→ Propose Improved Test
```

Part17 이후 연결:

```text
Part16 Frontend Testing Review
→ Part17 Final Frontend Testing Rules
```

### [FAQ]

Q. Part16의 최종 목적은 뭐야?
A. Frontend Agent가 테스트 코드의 품질을 사용자 관점, 안정성, 접근성, 보안 기준으로 리뷰할 수 있게 만드는 것이다.

Q. Frontend Testing Review에서 가장 중요한 규칙은 뭐야?
A. 테스트가 통과하는지가 아니라 사용자에게 중요한 동작을 의미 있게 보장하는지 확인하는 것이다.

Q. Part16 다음에는 어떤 내용이 이어져야 해?
A. Frontend Testing 전체 문서를 통합한 최종 규칙과 Agent 적용 기준인 Final Frontend Testing Rules가 이어지는 것이 좋다.

# Retrieval Queries

### [FAQ]

Q. Frontend Testing Review는 뭐야?
A. 테스트 코드가 사용자 관점, 접근성, 안정성, 유지보수성 기준을 만족하는지 검토하는 과정이다.

Q. 테스트가 통과하면 리뷰가 필요 없어?
A. 아니다. 통과하는 테스트라도 의미가 약하거나 불안정하면 좋은 테스트가 아니다.

Q. 테스트 리뷰에서 가장 먼저 볼 것은 뭐야?
A. 테스트 이름과 목적이 사용자 시나리오와 기대 결과를 명확히 설명하는지 확인한다.

Q. 테스트 리뷰는 무엇까지 봐야 해?
A. 이름, 사용자 시나리오, Query, async, Mock, Provider, 독립성, 보안 데이터를 함께 본다.

Q. 모든 테스트에 같은 기준을 적용해야 해?
A. 아니다. Unit, Component, Integration, Router, Query 테스트마다 중점이 다르다.

Q. Test Name Review의 핵심은 뭐야?
A. 테스트 이름만 보고 조건, 행동, 기대 결과를 이해할 수 있어야 한다.

Q. 테스트 이름이 길어도 돼?
A. 길어도 명확하면 괜찮지만 불필요한 구현 설명은 줄이는 것이 좋다.

Q. renders 같은 이름은 왜 안 좋아?
A. 무엇이 렌더링되어야 하는지 알 수 없어 실패 원인을 파악하기 어렵다.

Q. Assertion Purpose Review는 왜 필요해?
A. 테스트 이름과 실제 검증 내용이 다르면 테스트가 통과해도 기대 기능을 보장하지 못하기 때문이다.

Q. API 호출 여부만 확인하면 부족해?
A. 대부분 부족하다. API 결과로 사용자에게 보이는 UI를 검증해야 한다.

Q. User-centric Query Review는 뭐야?
A. 테스트가 사용자가 인식하는 role, label, name 기준으로 요소를 찾는지 검토하는 것이다.

Q. getByTestId는 쓰면 안 돼?
A. 최후 수단으로는 가능하지만 기본 Query로 사용하면 접근성 문제를 숨길 수 있다.

Q. className으로 요소를 찾으면 왜 안 좋아?
A. 사용자 관점이 아니라 구현 세부사항에 의존해 테스트가 쉽게 깨진다.

Q. User Event Review의 핵심은 뭐야?
A. 테스트가 실제 사용자 행동에 가깝게 userEvent로 interaction을 실행하는지 확인하는 것이다.

Q. fireEvent는 쓰면 안 돼?
A. 특수 event나 userEvent가 지원하지 않는 상황에서는 가능하지만 일반 클릭/입력은 userEvent가 우선이다.

Q. userEvent에 await를 안 붙이면?
A. 상태 업데이트를 기다리지 못해 act warning이나 flaky test가 발생할 수 있다.

Q. Async Query Review는 뭐야?
A. 비동기 UI에 getBy/findBy/queryBy/waitFor를 올바르게 사용하는지 검토하는 것이다.

Q. API 결과를 getBy로 찾으면 안 돼?
A. API 응답 후 비동기로 나타나는 UI는 findBy가 안전하다.

Q. waitFor는 언제 쓰는 게 좋아?
A. callback 호출이나 특정 조건 변화처럼 findBy로 표현하기 어려운 경우에 사용한다.

Q. Loading Error Empty Review는 왜 필요해?
A. 성공 상태만으로는 실제 사용자가 겪는 대기, 실패, 빈 데이터 상황을 보장할 수 없기 때문이다.

Q. 모든 화면에 Loading/Error/Empty 테스트가 필요해?
A. 데이터 요청이 핵심인 화면에는 필요하고, 작은 정적 Component에는 필요하지 않을 수 있다.

Q. API Mock Review의 핵심은 뭐야?
A. mock 경로와 response/error shape가 실제 코드와 일치하는지 확인하는 것이다.

Q. mock이 실제 API와 조금 달라도 테스트만 통과하면 괜찮아?
A. 아니다. 실제 연동에서 깨질 수 있으므로 mock shape를 실제와 맞춰야 한다.

Q. Fixture Review에서 가장 중요한 건 뭐야?
A. 실제 API shape와 일치하면서 테스트 의도를 흐리지 않을 만큼 작아야 한다는 것이다.

Q. 큰 fixture는 왜 안 좋아?
A. 테스트가 무엇을 검증하는지 흐리고 유지보수 비용이 커진다.

Q. MSW Review의 핵심은 뭐야?
A. handler URL/method/response가 실제 요청과 일치하고 테스트별 override가 격리되는지 확인하는 것이다.

Q. unhandled request warning은 리뷰에서 어떻게 봐?
A. mock 누락이나 URL 불일치 신호이므로 방치하면 안 된다.

Q. Provider Setup Review의 핵심은 뭐야?
A. 테스트 대상이 실제 동작에 필요한 Provider를 갖고 있고, 불필요한 Provider로 테스트 의도를 숨기지 않는지 확인하는 것이다.

Q. 모든 Provider를 항상 감싸면 편하지 않아?
A. 편하지만 테스트가 무거워지고 어떤 의존성이 필요한지 숨겨질 수 있다.

Q. Environment Setup Review는 왜 필요해?
A. 테스트 환경 설정이 잘못되면 많은 테스트가 불안정하거나 실제 브라우저와 다른 결과를 낼 수 있기 때문이다.

Q. Independent Test Review는 왜 중요해?
A. 테스트 순서와 실행 환경에 따라 결과가 달라지는 문제를 막기 위해 중요하다.

Q. 로그인 상태를 테스트 간 공유해도 돼?
A. 안 된다. 각 테스트에서 인증 상태를 직접 준비해야 한다.

Q. Deterministic Review는 뭐야?
A. 테스트가 언제 어디서 실행되어도 같은 결과를 내는지 확인하는 리뷰다.

Q. 날짜 테스트는 어떻게 안정화해?
A. 현재 날짜 대신 고정 날짜 입력을 사용하거나 시스템 시간을 mock한다.

Q. Accessibility Assertion Review는 왜 필요해?
A. 테스트가 사용자 관점뿐 아니라 보조기술 사용자 관점에서도 UI를 검증하도록 하기 위해 필요하다.

Q. axe가 있으면 role/label 테스트는 없어도 돼?
A. 아니다. axe는 보조 도구이고 role/label/keyboard 테스트가 필요하다.

Q. Keyboard and Focus Review는 언제 중요해?
A. Form, Modal, Dropdown, Menu, Navigation처럼 조작 흐름이 중요한 UI에서 중요하다.

Q. Test Readability Review의 핵심은 뭐야?
A. 테스트가 사용자 흐름과 기대 결과를 명확히 보여주는지 확인하는 것이다.

Q. helper를 많이 만들면 좋은 거 아니야?
A. 반복은 줄지만 테스트 의도를 숨기면 오히려 나쁘다.

Q. 테스트 코드에서 추상화는 나쁜 거야?
A. 아니다. 하지만 과도하면 테스트 의도를 숨기므로 조심해야 한다.

Q. 커버리지 100%면 테스트가 충분해?
A. 아니다. 중요한 사용자 시나리오와 실패 상태를 검증하지 못하면 부족하다.

Q. Risk Based Review는 뭐야?
A. 사용자 피해와 장애 위험이 큰 기능을 우선 검토하는 테스트 리뷰 방식이다.

Q. 모든 Component를 같은 수준으로 테스트해야 해?
A. 아니다. 로그인, 결제, 권한, Form, mutation 같은 고위험 기능을 더 강하게 테스트한다.

Q. Test Data Security Review는 왜 필요해?
A. 테스트 코드와 snapshot도 저장소에 남기 때문에 민감정보가 유출될 수 있다.

Q. 실제 token을 잠깐 넣고 테스트해도 돼?
A. 안 된다. 더미 token만 사용해야 한다.

Q. 서버 error message를 그대로 테스트하면 안 돼?
A. 보안상 위험할 수 있다. 사용자에게 표시할 안전한 메시지를 테스트하는 것이 좋다.

Q. Review Anti Pattern의 대표 사례는 뭐야?
A. 테스트가 통과한다는 이유만으로 품질 검토 없이 승인하는 것이다.

Q. 커버리지가 올랐으면 좋은 테스트야?
A. 항상 그렇지는 않다. 의미 있는 사용자 시나리오를 검증하는지 봐야 한다.

Q. Frontend Testing Review Checklist의 핵심은 뭐야?
A. 테스트가 사용자 결과를 명확히 검증하고 안정적이며 실제 API shape와 접근성 기준을 만족하는지 확인하는 것이다.

Q. 좋은 테스트와 나쁜 테스트를 가르는 기준은 뭐야?
A. 통과 여부가 아니라 사용자 시나리오를 의미 있게 보장하는지, 실패했을 때 원인을 알 수 있는지가 중요하다.

Q. Part16 Frontend Testing Review의 최종 목표는 뭐야?
A. Frontend Agent가 테스트 코드의 품질을 사용자 관점, 안정성, 접근성, 보안 기준으로 리뷰할 수 있게 만드는 것이다.
