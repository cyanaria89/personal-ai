# Design System Foundation Part03 - Component Specification Rules

---

# 1. Component Specification Core

## 1.1 Component Specification Definition

### [개념]

Component Specification은 공통 UI 컴포넌트의 목적, 구조, props, variant, size, state, accessibility, usage, do / don't, examples를 정의한 규격이다.

Component Specification은 Frontend Agent가 컴포넌트를 일관되게 생성하고 Review Agent가 컴포넌트 품질을 검토하기 위한 기준 문서다.

Component Specification은 단순 설명서가 아니라 **RAG Retrieval 기반 코드 생성 / 코드 검토 / UI 승인 기준**이다.

---

### [핵심]

Component Specification 필수 항목:

```md
# Component Name

## Purpose

## Anatomy

## Props

## Variants

## Sizes

## States

## Accessibility

## Usage

## Do

## Don't

## Examples
```

Component Specification 목적:

- 컴포넌트 목적 명확화
- props API 통일
- variant 기준 통일
- size 기준 통일
- state 기준 통일
- accessibility 기본 품질 확보
- 사용 예시 제공
- 잘못된 사용 방지
- Frontend Agent 생성 기준 제공
- Review Agent 검토 기준 제공

---

### [실무]

Component Specification은 코드 생성 기준이 되어야 한다.

Frontend Agent는 Spec에 없는 variant, size, state를 임의로 만들지 않아야 한다.

Review Agent는 구현 코드가 Component Specification과 다른 props, variant, state, accessibility 기준을 만들었는지 검토해야 한다.

기본 Flow:

```text
Requirement
→ Component Specification 확인
→ Component 선택
→ Props / Variant / Size / State 적용
→ Accessibility 적용
→ Usage Example 기준 확인
→ UI 구현
→ Review Checklist
```

---

### [FAQ]

Q. Component Specification이 뭐야?
A. 컴포넌트의 목적, props, variant, size, state, accessibility, 사용 예시를 정의한 규격이다.

Q. Component Specification은 왜 필요해?
A. Frontend Agent와 개발자가 같은 컴포넌트를 같은 방식으로 사용하기 위해 필요하다.

Q. Component Specification은 사람용 문서야?
A. 아니다. Frontend Agent 코드 생성과 Review Agent 검토를 위한 RAG 기준 문서다.

Q. Spec에 없는 variant를 만들어도 돼?
A. 필요하면 가능하지만 먼저 기존 variant로 해결 가능한지 확인하고 추가 이유를 명확히 해야 한다.

---

## 1.2 Component Specification Scope

### [개념]

Component Specification Scope는 Design System Foundation 단계에서 공통 컴포넌트 규격으로 정의해야 하는 범위다.

이 문서는 Core Component와 UI Pattern Component의 공통 작성 규칙을 다룬다.

---

### [핵심]

포함 범위:

- Component Name
- Purpose
- Anatomy
- Props API
- Variant Rules
- Size Rules
- State Rules
- Accessibility Rules
- Usage Rules
- Do / Don't
- Examples
- Review Checklist
- Documentation Rules

주요 대상 컴포넌트:

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
- Empty State
- Loading State
- Error State

제외 범위:

- 컴포넌트 라이브러리 패키징 심화
- Storybook Addon 심화
- Visual Regression Testing 심화
- Multi-brand Component Governance
- Monorepo Package Publishing
- Native App Component Spec

---

### [실무]

Part03은 컴포넌트 규격 작성 방식의 기준이다.

Part04 Core Component Rules는 Part03 기준을 사용해 Button, Input, Card, Modal 같은 핵심 컴포넌트를 구체화한다.

문서 연계:

```text
Part01 Design System Core
→ Part02 Design Token Rules
→ Part03 Component Specification Rules
→ Part04 Core Component Rules
```

Component Spec은 반드시 Part02 Design Token Rules를 기반으로 작성한다.

---

### [FAQ]

Q. Component Specification Scope는 어디까지야?
A. 공통 UI 컴포넌트의 목적, props, variant, size, state, accessibility, usage 기준까지다.

Q. 모든 컴포넌트에 Specification이 필요해?
A. 공통 재사용 컴포넌트에는 필요하다. 일회성 UI는 최소 기준만 적용할 수 있다.

Q. Part03과 Part04는 뭐가 달라?
A. Part03은 규격 작성 방식이고, Part04는 Button, Input, Card, Modal 같은 실제 컴포넌트 기준이다.

Q. Component Spec은 token과 연결돼야 해?
A. 반드시 연결되어야 한다. variant, size, state 스타일은 Design Token을 기반으로 정의해야 한다.

---

# 2. Component API Rules

## 2.1 Component API Definition

### [개념]

Component API는 컴포넌트를 사용하는 props, event handler, children, ref, className, data attribute의 규칙이다.

Component API는 사용자가 컴포넌트를 예측 가능하게 사용할 수 있도록 만드는 인터페이스다.

---

### [핵심]

Component API 기준:

- props 이름은 역할 중심
- boolean props는 의미 명확
- variant와 size는 제한된 값 사용
- event handler는 `on` prefix 사용
- children 사용 가능성 검토
- disabled / loading 상태 명확화
- className override 정책 명확화
- style override 남용 금지
- accessibility props 지원
- type safety 확보

좋은 API:

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

나쁜 API:

```tsx
type ButtonProps = {
  blue?: boolean;
  big?: boolean;
  flag?: boolean;
  fn?: () => void;
};
```

---

### [실무]

좋은 사용 예:

```jsx
<Button variant="primary" size="md" onClick={handleSave}>
  저장
</Button>
```

나쁜 사용 예:

```jsx
<Button blue big flag fn={save}>
  저장
</Button>
```

Review 기준:

```md
- [ ] props 이름이 역할 중심인가?
- [ ] boolean props 의미가 명확한가?
- [ ] variant / size 값이 제한되어 있는가?
- [ ] event handler가 on prefix를 사용하는가?
- [ ] style override가 남용되지 않는가?
- [ ] 접근성에 필요한 props를 지원하는가?
```

---

### [FAQ]

Q. Component API가 뭐야?
A. 컴포넌트를 사용하는 props, event handler, children, override 정책의 규칙이다.

Q. props 이름은 어떻게 지어야 해?
A. 역할이 명확한 이름을 사용한다. 예: `variant`, `size`, `isLoading`, `disabled`, `onClick`.

Q. boolean props는 어떻게 지어야 해?
A. `isLoading`, `isOpen`, `isSelected`, `disabled`처럼 상태 의미가 명확해야 한다.

Q. event handler는 어떻게 지어야 해?
A. `onClick`, `onChange`, `onClose`, `onSubmit`처럼 `on` prefix를 사용한다.

---

## 2.2 Props Naming Rules

### [개념]

Props Naming Rules는 컴포넌트 props 이름을 일관되게 작성하는 기준이다.

Props 이름은 Frontend Agent가 검색하고 코드 생성할 수 있도록 의미가 명확해야 한다.

---

### [핵심]

권장 props 이름:

```text
variant
size
disabled
isLoading
isOpen
isSelected
isChecked
errorMessage
helperText
placeholder
value
defaultValue
onChange
onClick
onClose
onSubmit
children
className
ariaLabel
```

비권장 props 이름:

```text
blue
red
big
smallFlag
check
err
msg
func
fn
data1
mode2
```

Naming 기준:

- 색상명보다 의미 사용
- 축약어 남발 금지
- boolean은 상태 의미 명확
- event는 on prefix
- error는 errorMessage로 명확화
- helper text와 error message 구분

---

### [실무]

Input Props 예:

```tsx
type TextInputProps = {
  id: string;
  name: string;
  label: string;
  value: string;
  placeholder?: string;
  disabled?: boolean;
  readOnly?: boolean;
  helperText?: string;
  errorMessage?: string;
  onChange: (value: string) => void;
};
```

Modal Props 예:

```tsx
type ModalProps = {
  isOpen: boolean;
  title: string;
  children: React.ReactNode;
  onClose: () => void;
};
```

Review 기준:

```md
- [ ] props 이름이 컴포넌트 역할과 일치하는가?
- [ ] 축약어가 과하지 않은가?
- [ ] errorMessage와 helperText가 구분되는가?
- [ ] isOpen / isLoading 같은 boolean 이름이 명확한가?
```

---

### [FAQ]

Q. props 이름에 색상명을 넣어도 돼?
A. 권장하지 않는다. `blue`보다 `variant="primary"`처럼 의미 중심 이름이 좋다.

Q. `fn`, `msg`, `err` 같은 축약어를 써도 돼?
A. 권장하지 않는다. RAG 검색과 코드 가독성을 위해 명확한 이름을 사용한다.

Q. error와 helper text는 같은 props로 처리해도 돼?
A. 구분하는 것이 좋다. errorMessage는 오류, helperText는 안내 문구다.

Q. className prop은 허용해도 돼?
A. 가능하지만 override 범위를 명확히 해야 한다.

---

## 2.3 Event Handler Rules

### [개념]

Event Handler Rules는 컴포넌트 이벤트 props를 일관되게 정의하는 기준이다.

Event Handler는 사용자의 행동과 컴포넌트 상태 변경을 연결한다.

---

### [핵심]

Event Handler naming:

```text
onClick
onChange
onSubmit
onClose
onOpen
onConfirm
onCancel
onSelect
onDelete
onRetry
onPageChange
```

기준:

- `on` prefix 사용
- 이벤트 의미 명확화
- 불필요한 generic 이름 금지
- handler 인자 타입 명확화
- 상태 변경과 사이드 이펙트 구분
- 컴포넌트 내부에서 임의 API 호출 최소화

---

### [실무]

좋은 예:

```tsx
type PaginationProps = {
  currentPage: number;
  totalPages: number;
  onPageChange: (page: number) => void;
};
```

좋은 사용:

```jsx
<Pagination currentPage={page} totalPages={totalPages} onPageChange={setPage} />
```

나쁜 예:

```tsx
type PaginationProps = {
  fn: (x: any) => void;
};
```

Review 기준:

```md
- [ ] event handler 이름이 on prefix를 사용하는가?
- [ ] handler가 어떤 행동을 처리하는지 명확한가?
- [ ] 인자 타입이 명확한가?
- [ ] `any`가 불필요하게 사용되지 않는가?
```

---

### [FAQ]

Q. Event Handler 이름은 어떻게 지어야 해?
A. `onClick`, `onChange`, `onClose`, `onSubmit`처럼 `on` prefix와 행동 이름을 사용한다.

Q. `handleClick`을 props 이름으로 써도 돼?
A. 컴포넌트 내부 함수명으로는 가능하지만 외부 props는 `onClick`이 일반적이다.

Q. handler 인자 타입은 명확해야 해?
A. 명확해야 한다. TypeScript에서는 `page: number`, `value: string`처럼 제한하는 것이 좋다.

Q. 컴포넌트 내부에서 API를 직접 호출해도 돼?
A. 공통 UI 컴포넌트는 가능하면 UI 이벤트만 전달하고 API 호출은 상위에서 처리하는 것이 좋다.

---

## 2.4 Children and Composition Rules

### [개념]

Children and Composition Rules는 컴포넌트를 어떻게 조합 가능하게 만들지 정의하는 기준이다.

Composition은 작은 컴포넌트를 조합해 복잡한 UI를 만드는 방식이다.

---

### [핵심]

좋은 Composition:

```text
Card
→ CardHeader
→ CardBody
→ CardFooter

Modal
→ ModalHeader
→ ModalBody
→ ModalFooter

FormField
→ Label
→ Control
→ HelperText
→ ErrorMessage

Tabs
→ TabList
→ Tab
→ TabPanel
```

기준:

- children이 필요한 컴포넌트는 명확히 허용
- 단순 컴포넌트는 props 중심
- 복잡한 컴포넌트는 composition 고려
- sub component 이름 명확화
- 너무 깊은 조합 금지
- 기본 use case가 쉬워야 함

---

### [실무]

Card Composition 예:

```jsx
<Card>
  <CardHeader>
    <CardTitle>서울 빛 축제</CardTitle>
  </CardHeader>
  <CardBody>
    <p>야간 조명 축제입니다.</p>
  </CardBody>
  <CardFooter>
    <Button>자세히 보기</Button>
  </CardFooter>
</Card>
```

Modal Composition 예:

```jsx
<Modal isOpen={isOpen} onClose={closeModal}>
  <ModalHeader title="리뷰 작성" />
  <ModalBody>
    <ReviewForm />
  </ModalBody>
  <ModalFooter>
    <Button variant="secondary" onClick={closeModal}>
      취소
    </Button>
    <Button variant="primary">등록</Button>
  </ModalFooter>
</Modal>
```

Review 기준:

```md
- [ ] 조합 구조가 직관적인가?
- [ ] sub component 이름이 명확한가?
- [ ] 기본 사용이 과도하게 복잡하지 않은가?
- [ ] children 사용 목적이 명확한가?
```

---

### [FAQ]

Q. children은 언제 사용해?
A. Button 텍스트, Card 내용, Modal 내용처럼 사용자가 내용을 주입해야 할 때 사용한다.

Q. Compound Component 패턴을 꼭 써야 해?
A. 필수는 아니다. 복잡한 컴포넌트에서 조합 유연성이 필요할 때 적합하다.

Q. 컴포넌트를 많이 쪼개면 좋은 거야?
A. 아니다. 사용성이 떨어질 정도로 쪼개면 오히려 복잡해진다.

Q. 단순 컴포넌트도 composition이 필요해?
A. 대부분 필요 없다. Button, Badge 같은 단순 컴포넌트는 props 중심이 적합하다.

---

# 3. Variant Rules

## 3.1 Variant Definition

### [개념]

Variant는 같은 컴포넌트가 목적에 따라 다른 시각적 의미를 갖도록 하는 체계다.

Variant는 색상 이름이 아니라 UI 역할과 의미를 기준으로 작성해야 한다.

---

### [핵심]

권장 variant:

```text
primary
secondary
tertiary
danger
success
warning
info
ghost
outline
link
```

비권장 variant:

```text
blue
red
gray
bigBlue
nice
mainColor
subColor
```

Variant 기준:

- 의미 기반 이름 사용
- 색상 기반 이름 금지
- 컴포넌트별 허용 variant 제한
- danger는 위험 행동에만 사용
- primary는 주요 행동에만 사용
- variant별 state 정의 필요
- token과 연결 필요

---

### [실무]

Button Variant 기준:

```text
primary
→ 가장 중요한 주요 행동

secondary
→ 보조 행동

danger
→ 삭제 / 탈퇴 / 되돌릴 수 없는 위험 행동

ghost
→ 낮은 강조의 보조 행동
```

Badge Variant 기준:

```text
success
→ 성공 / 정상 / 완료

warning
→ 주의 / 마감 임박

error
→ 오류 / 실패 / 위험

info
→ 정보 / 안내
```

Review 기준:

```md
- [ ] variant 이름이 의미 기반인가?
- [ ] 색상 이름 variant가 아닌가?
- [ ] variant별 사용 기준이 있는가?
- [ ] variant별 state가 정의되어 있는가?
- [ ] token과 연결되어 있는가?
```

---

### [FAQ]

Q. Variant가 뭐야?
A. 같은 컴포넌트가 목적에 따라 다른 시각적 의미를 갖도록 하는 체계다.

Q. variant 이름을 blue, red로 해도 돼?
A. 권장하지 않는다. primary, secondary, danger처럼 역할 중심 이름이 좋다.

Q. danger variant는 언제 써?
A. 삭제, 탈퇴, 되돌릴 수 없는 위험 행동에 사용한다.

Q. primary variant는 여러 개 써도 돼?
A. 화면의 주요 행동을 강조하는 용도이므로 한 화면에 과도하게 많이 쓰지 않는 것이 좋다.

---

## 3.2 Variant Usage Rules

### [개념]

Variant Usage Rules는 각 variant를 언제 사용해야 하는지 정의하는 기준이다.

Variant 사용 기준이 없으면 Frontend Agent가 화면마다 다른 의미로 variant를 사용할 수 있다.

---

### [핵심]

Variant 사용 기준:

| Variant   | 사용 목적        | 예시             |
| --------- | ---------------- | ---------------- |
| primary   | 가장 중요한 행동 | 저장, 등록, 검색 |
| secondary | 보조 행동        | 취소, 뒤로가기   |
| danger    | 위험 행동        | 삭제, 탈퇴       |
| ghost     | 낮은 강조 행동   | 닫기, 보조 메뉴  |
| outline   | 중간 강조 행동   | 필터 열기        |
| success   | 성공 상태        | 완료, 정상       |
| warning   | 주의 상태        | 마감 임박        |
| error     | 오류 상태        | 실패, 오류       |
| info      | 안내 상태        | 공지, 도움말     |

---

### [실무]

좋은 예:

```jsx
<Button variant="primary">저장</Button>
<Button variant="secondary">취소</Button>
<Button variant="danger">삭제</Button>
```

나쁜 예:

```jsx
<Button variant="danger">검색</Button>
<Button variant="primary">닫기</Button>
<Button variant="success">삭제</Button>
```

Review 기준:

```md
- [ ] 주요 행동에 primary를 사용했는가?
- [ ] 위험 행동에 danger를 사용했는가?
- [ ] 단순 닫기 / 보조 행동에 primary를 남발하지 않는가?
- [ ] 상태 표시 variant와 행동 variant를 혼동하지 않는가?
```

---

### [FAQ]

Q. primary는 언제 써?
A. 화면에서 가장 중요한 주요 행동에 사용한다. 예: 저장, 등록, 검색.

Q. secondary는 언제 써?
A. 주요 행동을 보조하는 행동에 사용한다. 예: 취소, 뒤로가기.

Q. ghost는 언제 써?
A. 낮은 강조의 보조 행동이나 UI를 방해하지 않는 액션에 사용한다.

Q. success variant를 삭제 버튼에 써도 돼?
A. 안 된다. 삭제는 위험 행동이므로 danger variant가 적합하다.

---

## 3.3 Variant Token Mapping

### [개념]

Variant Token Mapping은 variant가 어떤 semantic token 또는 component token을 사용하는지 연결하는 규칙이다.

Variant와 token이 연결되어야 theme 변경과 Review Agent 검토가 가능하다.

---

### [핵심]

Button Token Mapping 예:

```text
primary
→ --button-primary-background
→ --button-primary-text
→ --button-primary-background-hover

secondary
→ --button-secondary-background
→ --button-secondary-text
→ --button-secondary-border

danger
→ --button-danger-background
→ --button-danger-text
→ --button-danger-background-hover

ghost
→ --button-ghost-background
→ --button-ghost-text
→ --button-ghost-background-hover
```

Badge Token Mapping 예:

```text
success
→ --badge-success-background
→ --badge-success-text

warning
→ --badge-warning-background
→ --badge-warning-text

error
→ --badge-error-background
→ --badge-error-text

info
→ --badge-info-background
→ --badge-info-text
```

---

### [실무]

CSS 예:

```css
.button[data-variant="primary"] {
  background: var(--button-primary-background);
  color: var(--button-primary-text);
}

.button[data-variant="danger"] {
  background: var(--button-danger-background);
  color: var(--button-danger-text);
}
```

Token 정의 예:

```css
:root {
  --button-primary-background: var(--color-primary);
  --button-primary-text: var(--color-on-primary);

  --button-danger-background: var(--color-error);
  --button-danger-text: var(--color-on-error);
}
```

Review 기준:

```md
- [ ] variant가 token과 연결되어 있는가?
- [ ] raw color를 직접 사용하지 않는가?
- [ ] hover / active / disabled state token이 있는가?
- [ ] dark mode에서도 variant 의미가 유지되는가?
```

---

### [FAQ]

Q. Variant Token Mapping이 왜 필요해?
A. variant 의미와 실제 스타일 token을 연결해 theme 변경과 리뷰를 안정적으로 하기 위해 필요하다.

Q. variant마다 hover token도 필요해?
A. 권장된다. 상태 표현이 화면마다 달라지는 것을 막을 수 있다.

Q. danger variant는 어떤 token과 연결돼?
A. 보통 `--color-error` 또는 `--button-danger-background`와 연결된다.

Q. variant에 raw color를 직접 써도 돼?
A. 공통 컴포넌트에서는 피해야 한다. token을 사용하는 것이 좋다.

---

## 3.4 Variant Mistakes

### [개념]

Variant Mistakes는 variant를 의미 없이 늘리거나 색상 기준으로 사용하는 실수다.

Variant 실수는 컴포넌트 일관성과 사용 기준을 무너뜨린다.

---

### [핵심]

자주 발생하는 실수:

- `blue`, `red`, `gray` variant 사용
- variant가 너무 많음
- primary를 모든 버튼에 사용
- danger를 위험 행동 외에 사용
- success를 행동 버튼에 남용
- variant별 state 누락
- variant별 token mapping 없음
- 화면 전용 variant 남발
- 이름은 다르지만 스타일이 같은 variant 존재
- 사용 기준 없는 variant 추가

---

### [실무]

Troubleshooting:

```text
버튼 스타일이 너무 많음
→ variant 축소 / usage 기준 정리

primary 버튼이 너무 많음
→ 주요 CTA만 primary 유지

danger가 일반 행동에 사용됨
→ 위험 행동만 danger로 제한

색상명 variant가 있음
→ semantic variant로 변경

variant별 hover가 다름
→ state token mapping 확인
```

Review Checklist:

```md
- [ ] variant 이름이 의미 기반인가?
- [ ] variant 개수가 과도하지 않은가?
- [ ] 사용 기준이 문서화되어 있는가?
- [ ] variant별 state가 정의되어 있는가?
- [ ] token mapping이 있는가?
```

---

### [FAQ]

Q. variant가 많아지면 좋은 거 아니야?
A. 아니다. variant가 너무 많으면 선택 기준이 흐려지고 유지보수가 어려워진다.

Q. 색상별 variant를 만들면 안 돼?
A. 권장하지 않는다. 색상보다 역할과 의미 기준으로 variant를 만들어야 한다.

Q. 화면 전용 variant를 만들어도 돼?
A. 반복 사용되지 않는 화면 전용 variant는 피하고 기존 variant로 해결 가능한지 먼저 확인한다.

Q. primary를 여러 개 쓰면 문제야?
A. 주요 행동이 흐려질 수 있다. 화면의 핵심 CTA 중심으로 제한하는 것이 좋다.

---

# 4. Size Rules

## 4.1 Size Definition

### [개념]

Size는 컴포넌트의 크기 체계다.

Size는 height, padding, font-size, icon-size, radius, gap 같은 값을 함께 정의해야 한다.

---

### [핵심]

권장 size:

```text
sm
md
lg
```

필요 시 확장:

```text
xs
xl
```

Size 기준:

- size 이름은 컴포넌트 전체에서 일관
- height / padding / font-size 함께 정의
- touch target 고려
- 모바일 조작 가능성 고려
- 임의 px 크기 남발 금지
- size별 token 사용 권장

---

### [실무]

Button size 기준:

```css
.button[data-size="sm"] {
  height: 32px;
  padding: 0 var(--spacing-3);
  font-size: var(--font-size-sm);
}

.button[data-size="md"] {
  height: 40px;
  padding: 0 var(--spacing-4);
  font-size: var(--font-size-md);
}

.button[data-size="lg"] {
  height: 48px;
  padding: 0 var(--spacing-6);
  font-size: var(--font-size-lg);
}
```

Input size 기준:

```css
.input[data-size="sm"] {
  height: 32px;
  font-size: var(--font-size-sm);
}

.input[data-size="md"] {
  height: 40px;
  font-size: var(--font-size-md);
}

.input[data-size="lg"] {
  height: 48px;
  font-size: var(--font-size-lg);
}
```

---

### [FAQ]

Q. Size는 어떻게 나눠?
A. 기본적으로 sm, md, lg를 사용하고 필요 시 xs, xl을 추가한다.

Q. Button 크기를 매번 직접 지정해도 돼?
A. 권장하지 않는다. size prop과 token으로 관리하는 것이 일관성에 좋다.

Q. size에는 height만 정의하면 돼?
A. 아니다. height, padding, font-size, icon-size 등을 함께 정의해야 한다.

Q. 모바일에서 size가 중요한 이유는?
A. 터치 가능한 충분한 영역을 제공해야 하기 때문이다.

---

## 4.2 Size Token Mapping

### [개념]

Size Token Mapping은 size prop이 실제 component token과 어떻게 연결되는지 정의하는 규칙이다.

Size와 token을 연결하면 컴포넌트 크기를 일관되게 관리할 수 있다.

---

### [핵심]

Button Size Token 예:

```text
sm
→ --button-height-sm
→ --button-padding-x-sm
→ --button-font-size-sm

md
→ --button-height-md
→ --button-padding-x-md
→ --button-font-size-md

lg
→ --button-height-lg
→ --button-padding-x-lg
→ --button-font-size-lg
```

Input Size Token 예:

```text
sm
→ --input-height-sm
→ --input-padding-x-sm
→ --input-font-size-sm

md
→ --input-height-md
→ --input-padding-x-md
→ --input-font-size-md

lg
→ --input-height-lg
→ --input-padding-x-lg
→ --input-font-size-lg
```

---

### [실무]

Token 정의 예:

```css
:root {
  --button-height-sm: 32px;
  --button-height-md: 40px;
  --button-height-lg: 48px;

  --button-padding-x-sm: var(--spacing-3);
  --button-padding-x-md: var(--spacing-4);
  --button-padding-x-lg: var(--spacing-6);

  --button-font-size-sm: var(--font-size-sm);
  --button-font-size-md: var(--font-size-md);
  --button-font-size-lg: var(--font-size-lg);
}
```

사용 예:

```css
.button[data-size="md"] {
  height: var(--button-height-md);
  padding-inline: var(--button-padding-x-md);
  font-size: var(--button-font-size-md);
}
```

Review 기준:

```md
- [ ] size prop이 token과 연결되어 있는가?
- [ ] height / padding / font-size가 함께 정의되는가?
- [ ] 임의 size 값이 직접 사용되지 않는가?
- [ ] sm / md / lg 기준이 일관적인가?
```

---

### [FAQ]

Q. Size Token Mapping이 왜 필요해?
A. size prop과 실제 스타일 값을 연결해 컴포넌트 크기를 일관되게 관리하기 위해 필요하다.

Q. size마다 font-size도 바꿔야 해?
A. 대부분 그렇다. height와 padding만 바꾸면 시각 균형이 깨질 수 있다.

Q. size token은 component token이야?
A. 보통 특정 컴포넌트 크기를 다루므로 component token에 가깝다.

Q. 모든 컴포넌트가 sm, md, lg를 가져야 해?
A. 필수는 아니다. 하지만 공통 interactive component는 일관된 size 체계를 갖는 것이 좋다.

---

## 4.3 Touch Target Rules

### [개념]

Touch Target Rules는 모바일과 터치 환경에서 사용자가 버튼, 링크, 입력 요소를 쉽게 누를 수 있도록 하는 기준이다.

Size Rule은 시각 크기뿐 아니라 실제 조작 가능 영역까지 고려해야 한다.

---

### [핵심]

Touch Target 기준:

- 모바일 interactive element는 충분한 높이 필요
- 너무 작은 icon button 금지
- 클릭 영역과 시각 영역 구분 가능
- 인접 버튼 사이 간격 확보
- disabled 상태도 영역 유지
- focus 영역과 click 영역 일치 권장

권장:

```text
Button md
→ 40px 이상

Button lg
→ 48px 권장

Icon Button
→ 최소 40px 전후 권장

Form Input
→ 40px 이상 권장
```

---

### [실무]

Icon Button 예:

```css
.iconButton {
  width: 40px;
  height: 40px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
```

나쁜 예:

```css
.iconButton {
  width: 20px;
  height: 20px;
}
```

Review 기준:

```md
- [ ] 모바일에서 버튼을 누르기 충분한가?
- [ ] icon button 클릭 영역이 너무 작지 않은가?
- [ ] 인접한 interactive element 간격이 충분한가?
- [ ] focus-visible 영역이 조작 영역과 일치하는가?
```

---

### [FAQ]

Q. Touch Target이 뭐야?
A. 사용자가 터치하거나 클릭할 수 있는 실제 조작 영역이다.

Q. 모바일 버튼 높이는 중요해?
A. 중요하다. 터치 가능한 충분한 영역을 제공해야 한다.

Q. 아이콘 버튼은 아이콘 크기만큼만 클릭되면 돼?
A. 아니다. 아이콘보다 넓은 조작 영역을 제공하는 것이 좋다.

Q. 작은 버튼은 언제 사용해?
A. 밀도가 높은 UI에서 사용할 수 있지만 모바일과 접근성 기준을 함께 확인해야 한다.

---

## 4.4 Size Mistakes

### [개념]

Size Mistakes는 컴포넌트 크기를 일관성 없이 정의할 때 발생하는 실수다.

Size 실수는 UI 밀도, 접근성, 모바일 사용성 문제로 이어진다.

---

### [핵심]

자주 발생하는 실수:

- 임의 height 값 남발
- sm / md / lg 기준 없음
- size마다 font-size 불일치
- Button과 Input 높이 불일치
- icon button 클릭 영역이 작음
- 모바일 touch target 부족
- padding만 바꾸고 height 미정의
- size prop 없이 className으로 크기 변경
- 같은 size 이름이 컴포넌트마다 다른 의미로 사용됨

---

### [실무]

Troubleshooting:

```text
버튼 크기가 화면마다 다름
→ Button size token 확인

Input과 Button 높이가 안 맞음
→ md height 기준 통일

아이콘 버튼 누르기 어려움
→ touch target size 확인

모바일에서 조작이 어려움
→ interactive element height 확인

sm / md / lg 의미가 다름
→ size naming rule 재정의
```

Review Checklist:

```md
- [ ] size 이름이 일관적인가?
- [ ] height / padding / font-size가 함께 정의되는가?
- [ ] 터치 영역이 충분한가?
- [ ] sm / md / lg 외 임의 크기가 남발되지 않는가?
```

---

### [FAQ]

Q. Size에서 가장 흔한 실수는?
A. height, padding, font-size를 각각 임의로 지정해 컴포넌트 크기가 제각각이 되는 것이다.

Q. Button과 Input 높이는 맞춰야 해?
A. 같은 form line에 배치된다면 md 기준 높이를 맞추는 것이 좋다.

Q. size prop 없이 className으로 크기를 바꿔도 돼?
A. 공통 컴포넌트에서는 권장하지 않는다. size prop과 token을 사용하는 것이 좋다.

Q. icon button 크기가 작으면 왜 문제야?
A. 터치와 키보드 focus 사용성이 떨어지고 접근성 문제가 생길 수 있다.

---

# 5. State Rules

## 5.1 Component State Definition

### [개념]

Component State는 컴포넌트가 현재 어떤 상태인지 표현하는 규칙이다.

State는 시각 스타일뿐 아니라 동작, 접근성 속성, 사용자 피드백을 함께 포함한다.

---

### [핵심]

필수 state:

```text
default
hover
active
focus
disabled
loading
error
success
selected
checked
open
closed
readonly
```

컴포넌트별 필수 상태:

| Component | Required States                                    |
| --------- | -------------------------------------------------- |
| Button    | default, hover, active, focus, disabled, loading   |
| Input     | default, focus, disabled, readonly, error, success |
| Modal     | open, closed, loading, error, focus                |
| Tab       | default, hover, selected, focus, disabled          |
| Toast     | info, success, warning, error                      |
| Checkbox  | unchecked, checked, disabled, focus                |
| Radio     | unchecked, checked, disabled, focus                |
| Select    | default, open, selected, disabled, error, focus    |

---

### [실무]

Button loading state:

```text
Button loading
→ spinner 또는 loading text 표시
→ disabled 처리
→ aria-busy 설정 고려
→ 중복 클릭 방지
```

Input error state:

```text
Input error
→ border error color
→ error message 표시
→ aria-invalid=true
→ aria-describedby 연결
```

Modal open state:

```text
Modal open
→ role dialog
→ aria-modal true
→ focus trap 고려
→ background scroll lock
```

---

### [FAQ]

Q. Component State가 뭐야?
A. default, hover, focus, disabled, loading, error처럼 컴포넌트의 현재 상태를 표현하는 규칙이다.

Q. hover만 있으면 충분해?
A. 아니다. focus, disabled, loading, error 같은 상태도 필요하다.

Q. state는 스타일만 정의하면 돼?
A. 아니다. 동작, 접근성 속성, 사용자 피드백까지 함께 정의해야 한다.

Q. loading 상태는 왜 필요해?
A. 사용자의 중복 클릭을 막고 처리 중임을 알리기 위해 필요하다.

---

## 5.2 Interactive State Rules

### [개념]

Interactive State Rules는 사용자가 조작하는 컴포넌트의 hover, active, focus, disabled 상태를 정의하는 기준이다.

Interactive State는 사용자가 조작 가능 여부와 현재 위치를 이해하게 만든다.

---

### [핵심]

Interactive State:

```text
hover
→ 마우스가 요소 위에 있음

active
→ 클릭 또는 터치가 진행 중

focus
→ 키보드 또는 보조기기 focus 위치

disabled
→ 조작 불가능 상태

readonly
→ 값은 읽을 수 있지만 수정 불가
```

기준:

- hover와 active 스타일 구분
- focus-visible 필수
- disabled는 조작 차단
- disabled와 readonly 구분
- 색상만으로 상태 전달 금지
- cursor와 aria 속성 고려

---

### [실무]

Button interactive state 예:

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

Input readonly / disabled 구분:

```jsx
<input readOnly value={value} />
<input disabled value={value} />
```

Review 기준:

```md
- [ ] hover / active / focus state가 정의되어 있는가?
- [ ] focus-visible이 보이는가?
- [ ] disabled와 readonly가 구분되는가?
- [ ] interactive element가 키보드로 조작 가능한가?
```

---

### [FAQ]

Q. focus와 hover는 뭐가 달라?
A. hover는 마우스 상태이고 focus는 키보드나 보조기기 사용자의 현재 위치다.

Q. focus-visible은 꼭 필요해?
A. 필요하다. 키보드 사용자가 현재 위치를 알 수 있어야 한다.

Q. disabled와 readonly는 뭐가 달라?
A. disabled는 조작과 제출에서 제외되고, readonly는 수정은 불가하지만 값은 읽을 수 있다.

Q. disabled 상태에 onClick이 있어도 돼?
A. disabled 상태에서는 조작이 실행되지 않아야 한다.

---

## 5.3 Feedback State Rules

### [개념]

Feedback State Rules는 사용자의 행동이나 시스템 요청 결과를 표시하는 loading, error, success, empty 상태 기준이다.

Feedback State는 사용자가 현재 상황과 다음 행동을 알 수 있게 한다.

---

### [핵심]

Feedback State:

```text
loading
→ 처리 중

error
→ 실패 / 오류

success
→ 성공 / 완료

empty
→ 요청 성공, 데이터 없음

submitting
→ form 제출 중

retrying
→ 재시도 중
```

기준:

- loading 중 중복 행동 방지
- error는 복구 행동 제공
- success는 작업 완료 명확화
- empty는 다음 행동 제공
- form error는 필드 가까이에 표시
- 중요 오류를 toast만으로 처리하지 않음

---

### [실무]

Loading Button 예:

```jsx
<Button isLoading={isSubmitting} disabled={isSubmitting}>
  저장
</Button>
```

Error State 예:

```jsx
<ErrorState
  title="데이터를 불러오지 못했습니다"
  description="네트워크 상태를 확인한 뒤 다시 시도해 주세요."
  action={<Button onClick={refetch}>다시 시도</Button>}
/>
```

Empty State 예:

```jsx
<EmptyState
  title="검색 결과가 없습니다"
  description="다른 키워드나 지역으로 다시 검색해 보세요."
/>
```

---

### [FAQ]

Q. Feedback State는 왜 필요해?
A. 사용자가 처리 중, 성공, 실패, 데이터 없음 상태를 이해할 수 있어야 하기 때문이다.

Q. loading 중에는 버튼을 disabled 처리해야 해?
A. 대부분 그렇다. 중복 클릭과 중복 API 요청을 막기 위해 필요하다.

Q. error state에는 무엇이 필요해?
A. 사용자 친화적 메시지와 가능한 경우 복구 action이 필요하다.

Q. empty state에는 무엇이 필요해?
A. 데이터가 없다는 설명과 다음 행동 안내가 필요하다.

---

## 5.4 Selection State Rules

### [개념]

Selection State Rules는 selected, checked, active tab, current page 같은 선택 상태를 표현하는 기준이다.

Selection State는 사용자가 현재 선택된 항목을 명확히 알 수 있게 한다.

---

### [핵심]

Selection State 대상:

- Tabs selected
- Checkbox checked
- Radio checked
- Select selected option
- Pagination current page
- Navigation active link
- Table selected row
- Filter selected chip

기준:

- 선택 상태가 시각적으로 명확
- 선택 상태가 접근성 속성과 연결
- 색상만으로 선택 표시 금지
- keyboard 조작 가능
- current / selected naming 일관
- URL 상태 연동 필요성 검토

---

### [실무]

Tab selected 예:

```jsx
<button role="tab" aria-selected={isSelected} aria-controls="panel-info">
  기본 정보
</button>
```

Pagination current 예:

```jsx
<button aria-current={page === currentPage ? "page" : undefined}>{page}</button>
```

Checkbox checked 예:

```jsx
<input type="checkbox" checked={checked} onChange={handleChange} />
```

Review 기준:

```md
- [ ] selected / checked 상태가 명확한가?
- [ ] aria-selected 또는 aria-current가 필요한 곳에 있는가?
- [ ] keyboard 조작이 가능한가?
- [ ] 선택 상태를 색상만으로 표현하지 않는가?
```

---

### [FAQ]

Q. Selection State가 뭐야?
A. selected, checked, current처럼 현재 선택된 항목을 표현하는 상태다.

Q. 선택 상태는 색상만으로 표시해도 돼?
A. 안 된다. 텍스트, 아이콘, 위치, aria 속성 등 추가 정보가 필요하다.

Q. 현재 페이지는 어떻게 표시해?
A. 시각적으로 강조하고 `aria-current="page"` 사용을 고려한다.

Q. Tab 선택 상태는 어떻게 표현해?
A. 선택된 tab에 `aria-selected`를 연결하고 panel과 관계를 명확히 한다.

---

## 5.5 State Mistakes

### [개념]

State Mistakes는 컴포넌트 상태를 누락하거나 스타일만 정의하고 동작 / 접근성을 놓치는 실수다.

State 실수는 사용자 피드백 부족, 접근성 문제, 중복 요청 문제를 만든다.

---

### [핵심]

자주 발생하는 실수:

- hover만 있고 focus 없음
- loading 중 중복 클릭 가능
- disabled 스타일만 있고 실제 disabled 아님
- error 색상만 있고 error message 없음
- input error와 aria 속성 연결 없음
- selected 상태가 색상으로만 표시됨
- modal open 상태에서 focus 관리 없음
- toast만 있고 화면 내 error 없음
- empty state 없이 빈 화면 표시
- success feedback 없음
- readonly와 disabled 혼동

---

### [실무]

Troubleshooting:

```text
키보드 위치를 알 수 없음
→ focus-visible 확인

저장 버튼 중복 클릭됨
→ loading + disabled 확인

입력 오류가 전달되지 않음
→ errorMessage + aria-invalid 확인

목록이 빈 화면임
→ Empty State 추가

선택 상태가 모호함
→ selected style + aria-current 확인
```

Review Checklist:

```md
- [ ] hover / active / focus / disabled 상태가 있는가?
- [ ] loading 중 중복 클릭이 방지되는가?
- [ ] error state가 메시지와 접근성 속성을 포함하는가?
- [ ] empty state가 있는가?
- [ ] selected / checked 상태가 명확한가?
```

---

### [FAQ]

Q. State에서 가장 흔한 실수는?
A. hover만 만들고 focus, disabled, loading, error 상태를 누락하는 것이다.

Q. disabled 스타일만 넣으면 충분해?
A. 아니다. 실제 disabled 속성이나 조작 차단 로직이 필요하다.

Q. error는 빨간 border만 있으면 돼?
A. 아니다. error message와 aria 속성 연결이 필요하다.

Q. empty state 없이 빈 화면이어도 돼?
A. 안 된다. 사용자는 오류인지 결과 없음인지 알 수 없다.

---

# 6. Accessibility Specification Rules

## 6.1 Accessibility Spec Definition

### [개념]

Accessibility Specification은 컴포넌트가 기본적으로 접근성을 만족하도록 하는 기준이다.

공통 컴포넌트가 접근성을 갖추면 전체 화면의 접근성 품질이 안정된다.

---

### [핵심]

Component Accessibility 필수 기준:

- Semantic HTML
- Keyboard Navigation
- Focus Visible
- Accessible Name
- Label Association
- Error Message Association
- ARIA 최소 사용
- Color Contrast
- Modal Focus Management
- Reduced Motion
- Touch Target Size

컴포넌트별 기준:

```text
Button
→ button 요소, focus-visible, loading 상태, icon button aria-label

Input
→ label 연결, error message 연결, aria-invalid

Modal
→ role dialog, aria-modal, title 연결, focus 관리

Tabs
→ role tablist / tab / tabpanel 또는 접근 가능한 구조

Table
→ th, scope, caption 필요성 검토
```

---

### [실무]

Button 접근성 예:

```jsx
<button type="button" aria-busy={isLoading}>
  {isLoading ? "처리 중..." : "저장"}
</button>
```

Icon Button 접근성 예:

```jsx
<button type="button" aria-label="검색">
  <SearchIcon aria-hidden="true" />
</button>
```

Input Error 접근성 예:

```jsx
<input
  id="email"
  name="email"
  aria-invalid="true"
  aria-describedby="email-error"
/>
<p id="email-error" role="alert">
  올바른 이메일 형식이 아닙니다.
</p>
```

---

### [FAQ]

Q. Accessibility Specification이 뭐야?
A. 컴포넌트가 기본적으로 접근성을 만족하도록 하는 기준이다.

Q. 공통 컴포넌트에 접근성이 필요한 이유는?
A. 공통 컴포넌트가 접근성을 갖추면 전체 화면 품질이 올라가기 때문이다.

Q. aria를 많이 넣으면 접근성이 좋아져?
A. 아니다. Semantic HTML을 우선 사용하고 부족한 의미를 보완할 때만 aria를 사용한다.

Q. icon button에는 무엇이 필요해?
A. `aria-label` 또는 스크린 리더용 텍스트가 필요하다.

---

## 6.2 Label and Error Association Rules

### [개념]

Label and Error Association Rules는 입력 컴포넌트에서 label, input, helper text, error message를 올바르게 연결하는 기준이다.

---

### [핵심]

Form 접근성 기준:

- label과 input 연결
- placeholder를 label 대체로 사용 금지
- error message를 input과 연결
- helper text와 error message 구분
- required 표시 명확화
- aria-invalid 사용
- aria-describedby 사용
- 동적 error는 role alert 고려

---

### [실무]

좋은 예:

```jsx
<label htmlFor="password">비밀번호</label>
<input
  id="password"
  name="password"
  type="password"
  aria-invalid={Boolean(errorMessage)}
  aria-describedby={errorMessage ? "password-error" : "password-help"}
/>
<p id="password-help">8자 이상 입력해 주세요.</p>
{errorMessage && (
  <p id="password-error" role="alert">
    {errorMessage}
  </p>
)}
```

나쁜 예:

```jsx
<input placeholder="비밀번호" />
<p>비밀번호가 짧습니다.</p>
```

Review 기준:

```md
- [ ] label과 input이 연결되어 있는가?
- [ ] placeholder를 label 대체로 사용하지 않는가?
- [ ] error message가 input과 연결되어 있는가?
- [ ] helper text와 error text가 구분되는가?
```

---

### [FAQ]

Q. placeholder만 있으면 label은 없어도 돼?
A. 권장하지 않는다. placeholder는 입력 예시이고 label은 입력 항목의 이름이다.

Q. error message는 input과 연결해야 해?
A. 해야 한다. `aria-describedby`로 연결하면 스크린 리더 사용자가 오류를 알 수 있다.

Q. aria-invalid는 언제 써?
A. 입력값이 오류 상태일 때 `aria-invalid="true"`를 사용한다.

Q. helper text와 error message는 구분해야 해?
A. 구분해야 한다. helper text는 안내이고 error message는 오류 상태다.

---

## 6.3 Keyboard and Focus Rules

### [개념]

Keyboard and Focus Rules는 사용자가 키보드만으로 컴포넌트를 탐색하고 조작할 수 있게 하는 기준이다.

---

### [핵심]

기본 기준:

- interactive element는 keyboard 접근 가능
- focus-visible 스타일 제공
- focus outline 제거 금지
- Modal focus trap 고려
- Modal 닫힌 후 이전 focus 복원
- Dropdown / Select ESC 닫기 고려
- Tabs 방향키 이동 고려
- Button Enter / Space 실행
- Link Enter 이동

---

### [실무]

Focus style 예:

```css
:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}
```

Modal focus 기준:

```text
Modal Open
→ 첫 번째 focusable element로 focus 이동
→ focus trap 적용
→ ESC 닫기 정책 적용
→ Close 후 trigger element로 focus 복원
```

Review 기준:

```md
- [ ] keyboard만으로 조작 가능한가?
- [ ] focus-visible이 보이는가?
- [ ] modal focus 관리가 있는가?
- [ ] custom control이 native 접근성을 유지하는가?
```

---

### [FAQ]

Q. 모든 컴포넌트를 키보드로 조작 가능해야 해?
A. 사용자가 조작하는 interactive component는 키보드 접근이 가능해야 한다.

Q. focus outline을 제거해도 돼?
A. 제거만 하면 안 된다. 반드시 대체 focus-visible style을 제공해야 한다.

Q. Modal 접근성에서 중요한 것은?
A. dialog 역할, title 연결, focus trap, ESC 닫기, focus 복원이다.

Q. custom button을 div로 만들어도 돼?
A. 권장하지 않는다. 가능한 native button 요소를 사용한다.

---

# 7. Usage Documentation Rules

## 7.1 Usage Rules

### [개념]

Usage Rules는 컴포넌트를 언제 사용하고 언제 사용하지 않아야 하는지 정의하는 기준이다.

Usage Rules가 없으면 같은 컴포넌트가 화면마다 다른 의미로 사용된다.

---

### [핵심]

Usage 문서에 포함할 항목:

- 사용 목적
- 사용 상황
- 사용하지 말아야 할 상황
- variant 선택 기준
- size 선택 기준
- state 처리 기준
- 접근성 기준
- 예시 코드
- domain 예시

Button Usage 예:

```text
사용
→ 저장, 등록, 삭제, 검색 같은 사용자 행동 실행

사용 금지
→ 단순 페이지 이동 링크를 Button으로 표현
```

Card Usage 예:

```text
사용
→ 관련 정보를 하나의 시각적 그룹으로 묶을 때

사용 금지
→ 단순 레이아웃 간격 조절용 박스로 사용
```

---

### [실무]

좋은 Usage 문서 예:

```md
## Button Usage

### Use When

- 사용자가 명확한 행동을 실행해야 할 때
- 저장, 등록, 삭제, 검색, 다시 시도 액션이 있을 때

### Don't Use When

- 단순 페이지 이동이면 Link 사용
- 상태 표시만 필요하면 Badge 사용
```

Review 기준:

```md
- [ ] 컴포넌트 사용 목적이 명확한가?
- [ ] 사용 금지 상황이 정의되어 있는가?
- [ ] variant 선택 기준이 있는가?
- [ ] domain 예시가 포함되어 있는가?
```

---

### [FAQ]

Q. Usage Rules가 왜 필요해?
A. 컴포넌트를 언제 어떻게 써야 하는지 명확히 해 UI 의미 혼선을 줄이기 위해 필요하다.

Q. Button과 Link는 어떻게 구분해?
A. 행동 실행은 Button, 페이지 이동은 Link를 사용한다.

Q. Card는 언제 써?
A. 관련 정보를 하나의 시각적 그룹으로 묶어 보여줄 때 사용한다.

Q. Usage 문서에 domain 예시가 필요해?
A. 좋다. Agent가 실제 프로젝트 맥락에서 컴포넌트를 선택하기 쉬워진다.

---

## 7.2 Do and Don't Rules

### [개념]

Do and Don't Rules는 컴포넌트의 좋은 사용과 나쁜 사용을 명확히 구분하는 문서화 규칙이다.

Do / Don't는 RAG Retrieval에서 Review Agent의 반려 기준으로 사용된다.

---

### [핵심]

Do / Don't 작성 기준:

- 짧고 직접적으로 작성
- 실제 오류 사례 포함
- variant / size / state 기준 포함
- accessibility 기준 포함
- token 사용 기준 포함
- domain 예시 포함 가능

Button Do:

```md
- 저장, 삭제, 검색처럼 명확한 동사를 사용한다.
- loading 중에는 disabled 처리한다.
- form submit에는 `type="submit"`을 명시한다.
```

Button Don't:

```md
- 링크 이동에 Button을 사용하지 않는다.
- danger variant를 일반 행동에 사용하지 않는다.
- icon button에 accessible name을 누락하지 않는다.
```

---

### [실무]

Input Do / Don't 예:

```md
## Do

- label을 반드시 제공한다.
- errorMessage를 input과 연결한다.
- disabled와 readonly를 구분한다.

## Don't

- placeholder를 label 대체로 사용하지 않는다.
- error를 색상만으로 표시하지 않는다.
- raw error message를 그대로 노출하지 않는다.
```

Modal Do / Don't 예:

```md
## Do

- modal title을 제공한다.
- 닫기 버튼을 제공한다.
- focus trap과 focus 복원을 고려한다.

## Don't

- 닫을 방법 없는 modal을 만들지 않는다.
- 중요한 입력 중 overlay click으로 실수 닫힘을 만들지 않는다.
```

---

### [FAQ]

Q. Do / Don't가 왜 필요해?
A. 좋은 사용과 나쁜 사용을 명확히 해 Frontend Agent 생성과 Review Agent 검토 기준으로 쓰기 위해 필요하다.

Q. Don't에는 어떤 내용을 넣어야 해?
A. 자주 발생하는 실수, 접근성 문제, 잘못된 variant 사용, token 미사용 사례를 넣는다.

Q. Do / Don't는 길게 써야 해?
A. 아니다. 짧고 직접적으로 작성해야 검색과 리뷰에 유리하다.

Q. Do / Don't는 모든 컴포넌트에 필요해?
A. 공통 컴포넌트에는 권장된다. Button, Input, Modal에는 반드시 필요하다.

---

## 7.3 Example Rules

### [개념]

Example Rules는 Component Specification에 포함되는 예제 코드 작성 기준이다.

예제는 Frontend Agent가 바로 코드 생성과 리뷰에 활용할 수 있어야 한다.

---

### [핵심]

좋은 예제 조건:

- 짧고 직접적
- variant 포함
- size 포함
- state 포함
- accessibility 반영
- token 사용
- 실제 domain 예시 포함
- 나쁜 예와 좋은 예 구분

좋은 예:

```jsx
<Button variant="primary" size="md" type="submit" isLoading={isSubmitting}>
  저장
</Button>
```

나쁜 예:

```jsx
<Button blue big flag>
  OK
</Button>
```

---

### [실무]

Form Field 예:

```jsx
<FormField
  id="email"
  label="이메일"
  helperText="로그인에 사용할 이메일을 입력해 주세요."
  errorMessage={emailError}
>
  <TextInput id="email" name="email" value={email} onChange={setEmail} />
</FormField>
```

Modal 예:

```jsx
<Modal isOpen={isOpen} title="삭제 확인" onClose={closeModal}>
  <p>삭제한 데이터는 복구할 수 없습니다.</p>
  <Button variant="danger" onClick={handleDelete}>
    삭제
  </Button>
</Modal>
```

Review 기준:

```md
- [ ] 예제가 실제 사용 가능한가?
- [ ] variant / size / state가 포함되어 있는가?
- [ ] 접근성 기준이 반영되어 있는가?
- [ ] 너무 긴 boilerplate가 아닌가?
```

---

### [FAQ]

Q. 예제 코드는 길수록 좋아?
A. 아니다. RAG 문서에서는 짧고 검색 가능한 예제가 더 좋다.

Q. 예제에 접근성을 포함해야 해?
A. 해야 한다. icon button, form field, modal 같은 컴포넌트는 접근성 예제를 포함하는 것이 좋다.

Q. 나쁜 예도 필요해?
A. 필요하다. Review Agent가 반려 기준을 잡는 데 도움이 된다.

Q. 예제는 실제 도메인과 연결해야 해?
A. 가능하면 좋다. Agent가 프로젝트 맥락에 맞는 UI를 생성하기 쉬워진다.

---

# 8. Component Documentation Template

## 8.1 Component Document Template

### [개념]

Component Document Template은 모든 공통 컴포넌트 문서가 따라야 하는 표준 구조다.

문서 구조가 통일되어야 RAG Retrieval과 Agent Review 품질이 안정된다.

---

### [핵심]

표준 Template:

```md
# Component Name

## Purpose

컴포넌트 목적.

## Anatomy

구조 요소.

## Props

props API.

## Variants

variant 목록과 사용 기준.

## Sizes

size 목록과 사용 기준.

## States

state 목록과 동작 기준.

## Accessibility

접근성 기준.

## Usage

사용 상황.

## Do

권장 사용.

## Don't

금지 사용.

## Examples

짧은 예제.
```

---

### [실무]

Button 문서 Template 예:

```md
# Button

## Purpose

사용자의 주요 행동을 실행한다.

## Variants

- primary: 가장 중요한 행동
- secondary: 보조 행동
- danger: 위험 행동
- ghost: 낮은 강조 행동

## Sizes

- sm
- md
- lg

## States

- default
- hover
- active
- focus
- disabled
- loading

## Accessibility

- button 요소 사용
- focus-visible 제공
- icon button은 accessible name 제공
- loading 중 aria-busy 고려

## Do

- 명확한 동사 사용
- loading 중 중복 클릭 방지

## Don't

- 페이지 이동에 Button 사용 금지
- danger를 일반 행동에 사용 금지
```

---

### [FAQ]

Q. Component Document Template이 왜 필요해?
A. 문서 구조를 통일해 RAG 검색과 Agent 검토 품질을 높이기 위해 필요하다.

Q. 모든 컴포넌트 문서가 같은 구조를 따라야 해?
A. 공통 컴포넌트는 같은 구조를 따르는 것이 좋다.

Q. Template에서 가장 중요한 항목은?
A. Purpose, Props, Variants, Sizes, States, Accessibility, Usage, Do / Don't, Examples다.

Q. Component 문서에 예제가 꼭 필요해?
A. 필요하다. Agent가 실제 코드 생성에 활용할 수 있어야 한다.

---

## 8.2 Props Table Rules

### [개념]

Props Table Rules는 컴포넌트 props를 표로 정리하는 기준이다.

Props Table은 Agent가 허용 props와 타입, 기본값, 설명을 빠르게 검색할 수 있게 한다.

---

### [핵심]

Props Table 필수 컬럼:

```md
| Prop | Type | Default | Required | Description |
| ---- | ---- | ------- | -------- | ----------- |
```

예:

```md
| Prop      | Type                                              | Default     | Required | Description            |
| --------- | ------------------------------------------------- | ----------- | -------- | ---------------------- |
| variant   | `"primary" \| "secondary" \| "danger" \| "ghost"` | `"primary"` | No       | Button visual priority |
| size      | `"sm" \| "md" \| "lg"`                            | `"md"`      | No       | Button size            |
| isLoading | `boolean`                                         | `false`     | No       | Loading state          |
| disabled  | `boolean`                                         | `false`     | No       | Disabled state         |
| onClick   | `() => void`                                      | -           | No       | Click handler          |
```

---

### [실무]

Props Table 작성 기준:

- Type은 가능한 정확히 작성
- Default 값 명시
- Required 여부 명시
- Description은 짧게 작성
- any 사용 지양
- variant / size union 명시
- accessibility props 포함

Review 기준:

```md
- [ ] props table이 있는가?
- [ ] type이 명확한가?
- [ ] default 값이 명시되어 있는가?
- [ ] required 여부가 명확한가?
- [ ] description이 짧고 직접적인가?
```

---

### [FAQ]

Q. Props Table은 왜 필요해?
A. Agent가 컴포넌트 API를 빠르게 검색하고 정확히 사용할 수 있게 하기 위해 필요하다.

Q. Type에는 union 값을 직접 써야 해?
A. variant, size처럼 허용 값이 제한되는 props는 union을 명확히 쓰는 것이 좋다.

Q. Default 값은 꼭 써야 해?
A. 권장된다. 기본 동작을 예측하기 쉽게 만든다.

Q. Description은 길게 써야 해?
A. 아니다. 짧고 직접적으로 작성하는 것이 RAG 검색에 유리하다.

---

## 8.3 Component Checklist Rules

### [개념]

Component Checklist Rules는 각 컴포넌트 문서 마지막에 포함할 검토 기준이다.

Checklist는 Review Agent가 승인 / 반려 판단을 할 때 사용한다.

---

### [핵심]

Component Checklist 항목:

```md
## Component Checklist

- [ ] Purpose가 명확한가?
- [ ] Props API가 명확한가?
- [ ] Variant 기준이 있는가?
- [ ] Size 기준이 있는가?
- [ ] State 기준이 있는가?
- [ ] Accessibility 기준이 있는가?
- [ ] Usage 기준이 있는가?
- [ ] Do / Don't가 있는가?
- [ ] Example이 있는가?
- [ ] Design Token과 연결되어 있는가?
```

---

### [실무]

Button Checklist 예:

```md
## Button Checklist

- [ ] 기본 type이 `button`인가?
- [ ] form submit에는 `type="submit"`을 명시하는가?
- [ ] variant가 의미 기반인가?
- [ ] size가 sm / md / lg로 제한되는가?
- [ ] loading 중 disabled 처리되는가?
- [ ] focus-visible이 제공되는가?
- [ ] icon button에 accessible name이 있는가?
```

Input Checklist 예:

```md
## Input Checklist

- [ ] label과 input이 연결되는가?
- [ ] placeholder를 label 대체로 쓰지 않는가?
- [ ] errorMessage가 input과 연결되는가?
- [ ] disabled와 readonly가 구분되는가?
- [ ] autocomplete 속성을 고려하는가?
```

---

### [FAQ]

Q. Component Checklist는 왜 필요해?
A. Review Agent가 컴포넌트 품질을 일관되게 검토하기 위해 필요하다.

Q. Checklist는 모든 컴포넌트에 필요해?
A. 공통 재사용 컴포넌트에는 권장된다.

Q. Checklist에는 무엇이 들어가야 해?
A. Purpose, Props, Variant, Size, State, Accessibility, Usage, Token 연결 여부가 들어가야 한다.

Q. Checklist는 코드 리뷰에도 사용할 수 있어?
A. 가능하다. Review Agent와 개발자 모두 검토 기준으로 사용할 수 있다.

---

# 9. Component Review Rules

## 9.1 Frontend Agent Component Generation Rules

### [개념]

Frontend Agent Component Generation Rules는 Frontend Agent가 컴포넌트를 생성할 때 따라야 하는 기준이다.

Frontend Agent는 Component Specification에 없는 구조와 스타일을 임의로 생성하지 않아야 한다.

---

### [핵심]

Frontend Agent 생성 기준:

- 기존 Component Specification 확인
- 기존 Design Token 사용
- variant / size 허용 값 준수
- required props 누락 금지
- state 처리 포함
- loading / error / disabled 고려
- accessibility 기본 적용
- className override 남용 금지
- raw style 직접 작성 최소화
- 새 컴포넌트 필요 시 목적 명시

---

### [실무]

Frontend Agent Flow:

```text
Requirement 분석
→ 기존 컴포넌트 검색
→ Component Specification 확인
→ props API 확인
→ variant / size / state 선택
→ accessibility 기준 적용
→ token 기반 스타일 적용
→ 예제와 비교
→ Output
```

생성 전 질문:

```md
- [ ] 기존 컴포넌트로 해결 가능한가?
- [ ] 어떤 variant가 적절한가?
- [ ] 어떤 size가 적절한가?
- [ ] loading / error / disabled 상태가 필요한가?
- [ ] 접근성 속성이 필요한가?
- [ ] token이 정의되어 있는가?
```

---

### [FAQ]

Q. Frontend Agent는 컴포넌트 생성 전에 무엇을 확인해야 해?
A. 기존 Component Specification, Design Token, variant, size, state, accessibility 기준을 확인해야 한다.

Q. 기존 컴포넌트가 있으면 새로 만들면 안 돼?
A. 공통 UI가 이미 있다면 재사용하는 것이 좋다. 새 컴포넌트는 목적이 명확해야 한다.

Q. Frontend Agent가 inline style을 써도 돼?
A. 공통 UI에서는 피해야 한다. token 기반 class 또는 component style을 사용하는 것이 좋다.

Q. required props를 누락하면 어떻게 돼?
A. 컴포넌트 동작과 접근성이 깨질 수 있으므로 Review Agent가 반려해야 한다.

---

## 9.2 Review Agent Component Checklist

### [개념]

Review Agent Component Checklist는 구현된 컴포넌트가 Component Specification을 따르는지 검토하는 기준이다.

Review Agent는 예쁜 UI보다 규격, 상태, 접근성, token 사용을 우선 검토한다.

---

### [핵심]

Review Checklist:

```md
## Component API

- [ ] props 이름이 명확한가?
- [ ] variant / size 값이 제한되어 있는가?
- [ ] event handler 이름이 일관적인가?
- [ ] required props가 누락되지 않았는가?

## Variant / Size

- [ ] variant가 의미 기반인가?
- [ ] variant 사용 기준이 적절한가?
- [ ] size 체계가 sm / md / lg 기준과 맞는가?
- [ ] size token과 연결되어 있는가?

## State

- [ ] hover / active / focus / disabled 상태가 있는가?
- [ ] loading 상태가 있는가?
- [ ] error state가 메시지와 연결되는가?
- [ ] selected / checked 상태가 명확한가?

## Accessibility

- [ ] semantic element를 사용하는가?
- [ ] label 연결이 있는가?
- [ ] focus-visible이 있는가?
- [ ] keyboard 조작이 가능한가?
- [ ] icon button accessible name이 있는가?

## Token

- [ ] raw color를 직접 사용하지 않는가?
- [ ] spacing token을 사용하는가?
- [ ] typography token을 사용하는가?
- [ ] component token 또는 semantic token과 연결되는가?
```

---

### [실무]

Review Decision:

```text
Approved
→ Component Specification 준수, 주요 상태와 접근성 문제 없음

Needs Fix
→ 일부 props / state / token 기준 미흡

Blocked
→ 접근성 심각 문제, 주요 상태 누락, variant 오용, 컴포넌트 사용 불가
```

Blocked 예:

```text
Input label 없음
Icon Button accessible name 없음
Button loading 중 중복 클릭 가능
Modal 닫기 불가
focus-visible 제거
danger action이 primary로 표시됨
```

---

### [FAQ]

Q. Review Agent는 컴포넌트에서 뭘 봐야 해?
A. Props API, variant, size, state, accessibility, token 사용, usage 기준을 확인해야 한다.

Q. UI가 예쁘면 승인해도 돼?
A. 아니다. Component Specification과 접근성 기준을 만족해야 한다.

Q. 어떤 경우 Blocked야?
A. 사용자 조작이 어렵거나 접근성 심각 문제, 주요 상태 누락, 잘못된 위험 행동 표현이 있으면 Blocked다.

Q. raw value가 있으면 무조건 반려야?
A. 공통 컴포넌트에서 반복 raw value가 많으면 반려 대상이다. 단발성 예외는 이유가 필요하다.

---

## 9.3 Component Change Rules

### [개념]

Component Change Rules는 기존 공통 컴포넌트에 props, variant, size, state를 추가하거나 변경할 때 적용하는 기준이다.

공통 컴포넌트 변경은 여러 화면에 영향을 줄 수 있으므로 신중해야 한다.

---

### [핵심]

변경 전 확인:

- 기존 variant로 해결 가능한가
- 기존 props로 해결 가능한가
- 새 props가 컴포넌트 목적과 맞는가
- 새 variant가 의미 기반인가
- 새 size가 정말 필요한가
- 기존 화면에 breaking change가 없는가
- accessibility 영향이 없는가
- token mapping이 추가되었는가
- documentation이 업데이트되었는가
- examples가 업데이트되었는가

---

### [실무]

새 variant 추가 Flow:

```text
요구사항 확인
→ 기존 variant 검토
→ 새 variant 필요성 확인
→ variant 이름 의미 검토
→ token mapping 추가
→ state 정의
→ documentation 업데이트
→ examples 추가
→ Review Agent 검토
```

나쁜 변경:

```text
Button에 blue2 variant 추가
→ 사용 기준 없음
→ token mapping 없음
→ hover / disabled state 없음
```

좋은 변경:

```text
Button에 outline variant 추가
→ 중간 강조 보조 행동 목적
→ token mapping 있음
→ hover / focus / disabled state 있음
→ docs / examples 업데이트
```

---

### [FAQ]

Q. 공통 컴포넌트에 props를 쉽게 추가해도 돼?
A. 신중해야 한다. props가 늘어나면 API가 복잡해지고 유지보수가 어려워진다.

Q. 새 variant를 추가할 때 필요한 것은?
A. 사용 목적, 의미 기반 이름, token mapping, state, documentation, example이 필요하다.

Q. 기존 variant로 해결 가능하면 어떻게 해?
A. 새 variant를 만들지 않고 기존 variant를 사용하는 것이 좋다.

Q. component 변경 시 문서도 수정해야 해?
A. 해야 한다. Component Specification과 예제를 함께 업데이트해야 한다.

---

# 10. Final Checklist

## 10.1 Part03 Quality Checklist

### [개념]

Part03 Quality Checklist는 Component Specification Rules 문서가 Agent 기준 문서로 사용 가능한지 확인하는 검수 기준이다.

---

### [핵심]

최종 체크 항목:

```md
## Core

- [ ] Component Specification 정의가 명확한가?
- [ ] Component Spec 필수 항목이 정의되어 있는가?
- [ ] Scope 포함 / 제외 기준이 명확한가?
- [ ] Part02 Token Rules와 연결되는가?

## API

- [ ] Component API 기준이 있는가?
- [ ] Props Naming Rules가 있는가?
- [ ] Event Handler Rules가 있는가?
- [ ] Children / Composition 기준이 있는가?

## Variant

- [ ] Variant 정의가 명확한가?
- [ ] 의미 기반 variant 기준이 있는가?
- [ ] Variant Usage Rules가 있는가?
- [ ] Variant Token Mapping 기준이 있는가?
- [ ] Variant Mistakes가 포함되어 있는가?

## Size

- [ ] Size 정의가 명확한가?
- [ ] sm / md / lg 기준이 있는가?
- [ ] Size Token Mapping 기준이 있는가?
- [ ] Touch Target 기준이 있는가?

## State

- [ ] Component State 기준이 있는가?
- [ ] Interactive State 기준이 있는가?
- [ ] Feedback State 기준이 있는가?
- [ ] Selection State 기준이 있는가?
- [ ] State Mistakes가 포함되어 있는가?

## Accessibility

- [ ] Accessibility Specification 기준이 있는가?
- [ ] Label / Error 연결 기준이 있는가?
- [ ] Keyboard / Focus 기준이 있는가?

## Documentation

- [ ] Usage Rules가 있는가?
- [ ] Do / Don't Rules가 있는가?
- [ ] Example Rules가 있는가?
- [ ] Component Document Template이 있는가?
- [ ] Props Table Rules가 있는가?
- [ ] Component Checklist 기준이 있는가?

## Agent Review

- [ ] Frontend Agent 생성 기준이 있는가?
- [ ] Review Agent 검토 기준이 있는가?
- [ ] Component Change Rules가 있는가?
```

---

### [실무]

Part03은 Part04 Core Component Rules의 직접 기준이다.

Part03 기준으로 Part04에서 다음 컴포넌트를 구체화한다.

```text
Button
Input
Form Field
Select
Checkbox
Radio
Card
Badge
Tag
Alert
Toast
Modal
Tabs
Pagination
Table
```

Part03 승인 기준:

```text
Component Specification 구조 명확
→ Props / Variant / Size / State 기준 명확
→ Accessibility 기준 포함
→ Documentation Template 포함
→ Review Agent 검토 가능
```

---

### [FAQ]

Q. Part03의 역할은 뭐야?
A. 공통 UI 컴포넌트의 Specification 작성 기준, API, variant, size, state, accessibility, documentation 규칙을 정의하는 문서다.

Q. Part03은 Part04와 어떻게 연결돼?
A. Part04 Core Component Rules는 Part03의 Component Specification 기준을 사용해 실제 컴포넌트를 정의한다.

Q. Part03에서 가장 중요한 것은 뭐야?
A. Props API, variant, size, state, accessibility, usage, do / don't, examples 기준이다.

Q. Part03 최종 승인 기준은 뭐야?
A. Frontend Agent가 컴포넌트를 생성하고 Review Agent가 검토할 수 있을 만큼 규격과 체크리스트가 명확해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Component Specification이 뭐야?
A. 컴포넌트의 목적, props, variant, size, state, accessibility, 사용 예시를 정의한 규격이다.

Q. Component Specification은 왜 필요해?
A. Frontend Agent와 개발자가 같은 컴포넌트를 같은 방식으로 사용하기 위해 필요하다.

Q. Component Specification 필수 항목은 뭐야?
A. Purpose, Anatomy, Props, Variants, Sizes, States, Accessibility, Usage, Do, Don't, Examples가 필요하다.

Q. Component API가 뭐야?
A. 컴포넌트를 사용하는 props, event handler, children, override 정책의 규칙이다.

Q. props 이름은 어떻게 지어야 해?
A. 역할이 명확한 이름을 사용한다. 예: `variant`, `size`, `isLoading`, `disabled`, `onClick`.

Q. boolean props는 어떻게 지어야 해?
A. `isLoading`, `isOpen`, `isSelected`, `disabled`처럼 상태 의미가 명확해야 한다.

Q. Event Handler 이름은 어떻게 지어야 해?
A. `onClick`, `onChange`, `onClose`, `onSubmit`처럼 `on` prefix와 행동 이름을 사용한다.

Q. children은 언제 사용해?
A. Button 텍스트, Card 내용, Modal 내용처럼 사용자가 내용을 주입해야 할 때 사용한다.

Q. Compound Component 패턴을 꼭 써야 해?
A. 필수는 아니다. 복잡한 컴포넌트에서 조합 유연성이 필요할 때 적합하다.

Q. Variant가 뭐야?
A. 같은 컴포넌트가 목적에 따라 다른 시각적 의미를 갖도록 하는 체계다.

Q. variant 이름을 blue, red로 해도 돼?
A. 권장하지 않는다. primary, secondary, danger처럼 역할 중심 이름이 좋다.

Q. primary는 언제 써?
A. 화면에서 가장 중요한 주요 행동에 사용한다. 예: 저장, 등록, 검색.

Q. secondary는 언제 써?
A. 주요 행동을 보조하는 행동에 사용한다. 예: 취소, 뒤로가기.

Q. danger variant는 언제 써?
A. 삭제, 탈퇴, 되돌릴 수 없는 위험 행동에 사용한다.

Q. ghost는 언제 써?
A. 낮은 강조의 보조 행동이나 UI를 방해하지 않는 액션에 사용한다.

Q. Variant Token Mapping이 왜 필요해?
A. variant 의미와 실제 스타일 token을 연결해 theme 변경과 리뷰를 안정적으로 하기 위해 필요하다.

Q. variant가 많아지면 좋은 거 아니야?
A. 아니다. variant가 너무 많으면 선택 기준이 흐려지고 유지보수가 어려워진다.

Q. Size는 어떻게 나눠?
A. 기본적으로 sm, md, lg를 사용하고 필요 시 xs, xl을 추가한다.

Q. Button 크기를 매번 직접 지정해도 돼?
A. 권장하지 않는다. size prop과 token으로 관리하는 것이 일관성에 좋다.

Q. Size Token Mapping이 왜 필요해?
A. size prop과 실제 스타일 값을 연결해 컴포넌트 크기를 일관되게 관리하기 위해 필요하다.

Q. Touch Target이 뭐야?
A. 사용자가 터치하거나 클릭할 수 있는 실제 조작 영역이다.

Q. 모바일 버튼 높이는 중요해?
A. 중요하다. 터치 가능한 충분한 영역을 제공해야 한다.

Q. Component State가 뭐야?
A. default, hover, focus, disabled, loading, error처럼 컴포넌트의 현재 상태를 표현하는 규칙이다.

Q. hover만 있으면 충분해?
A. 아니다. focus, disabled, loading, error 같은 상태도 필요하다.

Q. focus와 hover는 뭐가 달라?
A. hover는 마우스 상태이고 focus는 키보드나 보조기기 사용자의 현재 위치다.

Q. focus-visible은 꼭 필요해?
A. 필요하다. 키보드 사용자가 현재 위치를 알 수 있어야 한다.

Q. disabled와 readonly는 뭐가 달라?
A. disabled는 조작과 제출에서 제외되고, readonly는 수정은 불가하지만 값은 읽을 수 있다.

Q. Feedback State는 왜 필요해?
A. 사용자가 처리 중, 성공, 실패, 데이터 없음 상태를 이해할 수 있어야 하기 때문이다.

Q. loading 중에는 버튼을 disabled 처리해야 해?
A. 대부분 그렇다. 중복 클릭과 중복 API 요청을 막기 위해 필요하다.

Q. error state에는 무엇이 필요해?
A. 사용자 친화적 메시지와 가능한 경우 복구 action이 필요하다.

Q. empty state에는 무엇이 필요해?
A. 데이터가 없다는 설명과 다음 행동 안내가 필요하다.

Q. Selection State가 뭐야?
A. selected, checked, current처럼 현재 선택된 항목을 표현하는 상태다.

Q. 선택 상태는 색상만으로 표시해도 돼?
A. 안 된다. 텍스트, 아이콘, 위치, aria 속성 등 추가 정보가 필요하다.

Q. Accessibility Specification이 뭐야?
A. 컴포넌트가 기본적으로 접근성을 만족하도록 하는 기준이다.

Q. placeholder만 있으면 label은 없어도 돼?
A. 권장하지 않는다. placeholder는 입력 예시이고 label은 입력 항목의 이름이다.

Q. error message는 input과 연결해야 해?
A. 해야 한다. `aria-describedby`로 연결하면 스크린 리더 사용자가 오류를 알 수 있다.

Q. 모든 컴포넌트를 키보드로 조작 가능해야 해?
A. 사용자가 조작하는 interactive component는 키보드 접근이 가능해야 한다.

Q. Usage Rules가 왜 필요해?
A. 컴포넌트를 언제 어떻게 써야 하는지 명확히 해 UI 의미 혼선을 줄이기 위해 필요하다.

Q. Button과 Link는 어떻게 구분해?
A. 행동 실행은 Button, 페이지 이동은 Link를 사용한다.

Q. Do / Don't가 왜 필요해?
A. 좋은 사용과 나쁜 사용을 명확히 해 Frontend Agent 생성과 Review Agent 검토 기준으로 쓰기 위해 필요하다.

Q. 예제 코드는 길수록 좋아?
A. 아니다. RAG 문서에서는 짧고 검색 가능한 예제가 더 좋다.

Q. Props Table은 왜 필요해?
A. Agent가 컴포넌트 API를 빠르게 검색하고 정확히 사용할 수 있게 하기 위해 필요하다.

Q. Component Checklist는 왜 필요해?
A. Review Agent가 컴포넌트 품질을 일관되게 검토하기 위해 필요하다.

Q. Frontend Agent는 컴포넌트 생성 전에 무엇을 확인해야 해?
A. 기존 Component Specification, Design Token, variant, size, state, accessibility 기준을 확인해야 한다.

Q. Review Agent는 컴포넌트에서 뭘 봐야 해?
A. Props API, variant, size, state, accessibility, token 사용, usage 기준을 확인해야 한다.

Q. 새 variant를 추가할 때 필요한 것은?
A. 사용 목적, 의미 기반 이름, token mapping, state, documentation, example이 필요하다.

Q. Part03의 역할은 뭐야?
A. 공통 UI 컴포넌트의 Specification 작성 기준, API, variant, size, state, accessibility, documentation 규칙을 정의하는 문서다.
