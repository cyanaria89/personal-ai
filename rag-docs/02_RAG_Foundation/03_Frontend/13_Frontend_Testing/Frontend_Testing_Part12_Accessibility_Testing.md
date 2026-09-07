# Frontend Testing Part12 - Accessibility Testing

---

# 1. Accessibility Testing Overview

## 1.1 Accessibility Testing Definition

### [개념]

Accessibility Testing은 사용자가 키보드, 스크린리더, 보조기술, 다양한 입력 방식으로 Frontend UI를 사용할 수 있는지 검증하는 테스트다.

Frontend Testing에서 접근성 테스트는 `role`, `label`, `accessible name`, `keyboard interaction`, `aria state`, `focus management`를 중심으로 작성한다.

### [핵심]

- Accessibility Testing
- A11y Testing
- Accessible Query
- getByRole
- getByLabelText
- Accessible Name
- Semantic HTML
- Keyboard Navigation
- Focus Management
- aria-label
- aria-labelledby
- aria-describedby
- aria-invalid
- aria-expanded
- aria-selected
- role alert
- role status
- axe
- jest-axe
- Testing Library

### [실무]

2026 실무 기준에서 접근성 테스트는 별도의 특수 테스트가 아니라 React Testing Library의 기본 Query 전략과 연결된다.

기본 흐름:

```text
Semantic HTML 작성
→ role / label / accessible name 제공
→ RTL Query로 접근 가능 여부 확인
→ userEvent keyboard / tab 검증
→ aria state 검증
→ 필요한 경우 axe 자동 검사 추가
```

좋은 Accessibility Test:

```text
button을 getByRole로 찾을 수 있음
input을 getByLabelText로 찾을 수 있음
Modal이 dialog role과 accessible name을 가짐
Form error가 aria-invalid / aria-describedby로 연결됨
Tab 이동으로 주요 조작이 가능함
Escape 키로 Modal을 닫을 수 있음
Loading은 status role로 전달됨
Error는 alert role로 전달됨
```

나쁜 Accessibility Test:

```text
div onClick을 button처럼 사용
label 없는 input을 testId로만 찾음
icon button에 aria-label 없음
Modal에 dialog role 없음
오류 메시지가 input과 연결되지 않음
마우스 클릭만 테스트하고 keyboard 흐름 누락
aria 속성을 시각 상태와 다르게 설정
```

### [FAQ]

Q. Accessibility Testing은 뭐야?
A. 키보드, 스크린리더, 보조기술 사용자도 UI를 사용할 수 있는지 검증하는 테스트다.

Q. 접근성 테스트는 왜 Frontend Testing에 중요해?
A. 접근성 좋은 UI는 실제 사용자 경험이 좋고 React Testing Library의 사용자 관점 테스트와도 잘 맞기 때문이다.

Q. 접근성 테스트는 axe만 돌리면 충분해?
A. 아니다. axe는 자동 검사 보조 도구이고 role, label, keyboard, focus 흐름 테스트도 필요하다.

## 1.2 Accessibility Testing Scope

### [개념]

Accessibility Testing Scope는 Frontend에서 어떤 접근성 요소를 테스트할지 정하는 기준이다.

모든 ARIA 속성을 기계적으로 테스트하는 것이 아니라 사용자 조작과 이해에 중요한 접근성 정보를 검증한다.

### [핵심]

포함 범위:

- semantic HTML
- role
- accessible name
- form label
- image alt
- button name
- link name
- heading structure
- keyboard navigation
- focus order
- focus trap
- skip link
- dialog accessibility
- form error accessibility
- loading accessibility
- error accessibility
- aria state
- axe scan

분리 권장:

- 브라우저별 스크린리더 실제 낭독 검증
- 실제 디바이스 접근성 검증
- 색 대비 시각 검수 전체 자동화
- 복잡한 E2E keyboard journey
- 디자인 시스템 전체 WCAG 인증

### [실무]

Component Test 적합:

```text
Button이 accessible name을 가진다.
Input이 label로 연결된다.
IconButton이 aria-label을 가진다.
Accordion button이 aria-expanded를 갱신한다.
Error message가 role alert로 표시된다.
```

Integration Test 적합:

```text
Modal이 열리면 focus가 Modal 내부로 이동한다.
Tab 이동이 Form 순서대로 진행된다.
Protected Page에서 로그인 Form으로 focus가 이동한다.
Dropdown을 keyboard로 열고 option을 선택한다.
```

E2E Test 적합:

```text
전체 회원가입 Flow를 keyboard만으로 완료한다.
모바일 메뉴를 keyboard와 screen reader 흐름으로 점검한다.
실제 브라우저에서 focus trap이 깨지지 않는지 검증한다.
```

### [FAQ]

Q. 모든 aria 속성을 테스트해야 해?
A. 아니다. 사용자 상태 전달에 중요한 aria 속성을 중심으로 테스트한다.

Q. 접근성 테스트는 Component Test야 Integration Test야?
A. 단순 role/label은 Component Test이고 focus 흐름이나 keyboard journey는 Integration 또는 E2E에 가깝다.

Q. 스크린리더 실제 낭독까지 자동 테스트해야 해?
A. 일반 단위 테스트로는 어렵다. 자동 검사와 keyboard/focus 테스트를 기본으로 하고 필요 시 수동 검수한다.

# 2. Semantic HTML Test

## 2.1 Semantic HTML Rule

### [개념]

Semantic HTML은 HTML 요소 자체의 의미를 사용해 UI 구조를 표현하는 방식이다.

접근성 테스트에서는 `button`, `a`, `input`, `label`, `h1~h6`, `nav`, `main`, `section`, `dialog`, `ul/li`, `table` 같은 의미 있는 요소를 우선 사용한다.

### [핵심]

- Semantic HTML
- button element
- anchor element
- input label
- heading
- nav
- main
- section
- list
- table
- form
- dialog
- native accessibility
- avoid div button
- avoid span link

### [실무]

나쁜 예:

```tsx
<div onClick={onSave}>저장</div>
```

좋은 예:

```tsx
<button type="button" onClick={onSave}>
  저장
</button>
```

테스트:

```tsx
test("저장 버튼은 button role로 접근할 수 있다", () => {
  render(<SaveButton onSave={vi.fn()} />);

  expect(screen.getByRole("button", { name: "저장" })).toBeInTheDocument();
});
```

Link 예:

```tsx
<a href="/festivals/1">축제 상세 보기</a>
```

테스트:

```tsx
expect(screen.getByRole("link", { name: "축제 상세 보기" })).toHaveAttribute(
  "href",
  "/festivals/1",
);
```

권장:

- 클릭 가능한 요소는 button 또는 link 사용
- Form 요소는 label 연결
- heading으로 문서 구조 제공
- nav/main/section 같은 landmark 활용
- ARIA로 semantic HTML을 대체하려 하지 않음

### [FAQ]

Q. Semantic HTML은 왜 중요해?
A. 브라우저와 보조기술이 요소의 의미를 이해할 수 있고 RTL Query도 사용자 관점으로 작성할 수 있기 때문이다.

Q. div에 role="button"을 붙이면 button과 같아?
A. 완전히 같지 않다. keyboard 동작과 기본 접근성까지 고려하면 native button이 더 좋다.

Q. 접근성 테스트에서 semantic HTML을 어떻게 확인해?
A. getByRole, getByLabelText 같은 accessible query로 요소를 찾을 수 있는지 확인한다.

## 2.2 Heading Structure Test

### [개념]

Heading Structure Test는 Page나 Section이 명확한 heading 구조를 제공하는지 검증하는 테스트다.

Heading은 사용자가 화면 구조를 빠르게 이해하고 보조기술로 영역을 탐색하는 데 중요하다.

### [핵심]

- heading
- h1
- h2
- section title
- page title
- accessible heading
- document outline
- getByRole heading
- level option
- page structure

### [실무]

Page heading:

```tsx
test("축제 목록 Page는 h1 제목을 제공한다", () => {
  render(<FestivalListPage />);

  expect(
    screen.getByRole("heading", { name: "축제 목록", level: 1 }),
  ).toBeInTheDocument();
});
```

Section heading:

```tsx
test("인기 축제 섹션 제목을 제공한다", () => {
  render(<HomePage />);

  expect(
    screen.getByRole("heading", { name: "인기 축제", level: 2 }),
  ).toBeInTheDocument();
});
```

권장:

- Page마다 h1 제공
- Section은 h2/h3로 구조화
- heading level을 건너뛰지 않도록 검토
- 스타일을 위해 heading level을 선택하지 않음
- Card title은 상황에 따라 h2/h3 사용

### [FAQ]

Q. Heading Structure는 왜 테스트해?
A. Page 구조를 보조기술 사용자가 이해하고 탐색할 수 있어야 하기 때문이다.

Q. heading level까지 테스트해야 해?
A. 중요한 Page 구조에서는 level 옵션으로 검증하는 것이 좋다.

Q. 글씨 크기를 위해 h1/h2를 선택해도 돼?
A. 아니다. heading level은 문서 구조 기준으로 선택하고 스타일은 CSS로 조정한다.

## 2.3 Landmark Test

### [개념]

Landmark Test는 `main`, `nav`, `header`, `footer`, `aside`, `section` 같은 구조적 영역이 접근 가능한 landmark로 제공되는지 검증하는 테스트다.

복잡한 Page에서 사용자가 주요 영역으로 빠르게 이동하는 데 도움을 준다.

### [핵심]

- landmark
- main
- navigation
- banner
- contentinfo
- complementary
- region
- aria-label
- layout accessibility
- page structure

### [실무]

main 영역:

```tsx
test("Page는 main landmark를 제공한다", () => {
  render(<AppLayout />);

  expect(screen.getByRole("main")).toBeInTheDocument();
});
```

navigation 영역:

```tsx
test("주요 navigation landmark를 제공한다", () => {
  render(<MainNavigation />);

  expect(
    screen.getByRole("navigation", { name: "주요 메뉴" }),
  ).toBeInTheDocument();
});
```

region label:

```tsx
<section aria-label="축제 검색 결과">...</section>
```

테스트:

```tsx
expect(
  screen.getByRole("region", { name: "축제 검색 결과" }),
).toBeInTheDocument();
```

권장:

- Page에는 main landmark 제공
- 여러 nav가 있으면 aria-label로 구분
- section을 region으로 노출하려면 accessible name 제공
- layout component에서 landmark 구조 테스트 가능
- landmark 과다 사용 지양

### [FAQ]

Q. Landmark는 왜 필요해?
A. 보조기술 사용자가 Page의 주요 영역으로 빠르게 이동할 수 있게 한다.

Q. navigation이 여러 개면 어떻게 해?
A. `aria-label`로 주요 메뉴, 사용자 메뉴처럼 구분한다.

Q. section은 자동으로 region이 돼?
A. accessible name이 있어야 region으로 의미 있게 노출될 수 있다.

# 3. Accessible Name Test

## 3.1 Accessible Name Definition

### [개념]

Accessible Name은 보조기술이 요소를 사용자에게 설명할 때 사용하는 이름이다.

버튼 텍스트, 링크 텍스트, label, aria-label, aria-labelledby, image alt 등이 accessible name에 영향을 준다.

### [핵심]

- Accessible Name
- button text
- link text
- label text
- aria-label
- aria-labelledby
- alt text
- icon button
- getByRole name
- accessible query

### [실무]

Button accessible name:

```tsx
<button>검색</button>
```

테스트:

```tsx
expect(screen.getByRole("button", { name: "검색" })).toBeInTheDocument();
```

Icon button:

```tsx
<button aria-label="검색">
  <SearchIcon />
</button>
```

테스트:

```tsx
expect(screen.getByRole("button", { name: "검색" })).toBeInTheDocument();
```

aria-labelledby:

```tsx
<h2 id="modal-title">삭제 확인</h2>
<div role="dialog" aria-labelledby="modal-title">
  ...
</div>
```

테스트:

```tsx
expect(screen.getByRole("dialog", { name: "삭제 확인" })).toBeInTheDocument();
```

권장:

- 버튼과 링크는 명확한 이름 제공
- 아이콘만 있는 버튼은 aria-label 필수
- Modal은 accessible name 제공
- 같은 이름의 버튼이 반복되면 문맥을 추가하거나 within 사용
- name 없는 interactive element 금지

### [FAQ]

Q. Accessible Name은 뭐야?
A. 보조기술이 버튼, 링크, 입력창 같은 요소를 사용자에게 설명할 때 사용하는 이름이다.

Q. icon button에는 왜 aria-label이 필요해?
A. 시각적 아이콘만으로는 보조기술 사용자가 버튼 목적을 알 수 없기 때문이다.

Q. getByRole name 옵션은 접근성 테스트야?
A. 그렇다. role과 accessible name으로 요소를 찾는 것은 접근성 구조를 함께 검증한다.

## 3.2 Button Name Test

### [개념]

Button Name Test는 모든 조작 가능한 button이 사용자가 이해할 수 있는 accessible name을 가지는지 검증하는 테스트다.

### [핵심]

- button name
- accessible button
- icon button
- submit button
- close button
- delete button
- loading button
- disabled button
- aria-label
- visible text

### [실무]

일반 버튼:

```tsx
test("저장 버튼은 accessible name을 가진다", () => {
  render(<SaveButton />);

  expect(screen.getByRole("button", { name: "저장" })).toBeInTheDocument();
});
```

닫기 버튼:

```tsx
test("닫기 아이콘 버튼은 accessible name을 가진다", () => {
  render(<CloseButton />);

  expect(screen.getByRole("button", { name: "닫기" })).toBeInTheDocument();
});
```

Loading button:

```tsx
test("처리 중 버튼은 현재 상태를 이름으로 전달한다", () => {
  render(<SubmitButton loading>등록</SubmitButton>);

  expect(screen.getByRole("button", { name: "처리 중..." })).toBeDisabled();
});
```

권장:

- icon button은 aria-label 제공
- close/delete/search 같은 버튼 이름 명확화
- loading 중 button name 정책 일관화
- disabled 버튼도 이름 유지
- 동일한 이름의 삭제 버튼은 card/row 문맥으로 구분

### [FAQ]

Q. Button Name Test는 왜 필요해?
A. 버튼 목적이 보조기술 사용자에게도 명확히 전달되어야 하기 때문이다.

Q. 아이콘만 있는 닫기 버튼은 어떻게 테스트해?
A. `getByRole("button", { name: "닫기" })`로 찾을 수 있어야 한다.

Q. loading 중 버튼 이름은 바꿔도 돼?
A. 가능하다. 다만 사용자에게 현재 상태가 명확히 전달되도록 일관성 있게 설계한다.

## 3.3 Link Name Test

### [개념]

Link Name Test는 link가 목적지를 이해할 수 있는 accessible name을 가지는지 검증하는 테스트다.

`자세히`, `더보기`, `여기`처럼 문맥 없는 링크 이름은 지양한다.

### [핵심]

- link name
- accessible link
- href
- link purpose
- NavLink
- detail link
- external link
- same name links
- aria-label caution

### [실무]

좋은 예:

```tsx
<a href="/festivals/1">봄꽃 축제 상세 보기</a>
```

테스트:

```tsx
expect(
  screen.getByRole("link", { name: "봄꽃 축제 상세 보기" }),
).toHaveAttribute("href", "/festivals/1");
```

나쁜 예:

```tsx
<a href="/festivals/1">자세히</a>
```

개선:

```tsx
<a href="/festivals/1" aria-label="봄꽃 축제 상세 보기">
  자세히
</a>
```

테스트:

```tsx
expect(
  screen.getByRole("link", { name: "봄꽃 축제 상세 보기" }),
).toBeInTheDocument();
```

권장:

- 링크 이름만 보고 목적지를 이해할 수 있어야 함
- 반복 카드 링크는 항목명을 포함
- 외부 링크는 새 창 여부 안내 검토
- href 속성 검증 가능
- NavLink active 상태는 aria-current 검증

### [FAQ]

Q. Link Name Test는 왜 필요해?
A. 사용자가 링크 이름만 듣고 목적지를 이해할 수 있어야 하기 때문이다.

Q. “자세히” 링크는 안 좋아?
A. 문맥 없이 반복되면 목적지를 알기 어렵다. 항목명을 포함하는 이름이 좋다.

Q. 링크 href도 테스트해야 해?
A. 단순 Link Component에서는 href 검증이 유용하다.

# 4. Form Accessibility Test

## 4.1 Label Connection Test

### [개념]

Label Connection Test는 input, textarea, select, checkbox, radio가 label과 올바르게 연결되어 있는지 검증하는 테스트다.

Form 요소는 placeholder가 아니라 label 또는 aria-label로 식별 가능해야 한다.

### [핵심]

- label
- getByLabelText
- htmlFor
- input id
- aria-label
- aria-labelledby
- form control
- placeholder caution
- accessible input
- field name

### [실무]

기본 예:

```tsx
test("로그인 Form은 이메일과 비밀번호 label을 제공한다", () => {
  render(<LoginForm />);

  expect(screen.getByLabelText("이메일")).toBeInTheDocument();
  expect(screen.getByLabelText("비밀번호")).toBeInTheDocument();
});
```

Select label:

```tsx
test("지역 select는 label로 접근할 수 있다", () => {
  render(<RegionSelect />);

  expect(screen.getByRole("combobox", { name: "지역" })).toBeInTheDocument();
});
```

Checkbox label:

```tsx
test("약관 동의 checkbox는 label로 접근할 수 있다", () => {
  render(<TermsCheckbox />);

  expect(
    screen.getByRole("checkbox", { name: "약관 동의" }),
  ).toBeInTheDocument();
});
```

권장:

- visible label 우선
- password input은 getByLabelText 사용
- placeholder만으로 label 대체 지양
- label과 input id/htmlFor 연결 확인
- icon-only input은 aria-label 제공

### [FAQ]

Q. Form input은 어떤 Query로 찾는 게 좋아?
A. label 기반 Query인 getByLabelText 또는 role과 name을 사용하는 것이 좋다.

Q. placeholder가 있으면 label이 없어도 돼?
A. 권장하지 않는다. placeholder는 label을 대체하기 어렵다.

Q. checkbox와 radio도 label이 필요해?
A. 필요하다. 사용자가 선택지 의미를 이해할 수 있어야 한다.

## 4.2 Field Error Accessibility Test

### [개념]

Field Error Accessibility Test는 입력 오류가 발생했을 때 해당 field가 오류 상태임을 보조기술에 전달하는지 검증하는 테스트다.

`aria-invalid`, `aria-describedby`, 오류 메시지 id 연결이 핵심이다.

### [핵심]

- field error
- aria-invalid
- aria-describedby
- error id
- role alert
- input error
- validation error
- server field error
- accessible error message

### [실무]

예:

```tsx
test("이메일 오류가 input과 연결된다", async () => {
  const user = userEvent.setup();

  render(<LoginForm />);

  const emailInput = screen.getByLabelText("이메일");

  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(emailInput).toHaveAttribute("aria-invalid", "true");
  expect(emailInput).toHaveAttribute("aria-describedby", "email-error");
  expect(screen.getByText("이메일을 입력해 주세요.")).toHaveAttribute(
    "id",
    "email-error",
  );
});
```

Server field error:

```tsx
test("서버 field error가 email field와 연결된다", async () => {
  const user = userEvent.setup();

  vi.mocked(signup).mockRejectedValue({
    response: {
      status: 400,
      data: {
        fieldErrors: {
          email: "이미 사용 중인 이메일입니다.",
        },
      },
    },
  });

  render(<SignupForm />);

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.click(screen.getByRole("button", { name: "가입하기" }));

  expect(
    await screen.findByText("이미 사용 중인 이메일입니다."),
  ).toBeInTheDocument();
  expect(screen.getByLabelText("이메일")).toHaveAttribute(
    "aria-invalid",
    "true",
  );
});
```

권장:

- 오류 발생 input에 aria-invalid 적용
- 오류 메시지는 aria-describedby로 연결
- field별 error id 안정화
- 오류 메시지가 화면에 보이는지 함께 확인
- global error와 field error 구분

### [FAQ]

Q. aria-invalid는 언제 true가 돼야 해?
A. 해당 field에 오류가 있을 때 true로 설정한다.

Q. aria-describedby는 왜 필요해?
A. input과 오류 메시지를 연결해 보조기술이 오류 내용을 함께 전달할 수 있게 한다.

Q. 오류 메시지 텍스트만 보이면 충분해?
A. 시각 사용자에게는 보일 수 있지만 보조기술 사용자를 위해 field와 오류 메시지를 연결하는 것이 좋다.

## 4.3 Error Summary Test

### [개념]

Error Summary Test는 Form 제출 실패 시 전체 오류 요약이 제공되고, 각 오류가 해당 field로 연결되는지 검증하는 테스트다.

큰 Form이나 공공 서비스, 복잡한 회원가입 Form에서 유용하다.

### [핵심]

- error summary
- form error summary
- list of errors
- link to field
- focus to summary
- role alert
- heading
- invalid submit
- field navigation

### [실무]

예:

```tsx
test("제출 실패 시 오류 요약을 표시한다", async () => {
  const user = userEvent.setup();

  render(<SignupForm />);

  await user.click(screen.getByRole("button", { name: "가입하기" }));

  expect(screen.getByRole("alert")).toHaveTextContent(
    "입력값을 확인해 주세요.",
  );
  expect(
    screen.getByRole("link", { name: "이메일 오류로 이동" }),
  ).toBeInTheDocument();
});
```

오류 링크 클릭:

```tsx
await user.click(screen.getByRole("link", { name: "이메일 오류로 이동" }));

expect(screen.getByLabelText("이메일")).toHaveFocus();
```

권장:

- 큰 Form에서는 오류 요약 제공 검토
- 요약은 field error와 중복되더라도 탐색에 도움
- 링크 클릭 시 해당 field로 focus 이동
- alert 또는 heading으로 명확히 표시
- 작은 Form에서는 field error만으로 충분할 수 있음

### [FAQ]

Q. Error Summary는 언제 필요해?
A. 입력 field가 많아 오류 위치를 찾기 어려운 큰 Form에서 유용하다.

Q. Error Summary도 role alert가 필요해?
A. 즉시 알려야 하는 오류 요약이라면 role alert를 고려할 수 있다.

Q. 오류 요약 링크는 무엇을 해야 해?
A. 클릭 시 해당 오류 field로 focus를 이동시키는 것이 좋다.

# 5. Keyboard Accessibility Test

## 5.1 Keyboard Navigation Test

### [개념]

Keyboard Navigation Test는 사용자가 마우스 없이 키보드로 UI를 조작할 수 있는지 검증하는 테스트다.

`user.tab`, `user.keyboard`, `toHaveFocus`를 사용한다.

### [핵심]

- Keyboard Navigation
- user.tab
- user.keyboard
- toHaveFocus
- Enter
- Space
- Escape
- ArrowDown
- ArrowUp
- focus order
- keyboard only
- interactive element

### [실무]

Form Tab 이동:

```tsx
test("로그인 Form은 Tab 키로 순서대로 이동할 수 있다", async () => {
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

Enter 제출:

```tsx
test("검색어 입력 후 Enter로 검색할 수 있다", async () => {
  const user = userEvent.setup();

  render(<SearchForm />);

  await user.type(screen.getByLabelText("검색어"), "축제");
  await user.keyboard("{Enter}");

  expect(await screen.findByText("검색 결과")).toBeInTheDocument();
});
```

권장:

- 주요 Form과 Modal은 keyboard 흐름 테스트
- click만 테스트하지 않음
- disabled 요소는 focus되지 않아야 함
- custom interactive component는 Enter/Space 동작 확인
- Tab order는 DOM 순서와 사용자 흐름 기준

### [FAQ]

Q. Keyboard Accessibility Test는 왜 필요해?
A. 마우스를 사용할 수 없는 사용자도 UI를 조작할 수 있어야 하기 때문이다.

Q. Tab 이동은 어떻게 테스트해?
A. `await user.tab()`을 사용하고 `toHaveFocus`로 현재 focus 요소를 확인한다.

Q. 모든 화면의 Tab 순서를 테스트해야 해?
A. 모든 화면은 부담이 크다. Form, Modal, Dropdown, Navigation 같은 핵심 상호작용 UI를 우선한다.

## 5.2 Focus Management Test

### [개념]

Focus Management Test는 UI 상태 변화 후 focus가 사용자의 다음 행동에 적절한 위치로 이동하는지 검증하는 테스트다.

Modal, error summary, route change, dropdown, toast action에서 중요하다.

### [핵심]

- focus management
- initial focus
- return focus
- focus trap
- focus restore
- focus on error
- modal focus
- route focus
- dropdown focus
- toHaveFocus

### [실무]

Modal open focus:

```tsx
test("모달이 열리면 확인 버튼에 focus가 이동한다", async () => {
  const user = userEvent.setup();

  render(<DeleteConfirmExample />);

  await user.click(screen.getByRole("button", { name: "삭제" }));

  expect(screen.getByRole("button", { name: "확인" })).toHaveFocus();
});
```

Modal close focus restore:

```tsx
test("모달을 닫으면 열기 버튼으로 focus가 돌아간다", async () => {
  const user = userEvent.setup();

  render(<DeleteConfirmExample />);

  const openButton = screen.getByRole("button", { name: "삭제" });

  await user.click(openButton);
  await user.click(screen.getByRole("button", { name: "취소" }));

  expect(openButton).toHaveFocus();
});
```

Error focus:

```tsx
test("제출 실패 시 첫 번째 오류 field에 focus가 이동한다", async () => {
  const user = userEvent.setup();

  render(<SignupForm />);

  await user.click(screen.getByRole("button", { name: "가입하기" }));

  expect(screen.getByLabelText("이메일")).toHaveFocus();
});
```

권장:

- Modal 열림/닫힘 focus 검증
- Form 오류 발생 시 focus 정책 검증
- route change 후 h1 focus 또는 main focus 정책 검토
- custom dropdown open 후 option focus 검증 가능
- focus 이동이 과도하면 사용자 흐름 방해 가능

### [FAQ]

Q. Focus Management는 왜 중요해?
A. 화면 변화 후 keyboard 사용자가 현재 위치를 잃지 않도록 하기 위해 중요하다.

Q. Modal을 닫으면 focus는 어디로 가야 해?
A. 일반적으로 Modal을 열었던 trigger 요소로 돌아가는 것이 좋다.

Q. 오류 발생 시 focus 이동은 항상 필요해?
A. Form이 크거나 오류 위치를 찾기 어려우면 첫 오류 field나 error summary로 이동하는 것이 좋다.

## 5.3 Escape Key Test

### [개념]

Escape Key Test는 Modal, Dialog, Dropdown, Tooltip, Menu 같은 일시적 UI가 Escape 키로 닫히는지 검증하는 테스트다.

### [핵심]

- Escape key
- user.keyboard
- close modal
- close dialog
- close dropdown
- close menu
- dismiss overlay
- keyboard interaction
- queryByRole

### [실무]

Modal:

```tsx
test("Escape 키를 누르면 모달이 닫힌다", async () => {
  const user = userEvent.setup();

  render(<NoticeModal defaultOpen />);

  expect(screen.getByRole("dialog")).toBeInTheDocument();

  await user.keyboard("{Escape}");

  expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
});
```

Dropdown:

```tsx
test("Escape 키를 누르면 드롭다운이 닫힌다", async () => {
  const user = userEvent.setup();

  render(<RegionDropdown />);

  await user.click(screen.getByRole("button", { name: "지역 선택" }));

  expect(screen.getByRole("listbox")).toBeInTheDocument();

  await user.keyboard("{Escape}");

  expect(screen.queryByRole("listbox")).not.toBeInTheDocument();
});
```

권장:

- overlay UI는 Escape 닫기 검토
- 닫힘 검증에는 queryBy 사용
- 닫힌 후 focus restore 확인 가능
- AlertDialog처럼 강제 확인이 필요한 경우 Escape 정책 명확화
- keyboard event에는 await 사용

### [FAQ]

Q. Escape Key Test는 언제 필요해?
A. Modal, Dropdown, Menu처럼 임시로 열리는 UI에서 닫기 기능이 중요할 때 필요하다.

Q. Escape로 닫힌 상태는 어떻게 확인해?
A. `queryByRole("dialog")` 또는 `queryByRole("listbox")`가 없는지 확인한다.

Q. 모든 Modal이 Escape로 닫혀야 해?
A. 일반 Modal은 닫히는 것이 좋지만 중요한 확인 Dialog는 프로젝트 정책에 따라 다를 수 있다.

# 6. Dialog and Modal Accessibility Test

## 6.1 Dialog Role Test

### [개념]

Dialog Role Test는 Modal 또는 Dialog가 `role="dialog"` 또는 native dialog semantics와 accessible name을 제공하는지 검증한다.

Dialog는 사용자 focus와 화면 맥락을 강하게 바꾸므로 접근성 테스트가 중요하다.

### [핵심]

- dialog
- alertdialog
- role dialog
- aria-modal
- aria-labelledby
- aria-describedby
- accessible name
- modal title
- focus trap
- close button

### [실무]

예:

```tsx
test("삭제 확인 모달은 dialog role과 accessible name을 가진다", () => {
  render(<DeleteConfirmModal open onClose={vi.fn()} />);

  expect(screen.getByRole("dialog", { name: "삭제 확인" })).toBeInTheDocument();
});
```

aria-modal:

```tsx
expect(screen.getByRole("dialog", { name: "삭제 확인" })).toHaveAttribute(
  "aria-modal",
  "true",
);
```

description 연결:

```tsx
expect(screen.getByRole("dialog", { name: "삭제 확인" })).toHaveAttribute(
  "aria-describedby",
  "delete-confirm-description",
);
```

권장:

- dialog role 제공
- title과 accessible name 연결
- aria-modal 사용
- close button accessible name 제공
- focus trap과 focus restore 테스트
- 중요한 확인은 alertdialog 검토

### [FAQ]

Q. Modal은 어떤 role을 가져야 해?
A. 일반적으로 dialog role을 사용하고 중요한 확인 Dialog는 alertdialog를 고려할 수 있다.

Q. Dialog accessible name은 어디서 와?
A. 보통 제목을 aria-labelledby로 연결하거나 aria-label을 사용한다.

Q. aria-modal은 왜 필요해?
A. Modal이 열렸을 때 사용자의 상호작용 범위가 Dialog 내부로 제한됨을 알리는 데 사용한다.

## 6.2 Focus Trap Test

### [개념]

Focus Trap Test는 Modal이 열린 동안 Tab focus가 Modal 내부를 벗어나지 않는지 검증하는 테스트다.

Keyboard 사용자가 배경 UI로 focus를 잃지 않도록 하기 위해 중요하다.

### [핵심]

- focus trap
- modal focus
- tab cycle
- shift tab
- first focusable
- last focusable
- background inert
- keyboard containment
- toHaveFocus

### [실무]

예:

```tsx
test("모달 내부에서 Tab focus가 순환한다", async () => {
  const user = userEvent.setup();

  render(<DeleteConfirmModal open onClose={vi.fn()} />);

  const cancelButton = screen.getByRole("button", { name: "취소" });
  const confirmButton = screen.getByRole("button", { name: "삭제" });

  await user.tab();
  expect(cancelButton).toHaveFocus();

  await user.tab();
  expect(confirmButton).toHaveFocus();

  await user.tab();
  expect(cancelButton).toHaveFocus();
});
```

Shift+Tab:

```tsx
await user.tab({ shift: true });
expect(confirmButton).toHaveFocus();
```

권장:

- Modal/Dialog에서 focus trap 검증
- 첫 focus 위치와 순환 확인
- 닫힘 후 focus restore 확인
- 구현 라이브러리에 따라 E2E에서 보강 가능
- focus trap이 없는 Modal은 keyboard 사용성 문제 발생 가능

### [FAQ]

Q. Focus Trap은 왜 필요해?
A. Modal이 열린 상태에서 keyboard focus가 배경 화면으로 빠져나가지 않도록 하기 위해 필요하다.

Q. Focus Trap은 어떻게 테스트해?
A. user.tab을 반복 실행하며 focus가 Modal 내부 요소 사이에서 순환하는지 확인한다.

Q. Focus Trap 테스트는 항상 Component Test로 충분해?
A. 라이브러리와 브라우저 동작에 따라 E2E에서 보강하는 것이 좋을 수 있다.

# 7. ARIA State Test

## 7.1 aria-expanded Test

### [개념]

`aria-expanded`는 Accordion, Dropdown, Menu, Disclosure처럼 펼침 상태가 있는 요소에서 현재 열림/닫힘 상태를 나타낸다.

### [핵심]

- aria-expanded
- expanded state
- collapsed state
- accordion
- dropdown
- disclosure
- menu button
- user click
- state sync

### [실무]

Accordion:

```tsx
test("아코디언 열림 상태를 aria-expanded로 표시한다", async () => {
  const user = userEvent.setup();

  render(<Accordion title="상세 정보">내용</Accordion>);

  const trigger = screen.getByRole("button", { name: "상세 정보" });

  expect(trigger).toHaveAttribute("aria-expanded", "false");

  await user.click(trigger);

  expect(trigger).toHaveAttribute("aria-expanded", "true");
});
```

Dropdown:

```tsx
await user.click(screen.getByRole("button", { name: "지역 선택" }));

expect(screen.getByRole("button", { name: "지역 선택" })).toHaveAttribute(
  "aria-expanded",
  "true",
);
```

권장:

- 실제 UI 표시 상태와 aria-expanded 일치
- 열림/닫힘 모두 테스트
- aria-controls 연결 검토 가능
- button trigger에 적용
- 단순 구현 세부사항이 아니라 접근성 상태로 테스트

### [FAQ]

Q. aria-expanded는 언제 써?
A. 펼치고 접을 수 있는 UI의 현재 상태를 보조기술에 전달할 때 사용한다.

Q. aria-expanded 테스트는 왜 필요해?
A. 시각적 열림 상태와 보조기술 상태가 일치하는지 확인하기 위해 필요하다.

Q. aria-expanded는 어떤 요소에 붙여?
A. 보통 펼침을 제어하는 button trigger에 붙인다.

## 7.2 aria-selected Test

### [개념]

`aria-selected`는 Tab, Option, GridCell처럼 선택 가능한 UI에서 현재 선택 상태를 나타낸다.

### [핵심]

- aria-selected
- selected state
- tab
- option
- listbox
- active tab
- selected option
- keyboard selection

### [실무]

Tab:

```tsx
test("선택된 tab은 aria-selected true를 가진다", async () => {
  const user = userEvent.setup();

  render(<FestivalTabs />);

  await user.click(screen.getByRole("tab", { name: "공지" }));

  expect(screen.getByRole("tab", { name: "공지" })).toHaveAttribute(
    "aria-selected",
    "true",
  );
});
```

Listbox option:

```tsx
expect(screen.getByRole("option", { name: "서울" })).toHaveAttribute(
  "aria-selected",
  "true",
);
```

권장:

- Tab UI는 tab / tabpanel 구조와 함께 테스트
- 선택 상태와 표시되는 panel 내용 함께 검증
- native select는 toBeSelected 사용 가능
- custom select는 aria-selected 검토
- selected className보다 aria-selected 우선

### [FAQ]

Q. aria-selected는 언제 테스트해?
A. Tab이나 custom select처럼 선택 상태를 보조기술에 전달해야 하는 UI에서 테스트한다.

Q. native select option도 aria-selected를 테스트해?
A. native option은 `toBeSelected` matcher가 더 적합할 수 있다.

Q. 선택 상태는 className으로 테스트해도 돼?
A. 가능하지만 접근성 상태인 aria-selected가 더 의미 있다.

## 7.3 aria-current Test

### [개념]

`aria-current`는 Navigation, Breadcrumb, Pagination에서 현재 Page나 현재 Step을 나타내는 ARIA 속성이다.

### [핵심]

- aria-current
- current page
- NavLink
- breadcrumb
- pagination
- stepper
- active route
- current item
- accessible current state

### [실무]

Navigation:

```tsx
test("현재 메뉴는 aria-current page를 가진다", () => {
  render(
    <MemoryRouter initialEntries={["/mypage"]}>
      <MainNavigation />
    </MemoryRouter>,
  );

  expect(screen.getByRole("link", { name: "마이페이지" })).toHaveAttribute(
    "aria-current",
    "page",
  );
});
```

Pagination:

```tsx
expect(screen.getByRole("link", { name: "2페이지" })).toHaveAttribute(
  "aria-current",
  "page",
);
```

권장:

- 현재 route / breadcrumb / page를 aria-current로 표현
- active className보다 aria-current 검증 우선
- 현재 Step이면 `aria-current="step"` 검토
- 현재 위치를 사용자에게 명확히 전달

### [FAQ]

Q. aria-current는 언제 써?
A. Navigation, Breadcrumb, Pagination에서 현재 위치를 나타낼 때 사용한다.

Q. NavLink active class 대신 aria-current를 테스트하는 이유는?
A. aria-current는 보조기술 사용자에게 현재 위치를 전달하는 접근성 상태이기 때문이다.

Q. aria-current 값은 항상 page야?
A. 아니다. 상황에 따라 page, step, location 등을 사용할 수 있다.

# 8. Image and Media Accessibility Test

## 8.1 Image Alt Test

### [개념]

Image Alt Test는 의미 있는 이미지가 적절한 alt text를 가지고, 장식용 이미지가 보조기술에서 불필요하게 읽히지 않도록 처리되었는지 검증하는 테스트다.

### [핵심]

- image alt
- getByAltText
- meaningful image
- decorative image
- empty alt
- thumbnail
- profile image
- festival image
- icon image
- accessible image

### [실무]

의미 있는 이미지:

```tsx
test("축제 대표 이미지는 alt text를 제공한다", () => {
  render(<FestivalImage src="/festival.png" title="봄꽃 축제" />);

  expect(screen.getByAltText("봄꽃 축제 대표 이미지")).toBeInTheDocument();
});
```

장식용 이미지:

```tsx
<img src="/decoration.svg" alt="" />
```

테스트:

```tsx
expect(screen.queryByAltText("decoration")).not.toBeInTheDocument();
```

권장:

- 의미 있는 이미지는 구체적인 alt 제공
- 축제 이미지, 프로필 이미지, 상품 이미지는 alt 필요
- 장식용 이미지는 `alt=""`
- alt에 “이미지” 같은 불필요한 반복 지양 가능
- icon button 안의 icon은 button name으로 의미 전달

### [FAQ]

Q. Image Alt Test는 왜 필요해?
A. 보조기술 사용자가 이미지의 의미를 이해할 수 있어야 하기 때문이다.

Q. 장식용 이미지도 alt가 필요해?
A. 장식용 이미지는 `alt=""`로 보조기술에서 무시되도록 한다.

Q. icon button의 아이콘 alt도 필요해?
A. 보통 button의 aria-label로 의미를 전달하고 icon 자체는 장식으로 처리할 수 있다.

## 8.2 Media Control Test

### [개념]

Media Control Test는 audio, video, carousel, slider 같은 media UI의 control이 접근 가능한 이름과 keyboard 조작을 제공하는지 검증하는 테스트다.

### [핵심]

- media control
- play button
- pause button
- mute button
- carousel control
- slider
- aria-label
- keyboard control
- visible control
- accessible name

### [실무]

Carousel control:

```tsx
test("캐러셀 이전/다음 버튼은 accessible name을 가진다", () => {
  render(<FestivalCarousel />);

  expect(
    screen.getByRole("button", { name: "이전 축제 보기" }),
  ).toBeInTheDocument();
  expect(
    screen.getByRole("button", { name: "다음 축제 보기" }),
  ).toBeInTheDocument();
});
```

Play button:

```tsx
expect(screen.getByRole("button", { name: "영상 재생" })).toBeInTheDocument();
```

권장:

- icon-only media control에는 aria-label 제공
- carousel auto-play는 정지 버튼 제공 검토
- slider는 keyboard 조작 검토
- 현재 slide 정보가 필요하면 status/aria-live 정책 검토
- 복잡한 media 접근성은 E2E/수동 검수 보강

### [FAQ]

Q. Carousel 버튼도 접근성 테스트가 필요해?
A. 필요하다. 이전/다음 버튼 목적이 명확히 전달되어야 한다.

Q. 자동 재생 Carousel에는 무엇이 필요해?
A. 사용자가 자동 재생을 멈출 수 있는 control을 제공하는 것이 좋다.

Q. Media 접근성은 RTL로 충분해?
A. 기본 control 이름은 가능하지만 실제 keyboard와 screen reader 경험은 E2E/수동 검수가 필요할 수 있다.

# 9. axe Automated Accessibility Test

## 9.1 axe Test Definition

### [개념]

axe Test는 `jest-axe` 또는 axe 기반 도구를 사용해 렌더링된 DOM의 자동 접근성 위반을 검사하는 테스트다.

axe는 누락된 label, 잘못된 ARIA 사용, 일부 landmark 문제 등을 자동으로 탐지할 수 있다.

### [핵심]

- axe
- jest-axe
- automated accessibility test
- toHaveNoViolations
- a11y scan
- WCAG
- ARIA validation
- label detection
- automated check
- manual check limitation

### [실무]

예:

```tsx
import { axe, toHaveNoViolations } from "jest-axe";

expect.extend(toHaveNoViolations);

test("LoginForm은 자동 접근성 위반이 없다", async () => {
  const { container } = render(<LoginForm />);

  const results = await axe(container);

  expect(results).toHaveNoViolations();
});
```

Provider가 필요한 Page:

```tsx
test("FestivalListPage는 자동 접근성 위반이 없다", async () => {
  vi.mocked(getFestivals).mockResolvedValue([
    { festivalId: 1, title: "봄꽃 축제" },
  ]);

  const { container } = renderWithProviders(<FestivalListPage />);

  await screen.findByText("봄꽃 축제");

  expect(await axe(container)).toHaveNoViolations();
});
```

권장:

- 주요 Form / Modal / Page에 axe test 추가
- 비동기 데이터 로딩 후 axe 실행
- axe는 보조 도구이며 keyboard/focus 테스트를 대체하지 않음
- false positive/환경 제한을 이해하고 사용
- 모든 작은 Component에 무분별하게 추가하지 않음

### [FAQ]

Q. axe Test는 뭐야?
A. 렌더링된 DOM을 자동으로 검사해 접근성 위반을 찾는 테스트다.

Q. axe Test만 있으면 접근성 검증이 충분해?
A. 아니다. axe는 자동 검사 도구이고 keyboard, focus, 사용자 흐름 테스트가 별도로 필요하다.

Q. 비동기 Page에서 axe는 언제 실행해?
A. 필요한 데이터와 UI가 렌더링된 뒤 실행해야 한다.

## 9.2 axe Test Caution

### [개념]

axe Test Caution은 axe 자동 검사가 모든 접근성 문제를 잡지 못하고, 테스트를 과도하게 느리게 만들 수 있음을 주의하는 규칙이다.

### [핵심]

주의 대상:

- axe is not complete
- keyboard not fully checked
- focus management not fully checked
- screen reader wording not fully checked
- color contrast environment limitation
- async rendering
- hidden element
- false positive
- slow test
- overuse caution

### [실무]

axe로 잡기 어려운 것:

```text
Tab 순서가 사용자 흐름에 맞는지
Modal focus trap이 실제로 동작하는지
오류 발생 후 focus가 적절히 이동하는지
링크 이름이 문맥상 충분히 이해되는지
동적 상태 변경이 사용자에게 적절히 전달되는지
```

보완 테스트:

```text
user.tab + toHaveFocus
user.keyboard("{Escape}")
getByRole name 검증
aria-expanded / aria-selected 검증
role alert / status 검증
```

권장:

- axe는 주요 Page/복잡한 Component 중심으로 사용
- 모든 테스트에 axe를 넣어 속도를 떨어뜨리지 않음
- axe 실패는 실제 접근성 문제인지 검토
- axe 통과를 접근성 완전 보장으로 해석하지 않음

### [FAQ]

Q. axe가 통과하면 접근성이 완벽한 거야?
A. 아니다. 자동 검사로 잡지 못하는 keyboard/focus/문맥 문제가 있다.

Q. axe 테스트를 모든 Component에 넣어야 해?
A. 권장하지 않는다. 주요 Page, Form, Modal, 복잡한 Component에 우선 적용한다.

Q. axe 테스트가 느리면 어떻게 해?
A. 핵심 대상만 선별하고 나머지는 role/label/keyboard 테스트로 보완한다.

# 10. Accessibility Troubleshooting

## 10.1 getByRole Failed

### [개념]

getByRole Failed는 요소를 role과 accessible name으로 찾을 수 없는 상황이다.

이는 테스트 문제일 수도 있지만 semantic HTML이나 accessible name이 부족한 접근성 문제일 수 있다.

### [핵심]

원인:

- wrong role
- missing accessible name
- icon button without label
- div used as button
- label not connected
- hidden element
- async rendering
- text mismatch
- aria-hidden parent
- role conflict

### [실무]

Debug Flow:

```text
getByRole 실패
→ screen.debug 확인
→ 실제 요소 존재 확인
→ native semantic element 확인
→ role이 맞는지 확인
→ accessible name 확인
→ aria-label / label / text 확인
→ hidden 여부 확인
→ 비동기면 findByRole 사용
```

문제:

```tsx
<button>
  <SearchIcon />
</button>
```

개선:

```tsx
<button aria-label="검색">
  <SearchIcon />
</button>
```

테스트:

```tsx
expect(screen.getByRole("button", { name: "검색" })).toBeInTheDocument();
```

권장:

- 실패 시 testId로 바로 우회하지 않음
- role/name 문제를 먼저 해결
- Testing Playground로 Query 후보 확인 가능
- inaccessible UI는 Component 개선 우선
- async UI는 findByRole 사용

### [FAQ]

Q. getByRole이 실패하면 무조건 테스트가 잘못된 거야?
A. 아니다. Component의 접근성 구조가 부족할 수 있다.

Q. 화면에는 버튼이 보이는데 getByRole로 못 찾아.
A. 실제 button이 아니거나 accessible name이 없을 수 있다.

Q. 해결을 위해 바로 getByTestId를 써도 돼?
A. 최후 수단이다. 먼저 semantic HTML과 accessible name을 개선하는 것이 좋다.

## 10.2 getByLabelText Failed

### [개념]

getByLabelText Failed는 Form control이 label과 올바르게 연결되지 않았거나 accessible label이 없는 상황이다.

### [핵심]

원인:

- label htmlFor mismatch
- input id missing
- label text mismatch
- aria-label missing
- aria-labelledby wrong id
- custom input wrapper
- hidden input
- placeholder only
- multiple labels

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

Custom Input Debug Flow:

```text
getByLabelText 실패
→ label htmlFor 확인
→ input id 확인
→ 실제 input에 id 전달되는지 확인
→ aria-label 확인
→ custom component가 props를 input까지 전달하는지 확인
```

권장:

- placeholder를 label 대체로 사용하지 않음
- reusable Input Component는 id/htmlFor 전달 확인
- password input은 getByLabelText 우선
- label 없는 Form field 발견 시 Component 개선

### [FAQ]

Q. getByLabelText가 실패하면 뭘 확인해?
A. label의 htmlFor와 input id가 연결되어 있는지 확인한다.

Q. custom Input에서 label이 안 잡혀.
A. id, aria-label, htmlFor가 실제 input 요소까지 전달되는지 확인해야 한다.

Q. placeholder로 찾으면 안 돼?
A. 가능하지만 label 기반 접근성이 더 좋다. placeholder는 label 대체가 아니다.

## 10.3 Focus Test Failed

### [개념]

Focus Test Failed는 기대한 요소에 focus가 이동하지 않거나 Tab 순서가 예상과 다른 상황이다.

DOM 순서, disabled 상태, hidden 상태, focus trap, custom component focus forwarding을 확인해야 한다.

### [핵심]

원인:

- element not focusable
- disabled element
- hidden element
- tabindex wrong
- DOM order mismatch
- focus trap missing
- focus not restored
- custom component ref issue
- user.tab await missing

### [실무]

Debug Flow:

```text
focus 테스트 실패
→ await user.tab 확인
→ 요소가 focusable인지 확인
→ disabled/hidden 여부 확인
→ DOM 순서 확인
→ tabindex 확인
→ custom component ref forwarding 확인
→ Modal focus trap 확인
```

잘못된 예:

```tsx
<div onClick={onClick}>저장</div>
```

개선:

```tsx
<button type="button" onClick={onClick}>
  저장
</button>
```

권장:

- native focusable element 사용
- tabindex 남용 지양
- disabled 요소는 focus되지 않음
- hidden 요소는 focus 대상이 아니어야 함
- custom component는 ref 전달 확인

### [FAQ]

Q. user.tab 후 focus가 예상과 달라.
A. DOM 순서, focusable 요소, disabled/hidden 상태, tabindex를 확인한다.

Q. div onClick은 Tab focus가 되지 않아?
A. 기본적으로 focus되지 않는다. button을 사용하는 것이 좋다.

Q. tabindex를 넣으면 해결돼?
A. 임시 해결일 수 있다. native semantic element를 우선 사용한다.

# 11. Accessibility Anti Pattern

## 11.1 Common Accessibility Testing Anti Patterns

### [개념]

Accessibility Testing Anti Pattern은 접근성 문제를 숨기거나 실제 사용자 접근성을 충분히 검증하지 못하는 잘못된 테스트 방식이다.

### [핵심]

Anti Pattern:

- getByTestId 우선 사용
- role/label 실패를 testId로 우회
- div onClick을 button으로 사용
- icon button label 누락
- placeholder를 label로 대체
- Modal dialog role 누락
- focus trap 미검증
- keyboard interaction 누락
- aria 속성만 붙이고 실제 상태 불일치
- aria 남용
- axe만 실행하고 keyboard 테스트 누락
- className active만 검증
- error message와 input 연결 누락

### [실무]

나쁜 예:

```tsx
screen.getByTestId("login-button");
```

좋은 예:

```tsx
screen.getByRole("button", { name: "로그인" });
```

나쁜 예:

```tsx
<input placeholder="이메일" />
```

좋은 예:

```tsx
<label htmlFor="email">이메일</label>
<input id="email" type="email" />
```

나쁜 예:

```tsx
expect(screen.getByRole("tab", { name: "공지" })).toHaveClass("active");
```

좋은 예:

```tsx
expect(screen.getByRole("tab", { name: "공지" })).toHaveAttribute(
  "aria-selected",
  "true",
);
```

검수 기준:

```text
사용자 관점 Query를 사용하는가?
keyboard 조작이 가능한가?
focus 흐름이 유지되는가?
aria 상태와 시각 상태가 일치하는가?
자동 검사와 수동적 시나리오 테스트를 함께 고려하는가?
```

### [FAQ]

Q. Accessibility Test에서 가장 흔한 실수는 뭐야?
A. role/label Query가 실패하자 testId로 우회하고 실제 접근성 문제를 고치지 않는 것이다.

Q. aria를 많이 붙이면 접근성이 좋아져?
A. 아니다. semantic HTML을 우선하고 필요한 ARIA만 정확히 사용해야 한다.

Q. axe만 돌리면 충분해?
A. 아니다. keyboard, focus, role/name 검증이 함께 필요하다.

# 12. Accessibility Testing Checklist

## 12.1 Accessibility Testing Checklist

### [개념]

Accessibility Testing Checklist는 Frontend UI가 role, label, keyboard, focus, ARIA, error, loading 접근성 기준을 만족하는지 확인하는 기준이다.

### [핵심]

Checklist:

```md
- [ ] interactive element는 native button/link/input을 사용하는가?
- [ ] button은 accessible name을 가지는가?
- [ ] icon button은 aria-label을 가지는가?
- [ ] link name만으로 목적지를 이해할 수 있는가?
- [ ] input / textarea / select는 label과 연결되어 있는가?
- [ ] checkbox / radio는 label로 선택지를 설명하는가?
- [ ] Page는 h1 heading을 제공하는가?
- [ ] 주요 영역은 main / nav / region landmark를 제공하는가?
- [ ] Modal은 dialog role과 accessible name을 가지는가?
- [ ] Modal focus trap과 focus restore를 검증했는가?
- [ ] keyboard로 주요 기능을 조작할 수 있는가?
- [ ] Tab focus 순서가 사용자 흐름과 맞는가?
- [ ] Escape로 overlay를 닫을 수 있는가?
- [ ] Form error는 aria-invalid / aria-describedby로 연결되는가?
- [ ] Error message는 role alert 또는 명확한 안내를 제공하는가?
- [ ] Loading은 role status 또는 accessible label을 제공하는가?
- [ ] aria-expanded / aria-selected / aria-current가 실제 상태와 일치하는가?
- [ ] 의미 있는 이미지는 alt text를 가지는가?
- [ ] 장식용 이미지는 alt=""로 처리되는가?
- [ ] 주요 Form / Modal / Page에 axe test를 고려했는가?
- [ ] getByTestId로 접근성 문제를 우회하지 않았는가?
```

### [실무]

Agent Accessibility Test 작성 Flow:

```text
Identify UI Type
→ Check Semantic HTML
→ Check Role / Accessible Name
→ Check Label Connection
→ Check Keyboard Interaction
→ Check Focus Management
→ Check ARIA State
→ Check Loading / Error Accessibility
→ Add axe Test if Useful
→ Review Anti Pattern
```

예:

```text
Login Form
→ h1 로그인
→ email label
→ password label
→ login button name
→ Tab order
→ Enter submit
→ validation error aria-invalid
→ global error role alert
→ axe scan
```

### [FAQ]

Q. Accessibility Testing Checklist의 핵심은 뭐야?
A. semantic HTML, role/name, label, keyboard, focus, ARIA 상태가 실제 사용자 흐름과 일치하는지 확인하는 것이다.

Q. 접근성 테스트 작성 전 무엇을 정해야 해?
A. UI 유형, 주요 조작 방식, focus 정책, error 표시 방식, 필요한 ARIA 상태를 정해야 한다.

Q. 접근성 테스트가 너무 많아지면 어떻게 해?
A. 핵심 Form, Modal, Navigation, 상태 UI를 우선하고 나머지는 role/label Query와 axe를 선별 적용한다.

# 13. Part12 Summary

## 13.1 Accessibility Testing Final Rule

### [개념]

Frontend Testing Part12는 접근성 테스트의 기준을 정의한다.

이 Part의 목적은 Agent가 React Component를 사용자 관점뿐 아니라 키보드, 보조기술, semantic HTML, ARIA 상태 기준으로 검증하게 만드는 것이다.

### [핵심]

최종 기준:

- 접근성 테스트는 RTL Query 전략과 연결됨
- Semantic HTML 우선
- getByRole / getByLabelText 우선
- button / link / input은 accessible name 필요
- icon button은 aria-label 필요
- Form field는 label과 연결
- 오류 field는 aria-invalid / aria-describedby 연결
- Loading은 role status 또는 accessible label 제공
- Error는 role alert 또는 명확한 안내 제공
- Modal은 dialog role, accessible name, focus trap, focus restore 검증
- Keyboard 조작은 user.tab / user.keyboard로 검증
- aria-expanded / aria-selected / aria-current는 실제 UI 상태와 일치
- 의미 있는 이미지는 alt text 제공
- 장식용 이미지는 alt="" 사용
- axe test는 보조 도구이며 keyboard/focus 테스트를 대체하지 않음
- getByTestId로 접근성 문제를 우회하지 않음

### [실무]

Agent 작업 Flow:

```text
Accessibility Test Request
→ Identify Component Role
→ Prefer Semantic HTML
→ Query by Role / Label
→ Verify Accessible Name
→ Verify Keyboard Flow
→ Verify Focus Behavior
→ Verify ARIA State
→ Verify Error / Loading Accessibility
→ Run axe if Needed
→ Remove Accessibility Anti Pattern
```

Part13 이후 연결:

```text
Part12 Accessibility Testing
→ Part13 Snapshot Test Caution
→ Part14 Test Structure
→ Part15 Troubleshooting
→ Part16 Frontend Testing Review
→ Part17 Final Frontend Testing Rules
```

### [FAQ]

Q. Part12의 최종 목적은 뭐야?
A. Frontend Agent가 role, label, keyboard, focus, ARIA 기준으로 접근 가능한 UI 테스트를 작성하게 만드는 것이다.

Q. Accessibility Testing에서 가장 중요한 규칙은 뭐야?
A. semantic HTML을 우선하고 role/name/label 기반으로 사용자가 접근 가능한 요소를 검증하는 것이다.

Q. Part12 다음에는 어떤 내용이 이어져야 해?
A. Snapshot Test의 한계와 사용 기준을 정의하는 Snapshot Test Caution 기준이 이어지는 것이 좋다.

# Retrieval Queries

### [FAQ]

Q. Accessibility Testing은 뭐야?
A. 키보드, 스크린리더, 보조기술 사용자도 UI를 사용할 수 있는지 검증하는 테스트다.

Q. 접근성 테스트는 왜 Frontend Testing에 중요해?
A. 접근성 좋은 UI는 실제 사용자 경험이 좋고 React Testing Library의 사용자 관점 테스트와도 잘 맞기 때문이다.

Q. 접근성 테스트는 axe만 돌리면 충분해?
A. 아니다. axe는 자동 검사 보조 도구이고 role, label, keyboard, focus 흐름 테스트도 필요하다.

Q. 모든 aria 속성을 테스트해야 해?
A. 아니다. 사용자 상태 전달에 중요한 aria 속성을 중심으로 테스트한다.

Q. 접근성 테스트는 Component Test야 Integration Test야?
A. 단순 role/label은 Component Test이고 focus 흐름이나 keyboard journey는 Integration 또는 E2E에 가깝다.

Q. Semantic HTML은 왜 중요해?
A. 브라우저와 보조기술이 요소의 의미를 이해할 수 있고 RTL Query도 사용자 관점으로 작성할 수 있기 때문이다.

Q. div에 role="button"을 붙이면 button과 같아?
A. 완전히 같지 않다. keyboard 동작과 기본 접근성까지 고려하면 native button이 더 좋다.

Q. 접근성 테스트에서 semantic HTML을 어떻게 확인해?
A. getByRole, getByLabelText 같은 accessible query로 요소를 찾을 수 있는지 확인한다.

Q. Heading Structure는 왜 테스트해?
A. Page 구조를 보조기술 사용자가 이해하고 탐색할 수 있어야 하기 때문이다.

Q. heading level까지 테스트해야 해?
A. 중요한 Page 구조에서는 level 옵션으로 검증하는 것이 좋다.

Q. Landmark는 왜 필요해?
A. 보조기술 사용자가 Page의 주요 영역으로 빠르게 이동할 수 있게 한다.

Q. navigation이 여러 개면 어떻게 해?
A. `aria-label`로 주요 메뉴, 사용자 메뉴처럼 구분한다.

Q. Accessible Name은 뭐야?
A. 보조기술이 버튼, 링크, 입력창 같은 요소를 사용자에게 설명할 때 사용하는 이름이다.

Q. icon button에는 왜 aria-label이 필요해?
A. 시각적 아이콘만으로는 보조기술 사용자가 버튼 목적을 알 수 없기 때문이다.

Q. getByRole name 옵션은 접근성 테스트야?
A. 그렇다. role과 accessible name으로 요소를 찾는 것은 접근성 구조를 함께 검증한다.

Q. Button Name Test는 왜 필요해?
A. 버튼 목적이 보조기술 사용자에게도 명확히 전달되어야 하기 때문이다.

Q. 아이콘만 있는 닫기 버튼은 어떻게 테스트해?
A. `getByRole("button", { name: "닫기" })`로 찾을 수 있어야 한다.

Q. Link Name Test는 왜 필요해?
A. 사용자가 링크 이름만 듣고 목적지를 이해할 수 있어야 하기 때문이다.

Q. “자세히” 링크는 안 좋아?
A. 문맥 없이 반복되면 목적지를 알기 어렵다. 항목명을 포함하는 이름이 좋다.

Q. Form input은 어떤 Query로 찾는 게 좋아?
A. label 기반 Query인 getByLabelText 또는 role과 name을 사용하는 것이 좋다.

Q. placeholder가 있으면 label이 없어도 돼?
A. 권장하지 않는다. placeholder는 label을 대체하기 어렵다.

Q. aria-invalid는 언제 true가 돼야 해?
A. 해당 field에 오류가 있을 때 true로 설정한다.

Q. aria-describedby는 왜 필요해?
A. input과 오류 메시지를 연결해 보조기술이 오류 내용을 함께 전달할 수 있게 한다.

Q. Error Summary는 언제 필요해?
A. 입력 field가 많아 오류 위치를 찾기 어려운 큰 Form에서 유용하다.

Q. 오류 요약 링크는 무엇을 해야 해?
A. 클릭 시 해당 오류 field로 focus를 이동시키는 것이 좋다.

Q. Keyboard Accessibility Test는 왜 필요해?
A. 마우스를 사용할 수 없는 사용자도 UI를 조작할 수 있어야 하기 때문이다.

Q. Tab 이동은 어떻게 테스트해?
A. `await user.tab()`을 사용하고 `toHaveFocus`로 현재 focus 요소를 확인한다.

Q. Focus Management는 왜 중요해?
A. 화면 변화 후 keyboard 사용자가 현재 위치를 잃지 않도록 하기 위해 중요하다.

Q. Modal을 닫으면 focus는 어디로 가야 해?
A. 일반적으로 Modal을 열었던 trigger 요소로 돌아가는 것이 좋다.

Q. Escape Key Test는 언제 필요해?
A. Modal, Dropdown, Menu처럼 임시로 열리는 UI에서 닫기 기능이 중요할 때 필요하다.

Q. Escape로 닫힌 상태는 어떻게 확인해?
A. `queryByRole("dialog")` 또는 `queryByRole("listbox")`가 없는지 확인한다.

Q. Modal은 어떤 role을 가져야 해?
A. 일반적으로 dialog role을 사용하고 중요한 확인 Dialog는 alertdialog를 고려할 수 있다.

Q. Dialog accessible name은 어디서 와?
A. 보통 제목을 aria-labelledby로 연결하거나 aria-label을 사용한다.

Q. Focus Trap은 왜 필요해?
A. Modal이 열린 상태에서 keyboard focus가 배경 화면으로 빠져나가지 않도록 하기 위해 필요하다.

Q. Focus Trap은 어떻게 테스트해?
A. user.tab을 반복 실행하며 focus가 Modal 내부 요소 사이에서 순환하는지 확인한다.

Q. aria-expanded는 언제 써?
A. 펼치고 접을 수 있는 UI의 현재 상태를 보조기술에 전달할 때 사용한다.

Q. aria-expanded 테스트는 왜 필요해?
A. 시각적 열림 상태와 보조기술 상태가 일치하는지 확인하기 위해 필요하다.

Q. aria-selected는 언제 테스트해?
A. Tab이나 custom select처럼 선택 상태를 보조기술에 전달해야 하는 UI에서 테스트한다.

Q. aria-current는 언제 써?
A. Navigation, Breadcrumb, Pagination에서 현재 위치를 나타낼 때 사용한다.

Q. Image Alt Test는 왜 필요해?
A. 보조기술 사용자가 이미지의 의미를 이해할 수 있어야 하기 때문이다.

Q. 장식용 이미지도 alt가 필요해?
A. 장식용 이미지는 `alt=""`로 보조기술에서 무시되도록 한다.

Q. axe Test는 뭐야?
A. 렌더링된 DOM을 자동으로 검사해 접근성 위반을 찾는 테스트다.

Q. axe Test만 있으면 접근성 검증이 충분해?
A. 아니다. axe는 자동 검사 도구이고 keyboard, focus, 사용자 흐름 테스트가 별도로 필요하다.

Q. axe가 통과하면 접근성이 완벽한 거야?
A. 아니다. 자동 검사로 잡지 못하는 keyboard/focus/문맥 문제가 있다.

Q. axe 테스트를 모든 Component에 넣어야 해?
A. 권장하지 않는다. 주요 Page, Form, Modal, 복잡한 Component에 우선 적용한다.

Q. getByRole이 실패하면 무조건 테스트가 잘못된 거야?
A. 아니다. Component의 접근성 구조가 부족할 수 있다.

Q. getByLabelText가 실패하면 뭘 확인해?
A. label의 htmlFor와 input id가 연결되어 있는지 확인한다.

Q. user.tab 후 focus가 예상과 달라.
A. DOM 순서, focusable 요소, disabled/hidden 상태, tabindex를 확인한다.

Q. Accessibility Test에서 가장 흔한 실수는 뭐야?
A. role/label Query가 실패하자 testId로 우회하고 실제 접근성 문제를 고치지 않는 것이다.

Q. aria를 많이 붙이면 접근성이 좋아져?
A. 아니다. semantic HTML을 우선하고 필요한 ARIA만 정확히 사용해야 한다.

Q. Accessibility Testing Checklist의 핵심은 뭐야?
A. semantic HTML, role/name, label, keyboard, focus, ARIA 상태가 실제 사용자 흐름과 일치하는지 확인하는 것이다.

Q. Part12 Accessibility Testing의 최종 목표는 뭐야?
A. Frontend Agent가 role, label, keyboard, focus, ARIA 기준으로 접근 가능한 UI 테스트를 작성하게 만드는 것이다.
