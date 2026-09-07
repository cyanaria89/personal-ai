# UI Component Pattern Part04 - Base UI Components

---

# 1. Base UI Component Overview

## 1.1 Base UI Component Purpose

### [개념]

Base UI Component는 여러 화면과 여러 Feature에서 반복 사용하는 가장 기본적인 공통 UI Component다.

Base UI Component는 Button, TextField, Modal, Card, Badge 같은 UI 단위를 의미한다.

Base UI Component는 도메인 데이터를 직접 알지 않고, 화면 표현, 사용자 이벤트 전달, 접근성, 시각 상태 표현을 담당한다.

---

### [핵심]

Base UI Component 핵심 기준:

- Common UI Component로 설계
- 도메인 의존 제거
- API 호출 직접 포함 금지
- Props API 명확화
- variant / size / state 기준 통일
- Event Handler Props 사용
- children / composition 지원
- 접근성 기본 포함
- Styling Boundary 분리
- Feature UI에서 조합 가능해야 함

Base UI Component 예:

- Button
- IconButton
- TextField
- Textarea
- Select
- Checkbox
- Radio
- Modal
- Dialog
- Card
- Badge
- Avatar
- Tooltip Basics

---

### [실무]

2026 실무 기준에서 Base UI Component는 디자인 시스템의 시작점이다.

Base UI Component는 처음부터 완전한 Design System을 목표로 만들기보다, 반복되는 UI와 안정적인 Props API를 중심으로 작게 시작한다.

설계 Flow:

```text
Identify Repeated UI
→ Define Component Responsibility
→ Design Props API
→ Add Variant / Size / State
→ Add Event Handler Props
→ Add Accessibility
→ Separate Styling Boundary
→ Review Reusability
```

Base UI Component와 Feature UI 관계:

```text
Base UI
→ Button, Card, Badge, Modal

Feature UI
→ FestivalCard, ReviewForm, NotificationItem

Page
→ API 호출, route state, server state
```

---

### [FAQ]

Q. Base UI Component는 뭐야?
A. Button, TextField, Modal, Card처럼 여러 화면에서 반복 사용되는 가장 기본적인 Common UI Component다.

Q. Base UI Component 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. Base UI Component는 UI 표현과 이벤트 전달만 담당하고 API 호출은 Feature Component나 Hook에서 처리한다.

Q. Base UI Component는 언제 만들어?
A. 여러 화면에서 반복되고 역할과 Props가 안정적일 때 공통 Component로 만든다.

---

# 2. Button Component Pattern

## 2.1 Button Component Responsibility

### [개념]

Button Component는 사용자의 클릭 액션을 실행하는 기본 UI Component다.

Button은 액션 UI를 제공하고, 실제 도메인 로직은 onClick 같은 Event Handler Props를 통해 외부로 위임한다.

---

### [핵심]

Button 기본 책임:

- 클릭 가능한 UI 제공
- type 지정
- variant 적용
- size 적용
- disabled 상태 표현
- loading 상태 표현
- fullWidth 표현
- onClick 이벤트 전달
- children 렌더링
- 접근성 이름 제공

필수 고려 Props:

- type
- variant
- size
- disabled
- loading
- fullWidth
- onClick
- children
- ariaLabel
- className

Button에 넣지 않는 것:

- 직접 API 호출
- reviewId / festivalId 같은 도메인 Props
- deleteReview 같은 도메인 함수 직접 호출
- route 이동 정책 심화
- 인증 권한 판단 심화

---

### [실무]

기본 Button 예:

```tsx
type ButtonProps = {
  type?: "button" | "submit" | "reset";
  variant?: "primary" | "secondary" | "danger" | "ghost";
  size?: "sm" | "md" | "lg";
  loading?: boolean;
  disabled?: boolean;
  fullWidth?: boolean;
  ariaLabel?: string;
  className?: string;
  onClick?: () => void;
  children: React.ReactNode;
};

function Button({
  type = "button",
  variant = "primary",
  size = "md",
  loading = false,
  disabled = false,
  fullWidth = false,
  ariaLabel,
  className = "",
  onClick,
  children,
}: ButtonProps) {
  return (
    <button
      type={type}
      className={`button button-${variant} button-${size} ${className}`}
      disabled={disabled || loading}
      aria-label={ariaLabel}
      data-full-width={fullWidth}
      onClick={onClick}
    >
      {loading ? "처리 중..." : children}
    </button>
  );
}
```

Feature Button 조합 예:

```tsx
function ReviewDeleteButton({ reviewId }: { reviewId: number }) {
  const [loading, setLoading] = useState(false);

  async function handleDelete() {
    setLoading(true);
    await deleteReview(reviewId);
    setLoading(false);
  }

  return (
    <Button variant="danger" loading={loading} onClick={handleDelete}>
      리뷰 삭제
    </Button>
  );
}
```

권장:

- 기본 type은 `button`
- Form 제출 버튼은 `type="submit"` 명시
- loading 중 disabled 처리
- danger variant는 삭제 같은 위험 액션에 사용
- 아이콘만 있는 버튼은 aria-label 필수
- 도메인 로직은 Feature Component로 분리

---

### [FAQ]

Q. Button 기본 type은 submit이 좋아?
A. 공통 Button에서는 button을 기본값으로 두는 것이 안전하다. Form 제출 버튼은 명시적으로 type submit을 사용한다.

Q. loading 중 Button은 disabled 해야 해?
A. 권장한다. 중복 클릭을 줄이고 처리 중임을 명확히 보여줄 수 있다.

Q. 공통 Button Component 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. 공통 Button은 UI 역할만 담당하고 API 호출은 Feature Component나 Hook에서 처리하는 것이 좋다.

---

## 2.2 IconButton Component Pattern

### [개념]

IconButton Component는 아이콘만으로 액션을 제공하는 Button Component다.

IconButton은 시각적 텍스트가 없을 수 있으므로 접근 가능한 이름을 aria-label로 반드시 제공해야 한다.

---

### [핵심]

IconButton 필수 기준:

- button 요소 사용
- type 기본값 button
- aria-label 필수
- icon은 aria-hidden 가능
- disabled 상태 지원
- loading 상태 지원 가능
- onClick 이벤트 전달
- 크기 size 기준 통일
- variant 기준 통일

필수 Props:

- ariaLabel
- icon 또는 children
- variant
- size
- disabled
- loading
- onClick

---

### [실무]

IconButton 예:

```tsx
type IconButtonProps = {
  ariaLabel: string;
  variant?: "primary" | "secondary" | "danger" | "ghost";
  size?: "sm" | "md" | "lg";
  disabled?: boolean;
  loading?: boolean;
  onClick?: () => void;
  children: React.ReactNode;
};

function IconButton({
  ariaLabel,
  variant = "ghost",
  size = "md",
  disabled = false,
  loading = false,
  onClick,
  children,
}: IconButtonProps) {
  return (
    <button
      type="button"
      className={`icon-button icon-button-${variant} icon-button-${size}`}
      aria-label={ariaLabel}
      disabled={disabled || loading}
      onClick={onClick}
    >
      <span aria-hidden="true">{loading ? "..." : children}</span>
    </button>
  );
}
```

사용 예:

```tsx
<IconButton ariaLabel="검색어 초기화" onClick={resetKeyword}>
  ×
</IconButton>
```

주의:

- 아이콘만 있고 aria-label이 없으면 접근성 문제
- div에 onClick 사용 금지
- 아이콘의 시각 의미만으로 액션을 전달하지 않음
- 위험 액션은 confirm flow와 danger variant 고려

---

### [FAQ]

Q. 아이콘 버튼에는 텍스트가 없어도 돼?
A. 시각적 텍스트가 없다면 aria-label로 버튼의 목적을 제공해야 한다.

Q. IconButton도 Button으로 만들면 안 돼?
A. 가능하지만 aria-label 필수화와 아이콘 전용 크기 기준이 필요하면 별도 IconButton으로 분리할 수 있다.

Q. IconButton 안의 아이콘에는 aria-hidden을 써도 돼?
A. 버튼의 aria-label이 의미를 제공한다면 장식용 아이콘은 aria-hidden으로 처리할 수 있다.

---

# 3. TextField Component Pattern

## 3.1 TextField Component Responsibility

### [개념]

TextField Component는 label, input, helper text, error message를 함께 관리하는 입력 UI Component다.

TextField는 사용자 입력을 받고, 입력 상태와 오류 상태를 접근성 속성과 함께 표현한다.

---

### [핵심]

TextField 기본 책임:

- label 제공
- input 렌더링
- value 표시
- onChange 이벤트 전달
- placeholder 제공
- required 표시
- disabled 처리
- readOnly 처리
- helperText 표시
- error message 표시
- aria-invalid 연결
- aria-describedby 연결
- id / name 연결

필수 고려 Props:

- id
- name
- label
- value
- type
- placeholder
- error
- helperText
- required
- disabled
- readOnly
- autoComplete
- onChange
- onBlur

---

### [실무]

TextField 예:

```tsx
type TextFieldProps = {
  id: string;
  name?: string;
  label: string;
  value: string;
  type?: "text" | "email" | "password" | "search" | "tel" | "url";
  placeholder?: string;
  error?: string;
  helperText?: string;
  required?: boolean;
  disabled?: boolean;
  readOnly?: boolean;
  autoComplete?: string;
  onChange: (value: string) => void;
  onBlur?: () => void;
};

function TextField({
  id,
  name,
  label,
  value,
  type = "text",
  placeholder,
  error,
  helperText,
  required = false,
  disabled = false,
  readOnly = false,
  autoComplete,
  onChange,
  onBlur,
}: TextFieldProps) {
  const errorId = `${id}-error`;
  const helperId = `${id}-helper`;
  const describedBy = error ? errorId : helperText ? helperId : undefined;

  return (
    <div className="text-field">
      <label htmlFor={id}>
        {label}
        {required && <span aria-hidden="true">*</span>}
      </label>

      <input
        id={id}
        name={name}
        type={type}
        value={value}
        placeholder={placeholder}
        required={required}
        disabled={disabled}
        readOnly={readOnly}
        autoComplete={autoComplete}
        aria-invalid={Boolean(error)}
        aria-describedby={describedBy}
        onChange={(event) => onChange(event.target.value)}
        onBlur={onBlur}
      />

      {helperText && !error && <p id={helperId}>{helperText}</p>}

      {error && (
        <p id={errorId} role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
```

권장:

- placeholder만으로 label 대체 금지
- error가 있으면 helperText보다 error 우선
- aria-invalid / aria-describedby 적용
- id 중복 방지
- value undefined 방지
- password / email / search type 지원
- onChange 전달 방식은 프로젝트 기준 통일

---

### [FAQ]

Q. placeholder만 쓰고 label은 생략해도 돼?
A. 권장하지 않는다. 접근성과 사용성 측면에서 label을 제공하는 것이 좋다.

Q. TextField에 error props를 넣는 이유는?
A. 입력값 오류를 input과 가까운 위치에 일관되게 표시하고 접근성 속성을 연결하기 위해서다.

Q. error message는 input과 어떻게 연결해?
A. error message id를 만들고 input의 aria-describedby에 연결한다.

---

## 3.2 Textarea Component Pattern

### [개념]

Textarea Component는 여러 줄 텍스트 입력을 받는 UI Component다.

Textarea는 TextField와 유사하게 label, helperText, error, aria-describedby 연결을 제공해야 한다.

---

### [핵심]

Textarea 기본 책임:

- 여러 줄 입력 제공
- label 연결
- value 관리
- onChange 이벤트 전달
- rows 지정
- maxLength 지원 가능
- helperText 표시
- error message 표시
- aria-invalid 연결
- aria-describedby 연결

필수 고려 Props:

- id
- name
- label
- value
- placeholder
- rows
- maxLength
- error
- helperText
- required
- disabled
- readOnly
- onChange
- onBlur

---

### [실무]

Textarea 예:

```tsx
type TextareaProps = {
  id: string;
  name?: string;
  label: string;
  value: string;
  placeholder?: string;
  rows?: number;
  maxLength?: number;
  error?: string;
  helperText?: string;
  required?: boolean;
  disabled?: boolean;
  readOnly?: boolean;
  onChange: (value: string) => void;
  onBlur?: () => void;
};

function Textarea({
  id,
  name,
  label,
  value,
  placeholder,
  rows = 4,
  maxLength,
  error,
  helperText,
  required = false,
  disabled = false,
  readOnly = false,
  onChange,
  onBlur,
}: TextareaProps) {
  const errorId = `${id}-error`;
  const helperId = `${id}-helper`;
  const describedBy = error ? errorId : helperText ? helperId : undefined;

  return (
    <div className="textarea-field">
      <label htmlFor={id}>{label}</label>
      <textarea
        id={id}
        name={name}
        value={value}
        placeholder={placeholder}
        rows={rows}
        maxLength={maxLength}
        required={required}
        disabled={disabled}
        readOnly={readOnly}
        aria-invalid={Boolean(error)}
        aria-describedby={describedBy}
        onChange={(event) => onChange(event.target.value)}
        onBlur={onBlur}
      />
      {helperText && !error && <p id={helperId}>{helperText}</p>}
      {error && (
        <p id={errorId} role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
```

권장:

- label 필수
- error 연결 필수
- 글자 수 제한이 있으면 maxLength 사용
- 자동 높이 조절은 별도 기준 필요
- 도메인 검증은 Form 또는 Feature Hook에서 처리

---

### [FAQ]

Q. Textarea도 label이 필요해?
A. 필요하다. 여러 줄 입력도 접근성과 사용성을 위해 label을 제공해야 한다.

Q. Textarea 검증 로직은 Component 안에 넣어도 돼?
A. 공통 Textarea에는 넣지 않는 것이 좋다. 검증은 Form이나 Feature Hook에서 처리한다.

Q. 글자 수 제한은 어디서 처리해?
A. maxLength는 Textarea Props로 줄 수 있지만, 도메인별 글자 수 정책은 Feature Form에서 관리하는 것이 좋다.

---

# 4. Select and Choice Component Pattern

## 4.1 Select Component Pattern

### [개념]

Select Component는 사용자가 여러 선택지 중 하나를 선택할 수 있게 하는 Form UI Component다.

Select는 label, value, options, onChange, error 연결을 명확히 제공해야 한다.

---

### [핵심]

Select 기본 책임:

- label 제공
- options 렌더링
- value 표시
- onChange 이벤트 전달
- placeholder option 제공 가능
- disabled 처리
- required 처리
- error 표시
- aria-invalid 연결
- aria-describedby 연결

필수 Props:

- id
- name
- label
- value
- options
- placeholder
- error
- helperText
- required
- disabled
- onChange

Option 구조:

- label
- value
- disabled

---

### [실무]

Select 예:

```tsx
type SelectOption = {
  label: string;
  value: string;
  disabled?: boolean;
};

type SelectProps = {
  id: string;
  name?: string;
  label: string;
  value: string;
  options: SelectOption[];
  placeholder?: string;
  error?: string;
  helperText?: string;
  required?: boolean;
  disabled?: boolean;
  onChange: (value: string) => void;
};

function Select({
  id,
  name,
  label,
  value,
  options,
  placeholder,
  error,
  helperText,
  required = false,
  disabled = false,
  onChange,
}: SelectProps) {
  const errorId = `${id}-error`;
  const helperId = `${id}-helper`;
  const describedBy = error ? errorId : helperText ? helperId : undefined;

  return (
    <div className="select-field">
      <label htmlFor={id}>{label}</label>
      <select
        id={id}
        name={name}
        value={value}
        required={required}
        disabled={disabled}
        aria-invalid={Boolean(error)}
        aria-describedby={describedBy}
        onChange={(event) => onChange(event.target.value)}
      >
        {placeholder && <option value="">{placeholder}</option>}
        {options.map((option) => (
          <option
            key={option.value}
            value={option.value}
            disabled={option.disabled}
          >
            {option.label}
          </option>
        ))}
      </select>
      {helperText && !error && <p id={helperId}>{helperText}</p>}
      {error && (
        <p id={errorId} role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
```

권장:

- Form 값 선택에는 native select 우선 고려
- 복잡한 메뉴 액션은 Dropdown과 구분
- options는 label / value 구조 통일
- error 접근성 연결
- placeholder는 빈 value 기준 명확화

---

### [FAQ]

Q. Select와 Dropdown은 같아?
A. 다르다. Form 값 선택에는 select가 적합할 수 있고, 메뉴 액션에는 Dropdown Menu가 적합하다.

Q. Select options 구조는 어떻게 두는 게 좋아?
A. label과 value를 기본으로 하고 필요한 경우 disabled를 추가한다.

Q. Select에도 error props가 필요해?
A. Form 입력값 오류를 표시해야 하므로 aria-invalid와 aria-describedby 연결을 포함하는 것이 좋다.

---

## 4.2 Checkbox Component Pattern

### [개념]

Checkbox Component는 true / false 또는 여러 항목 선택 상태를 표현하는 Form UI Component다.

Checkbox는 label과 input이 명확히 연결되어야 한다.

---

### [핵심]

Checkbox 기본 책임:

- checked 상태 표시
- onChange 이벤트 전달
- label 연결
- disabled 처리
- required 처리
- error 표시 가능
- aria-describedby 연결 가능
- 단일 체크 / 그룹 체크 기준 분리

필수 Props:

- id
- name
- label
- checked
- disabled
- required
- error
- onChange

---

### [실무]

Checkbox 예:

```tsx
type CheckboxProps = {
  id: string;
  name?: string;
  label: string;
  checked: boolean;
  disabled?: boolean;
  required?: boolean;
  error?: string;
  onChange: (checked: boolean) => void;
};

function Checkbox({
  id,
  name,
  label,
  checked,
  disabled = false,
  required = false,
  error,
  onChange,
}: CheckboxProps) {
  const errorId = `${id}-error`;

  return (
    <div className="checkbox-field">
      <label htmlFor={id}>
        <input
          id={id}
          name={name}
          type="checkbox"
          checked={checked}
          disabled={disabled}
          required={required}
          aria-invalid={Boolean(error)}
          aria-describedby={error ? errorId : undefined}
          onChange={(event) => onChange(event.target.checked)}
        />
        {label}
      </label>

      {error && (
        <p id={errorId} role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
```

권장:

- label 클릭으로 checkbox 토글 가능해야 함
- checked는 boolean으로 관리
- 약관 동의 같은 도메인 문구는 Feature Form에서 전달
- CheckboxGroup은 별도 Component로 분리 가능

---

### [FAQ]

Q. Checkbox label은 꼭 연결해야 해?
A. 권장한다. label을 연결하면 클릭 영역과 접근성이 좋아진다.

Q. Checkbox onChange는 event를 넘겨야 해 checked를 넘겨야 해?
A. 프로젝트 기준에 따라 다르지만 공통 Checkbox에서는 checked boolean만 넘기면 사용이 단순해진다.

Q. 여러 Checkbox는 어떻게 처리해?
A. CheckboxGroup 또는 Feature Form에서 배열 상태로 관리하는 것이 좋다.

---

## 4.3 Radio Component Pattern

### [개념]

Radio Component는 여러 선택지 중 하나만 선택해야 하는 Form UI Component다.

Radio는 단일 Radio보다 RadioGroup 구조로 관리하는 것이 일반적이다.

---

### [핵심]

RadioGroup 기본 책임:

- options 렌더링
- value 선택 상태 표시
- onChange 이벤트 전달
- group label 제공
- name 통일
- disabled option 지원
- error 표시
- role radiogroup 고려
- aria-describedby 연결

필수 Props:

- name
- label
- value
- options
- error
- onChange

---

### [실무]

RadioGroup 예:

```tsx
type RadioOption = {
  label: string;
  value: string;
  disabled?: boolean;
};

type RadioGroupProps = {
  name: string;
  label: string;
  value: string;
  options: RadioOption[];
  error?: string;
  onChange: (value: string) => void;
};

function RadioGroup({
  name,
  label,
  value,
  options,
  error,
  onChange,
}: RadioGroupProps) {
  const groupId = `${name}-group`;
  const errorId = `${name}-error`;

  return (
    <fieldset id={groupId} aria-describedby={error ? errorId : undefined}>
      <legend>{label}</legend>

      {options.map((option) => {
        const id = `${name}-${option.value}`;

        return (
          <label key={option.value} htmlFor={id}>
            <input
              id={id}
              name={name}
              type="radio"
              value={option.value}
              checked={value === option.value}
              disabled={option.disabled}
              onChange={(event) => onChange(event.target.value)}
            />
            {option.label}
          </label>
        );
      })}

      {error && (
        <p id={errorId} role="alert">
          {error}
        </p>
      )}
    </fieldset>
  );
}
```

권장:

- 관련 radio는 fieldset / legend 사용
- name은 그룹 내 동일하게 유지
- options는 label / value 구조 통일
- 하나만 선택되는 상태 보장
- 도메인 옵션 생성은 Feature에서 처리 가능

---

### [FAQ]

Q. Radio는 개별 Component보다 RadioGroup이 좋아?
A. 여러 선택지 중 하나를 선택하는 구조라면 RadioGroup이 상태와 접근성 관리에 더 적합하다.

Q. RadioGroup에서 fieldset과 legend를 써야 해?
A. 관련 선택지 그룹을 의미 있게 묶을 수 있어 접근성에 좋다.

Q. Radio options는 어디서 만들어?
A. 공통 RadioGroup은 options만 받고, 도메인별 옵션 생성은 Feature Component에서 처리하는 것이 좋다.

---

# 5. Modal and Dialog Component Pattern

## 5.1 Modal Component Pattern

### [개념]

Modal Component는 현재 화면 위에 별도 작업이나 안내를 표시하는 UI Component다.

Modal은 open 상태, title, content, footer, onClose, 접근성 속성을 명확히 제공해야 한다.

---

### [핵심]

Modal 기본 책임:

- open 상태에 따라 렌더링
- dialog 영역 제공
- backdrop 제공 가능
- title 표시
- close button 제공
- content 영역 제공
- footer slot 제공 가능
- onClose 이벤트 전달
- role dialog 적용
- aria-modal 적용
- aria-labelledby 연결
- focus management 고려
- scroll lock 고려

필수 Props:

- open
- title
- children
- footer
- onClose
- closeOnBackdrop
- closeOnEscape

---

### [실무]

Modal 예:

```tsx
type ModalProps = {
  open: boolean;
  title: string;
  children: React.ReactNode;
  footer?: React.ReactNode;
  onClose: () => void;
};

function Modal({ open, title, children, footer, onClose }: ModalProps) {
  if (!open) {
    return null;
  }

  const titleId = "modal-title";

  return (
    <div className="modal-backdrop">
      <section
        role="dialog"
        aria-modal="true"
        aria-labelledby={titleId}
        className="modal"
      >
        <header>
          <h2 id={titleId}>{title}</h2>
          <button type="button" onClick={onClose} aria-label="닫기">
            ×
          </button>
        </header>

        <div className="modal-body">{children}</div>

        {footer && <footer className="modal-footer">{footer}</footer>}
      </section>
    </div>
  );
}
```

권장:

- open으로 표시 여부 제어
- title과 aria-labelledby 연결
- 닫기 버튼 제공
- footer는 ReactNode로 조합
- Confirm Dialog와 일반 Modal 구분 가능
- focus trap / scroll lock은 별도 구현 또는 라이브러리 검토
- 중첩 Modal 지양

---

### [FAQ]

Q. Modal은 div만 띄우면 돼?
A. 시각적으로는 가능하지만 접근성을 위해 role dialog, aria-modal, focus 관리, 닫기 동작을 고려해야 한다.

Q. Modal 안에서 API 호출을 직접 처리해도 돼?
A. Feature Modal은 가능하지만 공통 Modal은 UI 구조만 제공하고 실제 로직은 부모가 처리하는 것이 좋다.

Q. Modal footer는 어떻게 설계해?
A. footer를 ReactNode로 받아 확인, 취소, 링크 같은 다양한 액션을 외부에서 조합하게 만들 수 있다.

---

## 5.2 ConfirmDialog Component Pattern

### [개념]

ConfirmDialog Component는 삭제, 로그아웃, 결제 취소 같은 중요한 액션을 실행하기 전에 사용자 확인을 받는 Dialog Component다.

ConfirmDialog는 일반 Modal보다 confirm / cancel 이벤트와 destructive action 처리가 중요하다.

---

### [핵심]

ConfirmDialog 기본 책임:

- open 상태 제어
- title 표시
- description 표시
- confirm button 제공
- cancel button 제공
- loading 상태 처리
- onConfirm 이벤트 전달
- onCancel 이벤트 전달
- danger action 표현 가능
- role dialog 적용
- aria-modal 적용

필수 Props:

- open
- title
- description
- confirmText
- cancelText
- loading
- variant
- onConfirm
- onCancel

---

### [실무]

ConfirmDialog 예:

```tsx
type ConfirmDialogProps = {
  open: boolean;
  title: string;
  description?: string;
  confirmText?: string;
  cancelText?: string;
  loading?: boolean;
  variant?: "default" | "danger";
  onConfirm: () => void;
  onCancel: () => void;
};

function ConfirmDialog({
  open,
  title,
  description,
  confirmText = "확인",
  cancelText = "취소",
  loading = false,
  variant = "default",
  onConfirm,
  onCancel,
}: ConfirmDialogProps) {
  if (!open) {
    return null;
  }

  return (
    <section role="dialog" aria-modal="true" className="confirm-dialog">
      <h2>{title}</h2>
      {description && <p>{description}</p>}

      <div className="confirm-dialog-actions">
        <Button variant="secondary" disabled={loading} onClick={onCancel}>
          {cancelText}
        </Button>
        <Button
          variant={variant === "danger" ? "danger" : "primary"}
          loading={loading}
          onClick={onConfirm}
        >
          {confirmText}
        </Button>
      </div>
    </section>
  );
}
```

사용 예:

```tsx
<ConfirmDialog
  open={open}
  title="리뷰를 삭제할까요?"
  description="삭제한 리뷰는 복구할 수 없습니다."
  confirmText="삭제"
  cancelText="취소"
  variant="danger"
  loading={loading}
  onConfirm={deleteReview}
  onCancel={closeDialog}
/>
```

권장:

- 위험 액션은 confirm UI 제공
- confirmText는 액션을 구체적으로 표현
- loading 중 중복 confirm 방지
- cancel 가능 여부 명확화
- 실제 API 호출은 부모 또는 Feature Hook에서 처리

---

### [FAQ]

Q. 삭제 버튼을 누르면 바로 삭제해도 돼?
A. 중요한 데이터 삭제는 Confirm Dialog를 제공하는 것이 안전하다.

Q. ConfirmDialog 안에서 직접 delete API를 호출해도 돼?
A. 공통 Dialog라면 onConfirm만 호출하고 실제 delete API는 부모 Feature Component에서 처리하는 것이 좋다.

Q. ConfirmDialog의 confirmText는 어떻게 쓰는 게 좋아?
A. 확인보다 삭제, 저장, 로그아웃처럼 실제 실행 액션을 구체적으로 쓰는 것이 좋다.

---

# 6. Card and Badge Component Pattern

## 6.1 Card Component Pattern

### [개념]

Card Component는 관련 정보를 하나의 시각적 단위로 묶어 보여주는 UI Component다.

Common Card는 도메인 데이터를 직접 알지 않고 children을 받아 범용 컨테이너 역할을 한다.

---

### [핵심]

Card 기본 책임:

- 정보 그룹 컨테이너 제공
- children 렌더링
- variant 적용 가능
- interactive 여부 표현 가능
- semantic element 선택
- className 확장 가능
- 자체 스타일 담당
- grid / gap / margin 같은 layout 책임 제외

Card 사용 대상:

- FestivalCard
- ReviewCard
- NotificationCard
- ProfileCard
- DashboardCard
- SummaryCard

---

### [실무]

Common Card 예:

```tsx
type CardProps = {
  variant?: "default" | "outlined" | "elevated";
  interactive?: boolean;
  className?: string;
  onClick?: () => void;
  children: React.ReactNode;
};

function Card({
  variant = "default",
  interactive = false,
  className = "",
  onClick,
  children,
}: CardProps) {
  if (interactive) {
    return (
      <button
        type="button"
        className={`card card-${variant} card-interactive ${className}`}
        onClick={onClick}
      >
        {children}
      </button>
    );
  }

  return (
    <article className={`card card-${variant} ${className}`}>
      {children}
    </article>
  );
}
```

Feature Card 예:

```tsx
function FestivalCard({ festival }: { festival: Festival }) {
  return (
    <Card>
      <img src={festival.imageUrl} alt="" />
      <h3>{festival.title}</h3>
      <p>{festival.regionName}</p>
      <Badge>{festival.categoryName}</Badge>
    </Card>
  );
}
```

권장:

- 정보 그룹 단위로 사용
- Common Card는 도메인 데이터 직접 사용 금지
- 클릭 가능한 Card는 button 또는 Link 사용
- article / button / link 중 의미에 맞는 태그 선택
- Card는 자체 스타일만 담당하고 grid 배치는 부모가 담당

---

### [FAQ]

Q. 클릭 가능한 Card는 div에 onClick을 붙이면 돼?
A. 권장하지 않는다. 링크 이동이면 anchor 또는 Link, 액션이면 button을 사용하는 것이 접근성에 좋다.

Q. Card Component 안에 도메인 데이터를 직접 넣어야 해?
A. 공통 Card는 children만 받고 도메인 데이터는 FestivalCard 같은 Feature Component에서 처리하는 것이 좋다.

Q. Card가 grid 배치까지 담당해야 해?
A. 보통 Card는 자체 모양만 담당하고 grid 배치는 부모 List나 Layout Component가 담당한다.

---

## 6.2 Badge Component Pattern

### [개념]

Badge Component는 상태, 카테고리, 권한, 태그 같은 짧은 정보를 시각적으로 표시하는 UI Component다.

Badge는 색상만으로 의미를 전달하지 않고 텍스트나 접근 가능한 이름으로 의미를 제공해야 한다.

---

### [핵심]

Badge 기본 책임:

- 짧은 텍스트 표시
- variant 적용
- status 표현
- category 표현
- tag 표현
- count 표현 가능
- children 렌더링
- 색상 외 정보 제공
- className 확장 가능

사용 대상:

- status
- category
- role
- tag
- count
- notification
- festival theme
- review rating basics

Variant 후보:

- default
- success
- warning
- danger
- info

---

### [실무]

Badge 예:

```tsx
type BadgeProps = {
  variant?: "default" | "success" | "warning" | "danger" | "info";
  className?: string;
  children: React.ReactNode;
};

function Badge({ variant = "default", className = "", children }: BadgeProps) {
  return (
    <span className={`badge badge-${variant} ${className}`}>{children}</span>
  );
}
```

상태 Badge 예:

```tsx
<Badge variant="success">진행 중</Badge>
<Badge variant="warning">예정</Badge>
<Badge variant="danger">종료</Badge>
```

권장:

- 짧은 텍스트 표시
- 의미 기반 variant 사용
- 색상명 variant 지양
- 색상만으로 의미 전달 금지
- role badge는 실제 권한 검증과 구분
- count badge는 aria-label 고려

---

### [FAQ]

Q. Badge는 언제 써?
A. 상태, 카테고리, 태그, 권한처럼 짧은 보조 정보를 표시할 때 사용한다.

Q. Badge 색상만으로 상태를 표현해도 돼?
A. 권장하지 않는다. 텍스트나 아이콘 등 색상 외 정보도 함께 제공하는 것이 좋다.

Q. Badge variant는 색상명으로 만들어도 돼?
A. 가능은 하지만 success, warning, danger처럼 의미 기반 이름이 디자인 변경에 더 유연하다.

---

# 7. Tooltip and Avatar Basics

## 7.1 Avatar Component Pattern

### [개념]

Avatar Component는 사용자나 엔티티의 대표 이미지를 표시하는 UI Component다.

Avatar는 이미지가 없을 때 fallback 텍스트나 기본 UI를 제공해야 한다.

---

### [핵심]

Avatar 기본 책임:

- 이미지 표시
- fallback 표시
- size 적용
- alt 제공
- shape 적용 가능
- loading 실패 대응 가능
- 사용자 이름 기반 fallback 가능

필수 Props:

- src
- alt
- fallback
- size
- shape

주의:

- alt 누락 금지
- 장식용이면 alt 빈 문자열 가능
- 사용자 식별 목적이면 의미 있는 alt 필요
- 이미지 로딩 실패 fallback 고려

---

### [실무]

Avatar 예:

```tsx
type AvatarProps = {
  src?: string;
  alt: string;
  fallback: string;
  size?: "sm" | "md" | "lg";
  shape?: "circle" | "square";
};

function Avatar({
  src,
  alt,
  fallback,
  size = "md",
  shape = "circle",
}: AvatarProps) {
  if (!src) {
    return (
      <span className={`avatar avatar-${size} avatar-${shape}`}>
        {fallback}
      </span>
    );
  }

  return (
    <img
      className={`avatar avatar-${size} avatar-${shape}`}
      src={src}
      alt={alt}
    />
  );
}
```

사용 예:

```tsx
<Avatar
  src={user.profileImageUrl}
  alt={`${user.nickname} 프로필 이미지`}
  fallback={user.nickname.slice(0, 1)}
/>
```

---

### [FAQ]

Q. Avatar alt는 어떻게 써야 해?
A. 사용자를 식별하는 이미지라면 닉네임 프로필 이미지처럼 의미 있는 alt를 제공하는 것이 좋다.

Q. Avatar 이미지가 없으면 어떻게 해?
A. fallback 텍스트나 기본 아이콘을 보여주는 것이 좋다.

Q. Avatar size는 px로 받아도 돼?
A. 공통 Component에서는 sm, md, lg처럼 제한된 size 값을 사용하는 것이 일관성에 좋다.

---

## 7.2 Tooltip Basics

### [개념]

Tooltip은 짧은 보조 설명을 hover, focus 등으로 보여주는 UI Pattern이다.

Tooltip은 중요한 정보를 숨기는 용도가 아니라, 보조 설명이나 추가 힌트를 제공하는 용도로 사용해야 한다.

---

### [핵심]

Tooltip 기본 책임:

- 짧은 보조 설명 제공
- trigger 요소와 연결
- hover / focus 대응
- aria-describedby 고려
- keyboard 접근성 고려
- mobile 환경 대체 고려
- 긴 설명 지양

주의:

- 필수 정보를 Tooltip에만 숨기지 않음
- hover만 의존하지 않음
- tooltip 내용은 짧게 유지
- 복잡한 상호작용은 Popover 검토
- 접근성 구현 난도가 있음

---

### [실무]

Tooltip 기본 구조 예:

```tsx
type TooltipProps = {
  id: string;
  content: string;
  children: React.ReactElement;
};

function Tooltip({ id, content, children }: TooltipProps) {
  return (
    <span className="tooltip-wrapper">
      {React.cloneElement(children, {
        "aria-describedby": id,
      })}
      <span id={id} role="tooltip" className="tooltip">
        {content}
      </span>
    </span>
  );
}
```

사용 예:

```tsx
<Tooltip id="save-tooltip" content="변경 내용을 저장합니다.">
  <Button>저장</Button>
</Tooltip>
```

권장:

- 짧은 설명만 제공
- focus 접근 가능해야 함
- 중요한 오류나 안내는 Tooltip이 아니라 visible text 사용
- 복잡한 구현은 검증된 UI library 검토 가능

---

### [FAQ]

Q. Tooltip에 중요한 정보를 넣어도 돼?
A. 권장하지 않는다. 중요한 정보는 항상 보이게 표시하고 Tooltip은 보조 설명에 사용한다.

Q. Tooltip은 hover만 처리하면 돼?
A. 아니다. 키보드 사용자를 위해 focus 접근도 고려해야 한다.

Q. Tooltip이 복잡해지면 어떻게 해?
A. Popover나 Dialog 같은 다른 UI Pattern을 검토하는 것이 좋다.

---

# 8. Base UI Component Checklist

## 8.1 Base UI Review Checklist

### [개념]

Base UI Review Checklist는 Button, TextField, Modal, Card 같은 기본 공통 Component가 적절히 설계되었는지 검수하는 기준이다.

Frontend Agent와 Review Agent는 Base UI Component 생성 후 책임, Props, 접근성, 스타일 경계를 반드시 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Base UI Component가 Common UI 책임만 담당하는가?
- [ ] 도메인 Props가 포함되지 않았는가?
- [ ] 직접 API 호출이 없는가?
- [ ] Props 이름이 명확한가?
- [ ] variant / size 기준이 통일되었는가?
- [ ] disabled / loading 상태 처리가 명확한가?
- [ ] Event Handler Props는 onX 형태인가?
- [ ] Button 기본 type이 button인가?
- [ ] Form 제출 버튼은 type submit을 명시하는가?
- [ ] IconButton에 aria-label이 있는가?
- [ ] TextField / Textarea / Select에 label이 있는가?
- [ ] error message가 aria-describedby로 연결되는가?
- [ ] Modal에 role dialog와 aria-modal이 있는가?
- [ ] Card에 div onClick을 남용하지 않았는가?
- [ ] Badge가 색상만으로 의미를 전달하지 않는가?
- [ ] Component 자체 스타일과 Layout 스타일이 분리되었는가?
- [ ] className 확장 기준이 있는가?
- [ ] Props Explosion이 없는가?
- [ ] Over Abstraction이 없는가?
```

---

### [실무]

검수 Flow:

```text
Base UI Draft
→ Responsibility Check
→ Props API Check
→ State Props Check
→ Accessibility Check
→ Styling Boundary Check
→ Feature Dependency Check
→ Anti Pattern Check
→ Final Component Output
```

치명적 문제:

```text
Button 내부 API 호출
Button 기본 type 누락
IconButton aria-label 누락
TextField label 누락
error와 input 연결 누락
Modal 접근성 속성 누락
Card div onClick 남용
Badge 색상만으로 상태 전달
Common UI에 festivalId / reviewId 포함
Component 내부 margin 남발
```

---

### [FAQ]

Q. Base UI Component 검수에서 가장 중요한 것은 뭐야?
A. Common UI 책임만 담당하는지, 도메인 로직이 없는지, 접근성 속성이 포함되었는지 확인하는 것이다.

Q. Base UI Component에서 치명적인 문제는 뭐야?
A. API 호출, 도메인 Props, 접근성 누락, Props Explosion, div onClick 남용이 치명적이다.

Q. Review Agent는 Base UI Component를 어떻게 검토해야 해?
A. 책임 분리, Props API, variant / size, disabled / loading, 접근성, 스타일 경계, 도메인 의존성을 순서대로 확인해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Base UI Component는 뭐야?
A. Button, TextField, Modal, Card처럼 여러 화면에서 반복 사용되는 가장 기본적인 Common UI Component다.

Q. Base UI Component 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. Base UI Component는 UI 표현과 이벤트 전달만 담당하고 API 호출은 Feature Component나 Hook에서 처리한다.

Q. Base UI Component는 언제 만들어?
A. 여러 화면에서 반복되고 역할과 Props가 안정적일 때 공통 Component로 만든다.

Q. Button Component는 어떻게 설계해?
A. type, variant, size, disabled, loading, fullWidth, onClick, children, ariaLabel 기준을 명확히 설계한다.

Q. Button 기본 type은 submit이 좋아?
A. 공통 Button에서는 button을 기본값으로 두는 것이 안전하다. Form 제출 버튼은 명시적으로 type submit을 사용한다.

Q. loading 중 Button은 disabled 해야 해?
A. 권장한다. 중복 클릭을 줄이고 처리 중임을 명확히 보여줄 수 있다.

Q. 공통 Button Component 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. 공통 Button은 UI 역할만 담당하고 API 호출은 Feature Component나 Hook에서 처리하는 것이 좋다.

Q. IconButton은 어떻게 설계해?
A. button 요소를 사용하고 aria-label을 필수로 받아 아이콘만 있어도 접근 가능한 이름을 제공해야 한다.

Q. 아이콘 버튼에는 텍스트가 없어도 돼?
A. 시각적 텍스트가 없다면 aria-label로 버튼의 목적을 제공해야 한다.

Q. IconButton도 Button으로 만들면 안 돼?
A. 가능하지만 aria-label 필수화와 아이콘 전용 크기 기준이 필요하면 별도 IconButton으로 분리할 수 있다.

Q. IconButton 안의 아이콘에는 aria-hidden을 써도 돼?
A. 버튼의 aria-label이 의미를 제공한다면 장식용 아이콘은 aria-hidden으로 처리할 수 있다.

Q. TextField Component는 어떻게 설계해?
A. id, label, value, error, helperText, required, disabled, onChange를 받고 aria-invalid와 aria-describedby를 연결한다.

Q. placeholder만 쓰고 label은 생략해도 돼?
A. 권장하지 않는다. 접근성과 사용성 측면에서 label을 제공하는 것이 좋다.

Q. TextField에 error props를 넣는 이유는?
A. 입력값 오류를 input과 가까운 위치에 일관되게 표시하고 접근성 속성을 연결하기 위해서다.

Q. error message는 input과 어떻게 연결해?
A. error message id를 만들고 input의 aria-describedby에 연결한다.

Q. Textarea도 label이 필요해?
A. 필요하다. 여러 줄 입력도 접근성과 사용성을 위해 label을 제공해야 한다.

Q. Textarea 검증 로직은 Component 안에 넣어도 돼?
A. 공통 Textarea에는 넣지 않는 것이 좋다. 검증은 Form이나 Feature Hook에서 처리한다.

Q. 글자 수 제한은 어디서 처리해?
A. maxLength는 Textarea Props로 줄 수 있지만, 도메인별 글자 수 정책은 Feature Form에서 관리하는 것이 좋다.

Q. Select와 Dropdown은 같아?
A. 다르다. Form 값 선택에는 select가 적합할 수 있고, 메뉴 액션에는 Dropdown Menu가 적합하다.

Q. Select options 구조는 어떻게 두는 게 좋아?
A. label과 value를 기본으로 하고 필요한 경우 disabled를 추가한다.

Q. Select에도 error props가 필요해?
A. Form 입력값 오류를 표시해야 하므로 aria-invalid와 aria-describedby 연결을 포함하는 것이 좋다.

Q. Checkbox label은 꼭 연결해야 해?
A. 권장한다. label을 연결하면 클릭 영역과 접근성이 좋아진다.

Q. Checkbox onChange는 event를 넘겨야 해 checked를 넘겨야 해?
A. 프로젝트 기준에 따라 다르지만 공통 Checkbox에서는 checked boolean만 넘기면 사용이 단순해진다.

Q. 여러 Checkbox는 어떻게 처리해?
A. CheckboxGroup 또는 Feature Form에서 배열 상태로 관리하는 것이 좋다.

Q. Radio는 개별 Component보다 RadioGroup이 좋아?
A. 여러 선택지 중 하나를 선택하는 구조라면 RadioGroup이 상태와 접근성 관리에 더 적합하다.

Q. RadioGroup에서 fieldset과 legend를 써야 해?
A. 관련 선택지 그룹을 의미 있게 묶을 수 있어 접근성에 좋다.

Q. Radio options는 어디서 만들어?
A. 공통 RadioGroup은 options만 받고, 도메인별 옵션 생성은 Feature Component에서 처리하는 것이 좋다.

Q. Modal은 div만 띄우면 돼?
A. 시각적으로는 가능하지만 접근성을 위해 role dialog, aria-modal, focus 관리, 닫기 동작을 고려해야 한다.

Q. Modal 안에서 API 호출을 직접 처리해도 돼?
A. Feature Modal은 가능하지만 공통 Modal은 UI 구조만 제공하고 실제 로직은 부모가 처리하는 것이 좋다.

Q. Modal footer는 어떻게 설계해?
A. footer를 ReactNode로 받아 확인, 취소, 링크 같은 다양한 액션을 외부에서 조합하게 만들 수 있다.

Q. 삭제 버튼을 누르면 바로 삭제해도 돼?
A. 중요한 데이터 삭제는 Confirm Dialog를 제공하는 것이 안전하다.

Q. ConfirmDialog 안에서 직접 delete API를 호출해도 돼?
A. 공통 Dialog라면 onConfirm만 호출하고 실제 delete API는 부모 Feature Component에서 처리하는 것이 좋다.

Q. ConfirmDialog의 confirmText는 어떻게 쓰는 게 좋아?
A. 확인보다 삭제, 저장, 로그아웃처럼 실제 실행 액션을 구체적으로 쓰는 것이 좋다.

Q. 클릭 가능한 Card는 div에 onClick을 붙이면 돼?
A. 권장하지 않는다. 링크 이동이면 anchor 또는 Link, 액션이면 button을 사용하는 것이 접근성에 좋다.

Q. Card Component 안에 도메인 데이터를 직접 넣어야 해?
A. 공통 Card는 children만 받고 도메인 데이터는 FestivalCard 같은 Feature Component에서 처리하는 것이 좋다.

Q. Card가 grid 배치까지 담당해야 해?
A. 보통 Card는 자체 모양만 담당하고 grid 배치는 부모 List나 Layout Component가 담당한다.

Q. Badge는 언제 써?
A. 상태, 카테고리, 태그, 권한처럼 짧은 보조 정보를 표시할 때 사용한다.

Q. Badge 색상만으로 상태를 표현해도 돼?
A. 권장하지 않는다. 텍스트나 아이콘 등 색상 외 정보도 함께 제공하는 것이 좋다.

Q. Badge variant는 색상명으로 만들어도 돼?
A. 가능은 하지만 success, warning, danger처럼 의미 기반 이름이 디자인 변경에 더 유연하다.

Q. Avatar alt는 어떻게 써야 해?
A. 사용자를 식별하는 이미지라면 닉네임 프로필 이미지처럼 의미 있는 alt를 제공하는 것이 좋다.

Q. Avatar 이미지가 없으면 어떻게 해?
A. fallback 텍스트나 기본 아이콘을 보여주는 것이 좋다.

Q. Avatar size는 px로 받아도 돼?
A. 공통 Component에서는 sm, md, lg처럼 제한된 size 값을 사용하는 것이 일관성에 좋다.

Q. Tooltip에 중요한 정보를 넣어도 돼?
A. 권장하지 않는다. 중요한 정보는 항상 보이게 표시하고 Tooltip은 보조 설명에 사용한다.

Q. Tooltip은 hover만 처리하면 돼?
A. 아니다. 키보드 사용자를 위해 focus 접근도 고려해야 한다.

Q. Tooltip이 복잡해지면 어떻게 해?
A. Popover나 Dialog 같은 다른 UI Pattern을 검토하는 것이 좋다.

Q. Base UI Component 검수에서 가장 중요한 것은 뭐야?
A. Common UI 책임만 담당하는지, 도메인 로직이 없는지, 접근성 속성이 포함되었는지 확인하는 것이다.

Q. Base UI Component에서 치명적인 문제는 뭐야?
A. API 호출, 도메인 Props, 접근성 누락, Props Explosion, div onClick 남용이 치명적이다.

Q. Review Agent는 Base UI Component를 어떻게 검토해야 해?
A. 책임 분리, Props API, variant / size, disabled / loading, 접근성, 스타일 경계, 도메인 의존성을 순서대로 확인해야 한다.
