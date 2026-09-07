# UI Component Pattern Part08 - Accessibility Styling Troubleshooting

---

# 1. Accessibility Styling Troubleshooting Overview

## 1.1 Final Part Purpose

### [개념]

Accessibility Styling Troubleshooting 문서는 UI Component Pattern의 최종 검수 기준을 정의하는 RAG 문서다.

이 문서는 Frontend Agent / Review Agent / PM Agent가 UI Component를 생성한 뒤 접근성, 스타일 경계, 파일 구조, 공통 실수, Troubleshooting, 비교 기준, 최종 Checklist를 검토하기 위해 사용한다.

UI Component Pattern Part08은 Part01 ~ Part07에서 작성한 Component Responsibility, Props Design, Composition Pattern, Base UI Components, List Table Navigation, State UI Components, Form UI Components를 최종 검수하는 역할을 한다.

---

### [핵심]

Part08 핵심 대상:

- UI Component Accessibility
- Semantic HTML
- ARIA Attribute
- Keyboard Accessibility
- Styling Boundary
- Layout Responsibility
- className Extension
- File Structure
- Common Mistakes
- Troubleshooting
- Comparison Rules
- Final Review Checklist
- Retrieval Optimization

최종 검수 기준:

- Component 책임이 명확한가
- Common UI / Feature UI가 분리되었는가
- Props API가 안정적인가
- 접근성 속성이 포함되었는가
- Semantic Element를 사용했는가
- Styling Boundary가 분리되었는가
- Layout 책임이 부모에게 있는가
- 파일 위치가 적절한가
- Props Explosion이 없는가
- Over Abstraction이 없는가
- Retrieval Queries가 충분한가

---

### [실무]

2026 실무 기준에서 UI Component Pattern 최종 검수는 코드 스타일 점검이 아니라 Agent Output 품질 점검이다.

검수 Flow:

```text
Component Draft
→ Responsibility Check
→ Props API Check
→ Composition Check
→ Accessibility Check
→ Styling Boundary Check
→ File Structure Check
→ Troubleshooting Check
→ Common Mistakes Check
→ Final Checklist
→ Retrieval Query Review
```

Part08은 UI Component Pattern Domain 문서의 마지막 Part로 사용한다.

```text
Part01 Component Responsibility
→ Part02 Props Design
→ Part03 Composition Pattern
→ Part04 Base UI Components
→ Part05 List Table Navigation
→ Part06 State UI Components
→ Part07 Form UI Components
→ Part08 Accessibility Styling Troubleshooting
```

---

### [FAQ]

Q. Part08은 왜 필요해?
A. UI Component 문서 전체를 접근성, 스타일 경계, 파일 구조, Common Mistakes, Troubleshooting 기준으로 최종 검수하기 위해 필요하다.

Q. UI Component 최종 검수에서 가장 중요한 것은 뭐야?
A. Component 책임, Props API, 접근성, Styling Boundary, Common UI / Feature UI 분리, 과도한 추상화 방지다.

Q. Part08은 새 Component 작성 문서야?
A. 아니다. Part01 ~ Part07에서 작성한 UI Component 설계를 최종 검토하고 문제를 찾는 문서다.

---

# 2. UI Component Accessibility

## 2.1 Accessibility Responsibility

### [개념]

UI Component Accessibility는 공통 Component가 기본적으로 접근 가능한 HTML 구조와 ARIA 속성을 제공하도록 하는 기준이다.

UI Component는 시각적으로만 동작하는 것이 아니라 keyboard 사용자와 보조기술 사용자도 사용할 수 있어야 한다.

---

### [핵심]

필수 고려:

- semantic element
- button
- anchor
- Link
- label
- alt
- aria-label
- aria-labelledby
- aria-describedby
- aria-expanded
- aria-selected
- aria-invalid
- aria-current
- role
- keyboard navigation
- focus visible
- role status
- role alert

기본 기준:

```text
클릭 액션
→ button

페이지 이동
→ Link / anchor

입력 설명
→ label

오류 연결
→ aria-describedby

열림 상태
→ aria-expanded

선택 상태
→ aria-selected

현재 페이지
→ aria-current

아이콘 버튼
→ aria-label

로딩 상태
→ role status

오류 상태
→ role alert
```

---

### [실무]

Button 접근성 기준:

```tsx
<button type="button" onClick={onClick}>
  저장
</button>
```

IconButton 접근성 기준:

```tsx
<button type="button" aria-label="검색어 초기화" onClick={onReset}>
  <span aria-hidden="true">×</span>
</button>
```

Input 접근성 기준:

```tsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  value={email}
  aria-invalid={Boolean(error)}
  aria-describedby={error ? "email-error" : undefined}
  onChange={(event) => setEmail(event.target.value)}
/>
{error && (
  <p id="email-error" role="alert">
    이메일 형식이 올바르지 않습니다.
  </p>
)}
```

Dropdown 접근성 기준:

```tsx
<button
  type="button"
  aria-haspopup="menu"
  aria-expanded={open}
  onClick={toggleOpen}
>
  더보기
</button>
```

---

### [FAQ]

Q. div에 onClick을 붙이면 안 돼?
A. 가능은 하지만 키보드 접근성과 의미가 부족하다. 클릭 액션은 button, 이동은 Link나 anchor를 사용하는 것이 좋다.

Q. 아이콘 버튼에는 텍스트가 없어도 돼?
A. 시각적 텍스트가 없다면 aria-label로 버튼의 목적을 제공해야 한다.

Q. input error는 어떻게 접근성 연결해?
A. error message id를 만들고 input의 aria-describedby에 연결하며 aria-invalid를 함께 사용한다.

---

## 2.2 Semantic Element Rules

### [개념]

Semantic Element Rules는 UI 목적에 맞는 HTML 요소를 선택하는 기준이다.

Semantic HTML은 접근성, 검색 가능성, 유지보수성, 사용자 기대 동작에 직접 영향을 준다.

---

### [핵심]

권장 요소:

- button: 클릭 액션
- a / Link: 페이지 이동
- form: 입력 제출
- label: input 설명
- input: 단일 입력
- textarea: 여러 줄 입력
- select: Form 값 선택
- ul / ol / li: 목록
- table / thead / tbody / th / td: 표 데이터
- section: 독립 영역
- article: 독립 콘텐츠 카드
- nav: 탐색 영역
- dialog role: Modal / Dialog

주의:

- div onClick 남용 금지
- span button 대체 금지
- table 대신 div로 표 구현 지양
- placeholder를 label 대체로 사용 금지
- a 태그를 button처럼 사용 지양
- button을 Link처럼 사용하는 것 주의

---

### [실무]

좋은 예:

```tsx
<Link to={`/festivals/${festival.festivalId}`}>축제 상세 보기</Link>
```

```tsx
<button type="button" onClick={openModal}>
  삭제
</button>
```

나쁜 예:

```tsx
<div onClick={openModal}>삭제</div>
```

Table 좋은 예:

```tsx
<table>
  <caption>사용자 목록</caption>
  <thead>
    <tr>
      <th scope="col">닉네임</th>
      <th scope="col">권한</th>
    </tr>
  </thead>
  <tbody>
    {users.map((user) => (
      <tr key={user.userId}>
        <td>{user.nickname}</td>
        <td>{user.role}</td>
      </tr>
    ))}
  </tbody>
</table>
```

---

### [FAQ]

Q. 클릭 가능한 Card는 div로 만들어도 돼?
A. 권장하지 않는다. 링크 이동이면 Link나 anchor, 액션이면 button을 사용하는 것이 접근성에 좋다.

Q. Table 대신 div로 만들어도 돼?
A. 표 형태의 데이터라면 table 요소를 사용하는 것이 의미와 접근성에 좋다.

Q. form 태그는 꼭 써야 해?
A. 검색이나 제출 UI에서는 form을 사용하면 Enter 제출과 접근성 측면에서 유리하다.

---

## 2.3 Keyboard Accessibility

### [개념]

Keyboard Accessibility는 마우스 없이 keyboard만으로 UI를 탐색하고 조작할 수 있게 하는 기준이다.

Button, Link, Input 같은 native element를 사용하면 기본 keyboard 동작을 얻을 수 있다.

---

### [핵심]

Keyboard 기준:

- Tab 이동 가능
- Enter / Space 동작 가능
- focus visible 유지
- Modal focus management 고려
- Dropdown ESC 닫기 고려
- Accordion trigger button 사용
- Tab keyboard navigation 고려
- disabled 요소 focus 기준 명확화
- custom component는 keyboard event 직접 구현 필요 가능

주의:

- focus outline 제거 금지
- div onClick은 기본 keyboard 동작 없음
- hover에만 의존 금지
- Tooltip은 focus 접근도 고려
- Dropdown / Modal / Tabs는 접근성 난도 높음

---

### [실무]

Focus visible 기준:

```css
.button:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```

Accordion trigger 기준:

```tsx
<button
  type="button"
  aria-expanded={open}
  aria-controls={panelId}
  onClick={toggleOpen}
>
  상세 조건
</button>
```

Keyboard Debug Flow:

```text
마우스 없이 사용 가능한가?
→ Tab 이동 가능한가?
→ Enter / Space로 실행 가능한가?
→ focus 위치가 보이는가?
→ ESC / Arrow Key가 필요한 UI인가?
→ 보조기술 이름이 있는가?
```

---

### [FAQ]

Q. focus outline을 없애도 돼?
A. 권장하지 않는다. 대신 디자인에 맞는 focus visible 스타일을 제공하는 것이 좋다.

Q. hover로만 열리는 UI는 괜찮아?
A. 권장하지 않는다. keyboard focus로도 접근 가능해야 한다.

Q. div onClick에 keydown을 추가하면 button과 같아?
A. 일부 보완은 가능하지만 native button을 사용하는 것이 더 안전하고 단순하다.

---

# 3. Styling Boundary

## 3.1 Styling Boundary Responsibility

### [개념]

Styling Boundary는 UI Component가 자체 스타일을 어디까지 책임지고 외부 스타일 확장을 어떻게 허용할지 정하는 기준이다.

공통 UI Component는 자체 모양을 담당하고, 화면 배치와 간격은 부모 Layout Component가 담당하는 것이 좋다.

---

### [핵심]

스타일 Props 후보:

- className
- style
- variant
- size
- fullWidth
- align
- layout props basics

Component 자체 책임:

- padding
- border
- radius
- color variant
- size variant
- disabled style
- loading style
- error style
- focus visible style

부모 Layout 책임:

- margin
- gap
- grid placement
- flex alignment
- page width
- section spacing
- responsive layout
- component placement

주의:

- 공통 Component 내부 margin 남발 금지
- 모든 스타일을 Props로 열어두지 않음
- inline style 남용 지양
- className override 기준 필요
- Feature 전용 스타일을 Common UI에 추가하지 않음

---

### [실무]

Common Button:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "danger";
  size?: "sm" | "md" | "lg";
  className?: string;
  children: React.ReactNode;
};

function Button({
  variant = "primary",
  size = "md",
  className = "",
  children,
}: ButtonProps) {
  return (
    <button
      type="button"
      className={`button button-${variant} button-${size} ${className}`}
    >
      {children}
    </button>
  );
}
```

ButtonGroup:

```tsx
function ButtonGroup({ children }: { children: React.ReactNode }) {
  return <div className="button-group">{children}</div>;
}
```

책임 분리:

```text
Button
→ 버튼 자체 스타일

ButtonGroup
→ 버튼 간 gap / 정렬

PageLayout
→ 페이지 폭 / 섹션 간격
```

---

### [FAQ]

Q. 공통 Component에 className을 열어줘야 해?
A. 프로젝트 기준에 따라 다르지만 외부 확장이 필요한 경우 className을 허용하면 유연하다.

Q. Button 안에 margin을 넣어도 돼?
A. 공통 Button에는 margin을 넣지 않는 것이 좋다. 버튼 간 간격은 부모 Layout이나 ButtonGroup이 담당하는 편이 유연하다.

Q. style prop을 많이 쓰면 안 돼?
A. 동적 스타일에는 사용할 수 있지만 일관성 있는 UI를 위해 variant, size, className 기준을 우선하는 것이 좋다.

---

## 3.2 Layout Responsibility

### [개념]

Layout Responsibility는 Component 자체 스타일과 부모 Layout이 담당할 배치 스타일을 구분하는 기준이다.

UI Component는 자체 모양을 담당하고, Layout Component는 배치와 간격을 담당한다.

---

### [핵심]

UI Component 책임:

- Button 자체 모양
- Card 자체 모양
- Badge 자체 모양
- TextField 자체 구조
- Modal 자체 구조
- ErrorState 자체 표현

Layout Component 책임:

- Stack
- Grid
- Container
- PageLayout
- Section
- ButtonGroup
- CardGrid
- FormActions
- HeaderLayout

분리 기준:

```text
Component 자체 의미와 모양
→ UI Component

여러 Component 사이의 배치
→ Layout Component

화면 전체 구조
→ PageLayout

도메인 화면 배치
→ Feature Layout
```

---

### [실무]

Card와 Grid 분리:

```tsx
function Card({ children }: { children: React.ReactNode }) {
  return <article className="card">{children}</article>;
}

function CardGrid({ children }: { children: React.ReactNode }) {
  return <div className="card-grid">{children}</div>;
}
```

사용:

```tsx
<CardGrid>
  {festivals.map((festival) => (
    <FestivalCard key={festival.festivalId} festival={festival} />
  ))}
</CardGrid>
```

FormActions:

```tsx
function FormActions({ children }: { children: React.ReactNode }) {
  return <div className="form-actions">{children}</div>;
}
```

---

### [FAQ]

Q. Card가 grid 배치까지 담당해야 해?
A. 보통 Card는 자체 모양만 담당하고 grid 배치는 부모 List나 Layout Component가 담당한다.

Q. Layout Component는 왜 필요해?
A. UI Component 자체 스타일과 화면 배치 책임을 분리해 재사용성과 유지보수성을 높이기 위해 필요하다.

Q. 공통 Component에 gap props를 많이 넣어도 돼?
A. 제한적으로 가능하지만 여러 Component 사이의 간격은 Stack, Grid, ButtonGroup 같은 Layout Component가 담당하는 것이 좋다.

---

## 3.3 Styling Conflict Troubleshooting

### [개념]

Styling Conflict는 공통 UI Component의 스타일이 특정 화면 요구와 충돌하거나 외부 스타일이 내부 스타일을 깨는 문제다.

Styling Conflict는 Component 자체 스타일과 Layout 스타일의 책임이 섞일 때 자주 발생한다.

---

### [핵심]

원인:

- 공통 Component에 margin 포함
- CSS selector 범위 과도
- className merge 기준 없음
- inline style 남용
- variant 기준 불명확
- 부모 layout과 자식 component 책임 혼동
- 전역 CSS 충돌
- Feature 전용 스타일을 Common UI에 추가
- 모든 스타일을 props로 열어둠

해결:

- Component 자체 스타일과 Layout 스타일 분리
- className 확장 기준 통일
- variant / size 기준 정리
- 전역 selector 축소
- CSS Module / scoped style 검토
- margin은 부모가 담당
- Feature 스타일은 Feature Component에서 처리

---

### [실무]

문제 예:

```tsx
function Button({ children }: { children: React.ReactNode }) {
  return <button className="button with-margin">{children}</button>;
}
```

문제점:

```text
모든 Button에 margin 적용
ButtonGroup / Modal footer / FormActions에서 간격 충돌
화면마다 override 증가
```

개선:

```tsx
function Button({ children }: { children: React.ReactNode }) {
  return <button className="button">{children}</button>;
}

function ButtonGroup({ children }: { children: React.ReactNode }) {
  return <div className="button-group">{children}</div>;
}
```

Debug Flow:

```text
깨진 스타일 확인
→ 공통 Component 기본 스타일 확인
→ 부모 Layout 스타일 확인
→ className 충돌 확인
→ selector 우선순위 확인
→ 책임 분리
```

---

### [FAQ]

Q. 공통 Button에 margin을 넣었더니 화면마다 간격이 이상해?
A. Button 자체에 margin을 넣으면 부모 layout과 충돌할 수 있다. 간격은 ButtonGroup이나 부모 layout에서 관리하는 것이 좋다.

Q. className으로 외부 스타일을 덮어도 돼?
A. 가능하지만 기준이 없으면 스타일 충돌이 생긴다. 공통 Component의 확장 규칙을 정하는 것이 좋다.

Q. Feature 전용 스타일은 어디에 둬?
A. Feature Component className이나 Feature 스타일 파일에서 처리하는 것이 좋다.

---

# 4. File Structure Rules

## 4.1 UI Component File Structure

### [개념]

UI Component File Structure는 공통 UI, Feature UI, Page Component, Layout Component, State UI를 구분해 파일을 배치하는 기준이다.

파일 구조는 Agent가 Component 책임을 이해하고 적절한 위치에 코드를 생성하도록 돕는다.

---

### [핵심]

구분:

- components/ui
- components/common
- components/layout
- components/states
- components/form
- features
- pages
- hooks
- styles

기본 기준:

- 공통 UI는 도메인 의존 제거
- Feature Component는 features 내부 배치
- Page Component는 routing 단위
- Layout Component는 components/layout
- State UI는 components/states 또는 components/feedback
- Form 공통 UI는 components/form 또는 components/ui
- Domain Hook은 features/domain/hooks
- 공통 Hook은 hooks

---

### [실무]

권장 구조:

```text
src
├ components
│  ├ ui
│  │  ├ Button.tsx
│  │  ├ IconButton.tsx
│  │  ├ Card.tsx
│  │  ├ Modal.tsx
│  │  └ Badge.tsx
│  ├ form
│  │  ├ FormField.tsx
│  │  ├ TextField.tsx
│  │  ├ Select.tsx
│  │  └ Checkbox.tsx
│  ├ states
│  │  ├ LoadingState.tsx
│  │  ├ ErrorState.tsx
│  │  ├ EmptyState.tsx
│  │  └ Skeleton.tsx
│  └ layout
│     ├ PageLayout.tsx
│     ├ Stack.tsx
│     ├ CardGrid.tsx
│     └ ButtonGroup.tsx
├ features
│  ├ festival
│  │  ├ components
│  │  │  ├ FestivalCard.tsx
│  │  │  ├ FestivalFilterBar.tsx
│  │  │  └ FestivalList.tsx
│  │  └ hooks
│  │     └ useFestivals.ts
│  └ review
│     ├ components
│     │  ├ ReviewForm.tsx
│     │  └ ReviewDeleteButton.tsx
│     └ hooks
│        └ useReviews.ts
└ pages
   ├ FestivalListPage.tsx
   └ FestivalDetailPage.tsx
```

위치 판단:

```text
Button
→ components/ui

TextField
→ components/form or components/ui

LoadingState
→ components/states

FestivalCard
→ features/festival/components

ReviewForm
→ features/review/components

FestivalListPage
→ pages
```

---

### [FAQ]

Q. FestivalCard는 components/ui에 넣어?
A. 보통 아니다. festival 도메인 데이터에 의존하므로 features/festival/components에 두는 것이 적합하다.

Q. Button, Modal은 어디에 둬?
A. 여러 도메인에서 사용하는 공통 UI이므로 components/ui 또는 components/common에 둔다.

Q. LoadingState, ErrorState, EmptyState는 어디에 둬?
A. components/states 또는 components/feedback처럼 상태 UI 전용 위치에 둘 수 있다.

---

## 4.2 Common UI vs Feature UI File Boundary

### [개념]

Common UI vs Feature UI File Boundary는 Component 책임에 따라 파일 위치를 결정하는 기준이다.

파일 위치는 단순 취향이 아니라 Component 의존성과 재사용 범위를 드러낸다.

---

### [핵심]

Common UI 위치:

- components/ui
- components/common
- components/form
- components/states
- components/layout

Feature UI 위치:

- features/festival/components
- features/review/components
- features/auth/components
- features/notification/components
- features/chat/components

Page 위치:

- pages
- app routes
- route modules

Hook 위치:

- 공통 hook: hooks
- 도메인 hook: features/domain/hooks

주의:

- Common UI가 Feature 폴더를 import하지 않음
- Common UI가 domain type에 의존하지 않음
- Feature UI가 Common UI를 import하는 방향은 OK
- Page가 Feature UI를 조합
- 순환 의존 방지

---

### [실무]

좋은 의존 방향:

```text
Page
→ Feature Component
→ Common UI
```

나쁜 의존 방향:

```text
Common UI
→ Feature Component
→ Domain API
```

좋은 예:

```tsx
import { Card } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";

function FestivalCard({ festival }: { festival: Festival }) {
  return (
    <Card>
      <h3>{festival.title}</h3>
      <Badge>{festival.categoryName}</Badge>
    </Card>
  );
}
```

나쁜 예:

```tsx
import { Festival } from "@/features/festival/types";

function Card({ festival }: { festival: Festival }) {
  return <article>{festival.title}</article>;
}
```

---

### [FAQ]

Q. Common UI가 Feature type을 import해도 돼?
A. 권장하지 않는다. Common UI가 도메인 type을 알면 재사용성이 떨어지고 Feature 의존이 생긴다.

Q. Feature Component가 Common UI를 import하는 건 괜찮아?
A. 좋다. Feature UI가 Common UI를 조합하는 방향이 적절하다.

Q. Page Component는 어디까지 책임져?
A. route 단위 화면, server state 연결, Feature UI 조합, 페이지 레이아웃 구성을 담당한다.

---

# 5. Required Comparisons

## 5.1 UI Component Comparison Rules

### [개념]

UI Component Comparison Rules는 헷갈리는 Component 설계 개념을 비교해서 작성하는 기준이다.

비교 표는 RAG Retrieval에서 사용자의 질문 의도를 빠르게 매칭하고 Agent 답변 정확도를 높인다.

---

### [핵심]

필수 비교 대상:

- Common UI vs Feature UI
- Presentational Component vs Container Component
- Props vs Children
- Variant Props vs Boolean Props
- Button vs Link
- Modal vs Dialog
- Dropdown vs Select
- Tab vs Route
- Card vs List Item
- ErrorState vs EmptyState
- Spinner vs Skeleton
- Field Error vs Global Error
- className vs variant
- Component Style vs Layout Style
- Reusable Component vs Over Abstraction
- div onClick vs button

---

### [실무]

Common UI vs Feature UI:

| 기준        | Common UI           | Feature UI                 |
| ----------- | ------------------- | -------------------------- |
| 목적        | 범용 UI 제공        | 특정 도메인 UI 구현        |
| 도메인 의존 | 낮음                | 높음                       |
| API 호출    | 없음 권장           | 가능                       |
| 데이터 구조 | 모름                | 알고 있음                  |
| 예          | Button, Modal, Card | FestivalCard, ReviewForm   |
| 위치        | components/ui       | features/domain/components |
| Props       | 일반 UI Props       | 도메인 Props 가능          |

Variant Props vs Boolean Props:

| 기준        | Variant Props             | Boolean Props     |
| ----------- | ------------------------- | ----------------- |
| 목적        | 제한된 선택지             | true / false 상태 |
| 충돌 가능성 | 낮음                      | 많아질수록 증가   |
| 예          | variant="danger"          | disabled          |
| 적합 대상   | style type, semantic type | 상태, 가능 여부   |
| 주의점      | 값이 너무 많아짐          | 조합 충돌         |

Dropdown vs Select:

| 기준    | Dropdown       | Select           |
| ------- | -------------- | ---------------- |
| 목적    | 메뉴 / 액션    | Form 값 선택     |
| 요소    | button + menu  | select           |
| 값 제출 | 직접 처리      | Form과 자연 연결 |
| 접근성  | 구현 난도 높음 | native 지원      |
| 예      | 프로필 메뉴    | 지역 선택        |

ErrorState vs EmptyState:

| 기준   | ErrorState                  | EmptyState                |
| ------ | --------------------------- | ------------------------- |
| 상태   | 요청 실패                   | 요청 성공 후 데이터 없음  |
| 원인   | 네트워크 / 서버 / 권한 오류 | 검색 결과 없음 / 첫 사용  |
| Action | Retry / 로그인 / 이동       | 생성 / 필터 초기화 / 탐색 |
| 접근성 | role alert                  | 일반 section 가능         |
| 메시지 | 문제 해결 안내              | 다음 행동 안내            |

Component Style vs Layout Style:

| 기준      | Component Style          | Layout Style               |
| --------- | ------------------------ | -------------------------- |
| 목적      | 자체 모양                | 배치와 간격                |
| 예        | padding, border, variant | margin, gap, grid          |
| 위치      | Button, Card             | Stack, Grid, PageLayout    |
| 변경 영향 | Component 자체           | 화면 배치                  |
| 주의      | margin 남발 금지         | 자식 내부 스타일 침범 금지 |

---

### [FAQ]

Q. 비교 표는 왜 필요해?
A. 사용자가 자주 헷갈리는 UI Component 설계 질문에서 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. UI Component 비교 문서에서 가장 중요한 것은?
A. 공통화 기준, 책임 분리, Props 설계, 접근성, 과도한 추상화 방지를 함께 설명하는 것이다.

Q. 모든 비교를 표로 만들어야 해?
A. 필수는 아니지만 헷갈리는 개념은 표로 정리하면 Retrieval과 Review에 유리하다.

---

# 6. Troubleshooting Rules

## 6.1 Props Explosion Troubleshooting

### [개념]

Props Explosion은 Component가 너무 많은 Props를 받아 사용법이 복잡해지는 문제다.

Props Explosion은 Common UI에 Feature 요구사항을 계속 추가할 때 자주 발생한다.

---

### [핵심]

원인:

- 하나의 Component가 너무 많은 역할 담당
- 모든 예외를 Props로 처리
- boolean props 과다
- 도메인 요구사항을 공통 UI에 직접 추가
- composition 대신 props만 확장
- slot-like props 과다
- variant 값 과다
- Feature별 요구를 Common UI에 누적

해결:

- Component 책임 재정의
- Common UI / Feature UI 분리
- variant로 통합
- children / composition 사용
- slot-like props 제한
- Feature Component로 이동
- Component 분리
- 불필요한 Props 제거

---

### [실무]

문제 예:

```tsx
type ButtonProps = {
  primary?: boolean;
  secondary?: boolean;
  danger?: boolean;
  large?: boolean;
  small?: boolean;
  isReviewDelete?: boolean;
  isAdminOnly?: boolean;
  festivalId?: number;
  reviewId?: number;
  useConfirm?: boolean;
  useDeleteApi?: boolean;
};
```

개선:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "danger";
  size?: "sm" | "md" | "lg";
  loading?: boolean;
  disabled?: boolean;
  onClick?: () => void;
  children: React.ReactNode;
};
```

도메인 로직 분리:

```tsx
function ReviewDeleteButton({ reviewId }: { reviewId: number }) {
  function handleDelete() {
    deleteReview(reviewId);
  }

  return (
    <Button variant="danger" onClick={handleDelete}>
      삭제
    </Button>
  );
}
```

Debug Flow:

```text
Props 개수 확인
→ 서로 관련 없는 props 확인
→ boolean 충돌 확인
→ 도메인 props 확인
→ composition 가능 여부 확인
→ Component 분리
```

---

### [FAQ]

Q. Props가 너무 많으면 어떻게 해?
A. Component 책임을 다시 확인하고 composition, variant, Feature Component 분리를 검토한다.

Q. 도메인 전용 props를 공통 Component에 넣어도 돼?
A. 권장하지 않는다. 도메인 전용 로직은 Feature Component에 두는 것이 좋다.

Q. Props Explosion은 어떻게 찾을 수 있어?
A. Props 개수, boolean 충돌, 도메인 Props 포함 여부, Component 내부 조건문 증가 여부를 확인한다.

---

## 6.2 Over Abstraction Troubleshooting

### [개념]

Over Abstraction은 실제 필요보다 너무 범용적인 Component를 만들어 오히려 사용과 수정이 어려워지는 문제다.

UI Component는 DRY보다 명확한 책임과 사용 편의성이 우선일 수 있다.

---

### [핵심]

증상:

- Component 이름은 공통인데 사용법이 어려움
- props 조합을 이해하기 어려움
- 예외 처리가 많음
- 특정 화면 수정이 공통 Component 전체에 영향
- 재사용보다 조건문이 많음
- Component 내부가 도메인 분기로 가득함
- 문서화하기 어려움
- 단순 UI에 Compound Component 적용

해결:

- 실제 재사용 사례 확인
- 도메인 Component로 되돌리기
- 작은 UI 단위로 분리
- children / composition 활용
- 공통화 범위 축소
- Feature Component로 분리
- 단순 Props 방식으로 되돌리기

---

### [실무]

문제 예:

```tsx
type UniversalCardProps = {
  mode: "festival" | "review" | "notification";
  festival?: Festival;
  review?: Review;
  notification?: Notification;
};
```

문제점:

```text
Common Card가 도메인 데이터를 모두 앎
mode에 따라 내부 조건문 증가
새 도메인 추가 시 Common Card 수정 필요
Over Abstraction 발생
```

개선:

```tsx
function Card({ children }: { children: React.ReactNode }) {
  return <article className="card">{children}</article>;
}

function FestivalCard({ festival }: { festival: Festival }) {
  return (
    <Card>
      <h3>{festival.title}</h3>
      <p>{festival.regionName}</p>
    </Card>
  );
}

function ReviewCard({ review }: { review: Review }) {
  return (
    <Card>
      <p>{review.content}</p>
    </Card>
  );
}
```

판단 기준:

```text
공통 Component 수정 시 여러 화면이 깨짐
→ 추상화 범위 과도 가능
→ 역할별 Component 분리 검토
```

---

### [FAQ]

Q. 중복 코드를 없애려고 공통 Component를 만들었는데 더 복잡해졌어?
A. Over Abstraction일 수 있다. 반복 제거보다 역할 명확성과 사용 편의성이 중요하다.

Q. 공통화는 언제 하는 게 좋아?
A. 반복이 실제로 발생하고 역할과 props가 안정적일 때 하는 것이 좋다.

Q. 모든 Component를 처음부터 공통화해야 해?
A. 아니다. 실제 반복과 안정성이 확인된 뒤 공통화하는 것이 더 안전하다.

---

## 6.3 Accessibility Missing Troubleshooting

### [개념]

Accessibility Missing은 UI Component가 시각적으로는 동작하지만 keyboard나 보조기술 사용자가 사용하기 어려운 문제다.

접근성 누락은 UI Component Review에서 반드시 확인해야 하는 치명적 문제다.

---

### [핵심]

원인:

- div onClick 사용
- label 누락
- aria-label 누락
- focus outline 제거
- keyboard event 미지원
- color only status
- modal focus 관리 누락
- dropdown aria-expanded 누락
- tab aria-selected 누락
- error aria-describedby 누락
- icon button accessible name 누락

해결:

- semantic element 사용
- label 연결
- aria 속성 추가
- keyboard navigation 확인
- focus visible 유지
- 색상 외 텍스트 제공
- 접근성 체크리스트 적용
- 복잡한 UI는 검증된 라이브러리 검토

---

### [실무]

Debug Flow:

```text
마우스 없이 사용 가능한가?
→ Tab 이동 가능한가?
→ Enter / Space 동작하는가?
→ 스크린 리더 이름이 있는가?
→ 오류 메시지와 input이 연결되는가?
→ focus가 보이는가?
```

나쁜 예:

```tsx
<div onClick={onClose}>닫기</div>
```

개선:

```tsx
<button type="button" onClick={onClose}>
  닫기
</button>
```

나쁜 예:

```tsx
<button type="button">
  <CloseIcon />
</button>
```

개선:

```tsx
<button type="button" aria-label="닫기">
  <CloseIcon aria-hidden="true" />
</button>
```

---

### [FAQ]

Q. 마우스로 잘 되면 접근성 문제는 없는 거야?
A. 아니다. 키보드와 스크린 리더 사용자가 사용할 수 있는지도 확인해야 한다.

Q. 아이콘 버튼 접근성 문제는 어떻게 찾을 수 있어?
A. 시각적 텍스트가 없는 버튼에 aria-label이 있는지 확인해야 한다.

Q. 색상만으로 상태를 표시해도 돼?
A. 권장하지 않는다. 텍스트나 아이콘 등 색상 외 정보도 함께 제공해야 한다.

---

# 7. Common Mistakes

## 7.1 UI Component Common Mistakes

### [개념]

UI Component Common Mistakes는 UI Component 설계와 구현에서 반복적으로 발생하는 실수 목록이다.

Common Mistakes는 Frontend Agent가 코드 생성 후 자체 검수하고 Review Agent가 치명적 문제를 빠르게 찾기 위해 사용한다.

---

### [핵심]

자주 발생하는 실수:

- 공통 UI Component에 API 호출 포함
- Common UI와 Feature UI 혼동
- 모든 UI를 처음부터 공통화
- Props가 너무 많아짐
- boolean props로 variant를 대체
- 색상명 variant 사용
- Button 기본 type 누락
- div onClick 남용
- 아이콘 버튼 aria-label 누락
- input label 누락
- Error Message aria-describedby 누락
- Modal 접근성 누락
- Dropdown keyboard 접근성 누락
- Card에 div onClick 사용
- List key로 index 사용
- EmptyState 없이 빈 목록 표시
- 공통 Component에 margin 포함
- className 확장 기준 없음
- 과도한 추상화
- Feature 요구사항을 Common UI에 계속 추가
- Component 파일 위치 혼동
- SearchBox 내부 API 호출
- FilterBar 내부 API 호출
- Field Error와 Global Error 혼동

---

### [실무]

문제 연결 예:

```text
문제: Button Component가 reviewId를 받아 deleteReview API를 호출함
원인: 공통 UI Component와 Feature Component 책임 혼동
해결: Button은 UI만 담당하고 ReviewDeleteButton에서 API 호출 처리
```

```text
문제: TextField에 placeholder만 있고 label 없음
원인: 입력 접근성 기준 누락
해결: label + id/htmlFor 연결 추가
```

```text
문제: Card가 grid 배치와 margin까지 담당
원인: Component Style과 Layout Style 혼동
해결: Card는 자체 스타일만 담당하고 CardGrid가 배치 담당
```

---

### [FAQ]

Q. UI Component 초보가 가장 많이 하는 실수는?
A. 공통 UI와 Feature UI를 구분하지 못하거나, Props를 계속 추가해 만능 Component를 만드는 실수가 많다.

Q. UI Component 문제는 어떻게 찾는 게 좋아?
A. Component 책임, Props 개수, 도메인 의존성, 접근성, 스타일 책임, 재사용 범위를 순서대로 확인한다.

Q. Common Mistakes는 문서에 꼭 넣어야 해?
A. 좋다. Review Agent가 치명적 문제를 빠르게 찾고 Retrieval Query 매칭도 강화된다.

---

# 8. Final UI Component Checklist

## 8.1 Final Review Checklist

### [개념]

Final Review Checklist는 UI Component Pattern 문서 전체를 마무리할 때 사용하는 최종 검수 기준이다.

Frontend Agent와 Review Agent는 UI Component 생성, 수정, 리팩토링 요청 후 이 Checklist를 기준으로 최종 품질을 확인해야 한다.

---

### [핵심]

Final Checklist:

```md
- [ ] Component 책임이 명확한가?
- [ ] Common UI와 Feature UI가 구분되었는가?
- [ ] 도메인 로직이 공통 UI에 들어가지 않았는가?
- [ ] API 호출이 공통 UI에 들어가지 않았는가?
- [ ] Props 이름이 명확한가?
- [ ] variant / size 기준이 포함되었는가?
- [ ] boolean props 과다 사용을 피했는가?
- [ ] children / composition 기준이 적용되었는가?
- [ ] Event Handler props 기준이 일관적인가?
- [ ] Button / Input / Modal / Card / List 패턴이 적절한가?
- [ ] LoadingState / ErrorState / EmptyState 기준이 적용되었는가?
- [ ] Form label과 error 연결이 적절한가?
- [ ] Semantic HTML을 사용했는가?
- [ ] 접근성 속성이 포함되었는가?
- [ ] Keyboard 접근성을 고려했는가?
- [ ] Styling Boundary가 분리되었는가?
- [ ] Layout Responsibility가 분리되었는가?
- [ ] File Structure가 적절한가?
- [ ] Props Explosion이 없는가?
- [ ] Over Abstraction이 없는가?
- [ ] Common Mistakes를 피했는가?
- [ ] Troubleshooting 기준으로 치명적 문제를 확인했는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

최종 검수 Flow:

```text
Draft
→ Responsibility Check
→ Reusability Check
→ Props API Check
→ Composition Check
→ Accessibility Check
→ Styling Boundary Check
→ File Structure Check
→ Anti Pattern Check
→ Troubleshooting Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

치명적 문제:

```text
Common UI 내부 API 호출
Common UI 내부 domain field 직접 참조
Common UI props에 festivalId / reviewId / userId 직접 요구
Button 기본 type 누락
div onClick으로 클릭 UI 구현
label 없는 input
aria-label 없는 icon button
error aria-describedby 누락
Modal role dialog 누락
List key index 사용
EmptyState 누락
State UI 내부 API 호출
SearchBox 내부 API 호출
Props Explosion
Over Abstraction
```

---

### [FAQ]

Q. UI Component 최종 검수에서 가장 먼저 볼 것은 뭐야?
A. Component 책임이 명확한지, Common UI와 Feature UI가 섞이지 않았는지 먼저 확인한다.

Q. UI Component에서 치명적인 문제는 뭐야?
A. 공통 UI에 API 호출이나 도메인 로직이 들어가고, props가 과도하게 늘어나며, 접근성이 누락되는 문제다.

Q. Review Agent는 최종적으로 무엇을 확인해야 해?
A. 책임 분리, Props API, 접근성, 스타일 경계, 파일 위치, Props Explosion, Over Abstraction, Retrieval Queries 포함 여부를 확인해야 한다.

---

# 9. Retrieval Optimization Rules

## 9.1 Keyword Rules

### [개념]

Retrieval Optimization Rules는 UI Component Pattern 문서가 RAG 검색에서 잘 검색되도록 핵심 키워드와 실제 질문 표현을 포함하는 기준이다.

문서는 사람이 읽기 좋은 설명보다 Agent Retrieval Hit와 Semantic Search Matching을 우선한다.

---

### [핵심]

강조 키워드:

- UI Component Pattern
- React UI Component
- Reusable Component
- Common UI
- Feature UI
- Presentational Component
- Container Component
- Props Design
- Variant Props
- Size Props
- Boolean Props
- Event Handler Props
- Children Pattern
- Composition Pattern
- Slot Pattern
- Compound Component
- Button Component
- TextField Component
- Modal Component
- Dialog Component
- Card Component
- Badge Component
- List Component
- Table Component
- Tab Component
- Dropdown Component
- LoadingState
- ErrorState
- EmptyState
- Skeleton Component
- Form Field
- SearchBox
- FilterBar
- Accessibility
- Styling Boundary
- className
- Layout Responsibility
- File Structure
- Component Responsibility
- Over Abstraction
- Props Explosion

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

```text
공통 Component는 언제 만들어?
UI Component props는 어떻게 설계해?
variant는 어떻게 설계해?
boolean props가 많으면 왜 안 좋아?
Button 기본 type은 뭐가 좋아?
Modal은 어떻게 만들어?
Card는 공통 Component야?
FestivalCard는 어디에 둬?
EmptyState는 어떻게 만들어?
div onClick을 써도 돼?
className을 열어줘야 해?
Component에 margin을 넣어도 돼?
Props가 너무 많으면 어떻게 해?
공통화했는데 더 복잡해졌어
```

Retrieval Query 작성 기준:

- Q + A 모두 작성
- 실제 질문형 표현 사용
- 답변은 1~4줄
- 장문 금지
- 핵심 키워드 반복 허용
- [면접] 섹션 사용 금지
- [FAQ] 섹션 사용

---

### [FAQ]

Q. 키워드 반복은 중복이야?
A. 불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. FAQ 질문은 어떤 스타일이 좋아?
A. 실제 사용자가 검색하거나 질문할 법한 문장형 질문이 좋다.

Q. Retrieval Queries는 왜 마지막에 넣어?
A. 사용자 질문과 RAG 검색 매칭을 강화하고 Agent 답변 정확도를 높이기 위해서다.

---

# Retrieval Queries

### [FAQ]

Q. Part08은 왜 필요해?
A. UI Component 문서 전체를 접근성, 스타일 경계, 파일 구조, Common Mistakes, Troubleshooting 기준으로 최종 검수하기 위해 필요하다.

Q. UI Component 최종 검수에서 가장 중요한 것은 뭐야?
A. Component 책임, Props API, 접근성, Styling Boundary, Common UI / Feature UI 분리, 과도한 추상화 방지다.

Q. UI Component Accessibility는 뭐야?
A. keyboard 사용자와 보조기술 사용자도 UI Component를 사용할 수 있도록 semantic HTML과 ARIA 속성을 제공하는 기준이다.

Q. div에 onClick을 붙이면 안 돼?
A. 가능은 하지만 키보드 접근성과 의미가 부족하다. 클릭 액션은 button, 이동은 Link나 anchor를 사용하는 것이 좋다.

Q. 아이콘 버튼에는 텍스트가 없어도 돼?
A. 시각적 텍스트가 없다면 aria-label로 버튼의 목적을 제공해야 한다.

Q. input error는 어떻게 접근성 연결해?
A. error message id를 만들고 input의 aria-describedby에 연결하며 aria-invalid를 함께 사용한다.

Q. 클릭 가능한 Card는 div로 만들어도 돼?
A. 권장하지 않는다. 링크 이동이면 Link나 anchor, 액션이면 button을 사용하는 것이 접근성에 좋다.

Q. Table 대신 div로 만들어도 돼?
A. 표 형태의 데이터라면 table 요소를 사용하는 것이 의미와 접근성에 좋다.

Q. form 태그는 꼭 써야 해?
A. 검색이나 제출 UI에서는 form을 사용하면 Enter 제출과 접근성 측면에서 유리하다.

Q. focus outline을 없애도 돼?
A. 권장하지 않는다. 대신 디자인에 맞는 focus visible 스타일을 제공하는 것이 좋다.

Q. hover로만 열리는 UI는 괜찮아?
A. 권장하지 않는다. keyboard focus로도 접근 가능해야 한다.

Q. div onClick에 keydown을 추가하면 button과 같아?
A. 일부 보완은 가능하지만 native button을 사용하는 것이 더 안전하고 단순하다.

Q. Styling Boundary는 뭐야?
A. UI Component 자체 스타일과 부모 Layout이 담당할 배치 스타일을 분리하는 기준이다.

Q. 공통 Component에 className을 열어줘야 해?
A. 프로젝트 기준에 따라 다르지만 외부 확장이 필요한 경우 className을 허용하면 유연하다.

Q. Button 안에 margin을 넣어도 돼?
A. 공통 Button에는 margin을 넣지 않는 것이 좋다. 버튼 간 간격은 부모 Layout이나 ButtonGroup이 담당하는 편이 유연하다.

Q. style prop을 많이 쓰면 안 돼?
A. 동적 스타일에는 사용할 수 있지만 일관성 있는 UI를 위해 variant, size, className 기준을 우선하는 것이 좋다.

Q. Card가 grid 배치까지 담당해야 해?
A. 보통 Card는 자체 모양만 담당하고 grid 배치는 부모 List나 Layout Component가 담당한다.

Q. Layout Component는 왜 필요해?
A. UI Component 자체 스타일과 화면 배치 책임을 분리해 재사용성과 유지보수성을 높이기 위해 필요하다.

Q. 공통 Component에 gap props를 많이 넣어도 돼?
A. 제한적으로 가능하지만 여러 Component 사이의 간격은 Stack, Grid, ButtonGroup 같은 Layout Component가 담당하는 것이 좋다.

Q. 공통 Button에 margin을 넣었더니 화면마다 간격이 이상해?
A. Button 자체에 margin을 넣으면 부모 layout과 충돌할 수 있다. 간격은 ButtonGroup이나 부모 layout에서 관리하는 것이 좋다.

Q. className으로 외부 스타일을 덮어도 돼?
A. 가능하지만 기준이 없으면 스타일 충돌이 생긴다. 공통 Component의 확장 규칙을 정하는 것이 좋다.

Q. Feature 전용 스타일은 어디에 둬?
A. Feature Component className이나 Feature 스타일 파일에서 처리하는 것이 좋다.

Q. UI Component 파일 구조는 어떻게 나눠?
A. 공통 UI는 components/ui, 상태 UI는 components/states, Layout은 components/layout, 도메인 UI는 features/domain/components에 둔다.

Q. FestivalCard는 components/ui에 넣어?
A. 보통 아니다. festival 도메인 데이터에 의존하므로 features/festival/components에 두는 것이 적합하다.

Q. Button, Modal은 어디에 둬?
A. 여러 도메인에서 사용하는 공통 UI이므로 components/ui 또는 components/common에 둔다.

Q. LoadingState, ErrorState, EmptyState는 어디에 둬?
A. components/states 또는 components/feedback처럼 상태 UI 전용 위치에 둘 수 있다.

Q. Common UI가 Feature type을 import해도 돼?
A. 권장하지 않는다. Common UI가 도메인 type을 알면 재사용성이 떨어지고 Feature 의존이 생긴다.

Q. Feature Component가 Common UI를 import하는 건 괜찮아?
A. 좋다. Feature UI가 Common UI를 조합하는 방향이 적절하다.

Q. Page Component는 어디까지 책임져?
A. route 단위 화면, server state 연결, Feature UI 조합, 페이지 레이아웃 구성을 담당한다.

Q. 비교 표는 왜 필요해?
A. 사용자가 자주 헷갈리는 UI Component 설계 질문에서 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. UI Component 비교 문서에서 가장 중요한 것은?
A. 공통화 기준, 책임 분리, Props 설계, 접근성, 과도한 추상화 방지를 함께 설명하는 것이다.

Q. Props가 너무 많으면 어떻게 해?
A. Component 책임을 다시 확인하고 composition, variant, Feature Component 분리를 검토한다.

Q. 도메인 전용 props를 공통 Component에 넣어도 돼?
A. 권장하지 않는다. 도메인 전용 로직은 Feature Component에 두는 것이 좋다.

Q. Props Explosion은 어떻게 찾을 수 있어?
A. Props 개수, boolean 충돌, 도메인 Props 포함 여부, Component 내부 조건문 증가 여부를 확인한다.

Q. 중복 코드를 없애려고 공통 Component를 만들었는데 더 복잡해졌어?
A. Over Abstraction일 수 있다. 반복 제거보다 역할 명확성과 사용 편의성이 중요하다.

Q. 공통화는 언제 하는 게 좋아?
A. 반복이 실제로 발생하고 역할과 props가 안정적일 때 하는 것이 좋다.

Q. 모든 Component를 처음부터 공통화해야 해?
A. 아니다. 실제 반복과 안정성이 확인된 뒤 공통화하는 것이 더 안전하다.

Q. 마우스로 잘 되면 접근성 문제는 없는 거야?
A. 아니다. 키보드와 스크린 리더 사용자가 사용할 수 있는지도 확인해야 한다.

Q. 아이콘 버튼 접근성 문제는 어떻게 찾을 수 있어?
A. 시각적 텍스트가 없는 버튼에 aria-label이 있는지 확인해야 한다.

Q. 색상만으로 상태를 표시해도 돼?
A. 권장하지 않는다. 텍스트나 아이콘 등 색상 외 정보도 함께 제공해야 한다.

Q. UI Component 초보가 가장 많이 하는 실수는?
A. 공통 UI와 Feature UI를 구분하지 못하거나, Props를 계속 추가해 만능 Component를 만드는 실수가 많다.

Q. UI Component 문제는 어떻게 찾는 게 좋아?
A. Component 책임, Props 개수, 도메인 의존성, 접근성, 스타일 책임, 재사용 범위를 순서대로 확인한다.

Q. UI Component 최종 검수에서 가장 먼저 볼 것은 뭐야?
A. Component 책임이 명확한지, Common UI와 Feature UI가 섞이지 않았는지 먼저 확인한다.

Q. UI Component에서 치명적인 문제는 뭐야?
A. 공통 UI에 API 호출이나 도메인 로직이 들어가고, props가 과도하게 늘어나며, 접근성이 누락되는 문제다.

Q. Review Agent는 최종적으로 무엇을 확인해야 해?
A. 책임 분리, Props API, 접근성, 스타일 경계, 파일 위치, Props Explosion, Over Abstraction, Retrieval Queries 포함 여부를 확인해야 한다.

Q. 키워드 반복은 중복이야?
A. 불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. FAQ 질문은 어떤 스타일이 좋아?
A. 실제 사용자가 검색하거나 질문할 법한 문장형 질문이 좋다.

Q. Retrieval Queries는 왜 마지막에 넣어?
A. 사용자 질문과 RAG 검색 매칭을 강화하고 Agent 답변 정확도를 높이기 위해서다.
