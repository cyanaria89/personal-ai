# HTML CSS Foundation Part05 - CSS Syntax Selector Cascade

---

# 1. CSS Syntax

## 1.1 CSS Syntax Concept

### [개념]

CSS Syntax는 HTML 요소에 style을 적용하기 위한 CSS 작성 문법이다.

CSS는 selector로 대상 요소를 선택하고, declaration block 안에 property와 value를 작성한다.

기본 구조:

```css
selector {
  property: value;
}
```

예:

```css
.button {
  color: white;
  background-color: blue;
}
```

---

### [핵심]

CSS Syntax 핵심:

- Selector는 style을 적용할 HTML 요소를 선택한다.
- Declaration Block은 `{ }` 안에 작성한다.
- Property는 변경할 style 항목이다.
- Value는 property에 적용할 값이다.
- Declaration은 `property: value;` 형태다.
- Declaration 끝에는 semicolon을 사용한다.
- CSS는 위에서 아래로 해석된다.
- 같은 property가 여러 번 선언되면 cascade 규칙에 따라 최종 값이 결정된다.

---

### [실무]

2026 실무 기준에서 CSS Syntax는 단순 문법보다 유지보수성과 디버깅 가능성이 중요하다.

권장 작성 순서:

```text
Selector 작성
→ Layout 관련 property
→ Box Model 관련 property
→ Typography 관련 property
→ Visual 관련 property
→ Interaction 관련 property
```

예:

```css
.card {
  display: grid;
  gap: 1rem;
  padding: 1.5rem;
  color: #111827;
  background-color: #ffffff;
  border: 1px solid #e5e7eb;
}
```

검수 기준:

- selector가 실제 HTML 구조와 일치하는가?
- property 이름 오타가 없는가?
- value 단위가 올바른가?
- semicolon 누락이 없는가?
- 중복 property가 의도된 것인가?
- 동일 selector 안에서 property 순서가 읽기 쉬운가?

---

### [FAQ]

Q. CSS Syntax가 뭐야?
A. HTML 요소에 style을 적용하기 위해 selector, property, value를 작성하는 CSS 문법이다.

Q. CSS declaration은 뭐야?
A. `property: value;` 형태로 작성되는 한 줄의 style 선언이다.

Q. CSS declaration block은 뭐야?
A. selector 뒤의 `{ }` 안에 들어가는 style 선언 묶음이다.

Q. CSS에서 semicolon은 꼭 필요해?
A. 마지막 선언에서는 생략 가능하지만 실무에서는 일관성을 위해 작성하는 것이 좋다.

---

## 1.2 Declaration and Rule Set

### [개념]

Rule Set은 selector와 declaration block을 합친 CSS 규칙 단위다.

예:

```css
.card-title {
  font-size: 1.5rem;
  font-weight: 700;
}
```

위 코드에서:

- `.card-title`은 selector다.
- `{ ... }`는 declaration block이다.
- `font-size: 1.5rem;`은 declaration이다.
- `font-size`는 property다.
- `1.5rem`은 value다.

---

### [핵심]

Rule Set 핵심:

- 하나의 rule set은 하나의 선택 대상과 style 묶음을 표현한다.
- selector가 잘못되면 rule set은 적용되지 않는다.
- property가 잘못되면 해당 declaration만 무시될 수 있다.
- value가 잘못되면 해당 declaration이 무효가 될 수 있다.
- CSS는 오류가 있어도 전체 파일이 항상 중단되지는 않는다.
- DevTools에서 적용된 rule set과 무시된 declaration을 확인할 수 있다.

---

### [실무]

문제 예:

```css
.button {
  backgroun-color: blue;
}
```

`background-color` 오타로 인해 해당 declaration은 적용되지 않는다.

수정:

```css
.button {
  background-color: blue;
}
```

검수 기준:

- selector가 올바른가?
- property spelling이 올바른가?
- value가 property에 허용되는 형식인가?
- DevTools에서 취소선 처리된 rule이 있는가?
- CSS syntax error가 뒤 rule에 영향을 주지 않는가?

---

### [FAQ]

Q. Rule Set이 뭐야?
A. selector와 declaration block을 합친 CSS 규칙 단위다.

Q. property 오타가 있으면 어떻게 돼?
A. 해당 declaration이 무시될 수 있다.

Q. value가 잘못되면 어떻게 돼?
A. 브라우저가 해당 declaration을 무효로 처리할 수 있다.

Q. CSS 오류는 어디서 확인해?
A. 브라우저 DevTools의 Styles, Computed, Console에서 확인할 수 있다.

---

# 2. CSS Apply Methods

## 2.1 External CSS

### [개념]

External CSS는 별도 `.css` 파일을 만들고 HTML 또는 bundler에서 불러와 style을 적용하는 방식이다.

예:

```html
<link rel="stylesheet" href="/styles.css" />
```

React 또는 bundler 환경:

```js
import "./styles.css";
```

---

### [핵심]

External CSS 핵심:

- CSS 파일을 분리해 관리한다.
- 여러 HTML 또는 component에서 재사용할 수 있다.
- 유지보수성이 좋다.
- browser cache를 활용할 수 있다.
- CSS architecture 구성에 적합하다.
- 파일 import 순서가 cascade에 영향을 준다.
- reset, token, base, component CSS를 역할별로 분리할 수 있다.

---

### [실무]

권장 파일 구조 예:

```text
styles/
├ tokens.css
├ reset.css
├ base.css
├ layout.css
└ components/
  ├ button.css
  └ card.css
```

권장 import 순서 예:

```css
@import "./tokens.css";
@import "./reset.css";
@import "./base.css";
@import "./layout.css";
@import "./components/button.css";
@import "./components/card.css";
```

검수 기준:

- CSS 파일이 실제로 import되었는가?
- import 순서가 의도한 cascade와 일치하는가?
- reset이 component CSS 뒤에 로드되지 않는가?
- component CSS가 page CSS에 과도하게 의존하지 않는가?
- 같은 selector가 여러 파일에서 충돌하지 않는가?

---

### [FAQ]

Q. External CSS가 뭐야?
A. 별도 CSS 파일을 만들어 HTML이나 JavaScript에서 불러와 style을 적용하는 방식이다.

Q. 실무에서 가장 많이 쓰는 방식은 뭐야?
A. 일반적으로 External CSS 또는 CSS Module, CSS-in-JS, utility framework 등 파일 기반 관리 방식을 많이 사용한다.

Q. CSS import 순서가 중요한 이유는?
A. 같은 specificity라면 나중에 로드된 style이 이전 style을 덮어쓸 수 있기 때문이다.

Q. reset CSS는 언제 로드해야 해?
A. 보통 component CSS보다 먼저 로드해야 한다.

---

## 2.2 Internal CSS

### [개념]

Internal CSS는 HTML 문서의 `<style>` 태그 안에 CSS를 직접 작성하는 방식이다.

예:

```html
<style>
  .button {
    color: white;
    background-color: blue;
  }
</style>
```

---

### [핵심]

Internal CSS 핵심:

- HTML 문서 내부에 CSS를 작성한다.
- 단일 페이지나 빠른 테스트에 사용할 수 있다.
- CSS 재사용성이 낮다.
- 파일 분리가 되지 않아 유지보수가 어려워질 수 있다.
- 문서별로 style이 중복될 수 있다.
- 규모가 커지는 프로젝트에는 적합하지 않다.

---

### [실무]

사용해도 되는 경우:

```text
간단한 데모
→ 테스트 페이지
→ 이메일 HTML 일부
→ 빠른 prototype
```

피해야 하는 경우:

```text
대규모 서비스
→ Component 기반 프로젝트
→ Design System 기반 UI
→ 여러 페이지에서 재사용되는 style
```

검수 기준:

- Internal CSS가 임시 테스트인지 확인한다.
- 재사용되는 style이라면 external file로 분리한다.
- head 내부 style이 너무 길어지지 않았는가?
- component style이 문서 내부에 흩어져 있지 않은가?

---

### [FAQ]

Q. Internal CSS가 뭐야?
A. HTML 문서 내부의 style 태그에 CSS를 작성하는 방식이다.

Q. Internal CSS는 언제 써?
A. 간단한 예제, 테스트, prototype에서 사용할 수 있다.

Q. 실무 프로젝트에서 Internal CSS를 많이 써도 돼?
A. 보통 권장하지 않는다. 재사용성과 유지보수가 떨어질 수 있다.

---

## 2.3 Inline Style

### [개념]

Inline Style은 HTML 요소의 `style` attribute에 CSS를 직접 작성하는 방식이다.

예:

```html
<button style="color: white; background-color: blue;">Save</button>
```

---

### [핵심]

Inline Style 핵심:

- 특정 요소에 직접 style을 적용한다.
- specificity가 높다.
- 재사용성이 낮다.
- override가 어려울 수 있다.
- pseudo class와 media query를 직접 작성할 수 없다.
- JavaScript로 동적 style을 넣을 때 제한적으로 사용한다.
- 반복 UI에는 적합하지 않다.

---

### [실무]

사용 가능한 경우:

```text
동적으로 계산되는 값
→ CSS Variable 주입
→ 임시 테스트
→ 매우 제한된 one-off style
```

권장 방식:

```html
<div class="progress" style="--progress-value: 72%;">Progress</div>
```

```css
.progress {
  width: var(--progress-value);
}
```

검수 기준:

- inline style이 반복 사용되고 있지 않은가?
- class로 분리할 수 있는 style인가?
- inline style 때문에 component style override가 어려워지지 않는가?
- pseudo class나 responsive 처리가 필요한 style은 아닌가?
- 동적 값이라면 CSS Variable로 전달할 수 있는가?

---

### [FAQ]

Q. Inline Style이 뭐야?
A. HTML 요소의 style attribute에 CSS를 직접 작성하는 방식이다.

Q. Inline Style은 왜 조심해야 해?
A. 재사용성이 낮고 specificity가 높아 override가 어려워질 수 있기 때문이다.

Q. Inline Style로 hover를 작성할 수 있어?
A. 일반 HTML inline style만으로는 pseudo class hover를 직접 작성할 수 없다.

Q. 동적 style은 어떻게 처리하면 좋아?
A. 필요한 경우 CSS Variable을 inline style로 주입하고 실제 style은 CSS class에서 처리할 수 있다.

---

# 3. Selector

## 3.1 Selector Concept

### [개념]

Selector는 CSS rule이 적용될 HTML 요소를 선택하는 문법이다.

Selector가 정확하지 않으면 CSS는 적용되지 않거나 의도하지 않은 요소에 적용된다.

---

### [핵심]

Selector 핵심:

- type selector는 태그 이름으로 선택한다.
- class selector는 class attribute로 선택한다.
- id selector는 id attribute로 선택한다.
- attribute selector는 attribute 조건으로 선택한다.
- pseudo class는 상태나 조건을 선택한다.
- pseudo element는 요소의 일부 또는 가상 요소를 선택한다.
- selector가 복잡해질수록 유지보수성이 낮아질 수 있다.
- styling에는 class selector를 우선 사용한다.

---

### [실무]

권장 selector:

```css
.button {
}

.card-title {
}

.form-input[aria-invalid="true"] {
}
```

주의 selector:

```css
body main section div article h2 {
}

#saveButton {
}
```

검수 기준:

- selector가 실제 DOM과 일치하는가?
- selector chain이 지나치게 길지 않은가?
- id selector를 styling에 남용하지 않았는가?
- HTML 구조 변경에 취약하지 않은가?
- component class 기준으로 scope를 잡았는가?

---

### [FAQ]

Q. Selector가 뭐야?
A. CSS rule을 적용할 HTML 요소를 선택하는 문법이다.

Q. 실무에서 어떤 selector를 가장 많이 써?
A. 유지보수와 재사용성을 위해 class selector를 가장 많이 사용한다.

Q. 긴 selector chain은 왜 안 좋아?
A. HTML 구조 변경에 취약하고 specificity가 높아져 override가 어려워지기 때문이다.

Q. id selector는 쓰면 안 돼?
A. 사용할 수는 있지만 styling에는 class selector가 더 유지보수에 적합하다.

---

## 3.2 Type Selector

### [개념]

Type Selector는 HTML 태그 이름으로 요소를 선택하는 selector다.

예:

```css
p {
  line-height: 1.5;
}
```

---

### [핵심]

Type Selector 핵심:

- 태그 이름으로 선택한다.
- 모든 해당 태그에 적용된다.
- base style 작성에 유용하다.
- component 내부 styling에는 범위가 넓을 수 있다.
- 전역 type selector는 의도하지 않은 영향을 줄 수 있다.
- reset/base layer에서 제한적으로 사용하는 것이 좋다.

---

### [실무]

Base Style 예:

```css
body {
  margin: 0;
  font-family: system-ui, sans-serif;
}

img {
  display: block;
  max-width: 100%;
}

button,
input,
textarea,
select {
  font: inherit;
}
```

주의:

```css
h2 {
  color: blue;
}
```

모든 h2에 영향을 주므로 component별 heading style과 충돌할 수 있다.

검수 기준:

- 전역 type selector가 필요한가?
- reset/base 목적에 맞는가?
- component style을 의도치 않게 덮지 않는가?
- page-specific style이면 class selector가 더 적절하지 않은가?

---

### [FAQ]

Q. Type Selector가 뭐야?
A. HTML 태그 이름으로 요소를 선택하는 selector다.

Q. Type Selector는 언제 써?
A. reset, base style, 전역 typography 기준을 작성할 때 사용할 수 있다.

Q. Component style에 type selector만 쓰면 안 좋아?
A. 범위가 넓어 의도하지 않은 요소까지 영향을 줄 수 있다.

---

## 3.3 Class Selector

### [개념]

Class Selector는 HTML 요소의 `class` attribute 값을 기준으로 선택하는 selector다.

예:

```css
.button {
  padding: 1rem;
}
```

---

### [핵심]

Class Selector 핵심:

- `.`으로 시작한다.
- 여러 요소가 같은 class를 공유할 수 있다.
- component styling에 가장 많이 사용된다.
- specificity가 관리하기 적절하다.
- base class와 variant class를 조합할 수 있다.
- class naming이 유지보수성에 중요하다.
- React에서는 HTML의 class 대신 JSX `className`을 사용한다.

---

### [실무]

Component 예:

```html
<button class="button button-primary" type="button">Save</button>
```

```css
.button {
  display: inline-flex;
  align-items: center;
}

.button-primary {
  background-color: var(--color-primary);
}
```

검수 기준:

- class name이 역할 기반인가?
- CSS selector와 HTML className이 일치하는가?
- base class와 variant class가 분리되어 있는가?
- class selector가 component scope를 명확히 하는가?
- 색상이나 위치 기반 이름을 피했는가?

---

### [FAQ]

Q. Class Selector가 뭐야?
A. class attribute 값을 기준으로 요소를 선택하는 CSS selector다.

Q. Class Selector는 어떻게 작성해?
A. `.class-name` 형태로 작성한다.

Q. Component Styling에는 어떤 selector가 좋아?
A. 일반적으로 class selector가 가장 적합하다.

Q. React에서 class selector를 쓰려면?
A. JSX에서는 `className="button"`처럼 작성하고 CSS에서는 `.button`으로 선택한다.

---

## 3.4 ID Selector

### [개념]

ID Selector는 HTML 요소의 `id` attribute 값을 기준으로 선택하는 selector다.

예:

```css
#main-content {
  outline: none;
}
```

---

### [핵심]

ID Selector 핵심:

- `#`으로 시작한다.
- id는 문서 내에서 고유해야 한다.
- specificity가 높다.
- styling에 남용하면 override가 어려워진다.
- fragment link, label 연결, aria 연결에는 id가 필요하다.
- CSS styling에는 class selector를 우선 사용한다.

---

### [실무]

id가 적절한 경우:

```html
<main id="main-content">Main content</main>
```

id selector 남용 예:

```css
#cardTitle {
  color: blue;
}
```

권장:

```css
.card-title {
  color: var(--color-primary);
}
```

검수 기준:

- id가 문서 내 고유한가?
- styling에 id selector를 남용하지 않았는가?
- label/aria/fragment 목적이라면 id가 적절한가?
- override가 어려운 CSS 구조를 만들지 않았는가?

---

### [FAQ]

Q. ID Selector가 뭐야?
A. id attribute 값을 기준으로 요소를 선택하는 CSS selector다.

Q. ID Selector는 어떻게 작성해?
A. `#id-name` 형태로 작성한다.

Q. ID Selector를 styling에 많이 쓰면 왜 안 좋아?
A. specificity가 높아 override와 유지보수가 어려워지기 때문이다.

Q. id는 언제 필요해?
A. label 연결, aria 참조, fragment link target에 필요하다.

---

## 3.5 Attribute Selector

### [개념]

Attribute Selector는 HTML attribute의 존재나 값을 기준으로 요소를 선택하는 selector다.

예:

```css
input[disabled] {
  opacity: 0.6;
}

.form-input[aria-invalid="true"] {
  border-color: red;
}
```

---

### [핵심]

Attribute Selector 핵심:

- 특정 attribute가 있는 요소를 선택할 수 있다.
- 특정 attribute 값과 일치하는 요소를 선택할 수 있다.
- Form state와 ARIA state styling에 유용하다.
- `data-*` attribute와 함께 component state styling에 사용할 수 있다.
- attribute 상태와 실제 UI 상태가 일치해야 한다.
- 너무 복잡한 attribute selector는 읽기 어려워질 수 있다.

---

### [실무]

ARIA State 예:

```css
.nav-link[aria-current="page"] {
  font-weight: 700;
}

.form-input[aria-invalid="true"] {
  border-color: var(--color-danger);
}

.accordion-trigger[aria-expanded="true"] {
  color: var(--color-primary);
}
```

Data Attribute 예:

```css
[data-theme="dark"] {
  --color-background: #111827;
  --color-text: #f9fafb;
}
```

검수 기준:

- attribute 값이 실제 상태와 일치하는가?
- ARIA state를 styling hook으로 사용할 때 접근성 상태도 정확한가?
- `data-*`가 접근성 attribute를 대체하지 않는가?
- selector가 지나치게 복잡하지 않은가?

---

### [FAQ]

Q. Attribute Selector가 뭐야?
A. HTML attribute의 존재나 값을 기준으로 요소를 선택하는 CSS selector다.

Q. aria-invalid로 style을 줄 수 있어?
A. 가능하다. `[aria-invalid="true"]` selector로 오류 상태 style을 줄 수 있다.

Q. data attribute를 CSS selector로 써도 돼?
A. 가능하다. 다만 접근성 상태 전달은 ARIA attribute를 사용해야 한다.

Q. Attribute Selector는 언제 유용해?
A. form state, aria state, theme, component state styling에 유용하다.

---

# 4. Selector Relationship

## 4.1 Descendant Selector

### [개념]

Descendant Selector는 특정 요소 내부에 있는 모든 후손 요소를 선택하는 selector다.

공백으로 관계를 표현한다.

예:

```css
.card p {
  color: gray;
}
```

`.card` 내부의 모든 `p` 요소를 선택한다.

---

### [핵심]

Descendant Selector 핵심:

- 공백으로 후손 관계를 표현한다.
- 직접 자식뿐 아니라 모든 깊이의 하위 요소를 선택한다.
- 범위가 넓어질 수 있다.
- component 내부 typography에 사용할 수 있다.
- selector chain이 길어지면 유지보수가 어려워진다.
- 의도하지 않은 nested component에 영향을 줄 수 있다.

---

### [실무]

사용 가능 예:

```css
.article-content p {
  line-height: 1.7;
}
```

주의 예:

```css
.page main section div p span {
  color: red;
}
```

검수 기준:

- 후손 전체 선택이 의도된 것인가?
- nested component까지 영향을 주지 않는가?
- selector chain이 길지 않은가?
- class selector로 더 명확히 표현할 수 없는가?

---

### [FAQ]

Q. Descendant Selector가 뭐야?
A. 특정 요소 내부의 모든 후손 요소를 선택하는 selector다.

Q. Descendant Selector는 어떻게 작성해?
A. `.parent .child`처럼 공백으로 작성한다.

Q. Descendant Selector는 왜 조심해야 해?
A. 직접 자식뿐 아니라 깊은 하위 요소까지 영향을 줄 수 있기 때문이다.

---

## 4.2 Child Selector

### [개념]

Child Selector는 특정 요소의 직접 자식 요소만 선택하는 selector다.

`>` 기호를 사용한다.

예:

```css
.card > p {
  margin: 0;
}
```

---

### [핵심]

Child Selector 핵심:

- `>`로 직접 자식 관계를 표현한다.
- descendant selector보다 범위가 좁다.
- HTML 구조에 더 강하게 의존한다.
- wrapper 요소가 추가되면 selector가 깨질 수 있다.
- layout 구조를 명확히 제한할 때 유용하다.
- list나 direct item styling에 사용할 수 있다.

---

### [실무]

List 예:

```css
.nav-list > li {
  display: flex;
}
```

Grid Item 예:

```css
.card-grid > * {
  min-width: 0;
}
```

검수 기준:

- 직접 자식 관계가 실제 DOM과 일치하는가?
- wrapper 추가 시 깨질 가능성이 있는가?
- descendant selector보다 child selector가 적절한가?
- layout item을 직접 제어하는 목적이 명확한가?

---

### [FAQ]

Q. Child Selector가 뭐야?
A. 특정 요소의 직접 자식만 선택하는 selector다.

Q. Child Selector는 어떻게 작성해?
A. `.parent > .child`처럼 `>` 기호를 사용한다.

Q. Child Selector와 Descendant Selector 차이는?
A. Child Selector는 직접 자식만 선택하고 Descendant Selector는 모든 후손을 선택한다.

---

## 4.3 Group Selector

### [개념]

Group Selector는 여러 selector에 같은 style을 적용하기 위해 comma로 묶는 selector다.

예:

```css
h1,
h2,
h3 {
  line-height: 1.2;
}
```

---

### [핵심]

Group Selector 핵심:

- comma로 여러 selector를 묶는다.
- 중복 CSS를 줄일 수 있다.
- 각 selector는 독립적으로 해석된다.
- 하나의 selector 오타가 전체 rule 해석에 영향을 줄 수 있는 경우가 있다.
- 너무 많은 selector를 묶으면 의도가 흐려질 수 있다.
- 공통 base style에 적합하다.

---

### [실무]

좋은 예:

```css
button,
input,
textarea,
select {
  font: inherit;
}
```

```css
.card-title,
.modal-title,
.section-title {
  line-height: 1.2;
}
```

검수 기준:

- 묶인 selector들이 같은 style을 공유하는 것이 의미상 맞는가?
- 너무 많은 selector를 한 rule에 넣지 않았는가?
- selector 중 하나가 잘못 작성되지 않았는가?
- 나중에 개별 override가 많아지지 않는가?

---

### [FAQ]

Q. Group Selector가 뭐야?
A. 여러 selector에 같은 style을 적용하기 위해 comma로 묶는 selector다.

Q. Group Selector는 왜 써?
A. 중복 CSS를 줄이고 공통 style을 한 번에 관리하기 위해 사용한다.

Q. Group Selector는 언제 조심해야 해?
A. 서로 다른 목적의 selector를 억지로 묶으면 유지보수가 어려워질 수 있다.

---

# 5. Pseudo Class

## 5.1 Pseudo Class Concept

### [개념]

Pseudo Class는 요소의 상태나 조건을 기준으로 선택하는 CSS selector다.

기본적으로 `:` 기호를 사용한다.

예:

```css
a:hover {
  text-decoration-thickness: 0.12em;
}

button:disabled {
  opacity: 0.6;
}
```

---

### [핵심]

Pseudo Class 핵심:

- `:`로 시작한다.
- 요소의 상태, 조건, 위치를 선택한다.
- hover, focus, disabled 같은 기본 상태를 선택할 수 있다.
- first-child, last-child 같은 구조 조건을 선택할 수 있다.
- form 상태와 interaction 상태 styling에 사용된다.
- hover만으로 interaction을 설계하면 keyboard/touch 접근성 문제가 생길 수 있다.
- 상세 interaction state 기준은 Part12에서 다룬다.

---

### [실무]

기초 예:

```css
.link:hover {
  color: var(--color-primary);
}

.button:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.button:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}
```

검수 기준:

- pseudo class가 실제 요소 상태와 맞는가?
- hover만 있고 focus-visible이 빠지지 않았는가?
- disabled 상태에 hover/active가 적용되지 않는가?
- 구조 기반 pseudo class가 DOM 변경에 취약하지 않은가?
- 상세 상태 설계는 Part12 기준과 연결되는가?

---

### [FAQ]

Q. Pseudo Class가 뭐야?
A. 요소의 상태나 조건을 기준으로 선택하는 CSS selector다.

Q. Pseudo Class는 어떤 기호를 써?
A. `:` 기호를 사용한다.

Q. hover는 pseudo class야?
A. 맞다. `:hover`는 pseudo class다.

Q. Pseudo Class 상세 기준은 어디서 다뤄?
A. Interaction, Form State, Structural Pseudo Class 상세 기준은 Part12에서 다룬다.

---

## 5.2 Focus and Focus Visible

### [개념]

`:focus`와 `:focus-visible`은 요소가 keyboard 또는 사용자 입력에 의해 focus된 상태를 선택하는 pseudo class다.

Focus style은 keyboard accessibility의 핵심이다.

---

### [핵심]

Focus 핵심:

- `:focus`는 요소가 focus된 상태다.
- `:focus-visible`은 브라우저가 focus 표시가 필요하다고 판단한 상태다.
- keyboard 사용자는 focus 위치를 시각적으로 확인할 수 있어야 한다.
- outline을 제거만 하면 접근성 문제가 생긴다.
- focus style은 색상과 모양이 충분히 구분되어야 한다.
- overflow hidden이 focus ring을 자를 수 있다.

---

### [실무]

권장 예:

```css
:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}
```

Component 예:

```css
.button:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 3px;
}
```

금지 예:

```css
*:focus {
  outline: none;
}
```

검수 기준:

- keyboard Tab 이동 시 focus가 보이는가?
- outline을 제거만 하지 않았는가?
- focus ring이 배경과 구분되는가?
- focus ring이 overflow hidden에 잘리지 않는가?
- component별 focus-visible이 일관적인가?

---

### [FAQ]

Q. focus-visible은 뭐야?
A. 브라우저가 focus 표시가 필요하다고 판단한 상태를 선택하는 pseudo class다.

Q. focus outline을 없애도 돼?
A. 제거만 하면 안 된다. 반드시 대체 focus-visible style을 제공해야 한다.

Q. focus-visible은 왜 중요해?
A. keyboard 사용자가 현재 조작 위치를 알 수 있어야 하기 때문이다.

---

# 6. Pseudo Element

## 6.1 Pseudo Element Concept

### [개념]

Pseudo Element는 요소의 특정 부분 또는 가상 요소를 선택하는 CSS selector다.

기본적으로 `::` 기호를 사용한다.

예:

```css
.section-title::after {
  content: "";
  display: block;
  width: 48px;
  height: 3px;
  background-color: var(--color-primary);
}
```

---

### [핵심]

Pseudo Element 핵심:

- `::`로 시작한다.
- `::before`와 `::after`는 가상 요소를 생성한다.
- `content` property가 필요한 경우가 많다.
- 장식 요소에 적합하다.
- 중요한 정보를 pseudo element에만 넣으면 안 된다.
- placeholder, marker, selection 같은 특정 부분도 pseudo element로 선택할 수 있다.
- 상세 pseudo element 기준은 Part12에서 다룬다.

---

### [실무]

기초 예:

```css
.required-label::after {
  content: " *";
  color: var(--color-danger);
}
```

주의:

```css
.button::before {
  content: "Delete";
}
```

중요한 button name을 CSS content에만 넣으면 접근성 문제가 생길 수 있다.

검수 기준:

- pseudo element가 장식 목적에 사용되는가?
- `content`가 누락되지 않았는가?
- 중요한 정보가 CSS content에만 있지 않은가?
- 접근성 정보와 시각 정보가 분리되지 않았는가?
- 상세 pseudo element 사용 기준은 Part12와 일치하는가?

---

### [FAQ]

Q. Pseudo Element가 뭐야?
A. 요소의 특정 부분이나 가상 요소를 선택하는 CSS selector다.

Q. Pseudo Element는 어떤 기호를 써?
A. 일반적으로 `::` 기호를 사용한다.

Q. before와 after에는 content가 필요해?
A. 대부분 필요하다. content가 없으면 표시되지 않는 경우가 많다.

Q. Pseudo Element 상세 기준은 어디서 다뤄?
A. `::before`, `::after`, `::placeholder`, `::marker`, `::selection` 상세 기준은 Part12에서 다룬다.

---

# 7. Cascade

## 7.1 Cascade Concept

### [개념]

Cascade는 여러 CSS rule이 같은 요소와 같은 property에 적용될 때 최종 style을 결정하는 규칙이다.

Cascade는 CSS의 핵심 동작 방식이다.

---

### [핵심]

Cascade 결정 요소:

- Origin
- Importance
- Specificity
- Source Order
- Inheritance
- Cascade Layer

실무 기초 기준에서는 아래 세 가지를 우선 확인한다.

```text
Specificity
→ Source Order
→ Inheritance
```

---

### [실무]

예:

```css
.button {
  color: blue;
}

.primary-button {
  color: red;
}
```

HTML:

```html
<button class="button primary-button" type="button">Save</button>
```

두 selector의 specificity가 같다면 나중에 작성된 `.primary-button`의 `color: red`가 적용된다.

검수 기준:

- 같은 property를 여러 selector가 지정하고 있는가?
- 어떤 rule이 최종 적용되는지 DevTools에서 확인했는가?
- 나중에 로드된 CSS가 이전 CSS를 덮는 구조인가?
- specificity가 필요 이상으로 높아지지 않았는가?
- inheritance로 적용된 값인지 직접 적용된 값인지 구분했는가?

---

### [FAQ]

Q. Cascade가 뭐야?
A. 여러 CSS rule이 충돌할 때 최종 style을 결정하는 CSS 규칙이다.

Q. 같은 property를 여러 번 쓰면 뭐가 적용돼?
A. specificity와 source order 등 cascade 규칙에 따라 최종 값이 결정된다.

Q. Cascade 문제는 어떻게 확인해?
A. DevTools Styles와 Computed 패널에서 어떤 rule이 최종 적용되는지 확인한다.

---

## 7.2 Source Order

### [개념]

Source Order는 CSS rule이 작성되거나 로드된 순서다.

같은 specificity를 가진 rule이 충돌하면 나중에 작성된 rule이 우선 적용된다.

---

### [핵심]

Source Order 핵심:

- 같은 specificity일 때 뒤에 있는 rule이 우선한다.
- CSS 파일 import 순서도 source order에 영향을 준다.
- reset CSS가 나중에 로드되면 component style을 덮을 수 있다.
- page override는 나중에 로드될 수 있지만 남용하면 유지보수가 어렵다.
- source order를 이용한 override는 의도적으로 관리해야 한다.

---

### [실무]

예:

```css
.card-title {
  color: black;
}

.card-title {
  color: blue;
}
```

최종 color는 blue다.

파일 순서 예:

```css
@import "./reset.css";
@import "./base.css";
@import "./components/card.css";
```

검수 기준:

- CSS import 순서가 의도와 맞는가?
- component CSS가 reset/base 뒤에 로드되는가?
- page override가 component 기본 style을 과도하게 덮지 않는가?
- 같은 selector 중복이 의도된 것인가?

---

### [FAQ]

Q. Source Order가 뭐야?
A. CSS rule이 작성되거나 로드된 순서다.

Q. 같은 specificity면 어떤 rule이 이겨?
A. 나중에 작성되거나 로드된 rule이 우선 적용된다.

Q. CSS 파일 순서도 중요해?
A. 중요하다. import 순서에 따라 최종 style이 달라질 수 있다.

---

# 8. Specificity

## 8.1 Specificity Concept

### [개념]

Specificity는 selector의 우선순위를 계산하는 기준이다.

같은 요소와 같은 property에 여러 CSS rule이 적용될 때 specificity가 높은 selector가 우선한다.

---

### [핵심]

Specificity 기초:

```text
Inline Style
→ ID Selector
→ Class / Attribute / Pseudo Class
→ Type / Pseudo Element
```

예:

```css
.button {
  color: blue;
}

#save-button {
  color: red;
}
```

`#save-button`이 `.button`보다 specificity가 높다.

---

### [실무]

권장:

```css
.button {
  color: var(--color-text);
}

.button-primary {
  color: white;
}
```

주의:

```css
body main section .page .card .button {
  color: red;
}
```

Specificity를 낮게 유지하면 component override와 유지보수가 쉬워진다.

검수 기준:

- ID selector를 styling에 남용하지 않았는가?
- selector chain이 길지 않은가?
- specificity를 높이는 방식으로만 문제를 해결하지 않았는가?
- class selector 중심으로 component style을 작성했는가?
- `!important`로 specificity 문제를 숨기지 않았는가?

---

### [FAQ]

Q. Specificity가 뭐야?
A. CSS selector의 우선순위를 계산하는 기준이다.

Q. ID selector가 class selector보다 강해?
A. 맞다. ID selector는 class selector보다 specificity가 높다.

Q. Specificity를 낮게 유지해야 하는 이유는?
A. override와 유지보수가 쉬워지고 cascade 충돌이 줄어들기 때문이다.

---

## 8.2 Important

### [개념]

`!important`는 CSS declaration의 우선순위를 강하게 높이는 키워드다.

예:

```css
.button {
  color: red !important;
}
```

---

### [핵심]

`!important` 핵심:

- 일반 cascade 우선순위를 강하게 변경한다.
- 긴급 override에 사용할 수 있다.
- 남용하면 유지보수가 어려워진다.
- 다른 `!important`와 충돌하면 다시 specificity와 source order 문제가 발생한다.
- component styling의 일반 해결책으로 사용하면 안 된다.
- utility class나 외부 library override에서 제한적으로 사용할 수 있다.

---

### [실무]

피해야 할 예:

```css
.button {
  color: red !important;
}
```

권장 해결:

```text
selector 구조 단순화
→ import 순서 조정
→ component responsibility 정리
→ variant class 추가
→ token 값 수정
```

사용 가능성이 있는 경우:

```css
[hidden] {
  display: none !important;
}
```

검수 기준:

- `!important`가 정말 필요한가?
- selector 구조나 import 순서 문제를 숨기고 있지 않은가?
- 같은 property에 `!important`가 반복되지 않는가?
- accessibility 관련 hidden 처리처럼 명확한 목적이 있는가?

---

### [FAQ]

Q. !important는 뭐야?
A. CSS declaration의 우선순위를 강하게 높이는 키워드다.

Q. !important를 쓰면 문제가 해결돼?
A. 일시적으로 해결될 수 있지만 cascade 구조를 더 복잡하게 만들 수 있다.

Q. !important는 언제 써도 돼?
A. `[hidden]` 보호나 외부 style override처럼 명확한 이유가 있을 때 제한적으로 사용한다.

---

# 9. Inheritance

## 9.1 CSS Inheritance Concept

### [개념]

Inheritance는 일부 CSS property가 부모 요소에서 자식 요소로 전달되는 동작이다.

주로 typography 관련 property는 상속되는 경우가 많다.

---

### [핵심]

상속되는 대표 property:

- `color`
- `font-family`
- `font-size`
- `font-weight`
- `line-height`
- `visibility`

상속되지 않는 대표 property:

- `margin`
- `padding`
- `border`
- `background-color`
- `width`
- `height`
- `display`
- `position`

---

### [실무]

예:

```css
body {
  color: #111827;
  font-family: system-ui, sans-serif;
}
```

`body`의 `color`와 `font-family`는 자식 요소에 상속될 수 있다.

Form 요소는 브라우저 기본 style 때문에 font 상속을 명시하는 것이 좋다.

```css
button,
input,
textarea,
select {
  font: inherit;
}
```

검수 기준:

- 상속된 style인지 직접 적용된 style인지 구분했는가?
- form 요소가 font를 상속하는가?
- color가 의도치 않게 하위 component까지 전달되지 않는가?
- background-color가 상속된다고 착각하지 않았는가?

---

### [FAQ]

Q. CSS Inheritance가 뭐야?
A. 일부 CSS property가 부모 요소에서 자식 요소로 전달되는 동작이다.

Q. color는 상속돼?
A. 일반적으로 상속된다.

Q. margin과 padding도 상속돼?
A. 아니다. margin과 padding은 일반적으로 상속되지 않는다.

Q. button에 body font가 안 먹는 이유는?
A. form 요소가 브라우저 기본 font를 가질 수 있으므로 `font: inherit`을 명시한다.

---

# 10. CSS Units

## 10.1 CSS Unit Concept

### [개념]

CSS Unit은 길이, 크기, 간격, 비율을 표현하는 단위다.

대표 단위:

```text
px
rem
em
%
vw
vh
dvh
fr
```

---

### [핵심]

Unit 핵심:

- `px`는 고정 pixel 단위다.
- `rem`은 root font-size 기준이다.
- `em`은 현재 요소 또는 부모 font-size 기준이다.
- `%`는 기준 요소에 대한 비율이다.
- `vw`는 viewport width 기준이다.
- `vh`는 viewport height 기준이다.
- `dvh`는 dynamic viewport height 기준이다.
- `fr`은 CSS Grid에서 사용되는 fraction 단위다.
- typography와 spacing에는 rem 기반 token이 자주 사용된다.
- border나 세밀한 선에는 px가 적합할 수 있다.

---

### [실무]

예:

```css
:root {
  --space-4: 1rem;
}

.container {
  width: min(100% - 2rem, 1120px);
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-4);
}
```

검수 기준:

- fixed px width가 responsive 문제를 만들지 않는가?
- spacing scale이 rem 기반으로 일관되는가?
- viewport unit이 모바일 browser UI 변화에 취약하지 않은가?
- Grid에서 fr 단위가 적절히 사용되었는가?
- `%` 기준이 어떤 부모인지 이해했는가?

---

### [FAQ]

Q. CSS Unit이 뭐야?
A. 크기, 간격, 비율을 표현하는 CSS 단위다.

Q. rem은 뭐야?
A. root font-size를 기준으로 하는 단위다.

Q. em은 뭐야?
A. 현재 요소 또는 부모 font-size를 기준으로 하는 단위다.

Q. fr은 어디서 써?
A. CSS Grid에서 사용되는 fraction 단위다.

---

# 11. CSS Comments

## 11.1 Comment Rules

### [개념]

CSS Comment는 CSS 코드에 설명을 남기기 위한 문법이다.

CSS comment는 `/* ... */` 형태로 작성한다.

예:

```css
/* Button Component */
.button {
  display: inline-flex;
}
```

---

### [핵심]

Comment 핵심:

- CSS comment는 브라우저가 style로 해석하지 않는다.
- section 구분에 사용할 수 있다.
- 복잡한 의도 설명에 사용할 수 있다.
- 불필요한 comment는 noise가 된다.
- 오래된 comment는 실제 코드와 불일치할 수 있다.
- TODO comment는 작업 관리와 연결해야 한다.

---

### [실무]

좋은 예:

```css
/* Keep focus ring visible for keyboard users. */
.button:focus-visible {
  outline: 2px solid currentColor;
}
```

불필요한 예:

```css
/* color red */
.error {
  color: red;
}
```

검수 기준:

- comment가 코드의 의도를 설명하는가?
- 코드만 봐도 알 수 있는 내용을 반복하지 않는가?
- 오래된 comment가 실제 코드와 충돌하지 않는가?
- section comment가 파일 탐색에 도움이 되는가?

---

### [FAQ]

Q. CSS comment는 어떻게 작성해?
A. `/* comment */` 형태로 작성한다.

Q. CSS comment는 언제 써?
A. 복잡한 의도, 접근성 이유, section 구분이 필요할 때 사용한다.

Q. comment를 많이 쓰면 좋아?
A. 아니다. 코드만 봐도 알 수 있는 내용을 반복하면 noise가 된다.

---

# 12. CSS Debugging

## 12.1 CSS Not Applied

### [개념]

CSS Not Applied는 작성한 style이 요소에 적용되지 않는 문제다.

주요 원인은 selector 불일치, import 누락, syntax error, cascade override, media query 조건 불일치다.

---

### [핵심]

CSS Not Applied 원인:

- CSS 파일 import 누락
- className 오타
- selector와 DOM 구조 불일치
- property 오타
- value 오류
- semicolon 또는 brace 오류
- media query 조건 불일치
- specificity에서 밀림
- source order에서 밀림
- inline style 또는 important override

---

### [실무]

Debug Flow:

```text
CSS 파일 로드 확인
→ DOM className 확인
→ selector 매칭 확인
→ DevTools Styles 확인
→ 취소선 rule 확인
→ Computed Style 확인
→ Media Query 조건 확인
→ Specificity / Source Order 확인
```

문제 예:

```text
문제: .card-title style이 적용되지 않음
원인: HTML class는 card-titel
해결: className 오타 수정
```

검수 기준:

- DevTools에 CSS rule이 보이는가?
- rule이 취소선 처리되어 있는가?
- 실제 DOM class와 CSS selector가 일치하는가?
- media query가 현재 viewport에서 활성화되는가?
- property/value가 유효한가?

---

### [FAQ]

Q. CSS가 안 먹으면 무엇을 먼저 봐?
A. CSS 파일 import, className 오타, selector 매칭, DevTools Styles 패널을 먼저 본다.

Q. CSS rule이 DevTools에 보이는데 취소선이면?
A. 다른 rule에 의해 override된 것이다. specificity와 source order를 확인한다.

Q. media query 안 style이 안 먹으면?
A. viewport 조건과 min-width/max-width 방향을 확인한다.

---

# 13. Common Mistakes

## 13.1 CSS Syntax Selector Cascade Common Mistakes

### [개념]

CSS Syntax, Selector, Cascade 실수는 style 미적용, 의도하지 않은 override, layout 깨짐, 유지보수 어려움으로 이어진다.

---

### [핵심]

자주 발생하는 실수:

- CSS 파일 import 누락
- className 오타
- selector와 HTML 구조 불일치
- property 오타
- value 단위 누락
- semicolon 또는 brace 누락
- type selector를 component style에 남용
- id selector를 styling에 남용
- descendant selector chain 과다
- child selector가 DOM 구조 변경에 깨짐
- pseudo class를 hover에만 의존
- focus-visible 누락
- pseudo element content 누락
- 중요한 정보를 CSS content에만 작성
- source order를 고려하지 않음
- specificity를 계속 높여 문제 해결
- `!important` 남용
- inheritance와 direct style을 혼동
- form 요소 font inheritance 누락
- fixed px width 남용

---

### [실무]

Troubleshooting Flow:

```text
Style Problem
→ CSS import 확인
→ selector/className 확인
→ syntax 확인
→ DevTools Styles 확인
→ Computed Style 확인
→ cascade 확인
→ specificity 확인
→ inheritance 확인
→ 관련 상세 문서 참조
```

문제 예:

```text
문제: Button color가 예상과 다름
원인: 더 높은 specificity selector가 color를 override
해결: selector 구조 단순화, component class 기준으로 정리
```

```text
문제: Keyboard focus가 보이지 않음
원인: outline none만 적용
해결: focus-visible style 제공
```

검수 기준:

- 문제를 추측이 아니라 DevTools로 확인했는가?
- selector를 더 강하게 만드는 대신 구조를 정리했는가?
- `!important` 없이 해결 가능한가?
- pseudo/focus/accessibility 기준은 Part12와 연결되는가?
- troubleshooting 기준은 Part16과 연결되는가?

---

### [FAQ]

Q. CSS Syntax에서 가장 흔한 실수는 뭐야?
A. property 오타, value 단위 누락, brace/semicolon 누락, CSS import 누락이 흔하다.

Q. Selector에서 가장 흔한 실수는 뭐야?
A. className 오타, 실제 DOM과 맞지 않는 selector, 긴 descendant selector 남용이다.

Q. Cascade에서 가장 흔한 실수는 뭐야?
A. specificity와 source order를 고려하지 않고 style이 덮이는 문제를 놓치는 것이다.

Q. CSS 문제는 어떤 순서로 확인해?
A. import, selector, syntax, DevTools Styles, Computed, cascade, specificity, inheritance 순서로 확인한다.

---

# 14. Comparison Rules

## 14.1 CSS Apply Method Comparison

### [개념]

CSS 적용 방식은 External CSS, Internal CSS, Inline Style로 구분할 수 있다.

각 방식은 재사용성, 유지보수성, 우선순위, 사용 목적이 다르다.

---

### [핵심]

| 비교         | External CSS  | Internal CSS    | Inline Style         |
| ------------ | ------------- | --------------- | -------------------- |
| 위치         | 별도 CSS 파일 | HTML style 태그 | 요소 style attribute |
| 재사용성     | 높음          | 낮음            | 매우 낮음            |
| 유지보수     | 좋음          | 제한적          | 어려움               |
| 우선순위     | 일반 cascade  | 일반 cascade    | 높음                 |
| pseudo class | 가능          | 가능            | 직접 불가            |
| media query  | 가능          | 가능            | 직접 불가            |
| 적합         | 실무 프로젝트 | 데모/테스트     | 동적 값/임시         |

---

### [실무]

선택 기준:

```text
프로젝트 공통 style → External CSS
간단 테스트 → Internal CSS
동적 계산 값 전달 → Inline Style + CSS Variable
반복 Component style → External CSS / Component CSS
```

---

### [FAQ]

Q. External CSS와 Inline Style 중 뭐가 좋아?
A. 반복되고 재사용되는 style은 External CSS가 적합하다.

Q. Inline Style은 언제 써?
A. 동적으로 계산된 값 전달이나 매우 제한적인 one-off style에 사용한다.

Q. Inline Style로 pseudo class를 작성할 수 있어?
A. 일반 HTML inline style만으로는 어렵다.

---

## 14.2 Selector Comparison

### [개념]

Selector는 선택 기준에 따라 type, class, id, attribute, pseudo class, pseudo element로 나뉜다.

---

### [핵심]

| 비교           | 예시         | 목적                | 주의             |
| -------------- | ------------ | ------------------- | ---------------- |
| Type           | `button`     | 태그 전체 선택      | 범위 넓음        |
| Class          | `.button`    | component styling   | naming 중요      |
| ID             | `#main`      | 고유 요소 선택      | specificity 높음 |
| Attribute      | `[disabled]` | attribute 상태 선택 | 상태 동기화 필요 |
| Pseudo Class   | `:hover`     | 상태/조건 선택      | focus 고려       |
| Pseudo Element | `::before`   | 가상 요소/일부 선택 | content 필요     |

---

### [실무]

선택 기준:

```text
Base Style → Type Selector
Component Style → Class Selector
Label/ARIA 연결 → ID Attribute
State Style → Attribute Selector / Pseudo Class
Decoration → Pseudo Element
```

---

### [FAQ]

Q. Component style에는 어떤 selector가 좋아?
A. 일반적으로 class selector가 적합하다.

Q. State style에는 어떤 selector가 좋아?
A. pseudo class나 aria/data attribute selector를 사용할 수 있다.

Q. Decoration에는 어떤 selector가 좋아?
A. `::before`, `::after` 같은 pseudo element를 사용할 수 있다.

---

## 14.3 Descendant vs Child Selector

### [개념]

Descendant Selector는 모든 후손을 선택하고 Child Selector는 직접 자식만 선택한다.

---

### [핵심]

| 비교      | Descendant Selector | Child Selector       |
| --------- | ------------------- | -------------------- |
| 문법      | `.parent .child`    | `.parent > .child`   |
| 범위      | 모든 후손           | 직접 자식            |
| 구조 의존 | 상대적으로 낮음     | 높음                 |
| 위험      | 너무 넓게 적용      | wrapper 추가 시 깨짐 |
| 사용      | article content     | direct layout item   |

---

### [실무]

선택 기준:

```text
본문 내부 모든 p → Descendant Selector
nav-list 바로 아래 li → Child Selector
grid 바로 아래 item → Child Selector
nested component 보호 필요 → 더 명확한 class selector
```

---

### [FAQ]

Q. Descendant Selector와 Child Selector 차이는 뭐야?
A. Descendant는 모든 후손을 선택하고 Child는 직접 자식만 선택한다.

Q. Child Selector는 언제 써?
A. list item, grid item처럼 직접 자식 관계가 명확할 때 사용한다.

Q. Descendant Selector는 왜 조심해?
A. 깊은 nested component까지 영향을 줄 수 있기 때문이다.

---

## 14.4 Cascade vs Specificity vs Inheritance

### [개념]

Cascade, Specificity, Inheritance는 CSS 최종 style을 결정하는 핵심 개념이다.

---

### [핵심]

| 비교        | 의미                          | 예시               |
| ----------- | ----------------------------- | ------------------ |
| Cascade     | 여러 rule 중 최종값 결정      | 나중 rule 적용     |
| Specificity | selector 우선순위             | id > class > type  |
| Inheritance | 부모 property가 자식에게 전달 | color, font-family |

---

### [실무]

Debug 기준:

```text
값이 다른 rule에 덮임 → Cascade / Specificity
같은 selector인데 뒤 값 적용 → Source Order
부모 값이 자식에게 적용됨 → Inheritance
form font가 다름 → font inheritance 확인
```

---

### [FAQ]

Q. Cascade와 Specificity 차이는 뭐야?
A. Cascade는 최종 style 결정 전체 규칙이고 specificity는 그중 selector 우선순위 기준이다.

Q. Inheritance는 뭐야?
A. 일부 CSS property가 부모에서 자식으로 전달되는 동작이다.

Q. CSS 최종값은 어디서 확인해?
A. DevTools Computed 패널에서 확인한다.

---

# 15. Best Practice

## 15.1 CSS Syntax Selector Cascade Best Practice

### [개념]

CSS Syntax Selector Cascade Best Practice는 CSS를 예측 가능하고 유지보수 가능하게 작성하기 위한 기본 기준이다.

---

### [핵심]

권장 기준:

- External CSS 또는 역할별 CSS 파일 구조를 사용한다.
- selector는 class selector 중심으로 작성한다.
- ID selector styling을 피한다.
- 긴 descendant selector chain을 피한다.
- component root class로 scope를 잡는다.
- type selector는 reset/base style에 제한적으로 사용한다.
- attribute selector는 aria state, form state, data state에 활용한다.
- hover만 작성하지 말고 focus-visible을 함께 고려한다.
- pseudo element는 장식 목적 중심으로 사용한다.
- 중요한 정보는 CSS content에만 넣지 않는다.
- specificity를 낮게 유지한다.
- import 순서를 명확히 관리한다.
- `!important` 남용을 피한다.
- inheritance를 이해하고 form 요소 font inheritance를 정리한다.
- DevTools로 computed style을 확인한다.

---

### [실무]

권장 CSS 구조:

```css
@import "./tokens.css";
@import "./reset.css";
@import "./base.css";
@import "./components/button.css";
@import "./components/card.css";
```

권장 Component Selector:

```css
.button {
  display: inline-flex;
  align-items: center;
}

.button-primary {
  background-color: var(--color-primary);
}

.button:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}
```

검수 Checklist:

```md
- [ ] CSS 파일이 import되어 있는가?
- [ ] selector와 className이 일치하는가?
- [ ] property/value 오타가 없는가?
- [ ] class selector 중심으로 작성했는가?
- [ ] ID selector styling을 피했는가?
- [ ] selector chain이 과도하게 길지 않은가?
- [ ] import 순서가 의도와 맞는가?
- [ ] specificity가 과도하지 않은가?
- [ ] !important를 남용하지 않았는가?
- [ ] focus-visible style이 있는가?
- [ ] pseudo element에 중요한 정보만 넣지 않았는가?
- [ ] DevTools Computed에서 최종값을 확인했는가?
```

---

### [FAQ]

Q. CSS Syntax Selector Cascade Best Practice는 뭐야?
A. class selector 중심으로 낮은 specificity를 유지하고 import 순서와 cascade를 명확히 관리하는 것이다.

Q. CSS 검수에서 가장 먼저 볼 것은 뭐야?
A. CSS import, className/selector 일치, syntax error, computed style을 먼저 확인한다.

Q. CSS 구조를 유지보수하기 좋게 만들려면?
A. reset, base, token, component CSS를 역할별로 분리하고 selector specificity를 낮게 유지한다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 CSS syntax, selector, cascade, specificity 문제를 정확히 생성하고 검수하며 style 미적용 문제를 빠르게 디버깅하게 만드는 것이다.

---

# 16. Linkage Reference

## 16.1 Related Documents

### [개념]

Linkage Reference는 이 문서와 다른 HTML/CSS Foundation 문서의 역할을 구분하기 위한 참조 기준이다.

Part05는 CSS 문법, selector, cascade, specificity의 기초 기준 문서다.

---

### [핵심]

연계 기준:

- CSS Syntax, Selector, Cascade, Specificity의 기본 문법은 Part05에서 다룬다.
- Pseudo Class / Pseudo Element의 기본 문법은 Part05에서 다룬다.
- Interaction State, Form State, `:is()`, `:where()`, `:not()`, `::before`, `::after`, Transition과 연결되는 상세 기준은 Part12를 참조한다.
- CSS Variables와 token 기반 상태 관리는 Part12를 참조한다.
- Reset, Normalize, Base Style, CSS File Architecture는 Part13을 참조한다.
- Component State Styling 적용 예시는 Part14를 참조한다.
- Attribute, ARIA, Accessibility 상태 기준은 Part15를 참조한다.
- CSS Not Applied, Cascade Debugging, Review Checklist는 Part16을 참조한다.

---

### [실무]

문제 상황별 참조:

```text
CSS selector가 안 맞음 → Part05
Specificity 때문에 override됨 → Part05
Pseudo selector 상세 기준 필요 → Part12
Transition과 state styling 필요 → Part12
Reset/Base 구조 문제 → Part13
Button/Card/Form Component 상태 문제 → Part14
ARIA 상태와 접근성 attribute 문제 → Part15
전체 Troubleshooting Flow 필요 → Part16
```

---

### [FAQ]

Q. Part05는 어떤 문서야?
A. CSS syntax, selector, cascade, specificity의 기초 기준 문서다.

Q. Pseudo Class 상세 설명은 어디서 봐?
A. Part05는 기초 문법을 다루고 상세 interaction/state 기준은 Part12를 참조한다.

Q. CSS가 안 먹는 문제는 어디서 봐?
A. selector와 cascade 기초는 Part05, 전체 troubleshooting flow는 Part16을 참조한다.

Q. Component state styling은 어디서 봐?
A. selector 기초는 Part05, state selector 상세는 Part12, component 적용 예시는 Part14를 참조한다.

---

# Retrieval Queries

### [FAQ]

Q. CSS Syntax가 뭐야?
A. HTML 요소에 style을 적용하기 위해 selector, property, value를 작성하는 CSS 문법이다.

Q. CSS declaration은 뭐야?
A. `property: value;` 형태로 작성되는 한 줄의 style 선언이다.

Q. Rule Set이 뭐야?
A. selector와 declaration block을 합친 CSS 규칙 단위다.

Q. property 오타가 있으면 어떻게 돼?
A. 해당 declaration이 무시될 수 있다.

Q. External CSS가 뭐야?
A. 별도 CSS 파일을 만들어 HTML이나 JavaScript에서 불러와 style을 적용하는 방식이다.

Q. CSS import 순서가 중요한 이유는?
A. 같은 specificity라면 나중에 로드된 style이 이전 style을 덮어쓸 수 있기 때문이다.

Q. Internal CSS가 뭐야?
A. HTML 문서 내부의 style 태그에 CSS를 작성하는 방식이다.

Q. Inline Style이 뭐야?
A. HTML 요소의 style attribute에 CSS를 직접 작성하는 방식이다.

Q. Inline Style은 왜 조심해야 해?
A. 재사용성이 낮고 specificity가 높아 override가 어려워질 수 있기 때문이다.

Q. Selector가 뭐야?
A. CSS rule을 적용할 HTML 요소를 선택하는 문법이다.

Q. 실무에서 어떤 selector를 가장 많이 써?
A. 유지보수와 재사용성을 위해 class selector를 가장 많이 사용한다.

Q. 긴 selector chain은 왜 안 좋아?
A. HTML 구조 변경에 취약하고 specificity가 높아져 override가 어려워지기 때문이다.

Q. Type Selector가 뭐야?
A. HTML 태그 이름으로 요소를 선택하는 selector다.

Q. Type Selector는 언제 써?
A. reset, base style, 전역 typography 기준을 작성할 때 사용할 수 있다.

Q. Class Selector가 뭐야?
A. class attribute 값을 기준으로 요소를 선택하는 CSS selector다.

Q. Component Styling에는 어떤 selector가 좋아?
A. 일반적으로 class selector가 가장 적합하다.

Q. ID Selector가 뭐야?
A. id attribute 값을 기준으로 요소를 선택하는 CSS selector다.

Q. ID Selector를 styling에 많이 쓰면 왜 안 좋아?
A. specificity가 높아 override와 유지보수가 어려워지기 때문이다.

Q. Attribute Selector가 뭐야?
A. HTML attribute의 존재나 값을 기준으로 요소를 선택하는 CSS selector다.

Q. aria-invalid로 style을 줄 수 있어?
A. 가능하다. `[aria-invalid="true"]` selector로 오류 상태 style을 줄 수 있다.

Q. data attribute를 CSS selector로 써도 돼?
A. 가능하다. 다만 접근성 상태 전달은 ARIA attribute를 사용해야 한다.

Q. Descendant Selector가 뭐야?
A. 특정 요소 내부의 모든 후손 요소를 선택하는 selector다.

Q. Child Selector가 뭐야?
A. 특정 요소의 직접 자식만 선택하는 selector다.

Q. Descendant Selector와 Child Selector 차이는?
A. Child Selector는 직접 자식만 선택하고 Descendant Selector는 모든 후손을 선택한다.

Q. Group Selector가 뭐야?
A. 여러 selector에 같은 style을 적용하기 위해 comma로 묶는 selector다.

Q. Pseudo Class가 뭐야?
A. 요소의 상태나 조건을 기준으로 선택하는 CSS selector다.

Q. Pseudo Class는 어떤 기호를 써?
A. `:` 기호를 사용한다.

Q. hover는 pseudo class야?
A. 맞다. `:hover`는 pseudo class다.

Q. Pseudo Class 상세 기준은 어디서 다뤄?
A. Interaction, Form State, Structural Pseudo Class 상세 기준은 Part12에서 다룬다.

Q. focus-visible은 뭐야?
A. 브라우저가 focus 표시가 필요하다고 판단한 상태를 선택하는 pseudo class다.

Q. focus outline을 없애도 돼?
A. 제거만 하면 안 된다. 반드시 대체 focus-visible style을 제공해야 한다.

Q. Pseudo Element가 뭐야?
A. 요소의 특정 부분이나 가상 요소를 선택하는 CSS selector다.

Q. Pseudo Element는 어떤 기호를 써?
A. 일반적으로 `::` 기호를 사용한다.

Q. before와 after에는 content가 필요해?
A. 대부분 필요하다. content가 없으면 표시되지 않는 경우가 많다.

Q. Pseudo Element 상세 기준은 어디서 다뤄?
A. `::before`, `::after`, `::placeholder`, `::marker`, `::selection` 상세 기준은 Part12에서 다룬다.

Q. Cascade가 뭐야?
A. 여러 CSS rule이 충돌할 때 최종 style을 결정하는 CSS 규칙이다.

Q. Source Order가 뭐야?
A. CSS rule이 작성되거나 로드된 순서다.

Q. 같은 specificity면 어떤 rule이 이겨?
A. 나중에 작성되거나 로드된 rule이 우선 적용된다.

Q. Specificity가 뭐야?
A. CSS selector의 우선순위를 계산하는 기준이다.

Q. ID selector가 class selector보다 강해?
A. 맞다. ID selector는 class selector보다 specificity가 높다.

Q. !important는 뭐야?
A. CSS declaration의 우선순위를 강하게 높이는 키워드다.

Q. !important를 쓰면 문제가 해결돼?
A. 일시적으로 해결될 수 있지만 cascade 구조를 더 복잡하게 만들 수 있다.

Q. CSS Inheritance가 뭐야?
A. 일부 CSS property가 부모 요소에서 자식 요소로 전달되는 동작이다.

Q. color는 상속돼?
A. 일반적으로 상속된다.

Q. margin과 padding도 상속돼?
A. 아니다. margin과 padding은 일반적으로 상속되지 않는다.

Q. CSS Unit이 뭐야?
A. 크기, 간격, 비율을 표현하는 CSS 단위다.

Q. rem은 뭐야?
A. root font-size를 기준으로 하는 단위다.

Q. em은 뭐야?
A. 현재 요소 또는 부모 font-size를 기준으로 하는 단위다.

Q. CSS comment는 어떻게 작성해?
A. `/* comment */` 형태로 작성한다.

Q. CSS가 안 먹으면 무엇을 먼저 봐?
A. CSS 파일 import, className 오타, selector 매칭, DevTools Styles 패널을 먼저 본다.

Q. CSS rule이 DevTools에 보이는데 취소선이면?
A. 다른 rule에 의해 override된 것이다. specificity와 source order를 확인한다.

Q. CSS Syntax에서 가장 흔한 실수는 뭐야?
A. property 오타, value 단위 누락, brace/semicolon 누락, CSS import 누락이 흔하다.

Q. Selector에서 가장 흔한 실수는 뭐야?
A. className 오타, 실제 DOM과 맞지 않는 selector, 긴 descendant selector 남용이다.

Q. Cascade에서 가장 흔한 실수는 뭐야?
A. specificity와 source order를 고려하지 않고 style이 덮이는 문제를 놓치는 것이다.

Q. CSS Apply Method 차이는 뭐야?
A. External CSS는 별도 파일, Internal CSS는 style 태그, Inline Style은 요소 style attribute에 작성하는 방식이다.

Q. Component style에는 어떤 selector가 좋아?
A. 일반적으로 class selector가 적합하다.

Q. State style에는 어떤 selector가 좋아?
A. pseudo class나 aria/data attribute selector를 사용할 수 있다.

Q. Decoration에는 어떤 selector가 좋아?
A. `::before`, `::after` 같은 pseudo element를 사용할 수 있다.

Q. Descendant Selector와 Child Selector 차이는 뭐야?
A. Descendant는 모든 후손을 선택하고 Child는 직접 자식만 선택한다.

Q. Cascade와 Specificity 차이는 뭐야?
A. Cascade는 최종 style 결정 전체 규칙이고 specificity는 그중 selector 우선순위 기준이다.

Q. CSS Syntax Selector Cascade Best Practice는 뭐야?
A. class selector 중심으로 낮은 specificity를 유지하고 import 순서와 cascade를 명확히 관리하는 것이다.

Q. CSS 검수에서 가장 먼저 볼 것은 뭐야?
A. CSS import, className/selector 일치, syntax error, computed style을 먼저 확인한다.

Q. Part05는 어떤 문서야?
A. CSS syntax, selector, cascade, specificity의 기초 기준 문서다.

Q. Pseudo Class 상세 설명은 어디서 봐?
A. Part05는 기초 문법을 다루고 상세 interaction/state 기준은 Part12를 참조한다.

Q. CSS가 안 먹는 문제는 어디서 봐?
A. selector와 cascade 기초는 Part05, 전체 troubleshooting flow는 Part16을 참조한다.

Q. Component state styling은 어디서 봐?
A. selector 기초는 Part05, state selector 상세는 Part12, component 적용 예시는 Part14를 참조한다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 CSS syntax, selector, cascade, specificity 문제를 정확히 생성하고 검수하며 style 미적용 문제를 빠르게 디버깅하게 만드는 것이다.
