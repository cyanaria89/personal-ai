# React Component Design Part07 - Accessibility, Troubleshooting, Checklist

---

# 1. Component Accessibility

## 1.1 Component Accessibility Definition

### [개념]

Component Accessibility는 React Component 단위에서 Semantic HTML, ARIA, Keyboard Interaction, Focus Management를 고려해 접근 가능한 UI를 설계하는 기준이다.

Accessibility는 화면 완성 후 마지막에 추가하는 장식이 아니다.

Button, Input, Modal, Dropdown, Form, Image, List 같은 Component를 설계할 때 기본 책임으로 포함해야 한다.

---

### [핵심]

- Component Accessibility는 Component 설계 단계에서 포함한다.
- Semantic HTML을 먼저 사용한다.
- ARIA는 Semantic HTML로 부족한 의미를 보완할 때 사용한다.
- 클릭 가능한 요소는 button 또는 a를 우선 사용한다.
- input에는 label을 연결한다.
- 이미지에는 적절한 alt를 제공한다.
- Modal에는 role, aria-modal, focus 관리가 필요하다.
- Toggle에는 aria-expanded, aria-controls를 검토한다.
- Keyboard 조작이 가능해야 한다.
- Focus 상태가 시각적으로 보여야 한다.
- Accessibility는 Reusable UI Component의 기본 책임이다.

---

### [실무]

2026 실무 기준에서 접근성은 Component Design의 필수 검토 항목이다.

접근성 우선순위:

```text
Semantic HTML
→ Keyboard Interaction
→ Label / Alt
→ ARIA Supplement
→ Focus Management
→ Screen Reader Compatibility
```

좋은 Button 예:

```tsx
type ButtonProps = {
  type?: "button" | "submit" | "reset";
  disabled?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
};

function Button({
  type = "button",
  disabled = false,
  children,
  onClick,
}: ButtonProps) {
  return (
    <button type={type} disabled={disabled} onClick={onClick}>
      {children}
    </button>
  );
}
```

나쁜 Button 예:

```tsx
function FakeButton({ onClick, children }: FakeButtonProps) {
  return <div onClick={onClick}>{children}</div>;
}
```

문제:

```text
- Keyboard 접근성 부족
- 기본 button 동작 없음
- disabled 처리 어려움
- role / tabIndex / keydown 추가 필요
```

---

### [FAQ]

Q. Component Accessibility가 뭐야?
A. Component 단위에서 Semantic HTML, ARIA, Keyboard Interaction, Focus Management를 고려해 접근 가능한 UI를 만드는 기준이다.

Q. div에 onClick을 달아서 버튼처럼 써도 돼?
A. 권장하지 않는다. 동작 버튼은 button 태그를 사용해야 키보드 접근성과 기본 동작을 얻을 수 있다.

Q. ARIA를 많이 붙이면 접근성이 좋아져?
A. 아니다. 먼저 Semantic HTML을 사용하고 부족한 의미를 보완할 때 ARIA를 사용한다.

Q. Accessibility는 언제 검토해야 해?
A. Component 설계 단계부터 검토해야 한다. 특히 Button, Input, Modal, Dropdown, Form에서 중요하다.

---

## 1.2 Semantic HTML Rules

### [개념]

Semantic HTML Rules는 Component가 의미에 맞는 HTML 요소를 사용하도록 하는 기준이다.

Semantic HTML은 접근성, SEO, Keyboard Interaction, Screen Reader 이해를 위한 기본이다.

---

### [핵심]

Semantic HTML 기준:

- 클릭 동작은 button
- 페이지 이동은 a 또는 router link
- 주요 콘텐츠 영역은 main
- 영역 제목이 있는 독립 구역은 section
- 독립 콘텐츠 항목은 article
- 목록은 ul / ol / li
- 입력은 label + input
- 페이지 상단 구조는 header
- 네비게이션은 nav
- 하단 정보는 footer
- 표 데이터는 table

주의:

- div와 span 남용 금지
- button 역할을 div로 대체하지 않음
- link 역할과 button 역할 구분
- heading level 순서 유지
- 의미 없는 wrapper 최소화

---

### [실무]

좋은 예:

```tsx
function FestivalCard({ festival, onSelect }: FestivalCardProps) {
  return (
    <article>
      <h2>{festival.title}</h2>
      <p>{festival.regionName}</p>
      <button type="button" onClick={() => onSelect(festival.festivalId)}>
        상세 보기
      </button>
    </article>
  );
}
```

나쁜 예:

```tsx
function FestivalCard({ festival, onSelect }: FestivalCardProps) {
  return (
    <div>
      <div>{festival.title}</div>
      <div>{festival.regionName}</div>
      <div onClick={() => onSelect(festival.festivalId)}>상세 보기</div>
    </div>
  );
}
```

Button vs Link:

```text
button
→ 현재 화면에서 동작 수행
→ submit, open modal, toggle, delete, save

a / Link
→ 다른 URL 또는 Route로 이동
→ detail page, external link, navigation
```

---

### [FAQ]

Q. Semantic HTML이 왜 중요해?
A. 요소의 의미를 브라우저, 보조기술, 개발자가 명확히 이해할 수 있게 해 접근성과 유지보수성을 높인다.

Q. button과 a는 어떻게 구분해?
A. 현재 화면에서 동작을 수행하면 button, 다른 URL이나 Route로 이동하면 a 또는 Link를 사용한다.

Q. 모든 박스를 div로 만들면 안 돼?
A. 권장하지 않는다. 역할에 맞는 header, main, section, article, nav, footer, button을 우선 사용한다.

Q. FestivalCard는 article이 적합해?
A. 독립적으로 이해 가능한 콘텐츠 항목이면 article이 적합할 수 있다.

---

## 1.3 Form Accessibility Rules

### [개념]

Form Accessibility는 input, textarea, select, checkbox, radio 같은 Form Component가 label, error message, required 상태, keyboard 조작을 올바르게 제공하도록 하는 기준이다.

Form Component는 사용자가 값을 정확히 입력하고 오류를 이해할 수 있게 설계해야 한다.

---

### [핵심]

Form 접근성 기준:

- input에는 label 연결
- id와 htmlFor 연결
- error message 제공
- aria-invalid 사용 검토
- aria-describedby로 도움말과 오류 연결
- required 상태 명확화
- placeholder를 label 대체로 사용하지 않음
- fieldset / legend 사용 검토
- submit button type 명확화
- keyboard 조작 가능

---

### [실무]

좋은 Input 예:

```tsx
type TextFieldProps = {
  id: string;
  label: string;
  value: string;
  errorMessage?: string;
  required?: boolean;
  onValueChange: (value: string) => void;
};

function TextField({
  id,
  label,
  value,
  errorMessage,
  required = false,
  onValueChange,
}: TextFieldProps) {
  const errorId = `${id}-error`;

  return (
    <div>
      <label htmlFor={id}>
        {label}
        {required && <span aria-hidden="true">*</span>}
      </label>
      <input
        id={id}
        value={value}
        required={required}
        aria-invalid={Boolean(errorMessage)}
        aria-describedby={errorMessage ? errorId : undefined}
        onChange={(event) => onValueChange(event.target.value)}
      />
      {errorMessage && <p id={errorId}>{errorMessage}</p>}
    </div>
  );
}
```

나쁜 예:

```tsx
function TextField() {
  return <input placeholder="이메일" />;
}
```

문제:

```text
placeholder는 label 대체가 아니다.
입력 중 placeholder가 사라질 수 있다.
Screen Reader 사용자가 목적을 이해하기 어렵다.
```

---

### [FAQ]

Q. input에는 label이 꼭 필요해?
A. 필요하다. label은 사용자가 입력 필드의 목적을 이해하게 해준다.

Q. placeholder를 label 대신 써도 돼?
A. 권장하지 않는다. placeholder는 보조 설명일 뿐 label을 대체하지 않는다.

Q. aria-invalid는 언제 써?
A. 입력값이 유효하지 않은 상태임을 보조기술에 알릴 때 사용한다.

Q. error message는 input과 어떻게 연결해?
A. error message에 id를 주고 input의 aria-describedby에 연결한다.

---

# 2. Modal, Dropdown, Toggle Accessibility

## 2.1 Modal Accessibility Rules

### [개념]

Modal Accessibility는 Modal Component가 dialog 의미, 제목 연결, 닫기 동작, focus management, keyboard interaction을 제공하도록 하는 기준이다.

Modal은 화면 흐름을 강하게 제어하는 Component이므로 접근성 기준을 반드시 검토해야 한다.

---

### [핵심]

Modal 접근성 기준:

- role="dialog" 사용
- aria-modal="true" 사용
- aria-labelledby로 title 연결
- 닫기 버튼 제공
- Escape key 닫기 검토
- 열릴 때 focus 이동
- 닫힐 때 trigger로 focus 복귀
- Modal 내부 focus trap 검토
- 배경 스크롤 제어 검토
- children만으로 핵심 구조를 외부에 맡기지 않음

---

### [실무]

Modal 기본 예:

```tsx
type ModalProps = {
  id: string;
  title: string;
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
};

function Modal({ id, title, isOpen, onClose, children }: ModalProps) {
  const titleId = `${id}-title`;

  if (!isOpen) {
    return null;
  }

  return (
    <section role="dialog" aria-modal="true" aria-labelledby={titleId}>
      <header>
        <h2 id={titleId}>{title}</h2>
        <button type="button" onClick={onClose}>
          닫기
        </button>
      </header>
      <div>{children}</div>
    </section>
  );
}
```

주의:

```text
단순 role="dialog"만으로 완전한 Modal 접근성이 보장되지는 않는다.
Focus 이동, Escape 닫기, Focus Trap, Focus 복귀도 검토해야 한다.
```

나쁜 예:

```tsx
function Modal({ children }: { children: React.ReactNode }) {
  return <div>{children}</div>;
}
```

문제:

```text
dialog 의미가 없다.
title 연결이 없다.
닫기 구조가 없다.
focus 흐름이 없다.
```

---

### [FAQ]

Q. Modal에는 어떤 접근성 속성이 필요해?
A. role="dialog", aria-modal="true", aria-labelledby, 닫기 버튼, focus 관리가 필요하다.

Q. Modal title은 왜 연결해야 해?
A. Screen Reader가 dialog의 목적을 알 수 있게 하기 위해 aria-labelledby로 제목을 연결한다.

Q. Modal에서 Escape 닫기는 필수야?
A. 일반적으로 권장된다. 사용자가 keyboard로 쉽게 닫을 수 있어야 한다.

Q. Modal focus trap은 언제 필요해?
A. Modal이 열린 동안 keyboard focus가 Modal 내부에 머물러야 할 때 필요하다.

---

## 2.2 Dropdown and Toggle Accessibility Rules

### [개념]

Dropdown and Toggle Accessibility는 열림/닫힘 상태를 가진 Component가 현재 상태와 제어 관계를 보조기술에 전달하도록 하는 기준이다.

Dropdown, Accordion, Disclosure, Toggle Button은 aria-expanded, aria-controls, keyboard interaction을 검토해야 한다.

---

### [핵심]

Dropdown / Toggle 접근성 기준:

- trigger는 button 사용
- aria-expanded로 열림 상태 표시
- aria-controls로 제어 대상 연결
- menu 역할 필요 여부 검토
- keyboard 조작 검토
- Escape 닫기 검토
- click outside 닫기 검토
- focus 이동 검토
- hidden 상태와 DOM 렌더링 방식 결정
- 상태 이름은 isOpen으로 명확히 표현

---

### [실무]

Dropdown 예:

```tsx
function Dropdown({ label, children }: DropdownProps) {
  const [isOpen, setIsOpen] = useState(false);
  const contentId = "dropdown-content";

  return (
    <div>
      <button
        type="button"
        aria-expanded={isOpen}
        aria-controls={contentId}
        onClick={() => setIsOpen((prev) => !prev)}
      >
        {label}
      </button>
      {isOpen && <div id={contentId}>{children}</div>}
    </div>
  );
}
```

Accordion 예:

```tsx
function AccordionItem({ title, children }: AccordionItemProps) {
  const [isOpen, setIsOpen] = useState(false);
  const panelId = "accordion-panel";

  return (
    <section>
      <h3>
        <button
          type="button"
          aria-expanded={isOpen}
          aria-controls={panelId}
          onClick={() => setIsOpen((prev) => !prev)}
        >
          {title}
        </button>
      </h3>
      {isOpen && <div id={panelId}>{children}</div>}
    </section>
  );
}
```

---

### [FAQ]

Q. Dropdown trigger는 div로 만들어도 돼?
A. 권장하지 않는다. trigger는 button을 사용하는 것이 keyboard 접근성에 좋다.

Q. aria-expanded는 언제 써?
A. 열림/닫힘 상태를 가진 Dropdown, Accordion, Disclosure, Toggle에서 사용한다.

Q. aria-controls는 왜 써?
A. trigger가 어떤 영역을 제어하는지 보조기술에 알려준다.

Q. Dropdown에서 Escape 닫기를 구현해야 해?
A. 복잡한 Dropdown이나 Menu에서는 권장된다. 단순 Disclosure라도 keyboard 흐름을 검토해야 한다.

---

# 3. Styling Responsibility

## 3.1 Styling Responsibility Definition

### [개념]

Styling Responsibility는 Component가 어떤 스타일 책임을 내부에서 가지고 어떤 배치 책임을 부모에게 맡길지 결정하는 기준이다.

Component Design에서 스타일 책임은 Component Responsibility와 연결된다.

Reusable UI Component는 자체 시각 스타일을 가질 수 있지만, 외부 배치와 화면 레이아웃은 부모 Layout이나 Page가 담당하는 경우가 많다.

---

### [핵심]

Styling Responsibility 기준:

- Component 자체 스타일
- Layout 스타일
- Parent spacing
- Variant class
- Size class
- State class
- Global style
- Scoped style
- Responsive style
- className extension
- style prop caution

기본 원칙:

- Component 내부 스타일은 Component 책임이다.
- 외부 배치 margin은 부모 책임일 수 있다.
- layout positioning은 Layout Component가 담당한다.
- Reusable Component는 variant와 size를 지원할 수 있다.
- inline style 남용은 피한다.
- className prop은 확장성을 위해 고려한다.
- 도메인 Component와 UI Component 스타일 책임을 구분한다.

---

### [실무]

Card 스타일 책임:

```tsx
type CardProps = {
  className?: string;
  children: React.ReactNode;
};

function Card({ className = "", children }: CardProps) {
  return <section className={`card ${className}`}>{children}</section>;
}
```

책임 구분:

```text
Card
- background
- border
- border-radius
- padding

Parent Layout
- margin
- grid placement
- section spacing
- responsive layout
```

나쁜 예:

```tsx
function Card({ children }: CardProps) {
  return <section style={{ marginTop: 80, width: 1200 }}>{children}</section>;
}
```

문제:

```text
Card가 특정 Page layout에 강하게 결합된다.
Reusable Component로 사용하기 어렵다.
```

---

### [FAQ]

Q. Styling Responsibility가 뭐야?
A. Component가 어떤 스타일을 직접 책임지고 어떤 배치 스타일은 부모에게 맡길지 정하는 기준이다.

Q. Component margin은 내부에서 줘도 돼?
A. 상황에 따라 다르지만 Reusable UI Component는 외부 배치 margin을 부모가 관리하는 것이 유연하다.

Q. className prop을 받아야 해?
A. 재사용 Component라면 외부 스타일 확장이 필요할 수 있어 className prop을 고려한다.

Q. inline style은 쓰면 안 돼?
A. 금지는 아니지만 반복 UI에서는 className, variant, CSS class 기반 스타일이 더 유지보수에 좋다.

---

## 3.2 Styling Anti Pattern

### [개념]

Styling Anti Pattern은 Component 스타일 책임이 흐려져 재사용성과 유지보수성이 떨어지는 문제다.

스타일 책임이 잘못 배치되면 UI Component가 특정 Page에 결합되거나, Page가 모든 세부 스타일을 직접 관리하게 된다.

---

### [핵심]

자주 발생하는 문제:

- Reusable Component가 특정 Page margin을 강제
- UI Component가 fixed width를 강제
- style prop으로 모든 스타일 주입
- variant 대신 className 조합 남발
- boolean style props 과다
- global className 충돌
- Component 내부에서 부모 layout 제어
- inline style 반복
- 도메인 Component와 UI Component 스타일 혼합

해결:

- Component 자체 스타일과 Layout 스타일 분리
- variant / size union 사용
- className 확장 허용
- Page Layout에서 spacing 관리
- 공통 스타일 naming 규칙 유지
- 복잡한 스타일 변형은 Component 분리 검토

---

### [실무]

나쁜 예:

```tsx
type ButtonProps = {
  red?: boolean;
  blue?: boolean;
  large?: boolean;
  small?: boolean;
};
```

문제:

```text
red와 blue가 동시에 true 가능
large와 small이 동시에 true 가능
불가능한 스타일 상태 발생
```

개선:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "danger";
  size?: "sm" | "md" | "lg";
};
```

고정 layout 문제:

```tsx
function Modal() {
  return <section style={{ width: 1200, marginTop: 100 }}>...</section>;
}
```

개선:

```text
Modal
→ dialog 자체 스타일

ModalWrapper / Page
→ 배치와 반응형 layout 조정
```

---

### [FAQ]

Q. style prop으로 모든 스타일을 주입하면 안 좋아?
A. 일관성이 떨어질 수 있다. variant와 className 확장으로 해결 가능한지 먼저 검토한다.

Q. 스타일용 boolean props가 많으면 왜 문제야?
A. 서로 동시에 true가 되어 불가능한 상태가 생길 수 있다. variant와 size union을 사용하는 것이 좋다.

Q. UI Component가 width를 고정하면 안 돼?
A. 상황에 따라 가능하지만 Reusable Component라면 부모 layout에 맞게 유연하게 설계하는 것이 좋다.

Q. 스타일 책임은 어떻게 검수해?
A. Component 자체 스타일, 부모 layout 스타일, variant, className 확장, inline style 남용 여부를 확인한다.

---

# 4. File Structure and Naming

## 4.1 Component File Structure Rules

### [개념]

Component File Structure는 React Component, Hook, API Function, Type, Mapper, Style 파일을 어떤 기준으로 배치할지 정하는 구조다.

파일 구조는 Component Responsibility, Feature Boundary, Reusable Component 기준과 일치해야 한다.

---

### [핵심]

기본 폴더 역할:

- pages: 라우트 화면 단위
- features: 도메인 기능 단위
- components: 공통 UI Component
- hooks: 공통 Custom Hook
- api: 서버 요청 함수
- types: 공유 타입
- mappers: Response Mapping
- utils: 순수 유틸 함수
- styles: 전역 또는 공통 스타일

원칙:

- Page Component는 pages에 둔다.
- 도메인 Feature Component는 features에 둔다.
- 공통 UI Component는 components에 둔다.
- Feature 전용 Hook은 feature 내부 hooks에 둔다.
- 공통 Hook은 shared hooks에 둘 수 있다.
- API 함수는 api 파일로 분리한다.
- Component 이름과 파일명을 일치시킨다.
- 작은 프로젝트에는 과도한 구조를 적용하지 않는다.

---

### [실무]

권장 구조:

```text
src
├ pages
│  └ FestivalSearchPage
│     └ FestivalSearchPage.tsx
├ features
│  └ festival
│     ├ components
│     │  ├ FestivalSearchForm.tsx
│     │  ├ FestivalFilterPanel.tsx
│     │  ├ FestivalList.tsx
│     │  └ FestivalCard.tsx
│     ├ hooks
│     │  └ useFestivalSearch.ts
│     ├ api
│     │  └ festivalApi.ts
│     ├ mappers
│     │  └ festivalMapper.ts
│     └ types
│        └ festivalTypes.ts
├ components
│  ├ Button
│  │  └ Button.tsx
│  ├ Modal
│  │  └ Modal.tsx
│  └ EmptyState
│     └ EmptyState.tsx
├ hooks
│  └ useToggle.ts
└ utils
```

작은 프로젝트 단순 구조:

```text
src
├ pages
├ components
├ api
├ hooks
└ types
```

주의:

```text
모든 Component를 components 폴더에 몰아넣음
→ Feature Boundary 불명확

작은 프로젝트에 깊은 폴더 구조 적용
→ 탐색 비용 증가

API 함수가 Component 파일 내부에 있음
→ API Logic Separation 약화
```

---

### [FAQ]

Q. Component File Structure는 어떻게 잡아?
A. pages, features, components, hooks, api, types 기준으로 역할을 나눌 수 있다.

Q. Feature 기반 폴더 구조는 언제 좋아?
A. 도메인 기능이 많고 Component, API, Hook, Type이 함께 움직일 때 좋다.

Q. 작은 프로젝트도 features 구조를 써야 해?
A. 필수는 아니다. 작은 프로젝트는 pages, components, api, hooks 정도로 단순하게 시작해도 된다.

Q. Component 파일명과 Component 이름은 같아야 해?
A. 권장된다. 검색, import, 유지보수에 유리하다.

---

## 4.2 Component Naming Rules

### [개념]

Component Naming은 Component의 책임과 역할을 드러내는 이름을 붙이는 규칙이다.

좋은 Component 이름은 Page, Feature, UI, Layout, Hook, API 역할을 빠르게 이해하게 한다.

---

### [핵심]

Naming 원칙:

- Component 이름은 PascalCase
- Hook 이름은 use prefix
- Props Type은 ComponentNameProps
- Page Component는 Page suffix 사용 가능
- Layout Component는 Layout suffix 사용 가능
- Feature Component는 도메인 + 기능명 사용
- UI Component는 범용 역할명 사용
- 모호한 이름 금지
- Wrapper, Container, Box 남용 주의
- 이름이 책임을 설명해야 한다.

권장 이름:

```text
FestivalSearchPage
FestivalSearchForm
FestivalFilterPanel
FestivalList
FestivalCard
ReviewForm
NotificationList
PageLayout
Button
Modal
EmptyState
useFestivalSearch
useToggle
```

주의 이름:

```text
CommonBox
DataComponent
Item
Wrapper
Content
Section1
ComponentA
CustomCard
```

---

### [실무]

좋은 이름:

```tsx
function FestivalSearchForm() {
  return null;
}
```

이름이 드러내는 책임:

```text
Festival
→ 도메인

SearchForm
→ 검색 Form 기능
```

나쁜 이름:

```tsx
function DataBox() {
  return null;
}
```

문제:

```text
어떤 데이터를 다루는지 알 수 없다.
Box가 어떤 책임인지 불명확하다.
Component Boundary가 흐려진다.
```

---

### [FAQ]

Q. Component 이름은 어떻게 지어?
A. 도메인과 역할이 드러나도록 PascalCase로 짓는다.

Q. Page Component 이름에는 Page를 붙여야 해?
A. 필수는 아니지만 라우트 화면 단위라면 FestivalSearchPage처럼 Page suffix가 명확하다.

Q. Wrapper라는 이름은 쓰면 안 돼?
A. 금지는 아니지만 책임이 불명확하면 피한다. PageLayout, Section, Card처럼 구체적인 이름이 좋다.

Q. Hook 이름은 어떻게 지어?
A. 반드시 use로 시작하고 useFestivalSearch, useToggle처럼 책임을 드러내야 한다.

---

# 5. Troubleshooting

## 5.1 Overgrown Component

### [개념]

Overgrown Component는 하나의 Component가 너무 많은 책임과 코드를 가져 유지보수하기 어려운 상태다.

React Component Design에서 가장 자주 발생하는 문제다.

---

### [핵심]

문제 신호:

- JSX가 너무 길다.
- State가 너무 많다.
- useEffect가 너무 많다.
- Event Handler가 너무 많다.
- API Logic과 UI Logic이 섞인다.
- Form, List, Modal, Pagination이 한 Component에 섞인다.
- loading / error / empty 조건이 복잡하다.
- 수정 시 영향 범위가 크다.

원인:

- Component Responsibility 미정의
- Component Boundary 미정의
- Page Component에 모든 코드 작성
- Custom Hook 분리 지연
- UI Component 추출 지연
- API 함수 분리 지연

---

### [실무]

해결 Flow:

```text
Find Overgrown Component
→ Identify UI Sections
→ Extract Presentational Components
→ Extract Feature Components
→ Extract API Functions
→ Extract Custom Hook
→ Review State Ownership
→ Define Props Contract
```

Before:

```text
FestivalPage
- API 요청
- 검색 Form
- 필터
- 목록
- 카드
- Modal
- Pagination
- Error UI
```

After:

```text
FestivalPage
→ useFestivalSearch
→ FestivalSearchForm
→ FestivalFilterPanel
→ FestivalResultSection
→ FestivalList
→ FestivalCard
→ FestivalDetailModal
→ Pagination
→ ErrorMessage
→ EmptyState
```

---

### [FAQ]

Q. Overgrown Component가 뭐야?
A. 하나의 Component가 API 요청, 상태 관리, 이벤트 처리, 여러 UI 영역 렌더링을 모두 담당해 너무 커진 Component다.

Q. Component가 너무 커졌을 때 어디부터 나눠?
A. 먼저 UI 영역을 기준으로 List, Card, Form, Modal 같은 표시 Component를 분리한다.

Q. useEffect가 많은 Component는 어떻게 해?
A. 각 Effect 목적을 검토하고 API, Timer, Event Listener 로직을 Custom Hook으로 분리할 수 있는지 확인한다.

Q. Overgrown Component는 어떻게 예방해?
A. Component Responsibility, Boundary, State Ownership, Props Contract를 코드 작성 전 설계한다.

---

## 5.2 Props Drilling Problem

### [개념]

Props Drilling은 여러 중간 Component를 거쳐 깊은 자식 Component에게 Props를 계속 전달하는 문제다.

Props Drilling은 State Owner가 부적절하거나 Component Composition이 복잡할 때 자주 발생한다.

---

### [핵심]

문제:

- 중간 Component가 사용하지 않는 Props 전달
- Props 변경 시 여러 파일 수정
- Component 재사용성 저하
- 데이터 흐름 추적 어려움
- Component Boundary 불명확
- State 위치 부적절

해결:

- State Owner 재검토
- Component 구조 단순화
- children composition 활용
- slot-like props 활용
- Context 검토
- 전역 상태 검토
- Feature Boundary 재설계

---

### [실무]

Debug Flow:

```text
Trace Prop Path
→ Check Intermediate Usage
→ Review State Owner
→ Reduce Component Depth
→ Use Composition
→ Consider Context or Global State
```

판단:

```text
1~2단계 Props 전달
→ 일반적으로 허용

3단계 이상 반복 전달
→ 구조 검토

중간 Component가 사용하지 않음
→ Props Drilling 의심

여러 페이지에서 동일 상태 사용
→ Context 또는 전역 상태 검토
```

---

### [FAQ]

Q. Props Drilling이 뭐야?
A. 여러 중간 Component를 거쳐 깊은 자식에게 Props를 계속 전달하는 문제다.

Q. Props Drilling은 무조건 나빠?
A. 아니다. 짧은 전달은 자연스럽다. 깊고 반복되어 유지보수가 어려워질 때 문제가 된다.

Q. Props Drilling은 어떻게 해결해?
A. State 위치 조정, Component Composition, Context, 전역 상태를 순서대로 검토한다.

Q. Props Drilling 해결은 무조건 전역 상태야?
A. 아니다. State Ownership과 Component Composition을 먼저 검토하고 필요할 때 Context나 전역 상태를 사용한다.

---

## 5.3 Over-Abstraction Problem

### [개념]

Over-Abstraction은 실제 필요보다 과도하게 추상화해서 Component 사용성이 떨어지는 문제다.

React Component Design에서는 재사용성과 명확성의 균형이 중요하다.

---

### [핵심]

문제:

- 재사용하려고 만든 Component가 이해하기 어렵다.
- Props가 너무 많다.
- variant 조합이 복잡하다.
- Generic Component 사용이 어렵다.
- 단순한 UI 수정도 복잡하다.
- 실제 재사용 빈도가 낮다.
- 도메인 차이를 무시하고 강제로 통합한다.

원인:

- 미래 재사용성 과도 예측
- Design System 없이 공통화 남발
- Component 책임 과다
- Generic / slot / render props 남용
- 중복 제거에만 집중

해결:

- 실제 중복이 확인된 후 추출
- 단순 Component 유지
- 도메인별 Component 분리 허용
- variant 수 줄이기
- 명시적 Component가 더 나은지 검토
- 사용 예제 기준으로 Props API 재설계

---

### [실무]

판단 Flow:

```text
Is it reused now?
→ Does abstraction reduce duplication?
→ Is props API understandable?
→ Are variants limited?
→ Is explicit component simpler?
```

나쁜 예:

```text
UniversalCard
→ Festival mode
→ Review mode
→ User mode
→ Notification mode
→ Donation mode
```

좋은 예:

```text
Card
→ 공통 wrapper

FestivalCard
→ 축제 도메인 표시

ReviewCard
→ 리뷰 도메인 표시

NotificationItem
→ 알림 도메인 표시
```

---

### [FAQ]

Q. Over-Abstraction이 뭐야?
A. 실제 필요보다 과도하게 추상화해 Component 사용성과 가독성이 떨어지는 문제다.

Q. 재사용 가능하게 만들수록 좋은 거 아니야?
A. 아니다. 실제 사용성이 떨어지는 추상화는 유지보수를 어렵게 만든다.

Q. 중복 코드가 조금 있으면 바로 공통화해야 해?
A. 아니다. 반복 패턴이 명확해지고 변경 방향이 보일 때 공통화하는 것이 안전하다.

Q. Over-Abstraction은 어떻게 해결해?
A. 단순 Component 유지, 도메인별 분리 허용, variant 축소, 명시적 Component 검토로 해결한다.

---

## 5.4 Accessibility Missing Problem

### [개념]

Accessibility Missing Problem은 Component가 시각적으로는 동작하지만 Semantic HTML, Label, Keyboard, Focus, ARIA 기준을 충족하지 못하는 문제다.

접근성 누락은 Reusable UI Component에서 특히 치명적이다.

---

### [핵심]

문제:

- div onClick을 button처럼 사용
- input label 누락
- placeholder를 label로 사용
- img alt 누락
- Modal role 누락
- aria-expanded 누락
- keyboard 조작 불가
- focus 상태 안 보임
- error message와 input 연결 없음
- icon button aria-label 누락

해결:

- Semantic HTML 우선
- button / a 역할 구분
- label과 input 연결
- alt 제공
- role / aria 속성 검토
- keyboard interaction 검토
- focus management 검토
- accessibility checklist 적용

---

### [실무]

Icon Button 예:

```tsx
type IconButtonProps = {
  label: string;
  children: React.ReactNode;
  onClick: () => void;
};

function IconButton({ label, children, onClick }: IconButtonProps) {
  return (
    <button type="button" aria-label={label} onClick={onClick}>
      {children}
    </button>
  );
}
```

나쁜 예:

```tsx
function IconButton({ children, onClick }: IconButtonProps) {
  return <button onClick={onClick}>{children}</button>;
}
```

문제:

```text
아이콘만 있으면 Screen Reader가 버튼 목적을 알기 어렵다.
```

---

### [FAQ]

Q. Accessibility Missing Problem이 뭐야?
A. Component가 시각적으로는 동작하지만 접근성 기준을 충족하지 못하는 문제다.

Q. Icon Button에는 왜 aria-label이 필요해?
A. 아이콘만으로는 Screen Reader가 버튼 목적을 알 수 없기 때문이다.

Q. input label 누락은 왜 문제야?
A. 사용자가 입력 필드 목적을 알기 어렵고 보조기술 사용성이 떨어진다.

Q. 접근성 문제는 어떻게 찾는 게 좋아?
A. Semantic HTML, label, alt, keyboard, focus, ARIA를 순서대로 확인한다.

---

# 6. Component Design Checklist

## 6.1 Full Component Design Checklist

### [개념]

Full Component Design Checklist는 React Component 설계 전체를 검수하기 위한 최종 기준이다.

Frontend Agent와 Review Agent는 Component 생성 전후에 Responsibility, Boundary, Props, State, Composition, Hook, API, TypeScript, Accessibility를 함께 검토해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Component 책임이 명확한가?
- [ ] Component 이름이 역할을 드러내는가?
- [ ] Component Boundary가 적절한가?
- [ ] Page / Feature / UI Component 역할이 구분되는가?
- [ ] Layout Component가 공통 구조만 담당하는가?
- [ ] Props Contract가 명확한가?
- [ ] Props 이름이 모호하지 않은가?
- [ ] Callback Props 이름이 on prefix 기준인가?
- [ ] 내부 Handler 이름이 handle prefix 기준인가?
- [ ] Boolean Props가 불가능한 상태를 만들지 않는가?
- [ ] variant union type이 필요한 곳에 사용되었는가?
- [ ] State Owner가 적절한가?
- [ ] State를 너무 위로 올리지 않았는가?
- [ ] State를 너무 아래에 두지 않았는가?
- [ ] Local State와 Shared State가 구분되는가?
- [ ] Server State와 UI State가 구분되는가?
- [ ] Derived State를 불필요하게 만들지 않았는가?
- [ ] API Logic과 UI Logic이 과도하게 섞이지 않았는가?
- [ ] API Function이 api 파일로 분리되었는가?
- [ ] 반복 로직은 Custom Hook 분리 대상인가?
- [ ] Custom Hook 책임이 명확한가?
- [ ] Hook 반환 Contract가 명확한가?
- [ ] Reusable UI Component가 도메인에 강하게 의존하지 않는가?
- [ ] children / slot-like props 사용이 적절한가?
- [ ] TypeScript Props Type이 안정적인가?
- [ ] any Props를 사용하지 않았는가?
- [ ] Required / Optional / Nullable Props가 구분되는가?
- [ ] 접근성 기본 기준이 반영되었는가?
- [ ] Props Drilling이 과도하지 않은가?
- [ ] Overgrown Component가 아닌가?
- [ ] Over-Abstraction이 아닌가?
- [ ] Wrapper Hell이 발생하지 않았는가?
- [ ] 파일 구조가 Component 역할과 일치하는가?
```

---

### [실무]

Review Flow:

```text
Component Tree Review
→ Responsibility Check
→ Boundary Check
→ Props Check
→ State Ownership Check
→ Composition Check
→ Custom Hook Check
→ API Logic Check
→ TypeScript Check
→ Accessibility Check
→ Anti Pattern Check
```

치명적 문제:

```text
- Page Component가 전체 기능을 모두 담당
- UI Component가 API 호출 수행
- State Owner가 불명확함
- Props Type이 any
- Props 이름이 data, item, flag, action처럼 모호함
- 여러 boolean props로 불가능한 상태 발생
- Derived State를 중복 저장
- Custom Hook이 Page 전체 책임을 가짐
- 접근성 없는 Button / Modal / Input 작성
- 공통 Component가 도메인 로직에 강하게 의존
```

---

### [FAQ]

Q. Component Design 검수에서 가장 중요한 것은?
A. 책임, 경계, Props Contract, State Ownership, 재사용성, 접근성, Anti Pattern 포함 여부다.

Q. Review Agent는 무엇부터 확인해야 해?
A. Component Responsibility와 Boundary가 명확한지 먼저 확인해야 한다.

Q. 치명적인 Component 설계 문제는 뭐야?
A. UI Component API 호출, State Owner 불명확, any Props, 접근성 누락, Overgrown Component가 치명적이다.

Q. Checklist는 언제 사용해?
A. Component 코드 생성 전 설계 단계와 코드 작성 후 Review 단계에서 모두 사용한다.

---

## 6.2 Agent Review Output Rules

### [개념]

Agent Review Output Rules는 Frontend Agent와 Review Agent가 React Component 설계 결과를 검토할 때 출력해야 하는 항목이다.

Agent는 단순 코드 생성이 아니라 설계 근거와 위험 요소를 함께 제공해야 한다.

---

### [핵심]

Review Output 항목:

- Component Tree
- Responsibility Review
- Boundary Review
- Props Contract Review
- State Ownership Review
- Composition Review
- Custom Hook Review
- API Logic Separation Review
- TypeScript Props Review
- Accessibility Review
- Anti Pattern Review
- Final Decision

---

### [실무]

출력 예:

```text
Component Tree:
FestivalSearchPage
→ FestivalSearchForm
→ FestivalFilterPanel
→ FestivalResultSection
  → FestivalList
    → FestivalCard

Review:
- Responsibility: 적절
- Boundary: Search / Filter / Result 영역 분리 적절
- Props Contract: onSearch, filters, onChangeFilters 명확
- State Ownership: keyword, filters는 Page State 적절
- API Logic: useFestivalSearch Hook 분리 적절
- TypeScript: Props Type 명확
- Accessibility: input label, button type 확인 필요
- Anti Pattern: Props Drilling 과도하지 않음

Final Decision:
- 통과
- 단, SearchForm input label 연결 확인 필요
```

---

### [FAQ]

Q. Agent Review Output에는 무엇이 포함돼야 해?
A. Component Tree, Responsibility, Boundary, Props, State, Hook, API, TypeScript, Accessibility, Anti Pattern Review가 포함되어야 한다.

Q. Review Agent는 코드만 보면 돼?
A. 아니다. Component 설계 의도와 데이터 흐름, 책임 배치도 함께 검토해야 한다.

Q. Final Decision은 왜 필요해?
A. 설계가 통과 가능한지, 수정이 필요한지 Agent가 명확히 판단하기 위해 필요하다.

Q. Review에서 치명적 문제를 찾으면 어떻게 해?
A. 문제 원인, 영향, 수정 방향을 짧고 명확하게 제시해야 한다.

---

# 7. Final Domain Goal

## 7.1 React Component Design Final Goal

### [개념]

React Component Design 문서의 최종 목적은 Frontend Agent가 유지보수 가능한 React Component 구조를 설계하고 Review Agent가 Component Anti Pattern을 검출할 수 있게 하는 것이다.

이 문서는 React 기본 문법 설명서가 아니라, AI Agent Retrieval과 Code Generation, Review, Validation을 위한 RAG 최적화 문서다.

---

### [핵심]

최종 목표:

- Component Responsibility 정의
- Component Boundary 설정
- Page / Feature / UI Component 구분
- Layout Component 설계
- Props Contract 설계
- Props Naming 적용
- Callback Props 설계
- Boolean Props 개선
- Variant 설계
- State Ownership 결정
- Lifting State Up 적용
- Local State / Shared State 구분
- Server State / UI State 구분
- URL State / Global State 검토
- Component Composition 적용
- children / Slot-like Props 사용
- Container / Presentational 분리 판단
- Custom Hook 추출 판단
- API Logic Separation 적용
- Response Mapping 적용
- Reusable Component 설계
- React TypeScript Props Type 작성
- Component Accessibility 검토
- Component Anti Pattern 탐지
- File Structure 설계

---

### [실무]

Frontend Agent 수행 Flow:

```text
User Frontend Screen Request
→ Analyze Screen Sections
→ Define Component Responsibility
→ Split Page / Feature / UI Components
→ Decide State Ownership
→ Design Props Contract
→ Design Component Composition
→ Extract Hook if Needed
→ Separate API Logic
→ Define TypeScript Props Type
→ Check Accessibility
→ Review Anti Patterns
→ Generate Maintainable Component Output
```

Review Agent 수행 Flow:

```text
Generated Component Code
→ Component Tree Review
→ Responsibility Review
→ Boundary Review
→ Props Review
→ State Review
→ Composition Review
→ Hook Review
→ API Review
→ TypeScript Review
→ Accessibility Review
→ Anti Pattern Review
→ Final Decision
```

---

### [FAQ]

Q. React Component Design 문서의 최종 목적은 뭐야?
A. Frontend Agent가 React 화면을 책임, 경계, Props, State, Composition 기준으로 분해하고 유지보수 가능한 Component 구조를 설계하게 만드는 것이다.

Q. 이 문서는 React 문법 학습용이야?
A. 아니다. AI Agent Retrieval, Code Generation, Review, Validation을 위한 RAG 최적화 문서다.

Q. Frontend Agent는 이 문서로 무엇을 해야 해?
A. 화면 요구사항을 Component Tree로 분해하고 Props, State, Hook, API, TypeScript, 접근성 기준으로 코드를 생성해야 한다.

Q. Review Agent는 이 문서로 무엇을 해야 해?
A. React Component 설계의 책임 혼합, Props 문제, State 문제, API 결합, 접근성 누락, 과도한 추상화를 검출해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. React Component Accessibility가 뭐야?
A. Component 단위에서 Semantic HTML, ARIA, Keyboard Interaction, Focus Management를 고려해 접근 가능한 UI를 만드는 기준이다.

Q. div에 onClick을 달아서 버튼처럼 써도 돼?
A. 권장하지 않는다. 동작 버튼은 button 태그를 사용해야 키보드 접근성과 기본 동작을 얻을 수 있다.

Q. ARIA를 많이 붙이면 접근성이 좋아져?
A. 아니다. 먼저 Semantic HTML을 사용하고 부족한 의미를 보완할 때 ARIA를 사용한다.

Q. Semantic HTML이 왜 중요해?
A. 요소의 의미를 브라우저, 보조기술, 개발자가 명확히 이해할 수 있게 해 접근성과 유지보수성을 높인다.

Q. button과 a는 어떻게 구분해?
A. 현재 화면에서 동작을 수행하면 button, 다른 URL이나 Route로 이동하면 a 또는 Link를 사용한다.

Q. input에는 label이 꼭 필요해?
A. 필요하다. label은 사용자가 입력 필드의 목적을 이해하게 해준다.

Q. placeholder를 label 대신 써도 돼?
A. 권장하지 않는다. placeholder는 보조 설명일 뿐 label을 대체하지 않는다.

Q. aria-invalid는 언제 써?
A. 입력값이 유효하지 않은 상태임을 보조기술에 알릴 때 사용한다.

Q. Modal에는 어떤 접근성 속성이 필요해?
A. role="dialog", aria-modal="true", aria-labelledby, 닫기 버튼, focus 관리가 필요하다.

Q. Modal title은 왜 연결해야 해?
A. Screen Reader가 dialog의 목적을 알 수 있게 하기 위해 aria-labelledby로 제목을 연결한다.

Q. Modal에서 Escape 닫기는 필수야?
A. 일반적으로 권장된다. 사용자가 keyboard로 쉽게 닫을 수 있어야 한다.

Q. Dropdown trigger는 div로 만들어도 돼?
A. 권장하지 않는다. trigger는 button을 사용하는 것이 keyboard 접근성에 좋다.

Q. aria-expanded는 언제 써?
A. 열림/닫힘 상태를 가진 Dropdown, Accordion, Disclosure, Toggle에서 사용한다.

Q. aria-controls는 왜 써?
A. trigger가 어떤 영역을 제어하는지 보조기술에 알려준다.

Q. Styling Responsibility가 뭐야?
A. Component가 어떤 스타일을 직접 책임지고 어떤 배치 스타일은 부모에게 맡길지 정하는 기준이다.

Q. Component margin은 내부에서 줘도 돼?
A. 상황에 따라 다르지만 Reusable UI Component는 외부 배치 margin을 부모가 관리하는 것이 유연하다.

Q. className prop을 받아야 해?
A. 재사용 Component라면 외부 스타일 확장이 필요할 수 있어 className prop을 고려한다.

Q. style prop으로 모든 스타일을 주입하면 안 좋아?
A. 일관성이 떨어질 수 있다. variant와 className 확장으로 해결 가능한지 먼저 검토한다.

Q. 스타일용 boolean props가 많으면 왜 문제야?
A. 서로 동시에 true가 되어 불가능한 상태가 생길 수 있다. variant와 size union을 사용하는 것이 좋다.

Q. Component File Structure는 어떻게 잡아?
A. pages, features, components, hooks, api, types 기준으로 역할을 나눌 수 있다.

Q. Feature 기반 폴더 구조는 언제 좋아?
A. 도메인 기능이 많고 Component, API, Hook, Type이 함께 움직일 때 좋다.

Q. 작은 프로젝트도 features 구조를 써야 해?
A. 필수는 아니다. 작은 프로젝트는 pages, components, api, hooks 정도로 단순하게 시작해도 된다.

Q. Component 이름은 어떻게 지어?
A. 도메인과 역할이 드러나도록 PascalCase로 짓는다.

Q. Hook 이름은 어떻게 지어?
A. 반드시 use로 시작하고 useFestivalSearch, useToggle처럼 책임을 드러내야 한다.

Q. Overgrown Component가 뭐야?
A. 하나의 Component가 API 요청, 상태 관리, 이벤트 처리, 여러 UI 영역 렌더링을 모두 담당해 너무 커진 Component다.

Q. Component가 너무 커졌을 때 어디부터 나눠?
A. 먼저 UI 영역을 기준으로 List, Card, Form, Modal 같은 표시 Component를 분리한다.

Q. useEffect가 많은 Component는 어떻게 해?
A. 각 Effect 목적을 검토하고 API, Timer, Event Listener 로직을 Custom Hook으로 분리할 수 있는지 확인한다.

Q. Props Drilling이 뭐야?
A. 여러 중간 Component를 거쳐 깊은 자식에게 Props를 계속 전달하는 문제다.

Q. Props Drilling은 무조건 나빠?
A. 아니다. 짧은 전달은 자연스럽다. 깊고 반복되어 유지보수가 어려워질 때 문제가 된다.

Q. Props Drilling은 어떻게 해결해?
A. State 위치 조정, Component Composition, Context, 전역 상태를 순서대로 검토한다.

Q. Over-Abstraction이 뭐야?
A. 실제 필요보다 과도하게 추상화해 Component 사용성과 가독성이 떨어지는 문제다.

Q. 재사용 가능하게 만들수록 좋은 거 아니야?
A. 아니다. 실제 사용성이 떨어지는 추상화는 유지보수를 어렵게 만든다.

Q. 중복 코드가 조금 있으면 바로 공통화해야 해?
A. 아니다. 반복 패턴이 명확해지고 변경 방향이 보일 때 공통화하는 것이 안전하다.

Q. Accessibility Missing Problem이 뭐야?
A. Component가 시각적으로는 동작하지만 접근성 기준을 충족하지 못하는 문제다.

Q. Icon Button에는 왜 aria-label이 필요해?
A. 아이콘만으로는 Screen Reader가 버튼 목적을 알 수 없기 때문이다.

Q. Component Design 검수에서 가장 중요한 것은?
A. 책임, 경계, Props Contract, State Ownership, 재사용성, 접근성, Anti Pattern 포함 여부다.

Q. Review Agent는 무엇부터 확인해야 해?
A. Component Responsibility와 Boundary가 명확한지 먼저 확인해야 한다.

Q. 치명적인 Component 설계 문제는 뭐야?
A. UI Component API 호출, State Owner 불명확, any Props, 접근성 누락, Overgrown Component가 치명적이다.

Q. Agent Review Output에는 무엇이 포함돼야 해?
A. Component Tree, Responsibility, Boundary, Props, State, Hook, API, TypeScript, Accessibility, Anti Pattern Review가 포함되어야 한다.

Q. React Component Design 문서의 최종 목적은 뭐야?
A. Frontend Agent가 React 화면을 책임, 경계, Props, State, Composition 기준으로 분해하고 유지보수 가능한 Component 구조를 설계하게 만드는 것이다.

Q. React Component Design Part07의 핵심은 뭐야?
A. Accessibility, Styling Responsibility, File Structure, Troubleshooting, Checklist를 통해 React Component 설계의 최종 품질을 검수하는 것이다.
