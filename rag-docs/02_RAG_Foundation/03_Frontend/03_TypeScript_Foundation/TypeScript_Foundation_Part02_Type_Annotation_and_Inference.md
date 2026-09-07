# TypeScript Foundation Part02 - Type Annotation and Type Inference

---

# 1. Type Annotation

## 1.1 Type Annotation Definition

### [개념]

Type Annotation은 변수, 함수, 객체, 배열, parameter, return value에 Type을 명시하는 문법이다.

TypeScript는 Type Annotation을 기준으로 값의 사용 방식이 올바른지 Compile Time에 검사한다.

```typescript
const userName: string = "jun";
const count: number = 10;
const active: boolean = true;
```

Type Annotation은 Runtime 값을 변환하지 않는다.
Type Annotation은 Compile Time Type Check를 위한 정보다.

---

### [핵심]

- Type Annotation은 명시적 Type 지정이다.
- Type Annotation은 Compile Time에 검사된다.
- Type Annotation은 Runtime에 남지 않는다.
- 변수 Type Annotation은 필요한 경우에만 사용한다.
- Function Parameter Type은 대부분 명시한다.
- Function Return Type은 복잡한 함수나 API 함수에 명시한다.
- Object Type은 property 이름과 Type을 함께 정의한다.
- Array Type은 element Type을 명시한다.
- Type Annotation은 Type Safety와 자동완성 품질을 높인다.

---

### [실무]

2026 실무 기준에서 Type Annotation은 모든 변수에 무조건 붙이는 문법이 아니다.

명확한 초기값이 있는 변수는 Type Inference를 활용한다.

불필요한 예:

```typescript
const title: string = "Festival";
const count: number = 10;
```

개선:

```typescript
const title = "Festival";
const count = 10;
```

Type Annotation이 필요한 예:

```typescript
function formatPrice(price: number): string {
  return `${price.toLocaleString()}원`;
}
```

Function Parameter는 TypeScript가 자동 추론하기 어려운 경우가 많으므로 명시하는 것이 좋다.

---

### [FAQ]

Q. Type Annotation이 뭐야?
A. 변수, 함수, 객체 등에 Type을 명시하는 문법이다.

Q. Type Annotation은 Runtime 값을 바꿔?
A. 아니다. Type Annotation은 Compile Time Type Check용이며 Runtime 값 변환을 하지 않는다.

Q. 모든 변수에 Type Annotation을 써야 해?
A. 아니다. 명확한 초기값이 있는 변수는 Type Inference를 활용하는 것이 좋다.

Q. Function Parameter에는 Type Annotation을 써야 해?
A. 대부분 써야 한다. Parameter는 TypeScript가 자동 추론하기 어려운 경우가 많다.

---

## 1.2 Variable Type Annotation

### [개념]

Variable Type Annotation은 변수에 저장될 값의 Type을 명시하는 방식이다.

```typescript
let userName: string = "jun";
let age: number = 20;
let isLogin: boolean = false;
```

변수 Type Annotation은 값의 Type을 제한한다.

---

### [핵심]

기본 형태:

```typescript
let variableName: Type = value;
const constantName: Type = value;
```

주요 Type:

- `string`
- `number`
- `boolean`
- `null`
- `undefined`
- `string[]`
- `number[]`
- object type
- union type

---

### [실무]

명확한 초기값이 있는 경우 Type Annotation은 생략 가능하다.

권장:

```typescript
const serviceName = "FestivalService";
const maxCount = 10;
const enabled = true;
```

명시가 필요한 경우:

```typescript
let selectedFestivalId: number | null = null;
let status: "idle" | "loading" | "success" | "error" = "idle";
const festivals: Festival[] = [];
```

명시가 필요한 대표 상황:

- 초기값이 `null`
- 초기값이 빈 배열
- 값이 여러 Type 또는 상태를 가짐
- literal union으로 허용 값 제한 필요
- 외부 데이터 구조를 Type으로 고정해야 함

---

### [FAQ]

Q. 변수 Type Annotation은 언제 필요해?
A. 초기값이 null, 빈 배열, union 상태, 외부 데이터 구조처럼 TypeScript가 의도를 정확히 추론하기 어려울 때 필요하다.

Q. `const title: string = "Festival"`은 나쁜 코드야?
A. 동작은 가능하지만 TypeScript가 추론할 수 있으므로 보통 불필요하다.

Q. 초기값이 null이면 Type을 어떻게 써?
A. `User | null`처럼 null 가능성을 Union Type으로 명시한다.

---

## 1.3 Function Parameter Type Annotation

### [개념]

Function Parameter Type Annotation은 함수가 받을 parameter의 Type을 명시하는 방식이다.

```typescript
function findFestival(festivalId: number): void {
  console.log(festivalId);
}
```

Parameter Type은 함수 호출 시 잘못된 인자 전달을 방지한다.

---

### [핵심]

필수 포함:

- parameter type
- optional parameter
- default parameter
- union parameter
- object parameter
- callback parameter
- event parameter

기본 형태:

```typescript
function functionName(parameter: Type): ReturnType {
  return value;
}
```

---

### [실무]

좋은 예:

```typescript
function formatDate(dateText: string): string {
  return new Date(dateText).toLocaleDateString("ko-KR");
}
```

Object Parameter 예:

```typescript
type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  targetMonth?: string;
};

function searchFestivals(params: FestivalSearchParams): void {
  console.log(params.keyword);
}
```

Callback Parameter 예:

```typescript
type ClickHandler = (festivalId: number) => void;

function handleFestivalClick(festivalId: number): void {
  console.log(festivalId);
}
```

실무 기준:

- Utility Function Parameter는 명시
- API Function Parameter는 명시
- Event Handler Parameter는 명시
- Object Parameter는 type 또는 interface로 분리
- `any` parameter 지양

---

### [FAQ]

Q. Function Parameter에는 Type을 꼭 써야 해?
A. 대부분 써야 한다. Parameter는 TypeScript가 호출 의도를 자동으로 알기 어렵다.

Q. Object Parameter는 어떻게 Type을 붙여?
A. type 또는 interface로 객체 구조를 정의한 뒤 parameter Type으로 사용한다.

Q. Parameter Type을 any로 두면 안 돼?
A. 가능은 하지만 Type Check가 약해지므로 명시적 Type이나 unknown을 우선 고려한다.

---

## 1.4 Function Return Type Annotation

### [개념]

Function Return Type Annotation은 함수가 반환하는 값의 Type을 명시하는 방식이다.

```typescript
function add(a: number, b: number): number {
  return a + b;
}
```

Return Type은 함수 결과의 계약을 명확히 한다.

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
- nullable return type

---

### [실무]

Return Type 명시 권장 상황:

- API 호출 함수
- Public Utility Function
- 복잡한 조건 분기 함수
- Library처럼 재사용되는 함수
- Return Type이 Union인 함수
- 비동기 함수
- Review Agent 검토 대상 함수

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

반환값 없는 함수:

```typescript
function logMessage(message: string): void {
  console.log(message);
}
```

주의:

- async function return type은 `Promise<T>`다.
- 반환값이 없으면 `void`를 사용한다.
- API Response Type은 Backend DTO와 정합성을 유지한다.

---

### [FAQ]

Q. Function Return Type은 항상 써야 해?
A. 항상은 아니다. 하지만 API 함수, 복잡한 함수, 재사용 함수에는 명시하는 것이 좋다.

Q. async 함수 Return Type은 어떻게 써?
A. `Promise<T>` 형태로 작성한다.

Q. 반환값 없는 함수는 어떤 Type이야?
A. `void`를 사용한다.

---

# 2. Type Inference

## 2.1 Type Inference Definition

### [개념]

Type Inference는 TypeScript가 값과 코드 흐름을 보고 Type을 자동으로 추론하는 기능이다.

```typescript
const title = "Festival";
const count = 10;
const active = true;
```

TypeScript 추론:

```text
title → string
count → number
active → boolean
```

Type Inference는 불필요한 Type Annotation을 줄이고 코드 가독성을 높인다.

---

### [핵심]

- Type Inference는 자동 Type 추론이다.
- 명확한 초기값은 TypeScript가 Type을 추론할 수 있다.
- 불필요한 Type Annotation은 생략 가능하다.
- Function Parameter는 추론이 어려워 명시가 필요하다.
- 빈 배열은 element Type 추론에 주의한다.
- null 초기값은 Union Type 명시가 필요하다.
- Return Type은 추론 가능하지만 복잡한 함수는 명시 권장이다.

---

### [실무]

Type Inference 활용 예:

```typescript
const title = "Festival";
const maxReviewCount = 5;
const isFavorite = false;
```

불필요한 Type Annotation을 줄이면 코드가 간결해진다.

하지만 TypeScript가 의도를 정확히 모르는 경우에는 명시해야 한다.

```typescript
const festivals: Festival[] = [];
let selectedUser: User | null = null;
```

실무 기준:

```text
명확한 초기값
→ Type Inference 활용

함수 parameter / API Response / 빈 배열 / null 초기값
→ Type Annotation 사용
```

---

### [FAQ]

Q. Type Inference가 뭐야?
A. TypeScript가 값과 코드 흐름을 보고 Type을 자동으로 추론하는 기능이다.

Q. Type Inference를 믿어도 돼?
A. 명확한 초기값이 있는 경우 신뢰해도 된다. 빈 배열, null 초기값, 함수 parameter는 명시하는 것이 좋다.

Q. Type Annotation과 Type Inference 중 뭐가 좋아?
A. 명확한 값은 Inference를 활용하고 외부 입력, 함수 parameter, API Response는 Annotation을 사용한다.

---

## 2.2 Literal Inference

### [개념]

Literal Inference는 TypeScript가 `const` 선언과 literal value를 보고 더 좁은 Type을 추론하는 방식이다.

```typescript
const role = "ROLE_USER";
```

위 값은 변경할 수 없으므로 TypeScript는 `string`보다 좁은 `"ROLE_USER"`로 추론할 수 있다.

---

### [핵심]

- `const`는 값이 재할당되지 않는다.
- `let`은 값이 변경될 수 있다.
- `const` literal은 좁은 literal type으로 추론될 수 있다.
- `let` literal은 보통 넓은 primitive type으로 추론된다.
- 상태 값 제한에는 literal union이 유용하다.

---

### [실무]

예:

```typescript
const userRole = "ROLE_USER";
let status = "idle";
```

의미:

```text
userRole → "ROLE_USER"
status → string
```

상태 값을 제한하고 싶다면 Type을 명시한다.

```typescript
type RequestStatus = "idle" | "loading" | "success" | "error";

let status: RequestStatus = "idle";
status = "loading";
```

실무 기준:

- 단순 상수는 Inference 활용
- 변경 가능한 상태 값은 literal union 명시
- 권한, 상태, 테마, 라우트 이름은 literal union 고려

---

### [FAQ]

Q. const와 let의 Type Inference가 달라?
A. 다르다. const는 값이 고정되므로 더 좁은 literal type으로 추론될 수 있고 let은 변경 가능성을 고려해 더 넓게 추론된다.

Q. 상태 값은 string으로 두면 안 돼?
A. 가능하지만 `"idle" | "loading" | "success" | "error"` 같은 literal union이 더 안전하다.

Q. Role Type은 어떻게 제한해?
A. `type UserRole = "ROLE_USER" | "ROLE_ADMIN"`처럼 literal union으로 제한할 수 있다.

---

## 2.3 Array Inference

### [개념]

Array Inference는 배열 초기값을 기준으로 element Type을 추론하는 방식이다.

```typescript
const names = ["jun", "kim"];
const scores = [90, 80, 70];
```

TypeScript 추론:

```text
names → string[]
scores → number[]
```

---

### [핵심]

- 배열 초기값이 있으면 element Type을 추론할 수 있다.
- 빈 배열은 의도한 element Type을 알기 어렵다.
- 객체 배열은 property 구조를 기준으로 추론된다.
- API 목록 데이터는 명시적 Type 정의를 권장한다.
- 배열 Method 결과 Type도 element Type에 따라 결정된다.

---

### [실무]

초기값이 있는 배열:

```typescript
const regions = ["서울", "부산", "대구"];
```

빈 배열은 Type 명시 권장:

```typescript
type Festival = {
  festivalId: number;
  title: string;
};

const festivals: Festival[] = [];
```

객체 배열 예:

```typescript
const festivalCards: Festival[] = [
  { festivalId: 1, title: "Spring Festival" },
  { festivalId: 2, title: "Summer Festival" },
];
```

주의:

- 빈 배열은 Type 의도가 드러나지 않는다.
- API 응답 목록은 `FestivalInfoResponse[]`처럼 명시한다.
- React State 빈 배열은 Type 명시가 특히 중요하다.

---

### [FAQ]

Q. 빈 배열에는 왜 Type을 써야 해?
A. TypeScript가 배열에 어떤 element가 들어갈지 정확히 추론하기 어렵기 때문이다.

Q. 객체 배열 Type은 어떻게 정의해?
A. 객체 Type을 type 또는 interface로 정의한 뒤 `Festival[]`처럼 사용한다.

Q. React State 빈 배열도 Type이 필요해?
A. 쓰는 것이 좋다. 초기값만으로 element Type을 알기 어렵기 때문이다.

---

## 2.4 Object Inference

### [개념]

Object Inference는 객체 literal의 property 이름과 value를 보고 TypeScript가 객체 Type을 추론하는 방식이다.

```typescript
const user = {
  id: 1,
  name: "jun",
  active: true,
};
```

TypeScript 추론:

```text
user → { id: number; name: string; active: boolean }
```

---

### [핵심]

- 객체 literal은 property 기준으로 Type이 추론된다.
- property Type은 초기값 기준으로 추론된다.
- 객체 구조가 API Response라면 명시적 Type 정의가 좋다.
- optional property는 명시하지 않으면 추론되지 않는다.
- nullable property는 Type에 명시해야 한다.
- Backend DTO와 Frontend Type 정합성이 중요하다.

---

### [실무]

단순 내부 객체는 Inference 가능:

```typescript
const filterOption = {
  keyword: "",
  page: 1,
};
```

API Response 객체는 Type 명시 권장:

```typescript
type UserResponse = {
  userId: number;
  nickname: string;
  profileImageUrl: string | null;
};

const user: UserResponse = {
  userId: 1,
  nickname: "jun",
  profileImageUrl: null,
};
```

주의:

```typescript
const festival = {
  festivalId: 1,
  title: "Festival",
};
```

위 객체에는 `imageUrl` property가 없다.
나중에 `festival.imageUrl`을 사용하면 Type Error가 발생한다.

필요하면 optional 또는 nullable property를 Type으로 정의한다.

```typescript
type Festival = {
  festivalId: number;
  title: string;
  imageUrl?: string;
  averageRating: number | null;
};
```

---

### [FAQ]

Q. Object Type도 자동 추론돼?
A. 된다. 객체 literal의 property 이름과 value Type을 보고 추론한다.

Q. API Response 객체도 Inference만 쓰면 돼?
A. 권장하지 않는다. API Response는 Backend DTO와 맞춰 명시적 Type으로 관리하는 것이 좋다.

Q. optional property는 자동으로 추론돼?
A. 객체 초기값에 없는 property는 자동으로 optional로 추론되지 않는다. Type 정의가 필요하다.

---

# 3. Annotation vs Inference

## 3.1 Selection Criteria

### [개념]

Type Annotation과 Type Inference는 경쟁 관계가 아니라 함께 사용하는 TypeScript 작성 방식이다.

TypeScript Code는 불필요한 Annotation을 줄이고 필요한 지점에 명확한 Type을 작성해야 한다.

---

### [핵심]

Type Inference 권장:

- 명확한 primitive 초기값
- 단순 상수
- 단순 내부 변수
- 간단한 계산 결과
- 지역 변수

Type Annotation 권장:

- Function Parameter
- Function Return Type
- API Request Type
- API Response Type
- Error Response Type
- Object Model Type
- React Props Type
- React Event Type
- React State Type
- 빈 배열
- null 초기값
- Union Type
- Literal Union 상태값

---

### [실무]

판단 Flow:

```text
값의 Type이 초기값만 보고 명확한가?
→ Yes: Type Inference 사용
→ No: Type Annotation 사용

외부 입력 또는 API 데이터인가?
→ Yes: Type Annotation + Runtime Validation 고려

함수 parameter인가?
→ Yes: Type Annotation 사용

빈 배열 또는 null 초기값인가?
→ Yes: Type Annotation 사용
```

예:

```typescript
const title = "Festival";
const page = 1;

type Festival = {
  festivalId: number;
  title: string;
};

const festivals: Festival[] = [];

function getFestivalTitle(festival: Festival): string {
  return festival.title;
}
```

---

### [FAQ]

Q. Type Annotation과 Type Inference 중 하나만 써야 해?
A. 아니다. 명확한 값은 Inference를 쓰고 외부 입력, 함수, API, State는 Annotation을 쓴다.

Q. Type을 많이 쓸수록 좋은 TypeScript 코드야?
A. 아니다. 불필요한 Annotation은 가독성을 떨어뜨릴 수 있다.

Q. Type을 적게 쓰면 좋은 코드야?
A. 아니다. 필요한 지점의 Type이 없으면 안정성이 떨어진다.

---

## 3.2 Practical Style Guide

### [개념]

TypeScript Practical Style Guide는 Type Annotation과 Type Inference를 일관되게 사용하는 기준이다.

Frontend Agent는 이 기준으로 TypeScript Code를 생성하고 Review Agent는 이 기준으로 검토한다.

---

### [핵심]

권장 스타일:

- Primitive 초기값은 Inference 사용
- Function Parameter는 Annotation 사용
- API Function Return Type은 Annotation 사용
- React Props는 Type 정의
- React State 빈 배열은 Type 명시
- null 초기값은 Union Type 명시
- API Response는 Type Alias 또는 Interface로 정의
- Error Response도 Type으로 정의
- `any` 대신 구체적 Type 또는 `unknown` 사용
- `as` Type Assertion 남용 금지

---

### [실무]

권장 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};

type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

async function getFestivalList(): Promise<ApiResponse<FestivalInfoResponse[]>> {
  const response = await fetch("/api/festivals");

  if (!response.ok) {
    throw new Error("Failed to load festivals");
  }

  return await response.json();
}
```

나쁜 예:

```typescript
async function getFestivalList(): Promise<any> {
  const response = await fetch("/api/festivals");
  return await response.json();
}
```

문제:

- API Response 구조를 알 수 없다.
- 잘못된 property 접근을 TypeScript가 잡기 어렵다.
- Review Agent가 안정성을 판단하기 어렵다.

---

### [FAQ]

Q. API 함수 Return Type은 꼭 써야 해?
A. 권장한다. API 함수는 외부 데이터 구조를 다루므로 Return Type이 명확해야 한다.

Q. any는 언제 써도 돼?
A. 임시 Migration 상황에서 제한적으로 사용할 수 있지만 최종 코드에서는 제거하거나 범위를 최소화해야 한다.

Q. Review Agent는 무엇을 확인해야 해?
A. Function Parameter, API Type, Props Type, State Type, nullable 처리, any 남용 여부를 확인해야 한다.

---

# 4. Common Type Annotation Patterns

## 4.1 API Type Annotation

### [개념]

API Type Annotation은 Frontend가 Backend와 주고받는 Request / Response 구조를 Type으로 정의하는 방식이다.

API Type은 Frontend와 Backend 사이의 데이터 계약 역할을 한다.

---

### [핵심]

필수 대상:

- Request Body Type
- Query Parameter Type
- Path Parameter Type
- Response Body Type
- Common Response Wrapper
- Error Response Type
- Page Response Type
- Slice Response Type
- Nullable Field

---

### [실무]

Request Type 예:

```typescript
type ReviewCreateRequest = {
  festivalId: number;
  rating: number;
  content: string;
};
```

Search Params Type 예:

```typescript
type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  themeCode?: string;
  targetMonth?: string;
};
```

Response Type 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};

type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  averageRating: number | null;
};

type FestivalListResponse = ApiResponse<FestivalInfoResponse[]>;
```

실무 기준:

- Backend DTO 필드명과 Frontend Type 필드명 일치
- nullable field는 반드시 반영
- 날짜는 대부분 string으로 수신
- ViewModel Type과 API Response Type은 분리 가능
- Error Response도 Type으로 관리

---

### [FAQ]

Q. API Type Annotation은 왜 필요해?
A. Backend와 Frontend 사이의 데이터 구조를 명확히 하고 잘못된 property 접근을 줄이기 위해 필요하다.

Q. API 날짜 Type은 Date로 써?
A. 대부분 JSON 응답에서는 string으로 받고 필요하면 Frontend에서 Date로 변환한다.

Q. nullable API field는 어떻게 표현해?
A. `string | null`, `number | null`처럼 Union Type으로 표현한다.

---

## 4.2 React Props Type Annotation

### [개념]

React Props Type Annotation은 Component가 외부에서 받는 데이터의 구조를 Type으로 정의하는 방식이다.

Props Type은 Component 입력 계약이다.

---

### [핵심]

Props Type 대상:

- data props
- optional props
- callback props
- children
- event handler props
- nullable props
- list props

---

### [실무]

Props Type 예:

```typescript
type FestivalCardProps = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  onClick: (festivalId: number) => void;
};

function FestivalCard({
  festivalId,
  title,
  imageUrl,
  onClick,
}: FestivalCardProps) {
  return null;
}
```

Optional Props 예:

```typescript
type EmptyStateProps = {
  message?: string;
};

function EmptyState({ message = "데이터가 없습니다." }: EmptyStateProps) {
  return null;
}
```

실무 기준:

- Component 가까이에 Props Type 정의 가능
- 여러 Component에서 공유하면 별도 Type 파일로 분리
- optional props는 기본값 고려
- callback props는 parameter와 return type 명시
- nullable props는 fallback UI 처리

---

### [FAQ]

Q. Props Type은 왜 필요해?
A. Component가 어떤 데이터를 받아야 하는지 명확히 하고 잘못된 props 전달을 막기 위해 필요하다.

Q. Optional Props는 어떻게 써?
A. property 이름 뒤에 `?`를 붙이고 Component 내부에서 기본값을 처리한다.

Q. Callback Props는 어떻게 Type을 써?
A. `(parameter: Type) => ReturnType` 형태로 작성한다. 반환값이 없으면 `void`를 쓴다.

---

## 4.3 React State Type Annotation

### [개념]

React State Type Annotation은 State 값의 Type을 명확히 정의하는 방식이다.

특히 빈 배열, null 초기값, union 상태 값에서 중요하다.

---

### [핵심]

State Type 명시 대상:

- empty array state
- nullable object state
- async status state
- form state
- selected id state
- error state
- API response state

---

### [실무]

빈 배열 State:

```typescript
type Festival = {
  festivalId: number;
  title: string;
};

const initialFestivals: Festival[] = [];
```

nullable State:

```typescript
type User = {
  userId: number;
  nickname: string;
};

const initialUser: User | null = null;
```

비동기 상태:

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";

let status: AsyncStatus = "idle";
```

실무 기준:

- 빈 배열은 element Type 명시
- null 초기값은 `T | null` 명시
- loading / success / error는 literal union 권장
- error message는 `string | null` 사용 가능
- form state는 object type으로 정의

---

### [FAQ]

Q. React State 빈 배열은 Type을 써야 해?
A. 쓰는 것이 좋다. 빈 배열만으로는 element Type을 정확히 알기 어렵다.

Q. 초기값이 null이면 Type을 어떻게 써?
A. `User | null`처럼 null 가능성을 Union Type으로 명시한다.

Q. Loading 상태는 boolean으로만 두면 돼?
A. 단순하면 가능하지만 idle, loading, success, error가 필요하면 literal union이 더 명확하다.

---

# 5. Common Mistakes

## 5.1 Type Annotation Mistakes

### [개념]

Type Annotation 실수는 Type을 너무 많이 쓰거나, 필요한 곳에 쓰지 않거나, Runtime 변환과 혼동할 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- 모든 primitive 변수에 불필요한 Type Annotation 작성
- Function Parameter Type 누락
- API Response Type을 `any`로 처리
- 빈 배열 Type 미정의
- null 초기값에 Union Type 미정의
- nullable field를 string으로 단정
- async function return type을 `T`로 오해
- Type Annotation이 Runtime 변환을 한다고 오해
- Type Error를 `as`로만 해결
- Backend DTO 변경 후 Type 미수정

---

### [실무]

나쁜 예:

```typescript
const title: string = "Festival";

function getTitle(festival) {
  return festival.title;
}
```

문제:

- `title: string`은 불필요하다.
- `festival` parameter Type이 없다.
- `noImplicitAny` 설정에서 오류가 발생한다.

개선:

```typescript
type Festival = {
  title: string;
};

const title = "Festival";

function getTitle(festival: Festival): string {
  return festival.title;
}
```

---

### [FAQ]

Q. Type Annotation을 많이 쓰면 좋은 코드야?
A. 아니다. TypeScript가 명확히 추론할 수 있는 값에는 생략하는 것이 좋다.

Q. Parameter implicitly has an any type 오류는 왜 나?
A. Function Parameter Type이 명시되지 않았고 TypeScript가 추론할 수 없기 때문이다.

Q. Type Error를 as로 해결해도 돼?
A. 남용하면 위험하다. 실제 Type 정의와 데이터 구조를 먼저 확인해야 한다.

---

## 5.2 Type Inference Mistakes

### [개념]

Type Inference 실수는 TypeScript가 추론한 Type과 개발자가 의도한 Type이 다를 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- 빈 배열 Type 추론 방치
- null 초기값 Type 추론 방치
- let 상태 값을 string으로 넓게 추론
- 객체 Type에 optional property 누락
- API Response를 Inference만으로 처리
- Return Type 추론만 믿고 복잡한 함수 방치
- any 추론을 놓침
- literal union이 필요한 곳에 string 사용

---

### [실무]

나쁜 예:

```typescript
let status = "idle";

status = "loading";
status = "done";
```

문제:

- `status`는 string으로 추론된다.
- `"done"` 같은 의도하지 않은 상태도 허용된다.

개선:

```typescript
type RequestStatus = "idle" | "loading" | "success" | "error";

let status: RequestStatus = "idle";

status = "loading";
```

빈 배열 문제:

```typescript
const festivals = [];
```

개선:

```typescript
const festivals: Festival[] = [];
```

---

### [FAQ]

Q. Type Inference 때문에 문제가 생길 수 있어?
A. 있다. 빈 배열, null 초기값, 상태 문자열처럼 의도를 정확히 표현하지 못하는 경우가 있다.

Q. 상태 값이 string으로 추론되면 뭐가 문제야?
A. 허용하지 않아야 할 문자열도 들어갈 수 있어 상태 분기 오류가 발생할 수 있다.

Q. API Response도 Inference로 처리하면 안 돼?
A. 권장하지 않는다. API Response는 명시적 Type으로 Backend DTO와 정합성을 유지해야 한다.

---

# 6. Review Checklist

## 6.1 Part02 Checklist

### [개념]

TypeScript Foundation Part02 검수는 Type Annotation과 Type Inference 사용 기준이 명확한지 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] Type Annotation 정의가 포함되었는가?
- [ ] Type Annotation이 Runtime 변환이 아님을 설명했는가?
- [ ] Variable Type Annotation 기준이 포함되었는가?
- [ ] Function Parameter Type 기준이 포함되었는가?
- [ ] Function Return Type 기준이 포함되었는가?
- [ ] Type Inference 정의가 포함되었는가?
- [ ] Literal Inference 설명이 포함되었는가?
- [ ] Array Inference 주의점이 포함되었는가?
- [ ] Object Inference 주의점이 포함되었는가?
- [ ] Annotation vs Inference 선택 기준이 포함되었는가?
- [ ] API Type Annotation 예제가 포함되었는가?
- [ ] React Props Type 예제가 포함되었는가?
- [ ] React State Type 예제가 포함되었는가?
- [ ] any 남용 주의가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Required Section Check
→ Annotation Criteria Check
→ Inference Criteria Check
→ API Type Check
→ React Props Type Check
→ React State Type Check
→ Common Mistake Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

Part02는 이후 Basic Type, Object Type, Function Type, API Type 문서의 직접 기반이다.

---

### [FAQ]

Q. Part02에서 가장 중요한 검수 기준은?
A. Type Annotation과 Type Inference를 언제 각각 사용할지 명확히 구분하는 것이다.

Q. Part02가 이후 문서와 어떻게 연결돼?
A. Basic Type, Object Type, Function Type, API Response Type, React Props Type 작성 기준이 된다.

---

# Retrieval Queries

### [FAQ]

Q. Type Annotation이 뭐야?
A. 변수, 함수, 객체, 배열, parameter, return value에 Type을 명시하는 문법이다.

Q. Type Annotation은 Runtime 값을 바꿔?
A. 아니다. Type Annotation은 Compile Time Type Check용이며 Runtime 값 변환을 하지 않는다.

Q. 모든 변수에 Type Annotation을 써야 해?
A. 아니다. 명확한 초기값이 있는 변수는 Type Inference를 활용하는 것이 좋다.

Q. Variable Type Annotation은 언제 필요해?
A. 초기값이 null, 빈 배열, union 상태, 외부 데이터 구조처럼 TypeScript가 의도를 정확히 추론하기 어려울 때 필요하다.

Q. Function Parameter에는 Type을 써야 해?
A. 대부분 써야 한다. Parameter는 TypeScript가 자동 추론하기 어려운 경우가 많다.

Q. Function Return Type은 항상 써야 해?
A. 항상은 아니지만 API 함수, 복잡한 함수, 재사용 함수에는 명시하는 것이 좋다.

Q. async 함수 Return Type은 어떻게 써?
A. `Promise<T>` 형태로 작성한다.

Q. 반환값 없는 함수는 어떤 Type이야?
A. `void`를 사용한다.

Q. Type Inference가 뭐야?
A. TypeScript가 값과 코드 흐름을 보고 Type을 자동으로 추론하는 기능이다.

Q. Type Inference를 믿어도 돼?
A. 명확한 초기값이 있는 경우 신뢰해도 된다. 빈 배열, null 초기값, 함수 parameter는 명시하는 것이 좋다.

Q. Type Annotation과 Type Inference 중 뭐가 좋아?
A. 명확한 값은 Inference를 활용하고 외부 입력, 함수 parameter, API Response는 Annotation을 사용한다.

Q. const와 let의 Type Inference가 달라?
A. 다르다. const는 더 좁은 literal type으로 추론될 수 있고 let은 변경 가능성을 고려해 더 넓게 추론된다.

Q. 상태 값은 string으로 두면 안 돼?
A. 가능하지만 `"idle" | "loading" | "success" | "error"` 같은 literal union이 더 안전하다.

Q. 빈 배열에는 왜 Type을 써야 해?
A. TypeScript가 배열에 어떤 element가 들어갈지 정확히 추론하기 어렵기 때문이다.

Q. 객체 배열 Type은 어떻게 정의해?
A. 객체 Type을 type 또는 interface로 정의한 뒤 `Festival[]`처럼 사용한다.

Q. Object Type도 자동 추론돼?
A. 된다. 객체 literal의 property 이름과 value Type을 보고 추론한다.

Q. API Response 객체도 Inference만 쓰면 돼?
A. 권장하지 않는다. API Response는 Backend DTO와 맞춰 명시적 Type으로 관리하는 것이 좋다.

Q. optional property는 자동으로 추론돼?
A. 객체 초기값에 없는 property는 자동으로 optional로 추론되지 않는다. Type 정의가 필요하다.

Q. Type Annotation과 Type Inference는 어떻게 선택해?
A. 초기값만 보고 명확하면 Inference를 쓰고 함수 parameter, API, State, 빈 배열, null 초기값은 Annotation을 쓴다.

Q. API Type Annotation은 왜 필요해?
A. Backend와 Frontend 사이의 데이터 구조를 명확히 하고 잘못된 property 접근을 줄이기 위해 필요하다.

Q. API 날짜 Type은 Date로 써?
A. 대부분 JSON 응답에서는 string으로 받고 필요하면 Frontend에서 Date로 변환한다.

Q. nullable API field는 어떻게 표현해?
A. `string | null`, `number | null`처럼 Union Type으로 표현한다.

Q. Props Type은 왜 필요해?
A. Component가 어떤 데이터를 받아야 하는지 명확히 하고 잘못된 props 전달을 막기 위해 필요하다.

Q. Callback Props는 어떻게 Type을 써?
A. `(parameter: Type) => ReturnType` 형태로 작성한다. 반환값이 없으면 `void`를 쓴다.

Q. React State 빈 배열은 Type을 써야 해?
A. 쓰는 것이 좋다. 빈 배열만으로는 element Type을 정확히 알기 어렵다.

Q. 초기값이 null이면 Type을 어떻게 써?
A. `User | null`처럼 null 가능성을 Union Type으로 명시한다.

Q. Loading 상태는 boolean으로만 두면 돼?
A. 단순하면 가능하지만 idle, loading, success, error가 필요하면 literal union이 더 명확하다.

Q. Type Annotation을 많이 쓰면 좋은 코드야?
A. 아니다. TypeScript가 명확히 추론할 수 있는 값에는 생략하는 것이 좋다.

Q. Parameter implicitly has an any type 오류는 왜 나?
A. Function Parameter Type이 명시되지 않았고 TypeScript가 추론할 수 없기 때문이다.

Q. any는 언제 써도 돼?
A. 임시 Migration 상황에서 제한적으로 사용할 수 있지만 최종 코드에서는 제거하거나 범위를 최소화해야 한다.

Q. Type Error를 as로 해결해도 돼?
A. 남용하면 위험하다. 실제 Type 정의와 데이터 구조를 먼저 확인해야 한다.

Q. Type Inference 때문에 문제가 생길 수 있어?
A. 있다. 빈 배열, null 초기값, 상태 문자열처럼 의도를 정확히 표현하지 못하는 경우가 있다.

Q. 상태 값이 string으로 추론되면 뭐가 문제야?
A. 허용하지 않아야 할 문자열도 들어갈 수 있어 상태 분기 오류가 발생할 수 있다.

Q. TypeScript Part02의 핵심은 뭐야?
A. Type Annotation과 Type Inference를 언제 각각 사용할지 구분하는 것이다.

Q. TypeScript Part02 다음 문서는 뭐가 좋아?
A. Primitive Type, Array Type, Tuple Type, Any Unknown Never Void 같은 Basic Type 문서가 적합하다.
