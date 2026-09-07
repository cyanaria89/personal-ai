# UI Component Pattern Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

UI Component Pattern Domain 문서는 Frontend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- 재사용 가능한 UI Component 설계 기준 제공
- Button / Input / Modal / Card / List / Table / Tab / Dropdown 같은 공통 UI Pattern 정리
- Presentational Component와 Feature Component 구분 지원
- Props 설계 기준 제공
- Variant / Size / State / Event Handler 설계 지원
- Loading / Error / Empty 상태 UI Component화 기준 제공
- 접근성 있는 UI Component 작성 기준 제공
- 일관된 디자인 시스템 확장 기반 제공
- 과도한 추상화와 중복 Component 생성을 방지
- 유지보수 가능한 UI Component 구조 설계 지원

---

### [핵심]

우선순위:

1. UI Component Responsibility
2. Reusable Component
3. Presentational Component
4. Feature Component
5. Props Design
6. Variant Pattern
7. Size Pattern
8. State Pattern
9. Event Handler Pattern
10. Composition Pattern
11. Children Pattern
12. Slot Pattern Basics
13. Accessibility
14. Loading / Error / Empty Component
15. Component Naming
16. Styling Boundary
17. Anti Pattern

---

### [실무]

2026 실무 기준에서 UI Component Pattern 문서는 단순 Component 모음집이 아니다.

Frontend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- UI Component 책임 분리
- 재사용 가능한 Component 설계
- 도메인 UI와 공통 UI 구분
- Props 인터페이스 설계
- Variant / Size / Disabled / Loading 상태 설계
- children / composition 활용
- 접근성 속성 포함
- 공통 상태 UI 작성
- 디자인 일관성 유지
- 중복 Component 통합
- 과도한 추상화 방지
- UI Component Review 기준 제공

---

### [FAQ]

Q. UI Component Pattern 문서는 React Component Design과 뭐가 달라?

A.
React Component Design은 Component 분리와 상태 위치를 다루고, UI Component Pattern은 Button, Modal, Card 같은 재사용 UI 단위의 설계 기준에 집중한다.

Q. UI Component Pattern에서 가장 중요한 기준은 뭐야?

A.
Component 책임, Props 설계, 재사용 범위, Variant 설계, 접근성, 과도한 추상화 방지다.

Q. 모든 UI를 공통 Component로 만들어야 해?

A.
아니다. 반복되고 의미가 안정적인 UI만 공통화하고, 한 화면에서만 쓰이는 UI는 Feature Component로 두는 것이 좋다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

UI Component Pattern 문서는 재사용 UI 설계에 필요한 범위를 포함한다.

포함 범위:

- UI Component Responsibility
- Reusable Component
- Presentational Component
- Feature Component
- Layout Component
- Base Component
- Compound Component Basics
- Composition Pattern
- Children Pattern
- Slot-like Pattern
- Props Design
- Variant Props
- Size Props
- Boolean Props
- Event Handler Props
- Controlled / Uncontrolled UI Basics
- Button Component
- Input Component
- Textarea Component
- Select Component
- Checkbox Component
- Radio Component
- Modal Component
- Dialog Component
- Card Component
- List Component
- Table Component
- Tab Component
- Dropdown Component
- Accordion Component
- Badge Component
- Avatar Component
- Tooltip Basics
- Toast Basics
- LoadingState Component
- ErrorState Component
- EmptyState Component
- Skeleton Component
- Pagination Component
- SearchBox Component
- FilterBar Component
- Accessibility
- Styling Boundary
- Naming Convention
- UI Component Troubleshooting

---

### [핵심]

반드시 포함:

- UI Component는 역할이 명확해야 함
- 공통 UI와 도메인 UI를 구분해야 함
- 재사용성은 실제 반복이 있을 때 강화
- Props는 사용 의도를 드러내야 함
- variant / size / disabled / loading 기준을 통일
- boolean props 과다 사용을 주의
- children과 composition으로 유연성 확보
- 접근성 속성은 Component 책임에 포함
- API 호출은 공통 UI Component에 넣지 않음
- 도메인 로직은 Feature Component로 분리
- 너무 범용적인 만능 Component를 만들지 않음

---

### [실무]

UI Component Pattern은 Component Design 이후 공통 UI를 정리하는 단계에서 사용한다.

실무 연결:

```text
React Component Design
→ UI Component Pattern
→ State Management
→ Error Handling & Loading UX
→ Frontend Accessibility
→ Design System
```

---

### [FAQ]

Q. UI Component Pattern 문서에서 Design System도 다뤄?

A.
기초 기반은 포함하지만 색상 토큰, 테마 시스템, Storybook, 디자인 시스템 운영 심화는 별도 문서에서 다룬다.

Q. Tailwind나 CSS-in-JS도 여기서 다뤄?

A.
스타일 경계와 className 전달 기준은 포함하지만 Tailwind / CSS-in-JS 심화는 Styling 문서에서 다룬다.

Q. Compound Component도 깊게 다뤄?

A.
기초 개념과 사용 기준만 포함한다. 고급 Compound Pattern은 Advanced React Pattern 문서에서 다룬다.

---

## 2.2 Excluded Scope

### [개념]

UI Component Pattern 문서에서는 고급 디자인 시스템 운영과 특정 스타일링 도구 심화를 제외한다.

제외 범위:

- Full Design System Architecture
- Design Token System 심화
- Storybook 심화
- Chromatic / Visual Regression 심화
- Tailwind CSS 심화
- CSS-in-JS 심화
- Headless UI 심화
- Radix UI 심화
- Animation Library 심화
- Framer Motion 심화
- Canvas / SVG / WebGL UI
- Advanced Compound Component
- Render Props 심화
- Polymorphic Component 심화
- Accessibility Full Audit
- Micro Frontend UI Sharing

---

### [핵심]

제외 이유:

- Foundation 범위 초과
- Styling / Accessibility / Design System 문서와 분리 필요
- Agent Retrieval 혼선 방지
- Chunk 품질 유지
- 실무 UI Component Pattern 기준에 집중

---

### [실무]

고급 기술은 별도 Domain Rules에서 관리한다.

예:

```text
UI Component Pattern
→ Frontend Accessibility
→ Styling Architecture
→ Design System
→ Storybook
→ Advanced React Pattern
```

---

### [FAQ]

Q. Storybook 사용법도 여기서 다뤄?

A.
아니다. Component 문서화 필요성은 언급할 수 있지만 Storybook 사용법은 별도 문서에서 다룬다.

Q. Radix UI 같은 Headless UI도 여기서 다뤄?

A.
기초 선택 기준은 언급 가능하지만 라이브러리 사용법은 별도 문서가 적합하다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

UI Component Pattern RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

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
- [실무]: 실제 UI Component 설계 기준
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

Q. 모든 UI Component 문서에 FAQ가 필요해?

A.
필요하다. FAQ는 사용자 질문과 RAG 검색 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

UI Component Pattern 문서에는 설계 기준과 오류 검증을 위해 추가 Section을 포함할 수 있다.

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

- Component 책임 설명 → [Flow], [Checklist]
- Props 설계 설명 → [예제], [Best Practice]
- Button / Modal / Card 패턴 → [예제]
- Variant 설계 → [Comparison], [주의]
- 접근성 설명 → [Checklist], [주의]
- Anti Pattern 설명 → [Troubleshooting]

---

### [실무]

예시:

```md
### [Flow]

Identify UI Repetition
→ Define Responsibility
→ Decide Common or Feature Component
→ Design Props
→ Add Accessibility
→ Review Reusability
```

---

### [FAQ]

Q. UI Component 문서에 Comparison이 중요한 이유는?

A.
공통 Component와 Feature Component, variant와 boolean props, composition과 props drilling 같은 선택 기준이 자주 헷갈리기 때문이다.

Q. UI Component 문서에 Troubleshooting이 필요한 이유는?

A.
Props가 복잡해지거나 Component가 너무 범용화되거나 접근성이 누락되는 문제가 자주 발생하기 때문이다.

---

# 4. UI Component Responsibility Rules

## 4.1 Component Responsibility

### [개념]

UI Component Responsibility는 Component가 담당하는 역할과 책임 범위를 명확히 정하는 기준이다.

UI Component는 화면 표현과 사용자 상호작용을 담당하되, 도메인 API 로직이나 복잡한 비즈니스 로직을 직접 포함하지 않는 것이 좋다.

---

### [핵심]

책임 기준:

- 화면 표시
- 사용자 입력
- 클릭 이벤트 전달
- 시각 상태 표현
- 접근성 속성 제공
- 스타일 variant 적용
- loading / disabled 상태 표현
- error message 표시

포함하지 않는 것이 좋은 책임:

- 직접 API 호출
- 인증 판단 심화
- 도메인 데이터 가공 심화
- 서버 상태 캐싱
- 복잡한 비즈니스 규칙
- route 이동 정책 심화

---

### [실무]

책임 분리 예:

```text
Button Component
→ 클릭 가능한 공통 버튼 UI 제공

ReviewSubmitButton
→ 리뷰 등록이라는 도메인 액션 연결

ReviewForm
→ 입력값 검증과 제출 흐름 관리
```

잘못된 예:

```jsx
function Button({ reviewId }) {
  async function handleClick() {
    await deleteReview(reviewId);
  }

  return <button onClick={handleClick}>삭제</button>;
}
```

개선 예:

```jsx
function Button({ children, onClick, disabled }) {
  return (
    <button type="button" onClick={onClick} disabled={disabled}>
      {children}
    </button>
  );
}
```

---

### [FAQ]

Q. 공통 Button Component 안에서 API 호출을 해도 돼?

A.
권장하지 않는다. 공통 Button은 UI 역할만 담당하고 API 호출은 Feature Component나 Hook에서 처리하는 것이 좋다.

Q. UI Component의 책임은 어디까지야?

A.
화면 표시, 사용자 이벤트 전달, 접근성, 시각 상태 표현까지가 기본 책임이다.

---

## 4.2 Common UI vs Feature UI

### [개념]

Common UI는 여러 화면에서 반복 사용할 수 있는 범용 UI Component다.

Feature UI는 특정 도메인이나 기능에 맞춰진 Component다.

---

### [핵심]

Common UI 예:

- Button
- TextField
- Modal
- Card
- Badge
- LoadingState
- EmptyState
- ErrorState
- Pagination

Feature UI 예:

- FestivalCard
- ReviewForm
- LoginForm
- NotificationItem
- ChatMessageBubble
- DonationButton
- FestivalSearchFilter

---

### [실무]

분리 기준:

```text
여러 도메인에서 반복 사용 → Common UI
특정 도메인 데이터 구조에 의존 → Feature UI
특정 API 응답 필드에 의존 → Feature UI
스타일과 상호작용만 제공 → Common UI
```

예:

```tsx
function Card({ children }) {
  return <article className="card">{children}</article>;
}

function FestivalCard({ festival }) {
  return (
    <Card>
      <h3>{festival.title}</h3>
      <p>{festival.regionName}</p>
    </Card>
  );
}
```

권장:

- Common UI는 도메인 용어를 모르게 작성
- Feature UI는 도메인 데이터와 사용자 시나리오를 반영
- Common UI가 Feature 요구사항을 모두 끌어안지 않게 주의
- Feature UI에서 Common UI를 조합

---

### [FAQ]

Q. FestivalCard는 공통 Component야?

A.
보통 Feature UI다. festival 데이터 구조에 의존하기 때문이다.

Q. Card Component와 FestivalCard는 뭐가 달라?

A.
Card는 범용 컨테이너이고 FestivalCard는 축제 정보를 보여주는 도메인 Component다.

---

## 4.3 Reusability Criteria

### [개념]

Reusability Criteria는 Component를 재사용 가능하게 만들지 판단하는 기준이다.

재사용성은 예상이 아니라 실제 반복과 안정적인 역할을 기준으로 판단한다.

---

### [핵심]

공통화 적합 기준:

- 여러 화면에서 반복 사용
- 역할이 명확함
- Props가 단순함
- 도메인 의존이 적음
- 스타일 변형이 제한적임
- 접근성 처리 반복 가능
- 테스트 가능함

공통화 부적합 기준:

- 한 화면에서만 사용
- 도메인 로직이 강함
- Props가 계속 늘어남
- 예외 케이스가 많음
- 이름은 공통이지만 실제 요구가 다름

---

### [실무]

공통화 판단 Flow:

```text
UI가 반복되는가?
→ 역할이 같은가?
→ 도메인 의존이 없는가?
→ Props가 안정적인가?
→ 공통 UI로 분리
```

주의:

- 처음부터 모든 UI를 공통화하지 않음
- 두세 번 반복된 뒤 공통화해도 늦지 않음
- 공통 Component가 예외 props로 가득 차면 분리 재검토
- 재사용성보다 명확성이 우선

---

### [FAQ]

Q. Component는 처음부터 재사용 가능하게 만들어야 해?

A.
항상 그럴 필요는 없다. 실제 반복과 역할 안정성이 확인된 후 공통화하는 것이 더 안전하다.

Q. 공통 Component props가 너무 많아지면?

A.
역할이 너무 커졌을 가능성이 있다. Component 분리나 composition을 검토한다.

---

# 5. Props Design Rules

## 5.1 Props Naming Rules

### [개념]

Props Naming은 Component 사용자가 의도를 쉽게 이해할 수 있도록 Props 이름을 정하는 기준이다.

---

### [핵심]

Naming 기준:

- 명확한 의미
- 도메인 의존 최소화
- boolean은 is / has / disabled / loading
- event handler는 on으로 시작
- 내부 handler는 handle로 시작
- children 활용
- value / defaultValue 구분
- variant / size 통일

---

### [실무]

좋은 예:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "danger";
  size?: "sm" | "md" | "lg";
  loading?: boolean;
  disabled?: boolean;
  onClick?: () => void;
  children: ReactNode;
};
```

나쁜 예:

```tsx
type ButtonProps = {
  blue?: boolean;
  red?: boolean;
  big?: boolean;
  isReviewDeleteButton?: boolean;
};
```

권장:

- 색상명보다 의미 기반 variant 사용
- `onClick`, `onClose`, `onSubmit`, `onChange`처럼 이벤트 이름 통일
- `isOpen`, `hasError`, `disabled`, `loading`처럼 boolean 의미 명확화
- 도메인 전용 Props는 Feature Component에 둠

---

### [FAQ]

Q. boolean props 이름은 어떻게 지어?

A.
상태를 나타내면 is / has를 사용하고, HTML 속성과 유사한 경우 disabled, required, loading처럼 명확히 쓴다.

Q. Button variant는 blue, red로 만들면 안 돼?

A.
가능은 하지만 primary, secondary, danger처럼 의미 기반 이름이 디자인 변경에 더 유연하다.

---

## 5.2 Variant Props Rules

### [개념]

Variant Props는 Component의 시각적 또는 의미적 변형을 제한된 값으로 표현하는 Props다.

---

### [핵심]

사용 대상:

- button variant
- badge variant
- alert variant
- card variant
- text field status
- modal size
- toast type

예:

```text
primary
secondary
danger
ghost
outline
success
warning
error
info
```

---

### [실무]

예:

```tsx
type ButtonVariant = "primary" | "secondary" | "danger" | "ghost";

type ButtonProps = {
  variant?: ButtonVariant;
  children: ReactNode;
};

function Button({ variant = "primary", children }: ButtonProps) {
  return <button className={`button button-${variant}`}>{children}</button>;
}
```

권장:

- 제한된 union type 사용
- 의미 기반 variant 이름 사용
- 색상명 직접 노출 지양
- variant 조합이 많아지면 분리 검토
- 디자인 시스템 토큰과 연결 가능

주의:

- `primary`, `danger` 같은 의미 기준 유지
- `red`, `blue`, `pink`처럼 색상 직접 의존은 변경에 취약
- variant가 너무 많으면 Component 책임이 커진 것

---

### [FAQ]

Q. variant는 왜 union type으로 제한해?

A.
허용되는 스타일 종류를 명확히 하고 잘못된 문자열 사용을 방지하기 위해서다.

Q. variant가 너무 많아지면 어떻게 해?

A.
Component 책임이 너무 넓어진 것일 수 있으므로 별도 Component나 composition을 검토한다.

---

## 5.3 Size Props Rules

### [개념]

Size Props는 Component 크기를 제한된 값으로 제어하는 Props다.

---

### [핵심]

사용 대상:

- Button size
- Input size
- Modal size
- Avatar size
- Badge size
- Spinner size

예:

```text
sm
md
lg
full
compact
```

---

### [실무]

예:

```tsx
type ButtonSize = "sm" | "md" | "lg";

type ButtonProps = {
  size?: ButtonSize;
  children: ReactNode;
};

function Button({ size = "md", children }: ButtonProps) {
  return <button className={`button button-${size}`}>{children}</button>;
}
```

권장:

- size 이름 통일
- 기본값 제공
- 임의 숫자 props 남발 지양
- width와 size 역할 구분
- 반응형 처리는 className 또는 layout에서 처리 가능

---

### [FAQ]

Q. Button size는 px 값으로 받는 게 좋아?

A.
공통 Component에서는 sm, md, lg처럼 제한된 크기 값을 사용하는 것이 일관성에 좋다.

Q. full width 버튼은 size야 variant야?

A.
보통 size보다 layout 성격이 강하므로 `fullWidth` 같은 별도 prop으로 둘 수 있다.

---

## 5.4 Boolean Props Rules

### [개념]

Boolean Props는 true / false로 Component 상태를 제어하는 Props다.

간단하지만 많아질수록 조합 복잡도가 증가한다.

---

### [핵심]

사용 대상:

- disabled
- loading
- required
- selected
- checked
- open
- invalid
- fullWidth

주의 대상:

- primary
- secondary
- danger
- large
- small
- isSpecial
- isFestivalMode

---

### [실무]

좋은 예:

```tsx
<Button variant="danger" loading disabled>
  삭제
</Button>
```

나쁜 예:

```tsx
<Button danger primary large small>
  삭제
</Button>
```

권장:

- 상호 배타적인 값은 boolean 여러 개보다 variant 사용
- 상태성 boolean은 명확하게 사용
- boolean props가 많아지면 API 복잡도 점검
- 도메인 전용 boolean은 Feature Component로 이동

---

### [FAQ]

Q. boolean props가 많으면 왜 문제야?

A.
서로 충돌하는 조합이 생기고 Component 사용법이 복잡해지기 때문이다.

Q. primary, danger를 boolean으로 두면 안 돼?

A.
가능은 하지만 동시에 true가 될 수 있어 variant union으로 제한하는 것이 더 안전하다.

---

# 6. Event Handler Pattern Rules

## 6.1 Event Handler Props

### [개념]

Event Handler Props는 Component 내부에서 발생한 사용자 이벤트를 외부로 전달하는 Props다.

공통 UI Component는 이벤트가 발생했다는 사실만 전달하고 실제 도메인 로직은 부모가 처리한다.

---

### [핵심]

Naming 기준:

- onClick
- onChange
- onSubmit
- onClose
- onOpen
- onSelect
- onConfirm
- onCancel
- onRetry
- onReset

내부 함수 기준:

- handleClick
- handleChange
- handleSubmit
- handleClose
- handleSelect

---

### [실무]

예:

```tsx
type ModalProps = {
  open: boolean;
  onClose: () => void;
  children: ReactNode;
};

function Modal({ open, onClose, children }: ModalProps) {
  if (!open) {
    return null;
  }

  return (
    <div role="dialog" aria-modal="true">
      <button type="button" onClick={onClose}>
        닫기
      </button>
      {children}
    </div>
  );
}
```

권장:

- Props는 `onX` 형태
- 내부 handler는 `handleX` 형태
- 공통 UI에서 도메인 API 직접 호출 금지
- event 객체를 넘길지 value만 넘길지 기준 통일
- callback이 optional이면 호출 전 확인

---

### [FAQ]

Q. onClick 안에서 API 호출을 넣어도 돼?

A.
Feature Component에서는 가능하지만 공통 UI Component에서는 부모로 이벤트를 전달하는 것이 좋다.

Q. onChange는 event를 넘기는 게 좋아 value를 넘기는 게 좋아?

A.
공통 input은 event를 넘기거나 value를 넘길 수 있다. 프로젝트 컨벤션을 통일하는 것이 중요하다.

---

## 6.2 Confirm / Cancel Pattern

### [개념]

Confirm / Cancel Pattern은 Modal, Dialog, 위험 액션에서 확인과 취소 이벤트를 분리하는 패턴이다.

---

### [핵심]

사용 대상:

- delete confirm
- logout confirm
- payment cancel
- modal close
- destructive action
- unsaved changes

---

### [실무]

예:

```tsx
type ConfirmDialogProps = {
  open: boolean;
  title: string;
  description?: string;
  confirmText?: string;
  cancelText?: string;
  loading?: boolean;
  onConfirm: () => void;
  onCancel: () => void;
};

function ConfirmDialog({
  open,
  title,
  description,
  confirmText = "확인",
  cancelText = "취소",
  loading = false,
  onConfirm,
  onCancel,
}: ConfirmDialogProps) {
  if (!open) {
    return null;
  }

  return (
    <div role="dialog" aria-modal="true">
      <h2>{title}</h2>
      {description && <p>{description}</p>}
      <button type="button" onClick={onCancel} disabled={loading}>
        {cancelText}
      </button>
      <button type="button" onClick={onConfirm} disabled={loading}>
        {loading ? "처리 중..." : confirmText}
      </button>
    </div>
  );
}
```

권장:

- 위험 액션은 confirm UI 제공
- loading 중 confirm / cancel 처리 기준 명확화
- confirmText는 액션을 구체적으로 표현
- destructive action은 danger variant 사용 가능
- ESC / backdrop close 기준 통일

---

### [FAQ]

Q. 삭제 버튼을 누르면 바로 삭제해도 돼?

A.
중요한 데이터 삭제는 Confirm Dialog를 제공하는 것이 안전하다.

Q. ConfirmDialog 안에서 직접 delete API를 호출해도 돼?

A.
공통 Dialog라면 onConfirm만 호출하고 실제 delete API는 부모 Feature Component에서 처리하는 것이 좋다.

---

# 7. Composition Pattern Rules

## 7.1 Children Pattern

### [개념]

Children Pattern은 Component 내부에 들어갈 내용을 props.children으로 받아 유연하게 조합하는 방식이다.

---

### [핵심]

사용 대상:

- Card
- Modal
- Layout
- Section
- Button
- List
- EmptyState action
- ErrorState action

---

### [실무]

예:

```tsx
type CardProps = {
  children: ReactNode;
};

function Card({ children }: CardProps) {
  return <article className="card">{children}</article>;
}
```

사용:

```tsx
<Card>
  <h3>축제 제목</h3>
  <p>서울</p>
</Card>
```

권장:

- 내용이 다양하면 children 사용
- 고정 필드는 명시 props 사용
- children이 필수인지 optional인지 타입으로 표현
- layout 역할 Component에 적합
- children 내부 구조를 과도하게 가정하지 않음

---

### [FAQ]

Q. children은 언제 써?

A.
Component 내부 내용이 다양하거나 외부에서 자유롭게 조합해야 할 때 사용한다.

Q. 모든 것을 children으로 받으면 좋아?

A.
아니다. title, value처럼 의미가 명확한 데이터는 명시 props가 더 좋을 수 있다.

---

## 7.2 Slot-like Pattern Basics

### [개념]

Slot-like Pattern은 Component의 특정 위치에 들어갈 UI를 props로 전달하는 방식이다.

React에서는 header, footer, action 같은 ReactNode props로 구현할 수 있다.

---

### [핵심]

사용 대상:

- modal header / footer
- card action
- empty state action
- page header action
- list item right area
- layout sidebar
- table cell custom render basics

---

### [실무]

예:

```tsx
type EmptyStateProps = {
  title: string;
  description?: string;
  action?: ReactNode;
};

function EmptyState({ title, description, action }: EmptyStateProps) {
  return (
    <section>
      <h2>{title}</h2>
      {description && <p>{description}</p>}
      {action}
    </section>
  );
}
```

사용:

```tsx
<EmptyState
  title="검색 결과가 없습니다."
  description="검색어를 바꾸거나 필터를 초기화해 보세요."
  action={<button type="button">필터 초기화</button>}
/>
```

권장:

- 고정된 위치에 선택적 UI를 넣을 때 사용
- action, header, footer 이름 명확화
- 너무 많은 slot props는 Component 복잡도 증가
- 복잡해지면 Compound Component 검토

---

### [FAQ]

Q. action props는 왜 ReactNode로 받아?

A.
버튼, 링크, 여러 액션 등 다양한 UI를 유연하게 넣기 위해서다.

Q. slot props가 많아지면 어떻게 해?

A.
Component 책임이 커졌을 수 있다. children 구조나 compound pattern을 검토한다.

---

## 7.3 Compound Component Basics

### [개념]

Compound Component는 관련된 여러 하위 Component를 조합해 하나의 UI 패턴을 구성하는 방식이다.

Tabs, Accordion, Select, Modal 같은 UI에서 사용할 수 있다.

---

### [핵심]

사용 대상:

- Tabs
- Accordion
- Modal
- Dropdown
- Select
- Menu
- Stepper

---

### [실무]

간단한 사용 형태:

```tsx
<Tabs defaultValue="info">
  <Tabs.List>
    <Tabs.Trigger value="info">정보</Tabs.Trigger>
    <Tabs.Trigger value="review">리뷰</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="info">축제 정보</Tabs.Content>
  <Tabs.Content value="review">리뷰 목록</Tabs.Content>
</Tabs>
```

권장:

- 하위 요소 관계가 강할 때 사용
- 조합 자유도가 필요한 UI에 적합
- 내부 상태 공유 기준 필요
- 접근성 구현 난도가 높아질 수 있음
- Foundation 문서에서는 개념과 사용 기준만 다룸

---

### [FAQ]

Q. Compound Component는 언제 써?

A.
Tabs나 Accordion처럼 여러 하위 Component가 함께 동작하는 UI에서 유용하다.

Q. 모든 Component를 Compound 방식으로 만들면 좋아?

A.
아니다. 구현 복잡도가 높아질 수 있으므로 조합 자유도가 필요한 UI에만 적용한다.

---

# 8. Base UI Component Rules

## 8.1 Button Component Pattern

### [개념]

Button Component는 사용자 액션을 실행하는 기본 UI Component다.

variant, size, disabled, loading, type, onClick 기준을 명확히 해야 한다.

---

### [핵심]

필수 Props:

- children
- type
- variant
- size
- disabled
- loading
- onClick
- fullWidth
- aria-label

---

### [실무]

예:

```tsx
type ButtonProps = {
  type?: "button" | "submit" | "reset";
  variant?: "primary" | "secondary" | "danger" | "ghost";
  size?: "sm" | "md" | "lg";
  loading?: boolean;
  disabled?: boolean;
  fullWidth?: boolean;
  onClick?: () => void;
  children: ReactNode;
};

function Button({
  type = "button",
  variant = "primary",
  size = "md",
  loading = false,
  disabled = false,
  fullWidth = false,
  onClick,
  children,
}: ButtonProps) {
  return (
    <button
      type={type}
      className={`button button-${variant} button-${size}`}
      disabled={disabled || loading}
      onClick={onClick}
      data-full-width={fullWidth}
    >
      {loading ? "처리 중..." : children}
    </button>
  );
}
```

권장:

- 기본 type은 button
- form submit에서는 type submit 명시
- loading 중 disabled 처리
- danger variant는 삭제 같은 위험 액션에 사용
- 아이콘만 있는 버튼은 aria-label 필요
- onClick은 optional 가능

주의:

- form 안 button 기본 submit 동작 주의
- loading과 disabled가 동시에 있을 때 처리 기준 통일
- Button 내부에 도메인 API 호출 금지
- 색상명 variant 지양

---

### [FAQ]

Q. Button 기본 type은 submit이 좋아?

A.
공통 Button에서는 `button`을 기본값으로 두는 것이 안전하다. Form 제출 버튼은 명시적으로 `type="submit"`을 사용한다.

Q. loading 중 Button은 disabled 해야 해?

A.
권장한다. 중복 클릭을 줄이고 처리 중임을 명확히 보여줄 수 있다.

---

## 8.2 TextField Component Pattern

### [개념]

TextField Component는 label, input, error message, helper text를 함께 관리하는 입력 UI Component다.

---

### [핵심]

필수 Props:

- id
- name
- label
- value
- placeholder
- error
- helperText
- required
- disabled
- onChange
- onBlur
- type
- autoComplete

---

### [실무]

예:

```tsx
type TextFieldProps = {
  id: string;
  name: string;
  label: string;
  value: string;
  type?: string;
  placeholder?: string;
  error?: string;
  helperText?: string;
  required?: boolean;
  disabled?: boolean;
  autoComplete?: string;
  onChange: (event: ChangeEvent<HTMLInputElement>) => void;
  onBlur?: (event: FocusEvent<HTMLInputElement>) => void;
};

function TextField({
  id,
  name,
  label,
  value,
  type = "text",
  placeholder,
  error,
  helperText,
  required = false,
  disabled = false,
  autoComplete,
  onChange,
  onBlur,
}: TextFieldProps) {
  const errorId = `${id}-error`;
  const helperId = `${id}-helper`;

  return (
    <div className="field">
      <label htmlFor={id}>
        {label}
        {required && <span aria-hidden="true">*</span>}
      </label>
      <input
        id={id}
        name={name}
        type={type}
        value={value}
        placeholder={placeholder}
        required={required}
        disabled={disabled}
        autoComplete={autoComplete}
        onChange={onChange}
        onBlur={onBlur}
        aria-invalid={Boolean(error)}
        aria-describedby={error ? errorId : helperText ? helperId : undefined}
      />
      {helperText && !error && <p id={helperId}>{helperText}</p>}
      {error && (
        <p id={errorId} role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
```

권장:

- label 필수
- error와 helperText 우선순위 결정
- aria-invalid / aria-describedby 적용
- id 중복 방지
- value undefined 방지
- password, email 등 type 지원

---

### [FAQ]

Q. placeholder만 쓰고 label은 생략해도 돼?

A.
권장하지 않는다. 접근성과 사용성 측면에서 label을 제공하는 것이 좋다.

Q. TextField에 error props를 넣는 이유는?

A.
입력값 오류를 input과 가까운 위치에 일관되게 표시하고 접근성 속성을 연결하기 위해서다.

---

## 8.3 Modal / Dialog Component Pattern

### [개념]

Modal 또는 Dialog Component는 사용자의 현재 흐름 위에 별도 작업이나 안내를 표시하는 UI Pattern이다.

---

### [핵심]

필수 Props:

- open
- title
- children
- onClose
- footer
- closeOnBackdrop
- closeOnEscape
- aria-labelledby
- aria-modal
- role dialog

---

### [실무]

예:

```tsx
type ModalProps = {
  open: boolean;
  title: string;
  children: ReactNode;
  footer?: ReactNode;
  onClose: () => void;
};

function Modal({ open, title, children, footer, onClose }: ModalProps) {
  if (!open) {
    return null;
  }

  const titleId = "modal-title";

  return (
    <div className="modal-backdrop">
      <section
        role="dialog"
        aria-modal="true"
        aria-labelledby={titleId}
        className="modal"
      >
        <header>
          <h2 id={titleId}>{title}</h2>
          <button type="button" onClick={onClose} aria-label="닫기">
            ×
          </button>
        </header>
        <div>{children}</div>
        {footer && <footer>{footer}</footer>}
      </section>
    </div>
  );
}
```

권장:

- open으로 표시 여부 제어
- onClose 제공
- title과 aria-labelledby 연결
- 닫기 버튼 제공
- focus management 고려
- ESC / backdrop close 기준 통일
- Confirm Dialog와 일반 Modal 구분 가능

주의:

- Modal 내부 API 로직 직접 포함 지양
- focus trap / scroll lock은 별도 구현 또는 라이브러리 검토
- 접근성 구현 난도가 높음
- 중첩 Modal 지양

---

### [FAQ]

Q. Modal은 div만 띄우면 돼?

A.
시각적으로는 가능하지만 접근성을 위해 role dialog, aria-modal, focus 관리, 닫기 동작을 고려해야 한다.

Q. Modal 안에서 API 호출을 직접 처리해도 돼?

A.
Feature Modal은 가능하지만 공통 Modal은 UI 구조만 제공하고 실제 로직은 부모가 처리하는 것이 좋다.

---

## 8.4 Card Component Pattern

### [개념]

Card Component는 관련 정보를 하나의 시각적 단위로 묶어 보여주는 UI Pattern이다.

---

### [핵심]

사용 대상:

- festival card
- review card
- notification card
- profile card
- dashboard card
- summary card

---

### [실무]

공통 Card 예:

```tsx
type CardProps = {
  children: ReactNode;
  interactive?: boolean;
  onClick?: () => void;
};

function Card({ children, interactive = false, onClick }: CardProps) {
  if (interactive) {
    return (
      <button type="button" className="card card-interactive" onClick={onClick}>
        {children}
      </button>
    );
  }

  return <article className="card">{children}</article>;
}
```

Feature Card 예:

```tsx
function FestivalCard({ festival }) {
  return (
    <Card>
      <img src={festival.imageUrl} alt="" />
      <h3>{festival.title}</h3>
      <p>{festival.regionName}</p>
    </Card>
  );
}
```

권장:

- 정보 그룹 단위로 사용
- 클릭 가능한 Card는 키보드 접근성 고려
- article / button / link 중 의미에 맞는 태그 선택
- 이미지 alt 기준 정의
- 공통 Card와 도메인 Card 분리

---

### [FAQ]

Q. 클릭 가능한 Card는 div에 onClick을 붙이면 돼?

A.
권장하지 않는다. 링크 이동이면 anchor 또는 Link, 액션이면 button을 사용하는 것이 접근성에 좋다.

Q. Card Component 안에 도메인 데이터를 직접 넣어야 해?

A.
공통 Card는 children만 받고 도메인 데이터는 FestivalCard 같은 Feature Component에서 처리하는 것이 좋다.

---

## 8.5 Badge Component Pattern

### [개념]

Badge Component는 상태, 카테고리, 권한, 태그 같은 짧은 정보를 시각적으로 표시하는 UI Component다.

---

### [핵심]

사용 대상:

- status
- category
- role
- tag
- count
- notification
- festival theme
- review rating basics

---

### [실무]

예:

```tsx
type BadgeProps = {
  variant?: "default" | "success" | "warning" | "danger" | "info";
  children: ReactNode;
};

function Badge({ variant = "default", children }: BadgeProps) {
  return <span className={`badge badge-${variant}`}>{children}</span>;
}
```

권장:

- 짧은 텍스트 표시
- 의미 기반 variant 사용
- 색상만으로 의미 전달 금지
- count badge는 aria-label 고려
- role badge는 실제 권한 검증과 구분

---

### [FAQ]

Q. Badge는 언제 써?

A.
상태, 카테고리, 태그, 권한처럼 짧은 보조 정보를 표시할 때 사용한다.

Q. Badge 색상만으로 상태를 표현해도 돼?

A.
권장하지 않는다. 텍스트나 아이콘 등 색상 외 정보도 함께 제공하는 것이 좋다.

---

# 9. List / Table Component Rules

## 9.1 List Component Pattern

### [개념]

List Component는 여러 데이터를 반복 렌더링하는 UI Pattern이다.

key, empty state, item component, loading 상태를 함께 고려해야 한다.

---

### [핵심]

필수 포함:

- items
- key
- item component
- empty state
- loading state
- list semantics
- map
- unique id

---

### [실무]

예:

```tsx
function FestivalList({ festivals }) {
  if (festivals.length === 0) {
    return <EmptyState title="축제 정보가 없습니다." />;
  }

  return (
    <ul>
      {festivals.map((festival) => (
        <li key={festival.festivalId}>
          <FestivalCard festival={festival} />
        </li>
      ))}
    </ul>
  );
}
```

권장:

- 안정적인 key 사용
- index key 지양
- Empty State 포함
- List와 Item Component 분리
- ul / ol / li 의미 고려
- 무한 스크롤이면 append 기준 명확화

---

### [FAQ]

Q. List key로 index를 써도 돼?

A.
정렬, 추가, 삭제가 있는 목록에서는 index key를 지양하고 고유 id를 사용하는 것이 좋다.

Q. 목록이 비어 있으면 그냥 아무것도 안 보여줘도 돼?

A.
권장하지 않는다. Empty State를 보여주는 것이 사용자 경험에 좋다.

---

## 9.2 Table Component Pattern

### [개념]

Table Component는 행과 열 구조의 데이터를 표현하는 UI Pattern이다.

데이터 비교, 관리자 목록, 통계 화면에 적합하다.

---

### [핵심]

필수 포함:

- table
- thead
- tbody
- th
- td
- caption
- row key
- empty row
- sorting basics
- pagination relation

---

### [실무]

예:

```tsx
function UserTable({ users }) {
  if (users.length === 0) {
    return <EmptyState title="사용자 목록이 없습니다." />;
  }

  return (
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
  );
}
```

권장:

- 실제 표 데이터에 table 사용
- caption 제공 고려
- th scope 지정
- 행 key는 고유 id 사용
- mobile responsive 기준 필요
- 정렬 / 페이지네이션은 별도 책임으로 분리 가능

---

### [FAQ]

Q. Table 대신 div로 만들어도 돼?

A.
표 형태의 데이터라면 table 요소를 사용하는 것이 의미와 접근성에 좋다.

Q. Table에 caption이 꼭 필요해?

A.
권장한다. 특히 복잡한 표에서는 표의 목적을 설명하는 데 도움이 된다.

---

# 10. Navigation UI Rules

## 10.1 Tab Component Pattern

### [개념]

Tab Component는 같은 영역 안에서 여러 패널을 전환하는 UI Pattern이다.

상태 관리와 접근성을 함께 고려해야 한다.

---

### [핵심]

필수 포함:

- selected tab
- tab list
- tab trigger
- tab panel
- value
- onChange
- keyboard navigation basics
- aria-selected
- role tablist
- role tab
- role tabpanel

---

### [실무]

간단한 예:

```tsx
type TabValue = "info" | "review";

function FestivalTabs() {
  const [selectedTab, setSelectedTab] = useState<TabValue>("info");

  return (
    <section>
      <div role="tablist">
        <button
          type="button"
          role="tab"
          aria-selected={selectedTab === "info"}
          onClick={() => setSelectedTab("info")}
        >
          정보
        </button>
        <button
          type="button"
          role="tab"
          aria-selected={selectedTab === "review"}
          onClick={() => setSelectedTab("review")}
        >
          리뷰
        </button>
      </div>

      {selectedTab === "info" && <div role="tabpanel">축제 정보</div>}

      {selectedTab === "review" && <div role="tabpanel">리뷰 목록</div>}
    </section>
  );
}
```

권장:

- selected state 명확화
- URL 공유가 필요한 tab은 URL State 검토
- 접근성 role 고려
- 탭이 route 수준이면 React Router 사용 검토
- keyboard navigation 심화는 Accessibility 문서에서 다룸

---

### [FAQ]

Q. Tab 상태는 Local State로 둬도 돼?

A.
해당 화면 내부에서만 필요하면 Local State로 충분하다. 공유나 새로고침 유지가 필요하면 URL State를 검토한다.

Q. Tab과 Route는 어떻게 구분해?

A.
페이지 수준 이동이면 Route, 같은 페이지 내부 패널 전환이면 Tab이 적합하다.

---

## 10.2 Dropdown Component Pattern

### [개념]

Dropdown Component는 버튼이나 입력을 기준으로 메뉴 또는 선택지를 펼쳐 보여주는 UI Pattern이다.

---

### [핵심]

필수 포함:

- open state
- trigger
- menu
- item
- onSelect
- onClose
- keyboard navigation basics
- outside click basics
- aria-expanded
- aria-haspopup

---

### [실무]

간단한 예:

```tsx
function Dropdown({ label, items, onSelect }) {
  const [open, setOpen] = useState(false);

  function handleSelect(value) {
    onSelect(value);
    setOpen(false);
  }

  return (
    <div className="dropdown">
      <button
        type="button"
        aria-haspopup="menu"
        aria-expanded={open}
        onClick={() => setOpen((prev) => !prev)}
      >
        {label}
      </button>

      {open && (
        <ul role="menu">
          {items.map((item) => (
            <li key={item.value}>
              <button
                type="button"
                role="menuitem"
                onClick={() => handleSelect(item.value)}
              >
                {item.label}
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

권장:

- trigger와 menu 관계 명확화
- 선택 후 닫기 기준 통일
- 바깥 클릭 / ESC 닫기 고려
- 접근성 구현 난도 주의
- 복잡한 Dropdown은 Headless UI 라이브러리 검토 가능

---

### [FAQ]

Q. Dropdown은 그냥 div로 열고 닫으면 돼?

A.
시각적으로는 가능하지만 키보드 접근성, aria-expanded, 닫기 동작을 고려해야 한다.

Q. Select와 Dropdown은 같아?

A.
다르다. Form 값 선택에는 select가 적합할 수 있고, 메뉴 액션에는 Dropdown Menu가 적합하다.

---

# 11. State UI Component Rules

## 11.1 LoadingState Component

### [개념]

LoadingState Component는 데이터를 불러오거나 작업을 처리하는 중임을 사용자에게 알려주는 공통 UI Component다.

---

### [핵심]

Props 후보:

- message
- size
- fullPage
- ariaLabel
- variant
- children

---

### [실무]

예:

```tsx
type LoadingStateProps = {
  message?: string;
  fullPage?: boolean;
};

function LoadingState({
  message = "불러오는 중입니다.",
  fullPage = false,
}: LoadingStateProps) {
  return (
    <section
      className={fullPage ? "loading loading-full" : "loading"}
      role="status"
      aria-live="polite"
    >
      <span className="spinner" aria-hidden="true" />
      <p>{message}</p>
    </section>
  );
}
```

권장:

- 기본 message 제공
- role status 사용
- full page와 inline loading 구분
- spinner만 단독 사용 지양
- skeleton과 역할 구분

---

### [FAQ]

Q. LoadingState에는 텍스트가 필요해?

A.
접근성과 사용자 이해를 위해 짧은 loading message를 제공하는 것이 좋다.

Q. 모든 로딩에 같은 LoadingState를 써도 돼?

A.
가능하지만 페이지 로딩, 버튼 로딩, 하단 더보기 로딩은 크기와 위치가 다를 수 있다.

---

## 11.2 ErrorState Component

### [개념]

ErrorState Component는 요청 실패나 화면 표시 실패 상황에서 사용자에게 오류 안내와 다음 행동을 제공하는 Component다.

---

### [핵심]

Props 후보:

- title
- message
- action
- onRetry
- retryText
- statusCode
- variant

---

### [실무]

예:

```tsx
type ErrorStateProps = {
  title?: string;
  message: string;
  onRetry?: () => void;
};

function ErrorState({
  title = "문제가 발생했습니다.",
  message,
  onRetry,
}: ErrorStateProps) {
  return (
    <section role="alert" className="error-state">
      <h2>{title}</h2>
      <p>{message}</p>
      {onRetry && (
        <button type="button" onClick={onRetry}>
          다시 시도
        </button>
      )}
    </section>
  );
}
```

권장:

- 사용자 친화 메시지 사용
- Retry 가능 여부에 따라 버튼 제공
- 내부 에러 상세 노출 금지
- statusCode에 따라 문구 변경 가능
- Page Error와 Inline Error 구분

---

### [FAQ]

Q. ErrorState에는 항상 Retry 버튼이 있어야 해?

A.
아니다. 재시도 가능한 오류에만 제공하는 것이 좋다.

Q. 서버 에러 원문을 ErrorState에 그대로 넣어도 돼?

A.
권장하지 않는다. 사용자용 메시지로 변환하는 것이 안전하다.

---

## 11.3 EmptyState Component

### [개념]

EmptyState Component는 요청 성공 후 표시할 데이터가 없거나 사용자가 아직 데이터를 만들지 않은 상태를 안내하는 Component다.

---

### [핵심]

Props 후보:

- title
- description
- action
- icon
- variant
- align

---

### [실무]

예:

```tsx
type EmptyStateProps = {
  title: string;
  description?: string;
  action?: ReactNode;
};

function EmptyState({ title, description, action }: EmptyStateProps) {
  return (
    <section className="empty-state">
      <h2>{title}</h2>
      {description && <p>{description}</p>}
      {action}
    </section>
  );
}
```

권장:

- 데이터 없음의 의미 설명
- 다음 행동 제공
- 검색 결과 없음과 첫 사용 상태 구분
- action props로 버튼 / 링크 전달
- 부정적인 문구 지양

---

### [FAQ]

Q. EmptyState에는 뭘 넣어야 해?

A.
데이터가 없다는 안내, 이유, 사용자가 할 수 있는 다음 행동을 넣는 것이 좋다.

Q. EmptyState와 ErrorState는 뭐가 달라?

A.
EmptyState는 요청 성공 후 데이터가 없는 상태이고 ErrorState는 요청 실패 상태다.

---

# 12. Form UI Component Rules

## 12.1 Form Field Pattern

### [개념]

Form Field Pattern은 label, input, helper text, error message를 하나의 구조로 묶는 UI 패턴이다.

---

### [핵심]

구성 요소:

- label
- control
- helperText
- error
- required mark
- id
- aria-invalid
- aria-describedby

---

### [실무]

기본 구조:

```tsx
function FormField({ label, htmlFor, error, helperText, children }) {
  const description = error || helperText;

  return (
    <div className="form-field">
      <label htmlFor={htmlFor}>{label}</label>
      {children}
      {description && <p role={error ? "alert" : undefined}>{description}</p>}
    </div>
  );
}
```

권장:

- Field 구조 반복 제거
- label과 input 연결
- error 우선순위 명확화
- aria 속성은 input Component와 함께 설계
- React Hook Form과 연결할 경우 register 전달 방식 검토

---

### [FAQ]

Q. FormField와 TextField는 뭐가 달라?

A.
TextField는 input까지 포함한 Component이고 FormField는 label, 설명, 에러 영역을 감싸는 구조 Component로 사용할 수 있다.

Q. helper text와 error가 동시에 있으면?

A.
보통 error를 우선 표시하고 helper text는 숨기거나 보조로 유지한다.

---

## 12.2 SearchBox Pattern

### [개념]

SearchBox는 검색어 입력과 검색 실행을 위한 UI Component다.

검색 Form, 필터 영역, Header 검색에서 사용할 수 있다.

---

### [핵심]

Props 후보:

- value
- placeholder
- loading
- disabled
- onChange
- onSearch
- onReset
- submitOnEnter

---

### [실무]

예:

```tsx
type SearchBoxProps = {
  value: string;
  placeholder?: string;
  loading?: boolean;
  onChange: (value: string) => void;
  onSearch: () => void;
  onReset?: () => void;
};

function SearchBox({
  value,
  placeholder = "검색어를 입력하세요.",
  loading = false,
  onChange,
  onSearch,
  onReset,
}: SearchBoxProps) {
  function handleSubmit(event) {
    event.preventDefault();
    onSearch();
  }

  return (
    <form role="search" onSubmit={handleSubmit}>
      <input
        value={value}
        placeholder={placeholder}
        onChange={(event) => onChange(event.target.value)}
      />
      {onReset && (
        <button type="button" onClick={onReset}>
          초기화
        </button>
      )}
      <button type="submit" disabled={loading}>
        {loading ? "검색 중..." : "검색"}
      </button>
    </form>
  );
}
```

권장:

- role search 사용 가능
- Enter 제출 지원
- 검색 중 disabled 기준
- reset 버튼 제공 가능
- API 호출은 부모에서 처리
- 검색 조건 URL 반영은 부모 책임

---

### [FAQ]

Q. SearchBox 안에서 API 호출까지 해도 돼?

A.
공통 SearchBox라면 검색 이벤트만 부모로 전달하고 API 호출은 부모나 hook에서 처리하는 것이 좋다.

Q. 검색 Form에는 form 태그를 쓰는 게 좋아?

A.
좋다. Enter key 제출과 접근성 측면에서 유리하다.

---

# 13. Styling Boundary Rules

## 13.1 className and Style Props

### [개념]

Styling Boundary는 UI Component가 자체 스타일을 어디까지 책임지고 외부 스타일 확장을 어떻게 허용할지 정하는 기준이다.

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

---

### [실무]

예:

```tsx
type CardProps = {
  className?: string;
  children: ReactNode;
};

function Card({ className = "", children }: CardProps) {
  return <article className={`card ${className}`}>{children}</article>;
}
```

권장:

- 공통 Component는 기본 스타일 제공
- 외부 확장이 필요하면 className 허용
- style prop 남용 지양
- variant / size로 주요 스타일 제어
- layout 전용 스타일은 부모 Layout Component가 담당
- className merge 기준 통일

주의:

- 공통 Component 내부 CSS가 너무 강하면 재사용 어려움
- 모든 스타일을 props로 열어두면 API가 복잡해짐
- inline style은 동적 값이 필요한 경우 제한적으로 사용

---

### [FAQ]

Q. 공통 Component에 className을 열어줘야 해?

A.
프로젝트 기준에 따라 다르지만 외부 확장이 필요한 경우 className을 허용하면 유연하다.

Q. style prop을 많이 쓰면 안 돼?

A.
동적 스타일에는 사용할 수 있지만 일관성 있는 UI를 위해 variant, size, className 기준을 우선하는 것이 좋다.

---

## 13.2 Layout Responsibility

### [개념]

Layout Responsibility는 Component 자체 스타일과 부모 Layout이 담당할 배치 스타일을 구분하는 기준이다.

---

### [핵심]

Component 책임:

- 자체 padding
- 자체 border
- 자체 variant
- 자체 disabled style
- 자체 error style

부모 Layout 책임:

- grid placement
- flex gap
- page width
- section spacing
- responsive layout
- alignment between components

---

### [실무]

예:

```tsx
function ButtonGroup({ children }) {
  return <div className="button-group">{children}</div>;
}
```

권장:

- Button은 버튼 자체 스타일 담당
- ButtonGroup은 버튼 간 배치 담당
- Card는 카드 자체 스타일 담당
- Grid는 카드 배치 담당
- Component가 부모 여백까지 과도하게 책임지지 않음

---

### [FAQ]

Q. Button 안에 margin을 넣어도 돼?

A.
공통 Button에는 margin을 넣지 않는 것이 좋다. 버튼 간 간격은 부모 Layout이나 ButtonGroup이 담당하는 편이 유연하다.

Q. Card가 grid 배치까지 담당해야 해?

A.
보통 Card는 자체 모양만 담당하고 grid 배치는 부모 List나 Layout Component가 담당한다.

---

# 14. Accessibility Rules

## 14.1 UI Component Accessibility

### [개념]

UI Component Accessibility는 공통 Component가 기본적으로 접근 가능한 HTML 구조와 ARIA 속성을 제공하도록 하는 기준이다.

---

### [핵심]

필수 고려:

- semantic element
- button
- anchor
- label
- alt
- aria-label
- aria-labelledby
- aria-describedby
- aria-expanded
- aria-selected
- aria-invalid
- role
- keyboard navigation
- focus visible

---

### [실무]

기준:

```text
클릭 액션 → button
페이지 이동 → Link / anchor
입력 설명 → label
오류 연결 → aria-describedby
열림 상태 → aria-expanded
선택 상태 → aria-selected
아이콘 버튼 → aria-label
```

권장:

- div onClick 남용 금지
- 키보드 접근 가능해야 함
- 색상만으로 상태 표시 금지
- focus outline 제거 금지
- alt 기준 명확화
- Modal / Dropdown / Tabs는 접근성 난도가 높으므로 주의

---

### [FAQ]

Q. div에 onClick을 붙이면 안 돼?

A.
가능은 하지만 키보드 접근성과 의미가 부족하다. 클릭 액션은 button, 이동은 Link나 anchor를 사용하는 것이 좋다.

Q. 아이콘 버튼에는 텍스트가 없어도 돼?

A.
시각적 텍스트가 없다면 aria-label로 버튼의 목적을 제공해야 한다.

---

# 15. File Structure Rules

## 15.1 UI Component File Structure

### [개념]

UI Component File Structure는 공통 UI, Feature UI, Page Component를 구분해 파일을 배치하는 기준이다.

---

### [핵심]

구분:

- components/ui
- components/common
- components/layout
- components/states
- features
- pages
- hooks
- styles

---

### [실무]

예:

```text
src
├ components
│  ├ ui
│  │  ├ Button.tsx
│  │  ├ TextField.tsx
│  │  ├ Modal.tsx
│  │  └ Badge.tsx
│  ├ states
│  │  ├ LoadingState.tsx
│  │  ├ ErrorState.tsx
│  │  └ EmptyState.tsx
│  └ layout
│     ├ Header.tsx
│     └ PageLayout.tsx
├ features
│  ├ festival
│  │  ├ components
│  │  │  ├ FestivalCard.tsx
│  │  │  └ FestivalSearchFilter.tsx
│  │  └ hooks
│  └ review
│     └ components
└ pages
```

권장:

- 공통 UI는 도메인 의존 제거
- Feature Component는 features 내부 배치
- Page Component는 routing 단위
- Layout Component는 공통 layout 폴더
- 상태 UI는 states 또는 feedback 폴더로 분리 가능
- index export는 프로젝트 기준에 따라 선택

---

### [FAQ]

Q. FestivalCard는 components/ui에 넣어?

A.
보통 아니다. festival 도메인 데이터에 의존하므로 features/festival/components에 두는 것이 적합하다.

Q. Button, Modal은 어디에 둬?

A.
여러 도메인에서 사용하는 공통 UI이므로 components/ui 또는 components/common에 둔다.

---

# 16. Troubleshooting Rules

## 16.1 Props Explosion Troubleshooting

### [개념]

Props Explosion은 Component가 너무 많은 props를 받아 사용법이 복잡해지는 문제다.

---

### [핵심]

원인:

- 하나의 Component가 너무 많은 역할 담당
- 모든 예외를 props로 처리
- boolean props 과다
- 도메인 요구사항을 공통 UI에 직접 추가
- composition 대신 props만 확장

해결:

- Component 책임 재정의
- variant로 통합
- composition 사용
- Feature Component로 분리
- slot-like props 사용
- Component 분리

---

### [실무]

Debug Flow:

```text
Props 개수 확인
→ 서로 관련 없는 props 확인
→ boolean 충돌 확인
→ 도메인 props 확인
→ composition 가능 여부 확인
→ Component 분리
```

예:

```text
문제: Button에 isReviewDelete, isAdminOnly, festivalId props 추가
해결: Button은 공통 UI로 유지하고 ReviewDeleteButton Feature Component 생성
```

---

### [FAQ]

Q. Props가 너무 많으면 어떻게 해?

A.
Component 책임을 다시 확인하고 composition, variant, Feature Component 분리를 검토한다.

Q. 도메인 전용 props를 공통 Component에 넣어도 돼?

A.
권장하지 않는다. 도메인 전용 로직은 Feature Component에 두는 것이 좋다.

---

## 16.2 Over Abstraction Troubleshooting

### [개념]

Over Abstraction은 실제 필요보다 너무 범용적인 Component를 만들어 오히려 사용과 수정이 어려워지는 문제다.

---

### [핵심]

증상:

- Component 이름은 공통인데 사용법이 어려움
- props 조합을 이해하기 어려움
- 예외 처리가 많음
- 특정 화면 수정이 공통 Component 전체에 영향
- 재사용보다 조건문이 많음
- Component 내부가 도메인 분기로 가득함

해결:

- 실제 재사용 사례 확인
- 도메인 Component로 되돌리기
- 작은 UI 단위로 분리
- children / composition 활용
- 공통화 범위 축소
- 문서화 가능한 API만 유지

---

### [실무]

판단 기준:

```text
공통 Component 수정 시 여러 화면이 깨짐
→ 추상화 범위 과도 가능
→ 역할별 Component 분리 검토
```

주의:

- DRY보다 명확성이 우선일 수 있음
- 반복이 조금 있다고 무조건 추상화하지 않음
- 공통화는 유지보수 비용을 줄여야 의미가 있음

---

### [FAQ]

Q. 중복 코드를 없애려고 공통 Component를 만들었는데 더 복잡해졌어?

A.
Over Abstraction일 수 있다. 반복 제거보다 역할 명확성과 사용 편의성이 중요하다.

Q. 공통화는 언제 하는 게 좋아?

A.
반복이 실제로 발생하고 역할과 props가 안정적일 때 하는 것이 좋다.

---

## 16.3 Accessibility Missing Troubleshooting

### [개념]

Accessibility Missing은 UI Component가 시각적으로는 동작하지만 키보드나 보조기술 사용자가 사용하기 어려운 문제다.

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
- error aria-describedby 누락

해결:

- semantic element 사용
- label 연결
- aria 속성 추가
- keyboard navigation 확인
- focus visible 유지
- 색상 외 텍스트 제공
- 접근성 체크리스트 적용

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

---

### [FAQ]

Q. 마우스로 잘 되면 접근성 문제는 없는 거야?

A.
아니다. 키보드와 스크린 리더 사용자가 사용할 수 있는지도 확인해야 한다.

Q. focus outline을 없애도 돼?

A.
권장하지 않는다. 대신 디자인에 맞는 focus visible 스타일을 제공하는 것이 좋다.

---

## 16.4 Styling Conflict Troubleshooting

### [개념]

Styling Conflict는 공통 UI Component의 스타일이 특정 화면 요구와 충돌하거나 외부 스타일이 내부 스타일을 깨는 문제다.

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

해결:

- Component 자체 스타일과 Layout 스타일 분리
- className 확장 기준 통일
- variant / size 기준 정리
- 전역 selector 축소
- CSS Module / scoped style 검토
- margin은 부모가 담당

---

### [실무]

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

A.
Button 자체에 margin을 넣으면 부모 layout과 충돌할 수 있다. 간격은 ButtonGroup이나 부모 layout에서 관리하는 것이 좋다.

Q. className으로 외부 스타일을 덮어도 돼?

A.
가능하지만 기준이 없으면 스타일 충돌이 생긴다. 공통 Component의 확장 규칙을 정하는 것이 좋다.

---

# 17. Comparison Rules

## 17.1 Required Comparisons

### [개념]

UI Component Pattern 문서는 헷갈리는 Component 설계 개념을 비교해서 작성한다.

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

예시:

| 비교        | Common UI     | Feature UI                 |
| ----------- | ------------- | -------------------------- |
| 목적        | 범용 UI 제공  | 특정 도메인 화면 구현      |
| 도메인 의존 | 낮음          | 높음                       |
| 예          | Button, Modal | FestivalCard, ReviewForm   |
| API 호출    | 없음          | 가능                       |
| 위치        | components/ui | features/domain/components |

---

### [FAQ]

Q. 비교 표는 왜 필요해?

A.
사용자가 자주 헷갈리는 UI Component 설계 질문에서 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. UI Component 비교 문서에서 가장 중요한 것은?

A.
공통화 기준, 책임 분리, Props 설계, 접근성, 과도한 추상화 방지를 함께 설명하는 것이다.

---

# 18. Checklist Rules

## 18.1 UI Component Pattern Checklist

### [개념]

UI Component Pattern 문서 검수 시 Component 설계 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] Component 책임이 명확한가?
- [ ] Common UI와 Feature UI가 구분되었는가?
- [ ] 도메인 로직이 공통 UI에 들어가지 않았는가?
- [ ] Props 이름이 명확한가?
- [ ] variant / size 기준이 포함되었는가?
- [ ] boolean props 과다 사용을 경고하는가?
- [ ] children / composition 기준이 포함되었는가?
- [ ] Event Handler props 기준이 포함되었는가?
- [ ] Button / Input / Modal / Card / List 패턴이 포함되었는가?
- [ ] LoadingState / ErrorState / EmptyState 기준이 포함되었는가?
- [ ] 접근성 기준이 포함되었는가?
- [ ] Styling Boundary 기준이 포함되었는가?
- [ ] File Structure 기준이 포함되었는가?
- [ ] Troubleshooting이 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 기준:

```text
Draft
→ Responsibility Check
→ Reusability Check
→ Props API Check
→ Accessibility Check
→ Styling Boundary Check
→ Anti Pattern Check
→ Troubleshooting Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. UI Component 문서 검수에서 가장 중요한 것은?

A.
Component 책임, 재사용 기준, Props 설계, 접근성, 스타일 책임 분리, 과도한 추상화 방지 포함 여부다.

---

# 19. Retrieval Optimization Rules

## 19.1 Keyword Rules

### [개념]

UI Component Pattern 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

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
- Accessibility
- Styling Boundary
- className
- Component Responsibility
- Over Abstraction
- Props Explosion

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- 공통 Component는 언제 만들어?
- UI Component props는 어떻게 설계해?
- variant는 어떻게 설계해?
- boolean props가 많으면 왜 안 좋아?
- Button 기본 type은 뭐가 좋아?
- Modal은 어떻게 만들어?
- Card는 공통 Component야?
- FestivalCard는 어디에 둬?
- EmptyState는 어떻게 만들어?
- div onClick을 써도 돼?
- className을 열어줘야 해?
- Component에 margin을 넣어도 돼?
- Props가 너무 많으면 어떻게 해?
- 공통화했는데 더 복잡해졌어

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. FAQ 질문은 어떤 스타일이 좋아?

A.
실제 사용자가 검색하거나 질문할 법한 문장형 질문이 좋다.

---

# 20. Version Rules

## 20.1 Modern UI Component 기준

### [개념]

UI Component Pattern 문서는 Modern React UI Component 기준으로 작성한다.

---

### [핵심]

기준:

- React 18+
- React 19 호환 고려
- Functional Component
- TypeScript Ready Props
- Composition 기반 설계
- Semantic HTML 우선
- Accessibility 기본 포함
- Controlled / Uncontrolled 구분
- Common UI / Feature UI 분리
- Design System 확장 가능 구조
- Props API 명확화

Legacy 제외:

- jQuery UI 중심 설명
- div onClick 남용
- Inline Style 남발
- 모든 UI를 하나의 만능 Component로 통합
- 도메인 API 호출을 공통 UI에 포함
- 색상명 중심 variant
- label 없는 input
- 접근성 없는 Modal / Dropdown / Tab
- class component 중심 UI 설계

---

### [실무]

실무 기준:

```text
Modern UI Component
→ Define Responsibility
→ Design Props
→ Add Accessibility
→ Separate Styling Boundary
→ Compose Feature UI
→ Review Anti Pattern
```

---

### [FAQ]

Q. jQuery UI 방식도 다뤄?

A.
신규 React 문서에서는 Functional Component, Props, Composition, 접근성 기준을 우선한다.

Q. TypeScript가 아니어도 이 기준을 적용할 수 있어?

A.
가능하다. 다만 TypeScript를 사용하면 Props 설계를 더 명확히 표현할 수 있다.

---

# 21. Common Mistakes

## 21.1 UI Component Common Mistakes

### [개념]

UI Component Pattern 문서는 자주 발생하는 Component 설계 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

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

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: Button Component가 reviewId를 받아 deleteReview API를 호출함
원인: 공통 UI Component와 Feature Component 책임 혼동
해결: Button은 UI만 담당하고 ReviewDeleteButton에서 API 호출 처리
```

---

### [FAQ]

Q. UI Component 초보가 가장 많이 하는 실수는?

A.
공통 UI와 Feature UI를 구분하지 못하거나, Props를 계속 추가해 만능 Component를 만드는 실수가 많다.

Q. UI Component 문제는 어떻게 찾는 게 좋아?

A.
Component 책임, Props 개수, 도메인 의존성, 접근성, 스타일 책임, 재사용 범위를 순서대로 확인한다.

---

# 22. Final Goal

## 22.1 Domain Final Goal

### [개념]

UI Component Pattern RAG 문서는 Frontend Agent가 일관되고 재사용 가능하며 접근성 있는 UI Component를 설계하고 검토하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- UI Component 책임 정의
- Common UI / Feature UI 구분
- Reusable Component 판단
- Props Design 수행
- Variant / Size / Boolean Props 설계
- Event Handler Props 설계
- Children / Composition 적용
- Slot-like Pattern 적용
- Compound Component 기초 판단
- Button / TextField / Modal / Card / Badge 설계
- List / Table / Tab / Dropdown 설계
- LoadingState / ErrorState / EmptyState 설계
- Form Field / SearchBox 설계
- Accessibility 기준 적용
- Styling Boundary 설정
- File Structure 정리
- Props Explosion 감지
- Over Abstraction 감지
- Common Mistakes 검토

---

### [실무]

Agent 수행 가능 작업:

```text
User UI Component Request
→ Identify Component Role
→ Decide Common UI or Feature UI
→ Design Props API
→ Add Variant / Size / State
→ Add Event Handlers
→ Add Accessibility
→ Separate Styling Boundary
→ Check Anti Patterns
→ UI Component Pattern Output
```

---

### [FAQ]

Q. UI Component Pattern 문서의 최종 목적은 뭐야?

A.
Frontend Agent가 공통 UI와 도메인 UI를 구분하고, Props와 접근성을 갖춘 유지보수 가능한 UI Component를 설계하게 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
Frontend Accessibility, Frontend Testing, Styling Architecture, Design System 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. UI Component Pattern 문서는 왜 필요해?
A. Frontend Agent가 Button, Modal, Card 같은 UI Component를 일관되게 설계하고 재사용 기준을 판단해야 하기 때문이다.

Q. React UI Component는 어떻게 설계해?
A. Component 책임을 먼저 정하고 Props, variant, event handler, 접근성, 스타일 경계를 설계한다.

Q. 공통 Component는 언제 만들어?
A. 여러 화면에서 반복되고 역할이 안정적이며 도메인 의존이 적을 때 만든다.

Q. 모든 UI를 공통 Component로 만들어야 해?
A. 아니다. 반복되고 의미가 안정적인 UI만 공통화하고 한 화면 전용 UI는 Feature Component로 두는 것이 좋다.

Q. Common UI와 Feature UI 차이는?
A. Common UI는 도메인 의존이 낮은 범용 UI이고 Feature UI는 특정 도메인 데이터와 기능에 맞춰진 Component다.

Q. FestivalCard는 공통 Component야?
A. 보통 Feature UI다. festival 데이터 구조에 의존하기 때문이다.

Q. Card Component와 FestivalCard는 뭐가 달라?
A. Card는 범용 컨테이너이고 FestivalCard는 축제 정보를 보여주는 도메인 Component다.

Q. 공통 Button Component 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. 공통 Button은 UI 역할만 담당하고 API 호출은 Feature Component나 Hook에서 처리하는 것이 좋다.

Q. UI Component의 책임은 어디까지야?
A. 화면 표시, 사용자 이벤트 전달, 접근성, 시각 상태 표현까지가 기본 책임이다.

Q. Component는 처음부터 재사용 가능하게 만들어야 해?
A. 항상 그럴 필요는 없다. 실제 반복과 역할 안정성이 확인된 후 공통화하는 것이 더 안전하다.

Q. 공통 Component props가 너무 많아지면?
A. 역할이 너무 커졌을 가능성이 있다. Component 분리나 composition을 검토한다.

Q. UI Component props는 어떻게 설계해?
A. 의미가 명확한 이름을 사용하고 variant, size, disabled, loading, onClick, children 같은 기준을 일관되게 둔다.

Q. boolean props 이름은 어떻게 지어?
A. 상태를 나타내면 is / has를 사용하고, HTML 속성과 유사한 경우 disabled, required, loading처럼 명확히 쓴다.

Q. Button variant는 blue, red로 만들면 안 돼?
A. 가능은 하지만 primary, secondary, danger처럼 의미 기반 이름이 디자인 변경에 더 유연하다.

Q. variant는 왜 union type으로 제한해?
A. 허용되는 스타일 종류를 명확히 하고 잘못된 문자열 사용을 방지하기 위해서다.

Q. variant가 너무 많아지면 어떻게 해?
A. Component 책임이 너무 넓어진 것일 수 있으므로 별도 Component나 composition을 검토한다.

Q. Button size는 px 값으로 받는 게 좋아?
A. 공통 Component에서는 sm, md, lg처럼 제한된 크기 값을 사용하는 것이 일관성에 좋다.

Q. full width 버튼은 size야 variant야?
A. 보통 size보다 layout 성격이 강하므로 fullWidth 같은 별도 prop으로 둘 수 있다.

Q. boolean props가 많으면 왜 문제야?
A. 서로 충돌하는 조합이 생기고 Component 사용법이 복잡해지기 때문이다.

Q. primary, danger를 boolean으로 두면 안 돼?
A. 가능은 하지만 동시에 true가 될 수 있어 variant union으로 제한하는 것이 더 안전하다.

Q. onClick 안에서 API 호출을 넣어도 돼?
A. Feature Component에서는 가능하지만 공통 UI Component에서는 부모로 이벤트를 전달하는 것이 좋다.

Q. onChange는 event를 넘기는 게 좋아 value를 넘기는 게 좋아?
A. 공통 input은 event를 넘기거나 value를 넘길 수 있다. 프로젝트 컨벤션을 통일하는 것이 중요하다.

Q. 삭제 버튼을 누르면 바로 삭제해도 돼?
A. 중요한 데이터 삭제는 Confirm Dialog를 제공하는 것이 안전하다.

Q. ConfirmDialog 안에서 직접 delete API를 호출해도 돼?
A. 공통 Dialog라면 onConfirm만 호출하고 실제 delete API는 부모 Feature Component에서 처리하는 것이 좋다.

Q. children은 언제 써?
A. Component 내부 내용이 다양하거나 외부에서 자유롭게 조합해야 할 때 사용한다.

Q. 모든 것을 children으로 받으면 좋아?
A. 아니다. title, value처럼 의미가 명확한 데이터는 명시 props가 더 좋을 수 있다.

Q. action props는 왜 ReactNode로 받아?
A. 버튼, 링크, 여러 액션 등 다양한 UI를 유연하게 넣기 위해서다.

Q. slot props가 많아지면 어떻게 해?
A. Component 책임이 커졌을 수 있다. children 구조나 compound pattern을 검토한다.

Q. Compound Component는 언제 써?
A. Tabs나 Accordion처럼 여러 하위 Component가 함께 동작하는 UI에서 유용하다.

Q. 모든 Component를 Compound 방식으로 만들면 좋아?
A. 아니다. 구현 복잡도가 높아질 수 있으므로 조합 자유도가 필요한 UI에만 적용한다.

Q. Button 기본 type은 submit이 좋아?
A. 공통 Button에서는 button을 기본값으로 두는 것이 안전하다. Form 제출 버튼은 명시적으로 type submit을 사용한다.

Q. loading 중 Button은 disabled 해야 해?
A. 권장한다. 중복 클릭을 줄이고 처리 중임을 명확히 보여줄 수 있다.

Q. placeholder만 쓰고 label은 생략해도 돼?
A. 권장하지 않는다. 접근성과 사용성 측면에서 label을 제공하는 것이 좋다.

Q. TextField에 error props를 넣는 이유는?
A. 입력값 오류를 input과 가까운 위치에 일관되게 표시하고 접근성 속성을 연결하기 위해서다.

Q. Modal은 div만 띄우면 돼?
A. 시각적으로는 가능하지만 접근성을 위해 role dialog, aria-modal, focus 관리, 닫기 동작을 고려해야 한다.

Q. Modal 안에서 API 호출을 직접 처리해도 돼?
A. Feature Modal은 가능하지만 공통 Modal은 UI 구조만 제공하고 실제 로직은 부모가 처리하는 것이 좋다.

Q. 클릭 가능한 Card는 div에 onClick을 붙이면 돼?
A. 권장하지 않는다. 링크 이동이면 anchor 또는 Link, 액션이면 button을 사용하는 것이 접근성에 좋다.

Q. Card Component 안에 도메인 데이터를 직접 넣어야 해?
A. 공통 Card는 children만 받고 도메인 데이터는 FestivalCard 같은 Feature Component에서 처리하는 것이 좋다.

Q. Badge는 언제 써?
A. 상태, 카테고리, 태그, 권한처럼 짧은 보조 정보를 표시할 때 사용한다.

Q. Badge 색상만으로 상태를 표현해도 돼?
A. 권장하지 않는다. 텍스트나 아이콘 등 색상 외 정보도 함께 제공하는 것이 좋다.

Q. List key로 index를 써도 돼?
A. 정렬, 추가, 삭제가 있는 목록에서는 index key를 지양하고 고유 id를 사용하는 것이 좋다.

Q. 목록이 비어 있으면 그냥 아무것도 안 보여줘도 돼?
A. 권장하지 않는다. Empty State를 보여주는 것이 사용자 경험에 좋다.

Q. Table 대신 div로 만들어도 돼?
A. 표 형태의 데이터라면 table 요소를 사용하는 것이 의미와 접근성에 좋다.

Q. Table에 caption이 꼭 필요해?
A. 권장한다. 특히 복잡한 표에서는 표의 목적을 설명하는 데 도움이 된다.

Q. Tab 상태는 Local State로 둬도 돼?
A. 해당 화면 내부에서만 필요하면 Local State로 충분하다. 공유나 새로고침 유지가 필요하면 URL State를 검토한다.

Q. Tab과 Route는 어떻게 구분해?
A. 페이지 수준 이동이면 Route, 같은 페이지 내부 패널 전환이면 Tab이 적합하다.

Q. Dropdown은 그냥 div로 열고 닫으면 돼?
A. 시각적으로는 가능하지만 키보드 접근성, aria-expanded, 닫기 동작을 고려해야 한다.

Q. Select와 Dropdown은 같아?
A. 다르다. Form 값 선택에는 select가 적합할 수 있고, 메뉴 액션에는 Dropdown Menu가 적합하다.

Q. LoadingState에는 텍스트가 필요해?
A. 접근성과 사용자 이해를 위해 짧은 loading message를 제공하는 것이 좋다.

Q. ErrorState에는 항상 Retry 버튼이 있어야 해?
A. 아니다. 재시도 가능한 오류에만 제공하는 것이 좋다.

Q. EmptyState에는 뭘 넣어야 해?
A. 데이터가 없다는 안내, 이유, 사용자가 할 수 있는 다음 행동을 넣는 것이 좋다.

Q. EmptyState와 ErrorState는 뭐가 달라?
A. EmptyState는 요청 성공 후 데이터가 없는 상태이고 ErrorState는 요청 실패 상태다.

Q. FormField와 TextField는 뭐가 달라?
A. TextField는 input까지 포함한 Component이고 FormField는 label, 설명, 에러 영역을 감싸는 구조 Component로 사용할 수 있다.

Q. SearchBox 안에서 API 호출까지 해도 돼?
A. 공통 SearchBox라면 검색 이벤트만 부모로 전달하고 API 호출은 부모나 hook에서 처리하는 것이 좋다.

Q. 검색 Form에는 form 태그를 쓰는 게 좋아?
A. 좋다. Enter key 제출과 접근성 측면에서 유리하다.

Q. 공통 Component에 className을 열어줘야 해?
A. 프로젝트 기준에 따라 다르지만 외부 확장이 필요한 경우 className을 허용하면 유연하다.

Q. style prop을 많이 쓰면 안 돼?
A. 동적 스타일에는 사용할 수 있지만 일관성 있는 UI를 위해 variant, size, className 기준을 우선하는 것이 좋다.

Q. Button 안에 margin을 넣어도 돼?
A. 공통 Button에는 margin을 넣지 않는 것이 좋다. 버튼 간 간격은 부모 Layout이나 ButtonGroup이 담당하는 편이 유연하다.

Q. Card가 grid 배치까지 담당해야 해?
A. 보통 Card는 자체 모양만 담당하고 grid 배치는 부모 List나 Layout Component가 담당한다.

Q. div에 onClick을 붙이면 안 돼?
A. 가능은 하지만 키보드 접근성과 의미가 부족하다. 클릭 액션은 button, 이동은 Link나 anchor를 사용하는 것이 좋다.

Q. 아이콘 버튼에는 텍스트가 없어도 돼?
A. 시각적 텍스트가 없다면 aria-label로 버튼의 목적을 제공해야 한다.

Q. FestivalCard는 components/ui에 넣어?
A. 보통 아니다. festival 도메인 데이터에 의존하므로 features/festival/components에 두는 것이 적합하다.

Q. Button, Modal은 어디에 둬?
A. 여러 도메인에서 사용하는 공통 UI이므로 components/ui 또는 components/common에 둔다.

Q. Props가 너무 많으면 어떻게 해?
A. Component 책임을 다시 확인하고 composition, variant, Feature Component 분리를 검토한다.

Q. 도메인 전용 props를 공통 Component에 넣어도 돼?
A. 권장하지 않는다. 도메인 전용 로직은 Feature Component에 두는 것이 좋다.

Q. 중복 코드를 없애려고 공통 Component를 만들었는데 더 복잡해졌어?
A. Over Abstraction일 수 있다. 반복 제거보다 역할 명확성과 사용 편의성이 중요하다.

Q. 공통화는 언제 하는 게 좋아?
A. 반복이 실제로 발생하고 역할과 props가 안정적일 때 하는 것이 좋다.

Q. 마우스로 잘 되면 접근성 문제는 없는 거야?
A. 아니다. 키보드와 스크린 리더 사용자가 사용할 수 있는지도 확인해야 한다.

Q. focus outline을 없애도 돼?
A. 권장하지 않는다. 대신 디자인에 맞는 focus visible 스타일을 제공하는 것이 좋다.

Q. 공통 Button에 margin을 넣었더니 화면마다 간격이 이상해?
A. Button 자체에 margin을 넣으면 부모 layout과 충돌할 수 있다. 간격은 ButtonGroup이나 부모 layout에서 관리하는 것이 좋다.

Q. className으로 외부 스타일을 덮어도 돼?
A. 가능하지만 기준이 없으면 스타일 충돌이 생긴다. 공통 Component의 확장 규칙을 정하는 것이 좋다.

Q. TypeScript가 아니어도 이 기준을 적용할 수 있어?
A. 가능하다. 다만 TypeScript를 사용하면 Props 설계를 더 명확히 표현할 수 있다.

Q. UI Component 초보가 가장 많이 하는 실수는?
A. 공통 UI와 Feature UI를 구분하지 못하거나, Props를 계속 추가해 만능 Component를 만드는 실수가 많다.

Q. UI Component 문제는 어떻게 찾는 게 좋아?
A. Component 책임, Props 개수, 도메인 의존성, 접근성, 스타일 책임, 재사용 범위를 순서대로 확인한다.

Q. UI Component Pattern 다음 문서는 뭐가 좋아?
A. Frontend Accessibility, Frontend Testing, Styling Architecture, Design System 순서가 좋다.
