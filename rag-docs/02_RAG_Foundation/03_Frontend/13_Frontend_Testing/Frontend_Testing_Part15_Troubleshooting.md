# Frontend Testing Part15 - Troubleshooting

---

# 1. Frontend Testing Troubleshooting Overview

## 1.1 Troubleshooting Definition

### [개념]

Frontend Testing Troubleshooting은 React Testing Library, Vitest/Jest, userEvent, API Mock, Router, TanStack Query, Provider, jsdom 환경에서 테스트 실패 원인을 찾고 해결하는 기준이다.

Frontend 테스트 실패는 대부분 Query 선택 오류, 비동기 대기 누락, Provider 누락, mock 미적용, 상태 공유, jsdom 환경 차이에서 발생한다.

### [핵심]

- Frontend Testing Troubleshooting
- Test Failure
- Query Failed
- Async Timeout
- act Warning
- Provider Missing
- Mock Not Working
- API Mock Error
- userEvent Issue
- waitFor Issue
- TanStack Query Retry
- Router Context Error
- jsdom Limitation
- Flaky Test
- Test Isolation
- Debug Flow
- screen.debug
- Testing Playground

### [실무]

문제 해결 기본 Flow:

```text
Test Failed
→ 에러 메시지 확인
→ 실패한 assertion 확인
→ screen.debug로 현재 DOM 확인
→ Query 종류 확인
→ 비동기 여부 확인
→ Provider 누락 확인
→ Mock 적용 여부 확인
→ 테스트 간 상태 공유 확인
→ jsdom 환경 한계 확인
```

자주 발생하는 실패 유형:

```text
Unable to find role
Unable to find text
Timed out in waitFor
act warning
No QueryClient set
useNavigate outside Router
mockResolvedValue not applied
API actually called
Element not disabled
Element still in document
Focus assertion failed
```

좋은 Troubleshooting 습관:

```text
에러 메시지를 먼저 읽는다.
DOM을 확인한다.
사용자 관점 Query가 맞는지 확인한다.
비동기 UI에는 findBy를 사용한다.
Provider와 mock을 확인한다.
테스트 코드를 무작정 waitFor로 감싸지 않는다.
```

### [FAQ]

Q. Frontend Testing Troubleshooting은 뭐야?
A. 테스트 실패 원인을 Query, async, Provider, mock, 환경, 상태 공유 관점에서 찾아 해결하는 기준이다.

Q. 테스트가 실패하면 가장 먼저 뭘 봐야 해?
A. 에러 메시지와 현재 DOM 상태를 확인해야 한다.

Q. screen.debug는 언제 써?
A. 테스트가 찾는 요소가 실제 DOM에 있는지 확인하고 싶을 때 사용한다.

## 1.2 Troubleshooting Priority

### [개념]

Troubleshooting Priority는 테스트 실패 원인을 찾을 때 어떤 순서로 점검할지 정하는 기준이다.

대부분의 Frontend 테스트 문제는 Query, Async, Provider, Mock 순서로 확인하면 빠르게 좁힐 수 있다.

### [핵심]

점검 우선순위:

1. Query가 사용자 관점에 맞는가?
2. 요소가 비동기로 나타나는가?
3. Provider가 필요한가?
4. Mock이 실제 import 경로에 적용되었는가?
5. Mock response shape가 실제 코드와 맞는가?
6. 테스트 간 상태가 공유되고 있는가?
7. jsdom이 지원하지 않는 browser API인가?
8. 테스트가 구현 세부사항에 의존하는가?

### [실무]

Debug Checklist:

```md
- [ ] getBy / findBy / queryBy 선택이 맞는가?
- [ ] role과 accessible name이 맞는가?
- [ ] userEvent에 await를 붙였는가?
- [ ] 비동기 결과를 findBy로 기다렸는가?
- [ ] Router / QueryClient / Auth Provider가 있는가?
- [ ] API mock path가 실제 import와 일치하는가?
- [ ] mockResolvedValue / mockRejectedValue가 테스트 전에 설정되었는가?
- [ ] error response shape가 실제 코드와 맞는가?
- [ ] QueryClient cache가 테스트 간 공유되지 않는가?
- [ ] localStorage / sessionStorage가 남아 있지 않은가?
```

주의:

```text
waitFor를 추가하기 전에
왜 기다려야 하는지 먼저 확인한다.
```

### [FAQ]

Q. 테스트 실패 원인은 어떤 순서로 봐야 해?
A. Query, Async, Provider, Mock, State Isolation, jsdom 환경 순서로 보는 것이 좋다.

Q. waitFor를 넣으면 대부분 해결돼?
A. 일시적으로 통과할 수 있지만 원인을 숨길 수 있다. 먼저 비동기 여부와 Query를 확인해야 한다.

Q. 테스트가 로컬에서는 되는데 CI에서 실패하면?
A. 비동기 대기, 테스트 간 상태 공유, 환경 의존 값, jsdom global mock을 우선 확인한다.

# 2. Query Failure Troubleshooting

## 2.1 Unable to Find Role

### [개념]

Unable to Find Role은 `getByRole`, `findByRole`, `queryByRole`이 기대한 role 요소를 찾지 못하는 오류다.

이 오류는 테스트 Query 문제일 수도 있지만 Component의 접근성 문제가 드러난 것일 수 있다.

### [핵심]

원인:

- wrong role
- wrong accessible name
- element not rendered
- async rendering
- hidden element
- disabled but still role exists
- icon button without aria-label
- div used instead of button
- link missing href
- label not connected
- aria-hidden parent

### [실무]

문제 예:

```tsx
screen.getByRole("button", { name: "검색" });
```

실제 DOM:

```tsx
<button>
  <SearchIcon />
</button>
```

해결:

```tsx
<button aria-label="검색">
  <SearchIcon />
</button>
```

Debug Flow:

```text
Unable to find role
→ screen.debug 확인
→ Testing Playground 확인
→ 실제 semantic element인지 확인
→ accessible name 확인
→ hidden 여부 확인
→ 비동기 렌더링이면 findByRole 사용
→ Component 접근성 개선
```

Testing Library error message에는 접근 가능한 role 목록이 포함되는 경우가 많다.

```text
Available roles:
button:
  Name "로그인":
  <button />
```

권장:

- role/name 실패 시 testId로 바로 우회하지 않음
- icon button은 aria-label 제공
- 클릭 가능한 div는 button으로 변경
- link는 href를 가져야 link role로 인식됨
- 비동기 UI는 findByRole 사용

### [FAQ]

Q. getByRole이 실패하면 테스트가 잘못된 거야?
A. 테스트 문제일 수도 있지만 Component 접근성 문제가 드러난 것일 수 있다.

Q. 화면에는 버튼이 보이는데 getByRole로 못 찾아.
A. 실제 button이 아니거나 accessible name이 없을 수 있다.

Q. 바로 getByTestId로 바꿔도 돼?
A. 최후 수단이다. 먼저 semantic HTML과 accessible name을 개선한다.

## 2.2 Unable to Find Text

### [개념]

Unable to Find Text는 `getByText`나 `findByText`가 기대한 텍스트를 찾지 못하는 오류다.

텍스트가 쪼개져 있거나, 비동기로 나타나거나, 실제 문구가 다르거나, 렌더링 조건이 맞지 않을 때 발생한다.

### [핵심]

원인:

- text mismatch
- async rendering
- split text nodes
- hidden text
- conditional rendering false
- API mock empty
- wrong mock response
- translation key shown
- whitespace difference
- text transformed
- wrong page rendered

### [실무]

문제:

```tsx
expect(screen.getByText("서버 오류가 발생했습니다.")).toBeInTheDocument();
```

비동기 오류라면:

```tsx
expect(
  await screen.findByText("서버 오류가 발생했습니다."),
).toBeInTheDocument();
```

텍스트가 여러 요소로 쪼개진 경우:

```tsx
expect(
  screen.getByText((content) => content.includes("서버 오류")),
).toBeInTheDocument();
```

하지만 가능하면 role 기반 Query가 더 좋다.

```tsx
expect(await screen.findByRole("alert")).toHaveTextContent(
  "서버 오류가 발생했습니다.",
);
```

Debug Flow:

```text
Unable to find text
→ screen.debug 확인
→ 실제 텍스트 확인
→ 비동기 여부 확인
→ getByText를 findByText로 바꿔야 하는지 확인
→ 텍스트가 쪼개졌는지 확인
→ mock response 확인
→ 올바른 Page가 렌더링되었는지 확인
```

권장:

- 버튼/링크/heading은 getByRole 우선
- 오류 메시지는 findByRole("alert") 고려
- 비동기 텍스트는 findByText 사용
- 문구가 자주 바뀌면 role + 부분 text 검토
- 번역 key가 그대로 보이면 i18n setup 확인

### [FAQ]

Q. getByText가 실패하면 뭘 확인해?
A. 실제 DOM 텍스트, 비동기 렌더링 여부, mock 응답, 렌더링 조건을 확인한다.

Q. 비동기 텍스트에는 어떤 Query를 써?
A. `findByText` 또는 role이 있으면 `findByRole`을 사용한다.

Q. 텍스트가 여러 span으로 쪼개져 있으면?
A. role 기반 Query를 우선하고, 필요하면 function matcher를 사용한다.

## 2.3 getByLabelText Failed

### [개념]

getByLabelText Failed는 input, textarea, select, checkbox, radio가 label과 연결되지 않았거나 accessible label이 없을 때 발생한다.

Form 접근성 문제를 가장 자주 드러내는 실패다.

### [핵심]

원인:

- label htmlFor mismatch
- input id missing
- custom input props not forwarded
- aria-label missing
- aria-labelledby id mismatch
- placeholder only
- hidden input
- wrong label text
- duplicate label
- wrapper clicked instead of input

### [실무]

문제:

```tsx
<label>이메일</label>
<input type="email" />
```

개선:

```tsx
<label htmlFor="email">이메일</label>
<input id="email" type="email" />
```

테스트:

```tsx
expect(screen.getByLabelText("이메일")).toBeInTheDocument();
```

Custom Input 문제:

```tsx
<CustomInput label="이메일" />
```

확인할 것:

```text
CustomInput이 id를 생성하는가?
label htmlFor와 input id가 일치하는가?
aria-label이 실제 input에 전달되는가?
ref와 props가 input에 전달되는가?
```

권장:

- placeholder를 label 대체로 사용하지 않음
- Form input은 label 기반으로 테스트 가능해야 함
- custom input component는 label 연결 테스트 작성
- password input은 getByLabelText 우선
- label 실패를 testId로 우회하지 않음

### [FAQ]

Q. getByLabelText가 실패하면 뭘 확인해?
A. label의 htmlFor와 input id 연결, aria-label, aria-labelledby를 확인한다.

Q. CustomInput에서 label이 안 잡히면?
A. label 관련 props가 실제 input 요소까지 전달되는지 확인해야 한다.

Q. placeholder로 테스트하면 안 돼?
A. 가능하지만 label 접근성을 대체하지 못하므로 getByLabelText가 우선이다.

# 3. Async Troubleshooting

## 3.1 findBy Timeout

### [개념]

findBy Timeout은 `findBy`가 제한 시간 안에 요소를 찾지 못해 실패하는 상황이다.

비동기 작업이 실행되지 않았거나 mock 응답이 잘못되었거나 조건부 렌더링이 기대와 다를 때 발생한다.

### [핵심]

원인:

- API mock not resolved
- mock path mismatch
- wrong response shape
- Provider missing
- component not rendered
- userEvent await missing
- button disabled
- validation blocked submit
- query enabled false
- retry delay
- wrong text or role
- promise never resolved

### [실무]

문제 예:

```tsx
expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
```

점검:

```text
getFestivals mockResolvedValue 설정했는가?
Component가 실제로 getFestivals를 호출하는가?
response shape가 data.content인지 array인지 맞는가?
QueryClientProvider가 있는가?
query enabled 조건이 true인가?
```

Debug Flow:

```text
findBy timeout
→ screen.debug 확인
→ API mock 호출 여부 확인
→ mock response shape 확인
→ Provider 확인
→ user action이 실행됐는지 확인
→ validation으로 submit이 막혔는지 확인
→ query enabled 조건 확인
```

예:

```tsx
expect(getFestivals).toHaveBeenCalled();
```

API 호출 여부는 원인 파악용으로 사용하고, 최종 테스트 목적은 UI 결과 검증으로 유지한다.

### [FAQ]

Q. findBy가 timeout이면 무슨 뜻이야?
A. 기대한 요소가 제한 시간 안에 DOM에 나타나지 않았다는 뜻이다.

Q. findBy timeout에서 가장 먼저 확인할 것은?
A. mock이 적용되었는지, 응답 shape가 맞는지, Component가 실제로 렌더링되었는지 확인한다.

Q. timeout을 늘리면 해결돼?
A. 근본 해결이 아닐 수 있다. 먼저 mock, Provider, 조건부 렌더링을 확인해야 한다.

## 3.2 waitFor Timeout

### [개념]

waitFor Timeout은 `waitFor` 내부 조건이 제한 시간 안에 통과하지 못해 실패하는 상황이다.

callback 호출, 상태 변경, element removal을 기다릴 때 흔히 발생한다.

### [핵심]

원인:

- callback not called
- async action not awaited
- wrong assertion
- mock not applied
- promise unresolved
- state not updated
- userEvent missing await
- fake timer issue
- waitFor misuse
- assertion impossible

### [실무]

나쁜 예:

```tsx
await waitFor(() => {
  user.click(screen.getByRole("button", { name: "저장" }));
  expect(save).toHaveBeenCalled();
});
```

좋은 예:

```tsx
await user.click(screen.getByRole("button", { name: "저장" }));

await waitFor(() => {
  expect(save).toHaveBeenCalled();
});
```

요소 등장에는 findBy 우선:

```tsx
expect(await screen.findByText("저장되었습니다.")).toBeInTheDocument();
```

waitFor가 적합한 경우:

```tsx
await waitFor(() => {
  expect(onSubmit).toHaveBeenCalledWith(expectedPayload);
});
```

Debug Flow:

```text
waitFor timeout
→ waitFor 안에서 userEvent 실행 여부 확인
→ assertion이 실제로 가능해지는지 확인
→ mock 호출 여부 확인
→ Promise resolve 여부 확인
→ fake timer 사용 여부 확인
→ findBy로 대체 가능한지 확인
```

권장:

- waitFor 안에서 userEvent 실행 금지
- 요소 등장에는 findBy 사용
- callback 호출 대기에 waitFor 사용
- waitFor 내부 assertion은 하나의 조건에 집중
- 무작정 waitFor로 감싸지 않음

### [FAQ]

Q. waitFor timeout은 왜 생겨?
A. 기다리는 조건이 실제로 발생하지 않거나 userEvent/mocking/비동기 처리가 잘못되었기 때문이다.

Q. waitFor 안에서 user.click 해도 돼?
A. 권장하지 않는다. user action은 waitFor 밖에서 실행한다.

Q. findBy와 waitFor 중 무엇을 써야 해?
A. 요소가 나타나는 것을 기다리면 findBy, callback이나 조건 변화를 기다리면 waitFor가 적합하다.

## 3.3 act Warning

### [개념]

act Warning은 React 상태 업데이트가 테스트 assertion 밖에서 발생했거나 비동기 업데이트를 제대로 기다리지 않았을 때 발생한다.

대부분 userEvent await 누락, async state 미대기, timer 미처리, API promise 미처리에서 발생한다.

### [핵심]

원인:

- userEvent await missing
- async UI not awaited
- promise resolved after test
- timer update not flushed
- state update in effect
- mutation result not awaited
- fireEvent misuse
- cleanup before update
- manual act needed rare

### [실무]

문제:

```tsx
user.click(screen.getByRole("button", { name: "저장" }));

expect(screen.getByText("저장되었습니다.")).toBeInTheDocument();
```

개선:

```tsx
await user.click(screen.getByRole("button", { name: "저장" }));

expect(await screen.findByText("저장되었습니다.")).toBeInTheDocument();
```

Form 입력:

```tsx
await user.type(screen.getByLabelText("이메일"), "test@example.com");
```

Timer가 있는 경우:

```tsx
vi.useFakeTimers();

await user.click(screen.getByRole("button", { name: "토스트 표시" }));

act(() => {
  vi.runAllTimers();
});
```

주의:

```text
대부분의 RTL 테스트에서는 직접 act를 쓸 필요가 없다.
먼저 userEvent await와 findBy 대기를 확인한다.
```

### [FAQ]

Q. act warning은 왜 나?
A. React 상태 업데이트를 테스트가 기다리지 않았기 때문에 발생하는 경우가 많다.

Q. act를 직접 감싸면 해결돼?
A. 가끔 필요하지만 대부분은 userEvent에 await를 붙이고 findBy로 UI 업데이트를 기다리면 해결된다.

Q. user.click에도 await가 필요해?
A. 필요하다. userEvent의 interaction은 비동기 동작을 포함할 수 있다.

# 4. userEvent Troubleshooting

## 4.1 userEvent Not Working

### [개념]

userEvent Not Working은 클릭, 입력, 키보드 동작이 기대한 UI 변화를 만들지 못하는 상황이다.

요소가 disabled이거나, 잘못된 요소를 클릭했거나, 이벤트 핸들러가 연결되지 않았거나, await가 누락되었을 수 있다.

### [핵심]

원인:

- await missing
- wrong target
- disabled element
- hidden element
- pointer-events none
- input readOnly
- controlled component wrapper missing
- event handler missing
- validation blocking
- focus not on target
- custom component issue

### [실무]

Debug Flow:

```text
userEvent 동작 안 함
→ await 사용 확인
→ 올바른 요소를 query했는지 확인
→ disabled/readOnly 여부 확인
→ handler 연결 확인
→ controlled component state 업데이트 확인
→ screen.debug 확인
→ 실제 사용자 흐름과 같은지 확인
```

입력 안 됨 문제:

```tsx
await user.type(screen.getByLabelText("이메일"), "test@example.com");

expect(screen.getByLabelText("이메일")).toHaveValue("test@example.com");
```

값이 안 바뀌면:

```text
input이 controlled인데 onChange가 state를 업데이트하는가?
value가 고정 문자열인가?
readOnly인가?
실제 input이 아닌 wrapper를 잡았는가?
```

권장:

- userEvent는 await 사용
- 실제 interactive element를 query
- disabled 요소 클릭으로 상태 변경 기대하지 않음
- controlled component는 wrapper state 필요
- fireEvent로 우회하기 전에 사용자 동작 가능 여부 확인

### [FAQ]

Q. user.click 했는데 아무 일도 안 일어나.
A. await 누락, disabled 상태, 잘못된 요소 클릭, handler 누락을 확인한다.

Q. user.type 했는데 값이 안 들어가.
A. controlled component의 value/onChange 연결과 readOnly 여부를 확인한다.

Q. fireEvent로 바꾸면 해결돼?
A. 임시로 될 수 있지만 실제 사용자 동작 문제를 숨길 수 있다. 먼저 userEvent 실패 원인을 확인한다.

## 4.2 Input Value Not Changing

### [개념]

Input Value Not Changing은 `user.type` 또는 `user.clear` 후 input 값이 바뀌지 않는 상황이다.

Controlled Component 구조와 state update 연결을 확인해야 한다.

### [핵심]

원인:

- controlled input without state update
- fixed value prop
- missing onChange
- wrong input target
- readOnly input
- disabled input
- masked input
- custom input wrapper
- debounce delay
- formatter transforms value

### [실무]

문제:

```tsx
render(<EmailInput value="" onChange={vi.fn()} />);

await user.type(screen.getByLabelText("이메일"), "test@example.com");

expect(screen.getByLabelText("이메일")).toHaveValue("test@example.com");
```

이 테스트는 실패할 수 있다. 부모 state가 value를 업데이트하지 않기 때문이다.

개선:

```tsx
function EmailInputTestWrapper() {
  const [email, setEmail] = useState("");

  return <EmailInput value={email} onChange={setEmail} />;
}
```

테스트:

```tsx
render(<EmailInputTestWrapper />);

await user.type(screen.getByLabelText("이메일"), "test@example.com");

expect(screen.getByLabelText("이메일")).toHaveValue("test@example.com");
```

권장:

- controlled input은 wrapper로 테스트
- value만 고정해놓고 user.type 결과 기대하지 않음
- custom input은 실제 input 요소에 label이 연결되는지 확인
- formatter가 있으면 기대 value도 변환 후 기준으로 검증
- debounce가 있으면 async 처리 고려

### [FAQ]

Q. controlled input 테스트에서 값이 안 바뀌어.
A. 부모 state가 onChange 결과로 value를 업데이트하지 않기 때문이다.

Q. wrapper component를 만들어도 돼?
A. 된다. controlled component의 실제 사용 방식을 재현하는 좋은 방법이다.

Q. user.clear도 await가 필요해?
A. 필요하다. `await user.clear(input)`으로 작성하는 것이 안전하다.

## 4.3 Keyboard Focus Failed

### [개념]

Keyboard Focus Failed는 `user.tab`, `user.keyboard`, `toHaveFocus` 테스트가 예상과 다르게 동작하는 상황이다.

focusable 요소, DOM 순서, disabled/hidden 상태, tabindex, jsdom 한계를 확인해야 한다.

### [핵심]

원인:

- element not focusable
- wrong tab order
- disabled element
- hidden element
- tabindex issue
- focus trap missing
- focus restore missing
- custom component no ref
- user.tab await missing
- jsdom limitation

### [실무]

Debug Flow:

```text
focus 테스트 실패
→ await user.tab 확인
→ 요소가 focusable인지 확인
→ disabled/hidden 여부 확인
→ DOM 순서 확인
→ tabindex 확인
→ Modal focus trap 확인
→ custom component ref forwarding 확인
```

예:

```tsx
await user.tab();
expect(screen.getByLabelText("이메일")).toHaveFocus();
```

div onClick 문제:

```tsx
<div onClick={onSave}>저장</div>
```

개선:

```tsx
<button type="button" onClick={onSave}>
  저장
</button>
```

권장:

- native focusable element 사용
- tabindex 남용 지양
- disabled 요소는 focus되지 않음
- hidden 요소는 focus 대상이 아님
- focus trap은 Modal 테스트에서 별도 검증

### [FAQ]

Q. user.tab 후 focus가 예상과 달라.
A. DOM 순서, focusable 여부, disabled/hidden 상태를 확인한다.

Q. div onClick은 keyboard focus가 돼?
A. 기본적으로 되지 않는다. button을 사용하는 것이 좋다.

Q. focus 테스트는 jsdom에서 완벽해?
A. 대부분 가능하지만 실제 브라우저 focus 동작은 E2E에서 보강할 수 있다.

# 5. Mock Troubleshooting

## 5.1 API Mock Not Applied

### [개념]

API Mock Not Applied는 `vi.mock` 또는 `jest.mock`을 설정했지만 Component에서 실제 API 함수가 호출되거나 mockResolvedValue가 반영되지 않는 상황이다.

가장 흔한 원인은 import path 불일치다.

### [핵심]

원인:

- import path mismatch
- alias path mismatch
- default export mismatch
- named export mismatch
- mock declaration order
- module cache
- actual API imported from another file
- axios instance direct call
- MSW handler missing
- setup file conflict

### [실무]

문제:

```tsx
vi.mock("../api/festivalApi", () => ({
  getFestivals: vi.fn(),
}));
```

실제 Component:

```tsx
import { getFestivals } from "@/features/festival/api/festivalApi";
```

경로가 다르면 mock이 적용되지 않을 수 있다.

개선:

```tsx
vi.mock("@/features/festival/api/festivalApi", () => ({
  getFestivals: vi.fn(),
}));
```

Debug Flow:

```text
API mock 미적용
→ Component의 실제 import path 확인
→ test의 vi.mock path 확인
→ named/default export 확인
→ vi.mocked(apiFn) 사용 확인
→ 실제 네트워크 요청 발생 여부 확인
→ API 함수가 다른 모듈에서 import되는지 확인
```

권장:

- mock path는 실제 import와 일치
- alias 사용 시 테스트도 alias 사용
- API function layer를 mock
- axios instance mock은 필요한 경우에만 사용
- 실제 API 호출 로그가 있으면 mock 미적용 의심

### [FAQ]

Q. mockResolvedValue를 했는데 실제 API가 호출돼.
A. mock path가 실제 Component import path와 다를 가능성이 높다.

Q. alias import를 쓰면 vi.mock도 alias로 써야 해?
A. 실제 import path와 맞추는 것이 안전하다.

Q. named export와 default export를 혼동하면?
A. mock 객체 구조가 실제 export 구조와 달라 적용되지 않을 수 있다.

## 5.2 Mock Response Shape Mismatch

### [개념]

Mock Response Shape Mismatch는 mock 데이터 구조가 실제 API 함수 반환값 또는 Component 기대 구조와 달라 테스트가 실패하는 상황이다.

Frontend 테스트에서는 Backend DTO와 API wrapper 반환 shape를 정확히 구분해야 한다.

### [핵심]

원인:

- array vs page object mismatch
- response.data mismatch
- content field missing
- id vs festivalId
- name vs title
- nullable field missing
- enum value mismatch
- error.response.data mismatch
- fieldErrors mismatch

### [실무]

문제:

```tsx
vi.mocked(getFestivals).mockResolvedValue([{ id: 1, name: "봄꽃 축제" }]);
```

Component 기대:

```tsx
festival.festivalId;
festival.title;
```

개선:

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

Page 응답 mismatch:

```tsx
mockResolvedValue([]);
```

Component 기대:

```tsx
data.content.map(...)
```

개선:

```tsx
mockResolvedValue({
  content: [],
  page: 0,
  size: 10,
  totalElements: 0,
});
```

권장:

- API wrapper가 `response.data`를 반환하는지 전체 response를 반환하는지 확인
- Backend DTO field명과 일치
- Page/Slice 응답 구조 구분
- null 가능 field 포함
- error shape도 실제 handler와 일치

### [FAQ]

Q. mock 데이터가 있는데 화면이 안 떠.
A. mock response shape가 Component가 기대하는 구조와 다른지 확인한다.

Q. API mock에는 response.data까지 넣어야 해?
A. API 함수가 무엇을 반환하는지에 따라 다르다. wrapper가 data를 반환하면 data shape만 넣는다.

Q. id/name으로 mock하면 안 돼?
A. 실제 DTO가 festivalId/title이면 mock도 festivalId/title을 사용해야 한다.

## 5.3 MSW Handler Not Working

### [개념]

MSW Handler Not Working은 MSW handler가 실제 요청을 가로채지 못하는 상황이다.

URL, method, baseURL, query string, trailing slash, server setup을 확인해야 한다.

### [핵심]

원인:

- URL mismatch
- method mismatch
- baseURL mismatch
- absolute URL
- relative URL
- trailing slash
- query param misunderstanding
- server.listen missing
- server.resetHandlers issue
- handler order
- unhandled request

### [실무]

문제:

```ts
http.get("/api/festivals", () => {
  return HttpResponse.json([]);
});
```

실제 요청:

```text
http://localhost:8080/api/festivals
```

환경에 따라 absolute URL handler가 필요할 수 있다.

```ts
http.get("http://localhost:8080/api/festivals", () => {
  return HttpResponse.json([]);
});
```

Debug Flow:

```text
MSW handler 미적용
→ server.listen 실행 확인
→ 실제 request URL 확인
→ handler URL 확인
→ HTTP method 확인
→ baseURL 포함 여부 확인
→ trailing slash 확인
→ unhandled request warning 확인
```

권장:

- MSW unhandled request warning 무시하지 않음
- query string은 handler path보다 request.url로 읽음
- 테스트 환경 baseURL 통일
- 테스트별 override 후 resetHandlers
- handler를 domain별로 관리

### [FAQ]

Q. MSW handler가 요청을 못 잡아.
A. 실제 request URL과 handler URL/method가 일치하는지 확인한다.

Q. query string까지 handler에 써야 해?
A. 보통 path만 매칭하고 query string은 handler 내부에서 URL로 읽는다.

Q. unhandled request warning은 무시해도 돼?
A. 권장하지 않는다. mock 누락이나 URL 불일치 신호다.

# 6. Provider Troubleshooting

## 6.1 Router Provider Missing

### [개념]

Router Provider Missing은 `useNavigate`, `useParams`, `useSearchParams`, `Link`, `NavLink`를 사용하는 Component를 Router 없이 렌더링했을 때 발생하는 문제다.

### [핵심]

오류 원인:

- MemoryRouter missing
- Routes missing
- Route path missing
- useParams without route
- Link outside Router
- useNavigate outside Router
- renderWithRouter not used

### [실무]

문제:

```tsx
render(<FestivalDetailPage />);
```

Component 내부에서 `useParams` 사용 시 실패할 수 있다.

개선:

```tsx
render(
  <MemoryRouter initialEntries={["/festivals/1"]}>
    <Routes>
      <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
    </Routes>
  </MemoryRouter>,
);
```

Debug Flow:

```text
Router 오류
→ Component가 Router Hook 사용 확인
→ MemoryRouter wrapper 확인
→ initialEntries 확인
→ Route path 확인
→ nested route면 Outlet 확인
```

권장:

- Router Hook 사용 Component는 renderWithRouter 사용
- useParams 테스트는 initialEntry와 path 모두 필요
- useNavigate 테스트는 이동 결과 Page UI 검증
- Link는 Router Context 필요

### [FAQ]

Q. useNavigate outside Router 오류는 왜 나?
A. Router Provider 없이 useNavigate를 사용하는 Component를 렌더링했기 때문이다.

Q. useParams 테스트에 MemoryRouter만 있으면 돼?
A. Route path도 필요하다. parameter가 path에서 매칭되어야 한다.

Q. Link만 있는 Component도 Router가 필요해?
A. 필요하다. Link는 Router Context 안에서 동작한다.

## 6.2 QueryClient Provider Missing

### [개념]

QueryClient Provider Missing은 TanStack Query의 `useQuery`나 `useMutation`을 사용하는 Component를 QueryClientProvider 없이 렌더링했을 때 발생한다.

### [핵심]

오류 원인:

- QueryClientProvider missing
- renderWithQueryClient not used
- renderWithProviders missing
- custom hook uses useQuery
- nested component uses useMutation
- Provider order issue

### [실무]

문제:

```tsx
render(<FestivalListPage />);
```

개선:

```tsx
renderWithQueryClient(<FestivalListPage />);
```

또는:

```tsx
const queryClient = createTestQueryClient();

render(
  <QueryClientProvider client={queryClient}>
    <FestivalListPage />
  </QueryClientProvider>,
);
```

Debug Flow:

```text
No QueryClient set
→ Component 또는 child가 useQuery/useMutation 사용 확인
→ QueryClientProvider wrapper 확인
→ render utility 확인
→ 테스트마다 새 QueryClient인지 확인
```

권장:

- Query 사용 Component는 renderWithQueryClient 사용
- Router/Auth도 필요하면 renderWithProviders 사용
- QueryClient는 테스트마다 새로 생성
- retry false 설정

### [FAQ]

Q. No QueryClient set 오류는 왜 나?
A. QueryClientProvider 없이 useQuery/useMutation Component를 렌더링했기 때문이다.

Q. child Component가 useQuery를 써도 Provider가 필요해?
A. 필요하다. 트리 안 어디서든 useQuery를 쓰면 Provider가 필요하다.

Q. QueryClient를 전역으로 재사용해도 돼?
A. 권장하지 않는다. 테스트 간 cache 공유 문제가 생길 수 있다.

## 6.3 Auth Provider State Not Applied

### [개념]

Auth Provider State Not Applied는 테스트에서 설정한 로그인 상태나 사용자 role이 Component에 반영되지 않는 상황이다.

MockAuthProvider, Auth Store, initial state, provider order, storage 상태를 확인해야 한다.

### [핵심]

원인:

- AuthProvider missing
- wrong MockAuthProvider
- initial auth state missing
- authLoading true
- user object missing
- role field mismatch
- storage value conflict
- store not reset
- Provider order issue
- actual auth API call

### [실무]

문제:

```tsx
renderWithProviders(<AdminPage />, {
  authenticated: true,
  user: {
    role: "ADMIN",
  },
});
```

실제 앱은 `ROLE_ADMIN`을 기대할 수 있다.

개선:

```tsx
renderWithProviders(<AdminPage />, {
  authenticated: true,
  user: {
    userId: 1,
    role: "ROLE_ADMIN",
  },
});
```

Debug Flow:

```text
Auth state 미반영
→ AuthProvider 포함 여부 확인
→ authenticated 값 확인
→ authLoading false인지 확인
→ user object 확인
→ role field 이름과 값 확인
→ storage 충돌 확인
→ store reset 확인
```

권장:

- Auth 상태는 render option으로 명확히 주입
- role 이름은 Backend와 통일
- authLoading과 authenticated 구분
- 실제 token 대신 더미 token 사용
- 테스트마다 Auth Store 초기화

### [FAQ]

Q. authenticated true인데 보호 Page가 안 보여.
A. authLoading이 true로 남아 있거나 user 객체/role 값이 잘못되었을 수 있다.

Q. role 테스트가 실패해.
A. 실제 앱이 기대하는 role 값이 `ROLE_ADMIN`인지 `ADMIN`인지 확인한다.

Q. localStorage token을 직접 넣으면 돼?
A. 가능은 하지만 Flow 테스트에서는 MockAuthProvider로 상태를 주입하는 것이 더 명확하다.

# 7. TanStack Query Troubleshooting

## 7.1 Query Retry Causes Slow Test

### [개념]

Query Retry Causes Slow Test는 TanStack Query의 기본 retry 동작 때문에 실패 테스트가 느려지거나 timeout 되는 문제다.

테스트용 QueryClient에서는 retry를 false로 설정한다.

### [핵심]

원인:

- queries retry true
- mutations retry true
- failed query retry delay
- error test slow
- timeout
- flaky test
- default QueryClient used

### [실무]

문제:

```tsx
const queryClient = new QueryClient();
```

개선:

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

Debug Flow:

```text
Query error test 느림
→ Test QueryClient 확인
→ queries retry false 확인
→ mutations retry false 확인
→ 실제 API 호출 여부 확인
→ findBy timeout 확인
```

권장:

- 테스트 QueryClient는 retry false
- 실패 상태 테스트에서 특히 중요
- 전역 QueryClient 재사용 금지
- retry behavior 자체 테스트는 별도로 작성

### [FAQ]

Q. Query Error 테스트가 느려.
A. TanStack Query retry가 켜져 있을 수 있다. 테스트 QueryClient에서 retry false를 설정한다.

Q. mutation에도 retry false가 필요해?
A. 실패 mutation 테스트 안정성을 위해 설정하는 것이 좋다.

Q. retry 기능 자체는 테스트하지 않아?
A. 필요한 경우 별도 테스트로 명확히 작성한다.

## 7.2 Query Cache Leak

### [개념]

Query Cache Leak은 이전 테스트의 Query Cache 데이터가 다음 테스트에 영향을 주는 문제다.

전역 QueryClient 재사용이 대표 원인이다.

### [핵심]

원인:

- global QueryClient
- shared cache
- queryClient not cleared
- same queryKey
- stale data
- previous test data
- test order dependency
- cacheTime/gcTime reliance

### [실무]

문제:

```tsx
const queryClient = createTestQueryClient();

function renderWithQueryClient(ui: React.ReactElement) {
  return render(
    <QueryClientProvider client={queryClient}>{ui}</QueryClientProvider>,
  );
}
```

개선:

```tsx
function renderWithQueryClient(ui: React.ReactElement) {
  const queryClient = createTestQueryClient();

  return render(
    <QueryClientProvider client={queryClient}>{ui}</QueryClientProvider>,
  );
}
```

Debug Flow:

```text
이전 테스트 데이터가 보임
→ QueryClient 전역 재사용 확인
→ 같은 queryKey cache 확인
→ 테스트마다 새 client 생성 확인
→ queryClient.clear 사용 여부 확인
→ mock reset 확인
```

권장:

- 테스트마다 새 QueryClient 생성
- cache seed가 필요한 경우에만 queryClient 반환
- 같은 테스트 안의 관련 Component는 같은 QueryClient 공유
- 테스트 간에는 공유하지 않음

### [FAQ]

Q. 이전 테스트 데이터가 다음 테스트에 보여.
A. QueryClient cache가 공유되고 있을 가능성이 높다.

Q. queryClient.clear를 afterEach에 넣으면 돼?
A. 가능하지만 테스트마다 새 QueryClient를 생성하는 방식이 더 안전하다.

Q. 한 테스트 안에서 QueryClient가 여러 개면?
A. invalidate/refetch가 연결되지 않을 수 있다. 관련 Component는 같은 QueryClient를 사용해야 한다.

## 7.3 invalidateQueries Not Updating UI

### [개념]

invalidateQueries Not Updating UI는 mutation 성공 후 `invalidateQueries`를 호출했지만 화면이 갱신되지 않는 상황이다.

queryKey 불일치, QueryClient 분리, refetch mock 누락이 대표 원인이다.

### [핵심]

원인:

- queryKey mismatch
- wrong invalidation key
- different QueryClient
- refetch mock missing
- mockResolvedValueOnce order wrong
- enabled false
- staleTime issue
- mutation success not reached
- error swallowed

### [실무]

Debug Flow:

```text
invalidate 후 UI 미갱신
→ mutation 성공했는지 확인
→ invalidate queryKey 확인
→ 목록 queryKey와 일치하는지 확인
→ 같은 QueryClient 사용 확인
→ refetch API mock 두 번째 응답 확인
→ findBy로 새 UI 대기
```

테스트 예:

```tsx
vi.mocked(getReviews)
  .mockResolvedValueOnce([])
  .mockResolvedValueOnce([{ reviewId: 1, content: "좋았어요" }]);

vi.mocked(createReview).mockResolvedValue({ reviewId: 1 });

renderWithQueryClient(<ReviewSection festivalId={1} />);

expect(await screen.findByText("아직 리뷰가 없습니다.")).toBeInTheDocument();

await user.click(screen.getByRole("button", { name: "등록" }));

expect(await screen.findByText("좋았어요")).toBeInTheDocument();
```

권장:

- invalidateQueries 호출 spy보다 UI 갱신 결과 검증
- queryKey factory 사용
- 한 테스트 안에서 같은 QueryClient 공유
- refetch 응답 mockResolvedValueOnce 순서 확인

### [FAQ]

Q. invalidateQueries를 했는데 목록이 안 바뀌어.
A. queryKey가 다르거나 같은 QueryClient를 쓰지 않거나 refetch mock 응답이 없을 수 있다.

Q. invalidateQueries 호출 여부를 spy하면 충분해?
A. 부족할 수 있다. 실제 UI가 갱신되는지 확인해야 한다.

Q. refetch mock 응답은 왜 두 번 설정해?
A. 첫 조회와 invalidate 후 재조회의 응답을 다르게 제어하기 위해서다.

# 8. Router Troubleshooting

## 8.1 Route Not Rendering

### [개념]

Route Not Rendering은 MemoryRouter의 `initialEntries`와 Route path가 맞지 않아 기대한 Page가 표시되지 않는 문제다.

Nested Route, index route, dynamic parameter, Outlet 누락도 원인이 된다.

### [핵심]

원인:

- initialEntries mismatch
- route path mismatch
- missing Routes
- wrong dynamic path
- nested route path issue
- Layout missing Outlet
- catch-all route intercept
- basename issue
- auth redirect

### [실무]

문제:

```tsx
<MemoryRouter initialEntries={["/settings/profile"]}>
  <Routes>
    <Route path="/settings" element={<SettingsLayout />}>
      <Route path="/profile" element={<ProfilePage />} />
    </Route>
  </Routes>
</MemoryRouter>
```

중첩 Route에서 child path가 절대 경로가 되어 기대와 다르게 동작할 수 있다.

개선:

```tsx
<Route path="/settings" element={<SettingsLayout />}>
  <Route path="profile" element={<ProfilePage />} />
</Route>
```

Layout 확인:

```tsx
function SettingsLayout() {
  return (
    <main>
      <Outlet />
    </main>
  );
}
```

Debug Flow:

```text
Route 렌더링 실패
→ initialEntries 확인
→ Route path 확인
→ dynamic param 확인
→ nested route relative path 확인
→ Layout Outlet 확인
→ Auth redirect 여부 확인
→ screen.debug 확인
```

### [FAQ]

Q. Route가 테스트에서 렌더링되지 않아.
A. initialEntries와 Route path가 맞는지, nested route 구조와 Outlet이 있는지 확인한다.

Q. Nested Route child path는 slash를 붙여?
A. 보통 중첩 경로에서는 상대 path를 사용한다.

Q. Layout은 보이는데 child page가 안 보여.
A. Layout Component에 `<Outlet />`이 있는지 확인한다.

## 8.2 Redirect Test Failing

### [개념]

Redirect Test Failing은 로그인 redirect, 보호 Route redirect, useNavigate 이동 결과가 기대와 다르게 나타나는 문제다.

Auth 상태, Router Tree, Navigate replace, previous location, async login 결과를 확인해야 한다.

### [핵심]

원인:

- auth state wrong
- authLoading true
- previous location missing
- route tree missing destination
- login API mock missing
- navigate after async not awaited
- wrong default redirect path
- ProtectedRoute condition wrong
- MemoryRouter missing destination route

### [실무]

Debug Flow:

```text
Redirect 실패
→ Auth 상태 확인
→ authLoading 확인
→ 목적지 Route가 테스트에 포함되어 있는지 확인
→ login API mockResolvedValue 확인
→ userEvent await 확인
→ 이동 후 Page UI를 findBy로 기다림
→ previous location state 확인
```

예:

```tsx
await user.click(screen.getByRole("button", { name: "로그인" }));

expect(
  await screen.findByRole("heading", { name: "마이페이지" }),
).toBeInTheDocument();
```

권장:

- redirect 결과는 URL보다 Page UI로 검증
- 목적지 Route를 Route Tree에 포함
- 비동기 로그인 후 이동은 findBy 사용
- authLoading과 authenticated 구분
- previous location 정책 명확화

### [FAQ]

Q. 로그인 후 redirect 테스트가 실패해.
A. login mock, auth state 갱신, 목적지 Route 포함 여부, findBy 대기를 확인한다.

Q. redirect URL을 직접 봐야 해?
A. 일반적으로는 이동 후 Page UI 검증이 우선이다.

Q. 비로그인 보호 Route 테스트가 실패해.
A. authenticated false와 authLoading false가 제대로 설정되었는지 확인한다.

## 8.3 Query String Test Failing

### [개념]

Query String Test Failing은 `useSearchParams` 기반 검색어, 필터, 페이지 번호가 기대대로 반영되지 않는 문제다.

initialEntries, URL encoding, default value, setSearchParams 동작을 확인해야 한다.

### [핵심]

원인:

- initialEntries missing query
- wrong param name
- URL encoding issue
- default value override
- setSearchParams not called
- Form state not synced
- API argument mismatch
- LocationDisplay missing
- router not configured

### [실무]

문제:

```tsx
<MemoryRouter initialEntries={["/festivals"]}>
```

query string 테스트라면:

```tsx
<MemoryRouter initialEntries={["/festivals?keyword=봄꽃&region=seoul"]}>
```

Debug Flow:

```text
Query String 테스트 실패
→ initialEntries에 query 포함 확인
→ param name 확인
→ URL encoding 확인
→ input 초기값 확인
→ API 호출 인자 확인
→ setSearchParams 실행 여부 확인
→ LocationDisplay로 현재 search 확인
```

검증:

```tsx
expect(screen.getByLabelText("검색어")).toHaveValue("봄꽃");
```

API 인자:

```tsx
expect(searchFestivals).toHaveBeenCalledWith(
  expect.objectContaining({
    keyword: "봄꽃",
    region: "seoul",
  }),
);
```

### [FAQ]

Q. query string 값이 input에 안 들어와.
A. initialEntries에 query string이 포함되어 있는지, param 이름이 맞는지 확인한다.

Q. 한글 query string은 문제 없나?
A. 일반적으로 가능하지만 encoding 차이가 있으면 decode 처리와 테스트 입력을 확인해야 한다.

Q. URL 자체를 검증하려면?
A. useLocation 기반 LocationDisplay helper를 사용할 수 있다.

# 9. jsdom and Environment Troubleshooting

## 9.1 Browser API Not Defined

### [개념]

Browser API Not Defined는 jsdom 테스트 환경에 실제 브라우저 API가 없어 발생하는 오류다.

ResizeObserver, IntersectionObserver, matchMedia, scrollTo 등이 대표적이다.

### [핵심]

오류 대상:

- ResizeObserver is not defined
- IntersectionObserver is not defined
- window.matchMedia is not a function
- window.scrollTo is not a function
- URL.createObjectURL missing
- crypto.randomUUID issue
- canvas API missing

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

URL.createObjectURL mock:

```ts
URL.createObjectURL = vi.fn(() => "blob:test-url");
URL.revokeObjectURL = vi.fn();
```

권장:

- setupTests에 공통 browser API mock 추가
- 필요한 API만 mock
- 실제 레이아웃/브라우저 동작 검증은 E2E로 분리
- global mock이 테스트 결과를 왜곡하지 않는지 주의

### [FAQ]

Q. ResizeObserver is not defined는 왜 나?
A. jsdom에 ResizeObserver가 없기 때문이다. 테스트 setup에서 mock해야 한다.

Q. matchMedia 오류는 언제 나?
A. responsive hook이나 UI library가 matchMedia를 사용할 때 발생한다.

Q. 모든 browser API를 mock해야 해?
A. 아니다. 테스트에서 실제로 필요한 API만 mock한다.

## 9.2 Layout Measurement Issue

### [개념]

Layout Measurement Issue는 jsdom이 실제 레이아웃 계산을 하지 않아 `offsetWidth`, `clientHeight`, `getBoundingClientRect` 같은 값이 기대와 다르게 나오는 문제다.

### [핵심]

원인:

- jsdom no real layout
- offsetWidth 0
- clientHeight 0
- getBoundingClientRect default
- scroll position not real
- CSS not computed fully
- virtual DOM limitation
- visual behavior test mismatch

### [실무]

문제 상황:

```text
Tooltip 위치 계산
Dropdown 위치 계산
Virtual list 높이 계산
Carousel width 계산
Responsive layout 계산
```

필요 시 mock:

```ts
element.getBoundingClientRect = vi.fn(() => ({
  width: 200,
  height: 100,
  top: 0,
  left: 0,
  right: 200,
  bottom: 100,
  x: 0,
  y: 0,
  toJSON: () => {},
}));
```

권장:

- 레이아웃 위치 자체는 단위 테스트에서 과도하게 검증하지 않음
- 사용자가 보는 상태나 role을 우선 검증
- 위치/반응형/스크롤 동작은 E2E 또는 visual regression 고려
- 필요한 경우 layout API만 최소 mock

### [FAQ]

Q. jsdom에서 offsetWidth가 0이야.
A. jsdom은 실제 레이아웃을 계산하지 않기 때문에 정상적인 한계다.

Q. Tooltip 위치 테스트는 RTL로 해야 해?
A. 위치 계산 자체보다는 Tooltip 표시 여부와 접근성을 테스트하고, 실제 위치는 E2E/visual test가 적합하다.

Q. getBoundingClientRect를 mock해도 돼?
A. 필요한 경우 가능하지만 테스트 목적을 명확히 해야 한다.

## 9.3 File Upload Preview Issue

### [개념]

File Upload Preview Issue는 파일 업로드 미리보기 테스트에서 `URL.createObjectURL`, FileReader, image load 이벤트가 jsdom 환경에서 실제 브라우저와 다르게 동작하는 문제다.

### [핵심]

원인:

- URL.createObjectURL missing
- FileReader async
- image load not fired
- object URL not revoked
- file type mismatch
- input accept not enforced by jsdom
- preview async rendering

### [실무]

objectURL mock:

```ts
URL.createObjectURL = vi.fn(() => "blob:test-image-url");
URL.revokeObjectURL = vi.fn();
```

테스트:

```tsx
const file = new File(["image"], "festival.png", {
  type: "image/png",
});

await user.upload(screen.getByLabelText("대표 이미지"), file);

expect(await screen.findByAltText("업로드 이미지 미리보기")).toHaveAttribute(
  "src",
  "blob:test-image-url",
);
```

주의:

```text
input accept="image/*"는 브라우저 파일 선택 UI 제약에 가까움
jsdom에서 완전한 차단을 기대하지 말고
컴포넌트 validation 로직을 테스트한다.
```

권장:

- File 객체는 더미 데이터 사용
- createObjectURL mock 필요
- 미리보기는 findBy로 대기
- revokeObjectURL 호출은 필요 시 검증
- 파일 타입/크기 validation은 별도 테스트

### [FAQ]

Q. URL.createObjectURL is not a function 오류는 왜 나?
A. jsdom에 해당 API가 없을 수 있어 setup에서 mock해야 한다.

Q. accept="image/\*"면 텍스트 파일 업로드가 막혀야 해?
A. jsdom에서는 실제 파일 선택 UI 제한이 완전히 재현되지 않을 수 있다. validation 로직을 테스트한다.

Q. 이미지 미리보기는 어떻게 테스트해?
A. createObjectURL을 mock하고 preview 이미지의 alt/src를 검증한다.

# 10. Flaky Test Troubleshooting

## 10.1 Flaky Test Definition

### [개념]

Flaky Test는 코드가 바뀌지 않았는데 실행할 때마다 통과하거나 실패하는 테스트다.

Frontend Flaky Test는 대부분 비동기 대기 누락, 공유 상태, 실제 네트워크, 타이머, 날짜/랜덤 값 의존 때문에 발생한다.

### [핵심]

원인:

- async not awaited
- shared QueryClient
- shared Auth Store
- localStorage leak
- mock not reset
- MSW handler leak
- real API call
- timer dependency
- Date.now dependency
- Math.random dependency
- test order dependency
- CI performance difference

### [실무]

Flaky Debug Flow:

```text
Flaky Test 발생
→ 단독 실행과 전체 실행 비교
→ 테스트 순서 의존 확인
→ shared state 확인
→ mock reset 확인
→ QueryClient cache 확인
→ localStorage/sessionStorage 확인
→ 실제 API 호출 확인
→ 비동기 findBy/waitFor 확인
→ timer/date/random 의존 확인
```

단독 실행은 통과하지만 전체 실행 실패:

```text
테스트 간 상태 공유 가능성 높음
```

전체 실행은 통과하지만 CI 실패:

```text
비동기 대기 누락
환경 API mock 누락
타이밍 의존
timezone/locale 차이 가능성
```

권장:

- 테스트마다 독립 Provider와 QueryClient 생성
- afterEach에서 mock/storage/MSW reset
- 실제 API 호출 금지
- fixed date/random 사용
- userEvent와 async UI는 await 사용

### [FAQ]

Q. Flaky Test는 뭐야?
A. 같은 코드인데 실행할 때마다 통과하거나 실패하는 불안정한 테스트다.

Q. 단독 실행은 되는데 전체 실행에서 실패해.
A. 테스트 간 상태 공유나 mock reset 누락 가능성이 높다.

Q. CI에서만 실패하면?
A. 비동기 대기 누락, 환경 API mock 누락, timezone/locale 차이를 확인한다.

## 10.2 Test Order Dependency

### [개념]

Test Order Dependency는 테스트 실행 순서에 따라 결과가 달라지는 문제다.

전역 상태, storage, cache, mock 구현 공유가 대표 원인이다.

### [핵심]

원인:

- shared variable
- global QueryClient
- Zustand/Redux store not reset
- localStorage not cleared
- mockResolvedValue remains
- MSW override remains
- Date mock not restored
- fake timer not restored
- DOM not cleaned

### [실무]

나쁜 예:

```tsx
let isLoggedIn = false;

test("로그인한다", () => {
  isLoggedIn = true;
});

test("마이페이지를 본다", () => {
  expect(isLoggedIn).toBe(true);
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

Reset 예:

```ts
afterEach(() => {
  vi.clearAllMocks();
  localStorage.clear();
  sessionStorage.clear();
  server.resetHandlers();
});
```

권장:

- 각 테스트가 필요한 상태를 직접 준비
- 테스트 순서에 의존하지 않음
- store reset helper 준비
- Date/fake timer restore
- QueryClient 전역 공유 금지

### [FAQ]

Q. Test Order Dependency는 왜 위험해?
A. 테스트 순서가 바뀌면 결과가 달라져 신뢰할 수 없기 때문이다.

Q. 테스트 간 로그인 상태를 공유해도 돼?
A. 안 된다. 각 테스트에서 인증 상태를 직접 준비해야 한다.

Q. 순서 의존을 없애려면?
A. mock, storage, store, QueryClient, timer를 테스트마다 초기화한다.

## 10.3 Timer and Date Flaky Test

### [개념]

Timer and Date Flaky Test는 setTimeout, debounce, interval, 현재 날짜, timezone에 의존해 불안정해지는 테스트다.

타이머와 날짜는 명시적으로 제어해야 한다.

### [핵심]

원인:

- setTimeout real wait
- debounce delay
- interval not cleared
- Date.now
- new Date
- timezone difference
- locale difference
- fake timer not restored
- userEvent with fake timer issue

### [실무]

날짜 고정:

```ts
expect(formatDate("2026-07-06")).toBe("2026.07.06");
```

Date mock:

```ts
vi.setSystemTime(new Date("2026-07-06T00:00:00Z"));
```

Timer 사용:

```ts
vi.useFakeTimers();

await user.type(screen.getByLabelText("검색어"), "축제");

act(() => {
  vi.runAllTimers();
});

expect(searchFestivals).toHaveBeenCalled();
```

정리:

```ts
afterEach(() => {
  vi.useRealTimers();
});
```

권장:

- 실제 시간 대기 지양
- debounce 테스트는 fake timer 또는 유틸 분리
- Date는 고정 입력 우선
- timezone에 의존하는 expected 값 주의
- fake timer 사용 후 반드시 restore

### [FAQ]

Q. debounce 테스트가 느리고 불안정해.
A. fake timer를 사용하거나 debounce 로직을 별도 테스트로 분리한다.

Q. 날짜 테스트가 CI에서만 실패해.
A. timezone/locale 차이일 수 있다. 고정 입력과 명확한 timezone 처리를 사용한다.

Q. fake timer를 쓰면 항상 좋아?
A. 아니다. userEvent와 충돌할 수 있으므로 필요한 테스트에만 신중히 사용한다.

# 11. Error Message Troubleshooting

## 11.1 Error Message Not Showing

### [개념]

Error Message Not Showing은 validation error, API error, network error를 mock했지만 화면에 오류 메시지가 표시되지 않는 문제다.

validation trigger, error mapping, error shape, async 대기를 확인해야 한다.

### [핵심]

원인:

- validation not triggered
- blur required
- submit not clicked
- userEvent await missing
- mockRejectedValue shape mismatch
- error mapper mismatch
- fieldErrors key mismatch
- error swallowed
- role alert missing
- getBy used instead of findBy

### [실무]

Validation 오류:

```tsx
await user.click(screen.getByRole("button", { name: "로그인" }));

expect(screen.getByText("이메일을 입력해 주세요.")).toBeInTheDocument();
```

Blur validation:

```tsx
await user.type(screen.getByLabelText("이메일"), "wrong-email");
await user.tab();

expect(screen.getByText("올바른 이메일 형식이 아닙니다.")).toBeInTheDocument();
```

API 오류:

```tsx
vi.mocked(login).mockRejectedValue({
  response: {
    status: 401,
  },
});

expect(await screen.findByRole("alert")).toHaveTextContent(
  "이메일 또는 비밀번호가 올바르지 않습니다.",
);
```

Debug Flow:

```text
Error message 안 보임
→ 오류 발생 trigger 확인
→ validation이 submit/blur/change 중 언제인지 확인
→ mockRejectedValue shape 확인
→ error mapper 확인
→ fieldErrors key 확인
→ findBy 사용 확인
```

### [FAQ]

Q. 오류 메시지가 안 보여.
A. 오류를 발생시키는 사용자 행동을 했는지, error shape와 async 대기가 맞는지 확인한다.

Q. blur validation은 어떻게 발생시켜?
A. 입력 후 `await user.tab()`으로 focus를 이동시켜 blur를 발생시킨다.

Q. API error는 왜 findBy가 필요해?
A. API 실패 후 오류 UI가 비동기로 렌더링되기 때문이다.

## 11.2 Wrong Error Message

### [개념]

Wrong Error Message는 오류는 표시되지만 기대한 문구와 다른 문구가 나오는 문제다.

status mapping, field error mapping, fallback 우선순위, i18n key를 확인해야 한다.

### [핵심]

원인:

- wrong status mapping
- fallback message used
- field error not mapped
- server message ignored
- server message exposed
- i18n key mismatch
- validation priority issue
- client validation blocks server call

### [실무]

문제:

```text
기대: 이미 사용 중인 이메일입니다.
실제: 입력값을 확인해 주세요.
```

가능 원인:

```text
fieldErrors.email key가 없음
error.response.data.fieldErrors 구조가 다름
서버 validation mapping 코드가 fallback으로 빠짐
client validation이 먼저 실패해서 API 호출 자체가 안 됨
```

Debug Flow:

```text
Wrong error message
→ 실제 표시 문구 확인
→ mock error status 확인
→ error.response.data 확인
→ fieldErrors key 확인
→ error mapper 우선순위 확인
→ client validation이 먼저 막았는지 확인
```

권장:

- status별 메시지 정책 문서화
- field error와 global error 구분
- 서버 내부 메시지 직접 노출 금지
- 테스트 mock은 실제 error mapper와 맞춤
- client validation과 server validation case 분리

### [FAQ]

Q. 오류 문구가 예상과 달라.
A. status mapping, fieldErrors 구조, fallback message, client validation 우선순위를 확인한다.

Q. 서버 field error 대신 global error가 떠.
A. fieldErrors key나 response shape가 실제 코드와 맞지 않을 수 있다.

Q. 서버 message를 그대로 테스트해야 해?
A. 서비스 정책에 따라 다르지만 보통 사용자 친화적 메시지로 mapping한 결과를 테스트한다.

# 12. Performance and Slow Test Troubleshooting

## 12.1 Slow Test Cause

### [개념]

Slow Test는 테스트 실행 시간이 과도하게 길어 개발 피드백을 늦추는 문제다.

Frontend 테스트에서는 retry, 실제 네트워크, 과도한 waitFor, 큰 render tree, axe 남용, fake timer 미정리가 원인일 수 있다.

### [핵심]

원인:

- TanStack Query retry
- real network call
- long waitFor timeout
- unnecessary full App render
- heavy Provider
- large fixture
- axe overuse
- fake timer issue
- slow user.type for long text
- unhandled promise

### [실무]

Debug Flow:

```text
테스트 느림
→ retry false 확인
→ 실제 API 호출 여부 확인
→ waitFor timeout 확인
→ App 전체 렌더링 여부 확인
→ axe 사용 범위 확인
→ fixture 크기 확인
→ fake timer 정리 확인
```

개선:

```text
필요한 Component만 렌더링
QueryClient retry false
API mock 확실히 적용
긴 user.type 입력 최소화
axe는 주요 대상에만 적용
waitFor 대신 findBy 사용
```

긴 입력 최적화:

```tsx
await user.type(textarea, "좋았어요");
```

매우 긴 본문 입력이 테스트 목적이 아니라면 짧은 대표 문자열 사용.

권장:

- 전체 App render를 남용하지 않음
- 필요한 Provider만 사용
- fixture는 작게 유지
- 실패 테스트 retry false
- axe test 선별 적용

### [FAQ]

Q. Frontend 테스트가 느린 이유는 뭐야?
A. retry, 실제 API 호출, 과도한 waitFor, 큰 렌더링, axe 남용이 흔한 원인이다.

Q. 모든 테스트에서 App 전체를 렌더링해도 돼?
A. 권장하지 않는다. 필요한 Route/Provider만 구성하는 것이 빠르고 명확하다.

Q. axe 테스트가 느리면?
A. 모든 Component가 아니라 주요 Page, Form, Modal 중심으로 선별 적용한다.

## 12.2 Test Timeout

### [개념]

Test Timeout은 테스트가 제한 시간 안에 끝나지 않는 문제다.

해결책은 timeout을 늘리는 것이 아니라 unresolved promise, retry, fake timer, waitFor misuse 원인을 찾는 것이다.

### [핵심]

원인:

- unresolved promise awaited
- pending promise never resolved
- waitFor impossible condition
- TanStack retry
- fake timer not advanced
- fake timer not restored
- real network hang
- userEvent with fake timers
- infinite loop render
- MSW unhandled request

### [실무]

Debug Flow:

```text
Test timeout
→ pending promise를 await하고 있는지 확인
→ waitFor 조건이 가능한지 확인
→ fake timer advance 여부 확인
→ retry false 확인
→ 실제 네트워크 요청 확인
→ infinite render 여부 확인
→ MSW unhandled request 확인
```

pending promise 주의:

```tsx
vi.mocked(getData).mockReturnValue(new Promise(() => {}));

render(<Page />);

expect(screen.getByRole("status")).toBeInTheDocument();
```

위처럼 loading 확인 후 테스트가 끝나야 한다.

나쁜 예:

```tsx
await screen.findByText("데이터");
```

pending promise가 resolve되지 않으므로 timeout 된다.

권장:

- loading test에서는 pending promise 후 loading만 검증
- success test에서는 mockResolvedValue 사용
- timeout 증가 전 원인 분석
- fake timer 사용 후 cleanup
- 실제 API 호출 방지

### [FAQ]

Q. Test timeout이 나면 timeout을 늘리면 돼?
A. 먼저 원인을 찾아야 한다. unresolved promise, retry, waitFor misuse가 흔하다.

Q. pending promise를 쓰면 timeout이 나지 않아?
A. pending 상태만 검증하고 끝내면 괜찮다. resolve될 UI를 기다리면 timeout이 난다.

Q. timeout 원인을 빨리 찾으려면?
A. 실제 API 호출, fake timer, waitFor 조건, retry 설정을 먼저 확인한다.

# 13. Debug Tools

## 13.1 screen.debug

### [개념]

screen.debug는 현재 테스트 DOM을 출력해 실제 렌더링 상태를 확인하는 도구다.

Query 실패, 조건부 렌더링, Provider 누락, mock response 문제를 확인할 때 유용하다.

### [핵심]

- screen.debug
- DOM debug
- current DOM
- testing library debug
- query failure
- conditional rendering
- debug output

### [실무]

기본 사용:

```tsx
render(<LoginForm />);

screen.debug();
```

특정 요소만 출력:

```tsx
const form = screen.getByRole("form", { name: "로그인" });

screen.debug(form);
```

긴 DOM 출력 제한 조정:

```tsx
screen.debug(undefined, 10000);
```

사용 시점:

```text
Query 실패
예상 Page가 아닌 Page가 렌더링됨
ErrorState 대신 Loading이 남아 있음
Mock 데이터가 화면에 안 나옴
Provider fallback이 보임
```

권장:

- 원인 파악용으로 사용
- 최종 테스트 코드에는 불필요한 debug 제거
- debug 출력에서 accessible name이 보이지 않으면 role/name 문제 확인
- 너무 큰 DOM이면 테스트 scope 축소 검토

### [FAQ]

Q. screen.debug는 뭐야?
A. 현재 렌더링된 DOM을 출력해 테스트 상태를 확인하는 도구다.

Q. screen.debug는 최종 코드에 남겨도 돼?
A. 보통 제거하는 것이 좋다. 디버깅 중에만 사용한다.

Q. debug 출력이 너무 길면?
A. 특정 요소만 debug하거나 테스트 scope를 줄인다.

## 13.2 Testing Playground

### [개념]

Testing Playground는 현재 DOM에서 Testing Library가 추천하는 Query를 확인하는 도구다.

Query 실패나 접근성 Query 선택이 어려울 때 유용하다.

### [핵심]

- Testing Playground
- logTestingPlaygroundURL
- recommended query
- accessible query
- role query
- label query
- query suggestion

### [실무]

사용:

```tsx
import { logTestingPlaygroundURL } from "@testing-library/dom";

render(<LoginForm />);

logTestingPlaygroundURL();
```

활용:

```text
현재 DOM 기준 추천 Query 확인
role/name 확인
label 연결 확인
getByText보다 나은 Query 탐색
접근성 문제 발견
```

권장:

- Query 선택이 애매할 때 사용
- 추천 Query가 role/label 중심인지 확인
- testId 추천이 나오면 접근성 구조 부족 가능성 점검
- 최종 테스트 코드에는 로그 제거

### [FAQ]

Q. Testing Playground는 언제 써?
A. 어떤 Query로 요소를 찾아야 할지 애매하거나 getByRole이 실패할 때 사용한다.

Q. Testing Playground가 추천한 Query를 무조건 쓰면 돼?
A. 대부분 좋지만 테스트 의도와 사용자 관점에 맞는지 확인해야 한다.

Q. testId만 추천되면?
A. 접근성 정보가 부족할 수 있으므로 role, label, accessible name 개선을 검토한다.

# 14. Troubleshooting Anti Pattern

## 14.1 Common Troubleshooting Anti Patterns

### [개념]

Troubleshooting Anti Pattern은 테스트 실패 원인을 해결하지 않고 우회하거나 더 불안정한 테스트로 만드는 잘못된 해결 방식이다.

### [핵심]

Anti Pattern:

- getByRole 실패 시 즉시 getByTestId 사용
- 비동기 실패를 무조건 waitFor로 감쌈
- timeout을 무작정 늘림
- act warning을 직접 act로만 덮음
- 실제 API 호출을 허용
- mock shape를 실제 코드와 다르게 맞춤
- Snapshot 업데이트로 실패 무시
- 테스트 순서 의존 방치
- 전역 QueryClient 재사용
- userEvent await 누락 방치
- CI 실패를 rerun으로만 해결
- 접근성 문제를 테스트 수정으로 숨김

### [실무]

나쁜 해결:

```tsx
screen.getByTestId("submit");
```

좋은 해결:

```tsx
screen.getByRole("button", { name: "제출" });
```

나쁜 해결:

```tsx
await waitFor(() => {
  expect(screen.getByText("완료")).toBeInTheDocument();
});
```

좋은 해결:

```tsx
expect(await screen.findByText("완료")).toBeInTheDocument();
```

나쁜 해결:

```text
테스트 timeout을 30초로 늘림
```

좋은 해결:

```text
unresolved promise / retry / 실제 API 호출 / waitFor 조건을 확인함
```

권장:

- 실패 원인을 해결
- 사용자 관점 Query 유지
- async 원인에 맞는 Query 사용
- timeout 증가 전 원인 분석
- 접근성 문제는 Component 개선
- flaky test는 격리와 reset으로 해결

### [FAQ]

Q. 테스트 실패를 빨리 없애려고 testId로 바꾸면 안 돼?
A. 접근성 문제를 숨길 수 있으므로 먼저 role/name/label을 개선해야 한다.

Q. waitFor로 감싸면 안전해져?
A. 아니다. 원인을 숨기고 테스트를 느리게 만들 수 있다.

Q. timeout을 늘리는 건 언제 해?
A. 정말 긴 작업을 의도적으로 테스트할 때만 고려하고, 대부분은 원인 분석이 먼저다.

# 15. Troubleshooting Checklist

## 15.1 Frontend Testing Troubleshooting Checklist

### [개념]

Frontend Testing Troubleshooting Checklist는 테스트 실패 시 원인을 체계적으로 좁히기 위한 점검표다.

### [핵심]

Checklist:

```md
- [ ] 에러 메시지를 끝까지 읽었는가?
- [ ] screen.debug로 현재 DOM을 확인했는가?
- [ ] Query가 사용자 관점 role/name/label 기준인가?
- [ ] getBy / findBy / queryBy 선택이 맞는가?
- [ ] userEvent에 await를 붙였는가?
- [ ] 비동기 UI를 findBy로 기다렸는가?
- [ ] waitFor 안에서 userEvent를 실행하지 않았는가?
- [ ] 필요한 Provider가 모두 있는가?
- [ ] Router initialEntries와 Route path가 맞는가?
- [ ] QueryClientProvider와 retry false가 설정되었는가?
- [ ] Auth state가 명확히 주입되었는가?
- [ ] API mock path가 실제 import path와 일치하는가?
- [ ] mock response shape가 실제 API와 일치하는가?
- [ ] error response shape가 실제 error handler와 일치하는가?
- [ ] MSW handler URL/method가 실제 요청과 일치하는가?
- [ ] QueryClient cache가 테스트 간 공유되지 않는가?
- [ ] localStorage/sessionStorage가 테스트 간 남아 있지 않은가?
- [ ] browser API mock이 필요한가?
- [ ] 날짜/랜덤/타이머 의존이 있는가?
- [ ] timeout을 늘리기 전에 원인을 분석했는가?
```

### [실무]

Agent Troubleshooting Flow:

```text
Receive Failed Test
→ Classify Failure Type
→ Read Error Message
→ Inspect DOM
→ Check Query and Async
→ Check Provider
→ Check Mock
→ Check State Isolation
→ Check jsdom Environment
→ Propose Minimal Fix
→ Review Anti Pattern
```

문제 유형별 우선 점검:

```text
Unable to find role
→ role/name/accessibility

findBy timeout
→ mock/provider/async condition

act warning
→ await userEvent/findBy

No QueryClient set
→ QueryClientProvider

useNavigate error
→ MemoryRouter

mock not applied
→ import path/export structure

CI only failure
→ async/state/timezone/environment
```

### [FAQ]

Q. Troubleshooting Checklist의 핵심은 뭐야?
A. DOM 확인, Query 선택, async 대기, Provider, mock, 상태 격리를 순서대로 점검하는 것이다.

Q. 테스트 실패를 Agent에게 맡길 때 무엇을 주면 좋아?
A. 실패 메시지, 테스트 코드, 대상 Component 코드, 관련 mock/setup 코드를 함께 주면 좋다.

Q. 가장 먼저 고쳐야 하는 문제는?
A. 테스트를 우회하는 것이 아니라 사용자 관점 Query와 Component 접근성/상태 흐름을 먼저 맞춰야 한다.

# 16. Part15 Summary

## 16.1 Troubleshooting Final Rule

### [개념]

Frontend Testing Part15는 Frontend 테스트 실패 원인을 찾고 해결하는 Troubleshooting 기준을 정의한다.

이 Part의 목적은 Agent가 테스트 실패를 무작정 우회하지 않고 Query, Async, Provider, Mock, Environment, State Isolation 기준으로 체계적으로 해결하게 만드는 것이다.

### [핵심]

최종 기준:

- 테스트 실패 시 에러 메시지를 먼저 읽음
- screen.debug로 현재 DOM 확인
- getByRole/getByLabelText 실패는 접근성 문제 가능성으로 판단
- 비동기 UI는 findBy로 대기
- waitFor는 callback/조건 변화에 제한 사용
- waitFor 안에서 userEvent 실행 금지
- act warning은 userEvent await와 findBy 대기부터 확인
- userEvent는 await 사용
- Router Hook은 MemoryRouter 필요
- TanStack Query는 QueryClientProvider 필요
- QueryClient는 테스트마다 새로 생성
- Query retry false 설정
- API mock path는 실제 import와 일치
- mock response shape는 실제 API와 일치
- MSW handler URL/method 일치
- Auth state는 명확히 주입
- jsdom에 없는 browser API는 setup에서 mock
- flaky test는 상태 공유, 비동기, timer, 실제 API 호출을 우선 확인
- timeout 증가보다 원인 분석 우선
- testId, snapshot update, waitFor 남용으로 문제를 숨기지 않음

### [실무]

Agent 작업 Flow:

```text
Test Failure Request
→ Read Error Message
→ Identify Failure Category
→ Inspect DOM
→ Verify Query Strategy
→ Verify Async Waiting
→ Verify Providers
→ Verify Mock Path and Shape
→ Verify State Isolation
→ Verify jsdom Limitations
→ Apply Minimal Fix
→ Explain Root Cause
```

Part16 이후 연결:

```text
Part15 Troubleshooting
→ Part16 Frontend Testing Review
→ Part17 Final Frontend Testing Rules
```

### [FAQ]

Q. Part15의 최종 목적은 뭐야?
A. Frontend Agent가 테스트 실패를 우회하지 않고 원인 기반으로 안정적으로 해결하게 만드는 것이다.

Q. Troubleshooting에서 가장 중요한 규칙은 뭐야?
A. 에러 메시지와 현재 DOM을 확인한 뒤 Query, Async, Provider, Mock 순서로 원인을 좁히는 것이다.

Q. Part15 다음에는 어떤 내용이 이어져야 해?
A. 테스트 코드 리뷰, 품질 검수, 커버리지보다 중요한 기준을 다루는 Frontend Testing Review 기준이 이어지는 것이 좋다.

# Retrieval Queries

### [FAQ]

Q. Frontend Testing Troubleshooting은 뭐야?
A. 테스트 실패 원인을 Query, async, Provider, mock, 환경, 상태 공유 관점에서 찾아 해결하는 기준이다.

Q. 테스트가 실패하면 가장 먼저 뭘 봐야 해?
A. 에러 메시지와 현재 DOM 상태를 확인해야 한다.

Q. screen.debug는 언제 써?
A. 테스트가 찾는 요소가 실제 DOM에 있는지 확인하고 싶을 때 사용한다.

Q. 테스트 실패 원인은 어떤 순서로 봐야 해?
A. Query, Async, Provider, Mock, State Isolation, jsdom 환경 순서로 보는 것이 좋다.

Q. waitFor를 넣으면 대부분 해결돼?
A. 일시적으로 통과할 수 있지만 원인을 숨길 수 있다. 먼저 비동기 여부와 Query를 확인해야 한다.

Q. getByRole이 실패하면 테스트가 잘못된 거야?
A. 테스트 문제일 수도 있지만 Component 접근성 문제가 드러난 것일 수 있다.

Q. 화면에는 버튼이 보이는데 getByRole로 못 찾아.
A. 실제 button이 아니거나 accessible name이 없을 수 있다.

Q. 바로 getByTestId로 바꿔도 돼?
A. 최후 수단이다. 먼저 semantic HTML과 accessible name을 개선한다.

Q. getByText가 실패하면 뭘 확인해?
A. 실제 DOM 텍스트, 비동기 렌더링 여부, mock 응답, 렌더링 조건을 확인한다.

Q. 비동기 텍스트에는 어떤 Query를 써?
A. `findByText` 또는 role이 있으면 `findByRole`을 사용한다.

Q. getByLabelText가 실패하면 뭘 확인해?
A. label의 htmlFor와 input id 연결, aria-label, aria-labelledby를 확인한다.

Q. findBy가 timeout이면 무슨 뜻이야?
A. 기대한 요소가 제한 시간 안에 DOM에 나타나지 않았다는 뜻이다.

Q. findBy timeout에서 가장 먼저 확인할 것은?
A. mock이 적용되었는지, 응답 shape가 맞는지, Component가 실제로 렌더링되었는지 확인한다.

Q. waitFor timeout은 왜 생겨?
A. 기다리는 조건이 실제로 발생하지 않거나 userEvent/mocking/비동기 처리가 잘못되었기 때문이다.

Q. waitFor 안에서 user.click 해도 돼?
A. 권장하지 않는다. user action은 waitFor 밖에서 실행한다.

Q. findBy와 waitFor 중 무엇을 써야 해?
A. 요소가 나타나는 것을 기다리면 findBy, callback이나 조건 변화를 기다리면 waitFor가 적합하다.

Q. act warning은 왜 나?
A. React 상태 업데이트를 테스트가 기다리지 않았기 때문에 발생하는 경우가 많다.

Q. act를 직접 감싸면 해결돼?
A. 가끔 필요하지만 대부분은 userEvent에 await를 붙이고 findBy로 UI 업데이트를 기다리면 해결된다.

Q. user.click 했는데 아무 일도 안 일어나.
A. await 누락, disabled 상태, 잘못된 요소 클릭, handler 누락을 확인한다.

Q. user.type 했는데 값이 안 들어가.
A. controlled component의 value/onChange 연결과 readOnly 여부를 확인한다.

Q. controlled input 테스트에서 값이 안 바뀌어.
A. 부모 state가 onChange 결과로 value를 업데이트하지 않기 때문이다.

Q. wrapper component를 만들어도 돼?
A. 된다. controlled component의 실제 사용 방식을 재현하는 좋은 방법이다.

Q. user.tab 후 focus가 예상과 달라.
A. DOM 순서, focusable 여부, disabled/hidden 상태를 확인한다.

Q. mockResolvedValue를 했는데 실제 API가 호출돼.
A. mock path가 실제 Component import path와 다를 가능성이 높다.

Q. alias import를 쓰면 vi.mock도 alias로 써야 해?
A. 실제 import path와 맞추는 것이 안전하다.

Q. mock 데이터가 있는데 화면이 안 떠.
A. mock response shape가 Component가 기대하는 구조와 다른지 확인한다.

Q. API mock에는 response.data까지 넣어야 해?
A. API 함수가 무엇을 반환하는지에 따라 다르다. wrapper가 data를 반환하면 data shape만 넣는다.

Q. MSW handler가 요청을 못 잡아.
A. 실제 request URL과 handler URL/method가 일치하는지 확인한다.

Q. unhandled request warning은 무시해도 돼?
A. 권장하지 않는다. mock 누락이나 URL 불일치 신호다.

Q. useNavigate outside Router 오류는 왜 나?
A. Router Provider 없이 useNavigate를 사용하는 Component를 렌더링했기 때문이다.

Q. useParams 테스트에 MemoryRouter만 있으면 돼?
A. Route path도 필요하다. parameter가 path에서 매칭되어야 한다.

Q. No QueryClient set 오류는 왜 나?
A. QueryClientProvider 없이 useQuery/useMutation Component를 렌더링했기 때문이다.

Q. authenticated true인데 보호 Page가 안 보여.
A. authLoading이 true로 남아 있거나 user 객체/role 값이 잘못되었을 수 있다.

Q. Query Error 테스트가 느려.
A. TanStack Query retry가 켜져 있을 수 있다. 테스트 QueryClient에서 retry false를 설정한다.

Q. 이전 테스트 데이터가 다음 테스트에 보여.
A. QueryClient cache가 공유되고 있을 가능성이 높다.

Q. invalidateQueries를 했는데 목록이 안 바뀌어.
A. queryKey가 다르거나 같은 QueryClient를 쓰지 않거나 refetch mock 응답이 없을 수 있다.

Q. Route가 테스트에서 렌더링되지 않아.
A. initialEntries와 Route path가 맞는지, nested route 구조와 Outlet이 있는지 확인한다.

Q. 로그인 후 redirect 테스트가 실패해.
A. login mock, auth state 갱신, 목적지 Route 포함 여부, findBy 대기를 확인한다.

Q. query string 값이 input에 안 들어와.
A. initialEntries에 query string이 포함되어 있는지, param 이름이 맞는지 확인한다.

Q. ResizeObserver is not defined는 왜 나?
A. jsdom에 ResizeObserver가 없기 때문이다. 테스트 setup에서 mock해야 한다.

Q. jsdom에서 offsetWidth가 0이야.
A. jsdom은 실제 레이아웃을 계산하지 않기 때문에 정상적인 한계다.

Q. URL.createObjectURL is not a function 오류는 왜 나?
A. jsdom에 해당 API가 없을 수 있어 setup에서 mock해야 한다.

Q. Flaky Test는 뭐야?
A. 같은 코드인데 실행할 때마다 통과하거나 실패하는 불안정한 테스트다.

Q. 단독 실행은 되는데 전체 실행에서 실패해.
A. 테스트 간 상태 공유나 mock reset 누락 가능성이 높다.

Q. CI에서만 실패하면?
A. 비동기 대기 누락, 환경 API mock 누락, timezone/locale 차이를 확인한다.

Q. Test Order Dependency는 왜 위험해?
A. 테스트 순서가 바뀌면 결과가 달라져 신뢰할 수 없기 때문이다.

Q. 날짜 테스트가 CI에서만 실패해.
A. timezone/locale 차이일 수 있다. 고정 입력과 명확한 timezone 처리를 사용한다.

Q. 오류 메시지가 안 보여.
A. 오류를 발생시키는 사용자 행동을 했는지, error shape와 async 대기가 맞는지 확인한다.

Q. 오류 문구가 예상과 달라.
A. status mapping, fieldErrors 구조, fallback message, client validation 우선순위를 확인한다.

Q. Frontend 테스트가 느린 이유는 뭐야?
A. retry, 실제 API 호출, 과도한 waitFor, 큰 렌더링, axe 남용이 흔한 원인이다.

Q. Test timeout이 나면 timeout을 늘리면 돼?
A. 먼저 원인을 찾아야 한다. unresolved promise, retry, waitFor misuse가 흔하다.

Q. screen.debug는 뭐야?
A. 현재 렌더링된 DOM을 출력해 테스트 상태를 확인하는 도구다.

Q. Testing Playground는 언제 써?
A. 어떤 Query로 요소를 찾아야 할지 애매하거나 getByRole이 실패할 때 사용한다.

Q. 테스트 실패를 빨리 없애려고 testId로 바꾸면 안 돼?
A. 접근성 문제를 숨길 수 있으므로 먼저 role/name/label을 개선해야 한다.

Q. Troubleshooting Checklist의 핵심은 뭐야?
A. DOM 확인, Query 선택, async 대기, Provider, mock, 상태 격리를 순서대로 점검하는 것이다.

Q. Part15 Troubleshooting의 최종 목표는 뭐야?
A. Frontend Agent가 테스트 실패를 우회하지 않고 원인 기반으로 안정적으로 해결하게 만드는 것이다.
