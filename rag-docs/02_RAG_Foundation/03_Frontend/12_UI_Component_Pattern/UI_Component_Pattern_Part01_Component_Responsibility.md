# UI Component Pattern Part01 - Component Responsibility

---

# 1. UI Component Pattern Overview

## 1.1 UI Component Pattern Purpose

### [개념]

UI Component Pattern은 React Frontend에서 재사용 가능한 UI Component를 설계하기 위한 기준이다.

이 문서는 사람이 읽는 학습 문서가 아니라 Frontend Agent / Review Agent / PM Agent가 UI Component 설계, 코드 생성, 코드 검토, 리팩토링 판단에 사용할 RAG 문서다.

UI Component Pattern은 Button, Input, Modal, Card, List, Table, Tab, Dropdown 같은 공통 UI 단위의 책임, 재사용 기준, Props 설계, 접근성, 스타일 경계를 정의한다.

---

### [핵심]

- UI Component Pattern은 재사용 가능한 UI 설계 기준이다.
- UI Component는 화면 표현과 사용자 상호작용을 담당한다.
- Common UI와 Feature UI를 구분해야 한다.
- Component 책임이 명확해야 한다.
- Props 설계는 사용 의도를 드러내야 한다.
- 접근성은 UI Component의 기본 책임이다.
- Styling Boundary를 분리해야 한다.
- 과도한 추상화와 Props Explosion을 방지해야 한다.
- Frontend Agent는 이 기준으로 Component를 생성하고 Review Agent는 이 기준으로 검토한다.

---

### [실무]

2026 실무 기준에서 UI Component Pattern은 단순 Component 모음집이 아니다.

Frontend Agent는 UI Component Pattern을 기준으로 다음 작업을 수행해야 한다.

```text
User UI Request
→ Identify UI Responsibility
→ Decide Common UI or Feature UI
→ Design Props API
→ Add Variant / Size / State
→ Add Event Handler Props
→ Add Accessibility
→ Separate Styling Boundary
→ Check Anti Pattern
→ Generate Component
```

UI Component Pattern은 React Component Design 이후 공통 UI를 정리하는 단계에서 사용한다.

```text
React Component Design
→ UI Component Pattern
→ State Management
→ Error Handling & Loading UX
→ Frontend Accessibility
→ Design System Foundation
```

---

### [FAQ]

Q. UI Component Pattern 문서는 왜 필요해?
A. Frontend Agent가 Button, Modal, Card 같은 UI Component를 일관되게 설계하고 재사용 기준을 판단해야 하기 때문이다.

Q. UI Component Pattern은 React Component Design과 뭐가 달라?
A. React Component Design은 Component 분리와 상태 위치를 다루고, UI Component Pattern은 Button, Modal, Card 같은 재사용 UI 단위의 설계 기준에 집중한다.

Q. UI Component Pattern에서 가장 중요한 기준은 뭐야?
A. Component Responsibility, Common UI / Feature UI 구분, Props Design, Accessibility, Styling Boundary, Anti Pattern 방지다.

---

# 2. Component Responsibility

## 2.1 UI Component Responsibility

### [개념]

UI Component Responsibility는 Component가 담당하는 역할과 책임 범위를 명확히 정하는 기준이다.

UI Component는 화면 표현, 사용자 입력, 시각 상태, 접근성 속성, 이벤트 전달을 담당한다.

UI Component는 도메인 API 호출, 인증 판단, 서버 상태 캐싱, 복잡한 비즈니스 로직을 직접 포함하지 않는 것이 좋다.

---

### [핵심]

UI Component 기본 책임:

- 화면 표시
- 사용자 입력
- 사용자 이벤트 전달
- 클릭 가능 상태 표현
- disabled 상태 표현
- loading 상태 표현
- error 상태 표현
- selected 상태 표현
- 접근성 속성 제공
- semantic HTML 사용
- variant / size 스타일 적용
- children / composition 구조 제공

UI Component에 넣지 않는 것이 좋은 책임:

- 직접 API 호출
- 인증 권한 판단 심화
- 도메인 데이터 가공 심화
- 서버 상태 캐싱
- route 이동 정책 심화
- 복잡한 비즈니스 규칙
- 특정 도메인 엔티티 의존
- 특정 API 응답 필드 의존

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

```tsx
function Button({ reviewId }) {
  async function handleClick() {
    await deleteReview(reviewId);
  }

  return <button onClick={handleClick}>삭제</button>;
}
```

개선 예:

```tsx
type ButtonProps = {
  type?: "button" | "submit" | "reset";
  disabled?: boolean;
  loading?: boolean;
  onClick?: () => void;
  children: React.ReactNode;
};

function Button({
  type = "button",
  disabled = false,
  loading = false,
  onClick,
  children,
}: ButtonProps) {
  return (
    <button type={type} disabled={disabled || loading} onClick={onClick}>
      {loading ? "처리 중..." : children}
    </button>
  );
}
```

도메인 삭제 로직은 Feature Component에서 처리한다.

```tsx
function ReviewDeleteButton({ reviewId }: { reviewId: number }) {
  async function handleDelete() {
    await deleteReview(reviewId);
  }

  return <Button onClick={handleDelete}>삭제</Button>;
}
```

---

### [FAQ]

Q. 공통 Button Component 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. 공통 Button은 UI 역할만 담당하고 API 호출은 Feature Component나 Hook에서 처리하는 것이 좋다.

Q. UI Component의 책임은 어디까지야?
A. 화면 표시, 사용자 이벤트 전달, 접근성, 시각 상태 표현까지가 기본 책임이다.

Q. API 호출은 어느 Component에서 처리해야 해?
A. Feature Component, Page Component, Custom Hook, Server State Hook에서 처리하는 것이 좋다.

---

## 2.2 Responsibility Flow

### [개념]

Responsibility Flow는 UI 요청을 Component 구조로 나누는 판단 흐름이다.

Agent는 UI를 만들기 전에 먼저 Component가 공통 UI인지, Feature UI인지, Page Component인지 구분해야 한다.

---

### [핵심]

판단 흐름:

```text
UI Request
→ Identify Visible Element
→ Identify User Interaction
→ Check Domain Dependency
→ Check Reuse Possibility
→ Decide Component Type
→ Design Props
→ Add Accessibility
→ Review Responsibility
```

Component Type 후보:

- Common UI Component
- Feature UI Component
- Layout Component
- State UI Component
- Page Component

---

### [실무]

예시 요청:

```text
축제 목록 화면에 축제 카드를 보여줘.
```

분해:

```text
Page
→ FestivalListPage

Feature UI
→ FestivalList
→ FestivalCard

Common UI
→ Card
→ Badge
→ Button

State UI
→ LoadingState
→ ErrorState
→ EmptyState
```

책임 분리:

```text
FestivalListPage
→ API 호출, page state 관리

FestivalList
→ festival 배열 렌더링

FestivalCard
→ festival 데이터 표시

Card
→ 범용 카드 UI 구조 제공

Badge
→ 카테고리 / 상태 표시

Button
→ 사용자 액션 UI 제공
```

---

### [FAQ]

Q. UI 요청이 들어오면 Component부터 바로 만들면 돼?
A. 아니다. 먼저 책임, 도메인 의존성, 재사용 가능성, 접근성 기준을 확인해야 한다.

Q. Component Type은 왜 먼저 나눠?
A. Common UI와 Feature UI를 섞으면 API 호출, 도메인 props, 스타일 예외가 공통 Component에 누적되기 때문이다.

Q. Page Component와 Feature Component는 뭐가 달라?
A. Page Component는 routing 단위 화면이고 Feature Component는 특정 도메인 기능을 구성하는 UI 단위다.

---

# 3. Common UI and Feature UI

## 3.1 Common UI Component

### [개념]

Common UI Component는 여러 화면과 여러 도메인에서 반복 사용할 수 있는 범용 UI Component다.

Common UI Component는 도메인 데이터를 알지 않아야 하며, 특정 API 호출이나 특정 엔티티 필드에 의존하지 않는 것이 좋다.

---

### [핵심]

Common UI 예:

- Button
- TextField
- Modal
- Dialog
- Card
- Badge
- Avatar
- Tabs
- Dropdown
- Pagination
- LoadingState
- ErrorState
- EmptyState
- Skeleton
- SearchBox
- FormField

Common UI 기준:

- 도메인 의존 낮음
- 여러 화면에서 반복 사용
- Props가 단순함
- 역할이 안정적임
- 스타일 변형이 제한적임
- 접근성 처리 반복 가능
- API 호출 없음
- 엔티티 필드 직접 의존 없음

---

### [실무]

Common UI 예:

```tsx
type CardProps = {
  children: React.ReactNode;
};

function Card({ children }: CardProps) {
  return <article className="card">{children}</article>;
}
```

Common UI는 도메인 용어를 모르게 작성한다.

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "danger";
  size?: "sm" | "md" | "lg";
  onClick?: () => void;
  children: React.ReactNode;
};

function Button({
  variant = "primary",
  size = "md",
  onClick,
  children,
}: ButtonProps) {
  return (
    <button
      type="button"
      className={`button button-${variant} button-${size}`}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
```

Common UI에 넣으면 안 좋은 예:

```tsx
type ButtonProps = {
  festivalId: number;
  reviewId: number;
  isAdminOnly: boolean;
  onDeleteReview: () => void;
};
```

이 경우 Button이 아니라 Feature Component를 만들어야 한다.

---

### [FAQ]

Q. Common UI Component는 어떤 Component야?
A. 여러 도메인에서 반복 사용할 수 있고 도메인 데이터나 API에 의존하지 않는 범용 UI Component다.

Q. Button, Modal은 어디에 둬?
A. 여러 도메인에서 사용하는 공통 UI이므로 components/ui 또는 components/common에 둔다.

Q. Common UI에서 도메인 props를 받아도 돼?
A. 권장하지 않는다. 도메인 props는 Feature Component에서 처리하는 것이 좋다.

---

## 3.2 Feature UI Component

### [개념]

Feature UI Component는 특정 도메인, 특정 화면, 특정 사용자 시나리오에 맞춰진 Component다.

Feature UI Component는 도메인 데이터 구조, API 응답 필드, 사용자 액션 흐름을 알고 있어도 된다.

---

### [핵심]

Feature UI 예:

- FestivalCard
- FestivalSearchFilter
- ReviewForm
- ReviewDeleteButton
- LoginForm
- NotificationItem
- ChatMessageBubble
- DonationButton
- UserProfileCard

Feature UI 기준:

- 특정 도메인 데이터에 의존
- 특정 API 응답 필드 사용
- 특정 사용자 액션 처리
- Common UI를 조합
- 도메인 UX 반영
- Feature Hook 사용 가능
- Page보다 작은 기능 단위

---

### [실무]

Feature UI 예:

```tsx
type Festival = {
  festivalId: number;
  title: string;
  regionName: string;
  categoryName: string;
};

type FestivalCardProps = {
  festival: Festival;
  onClick?: (festivalId: number) => void;
};

function FestivalCard({ festival, onClick }: FestivalCardProps) {
  return (
    <Card>
      <h3>{festival.title}</h3>
      <p>{festival.regionName}</p>
      <Badge>{festival.categoryName}</Badge>
      <Button onClick={() => onClick?.(festival.festivalId)}>
        자세히 보기
      </Button>
    </Card>
  );
}
```

Feature UI는 Common UI를 조합한다.

```text
FestivalCard
→ Card
→ Badge
→ Button
```

Feature UI는 domain field를 사용할 수 있다.

```text
festival.title
festival.regionName
festival.categoryName
festival.festivalId
```

---

### [FAQ]

Q. FestivalCard는 공통 Component야?
A. 보통 Feature UI다. festival 데이터 구조에 의존하기 때문이다.

Q. Card Component와 FestivalCard는 뭐가 달라?
A. Card는 범용 컨테이너이고 FestivalCard는 축제 정보를 보여주는 도메인 Component다.

Q. Feature UI 안에서는 API 호출을 해도 돼?
A. 가능하지만 복잡한 API 로직은 Custom Hook이나 Page Component로 분리하는 것이 좋다.

---

## 3.3 Common UI vs Feature UI

### [개념]

Common UI와 Feature UI는 도메인 의존성, 재사용 범위, 책임 범위가 다르다.

Common UI는 범용 UI 구조를 제공하고 Feature UI는 도메인 기능과 사용자 시나리오를 구현한다.

---

### [핵심]

| 비교        | Common UI           | Feature UI                 |
| ----------- | ------------------- | -------------------------- |
| 목적        | 범용 UI 제공        | 특정 도메인 UI 구현        |
| 도메인 의존 | 낮음                | 높음                       |
| API 호출    | 없음 권장           | 가능                       |
| 데이터 구조 | 모름                | 알고 있음                  |
| 예          | Button, Modal, Card | FestivalCard, ReviewForm   |
| 위치        | components/ui       | features/domain/components |
| Props       | 일반 UI Props       | 도메인 Props 가능          |
| 변경 영향   | 여러 화면 영향      | 특정 기능 영향             |

---

### [실무]

분리 기준:

```text
여러 도메인에서 반복 사용
→ Common UI

특정 도메인 데이터 구조에 의존
→ Feature UI

특정 API 응답 필드에 의존
→ Feature UI

스타일과 상호작용만 제공
→ Common UI

비즈니스 액션을 연결
→ Feature UI
```

권장 구조:

```text
src
├ components
│  └ ui
│     ├ Button.tsx
│     ├ Card.tsx
│     ├ Modal.tsx
│     └ Badge.tsx
└ features
   └ festival
      └ components
         ├ FestivalCard.tsx
         └ FestivalSearchFilter.tsx
```

---

### [FAQ]

Q. Common UI와 Feature UI를 나누는 가장 쉬운 기준은 뭐야?
A. Component가 특정 도메인 데이터나 API 응답 필드를 알고 있으면 Feature UI로 보는 것이 안전하다.

Q. 공통 UI가 Feature 요구사항을 모두 처리하면 안 돼?
A. 권장하지 않는다. 공통 UI가 예외 props로 가득 차고 재사용성이 떨어질 수 있다.

Q. Feature UI에서 Common UI를 사용하는 방식이 좋아?
A. 좋다. Common UI는 기본 구조를 제공하고 Feature UI는 도메인 데이터를 조합하는 방식이 유지보수에 좋다.

---

# 4. Reusability Criteria

## 4.1 Reusable Component Criteria

### [개념]

Reusable Component Criteria는 Component를 공통화할지 판단하는 기준이다.

재사용성은 예상이 아니라 실제 반복, 역할 안정성, 낮은 도메인 의존성을 기준으로 판단한다.

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
- 이름이 범용적임
- 변경 이유가 적음

공통화 부적합 기준:

- 한 화면에서만 사용
- 도메인 로직이 강함
- Props가 계속 늘어남
- 예외 케이스가 많음
- 특정 API 응답에 의존
- 특정 사용자 시나리오만 처리
- 이름은 공통인데 실제 요구가 다름

---

### [실무]

공통화 판단 Flow:

```text
UI가 반복되는가?
→ 역할이 같은가?
→ 도메인 의존이 없는가?
→ Props가 안정적인가?
→ 접근성 처리를 반복할 수 있는가?
→ 공통 UI로 분리
```

예시:

```text
여러 화면에서 같은 모양의 버튼 사용
→ Button Common UI 가능

축제 정보를 표시하는 카드 사용
→ FestivalCard Feature UI

여러 도메인에서 카드 껍데기만 반복
→ Card Common UI 가능
```

처음부터 모든 UI를 공통화하지 않는다.

```text
첫 번째 사용
→ Feature 내부 작성 가능

두세 번 반복
→ 역할과 props 안정성 확인

반복 패턴 확정
→ Common UI로 분리
```

---

### [FAQ]

Q. Component는 처음부터 재사용 가능하게 만들어야 해?
A. 항상 그럴 필요는 없다. 실제 반복과 역할 안정성이 확인된 후 공통화하는 것이 더 안전하다.

Q. 공통화는 언제 하는 게 좋아?
A. 반복이 실제로 발생하고 역할과 props가 안정적일 때 하는 것이 좋다.

Q. 재사용성보다 중요한 기준이 있어?
A. 명확한 책임과 유지보수성이 더 중요하다. 재사용을 위해 Component가 복잡해지면 역효과가 날 수 있다.

---

## 4.2 Over Abstraction Prevention

### [개념]

Over Abstraction은 실제 필요보다 너무 범용적인 Component를 만들어 오히려 사용과 수정이 어려워지는 문제다.

UI Component는 중복 제거보다 명확한 책임과 안정적인 Props API가 우선이다.

---

### [핵심]

Over Abstraction 증상:

- Component 이름은 공통인데 사용법이 어려움
- props 조합을 이해하기 어려움
- boolean props가 많음
- 예외 처리가 많음
- 특정 화면 수정이 공통 Component 전체에 영향
- Component 내부가 도메인 분기로 가득함
- 재사용보다 조건문이 많음
- 문서화하기 어려운 API가 됨

해결 기준:

- 실제 재사용 사례 확인
- 도메인 Component로 되돌리기
- 작은 UI 단위로 분리
- children / composition 활용
- slot-like props 활용
- 공통화 범위 축소
- Feature Component로 분리

---

### [실무]

문제 예:

```tsx
type CardProps = {
  festival?: Festival;
  review?: Review;
  notification?: Notification;
  isFestivalMode?: boolean;
  isReviewMode?: boolean;
  isNotificationMode?: boolean;
};
```

문제점:

- Common Card가 도메인 데이터를 모두 알고 있음
- boolean props 조합이 복잡함
- 새로운 도메인이 추가될 때마다 Card가 수정됨
- Common UI 책임을 벗어남

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
      <Badge>{review.rating}</Badge>
    </Card>
  );
}
```

---

### [FAQ]

Q. 중복 코드를 없애려고 공통 Component를 만들었는데 더 복잡해졌어?
A. Over Abstraction일 수 있다. 반복 제거보다 역할 명확성과 사용 편의성이 중요하다.

Q. 공통 Component props가 너무 많아지면?
A. 역할이 너무 커졌을 가능성이 있다. Component 분리나 composition을 검토한다.

Q. 도메인 전용 props를 공통 Component에 넣어도 돼?
A. 권장하지 않는다. 도메인 전용 로직은 Feature Component에 두는 것이 좋다.

---

# 5. Component Responsibility Checklist

## 5.1 Responsibility Review Checklist

### [개념]

Component Responsibility Checklist는 UI Component 설계나 코드 리뷰 시 책임 분리가 적절한지 검수하는 기준이다.

Frontend Agent와 Review Agent는 Component 생성 후 이 체크리스트로 치명적 문제를 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Component 책임이 명확한가?
- [ ] Common UI와 Feature UI가 구분되었는가?
- [ ] 공통 UI에 도메인 로직이 들어가지 않았는가?
- [ ] 공통 UI에 API 호출이 들어가지 않았는가?
- [ ] 공통 UI가 특정 API 응답 필드에 의존하지 않는가?
- [ ] Props 이름이 명확한가?
- [ ] Props가 과도하게 많지 않은가?
- [ ] boolean props가 variant 역할을 대신하지 않는가?
- [ ] children / composition을 활용할 수 있는가?
- [ ] 접근성 속성이 포함되었는가?
- [ ] semantic HTML을 사용했는가?
- [ ] 스타일 책임과 layout 책임이 분리되었는가?
- [ ] Component 파일 위치가 적절한가?
- [ ] 과도한 추상화가 없는가?
- [ ] Feature Component로 분리할 부분이 있는가?
```

---

### [실무]

검수 Flow:

```text
Draft Component
→ Responsibility Check
→ Domain Dependency Check
→ Props API Check
→ Accessibility Check
→ Styling Boundary Check
→ Anti Pattern Check
→ Final Component Output
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
Props Explosion
Over Abstraction
```

---

### [FAQ]

Q. UI Component 검수에서 가장 먼저 볼 것은 뭐야?
A. Component 책임이 명확한지, Common UI와 Feature UI가 섞이지 않았는지 먼저 확인한다.

Q. 치명적인 UI Component 설계 문제는 뭐야?
A. 공통 UI에 API 호출이나 도메인 로직이 들어가고, props가 과도하게 늘어나며, 접근성이 누락되는 문제다.

Q. Review Agent는 어떤 기준으로 UI Component를 검토해야 해?
A. 책임 분리, 도메인 의존성, Props API, 접근성, 스타일 경계, 과도한 추상화 여부를 순서대로 확인해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. UI Component Pattern 문서는 왜 필요해?
A. Frontend Agent가 Button, Modal, Card 같은 UI Component를 일관되게 설계하고 재사용 기준을 판단해야 하기 때문이다.

Q. UI Component Pattern은 React Component Design과 뭐가 달라?
A. React Component Design은 Component 분리와 상태 위치를 다루고, UI Component Pattern은 Button, Modal, Card 같은 재사용 UI 단위의 설계 기준에 집중한다.

Q. UI Component Responsibility란 뭐야?
A. Component가 담당할 화면 표현, 사용자 이벤트, 접근성, 시각 상태와 제외해야 할 도메인 로직 범위를 정하는 기준이다.

Q. UI Component의 책임은 어디까지야?
A. 화면 표시, 사용자 이벤트 전달, 접근성, 시각 상태 표현까지가 기본 책임이다.

Q. 공통 Button Component 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. 공통 Button은 UI 역할만 담당하고 API 호출은 Feature Component나 Hook에서 처리하는 것이 좋다.

Q. API 호출은 어느 Component에서 처리해야 해?
A. Feature Component, Page Component, Custom Hook, Server State Hook에서 처리하는 것이 좋다.

Q. UI 요청이 들어오면 Component부터 바로 만들면 돼?
A. 아니다. 먼저 책임, 도메인 의존성, 재사용 가능성, 접근성 기준을 확인해야 한다.

Q. Common UI Component는 뭐야?
A. 여러 도메인에서 반복 사용할 수 있고 도메인 데이터나 API에 의존하지 않는 범용 UI Component다.

Q. Feature UI Component는 뭐야?
A. 특정 도메인 데이터, API 응답 필드, 사용자 시나리오에 맞춰진 Component다.

Q. Common UI와 Feature UI 차이는?
A. Common UI는 도메인 의존이 낮은 범용 UI이고 Feature UI는 특정 도메인 데이터와 기능에 맞춰진 Component다.

Q. Common UI와 Feature UI를 나누는 가장 쉬운 기준은 뭐야?
A. Component가 특정 도메인 데이터나 API 응답 필드를 알고 있으면 Feature UI로 보는 것이 안전하다.

Q. Button, Modal은 어디에 둬?
A. 여러 도메인에서 사용하는 공통 UI이므로 components/ui 또는 components/common에 둔다.

Q. FestivalCard는 공통 Component야?
A. 보통 Feature UI다. festival 데이터 구조에 의존하기 때문이다.

Q. Card Component와 FestivalCard는 뭐가 달라?
A. Card는 범용 컨테이너이고 FestivalCard는 축제 정보를 보여주는 도메인 Component다.

Q. Feature UI에서 Common UI를 사용하는 방식이 좋아?
A. 좋다. Common UI는 기본 구조를 제공하고 Feature UI는 도메인 데이터를 조합하는 방식이 유지보수에 좋다.

Q. Component는 처음부터 재사용 가능하게 만들어야 해?
A. 항상 그럴 필요는 없다. 실제 반복과 역할 안정성이 확인된 후 공통화하는 것이 더 안전하다.

Q. 공통화는 언제 하는 게 좋아?
A. 반복이 실제로 발생하고 역할과 props가 안정적일 때 하는 것이 좋다.

Q. 재사용성보다 중요한 기준이 있어?
A. 명확한 책임과 유지보수성이 더 중요하다. 재사용을 위해 Component가 복잡해지면 역효과가 날 수 있다.

Q. 중복 코드를 없애려고 공통 Component를 만들었는데 더 복잡해졌어?
A. Over Abstraction일 수 있다. 반복 제거보다 역할 명확성과 사용 편의성이 중요하다.

Q. 공통 Component props가 너무 많아지면?
A. 역할이 너무 커졌을 가능성이 있다. Component 분리나 composition을 검토한다.

Q. 도메인 전용 props를 공통 Component에 넣어도 돼?
A. 권장하지 않는다. 도메인 전용 로직은 Feature Component에 두는 것이 좋다.

Q. UI Component 검수에서 가장 먼저 볼 것은 뭐야?
A. Component 책임이 명확한지, Common UI와 Feature UI가 섞이지 않았는지 먼저 확인한다.

Q. 치명적인 UI Component 설계 문제는 뭐야?
A. 공통 UI에 API 호출이나 도메인 로직이 들어가고, props가 과도하게 늘어나며, 접근성이 누락되는 문제다.

Q. Review Agent는 어떤 기준으로 UI Component를 검토해야 해?
A. 책임 분리, 도메인 의존성, Props API, 접근성, 스타일 경계, 과도한 추상화 여부를 순서대로 확인해야 한다.
