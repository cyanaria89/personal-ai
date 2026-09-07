# Design System Foundation Part02 - Design Token Rules

---

# 1. Design Token Core

## 1.1 Design Token Definition

### [개념]

Design Token은 색상, 간격, 폰트, radius, shadow, z-index, motion 같은 디자인 값을 코드에서 재사용 가능한 이름으로 관리하는 방식이다.

Design Token은 Design System의 가장 작은 기준 단위다.

Design Token은 Frontend Agent가 UI 스타일을 생성할 때 raw value를 직접 사용하지 않고 의미 있는 이름으로 스타일을 적용하게 만드는 기준이다.

---

### [핵심]

Design Token의 핵심 목적:

- 디자인 값 일관성 유지
- raw value 하드코딩 감소
- 색상 / 간격 / 폰트 기준 통일
- 컴포넌트 스타일 재사용
- Theme / Dark Mode 확장 가능
- Review Agent 검토 기준 제공
- Frontend Agent 스타일 생성 기준 제공

Token 종류:

- Color Token
- Typography Token
- Spacing Token
- Radius Token
- Shadow Token
- Z-index Token
- Breakpoint Token
- Motion Token
- Size Token
- Opacity Token

---

### [실무]

Design Token 사용 Flow:

```text
Raw Value
→ Primitive Token
→ Semantic Token
→ Component Token
→ Component Style
→ Theme Extension
```

나쁜 예:

```css
.button {
  background: #2563eb;
  color: white;
  padding: 13px 21px;
  border-radius: 7px;
}
```

좋은 예:

```css
.button {
  background: var(--button-primary-background);
  color: var(--button-primary-text);
  padding: var(--spacing-2) var(--spacing-4);
  border-radius: var(--radius-button);
}
```

Review Agent는 반복되는 raw value가 token으로 관리되는지 확인해야 한다.

Frontend Agent는 컴포넌트 스타일 작성 시 semantic token 또는 component token을 우선 사용해야 한다.

---

### [FAQ]

Q. Design Token이 뭐야?
A. 색상, 간격, 폰트, radius, shadow 같은 디자인 값을 이름으로 관리하는 방식이다.

Q. Design Token은 왜 필요해?
A. 디자인 값을 일관되게 관리하고 변경 시 전체 UI에 안정적으로 반영하기 위해 필요하다.

Q. 모든 값을 token으로 만들어야 해?
A. 아니다. 반복 사용되거나 의미 있는 값부터 token으로 관리한다.

Q. Design Token은 Design System에서 어떤 역할이야?
A. Design System의 가장 작은 기준 단위이며 컴포넌트 스타일과 theme 확장의 기반이다.

---

## 1.2 Token Type

### [개념]

Token Type은 디자인 값을 목적별로 분류한 체계다.

Token Type을 분리하면 Frontend Agent가 색상, 간격, 폰트, 레이아웃, 상태 스타일을 구분해서 생성할 수 있다.

---

### [핵심]

주요 Token Type:

| Token Type       | 목적                        | 예시                  |
| ---------------- | --------------------------- | --------------------- |
| Color Token      | 색상 관리                   | `--color-primary`     |
| Typography Token | 글자 스타일 관리            | `--font-size-md`      |
| Spacing Token    | 간격 관리                   | `--spacing-4`         |
| Radius Token     | 모서리 둥글기 관리          | `--radius-md`         |
| Shadow Token     | 깊이 표현 관리              | `--shadow-card`       |
| Z-index Token    | 겹침 순서 관리              | `--z-modal`           |
| Breakpoint Token | 반응형 기준 관리            | `--breakpoint-tablet` |
| Motion Token     | transition / animation 관리 | `--duration-fast`     |
| Size Token       | 컴포넌트 크기 관리          | `--button-height-md`  |
| Opacity Token    | 투명도 관리                 | `--opacity-disabled`  |

---

### [실무]

Token Type 사용 기준:

```text
색상 변경 가능성이 있는 값
→ Color Token

margin / padding / gap
→ Spacing Token

font-size / font-weight / line-height
→ Typography Token

border-radius
→ Radius Token

box-shadow
→ Shadow Token

modal / toast / dropdown 겹침
→ Z-index Token

hover / active transition
→ Motion Token
```

권장 파일 예:

```text
src/styles/tokens.css
src/styles/theme.css
src/styles/global.css
```

또는 규모가 커질 경우:

```text
src/styles/tokens/color.css
src/styles/tokens/typography.css
src/styles/tokens/spacing.css
src/styles/tokens/elevation.css
src/styles/tokens/motion.css
```

---

### [FAQ]

Q. Token Type을 나누는 이유는?
A. 디자인 값을 목적별로 관리해 검색, 변경, 리뷰가 쉬워지기 때문이다.

Q. 색상과 간격 token을 같은 파일에 둬도 돼?
A. 작은 프로젝트는 가능하다. 규모가 커지면 type별 파일로 분리하는 것이 좋다.

Q. Size Token과 Spacing Token은 뭐가 달라?
A. Spacing Token은 간격이고, Size Token은 버튼 높이, 아이콘 크기 같은 요소 자체의 크기다.

Q. Motion Token도 꼭 필요해?
A. 반복되는 transition이나 animation이 있다면 필요하다.

---

## 1.3 Token Naming Rules

### [개념]

Token Naming Rules는 디자인 값을 일관되게 이름 붙이는 규칙이다.

Token 이름은 Frontend Agent와 Review Agent가 검색하고 판단할 수 있도록 역할과 의미가 명확해야 한다.

---

### [핵심]

권장 naming 구조:

```text
--category-scale
--category-role
--category-role-state
--component-property
--component-property-state
```

예:

```text
--spacing-4
--color-primary
--color-primary-hover
--color-text-muted
--radius-card
--shadow-card
--z-modal
--button-height-md
--button-primary-background
--input-border-error
```

좋은 token 이름:

```text
--color-error
--color-surface
--color-border
--spacing-md
--font-size-lg
--radius-button
--z-toast
```

나쁜 token 이름:

```text
--blue
--red1
--big-space
--nice-shadow
--temp-color
--mainThing
```

---

### [실무]

Token naming checklist:

```md
- [ ] 역할이 드러나는가?
- [ ] 프로젝트 전체에서 일관적인가?
- [ ] theme 변경에 안전한가?
- [ ] 컴포넌트에서 raw value를 숨길 수 있는가?
- [ ] 화면 이름에 과하게 묶이지 않는가?
- [ ] 상태 이름이 명확한가?
- [ ] category / role / state 순서가 일관적인가?
```

권장:

```css
:root {
  --color-primary: #2563eb;
  --color-primary-hover: #1d4ed8;
  --color-text-muted: #6b7280;
  --spacing-4: 16px;
  --radius-card: 12px;
}
```

비권장:

```css
:root {
  --blue: #2563eb;
  --blue2: #1d4ed8;
  --gray-text: #6b7280;
  --gap-big: 16px;
  --round-nice: 12px;
}
```

---

### [FAQ]

Q. Token 이름은 어떻게 지어야 해?
A. 역할과 의미가 드러나게 짓는다. 예: `--color-primary`, `--color-error`, `--spacing-4`.

Q. `--blue-500` 같은 이름은 쓰면 안 돼?
A. Primitive Token으로는 가능하다. 컴포넌트에서는 `--color-primary` 같은 semantic token 사용을 우선한다.

Q. token 이름에 컴포넌트 이름을 넣어도 돼?
A. 특정 컴포넌트 전용 token이면 가능하다. 예: `--button-height-md`.

Q. 색상 이름 token과 의미 token 중 뭐가 좋아?
A. 컴포넌트 스타일에서는 의미 token이 좋다. theme 변경과 역할 관리에 유리하다.

---

# 2. Primitive Token and Semantic Token

## 2.1 Primitive Token

### [개념]

Primitive Token은 원시 디자인 값을 이름으로 저장한 token이다.

Primitive Token은 색상 팔레트, 간격 scale, 폰트 크기 scale처럼 의미보다 값 자체의 기준을 관리한다.

---

### [핵심]

Primitive Token 예:

```text
--blue-50
--blue-100
--blue-500
--blue-600
--red-600
--gray-50
--gray-900
--space-4
--space-8
--font-size-16
```

Primitive Token 특징:

- 값 중심
- 팔레트 중심
- scale 중심
- semantic token의 기반
- 컴포넌트 직접 사용은 제한 권장
- theme 변경 시 직접 대응 어려움

---

### [실무]

Primitive Color Token 예:

```css
:root {
  --blue-50: #eff6ff;
  --blue-100: #dbeafe;
  --blue-600: #2563eb;
  --blue-700: #1d4ed8;

  --red-600: #dc2626;
  --green-600: #16a34a;
  --yellow-500: #f59e0b;

  --gray-50: #f9fafb;
  --gray-100: #f3f4f6;
  --gray-500: #6b7280;
  --gray-900: #111827;
}
```

Primitive Token은 직접 컴포넌트에 쓰기보다 semantic token의 재료로 사용한다.

권장 Flow:

```text
--blue-600
→ --color-primary
→ --button-primary-background
→ Button style
```

---

### [FAQ]

Q. Primitive Token이 뭐야?
A. `--blue-600`처럼 원시 색상이나 값을 나타내는 token이다.

Q. Primitive Token은 언제 사용해?
A. 색상 팔레트, spacing scale, typography scale 같은 기본 값 체계를 만들 때 사용한다.

Q. Primitive Token을 컴포넌트에서 바로 써도 돼?
A. 가능하지만 권장하지 않는다. 컴포넌트에서는 semantic token을 우선 사용한다.

Q. Primitive Token만 있으면 충분해?
A. 아니다. theme 변경과 UI 의미 관리를 위해 semantic token이 필요하다.

---

## 2.2 Semantic Token

### [개념]

Semantic Token은 UI 역할과 의미를 가진 디자인 token이다.

Semantic Token은 `primary`, `error`, `surface`, `text`, `border`처럼 값보다 사용 목적을 표현한다.

---

### [핵심]

Semantic Token 예:

```text
--color-primary
--color-primary-hover
--color-background
--color-surface
--color-text
--color-text-muted
--color-border
--color-error
--color-warning
--color-success
--color-info
--color-focus-ring
```

Semantic Token 특징:

- 역할 중심
- UI 의미 중심
- 컴포넌트 사용 권장
- theme 변경에 유리
- dark mode 대응에 유리
- Review Agent 검토에 유리

---

### [실무]

Semantic Token 예:

```css
:root {
  --blue-600: #2563eb;
  --blue-700: #1d4ed8;
  --red-600: #dc2626;
  --gray-50: #f9fafb;
  --gray-900: #111827;

  --color-primary: var(--blue-600);
  --color-primary-hover: var(--blue-700);
  --color-error: var(--red-600);
  --color-surface: var(--gray-50);
  --color-text: var(--gray-900);
}
```

컴포넌트 사용:

```css
.buttonPrimary {
  background: var(--color-primary);
}

.buttonPrimary:hover {
  background: var(--color-primary-hover);
}
```

Dark Mode 확장:

```css
[data-theme="dark"] {
  --color-surface: #1f2937;
  --color-text: #f9fafb;
}
```

컴포넌트는 `--color-surface`, `--color-text`를 그대로 사용하므로 theme 변경에 안전하다.

---

### [FAQ]

Q. Semantic Token이 뭐야?
A. `--color-primary`, `--color-error`처럼 UI 역할과 의미를 가진 token이다.

Q. Semantic Token은 왜 좋아?
A. 색상 값이 바뀌어도 컴포넌트는 역할 이름을 유지할 수 있어서 확장에 유리하다.

Q. 컴포넌트에서는 어떤 token을 써야 해?
A. 컴포넌트에서는 semantic token 또는 component token을 우선 사용한다.

Q. Dark Mode에 semantic token이 필요한 이유는?
A. 컴포넌트 코드를 바꾸지 않고 theme 값만 교체할 수 있기 때문이다.

---

## 2.3 Component Token

### [개념]

Component Token은 특정 컴포넌트의 스타일 속성을 관리하는 token이다.

Component Token은 semantic token을 기반으로 Button, Input, Card, Modal 같은 컴포넌트의 세부 스타일을 정의한다.

---

### [핵심]

Component Token 예:

```text
--button-primary-background
--button-primary-background-hover
--button-primary-text
--button-height-md
--button-radius

--input-border
--input-border-focus
--input-border-error
--input-background
--input-text

--card-background
--card-border
--card-radius
--card-shadow

--modal-background
--modal-radius
--modal-shadow
--modal-z-index
```

Component Token 특징:

- 특정 컴포넌트 기준
- semantic token 기반
- 컴포넌트 스타일 변경에 유리
- variant / state 표현에 유리
- 공통 컴포넌트 규모가 커질 때 사용 권장

---

### [실무]

Button Component Token 예:

```css
:root {
  --button-primary-background: var(--color-primary);
  --button-primary-background-hover: var(--color-primary-hover);
  --button-primary-text: var(--color-on-primary);
  --button-height-md: 40px;
  --button-padding-x-md: var(--spacing-4);
  --button-radius: var(--radius-button);
}
```

Button Style 예:

```css
.button {
  height: var(--button-height-md);
  padding: 0 var(--button-padding-x-md);
  border-radius: var(--button-radius);
}

.button[data-variant="primary"] {
  background: var(--button-primary-background);
  color: var(--button-primary-text);
}

.button[data-variant="primary"]:hover {
  background: var(--button-primary-background-hover);
}
```

작은 프로젝트에서는 semantic token만으로 시작해도 된다.

컴포넌트가 복잡해지면 component token을 추가한다.

---

### [FAQ]

Q. Component Token이 뭐야?
A. Button, Input, Card 같은 특정 컴포넌트의 스타일 속성을 관리하는 token이다.

Q. Component Token은 꼭 필요해?
A. 작은 프로젝트에서는 필수는 아니다. 컴포넌트 variant와 state가 많아지면 유용하다.

Q. Semantic Token과 Component Token은 뭐가 달라?
A. Semantic Token은 UI 역할 기준이고, Component Token은 특정 컴포넌트 스타일 기준이다.

Q. Button 색상은 semantic token만 써도 돼?
A. 가능하다. 다만 Button variant가 많아지면 component token으로 분리하는 것이 좋다.

---

## 2.4 Token Hierarchy

### [개념]

Token Hierarchy는 token을 원시 값에서 컴포넌트 스타일까지 단계적으로 연결하는 구조다.

Token Hierarchy를 명확히 하면 theme 변경과 컴포넌트 스타일 변경이 안정적으로 이루어진다.

---

### [핵심]

권장 Token Hierarchy:

```text
Primitive Token
→ Semantic Token
→ Component Token
→ Component Style
```

예:

```text
--blue-600
→ --color-primary
→ --button-primary-background
→ .button[data-variant="primary"]
```

금지 흐름:

```text
Raw Value
→ Component Style
```

비권장 예:

```css
.button {
  background: #2563eb;
}
```

권장 예:

```css
.button {
  background: var(--button-primary-background);
}
```

---

### [실무]

Token Hierarchy 예:

```css
:root {
  /* Primitive */
  --blue-600: #2563eb;
  --blue-700: #1d4ed8;
  --white: #ffffff;

  /* Semantic */
  --color-primary: var(--blue-600);
  --color-primary-hover: var(--blue-700);
  --color-on-primary: var(--white);

  /* Component */
  --button-primary-background: var(--color-primary);
  --button-primary-background-hover: var(--color-primary-hover);
  --button-primary-text: var(--color-on-primary);
}
```

사용:

```css
.button[data-variant="primary"] {
  background: var(--button-primary-background);
  color: var(--button-primary-text);
}
```

Review 기준:

```md
- [ ] raw value가 컴포넌트에 직접 흩어져 있지 않은가?
- [ ] primitive token과 semantic token 역할이 구분되는가?
- [ ] component token이 필요한 복잡도인지 판단했는가?
- [ ] theme 변경 시 컴포넌트 수정이 최소화되는가?
```

---

### [FAQ]

Q. Token Hierarchy가 왜 필요해?
A. 디자인 값 변경, theme 변경, 컴포넌트 스타일 변경을 안전하게 분리하기 위해 필요하다.

Q. Primitive Token에서 바로 Component Style로 가면 안 돼?
A. 가능하지만 theme 변경과 의미 관리가 어려워진다.

Q. 가장 권장되는 token 흐름은 뭐야?
A. Primitive Token → Semantic Token → Component Token → Component Style 흐름이다.

Q. 작은 프로젝트도 Component Token까지 필요해?
A. 아니다. 작은 프로젝트는 Primitive + Semantic Token으로 시작해도 충분하다.

---

# 3. Color Token Rules

## 3.1 Color Token Definition

### [개념]

Color Token은 UI 색상을 역할과 상태에 따라 관리하는 token이다.

Color Token은 버튼, 텍스트, 배경, 테두리, 상태 메시지, focus ring, disabled 상태, theme 변경의 기준이다.

---

### [핵심]

필수 Color Token:

```text
--color-primary
--color-primary-hover
--color-primary-active
--color-background
--color-surface
--color-surface-muted
--color-text
--color-text-muted
--color-border
--color-border-strong
--color-error
--color-warning
--color-success
--color-info
--color-disabled
--color-focus-ring
```

추가 권장 Color Token:

```text
--color-on-primary
--color-on-error
--color-on-success
--color-overlay
--color-backdrop
--color-link
--color-link-hover
```

---

### [실무]

Color Token 예:

```css
:root {
  --color-primary: #2563eb;
  --color-primary-hover: #1d4ed8;
  --color-primary-active: #1e40af;

  --color-background: #ffffff;
  --color-surface: #f9fafb;
  --color-surface-muted: #f3f4f6;

  --color-text: #111827;
  --color-text-muted: #6b7280;

  --color-border: #e5e7eb;
  --color-border-strong: #d1d5db;

  --color-error: #dc2626;
  --color-warning: #f59e0b;
  --color-success: #16a34a;
  --color-info: #0284c7;

  --color-disabled: #d1d5db;
  --color-focus-ring: #2563eb;

  --color-on-primary: #ffffff;
  --color-overlay: rgb(0 0 0 / 0.5);
}
```

Color Token Review:

```md
- [ ] 상태 색상이 semantic token으로 분리되어 있는가?
- [ ] hover / active 색상이 정의되어 있는가?
- [ ] text / muted / border / surface가 구분되어 있는가?
- [ ] error를 색상만으로 전달하지 않는가?
- [ ] focus-ring 색상이 정의되어 있는가?
- [ ] dark mode 대응 가능성이 있는가?
```

---

### [FAQ]

Q. Color Token은 어떤 것이 필요해?
A. primary, background, surface, text, muted, border, error, warning, success, info, disabled, focus-ring이 필요하다.

Q. Error 색상은 그냥 red로 쓰면 안 돼?
A. 가능하지만 `--color-error` 같은 semantic token으로 관리하는 것이 좋다.

Q. Text color와 muted color를 나눠야 해?
A. 권장된다. 본문 텍스트와 보조 텍스트의 계층을 명확히 관리할 수 있다.

Q. Focus ring 색상도 token이 필요해?
A. 필요하다. 접근성과 theme 대응을 위해 `--color-focus-ring`을 정의하는 것이 좋다.

---

## 3.2 State Color Token

### [개념]

State Color Token은 hover, active, focus, disabled, error, success 같은 UI 상태를 표현하는 색상 token이다.

State Color Token은 컴포넌트 상태가 일관되게 표현되도록 만든다.

---

### [핵심]

상태별 Color Token:

```text
hover
active
focus
disabled
error
success
warning
info
selected
checked
open
```

예:

```text
--color-primary-hover
--color-primary-active
--color-border-focus
--color-border-error
--color-background-disabled
--color-text-disabled
--color-surface-selected
```

필수 상태:

- hover
- active
- focus
- disabled
- error
- success

---

### [실무]

State Color Token 예:

```css
:root {
  --color-primary: #2563eb;
  --color-primary-hover: #1d4ed8;
  --color-primary-active: #1e40af;

  --color-border-focus: #2563eb;
  --color-border-error: #dc2626;

  --color-background-disabled: #f3f4f6;
  --color-text-disabled: #9ca3af;

  --color-surface-selected: #eff6ff;
}
```

Input 상태 예:

```css
.input {
  border-color: var(--color-border);
}

.input:focus {
  border-color: var(--color-border-focus);
}

.input[aria-invalid="true"] {
  border-color: var(--color-border-error);
}

.input:disabled {
  background: var(--color-background-disabled);
  color: var(--color-text-disabled);
}
```

---

### [FAQ]

Q. State Color Token이 뭐야?
A. hover, active, focus, disabled, error 같은 상태를 표현하는 색상 token이다.

Q. hover 색상을 따로 정의해야 해?
A. 권장된다. hover / active 색상이 없으면 상태 표현이 화면마다 달라질 수 있다.

Q. disabled 색상은 왜 분리해?
A. 비활성 상태를 일관되게 표현하고 접근성 검토를 쉽게 하기 위해서다.

Q. error 상태는 색상만 있으면 충분해?
A. 아니다. error message와 aria 속성도 함께 필요하다.

---

## 3.3 Semantic Color Usage

### [개념]

Semantic Color Usage는 색상 값을 직접 사용하는 대신 UI 의미에 맞는 semantic color token을 사용하는 규칙이다.

---

### [핵심]

권장 사용:

```text
주요 행동
→ --color-primary

오류
→ --color-error

경고
→ --color-warning

성공
→ --color-success

정보
→ --color-info

본문
→ --color-text

보조 텍스트
→ --color-text-muted

배경
→ --color-background

표면
→ --color-surface

테두리
→ --color-border
```

비권장 사용:

```text
blue = primary로 가정
red = error로 가정
gray = disabled로 가정
```

색상 이름보다 의미 token을 우선한다.

---

### [실무]

나쁜 예:

```css
.deleteButton {
  background: red;
}

.card {
  background: #f9fafb;
}

.mutedText {
  color: gray;
}
```

좋은 예:

```css
.deleteButton {
  background: var(--color-error);
  color: var(--color-on-error);
}

.card {
  background: var(--color-surface);
}

.mutedText {
  color: var(--color-text-muted);
}
```

Review 기준:

```md
- [ ] 색상 값이 의미 token으로 표현되는가?
- [ ] primary / error / warning / success 의미가 구분되는가?
- [ ] 색상 이름이 컴포넌트 의미를 대신하고 있지 않은가?
- [ ] theme 변경 시 안전한가?
```

---

### [FAQ]

Q. Semantic Color는 왜 써야 해?
A. 색상 값보다 UI 의미를 기준으로 관리해야 theme 변경과 유지보수가 쉬워지기 때문이다.

Q. danger 버튼에 red를 직접 쓰면 안 돼?
A. 공통 컴포넌트에서는 `--color-error` 또는 `--button-danger-background`를 사용하는 것이 좋다.

Q. 회색 텍스트는 그냥 gray로 쓰면 안 돼?
A. 보조 텍스트라면 `--color-text-muted` 같은 의미 token을 사용하는 것이 좋다.

Q. 색상이 같으면 같은 token을 써도 돼?
A. 의미가 다르면 분리하는 것이 좋다. 같은 값이어도 역할이 다르면 다른 semantic token이 될 수 있다.

---

## 3.4 Color Token Mistakes

### [개념]

Color Token Mistakes는 색상 token을 사용할 때 자주 발생하는 실수다.

Color Token 실수는 UI 일관성, theme 확장성, 접근성 문제로 이어진다.

---

### [핵심]

자주 발생하는 실수:

- raw hex color 직접 사용
- `red`, `blue`, `gray` 색상명 남발
- hover / active 색상 누락
- text / muted / border 구분 없음
- background / surface 구분 없음
- error를 색상만으로 표시
- disabled 색상이 너무 흐림
- focus ring 색상 누락
- dark mode에서 contrast 깨짐
- 상태 색상과 문구 불일치
- 컴포넌트마다 다른 primary 색상 사용

---

### [실무]

Troubleshooting:

```text
버튼 색상이 화면마다 다름
→ --color-primary / Button Component Token 확인

에러 색상만 표시됨
→ error message / aria-invalid / color-error 확인

Dark Mode에서 글자가 안 보임
→ background / surface / text token 확인

disabled 텍스트가 너무 흐림
→ color contrast 확인

focus 표시가 안 보임
→ --color-focus-ring 확인
```

Review Checklist:

```md
- [ ] raw color가 반복 사용되지 않는가?
- [ ] 상태 색상이 token으로 정의되어 있는가?
- [ ] 색상만으로 상태를 전달하지 않는가?
- [ ] dark mode에서 text contrast가 유지되는가?
- [ ] focus ring이 모든 theme에서 보이는가?
```

---

### [FAQ]

Q. Color Token에서 가장 흔한 실수는?
A. 색상 값을 직접 쓰고 의미 token 없이 화면마다 다른 색상을 사용하는 것이다.

Q. background와 surface를 구분해야 해?
A. 권장된다. 페이지 배경과 카드 / 모달 표면을 분리하면 theme 대응이 쉬워진다.

Q. disabled 색상은 흐리게만 하면 돼?
A. 아니다. 비활성 상태를 표현하되 필요한 텍스트는 읽을 수 있어야 한다.

Q. focus ring이 안 보이면 왜 문제야?
A. 키보드 사용자가 현재 위치를 알 수 없어 접근성 문제가 된다.

---

# 4. Spacing Token Rules

## 4.1 Spacing Token Definition

### [개념]

Spacing Token은 margin, padding, gap에 사용하는 간격 값을 일정한 scale로 관리하는 token이다.

Spacing Token은 화면마다 간격이 제각각이 되는 것을 막고 UI 리듬을 유지한다.

---

### [핵심]

권장 spacing scale:

```css
:root {
  --spacing-0: 0;
  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-3: 12px;
  --spacing-4: 16px;
  --spacing-5: 20px;
  --spacing-6: 24px;
  --spacing-8: 32px;
  --spacing-10: 40px;
  --spacing-12: 48px;
  --spacing-16: 64px;
}
```

Spacing 적용 대상:

- padding
- margin
- gap
- section spacing
- form field spacing
- card spacing
- layout spacing
- stack spacing
- grid spacing

---

### [실무]

Spacing 사용 기준:

```text
Component 내부 간격
→ padding / gap

Component 외부 배치
→ parent layout gap

Page section 간격
→ layout token

Form field 간격
→ form pattern token

List item 간격
→ grid / stack gap
```

나쁜 예:

```css
.card {
  padding: 17px;
  margin-bottom: 23px;
}
```

좋은 예:

```css
.card {
  padding: var(--spacing-4);
}

.cardList {
  display: grid;
  gap: var(--spacing-6);
}
```

---

### [FAQ]

Q. Spacing Token은 왜 필요해?
A. 화면마다 margin, padding, gap이 제각각이 되는 것을 막고 UI 리듬을 유지하기 위해 필요하다.

Q. spacing scale은 어떤 기준이 좋아?
A. 4px 또는 8px 기반 scale을 많이 사용한다. 프로젝트에서는 하나의 기준으로 통일해야 한다.

Q. 모든 margin과 padding을 token으로 써야 해?
A. 반복되는 간격과 공통 UI 간격은 token으로 관리하는 것이 좋다.

Q. 임의로 17px 같은 값을 써도 돼?
A. 특별한 이유가 없으면 피해야 한다. spacing token을 우선 사용한다.

---

## 4.2 Margin Gap Padding Rules

### [개념]

Margin, Gap, Padding Rules는 spacing token을 어디에 적용할지 결정하는 기준이다.

재사용 컴포넌트는 외부 margin을 최소화하고, 부모 layout이 gap으로 배치를 담당하는 것이 좋다.

---

### [핵심]

사용 기준:

```text
padding
→ 컴포넌트 내부 여백

gap
→ 부모 layout에서 자식 요소 사이 간격

margin
→ 문맥상 필요한 예외적 외부 간격

section spacing
→ 페이지 섹션 사이 간격

layout gap
→ grid / stack / inline 배치 간격
```

권장:

- Card 내부 여백은 padding
- Card 목록 간격은 parent grid gap
- Form Field 사이 간격은 form layout gap
- Button 내부 좌우 여백은 padding
- Header와 Section 간격은 layout token

비권장:

- 모든 컴포넌트에 margin-bottom 직접 지정
- 재사용 컴포넌트가 외부 배치까지 담당
- 화면마다 임의 px 사용

---

### [실무]

나쁜 예:

```css
.card {
  margin-bottom: 24px;
}

.input {
  margin-bottom: 18px;
}
```

좋은 예:

```css
.cardGrid {
  display: grid;
  gap: var(--spacing-6);
}

.formStack {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-4);
}
```

Component 내부 padding:

```css
.card {
  padding: var(--spacing-4);
}

.button {
  padding: 0 var(--spacing-4);
}
```

---

### [FAQ]

Q. margin과 gap 중 뭐가 좋아?
A. 리스트나 레이아웃 요소 사이 간격은 gap이 더 명확한 경우가 많다.

Q. 컴포넌트에 margin을 직접 주면 안 돼?
A. 재사용 컴포넌트라면 외부 배치는 부모 layout이 담당하는 것이 좋다.

Q. padding은 언제 써?
A. 컴포넌트 내부 콘텐츠와 테두리 사이 여백을 줄 때 사용한다.

Q. Form Field 사이 간격은 어떻게 관리해?
A. 개별 Form Field margin보다 form parent의 gap으로 관리하는 것이 좋다.

---

## 4.3 Layout Spacing Rules

### [개념]

Layout Spacing Rules는 페이지 레이아웃, 섹션, 컨테이너, 그리드, 스택 구조의 간격을 관리하는 기준이다.

Layout Spacing은 컴포넌트 spacing보다 큰 단위의 화면 구조를 담당한다.

---

### [핵심]

Layout Spacing 대상:

- Page Container padding
- Section gap
- Grid gap
- Stack gap
- Sidebar gap
- Header spacing
- Footer spacing
- Content width
- Form layout spacing

권장 layout token:

```text
--layout-page-padding
--layout-section-gap
--layout-container-max-width
--layout-grid-gap
--layout-stack-gap
```

---

### [실무]

Layout Token 예:

```css
:root {
  --layout-page-padding: var(--spacing-4);
  --layout-section-gap: var(--spacing-10);
  --layout-grid-gap: var(--spacing-6);
  --layout-container-max-width: 1200px;
}
```

Container 예:

```css
.container {
  width: min(
    100% - calc(var(--layout-page-padding) * 2),
    var(--layout-container-max-width)
  );
  margin: 0 auto;
}
```

Section 예:

```css
.page {
  display: flex;
  flex-direction: column;
  gap: var(--layout-section-gap);
}
```

Grid 예:

```css
.cardGrid {
  display: grid;
  gap: var(--layout-grid-gap);
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}
```

---

### [FAQ]

Q. Layout Spacing과 Component Spacing은 뭐가 달라?
A. Layout Spacing은 페이지와 섹션 배치 간격이고, Component Spacing은 컴포넌트 내부 간격이다.

Q. Page padding도 token으로 관리해야 해?
A. 권장된다. 모바일과 데스크톱에서 일관된 화면 여백을 유지할 수 있다.

Q. Section gap은 왜 필요해?
A. 페이지마다 섹션 간격이 달라지는 것을 막기 위해 필요하다.

Q. Grid gap은 어디서 관리해?
A. Card 자체가 아니라 Card Grid 같은 부모 layout에서 관리한다.

---

## 4.4 Spacing Token Mistakes

### [개념]

Spacing Token Mistakes는 간격 값 관리에서 자주 발생하는 실수다.

Spacing 실수는 화면이 어수선해지고 컴포넌트 재사용성이 떨어지는 원인이 된다.

---

### [핵심]

자주 발생하는 실수:

- 임의 px 값 남발
- 화면마다 다른 padding 사용
- card 내부와 외부 spacing 혼동
- 재사용 컴포넌트에 margin 직접 지정
- parent gap 대신 child margin 사용
- section spacing 기준 없음
- form field 간격 불일치
- 모바일 padding 과도함
- desktop spacing만 고려
- spacing scale 없이 감각으로 작성

---

### [실무]

Troubleshooting:

```text
화면 간격이 제각각
→ spacing scale 확인

카드 목록 간격이 다름
→ parent grid gap 확인

Form 간격이 불일치
→ form stack gap 확인

모바일에서 여백이 너무 큼
→ responsive layout padding 확인

컴포넌트 재사용 시 간격 깨짐
→ component margin 제거, parent gap 사용
```

Review Checklist:

```md
- [ ] spacing token scale이 있는가?
- [ ] 임의 px 값이 남발되지 않는가?
- [ ] component 내부 padding과 외부 layout gap이 분리되는가?
- [ ] form spacing이 일관적인가?
- [ ] 모바일 spacing이 과하지 않은가?
```

---

### [FAQ]

Q. Spacing에서 가장 흔한 실수는?
A. 화면마다 임의 px 값을 사용하고 재사용 컴포넌트에 margin을 직접 넣는 것이다.

Q. Card에 margin-bottom을 넣으면 안 돼?
A. 재사용 Card라면 권장하지 않는다. Card 목록의 부모가 gap으로 관리하는 것이 좋다.

Q. 모바일 spacing도 따로 봐야 해?
A. 봐야 한다. 데스크톱 기준 spacing이 모바일에서 과도할 수 있다.

Q. spacing token 없이도 화면은 만들 수 있지 않아?
A. 가능하지만 화면이 늘어날수록 일관성과 유지보수가 어려워진다.

---

# 5. Typography Token Rules

## 5.1 Typography Token Definition

### [개념]

Typography Token은 글자의 크기, 굵기, 줄 간격, 폰트 패밀리를 관리하는 token이다.

Typography Token은 제목, 본문, 보조 텍스트, 캡션, 버튼 텍스트의 계층을 일관되게 만든다.

---

### [핵심]

필수 Typography Token:

```text
--font-family-base
--font-family-mono
--font-size-xs
--font-size-sm
--font-size-md
--font-size-lg
--font-size-xl
--font-size-2xl
--font-size-3xl
--font-weight-regular
--font-weight-medium
--font-weight-semibold
--font-weight-bold
--line-height-tight
--line-height-base
--line-height-relaxed
```

적용 대상:

- Page Title
- Section Title
- Card Title
- Body Text
- Caption
- Button Text
- Form Label
- Helper Text
- Error Message
- Table Text

---

### [실무]

Typography Token 예:

```css
:root {
  --font-family-base: system-ui, sans-serif;
  --font-family-mono: ui-monospace, SFMono-Regular, Menlo, monospace;

  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-md: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --font-size-3xl: 2rem;

  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  --line-height-tight: 1.25;
  --line-height-base: 1.5;
  --line-height-relaxed: 1.7;
}
```

Typography hierarchy 예:

```text
Page Title
→ font-size-3xl / bold / tight

Section Title
→ font-size-2xl / bold / tight

Card Title
→ font-size-lg / bold / base

Body
→ font-size-md / regular / base

Caption
→ font-size-sm / regular / base

Error Message
→ font-size-sm / regular / base
```

---

### [FAQ]

Q. Typography Token은 뭘 관리해?
A. font-size, font-weight, line-height, font-family 같은 글자 스타일을 관리한다.

Q. font-size를 px로 직접 쓰면 안 돼?
A. 가능하지만 token과 rem 단위를 사용하면 접근성과 일관성에 더 좋다.

Q. heading tag와 typography style은 같아야 해?
A. heading tag는 의미 구조이고, 시각 스타일은 typography token으로 관리한다.

Q. 버튼 텍스트도 typography token을 써야 해?
A. 권장된다. 버튼 크기와 텍스트 크기가 size 체계와 함께 일관되어야 한다.

---

## 5.2 Typography Hierarchy Rules

### [개념]

Typography Hierarchy Rules는 화면에서 제목, 본문, 보조 문구, 캡션의 시각적 계층을 정하는 기준이다.

Typography Hierarchy는 사용자가 정보 구조를 빠르게 이해하도록 돕는다.

---

### [핵심]

Typography 계층:

```text
Display
→ Page Title
→ Section Title
→ Card Title
→ Body
→ Caption
→ Helper Text
```

기준:

- 제목은 크기와 굵기로 계층 표현
- 본문은 가독성 우선
- 보조 텍스트는 muted color와 작은 font-size 사용
- Error Message는 색상 + 문구로 상태 표현
- Button Text는 짧고 명확한 동사 사용
- heading tag와 시각 스타일을 혼동하지 않음

---

### [실무]

나쁜 예:

```css
.pageTitle {
  font-size: 31px;
  font-weight: 700;
}

.cardTitle {
  font-size: 19px;
  font-weight: 650;
}

.caption {
  font-size: 13px;
}
```

좋은 예:

```css
.pageTitle {
  font-size: var(--font-size-3xl);
  font-weight: var(--font-weight-bold);
  line-height: var(--line-height-tight);
}

.cardTitle {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-bold);
  line-height: var(--line-height-base);
}

.caption {
  font-size: var(--font-size-sm);
  color: var(--color-text-muted);
}
```

---

### [FAQ]

Q. Typography Hierarchy가 왜 필요해?
A. 사용자가 제목, 본문, 보조 정보를 빠르게 구분할 수 있어야 하기 때문이다.

Q. 제목은 항상 h1, h2 크기와 같아야 해?
A. 아니다. heading tag는 의미 구조이고 시각 크기는 typography token으로 조정할 수 있다.

Q. Caption은 어떻게 표현해?
A. 작은 font-size와 muted color를 사용하되 읽을 수 있어야 한다.

Q. Error Message는 어떤 typography를 써?
A. 보통 `font-size-sm`과 error color를 사용하고, 입력 필드 가까이에 표시한다.

---

## 5.3 Typography Token Mistakes

### [개념]

Typography Token Mistakes는 글자 스타일을 일관성 없이 작성할 때 발생하는 실수다.

Typography 실수는 정보 계층을 흐리고 화면 가독성을 낮춘다.

---

### [핵심]

자주 발생하는 실수:

- font-size 직접 px 남발
- heading tag를 시각 스타일 용도로만 사용
- line-height 누락
- 본문 line-height가 너무 좁음
- 보조 텍스트가 너무 흐림
- 버튼 텍스트 크기 불일치
- form label 크기 불일치
- error message 스타일 불일치
- font-weight 임의 값 사용
- 모바일에서 제목이 과도하게 큼

---

### [실무]

Troubleshooting:

```text
화면 제목 크기가 제각각
→ typography hierarchy 확인

본문이 읽기 어려움
→ line-height-base 확인

보조 텍스트가 안 보임
→ color-text-muted contrast 확인

버튼 텍스트 크기가 다름
→ button size typography 확인

모바일에서 제목이 큼
→ responsive typography 확인
```

Review Checklist:

```md
- [ ] typography token scale이 있는가?
- [ ] heading 의미와 시각 스타일이 분리되어 있는가?
- [ ] line-height가 정의되어 있는가?
- [ ] 본문 텍스트 가독성이 충분한가?
- [ ] 모바일에서 글자 크기가 적절한가?
```

---

### [FAQ]

Q. Typography에서 가장 흔한 실수는?
A. font-size를 화면마다 직접 지정하고 제목, 본문, 보조 텍스트 계층을 통일하지 않는 것이다.

Q. line-height는 꼭 필요해?
A. 필요하다. 본문 가독성과 UI 밀도에 큰 영향을 준다.

Q. 보조 텍스트는 흐리게 하면 돼?
A. 너무 흐리면 읽기 어렵다. muted color도 contrast를 고려해야 한다.

Q. 모바일에서 typography도 조정해야 해?
A. 필요하다. 데스크톱 제목 크기가 모바일에서 과도할 수 있다.

---

# 6. Radius Shadow Z-index Token Rules

## 6.1 Radius Token Rules

### [개념]

Radius Token은 Button, Card, Modal, Input 같은 UI 요소의 모서리 둥글기를 일관되게 관리하는 token이다.

---

### [핵심]

권장 Radius Token:

```css
:root {
  --radius-none: 0;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-full: 9999px;

  --radius-button: var(--radius-md);
  --radius-input: var(--radius-md);
  --radius-card: var(--radius-lg);
  --radius-modal: var(--radius-lg);
}
```

사용 기준:

```text
Button
→ radius-button

Input
→ radius-input

Card
→ radius-card

Modal
→ radius-modal

Badge / Tag
→ radius-full 또는 radius-sm
```

---

### [실무]

나쁜 예:

```css
.button {
  border-radius: 7px;
}

.card {
  border-radius: 13px;
}

.modal {
  border-radius: 11px;
}
```

좋은 예:

```css
.button {
  border-radius: var(--radius-button);
}

.card {
  border-radius: var(--radius-card);
}

.modal {
  border-radius: var(--radius-modal);
}
```

Review 기준:

```md
- [ ] radius scale이 정의되어 있는가?
- [ ] Button / Input / Card / Modal radius가 일관적인가?
- [ ] 임의 radius 값이 남발되지 않는가?
- [ ] badge / pill 형태는 radius-full을 사용하는가?
```

---

### [FAQ]

Q. Radius Token은 왜 필요해?
A. Button, Card, Modal의 모서리 둥글기를 일관되게 관리하기 위해 필요하다.

Q. 모든 컴포넌트가 같은 radius를 써야 해?
A. 아니다. Button, Card, Modal의 목적에 따라 token을 다르게 사용할 수 있다.

Q. `9999px` radius는 언제 써?
A. Badge, Tag, pill button처럼 완전히 둥근 형태에 사용한다.

Q. radius를 직접 px로 써도 돼?
A. 반복되는 컴포넌트에서는 token을 사용하는 것이 좋다.

---

## 6.2 Shadow Token Rules

### [개념]

Shadow Token은 Card, Modal, Dropdown, Toast 같은 UI의 깊이 표현을 일관되게 관리하는 token이다.

---

### [핵심]

권장 Shadow Token:

```css
:root {
  --shadow-none: none;
  --shadow-sm: 0 1px 2px rgb(0 0 0 / 0.08);
  --shadow-md: 0 4px 12px rgb(0 0 0 / 0.12);
  --shadow-lg: 0 12px 24px rgb(0 0 0 / 0.16);

  --shadow-card: var(--shadow-sm);
  --shadow-dropdown: var(--shadow-md);
  --shadow-modal: var(--shadow-lg);
  --shadow-toast: var(--shadow-md);
}
```

사용 기준:

```text
Card
→ shadow-card

Dropdown
→ shadow-dropdown

Modal
→ shadow-modal

Toast
→ shadow-toast
```

---

### [실무]

나쁜 예:

```css
.card {
  box-shadow: 2px 4px 8px #ccc;
}

.modal {
  box-shadow: 0 0 999px black;
}
```

좋은 예:

```css
.card {
  box-shadow: var(--shadow-card);
}

.modal {
  box-shadow: var(--shadow-modal);
}
```

Dark Mode 주의:

```text
Dark Mode에서는 shadow만으로 depth가 잘 보이지 않을 수 있다.
surface 색상, border, overlay를 함께 조정한다.
```

Review 기준:

```md
- [ ] shadow scale이 정의되어 있는가?
- [ ] card / modal / dropdown shadow 기준이 있는가?
- [ ] 과도한 shadow가 사용되지 않는가?
- [ ] dark mode depth 표현을 고려했는가?
```

---

### [FAQ]

Q. Shadow Token은 왜 필요해?
A. Card, Modal, Toast 같은 UI의 깊이 표현을 일관되게 관리하기 위해 필요하다.

Q. shadow는 많을수록 좋아?
A. 아니다. depth 표현이 필요한 곳에 제한적으로 사용해야 UI가 복잡해지지 않는다.

Q. Dark Mode에서도 shadow가 잘 보여?
A. 항상 그렇지 않다. surface, border, overlay를 함께 조정해야 한다.

Q. Card와 Modal shadow는 같아도 돼?
A. 가능하지만 Modal은 보통 더 높은 depth를 표현하므로 더 강한 shadow를 사용한다.

---

## 6.3 Z-index Token Rules

### [개념]

Z-index Token은 Header, Dropdown, Overlay, Modal, Toast 같은 UI의 겹침 순서를 예측 가능하게 관리하는 token이다.

---

### [핵심]

권장 Z-index Token:

```css
:root {
  --z-base: 0;
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-header: 300;
  --z-overlay: 900;
  --z-modal: 1000;
  --z-popover: 1050;
  --z-toast: 1100;
}
```

겹침 순서:

```text
base
→ dropdown
→ sticky
→ header
→ overlay
→ modal
→ popover
→ toast
```

금지:

```css
.modal {
  z-index: 9999;
}
```

권장:

```css
.modal {
  z-index: var(--z-modal);
}
```

---

### [실무]

사용 기준:

```css
.header {
  z-index: var(--z-header);
}

.dropdown {
  z-index: var(--z-dropdown);
}

.modalOverlay {
  z-index: var(--z-overlay);
}

.modal {
  z-index: var(--z-modal);
}

.toastContainer {
  z-index: var(--z-toast);
}
```

Review 기준:

```md
- [ ] z-index scale이 정의되어 있는가?
- [ ] modal / toast / dropdown 순서가 예측 가능한가?
- [ ] 9999 같은 임의 값이 사용되지 않는가?
- [ ] overlay와 modal z-index가 구분되는가?
```

---

### [FAQ]

Q. Z-index Token은 왜 필요해?
A. Modal, Toast, Dropdown, Header의 겹침 순서를 예측 가능하게 관리하기 위해 필요하다.

Q. z-index는 그냥 9999로 쓰면 안 돼?
A. 권장하지 않는다. token scale로 관리해야 겹침 순서가 무너지지 않는다.

Q. Toast는 Modal보다 위에 있어야 해?
A. 프로젝트 정책에 따라 다르지만 보통 Toast가 가장 위에 표시되는 경우가 많다.

Q. Overlay와 Modal의 z-index는 같아도 돼?
A. 구분하는 것이 좋다. Overlay는 Modal보다 아래에 있어야 한다.

---

# 7. Motion Breakpoint Opacity Token Rules

## 7.1 Motion Token Rules

### [개념]

Motion Token은 transition duration, easing, animation timing을 관리하는 token이다.

Motion Token은 hover, modal open, toast, dropdown 같은 상호작용의 움직임을 일관되게 만든다.

---

### [핵심]

권장 Motion Token:

```css
:root {
  --duration-fast: 150ms;
  --duration-base: 250ms;
  --duration-slow: 400ms;

  --easing-standard: ease;
  --easing-emphasized: cubic-bezier(0.2, 0, 0, 1);
}
```

적용 대상:

- Button hover
- Link hover
- Modal open / close
- Toast enter / exit
- Dropdown open / close
- Skeleton shimmer
- Drawer slide

---

### [실무]

Button transition 예:

```css
.button {
  transition:
    background-color var(--duration-fast) var(--easing-standard),
    transform var(--duration-fast) var(--easing-standard);
}
```

Reduced Motion 대응:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms;
    animation-iteration-count: 1;
    transition-duration: 0.01ms;
    scroll-behavior: auto;
  }
}
```

Motion Review:

```md
- [ ] transition duration이 token으로 관리되는가?
- [ ] motion이 사용성을 돕는가?
- [ ] prefers-reduced-motion을 고려했는가?
- [ ] 과도한 animation이 없는가?
```

---

### [FAQ]

Q. Motion Token은 왜 필요해?
A. transition duration과 easing을 일관되게 관리하기 위해 필요하다.

Q. 애니메이션은 많을수록 좋아?
A. 아니다. 사용성을 돕는 수준으로 제한해야 한다.

Q. prefers-reduced-motion은 왜 필요해?
A. 움직임에 민감한 사용자가 animation을 줄일 수 있어야 하기 때문이다.

Q. Button hover에도 Motion Token을 써야 해?
A. 권장된다. hover 반응 속도가 UI 전체에서 일관되어야 한다.

---

## 7.2 Breakpoint Token Rules

### [개념]

Breakpoint Token은 반응형 화면 전환 기준을 관리하는 token이다.

Breakpoint Token은 모바일, 태블릿, 데스크톱, 와이드 화면의 layout 기준을 통일한다.

---

### [핵심]

권장 breakpoint:

```text
mobile: default
tablet: 768px
desktop: 1024px
wide: 1280px
```

CSS 변수 예:

```css
:root {
  --breakpoint-tablet: 768px;
  --breakpoint-desktop: 1024px;
  --breakpoint-wide: 1280px;
}
```

주의:

```text
CSS custom property는 media query 조건에서 직접 사용이 제한된다.
빌드 도구, preprocessor, JS constant, CSS-in-JS theme에서 breakpoint token을 관리할 수 있다.
```

---

### [실무]

CSS media query 예:

```css
.cardGrid {
  display: grid;
  gap: var(--spacing-4);
  grid-template-columns: 1fr;
}

@media (min-width: 768px) {
  .cardGrid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .cardGrid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

JS / TS breakpoint constant 예:

```ts
export const breakpoints = {
  tablet: 768,
  desktop: 1024,
  wide: 1280,
} as const;
```

Review 기준:

```md
- [ ] breakpoint 기준이 문서화되어 있는가?
- [ ] Mobile First 기준인가?
- [ ] 카드 목록이 화면 크기에 따라 자연스럽게 변하는가?
- [ ] Table / Modal / Navigation 모바일 대응이 있는가?
```

---

### [FAQ]

Q. Breakpoint Token은 왜 필요해?
A. 컴포넌트와 레이아웃이 같은 반응형 기준을 공유해야 하기 때문이다.

Q. 기본 breakpoint는 뭐가 좋아?
A. mobile default, tablet 768px, desktop 1024px, wide 1280px 기준을 사용할 수 있다.

Q. CSS 변수로 media query를 직접 작성할 수 있어?
A. 일반 CSS에서는 제한이 있다. 빌드 도구나 JS constant로 관리하는 방법을 고려한다.

Q. breakpoint는 고정값이야?
A. 아니다. 일반 기준은 있지만 콘텐츠가 깨지는 지점을 기준으로 조정할 수 있다.

---

## 7.3 Opacity Token Rules

### [개념]

Opacity Token은 disabled, overlay, backdrop, hover overlay 같은 투명도 값을 관리하는 token이다.

Opacity Token은 상태 표현과 레이어 표현을 일관되게 만든다.

---

### [핵심]

권장 Opacity Token:

```css
:root {
  --opacity-disabled: 0.5;
  --opacity-muted: 0.7;
  --opacity-overlay: 0.5;
  --opacity-hover: 0.08;
  --opacity-active: 0.12;
}
```

적용 대상:

- Disabled component
- Modal overlay
- Backdrop
- Hover overlay
- Skeleton opacity
- Muted icon
- Inactive item

주의:

- 텍스트 전체 opacity 남용 금지
- disabled text contrast 확인
- overlay opacity는 theme별 검토
- 색상 token과 함께 사용

---

### [실무]

Disabled 예:

```css
.button:disabled {
  opacity: var(--opacity-disabled);
  cursor: not-allowed;
}
```

Overlay 예:

```css
.modalOverlay {
  background: rgb(0 0 0 / var(--opacity-overlay));
}
```

주의 예:

```css
.formField {
  opacity: 0.4;
}
```

위 방식은 label, input, helper text 전체가 흐려져 가독성 문제가 생길 수 있다.

권장:

```css
.input:disabled {
  background: var(--color-background-disabled);
  color: var(--color-text-disabled);
}
```

---

### [FAQ]

Q. Opacity Token은 왜 필요해?
A. disabled, overlay, hover 같은 투명도 상태를 일관되게 관리하기 위해 필요하다.

Q. disabled는 opacity만 낮추면 돼?
A. 아니다. 텍스트 가독성과 상태 인지가 가능해야 하므로 색상 token도 함께 고려한다.

Q. overlay opacity는 어떻게 관리해?
A. `--opacity-overlay` 같은 token으로 관리하고 theme별로 contrast를 확인한다.

Q. 텍스트에 opacity를 많이 써도 돼?
A. 주의해야 한다. 텍스트 가독성과 접근성 contrast가 떨어질 수 있다.

---

# 8. Theme Token Rules

## 8.1 Theme Token Structure

### [개념]

Theme Token Structure는 Light Mode, Dark Mode, Brand Theme 같은 시각 테마를 token으로 전환할 수 있게 만드는 구조다.

Theme Token은 semantic token을 중심으로 설계해야 한다.

---

### [핵심]

Theme Token Flow:

```text
Primitive Token
→ Semantic Token
→ Theme Value
→ Component Style
```

Theme에서 반드시 관리할 token:

- background
- surface
- text
- text-muted
- border
- primary
- error
- warning
- success
- focus-ring
- overlay
- disabled

---

### [실무]

Light / Dark Theme 예:

```css
:root {
  --color-background: #ffffff;
  --color-surface: #f9fafb;
  --color-text: #111827;
  --color-text-muted: #6b7280;
  --color-border: #e5e7eb;
  --color-focus-ring: #2563eb;
}

[data-theme="dark"] {
  --color-background: #111827;
  --color-surface: #1f2937;
  --color-text: #f9fafb;
  --color-text-muted: #d1d5db;
  --color-border: #374151;
  --color-focus-ring: #60a5fa;
}
```

Component Style:

```css
.card {
  background: var(--color-surface);
  color: var(--color-text);
  border: 1px solid var(--color-border);
}
```

컴포넌트는 theme 이름을 몰라도 semantic token을 통해 자동 대응한다.

---

### [FAQ]

Q. Theme Token은 왜 필요해?
A. 컴포넌트 구조를 유지하면서 색상과 시각 스타일을 전환하기 위해 필요하다.

Q. Theme 구현에는 CSS variable이 좋아?
A. CSS variable은 런타임 theme 전환에 유리하다.

Q. Dark Mode는 배경만 바꾸면 돼?
A. 아니다. text, border, surface, disabled, hover, focus, icon까지 함께 조정해야 한다.

Q. 컴포넌트에서 raw color를 쓰면 왜 문제야?
A. theme 변경 시 컴포넌트마다 직접 수정해야 하므로 확장성이 떨어진다.

---

## 8.2 Dark Mode Token Rules

### [개념]

Dark Mode Token Rules는 어두운 배경에서 텍스트, 표면, 테두리, 상태 색상, focus ring이 충분히 보이도록 token을 정의하는 기준이다.

---

### [핵심]

Dark Mode 필수 확인:

```md
- [ ] background와 text contrast
- [ ] surface 색상
- [ ] border 색상
- [ ] muted text 색상
- [ ] disabled 색상
- [ ] hover 색상
- [ ] focus ring 색상
- [ ] shadow 대체
- [ ] icon visibility
- [ ] overlay 색상
```

Dark Mode Token 대상:

```text
--color-background
--color-surface
--color-surface-muted
--color-text
--color-text-muted
--color-border
--color-border-strong
--color-primary
--color-error
--color-warning
--color-success
--color-focus-ring
--color-background-disabled
--color-text-disabled
```

---

### [실무]

Dark Mode 예:

```css
[data-theme="dark"] {
  --color-background: #111827;
  --color-surface: #1f2937;
  --color-surface-muted: #374151;

  --color-text: #f9fafb;
  --color-text-muted: #d1d5db;

  --color-border: #374151;
  --color-border-strong: #4b5563;

  --color-primary: #60a5fa;
  --color-primary-hover: #93c5fd;

  --color-error: #f87171;
  --color-warning: #fbbf24;
  --color-success: #4ade80;
  --color-focus-ring: #93c5fd;

  --color-background-disabled: #374151;
  --color-text-disabled: #9ca3af;
}
```

Dark Mode Review:

```md
- [ ] raw color가 dark mode에서 깨지지 않는가?
- [ ] text / surface / border token이 재정의되는가?
- [ ] focus ring이 dark background에서 보이는가?
- [ ] shadow만으로 depth를 표현하지 않는가?
- [ ] icon 색상이 currentColor 또는 token을 사용하는가?
```

---

### [FAQ]

Q. Dark Mode Token에서 가장 중요한 것은?
A. background, surface, text, border, focus-ring contrast를 유지하는 것이다.

Q. Dark Mode는 배경만 검게 바꾸면 돼?
A. 아니다. text, border, surface, disabled, hover, focus, icon까지 함께 조정해야 한다.

Q. Dark Mode에서 shadow가 약하면 어떻게 해?
A. surface 색상, border, overlay를 함께 사용해 depth를 표현한다.

Q. Dark Mode에서 icon 색상은 어떻게 관리해?
A. `currentColor` 또는 semantic color token을 사용하는 것이 좋다.

---

# 9. Token Implementation Rules

## 9.1 CSS Variable Implementation

### [개념]

CSS Variable Implementation은 Design Token을 CSS custom property로 구현하는 방식이다.

CSS variable은 runtime theme 변경, component style 재사용, token cascade에 유리하다.

---

### [핵심]

CSS Variable 장점:

- 런타임 theme 전환 가능
- cascade 활용 가능
- 컴포넌트 스타일과 연결 쉬움
- CSS Modules / plain CSS / styled-components와 함께 사용 가능
- JavaScript 없이 기본 theme 적용 가능

기본 구조:

```css
:root {
  --color-primary: #2563eb;
  --spacing-4: 16px;
  --radius-md: 8px;
}
```

사용:

```css
.button {
  background: var(--color-primary);
  padding: var(--spacing-2) var(--spacing-4);
  border-radius: var(--radius-md);
}
```

---

### [실무]

권장 파일 구조:

```text
src/styles/tokens.css
src/styles/theme.css
src/styles/global.css
```

import 순서:

```css
@import "./tokens.css";
@import "./theme.css";
@import "./global.css";
```

React entry 예:

```tsx
import "./styles/tokens.css";
import "./styles/theme.css";
import "./styles/global.css";
```

Fallback 예:

```css
.button {
  background: var(--color-primary, #2563eb);
}
```

주의:

```text
fallback은 안전장치로만 사용한다.
반복 fallback으로 token 누락을 숨기지 않는다.
```

---

### [FAQ]

Q. CSS Variable로 token을 구현해도 돼?
A. 권장된다. CSS variable은 runtime theme 전환과 컴포넌트 스타일 재사용에 유리하다.

Q. token 파일은 어디에 두면 좋아?
A. 작은 프로젝트는 `src/styles/tokens.css`로 시작하고, 규모가 커지면 type별로 분리한다.

Q. CSS variable fallback은 써도 돼?
A. 가능하지만 token 누락을 숨기는 용도로 남발하면 안 된다.

Q. React에서도 CSS variable을 사용할 수 있어?
A. 가능하다. CSS Modules, plain CSS, CSS-in-JS 등에서 사용할 수 있다.

---

## 9.2 TypeScript Token Constant

### [개념]

TypeScript Token Constant는 JavaScript 로직에서 필요한 token 값을 TypeScript 객체로 관리하는 방식이다.

주로 breakpoint, z-index, component size, chart color, theme name 같은 로직 연동 값에 사용한다.

---

### [핵심]

TS token constant 사용 대상:

- breakpoints
- theme names
- z-index map
- component size map
- chart color key
- animation duration key
- variant names
- size names

주의:

- CSS token과 TS token 불일치 방지
- 중복 정의 최소화
- source of truth 명확화
- type safety 확보

---

### [실무]

Breakpoint constant 예:

```ts
export const breakpoints = {
  tablet: 768,
  desktop: 1024,
  wide: 1280,
} as const;

export type Breakpoint = keyof typeof breakpoints;
```

Variant constant 예:

```ts
export const buttonVariants = [
  "primary",
  "secondary",
  "danger",
  "ghost",
] as const;

export type ButtonVariant = (typeof buttonVariants)[number];
```

Size constant 예:

```ts
export const componentSizes = ["sm", "md", "lg"] as const;

export type ComponentSize = (typeof componentSizes)[number];
```

Review 기준:

```md
- [ ] variant string이 여러 파일에 흩어져 있지 않은가?
- [ ] breakpoint 값이 CSS와 JS에서 불일치하지 않는가?
- [ ] type union으로 허용 값이 제한되는가?
- [ ] token source of truth가 명확한가?
```

---

### [FAQ]

Q. TypeScript에도 token이 필요해?
A. CSS가 아닌 로직에서 breakpoint, variant, size 같은 값을 사용할 때 필요하다.

Q. CSS token과 TS token이 중복되면 문제야?
A. 불일치 위험이 있다. source of truth와 동기화 기준을 정해야 한다.

Q. variant는 TypeScript type으로 제한하는 게 좋아?
A. 좋다. `primary`, `secondary`, `danger` 같은 허용 값을 제한하면 안정성이 높아진다.

Q. breakpoint는 CSS와 JS 중 어디서 관리해?
A. 프로젝트 구조에 따라 다르지만 값이 불일치하지 않도록 하나의 기준을 명확히 해야 한다.

---

## 9.3 Token Review Checklist

### [개념]

Token Review Checklist는 Review Agent가 Design Token 품질을 검토하기 위한 기준이다.

Token Review는 색상, 간격, 폰트, radius, shadow, z-index, motion, theme 확장성을 모두 확인한다.

---

### [핵심]

Token Review Checklist:

```md
## Token Core

- [ ] Design Token 파일이 존재하는가?
- [ ] token naming 규칙이 일관적인가?
- [ ] primitive token과 semantic token 역할이 구분되는가?
- [ ] 반복 raw value가 token으로 관리되는가?

## Color

- [ ] primary / error / warning / success / info token이 있는가?
- [ ] background / surface / text / border token이 있는가?
- [ ] hover / active / focus / disabled token이 있는가?
- [ ] 색상만으로 상태를 전달하지 않는가?

## Spacing

- [ ] spacing scale이 정의되어 있는가?
- [ ] margin / padding / gap에 token을 사용하는가?
- [ ] component 내부 spacing과 layout spacing이 구분되는가?

## Typography

- [ ] font-size token이 정의되어 있는가?
- [ ] font-weight token이 정의되어 있는가?
- [ ] line-height token이 정의되어 있는가?
- [ ] typography hierarchy가 일관적인가?

## Shape / Depth

- [ ] radius token이 정의되어 있는가?
- [ ] shadow token이 정의되어 있는가?
- [ ] z-index token이 정의되어 있는가?
- [ ] 9999 같은 임의 z-index가 없는가?

## Motion / Responsive / Theme

- [ ] motion token이 정의되어 있는가?
- [ ] breakpoint 기준이 문서화되어 있는가?
- [ ] semantic token 기반 theme 확장이 가능한가?
- [ ] dark mode에서 contrast가 유지되는가?
```

---

### [실무]

Review Agent 판단:

```text
Approved
→ token 기준이 명확하고 주요 컴포넌트가 token을 사용함

Needs Fix
→ 일부 raw value 또는 상태 token 누락이 있음

Blocked
→ token 기준이 없고 화면별 스타일이 제각각이며 theme / accessibility 문제가 큼
```

Frontend Agent 생성 전 확인:

```md
- [ ] 사용할 color token이 있는가?
- [ ] 사용할 spacing token이 있는가?
- [ ] 사용할 typography token이 있는가?
- [ ] component token이 필요한가?
- [ ] dark mode를 고려해야 하는가?
```

---

### [FAQ]

Q. Review Agent는 token에서 뭘 봐야 해?
A. Token naming, raw value 사용, semantic token, spacing scale, typography, radius, shadow, z-index, theme 확장성을 확인해야 한다.

Q. token이 없으면 무조건 Blocked야?
A. 공통 UI가 많은데 token 기준이 없으면 Blocked가 될 수 있다. 작은 화면 단위라면 Needs Fix일 수 있다.

Q. raw value가 하나라도 있으면 반려야?
A. 반복 스타일이나 공통 컴포넌트에서 raw value가 많으면 반려 대상이다. 단발성 예외는 이유가 필요하다.

Q. token 검토에서 가장 중요한 것은?
A. semantic token 사용, raw value 최소화, component style 일관성, theme 확장 가능성이다.

---

# 10. Final Checklist

## 10.1 Part02 Quality Checklist

### [개념]

Part02 Quality Checklist는 Design Token Rules 문서가 Agent 기준 문서로 사용 가능한지 확인하는 검수 기준이다.

---

### [핵심]

최종 체크 항목:

```md
## Core

- [ ] Design Token 정의가 명확한가?
- [ ] Token Type이 구분되어 있는가?
- [ ] Token Naming Rules가 있는가?
- [ ] Primitive / Semantic / Component Token이 구분되는가?
- [ ] Token Hierarchy가 명확한가?

## Color

- [ ] Color Token 필수 항목이 있는가?
- [ ] State Color Token 기준이 있는가?
- [ ] Semantic Color Usage 기준이 있는가?
- [ ] Dark Mode 대응 기준이 있는가?

## Spacing

- [ ] Spacing Token scale이 있는가?
- [ ] margin / gap / padding 사용 기준이 있는가?
- [ ] layout spacing 기준이 있는가?

## Typography

- [ ] Typography Token 기준이 있는가?
- [ ] hierarchy 기준이 있는가?
- [ ] line-height 기준이 있는가?

## Shape / Depth

- [ ] Radius Token 기준이 있는가?
- [ ] Shadow Token 기준이 있는가?
- [ ] Z-index Token 기준이 있는가?

## Advanced Token

- [ ] Motion Token 기준이 있는가?
- [ ] Breakpoint Token 기준이 있는가?
- [ ] Opacity Token 기준이 있는가?
- [ ] Theme Token 기준이 있는가?

## Implementation

- [ ] CSS Variable 구현 기준이 있는가?
- [ ] TypeScript Token Constant 기준이 있는가?
- [ ] Review Checklist가 있는가?
```

---

### [실무]

Part02는 Part01 Design System Core의 token 세부 기준 문서다.

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

Part02 기준은 Part03 이후 모든 Component Specification에서 사용된다.

컴포넌트는 raw value보다 token을 우선 사용해야 한다.

---

### [FAQ]

Q. Part02의 역할은 뭐야?
A. Design System Foundation에서 사용할 Color, Spacing, Typography, Radius, Shadow, Z-index, Motion, Theme token 기준을 정의하는 문서다.

Q. Part02는 Part03과 어떻게 연결돼?
A. Part03 Component Specification에서 variant, size, state 스타일을 정의할 때 Part02 token 기준을 사용한다.

Q. Part02 최종 승인 기준은 뭐야?
A. Token Type, Naming, Hierarchy, Color, Spacing, Typography, Radius, Shadow, Z-index, Theme 기준이 명확해야 한다.

Q. Part02에서 가장 중요한 것은 뭐야?
A. semantic token 사용, raw value 최소화, token hierarchy, theme 확장 가능성이다.

---

# Retrieval Queries

### [FAQ]

Q. Design Token이 뭐야?
A. 색상, 간격, 폰트, radius, shadow 같은 디자인 값을 이름으로 관리하는 방식이다.

Q. Design Token은 왜 필요해?
A. 디자인 값을 일관되게 관리하고 변경 시 전체 UI에 안정적으로 반영하기 위해 필요하다.

Q. 모든 값을 token으로 만들어야 해?
A. 아니다. 반복 사용되거나 의미 있는 값부터 token으로 관리한다.

Q. Token Type에는 뭐가 있어?
A. Color, Typography, Spacing, Radius, Shadow, Z-index, Breakpoint, Motion, Size, Opacity Token이 있다.

Q. Token 이름은 어떻게 지어야 해?
A. 역할과 의미가 드러나게 짓는다. 예: `--color-primary`, `--color-error`, `--spacing-4`.

Q. Primitive Token이 뭐야?
A. `--blue-600`처럼 원시 색상이나 값을 나타내는 token이다.

Q. Semantic Token이 뭐야?
A. `--color-primary`, `--color-error`처럼 UI 역할과 의미를 가진 token이다.

Q. Component Token이 뭐야?
A. Button, Input, Card 같은 특정 컴포넌트의 스타일 속성을 관리하는 token이다.

Q. Primitive Token과 Semantic Token 중 뭐를 컴포넌트에서 써야 해?
A. 컴포넌트에서는 semantic token 또는 component token을 우선 사용하는 것이 좋다.

Q. Token Hierarchy는 뭐야?
A. Primitive Token → Semantic Token → Component Token → Component Style로 이어지는 token 구조다.

Q. Color Token은 어떤 것이 필요해?
A. primary, background, surface, text, muted, border, error, warning, success, info, disabled, focus-ring이 필요하다.

Q. Error 색상은 그냥 red로 쓰면 안 돼?
A. 가능하지만 `--color-error` 같은 semantic token으로 관리하는 것이 좋다.

Q. State Color Token이 뭐야?
A. hover, active, focus, disabled, error 같은 상태를 표현하는 색상 token이다.

Q. Semantic Color는 왜 써야 해?
A. 색상 값보다 UI 의미를 기준으로 관리해야 theme 변경과 유지보수가 쉬워지기 때문이다.

Q. Color Token에서 가장 흔한 실수는?
A. 색상 값을 직접 쓰고 의미 token 없이 화면마다 다른 색상을 사용하는 것이다.

Q. Spacing Token은 왜 필요해?
A. 화면마다 margin, padding, gap이 제각각이 되는 것을 막고 UI 리듬을 유지하기 위해 필요하다.

Q. spacing scale은 어떤 기준이 좋아?
A. 4px 또는 8px 기반 scale을 많이 사용한다. 프로젝트에서는 하나의 기준으로 통일해야 한다.

Q. margin과 gap 중 뭐가 좋아?
A. 리스트나 레이아웃 요소 사이 간격은 gap이 더 명확한 경우가 많다.

Q. 컴포넌트에 margin을 직접 주면 안 돼?
A. 재사용 컴포넌트라면 외부 배치는 부모 layout이 담당하는 것이 좋다.

Q. Layout Spacing과 Component Spacing은 뭐가 달라?
A. Layout Spacing은 페이지와 섹션 배치 간격이고, Component Spacing은 컴포넌트 내부 간격이다.

Q. Typography Token은 뭘 관리해?
A. font-size, font-weight, line-height, font-family 같은 글자 스타일을 관리한다.

Q. heading tag와 typography style은 같아야 해?
A. heading tag는 의미 구조이고, 시각 스타일은 typography token으로 관리한다.

Q. Typography Hierarchy가 왜 필요해?
A. 사용자가 제목, 본문, 보조 정보를 빠르게 구분할 수 있어야 하기 때문이다.

Q. Radius Token은 왜 필요해?
A. Button, Card, Modal의 모서리 둥글기를 일관되게 관리하기 위해 필요하다.

Q. Shadow Token은 왜 필요해?
A. Card, Modal, Toast 같은 UI의 깊이 표현을 일관되게 관리하기 위해 필요하다.

Q. Z-index Token은 왜 필요해?
A. Modal, Toast, Dropdown, Header의 겹침 순서를 예측 가능하게 관리하기 위해 필요하다.

Q. z-index는 그냥 9999로 쓰면 안 돼?
A. 권장하지 않는다. token scale로 관리해야 겹침 순서가 무너지지 않는다.

Q. Motion Token은 왜 필요해?
A. transition duration과 easing을 일관되게 관리하기 위해 필요하다.

Q. Breakpoint Token은 왜 필요해?
A. 컴포넌트와 레이아웃이 같은 반응형 기준을 공유해야 하기 때문이다.

Q. Opacity Token은 왜 필요해?
A. disabled, overlay, hover 같은 투명도 상태를 일관되게 관리하기 위해 필요하다.

Q. Theme Token은 왜 필요해?
A. 컴포넌트 구조를 유지하면서 색상과 시각 스타일을 전환하기 위해 필요하다.

Q. Dark Mode Token에서 가장 중요한 것은?
A. background, surface, text, border, focus-ring contrast를 유지하는 것이다.

Q. CSS Variable로 token을 구현해도 돼?
A. 권장된다. CSS variable은 runtime theme 전환과 컴포넌트 스타일 재사용에 유리하다.

Q. TypeScript에도 token이 필요해?
A. CSS가 아닌 로직에서 breakpoint, variant, size 같은 값을 사용할 때 필요하다.

Q. Review Agent는 token에서 뭘 봐야 해?
A. Token naming, raw value 사용, semantic token, spacing scale, typography, radius, shadow, z-index, theme 확장성을 확인해야 한다.

Q. Part02의 역할은 뭐야?
A. Design System Foundation에서 사용할 Color, Spacing, Typography, Radius, Shadow, Z-index, Motion, Theme token 기준을 정의하는 문서다.
