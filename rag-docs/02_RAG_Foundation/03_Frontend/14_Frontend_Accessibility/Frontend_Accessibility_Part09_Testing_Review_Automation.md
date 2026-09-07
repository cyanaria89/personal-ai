# Frontend Accessibility Part09 - Testing Review Automation

---

# 1. Accessibility Testing Foundation

## 1.1 Accessibility Testing Purpose

### [개념]

Accessibility Testing은 Frontend UI가 semantic HTML, keyboard, focus, ARIA, form label, error message, state feedback 기준을 만족하는지 검증하는 과정이다.

접근성 테스트는 자동화 테스트만 의미하지 않는다.

Testing Library, axe, keyboard 수동 점검, 시각 검토, 코드 리뷰를 함께 사용해야 접근성 누락을 줄일 수 있다.

---

### [핵심]

Accessibility Testing 핵심 축:

- Testing Library Query
- User Event Test
- Keyboard Manual Test
- Focus Manual Check
- axe Automated Test
- Semantic HTML Review
- Form Label Review
- ARIA State Review
- Color Contrast Check
- Screen Reader Basic Check
- Component Review
- Regression Test

검증 대상:

- role
- accessible name
- label
- description
- keyboard interaction
- focus visible
- focus management
- error message
- loading state
- empty state
- modal / dropdown / tab
- image alt
- color only meaning

---

### [실무]

Accessibility Testing Flow:

```text
Component 구현
→ Testing Library role / label query 작성
→ userEvent keyboard interaction 작성
→ axe basic check 실행
→ keyboard only manual check
→ focus visible manual check
→ color / visual state check
→ Review Checklist 적용
→ Regression Test 유지
```

실무 기준:

- `getByRole` 우선
- Form은 `getByLabelText` 우선
- Error는 `getByRole("alert")` 또는 error text 확인
- Loading은 `getByRole("status")` 또는 loading text 확인
- Modal은 `getByRole("dialog", { name })` 확인
- IconButton은 role/name으로 확인
- Dropdown / Accordion은 `aria-expanded` 확인
- Tab은 `aria-selected` 확인
- keyboard 흐름은 수동 점검 필수
- axe 통과만으로 접근성 완료 판단 금지

---

### [FAQ]

Q. Accessibility Testing은 왜 필요해?
A. 접근성 문제는 눈으로만 확인하기 어렵고, 테스트와 리뷰를 통해 semantic, keyboard, focus, ARIA 누락을 줄일 수 있기 때문이다.

Q. 자동화 테스트만 있으면 접근성 검증이 끝나?
A. 아니다. keyboard 흐름, focus visible, 문구 품질, 색상 의미는 수동 검토가 필요하다.

Q. 접근성 테스트에서 가장 먼저 할 것은?
A. Testing Library의 getByRole, getByLabelText로 사용자가 인식하는 구조를 검증하는 것이다.

Q. axe 테스트를 통과하면 접근성 문제 없는 거야?
A. 아니다. axe는 일부 오류만 탐지하며 실제 사용 흐름은 수동 점검해야 한다.

---

# 2. Testing Library Query Priority

## 2.1 Query Priority Rules

### [개념]

Testing Library Query Priority는 사용자가 실제로 인식하는 방식과 가까운 Query를 우선 사용하는 기준이다.

접근성 있는 UI는 role, label, text, alt text로 자연스럽게 찾을 수 있어야 한다.

`testId`는 접근성 구조를 검증하지 못하므로 최후 수단으로 사용한다.

---

### [핵심]

Query 우선순위:

1. `getByRole`
2. `getByLabelText`
3. `getByPlaceholderText`
4. `getByText`
5. `getByDisplayValue`
6. `getByAltText`
7. `getByTitle`
8. `getByTestId`

권장 Query:

- Button: `getByRole("button", { name })`
- Link: `getByRole("link", { name })`
- Input: `getByLabelText`
- Select: `getByRole("combobox", { name })`
- Checkbox: `getByRole("checkbox", { name })`
- Radio: `getByRole("radio", { name })`
- Dialog: `getByRole("dialog", { name })`
- Alert: `getByRole("alert")`
- Status: `getByRole("status")`

---

### [실무]

Button Query:

```tsx
screen.getByRole("button", { name: "저장" });
```

Link Query:

```tsx
screen.getByRole("link", { name: "축제 목록 보기" });
```

Input Query:

```tsx
screen.getByLabelText("이메일");
```

Dialog Query:

```tsx
screen.getByRole("dialog", { name: "리뷰 작성" });
```

Alert Query:

```tsx
screen.getByRole("alert");
```

실무 기준:

- 사용자가 인식하는 이름으로 요소를 찾음
- `getByRole` 실패 시 role과 accessible name 확인
- `getByLabelText` 실패 시 label 연결 확인
- `getByTestId`는 복잡한 비사용자 노출 요소에 제한적으로 사용
- Query 실패를 접근성 개선 신호로 활용
- 테스트 문구는 사용자용 문구와 동기화

---

### [FAQ]

Q. Testing Library에서 어떤 Query를 먼저 써야 해?
A. getByRole을 우선 사용하고 Form Control은 getByLabelText를 우선 사용한다.

Q. getByRole이 좋은 이유는?
A. 사용자가 인식하는 role과 accessible name 기준으로 요소를 찾기 때문에 접근성 구조를 검증할 수 있다.

Q. getByTestId를 쓰면 안 돼?
A. 필요한 경우 가능하지만 접근성 구조를 검증하지 못하므로 최후 수단으로 두는 것이 좋다.

Q. getByRole이 실패하면 어떻게 해?
A. semantic element, role, accessible name, hidden 상태를 확인한다.

---

## 2.2 getByRole Rules

### [개념]

`getByRole`은 요소의 semantic role과 accessible name을 기준으로 UI를 찾는 Query다.

접근성 테스트에서 가장 강력한 Query이며 Button, Link, Dialog, Heading, Alert, Status, Tab, Table 등 많은 요소를 검증할 수 있다.

---

### [핵심]

자주 쓰는 Role:

- `button`
- `link`
- `heading`
- `textbox`
- `checkbox`
- `radio`
- `combobox`
- `dialog`
- `alert`
- `status`
- `tab`
- `tabpanel`
- `navigation`
- `main`
- `table`
- `row`
- `cell`

검증 가능 항목:

- semantic role
- accessible name
- heading level
- hidden 여부
- selected 상태 일부
- checked 상태 일부
- expanded 상태는 attribute 확인

---

### [실무]

Heading:

```tsx
screen.getByRole("heading", {
  name: "축제 목록",
  level: 1,
});
```

Button:

```tsx
screen.getByRole("button", { name: "필터 초기화" });
```

Navigation:

```tsx
screen.getByRole("navigation", { name: "주요 메뉴" });
```

Dialog:

```tsx
screen.getByRole("dialog", { name: "리뷰 삭제" });
```

Tab:

```tsx
screen.getByRole("tab", { name: "리뷰" });
```

실무 기준:

- button/link/dialog/tab은 role과 name으로 찾음
- heading은 level까지 검증 가능
- navigation landmark는 name으로 구분
- icon button은 `aria-label`이 있어야 role/name query 가능
- role query 실패 시 semantic HTML과 ARIA 구조 점검
- hidden 요소는 기본적으로 Query 대상에서 제외될 수 있음

---

### [FAQ]

Q. getByRole로 무엇을 검증할 수 있어?
A. 요소의 role, accessible name, heading level, landmark, dialog name 등을 검증할 수 있다.

Q. icon button은 getByRole로 찾을 수 있어?
A. button에 aria-label이 있으면 getByRole("button", { name })으로 찾을 수 있다.

Q. heading level도 테스트할 수 있어?
A. 가능하다. getByRole("heading", { level: 1 })처럼 검증할 수 있다.

Q. getByRole이 안 잡히면 무조건 role을 붙이면 돼?
A. 아니다. 먼저 적절한 native HTML을 사용했는지 확인해야 한다.

---

## 2.3 getByLabelText Rules

### [개념]

`getByLabelText`는 label과 연결된 Form Control을 찾는 Query다.

Form 접근성 검증에서 가장 중요한 Query 중 하나이며 input, textarea, select, checkbox, radio의 label 연결을 확인할 수 있다.

---

### [핵심]

검증 대상:

- label htmlFor / input id 연결
- wrapping label
- aria-label
- aria-labelledby
- checkbox label
- radio label
- select label
- textarea label
- file input label

실패 원인:

- label 누락
- htmlFor / id 불일치
- id 중복
- label text 오타
- placeholder만 사용
- hidden label 처리 오류
- custom component label 미연결

---

### [실무]

Input Test:

```tsx
screen.getByLabelText("이메일");
screen.getByLabelText("비밀번호");
```

Select Test:

```tsx
screen.getByLabelText("지역");
```

Checkbox Test:

```tsx
screen.getByLabelText("이용약관에 동의합니다.");
```

File Input Test:

```tsx
screen.getByLabelText("리뷰 이미지");
```

실무 기준:

- Form Control은 label로 찾을 수 있어야 함
- placeholder 기반 Query보다 label 기반 Query 우선
- getByLabelText 실패는 접근성 문제 가능성이 높음
- checkbox / radio도 label로 찾을 수 있어야 함
- sr-only label도 Query 가능
- Custom Form Control은 label 연결 방식 검토 필요

---

### [FAQ]

Q. getByLabelText는 언제 써?
A. input, select, textarea, checkbox, radio 같은 Form Control을 label 기준으로 찾을 때 사용한다.

Q. getByLabelText가 실패하면 접근성 문제야?
A. 가능성이 높다. label 연결, id 일치, label text를 확인해야 한다.

Q. placeholder가 있는데 getByLabelText가 실패하면 괜찮아?
A. 권장하지 않는다. placeholder는 label 대체가 아니므로 label을 제공하는 것이 좋다.

Q. sr-only label도 getByLabelText로 찾을 수 있어?
A. 가능하다. 화면에 보이지 않아도 접근성 트리에 제공되면 Query 대상이 될 수 있다.

---

# 3. User Event Keyboard Testing

## 3.1 Keyboard Test Basics

### [개념]

Keyboard Test는 사용자가 마우스 없이 keyboard로 UI를 조작할 수 있는지 검증하는 테스트다.

Testing Library의 `userEvent.tab`, `userEvent.keyboard`를 사용하면 focus 이동, Enter / Space 실행, Escape 닫기 일부를 코드로 검증할 수 있다.

---

### [핵심]

검증 대상:

- Tab focus order
- Shift+Tab reverse order
- Enter activation
- Space activation
- Escape close
- checkbox toggle
- radio selection
- modal close
- dropdown open / close
- focus return
- form submit
- keyboard trap 일부

사용 API:

- `user.tab()`
- `user.keyboard()`
- `toHaveFocus()`
- `toBeChecked()`
- `toBeDisabled()`
- `toHaveAttribute()`

---

### [실무]

Tab Focus Test:

```tsx
test("로그인 Form은 Tab으로 이동할 수 있다", async () => {
  render(<LoginForm />);

  await user.tab();
  expect(screen.getByLabelText("이메일")).toHaveFocus();

  await user.tab();
  expect(screen.getByLabelText("비밀번호")).toHaveFocus();

  await user.tab();
  expect(screen.getByRole("button", { name: "로그인" })).toHaveFocus();
});
```

Escape Close Test:

```tsx
test("Escape로 Dialog를 닫을 수 있다", async () => {
  render(<ReviewDialog />);

  const openButton = screen.getByRole("button", { name: "리뷰 작성" });

  await user.click(openButton);
  expect(screen.getByRole("dialog", { name: "리뷰 작성" })).toBeInTheDocument();

  await user.keyboard("{Escape}");

  expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  expect(openButton).toHaveFocus();
});
```

Space Toggle Test:

```tsx
test("Space로 약관 checkbox를 토글한다", async () => {
  render(<TermsCheckbox />);

  const checkbox = screen.getByRole("checkbox", {
    name: /이용약관에 동의합니다/,
  });

  checkbox.focus();
  await user.keyboard("[Space]");

  expect(checkbox).toBeChecked();
});
```

실무 기준:

- keyboard test는 role / label query와 함께 사용
- `toHaveFocus`로 focus 흐름 검증
- Modal / Dropdown / Form 우선 테스트
- keyboard test가 focus visible 시각 품질까지 보장하지 않음
- 복잡한 widget은 수동 점검 병행
- test environment와 실제 browser 차이를 고려

---

### [FAQ]

Q. Keyboard 접근성도 자동 테스트할 수 있어?
A. 일부 가능하다. userEvent.tab, userEvent.keyboard, toHaveFocus를 사용한다.

Q. keyboard test에서 무엇을 확인해?
A. focus 이동, Enter / Space 실행, Escape 닫기, focus return 등을 확인한다.

Q. keyboard test가 있으면 수동 점검은 생략해도 돼?
A. 아니다. 실제 focus visible, scroll, 복잡한 흐름은 수동 확인이 필요하다.

Q. keyboard test도 getByRole을 써야 해?
A. 권장한다. 사용자가 인식하는 role과 name 기준으로 테스트하는 것이 좋다.

---

## 3.2 Focus Test Rules

### [개념]

Focus Test는 사용자가 keyboard로 이동할 때 focus가 예상되는 위치로 이동하는지 검증하는 테스트다.

Focus Test는 Form, Modal, Dropdown, Route transition, Error Summary에서 중요하다.

---

### [핵심]

검증 대상:

- initial focus
- tab order
- focus visible 대상
- modal open focus
- modal close focus return
- error summary focus
- first invalid field focus
- dynamic field focus
- deleted item focus recovery
- hidden element no focus

---

### [실무]

Modal Open Focus:

```tsx
test("Dialog open 시 title에 focus가 이동한다", async () => {
  render(<ReviewDialog />);

  await user.click(screen.getByRole("button", { name: "리뷰 작성" }));

  expect(screen.getByRole("heading", { name: "리뷰 작성" })).toHaveFocus();
});
```

Error Summary Focus:

```tsx
test("Submit 실패 시 Error Summary로 focus가 이동한다", async () => {
  render(<SignupForm />);

  await user.click(screen.getByRole("button", { name: "회원가입" }));

  const errorSummary = screen.getByRole("alert");

  expect(errorSummary).toHaveTextContent("입력 내용을 확인해 주세요.");
  expect(errorSummary).toHaveFocus();
});
```

Focus Return:

```tsx
test("Dialog close 후 trigger로 focus가 돌아간다", async () => {
  render(<DeleteDialog />);

  const trigger = screen.getByRole("button", { name: "삭제" });

  await user.click(trigger);
  await user.keyboard("{Escape}");

  expect(trigger).toHaveFocus();
});
```

실무 기준:

- focus 이동이 UX상 필요한 경우에만 테스트
- programmatic focus 대상은 `tabIndex={-1}` 필요 가능
- hidden 요소에 focus가 가지 않는지 확인
- focus return은 Modal / Dropdown에서 우선 검증
- focus visible은 코드 테스트보다 수동 확인 필요
- Route focus는 프로젝트 정책에 맞게 테스트

---

### [FAQ]

Q. Focus Test는 언제 필요해?
A. Modal, Form 오류, Error Summary, 동적 UI처럼 focus 이동이 중요한 상황에 필요하다.

Q. 모든 클릭 후 focus를 테스트해야 해?
A. 아니다. 사용자 흐름상 focus 관리가 중요한 interaction을 우선 테스트한다.

Q. focus visible도 테스트 코드로 검증할 수 있어?
A. 제한적이다. 실제 시각적 focus는 수동 확인이 필요하다.

Q. hidden element focus는 왜 문제야?
A. 보이지 않는 요소에 focus가 가면 keyboard 사용자가 현재 위치를 알 수 없기 때문이다.

---

# 4. Form Accessibility Test

## 4.1 Form Query Test

### [개념]

Form Query Test는 Form Control이 label, role, accessible name 기준으로 검색 가능한지 검증하는 테스트다.

Form Accessibility의 기본은 사용자가 입력 필드의 목적을 이해할 수 있는지 확인하는 것이다.

---

### [핵심]

Form Test 대상:

- input label
- select label
- textarea label
- checkbox label
- radio label
- file input label
- submit button name
- required error
- helper text
- field error
- global error
- error summary

---

### [실무]

Login Form:

```tsx
test("로그인 Form은 접근 가능한 label과 submit button을 제공한다", () => {
  render(<LoginForm />);

  expect(screen.getByLabelText("이메일")).toBeInTheDocument();
  expect(screen.getByLabelText("비밀번호")).toBeInTheDocument();
  expect(screen.getByRole("button", { name: "로그인" })).toBeInTheDocument();
});
```

Signup Form:

```tsx
test("회원가입 Form은 약관 checkbox를 label로 찾을 수 있다", () => {
  render(<SignupForm />);

  expect(
    screen.getByRole("checkbox", { name: /이용약관에 동의합니다/ }),
  ).toBeInTheDocument();
});
```

Select:

```tsx
test("지역 select는 label로 찾을 수 있다", () => {
  render(<RegionSelect />);

  expect(screen.getByLabelText("지역")).toBeInTheDocument();
});
```

실무 기준:

- Form Control은 label 기반 Query로 검증
- submit button은 role/name으로 검증
- checkbox / radio는 role/name 또는 label로 검증
- placeholder Query는 보조 수단
- testId로 Form Control을 찾는 테스트는 접근성 누락을 숨길 수 있음

---

### [FAQ]

Q. Form input은 어떤 Query로 테스트해?
A. getByLabelText를 우선 사용한다.

Q. Form submit button은 어떻게 테스트해?
A. getByRole("button", { name: "저장" })처럼 role/name으로 찾는다.

Q. checkbox는 어떻게 테스트해?
A. getByRole("checkbox", { name }) 또는 getByLabelText로 찾는다.

Q. placeholder로 input을 테스트하면 안 돼?
A. 가능하지만 label 접근성을 검증하지 못하므로 label query를 우선 사용한다.

---

## 4.2 Form Error Test

### [개념]

Form Error Test는 validation 실패 시 오류 메시지가 사용자에게 인식 가능한 방식으로 표시되고 input과 연결되는지 검증하는 테스트다.

오류 테스트는 문구, role, aria-invalid, aria-describedby를 함께 확인할 수 있다.

---

### [핵심]

검증 대상:

- required error
- format error
- password mismatch
- field error text
- global error text
- role alert
- aria-invalid
- aria-describedby
- error summary
- focus on error

---

### [실무]

Required Error:

```tsx
test("이메일 미입력 시 오류 메시지를 표시한다", async () => {
  render(<LoginForm />);

  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(screen.getByRole("alert")).toHaveTextContent(
    "이메일을 입력해 주세요.",
  );

  expect(screen.getByLabelText("이메일")).toHaveAttribute(
    "aria-invalid",
    "true",
  );
});
```

aria-describedby:

```tsx
test("이메일 오류 메시지가 input과 연결된다", async () => {
  render(<EmailField error="이메일을 입력해 주세요." />);

  const input = screen.getByLabelText("이메일");
  const error = screen.getByText("이메일을 입력해 주세요.");

  expect(input).toHaveAttribute("aria-describedby", error.id);
});
```

Global Error:

```tsx
test("로그인 실패 시 global error를 표시한다", async () => {
  render(<LoginForm loginError />);

  expect(screen.getByRole("alert")).toHaveTextContent(
    "이메일 또는 비밀번호가 올바르지 않습니다.",
  );
});
```

실무 기준:

- 오류 메시지는 사용자용 문구로 검증
- `aria-invalid`는 오류 상태와 동기화
- `aria-describedby`는 실제 error id와 연결
- role alert 남발 여부는 Review에서 추가 확인
- 긴 Form은 Error Summary 테스트 검토
- 서버 내부 오류 문구 노출 금지 테스트도 가능

---

### [FAQ]

Q. Form Error는 무엇을 테스트해야 해?
A. 오류 문구, role alert, aria-invalid, aria-describedby 연결을 확인한다.

Q. aria-invalid도 테스트해야 해?
A. validation 상태를 전달해야 하는 input이라면 오류 상태와 동기화되는지 확인하는 것이 좋다.

Q. error message와 input 연결은 어떻게 테스트해?
A. input의 aria-describedby가 실제 error message id를 참조하는지 확인한다.

Q. 오류 문구도 테스트해야 해?
A. 그렇다. 사용자가 이해 가능한 문구인지 확인하는 데 도움이 된다.

---

# 5. Component Accessibility Test

## 5.1 Modal Test

### [개념]

Modal Test는 Dialog가 role, accessible name, focus 이동, Escape 닫기, focus return 기준을 만족하는지 검증하는 테스트다.

Modal은 접근성 문제가 자주 발생하므로 공통 Component 단계에서 테스트를 작성하는 것이 좋다.

---

### [핵심]

Modal Test 대상:

- trigger button
- dialog role
- dialog name
- aria-modal
- dialog description
- open focus
- close button
- Escape close
- focus return
- background focus 방지 일부
- confirm / cancel button

---

### [실무]

Dialog Role Test:

```tsx
test("Dialog는 accessible name을 가진다", async () => {
  render(<ReviewDialog />);

  await user.click(screen.getByRole("button", { name: "리뷰 작성" }));

  expect(screen.getByRole("dialog", { name: "리뷰 작성" })).toBeInTheDocument();
});
```

Escape Close and Focus Return:

```tsx
test("Escape로 Dialog를 닫고 trigger로 focus가 돌아간다", async () => {
  render(<ReviewDialog />);

  const trigger = screen.getByRole("button", { name: "리뷰 작성" });

  await user.click(trigger);
  await user.keyboard("{Escape}");

  expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  expect(trigger).toHaveFocus();
});
```

Close Button:

```tsx
test("닫기 버튼으로 Dialog를 닫을 수 있다", async () => {
  render(<ReviewDialog />);

  await user.click(screen.getByRole("button", { name: "리뷰 작성" }));
  await user.click(screen.getByRole("button", { name: "닫기" }));

  expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
});
```

실무 기준:

- Dialog는 role/name으로 검증
- close action은 button name으로 검증
- Escape와 close button 모두 검토
- focus return은 `toHaveFocus`로 확인
- focus trap은 코드 테스트와 수동 점검 병행
- alertdialog는 role alertdialog로 검증

---

### [FAQ]

Q. Modal 접근성 테스트에서 가장 중요한 것은?
A. dialog role/name, focus 이동, Escape 닫기, focus return이다.

Q. Modal title 연결은 어떻게 테스트해?
A. getByRole("dialog", { name: "제목" })으로 accessible name을 확인한다.

Q. focus trap도 자동 테스트해야 해?
A. 일부 테스트 가능하지만 실제 Tab 순환과 visual focus는 수동 점검도 필요하다.

Q. Modal 닫기 버튼은 어떻게 테스트해?
A. getByRole("button", { name: "닫기" })로 찾고 click 또는 keyboard로 닫힘을 확인한다.

---

## 5.2 Dropdown Accordion Tab Test

### [개념]

Dropdown, Accordion, Tab Test는 open / close 상태, selected 상태, ARIA state, keyboard 조작을 검증하는 테스트다.

이 Component들은 ARIA state와 실제 UI state가 어긋나기 쉽다.

---

### [핵심]

Dropdown Test:

- trigger role/name
- `aria-expanded`
- open panel
- Escape close
- hidden item focus 방지

Accordion Test:

- trigger button
- `aria-expanded`
- panel visible / hidden
- Enter / Space toggle

Tab Test:

- tablist
- tab role/name
- `aria-selected`
- tabpanel 연결
- Arrow Key 이동
- hidden panel focus 방지

---

### [실무]

Dropdown Expanded:

```tsx
test("Dropdown open 상태와 aria-expanded가 동기화된다", async () => {
  render(<FilterDropdown />);

  const trigger = screen.getByRole("button", { name: "필터" });

  expect(trigger).toHaveAttribute("aria-expanded", "false");

  await user.click(trigger);

  expect(trigger).toHaveAttribute("aria-expanded", "true");
});
```

Accordion Toggle:

```tsx
test("Accordion은 열림 상태를 aria-expanded로 전달한다", async () => {
  render(<FAQAccordion />);

  const trigger = screen.getByRole("button", { name: "환불 정책" });

  await user.click(trigger);

  expect(trigger).toHaveAttribute("aria-expanded", "true");
  expect(screen.getByText("환불 정책 설명입니다.")).toBeVisible();
});
```

Tab Selected:

```tsx
test("Tab 선택 상태가 aria-selected와 일치한다", async () => {
  render(<FestivalTabs />);

  const reviewTab = screen.getByRole("tab", { name: "리뷰" });

  await user.click(reviewTab);

  expect(reviewTab).toHaveAttribute("aria-selected", "true");
  expect(screen.getByRole("tabpanel", { name: "리뷰" })).toBeVisible();
});
```

실무 기준:

- ARIA state는 실제 UI state와 함께 검증
- hidden panel이 Query에 잡히는지 여부 확인
- keyboard 조작은 userEvent로 일부 검증
- complex widget은 수동 keyboard check 병행
- role을 사용하면 pattern에 맞는 테스트 필요

---

### [FAQ]

Q. Dropdown 테스트에서 무엇을 확인해?
A. trigger button, aria-expanded 동기화, open/close, keyboard 닫기를 확인한다.

Q. Accordion 테스트에서 무엇을 확인해?
A. trigger button과 panel 표시 상태, aria-expanded 동기화를 확인한다.

Q. Tab 테스트에서 무엇을 확인해?
A. role tab, aria-selected, visible tabpanel, keyboard 이동을 확인한다.

Q. aria-expanded나 aria-selected는 꼭 테스트해야 해?
A. 상태 UI에서는 실제 상태와 동기화되는지 테스트하는 것이 좋다.

---

# 6. State Accessibility Test

## 6.1 Loading Success Error Empty Test

### [개념]

State Accessibility Test는 Loading, Success, Error, Empty 상태가 사용자에게 인식 가능한 role과 text로 제공되는지 검증하는 테스트다.

상태 UI는 단순히 렌더링되는지보다 사용자가 현재 상태와 다음 행동을 이해할 수 있는지가 중요하다.

---

### [핵심]

검증 대상:

- loading text
- role status
- success message
- role alert
- error message
- retry button
- empty state heading
- empty state action
- pending button text
- disabled reason
- offline message

---

### [실무]

Loading:

```tsx
expect(screen.getByRole("status")).toHaveTextContent(
  "데이터를 불러오는 중입니다.",
);
```

Success:

```tsx
expect(screen.getByRole("status")).toHaveTextContent("저장되었습니다.");
```

Error:

```tsx
expect(screen.getByRole("alert")).toHaveTextContent("저장에 실패했습니다.");
expect(screen.getByRole("button", { name: "다시 시도" })).toBeInTheDocument();
```

Empty:

```tsx
expect(
  screen.getByRole("heading", { name: "검색 결과가 없습니다." }),
).toBeInTheDocument();
expect(screen.getByRole("button", { name: "필터 초기화" })).toBeInTheDocument();
```

Pending Button:

```tsx
expect(screen.getByRole("button", { name: "저장 중..." })).toBeDisabled();
```

실무 기준:

- loading / success는 role status 검토
- error는 role alert 검토
- empty는 heading과 다음 action 검증
- retry action은 button role/name으로 검증
- pending button은 text 변경과 disabled 확인
- spinner나 skeleton만 있는 상태를 테스트로 허용하지 않음

---

### [FAQ]

Q. Loading 상태는 어떻게 테스트해?
A. role status나 loading text로 사용자가 인식 가능한 상태를 검증한다.

Q. Error 상태는 어떻게 테스트해?
A. role alert와 error message, retry button을 함께 확인한다.

Q. Empty State는 어떻게 테스트해?
A. heading, 설명 문구, 다음 action button 또는 link를 확인한다.

Q. pending button은 어떻게 테스트해?
A. 버튼 text가 “저장 중...”처럼 바뀌고 disabled 또는 aria-busy 상태인지 확인한다.

---

# 7. Image Icon Visual Test

## 7.1 Image and Icon Test

### [개념]

Image and Icon Test는 이미지 alt, 장식 이미지 처리, IconButton accessible name, 상태 icon text가 올바르게 제공되는지 검증하는 테스트다.

이미지와 아이콘은 시각적으로는 명확해 보여도 보조기술에는 의미가 없거나 과도하게 노출될 수 있다.

---

### [핵심]

검증 대상:

- informative image alt
- decorative image empty alt
- linked image purpose
- icon button accessible name
- status message text
- loading spinner text
- error icon with text
- chart description text

---

### [실무]

Informative Image:

```tsx
expect(screen.getByAltText("봄꽃 축제 행사장 전경")).toBeInTheDocument();
```

IconButton:

```tsx
expect(screen.getByRole("button", { name: "알림 열기" })).toBeInTheDocument();
```

Status Icon with Text:

```tsx
expect(screen.getByText("저장되었습니다.")).toBeInTheDocument();
```

Loading Spinner with Text:

```tsx
expect(screen.getByRole("status")).toHaveTextContent("처리 중입니다.");
```

Chart Description:

```tsx
expect(screen.getByText(/2026년 1월부터 6월까지 매출/)).toBeInTheDocument();
```

실무 기준:

- 정보 이미지는 alt로 검증
- 장식 이미지는 불필요하게 이름이 노출되지 않게 검토
- IconButton은 role/name으로 검증
- status icon은 텍스트 문구로 검증
- chart는 alt뿐 아니라 설명 문구나 table 검증
- 색상 대비는 전용 도구와 수동 검토 필요

---

### [FAQ]

Q. 이미지 alt는 테스트할 수 있어?
A. 가능하다. getByAltText로 정보 이미지의 alt를 확인할 수 있다.

Q. IconButton 접근성은 어떻게 테스트해?
A. getByRole("button", { name })으로 accessible name을 검증한다.

Q. 상태 아이콘은 어떻게 테스트해?
A. 아이콘만 검증하기보다 상태 텍스트가 제공되는지 확인한다.

Q. 색상 대비도 Testing Library로 테스트해?
A. 일반적으로 색상 대비는 전용 도구나 수동 검토가 필요하다.

---

# 8. axe Automated Testing

## 8.1 axe Testing Purpose

### [개념]

axe Automated Testing은 접근성 규칙 기반 도구로 label 누락, role 오류, ARIA 참조 오류, alt 누락, 일부 contrast 문제를 자동 탐지할 수 있다.

axe는 유용하지만 접근성 전체를 보장하지 않는다.

자동화 도구는 사람이 놓치기 쉬운 정적 문제를 찾는 보조 수단이다.

---

### [핵심]

axe가 잘 찾는 문제:

- missing image alt
- missing form label
- empty button name
- invalid ARIA attribute
- invalid ARIA role
- broken aria reference
- aria-hidden focus issue 일부
- required role children 누락
- heading / landmark 일부 문제
- color contrast 일부 문제

axe가 부족한 문제:

- alt text 품질
- keyboard flow 전체
- focus return 의도
- focus visible 품질
- color only meaning
- 문구 품질
- custom widget 사용성
- screen reader 실제 경험
- 업무 흐름 맥락

---

### [실무]

axe 적용 우선순위:

```text
Common Component
→ Form
→ Modal
→ Dropdown
→ Tab
→ Page Template
→ Table
→ Dashboard
```

실무 기준:

- axe 오류는 무시하지 말고 원인 확인
- axe 통과는 접근성 완료가 아님
- axe 결과는 Testing Library Query와 함께 해석
- keyboard manual check와 병행
- contrast 오류는 design token 수정으로 연결
- CI 연동은 프로젝트 규모에 따라 단계적으로 적용

---

### [FAQ]

Q. axe는 무엇을 찾아줘?
A. label 누락, role 오류, ARIA 참조 오류, alt 누락, 일부 contrast 문제를 찾을 수 있다.

Q. axe 테스트만 통과하면 접근성 완료야?
A. 아니다. keyboard, focus, 문구, 사용자 흐름은 수동 검토가 필요하다.

Q. axe 오류는 무조건 수정해야 해?
A. 대부분 원인을 확인해야 한다. 예외가 있다면 명확한 이유와 대체 검증이 필요하다.

Q. axe는 어디에 우선 적용해?
A. Form, Modal, 공통 Component처럼 접근성 영향이 큰 곳에 우선 적용한다.

---

## 8.2 axe and Testing Library Integration

### [개념]

axe와 Testing Library를 함께 사용하면 렌더링된 React Component에 대해 기본 접근성 규칙을 자동 검사할 수 있다.

Testing Library는 사용자 관점 Query를 검증하고 axe는 규칙 기반 오류를 탐지한다.

---

### [핵심]

통합 검증 대상:

- Component render
- Page render
- Modal open state
- Dropdown open state
- Form error state
- Loading state
- Empty state
- Dark mode state 선택
- Responsive state 선택

---

### [실무]

예시 패턴:

```tsx
test("LoginForm은 기본 접근성 위반이 없다", async () => {
  const { container } = render(<LoginForm />);

  const results = await axe(container);

  expect(results).toHaveNoViolations();
});
```

상태별 검사:

```tsx
test("Dialog open 상태에서 접근성 위반이 없다", async () => {
  const { container } = render(<ReviewDialog />);

  await user.click(screen.getByRole("button", { name: "리뷰 작성" }));

  const results = await axe(container);

  expect(results).toHaveNoViolations();
});
```

실무 기준:

- closed 상태만 검사하지 말고 open / error / loading 상태도 검사
- Modal, Dropdown은 열린 상태에서 검사
- Form은 error 상태도 검사
- axe 결과는 Snapshot처럼 방치하지 않음
- 테스트 성능 부담이 있으면 핵심 Component 중심으로 적용
- false positive / 예외는 별도 주석으로 관리

---

### [FAQ]

Q. axe는 React Component 테스트에 붙일 수 있어?
A. 가능하다. Testing Library로 렌더링한 container에 axe를 실행할 수 있다.

Q. axe는 열린 Modal 상태도 검사해야 해?
A. 그렇다. 닫힌 상태만 검사하면 Modal 내부 접근성 문제를 놓칠 수 있다.

Q. Form error 상태도 axe 검사해야 해?
A. 가능하면 검사하는 것이 좋다. 오류 메시지와 aria 연결 문제가 드러날 수 있다.

Q. axe 테스트가 느리면 어떻게 해?
A. 모든 테스트에 넣기보다 공통 Component와 핵심 Page 중심으로 적용한다.

---

# 9. Manual Accessibility Review

## 9.1 Manual Keyboard Review

### [개념]

Manual Keyboard Review는 실제 키보드만 사용해 UI를 조작하며 접근성 문제를 찾는 절차다.

자동화 테스트는 keyboard 흐름 전체와 focus visible 품질을 완전히 검증하지 못하므로 수동 점검이 필요하다.

---

### [핵심]

점검 항목:

- Tab 이동
- Shift+Tab 역방향 이동
- Enter 실행
- Space 실행
- Escape 닫기
- Arrow Key navigation
- focus visible
- focus order
- focus trap
- keyboard trap
- focus return
- hidden element focus
- route transition focus

---

### [실무]

Manual Keyboard Flow:

```text
마우스 사용 금지
→ Header Navigation 이동
→ Main Content 이동
→ Form 입력
→ Button 실행
→ Modal 열기 / 닫기
→ Dropdown 열기 / 닫기
→ Error State 확인
→ Retry 실행
→ Focus Return 확인
```

우선 점검 화면:

- Login
- Signup
- Search
- Payment
- Review Form
- Festival Detail
- Modal
- Dropdown
- Tab
- Admin Table
- File Upload
- Navigation

실무 기준:

- keyboard만으로 핵심 user flow 완료 가능해야 함
- focus가 보이지 않거나 사라지면 수정 대상
- Modal은 focus trap과 close 방법 확인
- Dropdown은 닫힌 item focus 방지 확인
- Form 오류 후 focus 흐름 확인
- 수동 점검 결과는 재현 가능한 수정 항목으로 기록

---

### [FAQ]

Q. Manual Keyboard Review는 왜 필요해?
A. 실제 focus 흐름, focus visible, keyboard trap은 자동화 도구가 완전히 검증하지 못하기 때문이다.

Q. keyboard 점검은 어디부터 해?
A. 로그인, 회원가입, 검색, 결제, Modal, Dropdown 같은 핵심 흐름부터 확인한다.

Q. keyboard trap은 어떻게 찾어?
A. Tab, Shift+Tab, Escape, 닫기 버튼으로 빠져나갈 수 있는지 확인한다.

Q. focus visible은 어떻게 확인해?
A. Tab으로 이동하면서 현재 위치가 시각적으로 명확히 보이는지 확인한다.

---

## 9.2 Manual Visual Review

### [개념]

Manual Visual Review는 색상 대비, focus ring, error state, loading state, image alt 목적, responsive zoom, dark mode를 사람이 직접 확인하는 절차다.

시각 접근성은 자동화 도구만으로 완전히 판단하기 어렵다.

---

### [핵심]

점검 항목:

- color contrast
- color only meaning
- focus ring visibility
- focus ring clipping
- dark mode contrast
- placeholder readability
- disabled readability
- text zoom
- responsive layout
- image alt quality
- icon button name
- chart description
- reduced motion

---

### [실무]

Manual Visual Flow:

```text
Text Contrast 확인
→ Link 구분 확인
→ Error / Success 색상 외 단서 확인
→ Focus Ring 확인
→ Dark Mode 확인
→ Zoom 확인
→ Image / Icon 의미 확인
→ Motion 설정 확인
```

실무 기준:

- 색상 대비는 도구로 확인
- 색상만으로 상태 전달 금지
- focus ring이 충분히 보이는지 확인
- 다크모드에서 focus와 text 대비 확인
- 브라우저 zoom에서 텍스트 clipping 확인
- chart는 text summary 또는 table 확인
- reduced motion 환경에서 animation 확인

---

### [FAQ]

Q. Manual Visual Review는 왜 필요해?
A. 색상 의미, focus 시각 품질, 이미지 alt 품질, zoom 사용성은 자동화만으로 판단하기 어렵기 때문이다.

Q. 색상 대비는 어떻게 확인해?
A. contrast checker 같은 도구를 사용하고 light/dark mode 모두 확인한다.

Q. 색상만 의미 전달하는 문제는 어떻게 찾어?
A. 색상을 제거하거나 흑백으로 봐도 상태를 이해할 수 있는지 확인한다.

Q. zoom 테스트도 해야 해?
A. 확대 환경에서 텍스트가 잘리지 않고 조작 가능한지 확인하는 것이 좋다.

---

# 10. Accessibility Code Review

## 10.1 Review Agent Checklist

### [개념]

Accessibility Code Review는 코드 레벨에서 semantic HTML, ARIA, keyboard, focus, Form, state feedback, visual accessibility 문제를 찾는 과정이다.

Review Agent는 접근성 문제를 UI 결과만이 아니라 코드 구조에서 빠르게 탐지해야 한다.

---

### [핵심]

Code Review 탐지 패턴:

- `div onClick`
- `span onClick`
- `button` type 누락
- `a href="#"` action 처리
- label 없는 input
- placeholder-only input
- error message 미연결
- `aria-invalid` 상태 불일치
- `aria-expanded` 하드코딩
- `aria-selected` 상태 불일치
- `aria-hidden` 내부 focusable element
- `outline: none`
- icon button aria-label 누락
- modal focus return 누락
- dropdown hidden focus 가능
- spinner only
- empty state 없음
- color only error
- testId 중심 테스트

---

### [실무]

Review Flow:

```text
Interactive Element 검색
→ Form Control 검색
→ ARIA 속성 검색
→ Focus 관련 코드 검색
→ State Feedback 검색
→ CSS focus reset 검색
→ Test Query 검색
→ Checklist 매칭
→ 수정 제안
```

코드 검색 키워드:

```text
onClick
role=
aria-
tabIndex
outline
placeholder
disabled
loading
error
alert
status
dialog
expanded
selected
testId
```

대표 수정:

```text
문제: div onClick 사용
수정: button type="button" 사용
```

```text
문제: input placeholder만 있음
수정: label htmlFor + input id 연결
```

```text
문제: aria-expanded="true" 하드코딩
수정: open state와 동기화
```

```text
문제: outline: none 후 대체 없음
수정: :focus-visible focus style 제공
```

---

### [FAQ]

Q. Accessibility Code Review에서 가장 먼저 찾을 것은?
A. div onClick, label 없는 input, icon button label 누락, outline none, ARIA 상태 불일치를 먼저 찾는다.

Q. onClick이 있으면 무조건 문제야?
A. 아니다. button onClick은 정상일 수 있다. div/span onClick처럼 non-interactive element 사용이 문제다.

Q. ARIA가 보이면 좋은 코드야?
A. 아니다. ARIA가 실제 상태와 동기화되고 필요한 곳에만 쓰였는지 확인해야 한다.

Q. 테스트 코드도 접근성 리뷰 대상이야?
A. 그렇다. getByRole / getByLabelText 대신 testId만 쓰는 테스트는 접근성 문제를 숨길 수 있다.

---

## 10.2 Pull Request Accessibility Review

### [개념]

Pull Request Accessibility Review는 PR 단위로 접근성 변경사항과 위험 요소를 점검하는 절차다.

PR에서 UI Component, Form, Modal, Dropdown, State Feedback이 추가되면 접근성 체크리스트를 함께 검토해야 한다.

---

### [핵심]

PR Review 대상:

- new component
- changed component
- new form
- new modal
- new dropdown
- new route
- new state UI
- new table
- new image/icon
- new CSS reset
- changed design token
- changed test query

PR 질문:

- keyboard로 사용 가능한가?
- label이 있는가?
- focus가 보이는가?
- 오류 메시지가 연결되는가?
- ARIA 상태가 동기화되는가?
- 상태 메시지가 있는가?
- 색상만으로 의미 전달하지 않는가?
- role/name query 테스트가 있는가?

---

### [실무]

PR Checklist:

```md
- [ ] 새 interactive element가 native HTML을 사용하는가?
- [ ] 새 Form Control에 label이 있는가?
- [ ] 새 Button의 type이 적절한가?
- [ ] 새 IconButton에 accessible name이 있는가?
- [ ] 새 Modal에 focus 관리가 있는가?
- [ ] 새 Dropdown에 keyboard 조작이 가능한가?
- [ ] 새 Error State에 사용자용 문구와 retry가 있는가?
- [ ] 새 Empty State가 제공되는가?
- [ ] 새 이미지 alt가 목적에 맞는가?
- [ ] 새 색상 token의 contrast를 확인했는가?
- [ ] 새 테스트가 role / label query를 사용하는가?
```

실무 기준:

- PR에서 접근성 변경을 명시
- UI 변경은 keyboard screenshot보다 keyboard flow 설명이 더 중요할 수 있음
- 공통 Component 변경은 영향 범위가 크므로 우선 검토
- design token 변경은 contrast regression 가능성 확인
- 자동화 테스트 결과와 수동 점검 결과를 함께 기록 가능

---

### [FAQ]

Q. PR에서 접근성은 언제 리뷰해?
A. UI, Form, Modal, Dropdown, state, CSS, design token 변경이 있으면 리뷰해야 한다.

Q. PR 접근성 체크리스트는 너무 무겁지 않아?
A. 핵심 항목만 반복 적용하면 큰 문제를 빠르게 줄일 수 있다.

Q. 공통 Component PR은 왜 더 중요해?
A. 여러 화면에 영향을 주므로 접근성 문제가 넓게 퍼질 수 있기 때문이다.

Q. PR에 접근성 테스트 결과를 남겨야 해?
A. 핵심 UI 변경이라면 자동화 테스트나 keyboard 수동 점검 결과를 남기는 것이 좋다.

---

# 11. Regression and CI Strategy

## 11.1 Accessibility Regression

### [개념]

Accessibility Regression은 기존에 접근성 기준을 만족하던 UI가 변경 후 다시 접근성 문제를 갖게 되는 현상이다.

공통 Component, Design Token, CSS Reset, Form Validation 변경에서 자주 발생한다.

---

### [핵심]

Regression 위험 요소:

- CSS reset 변경
- focus outline 제거
- Button Component 변경
- Modal library 변경
- Form validation 변경
- Error message 구조 변경
- color token 변경
- icon library 변경
- Router 변경
- Test Query를 testId로 변경
- Dropdown / Tab refactor

방지 방법:

- role/name query 유지
- axe basic test
- keyboard regression check
- visual focus check
- component story review
- PR checklist
- design token contrast check

---

### [실무]

Regression Test 대상:

```text
Button
IconButton
Input
Select
Checkbox
Modal
Dropdown
Tab
Toast
Form Error
Loading State
Empty State
Navigation
```

실무 기준:

- 공통 Component 테스트를 먼저 안정화
- focus style regression은 수동 확인 필요
- color token 변경 시 contrast 재확인
- Form error 구조 변경 시 aria-describedby 재확인
- Modal 변경 시 focus return 재확인
- Test Query를 testId로 낮추는 변경은 주의
- CI에서 핵심 axe test만 우선 적용 가능

---

### [FAQ]

Q. Accessibility Regression은 뭐야?
A. 기존에 접근성 기준을 만족하던 UI가 변경 후 다시 접근성 문제가 생기는 것이다.

Q. Regression은 어디서 자주 생겨?
A. 공통 Component, CSS reset, design token, Form validation, Modal 변경에서 자주 생긴다.

Q. 접근성 Regression을 어떻게 막아?
A. role/name query 테스트, axe basic test, PR checklist, 수동 keyboard check를 함께 사용한다.

Q. focus outline 제거도 Regression이야?
A. 그렇다. keyboard 사용성이 크게 나빠지는 접근성 Regression이다.

---

## 11.2 CI Accessibility Strategy

### [개념]

CI Accessibility Strategy는 접근성 테스트를 CI 파이프라인에 단계적으로 포함해 반복적인 접근성 오류를 줄이는 전략이다.

Foundation 단계에서는 모든 페이지 완전 자동화를 목표로 하기보다 공통 Component와 핵심 Form부터 적용하는 것이 현실적이다.

---

### [핵심]

CI 적용 우선순위:

1. Common Component axe test
2. Form label / error test
3. Modal dialog test
4. Dropdown / Tab state test
5. Page template axe test
6. Critical user flow keyboard test
7. Design token contrast check
8. Storybook accessibility check

CI에서 잡기 좋은 문제:

- missing label
- empty button name
- broken aria reference
- invalid role
- missing alt
- role/name query regression
- dialog name missing

---

### [실무]

단계적 적용:

```text
Step 1: Button / Form / Modal 테스트
Step 2: axe basic test 추가
Step 3: Dropdown / Tab keyboard test 추가
Step 4: Page Template axe test 추가
Step 5: PR checklist와 수동 점검 병행
```

실무 기준:

- 모든 화면을 한 번에 CI 적용하지 않음
- 실패가 잦은 핵심 Component부터 자동화
- axe test는 실행 비용을 고려
- flaky keyboard test는 단순화
- 수동 점검이 필요한 항목은 PR checklist로 관리
- CI 실패 메시지를 수정 가능한 단위로 유지

---

### [FAQ]

Q. 접근성 테스트를 CI에 넣어야 해?
A. 공통 Component와 핵심 Form부터 넣으면 반복 오류를 줄이는 데 도움이 된다.

Q. 모든 페이지에 axe를 돌려야 해?
A. 이상적일 수 있지만 비용이 크다. 핵심 Component와 Page Template부터 단계적으로 적용하는 것이 현실적이다.

Q. CI로 keyboard 접근성을 완전히 검증할 수 있어?
A. 아니다. 일부 interaction은 검증 가능하지만 실제 focus visible과 복잡한 흐름은 수동 점검이 필요하다.

Q. CI 접근성 테스트의 목적은 뭐야?
A. 반복적으로 발생하는 label 누락, empty button name, ARIA 오류 같은 기본 문제를 빠르게 잡는 것이다.

---

# 12. Accessibility Review Output Pattern

## 12.1 Review Result Format

### [개념]

Accessibility Review Output Pattern은 Review Agent가 접근성 문제를 발견했을 때 일관된 형식으로 문제, 영향, 수정 방향을 제시하는 기준이다.

Review 결과는 단순 지적이 아니라 수정 가능한 action으로 연결되어야 한다.

---

### [핵심]

Review Output 구성:

- 문제 위치
- 문제 유형
- 접근성 영향
- 수정 기준
- 예시 코드
- 테스트 기준
- 우선순위
- 관련 Domain Rule

문제 유형:

- Semantic HTML
- Keyboard
- Focus
- Form Label
- Error Message
- ARIA State
- Image Alt
- Color Contrast
- State Feedback
- Component Pattern
- Testing Gap

---

### [실무]

Review Output 예:

```md
## 문제: IconButton accessible name 누락

- 위치: `NotificationButton`
- 유형: Accessible Name
- 영향: 스크린 리더 사용자가 버튼 목적을 알 수 없음
- 수정: button에 `aria-label="알림 열기"` 제공, icon은 `aria-hidden` 처리
- 테스트: `getByRole("button", { name: "알림 열기" })`로 검증
```

Review Output 예:

```md
## 문제: Dropdown open 상태와 aria-expanded 불일치

- 위치: `FilterDropdown`
- 유형: ARIA State
- 영향: 보조기술 사용자에게 실제 open 상태와 다른 정보 전달
- 수정: `aria-expanded={open}`으로 state와 동기화
- 테스트: open / close 후 `aria-expanded` 값 검증
```

실무 기준:

- 문제만 말하지 말고 수정 기준 제공
- 사용자 영향 중심으로 설명
- 예시 코드는 최소 수정 단위로 제공
- 테스트 기준을 함께 제안
- 우선순위는 사용성 영향과 범위 기준
- 공통 Component 문제는 높은 우선순위로 분류

---

### [FAQ]

Q. Accessibility Review 결과는 어떻게 써야 해?
A. 문제 위치, 문제 유형, 사용자 영향, 수정 기준, 테스트 기준을 함께 작성한다.

Q. 단순히 “접근성 안 좋음”이라고 하면 안 돼?
A. 안 된다. 수정 가능한 구체적 문제로 나눠야 한다.

Q. Review에 테스트 기준도 포함해야 해?
A. 가능하면 포함하는 것이 좋다. 재발 방지에 도움이 된다.

Q. 공통 Component 문제는 우선순위가 높아?
A. 그렇다. 여러 화면에 반복 영향을 주기 때문에 우선 수정 대상이다.

---

# 13. Common Accessibility Testing Mistakes

## 13.1 Testing Anti Patterns

### [개념]

Testing Anti Pattern은 테스트는 통과하지만 접근성 구조를 검증하지 못하거나 접근성 문제를 숨기는 방식이다.

테스트는 사용자가 인식하는 role, label, text, state를 기준으로 작성해야 한다.

---

### [핵심]

자주 발생하는 실수:

- 모든 요소를 `getByTestId`로 찾음
- input을 placeholder로만 찾음
- button name 검증 없음
- icon button accessible name 검증 없음
- modal role/name 검증 없음
- error message role / 연결 검증 없음
- aria-expanded / selected 상태 검증 없음
- keyboard interaction 테스트 없음
- focus return 테스트 없음
- spinner 렌더링만 확인
- empty state 문구 검증 없음
- axe만 돌리고 수동 점검 없음
- snapshot만으로 UI 검증
- hidden element focus 미검증
- color only meaning 미검토

---

### [실무]

Anti Pattern:

```tsx
screen.getByTestId("save-button");
```

개선:

```tsx
screen.getByRole("button", { name: "저장" });
```

Anti Pattern:

```tsx
screen.getByPlaceholderText("이메일");
```

개선:

```tsx
screen.getByLabelText("이메일");
```

Anti Pattern:

```tsx
expect(screen.getByTestId("modal")).toBeInTheDocument();
```

개선:

```tsx
expect(screen.getByRole("dialog", { name: "리뷰 작성" })).toBeInTheDocument();
```

Anti Pattern:

```tsx
expect(screen.getByTestId("spinner")).toBeInTheDocument();
```

개선:

```tsx
expect(screen.getByRole("status")).toHaveTextContent(
  "데이터를 불러오는 중입니다.",
);
```

---

### [FAQ]

Q. Testing 접근성 초보가 가장 많이 하는 실수는?
A. getByTestId 중심 테스트, placeholder 기반 input 테스트, button accessible name 미검증이 많다.

Q. snapshot 테스트는 접근성 검증에 충분해?
A. 아니다. 사용자가 인식하는 role, label, state를 직접 검증해야 한다.

Q. spinner가 렌더링되는지만 확인하면 돼?
A. 아니다. loading text와 role status를 확인해야 한다.

Q. axe만 돌리면 충분해?
A. 아니다. keyboard, focus, 문구 품질, 사용자 흐름은 별도 검토가 필요하다.

---

# Retrieval Queries

### [FAQ]

Q. Accessibility Testing은 왜 필요해?
A. 접근성 문제는 눈으로만 확인하기 어렵고, 테스트와 리뷰를 통해 semantic, keyboard, focus, ARIA 누락을 줄일 수 있기 때문이다.

Q. 자동화 테스트만 있으면 접근성 검증이 끝나?
A. 아니다. keyboard 흐름, focus visible, 문구 품질, 색상 의미는 수동 검토가 필요하다.

Q. 접근성 테스트에서 가장 먼저 할 것은?
A. Testing Library의 getByRole, getByLabelText로 사용자가 인식하는 구조를 검증하는 것이다.

Q. axe 테스트를 통과하면 접근성 문제 없는 거야?
A. 아니다. axe는 일부 오류만 탐지하며 실제 사용 흐름은 수동 점검해야 한다.

Q. Testing Library에서 어떤 Query를 먼저 써야 해?
A. getByRole을 우선 사용하고 Form Control은 getByLabelText를 우선 사용한다.

Q. getByRole이 좋은 이유는?
A. 사용자가 인식하는 role과 accessible name 기준으로 요소를 찾기 때문에 접근성 구조를 검증할 수 있다.

Q. getByTestId를 쓰면 안 돼?
A. 필요한 경우 가능하지만 접근성 구조를 검증하지 못하므로 최후 수단으로 두는 것이 좋다.

Q. getByRole이 실패하면 어떻게 해?
A. semantic element, role, accessible name, hidden 상태를 확인한다.

Q. getByRole로 무엇을 검증할 수 있어?
A. 요소의 role, accessible name, heading level, landmark, dialog name 등을 검증할 수 있다.

Q. icon button은 getByRole로 찾을 수 있어?
A. button에 aria-label이 있으면 getByRole("button", { name })으로 찾을 수 있다.

Q. heading level도 테스트할 수 있어?
A. 가능하다. getByRole("heading", { level: 1 })처럼 검증할 수 있다.

Q. getByRole이 안 잡히면 무조건 role을 붙이면 돼?
A. 아니다. 먼저 적절한 native HTML을 사용했는지 확인해야 한다.

Q. getByLabelText는 언제 써?
A. input, select, textarea, checkbox, radio 같은 Form Control을 label 기준으로 찾을 때 사용한다.

Q. getByLabelText가 실패하면 접근성 문제야?
A. 가능성이 높다. label 연결, id 일치, label text를 확인해야 한다.

Q. placeholder가 있는데 getByLabelText가 실패하면 괜찮아?
A. 권장하지 않는다. placeholder는 label 대체가 아니므로 label을 제공하는 것이 좋다.

Q. sr-only label도 getByLabelText로 찾을 수 있어?
A. 가능하다. 화면에 보이지 않아도 접근성 트리에 제공되면 Query 대상이 될 수 있다.

Q. Keyboard 접근성도 자동 테스트할 수 있어?
A. 일부 가능하다. userEvent.tab, userEvent.keyboard, toHaveFocus를 사용한다.

Q. keyboard test에서 무엇을 확인해?
A. focus 이동, Enter / Space 실행, Escape 닫기, focus return 등을 확인한다.

Q. keyboard test가 있으면 수동 점검은 생략해도 돼?
A. 아니다. 실제 focus visible, scroll, 복잡한 흐름은 수동 확인이 필요하다.

Q. keyboard test도 getByRole을 써야 해?
A. 권장한다. 사용자가 인식하는 role과 name 기준으로 테스트하는 것이 좋다.

Q. Focus Test는 언제 필요해?
A. Modal, Form 오류, Error Summary, 동적 UI처럼 focus 이동이 중요한 상황에 필요하다.

Q. 모든 클릭 후 focus를 테스트해야 해?
A. 아니다. 사용자 흐름상 focus 관리가 중요한 interaction을 우선 테스트한다.

Q. focus visible도 테스트 코드로 검증할 수 있어?
A. 제한적이다. 실제 시각적 focus는 수동 확인이 필요하다.

Q. hidden element focus는 왜 문제야?
A. 보이지 않는 요소에 focus가 가면 keyboard 사용자가 현재 위치를 알 수 없기 때문이다.

Q. Form input은 어떤 Query로 테스트해?
A. getByLabelText를 우선 사용한다.

Q. Form submit button은 어떻게 테스트해?
A. getByRole("button", { name: "저장" })처럼 role/name으로 찾는다.

Q. checkbox는 어떻게 테스트해?
A. getByRole("checkbox", { name }) 또는 getByLabelText로 찾는다.

Q. placeholder로 input을 테스트하면 안 돼?
A. 가능하지만 label 접근성을 검증하지 못하므로 label query를 우선 사용한다.

Q. Form Error는 무엇을 테스트해야 해?
A. 오류 문구, role alert, aria-invalid, aria-describedby 연결을 확인한다.

Q. aria-invalid도 테스트해야 해?
A. validation 상태를 전달해야 하는 input이라면 오류 상태와 동기화되는지 확인하는 것이 좋다.

Q. error message와 input 연결은 어떻게 테스트해?
A. input의 aria-describedby가 실제 error message id를 참조하는지 확인한다.

Q. 오류 문구도 테스트해야 해?
A. 그렇다. 사용자가 이해 가능한 문구인지 확인하는 데 도움이 된다.

Q. Modal 접근성 테스트에서 가장 중요한 것은?
A. dialog role/name, focus 이동, Escape 닫기, focus return이다.

Q. Modal title 연결은 어떻게 테스트해?
A. getByRole("dialog", { name: "제목" })으로 accessible name을 확인한다.

Q. focus trap도 자동 테스트해야 해?
A. 일부 테스트 가능하지만 실제 Tab 순환과 visual focus는 수동 점검도 필요하다.

Q. Modal 닫기 버튼은 어떻게 테스트해?
A. getByRole("button", { name: "닫기" })로 찾고 click 또는 keyboard로 닫힘을 확인한다.

Q. Dropdown 테스트에서 무엇을 확인해?
A. trigger button, aria-expanded 동기화, open/close, keyboard 닫기를 확인한다.

Q. Accordion 테스트에서 무엇을 확인해?
A. trigger button과 panel 표시 상태, aria-expanded 동기화를 확인한다.

Q. Tab 테스트에서 무엇을 확인해?
A. role tab, aria-selected, visible tabpanel, keyboard 이동을 확인한다.

Q. aria-expanded나 aria-selected는 꼭 테스트해야 해?
A. 상태 UI에서는 실제 상태와 동기화되는지 테스트하는 것이 좋다.

Q. Loading 상태는 어떻게 테스트해?
A. role status나 loading text로 사용자가 인식 가능한 상태를 검증한다.

Q. Error 상태는 어떻게 테스트해?
A. role alert와 error message, retry button을 함께 확인한다.

Q. Empty State는 어떻게 테스트해?
A. heading, 설명 문구, 다음 action button 또는 link를 확인한다.

Q. pending button은 어떻게 테스트해?
A. 버튼 text가 “저장 중...”처럼 바뀌고 disabled 또는 aria-busy 상태인지 확인한다.

Q. 이미지 alt는 테스트할 수 있어?
A. 가능하다. getByAltText로 정보 이미지의 alt를 확인할 수 있다.

Q. IconButton 접근성은 어떻게 테스트해?
A. getByRole("button", { name })으로 accessible name을 검증한다.

Q. 상태 아이콘은 어떻게 테스트해?
A. 아이콘만 검증하기보다 상태 텍스트가 제공되는지 확인한다.

Q. 색상 대비도 Testing Library로 테스트해?
A. 일반적으로 색상 대비는 전용 도구나 수동 검토가 필요하다.

Q. axe는 무엇을 찾아줘?
A. label 누락, role 오류, ARIA 참조 오류, alt 누락, 일부 contrast 문제를 찾을 수 있다.

Q. axe 테스트만 통과하면 접근성 완료야?
A. 아니다. keyboard, focus, 문구, 사용자 흐름은 수동 검토가 필요하다.

Q. axe 오류는 무조건 수정해야 해?
A. 대부분 원인을 확인해야 한다. 예외가 있다면 명확한 이유와 대체 검증이 필요하다.

Q. axe는 React Component 테스트에 붙일 수 있어?
A. 가능하다. Testing Library로 렌더링한 container에 axe를 실행할 수 있다.

Q. axe는 열린 Modal 상태도 검사해야 해?
A. 그렇다. 닫힌 상태만 검사하면 Modal 내부 접근성 문제를 놓칠 수 있다.

Q. Form error 상태도 axe 검사해야 해?
A. 가능하면 검사하는 것이 좋다. 오류 메시지와 aria 연결 문제가 드러날 수 있다.

Q. axe 테스트가 느리면 어떻게 해?
A. 모든 테스트에 넣기보다 공통 Component와 핵심 Page 중심으로 적용한다.

Q. Manual Keyboard Review는 왜 필요해?
A. 실제 focus 흐름, focus visible, keyboard trap은 자동화 도구가 완전히 검증하지 못하기 때문이다.

Q. keyboard 점검은 어디부터 해?
A. 로그인, 회원가입, 검색, 결제, Modal, Dropdown 같은 핵심 흐름부터 확인한다.

Q. keyboard trap은 어떻게 찾어?
A. Tab, Shift+Tab, Escape, 닫기 버튼으로 빠져나갈 수 있는지 확인한다.

Q. focus visible은 어떻게 확인해?
A. Tab으로 이동하면서 현재 위치가 시각적으로 명확히 보이는지 확인한다.

Q. Manual Visual Review는 왜 필요해?
A. 색상 의미, focus 시각 품질, 이미지 alt 품질, zoom 사용성은 자동화만으로 판단하기 어렵기 때문이다.

Q. 색상 대비는 어떻게 확인해?
A. contrast checker 같은 도구를 사용하고 light/dark mode 모두 확인한다.

Q. 색상만 의미 전달하는 문제는 어떻게 찾어?
A. 색상을 제거하거나 흑백으로 봐도 상태를 이해할 수 있는지 확인한다.

Q. zoom 테스트도 해야 해?
A. 확대 환경에서 텍스트가 잘리지 않고 조작 가능한지 확인하는 것이 좋다.

Q. Accessibility Code Review에서 가장 먼저 찾을 것은?
A. div onClick, label 없는 input, icon button label 누락, outline none, ARIA 상태 불일치를 먼저 찾는다.

Q. onClick이 있으면 무조건 문제야?
A. 아니다. button onClick은 정상일 수 있다. div/span onClick처럼 non-interactive element 사용이 문제다.

Q. ARIA가 보이면 좋은 코드야?
A. 아니다. ARIA가 실제 상태와 동기화되고 필요한 곳에만 쓰였는지 확인해야 한다.

Q. 테스트 코드도 접근성 리뷰 대상이야?
A. 그렇다. getByRole / getByLabelText 대신 testId만 쓰는 테스트는 접근성 문제를 숨길 수 있다.

Q. PR에서 접근성은 언제 리뷰해?
A. UI, Form, Modal, Dropdown, state, CSS, design token 변경이 있으면 리뷰해야 한다.

Q. PR 접근성 체크리스트는 너무 무겁지 않아?
A. 핵심 항목만 반복 적용하면 큰 문제를 빠르게 줄일 수 있다.

Q. 공통 Component PR은 왜 더 중요해?
A. 여러 화면에 영향을 주므로 접근성 문제가 넓게 퍼질 수 있기 때문이다.

Q. PR에 접근성 테스트 결과를 남겨야 해?
A. 핵심 UI 변경이라면 자동화 테스트나 keyboard 수동 점검 결과를 남기는 것이 좋다.

Q. Accessibility Regression은 뭐야?
A. 기존에 접근성 기준을 만족하던 UI가 변경 후 다시 접근성 문제가 생기는 것이다.

Q. Regression은 어디서 자주 생겨?
A. 공통 Component, CSS reset, design token, Form validation, Modal 변경에서 자주 생긴다.

Q. 접근성 Regression을 어떻게 막아?
A. role/name query 테스트, axe basic test, PR checklist, 수동 keyboard check를 함께 사용한다.

Q. focus outline 제거도 Regression이야?
A. 그렇다. keyboard 사용성이 크게 나빠지는 접근성 Regression이다.

Q. 접근성 테스트를 CI에 넣어야 해?
A. 공통 Component와 핵심 Form부터 넣으면 반복 오류를 줄이는 데 도움이 된다.

Q. 모든 페이지에 axe를 돌려야 해?
A. 이상적일 수 있지만 비용이 크다. 핵심 Component와 Page Template부터 단계적으로 적용하는 것이 현실적이다.

Q. CI로 keyboard 접근성을 완전히 검증할 수 있어?
A. 아니다. 일부 interaction은 검증 가능하지만 실제 focus visible과 복잡한 흐름은 수동 점검이 필요하다.

Q. CI 접근성 테스트의 목적은 뭐야?
A. 반복적으로 발생하는 label 누락, empty button name, ARIA 오류 같은 기본 문제를 빠르게 잡는 것이다.

Q. Accessibility Review 결과는 어떻게 써야 해?
A. 문제 위치, 문제 유형, 사용자 영향, 수정 기준, 테스트 기준을 함께 작성한다.

Q. 단순히 접근성 안 좋음이라고 하면 안 돼?
A. 안 된다. 수정 가능한 구체적 문제로 나눠야 한다.

Q. Review에 테스트 기준도 포함해야 해?
A. 가능하면 포함하는 것이 좋다. 재발 방지에 도움이 된다.

Q. 공통 Component 문제는 우선순위가 높아?
A. 그렇다. 여러 화면에 반복 영향을 주기 때문에 우선 수정 대상이다.

Q. Testing 접근성 초보가 가장 많이 하는 실수는?
A. getByTestId 중심 테스트, placeholder 기반 input 테스트, button accessible name 미검증이 많다.

Q. snapshot 테스트는 접근성 검증에 충분해?
A. 아니다. 사용자가 인식하는 role, label, state를 직접 검증해야 한다.

Q. spinner가 렌더링되는지만 확인하면 돼?
A. 아니다. loading text와 role status를 확인해야 한다.

Q. axe만 돌리면 충분해?
A. 아니다. keyboard, focus, 문구 품질, 사용자 흐름은 별도 검토가 필요하다.
