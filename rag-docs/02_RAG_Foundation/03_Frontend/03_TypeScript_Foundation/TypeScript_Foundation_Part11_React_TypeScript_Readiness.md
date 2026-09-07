# TypeScript Foundation Part11 - React TypeScript Readiness

---

# 1. React TypeScript Overview

## 1.1 React TypeScript Readiness Definition

### [개념]

React TypeScript Readiness는 React Project에서 TypeScript를 안정적으로 사용하기 위한 기본 Type 기준이다.

React TypeScript는 Component Props, State, Event Handler, Form Data, API Response, Custom Hook Return Type을 명확히 정의하는 데 사용된다.

```text
API Response Type
→ Component Props Type
→ State Type
→ Event Handler Type
→ UI Rendering
```

React TypeScript Readiness는 React 심화 문서가 아니라 React Core 진입 전 TypeScript 기반을 정리하는 문서다.

---

### [핵심]

React TypeScript 주요 대상:

- Component Props Type
- React State Type
- React Event Type
- Form Data Type
- Callback Props Type
- Children Type
- Custom Hook Return Type
- API Response Type 연결
- Nullable State
- Empty Array State
- Async Status State

핵심 원칙:

- Props는 Component 입력 계약이다.
- State는 UI 상태 구조다.
- Event Type은 React Synthetic Event 기준이다.
- API Response Type과 Props Type은 항상 같지 않다.
- Form input value는 대부분 string이다.
- nullable 값은 Type에 반영한다.
- empty array state는 element Type을 명시한다.
- any Event, any Props, any State 지양.

---

### [실무]

2026 Frontend 실무 기준에서 React TypeScript는 아래 문제를 줄인다.

- 잘못된 Props 전달
- nullable data 직접 접근
- Event target Type 오류
- input number value 오해
- API Response 구조 오해
- 빈 배열 State Type 추론 실패
- Callback Props parameter 불일치
- Loading / Error 상태 조합 오류

기본 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

type FestivalCardProps = {
  festival: FestivalInfoResponse;
  onSelect: (festivalId: number) => void;
};

function FestivalCard({ festival, onSelect }: FestivalCardProps) {
  return null;
}
```

실무 기준:

- Component Props Type을 명확히 작성
- API Response nullable field를 UI에서 처리
- Event Handler Type을 any로 두지 않음
- State 초기값이 null 또는 빈 배열이면 Type 명시
- Props / State / API Type 역할 구분

---

### [FAQ]

Q. React TypeScript Readiness가 뭐야?
A. React에서 Props, State, Event, Form, API Type을 안정적으로 사용하기 위한 기본 Type 기준이다.

Q. React TypeScript 문서는 React 심화 문서야?
A. 아니다. React Core 이전에 필요한 TypeScript 준비 문서다.

Q. React에서 TypeScript가 가장 많이 쓰이는 곳은?
A. Props Type, State Type, Event Handler Type, Form Data Type, API Response Type이다.

Q. React에서 any를 써도 돼?
A. 가능은 하지만 Props, State, Event, API에는 구체적 Type을 쓰는 것이 좋다.

---

# 2. Component Props Type

## 2.1 Props Type Definition

### [개념]

Props Type은 React Component가 외부에서 받는 데이터와 callback의 구조를 정의하는 Type이다.

Props Type은 Component 입력 계약이다.

```typescript
type ButtonProps = {
  label: string;
  onClick: () => void;
};
```

Props Type을 사용하면 Component 호출 시 잘못된 props 전달을 Compile Time에 감지할 수 있다.

---

### [핵심]

Props Type 구성 요소:

- required props
- optional props
- nullable props
- callback props
- children
- list props
- object props
- union props
- event handler props

Props Type 작성 기준:

- Component 이름 + `Props` suffix 사용
- 필요한 값만 props로 전달
- optional props는 기본값 처리
- nullable props는 fallback UI 처리
- callback props는 parameter와 return Type 명시
- `any` props 금지

---

### [실무]

기본 Props 예:

```typescript
type FestivalCardProps = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  onSelect: (festivalId: number) => void;
};

function FestivalCard({
  festivalId,
  title,
  imageUrl,
  onSelect,
}: FestivalCardProps) {
  return null;
}
```

Object Props 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

type FestivalCardProps = {
  festival: FestivalInfoResponse;
  onSelect: (festivalId: number) => void;
};
```

실무 기준:

- Props Type은 Component 가까이에 둘 수 있음
- 여러 Component에서 공유하면 별도 Type 파일로 분리
- API Response 객체를 그대로 props로 넘길 수 있지만 UI 전용 ViewModel도 가능
- callback props 이름은 `onSelect`, `onClick`, `onSubmit`처럼 `on` prefix 권장
- Props Type 이름은 검색 가능하게 작성

---

### [FAQ]

Q. Props Type은 뭐야?
A. Component가 외부에서 받는 데이터와 callback 구조를 정의하는 Type이다.

Q. Props Type 이름은 어떻게 지어?
A. 일반적으로 Component 이름에 `Props` suffix를 붙인다. 예: `FestivalCardProps`.

Q. API Response Type을 그대로 Props로 써도 돼?
A. 가능하지만 화면 전용 가공이 필요하면 ViewModel Type을 Props로 사용하는 것이 좋다.

---

## 2.2 Required Props

### [개념]

Required Props는 Component가 렌더링되기 위해 반드시 받아야 하는 props다.

Props Type에서 `?`가 없는 property는 Required Props다.

```typescript
type UserProfileProps = {
  userId: number;
  nickname: string;
};
```

---

### [핵심]

Required Props 사용 기준:

- Component 렌더링 필수 데이터
- callback 필수 동작
- id 값
- title 값
- data object
- route-linked data
- UI에서 반드시 필요한 label

주의:

- 실제로 없을 수 있는 API field를 required non-null로 단정하지 않음
- optional data loading 상태와 구분
- nullable API field는 Props Type에 반영
- parent component가 반드시 넘겨야 함

---

### [실무]

필수 Props 예:

```typescript
type ReviewCardProps = {
  reviewId: number;
  rating: number;
  content: string;
};

function ReviewCard(props: ReviewCardProps) {
  return null;
}
```

필수 Callback 예:

```typescript
type FestivalListItemProps = {
  festivalId: number;
  title: string;
  onSelect: (festivalId: number) => void;
};
```

실무 기준:

- 화면 표시 필수 값은 Required Props로 정의
- 사용자 행동 처리에 필수인 callback도 Required Props 가능
- 데이터 로딩 전에는 Component를 렌더링하지 않거나 nullable props를 명시
- required와 nullable은 다르다.
- `title: string | null`은 required property지만 값이 null 가능하다.

---

### [FAQ]

Q. Required Props는 뭐야?
A. Component 사용 시 반드시 전달해야 하는 props다.

Q. Props에 ?가 없으면 required야?
A. 그렇다. TypeScript Object Type에서 ?가 없는 property는 필수다.

Q. required props와 nullable props는 같아?
A. 아니다. required는 property 존재 여부이고 nullable은 값이 null일 수 있다는 의미다.

---

## 2.3 Optional Props

### [개념]

Optional Props는 Component 사용 시 생략할 수 있는 props다.

property 이름 뒤에 `?`를 붙여 작성한다.

```typescript
type EmptyStateProps = {
  message?: string;
};
```

Optional Props는 기본적으로 `T | undefined` 가능성을 가진다.

---

### [핵심]

Optional Props 사용 영역:

- optional message
- optional className
- optional disabled
- optional callback
- optional icon
- optional placeholder
- optional variant
- optional children

주의:

- optional은 null과 다름
- Optional Props는 default value 처리 권장
- optional callback은 `?.()`로 호출
- 너무 많은 optional props는 Component 책임 과다 신호일 수 있음

---

### [실무]

Default Value 예:

```typescript
type EmptyStateProps = {
  message?: string;
};

function EmptyState({ message = "데이터가 없습니다." }: EmptyStateProps) {
  return null;
}
```

Optional Callback 예:

```typescript
type ModalProps = {
  open: boolean;
  onClose?: () => void;
};

function closeModal(props: ModalProps): void {
  props.onClose?.();
}
```

Optional ClassName 예:

```typescript
type CardProps = {
  title: string;
  className?: string;
};
```

실무 기준:

- optional props에는 default value 또는 fallback 처리
- optional callback은 optional chaining 사용
- optional과 nullable 의미를 혼동하지 않음
- optional props가 많으면 Component 분리 검토
- Props Type에 undefined 가능성을 고려

---

### [FAQ]

Q. Optional Props는 어떻게 써?
A. property 이름 뒤에 `?`를 붙인다. 예: `message?: string`.

Q. Optional Props는 null도 허용해?
A. 아니다. 기본적으로 생략 또는 undefined 가능성을 의미한다. null도 허용하려면 `string | null`을 추가해야 한다.

Q. Optional Callback은 어떻게 호출해?
A. `onClose?.()`처럼 optional chaining으로 안전하게 호출한다.

---

## 2.4 Nullable Props

### [개념]

Nullable Props는 props property는 존재하지만 값이 null일 수 있음을 표현한다.

```typescript
type AvatarProps = {
  imageUrl: string | null;
};
```

Nullable Props는 API nullable field를 UI에 전달할 때 자주 사용된다.

---

### [핵심]

Nullable Props 사용 영역:

- profileImageUrl
- imageUrl
- averageRating
- selectedUser
- currentUser
- description
- optional relation data

주의:

- nullable은 optional과 다름
- null 가능 값은 fallback UI 필요
- direct property access 주의
- `as string`으로 null 제거 금지
- API nullable field를 정확히 반영

---

### [실무]

Image Fallback 예:

```typescript
type AvatarProps = {
  imageUrl: string | null;
};

function getAvatarImageUrl({ imageUrl }: AvatarProps): string {
  return imageUrl ?? "/default-avatar.png";
}
```

Rating Fallback 예:

```typescript
type RatingTextProps = {
  averageRating: number | null;
};

function getRatingText({ averageRating }: RatingTextProps): string {
  return averageRating !== null ? averageRating.toFixed(1) : "평점 없음";
}
```

실무 기준:

- null 가능 API field는 Props Type에 반영
- UI fallback 처리
- null check 없이 method 호출 금지
- nullable props가 많으면 ViewModel에서 fallback 처리 가능
- Mapping Function으로 null 제거 후 UI에 전달 가능

---

### [FAQ]

Q. Nullable Props는 뭐야?
A. props property는 존재하지만 값이 null일 수 있는 Props다.

Q. imageUrl이 null 가능하면 어떻게 Type을 써?
A. `imageUrl: string | null`로 작성한다.

Q. nullable props를 UI에서 어떻게 처리해?
A. null check, `??`, optional chaining, fallback UI를 사용한다.

---

## 2.5 Children Type

### [개념]

Children Type은 Component가 내부에 JSX children을 받을 수 있는지 정의하는 Type이다.

React에서는 `ReactNode`를 사용해 다양한 children 값을 표현할 수 있다.

```typescript
import type { ReactNode } from "react";

type LayoutProps = {
  children: ReactNode;
};
```

---

### [핵심]

Children Type 주요 선택:

- `ReactNode`
- optional children
- required children
- render props
- JSX.Element

ReactNode 포함 가능 값:

- string
- number
- JSX element
- fragment
- array
- null
- undefined
- boolean

주의:

- children이 필수인지 optional인지 명확히 함
- 모든 Component에 children을 자동으로 넣지 않음
- React.FC 사용 여부는 팀 컨벤션 따름
- render props는 function type으로 별도 정의

---

### [실무]

Required Children 예:

```typescript
import type { ReactNode } from "react";

type PageLayoutProps = {
  children: ReactNode;
};

function PageLayout({ children }: PageLayoutProps) {
  return null;
}
```

Optional Children 예:

```typescript
import type { ReactNode } from "react";

type CardProps = {
  title: string;
  children?: ReactNode;
};
```

Render Props 예:

```typescript
type DataRendererProps<T> = {
  data: T;
  children: (data: T) => ReactNode;
};
```

실무 기준:

- Layout Component는 children required 가능
- Card / Modal은 children optional 가능
- children을 받지 않는 Component에는 children을 정의하지 않음
- ReactNode는 대부분 children Type에 적합
- render props는 function type으로 명확히 작성

---

### [FAQ]

Q. children Type은 보통 뭐로 써?
A. 대부분 `ReactNode`를 사용한다.

Q. children은 항상 optional이야?
A. 아니다. Layout처럼 반드시 children이 필요하면 required로 정의할 수 있다.

Q. 모든 Component Props에 children을 넣어야 해?
A. 아니다. 실제로 children을 받는 Component에만 정의한다.

---

# 3. React State Type

## 3.1 State Type Definition

### [개념]

State Type은 React Component 내부에서 관리하는 값의 Type이다.

State는 UI 상태, API 응답 데이터, Form 입력값, loading 상태, error 상태를 표현한다.

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";
```

React State는 초기값만으로 TypeScript가 의도를 정확히 추론하지 못하는 경우가 있으므로 명시적 Type이 필요할 수 있다.

---

### [핵심]

State Type 명시가 필요한 상황:

- empty array state
- nullable object state
- selected id state
- async status state
- form state
- error message state
- API response state
- union state

주의:

- 빈 배열은 element Type 명시
- null 초기값은 `T | null` 명시
- status 값은 literal union 권장
- form input value는 string 기반
- error message는 `string | null` 가능

---

### [실무]

State Type 예:

```typescript
type Festival = {
  festivalId: number;
  title: string;
};

type AsyncStatus = "idle" | "loading" | "success" | "error";

type FestivalPageState = {
  festivals: Festival[];
  selectedFestivalId: number | null;
  status: AsyncStatus;
  errorMessage: string | null;
};
```

실무 기준:

- 관련 상태는 State Type으로 묶을 수 있음
- 단순 상태는 개별 useState 가능
- 복잡한 상태 전이는 reducer 고려
- nullable state는 사용 전 null check
- API 상태는 `ApiState<T>` 패턴 가능

---

### [FAQ]

Q. React State Type은 언제 명시해야 해?
A. 빈 배열, null 초기값, union 상태, Form object처럼 TypeScript가 의도를 정확히 추론하기 어려울 때 명시한다.

Q. loading 상태는 boolean으로 충분해?
A. 단순 loading 여부만 필요하면 충분하다. idle, success, error까지 필요하면 literal union이 더 명확하다.

Q. errorMessage Type은 어떻게 써?
A. 오류가 없을 수 있으므로 `string | null`로 자주 정의한다.

---

## 3.2 Empty Array State

### [개념]

Empty Array State는 초기값이 빈 배열인 State다.

빈 배열은 element Type을 추론하기 어려우므로 Type 명시가 중요하다.

```typescript
const initialFestivals: Festival[] = [];
```

React `useState([])`는 의도한 element Type이 드러나지 않을 수 있다.

---

### [핵심]

Empty Array State 사용 영역:

- festival list
- review list
- comment list
- chat message list
- notification list
- option list
- table row list

주의:

- empty array에는 element Type 명시
- `any[]` 지양
- API Response Type 재사용 가능
- find 결과 undefined 가능
- map / filter 결과 Type 확인

---

### [실무]

기본 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
};

const initialFestivals: FestivalInfoResponse[] = [];
```

useState 예:

```typescript
import { useState } from "react";

const [festivals, setFestivals] = useState<FestivalInfoResponse[]>([]);
```

Option State 예:

```typescript
type SelectOption<TValue> = {
  label: string;
  value: TValue;
};

const [regionOptions, setRegionOptions] = useState<SelectOption<string>[]>([]);
```

실무 기준:

- `useState<T[]>([])` 패턴 사용
- API list response element Type과 일치
- options는 Generic Option Type 사용 가능
- 빈 배열을 any[]로 두지 않음
- setState에 잘못된 element 구조가 들어가지 않도록 함

---

### [FAQ]

Q. useState([])에는 Type을 써야 해?
A. 쓰는 것이 좋다. 빈 배열만으로는 element Type을 명확히 알기 어렵다.

Q. empty array state는 어떻게 Type을 써?
A. `useState<FestivalInfoResponse[]>([])`처럼 element Type 배열을 명시한다.

Q. 빈 배열 State를 any[]로 두면 안 돼?
A. Type Safety가 사라지므로 구체적인 Type을 사용하는 것이 좋다.

---

## 3.3 Nullable State

### [개념]

Nullable State는 초기값이 null이거나 값이 없을 수 있는 State다.

```typescript
const [currentUser, setCurrentUser] = useState<User | null>(null);
```

로그인 사용자, 선택된 항목, 상세 데이터, Modal 대상 데이터에서 자주 사용된다.

---

### [핵심]

Nullable State 사용 영역:

- current user
- selected item
- detail data
- profile data
- modal target
- selected id
- error message
- image url

주의:

- `T | null` 명시
- 사용 전 null check
- optional chaining 활용
- fallback UI 제공
- `as T`로 null 제거 금지

---

### [실무]

Current User 예:

```typescript
type UserResponse = {
  userId: number;
  nickname: string;
};

const [currentUser, setCurrentUser] = useState<UserResponse | null>(null);
```

Selected Id 예:

```typescript
const [selectedFestivalId, setSelectedFestivalId] = useState<number | null>(
  null,
);
```

Detail Data 예:

```typescript
type FestivalDetailResponse = {
  festivalId: number;
  title: string;
  description: string;
};

const [festivalDetail, setFestivalDetail] =
  useState<FestivalDetailResponse | null>(null);
```

사용 기준:

```typescript
function getDetailTitle(detail: FestivalDetailResponse | null): string {
  return detail?.title ?? "상세 정보 없음";
}
```

실무 기준:

- null 초기값은 Generic Type 명시
- 렌더링 전 null guard 작성
- loading 상태와 null 상태를 구분
- detail data는 `T | null` 패턴 자주 사용
- null 제거를 Type Assertion으로 처리하지 않음

---

### [FAQ]

Q. useState(null)은 Type을 어떻게 써?
A. `useState<User | null>(null)`처럼 null 가능성을 Union Type으로 명시한다.

Q. nullable state를 바로 사용하면 왜 오류가 나?
A. 값이 null일 수 있으므로 TypeScript가 직접 property 접근을 막기 때문이다.

Q. nullable state는 어떻게 렌더링해?
A. null guard, optional chaining, fallback UI를 사용한다.

---

## 3.4 Async State

### [개념]

Async State는 API 요청의 진행 상태, 성공 데이터, 오류 메시지를 표현하는 State다.

단순 boolean flag보다 literal union 또는 Discriminated Union으로 표현하면 모순 상태를 줄일 수 있다.

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";
```

---

### [핵심]

Async State 구성:

- status
- data
- errorMessage
- loading
- success
- error
- retry
- refetch

표현 방식:

- boolean flag
- AsyncStatus literal union
- ApiState discriminated union

주의:

- `isLoading`, `isSuccess`, `isError`가 동시에 true가 되는 모순 가능
- data와 error 동시 존재 가능성 관리
- 상태별 data 구조가 다르면 Discriminated Union 고려

---

### [실무]

AsyncStatus 방식:

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";

type RequestState = {
  status: AsyncStatus;
  errorMessage: string | null;
};
```

ApiState 방식:

```typescript
type ApiState<T> =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; message: string };
```

사용 예:

```typescript
type FestivalListState = ApiState<FestivalInfoResponse[]>;

function getFestivalCount(state: FestivalListState): number {
  if (state.status === "success") {
    return state.data.length;
  }

  return 0;
}
```

실무 기준:

- 단순 loading만 있으면 boolean 가능
- 상태가 3개 이상이면 AsyncStatus 권장
- 상태별 data 구조가 다르면 ApiState 권장
- Error Message는 string | null 또는 error state에 포함
- Review Agent는 모순 상태 가능성 확인

---

### [FAQ]

Q. Async State는 어떻게 Type으로 관리해?
A. `AsyncStatus` literal union 또는 `ApiState<T>` Discriminated Union으로 관리할 수 있다.

Q. isLoading boolean 하나면 안 돼?
A. 단순한 경우는 가능하지만 성공, 실패, 대기 상태까지 표현하려면 literal union이 더 명확하다.

Q. ApiState<T>는 언제 좋아?
A. 상태별로 data 또는 error message 구조가 다를 때 좋다.

---

# 4. Form Type

## 4.1 Form Data Type

### [개념]

Form Data Type은 React Form에서 관리하는 입력값 구조를 정의하는 Type이다.

Form input value는 대부분 string으로 시작한다.

```typescript
type LoginFormData = {
  email: string;
  password: string;
};
```

Form Data Type과 API Request Type은 항상 같지 않다.

---

### [핵심]

Form Data Type 대상:

- login form
- signup form
- review form
- search form
- profile update form
- password update form
- festival filter form

주의:

- input value는 string
- number input도 string으로 들어올 수 있음
- checkbox는 boolean
- select value는 string
- file input은 File 또는 FileList
- Form Data → Request Type 변환 필요 가능

---

### [실무]

Login Form 예:

```typescript
type LoginFormData = {
  email: string;
  password: string;
};
```

Review Form 예:

```typescript
type ReviewFormData = {
  festivalId: string;
  rating: string;
  content: string;
};

type ReviewCreateRequest = {
  festivalId: number;
  rating: 1 | 2 | 3 | 4 | 5;
  content: string;
};
```

Mapping Function:

```typescript
function toReviewCreateRequest(
  formData: ReviewFormData,
): ReviewCreateRequest | null {
  const festivalId = Number(formData.festivalId);
  const rating = Number(formData.rating);

  if (
    Number.isNaN(festivalId) ||
    !Number.isInteger(rating) ||
    rating < 1 ||
    rating > 5
  ) {
    return null;
  }

  return {
    festivalId,
    rating: rating as 1 | 2 | 3 | 4 | 5,
    content: formData.content.trim(),
  };
}
```

실무 기준:

- Form Data는 입력 단계 Type
- Request Type은 API 전송 단계 Type
- 숫자 변환은 Mapping Function에서 처리
- validation 실패 가능성을 Return Type에 반영
- Form field name과 validation error field name 정합성 유지

---

### [FAQ]

Q. Form Data Type과 Request Type은 같아?
A. 항상 같지 않다. Form input은 string으로 관리되고 Request에서는 number나 literal union으로 변환될 수 있다.

Q. number input value는 number야?
A. 아니다. 일반적으로 input value는 string이다.

Q. Form Data에서 Request로 변환은 어디서 해?
A. Mapping Function에서 Runtime 변환과 validation을 수행한다.

---

## 4.2 Change Event Type

### [개념]

Change Event Type은 input, textarea, select 값 변경 이벤트의 Type이다.

React에서는 `ChangeEvent`를 사용한다.

```typescript
import type { ChangeEvent } from "react";

function handleChange(event: ChangeEvent<HTMLInputElement>): void {
  console.log(event.target.value);
}
```

---

### [핵심]

Change Event Type:

- input → `ChangeEvent<HTMLInputElement>`
- textarea → `ChangeEvent<HTMLTextAreaElement>`
- select → `ChangeEvent<HTMLSelectElement>`

값 Type:

- text input value → string
- number input value → string
- select value → string
- checkbox checked → boolean

주의:

- event any 금지
- checkbox는 value가 아니라 checked
- select literal union은 validation 필요
- number 변환은 Runtime 처리

---

### [실무]

Text Input 예:

```typescript
import type { ChangeEvent } from "react";

function handleEmailChange(event: ChangeEvent<HTMLInputElement>): string {
  return event.target.value;
}
```

Checkbox 예:

```typescript
import type { ChangeEvent } from "react";

function handleCheckboxChange(event: ChangeEvent<HTMLInputElement>): boolean {
  return event.target.checked;
}
```

Select 예:

```typescript
import type { ChangeEvent } from "react";

type SortOption = "latest" | "popular" | "rating";

function isSortOption(value: string): value is SortOption {
  return value === "latest" || value === "popular" || value === "rating";
}

function parseSortOption(event: ChangeEvent<HTMLSelectElement>): SortOption {
  const value = event.target.value;

  if (isSortOption(value)) {
    return value;
  }

  return "latest";
}
```

실무 기준:

- React Event Type을 type-only import
- target element Type을 정확히 지정
- input value는 string으로 처리
- checkbox는 checked 사용
- select 값은 literal union 검증 후 사용

---

### [FAQ]

Q. input onChange Type은 뭐야?
A. `ChangeEvent<HTMLInputElement>`를 사용한다.

Q. textarea onChange Type은 뭐야?
A. `ChangeEvent<HTMLTextAreaElement>`를 사용한다.

Q. select onChange Type은 뭐야?
A. `ChangeEvent<HTMLSelectElement>`를 사용한다.

Q. checkbox 값은 어떻게 읽어?
A. `event.target.checked`를 사용한다.

---

## 4.3 Submit Event Type

### [개념]

Submit Event Type은 form submit 이벤트의 Type이다.

React에서는 `FormEvent<HTMLFormElement>`를 사용한다.

```typescript
import type { FormEvent } from "react";

function handleSubmit(event: FormEvent<HTMLFormElement>): void {
  event.preventDefault();
}
```

Submit Handler는 Form Data 검증, Request Mapping, API 호출과 연결된다.

---

### [핵심]

Submit Event 핵심:

- `FormEvent<HTMLFormElement>`
- `event.preventDefault()`
- form validation
- request mapping
- async submit
- error handling
- loading status

주의:

- submit handler가 async이면 `Promise<void>` 가능
- Form Data와 Request Type 구분
- validation 실패 시 API 호출 중단
- event any 금지

---

### [실무]

동기 Submit 예:

```typescript
import type { FormEvent } from "react";

function handleSubmit(event: FormEvent<HTMLFormElement>): void {
  event.preventDefault();
}
```

비동기 Submit 예:

```typescript
type LoginFormData = {
  email: string;
  password: string;
};

type LoginRequest = {
  email: string;
  password: string;
};

async function submitLogin(request: LoginRequest): Promise<void> {
  await fetch("/api/login", {
    method: "POST",
    body: JSON.stringify(request),
  });
}
```

Submit Handler Type:

```typescript
type LoginSubmitHandler = (formData: LoginFormData) => Promise<void>;
```

실무 기준:

- form submit event는 FormEvent 사용
- API submit handler는 Promise<void> 가능
- validation 후 request mapping
- loading / error state와 연결
- password / token 로그 출력 금지

---

### [FAQ]

Q. form onSubmit Type은 뭐야?
A. `FormEvent<HTMLFormElement>`를 사용한다.

Q. submit handler가 async면 Return Type은 뭐야?
A. `Promise<void>`로 표현할 수 있다.

Q. submit에서 Form Data와 Request Type은 구분해야 해?
A. 구분하는 것이 좋다. Form 입력값과 API 전송 구조가 다를 수 있다.

---

# 5. API Data and Component Type

## 5.1 API Response to Props

### [개념]

API Response to Props는 서버에서 받은 응답 데이터를 Component Props로 전달하는 구조다.

```text
API Response
→ Response Type
→ Props Type
→ Component Rendering
```

API Response Type을 그대로 Props로 사용할 수도 있고, ViewModel로 변환한 뒤 Props로 사용할 수도 있다.

---

### [핵심]

API Response to Props 방식:

- Response Type 직접 전달
- ViewModel 변환 후 전달
- 필요한 field만 Pick
- nullable fallback 후 전달
- list item props로 분해
- callback props 추가

주의:

- API nullable field를 UI에서 처리
- Response Type과 Props Type을 무조건 동일시하지 않음
- Component 책임이 너무 커지면 Mapping Function 사용
- UI 표시용 label / date format은 ViewModel로 변환 가능

---

### [실무]

Response 직접 전달:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

type FestivalCardProps = {
  festival: FestivalInfoResponse;
  onSelect: (festivalId: number) => void;
};
```

ViewModel 전달:

```typescript
type FestivalCardViewModel = {
  id: number;
  title: string;
  imageUrl: string;
};

type FestivalCardProps = {
  festival: FestivalCardViewModel;
  onSelect: (festivalId: number) => void;
};
```

실무 기준:

- 단순 화면은 Response Type 직접 전달 가능
- fallback / formatting이 많으면 ViewModel 사용
- Props Type에 callback 포함
- nullable 처리 위치를 명확히 정함
- Review Agent는 Component가 API 구조에 과도하게 종속되는지 확인

---

### [FAQ]

Q. API Response Type을 Props로 바로 넘겨도 돼?
A. 가능하다. 하지만 화면 전용 가공이나 fallback이 많으면 ViewModel로 변환하는 것이 좋다.

Q. Props Type과 Response Type은 항상 같아?
A. 아니다. Props는 Component 입력 구조이고 Response는 서버 응답 구조다.

Q. nullable field 처리는 어디서 해?
A. Component 내부, Mapping Function, ViewModel 변환 단계 중 하나에서 명확히 처리해야 한다.

---

## 5.2 List Rendering Type

### [개념]

List Rendering Type은 배열 데이터를 map으로 렌더링할 때 element Type과 key 값을 명확히 정의하는 기준이다.

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
};
```

목록 UI에서는 element Type, key field, callback parameter Type이 중요하다.

---

### [핵심]

List Rendering 확인 대상:

- array element type
- key field
- nullable field
- callback parameter
- empty list state
- find result
- filter narrowing
- sort mutation

주의:

- key는 안정적인 id 사용
- index key 지양
- 빈 배열 state Type 명시
- nullable field fallback 처리
- find 결과 undefined 방어
- sort는 원본 변경 주의

---

### [실무]

List Item Props 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

type FestivalListProps = {
  festivals: FestivalInfoResponse[];
  onSelect: (festivalId: number) => void;
};
```

List Rendering 기준:

```typescript
function getFestivalKeys(festivals: FestivalInfoResponse[]): number[] {
  return festivals.map((festival) => festival.festivalId);
}
```

Image Filter Type Guard:

```typescript
type FestivalWithImage = FestivalInfoResponse & {
  imageUrl: string;
};

function hasFestivalImage(
  festival: FestivalInfoResponse,
): festival is FestivalWithImage {
  return festival.imageUrl !== null;
}

function getFestivalsWithImage(
  festivals: FestivalInfoResponse[],
): FestivalWithImage[] {
  return festivals.filter(hasFestivalImage);
}
```

실무 기준:

- List Props는 `T[]`로 명시
- key는 `festivalId`, `reviewId` 같은 stable id 사용
- index key는 순서 변경 가능 목록에서 지양
- filter로 Type Narrowing 필요 시 Type Guard 사용
- sort 사용 시 원본 변경 방지

---

### [FAQ]

Q. List Rendering Type에서 중요한 것은 뭐야?
A. 배열 element Type, key field, callback parameter Type, nullable field 처리다.

Q. React list key는 index로 써도 돼?
A. 고정 목록이면 가능하지만 변경 가능한 목록에서는 stable id를 사용하는 것이 좋다.

Q. filter로 nullable field를 제거하면 Type도 좁혀져?
A. 명확한 Type Narrowing이 필요하면 Type Guard를 사용하는 것이 좋다.

---

# 6. Custom Hook Type Basics

## 6.1 Custom Hook Return Type

### [개념]

Custom Hook Return Type은 Custom Hook이 반환하는 데이터와 함수 구조를 정의하는 Type이다.

```typescript
type UseFestivalListResult = {
  festivals: FestivalInfoResponse[];
  status: AsyncStatus;
  errorMessage: string | null;
  refetch: () => Promise<void>;
};
```

Custom Hook은 API 상태, Form 상태, UI 상태를 재사용할 때 사용된다.

---

### [핵심]

Custom Hook Return Type 구성:

- data
- status
- errorMessage
- loading
- action function
- refetch
- reset
- submit
- selected value

주의:

- Return Type 명시 권장
- tuple return이면 위치 의미 주의
- object return이 검색성과 가독성에 유리
- async function은 Promise<void>
- nullable data 반영

---

### [실무]

Object Return Type 예:

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";

type UseFestivalListResult = {
  festivals: FestivalInfoResponse[];
  status: AsyncStatus;
  errorMessage: string | null;
  refetch: () => Promise<void>;
};
```

Form Hook Return 예:

```typescript
type UseLoginFormResult = {
  formData: LoginFormData;
  errors: Partial<Record<keyof LoginFormData, string>>;
  submit: () => Promise<void>;
  reset: () => void;
};
```

실무 기준:

- Custom Hook Return Type은 명시 권장
- object return은 property 이름으로 의미 표현 가능
- tuple return은 짧고 관례적인 경우에만 사용
- API Hook은 status / data / error 구조 명확화
- action function Type을 명확히 작성

---

### [FAQ]

Q. Custom Hook Return Type은 꼭 써야 해?
A. 복잡한 Hook이나 공유 Hook은 명시하는 것이 좋다.

Q. Custom Hook은 object와 tuple 중 뭐를 반환하는 게 좋아?
A. 값이 여러 개이고 의미가 중요하면 object return이 가독성과 검색성에 유리하다.

Q. refetch 함수 Type은 어떻게 써?
A. 비동기 refetch라면 `() => Promise<void>`로 작성할 수 있다.

---

## 6.2 Custom Hook Parameter Type

### [개념]

Custom Hook Parameter Type은 Hook이 외부에서 받는 입력값의 Type이다.

```typescript
type UseFestivalDetailParams = {
  festivalId: number | null;
  enabled?: boolean;
};
```

Hook Parameter는 API 호출 조건, 초기값, 옵션을 표현한다.

---

### [핵심]

Hook Parameter Type 대상:

- id
- params object
- enabled option
- initial value
- search params
- pagination params
- callback options

주의:

- optional parameter가 많으면 object parameter 사용
- nullable id 처리
- enabled flag로 조건부 실행 가능
- Hook 내부에서 null guard 필요
- API Query Type과 Hook Params Type은 다를 수 있음

---

### [실무]

Detail Hook Params 예:

```typescript
type UseFestivalDetailParams = {
  festivalId: number | null;
  enabled?: boolean;
};

type UseFestivalDetailResult = {
  data: FestivalDetailResponse | null;
  status: AsyncStatus;
  errorMessage: string | null;
  refetch: () => Promise<void>;
};
```

Search Hook Params 예:

```typescript
type UseFestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  page?: number;
  size?: number;
};
```

실무 기준:

- Hook Parameter가 2개 이상이면 object parameter 고려
- nullable id는 내부에서 API 호출 전 guard
- enabled option으로 조건부 fetch 제어 가능
- Hook Params와 API Params가 같을 수도 다를 수도 있음
- Hook Return Type과 함께 정의

---

### [FAQ]

Q. Custom Hook Parameter Type은 왜 필요해?
A. Hook이 어떤 입력값을 받아 어떤 조건으로 동작하는지 명확히 하기 위해 필요하다.

Q. Hook parameter가 많으면 어떻게 해?
A. object parameter로 묶고 Type Alias나 Interface로 정의하는 것이 좋다.

Q. festivalId가 null일 수 있으면 어떻게 처리해?
A. `number | null`로 정의하고 Hook 내부에서 null guard 후 API 호출 여부를 결정한다.

---

# 7. Type-Only Import and Export

## 7.1 Type-Only Import

### [개념]

Type-only import는 Runtime 값이 아니라 Type만 가져올 때 사용하는 import 방식이다.

```typescript
import type { ChangeEvent, ReactNode } from "react";
```

Type-only import는 TypeScript 5.x+ 환경에서 Runtime import와 Type import를 구분하는 데 유용하다.

---

### [핵심]

Type-only import 사용 대상:

- Type Alias
- Interface
- React Event Type
- ReactNode
- Props Type
- API Response Type
- Utility Type

장점:

- Runtime import와 Type import 구분
- Bundle 혼선 감소
- 코드 의도 명확
- lint rule과 호환
- modern TypeScript 스타일

---

### [실무]

React Event Type 예:

```typescript
import type { ChangeEvent, FormEvent } from "react";
```

API Type 예:

```typescript
import type { FestivalInfoResponse } from "../types/festivalTypes";
```

혼합 import 예:

```typescript
import { useState } from "react";
import type { ChangeEvent } from "react";
```

실무 기준:

- Type만 사용하는 import는 `import type` 사용 권장
- Runtime 값은 일반 import 사용
- tsconfig / bundler 설정과 lint rule 확인
- Type-only import는 Runtime Code에 포함되지 않음
- Agent는 Type import와 Runtime import를 구분해 생성

---

### [FAQ]

Q. import type은 뭐야?
A. Runtime 값이 아니라 Type만 가져올 때 사용하는 TypeScript import 문법이다.

Q. React Event Type은 import type으로 가져와도 돼?
A. 된다. `ChangeEvent`, `FormEvent`, `ReactNode` 같은 Type은 import type으로 가져올 수 있다.

Q. useState도 import type으로 가져와?
A. 아니다. useState는 Runtime에서 사용하는 함수이므로 일반 import를 사용한다.

---

## 7.2 Type Export

### [개념]

Type Export는 Type Alias, Interface를 다른 파일에서 재사용할 수 있도록 export하는 방식이다.

```typescript
export type FestivalInfoResponse = {
  festivalId: number;
  title: string;
};
```

Type Export는 API Type, Props Type, Common Type 공유에 사용된다.

---

### [핵심]

Type Export 대상:

- API Response Type
- API Request Type
- Common Wrapper Type
- Error Type
- Props Type
- Form Data Type
- Utility Type
- Literal Union Type

주의:

- 너무 많은 Type을 한 파일에 몰아넣지 않음
- 이름 충돌 주의
- Domain별 Type 파일 분리
- default export보다 named export 권장 가능
- Type 이름은 검색 가능하게 작성

---

### [실무]

Domain Type Export:

```typescript
export type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

export type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
};
```

Common Type Export:

```typescript
export type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};

export type SliceResponse<T> = {
  content: T[];
  hasNext: boolean;
  number: number;
  size: number;
};
```

실무 기준:

- 공통 Type은 common file에서 export
- Domain Type은 domain file에서 export
- Component 내부 전용 Props는 export하지 않아도 됨
- 여러 곳에서 재사용되는 Props는 export 가능
- Type 이름에 Domain과 Role을 포함

---

### [FAQ]

Q. Type은 어떻게 export해?
A. `export type TypeName = ...` 형태로 export할 수 있다.

Q. 모든 Props Type을 export해야 해?
A. 아니다. Component 내부에서만 쓰는 Props Type은 export하지 않아도 된다.

Q. default export로 Type을 내보내도 돼?
A. 가능하지만 named export가 검색성과 일관성에 유리한 경우가 많다.

---

# 8. React TypeScript Common Mistakes

## 8.1 Props Type Mistakes

### [개념]

Props Type 실수는 optional / nullable 혼동, callback Type 누락, API Response와 Props 역할 혼동에서 자주 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Props Type을 any로 정의
- optional props 기본값 누락
- nullable props fallback 누락
- callback parameter Type 누락
- optional callback 직접 호출
- children을 무조건 포함
- API Response Type과 Props Type 무조건 동일시
- Component가 API 구조에 과도하게 종속
- Props 이름이 모호함

---

### [실무]

나쁜 예:

```typescript
type FestivalCardProps = any;
```

문제:

- 잘못된 props 전달을 TypeScript가 잡지 못한다.
- 자동완성 품질이 낮다.

개선:

```typescript
type FestivalCardProps = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  onSelect: (festivalId: number) => void;
};
```

Optional Callback 실수:

```typescript
type ModalProps = {
  onClose?: () => void;
};

function closeModal(props: ModalProps): void {
  props.onClose();
}
```

개선:

```typescript
function closeModal(props: ModalProps): void {
  props.onClose?.();
}
```

실무 기준:

- Props any 금지
- optional props는 default / fallback 처리
- nullable props는 null guard
- callback props는 Type 명확화
- Component 역할과 API Type 역할 구분

---

### [FAQ]

Q. Props Type에서 가장 흔한 실수는?
A. any 사용, optional callback 직접 호출, nullable props fallback 누락이다.

Q. optional props는 어떻게 처리해야 해?
A. default value, optional chaining, fallback UI를 사용해야 한다.

Q. API Response를 그대로 Props로 쓰면 안 돼?
A. 가능하지만 Component가 API 구조에 과도하게 종속되면 ViewModel로 분리하는 것이 좋다.

---

## 8.2 State Type Mistakes

### [개념]

State Type 실수는 초기값 기준 Type 추론을 과신하거나, null / empty array / status state를 명확히 정의하지 않을 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- `useState([])` Type 미정의
- `useState(null)` Type 미정의
- nullable state null guard 누락
- loading / success / error boolean flag 모순
- errorMessage를 string으로만 정의
- selected id undefined / null 혼동
- API data state와 UI ViewModel state 혼동
- State에 any 사용

---

### [실무]

나쁜 예:

```typescript
const [festivals, setFestivals] = useState([]);
const [currentUser, setCurrentUser] = useState(null);
```

문제:

- 빈 배열 element Type이 명확하지 않다.
- currentUser가 어떤 Type인지 알 수 없다.

개선:

```typescript
const [festivals, setFestivals] = useState<FestivalInfoResponse[]>([]);

const [currentUser, setCurrentUser] = useState<UserResponse | null>(null);
```

Boolean Flag 실수:

```typescript
type BadState = {
  isLoading: boolean;
  isSuccess: boolean;
  isError: boolean;
};
```

개선:

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";
```

실무 기준:

- empty array state는 `T[]` 명시
- nullable state는 `T | null` 명시
- async status는 literal union 고려
- error state는 nullable 처리
- state mutation 금지

---

### [FAQ]

Q. State Type에서 가장 흔한 실수는?
A. useState 빈 배열과 null 초기값에 Type을 명시하지 않는 것이다.

Q. useState(null)은 왜 문제가 돼?
A. 어떤 Type의 값이 나중에 들어올지 TypeScript가 알기 어렵기 때문이다.

Q. loading 상태는 boolean 여러 개로 관리해도 돼?
A. 가능하지만 모순 상태가 생길 수 있으므로 literal union이 더 명확한 경우가 많다.

---

## 8.3 Event and Form Type Mistakes

### [개념]

Event and Form Type 실수는 Event를 any로 처리하거나 input value Type을 실제와 다르게 이해할 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- event any 사용
- React Event와 DOM Event 혼동
- input number value를 number로 단정
- checkbox value와 checked 혼동
- select value를 literal union으로 바로 단정
- Form Data와 Request Type 혼동
- submit event preventDefault 누락
- password / token 로그 출력
- validation 실패 가능성 미반영

---

### [실무]

나쁜 예:

```typescript
function handleChange(event: any): number {
  return event.target.value;
}
```

문제:

- event Type이 any
- input value는 string인데 number로 반환한다고 단정

개선:

```typescript
import type { ChangeEvent } from "react";

function handleNumberInputChange(
  event: ChangeEvent<HTMLInputElement>,
): number | null {
  const value = Number(event.target.value);

  if (Number.isNaN(value)) {
    return null;
  }

  return value;
}
```

Checkbox 실수:

```typescript
function handleCheckboxChange(event: ChangeEvent<HTMLInputElement>): boolean {
  return event.target.checked;
}
```

실무 기준:

- Event Type 명시
- input value는 string으로 시작
- 숫자 변환은 Number + NaN 방어
- checkbox는 checked 사용
- select literal union은 Type Guard 사용
- Form Data와 Request Type 분리

---

### [FAQ]

Q. Event Type에서 가장 흔한 실수는?
A. event를 any로 두거나 input value Type을 number로 오해하는 것이다.

Q. input number value는 number가 아니야?
A. 일반적으로 string이다. number로 쓰려면 Runtime 변환이 필요하다.

Q. select value를 literal union으로 바로 써도 돼?
A. 권장하지 않는다. 허용 값인지 Type Guard로 확인하는 것이 안전하다.

---

# 9. Review Checklist

## 9.1 Part11 Checklist

### [개념]

TypeScript Foundation Part11 검수는 React Props, State, Event, Form, API Response 연결, Custom Hook Type, Type-only Import 기준을 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] React TypeScript Readiness 정의가 포함되었는가?
- [ ] Component Props Type 설명이 포함되었는가?
- [ ] Required Props 설명이 포함되었는가?
- [ ] Optional Props 설명이 포함되었는가?
- [ ] Nullable Props 설명이 포함되었는가?
- [ ] Children Type 설명이 포함되었는가?
- [ ] React State Type 설명이 포함되었는가?
- [ ] Empty Array State 설명이 포함되었는가?
- [ ] Nullable State 설명이 포함되었는가?
- [ ] Async State 설명이 포함되었는가?
- [ ] Form Data Type 설명이 포함되었는가?
- [ ] Change Event Type 설명이 포함되었는가?
- [ ] Submit Event Type 설명이 포함되었는가?
- [ ] API Response to Props 설명이 포함되었는가?
- [ ] List Rendering Type 설명이 포함되었는가?
- [ ] Custom Hook Return Type 설명이 포함되었는가?
- [ ] Custom Hook Parameter Type 설명이 포함되었는가?
- [ ] Type-only import 설명이 포함되었는가?
- [ ] Type Export 설명이 포함되었는가?
- [ ] Props / State / Event Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Required Section Check
→ Props Type Check
→ State Type Check
→ Event Type Check
→ Form Type Check
→ API Data Connection Check
→ Custom Hook Type Check
→ Import Export Check
→ Common Mistake Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

Part11은 React Core, React Component Design, Data Fetching, Form Handling 문서의 TypeScript 기반이다.

---

### [FAQ]

Q. Part11에서 가장 중요한 검수 기준은?
A. React Props, State, Event, Form Type을 API Response Type과 연결하고 optional / nullable / empty array / event value를 정확히 처리했는지 확인하는 것이다.

Q. Part11이 이후 문서와 어떻게 연결돼?
A. React Core, Component Design, Data Fetching, Form Handling, Authentication Frontend Flow의 TypeScript 기반으로 연결된다.

---

# Retrieval Queries

### [FAQ]

Q. React TypeScript Readiness가 뭐야?
A. React에서 Props, State, Event, Form, API Type을 안정적으로 사용하기 위한 기본 Type 기준이다.

Q. React TypeScript 문서는 React 심화 문서야?
A. 아니다. React Core 이전에 필요한 TypeScript 준비 문서다.

Q. React에서 TypeScript가 가장 많이 쓰이는 곳은?
A. Props Type, State Type, Event Handler Type, Form Data Type, API Response Type이다.

Q. Props Type은 뭐야?
A. Component가 외부에서 받는 데이터와 callback 구조를 정의하는 Type이다.

Q. Props Type 이름은 어떻게 지어?
A. 일반적으로 Component 이름에 `Props` suffix를 붙인다. 예: `FestivalCardProps`.

Q. API Response Type을 그대로 Props로 써도 돼?
A. 가능하지만 화면 전용 가공이 필요하면 ViewModel Type을 Props로 사용하는 것이 좋다.

Q. Required Props는 뭐야?
A. Component 사용 시 반드시 전달해야 하는 props다.

Q. Props에 ?가 없으면 required야?
A. 그렇다. TypeScript Object Type에서 ?가 없는 property는 필수다.

Q. required props와 nullable props는 같아?
A. 아니다. required는 property 존재 여부이고 nullable은 값이 null일 수 있다는 의미다.

Q. Optional Props는 어떻게 써?
A. property 이름 뒤에 `?`를 붙인다. 예: `message?: string`.

Q. Optional Props는 null도 허용해?
A. 아니다. 기본적으로 생략 또는 undefined 가능성을 의미한다. null도 허용하려면 `string | null`을 추가해야 한다.

Q. Optional Callback은 어떻게 호출해?
A. `onClose?.()`처럼 optional chaining으로 안전하게 호출한다.

Q. Nullable Props는 뭐야?
A. props property는 존재하지만 값이 null일 수 있는 Props다.

Q. imageUrl이 null 가능하면 어떻게 Type을 써?
A. `imageUrl: string | null`로 작성한다.

Q. nullable props를 UI에서 어떻게 처리해?
A. null check, `??`, optional chaining, fallback UI를 사용한다.

Q. children Type은 보통 뭐로 써?
A. 대부분 `ReactNode`를 사용한다.

Q. children은 항상 optional이야?
A. 아니다. Layout처럼 반드시 children이 필요하면 required로 정의할 수 있다.

Q. 모든 Component Props에 children을 넣어야 해?
A. 아니다. 실제로 children을 받는 Component에만 정의한다.

Q. React State Type은 언제 명시해야 해?
A. 빈 배열, null 초기값, union 상태, Form object처럼 TypeScript가 의도를 정확히 추론하기 어려울 때 명시한다.

Q. loading 상태는 boolean으로 충분해?
A. 단순 loading 여부만 필요하면 충분하다. idle, success, error까지 필요하면 literal union이 더 명확하다.

Q. errorMessage Type은 어떻게 써?
A. 오류가 없을 수 있으므로 `string | null`로 자주 정의한다.

Q. useState([])에는 Type을 써야 해?
A. 쓰는 것이 좋다. 빈 배열만으로는 element Type을 명확히 알기 어렵다.

Q. empty array state는 어떻게 Type을 써?
A. `useState<FestivalInfoResponse[]>([])`처럼 element Type 배열을 명시한다.

Q. 빈 배열 State를 any[]로 두면 안 돼?
A. Type Safety가 사라지므로 구체적인 Type을 사용하는 것이 좋다.

Q. useState(null)은 Type을 어떻게 써?
A. `useState<User | null>(null)`처럼 null 가능성을 Union Type으로 명시한다.

Q. nullable state를 바로 사용하면 왜 오류가 나?
A. 값이 null일 수 있으므로 TypeScript가 직접 property 접근을 막기 때문이다.

Q. nullable state는 어떻게 렌더링해?
A. null guard, optional chaining, fallback UI를 사용한다.

Q. Async State는 어떻게 Type으로 관리해?
A. `AsyncStatus` literal union 또는 `ApiState<T>` Discriminated Union으로 관리할 수 있다.

Q. isLoading boolean 하나면 안 돼?
A. 단순한 경우는 가능하지만 성공, 실패, 대기 상태까지 표현하려면 literal union이 더 명확하다.

Q. ApiState<T>는 언제 좋아?
A. 상태별로 data 또는 error message 구조가 다를 때 좋다.

Q. Form Data Type과 Request Type은 같아?
A. 항상 같지 않다. Form input은 string으로 관리되고 Request에서는 number나 literal union으로 변환될 수 있다.

Q. number input value는 number야?
A. 아니다. 일반적으로 input value는 string이다.

Q. Form Data에서 Request로 변환은 어디서 해?
A. Mapping Function에서 Runtime 변환과 validation을 수행한다.

Q. input onChange Type은 뭐야?
A. `ChangeEvent<HTMLInputElement>`를 사용한다.

Q. textarea onChange Type은 뭐야?
A. `ChangeEvent<HTMLTextAreaElement>`를 사용한다.

Q. select onChange Type은 뭐야?
A. `ChangeEvent<HTMLSelectElement>`를 사용한다.

Q. checkbox 값은 어떻게 읽어?
A. `event.target.checked`를 사용한다.

Q. form onSubmit Type은 뭐야?
A. `FormEvent<HTMLFormElement>`를 사용한다.

Q. submit handler가 async면 Return Type은 뭐야?
A. `Promise<void>`로 표현할 수 있다.

Q. submit에서 Form Data와 Request Type은 구분해야 해?
A. 구분하는 것이 좋다. Form 입력값과 API 전송 구조가 다를 수 있다.

Q. API Response Type을 Props로 바로 넘겨도 돼?
A. 가능하다. 하지만 화면 전용 가공이나 fallback이 많으면 ViewModel로 변환하는 것이 좋다.

Q. Props Type과 Response Type은 항상 같아?
A. 아니다. Props는 Component 입력 구조이고 Response는 서버 응답 구조다.

Q. nullable field 처리는 어디서 해?
A. Component 내부, Mapping Function, ViewModel 변환 단계 중 하나에서 명확히 처리해야 한다.

Q. List Rendering Type에서 중요한 것은 뭐야?
A. 배열 element Type, key field, callback parameter Type, nullable field 처리다.

Q. React list key는 index로 써도 돼?
A. 고정 목록이면 가능하지만 변경 가능한 목록에서는 stable id를 사용하는 것이 좋다.

Q. filter로 nullable field를 제거하면 Type도 좁혀져?
A. 명확한 Type Narrowing이 필요하면 Type Guard를 사용하는 것이 좋다.

Q. Custom Hook Return Type은 꼭 써야 해?
A. 복잡한 Hook이나 공유 Hook은 명시하는 것이 좋다.

Q. Custom Hook은 object와 tuple 중 뭐를 반환하는 게 좋아?
A. 값이 여러 개이고 의미가 중요하면 object return이 가독성과 검색성에 유리하다.

Q. refetch 함수 Type은 어떻게 써?
A. 비동기 refetch라면 `() => Promise<void>`로 작성할 수 있다.

Q. Custom Hook Parameter Type은 왜 필요해?
A. Hook이 어떤 입력값을 받아 어떤 조건으로 동작하는지 명확히 하기 위해 필요하다.

Q. Hook parameter가 많으면 어떻게 해?
A. object parameter로 묶고 Type Alias나 Interface로 정의하는 것이 좋다.

Q. festivalId가 null일 수 있으면 어떻게 처리해?
A. `number | null`로 정의하고 Hook 내부에서 null guard 후 API 호출 여부를 결정한다.

Q. import type은 뭐야?
A. Runtime 값이 아니라 Type만 가져올 때 사용하는 TypeScript import 문법이다.

Q. React Event Type은 import type으로 가져와도 돼?
A. 된다. `ChangeEvent`, `FormEvent`, `ReactNode` 같은 Type은 import type으로 가져올 수 있다.

Q. useState도 import type으로 가져와?
A. 아니다. useState는 Runtime에서 사용하는 함수이므로 일반 import를 사용한다.

Q. Type은 어떻게 export해?
A. `export type TypeName = ...` 형태로 export할 수 있다.

Q. 모든 Props Type을 export해야 해?
A. 아니다. Component 내부에서만 쓰는 Props Type은 export하지 않아도 된다.

Q. Props Type에서 가장 흔한 실수는?
A. any 사용, optional callback 직접 호출, nullable props fallback 누락이다.

Q. State Type에서 가장 흔한 실수는?
A. useState 빈 배열과 null 초기값에 Type을 명시하지 않는 것이다.

Q. Event Type에서 가장 흔한 실수는?
A. event를 any로 두거나 input value Type을 number로 오해하는 것이다.

Q. TypeScript Part11의 핵심은 뭐야?
A. React Props, State, Event, Form Type을 API Response Type과 연결하고 optional / nullable / empty array / event value를 정확히 처리하는 것이다.

Q. TypeScript Part11 다음 문서는 뭐가 좋아?
A. tsconfig, Migration, Troubleshooting, Final Review 문서가 적합하다.
