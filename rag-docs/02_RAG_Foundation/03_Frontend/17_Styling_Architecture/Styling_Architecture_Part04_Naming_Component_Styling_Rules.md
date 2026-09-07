# Styling Architecture Part04 - Naming Convention, Component Styling, Variant Rules

---

# 1. Naming Convention Rules

## 1.1 Class Naming Rules

### [개념]

Class Naming은 CSS class 이름을 일관되게 작성하는 규칙이다.

Class Naming은 단순 이름 짓기가 아니다.

Class Naming은 Agent가 스타일의 역할, 적용 범위, 컴포넌트 구조, 상태를 검색하고 이해할 수 있게 만드는 Retrieval 기준이다.

좋은 class name은 다음 정보를 포함한다.

- 어떤 컴포넌트인가
- 어떤 요소인가
- 어떤 상태인가
- 어떤 역할인가
- 재사용 가능한가
- 전역 충돌 위험이 있는가

---

### [핵심]

좋은 class name 기준:

- 역할과 의미가 드러난다.
- 컴포넌트 단위 prefix를 사용한다.
- 시각 속성보다 도메인 / 역할 중심이다.
- 너무 짧거나 모호하지 않다.
- 재사용 범위가 명확하다.
- 상태 class는 상태 의미가 드러난다.
- 프로젝트 전체 naming pattern이 일관적이다.

좋은 예:

```css
.festival-card {
}

.festival-card__title {
}

.festival-card__description {
}

.search-form {
}

.search-form__input {
}
```

나쁜 예:

```css
.box {
}

.red {
}

.big {
}

.a1 {
}

.temp {
}
```

---

### [실무]

Class Naming 리뷰 기준:

```md
- [ ] 이름이 역할을 설명하는가?
- [ ] 색상 / 크기 중심 이름을 남용하지 않는가?
- [ ] 같은 패턴이 프로젝트 전체에서 유지되는가?
- [ ] 컴포넌트 이름과 스타일 이름이 연결되는가?
- [ ] 상태 class가 명확한가?
- [ ] 전역 class 충돌 가능성이 낮은가?
```

Class Naming 판단 Flow:

```text
Style 대상 확인
→ Component 이름 확인
→ Element 역할 확인
→ State 여부 확인
→ Variant 여부 확인
→ Naming Pattern 적용
→ 충돌 가능성 검토
```

---

### [FAQ]

Q. class 이름은 짧을수록 좋아?
A. 아니다. 의미가 명확한 이름이 더 중요하다.

Q. blue-button 같은 이름은 안 좋아?
A. 색상이 바뀌면 이름과 실제 스타일이 어긋날 수 있다. primary-button 같은 의미 기반 이름이 좋다.

Q. class 이름에 컴포넌트 이름을 넣어야 해?
A. Plain CSS에서는 권장된다. CSS Module에서는 scope가 있지만 의미 파악을 위해 역할 기반 이름을 쓰는 것이 좋다.

Q. box, wrap, area 같은 이름은 쓰면 안 돼?
A. 무조건 금지는 아니지만 의미가 모호하면 유지보수와 검색성이 떨어진다.

---

## 1.2 Role-based Naming

### [개념]

Role-based Naming은 색상, 크기, 위치 같은 시각 속성보다 UI 역할과 의미를 기준으로 이름 짓는 방식이다.

역할 기반 이름은 디자인 변경에 강하다.

색상 기반 이름은 디자인 변경 시 이름과 실제 스타일이 어긋날 수 있다.

---

### [핵심]

권장 naming 방향:

```text
시각 속성 기반
→ .blue-button
→ .big-title
→ .red-text

역할 기반
→ .primary-button
→ .page-title
→ .error-message
```

역할 기반 이름 장점:

- 디자인 변경에 강함
- UI 의미가 명확함
- Agent 검색성 향상
- Review Agent 검토 쉬움
- component variant와 연결 쉬움

---

### [실무]

나쁜 예:

```css
.red-text {
  color: var(--color-error);
}

.big-button {
  padding: var(--spacing-4);
}
```

좋은 예:

```css
.error-message {
  color: var(--color-error);
}

.primary-button {
  padding: var(--spacing-4);
}
```

Naming 변환 기준:

```text
red
→ error / danger / warning

blue
→ primary / info

gray
→ muted / secondary / disabled

big
→ large / title / emphasized

small
→ small / caption / helper
```

---

### [FAQ]

Q. 왜 색상 이름으로 class를 만들면 안 좋아?
A. 색상이 바뀌면 이름과 실제 스타일이 달라져 코드 의미가 깨질 수 있다.

Q. primary와 blue는 뭐가 달라?
A. primary는 UI 역할이고 blue는 색상값이다. 컴포넌트 이름에는 역할 기반 이름이 더 좋다.

Q. error-message와 red-text 중 뭐가 좋아?
A. error-message가 좋다. 에러라는 의미가 유지되고 색상 변경에도 안전하다.

---

# 2. BEM Rules

## 2.1 BEM Definition

### [개념]

BEM은 Block, Element, Modifier를 기준으로 class 이름을 작성하는 방식이다.

BEM 형식:

```text
block
block__element
block--modifier
```

BEM은 Plain CSS나 SCSS에서 전역 class 충돌을 줄이고 구조를 명확히 하는 데 유용하다.

---

### [핵심]

BEM 구성:

- Block: 독립적인 UI 단위
- Element: Block 내부 요소
- Modifier: Block 또는 Element의 변형 상태

예:

```text
festival-card
→ Block

festival-card__title
→ Element

festival-card--featured
→ Modifier
```

BEM 장점:

- class 역할 명확
- 전역 CSS 충돌 감소
- 구조 파악 쉬움
- modifier로 상태 표현 가능
- Agent Retrieval에 유리

BEM 단점:

- 이름이 길어질 수 있음
- CSS Module 사용 시 필요성이 줄어들 수 있음
- 팀 규칙 없으면 어색할 수 있음

---

### [실무]

BEM 예:

```html
<article class="festival-card festival-card--featured">
  <h2 class="festival-card__title">Festival Title</h2>
  <p class="festival-card__description">Description</p>
</article>
```

```css
.festival-card {
  padding: var(--spacing-4);
}

.festival-card__title {
  font-size: var(--font-size-lg);
}

.festival-card__description {
  color: var(--color-muted);
}

.festival-card--featured {
  border-color: var(--color-primary);
}
```

BEM 리뷰 기준:

```md
- [ ] block 이름이 독립 UI 단위를 표현하는가?
- [ ] element가 block 내부 요소로 표현되는가?
- [ ] modifier가 변형 또는 상태를 표현하는가?
- [ ] class 이름이 과하게 복잡하지 않은가?
- [ ] 프로젝트 전체에서 BEM 사용 여부가 일관적인가?
```

---

### [FAQ]

Q. BEM은 꼭 써야 해?
A. 필수는 아니다. Plain CSS나 SCSS에서 전역 충돌을 줄이고 구조를 명확히 할 때 유용하다.

Q. CSS Module을 쓰면 BEM이 필요 없어?
A. 필수는 아니지만 class 의미를 명확히 하기 위해 일부 패턴을 사용할 수 있다.

Q. BEM 이름이 너무 길면 문제야?
A. 길어질 수 있다. 다만 의미가 명확하면 유지보수에는 도움이 된다.

---

## 2.2 BEM Modifier Rules

### [개념]

BEM Modifier는 Block 또는 Element의 변형 상태를 표현한다.

Modifier는 시각 속성보다 역할, 상태, 크기, 의미를 기준으로 작성한다.

---

### [핵심]

Modifier 적합 대상:

- variant
- size
- status
- selected
- featured
- disabled-like visual state
- open / closed state

좋은 modifier:

```css
.button--primary {
}

.button--secondary {
}

.button--danger {
}

.button--large {
}

.festival-card--featured {
}
```

나쁜 modifier:

```css
.button--blue {
}

.button--red {
}

.card--margin-20 {
}

.box--big {
}
```

---

### [실무]

Modifier 사용 예:

```html
<button class="button button--primary button--large">저장</button>
```

```css
.button {
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-medium);
}

.button--primary {
  background: var(--color-primary);
  color: white;
}

.button--danger {
  background: var(--color-error);
  color: white;
}

.button--large {
  padding: var(--spacing-3) var(--spacing-5);
}
```

Modifier 리뷰 기준:

```md
- [ ] modifier가 역할 기반인가?
- [ ] variant와 size가 분리되어 있는가?
- [ ] 상태와 variant가 혼동되지 않는가?
- [ ] 색상 이름 기반 modifier를 남용하지 않는가?
```

---

### [FAQ]

Q. modifier 이름을 blue, red로 해도 돼?
A. 권장하지 않는다. primary, danger, success처럼 역할 중심 이름이 좋다.

Q. size modifier와 variant modifier를 같이 써도 돼?
A. 가능하다. `button--primary button--large`처럼 역할과 크기를 분리하는 것이 좋다.

Q. disabled도 modifier야?
A. 시각 표현에는 modifier를 쓸 수 있지만 실제 disabled 상태는 HTML disabled attribute와 함께 처리하는 것이 좋다.

---

# 3. State Class Naming Rules

## 3.1 State Class Naming

### [개념]

State Class Naming은 active, disabled, selected, open, error 같은 UI 상태를 class로 표현하는 방식이다.

State Class는 사용자의 상호작용이나 데이터 상태에 따라 UI가 달라지는 경우 사용한다.

---

### [핵심]

권장 state naming:

```text
is-active
is-disabled
is-selected
is-open
is-loading
has-error
has-value
has-icon
```

또는 component modifier:

```text
button--disabled
tab--active
input--error
modal--open
```

상태 class 기준:

- `is-*`: 현재 상태
- `has-*`: 특정 요소나 조건을 가지고 있음
- `aria-*`: 접근성 상태와 연결 가능
- attribute selector와 병행 가능

---

### [실무]

State Class 예:

```css
.tab {
  color: var(--color-muted);
}

.tab.is-active {
  color: var(--color-primary);
  font-weight: var(--font-weight-bold);
}
```

React 조건부 class 예:

```jsx
<button className={`tab ${isActive ? "is-active" : ""}`} type="button">
  메뉴
</button>
```

상태 class 리뷰 기준:

```md
- [ ] 상태 이름이 명확한가?
- [ ] active, selected, open의 의미가 혼동되지 않는가?
- [ ] disabled 상태가 attribute와 함께 관리되는가?
- [ ] error 상태가 색상만으로 표현되지 않는가?
- [ ] loading 상태가 사용 흐름과 연결되는가?
```

---

### [FAQ]

Q. 상태 class는 어떻게 이름 짓는 게 좋아?
A. `is-active`, `has-error`, `is-loading`처럼 상태 의미가 명확하게 드러나게 작성한다.

Q. 상태를 inline style로 처리해도 돼?
A. 간단한 경우는 가능하지만 반복되는 상태 스타일은 class로 관리하는 것이 좋다.

Q. active와 selected는 같은 뜻이야?
A. 비슷하게 쓰일 수 있지만 active는 현재 활성 상태, selected는 선택된 상태를 의미하는 경우가 많다.

---

## 3.2 Attribute State Styling

### [개념]

Attribute State Styling은 HTML attribute나 ARIA attribute를 사용해 상태 스타일을 적용하는 방식이다.

상태를 class로만 관리하지 않고 실제 semantic attribute와 연결하면 접근성과 유지보수성이 좋아진다.

---

### [핵심]

사용 가능한 attribute:

- `disabled`
- `aria-selected`
- `aria-expanded`
- `aria-invalid`
- `aria-current`
- `data-state`
- `data-variant`
- `data-size`

예:

```css
button:disabled {
}

[aria-selected="true"] {
}

[data-state="open"] {
}
```

장점:

- 상태와 의미가 연결됨
- 접근성 상태와 스타일 일치
- JS 상태와 DOM 상태 추적 쉬움
- Headless UI / Radix UI 같은 라이브러리와 호환 좋음

---

### [실무]

Attribute styling 예:

```css
.tab[aria-selected="true"] {
  color: var(--color-primary);
  font-weight: var(--font-weight-bold);
}

.accordion-trigger[aria-expanded="true"] {
  background: var(--color-surface);
}

.input[aria-invalid="true"] {
  border-color: var(--color-error);
}
```

React 예:

```jsx
<button type="button" className="tab" aria-selected={isSelected}>
  탭
</button>
```

리뷰 기준:

```md
- [ ] 상태 class와 attribute가 충돌하지 않는가?
- [ ] aria 상태가 실제 UI 상태와 일치하는가?
- [ ] disabled는 class뿐 아니라 attribute로도 처리되는가?
- [ ] error 상태는 aria-invalid와 연결 가능한가?
```

---

### [FAQ]

Q. 상태 class 대신 aria attribute를 써도 돼?
A. 가능하다. 특히 selected, expanded, invalid 같은 상태는 aria attribute와 연결하는 것이 좋다.

Q. disabled는 class만 주면 돼?
A. 아니다. 실제 조작을 막아야 한다면 HTML disabled attribute를 사용해야 한다.

Q. data-state는 언제 사용해?
A. open, closed, checked 같은 컴포넌트 내부 상태를 스타일과 연결할 때 사용할 수 있다.

---

# 4. Component Styling Rules

## 4.1 Component Style Definition

### [개념]

Component Style은 특정 컴포넌트의 UI 구조와 상태에 필요한 스타일이다.

Component Style은 재사용 가능한 UI 단위의 외형, 내부 배치, 상태, variant를 담당한다.

Component Style은 전체 페이지 layout을 담당하지 않는다.

---

### [핵심]

Component Style에 포함할 것:

- 컴포넌트 내부 layout
- component variant
- component size
- hover state
- active state
- focus state
- disabled state
- error state
- child element style
- component-specific responsive
- component state style

Component Style에 포함하지 않을 것:

- 전체 페이지 layout
- 전역 reset
- 전역 typography 기본값
- 다른 컴포넌트 override
- unrelated utility
- page section spacing
- parent layout margin

---

### [실무]

Component Style 예:

```css
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-2);
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-medium);
}

.buttonPrimary {
  background: var(--color-primary);
  color: white;
}

.buttonPrimary:hover {
  background: var(--color-primary-hover);
}

.button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

Component Style 리뷰 기준:

```md
- [ ] 컴포넌트 내부 스타일이 외부 layout에 의존하지 않는가?
- [ ] variant가 명확히 분리되어 있는가?
- [ ] disabled / hover / focus 상태가 있는가?
- [ ] token을 사용하고 있는가?
- [ ] 다른 컴포넌트를 직접 override하지 않는가?
- [ ] 외부 margin을 강제하지 않는가?
```

---

### [FAQ]

Q. Component Style에는 무엇을 넣어야 해?
A. 컴포넌트 내부 layout, variant, hover, focus, disabled, error 같은 컴포넌트 전용 스타일을 넣는다.

Q. Component Style에 넣으면 안 되는 것은?
A. 전체 page layout, global reset, 다른 컴포넌트 override 같은 스타일은 넣지 않는 것이 좋다.

Q. 컴포넌트 스타일에서 margin을 줘도 돼?
A. 컴포넌트 내부 간격은 가능하지만 외부 배치 margin은 부모 layout에서 관리하는 것이 좋다.

---

## 4.2 Component Internal Layout

### [개념]

Component Internal Layout은 컴포넌트 내부 요소의 배치와 간격을 관리하는 스타일이다.

컴포넌트 내부 layout은 컴포넌트가 자체적으로 관리해도 된다.

다만 외부 배치와 페이지 layout은 부모가 담당해야 한다.

---

### [핵심]

Component Internal Layout 대상:

- button icon gap
- card title / description spacing
- input label / field spacing
- modal header / body / footer 내부 배치
- tab 내부 정렬
- badge icon alignment

부모 layout이 담당할 것:

- card list gap
- page section spacing
- grid column
- container width
- sidebar / content 배치
- 페이지 전체 margin

---

### [실무]

좋은 예:

```css
.card {
  padding: var(--spacing-4);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
}

.cardHeader {
  display: flex;
  align-items: center;
  gap: var(--spacing-2);
}

.cardBody {
  margin-top: var(--spacing-3);
}
```

주의할 예:

```css
.card {
  width: 1200px;
  margin: 0 auto 24px;
}
```

Component internal layout 리뷰 기준:

```md
- [ ] 컴포넌트 내부 간격과 외부 배치 간격이 구분되는가?
- [ ] 내부 gap은 token을 사용하는가?
- [ ] 재사용 컴포넌트가 page width를 강제하지 않는가?
- [ ] component root가 부모 layout에 과하게 의존하지 않는가?
```

---

### [FAQ]

Q. Card 내부 title과 description 간격은 어디서 관리해?
A. Card 컴포넌트 스타일에서 관리하는 것이 좋다.

Q. Card 목록 간격은 어디서 관리해?
A. CardList 또는 page layout의 gap으로 관리하는 것이 좋다.

Q. Button 내부 icon과 text 간격은 어디서 관리해?
A. Button 컴포넌트 내부 스타일에서 gap으로 관리하는 것이 좋다.

---

## 4.3 Component External Layout Warning

### [개념]

Component External Layout Warning은 재사용 컴포넌트가 외부 배치를 강제하는 문제를 방지하는 규칙이다.

재사용 컴포넌트가 margin, width, page position을 강제하면 다른 화면에서 재사용하기 어려워진다.

---

### [핵심]

주의해야 할 스타일:

- `margin: 0 auto`
- `margin-bottom`
- `width: 1200px`
- `position: absolute` 남용
- page-specific spacing
- parent container 의존 selector
- 특정 page class에 의존하는 component style

피해야 할 구조:

```css
.card {
  margin-bottom: 24px;
  width: 1200px;
}

.main-page .card {
  margin-left: 32px;
}
```

권장 구조:

```css
.cardGrid {
  display: grid;
  gap: var(--spacing-6);
}

.card {
  padding: var(--spacing-4);
}
```

---

### [실무]

외부 배치 책임 분리:

```text
Page Layout
→ container width
→ section spacing
→ grid / flex layout
→ component list gap

Component Style
→ internal padding
→ internal alignment
→ visual style
→ state style
```

Review Agent 확인:

```md
- [ ] 재사용 컴포넌트가 외부 margin을 강제하지 않는가?
- [ ] component width가 고정되어 있지 않은가?
- [ ] page class selector에 의존하지 않는가?
- [ ] 부모 layout에서 gap을 관리하는가?
```

---

### [FAQ]

Q. 컴포넌트가 자기 margin을 가지면 안 돼?
A. 항상 안 되는 것은 아니지만 재사용 컴포넌트라면 외부 배치는 부모가 담당하는 것이 좋다.

Q. width: 100%는 컴포넌트에 넣어도 돼?
A. 상황에 따라 가능하지만 모든 사용처에 적합한지 확인해야 한다.

Q. 재사용 컴포넌트가 page class를 참조하면 안 돼?
A. 권장하지 않는다. 특정 page 구조에 묶이면 재사용성이 떨어진다.

---

# 5. Layout Style vs Component Style

## 5.1 Layout Style

### [개념]

Layout Style은 요소들을 배치하는 스타일이다.

Layout Style은 페이지나 레이아웃 컴포넌트에서 관리하며, 개별 UI 컴포넌트의 외형과 분리되어야 한다.

---

### [핵심]

Layout Style 대상:

- page container
- section spacing
- grid layout
- flex layout
- sidebar layout
- header layout
- footer layout
- content width
- responsive columns
- list gap

Component Style 대상:

- button visual
- card visual
- input visual
- modal visual
- badge visual
- tab visual
- toast visual

원칙:

```text
부모는 배치 담당
자식은 자기 외형 담당
```

---

### [실무]

Layout Style 예:

```css
.pageLayout {
  width: min(100% - 32px, 1200px);
  margin: 0 auto;
}

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
```

Component Style 예:

```css
.card {
  padding: var(--spacing-4);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background: var(--color-surface);
}
```

---

### [FAQ]

Q. Layout Style과 Component Style 차이는 뭐야?
A. Layout Style은 배치와 공간 구조를 담당하고 Component Style은 개별 UI 요소의 외형과 상태를 담당한다.

Q. layout과 component style을 왜 분리해?
A. 컴포넌트 재사용성과 화면 구조 변경의 유연성을 높이기 위해서다.

Q. page container는 어디서 관리해?
A. page style 또는 layout component에서 관리하는 것이 좋다.

---

## 5.2 Layout Component Pattern

### [개념]

Layout Component Pattern은 반복되는 배치 구조를 별도 layout component나 layout class로 분리하는 방식이다.

반복되는 page spacing, container, grid 구조는 컴포넌트 스타일에 중복 작성하지 않는 것이 좋다.

---

### [핵심]

Layout Component로 분리할 수 있는 것:

- PageContainer
- Section
- Stack
- Grid
- SidebarLayout
- HeaderLayout
- ContentLayout
- FormLayout

분리 기준:

```text
3회 이상 반복
+ 의미가 같음
+ 변경 방향이 같음
+ 재사용 가능성이 있음
→ layout component 또는 utility로 분리 고려
```

---

### [실무]

Layout utility 예:

```css
.container {
  width: min(100% - 32px, 1200px);
  margin: 0 auto;
}

.stack {
  display: grid;
  gap: var(--spacing-4);
}

.cluster {
  display: flex;
  flex-wrap: wrap;
  gap: var(--spacing-3);
}
```

Layout Component 리뷰 기준:

```md
- [ ] 반복되는 layout 구조가 중복 작성되지 않는가?
- [ ] layout component가 visual style까지 과하게 포함하지 않는가?
- [ ] container, stack, grid 역할이 명확한가?
- [ ] component style과 layout utility가 충돌하지 않는가?
```

---

### [FAQ]

Q. Layout Component는 언제 만들어?
A. 같은 배치 구조가 반복되고 의미와 변경 방향이 같을 때 만든다.

Q. container class는 global utility로 둬도 돼?
A. 가능하다. 여러 화면에서 공통으로 쓰는 layout helper라면 utility로 관리할 수 있다.

Q. Stack이나 Grid 같은 layout utility를 직접 만들어도 돼?
A. 가능하다. 다만 프로젝트 전체에서 일관된 규칙이 있어야 한다.

---

# 6. Variant Style Rules

## 6.1 Variant Style

### [개념]

Variant Style은 같은 컴포넌트가 목적이나 상태에 따라 다른 스타일을 갖는 구조다.

Variant는 컴포넌트의 의미 있는 변형이다.

예:

- primary button
- secondary button
- danger button
- outline button
- small button
- large button

---

### [핵심]

Variant 설계 기준:

- 의미 기반 variant 사용
- 색상 이름보다 역할 이름 사용
- size와 intent 분리
- disabled는 variant가 아니라 state로 처리
- variant 조합이 과도하면 구조 재검토
- token 기반 스타일 사용
- variant 이름은 프로젝트 전체에서 일관되게 유지

권장 variant:

```text
primary
secondary
danger
success
warning
outline
ghost
sm
md
lg
```

피해야 할 variant:

```text
blue
red
big
small-red
main-blue
temp
```

---

### [실무]

Variant 사용 예:

```jsx
<Button variant="primary" size="md">
  저장
</Button>

<Button variant="danger" size="sm">
  삭제
</Button>
```

CSS Module 예:

```css
.button {
  border-radius: var(--radius-md);
}

.primary {
  background: var(--color-primary);
  color: white;
}

.danger {
  background: var(--color-error);
  color: white;
}

.sm {
  padding: var(--spacing-1) var(--spacing-3);
}

.md {
  padding: var(--spacing-2) var(--spacing-4);
}
```

Review 기준:

```md
- [ ] variant 이름이 역할 기반인가?
- [ ] size와 intent가 분리되어 있는가?
- [ ] disabled를 variant로 오해하지 않는가?
- [ ] token을 사용하고 있는가?
- [ ] variant 조합이 과도하게 많지 않은가?
```

---

### [FAQ]

Q. Variant Style은 뭐야?
A. 같은 컴포넌트가 primary, secondary, danger, small, large처럼 목적이나 크기에 따라 다른 스타일을 갖는 구조다.

Q. variant 이름을 blue, red로 해도 돼?
A. 권장하지 않는다. 색상보다 primary, danger, secondary처럼 역할 중심 이름이 좋다.

Q. disabled도 variant야?
A. 보통은 variant가 아니라 상태다. disabled attribute와 disabled style로 처리한다.

---

## 6.2 Intent Variant vs Size Variant

### [개념]

Intent Variant는 컴포넌트의 의미나 목적을 표현한다.

Size Variant는 컴포넌트의 크기를 표현한다.

두 개념을 섞으면 variant 조합이 폭발하고 유지보수가 어려워진다.

---

### [핵심]

Intent Variant 예:

- primary
- secondary
- danger
- success
- warning
- info
- ghost
- outline

Size Variant 예:

- xs
- sm
- md
- lg
- xl

나쁜 조합:

```text
primaryLarge
primarySmall
dangerLarge
dangerSmall
blueBig
redSmall
```

좋은 조합:

```text
variant="primary" size="lg"
variant="danger" size="sm"
variant="outline" size="md"
```

---

### [실무]

React props 구조 예:

```jsx
function Button({
  variant = "primary",
  size = "md",
  disabled = false,
  children,
}) {
  return (
    <button type="button" disabled={disabled}>
      {children}
    </button>
  );
}
```

CSS Module 구조 예:

```css
.button {
  display: inline-flex;
  align-items: center;
}

.primary {
  background: var(--color-primary);
}

.secondary {
  background: var(--color-surface);
}

.sm {
  padding: var(--spacing-1) var(--spacing-3);
}

.lg {
  padding: var(--spacing-3) var(--spacing-5);
}
```

---

### [FAQ]

Q. intent와 size를 왜 분리해?
A. 의미와 크기를 분리하면 variant 조합이 줄고 유지보수가 쉬워진다.

Q. primaryLarge 같은 class는 안 좋아?
A. 조합이 늘어날수록 class가 폭발할 수 있다. primary와 large를 분리하는 것이 좋다.

Q. size variant도 token을 써야 해?
A. 권장된다. padding, font-size, gap을 spacing과 typography token으로 관리하는 것이 좋다.

---

## 6.3 Variant Explosion Warning

### [개념]

Variant Explosion은 하나의 컴포넌트에 너무 많은 variant와 조건이 추가되어 유지보수가 어려워지는 문제다.

Variant Explosion은 공통 컴포넌트를 과하게 일반화할 때 자주 발생한다.

---

### [핵심]

Variant Explosion 징후:

- props가 너무 많음
- variant 조합이 과도함
- 조건부 class가 너무 복잡함
- 작은 차이 때문에 조건문이 많음
- 하나의 컴포넌트가 서로 다른 UI를 억지로 처리함
- 공통 컴포넌트 수정 시 영향 범위가 너무 큼

예:

```text
Button props:
variant
size
shape
tone
filled
outline
ghost
iconOnly
loading
danger
active
selected
mobileFull
```

---

### [실무]

해결 기준:

```text
variant 수 증가
→ intent / size / state 분리

조건문 증가
→ variant mapping 도입

서로 다른 UI 처리
→ 컴포넌트 분리

props 의미 충돌
→ API 재설계

영향 범위 과다
→ specialized component 분리
```

Review Agent 확인:

```md
- [ ] variant와 state가 분리되어 있는가?
- [ ] props가 과도하게 많지 않은가?
- [ ] 조건부 class 조합이 읽기 쉬운가?
- [ ] 실제로 다른 UI를 하나로 억지 통합하지 않았는가?
```

---

### [FAQ]

Q. variant가 많아지면 어떻게 해?
A. intent, size, state를 분리하고 필요하면 컴포넌트를 나누는 것이 좋다.

Q. 공통 컴포넌트는 모든 경우를 처리해야 해?
A. 아니다. 모든 경우를 처리하려 하면 오히려 복잡해질 수 있다.

Q. 조건부 class가 길어지면 어떻게 해?
A. variant mapping, clsx, helper 함수, 컴포넌트 분리를 고려한다.

---

# 7. Component State Style Rules

## 7.1 Interaction State Style

### [개념]

Interaction State Style은 사용자의 상호작용이나 컴포넌트 상태에 따라 달라지는 스타일이다.

상태 스타일은 사용자에게 현재 UI가 어떤 상태인지 알려준다.

---

### [핵심]

반드시 검토할 상태:

```md
- [ ] button hover
- [ ] button active
- [ ] button disabled
- [ ] button loading
- [ ] input focus
- [ ] input error
- [ ] input disabled
- [ ] link hover
- [ ] selected tab
- [ ] active menu
- [ ] modal open
```

상태 예:

- hover
- active
- focus
- disabled
- selected
- loading
- error
- success
- open
- checked

---

### [실무]

State Style 예:

```css
.button {
  background: var(--color-primary);
}

.button:hover {
  background: var(--color-primary-hover);
}

.button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.input:focus {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.inputError {
  border-color: var(--color-error);
}
```

State Style 리뷰 기준:

```md
- [ ] hover만 있고 focus가 누락되지 않았는가?
- [ ] disabled 상태가 명확한가?
- [ ] error 상태가 색상만으로 전달되지 않는가?
- [ ] loading 상태에서 중복 클릭을 방지하는가?
- [ ] selected / active 상태가 시각적으로 구분되는가?
```

---

### [FAQ]

Q. hover만 있으면 충분해?
A. 아니다. keyboard 사용자를 위해 focus style도 필요하고, disabled / active / error 상태도 고려해야 한다.

Q. disabled 스타일은 왜 필요해?
A. 사용자가 조작 불가능한 상태를 시각적으로 이해해야 하기 때문이다.

Q. loading 상태도 스타일이 필요해?
A. 필요하다. 사용자가 요청 처리 중임을 알 수 있어야 하고 중복 클릭을 방지해야 한다.

---

## 7.2 Disabled State Rules

### [개념]

Disabled State는 사용자가 특정 UI를 조작할 수 없는 상태다.

Disabled는 단순히 회색으로 보이게 하는 것이 아니라 실제 조작 불가능 상태와 연결되어야 한다.

---

### [핵심]

Disabled 처리 기준:

- button은 `disabled` attribute 사용
- input은 `disabled` 또는 `readOnly` 구분
- disabled style 제공
- cursor 처리
- opacity만으로 의미 전달하지 않음
- disabled 이유가 필요한 경우 helper text 제공
- keyboard focus 가능 여부 검토

---

### [실무]

Disabled 예:

```css
.button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.input:disabled {
  background: var(--color-surface);
  color: var(--color-muted);
}
```

React 예:

```jsx
<button type="button" disabled={isSubmitting}>
  저장
</button>
```

Review 기준:

```md
- [ ] disabled class만 쓰지 않고 attribute를 사용하는가?
- [ ] disabled 상태가 시각적으로 구분되는가?
- [ ] disabled 이유가 사용자에게 필요한 경우 설명되는가?
- [ ] disabled와 loading 상태가 충돌하지 않는가?
```

---

### [FAQ]

Q. disabled는 class만 주면 돼?
A. 아니다. 실제 조작을 막아야 한다면 HTML disabled attribute를 사용해야 한다.

Q. disabled 상태는 opacity만 낮추면 돼?
A. 부족할 수 있다. cursor, 배경, 텍스트 색상, 안내 메시지도 고려해야 한다.

Q. readOnly와 disabled는 같아?
A. 아니다. readOnly는 값 수정만 막고 focus와 제출 동작은 다를 수 있다.

---

## 7.3 Error State Rules

### [개념]

Error State는 입력값 오류, 요청 실패, 검증 실패 같은 문제 상태를 사용자에게 전달하는 스타일이다.

Error State는 색상만으로 전달하면 안 된다.

---

### [핵심]

Error State 기준:

- error color token 사용
- error message 제공
- aria-invalid 고려
- input border / text / icon 조합 가능
- 색상만으로 상태 전달 금지
- 에러 위치가 입력 요소와 연결되어야 함
- form validation message와 일관성 유지

---

### [실무]

Error Style 예:

```css
.input[aria-invalid="true"] {
  border-color: var(--color-error);
}

.errorMessage {
  margin-top: var(--spacing-1);
  color: var(--color-error);
  font-size: var(--font-size-sm);
}
```

React 예:

```jsx
<input
  className={styles.input}
  aria-invalid={Boolean(error)}
  aria-describedby={error ? "email-error" : undefined}
/>;

{
  error && (
    <p id="email-error" className={styles.errorMessage}>
      이메일 형식이 올바르지 않습니다.
    </p>
  );
}
```

Review 기준:

```md
- [ ] error color token을 사용하는가?
- [ ] 에러 메시지가 제공되는가?
- [ ] aria-invalid 또는 aria-describedby를 고려하는가?
- [ ] 색상만으로 에러를 전달하지 않는가?
```

---

### [FAQ]

Q. 에러를 빨간색으로만 표시하면 안 돼?
A. 안 된다. 텍스트 메시지, 아이콘, aria 등 추가 정보가 필요하다.

Q. error color는 직접 red를 쓰면 돼?
A. 가능하지만 `--color-error` 같은 token을 사용하는 것이 좋다.

Q. input error와 error message는 연결해야 해?
A. 권장된다. aria-describedby로 연결하면 접근성에 좋다.

---

# 8. Component Styling File Structure

## 8.1 Component File Structure

### [개념]

Component File Structure는 컴포넌트 코드와 스타일 파일을 어디에 배치할지 정하는 규칙이다.

컴포넌트 전용 스타일은 컴포넌트와 가까운 위치에 두는 것이 유지보수에 좋다.

---

### [핵심]

CSS Module 권장 구조:

```text
src/
└─ components/
   └─ Button/
      ├─ Button.jsx
      ├─ Button.module.css
      └─ index.js
```

Plain CSS 권장 구조:

```text
src/
├─ styles/
│  ├─ reset.css
│  ├─ tokens.css
│  └─ globals.css
└─ components/
   └─ Button/
      ├─ Button.jsx
      └─ Button.css
```

Page style 구조:

```text
src/
└─ pages/
   └─ MainPage/
      ├─ MainPage.jsx
      └─ MainPage.module.css
```

---

### [실무]

구조 판단 기준:

```md
- [ ] 컴포넌트 전용 스타일이 컴포넌트와 가까이 있는가?
- [ ] 페이지 레이아웃 스타일이 page 단위로 분리되어 있는가?
- [ ] global style과 component style이 섞이지 않았는가?
- [ ] token은 전역 styles 폴더에서 관리되는가?
- [ ] index.js 사용 여부가 프로젝트 기준과 일치하는가?
```

Agent 파일 생성 Flow:

```text
Component 생성 요청
→ 기존 프로젝트 구조 확인
→ CSS Module / Plain CSS 여부 확인
→ Component 파일 위치 결정
→ Style 파일 위치 결정
→ Import 방식 적용
→ Review Checklist 수행
```

---

### [FAQ]

Q. 스타일 파일은 컴포넌트 옆에 두는 게 좋아?
A. 컴포넌트 전용 스타일이라면 가까이 두는 것이 유지보수에 좋다.

Q. 모든 CSS를 styles 폴더에 모아도 돼?
A. 가능하지만 컴포넌트가 많아지면 어떤 스타일이 어디에 쓰이는지 추적하기 어려울 수 있다.

Q. Page 스타일과 Component 스타일은 나눠야 해?
A. 권장된다. page는 layout, component는 개별 UI 외형과 상태를 담당하는 것이 좋다.

---

# 9. Agent Naming and Component Styling Rules

## 9.1 Frontend Agent Rules

### [개념]

Frontend Agent는 컴포넌트 스타일을 생성할 때 Naming Convention, Component Styling, Variant Rules를 따라야 한다.

Frontend Agent는 기존 프로젝트의 naming pattern과 file structure를 우선 확인해야 한다.

---

### [핵심]

Frontend Agent 생성 규칙:

- 기존 naming convention 확인
- 기존 Styling Method 확인
- component style과 layout style 분리
- role-based naming 사용
- token 기반 스타일 작성
- variant와 state 분리
- disabled / hover / focus / error 상태 포함
- 외부 margin 강제 지양
- class 이름 모호하게 작성 금지

---

### [실무]

Frontend Agent 작업 Flow:

```text
Component Styling Request
→ Existing Naming Pattern 확인
→ Styling Method 확인
→ Component / Layout 책임 분리
→ Variant / State 정의
→ Token 적용
→ File Structure 적용
→ Responsive / Accessibility 확인
→ Review Agent 전달
```

생성 금지에 가까운 예:

```text
.box, .red, .big 같은 모호한 class 생성
raw color 반복
button disabled를 class만으로 처리
global style에 특정 component style 추가
재사용 component에 margin-bottom 강제
variant 이름을 blue, red로 작성
```

---

### [FAQ]

Q. Frontend Agent가 class 이름을 임의로 만들어도 돼?
A. 기존 naming convention을 확인한 뒤 역할 기반 이름으로 작성해야 한다.

Q. Frontend Agent가 Button variant를 blue로 만들어도 돼?
A. 권장하지 않는다. primary, secondary, danger처럼 역할 기반 variant가 좋다.

Q. Frontend Agent가 global.css에 컴포넌트 스타일을 넣어도 돼?
A. 권장하지 않는다. 컴포넌트 전용 스타일은 컴포넌트 스타일 파일에 작성해야 한다.

---

## 9.2 Review Agent Rules

### [개념]

Review Agent는 Naming Convention, Component Styling, Variant Style, State Style이 프로젝트 기준과 일치하는지 검토한다.

Review Agent는 스타일이 보이는 결과뿐 아니라 구조적 안정성도 확인해야 한다.

---

### [핵심]

Review Agent 검토 항목:

- class naming 명확성
- role-based naming 사용 여부
- BEM / CSS Module naming 일관성
- state class 명확성
- attribute state styling 여부
- component style과 layout style 분리
- variant와 size 분리
- disabled / error / focus 상태 처리
- 외부 margin 강제 여부
- token 사용 여부

---

### [실무]

Review Agent 판단 Flow:

```text
Class Naming 확인
→ Role-based Naming 확인
→ Component / Layout 분리 확인
→ Variant / Size / State 분리 확인
→ Token 사용 확인
→ Interaction State 확인
→ Accessibility State 확인
→ File Structure 확인
→ Final Review
```

Review 결과 기준:

```text
Approved
→ naming 명확 + token 사용 + variant/state 분리 + 접근성 상태 포함

Needs Fix
→ 일부 class 이름 모호, focus 누락, raw value 반복

Rejected
→ global 오염, variant/state 혼동, disabled attribute 누락, page layout 강제
```

---

### [FAQ]

Q. Review Agent가 class 이름도 봐야 해?
A. 봐야 한다. class 이름은 유지보수성과 Retrieval 품질에 영향을 준다.

Q. 화면상 문제없으면 naming은 넘어가도 돼?
A. 아니다. 모호한 naming은 이후 유지보수와 Agent 검색 품질을 떨어뜨린다.

Q. Review Agent가 가장 먼저 볼 것은 뭐야?
A. 기존 프로젝트 naming convention과 component/layout 책임 분리가 지켜졌는지 확인해야 한다.

---

# 10. Part04 Quality Checklist

## 10.1 Naming and Component Styling Checklist

### [개념]

Part04 단계에서는 Naming Convention, Component Styling, Variant Rules, State Style 기준이 명확한지 검토한다.

이 단계는 실제 컴포넌트 스타일 코드의 일관성과 유지보수성을 결정한다.

---

### [핵심]

Part04 체크리스트:

```md
## Naming

- [ ] class naming 기준이 명확한가?
- [ ] role-based naming 원칙이 있는가?
- [ ] 색상 / 크기 기반 naming을 경고하는가?
- [ ] BEM 기준이 포함되어 있는가?
- [ ] state class naming 기준이 있는가?

## Component Styling

- [ ] component style의 책임이 명확한가?
- [ ] component style과 layout style이 분리되어 있는가?
- [ ] component internal layout 기준이 있는가?
- [ ] component external layout warning이 있는가?
- [ ] file structure 기준이 있는가?

## Variant

- [ ] variant style 기준이 명확한가?
- [ ] intent variant와 size variant가 분리되어 있는가?
- [ ] disabled가 state라는 기준이 있는가?
- [ ] variant explosion warning이 있는가?

## State

- [ ] hover / focus / disabled / error 상태 기준이 있는가?
- [ ] disabled attribute 기준이 있는가?
- [ ] error state accessibility 기준이 있는가?
- [ ] attribute state styling 기준이 있는가?

## Agent Review

- [ ] Frontend Agent 생성 규칙이 있는가?
- [ ] Review Agent 검토 규칙이 있는가?
- [ ] Retrieval Queries가 충분한가?
```

---

### [실무]

Part04 승인 기준:

```text
Naming 기준 명확
+ Component / Layout 분리 명확
+ Variant / State 분리 명확
+ Accessibility State 포함
+ Agent 생성 / 검토 기준 포함
+ FAQ 충분
+ Retrieval Queries 포함
→ Part04 승인 가능
```

Part04 보류 기준:

```text
class naming 모호
또는 색상 기반 variant 권장
또는 component가 page layout 강제
또는 disabled를 class만으로 처리
또는 error를 색상만으로 처리
또는 Agent 검토 기준 부족
→ 재작성 필요
```

---

### [FAQ]

Q. Part04의 핵심 목적은 뭐야?
A. 컴포넌트 스타일 코드의 naming, variant, state, layout 책임 분리 기준을 고정하는 것이다.

Q. Part04에서 가장 위험한 문제는 뭐야?
A. 모호한 class 이름, 색상 기반 variant, component와 layout 책임 혼합, 접근성 상태 누락이다.

Q. Part04 다음에는 뭘 다루는 게 자연스러워?
A. Responsive Styling, Breakpoint, Mobile First, Theme, Dark Mode 구조를 다루는 것이 자연스럽다.

---

# Retrieval Queries

### [FAQ]

Q. Class Naming은 뭐야?
A. CSS class 이름을 일관되게 작성해 스타일 역할, 적용 범위, 컴포넌트 구조, 상태를 명확히 하는 규칙이다.

Q. 좋은 class name 기준은 뭐야?
A. 역할과 의미가 드러나고, 컴포넌트 단위 prefix를 사용하며, 모호하지 않고 재사용 범위가 명확해야 한다.

Q. class 이름은 짧을수록 좋아?
A. 아니다. 의미가 명확한 이름이 더 중요하다.

Q. blue-button 같은 이름은 안 좋아?
A. 색상이 바뀌면 이름과 실제 스타일이 어긋날 수 있다. primary-button 같은 의미 기반 이름이 좋다.

Q. Role-based Naming은 뭐야?
A. 색상, 크기, 위치보다 UI 역할과 의미를 기준으로 class 이름을 짓는 방식이다.

Q. red-text와 error-message 중 뭐가 좋아?
A. error-message가 좋다. 에러라는 의미가 유지되고 색상 변경에도 안전하다.

Q. primary와 blue는 뭐가 달라?
A. primary는 UI 역할이고 blue는 색상값이다. 컴포넌트 이름에는 역할 기반 이름이 더 좋다.

Q. BEM은 뭐야?
A. Block, Element, Modifier를 기준으로 `block`, `block__element`, `block--modifier` 형태로 class 이름을 작성하는 방식이다.

Q. BEM은 꼭 써야 해?
A. 필수는 아니다. Plain CSS나 SCSS에서 전역 충돌을 줄이고 구조를 명확히 할 때 유용하다.

Q. CSS Module을 쓰면 BEM이 필요 없어?
A. 필수는 아니지만 class 의미를 명확히 하기 위해 일부 패턴을 사용할 수 있다.

Q. BEM Modifier는 뭐야?
A. Block 또는 Element의 변형 상태를 표현하는 class 이름이다.

Q. modifier 이름을 blue, red로 해도 돼?
A. 권장하지 않는다. primary, danger, success처럼 역할 중심 이름이 좋다.

Q. size modifier와 variant modifier를 같이 써도 돼?
A. 가능하다. `button--primary button--large`처럼 역할과 크기를 분리하는 것이 좋다.

Q. State Class Naming은 뭐야?
A. active, disabled, selected, open, error 같은 UI 상태를 class로 표현하는 방식이다.

Q. 상태 class는 어떻게 이름 짓는 게 좋아?
A. `is-active`, `has-error`, `is-loading`처럼 상태 의미가 명확하게 드러나게 작성한다.

Q. active와 selected는 같은 뜻이야?
A. 비슷하게 쓰일 수 있지만 active는 현재 활성 상태, selected는 선택된 상태를 의미하는 경우가 많다.

Q. Attribute State Styling은 뭐야?
A. HTML attribute나 ARIA attribute를 사용해 상태 스타일을 적용하는 방식이다.

Q. 상태 class 대신 aria attribute를 써도 돼?
A. 가능하다. 특히 selected, expanded, invalid 같은 상태는 aria attribute와 연결하는 것이 좋다.

Q. disabled는 class만 주면 돼?
A. 아니다. 실제 조작을 막아야 한다면 HTML disabled attribute를 사용해야 한다.

Q. data-state는 언제 사용해?
A. open, closed, checked 같은 컴포넌트 내부 상태를 스타일과 연결할 때 사용할 수 있다.

Q. Component Style은 뭐야?
A. 특정 컴포넌트의 UI 구조, 외형, 내부 배치, 상태, variant에 필요한 스타일이다.

Q. Component Style에는 무엇을 넣어야 해?
A. 컴포넌트 내부 layout, variant, hover, focus, disabled, error 같은 컴포넌트 전용 스타일을 넣는다.

Q. Component Style에 넣으면 안 되는 것은?
A. 전체 page layout, global reset, 다른 컴포넌트 override 같은 스타일은 넣지 않는 것이 좋다.

Q. 컴포넌트 스타일에서 margin을 줘도 돼?
A. 컴포넌트 내부 간격은 가능하지만 외부 배치 margin은 부모 layout에서 관리하는 것이 좋다.

Q. Component Internal Layout은 뭐야?
A. 컴포넌트 내부 요소의 배치와 간격을 관리하는 스타일이다.

Q. Card 내부 title과 description 간격은 어디서 관리해?
A. Card 컴포넌트 스타일에서 관리하는 것이 좋다.

Q. Card 목록 간격은 어디서 관리해?
A. CardList 또는 page layout의 gap으로 관리하는 것이 좋다.

Q. Button 내부 icon과 text 간격은 어디서 관리해?
A. Button 컴포넌트 내부 스타일에서 gap으로 관리하는 것이 좋다.

Q. Component External Layout Warning은 뭐야?
A. 재사용 컴포넌트가 외부 배치 margin, width, page position을 강제하지 않도록 하는 규칙이다.

Q. 재사용 컴포넌트가 margin-bottom을 가져도 돼?
A. 권장하지 않는다. 목록 간격은 부모 layout의 gap으로 관리하는 것이 좋다.

Q. 재사용 컴포넌트가 page class를 참조하면 안 돼?
A. 권장하지 않는다. 특정 page 구조에 묶이면 재사용성이 떨어진다.

Q. Layout Style은 뭐야?
A. 페이지나 레이아웃 컴포넌트에서 요소들을 배치하는 스타일이다.

Q. Layout Style과 Component Style 차이는 뭐야?
A. Layout Style은 배치와 공간 구조를 담당하고 Component Style은 개별 UI 요소의 외형과 상태를 담당한다.

Q. 부모와 자식 스타일 책임 원칙은 뭐야?
A. 부모는 배치를 담당하고 자식은 자기 외형을 담당하는 것이다.

Q. page container는 어디서 관리해?
A. page style 또는 layout component에서 관리하는 것이 좋다.

Q. Layout Component Pattern은 뭐야?
A. 반복되는 배치 구조를 별도 layout component나 layout class로 분리하는 방식이다.

Q. Layout Component는 언제 만들어?
A. 같은 배치 구조가 반복되고 의미와 변경 방향이 같을 때 만든다.

Q. container class는 global utility로 둬도 돼?
A. 가능하다. 여러 화면에서 공통으로 쓰는 layout helper라면 utility로 관리할 수 있다.

Q. Variant Style은 뭐야?
A. 같은 컴포넌트가 primary, secondary, danger, small, large처럼 목적이나 크기에 따라 다른 스타일을 갖는 구조다.

Q. variant 이름을 blue, red로 해도 돼?
A. 권장하지 않는다. 색상보다 primary, danger, secondary처럼 역할 중심 이름이 좋다.

Q. disabled도 variant야?
A. 보통은 variant가 아니라 상태다. disabled attribute와 disabled style로 처리한다.

Q. Intent Variant는 뭐야?
A. primary, secondary, danger처럼 컴포넌트의 의미나 목적을 표현하는 variant다.

Q. Size Variant는 뭐야?
A. sm, md, lg처럼 컴포넌트의 크기를 표현하는 variant다.

Q. intent와 size를 왜 분리해?
A. 의미와 크기를 분리하면 variant 조합이 줄고 유지보수가 쉬워진다.

Q. primaryLarge 같은 class는 안 좋아?
A. 조합이 늘어날수록 class가 폭발할 수 있다. primary와 large를 분리하는 것이 좋다.

Q. Variant Explosion은 뭐야?
A. 하나의 컴포넌트에 너무 많은 variant와 조건이 추가되어 유지보수가 어려워지는 문제다.

Q. variant가 많아지면 어떻게 해?
A. intent, size, state를 분리하고 필요하면 컴포넌트를 나누는 것이 좋다.

Q. 공통 컴포넌트는 모든 경우를 처리해야 해?
A. 아니다. 모든 경우를 처리하려 하면 오히려 복잡해질 수 있다.

Q. 조건부 class가 길어지면 어떻게 해?
A. variant mapping, clsx, helper 함수, 컴포넌트 분리를 고려한다.

Q. Interaction State Style은 뭐야?
A. 사용자의 상호작용이나 컴포넌트 상태에 따라 달라지는 스타일이다.

Q. hover만 있으면 충분해?
A. 아니다. keyboard 사용자를 위해 focus style도 필요하고 disabled, active, error 상태도 고려해야 한다.

Q. disabled 스타일은 왜 필요해?
A. 사용자가 조작 불가능한 상태를 시각적으로 이해해야 하기 때문이다.

Q. loading 상태도 스타일이 필요해?
A. 필요하다. 사용자가 요청 처리 중임을 알 수 있어야 하고 중복 클릭을 방지해야 한다.

Q. Disabled State는 어떻게 처리해?
A. button은 disabled attribute를 사용하고, 시각적으로 구분되는 disabled style을 제공해야 한다.

Q. readOnly와 disabled는 같아?
A. 아니다. readOnly는 값 수정만 막고 focus와 제출 동작은 다를 수 있다.

Q. Error State는 뭐야?
A. 입력값 오류, 요청 실패, 검증 실패 같은 문제 상태를 사용자에게 전달하는 스타일이다.

Q. 에러를 빨간색으로만 표시하면 안 돼?
A. 안 된다. 텍스트 메시지, 아이콘, aria 등 추가 정보가 필요하다.

Q. input error와 error message는 연결해야 해?
A. 권장된다. aria-describedby로 연결하면 접근성에 좋다.

Q. Component File Structure는 어떻게 하는 게 좋아?
A. 컴포넌트 전용 스타일은 컴포넌트와 가까이 두고, 페이지 스타일은 page 폴더에 분리하는 것이 좋다.

Q. 모든 CSS를 styles 폴더에 모아도 돼?
A. 가능하지만 컴포넌트가 많아지면 어떤 스타일이 어디에 쓰이는지 추적하기 어려울 수 있다.

Q. Frontend Agent는 class 이름을 어떻게 만들어야 해?
A. 기존 naming convention을 확인한 뒤 역할 기반 이름으로 작성해야 한다.

Q. Frontend Agent가 Button variant를 blue로 만들어도 돼?
A. 권장하지 않는다. primary, secondary, danger처럼 역할 기반 variant가 좋다.

Q. Frontend Agent가 global.css에 컴포넌트 스타일을 넣어도 돼?
A. 권장하지 않는다. 컴포넌트 전용 스타일은 컴포넌트 스타일 파일에 작성해야 한다.

Q. Review Agent가 class 이름도 봐야 해?
A. 봐야 한다. class 이름은 유지보수성과 Retrieval 품질에 영향을 준다.

Q. 화면상 문제없으면 naming은 넘어가도 돼?
A. 아니다. 모호한 naming은 이후 유지보수와 Agent 검색 품질을 떨어뜨린다.

Q. Part04의 핵심 목적은 뭐야?
A. 컴포넌트 스타일 코드의 naming, variant, state, layout 책임 분리 기준을 고정하는 것이다.

Q. Part04에서 가장 위험한 문제는 뭐야?
A. 모호한 class 이름, 색상 기반 variant, component와 layout 책임 혼합, 접근성 상태 누락이다.

Q. Part04 다음에는 뭘 다루는 게 자연스러워?
A. Responsive Styling, Breakpoint, Mobile First, Theme, Dark Mode 구조를 다루는 것이 자연스럽다.
