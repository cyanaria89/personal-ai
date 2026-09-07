# HTML CSS Foundation Part12 - CSS Variables Pseudo Transition

---

# 1. Document Role

## 1.1 Document Role Concept

### [개념]

이 문서는 CSS Variables, Pseudo Class, Pseudo Element, Transition, Transform, Reduced Motion의 상세 기준을 다룬다.

Part12는 CSS selector 기초 문서가 아니라, 상태 기반 스타일링과 interaction styling을 실무 기준으로 확장하는 문서다.

---

### [핵심]

문서 역할:

- CSS Variables와 Design Token 연결 기준을 다룬다.
- Component Scoped Variables 기준을 다룬다.
- Pseudo Class의 상세 상태 기준을 다룬다.
- Pseudo Element의 실무 사용 기준을 다룬다.
- Transition과 Transform의 기본 interaction 기준을 다룬다.
- Reduced Motion과 사용자 환경 대응 기준을 다룬다.
- Component State Styling과 연결된다.
- Accessibility와 Focus Style 기준을 포함한다.

연계 기준:

- Selector와 Pseudo Selector의 기초 문법은 Part05를 참조한다.
- Responsive Media Query의 기본 구조는 Part10을 참조한다.
- Typography, Color, Spacing Token 기준은 Part11을 참조한다.
- Component State Styling 적용 예시는 Part14를 참조한다.
- Attribute, ARIA, Accessibility 상태 기준은 Part15를 참조한다.
- Troubleshooting과 Review Checklist는 Part16을 참조한다.

---

### [실무]

문서 사용 기준:

```text
CSS Variable 문법/Token 연결 필요 → Part12
Pseudo Class 상세 상태 기준 필요 → Part12
Pseudo Element 장식/marker/placeholder 기준 필요 → Part12
Transition / Transform interaction 필요 → Part12
Reduced Motion 대응 필요 → Part12
Selector 기초 문법 필요 → Part05
Responsive breakpoint 필요 → Part10
Component 적용 예시 필요 → Part14
```

---

### [FAQ]

Q. Part12는 어떤 문서야?
A. CSS Variables, Pseudo Class, Pseudo Element, Transition, Reduced Motion의 상세 기준 문서다.

Q. Pseudo Selector 기초는 어디서 봐?
A. 기초 문법은 Part05를 참조하고 상세 상태 기준은 Part12에서 다룬다.

Q. Responsive Media Query 기초는 어디서 봐?
A. viewport, breakpoint, media query 기본 구조는 Part10을 참조한다.

Q. Component State Styling 예시는 어디서 봐?
A. 상세 selector 기준은 Part12, component 적용 예시는 Part14를 참조한다.

---

# 2. CSS Variables

## 2.1 CSS Variables Concept

### [개념]

CSS Variables는 CSS 안에서 재사용 가능한 값을 정의하고 참조하는 기능이다.

CSS Variables는 Custom Properties라고도 하며, `--name` 형태로 정의하고 `var(--name)`으로 사용한다.

기본 예:

```css
:root {
  --color-primary: #2563eb;
  --space-4: 1rem;
}

.button {
  padding: var(--space-4);
  background-color: var(--color-primary);
}
```

---

### [핵심]

CSS Variables 핵심:

- `--`로 시작하는 이름을 사용한다.
- `var()` 함수로 값을 참조한다.
- cascade와 inheritance 영향을 받는다.
- `:root`에 정의하면 전역 token처럼 사용할 수 있다.
- component 내부에서 scoped variable로 override할 수 있다.
- theme, variant, state styling에 유용하다.
- fallback value를 지정할 수 있다.
- runtime theme 변경에 적합하다.
- CSS Variables는 Sass 변수와 다르게 브라우저 runtime에서 동작한다.

---

### [실무]

Fallback 예:

```css
.button {
  color: var(--button-color, #ffffff);
}
```

Theme 예:

```css
:root {
  --color-background: #ffffff;
  --color-text: #111827;
}

[data-theme="dark"] {
  --color-background: #111827;
  --color-text: #f9fafb;
}

body {
  color: var(--color-text);
  background-color: var(--color-background);
}
```

검수 기준:

- 변수 이름이 의미 기반인가?
- 전역 token과 component scoped variable이 구분되는가?
- fallback이 필요한 변수에 fallback이 있는가?
- 같은 값이 하드코딩으로 반복되지 않는가?
- theme 변경 시 cascade 범위가 의도와 맞는가?

---

### [FAQ]

Q. CSS Variables가 뭐야?
A. CSS에서 재사용 가능한 값을 `--name`으로 정의하고 `var(--name)`으로 사용하는 기능이다.

Q. CSS Variables는 어디에 정의해?
A. 전역 token은 `:root`, component별 값은 component root class에 정의할 수 있다.

Q. CSS Variables는 runtime에서 바뀔 수 있어?
A. 가능하다. theme 변경이나 state 변경에 따라 cascade로 값이 바뀔 수 있다.

Q. CSS Variables fallback은 어떻게 써?
A. `var(--name, fallback-value)` 형태로 작성한다.

---

# 3. CSS Variable Syntax

## 3.1 Variable Definition and Usage

### [개념]

CSS Variable Syntax는 Custom Property를 정의하고 참조하는 문법이다.

정의는 `--variable-name: value;` 형태이며, 사용은 `var(--variable-name)` 형태다.

---

### [핵심]

Syntax 핵심:

- 변수 이름은 `--`로 시작한다.
- 변수 값은 CSS value로 사용할 수 있는 값을 가진다.
- `var()` 안에 변수 이름을 넣어 참조한다.
- fallback 값은 comma 뒤에 작성한다.
- 변수 이름은 대소문자를 구분한다.
- 변수는 정의된 scope 안에서 사용할 수 있다.
- 유효하지 않은 변수 값은 해당 declaration을 무효화할 수 있다.

---

### [실무]

좋은 예:

```css
:root {
  --radius-md: 0.5rem;
  --duration-fast: 180ms;
  --ease-standard: ease;
}

.card {
  border-radius: var(--radius-md);
  transition: box-shadow var(--duration-fast) var(--ease-standard);
}
```

잘못된 예:

```css
:root {
  color-primary: blue;
}

.button {
  background-color: var(color-primary);
}
```

수정:

```css
:root {
  --color-primary: blue;
}

.button {
  background-color: var(--color-primary);
}
```

검수 기준:

- 변수 이름이 `--`로 시작하는가?
- `var()` 안에도 `--`가 포함되어 있는가?
- 변수 이름 오타가 없는가?
- fallback 값이 필요한가?
- 변수 값이 해당 property에 유효한가?

---

### [FAQ]

Q. CSS Variable은 어떻게 정의해?
A. `--color-primary: blue;`처럼 `--`로 시작하는 이름에 값을 지정한다.

Q. CSS Variable은 어떻게 사용해?
A. `var(--color-primary)`처럼 `var()` 함수로 사용한다.

Q. 변수 이름은 대소문자를 구분해?
A. 구분한다. 이름 오타와 대소문자 차이에 주의해야 한다.

Q. 변수 값이 잘못되면 어떻게 돼?
A. 해당 declaration이 무효가 될 수 있다.

---

# 4. Global Tokens

## 4.1 Global Design Tokens

### [개념]

Global Token은 프로젝트 전체에서 재사용되는 색상, 간격, 글자 크기, radius, shadow, transition 같은 디자인 값이다.

CSS Variables를 `:root`에 정의하면 Global Token처럼 사용할 수 있다.

---

### [핵심]

Global Token 핵심:

- 전역 디자인 기준을 만든다.
- 반복되는 하드코딩 값을 줄인다.
- UI 일관성을 높인다.
- theme 변경을 쉽게 만든다.
- component 간 style 기준을 공유한다.
- spacing, color, typography, radius, z-index, duration을 token화할 수 있다.
- token 이름은 값보다 의미를 표현해야 한다.

---

### [실무]

Token 예:

```css
:root {
  --color-primary: #2563eb;
  --color-danger: #dc2626;
  --color-background: #ffffff;
  --color-surface: #f9fafb;
  --color-text: #111827;
  --color-text-muted: #6b7280;
  --color-border: #e5e7eb;

  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;

  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-xl: 1.25rem;

  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;

  --duration-fast: 180ms;
  --duration-normal: 240ms;
  --ease-standard: ease;
}
```

검수 기준:

- 색상과 간격 값이 token으로 관리되는가?
- token 이름이 의미 기반인가?
- 같은 hex 값과 spacing 값이 반복되지 않는가?
- component에서 token을 직접 참조하는가?
- theme 변경이 필요한 값이 token화되어 있는가?

---

### [FAQ]

Q. Global Token이 뭐야?
A. 프로젝트 전체에서 재사용하는 색상, 간격, 글자 크기 같은 디자인 기준 값이다.

Q. CSS Variables와 Design Token은 같은 거야?
A. CSS Variables는 구현 방법이고 Design Token은 디자인 값의 개념이다.

Q. token 이름은 어떻게 지어?
A. `--color-primary`, `--space-4`처럼 역할과 의미 중심으로 짓는다.

Q. token이 왜 필요해?
A. 반복 값을 줄이고 UI 일관성과 유지보수성을 높이기 위해 필요하다.

---

# 5. Component Scoped Variables

## 5.1 Scoped Variable Concept

### [개념]

Component Scoped Variable은 특정 component 내부에서만 사용하는 CSS Variables다.

Component의 variant, state, theme를 관리할 때 유용하다.

---

### [핵심]

Scoped Variable 핵심:

- component root class에서 정의한다.
- component 내부 property가 scoped variable을 참조한다.
- variant class가 scoped variable 값을 override할 수 있다.
- state selector가 scoped variable을 바꿀 수 있다.
- component 재사용성이 좋아진다.
- 중복 selector를 줄일 수 있다.
- variant별 property 반복을 줄인다.

---

### [실무]

Button 예:

```css
.button {
  --button-bg: var(--color-primary);
  --button-color: #ffffff;
  --button-border: transparent;

  color: var(--button-color);
  background-color: var(--button-bg);
  border: 1px solid var(--button-border);
}

.button-secondary {
  --button-bg: var(--color-surface);
  --button-color: var(--color-text);
  --button-border: var(--color-border);
}

.button-danger {
  --button-bg: var(--color-danger);
  --button-color: #ffffff;
  --button-border: transparent;
}
```

Card 예:

```css
.card {
  --card-padding: var(--space-6);
  --card-bg: var(--color-surface);
  --card-border: var(--color-border);

  padding: var(--card-padding);
  background-color: var(--card-bg);
  border: 1px solid var(--card-border);
}

.card-compact {
  --card-padding: var(--space-4);
}
```

검수 기준:

- component root에 scoped variable이 정의되어 있는가?
- variant가 variable 값만 override하는가?
- 같은 property가 variant마다 반복되지 않는가?
- scoped variable 이름에 component prefix가 있는가?
- global token과 scoped variable 역할이 구분되는가?

---

### [FAQ]

Q. Component Scoped Variable이 뭐야?
A. 특정 component 내부에서만 사용하는 CSS Variable이다.

Q. Scoped Variable은 왜 써?
A. variant와 state별 style을 중복 없이 관리하기 위해 사용한다.

Q. component prefix를 붙이는 이유는?
A. 변수 충돌을 줄이고 어떤 component의 변수인지 명확히 하기 위해서다.

Q. Button variant에 scoped variable을 쓰면 뭐가 좋아?
A. base style은 유지하고 variant별 값만 바꾸면 되어 CSS가 단순해진다.

---

# 6. Theme and Dark Mode

## 6.1 Theme Variables

### [개념]

Theme Variables는 light mode, dark mode, brand theme처럼 UI 전체의 색상과 시각 기준을 전환하기 위한 CSS Variables다.

`data-theme` attribute나 class를 사용해 theme scope를 바꿀 수 있다.

---

### [핵심]

Theme 핵심:

- 색상 token을 theme별로 override한다.
- `data-theme="dark"` 같은 attribute selector를 사용할 수 있다.
- body 또는 html에 theme attribute를 두는 경우가 많다.
- component는 직접 색상을 하드코딩하지 않고 token을 참조한다.
- dark mode에서는 contrast를 다시 검수해야 한다.
- shadow, border, surface color도 theme별 조정이 필요하다.
- 사용자 OS 설정은 `prefers-color-scheme`으로 감지할 수 있다.

---

### [실무]

Theme 예:

```css
:root {
  --color-background: #ffffff;
  --color-surface: #f9fafb;
  --color-text: #111827;
  --color-border: #e5e7eb;
}

[data-theme="dark"] {
  --color-background: #111827;
  --color-surface: #1f2937;
  --color-text: #f9fafb;
  --color-border: #374151;
}

body {
  color: var(--color-text);
  background-color: var(--color-background);
}

.card {
  background-color: var(--color-surface);
  border-color: var(--color-border);
}
```

System Preference 예:

```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-background: #111827;
    --color-text: #f9fafb;
  }
}
```

검수 기준:

- component가 token을 참조하는가?
- dark mode에서 contrast가 충분한가?
- border와 surface 구분이 가능한가?
- focus-visible이 dark mode에서도 보이는가?
- theme attribute가 적용되는 scope가 명확한가?

---

### [FAQ]

Q. Theme Variables는 뭐야?
A. light, dark, brand theme처럼 UI 전체 색상 기준을 바꾸기 위한 CSS Variables다.

Q. dark mode는 어떻게 구현해?
A. `data-theme="dark"` 또는 `prefers-color-scheme` 기준으로 color token을 override할 수 있다.

Q. dark mode에서 무엇을 검수해야 해?
A. text contrast, border/surface 구분, focus-visible, disabled 상태를 다시 확인해야 한다.

Q. component마다 색상을 직접 바꾸면 안 돼?
A. 가능은 하지만 token 기반으로 바꾸는 것이 유지보수에 더 좋다.

---

# 7. Pseudo Classes

## 7.1 Interaction Pseudo Classes

### [개념]

Interaction Pseudo Class는 사용자의 조작 상태에 따라 요소를 선택하는 pseudo class다.

대표 예:

- `:hover`
- `:focus`
- `:focus-visible`
- `:active`
- `:disabled`
- `:checked`

---

### [핵심]

Interaction Pseudo Class 핵심:

- hover는 pointer가 요소 위에 있는 상태다.
- focus는 요소가 focus를 받은 상태다.
- focus-visible은 focus 표시가 필요한 상태다.
- active는 요소가 활성화되는 순간의 상태다.
- disabled는 조작 불가 상태다.
- checked는 checkbox/radio의 선택 상태다.
- hover만으로 interaction을 설계하면 keyboard/touch 접근성 문제가 생길 수 있다.
- 상태별 style은 실제 HTML/ARIA 상태와 일치해야 한다.

---

### [실무]

Button State 예:

```css
.button:hover {
  background-color: var(--color-primary-hover);
}

.button:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.button:not(:disabled):active {
  transform: translateY(1px);
}

.button:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}
```

Touch 환경 고려:

```css
@media (hover: hover) and (pointer: fine) {
  .card:hover {
    transform: translateY(-2px);
  }
}
```

검수 기준:

- hover와 focus-visible이 함께 고려되었는가?
- disabled 상태에 hover/active가 적용되지 않는가?
- active transform이 과도하지 않은가?
- touch 환경에서 hover 의존 기능이 없는가?
- state style이 색상만으로 의미를 전달하지 않는가?

---

### [FAQ]

Q. Interaction Pseudo Class가 뭐야?
A. hover, focus, active, disabled처럼 사용자 조작 상태를 선택하는 pseudo class다.

Q. hover만 있으면 충분해?
A. 아니다. keyboard 사용자를 위해 focus-visible도 필요하다.

Q. disabled 상태에는 hover를 적용해도 돼?
A. 일반적으로 disabled 상태는 조작 불가이므로 hover/active 효과를 제외하는 것이 좋다.

Q. active 상태는 언제 쓰여?
A. button을 누르는 순간 같은 짧은 조작 feedback에 사용할 수 있다.

---

## 7.2 Structural Pseudo Classes

### [개념]

Structural Pseudo Class는 DOM 구조나 요소 위치를 기준으로 선택하는 pseudo class다.

대표 예:

- `:first-child`
- `:last-child`
- `:nth-child()`
- `:not()`
- `:is()`
- `:where()`
- `:has()`

---

### [핵심]

Structural Pseudo Class 핵심:

- child 위치나 조건을 기준으로 선택한다.
- list item, table row, repeated component에 유용하다.
- DOM 구조 변경에 취약할 수 있다.
- `:not()`은 특정 조건을 제외한다.
- `:is()`는 selector group을 간결하게 만든다.
- `:where()`는 specificity를 0으로 낮출 수 있다.
- `:has()`는 특정 하위 요소가 있는 부모를 선택할 수 있다.
- browser support와 사용 목적을 확인해야 한다.

---

### [실무]

List 예:

```css
.list-item:not(:last-child) {
  border-bottom: 1px solid var(--color-border);
}
```

`:is()` 예:

```css
:is(h1, h2, h3) {
  line-height: 1.2;
}
```

`:where()` 예:

```css
:where(.prose) :where(h1, h2, h3, p, ul, ol) {
  margin-block-start: 0;
}
```

`:has()` 예:

```css
.card:has(.card-link:focus-visible) {
  outline: 2px solid var(--color-primary);
}
```

검수 기준:

- DOM 구조 변경에 취약하지 않은가?
- `:nth-child()`가 실제 콘텐츠 순서와 맞는가?
- `:not()` 조건이 너무 복잡하지 않은가?
- `:where()`를 specificity 낮추기 목적으로 사용했는가?
- `:has()` 사용 시 browser support와 대체 방안을 검토했는가?

---

### [FAQ]

Q. Structural Pseudo Class가 뭐야?
A. DOM 구조나 요소 위치를 기준으로 선택하는 pseudo class다.

Q. nth-child는 언제 써?
A. 반복 item 중 특정 순서나 패턴을 선택할 때 사용한다.

Q. :where()는 왜 써?
A. selector를 묶으면서 specificity를 낮게 유지하기 위해 사용할 수 있다.

Q. :has()는 뭐야?
A. 특정 하위 요소나 조건을 가진 부모 요소를 선택할 수 있는 pseudo class다.

---

## 7.3 Form State Pseudo Classes

### [개념]

Form State Pseudo Class는 Form Control의 입력 상태를 기준으로 선택하는 pseudo class다.

대표 예:

- `:required`
- `:optional`
- `:valid`
- `:invalid`
- `:checked`
- `:disabled`
- `:read-only`
- `:placeholder-shown`

---

### [핵심]

Form State 핵심:

- required field를 선택할 수 있다.
- invalid field를 선택할 수 있다.
- checked checkbox/radio를 선택할 수 있다.
- disabled와 readonly 상태를 구분해야 한다.
- placeholder-shown은 placeholder가 표시 중인 상태다.
- CSS validation style만으로 error UX를 완성할 수 없다.
- error message와 aria-invalid, aria-describedby가 함께 필요하다.
- 색상만으로 오류를 표시하면 접근성 문제가 생길 수 있다.

---

### [실무]

Form State 예:

```css
.form-input:required {
  border-inline-start: 3px solid var(--color-primary);
}

.form-input:invalid {
  border-color: var(--color-danger);
}

.form-input[aria-invalid="true"] {
  border-color: var(--color-danger);
}

.checkbox-input:checked + .checkbox-label {
  font-weight: var(--font-semibold);
}
```

주의:

```css
.form-input:invalid {
  color: red;
}
```

오류 이유와 해결 방법을 제공하지 않으면 사용자가 문제를 이해하기 어렵다.

검수 기준:

- CSS 상태와 실제 validation 상태가 일치하는가?
- aria-invalid와 error message가 함께 있는가?
- required 표시가 색상만으로 제공되지 않는가?
- disabled와 readonly style이 구분되는가?
- placeholder-shown으로 label을 대체하지 않았는가?

---

### [FAQ]

Q. Form State Pseudo Class가 뭐야?
A. required, invalid, checked, disabled처럼 form control 상태를 선택하는 pseudo class다.

Q. :invalid만 쓰면 error 처리가 충분해?
A. 아니다. error message와 aria-invalid, aria-describedby 연결이 필요하다.

Q. :checked는 어디에 써?
A. checkbox나 radio가 선택된 상태를 styling할 때 사용한다.

Q. placeholder-shown은 label 대체로 써도 돼?
A. 권장하지 않는다. placeholder는 label을 대체할 수 없다.

---

# 8. Pseudo Elements

## 8.1 ::before and ::after

### [개념]

`::before`와 `::after`는 요소의 콘텐츠 앞이나 뒤에 가상 요소를 생성하는 pseudo element다.

주로 장식, 아이콘, 구분선, badge marker, required mark에 사용한다.

---

### [핵심]

`::before` / `::after` 핵심:

- `content` property가 필요하다.
- 실제 DOM에는 존재하지 않는 가상 요소다.
- 장식 목적에 적합하다.
- 중요한 텍스트 정보를 CSS content에만 넣으면 안 된다.
- position과 함께 overlay 장식에 사용할 수 있다.
- `box-sizing` reset이 pseudo element에도 적용되어야 한다.
- screen reader 전달 여부는 구현과 환경에 따라 다를 수 있으므로 중요한 정보에 의존하지 않는다.

---

### [실무]

장식선 예:

```css
.section-title::after {
  content: "";
  display: block;
  width: 3rem;
  height: 3px;
  margin-block-start: var(--space-2);
  background-color: var(--color-primary);
}
```

Required Mark 예:

```css
.form-label-required::after {
  content: " *";
  color: var(--color-danger);
}
```

중요 정보는 HTML에도 제공:

```html
<label class="form-label form-label-required" for="email">
  Email <span class="visually-hidden">required</span>
</label>
```

검수 기준:

- content가 정의되어 있는가?
- 장식 목적에 사용되는가?
- 중요한 정보가 CSS content에만 있지 않은가?
- position 사용 시 stacking과 overflow 문제가 없는가?
- pseudo element에도 box-sizing이 적용되는가?

---

### [FAQ]

Q. ::before와 ::after는 뭐야?
A. 요소 앞이나 뒤에 가상 요소를 생성하는 pseudo element다.

Q. before/after에 content가 꼭 필요해?
A. 대부분 필요하다. content가 없으면 표시되지 않는 경우가 많다.

Q. 중요한 텍스트를 content에 넣어도 돼?
A. 권장하지 않는다. 중요한 정보는 HTML 텍스트나 접근성 정보로 제공해야 한다.

Q. before/after는 실제 DOM에 있어?
A. 아니다. CSS가 생성하는 가상 요소다.

---

## 8.2 ::placeholder

### [개념]

`::placeholder`는 input 또는 textarea의 placeholder text를 선택하는 pseudo element다.

Placeholder는 입력 힌트이며 label을 대체할 수 없다.

---

### [핵심]

Placeholder 핵심:

- placeholder text style을 지정한다.
- placeholder는 field name이 아니다.
- placeholder 색상은 너무 낮은 contrast면 읽기 어렵다.
- placeholder에 중요한 정보를 모두 넣으면 안 된다.
- 입력 중 placeholder가 사라지므로 label 대체가 불가능하다.
- form accessibility는 label과 helper text로 보완해야 한다.

---

### [실무]

예:

```css
.form-input::placeholder {
  color: var(--color-text-muted);
}
```

나쁜 예:

```html
<input type="email" placeholder="Email" />
```

좋은 예:

```html
<label for="email">Email</label>
<input id="email" name="email" type="email" placeholder="you@example.com" />
```

검수 기준:

- placeholder가 label을 대체하지 않는가?
- placeholder contrast가 너무 낮지 않은가?
- placeholder에 필수 정보를 몰아넣지 않았는가?
- label과 helper text가 별도로 있는가?

---

### [FAQ]

Q. ::placeholder는 뭐야?
A. input이나 textarea의 placeholder text를 styling하는 pseudo element다.

Q. placeholder는 label 대신 쓸 수 있어?
A. 안 된다. placeholder는 입력 힌트이고 label은 필드 이름이다.

Q. placeholder 색상은 흐리게 해도 돼?
A. 가능하지만 읽기 어려울 정도로 contrast가 낮으면 안 된다.

---

## 8.3 ::marker and ::selection

### [개념]

`::marker`는 list item marker를 선택하고, `::selection`은 사용자가 선택한 텍스트 영역을 선택하는 pseudo element다.

---

### [핵심]

`::marker` 핵심:

- list item의 bullet 또는 number marker를 styling한다.
- list semantics를 유지하면서 marker만 조정할 수 있다.
- 모든 list marker를 제거하기보다 필요한 곳만 조정한다.

`::selection` 핵심:

- 사용자가 드래그로 선택한 text style을 지정한다.
- text와 background contrast를 유지해야 한다.
- 과도한 selection style은 가독성을 해칠 수 있다.

---

### [실무]

Marker 예:

```css
.prose li::marker {
  color: var(--color-primary);
}
```

Selection 예:

```css
::selection {
  color: var(--color-background);
  background-color: var(--color-text);
}
```

검수 기준:

- list semantics를 유지하는가?
- marker style이 콘텐츠 이해를 방해하지 않는가?
- selection color contrast가 충분한가?
- selection style이 theme에서 적절한가?

---

### [FAQ]

Q. ::marker는 뭐야?
A. list item의 bullet이나 number marker를 styling하는 pseudo element다.

Q. ::selection은 뭐야?
A. 사용자가 선택한 텍스트 영역의 style을 지정하는 pseudo element다.

Q. marker를 없애면 list semantics도 사라져?
A. marker 제거는 시각 표현 변경이고 HTML list semantics와는 별개다. 다만 사용성은 검토해야 한다.

---

# 9. Transition

## 9.1 Transition Concept

### [개념]

Transition은 CSS property 값이 변경될 때 즉시 바뀌지 않고 일정 시간 동안 부드럽게 변화하도록 만드는 기능이다.

Hover, focus, active, open/close state 같은 interaction feedback에 사용된다.

---

### [핵심]

Transition 핵심:

- `transition-property`는 변화시킬 property다.
- `transition-duration`은 변화 시간이다.
- `transition-timing-function`은 변화 속도 곡선이다.
- `transition-delay`는 시작 지연 시간이다.
- 축약형 `transition`을 자주 사용한다.
- 모든 property가 transition에 적합하지 않다.
- layout을 크게 유발하는 property보다 transform/opacity가 성능에 유리한 경우가 많다.
- transition은 상태 변화 이해를 돕는 보조 수단이다.
- reduced motion을 고려해야 한다.

---

### [실무]

기본 예:

```css
.button {
  transition:
    background-color var(--duration-fast) var(--ease-standard),
    color var(--duration-fast) var(--ease-standard),
    border-color var(--duration-fast) var(--ease-standard);
}

.button:hover {
  background-color: var(--color-primary-hover);
}
```

주의:

```css
.card {
  transition: all 300ms ease;
}
```

`transition: all`은 예상치 못한 property까지 transition되어 디버깅과 성능 문제가 생길 수 있다.

검수 기준:

- transition property가 명확한가?
- duration이 과도하게 길지 않은가?
- transition all을 남용하지 않았는가?
- layout을 크게 유발하는 property를 transition하지 않는가?
- reduced motion 대응이 있는가?

---

### [FAQ]

Q. Transition이 뭐야?
A. CSS property 값이 변경될 때 일정 시간 동안 부드럽게 변화하게 만드는 기능이다.

Q. transition: all은 왜 조심해야 해?
A. 예상하지 않은 property까지 transition되어 성능과 디버깅 문제가 생길 수 있기 때문이다.

Q. transition은 어디에 많이 써?
A. button hover, focus, card hover, modal fade, accordion state 등에 사용한다.

Q. transition에도 접근성 고려가 필요해?
A. 필요하다. 움직임에 민감한 사용자를 위해 reduced motion을 고려해야 한다.

---

# 10. Transform and Opacity

## 10.1 Transform

### [개념]

Transform은 요소의 위치, 크기, 회전, 기울기를 시각적으로 변형하는 CSS property다.

대표 함수:

- `translate()`
- `scale()`
- `rotate()`

---

### [핵심]

Transform 핵심:

- layout flow 자체를 바꾸지 않고 시각적으로 이동할 수 있다.
- hover feedback에 자주 사용된다.
- position offset과 다르게 주변 layout에 영향을 덜 준다.
- stacking context를 생성할 수 있다.
- 너무 큰 transform motion은 사용성 문제를 만들 수 있다.
- transform된 요소와 focus outline 위치를 확인해야 한다.

---

### [실무]

Card Hover 예:

```css
.card {
  transition: transform var(--duration-fast) var(--ease-standard);
}

@media (hover: hover) and (pointer: fine) {
  .card:hover {
    transform: translateY(-2px);
  }
}
```

Scale 예:

```css
.icon-button:active {
  transform: scale(0.96);
}
```

검수 기준:

- transform이 layout 변경 대신 시각 feedback에 사용되는가?
- motion 크기가 과도하지 않은가?
- transform으로 stacking context 문제가 생기지 않는가?
- focus-visible과 함께 보이는가?
- reduced motion에서 제거 또는 완화되는가?

---

### [FAQ]

Q. Transform은 뭐야?
A. 요소를 시각적으로 이동, 확대/축소, 회전시키는 CSS property다.

Q. transform은 layout에 영향을 줘?
A. 일반적으로 normal flow의 주변 layout에는 직접 영향을 주지 않는다.

Q. transform이 z-index 문제를 만들 수 있어?
A. transform은 stacking context를 만들 수 있어 layer 문제에 영향을 줄 수 있다.

---

## 10.2 Opacity

### [개념]

Opacity는 요소의 투명도를 조정하는 CSS property다.

0은 완전 투명, 1은 완전 불투명이다.

---

### [핵심]

Opacity 핵심:

- `opacity: 0`은 보이지 않지만 layout 공간은 유지한다.
- `opacity: 0` 요소는 상황에 따라 focus 가능하거나 클릭 가능할 수 있다.
- disabled 상태 표현에 opacity를 사용할 수 있다.
- 너무 낮은 opacity는 contrast 문제를 만들 수 있다.
- opacity는 stacking context를 생성할 수 있다.
- fade transition에 자주 사용된다.

---

### [실무]

Fade 예:

```css
.toast {
  opacity: 0;
  transition: opacity var(--duration-fast) var(--ease-standard);
}

.toast[data-state="open"] {
  opacity: 1;
}
```

주의:

```css
.hidden-button {
  opacity: 0;
}
```

보이지 않지만 focus되거나 클릭될 수 있으므로 hidden 상태와 접근성 상태를 함께 관리해야 한다.

검수 기준:

- opacity 0 요소가 focus되거나 클릭되지 않는가?
- disabled opacity가 contrast를 너무 낮추지 않는가?
- fade animation이 reduced motion에서 적절히 처리되는가?
- opacity로 숨김 처리할 때 visibility, pointer-events, hidden과의 관계를 검토했는가?

---

### [FAQ]

Q. Opacity는 뭐야?
A. 요소의 투명도를 조정하는 CSS property다.

Q. opacity 0이면 display none과 같아?
A. 아니다. 보이지 않지만 layout 공간은 유지되고 focus나 클릭 가능성이 남을 수 있다.

Q. disabled에 opacity를 써도 돼?
A. 가능하지만 contrast와 조작 불가 표현이 명확한지 확인해야 한다.

---

# 11. Reduced Motion

## 11.1 Reduced Motion Concept

### [개념]

Reduced Motion은 움직임에 민감한 사용자를 위해 animation, transition, scroll motion, parallax 같은 움직임을 줄이는 접근성 대응이다.

CSS에서는 `prefers-reduced-motion` media feature를 사용한다.

---

### [핵심]

Reduced Motion 핵심:

- 사용자 시스템 설정을 존중한다.
- 큰 이동, 회전, 확대/축소, parallax를 줄인다.
- 자동 반복 animation을 줄인다.
- smooth scroll을 비활성화할 수 있다.
- 상태 변화 자체를 제거하면 안 된다.
- motion 대신 색상, border, text 등 다른 feedback을 제공한다.
- transition duration을 줄이거나 none으로 처리할 수 있다.

---

### [실무]

Global Reduced Motion 예:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms;
    animation-iteration-count: 1;
    scroll-behavior: auto;
    transition-duration: 0.01ms;
  }
}
```

Component 예:

```css
.card {
  transition:
    transform var(--duration-fast) var(--ease-standard),
    box-shadow var(--duration-fast) var(--ease-standard);
}

@media (prefers-reduced-motion: reduce) {
  .card {
    transition: box-shadow var(--duration-fast) var(--ease-standard);
  }

  .card:hover {
    transform: none;
  }
}
```

검수 기준:

- 큰 이동 motion이 있는가?
- 반복 animation이 있는가?
- smooth scroll이 강제되는가?
- reduced motion에서도 상태 변화가 이해되는가?
- motion 대신 다른 feedback이 있는가?

---

### [FAQ]

Q. Reduced Motion이 뭐야?
A. 움직임에 민감한 사용자를 위해 animation과 transition 같은 motion을 줄이는 접근성 대응이다.

Q. prefers-reduced-motion은 뭐야?
A. 사용자가 시스템에서 움직임 감소를 선호하는지 감지하는 media feature다.

Q. reduced motion이면 모든 transition을 없애야 해?
A. 반드시 전부 없앨 필요는 없지만 큰 움직임과 반복 animation은 줄이는 것이 좋다.

Q. motion을 줄이면 feedback은 어떻게 줘?
A. 색상, border, shadow, text 같은 비동작 feedback을 함께 제공한다.

---

# 12. Common Interaction Patterns

## 12.1 Button Interaction

### [개념]

Button Interaction은 button의 hover, focus-visible, active, disabled 상태를 시각적으로 표현하는 styling pattern이다.

---

### [핵심]

Button Interaction 핵심:

- hover는 보조 feedback이다.
- focus-visible은 keyboard 접근성에 필수다.
- active는 눌림 feedback이다.
- disabled는 조작 불가 상태다.
- disabled에는 pointer cursor와 active motion을 적용하지 않는다.
- loading 상태는 중복 제출 방지와 함께 처리한다.
- 색상 변화만으로 상태를 전달하지 않는다.

---

### [실무]

Button Pattern:

```css
.button {
  transition:
    background-color var(--duration-fast) var(--ease-standard),
    transform var(--duration-fast) var(--ease-standard);
}

@media (hover: hover) and (pointer: fine) {
  .button:not(:disabled):hover {
    background-color: var(--button-hover-bg);
  }
}

.button:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.button:not(:disabled):active {
  transform: translateY(1px);
}

.button:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}
```

검수 기준:

- disabled 상태가 hover/active에서 제외되는가?
- focus-visible이 명확한가?
- active transform이 과하지 않은가?
- touch 환경에서 hover 의존이 없는가?
- loading 상태가 aria-busy 또는 disabled와 연결되는가?

---

### [FAQ]

Q. Button Interaction에서 가장 중요한 상태는?
A. hover, focus-visible, active, disabled 상태를 함께 설계하는 것이다.

Q. disabled button에도 hover를 줘도 돼?
A. 권장하지 않는다. disabled는 조작 불가 상태가 명확해야 한다.

Q. Button focus-visible은 왜 필요해?
A. keyboard 사용자가 현재 위치를 알 수 있어야 하기 때문이다.

---

## 12.2 Card Hover and Focus

### [개념]

Card Hover and Focus는 Card Component가 hover 또는 내부 link focus 상태에서 클릭 가능성과 계층감을 표현하는 pattern이다.

---

### [핵심]

Card Interaction 핵심:

- hover는 mouse 환경에서만 보조 feedback으로 사용한다.
- clickable card는 link semantic이 명확해야 한다.
- keyboard focus는 card 내부 link 또는 card wrapper에 명확히 보여야 한다.
- transform motion은 과도하지 않게 사용한다.
- reduced motion에서 transform을 제거할 수 있다.
- nested interactive element를 주의한다.

---

### [실무]

Card Interaction 예:

```css
.card {
  transition:
    border-color var(--duration-fast) var(--ease-standard),
    transform var(--duration-fast) var(--ease-standard);
}

@media (hover: hover) and (pointer: fine) {
  .card:has(.card-link:hover) {
    border-color: var(--color-primary);
    transform: translateY(-2px);
  }
}

.card-link:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .card {
    transition: border-color var(--duration-fast) var(--ease-standard);
  }

  .card:has(.card-link:hover) {
    transform: none;
  }
}
```

검수 기준:

- Card 전체가 link처럼 보이면 실제 link가 있는가?
- keyboard focus가 보이는가?
- hover만으로 정보를 전달하지 않는가?
- transform이 reduced motion에서 제거되는가?
- nested interactive 문제가 없는가?

---

### [FAQ]

Q. Card hover는 필수야?
A. 필수는 아니지만 클릭 가능성이나 계층감을 보조하는 feedback으로 사용할 수 있다.

Q. Clickable Card 접근성에서 중요한 것은?
A. link semantic과 keyboard focus가 명확해야 한다.

Q. Card transform은 reduced motion에서 어떻게 해?
A. transform을 제거하고 border나 shadow 같은 정적 feedback으로 대체할 수 있다.

---

# 13. CSS Variable Pseudo Transition Debugging

## 13.1 Variable Debugging

### [개념]

CSS Variable Debugging은 CSS Variables가 정의되지 않았거나, scope가 맞지 않거나, fallback이 없거나, 잘못된 값으로 인해 style이 적용되지 않는 문제를 분석하는 과정이다.

---

### [핵심]

Variable 문제 원인:

- 변수 이름 오타
- `--` 누락
- `var()` 안 변수명 오타
- 변수 정의 scope가 요소 밖에 있음
- fallback 없음
- property에 유효하지 않은 값
- theme attribute가 적용되지 않음
- component scoped variable override 실패
- cascade 순서 문제

---

### [실무]

Debug Flow:

```text
DevTools Computed 확인
→ var() resolved value 확인
→ 변수 정의 위치 확인
→ scope 확인
→ theme attribute 확인
→ fallback 확인
→ property 유효성 확인
```

문제 예:

```text
문제: button background가 적용되지 않음
원인: var(--button-bg) 정의 누락
해결: .button root에 --button-bg 또는 fallback 추가
```

검수 기준:

- DevTools에서 variable resolved value를 확인했는가?
- 변수 이름 오타가 없는가?
- variable scope가 의도와 맞는가?
- fallback이 필요한가?
- theme 상태에서 variable 값이 바뀌는가?

---

### [FAQ]

Q. CSS Variable이 안 먹으면 무엇을 확인해?
A. 변수 이름, 정의 위치, scope, fallback, DevTools computed value를 확인한다.

Q. var() 값이 비어 있으면?
A. 변수가 정의되지 않았거나 scope 밖에 있을 수 있다.

Q. theme variable이 안 바뀌면?
A. data-theme/class 적용 위치와 selector, cascade 순서를 확인한다.

---

## 13.2 Pseudo and Transition Debugging

### [개념]

Pseudo and Transition Debugging은 pseudo class, pseudo element, transition, transform 상태가 예상대로 동작하지 않는 문제를 분석하는 과정이다.

---

### [핵심]

Pseudo / Transition 문제 원인:

- pseudo selector 오타
- hover 환경이 아닌 touch device
- focus-visible style 누락
- disabled 상태에 hover 적용
- `::before` / `::after` content 누락
- 중요한 정보가 CSS content에만 존재
- transition property가 실제 변경되지 않음
- transition 대상 property가 transition에 적합하지 않음
- transition all로 예상치 못한 property가 움직임
- reduced motion에서 motion이 제거되지 않음
- transform으로 stacking context 생성

---

### [실무]

Debug Flow:

```text
Pseudo Selector 확인
→ 상태 강제 확인
→ content 확인
→ transition property 확인
→ computed style 변경 확인
→ hover/pointer 환경 확인
→ reduced motion 확인
→ stacking context 확인
```

문제 예:

```text
문제: ::before가 보이지 않음
원인: content property 누락
해결: content: ""; 추가
```

```text
문제: hover animation이 모바일에서 이상하게 남음
원인: touch 환경에서 hover 의존
해결: @media (hover: hover) and (pointer: fine) 조건 적용
```

검수 기준:

- DevTools에서 pseudo state를 강제해 확인했는가?
- pseudo element content가 있는가?
- hover와 focus-visible을 모두 확인했는가?
- transition 대상 property가 실제로 변경되는가?
- reduced motion 설정에서 motion이 줄어드는가?

---

### [FAQ]

Q. ::before가 안 보이면 무엇을 확인해?
A. content property, display, size, color, position을 확인한다.

Q. hover가 모바일에서 이상하면?
A. touch 환경에서는 hover가 없거나 불안정하므로 hover media query를 검토한다.

Q. transition이 안 되는 이유는?
A. transition 대상 property가 바뀌지 않거나, property가 transition 가능한 값이 아닐 수 있다.

Q. transform 후 layer 문제가 생기면?
A. transform이 stacking context를 만들 수 있으므로 z-index와 stacking context를 확인한다.

---

# 14. Comparison Rules

## 14.1 CSS Variables vs Hardcoded Values

### [개념]

CSS Variables는 재사용 가능한 값이고 Hardcoded Values는 CSS property에 직접 작성된 값이다.

---

### [핵심]

| 비교       | CSS Variables            | Hardcoded Values  |
| ---------- | ------------------------ | ----------------- |
| 재사용성   | 높음                     | 낮음              |
| theme 변경 | 쉬움                     | 어려움            |
| 일관성     | 좋음                     | 깨지기 쉬움       |
| 디버깅     | scope 확인 필요          | 즉시 값 확인 쉬움 |
| 적합       | token, component variant | one-off 값        |
| 주의       | 이름/scope 관리 필요     | 중복 증가         |

---

### [실무]

선택 기준:

```text
반복 색상 → CSS Variables
반복 spacing → CSS Variables
component variant 값 → Scoped Variables
임시 테스트 값 → Hardcoded 가능
단발성 계산 값 → Hardcoded 가능
```

---

### [FAQ]

Q. CSS Variables와 Hardcoded Values 차이는?
A. CSS Variables는 재사용 가능한 값이고 Hardcoded Values는 직접 property에 작성된 값이다.

Q. 반복되는 값은 어떻게 관리해?
A. CSS Variables 또는 Design Token으로 관리하는 것이 좋다.

Q. 모든 값을 변수로 만들어야 해?
A. 아니다. 반복되거나 의미 있는 디자인 값 위주로 token화한다.

---

## 14.2 Global Token vs Scoped Variable

### [개념]

Global Token은 프로젝트 전체에서 공유하는 디자인 값이고 Scoped Variable은 특정 component 내부에서 사용하는 값이다.

---

### [핵심]

| 비교     | Global Token      | Scoped Variable       |
| -------- | ----------------- | --------------------- |
| 범위     | 전역              | component 내부        |
| 예시     | `--color-primary` | `--button-bg`         |
| 목적     | 디자인 기준       | component 구현        |
| override | theme 단위        | variant/state 단위    |
| 위치     | `:root`           | component root        |
| 주의     | 과도한 세분화     | component prefix 필요 |

---

### [실무]

선택 기준:

```text
브랜드 색상 → Global Token
spacing scale → Global Token
button background → Scoped Variable
card padding → Scoped Variable
danger variant 값 → Scoped Variable + Global Token 참조
```

---

### [FAQ]

Q. Global Token과 Scoped Variable 차이는?
A. Global Token은 전체 디자인 기준이고 Scoped Variable은 component 내부 구현 값이다.

Q. button-bg는 global token이야 scoped variable이야?
A. 일반적으로 Button Component 내부의 scoped variable이다.

Q. Scoped Variable도 Global Token을 참조할 수 있어?
A. 가능하다. `--button-bg: var(--color-primary);`처럼 사용할 수 있다.

---

## 14.3 Pseudo Class vs Pseudo Element

### [개념]

Pseudo Class는 요소의 상태나 조건을 선택하고, Pseudo Element는 요소의 일부 또는 가상 요소를 선택한다.

---

### [핵심]

| 비교      | Pseudo Class                       | Pseudo Element                  |
| --------- | ---------------------------------- | ------------------------------- |
| 기호      | `:`                                | `::`                            |
| 선택 기준 | 상태/조건                          | 요소 일부/가상 요소             |
| 예시      | `:hover`, `:focus-visible`         | `::before`, `::placeholder`     |
| 사용      | interaction, structure, form state | decoration, marker, placeholder |
| 주의      | 상태 접근성                        | content 접근성                  |

---

### [실무]

선택 기준:

```text
hover 상태 → Pseudo Class
focus-visible 상태 → Pseudo Class
invalid input 상태 → Pseudo Class / Attribute Selector
장식선 추가 → Pseudo Element
placeholder style → Pseudo Element
list marker style → Pseudo Element
```

---

### [FAQ]

Q. Pseudo Class와 Pseudo Element 차이는?
A. Pseudo Class는 상태나 조건을 선택하고 Pseudo Element는 요소 일부나 가상 요소를 선택한다.

Q. hover는 Pseudo Class야?
A. 맞다. `:hover`는 pseudo class다.

Q. before는 Pseudo Element야?
A. 맞다. `::before`는 pseudo element다.

---

## 14.4 Transition vs Animation

### [개념]

Transition은 상태 변화 사이를 부드럽게 연결하는 기능이고 Animation은 keyframes를 기반으로 독립적인 움직임을 정의하는 기능이다.

---

### [핵심]

| 비교   | Transition            | Animation              |
| ------ | --------------------- | ---------------------- |
| 트리거 | 상태 변화             | keyframes 실행         |
| 문법   | transition            | @keyframes + animation |
| 적합   | hover/focus/open 상태 | loading, 반복 motion   |
| 제어   | 단순                  | 복잡                   |
| 주의   | property 변경 필요    | reduced motion 중요    |

---

### [실무]

선택 기준:

```text
button hover 색상 변화 → Transition
card hover 이동 → Transition
loading spinner → Animation
skeleton shimmer → Animation
modal fade in/out → Transition 또는 Animation
```

---

### [FAQ]

Q. Transition과 Animation 차이는?
A. Transition은 상태 변화 사이를 보간하고 Animation은 keyframes로 독립 motion을 실행한다.

Q. hover 효과에는 뭐가 좋아?
A. 일반적으로 transition이 적합하다.

Q. loading spinner에는 뭐가 좋아?
A. animation이 적합할 수 있다.

---

# 15. Common Mistakes

## 15.1 CSS Variables Pseudo Transition Common Mistakes

### [개념]

CSS Variables, Pseudo Selector, Transition 실수는 style 미적용, theme 오류, 접근성 저하, motion 문제, component state 불일치로 이어진다.

---

### [핵심]

자주 발생하는 실수:

- CSS Variable 이름 오타
- `--` 누락
- `var()` fallback 누락
- variable scope 오해
- global token과 scoped variable 혼동
- component variant에 하드코딩 값 반복
- dark mode contrast 재검수 누락
- hover만 작성하고 focus-visible 누락
- disabled 상태에도 hover/active 적용
- `::before` / `::after` content 누락
- 중요한 정보를 CSS content에만 작성
- placeholder를 label처럼 사용
- transition all 남용
- 너무 긴 transition duration
- transform motion 과다
- opacity 0 요소가 focus 가능
- reduced motion 대응 누락
- transform으로 stacking context가 생기는 점 누락
- hover/pointer media query 없이 touch 환경에 hover 의존

---

### [실무]

Troubleshooting Flow:

```text
Interaction Style Bug
→ CSS Variable resolved value 확인
→ selector 상태 확인
→ pseudo class 강제 확인
→ pseudo element content 확인
→ transition property 확인
→ reduced motion 확인
→ accessibility state 확인
→ component state 동기화 확인
```

문제 예:

```text
문제: dark mode에서 card text가 안 보임
원인: component가 hardcoded dark text color 사용
해결: color token 사용 및 dark theme token override
```

```text
문제: keyboard focus가 보이지 않음
원인: hover만 작성하고 focus-visible 누락
해결: :focus-visible style 추가
```

```text
문제: before 장식이 보이지 않음
원인: content 누락
해결: content: ""; 추가
```

검수 기준:

- variable resolved value를 DevTools에서 확인했는가?
- state selector와 actual state가 일치하는가?
- focus-visible이 있는가?
- 중요한 정보가 CSS content에만 있지 않은가?
- reduced motion이 적용되는가?

---

### [FAQ]

Q. CSS Variables에서 가장 흔한 실수는 뭐야?
A. 변수 이름 오타, scope 오해, fallback 누락, hardcoded value 반복이 흔하다.

Q. Pseudo Selector에서 가장 흔한 실수는 뭐야?
A. hover만 작성하고 focus-visible을 누락하거나 before/after content를 빠뜨리는 것이다.

Q. Transition에서 가장 흔한 실수는 뭐야?
A. `transition: all` 남용, 과도한 duration, reduced motion 미고려가 흔하다.

Q. CSS Variables Pseudo Transition 문제는 어떻게 디버깅해?
A. variable resolved value, selector state, pseudo element content, transition property, reduced motion을 확인한다.

---

# 16. Best Practice

## 16.1 CSS Variables Pseudo Transition Best Practice

### [개념]

CSS Variables Pseudo Transition Best Practice는 token 기반 style, 상태 기반 selector, 접근 가능한 focus style, motion 사용자 설정 대응을 함께 적용하는 기준이다.

---

### [핵심]

권장 기준:

- 반복되는 색상, spacing, radius, duration은 CSS Variables로 관리한다.
- Global Token과 Component Scoped Variable을 구분한다.
- component variant는 scoped variable override로 처리한다.
- theme는 color token override로 처리한다.
- dark mode에서는 contrast와 focus-visible을 재검수한다.
- hover와 focus-visible을 함께 설계한다.
- disabled 상태는 hover/active에서 제외한다.
- form state는 visual style과 aria 상태를 함께 관리한다.
- pseudo element는 장식 목적 중심으로 사용한다.
- 중요한 정보는 CSS content에만 넣지 않는다.
- transition property를 명확히 지정한다.
- `transition: all`을 피한다.
- transform motion은 작고 의미 있게 사용한다.
- opacity로 숨김 처리 시 focus/click 가능성을 확인한다.
- `prefers-reduced-motion`을 고려한다.
- touch 환경에서는 hover 의존을 피한다.

---

### [실무]

Recommended Pattern:

```css
:root {
  --color-primary: #2563eb;
  --color-primary-hover: #1d4ed8;
  --duration-fast: 180ms;
  --ease-standard: ease;
}

.button {
  --button-bg: var(--color-primary);
  --button-hover-bg: var(--color-primary-hover);
  --button-color: #ffffff;

  color: var(--button-color);
  background-color: var(--button-bg);
  transition:
    background-color var(--duration-fast) var(--ease-standard),
    transform var(--duration-fast) var(--ease-standard);
}

@media (hover: hover) and (pointer: fine) {
  .button:not(:disabled):hover {
    background-color: var(--button-hover-bg);
  }
}

.button:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.button:not(:disabled):active {
  transform: translateY(1px);
}

.button:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

@media (prefers-reduced-motion: reduce) {
  .button {
    transition: background-color var(--duration-fast) var(--ease-standard);
  }

  .button:not(:disabled):active {
    transform: none;
  }
}
```

Review Checklist:

```md
- [ ] 반복 값이 CSS Variables로 관리되는가?
- [ ] Global Token과 Scoped Variable이 구분되는가?
- [ ] component variant가 scoped variable로 관리되는가?
- [ ] dark mode contrast를 검수했는가?
- [ ] hover와 focus-visible이 함께 있는가?
- [ ] disabled 상태가 hover/active에서 제외되는가?
- [ ] important information이 CSS content에만 있지 않은가?
- [ ] placeholder를 label 대체로 사용하지 않았는가?
- [ ] transition property가 명확한가?
- [ ] transition all을 피했는가?
- [ ] transform motion이 과하지 않은가?
- [ ] opacity 0 요소의 focus/click 가능성을 확인했는가?
- [ ] prefers-reduced-motion 대응이 있는가?
- [ ] touch 환경에서 hover 의존이 없는가?
```

---

### [FAQ]

Q. CSS Variables Pseudo Transition Best Practice는 뭐야?
A. token 기반 변수, 접근 가능한 상태 selector, 명확한 transition, reduced motion 대응을 함께 적용하는 기준이다.

Q. Interaction Style 검수에서 가장 먼저 볼 것은?
A. hover와 focus-visible, disabled 제외, reduced motion, touch 환경 의존 여부를 먼저 본다.

Q. CSS Variables 검수에서 가장 먼저 볼 것은?
A. 변수 이름, scope, fallback, global/scoped 역할 구분, resolved value를 먼저 확인한다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 CSS Variables, Pseudo Selector, Transition을 사용해 접근 가능하고 유지보수 가능한 interaction style을 생성하고 검수하게 만드는 것이다.

---

# 17. Linkage Reference

## 17.1 Related Documents

### [개념]

Linkage Reference는 이 문서와 다른 HTML/CSS Foundation 문서의 역할을 구분하기 위한 참조 기준이다.

Part12는 CSS Variables, Pseudo Selector 상세, Transition, Reduced Motion의 중심 문서다.

---

### [핵심]

연계 기준:

- CSS Syntax, Selector, Cascade, Specificity의 기본 문법은 Part05를 참조한다.
- Pseudo Class / Pseudo Element의 상세 상태와 실무 적용 기준은 Part12에서 다룬다.
- Viewport, Breakpoint, Responsive Media Query 기본 구조는 Part10을 참조한다.
- Typography, Color, Spacing Token의 기초 기준은 Part11을 참조한다.
- Reset, Normalize, Base Style, CSS File Architecture는 Part13을 참조한다.
- Button, Card, Form, Navigation, Modal 등 Component 적용 예시는 Part14를 참조한다.
- HTML Attribute, ARIA, Accessibility 상태 기준은 Part15를 참조한다.
- 최종 Troubleshooting과 Review Checklist는 Part16을 참조한다.

---

### [실무]

문제 상황별 참조:

```text
CSS selector 기초가 필요함 → Part05
Pseudo Class 상세 상태가 필요함 → Part12
Pseudo Element 실무 기준이 필요함 → Part12
Transition / Reduced Motion 기준이 필요함 → Part12
Responsive breakpoint 기준이 필요함 → Part10
Typography/Spacing token 기준이 필요함 → Part11
Component State 적용 예시가 필요함 → Part14
ARIA state와 접근성 연결이 필요함 → Part15
전체 디버깅 흐름이 필요함 → Part16
```

---

### [FAQ]

Q. Part12는 어떤 역할이야?
A. CSS Variables, Pseudo Selector 상세, Transition, Reduced Motion의 중심 문서다.

Q. Part05와 Part12 차이는 뭐야?
A. Part05는 selector 기초 문법이고 Part12는 pseudo selector와 interaction state 상세 기준이다.

Q. Part10과 Part12 차이는 뭐야?
A. Part10은 responsive media query 기본이고 Part12는 interaction, motion, reduced motion 상세 기준이다.

Q. Part14와 Part12 차이는 뭐야?
A. Part12는 selector와 state 기준이고 Part14는 실제 component styling pattern 적용 예시다.

---

# Retrieval Queries

### [FAQ]

Q. Part12는 어떤 문서야?
A. CSS Variables, Pseudo Class, Pseudo Element, Transition, Reduced Motion의 상세 기준 문서다.

Q. Pseudo Selector 기초는 어디서 봐?
A. 기초 문법은 Part05를 참조하고 상세 상태 기준은 Part12에서 다룬다.

Q. Responsive Media Query 기초는 어디서 봐?
A. viewport, breakpoint, media query 기본 구조는 Part10을 참조한다.

Q. Component State Styling 예시는 어디서 봐?
A. 상세 selector 기준은 Part12, component 적용 예시는 Part14를 참조한다.

Q. CSS Variables가 뭐야?
A. CSS에서 재사용 가능한 값을 `--name`으로 정의하고 `var(--name)`으로 사용하는 기능이다.

Q. CSS Variables는 어디에 정의해?
A. 전역 token은 `:root`, component별 값은 component root class에 정의할 수 있다.

Q. CSS Variables는 runtime에서 바뀔 수 있어?
A. 가능하다. theme 변경이나 state 변경에 따라 cascade로 값이 바뀔 수 있다.

Q. CSS Variable은 어떻게 정의해?
A. `--color-primary: blue;`처럼 `--`로 시작하는 이름에 값을 지정한다.

Q. CSS Variable은 어떻게 사용해?
A. `var(--color-primary)`처럼 `var()` 함수로 사용한다.

Q. Global Token이 뭐야?
A. 프로젝트 전체에서 재사용하는 색상, 간격, 글자 크기 같은 디자인 기준 값이다.

Q. CSS Variables와 Design Token은 같은 거야?
A. CSS Variables는 구현 방법이고 Design Token은 디자인 값의 개념이다.

Q. Component Scoped Variable이 뭐야?
A. 특정 component 내부에서만 사용하는 CSS Variable이다.

Q. Scoped Variable은 왜 써?
A. variant와 state별 style을 중복 없이 관리하기 위해 사용한다.

Q. Theme Variables는 뭐야?
A. light, dark, brand theme처럼 UI 전체 색상 기준을 바꾸기 위한 CSS Variables다.

Q. dark mode는 어떻게 구현해?
A. `data-theme="dark"` 또는 `prefers-color-scheme` 기준으로 color token을 override할 수 있다.

Q. Interaction Pseudo Class가 뭐야?
A. hover, focus, active, disabled처럼 사용자 조작 상태를 선택하는 pseudo class다.

Q. hover만 있으면 충분해?
A. 아니다. keyboard 사용자를 위해 focus-visible도 필요하다.

Q. disabled 상태에는 hover를 적용해도 돼?
A. 일반적으로 disabled 상태는 조작 불가이므로 hover/active 효과를 제외하는 것이 좋다.

Q. Structural Pseudo Class가 뭐야?
A. DOM 구조나 요소 위치를 기준으로 선택하는 pseudo class다.

Q. :where()는 왜 써?
A. selector를 묶으면서 specificity를 낮게 유지하기 위해 사용할 수 있다.

Q. :has()는 뭐야?
A. 특정 하위 요소나 조건을 가진 부모 요소를 선택할 수 있는 pseudo class다.

Q. Form State Pseudo Class가 뭐야?
A. required, invalid, checked, disabled처럼 form control 상태를 선택하는 pseudo class다.

Q. :invalid만 쓰면 error 처리가 충분해?
A. 아니다. error message와 aria-invalid, aria-describedby 연결이 필요하다.

Q. :checked는 어디에 써?
A. checkbox나 radio가 선택된 상태를 styling할 때 사용한다.

Q. ::before와 ::after는 뭐야?
A. 요소 앞이나 뒤에 가상 요소를 생성하는 pseudo element다.

Q. before/after에 content가 꼭 필요해?
A. 대부분 필요하다. content가 없으면 표시되지 않는 경우가 많다.

Q. 중요한 텍스트를 content에 넣어도 돼?
A. 권장하지 않는다. 중요한 정보는 HTML 텍스트나 접근성 정보로 제공해야 한다.

Q. ::placeholder는 뭐야?
A. input이나 textarea의 placeholder text를 styling하는 pseudo element다.

Q. placeholder는 label 대신 쓸 수 있어?
A. 안 된다. placeholder는 입력 힌트이고 label은 필드 이름이다.

Q. ::marker는 뭐야?
A. list item의 bullet이나 number marker를 styling하는 pseudo element다.

Q. ::selection은 뭐야?
A. 사용자가 선택한 텍스트 영역의 style을 지정하는 pseudo element다.

Q. Transition이 뭐야?
A. CSS property 값이 변경될 때 일정 시간 동안 부드럽게 변화하게 만드는 기능이다.

Q. transition: all은 왜 조심해야 해?
A. 예상하지 않은 property까지 transition되어 성능과 디버깅 문제가 생길 수 있기 때문이다.

Q. transition은 어디에 많이 써?
A. button hover, focus, card hover, modal fade, accordion state 등에 사용한다.

Q. Transform은 뭐야?
A. 요소를 시각적으로 이동, 확대/축소, 회전시키는 CSS property다.

Q. transform은 layout에 영향을 줘?
A. 일반적으로 normal flow의 주변 layout에는 직접 영향을 주지 않는다.

Q. transform이 z-index 문제를 만들 수 있어?
A. transform은 stacking context를 만들 수 있어 layer 문제에 영향을 줄 수 있다.

Q. Opacity는 뭐야?
A. 요소의 투명도를 조정하는 CSS property다.

Q. opacity 0이면 display none과 같아?
A. 아니다. 보이지 않지만 layout 공간은 유지되고 focus나 클릭 가능성이 남을 수 있다.

Q. Reduced Motion이 뭐야?
A. 움직임에 민감한 사용자를 위해 animation과 transition 같은 motion을 줄이는 접근성 대응이다.

Q. prefers-reduced-motion은 뭐야?
A. 사용자가 시스템에서 움직임 감소를 선호하는지 감지하는 media feature다.

Q. reduced motion이면 모든 transition을 없애야 해?
A. 반드시 전부 없앨 필요는 없지만 큰 움직임과 반복 animation은 줄이는 것이 좋다.

Q. Button Interaction에서 가장 중요한 상태는?
A. hover, focus-visible, active, disabled 상태를 함께 설계하는 것이다.

Q. disabled button에도 hover를 줘도 돼?
A. 권장하지 않는다. disabled는 조작 불가 상태가 명확해야 한다.

Q. Card hover는 필수야?
A. 필수는 아니지만 클릭 가능성이나 계층감을 보조하는 feedback으로 사용할 수 있다.

Q. CSS Variable이 안 먹으면 무엇을 확인해?
A. 변수 이름, 정의 위치, scope, fallback, DevTools computed value를 확인한다.

Q. theme variable이 안 바뀌면?
A. data-theme/class 적용 위치와 selector, cascade 순서를 확인한다.

Q. ::before가 안 보이면 무엇을 확인해?
A. content property, display, size, color, position을 확인한다.

Q. hover가 모바일에서 이상하면?
A. touch 환경에서는 hover가 없거나 불안정하므로 hover media query를 검토한다.

Q. transition이 안 되는 이유는?
A. transition 대상 property가 바뀌지 않거나, property가 transition 가능한 값이 아닐 수 있다.

Q. CSS Variables와 Hardcoded Values 차이는?
A. CSS Variables는 재사용 가능한 값이고 Hardcoded Values는 직접 property에 작성된 값이다.

Q. Global Token과 Scoped Variable 차이는?
A. Global Token은 전체 디자인 기준이고 Scoped Variable은 component 내부 구현 값이다.

Q. Pseudo Class와 Pseudo Element 차이는?
A. Pseudo Class는 상태나 조건을 선택하고 Pseudo Element는 요소 일부나 가상 요소를 선택한다.

Q. Transition과 Animation 차이는?
A. Transition은 상태 변화 사이를 보간하고 Animation은 keyframes로 독립 motion을 실행한다.

Q. CSS Variables에서 가장 흔한 실수는 뭐야?
A. 변수 이름 오타, scope 오해, fallback 누락, hardcoded value 반복이 흔하다.

Q. Pseudo Selector에서 가장 흔한 실수는 뭐야?
A. hover만 작성하고 focus-visible을 누락하거나 before/after content를 빠뜨리는 것이다.

Q. Transition에서 가장 흔한 실수는 뭐야?
A. `transition: all` 남용, 과도한 duration, reduced motion 미고려가 흔하다.

Q. CSS Variables Pseudo Transition Best Practice는 뭐야?
A. token 기반 변수, 접근 가능한 상태 selector, 명확한 transition, reduced motion 대응을 함께 적용하는 기준이다.

Q. Interaction Style 검수에서 가장 먼저 볼 것은?
A. hover와 focus-visible, disabled 제외, reduced motion, touch 환경 의존 여부를 먼저 본다.

Q. Part05와 Part12 차이는 뭐야?
A. Part05는 selector 기초 문법이고 Part12는 pseudo selector와 interaction state 상세 기준이다.

Q. Part10과 Part12 차이는 뭐야?
A. Part10은 responsive media query 기본이고 Part12는 interaction, motion, reduced motion 상세 기준이다.

Q. Part14와 Part12 차이는 뭐야?
A. Part12는 selector와 state 기준이고 Part14는 실제 component styling pattern 적용 예시다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 CSS Variables, Pseudo Selector, Transition을 사용해 접근 가능하고 유지보수 가능한 interaction style을 생성하고 검수하게 만드는 것이다.
