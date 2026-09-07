# Frontend Testing Part07 - Form Testing

---

# 1. Form Testing Overview

## 1.1 Form Testing Definition

### [개념]

Form Testing은 사용자가 입력창, 선택 요소, 체크박스, 라디오, 파일 입력 등을 조작하고 제출했을 때 validation, submit, loading, success, error UI가 올바르게 동작하는지 검증하는 테스트다.

Frontend Form Testing은 사용자의 입력 흐름과 화면 결과를 기준으로 작성한다.

---

### [핵심]

- Form Testing
- Input Test
- Textarea Test
- Select Test
- Checkbox Test
- Radio Test
- File Upload Test
- Validation Test
- Submit Test
- Field Error
- Global Error
- Server Validation Error
- Loading State
- Success State
- Error State
- userEvent
- getByLabelText
- getByRole

---

### [실무]

2026 실무 기준에서 Form Testing은 단순히 input value만 확인하는 테스트가 아니다.

검증 흐름:

```text
Form render
→ label 기반 input query
→ userEvent로 입력
→ submit 실행
→ validation 확인
→ API mock 확인
→ loading / success / error UI 확인
```

좋은 Form Test:

```text
사용자가 입력할 수 있음
필수값 누락 시 오류 메시지 표시
잘못된 형식 입력 시 오류 메시지 표시
submit 중 버튼 disabled
성공 후 메시지 / redirect / reset 확인
실패 후 field error / global error 표시
```

나쁜 Form Test:

```text
input 내부 state 직접 확인
fireEvent.change만 사용
label 없는 input을 testId로만 찾음
submit 함수 직접 호출
API 실제 서버 호출
오류 메시지 검증 누락
```

---

### [FAQ]

Q. Form Testing은 뭐야?
A. 사용자가 Form을 입력하고 제출하는 흐름과 validation, loading, success, error UI를 검증하는 테스트다.

Q. Form Testing에서 가장 중요한 기준은 뭐야?
A. 사용자가 실제로 입력하고 제출하는 흐름을 userEvent로 재현하고 화면 결과를 검증하는 것이다.

Q. input value만 확인하면 충분해?
A. 부족하다. validation, submit 결과, API 상태, 오류 메시지도 함께 검증해야 한다.

---

## 1.2 Form Testing Scope

### [개념]

Form Testing Scope는 Form 테스트에서 검증할 대상과 분리할 대상을 정하는 기준이다.

Form Component 단위 테스트와 Page / API 연동 흐름 테스트를 구분해야 한다.

---

### [핵심]

포함 범위:

- input typing
- textarea typing
- select option
- checkbox toggle
- radio select
- file upload
- submit button
- validation message
- field error
- global error
- loading disabled
- success message
- error message
- form reset
- callback arguments

분리 권장:

- 실제 API 호출
- 실제 Backend validation 통합
- 전체 Auth redirect 흐름
- 실제 브라우저 E2E
- 복잡한 서버 상태 cache 갱신
- 결제 전체 흐름

---

### [실무]

Component Form Test 적합 예:

```text
LoginForm에 이메일과 비밀번호를 입력하면 onLogin이 호출된다.
ReviewForm에서 내용이 비어 있으면 오류 메시지를 표시한다.
ImageUploadForm에서 이미지 파일을 선택하면 미리보기를 표시한다.
SearchForm에서 Enter 키로 검색을 실행한다.
SubmitButton이 submitting 중 disabled 된다.
```

Integration Test가 더 적합한 예:

```text
로그인 API 성공 후 token 저장과 redirect
회원가입 API 실패 후 서버 field error 표시
리뷰 등록 성공 후 TanStack Query 목록 갱신
보호 Route에서 로그인 Form으로 이동 후 원래 페이지 복귀
```

---

### [FAQ]

Q. Form Testing은 Component Test야 Integration Test야?
A. 단순 Form 입력과 callback 검증은 Component Test이고 API, Router, Auth Store가 엮이면 Integration Test에 가깝다.

Q. 실제 API를 호출해 Form을 테스트해도 돼?
A. 일반 Form Test에서는 권장하지 않는다. API 응답은 mock으로 제어한다.

Q. Form 내부 validation과 서버 validation은 모두 테스트해야 해?
A. 중요한 Form이라면 클라이언트 validation과 서버 validation error 표시를 모두 테스트하는 것이 좋다.

---

# 2. Form Input Test

## 2.1 Text Input Test

### [개념]

Text Input Test는 사용자가 input에 텍스트를 입력했을 때 값이 반영되고 submit 또는 validation에 사용되는지 검증하는 테스트다.

Form input은 가능한 `getByLabelText` 또는 `getByRole("textbox", { name })`로 찾는다.

---

### [핵심]

- text input
- email input
- password input
- search input
- user.type
- getByLabelText
- getByRole textbox
- toHaveValue
- getByDisplayValue
- controlled input
- form submit

---

### [실무]

기본 예:

```tsx
test("이메일을 입력하면 입력값이 반영된다", async () => {
  const user = userEvent.setup();

  render(<LoginForm onLogin={vi.fn()} />);

  const emailInput = screen.getByLabelText("이메일");

  await user.type(emailInput, "test@example.com");

  expect(emailInput).toHaveValue("test@example.com");
});
```

password input 예:

```tsx
test("비밀번호를 입력한다", async () => {
  const user = userEvent.setup();

  render(<LoginForm onLogin={vi.fn()} />);

  await user.type(screen.getByLabelText("비밀번호"), "password123");

  expect(screen.getByLabelText("비밀번호")).toHaveValue("password123");
});
```

권장:

- 실제 비밀번호 사용 금지
- label 기반 query 우선
- user.type에는 await 사용
- 입력값 검증은 toHaveValue 사용
- submit 결과 검증과 함께 작성 가능

---

### [FAQ]

Q. Text Input Test는 어떻게 작성해?
A. label로 input을 찾고 `await user.type`으로 입력한 뒤 `toHaveValue`로 검증한다.

Q. password input은 어떤 Query를 써?
A. `getByLabelText("비밀번호")`가 안전하다.

Q. 테스트에 실제 비밀번호를 써도 돼?
A. 안 된다. `password123` 같은 더미 값을 사용한다.

---

## 2.2 Textarea Test

### [개념]

Textarea Test는 사용자가 여러 줄 텍스트나 긴 내용을 입력했을 때 값이 반영되고 validation 또는 submit에 사용되는지 검증하는 테스트다.

리뷰, 댓글, 문의, 게시글 내용 Form에서 자주 사용한다.

---

### [핵심]

- textarea
- multiline input
- review content
- comment content
- inquiry content
- post content
- user.type
- user.clear
- toHaveValue
- max length
- required validation

---

### [실무]

예:

```tsx
test("리뷰 내용을 입력하면 값이 반영된다", async () => {
  const user = userEvent.setup();

  render(<ReviewForm onSubmit={vi.fn()} />);

  const textarea = screen.getByLabelText("리뷰 내용");

  await user.type(textarea, "축제가 정말 좋았어요.");

  expect(textarea).toHaveValue("축제가 정말 좋았어요.");
});
```

여러 줄 입력:

```tsx
await user.type(
  screen.getByLabelText("문의 내용"),
  "첫 번째 줄{enter}두 번째 줄",
);

expect(screen.getByLabelText("문의 내용")).toHaveValue(
  "첫 번째 줄\n두 번째 줄",
);
```

권장:

- textarea도 label 연결
- required validation 테스트
- max length가 있으면 boundary 테스트
- submit 결과에 content trim 여부 확인 가능
- Enter 동작이 submit인지 줄바꿈인지 명확히 구분

---

### [FAQ]

Q. textarea는 어떻게 테스트해?
A. `getByLabelText`로 찾고 `user.type` 후 `toHaveValue`로 입력값을 검증한다.

Q. textarea에서 Enter는 submit이야?
A. 보통 줄바꿈이다. Form 설계에 따라 다르므로 사용자 동작 기준으로 테스트한다.

Q. 리뷰 내용 공백 검증도 해야 해?
A. 중요하다. 공백만 입력한 경우 required validation이 동작하는지 확인해야 한다.

---

## 2.3 Clear and Reset Input Test

### [개념]

Clear and Reset Input Test는 사용자가 입력값을 지우거나 reset action을 실행했을 때 Form 값이 비워지고 관련 UI가 초기화되는지 검증하는 테스트다.

---

### [핵심]

- user.clear
- reset button
- form reset
- input empty
- textarea empty
- select reset
- checkbox reset
- validation reset
- filter reset
- search reset

---

### [실무]

clear 예:

```tsx
test("검색어를 지우면 입력값이 비워진다", async () => {
  const user = userEvent.setup();

  render(<SearchForm initialKeyword="축제" onSearch={vi.fn()} />);

  const input = screen.getByLabelText("검색어");

  expect(input).toHaveValue("축제");

  await user.clear(input);

  expect(input).toHaveValue("");
});
```

reset button 예:

```tsx
test("초기화 버튼을 클릭하면 Form 값이 초기화된다", async () => {
  const user = userEvent.setup();

  render(<FestivalFilterForm />);

  await user.type(screen.getByLabelText("검색어"), "봄꽃");
  await user.selectOptions(
    screen.getByRole("combobox", { name: "지역" }),
    "seoul",
  );

  await user.click(screen.getByRole("button", { name: "초기화" }));

  expect(screen.getByLabelText("검색어")).toHaveValue("");
  expect(screen.getByRole("combobox", { name: "지역" })).toHaveValue("");
});
```

권장:

- user.clear에는 await 사용
- reset 후 input / select / checkbox 상태 확인
- validation message도 reset되는지 확인
- search filter reset은 결과 UI까지 검증 가능

---

### [FAQ]

Q. input clear는 어떻게 테스트해?
A. `await user.clear(input)` 후 값이 빈 문자열인지 확인한다.

Q. Form reset은 뭘 확인해야 해?
A. input, select, checkbox, validation message, filter 결과가 초기화되는지 확인한다.

Q. reset 후 오류 메시지도 사라져야 해?
A. Form 정책에 따라 다르지만 일반적으로 reset이면 validation error도 초기화하는 것이 자연스럽다.

---

# 3. Select, Checkbox, Radio Test

## 3.1 Select Test

### [개념]

Select Test는 사용자가 select box에서 option을 선택했을 때 선택 값과 submit 결과 또는 필터 결과가 올바르게 반영되는지 검증한다.

---

### [핵심]

- select
- option
- combobox
- user.selectOptions
- toHaveValue
- toBeSelected
- filter form
- category select
- region select
- default option
- disabled option

---

### [실무]

기본 예:

```tsx
test("지역을 선택하면 선택값이 반영된다", async () => {
  const user = userEvent.setup();

  render(<RegionSelect />);

  const select = screen.getByRole("combobox", { name: "지역" });

  await user.selectOptions(select, "seoul");

  expect(select).toHaveValue("seoul");
  expect(screen.getByRole("option", { name: "서울" })).toBeSelected();
});
```

submit 연계:

```tsx
test("선택한 지역 값으로 검색한다", async () => {
  const user = userEvent.setup();
  const onSearch = vi.fn();

  render(<FestivalSearchForm onSearch={onSearch} />);

  await user.selectOptions(
    screen.getByRole("combobox", { name: "지역" }),
    "seoul",
  );
  await user.click(screen.getByRole("button", { name: "검색" }));

  expect(onSearch).toHaveBeenCalledWith({
    region: "seoul",
  });
});
```

권장:

- native select는 user.selectOptions 사용
- custom select는 실제 클릭 흐름 테스트
- 기본 option 처리 검증
- disabled option이 있으면 선택 불가 검증
- submit 값과 연결 검증

---

### [FAQ]

Q. select는 어떻게 테스트해?
A. `user.selectOptions`로 option을 선택하고 `toHaveValue` 또는 `toBeSelected`로 확인한다.

Q. select는 어떤 Query로 찾아?
A. 일반 select는 `getByRole("combobox", { name })`를 사용한다.

Q. custom select도 selectOptions를 써?
A. native select가 아니라면 실제 사용자처럼 trigger를 클릭하고 option을 선택한다.

---

## 3.2 Checkbox Test

### [개념]

Checkbox Test는 사용자가 checkbox를 선택하거나 해제했을 때 checked 상태와 Form 제출 값이 올바르게 반영되는지 검증한다.

---

### [핵심]

- checkbox
- user.click
- toBeChecked
- not.toBeChecked
- agreement
- multi filter
- terms
- required checkbox
- submit value
- toggle

---

### [실무]

기본 예:

```tsx
test("약관 동의 체크박스를 선택한다", async () => {
  const user = userEvent.setup();

  render(<SignupForm onSubmit={vi.fn()} />);

  const checkbox = screen.getByRole("checkbox", { name: "약관 동의" });

  expect(checkbox).not.toBeChecked();

  await user.click(checkbox);

  expect(checkbox).toBeChecked();
});
```

required checkbox validation:

```tsx
test("약관에 동의하지 않으면 오류 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  render(<SignupForm onSubmit={vi.fn()} />);

  await user.click(screen.getByRole("button", { name: "가입하기" }));

  expect(screen.getByText("약관에 동의해 주세요.")).toBeInTheDocument();
});
```

multi filter:

```tsx
await user.click(screen.getByRole("checkbox", { name: "무료" }));
await user.click(screen.getByRole("checkbox", { name: "실내" }));

expect(screen.getByRole("checkbox", { name: "무료" })).toBeChecked();
expect(screen.getByRole("checkbox", { name: "실내" })).toBeChecked();
```

권장:

- checkbox는 role과 name으로 찾음
- checked 상태는 toBeChecked 사용
- required checkbox validation 검증
- 여러 checkbox 필터는 선택 조합 검증
- submit 값에 반영되는지 확인

---

### [FAQ]

Q. checkbox는 어떻게 테스트해?
A. `getByRole("checkbox", { name })`로 찾고 `await user.click` 후 `toBeChecked`로 검증한다.

Q. 약관 동의 validation도 테스트해야 해?
A. 회원가입처럼 중요한 Form에서는 테스트하는 것이 좋다.

Q. 여러 checkbox 선택은 어떻게 검증해?
A. 각각 클릭한 뒤 각 checkbox의 checked 상태와 submit 값 또는 필터 결과를 확인한다.

---

## 3.3 Radio Test

### [개념]

Radio Test는 사용자가 여러 선택지 중 하나를 선택했을 때 같은 group 내에서 하나만 선택되고 Form 값에 반영되는지 검증한다.

---

### [핵심]

- radio
- radio group
- user.click
- toBeChecked
- exclusive selection
- rating
- visibility
- gender optional caution
- survey
- submit value

---

### [실무]

기본 예:

```tsx
test("평점을 선택한다", async () => {
  const user = userEvent.setup();

  render(<ReviewForm onSubmit={vi.fn()} />);

  const fiveStar = screen.getByRole("radio", { name: "5점" });
  const fourStar = screen.getByRole("radio", { name: "4점" });

  await user.click(fiveStar);

  expect(fiveStar).toBeChecked();
  expect(fourStar).not.toBeChecked();
});
```

submit 연계:

```tsx
test("선택한 평점을 submit 값에 포함한다", async () => {
  const user = userEvent.setup();
  const onSubmit = vi.fn();

  render(<ReviewForm onSubmit={onSubmit} />);

  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(onSubmit).toHaveBeenCalledWith({
    rating: 5,
    content: "좋았어요",
  });
});
```

권장:

- radio option은 role과 name으로 찾음
- 선택된 값과 선택되지 않은 값 모두 확인 가능
- required radio validation 테스트
- submit 값 반영 확인
- radio group 접근성 label 검토

---

### [FAQ]

Q. radio는 어떻게 테스트해?
A. `getByRole("radio", { name })`로 찾고 클릭 후 `toBeChecked`로 검증한다.

Q. radio group에서는 무엇을 확인해야 해?
A. 선택한 option만 checked이고 다른 option은 unchecked인지 확인한다.

Q. radio 선택값도 submit에서 확인해야 해?
A. Form 흐름에서는 submit 값에 선택값이 포함되는지 확인하는 것이 좋다.

---

# 4. Validation Test

## 4.1 Client Validation Test

### [개념]

Client Validation Test는 사용자가 잘못된 값을 입력하거나 필수값을 누락했을 때 Frontend에서 오류 메시지를 표시하고 submit을 막는지 검증하는 테스트다.

---

### [핵심]

- client validation
- required error
- format error
- length error
- range error
- password mismatch
- invalid submit
- no API call
- field error
- role alert
- aria-invalid

---

### [실무]

필수값 오류:

```tsx
test("이메일을 입력하지 않으면 오류 메시지를 표시한다", async () => {
  const user = userEvent.setup();
  const onSubmit = vi.fn();

  render(<LoginForm onLogin={onSubmit} />);

  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(screen.getByText("이메일을 입력해 주세요.")).toBeInTheDocument();
  expect(onSubmit).not.toHaveBeenCalled();
});
```

형식 오류:

```tsx
test("이메일 형식이 올바르지 않으면 오류 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  render(<LoginForm onLogin={vi.fn()} />);

  await user.type(screen.getByLabelText("이메일"), "wrong-email");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(
    screen.getByText("올바른 이메일 형식이 아닙니다."),
  ).toBeInTheDocument();
});
```

권장:

- 사용자 행동으로 validation 발생
- 오류 메시지가 화면에 표시되는지 확인
- invalid submit 시 submit callback / API call이 실행되지 않는지 확인
- field별 오류 메시지 구분
- role alert / aria-invalid 접근성 검토

---

### [FAQ]

Q. Client Validation Test는 뭐야?
A. 잘못된 입력값에 대해 Frontend가 오류 메시지를 표시하고 submit을 막는지 검증하는 테스트다.

Q. validation 함수만 Unit Test하면 충분해?
A. 아니다. Component에서 실제 오류 메시지가 표시되는지도 테스트해야 한다.

Q. invalid submit 시 무엇을 확인해야 해?
A. 오류 메시지 표시와 submit callback 또는 API 요청이 실행되지 않는지 확인한다.

---

## 4.2 Field Error Test

### [개념]

Field Error Test는 특정 Form field에 오류가 있을 때 해당 field 근처에 오류 메시지가 표시되고 접근성 상태가 반영되는지 검증한다.

---

### [핵심]

- field error
- input error
- error message
- aria-invalid
- aria-describedby
- role alert
- field validation
- server field error
- error placement

---

### [실무]

예:

```tsx
test("비밀번호가 짧으면 비밀번호 field 오류를 표시한다", async () => {
  const user = userEvent.setup();

  render(<SignupForm onSubmit={vi.fn()} />);

  const passwordInput = screen.getByLabelText("비밀번호");

  await user.type(passwordInput, "123");
  await user.click(screen.getByRole("button", { name: "가입하기" }));

  expect(
    screen.getByText("비밀번호는 8자 이상이어야 합니다."),
  ).toBeInTheDocument();
  expect(passwordInput).toHaveAttribute("aria-invalid", "true");
});
```

aria-describedby 예:

```tsx
expect(screen.getByLabelText("비밀번호")).toHaveAttribute(
  "aria-describedby",
  "password-error",
);
```

권장:

- field 오류는 field별로 명확히 검증
- 오류 메시지와 input 연결 확인
- aria-invalid 사용 고려
- 오류 발생 후 focus 이동 정책이 있으면 테스트
- 서버 field error도 같은 UI로 표시되는지 확인

---

### [FAQ]

Q. Field Error는 뭘 테스트해?
A. 특정 입력값 오류 메시지와 해당 input의 오류 접근성 상태를 테스트한다.

Q. aria-invalid도 테스트해야 해?
A. 접근성이 중요한 Form에서는 테스트하는 것이 좋다.

Q. 오류 메시지는 input 근처에 있어야 해?
A. 사용자 경험상 해당 field와 연결되어 표시되는 것이 좋다.

---

## 4.3 Global Error Test

### [개념]

Global Error Test는 Form 전체에 영향을 주는 오류가 발생했을 때 상단 또는 공통 영역에 오류 메시지가 표시되는지 검증하는 테스트다.

로그인 실패, 서버 오류, 권한 오류, 네트워크 오류에 사용한다.

---

### [핵심]

- global error
- form error
- login failed
- server error
- network error
- unauthorized
- forbidden
- alert role
- error summary
- retry action

---

### [실무]

예:

```tsx
test("로그인 실패 시 global error 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  render(
    <LoginForm onLogin={vi.fn().mockRejectedValue(new Error("failed"))} />,
  );

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "wrong-password");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(await screen.findByRole("alert")).toHaveTextContent(
    "이메일 또는 비밀번호가 올바르지 않습니다.",
  );
});
```

권장:

- field error와 global error 구분
- 로그인 실패 / 서버 오류 / 네트워크 오류 메시지 구분
- role alert 사용 고려
- 서버 내부 상세 메시지 노출 금지
- retry action이 있으면 테스트

---

### [FAQ]

Q. Global Error는 뭐야?
A. 특정 field가 아니라 Form 전체에 해당하는 오류 메시지다.

Q. 로그인 실패는 Field Error야 Global Error야?
A. 보통 이메일 또는 비밀번호 조합 실패는 Global Error로 처리한다.

Q. 서버 내부 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자에게 안전하고 일반적인 오류 메시지를 표시한다.

---

## 4.4 Password Confirm Test

### [개념]

Password Confirm Test는 비밀번호와 비밀번호 확인 값이 일치하지 않을 때 오류 메시지가 표시되고 submit이 막히는지 검증하는 테스트다.

회원가입 Form에서 자주 사용한다.

---

### [핵심]

- password confirm
- password mismatch
- confirm password
- validation error
- invalid submit
- no API call
- field error
- signup form

---

### [실무]

예:

```tsx
test("비밀번호 확인이 일치하지 않으면 오류 메시지를 표시한다", async () => {
  const user = userEvent.setup();
  const onSubmit = vi.fn();

  render(<SignupForm onSubmit={onSubmit} />);

  await user.type(screen.getByLabelText("비밀번호"), "password123");
  await user.type(screen.getByLabelText("비밀번호 확인"), "password456");
  await user.click(screen.getByRole("button", { name: "가입하기" }));

  expect(screen.getByText("비밀번호가 일치하지 않습니다.")).toBeInTheDocument();
  expect(onSubmit).not.toHaveBeenCalled();
});
```

정상 케이스:

```tsx
test("비밀번호와 확인 값이 일치하면 submit이 가능하다", async () => {
  const user = userEvent.setup();
  const onSubmit = vi.fn();

  render(<SignupForm onSubmit={onSubmit} />);

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "password123");
  await user.type(screen.getByLabelText("비밀번호 확인"), "password123");
  await user.click(screen.getByRole("button", { name: "가입하기" }));

  expect(onSubmit).toHaveBeenCalled();
});
```

권장:

- mismatch case 테스트
- match case 테스트
- invalid submit 방지 확인
- 비밀번호 실제 값 사용 금지
- 오류 메시지 field 연결 확인

---

### [FAQ]

Q. Password Confirm Test는 왜 필요해?
A. 회원가입에서 자주 발생하는 입력 오류이며 submit 방지가 중요하기 때문이다.

Q. 비밀번호 확인 오류는 Field Error야?
A. 일반적으로 비밀번호 확인 field의 Field Error로 처리한다.

Q. 정상 케이스도 테스트해야 해?
A. 가능하면 mismatch와 match 케이스를 모두 테스트한다.

---

# 5. Submit Test

## 5.1 Submit Callback Test

### [개념]

Submit Callback Test는 사용자가 Form을 올바르게 입력하고 제출했을 때 callback이 올바른 값으로 호출되는지 검증하는 테스트다.

Form Component 단위 테스트에서 자주 사용한다.

---

### [핵심]

- submit callback
- onSubmit
- user.type
- user.click
- submit button
- callback arguments
- form values
- trimmed value
- transformed value
- valid submit

---

### [실무]

예:

```tsx
test("로그인 Form을 제출하면 이메일과 비밀번호로 onLogin이 호출된다", async () => {
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

trim 검증:

```tsx
test("리뷰 내용을 trim하여 제출한다", async () => {
  const user = userEvent.setup();
  const onSubmit = vi.fn();

  render(<ReviewForm onSubmit={onSubmit} />);

  await user.type(screen.getByLabelText("리뷰 내용"), " 좋았어요 ");
  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(onSubmit).toHaveBeenCalledWith({
    rating: 5,
    content: "좋았어요",
  });
});
```

권장:

- callback 인자 shape 검증
- trim / type conversion 검증
- validation 통과 후 submit 확인
- invalid submit은 not.toHaveBeenCalled 검증
- 실제 API 호출 대신 callback mock 사용

---

### [FAQ]

Q. Submit Callback Test는 뭐야?
A. Form 제출 시 onSubmit 같은 callback이 올바른 Form 값으로 호출되는지 검증하는 테스트다.

Q. submit 값의 trim도 테스트해야 해?
A. Form 정책에 포함된 변환이라면 테스트하는 것이 좋다.

Q. invalid submit에서는 무엇을 확인해?
A. callback이 호출되지 않고 오류 메시지가 표시되는지 확인한다.

---

## 5.2 Submit Loading Test

### [개념]

Submit Loading Test는 Form 제출 중 loading 상태가 표시되고 제출 버튼이 disabled 되는지 검증하는 테스트다.

중복 제출 방지와 사용자 피드백을 위해 중요하다.

---

### [핵심]

- submit loading
- submitting state
- pending state
- button disabled
- loading text
- spinner
- duplicate submit prevention
- pending promise
- no double submit

---

### [실무]

예:

```tsx
test("로그인 요청 중 버튼을 비활성화한다", async () => {
  const user = userEvent.setup();

  render(<LoginForm onLogin={() => new Promise(() => {})} />);

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "password123");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(screen.getByRole("button", { name: "처리 중..." })).toBeDisabled();
});
```

중복 제출 방지:

```tsx
test("제출 중 중복 클릭해도 submit은 한 번만 호출된다", async () => {
  const user = userEvent.setup();
  const onSubmit = vi.fn(() => new Promise(() => {}));

  render(<LoginForm onLogin={onSubmit} />);

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "password123");

  const button = screen.getByRole("button", { name: "로그인" });

  await user.click(button);
  await user.click(screen.getByRole("button", { name: "처리 중..." }));

  expect(onSubmit).toHaveBeenCalledTimes(1);
});
```

권장:

- pending 상태에서 button disabled 검증
- loading text 또는 spinner 검증
- 중복 submit 방지 검증
- pending promise 사용 시 테스트 hang 주의
- 성공 / 실패 후 상태 복구는 별도 테스트 가능

---

### [FAQ]

Q. Submit Loading Test는 왜 필요해?
A. 중복 제출을 막고 사용자에게 처리 중 상태를 알려주는지 확인하기 위해 필요하다.

Q. pending promise 테스트는 위험해?
A. 잘못 구성하면 테스트가 끝나지 않을 수 있다. 상태 확인 후 테스트가 종료되도록 작성한다.

Q. 중복 제출 방지는 어떻게 테스트해?
A. submit 중 버튼이 disabled되고 callback이 한 번만 호출되는지 확인한다.

---

## 5.3 Submit Success Test

### [개념]

Submit Success Test는 Form 제출이 성공했을 때 성공 메시지, form reset, redirect, list update 같은 사용자 결과가 표시되는지 검증하는 테스트다.

---

### [핵심]

- submit success
- success message
- toast
- form reset
- redirect
- close modal
- list update
- callback success
- mutation success
- user-visible result

---

### [실무]

성공 메시지 예:

```tsx
test("리뷰 등록 성공 시 성공 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  render(<ReviewForm onSubmit={vi.fn().mockResolvedValue(undefined)} />);

  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(await screen.findByText("리뷰가 등록되었습니다.")).toBeInTheDocument();
});
```

form reset 예:

```tsx
test("제출 성공 후 Form을 초기화한다", async () => {
  const user = userEvent.setup();

  render(<ReviewForm onSubmit={vi.fn().mockResolvedValue(undefined)} />);

  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");
  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(await screen.findByText("리뷰가 등록되었습니다.")).toBeInTheDocument();
  expect(screen.getByLabelText("리뷰 내용")).toHaveValue("");
});
```

권장:

- 성공 후 사용자에게 보이는 결과 검증
- submit callback 호출만으로 끝내지 않음
- 성공 메시지 / redirect / reset / close 중 정책에 맞게 검증
- 비동기 성공 결과는 findBy 사용

---

### [FAQ]

Q. Submit Success Test는 뭘 확인해?
A. 성공 메시지, Form reset, redirect, Modal close, 목록 갱신 같은 사용자 결과를 확인한다.

Q. callback 호출만 확인하면 부족해?
A. 핵심 흐름에서는 사용자가 보는 성공 결과까지 확인하는 것이 좋다.

Q. 성공 메시지는 findBy로 찾아야 해?
A. 비동기 submit 결과라면 `await screen.findByText`를 사용한다.

---

## 5.4 Submit Error Test

### [개념]

Submit Error Test는 Form 제출 실패 시 field error, global error, retry 가능 상태, 버튼 상태 복구가 올바르게 동작하는지 검증하는 테스트다.

---

### [핵심]

- submit error
- rejected promise
- field error
- global error
- server validation error
- network error
- button enabled after error
- retry possible
- safe error message

---

### [실무]

global error 예:

```tsx
test("제출 실패 시 오류 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  render(
    <LoginForm onLogin={vi.fn().mockRejectedValue(new Error("failed"))} />,
  );

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "wrong-password");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(await screen.findByRole("alert")).toHaveTextContent(
    "로그인에 실패했습니다.",
  );
});
```

버튼 상태 복구:

```tsx
test("제출 실패 후 버튼을 다시 활성화한다", async () => {
  const user = userEvent.setup();

  render(
    <LoginForm onLogin={vi.fn().mockRejectedValue(new Error("failed"))} />,
  );

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "wrong-password");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(await screen.findByRole("alert")).toBeInTheDocument();
  expect(screen.getByRole("button", { name: "로그인" })).toBeEnabled();
});
```

권장:

- 실패 메시지는 사용자 친화적 문구
- 서버 내부 error detail 노출 지양
- 실패 후 재시도 가능 상태 확인
- field error와 global error 구분
- rejected promise 결과는 findBy로 대기

---

### [FAQ]

Q. Submit Error Test는 뭘 확인해?
A. 오류 메시지 표시, 버튼 상태 복구, field/global error 구분, 재시도 가능 여부를 확인한다.

Q. 제출 실패 후 버튼은 다시 활성화되어야 해?
A. 일반적으로 재시도를 위해 다시 활성화되어야 한다.

Q. 서버 error detail을 그대로 보여줘도 돼?
A. 권장하지 않는다. 안전한 사용자 메시지로 변환해 표시한다.

---

# 6. Server Validation Error Test

## 6.1 Server Field Error Test

### [개념]

Server Field Error Test는 서버가 특정 field에 대한 validation error를 반환했을 때 Frontend가 해당 field 오류 메시지로 표시하는지 검증한다.

회원가입, 로그인, 리뷰 작성, 결제 Form에서 중요하다.

---

### [핵심]

- server validation error
- field error
- 400 error
- error.response.data
- fieldErrors
- email duplicate
- nickname duplicate
- invalid field
- API mock
- AxiosError shape

---

### [실무]

서버 오류 mock 예:

```tsx
const duplicateEmailError = {
  response: {
    status: 400,
    data: {
      fieldErrors: {
        email: "이미 사용 중인 이메일입니다.",
      },
    },
  },
};
```

테스트:

```tsx
test("서버 field error를 이메일 오류로 표시한다", async () => {
  const user = userEvent.setup();

  render(
    <SignupForm onSubmit={vi.fn().mockRejectedValue(duplicateEmailError)} />,
  );

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "password123");
  await user.type(screen.getByLabelText("비밀번호 확인"), "password123");
  await user.click(screen.getByRole("button", { name: "가입하기" }));

  expect(
    await screen.findByText("이미 사용 중인 이메일입니다."),
  ).toBeInTheDocument();
});
```

권장:

- 실제 코드가 참조하는 error shape와 mock shape 일치
- field error는 해당 field 근처에 표시
- client validation과 server validation 구분
- 중복 이메일 / 중복 닉네임 같은 실무 오류 테스트
- 서버 메시지를 그대로 표시할지 mapping할지 정책 명확화

---

### [FAQ]

Q. Server Field Error는 뭐야?
A. 서버가 특정 field에 대해 반환한 validation error를 Form field 오류로 표시하는 것이다.

Q. mockRejectedValue 구조는 실제 AxiosError와 같아야 해?
A. 가능하면 실제 코드가 참조하는 `error.response.status`, `error.response.data` 구조와 맞춰야 한다.

Q. 서버 validation error도 테스트해야 해?
A. 중요한 Form에서는 해야 한다. 클라이언트에서 잡지 못한 오류를 사용자에게 올바르게 표시해야 한다.

---

## 6.2 Server Global Error Test

### [개념]

Server Global Error Test는 서버 오류가 특정 field가 아닌 Form 전체 오류로 반환되었을 때 global error 영역에 표시되는지 검증한다.

---

### [핵심]

- server global error
- 401
- 403
- 409
- 500
- network error
- timeout
- global message
- role alert
- safe fallback
- retry

---

### [실무]

예:

```tsx
const serverError = {
  response: {
    status: 500,
    data: {
      message: "Internal Server Error",
    },
  },
};
```

테스트:

```tsx
test("서버 오류가 발생하면 global error를 표시한다", async () => {
  const user = userEvent.setup();

  render(<ContactForm onSubmit={vi.fn().mockRejectedValue(serverError)} />);

  await user.type(screen.getByLabelText("문의 내용"), "문의합니다.");
  await user.click(screen.getByRole("button", { name: "보내기" }));

  expect(await screen.findByRole("alert")).toHaveTextContent(
    "서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.",
  );
});
```

권장:

- 401 / 403 / 409 / 500 주요 상태 테스트
- network error fallback 테스트
- 서버 내부 메시지 직접 노출 방지
- alert role 사용
- retry action이 있으면 테스트

---

### [FAQ]

Q. Server Global Error는 뭐야?
A. 특정 field가 아니라 Form 전체에 표시해야 하는 서버 오류다.

Q. 500 에러는 어떻게 표시해야 해?
A. 서버 내부 상세 대신 일반적인 오류 안내 메시지를 표시하는 것이 좋다.

Q. 네트워크 오류도 테스트해야 해?
A. 중요한 Form에서는 fallback 메시지를 테스트하는 것이 좋다.

---

# 7. File Upload Form Test

## 7.1 File Input Test

### [개념]

File Input Test는 사용자가 파일을 선택했을 때 input files 값, 파일명 표시, 미리보기, validation이 올바르게 동작하는지 검증하는 테스트다.

`user.upload`를 사용한다.

---

### [핵심]

- file input
- user.upload
- File object
- image upload
- preview
- file name
- file size
- file type
- multiple files
- validation
- test data security

---

### [실무]

기본 예:

```tsx
test("이미지 파일을 선택하면 input에 파일이 반영된다", async () => {
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

미리보기:

```tsx
expect(
  await screen.findByAltText("업로드 이미지 미리보기"),
).toBeInTheDocument();
```

파일명 표시:

```tsx
expect(screen.getByText("festival.png")).toBeInTheDocument();
```

권장:

- 더미 File 객체 사용
- 실제 개인정보 파일 사용 금지
- file input도 label 연결
- 미리보기가 비동기면 findBy 사용
- 파일명 / 파일 수 / validation 검증

---

### [FAQ]

Q. File Input Test는 어떻게 작성해?
A. `new File()`로 더미 파일을 만들고 `await user.upload(input, file)`로 업로드한다.

Q. 실제 파일을 테스트에 넣어도 돼?
A. 가능하면 더미 File 객체를 사용하고 실제 민감 파일은 사용하지 않는다.

Q. 업로드 후 뭘 검증해야 해?
A. input files, 파일명 표시, 미리보기, validation 메시지를 검증한다.

---

## 7.2 File Validation Test

### [개념]

File Validation Test는 사용자가 허용되지 않는 파일 형식, 너무 큰 파일, 파일 누락 상태로 제출했을 때 오류 메시지가 표시되는지 검증하는 테스트다.

---

### [핵심]

- file type validation
- file size validation
- required file
- image only
- max size
- multiple file count
- invalid file
- validation message
- no submit

---

### [실무]

파일 형식 오류:

```tsx
test("이미지가 아닌 파일을 업로드하면 오류 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  render(<ImageUploadForm onSubmit={vi.fn()} />);

  const file = new File(["text"], "memo.txt", {
    type: "text/plain",
  });

  await user.upload(screen.getByLabelText("대표 이미지"), file);

  expect(
    screen.getByText("이미지 파일만 업로드할 수 있습니다."),
  ).toBeInTheDocument();
});
```

파일 크기 오류:

```tsx
const largeFile = new File(["x".repeat(1024 * 1024 * 6)], "large.png", {
  type: "image/png",
});

await user.upload(screen.getByLabelText("대표 이미지"), largeFile);

expect(
  screen.getByText("파일 크기는 5MB 이하만 가능합니다."),
).toBeInTheDocument();
```

권장:

- 허용 file type 테스트
- 금지 file type 테스트
- max size boundary 테스트
- required file 테스트
- invalid file submit 방지 확인

---

### [FAQ]

Q. File Validation은 뭘 테스트해?
A. 파일 형식, 파일 크기, 필수 파일 누락, 파일 개수 제한을 테스트한다.

Q. 큰 파일 테스트는 실제 큰 파일이 필요해?
A. `new File()`로 더미 content를 만들어 크기 조건을 재현할 수 있다.

Q. invalid file이면 submit도 막아야 해?
A. 일반적으로 오류 메시지를 표시하고 submit을 막아야 한다.

---

# 8. Accessibility Form Test

## 8.1 Form Label Test

### [개념]

Form Label Test는 input, textarea, select, checkbox, radio가 사용자가 이해할 수 있는 label과 연결되어 있는지 검증하는 테스트다.

label이 잘 연결된 Form은 테스트와 접근성이 모두 좋아진다.

---

### [핵심]

- label
- htmlFor
- input id
- getByLabelText
- accessible name
- aria-label
- aria-labelledby
- form accessibility
- visible label
- placeholder caution

---

### [실무]

예:

```tsx
test("로그인 Form은 이메일과 비밀번호 label을 제공한다", () => {
  render(<LoginForm onLogin={vi.fn()} />);

  expect(screen.getByLabelText("이메일")).toBeInTheDocument();
  expect(screen.getByLabelText("비밀번호")).toBeInTheDocument();
});
```

권장 구조:

```tsx
<label htmlFor="email">이메일</label>
<input id="email" type="email" />
```

지양:

```tsx
<input placeholder="이메일" />
```

권장:

- placeholder를 label 대체로 사용하지 않음
- 시각 label이 어렵다면 aria-label 사용
- icon-only control에는 aria-label 제공
- Form query는 label 기반으로 작성

---

### [FAQ]

Q. Form Label Test는 왜 필요해?
A. 사용자가 입력창의 의미를 이해할 수 있고 테스트도 사용자 관점으로 작성할 수 있기 때문이다.

Q. placeholder만 있으면 label 없이 괜찮아?
A. 권장하지 않는다. label 또는 aria-label을 제공하는 것이 좋다.

Q. getByLabelText가 실패하면 뭘 확인해?
A. label과 input의 htmlFor/id 연결, aria-label, aria-labelledby를 확인한다.

---

## 8.2 Form Error Accessibility Test

### [개념]

Form Error Accessibility Test는 오류 메시지가 보조기술에 전달될 수 있도록 role, aria-invalid, aria-describedby가 올바르게 적용되는지 검증하는 테스트다.

---

### [핵심]

- form error accessibility
- aria-invalid
- aria-describedby
- role alert
- error summary
- field error
- global error
- accessible error message
- focus management

---

### [실무]

예:

```tsx
test("이메일 오류가 발생하면 aria-invalid와 오류 메시지를 연결한다", async () => {
  const user = userEvent.setup();

  render(<LoginForm onLogin={vi.fn()} />);

  const emailInput = screen.getByLabelText("이메일");

  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(emailInput).toHaveAttribute("aria-invalid", "true");
  expect(emailInput).toHaveAttribute("aria-describedby", "email-error");
  expect(screen.getByRole("alert")).toHaveTextContent(
    "이메일을 입력해 주세요.",
  );
});
```

권장:

- field error는 input과 연결
- global error는 role alert 사용 고려
- 오류 발생 후 focus 이동 정책이 있으면 테스트
- 오류 summary가 있으면 link / focus 동작 검증
- 접근성 속성만 검증하지 말고 실제 오류 메시지도 검증

---

### [FAQ]

Q. Form 오류 접근성은 왜 테스트해?
A. 오류가 시각 사용자뿐 아니라 보조기술 사용자에게도 전달되어야 하기 때문이다.

Q. aria-invalid는 언제 true가 돼야 해?
A. 해당 field에 validation error가 있을 때 true로 설정한다.

Q. role alert는 언제 사용해?
A. 사용자가 즉시 알아야 하는 오류 메시지를 전달할 때 사용할 수 있다.

---

# 9. Form Test Troubleshooting

## 9.1 Input Value Not Changing

### [개념]

Input Value Not Changing은 user.type이나 user.clear를 실행했는데 input 값이 바뀌지 않는 상황이다.

Controlled Component, onChange 연결, disabled/readOnly 상태를 확인해야 한다.

---

### [핵심]

원인:

- controlled component wrapper 없음
- onChange 누락
- value 고정
- disabled input
- readOnly input
- wrong query target
- await 누락
- masked input
- custom input wrapper

---

### [실무]

Debug Flow:

```text
input 값 변경 안 됨
→ user.type await 확인
→ input이 disabled/readOnly인지 확인
→ controlled component인지 확인
→ onChange가 value를 업데이트하는지 확인
→ 올바른 input을 query했는지 확인
→ custom input이면 실제 input 요소 확인
```

문제 예:

```tsx
render(<EmailInput value="" onChange={vi.fn()} />);

await user.type(screen.getByLabelText("이메일"), "test@example.com");

expect(screen.getByLabelText("이메일")).toHaveValue("test@example.com");
```

개선:

```tsx
function EmailInputWrapper() {
  const [email, setEmail] = useState("");

  return <EmailInput value={email} onChange={setEmail} />;
}
```

---

### [FAQ]

Q. user.type을 했는데 input 값이 안 바뀌어.
A. controlled component에서 부모 state를 업데이트하는 wrapper가 없을 수 있다.

Q. input이 readOnly면 user.type이 동작해?
A. 값 변경이 되지 않는다. readOnly 상태가 의도된 것인지 확인해야 한다.

Q. custom input에서 값이 안 바뀌면?
A. label이 실제 input에 연결되어 있는지, query 대상이 실제 input인지 확인한다.

---

## 9.2 Submit Not Working

### [개념]

Submit Not Working은 사용자가 Form을 제출했지만 callback, API mock, validation, success UI가 예상대로 동작하지 않는 상황이다.

Form button type, validation 조건, async 처리, mock 설정을 확인해야 한다.

---

### [핵심]

원인:

- button type 문제
- form onSubmit 연결 누락
- preventDefault 처리 문제
- validation 실패
- required field 누락
- disabled button
- await 누락
- mockRejectedValue / mockResolvedValue 누락
- async result에 getBy 사용
- callback argument mismatch

---

### [실무]

Debug Flow:

```text
submit 동작 안 함
→ submit button type 확인
→ form onSubmit 연결 확인
→ 필수 입력값 입력 여부 확인
→ validation error 확인
→ button disabled 여부 확인
→ userEvent await 확인
→ callback 호출 여부 확인
→ mock resolve/reject 확인
→ async 결과는 findBy 사용
```

button type 권장:

```tsx
<button type="submit">등록</button>
<button type="button">취소</button>
```

테스트:

```tsx
await user.click(screen.getByRole("button", { name: "등록" }));

expect(onSubmit).toHaveBeenCalled();
```

---

### [FAQ]

Q. submit 버튼을 눌렀는데 onSubmit이 호출되지 않아.
A. button type, Form onSubmit 연결, validation 실패, disabled 상태를 확인한다.

Q. button type은 왜 중요해?
A. Form 내부 button은 기본 submit이 될 수 있으므로 취소 버튼에는 type="button"을 명시해야 한다.

Q. submit 후 성공 메시지를 못 찾으면?
A. 비동기 결과일 수 있으므로 findBy를 사용하고 mockResolvedValue 설정을 확인한다.

---

## 9.3 Validation Message Not Showing

### [개념]

Validation Message Not Showing은 잘못된 입력을 했는데 오류 메시지가 표시되지 않는 상황이다.

Validation trigger, blur/change/submit 시점, 오류 상태 연결, query 선택을 확인해야 한다.

---

### [핵심]

원인:

- validation trigger 다름
- submit을 실행하지 않음
- blur 이벤트 필요
- touched 상태 미충족
- error state 연결 누락
- field name mismatch
- schema key mismatch
- async validation 미대기
- getBy 대신 findBy 필요

---

### [실무]

Debug Flow:

```text
오류 메시지 안 보임
→ validation 발생 시점 확인
→ submit / blur / change 중 무엇인지 확인
→ required field 조건 확인
→ field name과 error key 확인
→ error UI 렌더링 조건 확인
→ async validation이면 findBy 사용
```

blur validation 예:

```tsx
await user.type(screen.getByLabelText("이메일"), "wrong-email");
await user.tab();

expect(screen.getByText("올바른 이메일 형식이 아닙니다.")).toBeInTheDocument();
```

submit validation 예:

```tsx
await user.click(screen.getByRole("button", { name: "로그인" }));

expect(screen.getByText("이메일을 입력해 주세요.")).toBeInTheDocument();
```

---

### [FAQ]

Q. 오류 메시지가 안 보이면 뭘 확인해?
A. validation이 submit, blur, change 중 언제 발생하는지 먼저 확인한다.

Q. blur validation은 어떻게 테스트해?
A. 입력 후 `await user.tab()`으로 focus를 이동시켜 blur를 발생시킨다.

Q. async validation 오류는 어떤 Query를 써?
A. 비동기로 나타나면 `findByText` 또는 `findByRole`을 사용한다.

---

# 10. Form Testing Anti Pattern

## 10.1 Common Form Testing Anti Patterns

### [개념]

Form Testing Anti Pattern은 Form 테스트가 실제 사용자 흐름과 다르거나 유지보수성이 낮아지는 잘못된 작성 방식이다.

Form 테스트는 label 기반 query, userEvent, validation, submit 결과 중심으로 작성해야 한다.

---

### [핵심]

Anti Pattern:

- label 없는 input을 testId로만 찾음
- fireEvent.change 남용
- userEvent await 누락
- submit 함수 직접 호출
- validation 메시지 미검증
- invalid submit에서 callback not called 미검증
- 실제 API 호출
- server error shape 불일치
- password / token 실제 값 사용
- button type 미검증
- field error와 global error 혼동
- loading disabled 미검증
- getBy로 async error 검증
- Form 내부 state 직접 확인

---

### [실무]

나쁜 예:

```tsx
fireEvent.change(screen.getByTestId("email"), {
  target: { value: "test@example.com" },
});

handleSubmit();

expect(handleSubmit).toHaveBeenCalled();
```

좋은 예:

```tsx
await user.type(screen.getByLabelText("이메일"), "test@example.com");
await user.type(screen.getByLabelText("비밀번호"), "password123");
await user.click(screen.getByRole("button", { name: "로그인" }));

expect(await screen.findByText("로그인 성공")).toBeInTheDocument();
```

검수 기준:

```text
Form 요소를 label로 찾는가?
사용자 입력을 userEvent로 수행하는가?
validation 오류를 화면에서 확인하는가?
submit 결과를 사용자 UI로 검증하는가?
실제 API와 secret을 사용하지 않는가?
```

---

### [FAQ]

Q. Form Testing에서 가장 흔한 실수는 뭐야?
A. label 없이 testId로 찾거나 fireEvent.change만 사용하고 실제 submit 결과를 검증하지 않는 것이다.

Q. submit 함수를 직접 호출하면 왜 안 좋아?
A. 사용자가 실제로 입력하고 버튼을 누르는 흐름을 검증하지 못하기 때문이다.

Q. Form 내부 state를 확인하면 안 돼?
A. 권장하지 않는다. 입력값, 오류 메시지, submit 결과처럼 사용자 결과를 검증한다.

---

# 11. Form Testing Checklist

## 11.1 Form Testing Checklist

### [개념]

Form Testing Checklist는 Form 테스트가 사용자 입력, validation, submit, 상태 UI, 접근성 기준을 만족하는지 검수하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] Form 요소를 label 또는 role로 찾는가?
- [ ] userEvent.setup()을 사용했는가?
- [ ] user.type / click / selectOptions에 await를 사용했는가?
- [ ] input / textarea 값 반영을 검증했는가?
- [ ] select / checkbox / radio 상태를 검증했는가?
- [ ] required validation을 테스트했는가?
- [ ] format validation을 테스트했는가?
- [ ] invalid submit 시 callback / API가 호출되지 않는지 확인했는가?
- [ ] field error와 global error를 구분했는가?
- [ ] server validation error mock shape가 실제 코드와 맞는가?
- [ ] submit loading 중 button disabled를 검증했는가?
- [ ] success UI를 검증했는가?
- [ ] error UI를 검증했는가?
- [ ] file upload는 더미 File 객체를 사용했는가?
- [ ] aria-invalid / role alert 등 오류 접근성을 고려했는가?
- [ ] 실제 password / token / 개인정보를 사용하지 않았는가?
```

---

### [실무]

Agent Form Test 작성 Flow:

```text
Identify Form Fields
→ Query Fields by Label
→ Fill with userEvent
→ Submit by Button or Enter
→ Validate Client Errors
→ Mock Server Result if Needed
→ Assert Loading / Success / Error UI
→ Check Accessibility
→ Check Security Test Data
```

예:

```text
Signup Form
→ email 입력
→ password 입력
→ password confirm 입력
→ terms checkbox 선택
→ submit
→ duplicate email server error
→ field error 표시
```

---

### [FAQ]

Q. Form Testing Checklist의 핵심은 뭐야?
A. label 기반 query, userEvent, validation, submit 결과, loading/success/error UI 검증이다.

Q. Form Test 작성 전 무엇을 정해야 해?
A. field 목록, validation 규칙, submit 결과, 서버 오류 shape, 접근성 요구사항을 정해야 한다.

Q. Form Test가 너무 길어지면 어떻게 해?
A. validation, submit success, submit error를 테스트 케이스로 분리한다.

---

# 12. Part07 Summary

## 12.1 Form Testing Final Rule

### [개념]

Frontend Testing Part07은 React Form 테스트의 입력, 선택, validation, submit, 서버 오류, 파일 업로드, 접근성 기준을 정의한다.

이 Part의 목적은 Agent가 실제 사용자 입력 흐름을 기준으로 Form 기능을 안정적으로 검증하게 만드는 것이다.

---

### [핵심]

최종 기준:

- Form 요소는 label / role 기반 query 사용
- userEvent 기반 입력과 제출 우선
- userEvent에는 await 사용
- input / textarea는 toHaveValue로 검증
- select는 selectOptions / toHaveValue 검증
- checkbox / radio는 toBeChecked 검증
- validation은 사용자 행동으로 발생시킴
- invalid submit 시 callback / API 호출 방지 확인
- field error와 global error 구분
- server validation error shape는 실제 코드와 일치
- submit loading / success / error UI 검증
- file upload는 더미 File 객체 사용
- Form error 접근성 확인
- 실제 secret / token / 개인정보 사용 금지

---

### [실무]

Agent 작업 Flow:

```text
Form Testing Request
→ Identify Field Types
→ Render Form
→ Query by Label / Role
→ Fill Inputs with userEvent
→ Trigger Validation / Submit
→ Assert Field / Global Error
→ Mock Server Success / Error
→ Assert Loading / Success / Error State
→ Review Accessibility / Security
```

Part08 이후 연결:

```text
Part07 Form Testing
→ Part08 API Mocking
→ Part09 Loading Error Empty
→ Part10 Router Auth Testing
→ Part11 TanStack Query Testing
→ Part12 Accessibility Testing
```

---

### [FAQ]

Q. Part07의 최종 목적은 뭐야?
A. Frontend Agent가 Form 입력, validation, submit, 오류 상태를 사용자 흐름 기준으로 테스트하게 만드는 것이다.

Q. Form Testing에서 가장 중요한 규칙은 뭐야?
A. label 기반 query와 userEvent를 사용하고, submit 결과를 화면 UI로 검증하는 것이다.

Q. Part07 다음에는 어떤 내용이 이어져야 해?
A. API 함수 mock, MSW, error response mock, server state mock을 다루는 API Mocking 기준이 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Form Testing은 뭐야?
A. 사용자가 Form을 입력하고 제출하는 흐름과 validation, loading, success, error UI를 검증하는 테스트다.

Q. Form Testing에서 가장 중요한 기준은 뭐야?
A. 사용자가 실제로 입력하고 제출하는 흐름을 userEvent로 재현하고 화면 결과를 검증하는 것이다.

Q. input value만 확인하면 충분해?
A. 부족하다. validation, submit 결과, API 상태, 오류 메시지도 함께 검증해야 한다.

Q. Form Testing은 Component Test야 Integration Test야?
A. 단순 Form 입력과 callback 검증은 Component Test이고 API, Router, Auth Store가 엮이면 Integration Test에 가깝다.

Q. 실제 API를 호출해 Form을 테스트해도 돼?
A. 일반 Form Test에서는 권장하지 않는다. API 응답은 mock으로 제어한다.

Q. Text Input Test는 어떻게 작성해?
A. label로 input을 찾고 `await user.type`으로 입력한 뒤 `toHaveValue`로 검증한다.

Q. password input은 어떤 Query를 써?
A. `getByLabelText("비밀번호")`가 안전하다.

Q. 테스트에 실제 비밀번호를 써도 돼?
A. 안 된다. 더미 값을 사용한다.

Q. textarea는 어떻게 테스트해?
A. `getByLabelText`로 찾고 `user.type` 후 `toHaveValue`로 입력값을 검증한다.

Q. textarea에서 Enter는 submit이야?
A. 보통 줄바꿈이다. Form 설계에 따라 다르므로 사용자 동작 기준으로 테스트한다.

Q. input clear는 어떻게 테스트해?
A. `await user.clear(input)` 후 값이 빈 문자열인지 확인한다.

Q. Form reset은 뭘 확인해야 해?
A. input, select, checkbox, validation message, filter 결과가 초기화되는지 확인한다.

Q. select는 어떻게 테스트해?
A. `user.selectOptions`로 option을 선택하고 `toHaveValue` 또는 `toBeSelected`로 확인한다.

Q. custom select도 selectOptions를 써?
A. native select가 아니라면 실제 사용자처럼 trigger를 클릭하고 option을 선택한다.

Q. checkbox는 어떻게 테스트해?
A. `getByRole("checkbox", { name })`로 찾고 `await user.click` 후 `toBeChecked`로 검증한다.

Q. 약관 동의 validation도 테스트해야 해?
A. 회원가입처럼 중요한 Form에서는 테스트하는 것이 좋다.

Q. radio는 어떻게 테스트해?
A. `getByRole("radio", { name })`로 찾고 클릭 후 `toBeChecked`로 검증한다.

Q. radio group에서는 무엇을 확인해야 해?
A. 선택한 option만 checked이고 다른 option은 unchecked인지 확인한다.

Q. Client Validation Test는 뭐야?
A. 잘못된 입력값에 대해 Frontend가 오류 메시지를 표시하고 submit을 막는지 검증하는 테스트다.

Q. validation 함수만 Unit Test하면 충분해?
A. 아니다. Component에서 실제 오류 메시지가 표시되는지도 테스트해야 한다.

Q. invalid submit 시 무엇을 확인해야 해?
A. 오류 메시지 표시와 submit callback 또는 API 요청이 실행되지 않는지 확인한다.

Q. Field Error는 뭘 테스트해?
A. 특정 입력값 오류 메시지와 해당 input의 오류 접근성 상태를 테스트한다.

Q. aria-invalid도 테스트해야 해?
A. 접근성이 중요한 Form에서는 테스트하는 것이 좋다.

Q. Global Error는 뭐야?
A. 특정 field가 아니라 Form 전체에 해당하는 오류 메시지다.

Q. 로그인 실패는 Field Error야 Global Error야?
A. 보통 이메일 또는 비밀번호 조합 실패는 Global Error로 처리한다.

Q. Password Confirm Test는 왜 필요해?
A. 회원가입에서 자주 발생하는 입력 오류이며 submit 방지가 중요하기 때문이다.

Q. 비밀번호 확인 오류는 Field Error야?
A. 일반적으로 비밀번호 확인 field의 Field Error로 처리한다.

Q. Submit Callback Test는 뭐야?
A. Form 제출 시 onSubmit 같은 callback이 올바른 Form 값으로 호출되는지 검증하는 테스트다.

Q. submit 값의 trim도 테스트해야 해?
A. Form 정책에 포함된 변환이라면 테스트하는 것이 좋다.

Q. Submit Loading Test는 왜 필요해?
A. 중복 제출을 막고 사용자에게 처리 중 상태를 알려주는지 확인하기 위해 필요하다.

Q. 중복 제출 방지는 어떻게 테스트해?
A. submit 중 버튼이 disabled되고 callback이 한 번만 호출되는지 확인한다.

Q. Submit Success Test는 뭘 확인해?
A. 성공 메시지, Form reset, redirect, Modal close, 목록 갱신 같은 사용자 결과를 확인한다.

Q. 성공 메시지는 findBy로 찾아야 해?
A. 비동기 submit 결과라면 `await screen.findByText`를 사용한다.

Q. Submit Error Test는 뭘 확인해?
A. 오류 메시지 표시, 버튼 상태 복구, field/global error 구분, 재시도 가능 여부를 확인한다.

Q. 제출 실패 후 버튼은 다시 활성화되어야 해?
A. 일반적으로 재시도를 위해 다시 활성화되어야 한다.

Q. Server Field Error는 뭐야?
A. 서버가 특정 field에 대해 반환한 validation error를 Form field 오류로 표시하는 것이다.

Q. mockRejectedValue 구조는 실제 AxiosError와 같아야 해?
A. 가능하면 실제 코드가 참조하는 `error.response.status`, `error.response.data` 구조와 맞춰야 한다.

Q. 서버 validation error도 테스트해야 해?
A. 중요한 Form에서는 해야 한다. 클라이언트에서 잡지 못한 오류를 사용자에게 올바르게 표시해야 한다.

Q. Server Global Error는 뭐야?
A. 특정 field가 아니라 Form 전체에 표시해야 하는 서버 오류다.

Q. 500 에러는 어떻게 표시해야 해?
A. 서버 내부 상세 대신 일반적인 오류 안내 메시지를 표시하는 것이 좋다.

Q. File Input Test는 어떻게 작성해?
A. `new File()`로 더미 파일을 만들고 `await user.upload(input, file)`로 업로드한다.

Q. 실제 파일을 테스트에 넣어도 돼?
A. 가능하면 더미 File 객체를 사용하고 실제 민감 파일은 사용하지 않는다.

Q. File Validation은 뭘 테스트해?
A. 파일 형식, 파일 크기, 필수 파일 누락, 파일 개수 제한을 테스트한다.

Q. 큰 파일 테스트는 실제 큰 파일이 필요해?
A. `new File()`로 더미 content를 만들어 크기 조건을 재현할 수 있다.

Q. Form Label Test는 왜 필요해?
A. 사용자가 입력창의 의미를 이해할 수 있고 테스트도 사용자 관점으로 작성할 수 있기 때문이다.

Q. placeholder만 있으면 label 없이 괜찮아?
A. 권장하지 않는다. label 또는 aria-label을 제공하는 것이 좋다.

Q. Form 오류 접근성은 왜 테스트해?
A. 오류가 시각 사용자뿐 아니라 보조기술 사용자에게도 전달되어야 하기 때문이다.

Q. user.type을 했는데 input 값이 안 바뀌어.
A. controlled component에서 부모 state를 업데이트하는 wrapper가 없을 수 있다.

Q. submit 버튼을 눌렀는데 onSubmit이 호출되지 않아.
A. button type, Form onSubmit 연결, validation 실패, disabled 상태를 확인한다.

Q. 오류 메시지가 안 보이면 뭘 확인해?
A. validation이 submit, blur, change 중 언제 발생하는지 먼저 확인한다.

Q. Form Testing에서 가장 흔한 실수는 뭐야?
A. label 없이 testId로 찾거나 fireEvent.change만 사용하고 실제 submit 결과를 검증하지 않는 것이다.

Q. Form Testing Checklist의 핵심은 뭐야?
A. label 기반 query, userEvent, validation, submit 결과, loading/success/error UI 검증이다.

Q. Part07 Form Testing의 최종 목표는 뭐야?
A. Frontend Agent가 Form 입력, validation, submit, 오류 상태를 사용자 흐름 기준으로 테스트하게 만드는 것이다.
