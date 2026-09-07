# Styling Architecture Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

Styling Architecture Domain Rules 문서는 Frontend Agent / Review Agent / PM Agent가 프론트엔드 프로젝트의 스타일 구조, CSS 관리 방식, 스타일 도구 선택, 컴포넌트 스타일링 기준, 전역 스타일, 디자인 토큰, 반응형 스타일, 테마, 유지보수성을 판단하기 위한 RAG Retrieval 최적화 문서이다.

이 문서는 사람 공부용 CSS 문서가 아니라 Agent가 실제 프론트엔드 프로젝트에서 스타일 구조를 설계하고 리뷰하기 위한 기준 문서이다.

목적:

- CSS 구조 설계 기준 제공
- Plain CSS / CSS Module / CSS-in-JS / Tailwind CSS 판단
- Global Style과 Component Style 분리
- Design Token 기반 스타일 관리
- Class Naming 규칙 검토
- CSS 충돌과 우선순위 문제 예방
- Responsive Styling 기준 제공
- Theme / Dark Mode 구조 판단
- Style Duplication 검토
- Frontend Agent의 스타일 코드 생성 기준 제공
- Review Agent의 스타일 구조 검토 기준 제공
- PM Agent의 UI 품질 완료 판단 지원

---

### [핵심]

Styling Architecture의 핵심 기준:

1. 스타일 책임이 분리되어 있는가?
2. 전역 스타일과 컴포넌트 스타일이 구분되는가?
3. 색상, 간격, 폰트, radius가 토큰화되어 있는가?
4. CSS 충돌 가능성이 낮은가?
5. 스타일 도구 사용 규칙이 일관적인가?
6. 반응형 기준이 통일되어 있는가?
7. hover / active / disabled / focus 상태가 관리되는가?
8. 재사용 가능한 UI 스타일이 중복 작성되지 않는가?
9. 접근성 스타일을 해치지 않는가?
10. 확장 가능한 구조인가?

---

### [실무]

Frontend Agent는 스타일을 작성할 때 단순히 “화면이 예쁘게 보이는가”만 판단하면 안 된다.

실무 판단 Flow:

```text
UI Requirement
→ Design Token 확인
→ Styling Method 확인
→ Global / Component Style 분리
→ Responsive Rule 적용
→ Interaction State 적용
→ Accessibility Style 확인
→ Duplication 확인
→ Review Agent 검토
```

---

### [FAQ]

Q. Styling Architecture 문서는 CSS 공부용이야?

A.
아니다. Frontend Agent / Review Agent / PM Agent가 스타일 구조를 설계하고 검토하기 위한 RAG 문서다.

Q. Styling Architecture에서 가장 중요한 것은 뭐야?

A.
스타일이 일관되고, 충돌이 적고, 재사용 가능하며, 유지보수 가능한 구조인지가 중요하다.

Q. 스타일은 그냥 CSS 파일 하나에 작성하면 안 돼?

A.
작은 프로젝트에서는 가능하지만 규모가 커지면 충돌, 중복, 유지보수 문제가 커질 수 있다.

Q. 스타일 도구는 하나만 정답이 있어?

A.
없다. 프로젝트 규모, 팀 숙련도, 디자인 시스템 필요성, 빌드 환경에 따라 선택해야 한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Styling Architecture 문서는 프론트엔드 스타일 구조 설계에 필요한 실무 범위를 포함한다.

포함 범위:

- CSS Architecture
- Global Style
- Reset CSS
- Normalize CSS
- Component Style
- CSS Module
- CSS-in-JS
- Styled Components
- Emotion
- Tailwind CSS
- Utility First CSS
- Plain CSS
- SCSS / Sass
- Class Naming
- BEM
- Design Token
- CSS Variable
- Theme
- Dark Mode
- Responsive Styling
- Breakpoint
- Layout Token
- Spacing Scale
- Color Token
- Typography Token
- Z-index Scale
- Shadow / Radius Token
- State Style
- Focus Style
- Style Duplication
- Style Review Checklist
- Styling Troubleshooting

---

### [핵심]

반드시 포함:

- Global Style과 Component Style 분리
- CSS Reset 기준
- Design Token 사용 기준
- CSS Variable 사용 기준
- Styling Method 비교
- Naming Convention 기준
- Responsive Styling 기준
- Accessibility Style 기준
- Theme 구조 기준
- Code Review 기준
- Troubleshooting 기준

---

### [실무]

Styling Architecture는 다음 Domain Rules와 연결된다.

```text
HTML CSS Foundation
→ React Component Design
→ UI Component Pattern
→ Frontend Accessibility
→ Frontend Code Review
→ Styling Architecture
→ Design System
```

---

### [FAQ]

Q. Styling Architecture와 Design System은 뭐가 달라?

A.
Styling Architecture는 스타일 코드 구조와 관리 방식이고, Design System은 UI 규격, 컴포넌트 규칙, 디자인 토큰 체계까지 포함하는 더 큰 시스템이다.

Q. CSS 기초도 여기서 다뤄?

A.
기초 문법은 HTML CSS Foundation 문서에서 다루고, 여기서는 구조와 관리 기준을 중심으로 다룬다.

Q. Tailwind도 이 문서 범위야?

A.
Tailwind 사용 구조와 리뷰 기준은 포함한다. Tailwind 자체 문법 전체 설명은 별도 문서로 분리할 수 있다.

---

## 2.2 Excluded Scope

### [개념]

Styling Architecture 문서는 스타일 구조와 유지보수 기준에 집중한다.

제외 범위:

- HTML/CSS 기초 문법 전체 설명
- CSS Selector 기초 전체 설명
- React Core 문법
- Advanced Animation Library
- Framer Motion 심화
- Canvas / WebGL
- Design System 전체 컴포넌트 명세
- Figma 운영 규칙 심화
- Frontend Performance Profiling 심화
- Browser Rendering Engine 심화
- Next.js Styling 전략 심화
- Native App Styling

---

### [핵심]

제외 이유:

- Level 3 Frontend Foundation 범위 유지
- HTML/CSS Foundation 문서와 중복 방지
- Design System 문서와 책임 분리
- Retrieval 혼선 방지
- Chunk 품질 유지

---

### [실무]

다른 문서로 위임하는 경우:

```text
CSS 기본 문법
→ HTML CSS Foundation

컴포넌트 설계
→ React Component Design

UI 패턴
→ UI Component Pattern

접근성 세부 기준
→ Frontend Accessibility

디자인 토큰과 컴포넌트 규격 심화
→ Design System
```

---

### [FAQ]

Q. 이 문서에서 CSS Grid와 Flexbox를 자세히 설명해?

A.
자세한 문법은 HTML CSS Foundation에서 다루고, 여기서는 레이아웃 스타일 구조와 재사용 기준을 다룬다.

Q. 애니메이션도 포함해?

A.
기본 transition과 상태 스타일 관점은 포함하지만 Framer Motion 같은 심화 애니메이션은 제외한다.

---

# 3. Styling Architecture Core

## 3.1 Styling Architecture Definition

### [개념]

Styling Architecture는 프로젝트에서 스타일을 어디에, 어떤 기준으로, 어떤 도구를 사용해, 어떻게 재사용하고 확장할지 정하는 구조다.

---

### [핵심]

Styling Architecture가 필요한 이유:

- CSS 충돌 방지
- 중복 스타일 감소
- 디자인 일관성 유지
- 컴포넌트 재사용성 증가
- 반응형 관리 단순화
- 테마 확장 가능
- 코드 리뷰 기준 통일
- 신규 개발자 또는 Agent의 스타일 생성 안정성 향상

---

### [실무]

좋은 Styling Architecture는 다음 질문에 답할 수 있어야 한다.

```md
- [ ] 전역 스타일은 어디에 작성하는가?
- [ ] 컴포넌트 스타일은 어디에 작성하는가?
- [ ] 색상과 간격은 어디에서 관리하는가?
- [ ] 반응형 breakpoint는 어디에서 관리하는가?
- [ ] class naming 규칙은 무엇인가?
- [ ] 공통 UI 스타일은 어떻게 재사용하는가?
- [ ] dark mode는 어떻게 처리하는가?
- [ ] style override는 어디까지 허용하는가?
```

---

### [FAQ]

Q. Styling Architecture가 없으면 뭐가 문제야?

A.
스타일 중복, CSS 충돌, 색상 불일치, 반응형 깨짐, 유지보수 어려움이 생길 수 있다.

Q. 작은 프로젝트도 Styling Architecture가 필요해?

A.
간단한 기준은 필요하다. 다만 구조를 과하게 복잡하게 만들 필요는 없다.

---

## 3.2 Styling Responsibility

### [개념]

Styling Responsibility는 스타일 책임을 전역, 레이아웃, 컴포넌트, 유틸리티, 토큰 단위로 나누는 기준이다.

---

### [핵심]

권장 책임 분리:

```text
Reset / Base Style
→ Global Style

Color / Spacing / Font / Radius
→ Design Token

Page Layout
→ Layout Style

Reusable UI
→ Component Style

One-off Adjustment
→ Utility or Local Style
```

---

### [실무]

권장 구조 예:

```text
src/
├─ styles/
│  ├─ reset.css
│  ├─ globals.css
│  ├─ tokens.css
│  ├─ typography.css
│  └─ utilities.css
├─ components/
│  └─ Button/
│     ├─ Button.jsx
│     └─ Button.module.css
└─ pages/
   └─ MainPage/
      ├─ MainPage.jsx
      └─ MainPage.module.css
```

---

### [FAQ]

Q. reset, global, token 파일을 꼭 나눠야 해?

A.
프로젝트 규모에 따라 다르다. 다만 역할을 구분하면 유지보수와 리뷰가 쉬워진다.

Q. 페이지 스타일과 컴포넌트 스타일은 나눠야 해?

A.
권장된다. 페이지 레이아웃과 재사용 컴포넌트 스타일을 섞으면 재사용성이 떨어진다.

---

# 4. Global Style Rules

## 4.1 Global Style

### [개념]

Global Style은 애플리케이션 전체에 적용되는 기본 스타일이다.

포함 예:

- reset
- body margin
- root font
- base background
- base text color
- link 기본 스타일
- image 기본 스타일
- box-sizing
- CSS variables
- typography base

---

### [핵심]

Global Style에 넣기 적합한 것:

```text
box-sizing
body margin reset
font-family
background color
text color
root CSS variables
a 기본 스타일
img max-width
button font inherit
```

Global Style에 넣기 부적합한 것:

```text
특정 Card 디자인
특정 Modal 디자인
특정 Page layout
특정 Button variant
특정 Form field spacing
```

---

### [예제]

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: system-ui, sans-serif;
  color: var(--color-text);
  background: var(--color-background);
}

img {
  max-width: 100%;
  display: block;
}

button,
input,
textarea,
select {
  font: inherit;
}
```

---

### [실무]

Global Style 리뷰 기준:

```md
- [ ] 전역 스타일이 너무 많은 책임을 갖지 않는가?
- [ ] 특정 컴포넌트 스타일이 global에 들어가지 않았는가?
- [ ] reset이 접근성 스타일을 제거하지 않는가?
- [ ] CSS variable이 root에 정의되어 있는가?
- [ ] body 기본 색상과 폰트가 설정되어 있는가?
```

---

### [FAQ]

Q. 모든 스타일을 globals.css에 넣어도 돼?

A.
권장하지 않는다. global에는 전체 기본 스타일만 두고 컴포넌트 스타일은 분리하는 것이 좋다.

Q. body에 font-family를 넣는 건 괜찮아?

A.
괜찮다. 전체 앱의 기본 폰트는 global style에서 관리하는 것이 일반적이다.

Q. button 기본 스타일을 global에서 모두 제거해도 돼?

A.
가능하지만 focus style과 접근성 상태를 함께 고려해야 한다.

---

## 4.2 Reset CSS Rules

### [개념]

Reset CSS는 브라우저 기본 스타일 차이를 줄이고 프로젝트 스타일 기준을 통일하기 위한 초기화 스타일이다.

---

### [핵심]

Reset CSS 목적:

- 브라우저 기본 margin 제거
- box-sizing 통일
- font inheritance 정리
- image layout 문제 감소
- form element 기본 차이 완화

---

### [예제]

기본 reset 예:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body,
h1,
h2,
h3,
h4,
p,
figure,
blockquote,
dl,
dd {
  margin: 0;
}

ul,
ol {
  padding: 0;
}

img,
picture {
  max-width: 100%;
  display: block;
}
```

---

### [주의]

Reset CSS에서 주의할 점:

- focus outline을 무조건 제거하지 않음
- list style 제거 시 semantic list 사용성 고려
- button cursor, disabled 상태 고려
- form 요소 접근성 고려
- 너무 공격적인 reset은 유지보수 비용 증가

---

### [FAQ]

Q. reset css는 꼭 필요해?

A.
프로젝트 스타일 일관성을 위해 많이 사용한다. 다만 접근성에 필요한 기본 스타일을 제거하지 않도록 주의해야 한다.

Q. outline: none을 reset에 넣어도 돼?

A.
권장하지 않는다. 제거한다면 반드시 대체 focus style을 제공해야 한다.

---

## 4.3 Normalize vs Reset

### [Comparison]

| 구분        | Reset CSS               | Normalize CSS                |
| ----------- | ----------------------- | ---------------------------- |
| 목적        | 기본 스타일 제거        | 브라우저 차이 보정           |
| 스타일 방향 | 초기화 중심             | 기본값 유지 중심             |
| 장점        | 프로젝트 기준 통일 쉬움 | 기본 접근성 스타일 유지 쉬움 |
| 단점        | 과하면 기본 사용성 손상 | 완전한 초기화는 아님         |
| 적합        | 디자인 통제 강한 앱     | 기본 HTML 스타일 활용 앱     |

---

### [실무]

선택 기준:

```text
디자인 시안이 명확하고 UI 통제가 필요
→ Reset CSS

브라우저 기본 스타일을 어느 정도 유지
→ Normalize CSS

소규모 React 앱
→ 간단한 Reset + CSS Variable 조합
```

---

### [FAQ]

Q. Reset과 Normalize 중 뭐가 좋아?

A.
정답은 없다. 프로젝트 스타일 통제 수준과 접근성 기준에 따라 선택한다.

Q. 둘 다 써도 돼?

A.
가능은 하지만 중복 초기화가 생길 수 있어 주의해야 한다.

---

# 5. Design Token Rules

## 5.1 Design Token

### [개념]

Design Token은 색상, 간격, 폰트, radius, shadow, z-index 같은 디자인 값을 이름으로 관리하는 방식이다.

---

### [핵심]

Token으로 관리할 대상:

- Color
- Spacing
- Font Size
- Font Weight
- Line Height
- Border Radius
- Shadow
- Z-index
- Breakpoint
- Transition
- Layout Width

---

### [예제]

```css
:root {
  --color-primary: #2563eb;
  --color-primary-hover: #1d4ed8;
  --color-text: #111827;
  --color-muted: #6b7280;
  --color-border: #e5e7eb;
  --color-background: #ffffff;

  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;

  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;

  --z-header: 100;
  --z-modal: 1000;
  --z-toast: 1100;
}
```

---

### [실무]

Design Token 사용 예:

```css
.card {
  padding: var(--spacing-md);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background: var(--color-background);
}
```

장점:

- 스타일 일관성 유지
- 수정 범위 감소
- theme 확장 쉬움
- Agent 코드 생성 기준 명확
- Review Agent 검토 쉬움

---

### [FAQ]

Q. Design Token은 Design System에서만 쓰는 거야?

A.
아니다. 작은 프로젝트에서도 색상과 간격을 token으로 관리하면 유지보수에 좋다.

Q. 모든 값을 token으로 만들어야 해?

A.
아니다. 반복 사용되거나 의미가 있는 값부터 token으로 관리한다.

Q. 색상 코드를 직접 쓰면 안 돼?

A.
한두 번은 가능하지만 반복되는 색상은 token으로 분리하는 것이 좋다.

---

## 5.2 Color Token Rules

### [개념]

Color Token은 UI 색상을 의미 단위로 관리하는 방식이다.

---

### [핵심]

권장 token 유형:

```text
Brand Color
→ --color-primary

Text Color
→ --color-text
→ --color-muted

Background Color
→ --color-background
→ --color-surface

Border Color
→ --color-border

Semantic Color
→ --color-success
→ --color-warning
→ --color-error
→ --color-info
```

---

### [예제]

```css
:root {
  --color-primary: #2563eb;
  --color-primary-hover: #1d4ed8;

  --color-success: #16a34a;
  --color-warning: #f59e0b;
  --color-error: #dc2626;
  --color-info: #0284c7;

  --color-text: #111827;
  --color-muted: #6b7280;
  --color-background: #ffffff;
  --color-surface: #f9fafb;
  --color-border: #e5e7eb;
}
```

---

### [실무]

나쁜 예:

```css
.error-message {
  color: red;
}
```

좋은 예:

```css
.error-message {
  color: var(--color-error);
}
```

---

### [주의]

색상 관리 주의:

- 색상만으로 상태 전달 금지
- contrast 부족 주의
- hover / disabled 색상 누락 주의
- brand color와 semantic color 구분
- dark mode 고려 시 token alias 구조 필요

---

### [FAQ]

Q. primary와 success는 뭐가 달라?

A.
primary는 브랜드나 주요 행동 색상이고, success는 성공 상태를 나타내는 의미 색상이다.

Q. 에러 색상을 red로 쓰면 안 돼?

A.
가능하지만 token으로 관리하는 것이 일관성과 테마 확장에 좋다.

---

## 5.3 Spacing Token Rules

### [개념]

Spacing Token은 margin, padding, gap 같은 간격 값을 일정한 scale로 관리하는 방식이다.

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
}
```

---

### [실무]

사용 예:

```css
.form {
  display: grid;
  gap: var(--spacing-4);
}

.card {
  padding: var(--spacing-6);
}
```

Review 기준:

```md
- [ ] 간격 값이 무작위로 증가하지 않는가?
- [ ] margin / padding / gap 사용 기준이 일관적인가?
- [ ] 컴포넌트 내부 간격과 외부 간격이 구분되는가?
- [ ] layout gap에 margin 남용이 없는가?
```

---

### [FAQ]

Q. spacing token은 왜 필요해?

A.
간격이 화면마다 제각각이 되는 것을 막고 UI 리듬을 일관되게 유지하기 위해 필요하다.

Q. 13px, 17px 같은 값을 쓰면 안 돼?

A.
특별한 이유가 없다면 spacing scale 안에서 선택하는 것이 좋다.

---

## 5.4 Typography Token Rules

### [개념]

Typography Token은 font size, line height, font weight, letter spacing 같은 글자 스타일을 체계화하는 방식이다.

---

### [핵심]

권장 token:

```css
:root {
  --font-family-base: system-ui, sans-serif;

  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-md: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --font-size-3xl: 2rem;

  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;

  --line-height-tight: 1.25;
  --line-height-base: 1.5;
  --line-height-relaxed: 1.7;
}
```

---

### [실무]

사용 예:

```css
.page-title {
  font-size: var(--font-size-3xl);
  font-weight: var(--font-weight-bold);
  line-height: var(--line-height-tight);
}

.body-text {
  font-size: var(--font-size-md);
  line-height: var(--line-height-base);
}
```

---

### [FAQ]

Q. font-size를 매번 직접 써도 돼?

A.
가능하지만 typography token을 사용하면 화면 계층과 일관성을 유지하기 쉽다.

Q. line-height도 token으로 관리해야 해?

A.
권장된다. 가독성과 UI 밀도 관리에 중요하다.

---

## 5.5 Z-index Token Rules

### [개념]

Z-index Token은 modal, header, dropdown, toast 같은 겹침 UI의 stacking order를 체계적으로 관리하는 방식이다.

---

### [핵심]

권장 scale:

```css
:root {
  --z-base: 0;
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-header: 300;
  --z-overlay: 900;
  --z-modal: 1000;
  --z-toast: 1100;
}
```

---

### [실무]

나쁜 예:

```css
.modal {
  z-index: 999999;
}
```

좋은 예:

```css
.modal {
  z-index: var(--z-modal);
}
```

---

### [주의]

z-index 문제 원인:

- stacking context
- position 미설정
- 부모 z-index
- transform / opacity / filter
- overflow hidden
- portal 미사용

---

### [FAQ]

Q. z-index는 크게 주면 해결돼?

A.
아니다. stacking context 때문에 큰 숫자를 줘도 해결되지 않을 수 있다.

Q. modal z-index는 어떻게 관리해?

A.
프로젝트 z-index token scale을 정하고 modal, toast, dropdown 우선순위를 명확히 관리한다.

---

# 6. Styling Method Rules

## 6.1 Plain CSS Rules

### [개념]

Plain CSS는 별도 스타일링 라이브러리 없이 일반 CSS 파일을 작성하는 방식이다.

---

### [핵심]

장점:

- 단순함
- 러닝 커브 낮음
- 브라우저 기본 기술
- 빌드 도구 의존도 낮음

단점:

- 전역 충돌 가능
- naming 관리 필요
- 큰 프로젝트에서 유지보수 어려움
- unused CSS 관리 어려움

---

### [실무]

Plain CSS 적합 상황:

```text
소규모 프로젝트
학원 프로젝트
빠른 프로토타입
CSS 기초 학습 목적
스타일 구조가 단순한 앱
```

권장 구조:

```text
src/
├─ styles/
│  ├─ reset.css
│  ├─ tokens.css
│  └─ globals.css
└─ components/
   └─ Button.css
```

---

### [FAQ]

Q. Plain CSS는 실무에서 안 써?

A.
쓴다. 다만 규모가 커질수록 naming과 scope 관리 규칙이 중요해진다.

Q. Plain CSS에서 가장 조심할 점은?

A.
전역 class 충돌과 selector 우선순위 복잡도다.

---

## 6.2 CSS Module Rules

### [개념]

CSS Module은 CSS class를 파일 단위로 scope 처리해 class 충돌을 줄이는 방식이다.

---

### [핵심]

특징:

- 파일 단위 scope
- class 이름 충돌 방지
- React 컴포넌트와 결합 쉬움
- build 시 고유 class name 생성
- 전역 스타일과 구분 가능

---

### [예제]

파일 구조:

```text
Button.jsx
Button.module.css
```

CSS:

```css
.button {
  padding: var(--spacing-2) var(--spacing-4);
  border-radius: var(--radius-md);
}
```

JSX:

```jsx
import styles from "./Button.module.css";

function Button({ children }) {
  return <button className={styles.button}>{children}</button>;
}
```

---

### [실무]

CSS Module 적합 상황:

```text
React 컴포넌트 단위 스타일
중소규모 프로젝트
전역 충돌 방지 필요
CSS-in-JS 없이 scope 필요
```

Review 기준:

```md
- [ ] 파일명이 `*.module.css`인가?
- [ ] 컴포넌트와 같은 위치에 있는가?
- [ ] global style과 component style이 분리되어 있는가?
- [ ] className 조합이 과도하게 복잡하지 않은가?
```

---

### [FAQ]

Q. CSS Module을 쓰면 class 이름 충돌이 없어져?

A.
대부분 줄어든다. build 시 고유 class name으로 변환되기 때문이다.

Q. CSS Module에서도 global style을 만들 수 있어?

A.
가능하지만 남용하지 않는 것이 좋다. 전역 스타일은 별도 global 파일에서 관리하는 것이 명확하다.

---

## 6.3 CSS-in-JS Rules

### [개념]

CSS-in-JS는 JavaScript 또는 TypeScript 파일 안에서 스타일을 작성하는 방식이다.

대표 도구:

- Styled Components
- Emotion

---

### [핵심]

장점:

- 컴포넌트와 스타일 결합
- props 기반 동적 스타일 작성 쉬움
- theme provider 사용 가능
- class naming 고민 감소
- 조건부 스타일 처리 쉬움

단점:

- 런타임 비용 가능
- 번들 크기 증가 가능
- 스타일과 로직 과결합 위험
- SSR 설정 고려 필요
- 디버깅 방식이 달라질 수 있음

---

### [예제]

```jsx
import styled from "styled-components";

const Button = styled.button`
  padding: 8px 16px;
  border-radius: 8px;
  background: ${({ $variant }) =>
    $variant === "primary" ? "var(--color-primary)" : "transparent"};
`;

function PrimaryButton() {
  return <Button $variant="primary">저장</Button>;
}
```

---

### [실무]

CSS-in-JS 적합 상황:

```text
컴포넌트 중심 개발
theme provider 필요
동적 스타일 많음
디자인 시스템 컴포넌트 구현
상태 기반 스타일 많음
```

주의:

```text
props가 너무 많아 스타일 분기가 복잡해지면 variant 체계 분리 필요
```

---

### [FAQ]

Q. CSS-in-JS는 무조건 좋은 방식이야?

A.
아니다. 동적 스타일과 테마에는 강하지만 런타임 비용과 복잡도도 고려해야 한다.

Q. Styled Components에서 props 이름 앞에 `$`를 붙이는 이유는?

A.
DOM으로 전달되지 않는 transient props로 구분하기 위해 사용한다.

---

## 6.4 Tailwind CSS Rules

### [개념]

Tailwind CSS는 utility class를 조합해 스타일을 작성하는 Utility First CSS 프레임워크다.

---

### [핵심]

장점:

- 빠른 UI 작성
- design scale 강제
- CSS 파일 작성량 감소
- 반응형 class 사용 쉬움
- 상태 class 관리 쉬움
- unused CSS 최적화 가능

단점:

- className이 길어질 수 있음
- 재사용 패턴 추출 기준 필요
- 디자인 토큰 설정 필요
- class 중복 증가 가능
- 조건부 class 관리 복잡 가능

---

### [예제]

```jsx
function Card({ title, description }) {
  return (
    <article className="rounded-lg border p-4 shadow-sm">
      <h2 className="text-lg font-bold">{title}</h2>
      <p className="mt-2 text-sm text-gray-600">{description}</p>
    </article>
  );
}
```

---

### [실무]

Tailwind 적합 상황:

```text
빠른 UI 개발
디자인 scale 강제
컴포넌트 기반 React 프로젝트
작은 팀
스타일 파일 분산을 줄이고 싶을 때
```

Review 기준:

```md
- [ ] className이 과도하게 길지 않은가?
- [ ] 반복되는 조합은 컴포넌트로 추출했는가?
- [ ] tailwind.config에 theme token이 정의되어 있는가?
- [ ] arbitrary value 남용이 없는가?
- [ ] responsive / hover / focus 상태가 일관적인가?
```

---

### [FAQ]

Q. Tailwind를 쓰면 CSS Architecture가 필요 없어?

A.
아니다. Tailwind도 token, component extraction, class 관리 기준이 필요하다.

Q. Tailwind className이 너무 길면 어떻게 해?

A.
반복되는 UI는 컴포넌트로 추출하거나 class 조합 유틸을 사용할 수 있다.

Q. arbitrary value를 써도 돼?

A.
필요할 때는 가능하지만 남용하면 design scale이 깨진다.

---

## 6.5 SCSS Sass Rules

### [개념]

SCSS / Sass는 CSS에 변수, nesting, mixin, function 같은 기능을 추가한 CSS 전처리기다.

---

### [핵심]

장점:

- nesting 가능
- 변수 사용 가능
- mixin 재사용 가능
- partial 파일 분리 가능
- CSS 구조화에 유리

단점:

- CSS variable과 역할 중복 가능
- nesting 남용 시 selector 복잡
- build 설정 필요
- 전역 충돌은 여전히 관리 필요

---

### [예제]

```scss
.card {
  padding: var(--spacing-4);
  border: 1px solid var(--color-border);

  &__title {
    font-size: var(--font-size-lg);
    font-weight: var(--font-weight-bold);
  }
}
```

---

### [실무]

SCSS 리뷰 기준:

```md
- [ ] nesting 깊이가 과하지 않은가?
- [ ] mixin이 남용되지 않는가?
- [ ] partial 구조가 명확한가?
- [ ] CSS variable과 Sass variable 역할이 구분되는가?
- [ ] 전역 selector 충돌 가능성이 없는가?
```

---

### [FAQ]

Q. SCSS nesting은 깊게 써도 돼?

A.
권장하지 않는다. nesting이 깊으면 selector가 복잡해지고 override가 어려워진다.

Q. Sass variable과 CSS variable 중 뭐가 좋아?

A.
Sass variable은 빌드 시점 값이고 CSS variable은 런타임 변경과 theme에 유리하다.

---

## 6.6 Styling Method Comparison

### [Comparison]

| 방식         | 장점                  | 단점              | 적합 상황              |
| ------------ | --------------------- | ----------------- | ---------------------- |
| Plain CSS    | 단순함, 표준          | 전역 충돌 가능    | 소규모, 학습, 단순 앱  |
| CSS Module   | scope 안전            | class 조합 필요   | React 중소규모 앱      |
| CSS-in-JS    | 동적 스타일 강함      | 런타임 비용 가능  | 테마, 디자인 시스템    |
| Tailwind CSS | 빠른 개발, scale 강제 | className 길어짐  | 빠른 UI, 컴포넌트 기반 |
| SCSS         | 구조화, mixin         | nesting 남용 위험 | 기존 CSS 확장          |

---

### [실무]

선택 기준:

```text
학원 프로젝트 / 단순 React
→ CSS Module 또는 Plain CSS

컴포넌트 scope 중요
→ CSS Module

동적 스타일 / Theme 중요
→ CSS-in-JS

빠른 UI 작성 / Utility 선호
→ Tailwind CSS

기존 CSS 확장 / 전처리 필요
→ SCSS
```

---

### [FAQ]

Q. 어떤 스타일링 방식이 제일 좋아?

A.
정답은 없다. 팀 숙련도, 프로젝트 규모, 디자인 시스템 필요성, 배포 환경에 따라 선택한다.

Q. 여러 스타일 방식을 섞어도 돼?

A.
가능하지만 명확한 기준 없이 섞으면 유지보수가 어려워진다.

---

# 7. Naming Convention Rules

## 7.1 Class Naming Rules

### [개념]

Class Naming은 CSS class 이름을 일관되게 작성하는 규칙이다.

---

### [핵심]

좋은 class name 기준:

- 역할과 의미가 드러남
- 컴포넌트 단위 prefix 사용
- 시각 속성보다 도메인 / 역할 중심
- 너무 짧거나 모호하지 않음
- 재사용 범위가 명확함

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

Class naming 리뷰 기준:

```md
- [ ] 이름이 역할을 설명하는가?
- [ ] 색상 / 크기 중심 이름을 남용하지 않는가?
- [ ] 같은 패턴이 프로젝트 전체에서 유지되는가?
- [ ] 컴포넌트 이름과 스타일 이름이 연결되는가?
```

---

### [FAQ]

Q. class 이름은 짧을수록 좋아?

A.
아니다. 의미가 명확한 이름이 더 중요하다.

Q. blue-button 같은 이름은 안 좋아?

A.
색상이 바뀌면 이름과 실제 스타일이 어긋날 수 있다. primary-button 같은 의미 기반 이름이 좋다.

---

## 7.2 BEM Rules

### [개념]

BEM은 Block, Element, Modifier를 기준으로 class 이름을 작성하는 방식이다.

형식:

```text
block
block__element
block--modifier
```

---

### [예제]

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

.festival-card--featured {
  border-color: var(--color-primary);
}
```

---

### [핵심]

BEM 장점:

- class 역할 명확
- 전역 CSS 충돌 감소
- 구조 파악 쉬움
- modifier로 상태 표현 가능

단점:

- 이름이 길어질 수 있음
- CSS Module 사용 시 필요성이 줄어들 수 있음
- 팀 규칙 없으면 어색할 수 있음

---

### [FAQ]

Q. BEM은 꼭 써야 해?

A.
필수는 아니다. Plain CSS나 SCSS에서 전역 충돌을 줄이고 구조를 명확히 할 때 유용하다.

Q. CSS Module을 쓰면 BEM이 필요 없어?

A.
필수는 아니지만 class 의미를 명확히 하기 위해 일부 패턴을 사용할 수 있다.

---

## 7.3 State Class Naming

### [개념]

State Class Naming은 active, disabled, selected, open 같은 UI 상태를 class로 표현하는 방식이다.

---

### [핵심]

권장 state naming:

```text
is-active
is-disabled
is-selected
is-open
has-error
is-loading
```

또는 component modifier:

```text
button--disabled
tab--active
input--error
modal--open
```

---

### [예제]

```css
.tab {
  color: var(--color-muted);
}

.tab.is-active {
  color: var(--color-primary);
  font-weight: var(--font-weight-bold);
}
```

---

### [실무]

React에서는 조건부 class 처리 기준이 필요하다.

```jsx
<button className={`tab ${isActive ? "is-active" : ""}`} type="button">
  메뉴
</button>
```

class 조합이 복잡하면 `clsx` 같은 유틸 사용을 고려한다.

---

### [FAQ]

Q. 상태 class는 어떻게 이름 짓는 게 좋아?

A.
`is-active`, `has-error`, `is-loading`처럼 상태 의미가 명확하게 드러나게 작성한다.

Q. 상태를 inline style로 처리해도 돼?

A.
간단한 경우는 가능하지만 반복되는 상태 스타일은 class로 관리하는 것이 좋다.

---

# 8. Component Styling Rules

## 8.1 Component Style

### [개념]

Component Style은 특정 컴포넌트의 UI 구조와 상태에 필요한 스타일이다.

---

### [핵심]

Component Style에 포함할 것:

- 컴포넌트 내부 layout
- component variant
- hover / active / disabled
- child element style
- component-specific responsive
- component state style

Component Style에 포함하지 않을 것:

- 전체 페이지 layout
- 전역 reset
- 전역 typography 기본값
- 다른 컴포넌트 override
- unrelated utility

---

### [예제]

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

---

### [실무]

Review 기준:

```md
- [ ] 컴포넌트 내부 스타일이 외부 layout에 의존하지 않는가?
- [ ] variant가 명확히 분리되어 있는가?
- [ ] disabled / hover / focus 상태가 있는가?
- [ ] 토큰을 사용하고 있는가?
- [ ] 다른 컴포넌트를 직접 override하지 않는가?
```

---

### [FAQ]

Q. 컴포넌트 스타일에서 margin을 줘도 돼?

A.
컴포넌트 내부 간격은 가능하지만 외부 배치 margin은 부모 layout에서 관리하는 것이 좋다.

Q. Button 컴포넌트에 width: 100%를 기본으로 넣어도 돼?

A.
모든 버튼에 필요한 스타일이 아니라면 variant나 parent layout에서 제어하는 것이 좋다.

---

## 8.2 Layout Style vs Component Style

### [개념]

Layout Style은 요소들을 배치하는 스타일이고, Component Style은 개별 UI 요소의 외형과 상태를 정의하는 스타일이다.

---

### [Comparison]

| 구분      | Layout Style                     | Component Style     |
| --------- | -------------------------------- | ------------------- |
| 목적      | 배치와 공간 구조                 | UI 요소 외형        |
| 예시      | grid, flex, gap, container width | button, card, input |
| 위치      | page / layout component          | component file      |
| 변경 영향 | 화면 구조                        | 개별 컴포넌트       |
| 재사용    | layout pattern                   | UI component        |

---

### [예제]

Layout Style:

```css
.page-layout {
  display: grid;
  gap: var(--spacing-6);
  max-width: 1200px;
  margin: 0 auto;
}
```

Component Style:

```css
.card {
  padding: var(--spacing-4);
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border);
}
```

---

### [실무]

원칙:

```text
부모는 배치 담당
자식은 자기 외형 담당
```

나쁜 예:

```css
.card {
  margin: 0 auto;
  width: 1200px;
}
```

좋은 예:

```css
.card-grid {
  display: grid;
  gap: var(--spacing-4);
}

.card {
  border: 1px solid var(--color-border);
}
```

---

### [FAQ]

Q. 컴포넌트가 자기 margin을 가지면 안 돼?

A.
항상 안 되는 것은 아니지만 재사용 컴포넌트라면 외부 배치는 부모가 담당하는 것이 좋다.

Q. layout과 component style을 왜 분리해?

A.
컴포넌트 재사용성과 화면 구조 변경의 유연성을 높이기 위해서다.

---

## 8.3 Variant Style Rules

### [개념]

Variant Style은 같은 컴포넌트가 목적이나 상태에 따라 다른 스타일을 갖는 구조다.

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

---

### [예제]

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

---

### [FAQ]

Q. variant 이름을 blue, red로 해도 돼?

A.
권장하지 않는다. 색상이 아니라 primary, danger, secondary처럼 역할 중심 이름이 좋다.

Q. disabled도 variant야?

A.
보통은 variant가 아니라 상태다. `disabled` attribute와 disabled style로 처리한다.

---

# 9. Responsive Styling Rules

## 9.1 Responsive Architecture

### [개념]

Responsive Architecture는 화면 크기에 따라 UI가 자연스럽게 변하도록 스타일 기준을 체계화하는 방식이다.

---

### [핵심]

반응형 기준:

- Mobile First 우선
- 고정 width 남용 금지
- container max-width 사용
- grid / flex 기반 layout
- image max-width 처리
- breakpoint 기준 통일
- touch target 고려
- table / modal / navigation 모바일 대응

---

### [예제]

```css
.container {
  width: min(100% - 32px, 1200px);
  margin: 0 auto;
}

.card-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--spacing-4);
}

@media (min-width: 768px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .card-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

---

### [실무]

반응형 리뷰 기준:

```md
- [ ] 모바일 360px에서 가로 스크롤이 없는가?
- [ ] tablet / desktop layout이 자연스러운가?
- [ ] 이미지와 카드가 줄바꿈되는가?
- [ ] modal이 모바일에서 화면을 넘지 않는가?
- [ ] table overflow 처리되어 있는가?
- [ ] 버튼 터치 영역이 충분한가?
```

---

### [FAQ]

Q. Mobile First가 뭐야?

A.
모바일 스타일을 기본으로 작성하고 큰 화면 스타일을 media query로 확장하는 방식이다.

Q. 반응형에서 가장 흔한 문제는 뭐야?

A.
고정 width, 큰 이미지, flex-wrap 누락, table overflow, modal width 고정이다.

---

## 9.2 Breakpoint Rules

### [개념]

Breakpoint는 화면 크기에 따라 스타일이 바뀌는 기준점이다.

---

### [핵심]

권장 breakpoint 예:

```text
mobile: default
tablet: 768px
desktop: 1024px
wide: 1280px
```

CSS variable은 media query에 직접 쓰기 어려운 경우가 있으므로 문서화가 필요하다.

---

### [예제]

```css
@media (min-width: 768px) {
  .layout {
    display: grid;
    grid-template-columns: 240px 1fr;
  }
}
```

---

### [실무]

Breakpoint 설계 원칙:

```text
기기명보다 콘텐츠가 깨지는 지점 기준
불필요한 breakpoint 남발 금지
프로젝트 전체 기준 통일
component-specific breakpoint 최소화
```

---

### [FAQ]

Q. breakpoint는 꼭 768, 1024를 써야 해?

A.
아니다. 일반 기준일 뿐이며 실제 콘텐츠가 깨지는 지점을 기준으로 조정할 수 있다.

Q. 컴포넌트마다 breakpoint가 달라도 돼?

A.
가능하지만 너무 많으면 관리가 어려워진다. 공통 breakpoint를 우선 사용한다.

---

# 10. Theme and Dark Mode Rules

## 10.1 Theme Architecture

### [개념]

Theme Architecture는 색상, 배경, 텍스트, border, shadow 같은 스타일 값을 theme별로 전환할 수 있도록 설계하는 방식이다.

---

### [핵심]

Theme 구조:

```text
Base Token
→ Semantic Token
→ Theme Override
→ Component Style
```

예:

```text
--color-blue-600
→ --color-primary
→ light/dark value
→ Button background
```

---

### [예제]

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

사용:

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

---

### [실무]

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

Q. Dark Mode를 만들려면 모든 색상을 다시 써야 해?

A.
컴포넌트가 semantic token을 사용한다면 theme token 값만 바꿔도 많은 부분을 대응할 수 있다.

Q. Theme를 만들 때 raw color를 직접 쓰면 안 돼?

A.
컴포넌트에서는 raw color보다 semantic token을 사용하는 것이 theme 확장에 좋다.

---

## 10.2 Dark Mode Rules

### [개념]

Dark Mode는 어두운 배경과 밝은 텍스트를 기준으로 UI를 전환하는 theme의 한 종류다.

---

### [핵심]

Dark Mode 체크 항목:

- background와 text contrast
- surface 색상
- border 색상
- hover 색상
- disabled 색상
- shadow 대체
- image / icon visibility
- focus style visibility
- chart / map 색상
- system preference 대응

---

### [예제]

```css
:root {
  color-scheme: light;
}

[data-theme="dark"] {
  color-scheme: dark;
}
```

---

### [실무]

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

---

### [FAQ]

Q. Dark Mode에서 단순히 배경만 검게 하면 돼?

A.
아니다. 텍스트, border, surface, hover, disabled, focus, icon 색상까지 함께 조정해야 한다.

Q. color-scheme은 왜 써?

A.
브라우저 기본 form control, scrollbar 등이 theme에 맞게 표시되도록 돕는다.

---

# 11. Interaction State Style Rules

## 11.1 State Style

### [개념]

State Style은 사용자의 상호작용이나 컴포넌트 상태에 따라 달라지는 스타일이다.

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

### [핵심]

반드시 검토할 상태:

```md
- [ ] button hover
- [ ] button disabled
- [ ] input focus
- [ ] input error
- [ ] link hover
- [ ] selected tab
- [ ] active menu
- [ ] loading button
- [ ] modal open
```

---

### [예제]

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

---

### [FAQ]

Q. hover만 있으면 충분해?

A.
아니다. keyboard 사용자를 위해 focus style도 필요하고, disabled / active / error 상태도 고려해야 한다.

Q. disabled 스타일은 왜 필요해?

A.
사용자가 조작 불가능한 상태를 시각적으로 이해해야 하기 때문이다.

---

## 11.2 Focus Style Rules

### [개념]

Focus Style은 키보드나 보조 기술 사용자가 현재 조작 중인 요소를 알 수 있게 하는 스타일이다.

---

### [핵심]

Focus Style 기준:

- focus outline 제거 금지
- 제거 시 대체 focus style 제공
- 색상 대비 충분
- button, link, input, select, textarea 모두 확인
- modal 내부 focus 이동 확인
- skip link 고려 가능

---

### [예제]

```css
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

---

### [주의]

나쁜 예:

```css
* {
  outline: none;
}
```

좋은 예:

```css
.button:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

---

### [FAQ]

Q. focus outline이 디자인상 안 예쁘면 지워도 돼?

A.
지우기만 하면 안 된다. 반드시 대체 focus style을 제공해야 한다.

Q. focus와 focus-visible 차이는 뭐야?

A.
focus는 모든 포커스 상태에 적용되고, focus-visible은 주로 키보드 접근처럼 시각적 표시가 필요한 경우에 적용된다.

---

# 12. CSS Specificity and Override Rules

## 12.1 Specificity Management

### [개념]

Specificity는 CSS selector의 우선순위다. Styling Architecture에서는 우선순위가 복잡해지지 않도록 관리해야 한다.

---

### [핵심]

권장:

- class 기반 styling
- id selector 스타일링 지양
- 긴 selector chain 지양
- `!important` 남용 금지
- component scope 유지
- override 최소화

금지에 가까운 예:

```css
body div main section article div .card .title span {
  color: red;
}
```

---

### [실무]

좋은 구조:

```css
.cardTitle {
  color: var(--color-text);
}
```

나쁜 구조:

```css
.page .container .section .card h2.title {
  color: var(--color-text);
}
```

---

### [FAQ]

Q. CSS가 안 먹으면 !important를 쓰면 돼?

A.
일시 해결은 가능하지만 장기적으로 유지보수를 어렵게 만든다. selector 구조와 우선순위를 먼저 확인해야 한다.

Q. id selector를 스타일링에 쓰면 안 돼?

A.
가능하지만 우선순위가 높아 override가 어려워지므로 일반 스타일링에는 class가 더 적합하다.

---

## 12.2 Override Rules

### [개념]

Override는 기존 스타일을 다른 스타일로 덮어쓰는 것이다.

---

### [핵심]

Override가 필요한 경우:

- 외부 라이브러리 스타일 조정
- theme별 스타일 변경
- variant 스타일 적용
- 특정 page에서 spacing 조정
- responsive style 변경

주의할 경우:

- 다른 컴포넌트 내부 class 직접 수정
- 전역 selector로 강제 override
- `!important` 사용
- 깊은 selector chain 사용
- 의도하지 않은 side effect 발생

---

### [실무]

권장 override 순서:

```text
Token 변경
→ Variant 추가
→ Props 기반 style
→ Local class override
→ Global override 최소화
→ !important 최후 수단
```

---

### [FAQ]

Q. 외부 라이브러리 스타일은 어떻게 수정해?

A.
가능하면 라이브러리의 theme API나 className override API를 먼저 사용한다.

Q. !important는 절대 금지야?

A.
절대 금지는 아니지만 최후 수단으로만 사용해야 한다.

---

# 13. Utility Class Rules

## 13.1 Utility Class

### [개념]

Utility Class는 하나의 작은 스타일 역할을 수행하는 재사용 class다.

예:

```css
.sr-only {
}
.text-center {
}
.mt-4 {
}
.flex-center {
}
```

---

### [핵심]

Utility Class 적합 대상:

- screen reader only
- visually hidden
- text alignment
- flex center
- layout helper
- spacing helper
- container helper

---

### [예제]

```css
.container {
  width: min(100% - 32px, 1200px);
  margin: 0 auto;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}
```

---

### [실무]

주의:

- utility class가 너무 많으면 Tailwind와 비슷한 체계 필요
- 컴포넌트 스타일을 utility로 과도하게 조합하지 않음
- 의미 있는 component class와 균형 필요

---

### [FAQ]

Q. Utility class를 직접 만들어도 돼?

A.
가능하다. 다만 프로젝트 전체에서 일관된 규칙이 있어야 한다.

Q. Utility class가 많아지면 문제야?

A.
관리 체계 없이 많아지면 중복과 혼란이 생긴다. Tailwind 같은 체계를 쓰거나 범위를 제한해야 한다.

---

# 14. File Structure Rules

## 14.1 Styling File Structure

### [개념]

Styling File Structure는 스타일 파일을 프로젝트 안에서 어디에 배치할지 정하는 규칙이다.

---

### [핵심]

권장 구조 예:

```text
src/
├─ styles/
│  ├─ reset.css
│  ├─ tokens.css
│  ├─ globals.css
│  ├─ typography.css
│  └─ utilities.css
├─ components/
│  └─ Button/
│     ├─ Button.tsx
│     └─ Button.module.css
├─ pages/
│  └─ FestivalPage/
│     ├─ FestivalPage.tsx
│     └─ FestivalPage.module.css
└─ layout/
   └─ AppLayout/
      ├─ AppLayout.tsx
      └─ AppLayout.module.css
```

---

### [실무]

구조 판단 기준:

```md
- [ ] 전역 스타일 파일이 분리되어 있는가?
- [ ] component style이 component와 가까이 있는가?
- [ ] page layout style이 page 단위로 분리되어 있는가?
- [ ] token 파일이 독립되어 있는가?
- [ ] style import 순서가 명확한가?
```

---

### [FAQ]

Q. 스타일 파일은 컴포넌트 옆에 두는 게 좋아?

A.
컴포넌트 전용 스타일이라면 가까이 두는 것이 유지보수에 좋다.

Q. 모든 CSS를 styles 폴더에 모아도 돼?

A.
가능하지만 컴포넌트가 많아지면 어떤 스타일이 어디에 쓰이는지 추적하기 어려울 수 있다.

---

## 14.2 Import Order Rules

### [개념]

Style Import Order는 CSS 파일을 어떤 순서로 불러올지 정하는 규칙이다.

---

### [핵심]

권장 순서:

```text
Reset
→ Token
→ Global
→ Typography
→ Utility
→ Layout
→ Component
```

---

### [예제]

```js
import "./styles/reset.css";
import "./styles/tokens.css";
import "./styles/globals.css";
import "./styles/typography.css";
import "./styles/utilities.css";
```

---

### [실무]

주의:

- reset이 component style 뒤에 오면 스타일이 깨질 수 있음
- token 파일은 token 사용 파일보다 먼저 import
- global override가 component style을 덮어쓰지 않게 주의
- CSS Module은 component에서 import

---

### [FAQ]

Q. CSS import 순서가 중요해?

A.
중요하다. 같은 우선순위의 selector는 나중에 import된 스타일이 덮어쓸 수 있다.

Q. token 파일은 언제 import해야 해?

A.
CSS variable을 사용하는 스타일보다 먼저 import되어야 한다.

---

# 15. Tailwind Architecture Rules

## 15.1 Tailwind Project Structure

### [개념]

Tailwind Architecture는 utility class를 사용하더라도 token, component extraction, class composition 기준을 정하는 구조다.

---

### [핵심]

Tailwind 구조 기준:

- `tailwind.config.js`에 theme 확장
- 반복 UI는 component로 추출
- arbitrary value 남용 금지
- className 조건부 조합 기준 마련
- design token과 Tailwind theme 연결
- global base style 최소화
- plugin 사용 기준 명확화

---

### [예제]

Tailwind config 예:

```js
export default {
  theme: {
    extend: {
      colors: {
        primary: "#2563eb",
        error: "#dc2626",
      },
      borderRadius: {
        card: "12px",
      },
    },
  },
};
```

---

### [실무]

Tailwind 리뷰 기준:

```md
- [ ] 같은 class 조합이 반복되지 않는가?
- [ ] 반복 UI가 컴포넌트로 추출되었는가?
- [ ] `w-[437px]` 같은 arbitrary value가 남용되지 않는가?
- [ ] hover / focus / disabled 상태가 포함되어 있는가?
- [ ] responsive class가 일관적인가?
```

---

### [FAQ]

Q. Tailwind에서는 CSS 파일이 필요 없어?

A.
대부분 줄어들지만 global style, font, base reset, 일부 custom style은 필요할 수 있다.

Q. className이 너무 길면 어떻게 해?

A.
컴포넌트로 추출하거나 class 조합 유틸을 사용해 관리한다.

---

## 15.2 Tailwind Class Composition

### [개념]

Tailwind Class Composition은 조건부 class와 variant class를 안전하게 조합하는 방식이다.

---

### [예제]

```jsx
import clsx from "clsx";

function Button({ variant = "primary", disabled, children }) {
  return (
    <button
      type="button"
      disabled={disabled}
      className={clsx(
        "rounded-md px-4 py-2 font-medium",
        variant === "primary" && "bg-blue-600 text-white",
        variant === "secondary" && "border bg-white text-gray-900",
        disabled && "cursor-not-allowed opacity-50",
      )}
    >
      {children}
    </button>
  );
}
```

---

### [핵심]

권장:

- 조건부 class는 `clsx` 등으로 명확히 관리
- variant는 객체 mapping으로 분리 가능
- 반복되는 class는 컴포넌트화
- class merge 충돌 주의
- Tailwind class 순서 일관성 유지

---

### [FAQ]

Q. 조건부 Tailwind class는 삼항 연산자로 계속 써도 돼?

A.
간단한 경우는 가능하지만 복잡해지면 clsx나 variant helper로 분리하는 것이 좋다.

Q. Tailwind에서 variant가 많아지면 어떻게 해?

A.
Button, Card 같은 컴포넌트 내부에서 variant mapping을 만들거나 별도 유틸로 분리한다.

---

# 16. CSS-in-JS Architecture Rules

## 16.1 Theme Provider Rules

### [개념]

Theme Provider는 CSS-in-JS에서 theme 값을 컴포넌트에 전달하는 구조다.

---

### [예제]

```jsx
const theme = {
  colors: {
    primary: "#2563eb",
    text: "#111827",
    background: "#ffffff",
  },
  spacing: {
    sm: "8px",
    md: "16px",
  },
};

<ThemeProvider theme={theme}>
  <App />
</ThemeProvider>;
```

---

### [핵심]

검토 항목:

- theme 값이 일관적인가?
- raw color가 컴포넌트에 흩어지지 않는가?
- theme 타입이 정의되어 있는가?
- light / dark theme 구조가 있는가?
- props 기반 분기가 과도하지 않은가?

---

### [FAQ]

Q. Theme Provider는 언제 필요해?

A.
CSS-in-JS에서 색상, 간격, theme 값을 컴포넌트 전체에 일관되게 제공할 때 필요하다.

Q. Theme와 CSS variable을 같이 써도 돼?

A.
가능하다. CSS-in-JS theme와 CSS variable을 조합해 사용할 수 있다.

---

## 16.2 Dynamic Style Rules

### [개념]

Dynamic Style은 props, state, theme에 따라 스타일이 바뀌는 구조다.

---

### [예제]

```jsx
const Badge = styled.span`
  color: ${({ $status }) =>
    $status === "error" ? "var(--color-error)" : "var(--color-success)"};
`;
```

---

### [핵심]

주의:

- dynamic style 분기가 너무 많으면 variant 체계 필요
- DOM에 불필요한 props 전달 금지
- style 계산이 복잡하면 helper로 분리
- theme token 사용
- inline style과 역할 구분

---

### [FAQ]

Q. props로 스타일을 많이 바꿔도 돼?

A.
가능하지만 분기가 많아지면 variant 설계나 컴포넌트 분리가 필요하다.

Q. DOM에 스타일용 props가 내려가면 문제야?

A.
불필요한 DOM attribute 경고가 날 수 있다. transient props나 prop filtering을 사용한다.

---

# 17. Style Duplication Rules

## 17.1 Style Duplication

### [개념]

Style Duplication은 같은 스타일 패턴이 여러 파일에 반복 작성되는 문제다.

---

### [핵심]

중복이 자주 발생하는 대상:

- button style
- card style
- input style
- modal layout
- page container
- section spacing
- typography
- color
- shadow
- radius

---

### [실무]

중복 해결 우선순위:

```text
반복되는 디자인 값
→ token으로 분리

반복되는 UI 구조
→ component로 분리

반복되는 layout
→ layout component 또는 utility로 분리

반복되는 class 조합
→ variant 또는 helper로 분리
```

---

### [예제]

나쁜 예:

```css
.notice-card {
  padding: 16px;
  border-radius: 12px;
  border: 1px solid #e5e7eb;
}

.review-card {
  padding: 16px;
  border-radius: 12px;
  border: 1px solid #e5e7eb;
}
```

좋은 예:

```css
.card {
  padding: var(--spacing-4);
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border);
}
```

---

### [FAQ]

Q. 중복 스타일은 무조건 공통화해야 해?

A.
무조건은 아니다. 우연히 같은 스타일인지, 의미상 같은 패턴인지 구분해야 한다.

Q. 언제 컴포넌트로 분리해야 해?

A.
같은 UI 구조와 행동이 반복될 때 컴포넌트로 분리하는 것이 좋다.

---

## 17.2 Over-Abstraction Warning

### [개념]

Over-Abstraction은 공통화를 지나치게 많이 해서 오히려 수정과 이해가 어려워지는 문제다.

---

### [핵심]

과한 공통화 징후:

- props가 너무 많음
- variant 조합이 폭발함
- 작은 차이 때문에 조건문이 많음
- 공통 컴포넌트 수정 시 영향 범위가 너무 큼
- 실제로는 다른 UI인데 억지로 하나로 합침

---

### [실무]

공통화 판단 기준:

```text
3회 이상 반복
+ 의미가 같음
+ 변경 방향이 같음
+ 재사용 가능성이 있음
→ 공통화 고려
```

공통화 보류:

```text
모양만 우연히 비슷함
도메인 의미가 다름
변경 방향이 다름
조건 분기가 더 복잡해짐
```

---

### [FAQ]

Q. 중복이 보이면 바로 공통화해야 해?

A.
아니다. 의미와 변경 방향이 같은지 확인한 뒤 공통화해야 한다.

Q. 공통 컴포넌트가 너무 복잡해지면 어떻게 해?

A.
variant를 정리하거나 컴포넌트를 분리하는 것이 좋다.

---

# 18. Accessibility Styling Rules

## 18.1 Accessibility Style

### [개념]

Accessibility Style은 키보드, 스크린 리더, 저시력 사용자 등 다양한 사용자가 UI를 인식하고 조작할 수 있도록 돕는 스타일이다.

---

### [핵심]

검토 항목:

- focus visible
- color contrast
- disabled state
- error state
- hover에만 의존하지 않음
- text underline 제거 시 대체 표시
- reduced motion 대응
- screen reader only class
- touch target size

---

### [예제]

```css
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.error-text {
  color: var(--color-error);
}

.error-input {
  border-color: var(--color-error);
}

@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms;
    animation-iteration-count: 1;
    scroll-behavior: auto;
  }
}
```

---

### [실무]

Accessibility Style 리뷰:

```md
- [ ] focus style이 보이는가?
- [ ] error를 색상만으로 표시하지 않는가?
- [ ] disabled 상태가 명확한가?
- [ ] link와 button이 시각적으로 구분되는가?
- [ ] motion 감소 설정을 고려했는가?
```

---

### [FAQ]

Q. 에러를 빨간색으로만 표시하면 안 돼?

A.
안 된다. 텍스트 메시지, 아이콘, aria 등 추가 정보가 필요하다.

Q. hover 효과만 있으면 충분해?

A.
아니다. 키보드 사용자를 위한 focus style이 필요하다.

---

# 19. Animation and Transition Rules

## 19.1 Transition Rules

### [개념]

Transition은 상태 변화가 부드럽게 보이도록 CSS 속성 변화를 시간에 따라 처리하는 방식이다.

---

### [핵심]

적합한 대상:

- button hover
- link hover
- modal open
- dropdown open
- opacity
- transform
- background color
- border color

주의 대상:

- width / height transition 남용
- layout shift 유발
- 긴 animation
- motion sickness 유발
- prefers-reduced-motion 미고려

---

### [예제]

```css
.button {
  transition:
    background-color 150ms ease,
    transform 150ms ease;
}

.button:hover {
  background: var(--color-primary-hover);
}
```

---

### [실무]

Transition token 예:

```css
:root {
  --transition-fast: 150ms ease;
  --transition-base: 250ms ease;
}
```

사용:

```css
.card {
  transition:
    box-shadow var(--transition-fast),
    transform var(--transition-fast);
}
```

---

### [FAQ]

Q. 애니메이션은 많을수록 좋아?

A.
아니다. 사용성을 돕는 정도로 제한해야 한다.

Q. transition도 token으로 관리해야 해?

A.
반복 사용되는 duration과 easing은 token으로 관리하면 일관성에 좋다.

---

## 19.2 Reduced Motion Rules

### [개념]

Reduced Motion은 사용자가 애니메이션 감소를 설정했을 때 과도한 움직임을 줄이는 접근성 기준이다.

---

### [예제]

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms;
    animation-iteration-count: 1;
    transition-duration: 0.01ms;
    scroll-behavior: auto;
  }
}
```

---

### [핵심]

적용 대상:

- page transition
- modal animation
- carousel
- auto scrolling
- parallax
- skeleton shimmer
- hover transform

---

### [FAQ]

Q. prefers-reduced-motion은 꼭 필요해?

A.
움직임이 많은 UI라면 필요하다. 일부 사용자는 과도한 motion에 불편을 느낄 수 있다.

Q. 모든 transition을 없애야 해?

A.
사용자 설정이 reduce일 때는 불필요한 motion을 최소화하는 것이 좋다.

---

# 20. Third-party UI Library Styling Rules

## 20.1 UI Library Styling

### [개념]

Third-party UI Library Styling은 외부 UI 라이브러리의 기본 스타일을 프로젝트 디자인에 맞게 조정하는 방식이다.

예:

- MUI
- Ant Design
- Bootstrap
- Chakra UI
- Radix UI
- Headless UI

---

### [핵심]

검토 항목:

- theme API 사용 여부
- 전역 override 남용 여부
- class selector 강제 override 여부
- design token과 연결 여부
- bundle size 영향
- accessibility 기본 제공 여부
- custom component와 스타일 일관성

---

### [실무]

권장 override 순서:

```text
Library Theme API
→ Component Props
→ Slot / className API
→ Local wrapper style
→ Global override 최소화
```

---

### [FAQ]

Q. UI 라이브러리 스타일은 그냥 CSS로 덮어써도 돼?

A.
가능하지만 theme API나 component props를 먼저 사용하는 것이 안전하다.

Q. 외부 UI 라이브러리를 쓰면 Styling Architecture가 필요 없어?

A.
아니다. theme, override, custom component와의 일관성 기준이 필요하다.

---

# 21. Troubleshooting Rules

## 21.1 CSS Not Applied

### [개념]

CSS Not Applied는 작성한 스타일이 화면에 적용되지 않는 문제다.

---

### [핵심]

원인:

- CSS 파일 import 누락
- className 오타
- CSS Module import 오류
- selector 우선순위 문제
- 작성 순서 문제
- scoped class와 global class 혼동
- browser cache
- Tailwind class purge 문제
- build output cache

---

### [Flow]

```text
Element Inspect
→ className 적용 확인
→ CSS rule 로드 확인
→ computed style 확인
→ specificity 확인
→ import order 확인
→ cache 확인
```

---

### [FAQ]

Q. CSS가 안 먹을 때 제일 먼저 뭐 봐?

A.
브라우저 개발자 도구에서 해당 요소에 class가 실제로 붙었는지 확인한다.

Q. CSS Module 스타일이 안 먹어?

A.
`styles.className`으로 접근했는지, 파일명이 `module.css`인지, import가 맞는지 확인한다.

---

## 21.2 Style Conflict

### [개념]

Style Conflict는 여러 CSS 규칙이 같은 요소에 적용되어 의도와 다른 스타일이 나타나는 문제다.

---

### [핵심]

원인:

- 전역 class 이름 중복
- selector specificity 차이
- import order 문제
- UI library global style
- reset style 영향
- parent style inheritance
- media query override

---

### [실무]

해결 우선순위:

```text
DevTools Computed 확인
→ 적용된 CSS source 확인
→ selector 단순화
→ scope 분리
→ class naming 수정
→ import order 정리
→ token / variant 구조로 개선
```

---

### [FAQ]

Q. 스타일이 자꾸 다른 곳에도 적용돼?

A.
전역 class 충돌 가능성이 높다. CSS Module이나 naming convention을 고려한다.

Q. import 순서 때문에 스타일이 바뀔 수 있어?

A.
그렇다. 같은 우선순위라면 나중에 import된 스타일이 적용될 수 있다.

---

## 21.3 Responsive Broken

### [개념]

Responsive Broken은 화면 크기 변화에 따라 레이아웃이 깨지는 문제다.

---

### [핵심]

원인:

- fixed width
- min-width 문제
- image max-width 누락
- flex-wrap 누락
- grid minmax 누락
- table overflow 누락
- modal width 고정
- long text overflow

---

### [Flow]

```text
Mobile Width 확인
→ 가로 스크롤 원인 요소 찾기
→ fixed width 확인
→ image / table 확인
→ flex item min-width 확인
→ media query 확인
→ 수정
```

---

### [FAQ]

Q. 모바일에서 가로 스크롤이 생겨?

A.
고정 width, 큰 이미지, 긴 텍스트, flex item min-width, table overflow 문제가 원인일 수 있다.

Q. flex item이 줄어들지 않아?

A.
`min-width: 0`이 필요할 수 있다.

---

## 21.4 Z-index Problem

### [개념]

Z-index Problem은 modal, dropdown, tooltip 등이 예상한 순서로 겹쳐 보이지 않는 문제다.

---

### [핵심]

원인:

- stacking context
- transform 사용
- opacity 사용
- position 미설정
- 부모 overflow hidden
- z-index scale 부재
- portal 미사용

---

### [Flow]

```text
Target Element 확인
→ position 확인
→ parent stacking context 확인
→ overflow hidden 확인
→ z-index token 확인
→ portal 필요 여부 확인
```

---

### [FAQ]

Q. z-index를 9999로 줬는데도 안 돼?

A.
부모 stacking context나 overflow hidden 때문에 가려질 수 있다.

Q. dropdown이 card 뒤에 숨어?

A.
부모 요소의 overflow, stacking context, z-index를 확인해야 한다.

---

# 22. Review Agent Rules

## 22.1 Styling Review Checklist

### [Checklist]

Review Agent는 스타일 구조 검토 시 다음을 확인한다.

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
→ Responsive 확인
→ Accessibility Style 확인
→ Duplication 확인
→ Troubleshooting Risk 확인
→ Final Review
```

---

### [FAQ]

Q. Review Agent가 스타일 코드에서 가장 먼저 봐야 할 것은?

A.
스타일 방식의 일관성, 전역 충돌 가능성, token 사용 여부, 반응형과 접근성 스타일이다.

Q. 스타일이 화면상 예쁘면 승인해도 돼?

A.
아니다. 유지보수성, 반응형, 접근성, 중복, 충돌 가능성까지 검토해야 한다.

---

# 23. Frontend Agent Rules

## 23.1 Styling Generation Rules

### [개념]

Frontend Agent는 스타일 코드를 생성할 때 프로젝트의 Styling Architecture를 따라야 한다.

---

### [핵심]

Frontend Agent 스타일 생성 기준:

```md
- [ ] 프로젝트의 스타일링 방식을 먼저 확인한다.
- [ ] raw color보다 token을 사용한다.
- [ ] component style과 layout style을 분리한다.
- [ ] hover / focus / disabled 상태를 포함한다.
- [ ] mobile first 기준으로 작성한다.
- [ ] fixed width를 남용하지 않는다.
- [ ] 접근성 스타일을 제거하지 않는다.
- [ ] class naming을 일관되게 작성한다.
- [ ] 중복 스타일은 component 또는 token으로 분리한다.
```

---

### [예제]

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

---

### [FAQ]

Q. Frontend Agent가 스타일을 만들 때 가장 조심할 점은?

A.
프로젝트 기존 스타일 방식과 token 체계를 따르는 것이 가장 중요하다.

Q. Agent가 임의 색상값을 만들어도 돼?

A.
가능하면 기존 token을 사용하고, 없는 경우 새 token 추가 이유를 명확히 해야 한다.

---

# 24. PM Agent Rules

## 24.1 PM Styling Quality Check

### [개념]

PM Agent는 Styling Architecture를 기준으로 UI 품질과 완료 여부를 판단한다.

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
- [ ] 배포 전 수정이 필요한 스타일 이슈가 있는가?
```

---

### [실무]

PM Agent 판단 기준:

```text
UI Complete
→ 요구사항 충족 + 주요 화면 일관성 + 반응형 OK

UI Partial
→ 기능은 있으나 일부 스타일 불일치 또는 반응형 미흡

UI Blocked
→ 모바일 깨짐, 주요 버튼 식별 불가, 접근성 심각, 사용 흐름 방해
```

---

### [FAQ]

Q. PM Agent가 CSS 코드까지 봐야 해?

A.
세부 구현 전체보다는 UI 일관성, 반응형, 사용자 흐름, 완료 여부를 중심으로 판단한다.

Q. 스타일 이슈도 기능 완료를 막을 수 있어?

A.
사용자가 기능을 사용하기 어렵게 만들면 Blocker가 될 수 있다.

---

# 25. Common Styling Mistakes

## 25.1 Common Mistakes

### [개념]

Styling Architecture 문서는 자주 발생하는 스타일 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생하는 실수:

- 모든 스타일을 globals.css에 작성
- raw color 하드코딩 남발
- spacing 값 무작위 사용
- CSS variable 없이 반복 값 사용
- reset에서 focus outline 제거
- `!important` 남용
- id selector 스타일링 남용
- 긴 selector chain
- inline style 남용
- component style이 parent layout에 강하게 의존
- margin으로 layout gap 남용
- fixed width 남용
- 모바일 가로 스크롤 방치
- hover만 있고 focus 없음
- disabled style 없음
- dark mode에서 contrast 깨짐
- z-index 9999 남발
- Tailwind arbitrary value 남용
- CSS-in-JS props 분기 과다
- SCSS nesting 과다
- 외부 라이브러리 스타일 전역 override 남용

---

### [Troubleshooting]

문제별 빠른 판단:

```text
스타일 안 먹음
→ import / className / specificity / cache 확인

다른 화면까지 스타일 영향
→ global class 충돌 / selector 범위 확인

모바일 깨짐
→ fixed width / image / flex-wrap / overflow 확인

z-index 안 먹음
→ stacking context / overflow hidden / portal 확인

dark mode 이상함
→ raw color / semantic token / contrast 확인
```

---

### [FAQ]

Q. 스타일 초보가 가장 많이 하는 실수는?

A.
전역 CSS에 모든 스타일을 넣고, 색상과 간격을 하드코딩하며, 반응형과 focus 상태를 놓치는 경우가 많다.

Q. `!important`를 쓰면 빨리 해결되는데 왜 문제야?

A.
나중에 override가 더 어려워지고 스타일 우선순위가 복잡해지기 때문이다.

---

# 26. Final Quality Checklist

## 26.1 Styling Architecture Quality Checklist

### [Checklist]

최종 Styling Architecture 체크리스트:

```md
## Structure

- [ ] 스타일링 방식이 프로젝트 기준과 일치하는가?
- [ ] Global Style과 Component Style이 분리되어 있는가?
- [ ] Reset / Token / Global / Utility 파일 구조가 있는가?
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

## Maintainability

- [ ] 중복 스타일이 과하지 않은가?
- [ ] `!important` 남용이 없는가?
- [ ] selector가 과도하게 깊지 않은가?
- [ ] 외부 라이브러리 override가 안전한가?
```

---

### [FAQ]

Q. 이 체크리스트를 매번 다 써야 해?

A.
변경 범위에 따라 선택 적용할 수 있다. 다만 token, 반응형, 접근성, 충돌 가능성은 항상 확인하는 것이 좋다.

Q. 최종 승인 기준은 뭐야?

A.
스타일 방식이 일관되고, 반응형과 접근성 문제가 없으며, 유지보수 가능한 구조여야 한다.

---

# 27. Final Goal

## 27.1 Domain Final Goal

### [개념]

Styling Architecture Domain Rules의 최종 목적은 Frontend Agent가 일관된 스타일 코드를 생성하고, Review Agent가 스타일 구조의 유지보수성, 반응형, 접근성, 테마 확장성을 검토하며, PM Agent가 UI 품질 완료 여부를 판단할 수 있도록 하는 것이다.

---

### [핵심]

최종 수행 가능 작업:

- 스타일링 방식 선택
- Plain CSS / CSS Module / CSS-in-JS / Tailwind CSS 비교
- Global Style과 Component Style 분리
- Design Token 정의
- CSS Variable 사용
- Class Naming 검토
- Component Variant Style 설계
- Responsive Styling 설계
- Theme / Dark Mode 구조 판단
- Focus / Disabled / Error 상태 스타일 검토
- CSS Specificity 문제 분석
- Style Duplication 검토
- Tailwind class 구조 검토
- CSS-in-JS theme 구조 검토
- Styling Troubleshooting 수행
- Styling Code Review 수행

---

### [실무]

최종 Agent Flow:

```text
Styling Request
→ Project Styling Method 확인
→ Token 확인
→ Global / Component 책임 분리
→ Component Style 생성
→ Responsive 적용
→ Interaction State 적용
→ Accessibility Style 확인
→ Duplication 제거
→ Review Checklist 수행
```

---

### [FAQ]

Q. Styling Architecture 문서의 최종 목적은 뭐야?

A.
Frontend Agent / Review Agent / PM Agent가 스타일 구조를 일관되게 설계하고 검토할 수 있도록 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
Design System Domain Rules가 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Styling Architecture 문서는 왜 필요해?

A.
Frontend Agent / Review Agent / PM Agent가 스타일 구조, CSS 관리 방식, 디자인 토큰, 반응형, 테마, 접근성 스타일을 일관되게 판단하기 위해 필요하다.

Q. Styling Architecture가 뭐야?

A.
프로젝트에서 스타일을 어디에, 어떤 기준으로, 어떤 도구로 작성하고 관리할지 정하는 구조다.

Q. 스타일 구조가 없으면 뭐가 문제야?

A.
CSS 충돌, 중복 스타일, 색상 불일치, 반응형 깨짐, 유지보수 어려움이 생길 수 있다.

Q. Styling Architecture와 Design System은 뭐가 달라?

A.
Styling Architecture는 스타일 코드 구조와 관리 방식이고, Design System은 UI 규격과 컴포넌트 체계까지 포함한다.

Q. Global Style에는 무엇을 넣어야 해?

A.
reset, body 기본 스타일, font-family, text color, background, CSS variable, image 기본 스타일 같은 전체 기본 스타일을 넣는다.

Q. Global Style에 넣으면 안 되는 것은?

A.
특정 Card, Modal, Button variant, Page layout 같은 컴포넌트 전용 스타일은 넣지 않는 것이 좋다.

Q. reset css는 왜 필요해?

A.
브라우저 기본 스타일 차이를 줄이고 프로젝트 스타일 기준을 통일하기 위해 사용한다.

Q. reset에서 outline none을 써도 돼?

A.
권장하지 않는다. 제거한다면 반드시 대체 focus style을 제공해야 한다.

Q. Reset CSS와 Normalize CSS 차이는?

A.
Reset은 기본 스타일 제거 중심이고 Normalize는 브라우저 차이 보정 중심이다.

Q. Design Token이 뭐야?

A.
색상, 간격, 폰트, radius, shadow, z-index 같은 디자인 값을 이름으로 관리하는 방식이다.

Q. Design Token은 왜 필요해?

A.
스타일 일관성을 유지하고 수정 범위를 줄이며 theme 확장을 쉽게 하기 위해 필요하다.

Q. 모든 값을 token으로 만들어야 해?

A.
아니다. 반복 사용되거나 의미 있는 값부터 token으로 관리한다.

Q. Color Token은 어떻게 나눠?

A.
primary, text, muted, background, surface, border, success, warning, error, info처럼 역할 기준으로 나눈다.

Q. raw color를 직접 쓰면 안 돼?

A.
한두 번은 가능하지만 반복되는 색상은 token으로 분리하는 것이 좋다.

Q. Spacing Token은 왜 필요해?

A.
margin, padding, gap 값이 화면마다 제각각이 되는 것을 막고 UI 리듬을 유지하기 위해 필요하다.

Q. Typography Token은 뭘 관리해?

A.
font-size, font-weight, line-height, font-family, letter-spacing 같은 글자 스타일을 관리한다.

Q. Z-index Token은 왜 필요해?

A.
modal, toast, dropdown, header 같은 겹침 UI의 우선순위를 체계적으로 관리하기 위해 필요하다.

Q. z-index를 크게 주면 해결돼?

A.
아니다. stacking context 때문에 큰 숫자를 줘도 해결되지 않을 수 있다.

Q. Plain CSS는 언제 적합해?

A.
소규모 프로젝트, 학원 프로젝트, 빠른 프로토타입, 단순한 앱에 적합하다.

Q. Plain CSS의 가장 큰 위험은?

A.
전역 class 충돌과 selector 우선순위 복잡도다.

Q. CSS Module은 뭐야?

A.
CSS class를 파일 단위로 scope 처리해 class 이름 충돌을 줄이는 방식이다.

Q. CSS Module은 언제 좋아?

A.
React 컴포넌트 단위 스타일을 안전하게 관리하고 싶을 때 좋다.

Q. CSS Module 파일명은 어떻게 해?

A.
보통 `ComponentName.module.css` 형식을 사용한다.

Q. CSS-in-JS는 뭐야?

A.
JavaScript 또는 TypeScript 파일 안에서 스타일을 작성하는 방식이다.

Q. CSS-in-JS는 언제 적합해?

A.
동적 스타일, theme provider, 디자인 시스템 컴포넌트 구현이 중요한 경우 적합하다.

Q. CSS-in-JS의 단점은 뭐야?

A.
런타임 비용, 번들 크기 증가, 스타일과 로직 과결합 위험이 있다.

Q. Styled Components에서 `$variant`처럼 `$`를 붙이는 이유는?

A.
DOM으로 전달되지 않는 transient props로 구분하기 위해 사용한다.

Q. Tailwind CSS는 뭐야?

A.
utility class를 조합해 스타일을 작성하는 Utility First CSS 프레임워크다.

Q. Tailwind를 쓰면 CSS Architecture가 필요 없어?

A.
아니다. Tailwind도 token, component extraction, class composition 기준이 필요하다.

Q. Tailwind className이 너무 길면 어떻게 해?

A.
반복되는 UI를 컴포넌트로 추출하거나 class 조합 유틸을 사용한다.

Q. Tailwind arbitrary value를 써도 돼?

A.
필요할 때는 가능하지만 남용하면 design scale이 깨진다.

Q. SCSS는 언제 적합해?

A.
기존 CSS를 구조화하고 nesting, mixin, partial 파일 분리가 필요한 경우 적합하다.

Q. SCSS nesting은 깊게 써도 돼?

A.
권장하지 않는다. nesting이 깊으면 selector가 복잡해지고 override가 어려워진다.

Q. Sass variable과 CSS variable 차이는?

A.
Sass variable은 빌드 시점 값이고 CSS variable은 런타임 변경과 theme에 유리하다.

Q. 어떤 스타일링 방식이 제일 좋아?

A.
정답은 없다. 팀 숙련도, 프로젝트 규모, 디자인 시스템 필요성, 배포 환경에 따라 선택한다.

Q. 여러 스타일 방식을 섞어도 돼?

A.
가능하지만 명확한 기준 없이 섞으면 유지보수가 어려워진다.

Q. class 이름은 어떻게 지어야 해?

A.
역할과 의미가 드러나고 컴포넌트 단위로 구분되는 이름이 좋다.

Q. blue-button 같은 이름은 안 좋아?

A.
색상이 바뀌면 이름과 실제 스타일이 어긋날 수 있으므로 primary-button 같은 의미 기반 이름이 좋다.

Q. BEM은 뭐야?

A.
Block, Element, Modifier를 기준으로 `block__element--modifier` 형태로 class 이름을 작성하는 방식이다.

Q. BEM은 꼭 써야 해?

A.
필수는 아니지만 Plain CSS나 SCSS에서 구조와 충돌 방지에 유용하다.

Q. 상태 class는 어떻게 이름 짓는 게 좋아?

A.
is-active, has-error, is-loading, is-open처럼 상태 의미가 명확하게 드러나게 작성한다.

Q. Component Style에는 무엇을 넣어야 해?

A.
컴포넌트 내부 layout, variant, hover, focus, disabled, error 같은 컴포넌트 전용 스타일을 넣는다.

Q. Component Style에 넣으면 안 되는 것은?

A.
전체 page layout, global reset, 다른 컴포넌트 override 같은 스타일은 넣지 않는 것이 좋다.

Q. Layout Style과 Component Style 차이는?

A.
Layout Style은 배치와 공간 구조를 담당하고 Component Style은 개별 UI 요소의 외형과 상태를 담당한다.

Q. 컴포넌트가 자기 margin을 가져도 돼?

A.
항상 안 되는 것은 아니지만 재사용 컴포넌트라면 외부 배치는 부모가 담당하는 것이 좋다.

Q. Variant Style은 뭐야?

A.
같은 컴포넌트가 primary, secondary, danger, small, large처럼 목적이나 크기에 따라 다른 스타일을 갖는 구조다.

Q. variant 이름을 blue, red로 해도 돼?

A.
권장하지 않는다. 색상보다 primary, danger, secondary처럼 역할 중심 이름이 좋다.

Q. disabled는 variant야?

A.
보통은 variant가 아니라 상태다. disabled attribute와 disabled style로 처리한다.

Q. Responsive Styling은 어떻게 설계해?

A.
Mobile First 기준으로 작성하고, 공통 breakpoint와 유연한 layout을 사용한다.

Q. Mobile First가 뭐야?

A.
모바일 스타일을 기본으로 작성하고 큰 화면 스타일을 media query로 확장하는 방식이다.

Q. 반응형에서 가장 흔한 문제는?

A.
고정 width, 큰 이미지, flex-wrap 누락, table overflow, modal width 고정이다.

Q. breakpoint는 꼭 768, 1024를 써야 해?

A.
아니다. 일반 기준일 뿐이고 실제 콘텐츠가 깨지는 지점을 기준으로 조정할 수 있다.

Q. Theme Architecture는 뭐야?

A.
색상, 배경, 텍스트, border, shadow 같은 스타일 값을 theme별로 전환할 수 있도록 설계하는 방식이다.

Q. Dark Mode는 어떻게 설계해?

A.
semantic token을 정의하고 light / dark theme에서 token 값만 바뀌도록 설계하는 것이 좋다.

Q. Dark Mode에서 단순히 배경만 검게 하면 돼?

A.
아니다. 텍스트, border, surface, hover, disabled, focus, icon 색상까지 함께 조정해야 한다.

Q. color-scheme은 왜 써?

A.
브라우저 기본 form control과 scrollbar 등이 theme에 맞게 표시되도록 돕는다.

Q. State Style은 뭐야?

A.
hover, active, focus, disabled, selected, loading, error 같은 UI 상태에 따른 스타일이다.

Q. hover만 있으면 충분해?

A.
아니다. keyboard 사용자를 위한 focus style과 disabled, active, error 상태도 필요하다.

Q. Focus Style은 왜 필요해?

A.
키보드 사용자가 현재 조작 중인 요소를 알 수 있어야 하기 때문이다.

Q. focus outline이 디자인상 안 예쁘면 지워도 돼?

A.
지우기만 하면 안 된다. 반드시 대체 focus style을 제공해야 한다.

Q. CSS Specificity는 왜 관리해야 해?

A.
우선순위가 복잡해지면 스타일 override가 어려워지고 예측하기 힘든 충돌이 생긴다.

Q. CSS가 안 먹으면 !important를 써도 돼?

A.
최후 수단으로만 사용해야 한다. 먼저 selector, import order, specificity를 확인해야 한다.

Q. id selector를 스타일링에 써도 돼?

A.
가능하지만 우선순위가 높아 override가 어려워지므로 일반 스타일링에는 class가 더 적합하다.

Q. 외부 라이브러리 스타일은 어떻게 override해?

A.
라이브러리의 theme API, component props, slot API를 먼저 사용하고 global override는 최소화한다.

Q. Utility Class는 뭐야?

A.
text-center, sr-only, container, flex-center처럼 작은 스타일 역할을 수행하는 재사용 class다.

Q. Utility Class를 직접 만들어도 돼?

A.
가능하지만 프로젝트 전체에서 일관된 규칙이 있어야 한다.

Q. 스타일 파일은 어디에 두는 게 좋아?

A.
전역 스타일은 styles 폴더에, 컴포넌트 전용 스타일은 컴포넌트 옆에 두는 방식이 유지보수에 좋다.

Q. CSS import 순서가 중요해?

A.
중요하다. 같은 우선순위라면 나중에 import된 스타일이 덮어쓸 수 있다.

Q. CSS import 순서는 어떻게 하는 게 좋아?

A.
Reset → Token → Global → Typography → Utility → Layout → Component 순서가 좋다.

Q. Tailwind에서 config는 왜 중요해?

A.
색상, spacing, radius 같은 theme 값을 프로젝트 기준으로 통일하기 위해 중요하다.

Q. Tailwind 조건부 class는 어떻게 관리해?

A.
간단한 경우 삼항 연산자로 가능하지만 복잡해지면 clsx나 variant helper를 사용한다.

Q. CSS-in-JS Theme Provider는 언제 필요해?

A.
색상, 간격, theme 값을 컴포넌트 전체에 일관되게 제공할 때 필요하다.

Q. props로 스타일을 많이 바꿔도 돼?

A.
가능하지만 분기가 많아지면 variant 설계나 컴포넌트 분리가 필요하다.

Q. Style Duplication은 뭐야?

A.
같은 스타일 패턴이 여러 파일에 반복 작성되는 문제다.

Q. 중복 스타일은 무조건 공통화해야 해?

A.
아니다. 의미와 변경 방향이 같은지 확인한 뒤 공통화해야 한다.

Q. Over-Abstraction은 뭐야?

A.
공통화를 지나치게 많이 해서 props와 variant가 복잡해지고 오히려 수정이 어려워지는 문제다.

Q. 에러를 빨간색으로만 표시하면 안 돼?

A.
안 된다. 텍스트 메시지, 아이콘, aria 등 추가 정보가 필요하다.

Q. transition은 어디에 쓰면 좋아?

A.
button hover, modal open, dropdown, opacity, transform 같은 상태 변화에 적합하다.

Q. prefers-reduced-motion은 왜 필요해?

A.
움직임에 민감한 사용자를 위해 과도한 animation과 transition을 줄이기 위해 필요하다.

Q. UI 라이브러리를 쓰면 Styling Architecture가 필요 없어?

A.
아니다. theme, override, custom component와의 일관성 기준이 필요하다.

Q. CSS가 안 먹을 때 제일 먼저 뭘 확인해?

A.
브라우저 개발자 도구에서 className이 실제로 붙었는지, CSS rule이 로드되었는지 확인한다.

Q. CSS Module 스타일이 안 먹어?

A.
파일명이 `module.css`인지, import가 맞는지, `styles.className`으로 접근했는지 확인한다.

Q. 스타일이 다른 화면까지 영향을 줘?

A.
전역 class 충돌 가능성이 높다. scope 분리, CSS Module, naming convention을 고려한다.

Q. 모바일에서 가로 스크롤이 생겨?

A.
고정 width, 큰 이미지, 긴 텍스트, flex item min-width, table overflow가 원인일 수 있다.

Q. flex item이 줄어들지 않아?

A.
`min-width: 0`이 필요할 수 있다.

Q. z-index가 안 먹어?

A.
stacking context, parent overflow hidden, position, transform, portal 사용 여부를 확인한다.

Q. Review Agent는 스타일에서 뭘 봐야 해?

A.
스타일 방식 일관성, token 사용, global/component 분리, 반응형, 접근성, 중복, 충돌 가능성을 확인해야 한다.

Q. 스타일이 예쁘면 승인해도 돼?

A.
아니다. 유지보수성, 반응형, 접근성, 중복, 충돌 가능성도 검토해야 한다.

Q. Frontend Agent가 스타일을 생성할 때 가장 중요한 것은?

A.
프로젝트 기존 styling method와 token 체계를 따르는 것이다.

Q. Agent가 임의 색상값을 만들어도 돼?

A.
가능하면 기존 token을 사용하고, 없는 경우 새 token 추가 이유를 명확히 해야 한다.

Q. PM Agent는 스타일 품질을 어떻게 판단해?

A.
요구사항 일치, UI 일관성, 모바일 대응, 사용자 흐름, 접근성 문제가 있는지 중심으로 판단한다.

Q. 스타일 이슈도 기능 완료를 막을 수 있어?

A.
사용자가 기능을 사용하기 어렵게 만들면 Blocker가 될 수 있다.

Q. 스타일 초보가 가장 많이 하는 실수는?

A.
전역 CSS에 모든 스타일을 넣고, 색상과 간격을 하드코딩하며, 반응형과 focus 상태를 놓치는 경우가 많다.

Q. Styling Architecture 최종 승인 기준은?

A.
스타일 방식이 일관되고, 반응형과 접근성 문제가 없으며, 유지보수 가능한 구조여야 한다.

Q. Styling Architecture 다음 문서는 뭐야?

A.
Design System Domain Rules가 이어지는 것이 좋다.
