# Styling Architecture Part07 - File Structure, Import Order, Troubleshooting, Agent Rules

---

# 1. Styling File Structure Rules

## 1.1 Styling File Structure

### [개념]

Styling File Structure는 스타일 파일을 프로젝트 안에서 어디에 배치할지 정하는 규칙이다.

Styling File Structure는 스타일 탐색성, 유지보수성, Agent Retrieval 품질에 직접 영향을 준다.

좋은 파일 구조는 다음 질문에 답할 수 있어야 한다.

- 전역 스타일은 어디에 있는가?
- token은 어디에 있는가?
- reset은 어디에 있는가?
- component style은 어디에 있는가?
- page layout style은 어디에 있는가?
- utility style은 어디에 있는가?
- theme style은 어디에 있는가?

---

### [핵심]

권장 스타일 파일 책임:

```text
reset.css
→ 브라우저 기본 스타일 초기화

tokens.css
→ color, spacing, typography, radius, shadow, z-index token

theme.css
→ light / dark theme token override

globals.css
→ body, root, base element style

typography.css
→ heading, paragraph, text baseline

utilities.css
→ sr-only, container, stack, flex-center

Component.module.css
→ component-specific style

Page.module.css
→ page layout style
```

권장 구조:

```text
src/
├─ styles/
│  ├─ reset.css
│  ├─ tokens.css
│  ├─ theme.css
│  ├─ globals.css
│  ├─ typography.css
│  └─ utilities.css
├─ components/
│  └─ Button/
│     ├─ Button.jsx
│     └─ Button.module.css
├─ pages/
│  └─ MainPage/
│     ├─ MainPage.jsx
│     └─ MainPage.module.css
└─ layouts/
   └─ AppLayout/
      ├─ AppLayout.jsx
      └─ AppLayout.module.css
```

---

### [실무]

구조 판단 기준:

```md
- [ ] 전역 스타일 파일이 `src/styles`에 분리되어 있는가?
- [ ] reset, token, theme, global, utility 책임이 분리되어 있는가?
- [ ] component style이 component와 가까운 위치에 있는가?
- [ ] page layout style이 page 단위로 분리되어 있는가?
- [ ] theme style이 token 구조와 연결되어 있는가?
- [ ] style import 순서가 명확한가?
```

파일 위치 결정 Flow:

```text
Style 작성 요청
→ Global / Component / Page / Layout / Utility / Theme 책임 확인
→ 기존 Styling Method 확인
→ 기존 File Structure 확인
→ 알맞은 파일 위치 선택
→ Import Order 확인
→ Review Agent 검토
```

---

### [FAQ]

Q. 스타일 파일은 컴포넌트 옆에 두는 게 좋아?
A. 컴포넌트 전용 스타일이라면 가까이 두는 것이 유지보수에 좋다.

Q. 모든 CSS를 styles 폴더에 모아도 돼?
A. 가능하지만 컴포넌트가 많아지면 어떤 스타일이 어디에 쓰이는지 추적하기 어려울 수 있다.

Q. styles 폴더에는 무엇을 넣어야 해?
A. reset, tokens, theme, globals, typography, utilities처럼 전역 기준 스타일을 넣는 것이 좋다.

Q. page style과 component style은 나눠야 해?
A. 권장된다. page는 layout, component는 개별 UI 외형과 상태를 담당하는 것이 좋다.

---

## 1.2 Global Styles Folder Rules

### [개념]

Global Styles Folder는 애플리케이션 전체에 영향을 주는 스타일 파일을 모아두는 위치다.

Global Styles Folder는 컴포넌트 디자인을 모아두는 곳이 아니다.

---

### [핵심]

Global Styles Folder에 적합:

- reset.css
- tokens.css
- theme.css
- globals.css
- typography.css
- utilities.css
- fonts.css
- print.css

Global Styles Folder에 부적합:

- Button.module.css
- Card.module.css
- LoginPage.module.css
- Modal variant style
- 특정 page layout
- 특정 domain component style

---

### [실무]

권장 구조 예:

```text
src/styles/
├─ reset.css
├─ tokens.css
├─ theme.css
├─ globals.css
├─ typography.css
└─ utilities.css
```

Global Styles Folder 리뷰 기준:

```md
- [ ] styles 폴더가 전역 기준 스타일만 담당하는가?
- [ ] 특정 컴포넌트 스타일이 styles 폴더에 몰려 있지 않은가?
- [ ] token과 theme 파일이 구분되어 있는가?
- [ ] utility class 범위가 과도하게 넓지 않은가?
```

---

### [FAQ]

Q. Button.css를 styles 폴더에 넣어도 돼?
A. 가능은 하지만 Button 전용 스타일이라면 Button 컴포넌트 폴더에 두는 것이 추적하기 쉽다.

Q. utilities.css는 styles 폴더에 넣어도 돼?
A. 가능하다. 전역으로 재사용하는 작은 utility class는 styles 폴더에 두는 것이 일반적이다.

Q. theme.css는 어디에 둬?
A. 보통 `src/styles/theme.css` 또는 `src/styles/themes/`에 둔다.

---

## 1.3 Component Style File Rules

### [개념]

Component Style File은 특정 컴포넌트의 외형, 내부 layout, variant, state를 담당하는 스타일 파일이다.

Component Style File은 해당 컴포넌트와 가까운 위치에 두는 것이 좋다.

---

### [핵심]

Component Style File에 포함:

- component root style
- component child element style
- variant style
- size style
- hover / focus / disabled / error state
- component internal layout
- component-specific responsive

Component Style File에 포함하지 않음:

- global reset
- app-wide token
- page container
- external layout margin
- unrelated utility
- 다른 컴포넌트 override

---

### [실무]

CSS Module 구조 예:

```text
src/components/Button/
├─ Button.jsx
├─ Button.module.css
└─ index.js
```

Component CSS 예:

```css
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-2);
  border-radius: var(--radius-md);
}

.primary {
  background: var(--color-primary);
  color: white;
}

.button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

리뷰 기준:

```md
- [ ] component style이 component와 가까운 위치에 있는가?
- [ ] variant와 state가 component style 안에서 관리되는가?
- [ ] page layout 책임이 component style에 들어가지 않았는가?
- [ ] token을 사용하고 있는가?
```

---

### [FAQ]

Q. Component Style File은 무엇을 담당해?
A. 특정 컴포넌트의 외형, 내부 배치, variant, state를 담당한다.

Q. Component Style File에 margin-bottom을 넣어도 돼?
A. 재사용 컴포넌트라면 외부 배치 margin은 부모 layout에서 관리하는 것이 좋다.

Q. CSS Module 파일은 꼭 컴포넌트 폴더에 둬야 해?
A. 필수는 아니지만 컴포넌트와 가까이 두는 것이 유지보수에 좋다.

---

## 1.4 Page and Layout Style Rules

### [개념]

Page Style은 특정 화면의 layout과 section 배치를 담당한다.

Layout Style은 여러 화면에서 반복되는 배치 구조를 담당한다.

Page Style과 Component Style을 섞으면 재사용성이 떨어진다.

---

### [핵심]

Page Style 담당:

- page container
- section spacing
- page-level grid
- page-specific layout
- content width
- responsive page structure

Layout Style 담당:

- AppLayout
- HeaderLayout
- SidebarLayout
- PageContainer
- Stack
- Grid
- Section

Component Style 담당하지 않는 것:

- page 전체 margin
- section 간격
- sidebar와 content 배치
- page-level grid column

---

### [실무]

Page Style 예:

```css
.mainPage {
  width: min(100% - 32px, 1200px);
  margin-inline: auto;
}

.section {
  margin-block: var(--spacing-8);
}

.cardGrid {
  display: grid;
  gap: var(--spacing-4);
}
```

Layout Component 구조 예:

```text
src/layouts/AppLayout/
├─ AppLayout.jsx
└─ AppLayout.module.css
```

리뷰 기준:

```md
- [ ] page layout이 page style에서 관리되는가?
- [ ] 재사용 layout은 layout component로 분리되어 있는가?
- [ ] component style이 page container를 강제하지 않는가?
- [ ] section spacing이 컴포넌트마다 중복되지 않는가?
```

---

### [FAQ]

Q. Page Style은 무엇을 담당해?
A. 특정 화면의 container, section spacing, page-level grid, responsive layout을 담당한다.

Q. Layout Style과 Page Style은 뭐가 달라?
A. Layout Style은 여러 화면에서 재사용되는 배치 구조이고, Page Style은 특정 화면에 종속된 배치다.

Q. section spacing은 어디서 관리해?
A. page style 또는 layout component에서 관리하는 것이 좋다.

---

# 2. Style Import Order Rules

## 2.1 Import Order

### [개념]

Style Import Order는 CSS 파일을 어떤 순서로 불러올지 정하는 규칙이다.

CSS는 같은 우선순위의 selector일 경우 나중에 import된 스타일이 앞선 스타일을 덮어쓸 수 있다.

Import Order가 불명확하면 스타일 충돌과 예측 불가능한 override가 발생한다.

---

### [핵심]

권장 import 순서:

```text
Reset
→ Token
→ Theme
→ Global
→ Typography
→ Utility
→ Layout
→ Page
→ Component
```

기본 원칙:

- reset은 가장 먼저 import
- token은 token 사용 파일보다 먼저 import
- theme은 base token 이후 import
- theme은 semantic token override를 담당
- global은 reset, token, theme 이후 import
- utility는 global 이후 import
- component style은 component에서 import
- page style은 page에서 import

---

### [실무]

React / CRA 예:

```js
import "./styles/reset.css";
import "./styles/tokens.css";
import "./styles/theme.css";
import "./styles/globals.css";
import "./styles/typography.css";
import "./styles/utilities.css";
```

Component import 예:

```jsx
import styles from "./Button.module.css";

function Button() {
  return <button className={styles.button}>저장</button>;
}
```

Import Order 리뷰 기준:

```md
- [ ] reset이 component style 뒤에 오지 않는가?
- [ ] token 파일이 token 사용 파일보다 먼저 import되는가?
- [ ] theme 파일이 token 이후 import되는가?
- [ ] global style이 component style을 불필요하게 덮어쓰지 않는가?
- [ ] CSS Module은 component에서 import되는가?
- [ ] theme 파일이 token 구조와 충돌하지 않는가?
```

---

### [FAQ]

Q. CSS import 순서가 중요해?
A. 중요하다. 같은 우선순위의 selector는 나중에 import된 스타일이 덮어쓸 수 있다.

Q. token 파일은 언제 import해야 해?
A. CSS variable을 사용하는 스타일보다 먼저 import되어야 한다.

Q. reset을 나중에 import하면 어떻게 돼?
A. component style이 reset에 의해 덮이거나 예상치 못하게 깨질 수 있다.

Q. Component CSS Module은 어디서 import해?
A. 해당 컴포넌트 파일에서 import하는 것이 일반적이다.

---

## 2.2 Theme Import Order

### [개념]

Theme Import Order는 theme token override가 base token, global style, component style과 충돌하지 않도록 관리하는 규칙이다.

Theme style은 token 구조를 확장하거나 override하는 역할이므로 base token 이후에 import해야 한다.

이 문서에서는 Part02와 Part05의 token / theme 기준과 일관되게 다음 순서를 권장한다.

```text
reset.css
→ tokens.css
→ theme.css
→ globals.css
→ typography.css
→ utilities.css
→ layout / page / component style
```

---

### [핵심]

Theme import 원칙:

- base token 이후 import
- global style보다 먼저 import 권장
- component style보다 먼저 import
- theme attribute selector 사용 가능
- raw color override 지양
- semantic token override 중심
- dark mode token은 component raw style을 우회하지 않아야 함

권장 구조:

```text
tokens.css
→ theme.css
→ globals.css
→ component style
```

theme.css를 globals.css보다 먼저 두는 이유:

- globals.css의 body background / text color가 theme token을 바로 참조할 수 있다.
- component style이 semantic token을 안정적으로 사용할 수 있다.
- Part02의 token-first 원칙과 Part05의 theme-token 원칙을 동시에 만족한다.

---

### [실무]

Theme import 예:

```js
import "./styles/reset.css";
import "./styles/tokens.css";
import "./styles/theme.css";
import "./styles/globals.css";
```

Theme CSS 예:

```css
:root {
  --color-background: #ffffff;
  --color-text: #111827;
}

[data-theme="dark"] {
  --color-background: #111827;
  --color-text: #f9fafb;
}
```

Component 사용 예:

```css
.card {
  background: var(--color-surface);
  color: var(--color-text);
  border: 1px solid var(--color-border);
}
```

리뷰 기준:

```md
- [ ] theme token이 base token 이후에 정의되는가?
- [ ] theme.css가 global / component style보다 먼저 import되는가?
- [ ] component가 semantic token을 사용해 theme 변경을 반영하는가?
- [ ] raw color 때문에 theme override가 무시되지 않는가?
- [ ] theme import 순서가 프로젝트 전체에서 일관적인가?
```

---

### [FAQ]

Q. theme.css는 tokens.css보다 먼저 import해도 돼?
A. 권장하지 않는다. theme은 token을 override하거나 확장하므로 base token 이후 import하는 것이 좋다.

Q. theme.css는 globals.css 앞에 와야 해 뒤에 와야 해?
A. 이 문서에서는 Part02 / Part05와의 일관성을 위해 `tokens.css → theme.css → globals.css` 순서를 권장한다.

Q. component에서 raw color를 쓰면 theme이 적용돼?
A. 적용되지 않을 수 있다. semantic token을 사용해야 theme 전환이 안정적이다.

Q. theme.css를 component style 뒤에 import해도 돼?
A. 권장하지 않는다. component style이 theme token을 안정적으로 참조하려면 theme.css가 먼저 로드되는 것이 좋다.

---

# 3. Styling Troubleshooting Rules

## 3.1 CSS Not Applied

### [개념]

CSS Not Applied는 작성한 스타일이 화면에 적용되지 않는 문제다.

CSS가 적용되지 않는 원인은 파일 import, className, scope, specificity, cache, build output 등 여러 가지가 있다.

Agent는 CSS가 안 먹는 문제를 `!important`로 바로 해결하면 안 된다.

---

### [핵심]

주요 원인:

- CSS 파일 import 누락
- className 오타
- CSS Module import 오류
- selector 우선순위 문제
- 작성 순서 문제
- scoped class와 global class 혼동
- browser cache
- Tailwind class purge 문제
- build output cache
- 잘못된 파일 위치
- component가 다른 className을 받고 있음

---

### [실무]

CSS Not Applied Flow:

```text
Element Inspect
→ className 적용 확인
→ CSS rule 로드 확인
→ computed style 확인
→ specificity 확인
→ import order 확인
→ scoped/global class 확인
→ cache 확인
→ 수정
```

CSS Module 확인:

```text
파일명이 *.module.css 인가?
→ import styles from "./Component.module.css" 인가?
→ className={styles.className} 형식인가?
→ 실제 CSS class가 존재하는가?
```

리뷰 기준:

```md
- [ ] className이 실제 DOM에 붙어 있는가?
- [ ] CSS 파일이 import되어 있는가?
- [ ] CSS Module 접근 방식이 올바른가?
- [ ] 다른 selector에 의해 override되고 있지 않은가?
- [ ] import order 문제가 아닌가?
```

---

### [FAQ]

Q. CSS가 안 먹을 때 제일 먼저 뭘 확인해?
A. 브라우저 개발자 도구에서 해당 요소에 class가 실제로 붙었는지 확인한다.

Q. CSS Module 스타일이 안 먹어?
A. `styles.className`으로 접근했는지, 파일명이 `module.css`인지, import가 맞는지 확인한다.

Q. CSS가 안 먹으면 !important를 쓰면 돼?
A. 최후 수단으로만 사용해야 한다. 먼저 import, className, specificity를 확인해야 한다.

Q. className은 붙었는데 스타일이 안 보여?
A. computed style에서 다른 CSS rule이 덮어쓰는지 확인해야 한다.

---

## 3.2 Style Conflict

### [개념]

Style Conflict는 여러 CSS 규칙이 같은 요소에 적용되어 의도와 다른 스타일이 나타나는 문제다.

Style Conflict는 전역 class 충돌, specificity 차이, import order, UI library style, reset 영향으로 자주 발생한다.

---

### [핵심]

Style Conflict 원인:

- 전역 class 이름 중복
- selector specificity 차이
- import order 문제
- UI library global style
- reset style 영향
- parent style inheritance
- media query override
- theme override 순서 문제
- CSS Module과 global class 혼동

---

### [실무]

Style Conflict 해결 Flow:

```text
DevTools Computed 확인
→ 적용된 CSS source 확인
→ selector specificity 확인
→ import order 확인
→ scope 분리
→ class naming 수정
→ token / variant 구조로 개선
→ global override 제거
```

Conflict 리뷰 기준:

```md
- [ ] 전역 class 이름이 중복되지 않는가?
- [ ] selector가 과하게 깊지 않은가?
- [ ] import order가 의도와 맞는가?
- [ ] global style이 component style을 덮지 않는가?
- [ ] UI library style과 충돌하지 않는가?
```

---

### [FAQ]

Q. 스타일이 자꾸 다른 곳에도 적용돼?
A. 전역 class 충돌 가능성이 높다. CSS Module이나 naming convention을 고려한다.

Q. import 순서 때문에 스타일이 바뀔 수 있어?
A. 그렇다. 같은 우선순위라면 나중에 import된 스타일이 적용될 수 있다.

Q. Style Conflict는 어떻게 찾는 게 좋아?
A. DevTools의 Computed 탭에서 어떤 CSS rule이 실제 적용되는지 확인한다.

Q. UI library 스타일과 충돌하면 어떻게 해?
A. 라이브러리 theme API, props, slot/className API를 먼저 확인하고 global override는 최소화한다.

---

## 3.3 Responsive Broken

### [개념]

Responsive Broken은 화면 크기 변화에 따라 layout이 깨지는 문제다.

Responsive Broken은 fixed width, image overflow, flex/grid 설정, table overflow, modal width 고정 때문에 자주 발생한다.

---

### [핵심]

Responsive Broken 원인:

- fixed width
- min-width 문제
- image max-width 누락
- flex-wrap 누락
- grid minmax 누락
- table overflow 누락
- modal width 고정
- long text overflow
- container padding 누락
- breakpoint 불일치

---

### [실무]

Responsive Broken Flow:

```text
Mobile Width 확인
→ 가로 스크롤 원인 요소 찾기
→ fixed width 확인
→ image / table 확인
→ flex item min-width 확인
→ modal width 확인
→ media query 확인
→ 수정
```

빠른 수정 기준:

```text
fixed width
→ max-width / width: min() 사용

image overflow
→ max-width: 100%

flex item overflow
→ min-width: 0

table overflow
→ wrapper overflow-x: auto

modal overflow
→ width: min(100% - 여백, max-width)
```

리뷰 기준:

```md
- [ ] 모바일 360px에서 가로 스크롤이 없는가?
- [ ] fixed width가 없는가?
- [ ] image가 container를 넘지 않는가?
- [ ] table wrapper overflow가 있는가?
- [ ] modal이 viewport를 넘지 않는가?
```

---

### [FAQ]

Q. 모바일에서 가로 스크롤이 생겨?
A. 고정 width, 큰 이미지, 긴 텍스트, flex item min-width, table overflow 문제가 원인일 수 있다.

Q. flex item이 줄어들지 않아?
A. `min-width: 0`이 필요할 수 있다.

Q. modal이 모바일 화면을 넘으면 어떻게 해?
A. `width: min(100% - 여백, max-width)`와 `max-height`, `overflow-y: auto`를 적용한다.

Q. table이 모바일에서 화면을 밀어내면 어떻게 해?
A. table wrapper에 `overflow-x: auto`를 적용한다.

---

## 3.4 Z-index Problem

### [개념]

Z-index Problem은 modal, dropdown, tooltip, toast 등이 예상한 순서로 겹쳐 보이지 않는 문제다.

Z-index 문제는 단순히 큰 숫자를 넣는다고 해결되지 않는다.

---

### [핵심]

Z-index Problem 원인:

- stacking context
- transform 사용
- opacity 사용
- filter 사용
- position 미설정
- 부모 overflow hidden
- z-index scale 부재
- portal 미사용
- modal / overlay / toast 우선순위 불명확

---

### [실무]

Z-index Problem Flow:

```text
Target Element 확인
→ position 확인
→ z-index token 확인
→ parent stacking context 확인
→ overflow hidden 확인
→ transform / opacity 확인
→ portal 필요 여부 확인
```

좋은 예:

```css
.overlay {
  z-index: var(--z-overlay);
}

.modal {
  z-index: var(--z-modal);
}

.toast {
  z-index: var(--z-toast);
}
```

리뷰 기준:

```md
- [ ] z-index token scale이 있는가?
- [ ] 9999 같은 임의 숫자를 남용하지 않는가?
- [ ] parent stacking context를 확인했는가?
- [ ] overflow hidden에 가려지지 않는가?
- [ ] portal이 필요한 UI인지 검토했는가?
```

---

### [FAQ]

Q. z-index를 9999로 줬는데도 안 돼?
A. 부모 stacking context나 overflow hidden 때문에 가려질 수 있다.

Q. dropdown이 card 뒤에 숨어?
A. 부모 요소의 overflow, stacking context, z-index를 확인해야 한다.

Q. modal은 z-index만 높이면 돼?
A. 아니다. overlay, stacking context, portal, focus management까지 함께 고려해야 한다.

---

## 3.5 Dark Mode Broken

### [개념]

Dark Mode Broken은 dark theme 전환 시 텍스트, 배경, border, icon, focus, disabled 상태가 식별되지 않는 문제다.

Dark Mode Broken은 raw color 하드코딩과 semantic token 부재 때문에 자주 발생한다.

---

### [핵심]

Dark Mode Broken 원인:

- raw color 하드코딩
- semantic token 미사용
- surface token 누락
- border token 누락
- muted text contrast 부족
- focus ring contrast 부족
- disabled opacity 과다
- icon 색상 고정
- shadow만으로 elevation 표현
- third-party library theme 미연동

---

### [실무]

Dark Mode Broken Flow:

```text
Theme 전환
→ background / text contrast 확인
→ surface / border 확인
→ raw color 검색
→ focus / hover / disabled 확인
→ icon visibility 확인
→ third-party theme 확인
→ semantic token으로 수정
```

나쁜 예:

```css
.card {
  background: white;
  color: black;
}
```

좋은 예:

```css
.card {
  background: var(--color-surface);
  color: var(--color-text);
  border: 1px solid var(--color-border);
}
```

리뷰 기준:

```md
- [ ] raw color가 theme 전환을 방해하지 않는가?
- [ ] text와 background contrast가 충분한가?
- [ ] surface와 border가 dark mode에서 구분되는가?
- [ ] focus / hover / disabled 상태가 dark mode에서 보이는가?
- [ ] icon 색상이 theme token을 따르는가?
```

---

### [FAQ]

Q. Dark Mode에서 글자가 안 보여?
A. raw color 하드코딩이나 contrast 부족 가능성이 높다. semantic token을 사용해야 한다.

Q. Dark Mode에서 border가 안 보여?
A. dark theme용 border token을 따로 정의해야 한다.

Q. Dark Mode에서 shadow가 잘 안 보여?
A. 어두운 배경에서는 shadow만으로 elevation이 부족할 수 있어 surface와 border를 함께 조정해야 한다.

---

# 4. Review Agent Rules

## 4.1 Styling Review Checklist

### [개념]

Review Agent는 스타일 구조 검토 시 화면 결과뿐 아니라 유지보수성, 반응형, 접근성, theme 확장성, 충돌 가능성을 함께 확인해야 한다.

Review Agent는 Styling Architecture Domain Rules를 기준으로 최종 승인 여부를 판단한다.

---

### [핵심]

Review Agent 전체 체크리스트:

```md
## Architecture

- [ ] Styling Method가 프로젝트 기준과 일치하는가?
- [ ] Global Style과 Component Style이 분리되어 있는가?
- [ ] Design Token이 정의되어 있는가?
- [ ] 색상 / 간격 / 폰트 / radius가 token으로 관리되는가?
- [ ] 스타일 파일 구조가 명확한가?

## CSS Quality

- [ ] 전역 class 충돌 가능성이 낮은가?
- [ ] selector가 과도하게 깊지 않은가?
- [ ] !important 남용이 없는가?
- [ ] inline style 남용이 없는가?
- [ ] 중복 스타일이 과하지 않은가?

## Component Style

- [ ] component style이 외부 layout에 과하게 의존하지 않는가?
- [ ] variant / size / state가 명확한가?
- [ ] hover / focus / disabled / error 상태가 있는가?
- [ ] props 기반 style 분기가 과하지 않은가?

## Responsive

- [ ] 모바일 화면에서 가로 스크롤이 없는가?
- [ ] breakpoint 기준이 일관적인가?
- [ ] card / grid / modal / table 반응형 처리가 있는가?

## Accessibility

- [ ] focus-visible 스타일이 있는가?
- [ ] color contrast가 충분한가?
- [ ] 색상만으로 상태를 전달하지 않는가?
- [ ] reduced motion을 고려했는가?

## Theme

- [ ] raw color가 컴포넌트에 흩어져 있지 않은가?
- [ ] semantic token을 사용하는가?
- [ ] dark mode 대응 구조가 있는가?
```

---

### [실무]

Review Agent 판단 Flow:

```text
Styling Method 확인
→ File Structure 확인
→ Token 사용 확인
→ Global / Component 분리 확인
→ Naming / Variant / State 확인
→ Responsive 확인
→ Accessibility Style 확인
→ Theme / Dark Mode 확인
→ Duplication 확인
→ Troubleshooting Risk 확인
→ Final Review
```

Review 결과 기준:

```text
Approved
→ 구조 일관성 + token 사용 + 반응형 OK + 접근성 치명 문제 없음

Needs Fix
→ 일부 raw value 반복, focus 누락, breakpoint 불일치, 중복 스타일 존재

Rejected
→ global 오염, 모바일 깨짐, 접근성 심각, !important 남용, dark mode contrast 심각
```

---

### [FAQ]

Q. Review Agent가 스타일 코드에서 가장 먼저 봐야 할 것은?
A. 스타일 방식의 일관성, 전역 충돌 가능성, token 사용 여부, 반응형과 접근성 스타일이다.

Q. 스타일이 화면상 예쁘면 승인해도 돼?
A. 아니다. 유지보수성, 반응형, 접근성, 중복, 충돌 가능성까지 검토해야 한다.

Q. Review Agent가 desktop 화면만 보면 돼?
A. 아니다. mobile, tablet, desktop과 theme 상태까지 확인해야 한다.

---

## 4.2 Review Severity Rules

### [개념]

Review Severity Rules는 스타일 문제의 심각도를 구분하는 기준이다.

모든 스타일 이슈가 같은 우선순위를 갖지는 않는다.

Review Agent는 Blocker, Major, Minor로 구분해 수정 우선순위를 판단할 수 있어야 한다.

---

### [핵심]

Blocker:

- 모바일에서 주요 기능 사용 불가
- modal 조작 불가
- 버튼 식별 불가
- focus style 완전 제거
- error 상태 전달 불가
- dark mode에서 텍스트 식별 불가
- layout collapse
- global override로 여러 화면 파손

Major:

- 일부 화면 responsive 깨짐
- token 미사용 반복
- component와 layout 책임 혼합
- variant / state 혼동
- !important 반복 사용
- table overflow 방치
- z-index 문제로 dropdown 일부 가림

Minor:

- 일부 spacing 불일치
- class naming 개선 필요
- transition duration 조정 필요
- utility class 정리 필요
- 일부 중복 스타일 존재

---

### [실무]

Severity 판단 예:

```text
focus outline 제거 + 대체 없음
→ Blocker

Button primary color raw value 반복
→ Major 또는 Minor

Card padding 16px / 17px 혼재
→ Minor

Mobile에서 가로 스크롤로 저장 버튼 접근 불가
→ Blocker

Dark Mode에서 muted text contrast 낮음
→ Major

class 이름이 box, temp
→ Minor 또는 Major
```

리뷰 결과 작성 기준:

```text
Issue
→ Severity
→ Location
→ Reason
→ Suggested Fix
```

---

### [FAQ]

Q. 모든 스타일 이슈가 Blocker야?
A. 아니다. 사용자 흐름을 막거나 접근성 치명 문제가 있으면 Blocker이고, 나머지는 영향도에 따라 구분한다.

Q. focus style 누락은 어느 정도 심각해?
A. 키보드 사용성을 막을 수 있으므로 심각도가 높다.

Q. spacing 조금 다른 것도 수정해야 해?
A. UI 일관성에는 영향을 주지만 보통 Blocker는 아니다.

---

# 5. Frontend Agent Rules

## 5.1 Styling Generation Rules

### [개념]

Frontend Agent는 스타일 코드를 생성할 때 프로젝트의 Styling Architecture를 따라야 한다.

Frontend Agent는 임의의 스타일링 방식, 임의 색상, 임의 breakpoint, 임의 override를 생성하면 안 된다.

---

### [핵심]

Frontend Agent 스타일 생성 기준:

```md
- [ ] 프로젝트의 스타일링 방식을 먼저 확인한다.
- [ ] raw color보다 token을 사용한다.
- [ ] component style과 layout style을 분리한다.
- [ ] hover / focus / disabled / error 상태를 포함한다.
- [ ] mobile first 기준으로 작성한다.
- [ ] fixed width를 남용하지 않는다.
- [ ] 접근성 스타일을 제거하지 않는다.
- [ ] class naming을 일관되게 작성한다.
- [ ] 중복 스타일은 component 또는 token으로 분리한다.
- [ ] global override를 최소화한다.
- [ ] !important를 최후 수단으로만 사용한다.
```

---

### [실무]

Frontend Agent 작업 Flow:

```text
Styling Request
→ Existing Styling Method 확인
→ Existing File Structure 확인
→ Token 확인
→ Component / Layout 책임 분리
→ Naming / Variant / State 정의
→ Responsive 적용
→ Accessibility State 적용
→ Theme 영향 확인
→ Duplication 제거
→ Review Agent 전달
```

좋은 생성 예:

```css
.festival-card {
  padding: var(--spacing-4);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background: var(--color-surface);
}

.festival-card__title {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-bold);
  color: var(--color-text);
}

.festival-card:focus-within {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

생성 금지 예:

```text
global.css에 특정 component style 추가
raw color 반복
focus outline 제거
width: 1200px 고정
button disabled를 class만으로 처리
error를 red 색상만으로 표현
!important 남용
기존 프로젝트와 다른 styling library 도입
```

---

### [FAQ]

Q. Frontend Agent가 스타일을 만들 때 가장 조심할 점은?
A. 프로젝트 기존 스타일 방식과 token 체계를 따르는 것이 가장 중요하다.

Q. Agent가 임의 색상값을 만들어도 돼?
A. 가능하면 기존 token을 사용하고, 없는 경우 새 token 추가 이유를 명확히 해야 한다.

Q. Frontend Agent가 새 스타일 라이브러리를 추가해도 돼?
A. 명확한 요구나 승인 없이 새 라이브러리를 도입하면 안 된다.

---

## 5.2 Frontend Agent Pre-check

### [개념]

Frontend Agent Pre-check는 스타일 코드 생성 전에 반드시 확인해야 하는 사전 점검이다.

Pre-check 없이 스타일을 생성하면 기존 프로젝트 구조와 충돌할 수 있다.

---

### [핵심]

Pre-check 항목:

```md
## Project

- [ ] Styling Method는 무엇인가?
- [ ] CSS Module을 사용하는가?
- [ ] Tailwind를 사용하는가?
- [ ] CSS-in-JS를 사용하는가?
- [ ] Plain CSS인가?

## File Structure

- [ ] 전역 styles 폴더 위치는 어디인가?
- [ ] component style 위치는 어디인가?
- [ ] page style 위치는 어디인가?

## Token

- [ ] color token이 있는가?
- [ ] spacing token이 있는가?
- [ ] typography token이 있는가?
- [ ] z-index token이 있는가?
- [ ] breakpoint 기준이 있는가?

## Rules

- [ ] naming convention이 있는가?
- [ ] responsive 기준이 있는가?
- [ ] theme / dark mode 기준이 있는가?
- [ ] accessibility 기준이 있는가?
```

---

### [실무]

Pre-check Flow:

```text
스타일 코드 생성 전
→ 프로젝트 구조 확인
→ 기존 CSS import 확인
→ token 파일 확인
→ 컴포넌트 스타일 위치 확인
→ breakpoint 확인
→ 생성 범위 결정
```

Pre-check 실패 시:

```text
기존 기준 없음
→ 최소 기준 제안

token 없음
→ 반복 값에 대한 token 제안

style 위치 불명확
→ styles / components / pages 책임 분리 제안

breakpoint 없음
→ common breakpoint 기준 제안
```

---

### [FAQ]

Q. Frontend Agent가 코드부터 작성하면 안 돼?
A. 기존 스타일 방식, token, 파일 구조를 먼저 확인해야 충돌을 줄일 수 있다.

Q. token이 없으면 어떻게 해?
A. 반복되는 색상과 간격부터 token으로 분리하는 제안을 할 수 있다.

Q. 기존 스타일 기준이 없으면 어떻게 해?
A. 최소한 reset, token, global, component style 책임 분리 기준을 제안하는 것이 좋다.

---

# 6. PM Agent Rules

## 6.1 PM Styling Quality Check

### [개념]

PM Agent는 Styling Architecture를 기준으로 UI 품질과 완료 여부를 판단한다.

PM Agent는 CSS 구현 세부사항 전체보다 사용자 흐름, 요구사항 충족, 화면 일관성, 반응형, 접근성 리스크를 중심으로 판단한다.

---

### [핵심]

PM Agent 확인 항목:

```md
- [ ] 화면이 요구사항과 일치하는가?
- [ ] 주요 UI가 일관된 스타일을 사용하는가?
- [ ] 모바일 화면에서 깨지지 않는가?
- [ ] 버튼 / 입력 / 카드 스타일이 일관적인가?
- [ ] 다크모드가 요구사항이면 적용되었는가?
- [ ] 접근성 문제가 큰가?
- [ ] 사용자가 주요 기능을 완료할 수 있는가?
- [ ] 배포 전 수정이 필요한 스타일 이슈가 있는가?
```

PM 판단 기준:

```text
UI Complete
→ 요구사항 충족 + 주요 화면 일관성 + 반응형 OK + 치명 접근성 문제 없음

UI Partial
→ 기능은 있으나 일부 스타일 불일치 또는 반응형 미흡

UI Blocked
→ 모바일 깨짐, 주요 버튼 식별 불가, 접근성 심각, 사용 흐름 방해
```

---

### [실무]

PM Agent 판단 Flow:

```text
UI Requirement 확인
→ 주요 화면 확인
→ 사용자 흐름 확인
→ 모바일 화면 확인
→ 주요 상태 확인
→ 접근성 치명 문제 확인
→ UI Complete / Partial / Blocked 판단
```

PM Agent 스타일 이슈 예:

```text
저장 버튼이 모바일에서 화면 밖으로 밀림
→ UI Blocked

카드 간격이 일부 화면에서 다름
→ UI Partial

다크모드에서 본문이 안 보임
→ UI Blocked

버튼 hover 색상 일부 누락
→ UI Partial 또는 Minor Issue
```

---

### [FAQ]

Q. PM Agent가 CSS 코드까지 봐야 해?
A. 세부 구현 전체보다는 UI 일관성, 반응형, 사용자 흐름, 완료 여부를 중심으로 판단한다.

Q. 스타일 이슈도 기능 완료를 막을 수 있어?
A. 사용자가 기능을 사용하기 어렵게 만들면 Blocker가 될 수 있다.

Q. PM Agent는 어떤 스타일 문제를 가장 중요하게 봐야 해?
A. 사용자 흐름을 막는 문제, 모바일 깨짐, 주요 버튼 식별 불가, 접근성 치명 문제를 우선 확인해야 한다.

---

# 7. Final Styling Architecture Checklist

## 7.1 Final Quality Checklist

### [개념]

Final Styling Architecture Checklist는 스타일 구조 최종 승인 전에 확인해야 하는 전체 검수 기준이다.

Frontend Agent, Review Agent, PM Agent는 이 체크리스트를 기준으로 스타일 생성, 검토, 완료 판단을 수행한다.

---

### [핵심]

최종 체크리스트:

```md
## Structure

- [ ] 스타일링 방식이 프로젝트 기준과 일치하는가?
- [ ] Global Style과 Component Style이 분리되어 있는가?
- [ ] Reset / Token / Theme / Global / Utility 파일 구조가 있는가?
- [ ] 컴포넌트 전용 스타일이 컴포넌트와 가까운 위치에 있는가?

## Token

- [ ] Color Token이 정의되어 있는가?
- [ ] Spacing Token이 정의되어 있는가?
- [ ] Typography Token이 정의되어 있는가?
- [ ] Radius / Shadow / Z-index Token이 정의되어 있는가?
- [ ] raw value 하드코딩이 과하지 않은가?

## Naming

- [ ] class naming 규칙이 일관적인가?
- [ ] 역할 기반 이름을 사용하는가?
- [ ] 상태 class가 명확한가?
- [ ] 모호한 이름이 없는가?

## Component

- [ ] component style과 layout style이 분리되어 있는가?
- [ ] variant 구조가 명확한가?
- [ ] hover / focus / disabled / error 상태가 있는가?
- [ ] 외부 layout에 과하게 의존하지 않는가?

## Responsive

- [ ] Mobile First 기준인가?
- [ ] breakpoint 기준이 일관적인가?
- [ ] 모바일 가로 스크롤이 없는가?
- [ ] modal / table / card 반응형 처리가 있는가?

## Accessibility

- [ ] focus-visible 스타일이 있는가?
- [ ] color contrast가 충분한가?
- [ ] 색상만으로 상태를 전달하지 않는가?
- [ ] prefers-reduced-motion을 고려했는가?

## Theme

- [ ] semantic token을 사용하는가?
- [ ] dark mode 대응 구조가 있는가?
- [ ] theme 전환 시 raw color 문제가 없는가?
- [ ] theme import order가 token 이후, component style 이전인가?

## Maintainability

- [ ] 중복 스타일이 과하지 않은가?
- [ ] `!important` 남용이 없는가?
- [ ] selector가 과도하게 깊지 않은가?
- [ ] 외부 라이브러리 override가 안전한가?
```

---

### [실무]

최종 승인 기준:

```text
Styling Method 일관성
+ Token 기반 스타일
+ Theme Import Order 일관성
+ Component / Layout 책임 분리
+ Mobile First 반응형
+ Focus / Disabled / Error 접근성 상태
+ Theme 확장 가능성
+ Specificity 안정성
+ Duplication 관리
→ Styling Architecture 승인 가능
```

최종 보류 기준:

```text
global style 오염
또는 token 부재
또는 theme import order 불명확
또는 모바일 깨짐
또는 focus 제거
또는 dark mode contrast 심각
또는 !important 남용
또는 component / layout 책임 혼합
→ 수정 필요
```

---

### [FAQ]

Q. 이 체크리스트를 매번 다 써야 해?
A. 변경 범위에 따라 선택 적용할 수 있다. 다만 token, 반응형, 접근성, 충돌 가능성은 항상 확인하는 것이 좋다.

Q. 최종 승인 기준은 뭐야?
A. 스타일 방식이 일관되고, 반응형과 접근성 문제가 없으며, 유지보수 가능한 구조여야 한다.

Q. 가장 먼저 확인해야 하는 최종 항목은 뭐야?
A. Styling Method 일관성, token 사용, theme import order, component/layout 분리, mobile responsive, focus style이다.

---

# 8. Part07 Quality Checklist

## 8.1 File Structure, Troubleshooting, Agent Rules Checklist

### [개념]

Part07 단계에서는 Styling File Structure, Import Order, Troubleshooting, Review Agent, Frontend Agent, PM Agent의 최종 규칙이 명확한지 검토한다.

이 단계는 Styling Architecture Domain Rules의 운영 기준을 완성하는 단계다.

---

### [핵심]

Part07 체크리스트:

```md
## File Structure

- [ ] global styles folder 책임이 명확한가?
- [ ] component style file 위치가 명확한가?
- [ ] page / layout style 책임이 분리되어 있는가?
- [ ] theme style 위치가 명확한가?

## Import Order

- [ ] reset, token, theme, global, utility 순서가 명확한가?
- [ ] component style import 위치가 명확한가?
- [ ] theme import order 기준이 Part02 / Part05와 일관되는가?

## Troubleshooting

- [ ] CSS Not Applied Flow가 있는가?
- [ ] Style Conflict Flow가 있는가?
- [ ] Responsive Broken Flow가 있는가?
- [ ] Z-index Problem Flow가 있는가?
- [ ] Dark Mode Broken Flow가 있는가?

## Agent Rules

- [ ] Review Agent checklist가 포함되어 있는가?
- [ ] Review Severity Rules가 포함되어 있는가?
- [ ] Frontend Agent generation rules가 포함되어 있는가?
- [ ] Frontend Agent pre-check가 포함되어 있는가?
- [ ] PM Agent quality check가 포함되어 있는가?

## Final

- [ ] Final Styling Architecture Checklist가 있는가?
- [ ] Retrieval Queries가 충분한가?
```

---

### [실무]

Part07 승인 기준:

```text
File Structure 명확
+ Import Order 명확
+ Theme Import Order 일관성 확보
+ Troubleshooting Flow 포함
+ Review Agent / Frontend Agent / PM Agent 규칙 포함
+ Final Checklist 포함
+ FAQ 충분
+ Retrieval Queries 포함
→ Part07 승인 가능
```

Part07 보류 기준:

```text
파일 구조 불명확
또는 import order 누락
또는 theme import order가 Part02 / Part05와 충돌
또는 troubleshooting flow 부족
또는 Agent별 역할 불명확
또는 최종 checklist 부족
또는 Retrieval Queries 부족
→ 재작성 필요
```

---

### [FAQ]

Q. Part07의 핵심 목적은 뭐야?
A. 파일 구조, import 순서, 문제 해결 Flow, Agent별 운영 규칙, 최종 체크리스트를 고정하는 것이다.

Q. Part07에서 가장 위험한 문제는 뭐야?
A. 파일 위치와 import 순서가 불명확하거나 Agent별 검토 기준이 부족한 것이다.

Q. Part07에서 theme import order는 어떻게 정리했어?
A. `reset.css → tokens.css → theme.css → globals.css → typography.css → utilities.css → layout / page / component style` 순서로 통일했다.

Q. Part07이 끝나면 Styling Architecture Domain Rules는 완료야?
A. 기본 Styling Architecture Domain Rules는 완료 가능하다. 이후 Design System Foundation Domain Rules와 연계하는 것이 자연스럽다.

---

# Retrieval Queries

### [FAQ]

Q. Styling File Structure는 뭐야?
A. 스타일 파일을 프로젝트 안에서 어디에 배치할지 정하는 규칙이다.

Q. Styling File Structure는 왜 중요해?
A. 스타일 탐색성, 유지보수성, Agent Retrieval 품질에 직접 영향을 주기 때문이다.

Q. styles 폴더에는 무엇을 넣어야 해?
A. reset, tokens, theme, globals, typography, utilities처럼 전역 기준 스타일을 넣는 것이 좋다.

Q. reset.css는 무엇을 담당해?
A. 브라우저 기본 스타일 초기화를 담당한다.

Q. tokens.css는 무엇을 담당해?
A. color, spacing, typography, radius, shadow, z-index 같은 design token을 담당한다.

Q. theme.css는 무엇을 담당해?
A. light / dark theme token override를 담당한다.

Q. globals.css는 무엇을 담당해?
A. body, root, base element style 같은 앱 전체 기본 스타일을 담당한다.

Q. utilities.css는 무엇을 담당해?
A. sr-only, container, stack, flex-center 같은 작은 재사용 utility style을 담당한다.

Q. Button.css를 styles 폴더에 넣어도 돼?
A. 가능은 하지만 Button 전용 스타일이라면 Button 컴포넌트 폴더에 두는 것이 추적하기 쉽다.

Q. Component Style File은 무엇을 담당해?
A. 특정 컴포넌트의 외형, 내부 배치, variant, state를 담당한다.

Q. Component Style File에 넣으면 안 되는 것은 뭐야?
A. global reset, app-wide token, page container, external layout margin, 다른 컴포넌트 override는 넣지 않는 것이 좋다.

Q. Component Style File에 margin-bottom을 넣어도 돼?
A. 재사용 컴포넌트라면 외부 배치 margin은 부모 layout에서 관리하는 것이 좋다.

Q. Page Style은 무엇을 담당해?
A. 특정 화면의 container, section spacing, page-level grid, responsive layout을 담당한다.

Q. Layout Style은 무엇을 담당해?
A. AppLayout, HeaderLayout, SidebarLayout, PageContainer, Stack, Grid 같은 반복 배치 구조를 담당한다.

Q. Page Style과 Component Style은 왜 나눠야 해?
A. page는 layout, component는 개별 UI 외형과 상태를 담당해야 재사용성이 높아진다.

Q. CSS import 순서가 중요해?
A. 중요하다. 같은 우선순위의 selector는 나중에 import된 스타일이 덮어쓸 수 있다.

Q. 권장 CSS import 순서는 뭐야?
A. Reset → Token → Theme → Global → Typography → Utility → Layout → Page → Component 순서가 좋다.

Q. token 파일은 언제 import해야 해?
A. CSS variable을 사용하는 스타일보다 먼저 import되어야 한다.

Q. theme.css는 언제 import해야 해?
A. base token 이후, global style과 component style보다 먼저 import하는 것을 권장한다.

Q. reset을 나중에 import하면 어떻게 돼?
A. component style이 reset에 의해 덮이거나 예상치 못하게 깨질 수 있다.

Q. Component CSS Module은 어디서 import해?
A. 해당 컴포넌트 파일에서 import하는 것이 일반적이다.

Q. theme.css는 tokens.css보다 먼저 import해도 돼?
A. 권장하지 않는다. theme은 token을 override하거나 확장하므로 base token 이후 import하는 것이 좋다.

Q. theme.css는 globals.css 앞에 와야 해 뒤에 와야 해?
A. 이 문서에서는 Part02 / Part05와의 일관성을 위해 `tokens.css → theme.css → globals.css` 순서를 권장한다.

Q. component에서 raw color를 쓰면 theme이 적용돼?
A. 적용되지 않을 수 있다. semantic token을 사용해야 theme 전환이 안정적이다.

Q. CSS가 안 먹을 때 제일 먼저 뭘 확인해?
A. 브라우저 개발자 도구에서 해당 요소에 class가 실제로 붙었는지 확인한다.

Q. CSS Module 스타일이 안 먹어?
A. `styles.className`으로 접근했는지, 파일명이 `module.css`인지, import가 맞는지 확인한다.

Q. CSS가 안 먹으면 !important를 쓰면 돼?
A. 최후 수단으로만 사용해야 한다. 먼저 import, className, specificity를 확인해야 한다.

Q. className은 붙었는데 스타일이 안 보여?
A. computed style에서 다른 CSS rule이 덮어쓰는지 확인해야 한다.

Q. Style Conflict는 뭐야?
A. 여러 CSS 규칙이 같은 요소에 적용되어 의도와 다른 스타일이 나타나는 문제다.

Q. 스타일이 자꾸 다른 곳에도 적용돼?
A. 전역 class 충돌 가능성이 높다. CSS Module이나 naming convention을 고려한다.

Q. import 순서 때문에 스타일이 바뀔 수 있어?
A. 그렇다. 같은 우선순위라면 나중에 import된 스타일이 적용될 수 있다.

Q. Style Conflict는 어떻게 찾는 게 좋아?
A. DevTools의 Computed 탭에서 어떤 CSS rule이 실제 적용되는지 확인한다.

Q. Responsive Broken은 뭐야?
A. 화면 크기 변화에 따라 layout이 깨지는 문제다.

Q. 모바일에서 가로 스크롤이 생겨?
A. 고정 width, 큰 이미지, 긴 텍스트, flex item min-width, table overflow 문제가 원인일 수 있다.

Q. flex item이 줄어들지 않아?
A. `min-width: 0`이 필요할 수 있다.

Q. modal이 모바일 화면을 넘으면 어떻게 해?
A. `width: min(100% - 여백, max-width)`와 `max-height`, `overflow-y: auto`를 적용한다.

Q. table이 모바일에서 화면을 밀어내면 어떻게 해?
A. table wrapper에 `overflow-x: auto`를 적용한다.

Q. Z-index Problem은 뭐야?
A. modal, dropdown, tooltip, toast 등이 예상한 순서로 겹쳐 보이지 않는 문제다.

Q. z-index를 9999로 줬는데도 안 돼?
A. 부모 stacking context나 overflow hidden 때문에 가려질 수 있다.

Q. dropdown이 card 뒤에 숨어?
A. 부모 요소의 overflow, stacking context, z-index를 확인해야 한다.

Q. modal은 z-index만 높이면 돼?
A. 아니다. overlay, stacking context, portal, focus management까지 함께 고려해야 한다.

Q. Dark Mode Broken은 뭐야?
A. dark theme 전환 시 텍스트, 배경, border, icon, focus, disabled 상태가 식별되지 않는 문제다.

Q. Dark Mode에서 글자가 안 보여?
A. raw color 하드코딩이나 contrast 부족 가능성이 높다. semantic token을 사용해야 한다.

Q. Dark Mode에서 border가 안 보여?
A. dark theme용 border token을 따로 정의해야 한다.

Q. Dark Mode에서 shadow가 잘 안 보여?
A. 어두운 배경에서는 shadow만으로 elevation이 부족할 수 있어 surface와 border를 함께 조정해야 한다.

Q. Review Agent는 스타일 코드에서 가장 먼저 봐야 할 것은?
A. 스타일 방식의 일관성, 전역 충돌 가능성, token 사용 여부, 반응형과 접근성 스타일이다.

Q. 스타일이 화면상 예쁘면 승인해도 돼?
A. 아니다. 유지보수성, 반응형, 접근성, 중복, 충돌 가능성까지 검토해야 한다.

Q. Review Agent가 desktop 화면만 보면 돼?
A. 아니다. mobile, tablet, desktop과 theme 상태까지 확인해야 한다.

Q. Review Severity Rules는 뭐야?
A. 스타일 문제의 심각도를 Blocker, Major, Minor로 구분하는 기준이다.

Q. Styling Review에서 Blocker는 뭐야?
A. 모바일 주요 기능 사용 불가, focus 제거, dark mode 텍스트 식별 불가, layout collapse처럼 사용자 흐름을 막는 문제다.

Q. Styling Review에서 Major는 뭐야?
A. 일부 responsive 깨짐, token 미사용 반복, variant/state 혼동, !important 반복 같은 큰 유지보수 문제다.

Q. Styling Review에서 Minor는 뭐야?
A. 일부 spacing 불일치, class naming 개선, transition 조정, 일부 중복 스타일 같은 낮은 심각도 문제다.

Q. Frontend Agent가 스타일을 만들 때 가장 조심할 점은?
A. 프로젝트 기존 스타일 방식과 token 체계를 따르는 것이 가장 중요하다.

Q. Frontend Agent가 임의 색상값을 만들어도 돼?
A. 가능하면 기존 token을 사용하고, 없는 경우 새 token 추가 이유를 명확히 해야 한다.

Q. Frontend Agent가 새 스타일 라이브러리를 추가해도 돼?
A. 명확한 요구나 승인 없이 새 라이브러리를 도입하면 안 된다.

Q. Frontend Agent Pre-check는 뭐야?
A. 스타일 코드 생성 전에 기존 styling method, file structure, token, naming, responsive, theme, accessibility 기준을 확인하는 절차다.

Q. token이 없으면 어떻게 해?
A. 반복되는 색상과 간격부터 token으로 분리하는 제안을 할 수 있다.

Q. 기존 스타일 기준이 없으면 어떻게 해?
A. 최소한 reset, token, global, component style 책임 분리 기준을 제안하는 것이 좋다.

Q. PM Agent는 스타일 품질을 어떻게 판단해?
A. 요구사항 충족, UI 일관성, 모바일 대응, 사용자 흐름, 접근성 문제가 있는지 중심으로 판단한다.

Q. PM Agent가 CSS 코드까지 봐야 해?
A. 세부 구현 전체보다는 UI 일관성, 반응형, 사용자 흐름, 완료 여부를 중심으로 판단한다.

Q. 스타일 이슈도 기능 완료를 막을 수 있어?
A. 사용자가 기능을 사용하기 어렵게 만들면 Blocker가 될 수 있다.

Q. UI Complete 기준은 뭐야?
A. 요구사항 충족, 주요 화면 일관성, 반응형 OK, 치명 접근성 문제가 없는 상태다.

Q. UI Partial 기준은 뭐야?
A. 기능은 있으나 일부 스타일 불일치 또는 반응형 미흡이 있는 상태다.

Q. UI Blocked 기준은 뭐야?
A. 모바일 깨짐, 주요 버튼 식별 불가, 접근성 심각, 사용 흐름 방해가 있는 상태다.

Q. Final Styling Architecture Checklist는 왜 필요해?
A. 스타일 구조 최종 승인 전에 구조, token, naming, component, responsive, accessibility, theme, maintainability를 검토하기 위해 필요하다.

Q. Styling Architecture 최종 승인 기준은 뭐야?
A. 스타일 방식이 일관되고, 반응형과 접근성 문제가 없으며, 유지보수 가능한 구조여야 한다.

Q. Part07의 핵심 목적은 뭐야?
A. 파일 구조, import 순서, 문제 해결 Flow, Agent별 운영 규칙, 최종 체크리스트를 고정하는 것이다.

Q. Part07에서 가장 위험한 문제는 뭐야?
A. 파일 위치와 import 순서가 불명확하거나 Agent별 검토 기준이 부족한 것이다.

Q. Part07에서 theme import order는 어떻게 정리했어?
A. `reset.css → tokens.css → theme.css → globals.css → typography.css → utilities.css → layout / page / component style` 순서로 통일했다.

Q. Part07이 끝나면 Styling Architecture Domain Rules는 완료야?
A. 기본 Styling Architecture Domain Rules는 완료 가능하다. 이후 Design System Foundation Domain Rules와 연계하는 것이 자연스럽다.
