# React Component Design Part02 - Props Design

---

# 1. Props Design

## 1.1 Props Design Definition

### [개념]

Props Design은 부모 Component가 자식 Component에 전달하는 데이터, 이벤트, 설정값의 구조를 설계하는 작업이다.

Props는 Component 외부 계약이다.

React Component는 Props를 통해 외부에서 필요한 값을 받고, Callback Props를 통해 내부에서 발생한 이벤트를 부모에게 알린다.

Props Design이 명확하면 Component Responsibility, Component Boundary, State Ownership을 안정적으로 연결할 수 있다.

---

### [핵심]

- Props는 Component Contract다.
- Props는 부모와 자식 사이의 데이터 전달 계약이다.
- Props는 읽기 전용으로 다룬다.
- Props 이름은 Component 사용 의도를 드러내야 한다.
- Props는 필요한 값만 전달하는 것이 기본이다.
- Callback Props는 자식 이벤트를 부모에게 알리는 방식이다.
- Boolean Props가 많아지면 불가능한 상태가 생길 수 있다.
- 상호 배타 상태는 union variant로 설계한다.
- Props Type은 Component Contract를 문서화한다.
- Props가 과도하게 많으면 Component Boundary를 재검토한다.

---

### [실무]

2026 실무 기준에서 Props Design은 단순히 값을 넘기는 문법이 아니다.

Props Design은 아래 질문에 답해야 한다.

```text
이 Component는 외부에서 어떤 데이터를 받아야 하는가?
이 Component는 어떤 이벤트를 외부에 알려야 하는가?
이 Component는 어떤 상태를 직접 소유하지 않아야 하는가?
이 Component의 외부 사용법이 명확한가?
```

좋은 Props Design 예:

```tsx
type FestivalCardProps = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  regionName: string;
  isSelected?: boolean;
  onSelect: (festivalId: number) => void;
};

function FestivalCard({
  festivalId,
  title,
  imageUrl,
  regionName,
  isSelected = false,
  onSelect,
}: FestivalCardProps) {
  return (
    <article aria-selected={isSelected}>
      {imageUrl && <img src={imageUrl} alt={title} />}
      <h2>{title}</h2>
      <p>{regionName}</p>
      <button type="button" onClick={() => onSelect(festivalId)}>
        상세 보기
      </button>
    </article>
  );
}
```

좋은 점:

- 필요한 값이 명확하다.
- Props 이름이 구체적이다.
- Callback Props 이름이 `onSelect`로 명확하다.
- 자식은 선택 이벤트만 알리고 실제 처리는 부모가 담당한다.
- Optional Props에 기본값을 제공한다.
- Props Type이 Component Contract 역할을 한다.

---

### [FAQ]

Q. Props Design이 뭐야?
A. Component가 외부에서 어떤 데이터와 이벤트 함수를 받을지 정하는 설계 작업이다.

Q. Props는 왜 Component Contract라고 해?
A. 부모가 자식 Component를 사용할 때 어떤 값을 제공해야 하는지 정의하는 외부 계약이기 때문이다.

Q. Props는 자식 Component에서 수정해도 돼?
A. 안 된다. Props는 읽기 전용으로 다루고 변경이 필요하면 부모에게 Callback Props로 알린다.

Q. Props Design이 나쁘면 어떤 문제가 생겨?
A. Component 사용법이 모호해지고 Props Drilling, 불가능한 상태, 과도한 결합, 재사용성 저하가 발생할 수 있다.

---

# 2. Props Contract

## 2.1 Props Contract Rules

### [개념]

Props Contract는 Component가 외부에서 요구하는 데이터와 이벤트 함수의 명확한 계약이다.

Props Contract는 Component 사용자가 어떤 값을 전달해야 하는지, 어떤 값은 선택 사항인지, 어떤 이벤트를 받을 수 있는지 설명한다.

---

### [핵심]

Props Contract 구성 요소:

- Required Props
- Optional Props
- Default Value
- Callback Props
- Children
- Variant
- TypeScript Props Type
- Event Handler Type
- Data Shape
- Stable Props Shape

Props Contract 원칙:

- 필수 값과 선택 값을 구분한다.
- Optional Props에는 기본값을 고려한다.
- Callback Props는 의도를 드러낸다.
- Props 이름은 구체적으로 작성한다.
- Component 책임에 필요한 Props만 받는다.
- Props Type은 Component 가까이에 작성한다.
- 공유 타입은 별도 types 파일로 분리한다.

---

### [실무]

Required Props 예:

```tsx
type UserAvatarProps = {
  imageUrl: string | null;
  username: string;
};

function UserAvatar({ imageUrl, username }: UserAvatarProps) {
  return (
    <div>
      {imageUrl ? (
        <img src={imageUrl} alt={`${username} 프로필 이미지`} />
      ) : (
        <span>{username[0]}</span>
      )}
    </div>
  );
}
```

Optional Props 예:

```tsx
type BadgeProps = {
  label: string;
  variant?: "default" | "success" | "warning" | "error";
};

function Badge({ label, variant = "default" }: BadgeProps) {
  return <span className={`badge badge-${variant}`}>{label}</span>;
}
```

Callback Props 예:

```tsx
type SearchFormProps = {
  initialKeyword?: string;
  onSearch: (keyword: string) => void;
};

function SearchForm({ initialKeyword = "", onSearch }: SearchFormProps) {
  const [keyword, setKeyword] = useState(initialKeyword);

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    onSearch(keyword.trim());
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={keyword}
        onChange={(event) => setKeyword(event.target.value)}
      />
      <button type="submit">검색</button>
    </form>
  );
}
```

---

### [FAQ]

Q. Props Contract가 뭐야?
A. Component가 외부에서 받는 데이터, 설정값, 이벤트 함수의 계약이다.

Q. Required Props와 Optional Props는 어떻게 구분해?
A. Component가 정상 동작하는 데 반드시 필요한 값은 Required, 없어도 기본값으로 처리 가능한 값은 Optional로 둔다.

Q. Optional Props에는 기본값이 필요해?
A. 가능하면 기본값을 제공하는 것이 좋다. Component 내부 조건 분기를 줄이고 사용성을 높일 수 있다.

Q. Props Type은 어디에 두는 게 좋아?
A. Component 전용이면 같은 파일에 두고 여러 Component가 공유하면 types 파일로 분리한다.

---

## 2.2 Stable Props Shape

### [개념]

Stable Props Shape는 Props 구조를 예측 가능하고 일관되게 유지하는 설계 원칙이다.

Props 구조가 자주 바뀌거나 의미가 모호하면 Component 사용성과 유지보수성이 떨어진다.

---

### [핵심]

Stable Props Shape 원칙:

- Props 이름을 자주 바꾸지 않는다.
- 동일 목적의 Props는 일관된 이름을 사용한다.
- 모호한 data, item, info 이름을 남용하지 않는다.
- 같은 Component 계열은 Props 패턴을 맞춘다.
- 객체 Props와 개별 Props 전달 기준을 명확히 한다.
- Callback Props parameter를 안정적으로 유지한다.
- Optional Props 증가를 주의한다.
- Props 조합으로 불가능한 상태가 생기지 않게 한다.

---

### [실무]

나쁜 예:

```tsx
type Props = {
  data: any;
  flag: boolean;
  action: () => void;
};
```

문제:

- `data`가 무엇인지 알 수 없다.
- `flag`가 어떤 상태인지 알 수 없다.
- `action`이 어떤 행동인지 알 수 없다.
- TypeScript를 사용해도 Component Contract가 불명확하다.

좋은 예:

```tsx
type FestivalCardProps = {
  festival: FestivalSummary;
  isSelected: boolean;
  onSelect: (festivalId: number) => void;
};
```

개선점:

- `festival`은 도메인 데이터를 명확히 드러낸다.
- `isSelected`는 boolean 의미가 명확하다.
- `onSelect`는 외부 이벤트를 명확히 드러낸다.
- Callback parameter가 구체적이다.

---

### [FAQ]

Q. Stable Props Shape가 뭐야?
A. Props 구조와 이름을 예측 가능하고 일관되게 유지하는 설계 원칙이다.

Q. data라는 Props 이름은 안 좋아?
A. 항상 나쁜 것은 아니지만 의미가 모호하다. festival, user, items처럼 구체적인 이름이 더 좋다.

Q. Props 이름을 자주 바꾸면 왜 문제야?
A. Component 사용처가 많아질수록 수정 범위가 커지고 사용법 추적이 어려워진다.

Q. Props 구조가 불안정하면 어떤 문제가 생겨?
A. Component Contract가 흐려지고 재사용, 테스트, 리팩터링이 어려워진다.

---

# 3. Props Naming

## 3.1 Props Naming Rules

### [개념]

Props Naming은 Component 사용 의도와 데이터 의미를 드러내는 이름을 붙이는 규칙이다.

Props 이름은 Component를 사용하는 개발자와 Agent가 Component의 역할을 빠르게 이해할 수 있게 해야 한다.

---

### [핵심]

권장 Naming:

- 데이터 Props: `title`, `value`, `items`, `festival`, `user`
- Boolean Props: `isOpen`, `isActive`, `isSelected`, `disabled`, `loading`
- Callback Props: `onClick`, `onSubmit`, `onSelect`, `onChange`, `onClose`
- 내부 Handler: `handleClick`, `handleSubmit`, `handleSelect`, `handleChange`
- Render Props / ReactNode: `children`, `header`, `footer`, `actions`
- Variant Props: `variant`, `size`, `tone`
- ID Props: `festivalId`, `userId`, `postId`

금지 또는 주의:

- `data`
- `item`
- `info`
- `flag`
- `callback`
- `action`
- `func`
- `isCheck`
- `isData`

---

### [실무]

좋은 예:

```tsx
type ModalProps = {
  isOpen: boolean;
  title: string;
  onClose: () => void;
  children: React.ReactNode;
};
```

나쁜 예:

```tsx
type ModalProps = {
  open: boolean;
  data: string;
  close: () => void;
  child: React.ReactNode;
};
```

비교:

| 구분        | 좋은 이름    | 나쁜 이름              |
| ----------- | ------------ | ---------------------- |
| 열림 상태   | `isOpen`     | `open`, `flag`         |
| 제목        | `title`      | `data`                 |
| 닫기 이벤트 | `onClose`    | `close`, `action`      |
| 내용        | `children`   | `child`, `contentData` |
| 선택 상태   | `isSelected` | `selectedFlag`         |
| 변경 이벤트 | `onChange`   | `change`, `callback`   |

---

### [FAQ]

Q. Props 이름은 어떻게 지어?
A. 데이터 의미와 이벤트 의도가 드러나도록 구체적으로 짓는다.

Q. Callback Props 이름은 어떻게 지어?
A. 부모가 전달하는 이벤트 함수는 `onSelect`, `onSubmit`, `onClose`처럼 `on` prefix를 사용한다.

Q. 내부 함수 이름은 어떻게 지어?
A. Component 내부에서 이벤트를 처리하는 함수는 `handleSelect`, `handleSubmit`, `handleClose`처럼 `handle` prefix를 사용한다.

Q. Boolean Props 이름은 어떻게 지어?
A. `isOpen`, `isSelected`, `loading`, `disabled`처럼 true/false 의미가 명확해야 한다.

---

## 3.2 Boolean Props Naming

### [개념]

Boolean Props Naming은 true 또는 false 상태를 명확하게 표현하는 이름을 정하는 규칙이다.

Boolean Props는 이름만 보고 true일 때 어떤 상태인지 알 수 있어야 한다.

---

### [핵심]

권장 Boolean Props:

- `isOpen`
- `isActive`
- `isSelected`
- `isChecked`
- `isRequired`
- `disabled`
- `loading`
- `readOnly`
- `multiple`

주의할 이름:

- `flag`
- `check`
- `status`
- `state`
- `visible`
- `use`
- `has`

Boolean Props 원칙:

- true일 때 의미가 명확해야 한다.
- 부정형 이름을 남용하지 않는다.
- 상호 배타 상태는 boolean 여러 개보다 variant를 사용한다.
- boolean props가 많아지면 Component 책임을 재검토한다.

---

### [실무]

좋은 예:

```tsx
type DropdownProps = {
  isOpen: boolean;
  disabled?: boolean;
  onClose: () => void;
};
```

나쁜 예:

```tsx
type DropdownProps = {
  openFlag: boolean;
  use: boolean;
  state: boolean;
};
```

부정형 이름 주의:

```tsx
type ButtonProps = {
  isNotDisabled?: boolean;
};
```

문제:

- true일 때 의미가 헷갈린다.
- 조건문이 읽기 어려워진다.

개선:

```tsx
type ButtonProps = {
  disabled?: boolean;
};
```

---

### [FAQ]

Q. Boolean Props 이름에서 가장 중요한 건 뭐야?
A. true일 때 Component 상태가 명확하게 읽혀야 한다.

Q. disabled는 isDisabled보다 안 좋아?
A. 둘 다 가능하다. HTML 속성과 맞는 `disabled`, `readOnly`, `checked`는 그대로 사용해도 자연스럽다.

Q. flag라는 Props 이름은 왜 안 좋아?
A. 어떤 상태를 의미하는지 알 수 없어 Component Contract가 모호해진다.

Q. 부정형 Boolean Props는 피해야 해?
A. 가능하면 피하는 것이 좋다. 조건문과 사용법이 헷갈릴 수 있다.

---

# 4. Callback Props

## 4.1 Callback Props Rules

### [개념]

Callback Props는 자식 Component에서 발생한 이벤트나 결과를 부모 Component에 전달하기 위한 함수 Props다.

자식 Component는 부모 State를 직접 변경할 수 없으므로 Callback Props를 호출해 이벤트 발생 사실과 필요한 값을 부모에게 알린다.

---

### [핵심]

Callback Props 핵심:

- 자식 이벤트를 부모에게 알린다.
- 부모가 실제 상태 변경을 결정한다.
- 자식은 비즈니스 흐름을 강제하지 않는다.
- Callback Props 이름은 `on` prefix를 사용한다.
- 내부 Handler 이름은 `handle` prefix를 사용한다.
- Callback parameter는 최소한으로 전달한다.
- DOM Event를 그대로 외부로 넘길지 값만 넘길지 결정한다.
- UI Component는 결과를 강제하지 않고 이벤트만 알린다.

---

### [실무]

좋은 예:

```tsx
type FestivalCardProps = {
  festivalId: number;
  title: string;
  onSelect: (festivalId: number) => void;
};

function FestivalCard({ festivalId, title, onSelect }: FestivalCardProps) {
  return (
    <button type="button" onClick={() => onSelect(festivalId)}>
      {title}
    </button>
  );
}
```

부모 Component:

```tsx
function FestivalPage() {
  function handleSelectFestival(festivalId: number) {
    // 상세 페이지 이동 또는 선택 상태 변경
  }

  return (
    <FestivalCard
      festivalId={1}
      title="Spring Festival"
      onSelect={handleSelectFestival}
    />
  );
}
```

좋은 구조:

```text
FestivalCard
→ onSelect(festivalId) 호출
→ FestivalPage
→ handleSelectFestival 실행
→ 상태 변경 또는 페이지 이동
```

나쁜 구조:

```tsx
function FestivalCard({ festivalId }) {
  function handleClick() {
    window.location.href = `/festivals/${festivalId}`;
  }

  return <button onClick={handleClick}>상세 보기</button>;
}
```

문제:

- Card가 페이지 이동 정책을 직접 안다.
- 재사용성이 낮아진다.
- 테스트가 어려워진다.
- 부모가 동작을 제어하기 어렵다.

---

### [FAQ]

Q. Callback Props가 뭐야?
A. 자식 Component에서 발생한 이벤트를 부모 Component에 전달하기 위한 함수 Props다.

Q. 자식 Component가 부모 State를 직접 바꿀 수 있어?
A. 직접 바꿀 수 없다. 부모가 Callback Props를 전달하고 자식은 그 함수를 호출한다.

Q. Callback Props에는 어떤 값을 넘겨야 해?
A. 부모가 다음 작업을 수행하는 데 필요한 최소한의 값만 넘기는 것이 좋다.

Q. UI Component가 페이지 이동을 직접 해도 돼?
A. 권장하지 않는다. UI Component는 이벤트만 알리고 실제 이동은 부모나 라우팅 계층에서 처리하는 것이 좋다.

---

## 4.2 Callback Parameter Design

### [개념]

Callback Parameter Design은 Callback Props를 호출할 때 어떤 값을 부모에게 전달할지 정하는 설계다.

Callback parameter는 부모가 상태 변경, API 요청, 페이지 이동 등 다음 작업을 수행하는 데 필요한 최소 정보여야 한다.

---

### [핵심]

Callback Parameter 기준:

- 필요한 최소 값만 전달한다.
- DOM Event 전달을 남용하지 않는다.
- ID만 필요한 경우 객체 전체를 넘기지 않는다.
- 객체 전체가 필요한 경우 타입을 명확히 한다.
- Form submit은 정제된 value를 전달할 수 있다.
- List item 선택은 itemId를 전달하는 경우가 많다.
- UI Component는 도메인 객체를 몰라도 되게 설계한다.

---

### [실무]

ID 전달 예:

```tsx
type NotificationItemProps = {
  notificationId: number;
  title: string;
  onRead: (notificationId: number) => void;
};

function NotificationItem({
  notificationId,
  title,
  onRead,
}: NotificationItemProps) {
  return (
    <button type="button" onClick={() => onRead(notificationId)}>
      {title}
    </button>
  );
}
```

Form 값 전달 예:

```tsx
type LoginFormValues = {
  email: string;
  password: string;
};

type LoginFormProps = {
  onSubmit: (values: LoginFormValues) => void;
};
```

DOM Event 전달이 적합한 경우:

```tsx
type TextInputProps = {
  value: string;
  onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
};
```

값만 전달하는 방식:

```tsx
type TextInputProps = {
  value: string;
  onValueChange: (value: string) => void;
};
```

선택 기준:

```text
범용 Input
→ onChange(event) 가능

도메인 Form
→ onSubmit(values) 권장

List Item 선택
→ onSelect(id) 권장

도메인 객체 전체 필요
→ onSelect(item) 가능
```

---

### [FAQ]

Q. Callback Props에는 ID만 넘기는 게 좋아?
A. 부모가 ID만 필요하면 ID만 넘기는 것이 좋다. 객체 전체가 필요하면 타입을 명확히 해서 전달할 수 있다.

Q. onChange에는 event를 넘겨야 해?
A. 범용 Input은 event를 넘길 수 있고, 도메인 Component는 value만 넘기는 방식이 더 읽기 쉬울 수 있다.

Q. Callback parameter를 많이 넘기면 왜 문제야?
A. 부모와 자식 사이의 결합도가 높아지고 Component 재사용성이 떨어질 수 있다.

Q. onSubmit은 어떤 값을 넘기는 게 좋아?
A. Form 내부 값을 정제한 values 객체를 넘기는 방식이 일반적으로 좋다.

---

# 5. Boolean Props and Variant

## 5.1 Boolean Props Problem

### [개념]

Boolean Props Problem은 여러 boolean props가 조합되면서 불가능한 상태나 모호한 상태가 생기는 문제다.

Boolean Props는 단순한 on/off 상태에 적합하지만, 상호 배타적인 상태 표현에는 적합하지 않을 수 있다.

---

### [핵심]

Boolean Props 문제:

- 여러 상태가 동시에 true가 될 수 있다.
- 불가능한 상태가 생긴다.
- Component 동작 예측이 어려워진다.
- 조건부 렌더링이 복잡해진다.
- Props Contract가 불명확해진다.
- Component 테스트 케이스가 증가한다.

문제 상황:

- `success`, `warning`, `error`가 동시에 true
- `primary`, `secondary`, `danger`가 동시에 true
- `small`, `large`가 동시에 true
- `isOpen`, `isClosed`가 동시에 true

---

### [실무]

나쁜 예:

```tsx
type AlertProps = {
  success?: boolean;
  warning?: boolean;
  error?: boolean;
};
```

문제:

```tsx
<Alert success error />
```

위 코드는 성공 상태와 에러 상태가 동시에 true가 된다.

개선:

```tsx
type AlertVariant = "success" | "warning" | "error";

type AlertProps = {
  variant: AlertVariant;
};
```

사용:

```tsx
<Alert variant="success" />
<Alert variant="error" />
```

장점:

- 하나의 상태만 선택된다.
- 불가능한 상태를 줄인다.
- TypeScript가 오타를 막을 수 있다.
- Component 조건 분기가 단순해진다.

---

### [FAQ]

Q. Boolean Props가 많으면 왜 문제야?
A. 여러 boolean 값이 동시에 true가 되어 불가능한 상태가 생길 수 있기 때문이다.

Q. success, error 같은 상태는 boolean으로 둬도 돼?
A. 하나만 선택되어야 하는 상태라면 `variant: "success" | "error"` 같은 union 방식이 더 안전하다.

Q. Boolean Props는 언제 써도 돼?
A. `disabled`, `loading`, `isOpen`처럼 독립적인 true/false 상태에는 적합하다.

Q. Boolean Props를 모두 없애야 해?
A. 아니다. 상호 배타 상태나 변형 표현에 boolean 여러 개를 쓰는 것을 주의하면 된다.

---

## 5.2 Variant Props Rules

### [개념]

Variant Props는 Component의 시각적 또는 의미적 변형을 제한된 값으로 표현하는 Props다.

Variant는 여러 boolean props보다 안전하고 명확하게 Component 상태나 스타일 의도를 표현할 수 있다.

---

### [핵심]

Variant Props 사용 대상:

- Button variant
- Badge status
- Alert type
- Card tone
- Size
- Color intent
- Semantic status
- Toast type
- Message type

Variant Props 원칙:

- 가능한 값의 범위를 제한한다.
- 의미 기반 이름을 사용한다.
- boolean 여러 개보다 union type을 우선한다.
- variant와 size는 분리한다.
- variant가 너무 많아지면 Component 책임을 재검토한다.
- 스타일 이름보다 의미 이름을 우선한다.

---

### [실무]

Button Variant 예:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "danger";
  size?: "sm" | "md" | "lg";
  children: React.ReactNode;
};

function Button({ variant = "primary", size = "md", children }: ButtonProps) {
  return (
    <button className={`button button-${variant} button-${size}`}>
      {children}
    </button>
  );
}
```

Badge Variant 예:

```tsx
type BadgeProps = {
  label: string;
  status: "active" | "inactive" | "pending" | "blocked";
};

function Badge({ label, status }: BadgeProps) {
  return <span className={`badge badge-${status}`}>{label}</span>;
}
```

주의:

```text
variant가 10개 이상으로 늘어난다
→ Component 책임이 너무 넓은지 확인

variant 조합 조건이 복잡하다
→ 하위 Component 분리 검토

시각 이름만 사용한다
→ 의미 기반 이름으로 변경 검토
```

---

### [FAQ]

Q. Variant Props가 뭐야?
A. Component의 상태나 스타일 변형을 제한된 문자열 값으로 표현하는 Props다.

Q. variant는 왜 써?
A. Component 변형을 제한된 값으로 관리해 오타와 불가능한 상태를 줄이기 위해 사용한다.

Q. variant와 size는 분리해야 해?
A. 보통 분리하는 것이 좋다. variant는 의미나 의도, size는 크기를 나타내기 때문이다.

Q. variant가 많아지면 어떻게 해?
A. Component 책임이 과도한지 확인하고 하위 Component 분리나 설계 단순화를 검토한다.

---

# 6. Object Props vs Primitive Props

## 6.1 Object Props Rules

### [개념]

Object Props는 Component에 여러 필드를 가진 객체를 하나의 Props로 전달하는 방식이다.

도메인 Component에서는 객체 Props가 자연스러울 수 있지만, 공통 UI Component에서는 도메인 객체 의존성을 주의해야 한다.

---

### [핵심]

Object Props 적합 상황:

- 도메인 Card
- List Item
- Detail Section
- Profile Summary
- Review Item
- Notification Item
- 여러 필드가 항상 함께 사용되는 경우

Object Props 주의:

- Component가 API Response 구조에 직접 의존할 수 있다.
- 필요 없는 필드까지 전달될 수 있다.
- 재사용성이 낮아질 수 있다.
- 객체 구조 변경 시 영향 범위가 커질 수 있다.
- UI Component에는 도메인 객체 전달을 피한다.

---

### [실무]

도메인 Component에서 객체 Props 사용:

```tsx
type FestivalCardProps = {
  festival: FestivalSummary;
  onSelect: (festivalId: number) => void;
};

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

공통 UI Component에서 객체 Props 지양:

```tsx
type CardProps = {
  title: string;
  description?: string;
  imageUrl?: string | null;
  actions?: React.ReactNode;
};
```

비교:

| 기준      | Object Props     | Primitive Props                    |
| --------- | ---------------- | ---------------------------------- |
| 적합 대상 | 도메인 Component | 공통 UI Component                  |
| 장점      | 전달 간단        | 계약 명확                          |
| 단점      | 객체 구조 의존   | Props 개수 증가 가능               |
| 예        | `festival`       | `title`, `imageUrl`, `description` |

---

### [FAQ]

Q. Props는 객체 하나로 넘기는 게 좋아?
A. 도메인 Component라면 객체 Props가 자연스러울 수 있다. 공통 UI Component는 필요한 값만 명확히 받는 편이 좋다.

Q. API Response 객체를 그대로 Props로 넘겨도 돼?
A. 가능은 하지만 주의해야 한다. Component가 서버 응답 구조에 강하게 의존할 수 있다.

Q. UI Component에 도메인 객체를 넘겨도 돼?
A. 권장하지 않는다. UI Component는 도메인과 무관하게 필요한 primitive 값이나 ReactNode를 받는 것이 좋다.

Q. Object Props와 Primitive Props 중 뭐가 더 좋아?
A. Component 성격에 따라 다르다. 도메인 Feature Component는 Object Props, 공통 UI Component는 Primitive Props가 적합한 경우가 많다.

---

## 6.2 Props Mapping Rules

### [개념]

Props Mapping은 서버 응답 데이터나 도메인 객체를 Component가 사용하기 쉬운 Props 형태로 변환하는 작업이다.

Props Mapping은 API Response와 UI Component 사이의 결합도를 줄인다.

---

### [핵심]

Props Mapping 대상:

- API Response Field
- Domain Model
- UI Display Value
- Optional Value
- Null Handling
- Date Formatting
- Status Mapping
- Image URL Mapping
- Label Mapping

Props Mapping 원칙:

- API Response를 UI Component에 그대로 강제하지 않는다.
- Page, Container, Hook, Mapper 함수에서 화면용 데이터로 변환한다.
- null 값을 Component 내부에서 반복 처리하지 않도록 정리한다.
- 표시용 텍스트와 원본 데이터를 구분한다.

---

### [실무]

API Response 예:

```ts
type FestivalResponse = {
  id: number;
  name: string;
  img_url: string | null;
  sigungu: string;
  start_date: string;
};
```

UI Props 예:

```ts
type FestivalCardViewModel = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  regionName: string;
  periodText: string;
};
```

Mapping 함수:

```ts
function mapFestivalToCardViewModel(
  festival: FestivalResponse,
): FestivalCardViewModel {
  return {
    festivalId: festival.id,
    title: festival.name,
    imageUrl: festival.img_url,
    regionName: festival.sigungu,
    periodText: festival.start_date,
  };
}
```

Component 사용:

```tsx
function FestivalList({ festivals }: { festivals: FestivalCardViewModel[] }) {
  return (
    <section>
      {festivals.map((festival) => (
        <FestivalCard key={festival.festivalId} festival={festival} />
      ))}
    </section>
  );
}
```

---

### [FAQ]

Q. Props Mapping이 뭐야?
A. API Response나 도메인 객체를 Component가 사용하기 쉬운 Props 구조로 변환하는 작업이다.

Q. API Response를 그대로 UI에 넘기면 왜 문제야?
A. 서버 응답 필드 변경이 UI Component에 직접 영향을 주고 Component 재사용성이 떨어질 수 있다.

Q. Props Mapping은 어디서 해?
A. Page, Container, Custom Hook, API mapper 함수에서 처리할 수 있다.

Q. 표시용 데이터와 원본 데이터는 왜 구분해?
A. UI Component가 서버 구조나 비즈니스 원본 데이터에 과도하게 의존하지 않도록 하기 위해서다.

---

# 7. Children and ReactNode Props

## 7.1 Children Props Rules

### [개념]

Children Props는 Component 내부 내용을 외부에서 전달해 유연하게 조합하는 React Composition 방식이다.

children은 Layout, Card, Modal, Section, Button 같은 Wrapper Component에서 자주 사용한다.

---

### [핵심]

children 적합 대상:

- Layout
- Card
- Modal
- Panel
- Section
- Button
- FormGroup
- PageContainer
- Wrapper Component

children 원칙:

- 내부 구성이 유연해야 할 때 사용한다.
- 본문 영역을 외부에서 조합할 때 적합하다.
- 구조가 고정되어 있으면 explicit props가 더 나을 수 있다.
- TypeScript에서는 일반적으로 ReactNode를 사용한다.
- children이 너무 암묵적이면 slot-like props를 검토한다.

---

### [실무]

Card 예:

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
  <p>축제 설명</p>
  <Button>상세 보기</Button>
</Card>
```

children이 적합한 경우:

```text
Card 내부 내용이 화면마다 다르다
Modal 본문이 상황마다 다르다
Layout 내부에 Page를 넣어야 한다
Button 내부에 텍스트나 아이콘이 들어갈 수 있다
```

---

### [FAQ]

Q. children은 언제 써?
A. Component 내부 내용을 외부에서 자유롭게 조합해야 할 때 사용한다.

Q. children 타입은 뭐로 써?
A. TypeScript React에서는 일반적으로 `ReactNode`를 사용한다.

Q. children보다 explicit props가 나은 경우도 있어?
A. 있다. 구조가 고정되어 있고 필요한 데이터가 명확하면 explicit props가 더 읽기 쉽다.

Q. children을 쓰면 무조건 재사용성이 좋아져?
A. 아니다. 구조가 너무 암묵적이면 오히려 사용법이 어려워질 수 있다.

---

## 7.2 Slot-like Props Rules

### [개념]

Slot-like Props는 `header`, `footer`, `actions`처럼 특정 영역에 ReactNode를 전달해 Component를 조합하는 방식이다.

children보다 구조가 명확하고 Compound Component보다 단순한 조합 방식이다.

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

Slot-like Props 원칙:

- 특정 영역만 외부에서 커스터마이징할 때 사용한다.
- ReactNode Props 이름을 명확히 한다.
- slot props가 너무 많아지면 Component 책임을 재검토한다.
- 접근성 구조를 Component 내부에서 유지한다.
- children과 slot-like props 역할을 구분한다.

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

children vs slot-like props:

| 기준 | children       | slot-like props         |
| ---- | -------------- | ----------------------- |
| 역할 | 본문 전체 조합 | 특정 영역 조합          |
| 예   | Card 내용      | header, footer, actions |
| 장점 | 유연함         | 구조 명확               |
| 주의 | 암묵적 구조    | props 증가              |

---

### [FAQ]

Q. Slot-like Props가 뭐야?
A. header, footer, actions처럼 특정 영역에 ReactNode를 전달해 Component를 조합하는 방식이다.

Q. Slot-like Props는 언제 써?
A. Card, Modal, Panel처럼 특정 영역만 외부에서 커스터마이징하고 싶을 때 사용한다.

Q. children과 Slot-like Props 차이는?
A. children은 전체 본문을 전달하고 Slot-like Props는 header, action, footer 같은 특정 영역을 전달한다.

Q. Slot Props가 너무 많으면 어떻게 해?
A. Component 책임이 과도한지 확인하고 Component 분리나 Compound Component 패턴을 검토한다.

---

# 8. Props Drilling

## 8.1 Props Drilling Problem

### [개념]

Props Drilling은 여러 중간 Component를 거쳐 깊은 자식 Component에게 Props를 계속 전달하는 문제다.

중간 Component가 사용하지 않는 Props를 단순 전달만 한다면 Component 구조와 State Ownership을 재검토해야 한다.

---

### [핵심]

Props Drilling 문제:

- 중간 Component가 사용하지 않는 Props를 전달한다.
- Props 변경 시 여러 파일 수정이 필요하다.
- 데이터 흐름 추적이 어려워진다.
- Component 재사용성이 떨어진다.
- Component Boundary가 흐려진다.
- State 위치가 부적절할 수 있다.

Props Drilling 원인:

- State가 너무 위에 있다.
- Component 계층이 너무 깊다.
- Composition 구조가 부적절하다.
- Context 또는 전역 상태가 필요한 상황을 방치했다.
- Feature Boundary가 불명확하다.

---

### [실무]

문제 예:

```tsx
function App() {
  const [selectedId, setSelectedId] = useState<number | null>(null);

  return <Page selectedId={selectedId} onSelect={setSelectedId} />;
}

function Page({ selectedId, onSelect }) {
  return <Section selectedId={selectedId} onSelect={onSelect} />;
}

function Section({ selectedId, onSelect }) {
  return <FestivalList selectedId={selectedId} onSelect={onSelect} />;
}
```

문제:

```text
Page와 Section은 selectedId를 직접 사용하지 않는다.
중간 Component가 Props 전달만 담당한다.
Component 계층이 깊어질수록 수정 범위가 커진다.
```

해결 Flow:

```text
Trace Prop Path
→ Check Intermediate Usage
→ Review State Owner
→ Reduce Component Depth
→ Use Composition
→ Consider Context
→ Consider Global State
```

주의:

- Props Drilling이 항상 나쁜 것은 아니다.
- 1~2단계 Props 전달은 자연스럽다.
- 깊고 반복적이며 중간 Component가 사용하지 않을 때 문제가 된다.

---

### [FAQ]

Q. Props Drilling이 뭐야?
A. 여러 중간 Component를 거쳐 깊은 자식에게 Props를 계속 전달하는 문제다.

Q. Props Drilling은 무조건 나빠?
A. 아니다. 짧은 Props 전달은 자연스럽다. 깊고 반복되어 유지보수가 어려워질 때 문제가 된다.

Q. Props Drilling은 어떻게 해결해?
A. State 위치 조정, Component 구조 단순화, children composition, Context, 전역 상태를 순서대로 검토한다.

Q. Props Drilling 해결은 무조건 전역 상태야?
A. 아니다. State Ownership과 Component Composition을 먼저 검토하고 필요할 때 Context나 전역 상태를 사용한다.

---

## 8.2 Props Drilling Review Rules

### [개념]

Props Drilling Review는 Props 전달 경로를 추적해 불필요한 중간 전달과 State Ownership 문제를 찾는 검수 작업이다.

Review Agent는 Props가 어떤 Component에서 생성되고 어디까지 전달되는지 확인해야 한다.

---

### [핵심]

Review 기준:

- Props가 몇 단계 전달되는가?
- 중간 Component가 해당 Props를 직접 사용하는가?
- Props 이름이 전달 과정에서 일관되는가?
- Props 변경 시 수정 범위가 큰가?
- State Owner가 너무 위에 있는가?
- State Owner가 너무 아래에 있는가?
- children composition으로 줄일 수 있는가?
- Context가 적합한 공유 상태인가?
- 전역 상태가 필요한 상태인가?

---

### [실무]

검수 Checklist:

```md
- [ ] Props 전달 단계가 3단계 이상인가?
- [ ] 중간 Component가 Props를 사용하지 않고 전달만 하는가?
- [ ] Props 이름이 중간에서 바뀌어 추적이 어려운가?
- [ ] State Owner가 적절한가?
- [ ] Component 계층을 단순화할 수 있는가?
- [ ] children 또는 slot-like props로 구조 개선이 가능한가?
- [ ] Context가 더 적합한 공유 방식인가?
- [ ] 전역 상태로 올릴 만큼 여러 페이지에서 반복 사용되는가?
```

판단:

```text
1~2단계 전달
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

Q. Props Drilling은 몇 단계부터 문제야?
A. 절대 기준은 없지만 3단계 이상 반복되고 중간 Component가 사용하지 않으면 검토가 필요하다.

Q. 중간 Component가 Props를 전달만 하면 무조건 문제야?
A. 항상 문제는 아니다. 하지만 반복되거나 깊어지면 Component 구조 개선을 검토해야 한다.

Q. Props Drilling 검수에서 가장 먼저 볼 것은?
A. Props가 어디서 생성되고 어떤 Component를 거쳐 어디에서 실제 사용되는지 추적해야 한다.

Q. Context는 언제 검토해?
A. 여러 하위 Component가 같은 값을 반복적으로 필요로 하고 Props 전달이 깊어질 때 검토한다.

---

# 9. TypeScript Props Type

## 9.1 Props Type Design

### [개념]

Props Type Design은 TypeScript로 Component가 외부에서 받는 데이터와 Callback Props의 타입을 명확히 정의하는 작업이다.

Props Type은 Component Contract를 코드 수준에서 강제하고 문서화한다.

---

### [핵심]

Props Type 포함 대상:

- Required Props
- Optional Props
- Callback Props
- Children Type
- ReactNode
- Event Handler Type
- Variant Union
- Object Props Type
- Generic Props Basics

Props Type 원칙:

- Component 전용 Props Type은 같은 파일에 둔다.
- 여러 Component에서 공유하는 타입은 별도 types 파일로 분리한다.
- Callback parameter와 return type을 명확히 한다.
- children은 일반적으로 ReactNode를 사용한다.
- 불필요한 React.FC 강제는 피한다.
- any 사용을 피한다.
- Props Type 이름은 Component 이름과 맞춘다.

---

### [실무]

Props Type 예:

```tsx
import type { ReactNode } from "react";

type ModalProps = {
  isOpen: boolean;
  title: string;
  onClose: () => void;
  children: ReactNode;
};

function Modal({ isOpen, title, onClose, children }: ModalProps) {
  if (!isOpen) {
    return null;
  }

  return (
    <section role="dialog" aria-modal="true" aria-labelledby="modal-title">
      <h2 id="modal-title">{title}</h2>
      <button type="button" onClick={onClose}>
        닫기
      </button>
      {children}
    </section>
  );
}
```

Callback Type 예:

```tsx
type ReviewFormValues = {
  rating: number;
  content: string;
};

type ReviewFormProps = {
  onSubmit: (values: ReviewFormValues) => void;
  onCancel?: () => void;
};
```

Variant Type 예:

```tsx
type AlertVariant = "success" | "warning" | "error";

type AlertProps = {
  variant: AlertVariant;
  message: string;
};
```

---

### [FAQ]

Q. Props Type은 왜 중요해?
A. Component가 외부에서 요구하는 데이터 구조를 명확히 해 잘못된 사용을 줄인다.

Q. Props Type 이름은 어떻게 지어?
A. Component 이름 뒤에 Props를 붙인다. 예를 들어 ModalProps, FestivalCardProps처럼 작성한다.

Q. React.FC를 꼭 써야 해?
A. 필수는 아니다. 프로젝트 컨벤션에 따라 사용할 수 있지만 불필요하게 강제하지 않는다.

Q. any Props는 써도 돼?
A. 권장하지 않는다. Props Contract가 무너지고 TypeScript의 검증 장점이 사라진다.

---

## 9.2 Generic Props Basics

### [개념]

Generic Props는 여러 데이터 타입에 재사용 가능한 Component를 만들 때 사용하는 TypeScript Props 설계 방식이다.

Generic Props는 List, Select, Table처럼 데이터 타입은 다르지만 렌더링 구조가 반복되는 Component에 적합하다.

---

### [핵심]

Generic Props 적합 대상:

- List
- Select
- Table
- Combobox
- Option List
- Data Renderer

Generic Props 원칙:

- 실제 반복 패턴이 있을 때 사용한다.
- 너무 추상적인 Generic Component는 피한다.
- renderItem, getKey 같은 명확한 Props를 제공한다.
- Generic이 사용성을 해치면 명시적 Component가 더 낫다.
- Foundation 단계에서는 단순 Generic만 사용한다.

---

### [실무]

List Generic Props 예:

```tsx
type ListProps<T> = {
  items: T[];
  getKey: (item: T) => string | number;
  renderItem: (item: T) => React.ReactNode;
};

function List<T>({ items, getKey, renderItem }: ListProps<T>) {
  return (
    <ul>
      {items.map((item) => (
        <li key={getKey(item)}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}
```

사용:

```tsx
<List
  items={festivals}
  getKey={(festival) => festival.festivalId}
  renderItem={(festival) => <FestivalCard festival={festival} />}
/>
```

주의:

```text
Generic이 Component 사용법을 어렵게 만든다
→ 명시적 Component 검토

Props가 너무 많다
→ Component 책임 재검토

렌더링 구조가 도메인마다 다르다
→ 공통 Generic보다 도메인 Component 유지
```

---

### [FAQ]

Q. Generic Props는 언제 써?
A. List, Select, Table처럼 데이터 타입은 다르지만 렌더링 구조가 반복될 때 사용한다.

Q. Generic Component를 많이 만들면 좋아?
A. 아니다. 과도한 Generic은 사용성과 가독성을 떨어뜨릴 수 있다.

Q. renderItem Props는 뭐야?
A. Generic Component가 각 item을 어떻게 렌더링할지 외부에서 전달받는 함수 Props다.

Q. Generic이 어렵다면 어떻게 해?
A. 명시적인 도메인 Component를 유지하는 것이 더 나을 수 있다.

---

# 10. Props Design Anti Patterns

## 10.1 Unclear Props Problem

### [개념]

Unclear Props Problem은 Props 이름이나 구조가 모호해서 Component 사용 의도를 알기 어려운 문제다.

Props가 모호하면 Component Responsibility와 Props Contract가 함께 흐려진다.

---

### [핵심]

문제:

- `data`, `item`, `info` 같은 모호한 이름
- `flag`, `status`, `state` 같은 의미 불명확 boolean
- `action`, `callback`, `func` 같은 모호한 함수 이름
- Optional Props가 너무 많음
- Props 조합으로 불가능한 상태 발생
- Props Type이 `any`로 작성됨
- 도메인 객체를 UI Component에 무분별하게 전달

해결:

- Props 이름 구체화
- Props Type 정의
- Callback Props `on` prefix 사용
- Boolean Props 의미 명확화
- Boolean 여러 개 대신 variant 사용
- Component 책임 재정의
- 필요한 값만 전달

---

### [실무]

나쁜 예:

```tsx
type Props = {
  data: any;
  flag: boolean;
  action: () => void;
};
```

좋은 예:

```tsx
type FestivalCardProps = {
  festival: FestivalSummary;
  isSelected: boolean;
  onSelect: (festivalId: number) => void;
};
```

Review 기준:

```text
Props 이름만 보고 의미를 알 수 있는가?
Callback이 어떤 이벤트인지 알 수 있는가?
Boolean true 상태가 명확한가?
Props Type이 Component Contract 역할을 하는가?
```

---

### [FAQ]

Q. Unclear Props Problem이 뭐야?
A. Props 이름이나 구조가 모호해서 Component 사용 의도를 알기 어려운 문제다.

Q. action이라는 Props 이름은 왜 안 좋아?
A. 어떤 동작을 의미하는지 알 수 없다. onSubmit, onClose, onSelect처럼 구체적인 이름이 좋다.

Q. Props 이름이 모호하면 어떻게 고쳐?
A. 데이터 의미, 이벤트 의도, boolean 상태가 드러나도록 이름을 구체화한다.

Q. Props Type이 any면 왜 문제야?
A. Component Contract가 사라져 잘못된 Props 전달을 TypeScript가 막을 수 없다.

---

## 10.2 Too Many Props Problem

### [개념]

Too Many Props Problem은 하나의 Component가 너무 많은 Props를 받아 사용법이 복잡해지는 문제다.

Props가 너무 많으면 Component 책임이 과도하거나 Component Boundary가 잘못되었을 가능성이 있다.

---

### [핵심]

Too Many Props 원인:

- Component 책임 과다
- 여러 UI 영역을 하나의 Component가 담당
- Container와 Presentational 책임 혼합
- State를 너무 위에서 관리
- Variant 조합 과다
- Optional Props 남용
- 재사용성을 과도하게 예측

문제:

- Component 사용법이 어렵다.
- Props 조합 테스트가 어려워진다.
- 불가능한 상태가 생긴다.
- 유지보수성이 낮아진다.
- 재사용성이 오히려 떨어진다.

해결:

- Component 분리
- Props Grouping 검토
- children / slot-like props 검토
- variant 단순화
- State Ownership 재검토
- 과도한 재사용성 제거

---

### [실무]

문제 예:

```tsx
type CardProps = {
  title: string;
  subtitle?: string;
  imageUrl?: string;
  footerText?: string;
  buttonText?: string;
  onButtonClick?: () => void;
  showBadge?: boolean;
  badgeText?: string;
  badgeColor?: string;
  isLoading?: boolean;
  isError?: boolean;
  isSelected?: boolean;
  isDisabled?: boolean;
};
```

개선 방향:

```tsx
type CardProps = {
  title: string;
  subtitle?: string;
  imageUrl?: string | null;
  headerAction?: React.ReactNode;
  footer?: React.ReactNode;
  children?: React.ReactNode;
};
```

또는 도메인 Component 분리:

```text
Generic Card
→ 기본 레이아웃만 담당

FestivalCard
→ 축제 카드 도메인 표시 담당

SelectableCard
→ 선택 가능한 카드 담당
```

판단 기준:

```text
Props가 8개 이상이다
→ Component 책임 검토

Optional Props가 대부분이다
→ Component 변형 과다 의심

Boolean Props가 많다
→ variant 또는 Component 분리 검토

Props 조합 설명이 어렵다
→ Component Boundary 재검토
```

---

### [FAQ]

Q. Props가 많으면 무조건 나쁜 설계야?
A. 무조건은 아니지만 Component 책임이 과도하거나 Boundary가 잘못되었을 가능성이 높다.

Q. Props가 너무 많을 때 어떻게 해결해?
A. Component 분리, children, slot-like props, variant 단순화, State Ownership 재검토를 순서대로 검토한다.

Q. Optional Props가 많으면 왜 문제야?
A. Component 변형이 과도해지고 어떤 조합이 유효한지 알기 어려워질 수 있다.

Q. Props Grouping은 언제 해?
A. 관련 Props가 항상 함께 움직이고 의미 있는 그룹을 만들 수 있을 때 검토한다.

---

# 11. Props Design Review Checklist

## 11.1 Props Design Checklist

### [개념]

Props Design Checklist는 Component Props가 명확하고 안정적인지 검수하기 위한 기준이다.

Frontend Agent와 Review Agent는 Component 코드 생성 전후에 Props Contract를 검토해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Props 이름이 구체적인가?
- [ ] Props Contract가 명확한가?
- [ ] Required Props와 Optional Props가 구분되는가?
- [ ] Optional Props에 기본값이 필요한가?
- [ ] Callback Props가 `on` prefix를 사용하는가?
- [ ] 내부 Handler가 `handle` prefix를 사용하는가?
- [ ] Callback parameter가 최소한인가?
- [ ] Boolean Props true 의미가 명확한가?
- [ ] 상호 배타 상태를 boolean 여러 개로 표현하지 않았는가?
- [ ] variant union type이 필요한가?
- [ ] Props Type이 Component Contract 역할을 하는가?
- [ ] any Props를 사용하지 않았는가?
- [ ] UI Component가 도메인 객체에 의존하지 않는가?
- [ ] API Response를 UI Component에 그대로 강제하지 않는가?
- [ ] children 사용이 적절한가?
- [ ] slot-like props 사용이 적절한가?
- [ ] Props 개수가 과도하지 않은가?
- [ ] Props Drilling이 과도하지 않은가?
- [ ] Props 변경 시 수정 범위가 과도하지 않은가?
```

---

### [실무]

Review Flow:

```text
Component Review
→ Props Naming Check
→ Required / Optional Check
→ Callback Props Check
→ Boolean / Variant Check
→ Props Type Check
→ Props Drilling Check
→ Anti Pattern Check
```

치명적 문제:

```text
- Props Type이 any
- data, item, flag, action 남용
- UI Component에서 도메인 객체 직접 의존
- boolean props 여러 개로 불가능한 상태 발생
- Callback Props 이름이 모호함
- Props가 너무 많아 Component 사용법이 불명확함
```

---

### [FAQ]

Q. Props Design 검수에서 가장 중요한 것은?
A. Props 이름, Props Contract, Callback Props, Boolean Props, Props Type, Props Drilling 여부다.

Q. 치명적인 Props 설계 문제는 뭐야?
A. any Props, 모호한 Props 이름, boolean 조합 문제, 과도한 Props 개수, UI Component의 도메인 의존이다.

Q. Review Agent는 Props에서 뭘 먼저 봐야 해?
A. Props 이름만 보고 Component 사용 의도와 데이터 의미를 알 수 있는지 먼저 확인해야 한다.

Q. Props Design Checklist는 언제 사용해?
A. Component 생성 전 설계 단계와 코드 작성 후 Review 단계에서 모두 사용한다.

---

# 12. Agent Output Rules

## 12.1 Frontend Agent Props Design Output

### [개념]

Frontend Agent는 Component를 생성하기 전에 Props Contract를 명확히 정의해야 한다.

Props Design Output은 Component 이름, 책임, Required Props, Optional Props, Callback Props, State Owner를 함께 제시해야 한다.

---

### [핵심]

Frontend Agent Props Design 출력 항목:

- Component Name
- Component Responsibility
- Required Props
- Optional Props
- Callback Props
- Children Props
- Variant Props
- State Owner
- Props Type
- Props Drilling Risk
- Anti Pattern Review

---

### [실무]

출력 예:

```text
Component: FestivalCard

Responsibility:
- 축제 단일 항목 요약 표시
- 선택 이벤트를 부모에게 전달

Required Props:
- festival: FestivalSummary
- onSelect: (festivalId: number) => void

Optional Props:
- isSelected?: boolean

State Owner:
- selectedFestivalId는 FestivalList 또는 FestivalPage가 소유

Props Drilling Risk:
- FestivalCard까지 1단계 전달이면 허용
- 3단계 이상 전달되면 구조 재검토

Anti Pattern Review:
- API 호출 없음
- 페이지 이동 직접 수행 없음
- boolean props 과다 없음
- Props 이름 명확
```

Props Type 예:

```tsx
type FestivalCardProps = {
  festival: FestivalSummary;
  isSelected?: boolean;
  onSelect: (festivalId: number) => void;
};
```

---

### [FAQ]

Q. Frontend Agent는 Props를 언제 설계해야 해?
A. Component 코드를 생성하기 전에 Component Responsibility와 함께 Props Contract를 먼저 설계해야 한다.

Q. Props Design Output에는 무엇이 포함돼야 해?
A. Component 이름, 책임, Required Props, Optional Props, Callback Props, State Owner, Props Type이 포함되어야 한다.

Q. Props 설계 없이 코드를 생성하면 뭐가 문제야?
A. Component 사용법이 모호해지고 State Ownership, Callback 흐름, Props Drilling 문제가 생기기 쉽다.

Q. Review Agent는 Props Design Output에서 뭘 봐야 해?
A. Props 이름이 명확한지, Callback Props가 적절한지, Boolean Props 문제가 없는지, Props Type이 안정적인지 확인해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. React Props Design이 뭐야?
A. Component가 외부에서 어떤 데이터와 이벤트 함수를 받을지 정하는 설계 작업이다.

Q. Props Contract가 뭐야?
A. Component가 외부에서 받는 데이터, 설정값, 이벤트 함수의 계약이다.

Q. Props는 왜 Component Contract라고 해?
A. 부모가 자식 Component를 사용할 때 어떤 값을 제공해야 하는지 정의하는 외부 계약이기 때문이다.

Q. Props는 자식 Component에서 수정해도 돼?
A. 안 된다. Props는 읽기 전용으로 다루고 변경이 필요하면 부모에게 Callback Props로 알린다.

Q. Props 이름은 어떻게 지어?
A. 데이터 의미와 이벤트 의도가 드러나도록 구체적으로 짓는다.

Q. data라는 Props 이름은 안 좋아?
A. 항상 나쁜 것은 아니지만 의미가 모호하다. festival, user, items처럼 구체적인 이름이 더 좋다.

Q. Callback Props는 어떻게 이름 지어?
A. 부모가 전달하는 이벤트 함수는 onSelect, onSubmit, onClose처럼 on prefix를 사용한다.

Q. 내부 Handler는 어떻게 이름 지어?
A. Component 내부 이벤트 처리 함수는 handleSelect, handleSubmit, handleClose처럼 handle prefix를 사용한다.

Q. Boolean Props 이름은 어떻게 지어?
A. isOpen, isSelected, loading, disabled처럼 true/false 의미가 명확해야 한다.

Q. flag라는 Props 이름은 왜 안 좋아?
A. 어떤 상태를 의미하는지 알 수 없어 Component Contract가 모호해진다.

Q. Callback Props가 뭐야?
A. 자식 Component에서 발생한 이벤트를 부모 Component에 전달하기 위한 함수 Props다.

Q. 자식 Component가 부모 State를 직접 바꿀 수 있어?
A. 직접 바꿀 수 없다. 부모가 Callback Props를 전달하고 자식은 그 함수를 호출한다.

Q. Callback Props에는 어떤 값을 넘겨야 해?
A. 부모가 다음 작업을 수행하는 데 필요한 최소한의 값만 넘기는 것이 좋다.

Q. onChange에는 event를 넘겨야 해?
A. 범용 Input은 event를 넘길 수 있고 도메인 Component는 value만 넘기는 방식이 더 읽기 쉬울 수 있다.

Q. onSubmit은 어떤 값을 넘기는 게 좋아?
A. Form 내부 값을 정제한 values 객체를 넘기는 방식이 일반적으로 좋다.

Q. Boolean Props가 많으면 왜 문제야?
A. 여러 boolean 값이 동시에 true가 되어 불가능한 상태가 생길 수 있기 때문이다.

Q. Boolean Props 대신 뭘 써?
A. 상호 배타적인 상태라면 variant union type을 사용한다.

Q. Variant Props가 뭐야?
A. Component의 상태나 스타일 변형을 제한된 문자열 값으로 표현하는 Props다.

Q. variant는 왜 써?
A. Component 변형을 제한된 값으로 관리해 오타와 불가능한 상태를 줄이기 위해 사용한다.

Q. variant와 size는 분리해야 해?
A. 보통 분리하는 것이 좋다. variant는 의미나 의도, size는 크기를 나타내기 때문이다.

Q. Props는 객체 하나로 넘기는 게 좋아?
A. 도메인 Component라면 객체 Props가 자연스러울 수 있다. 공통 UI Component는 필요한 값만 명확히 받는 편이 좋다.

Q. API Response 객체를 그대로 Props로 넘겨도 돼?
A. 가능은 하지만 Component가 서버 응답 구조에 강하게 의존할 수 있으므로 주의해야 한다.

Q. UI Component에 도메인 객체를 넘겨도 돼?
A. 권장하지 않는다. UI Component는 도메인과 무관하게 필요한 primitive 값이나 ReactNode를 받는 것이 좋다.

Q. Props Mapping이 뭐야?
A. API Response나 도메인 객체를 Component가 사용하기 쉬운 Props 구조로 변환하는 작업이다.

Q. API Response를 그대로 UI에 넘기면 왜 문제야?
A. 서버 응답 필드 변경이 UI Component에 직접 영향을 주고 Component 재사용성이 떨어질 수 있다.

Q. children은 언제 써?
A. Component 내부 내용을 외부에서 자유롭게 조합해야 할 때 사용한다.

Q. children 타입은 뭐로 써?
A. TypeScript React에서는 일반적으로 ReactNode를 사용한다.

Q. Slot-like Props가 뭐야?
A. header, footer, actions처럼 특정 영역에 ReactNode를 전달해 Component를 조합하는 방식이다.

Q. children과 Slot-like Props 차이는?
A. children은 전체 본문을 전달하고 Slot-like Props는 header, action, footer 같은 특정 영역을 전달한다.

Q. Props Drilling이 뭐야?
A. 여러 중간 Component를 거쳐 깊은 자식에게 Props를 계속 전달하는 문제다.

Q. Props Drilling은 무조건 나빠?
A. 아니다. 짧은 Props 전달은 자연스럽다. 깊고 반복되어 유지보수가 어려워질 때 문제가 된다.

Q. Props Drilling은 어떻게 해결해?
A. State 위치 조정, Component 구조 단순화, children composition, Context, 전역 상태를 순서대로 검토한다.

Q. Props Type은 왜 중요해?
A. Component가 외부에서 요구하는 데이터 구조를 명확히 해 잘못된 사용을 줄인다.

Q. Props Type 이름은 어떻게 지어?
A. Component 이름 뒤에 Props를 붙인다. 예를 들어 ModalProps, FestivalCardProps처럼 작성한다.

Q. React.FC를 꼭 써야 해?
A. 필수는 아니다. 프로젝트 컨벤션에 따라 사용할 수 있지만 불필요하게 강제하지 않는다.

Q. any Props는 써도 돼?
A. 권장하지 않는다. Props Contract가 무너지고 TypeScript의 검증 장점이 사라진다.

Q. Generic Props는 언제 써?
A. List, Select, Table처럼 데이터 타입은 다르지만 렌더링 구조가 반복될 때 사용한다.

Q. Unclear Props Problem이 뭐야?
A. Props 이름이나 구조가 모호해서 Component 사용 의도를 알기 어려운 문제다.

Q. Too Many Props Problem이 뭐야?
A. 하나의 Component가 너무 많은 Props를 받아 사용법이 복잡해지는 문제다.

Q. Props가 너무 많을 때 어떻게 해결해?
A. Component 분리, children, slot-like props, variant 단순화, State Ownership 재검토를 순서대로 검토한다.

Q. Props Design 검수에서 가장 중요한 것은?
A. Props 이름, Props Contract, Callback Props, Boolean Props, Props Type, Props Drilling 여부다.

Q. React Component Design Part02의 핵심은 뭐야?
A. Props를 Component Contract로 설계하고 명확한 이름, Callback Props, Variant, Props Type으로 안정적인 Component 사용법을 만드는 것이다.
