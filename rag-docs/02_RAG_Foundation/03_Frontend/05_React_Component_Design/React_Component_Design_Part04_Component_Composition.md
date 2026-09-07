# React Component Design Part04 - Component Composition

---

# 1. Component Composition

## 1.1 Component Composition Definition

### [개념]

Component Composition은 작은 React Component를 조합해서 더 큰 UI와 화면을 구성하는 설계 방식이다.

React에서는 상속보다 Composition을 우선한다.

Component Composition은 Page Component, Feature Component, UI Component를 책임 기준으로 나누고, Props, children, slot-like props, callback props를 통해 조합하는 구조를 만든다.

---

### [핵심]

- Component Composition은 작은 Component를 조합해 큰 화면을 만드는 방식이다.
- React Component 설계는 inheritance보다 composition을 우선한다.
- Page Component는 Feature Component를 조합한다.
- Feature Component는 UI Component를 조합한다.
- UI Component는 children과 props로 유연하게 조합될 수 있다.
- Composition은 Component Responsibility와 Component Boundary를 유지하는 핵심 방식이다.
- Composition이 좋으면 Props Contract가 명확해진다.
- Composition이 좋으면 재사용성과 유지보수성이 높아진다.
- Composition이 나쁘면 Props Drilling과 Overgrown Component가 발생한다.

---

### [실무]

2026 실무 기준에서 React 화면은 하나의 큰 Component로 작성하지 않고 의미 있는 Component Tree로 조합한다.

기본 Composition 구조:

```text
Page
→ Feature Section
→ List
→ Card
→ Button / Badge / Image
```

예:

```tsx
function FestivalPage() {
  return (
    <PageLayout>
      <FestivalSearchSection />
      <FestivalRecommendationSection />
      <FestivalListSection />
    </PageLayout>
  );
}
```

책임 기준:

```text
PageLayout
- 공통 화면 구조

FestivalPage
- 화면 조립

FestivalSearchSection
- 축제 검색 기능

FestivalRecommendationSection
- 추천 축제 영역

FestivalListSection
- 목록 영역

FestivalCard
- 단일 축제 표시

Button / Badge
- 범용 UI 표시
```

Composition 설계 Flow:

```text
Screen Requirement
→ Identify Page
→ Identify Feature Sections
→ Identify Repeated UI
→ Identify Shared UI Components
→ Compose Components
→ Define Props Contract
→ Review State Ownership
```

---

### [FAQ]

Q. Component Composition이 뭐야?
A. 작은 Component를 조합해 큰 UI와 화면을 만드는 React 설계 방식이다.

Q. React에서 상속보다 Composition을 쓰는 이유는?
A. Component 조합 방식이 UI 재사용, 변경, 확장에 더 유연하기 때문이다.

Q. Composition은 Component 분리와 뭐가 달라?
A. Component 분리는 경계를 나누는 작업이고 Composition은 나눈 Component를 다시 조합해 화면을 만드는 작업이다.

Q. 좋은 Composition의 기준은 뭐야?
A. Page, Feature, UI Component 책임이 명확하고 Props 흐름이 단순하며 재사용 가능한 UI가 잘 분리된 구조다.

---

## 1.2 Composition Design Principles

### [개념]

Composition Design Principles는 React Component를 조합할 때 지켜야 하는 설계 원칙이다.

Composition은 단순히 Component를 많이 중첩하는 것이 아니라, 책임과 데이터 흐름이 명확한 Component Tree를 만드는 것이다.

---

### [핵심]

Composition 원칙:

- 큰 화면을 의미 있는 영역으로 나눈다.
- Page Component는 화면 조립에 집중한다.
- Feature Component는 도메인 기능을 담당한다.
- UI Component는 도메인 의존성을 줄인다.
- 공통 Wrapper는 children을 활용한다.
- 특정 영역 커스터마이징은 slot-like props를 활용한다.
- 데이터 흐름은 위에서 아래로 전달한다.
- 이벤트는 callback props로 아래에서 위로 전달한다.
- Props만 전달하는 중간 Component가 많아지면 구조를 재검토한다.
- 과도한 Composition은 Over-Splitting이 될 수 있다.

---

### [실무]

Composition 판단 기준:

```text
Is this a meaningful UI section?
→ Create Feature Component

Is this repeated UI?
→ Create Reusable UI Component

Does this component wrap flexible content?
→ Use children

Does this component expose specific areas?
→ Use slot-like props

Does this component only pass props?
→ Review Component Boundary
```

좋은 Composition 예:

```tsx
function FestivalDetailPage() {
  return (
    <PageLayout>
      <FestivalHeroSection />
      <FestivalInfoSection />
      <FestivalMapSection />
      <ReviewSection />
    </PageLayout>
  );
}
```

나쁜 Composition 예:

```tsx
function FestivalDetailPage() {
  return (
    <div>
      {/* Header markup */}
      {/* Hero markup */}
      {/* Info markup */}
      {/* Map markup */}
      {/* Review form markup */}
      {/* Review list markup */}
      {/* Footer markup */}
    </div>
  );
}
```

문제:

- 화면 영역 책임이 불명확하다.
- 특정 UI 영역을 독립적으로 수정하기 어렵다.
- 테스트 단위가 불명확하다.
- ReviewSection, MapSection 같은 Feature Component 추출이 어렵다.

---

### [FAQ]

Q. Component를 조합할 때 가장 중요한 기준은 뭐야?
A. 책임이 명확한 Component Tree를 만드는 것이다.

Q. Component 중첩이 많으면 무조건 나빠?
A. 아니다. 의미 있는 계층이면 괜찮다. 하지만 Props만 전달하는 계층이 많으면 구조를 재검토해야 한다.

Q. Composition이 잘못되면 어떤 문제가 생겨?
A. Props Drilling, Overgrown Component, Over-Splitting, 불명확한 Component 책임이 생길 수 있다.

Q. Page Component는 Composition에서 어떤 역할이야?
A. Page Component는 화면의 주요 Feature Component를 조합하는 역할을 한다.

---

# 2. Children Composition

## 2.1 Children Props Definition

### [개념]

Children Composition은 Component 내부 내용을 외부에서 전달해 유연하게 조합하는 React 패턴이다.

`children`은 Layout, Card, Modal, Section, Button 같은 Wrapper Component에서 자주 사용한다.

children을 사용하면 Component가 내부 콘텐츠를 직접 알지 않아도 외부에서 다양한 UI를 넣을 수 있다.

---

### [핵심]

children 적합 대상:

- Layout
- PageContainer
- Card
- Modal
- Panel
- Section
- Button
- FormGroup
- Wrapper Component

children 원칙:

- 내부 내용이 유동적이면 children을 사용한다.
- Wrapper 구조는 Component가 담당한다.
- 본문 내용은 사용하는 쪽에서 조합한다.
- TypeScript에서는 일반적으로 ReactNode를 사용한다.
- children 구조가 너무 암묵적이면 explicit props 또는 slot-like props를 검토한다.
- 접근성 구조가 깨지지 않도록 Wrapper가 semantic element를 제공한다.

---

### [실무]

Card children 예:

```tsx
import type { ReactNode } from "react";

type CardProps = {
  title?: string;
  children: ReactNode;
};

function Card({ title, children }: CardProps) {
  return (
    <section className="card">
      {title && <h2>{title}</h2>}
      <div className="card-content">{children}</div>
    </section>
  );
}
```

사용:

```tsx
<Card title="축제 정보">
  <p>서울 봄 축제</p>
  <Button>상세 보기</Button>
</Card>
```

Layout children 예:

```tsx
type PageLayoutProps = {
  children: ReactNode;
};

function PageLayout({ children }: PageLayoutProps) {
  return (
    <div className="page-layout">
      <Header />
      <main>{children}</main>
      <Footer />
    </div>
  );
}
```

사용:

```tsx
<PageLayout>
  <FestivalListPage />
</PageLayout>
```

---

### [FAQ]

Q. children이 뭐야?
A. Component 내부에 외부에서 전달한 ReactNode를 렌더링하는 Props다.

Q. children은 언제 써?
A. Component 내부 내용을 외부에서 자유롭게 조합해야 할 때 사용한다.

Q. children 타입은 뭐로 써?
A. TypeScript React에서는 일반적으로 ReactNode를 사용한다.

Q. children을 쓰면 무조건 좋은 설계야?
A. 아니다. 구조가 고정되어 있거나 필요한 데이터가 명확하면 explicit props가 더 좋을 수 있다.

---

## 2.2 Children vs Explicit Props

### [개념]

Children과 Explicit Props는 Component에 콘텐츠를 전달하는 두 가지 방식이다.

children은 자유로운 UI 조합에 적합하고, explicit props는 구조가 고정되어 있으며 데이터 의미가 명확할 때 적합하다.

---

### [핵심]

children 적합 상황:

- 본문 구성이 자유롭다.
- 내부에 여러 Component가 들어갈 수 있다.
- Wrapper Component다.
- Layout이나 Card처럼 영역만 제공한다.
- Button처럼 텍스트와 아이콘 조합이 가능하다.

explicit props 적합 상황:

- 구조가 고정되어 있다.
- 필요한 데이터가 명확하다.
- Component가 특정 표시 책임을 가진다.
- 접근성 속성을 Component가 직접 구성해야 한다.
- 데이터 기반 UI가 중요하다.

---

### [실무]

children 방식:

```tsx
function Card({ children }: { children: ReactNode }) {
  return <section className="card">{children}</section>;
}
```

사용:

```tsx
<Card>
  <h2>축제 정보</h2>
  <p>축제 설명</p>
</Card>
```

explicit props 방식:

```tsx
type FestivalSummaryCardProps = {
  title: string;
  description: string;
  imageUrl: string | null;
};

function FestivalSummaryCard({
  title,
  description,
  imageUrl,
}: FestivalSummaryCardProps) {
  return (
    <article>
      {imageUrl && <img src={imageUrl} alt={title} />}
      <h2>{title}</h2>
      <p>{description}</p>
    </article>
  );
}
```

비교:

| 기준 | children                  | explicit props                |
| ---- | ------------------------- | ----------------------------- |
| 구조 | 자유로움                  | 고정적                        |
| 장점 | 조합성 높음               | 의미 명확                     |
| 단점 | 사용법이 암묵적일 수 있음 | 유연성 낮음                   |
| 적합 | Layout, Card, Modal       | Domain Card, Profile, Summary |
| 타입 | ReactNode                 | 명확한 field type             |

---

### [FAQ]

Q. children과 explicit props 차이는 뭐야?
A. children은 자유로운 내부 조합에 좋고 explicit props는 구조가 고정되고 데이터 의미가 명확할 때 좋다.

Q. Card에는 children이 좋아?
A. 공통 Card Wrapper라면 children이 좋고, 도메인 카드라면 title, imageUrl 같은 explicit props가 좋을 수 있다.

Q. explicit props가 children보다 좋은 경우는 언제야?
A. Component가 정해진 데이터 구조를 표시하고 접근성이나 레이아웃을 안정적으로 관리해야 할 때 좋다.

Q. children을 남용하면 어떤 문제가 있어?
A. Component 사용법이 암묵적이 되고 내부 구조 일관성이 떨어질 수 있다.

---

## 2.3 Children Composition Caution

### [개념]

Children Composition Caution은 children을 사용할 때 구조가 지나치게 암묵적이거나 접근성 구조가 깨지는 문제를 방지하는 규칙이다.

children은 유연하지만 Component Contract를 약하게 만들 수 있다.

---

### [핵심]

주의 사항:

- children 내부 구조가 너무 자유로우면 사용법이 불명확해진다.
- children에 무엇을 넣어야 하는지 문서화가 필요할 수 있다.
- 접근성 구조를 children 사용자에게 모두 맡기면 위험하다.
- children이 너무 많은 책임을 가지면 slot-like props를 검토한다.
- title, actions, footer처럼 의미 있는 영역은 명시적 props가 더 좋을 수 있다.
- children과 explicit props가 충돌하지 않도록 역할을 구분한다.

---

### [실무]

나쁜 예:

```tsx
function Modal({ children }: { children: ReactNode }) {
  return <div>{children}</div>;
}
```

문제:

```text
role="dialog"가 없다.
aria-modal이 없다.
title 구조가 보장되지 않는다.
닫기 버튼 위치가 일관되지 않는다.
Modal 접근성 책임이 사용자에게 넘어간다.
```

개선:

```tsx
type ModalProps = {
  title: string;
  isOpen: boolean;
  onClose: () => void;
  children: ReactNode;
};

function Modal({ title, isOpen, onClose, children }: ModalProps) {
  if (!isOpen) {
    return null;
  }

  return (
    <section role="dialog" aria-modal="true" aria-labelledby="modal-title">
      <header>
        <h2 id="modal-title">{title}</h2>
        <button type="button" onClick={onClose}>
          닫기
        </button>
      </header>
      <div>{children}</div>
    </section>
  );
}
```

판단:

```text
Modal title, role, close button은 Modal 책임이다.
본문 내용만 children으로 받는다.
```

---

### [FAQ]

Q. children을 쓸 때 주의할 점은 뭐야?
A. 내부 구조가 너무 암묵적이지 않게 하고 접근성 구조를 Component가 책임질 수 있게 설계해야 한다.

Q. Modal을 children만으로 만들면 안 돼?
A. 가능은 하지만 title, role, aria-modal, close button 같은 핵심 구조는 Modal Component가 책임지는 것이 좋다.

Q. children에 무엇이 들어가는지 어떻게 알게 해?
A. Component 이름, Props Type, 문서, 예제, slot-like props를 통해 사용 의도를 명확히 한다.

Q. children이 너무 복잡하면 어떻게 해?
A. header, footer, actions 같은 slot-like props 또는 하위 Component 분리를 검토한다.

---

# 3. Slot-like Props

## 3.1 Slot-like Props Definition

### [개념]

Slot-like Props는 `header`, `footer`, `actions`, `aside`처럼 특정 영역에 ReactNode를 전달해 Component를 조합하는 방식이다.

Slot-like Props는 children보다 구조가 명확하고, Compound Component보다 단순한 Composition 방식이다.

---

### [핵심]

Slot-like Props 적합 대상:

- Modal Header
- Modal Footer
- Card Actions
- Panel Toolbar
- Page Header Actions
- List Empty View
- Table Action Area
- Layout Aside
- Form Footer
- Section Header

Slot-like Props 원칙:

- 특정 영역만 외부에서 커스터마이징할 때 사용한다.
- ReactNode Props 이름을 명확히 한다.
- children은 본문 영역으로 유지한다.
- header, footer, actions는 특정 영역을 담당한다.
- slot props가 너무 많아지면 Component 책임을 재검토한다.
- 접근성 구조를 Component 내부에서 유지한다.

---

### [실무]

Panel 예:

```tsx
type PanelProps = {
  title: string;
  actions?: React.ReactNode;
  children: React.ReactNode;
};

function Panel({ title, actions, children }: PanelProps) {
  return (
    <section className="panel">
      <header className="panel-header">
        <h2>{title}</h2>
        {actions && <div className="panel-actions">{actions}</div>}
      </header>
      <div className="panel-content">{children}</div>
    </section>
  );
}
```

사용:

```tsx
<Panel
  title="축제 목록"
  actions={<Button onClick={handleRefresh}>새로고침</Button>}
>
  <FestivalList festivals={festivals} />
</Panel>
```

Modal 예:

```tsx
type ModalProps = {
  title: string;
  footer?: React.ReactNode;
  children: React.ReactNode;
};

function Modal({ title, footer, children }: ModalProps) {
  return (
    <section role="dialog" aria-modal="true">
      <header>
        <h2>{title}</h2>
      </header>
      <div>{children}</div>
      {footer && <footer>{footer}</footer>}
    </section>
  );
}
```

---

### [FAQ]

Q. Slot-like Props가 뭐야?
A. header, footer, actions처럼 특정 영역에 ReactNode를 전달해 Component를 조합하는 방식이다.

Q. Slot-like Props는 언제 써?
A. Card, Modal, Panel처럼 특정 영역만 외부에서 커스터마이징하고 싶을 때 사용한다.

Q. children과 Slot-like Props 차이는?
A. children은 전체 본문을 전달하고 Slot-like Props는 header, action, footer 같은 특정 영역을 전달한다.

Q. Slot-like Props는 Compound Component와 같아?
A. 아니다. Slot-like Props는 ReactNode props를 전달하는 단순 방식이고 Compound Component는 하위 Component 조합 규칙을 더 강하게 가진다.

---

## 3.2 Slot-like Props Design Rules

### [개념]

Slot-like Props Design Rules는 ReactNode 영역 Props를 안정적으로 설계하기 위한 규칙이다.

Slot-like Props는 자유도와 명확성 사이의 균형을 제공한다.

---

### [핵심]

설계 규칙:

- 본문은 `children`으로 받는다.
- 상단 영역은 `header`, `title`, `actions`로 구분한다.
- 하단 영역은 `footer` 또는 `actions`로 구분한다.
- ReactNode Props 이름은 영역을 명확히 표현한다.
- slot props가 3개 이상이면 Component 책임을 검토한다.
- slot props에 비즈니스 로직을 강제하지 않는다.
- 접근성에 필요한 구조는 Component 내부에서 보장한다.
- 단순 텍스트는 ReactNode보다 string props가 나을 수 있다.
- 반복되는 slot 구조는 별도 Component로 분리할 수 있다.

---

### [실무]

좋은 예:

```tsx
type PageHeaderProps = {
  title: string;
  description?: string;
  actions?: React.ReactNode;
};

function PageHeader({ title, description, actions }: PageHeaderProps) {
  return (
    <header className="page-header">
      <div>
        <h1>{title}</h1>
        {description && <p>{description}</p>}
      </div>
      {actions && <div className="page-header-actions">{actions}</div>}
    </header>
  );
}
```

나쁜 예:

```tsx
type BoxProps = {
  top?: React.ReactNode;
  left?: React.ReactNode;
  right?: React.ReactNode;
  bottom?: React.ReactNode;
  content?: React.ReactNode;
  extra?: React.ReactNode;
};
```

문제:

```text
slot 이름이 의미 기반이 아니다.
Box 책임이 불명확하다.
사용자가 어떤 영역에 무엇을 넣어야 하는지 알기 어렵다.
```

개선 방향:

```text
Box
→ Panel
→ PageHeader
→ Card
→ Modal
처럼 목적이 명확한 Component로 분리
```

---

### [FAQ]

Q. Slot-like Props 이름은 어떻게 지어?
A. header, footer, actions, aside처럼 영역과 의미가 명확한 이름을 사용한다.

Q. actions는 언제 써?
A. 버튼, 링크, 메뉴처럼 사용자가 수행할 수 있는 동작 영역을 전달할 때 사용한다.

Q. title도 ReactNode로 받아야 해?
A. 단순 텍스트라면 string이 더 명확하다. 아이콘이나 강조가 필요하면 ReactNode를 검토한다.

Q. slot props가 많으면 왜 문제야?
A. Component가 너무 많은 영역과 변형을 담당해 책임이 불명확해질 수 있다.

---

# 4. Layout Composition

## 4.1 Layout Component Composition

### [개념]

Layout Component Composition은 공통 화면 구조를 children과 Outlet 영역으로 조합하는 방식이다.

Layout Component는 Header, Footer, Sidebar, Main 영역 같은 공통 구조를 담당하고 도메인 로직은 최소화한다.

---

### [핵심]

Layout Component 역할:

- 공통 페이지 구조 제공
- Header / Footer / Sidebar 배치
- main 영역 제공
- children 렌더링
- Router Outlet 연결 가능
- 공통 여백 / 폭 / 영역 관리
- semantic landmark 제공
- 도메인 로직 최소화

Layout Component 예:

- AppLayout
- PageLayout
- DashboardLayout
- AuthLayout
- PageContainer
- SectionLayout

---

### [실무]

PageLayout 예:

```tsx
type PageLayoutProps = {
  children: React.ReactNode;
};

function PageLayout({ children }: PageLayoutProps) {
  return (
    <div className="page-layout">
      <Header />
      <main className="page-main">{children}</main>
      <Footer />
    </div>
  );
}
```

DashboardLayout 예:

```tsx
function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="dashboard-layout">
      <Sidebar />
      <main>{children}</main>
    </div>
  );
}
```

권장:

```text
Layout Component
→ 공통 구조 책임
→ children 렌더링
→ semantic tag 사용
→ 도메인 데이터 요청 없음
```

금지:

```text
Layout Component 내부에서 특정 축제 목록 API 호출
Layout Component가 특정 Page 검색 조건 관리
Layout Component가 특정 Feature Modal 상태 관리
```

---

### [FAQ]

Q. Layout Component는 뭐야?
A. Header, Footer, Sidebar, main 영역 같은 공통 화면 구조를 담당하는 Component다.

Q. Layout Component는 children을 써?
A. 일반적으로 children을 사용해 페이지별 내용을 main 영역에 렌더링한다.

Q. Layout Component에 API 호출이 있어도 돼?
A. 공통 사용자 정보처럼 앱 전체에 필요한 경우는 가능하지만 특정 Page 도메인 API는 넣지 않는 것이 좋다.

Q. Layout Component의 핵심 책임은 뭐야?
A. 공통 구조와 배치를 제공하고 페이지별 내용은 children으로 받는 것이다.

---

## 4.2 Page Composition Rules

### [개념]

Page Composition은 하나의 화면을 여러 Feature Section과 UI Component로 조합하는 방식이다.

Page Component는 화면 전체를 대표하며, 세부 기능을 Feature Component로 나누어 조립한다.

---

### [핵심]

Page Composition 원칙:

- Page는 화면 조립자 역할을 한다.
- Page는 주요 State와 데이터 흐름을 소유할 수 있다.
- Page는 Feature Component를 배치한다.
- Page는 공통 Layout과 연결될 수 있다.
- 세부 UI Markup을 Page에 몰아넣지 않는다.
- API 상태 로직이 길면 Custom Hook으로 분리한다.
- Page 내부 조건부 렌더링은 Loading / Error / Empty View로 분리할 수 있다.

---

### [실무]

FestivalSearchPage 예:

```tsx
function FestivalSearchPage() {
  const { festivals, loading, error } = useFestivalSearch();

  return (
    <PageLayout>
      <PageHeader
        title="축제 검색"
        description="지역과 테마로 축제를 찾아보세요."
      />
      <FestivalSearchSection />
      <FestivalFilterSection />
      <FestivalResultSection
        festivals={festivals}
        loading={loading}
        error={error}
      />
    </PageLayout>
  );
}
```

Page Composition 구조:

```text
FestivalSearchPage
→ PageLayout
→ PageHeader
→ FestivalSearchSection
→ FestivalFilterSection
→ FestivalResultSection
  → FestivalList
  → FestivalCard
```

주의:

```text
Page가 모든 markup을 직접 렌더링한다
→ Feature Component 분리 검토

Page가 모든 API 로직을 직접 가진다
→ Custom Hook 분리 검토

Page가 모든 UI State를 소유한다
→ Feature State로 내릴 수 있는지 검토
```

---

### [FAQ]

Q. Page Composition이 뭐야?
A. 하나의 화면을 여러 Feature Section과 UI Component로 조합하는 방식이다.

Q. Page Component는 어떤 역할을 해야 해?
A. 화면 조립, 주요 State 관리, 데이터 흐름 연결을 담당하고 세부 UI는 하위 Component로 분리한다.

Q. Page에 모든 JSX를 넣으면 왜 안 좋아?
A. Page가 Overgrown Component가 되어 책임이 불명확하고 유지보수가 어려워진다.

Q. Page에서 API Hook을 호출해도 돼?
A. 가능하다. Page는 화면 단위 데이터 흐름의 시작점이 될 수 있다.

---

# 5. Feature Composition

## 5.1 Feature Component Composition

### [개념]

Feature Component Composition은 특정 도메인 기능을 여러 하위 UI Component와 Local State로 구성하는 방식이다.

Feature Component는 Page보다 작고 UI Component보다 도메인 의존성이 높다.

---

### [핵심]

Feature Component 역할:

- 특정 기능 UI 구성
- 도메인 데이터 표시
- Local State 소유 가능
- 하위 UI Component 조합
- Callback Props로 결과 전달
- Feature 내부 이벤트 처리
- 필요 시 Custom Hook 사용

Feature Composition 예:

- FestivalSearchSection
- FestivalFilterPanel
- ReviewSection
- NotificationList
- ChatRoomPanel
- LoginForm
- UserProfileEditor

---

### [실무]

ReviewSection 예:

```tsx
function ReviewSection({ reviews, onSubmitReview }: ReviewSectionProps) {
  return (
    <section>
      <SectionHeader title="리뷰" />
      <ReviewForm onSubmit={onSubmitReview} />
      <ReviewList reviews={reviews} />
    </section>
  );
}
```

하위 구조:

```text
ReviewSection
→ SectionHeader
→ ReviewForm
  → RatingInput
  → Textarea
  → Button
→ ReviewList
  → ReviewItem
```

책임:

```text
ReviewSection
- 리뷰 영역 조립

ReviewForm
- 리뷰 작성 Form

ReviewList
- 리뷰 목록 표시

ReviewItem
- 리뷰 단일 항목 표시
```

---

### [FAQ]

Q. Feature Composition이 뭐야?
A. 특정 도메인 기능을 여러 하위 UI Component와 Local State로 구성하는 방식이다.

Q. Feature Component는 UI Component를 조합해도 돼?
A. 가능하다. Button, Input, Card 같은 공통 UI Component를 조합해 도메인 기능을 만든다.

Q. Feature Component는 State를 가져도 돼?
A. 가능하다. 해당 기능 내부에서만 필요한 State는 Feature Component가 소유할 수 있다.

Q. Feature Component가 커지면 어떻게 해?
A. Form, List, Item, Panel 같은 하위 Component로 다시 분리한다.

---

## 5.2 Feature Boundary in Composition

### [개념]

Feature Boundary in Composition은 기능 단위 Component가 어디까지 책임질지 결정하는 기준이다.

Feature Boundary가 명확해야 Page, Feature, UI Component 역할이 섞이지 않는다.

---

### [핵심]

Feature Boundary 기준:

- 도메인 기능 단위
- 독립적인 UI 영역
- 독립적인 Local State
- 독립적인 이벤트 흐름
- 반복 가능한 기능 패턴
- Page State와의 연결 지점
- UI Component 조합 범위

Feature Boundary 주의:

- Feature가 Page 전체 책임을 가져서는 안 된다.
- Feature가 공통 UI Component처럼 너무 범용화되면 안 된다.
- Feature 내부에 너무 많은 하위 기능이 섞이면 분리한다.
- API Logic이 복잡하면 Custom Hook으로 분리한다.

---

### [실무]

좋은 Feature Boundary:

```text
FestivalSearchSection
- 검색어 입력
- 검색 이벤트 전달

FestivalFilterPanel
- 지역 / 테마 / 기간 필터 선택
- 필터 변경 이벤트 전달

FestivalResultSection
- 검색 결과 상태 표시
- 목록 / Empty / Error 표시
```

나쁜 Feature Boundary:

```text
FestivalEverythingSection
- 검색
- 필터
- 목록
- 상세
- 리뷰
- 지도
- 모달
```

문제:

```text
Feature Component가 너무 많은 책임을 가진다.
Page와 Feature 경계가 흐려진다.
하위 Component 재사용이 어렵다.
```

---

### [FAQ]

Q. Feature Boundary는 어떻게 잡아?
A. 도메인 기능 단위, 독립 UI 영역, Local State, 이벤트 흐름을 기준으로 잡는다.

Q. Feature Component가 너무 커지면 어떻게 해?
A. SearchForm, FilterPanel, List, Item, Modal 같은 하위 Component로 분리한다.

Q. Feature Component와 Page Component 경계는 뭐야?
A. Page는 화면 전체 조립과 주요 흐름을 담당하고 Feature는 특정 기능 영역을 담당한다.

Q. Feature Component와 UI Component 경계는 뭐야?
A. Feature는 도메인 기능에 의존하고 UI Component는 도메인과 무관한 표시와 상호작용을 담당한다.

---

# 6. Reusable UI Composition

## 6.1 Reusable UI Composition Rules

### [개념]

Reusable UI Composition은 Button, Input, Card, Modal, Badge 같은 공통 UI Component를 조합해 여러 Feature에서 재사용하는 방식이다.

Reusable UI Component는 도메인 의존성을 줄이고 Props, children, variant, slot-like props로 동작과 표시를 제어한다.

---

### [핵심]

Reusable UI Component 후보:

- Button
- Input
- Select
- Checkbox
- Modal
- Card
- Badge
- Spinner
- EmptyState
- ErrorMessage
- Pagination
- PageHeader
- SectionHeader

Reusable UI Composition 원칙:

- 도메인 로직을 넣지 않는다.
- API 호출을 하지 않는다.
- Props 기반으로 표시한다.
- Callback Props로 이벤트를 알린다.
- children을 지원할 수 있다.
- variant로 시각적 변형을 제한한다.
- 접근성 기본 구조를 포함한다.
- className 확장을 고려한다.

---

### [실무]

Reusable Button 예:

```tsx
type ButtonProps = {
  type?: "button" | "submit" | "reset";
  variant?: "primary" | "secondary" | "danger";
  disabled?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
};

function Button({
  type = "button",
  variant = "primary",
  disabled = false,
  children,
  onClick,
}: ButtonProps) {
  return (
    <button
      type={type}
      className={`button button-${variant}`}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
```

Feature에서 조합:

```tsx
function FestivalSearchForm({ onSearch }: FestivalSearchFormProps) {
  return (
    <form onSubmit={handleSubmit}>
      <Input value={keyword} onValueChange={setKeyword} />
      <Button type="submit" variant="primary">
        검색
      </Button>
    </form>
  );
}
```

주의:

```text
Button이 Festival API를 호출한다
→ 잘못된 UI Component 책임

Input이 전역 검색 상태를 직접 변경한다
→ 재사용성 저하

Card가 특정 도메인 Response를 강제한다
→ 공통 Card보다 Feature Card로 분리
```

---

### [FAQ]

Q. Reusable UI Composition이 뭐야?
A. 공통 UI Component를 조합해 여러 Feature에서 재사용하는 방식이다.

Q. Reusable UI Component는 API 호출을 해도 돼?
A. 권장하지 않는다. UI Component는 표시와 상호작용만 담당해야 한다.

Q. Button이나 Card는 children을 받아도 돼?
A. 가능하다. 내부 내용을 유연하게 조합해야 하는 경우 children이 적합하다.

Q. Reusable UI Component에 도메인 데이터를 넣어도 돼?
A. 권장하지 않는다. 도메인 데이터는 Feature Component에서 가공해 필요한 값만 전달하는 것이 좋다.

---

## 6.2 Domain Component vs Reusable UI Component

### [개념]

Domain Component는 특정 도메인 기능이나 데이터를 표시하는 Component다.

Reusable UI Component는 도메인과 무관하게 여러 화면에서 재사용 가능한 Component다.

Composition 설계에서는 Domain Component와 Reusable UI Component를 구분해야 한다.

---

### [핵심]

Domain Component 예:

- FestivalCard
- ReviewForm
- ChatMessageItem
- NotificationItem
- UserProfileSummary
- DonationHistoryItem

Reusable UI Component 예:

- Button
- Card
- Modal
- Badge
- Input
- EmptyState
- Spinner

구분 기준:

- 도메인 데이터에 의존하면 Domain Component
- 범용 표시와 상호작용이면 Reusable UI Component
- API Response 구조를 알면 Domain Component
- variant, children 중심이면 UI Component
- Feature 폴더에 있으면 Domain Component 가능성 높음
- shared components에 있으면 UI Component 가능성 높음

---

### [실무]

Domain Component 예:

```tsx
type FestivalCardProps = {
  festival: FestivalSummary;
  onSelect: (festivalId: number) => void;
};

function FestivalCard({ festival, onSelect }: FestivalCardProps) {
  return (
    <Card>
      <h2>{festival.title}</h2>
      <Badge label={festival.regionName} />
      <Button onClick={() => onSelect(festival.festivalId)}>상세 보기</Button>
    </Card>
  );
}
```

구조:

```text
FestivalCard
→ Domain Component
→ festival 도메인 데이터 사용

Card / Badge / Button
→ Reusable UI Component
→ 도메인 모름
```

비교:

| 기준        | Domain Component | Reusable UI Component    |
| ----------- | ---------------- | ------------------------ |
| 의존성      | 도메인 의존      | 도메인 독립              |
| 위치        | features         | components               |
| 예          | FestivalCard     | Card                     |
| Props       | festival, review | title, children, variant |
| API 지식    | 가질 수 있음     | 없어야 함                |
| 재사용 범위 | 도메인 내부      | 앱 전체                  |

---

### [FAQ]

Q. Domain Component와 Reusable UI Component 차이는 뭐야?
A. Domain Component는 특정 도메인 데이터와 기능에 의존하고 Reusable UI Component는 도메인과 무관하게 재사용된다.

Q. FestivalCard는 UI Component야?
A. 축제 도메인 데이터를 직접 사용하면 Domain Component 또는 Feature Component에 가깝다.

Q. Card는 공통 UI Component야?
A. 도메인 데이터 없이 children, title, actions 같은 Props로 구성되면 공통 UI Component다.

Q. Domain Component에서 UI Component를 조합해도 돼?
A. 가능하다. 일반적인 Feature Composition 방식이다.

---

# 7. Compound Component Basics

## 7.1 Compound Component Definition

### [개념]

Compound Component는 여러 하위 Component를 조합해 하나의 UI 패턴을 구성하는 React Component Pattern이다.

예를 들어 Tabs, Accordion, Select, Dropdown 같은 UI에서 Root, List, Trigger, Content 같은 하위 Component를 함께 사용한다.

Foundation 단계에서는 Compound Component를 깊게 구현하기보다 사용 기준과 도입 판단만 다룬다.

---

### [핵심]

Compound Component 적합 대상:

- Tabs
- Accordion
- Dropdown
- Select
- Menu
- Stepper
- Modal compound variant
- Table compound structure

Compound Component 특징:

- 관련 Component들을 하나의 패턴으로 묶는다.
- children 기반 조합을 사용한다.
- 내부 상태 공유가 필요할 수 있다.
- Context와 함께 사용되는 경우가 많다.
- API가 잘 설계되지 않으면 사용법이 어려워진다.
- Foundation 단계에서는 단순 slot-like props가 더 적합할 수 있다.

---

### [실무]

Tabs 사용 형태 예:

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

도입 판단:

```text
여러 하위 Component가 강하게 연결되어 있다
→ Compound Component 검토

단순 header / footer / actions 전달이면 충분하다
→ Slot-like Props 우선

하위 Component 사용 규칙이 복잡하다
→ 문서화 필요

작은 프로젝트에서 단순 Modal만 필요하다
→ Compound Component 과할 수 있음
```

---

### [FAQ]

Q. Compound Component가 뭐야?
A. 여러 하위 Component를 조합해 하나의 UI 패턴을 구성하는 React Component Pattern이다.

Q. Compound Component는 언제 써?
A. Tabs, Accordion, Dropdown처럼 하위 Component들이 강하게 연결된 UI 패턴에 적합하다.

Q. Slot-like Props와 Compound Component 차이는?
A. Slot-like Props는 특정 영역에 ReactNode를 전달하는 단순 방식이고 Compound Component는 하위 Component 조합 규칙을 가진 패턴이다.

Q. Foundation 단계에서 Compound Component를 많이 써도 돼?
A. 권장하지 않는다. 단순한 구조는 children이나 slot-like props로 먼저 해결한다.

---

## 7.2 Compound Component Caution

### [개념]

Compound Component Caution은 Compound Component를 과도하게 사용해 Component API가 복잡해지는 문제를 방지하는 규칙이다.

Compound Component는 강력하지만 작은 UI나 단순 구조에 사용하면 Over-Abstraction이 될 수 있다.

---

### [핵심]

주의 사항:

- 단순 Component에 Compound Component를 적용하지 않는다.
- 사용 규칙이 복잡하면 문서화가 필요하다.
- 하위 Component 순서와 위치 제약을 명확히 해야 한다.
- Context 사용 시 내부 상태 흐름을 관리해야 한다.
- TypeScript 타입 설계가 복잡해질 수 있다.
- 접근성 요구사항이 큰 UI에서는 더 신중해야 한다.
- 처음부터 Design System 수준으로 추상화하지 않는다.

---

### [실무]

과도한 예:

```tsx
<Card.Root>
  <Card.Header>
    <Card.Title>축제</Card.Title>
    <Card.Action>...</Card.Action>
  </Card.Header>
  <Card.Body>
    <Card.Description>...</Card.Description>
  </Card.Body>
  <Card.Footer>
    <Card.Button>...</Card.Button>
  </Card.Footer>
</Card.Root>
```

문제 가능성:

```text
단순 Card에 비해 사용법이 복잡하다.
하위 Component가 많다.
실제 재사용 패턴이 확인되지 않았다.
```

단순 대안:

```tsx
<Card title="축제" actions={<Button>상세 보기</Button>}>
  <p>축제 설명</p>
</Card>
```

판단:

```text
반복되는 복잡한 UI 패턴
→ Compound Component 검토

단순 영역 커스터마이징
→ Slot-like Props 우선

단순 내용 조합
→ children 우선
```

---

### [FAQ]

Q. Compound Component를 많이 만들면 좋아?
A. 아니다. 실제 반복되는 복잡한 UI 패턴이 있을 때만 사용하는 것이 좋다.

Q. Card도 Compound Component로 만들어야 해?
A. 단순 Card라면 children이나 slot-like props가 더 적합하다.

Q. Compound Component의 위험은 뭐야?
A. 사용법이 복잡해지고 타입 설계와 접근성 관리가 어려워질 수 있다.

Q. Compound Component 도입 전 뭘 확인해야 해?
A. 실제 반복 패턴, 하위 Component 관계, 접근성 요구사항, 문서화 가능성을 확인해야 한다.

---

# 8. Composition and Props Flow

## 8.1 Data Down, Action Up

### [개념]

Data Down, Action Up은 React Component Composition에서 데이터는 부모에서 자식으로 내려가고, 이벤트는 자식에서 부모로 올라가는 기본 흐름이다.

Props는 데이터를 내려보내고 Callback Props는 이벤트를 부모에게 전달한다.

---

### [핵심]

Data Down:

- 부모가 State를 소유한다.
- 자식은 Props로 값을 받는다.
- UI Component는 Props 기반으로 렌더링한다.
- 데이터 흐름은 위에서 아래로 읽힌다.

Action Up:

- 자식에서 이벤트가 발생한다.
- 자식은 Callback Props를 호출한다.
- 부모가 State 변경 또는 API 호출을 결정한다.
- 자식은 부모 State를 직접 변경하지 않는다.

---

### [실무]

예:

```tsx
function FestivalPage() {
  const [selectedFestivalId, setSelectedFestivalId] = useState<number | null>(
    null,
  );

  return (
    <FestivalList
      selectedFestivalId={selectedFestivalId}
      onSelectFestival={setSelectedFestivalId}
    />
  );
}
```

하위 Component:

```tsx
function FestivalList({
  festivals,
  selectedFestivalId,
  onSelectFestival,
}: FestivalListProps) {
  return (
    <section>
      {festivals.map((festival) => (
        <FestivalCard
          key={festival.festivalId}
          festival={festival}
          isSelected={festival.festivalId === selectedFestivalId}
          onSelect={onSelectFestival}
        />
      ))}
    </section>
  );
}
```

흐름:

```text
FestivalPage State
→ FestivalList Props
→ FestivalCard Props

FestivalCard click
→ onSelect(festivalId)
→ FestivalList
→ onSelectFestival(festivalId)
→ FestivalPage State Update
```

---

### [FAQ]

Q. Data Down, Action Up이 뭐야?
A. 데이터는 부모에서 자식으로 Props로 내려가고 이벤트는 자식에서 부모로 Callback Props로 올라가는 흐름이다.

Q. 자식이 부모 State를 직접 바꿀 수 있어?
A. 직접 바꿀 수 없다. 부모가 전달한 Callback Props를 호출해 변경 요청을 전달한다.

Q. Data Down, Action Up은 왜 중요해?
A. 데이터 흐름과 이벤트 흐름이 예측 가능해져 Component 구조를 이해하기 쉬워진다.

Q. 이벤트가 여러 단계 올라가면 어떻게 해?
A. Props Drilling이 깊어지면 State Owner, Composition 구조, Context 도입을 검토한다.

---

## 8.2 Composition and Props Drilling

### [개념]

Composition과 Props Drilling은 밀접하게 연결된다.

좋은 Composition은 Props 흐름을 단순하게 만들지만, 나쁜 Composition은 중간 Component가 사용하지 않는 Props를 계속 전달하게 만든다.

---

### [핵심]

Props Drilling 발생 조건:

- Component 계층이 깊다.
- State Owner가 너무 위에 있다.
- 중간 Component가 Props를 사용하지 않는다.
- Feature Boundary가 불명확하다.
- children composition을 활용하지 않는다.
- Context가 필요한 상태를 Props로만 전달한다.

Composition 개선 방법:

- Component 계층을 단순화한다.
- State Owner를 재검토한다.
- Feature Component 경계를 재설계한다.
- children으로 하위 구조를 직접 주입한다.
- slot-like props로 특정 영역을 주입한다.
- 반복 공유 상태는 Context를 검토한다.

---

### [실무]

Props Drilling 예:

```tsx
<Page selectedId={selectedId} onSelect={setSelectedId}>
  <Section selectedId={selectedId} onSelect={setSelectedId}>
    <List selectedId={selectedId} onSelect={setSelectedId} />
  </Section>
</Page>
```

문제:

```text
Page와 Section이 selectedId를 직접 사용하지 않고 전달만 한다.
```

Composition 개선 예:

```tsx
function FestivalPage() {
  const [selectedId, setSelectedId] = useState<number | null>(null);

  return (
    <PageLayout>
      <FestivalList selectedId={selectedId} onSelect={setSelectedId} />
    </PageLayout>
  );
}
```

또는 children 활용:

```tsx
function Section({ title, children }: SectionProps) {
  return (
    <section>
      <h2>{title}</h2>
      {children}
    </section>
  );
}

function FestivalPage() {
  return (
    <Section title="축제 목록">
      <FestivalList selectedId={selectedId} onSelect={setSelectedId} />
    </Section>
  );
}
```

---

### [FAQ]

Q. Composition이 Props Drilling을 줄일 수 있어?
A. 가능하다. children이나 slot-like props를 활용하면 중간 Component가 Props 전달만 하는 구조를 줄일 수 있다.

Q. Props Drilling은 무조건 Context로 해결해야 해?
A. 아니다. State Owner와 Component Composition을 먼저 재검토한다.

Q. 중간 Component가 Props를 전달만 하면 문제야?
A. 항상 문제는 아니지만 반복되고 깊어지면 구조 개선이 필요하다.

Q. children이 Props Drilling을 줄이는 이유는?
A. 부모가 필요한 Component를 직접 조합해 중간 Wrapper가 사용하지 않는 Props를 받을 필요가 줄어들기 때문이다.

---

# 9. Composition Anti Patterns

## 9.1 Inheritance-like Component Design

### [개념]

Inheritance-like Component Design은 React에서 상속처럼 Component를 확장하려고 하거나, 하나의 Base Component에 모든 변형을 몰아넣는 Anti Pattern이다.

React에서는 Component 상속보다 Composition과 Props 기반 변형을 우선한다.

---

### [핵심]

문제:

- Base Component가 너무 많은 책임을 가진다.
- variant가 과도하게 증가한다.
- Props 조합이 복잡해진다.
- 작은 변경도 Base Component에 영향을 준다.
- 도메인별 차이를 무리하게 하나로 통합한다.
- Component 사용법이 어려워진다.

해결:

- Composition을 사용한다.
- 도메인 Component 분리를 허용한다.
- 공통 UI는 작게 유지한다.
- variant를 제한한다.
- children과 slot-like props를 활용한다.
- 실제 중복이 확인된 후 추상화한다.

---

### [실무]

나쁜 방향:

```text
BaseCard
→ FestivalCard mode
→ ReviewCard mode
→ UserCard mode
→ NotificationCard mode
→ DonationCard mode
```

문제:

```text
BaseCard가 모든 도메인 요구사항을 알게 된다.
Props가 계속 증가한다.
도메인별 수정이 공통 Component에 영향을 준다.
```

좋은 방향:

```text
Card
- 공통 wrapper

FestivalCard
- 축제 도메인 카드

ReviewCard
- 리뷰 도메인 카드

NotificationCard
- 알림 도메인 카드
```

구조:

```tsx
function FestivalCard({ festival }: FestivalCardProps) {
  return (
    <Card>
      <h2>{festival.title}</h2>
      <p>{festival.regionName}</p>
    </Card>
  );
}
```

---

### [FAQ]

Q. React에서 상속으로 Component를 확장하면 안 돼?
A. React에서는 상속보다 Composition을 우선한다. Component 조합과 Props 기반 설계가 더 유연하다.

Q. BaseCard에 모든 변형을 넣으면 편하지 않아?
A. 초기에는 편하지만 Props가 늘어나고 도메인 결합이 커져 유지보수가 어려워진다.

Q. 공통 Card와 FestivalCard는 어떻게 나눠?
A. Card는 공통 wrapper 역할을 하고 FestivalCard는 축제 도메인 데이터를 표시한다.

Q. 도메인별 Card를 따로 만들면 중복 아니야?
A. 일부 중복은 허용할 수 있다. 무리한 통합보다 명확한 책임 분리가 더 좋을 수 있다.

---

## 9.2 Wrapper Hell Problem

### [개념]

Wrapper Hell은 의미 없는 Wrapper Component가 과도하게 중첩되어 Component Tree가 복잡해지는 문제다.

Wrapper Hell은 Composition을 잘못 사용했을 때 발생하는 Over-Splitting Anti Pattern이다.

---

### [핵심]

문제:

- 의미 없는 Component 계층이 많다.
- Props 전달만 하는 Component가 증가한다.
- 실제 책임이 없는 Wrapper가 생긴다.
- DOM 구조가 불필요하게 깊어진다.
- 스타일 충돌 가능성이 커진다.
- 디버깅과 테스트가 어려워진다.

원인:

- 모든 div를 Component로 분리
- 책임 없는 Layout Component 남발
- 과도한 재사용성 예측
- 추상화 기준 부재
- children Wrapper 과다

---

### [실무]

나쁜 예:

```tsx
<AppWrapper>
  <PageWrapper>
    <ContentWrapper>
      <SectionWrapper>
        <ListWrapper>
          <FestivalList />
        </ListWrapper>
      </SectionWrapper>
    </ContentWrapper>
  </PageWrapper>
</AppWrapper>
```

문제:

```text
각 Wrapper의 책임이 불명확하다.
구조를 읽기 어렵다.
Props 전달과 스타일 적용 위치가 복잡해진다.
```

개선:

```tsx
<PageLayout>
  <Section title="축제 목록">
    <FestivalList />
  </Section>
</PageLayout>
```

검토 기준:

```text
Wrapper 이름이 책임을 설명하는가?
Wrapper가 semantic structure를 제공하는가?
Wrapper가 layout rule을 담당하는가?
Wrapper가 없으면 구조가 더 단순한가?
```

---

### [FAQ]

Q. Wrapper Hell이 뭐야?
A. 의미 없는 Wrapper Component가 과도하게 중첩되어 Component Tree가 복잡해지는 문제다.

Q. Wrapper Component는 언제 만들어?
A. 공통 Layout, semantic structure, 재사용 가능한 Section 구조처럼 명확한 책임이 있을 때 만든다.

Q. 모든 div를 Component로 분리하면 안 돼?
A. 권장하지 않는다. 책임 없는 Component는 파일과 계층만 늘린다.

Q. Wrapper Hell은 어떻게 해결해?
A. 책임 없는 Wrapper를 제거하고 PageLayout, Section처럼 의미 있는 Component만 남긴다.

---

## 9.3 Over-Composition Problem

### [개념]

Over-Composition은 Component 조합을 과도하게 세분화해서 오히려 사용성과 가독성이 떨어지는 문제다.

Composition은 책임 분리를 위해 사용해야 하며, 단순한 UI까지 모두 추상화하면 유지보수성이 떨어질 수 있다.

---

### [핵심]

Over-Composition 문제:

- Component 수가 과도하게 많다.
- 작은 수정에도 여러 파일을 이동해야 한다.
- Component 이름이 모호하다.
- Props 전달이 증가한다.
- 추상화 수준이 일관되지 않다.
- 실제 재사용성이 낮다.
- 코드 흐름 추적이 어렵다.

해결:

- 실제 책임이 있는 Component만 분리한다.
- 반복 패턴이 확인된 후 공통화한다.
- 단순한 1회성 JSX는 유지한다.
- 의미 없는 Wrapper를 제거한다.
- Props만 전달하는 Component를 줄인다.
- Composition depth를 검토한다.

---

### [실무]

과도한 분리 예:

```text
FestivalTitle
FestivalTitleText
FestivalTitleWrapper
FestivalDescriptionText
FestivalRegionText
FestivalDateText
FestivalImageBox
FestivalImageWrapper
```

문제:

```text
각 Component의 독립 책임이 약하다.
파일 수가 늘어난다.
수정 흐름이 분산된다.
```

개선:

```tsx
function FestivalCard({ festival }: FestivalCardProps) {
  return (
    <article>
      <img src={festival.imageUrl} alt={festival.title} />
      <h2>{festival.title}</h2>
      <p>{festival.regionName}</p>
      <p>{festival.periodText}</p>
    </article>
  );
}
```

분리 기준:

```text
독립적인 상태가 있다
→ 분리 검토

반복 렌더링된다
→ 분리 검토

재사용된다
→ 분리 검토

단순 텍스트 표시다
→ 유지 가능
```

---

### [FAQ]

Q. Over-Composition이 뭐야?
A. Component 조합을 과도하게 세분화해서 오히려 사용성과 가독성이 떨어지는 문제다.

Q. 작은 JSX도 모두 Component로 분리해야 해?
A. 아니다. 책임이 명확하지 않은 1회성 JSX는 그대로 둬도 된다.

Q. Over-Composition은 어떻게 찾을 수 있어?
A. Component 이름이 모호하고 Props 전달만 하며 실제 재사용성이 낮은 Component가 많으면 의심할 수 있다.

Q. Composition과 Over-Composition의 차이는 뭐야?
A. Composition은 책임 있는 조합이고 Over-Composition은 책임 없는 과도한 분리다.

---

# 10. Composition Review Checklist

## 10.1 Component Composition Checklist

### [개념]

Component Composition Checklist는 Component 조합 구조가 명확하고 유지보수 가능한지 검수하는 기준이다.

Frontend Agent와 Review Agent는 Component Tree, Props 흐름, children 사용, slot-like props 사용, Over-Composition 여부를 함께 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Page Component가 화면 조립자 역할을 하는가?
- [ ] Feature Component가 도메인 기능 단위를 담당하는가?
- [ ] UI Component가 도메인 로직에서 분리되어 있는가?
- [ ] Component Tree가 책임 기준으로 구성되었는가?
- [ ] children 사용이 적절한가?
- [ ] children 구조가 너무 암묵적이지 않은가?
- [ ] slot-like props가 필요한 영역에 사용되었는가?
- [ ] slot-like props 이름이 명확한가?
- [ ] Layout Component가 공통 구조만 담당하는가?
- [ ] Feature Boundary가 명확한가?
- [ ] Reusable UI Component가 API 호출을 하지 않는가?
- [ ] Domain Component와 UI Component가 구분되는가?
- [ ] Props 흐름이 과도하게 깊지 않은가?
- [ ] Data Down, Action Up 흐름이 유지되는가?
- [ ] Props만 전달하는 중간 Component가 과도하지 않은가?
- [ ] Wrapper Hell이 발생하지 않았는가?
- [ ] Over-Composition이 아닌가?
- [ ] Compound Component가 과도하게 도입되지 않았는가?
```

---

### [실무]

Review Flow:

```text
Component Tree Review
→ Page / Feature / UI Role Check
→ Children Usage Check
→ Slot-like Props Check
→ Layout Responsibility Check
→ Props Flow Check
→ Domain / UI Separation Check
→ Anti Pattern Check
```

치명적 문제:

```text
- Page Component가 모든 JSX를 직접 렌더링
- UI Component가 API 호출 수행
- 의미 없는 Wrapper Component 과다
- children으로 접근성 책임을 모두 외부에 넘김
- slot props가 너무 많아 Component 책임 불명확
- Base Component 하나에 모든 도메인 변형을 몰아넣음
- Compound Component를 불필요하게 남용
```

---

### [FAQ]

Q. Composition 검수에서 가장 중요한 것은?
A. Page, Feature, UI Component 역할 구분과 Props 흐름의 명확성이다.

Q. children 사용 검수에서 뭘 봐야 해?
A. children이 적절한 조합성을 제공하는지, 구조가 너무 암묵적이지 않은지, 접근성 책임이 유지되는지 확인한다.

Q. Slot-like Props 검수에서 뭘 봐야 해?
A. header, footer, actions 같은 이름이 명확한지와 slot props가 과도하지 않은지 확인한다.

Q. 치명적인 Composition 문제는 뭐야?
A. Page에 모든 JSX가 몰리거나 UI Component가 API를 호출하거나 의미 없는 Wrapper가 과도한 경우다.

---

# 11. Agent Output Rules

## 11.1 Frontend Agent Composition Output

### [개념]

Frontend Agent는 React 화면 코드를 생성하기 전에 Component Composition 구조를 먼저 설계해야 한다.

Composition Output은 Component Tree, Page / Feature / UI 구분, children 사용 여부, slot-like props 사용 여부, Props Flow를 포함해야 한다.

---

### [핵심]

Frontend Agent Composition 출력 항목:

- Page Component
- Feature Components
- Reusable UI Components
- Layout Components
- Component Tree
- Component Responsibility
- Composition Pattern
- children 사용 여부
- slot-like props 사용 여부
- Data Down Flow
- Action Up Flow
- Props Drilling Risk
- Anti Pattern Review

---

### [실무]

출력 예:

```text
Component Tree:

FestivalSearchPage
- type: Page Component
- responsibility: 축제 검색 화면 조립, 검색 조건 State 소유

PageLayout
- type: Layout Component
- responsibility: 공통 Header / main / Footer 구조 제공
- composition: children

PageHeader
- type: Reusable UI Component
- responsibility: 페이지 제목과 actions 영역 표시
- props: title, description, actions

FestivalSearchSection
- type: Feature Component
- responsibility: 검색어 입력과 검색 이벤트 전달

FestivalFilterSection
- type: Feature Component
- responsibility: 지역 / 테마 필터 선택

FestivalResultSection
- type: Feature Component
- responsibility: loading / error / empty / list 상태 표시

FestivalCard
- type: Domain Component
- responsibility: 축제 단일 항목 표시

Button
- type: Reusable UI Component
- responsibility: 클릭 가능한 버튼 표시
```

Props Flow 예:

```text
Data Down:
FestivalSearchPage → FestivalResultSection → FestivalList → FestivalCard

Action Up:
FestivalCard onSelect
→ FestivalList onSelectFestival
→ FestivalSearchPage handleSelectFestival
```

Anti Pattern Review:

```text
- UI Component API 호출 없음
- Page에 모든 JSX 몰림 없음
- Wrapper Hell 없음
- children 사용 목적 명확
- slot-like props 과다 없음
```

---

### [FAQ]

Q. Frontend Agent는 Composition을 언제 설계해야 해?
A. Component 코드를 생성하기 전에 Component Tree와 Composition 구조를 먼저 설계해야 한다.

Q. Composition Output에는 무엇이 포함돼야 해?
A. Component Tree, 역할 구분, children 사용 여부, slot-like props, Props Flow, Anti Pattern Review가 포함되어야 한다.

Q. Component Tree는 왜 필요해?
A. 화면을 어떤 Component 조합으로 만들지 명확히 해서 코드 생성과 Review 품질을 높이기 위해 필요하다.

Q. Review Agent는 Composition Output에서 뭘 봐야 해?
A. Page / Feature / UI 역할 구분, Props 흐름, children 사용 적절성, Over-Composition 여부를 확인해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. React Component Composition이 뭐야?
A. 작은 Component를 조합해 큰 UI와 화면을 만드는 React 설계 방식이다.

Q. React에서 상속보다 Composition을 쓰는 이유는?
A. Component 조합 방식이 UI 재사용, 변경, 확장에 더 유연하기 때문이다.

Q. Component Composition과 Component 분리 차이는 뭐야?
A. Component 분리는 경계를 나누는 작업이고 Composition은 나눈 Component를 다시 조합해 화면을 만드는 작업이다.

Q. 좋은 Composition의 기준은 뭐야?
A. Page, Feature, UI Component 책임이 명확하고 Props 흐름이 단순하며 재사용 가능한 UI가 잘 분리된 구조다.

Q. Component를 조합할 때 가장 중요한 기준은 뭐야?
A. 책임이 명확한 Component Tree를 만드는 것이다.

Q. Component 중첩이 많으면 무조건 나빠?
A. 아니다. 의미 있는 계층이면 괜찮다. 하지만 Props만 전달하는 계층이 많으면 구조를 재검토해야 한다.

Q. children이 뭐야?
A. Component 내부에 외부에서 전달한 ReactNode를 렌더링하는 Props다.

Q. children은 언제 써?
A. Component 내부 내용을 외부에서 자유롭게 조합해야 할 때 사용한다.

Q. children 타입은 뭐로 써?
A. TypeScript React에서는 일반적으로 ReactNode를 사용한다.

Q. children을 쓰면 무조건 좋은 설계야?
A. 아니다. 구조가 고정되어 있거나 필요한 데이터가 명확하면 explicit props가 더 좋을 수 있다.

Q. children과 explicit props 차이는 뭐야?
A. children은 자유로운 내부 조합에 좋고 explicit props는 구조가 고정되고 데이터 의미가 명확할 때 좋다.

Q. Card에는 children이 좋아?
A. 공통 Card Wrapper라면 children이 좋고, 도메인 카드라면 title, imageUrl 같은 explicit props가 좋을 수 있다.

Q. Modal을 children만으로 만들면 안 돼?
A. 가능은 하지만 title, role, aria-modal, close button 같은 핵심 구조는 Modal Component가 책임지는 것이 좋다.

Q. Slot-like Props가 뭐야?
A. header, footer, actions처럼 특정 영역에 ReactNode를 전달해 Component를 조합하는 방식이다.

Q. Slot-like Props는 언제 써?
A. Card, Modal, Panel처럼 특정 영역만 외부에서 커스터마이징하고 싶을 때 사용한다.

Q. children과 Slot-like Props 차이는?
A. children은 전체 본문을 전달하고 Slot-like Props는 header, action, footer 같은 특정 영역을 전달한다.

Q. Slot-like Props 이름은 어떻게 지어?
A. header, footer, actions, aside처럼 영역과 의미가 명확한 이름을 사용한다.

Q. actions는 언제 써?
A. 버튼, 링크, 메뉴처럼 사용자가 수행할 수 있는 동작 영역을 전달할 때 사용한다.

Q. slot props가 많으면 왜 문제야?
A. Component가 너무 많은 영역과 변형을 담당해 책임이 불명확해질 수 있다.

Q. Layout Component는 뭐야?
A. Header, Footer, Sidebar, main 영역 같은 공통 화면 구조를 담당하는 Component다.

Q. Layout Component는 children을 써?
A. 일반적으로 children을 사용해 페이지별 내용을 main 영역에 렌더링한다.

Q. Page Composition이 뭐야?
A. 하나의 화면을 여러 Feature Section과 UI Component로 조합하는 방식이다.

Q. Page Component는 어떤 역할을 해야 해?
A. 화면 조립, 주요 State 관리, 데이터 흐름 연결을 담당하고 세부 UI는 하위 Component로 분리한다.

Q. Page에 모든 JSX를 넣으면 왜 안 좋아?
A. Page가 Overgrown Component가 되어 책임이 불명확하고 유지보수가 어려워진다.

Q. Feature Composition이 뭐야?
A. 특정 도메인 기능을 여러 하위 UI Component와 Local State로 구성하는 방식이다.

Q. Feature Component는 UI Component를 조합해도 돼?
A. 가능하다. Button, Input, Card 같은 공통 UI Component를 조합해 도메인 기능을 만든다.

Q. Feature Boundary는 어떻게 잡아?
A. 도메인 기능 단위, 독립 UI 영역, Local State, 이벤트 흐름을 기준으로 잡는다.

Q. Reusable UI Composition이 뭐야?
A. 공통 UI Component를 조합해 여러 Feature에서 재사용하는 방식이다.

Q. Reusable UI Component는 API 호출을 해도 돼?
A. 권장하지 않는다. UI Component는 표시와 상호작용만 담당해야 한다.

Q. Domain Component와 Reusable UI Component 차이는 뭐야?
A. Domain Component는 특정 도메인 데이터와 기능에 의존하고 Reusable UI Component는 도메인과 무관하게 재사용된다.

Q. FestivalCard는 UI Component야?
A. 축제 도메인 데이터를 직접 사용하면 Domain Component 또는 Feature Component에 가깝다.

Q. Compound Component가 뭐야?
A. 여러 하위 Component를 조합해 하나의 UI 패턴을 구성하는 React Component Pattern이다.

Q. Compound Component는 언제 써?
A. Tabs, Accordion, Dropdown처럼 하위 Component들이 강하게 연결된 UI 패턴에 적합하다.

Q. Slot-like Props와 Compound Component 차이는?
A. Slot-like Props는 특정 영역에 ReactNode를 전달하는 단순 방식이고 Compound Component는 하위 Component 조합 규칙을 가진 패턴이다.

Q. Compound Component를 많이 만들면 좋아?
A. 아니다. 실제 반복되는 복잡한 UI 패턴이 있을 때만 사용하는 것이 좋다.

Q. Data Down, Action Up이 뭐야?
A. 데이터는 부모에서 자식으로 Props로 내려가고 이벤트는 자식에서 부모로 Callback Props로 올라가는 흐름이다.

Q. Composition이 Props Drilling을 줄일 수 있어?
A. 가능하다. children이나 slot-like props를 활용하면 중간 Component가 Props 전달만 하는 구조를 줄일 수 있다.

Q. Props Drilling은 무조건 Context로 해결해야 해?
A. 아니다. State Owner와 Component Composition을 먼저 재검토한다.

Q. React에서 상속으로 Component를 확장하면 안 돼?
A. React에서는 상속보다 Composition을 우선한다. Component 조합과 Props 기반 설계가 더 유연하다.

Q. Wrapper Hell이 뭐야?
A. 의미 없는 Wrapper Component가 과도하게 중첩되어 Component Tree가 복잡해지는 문제다.

Q. Wrapper Component는 언제 만들어?
A. 공통 Layout, semantic structure, 재사용 가능한 Section 구조처럼 명확한 책임이 있을 때 만든다.

Q. Over-Composition이 뭐야?
A. Component 조합을 과도하게 세분화해서 오히려 사용성과 가독성이 떨어지는 문제다.

Q. 작은 JSX도 모두 Component로 분리해야 해?
A. 아니다. 책임이 명확하지 않은 1회성 JSX는 그대로 둬도 된다.

Q. Composition 검수에서 가장 중요한 것은?
A. Page, Feature, UI Component 역할 구분과 Props 흐름의 명확성이다.

Q. React Component Design Part04의 핵심은 뭐야?
A. children, slot-like props, Layout, Feature, Reusable UI Component를 조합해 유지보수 가능한 Component Tree를 설계하는 것이다.
