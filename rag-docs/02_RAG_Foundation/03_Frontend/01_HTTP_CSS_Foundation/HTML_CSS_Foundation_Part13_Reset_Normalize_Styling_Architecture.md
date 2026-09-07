# HTML CSS Foundation Part13 - Reset Normalize Styling Architecture

---

# 1. Document Role

## 1.1 Document Role Concept

### [개념]

이 문서는 CSS Reset, Normalize, Base Style, CSS File Architecture, Styling Architecture의 설계 기준을 다룬다.

Part13은 개별 component style 문서가 아니라, 프로젝트 전체 CSS 기반을 어떻게 초기화하고 구조화할지 정의하는 Architecture 문서다.

---

### [핵심]

문서 역할:

- CSS Reset 기준을 다룬다.
- Normalize와 Reset의 차이를 다룬다.
- Modern CSS Reset 기준을 다룬다.
- Base Style 작성 기준을 다룬다.
- Box Sizing Reset 기준을 다룬다.
- Media Element Reset 기준을 다룬다.
- Form Element Reset 기준을 다룬다.
- Link/List/Focus 기본 style 기준을 다룬다.
- CSS File Architecture 기준을 다룬다.
- Styling Architecture와 scope 관리 기준을 다룬다.
- Naming Convention과 Utility Class 기준을 다룬다.

연계 기준:

- CSS Syntax, Selector, Cascade, Specificity 기초는 Part05를 참조한다.
- Responsive Layout과 Media Query 기준은 Part10을 참조한다.
- CSS Variables와 Design Token 상세 기준은 Part12를 참조한다.
- Component Styling Practical Pattern은 Part14를 참조한다.
- Attribute, Accessibility, SEO 기준은 Part15를 참조한다.
- 실제 검수 단계의 Troubleshooting Flow와 Review Checklist는 Part16을 참조한다.

---

### [실무]

문서 사용 기준:

```text
브라우저 기본 스타일 차이 정리 필요 → Part13
reset.css / base.css 구조 설계 필요 → Part13
box-sizing / body margin / media reset 필요 → Part13
form element reset 필요 → Part13
focus-visible base style 필요 → Part13
CSS 파일 구조와 import 순서 필요 → Part13
component별 실전 패턴 필요 → Part14
최종 검수 checklist 필요 → Part16
```

---

### [FAQ]

Q. Part13은 어떤 문서야?
A. CSS Reset, Normalize, Base Style, CSS File Architecture, Styling Architecture의 설계 기준 문서다.

Q. Part13과 Part16 차이는 뭐야?
A. Part13은 구조 설계 문서이고 Part16은 최종 Troubleshooting과 Review Checklist 문서다.

Q. Component별 style 예시는 어디서 봐?
A. CSS 기반 구조는 Part13, Button/Card/Form 같은 component 적용 예시는 Part14를 참조한다.

Q. CSS Variables 상세 기준은 어디서 봐?
A. token과 scoped variable 상세 기준은 Part12를 참조한다.

---

# 2. CSS Reset

## 2.1 CSS Reset Concept

### [개념]

CSS Reset은 브라우저가 기본으로 제공하는 User Agent Style을 제거하거나 최소화해 프로젝트의 스타일 기준을 일관되게 만드는 CSS 초기화 방식이다.

브라우저마다 기본 margin, padding, font, form style, list style, heading style이 조금씩 다를 수 있다.

Reset은 이런 차이를 줄이고 Component Styling과 Layout을 예측 가능하게 만든다.

기본 예:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
}
```

---

### [핵심]

CSS Reset 핵심:

- 브라우저 기본 스타일 차이를 줄인다.
- 기본 margin과 padding을 정리한다.
- `box-sizing: border-box`를 전역 적용한다.
- body margin을 제거한다.
- img, picture, video 같은 media 요소의 overflow를 방지한다.
- button, input, textarea, select의 font 상속을 정리한다.
- list style 제거는 상황에 맞게 적용한다.
- 지나친 reset은 semantic 기본 표현까지 제거할 수 있다.
- reset 이후 base style을 반드시 다시 정의해야 한다.

---

### [실무]

2026 실무 기준에서 CSS Reset은 프로젝트 시작 시 가장 먼저 설계하는 스타일 기반이다.

Frontend Agent는 reset을 작성할 때 아래를 함께 고려해야 한다.

- Box Model 기준
- Body 기본 margin
- Typography 기본값
- Media element responsive 처리
- Form element font inheritance
- Button 기본 스타일
- Link 기본 스타일
- List 기본 스타일
- Reduced motion
- Accessibility preservation
- Component style과 충돌 여부

Reset 작성 Flow:

```text
Browser Default 확인
→ Reset 범위 결정
→ Box Sizing 적용
→ Body 기본값 설정
→ Media 기본값 설정
→ Form 기본값 설정
→ Accessibility 유지 확인
→ Base Style 작성
```

---

### [FAQ]

Q. CSS Reset이 뭐야?
A. 브라우저 기본 스타일을 제거하거나 줄여 프로젝트 스타일 기준을 일관되게 만드는 CSS 초기화 방식이다.

Q. CSS Reset은 왜 필요해?
A. 브라우저 기본 margin, padding, form style 차이로 인한 Layout 차이를 줄이기 위해 필요하다.

Q. Reset을 많이 하면 좋은 거야?
A. 아니다. 과도한 reset은 접근성이나 semantic 기본 표현을 해칠 수 있다.

Q. Reset 이후에는 무엇이 필요해?
A. body, heading, link, form, media 요소에 대한 base style을 다시 정의해야 한다.

---

# 3. Normalize

## 3.1 Normalize Concept

### [개념]

Normalize는 브라우저 기본 스타일을 완전히 제거하기보다 브라우저 간 차이를 줄이고 유용한 기본 스타일은 유지하는 CSS 초기화 방식이다.

Reset이 “기본 스타일 제거”에 가깝다면 Normalize는 “기본 스타일 표준화”에 가깝다.

---

### [핵심]

Normalize 핵심:

- 브라우저 간 기본 스타일 차이를 줄인다.
- 유용한 기본 스타일을 유지한다.
- reset보다 보수적인 접근이다.
- heading, list, form 등 기본 의미 표현을 일부 유지할 수 있다.
- 프로젝트 성격에 따라 reset보다 적합할 수 있다.
- Modern CSS Reset과 함께 일부 normalize 개념을 섞어 사용한다.

---

### [실무]

실무에서는 완전한 reset 또는 normalize만 선택하기보다 “Modern CSS Reset + Base Style” 형태를 많이 사용한다.

선택 기준:

```text
Design System 기반 UI → Reset 성향 강함
문서 중심 콘텐츠 → Normalize 성향 유리
Component Library → Reset + Base Token
Markdown / Article Page → Normalize + Prose Style
```

검수 기준:

- 프로젝트가 문서 중심인가 UI 중심인가?
- 기본 heading/list style을 유지해야 하는가?
- component style을 완전히 통제해야 하는가?
- reset 후 base style이 충분히 정의되어 있는가?
- normalize 성격이 component style과 충돌하지 않는가?

---

### [FAQ]

Q. Normalize가 뭐야?
A. 브라우저 기본 스타일을 완전히 없애기보다 브라우저 간 차이를 줄여 일관되게 만드는 방식이다.

Q. Reset과 Normalize 차이는 뭐야?
A. Reset은 기본 스타일 제거에 가깝고 Normalize는 유용한 기본 스타일을 유지하며 차이를 줄이는 방식이다.

Q. 실무에서는 Reset과 Normalize 중 하나만 써?
A. 꼭 그렇지 않다. Modern Reset과 Base Style을 조합하는 경우가 많다.

Q. 문서 중심 페이지에는 뭐가 좋아?
A. heading, list, paragraph 기본 표현을 유지하기 쉬운 Normalize 성향이 유리할 수 있다.

---

# 4. Modern CSS Reset

## 4.1 Modern Reset Concept

### [개념]

Modern CSS Reset은 과거처럼 모든 기본 스타일을 강하게 제거하기보다, Layout 예측 가능성과 접근성을 유지하면서 필요한 기본값만 정리하는 현대적 reset 방식이다.

---

### [핵심]

Modern Reset 핵심:

- 전역 `box-sizing: border-box` 적용
- body margin 제거
- media element responsive 처리
- form element font inheritance
- text rendering과 line-height 기본값 설정
- hidden attribute 존중
- reduced motion 고려
- semantic element의 의미는 유지
- focus outline 제거 금지
- list reset은 class 기반으로 제한 가능

---

### [실무]

Modern Reset 예:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  min-height: 100dvh;
  font-family:
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    sans-serif;
  line-height: 1.5;
}

img,
picture,
svg,
video,
canvas {
  display: block;
  max-width: 100%;
}

button,
input,
textarea,
select {
  font: inherit;
}

[hidden] {
  display: none !important;
}
```

주의:

```css
*:focus {
  outline: none;
}
```

위 코드는 keyboard accessibility를 해칠 수 있으므로 금지한다.

검수 기준:

- focus outline을 제거하지 않았는가?
- reset 이후 body typography가 정의되어 있는가?
- media 요소가 부모를 넘지 않는가?
- form 요소가 font를 상속하는가?
- hidden attribute가 정상 동작하는가?
- reset이 component style보다 먼저 로드되는가?

---

### [FAQ]

Q. Modern CSS Reset이 뭐야?
A. Layout 예측 가능성과 접근성을 유지하면서 필요한 기본값만 정리하는 현대적 reset 방식이다.

Q. Modern Reset에서 가장 중요한 것은 뭐야?
A. `box-sizing: border-box`, body margin 제거, media responsive 처리, form font 상속, focus 접근성 유지다.

Q. focus outline을 reset에서 없애도 돼?
A. 안 된다. 제거만 하면 keyboard 사용자가 현재 위치를 알 수 없다.

Q. img max-width 100%는 왜 reset에 넣어?
A. 이미지가 부모 너비를 넘어 가로 스크롤을 만드는 문제를 줄이기 위해서다.

---

# 5. Base Style

## 5.1 Base Style Concept

### [개념]

Base Style은 Reset 이후 프로젝트 전체에 적용되는 기본 스타일이다.

Reset이 브라우저 기본값을 정리한다면, Base Style은 프로젝트의 기본 typography, color, background, link, form, media 기준을 다시 정의한다.

---

### [핵심]

Base Style 핵심:

- reset 이후 반드시 필요하다.
- body 기본 font, color, background를 정의한다.
- heading 기본 line-height와 margin 전략을 정한다.
- paragraph 기본 margin 전략을 정한다.
- link 기본 색상과 underline을 정한다.
- form element 기본 font와 focus style을 정한다.
- media element 기본 responsive 규칙을 정한다.
- design token을 사용해 일관성을 유지한다.

---

### [실무]

Base Style 예:

```css
:root {
  --font-sans:
    system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --color-text: #111827;
  --color-background: #ffffff;
  --color-link: #2563eb;
}

body {
  font-family: var(--font-sans);
  color: var(--color-text);
  background-color: var(--color-background);
}

a {
  color: var(--color-link);
  text-decoration-thickness: 0.08em;
  text-underline-offset: 0.16em;
}

:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}
```

검수 기준:

- reset 이후 typography가 다시 정의되어 있는가?
- body color와 background가 정의되어 있는가?
- link가 링크처럼 보이는가?
- focus-visible 기본 스타일이 있는가?
- base style이 component style을 과도하게 침범하지 않는가?
- token 기반으로 작성되었는가?

---

### [FAQ]

Q. Base Style이 뭐야?
A. Reset 이후 프로젝트 전체에 적용되는 기본 typography, color, link, form, media 스타일이다.

Q. Reset만 하면 안 돼?
A. 안 된다. Reset은 기본값을 정리할 뿐이고 프로젝트 기준 스타일은 Base Style로 다시 정의해야 한다.

Q. Base Style에는 무엇이 들어가?
A. body, heading, paragraph, link, form, media, focus-visible 기본 스타일이 들어갈 수 있다.

Q. Base Style과 Component Style 차이는?
A. Base Style은 전체 기본값이고 Component Style은 특정 UI 단위의 구체적 스타일이다.

---

# 6. Box Sizing Architecture

## 6.1 box-sizing Strategy

### [개념]

Box Sizing Architecture는 프로젝트 전체의 width, padding, border 계산 방식을 일관되게 만드는 스타일 기준이다.

실무에서는 대부분 `box-sizing: border-box`를 전역 적용한다.

---

### [핵심]

Box Sizing 핵심:

- `content-box`는 width에 padding과 border가 추가된다.
- `border-box`는 width 안에 padding과 border가 포함된다.
- 전역 border-box는 Layout 계산을 단순하게 만든다.
- pseudo element에도 box-sizing을 적용해야 한다.
- form, card, grid item overflow 문제를 줄인다.
- reset 초기 단계에서 정의한다.

예:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

---

### [실무]

권장 방식:

```css
html {
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: inherit;
}
```

또는:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

검수 기준:

- pseudo element까지 box-sizing이 적용되는가?
- width 100% input이 padding 때문에 넘치지 않는가?
- border 추가로 layout이 흔들리지 않는가?
- 외부 library와 충돌하지 않는가?
- reset 파일의 초반에 선언되어 있는가?

---

### [FAQ]

Q. box-sizing border-box는 왜 전역으로 써?
A. width 안에 padding과 border가 포함되어 요소 크기 계산이 예측 가능해지기 때문이다.

Q. pseudo element에도 box-sizing이 필요해?
A. 필요하다. `*::before`, `*::after`에도 적용해야 가상 요소 크기 계산이 일관된다.

Q. border-box를 쓰면 모든 overflow가 사라져?
A. 아니다. 고정 width, 긴 텍스트, 이미지, table overflow는 별도 대응이 필요하다.

---

# 7. Media Element Reset

## 7.1 Image Video SVG Reset

### [개념]

Media Element Reset은 이미지, 비디오, SVG, canvas 같은 media 요소가 부모 영역을 넘지 않고 예측 가능하게 표시되도록 기본 스타일을 설정하는 것이다.

---

### [핵심]

Media Reset 핵심:

- `max-width: 100%`로 부모 너비를 넘지 않게 한다.
- `height: auto`로 이미지 비율을 유지한다.
- `display: block`으로 inline image 하단 공백을 줄인다.
- SVG도 부모 크기에 맞게 제한할 수 있다.
- 의미 있는 이미지는 HTML `img`와 alt를 사용한다.
- 장식 이미지는 CSS background 또는 빈 alt를 고려한다.

예:

```css
img,
picture,
video,
canvas,
svg {
  display: block;
  max-width: 100%;
}
```

---

### [실무]

이미지 기본값:

```css
img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

SVG Icon 예:

```css
svg {
  flex-shrink: 0;
}
```

검수 기준:

- 이미지가 부모를 넘지 않는가?
- 이미지 비율이 깨지지 않는가?
- inline image 하단 공백이 의도한 것인가?
- SVG icon이 flex layout에서 찌그러지지 않는가?
- alt 처리 기준이 HTML 문서와 일치하는가?

---

### [FAQ]

Q. Media Element Reset이 뭐야?
A. 이미지, 비디오, SVG 등이 부모 영역을 넘지 않도록 기본 스타일을 정리하는 것이다.

Q. img에 max-width 100%를 주는 이유는?
A. 원본 이미지가 부모보다 클 때 가로 overflow를 막기 위해서다.

Q. img display block은 왜 써?
A. inline image에서 생길 수 있는 하단 공백을 줄이기 위해 사용한다.

Q. SVG에도 reset이 필요해?
A. icon이나 responsive media로 사용할 때 크기와 flex shrink 문제를 관리하기 위해 필요할 수 있다.

---

# 8. Form Element Reset

## 8.1 Form Reset Concept

### [개념]

Form Element Reset은 input, textarea, select, button 같은 Form 요소의 브라우저 기본 스타일 차이를 줄이고 프로젝트 typography와 일관되게 만드는 초기화 기준이다.

---

### [핵심]

Form Reset 핵심:

- form 요소는 브라우저 기본 font를 가질 수 있다.
- `font: inherit`으로 body typography를 상속하게 만들 수 있다.
- button 기본 appearance는 브라우저마다 다를 수 있다.
- input height는 font, line-height, padding, border 영향을 받는다.
- focus style은 제거하지 않는다.
- disabled 상태는 시각적으로 구분해야 한다.
- form reset 후 component style에서 세부 디자인을 정의한다.

예:

```css
button,
input,
textarea,
select {
  font: inherit;
}
```

---

### [실무]

Button Reset 예:

```css
button {
  font: inherit;
}

button:not(:disabled) {
  cursor: pointer;
}
```

Form Control 예:

```css
input,
textarea,
select {
  font: inherit;
  color: inherit;
}

textarea {
  resize: vertical;
}
```

검수 기준:

- form 요소가 body font를 상속하는가?
- button cursor가 상태에 맞게 표시되는가?
- disabled button에 pointer cursor가 남아 있지 않은가?
- focus-visible이 유지되는가?
- textarea resize 정책이 명확한가?
- placeholder를 label 대신 쓰지 않는가?

---

### [FAQ]

Q. Form Reset이 뭐야?
A. input, textarea, select, button의 브라우저 기본 스타일 차이를 줄이는 초기화 기준이다.

Q. form 요소에 font inherit을 주는 이유는?
A. button과 input이 body font와 다르게 보이는 문제를 줄이기 위해서다.

Q. button focus outline을 없애도 돼?
A. 안 된다. 제거하려면 반드시 대체 focus-visible 스타일을 제공해야 한다.

Q. disabled button에도 cursor pointer를 줘도 돼?
A. 권장하지 않는다. disabled는 조작 불가 상태가 명확해야 한다.

---

# 9. List Reset

## 9.1 List Reset Concept

### [개념]

List Reset은 `ul`, `ol`, `li`의 기본 margin, padding, marker를 정리하는 방식이다.

Navigation, Menu, Card List처럼 시각적으로 marker가 필요 없는 목록에서 자주 사용한다.

---

### [핵심]

List Reset 핵심:

- list semantics는 유지하면서 시각 marker만 제거할 수 있다.
- 모든 list를 전역으로 reset하면 문서 콘텐츠의 목록 표현이 사라질 수 있다.
- class 기반 reset이 안전하다.
- navigation list, menu list, card list에 적합하다.
- article body나 markdown content의 목록은 marker를 유지하는 것이 좋다.

전역 reset 주의:

```css
ul,
ol {
  list-style: none;
  margin: 0;
  padding: 0;
}
```

Class 기반 권장:

```css
.list-unstyled {
  list-style: none;
  margin: 0;
  padding: 0;
}
```

---

### [실무]

Navigation 예:

```html
<ul class="nav-list list-unstyled">
  <li><a href="/festivals">Festivals</a></li>
  <li><a href="/calendar">Calendar</a></li>
</ul>
```

```css
.list-unstyled {
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-list {
  display: flex;
  gap: 16px;
}
```

검수 기준:

- list semantics는 유지되는가?
- marker 제거가 필요한 UI인가?
- article content list까지 marker가 사라지지 않는가?
- navigation에는 ul/li 구조가 유지되는가?
- list 간격은 gap 또는 prose style로 관리되는가?

---

### [FAQ]

Q. List Reset이 뭐야?
A. ul, ol의 기본 marker, margin, padding을 정리하는 방식이다.

Q. 모든 ul ol을 전역 reset해도 돼?
A. 주의해야 한다. 문서 본문의 목록 의미 표현까지 사라질 수 있다.

Q. marker 없는 nav list는 어떻게 만들어?
A. ul/li semantic은 유지하고 `list-style: none`, margin/padding reset을 class로 적용한다.

Q. list semantics와 list marker는 같은 거야?
A. 아니다. semantics는 HTML 구조이고 marker는 시각 표현이다.

---

# 10. Link Reset and Base

## 10.1 Link Style

### [개념]

Link Style은 `a` 요소의 기본 색상, 밑줄, hover, focus 상태를 정의하는 스타일 기준이다.

Link는 사용자가 이동 가능한 텍스트임을 명확히 인식할 수 있어야 한다.

---

### [핵심]

Link Style 핵심:

- 링크는 링크처럼 보여야 한다.
- underline 제거 시 다른 명확한 식별 단서가 필요하다.
- 색상만으로 링크를 구분하면 접근성 문제가 생길 수 있다.
- hover 상태만으로 링크를 구분하면 안 된다.
- focus-visible 상태가 필요하다.
- text link와 nav link는 스타일 목적이 다를 수 있다.

---

### [실무]

Base Link 예:

```css
a {
  color: var(--color-link);
  text-decoration-thickness: 0.08em;
  text-underline-offset: 0.16em;
}

a:hover {
  text-decoration-thickness: 0.12em;
}

a:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}
```

Navigation Link 예:

```css
.nav-link {
  text-decoration: none;
}

.nav-link[aria-current="page"] {
  font-weight: var(--font-semibold);
}
```

검수 기준:

- text link가 기본 상태에서 링크로 인식되는가?
- hover 없이도 링크 구분이 가능한가?
- focus-visible이 보이는가?
- nav link와 prose link 스타일 책임이 분리되는가?
- aria-current 같은 현재 페이지 표시가 있는가?

---

### [FAQ]

Q. Link Reset은 왜 조심해야 해?
A. 밑줄과 색상을 제거하면 사용자가 링크를 인식하기 어려워질 수 있기 때문이다.

Q. 링크 underline을 없애도 돼?
A. navigation처럼 문맥상 명확한 경우 가능하지만 text link에서는 대체 단서가 필요하다.

Q. 링크 focus style은 왜 필요해?
A. 키보드 사용자가 현재 선택된 링크를 알 수 있어야 하기 때문이다.

Q. 현재 페이지 nav link는 어떻게 표시해?
A. `aria-current="page"`와 시각 스타일을 함께 사용할 수 있다.

---

# 11. Focus Style Architecture

## 11.1 Focus Style Concept

### [개념]

Focus Style Architecture는 keyboard 사용자가 현재 조작 위치를 명확히 알 수 있도록 focus-visible 스타일을 일관되게 설계하는 기준이다.

Focus Style은 접근성 품질의 핵심이다.

---

### [핵심]

Focus Style 핵심:

- focus outline을 제거만 하면 안 된다.
- `:focus-visible`을 사용해 keyboard focus 표시를 제공한다.
- focus ring은 배경과 충분히 구분되어야 한다.
- interactive element에 일관된 focus style이 필요하다.
- overflow hidden 부모가 focus ring을 자를 수 있다.
- fixed header가 focus target을 가릴 수 있다.
- focus style은 theme와 contrast를 고려해야 한다.

---

### [실무]

전역 Focus Style 예:

```css
:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}
```

Component Focus 예:

```css
.button:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 3px;
}

.input:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

검수 기준:

- keyboard Tab 이동 시 focus가 보이는가?
- outline을 제거만 하지 않았는가?
- focus ring이 배경과 구분되는가?
- overflow hidden으로 focus ring이 잘리지 않는가?
- dark mode에서도 focus가 보이는가?
- disabled element에 focus가 가지 않는가?

---

### [FAQ]

Q. Focus Style Architecture가 뭐야?
A. keyboard 사용자가 현재 조작 위치를 알 수 있도록 focus-visible 스타일을 일관되게 설계하는 기준이다.

Q. outline none을 써도 돼?
A. 제거만 하면 안 된다. 반드시 대체 focus style을 제공해야 한다.

Q. focus와 focus-visible 차이는 뭐야?
A. focus는 모든 focus 상태이고 focus-visible은 브라우저가 표시가 필요하다고 판단한 focus 상태다.

Q. focus ring이 잘리면 무엇을 확인해?
A. 부모 overflow hidden, outline-offset, z-index, component clipping 구조를 확인한다.

---

# 12. CSS File Architecture

## 12.1 CSS File Structure

### [개념]

CSS File Architecture는 CSS 파일을 역할에 따라 분리하고 로드 순서를 정해 유지보수성을 높이는 구조 설계다.

무작위로 하나의 CSS 파일에 모든 스타일을 작성하면 cascade 충돌, 중복, override 문제가 증가한다.

---

### [핵심]

CSS File Architecture 핵심:

- reset은 가장 먼저 로드한다.
- token은 base와 component에서 참조할 수 있어야 한다.
- base style은 reset 이후 로드한다.
- layout style은 page structure를 담당한다.
- component style은 독립적인 UI 단위를 담당한다.
- utility style은 제한적으로 사용한다.
- page style은 특정 화면 전용 스타일이다.
- CSS import 순서는 cascade에 영향을 준다.

예시 구조:

```text
styles/
├ reset.css
├ tokens.css
├ base.css
├ layout.css
├ utilities.css
└ components/
  ├ button.css
  ├ card.css
  └ form.css
```

---

### [실무]

권장 로드 순서:

```css
@import "./tokens.css";
@import "./reset.css";
@import "./base.css";
@import "./layout.css";
@import "./utilities.css";
@import "./components/button.css";
@import "./components/card.css";
```

주의:

- token은 reset보다 먼저 둬도 되고 base 전에만 참조 가능하면 된다.
- reset이 component style 뒤에 로드되면 component style을 깨뜨릴 수 있다.
- page-specific override는 마지막에 로드될 수 있으나 남용하지 않는다.

검수 기준:

- reset/base/component 역할이 분리되어 있는가?
- CSS 로드 순서가 cascade 의도와 맞는가?
- component style이 전역 selector에 과도하게 의존하지 않는가?
- page style이 component 내부를 지나치게 override하지 않는가?
- 중복 selector가 많은가?

---

### [FAQ]

Q. CSS File Architecture가 뭐야?
A. reset, token, base, layout, component, utility, page style을 역할별로 분리하는 구조 설계다.

Q. CSS 파일 로드 순서는 중요해?
A. 중요하다. 나중에 로드된 CSS가 같은 specificity의 이전 스타일을 덮어쓸 수 있다.

Q. reset은 언제 로드해야 해?
A. 일반적으로 component style보다 먼저 로드해야 한다.

Q. 모든 CSS를 한 파일에 넣어도 돼?
A. 작은 예제는 가능하지만 프로젝트가 커지면 유지보수와 충돌 관리가 어려워진다.

---

# 13. Styling Architecture

## 13.1 Styling Architecture Concept

### [개념]

Styling Architecture는 CSS를 작성하는 규칙, naming, 파일 구조, component 책임, token 사용, cascade 관리 기준을 정하는 설계다.

목표는 스타일 충돌을 줄이고 Component 재사용성과 Review 가능성을 높이는 것이다.

---

### [핵심]

Styling Architecture 핵심:

- 역할별 CSS Layer를 구분한다.
- reset과 base를 분리한다.
- token 기반으로 반복 값을 관리한다.
- component class를 명확히 작성한다.
- 전역 selector 남용을 피한다.
- ID selector styling을 피한다.
- specificity를 낮게 유지한다.
- utility class 사용 범위를 정한다.
- page-specific override를 최소화한다.
- naming convention을 일관되게 유지한다.

---

### [실무]

Layer 전략:

```text
Tokens → Reset → Base → Layout → Components → Utilities → Page Overrides
```

Component 중심 예:

```css
.festival-card {
  padding: var(--space-6);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
}

.festival-card-title {
  margin: 0;
  font-size: var(--text-xl);
}

.festival-card-description {
  margin-block-start: var(--space-2);
}
```

피해야 할 예:

```css
main section div article h2 {
  font-size: 24px;
}

#festivalCardTitle {
  color: blue;
}
```

검수 기준:

- style 책임이 reset/base/component/page로 분리되어 있는가?
- component class가 역할 기반인가?
- selector chain이 길지 않은가?
- ID selector로 styling하지 않았는가?
- token 없이 임의 값이 반복되지 않는가?
- component가 page style에 과도하게 의존하지 않는가?

---

### [FAQ]

Q. Styling Architecture가 뭐야?
A. CSS 작성 규칙, 파일 구조, naming, token, component 책임, cascade 관리 기준을 정하는 설계다.

Q. Styling Architecture가 왜 필요해?
A. 스타일 충돌을 줄이고 Component 재사용성과 유지보수성을 높이기 위해 필요하다.

Q. 좋은 CSS 구조의 기준은 뭐야?
A. reset, base, token, layout, component 역할이 분리되고 specificity가 낮으며 token 기반으로 작성된 구조다.

Q. 긴 selector chain은 왜 문제야?
A. HTML 구조 변경에 취약하고 specificity가 높아져 override가 어려워지기 때문이다.

---

# 14. Naming Convention

## 14.1 Class Naming

### [개념]

Class Naming은 CSS class 이름을 일관된 규칙으로 작성하는 방식이다.

좋은 class naming은 Component의 역할과 구조를 명확히 표현하고 검색성과 유지보수성을 높인다.

---

### [핵심]

Class Naming 핵심:

- 역할 기반 이름을 사용한다.
- 색상이나 크기 같은 변하기 쉬운 이름을 피한다.
- component prefix를 사용하면 충돌을 줄일 수 있다.
- 너무 축약된 이름은 피한다.
- 너무 긴 이름도 피한다.
- 상태 class는 명확하게 작성한다.
- React에서는 `className`과 CSS selector가 정확히 일치해야 한다.

좋은 예:

```css
.festival-card
.festival-card-title
.festival-card-description
.festival-card-actions
.button-primary
.form-field-error
```

나쁜 예:

```css
.blue-box
.big-text
.abc
.box1
.left
```

---

### [실무]

Component Naming 예:

```html
<article class="festival-card festival-card-featured">
  <h2 class="festival-card-title">Seoul Light Festival</h2>
  <p class="festival-card-description">Night festival in Seoul.</p>
</article>
```

```css
.festival-card {
  padding: var(--space-6);
}

.festival-card-featured {
  border-color: var(--color-primary);
}

.festival-card-title {
  font-size: var(--text-xl);
}
```

검수 기준:

- class name이 역할과 의미를 표현하는가?
- 색상, 위치, 크기 기반 이름에 의존하지 않는가?
- component 단위 prefix가 있는가?
- 상태와 variant class가 명확한가?
- className 오타가 없는가?

---

### [FAQ]

Q. CSS class 이름은 어떻게 지어야 해?
A. 색상이나 크기보다 component 역할과 의미 중심으로 짓는 것이 좋다.

Q. blue-box 같은 이름은 왜 안 좋아?
A. 색상이 바뀌면 이름과 실제 스타일이 맞지 않아 유지보수성이 떨어지기 때문이다.

Q. component prefix는 왜 써?
A. class 충돌을 줄이고 어떤 component의 style인지 검색하기 쉽게 하기 위해서다.

Q. React에서 class 이름 검수는 무엇이 중요해?
A. JSX의 className과 CSS selector 이름이 정확히 일치해야 한다.

---

# 15. Utility Class

## 15.1 Utility Class Concept

### [개념]

Utility Class는 하나의 작은 스타일 목적을 가진 재사용 class다.

예를 들어 visually-hidden, container, text-center, list-unstyled 같은 class가 utility class가 될 수 있다.

---

### [핵심]

Utility Class 핵심:

- 작은 단일 목적 스타일을 제공한다.
- 반복되는 보조 스타일에 유용하다.
- 과도한 utility 남용은 HTML class가 복잡해질 수 있다.
- component style과 utility style 책임을 구분해야 한다.
- 접근성 utility는 프로젝트 전역에서 유용하다.
- reset을 보완하는 용도로 사용할 수 있다.

대표 utility:

```css
.visually-hidden
.container
.list-unstyled
.text-center
.flow
.cluster
.stack
```

---

### [실무]

Visually Hidden 예:

```css
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}
```

Container 예:

```css
.container {
  width: min(100% - 32px, 1120px);
  margin-inline: auto;
}
```

Stack Utility 예:

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}
```

검수 기준:

- utility가 단일 목적을 가지는가?
- component style로 작성해야 할 것을 utility로 과도하게 조립하지 않았는가?
- utility naming이 명확한가?
- accessibility utility가 안전하게 작성되었는가?
- utility가 component style을 예측 불가능하게 override하지 않는가?

---

### [FAQ]

Q. Utility Class가 뭐야?
A. 하나의 작은 스타일 목적을 가진 재사용 CSS class다.

Q. visually-hidden은 언제 써?
A. 화면에는 숨기지만 스크린 리더에는 제공해야 하는 텍스트에 사용한다.

Q. utility class는 많이 쓸수록 좋아?
A. 아니다. 과도하면 HTML class가 복잡해지고 component 책임이 흐려질 수 있다.

Q. list-unstyled는 utility class로 괜찮아?
A. 괜찮다. marker 없는 list UI를 재사용하기 좋다.

---

# 16. CSS Scope and Cascade Management

## 16.1 Scope Strategy

### [개념]

CSS Scope Strategy는 특정 스타일이 어디까지 영향을 미치게 할지 정하는 방식이다.

CSS는 기본적으로 전역 cascade를 가지므로 scope를 관리하지 않으면 스타일 충돌이 쉽게 발생한다.

---

### [핵심]

Scope 핵심:

- 전역 스타일은 최소화한다.
- Base Style은 HTML element 기본값만 담당한다.
- Component Style은 component class 기준으로 제한한다.
- Page Style은 특정 page wrapper 내부로 제한한다.
- Utility Class는 단일 목적만 수행한다.
- ID selector는 styling scope로 사용하지 않는다.
- 긴 descendant selector는 피한다.
- 낮은 specificity를 유지한다.

---

### [실무]

Component Scope 예:

```css
.festival-card {
}

.festival-card-title {
}

.festival-card-description {
}
```

Page Scope 예:

```css
.festival-page .filter-panel {
}
```

주의:

```css
body .page main section article div h2 {
}
```

검수 기준:

- style이 예상보다 넓게 적용되지 않는가?
- 전역 selector가 component를 깨뜨리지 않는가?
- page-specific style이 다른 page에 영향을 주지 않는가?
- component style이 독립적으로 재사용 가능한가?
- selector specificity가 낮게 유지되는가?

---

### [FAQ]

Q. CSS Scope Strategy가 뭐야?
A. CSS 스타일이 어디까지 영향을 미치게 할지 정해 충돌을 줄이는 방식이다.

Q. CSS는 기본적으로 scope가 있어?
A. 일반 CSS는 기본적으로 전역 cascade를 가지므로 명시적 class와 구조로 scope를 관리해야 한다.

Q. 전역 selector를 많이 쓰면 왜 문제야?
A. 의도하지 않은 component까지 영향을 주고 override 문제가 늘어나기 때문이다.

Q. Component style은 어떻게 scope를 잡아?
A. component root class와 하위 element class를 기준으로 작성한다.

---

# 17. Common Mistakes

## 17.1 Reset Normalize Styling Architecture Common Mistakes

### [개념]

Reset, Normalize, Styling Architecture 실수는 브라우저별 차이, 접근성 저하, CSS 충돌, Component 재사용성 저하, 유지보수 어려움으로 이어진다.

---

### [핵심]

자주 발생하는 실수:

- Reset 없이 브라우저 기본 margin 차이를 방치
- Reset만 하고 Base Style을 정의하지 않음
- focus outline을 제거하고 대체 focus style을 제공하지 않음
- 모든 ul/ol을 전역 reset해 article list marker까지 제거
- img max-width reset 누락
- form element font inheritance 누락
- button disabled 상태 cursor 처리 누락
- reset을 component CSS 뒤에 로드
- CSS 파일 구조 없이 모든 스타일을 한 파일에 누적
- token 없이 임의 hex, spacing 값 반복
- ID selector로 styling
- 긴 selector chain 사용
- page style이 component 내부를 과도하게 override
- class naming이 색상, 크기, 위치 중심
- utility class를 과도하게 남용
- visually-hidden을 display none으로 작성
- CSS import 순서가 cascade 의도와 다름

---

### [실무]

Troubleshooting Flow:

```text
Style Architecture Bug
→ Reset 로드 여부 확인
→ Base Style 존재 확인
→ Focus Style 확인
→ Box Sizing 확인
→ Media / Form Reset 확인
→ CSS 파일 순서 확인
→ Selector Specificity 확인
→ Token 사용 여부 확인
→ Component Scope 확인
→ 최종 Review Checklist 확인
```

문제 예:

```text
문제: 브라우저마다 body 여백이 다르게 보임
원인: body margin reset 누락
해결: body { margin: 0; } 적용
```

```text
문제: 키보드로 버튼 위치를 알 수 없음
원인: outline none만 적용
해결: focus-visible 대체 스타일 제공
```

```text
문제: 게시글 본문 목록의 bullet이 사라짐
원인: 모든 ul/ol 전역 list reset
해결: list-unstyled utility로 필요한 list에만 적용
```

검수 기준:

- 구조 설계 문제는 Part13 기준으로 확인했는가?
- 최종 검수 항목은 Part16 Checklist와 연결했는가?
- CSS Variables와 token 문제는 Part12 기준과 연결했는가?
- Component 적용 문제는 Part14 기준과 연결했는가?

---

### [FAQ]

Q. Reset에서 가장 흔한 실수는 뭐야?
A. focus outline을 제거하거나 reset 후 base style을 다시 정의하지 않는 것이다.

Q. Styling Architecture에서 가장 흔한 실수는 뭐야?
A. 역할 분리 없이 한 파일에 모든 스타일을 누적하고 selector specificity를 계속 높이는 것이다.

Q. List Reset에서 가장 흔한 실수는 뭐야?
A. 모든 ul/ol을 전역 reset해 문서 본문 목록 marker까지 제거하는 것이다.

Q. CSS 구조 문제는 어떤 순서로 디버깅해?
A. reset, base, focus, box sizing, media/form reset, 파일 순서, selector specificity, token, scope 순서로 확인한다.

---

# 18. Comparison Rules

## 18.1 Reset vs Normalize

### [개념]

Reset은 브라우저 기본 스타일을 제거하는 성격이 강하고 Normalize는 브라우저 간 차이를 줄이면서 유용한 기본 스타일을 유지하는 성격이 강하다.

---

### [핵심]

| 비교      | Reset               | Normalize               |
| --------- | ------------------- | ----------------------- |
| 목적      | 기본 스타일 제거    | 브라우저 차이 표준화    |
| 강도      | 강함                | 보수적                  |
| 기본 표현 | 많이 제거           | 일부 유지               |
| 적합      | Component UI        | 문서 중심 콘텐츠        |
| 주의      | Base Style 필요     | 기본 스타일과 충돌 가능 |
| 실무 조합 | Modern Reset + Base | Normalize + Prose       |

---

### [실무]

선택 기준:

```text
Design System UI → Reset 성향
Article / Markdown → Normalize 성향
React Component App → Modern Reset + Base Style
Landing Page → Reset + Token + Base
```

---

### [FAQ]

Q. Reset과 Normalize 차이는 뭐야?
A. Reset은 기본 스타일 제거에 가깝고 Normalize는 브라우저 차이를 줄이되 유용한 기본 스타일을 유지한다.

Q. React App에는 뭐가 좋아?
A. 보통 Modern Reset과 Base Style 조합이 적합하다.

Q. 문서 중심 페이지에는 뭐가 좋아?
A. Normalize 성향 또는 Prose Style을 함께 사용하는 방식이 적합할 수 있다.

---

## 18.2 Reset vs Base Style

### [개념]

Reset은 브라우저 기본 스타일을 정리하는 역할이고 Base Style은 프로젝트의 기본 스타일 기준을 정의하는 역할이다.

---

### [핵심]

| 비교 | Reset                                | Base Style                      |
| ---- | ------------------------------------ | ------------------------------- |
| 역할 | 브라우저 기본값 정리                 | 프로젝트 기본값 정의            |
| 대상 | box sizing, body margin, media, form | body font, color, link, heading |
| 위치 | 먼저 로드                            | reset 이후 로드                 |
| 목적 | 예측 가능성                          | 일관된 기본 UI                  |
| 주의 | 과도한 제거                          | component 침범 금지             |

---

### [실무]

선택 기준:

```text
body margin 제거 → Reset
body font-family 지정 → Base Style
img max-width 100% → Reset
link color와 underline 기준 → Base Style
focus-visible 기본값 → Base / Accessibility Base
```

---

### [FAQ]

Q. Reset과 Base Style 차이는 뭐야?
A. Reset은 기본값을 정리하고 Base Style은 프로젝트의 기본 디자인 기준을 정의한다.

Q. Reset만 있으면 충분해?
A. 아니다. Reset 이후 Base Style을 정의해야 UI 기준이 생긴다.

---

## 18.3 Global CSS vs Component CSS

### [개념]

Global CSS는 전체 문서에 영향을 주는 스타일이고 Component CSS는 특정 UI Component에 제한된 스타일이다.

---

### [핵심]

| 비교 | Global CSS         | Component CSS      |
| ---- | ------------------ | ------------------ |
| 범위 | 전역               | 특정 component     |
| 대상 | reset, base, token | button, card, form |
| 위험 | 의도치 않은 영향   | 중복 가능          |
| 장점 | 공통 기준          | 재사용성           |
| 주의 | selector 남용 금지 | naming 일관성      |

---

### [실무]

선택 기준:

```text
body 기본값 → Global CSS
CSS Variables Token → Global CSS
Button style → Component CSS
Card style → Component CSS
Specific page override → Page CSS
```

---

### [FAQ]

Q. Global CSS와 Component CSS 차이는 뭐야?
A. Global CSS는 전체 문서에 적용되고 Component CSS는 특정 UI 단위에 제한된다.

Q. 모든 스타일을 Global CSS로 써도 돼?
A. 권장하지 않는다. Component별 책임을 나눠야 충돌이 줄어든다.

Q. Reset은 Global CSS야?
A. 맞다. reset은 전역 스타일에 해당한다.

---

## 18.4 Utility Class vs Component Class

### [개념]

Utility Class는 작은 단일 목적 스타일이고 Component Class는 특정 UI Component의 구조와 디자인을 담당하는 class다.

---

### [핵심]

| 비교 | Utility Class                    | Component Class             |
| ---- | -------------------------------- | --------------------------- |
| 목적 | 단일 보조 스타일                 | UI 단위 스타일              |
| 예시 | `.container`, `.visually-hidden` | `.button`, `.festival-card` |
| 범위 | 재사용 보조                      | component 구조              |
| 장점 | 반복 제거                        | 의미 명확                   |
| 주의 | 남용 시 HTML 복잡                | 중복 style 가능             |

---

### [실무]

선택 기준:

```text
화면 숨김 접근성 텍스트 → utility
반응형 container → utility
버튼 디자인 → component class
카드 디자인 → component class
일회성 page layout → page class
```

---

### [FAQ]

Q. Utility Class와 Component Class 차이는 뭐야?
A. Utility Class는 작은 보조 스타일이고 Component Class는 특정 UI 단위의 스타일이다.

Q. 버튼 스타일을 utility만으로 만드는 게 좋아?
A. 작은 프로젝트에서는 가능하지만 재사용 component라면 button component class가 더 명확하다.

Q. visually-hidden은 utility야?
A. 맞다. 접근성용 재사용 utility로 적합하다.

---

# 19. Best Practice

## 19.1 Reset Normalize Styling Architecture Best Practice

### [개념]

Reset Normalize Styling Architecture Best Practice는 브라우저 기본 차이를 줄이고, 접근성을 유지하며, CSS 파일 구조와 component style 책임을 명확히 만드는 기준이다.

---

### [핵심]

권장 기준:

- Modern CSS Reset을 프로젝트 초기에 정의한다.
- Reset 이후 Base Style을 작성한다.
- `box-sizing: border-box`를 전역 적용한다.
- body margin을 제거하고 기본 typography를 정의한다.
- img/video/svg 등 media 요소에 responsive 기본값을 적용한다.
- form 요소에 font inheritance를 적용한다.
- focus outline을 제거만 하지 않는다.
- link는 링크로 인식 가능하게 유지한다.
- list reset은 class 기반으로 제한한다.
- token, reset, base, layout, component, utility 역할을 분리한다.
- CSS import 순서를 명확히 관리한다.
- component class naming을 의미 기반으로 작성한다.
- selector specificity를 낮게 유지한다.
- ID selector styling을 피한다.
- utility class는 제한적으로 사용한다.
- visually-hidden은 접근성 패턴으로 안전하게 작성한다.

---

### [실무]

Recommended File Structure:

```text
styles/
├ tokens.css
├ reset.css
├ base.css
├ layout.css
├ utilities.css
├ components/
│ ├ button.css
│ ├ card.css
│ ├ form.css
│ └ modal.css
└ pages/
  └ festival-page.css
```

Recommended Import Order:

```css
@import "./tokens.css";
@import "./reset.css";
@import "./base.css";
@import "./layout.css";
@import "./utilities.css";
@import "./components/button.css";
@import "./components/card.css";
@import "./components/form.css";
```

Recommended Reset + Base:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  min-height: 100dvh;
  font-family: var(--font-sans);
  line-height: 1.5;
  color: var(--color-text);
  background-color: var(--color-background);
}

img,
picture,
video,
canvas,
svg {
  display: block;
  max-width: 100%;
}

button,
input,
textarea,
select {
  font: inherit;
}

:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

[hidden] {
  display: none !important;
}
```

Recommended Utilities:

```css
.container {
  width: min(100% - 32px, 1120px);
  margin-inline: auto;
}

.list-unstyled {
  list-style: none;
  margin: 0;
  padding: 0;
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}
```

검수 Checklist:

```md
- [ ] Modern Reset이 component style보다 먼저 로드되는가?
- [ ] Reset 이후 Base Style이 정의되어 있는가?
- [ ] box-sizing border-box가 pseudo element까지 적용되는가?
- [ ] body margin이 제거되어 있는가?
- [ ] body font, color, background가 정의되어 있는가?
- [ ] img/video/svg가 부모를 넘지 않는가?
- [ ] form element가 font를 상속하는가?
- [ ] focus-visible style이 유지되는가?
- [ ] 모든 ul/ol을 무분별하게 reset하지 않았는가?
- [ ] link가 링크로 인식 가능한가?
- [ ] CSS 파일 역할이 token/reset/base/component로 분리되어 있는가?
- [ ] class naming이 의미 기반인가?
- [ ] selector chain이 과도하게 길지 않은가?
- [ ] ID selector styling을 피했는가?
- [ ] utility class를 남용하지 않았는가?
```

---

### [FAQ]

Q. Reset Normalize Styling Architecture Best Practice는 뭐야?
A. Modern Reset과 Base Style을 분리하고 token, component, utility 구조를 명확히 해 CSS 충돌과 접근성 문제를 줄이는 것이다.

Q. Reset 검수에서 가장 먼저 볼 것은 뭐야?
A. box-sizing, body margin, media reset, form font inheritance, focus-visible 보존 여부를 먼저 확인한다.

Q. Styling Architecture 검수에서 가장 먼저 볼 것은 뭐야?
A. CSS 파일 역할 분리, import 순서, selector specificity, token 사용, component scope를 확인한다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 Reset, Normalize, Base Style, CSS Architecture를 기준으로 예측 가능하고 유지보수 가능한 CSS 기반을 생성하고 검토하게 만드는 것이다.

---

# 20. Linkage Reference

## 20.1 Related Documents

### [개념]

Linkage Reference는 이 문서와 다른 HTML/CSS Foundation 문서의 역할을 구분하기 위한 참조 기준이다.

Part13은 Reset, Normalize, Base Style, CSS File Architecture, Styling Architecture의 설계 기준 문서다.

---

### [핵심]

연계 기준:

- Reset, Normalize, Base Style, CSS File Architecture의 설계 기준은 Part13에서 다룬다.
- CSS Selector, Cascade, Specificity의 기초 기준은 Part05를 참조한다.
- Responsive Layout과 Media Query 기준은 Part10을 참조한다.
- CSS Variables와 token 상세 기준은 Part12를 참조한다.
- Component별 실전 styling pattern은 Part14를 참조한다.
- HTML Attribute, ARIA, Accessibility, SEO 기준은 Part15를 참조한다.
- 실제 검수 단계의 Checklist와 Troubleshooting Flow는 Part16을 참조한다.

---

### [실무]

문제 상황별 참조:

```text
body margin / box-sizing / reset 문제 → Part13
reset/base import 순서 문제 → Part13 + Part16
CSS specificity 문제 → Part05
responsive overflow 문제 → Part10 + Part16
CSS Variables / token 문제 → Part12
button/card/form component style 문제 → Part14
accessibility attribute 문제 → Part15
최종 review checklist 필요 → Part16
```

---

### [FAQ]

Q. Part13은 어떤 역할이야?
A. Reset, Normalize, Base Style, CSS File Architecture, Styling Architecture의 설계 기준 문서다.

Q. Part13과 Part16은 어떻게 달라?
A. Part13은 CSS 기반 구조 설계 문서이고 Part16은 문제 진단과 최종 검수 문서다.

Q. Reset 문제가 생기면 어디를 봐?
A. reset/base 구조는 Part13, 실제 troubleshooting flow는 Part16을 함께 참조한다.

Q. Component Styling은 Part13에서 다뤄?
A. Part13은 구조 설계만 다루고 Button/Card/Form 같은 실전 component pattern은 Part14를 참조한다.

---

# Retrieval Queries

### [FAQ]

Q. Part13은 어떤 문서야?
A. CSS Reset, Normalize, Base Style, CSS File Architecture, Styling Architecture의 설계 기준 문서다.

Q. Part13과 Part16 차이는 뭐야?
A. Part13은 구조 설계 문서이고 Part16은 최종 Troubleshooting과 Review Checklist 문서다.

Q. Component별 style 예시는 어디서 봐?
A. CSS 기반 구조는 Part13, Button/Card/Form 같은 component 적용 예시는 Part14를 참조한다.

Q. CSS Variables 상세 기준은 어디서 봐?
A. token과 scoped variable 상세 기준은 Part12를 참조한다.

Q. CSS Reset이 뭐야?
A. 브라우저 기본 스타일을 제거하거나 줄여 프로젝트 스타일 기준을 일관되게 만드는 CSS 초기화 방식이다.

Q. CSS Reset은 왜 필요해?
A. 브라우저 기본 margin, padding, form style 차이로 인한 Layout 차이를 줄이기 위해 필요하다.

Q. Reset을 많이 하면 좋은 거야?
A. 아니다. 과도한 reset은 접근성이나 semantic 기본 표현을 해칠 수 있다.

Q. Reset 이후에는 무엇이 필요해?
A. body, heading, link, form, media 요소에 대한 base style을 다시 정의해야 한다.

Q. Normalize가 뭐야?
A. 브라우저 기본 스타일을 완전히 없애기보다 브라우저 간 차이를 줄여 일관되게 만드는 방식이다.

Q. Reset과 Normalize 차이는 뭐야?
A. Reset은 기본 스타일 제거에 가깝고 Normalize는 유용한 기본 스타일을 유지하며 차이를 줄이는 방식이다.

Q. Modern CSS Reset이 뭐야?
A. Layout 예측 가능성과 접근성을 유지하면서 필요한 기본값만 정리하는 현대적 reset 방식이다.

Q. Modern Reset에서 가장 중요한 것은 뭐야?
A. `box-sizing: border-box`, body margin 제거, media responsive 처리, form font 상속, focus 접근성 유지다.

Q. focus outline을 reset에서 없애도 돼?
A. 안 된다. 제거만 하면 keyboard 사용자가 현재 위치를 알 수 없다.

Q. img max-width 100%는 왜 reset에 넣어?
A. 이미지가 부모 너비를 넘어 가로 스크롤을 만드는 문제를 줄이기 위해서다.

Q. Base Style이 뭐야?
A. Reset 이후 프로젝트 전체에 적용되는 기본 typography, color, link, form, media 스타일이다.

Q. Reset만 하면 안 돼?
A. 안 된다. Reset은 기본값을 정리할 뿐이고 프로젝트 기준 스타일은 Base Style로 다시 정의해야 한다.

Q. Base Style과 Component Style 차이는?
A. Base Style은 전체 기본값이고 Component Style은 특정 UI 단위의 구체적 스타일이다.

Q. box-sizing border-box는 왜 전역으로 써?
A. width 안에 padding과 border가 포함되어 요소 크기 계산이 예측 가능해지기 때문이다.

Q. pseudo element에도 box-sizing이 필요해?
A. 필요하다. `*::before`, `*::after`에도 적용해야 가상 요소 크기 계산이 일관된다.

Q. Media Element Reset이 뭐야?
A. 이미지, 비디오, SVG 등이 부모 영역을 넘지 않도록 기본 스타일을 정리하는 것이다.

Q. img에 max-width 100%를 주는 이유는?
A. 원본 이미지가 부모보다 클 때 가로 overflow를 막기 위해서다.

Q. Form Reset이 뭐야?
A. input, textarea, select, button의 브라우저 기본 스타일 차이를 줄이는 초기화 기준이다.

Q. form 요소에 font inherit을 주는 이유는?
A. button과 input이 body font와 다르게 보이는 문제를 줄이기 위해서다.

Q. List Reset이 뭐야?
A. ul, ol의 기본 marker, margin, padding을 정리하는 방식이다.

Q. 모든 ul ol을 전역 reset해도 돼?
A. 주의해야 한다. 문서 본문의 목록 의미 표현까지 사라질 수 있다.

Q. Link Reset은 왜 조심해야 해?
A. 밑줄과 색상을 제거하면 사용자가 링크를 인식하기 어려워질 수 있기 때문이다.

Q. 링크 underline을 없애도 돼?
A. navigation처럼 문맥상 명확한 경우 가능하지만 text link에서는 대체 단서가 필요하다.

Q. Focus Style Architecture가 뭐야?
A. keyboard 사용자가 현재 조작 위치를 알 수 있도록 focus-visible 스타일을 일관되게 설계하는 기준이다.

Q. outline none을 써도 돼?
A. 제거만 하면 안 된다. 반드시 대체 focus style을 제공해야 한다.

Q. CSS File Architecture가 뭐야?
A. reset, token, base, layout, component, utility, page style을 역할별로 분리하는 구조 설계다.

Q. CSS 파일 로드 순서는 중요해?
A. 중요하다. 나중에 로드된 CSS가 같은 specificity의 이전 스타일을 덮어쓸 수 있다.

Q. reset은 언제 로드해야 해?
A. 일반적으로 component style보다 먼저 로드해야 한다.

Q. Styling Architecture가 뭐야?
A. CSS 작성 규칙, 파일 구조, naming, token, component 책임, cascade 관리 기준을 정하는 설계다.

Q. Styling Architecture가 왜 필요해?
A. 스타일 충돌을 줄이고 Component 재사용성과 유지보수성을 높이기 위해 필요하다.

Q. 좋은 CSS 구조의 기준은 뭐야?
A. reset, base, token, layout, component 역할이 분리되고 specificity가 낮으며 token 기반으로 작성된 구조다.

Q. CSS class 이름은 어떻게 지어야 해?
A. 색상이나 크기보다 component 역할과 의미 중심으로 짓는 것이 좋다.

Q. Utility Class가 뭐야?
A. 하나의 작은 스타일 목적을 가진 재사용 CSS class다.

Q. visually-hidden은 언제 써?
A. 화면에는 숨기지만 스크린 리더에는 제공해야 하는 텍스트에 사용한다.

Q. CSS Scope Strategy가 뭐야?
A. CSS 스타일이 어디까지 영향을 미치게 할지 정해 충돌을 줄이는 방식이다.

Q. CSS는 기본적으로 scope가 있어?
A. 일반 CSS는 기본적으로 전역 cascade를 가지므로 명시적 class와 구조로 scope를 관리해야 한다.

Q. Reset에서 가장 흔한 실수는 뭐야?
A. focus outline을 제거하거나 reset 후 base style을 다시 정의하지 않는 것이다.

Q. Styling Architecture에서 가장 흔한 실수는 뭐야?
A. 역할 분리 없이 한 파일에 모든 스타일을 누적하고 selector specificity를 계속 높이는 것이다.

Q. List Reset에서 가장 흔한 실수는 뭐야?
A. 모든 ul/ol을 전역 reset해 문서 본문 목록 marker까지 제거하는 것이다.

Q. Reset과 Normalize 차이는 뭐야?
A. Reset은 기본 스타일 제거에 가깝고 Normalize는 브라우저 차이를 줄이되 유용한 기본 스타일을 유지한다.

Q. React App에는 뭐가 좋아?
A. 보통 Modern Reset과 Base Style 조합이 적합하다.

Q. Reset과 Base Style 차이는 뭐야?
A. Reset은 기본값을 정리하고 Base Style은 프로젝트의 기본 디자인 기준을 정의한다.

Q. Global CSS와 Component CSS 차이는 뭐야?
A. Global CSS는 전체 문서에 적용되고 Component CSS는 특정 UI 단위에 제한된다.

Q. Utility Class와 Component Class 차이는 뭐야?
A. Utility Class는 작은 보조 스타일이고 Component Class는 특정 UI 단위의 스타일이다.

Q. Reset Normalize Styling Architecture Best Practice는 뭐야?
A. Modern Reset과 Base Style을 분리하고 token, component, utility 구조를 명확히 해 CSS 충돌과 접근성 문제를 줄이는 것이다.

Q. Reset 검수에서 가장 먼저 볼 것은 뭐야?
A. box-sizing, body margin, media reset, form font inheritance, focus-visible 보존 여부를 먼저 확인한다.

Q. Styling Architecture 검수에서 가장 먼저 볼 것은 뭐야?
A. CSS 파일 역할 분리, import 순서, selector specificity, token 사용, component scope를 확인한다.

Q. Part13은 어떤 역할이야?
A. Reset, Normalize, Base Style, CSS File Architecture, Styling Architecture의 설계 기준 문서다.

Q. Part13과 Part16은 어떻게 달라?
A. Part13은 CSS 기반 구조 설계 문서이고 Part16은 문제 진단과 최종 검수 문서다.

Q. Reset 문제가 생기면 어디를 봐?
A. reset/base 구조는 Part13, 실제 troubleshooting flow는 Part16을 함께 참조한다.

Q. Component Styling은 Part13에서 다뤄?
A. Part13은 구조 설계만 다루고 Button/Card/Form 같은 실전 component pattern은 Part14를 참조한다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 Reset, Normalize, Base Style, CSS Architecture를 기준으로 예측 가능하고 유지보수 가능한 CSS 기반을 생성하고 검토하게 만드는 것이다.
