# Design System Advanced Domain Rules

---

# 1. Domain Purpose

## 1.1 Design System Advanced Domain 목적

### [개념]

Design System Advanced Domain 문서는 Frontend Agent / UI Agent / Review Agent / Architecture Review Agent용 RAG 문서 제작 규칙이다.

Design System은 제품 전반에서 일관된 UI / UX를 만들기 위한 디자인 원칙, 토큰, 컴포넌트, 패턴, 접근성, 문서화, 테스트, 운영 체계이다.

목적:

- 공통 UI 설계 지원
- Design Token 구조 설계 지원
- Component API 설계 지원
- Variant / Size / State 설계 지원
- Accessibility 기준 적용 지원
- Theming / Dark Mode 설계 지원
- Storybook 문서화 지원
- UI 테스트 기준 제공
- Frontend Architecture와 연계 지원
- Next.js / React 컴포넌트 구현 지원
- UI 코드 리뷰 지원
- 디자인 일관성 검수 지원

---

### [핵심]

우선순위:

1. Design System Purpose
2. Design Token
3. Component API
4. Base Component
5. Composite Component
6. Variant System
7. State Pattern
8. Theming / Dark Mode
9. Accessibility
10. Layout / Spacing
11. Typography
12. Icon / Asset
13. Form Component
14. Feedback Component
15. Overlay Component
16. Documentation / Storybook
17. Testing / Visual Regression
18. Governance / Versioning
19. Frontend Integration
20. Code Review Criteria

---

### [실무]

2026 실무 기준:

- React / TypeScript 기준 예제 우선
- Next.js App Router와 연계 가능하게 작성
- 디자인 토큰과 컴포넌트 구현을 분리
- 컴포넌트는 접근성을 기본값으로 포함
- Button / Input / Modal / Dialog / Form 같은 핵심 컴포넌트 우선
- Variant는 무분별하게 늘리지 않음
- 공통 UI에는 비즈니스 로직을 넣지 않음
- Feature 전용 UI와 Design System UI를 구분
- Storybook 또는 문서화 기준 포함
- 테스트 가능한 Component API 설계
- 디자인과 코드의 단일 기준 유지
- Agent가 UI 생성과 리뷰에 바로 사용할 수 있는 판단 기준 포함

---

### [FAQ]

Q. Design System 문서는 무엇을 위한 문서인가?

A.
Agent가 공통 UI, 디자인 토큰, 컴포넌트 API, 접근성, 테마, 테스트, 문서화 기준을 설계하고 리뷰하도록 돕는 RAG 문서 제작 규칙이다.

Q. Design System은 단순 UI 컴포넌트 모음인가?

A.
아니다. 토큰, 컴포넌트, 패턴, 접근성, 문서화, 운영 기준까지 포함하는 제품 UI의 공통 체계이다.

Q. Design System 문서는 Frontend Architecture와 어떻게 연결되나?

A.
Frontend Architecture가 구조와 레이어를 다룬다면, Design System은 Shared UI Layer의 컴포넌트 품질과 일관성 기준을 담당한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Design System Domain은 제품 UI의 일관성과 재사용성을 높이기 위한 설계 기준을 포함한다.

---

### [핵심]

포함 범위:

- Design System
- Design Token
- Color Token
- Typography Token
- Spacing Token
- Radius Token
- Shadow Token
- Z-index Token
- Motion Token
- Theme
- Dark Mode
- Component Library
- Base Component
- Composite Component
- Primitive Component
- Headless Component
- Component API
- Variant
- Size
- State
- Accessibility
- Semantic HTML
- ARIA
- Keyboard Navigation
- Focus Management
- Button
- Input
- Select
- Checkbox
- Radio
- Textarea
- Form Field
- Modal / Dialog
- Dropdown
- Tooltip
- Toast
- Badge
- Card
- Tabs
- Accordion
- Table
- Skeleton
- Loading
- Empty State
- Error State
- Icon System
- Layout System
- Storybook
- Visual Regression Test
- Component Test
- Documentation
- Governance
- Versioning

---

### [실무]

제외 범위:

- Figma 상세 사용법 전체
- CSS 기초 문법 전체
- React 기초 문법 전체
- Next.js App Router 상세 전체
- 비즈니스 Feature 컴포넌트 상세
- 브랜드 전략 심화
- 디자인 이론 장문 설명
- 애니메이션 라이브러리 심화
- Micro Frontend 심화
- Monorepo 패키지 배포 심화

단, Design System 구현과 연계되는 React / TypeScript / CSS / Storybook / Accessibility 기준은 포함 가능하다.

---

### [FAQ]

Q. Design System 문서에 CSS 기초도 포함해야 하나?

A.
전체 CSS 기초는 포함하지 않는다. 토큰, 테마, 컴포넌트 상태, 반응형, 접근성 구현에 필요한 CSS 기준만 포함한다.

Q. Feature 전용 컴포넌트도 Design System에 포함하나?

A.
반복 사용이 검증되고 비즈니스 로직이 제거된 경우에만 Design System으로 승격한다.

Q. Storybook은 필수인가?

A.
필수 도구는 아니지만 Design System 문서화, 상태 검증, 시각 테스트를 위해 강력히 권장한다.

---

# 3. Required Section Rules

## 3.1 문서 Section 구조

### [개념]

모든 Design System RAG 문서는 MASTER_RAG_RULES의 기본 Section 구조를 따른다.

---

### [핵심]

필수 Section:

- `[개념]`
- `[핵심]`
- `[실무]`
- `[FAQ]`

강력 권장 Section:

- `[Flow]`
- `[예제]`
- `[주의]`
- `[Best Practice]`
- `[Troubleshooting]`
- `[Checklist]`
- `[Comparison]`

---

### [실무]

Design System 문서는 UI 판단과 재사용 기준이 중요하므로 아래 Section을 적극 사용한다.

- `[Flow]`: Token → Component → Pattern → Page
- `[Comparison]`: Design Token vs CSS Variable, Base Component vs Feature Component
- `[Best Practice]`: 접근성, Variant 제한, API 일관성
- `[Troubleshooting]`: Variant 폭발, 스타일 불일치, 접근성 누락
- `[Checklist]`: 컴포넌트 출시 전 검수

---

### [FAQ]

Q. Design System 문서에 Comparison이 필요한 이유는?

A.
공통 UI로 승격할지, Feature 내부에 둘지, Token으로 뺄지 판단해야 하므로 비교 기준이 필요하다.

Q. `[FAQ]` 대신 `[면접]` 섹션을 써도 되나?

A.
안 된다. MASTER_RAG_RULES에 따라 반드시 `[FAQ]`를 사용한다.

---

# 4. Design System Principles Rules

## 4.1 Design System 원칙

### [개념]

Design System 원칙은 UI가 커져도 일관성, 접근성, 재사용성, 유지보수성을 유지하기 위한 기준이다.

---

### [핵심]

필수 원칙:

- Consistency
- Accessibility First
- Token-based Design
- Reusable Component
- Predictable API
- Composition
- Scalability
- Maintainability
- Documentation
- Testability
- Low Business Coupling
- Clear Ownership
- Design-Code Alignment
- Progressive Adoption

---

### [실무]

설계 기준:

- 디자인 값은 토큰으로 관리
- 컴포넌트 API는 예측 가능하게 설계
- 공통 컴포넌트에 비즈니스 로직 금지
- 접근성은 옵션이 아니라 기본 요구사항
- Variant는 제품에서 실제로 필요한 조합만 제공
- 컴포넌트 상태는 명확히 문서화
- 디자인 변경이 코드 전체에 퍼지지 않도록 토큰화
- 재사용 가능성보다 명확성과 안정성 우선
- 공통화는 반복 사용이 확인된 후 진행
- 문서와 실제 구현이 어긋나지 않도록 관리

---

### [FAQ]

Q. Design System에서 가장 중요한 원칙은?

A.
일관성, 접근성, 토큰 기반 설계, 예측 가능한 컴포넌트 API이다.

Q. 공통 컴포넌트는 무조건 많이 만들수록 좋은가?

A.
아니다. 실제 반복 사용이 확인되고 비즈니스 로직이 제거된 컴포넌트만 공통화하는 것이 좋다.

Q. Design System은 처음부터 완성해야 하나?

A.
아니다. 핵심 컴포넌트와 토큰부터 시작해 제품 요구에 따라 점진적으로 확장한다.

---

# 5. Design Token Rules

## 5.1 Design Token 구조

### [개념]

Design Token은 색상, 타이포그래피, 간격, radius, shadow, z-index, motion 같은 디자인 값을 이름 있는 변수로 관리하는 방식이다.

---

### [핵심]

필수 포함:

- Design Token
- Primitive Token
- Semantic Token
- Component Token
- Color Token
- Typography Token
- Spacing Token
- Radius Token
- Shadow Token
- Z-index Token
- Motion Token
- CSS Variable
- Theme Token

Token Layer:

```text
Primitive Token
→ Semantic Token
→ Component Token
→ Component Style
```

예시:

```css
:root {
  --color-blue-500: #3b82f6;
  --color-background-primary: #ffffff;
  --color-text-primary: #111827;
  --space-4: 1rem;
  --radius-md: 0.5rem;
}
```

---

### [실무]

Token 작성 기준:

- Primitive Token은 원시 값
- Semantic Token은 역할 기반 이름
- Component Token은 특정 컴포넌트 적용 값
- 컴포넌트는 가능하면 Semantic Token 사용
- 색상 이름보다 역할 이름 우선
- Dark Mode는 Semantic Token 재매핑으로 처리
- Magic Number 직접 사용 지양
- Token 이름은 일관된 규칙 사용
- 변경 가능성이 큰 값은 Token으로 추상화
- 너무 세분화된 Token은 관리 비용 증가

Token 예시:

| 유형      | 예시                 | 목적             |
| --------- | -------------------- | ---------------- |
| Primitive | `blue-500`           | 원시 팔레트      |
| Semantic  | `background-primary` | 역할 기반 색상   |
| Component | `button-primary-bg`  | 컴포넌트 전용 값 |
| Spacing   | `space-4`            | 간격             |
| Radius    | `radius-md`          | 둥근 모서리      |

---

### [FAQ]

Q. Design Token은 왜 필요한가?

A.
디자인 값을 코드 전체에 직접 쓰지 않고 중앙에서 관리해 일관성과 변경 용이성을 높이기 위해 필요하다.

Q. Primitive Token과 Semantic Token 차이는?

A.
Primitive Token은 원시 색상이나 크기 값이고, Semantic Token은 UI 역할을 나타내는 값이다.

Q. 컴포넌트에서 원시 색상을 직접 써도 되나?

A.
가능하면 피한다. 컴포넌트는 Semantic Token이나 Component Token을 사용하는 것이 좋다.

---

# 6. Color System Rules

## 6.1 Color Token 설계

### [개념]

Color System은 브랜드 색상, 배경, 텍스트, Border, 상태 색상, 다크 모드 색상을 일관되게 관리하는 체계이다.

---

### [핵심]

필수 포함:

- Brand Color
- Neutral Color
- Semantic Color
- Background Color
- Text Color
- Border Color
- Surface Color
- State Color
- Success
- Warning
- Error
- Info
- Disabled
- Focus Ring
- Dark Mode Color
- Contrast Ratio

---

### [실무]

Color Token 기준:

- 브랜드 색상과 의미 색상 분리
- 텍스트 색상은 배경 대비 확인
- Error / Warning / Success는 의미 기반 Token 사용
- Hover / Active / Disabled 상태 색상 포함
- Focus Ring 색상 포함
- Dark Mode에서 단순 반전 금지
- 색상만으로 상태 전달 금지
- 차트 색상과 UI 색상 역할 분리 가능
- 접근성 기준을 만족하지 않는 조합 금지

예시:

```text
color.background.primary
color.background.secondary
color.text.primary
color.text.muted
color.border.default
color.intent.success
color.intent.warning
color.intent.error
color.focus.ring
```

---

### [FAQ]

Q. 색상 Token은 어떻게 이름 짓는 게 좋나?

A.
`blue-500` 같은 원시 이름보다 `text-primary`, `background-primary`, `intent-error`처럼 역할 기반 이름을 우선한다.

Q. 색상만으로 에러 상태를 표시해도 되나?

A.
안 된다. 색상 외에 텍스트, 아이콘, ARIA 속성 등 보조 정보를 함께 제공해야 한다.

Q. Dark Mode는 색상을 반전하면 되나?

A.
아니다. Semantic Token을 기준으로 별도 매핑해 명도, 대비, 브랜드 톤을 조정해야 한다.

---

# 7. Typography Rules

## 7.1 Typography System

### [개념]

Typography System은 글꼴, 크기, 줄 높이, 굵기, 자간, 제목 계층, 본문 계층을 일관되게 관리하는 체계이다.

---

### [핵심]

필수 포함:

- Font Family
- Font Size
- Font Weight
- Line Height
- Letter Spacing
- Heading
- Body Text
- Caption
- Label
- Code Font
- Responsive Typography
- Readability
- Text Truncation

예시:

```text
font.family.sans
font.family.mono
font.size.sm
font.size.md
font.size.lg
font.weight.regular
font.weight.semibold
lineHeight.normal
lineHeight.relaxed
```

---

### [실무]

Typography 기준:

- 제목 계층은 의미 있는 HTML Heading과 연결
- 시각 크기와 Semantic Heading을 혼동하지 않기
- 본문 가독성을 위한 line-height 확보
- 버튼 / 라벨 / 캡션 크기 정의
- 모바일과 데스크톱 Typography 차이 고려
- 긴 텍스트는 줄바꿈 / 말줄임 기준 포함
- 폰트 로딩 성능 고려
- 숫자 / 코드 / 테이블에는 별도 폰트 규칙 고려

---

### [FAQ]

Q. Typography Token은 왜 필요한가?

A.
페이지마다 임의의 폰트 크기를 쓰지 않고 제목, 본문, 라벨, 캡션을 일관되게 유지하기 위해 필요하다.

Q. Heading은 크기 기준인가 의미 기준인가?

A.
HTML Heading은 의미 구조 기준이다. 시각적 크기는 스타일로 조정할 수 있다.

Q. 본문 line-height는 왜 중요한가?

A.
가독성과 접근성에 직접 영향을 주기 때문이다.

---

# 8. Spacing and Layout Rules

## 8.1 Spacing / Layout System

### [개념]

Spacing System은 margin, padding, gap, grid, container, layout 간격을 일관되게 관리하는 체계이다.

---

### [핵심]

필수 포함:

- Spacing Token
- Margin
- Padding
- Gap
- Stack
- Inline
- Grid
- Container
- Section
- Breakpoint
- Responsive Layout
- Density
- Layout Rhythm

예시:

```text
space.1 = 0.25rem
space.2 = 0.5rem
space.4 = 1rem
space.6 = 1.5rem
space.8 = 2rem
```

---

### [실무]

Spacing 기준:

- 임의의 pixel 값 남용 금지
- 반복되는 간격은 Token 사용
- 내부 간격은 padding, 요소 간 간격은 gap 사용 권장
- Layout 컴포넌트는 Stack / Grid / Container로 추상화 가능
- 모바일 / 데스크톱 간격 차이 고려
- 밀도 높은 UI와 여백 중심 UI 기준 분리 가능
- 섹션 간격과 컴포넌트 내부 간격 구분
- 디자인 시안과 코드 Token 매핑 유지

---

### [FAQ]

Q. Spacing Token은 왜 필요한가?

A.
화면마다 임의의 간격을 쓰지 않고 일관된 UI 리듬을 유지하기 위해 필요하다.

Q. margin과 gap 중 무엇을 써야 하나?

A.
요소 간 반복 간격은 gap이 명확하고, 개별 위치 조정에는 margin을 사용할 수 있다.

Q. Layout 컴포넌트는 언제 만들면 되나?

A.
Stack, Grid, Container처럼 반복되는 배치 패턴이 많아질 때 만들면 좋다.

---

# 9. Component Classification Rules

## 9.1 Component 분류 기준

### [개념]

Design System Component는 책임과 재사용 범위에 따라 Primitive, Base, Composite, Pattern, Feature Component로 구분한다.

---

### [핵심]

분류:

| 유형                | 설명                  | 예시                      |
| ------------------- | --------------------- | ------------------------- |
| Primitive           | 낮은 수준의 기본 요소 | Box, Text, VisuallyHidden |
| Base Component      | 독립 공통 UI          | Button, Input, Badge      |
| Composite Component | 여러 Base 조합        | FormField, SearchBox      |
| Pattern Component   | 특정 UX 패턴          | EmptyState, ErrorState    |
| Feature Component   | 비즈니스 기능 UI      | LoginForm, PaymentSummary |

---

### [실무]

분류 기준:

- Primitive는 스타일 시스템 기반
- Base Component는 비즈니스 로직 없음
- Composite Component는 여러 Base를 조합
- Pattern Component는 반복 UX 패턴 제공
- Feature Component는 Design System이 아니라 Feature 내부에 둠
- Feature Component가 반복되면 비즈니스 로직 제거 후 승격 검토
- 컴포넌트 책임과 위치를 문서화

---

### [FAQ]

Q. Base Component와 Feature Component 차이는?

A.
Base Component는 비즈니스 로직 없는 공통 UI이고, Feature Component는 특정 기능이나 도메인에 종속된 UI이다.

Q. LoginForm은 Design System 컴포넌트인가?

A.
일반적으로 아니다. LoginForm은 인증 Feature에 종속된 Feature Component이다.

Q. FormField는 Design System에 들어갈 수 있나?

A.
가능하다. Label, Input, Error Message를 조합한 반복 UI 패턴이면 Composite Component로 둘 수 있다.

---

# 10. Component API Rules

## 10.1 Component Props 설계

### [개념]

Component API는 컴포넌트를 사용하는 개발자가 예측 가능하고 안전하게 UI를 조합할 수 있도록 props, event, variant, state를 설계하는 규칙이다.

---

### [핵심]

필수 포함:

- Props API
- Required Props
- Optional Props
- Variant Props
- Size Props
- Boolean Props
- Callback Props
- Children
- Slot Props
- Controlled Props
- Uncontrolled Props
- Ref
- Accessibility Props
- TypeScript Type

예시:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "danger";
  size?: "sm" | "md" | "lg";
  disabled?: boolean;
  loading?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
};
```

---

### [실무]

Props 설계 기준:

- 필수와 선택 props 구분
- `variant`, `size`, `intent` 같은 명확한 props 사용
- Boolean Props 폭발 주의
- 콜백은 `onClick`, `onChange`, `onOpenChange`처럼 의도 중심
- `children`은 주요 콘텐츠에 사용
- `Slot Props`는 특정 위치 UI 주입에 사용
- Controlled / Uncontrolled API를 명확히 분리
- 접근성 관련 props 전달 가능하게 설계
- DOM props 확장 여부 결정
- 잘못된 조합은 TypeScript로 막을 수 있게 설계

---

### [FAQ]

Q. Component API에서 가장 중요한 것은?

A.
예측 가능성이다. 사용하는 사람이 props 이름과 조합만 보고 동작을 이해할 수 있어야 한다.

Q. Boolean Props가 많으면 왜 문제인가?

A.
조합 폭발이 발생하고 컴포넌트 내부 조건 분기가 복잡해진다.

Q. Callback 이름은 어떻게 짓는 게 좋나?

A.
`onSubmit`, `onChange`, `onOpenChange`, `onSelect`처럼 사용자 행동이나 상태 변경 의도를 드러내야 한다.

---

# 11. Variant System Rules

## 11.1 Variant / Size / Intent 설계

### [개념]

Variant System은 컴포넌트의 시각적 형태, 크기, 의미, 상태를 제한된 조합으로 제공하는 규칙이다.

---

### [핵심]

필수 포함:

- Variant
- Size
- Intent
- Tone
- State
- Disabled
- Loading
- Selected
- Active
- Focus
- Hover
- Compound Variant
- Default Variant

예시:

```text
Button
- variant: primary | secondary | ghost | outline
- size: sm | md | lg
- intent: default | danger
- state: default | hover | active | focus | disabled | loading
```

---

### [실무]

Variant 설계 기준:

- 제품에서 실제 필요한 조합만 제공
- Variant 이름은 시각보다 목적 중심으로 작성
- `danger`, `success` 등 의미 있는 intent 분리
- `size`는 spacing / typography와 연결
- 상태별 스타일은 Token 기반으로 작성
- Variant 조합이 많아지면 Compound Variant 검토
- 잘못된 variant 조합은 타입으로 제한 가능
- Feature 전용 variant를 Design System에 무분별하게 추가하지 않기

주의:

- 모든 요구를 variant로 해결하지 않기
- `isBlue`, `isLarge`, `isRounded` 같은 Boolean 스타일 props 남용 금지
- Variant가 많아지면 API 재설계 필요
- 커스텀 스타일 escape hatch는 신중히 제공

---

### [FAQ]

Q. Variant는 어떻게 정해야 하나?

A.
제품에서 반복되는 UI 의도와 상태를 기준으로 제한된 선택지를 제공한다.

Q. `primary`, `secondary`는 좋은 variant 이름인가?

A.
일반적인 버튼 우선순위 표현에는 적합하다. 위험 동작은 `danger` 같은 intent로 분리하는 것이 좋다.

Q. Feature마다 필요한 스타일을 variant로 계속 추가해도 되나?

A.
권장하지 않는다. Feature 전용 요구는 Feature 내부 스타일로 처리하고 반복되면 Design System 승격을 검토한다.

---

# 12. State Pattern Rules

## 12.1 Component State 설계

### [개념]

Component State Pattern은 컴포넌트가 가질 수 있는 default, hover, focus, active, disabled, loading, error, selected 상태를 일관되게 정의하는 규칙이다.

---

### [핵심]

필수 상태:

- Default
- Hover
- Focus
- Focus Visible
- Active
- Disabled
- Loading
- Selected
- Checked
- Expanded
- Error
- Success
- Readonly
- Required

상태 기준:

```text
Default
→ Hover
→ Focus
→ Active
→ Disabled
→ Loading
→ Error
```

---

### [실무]

상태 작성 기준:

- 모든 interactive component는 focus 상태 필수
- Disabled 상태는 시각적 / 동작적으로 모두 비활성
- Loading 상태는 중복 클릭 방지
- Error 상태는 색상 + 메시지 + 접근성 연결
- Selected / Checked / Expanded는 ARIA 속성과 연결
- Readonly와 Disabled를 구분
- Required는 label / validation과 연결
- 상태 조합 우선순위 문서화
- Keyboard interaction 상태 포함

---

### [FAQ]

Q. Focus 상태는 꼭 필요하나?

A.
필수이다. 키보드 사용자가 현재 위치를 알 수 있어야 한다.

Q. Disabled와 Readonly 차이는?

A.
Disabled는 상호작용과 제출에서 제외될 수 있고, Readonly는 값을 볼 수 있지만 수정하지 못하는 상태이다.

Q. Error 상태는 색상만 바꾸면 되나?

A.
아니다. 에러 메시지, `aria-invalid`, `aria-describedby` 같은 접근성 연결이 필요하다.

---

# 13. Button Component Rules

## 13.1 Button 설계

### [개념]

Button은 사용자의 동작 실행을 담당하는 핵심 Design System 컴포넌트이다.

---

### [핵심]

필수 포함:

- Button
- Variant
- Size
- Intent
- Disabled
- Loading
- Icon Button
- Full Width
- Button Type
- Click Handler
- Focus Visible
- Keyboard Interaction
- Accessible Name

예시:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "ghost";
  intent?: "default" | "danger";
  size?: "sm" | "md" | "lg";
  loading?: boolean;
  disabled?: boolean;
  type?: "button" | "submit" | "reset";
  children: React.ReactNode;
  onClick?: () => void;
};
```

---

### [실무]

Button 기준:

- 기본 `type`은 의도 명확히 지정
- Form 내부 Button은 `submit` 여부 명확화
- Loading 중 중복 클릭 방지
- Disabled와 Loading 스타일 구분
- Icon-only Button은 `aria-label` 필수
- 위험 동작은 `intent="danger"` 사용
- Link 이동에는 Button 대신 Link 사용
- Focus Ring 제공
- 클릭 가능한 `div`로 Button 대체 금지

---

### [FAQ]

Q. Button과 Link는 어떻게 구분하나?

A.
동작 실행은 Button, 페이지 이동은 Link를 사용한다.

Q. Icon Button에는 무엇이 필요하나?

A.
눈에 보이는 텍스트가 없으므로 `aria-label` 같은 accessible name이 필요하다.

Q. Button 기본 type은 왜 중요하나?

A.
Form 안에서 의도치 않게 submit이 발생할 수 있으므로 명확히 지정해야 한다.

---

# 14. Form Component Rules

## 14.1 Form / Input / Field 설계

### [개념]

Form Component는 사용자 입력, 검증, 에러 메시지, 접근성 연결을 일관되게 제공하는 컴포넌트 체계이다.

---

### [핵심]

필수 포함:

- Form
- FormField
- Label
- Input
- Textarea
- Select
- Checkbox
- Radio
- Helper Text
- Error Message
- Required
- Disabled
- Readonly
- Validation
- `aria-invalid`
- `aria-describedby`

예시:

```tsx
type FormFieldProps = {
  label: string;
  required?: boolean;
  error?: string;
  helperText?: string;
  children: React.ReactNode;
};
```

---

### [실무]

Form Component 기준:

- Input에는 Label 연결 필수
- Error Message는 Input과 연결
- Required 표시는 시각적 표시와 검증을 구분
- Client Validation은 UX용
- Server Validation 결과 표시 구조 포함
- Disabled와 Readonly 구분
- Placeholder를 Label 대체로 사용 금지
- Checkbox / Radio는 그룹 Label 고려
- Field 단위 Error와 Form 전체 Error 구분
- Form Submit 중 Pending 상태 표시

---

### [FAQ]

Q. Placeholder를 Label 대신 써도 되나?

A.
안 된다. Placeholder는 입력 힌트이고 Label을 대체할 수 없다.

Q. Form Error는 어떻게 표시해야 하나?

A.
Field 단위 에러는 해당 Input과 연결하고, 전체 에러는 Form 상단이나 Summary로 표시한다.

Q. Client Validation만 해도 되나?

A.
안 된다. Client Validation은 UX용이고 서버 검증이 필수이다.

---

# 15. Overlay Component Rules

## 15.1 Modal / Dialog / Dropdown / Tooltip

### [개념]

Overlay Component는 화면 위에 떠서 추가 정보, 선택지, 확인, 입력을 제공하는 컴포넌트이다.

---

### [핵심]

필수 포함:

- Modal
- Dialog
- Alert Dialog
- Dropdown
- Popover
- Tooltip
- Focus Trap
- Escape Key
- Backdrop
- Portal
- Z-index
- Scroll Lock
- ARIA Role
- Keyboard Navigation

---

### [실무]

Overlay 기준:

- Dialog는 focus trap 필요
- Dialog 열릴 때 적절한 요소로 focus 이동
- Dialog 닫힐 때 trigger로 focus 복귀
- Escape 닫기 동작 고려
- Backdrop 클릭 닫기 여부 명확화
- Alert Dialog는 위험 동작 확인에 사용
- Dropdown은 키보드 탐색 지원
- Tooltip은 필수 정보 전달 수단으로 사용하지 않기
- z-index Token 사용
- Body scroll lock 처리
- Portal 사용 시 테스트와 접근성 확인

---

### [FAQ]

Q. Modal과 Dialog는 접근성에서 무엇이 중요한가?

A.
focus trap, focus return, keyboard navigation, 적절한 role과 label이 중요하다.

Q. Tooltip에 중요한 정보를 넣어도 되나?

A.
권장하지 않는다. Tooltip은 보조 정보용이며 필수 정보는 항상 화면에 표시되어야 한다.

Q. z-index는 어떻게 관리해야 하나?

A.
임의 숫자를 쓰지 않고 z-index Token으로 계층을 관리한다.

---

# 16. Feedback Component Rules

## 16.1 Toast / Alert / Badge / Skeleton

### [개념]

Feedback Component는 사용자에게 성공, 실패, 진행 중, 상태, 개수, 알림을 전달하는 UI 컴포넌트이다.

---

### [핵심]

필수 포함:

- Toast
- Alert
- Banner
- Badge
- Tag
- Skeleton
- Spinner
- Progress
- Empty State
- Error State
- Success Message
- Warning Message
- Info Message
- Dismissible
- Live Region

---

### [실무]

Feedback 기준:

- Toast는 짧은 결과 알림에 사용
- 중요한 오류는 Toast만으로 처리하지 않음
- Alert는 화면 내 지속 메시지에 사용
- Skeleton은 초기 로딩 UI에 적합
- Spinner만 단독 사용하면 맥락 부족 가능
- Badge는 상태나 개수 표시
- Empty State는 다음 행동을 안내
- Error State는 재시도 가능 여부 표시
- 스크린 리더가 상태 변화를 인식할 수 있게 처리
- 자동 사라지는 메시지는 충분한 시간 제공

---

### [FAQ]

Q. Toast는 언제 사용하나?

A.
저장 성공, 복사 완료, 짧은 실패 알림처럼 일시적인 결과 전달에 사용한다.

Q. 중요한 에러를 Toast만으로 보여줘도 되나?

A.
권장하지 않는다. 사용자가 놓칠 수 있으므로 화면 내 Error State나 Alert를 함께 고려한다.

Q. Skeleton과 Spinner 차이는?

A.
Skeleton은 로딩될 UI 형태를 미리 보여주고, Spinner는 단순 진행 중 상태를 표시한다.

---

# 17. Navigation Component Rules

## 17.1 Tabs / Breadcrumb / Pagination

### [개념]

Navigation Component는 사용자가 화면 구조를 이해하고 이동하거나 콘텐츠 범위를 전환하도록 돕는 컴포넌트이다.

---

### [핵심]

필수 포함:

- Tabs
- Breadcrumb
- Pagination
- Sidebar
- Navbar
- Menu
- Stepper
- Link
- Active State
- Current Page
- Keyboard Navigation
- ARIA Current
- Route Integration

---

### [실무]

Navigation 기준:

- 페이지 이동은 Link 사용
- 현재 위치는 active / current 상태로 표시
- Breadcrumb은 계층 위치를 나타냄
- Pagination은 현재 페이지와 전체 범위 표시
- Tabs는 같은 문맥 내 콘텐츠 전환에 사용
- URL과 동기화해야 하는 Tabs는 Routing 기준 설계
- Menu는 키보드 이동 지원
- Sidebar는 현재 Route와 연결
- Stepper는 진행 단계와 완료 상태 표시

---

### [FAQ]

Q. Tabs와 Navigation Link 차이는?

A.
Tabs는 같은 문맥 내 콘텐츠 전환이고, Link는 페이지나 Route 이동이다.

Q. Pagination에서 중요한 정보는?

A.
현재 페이지, 전체 페이지 또는 다음 / 이전 가능 여부를 명확히 보여줘야 한다.

Q. 현재 페이지는 어떻게 표시해야 하나?

A.
시각적 active 상태와 함께 `aria-current` 같은 접근성 속성을 고려한다.

---

# 18. Table and Data Display Rules

## 18.1 Table / List / Card 데이터 표시

### [개념]

Data Display Component는 목록, 표, 카드, 상세 정보처럼 데이터를 읽기 쉽게 표현하는 컴포넌트이다.

---

### [핵심]

필수 포함:

- Table
- List
- Card
- Description List
- Data Grid
- Sort
- Filter
- Empty State
- Loading State
- Error State
- Pagination
- Responsive Table
- Column Alignment
- Row Action

---

### [실무]

Data Display 기준:

- 표 형태 데이터는 Semantic Table 사용
- 숫자는 정렬과 단위 표시 기준 포함
- Action Column은 명확히 분리
- Empty / Loading / Error 상태 포함
- 모바일에서는 카드형 전환 고려
- 정렬 / 필터 상태는 URL과 연계 가능
- 행 선택 상태는 keyboard 접근성 고려
- 대량 데이터는 Pagination 또는 Virtualization 고려
- 컬럼 정의는 재사용 가능한 구조 검토

---

### [FAQ]

Q. Table은 언제 사용하나?

A.
행과 열의 관계가 중요한 구조화된 데이터를 비교하거나 관리할 때 사용한다.

Q. 모바일에서 Table은 어떻게 처리하나?

A.
중요 컬럼 중심으로 줄이거나 카드형 레이아웃으로 전환할 수 있다.

Q. 목록이 비어 있으면 그냥 아무것도 안 보여줘도 되나?

A.
아니다. Empty State를 제공해 데이터가 없다는 사실과 다음 행동을 알려주는 것이 좋다.

---

# 19. Accessibility Rules

## 19.1 Design System 접근성 기준

### [개념]

Accessibility는 모든 사용자가 키보드, 스크린 리더, 다양한 입력 장치, 다양한 시각 조건에서 UI를 사용할 수 있도록 보장하는 기준이다.

---

### [핵심]

필수 포함:

- Semantic HTML
- ARIA
- Keyboard Navigation
- Focus Management
- Focus Visible
- Accessible Name
- Color Contrast
- Screen Reader
- Label
- Error Message
- Live Region
- Reduced Motion
- Touch Target
- Button vs Link
- Dialog Accessibility

---

### [실무]

접근성 기준:

- Semantic HTML 우선
- ARIA는 필요한 경우에만 정확히 사용
- 모든 interactive component는 키보드 접근 가능
- Focus Ring 제거 금지
- Icon-only Button은 accessible name 필수
- Form Field는 Label과 Error 연결
- 색상만으로 상태 전달 금지
- Dialog는 focus trap과 focus return 제공
- Motion은 reduced motion 설정 고려
- Touch Target 크기 고려
- Error / Success 알림은 스크린 리더 대응 고려
- 컴포넌트 문서에 접근성 요구사항 포함

---

### [FAQ]

Q. Design System에서 접근성은 선택 사항인가?

A.
아니다. 공통 컴포넌트에 접근성 문제가 있으면 제품 전체에 문제가 확산된다.

Q. ARIA를 많이 쓰면 접근성이 좋아지나?

A.
아니다. Semantic HTML을 우선 사용하고 ARIA는 필요한 경우에만 정확히 사용해야 한다.

Q. Focus Ring을 제거해도 되나?

A.
안 된다. 키보드 사용자가 현재 위치를 알 수 있어야 한다.

---

# 20. Theming and Dark Mode Rules

## 20.1 Theme / Dark Mode 설계

### [개념]

Theming은 디자인 토큰을 기반으로 제품의 시각적 스타일을 상황에 따라 전환하는 구조이다. Dark Mode는 대표적인 Theme 전환 사례이다.

---

### [핵심]

필수 포함:

- Theme
- Light Theme
- Dark Theme
- System Theme
- CSS Variable
- Semantic Token
- Theme Provider
- Theme Persistence
- Color Scheme
- Token Remapping
- Contrast
- Flash Prevention

예시:

```css
:root {
  --color-background-primary: #ffffff;
  --color-text-primary: #111827;
}

[data-theme="dark"] {
  --color-background-primary: #111827;
  --color-text-primary: #f9fafb;
}
```

---

### [실무]

Theme 기준:

- Theme 전환은 Semantic Token 재매핑 중심
- Dark Mode는 단순 색상 반전 금지
- 사용자 선택과 시스템 설정 우선순위 정의
- 선택한 Theme 저장 방식 결정
- 초기 렌더링 Flash 방지 고려
- 이미지 / 아이콘 / 차트 색상도 Theme 대응
- Focus / Error / Disabled 색상도 Theme별 확인
- 다크 모드 대비 확인
- Theme Provider 범위 명확히 설정

---

### [FAQ]

Q. Dark Mode는 어떻게 구현하는 게 좋나?

A.
Semantic Token을 CSS Variable로 정의하고 Theme별로 값을 재매핑하는 방식이 좋다.

Q. Dark Mode에서 색상을 단순 반전하면 안 되나?

A.
권장하지 않는다. 대비, 브랜드 톤, 상태 색상, 가독성이 깨질 수 있다.

Q. Theme Flash는 왜 발생하나?

A.
초기 HTML 렌더링과 클라이언트 Theme 적용 시점이 달라 화면이 잠깐 다른 Theme로 보일 때 발생한다.

---

# 21. Icon and Asset Rules

## 21.1 Icon / Asset System

### [개념]

Icon and Asset System은 아이콘, 로고, 일러스트, 이미지 같은 시각 자산을 일관된 크기, 색상, 의미, 접근성 기준으로 관리하는 체계이다.

---

### [핵심]

필수 포함:

- Icon
- SVG
- Icon Size
- Icon Color
- Decorative Icon
- Informative Icon
- Accessible Name
- Logo
- Illustration
- Image Asset
- Asset Naming
- Optimization
- Sprite / Component Icon

---

### [실무]

Icon 기준:

- 아이콘 크기 Token 사용
- 색상은 currentColor 또는 Token 사용
- 장식용 아이콘은 스크린 리더에서 숨김
- 의미 있는 아이콘은 accessible name 제공
- Icon-only Button은 `aria-label` 필수
- 로고와 제품 아이콘은 별도 관리
- SVG 최적화 적용
- 아이콘 이름은 의미 중심으로 작성
- 같은 의미의 아이콘 중복 방지
- 이미지 자산은 최적화와 반응형 고려

---

### [FAQ]

Q. Icon-only Button에는 무엇이 필요한가?

A.
텍스트가 없으므로 `aria-label` 같은 accessible name이 필요하다.

Q. 장식용 아이콘도 스크린 리더가 읽어야 하나?

A.
아니다. 의미가 없는 장식용 아이콘은 스크린 리더에서 숨기는 것이 좋다.

Q. 아이콘 색상은 어떻게 관리하나?

A.
가능하면 `currentColor`나 Semantic Color Token을 사용해 텍스트 색상과 일관되게 관리한다.

---

# 22. Responsive Design Rules

## 22.1 반응형 Design System

### [개념]

Responsive Design은 다양한 화면 크기와 입력 환경에서 컴포넌트와 레이아웃이 자연스럽게 동작하도록 설계하는 기준이다.

---

### [핵심]

필수 포함:

- Breakpoint
- Mobile First
- Responsive Token
- Container
- Grid
- Stack
- Adaptive Layout
- Touch Target
- Responsive Typography
- Responsive Spacing
- Responsive Table
- Viewport
- Density

---

### [실무]

반응형 기준:

- Mobile First 기준 권장
- Breakpoint는 제품 레이아웃 기준으로 정의
- 단순 디바이스 이름보다 레이아웃 전환 기준 사용
- Touch Target 크기 고려
- 모바일에서 Hover 의존 금지
- Typography와 Spacing도 반응형 조정 가능
- Table은 모바일 대응 전략 포함
- Sidebar / Navigation은 작은 화면 전략 필요
- Modal은 모바일에서 Drawer로 대체 가능
- 콘텐츠 우선순위에 따라 숨김 / 재배치 결정

---

### [FAQ]

Q. Breakpoint는 어떻게 정해야 하나?

A.
특정 디바이스보다 레이아웃이 깨지는 지점과 콘텐츠 우선순위를 기준으로 정하는 것이 좋다.

Q. 모바일에서 Hover UI를 써도 되나?

A.
주의해야 한다. 터치 환경에서는 Hover가 안정적으로 동작하지 않을 수 있다.

Q. 모바일에서 Modal은 항상 좋은가?

A.
아니다. 작은 화면에서는 Drawer나 전체 화면 Dialog가 더 적합할 수 있다.

---

# 23. Motion Rules

## 23.1 Motion / Animation 기준

### [개념]

Motion System은 전환, 피드백, 강조, 로딩 등 UI 움직임을 일관되고 접근성 있게 관리하는 기준이다.

---

### [핵심]

필수 포함:

- Motion Token
- Duration
- Easing
- Transition
- Enter Animation
- Exit Animation
- Loading Animation
- Reduced Motion
- Interaction Feedback
- Layout Shift
- Performance

예시:

```text
motion.duration.fast
motion.duration.normal
motion.duration.slow
motion.easing.standard
motion.easing.emphasized
```

---

### [실무]

Motion 기준:

- Motion은 의미 있는 피드백에 사용
- 과도한 애니메이션 금지
- Duration과 easing은 Token으로 관리
- Loading Animation은 너무 긴 반복 피로감 주의
- Layout Shift를 유발하는 Motion 주의
- `prefers-reduced-motion` 고려
- 중요한 정보 전달을 Motion에만 의존 금지
- 성능을 위해 transform / opacity 중심 사용 권장
- Overlay enter / exit 기준 문서화

---

### [FAQ]

Q. Motion Token은 왜 필요한가?

A.
화면마다 다른 속도와 easing을 쓰지 않고 일관된 움직임 경험을 제공하기 위해 필요하다.

Q. 애니메이션은 많을수록 좋은가?

A.
아니다. 과도한 Motion은 피로감과 성능 문제를 만들 수 있다.

Q. Reduced Motion은 왜 고려해야 하나?

A.
움직임에 민감한 사용자가 불편을 느끼지 않도록 하기 위해 필요하다.

---

# 24. Documentation Rules

## 24.1 Storybook / Component Docs

### [개념]

Design System Documentation은 컴포넌트 사용법, Props, Variant, 상태, 접근성, 예제를 문서화해 팀이 일관되게 사용할 수 있게 하는 체계이다.

---

### [핵심]

필수 포함:

- Storybook
- Component Docs
- Props Table
- Variant Example
- State Example
- Accessibility Notes
- Usage Guideline
- Do / Don't
- Changelog
- Migration Guide
- Design Reference
- Code Example

---

### [실무]

문서화 기준:

- 컴포넌트 목적 설명
- 사용해야 하는 경우 / 피해야 하는 경우 작성
- Props와 기본값 표시
- Variant / Size / State 예제 제공
- 접근성 요구사항 문서화
- Keyboard Interaction 문서화
- Do / Don't 예시 포함
- 디자인 시안 링크 또는 참고 정보 연결
- 변경 이력 기록
- Deprecated 컴포넌트는 대체안 제공
- 문서와 실제 구현 불일치 방지

---

### [FAQ]

Q. Design System 문서에는 무엇을 써야 하나?

A.
컴포넌트 목적, 사용 기준, Props, Variant, 상태, 접근성, 예제, 금지 사용법을 포함해야 한다.

Q. Storybook은 어떤 역할을 하나?

A.
컴포넌트를 독립적으로 확인하고 상태별 예제와 문서를 제공하는 역할을 한다.

Q. Do / Don't 문서는 왜 필요한가?

A.
잘못된 사용을 줄이고 컴포넌트 의도를 명확히 전달하기 위해 필요하다.

---

# 25. Testing Rules

## 25.1 Design System 테스트 기준

### [개념]

Design System Testing은 공통 컴포넌트가 다양한 상태, 접근성, 시각적 회귀, 상호작용에서 안정적으로 동작하는지 검증하는 기준이다.

---

### [핵심]

필수 포함:

- Unit Test
- Component Test
- Accessibility Test
- Visual Regression Test
- Interaction Test
- Keyboard Test
- Snapshot Test
- Story Test
- Cross-browser Test
- Theme Test
- Responsive Test

---

### [실무]

테스트 기준:

- Button / Input / Modal 같은 핵심 컴포넌트 우선
- Variant / Size / State별 렌더링 확인
- Keyboard Interaction 테스트
- Focus 이동 테스트
- ARIA 속성 확인
- Disabled / Loading / Error 상태 검증
- Theme별 시각 검증
- 모바일 / 데스크톱 반응형 확인
- Visual Regression Test로 의도치 않은 스타일 변경 감지
- Snapshot Test 남용 금지
- 테스트는 구현 세부보다 사용자 행동 기준

---

### [FAQ]

Q. Design System에서 무엇을 테스트해야 하나?

A.
컴포넌트 상태, variant, 접근성, keyboard interaction, theme, visual regression을 테스트해야 한다.

Q. Visual Regression Test는 왜 필요한가?

A.
공통 컴포넌트 스타일 변경이 제품 전체에 영향을 줄 수 있기 때문에 의도치 않은 시각 변경을 잡기 위해 필요하다.

Q. Snapshot Test만으로 충분한가?

A.
아니다. 상호작용, 접근성, 시각 회귀 테스트가 함께 필요하다.

---

# 26. Governance and Versioning Rules

## 26.1 운영 / 버전 관리

### [개념]

Design System Governance는 컴포넌트 추가, 변경, 폐기, 버전 관리, 리뷰 기준을 정해 Design System이 무질서하게 확장되지 않도록 관리하는 체계이다.

---

### [핵심]

필수 포함:

- Component Ownership
- Contribution Rule
- Review Process
- Versioning
- Changelog
- Deprecation
- Migration Guide
- Breaking Change
- Design Review
- Accessibility Review
- Release Note
- Adoption Tracking

---

### [실무]

운영 기준:

- 컴포넌트 추가 기준 명확화
- Feature 전용 요구인지 공통 요구인지 검토
- API 변경은 Breaking Change 여부 판단
- Deprecated 컴포넌트는 대체 경로 제공
- Changelog 작성
- 디자인 리뷰와 코드 리뷰 모두 필요
- 접근성 리뷰 포함
- 사용되지 않는 컴포넌트 정리
- 문서 업데이트 없이 컴포넌트 변경 금지
- Versioning 정책 유지
- 마이그레이션 가이드 제공

---

### [FAQ]

Q. Design System에 새 컴포넌트를 추가하는 기준은?

A.
여러 Feature에서 반복 사용되고 비즈니스 로직 없이 공통 UI로 일반화 가능할 때 추가한다.

Q. 컴포넌트 API를 바꿀 때 무엇을 확인해야 하나?

A.
Breaking Change 여부, 사용처 영향, 마이그레이션 방법, 문서 업데이트를 확인해야 한다.

Q. Deprecated 컴포넌트는 바로 삭제해도 되나?

A.
권장하지 않는다. 대체 컴포넌트와 마이그레이션 기간을 제공한 뒤 제거한다.

---

# 27. Integration Rules

## 27.1 Frontend Architecture / React / Next.js 연계

### [개념]

Design System은 Frontend Architecture의 Shared UI Layer와 연결되고, React Component Pattern과 Next.js App Router 환경에서 사용될 수 있어야 한다.

---

### [핵심]

연계 대상:

- Frontend Architecture
- Shared UI Layer
- Advanced React Pattern
- Next.js App Router
- Server Component
- Client Component
- TypeScript Props Pattern
- Theme Provider
- CSS Variable
- Component Boundary
- Feature Component
- Form Handling
- Accessibility Pattern

---

### [실무]

연계 기준:

- Design System 컴포넌트는 `shared/ui` 또는 별도 패키지에 배치 가능
- Next.js App Router에서 Server Component로 가능한 UI와 Client Component가 필요한 UI 구분
- Button / Badge / Card 같은 단순 UI는 Server Component 호환 가능하게 설계
- Modal / Dropdown / Select처럼 상태와 이벤트가 필요한 UI는 Client Component 필요
- Theme Provider는 App Layer 또는 Layout에서 적용 가능
- Feature는 Design System 컴포넌트를 조합해 비즈니스 UI 구현
- Design System은 Feature를 import하지 않음
- 공통 UI에서 API 호출 금지
- 접근성 기준은 모든 Feature에서 재사용됨

---

### [FAQ]

Q. Design System 컴포넌트는 어디에 둬야 하나?

A.
프로젝트 내부에서는 `shared/ui`, 규모가 커지면 별도 패키지나 workspace로 분리할 수 있다.

Q. Design System 컴포넌트가 Feature를 import해도 되나?

A.
안 된다. Design System은 하위 공통 레이어이므로 Feature에 의존하면 구조가 무너진다.

Q. Next.js App Router에서 Design System 컴포넌트는 Server Component가 될 수 있나?

A.
상태나 이벤트가 없는 순수 UI는 가능하다. 브라우저 이벤트나 Hook이 필요한 컴포넌트는 Client Component가 필요하다.

---

# 28. Troubleshooting Rules

## 28.1 자주 발생하는 문제

### [개념]

Troubleshooting 문서는 Agent가 Design System 문제의 원인과 해결책을 빠르게 검색할 수 있도록 문제 / 원인 / 해결 형식을 사용한다.

---

### [핵심]

필수 Troubleshooting 항목:

- Variant Explosion
- Inconsistent Style
- Token Duplication
- Hardcoded Color
- Accessibility Missing
- Focus Ring Removed
- Button vs Link Confusion
- Component API Bloat
- Feature Logic in Shared UI
- Dark Mode Broken
- Theme Flash
- Z-index Conflict
- Modal Focus Trap Missing
- Form Label Missing
- Visual Regression
- Storybook Outdated
- Deprecated Component Usage

---

### [실무]

형식:

```md
문제:

원인:

해결:
```

예시:

```md
문제:

- Button variant가 너무 많아짐

원인:

- Feature 전용 스타일 요구를 모두 Design System variant로 추가함
- variant와 intent 기준이 분리되지 않음

해결:

- 실제 공통 variant만 유지
- 위험 / 성공 같은 의미는 intent로 분리
- Feature 전용 스타일은 Feature 내부에서 처리
```

예시:

```md
문제:

- Modal에서 키보드 focus가 배경으로 이동함

원인:

- Focus Trap이 없거나 Dialog 닫힘 후 Focus Return이 구현되지 않음

해결:

- Dialog 내부에 Focus Trap 적용
- 열릴 때 초기 focus 설정
- 닫힐 때 trigger 요소로 focus 복귀
```

---

### [FAQ]

Q. Variant Explosion은 왜 발생하나?

A.
Feature마다 필요한 스타일을 모두 공통 컴포넌트 variant로 추가할 때 발생한다.

Q. 스타일 불일치는 왜 생기나?

A.
Token을 사용하지 않고 하드코딩하거나 컴포넌트별로 임의 스타일을 적용할 때 생긴다.

Q. 접근성 문제는 왜 Design System에서 특히 위험한가?

A.
공통 컴포넌트의 접근성 문제가 제품 전체로 확산되기 때문이다.

---

# 29. Code Example Rules

## 29.1 코드 예제 작성 기준

### [개념]

Design System 문서의 Code Example은 Agent 코드 생성과 리뷰에 직접 사용될 수 있도록 짧고 목적이 명확해야 한다.

---

### [핵심]

코드 예제 필수 기준:

- TypeScript 우선
- React Function Component 기준
- Props 타입 명확화
- Token 사용
- 접근성 속성 포함
- 핵심 로직 중심
- 긴 전체 파일 금지
- 비즈니스 로직 금지
- API 호출 금지
- `any` 남용 금지
- Focus / Disabled / Loading 상태 고려

---

### [실무]

권장 예제 유형:

- Design Token CSS Variable
- Button Component
- Input / FormField Component
- Modal / Dialog 구조
- Badge / Toast / Alert
- Theme Provider 구조
- Variant Props Type
- Accessibility Props
- Storybook Story
- Component Test
- Visual Regression 기준

금지 예제:

- 하드코딩 색상 남용
- API 호출이 들어간 공통 UI
- 접근성 없는 Icon Button
- Label 없는 Input
- Focus Ring 제거
- 클릭 가능한 `div`
- 비즈니스 조건이 들어간 Button
- Feature 전용 로직이 들어간 Shared UI
- 너무 긴 전체 라이브러리 코드

---

### [FAQ]

Q. Design System 코드 예제는 길어도 되나?

A.
길면 안 된다. RAG Retrieval과 코드 생성에 필요한 핵심 snippet 중심으로 작성한다.

Q. 코드 예제에 비즈니스 로직을 넣어도 되나?

A.
안 된다. Design System 컴포넌트는 비즈니스 로직 없이 재사용 가능한 UI에 집중해야 한다.

---

# 30. Comparison Rules

## 30.1 필수 비교 대상

### [개념]

Design System 문서는 Agent의 UI 설계 판단을 돕기 위해 비교 섹션을 적극 사용한다.

---

### [핵심]

필수 비교:

- Design System vs Component Library
- Design Token vs CSS Variable
- Primitive Token vs Semantic Token
- Base Component vs Feature Component
- Primitive Component vs Composite Component
- Controlled vs Uncontrolled Component
- Variant vs Intent
- Disabled vs Readonly
- Button vs Link
- Modal vs Drawer
- Tooltip vs Popover
- Toast vs Alert
- Skeleton vs Spinner
- Dark Mode vs Theme
- Shared UI vs Feature UI
- Headless Component vs Styled Component
- Visual Regression Test vs Snapshot Test
- Accessibility Test vs Manual Review

---

### [실무]

Comparison 작성 기준:

- 표 사용 권장
- 기준은 목적 / 사용 위치 / 장점 / 주의점으로 정리
- 결론을 명확히 작성
- “항상 A” 같은 절대 표현 금지
- 실무 판단 Flow 포함

---

### [FAQ]

Q. Design System과 Component Library 차이는?

A.
Component Library는 UI 컴포넌트 모음에 가깝고, Design System은 토큰, 원칙, 패턴, 접근성, 문서화, 운영 기준까지 포함한다.

Q. Toast와 Alert는 어떻게 구분하나?

A.
Toast는 일시적 알림이고, Alert는 화면 내 지속 메시지에 적합하다.

Q. Skeleton과 Spinner는 어떻게 구분하나?

A.
Skeleton은 로딩될 형태를 보여주고, Spinner는 단순 진행 중 상태를 표시한다.

---

# 31. Checklist Rules

## 31.1 문서 품질 체크리스트

### [개념]

Design System RAG 문서는 출력 전 구조, 용어, Retrieval Query, 코드 안전성을 검수해야 한다.

---

### [핵심]

Checklist:

- [ ] Design System 목적이 명확한가?
- [ ] Design Token 기준을 포함했는가?
- [ ] Color / Typography / Spacing 기준을 포함했는가?
- [ ] Component Classification을 포함했는가?
- [ ] Component API 설계 기준을 포함했는가?
- [ ] Variant / Size / Intent 기준을 포함했는가?
- [ ] State Pattern을 포함했는가?
- [ ] Button / Form / Overlay / Feedback 기준을 포함했는가?
- [ ] Accessibility 기준을 충분히 포함했는가?
- [ ] Theming / Dark Mode 기준을 포함했는가?
- [ ] Icon / Asset 기준을 포함했는가?
- [ ] Responsive Design 기준을 포함했는가?
- [ ] Motion 기준을 포함했는가?
- [ ] Storybook / Documentation 기준을 포함했는가?
- [ ] Testing / Visual Regression 기준을 포함했는가?
- [ ] Governance / Versioning 기준을 포함했는가?
- [ ] Frontend Architecture와 연계되는가?
- [ ] Troubleshooting을 포함했는가?
- [ ] FAQ를 충분히 포함했는가?
- [ ] Retrieval Queries를 포함했는가?
- [ ] 코드블록에 `id=""`가 없는가?
- [ ] 오타와 용어 혼용을 제거했는가?

---

### [실무]

검수 기준:

- Minimum Quality: 95/100
- Target Quality: 97+/100
- 문서 하나는 하나의 주제를 중심으로 작성
- Chunk 단위로 독립 검색 가능해야 함
- FAQ는 실제 사용자 질문 문장으로 작성
- Retrieval Queries는 Agent 검색 패턴 중심으로 작성
- Frontend Architecture / Advanced React Pattern 문서와 충돌하지 않아야 함

---

### [FAQ]

Q. Design System 문서 품질에서 가장 중요한 것은?

A.
Token, Component API, Variant, State, Accessibility, Documentation, Testing 기준이 명확해야 한다.

---

# 32. Retrieval Optimization Rules

## 32.1 검색 최적화 키워드

### [개념]

Retrieval Optimization은 Agent가 사용자의 질문을 정확한 문서 Chunk로 연결하도록 키워드와 질문 패턴을 강화하는 규칙이다.

---

### [핵심]

강조 키워드:

- Design System
- Design Token
- Component Library
- Component API
- Base Component
- Composite Component
- Primitive Component
- Feature Component
- Shared UI
- Design System Architecture
- Color Token
- Semantic Token
- Primitive Token
- Typography Token
- Spacing Token
- Radius Token
- Shadow Token
- Z-index Token
- Motion Token
- CSS Variable
- Theme
- Dark Mode
- Variant
- Size
- Intent
- State Pattern
- Button Component
- Form Component
- Modal
- Dialog
- Dropdown
- Tooltip
- Toast
- Alert
- Badge
- Skeleton
- Empty State
- Error State
- Accessibility
- ARIA
- Keyboard Navigation
- Focus Management
- Storybook
- Visual Regression Test
- Component Test
- Governance
- Versioning
- Deprecation

---

### [실무]

FAQ와 Retrieval Queries에는 아래 표현을 포함한다.

- Design System은 뭐야?
- Design System 문서는 어떻게 만들어?
- Design Token은 왜 필요해?
- Primitive Token과 Semantic Token 차이는?
- Button 컴포넌트는 어떻게 설계해?
- 공통 UI와 Feature UI 차이는?
- Variant는 어떻게 설계해?
- Boolean Props가 많으면 어떻게 해?
- 접근성은 Design System에서 어떻게 적용해?
- Icon Button에는 뭐가 필요해?
- Modal 접근성은 어떻게 처리해?
- Toast와 Alert 차이는?
- Skeleton과 Spinner 차이는?
- Dark Mode는 어떻게 설계해?
- Storybook에는 무엇을 문서화해?
- Visual Regression Test는 왜 필요해?
- Design System에 새 컴포넌트는 언제 추가해?
- Deprecated 컴포넌트는 어떻게 처리해?
- Design System 코드 리뷰 기준은?
- Feature 전용 컴포넌트를 공통화해도 돼?

---

### [FAQ]

Q. Retrieval Queries는 왜 필요한가?

A.
사용자의 자연어 질문을 문서 Chunk와 매칭하기 위해 필요하다.

Q. 키워드 반복은 허용되나?

A.
허용된다. 단, 문서 품질을 해치지 않는 범위에서 검색 친화적으로 반복한다.

---

# 33. Version Rules

## 33.1 기준 버전

### [개념]

Design System 문서는 Modern Frontend 기준으로 작성하며 React / TypeScript / Next.js App Router와 연계 가능해야 한다.

---

### [핵심]

기준:

- Modern Frontend
- React 19+
- TypeScript
- Next.js App Router 연계 가능
- Function Component
- CSS Variable
- Token-based Design
- Accessibility First
- Storybook-compatible Component
- Visual Regression Test
- Component-driven Development
- Dark Mode / Theming
- Design-Code Alignment

Legacy 제외:

- jQuery 기반 UI
- Class Component 중심 UI
- 하드코딩 색상 중심 스타일
- 접근성 없는 Custom UI
- 모든 스타일을 페이지마다 직접 작성하는 구조
- 비즈니스 로직이 들어간 공통 컴포넌트
- 문서 없는 공통 컴포넌트
- 토큰 없이 무작위 CSS 값 사용하는 구조

---

### [실무]

문서 작성 시 주의:

- Frontend Architecture의 Shared UI Layer와 충돌하지 않도록 작성
- Advanced React Pattern의 Hook / Composition 상세와 중복 최소화
- Next.js App Router의 Server / Client Component 경계 고려
- CSS-in-JS / CSS Modules / Tailwind / Vanilla CSS 등 구현 방식은 프로젝트별 선택 가능
- 구현 도구보다 Token / API / Accessibility / Governance 기준을 우선
- 디자인 도구와 코드 간 Token 명칭 일치 권장

---

### [FAQ]

Q. Design System 문서는 특정 CSS 도구 기준이어야 하나?

A.
아니다. Tailwind, CSS Modules, CSS-in-JS 등은 프로젝트 선택이다. 핵심은 Token, Component API, Accessibility 기준이다.

Q. React 19 기준을 고려해야 하나?

A.
Modern React 기준으로 작성하고, React / Next.js 환경에서 Server Component와 Client Component 경계를 고려하는 것이 좋다.

---

# 34. Common Mistakes

## 34.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Agent가 Design System 코드 리뷰와 UI 품질 진단에서 자주 참조하는 검색 최적화 Chunk이다.

---

### [핵심]

자주 발생하는 실수:

- Design Token 없이 하드코딩 색상 사용
- Primitive Token만 사용하고 Semantic Token 없음
- Button variant 무분별 증가
- Boolean Props 폭발
- 공통 UI에 비즈니스 로직 포함
- Feature 전용 컴포넌트를 성급히 Shared UI로 승격
- Label 없는 Input
- 접근성 없는 Icon Button
- Focus Ring 제거
- 클릭 가능한 `div` 사용
- Modal Focus Trap 누락
- Tooltip에 필수 정보 배치
- Toast만으로 중요한 에러 처리
- Disabled와 Readonly 혼동
- Button과 Link 역할 혼동
- z-index 임의 숫자 남용
- Dark Mode 색상 단순 반전
- Storybook 문서와 실제 구현 불일치
- Visual Regression Test 부재
- Deprecated 컴포넌트 대체안 없음
- 컴포넌트 API 변경 후 Changelog 누락

---

### [실무]

리뷰 기준:

- Token 사용 여부 확인
- Semantic Token 사용 여부 확인
- Component API 단순성 확인
- Variant / Size / Intent 조합 확인
- 접근성 속성 확인
- Keyboard Interaction 확인
- Focus Management 확인
- Feature 로직 포함 여부 확인
- Storybook 문서화 확인
- Visual Regression 영향 확인
- Dark Mode 대응 확인
- Breaking Change 여부 확인

---

### [FAQ]

Q. Design System에서 가장 흔한 실수는?

A.
토큰 없이 스타일을 하드코딩하고, Feature별 요구를 모두 공통 컴포넌트 variant로 추가하는 것이다.

Q. 공통 UI에 비즈니스 로직이 들어가면 왜 문제인가?

A.
재사용성이 떨어지고 특정 Feature 변경이 Design System 전체에 영향을 줄 수 있다.

Q. 접근성 누락이 왜 큰 문제인가?

A.
공통 컴포넌트의 접근성 문제가 제품 전체로 확산되기 때문이다.

---

# 35. Final Goal

## 35.1 최종 목표

### [개념]

Design System RAG 문서는 Agent가 제품 UI의 공통 기준을 설계, 생성, 검토, 문서화, 운영할 수 있도록 만들어야 한다.

---

### [핵심]

Agent가 수행 가능해야 하는 작업:

- Design Token 구조 설계
- Color / Typography / Spacing Token 설계
- Component Classification 판단
- Component API 설계
- Variant / Size / Intent 설계
- Button / Form / Modal / Toast 등 공통 컴포넌트 설계
- 접근성 기준 적용
- Theming / Dark Mode 구조 설계
- Icon / Asset 기준 검토
- Responsive Design 기준 제안
- Motion Token 기준 제안
- Storybook 문서화 기준 작성
- Component Test 기준 제안
- Visual Regression Test 기준 제안
- Governance / Versioning 기준 제안
- Deprecated Component 마이그레이션 기준 작성
- Frontend Architecture와 Shared UI Layer 연계
- Design System 코드 리뷰
- UI 일관성 문제 Troubleshooting

---

### [실무]

최종 품질 기준:

- 검색 가능한 Chunk 구조
- 명확한 용어 통일
- FAQ 강화
- 실무 판단 기준 포함
- 코드 예제는 짧고 안전하게 작성
- Token / Component / Pattern / Governance 경계 명확화
- 접근성 / 테스트 / 문서화 기준 포함
- Frontend Architecture / Advanced React Pattern 문서와 연계 가능
- Retrieval Queries 포함

---

### [FAQ]

Q. Design System Domain Rules의 최종 목적은?

A.
Agent가 제품 UI의 토큰, 공통 컴포넌트, 접근성, 테마, 문서화, 테스트, 운영 기준을 설계하고 리뷰하도록 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Design System 문서는 어떤 기준으로 작성해야 해?

A.
Design Token, Component API, Variant, State, Accessibility, Theming, Documentation, Testing, Governance 중심으로 작성해야 한다.

Q. Design System은 뭐야?

A.
제품 전반의 UI 일관성을 위한 토큰, 컴포넌트, 패턴, 접근성, 문서화, 운영 기준을 포함하는 체계이다.

Q. Design System과 Component Library 차이는?

A.
Component Library는 UI 컴포넌트 모음이고, Design System은 토큰, 원칙, 패턴, 접근성, 문서화, 운영 기준까지 포함한다.

Q. Design Token은 왜 필요해?

A.
색상, 간격, 폰트 같은 디자인 값을 중앙에서 관리해 일관성과 변경 용이성을 높이기 위해 필요하다.

Q. Primitive Token과 Semantic Token 차이는?

A.
Primitive Token은 원시 값이고, Semantic Token은 UI 역할을 나타내는 값이다.

Q. Component Token은 언제 써?

A.
특정 컴포넌트에만 적용되는 디자인 값이 반복되고 의미가 명확할 때 사용한다.

Q. 컴포넌트에서 색상을 직접 써도 돼?

A.
가능하면 피한다. Semantic Token이나 Component Token을 사용하는 것이 좋다.

Q. Color Token은 어떻게 설계해?

A.
Brand, Neutral, Background, Text, Border, Intent, Focus Ring처럼 역할 기준으로 설계한다.

Q. Dark Mode는 어떻게 설계해?

A.
Semantic Token을 CSS Variable로 정의하고 Theme별로 값을 재매핑하는 방식이 좋다.

Q. Dark Mode에서 색상 반전만 하면 돼?

A.
아니다. 대비, 브랜드 톤, 상태 색상, 가독성을 따로 검토해야 한다.

Q. Typography Token은 왜 필요해?

A.
제목, 본문, 라벨, 캡션의 크기와 줄 높이를 일관되게 유지하기 위해 필요하다.

Q. Spacing Token은 왜 필요해?

A.
화면마다 임의의 간격을 쓰지 않고 일관된 UI 리듬을 유지하기 위해 필요하다.

Q. Base Component와 Feature Component 차이는?

A.
Base Component는 비즈니스 로직 없는 공통 UI이고, Feature Component는 특정 기능이나 도메인에 종속된 UI이다.

Q. LoginForm은 Design System에 넣어도 돼?

A.
일반적으로 넣지 않는다. LoginForm은 인증 Feature에 종속된 Feature Component이다.

Q. 공통 UI와 Feature UI 차이는?

A.
공통 UI는 여러 기능에서 재사용되는 비즈니스 로직 없는 컴포넌트이고, Feature UI는 특정 기능에 종속된 컴포넌트이다.

Q. Feature 전용 컴포넌트를 공통화해도 돼?

A.
반복 사용이 확인되고 비즈니스 로직을 제거할 수 있을 때만 공통화한다.

Q. Component API는 어떻게 설계해?

A.
필수 props, 선택 props, variant, size, state, callback, children, accessibility props를 예측 가능하게 설계한다.

Q. Variant는 어떻게 설계해?

A.
제품에서 반복되는 UI 의도와 상태를 기준으로 제한된 선택지를 제공한다.

Q. Boolean Props가 많으면 어떻게 해?

A.
`variant`, `size`, `intent` 같은 명시적 prop이나 Composition으로 개선한다.

Q. Variant Explosion은 왜 발생해?

A.
Feature마다 필요한 스타일을 모두 공통 컴포넌트 variant로 추가할 때 발생한다.

Q. Button 컴포넌트는 어떻게 설계해?

A.
variant, size, intent, disabled, loading, type, focus 상태, accessible name을 기준으로 설계한다.

Q. Button과 Link는 어떻게 구분해?

A.
동작 실행은 Button, 페이지 이동은 Link를 사용한다.

Q. Icon Button에는 뭐가 필요해?

A.
눈에 보이는 텍스트가 없으므로 `aria-label` 같은 accessible name이 필요하다.

Q. Form Component는 어떻게 설계해?

A.
Label, Input, Helper Text, Error Message, Required, Disabled, Validation, 접근성 연결을 함께 설계한다.

Q. Placeholder를 Label 대신 써도 돼?

A.
안 된다. Placeholder는 입력 힌트이고 Label을 대체할 수 없다.

Q. Error 상태는 색상만 바꾸면 돼?

A.
아니다. 에러 메시지와 `aria-invalid`, `aria-describedby` 같은 접근성 연결이 필요하다.

Q. Modal 접근성은 어떻게 처리해?

A.
Focus Trap, Focus Return, Escape Key, 적절한 role과 label을 제공해야 한다.

Q. Tooltip과 Popover 차이는?

A.
Tooltip은 짧은 보조 정보에 적합하고, Popover는 더 복잡한 콘텐츠나 상호작용에 적합하다.

Q. Tooltip에 필수 정보를 넣어도 돼?

A.
권장하지 않는다. 필수 정보는 항상 화면에 표시되어야 한다.

Q. Toast와 Alert 차이는?

A.
Toast는 일시적 알림이고, Alert는 화면 내 지속 메시지에 적합하다.

Q. 중요한 에러를 Toast만으로 처리해도 돼?

A.
권장하지 않는다. 사용자가 놓칠 수 있으므로 화면 내 Error State나 Alert를 고려한다.

Q. Skeleton과 Spinner 차이는?

A.
Skeleton은 로딩될 UI 형태를 미리 보여주고, Spinner는 단순 진행 중 상태를 표시한다.

Q. Empty State에는 무엇을 넣어야 해?

A.
데이터가 없다는 사실과 사용자가 다음에 할 수 있는 행동을 안내하는 내용을 넣는다.

Q. 접근성은 Design System에서 어떻게 적용해?

A.
Semantic HTML, Keyboard Navigation, Focus Management, Label, ARIA, Color Contrast를 공통 컴포넌트 기본 기준으로 적용한다.

Q. Focus Ring을 제거해도 돼?

A.
안 된다. 키보드 사용자가 현재 위치를 알 수 있어야 한다.

Q. ARIA를 많이 쓰면 접근성이 좋아져?

A.
아니다. Semantic HTML을 우선 사용하고 필요한 경우에만 정확히 사용해야 한다.

Q. z-index는 어떻게 관리해?

A.
임의 숫자를 쓰지 않고 z-index Token으로 Modal, Popover, Tooltip 같은 계층을 관리한다.

Q. Icon 색상은 어떻게 관리해?

A.
가능하면 `currentColor`나 Semantic Color Token을 사용한다.

Q. Breakpoint는 어떻게 정해?

A.
특정 디바이스보다 레이아웃이 깨지는 지점과 콘텐츠 우선순위를 기준으로 정한다.

Q. 모바일에서 Hover UI를 써도 돼?

A.
주의해야 한다. 터치 환경에서는 Hover가 안정적으로 동작하지 않을 수 있다.

Q. Motion Token은 왜 필요해?

A.
화면마다 다른 속도와 easing을 쓰지 않고 일관된 움직임 경험을 제공하기 위해 필요하다.

Q. Reduced Motion은 왜 고려해?

A.
움직임에 민감한 사용자가 불편을 느끼지 않도록 하기 위해 필요하다.

Q. Storybook에는 무엇을 문서화해?

A.
컴포넌트 목적, Props, Variant, 상태, 접근성, 사용 예시, Do / Don't를 문서화한다.

Q. Visual Regression Test는 왜 필요해?

A.
공통 컴포넌트 스타일 변경이 제품 전체에 영향을 줄 수 있으므로 의도치 않은 시각 변경을 잡기 위해 필요하다.

Q. Design System에서 무엇을 테스트해야 해?

A.
컴포넌트 상태, variant, 접근성, keyboard interaction, theme, visual regression을 테스트해야 한다.

Q. Snapshot Test만으로 충분해?

A.
아니다. 상호작용, 접근성, 시각 회귀 테스트가 함께 필요하다.

Q. Design System에 새 컴포넌트는 언제 추가해?

A.
여러 Feature에서 반복 사용되고 비즈니스 로직 없이 공통 UI로 일반화 가능할 때 추가한다.

Q. Deprecated 컴포넌트는 어떻게 처리해?

A.
대체 컴포넌트와 마이그레이션 가이드를 제공하고 충분한 전환 기간 후 제거한다.

Q. Component API 변경 시 무엇을 확인해?

A.
Breaking Change 여부, 사용처 영향, 마이그레이션 방법, 문서 업데이트를 확인한다.

Q. Design System 컴포넌트는 어디에 둬?

A.
프로젝트 내부에서는 `shared/ui`, 규모가 커지면 별도 패키지나 workspace로 분리할 수 있다.

Q. Design System 컴포넌트가 Feature를 import해도 돼?

A.
안 된다. Design System은 공통 레이어이므로 Feature에 의존하면 구조가 무너진다.

Q. Next.js App Router에서 Design System 컴포넌트는 Server Component가 될 수 있어?

A.
상태나 이벤트가 없는 순수 UI는 가능하다. 브라우저 이벤트나 Hook이 필요한 컴포넌트는 Client Component가 필요하다.

Q. Design System 코드 리뷰 기준은?

A.
Token 사용, Component API 단순성, Variant 조합, 접근성, Keyboard Interaction, Theme 대응, Storybook 문서화, Visual Regression 영향을 확인한다.

Q. Design System에서 가장 흔한 실수는?

A.
토큰 없이 스타일을 하드코딩하고, Feature별 요구를 모두 공통 컴포넌트 variant로 추가하는 것이다.

Q. Design System RAG 문서 최종 목표는?

A.
Agent가 제품 UI의 토큰, 공통 컴포넌트, 접근성, 테마, 문서화, 테스트, 운영 기준을 설계하고 리뷰하게 만드는 것이다.
