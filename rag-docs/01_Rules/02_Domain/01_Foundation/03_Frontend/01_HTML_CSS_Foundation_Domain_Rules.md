# HTML CSS Foundation Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

HTML CSS Foundation Domain 문서는 Frontend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- HTML 기본 구조 이해
- Semantic HTML 작성 지원
- CSS 기본 문법 이해
- Layout 구현 지원
- Responsive Web Design 지원
- Accessibility 기초 지원
- Frontend 화면 구조 설계 지원
- Backend API 연동 전 UI Foundation 구성 지원
- React Component 작성 전 HTML/CSS 기반 이해 지원

---

### [핵심]

우선순위:

1. Semantic HTML
2. CSS Core Syntax
3. Layout System
4. Responsive Design
5. Accessibility
6. Maintainable Styling
7. Frontend Component Foundation
8. Practical UI Implementation

---

### [실무]

2026 실무 기준에서 HTML/CSS Foundation 문서는 단순 태그 암기용 문서가 아니다.

Frontend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- 화면 구조 설계
- 컴포넌트 마크업 작성
- CSS Layout 구현
- 반응형 UI 구성
- 접근성 기본 검토
- React JSX 변환 전 HTML 구조 설계
- UI 문제 원인 분석
- CSS 충돌 및 우선순위 검토

---

### [FAQ]

Q. HTML CSS Foundation 문서는 사람 공부용 문서야?

A.
아니다. AI Agent가 Frontend 화면을 만들고 검토하기 위한 RAG 문서다.

Q. HTML과 CSS를 왜 Level 3 Frontend Foundation에 먼저 둬야 해?

A.
React, Router, State Management 이전에 화면 구조와 스타일링의 기본이 HTML/CSS이기 때문이다.

Q. HTML CSS 문서에서 가장 중요한 기준은 뭐야?

A.
Semantic HTML, Layout, Responsive Design, Accessibility, Maintainable Styling이다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

HTML CSS Foundation 문서는 Frontend 기본 화면 구현에 필요한 범위를 포함한다.

포함 범위:

- HTML Document Structure
- Semantic HTML
- Text Element
- Link / Image
- List / Table
- Form Element
- Input / Label
- Button
- HTML Attribute
- Accessibility Basics
- SEO Basics
- CSS Syntax
- Selector
- Specificity
- Cascade
- Box Model
- Display
- Position
- Flexbox
- Grid
- Responsive Design
- Media Query
- Typography
- Color
- Spacing
- CSS Variable
- Pseudo Class
- Pseudo Element
- Transition Basics
- Reset / Normalize
- CSS Architecture Basics
- Component Styling Foundation

---

### [핵심]

반드시 포함:

- HTML은 구조
- CSS는 표현
- Semantic HTML은 의미 전달
- CSS Layout은 Flexbox / Grid 중심
- 반응형은 Mobile First 기준
- 접근성은 label, alt, button, heading 구조 중심
- React JSX로 변환 가능한 구조 고려

---

### [실무]

HTML/CSS 문서는 React 프로젝트의 기초 문서로 사용된다.

실무 연결:

```text
HTML Structure
→ CSS Styling
→ Responsive Layout
→ Component Markup
→ React JSX
→ Frontend Page
```

---

### [FAQ]

Q. CSS Framework 문서도 여기에 포함해?

A.
아니다. Tailwind, Bootstrap, Styled Components 같은 심화 도구는 별도 문서에서 다룬다.

Q. React 문법도 이 문서에 포함해?

A.
아니다. HTML/CSS Foundation은 React 이전의 화면 구조와 스타일링 기초만 다룬다.

Q. SEO 심화도 포함해?

A.
아니다. title, meta, heading, semantic tag 같은 기초만 포함한다.

---

## 2.2 Excluded Scope

### [개념]

HTML CSS Foundation 문서에서는 고급 Frontend Architecture를 제외한다.

제외 범위:

- React Core 심화
- Next.js App Router
- CSS-in-JS 심화
- Tailwind CSS 심화
- Design System 심화
- Animation Library
- Canvas / SVG 심화
- WebGL
- Frontend Build Tool 심화
- Performance Profiling 심화
- Browser Rendering Engine 심화

---

### [핵심]

제외 이유:

- Foundation 범위 초과
- React / TypeScript / Design System 문서와 분리 필요
- Agent Retrieval 혼선 방지
- Chunk 품질 유지

---

### [실무]

고급 기술은 별도 Domain Rules에서 관리한다.

예:

```text
HTML CSS Foundation
→ JavaScript Foundation
→ React Core
→ React Component Design
→ UI Component Pattern
→ Frontend Architecture
```

---

### [FAQ]

Q. CSS-in-JS는 여기서 다뤄?

A.
아니다. CSS-in-JS는 React Component Design 또는 Frontend Architecture 문서에서 다룬다.

Q. Tailwind CSS는 여기서 다뤄?

A.
아니다. Tailwind는 Utility CSS 도구로 별도 문서가 적합하다.

Q. CSS 애니메이션 심화는 여기서 다뤄?

A.
아니다. transition 기초만 포함하고 animation 심화는 별도 문서로 분리한다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

HTML CSS Foundation RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

Required:

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

### [핵심]

필수 Section 목적:

- [개념]: 정의와 역할
- [핵심]: 검색 친화 키워드
- [실무]: 실제 화면 구현 기준
- [FAQ]: 사용자 질문 매칭 강화

---

### [실무]

각 문서는 아래 구조를 기본으로 한다.

```md
# Topic

## Sub Topic

### [개념]

### [핵심]

### [실무]

### [FAQ]
```

---

### [FAQ]

Q. 모든 HTML/CSS 문서에 FAQ가 필요해?

A.
필요하다. FAQ는 사용자 질문과 RAG 검색 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

HTML/CSS 문서에는 실무 적용과 검증을 위해 추가 Section을 포함할 수 있다.

Strongly Recommended:

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

### [핵심]

추천 Section 사용 기준:

- Layout 설명 → [Flow], [예제], [Comparison]
- Accessibility 설명 → [Checklist], [주의]
- CSS 충돌 설명 → [Troubleshooting]
- Semantic HTML 설명 → [Best Practice]

---

### [실무]

예시:

```md
### [Flow]

HTML Structure
→ CSS Layout
→ Responsive Check
→ Accessibility Check
```

---

### [FAQ]

Q. HTML/CSS 문서에 Troubleshooting이 필요한 이유는?

A.
CSS 적용 안 됨, 레이아웃 깨짐, 반응형 문제 같은 실무 오류가 자주 발생하기 때문이다.

Q. Comparison은 언제 쓰면 좋아?

A.
Flexbox vs Grid, class vs id, inline vs block처럼 헷갈리는 개념을 비교할 때 사용한다.

---

# 4. HTML Core Rules

## 4.1 HTML Document Structure

### [개념]

HTML Document Structure는 웹 페이지의 기본 골격이다.

기본 구성:

```html
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Page Title</title>
  </head>
  <body>
    <main>
      <h1>Content Title</h1>
    </main>
  </body>
</html>
```

---

### [핵심]

반드시 설명:

- `<!doctype html>`은 HTML5 문서 선언
- `html lang="ko"`는 문서 언어 지정
- `head`는 메타데이터 영역
- `body`는 사용자에게 보이는 콘텐츠 영역
- `meta viewport`는 반응형 화면의 기본
- `title`은 브라우저 탭과 SEO에 사용

---

### [실무]

React 프로젝트에서는 전체 HTML 문서 구조를 직접 자주 작성하지 않지만, 기본 구조 이해는 필수다.

CRA / Vite / Next.js에서도 아래 개념은 유지된다.

- root element
- viewport
- document language
- title
- meta tag
- body content

---

### [FAQ]

Q. React를 써도 HTML 문서 구조를 알아야 해?

A.
알아야 한다. React도 결국 HTML 구조를 브라우저에 렌더링하기 때문이다.

Q. viewport meta가 없으면 어떻게 돼?

A.
모바일 화면에서 반응형 레이아웃이 의도대로 동작하지 않을 수 있다.

Q. lang 속성은 왜 필요해?

A.
스크린 리더, 검색 엔진, 브라우저가 문서 언어를 이해하는 데 필요하다.

---

## 4.2 Semantic HTML Rules

### [개념]

Semantic HTML은 태그의 의미를 기준으로 구조를 작성하는 방식이다.

예:

```html
<header>Header</header>
<nav>Navigation</nav>
<main>Main Content</main>
<section>Section</section>
<article>Article</article>
<aside>Aside</aside>
<footer>Footer</footer>
```

---

### [핵심]

반드시 포함:

- `header`: 상단 영역
- `nav`: 주요 탐색 영역
- `main`: 페이지 핵심 콘텐츠
- `section`: 주제별 구역
- `article`: 독립 콘텐츠
- `aside`: 보조 콘텐츠
- `footer`: 하단 정보
- `button`: 동작
- `a`: 이동

---

### [실무]

Semantic HTML은 Accessibility와 SEO에 직접 연결된다.

권장 Flow:

```text
Content Meaning
→ Semantic Tag Selection
→ Heading Structure
→ Accessibility Check
→ CSS Styling
```

금지:

- 모든 영역을 `div`로만 작성
- 클릭 동작에 `a` 태그 남용
- 페이지 이동에 `button` 사용
- 의미 없는 heading 사용

---

### [FAQ]

Q. div를 쓰면 안 돼?

A.
아니다. 의미 있는 태그가 없을 때는 div를 사용할 수 있다. 다만 모든 구조를 div로만 작성하면 좋지 않다.

Q. button과 a 태그 차이는?

A.
button은 동작 실행, a는 페이지 이동이나 URL 이동에 사용한다.

Q. section과 article 차이는?

A.
section은 주제 구역이고 article은 독립적으로 재사용 가능한 콘텐츠다.

---

## 4.3 Heading Rules

### [개념]

Heading은 문서의 제목 계층을 표현한다.

예:

```html
<h1>Page Title</h1>
<h2>Section Title</h2>
<h3>Sub Section Title</h3>
```

---

### [핵심]

규칙:

- 한 페이지의 핵심 제목은 `h1`
- 큰 구역은 `h2`
- 하위 구역은 `h3`
- heading level을 건너뛰지 않음
- 글자 크기 조절 목적으로 heading 사용 금지

---

### [실무]

Heading 구조는 스크린 리더와 SEO에 중요하다.

좋은 구조:

```text
h1
→ h2
  → h3
→ h2
  → h3
```

나쁜 구조:

```text
h1
→ h4
→ h2
```

---

### [FAQ]

Q. h1을 여러 개 써도 돼?

A.
가능은 하지만 일반적인 페이지에서는 핵심 제목 하나를 h1로 두는 구조가 명확하다.

Q. 글자를 크게 만들려고 h1을 써도 돼?

A.
안 된다. 글자 크기는 CSS로 조절하고 heading은 문서 구조 표현에 사용한다.

---

## 4.4 Form Rules

### [개념]

Form은 사용자 입력을 받는 HTML 구조다.

예:

```html
<form>
  <label for="email">Email</label>
  <input id="email" name="email" type="email" />

  <button type="submit">Submit</button>
</form>
```

---

### [핵심]

반드시 포함:

- `form`
- `label`
- `input`
- `textarea`
- `select`
- `button`
- `name`
- `type`
- `required`
- `placeholder`
- `disabled`

---

### [실무]

Form 작성 기준:

- input에는 label 연결
- button type 명시
- placeholder를 label 대체로 사용하지 않음
- 필수 입력은 required 또는 validation 처리
- 에러 메시지는 입력 필드와 가까운 곳에 배치

---

### [FAQ]

Q. label 없이 placeholder만 써도 돼?

A.
권장하지 않는다. placeholder는 입력 안내이고 label은 입력 항목의 이름이다.

Q. button type을 꼭 써야 해?

A.
form 안에서는 명시하는 것이 좋다. 기본 submit 동작 때문에 의도치 않은 제출이 발생할 수 있다.

Q. input name은 왜 필요해?

A.
폼 데이터 식별과 서버 전송, 자동화 처리에서 입력 필드를 구분하는 데 필요하다.

---

# 5. CSS Core Rules

## 5.1 CSS Syntax Rules

### [개념]

CSS는 HTML 요소의 스타일을 정의하는 언어다.

기본 구조:

```css
.selector {
  property: value;
}
```

예:

```css
.card {
  padding: 16px;
  border-radius: 12px;
  background-color: #ffffff;
}
```

---

### [핵심]

반드시 설명:

- selector는 스타일 적용 대상
- property는 스타일 속성
- value는 속성 값
- 선언은 세미콜론으로 구분
- class selector는 재사용에 적합
- id selector는 우선순위가 높아 남용 금지

---

### [실무]

CSS 문서는 실무 예제 중심으로 작성한다.

권장:

- class 기반 스타일링
- 의미 있는 class name
- 중복 스타일 최소화
- 긴 selector 체인 금지
- inline style 남용 금지

---

### [FAQ]

Q. CSS에서 class와 id 중 뭐를 주로 써?

A.
재사용성과 유지보수성을 위해 class를 주로 사용한다.

Q. inline style은 쓰면 안 돼?

A.
간단한 동적 스타일에는 가능하지만 일반 스타일링은 CSS class로 분리하는 것이 좋다.

---

## 5.2 Selector Rules

### [개념]

Selector는 CSS가 어떤 HTML 요소에 적용될지 결정한다.

예:

```css
button {
  cursor: pointer;
}

.primary-button {
  background-color: blue;
}

#main-title {
  font-size: 32px;
}
```

---

### [핵심]

필수 포함:

- Type Selector
- Class Selector
- ID Selector
- Descendant Selector
- Child Selector
- Attribute Selector
- Pseudo Class
- Pseudo Element

---

### [실무]

권장 selector:

```css
.card {
}
.card-title {
}
.card-description {
}
```

주의할 selector:

```css
body div section article div p span {
}
```

긴 selector chain은 유지보수를 어렵게 만든다.

---

### [FAQ]

Q. CSS selector는 짧을수록 좋아?

A.
대체로 그렇다. 너무 긴 selector는 재사용성과 유지보수성을 떨어뜨린다.

Q. id selector를 쓰면 안 돼?

A.
쓸 수 있지만 우선순위가 높아 스타일 충돌 해결을 어렵게 만들 수 있다.

---

## 5.3 Cascade and Specificity Rules

### [개념]

Cascade는 여러 CSS 규칙이 충돌할 때 어떤 스타일이 적용되는지 결정하는 규칙이다.

Specificity는 selector의 우선순위 점수다.

---

### [핵심]

우선순위 기준:

1. `!important`
2. Inline Style
3. ID Selector
4. Class / Attribute / Pseudo Class
5. Type Selector
6. 작성 순서

---

### [실무]

금지:

- `!important` 남용
- id selector 남용
- inline style 남용
- 불필요하게 깊은 selector
- CSS 파일 순서 의존

권장:

- class 기반 스타일
- 명확한 naming
- component 단위 스타일 분리
- 충돌 가능한 공통 class 최소화

---

### [FAQ]

Q. CSS가 적용되지 않을 때 가장 먼저 뭘 확인해?

A.
selector 오타, 파일 import 여부, 우선순위, 작성 순서, 브라우저 개발자 도구 computed style을 확인한다.

Q. !important를 쓰면 해결되는 거 아니야?

A.
일시적으로 해결될 수 있지만 장기적으로 스타일 충돌을 더 어렵게 만든다.

---

## 5.4 Box Model Rules

### [개념]

Box Model은 HTML 요소가 차지하는 공간을 계산하는 방식이다.

구성:

```text
Content
→ Padding
→ Border
→ Margin
```

---

### [핵심]

필수 포함:

- width
- height
- padding
- border
- margin
- box-sizing
- content-box
- border-box

권장 설정:

```css
* {
  box-sizing: border-box;
}
```

---

### [실무]

실무에서는 `border-box`를 기본으로 사용하는 경우가 많다.

이유:

- width 계산이 직관적
- padding과 border 포함
- 레이아웃 계산 오류 감소
- 반응형 UI 작성에 유리

---

### [FAQ]

Q. box-sizing: border-box는 왜 써?

A.
요소의 width와 height에 padding과 border가 포함되어 레이아웃 계산이 쉬워진다.

Q. margin과 padding 차이는?

A.
padding은 요소 내부 여백이고 margin은 요소 외부 여백이다.

---

# 6. CSS Layout Rules

## 6.1 Display Rules

### [개념]

display는 요소가 화면에서 배치되는 방식을 결정한다.

주요 값:

```css
display: block;
display: inline;
display: inline-block;
display: flex;
display: grid;
display: none;
```

---

### [핵심]

반드시 설명:

- block은 한 줄 전체 차지
- inline은 콘텐츠 크기만 차지
- inline-block은 inline 흐름 + box 크기 지정 가능
- flex는 1차원 layout
- grid는 2차원 layout
- none은 화면과 접근성 트리에서 제거

---

### [실무]

Layout 선택 기준:

```text
Simple Text Flow → block / inline
Horizontal or Vertical Alignment → flex
Page or Card Grid Layout → grid
Hide Element → display none
```

---

### [FAQ]

Q. Flexbox와 Grid 중 뭐를 써야 해?

A.
한 방향 정렬은 Flexbox, 행과 열이 모두 중요한 2차원 배치는 Grid가 적합하다.

Q. display none은 접근성에 영향 있어?

A.
있다. display none 요소는 화면뿐 아니라 접근성 트리에서도 제거된다.

---

## 6.2 Flexbox Rules

### [개념]

Flexbox는 1차원 레이아웃을 구현하는 CSS Layout 방식이다.

예:

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
}
```

---

### [핵심]

필수 포함:

- display: flex
- flex-direction
- justify-content
- align-items
- gap
- flex-wrap
- flex-grow
- flex-shrink
- flex-basis

---

### [실무]

Flexbox 적합 상황:

- 버튼 정렬
- 카드 내부 정렬
- header navigation
- icon + text 정렬
- 중앙 정렬
- row / column layout

기본 Flow:

```text
Parent Container
→ display flex
→ main axis 설정
→ cross axis 정렬
→ gap 설정
→ wrap 여부 결정
```

---

### [FAQ]

Q. justify-content와 align-items 차이는?

A.
justify-content는 main axis 정렬이고 align-items는 cross axis 정렬이다.

Q. gap을 써도 돼?

A.
가능하다. Flexbox와 Grid에서 요소 간 간격을 관리할 때 margin보다 명확한 경우가 많다.

Q. Flexbox는 언제 쓰면 좋아?

A.
한 줄 또는 한 방향 중심의 정렬과 배치에 적합하다.

---

## 6.3 Grid Rules

### [개념]

CSS Grid는 행과 열을 기준으로 2차원 레이아웃을 구현하는 방식이다.

예:

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
```

---

### [핵심]

필수 포함:

- display: grid
- grid-template-columns
- grid-template-rows
- gap
- repeat
- minmax
- auto-fit
- auto-fill
- grid-column
- grid-row

---

### [실무]

Grid 적합 상황:

- 카드 목록
- 상품 목록
- 갤러리
- 대시보드
- 전체 페이지 레이아웃
- 행/열 기준이 중요한 UI

반응형 예:

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
}
```

---

### [FAQ]

Q. Grid는 Flexbox보다 좋은 거야?

A.
무조건 좋다는 의미가 아니다. Grid는 2차원 배치에 강하고 Flexbox는 1차원 정렬에 강하다.

Q. repeat(auto-fit, minmax())는 왜 써?

A.
화면 너비에 따라 가능한 만큼 컬럼을 자동 배치해 반응형 카드 레이아웃을 만들기 좋다.

---

## 6.4 Position Rules

### [개념]

position은 요소의 위치 기준을 설정한다.

주요 값:

```css
position: static;
position: relative;
position: absolute;
position: fixed;
position: sticky;
```

---

### [핵심]

반드시 설명:

- static은 기본 위치
- relative는 원래 위치 기준 이동
- absolute는 가장 가까운 positioned ancestor 기준 배치
- fixed는 viewport 기준 고정
- sticky는 스크롤 위치에 따라 고정
- z-index는 stacking order 제어

---

### [실무]

주의:

- absolute 사용 시 부모에 relative 필요 여부 확인
- fixed header는 body padding 고려
- z-index 숫자 남용 금지
- position으로 layout 전체를 억지 구현하지 않음
- 기본 layout은 Flexbox / Grid 우선

---

### [FAQ]

Q. absolute가 이상한 위치로 가는 이유는?

A.
기준이 되는 positioned parent가 없으면 viewport 또는 상위 기준으로 배치될 수 있다.

Q. z-index가 안 먹는 이유는?

A.
position, stacking context, 부모 요소의 z-index, transform 속성 등을 확인해야 한다.

---

# 7. Responsive Design Rules

## 7.1 Responsive Web Design

### [개념]

Responsive Web Design은 화면 크기에 따라 UI가 자연스럽게 변하는 설계 방식이다.

기본 요소:

- Fluid Layout
- Flexible Image
- Media Query
- Relative Unit
- Mobile First

---

### [핵심]

반드시 포함:

- viewport meta
- media query
- rem / em / %
- min-width / max-width
- flexible grid
- image max-width
- mobile first

예:

```css
.container {
  width: min(100% - 32px, 1200px);
  margin: 0 auto;
}

img {
  max-width: 100%;
  height: auto;
}
```

---

### [실무]

Mobile First 권장 Flow:

```text
Mobile Base Style
→ Tablet Media Query
→ Desktop Media Query
→ Large Screen Optimization
```

예:

```css
.card-list {
  display: grid;
  grid-template-columns: 1fr;
}

@media (min-width: 768px) {
  .card-list {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .card-list {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

---

### [FAQ]

Q. Mobile First가 뭐야?

A.
모바일 화면 스타일을 기본으로 작성하고 큰 화면 스타일을 media query로 확장하는 방식이다.

Q. px를 쓰면 안 돼?

A.
쓸 수 있다. 다만 폰트, 간격, 레이아웃에는 rem, %, minmax 같은 유연한 단위를 함께 고려한다.

Q. 이미지 반응형은 어떻게 처리해?

A.
일반적으로 `max-width: 100%`와 `height: auto`를 사용한다.

---

## 7.2 Media Query Rules

### [개념]

Media Query는 화면 크기나 환경 조건에 따라 CSS를 다르게 적용하는 기능이다.

예:

```css
@media (min-width: 768px) {
  .layout {
    display: flex;
  }
}
```

---

### [핵심]

필수 포함:

- min-width
- max-width
- breakpoint
- mobile first
- desktop first
- orientation
- prefers-reduced-motion

---

### [실무]

권장 breakpoint 예시:

```text
Mobile: default
Tablet: 768px+
Desktop: 1024px+
Wide: 1280px+
```

주의:

- 무분별한 breakpoint 생성 금지
- 특정 기기명 기준 설계 지양
- 콘텐츠가 깨지는 지점을 기준으로 breakpoint 설정
- CSS 중복 최소화

---

### [FAQ]

Q. breakpoint는 정해진 값이 있어?

A.
고정 정답은 없다. 일반 기준은 있지만 실제로는 콘텐츠가 깨지는 지점을 기준으로 잡는 것이 좋다.

Q. max-width와 min-width 중 뭐가 좋아?

A.
Mobile First에서는 min-width를 사용하는 방식이 일반적으로 관리하기 쉽다.

---

# 8. Accessibility Rules

## 8.1 Accessibility Basics

### [개념]

Accessibility는 다양한 사용자가 웹 콘텐츠를 사용할 수 있도록 만드는 기준이다.

HTML/CSS Foundation에서는 접근성 기초를 반드시 포함한다.

---

### [핵심]

필수 포함:

- semantic tag
- heading structure
- alt text
- label
- button
- focus state
- keyboard navigation
- color contrast
- aria basics

---

### [실무]

기본 Checklist:

```md
- [ ] 이미지에 적절한 alt가 있는가?
- [ ] input과 label이 연결되어 있는가?
- [ ] 클릭 가능한 요소가 button 또는 a로 작성되었는가?
- [ ] 키보드로 이동 가능한가?
- [ ] focus style이 보이는가?
- [ ] heading 순서가 자연스러운가?
- [ ] 색상만으로 정보를 전달하지 않는가?
```

---

### [FAQ]

Q. 접근성은 나중에 해도 돼?

A.
나중에 고치면 비용이 커진다. HTML 구조를 작성할 때부터 기본 접근성을 고려하는 것이 좋다.

Q. aria를 많이 쓰면 접근성이 좋아져?

A.
아니다. 먼저 Semantic HTML을 사용하고, 부족한 의미를 보완할 때만 aria를 사용한다.

Q. focus outline을 제거해도 돼?

A.
제거만 하면 안 된다. 제거할 경우 반드시 대체 focus style을 제공해야 한다.

---

## 8.2 Image Alt Rules

### [개념]

alt는 이미지의 대체 텍스트다.

예:

```html
<img src="festival.jpg" alt="야간 축제 무대 전경" />
```

---

### [핵심]

규칙:

- 의미 있는 이미지는 설명 alt 작성
- 장식 이미지는 빈 alt 사용 가능
- 파일명 그대로 alt 작성 금지
- "이미지"라는 단어 반복 불필요
- 콘텐츠 맥락에 맞게 작성

---

### [실무]

예:

```html
<!-- 의미 있는 이미지 -->
<img src="map.png" alt="서울 강남구 축제 위치 지도" />

<!-- 장식 이미지 -->
<img src="decor-line.svg" alt="" />
```

---

### [FAQ]

Q. 모든 이미지에 alt가 필요해?

A.
필요하다. 의미 있는 이미지는 설명을 넣고 장식 이미지는 빈 alt를 사용할 수 있다.

Q. alt에 “이미지”라고 써야 해?

A.
대부분 필요 없다. 스크린 리더가 이미 이미지임을 알려줄 수 있다.

---

# 9. Typography and Visual Style Rules

## 9.1 Typography Rules

### [개념]

Typography는 글자의 크기, 굵기, 줄 간격, 계층 구조를 설계하는 방식이다.

---

### [핵심]

필수 포함:

- font-family
- font-size
- font-weight
- line-height
- letter-spacing
- text-align
- hierarchy
- rem unit

---

### [실무]

권장:

```css
body {
  font-family: system-ui, sans-serif;
  line-height: 1.5;
}

.title {
  font-size: 2rem;
  font-weight: 700;
}

.description {
  font-size: 1rem;
  line-height: 1.6;
}
```

주의:

- 너무 작은 font-size 금지
- line-height 누락 주의
- heading 구조와 시각 계층 일치
- 폰트 과다 사용 금지

---

### [FAQ]

Q. font-size는 px와 rem 중 뭐가 좋아?

A.
고정값이 필요한 경우 px도 가능하지만 접근성과 확장성을 위해 rem 사용을 고려한다.

Q. line-height는 왜 중요해?

A.
줄 간격은 가독성에 직접 영향을 준다.

---

## 9.2 Color Rules

### [개념]

Color는 UI의 정보 구조와 시각적 강조를 만든다.

---

### [핵심]

필수 포함:

- text color
- background color
- border color
- semantic color
- contrast
- hover color
- disabled color
- CSS variable

---

### [실무]

권장:

```css
:root {
  --color-primary: #2563eb;
  --color-text: #111827;
  --color-muted: #6b7280;
  --color-border: #e5e7eb;
  --color-background: #ffffff;
}
```

주의:

- 색상만으로 상태 전달 금지
- contrast 부족 주의
- 하드코딩 색상 남용 금지
- semantic token 사용 권장

---

### [FAQ]

Q. CSS variable은 왜 써?

A.
색상, 간격, 폰트 크기 같은 디자인 값을 일관되게 관리하기 위해 사용한다.

Q. 색상만으로 에러를 표시해도 돼?

A.
안 된다. 텍스트, 아이콘, 메시지 등 다른 정보도 함께 제공해야 한다.

---

# 10. CSS Maintainability Rules

## 10.1 Naming Rules

### [개념]

CSS Naming은 class 이름을 일관되게 작성하는 규칙이다.

---

### [핵심]

권장:

- 의미 기반 이름
- component 기반 이름
- 재사용 가능한 이름
- 과도한 축약 금지
- 시각적 이름 남용 금지

예:

```css
.festival-card {
}
.festival-card-title {
}
.festival-card-description {
}
```

---

### [실무]

좋은 예:

```css
.search-form {
}
.search-input {
}
.search-button {
}
```

나쁜 예:

```css
.blue-box {
}
.big-text {
}
.abc {
}
.box1 {
}
```

---

### [FAQ]

Q. class 이름은 디자인 기준으로 지어도 돼?

A.
가능하지만 색상이나 크기처럼 쉽게 바뀌는 시각 속성보다 역할과 의미 중심이 좋다.

Q. BEM을 꼭 써야 해?

A.
필수는 아니다. 다만 component 기반 naming 원칙은 유지하는 것이 좋다.

---

## 10.2 CSS Variable Rules

### [개념]

CSS Variable은 재사용 가능한 스타일 값을 정의하는 방식이다.

예:

```css
:root {
  --spacing-md: 16px;
  --radius-card: 12px;
}
```

---

### [핵심]

사용 대상:

- color
- spacing
- font-size
- border-radius
- shadow
- z-index
- transition duration

---

### [실무]

예:

```css
.card {
  padding: var(--spacing-md);
  border-radius: var(--radius-card);
}
```

장점:

- 디자인 일관성 유지
- 전역 수정 용이
- theme 확장 가능
- 중복 감소

---

### [FAQ]

Q. CSS Variable은 언제 쓰면 좋아?

A.
여러 곳에서 반복되는 색상, 간격, radius, shadow 같은 디자인 값을 관리할 때 좋다.

Q. 모든 값을 variable로 만들어야 해?

A.
아니다. 반복 사용되거나 의미 있는 design token 중심으로 만든다.

---

## 10.3 Reset and Normalize Rules

### [개념]

Reset / Normalize는 브라우저 기본 스타일 차이를 줄이기 위한 CSS 초기화 방식이다.

---

### [핵심]

반드시 설명:

- browser default style
- reset css
- normalize css
- box-sizing
- margin reset
- font inheritance

예:

```css
* {
  box-sizing: border-box;
}

body {
  margin: 0;
}
```

---

### [실무]

기본 Reset 예:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: system-ui, sans-serif;
}

img {
  max-width: 100%;
  display: block;
}
```

주의:

- 과도한 reset은 기본 접근성 스타일을 제거할 수 있음
- focus style 제거 금지
- 프로젝트 기준 reset 파일 분리 권장

---

### [FAQ]

Q. Reset CSS는 꼭 필요해?

A.
프로젝트 일관성을 위해 사용하는 경우가 많다. 다만 접근성에 필요한 기본 스타일을 제거하지 않도록 주의해야 한다.

Q. img에 display block을 주는 이유는?

A.
inline 이미지의 하단 여백 문제를 줄이고 레이아웃 제어를 쉽게 하기 위해 사용한다.

---

# 11. Code Example Rules

## 11.1 Example Style

### [개념]

HTML/CSS 예제는 짧고 직접적이어야 한다.

목적:

- Retrieval
- Code Generation
- Review
- Debugging

---

### [핵심]

권장:

- 핵심 구조만 포함
- 긴 전체 페이지 코드 금지
- HTML과 CSS 연결 예제 포함
- 의미 있는 class name 사용
- 접근성 기준 반영
- 반응형 예제 포함

금지:

- 불필요한 boilerplate
- 과도한 디자인 코드
- 의미 없는 lorem ipsum 남용
- inline style 중심 예제
- div만 사용하는 예제

---

### [실무]

좋은 예:

```html
<section class="festival-card">
  <h2 class="festival-card-title">Festival Title</h2>
  <p class="festival-card-description">Festival description</p>
  <button type="button" class="festival-card-button">View Detail</button>
</section>
```

```css
.festival-card {
  padding: 16px;
  border: 1px solid var(--color-border);
  border-radius: 12px;
}
```

---

### [FAQ]

Q. 예제 코드는 길수록 좋아?

A.
아니다. RAG 문서에서는 짧고 검색 가능한 예제가 더 좋다.

Q. 예제에 접근성도 반영해야 해?

A.
해야 한다. label, alt, button type, heading 구조 같은 기본 기준은 예제에 반영한다.

---

# 12. Troubleshooting Rules

## 12.1 CSS Not Applied

### [개념]

CSS가 적용되지 않는 문제는 Frontend 실무에서 자주 발생한다.

---

### [핵심]

문제:

- CSS 작성했는데 화면에 적용되지 않음

원인:

- CSS 파일 import 누락
- selector 오타
- className 오타
- specificity 충돌
- 작성 순서 문제
- browser cache
- scoped style 범위 문제

해결:

- 개발자 도구 Elements 확인
- class 적용 여부 확인
- computed style 확인
- CSS 파일 import 확인
- 우선순위 확인
- cache 새로고침

---

### [실무]

Debug Flow:

```text
Element Inspect
→ Class Exists Check
→ CSS Rule Loaded Check
→ Specificity Check
→ Override Rule Check
→ Fix Selector or Structure
```

---

### [FAQ]

Q. CSS가 안 먹을 때 제일 먼저 볼 것은?

A.
브라우저 개발자 도구에서 해당 요소에 class가 실제로 적용되어 있는지 확인한다.

Q. className 오타도 흔한 원인이야?

A.
맞다. React에서는 class가 아니라 className을 사용하므로 오타를 확인해야 한다.

---

## 12.2 Layout Broken

### [개념]

Layout Broken은 요소가 예상 위치에서 벗어나거나 화면이 깨지는 문제다.

---

### [핵심]

문제:

- 요소가 삐져나감
- 카드가 줄바꿈되지 않음
- 모바일에서 가로 스크롤 발생
- 중앙 정렬 실패

원인:

- width 고정
- flex-wrap 누락
- min-width 문제
- overflow 처리 누락
- box-sizing 누락
- image width 문제

해결:

- `box-sizing: border-box`
- `max-width: 100%`
- `flex-wrap: wrap`
- `min-width: 0`
- Grid `minmax()` 사용
- overflow 원인 요소 확인

---

### [실무]

가로 스크롤 Debug Flow:

```text
Viewport Check
→ Overflow Element Inspect
→ Fixed Width Check
→ Image Width Check
→ Flex/Grid Item min-width Check
→ Responsive Rule Fix
```

---

### [FAQ]

Q. 모바일에서 가로 스크롤이 생기는 이유는?

A.
고정 width, 큰 이미지, 긴 텍스트, flex item의 min-width 문제 등이 원인일 수 있다.

Q. flex item 내부 텍스트가 안 줄어드는 이유는?

A.
flex item의 기본 min-width 때문에 발생할 수 있으며 `min-width: 0`이 필요할 수 있다.

---

## 12.3 Z-Index Problem

### [개념]

z-index 문제는 요소의 앞뒤 배치가 예상과 다르게 나타나는 문제다.

---

### [핵심]

문제:

- modal이 header 뒤에 가려짐
- dropdown이 card 뒤에 가려짐
- z-index를 높여도 변화 없음

원인:

- stacking context
- position 미설정
- 부모 요소 z-index
- transform / opacity / filter 사용
- overflow hidden

해결:

- position 확인
- stacking context 확인
- 부모 overflow 확인
- z-index scale 정의
- modal root 분리 고려

---

### [실무]

Debug Flow:

```text
Target Element Inspect
→ position Check
→ Parent Stacking Context Check
→ overflow Check
→ z-index Token Check
→ Portal or DOM Position Review
```

---

### [FAQ]

Q. z-index를 9999로 줬는데도 안 되는 이유는?

A.
부모 stacking context나 overflow hidden 때문에 가려질 수 있다.

Q. z-index 숫자는 크게 주면 좋은 거야?

A.
아니다. 프로젝트 기준 z-index scale을 정해서 관리하는 것이 좋다.

---

# 13. Comparison Rules

## 13.1 Required Comparisons

### [개념]

HTML/CSS 문서는 헷갈리는 개념을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- div vs semantic tag
- button vs a
- block vs inline vs inline-block
- Flexbox vs Grid
- margin vs padding
- relative vs absolute
- px vs rem vs %
- min-width vs max-width
- class vs id
- display none vs visibility hidden
- Reset CSS vs Normalize CSS

---

### [실무]

예시:

| 비교      | Flexbox                      | Grid                            |
| --------- | ---------------------------- | ------------------------------- |
| 기준      | 1차원 Layout                 | 2차원 Layout                    |
| 방향      | row 또는 column 중심         | row + column                    |
| 적합      | 정렬, navbar, card 내부      | 카드 목록, 갤러리, 대시보드     |
| 핵심 속성 | justify-content, align-items | grid-template-columns, grid-row |

---

### [FAQ]

Q. 비교 표는 왜 필요해?

A.
사용자가 헷갈리는 질문을 했을 때 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. 모든 개념을 비교해야 해?

A.
아니다. 실무에서 자주 혼동되는 개념만 비교한다.

---

# 14. Checklist Rules

## 14.1 Document Quality Checklist

### [개념]

HTML/CSS 문서 검수 시 품질 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] Semantic HTML 기준이 포함되었는가?
- [ ] HTML 구조 예제가 포함되었는가?
- [ ] CSS 기본 문법이 포함되었는가?
- [ ] Selector / Specificity 설명이 있는가?
- [ ] Box Model 설명이 있는가?
- [ ] Flexbox 예제가 포함되었는가?
- [ ] Grid 예제가 포함되었는가?
- [ ] Responsive Design 기준이 포함되었는가?
- [ ] Accessibility 기준이 포함되었는가?
- [ ] Troubleshooting이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 기준:

```text
Draft
→ Required Section Check
→ Example Check
→ FAQ Check
→ Retrieval Query Check
→ Domain Scope Check
→ Final Review
```

---

### [FAQ]

Q. HTML/CSS 문서 검수에서 가장 중요한 것은?

A.
Semantic HTML, Layout, Responsive Design, Accessibility, FAQ, Retrieval Queries 포함 여부다.

---

# 15. Retrieval Optimization Rules

## 15.1 Keyword Rules

### [개념]

HTML CSS Foundation 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- HTML
- HTML Document Structure
- Semantic HTML
- HTML Tag
- Heading
- Form
- Input
- Label
- Button
- Link
- Image Alt
- Accessibility
- SEO Basics
- CSS
- CSS Syntax
- Selector
- Specificity
- Cascade
- Box Model
- Display
- Position
- Flexbox
- Grid
- Responsive Design
- Media Query
- Mobile First
- Typography
- Color
- CSS Variable
- Reset CSS
- Normalize CSS
- Frontend Foundation
- Component Markup
- React JSX Foundation

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- HTML 기본 구조는?
- Semantic HTML 왜 써?
- div만 쓰면 안 돼?
- button과 a 차이는?
- CSS가 안 먹는 이유는?
- Flexbox와 Grid 차이는?
- 가운데 정렬 어떻게 해?
- 반응형 CSS 어떻게 작성해?
- media query 어떻게 써?
- 모바일에서 가로 스크롤 생기는 이유는?
- z-index 왜 안 먹어?
- label은 왜 필요해?
- alt는 왜 필요해?

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. FAQ 질문은 어떤 스타일이 좋아?

A.
실제 사용자가 검색하거나 질문할 법한 문장형 질문이 좋다.

---

# 16. Version Rules

## 16.1 Modern HTML CSS 기준

### [개념]

HTML CSS Foundation 문서는 Modern HTML / Modern CSS 기준으로 작성한다.

---

### [핵심]

기준:

- HTML5
- Semantic HTML
- Modern CSS
- Flexbox
- Grid
- CSS Variable
- Responsive Design
- Mobile First
- Accessibility Basics
- Browser DevTools Debugging

Legacy 제외:

- table layout 중심 설명
- float layout 중심 설명
- XHTML 중심 설명
- 오래된 IE 대응 중심 설명
- vendor prefix 중심 설명
- image sprite 중심 설명

---

### [실무]

실무 기준:

```text
Semantic HTML
→ CSS Layout
→ Responsive Design
→ Accessibility
→ Component-based UI
```

---

### [FAQ]

Q. float layout도 배워야 해?

A.
기존 코드 유지보수에서는 볼 수 있지만 신규 레이아웃 학습과 작성은 Flexbox와 Grid를 우선한다.

Q. table로 layout을 잡아도 돼?

A.
안 된다. table은 표 데이터 표현에 사용하고 layout은 CSS Layout을 사용한다.

---

# 17. Common Mistakes

## 17.1 HTML CSS Common Mistakes

### [개념]

HTML/CSS Foundation 문서는 자주 발생하는 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

- 모든 구조를 div로만 작성
- button과 a 역할 혼동
- heading level 건너뜀
- label 없이 input 작성
- placeholder를 label로 사용
- alt 누락
- CSS selector 오타
- className 오타
- id selector 남용
- !important 남용
- box-sizing 누락
- fixed width 남용
- flex-wrap 누락
- media query 과다 생성
- z-index 숫자 남용
- focus outline 제거
- 색상만으로 상태 전달
- inline style 남용
- Reset CSS로 접근성 스타일 제거

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: 모바일에서 레이아웃 깨짐
원인: 고정 width, flex-wrap 누락
해결: max-width, flex-wrap, responsive grid 적용
```

---

### [FAQ]

Q. HTML/CSS 초보가 가장 많이 하는 실수는?

A.
div 남용, CSS 우선순위 혼동, box model 오해, 반응형 미고려, 접근성 누락이 많다.

Q. CSS 문제는 어떻게 찾는 게 좋아?

A.
브라우저 개발자 도구에서 element, class, computed style, layout box를 확인한다.

---

# 18. Final Goal

## 18.1 Domain Final Goal

### [개념]

HTML CSS Foundation RAG 문서는 Frontend Agent가 화면 구조와 기본 스타일을 정확히 작성하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- HTML 기본 구조 작성
- Semantic HTML 선택
- Form Markup 작성
- CSS 기본 문법 이해
- CSS Selector 검토
- Specificity 문제 분석
- Box Model 이해
- Flexbox Layout 구현
- Grid Layout 구현
- Responsive Design 작성
- Media Query 작성
- Accessibility 기본 검토
- CSS Troubleshooting 수행
- React Component Markup Foundation 제공

---

### [실무]

Agent 수행 가능 작업:

```text
User UI Request
→ Semantic HTML Structure
→ CSS Layout
→ Responsive Rule
→ Accessibility Check
→ React JSX Conversion Ready Markup
```

---

### [FAQ]

Q. HTML CSS Foundation 문서의 최종 목적은 뭐야?

A.
Frontend Agent가 React 이전 단계의 화면 구조, 스타일, 반응형, 접근성 기초를 안정적으로 생성하고 검토하게 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
JavaScript Foundation, TypeScript Foundation, React Core, React Component Design 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. HTML CSS Foundation 문서는 왜 필요해?
A. Frontend Agent가 React 화면을 만들기 전에 HTML 구조와 CSS Layout 기초를 이해해야 하기 때문이다.

Q. HTML 기본 구조는 뭐야?
A. `doctype`, `html`, `head`, `meta`, `title`, `body`로 구성되며 실제 콘텐츠는 body 안에 작성한다.

Q. Semantic HTML이 뭐야?
A. 태그의 의미를 기준으로 HTML 구조를 작성하는 방식이다.

Q. Semantic HTML은 왜 써?
A. 접근성, SEO, 유지보수성, 문서 구조 이해에 도움이 된다.

Q. div만 쓰면 안 돼?
A. div도 사용할 수 있지만 header, nav, main, section, article, footer 같은 의미 태그를 우선 고려해야 한다.

Q. button과 a 태그 차이는?
A. button은 동작 실행, a는 URL 이동이나 페이지 이동에 사용한다.

Q. h1 h2 h3는 어떻게 써?
A. h1은 페이지 핵심 제목, h2는 큰 구역, h3는 하위 구역처럼 계층 구조에 맞게 사용한다.

Q. input에 label은 왜 필요해?
A. 사용자가 입력 항목을 이해하고 스크린 리더가 필드를 올바르게 안내하기 위해 필요하다.

Q. placeholder를 label 대신 써도 돼?
A. 권장하지 않는다. placeholder는 입력 예시이고 label은 입력 항목의 이름이다.

Q. img alt는 왜 필요해?
A. 이미지가 보이지 않거나 스크린 리더를 사용할 때 이미지 의미를 전달하기 위해 필요하다.

Q. CSS 기본 문법은 뭐야?
A. selector로 대상을 선택하고 property와 value로 스타일을 선언한다.

Q. CSS selector는 뭐야?
A. CSS를 적용할 HTML 요소를 선택하는 규칙이다.

Q. class와 id 차이는?
A. class는 재사용에 적합하고 id는 고유 식별에 사용되며 CSS 우선순위가 높다.

Q. CSS 우선순위는 어떻게 결정돼?
A. important, inline style, id, class, type selector, 작성 순서에 따라 결정된다.

Q. CSS가 안 먹는 이유는?
A. CSS import 누락, selector 오타, className 오타, specificity 충돌, 작성 순서 문제가 원인일 수 있다.

Q. Box Model이 뭐야?
A. 요소의 공간을 content, padding, border, margin으로 계산하는 방식이다.

Q. margin과 padding 차이는?
A. padding은 요소 내부 여백이고 margin은 요소 외부 여백이다.

Q. box-sizing border-box는 왜 써?
A. width와 height 계산에 padding과 border가 포함되어 레이아웃 계산이 쉬워진다.

Q. display block inline 차이는?
A. block은 한 줄 전체를 차지하고 inline은 콘텐츠 크기만큼만 차지한다.

Q. Flexbox는 언제 써?
A. 한 방향 정렬, 중앙 정렬, 버튼 그룹, 카드 내부 정렬에 적합하다.

Q. Grid는 언제 써?
A. 카드 목록, 갤러리, 대시보드처럼 행과 열이 모두 중요한 2차원 레이아웃에 적합하다.

Q. Flexbox와 Grid 차이는?
A. Flexbox는 1차원 레이아웃, Grid는 2차원 레이아웃에 적합하다.

Q. justify-content와 align-items 차이는?
A. justify-content는 main axis 정렬이고 align-items는 cross axis 정렬이다.

Q. position absolute가 이상한 위치로 가는 이유는?
A. 기준이 되는 positioned parent가 없기 때문일 수 있다.

Q. z-index가 안 먹는 이유는?
A. stacking context, position, parent z-index, overflow hidden 등이 원인일 수 있다.

Q. 반응형 CSS는 어떻게 작성해?
A. Mobile First 기준으로 기본 스타일을 작성하고 min-width media query로 큰 화면을 확장한다.

Q. media query는 왜 써?
A. 화면 크기나 환경 조건에 따라 다른 CSS를 적용하기 위해 사용한다.

Q. Mobile First가 뭐야?
A. 모바일 스타일을 기본으로 작성하고 태블릿, 데스크톱 스타일을 점진적으로 추가하는 방식이다.

Q. 모바일에서 가로 스크롤이 생기는 이유는?
A. 고정 width, 큰 이미지, 긴 텍스트, flex item min-width, overflow 문제 때문일 수 있다.

Q. CSS Variable은 왜 써?
A. 색상, 간격, radius 같은 디자인 값을 일관되게 관리하기 위해 사용한다.

Q. Reset CSS는 왜 써?
A. 브라우저 기본 스타일 차이를 줄이고 프로젝트 스타일 기준을 통일하기 위해 사용한다.

Q. Accessibility 기본 체크는 뭐야?
A. semantic tag, heading 구조, label, alt, keyboard navigation, focus style, color contrast를 확인한다.

Q. focus outline을 지워도 돼?
A. 지우기만 하면 안 된다. 반드시 대체 focus style을 제공해야 한다.

Q. HTML CSS 문서에서 FAQ가 중요한 이유는?
A. 실제 사용자 질문과 RAG Retrieval Query Matching을 강화하기 위해 중요하다.

Q. HTML CSS Foundation 다음 문서는 뭐가 좋아?
A. JavaScript Foundation, TypeScript Foundation, React Core, React Component Design 순서가 좋다.
