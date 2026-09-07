# TypeScript Foundation Part07 - Function Type and Callback Type

---

# 1. Function Type

## 1.1 Function Type Definition

### [개념]

Function Type은 함수의 parameter Type과 return Type을 정의하는 TypeScript Type이다.

```typescript
function add(a: number, b: number): number {
  return a + b;
}
```

Function Type은 함수가 어떤 값을 받고 어떤 값을 반환하는지 Compile Time에 검사한다.

Frontend에서는 Utility Function, API Function, Event Handler, Callback Props, Mapping Function에서 Function Type이 중요하다.

---

### [핵심]

Function Type 핵심 요소:

- parameter type
- return type
- optional parameter
- default parameter
- rest parameter
- function declaration
- function expression
- arrow function
- callback function
- async function
- `void`
- `Promise<T>`

Function Type 사용 영역:

- Utility Function
- API Function
- React Event Handler
- Callback Props
- Mapper Function
- Predicate Function
- Form Submit Handler
- Type Guard Function

---

### [실무]

2026 Frontend 실무 기준에서 Function Type은 API 연동, Component Props, Event Handler, 데이터 변환 로직의 안정성을 높이는 핵심 기준이다.

Utility Function 예:

```typescript
function formatPrice(price: number): string {
  return `${price.toLocaleString()}원`;
}
```

API Function 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

async function getFestivals(): Promise<FestivalInfoResponse[]> {
  const response = await fetch("/api/festivals");

  if (!response.ok) {
    throw new Error("Failed to load festivals");
  }

  return await response.json();
}
```

Callback Function 예:

```typescript
type FestivalClickHandler = (festivalId: number) => void;

const handleFestivalClick: FestivalClickHandler = (festivalId) => {
  console.log(festivalId);
};
```

실무 기준:

- Function Parameter Type은 대부분 명시
- 복잡한 Function Return Type은 명시
- API Function Return Type은 `Promise<T>`로 명시
- Callback Props는 parameter와 return type 명시
- `any` parameter 사용 지양
- 반환값 없는 함수는 `void` 사용

---

### [FAQ]

Q. Function Type이 뭐야?
A. 함수의 parameter Type과 return Type을 정의하는 TypeScript Type이다.

Q. 함수 parameter에는 Type을 꼭 써야 해?
A. 대부분 써야 한다. Function Parameter는 TypeScript가 자동 추론하기 어려운 경우가 많다.

Q. Function Return Type은 항상 써야 해?
A. 항상은 아니지만 API 함수, 복잡한 함수, 재사용 함수에는 명시하는 것이 좋다.

Q. 반환값 없는 함수는 어떤 Type이야?
A. `void`를 사용한다.

---

## 1.2 Function Declaration Type

### [개념]

Function Declaration Type은 `function` 키워드로 선언한 함수에 parameter Type과 return Type을 명시하는 방식이다.

```typescript
function getFestivalTitle(title: string): string {
  return title;
}
```

Function Declaration은 일반 함수, Utility Function, Service Function에서 자주 사용된다.

---

### [핵심]

Function Declaration Type 구성:

- function name
- parameter type
- return type
- optional parameter
- default parameter
- union parameter
- object parameter
- async return type

기본 형태:

```typescript
function functionName(parameter: Type): ReturnType {
  return value;
}
```

---

### [실무]

Object Parameter 예:

```typescript
type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  targetMonth?: string;
};

function createSearchQuery(params: FestivalSearchParams): string {
  const searchParams = new URLSearchParams();

  if (params.keyword) {
    searchParams.set("keyword", params.keyword);
  }

  if (params.regionCode) {
    searchParams.set("regionCode", params.regionCode);
  }

  if (params.targetMonth) {
    searchParams.set("targetMonth", params.targetMonth);
  }

  return searchParams.toString();
}
```

Union Parameter 예:

```typescript
function formatId(id: number | string): string {
  return String(id);
}
```

실무 기준:

- parameter Type은 명시
- return Type은 함수 계약이 중요하면 명시
- Object Parameter는 Type Alias 또는 Interface로 분리
- Union Parameter는 내부에서 Type Narrowing 적용
- Function 이름은 동작을 명확히 표현

---

### [FAQ]

Q. Function Declaration에서 Type은 어디에 써?
A. parameter 뒤와 함수 괄호 뒤 return 위치에 쓴다. 예: `function add(a: number): number`.

Q. Object Parameter는 어떻게 Type을 붙여?
A. type 또는 interface로 객체 구조를 정의한 뒤 parameter Type으로 사용한다.

Q. Union Parameter를 쓰면 바로 Type별 method를 쓸 수 있어?
A. 아니다. Type Narrowing으로 구체적인 Type을 확인한 뒤 사용해야 한다.

---

## 1.3 Function Expression Type

### [개념]

Function Expression Type은 함수를 변수에 할당하면서 함수 구조를 Type으로 정의하는 방식이다.

```typescript
const formatPrice = function (price: number): string {
  return `${price.toLocaleString()}원`;
};
```

Function Expression은 Arrow Function, Callback Function, Handler Function과 함께 자주 사용된다.

---

### [핵심]

Function Expression Type 방식:

- parameter Type 직접 명시
- return Type 직접 명시
- Function Type Alias 사용
- Arrow Function Type 사용
- Callback Type으로 재사용

예:

```typescript
type Formatter = (value: number) => string;

const formatPrice: Formatter = (value) => {
  return `${value.toLocaleString()}원`;
};
```

---

### [실무]

Function Type Alias 예:

```typescript
type ReviewPredicate = (rating: number) => boolean;

const isHighRating: ReviewPredicate = (rating) => {
  return rating >= 4;
};
```

Mapper Function 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

type FestivalCardViewModel = {
  id: number;
  title: string;
  imageUrl: string;
};

const toFestivalCardViewModel = (
  response: FestivalInfoResponse,
): FestivalCardViewModel => {
  return {
    id: response.festivalId,
    title: response.title,
    imageUrl: response.imageUrl ?? "/default-festival.png",
  };
};
```

실무 기준:

- 반복되는 Function 구조는 Type Alias로 분리
- Mapper Function은 input Type과 output Type을 명확히 정의
- Predicate Function은 boolean return Type 사용
- Callback Function은 parameter와 return Type을 명확히 유지
- Function Expression에서 any parameter 지양

---

### [FAQ]

Q. Function Expression에도 Type을 붙일 수 있어?
A. 가능하다. parameter와 return Type을 직접 쓰거나 Function Type Alias를 사용할 수 있다.

Q. Function Type Alias는 언제 써?
A. 같은 함수 구조가 반복되거나 Callback Props로 재사용할 때 사용한다.

Q. Mapper Function은 Return Type을 써야 해?
A. 권장한다. API Response를 ViewModel로 변환할 때 output 구조를 명확히 할 수 있다.

---

# 2. Parameter Type

## 2.1 Required Parameter

### [개념]

Required Parameter는 함수 호출 시 반드시 전달해야 하는 parameter다.

```typescript
function findFestival(festivalId: number): void {
  console.log(festivalId);
}
```

Parameter 뒤에 `?`가 없으면 기본적으로 Required Parameter다.

---

### [핵심]

Required Parameter 특징:

- 함수 호출 시 반드시 필요
- 누락 시 Type Error 발생
- Function Contract 명확화
- API Function에 자주 사용
- Utility Function에 자주 사용
- Callback Function에 자주 사용

---

### [실무]

API Function 예:

```typescript
async function getFestivalDetail(
  festivalId: number,
): Promise<FestivalDetailResponse> {
  const response = await fetch(`/api/festivals/${festivalId}`);

  if (!response.ok) {
    throw new Error("Failed to load festival detail");
  }

  return await response.json();
}
```

Callback 예:

```typescript
type SelectFestivalHandler = (festivalId: number) => void;

const selectFestival: SelectFestivalHandler = (festivalId) => {
  console.log(festivalId);
};
```

실무 기준:

- path parameter는 Required Parameter로 정의
- 반드시 필요한 request 값은 Required Parameter 또는 Required Property로 정의
- Callback에서 필요한 id 값은 Required Parameter로 정의
- 값 누락 가능성이 있으면 optional 또는 nullable 검토

---

### [FAQ]

Q. Required Parameter는 뭐야?
A. 함수 호출 시 반드시 전달해야 하는 parameter다.

Q. parameter에 ?가 없으면 필수야?
A. 그렇다. TypeScript 함수 parameter는 기본적으로 필수다.

Q. API path parameter는 required로 두면 돼?
A. 대부분 그렇다. `/api/festivals/{id}` 같은 id는 필수 parameter다.

---

## 2.2 Optional Parameter

### [개념]

Optional Parameter는 함수 호출 시 생략할 수 있는 parameter다.

parameter 이름 뒤에 `?`를 붙여 작성한다.

```typescript
function createPageUrl(page?: number): string {
  return `/page/${page ?? 1}`;
}
```

Optional Parameter는 기본적으로 `T | undefined` 가능성을 가진다.

---

### [핵심]

Optional Parameter 특징:

- 호출 시 생략 가능
- 값은 `T | undefined`
- 기본값 처리 필요
- Required Parameter 뒤에 배치
- null을 자동 허용하지 않음
- 남용 시 함수 계약이 약해짐

주의:

- `name?: string`은 `string | undefined`
- null도 허용하려면 `string | null` 명시
- Optional Parameter는 뒤쪽에 배치
- 복잡한 옵션은 Object Parameter 사용 권장

---

### [실무]

Optional Parameter 예:

```typescript
function createFestivalListUrl(page?: number, size?: number): string {
  const searchParams = new URLSearchParams();

  searchParams.set("page", String(page ?? 1));
  searchParams.set("size", String(size ?? 10));

  return `/api/festivals?${searchParams.toString()}`;
}
```

복잡한 조건은 Object Parameter 권장:

```typescript
type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  themeCode?: string;
  page?: number;
  size?: number;
};

function createFestivalSearchUrl(params: FestivalSearchParams): string {
  return `/api/festivals?${new URLSearchParams(
    Object.entries(params)
      .filter(([, value]) => value !== undefined)
      .map(([key, value]) => [key, String(value)]),
  ).toString()}`;
}
```

실무 기준:

- optional 값은 `??`로 기본값 처리
- optional parameter가 많아지면 params object로 전환
- null 허용 여부와 undefined 허용 여부 구분
- API 검색 조건은 Object Type으로 관리하는 것이 검색에 유리

---

### [FAQ]

Q. Optional Parameter는 어떻게 써?
A. parameter 이름 뒤에 `?`를 붙인다. 예: `page?: number`.

Q. Optional Parameter는 null도 허용해?
A. 아니다. 기본적으로 `T | undefined`를 의미한다. null도 허용하려면 `T | null`을 명시해야 한다.

Q. Optional Parameter가 많으면 어떻게 해?
A. Object Parameter로 묶고 Type Alias나 Interface로 정의하는 것이 좋다.

---

## 2.3 Default Parameter

### [개념]

Default Parameter는 함수 호출 시 argument가 생략되면 사용할 기본값을 지정하는 parameter다.

```typescript
function createPageUrl(page: number = 1): string {
  return `/page/${page}`;
}
```

Default Parameter는 optional한 호출을 허용하면서 내부에서 기본값을 보장한다.

---

### [핵심]

Default Parameter 특징:

- argument 생략 시 기본값 사용
- parameter Type 추론 가능
- undefined 전달 시 기본값 사용
- null 전달 시 기본값 사용 안 됨
- optional parameter와 목적이 다름
- 기본값으로 함수 내부 로직 단순화

---

### [실무]

Page Query 예:

```typescript
function createPaginationQuery(page: number = 1, size: number = 10): string {
  return `page=${page}&size=${size}`;
}
```

Sort Option 예:

```typescript
type FestivalSortOption = "latest" | "popular" | "rating";

function createSortQuery(sort: FestivalSortOption = "latest"): string {
  return `sort=${sort}`;
}
```

주의:

```typescript
function createPageUrl(page: number = 1): string {
  return `/page/${page}`;
}

createPageUrl(undefined);
createPageUrl(null);
```

설명:

- `undefined`는 default value 적용
- `null`은 Type Error 또는 별도 처리 대상
- Runtime 입력이면 null 방어 필요 가능

실무 기준:

- 기본값이 명확한 parameter는 default parameter 사용
- 복잡한 옵션은 params object + default merge 고려
- null과 undefined 동작 차이 이해
- literal union default value 활용 가능

---

### [FAQ]

Q. Default Parameter는 뭐야?
A. argument가 생략되거나 undefined일 때 사용할 기본값을 지정하는 parameter다.

Q. Optional Parameter와 Default Parameter 차이는?
A. Optional Parameter는 생략 가능성을 표현하고, Default Parameter는 생략 시 사용할 기본값을 제공한다.

Q. null을 넘겨도 default 값이 적용돼?
A. 아니다. default value는 보통 undefined에 적용된다. null은 별도 처리해야 한다.

---

## 2.4 Rest Parameter

### [개념]

Rest Parameter는 여러 argument를 배열로 받는 parameter다.

```typescript
function sum(...numbers: number[]): number {
  return numbers.reduce((total, value) => total + value, 0);
}
```

Rest Parameter Type은 배열 Type으로 정의한다.

---

### [핵심]

Rest Parameter 특징:

- 여러 argument 수신
- 배열 Type으로 정의
- `...parameterName: Type[]`
- Utility Function에 사용
- Logger Function에 사용
- 제한 없는 인자 수 처리 가능

주의:

- Rest Parameter는 마지막 parameter여야 함
- Type을 너무 넓게 잡지 않음
- `any[]` 지양
- 필요하면 tuple rest pattern 고려

---

### [실무]

Class Name Utility 예:

```typescript
function joinClassNames(...classNames: string[]): string {
  return classNames.filter(Boolean).join(" ");
}
```

Message Logger 예:

```typescript
function logMessages(...messages: string[]): void {
  messages.forEach((message) => {
    console.log(message);
  });
}
```

API Query Utility 예:

```typescript
type QueryPair = [string, string];

function createQueryString(...pairs: QueryPair[]): string {
  return new URLSearchParams(pairs).toString();
}
```

실무 기준:

- Rest Parameter Type은 구체적으로 작성
- 문자열 유틸리티에는 `string[]`
- 숫자 유틸리티에는 `number[]`
- key-value pair는 Tuple Type 활용 가능
- Callback에서는 Rest Parameter 남용 지양

---

### [FAQ]

Q. Rest Parameter는 뭐야?
A. 여러 argument를 배열로 받는 parameter다.

Q. Rest Parameter Type은 어떻게 써?
A. `...numbers: number[]`처럼 배열 Type으로 작성한다.

Q. Rest Parameter는 어디에 위치해야 해?
A. 함수 parameter 목록의 마지막에 위치해야 한다.

---

# 3. Return Type

## 3.1 Return Type Definition

### [개념]

Return Type은 함수가 반환하는 값의 Type이다.

```typescript
function getTitle(): string {
  return "Festival";
}
```

Return Type은 함수의 결과 계약을 명확히 하고 호출하는 코드가 반환값을 안전하게 사용할 수 있게 한다.

---

### [핵심]

주요 Return Type:

- `string`
- `number`
- `boolean`
- `void`
- `Promise<T>`
- object type
- array type
- union type
- nullable type
- `undefined`
- `never`

Return Type 명시 권장 상황:

- API Function
- Public Utility Function
- 복잡한 조건 분기
- Mapper Function
- Type Guard Function
- Library Function
- Review 대상 핵심 함수

---

### [실무]

Mapper Function 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

type FestivalCardViewModel = {
  id: number;
  title: string;
  imageUrl: string;
};

function toFestivalCardViewModel(
  response: FestivalInfoResponse,
): FestivalCardViewModel {
  return {
    id: response.festivalId,
    title: response.title,
    imageUrl: response.imageUrl ?? "/default-festival.png",
  };
}
```

Union Return Type 예:

```typescript
function findFestivalTitle(
  festivals: FestivalInfoResponse[],
  festivalId: number,
): string | null {
  const festival = festivals.find((item) => item.festivalId === festivalId);

  return festival?.title ?? null;
}
```

실무 기준:

- API Function Return Type은 반드시 명확히 작성
- Mapper Function Return Type은 ViewModel 검증에 유용
- null 가능 반환은 `T | null`로 명시
- find 결과는 `T | undefined` 가능성 고려
- 복잡한 함수는 추론만 의존하지 않음

---

### [FAQ]

Q. Return Type은 어디에 써?
A. 함수 parameter 괄호 뒤에 쓴다. 예: `function getName(): string`.

Q. Return Type은 항상 명시해야 해?
A. 항상은 아니지만 API 함수, Mapper 함수, 복잡한 함수에는 명시하는 것이 좋다.

Q. null을 반환할 수 있으면 어떻게 써?
A. `string | null`, `User | null`처럼 Union Type으로 작성한다.

---

## 3.2 Void Return Type

### [개념]

`void` Return Type은 함수가 의미 있는 값을 반환하지 않음을 나타낸다.

```typescript
function logMessage(message: string): void {
  console.log(message);
}
```

Frontend에서는 Event Handler, Callback Props, State Update Function에서 자주 사용한다.

---

### [핵심]

`void` 사용 영역:

- event handler
- click handler
- submit handler
- callback prop
- logging function
- state update function
- command function

주의:

- `void`는 반환값 없음 의미
- `undefined`와 사용 목적이 다름
- async function은 `Promise<void>`
- 반환값이 필요한 함수에 void 사용 금지

---

### [실무]

Callback Props 예:

```typescript
type ModalProps = {
  open: boolean;
  onClose: () => void;
};
```

Click Handler 예:

```typescript
type FestivalClickHandler = (festivalId: number) => void;

const handleFestivalClick: FestivalClickHandler = (festivalId) => {
  console.log(festivalId);
};
```

Form Submit Handler 예:

```typescript
import type { FormEvent } from "react";

function handleSubmit(event: FormEvent<HTMLFormElement>): void {
  event.preventDefault();
}
```

실무 기준:

- 반환값 없는 handler는 `void`
- Callback Props에는 `() => void` 패턴 자주 사용
- Event Handler Return Type은 대부분 `void`
- async handler는 `Promise<void>` 가능성 고려

---

### [FAQ]

Q. void는 언제 써?
A. 반환값이 없는 함수의 Return Type에 사용한다.

Q. Callback Props에서 `() => void`는 무슨 뜻이야?
A. parameter 없이 호출되고 반환값이 없는 callback function이라는 뜻이다.

Q. Event Handler Return Type은 보통 뭐야?
A. 대부분 `void`를 사용한다.

---

## 3.3 Promise Return Type

### [개념]

Promise Return Type은 비동기 함수가 나중에 반환할 값의 Type을 표현한다.

`async` 함수는 항상 Promise를 반환한다.

```typescript
async function getTitle(): Promise<string> {
  return "Festival";
}
```

API Function에서는 `Promise<T>` Return Type이 필수적으로 사용된다.

---

### [핵심]

Promise Return Type 핵심:

- async function은 Promise 반환
- `Promise<T>` 형태로 작성
- API Response Type과 연결
- 반환값 없으면 `Promise<void>`
- error throw 가능성 고려
- await 결과는 T로 사용

---

### [실무]

API Function 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};

type FestivalInfoResponse = {
  festivalId: number;
  title: string;
};

async function getFestivalList(): Promise<ApiResponse<FestivalInfoResponse[]>> {
  const response = await fetch("/api/festivals");

  if (!response.ok) {
    throw new Error("Failed to load festival list");
  }

  return await response.json();
}
```

반환값 없는 async 예:

```typescript
async function sendLog(message: string): Promise<void> {
  await fetch("/api/logs", {
    method: "POST",
    body: JSON.stringify({ message }),
  });
}
```

실무 기준:

- API 함수는 `Promise<ResponseType>` 명시
- `await` 이후 값은 Promise 내부 Type으로 사용
- 반환값 없는 async function은 `Promise<void>`
- Error Response Type과 try / catch 처리 고려
- `Promise<any>` 지양

---

### [FAQ]

Q. async 함수 Return Type은 어떻게 써?
A. `Promise<T>` 형태로 작성한다.

Q. async 함수에서 반환값이 없으면 뭐라고 써?
A. `Promise<void>`로 작성한다.

Q. API Function Return Type은 왜 중요해?
A. 서버 응답 구조를 호출부에서 안전하게 사용할 수 있게 하기 때문이다.

---

# 4. Callback Type

## 4.1 Callback Type Definition

### [개념]

Callback Type은 다른 함수나 Component에 전달되는 함수의 parameter와 return Type을 정의하는 Type이다.

```typescript
type ClickHandler = (id: number) => void;
```

Callback Type은 React Props, Event Handling, Array Method, Async Flow에서 자주 사용된다.

---

### [핵심]

Callback Type 구성:

- parameter type
- return type
- void return
- async callback
- optional callback
- callback props
- mapper callback
- predicate callback

사용 영역:

- `onClick`
- `onChange`
- `onSubmit`
- `onClose`
- `onSelect`
- `map`
- `filter`
- `find`
- custom hooks
- service callbacks

---

### [실무]

Callback Props 예:

```typescript
type FestivalCardProps = {
  festivalId: number;
  title: string;
  onSelect: (festivalId: number) => void;
};

function selectFestival(props: FestivalCardProps): void {
  props.onSelect(props.festivalId);
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

Async Callback 예:

```typescript
type SubmitHandler = () => Promise<void>;

const handleSubmit: SubmitHandler = async () => {
  await fetch("/api/submit");
};
```

실무 기준:

- Callback Props는 parameter와 return Type 명확히 작성
- 반환값이 필요 없으면 `void`
- 비동기 callback은 `Promise<void>` 또는 `Promise<T>`
- optional callback은 호출 전 optional chaining 사용
- 반복되는 callback 구조는 Type Alias로 분리

---

### [FAQ]

Q. Callback Type이 뭐야?
A. 다른 함수나 Component에 전달되는 함수의 parameter와 return Type을 정의하는 Type이다.

Q. Callback Props는 어떻게 Type을 써?
A. `(parameter: Type) => ReturnType` 형태로 작성한다.

Q. Optional Callback은 어떻게 호출해?
A. `onClose?.()`처럼 optional chaining으로 안전하게 호출한다.

---

## 4.2 Callback Props

### [개념]

Callback Props는 React Component가 부모 Component로부터 전달받는 함수 Props다.

```typescript
type ButtonProps = {
  onClick: () => void;
};
```

Callback Props는 Component 내부 이벤트를 부모 Component에 전달하는 역할을 한다.

---

### [핵심]

Callback Props 주요 패턴:

- `onClick: () => void`
- `onSelect: (id: number) => void`
- `onChange: (value: string) => void`
- `onSubmit: (formData: FormDataType) => void`
- `onClose?: () => void`
- `onSuccess?: (data: T) => void`
- `onError?: (message: string) => void`

주의:

- parameter Type 명확화
- return Type 명확화
- optional callback 안전 호출
- callback 이름은 `on` prefix 권장
- 불필요한 any parameter 금지

---

### [실무]

Select Callback 예:

```typescript
type FestivalListItemProps = {
  festivalId: number;
  title: string;
  onSelect: (festivalId: number) => void;
};

function handleListItemClick(props: FestivalListItemProps): void {
  props.onSelect(props.festivalId);
}
```

Form Callback 예:

```typescript
type LoginFormData = {
  email: string;
  password: string;
};

type LoginFormProps = {
  onSubmit: (formData: LoginFormData) => Promise<void>;
};
```

Success / Error Callback 예:

```typescript
type ApiCallbackProps<T> = {
  onSuccess?: (data: T) => void;
  onError?: (message: string) => void;
};
```

실무 기준:

- Component Event 전달은 Callback Props 사용
- callback parameter는 필요한 값만 전달
- API 비동기 callback은 `Promise<void>` 고려
- optional callback은 `?.()`로 호출
- callback Type Alias로 재사용 가능

---

### [FAQ]

Q. Callback Props는 왜 필요해?
A. 자식 Component 이벤트를 부모 Component로 전달하기 위해 필요하다.

Q. onClick Type은 보통 어떻게 써?
A. 단순 클릭 callback은 `onClick: () => void`로 쓸 수 있다.

Q. onSelect처럼 id를 넘기는 callback은 어떻게 써?
A. `onSelect: (id: number) => void`처럼 parameter Type을 명시한다.

---

# 5. React Event Handler Type

## 5.1 React Event Type Basics

### [개념]

React Event Handler Type은 React 이벤트 객체의 Type을 정의하는 방식이다.

React Event Type은 DOM Event Type과 구분되며 React에서 제공하는 Synthetic Event 기반 Type을 사용한다.

```typescript
import type { ChangeEvent } from "react";

function handleChange(event: ChangeEvent<HTMLInputElement>): void {
  console.log(event.target.value);
}
```

---

### [핵심]

주요 React Event Type:

- `MouseEvent`
- `ChangeEvent`
- `FormEvent`
- `KeyboardEvent`
- `FocusEvent`

주요 Element Type:

- `HTMLInputElement`
- `HTMLButtonElement`
- `HTMLFormElement`
- `HTMLTextAreaElement`
- `HTMLSelectElement`

주의:

- React Event Type import 필요
- DOM Event와 React Event 구분
- target element Type 명시
- handler return은 대부분 `void`

---

### [실무]

Input Change 예:

```typescript
import type { ChangeEvent } from "react";

function handleInputChange(event: ChangeEvent<HTMLInputElement>): void {
  const value = event.target.value;
  console.log(value);
}
```

Form Submit 예:

```typescript
import type { FormEvent } from "react";

function handleFormSubmit(event: FormEvent<HTMLFormElement>): void {
  event.preventDefault();
}
```

Button Click 예:

```typescript
import type { MouseEvent } from "react";

function handleButtonClick(event: MouseEvent<HTMLButtonElement>): void {
  console.log(event.currentTarget.disabled);
}
```

실무 기준:

- input onChange는 `ChangeEvent<HTMLInputElement>`
- textarea onChange는 `ChangeEvent<HTMLTextAreaElement>`
- select onChange는 `ChangeEvent<HTMLSelectElement>`
- form onSubmit은 `FormEvent<HTMLFormElement>`
- button onClick은 `MouseEvent<HTMLButtonElement>`
- Type-only import 사용 권장

---

### [FAQ]

Q. input onChange event Type은 뭐야?
A. 일반적으로 `ChangeEvent<HTMLInputElement>`를 사용한다.

Q. form onSubmit event Type은 뭐야?
A. 일반적으로 `FormEvent<HTMLFormElement>`를 사용한다.

Q. button onClick event Type은 뭐야?
A. 일반적으로 `MouseEvent<HTMLButtonElement>`를 사용할 수 있다.

Q. React Event Type은 어디서 가져와?
A. `react`에서 type-only import로 가져올 수 있다.

---

## 5.2 Event Target Type

### [개념]

Event Target Type은 이벤트가 발생한 HTML Element의 Type을 명시하는 방식이다.

```typescript
ChangeEvent<HTMLInputElement>;
```

`HTMLInputElement`를 명시하면 `event.target.value`를 안전하게 사용할 수 있다.

---

### [핵심]

Element Type 예:

- input → `HTMLInputElement`
- textarea → `HTMLTextAreaElement`
- select → `HTMLSelectElement`
- form → `HTMLFormElement`
- button → `HTMLButtonElement`
- anchor → `HTMLAnchorElement`

주의:

- element Type을 잘못 지정하면 property 접근 오류 가능
- `event.target`과 `event.currentTarget` 차이 이해
- Form 내부 field 접근은 별도 처리 필요
- any로 event 처리 지양

---

### [실무]

Select Change 예:

```typescript
import type { ChangeEvent } from "react";

function handleSelectChange(event: ChangeEvent<HTMLSelectElement>): string {
  return event.target.value;
}
```

Textarea Change 예:

```typescript
import type { ChangeEvent } from "react";

function handleTextareaChange(event: ChangeEvent<HTMLTextAreaElement>): string {
  return event.target.value;
}
```

Checkbox Change 예:

```typescript
import type { ChangeEvent } from "react";

function handleCheckboxChange(event: ChangeEvent<HTMLInputElement>): boolean {
  return event.target.checked;
}
```

실무 기준:

- text input value는 string
- checkbox checked는 boolean
- select value는 string
- number input value도 string으로 들어옴
- 숫자로 사용하려면 Runtime 변환 필요

---

### [FAQ]

Q. input number의 value는 number야?
A. 아니다. input value는 대부분 string이다. 숫자로 쓰려면 Number로 변환해야 한다.

Q. checkbox 값은 어떻게 읽어?
A. `event.target.checked`를 사용하며 Type은 boolean이다.

Q. select value Type은 뭐야?
A. 기본적으로 string이다. literal union으로 쓰려면 허용 값 검증이 필요하다.

---

# 6. Array Method Callback Type

## 6.1 Map Filter Find Callback

### [개념]

Array Method Callback Type은 `map`, `filter`, `find` 같은 배열 메서드에 전달되는 callback 함수의 Type이다.

TypeScript는 배열 element Type을 기준으로 callback parameter Type을 추론한다.

```typescript
const titles = festivals.map((festival) => festival.title);
```

---

### [핵심]

Array Method Callback:

- `map`
- `filter`
- `find`
- `some`
- `every`
- `reduce`

Type 특징:

- callback parameter는 element Type으로 추론
- map 결과는 return Type 배열
- filter 결과는 같은 element Type 배열
- find 결과는 `T | undefined`
- reduce는 accumulator Type 주의

---

### [실무]

map 예:

```typescript
type Festival = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

function getFestivalTitles(festivals: Festival[]): string[] {
  return festivals.map((festival) => festival.title);
}
```

filter 예:

```typescript
function getFestivalsWithImage(festivals: Festival[]): Festival[] {
  return festivals.filter((festival) => festival.imageUrl !== null);
}
```

find 예:

```typescript
function findFestival(
  festivals: Festival[],
  festivalId: number,
): Festival | undefined {
  return festivals.find((festival) => festival.festivalId === festivalId);
}
```

실무 기준:

- Array element Type을 먼저 명확히 정의
- find 결과는 undefined 가능성 처리
- filter 이후 nullable property가 자동으로 좁혀지지 않을 수 있음
- 복잡한 filter narrowing은 Type Guard 사용 고려
- reduce는 accumulator Type 명시 고려

---

### [FAQ]

Q. map callback parameter Type은 직접 써야 해?
A. 배열 Type이 명확하면 TypeScript가 element Type으로 추론한다.

Q. find 결과는 왜 undefined가 붙어?
A. 조건에 맞는 요소가 없을 수 있기 때문이다.

Q. filter로 null을 제거하면 Type도 자동으로 좁혀져?
A. 단순 조건에서는 충분하지 않을 수 있다. 필요한 경우 Type Guard를 사용한다.

---

## 6.2 Predicate Callback

### [개념]

Predicate Callback은 조건을 검사해 `boolean`을 반환하는 callback 함수다.

```typescript
type FestivalPredicate = (festival: Festival) => boolean;
```

Predicate Callback은 `filter`, `find`, validation, 조건 분기에서 자주 사용된다.

---

### [핵심]

Predicate Callback 특징:

- input value 검사
- boolean return
- filter 조건
- find 조건
- validation 조건
- Type Guard로 확장 가능

---

### [실무]

일반 Predicate 예:

```typescript
type Festival = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

type FestivalPredicate = (festival: Festival) => boolean;

const hasImage: FestivalPredicate = (festival) => {
  return festival.imageUrl !== null;
};
```

Validation Predicate 예:

```typescript
function isValidRating(rating: number): boolean {
  return rating >= 1 && rating <= 5 && Number.isInteger(rating);
}
```

Type Guard Predicate 예:

```typescript
type FestivalWithImage = Festival & {
  imageUrl: string;
};

function hasFestivalImage(festival: Festival): festival is FestivalWithImage {
  return festival.imageUrl !== null;
}
```

실무 기준:

- Predicate는 boolean return Type
- Type Narrowing이 필요하면 Type Guard Predicate 사용
- 이름은 `is`, `has`, `can`, `should` prefix 권장
- Validation Logic은 Runtime 검증 목적임을 명확히 함

---

### [FAQ]

Q. Predicate Callback이 뭐야?
A. 값을 검사해 boolean을 반환하는 callback 함수다.

Q. Predicate 함수 이름은 어떻게 짓는 게 좋아?
A. `isValid`, `hasImage`, `canSubmit`처럼 boolean 의미가 드러나게 짓는 것이 좋다.

Q. Predicate와 Type Guard는 같아?
A. Type Guard는 Predicate의 특수한 형태로, true일 때 TypeScript에 더 좁은 Type을 알려준다.

---

# 7. Function Type and API Layer

## 7.1 API Function Type

### [개념]

API Function Type은 Frontend가 Backend API를 호출하는 함수의 parameter와 Promise Return Type을 명확히 정의하는 방식이다.

```typescript
async function getUser(userId: number): Promise<UserResponse> {
  const response = await fetch(`/api/users/${userId}`);
  return await response.json();
}
```

API Function Type은 Request Type, Response Type, Error Handling과 연결된다.

---

### [핵심]

API Function Type 구성:

- path parameter type
- query parameter type
- request body type
- response type
- promise return type
- error response consideration
- nullable response field
- wrapper response type

---

### [실무]

GET API 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};

type FestivalDetailResponse = {
  festivalId: number;
  title: string;
  description: string;
  imageUrl: string | null;
};

async function getFestivalDetail(
  festivalId: number,
): Promise<ApiResponse<FestivalDetailResponse>> {
  const response = await fetch(`/api/festivals/${festivalId}`);

  if (!response.ok) {
    throw new Error("Failed to load festival detail");
  }

  return await response.json();
}
```

POST API 예:

```typescript
type ReviewCreateRequest = {
  festivalId: number;
  rating: number;
  content: string;
};

type ReviewResponse = {
  reviewId: number;
  rating: number;
  content: string;
};

async function createReview(
  request: ReviewCreateRequest,
): Promise<ApiResponse<ReviewResponse>> {
  const response = await fetch("/api/reviews", {
    method: "POST",
    body: JSON.stringify(request),
  });

  if (!response.ok) {
    throw new Error("Failed to create review");
  }

  return await response.json();
}
```

실무 기준:

- API Function Return Type은 `Promise<ApiResponse<T>>` 형태로 명확히 작성
- Request Body는 별도 Type으로 정의
- Query Parameter는 Params Type으로 정의
- nullable Response field 반영
- Error Response Type은 별도 문서와 연결
- `Promise<any>` 금지

---

### [FAQ]

Q. API Function Type은 왜 중요해?
A. API 호출 parameter와 응답 구조를 Type으로 고정해 호출부의 오류를 줄이기 위해 중요하다.

Q. API 함수 Return Type은 어떻게 써?
A. `Promise<ResponseType>` 또는 `Promise<ApiResponse<T>>` 형태로 작성한다.

Q. API 함수에 any를 써도 돼?
A. 권장하지 않는다. Request Type과 Response Type을 명확히 정의해야 한다.

---

## 7.2 Mapping Function Type

### [개념]

Mapping Function Type은 API Response를 화면에서 사용하기 좋은 ViewModel로 변환하는 함수 Type이다.

```typescript
function toViewModel(response: ResponseType): ViewModelType {
  return mappedValue;
}
```

Mapping Function은 API Type과 UI Type을 분리할 때 중요하다.

---

### [핵심]

Mapping Function 사용 영역:

- API Response to ViewModel
- nullable field fallback
- date string formatting
- image fallback
- label conversion
- enum value to display text
- server field to UI field

---

### [실무]

ViewModel 변환 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  eventStartDate: string;
};

type FestivalCardViewModel = {
  id: number;
  title: string;
  imageUrl: string;
  displayDate: string;
};

function toFestivalCardViewModel(
  response: FestivalInfoResponse,
): FestivalCardViewModel {
  return {
    id: response.festivalId,
    title: response.title,
    imageUrl: response.imageUrl ?? "/default-festival.png",
    displayDate: new Date(response.eventStartDate).toLocaleDateString("ko-KR"),
  };
}
```

목록 변환 예:

```typescript
function toFestivalCardViewModels(
  responses: FestivalInfoResponse[],
): FestivalCardViewModel[] {
  return responses.map(toFestivalCardViewModel);
}
```

실무 기준:

- API Response Type과 ViewModel Type 분리 가능
- Mapping Function Return Type 명시
- nullable fallback 처리
- date string 변환 처리
- Backend field naming과 UI field naming 분리 가능
- Runtime 변환은 Type Annotation이 아니라 Mapping Function에서 수행

---

### [FAQ]

Q. Mapping Function은 왜 필요해?
A. API Response 구조를 화면에서 쓰기 좋은 ViewModel 구조로 변환하기 위해 필요하다.

Q. 날짜 string을 Date로 바꾸는 건 Type이 해줘?
A. 아니다. Mapping Function에서 `new Date()` 같은 Runtime 변환을 해야 한다.

Q. imageUrl null 처리는 어디서 해?
A. Mapping Function 또는 UI Rendering 단계에서 fallback 값을 처리할 수 있다.

---

# 8. Common Mistakes

## 8.1 Function Type Mistakes

### [개념]

Function Type 실수는 parameter Type 누락, return Type 오해, async Return Type 오해, callback Type 부정확성에서 자주 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Function Parameter Type 누락
- Parameter implicitly has an any type 방치
- Return Type을 any로 처리
- async function Return Type을 `T`로 작성
- 반환값 없는 async function을 `void`로 오해
- Optional Parameter와 Nullable Parameter 혼동
- Optional Callback 안전 호출 누락
- Event Type을 any로 처리
- input number value를 number로 오해
- find 결과 undefined 처리 누락
- API Function을 `Promise<any>`로 정의
- Mapping Function Return Type 누락

---

### [실무]

나쁜 예:

```typescript
async function getFestivalList() {
  const response = await fetch("/api/festivals");
  return await response.json();
}

function handleChange(event: any) {
  console.log(event.target.value);
}
```

문제:

- API Response Type 불명확
- Event Type이 any
- 호출부에서 잘못된 property 접근을 TypeScript가 잡기 어려움

개선:

```typescript
import type { ChangeEvent } from "react";

type FestivalInfoResponse = {
  festivalId: number;
  title: string;
};

async function getFestivalList(): Promise<FestivalInfoResponse[]> {
  const response = await fetch("/api/festivals");

  if (!response.ok) {
    throw new Error("Failed to load festival list");
  }

  return await response.json();
}

function handleChange(event: ChangeEvent<HTMLInputElement>): void {
  console.log(event.target.value);
}
```

실무 기준:

- Function Parameter Type 명시
- API Function Return Type 명시
- Event Type에서 any 제거
- async function은 `Promise<T>` 사용
- Optional Callback은 `?.()`로 호출
- find 결과는 undefined 방어

---

### [FAQ]

Q. Function Type에서 가장 흔한 실수는?
A. Parameter Type 누락, async Return Type 오해, API Function Return Type을 any로 두는 것이다.

Q. Parameter implicitly has an any type 오류는 왜 나?
A. Function Parameter Type이 명시되지 않았고 TypeScript가 추론할 수 없기 때문이다.

Q. async 함수 Return Type을 그냥 T로 쓰면 안 돼?
A. 안 된다. async 함수는 항상 Promise를 반환하므로 `Promise<T>`로 작성해야 한다.

---

## 8.2 Callback and Event Mistakes

### [개념]

Callback과 Event Type 실수는 React Component에서 Props 전달, 이벤트 처리, optional callback 호출에서 자주 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Callback Props parameter Type 누락
- Callback Return Type을 any로 작성
- Optional Callback을 바로 호출
- Event 객체를 any로 처리
- DOM Event와 React Event 혼동
- HTML Element Type 잘못 지정
- checkbox value와 checked 혼동
- select value를 literal union으로 바로 단정
- number input value를 number로 단정
- Event Handler에서 불필요한 return 사용

---

### [실무]

나쁜 예:

```typescript
type ModalProps = {
  onClose?: () => void;
};

function closeModal(props: ModalProps): void {
  props.onClose();
}
```

문제:

- `onClose`는 optional callback이므로 undefined일 수 있다.

개선:

```typescript
function closeModal(props: ModalProps): void {
  props.onClose?.();
}
```

이벤트 예:

```typescript
import type { ChangeEvent } from "react";

function handleCheckboxChange(event: ChangeEvent<HTMLInputElement>): boolean {
  return event.target.checked;
}
```

실무 기준:

- optional callback은 optional chaining 사용
- React Event Type을 정확히 import
- target element Type 지정
- checkbox는 checked 사용
- input value는 string으로 처리 후 필요 시 변환
- 외부 string을 literal union으로 단정하지 않음

---

### [FAQ]

Q. Optional Callback을 바로 호출하면 왜 문제야?
A. Callback이 전달되지 않았을 수 있어 undefined 호출 오류가 발생할 수 있다.

Q. React Event를 any로 처리하면 왜 안 좋아?
A. Event target property 접근 오류를 TypeScript가 잡기 어렵고 자동완성 품질이 떨어진다.

Q. checkbox는 value를 읽으면 돼?
A. 체크 여부는 `event.target.checked`를 사용한다.

---

# 9. Review Checklist

## 9.1 Part07 Checklist

### [개념]

TypeScript Foundation Part07 검수는 Function Type, Parameter Type, Return Type, Callback Type, React Event Handler Type, API Function Type 기준을 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] Function Type 정의가 포함되었는가?
- [ ] Function Declaration Type 설명이 포함되었는가?
- [ ] Function Expression Type 설명이 포함되었는가?
- [ ] Required Parameter 설명이 포함되었는가?
- [ ] Optional Parameter 설명이 포함되었는가?
- [ ] Default Parameter 설명이 포함되었는가?
- [ ] Rest Parameter 설명이 포함되었는가?
- [ ] Return Type 설명이 포함되었는가?
- [ ] Void Return Type 설명이 포함되었는가?
- [ ] Promise Return Type 설명이 포함되었는가?
- [ ] Callback Type 설명이 포함되었는가?
- [ ] Callback Props 설명이 포함되었는가?
- [ ] React Event Type 설명이 포함되었는가?
- [ ] Event Target Type 설명이 포함되었는가?
- [ ] Array Method Callback 설명이 포함되었는가?
- [ ] Predicate Callback 설명이 포함되었는가?
- [ ] API Function Type 예제가 포함되었는가?
- [ ] Mapping Function Type 예제가 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Required Section Check
→ Function Type Check
→ Parameter Type Check
→ Return Type Check
→ Callback Type Check
→ React Event Type Check
→ API Function Check
→ Mapping Function Check
→ Common Mistake Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

Part07은 이후 Type Narrowing, Type Guard, Generic, API Type, React TypeScript Readiness 문서의 기반이다.

---

### [FAQ]

Q. Part07에서 가장 중요한 검수 기준은?
A. Function Parameter, Return Type, Callback Props, React Event Handler, API Function Return Type이 명확한지 확인하는 것이다.

Q. Part07이 이후 문서와 어떻게 연결돼?
A. Type Guard Function, Generic Function, API Function, React Event Handler, Mapping Function 작성 기준으로 연결된다.

---

# Retrieval Queries

### [FAQ]

Q. Function Type이 뭐야?
A. 함수의 parameter Type과 return Type을 정의하는 TypeScript Type이다.

Q. 함수 parameter에는 Type을 꼭 써야 해?
A. 대부분 써야 한다. Function Parameter는 TypeScript가 자동 추론하기 어려운 경우가 많다.

Q. Function Return Type은 항상 써야 해?
A. 항상은 아니지만 API 함수, 복잡한 함수, 재사용 함수에는 명시하는 것이 좋다.

Q. 반환값 없는 함수는 어떤 Type이야?
A. `void`를 사용한다.

Q. Function Declaration에서 Type은 어디에 써?
A. parameter 뒤와 함수 괄호 뒤 return 위치에 쓴다. 예: `function add(a: number): number`.

Q. Object Parameter는 어떻게 Type을 붙여?
A. type 또는 interface로 객체 구조를 정의한 뒤 parameter Type으로 사용한다.

Q. Union Parameter를 쓰면 바로 Type별 method를 쓸 수 있어?
A. 아니다. Type Narrowing으로 구체적인 Type을 확인한 뒤 사용해야 한다.

Q. Function Expression에도 Type을 붙일 수 있어?
A. 가능하다. parameter와 return Type을 직접 쓰거나 Function Type Alias를 사용할 수 있다.

Q. Function Type Alias는 언제 써?
A. 같은 함수 구조가 반복되거나 Callback Props로 재사용할 때 사용한다.

Q. Mapper Function은 Return Type을 써야 해?
A. 권장한다. API Response를 ViewModel로 변환할 때 output 구조를 명확히 할 수 있다.

Q. Required Parameter는 뭐야?
A. 함수 호출 시 반드시 전달해야 하는 parameter다.

Q. parameter에 ?가 없으면 필수야?
A. 그렇다. TypeScript 함수 parameter는 기본적으로 필수다.

Q. API path parameter는 required로 두면 돼?
A. 대부분 그렇다. `/api/festivals/{id}` 같은 id는 필수 parameter다.

Q. Optional Parameter는 어떻게 써?
A. parameter 이름 뒤에 `?`를 붙인다. 예: `page?: number`.

Q. Optional Parameter는 null도 허용해?
A. 아니다. 기본적으로 `T | undefined`를 의미한다. null도 허용하려면 `T | null`을 명시해야 한다.

Q. Optional Parameter가 많으면 어떻게 해?
A. Object Parameter로 묶고 Type Alias나 Interface로 정의하는 것이 좋다.

Q. Default Parameter는 뭐야?
A. argument가 생략되거나 undefined일 때 사용할 기본값을 지정하는 parameter다.

Q. Optional Parameter와 Default Parameter 차이는?
A. Optional Parameter는 생략 가능성을 표현하고, Default Parameter는 생략 시 사용할 기본값을 제공한다.

Q. null을 넘겨도 default 값이 적용돼?
A. 아니다. default value는 보통 undefined에 적용된다. null은 별도 처리해야 한다.

Q. Rest Parameter는 뭐야?
A. 여러 argument를 배열로 받는 parameter다.

Q. Rest Parameter Type은 어떻게 써?
A. `...numbers: number[]`처럼 배열 Type으로 작성한다.

Q. Rest Parameter는 어디에 위치해야 해?
A. 함수 parameter 목록의 마지막에 위치해야 한다.

Q. Return Type은 어디에 써?
A. 함수 parameter 괄호 뒤에 쓴다. 예: `function getName(): string`.

Q. null을 반환할 수 있으면 어떻게 써?
A. `string | null`, `User | null`처럼 Union Type으로 작성한다.

Q. void는 언제 써?
A. 반환값이 없는 함수의 Return Type에 사용한다.

Q. Callback Props에서 `() => void`는 무슨 뜻이야?
A. parameter 없이 호출되고 반환값이 없는 callback function이라는 뜻이다.

Q. Event Handler Return Type은 보통 뭐야?
A. 대부분 `void`를 사용한다.

Q. async 함수 Return Type은 어떻게 써?
A. `Promise<T>` 형태로 작성한다.

Q. async 함수에서 반환값이 없으면 뭐라고 써?
A. `Promise<void>`로 작성한다.

Q. API Function Return Type은 왜 중요해?
A. 서버 응답 구조를 호출부에서 안전하게 사용할 수 있게 하기 때문이다.

Q. Callback Type이 뭐야?
A. 다른 함수나 Component에 전달되는 함수의 parameter와 return Type을 정의하는 Type이다.

Q. Callback Props는 어떻게 Type을 써?
A. `(parameter: Type) => ReturnType` 형태로 작성한다.

Q. Optional Callback은 어떻게 호출해?
A. `onClose?.()`처럼 optional chaining으로 안전하게 호출한다.

Q. Callback Props는 왜 필요해?
A. 자식 Component 이벤트를 부모 Component로 전달하기 위해 필요하다.

Q. onClick Type은 보통 어떻게 써?
A. 단순 클릭 callback은 `onClick: () => void`로 쓸 수 있다.

Q. onSelect처럼 id를 넘기는 callback은 어떻게 써?
A. `onSelect: (id: number) => void`처럼 parameter Type을 명시한다.

Q. input onChange event Type은 뭐야?
A. 일반적으로 `ChangeEvent<HTMLInputElement>`를 사용한다.

Q. form onSubmit event Type은 뭐야?
A. 일반적으로 `FormEvent<HTMLFormElement>`를 사용한다.

Q. button onClick event Type은 뭐야?
A. 일반적으로 `MouseEvent<HTMLButtonElement>`를 사용할 수 있다.

Q. React Event Type은 어디서 가져와?
A. `react`에서 type-only import로 가져올 수 있다.

Q. input number의 value는 number야?
A. 아니다. input value는 대부분 string이다. 숫자로 쓰려면 Number로 변환해야 한다.

Q. checkbox 값은 어떻게 읽어?
A. `event.target.checked`를 사용하며 Type은 boolean이다.

Q. select value Type은 뭐야?
A. 기본적으로 string이다. literal union으로 쓰려면 허용 값 검증이 필요하다.

Q. map callback parameter Type은 직접 써야 해?
A. 배열 Type이 명확하면 TypeScript가 element Type으로 추론한다.

Q. find 결과는 왜 undefined가 붙어?
A. 조건에 맞는 요소가 없을 수 있기 때문이다.

Q. filter로 null을 제거하면 Type도 자동으로 좁혀져?
A. 단순 조건에서는 충분하지 않을 수 있다. 필요한 경우 Type Guard를 사용한다.

Q. Predicate Callback이 뭐야?
A. 값을 검사해 boolean을 반환하는 callback 함수다.

Q. Predicate 함수 이름은 어떻게 짓는 게 좋아?
A. `isValid`, `hasImage`, `canSubmit`처럼 boolean 의미가 드러나게 짓는 것이 좋다.

Q. Predicate와 Type Guard는 같아?
A. Type Guard는 Predicate의 특수한 형태로, true일 때 TypeScript에 더 좁은 Type을 알려준다.

Q. API Function Type은 왜 중요해?
A. API 호출 parameter와 응답 구조를 Type으로 고정해 호출부의 오류를 줄이기 위해 중요하다.

Q. API 함수 Return Type은 어떻게 써?
A. `Promise<ResponseType>` 또는 `Promise<ApiResponse<T>>` 형태로 작성한다.

Q. API 함수에 any를 써도 돼?
A. 권장하지 않는다. Request Type과 Response Type을 명확히 정의해야 한다.

Q. Mapping Function은 왜 필요해?
A. API Response 구조를 화면에서 쓰기 좋은 ViewModel 구조로 변환하기 위해 필요하다.

Q. 날짜 string을 Date로 바꾸는 건 Type이 해줘?
A. 아니다. Mapping Function에서 `new Date()` 같은 Runtime 변환을 해야 한다.

Q. imageUrl null 처리는 어디서 해?
A. Mapping Function 또는 UI Rendering 단계에서 fallback 값을 처리할 수 있다.

Q. Function Type에서 가장 흔한 실수는?
A. Parameter Type 누락, async Return Type 오해, API Function Return Type을 any로 두는 것이다.

Q. Parameter implicitly has an any type 오류는 왜 나?
A. Function Parameter Type이 명시되지 않았고 TypeScript가 추론할 수 없기 때문이다.

Q. async 함수 Return Type을 그냥 T로 쓰면 안 돼?
A. 안 된다. async 함수는 항상 Promise를 반환하므로 `Promise<T>`로 작성해야 한다.

Q. Optional Callback을 바로 호출하면 왜 문제야?
A. Callback이 전달되지 않았을 수 있어 undefined 호출 오류가 발생할 수 있다.

Q. React Event를 any로 처리하면 왜 안 좋아?
A. Event target property 접근 오류를 TypeScript가 잡기 어렵고 자동완성 품질이 떨어진다.

Q. checkbox는 value를 읽으면 돼?
A. 체크 여부는 `event.target.checked`를 사용한다.

Q. TypeScript Part07의 핵심은 뭐야?
A. Function Parameter, Return Type, Callback Props, React Event Handler, API Function Return Type을 명확히 정의하는 것이다.

Q. TypeScript Part07 다음 문서는 뭐가 좋아?
A. Type Narrowing and Type Guard 문서가 적합하다.
