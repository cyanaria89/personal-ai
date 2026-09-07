# Frontend Testing Part04 - User Event

---

# 1. User Event Overview

## 1.1 User Event Definition

### [개념]

`userEvent`는 React Testing Library 테스트에서 사용자의 실제 행동에 가까운 이벤트를 시뮬레이션하는 도구다.

사용자가 화면에서 수행하는 클릭, 입력, 선택, 키보드 조작, 파일 업로드, 탭 이동 등을 테스트할 때 사용한다.

---

### [핵심]

- userEvent
- User Interaction
- User Behavior Test
- click
- type
- clear
- selectOptions
- upload
- keyboard
- tab
- hover
- unhover
- async event
- await userEvent
- fireEvent보다 우선
- 실제 사용자 흐름 기반 테스트

---

### [실무]

2026 실무 기준에서 React Component의 사용자 상호작용 테스트는 `fireEvent`보다 `userEvent`를 우선 사용한다.

권장 흐름:

```text
render Component
→ const user = userEvent.setup()
→ screen query로 요소 찾기
→ await user.click / type / selectOptions
→ 화면 결과 검증
```

예:

```tsx
test("검색어를 입력하고 검색 버튼을 누르면 검색 결과를 표시한다", async () => {
  const user = userEvent.setup();

  render(<SearchPage />);

  await user.type(screen.getByLabelText("검색어"), "축제");
  await user.click(screen.getByRole("button", { name: "검색" }));

  expect(await screen.findByText("축제 검색 결과")).toBeInTheDocument();
});
```

---

### [FAQ]

Q. userEvent는 뭐야?
A. 사용자의 클릭, 입력, 선택, 키보드 조작 같은 실제 행동에 가까운 이벤트를 테스트하는 도구다.

Q. userEvent는 언제 써?
A. Button 클릭, Form 입력, Select 선택, Modal 열기, Tab 이동 같은 사용자 상호작용 테스트에 사용한다.

Q. userEvent와 React Testing Library는 같은 거야?
A. 아니다. React Testing Library는 render와 query를 제공하고, userEvent는 사용자 이벤트 시뮬레이션을 담당한다.

---

## 1.2 userEvent First Rule

### [개념]

userEvent First Rule은 일반적인 사용자 상호작용 테스트에서 `fireEvent`보다 `userEvent`를 우선 사용하는 규칙이다.

`userEvent`는 실제 브라우저 사용자 이벤트 흐름에 더 가깝게 동작한다.

---

### [핵심]

userEvent 우선 대상:

- button click
- input typing
- input clear
- checkbox toggle
- radio select
- select option
- file upload
- keyboard navigation
- tab focus movement
- hover interaction

fireEvent 제한 사용:

- low-level DOM event
- custom event
- unsupported userEvent case
- legacy test
- specific event dispatch

---

### [실무]

권장:

```tsx
const user = userEvent.setup();

await user.click(screen.getByRole("button", { name: "저장" }));
```

지양:

```tsx
fireEvent.click(screen.getByRole("button", { name: "저장" }));
```

선택 기준:

```text
사용자가 실제로 할 수 있는 행동인가?
→ userEvent 우선

특정 DOM event만 직접 발생시켜야 하는가?
→ fireEvent 제한 사용
```

---

### [FAQ]

Q. fireEvent 대신 userEvent를 쓰는 이유는 뭐야?
A. userEvent가 실제 사용자 행동과 브라우저 이벤트 흐름에 더 가깝기 때문이다.

Q. fireEvent는 쓰면 안 돼?
A. 아니다. 다만 일반 클릭과 입력은 userEvent를 우선하고, 저수준 이벤트나 특수 상황에 fireEvent를 제한적으로 사용한다.

Q. userEvent만 쓰면 모든 이벤트 테스트가 가능해?
A. 대부분 가능하지만 특수 custom event나 지원되지 않는 저수준 이벤트는 fireEvent가 필요할 수 있다.

---

# 2. userEvent Setup Rules

## 2.1 userEvent.setup

### [개념]

`userEvent.setup()`은 userEvent 인스턴스를 생성하는 권장 방식이다.

각 테스트에서 독립적인 user 인스턴스를 만들고, 이 인스턴스를 통해 클릭, 입력, 키보드 조작을 수행한다.

---

### [핵심]

- userEvent.setup
- user instance
- per test setup
- async user action
- await required
- independent interaction
- stable test
- readable test

---

### [실무]

권장 예:

```tsx
test("로그인 버튼을 클릭한다", async () => {
  const user = userEvent.setup();

  render(<LoginForm />);

  await user.click(screen.getByRole("button", { name: "로그인" }));
});
```

지양 예:

```tsx
userEvent.click(screen.getByRole("button", { name: "로그인" }));
```

권장:

- 테스트마다 `const user = userEvent.setup()` 작성
- 사용자 이벤트 앞에 `await` 사용
- 테스트 흐름을 실제 사용자 행동 순서로 작성
- user 인스턴스를 테스트 간 공유하지 않음

---

### [FAQ]

Q. userEvent.setup은 왜 써?
A. 테스트별 user 인스턴스를 만들고 실제 사용자 이벤트 흐름에 가깝게 동작하도록 하기 위해 사용한다.

Q. userEvent.setup 없이 userEvent.click을 직접 써도 돼?
A. 가능하지만 현대 테스트에서는 setup으로 user 인스턴스를 만들어 사용하는 방식을 권장한다.

Q. user 인스턴스를 여러 테스트에서 공유해도 돼?
A. 권장하지 않는다. 테스트 독립성을 위해 각 테스트에서 새로 생성하는 것이 좋다.

---

## 2.2 Await User Event Rule

### [개념]

Await User Event Rule은 `userEvent`로 수행하는 사용자 행동 앞에 `await`를 붙이는 규칙이다.

`userEvent`는 실제 이벤트 흐름을 비동기로 처리할 수 있으므로 `await`를 사용하는 것이 안전하다.

---

### [핵심]

await 필요 대상:

- await user.click
- await user.type
- await user.clear
- await user.selectOptions
- await user.upload
- await user.keyboard
- await user.tab
- await user.hover
- await user.unhover

---

### [실무]

권장 예:

```tsx
const user = userEvent.setup();

await user.type(screen.getByLabelText("이메일"), "test@example.com");
await user.click(screen.getByRole("button", { name: "로그인" }));

expect(await screen.findByText("로그인 성공")).toBeInTheDocument();
```

지양 예:

```tsx
user.type(screen.getByLabelText("이메일"), "test@example.com");
user.click(screen.getByRole("button", { name: "로그인" }));
```

await 누락 시 문제:

```text
상태 업데이트 완료 전 assertion 실행
→ act warning 발생
→ 테스트 간헐 실패
→ 입력값 반영 누락
→ 비동기 UI 검증 실패
```

---

### [FAQ]

Q. userEvent에는 왜 await가 필요해?
A. userEvent가 실제 이벤트 흐름을 비동기로 처리할 수 있어 상태 업데이트를 안전하게 기다리기 위해 필요하다.

Q. click도 await 해야 해?
A. 권장한다. click 이후 state update, validation, API call, route change가 발생할 수 있기 때문이다.

Q. await를 빼도 테스트가 통과하면 괜찮아?
A. 통과할 수는 있지만 불안정해질 수 있다. 일관되게 await를 사용하는 것이 좋다.

---

# 3. Click Event Rules

## 3.1 Button Click Test

### [개념]

Button Click Test는 사용자가 버튼을 클릭했을 때 callback 호출, UI 상태 변화, API 요청, Routing 결과가 정상 동작하는지 검증하는 테스트다.

버튼은 `getByRole("button", { name })`으로 찾고 `await user.click`으로 클릭한다.

---

### [핵심]

- button click
- user.click
- getByRole button
- accessible name
- callback
- submit
- modal open
- modal close
- route navigation
- disabled state
- loading state
- result assertion

---

### [실무]

기본 예:

```tsx
test("저장 버튼을 클릭하면 저장 완료 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  render(<ProfileForm />);

  await user.click(screen.getByRole("button", { name: "저장" }));

  expect(await screen.findByText("저장되었습니다.")).toBeInTheDocument();
});
```

callback 검증:

```tsx
test("닫기 버튼을 클릭하면 onClose가 호출된다", async () => {
  const user = userEvent.setup();
  const onClose = vi.fn();

  render(<Modal onClose={onClose} />);

  await user.click(screen.getByRole("button", { name: "닫기" }));

  expect(onClose).toHaveBeenCalledTimes(1);
});
```

권장:

- 버튼은 role과 accessible name으로 찾음
- 클릭 후 사용자에게 보이는 결과 검증
- callback만 검증할 경우 callback 목적이 명확해야 함
- disabled 버튼 클릭 결과도 필요 시 검증
- loading 중 중복 클릭 방지 테스트 가능

---

### [FAQ]

Q. 버튼 클릭은 어떻게 테스트해?
A. `getByRole("button", { name: "..." })`으로 버튼을 찾고 `await user.click`으로 클릭한다.

Q. 버튼 클릭 후 함수 호출만 확인하면 돼?
A. 단순 presentational component는 가능하지만 핵심 흐름에서는 사용자에게 보이는 결과까지 검증하는 것이 좋다.

Q. 아이콘 버튼은 어떻게 클릭 테스트해?
A. 버튼에 `aria-label`을 제공하고 `getByRole("button", { name: "검색" })`으로 찾는다.

---

## 3.2 Disabled Button Click Test

### [개념]

Disabled Button Click Test는 버튼이 비활성화 상태일 때 사용자가 클릭해도 submit, API 요청, callback이 실행되지 않는지 검증하는 테스트다.

---

### [핵심]

- disabled button
- toBeDisabled
- user.click
- not called
- duplicate submit prevention
- loading disabled
- invalid form
- permission disabled

---

### [실무]

예:

```tsx
test("필수 입력값이 없으면 저장 버튼이 비활성화된다", async () => {
  const user = userEvent.setup();
  const onSubmit = vi.fn();

  render(<ReviewForm onSubmit={onSubmit} />);

  const button = screen.getByRole("button", { name: "등록" });

  expect(button).toBeDisabled();

  await user.click(button);

  expect(onSubmit).not.toHaveBeenCalled();
});
```

Loading 중 중복 클릭 방지:

```tsx
test("요청 중에는 제출 버튼을 비활성화한다", async () => {
  const user = userEvent.setup();

  render(<LoginForm onLogin={() => new Promise(() => {})} />);

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "password123");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(screen.getByRole("button", { name: "처리 중..." })).toBeDisabled();
});
```

---

### [FAQ]

Q. disabled 버튼도 클릭 테스트해야 해?
A. 중복 제출 방지나 권한 제어가 중요한 경우 테스트하는 것이 좋다.

Q. disabled 버튼 클릭 후 뭘 확인해?
A. callback이나 API 요청이 실행되지 않았는지 확인한다.

Q. loading 중 버튼 disabled는 왜 중요해?
A. 중복 제출과 중복 API 요청을 막기 위해 중요하다.

---

# 4. Type and Clear Rules

## 4.1 Input Type Test

### [개념]

Input Type Test는 사용자가 input 또는 textarea에 값을 입력했을 때 값이 반영되고 이후 제출이나 검증 흐름에 사용되는지 확인하는 테스트다.

`user.type`은 실제 사용자가 타이핑하는 흐름을 시뮬레이션한다.

---

### [핵심]

- user.type
- text input
- email input
- password input
- textarea
- getByLabelText
- toHaveValue
- getByDisplayValue
- controlled input
- form submit
- validation

---

### [실무]

입력값 검증:

```tsx
test("검색어를 입력하면 입력값이 반영된다", async () => {
  const user = userEvent.setup();

  render(<SearchForm />);

  await user.type(screen.getByLabelText("검색어"), "봄꽃");

  expect(screen.getByLabelText("검색어")).toHaveValue("봄꽃");
});
```

Form submit 검증:

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

권장:

- Form 요소는 label 기반 Query로 찾음
- user.type에는 await 사용
- password 값은 실제 비밀번호 사용 금지
- 입력 결과는 `toHaveValue` 또는 submit 결과로 검증
- 복잡한 Form은 validation / submit 결과까지 함께 검증

---

### [FAQ]

Q. input 입력 테스트는 어떻게 해?
A. `await user.type(screen.getByLabelText("이메일"), "test@example.com")`처럼 작성한다.

Q. 입력값 반영은 어떻게 확인해?
A. `toHaveValue` 또는 `getByDisplayValue`로 확인한다.

Q. password 입력 테스트에 실제 비밀번호를 써도 돼?
A. 안 된다. 테스트용 더미 값을 사용한다.

---

## 4.2 Clear Input Test

### [개념]

Clear Input Test는 사용자가 입력값을 지웠을 때 input 값이 비워지고 관련 UI 또는 validation 상태가 올바르게 바뀌는지 검증하는 테스트다.

`user.clear`를 사용한다.

---

### [핵심]

- user.clear
- input clear
- textarea clear
- empty value
- validation message
- required error
- search reset
- form edit
- controlled input

---

### [실무]

예:

```tsx
test("입력값을 지우면 검색어가 비워진다", async () => {
  const user = userEvent.setup();

  render(<SearchForm initialKeyword="축제" />);

  const input = screen.getByLabelText("검색어");

  expect(input).toHaveValue("축제");

  await user.clear(input);

  expect(input).toHaveValue("");
});
```

Validation 연계:

```tsx
test("필수 입력값을 지우고 제출하면 오류 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  render(<ReviewForm initialContent="좋았어요" />);

  await user.clear(screen.getByLabelText("리뷰 내용"));
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(screen.getByText("리뷰 내용을 입력해 주세요.")).toBeInTheDocument();
});
```

권장:

- 수정 Form 초기값 제거 테스트
- 검색어 reset 테스트
- required validation과 함께 테스트
- clear 이후 submit 결과 검증

---

### [FAQ]

Q. input 값을 지우는 테스트는 어떻게 해?
A. `await user.clear(input)`을 사용한다.

Q. clear 후 뭘 검증해야 해?
A. input 값이 빈 문자열인지, 필요하면 validation 메시지가 표시되는지 확인한다.

Q. clear도 await 해야 해?
A. 권장한다. userEvent 동작은 await를 사용하는 것이 안전하다.

---

# 5. Checkbox and Radio Rules

## 5.1 Checkbox Test

### [개념]

Checkbox Test는 사용자가 checkbox를 선택하거나 해제했을 때 checked 상태와 관련 UI가 올바르게 변경되는지 검증하는 테스트다.

---

### [핵심]

- checkbox
- user.click
- getByRole checkbox
- getByLabelText
- toBeChecked
- not.toBeChecked
- toggle
- agreement
- filter option
- multi select

---

### [실무]

예:

```tsx
test("약관 동의 체크박스를 선택한다", async () => {
  const user = userEvent.setup();

  render(<TermsForm />);

  const checkbox = screen.getByRole("checkbox", { name: "약관 동의" });

  expect(checkbox).not.toBeChecked();

  await user.click(checkbox);

  expect(checkbox).toBeChecked();
});
```

필터 체크박스 예:

```tsx
test("지역 필터를 선택하면 선택된 필터를 표시한다", async () => {
  const user = userEvent.setup();

  render(<FestivalFilter />);

  await user.click(screen.getByRole("checkbox", { name: "서울" }));

  expect(screen.getByRole("checkbox", { name: "서울" })).toBeChecked();
  expect(screen.getByText("서울 선택됨")).toBeInTheDocument();
});
```

권장:

- checkbox는 label 또는 role name으로 찾음
- checked 상태는 `toBeChecked` 사용
- 선택 후 사용자 결과도 함께 검증
- 전체 동의 / 부분 동의 흐름은 별도 테스트

---

### [FAQ]

Q. checkbox는 어떻게 테스트해?
A. `getByRole("checkbox", { name })`로 찾고 `await user.click` 후 `toBeChecked`로 검증한다.

Q. checkbox label이 없으면 어떻게 해?
A. label이나 aria-label을 추가하는 것이 좋다.

Q. checkbox 선택 후 상태만 확인하면 돼?
A. 필터나 약관처럼 UI 결과가 있다면 선택 결과 화면도 함께 검증한다.

---

## 5.2 Radio Test

### [개념]

Radio Test는 사용자가 여러 선택지 중 하나를 선택했을 때 선택 상태가 올바르게 변경되는지 검증하는 테스트다.

Radio Group은 label과 group 의미가 명확해야 한다.

---

### [핵심]

- radio
- radio group
- user.click
- getByRole radio
- toBeChecked
- exclusive selection
- option select
- form value
- accessibility

---

### [실무]

예:

```tsx
test("공개 범위를 선택한다", async () => {
  const user = userEvent.setup();

  render(<VisibilityForm />);

  const publicOption = screen.getByRole("radio", { name: "공개" });
  const privateOption = screen.getByRole("radio", { name: "비공개" });

  await user.click(privateOption);

  expect(privateOption).toBeChecked();
  expect(publicOption).not.toBeChecked();
});
```

Form submit 연계:

```tsx
test("선택한 평점을 제출한다", async () => {
  const user = userEvent.setup();
  const onSubmit = vi.fn();

  render(<RatingForm onSubmit={onSubmit} />);

  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(onSubmit).toHaveBeenCalledWith({
    rating: 5,
  });
});
```

권장:

- radio는 `getByRole("radio", { name })` 사용
- 선택된 radio와 선택 해제된 radio 모두 검증 가능
- submit 값 검증 포함
- radio group label 접근성 검토

---

### [FAQ]

Q. radio는 어떻게 테스트해?
A. `getByRole("radio", { name })`로 선택지를 찾고 `await user.click` 후 `toBeChecked`로 검증한다.

Q. radio는 checkbox와 뭐가 달라?
A. checkbox는 여러 개 선택 가능하고 radio는 같은 그룹에서 하나만 선택된다.

Q. radio 선택 후 submit 값도 확인해야 해?
A. Form 흐름에서는 선택 값이 submit 결과에 반영되는지 확인하는 것이 좋다.

---

# 6. Select and Option Rules

## 6.1 Select Option Test

### [개념]

Select Option Test는 사용자가 select box에서 option을 선택했을 때 선택 값과 관련 UI 결과가 올바르게 변경되는지 검증하는 테스트다.

`user.selectOptions`를 사용한다.

---

### [핵심]

- selectOptions
- select
- option
- combobox
- listbox
- getByRole combobox
- selected option
- toHaveValue
- filter select
- region select
- category select

---

### [실무]

예:

```tsx
test("지역을 선택하면 선택값이 반영된다", async () => {
  const user = userEvent.setup();

  render(<RegionSelect />);

  await user.selectOptions(
    screen.getByRole("combobox", { name: "지역 선택" }),
    "seoul",
  );

  expect(screen.getByRole("combobox", { name: "지역 선택" })).toHaveValue(
    "seoul",
  );
});
```

선택된 option 검증:

```tsx
expect(screen.getByRole("option", { name: "서울" })).toBeSelected();
```

검색 필터 연계:

```tsx
test("카테고리를 선택하면 해당 카테고리 축제를 표시한다", async () => {
  const user = userEvent.setup();

  render(<FestivalSearchPage />);

  await user.selectOptions(
    screen.getByRole("combobox", { name: "카테고리" }),
    "music",
  );

  expect(await screen.findByText("음악 축제")).toBeInTheDocument();
});
```

---

### [FAQ]

Q. select는 어떻게 테스트해?
A. `await user.selectOptions(selectElement, value)`로 option을 선택하고 `toHaveValue`로 확인한다.

Q. select는 어떤 role로 찾아?
A. 일반 select는 보통 `combobox` role로 찾는다.

Q. option이 선택되었는지 어떻게 확인해?
A. option 요소에 `toBeSelected` matcher를 사용할 수 있다.

---

## 6.2 Multi Select Test

### [개념]

Multi Select Test는 사용자가 여러 option을 선택할 수 있는 select 또는 custom multi-select UI를 검증하는 테스트다.

Native multiple select는 `user.selectOptions`에 여러 값을 전달할 수 있다.

---

### [핵심]

- multi select
- multiple option
- selectOptions array
- selected options
- filter chips
- custom select
- combobox
- listbox
- option
- aria-selected

---

### [실무]

Native multiple select 예:

```tsx
test("여러 테마를 선택한다", async () => {
  const user = userEvent.setup();

  render(<ThemeMultiSelect />);

  await user.selectOptions(screen.getByLabelText("테마 선택"), [
    "flower",
    "music",
  ]);

  expect(screen.getByRole("option", { name: "꽃" })).toBeSelected();
  expect(screen.getByRole("option", { name: "음악" })).toBeSelected();
});
```

Custom multi-select 기준:

```text
combobox 클릭
→ option 선택
→ selected chip 표시
→ aria-selected 또는 화면 결과 검증
```

권장:

- Native select와 custom select 구분
- custom select는 실제 사용자 클릭 흐름 테스트
- 선택 결과 chip, tag, filter result 검증
- 접근성 role 확인

---

### [FAQ]

Q. multiple select는 어떻게 테스트해?
A. `user.selectOptions`에 여러 값을 배열로 전달한다.

Q. custom select도 selectOptions를 써?
A. native select가 아니라면 실제 사용자처럼 combobox를 열고 option을 클릭하는 방식으로 테스트한다.

Q. multi-select 결과는 뭘 확인해?
A. 선택된 option, 표시되는 chip/tag, 필터 결과를 확인한다.

---

# 7. Keyboard and Tab Rules

## 7.1 Keyboard Test

### [개념]

Keyboard Test는 사용자가 키보드로 입력, 제출, 이동, 단축키, Escape 닫기 등을 수행하는 흐름을 검증하는 테스트다.

`user.keyboard`를 사용한다.

---

### [핵심]

- keyboard
- user.keyboard
- Enter
- Escape
- Space
- ArrowDown
- ArrowUp
- Tab
- shortcut
- submit by Enter
- close by Escape
- accessible interaction

---

### [실무]

Enter submit 예:

```tsx
test("Enter 키로 검색을 실행한다", async () => {
  const user = userEvent.setup();

  render(<SearchForm />);

  await user.type(screen.getByLabelText("검색어"), "축제");
  await user.keyboard("{Enter}");

  expect(await screen.findByText("검색 결과")).toBeInTheDocument();
});
```

Escape 닫기 예:

```tsx
test("Escape 키를 누르면 모달이 닫힌다", async () => {
  const user = userEvent.setup();

  render(<NoticeModal defaultOpen />);

  expect(screen.getByRole("dialog")).toBeInTheDocument();

  await user.keyboard("{Escape}");

  expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
});
```

권장:

- 키보드 접근성이 중요한 UI 테스트
- Modal, Dropdown, Combobox, Menu, Tab UI에 중요
- keyboard 이후 focus / UI 결과 검증
- click만 테스트하지 않고 keyboard 흐름도 핵심 UI에 포함

---

### [FAQ]

Q. keyboard 테스트는 언제 필요해?
A. Enter 제출, Escape 닫기, Dropdown 이동, Modal 닫기처럼 키보드 사용성이 중요한 UI에 필요하다.

Q. Enter 키는 어떻게 테스트해?
A. `await user.keyboard("{Enter}")`를 사용한다.

Q. Escape로 Modal 닫기는 테스트해야 해?
A. 접근성과 사용자 경험에 중요한 Modal이라면 테스트하는 것이 좋다.

---

## 7.2 Tab Focus Test

### [개념]

Tab Focus Test는 사용자가 Tab 키로 포커스를 이동할 때 Focus 순서와 접근 가능한 조작 흐름이 올바른지 검증하는 테스트다.

`user.tab`과 `toHaveFocus`를 사용한다.

---

### [핵심]

- user.tab
- focus order
- toHaveFocus
- keyboard navigation
- accessibility
- focus trap
- modal focus
- form focus
- interactive elements
- skip hidden element

---

### [실무]

Form focus 예:

```tsx
test("Tab 키로 로그인 Form을 순서대로 이동한다", async () => {
  const user = userEvent.setup();

  render(<LoginForm />);

  await user.tab();
  expect(screen.getByLabelText("이메일")).toHaveFocus();

  await user.tab();
  expect(screen.getByLabelText("비밀번호")).toHaveFocus();

  await user.tab();
  expect(screen.getByRole("button", { name: "로그인" })).toHaveFocus();
});
```

Modal focus trap 예:

```tsx
test("모달 내부에서 Tab 포커스가 유지된다", async () => {
  const user = userEvent.setup();

  render(<ConfirmModal open />);

  await user.tab();
  expect(screen.getByRole("button", { name: "확인" })).toHaveFocus();
});
```

권장:

- Form, Modal, Dropdown, Navigation에 적용
- focus order가 사용자 흐름과 맞는지 확인
- disabled 요소는 focus되지 않아야 함
- Modal은 focus trap 검토

---

### [FAQ]

Q. Tab 이동은 어떻게 테스트해?
A. `await user.tab()`을 사용하고 `toHaveFocus`로 현재 포커스 요소를 확인한다.

Q. focus 테스트는 꼭 해야 해?
A. 모든 Component에 필수는 아니지만 Form, Modal, Dropdown처럼 키보드 접근성이 중요한 UI에는 유용하다.

Q. disabled 버튼은 Tab으로 focus돼?
A. 일반적으로 disabled 요소는 focus되지 않아야 한다.

---

# 8. Hover and Pointer Rules

## 8.1 Hover Test

### [개념]

Hover Test는 사용자가 특정 요소에 마우스를 올렸을 때 tooltip, menu, preview 같은 UI가 표시되는지 검증하는 테스트다.

`user.hover`와 `user.unhover`를 사용한다.

---

### [핵심]

- hover
- unhover
- tooltip
- popover
- menu
- preview
- pointer interaction
- visible result
- hidden result
- accessibility caution

---

### [실무]

Tooltip 예:

```tsx
test("도움말 아이콘에 hover하면 tooltip을 표시한다", async () => {
  const user = userEvent.setup();

  render(<HelpTooltip />);

  await user.hover(screen.getByRole("button", { name: "도움말" }));

  expect(screen.getByRole("tooltip")).toBeInTheDocument();

  await user.unhover(screen.getByRole("button", { name: "도움말" }));

  expect(screen.queryByRole("tooltip")).not.toBeInTheDocument();
});
```

권장:

- hover 후 표시되는 UI 검증
- unhover 후 사라지는 UI 검증
- tooltip은 keyboard focus로도 접근 가능한지 검토
- hover-only UI는 모바일 / 접근성 이슈 검토

---

### [FAQ]

Q. hover 테스트는 어떻게 해?
A. `await user.hover(element)`를 사용하고 hover 결과 UI를 검증한다.

Q. unhover도 테스트해야 해?
A. tooltip이나 popover가 사라져야 하는 UI라면 테스트하는 것이 좋다.

Q. hover-only UI는 괜찮아?
A. 접근성과 모바일 사용성 문제가 있을 수 있어 focus나 click 대안도 고려해야 한다.

---

# 9. File Upload Rules

## 9.1 File Upload Test

### [개념]

File Upload Test는 사용자가 파일 input에 파일을 업로드했을 때 파일 값, 미리보기, validation, submit 결과가 올바르게 동작하는지 검증하는 테스트다.

`user.upload`를 사용한다.

---

### [핵심]

- user.upload
- file input
- File object
- image upload
- preview
- file size validation
- file type validation
- multiple files
- form submit
- test file security

---

### [실무]

기본 예:

```tsx
test("이미지 파일을 업로드한다", async () => {
  const user = userEvent.setup();

  render(<ImageUploadForm />);

  const file = new File(["image"], "festival.png", {
    type: "image/png",
  });

  const input = screen.getByLabelText("대표 이미지");

  await user.upload(input, file);

  expect(input.files?.[0]).toBe(file);
  expect(input.files).toHaveLength(1);
});
```

미리보기 검증:

```tsx
expect(
  await screen.findByAltText("업로드 이미지 미리보기"),
).toBeInTheDocument();
```

Validation 예:

```tsx
test("허용되지 않는 파일 형식이면 오류 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  render(<ImageUploadForm />);

  const file = new File(["text"], "memo.txt", {
    type: "text/plain",
  });

  await user.upload(screen.getByLabelText("대표 이미지"), file);

  expect(
    screen.getByText("이미지 파일만 업로드할 수 있습니다."),
  ).toBeInTheDocument();
});
```

권장:

- 더미 File 객체 사용
- 실제 개인정보 포함 파일 사용 금지
- 파일 형식 / 크기 validation 테스트
- preview UI가 있으면 사용자 결과 검증
- multiple file은 파일 개수와 목록 표시 검증

---

### [FAQ]

Q. 파일 업로드 테스트는 어떻게 해?
A. `new File()`로 더미 파일을 만들고 `await user.upload(input, file)`을 사용한다.

Q. 실제 파일을 테스트에 넣어도 돼?
A. 가능하면 더미 File 객체를 사용하고 실제 개인정보나 민감 파일은 사용하지 않는다.

Q. 업로드 후 뭘 검증해야 해?
A. input files, 미리보기, 파일명 표시, validation 메시지, submit 결과를 검증한다.

---

# 10. Form Submit Interaction Rules

## 10.1 Submit by Button

### [개념]

Submit by Button은 사용자가 Form 입력 후 제출 버튼을 클릭해 Form submit이 실행되는 흐름을 검증하는 테스트다.

사용자 입력, validation, submit callback, API 상태, 성공 / 실패 UI를 함께 검증한다.

---

### [핵심]

- form submit
- user.type
- user.click
- submit button
- validation
- onSubmit
- API mutation
- loading state
- success state
- error state
- duplicate submit prevention

---

### [실무]

예:

```tsx
test("리뷰 내용을 입력하고 등록하면 성공 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  mockCreateReviewSuccess();

  render(<ReviewForm />);

  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(await screen.findByText("리뷰가 등록되었습니다.")).toBeInTheDocument();
});
```

Validation 실패:

```tsx
test("리뷰 내용이 비어 있으면 오류 메시지를 표시한다", async () => {
  const user = userEvent.setup();
  const onSubmit = vi.fn();

  render(<ReviewForm onSubmit={onSubmit} />);

  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(screen.getByText("리뷰 내용을 입력해 주세요.")).toBeInTheDocument();
  expect(onSubmit).not.toHaveBeenCalled();
});
```

권장:

- 실제 사용자 입력 순서로 작성
- submit 전 validation 확인
- submit 중 loading / disabled 확인
- 성공 / 실패 메시지 검증
- API mutation은 mock으로 제어

---

### [FAQ]

Q. Form submit 테스트는 어떻게 해?
A. userEvent로 입력하고 제출 버튼을 클릭한 뒤 submit 결과 UI 또는 callback 값을 검증한다.

Q. validation 실패 시 뭘 확인해?
A. 오류 메시지가 표시되고 submit callback이나 API 요청이 실행되지 않는지 확인한다.

Q. submit 성공 후 함수 호출만 확인하면 돼?
A. 가능하면 성공 메시지, redirect, form reset, 목록 갱신 같은 사용자 결과까지 검증한다.

---

## 10.2 Submit by Enter

### [개념]

Submit by Enter는 사용자가 입력창에서 Enter 키를 눌러 Form을 제출하는 흐름을 검증하는 테스트다.

검색 Form, 로그인 Form, 단일 입력 Form에서 자주 사용한다.

---

### [핵심]

- submit by Enter
- user.keyboard
- Enter
- search form
- login form
- input focus
- form submit
- keyboard accessibility

---

### [실무]

검색 예:

```tsx
test("검색어 입력 후 Enter 키로 검색한다", async () => {
  const user = userEvent.setup();

  render(<SearchForm />);

  await user.type(screen.getByLabelText("검색어"), "축제");
  await user.keyboard("{Enter}");

  expect(await screen.findByText("검색 결과")).toBeInTheDocument();
});
```

로그인 예:

```tsx
test("비밀번호 입력 후 Enter 키로 로그인한다", async () => {
  const user = userEvent.setup();

  mockLoginSuccess();

  render(<LoginForm />);

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "password123");
  await user.keyboard("{Enter}");

  expect(await screen.findByText("로그인 성공")).toBeInTheDocument();
});
```

권장:

- 검색 / 로그인처럼 Enter 제출이 자연스러운 Form에 적용
- button click submit과 별도 테스트 가능
- focus가 적절한 input에 있는지 고려
- textarea에서는 Enter 동작이 제출이 아닐 수 있음

---

### [FAQ]

Q. Enter로 submit하는 테스트는 어떻게 해?
A. 입력 후 `await user.keyboard("{Enter}")`를 사용한다.

Q. 모든 Form에서 Enter submit을 테스트해야 해?
A. 필수는 아니다. 검색, 로그인처럼 Enter 제출이 중요한 Form에 우선 적용한다.

Q. textarea에서 Enter는 submit이야?
A. 보통 줄바꿈일 수 있다. Form 설계에 따라 다르므로 사용자 동작 기준으로 테스트한다.

---

# 11. fireEvent Rules

## 11.1 fireEvent Definition

### [개념]

`fireEvent`는 특정 DOM event를 직접 발생시키는 저수준 테스트 유틸리티다.

대부분의 사용자 상호작용 테스트에서는 `userEvent`를 우선하고, `fireEvent`는 제한적으로 사용한다.

---

### [핵심]

- fireEvent
- low-level event
- DOM event
- change event
- submit event
- scroll event
- resize event
- custom event
- legacy test
- userEvent first

---

### [실무]

사용 가능 예:

```tsx
fireEvent.scroll(window, {
  target: { scrollY: 500 },
});
```

change event 직접 발생:

```tsx
fireEvent.change(input, {
  target: { value: "축제" },
});
```

하지만 일반 입력은 userEvent 우선:

```tsx
await user.type(screen.getByLabelText("검색어"), "축제");
```

사용 기준:

```text
사용자가 실제 행동으로 표현 가능
→ userEvent

특정 DOM event를 직접 발생시켜야 함
→ fireEvent
```

---

### [FAQ]

Q. fireEvent는 뭐야?
A. 특정 DOM event를 직접 발생시키는 저수준 테스트 유틸리티다.

Q. fireEvent는 언제 써?
A. userEvent로 표현하기 어려운 custom event, scroll, resize 같은 저수준 이벤트에 제한적으로 사용한다.

Q. input change에 fireEvent를 써도 돼?
A. 가능하지만 일반 사용자 입력은 userEvent.type이 더 권장된다.

---

## 11.2 fireEvent Caution

### [개념]

fireEvent는 단일 DOM event를 직접 발생시키기 때문에 실제 사용자 행동과 브라우저 이벤트 흐름을 충분히 반영하지 못할 수 있다.

따라서 일반 사용자 상호작용에는 남용하지 않는다.

---

### [핵심]

주의 대상:

- click에 fireEvent 남용
- type에 fireEvent.change 남용
- 실제 focus / keyboard 흐름 누락
- pointer event 흐름 누락
- validation trigger 차이
- user behavior와 불일치
- 테스트는 통과하지만 실제 UX 실패

---

### [실무]

나쁜 예:

```tsx
fireEvent.change(screen.getByLabelText("이메일"), {
  target: { value: "test@example.com" },
});
fireEvent.click(screen.getByRole("button", { name: "로그인" }));
```

좋은 예:

```tsx
await user.type(screen.getByLabelText("이메일"), "test@example.com");
await user.click(screen.getByRole("button", { name: "로그인" }));
```

주의:

```text
fireEvent는 테스트를 빠르게 만들 수 있지만 실제 사용자 이벤트 흐름을 건너뛸 수 있음
사용자 행동 테스트에서는 userEvent 우선
```

---

### [FAQ]

Q. fireEvent를 쓰면 테스트가 틀린 거야?
A. 아니다. 하지만 사용자 행동에 가까운 테스트가 필요하면 userEvent가 더 적합하다.

Q. fireEvent가 실제 사용자 행동과 다른 이유는 뭐야?
A. fireEvent는 특정 DOM event 하나를 직접 발생시키므로 focus, keyboard, pointer 흐름을 생략할 수 있다.

Q. fireEvent를 남용하면 어떤 문제가 생겨?
A. 테스트는 통과하지만 실제 사용자가 조작할 때 실패하는 UI를 놓칠 수 있다.

---

# 12. User Event Troubleshooting

## 12.1 userEvent Not Working

### [개념]

userEvent Not Working은 사용자 이벤트를 실행했지만 값 변경, 클릭 결과, submit, focus 이동이 예상대로 동작하지 않는 상황이다.

원인은 await 누락, Query 대상 오류, disabled 상태, Provider 누락, controlled component wrapper 부족, mock 누락일 수 있다.

---

### [핵심]

원인:

- await 누락
- 잘못된 요소 query
- disabled element
- hidden element
- pointer-events none
- controlled component onChange 누락
- Provider 누락
- mock response 누락
- validation 조건 미충족
- focus target 오류
- async result에 getBy 사용

---

### [실무]

Debug Flow:

```text
userEvent 동작 안 함
→ await 사용 확인
→ screen.debug 확인
→ query 대상이 올바른지 확인
→ 요소 disabled 여부 확인
→ controlled component onChange 확인
→ Provider 누락 확인
→ mock 응답 확인
→ 비동기 결과는 findBy 사용
```

Controlled Component 문제 예:

```tsx
render(<SearchInput value="" onChange={vi.fn()} />);

await user.type(screen.getByLabelText("검색어"), "축제");

expect(screen.getByLabelText("검색어")).toHaveValue("축제");
```

위 테스트는 부모 state가 업데이트되지 않아 실패할 수 있다.

Wrapper 필요:

```tsx
function SearchInputWrapper() {
  const [value, setValue] = useState("");

  return <SearchInput value={value} onChange={setValue} />;
}
```

---

### [FAQ]

Q. user.type을 했는데 input 값이 안 바뀌어.
A. controlled component에서 부모 state를 업데이트하는 wrapper가 없을 수 있다.

Q. user.click을 했는데 아무 일도 안 일어나.
A. 클릭 대상이 disabled이거나 잘못된 요소를 찾았거나 조건부 렌더링 조건이 충족되지 않았을 수 있다.

Q. userEvent 후 결과를 못 찾으면?
A. 비동기 결과라면 getBy 대신 findBy를 사용한다.

---

## 12.2 act Warning Troubleshooting

### [개념]

act Warning은 테스트에서 React state update가 완료되기 전에 assertion이 실행되거나 비동기 처리를 기다리지 않았을 때 발생할 수 있다.

userEvent await 누락, findBy 미사용, waitFor 누락, pending promise 처리 문제가 주요 원인이다.

---

### [핵심]

원인:

- userEvent await 누락
- async UI에 getBy 사용
- state update 미대기
- promise unresolved
- timer 처리 누락
- Query retry 지연
- mutation 결과 미대기
- cleanup 전 state update 발생

---

### [실무]

문제 예:

```tsx
user.click(screen.getByRole("button", { name: "저장" }));

expect(screen.getByText("저장되었습니다.")).toBeInTheDocument();
```

개선:

```tsx
await user.click(screen.getByRole("button", { name: "저장" }));

expect(await screen.findByText("저장되었습니다.")).toBeInTheDocument();
```

Debug Flow:

```text
act warning 발생
→ userEvent await 확인
→ async result findBy 확인
→ waitFor 필요한 callback 확인
→ mock promise resolve/reject 확인
→ timer 사용 여부 확인
→ Query retry false 확인
```

---

### [FAQ]

Q. act warning은 왜 나?
A. 상태 업데이트가 끝나기 전에 assertion을 하거나 비동기 이벤트를 기다리지 않았을 가능성이 높다.

Q. act warning은 무시해도 돼?
A. 권장하지 않는다. 테스트가 불안정하거나 실제 상태 변화를 놓치고 있을 수 있다.

Q. act warning을 줄이는 기본 방법은?
A. userEvent에 await를 붙이고 비동기 UI는 findBy로 기다린다.

---

# 13. User Event Checklist

## 13.1 User Event Checklist

### [개념]

User Event Checklist는 사용자 상호작용 테스트가 실제 사용자 흐름과 테스트 안정성 기준을 만족하는지 검수하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] userEvent.setup()을 사용했는가?
- [ ] userEvent 동작에 await를 사용했는가?
- [ ] 클릭 대상은 getByRole로 찾았는가?
- [ ] Form 입력 요소는 getByLabelText로 찾았는가?
- [ ] 입력 후 값 또는 submit 결과를 검증했는가?
- [ ] 클릭 후 사용자에게 보이는 결과를 검증했는가?
- [ ] disabled 상태를 필요한 경우 검증했는가?
- [ ] keyboard 접근성이 중요한 UI를 테스트했는가?
- [ ] hover-only UI에 접근성 대안을 고려했는가?
- [ ] file upload는 더미 File 객체를 사용했는가?
- [ ] 일반 사용자 행동에 fireEvent를 남용하지 않았는가?
- [ ] act warning 원인을 방치하지 않았는가?
```

---

### [실무]

Agent User Event 작성 Flow:

```text
Identify User Action
→ Setup userEvent
→ Find Element by User Query
→ Execute await user action
→ Wait Async UI if needed
→ Assert Visible Result
→ Check fireEvent necessity
→ Review Anti Pattern
```

예:

```text
Login Form
→ type email
→ type password
→ click login
→ loading disabled
→ success redirect or error message
```

---

### [FAQ]

Q. User Event 테스트의 핵심 체크는 뭐야?
A. userEvent.setup, await 사용, 사용자 관점 Query, 사용자 결과 assertion이다.

Q. fireEvent 사용 전 무엇을 확인해야 해?
A. userEvent로 표현 가능한 사용자 행동인지 먼저 확인한다.

Q. userEvent 테스트가 불안정하면 뭘 확인해?
A. await 누락, 비동기 결과 findBy 사용 여부, mock 응답, Provider, controlled component wrapper를 확인한다.

---

# 14. Part04 Summary

## 14.1 User Event Final Rule

### [개념]

Frontend Testing Part04는 React Component의 사용자 상호작용 테스트 기준을 정의한다.

이 Part의 목적은 Agent가 `userEvent`를 우선 사용하고, 실제 사용자 흐름에 가까운 입력, 클릭, 선택, 키보드 조작 테스트를 작성하게 만드는 것이다.

---

### [핵심]

최종 기준:

- userEvent는 사용자 상호작용 테스트의 기본 도구
- fireEvent보다 userEvent 우선
- 테스트마다 userEvent.setup 사용
- userEvent 동작에는 await 사용
- click은 getByRole 기반
- input은 getByLabelText 기반
- 입력 결과는 toHaveValue 또는 submit 결과로 검증
- checkbox / radio는 toBeChecked 사용
- select는 selectOptions 사용
- keyboard / tab으로 접근성 흐름 검증 가능
- hover / upload는 사용자 결과까지 검증
- fireEvent는 저수준 이벤트에 제한 사용
- act warning 방치 금지

---

### [실무]

Agent 작업 Flow:

```text
User Interaction Request
→ Identify Interaction Type
→ Setup userEvent
→ Query Element by Role / Label
→ await user action
→ Assert Visible Result
→ Handle Async with findBy
→ Avoid fireEvent Overuse
→ Check act warning
```

Part05 이후 연결:

```text
Part04 User Event
→ Part05 Unit Test
→ Part06 Component Test
→ Part07 Form Testing
→ Part08 API Mocking
→ Part09 Loading Error Empty
→ Part10 Router Auth Testing
```

---

### [FAQ]

Q. Part04의 최종 목적은 뭐야?
A. Frontend Agent가 userEvent 기반으로 실제 사용자 행동에 가까운 테스트를 작성하게 만드는 것이다.

Q. User Event에서 가장 중요한 규칙은 뭐야?
A. userEvent.setup을 사용하고 모든 사용자 이벤트에 await를 붙이는 것이다.

Q. Part04 다음에는 어떤 내용이 이어져야 해?
A. 순수 함수, validation, formatter, mapper를 검증하는 Unit Test 기준이 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. userEvent는 뭐야?
A. 사용자의 클릭, 입력, 선택, 키보드 조작 같은 실제 행동에 가까운 이벤트를 테스트하는 도구다.

Q. userEvent는 언제 써?
A. Button 클릭, Form 입력, Select 선택, Modal 열기, Tab 이동 같은 사용자 상호작용 테스트에 사용한다.

Q. userEvent와 fireEvent 차이는 뭐야?
A. userEvent는 실제 사용자 행동에 가깝고 fireEvent는 특정 DOM event를 직접 발생시키는 저수준 도구다.

Q. fireEvent보다 userEvent를 먼저 쓰는 이유는 뭐야?
A. userEvent가 실제 브라우저 사용자 이벤트 흐름에 더 가깝기 때문이다.

Q. fireEvent는 언제 써?
A. userEvent로 표현하기 어려운 custom event, scroll, resize 같은 저수준 이벤트에 제한적으로 사용한다.

Q. userEvent.setup은 왜 써?
A. 테스트별 user 인스턴스를 만들고 실제 사용자 이벤트 흐름에 가깝게 동작하도록 하기 위해 사용한다.

Q. userEvent에는 왜 await가 필요해?
A. userEvent가 실제 이벤트 흐름을 비동기로 처리할 수 있어 상태 업데이트를 안전하게 기다리기 위해 필요하다.

Q. click도 await 해야 해?
A. 권장한다. click 이후 state update, validation, API call, route change가 발생할 수 있기 때문이다.

Q. await를 빼면 어떤 문제가 생겨?
A. act warning, assertion 타이밍 오류, 입력값 반영 누락, 간헐 실패가 발생할 수 있다.

Q. 버튼 클릭 테스트는 어떻게 해?
A. `getByRole("button", { name: "..." })`으로 버튼을 찾고 `await user.click`으로 클릭한다.

Q. 아이콘 버튼은 어떻게 테스트해?
A. 버튼에 aria-label을 제공하고 `getByRole("button", { name: "검색" })`으로 찾는다.

Q. disabled 버튼도 클릭 테스트해야 해?
A. 중복 제출 방지나 권한 제어가 중요한 경우 테스트하는 것이 좋다.

Q. disabled 버튼 클릭 후 뭘 확인해?
A. callback이나 API 요청이 실행되지 않았는지 확인한다.

Q. input 입력 테스트는 어떻게 해?
A. `await user.type(screen.getByLabelText("이메일"), "test@example.com")`처럼 작성한다.

Q. 입력값 반영은 어떻게 확인해?
A. `toHaveValue` 또는 `getByDisplayValue`로 확인한다.

Q. password 입력 테스트에 실제 비밀번호를 써도 돼?
A. 안 된다. 테스트용 더미 값을 사용한다.

Q. input 값을 지우는 테스트는 어떻게 해?
A. `await user.clear(input)`을 사용한다.

Q. clear 후 뭘 검증해야 해?
A. input 값이 빈 문자열인지, 필요하면 validation 메시지가 표시되는지 확인한다.

Q. checkbox는 어떻게 테스트해?
A. `getByRole("checkbox", { name })`로 찾고 `await user.click` 후 `toBeChecked`로 검증한다.

Q. radio는 어떻게 테스트해?
A. `getByRole("radio", { name })`로 선택지를 찾고 `await user.click` 후 `toBeChecked`로 검증한다.

Q. radio와 checkbox 차이는 뭐야?
A. checkbox는 여러 개 선택 가능하고 radio는 같은 그룹에서 하나만 선택된다.

Q. select는 어떻게 테스트해?
A. `await user.selectOptions(selectElement, value)`로 option을 선택하고 `toHaveValue`로 확인한다.

Q. select는 어떤 role로 찾아?
A. 일반 select는 보통 `combobox` role로 찾는다.

Q. multiple select는 어떻게 테스트해?
A. `user.selectOptions`에 여러 값을 배열로 전달한다.

Q. custom select도 selectOptions를 써?
A. native select가 아니라면 실제 사용자처럼 combobox를 열고 option을 클릭하는 방식으로 테스트한다.

Q. keyboard 테스트는 언제 필요해?
A. Enter 제출, Escape 닫기, Dropdown 이동, Modal 닫기처럼 키보드 사용성이 중요한 UI에 필요하다.

Q. Enter 키는 어떻게 테스트해?
A. `await user.keyboard("{Enter}")`를 사용한다.

Q. Escape로 Modal 닫기는 테스트해야 해?
A. 접근성과 사용자 경험에 중요한 Modal이라면 테스트하는 것이 좋다.

Q. Tab 이동은 어떻게 테스트해?
A. `await user.tab()`을 사용하고 `toHaveFocus`로 현재 포커스 요소를 확인한다.

Q. focus 테스트는 꼭 해야 해?
A. 모든 Component에 필수는 아니지만 Form, Modal, Dropdown처럼 키보드 접근성이 중요한 UI에는 유용하다.

Q. hover 테스트는 어떻게 해?
A. `await user.hover(element)`를 사용하고 hover 결과 UI를 검증한다.

Q. hover-only UI는 괜찮아?
A. 접근성과 모바일 사용성 문제가 있을 수 있어 focus나 click 대안도 고려해야 한다.

Q. 파일 업로드 테스트는 어떻게 해?
A. `new File()`로 더미 파일을 만들고 `await user.upload(input, file)`을 사용한다.

Q. 업로드 후 뭘 검증해야 해?
A. input files, 미리보기, 파일명 표시, validation 메시지, submit 결과를 검증한다.

Q. Form submit 테스트는 어떻게 해?
A. userEvent로 입력하고 제출 버튼을 클릭한 뒤 submit 결과 UI 또는 callback 값을 검증한다.

Q. validation 실패 시 뭘 확인해?
A. 오류 메시지가 표시되고 submit callback이나 API 요청이 실행되지 않는지 확인한다.

Q. Enter로 submit하는 테스트는 어떻게 해?
A. 입력 후 `await user.keyboard("{Enter}")`를 사용한다.

Q. user.type을 했는데 input 값이 안 바뀌는 이유는 뭐야?
A. controlled component에서 부모 state를 업데이트하는 wrapper가 없을 수 있다.

Q. user.click을 했는데 아무 일도 안 일어나는 이유는 뭐야?
A. 클릭 대상이 disabled이거나 잘못된 요소를 찾았거나 조건부 렌더링 조건이 충족되지 않았을 수 있다.

Q. act warning은 왜 나?
A. 상태 업데이트가 끝나기 전에 assertion을 하거나 비동기 이벤트를 기다리지 않았을 가능성이 높다.

Q. act warning을 줄이는 기본 방법은?
A. userEvent에 await를 붙이고 비동기 UI는 findBy로 기다린다.

Q. User Event 테스트의 핵심 체크는 뭐야?
A. userEvent.setup, await 사용, 사용자 관점 Query, 사용자 결과 assertion이다.

Q. Part04 User Event의 최종 목표는 뭐야?
A. Frontend Agent가 userEvent 기반으로 실제 사용자 행동에 가까운 테스트를 작성하게 만드는 것이다.
