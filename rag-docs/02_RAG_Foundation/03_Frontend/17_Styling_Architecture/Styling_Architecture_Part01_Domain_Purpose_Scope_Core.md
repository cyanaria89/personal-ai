# Styling Architecture Part01 - Domain Purpose, Scope, Core

---

# 1. Domain Purpose

## 1.1 Styling Architecture Purpose

### [개념]

Styling Architecture는 프론트엔드 프로젝트에서 스타일을 어디에 작성하고, 어떤 기준으로 분리하며, 어떤 도구와 규칙으로 관리할지 정의하는 구조다.

이 문서는 사람용 CSS 학습 문서가 아니다.

이 문서는 Frontend Agent, Review Agent, PM Agent가 스타일 구조를 설계하고 검토하기 위한 RAG Retrieval 최적화 문서다.

목적:

- CSS 구조 설계 기준 제공
- 스타일링 방식 선택 기준 제공
- Global Style과 Component Style 분리 기준 제공
- Design Token 기반 스타일 관리 기준 제공
- CSS 충돌과 중복 방지 기준 제공
- Responsive Styling 기준 제공
- Theme / Dark Mode 구조 판단 기준 제공
- Accessibility Style 검토 기준 제공
- Frontend Agent의 스타일 코드 생성 기준 제공
- Review Agent의 스타일 구조 검토 기준 제공
- PM Agent의 UI 품질 판단 기준 제공

---

### [핵심]

Styling Architecture 핵심 기준:

- 스타일 책임이 분리되어야 한다.
- 전역 스타일과 컴포넌트 스타일이 구분되어야 한다.
- 색상, 간격, 폰트, radius, z-index는 token으로 관리해야 한다.
- CSS 충돌 가능성을 줄여야 한다.
- 스타일링 방식은 프로젝트 전체에서 일관되어야 한다.
- 반응형 기준은 통일되어야 한다.
- hover, focus, active, disabled, error 상태를 관리해야 한다.
- 접근성 스타일을 제거하지 않아야 한다.
- 중복 스타일은 token, component, utility로 분리해야 한다.
- 유지보수 가능한 구조여야 한다.

---

### [실무]

2026 실무 기준으로 Frontend Agent는 스타일을 단순히 예쁘게 작성하면 안 된다.

실무 판단 Flow:

```text
UI Requirement
→ Project Styling Method 확인
→ Design Token 확인
→ Global Style / Component Style 분리
→ Layout Style / Component Style 분리
→ Responsive Rule 적용
→ Interaction State 적용
→ Accessibility Style 확인
→ Duplication 확인
→ Review Agent 검토
```

실무에서 좋은 Styling Architecture는 다음 질문에 답할 수 있어야 한다.

```md
- [ ] 전역 스타일은 어디에 작성하는가?
- [ ] 컴포넌트 스타일은 어디에 작성하는가?
- [ ] 페이지 레이아웃 스타일은 어디에 작성하는가?
- [ ] 색상과 간격은 어디에서 관리하는가?
- [ ] class naming 규칙은 무엇인가?
- [ ] 반응형 breakpoint는 무엇인가?
- [ ] 공통 UI 스타일은 어떻게 재사용하는가?
- [ ] dark mode는 어떻게 처리하는가?
- [ ] style override는 어디까지 허용하는가?
```

---

### [FAQ]

Q. Styling Architecture 문서는 CSS 공부용이야?
A. 아니다. Frontend Agent, Review Agent, PM Agent가 스타일 구조를 설계하고 검토하기 위한 RAG 문서다.

Q. Styling Architecture에서 가장 중요한 것은 뭐야?
A. 스타일이 일관되고, 충돌이 적고, 재사용 가능하며, 유지보수 가능한 구조인지가 중요하다.

Q. 스타일은 그냥 CSS 파일 하나에 작성하면 안 돼?
A. 작은 프로젝트에서는 가능하지만 규모가 커지면 충돌, 중복, 유지보수 문제가 커질 수 있다.

Q. 스타일 도구는 하나만 정답이 있어?
A. 없다. 프로젝트 규모, 팀 숙련도, 디자인 시스템 필요성, 빌드 환경에 따라 선택해야 한다.

---

## 1.2 Agent Role in Styling Architecture

### [개념]

Styling Architecture는 Agent별 역할을 분리해서 사용해야 한다.

Agent별 책임:

- Frontend Agent: 스타일 코드 생성
- Review Agent: 스타일 구조 검토
- PM Agent: UI 품질 완료 판단

각 Agent는 같은 Styling Architecture 기준을 공유해야 한다.

---

### [핵심]

Frontend Agent 책임:

- 프로젝트 스타일링 방식 확인
- token 기반 스타일 생성
- component style 작성
- responsive style 작성
- interaction state 작성
- accessibility style 유지

Review Agent 책임:

- styling method 일관성 검토
- global / component 분리 검토
- token 사용 검토
- specificity 문제 검토
- responsive 문제 검토
- accessibility style 검토
- duplication 검토

PM Agent 책임:

- 요구사항 충족 확인
- UI 일관성 확인
- 모바일 화면 확인
- 사용 흐름 방해 여부 확인
- 스타일 이슈의 blocker 여부 판단

---

### [실무]

Agent Workflow:

```text
PM Agent
→ UI Requirement 정의
→ Frontend Agent
→ Styling Architecture 기준으로 스타일 생성
→ Review Agent
→ 구조 / 반응형 / 접근성 / 중복 검토
→ PM Agent
→ UI Complete / UI Partial / UI Blocked 판단
```

PM 판단 기준:

```text
UI Complete
→ 요구사항 충족 + 스타일 일관성 + 반응형 OK + 접근성 치명 문제 없음

UI Partial
→ 기능은 있으나 스타일 불일치 또는 일부 반응형 미흡

UI Blocked
→ 모바일 깨짐, 버튼 식별 불가, 주요 흐름 방해, 접근성 심각
```

---

### [FAQ]

Q. Frontend Agent는 스타일을 자유롭게 만들어도 돼?
A. 아니다. 프로젝트의 styling method, design token, naming convention을 먼저 확인해야 한다.

Q. Review Agent는 화면이 예쁜지만 보면 돼?
A. 아니다. 유지보수성, 반응형, 접근성, 중복, 충돌 가능성까지 검토해야 한다.

Q. PM Agent가 CSS 코드까지 자세히 봐야 해?
A. 세부 CSS 전체보다 요구사항 충족, UI 일관성, 사용자 흐름, 완료 여부를 중심으로 판단한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Styling Architecture 문서는 프론트엔드 스타일 구조 설계와 검토에 필요한 실무 범위를 포함한다.

포함 범위:

- CSS Architecture
- Global Style
- Reset CSS
- Normalize CSS
- Component Style
- Layout Style
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
- Spacing Token
- Color Token
- Typography Token
- Z-index Token
- Shadow Token
- Radius Token
- State Style
- Focus Style
- Style Duplication
- Style Review Checklist
- Styling Troubleshooting

---

### [핵심]

반드시 포함해야 하는 기준:

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
→ Design System Foundation
```

문서 연계 기준:

```text
CSS 기본 문법
→ HTML CSS Foundation

React 컴포넌트 구조
→ React Component Design

공통 UI 패턴
→ UI Component Pattern

접근성 세부 기준
→ Frontend Accessibility

리뷰 기준
→ Frontend Code Review

디자인 토큰과 UI 규격
→ Design System Foundation
```

---

### [FAQ]

Q. Styling Architecture와 Design System은 뭐가 달라?
A. Styling Architecture는 스타일 코드 구조와 관리 방식이고, Design System은 UI 규격, 컴포넌트 규칙, 디자인 토큰 체계까지 포함하는 더 큰 시스템이다.

Q. CSS 기초도 여기서 다뤄?
A. 기초 문법은 HTML CSS Foundation 문서에서 다루고, 여기서는 구조와 관리 기준을 중심으로 다룬다.

Q. Tailwind도 이 문서 범위야?
A. Tailwind 사용 구조와 리뷰 기준은 포함한다. Tailwind 문법 전체 설명은 별도 문서로 분리할 수 있다.

Q. Theme와 Dark Mode도 Styling Architecture 범위야?
A. 포함된다. token 기반 theme 구조와 dark mode 확장 가능성을 검토해야 한다.

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
- HTML CSS Foundation 문서와 중복 방지
- React Component Design 문서와 책임 분리
- Frontend Accessibility 문서와 세부 기준 중복 방지
- Design System Foundation 문서와 책임 분리
- Retrieval 혼선 방지
- Chunk 품질 유지

---

### [실무]

다른 문서로 위임하는 경우:

```text
CSS selector 상세 문법
→ HTML CSS Foundation

Flexbox / Grid 상세 문법
→ HTML CSS Foundation

React props / state / hook 문법
→ React Core

컴포넌트 구조 설계
→ React Component Design

UI 재사용 패턴
→ UI Component Pattern

접근성 ARIA 세부 기준
→ Frontend Accessibility

디자인 시스템 컴포넌트 명세
→ Design System Foundation
```

---

### [FAQ]

Q. 이 문서에서 CSS Grid와 Flexbox를 자세히 설명해?
A. 자세한 문법은 HTML CSS Foundation에서 다루고, 여기서는 레이아웃 스타일 구조와 재사용 기준을 다룬다.

Q. 애니메이션도 포함해?
A. 기본 transition과 상태 스타일 관점은 포함하지만 Framer Motion 같은 심화 애니메이션은 제외한다.

Q. Next.js 전용 styling 전략도 포함해?
A. Level 3 범위에서는 제외한다. Next.js App Router나 SSR 기반 styling 전략은 Expert Frontend 문서에서 다루는 것이 적합하다.

---

# 3. Styling Architecture Core

## 3.1 Styling Architecture Definition

### [개념]

Styling Architecture는 프로젝트에서 스타일을 어디에, 어떤 기준으로, 어떤 도구를 사용해, 어떻게 재사용하고 확장할지 정하는 구조다.

단순 CSS 작성 규칙이 아니라 다음을 포함한다.

- 스타일 파일 구조
- 스타일링 방식 선택
- 전역 스타일 관리
- 컴포넌트 스타일 관리
- 디자인 토큰 관리
- 반응형 기준
- 테마 구조
- 접근성 스타일
- override 정책
- 중복 제거 기준
- 리뷰 체크리스트

---

### [핵심]

Styling Architecture가 필요한 이유:

- CSS 충돌 방지
- 중복 스타일 감소
- 디자인 일관성 유지
- 컴포넌트 재사용성 증가
- 반응형 관리 단순화
- theme 확장 가능
- 코드 리뷰 기준 통일
- 신규 개발자 또는 Agent의 스타일 생성 안정성 향상
- UI 품질 판단 기준 명확화

---

### [실무]

좋은 Styling Architecture 조건:

```md
- [ ] 스타일링 방식이 명확하다.
- [ ] Global Style과 Component Style이 분리되어 있다.
- [ ] Design Token이 정의되어 있다.
- [ ] class naming 규칙이 있다.
- [ ] responsive breakpoint가 통일되어 있다.
- [ ] interaction state 기준이 있다.
- [ ] accessibility style을 유지한다.
- [ ] override 정책이 있다.
- [ ] 공통 스타일 재사용 기준이 있다.
- [ ] Review Agent가 검토할 수 있는 체크리스트가 있다.
```

나쁜 Styling Architecture 징후:

```md
- [ ] 모든 스타일이 globals.css에 몰려 있다.
- [ ] 색상값이 컴포넌트마다 하드코딩되어 있다.
- [ ] spacing 값이 화면마다 다르다.
- [ ] class 이름이 box, red, temp처럼 모호하다.
- [ ] CSS Module과 Plain CSS가 기준 없이 섞여 있다.
- [ ] 모바일 화면에서 가로 스크롤이 발생한다.
- [ ] focus outline이 제거되어 있다.
- [ ] !important가 자주 사용된다.
```

---

### [FAQ]

Q. Styling Architecture가 없으면 뭐가 문제야?
A. 스타일 중복, CSS 충돌, 색상 불일치, 반응형 깨짐, 유지보수 어려움이 생길 수 있다.

Q. 작은 프로젝트도 Styling Architecture가 필요해?
A. 간단한 기준은 필요하다. 다만 구조를 과하게 복잡하게 만들 필요는 없다.

Q. Styling Architecture는 디자인이랑 같은 뜻이야?
A. 아니다. 디자인 결과물이 아니라 스타일 코드와 구조를 관리하는 기준이다.

---

## 3.2 Styling Responsibility

### [개념]

Styling Responsibility는 스타일 책임을 전역, 토큰, 레이아웃, 컴포넌트, 유틸리티 단위로 나누는 기준이다.

권장 책임 분리:

```text
Reset / Base Style
→ Global Style

Color / Spacing / Font / Radius / Z-index
→ Design Token

Page Layout
→ Layout Style

Reusable UI
→ Component Style

One-off Adjustment
→ Utility or Local Style
```

---

### [핵심]

역할별 책임:

- Reset Style: 브라우저 기본 스타일 차이 감소
- Global Style: 앱 전체 기본 스타일 정의
- Token Style: 반복되는 디자인 값 정의
- Layout Style: 페이지 배치와 공간 구조 담당
- Component Style: 개별 UI 요소의 외형과 상태 담당
- Utility Style: 작은 재사용 보조 스타일 담당

---

### [실무]

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
│     ├─ Button.jsx
│     └─ Button.module.css
└─ pages/
   └─ MainPage/
      ├─ MainPage.jsx
      └─ MainPage.module.css
```

책임 분리 원칙:

```text
전역 기본값
→ styles/

재사용 컴포넌트 외형
→ components/{ComponentName}/

페이지 배치
→ pages/{PageName}/

디자인 값
→ styles/tokens.css

접근성 utility
→ styles/utilities.css
```

---

### [FAQ]

Q. reset, global, token 파일을 꼭 나눠야 해?
A. 프로젝트 규모에 따라 다르다. 다만 역할을 구분하면 유지보수와 리뷰가 쉬워진다.

Q. 페이지 스타일과 컴포넌트 스타일은 나눠야 해?
A. 권장된다. 페이지 레이아웃과 재사용 컴포넌트 스타일을 섞으면 재사용성이 떨어진다.

Q. 컴포넌트 스타일은 컴포넌트 옆에 두는 게 좋아?
A. 컴포넌트 전용 스타일이라면 가까이 두는 것이 추적과 유지보수에 좋다.

---

## 3.3 Styling Decision Flow

### [개념]

Styling Decision Flow는 Agent가 스타일 구조를 선택하거나 검토할 때 따르는 판단 순서다.

스타일링 방식은 취향이 아니라 프로젝트 조건에 따라 선택해야 한다.

판단 조건:

- 프로젝트 규모
- 팀 숙련도
- React 사용 여부
- 디자인 시스템 필요성
- theme 필요성
- 동적 스타일 비중
- 배포 환경
- 유지보수 기간
- 학습 목적 여부

---

### [핵심]

기본 선택 기준:

```text
소규모 학원 프로젝트
→ Plain CSS 또는 CSS Module

React 컴포넌트 단위 스타일
→ CSS Module

동적 스타일 / theme provider 필요
→ CSS-in-JS

빠른 UI 작성 / utility-first 선호
→ Tailwind CSS

기존 CSS 확장 / nesting 필요
→ SCSS
```

---

### [실무]

Agent Styling Method 판단 Flow:

```text
Project Type 확인
→ Existing Styling Method 확인
→ Team Skill 확인
→ Component Scope 필요 여부 확인
→ Theme / Dark Mode 필요 여부 확인
→ Dynamic Style 필요 여부 확인
→ Build Environment 확인
→ Styling Method 선택
→ File Structure 정의
→ Review Checklist 적용
```

선택 결과 예:

```text
학원 React 프로젝트 + CRA + 팀 CSS 숙련도 보통
→ CSS Module 권장

빠른 프로토타입 + 작은 규모
→ Plain CSS 가능

디자인 시스템 + theme + variant 많음
→ CSS-in-JS 또는 Tailwind + Component Variant 구조 고려

대규모 운영 서비스
→ Design Token + Component Style + Review Rule 필수
```

---

### [FAQ]

Q. 스타일링 방식은 프로젝트 중간에 바꿔도 돼?
A. 가능하지만 비용이 크다. 기존 방식과 신규 방식이 섞이면 유지보수가 어려워질 수 있다.

Q. 학원 프로젝트에서는 어떤 방식이 무난해?
A. Plain CSS 또는 CSS Module이 무난하다. React 컴포넌트 단위 관리가 필요하면 CSS Module이 좋다.

Q. Tailwind를 쓰면 모든 문제가 해결돼?
A. 아니다. Tailwind도 token, component extraction, class composition 기준이 필요하다.

---

# 4. Core Separation Rules

## 4.1 Global Style vs Component Style

### [개념]

Global Style은 애플리케이션 전체에 적용되는 기본 스타일이다.

Component Style은 특정 컴포넌트의 외형, 상태, 내부 구조에 적용되는 스타일이다.

두 책임을 섞으면 CSS 충돌과 유지보수 문제가 커진다.

---

### [핵심]

Global Style에 적합한 것:

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

Component Style에 적합한 것:

- Button variant
- Card style
- Modal style
- Form field style
- Component hover
- Component disabled
- Component error
- Component responsive

Global Style에 부적합한 것:

- 특정 Card 디자인
- 특정 Modal 디자인
- 특정 Page layout
- 특정 Button variant
- 특정 Form field spacing

---

### [실무]

좋은 분리 예:

```text
styles/globals.css
→ body, a, img, button 기본값

styles/tokens.css
→ color, spacing, radius, z-index variable

components/Button/Button.module.css
→ button variant, button state

pages/MainPage/MainPage.module.css
→ main page layout
```

검토 기준:

```md
- [ ] 전역 스타일이 너무 많은 책임을 갖지 않는가?
- [ ] 특정 컴포넌트 스타일이 global에 들어가지 않았는가?
- [ ] token은 component style보다 먼저 로드되는가?
- [ ] component style이 다른 컴포넌트를 직접 override하지 않는가?
```

---

### [FAQ]

Q. 모든 스타일을 globals.css에 넣어도 돼?
A. 권장하지 않는다. global에는 전체 기본 스타일만 두고 컴포넌트 스타일은 분리하는 것이 좋다.

Q. body에 font-family를 넣는 건 괜찮아?
A. 괜찮다. 전체 앱의 기본 폰트는 global style에서 관리하는 것이 일반적이다.

Q. Button 스타일을 globals.css에 넣어도 돼?
A. 공통 button reset 정도는 가능하지만 variant와 상태 스타일은 Button 컴포넌트 스타일로 분리하는 것이 좋다.

---

## 4.2 Layout Style vs Component Style

### [개념]

Layout Style은 요소들을 배치하는 스타일이다.

Component Style은 개별 UI 요소의 외형과 상태를 정의하는 스타일이다.

원칙:

```text
부모는 배치 담당
자식은 자기 외형 담당
```

---

### [핵심]

Layout Style:

- grid
- flex
- gap
- container width
- page spacing
- section spacing
- sidebar layout
- header layout

Component Style:

- button
- card
- input
- badge
- modal
- dropdown
- tab
- toast

---

### [실무]

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
  border-radius: var(--radius-lg);
}
```

Review 기준:

```md
- [ ] 재사용 컴포넌트가 외부 margin을 강제하지 않는가?
- [ ] page layout이 component 내부에 들어가지 않았는가?
- [ ] 부모 layout에서 gap을 관리하는가?
- [ ] 컴포넌트 내부 간격과 외부 배치 간격이 구분되는가?
```

---

### [FAQ]

Q. 컴포넌트가 자기 margin을 가지면 안 돼?
A. 항상 안 되는 것은 아니지만 재사용 컴포넌트라면 외부 배치는 부모가 담당하는 것이 좋다.

Q. layout과 component style을 왜 분리해?
A. 컴포넌트 재사용성과 화면 구조 변경의 유연성을 높이기 위해서다.

Q. gap과 margin 중 뭐가 좋아?
A. 반복 배치 간격은 부모 layout의 gap으로 관리하는 것이 예측하기 쉽다.

---

# 5. Part01 Quality Checklist

## 5.1 Styling Architecture Initial Checklist

### [개념]

Part01 단계에서는 Styling Architecture의 목적, 범위, 책임 분리, 기본 판단 Flow를 검토한다.

이 단계는 실제 CSS 코드 작성 전에 스타일 구조 기준을 고정하는 단계다.

---

### [핵심]

초기 체크리스트:

```md
## Purpose

- [ ] 이 문서가 사람용 CSS 학습 문서가 아니라 Agent용 RAG 문서인가?
- [ ] Frontend Agent / Review Agent / PM Agent 역할이 분리되어 있는가?
- [ ] 스타일 구조 설계 목적이 명확한가?

## Scope

- [ ] 포함 범위가 명확한가?
- [ ] 제외 범위가 명확한가?
- [ ] 다른 Frontend Domain Rules와 책임이 분리되어 있는가?

## Architecture Core

- [ ] Styling Architecture 정의가 명확한가?
- [ ] 스타일 책임 분리 기준이 있는가?
- [ ] Global Style과 Component Style이 분리되어 있는가?
- [ ] Layout Style과 Component Style이 분리되어 있는가?

## Agent Retrieval

- [ ] FAQ가 충분한가?
- [ ] 검색 가능한 키워드가 포함되어 있는가?
- [ ] Flow가 포함되어 있는가?
- [ ] Retrieval Queries가 포함되어 있는가?
```

---

### [실무]

Part01 승인 기준:

```text
Purpose 명확
+ Scope 명확
+ Responsibility 명확
+ Agent Role 명확
+ FAQ 충분
+ Retrieval Queries 포함
→ Part01 승인 가능
```

Part01 보류 기준:

```text
CSS 기초 설명 과다
또는 사람용 문서처럼 장문 서술
또는 Agent 역할 불명확
또는 Scope 중복
또는 FAQ 부족
→ 재작성 필요
```

---

### [FAQ]

Q. Part01에서 실제 CSS 코드를 많이 넣어야 해?
A. 아니다. Part01은 목적, 범위, 책임 분리, 판단 Flow를 고정하는 단계다.

Q. Part01의 핵심 검수 기준은 뭐야?
A. Agent가 스타일 구조를 판단할 수 있도록 목적, 범위, 책임, Flow가 명확한지다.

Q. Part01에서 가장 위험한 문제는 뭐야?
A. CSS 기초 학습 문서처럼 변하거나 다른 Frontend Domain Rules와 범위가 중복되는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Styling Architecture 문서는 왜 필요해?
A. Frontend Agent, Review Agent, PM Agent가 스타일 구조, CSS 관리 방식, 디자인 토큰, 반응형, 테마, 접근성 스타일을 일관되게 판단하기 위해 필요하다.

Q. Styling Architecture가 뭐야?
A. 프로젝트에서 스타일을 어디에, 어떤 기준으로, 어떤 도구로 작성하고 관리할지 정하는 구조다.

Q. Styling Architecture 문서는 사람용 학습 문서야?
A. 아니다. Agent Retrieval, 스타일 코드 생성, 리뷰, UI 품질 판단을 위한 RAG 최적화 문서다.

Q. Styling Architecture의 핵심 기준은 뭐야?
A. 스타일 책임 분리, token 관리, CSS 충돌 방지, 반응형, 접근성, 유지보수성이다.

Q. Frontend Agent는 Styling Architecture를 어떻게 사용해?
A. 프로젝트 스타일링 방식과 token 체계를 확인한 뒤 component style, responsive style, state style을 생성한다.

Q. Review Agent는 Styling Architecture에서 뭘 검토해?
A. styling method 일관성, global/component 분리, token 사용, 반응형, 접근성, 중복, 충돌 가능성을 검토한다.

Q. PM Agent는 Styling Architecture에서 뭘 판단해?
A. 요구사항 충족, UI 일관성, 모바일 대응, 사용자 흐름, 스타일 이슈의 blocker 여부를 판단한다.

Q. Styling Architecture와 Design System은 뭐가 달라?
A. Styling Architecture는 스타일 코드 구조와 관리 방식이고, Design System은 UI 규격과 컴포넌트 체계까지 포함한다.

Q. Styling Architecture의 Included Scope는 뭐야?
A. Global Style, Component Style, Design Token, CSS Module, CSS-in-JS, Tailwind, Responsive Styling, Theme, Accessibility Style, Troubleshooting이다.

Q. Styling Architecture의 Excluded Scope는 뭐야?
A. HTML/CSS 기초 문법 전체, React Core 문법, Framer Motion 심화, Canvas/WebGL, Design System 전체 명세, Next.js 전용 전략이다.

Q. CSS 기본 문법은 어느 문서에서 다뤄?
A. HTML CSS Foundation 문서에서 다룬다.

Q. React 컴포넌트 구조는 어느 문서에서 다뤄?
A. React Component Design 문서에서 다룬다.

Q. 접근성 세부 기준은 어느 문서에서 다뤄?
A. Frontend Accessibility 문서에서 다룬다.

Q. Styling Architecture가 없으면 뭐가 문제야?
A. CSS 충돌, 중복 스타일, 색상 불일치, 반응형 깨짐, 유지보수 어려움이 생길 수 있다.

Q. 작은 프로젝트도 Styling Architecture가 필요해?
A. 간단한 기준은 필요하다. 다만 구조를 과하게 복잡하게 만들 필요는 없다.

Q. Styling Responsibility가 뭐야?
A. 스타일 책임을 reset, global, token, layout, component, utility 단위로 나누는 기준이다.

Q. Reset Style의 책임은 뭐야?
A. 브라우저 기본 스타일 차이를 줄이고 프로젝트 스타일 기준을 통일하는 것이다.

Q. Global Style의 책임은 뭐야?
A. 앱 전체 기본 스타일과 CSS variable 같은 전역 기준을 관리하는 것이다.

Q. Design Token의 책임은 뭐야?
A. 색상, 간격, 폰트, radius, z-index 같은 반복 디자인 값을 이름으로 관리하는 것이다.

Q. Layout Style의 책임은 뭐야?
A. 페이지 배치, grid, flex, gap, container width 같은 공간 구조를 담당한다.

Q. Component Style의 책임은 뭐야?
A. 버튼, 카드, 입력창 같은 개별 UI 요소의 외형과 상태를 담당한다.

Q. Utility Style의 책임은 뭐야?
A. sr-only, container, flex-center 같은 작은 재사용 보조 스타일을 담당한다.

Q. 전역 스타일과 컴포넌트 스타일은 왜 분리해야 해?
A. CSS 충돌을 줄이고 컴포넌트 재사용성과 유지보수성을 높이기 위해서다.

Q. Global Style에 넣기 좋은 것은 뭐야?
A. reset, body 기본 스타일, font-family, background, text color, CSS variables, image 기본 스타일이다.

Q. Global Style에 넣으면 안 되는 것은 뭐야?
A. 특정 Card, Modal, Button variant, Page layout 같은 컴포넌트 전용 스타일은 넣지 않는 것이 좋다.

Q. 모든 스타일을 globals.css에 넣어도 돼?
A. 권장하지 않는다. global에는 전체 기본 스타일만 두고 컴포넌트 스타일은 분리하는 것이 좋다.

Q. Layout Style과 Component Style 차이는 뭐야?
A. Layout Style은 배치와 공간 구조를 담당하고 Component Style은 개별 UI 요소의 외형과 상태를 담당한다.

Q. 부모와 자식 스타일 책임 원칙은 뭐야?
A. 부모는 배치를 담당하고 자식은 자기 외형을 담당하는 것이다.

Q. 컴포넌트가 자기 margin을 가져도 돼?
A. 항상 안 되는 것은 아니지만 재사용 컴포넌트라면 외부 배치는 부모가 담당하는 것이 좋다.

Q. 스타일링 방식은 어떻게 선택해?
A. 프로젝트 규모, 팀 숙련도, React 사용 여부, theme 필요성, 동적 스타일 비중, 유지보수 기간을 기준으로 선택한다.

Q. 학원 React 프로젝트에서는 어떤 스타일링 방식이 무난해?
A. Plain CSS 또는 CSS Module이 무난하며, 컴포넌트 단위 관리가 필요하면 CSS Module이 좋다.

Q. CSS Module은 언제 적합해?
A. React 컴포넌트 단위 스타일을 안전하게 관리하고 class 충돌을 줄이고 싶을 때 적합하다.

Q. CSS-in-JS는 언제 적합해?
A. 동적 스타일, theme provider, 디자인 시스템 컴포넌트 구현이 중요한 경우 적합하다.

Q. Tailwind CSS는 언제 적합해?
A. 빠른 UI 작성, utility-first 방식, design scale 강제, 컴포넌트 기반 개발이 필요할 때 적합하다.

Q. SCSS는 언제 적합해?
A. 기존 CSS를 구조화하고 nesting, mixin, partial 파일 분리가 필요한 경우 적합하다.

Q. 스타일링 방식을 여러 개 섞어도 돼?
A. 가능하지만 명확한 기준 없이 섞으면 유지보수가 어려워진다.

Q. Part01의 핵심 목적은 뭐야?
A. Styling Architecture의 목적, 범위, Agent 역할, 스타일 책임 분리, 기본 판단 Flow를 고정하는 것이다.

Q. Part01에서 실제 CSS 코드를 많이 넣어야 해?
A. 아니다. Part01은 구조 기준을 정하는 단계이며 실제 세부 코드는 이후 Part에서 다룬다.

Q. Part01 승인 기준은 뭐야?
A. Purpose, Scope, Responsibility, Agent Role, Flow, FAQ, Retrieval Queries가 명확하면 승인 가능하다.

Q. Part01에서 가장 위험한 문제는 뭐야?
A. CSS 기초 학습 문서처럼 변하거나 다른 Frontend Domain Rules와 범위가 중복되는 것이다.
