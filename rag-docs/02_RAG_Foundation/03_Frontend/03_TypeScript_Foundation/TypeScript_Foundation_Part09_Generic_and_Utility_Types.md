# TypeScript Foundation Part09 - Generic and Utility Types

---

# 1. Generic

## 1.1 Generic Definition

### [개념]

Generic은 Type을 parameter처럼 받아 재사용 가능한 Type, Function, Interface, Type Alias를 만드는 TypeScript 문법이다.

```typescript
function identity<T>(value: T): T {
  return value;
}
```

Generic은 실제 값이 아니라 Type을 재사용하기 위한 구조다.

같은 로직을 다양한 Type에 안전하게 적용할 수 있다.

---

### [핵심]

Generic 핵심:

- type parameter
- reusable type
- reusable function
- generic function
- generic type alias
- generic interface
- generic constraint
- API response generic
- array generic
- promise generic
- utility type 기반

대표 형태:

```typescript
function functionName<T>(value: T): T {
  return value;
}
```

실무 주요 사용 영역:

- `ApiResponse<T>`
- `SliceResponse<T>`
- `PageResponse<T>`
- `Promise<T>`
- `Array<T>`
- reusable utility function
- reusable component props
- reusable mapper function

---

### [실무]

2026 Frontend 실무 기준에서 Generic은 API Response Wrapper, List Response, Slice Response, Utility Function에 가장 많이 사용된다.

API Response Generic 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};
```

사용 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
};

type FestivalListResponse = ApiResponse<FestivalInfoResponse[]>;
```

Utility Function 예:

```typescript
function getFirst<T>(items: T[]): T | undefined {
  return items[0];
}
```

실무 기준:

- 구조는 같고 내부 data Type만 다르면 Generic 사용
- API wrapper는 Generic Type Alias로 정의
- 목록 처리 Utility에는 Generic Function 사용
- Generic 이름은 기본적으로 `T` 사용 가능
- 의미가 필요하면 `TData`, `TItem`, `TResponse` 사용

---

### [FAQ]

Q. Generic이 뭐야?
A. Type을 parameter처럼 받아 재사용 가능한 Type이나 Function을 만드는 TypeScript 문법이다.

Q. Generic은 왜 써?
A. Type은 다르지만 구조가 같은 로직을 Type Safety를 유지하면서 재사용하기 위해 쓴다.

Q. Generic의 T는 무슨 뜻이야?
A. 관례적으로 Type을 의미하는 Type Parameter 이름이다. 다른 이름도 사용할 수 있다.

Q. Generic은 Runtime에 남아?
A. 아니다. Generic Type 정보는 Compile Time에만 사용되고 Runtime에는 남지 않는다.

---

## 1.2 Generic Function

### [개념]

Generic Function은 Type Parameter를 받아 여러 Type에 재사용할 수 있는 함수다.

```typescript
function getFirst<T>(items: T[]): T | undefined {
  return items[0];
}
```

Generic Function은 입력 Type과 출력 Type의 관계를 유지할 수 있다.

---

### [핵심]

Generic Function 핵심:

- Type Parameter 사용
- input Type과 output Type 관계 유지
- array utility에 적합
- mapper utility에 적합
- identity function
- reusable helper
- Type Inference와 함께 사용

Generic Function 사용 영역:

- getFirst
- findById
- mapList
- createOption
- groupBy basics
- safeParse
- API helper

---

### [실무]

배열 첫 요소 예:

```typescript
function getFirst<T>(items: T[]): T | undefined {
  return items[0];
}

const firstName = getFirst(["jun", "kim"]);
const firstNumber = getFirst([1, 2, 3]);
```

결과 Type:

```text
firstName → string | undefined
firstNumber → number | undefined
```

Mapper Function 예:

```typescript
function mapList<TInput, TOutput>(
  items: TInput[],
  mapper: (item: TInput) => TOutput,
): TOutput[] {
  return items.map(mapper);
}
```

실무 기준:

- 입력 Type과 반환 Type이 연결되면 Generic 사용
- Generic이 필요 없는 단순 함수에는 사용하지 않음
- TypeScript가 Type Parameter를 추론할 수 있으면 명시 생략 가능
- Return Type에 undefined 가능성 반영
- Generic Function에 `any` 사용 지양

---

### [FAQ]

Q. Generic Function은 언제 써?
A. 같은 함수 로직을 여러 Type에 재사용하면서 입력과 출력 Type 관계를 유지해야 할 때 쓴다.

Q. Generic Type Parameter를 직접 써야 해?
A. TypeScript가 추론할 수 있으면 생략해도 된다.

Q. `getFirst<T>`의 반환 Type에 왜 undefined가 붙어?
A. 배열이 비어 있으면 첫 번째 요소가 없을 수 있기 때문이다.

---

## 1.3 Generic Type Alias

### [개념]

Generic Type Alias는 Type Parameter를 받는 재사용 가능한 Type Alias다.

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};
```

Generic Type Alias는 공통 구조는 유지하고 내부 Type만 바꿔야 할 때 유용하다.

---

### [핵심]

Generic Type Alias 사용 영역:

- API Response Wrapper
- Error Wrapper
- Slice Response
- Page Response
- Option Type
- Select Item Type
- Async State Type
- Result Type

대표 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};
```

---

### [실무]

API Response 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
};

type ReviewResponse = {
  reviewId: number;
  content: string;
};

type FestivalResponse = ApiResponse<FestivalInfoResponse>;
type FestivalListResponse = ApiResponse<FestivalInfoResponse[]>;
type ReviewListResponse = ApiResponse<ReviewResponse[]>;
```

Async State 예:

```typescript
type ApiState<T> =
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; message: string };
```

Option Type 예:

```typescript
type SelectOption<TValue> = {
  label: string;
  value: TValue;
};

type RegionOption = SelectOption<string>;
type PageSizeOption = SelectOption<number>;
```

실무 기준:

- API 공통 응답 구조는 Generic Type Alias 사용
- Select Option처럼 label / value 구조는 Generic 사용 가능
- 상태별 data Type만 달라지면 Generic State 사용 가능
- Generic Type 이름은 의미 있게 작성
- 너무 복잡한 Generic Type Alias는 Foundation 범위에서 지양

---

### [FAQ]

Q. Generic Type Alias는 언제 써?
A. 공통 Type 구조는 같고 내부 data Type만 달라질 때 사용한다.

Q. ApiResponse<T>는 왜 Generic으로 만들어?
A. success, message 구조는 공통이고 data Type만 API마다 달라지기 때문이다.

Q. Generic Type Alias가 너무 복잡하면 어떻게 해?
A. 명시적 Type으로 분리하거나 Advanced Type 문서로 분리하는 것이 좋다.

---

## 1.4 Generic Interface

### [개념]

Generic Interface는 Type Parameter를 받는 Interface다.

```typescript
interface Repository<T> {
  findAll(): T[];
  findById(id: number): T | undefined;
}
```

Generic Interface는 객체 구조나 계약이 같고 내부 Type만 달라질 때 사용한다.

---

### [핵심]

Generic Interface 사용 영역:

- repository pattern
- service contract
- list props
- table props
- form field props
- reusable component props
- response interface

장점:

- 확장 가능한 객체 구조
- 공통 계약 정의
- 내부 Type 재사용
- 객체 중심 Generic 표현

---

### [실무]

List Props 예:

```typescript
interface ListProps<TItem> {
  items: TItem[];
  renderItem: (item: TItem) => string;
}
```

Table Row 예:

```typescript
interface TableProps<TRow> {
  rows: TRow[];
  getRowId: (row: TRow) => number | string;
}
```

API Client Contract 예:

```typescript
interface ApiClient<TResponse> {
  get(): Promise<TResponse>;
}
```

실무 기준:

- 객체 계약이 확장 가능하면 Generic Interface 사용 가능
- React Component Props에도 Generic Interface 사용 가능
- Type Alias와 Interface 중 팀 컨벤션 우선
- Generic Props는 과도하게 복잡해지지 않도록 주의
- 재사용 목적이 명확할 때만 Generic 적용

---

### [FAQ]

Q. Generic Interface는 언제 써?
A. 객체 구조나 계약은 같고 내부 Type만 달라질 때 사용한다.

Q. React Props도 Generic Interface로 만들 수 있어?
A. 가능하다. 재사용 가능한 List, Table, Select Component에서 사용할 수 있다.

Q. Generic Interface와 Generic Type Alias 중 뭐가 좋아?
A. 객체 확장과 계약 중심이면 Interface, Union이나 wrapper 조합이면 Type Alias가 편하다.

---

# 2. Generic Constraint

## 2.1 Generic Constraint Definition

### [개념]

Generic Constraint는 Generic Type Parameter가 특정 구조를 만족하도록 제한하는 문법이다.

```typescript
function getId<T extends { id: number }>(item: T): number {
  return item.id;
}
```

Constraint를 사용하면 Generic Type에서도 특정 property가 존재함을 보장할 수 있다.

---

### [핵심]

Generic Constraint 핵심:

- `extends` 사용
- property 존재 보장
- safe property access
- reusable function
- Type Parameter 제한
- generic limitation
- object shape constraint

사용 영역:

- id 기반 검색
- key 기반 접근
- option value 제한
- API item list 처리
- table row id 처리

---

### [실무]

id 기반 함수 예:

```typescript
function findById<T extends { id: number }>(
  items: T[],
  id: number,
): T | undefined {
  return items.find((item) => item.id === id);
}
```

다양한 Type에 사용:

```typescript
type User = {
  id: number;
  nickname: string;
};

type Festival = {
  id: number;
  title: string;
};

const user = findById<User>([{ id: 1, nickname: "jun" }], 1);
const festival = findById<Festival>([{ id: 1, title: "Spring" }], 1);
```

실무 기준:

- Generic 내부에서 특정 property를 사용하려면 Constraint 필요
- Constraint는 필요한 최소 구조로 제한
- 너무 복잡한 Constraint는 가독성 저하
- Foundation 문서에서는 기본 Constraint 중심
- `extends`는 여기서 class 상속이 아니라 Type 조건 의미

---

### [FAQ]

Q. Generic Constraint가 뭐야?
A. Generic Type Parameter가 특정 구조를 만족하도록 제한하는 문법이다.

Q. Generic에서 property를 바로 못 쓰는 이유는?
A. T가 어떤 Type인지 모르기 때문에 해당 property가 있는지 TypeScript가 확신할 수 없기 때문이다.

Q. Generic Constraint의 extends는 class 상속이야?
A. 아니다. 여기서는 Type이 특정 구조를 만족해야 한다는 의미다.

---

## 2.2 Key Constraint

### [개념]

Key Constraint는 객체의 key만 허용하도록 Generic Type Parameter를 제한하는 방식이다.

`keyof`와 `extends`를 함께 사용한다.

```typescript
function getValue<T, K extends keyof T>(object: T, key: K): T[K] {
  return object[key];
}
```

Key Constraint는 객체 property 접근을 안전하게 만드는 데 사용된다.

---

### [핵심]

Key Constraint 핵심:

- `keyof`
- `K extends keyof T`
- safe property access
- return type relation
- dynamic key access
- object utility function

주의:

- key 문자열을 아무거나 허용하지 않음
- 객체에 존재하는 key만 허용
- 반환 Type은 해당 property Type과 연결
- 너무 복잡한 key utility는 Advanced Type 범위

---

### [실무]

객체 값 접근 예:

```typescript
function getValue<T, K extends keyof T>(object: T, key: K): T[K] {
  return object[key];
}

type User = {
  userId: number;
  nickname: string;
};

const user: User = {
  userId: 1,
  nickname: "jun",
};

const nickname = getValue(user, "nickname");
```

결과 Type:

```text
nickname → string
```

잘못된 key:

```typescript
getValue(user, "email");
```

문제:

- `email`은 User Type의 key가 아니다.

실무 기준:

- 동적 key 접근이 필요하면 `keyof` 활용
- API Response field 접근 utility에 사용 가능
- 잘못된 key 문자열을 Compile Time에 방지
- RAG Foundation에서는 기본 사용법까지만 포함

---

### [FAQ]

Q. keyof는 뭐야?
A. 객체 Type의 property 이름들을 Union Type으로 만드는 TypeScript 연산자다.

Q. `K extends keyof T`는 무슨 뜻이야?
A. K는 T 객체에 존재하는 key 중 하나여야 한다는 뜻이다.

Q. getValue 함수는 왜 안전해?
A. key가 실제 객체 Type의 property로 제한되고 반환 Type도 해당 property Type으로 연결되기 때문이다.

---

## 2.3 Generic Default Type

### [개념]

Generic Default Type은 Type Parameter에 기본 Type을 지정하는 방식이다.

```typescript
type ApiResponse<T = unknown> = {
  success: boolean;
  data: T;
  message: string;
};
```

Type Parameter를 명시하지 않았을 때 기본 Type이 사용된다.

---

### [핵심]

Generic Default Type 특징:

- 기본 Type 지정
- Type Parameter 생략 가능
- fallback type 제공
- reusable generic type 편의성 증가
- unknown default 권장 가능

주의:

- 기본값을 any로 두면 Type Safety 저하
- default가 실제 사용 의도를 숨기지 않도록 주의
- API data Type은 가능한 명시

---

### [실무]

ApiResponse Default 예:

```typescript
type ApiResponse<TData = unknown> = {
  success: boolean;
  data: TData;
  message: string;
};
```

사용 예:

```typescript
type UnknownApiResponse = ApiResponse;
type FestivalApiResponse = ApiResponse<FestivalInfoResponse>;
```

Component Props Default 예:

```typescript
type SelectOption<TValue = string> = {
  label: string;
  value: TValue;
};
```

실무 기준:

- Generic Default는 편의용으로 사용
- `any` default 지양
- unknown default는 안전한 fallback
- 중요한 API Response는 명시적 Type Parameter 사용
- 너무 많은 Default Generic은 가독성 저하

---

### [FAQ]

Q. Generic Default Type은 뭐야?
A. Generic Type Parameter를 생략했을 때 사용할 기본 Type을 지정하는 방식이다.

Q. Default Generic에 any를 써도 돼?
A. 권장하지 않는다. unknown이나 명확한 기본 Type이 더 안전하다.

Q. ApiResponse<T = unknown>은 무슨 뜻이야?
A. T를 지정하지 않으면 data Type을 unknown으로 사용한다는 뜻이다.

---

# 3. Generic in API Modeling

## 3.1 ApiResponse Generic

### [개념]

ApiResponse Generic은 Backend 공통 응답 wrapper를 TypeScript Generic으로 표현한 Type이다.

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};
```

공통 응답 구조는 유지하고 `data` Type만 API마다 다르게 지정한다.

---

### [핵심]

ApiResponse Generic 구성:

- `success: boolean`
- `data: T`
- `message: string`
- common response wrapper
- reusable response type
- API response consistency
- Backend DTO relation

사용 예:

- `ApiResponse<UserResponse>`
- `ApiResponse<FestivalInfoResponse[]>`
- `ApiResponse<SliceResponse<ReviewResponse>>`
- `ApiResponse<null>`

---

### [실무]

단건 응답:

```typescript
type UserResponse = {
  userId: number;
  nickname: string;
};

type UserApiResponse = ApiResponse<UserResponse>;
```

목록 응답:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
};

type FestivalListApiResponse = ApiResponse<FestivalInfoResponse[]>;
```

null data 응답:

```typescript
type DeleteResponse = ApiResponse<null>;
```

실무 기준:

- Backend ApiResponse 구조와 일치시킴
- data가 없는 성공 응답은 `null` 또는 `void` 정책 확인
- List Response는 `T[]`로 지정
- Slice / Page Response는 중첩 Generic 사용
- Error Response는 별도 Type으로 분리 가능

---

### [FAQ]

Q. ApiResponse<T>는 왜 필요해?
A. 공통 응답 구조는 재사용하고 data Type만 API마다 다르게 지정하기 위해 필요하다.

Q. 목록 응답은 어떻게 써?
A. `ApiResponse<FestivalInfoResponse[]>`처럼 data Type에 배열을 넣는다.

Q. data가 없으면 어떻게 써?
A. Backend 정책에 따라 `ApiResponse<null>` 또는 별도 응답 Type으로 정의할 수 있다.

---

## 3.2 SliceResponse Generic

### [개념]

SliceResponse Generic은 무한 스크롤 또는 더보기 목록 응답 구조를 Generic으로 표현한 Type이다.

```typescript
type SliceResponse<T> = {
  content: T[];
  hasNext: boolean;
  number: number;
  size: number;
};
```

SliceResponse는 Review, Chat Message, Notification, Festival List 같은 목록 UI에 적합하다.

---

### [핵심]

SliceResponse 구성:

- `content: T[]`
- `hasNext: boolean`
- `number: number`
- `size: number`
- list data
- pagination info
- infinite scroll
- load more UI

사용 예:

- `SliceResponse<ReviewResponse>`
- `SliceResponse<ChatMessageResponse>`
- `SliceResponse<NotificationResponse>`
- `ApiResponse<SliceResponse<FestivalInfoResponse>>`

---

### [실무]

Review Slice 예:

```typescript
type ReviewResponse = {
  reviewId: number;
  content: string;
  rating: number;
};

type ReviewSliceResponse = SliceResponse<ReviewResponse>;
type ReviewSliceApiResponse = ApiResponse<ReviewSliceResponse>;
```

Chat Message Slice 예:

```typescript
type ChatMessageResponse = {
  messageId: number;
  message: string | null;
  imageUrl: string | null;
  createdAt: string;
};

type ChatMessageSliceResponse = SliceResponse<ChatMessageResponse>;
```

실무 기준:

- 무한 스크롤 목록은 SliceResponse 사용
- `content` element Type은 명확히 지정
- `hasNext`로 다음 요청 여부 판단
- number / size는 Backend Slice 필드와 정합성 유지
- PageResponse와 SliceResponse 구분

---

### [FAQ]

Q. SliceResponse<T>는 언제 써?
A. 무한 스크롤이나 더보기 목록처럼 다음 페이지 존재 여부가 중요한 응답에 사용한다.

Q. SliceResponse와 PageResponse 차이는?
A. Slice는 보통 hasNext 중심이고 Page는 totalElements, totalPages 같은 전체 개수 정보를 포함한다.

Q. `ApiResponse<SliceResponse<T>>`처럼 중첩 Generic을 써도 돼?
A. 가능하다. 공통 wrapper 안에 slice data를 넣는 구조를 표현할 수 있다.

---

## 3.3 PageResponse Generic

### [개념]

PageResponse Generic은 페이지 번호 기반 목록 응답 구조를 Generic으로 표현한 Type이다.

```typescript
type PageResponse<T> = {
  content: T[];
  totalElements: number;
  totalPages: number;
  number: number;
  size: number;
};
```

PageResponse는 전체 개수와 전체 페이지 수가 필요한 목록 화면에 적합하다.

---

### [핵심]

PageResponse 구성:

- `content: T[]`
- `totalElements: number`
- `totalPages: number`
- `number: number`
- `size: number`
- page navigation
- total count
- table pagination

사용 영역:

- admin list
- search result
- table page
- management screen
- page number navigation

---

### [실무]

Festival Page 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
};

type FestivalPageResponse = PageResponse<FestivalInfoResponse>;
type FestivalPageApiResponse = ApiResponse<FestivalPageResponse>;
```

Page UI 기준:

```typescript
function canMoveNextPage<T>(page: PageResponse<T>): boolean {
  return page.number + 1 < page.totalPages;
}
```

실무 기준:

- 전체 페이지 수가 필요하면 PageResponse 사용
- 무한 스크롤이면 SliceResponse 사용
- Backend Page 필드명과 정합성 유지
- content Type은 명확히 지정
- totalElements / totalPages 값은 number

---

### [FAQ]

Q. PageResponse<T>는 언제 써?
A. 전체 개수와 전체 페이지 수가 필요한 페이지네이션 목록에 사용한다.

Q. SliceResponse 대신 PageResponse를 써도 돼?
A. 가능하지만 무한 스크롤에는 SliceResponse가 더 가볍고 적합할 수 있다.

Q. PageResponse의 content Type은 어떻게 지정해?
A. `PageResponse<FestivalInfoResponse>`처럼 목록 element Type을 Generic으로 넣는다.

---

# 4. Utility Type

## 4.1 Utility Type Definition

### [개념]

Utility Type은 기존 Type을 변형해 새로운 Type을 쉽게 만드는 TypeScript 내장 Type이다.

```typescript
type UserUpdateRequest = Partial<User>;
```

Utility Type은 Request Type, ViewModel Type, Form Type, Picked Type을 만들 때 유용하다.

---

### [핵심]

Foundation 필수 Utility Type:

- `Partial<T>`
- `Required<T>`
- `Pick<T, K>`
- `Omit<T, K>`
- `Record<K, V>`
- `Readonly<T>`
- `ReturnType<T>`
- `Parameters<T>`

Utility Type 사용 목적:

- 기존 Type 재사용
- 일부 field 선택
- 일부 field 제외
- optional 변환
- readonly 변환
- key-value map 표현
- function return 추출

---

### [실무]

기본 Type:

```typescript
type User = {
  userId: number;
  nickname: string;
  email: string;
  profileImageUrl: string | null;
};
```

Utility Type 예:

```typescript
type UserUpdateRequest = Partial<User>;
type UserSummary = Pick<User, "userId" | "nickname">;
type UserCreateRequest = Omit<User, "userId">;
type ReadonlyUser = Readonly<User>;
```

실무 기준:

- Utility Type은 중복 Type 작성 줄이기에 유용
- Backend Request DTO와 완전히 같지 않을 수 있음
- Utility Type 남용 시 의미가 흐려질 수 있음
- 중요한 API Request Type은 명시적으로 작성하는 것이 더 명확할 수 있음
- RAG 검색성에는 명시적 Type 이름이 유리

---

### [FAQ]

Q. Utility Type이 뭐야?
A. 기존 Type을 변형해 새 Type을 쉽게 만드는 TypeScript 내장 Type이다.

Q. Utility Type은 왜 써?
A. 중복 Type 작성을 줄이고 기존 Type에서 일부 property를 선택하거나 optional로 바꾸기 위해 쓴다.

Q. Utility Type은 무조건 쓰는 게 좋아?
A. 아니다. 복잡하거나 API 계약이 명확해야 하는 경우 명시적 Type이 더 좋을 수 있다.

---

## 4.2 Partial

### [개념]

`Partial<T>`는 객체 Type의 모든 property를 optional property로 변환하는 Utility Type이다.

```typescript
type UserUpdateRequest = Partial<User>;
```

Partial은 수정 요청, 임시 상태, form draft에 사용할 수 있다.

---

### [핵심]

Partial 특징:

- 모든 property를 optional로 변경
- update request에 사용 가능
- patch object에 사용 가능
- form draft에 사용 가능
- nested object는 deep partial이 아님
- 필수 field까지 optional이 되므로 주의

---

### [실무]

기본 예:

```typescript
type User = {
  userId: number;
  nickname: string;
  email: string;
};

type UserUpdateRequest = Partial<User>;
```

의미:

```typescript
type UserUpdateRequest = {
  userId?: number;
  nickname?: string;
  email?: string;
};
```

주의:

```typescript
type ReviewCreateRequest = Partial<Review>;
```

문제:

- 생성 요청에서 반드시 필요한 rating, content까지 optional이 될 수 있다.
- API Request 계약이 약해진다.

개선:

```typescript
type ReviewUpdateRequest = {
  rating?: number;
  content?: string;
};
```

실무 기준:

- Patch / Update에는 Partial 사용 가능
- Create Request에는 무분별한 Partial 지양
- server-generated field가 포함되지 않도록 주의
- API 계약이 중요하면 명시적 Request Type 작성
- Deep Partial은 Foundation 범위 밖

---

### [FAQ]

Q. Partial은 언제 써?
A. 객체의 모든 property를 optional로 만들 때 사용한다. 수정 요청이나 draft 상태에 사용할 수 있다.

Q. Partial은 nested object도 모두 optional로 만들어?
A. 아니다. 기본 Partial은 1단계 property만 optional로 만든다.

Q. Create Request에 Partial을 써도 돼?
A. 권장하지 않는다. 필수 field까지 optional이 되어 API 계약이 약해질 수 있다.

---

## 4.3 Required

### [개념]

`Required<T>`는 객체 Type의 모든 optional property를 required property로 변환하는 Utility Type이다.

```typescript
type CompleteUser = Required<UserDraft>;
```

Required는 optional field가 모두 채워진 상태를 표현할 때 사용한다.

---

### [핵심]

Required 특징:

- optional property를 required로 변경
- form completion state 표현 가능
- config default 적용 후 Type 표현 가능
- API 전송 직전 검증 완료 상태 표현 가능

주의:

- 실제 Runtime 값이 채워지는 것은 아님
- Type만 required로 바뀜
- Runtime Validation과 구분
- nullable field는 null 가능성이 그대로 남음

---

### [실무]

Form Draft 예:

```typescript
type SignupFormDraft = {
  email?: string;
  password?: string;
  nickname?: string;
};

type CompleteSignupForm = Required<SignupFormDraft>;
```

Default Config 예:

```typescript
type TableConfig = {
  pageSize?: number;
  showHeader?: boolean;
};

type ResolvedTableConfig = Required<TableConfig>;
```

주의:

```typescript
const form = draft as Required<SignupFormDraft>;
```

문제:

- Type Assertion만으로 실제 값이 채워지지 않는다.
- Runtime Validation이 필요하다.

실무 기준:

- Required는 검증 완료 후 Type 표현에 사용
- 실제 값 채움은 default merge 또는 validation으로 처리
- Type 변환과 Runtime 처리 구분
- nullable field는 별도 처리

---

### [FAQ]

Q. Required는 언제 써?
A. optional property를 모두 required로 바꿔 완성된 상태를 표현할 때 사용한다.

Q. Required를 쓰면 Runtime 값도 채워져?
A. 아니다. Type만 바뀐다. 실제 값은 validation이나 default 처리로 채워야 한다.

Q. Required가 null도 제거해?
A. 아니다. nullable field의 null 가능성은 그대로 남는다.

---

## 4.4 Pick

### [개념]

`Pick<T, K>`는 기존 Type에서 특정 property만 선택해 새로운 Type을 만드는 Utility Type이다.

```typescript
type UserSummary = Pick<User, "userId" | "nickname">;
```

Pick은 요약 응답, 카드 UI, 일부 field만 필요한 Props에 유용하다.

---

### [핵심]

Pick 특징:

- 기존 Type에서 일부 property 선택
- property 이름은 keyof T 중 하나
- summary type 생성
- props type 생성
- view model 일부 생성
- 중복 Type 작성 감소

주의:

- 원본 Type과 API DTO가 항상 같은 것은 아님
- 선택한 field 의미가 API 계약과 맞는지 확인
- 너무 많은 Pick 조합은 검색성 저하 가능

---

### [실무]

기본 Type:

```typescript
type User = {
  userId: number;
  nickname: string;
  email: string;
  profileImageUrl: string | null;
};
```

Pick 사용:

```typescript
type UserSummary = Pick<User, "userId" | "nickname">;
```

Props 예:

```typescript
type UserNameProps = Pick<User, "nickname">;
```

실무 기준:

- 같은 원본 Type에서 일부 field만 필요할 때 사용
- 카드 / 요약 / 작은 Props에 유용
- API Response Type은 실제 Backend DTO와 다르면 별도 정의
- RAG 검색성이 필요하면 명시적 Type 이름 부여
- Pick 남용보다 명확한 Summary Type도 고려

---

### [FAQ]

Q. Pick은 언제 써?
A. 기존 Type에서 일부 property만 선택해 새 Type을 만들 때 사용한다.

Q. Pick의 두 번째 인자는 뭐야?
A. 선택할 property 이름의 union이다. 예: `"userId" | "nickname"`.

Q. API Summary Response를 Pick으로 만들어도 돼?
A. 가능하지만 실제 Backend 응답 구조와 정확히 일치하는지 확인해야 한다.

---

## 4.5 Omit

### [개념]

`Omit<T, K>`는 기존 Type에서 특정 property를 제외해 새로운 Type을 만드는 Utility Type이다.

```typescript
type UserCreateRequest = Omit<User, "userId">;
```

Omit은 생성 요청에서 서버 생성 field를 제외하거나 화면에 필요 없는 field를 제거할 때 유용하다.

---

### [핵심]

Omit 특징:

- 기존 Type에서 일부 property 제외
- server-generated field 제거
- sensitive field 제거
- create request 구성
- props에서 불필요한 field 제외
- view model 변환에 사용 가능

주의:

- 제외만으로 API Request가 정확해지지 않을 수 있음
- nullable / optional 정책 확인 필요
- 민감정보 Type 포함 여부 주의
- Omit 남용 시 의미가 불명확해질 수 있음

---

### [실무]

기본 Type:

```typescript
type User = {
  userId: number;
  email: string;
  password: string;
  nickname: string;
};
```

Create Request 예:

```typescript
type UserCreateRequest = Omit<User, "userId">;
```

민감정보 제외 예:

```typescript
type PublicUser = Omit<User, "password">;
```

명시적 Type이 더 좋은 경우:

```typescript
type SignupRequest = {
  email: string;
  password: string;
  nickname: string;
};
```

실무 기준:

- server-generated field 제외에 Omit 사용 가능
- 민감정보 제외에 Omit 사용 가능
- API Request가 독립 계약이면 명시적 Type 권장
- Backend DTO와 정합성 확인
- Omit 체인이 길어지면 별도 Type 작성

---

### [FAQ]

Q. Omit은 언제 써?
A. 기존 Type에서 특정 property를 제외한 Type이 필요할 때 사용한다.

Q. Create Request는 Omit으로 만들면 돼?
A. 가능하지만 실제 생성 요청 구조와 정확히 맞는지 확인해야 한다.

Q. Omit과 Pick 중 뭐가 달라?
A. Pick은 필요한 property를 선택하고 Omit은 제외할 property를 제거한다.

---

## 4.6 Record

### [개념]

`Record<K, V>`는 key Type과 value Type을 지정해 객체 Type을 만드는 Utility Type이다.

```typescript
type FieldErrors = Record<string, string>;
```

Record는 validation error map, status label map, lookup table에 자주 사용된다.

---

### [핵심]

Record 사용 영역:

- validation error map
- status label map
- role label map
- lookup table
- config map
- route map
- option map

형태:

```typescript
Record<KeyType, ValueType>;
```

장점:

- key-value 구조 명확화
- literal union key 제한 가능
- missing key 감지 가능
- label map 관리에 유용

---

### [실무]

Field Error Map 예:

```typescript
type FieldErrors = Record<string, string>;

const errors: FieldErrors = {
  email: "이메일 형식이 올바르지 않습니다.",
  password: "비밀번호는 필수입니다.",
};
```

Status Label Map 예:

```typescript
type RequestStatus = "idle" | "loading" | "success" | "error";

const statusLabel: Record<RequestStatus, string> = {
  idle: "대기",
  loading: "로딩 중",
  success: "성공",
  error: "오류",
};
```

Role Label Map 예:

```typescript
type UserRole = "ROLE_USER" | "ROLE_ADMIN";

const roleLabel: Record<UserRole, string> = {
  ROLE_USER: "사용자",
  ROLE_ADMIN: "관리자",
};
```

실무 기준:

- 정해진 key set은 `Record<Union, Value>` 사용
- 동적 field error는 `Record<string, string>` 사용
- 모든 union key가 필요하면 Record가 유용
- key 일부만 있을 수 있으면 Partial<Record<K, V>> 고려
- 복잡한 객체는 명시적 Type 사용

---

### [FAQ]

Q. Record는 뭐야?
A. key Type과 value Type을 지정해 객체 Type을 만드는 Utility Type이다.

Q. Record<string, string>은 무슨 뜻이야?
A. 문자열 key와 문자열 value를 가지는 객체 Type이라는 뜻이다.

Q. Record는 언제 유용해?
A. 상태별 label map, validation error map, lookup table을 표현할 때 유용하다.

Q. Record<Union, string>을 쓰면 뭐가 좋아?
A. Union에 포함된 모든 key가 빠짐없이 정의되었는지 TypeScript가 확인할 수 있다.

---

## 4.7 Readonly

### [개념]

`Readonly<T>`는 객체 Type의 모든 property를 readonly로 변환하는 Utility Type이다.

```typescript
type ReadonlyUser = Readonly<User>;
```

Readonly Utility Type은 Type Check 단계에서 property 재할당을 제한한다.

---

### [핵심]

Readonly 특징:

- 모든 property를 readonly로 변경
- Type Level 변경 제한
- Runtime freeze 아님
- 얕은 readonly
- API Response 보호에 사용 가능
- React State mutation 방지에 도움

주의:

- nested object까지 deep readonly가 아님
- Runtime 불변성 보장 아님
- 수정 가능한 form state에는 부적합할 수 있음

---

### [실무]

예:

```typescript
type User = {
  userId: number;
  nickname: string;
};

type ReadonlyUser = Readonly<User>;
```

사용:

```typescript
const user: ReadonlyUser = {
  userId: 1,
  nickname: "jun",
};

user.nickname = "kim";
```

문제:

- ReadonlyUser의 property는 재할당할 수 없다.

Readonly Array와 함께 사용:

```typescript
function getUserNames(users: readonly Readonly<User>[]): string[] {
  return users.map((user) => user.nickname);
}
```

실무 기준:

- 외부에서 변경하면 안 되는 객체에 사용 가능
- React State 원본 변경 방지에 도움
- Runtime freeze가 필요하면 별도 처리
- deep readonly는 Foundation 범위 밖
- readonly 남용 시 업데이트 로직이 불편해질 수 있음

---

### [FAQ]

Q. Readonly<T>는 뭐야?
A. 객체 Type의 모든 property를 readonly로 바꾸는 Utility Type이다.

Q. Readonly를 쓰면 Runtime에서도 값이 안 바뀌어?
A. 아니다. TypeScript Type Check 단계에서 재할당을 막는 것이다.

Q. Readonly는 nested object까지 막아?
A. 기본 Readonly는 얕은 readonly다. nested object까지 자동으로 막지는 않는다.

---

## 4.8 ReturnType and Parameters

### [개념]

`ReturnType<T>`는 함수 Type의 반환 Type을 추출하는 Utility Type이다.

`Parameters<T>`는 함수 Type의 parameter Type들을 tuple로 추출하는 Utility Type이다.

```typescript
type Result = ReturnType<typeof createUser>;
type Args = Parameters<typeof createUser>;
```

---

### [핵심]

ReturnType 특징:

- 함수 반환 Type 추출
- mapper 결과 Type 추출
- factory function 결과 Type 추출
- 중복 Type 작성 감소

Parameters 특징:

- 함수 parameter Type tuple 추출
- wrapper function 작성에 유용
- callback parameter 재사용
- 고급 패턴으로 확장 가능

주의:

- 과도한 추출은 가독성 저하
- 명시적 Type이 더 검색 친화적일 수 있음
- Foundation에서는 기본 사용만 다룸

---

### [실무]

ReturnType 예:

```typescript
function createFestivalViewModel() {
  return {
    id: 1,
    title: "Spring Festival",
    imageUrl: "/default.png",
  };
}

type FestivalViewModel = ReturnType<typeof createFestivalViewModel>;
```

Parameters 예:

```typescript
function selectFestival(festivalId: number, title: string): void {
  console.log(festivalId, title);
}

type SelectFestivalParams = Parameters<typeof selectFestival>;
```

결과:

```text
SelectFestivalParams → [number, string]
```

실무 기준:

- Factory Function 결과 Type 추출에 ReturnType 사용 가능
- Public API Type은 명시적 Type이 더 좋을 수 있음
- Parameters는 wrapper function에서 유용
- RAG 검색성을 위해 중요한 Type은 이름을 명확히 부여

---

### [FAQ]

Q. ReturnType은 언제 써?
A. 함수의 반환 Type을 재사용하고 싶을 때 사용한다.

Q. Parameters는 언제 써?
A. 함수의 parameter Type들을 tuple로 재사용하고 싶을 때 사용한다.

Q. ReturnType을 쓰면 항상 좋은가?
A. 아니다. 중요한 API Type이나 ViewModel Type은 명시적으로 정의하는 것이 더 읽기 쉬울 수 있다.

---

# 5. Generic and Utility Type Selection

## 5.1 Generic vs Explicit Type

### [개념]

Generic과 Explicit Type은 모두 Type을 정의하는 방식이지만 목적이 다르다.

Generic은 재사용을 위한 Type 구조이고 Explicit Type은 특정 데이터 구조를 명확히 표현하는 방식이다.

```text
반복되는 공통 구조
→ Generic

특정 API 계약
→ Explicit Type
```

---

### [핵심]

Generic 적합:

- ApiResponse
- SliceResponse
- PageResponse
- SelectOption
- ApiState
- ListProps
- reusable utility function

Explicit Type 적합:

- API Request DTO
- API Response DTO
- Form Data
- ViewModel
- Domain Model
- Props with clear contract

---

### [실무]

Generic 좋은 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};
```

Explicit Type 좋은 예:

```typescript
type ReviewCreateRequest = {
  festivalId: number;
  rating: number;
  content: string;
};
```

나쁜 예:

```typescript
type Request<T> = T;
```

문제:

- Generic을 쓸 의미가 없다.
- 검색성과 명확성이 낮다.

실무 기준:

- Generic은 반복 구조가 있을 때 사용
- 특정 API 계약은 명시적 Type 우선
- Generic 남용 금지
- 코드 생성 Agent는 명확한 Type 이름 우선
- Review Agent는 Generic이 실제 재사용 가치를 갖는지 확인

---

### [FAQ]

Q. Generic과 명시적 Type 중 뭐가 좋아?
A. 반복되는 공통 구조는 Generic이 좋고, 특정 API 계약은 명시적 Type이 좋다.

Q. 모든 Type을 Generic으로 만들면 좋아?
A. 아니다. Generic 남용은 가독성과 검색성을 떨어뜨린다.

Q. API Request Type은 Generic으로 만들까?
A. 대부분 명시적 Type이 더 좋다. Request DTO는 API 계약이 명확해야 한다.

---

## 5.2 Utility Type vs Explicit Type

### [개념]

Utility Type은 기존 Type을 변형해 새 Type을 만드는 방식이고, Explicit Type은 필요한 구조를 직접 정의하는 방식이다.

```text
기존 Type 일부 재사용
→ Utility Type

API 계약 명확화
→ Explicit Type
```

---

### [핵심]

Utility Type 적합:

- 일부 field 선택
- 일부 field 제외
- optional draft
- readonly view
- label map
- simple derived type

Explicit Type 적합:

- API Request
- API Response
- validation contract
- security-sensitive data
- form submit data
- backend DTO matching

주의:

- Utility Type 남용 시 Type 의미가 흐려짐
- Backend DTO와 실제 구조가 다르면 위험
- 명시적 Type이 RAG Retrieval에 더 유리할 수 있음

---

### [실무]

Utility Type 예:

```typescript
type UserSummary = Pick<UserResponse, "userId" | "nickname">;
```

Explicit Type 예:

```typescript
type SignupRequest = {
  email: string;
  password: string;
  nickname: string;
};
```

나쁜 예:

```typescript
type SignupRequest = Omit<UserResponse, "userId" | "createdAt">;
```

문제:

- Response Type과 Request Type은 목적이 다르다.
- password 같은 Request 전용 field가 누락될 수 있다.
- API 계약이 불명확해진다.

실무 기준:

- Request Type은 명시적 정의 우선
- Summary / Props 일부 재사용은 Pick 가능
- Update Draft는 Partial 가능
- 민감정보 포함 여부 확인
- Utility Type 체인이 길어지면 명시적 Type 작성

---

### [FAQ]

Q. Utility Type과 명시적 Type 중 뭐가 좋아?
A. 기존 Type 일부 재사용이면 Utility Type이 좋고, API 계약이 중요하면 명시적 Type이 좋다.

Q. Request Type을 Response Type에서 Omit으로 만들어도 돼?
A. 가능은 하지만 목적이 다르므로 명시적 Request Type이 더 안전한 경우가 많다.

Q. Utility Type을 많이 쓰면 좋은 코드야?
A. 아니다. 의미가 흐려지거나 검색성이 떨어질 수 있다.

---

# 6. Common Mistakes

## 6.1 Generic Mistakes

### [개념]

Generic 실수는 Generic이 필요 없는 곳에 사용하거나, Type Parameter를 너무 넓게 잡거나, Constraint 없이 property에 접근하려 할 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Generic 남용
- Type Parameter 이름이 의미 없음
- Constraint 없이 property 접근
- `T extends any` 사용
- Generic Default를 any로 지정
- Generic Return Type에 undefined 가능성 누락
- API Request까지 무리하게 Generic 처리
- 복잡한 Generic으로 RAG 검색성 저하
- Generic과 Runtime 값을 혼동

---

### [실무]

나쁜 예:

```typescript
function getId<T>(item: T): number {
  return item.id;
}
```

문제:

- T에 id property가 있다는 보장이 없다.

개선:

```typescript
function getId<T extends { id: number }>(item: T): number {
  return item.id;
}
```

나쁜 예:

```typescript
type ApiResponse<T = any> = {
  data: T;
};
```

개선:

```typescript
type ApiResponse<T = unknown> = {
  data: T;
};
```

실무 기준:

- property 접근에는 Constraint 필요
- `any` default 지양
- Generic이 실제로 재사용되는지 확인
- Generic보다 명시적 Type이 나은지 검토
- Foundation 범위를 넘는 복잡한 Generic 지양

---

### [FAQ]

Q. Generic에서 가장 흔한 실수는?
A. Constraint 없이 property에 접근하거나 Generic이 필요 없는 곳에 남용하는 것이다.

Q. Generic Default에 any를 쓰면 왜 안 좋아?
A. Type Safety가 약해지고 잘못된 property 접근을 막기 어렵다.

Q. Generic을 많이 쓰면 고급 코드야?
A. 아니다. 필요한 곳에만 단순하게 쓰는 것이 더 좋다.

---

## 6.2 Utility Type Mistakes

### [개념]

Utility Type 실수는 Request / Response 목적이 다른 Type을 무리하게 재사용하거나, Partial / Omit / Pick을 남용할 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Create Request에 Partial 남용
- Response Type에서 Request Type을 Omit으로 생성
- 민감정보 포함 Type을 그대로 재사용
- Pick / Omit 체인이 길어짐
- Required를 Runtime Validation으로 오해
- Readonly를 Runtime 불변성으로 오해
- Record key set 불일치
- Utility Type 이름이 의미 없음
- API 계약보다 Type 재사용을 우선함

---

### [실무]

나쁜 예:

```typescript
type UserResponse = {
  userId: number;
  email: string;
  nickname: string;
  createdAt: string;
};

type SignupRequest = Omit<UserResponse, "userId" | "createdAt">;
```

문제:

- SignupRequest에는 password가 필요할 수 있다.
- Response와 Request는 목적이 다르다.

개선:

```typescript
type SignupRequest = {
  email: string;
  password: string;
  nickname: string;
};
```

Partial 남용 예:

```typescript
type ReviewCreateRequest = Partial<ReviewResponse>;
```

문제:

- 생성 요청 필수 값이 optional로 변할 수 있다.

실무 기준:

- API 계약은 명시적 Type 우선
- Utility Type은 단순 파생 Type에 사용
- 민감정보 포함 여부 확인
- Partial은 Update / Draft에 제한적으로 사용
- Omit / Pick chain이 길면 새 Type 작성

---

### [FAQ]

Q. Utility Type에서 가장 흔한 실수는?
A. API Request와 Response 목적이 다른데 억지로 재사용하는 것이다.

Q. Required를 쓰면 실제 값 검증이 끝난 거야?
A. 아니다. Required는 Type만 바꾼다. Runtime Validation은 별도로 필요하다.

Q. Readonly를 쓰면 객체가 Runtime에서 freeze돼?
A. 아니다. TypeScript Type Check 단계에서 재할당을 막을 뿐이다.

---

# 7. Review Checklist

## 7.1 Part09 Checklist

### [개념]

TypeScript Foundation Part09 검수는 Generic, Generic Constraint, API Generic Modeling, Utility Type, Generic 선택 기준, Utility Type 선택 기준을 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] Generic 정의가 포함되었는가?
- [ ] Generic Function 설명이 포함되었는가?
- [ ] Generic Type Alias 설명이 포함되었는가?
- [ ] Generic Interface 설명이 포함되었는가?
- [ ] Generic Constraint 설명이 포함되었는가?
- [ ] Key Constraint 설명이 포함되었는가?
- [ ] Generic Default Type 설명이 포함되었는가?
- [ ] ApiResponse Generic 예제가 포함되었는가?
- [ ] SliceResponse Generic 예제가 포함되었는가?
- [ ] PageResponse Generic 예제가 포함되었는가?
- [ ] Utility Type 정의가 포함되었는가?
- [ ] Partial 설명이 포함되었는가?
- [ ] Required 설명이 포함되었는가?
- [ ] Pick 설명이 포함되었는가?
- [ ] Omit 설명이 포함되었는가?
- [ ] Record 설명이 포함되었는가?
- [ ] Readonly 설명이 포함되었는가?
- [ ] ReturnType / Parameters 설명이 포함되었는가?
- [ ] Generic vs Explicit Type 기준이 포함되었는가?
- [ ] Utility Type vs Explicit Type 기준이 포함되었는가?
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
→ Generic Check
→ Generic Constraint Check
→ API Generic Modeling Check
→ Utility Type Check
→ Selection Criteria Check
→ Common Mistake Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

Part09는 이후 API Request / Response Type, React TypeScript Readiness, Troubleshooting 문서의 재사용 Type 기반이다.

---

### [FAQ]

Q. Part09에서 가장 중요한 검수 기준은?
A. Generic과 Utility Type을 API Wrapper, SliceResponse, PageResponse, Request / Response Type 재사용 기준과 정확히 연결했는지 확인하는 것이다.

Q. Part09가 이후 문서와 어떻게 연결돼?
A. ApiResponse<T>, SliceResponse<T>, PageResponse<T>, Utility Type 기반 API Type Modeling과 React Props 재사용으로 연결된다.

---

# Retrieval Queries

### [FAQ]

Q. Generic이 뭐야?
A. Type을 parameter처럼 받아 재사용 가능한 Type이나 Function을 만드는 TypeScript 문법이다.

Q. Generic은 왜 써?
A. Type은 다르지만 구조가 같은 로직을 Type Safety를 유지하면서 재사용하기 위해 쓴다.

Q. Generic의 T는 무슨 뜻이야?
A. 관례적으로 Type을 의미하는 Type Parameter 이름이다. 다른 이름도 사용할 수 있다.

Q. Generic은 Runtime에 남아?
A. 아니다. Generic Type 정보는 Compile Time에만 사용되고 Runtime에는 남지 않는다.

Q. Generic Function은 언제 써?
A. 같은 함수 로직을 여러 Type에 재사용하면서 입력과 출력 Type 관계를 유지해야 할 때 쓴다.

Q. Generic Type Parameter를 직접 써야 해?
A. TypeScript가 추론할 수 있으면 생략해도 된다.

Q. `getFirst<T>`의 반환 Type에 왜 undefined가 붙어?
A. 배열이 비어 있으면 첫 번째 요소가 없을 수 있기 때문이다.

Q. Generic Type Alias는 언제 써?
A. 공통 Type 구조는 같고 내부 data Type만 달라질 때 사용한다.

Q. ApiResponse<T>는 왜 Generic으로 만들어?
A. success, message 구조는 공통이고 data Type만 API마다 달라지기 때문이다.

Q. Generic Interface는 언제 써?
A. 객체 구조나 계약은 같고 내부 Type만 달라질 때 사용한다.

Q. React Props도 Generic Interface로 만들 수 있어?
A. 가능하다. 재사용 가능한 List, Table, Select Component에서 사용할 수 있다.

Q. Generic Interface와 Generic Type Alias 중 뭐가 좋아?
A. 객체 확장과 계약 중심이면 Interface, Union이나 wrapper 조합이면 Type Alias가 편하다.

Q. Generic Constraint가 뭐야?
A. Generic Type Parameter가 특정 구조를 만족하도록 제한하는 문법이다.

Q. Generic에서 property를 바로 못 쓰는 이유는?
A. T가 어떤 Type인지 모르기 때문에 해당 property가 있는지 TypeScript가 확신할 수 없기 때문이다.

Q. Generic Constraint의 extends는 class 상속이야?
A. 아니다. 여기서는 Type이 특정 구조를 만족해야 한다는 의미다.

Q. keyof는 뭐야?
A. 객체 Type의 property 이름들을 Union Type으로 만드는 TypeScript 연산자다.

Q. `K extends keyof T`는 무슨 뜻이야?
A. K는 T 객체에 존재하는 key 중 하나여야 한다는 뜻이다.

Q. getValue 함수는 왜 안전해?
A. key가 실제 객체 Type의 property로 제한되고 반환 Type도 해당 property Type으로 연결되기 때문이다.

Q. Generic Default Type은 뭐야?
A. Generic Type Parameter를 생략했을 때 사용할 기본 Type을 지정하는 방식이다.

Q. Default Generic에 any를 써도 돼?
A. 권장하지 않는다. unknown이나 명확한 기본 Type이 더 안전하다.

Q. ApiResponse<T = unknown>은 무슨 뜻이야?
A. T를 지정하지 않으면 data Type을 unknown으로 사용한다는 뜻이다.

Q. ApiResponse<T>는 왜 필요해?
A. 공통 응답 구조는 재사용하고 data Type만 API마다 다르게 지정하기 위해 필요하다.

Q. 목록 응답은 어떻게 써?
A. `ApiResponse<FestivalInfoResponse[]>`처럼 data Type에 배열을 넣는다.

Q. data가 없으면 어떻게 써?
A. Backend 정책에 따라 `ApiResponse<null>` 또는 별도 응답 Type으로 정의할 수 있다.

Q. SliceResponse<T>는 언제 써?
A. 무한 스크롤이나 더보기 목록처럼 다음 페이지 존재 여부가 중요한 응답에 사용한다.

Q. SliceResponse와 PageResponse 차이는?
A. Slice는 보통 hasNext 중심이고 Page는 totalElements, totalPages 같은 전체 개수 정보를 포함한다.

Q. `ApiResponse<SliceResponse<T>>`처럼 중첩 Generic을 써도 돼?
A. 가능하다. 공통 wrapper 안에 slice data를 넣는 구조를 표현할 수 있다.

Q. PageResponse<T>는 언제 써?
A. 전체 개수와 전체 페이지 수가 필요한 페이지네이션 목록에 사용한다.

Q. SliceResponse 대신 PageResponse를 써도 돼?
A. 가능하지만 무한 스크롤에는 SliceResponse가 더 가볍고 적합할 수 있다.

Q. PageResponse의 content Type은 어떻게 지정해?
A. `PageResponse<FestivalInfoResponse>`처럼 목록 element Type을 Generic으로 넣는다.

Q. Utility Type이 뭐야?
A. 기존 Type을 변형해 새 Type을 쉽게 만드는 TypeScript 내장 Type이다.

Q. Utility Type은 왜 써?
A. 중복 Type 작성을 줄이고 기존 Type에서 일부 property를 선택하거나 optional로 바꾸기 위해 쓴다.

Q. Utility Type은 무조건 쓰는 게 좋아?
A. 아니다. 복잡하거나 API 계약이 명확해야 하는 경우 명시적 Type이 더 좋을 수 있다.

Q. Partial은 언제 써?
A. 객체의 모든 property를 optional로 만들 때 사용한다. 수정 요청이나 draft 상태에 사용할 수 있다.

Q. Partial은 nested object도 모두 optional로 만들어?
A. 아니다. 기본 Partial은 1단계 property만 optional로 만든다.

Q. Create Request에 Partial을 써도 돼?
A. 권장하지 않는다. 필수 field까지 optional이 되어 API 계약이 약해질 수 있다.

Q. Required는 언제 써?
A. optional property를 모두 required로 바꿔 완성된 상태를 표현할 때 사용한다.

Q. Required를 쓰면 Runtime 값도 채워져?
A. 아니다. Type만 바뀐다. 실제 값은 validation이나 default 처리로 채워야 한다.

Q. Required가 null도 제거해?
A. 아니다. nullable field의 null 가능성은 그대로 남는다.

Q. Pick은 언제 써?
A. 기존 Type에서 일부 property만 선택해 새 Type을 만들 때 사용한다.

Q. Pick의 두 번째 인자는 뭐야?
A. 선택할 property 이름의 union이다. 예: `"userId" | "nickname"`.

Q. API Summary Response를 Pick으로 만들어도 돼?
A. 가능하지만 실제 Backend 응답 구조와 정확히 일치하는지 확인해야 한다.

Q. Omit은 언제 써?
A. 기존 Type에서 특정 property를 제외한 Type이 필요할 때 사용한다.

Q. Create Request는 Omit으로 만들면 돼?
A. 가능하지만 실제 생성 요청 구조와 정확히 맞는지 확인해야 한다.

Q. Omit과 Pick 중 뭐가 달라?
A. Pick은 필요한 property를 선택하고 Omit은 제외할 property를 제거한다.

Q. Record는 뭐야?
A. key Type과 value Type을 지정해 객체 Type을 만드는 Utility Type이다.

Q. Record<string, string>은 무슨 뜻이야?
A. 문자열 key와 문자열 value를 가지는 객체 Type이라는 뜻이다.

Q. Record는 언제 유용해?
A. 상태별 label map, validation error map, lookup table을 표현할 때 유용하다.

Q. Record<Union, string>을 쓰면 뭐가 좋아?
A. Union에 포함된 모든 key가 빠짐없이 정의되었는지 TypeScript가 확인할 수 있다.

Q. Readonly<T>는 뭐야?
A. 객체 Type의 모든 property를 readonly로 바꾸는 Utility Type이다.

Q. Readonly를 쓰면 Runtime에서도 값이 안 바뀌어?
A. 아니다. TypeScript Type Check 단계에서 재할당을 막는 것이다.

Q. Readonly는 nested object까지 막아?
A. 기본 Readonly는 얕은 readonly다. nested object까지 자동으로 막지는 않는다.

Q. ReturnType은 언제 써?
A. 함수의 반환 Type을 재사용하고 싶을 때 사용한다.

Q. Parameters는 언제 써?
A. 함수의 parameter Type들을 tuple로 재사용하고 싶을 때 사용한다.

Q. ReturnType을 쓰면 항상 좋은가?
A. 아니다. 중요한 API Type이나 ViewModel Type은 명시적으로 정의하는 것이 더 읽기 쉬울 수 있다.

Q. Generic과 명시적 Type 중 뭐가 좋아?
A. 반복되는 공통 구조는 Generic이 좋고, 특정 API 계약은 명시적 Type이 좋다.

Q. 모든 Type을 Generic으로 만들면 좋아?
A. 아니다. Generic 남용은 가독성과 검색성을 떨어뜨린다.

Q. API Request Type은 Generic으로 만들까?
A. 대부분 명시적 Type이 더 좋다. Request DTO는 API 계약이 명확해야 한다.

Q. Utility Type과 명시적 Type 중 뭐가 좋아?
A. 기존 Type 일부 재사용이면 Utility Type이 좋고, API 계약이 중요하면 명시적 Type이 좋다.

Q. Request Type을 Response Type에서 Omit으로 만들어도 돼?
A. 가능은 하지만 목적이 다르므로 명시적 Request Type이 더 안전한 경우가 많다.

Q. Utility Type에서 가장 흔한 실수는?
A. API Request와 Response 목적이 다른데 억지로 재사용하는 것이다.

Q. Generic에서 가장 흔한 실수는?
A. Constraint 없이 property에 접근하거나 Generic이 필요 없는 곳에 남용하는 것이다.

Q. TypeScript Part09의 핵심은 뭐야?
A. Generic과 Utility Type을 API Wrapper, SliceResponse, PageResponse, Request / Response Type 재사용 기준과 정확히 연결하는 것이다.

Q. TypeScript Part09 다음 문서는 뭐가 좋아?
A. API Request and Response Type 문서가 적합하다.
