# Styling Architecture Part05 - Responsive Styling, Theme, Dark Mode Rules

---

# 1. Responsive Styling Rules

## 1.1 Responsive Architecture

### [개념]

Responsive Architecture는 화면 크기에 따라 UI가 자연스럽게 변하도록 스타일 기준을 체계화하는 방식이다.

Responsive Styling은 단순히 media query를 추가하는 작업이 아니다.

Responsive Architecture는 layout, component, typography, spacing, image, modal, table, navigation이 다양한 화면에서 깨지지 않도록 관리하는 기준이다.

---

### [핵심]

반응형 핵심 기준:

- Mobile First 우선
- 고정 width 남용 금지
- container max-width 사용
- grid / flex 기반 layout 사용
- image max-width 처리
- breakpoint 기준 통일
- touch target 고려
- table overflow 처리
- modal 모바일 대응
- navigation 모바일 대응
- long text overflow 대응

---

### [실무]

Responsive Layout 예:

```css
.container {
  width: min(100% - 32px, 1200px);
  margin: 0 auto;
}

.cardGrid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--spacing-4);
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

Responsive Styling 리뷰 기준:

```md
- [ ] 모바일 360px에서 가로 스크롤이 없는가?
- [ ] tablet / desktop layout이 자연스러운가?
- [ ] 이미지와 카드가 줄바꿈되는가?
- [ ] modal이 모바일에서 화면을 넘지 않는가?
- [ ] table overflow 처리가 되어 있는가?
- [ ] 버튼 터치 영역이 충분한가?
- [ ] 고정 width가 반응형을 방해하지 않는가?
```

Responsive 판단 Flow:

```text
Viewport 확인
→ Mobile First 기본 스타일 확인
→ 고정 width 확인
→ grid / flex wrap 확인
→ image max-width 확인
→ table / modal overflow 확인
→ breakpoint 적용 확인
→ touch target 확인
```

---

### [FAQ]

Q. Responsive Architecture가 뭐야?
A. 화면 크기에 따라 layout, component, image, modal, table, navigation이 자연스럽게 변하도록 관리하는 스타일 구조다.

Q. Mobile First가 뭐야?
A. 모바일 스타일을 기본으로 작성하고 큰 화면 스타일을 media query로 확장하는 방식이다.

Q. 반응형에서 가장 흔한 문제는 뭐야?
A. 고정 width, 큰 이미지, flex-wrap 누락, table overflow, modal width 고정이다.

Q. 반응형은 media query만 추가하면 돼?
A. 아니다. layout 구조, width 전략, image, table, modal, touch target까지 함께 검토해야 한다.

---

## 1.2 Mobile First Rules

### [개념]

Mobile First는 모바일 화면을 기본 스타일로 작성하고, tablet과 desktop 스타일을 media query로 확장하는 방식이다.

Mobile First는 작은 화면에서 먼저 깨지지 않는 구조를 만든 뒤 큰 화면에서 레이아웃을 강화한다.

---

### [핵심]

Mobile First 원칙:

- 기본 스타일은 mobile 기준
- 큰 화면에서 `min-width` media query 사용
- 작은 화면에서 단일 column 우선
- mobile width에서 overflow 방지
- touch target 고려
- font size와 spacing 과대 사용 금지
- desktop layout을 mobile에 억지로 축소하지 않음

---

### [실무]

나쁜 예:

```css
.page {
  width: 1200px;
  display: grid;
  grid-template-columns: 300px 1fr;
}

@media (max-width: 767px) {
  .page {
    width: 100%;
    display: block;
  }
}
```

좋은 예:

```css
.page {
  display: grid;
  gap: var(--spacing-4);
}

@media (min-width: 768px) {
  .page {
    grid-template-columns: 240px 1fr;
  }
}
```

Mobile First 리뷰 기준:

```md
- [ ] 기본 스타일이 모바일 기준인가?
- [ ] 큰 화면 스타일이 min-width로 확장되는가?
- [ ] 모바일에서 단일 column이 자연스러운가?
- [ ] desktop 고정 width를 mobile에서 억지로 줄이지 않는가?
- [ ] mobile spacing과 font size가 과하지 않은가?
```

---

### [FAQ]

Q. Mobile First는 왜 좋아?
A. 작은 화면에서 먼저 안정적인 구조를 만들고 큰 화면에서 확장하기 때문에 반응형 깨짐을 줄이기 쉽다.

Q. max-width media query를 쓰면 안 돼?
A. 금지는 아니지만 Mobile First 구조에서는 min-width 기반 확장이 더 일관적이다.

Q. 모바일에서 desktop layout을 축소하면 안 돼?
A. 대부분 권장하지 않는다. 모바일에는 모바일에 맞는 단순한 흐름이 필요하다.

---

# 2. Breakpoint Rules

## 2.1 Breakpoint Definition

### [개념]

Breakpoint는 화면 크기에 따라 스타일이 바뀌는 기준점이다.

Breakpoint는 기기명만 기준으로 정하는 것이 아니라 콘텐츠가 깨지는 지점을 기준으로 정해야 한다.

---

### [핵심]

권장 breakpoint 예:

```text
mobile: default
tablet: 768px
desktop: 1024px
wide: 1280px
```

Breakpoint 설계 원칙:

- mobile은 기본값으로 처리
- common breakpoint를 우선 사용
- 불필요한 breakpoint 남발 금지
- 콘텐츠가 깨지는 지점 기준
- component-specific breakpoint 최소화
- 프로젝트 전체 기준 통일
- breakpoint 문서화

---

### [실무]

Breakpoint 예:

```css
@media (min-width: 768px) {
  .layout {
    display: grid;
    grid-template-columns: 240px 1fr;
  }
}

@media (min-width: 1024px) {
  .layout {
    grid-template-columns: 280px 1fr;
  }
}
```

Breakpoint 리뷰 기준:

```md
- [ ] 프로젝트 공통 breakpoint가 정의되어 있는가?
- [ ] breakpoint가 너무 많지 않은가?
- [ ] component마다 임의 breakpoint를 남용하지 않는가?
- [ ] mobile default 기준이 유지되는가?
- [ ] 실제 콘텐츠가 깨지는 지점과 맞는가?
```

---

### [FAQ]

Q. breakpoint는 꼭 768, 1024를 써야 해?
A. 아니다. 일반 기준일 뿐이며 실제 콘텐츠가 깨지는 지점을 기준으로 조정할 수 있다.

Q. 컴포넌트마다 breakpoint가 달라도 돼?
A. 가능하지만 너무 많으면 관리가 어려워진다. 공통 breakpoint를 우선 사용한다.

Q. mobile breakpoint는 따로 써야 해?
A. Mobile First에서는 mobile을 기본 스타일로 두고 tablet 이상부터 media query를 작성하는 것이 일반적이다.

---

## 2.2 Breakpoint Token Rules

### [개념]

Breakpoint Token은 반응형 기준 값을 프로젝트 전체에서 일관되게 관리하는 방식이다.

CSS variable은 media query 조건에 직접 사용하기 어려운 경우가 많으므로 breakpoint는 문서화나 전처리기 변수, config 파일로 관리할 수 있다.

---

### [핵심]

Breakpoint 관리 방식:

- 문서화된 breakpoint table
- SCSS variable
- Tailwind config theme screen
- JS constant
- Design System token
- CSS 주석 기준

CSS variable 주의:

```text
CSS custom property는 일반 media query 조건에서 직접 사용하기 어렵다.
따라서 breakpoint는 별도 문서화 또는 build tool 기반 token으로 관리한다.
```

---

### [실무]

Tailwind breakpoint 예:

```js
export default {
  theme: {
    screens: {
      tablet: "768px",
      desktop: "1024px",
      wide: "1280px",
    },
  },
};
```

SCSS breakpoint 예:

```scss
$breakpoint-tablet: 768px;
$breakpoint-desktop: 1024px;

@media (min-width: $breakpoint-tablet) {
  .layout {
    display: grid;
  }
}
```

Breakpoint Token 리뷰 기준:

```md
- [ ] breakpoint 기준이 한 곳에 정리되어 있는가?
- [ ] CSS / Tailwind / SCSS에서 breakpoint 기준이 어긋나지 않는가?
- [ ] 기기명보다 layout 변경 기준으로 설명되어 있는가?
- [ ] 임의 breakpoint가 반복되지 않는가?
```

---

### [FAQ]

Q. breakpoint도 token으로 관리해야 해?
A. 권장된다. 프로젝트 전체 반응형 기준을 통일하기 위해 필요하다.

Q. CSS variable로 media query breakpoint를 만들 수 있어?
A. 일반적인 media query 조건에서는 직접 사용하기 어렵다. SCSS variable, Tailwind config, 문서화 방식이 더 안정적이다.

Q. Tailwind에서는 breakpoint를 어디서 관리해?
A. `tailwind.config.js`의 `theme.screens`에서 관리한다.

---

# 3. Responsive Layout Patterns

## 3.1 Container Pattern

### [개념]

Container Pattern은 콘텐츠의 최대 너비와 좌우 여백을 일관되게 관리하는 layout pattern이다.

Container는 화면이 커져도 콘텐츠가 지나치게 넓어지지 않게 하고, 작은 화면에서는 안전한 여백을 유지한다.

---

### [핵심]

Container 기준:

- `max-width` 또는 `width: min()` 사용
- mobile side padding 확보
- center alignment
- page layout에서 관리
- component 내부에서 container width 강제 금지
- token 기반 spacing 사용 권장

---

### [실무]

Container 예:

```css
.container {
  width: min(100% - 32px, 1200px);
  margin-inline: auto;
}
```

Token 기반 예:

```css
.container {
  width: min(100% - var(--spacing-8), var(--layout-max-width));
  margin-inline: auto;
}
```

Container 리뷰 기준:

```md
- [ ] mobile에서 좌우 여백이 확보되는가?
- [ ] desktop에서 콘텐츠가 너무 넓어지지 않는가?
- [ ] container width가 component style에 흩어져 있지 않은가?
- [ ] page 또는 layout component에서 container를 관리하는가?
```

---

### [FAQ]

Q. Container Pattern은 왜 필요해?
A. 화면 크기와 관계없이 콘텐츠 폭과 좌우 여백을 안정적으로 유지하기 위해 필요하다.

Q. width: 1200px만 쓰면 안 돼?
A. 모바일에서 가로 스크롤이 생길 수 있다. `max-width`나 `width: min()`을 사용하는 것이 좋다.

Q. Container는 컴포넌트마다 넣어도 돼?
A. 권장하지 않는다. page layout이나 layout utility에서 관리하는 것이 좋다.

---

## 3.2 Grid and Flex Responsive Rules

### [개념]

Grid와 Flex는 responsive layout의 핵심 도구다.

Grid는 2차원 layout에 적합하고, Flex는 1차원 정렬과 wrapping에 적합하다.

---

### [핵심]

Grid 적합 상황:

- card grid
- dashboard layout
- gallery
- page sections
- column layout

Flex 적합 상황:

- button group
- navigation
- inline alignment
- toolbar
- icon + text alignment
- wrap 가능한 chip list

반응형 주의:

- flex-wrap 누락 주의
- grid fixed column 주의
- `minmax()` 활용
- `min-width: 0` 필요 여부 확인
- gap token 사용
- fixed width 지양

---

### [실무]

Grid 예:

```css
.cardGrid {
  display: grid;
  gap: var(--spacing-4);
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}
```

Flex wrap 예:

```css
.toolbar {
  display: flex;
  flex-wrap: wrap;
  gap: var(--spacing-2);
  align-items: center;
}
```

Flex item overflow 대응:

```css
.content {
  min-width: 0;
}
```

리뷰 기준:

```md
- [ ] grid column이 작은 화면에서 깨지지 않는가?
- [ ] flex item이 줄바꿈 가능한가?
- [ ] gap을 token으로 사용하는가?
- [ ] 긴 텍스트가 layout을 밀어내지 않는가?
- [ ] min-width: 0이 필요한 flex/grid item에 적용되었는가?
```

---

### [FAQ]

Q. Grid와 Flex 중 뭐를 써야 해?
A. 2차원 배치는 Grid, 한 방향 정렬과 wrapping은 Flex가 적합하다.

Q. flex item이 줄어들지 않아?
A. `min-width: 0`이 필요할 수 있다.

Q. card grid는 어떻게 반응형 처리해?
A. `repeat(auto-fit, minmax(...))` 또는 breakpoint별 column 변경을 사용할 수 있다.

---

## 3.3 Table Responsive Rules

### [개념]

Table Responsive Rules는 테이블이 작은 화면에서 가로로 넘치거나 내용이 깨지는 문제를 방지하는 기준이다.

테이블은 모바일에서 깨지기 쉬운 UI이므로 별도 overflow 전략이 필요하다.

---

### [핵심]

Table responsive 전략:

- wrapper에 horizontal scroll 적용
- `overflow-x: auto`
- 최소 너비 지정
- 중요한 column 우선 표시
- 모바일 카드형 변환 고려
- text wrapping 기준 설정
- sticky header / column은 z-index와 overflow 검토

---

### [실무]

Table overflow 예:

```css
.tableWrapper {
  overflow-x: auto;
}

.table {
  min-width: 720px;
  width: 100%;
  border-collapse: collapse;
}
```

Table 리뷰 기준:

```md
- [ ] 모바일에서 table이 화면을 밀어내지 않는가?
- [ ] wrapper overflow-x 처리가 있는가?
- [ ] table min-width가 의도적으로 설정되어 있는가?
- [ ] 중요한 정보가 작은 화면에서도 확인 가능한가?
- [ ] sticky column 사용 시 z-index 충돌이 없는가?
```

---

### [FAQ]

Q. 모바일에서 table이 깨지면 어떻게 해?
A. wrapper에 `overflow-x: auto`를 적용하거나 모바일 카드형 UI로 전환할 수 있다.

Q. table에 width: 100%만 주면 충분해?
A. 아니다. column이 많으면 내용이 압축되거나 화면을 밀어낼 수 있다.

Q. table을 모바일에서 카드로 바꿔도 돼?
A. 가능하다. 데이터 구조와 사용성을 고려해 선택해야 한다.

---

## 3.4 Modal Responsive Rules

### [개념]

Modal Responsive Rules는 modal이 작은 화면에서 화면을 넘거나 조작이 어려워지는 문제를 방지하는 기준이다.

Modal은 width, height, scroll, focus, close button, safe area를 함께 고려해야 한다.

---

### [핵심]

Modal responsive 기준:

- mobile width는 viewport 기준
- max-width 사용
- max-height와 내부 scroll 고려
- close button 접근성 확보
- focus-visible 유지
- overlay와 z-index token 사용
- mobile에서 여백 확보
- 키보드 / input focus 시 화면 대응 고려

---

### [실무]

Modal 예:

```css
.modal {
  width: min(100% - 32px, 560px);
  max-height: min(80vh, 720px);
  overflow-y: auto;
  border-radius: var(--radius-lg);
  background: var(--color-surface);
  box-shadow: var(--shadow-lg);
}

.overlay {
  position: fixed;
  inset: 0;
  z-index: var(--z-overlay);
}
```

Modal 리뷰 기준:

```md
- [ ] 모바일에서 modal width가 viewport를 넘지 않는가?
- [ ] modal content가 길 때 scroll 가능한가?
- [ ] close button이 항상 접근 가능한가?
- [ ] overlay와 modal z-index가 token으로 관리되는가?
- [ ] focus style이 유지되는가?
```

---

### [FAQ]

Q. 모바일에서 modal이 화면을 넘으면 어떻게 해?
A. `width: min(100% - 여백, max-width)`와 `max-height`, `overflow-y: auto`를 적용한다.

Q. modal width를 600px로 고정해도 돼?
A. 권장하지 않는다. 작은 화면에서 overflow가 발생할 수 있다.

Q. modal에도 focus style이 필요해?
A. 필요하다. close button, input, action button의 keyboard 조작이 가능해야 한다.

---

# 4. Image and Text Responsive Rules

## 4.1 Responsive Image Rules

### [개념]

Responsive Image Rules는 이미지가 화면 너비를 넘어가거나 layout을 깨지 않도록 관리하는 기준이다.

이미지는 반응형 깨짐의 주요 원인 중 하나다.

---

### [핵심]

이미지 기준:

- `max-width: 100%`
- `height: auto`
- `display: block`
- aspect-ratio 필요 시 사용
- object-fit 사용 기준
- container 기준에 맞게 크기 제한
- 큰 이미지 lazy loading 고려
- 이미지가 grid/flex를 밀어내지 않도록 확인

---

### [실무]

기본 이미지 스타일:

```css
img {
  max-width: 100%;
  display: block;
}
```

Card image 예:

```css
.cardImage {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  border-radius: var(--radius-md);
}
```

Image 리뷰 기준:

```md
- [ ] 이미지가 container를 넘지 않는가?
- [ ] aspect-ratio가 필요한 경우 정의되어 있는가?
- [ ] object-fit 기준이 명확한가?
- [ ] 이미지 로딩 전 layout shift가 과하지 않은가?
```

---

### [FAQ]

Q. 이미지가 모바일에서 화면을 넘으면 어떻게 해?
A. `max-width: 100%`와 container 기준 width를 적용한다.

Q. object-fit은 언제 써?
A. 이미지 비율을 유지하면서 정해진 영역을 채우거나 맞출 때 사용한다.

Q. aspect-ratio는 왜 필요해?
A. 이미지 로딩 전 공간을 확보해 layout shift를 줄이는 데 도움이 된다.

---

## 4.2 Text Overflow Rules

### [개념]

Text Overflow Rules는 긴 텍스트가 layout을 밀어내거나 화면 밖으로 나가는 문제를 방지하는 기준이다.

긴 제목, 긴 URL, 긴 단어, 사용자 입력 텍스트는 responsive layout을 깨뜨릴 수 있다.

---

### [핵심]

Text overflow 원인:

- 긴 URL
- 긴 영어 단어
- 긴 제목
- flex item min-width 기본값
- nowrap 남용
- table column 압축
- button label 과다

대응 방식:

- `min-width: 0`
- `overflow-wrap: break-word`
- `word-break` 신중 사용
- line clamp 사용
- ellipsis 사용
- max-width 설정

---

### [실무]

긴 텍스트 대응:

```css
.cardTitle {
  overflow-wrap: break-word;
}

.flexChild {
  min-width: 0;
}

.singleLineText {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

Line clamp 예:

```css
.description {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```

Text overflow 리뷰 기준:

```md
- [ ] 긴 텍스트가 layout을 밀어내지 않는가?
- [ ] flex/grid item에 min-width: 0이 필요한가?
- [ ] ellipsis 사용 시 전체 내용을 확인할 방법이 있는가?
- [ ] line clamp가 중요한 정보를 숨기지 않는가?
```

---

### [FAQ]

Q. 긴 텍스트가 카드 밖으로 나가면 어떻게 해?
A. `overflow-wrap: break-word`, `min-width: 0`, line clamp, ellipsis 등을 검토한다.

Q. flex item 안 텍스트가 줄어들지 않아?
A. flex child에 `min-width: 0`이 필요할 수 있다.

Q. ellipsis를 쓰면 항상 좋아?
A. 아니다. 중요한 정보가 잘릴 수 있으므로 필요한 경우 tooltip이나 상세 화면을 제공해야 한다.

---

# 5. Theme Architecture Rules

## 5.1 Theme Architecture

### [개념]

Theme Architecture는 색상, 배경, 텍스트, border, shadow 같은 스타일 값을 theme별로 전환할 수 있도록 설계하는 방식이다.

Theme Architecture는 raw color를 컴포넌트에 직접 흩뿌리지 않고 semantic token으로 연결하는 구조다.

---

### [핵심]

Theme 구조:

```text
Primitive Token
→ Semantic Token
→ Theme Override
→ Component Style
```

예:

```text
--blue-600
→ --color-primary
→ light / dark value
→ Button background
```

Theme Architecture 기준:

- semantic token 우선 사용
- component raw color 최소화
- light / dark token 분리
- surface / border / muted token 포함
- contrast 검토
- user preference 저장 전략
- system preference 대응 가능성 검토

---

### [실무]

Theme token 예:

```css
:root {
  --color-background: #ffffff;
  --color-text: #111827;
  --color-surface: #f9fafb;
  --color-border: #e5e7eb;
}

[data-theme="dark"] {
  --color-background: #111827;
  --color-text: #f9fafb;
  --color-surface: #1f2937;
  --color-border: #374151;
}
```

사용 예:

```css
body {
  background: var(--color-background);
  color: var(--color-text);
}

.card {
  background: var(--color-surface);
  border-color: var(--color-border);
}
```

Theme 리뷰 기준:

```md
- [ ] 컴포넌트가 raw color 대신 semantic token을 사용하는가?
- [ ] light / dark에서 contrast가 충분한가?
- [ ] border / surface / muted text가 theme별로 정의되어 있는가?
- [ ] theme 전환 시 layout shift가 없는가?
- [ ] localStorage 또는 system preference 전략이 있는가?
```

---

### [FAQ]

Q. Theme Architecture는 뭐야?
A. 색상, 배경, 텍스트, border, shadow 같은 스타일 값을 theme별로 전환할 수 있도록 설계하는 방식이다.

Q. Theme를 만들 때 raw color를 직접 쓰면 안 돼?
A. 컴포넌트에서는 raw color보다 semantic token을 사용하는 것이 theme 확장에 좋다.

Q. semantic token이 theme에 왜 중요해?
A. 컴포넌트 코드를 수정하지 않고 theme별 token 값만 바꿔 UI를 전환할 수 있기 때문이다.

---

## 5.2 Theme Token Responsibility

### [개념]

Theme Token Responsibility는 primitive token, semantic token, component token의 책임을 구분하는 규칙이다.

Token 책임이 섞이면 theme 확장과 dark mode 대응이 어려워진다.

---

### [핵심]

Token 책임 구조:

```text
Primitive Token
→ 실제 색상값
→ --blue-600, --gray-900

Semantic Token
→ UI 역할
→ --color-primary, --color-text, --color-background

Component Token
→ 특정 컴포넌트 역할
→ --button-primary-bg, --card-background
```

권장:

- 작은 프로젝트는 semantic token 중심으로 시작
- 큰 프로젝트는 primitive + semantic 분리
- component token은 디자인 시스템 규모에서 선택적 사용
- 컴포넌트에서는 semantic token 우선 사용

---

### [실무]

Token 책임 예:

```css
:root {
  --blue-600: #2563eb;
  --gray-900: #111827;
  --gray-50: #f9fafb;

  --color-primary: var(--blue-600);
  --color-text: var(--gray-900);
  --color-surface: var(--gray-50);
}
```

Dark theme override:

```css
[data-theme="dark"] {
  --color-text: #f9fafb;
  --color-surface: #1f2937;
}
```

Token Responsibility 리뷰 기준:

```md
- [ ] primitive token과 semantic token의 책임이 구분되는가?
- [ ] 컴포넌트가 raw primitive token에 과하게 의존하지 않는가?
- [ ] theme override는 semantic token 중심인가?
- [ ] component token이 과도하게 증가하지 않는가?
```

---

### [FAQ]

Q. primitive token과 semantic token은 뭐가 달라?
A. primitive token은 실제 색상값이고 semantic token은 UI 역할을 표현한다.

Q. 작은 프로젝트도 primitive token을 꼭 나눠야 해?
A. 필수는 아니다. 작은 프로젝트는 semantic token 중심으로 시작해도 충분하다.

Q. component token은 언제 필요해?
A. 디자인 시스템 규모에서 특정 컴포넌트의 theme 세부 제어가 필요할 때 사용할 수 있다.

---

# 6. Dark Mode Rules

## 6.1 Dark Mode Architecture

### [개념]

Dark Mode는 어두운 배경과 밝은 텍스트를 기준으로 UI를 전환하는 theme의 한 종류다.

Dark Mode는 단순히 배경을 검게 만드는 작업이 아니다.

Dark Mode는 text, background, surface, border, hover, disabled, focus, icon, shadow를 함께 조정해야 한다.

---

### [핵심]

Dark Mode 체크 항목:

- background와 text contrast
- surface 색상
- border 색상
- muted text 색상
- hover 색상
- disabled 색상
- shadow 대체
- image / icon visibility
- focus style visibility
- chart / map 색상
- system preference 대응
- color-scheme 설정

---

### [실무]

Dark Mode 기본 구조:

```css
:root {
  color-scheme: light;

  --color-background: #ffffff;
  --color-text: #111827;
  --color-surface: #f9fafb;
  --color-border: #e5e7eb;
}

[data-theme="dark"] {
  color-scheme: dark;

  --color-background: #111827;
  --color-text: #f9fafb;
  --color-surface: #1f2937;
  --color-border: #374151;
}
```

Dark Mode 구현 Flow:

```text
Semantic Token 정의
→ Light Token 값 정의
→ Dark Token 값 정의
→ Theme Attribute 적용
→ Component raw color 제거
→ Contrast 검토
→ User Preference 저장
```

Dark Mode 리뷰 기준:

```md
- [ ] background와 text contrast가 충분한가?
- [ ] surface와 border가 dark theme에 맞게 조정되는가?
- [ ] hover / disabled / focus 상태가 dark mode에서도 보이는가?
- [ ] icon과 image가 어두운 배경에서 식별되는가?
- [ ] 컴포넌트 raw color가 dark mode를 방해하지 않는가?
```

---

### [FAQ]

Q. Dark Mode를 만들려면 모든 색상을 다시 써야 해?
A. 컴포넌트가 semantic token을 사용한다면 theme token 값만 바꿔도 많은 부분을 대응할 수 있다.

Q. Dark Mode에서 단순히 배경만 검게 하면 돼?
A. 아니다. 텍스트, border, surface, hover, disabled, focus, icon 색상까지 함께 조정해야 한다.

Q. color-scheme은 왜 써?
A. 브라우저 기본 form control, scrollbar 등이 theme에 맞게 표시되도록 돕는다.

---

## 6.2 Dark Mode Implementation Strategy

### [개념]

Dark Mode Implementation Strategy는 dark theme을 적용하는 방식과 사용자 설정을 유지하는 기준이다.

Dark Mode는 CSS token만으로 일부 구현 가능하지만, 사용자 선택 저장과 system preference 대응은 JavaScript와 연결될 수 있다.

---

### [핵심]

Dark Mode 적용 방식:

- `data-theme="dark"` attribute
- `.dark` class
- `prefers-color-scheme`
- localStorage user preference
- system preference fallback
- server-rendered initial theme

권장 우선순위:

```text
User Preference
→ System Preference
→ Default Theme
```

---

### [실무]

CSS system preference 예:

```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-background: #111827;
    --color-text: #f9fafb;
  }
}
```

Attribute 기반 예:

```css
[data-theme="dark"] {
  --color-background: #111827;
  --color-text: #f9fafb;
}
```

Theme 적용 Flow:

```text
앱 초기 로드
→ localStorage theme 확인
→ 없으면 system preference 확인
→ document root에 data-theme 적용
→ token 값 변경
→ component style 자동 반영
```

리뷰 기준:

```md
- [ ] user preference와 system preference 우선순위가 명확한가?
- [ ] theme 전환 시 flicker 가능성이 검토되었는가?
- [ ] token 기반 전환인가?
- [ ] raw color가 남아 dark mode를 깨지 않는가?
```

---

### [FAQ]

Q. Dark Mode는 class 방식과 data-theme 방식 중 뭐가 좋아?
A. 둘 다 가능하다. 중요한 것은 프로젝트 전체에서 일관되게 사용하는 것이다.

Q. prefers-color-scheme만 쓰면 충분해?
A. 사용자 직접 선택을 저장해야 한다면 localStorage나 별도 상태 관리가 필요하다.

Q. theme 전환 시 깜빡임이 생기면 어떻게 해?
A. 초기 렌더 전에 theme attribute를 적용하는 전략을 고려해야 한다.

---

# 7. Theme and Responsive Integration

## 7.1 Responsive Theme Interaction

### [개념]

Responsive Theme Interaction은 반응형 스타일과 theme 스타일이 함께 적용될 때 충돌하지 않도록 관리하는 기준이다.

Theme과 responsive는 서로 다른 축이다.

Theme은 색상과 시각 의미를 바꾸고, responsive는 화면 구조와 배치를 바꾼다.

---

### [핵심]

분리 원칙:

```text
Responsive
→ layout
→ width
→ grid / flex
→ spacing adjustment

Theme
→ color
→ background
→ border
→ surface
→ shadow
→ state color
```

주의:

- media query 안에서 raw color 반복 금지
- dark mode에서 mobile layout만 깨지지 않는지 확인
- responsive component가 theme token을 유지하는지 확인
- breakpoint별로 다른 color를 임의 지정하지 않음
- state color는 theme token으로 관리

---

### [실무]

좋은 예:

```css
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  padding: var(--spacing-4);
}

@media (min-width: 768px) {
  .card {
    padding: var(--spacing-6);
  }
}
```

나쁜 예:

```css
@media (min-width: 768px) {
  .card {
    background: white;
    color: black;
  }
}
```

Review 기준:

```md
- [ ] responsive style이 layout 책임에 집중하는가?
- [ ] theme style이 color token 중심으로 관리되는가?
- [ ] media query 안에서 raw color를 반복하지 않는가?
- [ ] dark mode와 mobile layout을 함께 확인했는가?
```

---

### [FAQ]

Q. Responsive와 Theme는 같은 기준으로 관리해?
A. 아니다. Responsive는 layout 축이고 Theme은 color / visual token 축이다.

Q. media query 안에서 색상을 바꿔도 돼?
A. 가능하지만 theme token을 우회하는 raw color 반복은 피해야 한다.

Q. dark mode도 모바일에서 따로 확인해야 해?
A. 필요하다. dark mode token이 모바일 layout과 함께 적용될 때 깨지는 경우가 있을 수 있다.

---

# 8. Agent Responsive and Theme Rules

## 8.1 Frontend Agent Rules

### [개념]

Frontend Agent는 responsive style과 theme style을 생성할 때 기존 breakpoint, token, theme 구조를 따라야 한다.

Frontend Agent는 임의 breakpoint와 raw color를 남발하면 안 된다.

---

### [핵심]

Frontend Agent 생성 규칙:

- Mobile First 기본 적용
- 기존 breakpoint 확인
- 고정 width 남용 금지
- container pattern 사용
- grid / flex responsive 적용
- image max-width 확인
- table / modal overflow 고려
- semantic token 사용
- raw color 반복 금지
- dark mode 요구 시 theme token 기반 작성
- focus / hover / disabled 상태의 theme 대응 확인

---

### [실무]

Frontend Agent 작업 Flow:

```text
Responsive / Theme Request
→ Existing Breakpoint 확인
→ Existing Token 확인
→ Mobile First 구조 작성
→ Layout responsive 적용
→ Component overflow 확인
→ Theme token 적용
→ Dark Mode 필요 여부 확인
→ Accessibility State 확인
→ Review Agent 전달
```

생성 금지에 가까운 예:

```text
width: 1200px 고정
mobile에서 가로 스크롤 발생
media query마다 raw color 하드코딩
기존 breakpoint와 다른 임의 값 반복
dark mode에서 background만 변경
modal width 고정
table overflow 미처리
```

---

### [FAQ]

Q. Frontend Agent가 breakpoint를 임의로 추가해도 돼?
A. 기존 breakpoint를 먼저 확인해야 한다. 임의 breakpoint는 필요한 이유가 명확해야 한다.

Q. Frontend Agent가 dark mode에서 색상을 직접 지정해도 돼?
A. 가능하면 semantic token을 사용해야 한다. raw color 반복은 theme 확장을 어렵게 만든다.

Q. Frontend Agent가 반응형에서 가장 먼저 확인할 것은 뭐야?
A. 모바일 기본 구조, 고정 width, overflow, 기존 breakpoint를 먼저 확인해야 한다.

---

## 8.2 Review Agent Rules

### [개념]

Review Agent는 responsive style, breakpoint, theme, dark mode가 프로젝트 기준과 일치하는지 검토한다.

Review Agent는 desktop 화면만 확인하면 안 된다.

---

### [핵심]

Review Agent 검토 항목:

- Mobile First 구조
- 공통 breakpoint 사용
- mobile 360px 가로 스크롤 여부
- fixed width 남용 여부
- grid / flex wrapping
- image overflow
- table overflow
- modal mobile 대응
- text overflow
- semantic token 사용
- dark mode contrast
- focus style dark mode 가시성
- raw color 하드코딩 여부

---

### [실무]

Review Agent 판단 Flow:

```text
Mobile View 확인
→ Tablet View 확인
→ Desktop View 확인
→ Overflow 확인
→ Breakpoint 일관성 확인
→ Token 사용 확인
→ Theme 전환 확인
→ Dark Mode Contrast 확인
→ Interaction State 확인
→ Final Review
```

Review 결과 기준:

```text
Approved
→ mobile/tablet/desktop 안정 + token 사용 + dark mode contrast OK

Needs Fix
→ 일부 breakpoint 불일치, text overflow, hover/focus 색상 누락

Rejected
→ 모바일 가로 스크롤, modal 조작 불가, table overflow 방치, dark mode contrast 심각
```

---

### [FAQ]

Q. Review Agent는 desktop 화면만 보면 돼?
A. 아니다. mobile, tablet, desktop을 모두 확인해야 한다.

Q. 반응형에서 가장 심각한 문제는 뭐야?
A. 모바일 가로 스크롤, fixed width, modal 조작 불가, table overflow 방치가 치명적이다.

Q. Dark Mode 리뷰에서 가장 중요한 것은 뭐야?
A. background와 text contrast, surface, border, hover, focus, disabled 상태가 모두 식별 가능한지다.

---

# 9. Part05 Quality Checklist

## 9.1 Responsive Theme Checklist

### [개념]

Part05 단계에서는 Responsive Styling, Breakpoint, Theme, Dark Mode 기준이 명확한지 검토한다.

이 단계는 다양한 화면 크기와 theme 전환 상황에서 UI가 안정적으로 유지되는지 판단하는 기준이다.

---

### [핵심]

Part05 체크리스트:

```md
## Responsive

- [ ] Mobile First 기준이 명확한가?
- [ ] fixed width 남용을 경고하는가?
- [ ] container pattern 기준이 있는가?
- [ ] grid / flex responsive 기준이 있는가?
- [ ] image overflow 기준이 있는가?
- [ ] text overflow 기준이 있는가?
- [ ] table responsive 기준이 있는가?
- [ ] modal responsive 기준이 있는가?

## Breakpoint

- [ ] common breakpoint 기준이 있는가?
- [ ] breakpoint 남발을 경고하는가?
- [ ] breakpoint token 또는 문서화 기준이 있는가?
- [ ] component-specific breakpoint 주의가 있는가?

## Theme

- [ ] semantic token 기반 theme 구조가 있는가?
- [ ] primitive / semantic / component token 책임이 구분되는가?
- [ ] raw color 하드코딩을 경고하는가?
- [ ] theme와 responsive 책임이 분리되어 있는가?

## Dark Mode

- [ ] dark mode가 단순 배경 변경이 아님을 명시하는가?
- [ ] text / surface / border / hover / disabled / focus 기준이 있는가?
- [ ] color-scheme 기준이 있는가?
- [ ] user preference / system preference 기준이 있는가?

## Agent Review

- [ ] Frontend Agent 생성 규칙이 있는가?
- [ ] Review Agent 검토 규칙이 있는가?
- [ ] Retrieval Queries가 충분한가?
```

---

### [실무]

Part05 승인 기준:

```text
Responsive 기준 명확
+ Breakpoint 기준 명확
+ Theme token 구조 명확
+ Dark Mode contrast 기준 포함
+ Agent 생성 / 검토 기준 포함
+ FAQ 충분
+ Retrieval Queries 포함
→ Part05 승인 가능
```

Part05 보류 기준:

```text
desktop 중심 설명
또는 fixed width 방치
또는 breakpoint 기준 없음
또는 theme raw color 남용
또는 dark mode를 배경색 변경만으로 설명
또는 mobile / modal / table 대응 누락
→ 재작성 필요
```

---

### [FAQ]

Q. Part05의 핵심 목적은 뭐야?
A. 반응형, breakpoint, theme, dark mode 기준을 고정해 다양한 화면과 theme에서 UI가 안정적으로 유지되게 하는 것이다.

Q. Part05에서 가장 위험한 문제는 뭐야?
A. desktop 중심 설계, fixed width, 모바일 가로 스크롤, theme raw color, dark mode contrast 누락이다.

Q. Part05 다음에는 뭘 다루는 게 자연스러워?
A. Accessibility Styling, Focus Style, CSS Specificity, Override, Utility Class, Style Duplication을 다루는 것이 자연스럽다.

---

# Retrieval Queries

### [FAQ]

Q. Responsive Architecture가 뭐야?
A. 화면 크기에 따라 layout, component, image, modal, table, navigation이 자연스럽게 변하도록 관리하는 스타일 구조다.

Q. Responsive Styling은 media query만 추가하면 돼?
A. 아니다. layout 구조, width 전략, image, table, modal, touch target까지 함께 검토해야 한다.

Q. Mobile First가 뭐야?
A. 모바일 스타일을 기본으로 작성하고 큰 화면 스타일을 media query로 확장하는 방식이다.

Q. Mobile First는 왜 좋아?
A. 작은 화면에서 먼저 안정적인 구조를 만들고 큰 화면에서 확장하기 때문에 반응형 깨짐을 줄이기 쉽다.

Q. 반응형에서 가장 흔한 문제는 뭐야?
A. 고정 width, 큰 이미지, flex-wrap 누락, table overflow, modal width 고정이다.

Q. 모바일에서 가로 스크롤이 생기는 이유는 뭐야?
A. fixed width, 큰 이미지, 긴 텍스트, flex item min-width, table overflow가 원인일 수 있다.

Q. max-width media query를 쓰면 안 돼?
A. 금지는 아니지만 Mobile First 구조에서는 min-width 기반 확장이 더 일관적이다.

Q. Breakpoint는 뭐야?
A. 화면 크기에 따라 스타일이 바뀌는 기준점이다.

Q. breakpoint는 꼭 768, 1024를 써야 해?
A. 아니다. 일반 기준일 뿐이며 실제 콘텐츠가 깨지는 지점을 기준으로 조정할 수 있다.

Q. 컴포넌트마다 breakpoint가 달라도 돼?
A. 가능하지만 너무 많으면 관리가 어려워진다. 공통 breakpoint를 우선 사용한다.

Q. breakpoint도 token으로 관리해야 해?
A. 권장된다. 프로젝트 전체 반응형 기준을 통일하기 위해 필요하다.

Q. CSS variable로 media query breakpoint를 만들 수 있어?
A. 일반적인 media query 조건에서는 직접 사용하기 어렵다. SCSS variable, Tailwind config, 문서화 방식이 더 안정적이다.

Q. Tailwind에서는 breakpoint를 어디서 관리해?
A. `tailwind.config.js`의 `theme.screens`에서 관리한다.

Q. Container Pattern은 뭐야?
A. 콘텐츠의 최대 너비와 좌우 여백을 일관되게 관리하는 layout pattern이다.

Q. Container Pattern은 왜 필요해?
A. 화면 크기와 관계없이 콘텐츠 폭과 좌우 여백을 안정적으로 유지하기 위해 필요하다.

Q. width: 1200px만 쓰면 안 돼?
A. 모바일에서 가로 스크롤이 생길 수 있다. `max-width`나 `width: min()`을 사용하는 것이 좋다.

Q. Container는 컴포넌트마다 넣어도 돼?
A. 권장하지 않는다. page layout이나 layout utility에서 관리하는 것이 좋다.

Q. Grid와 Flex 중 뭐를 써야 해?
A. 2차원 배치는 Grid, 한 방향 정렬과 wrapping은 Flex가 적합하다.

Q. flex item이 줄어들지 않아?
A. `min-width: 0`이 필요할 수 있다.

Q. card grid는 어떻게 반응형 처리해?
A. `repeat(auto-fit, minmax(...))` 또는 breakpoint별 column 변경을 사용할 수 있다.

Q. 모바일에서 table이 깨지면 어떻게 해?
A. wrapper에 `overflow-x: auto`를 적용하거나 모바일 카드형 UI로 전환할 수 있다.

Q. table에 width: 100%만 주면 충분해?
A. 아니다. column이 많으면 내용이 압축되거나 화면을 밀어낼 수 있다.

Q. table을 모바일에서 카드로 바꿔도 돼?
A. 가능하다. 데이터 구조와 사용성을 고려해 선택해야 한다.

Q. 모바일에서 modal이 화면을 넘으면 어떻게 해?
A. `width: min(100% - 여백, max-width)`와 `max-height`, `overflow-y: auto`를 적용한다.

Q. modal width를 600px로 고정해도 돼?
A. 권장하지 않는다. 작은 화면에서 overflow가 발생할 수 있다.

Q. modal에도 focus style이 필요해?
A. 필요하다. close button, input, action button의 keyboard 조작이 가능해야 한다.

Q. 이미지가 모바일에서 화면을 넘으면 어떻게 해?
A. `max-width: 100%`와 container 기준 width를 적용한다.

Q. object-fit은 언제 써?
A. 이미지 비율을 유지하면서 정해진 영역을 채우거나 맞출 때 사용한다.

Q. aspect-ratio는 왜 필요해?
A. 이미지 로딩 전 공간을 확보해 layout shift를 줄이는 데 도움이 된다.

Q. 긴 텍스트가 카드 밖으로 나가면 어떻게 해?
A. `overflow-wrap: break-word`, `min-width: 0`, line clamp, ellipsis 등을 검토한다.

Q. ellipsis를 쓰면 항상 좋아?
A. 아니다. 중요한 정보가 잘릴 수 있으므로 필요한 경우 tooltip이나 상세 화면을 제공해야 한다.

Q. Theme Architecture는 뭐야?
A. 색상, 배경, 텍스트, border, shadow 같은 스타일 값을 theme별로 전환할 수 있도록 설계하는 방식이다.

Q. Theme 구조는 어떻게 설계해?
A. Primitive Token → Semantic Token → Theme Override → Component Style 구조가 좋다.

Q. Theme를 만들 때 raw color를 직접 쓰면 안 돼?
A. 컴포넌트에서는 raw color보다 semantic token을 사용하는 것이 theme 확장에 좋다.

Q. semantic token이 theme에 왜 중요해?
A. 컴포넌트 코드를 수정하지 않고 theme별 token 값만 바꿔 UI를 전환할 수 있기 때문이다.

Q. primitive token과 semantic token은 뭐가 달라?
A. primitive token은 실제 색상값이고 semantic token은 UI 역할을 표현한다.

Q. 작은 프로젝트도 primitive token을 꼭 나눠야 해?
A. 필수는 아니다. 작은 프로젝트는 semantic token 중심으로 시작해도 충분하다.

Q. component token은 언제 필요해?
A. 디자인 시스템 규모에서 특정 컴포넌트의 theme 세부 제어가 필요할 때 사용할 수 있다.

Q. Dark Mode는 뭐야?
A. 어두운 배경과 밝은 텍스트를 기준으로 UI를 전환하는 theme의 한 종류다.

Q. Dark Mode를 만들려면 모든 색상을 다시 써야 해?
A. 컴포넌트가 semantic token을 사용한다면 theme token 값만 바꿔도 많은 부분을 대응할 수 있다.

Q. Dark Mode에서 단순히 배경만 검게 하면 돼?
A. 아니다. 텍스트, border, surface, hover, disabled, focus, icon 색상까지 함께 조정해야 한다.

Q. Dark Mode에서 꼭 확인할 것은 뭐야?
A. background, text, surface, border, hover, disabled, focus, icon, shadow, contrast를 확인해야 한다.

Q. color-scheme은 왜 써?
A. 브라우저 기본 form control, scrollbar 등이 theme에 맞게 표시되도록 돕는다.

Q. Dark Mode는 class 방식과 data-theme 방식 중 뭐가 좋아?
A. 둘 다 가능하다. 중요한 것은 프로젝트 전체에서 일관되게 사용하는 것이다.

Q. prefers-color-scheme만 쓰면 충분해?
A. 사용자 직접 선택을 저장해야 한다면 localStorage나 별도 상태 관리가 필요하다.

Q. theme 전환 시 깜빡임이 생기면 어떻게 해?
A. 초기 렌더 전에 theme attribute를 적용하는 전략을 고려해야 한다.

Q. Responsive와 Theme는 같은 기준으로 관리해?
A. 아니다. Responsive는 layout 축이고 Theme은 color / visual token 축이다.

Q. media query 안에서 색상을 바꿔도 돼?
A. 가능하지만 theme token을 우회하는 raw color 반복은 피해야 한다.

Q. dark mode도 모바일에서 따로 확인해야 해?
A. 필요하다. dark mode token이 모바일 layout과 함께 적용될 때 깨지는 경우가 있을 수 있다.

Q. Frontend Agent가 breakpoint를 임의로 추가해도 돼?
A. 기존 breakpoint를 먼저 확인해야 한다. 임의 breakpoint는 필요한 이유가 명확해야 한다.

Q. Frontend Agent가 반응형에서 가장 먼저 확인할 것은 뭐야?
A. 모바일 기본 구조, 고정 width, overflow, 기존 breakpoint를 먼저 확인해야 한다.

Q. Frontend Agent가 dark mode에서 색상을 직접 지정해도 돼?
A. 가능하면 semantic token을 사용해야 한다. raw color 반복은 theme 확장을 어렵게 만든다.

Q. Review Agent는 responsive에서 뭘 검토해?
A. Mobile First, breakpoint 일관성, mobile 가로 스크롤, fixed width, grid/flex wrapping, image/table/modal overflow를 검토한다.

Q. Review Agent는 Dark Mode에서 뭘 검토해?
A. background와 text contrast, surface, border, hover, focus, disabled 상태가 모두 식별 가능한지 검토한다.

Q. Review Agent는 desktop 화면만 보면 돼?
A. 아니다. mobile, tablet, desktop을 모두 확인해야 한다.

Q. 반응형에서 가장 심각한 문제는 뭐야?
A. 모바일 가로 스크롤, fixed width, modal 조작 불가, table overflow 방치가 치명적이다.

Q. Part05의 핵심 목적은 뭐야?
A. 반응형, breakpoint, theme, dark mode 기준을 고정해 다양한 화면과 theme에서 UI가 안정적으로 유지되게 하는 것이다.

Q. Part05에서 가장 위험한 문제는 뭐야?
A. desktop 중심 설계, fixed width, 모바일 가로 스크롤, theme raw color, dark mode contrast 누락이다.

Q. Part05 다음에는 뭘 다루는 게 자연스러워?
A. Accessibility Styling, Focus Style, CSS Specificity, Override, Utility Class, Style Duplication을 다루는 것이 자연스럽다.
