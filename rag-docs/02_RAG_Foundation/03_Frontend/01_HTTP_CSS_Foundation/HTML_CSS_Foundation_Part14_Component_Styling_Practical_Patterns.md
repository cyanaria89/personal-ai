# HTML CSS Foundation Part14 - Component Styling Practical Patterns

---

# 1. Document Role

## 1.1 Document Role Concept

### [개념]

이 문서는 Button, Card, Badge, Form Field, Input, Navigation, Modal, Dropdown, Alert, Tabs, Accordion 같은 UI Component의 실전 Styling Pattern을 다룬다.

Part14는 CSS 문법 기초 문서가 아니라, HTML/CSS Foundation에서 배운 구조, selector, layout, responsive, variable, accessibility 기준을 실제 Component 단위로 적용하는 문서다.

---

### [핵심]

문서 역할:

- Component Styling 기준을 다룬다.
- Component Class Naming 기준을 다룬다.
- Component State Styling 기준을 다룬다.
- Component Responsive Styling 기준을 다룬다.
- Button, Card, Form, Navigation, Modal, Dropdown, Alert, Tabs, Accordion 실전 패턴을 다룬다.
- CSS Variables와 scoped variable을 component에 적용한다.
- Pseudo Class, Pseudo Element, Transition을 component 상태에 적용한다.
- HTML Attribute와 ARIA 상태를 component style과 연결한다.
- 접근성 검수 항목을 component 기준으로 정리한다.

연계 기준:

- CSS selector, cascade, specificity 기초는 Part05를 참조한다.
- Flexbox 상세 기준은 Part07을 참조한다.
- Grid 상세 기준은 Part08을 참조한다.
- Position, ZIndex, Stacking Context 기준은 Part09를 참조한다.
- Responsive Media Query 기준은 Part10을 참조한다.
- Typography, Color, Spacing 기준은 Part11을 참조한다.
- CSS Variables와 State Styling 상세 기준은 Part12를 참조한다.
- Reset, Base Style, Styling Architecture 기준은 Part13을 참조한다.
- HTML Attribute와 ARIA 상세 기준은 Part15를 참조한다.
- Component 문제 진단과 Review Checklist는 Part16을 참조한다.

---

### [실무]

문서 사용 기준:

```text
Component별 HTML/CSS 패턴 필요 → Part14
Button/Card/Form/Modal/Dropdown/Tabs 구현 기준 필요 → Part14
Component state class와 aria state 연결 필요 → Part14 + Part15
CSS Variables로 component variant 관리 필요 → Part12 + Part14
Responsive component 적용 필요 → Part10 + Part14
Component troubleshooting 필요 → Part16
```

Component Styling Flow:

```text
Component 역할 정의
→ Semantic HTML 선택
→ Required Attribute 확인
→ Root Class 작성
→ Element Class 작성
→ CSS Variables 정의
→ Base Style 작성
→ Variant Style 작성
→ State Style 작성
→ Responsive Style 작성
→ Accessibility State 검수
```

---

### [FAQ]

Q. Part14는 어떤 문서야?
A. HTML/CSS 기초 기준을 실제 UI Component Styling Pattern에 적용하는 문서다.

Q. Component Styling에서 가장 먼저 정할 것은?
A. Component의 역할과 semantic HTML 구조를 먼저 정해야 한다.

Q. Component State Styling 상세 기준은 어디서 봐?
A. CSS state selector와 transition 상세는 Part12, ARIA 상태 기준은 Part15를 함께 참조한다.

Q. Component 문제 진단은 어디서 봐?
A. Component별 패턴은 Part14, troubleshooting과 review checklist는 Part16을 참조한다.

---

# 2. Component Styling

## 2.1 Component Styling Concept

### [개념]

Component Styling은 Button, Card, Form Field, Modal처럼 재사용 가능한 UI 단위를 기준으로 CSS를 작성하는 방식이다.

Component는 HTML 구조, CSS class, state, variant, responsive, accessibility를 함께 가진다.

---

### [핵심]

Component Styling 핵심:

- Component의 역할을 먼저 정의한다.
- Semantic HTML을 우선 선택한다.
- Component root class를 둔다.
- Component 내부 element class를 둔다.
- Variant class와 state class를 구분한다.
- CSS Variables로 반복 값을 관리한다.
- State Styling은 실제 HTML/ARIA 상태와 일치해야 한다.
- Hover만이 아니라 focus-visible을 함께 설계한다.
- Responsive 상태에서도 component가 깨지지 않아야 한다.
- Component는 page style에 과도하게 의존하지 않아야 한다.

---

### [실무]

Component 기본 구조:

```html
<article class="festival-card festival-card-featured">
  <img
    class="festival-card-image"
    src="/images/festival.jpg"
    alt="서울 야간 축제 조명"
  />
  <div class="festival-card-body">
    <h2 class="festival-card-title">Seoul Light Festival</h2>
    <p class="festival-card-description">Night festival in Seoul.</p>
  </div>
</article>
```

CSS 기본 구조:

```css
.festival-card {
  --card-padding: var(--space-6);
  --card-bg: var(--color-surface);
  --card-border: var(--color-border);

  display: grid;
  overflow: hidden;
  background-color: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: var(--radius-lg);
}

.festival-card-featured {
  --card-border: var(--color-primary);
}

.festival-card-body {
  display: grid;
  gap: var(--space-3);
  padding: var(--card-padding);
}
```

검수 기준:

- Component root class가 있는가?
- 내부 element class가 역할을 표현하는가?
- variant class와 state class가 구분되는가?
- CSS Variables로 component 값을 관리하는가?
- Semantic HTML이 component 역할과 맞는가?
- Component가 독립적으로 재사용 가능한가?

---

### [FAQ]

Q. Component Styling이 뭐야?
A. 재사용 가능한 UI 단위를 기준으로 HTML 구조와 CSS class, state, variant를 함께 설계하는 방식이다.

Q. Component root class는 왜 필요해?
A. component scope를 명확히 하고 style 충돌을 줄이기 위해 필요하다.

Q. variant와 state 차이는 뭐야?
A. variant는 component 종류이고 state는 현재 상태다.

Q. Component가 page style에 의존하면 왜 안 좋아?
A. 다른 page에서 재사용할 때 깨지거나 예상과 다르게 보일 수 있기 때문이다.

---

# 3. Button Component

## 3.1 Button Component Concept

### [개념]

Button Component는 사용자가 특정 동작을 실행할 때 사용하는 interactive component다.

Button은 이동 목적이 아니라 “저장”, “삭제”, “열기”, “제출” 같은 action을 실행할 때 사용한다.

---

### [핵심]

Button 핵심:

- 동작 실행에는 `<button>`을 사용한다.
- 링크 이동에는 `<a href>`를 사용한다.
- form 내부 button에는 `type`을 명시한다.
- `type="button"`은 일반 동작 버튼이다.
- `type="submit"`은 form 제출 버튼이다.
- variant는 primary, secondary, danger, ghost 등으로 나눌 수 있다.
- state는 hover, focus-visible, active, disabled, loading을 고려한다.
- icon-only button에는 accessible name이 필요하다.
- disabled 상태는 hover/active에서 제외한다.
- touch target을 충분히 확보한다.

---

### [실무]

HTML 예:

```html
<button class="button button-primary" type="button">Save</button>

<button class="button button-danger" type="button">Delete</button>

<button class="icon-button" type="button" aria-label="Close dialog">
  <span aria-hidden="true">×</span>
</button>
```

CSS 예:

```css
.button {
  --button-bg: var(--color-primary);
  --button-color: #ffffff;
  --button-border: transparent;
  --button-hover-bg: var(--color-primary-hover);

  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  gap: var(--space-2);
  padding-inline: var(--space-4);
  color: var(--button-color);
  background-color: var(--button-bg);
  border: 1px solid var(--button-border);
  border-radius: var(--radius-md);
  font-weight: 600;
  text-decoration: none;
  transition:
    background-color var(--duration-fast) var(--ease-standard),
    border-color var(--duration-fast) var(--ease-standard),
    transform var(--duration-fast) var(--ease-standard);
}

.button-secondary {
  --button-bg: var(--color-surface);
  --button-color: var(--color-text);
  --button-border: var(--color-border);
  --button-hover-bg: var(--color-surface-hover);
}

.button-danger {
  --button-bg: var(--color-danger);
  --button-color: #ffffff;
  --button-hover-bg: var(--color-danger-hover);
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

Icon Button:

```css
.icon-button {
  display: inline-grid;
  place-items: center;
  width: 44px;
  height: 44px;
  color: var(--color-text);
  background-color: transparent;
  border: 0;
  border-radius: var(--radius-md);
}

.icon-button:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}
```

검수 기준:

- action에는 button을 사용했는가?
- navigation에는 anchor를 사용했는가?
- form 내부 button type이 명시되어 있는가?
- disabled 상태가 hover/active에서 제외되는가?
- focus-visible이 명확한가?
- icon-only button에 aria-label이 있는가?
- min-height 또는 hit area가 충분한가?

---

### [FAQ]

Q. Button Component는 언제 써?
A. 저장, 삭제, 열기, 제출처럼 사용자가 동작을 실행할 때 사용한다.

Q. 링크 이동도 button으로 만들어도 돼?
A. 이동 목적이면 `<a href>`를 사용하는 것이 semantic하게 맞다.

Q. button type은 왜 명시해야 해?
A. form 내부에서 의도치 않은 submit을 막기 위해 필요하다.

Q. icon-only button에는 무엇이 필요해?
A. `aria-label` 또는 visually-hidden text로 accessible name을 제공해야 한다.

---

# 4. Card Component

## 4.1 Card Component Concept

### [개념]

Card Component는 이미지, 제목, 설명, meta 정보, action을 하나의 독립된 콘텐츠 단위로 묶는 UI component다.

Festival Card, Product Card, Article Card, Dashboard Card에 자주 사용한다.

---

### [핵심]

Card 핵심:

- Card는 독립적인 콘텐츠 단위다.
- 제목 heading level은 page 구조에 맞춰 정한다.
- 이미지에는 의미 있는 alt가 필요하다.
- Card 전체가 link처럼 보이면 link semantic을 명확히 해야 한다.
- Card 내부 nested interactive element를 주의한다.
- Grid/Flex layout 안에서 responsive하게 줄어들어야 한다.
- hover는 보조 feedback이다.
- keyboard focus가 명확해야 한다.

---

### [실무]

HTML 예:

```html
<article class="card festival-card">
  <img
    class="card-image"
    src="/images/seoul-light.jpg"
    alt="서울 빛 축제 야간 조명"
    width="640"
    height="360"
    loading="lazy"
  />

  <div class="card-body">
    <h2 class="card-title">
      <a class="card-link" href="/festivals/seoul-light">
        Seoul Light Festival
      </a>
    </h2>
    <p class="card-description">서울에서 열리는 야간 조명 축제입니다.</p>
  </div>
</article>
```

CSS 예:

```css
.card {
  display: grid;
  overflow: hidden;
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  transition:
    border-color var(--duration-fast) var(--ease-standard),
    transform var(--duration-fast) var(--ease-standard);
}

.card-image {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}

.card-body {
  display: grid;
  gap: var(--space-3);
  padding: var(--space-6);
}

.card-title {
  margin: 0;
  font-size: var(--text-xl);
  line-height: 1.2;
}

.card-description {
  margin: 0;
  color: var(--color-text-muted);
}

.card-link {
  color: inherit;
  text-decoration: none;
}

.card-link:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

@media (hover: hover) and (pointer: fine) {
  .card:has(.card-link:hover) {
    border-color: var(--color-primary);
    transform: translateY(-2px);
  }
}
```

검수 기준:

- Card가 article/section 등 의미 있는 구조인가?
- 제목 heading level이 page 구조와 맞는가?
- 이미지 alt가 의미에 맞는가?
- link focus가 보이는가?
- hover만으로 정보가 전달되지 않는가?
- card가 작은 화면에서 overflow되지 않는가?
- nested interactive element가 충돌하지 않는가?

---

### [FAQ]

Q. Card Component는 뭐야?
A. 이미지, 제목, 설명, action을 하나의 독립된 콘텐츠 단위로 묶는 UI component다.

Q. Card 전체를 클릭 가능하게 만들어도 돼?
A. 가능하지만 link semantic과 keyboard focus가 명확해야 한다.

Q. Card 제목 heading은 항상 h2야?
A. 아니다. page heading hierarchy에 맞춰 h2, h3 등을 선택해야 한다.

Q. Card hover는 필수야?
A. 필수는 아니며 클릭 가능성이나 계층감을 보조하는 feedback으로 사용할 수 있다.

---

# 5. Badge Component

## 5.1 Badge Component Concept

### [개념]

Badge Component는 짧은 상태, 분류, 카운트, 라벨을 표시하는 작은 UI component다.

예: `NEW`, `HOT`, `진행중`, `마감`, `축제`, `무료`.

---

### [핵심]

Badge 핵심:

- 짧은 텍스트를 사용한다.
- 색상만으로 의미를 전달하지 않는다.
- 상태 의미가 중요하면 텍스트가 함께 있어야 한다.
- 크기는 작아도 읽기 쉬워야 한다.
- line-height와 padding을 명확히 설정한다.
- badge가 interactive하면 button/link semantic을 사용해야 한다.
- 상태별 variant를 CSS Variables로 관리할 수 있다.

---

### [실무]

HTML 예:

```html
<span class="badge badge-success">진행중</span>
<span class="badge badge-danger">마감</span>
<span class="badge badge-neutral">무료</span>
```

CSS 예:

```css
.badge {
  --badge-bg: var(--color-surface);
  --badge-color: var(--color-text);
  --badge-border: var(--color-border);

  display: inline-flex;
  align-items: center;
  min-height: 1.5rem;
  padding-inline: var(--space-2);
  color: var(--badge-color);
  background-color: var(--badge-bg);
  border: 1px solid var(--badge-border);
  border-radius: 999px;
  font-size: var(--text-sm);
  font-weight: 600;
  line-height: 1;
}

.badge-success {
  --badge-bg: var(--color-success-surface);
  --badge-color: var(--color-success-text);
  --badge-border: var(--color-success-border);
}

.badge-danger {
  --badge-bg: var(--color-danger-surface);
  --badge-color: var(--color-danger-text);
  --badge-border: var(--color-danger-border);
}
```

검수 기준:

- badge 텍스트가 짧고 명확한가?
- 색상만으로 상태를 전달하지 않는가?
- contrast가 충분한가?
- line-height와 padding이 읽기 쉬운가?
- interactive badge라면 semantic이 올바른가?

---

### [FAQ]

Q. Badge Component는 뭐야?
A. 짧은 상태, 분류, 카운트, 라벨을 표시하는 작은 UI component다.

Q. Badge를 색상만으로 구분해도 돼?
A. 안 된다. 상태 의미는 텍스트로도 전달되어야 한다.

Q. Badge가 클릭 가능하면 span을 써도 돼?
A. 클릭 동작이면 button, 이동이면 anchor를 사용해야 한다.

Q. Badge variant는 어떻게 관리해?
A. CSS Variables로 background, color, border 값을 variant별로 override할 수 있다.

---

# 6. Form Field Component

## 6.1 Form Field Component Concept

### [개념]

Form Field Component는 label, input, helper text, error message를 하나의 입력 단위로 묶는 component다.

Form 접근성에서 label 연결, error 연결, required 표시, invalid 상태가 중요하다.

---

### [핵심]

Form Field 핵심:

- label과 input은 연결되어야 한다.
- input에는 id와 name이 필요하다.
- helper text는 aria-describedby로 연결할 수 있다.
- error message는 aria-describedby와 aria-invalid로 연결한다.
- required는 시각 표시와 semantic 상태를 함께 고려한다.
- placeholder는 label을 대체할 수 없다.
- error 상태는 색상만으로 전달하지 않는다.
- disabled와 readonly는 의미가 다르다.

---

### [실무]

기본 Field:

```html
<div class="form-field">
  <label class="form-label" for="email">Email</label>
  <input
    class="form-input"
    id="email"
    name="email"
    type="email"
    autocomplete="email"
    aria-describedby="email-help"
  />
  <p class="form-help" id="email-help">Use a valid email address.</p>
</div>
```

Error Field:

```html
<div class="form-field form-field-error">
  <label class="form-label" for="password">
    Password <span aria-hidden="true">*</span>
    <span class="visually-hidden">required</span>
  </label>
  <input
    class="form-input"
    id="password"
    name="password"
    type="password"
    autocomplete="current-password"
    required
    aria-invalid="true"
    aria-describedby="password-error"
  />
  <p class="form-error" id="password-error">Password is required.</p>
</div>
```

CSS:

```css
.form-field {
  display: grid;
  gap: var(--space-2);
}

.form-label {
  font-weight: 600;
}

.form-help {
  margin: 0;
  color: var(--color-text-muted);
  font-size: var(--text-sm);
}

.form-error {
  margin: 0;
  color: var(--color-danger);
  font-size: var(--text-sm);
}

.form-field-error .form-input,
.form-input[aria-invalid="true"] {
  border-color: var(--color-danger);
}
```

검수 기준:

- label for와 input id가 일치하는가?
- input name이 있는가?
- helper/error text가 aria-describedby로 연결되는가?
- aria-invalid가 실제 오류 상태와 일치하는가?
- required 표시가 보조 기술에도 전달되는가?
- placeholder를 label로 사용하지 않았는가?

---

### [FAQ]

Q. Form Field Component는 뭐야?
A. label, input, helper text, error message를 하나의 입력 단위로 묶는 component다.

Q. error message는 어떻게 연결해?
A. input의 aria-describedby가 error message id를 참조하도록 연결한다.

Q. placeholder를 label 대신 쓰면 안 돼?
A. 안 된다. placeholder는 입력 힌트이고 label은 필드 이름이다.

Q. required 표시는 어떻게 해?
A. required attribute와 시각 표시, 필요 시 screen reader용 텍스트를 함께 제공한다.

---

# 7. Input Component

## 7.1 Input Component Concept

### [개념]

Input Component는 사용자가 텍스트, 숫자, 이메일, 비밀번호, 검색어 등을 입력하는 form control이다.

Input Styling은 상태별 border, focus, invalid, disabled, readonly를 명확히 표현해야 한다.

---

### [핵심]

Input 핵심:

- input type은 입력 목적에 맞게 지정한다.
- width는 부모에 맞게 유동적으로 설정한다.
- focus-visible 또는 focus style이 명확해야 한다.
- invalid 상태는 aria-invalid와 error message를 함께 사용한다.
- disabled 상태와 readonly 상태를 구분한다.
- placeholder contrast를 너무 낮게 만들지 않는다.
- 모바일 keyboard를 고려해 type과 autocomplete를 정확히 쓴다.

---

### [실무]

HTML:

```html
<input
  class="input"
  id="keyword"
  name="keyword"
  type="search"
  placeholder="축제 이름 검색"
/>
```

CSS:

```css
.input {
  width: 100%;
  min-width: 0;
  min-height: 44px;
  padding-inline: var(--space-4);
  color: var(--color-text);
  background-color: var(--color-background);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font: inherit;
}

.input::placeholder {
  color: var(--color-text-muted);
}

.input:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
  border-color: var(--color-primary);
}

.input[aria-invalid="true"] {
  border-color: var(--color-danger);
}

.input:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

.input:read-only {
  background-color: var(--color-surface);
}
```

검수 기준:

- input type이 입력 목적과 맞는가?
- width 100%와 min-width 0으로 overflow를 방지하는가?
- focus-visible이 명확한가?
- invalid style과 aria-invalid가 일치하는가?
- disabled/readonly 스타일이 구분되는가?
- placeholder가 label을 대체하지 않는가?

---

### [FAQ]

Q. Input Component에서 가장 중요한 것은?
A. 입력 목적에 맞는 type, label 연결, focus-visible, invalid/error 연결이다.

Q. input width 100%인데 overflow가 생기면?
A. box-sizing과 min-width, padding, parent width를 확인한다.

Q. disabled와 readonly style은 같아도 돼?
A. 의미가 다르므로 가능하면 구분해서 표현하는 것이 좋다.

Q. invalid 상태는 CSS만 있으면 돼?
A. 아니다. aria-invalid와 error message 연결이 필요하다.

---

# 8. Navigation Component

## 8.1 Navigation Component Concept

### [개념]

Navigation Component는 사용자가 사이트나 앱의 주요 영역으로 이동할 수 있게 하는 link group이다.

Navigation은 semantic `nav`, list structure, link, current page 표시가 중요하다.

---

### [핵심]

Navigation 핵심:

- navigation 영역에는 `nav`를 사용한다.
- 여러 nav가 있으면 aria-label로 구분한다.
- link 목록은 ul/li 구조를 사용할 수 있다.
- 현재 페이지 link에는 `aria-current="page"`를 사용한다.
- link는 이동 목적이므로 `<a href>`를 사용한다.
- mobile navigation에서는 menu button과 expanded state가 필요할 수 있다.
- keyboard focus가 명확해야 한다.
- hover만으로 current 상태를 구분하지 않는다.

---

### [실무]

HTML:

```html
<nav class="site-nav" aria-label="Main Navigation">
  <ul class="site-nav-list list-unstyled">
    <li>
      <a class="site-nav-link" href="/festivals" aria-current="page">
        Festivals
      </a>
    </li>
    <li>
      <a class="site-nav-link" href="/calendar">Calendar</a>
    </li>
  </ul>
</nav>
```

CSS:

```css
.site-nav-list {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}

.site-nav-link {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding-inline: var(--space-3);
  color: var(--color-text);
  text-decoration: none;
  border-radius: var(--radius-md);
}

.site-nav-link[aria-current="page"] {
  color: var(--color-primary);
  font-weight: 700;
}

.site-nav-link:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}
```

Mobile Menu Button:

```html
<button
  class="menu-button"
  type="button"
  aria-expanded="false"
  aria-controls="mobile-menu"
>
  Menu
</button>

<nav id="mobile-menu" class="mobile-menu" hidden aria-label="Mobile Navigation">
  ...
</nav>
```

검수 기준:

- nav에 aria-label이 필요한가?
- link에 href가 있는가?
- 현재 페이지에 aria-current가 있는가?
- mobile menu button에 aria-expanded와 aria-controls가 있는가?
- 닫힌 mobile menu 내부로 focus가 가지 않는가?
- focus-visible이 보이는가?

---

### [FAQ]

Q. Navigation Component는 뭐야?
A. 사용자가 사이트나 앱의 주요 영역으로 이동할 수 있게 하는 link group이다.

Q. nav에는 aria-label이 필요해?
A. nav가 여러 개 있거나 목적 구분이 필요하면 aria-label을 제공하는 것이 좋다.

Q. 현재 페이지 link는 어떻게 표시해?
A. `aria-current="page"`와 시각 스타일을 함께 사용한다.

Q. mobile menu에는 어떤 ARIA가 필요해?
A. menu button에 aria-expanded와 aria-controls를 적용하고 실제 열림 상태와 동기화해야 한다.

---

# 9. Modal Component

## 9.1 Modal Component Concept

### [개념]

Modal Component는 사용자의 현재 작업 흐름 위에 Dialog를 띄워 중요한 선택, 확인, 입력을 요구하는 overlay component다.

Modal은 시각적 layer뿐 아니라 focus management, keyboard handling, ARIA, scroll lock이 중요하다.

---

### [핵심]

Modal 핵심:

- dialog 역할을 명확히 한다.
- dialog 제목과 aria-labelledby를 연결한다.
- modal이면 `aria-modal="true"`를 사용한다.
- backdrop과 dialog layer를 분리한다.
- dialog는 viewport를 넘지 않아야 한다.
- 내용이 길면 내부 scroll을 제공한다.
- focus trap이 필요하다.
- Escape로 닫기 같은 keyboard behavior는 JavaScript와 연결된다.
- 닫힌 modal 내부로 focus가 가면 안 된다.

---

### [실무]

HTML:

```html
<div class="modal-backdrop">
  <section
    class="modal-dialog"
    role="dialog"
    aria-modal="true"
    aria-labelledby="delete-dialog-title"
  >
    <header class="modal-header">
      <h2 class="modal-title" id="delete-dialog-title">Delete Festival</h2>
      <button class="icon-button" type="button" aria-label="Close dialog">
        <span aria-hidden="true">×</span>
      </button>
    </header>

    <div class="modal-body">
      <p>Are you sure you want to delete this festival?</p>
    </div>

    <footer class="modal-actions">
      <button class="button button-secondary" type="button">Cancel</button>
      <button class="button button-danger" type="button">Delete</button>
    </footer>
  </section>
</div>
```

CSS:

```css
.modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: var(--z-modal);
  display: grid;
  place-items: center;
  padding: var(--space-4);
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-dialog {
  width: min(100%, 480px);
  max-height: calc(100dvh - 32px);
  overflow: auto;
  background-color: var(--color-background);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
}

.modal-header,
.modal-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-3);
  padding: var(--space-4);
}

.modal-body {
  padding: var(--space-4);
}
```

검수 기준:

- role dialog 또는 native dialog 사용 기준이 명확한가?
- aria-labelledby가 실제 title id를 참조하는가?
- aria-modal 상태가 실제 modal behavior와 일치하는가?
- dialog가 작은 viewport에서 잘리지 않는가?
- focus trap이 구현되는가?
- close button에 accessible name이 있는가?
- z-index layer가 다른 component와 충돌하지 않는가?

---

### [FAQ]

Q. Modal Component는 뭐야?
A. 현재 화면 위에 Dialog를 띄워 중요한 선택, 확인, 입력을 요구하는 overlay component다.

Q. Modal은 CSS만으로 충분해?
A. 아니다. focus trap, Escape handling, scroll lock은 JavaScript와 함께 필요하다.

Q. Modal 제목은 어떻게 연결해?
A. 제목 요소 id를 dialog의 aria-labelledby가 참조하도록 연결한다.

Q. 닫힌 modal 내부로 focus가 가면 안 되는 이유는?
A. 화면에 보이지 않는 요소에 keyboard focus가 이동해 사용자가 혼란을 느끼기 때문이다.

---

# 10. Dropdown Component

## 10.1 Dropdown Component Concept

### [개념]

Dropdown Component는 trigger button을 통해 숨겨진 menu 또는 option panel을 열고 닫는 component다.

Dropdown은 position, z-index, overflow, aria-expanded, focus management가 중요하다.

---

### [핵심]

Dropdown 핵심:

- trigger는 button을 사용한다.
- trigger에 aria-expanded를 적용한다.
- trigger에 aria-controls로 panel id를 연결할 수 있다.
- panel은 닫힌 상태에서 hidden 처리한다.
- panel은 trigger 기준으로 배치할 수 있다.
- overflow hidden 부모에 의해 잘릴 수 있다.
- keyboard interaction과 focus management가 필요하다.
- hover만으로 열리게 만들면 접근성 문제가 생길 수 있다.

---

### [실무]

HTML:

```html
<div class="dropdown">
  <button
    class="dropdown-trigger"
    type="button"
    aria-expanded="false"
    aria-controls="sort-menu"
  >
    Sort
  </button>

  <div class="dropdown-panel" id="sort-menu" hidden>
    <button class="dropdown-item" type="button">Newest</button>
    <button class="dropdown-item" type="button">Popular</button>
  </div>
</div>
```

CSS:

```css
.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-trigger {
  min-height: 44px;
}

.dropdown-panel {
  position: absolute;
  inset-block-start: calc(100% + var(--space-2));
  inset-inline-end: 0;
  z-index: var(--z-dropdown);
  min-width: 12rem;
  padding: var(--space-2);
  background-color: var(--color-background);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
}

.dropdown-item {
  display: flex;
  align-items: center;
  width: 100%;
  min-height: 40px;
  padding-inline: var(--space-3);
  color: var(--color-text);
  background: transparent;
  border: 0;
  text-align: start;
}
```

검수 기준:

- trigger가 button인가?
- aria-expanded가 실제 open state와 일치하는가?
- aria-controls id가 실제 panel을 참조하는가?
- 닫힌 panel이 hidden 처리되는가?
- 닫힌 panel 내부로 focus가 가지 않는가?
- overflow clipping 문제가 없는가?
- keyboard로 열고 닫고 항목 이동이 가능한가?

---

### [FAQ]

Q. Dropdown Component는 뭐야?
A. trigger button으로 숨겨진 menu나 panel을 열고 닫는 component다.

Q. Dropdown trigger는 a 태그로 만들어도 돼?
A. 이동이 아니라 열고 닫는 동작이면 button이 적절하다.

Q. aria-expanded는 어디에 붙여?
A. dropdown을 여는 trigger button에 붙인다.

Q. z-index를 높여도 dropdown이 잘리면?
A. 부모 overflow hidden/auto 또는 stacking context 문제를 확인해야 한다.

---

# 11. Alert Component

## 11.1 Alert Component Concept

### [개념]

Alert Component는 성공, 오류, 경고, 정보 같은 상태 메시지를 사용자에게 전달하는 component다.

Alert는 색상뿐 아니라 텍스트, role, live region 기준을 함께 고려해야 한다.

---

### [핵심]

Alert 핵심:

- 상태 메시지를 명확히 전달한다.
- 색상만으로 상태를 전달하지 않는다.
- 오류나 경고에는 텍스트 label을 포함한다.
- 동적으로 표시되는 중요한 메시지는 live region을 고려한다.
- `role="alert"`는 즉시 알림이 필요한 메시지에 사용할 수 있다.
- 모든 alert에 role alert를 남용하지 않는다.
- dismissible alert는 close button에 accessible name이 필요하다.

---

### [실무]

HTML:

```html
<div class="alert alert-error" role="alert">
  <strong class="alert-title">Error</strong>
  <p class="alert-message">Failed to save festival information.</p>
</div>
```

Dismissible Alert:

```html
<div class="alert alert-info">
  <div>
    <strong class="alert-title">Notice</strong>
    <p class="alert-message">Festival schedule has been updated.</p>
  </div>
  <button class="icon-button" type="button" aria-label="Dismiss notice">
    <span aria-hidden="true">×</span>
  </button>
</div>
```

CSS:

```css
.alert {
  --alert-bg: var(--color-surface);
  --alert-color: var(--color-text);
  --alert-border: var(--color-border);

  display: flex;
  align-items: start;
  justify-content: space-between;
  gap: var(--space-3);
  padding: var(--space-4);
  color: var(--alert-color);
  background-color: var(--alert-bg);
  border: 1px solid var(--alert-border);
  border-radius: var(--radius-md);
}

.alert-error {
  --alert-bg: var(--color-danger-surface);
  --alert-color: var(--color-danger-text);
  --alert-border: var(--color-danger-border);
}

.alert-title,
.alert-message {
  margin: 0;
}
```

검수 기준:

- alert 상태가 텍스트로 전달되는가?
- 색상만으로 상태를 구분하지 않는가?
- role alert를 필요한 경우에만 사용하는가?
- dismiss button에 accessible name이 있는가?
- alert 내용이 너무 길어 component가 깨지지 않는가?

---

### [FAQ]

Q. Alert Component는 뭐야?
A. 성공, 오류, 경고, 정보 같은 상태 메시지를 사용자에게 전달하는 component다.

Q. role alert는 언제 써?
A. 동적으로 나타나는 중요 메시지를 즉시 알릴 필요가 있을 때 사용한다.

Q. 모든 alert에 role alert를 써도 돼?
A. 남용하면 screen reader 경험이 나빠질 수 있으므로 중요한 동적 메시지에 제한적으로 사용한다.

Q. Alert 상태를 색상만으로 표시해도 돼?
A. 안 된다. 상태 텍스트나 아이콘, 제목 등 추가 단서가 필요하다.

---

# 12. Tabs Component

## 12.1 Tabs Component Concept

### [개념]

Tabs Component는 여러 panel 중 하나를 선택해 보여주는 component다.

Tabs는 `tablist`, `tab`, `tabpanel`, `aria-selected`, `aria-controls`, `hidden` 상태 동기화가 중요하다.

---

### [핵심]

Tabs 핵심:

- tab button group은 tablist 역할을 가진다.
- 각 tab은 선택 상태를 가진다.
- 선택된 tab에는 `aria-selected="true"`를 사용한다.
- tab은 연결된 tabpanel을 aria-controls로 참조할 수 있다.
- tabpanel은 aria-labelledby로 tab을 참조할 수 있다.
- 비활성 panel은 hidden 처리한다.
- keyboard interaction은 JavaScript와 함께 구현한다.
- visual active state와 ARIA state가 일치해야 한다.

---

### [실무]

HTML:

```html
<div class="tabs">
  <div class="tabs-list" role="tablist" aria-label="Festival information">
    <button
      class="tabs-trigger"
      id="tab-info"
      type="button"
      role="tab"
      aria-selected="true"
      aria-controls="panel-info"
    >
      Info
    </button>
    <button
      class="tabs-trigger"
      id="tab-reviews"
      type="button"
      role="tab"
      aria-selected="false"
      aria-controls="panel-reviews"
    >
      Reviews
    </button>
  </div>

  <section
    class="tabs-panel"
    id="panel-info"
    role="tabpanel"
    aria-labelledby="tab-info"
  >
    Info content
  </section>

  <section
    class="tabs-panel"
    id="panel-reviews"
    role="tabpanel"
    aria-labelledby="tab-reviews"
    hidden
  >
    Reviews content
  </section>
</div>
```

CSS:

```css
.tabs-list {
  display: flex;
  gap: var(--space-2);
  border-bottom: 1px solid var(--color-border);
}

.tabs-trigger {
  min-height: 44px;
  padding-inline: var(--space-4);
  color: var(--color-text-muted);
  background: transparent;
  border: 0;
  border-bottom: 2px solid transparent;
}

.tabs-trigger[aria-selected="true"] {
  color: var(--color-primary);
  border-bottom-color: var(--color-primary);
  font-weight: 700;
}

.tabs-trigger:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.tabs-panel {
  padding-block: var(--space-6);
}
```

검수 기준:

- tablist, tab, tabpanel 관계가 올바른가?
- aria-selected와 visual active state가 일치하는가?
- aria-controls와 aria-labelledby가 실제 id를 참조하는가?
- 비활성 panel이 hidden 처리되는가?
- hidden panel 내부로 focus가 가지 않는가?
- keyboard interaction이 가능한가?

---

### [FAQ]

Q. Tabs Component는 뭐야?
A. 여러 panel 중 하나를 선택해 보여주는 component다.

Q. 선택된 tab은 어떻게 표시해?
A. `aria-selected="true"`와 active visual style을 함께 사용한다.

Q. 비활성 tabpanel은 어떻게 처리해?
A. `hidden`을 사용해 화면과 accessibility tree에서 숨길 수 있다.

Q. Tabs는 CSS만으로 충분해?
A. ARIA 상태와 keyboard interaction 동기화가 필요하므로 JavaScript가 함께 필요할 수 있다.

---

# 13. Accordion Component

## 13.1 Accordion Component Concept

### [개념]

Accordion Component는 여러 section 중 사용자가 필요한 section을 펼치거나 접을 수 있는 disclosure component다.

Accordion은 trigger button, aria-expanded, aria-controls, panel hidden 상태가 중요하다.

---

### [핵심]

Accordion 핵심:

- trigger는 button을 사용한다.
- trigger에 aria-expanded를 적용한다.
- trigger에 aria-controls로 panel id를 연결한다.
- panel은 닫힌 상태에서 hidden 처리할 수 있다.
- heading 안에 button을 넣어 section 구조를 명확히 할 수 있다.
- visual state와 ARIA state가 일치해야 한다.
- transition을 적용하더라도 reduced motion을 고려한다.

---

### [실무]

HTML:

```html
<div class="accordion">
  <h3 class="accordion-heading">
    <button
      class="accordion-trigger"
      type="button"
      aria-expanded="false"
      aria-controls="faq-panel-1"
    >
      What is FestaPick?
    </button>
  </h3>

  <div class="accordion-panel" id="faq-panel-1" hidden>
    <p>FestaPick helps users discover festivals.</p>
  </div>
</div>
```

CSS:

```css
.accordion {
  border-block-start: 1px solid var(--color-border);
}

.accordion-heading {
  margin: 0;
}

.accordion-trigger {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  min-height: 48px;
  padding-block: var(--space-3);
  color: var(--color-text);
  background: transparent;
  border: 0;
  text-align: start;
}

.accordion-trigger[aria-expanded="true"] {
  color: var(--color-primary);
}

.accordion-trigger:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.accordion-panel {
  padding-block-end: var(--space-4);
}
```

검수 기준:

- trigger가 button인가?
- aria-expanded가 실제 open state와 일치하는가?
- aria-controls가 panel id와 일치하는가?
- 닫힌 panel이 hidden 처리되는가?
- heading 구조가 page hierarchy와 맞는가?
- keyboard로 조작 가능한가?

---

### [FAQ]

Q. Accordion Component는 뭐야?
A. 여러 section 중 필요한 section을 펼치거나 접을 수 있는 disclosure component다.

Q. Accordion trigger는 div로 만들어도 돼?
A. 권장하지 않는다. 조작 가능한 trigger는 button을 사용하는 것이 좋다.

Q. aria-expanded는 어디에 붙여?
A. accordion panel을 여는 trigger button에 붙인다.

Q. Accordion panel이 닫히면 어떻게 처리해?
A. `hidden`으로 숨기고 내부 focus가 이동하지 않도록 관리한다.

---

# 14. Layout Component Patterns

## 14.1 Stack Cluster Grid

### [개념]

Layout Component Pattern은 반복되는 배치 구조를 재사용 가능한 CSS class로 정의하는 방식이다.

Stack, Cluster, Grid는 작은 UI layout에서 자주 사용되는 기본 패턴이다.

---

### [핵심]

Layout Pattern 핵심:

- Stack은 세로 방향 간격을 관리한다.
- Cluster는 가로 방향 item 묶음과 wrap을 관리한다.
- Grid는 card list나 dashboard layout을 관리한다.
- gap을 사용해 item 간격을 일관되게 만든다.
- margin collapse와 item별 margin 중복을 줄인다.
- responsive layout을 component 밖에서 제어할 수 있다.

---

### [실무]

Stack:

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}
```

Cluster:

```css
.cluster {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--space-3);
}
```

Auto Grid:

```css
.auto-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr));
  gap: var(--space-6);
}
```

검수 기준:

- layout pattern이 component 내부 style과 충돌하지 않는가?
- gap으로 간격을 관리하는가?
- 작은 화면에서 wrap 또는 1 column이 되는가?
- item min-width 문제가 없는가?
- pattern class가 너무 많은 역할을 하지 않는가?

---

### [FAQ]

Q. Stack Pattern은 뭐야?
A. 세로 방향으로 item을 배치하고 gap으로 간격을 관리하는 layout pattern이다.

Q. Cluster Pattern은 뭐야?
A. 가로 방향 item을 배치하되 wrap과 gap을 허용하는 layout pattern이다.

Q. Auto Grid는 언제 써?
A. card list처럼 가능한 공간에 맞춰 column 수를 자동 조정할 때 사용한다.

Q. gap을 쓰는 이유는?
A. item별 margin보다 간격 관리가 일관되고 단순하기 때문이다.

---

# 15. Component State Styling

## 15.1 State Styling Concept

### [개념]

Component State Styling은 component의 현재 상태에 따라 시각 스타일을 바꾸는 방식이다.

상태는 hover, focus-visible, active, disabled, selected, expanded, invalid, current, loading 등이 있다.

---

### [핵심]

State Styling 핵심:

- visual state와 semantic state가 일치해야 한다.
- hover는 보조 feedback이다.
- focus-visible은 keyboard 접근성에 필수다.
- selected 상태는 aria-selected와 연결할 수 있다.
- expanded 상태는 aria-expanded와 연결할 수 있다.
- invalid 상태는 aria-invalid와 연결할 수 있다.
- current 상태는 aria-current와 연결할 수 있다.
- loading 상태는 disabled, aria-busy, loading text와 함께 검토한다.
- state class와 ARIA attribute selector를 혼용할 수 있으나 기준을 명확히 해야 한다.

---

### [실무]

ARIA State Styling:

```css
.tabs-trigger[aria-selected="true"] {
  color: var(--color-primary);
}

.accordion-trigger[aria-expanded="true"] {
  color: var(--color-primary);
}

.nav-link[aria-current="page"] {
  font-weight: 700;
}

.input[aria-invalid="true"] {
  border-color: var(--color-danger);
}
```

State Class 예:

```css
.toast[data-state="open"] {
  opacity: 1;
}

.toast[data-state="closed"] {
  opacity: 0;
}
```

검수 기준:

- state style이 실제 상태와 일치하는가?
- ARIA attribute를 styling hook으로 사용할 때 의미도 정확한가?
- state class가 semantic state를 대체하지 않는가?
- hover만 있고 focus-visible이 빠지지 않았는가?
- disabled/loading 상태에서 중복 submit이 방지되는가?

---

### [FAQ]

Q. Component State Styling이 뭐야?
A. component의 현재 상태에 따라 시각 스타일을 바꾸는 방식이다.

Q. ARIA attribute로 CSS selector를 써도 돼?
A. 가능하다. 다만 ARIA 상태는 실제 UI 상태와 정확히 일치해야 한다.

Q. data-state는 ARIA를 대체해?
A. 아니다. data-state는 styling hook이고 접근성 상태는 ARIA로 전달해야 한다.

Q. selected 상태는 어떻게 표현해?
A. Tabs 같은 경우 `aria-selected="true"`와 visual active style을 함께 사용한다.

---

# 16. Component Responsive Styling

## 16.1 Responsive Component Concept

### [개념]

Component Responsive Styling은 Component가 다양한 viewport, parent width, content length에서 깨지지 않도록 만드는 스타일 기준이다.

Component는 page layout에 따라 줄어들거나 늘어날 수 있으므로 자체적인 overflow 대응이 필요하다.

---

### [핵심]

Responsive Component 핵심:

- width는 가능한 유동적으로 작성한다.
- fixed width를 남용하지 않는다.
- image에는 max-width와 aspect-ratio를 적용한다.
- button group은 wrap 또는 column 전환을 고려한다.
- card grid는 auto-fit/minmax를 활용한다.
- modal은 viewport height를 넘지 않게 한다.
- dropdown은 화면 밖으로 나가지 않게 검토한다.
- table은 overflow-x wrapper를 고려한다.
- 긴 텍스트에는 overflow-wrap을 고려한다.
- touch target을 충분히 확보한다.

---

### [실무]

Responsive Card Grid:

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr));
  gap: var(--space-6);
}
```

Responsive Button Group:

```css
.button-group {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}

@media (max-width: 480px) {
  .button-group {
    flex-direction: column;
  }

  .button-group .button {
    width: 100%;
  }
}
```

Responsive Modal:

```css
.modal-dialog {
  width: min(100%, 480px);
  max-height: calc(100dvh - 32px);
  overflow: auto;
}
```

검수 기준:

- 작은 viewport에서 horizontal overflow가 없는가?
- component width가 부모에 맞게 줄어드는가?
- button group이 작은 화면에서 깨지지 않는가?
- modal이 viewport 안에 들어오는가?
- 긴 텍스트가 component를 밀어내지 않는가?
- touch target이 충분한가?

---

### [FAQ]

Q. Component Responsive Styling이 뭐야?
A. component가 다양한 화면 폭과 콘텐츠 길이에서 깨지지 않도록 만드는 스타일 기준이다.

Q. Component에서 fixed width는 왜 조심해야 해?
A. 작은 화면이나 좁은 parent에서 horizontal overflow를 만들 수 있기 때문이다.

Q. Button Group은 모바일에서 어떻게 처리해?
A. flex-wrap을 적용하거나 작은 화면에서 column과 width 100%로 전환할 수 있다.

Q. Modal은 모바일에서 무엇을 확인해야 해?
A. width, max-height, overflow, focus, fixed layer를 확인해야 한다.

---

# 17. Component Accessibility Checklist

## 17.1 Component Accessibility Concept

### [개념]

Component Accessibility Checklist는 Component 단위에서 semantic HTML, keyboard focus, ARIA 상태, label 연결, hidden 상태를 검수하는 기준이다.

접근성 상세 기준은 Part15에서 다루고, 이 문서는 Component 적용 관점의 체크 항목을 정리한다.

---

### [핵심]

Component Accessibility 핵심:

- button/link 역할을 구분한다.
- interactive element는 keyboard로 조작 가능해야 한다.
- focus-visible이 명확해야 한다.
- icon-only button에는 accessible name이 필요하다.
- form field는 label과 연결되어야 한다.
- error message는 input과 연결되어야 한다.
- dropdown/accordion은 aria-expanded와 hidden 상태를 동기화한다.
- tabs는 aria-selected와 panel hidden 상태를 동기화한다.
- modal은 focus trap과 dialog labeling이 필요하다.
- 색상만으로 상태를 전달하지 않는다.

---

### [실무]

Checklist:

```md
- [ ] action은 button, navigation은 anchor를 사용하는가?
- [ ] button type이 명시되어 있는가?
- [ ] icon-only button에 aria-label이 있는가?
- [ ] keyboard focus-visible이 보이는가?
- [ ] disabled 상태가 명확한가?
- [ ] form label과 input id가 연결되는가?
- [ ] error message가 aria-describedby로 연결되는가?
- [ ] aria-invalid가 실제 오류 상태와 일치하는가?
- [ ] aria-expanded가 실제 open state와 일치하는가?
- [ ] aria-selected가 실제 selected state와 일치하는가?
- [ ] aria-current가 현재 page link에 적용되는가?
- [ ] hidden content 내부로 focus가 이동하지 않는가?
- [ ] modal dialog에 accessible title이 있는가?
- [ ] 색상 외 상태 전달 수단이 있는가?
```

---

### [FAQ]

Q. Component 접근성에서 가장 먼저 볼 것은?
A. semantic element, keyboard focus, accessible name, ARIA state를 먼저 확인한다.

Q. Component 접근성 상세 기준은 어디서 봐?
A. HTML Attribute와 ARIA 상세 기준은 Part15를 참조한다.

Q. Component 접근성 검수 전체 흐름은 어디서 봐?
A. 최종 Review Checklist와 Troubleshooting Flow는 Part16을 참조한다.

Q. 색상만으로 상태를 표시하면 왜 안 돼?
A. 색상 구분이 어려운 사용자에게 상태 정보가 전달되지 않을 수 있기 때문이다.

---

# 18. Component Styling Troubleshooting

## 18.1 Component Styling Bug

### [개념]

Component Styling Bug는 Component의 style, state, layout, responsive, accessibility가 예상과 다르게 동작하는 문제다.

주요 원인은 className 오타, CSS import 누락, token 누락, state 불일치, ARIA 불일치, hidden/focus 문제, responsive overflow다.

---

### [핵심]

Component Bug 원인:

- Component CSS 파일 import 누락
- className과 selector 불일치
- root class 누락
- variant class 누락
- CSS Variable 정의 누락
- scoped variable scope 오류
- hover만 있고 focus-visible 누락
- disabled 상태에 active style 적용
- ARIA state와 visual state 불일치
- hidden content 내부 focus 가능
- modal/dropdown z-index 문제
- parent overflow clipping
- fixed width로 responsive overflow 발생
- nested interactive element 충돌

---

### [실무]

Troubleshooting Flow:

```text
Component 역할 확인
→ Semantic HTML 확인
→ CSS import 확인
→ className/selector 확인
→ CSS Variable 확인
→ Variant class 확인
→ State attribute 확인
→ ARIA state 확인
→ Focus/Hidden 상태 확인
→ Responsive overflow 확인
→ Part16 Checklist 참조
```

문제 예:

```text
문제: Button danger variant 색상이 적용되지 않음
원인: button-danger class 누락
해결: base class와 variant class 함께 적용
```

```text
문제: Accordion은 닫혔는데 panel 내부 link에 focus가 감
원인: hidden 처리 누락
해결: 닫힌 panel에 hidden 적용 및 aria-expanded 동기화
```

```text
문제: Dropdown z-index를 높여도 잘림
원인: 부모 overflow hidden clipping
해결: overflow 구조 수정 또는 layer root/portal 검토
```

검수 기준:

- Component root class가 있는가?
- CSS Variables resolved value가 정상인가?
- visual state와 ARIA state가 일치하는가?
- hidden/focus 상태가 일치하는가?
- responsive viewport에서 overflow가 없는가?
- 문제 진단은 Part16 흐름과 연결되는가?

---

### [FAQ]

Q. Component style이 안 먹으면 무엇을 먼저 봐?
A. CSS import, className/selector 일치, root class, variant class를 먼저 확인한다.

Q. Component state가 이상하면 무엇을 봐?
A. visual state, state class, data-state, ARIA attribute가 실제 상태와 일치하는지 확인한다.

Q. 닫힌 component 내부로 focus가 들어가면?
A. hidden 처리와 focus management가 잘못된 것이므로 닫힌 content를 focus 불가능하게 해야 한다.

Q. Component troubleshooting 전체 기준은 어디서 봐?
A. Part16의 Troubleshooting Review Checklist를 참조한다.

---

# 19. Comparison Rules

## 19.1 Button vs Link

### [개념]

Button과 Link는 모두 사용자가 조작하는 요소지만 의미가 다르다.

Button은 action 실행이고 Link는 navigation 이동이다.

---

### [핵심]

| 비교           | Button                | Link             |
| -------------- | --------------------- | ---------------- |
| HTML           | `<button>`            | `<a href>`       |
| 목적           | 동작 실행             | 페이지/위치 이동 |
| keyboard       | Enter, Space          | Enter            |
| form 영향      | submit 가능           | submit 아님      |
| 필수 attribute | type 권장             | href 필요        |
| 예시           | 저장, 삭제, 모달 열기 | 상세 페이지 이동 |

---

### [실무]

선택 기준:

```text
저장하기 → button
삭제하기 → button
모달 열기 → button
메뉴 펼치기 → button
상세 페이지 이동 → anchor
외부 사이트 이동 → anchor
```

---

### [FAQ]

Q. Button과 Link 차이는 뭐야?
A. Button은 동작 실행이고 Link는 페이지나 위치 이동이다.

Q. 모달 열기는 button이야 link야?
A. 현재 페이지에서 동작을 실행하므로 button이 적절하다.

Q. 상세 페이지 이동은 button이야 link야?
A. 이동 목적이므로 anchor link가 적절하다.

---

## 19.2 Variant vs State

### [개념]

Variant는 Component의 종류나 시각적 타입이고 State는 Component의 현재 상태다.

---

### [핵심]

| 비교      | Variant                | State                        |
| --------- | ---------------------- | ---------------------------- |
| 의미      | 종류/타입              | 현재 상태                    |
| 예시      | primary, danger, ghost | hover, disabled, selected    |
| 변경 원인 | 디자인 선택            | 사용자 조작/데이터           |
| CSS 방식  | variant class          | pseudo/attribute/state class |
| 지속성    | 상대적으로 고정        | 동적으로 변경                |
| 주의      | naming 명확성          | ARIA 동기화                  |

---

### [실무]

예:

```html
<button class="button button-danger" type="button" disabled>Delete</button>
```

- `button-danger`는 variant다.
- `disabled`는 state다.

---

### [FAQ]

Q. Variant와 State 차이는 뭐야?
A. Variant는 component 종류이고 State는 현재 상태다.

Q. primary는 variant야 state야?
A. variant다.

Q. disabled는 variant야 state야?
A. state다.

---

## 19.3 State Class vs ARIA Attribute

### [개념]

State Class는 styling을 위한 class이고 ARIA Attribute는 접근성 상태를 보조 기술에 전달하는 attribute다.

---

### [핵심]

| 비교      | State Class        | ARIA Attribute         |
| --------- | ------------------ | ---------------------- |
| 목적      | CSS styling        | Accessibility state    |
| 예시      | `.is-open`         | `aria-expanded="true"` |
| 전달 대상 | CSS/browser visual | assistive technology   |
| 의미      | 개발자 정의        | 표준 접근성 의미       |
| 주의      | 의미 전달 아님     | 실제 상태와 일치 필요  |

---

### [실무]

권장:

```html
<button
  class="accordion-trigger"
  type="button"
  aria-expanded="true"
  aria-controls="panel-1"
>
  Details
</button>
```

```css
.accordion-trigger[aria-expanded="true"] {
  color: var(--color-primary);
}
```

필요 시 data-state:

```html
<div class="dropdown-panel" data-state="open">...</div>
```

---

### [FAQ]

Q. State Class와 ARIA Attribute 차이는 뭐야?
A. State Class는 styling용이고 ARIA Attribute는 접근성 상태 전달용이다.

Q. is-open class만 있으면 접근성 상태도 전달돼?
A. 아니다. 필요한 경우 aria-expanded 같은 ARIA 상태를 함께 사용해야 한다.

Q. ARIA Attribute를 CSS selector로 써도 돼?
A. 가능하다. 다만 실제 상태와 정확히 동기화되어야 한다.

---

## 19.4 Component CSS vs Utility CSS

### [개념]

Component CSS는 특정 UI Component의 구조와 디자인을 담당하고 Utility CSS는 작은 단일 목적의 보조 스타일을 제공한다.

---

### [핵심]

| 비교 | Component CSS      | Utility CSS                      |
| ---- | ------------------ | -------------------------------- |
| 목적 | UI 단위 구현       | 단일 보조 스타일                 |
| 예시 | `.button`, `.card` | `.container`, `.visually-hidden` |
| 범위 | component          | 전역 재사용                      |
| 장점 | 의미 명확          | 반복 제거                        |
| 주의 | 중복 가능          | 남용 시 class 복잡               |

---

### [실무]

선택 기준:

```text
Button 디자인 → Component CSS
Card 구조 → Component CSS
Container 폭 제한 → Utility CSS
Visually hidden text → Utility CSS
List marker 제거 → Utility CSS
```

---

### [FAQ]

Q. Component CSS와 Utility CSS 차이는?
A. Component CSS는 UI 단위 구현이고 Utility CSS는 작은 보조 스타일이다.

Q. Button을 utility class만으로 만들면 안 돼?
A. 가능은 하지만 재사용 component라면 component class가 더 명확하다.

Q. visually-hidden은 component야 utility야?
A. 여러 곳에서 재사용되는 접근성 utility다.

---

# 20. Common Mistakes

## 20.1 Component Styling Common Mistakes

### [개념]

Component Styling 실수는 UI 재사용성 저하, style 충돌, 접근성 문제, responsive overflow, 상태 불일치로 이어진다.

---

### [핵심]

자주 발생하는 실수:

- button/link 역할 혼동
- button type 누락
- root class 누락
- className 오타
- variant와 state 혼동
- state class만 쓰고 ARIA 상태 누락
- ARIA 상태와 visual state 불일치
- hover만 있고 focus-visible 누락
- disabled 상태에 hover/active 적용
- icon-only button에 accessible name 누락
- form label과 input 연결 누락
- error message와 input 연결 누락
- modal에 accessible title 누락
- dropdown trigger를 a/div로 구현
- tabs의 aria-selected와 hidden panel 불일치
- accordion trigger를 div로 구현
- hidden content 내부 focus 가능
- fixed width로 mobile overflow 발생
- z-index 문제를 overflow clipping과 혼동
- component가 page style에 과도하게 의존

---

### [실무]

Troubleshooting Flow:

```text
Component Bug
→ Semantic 역할 확인
→ Required Attribute 확인
→ CSS class 확인
→ Variant/State 구분 확인
→ ARIA 상태 확인
→ Focus 상태 확인
→ Hidden 상태 확인
→ Responsive 확인
→ Part16 Checklist 연결
```

문제 예:

```text
문제: 버튼 클릭 시 form이 제출됨
원인: form 내부 button type 누락
해결: 일반 동작 버튼에 type="button" 명시
```

```text
문제: active tab과 보이는 panel이 다름
원인: aria-selected와 hidden panel 상태 불일치
해결: tab selected state와 panel hidden state 동시 업데이트
```

```text
문제: icon button을 screen reader가 읽지 못함
원인: accessible name 누락
해결: aria-label 또는 visually-hidden text 추가
```

검수 기준:

- Component 역할과 HTML 요소가 일치하는가?
- Required Attribute가 있는가?
- Visual State와 Semantic State가 일치하는가?
- Keyboard와 Screen Reader 상태를 확인했는가?
- Responsive viewport에서 component가 깨지지 않는가?

---

### [FAQ]

Q. Component Styling에서 가장 흔한 실수는 뭐야?
A. button/link 혼동, button type 누락, ARIA 상태 불일치, focus-visible 누락이 흔하다.

Q. Component 접근성에서 가장 흔한 실수는 뭐야?
A. accessible name 누락, label 연결 누락, hidden content focus 가능, ARIA state 불일치다.

Q. Component responsive에서 가장 흔한 실수는 뭐야?
A. fixed width, flex wrap 누락, modal max-height 누락, 긴 텍스트 overflow가 흔하다.

Q. Component 문제는 어떤 순서로 확인해?
A. semantic 역할, attribute, class, variant/state, ARIA, focus, hidden, responsive 순서로 확인한다.

---

# 21. Best Practice

## 21.1 Component Styling Best Practice

### [개념]

Component Styling Best Practice는 UI Component를 semantic HTML, 명확한 class naming, token 기반 CSS, 접근 가능한 state, responsive layout으로 구현하는 기준이다.

---

### [핵심]

권장 기준:

- action은 button, navigation은 link를 사용한다.
- form 내부 button에는 type을 명시한다.
- component root class를 사용한다.
- element class는 역할 기반으로 작성한다.
- variant와 state를 구분한다.
- CSS Variables로 component 값을 관리한다.
- global token과 scoped variable을 구분한다.
- hover와 focus-visible을 함께 작성한다.
- disabled 상태에는 hover/active를 적용하지 않는다.
- icon-only button에는 accessible name을 제공한다.
- form field는 label, input, helper/error를 함께 설계한다.
- state style은 ARIA attribute와 실제 UI 상태를 동기화한다.
- modal/dropdown/tabs/accordion은 hidden/focus 상태를 관리한다.
- responsive width, wrap, max-height, overflow를 검토한다.
- 색상만으로 상태를 전달하지 않는다.
- Part16 Checklist로 최종 검수한다.

---

### [실무]

Recommended Component Skeleton:

```html
<section class="component-name component-name-variant" data-state="open">
  <header class="component-name-header">
    <h2 class="component-name-title">Component Title</h2>
  </header>

  <div class="component-name-body">Component content</div>

  <footer class="component-name-actions">
    <button class="button button-primary" type="button">Action</button>
  </footer>
</section>
```

Recommended Component CSS:

```css
.component-name {
  --component-bg: var(--color-surface);
  --component-color: var(--color-text);
  --component-border: var(--color-border);
  --component-padding: var(--space-6);

  display: grid;
  gap: var(--space-4);
  padding: var(--component-padding);
  color: var(--component-color);
  background-color: var(--component-bg);
  border: 1px solid var(--component-border);
  border-radius: var(--radius-lg);
}

.component-name-variant {
  --component-border: var(--color-primary);
}

.component-name[data-state="open"] {
  --component-bg: var(--color-background);
}
```

Review Checklist:

```md
- [ ] Component 역할이 명확한가?
- [ ] Semantic HTML을 사용했는가?
- [ ] Component root class가 있는가?
- [ ] Element class가 역할 기반인가?
- [ ] Variant와 State가 구분되는가?
- [ ] CSS Variables를 사용하는가?
- [ ] Button type이 명시되어 있는가?
- [ ] Link와 Button 역할이 구분되는가?
- [ ] Focus-visible이 보이는가?
- [ ] Icon-only button에 accessible name이 있는가?
- [ ] ARIA state와 visual state가 일치하는가?
- [ ] Hidden content 내부로 focus가 이동하지 않는가?
- [ ] Responsive viewport에서 overflow가 없는가?
- [ ] 색상 외 상태 전달 수단이 있는가?
```

---

### [FAQ]

Q. Component Styling Best Practice는 뭐야?
A. Semantic HTML, 역할 기반 class, token 기반 CSS, 접근 가능한 state, responsive 대응을 함께 적용하는 기준이다.

Q. Component 검수에서 가장 먼저 볼 것은?
A. component 역할, semantic element, required attribute, root class, state 동기화를 먼저 확인한다.

Q. Component style을 유지보수하기 좋게 만들려면?
A. root class, element class, variant class, scoped variable을 일관되게 사용한다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 재사용 가능하고 접근 가능하며 responsive한 UI Component CSS를 생성하고 검수하게 만드는 것이다.

---

# 22. Linkage Reference

## 22.1 Related Documents

### [개념]

Linkage Reference는 이 문서와 다른 HTML/CSS Foundation 문서의 역할을 구분하기 위한 참조 기준이다.

Part14는 Component별 실전 Styling Pattern을 다루는 적용 문서다.

---

### [핵심]

연계 기준:

- Component별 실전 Styling Pattern은 Part14에서 다룬다.
- CSS Syntax, Selector, Cascade, Specificity 기초는 Part05를 참조한다.
- Flexbox 기반 Component Layout은 Part07을 참조한다.
- Grid 기반 Card/List Layout은 Part08을 참조한다.
- Modal, Dropdown, Layer, ZIndex 기준은 Part09를 참조한다.
- Responsive Component Styling 기준은 Part10을 참조한다.
- Typography, Color, Spacing 기준은 Part11을 참조한다.
- CSS Variables, Pseudo Selector, Transition, State Styling 상세 기준은 Part12를 참조한다.
- Reset, Normalize, Styling Architecture 기준은 Part13을 참조한다.
- HTML Attribute와 ARIA의 상세 기준은 Part15를 참조한다.
- Component 문제 진단과 Review Checklist는 Part16을 참조한다.

---

### [실무]

문제 상황별 참조:

```text
Button/Card/Form Component 패턴 필요 → Part14
Component class naming과 CSS 구조 필요 → Part13 + Part14
Component state selector 상세 필요 → Part12 + Part14
ARIA 상태와 attribute 연결 필요 → Part15
Modal/Dropdown z-index 문제 → Part09 + Part14 + Part16
Responsive component overflow 문제 → Part10 + Part14 + Part16
Component 최종 검수 필요 → Part16
```

---

### [FAQ]

Q. Part14는 어떤 역할이야?
A. Button, Card, Form, Modal, Dropdown, Tabs 등 Component별 실전 Styling Pattern을 다루는 적용 문서다.

Q. Part12와 Part14 차이는 뭐야?
A. Part12는 CSS Variables와 state selector 상세 기준이고 Part14는 이를 Component Pattern에 적용하는 문서다.

Q. Part15와 Part14 차이는 뭐야?
A. Part15는 HTML Attribute와 ARIA 상세 기준이고 Part14는 Component 단위 적용 예시를 다룬다.

Q. Component 검수는 어디서 마무리해?
A. Component pattern은 Part14에서 확인하고 최종 Troubleshooting과 Review Checklist는 Part16에서 마무리한다.

---

# Retrieval Queries

### [FAQ]

Q. Part14는 어떤 문서야?
A. HTML/CSS 기초 기준을 실제 UI Component Styling Pattern에 적용하는 문서다.

Q. Component Styling에서 가장 먼저 정할 것은?
A. Component의 역할과 semantic HTML 구조를 먼저 정해야 한다.

Q. Component State Styling 상세 기준은 어디서 봐?
A. CSS state selector와 transition 상세는 Part12, ARIA 상태 기준은 Part15를 함께 참조한다.

Q. Component 문제 진단은 어디서 봐?
A. Component별 패턴은 Part14, troubleshooting과 review checklist는 Part16을 참조한다.

Q. Component Styling이 뭐야?
A. 재사용 가능한 UI 단위를 기준으로 HTML 구조와 CSS class, state, variant를 함께 설계하는 방식이다.

Q. Component root class는 왜 필요해?
A. component scope를 명확히 하고 style 충돌을 줄이기 위해 필요하다.

Q. variant와 state 차이는 뭐야?
A. variant는 component 종류이고 state는 현재 상태다.

Q. Button Component는 언제 써?
A. 저장, 삭제, 열기, 제출처럼 사용자가 동작을 실행할 때 사용한다.

Q. 링크 이동도 button으로 만들어도 돼?
A. 이동 목적이면 `<a href>`를 사용하는 것이 semantic하게 맞다.

Q. button type은 왜 명시해야 해?
A. form 내부에서 의도치 않은 submit을 막기 위해 필요하다.

Q. icon-only button에는 무엇이 필요해?
A. `aria-label` 또는 visually-hidden text로 accessible name을 제공해야 한다.

Q. Card Component는 뭐야?
A. 이미지, 제목, 설명, action을 하나의 독립된 콘텐츠 단위로 묶는 UI component다.

Q. Card 전체를 클릭 가능하게 만들어도 돼?
A. 가능하지만 link semantic과 keyboard focus가 명확해야 한다.

Q. Badge Component는 뭐야?
A. 짧은 상태, 분류, 카운트, 라벨을 표시하는 작은 UI component다.

Q. Badge를 색상만으로 구분해도 돼?
A. 안 된다. 상태 의미는 텍스트로도 전달되어야 한다.

Q. Form Field Component는 뭐야?
A. label, input, helper text, error message를 하나의 입력 단위로 묶는 component다.

Q. error message는 어떻게 연결해?
A. input의 aria-describedby가 error message id를 참조하도록 연결한다.

Q. placeholder를 label 대신 쓰면 안 돼?
A. 안 된다. placeholder는 입력 힌트이고 label은 필드 이름이다.

Q. Input Component에서 가장 중요한 것은?
A. 입력 목적에 맞는 type, label 연결, focus-visible, invalid/error 연결이다.

Q. input width 100%인데 overflow가 생기면?
A. box-sizing과 min-width, padding, parent width를 확인한다.

Q. Navigation Component는 뭐야?
A. 사용자가 사이트나 앱의 주요 영역으로 이동할 수 있게 하는 link group이다.

Q. 현재 페이지 link는 어떻게 표시해?
A. `aria-current="page"`와 시각 스타일을 함께 사용한다.

Q. mobile menu에는 어떤 ARIA가 필요해?
A. menu button에 aria-expanded와 aria-controls를 적용하고 실제 열림 상태와 동기화해야 한다.

Q. Modal Component는 뭐야?
A. 현재 화면 위에 Dialog를 띄워 중요한 선택, 확인, 입력을 요구하는 overlay component다.

Q. Modal은 CSS만으로 충분해?
A. 아니다. focus trap, Escape handling, scroll lock은 JavaScript와 함께 필요하다.

Q. Modal 제목은 어떻게 연결해?
A. 제목 요소 id를 dialog의 aria-labelledby가 참조하도록 연결한다.

Q. Dropdown Component는 뭐야?
A. trigger button으로 숨겨진 menu나 panel을 열고 닫는 component다.

Q. Dropdown trigger는 a 태그로 만들어도 돼?
A. 이동이 아니라 열고 닫는 동작이면 button이 적절하다.

Q. aria-expanded는 어디에 붙여?
A. dropdown을 여는 trigger button에 붙인다.

Q. Alert Component는 뭐야?
A. 성공, 오류, 경고, 정보 같은 상태 메시지를 사용자에게 전달하는 component다.

Q. role alert는 언제 써?
A. 동적으로 나타나는 중요 메시지를 즉시 알릴 필요가 있을 때 사용한다.

Q. Tabs Component는 뭐야?
A. 여러 panel 중 하나를 선택해 보여주는 component다.

Q. 선택된 tab은 어떻게 표시해?
A. `aria-selected="true"`와 active visual style을 함께 사용한다.

Q. Accordion Component는 뭐야?
A. 여러 section 중 필요한 section을 펼치거나 접을 수 있는 disclosure component다.

Q. Accordion trigger는 div로 만들어도 돼?
A. 권장하지 않는다. 조작 가능한 trigger는 button을 사용하는 것이 좋다.

Q. Stack Pattern은 뭐야?
A. 세로 방향으로 item을 배치하고 gap으로 간격을 관리하는 layout pattern이다.

Q. Cluster Pattern은 뭐야?
A. 가로 방향 item을 배치하되 wrap과 gap을 허용하는 layout pattern이다.

Q. Auto Grid는 언제 써?
A. card list처럼 가능한 공간에 맞춰 column 수를 자동 조정할 때 사용한다.

Q. Component State Styling이 뭐야?
A. component의 현재 상태에 따라 시각 스타일을 바꾸는 방식이다.

Q. ARIA attribute로 CSS selector를 써도 돼?
A. 가능하다. 다만 ARIA 상태는 실제 UI 상태와 정확히 일치해야 한다.

Q. data-state는 ARIA를 대체해?
A. 아니다. data-state는 styling hook이고 접근성 상태는 ARIA로 전달해야 한다.

Q. Component Responsive Styling이 뭐야?
A. component가 다양한 화면 폭과 콘텐츠 길이에서 깨지지 않도록 만드는 스타일 기준이다.

Q. Button Group은 모바일에서 어떻게 처리해?
A. flex-wrap을 적용하거나 작은 화면에서 column과 width 100%로 전환할 수 있다.

Q. Component 접근성에서 가장 먼저 볼 것은?
A. semantic element, keyboard focus, accessible name, ARIA state를 먼저 확인한다.

Q. Component 접근성 상세 기준은 어디서 봐?
A. HTML Attribute와 ARIA 상세 기준은 Part15를 참조한다.

Q. Component style이 안 먹으면 무엇을 먼저 봐?
A. CSS import, className/selector 일치, root class, variant class를 먼저 확인한다.

Q. Component state가 이상하면 무엇을 봐?
A. visual state, state class, data-state, ARIA attribute가 실제 상태와 일치하는지 확인한다.

Q. Button과 Link 차이는 뭐야?
A. Button은 동작 실행이고 Link는 페이지나 위치 이동이다.

Q. Variant와 State 차이는 뭐야?
A. Variant는 component 종류이고 State는 현재 상태다.

Q. State Class와 ARIA Attribute 차이는 뭐야?
A. State Class는 styling용이고 ARIA Attribute는 접근성 상태 전달용이다.

Q. Component CSS와 Utility CSS 차이는?
A. Component CSS는 UI 단위 구현이고 Utility CSS는 작은 보조 스타일이다.

Q. Component Styling에서 가장 흔한 실수는 뭐야?
A. button/link 혼동, button type 누락, ARIA 상태 불일치, focus-visible 누락이 흔하다.

Q. Component 접근성에서 가장 흔한 실수는 뭐야?
A. accessible name 누락, label 연결 누락, hidden content focus 가능, ARIA state 불일치다.

Q. Component Styling Best Practice는 뭐야?
A. Semantic HTML, 역할 기반 class, token 기반 CSS, 접근 가능한 state, responsive 대응을 함께 적용하는 기준이다.

Q. Component 검수에서 가장 먼저 볼 것은?
A. component 역할, semantic element, required attribute, root class, state 동기화를 먼저 확인한다.

Q. Part12와 Part14 차이는 뭐야?
A. Part12는 CSS Variables와 state selector 상세 기준이고 Part14는 이를 Component Pattern에 적용하는 문서다.

Q. Part15와 Part14 차이는 뭐야?
A. Part15는 HTML Attribute와 ARIA 상세 기준이고 Part14는 Component 단위 적용 예시를 다룬다.

Q. Component 검수는 어디서 마무리해?
A. Component pattern은 Part14에서 확인하고 최종 Troubleshooting과 Review Checklist는 Part16에서 마무리한다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 재사용 가능하고 접근 가능하며 responsive한 UI Component CSS를 생성하고 검수하게 만드는 것이다.
