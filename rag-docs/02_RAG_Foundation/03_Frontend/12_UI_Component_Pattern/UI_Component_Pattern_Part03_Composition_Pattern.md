# UI Component Pattern Part03 - Composition Pattern

---

# 1. Composition Pattern Overview

## 1.1 Composition Pattern Purpose

### [개념]

Composition Pattern은 UI Component를 Props만으로 확장하지 않고, 작은 Component와 children, slot-like props, compound structure를 조합해 유연하게 구성하는 설계 기준이다.

UI Component Pattern에서 Composition Pattern은 Props Explosion과 Over Abstraction을 줄이고, Common UI와 Feature UI를 안전하게 분리하기 위한 핵심 전략이다.

Composition Pattern은 Component 내부의 모든 예외를 Props로 처리하지 않고, 외부에서 필요한 UI를 조합하게 만든다.

---

### [핵심]

Composition Pattern 핵심 목적:

- Props Explosion 방지
- Over Abstraction 방지
- Common UI 단순화
- Feature UI 조합성 강화
- children 활용
- slot-like props 활용
- Compound Component 기초 판단
- Layout Component와 UI Component 책임 분리
- 재사용 가능한 구조 제공
- 도메인 로직과 공통 UI 분리

Composition 대상:

- Card
- Modal
- Dialog
- Layout
- EmptyState
- ErrorState
- ListItem
- Tabs
- Accordion
- Dropdown
- FormField

---

### [실무]

2026 실무 기준에서 Composition Pattern은 공통 Component를 과도하게 범용화하지 않기 위한 기본 전략이다.

나쁜 방향:

```text
하나의 Component에 모든 기능을 props로 추가
→ Props 증가
→ 조건문 증가
→ 사용법 복잡
→ Common UI가 Feature UI로 오염
```

좋은 방향:

```text
작은 Common UI 제공
→ Feature UI에서 조합
→ 필요한 위치만 slot-like props로 확장
→ 복잡한 구조는 Compound Component 검토
```

Component 설계 흐름:

```text
Define Responsibility
→ Check Props Complexity
→ Use children
→ Use slot-like props
→ Use Feature Composition
→ Consider Compound Component
→ Review Accessibility
```

---

### [FAQ]

Q. Composition Pattern은 왜 필요해?
A. 모든 예외를 Props로 처리하면 Props Explosion이 발생하므로 children과 조합 구조로 UI 확장성을 확보하기 위해 필요하다.

Q. Composition Pattern은 Props Design과 뭐가 달라?
A. Props Design은 Component API를 설계하는 것이고, Composition Pattern은 Component를 조합해 구조를 확장하는 방식이다.

Q. Composition Pattern에서 가장 중요한 기준은 뭐야?
A. Common UI는 단순하게 유지하고 Feature UI에서 필요한 도메인 UI를 조합하는 것이다.

---

# 2. Children Pattern

## 2.1 Children Pattern Basics

### [개념]

Children Pattern은 Component 내부에 들어갈 내용을 props.children으로 받아 외부에서 자유롭게 조합하는 방식이다.

children은 Common UI Component가 내부 콘텐츠의 구체적인 도메인 구조를 몰라도 재사용될 수 있게 한다.

---

### [핵심]

children 적합 대상:

- Button
- Card
- Modal
- Dialog
- Layout
- Section
- ListItem
- FormField
- EmptyState action area
- ErrorState action area

children 사용 기준:

- 내부 내용이 다양함
- 외부에서 자유롭게 조합해야 함
- Component가 도메인 데이터를 몰라야 함
- Component가 wrapper 역할을 함
- 콘텐츠 구조가 고정되지 않음
- ReactNode 전달이 자연스러움

주의:

- 모든 데이터를 children으로 받지 않음
- title, value, label처럼 의미가 명확하면 명시 Props 사용 가능
- children 필수 여부를 타입으로 표현
- children 내부 구조를 과도하게 가정하지 않음
- children만으로 접근성 연결이 어려우면 명시 Props 사용

---

### [실무]

Card children 예:

```tsx
type CardProps = {
  children: React.ReactNode;
};

function Card({ children }: CardProps) {
  return <article className="card">{children}</article>;
}
```

사용:

```tsx
<Card>
  <h3>축제 제목</h3>
  <p>서울 강남구</p>
  <Badge>문화</Badge>
</Card>
```

Button children 예:

```tsx
type ButtonProps = {
  children: React.ReactNode;
  onClick?: () => void;
};

function Button({ children, onClick }: ButtonProps) {
  return (
    <button type="button" onClick={onClick}>
      {children}
    </button>
  );
}
```

Feature UI 조합 예:

```tsx
function FestivalCard({ festival }: { festival: Festival }) {
  return (
    <Card>
      <h3>{festival.title}</h3>
      <p>{festival.regionName}</p>
      <Badge>{festival.categoryName}</Badge>
    </Card>
  );
}
```

---

### [FAQ]

Q. children은 언제 써?
A. Component 내부 내용이 다양하거나 외부에서 자유롭게 조합해야 할 때 사용한다.

Q. 모든 것을 children으로 받으면 좋아?
A. 아니다. title, value, label처럼 의미가 명확한 데이터는 명시 Props가 더 좋을 수 있다.

Q. children 타입은 뭘로 두는 게 좋아?
A. ReactNode를 사용하는 경우가 많다.

---

## 2.2 Children Pattern Anti Pattern

### [개념]

Children Pattern Anti Pattern은 children을 너무 많이 사용해 Component 사용 의도가 불명확해지거나 접근성 연결이 어려워지는 문제다.

children은 유연하지만, 의미가 명확한 필드는 Props로 드러내는 것이 더 안전할 수 있다.

---

### [핵심]

주의 패턴:

- 의미가 중요한 데이터를 모두 children으로 처리
- label과 input 연결이 불명확함
- title id 연결이 어려움
- 내부 구조를 Component가 강제로 가정
- children 순서에 의존
- children 내부 타입을 검사하려 함
- 접근성 속성 연결이 누락됨

명시 Props가 좋은 경우:

- label
- title
- description
- value
- error
- helperText
- id
- name
- ariaLabel
- open
- onClose

---

### [실무]

나쁜 예:

```tsx
function TextField({ children }: { children: React.ReactNode }) {
  return <div className="field">{children}</div>;
}
```

사용 시 문제:

```tsx
<TextField>
  <span>이메일</span>
  <input />
  <p>이메일을 입력하세요.</p>
</TextField>
```

문제점:

```text
label과 input 연결 불명확
error 연결 불명확
aria-describedby 처리 어려움
Form Field 책임 불명확
```

개선:

```tsx
type TextFieldProps = {
  id: string;
  label: string;
  value: string;
  error?: string;
  helperText?: string;
  onChange: (value: string) => void;
};

function TextField({
  id,
  label,
  value,
  error,
  helperText,
  onChange,
}: TextFieldProps) {
  const errorId = `${id}-error`;
  const helperId = `${id}-helper`;

  return (
    <div className="field">
      <label htmlFor={id}>{label}</label>
      <input
        id={id}
        value={value}
        aria-invalid={Boolean(error)}
        aria-describedby={error ? errorId : helperText ? helperId : undefined}
        onChange={(event) => onChange(event.target.value)}
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

---

### [FAQ]

Q. children을 많이 쓰면 무조건 좋아?
A. 아니다. 의미와 접근성 연결이 필요한 값은 명시 Props가 더 안전하다.

Q. TextField는 children으로 만드는 게 좋아?
A. label, error, aria-describedby 연결이 필요하므로 명시 Props 기반 TextField가 더 적합한 경우가 많다.

Q. children 내부 구조를 검사해도 돼?
A. 가능은 하지만 복잡도가 커진다. 구조 제어가 필요하면 slot-like props나 compound pattern을 검토한다.

---

# 3. Slot-like Pattern

## 3.1 Slot-like Pattern Basics

### [개념]

Slot-like Pattern은 Component의 특정 위치에 들어갈 UI를 ReactNode Props로 전달하는 방식이다.

React에서는 header, footer, action, icon, rightArea 같은 Props로 Slot-like Pattern을 구현할 수 있다.

Slot-like Pattern은 위치가 정해진 확장 영역을 제공할 때 유용하다.

---

### [핵심]

Slot-like Props 사용 대상:

- Modal footer
- Modal header action
- Card action
- PageHeader action
- EmptyState action
- ErrorState action
- ListItem leftArea
- ListItem rightArea
- Table custom cell
- Layout sidebar
- Dropdown trigger
- SearchBox suffix

권장 이름:

- header
- footer
- action
- actions
- icon
- leftArea
- rightArea
- prefix
- suffix
- trigger
- sidebar

주의:

- slot props가 너무 많으면 Component 책임이 커짐
- 위치와 목적이 명확해야 함
- 단순 문자열은 명시 Props가 더 좋을 수 있음
- 복잡한 구조는 Compound Component 검토
- 접근성 책임이 어디에 있는지 명확해야 함

---

### [실무]

EmptyState action 예:

```tsx
type EmptyStateProps = {
  title: string;
  description?: string;
  action?: React.ReactNode;
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

사용:

```tsx
<EmptyState
  title="검색 결과가 없습니다."
  description="검색어를 바꾸거나 필터를 초기화해 보세요."
  action={<Button onClick={resetFilter}>필터 초기화</Button>}
/>
```

Modal footer 예:

```tsx
type ModalProps = {
  open: boolean;
  title: string;
  footer?: React.ReactNode;
  onClose: () => void;
  children: React.ReactNode;
};

function Modal({ open, title, footer, onClose, children }: ModalProps) {
  if (!open) {
    return null;
  }

  return (
    <section role="dialog" aria-modal="true" aria-labelledby="modal-title">
      <header>
        <h2 id="modal-title">{title}</h2>
        <button type="button" onClick={onClose} aria-label="닫기">
          ×
        </button>
      </header>
      <div>{children}</div>
      {footer && <footer>{footer}</footer>}
    </section>
  );
}
```

---

### [FAQ]

Q. action props는 왜 ReactNode로 받아?
A. 버튼, 링크, 여러 액션 등 다양한 UI를 유연하게 넣기 위해서다.

Q. slot props는 언제 써?
A. Component 내부의 특정 위치에 외부 UI를 넣어야 할 때 사용한다.

Q. header, footer는 children으로 처리하면 안 돼?
A. 가능하지만 위치가 고정되어야 하면 명시적인 slot-like props가 더 명확할 수 있다.

---

## 3.2 Slot-like Pattern Boundary

### [개념]

Slot-like Pattern Boundary는 slot-like props를 어디까지 허용할지 정하는 기준이다.

Slot-like Props는 유연하지만 너무 많아지면 Component API가 복잡해지고, Component 책임이 불명확해진다.

---

### [핵심]

적절한 Slot-like Props:

- action 하나만 필요한 EmptyState
- footer만 필요한 Modal
- rightArea만 필요한 ListItem
- icon만 필요한 Button
- trigger만 필요한 Dropdown

과도한 Slot-like Props:

- headerLeft
- headerRight
- bodyTop
- bodyBottom
- footerLeft
- footerRight
- beforeContent
- afterContent
- customRenderer
- customWrapper
- customEverything

해결 기준:

- slot props가 3개 이상이면 책임 재검토
- children 구조로 단순화
- Compound Component 검토
- Feature Component로 분리
- Layout Component로 분리
- Common UI 범위 축소

---

### [실무]

나쁜 예:

```tsx
type CardProps = {
  headerLeft?: React.ReactNode;
  headerRight?: React.ReactNode;
  bodyTop?: React.ReactNode;
  bodyBottom?: React.ReactNode;
  footerLeft?: React.ReactNode;
  footerRight?: React.ReactNode;
  action?: React.ReactNode;
};
```

문제점:

```text
Card 책임 과도
사용법 복잡
Feature 요구사항 누적
children으로 해결 가능한 구조
```

개선:

```tsx
type CardProps = {
  children: React.ReactNode;
};

function Card({ children }: CardProps) {
  return <article className="card">{children}</article>;
}
```

Feature에서 조합:

```tsx
function FestivalCard({ festival }: { festival: Festival }) {
  return (
    <Card>
      <header>
        <h3>{festival.title}</h3>
        <Badge>{festival.categoryName}</Badge>
      </header>
      <p>{festival.regionName}</p>
      <footer>
        <Button>자세히 보기</Button>
      </footer>
    </Card>
  );
}
```

---

### [FAQ]

Q. slot props가 많아지면 어떻게 해?
A. Component 책임이 커졌을 수 있다. children 구조나 compound pattern을 검토한다.

Q. Card에 header, body, footer props를 모두 넣는 게 좋아?
A. 단순 Card라면 children으로 조합하는 편이 더 유연할 수 있다.

Q. slot-like props는 몇 개까지 괜찮아?
A. 정해진 숫자는 없지만 3개 이상이면 Component 책임과 API 복잡도를 재검토하는 것이 좋다.

---

# 4. Compound Component Pattern

## 4.1 Compound Component Basics

### [개념]

Compound Component는 관련된 여러 하위 Component를 조합해 하나의 UI 패턴을 구성하는 방식이다.

Tabs, Accordion, Dropdown, Select, Modal 같은 UI에서 하위 Component 간 관계가 강할 때 사용할 수 있다.

---

### [핵심]

Compound Component 적합 대상:

- Tabs
- Accordion
- Modal
- Dropdown
- Select
- Menu
- Stepper
- FormField group

Compound Component 장점:

- 조합 자유도 높음
- 관련 UI 구조를 명확히 표현
- Props Explosion 감소
- 하위 Component 역할 분리
- 복잡한 UI 패턴 표현 가능

주의:

- 구현 복잡도 증가
- 내부 상태 공유 기준 필요
- Context 사용 가능성 증가
- 접근성 구현 난도 증가
- Foundation 범위에서는 기초 판단만 다룸

---

### [실무]

Tabs 사용 형태:

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

역할 분리:

```text
Tabs
→ selected value 상태 관리

Tabs.List
→ tab trigger group 제공

Tabs.Trigger
→ tab 선택 버튼 제공

Tabs.Content
→ selected value에 맞는 panel 표시
```

단순한 경우에는 Compound Component가 필요 없다.

```tsx
function SimpleTabs({ selectedTab, onChange }: SimpleTabsProps) {
  return (
    <div>
      <button type="button" onClick={() => onChange("info")}>
        정보
      </button>
      <button type="button" onClick={() => onChange("review")}>
        리뷰
      </button>
    </div>
  );
}
```

---

### [FAQ]

Q. Compound Component는 언제 써?
A. Tabs나 Accordion처럼 여러 하위 Component가 함께 동작하는 UI에서 유용하다.

Q. 모든 Component를 Compound 방식으로 만들면 좋아?
A. 아니다. 구현 복잡도가 높아질 수 있으므로 조합 자유도가 필요한 UI에만 적용한다.

Q. Compound Component는 Foundation 문서에서 깊게 다뤄?
A. 아니다. 기초 개념과 사용 기준만 다루고 고급 패턴은 Advanced React Pattern 문서가 적합하다.

---

## 4.2 Compound Component Decision Criteria

### [개념]

Compound Component Decision Criteria는 특정 UI를 Compound Component로 만들지 판단하는 기준이다.

Compound Component는 조합 자유도가 필요한 복잡한 UI에 적합하지만, 단순 UI에 사용하면 Over Engineering이 될 수 있다.

---

### [핵심]

Compound Component 적합 기준:

- 하위 Component 간 관계가 강함
- 사용자가 하위 구조를 조합해야 함
- Props만으로 표현하면 복잡함
- 상태를 여러 하위 Component가 공유함
- 접근성 role 관계가 필요함
- 반복 사용되는 복잡 UI 패턴임

Compound Component 부적합 기준:

- 단순 Button
- 단순 Card
- 단순 Badge
- 단순 LoadingState
- 한 화면에서만 사용
- 하위 구조가 고정됨
- Props 몇 개로 충분히 표현 가능
- 사용자가 조합할 필요 없음

---

### [실무]

판단 Flow:

```text
하위 Component가 여러 개인가?
→ 하위 Component가 함께 동작하는가?
→ 상태 공유가 필요한가?
→ 사용자 조합 자유도가 필요한가?
→ Props만으로 표현하면 복잡한가?
→ Compound Component 검토
```

Tabs는 적합:

```text
Tabs
→ List / Trigger / Content 관계 강함
→ selected value 공유
→ role tablist / tab / tabpanel 필요
→ Compound Component 적합
```

Button은 부적합:

```text
Button
→ 단일 액션 Component
→ 하위 관계 약함
→ variant / size / loading Props로 충분
→ Compound Component 불필요
```

---

### [FAQ]

Q. Button도 Compound Component로 만들 수 있어?
A. 가능은 하지만 일반 Button은 variant, size, loading Props로 충분해 Compound Component가 과할 수 있다.

Q. Tabs는 왜 Compound Component가 적합해?
A. List, Trigger, Content가 함께 동작하고 selected value와 접근성 role 관계를 공유하기 때문이다.

Q. Compound Component가 너무 복잡하면 어떻게 해?
A. 단순 Props 기반 Component나 Feature 전용 Component로 범위를 줄이는 것이 좋다.

---

# 5. Feature Composition

## 5.1 Common UI Composition in Feature UI

### [개념]

Feature Composition은 Common UI Component를 Feature UI 안에서 조합해 특정 도메인 화면을 만드는 방식이다.

Common UI는 도메인 구조를 모르고, Feature UI는 Common UI를 조합해 도메인 데이터를 표현한다.

---

### [핵심]

Feature Composition 기준:

- Common UI는 범용 구조 제공
- Feature UI는 도메인 데이터 사용
- API 호출은 Feature Hook 또는 Page에서 처리
- 도메인 이벤트는 Feature Component가 연결
- Common UI에 도메인 Props 추가 금지
- Card / Badge / Button 조합 가능
- LoadingState / ErrorState / EmptyState 조합 가능

역할 분리:

```text
Common UI
→ Card, Button, Badge, Modal

Feature UI
→ FestivalCard, ReviewForm, NotificationItem

Page
→ API 호출, route param, page state
```

---

### [실무]

FestivalCard 예:

```tsx
function FestivalCard({ festival }: { festival: Festival }) {
  return (
    <Card>
      <img src={festival.imageUrl} alt="" />
      <h3>{festival.title}</h3>
      <p>{festival.regionName}</p>
      <Badge>{festival.categoryName}</Badge>
      <Button variant="primary">상세 보기</Button>
    </Card>
  );
}
```

ReviewDeleteButton 예:

```tsx
function ReviewDeleteButton({ reviewId }: { reviewId: number }) {
  const [loading, setLoading] = useState(false);

  async function handleDelete() {
    setLoading(true);
    await deleteReview(reviewId);
    setLoading(false);
  }

  return (
    <Button variant="danger" loading={loading} onClick={handleDelete}>
      리뷰 삭제
    </Button>
  );
}
```

Common Button은 reviewId를 알지 않는다.

```text
Button
→ variant / loading / onClick만 처리

ReviewDeleteButton
→ reviewId / deleteReview 처리
```

---

### [FAQ]

Q. Feature UI에서 Common UI를 사용하는 방식이 좋아?
A. 좋다. Common UI는 기본 구조를 제공하고 Feature UI는 도메인 데이터를 조합하는 방식이 유지보수에 좋다.

Q. Common Button에 reviewId를 넘기면 안 돼?
A. 권장하지 않는다. reviewId는 ReviewDeleteButton 같은 Feature Component에서 처리해야 한다.

Q. API 호출은 Feature UI에서 해도 돼?
A. 가능하지만 복잡한 API 로직은 Custom Hook이나 Page Component로 분리하는 것이 좋다.

---

## 5.2 Composition with State UI

### [개념]

State UI Composition은 LoadingState, ErrorState, EmptyState 같은 상태 UI Component를 Feature UI나 Page에서 조합하는 방식이다.

상태 UI는 요청 상태를 사용자에게 일관되게 보여주는 Common UI 또는 State Component로 관리한다.

---

### [핵심]

State UI 대상:

- LoadingState
- ErrorState
- EmptyState
- Skeleton
- Retry Button
- Inline Error
- Page Error

Composition 기준:

- Page는 loading / error / empty 상태 판단
- State UI는 상태 화면 표시
- ErrorState는 사용자 친화 메시지 사용
- EmptyState는 다음 행동 제공
- LoadingState는 role status 고려
- Retry action은 onRetry로 전달
- API 에러 원문 노출 금지

---

### [실무]

FestivalListPage 예:

```tsx
function FestivalListPage() {
  const { data, loading, error, refetch } = useFestivals();

  if (loading) {
    return <LoadingState message="축제 정보를 불러오는 중입니다." />;
  }

  if (error) {
    return (
      <ErrorState
        message="축제 정보를 불러오지 못했습니다."
        onRetry={refetch}
      />
    );
  }

  if (!data || data.length === 0) {
    return (
      <EmptyState
        title="축제 정보가 없습니다."
        description="검색 조건을 변경해 보세요."
        action={<Button onClick={resetFilter}>필터 초기화</Button>}
      />
    );
  }

  return <FestivalList festivals={data} />;
}
```

역할 분리:

```text
FestivalListPage
→ 상태 판단

LoadingState
→ 로딩 UI 표시

ErrorState
→ 오류 안내와 재시도 제공

EmptyState
→ 빈 결과 안내와 다음 행동 제공

FestivalList
→ 데이터 목록 렌더링
```

---

### [FAQ]

Q. LoadingState, ErrorState, EmptyState는 어디에서 조합해?
A. 보통 Page나 Feature Container에서 데이터 상태를 판단한 뒤 조합한다.

Q. EmptyState action은 왜 ReactNode로 받아?
A. 버튼, 링크, 필터 초기화 등 다양한 다음 행동을 유연하게 넣기 위해서다.

Q. ErrorState에 서버 에러 원문을 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자 친화 메시지로 변환하는 것이 안전하다.

---

# 6. Layout Composition

## 6.1 Layout Component Composition

### [개념]

Layout Composition은 UI Component 자체 스타일과 화면 배치 책임을 분리하는 방식이다.

Button, Card 같은 UI Component는 자체 모양을 담당하고, Grid, Stack, ButtonGroup, PageLayout 같은 Layout Component는 배치를 담당한다.

---

### [핵심]

UI Component 책임:

- 자체 padding
- 자체 border
- 자체 radius
- 자체 variant
- 자체 disabled style
- 자체 error style
- 자체 semantic element

Layout Component 책임:

- flex
- grid
- gap
- margin
- page width
- section spacing
- responsive layout
- alignment
- component placement

Composition 기준:

- Button에 margin 넣지 않음
- Card가 grid 배치를 직접 담당하지 않음
- List가 item 간격을 담당할 수 있음
- PageLayout이 전체 폭과 section spacing 담당
- ButtonGroup이 버튼 간 간격 담당

---

### [실무]

ButtonGroup 예:

```tsx
type ButtonGroupProps = {
  children: React.ReactNode;
};

function ButtonGroup({ children }: ButtonGroupProps) {
  return <div className="button-group">{children}</div>;
}
```

사용:

```tsx
<ButtonGroup>
  <Button variant="secondary">취소</Button>
  <Button variant="primary">저장</Button>
</ButtonGroup>
```

CardGrid 예:

```tsx
function FestivalGrid({ festivals }: { festivals: Festival[] }) {
  return (
    <div className="festival-grid">
      {festivals.map((festival) => (
        <FestivalCard key={festival.festivalId} festival={festival} />
      ))}
    </div>
  );
}
```

책임 분리:

```text
Card
→ 카드 자체 스타일

FestivalCard
→ 축제 정보 표시

FestivalGrid
→ 카드 목록 배치

PageLayout
→ 페이지 전체 레이아웃
```

---

### [FAQ]

Q. Button 안에 margin을 넣어도 돼?
A. 공통 Button에는 margin을 넣지 않는 것이 좋다. 버튼 간 간격은 부모 Layout이나 ButtonGroup이 담당하는 편이 유연하다.

Q. Card가 grid 배치까지 담당해야 해?
A. 보통 Card는 자체 모양만 담당하고 grid 배치는 부모 List나 Layout Component가 담당한다.

Q. Layout Component는 왜 필요해?
A. UI Component 자체 스타일과 화면 배치 책임을 분리해 재사용성과 유지보수성을 높이기 위해 필요하다.

---

## 6.2 Styling Boundary with Composition

### [개념]

Styling Boundary with Composition은 Component 내부 스타일과 외부 조합 스타일의 책임을 나누는 기준이다.

Composition을 사용할 때 className, variant, size, layout wrapper의 역할이 명확해야 스타일 충돌을 줄일 수 있다.

---

### [핵심]

스타일 책임 기준:

- variant는 Component 의미 변형
- size는 Component 크기 변형
- className은 제한적 외부 확장
- layout wrapper는 배치 담당
- inline style은 제한적으로 사용
- margin은 부모 layout이 담당
- gap은 layout wrapper가 담당
- 도메인 전용 스타일은 Feature Component에서 처리

주의:

- 공통 Component 내부 CSS가 너무 강하면 재사용 어려움
- 모든 스타일을 Props로 열면 API 복잡
- className override 기준 없으면 충돌 발생
- Feature 스타일을 Common UI에 계속 추가하면 오염 발생

---

### [실무]

Common UI:

```tsx
type CardProps = {
  className?: string;
  children: React.ReactNode;
};

function Card({ className = "", children }: CardProps) {
  return <article className={`card ${className}`}>{children}</article>;
}
```

Feature UI:

```tsx
function FestivalCard({ festival }: { festival: Festival }) {
  return (
    <Card className="festival-card">
      <h3>{festival.title}</h3>
      <p>{festival.regionName}</p>
    </Card>
  );
}
```

Layout:

```tsx
function FestivalGrid({ children }: { children: React.ReactNode }) {
  return <div className="festival-grid">{children}</div>;
}
```

권장 Flow:

```text
Common UI default style
→ Feature className extension
→ Layout wrapper spacing
→ Review style conflict
```

---

### [FAQ]

Q. 공통 Component에 className을 열어줘야 해?
A. 프로젝트 기준에 따라 다르지만 외부 확장이 필요한 경우 className을 허용하면 유연하다.

Q. style prop을 많이 쓰면 안 돼?
A. 동적 스타일에는 사용할 수 있지만 일관성 있는 UI를 위해 variant, size, className 기준을 우선하는 것이 좋다.

Q. Feature 전용 스타일은 어디에 둬?
A. Feature Component className이나 Feature 스타일 파일에서 처리하는 것이 좋다.

---

# 7. Composition Troubleshooting

## 7.1 Props Explosion Troubleshooting

### [개념]

Props Explosion은 Component가 너무 많은 Props를 받아 사용법이 복잡해지는 문제다.

Composition Pattern은 Props Explosion을 줄이는 주요 해결책이다.

---

### [핵심]

Props Explosion 원인:

- 모든 예외를 Props로 처리
- children 대신 세부 Props를 과도하게 추가
- slot-like props가 너무 많음
- Feature 요구사항을 Common UI에 추가
- 도메인 Props가 공통 Component에 들어감
- boolean Props가 늘어남
- variant가 계속 증가

Composition 해결:

- children으로 콘텐츠 조합
- action / footer 같은 slot-like props 사용
- Feature Component로 도메인 로직 분리
- Layout Component로 배치 분리
- Compound Component 검토
- Common UI 책임 축소

---

### [실무]

문제 예:

```tsx
type EmptyStateProps = {
  title: string;
  description?: string;
  buttonText?: string;
  buttonVariant?: "primary" | "secondary";
  buttonIcon?: React.ReactNode;
  onButtonClick?: () => void;
  linkText?: string;
  linkHref?: string;
  showResetFilter?: boolean;
  showCreateButton?: boolean;
};
```

문제점:

```text
action 종류가 계속 증가
Props 조합 복잡
Feature 요구사항 누적
```

개선:

```tsx
type EmptyStateProps = {
  title: string;
  description?: string;
  action?: React.ReactNode;
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

사용:

```tsx
<EmptyState
  title="검색 결과가 없습니다."
  description="필터를 초기화하거나 검색어를 변경해 보세요."
  action={<Button onClick={resetFilter}>필터 초기화</Button>}
/>
```

---

### [FAQ]

Q. Props가 너무 많으면 어떻게 해?
A. Component 책임을 다시 확인하고 composition, variant, Feature Component 분리를 검토한다.

Q. Props Explosion을 Composition으로 어떻게 줄여?
A. 세부 예외 Props 대신 children이나 action 같은 ReactNode slot을 사용해 외부에서 조합하게 만든다.

Q. action props 하나로 여러 버튼을 처리해도 돼?
A. 가능하다. action을 ReactNode로 받으면 버튼, 링크, 여러 액션을 유연하게 넣을 수 있다.

---

## 7.2 Over Abstraction Troubleshooting

### [개념]

Over Abstraction은 실제 필요보다 너무 범용적인 Component를 만들어 사용과 수정이 어려워지는 문제다.

Composition Pattern은 Over Abstraction을 줄일 수 있지만, 잘못 사용하면 오히려 구조가 과도하게 복잡해질 수 있다.

---

### [핵심]

Over Abstraction 증상:

- Component 조합 방식이 너무 어려움
- 단순 UI에 Compound Component 적용
- Common UI가 도메인 분기로 가득함
- slot props가 과도함
- children 내부 구조를 강제함
- 한 화면 전용 UI를 과도하게 공통화함
- 조합보다 설정이 많음

해결:

- 실제 재사용 사례 확인
- Feature Component로 되돌리기
- Common UI를 작게 유지
- children만으로 충분한지 확인
- slot-like props 축소
- Compound Component 적용 재검토
- 단순 Props 방식으로 되돌리기

---

### [실무]

문제 예:

```tsx
<UniversalCard
  mode="festival"
  headerLeft={<FestivalTitle />}
  headerRight={<FestivalBadge />}
  bodyTop={<FestivalImage />}
  bodyBottom={<FestivalDescription />}
  footerLeft={<LikeButton />}
  footerRight={<DetailButton />}
/>
```

문제점:

```text
UniversalCard 사용법 복잡
Festival 도메인 구조가 Common UI에 영향
slot props 과다
Feature Component로 분리 필요
```

개선:

```tsx
function FestivalCard({ festival }: { festival: Festival }) {
  return (
    <Card>
      <FestivalCardHeader festival={festival} />
      <FestivalCardBody festival={festival} />
      <FestivalCardActions festivalId={festival.festivalId} />
    </Card>
  );
}
```

---

### [FAQ]

Q. 중복 코드를 없애려고 공통 Component를 만들었는데 더 복잡해졌어?
A. Over Abstraction일 수 있다. 반복 제거보다 역할 명확성과 사용 편의성이 중요하다.

Q. Compound Component를 쓰면 무조건 좋은 구조야?
A. 아니다. 단순 UI에는 과할 수 있고 접근성 및 상태 공유 구현이 복잡해질 수 있다.

Q. Composition이 복잡해지면 어떻게 해?
A. Feature Component로 구조를 감싸고 Common UI는 더 작고 단순하게 유지한다.

---

# 8. Composition Pattern Checklist

## 8.1 Composition Review Checklist

### [개념]

Composition Review Checklist는 UI Component 조합 구조가 명확하고 유지보수 가능한지 검수하는 기준이다.

Frontend Agent와 Review Agent는 Component 생성 후 Props와 Composition 구조를 함께 검토해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] children 사용이 적절한가?
- [ ] 의미가 명확한 값은 명시 Props로 분리되었는가?
- [ ] slot-like props의 목적과 위치가 명확한가?
- [ ] slot-like props가 과도하지 않은가?
- [ ] Common UI가 도메인 구조를 모르는가?
- [ ] Feature UI에서 Common UI를 조합하는가?
- [ ] API 호출이 Common UI에 들어가지 않았는가?
- [ ] Layout 책임과 UI 책임이 분리되었는가?
- [ ] margin / gap / grid 책임이 부모 Layout에 있는가?
- [ ] Compound Component 적용이 과하지 않은가?
- [ ] Compound Component가 필요한 이유가 명확한가?
- [ ] 접근성 role 관계가 유지되는가?
- [ ] Props Explosion을 Composition으로 줄였는가?
- [ ] Over Abstraction이 없는가?
- [ ] Feature Component로 분리할 부분이 있는가?
```

---

### [실무]

검수 Flow:

```text
Component Draft
→ Children Check
→ Slot-like Props Check
→ Feature Composition Check
→ Layout Boundary Check
→ Compound Component Check
→ Accessibility Check
→ Anti Pattern Check
→ Final Review
```

치명적 문제:

```text
Common UI가 festival / review / user 도메인 구조를 앎
slot props가 지나치게 많음
children 내부 구조를 강제로 검사
단순 Button에 Compound Component 적용
Card가 grid layout까지 담당
Button 내부 margin 포함
접근성 연결이 children으로 인해 누락
```

---

### [FAQ]

Q. Composition Pattern 검수에서 가장 중요한 것은 뭐야?
A. Common UI가 단순하게 유지되고 Feature UI에서 필요한 도메인 UI를 조합하는지 확인하는 것이다.

Q. Composition이 잘못되었다는 신호는 뭐야?
A. slot props가 많고, children 구조를 강제하며, Common UI가 도메인 데이터를 알기 시작하면 문제가 있을 수 있다.

Q. Review Agent는 Composition을 어떻게 검토해야 해?
A. children, slot-like props, Feature 조합, Layout 책임, Compound 적용 필요성, 접근성을 순서대로 확인해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Composition Pattern은 왜 필요해?
A. 모든 예외를 Props로 처리하면 Props Explosion이 발생하므로 children과 조합 구조로 UI 확장성을 확보하기 위해 필요하다.

Q. Composition Pattern은 Props Design과 뭐가 달라?
A. Props Design은 Component API를 설계하는 것이고, Composition Pattern은 Component를 조합해 구조를 확장하는 방식이다.

Q. Composition Pattern에서 가장 중요한 기준은 뭐야?
A. Common UI는 단순하게 유지하고 Feature UI에서 필요한 도메인 UI를 조합하는 것이다.

Q. children은 언제 써?
A. Component 내부 내용이 다양하거나 외부에서 자유롭게 조합해야 할 때 사용한다.

Q. 모든 것을 children으로 받으면 좋아?
A. 아니다. title, value, label처럼 의미가 명확한 데이터는 명시 Props가 더 좋을 수 있다.

Q. children 타입은 뭘로 두는 게 좋아?
A. ReactNode를 사용하는 경우가 많다.

Q. children을 많이 쓰면 무조건 좋아?
A. 아니다. 의미와 접근성 연결이 필요한 값은 명시 Props가 더 안전하다.

Q. TextField는 children으로 만드는 게 좋아?
A. label, error, aria-describedby 연결이 필요하므로 명시 Props 기반 TextField가 더 적합한 경우가 많다.

Q. children 내부 구조를 검사해도 돼?
A. 가능은 하지만 복잡도가 커진다. 구조 제어가 필요하면 slot-like props나 compound pattern을 검토한다.

Q. action props는 왜 ReactNode로 받아?
A. 버튼, 링크, 여러 액션 등 다양한 UI를 유연하게 넣기 위해서다.

Q. slot props는 언제 써?
A. Component 내부의 특정 위치에 외부 UI를 넣어야 할 때 사용한다.

Q. header, footer는 children으로 처리하면 안 돼?
A. 가능하지만 위치가 고정되어야 하면 명시적인 slot-like props가 더 명확할 수 있다.

Q. slot props가 많아지면 어떻게 해?
A. Component 책임이 커졌을 수 있다. children 구조나 compound pattern을 검토한다.

Q. Card에 header, body, footer props를 모두 넣는 게 좋아?
A. 단순 Card라면 children으로 조합하는 편이 더 유연할 수 있다.

Q. slot-like props는 몇 개까지 괜찮아?
A. 정해진 숫자는 없지만 3개 이상이면 Component 책임과 API 복잡도를 재검토하는 것이 좋다.

Q. Compound Component는 언제 써?
A. Tabs나 Accordion처럼 여러 하위 Component가 함께 동작하는 UI에서 유용하다.

Q. 모든 Component를 Compound 방식으로 만들면 좋아?
A. 아니다. 구현 복잡도가 높아질 수 있으므로 조합 자유도가 필요한 UI에만 적용한다.

Q. Compound Component는 Foundation 문서에서 깊게 다뤄?
A. 아니다. 기초 개념과 사용 기준만 다루고 고급 패턴은 Advanced React Pattern 문서가 적합하다.

Q. Button도 Compound Component로 만들 수 있어?
A. 가능은 하지만 일반 Button은 variant, size, loading Props로 충분해 Compound Component가 과할 수 있다.

Q. Tabs는 왜 Compound Component가 적합해?
A. List, Trigger, Content가 함께 동작하고 selected value와 접근성 role 관계를 공유하기 때문이다.

Q. Compound Component가 너무 복잡하면 어떻게 해?
A. 단순 Props 기반 Component나 Feature 전용 Component로 범위를 줄이는 것이 좋다.

Q. Feature UI에서 Common UI를 사용하는 방식이 좋아?
A. 좋다. Common UI는 기본 구조를 제공하고 Feature UI는 도메인 데이터를 조합하는 방식이 유지보수에 좋다.

Q. Common Button에 reviewId를 넘기면 안 돼?
A. 권장하지 않는다. reviewId는 ReviewDeleteButton 같은 Feature Component에서 처리해야 한다.

Q. API 호출은 Feature UI에서 해도 돼?
A. 가능하지만 복잡한 API 로직은 Custom Hook이나 Page Component로 분리하는 것이 좋다.

Q. LoadingState, ErrorState, EmptyState는 어디에서 조합해?
A. 보통 Page나 Feature Container에서 데이터 상태를 판단한 뒤 조합한다.

Q. EmptyState action은 왜 ReactNode로 받아?
A. 버튼, 링크, 필터 초기화 등 다양한 다음 행동을 유연하게 넣기 위해서다.

Q. ErrorState에 서버 에러 원문을 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자 친화 메시지로 변환하는 것이 안전하다.

Q. Button 안에 margin을 넣어도 돼?
A. 공통 Button에는 margin을 넣지 않는 것이 좋다. 버튼 간 간격은 부모 Layout이나 ButtonGroup이 담당하는 편이 유연하다.

Q. Card가 grid 배치까지 담당해야 해?
A. 보통 Card는 자체 모양만 담당하고 grid 배치는 부모 List나 Layout Component가 담당한다.

Q. Layout Component는 왜 필요해?
A. UI Component 자체 스타일과 화면 배치 책임을 분리해 재사용성과 유지보수성을 높이기 위해 필요하다.

Q. 공통 Component에 className을 열어줘야 해?
A. 프로젝트 기준에 따라 다르지만 외부 확장이 필요한 경우 className을 허용하면 유연하다.

Q. style prop을 많이 쓰면 안 돼?
A. 동적 스타일에는 사용할 수 있지만 일관성 있는 UI를 위해 variant, size, className 기준을 우선하는 것이 좋다.

Q. Feature 전용 스타일은 어디에 둬?
A. Feature Component className이나 Feature 스타일 파일에서 처리하는 것이 좋다.

Q. Props Explosion을 Composition으로 어떻게 줄여?
A. 세부 예외 Props 대신 children이나 action 같은 ReactNode slot을 사용해 외부에서 조합하게 만든다.

Q. action props 하나로 여러 버튼을 처리해도 돼?
A. 가능하다. action을 ReactNode로 받으면 버튼, 링크, 여러 액션을 유연하게 넣을 수 있다.

Q. 중복 코드를 없애려고 공통 Component를 만들었는데 더 복잡해졌어?
A. Over Abstraction일 수 있다. 반복 제거보다 역할 명확성과 사용 편의성이 중요하다.

Q. Compound Component를 쓰면 무조건 좋은 구조야?
A. 아니다. 단순 UI에는 과할 수 있고 접근성 및 상태 공유 구현이 복잡해질 수 있다.

Q. Composition이 복잡해지면 어떻게 해?
A. Feature Component로 구조를 감싸고 Common UI는 더 작고 단순하게 유지한다.

Q. Composition Pattern 검수에서 가장 중요한 것은 뭐야?
A. Common UI가 단순하게 유지되고 Feature UI에서 필요한 도메인 UI를 조합하는지 확인하는 것이다.

Q. Composition이 잘못되었다는 신호는 뭐야?
A. slot props가 많고, children 구조를 강제하며, Common UI가 도메인 데이터를 알기 시작하면 문제가 있을 수 있다.

Q. Review Agent는 Composition을 어떻게 검토해야 해?
A. children, slot-like props, Feature 조합, Layout 책임, Compound 적용 필요성, 접근성을 순서대로 확인해야 한다.
