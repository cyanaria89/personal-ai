# Design System Foundation Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

Design System Foundation Domain Rules 문서는 Frontend Agent / Review Agent / PM Agent가 프론트엔드 프로젝트에서 **UI 일관성, 디자인 토큰, 컴포넌트 규격, 패턴, 접근성, 반응형, 테마, 문서화 기준**을 판단하기 위한 RAG Retrieval 최적화 문서이다.

이 문서는 사람 공부용 디자인 이론 문서가 아니라, Agent가 실제 프로젝트에서 UI를 생성하고 검토할 때 사용하는 **Design System 판단 기준 문서**이다.

목적:

- Design System 개념과 범위 정의
- Design Token 체계 설계
- Component Specification 기준 제공
- Variant / Size / State 규칙 정의
- UI Pattern 일관성 유지
- Accessibility 기준 반영
- Responsive 기준 반영
- Theme / Dark Mode 확장 기준 제공
- Frontend Agent의 UI 생성 기준 제공
- Review Agent의 UI 품질 검토 기준 제공
- PM Agent의 화면 완료 판단 기준 제공
- Agent 간 UI 언어 통일

---

### [핵심]

Design System의 핵심 기준:

1. 디자인 값이 Token으로 관리되는가?
2. 공통 UI 컴포넌트 규격이 정의되어 있는가?
3. Button / Input / Card / Modal / Form 등 핵심 컴포넌트가 일관적인가?
4. Variant / Size / State 체계가 명확한가?
5. 접근성 기준이 기본 포함되어 있는가?
6. 반응형 기준이 정의되어 있는가?
7. UI Pattern이 재사용 가능한가?
8. Theme / Dark Mode 확장이 가능한가?
9. Frontend 코드와 디자인 규칙이 연결되는가?
10. Review Agent가 승인 / 반려 기준으로 사용할 수 있는가?

---

### [실무]

Design System은 단순히 예쁜 UI 모음이 아니다.

실무에서는 다음 역할을 한다.

```text
Design Decision
→ Design Token
→ Component Spec
→ Component Implementation
→ UI Pattern
→ Page Composition
→ Review Checklist
→ Product Consistency
```

Frontend Agent는 화면을 만들기 전에 Design System 기준을 우선 확인해야 한다.

Review Agent는 코드가 Design System 기준을 따르는지 검토해야 한다.

PM Agent는 화면이 요구사항과 디자인 기준을 만족하는지 판단해야 한다.

---

### [FAQ]

Q. Design System 문서는 사람 공부용이야?

A.
아니다. Frontend Agent / Review Agent / PM Agent가 UI를 일관되게 생성하고 검토하기 위한 RAG 문서다.

Q. Design System은 CSS Architecture랑 뭐가 달라?

A.
CSS Architecture는 스타일 코드 구조이고, Design System은 디자인 토큰, 컴포넌트 규격, UI 패턴, 사용 기준까지 포함한다.

Q. 작은 프로젝트에도 Design System이 필요해?

A.
거대한 시스템은 필요 없지만 Button, Input, Card, Color, Spacing 정도의 미니 Design System은 유지보수에 도움이 된다.

Q. Design System의 핵심은 뭐야?

A.
UI를 매번 새로 만드는 것이 아니라, 정해진 규칙과 컴포넌트를 재사용해 일관성을 유지하는 것이다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Design System 문서는 프론트엔드 UI 일관성과 재사용성을 위해 필요한 범위를 포함한다.

포함 범위:

- Design System 개념
- Design Principles
- Design Token
- Color Token
- Typography Token
- Spacing Token
- Radius Token
- Shadow Token
- Z-index Token
- Breakpoint Token
- Component Specification
- Button
- Input
- Select
- Checkbox
- Radio
- Textarea
- Form Field
- Card
- Badge
- Tag
- Alert
- Toast
- Modal
- Dialog
- Drawer
- Tabs
- Pagination
- Table
- Empty State
- Loading State
- Error State
- Navigation
- Layout
- Theme
- Dark Mode
- Accessibility
- Responsive Design
- Component Variant
- Component Size
- Component State
- Documentation
- Review Checklist

---

### [핵심]

반드시 포함:

- Design Token 체계
- Component Spec 작성 방식
- Component Variant 규칙
- Component State 규칙
- Accessibility 기준
- Responsive 기준
- UI Pattern 기준
- Frontend 구현 연결
- Review Agent 검토 기준
- PM Agent 완료 판단 기준
- Retrieval Queries

---

### [실무]

Design System은 다음 Domain Rules와 연결된다.

```text
HTML CSS Foundation
→ React Component Design
→ UI Component Pattern
→ Frontend Accessibility
→ Styling Architecture
→ Design System
→ Frontend Code Review
```

Design System은 Frontend Agent가 화면을 만들 때 마지막 품질 기준으로 작동한다.

---

### [FAQ]

Q. Design System 문서에 모든 컴포넌트를 다 넣어야 해?

A.
아니다. 프로젝트에서 자주 쓰는 핵심 컴포넌트부터 정의하는 것이 좋다.

Q. 디자인 토큰만 있으면 Design System이야?

A.
아니다. 토큰은 기초이고, 컴포넌트 규격과 사용 패턴까지 있어야 Design System에 가까워진다.

Q. UI Component Pattern 문서와 겹치지 않아?

A.
UI Component Pattern은 패턴 중심이고, Design System은 토큰, 규격, 상태, 변형, 리뷰 기준까지 포함한다.

---

## 2.2 Excluded Scope

### [개념]

Design System 문서는 Level 3 Frontend Foundation 범위에서 실무적인 UI 기준을 제공한다.

제외 범위:

- Figma 운영 심화
- Design Ops 심화
- Brand Identity 전체 전략
- Motion Design System 심화
- Advanced Animation Library
- Micro Interaction 심화
- Enterprise Design Governance
- Multi-brand Design System
- Token Build Pipeline 심화
- Style Dictionary 심화
- Monorepo Package Publishing 심화
- Storybook Addon 심화
- Native App Design System
- Advanced Visual Regression Testing

---

### [핵심]

제외 이유:

- Frontend Foundation 범위 초과
- Styling Architecture 문서와 역할 분리
- Frontend Expert 단계에서 다룰 내용과 분리
- Retrieval 혼선 방지
- Chunk 품질 유지

---

### [실무]

다른 문서로 위임하는 경우:

```text
스타일 파일 구조
→ Styling Architecture

컴포넌트 코드 설계
→ React Component Design

컴포넌트 패턴
→ UI Component Pattern

접근성 상세 기준
→ Frontend Accessibility

테스트 상세 기준
→ Frontend Testing

배포 / 빌드
→ Frontend Build Deploy
```

---

### [FAQ]

Q. Storybook도 여기서 자세히 다뤄?

A.
기초 문서화와 컴포넌트 예시 수준은 포함할 수 있지만 Storybook 심화 운영은 제외한다.

Q. Figma 디자인 시스템도 여기서 다뤄?

A.
프론트엔드 구현에 필요한 연결 기준은 포함하지만 Figma 운영 심화는 제외한다.

---

# 3. Design System Core

## 3.1 Design System Definition

### [개념]

Design System은 제품 UI를 일관되게 만들기 위한 **디자인 원칙, 디자인 토큰, 컴포넌트, 패턴, 문서화, 사용 규칙**의 집합이다.

---

### [핵심]

Design System 구성 요소:

- Design Principles
- Design Tokens
- Component Library
- UI Patterns
- Accessibility Rules
- Responsive Rules
- Content Rules
- Theme Rules
- Documentation
- Review Checklist

---

### [실무]

Design System은 다음 질문에 답할 수 있어야 한다.

```md
- [ ] Primary Button은 언제 사용하는가?
- [ ] Error 색상은 무엇인가?
- [ ] Card padding은 얼마인가?
- [ ] Form validation error는 어떻게 표시하는가?
- [ ] Modal은 어떻게 닫히는가?
- [ ] 모바일에서 Table은 어떻게 처리하는가?
- [ ] Loading State는 어떤 컴포넌트를 쓰는가?
- [ ] Empty State 문구는 어떤 형식인가?
- [ ] Disabled 상태는 어떻게 표현하는가?
- [ ] Focus Style은 어떻게 표시하는가?
```

---

### [FAQ]

Q. Design System은 컴포넌트 라이브러리랑 같아?

A.
아니다. 컴포넌트 라이브러리는 Design System의 일부다. Design System은 토큰, 규칙, 패턴, 사용 기준까지 포함한다.

Q. Design System이 있으면 개발이 빨라져?

A.
초기 구축 비용은 있지만 반복 UI 개발과 리뷰 기준이 명확해져 장기적으로 빨라진다.

---

## 3.2 Design Principles

### [개념]

Design Principles는 UI를 만들 때 지켜야 할 상위 원칙이다.

예:

- Consistency
- Clarity
- Accessibility
- Efficiency
- Feedback
- Responsiveness
- Maintainability

---

### [핵심]

권장 Design Principles:

```text
Consistency
→ 같은 의미의 UI는 같은 방식으로 표현한다.

Clarity
→ 사용자가 현재 상태와 다음 행동을 명확히 알 수 있어야 한다.

Accessibility
→ 키보드, 스크린 리더, 색각 다양성 사용자를 고려한다.

Feedback
→ 사용자 행동에 대한 loading, success, error 피드백을 제공한다.

Scalability
→ UI가 늘어나도 토큰과 컴포넌트 규칙으로 확장 가능해야 한다.
```

---

### [실무]

Agent가 UI를 생성할 때 우선순위:

```text
요구사항 충족
→ 사용성
→ 접근성
→ 일관성
→ 재사용성
→ 시각적 완성도
```

---

### [FAQ]

Q. Design Principles가 꼭 필요해?

A.
필요하다. 컴포넌트 규칙만 있으면 상황별 판단이 어려우므로 상위 원칙이 필요하다.

Q. 예쁜 UI가 가장 중요한가?

A.
아니다. 사용성, 접근성, 일관성, 요구사항 충족이 먼저다.

---

# 4. Design Token Rules

## 4.1 Design Token Overview

### [개념]

Design Token은 디자인 값을 코드에서 재사용 가능한 이름으로 관리하는 방식이다.

Design Token은 Design System의 가장 기본 단위다.

---

### [핵심]

Token 종류:

- Color Token
- Typography Token
- Spacing Token
- Radius Token
- Shadow Token
- Z-index Token
- Breakpoint Token
- Motion Token
- Size Token
- Opacity Token

---

### [예제]

```css
:root {
  --color-primary: #2563eb;
  --color-error: #dc2626;
  --color-text: #111827;
  --color-background: #ffffff;

  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-4: 16px;
  --spacing-6: 24px;

  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
}
```

---

### [실무]

Design Token 사용 Flow:

```text
Raw Value
→ Token Name
→ Semantic Meaning
→ Component Style
→ Theme Extension
```

나쁜 예:

```css
.button {
  background: #2563eb;
  padding: 13px 21px;
}
```

좋은 예:

```css
.button {
  background: var(--color-primary);
  padding: var(--spacing-2) var(--spacing-4);
}
```

---

### [FAQ]

Q. Design Token은 왜 필요해?

A.
디자인 값을 일관되게 관리하고 변경 시 전체 UI에 안정적으로 반영하기 위해 필요하다.

Q. 모든 값을 token으로 만들어야 해?

A.
아니다. 반복 사용되거나 의미 있는 값부터 token으로 관리한다.

Q. Token 이름은 색상값 기준이 좋아, 의미 기준이 좋아?

A.
컴포넌트에서는 의미 기준 token을 사용하는 것이 좋다. 예: `--color-primary`, `--color-error`.

---

## 4.2 Token Naming Rules

### [개념]

Token Naming은 디자인 값을 일관되게 이름 붙이는 규칙이다.

---

### [핵심]

권장 naming 구조:

```text
--category-role-state
--category-scale
--component-property-state
```

예:

```text
--color-primary
--color-primary-hover
--color-text-muted
--spacing-4
--radius-card
--z-modal
--shadow-card
```

---

### [Best Practice]

좋은 token 이름:

```text
--color-error
--color-surface
--color-border
--spacing-md
--font-size-lg
--radius-button
```

나쁜 token 이름:

```text
--blue
--red1
--big-space
--nice-shadow
--temp-color
```

---

### [실무]

Token naming 기준:

```md
- [ ] 역할이 드러나는가?
- [ ] 프로젝트 전체에서 일관적인가?
- [ ] theme 변경에 안전한가?
- [ ] 컴포넌트에서 raw value를 숨길 수 있는가?
- [ ] 너무 구체적인 화면 이름에 묶이지 않는가?
```

---

### [FAQ]

Q. `--blue-500` 같은 token은 쓰면 안 돼?

A.
쓸 수 있다. 다만 컴포넌트에서는 `--color-primary` 같은 semantic token을 우선 사용하는 것이 좋다.

Q. token 이름에 컴포넌트 이름을 넣어도 돼?

A.
특정 컴포넌트 전용 token이면 가능하다. 예: `--button-height-md`.

---

## 4.3 Primitive Token vs Semantic Token

### [개념]

Primitive Token은 원시 디자인 값이고, Semantic Token은 의미를 가진 디자인 값이다.

---

### [Comparison]

| 구분          | Primitive Token  | Semantic Token    |
| ------------- | ---------------- | ----------------- |
| 의미          | 원시 값          | 역할 의미         |
| 예시          | `--blue-600`     | `--color-primary` |
| 변경 기준     | 색상 팔레트      | UI 역할           |
| 컴포넌트 사용 | 제한적           | 권장              |
| 테마 대응     | 직접 대응 어려움 | 쉬움              |

---

### [예제]

```css
:root {
  --blue-600: #2563eb;
  --red-600: #dc2626;

  --color-primary: var(--blue-600);
  --color-error: var(--red-600);
}
```

---

### [실무]

권장 Flow:

```text
Primitive Token
→ Semantic Token
→ Component Token
→ Component Style
```

예:

```text
--blue-600
→ --color-primary
→ --button-primary-background
→ Button style
```

---

### [FAQ]

Q. Primitive Token만 쓰면 안 돼?

A.
가능하지만 theme 변경과 의미 기반 관리가 어려워진다.

Q. Semantic Token은 왜 좋아?

A.
색상 값이 바뀌어도 컴포넌트는 역할 이름을 유지할 수 있어서 확장에 유리하다.

---

## 4.4 Color Token Rules

### [개념]

Color Token은 UI 색상을 역할과 상태에 따라 관리하는 token이다.

---

### [핵심]

필수 Color Token:

```text
--color-primary
--color-primary-hover
--color-primary-active
--color-background
--color-surface
--color-text
--color-text-muted
--color-border
--color-error
--color-warning
--color-success
--color-info
--color-disabled
--color-focus-ring
```

---

### [예제]

```css
:root {
  --color-primary: #2563eb;
  --color-primary-hover: #1d4ed8;
  --color-primary-active: #1e40af;

  --color-background: #ffffff;
  --color-surface: #f9fafb;
  --color-text: #111827;
  --color-text-muted: #6b7280;
  --color-border: #e5e7eb;

  --color-error: #dc2626;
  --color-warning: #f59e0b;
  --color-success: #16a34a;
  --color-info: #0284c7;

  --color-disabled: #d1d5db;
  --color-focus-ring: #2563eb;
}
```

---

### [실무]

Color Token Review:

```md
- [ ] 상태 색상이 semantic token으로 분리되어 있는가?
- [ ] hover / active 색상이 정의되어 있는가?
- [ ] text / muted / border / surface가 구분되어 있는가?
- [ ] error를 색상만으로 전달하지 않는가?
- [ ] dark mode 대응 가능성이 있는가?
```

---

### [FAQ]

Q. Error 색상은 그냥 red로 쓰면 안 돼?

A.
가능하지만 `--color-error`로 관리하는 것이 의미와 일관성에 좋다.

Q. Text color와 muted color를 나눠야 해?

A.
권장된다. 본문 텍스트와 보조 텍스트의 계층을 명확히 관리할 수 있다.

---

## 4.5 Spacing Token Rules

### [개념]

Spacing Token은 margin, padding, gap에 사용하는 간격 값을 일정한 scale로 관리하는 token이다.

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
  --spacing-16: 64px;
}
```

---

### [실무]

Spacing 사용 기준:

```text
Component 내부 간격
→ padding / gap

Component 외부 배치
→ parent layout gap

Page section 간격
→ layout token

Form field 간격
→ form pattern token
```

---

### [주의]

피해야 할 방식:

```css
.card {
  padding: 17px;
  margin-bottom: 23px;
}
```

권장 방식:

```css
.card {
  padding: var(--spacing-4);
}

.card-list {
  display: grid;
  gap: var(--spacing-6);
}
```

---

### [FAQ]

Q. spacing token은 왜 필요해?

A.
화면마다 간격이 제각각이 되는 것을 막고 UI 리듬을 유지하기 위해 필요하다.

Q. margin과 gap 중 뭐가 좋아?

A.
리스트나 레이아웃 요소 사이 간격은 gap이 더 명확한 경우가 많다. 개별 컴포넌트 외부 margin은 남용하지 않는 것이 좋다.

---

## 4.6 Typography Token Rules

### [개념]

Typography Token은 글자의 크기, 굵기, 줄 간격, 폰트 패밀리를 관리하는 token이다.

---

### [핵심]

필수 Typography Token:

```text
--font-family-base
--font-size-xs
--font-size-sm
--font-size-md
--font-size-lg
--font-size-xl
--font-size-2xl
--font-weight-regular
--font-weight-medium
--font-weight-bold
--line-height-tight
--line-height-base
--line-height-relaxed
```

---

### [예제]

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

Typography hierarchy 예:

```text
Page Title
→ font-size-3xl / bold / tight

Section Title
→ font-size-2xl / bold / tight

Card Title
→ font-size-lg / bold / base

Body
→ font-size-md / regular / base

Caption
→ font-size-sm / regular / base
```

---

### [FAQ]

Q. font-size를 px로 직접 쓰면 안 돼?

A.
가능하지만 token과 rem 단위를 사용하면 접근성과 일관성에 더 좋다.

Q. heading tag와 typography style은 같아야 해?

A.
의미 구조는 heading tag가 담당하고, 시각 스타일은 typography token으로 관리한다.

---

## 4.7 Radius Shadow Z-index Token Rules

### [개념]

Radius, Shadow, Z-index Token은 UI의 형태, 깊이, 겹침 순서를 관리하는 token이다.

---

### [핵심]

권장 token:

```css
:root {
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;

  --shadow-sm: 0 1px 2px rgb(0 0 0 / 0.08);
  --shadow-md: 0 4px 12px rgb(0 0 0 / 0.12);
  --shadow-lg: 0 12px 24px rgb(0 0 0 / 0.16);

  --z-base: 0;
  --z-dropdown: 100;
  --z-header: 300;
  --z-overlay: 900;
  --z-modal: 1000;
  --z-toast: 1100;
}
```

---

### [실무]

사용 기준:

```text
Button
→ radius-md

Card
→ radius-lg + shadow-sm

Modal
→ radius-lg + shadow-lg + z-modal

Toast
→ shadow-md + z-toast
```

---

### [FAQ]

Q. z-index는 그냥 9999로 쓰면 안 돼?

A.
권장하지 않는다. token scale로 관리해야 modal, toast, dropdown 순서가 예측 가능하다.

Q. shadow는 많이 쓰면 좋아?

A.
아니다. depth 표현이 필요한 곳에 제한적으로 사용해야 UI가 복잡해지지 않는다.

---

## 4.8 Motion Token Rules

### [개념]

Motion Token은 transition duration, easing, animation timing을 관리하는 token이다.

---

### [핵심]

권장 token:

```css
:root {
  --duration-fast: 150ms;
  --duration-base: 250ms;
  --duration-slow: 400ms;

  --easing-standard: ease;
  --easing-emphasized: cubic-bezier(0.2, 0, 0, 1);
}
```

---

### [실무]

사용 예:

```css
.button {
  transition:
    background-color var(--duration-fast) var(--easing-standard),
    transform var(--duration-fast) var(--easing-standard);
}
```

Motion Review:

```md
- [ ] transition duration이 일관적인가?
- [ ] motion이 사용성을 돕는가?
- [ ] prefers-reduced-motion을 고려했는가?
- [ ] 과도한 animation이 없는가?
```

---

### [FAQ]

Q. Motion Token도 필요해?

A.
반복되는 transition과 animation이 있다면 필요하다. 일관된 사용감을 만들 수 있다.

Q. 애니메이션은 많을수록 좋아?

A.
아니다. 사용성을 돕는 수준으로 제한해야 한다.

---

# 5. Component Specification Rules

## 5.1 Component Spec Definition

### [개념]

Component Specification은 공통 UI 컴포넌트의 목적, props, variant, size, state, accessibility, 사용 예시를 정의한 규격이다.

---

### [핵심]

Component Spec 필수 항목:

```md
## Component Name

### Purpose

### Props

### Variants

### Sizes

### States

### Accessibility

### Usage

### Do

### Don't
```

---

### [예제]

Button Spec 기본 구조:

```md
# Button

## Purpose

사용자의 주요 행동을 실행한다.

## Variants

- primary
- secondary
- danger
- ghost

## Sizes

- sm
- md
- lg

## States

- default
- hover
- active
- focus
- disabled
- loading
```

---

### [실무]

Component Spec은 코드 생성 기준이 되어야 한다.

Frontend Agent는 Spec에 없는 variant를 임의로 만들지 않아야 한다.

Review Agent는 코드가 Spec과 다른 variant, size, state를 만들었는지 검토해야 한다.

---

### [FAQ]

Q. Component Spec은 왜 필요해?

A.
Agent와 개발자가 같은 컴포넌트를 같은 방식으로 사용하기 위해 필요하다.

Q. Spec에 없는 variant를 만들어도 돼?

A.
필요하면 가능하지만 먼저 기존 variant로 해결 가능한지 확인하고, 추가 이유를 명확히 해야 한다.

---

## 5.2 Component API Rules

### [개념]

Component API는 컴포넌트를 사용하는 props와 event handler의 규칙이다.

---

### [핵심]

Component API 기준:

- props 이름은 역할 중심
- boolean props는 의미 명확
- variant와 size는 제한된 값 사용
- event handler는 `on` prefix 사용
- children 사용 가능성 검토
- 불필요한 style override props 남용 금지
- className override 정책 명확화

---

### [예제]

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "danger" | "ghost";
  size?: "sm" | "md" | "lg";
  isLoading?: boolean;
  disabled?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
};
```

---

### [실무]

좋은 API:

```jsx
<Button variant="primary" size="md" onClick={handleSave}>
  저장
</Button>
```

나쁜 API:

```jsx
<Button blue big flag fn={save}>
  저장
</Button>
```

---

### [FAQ]

Q. component props 이름은 어떻게 지어야 해?

A.
역할과 의미가 명확해야 한다. `variant`, `size`, `isLoading`, `onClick`처럼 예측 가능한 이름이 좋다.

Q. className prop을 열어둬도 돼?

A.
가능하지만 override 범위를 명확히 해야 한다. 모든 스타일을 외부에서 덮게 하면 일관성이 깨질 수 있다.

---

## 5.3 Variant Rules

### [개념]

Variant는 같은 컴포넌트가 목적에 따라 다른 시각적 의미를 갖도록 하는 체계다.

---

### [핵심]

Variant 이름은 색상 기준이 아니라 의미 기준으로 작성한다.

권장:

```text
primary
secondary
tertiary
danger
success
warning
ghost
outline
```

비권장:

```text
blue
red
bigBlue
grayBox
```

---

### [실무]

Button variant 기준:

```text
primary
→ 가장 중요한 주요 행동

secondary
→ 보조 행동

danger
→ 삭제 / 취소 / 위험 행동

ghost
→ 낮은 강조의 보조 행동
```

---

### [FAQ]

Q. variant를 색상 이름으로 만들면 안 돼?

A.
권장하지 않는다. 색상은 바뀔 수 있으므로 역할 중심 이름이 좋다.

Q. danger variant는 언제 써?

A.
삭제, 탈퇴, 되돌릴 수 없는 위험 행동에 사용한다.

---

## 5.4 Size Rules

### [개념]

Size는 컴포넌트의 크기 체계다.

---

### [핵심]

권장 size:

```text
sm
md
lg
```

필요 시:

```text
xs
xl
```

---

### [예제]

Button size 기준:

```css
.buttonSm {
  height: 32px;
  padding: 0 var(--spacing-3);
  font-size: var(--font-size-sm);
}

.buttonMd {
  height: 40px;
  padding: 0 var(--spacing-4);
  font-size: var(--font-size-md);
}

.buttonLg {
  height: 48px;
  padding: 0 var(--spacing-6);
  font-size: var(--font-size-lg);
}
```

---

### [실무]

Size Review:

```md
- [ ] size 이름이 일관적인가?
- [ ] height / padding / font-size가 함께 정의되는가?
- [ ] 터치 영역이 충분한가?
- [ ] sm / md / lg 외 임의 크기가 남발되지 않는가?
```

---

### [FAQ]

Q. Button 크기를 매번 직접 지정해도 돼?

A.
권장하지 않는다. size prop과 token으로 관리하는 것이 일관성에 좋다.

Q. 모바일에서 버튼 높이는 중요해?

A.
중요하다. 터치 가능한 충분한 영역을 제공해야 한다.

---

## 5.5 State Rules

### [개념]

State는 컴포넌트가 현재 어떤 상태인지 표현하는 규칙이다.

---

### [핵심]

필수 상태:

```text
default
hover
active
focus
disabled
loading
error
success
selected
checked
open
```

컴포넌트별 필수 상태:

| Component | Required States                                  |
| --------- | ------------------------------------------------ |
| Button    | default, hover, active, focus, disabled, loading |
| Input     | default, focus, disabled, error, success         |
| Modal     | open, closed, focus                              |
| Tab       | default, hover, selected, focus                  |
| Toast     | info, success, warning, error                    |
| Checkbox  | unchecked, checked, disabled, focus              |

---

### [실무]

State는 시각 스타일과 동작이 함께 정의되어야 한다.

예:

```text
Button loading
→ spinner 표시
→ text 유지 또는 loading text
→ disabled 처리
→ 중복 클릭 방지
```

---

### [FAQ]

Q. hover만 있으면 상태 정의가 충분해?

A.
아니다. focus, disabled, loading, error 같은 상태도 필요하다.

Q. loading 상태는 왜 필요해?

A.
사용자의 중복 클릭을 막고 처리 중임을 알리기 위해 필요하다.

---

# 6. Core Component Rules

## 6.1 Button Component

### [개념]

Button은 사용자의 행동을 실행하는 가장 기본적인 interactive component다.

---

### [핵심]

Button Spec:

```text
Purpose
→ 사용자 행동 실행

Variants
→ primary, secondary, danger, ghost

Sizes
→ sm, md, lg

States
→ default, hover, active, focus, disabled, loading
```

---

### [예제]

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "danger" | "ghost";
  size?: "sm" | "md" | "lg";
  isLoading?: boolean;
  disabled?: boolean;
  type?: "button" | "submit" | "reset";
  children: React.ReactNode;
  onClick?: () => void;
};
```

사용 예:

```jsx
<Button variant="primary" type="submit" isLoading={isSubmitting}>
  저장
</Button>

<Button variant="danger" onClick={handleDelete}>
  삭제
</Button>
```

---

### [Best Practice]

Button 기준:

```md
- [ ] 기본 type은 `button`으로 설정한다.
- [ ] form submit에는 명시적으로 `type="submit"`을 사용한다.
- [ ] loading 중에는 중복 클릭을 방지한다.
- [ ] danger variant는 위험 행동에만 사용한다.
- [ ] focus-visible 스타일을 제공한다.
- [ ] icon button에는 accessible name을 제공한다.
```

---

### [FAQ]

Q. Button의 기본 type은 뭐가 좋아?

A.
일반 Button 컴포넌트는 `button`을 기본값으로 두는 것이 안전하다. form 제출 시에만 `submit`을 명시한다.

Q. loading button은 disabled 처리해야 해?

A.
대부분 그렇다. 중복 제출과 중복 API 요청을 막기 위해 필요하다.

Q. 아이콘만 있는 버튼은 어떻게 접근성 처리해?

A.
`aria-label` 또는 스크린 리더용 텍스트를 제공해야 한다.

---

## 6.2 Input Component

### [개념]

Input은 사용자의 텍스트 입력을 받는 component다.

---

### [핵심]

Input Spec:

```text
Types
→ text, email, password, number, search

States
→ default, focus, disabled, readonly, error, success

Required
→ label, name, value, onChange, errorMessage
```

---

### [예제]

```tsx
type TextInputProps = {
  id: string;
  name: string;
  label: string;
  value: string;
  placeholder?: string;
  disabled?: boolean;
  errorMessage?: string;
  onChange: (value: string) => void;
};
```

사용 예:

```jsx
<TextInput
  id="email"
  name="email"
  label="이메일"
  value={email}
  errorMessage={emailError}
  onChange={setEmail}
/>
```

---

### [Best Practice]

Input 기준:

```md
- [ ] label을 반드시 제공한다.
- [ ] placeholder를 label 대체로 사용하지 않는다.
- [ ] errorMessage를 입력 필드 가까이에 표시한다.
- [ ] error 상태는 색상만으로 표시하지 않는다.
- [ ] disabled와 readonly를 구분한다.
- [ ] autocomplete 속성을 적절히 사용한다.
```

---

### [FAQ]

Q. placeholder만 있으면 label은 없어도 돼?

A.
권장하지 않는다. placeholder는 입력 예시이고 label은 입력 항목의 이름이다.

Q. error input은 어떻게 표시해야 해?

A.
border 색상, error message, aria 속성 등을 함께 사용해야 한다.

Q. disabled와 readonly는 뭐가 달라?

A.
disabled는 조작과 제출에서 제외되고, readonly는 수정은 불가하지만 값은 읽을 수 있다.

---

## 6.3 Form Field Component

### [개념]

Form Field는 label, input, helper text, error message를 하나의 구조로 묶는 component다.

---

### [핵심]

Form Field 구성:

```text
Label
→ Control
→ Helper Text
→ Error Message
```

---

### [예제]

```jsx
<div className="form-field">
  <label htmlFor="password">비밀번호</label>
  <input id="password" name="password" type="password" />
  <p className="helper-text">8자 이상 입력해 주세요.</p>
</div>
```

Error 상태:

```jsx
<div className="form-field">
  <label htmlFor="email">이메일</label>
  <input
    id="email"
    name="email"
    type="email"
    aria-invalid="true"
    aria-describedby="email-error"
  />
  <p id="email-error" role="alert">
    올바른 이메일 형식이 아닙니다.
  </p>
</div>
```

---

### [실무]

Form Field Review:

```md
- [ ] label과 input이 연결되어 있는가?
- [ ] error message가 input과 연결되어 있는가?
- [ ] helper text와 error text가 구분되는가?
- [ ] spacing이 일관적인가?
- [ ] 필수 입력 표시가 명확한가?
```

---

### [FAQ]

Q. Form Field를 따로 컴포넌트로 만들면 좋아?

A.
반복되는 label, input, error 구조를 일관되게 유지할 수 있어 좋다.

Q. error message에 role alert가 필요해?

A.
동적으로 나타나는 중요한 오류 메시지는 스크린 리더 전달을 위해 고려할 수 있다.

---

## 6.4 Select Checkbox Radio Rules

### [개념]

Select, Checkbox, Radio는 사용자가 제한된 옵션 중 선택할 수 있게 하는 form component다.

---

### [핵심]

사용 기준:

```text
Select
→ 옵션이 많고 하나를 선택

Radio
→ 옵션이 적고 하나를 선택

Checkbox
→ 여러 개 선택 또는 동의 여부

Switch
→ 즉시 적용되는 on/off 상태
```

---

### [예제]

Radio:

```jsx
<fieldset>
  <legend>정렬 기준</legend>

  <label>
    <input type="radio" name="sort" value="latest" />
    최신순
  </label>

  <label>
    <input type="radio" name="sort" value="popular" />
    인기순
  </label>
</fieldset>
```

Checkbox:

```jsx
<label>
  <input type="checkbox" checked={agreed} onChange={handleChange} />
  약관에 동의합니다.
</label>
```

---

### [Best Practice]

```md
- [ ] 관련 radio는 fieldset / legend로 묶는다.
- [ ] checkbox label을 명확히 제공한다.
- [ ] 선택 상태가 시각적으로 명확해야 한다.
- [ ] keyboard 조작이 가능해야 한다.
- [ ] custom control은 native input 접근성을 유지해야 한다.
```

---

### [FAQ]

Q. Radio와 Select 중 뭐를 써야 해?

A.
옵션이 적고 비교가 필요하면 Radio, 옵션이 많으면 Select가 적합하다.

Q. Checkbox와 Switch는 뭐가 달라?

A.
Checkbox는 선택이나 동의에 적합하고, Switch는 즉시 적용되는 on/off 설정에 적합하다.

---

## 6.5 Card Component

### [개념]

Card는 관련 정보를 하나의 시각적 그룹으로 묶어 보여주는 component다.

---

### [핵심]

Card 구성:

```text
Container
→ Header
→ Media
→ Body
→ Footer
→ Actions
```

Card 사용 대상:

- 축제 카드
- 리뷰 카드
- 알림 카드
- 상품 카드
- 프로필 카드
- 통계 카드

---

### [예제]

```jsx
<article className="card">
  <img src="/festival.jpg" alt="야간 축제 무대" />
  <div className="card-body">
    <h2 className="card-title">서울 빛 축제</h2>
    <p className="card-description">서울에서 열리는 야간 조명 축제입니다.</p>
    <Button variant="primary">자세히 보기</Button>
  </div>
</article>
```

---

### [Best Practice]

```md
- [ ] Card는 의미에 따라 article 또는 section 사용을 고려한다.
- [ ] 제목 구조가 명확해야 한다.
- [ ] 클릭 가능한 영역과 버튼 역할을 구분한다.
- [ ] 이미지 alt를 제공한다.
- [ ] 내부 spacing은 token으로 관리한다.
- [ ] card list에서는 grid gap을 사용한다.
```

---

### [FAQ]

Q. Card 전체를 클릭 가능하게 해도 돼?

A.
가능하지만 내부 버튼과 충돌하지 않게 해야 한다. 접근성도 함께 고려해야 한다.

Q. Card에 margin을 직접 주는 게 좋아?

A.
Card 자체보다 Card List나 Grid 부모에서 gap으로 관리하는 것이 재사용에 좋다.

---

## 6.6 Badge Tag Component

### [개념]

Badge와 Tag는 상태, 카테고리, 라벨을 짧게 표시하는 component다.

---

### [핵심]

사용 기준:

```text
Badge
→ 상태나 수량 표시

Tag
→ 카테고리나 키워드 표시
```

Variant 예:

```text
default
primary
success
warning
error
info
```

---

### [예제]

```jsx
<Badge variant="success">진행중</Badge>
<Badge variant="warning">마감임박</Badge>
<Tag>음악</Tag>
<Tag>야간축제</Tag>
```

---

### [Best Practice]

```md
- [ ] 색상만으로 상태를 전달하지 않는다.
- [ ] 텍스트가 짧고 명확해야 한다.
- [ ] variant 의미가 semantic color와 연결되어야 한다.
- [ ] 너무 많은 색상 variant를 만들지 않는다.
```

---

### [FAQ]

Q. Badge와 Tag는 뭐가 달라?

A.
Badge는 상태나 수량을 표시하고, Tag는 카테고리나 키워드를 표시하는 경우가 많다.

Q. 상태 Badge는 색상만 보면 되게 만들어도 돼?

A.
안 된다. 텍스트도 함께 제공해야 한다.

---

## 6.7 Alert Toast Component

### [개념]

Alert와 Toast는 사용자에게 상태나 결과를 알려주는 feedback component다.

---

### [핵심]

사용 기준:

```text
Alert
→ 화면 안에 고정적으로 표시되는 중요한 안내

Toast
→ 일시적으로 표시되는 작업 결과 알림
```

Variant:

```text
info
success
warning
error
```

---

### [예제]

Alert:

```jsx
<Alert variant="error">
  데이터를 불러오지 못했습니다. 잠시 후 다시 시도해 주세요.
</Alert>
```

Toast:

```jsx
showToast({
  variant: "success",
  message: "저장되었습니다.",
});
```

---

### [Best Practice]

Alert 기준:

```md
- [ ] 중요한 오류나 안내를 화면 문맥 안에 표시한다.
- [ ] 닫기 가능 여부를 명확히 한다.
- [ ] role alert 사용 여부를 검토한다.
```

Toast 기준:

```md
- [ ] 너무 오래 표시하지 않는다.
- [ ] 중요한 정보는 Toast만으로 전달하지 않는다.
- [ ] 여러 Toast가 쌓이는 방식이 정의되어야 한다.
- [ ] 성공 / 실패 문구가 명확해야 한다.
```

---

### [FAQ]

Q. Alert와 Toast는 언제 구분해?

A.
사용자가 계속 확인해야 하는 정보는 Alert, 일시적인 작업 결과는 Toast가 적합하다.

Q. 중요한 오류를 Toast만으로 보여줘도 돼?

A.
권장하지 않는다. 사용자가 놓칠 수 있으므로 화면 내 Error State도 함께 제공하는 것이 좋다.

---

## 6.8 Modal Dialog Component

### [개념]

Modal / Dialog는 사용자의 주의를 현재 작업에 집중시키기 위해 화면 위에 표시하는 component다.

---

### [핵심]

사용 대상:

- 확인
- 입력
- 상세 보기
- 경고
- 삭제 확인
- 로그인 유도
- 리뷰 작성

필수 상태:

```text
open
closed
loading
error
```

---

### [예제]

```jsx
<Modal isOpen={isOpen} title="리뷰 작성" onClose={closeModal}>
  <ReviewForm />
</Modal>
```

접근성 구조:

```jsx
<div role="dialog" aria-modal="true" aria-labelledby="modal-title">
  <h2 id="modal-title">리뷰 작성</h2>
  <button type="button" onClick={onClose}>
    닫기
  </button>
</div>
```

---

### [Best Practice]

```md
- [ ] modal title이 있어야 한다.
- [ ] 닫기 버튼이 있어야 한다.
- [ ] ESC 닫기 정책을 정의한다.
- [ ] overlay 클릭 닫기 정책을 정의한다.
- [ ] focus trap을 고려한다.
- [ ] 닫힌 후 이전 focus를 복원한다.
- [ ] 배경 스크롤을 방지한다.
```

---

### [FAQ]

Q. Modal에는 꼭 닫기 버튼이 필요해?

A.
필요하다. 사용자가 명확하게 닫을 수 있어야 한다.

Q. overlay 클릭으로 닫히게 해야 해?

A.
상황에 따라 다르다. 중요한 입력 중이면 실수로 닫히지 않도록 막을 수 있다.

Q. Modal 접근성에서 가장 중요한 것은?

A.
dialog 역할, title 연결, focus 관리, keyboard 조작이다.

---

## 6.9 Tabs Component

### [개념]

Tabs는 같은 맥락의 여러 콘텐츠를 탭으로 전환해 보여주는 component다.

---

### [핵심]

구성:

```text
Tab List
→ Tab
→ Tab Panel
```

상태:

```text
default
hover
focus
selected
disabled
```

---

### [예제]

```jsx
<Tabs defaultValue="info">
  <TabList>
    <Tab value="info">기본 정보</Tab>
    <Tab value="review">리뷰</Tab>
  </TabList>

  <TabPanel value="info">축제 정보</TabPanel>
  <TabPanel value="review">리뷰 목록</TabPanel>
</Tabs>
```

---

### [Best Practice]

```md
- [ ] 선택된 tab이 명확해야 한다.
- [ ] keyboard 이동을 고려한다.
- [ ] tab과 panel 연결이 명확해야 한다.
- [ ] URL 상태가 필요한지 검토한다.
- [ ] 너무 많은 tab은 피한다.
```

---

### [FAQ]

Q. Tabs는 언제 써?

A.
같은 페이지 안에서 관련 있는 콘텐츠 묶음을 전환할 때 사용한다.

Q. Tab 상태를 URL에 넣어야 해?

A.
공유, 새로고침 유지, 뒤로가기 지원이 필요하면 URL query나 path로 관리할 수 있다.

---

## 6.10 Pagination Component

### [개념]

Pagination은 많은 데이터를 여러 페이지로 나누어 탐색하는 component다.

---

### [핵심]

구성:

```text
Previous
Page Numbers
Next
Current Page
Total Page
```

상태:

```text
default
current
disabled
hover
focus
```

---

### [예제]

```jsx
<Pagination currentPage={page} totalPages={totalPages} onPageChange={setPage} />
```

---

### [Best Practice]

```md
- [ ] 현재 페이지가 명확해야 한다.
- [ ] 첫 페이지에서 이전 버튼은 disabled 처리한다.
- [ ] 마지막 페이지에서 다음 버튼은 disabled 처리한다.
- [ ] 페이지 변경 시 loading 상태를 고려한다.
- [ ] URL query와 연동을 고려한다.
```

---

### [FAQ]

Q. Pagination과 Infinite Scroll 중 뭐가 좋아?

A.
검색 결과처럼 위치와 페이지 공유가 중요하면 Pagination, 피드처럼 계속 탐색하는 UX는 Infinite Scroll이 적합하다.

Q. 현재 페이지는 URL에 넣는 게 좋아?

A.
새로고침 유지와 공유가 필요하면 URL query에 넣는 것이 좋다.

---

## 6.11 Table Component

### [개념]

Table은 행과 열 구조의 데이터를 표시하는 component다.

---

### [핵심]

Table 사용 대상:

- 관리자 목록
- 결제 내역
- 통계
- 사용자 목록
- 검색 결과 중 구조화된 데이터

---

### [예제]

```jsx
<table>
  <thead>
    <tr>
      <th scope="col">축제명</th>
      <th scope="col">지역</th>
      <th scope="col">기간</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>서울 빛 축제</td>
      <td>서울</td>
      <td>2026.01.01 - 2026.01.10</td>
    </tr>
  </tbody>
</table>
```

---

### [Best Practice]

```md
- [ ] 표 데이터에는 table을 사용한다.
- [ ] th와 scope를 적절히 사용한다.
- [ ] 모바일 overflow 처리 기준이 있다.
- [ ] 정렬 가능 컬럼은 상태를 표시한다.
- [ ] 빈 데이터 상태를 제공한다.
- [ ] loading 상태를 제공한다.
```

---

### [FAQ]

Q. 레이아웃을 만들려고 table을 써도 돼?

A.
안 된다. table은 표 데이터에 사용하고 레이아웃은 CSS Grid / Flexbox를 사용한다.

Q. 모바일에서 table은 어떻게 처리해?

A.
가로 스크롤, 카드형 변환, 주요 컬럼만 표시 등 프로젝트 기준을 정해야 한다.

---

# 7. Feedback State Pattern Rules

## 7.1 Loading State Pattern

### [개념]

Loading State는 데이터 요청이나 작업 처리 중임을 사용자에게 알려주는 UI 패턴이다.

---

### [핵심]

Loading UI 종류:

```text
Spinner
Skeleton
Progress Bar
Button Loading
Page Loading
Section Loading
```

---

### [실무]

사용 기준:

```text
짧은 작업
→ Button Loading 또는 Spinner

목록 / 카드 로딩
→ Skeleton

파일 업로드 / 긴 작업
→ Progress Bar

페이지 최초 로딩
→ Page Loading
```

---

### [예제]

```jsx
if (isLoading) {
  return <SkeletonList count={5} />;
}
```

Button loading:

```jsx
<Button isLoading={isSubmitting} disabled={isSubmitting}>
  저장
</Button>
```

---

### [FAQ]

Q. Loading State는 꼭 필요해?

A.
필요하다. 사용자가 화면이 멈췄는지 처리 중인지 알 수 있어야 한다.

Q. Skeleton은 언제 쓰면 좋아?

A.
카드나 목록처럼 로딩 후 구조가 예상 가능한 콘텐츠에 적합하다.

---

## 7.2 Empty State Pattern

### [개념]

Empty State는 요청은 성공했지만 표시할 데이터가 없을 때 보여주는 UI 패턴이다.

---

### [핵심]

Empty State 구성:

```text
Title
→ Description
→ Optional Action
```

---

### [예제]

```jsx
<EmptyState
  title="검색 결과가 없습니다"
  description="다른 키워드나 지역으로 다시 검색해 보세요."
  action={<Button variant="secondary">필터 초기화</Button>}
/>
```

---

### [실무]

Empty State가 필요한 곳:

```text
검색 결과 없음
찜 목록 없음
리뷰 없음
알림 없음
채팅 없음
테이블 데이터 없음
필터 결과 없음
```

---

### [FAQ]

Q. 데이터가 없으면 빈 화면이면 안 돼?

A.
안 된다. 사용자는 오류인지 결과가 없는지 알 수 없다.

Q. Empty State에는 버튼이 꼭 있어야 해?

A.
필수는 아니지만 사용자가 다음 행동을 할 수 있으면 좋다.

---

## 7.3 Error State Pattern

### [개념]

Error State는 요청 실패나 처리 오류가 발생했을 때 사용자에게 문제와 복구 방법을 안내하는 UI 패턴이다.

---

### [핵심]

Error State 구성:

```text
Error Title
→ User Friendly Message
→ Recovery Action
→ Optional Detail
```

---

### [예제]

```jsx
<ErrorState
  title="데이터를 불러오지 못했습니다"
  description="네트워크 상태를 확인한 뒤 다시 시도해 주세요."
  action={<Button onClick={refetch}>다시 시도</Button>}
/>
```

---

### [실무]

Error Message 기준:

```md
- [ ] 개발자용 raw error를 그대로 노출하지 않는다.
- [ ] 사용자가 이해할 수 있는 문장으로 표현한다.
- [ ] 재시도 가능한 경우 action을 제공한다.
- [ ] 인증 오류는 로그인 이동을 제공한다.
- [ ] 권한 오류는 접근 불가 안내를 제공한다.
```

---

### [FAQ]

Q. 에러는 console.log만 해도 돼?

A.
안 된다. 사용자에게 실패 상태와 복구 방법을 알려야 한다.

Q. 서버 에러 메시지를 그대로 보여줘도 돼?

A.
민감한 정보가 포함될 수 있으므로 사용자 친화 메시지로 바꾸는 것이 좋다.

---

## 7.4 Success State Pattern

### [개념]

Success State는 사용자의 작업이 성공했음을 알려주는 UI 패턴이다.

---

### [핵심]

Success 사용 상황:

```text
저장 완료
삭제 완료
로그인 성공
회원가입 완료
리뷰 등록 완료
결제 완료
복사 완료
```

---

### [실무]

Success Feedback 기준:

```text
가벼운 작업
→ Toast

중요한 완료
→ Success Page 또는 Alert

Form 저장
→ Toast + 상태 갱신

삭제
→ Toast + 목록 갱신
```

---

### [FAQ]

Q. 성공 메시지는 꼭 필요해?

A.
사용자가 작업 완료를 확신해야 하는 경우 필요하다.

Q. 모든 성공에 Toast를 띄워도 돼?

A.
과하면 방해가 될 수 있다. 중요한 행동 중심으로 사용한다.

---

# 8. Layout System Rules

## 8.1 Layout System

### [개념]

Layout System은 페이지와 컴포넌트를 배치하는 공통 구조다.

---

### [핵심]

Layout 구성:

- App Layout
- Page Layout
- Container
- Section
- Grid
- Stack
- Inline
- Sidebar Layout
- Header / Footer
- Responsive Layout

---

### [예제]

Container:

```css
.container {
  width: min(100% - 32px, 1200px);
  margin: 0 auto;
}
```

Stack:

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-4);
}
```

Grid:

```css
.grid {
  display: grid;
  gap: var(--spacing-6);
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}
```

---

### [실무]

Layout Review:

```md
- [ ] Page container가 일관적인가?
- [ ] section spacing이 token으로 관리되는가?
- [ ] grid gap이 일관적인가?
- [ ] component가 외부 layout margin을 과하게 갖지 않는가?
- [ ] 모바일 layout이 정의되어 있는가?
```

---

### [FAQ]

Q. Layout System은 왜 필요해?

A.
페이지마다 간격과 배치가 달라지는 것을 막고 일관된 화면 구조를 만들기 위해 필요하다.

Q. 컴포넌트에 margin을 직접 주면 안 돼?

A.
재사용 컴포넌트라면 외부 배치는 부모 layout이 담당하는 것이 좋다.

---

## 8.2 Responsive Layout Rules

### [개념]

Responsive Layout은 화면 크기에 따라 레이아웃이 자연스럽게 변하도록 설계하는 규칙이다.

---

### [핵심]

반응형 기준:

```text
Mobile First
→ Tablet
→ Desktop
→ Wide
```

권장 breakpoint:

```text
mobile: default
tablet: 768px
desktop: 1024px
wide: 1280px
```

---

### [실무]

반응형 Layout 기준:

```md
- [ ] 모바일에서 가로 스크롤이 없는가?
- [ ] 카드 목록이 1열 → 2열 → 3열로 자연스럽게 변하는가?
- [ ] Modal이 모바일에서 화면을 넘지 않는가?
- [ ] Navigation이 모바일에서 대응되는가?
- [ ] Table은 overflow 또는 카드 변환 기준이 있는가?
```

---

### [FAQ]

Q. Design System에도 반응형 기준이 필요해?

A.
필요하다. 컴포넌트와 레이아웃이 같은 breakpoint 기준을 공유해야 한다.

Q. breakpoint는 고정값이야?

A.
아니다. 일반 기준은 있지만 콘텐츠가 깨지는 지점을 기준으로 조정할 수 있다.

---

# 9. Theme Rules

## 9.1 Theme System

### [개념]

Theme System은 같은 컴포넌트 구조를 유지하면서 색상과 시각 스타일을 전환할 수 있도록 만드는 구조다.

---

### [핵심]

Theme 구성:

```text
Primitive Token
→ Semantic Token
→ Theme Value
→ Component Style
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

---

### [실무]

Theme Review:

```md
- [ ] 컴포넌트가 raw color 대신 semantic token을 사용하는가?
- [ ] light / dark token이 구분되어 있는가?
- [ ] background / surface / text / border가 정의되어 있는가?
- [ ] focus ring이 dark mode에서도 보이는가?
- [ ] chart / icon / image 색상도 고려했는가?
```

---

### [FAQ]

Q. Theme를 만들려면 CSS variable이 좋아?

A.
CSS variable은 런타임 theme 전환에 유리하다.

Q. 컴포넌트에서 raw color를 쓰면 안 돼?

A.
Theme 확장을 고려하면 semantic token을 사용하는 것이 좋다.

---

## 9.2 Dark Mode Rules

### [개념]

Dark Mode는 어두운 배경과 밝은 텍스트를 사용하는 theme다.

---

### [핵심]

Dark Mode 필수 확인:

```md
- [ ] background와 text contrast
- [ ] surface 색상
- [ ] border 색상
- [ ] muted text 색상
- [ ] disabled 색상
- [ ] hover 색상
- [ ] focus ring 색상
- [ ] shadow 대체
- [ ] icon visibility
```

---

### [실무]

Dark Mode 구현 Flow:

```text
Semantic Token 정의
→ Light Token 정의
→ Dark Token 정의
→ Theme Attribute 적용
→ Component raw color 제거
→ Contrast 검토
→ User Preference 저장
```

---

### [FAQ]

Q. Dark Mode는 배경만 검게 바꾸면 돼?

A.
아니다. text, border, surface, disabled, hover, focus, icon까지 함께 조정해야 한다.

Q. Dark Mode가 꼭 필요해?

A.
요구사항이 아니라면 필수는 아니다. 다만 확장 가능하도록 token 기반 구조를 만드는 것이 좋다.

---

# 10. Accessibility Rules

## 10.1 Design System Accessibility

### [개념]

Design System Accessibility는 공통 컴포넌트가 기본적으로 접근성을 만족하도록 설계하는 기준이다.

---

### [핵심]

필수 기준:

- Semantic HTML
- Keyboard Navigation
- Focus Visible
- Accessible Name
- Label Association
- Color Contrast
- Error Message Association
- ARIA 최소 사용
- Modal Focus Management
- Reduced Motion
- Touch Target Size

---

### [Checklist]

```md
- [ ] Button은 button 요소를 사용하는가?
- [ ] Link는 a 또는 Link를 사용하는가?
- [ ] Input은 label과 연결되는가?
- [ ] Error message는 input과 연결되는가?
- [ ] Icon button은 accessible name이 있는가?
- [ ] Modal은 dialog role과 title이 있는가?
- [ ] Focus style이 보이는가?
- [ ] 색상만으로 상태를 전달하지 않는가?
- [ ] Keyboard만으로 조작 가능한가?
```

---

### [FAQ]

Q. Design System에 접근성을 넣어야 해?

A.
반드시 넣어야 한다. 공통 컴포넌트가 접근성을 만족하면 전체 화면 품질이 올라간다.

Q. aria를 많이 넣으면 접근성이 좋아져?

A.
아니다. Semantic HTML을 우선 사용하고 부족한 의미를 보완할 때만 aria를 사용한다.

---

## 10.2 Focus and Keyboard Rules

### [개념]

Focus and Keyboard Rules는 키보드 사용자가 컴포넌트를 탐색하고 조작할 수 있도록 하는 기준이다.

---

### [핵심]

컴포넌트별 기준:

```text
Button
→ Enter / Space 실행

Link
→ Enter 이동

Modal
→ focus trap / ESC 닫기

Tabs
→ 방향키 이동 고려

Select
→ keyboard 선택 가능

Dropdown
→ ESC 닫기 / 방향키 이동 고려
```

---

### [예제]

Focus style:

```css
:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}
```

---

### [FAQ]

Q. focus outline을 제거해도 돼?

A.
제거만 하면 안 된다. 반드시 대체 focus style을 제공해야 한다.

Q. 모든 컴포넌트를 키보드로 조작 가능해야 해?

A.
사용자가 조작하는 interactive component는 키보드 접근이 가능해야 한다.

---

## 10.3 Color Contrast Rules

### [개념]

Color Contrast는 텍스트와 배경의 명도 차이가 충분한지 판단하는 접근성 기준이다.

---

### [핵심]

검토 대상:

- 본문 텍스트
- 보조 텍스트
- 버튼 텍스트
- 에러 메시지
- disabled 텍스트
- placeholder
- link
- badge
- toast
- dark mode text

---

### [실무]

Review Agent는 다음을 확인한다.

```md
- [ ] primary button의 텍스트가 읽히는가?
- [ ] error message가 배경과 충분히 구분되는가?
- [ ] muted text가 너무 흐리지 않은가?
- [ ] disabled 상태가 정보 전달을 방해하지 않는가?
- [ ] dark mode에서 contrast가 유지되는가?
```

---

### [FAQ]

Q. 색상 contrast는 왜 중요해?

A.
저시력 사용자와 다양한 화면 환경에서 텍스트를 읽을 수 있어야 하기 때문이다.

Q. 색상만으로 상태를 표시해도 돼?

A.
안 된다. 텍스트, 아이콘, 메시지 등 추가 정보가 필요하다.

---

# 11. Content and Message Rules

## 11.1 UI Text Rules

### [개념]

UI Text는 버튼, 안내 문구, 에러 메시지, 빈 상태 문구 등 사용자가 화면에서 읽는 짧은 텍스트다.

---

### [핵심]

좋은 UI Text 기준:

- 짧고 명확함
- 사용자의 행동을 안내함
- 기술 용어 최소화
- 상태와 다음 행동을 알려줌
- 같은 상황에서 같은 표현 사용
- 부정확한 표현 금지

---

### [예제]

나쁜 예:

```text
Error occurred.
```

좋은 예:

```text
데이터를 불러오지 못했습니다. 잠시 후 다시 시도해 주세요.
```

나쁜 버튼:

```text
OK
```

좋은 버튼:

```text
저장
삭제
다시 시도
필터 초기화
```

---

### [FAQ]

Q. 버튼 텍스트는 어떻게 쓰는 게 좋아?

A.
사용자가 수행할 행동을 동사 중심으로 명확히 작성한다. 예: 저장, 삭제, 검색, 다시 시도.

Q. 에러 메시지는 자세할수록 좋아?

A.
사용자가 이해하고 행동할 수 있을 만큼만 명확히 쓰는 것이 좋다. 개발자용 세부 오류는 노출하지 않는다.

---

## 11.2 Empty Error Success Message Rules

### [개념]

상태 메시지는 Loading, Empty, Error, Success 상황에서 사용자에게 현재 상태를 알려주는 문구다.

---

### [핵심]

문구 구조:

```text
상태 설명
→ 이유 또는 맥락
→ 다음 행동
```

---

### [예제]

Empty:

```text
검색 결과가 없습니다.
다른 키워드나 지역으로 다시 검색해 보세요.
```

Error:

```text
축제 정보를 불러오지 못했습니다.
네트워크 상태를 확인한 뒤 다시 시도해 주세요.
```

Success:

```text
리뷰가 등록되었습니다.
```

---

### [FAQ]

Q. Empty State 문구에는 무엇이 들어가야 해?

A.
데이터가 없다는 사실과 사용자가 다음에 할 수 있는 행동이 들어가면 좋다.

Q. Success 메시지는 짧아도 돼?

A.
대부분 짧고 명확한 문구가 좋다. 예: 저장되었습니다.

---

# 12. Documentation Rules

## 12.1 Design System Documentation

### [개념]

Design System Documentation은 토큰, 컴포넌트, 패턴, 사용 기준을 문서화해 Agent와 개발자가 동일하게 참조할 수 있게 하는 것이다.

---

### [핵심]

문서에 포함할 항목:

```md
# Component Name

## Purpose

## Anatomy

## Props

## Variants

## Sizes

## States

## Accessibility

## Usage

## Do

## Don't

## Examples
```

---

### [실무]

Button 문서 예:

```md
# Button

## Purpose

사용자의 주요 행동을 실행한다.

## Variants

- primary: 가장 중요한 행동
- secondary: 보조 행동
- danger: 위험 행동
- ghost: 낮은 강조 행동

## Do

- 저장, 삭제, 검색처럼 명확한 동사를 사용한다.
- loading 중에는 disabled 처리한다.

## Don't

- 링크 이동에 Button을 사용하지 않는다.
- danger variant를 일반 행동에 사용하지 않는다.
```

---

### [FAQ]

Q. Design System 문서는 왜 필요해?

A.
컴포넌트 사용 기준을 명확히 해 UI 일관성과 코드 리뷰 품질을 높이기 위해 필요하다.

Q. 모든 컴포넌트를 문서화해야 해?

A.
자주 쓰는 핵심 컴포넌트부터 문서화하는 것이 현실적이다.

---

## 12.2 Example Rules

### [개념]

Design System 예제는 Agent가 바로 코드 생성과 리뷰에 활용할 수 있어야 한다.

---

### [핵심]

좋은 예제 조건:

- 짧고 직접적
- variant 포함
- state 포함
- accessibility 반영
- token 사용
- 실제 도메인 예시 포함

---

### [예제]

좋은 예:

```jsx
<Button variant="primary" size="md" type="submit" isLoading={isSubmitting}>
  저장
</Button>
```

나쁜 예:

```jsx
<Button blue big flag>
  OK
</Button>
```

---

### [FAQ]

Q. 예제 코드는 길수록 좋아?

A.
아니다. RAG 문서에서는 짧고 검색 가능한 예제가 더 좋다.

Q. 예제에 접근성을 포함해야 해?

A.
해야 한다. icon button, form field, modal 같은 컴포넌트는 접근성 예제를 포함하는 것이 좋다.

---

# 13. Frontend Implementation Rules

## 13.1 React Component Implementation

### [개념]

Design System 컴포넌트는 React에서 재사용 가능한 component로 구현될 수 있어야 한다.

---

### [핵심]

구현 기준:

- props API 명확
- variant 제한
- size 제한
- state 처리
- accessibility 기본 제공
- token 기반 스타일
- className override 정책
- ref 필요 여부 검토
- 테스트 가능성 확보

---

### [예제]

Button 구현 예:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "danger" | "ghost";
  size?: "sm" | "md" | "lg";
  isLoading?: boolean;
  disabled?: boolean;
  type?: "button" | "submit" | "reset";
  children: React.ReactNode;
  onClick?: () => void;
};

function Button({
  variant = "primary",
  size = "md",
  isLoading = false,
  disabled = false,
  type = "button",
  children,
  onClick,
}: ButtonProps) {
  return (
    <button
      type={type}
      disabled={disabled || isLoading}
      onClick={onClick}
      data-variant={variant}
      data-size={size}
      aria-busy={isLoading}
    >
      {isLoading ? "처리 중..." : children}
    </button>
  );
}
```

---

### [실무]

Review 기준:

```md
- [ ] 기본 props 값이 안전한가?
- [ ] form 내부에서 type 기본값이 안전한가?
- [ ] loading 중 중복 클릭이 방지되는가?
- [ ] variant 값이 제한되어 있는가?
- [ ] 접근성 속성이 필요한 경우 포함되어 있는가?
```

---

### [FAQ]

Q. Button 기본 type을 submit으로 해도 돼?

A.
권장하지 않는다. form 안에서 의도치 않은 제출이 발생할 수 있으므로 기본은 button이 안전하다.

Q. Design System 컴포넌트는 무조건 복잡해도 돼?

A.
아니다. 자주 쓰는 공통 요구만 포함하고, 과도한 props 확장은 피해야 한다.

---

## 13.2 Component Composition Rules

### [개념]

Component Composition은 작은 컴포넌트를 조합해 더 복잡한 UI를 만드는 방식이다.

---

### [핵심]

좋은 Composition:

```text
Card
→ CardHeader
→ CardBody
→ CardFooter

Modal
→ ModalHeader
→ ModalBody
→ ModalFooter

FormField
→ Label
→ Control
→ HelperText
→ ErrorMessage
```

---

### [예제]

```jsx
<Card>
  <CardHeader>
    <CardTitle>서울 빛 축제</CardTitle>
  </CardHeader>
  <CardBody>
    <p>야간 조명 축제입니다.</p>
  </CardBody>
  <CardFooter>
    <Button>자세히 보기</Button>
  </CardFooter>
</Card>
```

---

### [실무]

Composition Review:

```md
- [ ] 조합 구조가 직관적인가?
- [ ] sub component 이름이 명확한가?
- [ ] 너무 깊은 조합으로 사용성이 떨어지지 않는가?
- [ ] 단순 use case도 쉽게 작성 가능한가?
```

---

### [FAQ]

Q. Compound Component 패턴을 꼭 써야 해?

A.
필수는 아니다. 복잡한 컴포넌트에서 조합 유연성이 필요할 때 적합하다.

Q. 컴포넌트를 너무 쪼개면 좋은 거야?

A.
아니다. 사용성이 떨어질 정도로 쪼개면 오히려 복잡해진다.

---

# 14. Design System Review Rules

## 14.1 Review Agent Design System Checklist

### [Checklist]

Review Agent는 Design System 기준으로 다음을 검토한다.

```md
## Token

- [ ] Color Token이 정의되어 있는가?
- [ ] Spacing Token이 정의되어 있는가?
- [ ] Typography Token이 정의되어 있는가?
- [ ] Radius / Shadow / Z-index Token이 정의되어 있는가?
- [ ] raw value 하드코딩이 과하지 않은가?

## Component

- [ ] Button variant / size / state가 정의되어 있는가?
- [ ] Input label / error / disabled 상태가 정의되어 있는가?
- [ ] Card 구조와 spacing이 일관적인가?
- [ ] Modal 접근성 기준이 있는가?
- [ ] Alert / Toast 사용 기준이 구분되어 있는가?

## Pattern

- [ ] Loading State 기준이 있는가?
- [ ] Empty State 기준이 있는가?
- [ ] Error State 기준이 있는가?
- [ ] Success Feedback 기준이 있는가?

## Accessibility

- [ ] focus-visible 스타일이 있는가?
- [ ] keyboard navigation을 고려하는가?
- [ ] color contrast가 충분한가?
- [ ] icon button accessible name이 있는가?
- [ ] form field label 연결이 있는가?

## Responsive

- [ ] breakpoint 기준이 있는가?
- [ ] mobile first 기준인가?
- [ ] table / modal / navigation 모바일 대응 기준이 있는가?

## Theme

- [ ] semantic token을 사용하는가?
- [ ] dark mode 확장 가능성이 있는가?
- [ ] raw color가 컴포넌트에 흩어져 있지 않은가?

## Documentation

- [ ] component purpose가 명확한가?
- [ ] variant 사용 기준이 있는가?
- [ ] do / don't가 있는가?
- [ ] 예제 코드가 있는가?
```

---

### [실무]

Review Agent 판단 Flow:

```text
Design System 기준 확인
→ Token 사용 확인
→ Component Spec 확인
→ State / Variant 확인
→ Accessibility 확인
→ Responsive 확인
→ Theme 확장성 확인
→ Documentation 확인
→ Final Decision
```

---

### [FAQ]

Q. Review Agent가 Design System에서 가장 먼저 봐야 할 것은?

A.
Token, Component Spec, State, Accessibility, Responsive 기준이 있는지 먼저 봐야 한다.

Q. 디자인이 예쁘면 Design System 기준을 통과한 거야?

A.
아니다. 일관성, 재사용성, 접근성, 반응형, 문서화 기준까지 봐야 한다.

---

## 14.2 PM Agent Design System Checklist

### [Checklist]

PM Agent는 Design System 기준으로 화면 완료 여부를 판단한다.

```md
## UI Completion

- [ ] 화면이 요구사항과 일치하는가?
- [ ] 주요 버튼과 입력이 일관적인가?
- [ ] 사용자 행동 흐름이 명확한가?
- [ ] 로딩 / 빈 결과 / 오류 상태가 있는가?
- [ ] 모바일 화면이 깨지지 않는가?

## Product Consistency

- [ ] 같은 의미의 UI가 같은 방식으로 표현되는가?
- [ ] 색상 사용이 일관적인가?
- [ ] 버튼 중요도가 명확한가?
- [ ] 위험 행동이 danger style로 구분되는가?
- [ ] 에러 메시지가 사용자 친화적인가?

## Release Decision

- [ ] Critical UI 문제 없음
- [ ] 주요 기능 사용 가능
- [ ] 접근성 심각 이슈 없음
- [ ] 반응형 심각 이슈 없음
```

---

### [실무]

PM Agent 판단:

```text
UI Complete
→ 요구사항 충족 + Design System 기준 충족

UI Partial
→ 기능은 가능하지만 일부 UI 기준 미흡

UI Blocked
→ 사용자 흐름 방해, 모바일 깨짐, 주요 상태 누락
```

---

### [FAQ]

Q. PM Agent는 디자인 토큰까지 봐야 해?

A.
세부 구현보다 화면 일관성, 사용자 흐름, 상태 처리, 완료 여부를 중심으로 판단한다.

Q. UI 이슈가 기능 완료를 막을 수 있어?

A.
사용자가 기능을 사용하기 어렵다면 Blocker가 될 수 있다.

---

## 14.3 Frontend Agent Design System Rules

### [개념]

Frontend Agent는 UI를 생성할 때 Design System 기준을 우선 적용해야 한다.

---

### [핵심]

Frontend Agent 생성 기준:

```md
- [ ] 기존 Design Token을 사용한다.
- [ ] 기존 Component Spec을 따른다.
- [ ] 임의 variant를 만들지 않는다.
- [ ] Button / Input / Card 등 공통 컴포넌트를 재사용한다.
- [ ] Loading / Empty / Error State를 포함한다.
- [ ] 접근성 기본을 반영한다.
- [ ] Mobile First 기준을 따른다.
- [ ] raw color와 임의 spacing을 남발하지 않는다.
- [ ] 새 패턴이 필요하면 추가 이유를 명시한다.
```

---

### [실무]

Frontend Agent UI 생성 Flow:

```text
Requirement 분석
→ Design System 확인
→ 필요한 Component 선택
→ Token 적용
→ State 처리
→ Responsive 처리
→ Accessibility 처리
→ Review Checklist
```

---

### [FAQ]

Q. Frontend Agent가 임의로 새 버튼 스타일을 만들어도 돼?

A.
기존 variant로 해결할 수 없을 때만 가능하다. 새 variant 추가 이유를 명확히 해야 한다.

Q. 공통 컴포넌트 대신 div로 직접 만들어도 돼?

A.
단순한 경우는 가능하지만 공통 UI가 이미 있다면 재사용하는 것이 좋다.

---

# 15. Common Design System Mistakes

## 15.1 Common Mistakes

### [개념]

Design System 문서는 자주 발생하는 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생하는 실수:

- 토큰 없이 색상 직접 사용
- 화면마다 다른 spacing 사용
- Button variant 기준 없음
- danger action을 일반 버튼으로 표시
- disabled 상태 누락
- loading 상태 누락
- error state 누락
- empty state 누락
- input label 누락
- icon button accessible name 누락
- modal focus 관리 누락
- table 모바일 대응 없음
- dark mode에서 raw color 깨짐
- toast로 중요한 에러만 표시
- 공통 컴포넌트보다 일회성 div 남발
- variant가 너무 많아짐
- props가 너무 복잡해짐
- 문서화 없이 컴포넌트 추가
- 디자인과 코드 token 불일치
- 접근성 기준이 컴포넌트에 포함되지 않음
- PM / Frontend / Review Agent 기준 불일치

---

### [Troubleshooting]

문제별 빠른 판단:

```text
UI가 화면마다 다름
→ Token / Component Spec / Variant 기준 확인

버튼 스타일이 제각각
→ Button Component / Variant / Size 기준 확인

Form 품질이 낮음
→ FormField / Label / Error Message 기준 확인

모바일 깨짐
→ Responsive Layout / Breakpoint 기준 확인

Dark Mode 이상함
→ Raw Color / Semantic Token 확인

접근성 문제
→ Focus / Label / Accessible Name / Keyboard 확인
```

---

### [FAQ]

Q. Design System에서 가장 흔한 실수는?

A.
토큰 없이 화면마다 직접 스타일을 작성하고, 공통 컴포넌트 기준 없이 버튼과 입력을 매번 새로 만드는 것이다.

Q. variant가 많아지면 좋은 거 아니야?

A.
아니다. variant가 너무 많으면 선택 기준이 흐려지고 유지보수가 어려워진다.

Q. 문서화 없이 컴포넌트를 추가하면 안 돼?

A.
작은 프로젝트에서는 가능하지만 공통 컴포넌트라면 최소한 purpose, variant, state 기준은 남기는 것이 좋다.

---

# 16. Design System Maturity Rules

## 16.1 Maturity Level

### [개념]

Design System은 한 번에 완성하지 않고 프로젝트 규모에 맞게 단계적으로 성장시킨다.

---

### [Comparison]

| Level   | 상태              | 구성                                |
| ------- | ----------------- | ----------------------------------- |
| Level 0 | 없음              | 화면마다 직접 스타일                |
| Level 1 | Basic Token       | color, spacing, font token          |
| Level 2 | Core Components   | Button, Input, Card, Modal          |
| Level 3 | Pattern System    | Loading, Empty, Error, Form Pattern |
| Level 4 | Documented System | Spec, Do/Don't, Examples            |
| Level 5 | Managed System    | Versioning, Testing, Governance     |

---

### [실무]

학원 프로젝트 / 개인 프로젝트 권장 목표:

```text
Level 1 Basic Token
+ Level 2 Core Components
+ 일부 Level 3 Feedback Pattern
```

운영 서비스 권장 목표:

```text
Level 3 Pattern System
+ Level 4 Documented System
```

---

### [FAQ]

Q. 처음부터 완전한 Design System을 만들어야 해?

A.
아니다. 작은 프로젝트는 token과 핵심 컴포넌트부터 시작하는 것이 좋다.

Q. 개인 AI 프로젝트에서는 어느 정도가 적당해?

A.
Frontend Agent가 일관된 UI를 만들 수 있도록 Basic Token, Core Components, Feedback Pattern 기준까지 있으면 좋다.

---

# 17. Final Quality Checklist

## 17.1 Design System Quality Checklist

### [Checklist]

최종 Design System 품질 체크리스트:

```md
## Core

- [ ] Design System 목적이 명확한가?
- [ ] Design Principles가 있는가?
- [ ] Agent가 사용할 수 있는 기준인가?

## Token

- [ ] Color Token이 정의되어 있는가?
- [ ] Typography Token이 정의되어 있는가?
- [ ] Spacing Token이 정의되어 있는가?
- [ ] Radius / Shadow / Z-index Token이 정의되어 있는가?
- [ ] Semantic Token 구조가 있는가?
- [ ] raw value 사용이 제한되는가?

## Component

- [ ] Button Spec이 있는가?
- [ ] Input / FormField Spec이 있는가?
- [ ] Card Spec이 있는가?
- [ ] Modal Spec이 있는가?
- [ ] Alert / Toast 기준이 있는가?
- [ ] Badge / Tag 기준이 있는가?
- [ ] Table / Pagination 기준이 있는가?

## Variant State

- [ ] Variant 이름이 의미 기반인가?
- [ ] Size 기준이 일관적인가?
- [ ] Disabled 상태가 있는가?
- [ ] Loading 상태가 있는가?
- [ ] Error 상태가 있는가?
- [ ] Focus 상태가 있는가?

## Pattern

- [ ] Loading State Pattern이 있는가?
- [ ] Empty State Pattern이 있는가?
- [ ] Error State Pattern이 있는가?
- [ ] Success Feedback Pattern이 있는가?

## Accessibility

- [ ] Semantic HTML 기준이 반영되어 있는가?
- [ ] Focus Visible 기준이 있는가?
- [ ] Keyboard 조작 기준이 있는가?
- [ ] Label / Error 연결 기준이 있는가?
- [ ] Accessible Name 기준이 있는가?
- [ ] Color Contrast 기준이 있는가?

## Responsive

- [ ] Breakpoint 기준이 있는가?
- [ ] Mobile First 기준인가?
- [ ] Modal / Table / Navigation 모바일 대응 기준이 있는가?

## Theme

- [ ] Theme 확장 구조가 있는가?
- [ ] Dark Mode 대응 가능성이 있는가?
- [ ] semantic token을 사용하는가?

## Documentation

- [ ] Component purpose가 명확한가?
- [ ] Variant 사용 기준이 있는가?
- [ ] Do / Don't가 있는가?
- [ ] 예제 코드가 있는가?
- [ ] Review Checklist가 있는가?

## Agent Usage

- [ ] Frontend Agent가 UI 생성 기준으로 사용할 수 있는가?
- [ ] Review Agent가 승인 기준으로 사용할 수 있는가?
- [ ] PM Agent가 완료 판단에 사용할 수 있는가?
```

---

### [FAQ]

Q. Design System 최종 승인 기준은 뭐야?

A.
Token, Core Component, State, Accessibility, Responsive, Documentation 기준이 있어야 한다.

Q. 모든 항목이 완벽해야 해?

A.
아니다. 프로젝트 규모에 맞게 핵심 기준부터 갖추면 된다.

---

# 18. Final Goal

## 18.1 Domain Final Goal

### [개념]

Design System Domain Rules의 최종 목적은 Frontend Agent가 일관된 UI를 생성하고, Review Agent가 UI 품질과 접근성, 재사용성을 검토하며, PM Agent가 기능 화면의 완료 여부를 판단할 수 있도록 하는 것이다.

---

### [핵심]

최종 수행 가능 작업:

- Design System 범위 판단
- Design Token 설계
- Primitive Token / Semantic Token 구분
- Button / Input / Card / Modal 등 핵심 컴포넌트 규격 정의
- Variant / Size / State 기준 정의
- Loading / Empty / Error / Success Pattern 정의
- Form Field 접근성 기준 정의
- Theme / Dark Mode 확장 판단
- Responsive Layout 기준 판단
- UI Text 기준 판단
- Component Documentation 작성
- Frontend Agent UI 생성 기준 제공
- Review Agent UI 검토 기준 제공
- PM Agent 완료 판단 기준 제공

---

### [실무]

최종 Agent Flow:

```text
UI Request
→ Design Principles 확인
→ Token 확인
→ Component Spec 확인
→ Variant / State 선택
→ Accessibility 적용
→ Responsive 적용
→ Feedback State 적용
→ Documentation / Review 기준 확인
→ Final UI Output
```

---

### [FAQ]

Q. Design System 문서의 최종 목적은 뭐야?

A.
Frontend Agent / Review Agent / PM Agent가 일관된 UI를 만들고 검토하고 완료 판단할 수 있도록 기준을 제공하는 것이다.

Q. 이 문서가 Frontend Foundation 마지막 문서야?

A.
현재 계획된 Frontend Domain Rules 기준으로는 마지막 문서다. 이후에는 필요에 따라 Next.js, Advanced React Pattern, Frontend Performance Tuning 같은 Expert 문서로 확장할 수 있다.

---

# Retrieval Queries

### [FAQ]

Q. Design System 문서는 왜 필요해?

A.
Frontend Agent / Review Agent / PM Agent가 UI를 일관되게 생성하고 검토하기 위해 필요하다.

Q. Design System이 뭐야?

A.
디자인 원칙, 디자인 토큰, 컴포넌트, 패턴, 문서화, 사용 규칙의 집합이다.

Q. Design System은 컴포넌트 라이브러리와 같아?

A.
아니다. 컴포넌트 라이브러리는 Design System의 일부이고, Design System은 토큰과 사용 규칙까지 포함한다.

Q. Design System과 Styling Architecture 차이는?

A.
Styling Architecture는 스타일 코드 구조이고, Design System은 UI 규격, 토큰, 컴포넌트, 패턴, 사용 기준까지 포함한다.

Q. 작은 프로젝트에도 Design System이 필요해?

A.
거대한 시스템은 필요 없지만 색상, 간격, 버튼, 입력, 카드 정도의 미니 Design System은 도움이 된다.

Q. Design System의 핵심은 뭐야?

A.
UI를 매번 새로 만들지 않고 정해진 규칙과 컴포넌트로 일관성 있게 만드는 것이다.

Q. Design Principles는 뭐야?

A.
UI를 만들 때 지켜야 하는 상위 원칙이다. 예: 일관성, 명확성, 접근성, 피드백, 확장성.

Q. 예쁜 UI가 가장 중요해?

A.
아니다. 요구사항 충족, 사용성, 접근성, 일관성이 먼저다.

Q. Design Token이 뭐야?

A.
색상, 간격, 폰트, radius, shadow 같은 디자인 값을 이름으로 관리하는 방식이다.

Q. Design Token은 왜 필요해?

A.
디자인 값을 일관되게 관리하고 변경 시 전체 UI에 안정적으로 반영하기 위해 필요하다.

Q. 모든 값을 token으로 만들어야 해?

A.
아니다. 반복 사용되거나 의미 있는 값부터 token으로 관리한다.

Q. Token 이름은 어떻게 짓는 게 좋아?

A.
역할과 의미가 드러나게 짓는다. 예: `--color-primary`, `--color-error`, `--spacing-4`.

Q. Primitive Token이 뭐야?

A.
`--blue-600`처럼 원시 색상이나 값을 나타내는 token이다.

Q. Semantic Token이 뭐야?

A.
`--color-primary`, `--color-error`처럼 UI 역할과 의미를 가진 token이다.

Q. Primitive Token과 Semantic Token 중 뭐를 컴포넌트에서 써야 해?

A.
컴포넌트에서는 semantic token을 우선 사용하는 것이 좋다.

Q. Color Token은 어떤 것이 필요해?

A.
primary, background, surface, text, muted, border, error, warning, success, info, disabled, focus-ring이 필요하다.

Q. Error 색상은 그냥 red로 쓰면 안 돼?

A.
가능하지만 `--color-error` 같은 semantic token으로 관리하는 것이 좋다.

Q. Spacing Token은 왜 필요해?

A.
화면마다 margin, padding, gap이 제각각이 되는 것을 막기 위해 필요하다.

Q. margin과 gap 중 뭐가 좋아?

A.
리스트나 레이아웃 요소 사이 간격은 gap이 더 명확한 경우가 많다.

Q. Typography Token은 뭘 관리해?

A.
font-size, font-weight, line-height, font-family 같은 글자 스타일을 관리한다.

Q. heading tag와 typography style은 같아야 해?

A.
heading tag는 의미 구조이고, 시각 스타일은 typography token으로 관리한다.

Q. Radius Token은 왜 필요해?

A.
Button, Card, Modal의 모서리 둥글기를 일관되게 관리하기 위해 필요하다.

Q. Shadow Token은 왜 필요해?

A.
Card, Modal, Toast 같은 UI의 깊이 표현을 일관되게 관리하기 위해 필요하다.

Q. Z-index Token은 왜 필요해?

A.
Modal, Toast, Dropdown, Header의 겹침 순서를 예측 가능하게 관리하기 위해 필요하다.

Q. z-index는 그냥 9999로 쓰면 안 돼?

A.
권장하지 않는다. token scale로 관리하는 것이 좋다.

Q. Motion Token은 왜 필요해?

A.
transition duration과 easing을 일관되게 관리하기 위해 필요하다.

Q. Component Specification은 뭐야?

A.
컴포넌트의 목적, props, variant, size, state, accessibility, 사용 예시를 정의한 규격이다.

Q. Component Spec에는 뭐가 들어가야 해?

A.
Purpose, Props, Variants, Sizes, States, Accessibility, Usage, Do, Don’t, Examples가 들어가면 좋다.

Q. Component API는 뭐야?

A.
컴포넌트를 사용하는 props와 event handler의 규칙이다.

Q. props 이름은 어떻게 지어야 해?

A.
역할이 명확한 이름을 사용한다. 예: variant, size, isLoading, disabled, onClick.

Q. variant는 뭐야?

A.
같은 컴포넌트가 목적에 따라 다른 시각적 의미를 갖도록 하는 체계다.

Q. variant 이름을 blue, red로 해도 돼?

A.
권장하지 않는다. primary, secondary, danger처럼 역할 중심 이름이 좋다.

Q. danger variant는 언제 써?

A.
삭제, 탈퇴, 되돌릴 수 없는 위험 행동에 사용한다.

Q. size는 어떻게 나눠?

A.
기본적으로 sm, md, lg를 사용하고 필요 시 xs, xl을 추가한다.

Q. component state는 뭐야?

A.
default, hover, active, focus, disabled, loading, error, selected 같은 상태다.

Q. hover만 있으면 충분해?

A.
아니다. focus, disabled, loading, error 상태도 필요하다.

Q. Button Component 기준은 뭐야?

A.
variant, size, disabled, loading, type, focus style, accessible name 기준이 필요하다.

Q. Button 기본 type은 뭐가 좋아?

A.
일반 Button 컴포넌트는 `button`을 기본값으로 두는 것이 안전하다.

Q. form submit 버튼은 어떻게 해?

A.
명시적으로 `type="submit"`을 사용한다.

Q. loading button은 disabled 처리해야 해?

A.
대부분 그렇다. 중복 클릭과 중복 API 요청을 막기 위해 필요하다.

Q. 아이콘 버튼에는 뭐가 필요해?

A.
`aria-label` 또는 스크린 리더용 텍스트가 필요하다.

Q. Input Component 기준은 뭐야?

A.
label, name, value, onChange, disabled, errorMessage, helper text 기준이 필요하다.

Q. placeholder만 있으면 label은 없어도 돼?

A.
권장하지 않는다. placeholder는 입력 예시이고 label은 입력 항목의 이름이다.

Q. error input은 어떻게 표시해야 해?

A.
border 색상, error message, aria 속성 등을 함께 사용해야 한다.

Q. Form Field는 뭐야?

A.
label, input, helper text, error message를 하나의 구조로 묶는 component다.

Q. Form Field를 따로 만들면 좋아?

A.
반복되는 입력 구조를 일관되게 유지할 수 있어 좋다.

Q. Radio와 Select 중 뭐를 써야 해?

A.
옵션이 적고 비교가 필요하면 Radio, 옵션이 많으면 Select가 적합하다.

Q. Checkbox와 Switch는 뭐가 달라?

A.
Checkbox는 선택이나 동의에 적합하고, Switch는 즉시 적용되는 on/off 설정에 적합하다.

Q. Card Component는 언제 써?

A.
관련 정보를 하나의 시각적 그룹으로 묶어 보여줄 때 사용한다.

Q. Card 전체를 클릭 가능하게 해도 돼?

A.
가능하지만 내부 버튼과 충돌하지 않게 하고 접근성을 고려해야 한다.

Q. Badge와 Tag는 뭐가 달라?

A.
Badge는 상태나 수량을 표시하고, Tag는 카테고리나 키워드를 표시하는 경우가 많다.

Q. 상태 Badge는 색상만으로 표현해도 돼?

A.
안 된다. 텍스트도 함께 제공해야 한다.

Q. Alert와 Toast는 뭐가 달라?

A.
Alert는 화면 안에 고정되는 중요한 안내이고, Toast는 일시적인 작업 결과 알림이다.

Q. 중요한 오류를 Toast만으로 보여줘도 돼?

A.
권장하지 않는다. 화면 내 Error State도 함께 제공하는 것이 좋다.

Q. Modal에는 꼭 닫기 버튼이 필요해?

A.
필요하다. 사용자가 명확하게 닫을 수 있어야 한다.

Q. Modal 접근성에서 중요한 것은?

A.
dialog 역할, title 연결, focus 관리, keyboard 조작이다.

Q. Tabs는 언제 써?

A.
같은 페이지 안에서 관련 있는 콘텐츠 묶음을 전환할 때 사용한다.

Q. Tab 상태를 URL에 넣어야 해?

A.
공유, 새로고침 유지, 뒤로가기 지원이 필요하면 URL query나 path로 관리할 수 있다.

Q. Pagination과 Infinite Scroll 중 뭐가 좋아?

A.
검색 결과처럼 위치와 페이지 공유가 중요하면 Pagination, 피드처럼 계속 탐색하는 UX는 Infinite Scroll이 적합하다.

Q. Table은 언제 써?

A.
행과 열 구조의 데이터를 표시할 때 사용한다.

Q. 레이아웃을 만들려고 table을 써도 돼?

A.
안 된다. table은 표 데이터에 사용하고 레이아웃은 CSS Grid / Flexbox를 사용한다.

Q. 모바일에서 table은 어떻게 처리해?

A.
가로 스크롤, 카드형 변환, 주요 컬럼만 표시 등 프로젝트 기준을 정해야 한다.

Q. Loading State는 왜 필요해?

A.
사용자가 화면이 멈췄는지 처리 중인지 알 수 있어야 하기 때문이다.

Q. Skeleton은 언제 써?

A.
카드나 목록처럼 로딩 후 구조가 예상 가능한 콘텐츠에 적합하다.

Q. Empty State는 뭐야?

A.
요청은 성공했지만 표시할 데이터가 없을 때 보여주는 UI 패턴이다.

Q. Empty State에는 무엇이 들어가야 해?

A.
상태 설명, 이유 또는 맥락, 다음 행동이 들어가면 좋다.

Q. Error State는 뭐야?

A.
요청 실패나 처리 오류가 발생했을 때 문제와 복구 방법을 안내하는 UI 패턴이다.

Q. 에러는 console.log만 해도 돼?

A.
안 된다. 사용자에게 실패 상태와 복구 방법을 알려야 한다.

Q. Success State는 언제 필요해?

A.
저장, 삭제, 로그인, 회원가입, 리뷰 등록 같은 작업 성공을 알려야 할 때 필요하다.

Q. 모든 성공에 Toast를 띄워도 돼?

A.
과하면 방해가 될 수 있다. 중요한 행동 중심으로 사용한다.

Q. Layout System은 왜 필요해?

A.
페이지마다 간격과 배치가 달라지는 것을 막고 일관된 화면 구조를 만들기 위해 필요하다.

Q. 컴포넌트에 margin을 직접 주면 안 돼?

A.
재사용 컴포넌트라면 외부 배치는 부모 layout이 담당하는 것이 좋다.

Q. Design System에도 반응형 기준이 필요해?

A.
필요하다. 컴포넌트와 레이아웃이 같은 breakpoint 기준을 공유해야 한다.

Q. Theme System은 뭐야?

A.
같은 컴포넌트 구조를 유지하면서 색상과 시각 스타일을 전환하는 구조다.

Q. Dark Mode는 배경만 검게 바꾸면 돼?

A.
아니다. text, border, surface, disabled, hover, focus, icon까지 함께 조정해야 한다.

Q. Design System에 접근성을 넣어야 해?

A.
반드시 넣어야 한다. 공통 컴포넌트가 접근성을 만족하면 전체 화면 품질이 올라간다.

Q. aria를 많이 넣으면 접근성이 좋아져?

A.
아니다. Semantic HTML을 우선 사용하고 부족한 의미를 보완할 때만 aria를 사용한다.

Q. focus outline을 제거해도 돼?

A.
제거만 하면 안 된다. 반드시 대체 focus style을 제공해야 한다.

Q. 색상 contrast는 왜 중요해?

A.
저시력 사용자와 다양한 화면 환경에서 텍스트를 읽을 수 있어야 하기 때문이다.

Q. 색상만으로 상태를 표시해도 돼?

A.
안 된다. 텍스트, 아이콘, 메시지 등 추가 정보가 필요하다.

Q. UI Text는 어떻게 작성해야 해?

A.
짧고 명확하며 사용자의 행동과 현재 상태를 알려줘야 한다.

Q. Button 텍스트는 어떻게 쓰는 게 좋아?

A.
저장, 삭제, 검색, 다시 시도처럼 사용자가 수행할 행동을 동사 중심으로 작성한다.

Q. Error Message는 어떻게 작성해?

A.
사용자가 이해할 수 있는 문장으로 실패 이유와 다음 행동을 안내한다.

Q. Design System Documentation에는 무엇이 들어가?

A.
Component purpose, anatomy, props, variants, sizes, states, accessibility, usage, do, don’t, examples가 들어가면 좋다.

Q. 모든 컴포넌트를 문서화해야 해?

A.
자주 쓰는 핵심 컴포넌트부터 문서화하는 것이 현실적이다.

Q. 예제 코드는 길수록 좋아?

A.
아니다. 짧고 검색 가능한 예제가 RAG 문서에 적합하다.

Q. Design System 컴포넌트 구현 기준은 뭐야?

A.
props API, variant, size, state, accessibility, token 기반 스타일, 테스트 가능성이 명확해야 한다.

Q. Compound Component 패턴은 꼭 써야 해?

A.
필수는 아니다. 복잡한 컴포넌트에서 조합 유연성이 필요할 때 적합하다.

Q. Review Agent는 Design System에서 뭘 봐야 해?

A.
Token, Component Spec, State, Accessibility, Responsive, Theme, Documentation 기준을 확인해야 한다.

Q. 디자인이 예쁘면 Design System 기준을 통과한 거야?

A.
아니다. 일관성, 재사용성, 접근성, 반응형, 문서화 기준까지 봐야 한다.

Q. PM Agent는 Design System을 어떻게 써?

A.
화면이 요구사항과 일치하는지, UI가 일관적인지, 사용자 흐름이 명확한지 판단하는 데 사용한다.

Q. Frontend Agent는 Design System을 어떻게 써?

A.
기존 token과 component spec을 사용해 임의 스타일 생성을 줄이고 일관된 UI를 생성한다.

Q. Frontend Agent가 임의로 새 버튼 스타일을 만들어도 돼?

A.
기존 variant로 해결할 수 없을 때만 가능하고, 새 variant 추가 이유를 명확히 해야 한다.

Q. Design System에서 가장 흔한 실수는?

A.
토큰 없이 직접 스타일을 작성하고, 공통 컴포넌트 기준 없이 버튼과 입력을 매번 새로 만드는 것이다.

Q. variant가 많아지면 좋은 거 아니야?

A.
아니다. variant가 너무 많으면 선택 기준이 흐려지고 유지보수가 어려워진다.

Q. Design System은 처음부터 완성해야 해?

A.
아니다. token과 핵심 컴포넌트부터 시작해 단계적으로 확장하는 것이 좋다.

Q. 개인 AI 프로젝트에서는 어느 정도 Design System이 적당해?

A.
Basic Token, Core Components, Feedback Pattern 기준까지 있으면 Frontend Agent가 일관된 UI를 만들기 좋다.

Q. Design System 최종 승인 기준은 뭐야?

A.
Token, Core Component, State, Accessibility, Responsive, Documentation 기준이 있어야 한다.

Q. Design System 문서가 Frontend Foundation 마지막 문서야?

A.
현재 계획된 Frontend Domain Rules 기준으로는 마지막 문서다.
