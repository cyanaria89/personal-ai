# UI Component Pattern Part02 - Props Design

---

# 1. Props Design Overview

## 1.1 Props Design Purpose

### [개념]

Props Design은 React UI Component가 외부에서 어떤 값과 이벤트를 받을지 정의하는 설계 기준이다.

Props는 Component 사용자가 Component의 목적, 상태, 변형, 이벤트, 접근성 요구사항을 명확히 이해할 수 있도록 설계해야 한다.

UI Component Pattern에서 Props Design은 Component Responsibility 다음으로 중요한 기준이다.

---

### [핵심]

Props Design 핵심 기준:

- Props 이름은 의미가 명확해야 한다.
- Props는 Component 책임 범위 안에 있어야 한다.
- Common UI Props는 도메인 의존을 피해야 한다.
- Feature UI Props는 도메인 데이터를 받을 수 있다.
- 상호 배타적인 값은 variant union으로 제한한다.
- 크기는 size union으로 제한한다.
- 상태는 disabled, loading, selected, checked처럼 명확히 표현한다.
- 이벤트는 onClick, onChange, onSubmit처럼 on 접두사를 사용한다.
- 내부 handler는 handleClick, handleChange처럼 handle 접두사를 사용한다.
- children / composition을 적극 활용한다.
- Props Explosion을 방지한다.

---

### [실무]

2026 실무 기준에서 Props Design은 단순 매개변수 설계가 아니다.

Props Design은 Agent가 UI Component를 생성할 때 아래 판단을 수행하도록 지원해야 한다.

```text
Component Responsibility
→ Props Responsibility
→ Naming Convention
→ Variant / Size / State Props
→ Event Handler Props
→ Accessibility Props
→ Children / Composition Props
→ Props Explosion Check
```

Props는 Component API다.

Component API가 복잡하면 사용성이 떨어지고, Feature 요구사항이 Common UI에 섞이며, 유지보수 비용이 증가한다.

---

### [FAQ]

Q. Props Design이 왜 중요해?
A. Props는 Component 사용법을 결정하는 API이기 때문에 이름, 타입, 책임 범위가 명확해야 유지보수하기 쉽다.

Q. Common UI Props와 Feature UI Props는 달라?
A. 다르다. Common UI Props는 도메인 의존을 피하고, Feature UI Props는 도메인 데이터를 받을 수 있다.

Q. Props 설계에서 가장 먼저 볼 것은 뭐야?
A. Component 책임 범위 안에 있는 Props인지 먼저 확인해야 한다.

---

# 2. Props Naming Rules

## 2.1 Props Naming Convention

### [개념]

Props Naming Convention은 Component 사용자가 Props의 의도를 빠르게 이해할 수 있도록 이름을 통일하는 기준이다.

Props 이름은 짧지만 의미가 명확해야 하며, 도메인 의존이 필요한 경우 Feature Component에만 사용한다.

---

### [핵심]

Naming 기준:

- 의미 기반 이름 사용
- 도메인 의존 최소화
- boolean은 상태 의미를 명확히 표현
- event handler는 on 접두사 사용
- 내부 handler는 handle 접두사 사용
- variant / size 이름 통일
- value / defaultValue 구분
- controlled / uncontrolled Props 구분
- children 사용 가능 여부 명확화
- className 확장 기준 명확화

권장 이름:

- variant
- size
- disabled
- loading
- selected
- checked
- open
- required
- value
- defaultValue
- onClick
- onChange
- onSubmit
- onClose
- onOpen
- children
- className

주의 이름:

- blue
- red
- big
- small
- isSpecial
- isReviewDeleteButton
- festivalMode
- adminOnly
- useApi
- data
- item
- option

---

### [실무]

좋은 예:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "danger";
  size?: "sm" | "md" | "lg";
  loading?: boolean;
  disabled?: boolean;
  fullWidth?: boolean;
  onClick?: () => void;
  children: React.ReactNode;
};
```

나쁜 예:

```tsx
type ButtonProps = {
  blue?: boolean;
  red?: boolean;
  big?: boolean;
  isReviewDeleteButton?: boolean;
  festivalId?: number;
  useDeleteApi?: boolean;
};
```

개선 기준:

```text
blue / red
→ variant="primary" / variant="danger"

big / small
→ size="lg" / size="sm"

isReviewDeleteButton
→ ReviewDeleteButton Feature Component 분리

festivalId
→ Feature Component에서 처리
```

---

### [FAQ]

Q. Props 이름은 어떻게 지어야 해?
A. Component 사용자가 목적을 바로 이해할 수 있도록 의미 기반 이름을 사용해야 한다.

Q. Button variant는 blue, red로 만들면 안 돼?
A. 가능은 하지만 primary, secondary, danger처럼 의미 기반 이름이 디자인 변경에 더 유연하다.

Q. 도메인 전용 Props는 어디에 둬야 해?
A. Common UI가 아니라 Feature Component Props로 두는 것이 좋다.

---

## 2.2 Boolean Props Naming

### [개념]

Boolean Props는 true / false로 Component 상태를 제어하는 Props다.

Boolean Props는 간단하지만 많아질수록 조합 복잡도가 커지므로 상태성 값에만 제한적으로 사용해야 한다.

---

### [핵심]

권장 Boolean Props:

- disabled
- loading
- required
- selected
- checked
- open
- invalid
- fullWidth
- readOnly
- multiple
- hidden

상태 표현 접두사:

- is
- has
- can
- should

예:

- isOpen
- isSelected
- hasError
- canClose
- shouldRender

주의 Boolean Props:

- primary
- secondary
- danger
- large
- small
- blue
- red
- isFestivalMode
- isAdminMode
- isSpecial

---

### [실무]

좋은 예:

```tsx
<Button variant="danger" loading disabled>
  삭제
</Button>
```

나쁜 예:

```tsx
<Button danger primary large small>
  삭제
</Button>
```

문제점:

```text
danger와 primary가 동시에 true 가능
large와 small이 동시에 true 가능
style 조합 충돌
Component 사용법 불명확
```

개선:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "danger";
  size?: "sm" | "md" | "lg";
  loading?: boolean;
  disabled?: boolean;
};
```

상호 배타적인 값은 boolean 여러 개보다 union type Props로 제한한다.

---

### [FAQ]

Q. boolean props 이름은 어떻게 지어?
A. 상태를 나타내면 is / has를 사용하고, HTML 속성과 유사한 경우 disabled, required, loading처럼 명확히 쓴다.

Q. boolean props가 많으면 왜 문제야?
A. 서로 충돌하는 조합이 생기고 Component 사용법이 복잡해지기 때문이다.

Q. primary, danger를 boolean으로 두면 안 돼?
A. 가능은 하지만 동시에 true가 될 수 있어 variant union으로 제한하는 것이 더 안전하다.

---

# 3. Variant Props Rules

## 3.1 Variant Props

### [개념]

Variant Props는 Component의 시각적 또는 의미적 변형을 제한된 값으로 표현하는 Props다.

Variant는 색상명보다 의미 기반 이름을 사용하는 것이 좋다.

---

### [핵심]

Variant 사용 대상:

- Button variant
- Badge variant
- Alert variant
- Toast variant
- Card variant
- TextField status
- Modal type
- ErrorState variant

권장 Variant 이름:

- primary
- secondary
- danger
- ghost
- outline
- success
- warning
- error
- info
- default

주의 Variant 이름:

- blue
- red
- pink
- green
- big
- small
- festival
- review
- admin

---

### [실무]

Button Variant 예:

```tsx
type ButtonVariant = "primary" | "secondary" | "danger" | "ghost";

type ButtonProps = {
  variant?: ButtonVariant;
  children: React.ReactNode;
};

function Button({ variant = "primary", children }: ButtonProps) {
  return (
    <button type="button" className={`button button-${variant}`}>
      {children}
    </button>
  );
}
```

Badge Variant 예:

```tsx
type BadgeVariant = "default" | "success" | "warning" | "danger" | "info";

type BadgeProps = {
  variant?: BadgeVariant;
  children: React.ReactNode;
};

function Badge({ variant = "default", children }: BadgeProps) {
  return <span className={`badge badge-${variant}`}>{children}</span>;
}
```

권장:

- 제한된 union type 사용
- 의미 기반 variant 이름 사용
- 기본값 제공
- 색상명 직접 노출 지양
- variant가 너무 많아지면 Component 분리 검토

---

### [FAQ]

Q. variant는 왜 union type으로 제한해?
A. 허용되는 스타일 종류를 명확히 하고 잘못된 문자열 사용을 방지하기 위해서다.

Q. variant 이름은 색상 기준이 좋아 의미 기준이 좋아?
A. primary, danger, success처럼 의미 기준이 디자인 변경에 더 유연하다.

Q. variant가 너무 많아지면 어떻게 해?
A. Component 책임이 너무 넓어진 것일 수 있으므로 별도 Component나 composition을 검토한다.

---

## 3.2 Variant Props vs Boolean Props

### [개념]

Variant Props는 상호 배타적인 여러 선택지를 표현하고, Boolean Props는 독립적인 상태를 표현한다.

서로 동시에 true가 되면 안 되는 값은 boolean보다 variant로 설계해야 한다.

---

### [핵심]

Variant가 적합한 경우:

- primary / secondary / danger
- success / warning / error / info
- sm / md / lg
- filled / outline / ghost
- card / list / compact

Boolean이 적합한 경우:

- disabled
- loading
- required
- selected
- checked
- open
- invalid
- fullWidth

비교:

| 기준        | Variant Props             | Boolean Props     |
| ----------- | ------------------------- | ----------------- |
| 목적        | 제한된 선택지             | true / false 상태 |
| 충돌 가능성 | 낮음                      | 많아질수록 증가   |
| 예          | variant="danger"          | disabled          |
| 적합 대상   | style type, semantic type | 상태, 가능 여부   |
| 주의점      | 값이 너무 많아짐          | 조합 충돌         |

---

### [실무]

나쁜 예:

```tsx
<Button primary danger secondary>
  삭제
</Button>
```

좋은 예:

```tsx
<Button variant="danger">삭제</Button>
```

나쁜 예:

```tsx
<Alert success warning error>
  저장 실패
</Alert>
```

좋은 예:

```tsx
<Alert variant="error">저장 실패</Alert>
```

Boolean은 독립 상태에 사용한다.

```tsx
<Button variant="primary" loading disabled>
  저장
</Button>
```

---

### [FAQ]

Q. variant와 boolean props는 어떻게 구분해?
A. 서로 배타적인 선택지는 variant, 독립적인 true / false 상태는 boolean으로 둔다.

Q. danger, primary를 boolean으로 두면 왜 위험해?
A. 둘 다 true가 될 수 있어 스타일과 의미 충돌이 발생할 수 있다.

Q. loading은 variant야 boolean이야?
A. loading은 독립적인 상태이므로 boolean props가 적합하다.

---

# 4. Size Props Rules

## 4.1 Size Props

### [개념]

Size Props는 Component 크기를 제한된 값으로 제어하는 Props다.

공통 UI Component에서는 px 숫자보다 sm, md, lg 같은 제한된 값이 일관성에 좋다.

---

### [핵심]

Size 사용 대상:

- Button size
- TextField size
- Modal size
- Avatar size
- Badge size
- Spinner size
- Icon size
- Card density

권장 Size 이름:

- xs
- sm
- md
- lg
- xl
- full
- compact

기본 기준:

- md를 기본값으로 사용
- 프로젝트 전체에서 size 이름 통일
- 임의 숫자 props 남발 지양
- width와 size 역할 구분
- fullWidth는 layout 성격이므로 별도 boolean 가능

---

### [실무]

Button Size 예:

```tsx
type ButtonSize = "sm" | "md" | "lg";

type ButtonProps = {
  size?: ButtonSize;
  children: React.ReactNode;
};

function Button({ size = "md", children }: ButtonProps) {
  return (
    <button type="button" className={`button button-${size}`}>
      {children}
    </button>
  );
}
```

Modal Size 예:

```tsx
type ModalSize = "sm" | "md" | "lg";

type ModalProps = {
  open: boolean;
  size?: ModalSize;
  title: string;
  children: React.ReactNode;
  onClose: () => void;
};
```

fullWidth 예:

```tsx
type ButtonProps = {
  size?: "sm" | "md" | "lg";
  fullWidth?: boolean;
};
```

---

### [FAQ]

Q. Button size는 px 값으로 받는 게 좋아?
A. 공통 Component에서는 sm, md, lg처럼 제한된 크기 값을 사용하는 것이 일관성에 좋다.

Q. full width 버튼은 size야 variant야?
A. 보통 size보다 layout 성격이 강하므로 fullWidth 같은 별도 prop으로 둘 수 있다.

Q. size 기본값은 뭘로 두는 게 좋아?
A. 프로젝트 기준에 따라 다르지만 일반적으로 md를 기본값으로 둔다.

---

## 4.2 Size Props Anti Pattern

### [개념]

Size Props Anti Pattern은 Component 크기 제어를 지나치게 자유롭게 열어 스타일 일관성을 깨는 문제다.

공통 UI Component에서는 디자인 시스템 확장을 고려해 제한된 size 값을 우선 사용해야 한다.

---

### [핵심]

주의 패턴:

- width, height 숫자 props 남발
- padding, margin props 남발
- fontSize 직접 props 제공
- size와 layout 책임 혼동
- Component 내부 margin 포함
- 화면별 예외 크기를 공통 Component에 계속 추가
- compact, dense, small, sm 혼용

권장 해결:

- size union type 사용
- fullWidth 별도 prop 사용
- layout은 부모 Component가 담당
- spacing은 Layout Component가 담당
- 특수 크기는 Feature Component에서 처리
- size naming 통일

---

### [실무]

나쁜 예:

```tsx
type ButtonProps = {
  width?: number;
  height?: number;
  padding?: number;
  margin?: number;
  fontSize?: number;
};
```

개선 예:

```tsx
type ButtonProps = {
  size?: "sm" | "md" | "lg";
  fullWidth?: boolean;
  className?: string;
};
```

특정 화면 전용 크기는 Feature에서 처리한다.

```tsx
function HeroActionButton({ children }: { children: React.ReactNode }) {
  return (
    <Button className="hero-action-button" size="lg">
      {children}
    </Button>
  );
}
```

---

### [FAQ]

Q. 공통 Component에서 width, height를 직접 props로 열어도 돼?
A. 가능은 하지만 스타일 일관성이 깨질 수 있어 size union과 className 확장을 우선하는 것이 좋다.

Q. Button 안에 margin을 넣어도 돼?
A. 공통 Button에는 margin을 넣지 않는 것이 좋다. 버튼 간 간격은 부모 Layout이나 ButtonGroup이 담당하는 편이 유연하다.

Q. 화면마다 크기가 다르면 어떻게 해?
A. 공통 size 값으로 해결 가능한지 보고, 특수 화면 요구는 Feature Component나 className으로 처리한다.

---

# 5. Event Handler Props Rules

## 5.1 Event Handler Props

### [개념]

Event Handler Props는 Component 내부에서 발생한 사용자 이벤트를 외부로 전달하는 Props다.

공통 UI Component는 이벤트가 발생했다는 사실만 전달하고 실제 도메인 로직은 부모 Component, Feature Component, Custom Hook에서 처리한다.

---

### [핵심]

Event Handler Props 이름:

- onClick
- onChange
- onSubmit
- onClose
- onOpen
- onSelect
- onConfirm
- onCancel
- onRetry
- onReset
- onFocus
- onBlur

내부 handler 이름:

- handleClick
- handleChange
- handleSubmit
- handleClose
- handleOpen
- handleSelect
- handleConfirm
- handleCancel
- handleRetry
- handleReset

규칙:

- Props는 onX 형태
- 내부 함수는 handleX 형태
- Common UI에서 API 직접 호출 금지
- event 객체 전달 기준 통일
- value 전달 기준 통일
- optional callback은 호출 전 확인
- disabled / loading 상태에서 이벤트 처리 기준 통일

---

### [실무]

Button 예:

```tsx
type ButtonProps = {
  disabled?: boolean;
  loading?: boolean;
  onClick?: () => void;
  children: React.ReactNode;
};

function Button({
  disabled = false,
  loading = false,
  onClick,
  children,
}: ButtonProps) {
  function handleClick() {
    if (disabled || loading) {
      return;
    }

    onClick?.();
  }

  return (
    <button type="button" disabled={disabled || loading} onClick={handleClick}>
      {loading ? "처리 중..." : children}
    </button>
  );
}
```

Modal 예:

```tsx
type ModalProps = {
  open: boolean;
  onClose: () => void;
  children: React.ReactNode;
};

function Modal({ open, onClose, children }: ModalProps) {
  if (!open) {
    return null;
  }

  return (
    <div role="dialog" aria-modal="true">
      <button type="button" onClick={onClose}>
        닫기
      </button>
      {children}
    </div>
  );
}
```

---

### [FAQ]

Q. onClick 안에서 API 호출을 넣어도 돼?
A. Feature Component에서는 가능하지만 공통 UI Component에서는 부모로 이벤트를 전달하는 것이 좋다.

Q. Event Handler Props는 왜 on으로 시작해?
A. Component 외부에서 전달되는 이벤트 callback임을 명확히 하기 위해서다.

Q. 내부 함수는 왜 handle로 시작해?
A. Component 내부에서 이벤트를 처리하는 함수임을 구분하기 위해서다.

---

## 5.2 onChange Value Pattern

### [개념]

onChange Value Pattern은 Input 계열 Component에서 event 객체를 넘길지 value만 넘길지 정하는 기준이다.

프로젝트 컨벤션을 통일하는 것이 중요하다.

---

### [핵심]

event 전달 방식:

- React 기본 이벤트와 일치
- input 상세 제어 가능
- 타입이 길어질 수 있음
- Form library와 연결 쉬움

value 전달 방식:

- 사용이 단순함
- Component 사용자가 event를 몰라도 됨
- 공통 Component API가 단순해짐
- 여러 input type에서 변환 기준 필요

비교:

| 기준 | event 전달                    | value 전달         |
| ---- | ----------------------------- | ------------------ |
| 형태 | onChange(event)               | onChange(value)    |
| 장점 | React 기본 방식               | 사용 단순          |
| 단점 | 사용자가 event 처리           | 변환 책임 필요     |
| 적합 | Form library, low-level input | App-level UI input |

---

### [실무]

event 전달 예:

```tsx
type TextFieldProps = {
  value: string;
  onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
};
```

value 전달 예:

```tsx
type TextFieldProps = {
  value: string;
  onChange: (value: string) => void;
};

function TextField({ value, onChange }: TextFieldProps) {
  return (
    <input value={value} onChange={(event) => onChange(event.target.value)} />
  );
}
```

프로젝트 기준을 정한 뒤 일관되게 사용한다.

```text
Low-level input
→ event 전달 가능

App common input
→ value 전달 가능

React Hook Form 직접 연결
→ event / register 전달 검토
```

---

### [FAQ]

Q. onChange는 event를 넘기는 게 좋아 value를 넘기는 게 좋아?
A. 공통 input은 event를 넘기거나 value를 넘길 수 있다. 프로젝트 컨벤션을 통일하는 것이 중요하다.

Q. value 전달 방식의 장점은 뭐야?
A. Component 사용자가 event 객체를 직접 다루지 않아도 되어 사용법이 단순하다.

Q. React Hook Form을 쓰면 어떤 방식이 좋아?
A. register 연결 방식에 따라 event 전달이나 ref forwarding이 필요할 수 있다.

---

# 6. Children and Composition Props

## 6.1 Children Props

### [개념]

children Props는 Component 내부에 들어갈 내용을 외부에서 자유롭게 전달하는 Composition Pattern이다.

children은 내부 내용이 다양하거나 외부에서 조합해야 하는 UI Component에 적합하다.

---

### [핵심]

children 적합 대상:

- Button
- Card
- Modal
- Dialog
- Layout
- Section
- List Item
- EmptyState action 영역
- ErrorState action 영역

children 사용 기준:

- 내부 내용이 다양함
- 외부 조합이 필요함
- 단순 문자열보다 ReactNode가 적합함
- Layout 구조를 제공함
- 도메인 내용을 모르고 감쌀 수 있음

주의:

- 모든 Props를 children으로 대체하지 않음
- title, value처럼 의미가 명확한 데이터는 명시 Props가 좋을 수 있음
- children 필수 여부를 타입으로 표현해야 함
- children 내부 구조를 과도하게 가정하지 않음

---

### [실무]

Card 예:

```tsx
type CardProps = {
  children: React.ReactNode;
};

function Card({ children }: CardProps) {
  return <article className="card">{children}</article>;
}
```

사용:

```tsx
<Card>
  <h3>축제 제목</h3>
  <p>서울</p>
</Card>
```

Button 예:

```tsx
type ButtonProps = {
  children: React.ReactNode;
};

function Button({ children }: ButtonProps) {
  return <button type="button">{children}</button>;
}
```

명시 Props가 더 좋은 예:

```tsx
type EmptyStateProps = {
  title: string;
  description?: string;
  action?: React.ReactNode;
};
```

---

### [FAQ]

Q. children은 언제 써?
A. Component 내부 내용이 다양하거나 외부에서 자유롭게 조합해야 할 때 사용한다.

Q. 모든 것을 children으로 받으면 좋아?
A. 아니다. title, value처럼 의미가 명확한 데이터는 명시 Props가 더 좋을 수 있다.

Q. children 타입은 뭘로 두는 게 좋아?
A. ReactNode를 사용하는 경우가 많다.

---

## 6.2 Slot-like Props

### [개념]

Slot-like Props는 Component의 특정 위치에 들어갈 UI를 ReactNode Props로 전달하는 방식이다.

React에서는 header, footer, action, rightArea 같은 Props로 Slot-like Pattern을 구현할 수 있다.

---

### [핵심]

Slot-like Props 사용 대상:

- modal header
- modal footer
- card action
- page header action
- empty state action
- error state action
- list item right area
- table cell custom render
- layout sidebar

권장 이름:

- header
- footer
- action
- actions
- leftArea
- rightArea
- icon
- trigger

주의:

- slot props가 너무 많으면 Component 책임이 커짐
- slot 위치가 명확해야 함
- 복잡해지면 Compound Component 검토
- 단순 데이터는 ReactNode보다 명시 Props가 나을 수 있음

---

### [실무]

EmptyState 예:

```tsx
type EmptyStateProps = {
  title: string;
  description?: string;
  action?: React.ReactNode;
};

function EmptyState({ title, description, action }: EmptyStateProps) {
  return (
    <section className="empty-state">
      <h2>{title}</h2>
      {description && <p>{description}</p>}
      {action}
    </section>
  );
}
```

사용:

```tsx
<EmptyState
  title="검색 결과가 없습니다."
  description="검색어를 바꾸거나 필터를 초기화해 보세요."
  action={<Button onClick={resetFilter}>필터 초기화</Button>}
/>
```

Modal footer 예:

```tsx
type ModalProps = {
  open: boolean;
  title: string;
  footer?: React.ReactNode;
  onClose: () => void;
  children: React.ReactNode;
};
```

---

### [FAQ]

Q. action props는 왜 ReactNode로 받아?
A. 버튼, 링크, 여러 액션 등 다양한 UI를 유연하게 넣기 위해서다.

Q. slot props가 많아지면 어떻게 해?
A. Component 책임이 커졌을 수 있다. children 구조나 compound pattern을 검토한다.

Q. header, footer는 children으로 처리하면 안 돼?
A. 가능하지만 위치가 고정되어야 하면 명시적인 slot-like props가 더 명확할 수 있다.

---

# 7. Accessibility Props Rules

## 7.1 Accessibility Props

### [개념]

Accessibility Props는 UI Component가 접근 가능한 이름, 설명, 상태를 외부에서 전달받거나 내부에서 연결하기 위한 Props다.

공통 UI Component는 semantic HTML과 기본 ARIA 속성을 제공해야 한다.

---

### [핵심]

Accessibility Props 후보:

- aria-label
- aria-labelledby
- aria-describedby
- aria-expanded
- aria-selected
- aria-invalid
- role
- id
- htmlFor
- alt
- title

필수 고려:

- 아이콘 버튼은 aria-label 필요
- input은 label 또는 aria-label 필요
- error message는 aria-describedby 연결
- dropdown은 aria-expanded 필요
- tab은 aria-selected 필요
- modal은 role dialog와 aria-modal 필요
- 이미지 alt 기준 필요

---

### [실무]

Icon Button 예:

```tsx
type IconButtonProps = {
  ariaLabel: string;
  onClick?: () => void;
  children: React.ReactNode;
};

function IconButton({ ariaLabel, onClick, children }: IconButtonProps) {
  return (
    <button type="button" aria-label={ariaLabel} onClick={onClick}>
      {children}
    </button>
  );
}
```

TextField 예:

```tsx
type TextFieldProps = {
  id: string;
  label: string;
  value: string;
  error?: string;
  onChange: (value: string) => void;
};

function TextField({ id, label, value, error, onChange }: TextFieldProps) {
  const errorId = `${id}-error`;

  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input
        id={id}
        value={value}
        aria-invalid={Boolean(error)}
        aria-describedby={error ? errorId : undefined}
        onChange={(event) => onChange(event.target.value)}
      />
      {error && (
        <p id={errorId} role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
```

---

### [FAQ]

Q. 아이콘 버튼에는 텍스트가 없어도 돼?
A. 시각적 텍스트가 없다면 aria-label로 버튼의 목적을 제공해야 한다.

Q. input에 label이 꼭 필요해?
A. 접근성과 사용성 측면에서 label을 제공하는 것이 좋다.

Q. error message는 input과 어떻게 연결해?
A. error message id를 만들고 input의 aria-describedby에 연결한다.

---

# 8. Props Explosion Troubleshooting

## 8.1 Props Explosion

### [개념]

Props Explosion은 Component가 너무 많은 Props를 받아 사용법이 복잡해지는 문제다.

Props Explosion은 Component 책임이 커졌거나, Feature 요구사항을 Common UI에 계속 추가할 때 자주 발생한다.

---

### [핵심]

원인:

- 하나의 Component가 너무 많은 역할 담당
- 모든 예외를 Props로 처리
- boolean Props 과다
- 도메인 요구사항을 공통 UI에 직접 추가
- composition 대신 Props만 확장
- 특정 화면 요구사항을 Common UI에 누적
- Props 이름이 추상적임
- variant가 너무 많음

해결:

- Component 책임 재정의
- Common UI / Feature UI 분리
- variant로 통합
- composition 사용
- slot-like props 사용
- Component 분리
- Feature Component로 이동
- 불필요한 Props 제거

---

### [실무]

문제 예:

```tsx
type ButtonProps = {
  primary?: boolean;
  secondary?: boolean;
  danger?: boolean;
  large?: boolean;
  small?: boolean;
  isReviewDelete?: boolean;
  isAdminOnly?: boolean;
  festivalId?: number;
  reviewId?: number;
  useConfirm?: boolean;
  useDeleteApi?: boolean;
};
```

문제점:

```text
style boolean 충돌
도메인 Props 포함
API 처리 여부 포함
공통 Button 책임 초과
사용법 복잡
```

개선:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "danger";
  size?: "sm" | "md" | "lg";
  loading?: boolean;
  disabled?: boolean;
  onClick?: () => void;
  children: React.ReactNode;
};

function ReviewDeleteButton({ reviewId }: { reviewId: number }) {
  function handleDelete() {
    deleteReview(reviewId);
  }

  return (
    <Button variant="danger" onClick={handleDelete}>
      삭제
    </Button>
  );
}
```

---

### [FAQ]

Q. Props가 너무 많으면 어떻게 해?
A. Component 책임을 다시 확인하고 composition, variant, Feature Component 분리를 검토한다.

Q. 도메인 전용 Props를 공통 Component에 넣어도 돼?
A. 권장하지 않는다. 도메인 전용 로직은 Feature Component에 두는 것이 좋다.

Q. Props Explosion은 어떻게 찾을 수 있어?
A. Props 개수, boolean 충돌, 도메인 Props 포함 여부, Component 내부 조건문 증가 여부를 확인한다.

---

## 8.2 Props Design Checklist

### [개념]

Props Design Checklist는 UI Component Props가 명확하고 안정적인지 검수하기 위한 기준이다.

Frontend Agent와 Review Agent는 Component 생성 후 Props API를 반드시 검토해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Props가 Component 책임 범위 안에 있는가?
- [ ] Common UI에 도메인 Props가 들어가지 않았는가?
- [ ] Props 이름이 명확한가?
- [ ] boolean Props가 과도하지 않은가?
- [ ] 상호 배타적인 값은 variant로 제한했는가?
- [ ] 크기 값은 size로 통일했는가?
- [ ] disabled / loading 상태 기준이 명확한가?
- [ ] Event Handler Props는 onX 형태인가?
- [ ] 내부 handler는 handleX 형태인가?
- [ ] onChange 전달 방식이 프로젝트 기준과 일치하는가?
- [ ] children 사용이 적절한가?
- [ ] slot-like props가 과도하지 않은가?
- [ ] 접근성 Props가 필요한 곳에 포함되었는가?
- [ ] className 확장 기준이 있는가?
- [ ] Props Explosion이 없는가?
```

---

### [실무]

검수 Flow:

```text
Props Draft
→ Responsibility Check
→ Naming Check
→ Variant / Size Check
→ Boolean Conflict Check
→ Event Handler Check
→ Accessibility Check
→ Props Explosion Check
→ Final Props API
```

치명적 문제:

```text
Common UI에 festivalId / reviewId / userId 포함
Button에 deleteReview API 처리 Props 포함
primary / danger boolean 동시 사용
width / height / margin / padding Props 남발
aria-label 없는 IconButton
label 없는 TextField
onChange 방식 혼용
```

---

### [FAQ]

Q. Props Design 검수에서 가장 중요한 것은 뭐야?
A. Props가 Component 책임 범위 안에 있는지와 Common UI에 도메인 Props가 들어가지 않았는지다.

Q. Props 이름이 애매하면 어떻게 해?
A. 사용 목적을 드러내는 이름으로 바꾸고, 도메인 의미가 강하면 Feature Component로 이동한다.

Q. Props Design에서 치명적인 문제는 뭐야?
A. Common UI가 도메인 Props와 API 처리 Props를 받아 만능 Component가 되는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Props Design이 왜 중요해?
A. Props는 Component 사용법을 결정하는 API이기 때문에 이름, 타입, 책임 범위가 명확해야 유지보수하기 쉽다.

Q. UI Component props는 어떻게 설계해?
A. 의미가 명확한 이름을 사용하고 variant, size, disabled, loading, onClick, children 같은 기준을 일관되게 둔다.

Q. Common UI Props와 Feature UI Props는 달라?
A. 다르다. Common UI Props는 도메인 의존을 피하고, Feature UI Props는 도메인 데이터를 받을 수 있다.

Q. Props 설계에서 가장 먼저 볼 것은 뭐야?
A. Component 책임 범위 안에 있는 Props인지 먼저 확인해야 한다.

Q. Props 이름은 어떻게 지어야 해?
A. Component 사용자가 목적을 바로 이해할 수 있도록 의미 기반 이름을 사용해야 한다.

Q. Button variant는 blue, red로 만들면 안 돼?
A. 가능은 하지만 primary, secondary, danger처럼 의미 기반 이름이 디자인 변경에 더 유연하다.

Q. 도메인 전용 Props는 어디에 둬야 해?
A. Common UI가 아니라 Feature Component Props로 두는 것이 좋다.

Q. boolean props 이름은 어떻게 지어?
A. 상태를 나타내면 is / has를 사용하고, HTML 속성과 유사한 경우 disabled, required, loading처럼 명확히 쓴다.

Q. boolean props가 많으면 왜 문제야?
A. 서로 충돌하는 조합이 생기고 Component 사용법이 복잡해지기 때문이다.

Q. primary, danger를 boolean으로 두면 안 돼?
A. 가능은 하지만 동시에 true가 될 수 있어 variant union으로 제한하는 것이 더 안전하다.

Q. variant는 왜 union type으로 제한해?
A. 허용되는 스타일 종류를 명확히 하고 잘못된 문자열 사용을 방지하기 위해서다.

Q. variant 이름은 색상 기준이 좋아 의미 기준이 좋아?
A. primary, danger, success처럼 의미 기준이 디자인 변경에 더 유연하다.

Q. variant가 너무 많아지면 어떻게 해?
A. Component 책임이 너무 넓어진 것일 수 있으므로 별도 Component나 composition을 검토한다.

Q. variant와 boolean props는 어떻게 구분해?
A. 서로 배타적인 선택지는 variant, 독립적인 true / false 상태는 boolean으로 둔다.

Q. danger, primary를 boolean으로 두면 왜 위험해?
A. 둘 다 true가 될 수 있어 스타일과 의미 충돌이 발생할 수 있다.

Q. loading은 variant야 boolean이야?
A. loading은 독립적인 상태이므로 boolean props가 적합하다.

Q. Button size는 px 값으로 받는 게 좋아?
A. 공통 Component에서는 sm, md, lg처럼 제한된 크기 값을 사용하는 것이 일관성에 좋다.

Q. full width 버튼은 size야 variant야?
A. 보통 size보다 layout 성격이 강하므로 fullWidth 같은 별도 prop으로 둘 수 있다.

Q. size 기본값은 뭘로 두는 게 좋아?
A. 프로젝트 기준에 따라 다르지만 일반적으로 md를 기본값으로 둔다.

Q. 공통 Component에서 width, height를 직접 props로 열어도 돼?
A. 가능은 하지만 스타일 일관성이 깨질 수 있어 size union과 className 확장을 우선하는 것이 좋다.

Q. Button 안에 margin을 넣어도 돼?
A. 공통 Button에는 margin을 넣지 않는 것이 좋다. 버튼 간 간격은 부모 Layout이나 ButtonGroup이 담당하는 편이 유연하다.

Q. 화면마다 크기가 다르면 어떻게 해?
A. 공통 size 값으로 해결 가능한지 보고, 특수 화면 요구는 Feature Component나 className으로 처리한다.

Q. onClick 안에서 API 호출을 넣어도 돼?
A. Feature Component에서는 가능하지만 공통 UI Component에서는 부모로 이벤트를 전달하는 것이 좋다.

Q. Event Handler Props는 왜 on으로 시작해?
A. Component 외부에서 전달되는 이벤트 callback임을 명확히 하기 위해서다.

Q. 내부 함수는 왜 handle로 시작해?
A. Component 내부에서 이벤트를 처리하는 함수임을 구분하기 위해서다.

Q. onChange는 event를 넘기는 게 좋아 value를 넘기는 게 좋아?
A. 공통 input은 event를 넘기거나 value를 넘길 수 있다. 프로젝트 컨벤션을 통일하는 것이 중요하다.

Q. value 전달 방식의 장점은 뭐야?
A. Component 사용자가 event 객체를 직접 다루지 않아도 되어 사용법이 단순하다.

Q. React Hook Form을 쓰면 어떤 방식이 좋아?
A. register 연결 방식에 따라 event 전달이나 ref forwarding이 필요할 수 있다.

Q. children은 언제 써?
A. Component 내부 내용이 다양하거나 외부에서 자유롭게 조합해야 할 때 사용한다.

Q. 모든 것을 children으로 받으면 좋아?
A. 아니다. title, value처럼 의미가 명확한 데이터는 명시 Props가 더 좋을 수 있다.

Q. children 타입은 뭘로 두는 게 좋아?
A. ReactNode를 사용하는 경우가 많다.

Q. action props는 왜 ReactNode로 받아?
A. 버튼, 링크, 여러 액션 등 다양한 UI를 유연하게 넣기 위해서다.

Q. slot props가 많아지면 어떻게 해?
A. Component 책임이 커졌을 수 있다. children 구조나 compound pattern을 검토한다.

Q. header, footer는 children으로 처리하면 안 돼?
A. 가능하지만 위치가 고정되어야 하면 명시적인 slot-like props가 더 명확할 수 있다.

Q. 아이콘 버튼에는 텍스트가 없어도 돼?
A. 시각적 텍스트가 없다면 aria-label로 버튼의 목적을 제공해야 한다.

Q. input에 label이 꼭 필요해?
A. 접근성과 사용성 측면에서 label을 제공하는 것이 좋다.

Q. error message는 input과 어떻게 연결해?
A. error message id를 만들고 input의 aria-describedby에 연결한다.

Q. Props가 너무 많으면 어떻게 해?
A. Component 책임을 다시 확인하고 composition, variant, Feature Component 분리를 검토한다.

Q. Props Explosion은 어떻게 찾을 수 있어?
A. Props 개수, boolean 충돌, 도메인 Props 포함 여부, Component 내부 조건문 증가 여부를 확인한다.

Q. Props Design 검수에서 가장 중요한 것은 뭐야?
A. Props가 Component 책임 범위 안에 있는지와 Common UI에 도메인 Props가 들어가지 않았는지다.

Q. Props 이름이 애매하면 어떻게 해?
A. 사용 목적을 드러내는 이름으로 바꾸고, 도메인 의미가 강하면 Feature Component로 이동한다.

Q. Props Design에서 치명적인 문제는 뭐야?
A. Common UI가 도메인 Props와 API 처리 Props를 받아 만능 Component가 되는 것이다.
