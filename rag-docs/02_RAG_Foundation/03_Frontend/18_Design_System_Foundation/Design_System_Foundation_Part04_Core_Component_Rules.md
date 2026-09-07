# Design System Foundation Part04 - Core Component Rules

---

# 1. Core Component Overview

## 1.1 Core Component Definition

### [개념]

Core Component는 Design System에서 가장 자주 재사용되는 기본 UI 컴포넌트다.

Core Component는 Frontend Agent가 화면을 생성할 때 우선 사용해야 하는 공통 UI 단위이며, Review Agent가 UI 일관성, 접근성, 상태 처리, token 사용 여부를 검토하는 기준이다.

Core Component는 화면마다 새로 만드는 일회성 UI가 아니라, 프로젝트 전체에서 반복 사용되는 UI 규격이다.

---

### [핵심]

Core Component 대상:

- Button
- Input
- Form Field
- Select
- Checkbox
- Radio
- Card
- Badge
- Tag
- Alert
- Toast
- Modal
- Dialog
- Tabs
- Pagination
- Table

Core Component 기준:

- 목적이 명확해야 한다.
- props API가 제한되어야 한다.
- variant 기준이 있어야 한다.
- size 기준이 있어야 한다.
- state 기준이 있어야 한다.
- accessibility 기준이 있어야 한다.
- Design Token과 연결되어야 한다.
- 사용 예시가 있어야 한다.
- Do / Don't 기준이 있어야 한다.
- Review Checklist가 있어야 한다.

---

### [실무]

Core Component 사용 Flow:

```text
Requirement
→ Core Component 검색
→ Component Specification 확인
→ Variant / Size / State 선택
→ Design Token 적용
→ Accessibility 적용
→ Usage 기준 확인
→ UI 구현
→ Review Checklist
```

Frontend Agent는 Button, Input, Card, Modal 같은 Core Component가 이미 정의되어 있다면 임의 div / button / input 스타일을 새로 만들지 않는다.

Review Agent는 구현 코드가 Core Component를 재사용하지 않고 화면별 직접 스타일을 남발하는지 확인한다.

---

### [FAQ]

Q. Core Component가 뭐야?
A. Design System에서 가장 자주 재사용되는 Button, Input, Card, Modal 같은 기본 UI 컴포넌트다.

Q. Core Component는 왜 필요해?
A. 화면마다 UI를 새로 만들지 않고 일관된 컴포넌트 기준으로 재사용하기 위해 필요하다.

Q. Core Component가 있으면 div로 직접 만들어도 안 돼?
A. 공통 UI가 이미 있다면 Core Component를 재사용하는 것이 좋다. 직접 구현은 예외 사유가 필요하다.

Q. Review Agent는 Core Component에서 뭘 봐야 해?
A. props API, variant, size, state, accessibility, token 사용, usage 기준을 확인해야 한다.

---

## 1.2 Core Component Selection Rules

### [개념]

Core Component Selection Rules는 요구사항에 맞는 공통 컴포넌트를 선택하는 기준이다.

Frontend Agent는 UI를 생성하기 전에 먼저 기존 Core Component로 해결 가능한지 확인해야 한다.

---

### [핵심]

선택 기준:

```text
사용자 행동 실행
→ Button

페이지 이동
→ Link

텍스트 입력
→ Input

입력 묶음
→ Form Field

옵션 하나 선택
→ Select 또는 Radio

여러 개 선택 / 동의
→ Checkbox

정보 그룹
→ Card

상태 / 수량 표시
→ Badge

카테고리 / 키워드 표시
→ Tag

화면 내 중요 안내
→ Alert

일시적 작업 결과
→ Toast

집중 작업 / 확인 / 입력
→ Modal / Dialog

콘텐츠 전환
→ Tabs

페이지 단위 데이터 탐색
→ Pagination

행 / 열 구조 데이터
→ Table
```

---

### [실무]

좋은 선택:

```jsx
<Button variant="primary">저장</Button>
<Link to="/orders">주문 목록으로 이동</Link>
<Badge variant="success">완료</Badge>
<Tag>생산</Tag>
```

나쁜 선택:

```jsx
<Button>주문 목록으로 이동</Button>
<Badge>삭제</Badge>
<div className="click-box">저장</div>
```

Review 기준:

```md
- [ ] 행동 실행에 Button을 사용하는가?
- [ ] 페이지 이동에 Link를 사용하는가?
- [ ] 상태 표시와 행동 버튼을 혼동하지 않는가?
- [ ] 표 데이터에 Table을 사용하는가?
- [ ] 관련 정보 묶음에 Card를 사용하는가?
```

---

### [FAQ]

Q. Button과 Link는 어떻게 구분해?
A. 저장, 삭제, 검색 같은 행동 실행은 Button이고, 페이지 이동은 Link다.

Q. Badge와 Button은 어떻게 구분해?
A. Badge는 상태나 수량 표시이고, Button은 사용자의 행동 실행이다.

Q. Card와 Table은 어떻게 구분해?
A. Card는 관련 정보를 묶어 보여줄 때 쓰고, Table은 행과 열 구조 데이터에 사용한다.

Q. Alert와 Toast는 어떻게 구분해?
A. Alert는 화면 안에 유지되는 중요한 안내이고, Toast는 일시적인 작업 결과 알림이다.

---

# 2. Button Component

## 2.1 Button Definition

### [개념]

Button은 사용자의 행동을 실행하는 interactive component다.

Button은 저장, 등록, 삭제, 검색, 다시 시도, 제출 같은 명확한 action을 수행할 때 사용한다.

Button은 페이지 이동을 위한 컴포넌트가 아니다. 페이지 이동은 Link를 사용한다.

---

### [핵심]

Button Spec:

```text
Purpose
→ 사용자 행동 실행

Variants
→ primary, secondary, danger, ghost

Sizes
→ sm, md, lg

States
→ default, hover, active, focus, disabled, loading

Required Accessibility
→ button element
→ type 기본값 button
→ focus-visible
→ loading 중 aria-busy 고려
→ icon button accessible name
```

Button Props:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "danger" | "ghost";
  size?: "sm" | "md" | "lg";
  isLoading?: boolean;
  disabled?: boolean;
  type?: "button" | "submit" | "reset";
  children: React.ReactNode;
  onClick?: () => void;
};
```

---

### [실무]

사용 예:

```jsx
<Button variant="primary" type="submit" isLoading={isSubmitting}>
  저장
</Button>

<Button variant="secondary" onClick={handleCancel}>
  취소
</Button>

<Button variant="danger" onClick={handleDelete}>
  삭제
</Button>

<Button variant="ghost" onClick={handleClose}>
  닫기
</Button>
```

기본 구현 기준:

```tsx
function Button({
  variant = "primary",
  size = "md",
  isLoading = false,
  disabled = false,
  type = "button",
  children,
  onClick,
}: ButtonProps) {
  return (
    <button
      type={type}
      disabled={disabled || isLoading}
      onClick={onClick}
      data-variant={variant}
      data-size={size}
      aria-busy={isLoading}
    >
      {isLoading ? "처리 중..." : children}
    </button>
  );
}
```

---

### [FAQ]

Q. Button은 언제 써?
A. 저장, 등록, 삭제, 검색, 다시 시도처럼 사용자의 행동을 실행할 때 사용한다.

Q. Button 기본 type은 뭐가 좋아?
A. 일반 Button 컴포넌트는 `button`을 기본값으로 두는 것이 안전하다.

Q. form submit 버튼은 어떻게 해?
A. 명시적으로 `type="submit"`을 사용한다.

Q. 페이지 이동에 Button을 써도 돼?
A. 권장하지 않는다. 페이지 이동은 Link를 사용한다.

---

## 2.2 Button Variant Rules

### [개념]

Button Variant는 버튼의 행동 중요도와 의미를 표현하는 기준이다.

Button Variant 이름은 색상 기준이 아니라 행동 의미 기준으로 작성한다.

---

### [핵심]

Button Variant:

| Variant   | 의미                  | 사용 예          |
| --------- | --------------------- | ---------------- |
| primary   | 가장 중요한 주요 행동 | 저장, 등록, 검색 |
| secondary | 보조 행동             | 취소, 뒤로가기   |
| danger    | 위험 행동             | 삭제, 탈퇴       |
| ghost     | 낮은 강조 행동        | 닫기, 보조 메뉴  |

금지:

- `blue`
- `red`
- `gray`
- `main`
- `sub`
- `bigBlue`

---

### [실무]

좋은 예:

```jsx
<Button variant="primary">저장</Button>
<Button variant="secondary">취소</Button>
<Button variant="danger">삭제</Button>
<Button variant="ghost">닫기</Button>
```

나쁜 예:

```jsx
<Button variant="danger">검색</Button>
<Button variant="primary">닫기</Button>
<Button variant="blue">저장</Button>
```

Token Mapping:

```text
primary
→ --button-primary-background
→ --button-primary-text

secondary
→ --button-secondary-background
→ --button-secondary-text
→ --button-secondary-border

danger
→ --button-danger-background
→ --button-danger-text

ghost
→ --button-ghost-background
→ --button-ghost-text
```

---

### [FAQ]

Q. Button primary는 언제 써?
A. 화면에서 가장 중요한 주요 행동에 사용한다. 예: 저장, 등록, 검색.

Q. Button secondary는 언제 써?
A. 주요 행동을 보조하는 취소, 뒤로가기 같은 행동에 사용한다.

Q. Button danger는 언제 써?
A. 삭제, 탈퇴, 되돌릴 수 없는 위험 행동에 사용한다.

Q. Button variant를 색상명으로 만들어도 돼?
A. 권장하지 않는다. 색상이 아니라 행동 의미 기준으로 만들어야 한다.

---

## 2.3 Button State Rules

### [개념]

Button State는 Button의 현재 조작 상태를 표현하는 규칙이다.

Button State는 시각 스타일, 동작 차단, 접근성 속성을 함께 포함해야 한다.

---

### [핵심]

Button 필수 state:

- default
- hover
- active
- focus
- disabled
- loading

Loading State 기준:

```text
loading
→ 처리 중 표시
→ disabled 처리
→ 중복 클릭 방지
→ aria-busy 고려
```

Disabled State 기준:

```text
disabled
→ 조작 불가
→ 클릭 이벤트 실행 금지
→ cursor not-allowed 고려
→ 시각적 비활성 표현
```

Focus State 기준:

```text
focus
→ focus-visible 제공
→ outline 제거 금지
→ keyboard 위치 인식 가능
```

---

### [실무]

CSS 예:

```css
.button:hover {
  background: var(--button-primary-background-hover);
}

.button:active {
  background: var(--button-primary-background-active);
}

.button:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}

.button:disabled {
  opacity: var(--opacity-disabled);
  cursor: not-allowed;
}
```

Review 기준:

```md
- [ ] hover / active / focus state가 있는가?
- [ ] focus-visible이 보이는가?
- [ ] loading 중 중복 클릭이 방지되는가?
- [ ] disabled 상태에서 onClick이 실행되지 않는가?
- [ ] icon button에 accessible name이 있는가?
```

---

### [FAQ]

Q. Button loading은 왜 필요해?
A. 처리 중임을 알리고 중복 클릭과 중복 API 요청을 막기 위해 필요하다.

Q. loading 중에는 disabled 처리해야 해?
A. 대부분 그렇다. 사용자의 중복 제출을 막기 위해 필요하다.

Q. Button focus-visible은 꼭 필요해?
A. 필요하다. 키보드 사용자가 현재 위치를 알 수 있어야 한다.

Q. disabled 스타일만 있으면 충분해?
A. 아니다. 실제 disabled 속성이나 조작 차단 로직도 필요하다.

---

## 2.4 Button Do and Don't

### [개념]

Button Do and Don't는 Button의 올바른 사용과 잘못된 사용을 구분하는 기준이다.

---

### [핵심]

Do:

- 명확한 동사 사용
- 주요 행동에 primary 사용
- 위험 행동에 danger 사용
- loading 중 disabled 처리
- form submit에는 `type="submit"` 명시
- 기본 type은 `button`
- icon button에는 accessible name 제공
- focus-visible 제공

Don't:

- 페이지 이동에 Button 사용 금지
- danger를 일반 행동에 사용 금지
- primary를 화면에 과도하게 남발 금지
- `OK`, `Submit` 같은 모호한 문구 남발 금지
- icon button에 aria-label 누락 금지
- disabled 스타일만 적용하고 실제 조작 가능하게 두기 금지

---

### [실무]

좋은 예:

```jsx
<Button variant="primary" type="submit" isLoading={isSubmitting}>
  저장
</Button>

<Button variant="danger" onClick={handleDelete}>
  삭제
</Button>
```

나쁜 예:

```jsx
<Button variant="danger">검색</Button>
<Button>OK</Button>
<Button onClick={goToPage}>목록으로 이동</Button>
```

Review Checklist:

```md
- [ ] Button 텍스트가 행동 중심인가?
- [ ] type 기본값이 안전한가?
- [ ] 위험 행동이 danger로 표현되는가?
- [ ] loading / disabled / focus 상태가 있는가?
- [ ] Link 역할을 Button이 대신하지 않는가?
```

---

### [FAQ]

Q. Button 텍스트는 어떻게 써야 해?
A. 저장, 삭제, 검색, 다시 시도처럼 사용자가 수행할 행동을 동사 중심으로 작성한다.

Q. Button에 OK라고 써도 돼?
A. 가능하면 피한다. 사용자가 어떤 행동이 실행되는지 명확해야 한다.

Q. icon button에는 뭐가 필요해?
A. `aria-label` 또는 스크린 리더용 텍스트가 필요하다.

Q. Button에서 가장 흔한 실수는?
A. 기본 type을 submit으로 두거나, loading 중 중복 클릭을 막지 않거나, danger variant를 잘못 쓰는 것이다.

---

# 3. Input and Form Field Component

## 3.1 Input Component Definition

### [개념]

Input은 사용자의 텍스트 입력을 받는 component다.

Input은 단독으로 쓰기보다 label, helper text, error message를 포함하는 Form Field 구조와 함께 사용하는 것이 좋다.

---

### [핵심]

Input Spec:

```text
Types
→ text, email, password, number, search, tel, url

States
→ default, focus, disabled, readonly, error, success

Required
→ id, name, label 연결, value, onChange

Recommended
→ placeholder, helperText, errorMessage, autocomplete
```

Input Props:

```tsx
type TextInputProps = {
  id: string;
  name: string;
  label?: string;
  value: string;
  placeholder?: string;
  disabled?: boolean;
  readOnly?: boolean;
  errorMessage?: string;
  onChange: (value: string) => void;
};
```

---

### [실무]

좋은 예:

```jsx
<TextInput
  id="email"
  name="email"
  label="이메일"
  value={email}
  placeholder="example@email.com"
  errorMessage={emailError}
  onChange={setEmail}
/>
```

나쁜 예:

```jsx
<input placeholder="이메일" />
<input style={{ borderColor: "red" }} />
```

Input 상태 기준:

```text
focus
→ border focus token
→ focus-visible 확인

error
→ border error token
→ error message 표시
→ aria-invalid true
→ aria-describedby 연결

disabled
→ 조작 불가
→ 제출 제외

readonly
→ 수정 불가
→ 값 읽기 가능
```

---

### [FAQ]

Q. Input은 언제 써?
A. 사용자의 텍스트, 이메일, 비밀번호, 숫자, 검색어 같은 값을 입력받을 때 사용한다.

Q. placeholder만 있으면 label은 없어도 돼?
A. 권장하지 않는다. placeholder는 입력 예시이고 label은 입력 항목의 이름이다.

Q. disabled와 readonly는 뭐가 달라?
A. disabled는 조작과 제출에서 제외되고, readonly는 수정은 불가하지만 값은 읽을 수 있다.

Q. Input error는 어떻게 표시해야 해?
A. border 색상, error message, aria-invalid, aria-describedby를 함께 사용한다.

---

## 3.2 Form Field Component Definition

### [개념]

Form Field는 label, control, helper text, error message를 하나의 구조로 묶는 component다.

Form Field는 입력 컴포넌트의 접근성과 시각적 일관성을 유지하기 위한 핵심 패턴이다.

---

### [핵심]

Form Field Anatomy:

```text
Label
→ Control
→ Helper Text
→ Error Message
```

Form Field 기준:

- label과 input 연결
- placeholder를 label 대체로 사용 금지
- helper text와 error message 구분
- error message를 input과 연결
- required 표시 명확화
- spacing token 사용
- error 상태를 색상만으로 표시 금지

Props 예:

```tsx
type FormFieldProps = {
  id: string;
  label: string;
  helperText?: string;
  errorMessage?: string;
  required?: boolean;
  children: React.ReactNode;
};
```

---

### [실무]

좋은 예:

```jsx
<FormField
  id="email"
  label="이메일"
  helperText="로그인에 사용할 이메일을 입력해 주세요."
  errorMessage={emailError}
  required
>
  <TextInput id="email" name="email" value={email} onChange={setEmail} />
</FormField>
```

HTML 구조 예:

```jsx
<div className="formField">
  <label htmlFor="email">이메일</label>
  <input
    id="email"
    name="email"
    aria-invalid="true"
    aria-describedby="email-error"
  />
  <p id="email-error" role="alert">
    올바른 이메일 형식이 아닙니다.
  </p>
</div>
```

---

### [FAQ]

Q. Form Field가 뭐야?
A. label, input, helper text, error message를 하나의 구조로 묶는 component다.

Q. Form Field를 따로 만들면 좋아?
A. 반복되는 입력 구조를 일관되게 유지할 수 있어 좋다.

Q. error message는 input과 연결해야 해?
A. 해야 한다. `aria-describedby`로 연결하면 스크린 리더 사용자가 오류를 알 수 있다.

Q. helper text와 error message는 구분해야 해?
A. 구분해야 한다. helper text는 안내이고 error message는 오류 상태다.

---

## 3.3 Input State Rules

### [개념]

Input State는 입력 컴포넌트의 현재 상태를 표현하는 규칙이다.

Input State는 사용자 입력 가능 여부, 오류 여부, 성공 여부, 읽기 전용 여부를 명확하게 전달해야 한다.

---

### [핵심]

Input 필수 state:

- default
- focus
- disabled
- readonly
- error
- success

State 기준:

```text
default
→ 기본 입력 가능 상태

focus
→ 현재 입력 중인 상태

disabled
→ 입력 불가, 제출 제외

readonly
→ 수정 불가, 값 읽기 가능

error
→ 입력값 오류

success
→ 입력값 유효 또는 처리 성공
```

---

### [실무]

CSS 예:

```css
.input {
  border: 1px solid var(--input-border);
  background: var(--input-background);
  color: var(--input-text);
}

.input:focus {
  border-color: var(--input-border-focus);
}

.input[aria-invalid="true"] {
  border-color: var(--input-border-error);
}

.input:disabled {
  background: var(--color-background-disabled);
  color: var(--color-text-disabled);
}
```

Review 기준:

```md
- [ ] label과 input이 연결되어 있는가?
- [ ] focus state가 명확한가?
- [ ] disabled와 readonly가 구분되는가?
- [ ] error state가 메시지와 연결되는가?
- [ ] error를 색상만으로 표시하지 않는가?
```

---

### [FAQ]

Q. Input state에는 뭐가 있어?
A. default, focus, disabled, readonly, error, success 상태가 있다.

Q. Input focus는 왜 중요해?
A. 사용자가 현재 어떤 입력 필드를 조작 중인지 알아야 하기 때문이다.

Q. error border만 있으면 충분해?
A. 아니다. error message와 aria 속성 연결이 필요하다.

Q. success state는 항상 필요해?
A. 항상 필수는 아니지만 입력 검증 성공을 명확히 보여야 하는 경우 필요하다.

---

## 3.4 Input and Form Field Do and Don't

### [개념]

Input and Form Field Do and Don't는 입력 컴포넌트의 올바른 사용과 잘못된 사용을 구분하는 기준이다.

---

### [핵심]

Do:

- label을 반드시 제공한다.
- label과 input을 연결한다.
- placeholder는 입력 예시로만 사용한다.
- errorMessage를 input과 연결한다.
- error 상태는 색상과 문구를 함께 사용한다.
- disabled와 readonly를 구분한다.
- autocomplete 속성을 고려한다.
- form spacing은 token으로 관리한다.

Don't:

- placeholder를 label 대체로 사용하지 않는다.
- error를 빨간 border만으로 표시하지 않는다.
- 서버 raw error를 그대로 노출하지 않는다.
- 입력마다 임의 spacing을 직접 지정하지 않는다.
- disabled 상태인데 값 수정이 가능하게 두지 않는다.
- label 없는 input을 만들지 않는다.

---

### [실무]

좋은 예:

```jsx
<label htmlFor="password">비밀번호</label>
<input
  id="password"
  name="password"
  type="password"
  autoComplete="current-password"
  aria-invalid={Boolean(passwordError)}
  aria-describedby={passwordError ? "password-error" : undefined}
/>
{passwordError && (
  <p id="password-error" role="alert">
    {passwordError}
  </p>
)}
```

나쁜 예:

```jsx
<input placeholder="비밀번호" />
<p style={{ color: "red" }}>Error</p>
```

Review Checklist:

```md
- [ ] placeholder가 label을 대체하지 않는가?
- [ ] error message가 사용자 친화적인가?
- [ ] aria-invalid / aria-describedby가 필요한 곳에 있는가?
- [ ] disabled와 readonly가 구분되는가?
- [ ] form field spacing이 일관적인가?
```

---

### [FAQ]

Q. Input에서 가장 흔한 실수는?
A. placeholder를 label처럼 사용하고 error message를 input과 연결하지 않는 것이다.

Q. autocomplete는 꼭 써야 해?
A. 로그인, 이메일, 비밀번호 같은 필드에서는 적절히 사용하는 것이 좋다.

Q. raw error message를 보여줘도 돼?
A. 권장하지 않는다. 사용자가 이해할 수 있는 문장으로 바꿔야 한다.

Q. Form Field spacing은 어디서 관리해?
A. 개별 input margin보다 form layout gap과 spacing token으로 관리하는 것이 좋다.

---

# 4. Select Checkbox Radio Component

## 4.1 Select Component Rules

### [개념]

Select는 여러 옵션 중 하나를 선택할 때 사용하는 form component다.

옵션이 많고 화면 공간을 줄여야 할 때 Select가 적합하다.

---

### [핵심]

Select 사용 기준:

```text
옵션이 많음
→ Select

옵션이 적고 비교가 중요함
→ Radio

여러 개 선택
→ Checkbox
```

Select 필수 기준:

- label 제공
- selected value 명확화
- disabled 상태 제공
- error 상태 제공
- keyboard 조작 가능
- 옵션 텍스트 명확화
- placeholder option 사용 시 실제 값과 구분
- custom select는 접근성 주의

Props 예:

```tsx
type SelectProps = {
  id: string;
  name: string;
  label: string;
  value: string;
  options: Array<{ label: string; value: string }>;
  placeholder?: string;
  disabled?: boolean;
  errorMessage?: string;
  onChange: (value: string) => void;
};
```

---

### [실무]

Native Select 예:

```jsx
<label htmlFor="role">권한</label>
<select
  id="role"
  name="role"
  value={role}
  onChange={(event) => setRole(event.target.value)}
>
  <option value="">권한을 선택해 주세요</option>
  <option value="ADMIN">관리자</option>
  <option value="USER">사용자</option>
</select>
```

Review 기준:

```md
- [ ] label과 select가 연결되어 있는가?
- [ ] options label이 명확한가?
- [ ] disabled / error 상태가 있는가?
- [ ] keyboard 조작이 가능한가?
- [ ] custom select 접근성을 검토했는가?
```

---

### [FAQ]

Q. Select는 언제 써?
A. 옵션이 많고 하나를 선택해야 할 때 사용한다.

Q. Radio와 Select 중 뭐를 써야 해?
A. 옵션이 적고 비교가 필요하면 Radio, 옵션이 많으면 Select가 적합하다.

Q. custom select를 만들어도 돼?
A. 가능하지만 keyboard, focus, aria, screen reader 접근성을 신중히 구현해야 한다.

Q. Select에도 label이 필요해?
A. 필요하다. 사용자가 어떤 값을 선택하는지 명확해야 한다.

---

## 4.2 Checkbox Component Rules

### [개념]

Checkbox는 여러 옵션을 선택하거나 동의 여부를 표시할 때 사용하는 form component다.

Checkbox는 선택 상태가 independent하거나 다중 선택이 가능할 때 사용한다.

---

### [핵심]

Checkbox 사용 기준:

- 여러 개 선택
- 약관 동의
- 필터 선택
- 항목 선택
- on / off가 즉시 적용되지 않는 선택

Checkbox 필수 상태:

- unchecked
- checked
- indeterminate
- disabled
- focus
- error

기준:

- label 제공
- checked 상태 명확화
- keyboard 조작 가능
- disabled 상태 제공
- 색상만으로 선택 상태 표시 금지
- custom checkbox는 native input 유지 권장

---

### [실무]

Checkbox 예:

```jsx
<label>
  <input
    type="checkbox"
    checked={agreed}
    onChange={(event) => setAgreed(event.target.checked)}
  />
  약관에 동의합니다.
</label>
```

다중 선택 예:

```jsx
<label>
  <input
    type="checkbox"
    name="equipment"
    value="EQ1"
    checked={selectedEquipments.includes("EQ1")}
    onChange={handleEquipmentChange}
  />
  EQ1
</label>
```

Review 기준:

```md
- [ ] checkbox label이 명확한가?
- [ ] checked 상태가 시각적으로 명확한가?
- [ ] keyboard 조작이 가능한가?
- [ ] custom checkbox가 native 접근성을 유지하는가?
```

---

### [FAQ]

Q. Checkbox는 언제 써?
A. 여러 개 선택하거나 약관 동의 같은 선택 상태를 표시할 때 사용한다.

Q. Checkbox와 Switch는 뭐가 달라?
A. Checkbox는 선택이나 동의에 적합하고, Switch는 즉시 적용되는 on / off 설정에 적합하다.

Q. Checkbox에는 label이 필요해?
A. 필요하다. 사용자가 무엇을 선택하는지 명확해야 한다.

Q. Checkbox 선택 상태는 색상만으로 표시해도 돼?
A. 안 된다. 체크 표시, 텍스트, 상태 속성 등을 함께 사용해야 한다.

---

## 4.3 Radio Component Rules

### [개념]

Radio는 여러 옵션 중 하나만 선택해야 할 때 사용하는 form component다.

옵션 수가 적고 사용자가 선택지를 비교해야 할 때 Radio가 적합하다.

---

### [핵심]

Radio 사용 기준:

- 하나만 선택
- 옵션 수가 적음
- 선택지 비교가 필요함
- 모든 옵션을 화면에 보여주는 것이 좋음

Radio 필수 기준:

- 관련 radio는 같은 name 사용
- fieldset / legend 사용 고려
- label 제공
- checked 상태 명확화
- keyboard 조작 가능
- disabled 상태 제공
- error 상태 필요 시 표시

---

### [실무]

Radio 예:

```jsx
<fieldset>
  <legend>정렬 기준</legend>

  <label>
    <input
      type="radio"
      name="sort"
      value="latest"
      checked={sort === "latest"}
      onChange={handleSortChange}
    />
    최신순
  </label>

  <label>
    <input
      type="radio"
      name="sort"
      value="popular"
      checked={sort === "popular"}
      onChange={handleSortChange}
    />
    인기순
  </label>
</fieldset>
```

Review 기준:

```md
- [ ] 같은 그룹 radio가 같은 name을 사용하는가?
- [ ] fieldset / legend 사용을 고려했는가?
- [ ] label이 명확한가?
- [ ] checked 상태가 명확한가?
- [ ] keyboard 조작이 가능한가?
```

---

### [FAQ]

Q. Radio는 언제 써?
A. 옵션이 적고 여러 선택지 중 하나만 선택해야 할 때 사용한다.

Q. Radio 그룹에는 같은 name이 필요해?
A. 필요하다. 같은 name을 사용해야 하나의 그룹으로 동작한다.

Q. fieldset과 legend는 왜 필요해?
A. 관련 radio 그룹의 의미를 스크린 리더와 사용자에게 명확히 전달하기 위해 필요하다.

Q. 옵션이 많으면 Radio가 좋아?
A. 아니다. 옵션이 많으면 Select가 더 적합할 수 있다.

---

## 4.4 Select Checkbox Radio Do and Don't

### [개념]

Select, Checkbox, Radio Do and Don't는 선택 컴포넌트의 올바른 사용과 잘못된 사용을 구분하는 기준이다.

---

### [핵심]

Do:

- Select는 옵션이 많을 때 사용한다.
- Radio는 옵션이 적고 하나만 선택할 때 사용한다.
- Checkbox는 여러 개 선택하거나 동의 여부에 사용한다.
- label을 제공한다.
- keyboard 조작을 보장한다.
- custom control은 native input 접근성을 유지한다.
- 선택 상태를 명확히 표시한다.

Don't:

- 옵션이 적은데 무조건 Select로 숨기지 않는다.
- 여러 개 선택인데 Radio를 사용하지 않는다.
- 하나만 선택해야 하는데 Checkbox를 사용하지 않는다.
- label 없는 선택 컴포넌트를 만들지 않는다.
- 색상만으로 선택 상태를 표시하지 않는다.
- custom control에서 input 접근성을 제거하지 않는다.

---

### [실무]

좋은 선택:

```text
옵션 3개 중 하나 선택
→ Radio

옵션 20개 중 하나 선택
→ Select

여러 설비 필터 선택
→ Checkbox
```

나쁜 선택:

```text
약관 동의
→ Radio 사용

정렬 기준 2개
→ Select로 숨김

다중 필터
→ Radio 사용
```

Review Checklist:

```md
- [ ] 선택 방식과 컴포넌트가 일치하는가?
- [ ] label이 제공되는가?
- [ ] keyboard 조작이 가능한가?
- [ ] 선택 상태가 명확한가?
- [ ] custom control 접근성이 유지되는가?
```

---

### [FAQ]

Q. 선택 컴포넌트에서 가장 흔한 실수는?
A. Select, Radio, Checkbox의 선택 목적을 혼동하고 label이나 keyboard 접근성을 누락하는 것이다.

Q. 옵션이 2개면 Select보다 Radio가 좋아?
A. 비교가 필요한 선택이라면 Radio가 더 명확한 경우가 많다.

Q. custom checkbox를 만들어도 돼?
A. 가능하지만 native input의 접근성과 keyboard 동작을 유지해야 한다.

Q. 선택 상태는 어떻게 표시해야 해?
A. 시각적 표시, 텍스트, checked / selected 상태 속성을 함께 사용해야 한다.

---

# 5. Card Badge Tag Component

## 5.1 Card Component Rules

### [개념]

Card는 관련 정보를 하나의 시각적 그룹으로 묶어 보여주는 component다.

Card는 목록, 요약, 상세 일부, 통계, 프로필, 알림, 제품, 생산 항목 같은 정보를 구조화할 때 사용한다.

---

### [핵심]

Card Anatomy:

```text
Container
→ Header
→ Media
→ Body
→ Footer
→ Actions
```

Card 사용 대상:

- 축제 카드
- 리뷰 카드
- 알림 카드
- 상품 카드
- 프로필 카드
- 통계 카드
- 생산 현황 카드
- 설비 상태 카드
- LOT 요약 카드

Card 기준:

- 의미에 따라 article 또는 section 고려
- 제목 구조 명확화
- 이미지 alt 제공
- 내부 spacing은 token 사용
- 외부 간격은 parent layout gap 사용
- 클릭 영역과 버튼 역할 구분
- loading / empty 상태 고려

---

### [실무]

Card 예:

```jsx
<article className="card">
  <img src="/equipment.jpg" alt="EQ1 설비 이미지" />
  <div className="cardBody">
    <h2 className="cardTitle">EQ1 구동부 조립</h2>
    <p className="cardDescription">현재 상태: 정상 가동</p>
    <Button variant="primary">상세 보기</Button>
  </div>
</article>
```

Card Composition 예:

```jsx
<Card>
  <CardHeader>
    <CardTitle>LOT 생산 현황</CardTitle>
  </CardHeader>
  <CardBody>
    <p>완료 120EA / 불량 3EA</p>
  </CardBody>
  <CardFooter>
    <Button variant="secondary">이력 보기</Button>
  </CardFooter>
</Card>
```

---

### [FAQ]

Q. Card는 언제 써?
A. 관련 정보를 하나의 시각적 그룹으로 묶어 보여줄 때 사용한다.

Q. Card 전체를 클릭 가능하게 해도 돼?
A. 가능하지만 내부 버튼과 충돌하지 않게 하고 접근성을 고려해야 한다.

Q. Card에 margin을 직접 줘도 돼?
A. 재사용 Card라면 권장하지 않는다. Card List나 Grid 부모에서 gap으로 관리하는 것이 좋다.

Q. Card 이미지에는 alt가 필요해?
A. 의미 있는 이미지라면 alt를 제공해야 한다. 장식 이미지는 빈 alt를 고려할 수 있다.

---

## 5.2 Card Layout and State Rules

### [개념]

Card Layout and State Rules는 Card 내부 구조와 loading, selected, disabled, empty 같은 상태를 정의하는 기준이다.

---

### [핵심]

Card Layout 기준:

- Header는 제목 / 메타 정보 표시
- Media는 이미지 / 차트 / 썸네일 표시
- Body는 주요 내용 표시
- Footer는 보조 정보 / actions 표시
- Actions는 Button 또는 Link 사용
- Card 내부 padding은 token 사용
- Card 목록 간격은 parent grid gap 사용

Card State:

- default
- hover
- focus
- selected
- disabled
- loading
- error

---

### [실무]

Card CSS 예:

```css
.card {
  background: var(--card-background);
  border: 1px solid var(--card-border);
  border-radius: var(--card-radius);
  box-shadow: var(--card-shadow);
  padding: var(--spacing-4);
}

.cardList {
  display: grid;
  gap: var(--spacing-6);
}
```

Clickable Card 기준:

```jsx
<article className="card">
  <h2>
    <Link to="/lots/LOT-001">LOT-001 생산 현황</Link>
  </h2>
  <p>완료 120EA / 불량 3EA</p>
</article>
```

Review 기준:

```md
- [ ] Card 내부 구조가 명확한가?
- [ ] Card 자체 margin을 남발하지 않는가?
- [ ] Card list는 parent gap으로 관리되는가?
- [ ] 클릭 가능한 영역과 action button 역할이 충돌하지 않는가?
- [ ] title 구조가 명확한가?
```

---

### [FAQ]

Q. Card 내부 구조에는 뭐가 있어?
A. Header, Media, Body, Footer, Actions 구조를 사용할 수 있다.

Q. Card list 간격은 어디서 관리해?
A. Card 자체가 아니라 Card Grid나 parent layout의 gap으로 관리한다.

Q. 클릭 가능한 Card는 어떻게 만드는 게 좋아?
A. 전체 Card click보다 제목 Link 또는 명확한 action을 제공하는 방식이 접근성에 유리하다.

Q. Card loading 상태는 어떻게 표현해?
A. 카드 구조가 예상 가능하면 Skeleton Card를 사용할 수 있다.

---

## 5.3 Badge Component Rules

### [개념]

Badge는 상태, 수량, 짧은 라벨을 표시하는 component다.

Badge는 사용자가 현재 상태를 빠르게 파악할 수 있도록 짧고 명확한 텍스트를 제공해야 한다.

---

### [핵심]

Badge 사용 대상:

- 상태 표시
- 수량 표시
- 알림 개수
- 처리 상태
- 생산 상태
- 권한 상태
- 오류 / 경고 상태

Badge Variant:

```text
default
primary
success
warning
error
info
```

Badge 기준:

- 색상만으로 상태 전달 금지
- 텍스트 포함
- variant 의미 명확화
- 짧은 문구 사용
- 상태 token과 연결
- 너무 많은 색상 variant 금지

---

### [실무]

Badge 예:

```jsx
<Badge variant="success">정상</Badge>
<Badge variant="warning">점검 필요</Badge>
<Badge variant="error">불량</Badge>
<Badge variant="info">대기</Badge>
```

생산 상태 예:

```jsx
<Badge variant="success">완료</Badge>
<Badge variant="warning">진행중</Badge>
<Badge variant="error">NG</Badge>
```

Review 기준:

```md
- [ ] Badge 텍스트가 짧고 명확한가?
- [ ] 상태를 색상만으로 전달하지 않는가?
- [ ] variant 의미가 semantic color와 연결되는가?
- [ ] Badge를 행동 버튼처럼 사용하지 않는가?
```

---

### [FAQ]

Q. Badge는 언제 써?
A. 상태, 수량, 알림 개수처럼 짧은 정보를 표시할 때 사용한다.

Q. Badge와 Button은 뭐가 달라?
A. Badge는 상태 표시이고 Button은 행동 실행이다.

Q. 상태 Badge는 색상만 있으면 돼?
A. 안 된다. 텍스트도 함께 제공해야 한다.

Q. Badge variant는 어떻게 정해?
A. success, warning, error, info처럼 상태 의미 기준으로 정한다.

---

## 5.4 Tag Component Rules

### [개념]

Tag는 카테고리, 키워드, 속성, 필터 항목을 표시하는 component다.

Tag는 상태보다는 분류나 메타 정보를 표현하는 데 적합하다.

---

### [핵심]

Tag 사용 대상:

- 카테고리
- 키워드
- 필터
- 속성
- 기술 스택
- 품목 유형
- 설비 유형
- LOT 그룹

Tag 기준:

- 짧은 텍스트 사용
- 상태 표시보다 분류 표시
- 제거 가능한 Tag는 remove action 명확화
- 선택 가능한 Tag는 selected state 명확화
- Badge와 의미 구분

---

### [실무]

Tag 예:

```jsx
<Tag>조립</Tag>
<Tag>검사</Tag>
<Tag>EV Relay</Tag>
<Tag>LOT</Tag>
```

Filter Tag 예:

```jsx
<Tag selected onRemove={handleRemove}>
  EQ1
</Tag>
```

Badge와 구분:

```jsx
<Badge variant="success">정상</Badge>
<Tag>구동부 조립</Tag>
```

Review 기준:

```md
- [ ] Tag가 상태가 아닌 분류 / 키워드 표현에 사용되는가?
- [ ] remove action이 있으면 accessible name이 있는가?
- [ ] selected 상태가 명확한가?
- [ ] Badge와 의미가 혼동되지 않는가?
```

---

### [FAQ]

Q. Tag는 언제 써?
A. 카테고리, 키워드, 필터, 속성 같은 분류 정보를 표시할 때 사용한다.

Q. Badge와 Tag는 뭐가 달라?
A. Badge는 상태나 수량 표시이고, Tag는 카테고리나 키워드 표시다.

Q. Tag에 삭제 버튼을 넣어도 돼?
A. 가능하다. remove action이 있으면 접근 가능한 이름과 키보드 조작을 제공해야 한다.

Q. Tag를 상태 표시로 써도 돼?
A. 상태 표시에는 Badge가 더 적합하다.

---

# 6. Alert Toast Component

## 6.1 Alert Component Rules

### [개념]

Alert는 화면 안에 고정적으로 표시되는 중요한 안내, 경고, 오류, 성공 메시지 component다.

Alert는 사용자가 놓치면 안 되는 정보를 문맥 안에서 지속적으로 보여줄 때 사용한다.

---

### [핵심]

Alert 사용 대상:

- 오류 안내
- 경고 안내
- 성공 안내
- 정보 안내
- 권한 안내
- 인증 필요 안내
- 데이터 로드 실패
- 폼 제출 실패

Alert Variant:

```text
info
success
warning
error
```

Alert 기준:

- 화면 문맥 안에 표시
- title과 description 고려
- 닫기 가능 여부 명확화
- role alert 사용 여부 검토
- 색상만으로 상태 전달 금지
- 복구 action 제공 가능

---

### [실무]

Alert 예:

```jsx
<Alert variant="error" title="데이터를 불러오지 못했습니다">
  네트워크 상태를 확인한 뒤 다시 시도해 주세요.
</Alert>
```

Action 포함 예:

```jsx
<Alert
  variant="warning"
  title="권한이 필요합니다"
  action={<Button variant="secondary">권한 요청</Button>}
>
  이 화면은 관리자 권한이 있어야 사용할 수 있습니다.
</Alert>
```

Review 기준:

```md
- [ ] Alert variant가 메시지 의미와 일치하는가?
- [ ] 사용자 친화적 문구인가?
- [ ] 중요한 오류를 Toast만으로 처리하지 않는가?
- [ ] 복구 action이 필요한 경우 제공되는가?
```

---

### [FAQ]

Q. Alert는 언제 써?
A. 사용자가 계속 확인해야 하는 중요한 안내, 경고, 오류를 화면 안에 표시할 때 사용한다.

Q. Alert와 Toast는 뭐가 달라?
A. Alert는 화면 안에 유지되는 안내이고, Toast는 일시적인 작업 결과 알림이다.

Q. 중요한 오류를 Toast만으로 보여줘도 돼?
A. 권장하지 않는다. 화면 내 Error State나 Alert도 함께 제공하는 것이 좋다.

Q. Alert에 role alert가 항상 필요해?
A. 항상은 아니다. 동적으로 나타나는 중요한 메시지에는 고려할 수 있다.

---

## 6.2 Toast Component Rules

### [개념]

Toast는 사용자의 작업 결과를 일시적으로 알려주는 feedback component다.

Toast는 저장 완료, 삭제 완료, 복사 완료, 간단한 실패 같은 짧은 피드백에 적합하다.

---

### [핵심]

Toast 사용 대상:

- 저장 완료
- 삭제 완료
- 복사 완료
- 로그인 성공
- 리뷰 등록 완료
- 가벼운 오류
- 일시적 안내

Toast Variant:

```text
info
success
warning
error
```

Toast 기준:

- 짧은 메시지 사용
- 일정 시간 후 사라짐
- 중요한 정보는 Toast만 사용 금지
- 여러 Toast stacking 기준 정의
- 닫기 버튼 제공 고려
- screen reader 전달 고려
- 과도한 Toast 남발 금지

---

### [실무]

Toast 예:

```jsx
showToast({
  variant: "success",
  message: "저장되었습니다.",
});
```

Error Toast 예:

```jsx
showToast({
  variant: "error",
  message: "저장하지 못했습니다. 다시 시도해 주세요.",
});
```

Toast 사용 기준:

```text
가벼운 성공
→ Toast

중요한 오류
→ Alert 또는 Error State + Toast 선택

폼 검증 오류
→ Field Error 우선

페이지 로드 실패
→ Error State 우선
```

---

### [FAQ]

Q. Toast는 언제 써?
A. 저장 완료, 삭제 완료, 복사 완료처럼 일시적인 작업 결과를 알려줄 때 사용한다.

Q. 모든 성공에 Toast를 띄워도 돼?
A. 과하면 방해가 될 수 있다. 중요한 행동 중심으로 사용한다.

Q. 중요한 오류를 Toast만으로 처리해도 돼?
A. 권장하지 않는다. 사용자가 놓칠 수 있으므로 화면 내 Error State가 필요하다.

Q. Toast 문구는 길어도 돼?
A. 짧고 명확해야 한다. 긴 설명은 Alert나 Error State가 적합하다.

---

## 6.3 Alert Toast Usage Rules

### [개념]

Alert Toast Usage Rules는 Alert와 Toast를 상황에 맞게 구분해 사용하는 기준이다.

Alert와 Toast는 모두 feedback component지만 지속성, 중요도, 사용 맥락이 다르다.

---

### [핵심]

구분 기준:

| 상황             | 권장 컴포넌트          |
| ---------------- | ---------------------- |
| 페이지 로드 실패 | Error State 또는 Alert |
| 폼 필드 오류     | Field Error            |
| 저장 성공        | Toast                  |
| 삭제 성공        | Toast                  |
| 권한 없음        | Alert 또는 Error State |
| 로그인 필요      | Alert 또는 Modal       |
| 네트워크 오류    | Error State + 재시도   |
| 단순 복사 완료   | Toast                  |

핵심 기준:

```text
사용자가 계속 확인해야 함
→ Alert

잠깐 알려주면 충분함
→ Toast

사용자 조치가 필요함
→ Alert / Error State

작업 성공 확인
→ Toast
```

---

### [실무]

좋은 예:

```jsx
<ErrorState
  title="데이터를 불러오지 못했습니다"
  description="네트워크 상태를 확인한 뒤 다시 시도해 주세요."
  action={<Button onClick={refetch}>다시 시도</Button>}
/>
```

```jsx
showToast({
  variant: "success",
  message: "저장되었습니다.",
});
```

나쁜 예:

```jsx
showToast({
  variant: "error",
  message: "권한이 없어 이 페이지를 사용할 수 없습니다.",
});
```

위 경우는 Toast보다 화면 내 Alert 또는 Error State가 적합하다.

---

### [FAQ]

Q. Alert와 Toast를 구분하는 기준은?
A. 계속 확인해야 하는 정보는 Alert, 일시적인 작업 결과는 Toast가 적합하다.

Q. 폼 오류는 Toast로 보여줘도 돼?
A. 권장하지 않는다. 입력 필드 가까이에 Field Error로 보여주는 것이 우선이다.

Q. 저장 성공은 Alert가 좋아?
A. 대부분 Toast가 적합하다. 중요한 완료 화면이 필요하면 Success State를 사용할 수 있다.

Q. 권한 오류는 Toast로 충분해?
A. 대부분 충분하지 않다. 화면 내 Alert 또는 Error State로 안내하는 것이 좋다.

---

## 6.4 Alert Toast Do and Don't

### [개념]

Alert Toast Do and Don't는 feedback component의 올바른 사용과 잘못된 사용을 구분하는 기준이다.

---

### [핵심]

Do:

- Alert는 중요한 안내를 화면 문맥 안에 표시한다.
- Toast는 일시적인 작업 결과에 사용한다.
- variant 의미와 메시지를 일치시킨다.
- 오류 메시지는 사용자 친화적으로 작성한다.
- 필요한 경우 복구 action을 제공한다.
- 중요한 정보는 화면에 남긴다.
- Toast stacking 기준을 정의한다.

Don't:

- 중요한 오류를 Toast만으로 처리하지 않는다.
- Toast를 과도하게 남발하지 않는다.
- 개발자용 raw error를 그대로 노출하지 않는다.
- 성공 / 실패 의미와 variant를 불일치시키지 않는다.
- 긴 설명을 Toast에 넣지 않는다.
- 색상만으로 상태를 전달하지 않는다.

---

### [실무]

좋은 예:

```jsx
<Alert variant="error" title="저장하지 못했습니다">
  입력 내용을 확인한 뒤 다시 시도해 주세요.
</Alert>
```

```jsx
showToast({
  variant: "success",
  message: "삭제되었습니다.",
});
```

나쁜 예:

```jsx
showToast({
  variant: "error",
  message: "500 Internal Server Error: SQL constraint violation",
});
```

Review Checklist:

```md
- [ ] Alert와 Toast 사용 맥락이 적절한가?
- [ ] 메시지가 사용자 친화적인가?
- [ ] 중요한 오류가 화면에 유지되는가?
- [ ] variant와 메시지 의미가 일치하는가?
- [ ] Toast가 과도하게 남발되지 않는가?
```

---

### [FAQ]

Q. Alert Toast에서 가장 흔한 실수는?
A. 중요한 오류를 Toast만으로 보여주거나 개발자용 raw error를 그대로 노출하는 것이다.

Q. Error Toast에 서버 에러를 그대로 넣어도 돼?
A. 권장하지 않는다. 사용자가 이해할 수 있는 문장으로 바꿔야 한다.

Q. Toast가 여러 개 쌓이면 어떻게 해?
A. stacking 위치, 최대 개수, 자동 닫힘 기준을 정의해야 한다.

Q. 성공 메시지는 어떤 문구가 좋아?
A. 저장되었습니다, 삭제되었습니다, 등록되었습니다처럼 짧고 명확한 문구가 좋다.

---

# 7. Modal Dialog Component

## 7.1 Modal Dialog Definition

### [개념]

Modal / Dialog는 사용자의 주의를 현재 작업에 집중시키기 위해 화면 위에 표시하는 component다.

Modal은 확인, 입력, 상세 보기, 경고, 삭제 확인, 로그인 유도, 리뷰 작성 같은 맥락에서 사용한다.

---

### [핵심]

Modal 사용 대상:

- 확인
- 입력
- 상세 보기
- 경고
- 삭제 확인
- 로그인 유도
- 리뷰 작성
- 권한 요청
- 설정 변경

Modal 필수 상태:

- open
- closed
- loading
- error

Modal 필수 접근성:

- dialog role
- aria-modal
- title 연결
- 닫기 버튼
- ESC 닫기 정책
- overlay click 닫기 정책
- focus trap
- focus restore
- background scroll lock

---

### [실무]

Modal 예:

```jsx
<Modal isOpen={isOpen} title="리뷰 작성" onClose={closeModal}>
  <ReviewForm />
</Modal>
```

접근성 구조:

```jsx
<div role="dialog" aria-modal="true" aria-labelledby="modal-title">
  <h2 id="modal-title">리뷰 작성</h2>
  <button type="button" onClick={onClose}>
    닫기
  </button>
</div>
```

Review 기준:

```md
- [ ] modal title이 있는가?
- [ ] 닫기 버튼이 있는가?
- [ ] role dialog와 aria-modal이 있는가?
- [ ] focus 관리가 있는가?
- [ ] 배경 스크롤 방지가 있는가?
```

---

### [FAQ]

Q. Modal은 언제 써?
A. 사용자의 주의를 현재 작업에 집중시켜야 하는 확인, 입력, 경고, 상세 보기 상황에 사용한다.

Q. Modal에는 꼭 닫기 버튼이 필요해?
A. 필요하다. 사용자가 명확하게 닫을 수 있어야 한다.

Q. Modal 접근성에서 가장 중요한 것은?
A. dialog 역할, title 연결, focus 관리, keyboard 조작이다.

Q. Modal과 Dialog는 같은 거야?
A. Dialog는 대화형 창의 의미이고, Modal은 배경 상호작용을 막는 dialog 패턴으로 볼 수 있다.

---

## 7.2 Modal State and Action Rules

### [개념]

Modal State and Action Rules는 Modal 내부의 open, close, loading, error 상태와 action button 배치 기준이다.

---

### [핵심]

Modal 상태:

```text
open
→ 화면 위 표시
→ focus 이동
→ 배경 스크롤 잠금

closed
→ 화면에서 제거
→ 이전 focus 복원

loading
→ 제출 / 처리 중
→ action 중복 방지

error
→ modal 내부 오류 표시
→ 복구 가능 안내
```

Action 기준:

- Primary Action은 오른쪽 또는 주요 위치
- Secondary Action은 취소 / 닫기
- Danger Action은 삭제 / 위험 확인
- Loading 중 action disabled
- 닫기와 제출 구분
- 중요한 입력 중 overlay click 닫기 주의

---

### [실무]

삭제 확인 Modal 예:

```jsx
<Modal isOpen={isOpen} title="삭제 확인" onClose={closeModal}>
  <p>삭제한 데이터는 복구할 수 없습니다.</p>
  <ModalFooter>
    <Button variant="secondary" onClick={closeModal}>
      취소
    </Button>
    <Button variant="danger" isLoading={isDeleting} onClick={handleDelete}>
      삭제
    </Button>
  </ModalFooter>
</Modal>
```

Modal Error 예:

```jsx
<Alert variant="error" title="삭제하지 못했습니다">
  잠시 후 다시 시도해 주세요.
</Alert>
```

Review 기준:

```md
- [ ] primary / secondary / danger action이 명확한가?
- [ ] loading 중 중복 제출이 방지되는가?
- [ ] error state가 modal 내부에 표시되는가?
- [ ] 위험 행동이 danger variant로 표현되는가?
```

---

### [FAQ]

Q. Modal action은 어떻게 배치해?
A. 주요 행동과 취소 행동을 명확히 구분하고, 위험 행동은 danger variant로 표시한다.

Q. 삭제 확인 Modal에는 어떤 버튼이 필요해?
A. 취소 버튼과 danger 삭제 버튼이 필요하다.

Q. Modal loading 중에는 어떻게 해?
A. 제출 버튼을 loading / disabled 처리해 중복 요청을 막는다.

Q. Modal 내부 오류는 Toast로만 보여줘도 돼?
A. 권장하지 않는다. Modal 내부 Alert나 Error Message로 문맥 안에 표시하는 것이 좋다.

---

## 7.3 Modal Focus and Keyboard Rules

### [개념]

Modal Focus and Keyboard Rules는 Modal이 열렸을 때 keyboard focus와 닫기 동작을 관리하는 기준이다.

Modal은 화면 흐름을 강제로 바꾸므로 focus 관리가 중요하다.

---

### [핵심]

Modal Focus 기준:

```text
Open
→ 첫 번째 focusable element 또는 modal container로 focus 이동

During Open
→ focus trap 적용

ESC
→ 닫기 정책에 따라 close

Close
→ trigger element로 focus 복원
```

Keyboard 기준:

- Tab은 Modal 내부에서 순환
- Shift + Tab도 Modal 내부에서 순환
- ESC 닫기 정책 명확화
- 닫기 버튼 keyboard 접근 가능
- overlay click 닫기 정책 명확화
- background 요소 focus 방지

---

### [실무]

Modal focus flow:

```text
Button click
→ Modal open
→ Focus moves to close button or title
→ Tab cycles inside modal
→ ESC or close button
→ Modal close
→ Focus returns to trigger button
```

Review Checklist:

```md
- [ ] Modal open 시 focus가 이동하는가?
- [ ] Modal 내부 focus trap이 있는가?
- [ ] ESC 닫기 정책이 있는가?
- [ ] 닫힌 후 이전 focus가 복원되는가?
- [ ] 배경 요소에 focus가 가지 않는가?
```

---

### [FAQ]

Q. Modal focus trap이 뭐야?
A. Modal이 열린 동안 keyboard focus가 Modal 내부에서만 이동하도록 제한하는 것이다.

Q. Modal 닫힌 후 focus는 어디로 가야 해?
A. Modal을 열었던 trigger element로 돌아가는 것이 좋다.

Q. ESC로 Modal을 닫아야 해?
A. 일반적으로 권장된다. 다만 중요한 작업 중이면 정책을 명확히 정해야 한다.

Q. overlay click으로 닫히게 해야 해?
A. 상황에 따라 다르다. 중요한 입력 중이면 실수로 닫히지 않도록 막을 수 있다.

---

## 7.4 Modal Dialog Do and Don't

### [개념]

Modal Dialog Do and Don't는 Modal / Dialog의 올바른 사용과 잘못된 사용을 구분하는 기준이다.

---

### [핵심]

Do:

- title을 제공한다.
- 닫기 버튼을 제공한다.
- role dialog와 aria-modal을 적용한다.
- focus trap을 고려한다.
- 닫힌 후 focus를 복원한다.
- 배경 스크롤을 방지한다.
- loading / error 상태를 제공한다.
- 위험 행동은 danger variant로 표시한다.

Don't:

- 닫을 방법 없는 Modal을 만들지 않는다.
- title 없는 Modal을 만들지 않는다.
- focus 관리를 누락하지 않는다.
- 중요한 입력 중 overlay click으로 실수 닫힘을 만들지 않는다.
- Modal을 단순 안내 Toast 대체로 남발하지 않는다.
- Modal 안에 너무 많은 정보를 넣지 않는다.

---

### [실무]

좋은 예:

```jsx
<Modal isOpen={isOpen} title="권한 변경" onClose={closeModal}>
  <p>선택한 사용자의 권한을 변경합니다.</p>
  <Button variant="primary">저장</Button>
</Modal>
```

나쁜 예:

```jsx
<div className="modal">
  <p>삭제?</p>
  <button>OK</button>
</div>
```

Review Checklist:

```md
- [ ] title이 있는가?
- [ ] 닫기 방법이 있는가?
- [ ] keyboard 접근성이 있는가?
- [ ] focus 관리가 있는가?
- [ ] modal 사용이 과도하지 않은가?
```

---

### [FAQ]

Q. Modal에서 가장 흔한 실수는?
A. title, 닫기 버튼, focus 관리, keyboard 접근성을 누락하는 것이다.

Q. Modal을 자주 띄우면 좋아?
A. 아니다. 사용 흐름을 끊기 때문에 필요한 상황에만 사용해야 한다.

Q. Modal 안에 긴 내용을 넣어도 돼?
A. 가능하지만 과하면 사용성이 떨어진다. 긴 내용은 별도 페이지나 Drawer를 고려한다.

Q. 삭제 Modal에서 OK 버튼만 있어도 돼?
A. 권장하지 않는다. 취소와 삭제 행동을 명확히 구분해야 한다.

---

# 8. Tabs Pagination Table Component

## 8.1 Tabs Component Rules

### [개념]

Tabs는 같은 맥락의 여러 콘텐츠를 탭으로 전환해 보여주는 component다.

Tabs는 관련 있는 콘텐츠 그룹을 한 화면 안에서 전환할 때 사용한다.

---

### [핵심]

Tabs Anatomy:

```text
Tab List
→ Tab
→ Tab Panel
```

Tabs State:

- default
- hover
- focus
- selected
- disabled

Tabs 기준:

- 선택된 tab이 명확해야 한다.
- tab과 panel 연결이 명확해야 한다.
- keyboard 이동을 고려한다.
- URL 상태 필요성을 검토한다.
- 너무 많은 tab은 피한다.
- 관련 없는 콘텐츠를 tabs로 묶지 않는다.

---

### [실무]

Tabs 예:

```jsx
<Tabs defaultValue="info">
  <TabList>
    <Tab value="info">기본 정보</Tab>
    <Tab value="history">이력</Tab>
  </TabList>

  <TabPanel value="info">기본 정보 내용</TabPanel>
  <TabPanel value="history">이력 내용</TabPanel>
</Tabs>
```

접근성 예:

```jsx
<button role="tab" aria-selected={isSelected} aria-controls="panel-info">
  기본 정보
</button>
<div role="tabpanel" id="panel-info">
  기본 정보 내용
</div>
```

Review 기준:

```md
- [ ] 선택된 tab이 명확한가?
- [ ] tab과 panel 관계가 명확한가?
- [ ] keyboard 이동을 고려했는가?
- [ ] 너무 많은 tab을 만들지 않았는가?
```

---

### [FAQ]

Q. Tabs는 언제 써?
A. 같은 페이지 안에서 관련 있는 콘텐츠 묶음을 전환할 때 사용한다.

Q. Tab 상태를 URL에 넣어야 해?
A. 공유, 새로고침 유지, 뒤로가기 지원이 필요하면 URL query나 path로 관리할 수 있다.

Q. Tabs가 너무 많으면 어떻게 해?
A. 정보 구조를 다시 나누거나 페이지 분리, accordion, navigation을 고려한다.

Q. Tabs 접근성에서 중요한 것은?
A. tablist, tab, tabpanel 관계와 selected 상태, keyboard 조작이다.

---

## 8.2 Pagination Component Rules

### [개념]

Pagination은 많은 데이터를 여러 페이지로 나누어 탐색하는 component다.

Pagination은 검색 결과, 관리자 목록, 테이블 데이터처럼 위치와 페이지 공유가 중요한 데이터에 적합하다.

---

### [핵심]

Pagination Anatomy:

```text
Previous
Page Numbers
Next
Current Page
Total Page
```

Pagination State:

- default
- current
- disabled
- hover
- focus
- loading

Pagination 기준:

- 현재 페이지가 명확해야 한다.
- 첫 페이지에서 이전 버튼은 disabled 처리한다.
- 마지막 페이지에서 다음 버튼은 disabled 처리한다.
- 페이지 변경 시 loading 상태를 고려한다.
- URL query 연동을 고려한다.
- aria-current 사용을 고려한다.

---

### [실무]

Pagination 예:

```jsx
<Pagination currentPage={page} totalPages={totalPages} onPageChange={setPage} />
```

현재 페이지 접근성 예:

```jsx
<button aria-current={page === currentPage ? "page" : undefined}>{page}</button>
```

URL query 예:

```text
/members?page=2&size=20
```

Review 기준:

```md
- [ ] 현재 페이지가 명확한가?
- [ ] 이전 / 다음 disabled 상태가 올바른가?
- [ ] 페이지 변경 시 loading 상태가 있는가?
- [ ] URL query 연동이 필요한지 검토했는가?
```

---

### [FAQ]

Q. Pagination은 언제 써?
A. 검색 결과나 관리자 목록처럼 페이지 위치와 공유가 중요한 데이터에 사용한다.

Q. Pagination과 Infinite Scroll 중 뭐가 좋아?
A. 검색 결과처럼 위치와 페이지 공유가 중요하면 Pagination, 피드처럼 계속 탐색하는 UX는 Infinite Scroll이 적합하다.

Q. 현재 페이지는 어떻게 표시해?
A. 시각적으로 강조하고 `aria-current="page"` 사용을 고려한다.

Q. 현재 페이지는 URL에 넣는 게 좋아?
A. 새로고침 유지와 공유가 필요하면 URL query에 넣는 것이 좋다.

---

## 8.3 Table Component Rules

### [개념]

Table은 행과 열 구조의 데이터를 표시하는 component다.

Table은 관리자 목록, 통계, 결제 내역, 사용자 목록, 생산 이력, 설비 알람 이력처럼 구조화된 데이터에 사용한다.

---

### [핵심]

Table 사용 대상:

- 관리자 목록
- 사용자 목록
- 결제 내역
- 통계
- 검색 결과
- 생산 이력
- LOT 이력
- 설비 알람 이력
- 불량 이력

Table 기준:

- 표 데이터에는 table 사용
- 레이아웃 용도로 table 사용 금지
- th와 scope 사용
- caption 필요성 검토
- 정렬 가능 컬럼은 상태 표시
- 빈 데이터 상태 제공
- loading 상태 제공
- 모바일 overflow 또는 카드 변환 기준 정의

---

### [실무]

Table 예:

```jsx
<table>
  <thead>
    <tr>
      <th scope="col">LOT 번호</th>
      <th scope="col">품목</th>
      <th scope="col">상태</th>
      <th scope="col">완료 수량</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>LOT-001</td>
      <td>EV Relay</td>
      <td>진행중</td>
      <td>120EA</td>
    </tr>
  </tbody>
</table>
```

모바일 처리 기준:

```text
방법 1
→ 가로 스크롤

방법 2
→ 카드형 변환

방법 3
→ 주요 컬럼만 표시

방법 4
→ 상세 페이지 분리
```

---

### [FAQ]

Q. Table은 언제 써?
A. 행과 열 구조의 데이터를 표시할 때 사용한다.

Q. 레이아웃을 만들려고 table을 써도 돼?
A. 안 된다. table은 표 데이터에 사용하고 레이아웃은 CSS Grid / Flexbox를 사용한다.

Q. 모바일에서 table은 어떻게 처리해?
A. 가로 스크롤, 카드형 변환, 주요 컬럼만 표시 등 프로젝트 기준을 정해야 한다.

Q. Table에 Empty State가 필요해?
A. 필요하다. 데이터가 없을 때 빈 화면만 보여주면 사용자가 상태를 이해하기 어렵다.

---

## 8.4 Tabs Pagination Table Do and Don't

### [개념]

Tabs, Pagination, Table Do and Don't는 데이터 탐색과 구조화된 콘텐츠 컴포넌트의 올바른 사용과 잘못된 사용을 구분하는 기준이다.

---

### [핵심]

Do:

- 관련 콘텐츠 전환에 Tabs 사용
- 현재 tab / page 상태 명확화
- 검색 결과와 관리자 목록에 Pagination 사용
- 표 데이터에는 Table 사용
- Table에는 th / scope 사용
- Loading / Empty State 제공
- 모바일 대응 기준 정의
- URL 상태 연동 필요성 검토

Don't:

- 관련 없는 콘텐츠를 Tabs로 묶지 않는다.
- 너무 많은 Tabs를 만들지 않는다.
- Pagination current 상태를 누락하지 않는다.
- 표 데이터를 div만으로 만들지 않는다.
- 레이아웃 용도로 table을 사용하지 않는다.
- 모바일 table 깨짐을 방치하지 않는다.
- Empty State 없이 빈 tbody만 표시하지 않는다.

---

### [실무]

좋은 예:

```text
관리자 사용자 목록
→ Table + Pagination + Empty State

상세 화면의 기본정보 / 이력
→ Tabs

검색 결과
→ Pagination + URL query
```

나쁜 예:

```text
행 / 열 데이터
→ div grid로만 구성

관련 없는 페이지들
→ Tabs로 강제 묶음

모바일 table
→ 화면 밖으로 깨짐
```

Review Checklist:

```md
- [ ] 컴포넌트 선택이 데이터 구조와 맞는가?
- [ ] 현재 상태가 명확한가?
- [ ] 접근성 속성이 필요한 곳에 적용되어 있는가?
- [ ] Loading / Empty 상태가 있는가?
- [ ] 모바일 대응 기준이 있는가?
```

---

### [FAQ]

Q. Tabs Pagination Table에서 가장 흔한 실수는?
A. 현재 상태 표시를 누락하거나 Table 모바일 대응과 Empty State를 빠뜨리는 것이다.

Q. Table 대신 div grid를 써도 돼?
A. 표 데이터라면 table이 적합하다. div grid는 레이아웃에 사용한다.

Q. Pagination 없이 전체 데이터를 한 번에 보여줘도 돼?
A. 데이터가 적으면 가능하지만 많아질 수 있는 목록은 Pagination을 고려해야 한다.

Q. Tabs에 URL 연동은 항상 필요해?
A. 항상은 아니다. 공유, 새로고침 유지, 뒤로가기 지원이 필요하면 고려한다.

---

# 9. Core Component Review Rules

## 9.1 Frontend Agent Core Component Rules

### [개념]

Frontend Agent Core Component Rules는 Frontend Agent가 화면을 만들 때 Core Component를 선택하고 사용하는 기준이다.

Frontend Agent는 공통 컴포넌트가 정의되어 있으면 직접 스타일을 새로 만들기보다 Core Component를 우선 사용해야 한다.

---

### [핵심]

Frontend Agent 기준:

- Button / Input / Card / Modal 우선 검색
- Component Specification 확인
- props API 준수
- variant / size 허용 값 준수
- loading / disabled / error 상태 포함
- Design Token 사용
- 접근성 기본 반영
- 모바일 대응 고려
- 새 컴포넌트 생성 시 목적 명시

---

### [실무]

Frontend Agent Flow:

```text
UI Requirement 분석
→ 필요한 Core Component 식별
→ Component Spec 확인
→ props / variant / size / state 선택
→ token 기반 style 적용
→ accessibility 확인
→ responsive 확인
→ output 생성
```

생성 전 체크:

```md
- [ ] 기존 Button으로 해결 가능한가?
- [ ] 기존 Input / Form Field로 해결 가능한가?
- [ ] 기존 Card / Table로 데이터 표현 가능한가?
- [ ] Modal이 필요한 상황인가?
- [ ] Alert와 Toast 중 무엇이 적절한가?
```

---

### [FAQ]

Q. Frontend Agent는 Core Component를 어떻게 사용해?
A. 요구사항에 맞는 기존 Core Component를 먼저 찾고, Spec에 맞는 props, variant, size, state를 적용한다.

Q. Core Component가 있는데 직접 만들면 안 돼?
A. 공통 UI라면 재사용하는 것이 좋다. 직접 구현은 예외 사유가 필요하다.

Q. Frontend Agent가 새 컴포넌트를 만들 수 있어?
A. 가능하지만 기존 컴포넌트로 해결 불가능한 이유와 새 컴포넌트 목적이 명확해야 한다.

Q. Core Component 사용 전 확인할 것은?
A. Component Spec, Design Token, variant, size, state, accessibility 기준이다.

---

## 9.2 Review Agent Core Component Checklist

### [개념]

Review Agent Core Component Checklist는 구현된 UI가 Core Component 기준을 따르는지 검토하는 기준이다.

Review Agent는 기능 동작뿐 아니라 UI 재사용성, 일관성, 접근성, 상태 처리를 함께 확인한다.

---

### [핵심]

Review Checklist:

```md
## Component Selection

- [ ] 적절한 Core Component를 선택했는가?
- [ ] Button과 Link를 혼동하지 않았는가?
- [ ] Badge와 Button을 혼동하지 않았는가?
- [ ] Table과 layout div를 혼동하지 않았는가?

## API

- [ ] props API를 준수하는가?
- [ ] variant / size 허용 값을 준수하는가?
- [ ] required props가 누락되지 않았는가?

## State

- [ ] loading 상태가 필요한 곳에 있는가?
- [ ] disabled 상태가 필요한 곳에 있는가?
- [ ] error 상태가 메시지와 함께 있는가?
- [ ] empty 상태가 필요한 곳에 있는가?
- [ ] selected / checked / current 상태가 명확한가?

## Accessibility

- [ ] label 연결이 있는가?
- [ ] focus-visible이 있는가?
- [ ] keyboard 조작이 가능한가?
- [ ] icon button accessible name이 있는가?
- [ ] modal focus 관리가 있는가?

## Token

- [ ] Design Token을 사용하는가?
- [ ] raw color / spacing이 남발되지 않는가?
- [ ] variant와 token이 연결되어 있는가?
```

---

### [실무]

Review Decision:

```text
Approved
→ Core Component 기준 충족

Needs Fix
→ 일부 상태 / token / usage 기준 미흡

Blocked
→ 컴포넌트 선택 오류, 접근성 심각 문제, 주요 상태 누락
```

Blocked 예:

```text
Button으로 페이지 이동 처리
Input label 없음
Icon Button aria-label 없음
Modal 닫기 불가
Table 모바일 깨짐
중요한 Error를 Toast만으로 표시
loading 중 중복 제출 가능
```

---

### [FAQ]

Q. Review Agent는 Core Component에서 뭘 봐야 해?
A. 컴포넌트 선택, props API, variant, size, state, accessibility, token 사용을 확인해야 한다.

Q. 어떤 경우 Blocked야?
A. 사용자 조작이 어렵거나 접근성 심각 문제, 주요 상태 누락, 컴포넌트 선택 오류가 있으면 Blocked다.

Q. Core Component를 안 쓰면 무조건 반려야?
A. 공통 UI가 이미 있는데도 직접 구현했다면 반려될 수 있다. 예외 사유가 필요하다.

Q. Review Agent가 가장 먼저 보는 것은?
A. 컴포넌트 선택이 요구사항과 맞는지, 주요 상태와 접근성이 누락되지 않았는지다.

---

## 9.3 Core Component Common Mistakes

### [개념]

Core Component Common Mistakes는 공통 컴포넌트를 사용할 때 자주 발생하는 실수다.

이 실수들은 UI 일관성, 접근성, 유지보수성을 떨어뜨린다.

---

### [핵심]

자주 발생하는 실수:

- Button과 Link 혼동
- Button 기본 type을 submit으로 둠
- loading 중 중복 클릭 가능
- danger 행동을 primary로 표시
- placeholder를 label 대체로 사용
- Input error와 message 연결 누락
- Checkbox / Radio label 누락
- Badge를 Button처럼 사용
- Tag와 Badge 의미 혼동
- Alert와 Toast 구분 실패
- 중요한 오류를 Toast만으로 표시
- Modal title / close / focus 관리 누락
- Table을 레이아웃 용도로 사용
- Table Empty State 누락
- 모바일 Table 대응 없음
- raw color / spacing 직접 사용
- Core Component 대신 화면별 div 남발

---

### [실무]

Troubleshooting:

```text
버튼 의미가 모호함
→ Button variant / text 확인

입력 접근성이 낮음
→ Form Field / label / aria-describedby 확인

상태 메시지가 사라짐
→ Alert vs Toast 구분 확인

Modal 사용성이 낮음
→ title / close / focus trap 확인

목록 데이터가 이해 안 됨
→ Table header / Empty State 확인

UI가 화면마다 다름
→ Core Component 재사용 여부 확인
```

Review Checklist:

```md
- [ ] Core Component 선택 오류가 없는가?
- [ ] 접근성 필수 기준이 누락되지 않았는가?
- [ ] 주요 상태 처리가 있는가?
- [ ] token 사용 기준을 따르는가?
- [ ] 컴포넌트 의미가 혼동되지 않는가?
```

---

### [FAQ]

Q. Core Component에서 가장 흔한 실수는?
A. Button과 Link를 혼동하고, Input label과 error 연결을 누락하고, Modal focus 관리를 빼먹는 것이다.

Q. Badge를 클릭 가능하게 만들어도 돼?
A. 상태 표시 목적이면 권장하지 않는다. 클릭 가능한 필터라면 Tag 또는 Button 역할을 명확히 해야 한다.

Q. 중요한 오류를 Toast만으로 보여주면 왜 문제야?
A. Toast는 사라질 수 있어 사용자가 오류와 복구 방법을 놓칠 수 있다.

Q. Core Component 대신 div를 많이 쓰면 왜 문제야?
A. UI 일관성, 접근성, 상태 처리, 유지보수 기준이 깨지기 쉽다.

---

# 10. Final Checklist

## 10.1 Part04 Quality Checklist

### [개념]

Part04 Quality Checklist는 Core Component Rules 문서가 Agent 기준 문서로 사용 가능한지 확인하는 검수 기준이다.

---

### [핵심]

최종 체크 항목:

```md
## Core

- [ ] Core Component 정의가 명확한가?
- [ ] Component Selection Rules가 있는가?
- [ ] Button / Input / Form Field 기준이 있는가?
- [ ] Select / Checkbox / Radio 기준이 있는가?
- [ ] Card / Badge / Tag 기준이 있는가?
- [ ] Alert / Toast 기준이 있는가?
- [ ] Modal / Dialog 기준이 있는가?
- [ ] Tabs / Pagination / Table 기준이 있는가?

## Component Spec

- [ ] 각 컴포넌트 목적이 명확한가?
- [ ] variant 기준이 있는가?
- [ ] state 기준이 있는가?
- [ ] accessibility 기준이 있는가?
- [ ] usage 기준이 있는가?
- [ ] Do / Don't가 있는가?

## Agent Usage

- [ ] Frontend Agent 사용 기준이 있는가?
- [ ] Review Agent 검토 기준이 있는가?
- [ ] Approved / Needs Fix / Blocked 기준이 있는가?
- [ ] Common Mistakes가 포함되어 있는가?

## Retrieval

- [ ] FAQ가 충분한가?
- [ ] 컴포넌트별 검색 query가 포함되어 있는가?
- [ ] Button / Input / Modal / Table 같은 핵심 키워드가 반복 포함되어 있는가?
```

---

### [실무]

Part04는 Part03 Component Specification Rules를 실제 Core Component에 적용한 문서다.

Part 연계:

```text
Part01 Design System Core
→ Part02 Design Token Rules
→ Part03 Component Specification Rules
→ Part04 Core Component Rules
→ Part05 Feedback State Pattern Rules
→ Part06 Layout Responsive Theme Rules
→ Part07 Accessibility Documentation Review Rules
```

Part04 기준은 Frontend Agent가 실제 화면을 생성할 때 가장 자주 참조하는 Component Rules다.

---

### [FAQ]

Q. Part04의 역할은 뭐야?
A. Button, Input, Card, Modal, Table 같은 Core Component의 사용 기준과 검토 기준을 정의하는 문서다.

Q. Part04는 Part03과 어떻게 연결돼?
A. Part03의 Component Specification 구조를 사용해 실제 Core Component별 규칙을 정의한다.

Q. Part04에서 가장 중요한 컴포넌트는 뭐야?
A. Button, Input, Form Field, Card, Modal, Alert, Toast, Table이 우선이다.

Q. Part04 최종 승인 기준은 뭐야?
A. Frontend Agent가 Core Component를 선택하고 Review Agent가 검토할 수 있을 만큼 usage, state, accessibility 기준이 명확해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Core Component가 뭐야?
A. Design System에서 가장 자주 재사용되는 Button, Input, Card, Modal 같은 기본 UI 컴포넌트다.

Q. Core Component는 왜 필요해?
A. 화면마다 UI를 새로 만들지 않고 일관된 컴포넌트 기준으로 재사용하기 위해 필요하다.

Q. Button과 Link는 어떻게 구분해?
A. 저장, 삭제, 검색 같은 행동 실행은 Button이고, 페이지 이동은 Link다.

Q. Badge와 Button은 어떻게 구분해?
A. Badge는 상태나 수량 표시이고, Button은 사용자의 행동 실행이다.

Q. Alert와 Toast는 어떻게 구분해?
A. Alert는 화면 안에 유지되는 중요한 안내이고, Toast는 일시적인 작업 결과 알림이다.

Q. Button은 언제 써?
A. 저장, 등록, 삭제, 검색, 다시 시도처럼 사용자의 행동을 실행할 때 사용한다.

Q. Button 기본 type은 뭐가 좋아?
A. 일반 Button 컴포넌트는 `button`을 기본값으로 두는 것이 안전하다.

Q. form submit 버튼은 어떻게 해?
A. 명시적으로 `type="submit"`을 사용한다.

Q. Button primary는 언제 써?
A. 화면에서 가장 중요한 주요 행동에 사용한다. 예: 저장, 등록, 검색.

Q. Button danger는 언제 써?
A. 삭제, 탈퇴, 되돌릴 수 없는 위험 행동에 사용한다.

Q. Button loading은 왜 필요해?
A. 처리 중임을 알리고 중복 클릭과 중복 API 요청을 막기 위해 필요하다.

Q. Button 텍스트는 어떻게 써야 해?
A. 저장, 삭제, 검색, 다시 시도처럼 사용자가 수행할 행동을 동사 중심으로 작성한다.

Q. Input은 언제 써?
A. 사용자의 텍스트, 이메일, 비밀번호, 숫자, 검색어 같은 값을 입력받을 때 사용한다.

Q. placeholder만 있으면 label은 없어도 돼?
A. 권장하지 않는다. placeholder는 입력 예시이고 label은 입력 항목의 이름이다.

Q. disabled와 readonly는 뭐가 달라?
A. disabled는 조작과 제출에서 제외되고, readonly는 수정은 불가하지만 값은 읽을 수 있다.

Q. Input error는 어떻게 표시해야 해?
A. border 색상, error message, aria-invalid, aria-describedby를 함께 사용한다.

Q. Form Field가 뭐야?
A. label, input, helper text, error message를 하나의 구조로 묶는 component다.

Q. Form Field를 따로 만들면 좋아?
A. 반복되는 입력 구조를 일관되게 유지할 수 있어 좋다.

Q. Select는 언제 써?
A. 옵션이 많고 하나를 선택해야 할 때 사용한다.

Q. Radio와 Select 중 뭐를 써야 해?
A. 옵션이 적고 비교가 필요하면 Radio, 옵션이 많으면 Select가 적합하다.

Q. Checkbox는 언제 써?
A. 여러 개 선택하거나 약관 동의 같은 선택 상태를 표시할 때 사용한다.

Q. Checkbox와 Switch는 뭐가 달라?
A. Checkbox는 선택이나 동의에 적합하고, Switch는 즉시 적용되는 on / off 설정에 적합하다.

Q. Radio는 언제 써?
A. 옵션이 적고 여러 선택지 중 하나만 선택해야 할 때 사용한다.

Q. Card는 언제 써?
A. 관련 정보를 하나의 시각적 그룹으로 묶어 보여줄 때 사용한다.

Q. Card 전체를 클릭 가능하게 해도 돼?
A. 가능하지만 내부 버튼과 충돌하지 않게 하고 접근성을 고려해야 한다.

Q. Badge는 언제 써?
A. 상태, 수량, 알림 개수처럼 짧은 정보를 표시할 때 사용한다.

Q. Badge와 Tag는 뭐가 달라?
A. Badge는 상태나 수량 표시이고, Tag는 카테고리나 키워드 표시다.

Q. 상태 Badge는 색상만 있으면 돼?
A. 안 된다. 텍스트도 함께 제공해야 한다.

Q. Tag는 언제 써?
A. 카테고리, 키워드, 필터, 속성 같은 분류 정보를 표시할 때 사용한다.

Q. Alert는 언제 써?
A. 사용자가 계속 확인해야 하는 중요한 안내, 경고, 오류를 화면 안에 표시할 때 사용한다.

Q. Toast는 언제 써?
A. 저장 완료, 삭제 완료, 복사 완료처럼 일시적인 작업 결과를 알려줄 때 사용한다.

Q. 중요한 오류를 Toast만으로 보여줘도 돼?
A. 권장하지 않는다. 화면 내 Error State나 Alert도 함께 제공하는 것이 좋다.

Q. Modal은 언제 써?
A. 사용자의 주의를 현재 작업에 집중시켜야 하는 확인, 입력, 경고, 상세 보기 상황에 사용한다.

Q. Modal에는 꼭 닫기 버튼이 필요해?
A. 필요하다. 사용자가 명확하게 닫을 수 있어야 한다.

Q. Modal 접근성에서 가장 중요한 것은?
A. dialog 역할, title 연결, focus 관리, keyboard 조작이다.

Q. Modal focus trap이 뭐야?
A. Modal이 열린 동안 keyboard focus가 Modal 내부에서만 이동하도록 제한하는 것이다.

Q. Tabs는 언제 써?
A. 같은 페이지 안에서 관련 있는 콘텐츠 묶음을 전환할 때 사용한다.

Q. Pagination은 언제 써?
A. 검색 결과나 관리자 목록처럼 페이지 위치와 공유가 중요한 데이터에 사용한다.

Q. Pagination과 Infinite Scroll 중 뭐가 좋아?
A. 검색 결과처럼 위치와 페이지 공유가 중요하면 Pagination, 피드처럼 계속 탐색하는 UX는 Infinite Scroll이 적합하다.

Q. Table은 언제 써?
A. 행과 열 구조의 데이터를 표시할 때 사용한다.

Q. 레이아웃을 만들려고 table을 써도 돼?
A. 안 된다. table은 표 데이터에 사용하고 레이아웃은 CSS Grid / Flexbox를 사용한다.

Q. 모바일에서 table은 어떻게 처리해?
A. 가로 스크롤, 카드형 변환, 주요 컬럼만 표시 등 프로젝트 기준을 정해야 한다.

Q. Frontend Agent는 Core Component를 어떻게 사용해?
A. 요구사항에 맞는 기존 Core Component를 먼저 찾고, Spec에 맞는 props, variant, size, state를 적용한다.

Q. Review Agent는 Core Component에서 뭘 봐야 해?
A. 컴포넌트 선택, props API, variant, size, state, accessibility, token 사용을 확인해야 한다.

Q. Core Component에서 가장 흔한 실수는?
A. Button과 Link를 혼동하고, Input label과 error 연결을 누락하고, Modal focus 관리를 빼먹는 것이다.

Q. Part04의 역할은 뭐야?
A. Button, Input, Card, Modal, Table 같은 Core Component의 사용 기준과 검토 기준을 정의하는 문서다.
