# TypeScript Foundation Part08 - Type Narrowing and Type Guard

---

# 1. Type Narrowing

## 1.1 Type Narrowing Definition

### [개념]

Type Narrowing은 넓은 Type을 조건문과 검증 로직을 통해 더 구체적인 Type으로 좁히는 과정이다.

Union Type, unknown, nullable value, optional property는 사용 전에 Type Narrowing이 필요한 경우가 많다.

```typescript
function formatValue(value: string | number): string {
  if (typeof value === "number") {
    return value.toLocaleString();
  }

  return value.toUpperCase();
}
```

위 코드에서 `typeof value === "number"` 조건 안에서는 `value`가 `number`로 좁혀진다.

---

### [핵심]

Type Narrowing 핵심:

- Union Type을 안전하게 사용
- nullable value를 안전하게 사용
- optional property를 안전하게 사용
- unknown 값을 검증 후 사용
- Type별 method 접근 가능
- Runtime 조건과 Compile Time Type을 연결
- Type Assertion보다 안전함

주요 Narrowing 방식:

- `typeof`
- `instanceof`
- `in` operator
- equality narrowing
- truthiness narrowing
- null check
- discriminated union narrowing
- custom type guard

---

### [실무]

2026 Frontend 실무 기준에서 Type Narrowing은 API Response, Form Input, URL Query, localStorage, React State, Event Value를 안전하게 다루기 위한 필수 패턴이다.

Nullable 처리 예:

```typescript
function getImageUrl(imageUrl: string | null): string {
  return imageUrl ?? "/default-image.png";
}
```

Union Type 처리 예:

```typescript
function formatId(id: number | string): string {
  if (typeof id === "number") {
    return id.toString();
  }

  return id;
}
```

unknown 처리 예:

```typescript
function parseMessage(value: unknown): string {
  if (typeof value === "string") {
    return value;
  }

  return "알 수 없는 메시지";
}
```

실무 기준:

- 외부 입력은 바로 사용하지 않음
- Union Type은 사용 전 분기
- nullable 값은 fallback 처리
- optional property는 optional chaining 또는 guard 사용
- Type Assertion보다 Type Narrowing 우선

---

### [FAQ]

Q. Type Narrowing이 뭐야?
A. 넓은 Type을 조건문과 검증 로직으로 더 구체적인 Type으로 좁히는 과정이다.

Q. Type Narrowing은 왜 필요해?
A. Union Type, unknown, null 가능 값을 안전하게 사용하기 위해 필요하다.

Q. Type Assertion 대신 Narrowing을 써야 해?
A. 가능하면 Narrowing이 더 안전하다. Assertion은 검증 없이 TypeScript를 우회할 수 있다.

Q. Type Narrowing은 Runtime 검증이야?
A. 조건문은 Runtime에서 실행되고, TypeScript는 그 조건을 근거로 Compile Time Type을 좁힌다.

---

## 1.2 Narrowing Flow

### [개념]

Type Narrowing Flow는 값의 출처와 가능 Type을 확인한 뒤 안전한 Type으로 좁혀 사용하는 흐름이다.

```text
Unknown or Union Value
→ Runtime Check
→ Type Narrowing
→ Safe Property Access
→ Safe Function Call
```

Type Narrowing은 TypeScript가 값을 안전하게 사용할 수 있다고 판단할 수 있는 조건을 제공한다.

---

### [핵심]

Narrowing Flow:

1. 값의 출처 확인
2. 가능한 Type 확인
3. Runtime 조건 작성
4. TypeScript Narrowing 확인
5. 안전한 property / method 사용
6. fallback 처리
7. Type Assertion 제거

검증 대상:

- API Response
- URL Query
- localStorage
- JSON parse result
- user input
- nullable state
- optional props
- union status

---

### [실무]

API Response 처리 Flow:

```text
API Response
→ unknown or typed response
→ field existence check
→ null check
→ Type Guard
→ Safe UI Rendering
```

예:

```typescript
type Festival = {
  festivalId: number;
  title: string;
};

function parseFestival(value: unknown): Festival | null {
  if (
    typeof value === "object" &&
    value !== null &&
    "festivalId" in value &&
    "title" in value
  ) {
    return value as Festival;
  }

  return null;
}
```

주의:

- 위 예제의 `as Festival`은 최소 검증 후 사용하는 형태다.
- 더 안전하게 하려면 property value Type까지 검사한다.

개선:

```typescript
function isFestival(value: unknown): value is Festival {
  return (
    typeof value === "object" &&
    value !== null &&
    "festivalId" in value &&
    typeof value.festivalId === "number" &&
    "title" in value &&
    typeof value.title === "string"
  );
}
```

실무 기준:

- 단순 존재 확인보다 property value Type 확인 권장
- 복잡한 API Response는 Schema Validation 도구 고려
- Type Guard는 Runtime 조건과 Type 정의가 일치해야 함
- fallback UI와 error handling 연결

---

### [FAQ]

Q. Narrowing Flow는 어떻게 잡아?
A. 값의 출처 확인 → Runtime 조건 확인 → Type 좁히기 → 안전한 사용 → fallback 처리 순서로 잡는다.

Q. in operator만 쓰면 안전해?
A. property 존재는 확인하지만 value Type까지 보장하지는 않는다. 필요한 경우 typeof 검사도 함께 한다.

Q. API 응답은 항상 Type Guard가 필요해?
A. 모든 응답에 필수는 아니지만 신뢰하기 어려운 외부 데이터나 중요한 데이터에는 검증이 필요할 수 있다.

---

# 2. typeof Narrowing

## 2.1 typeof Narrowing Definition

### [개념]

`typeof` Narrowing은 JavaScript의 `typeof` 연산자를 사용해 Primitive Type을 구분하는 방식이다.

```typescript
function formatValue(value: string | number): string {
  if (typeof value === "string") {
    return value.toUpperCase();
  }

  return value.toLocaleString();
}
```

`typeof`는 string, number, boolean 같은 Primitive Type을 좁힐 때 가장 자주 사용된다.

---

### [핵심]

`typeof`로 구분 가능한 주요 값:

- `string`
- `number`
- `boolean`
- `undefined`
- `object`
- `function`
- `symbol`
- `bigint`

주의:

- `typeof null`은 `"object"`다.
- object check에서는 `value !== null`이 필요하다.
- array check는 `Array.isArray()` 사용
- Date, Error 같은 객체는 `instanceof` 사용 가능

---

### [실무]

Primitive Union 예:

```typescript
function normalizeId(id: number | string): string {
  if (typeof id === "number") {
    return id.toString();
  }

  return id.trim();
}
```

Boolean Union 예:

```typescript
function normalizeEnabled(value: boolean | string): boolean {
  if (typeof value === "boolean") {
    return value;
  }

  return value === "true";
}
```

unknown string 검증 예:

```typescript
function parseKeyword(value: unknown): string {
  if (typeof value === "string") {
    return value.trim();
  }

  return "";
}
```

실무 기준:

- Primitive Type 구분은 `typeof` 사용
- object 검증 시 null check 함께 작성
- number input value는 string으로 들어올 수 있어 변환 필요
- Type Assertion으로 Primitive 변환 대체 금지

---

### [FAQ]

Q. typeof Narrowing은 언제 써?
A. string, number, boolean 같은 Primitive Type을 구분할 때 사용한다.

Q. `typeof null`은 뭐야?
A. JavaScript에서 `typeof null`은 `"object"`다. 그래서 object check에는 `value !== null`이 필요하다.

Q. 배열도 typeof로 확인해?
A. 아니다. 배열은 `Array.isArray()`로 확인하는 것이 좋다.

---

## 2.2 typeof Object Caution

### [개념]

`typeof value === "object"`는 객체 가능성을 확인하지만 `null`도 object로 판정되므로 주의가 필요하다.

```typescript
function isObject(value: unknown): boolean {
  return typeof value === "object" && value !== null;
}
```

Object Type Guard에서는 `typeof`와 null check를 함께 사용해야 한다.

---

### [핵심]

Object Narrowing 주의:

- `typeof null === "object"`
- null check 필수
- array도 object로 판단됨
- Date도 object로 판단됨
- plain object와 class instance 구분 필요 가능
- property 검사에는 `in` operator 사용 가능

---

### [실무]

나쁜 예:

```typescript
function hasTitle(value: unknown): boolean {
  return typeof value === "object" && "title" in value;
}
```

문제:

- value가 null이면 `"title" in value`에서 Runtime Error 발생 가능

개선:

```typescript
function hasTitle(value: unknown): boolean {
  return typeof value === "object" && value !== null && "title" in value;
}
```

더 안전한 예:

```typescript
type TitleObject = {
  title: string;
};

function isTitleObject(value: unknown): value is TitleObject {
  return (
    typeof value === "object" &&
    value !== null &&
    "title" in value &&
    typeof value.title === "string"
  );
}
```

실무 기준:

- object 검사는 항상 null check 포함
- property 존재 확인 후 value Type 확인
- array 가능성이 있으면 `Array.isArray()`로 별도 처리
- Runtime Data 검증은 Type Guard로 분리 가능

---

### [FAQ]

Q. object narrowing에서 왜 null check가 필요해?
A. JavaScript에서 `typeof null`이 `"object"`이기 때문이다.

Q. `typeof value === "object"`면 plain object야?
A. 아니다. null, array, Date 같은 값과 구분이 필요할 수 있다.

Q. property Type까지 확인해야 해?
A. 외부 데이터 검증에서는 property 존재뿐 아니라 value Type까지 확인하는 것이 안전하다.

---

# 3. instanceof Narrowing

## 3.1 instanceof Narrowing Definition

### [개념]

`instanceof` Narrowing은 값이 특정 class 또는 built-in 객체의 instance인지 확인해 Type을 좁히는 방식이다.

```typescript
function formatDate(value: string | Date): string {
  if (value instanceof Date) {
    return value.toLocaleDateString("ko-KR");
  }

  return new Date(value).toLocaleDateString("ko-KR");
}
```

`instanceof`는 Date, Error, custom class instance를 구분할 때 유용하다.

---

### [핵심]

`instanceof` 사용 영역:

- Date
- Error
- custom class
- Map
- Set
- URL
- File
- Blob

주의:

- plain object에는 적합하지 않을 수 있음
- JSON API Response는 class instance가 아님
- API 날짜 string은 Date instance가 아님
- iframe / 다른 realm에서는 주의 필요 가능
- Runtime 객체 생성 여부 확인 필요

---

### [실무]

Error 처리 예:

```typescript
function getErrorMessage(error: unknown): string {
  if (error instanceof Error) {
    return error.message;
  }

  return "알 수 없는 오류가 발생했습니다.";
}
```

Date 처리 예:

```typescript
function normalizeDate(value: string | Date): Date {
  if (value instanceof Date) {
    return value;
  }

  return new Date(value);
}
```

File 처리 예:

```typescript
function getFileSize(value: unknown): number {
  if (value instanceof File) {
    return value.size;
  }

  return 0;
}
```

실무 기준:

- try / catch error는 unknown으로 받고 Error인지 확인
- API 날짜 string은 `new Date()`로 명시적 변환
- JSON Response를 class instance로 오해하지 않음
- Form File 처리에서 File instance 확인 가능

---

### [FAQ]

Q. instanceof Narrowing은 언제 써?
A. Date, Error, File, custom class처럼 instance 확인이 필요한 객체에 사용한다.

Q. API에서 받은 JSON 객체에 instanceof를 쓰면 돼?
A. 대부분 적합하지 않다. JSON 객체는 plain object이고 class instance가 아니다.

Q. catch error는 어떻게 Type Narrowing해?
A. `error instanceof Error`로 확인한 뒤 `error.message`를 사용할 수 있다.

---

## 3.2 Error Narrowing

### [개념]

Error Narrowing은 `unknown`으로 받은 오류 값을 안전하게 Error 객체인지 확인한 뒤 메시지를 추출하는 방식이다.

```typescript
function getErrorMessage(error: unknown): string {
  if (error instanceof Error) {
    return error.message;
  }

  return "알 수 없는 오류가 발생했습니다.";
}
```

try / catch에서 error는 다양한 값일 수 있으므로 바로 `error.message`에 접근하지 않는 것이 안전하다.

---

### [핵심]

Error Narrowing 핵심:

- catch error는 unknown 가능
- Error instance 확인
- fallback message 제공
- API Error Response와 구분
- 사용자 메시지와 개발자 로그 구분
- 민감한 서버 오류 직접 노출 금지

---

### [실무]

try / catch 예:

```typescript
async function loadFestivalList(): Promise<void> {
  try {
    await fetch("/api/festivals");
  } catch (error: unknown) {
    const message = getErrorMessage(error);
    console.error(message);
  }
}
```

API Error Response와 구분:

```typescript
type ApiErrorResponse = {
  success: false;
  message: string;
  code?: string;
};

function isApiErrorResponse(value: unknown): value is ApiErrorResponse {
  return (
    typeof value === "object" &&
    value !== null &&
    "success" in value &&
    value.success === false &&
    "message" in value &&
    typeof value.message === "string"
  );
}
```

실무 기준:

- catch error는 unknown으로 처리
- Error instance가 아니면 fallback message 사용
- API Error Response는 별도 Type Guard 사용
- 사용자에게 민감한 오류 detail 노출 금지
- Review Agent는 `catch (e) { e.message }` 패턴 확인

---

### [FAQ]

Q. catch error는 항상 Error 객체야?
A. 아니다. JavaScript에서는 어떤 값이든 throw될 수 있으므로 unknown으로 보고 검증하는 것이 안전하다.

Q. error.message를 바로 쓰면 안 돼?
A. error가 Error instance가 아닐 수 있으므로 `instanceof Error` 확인 후 사용하는 것이 좋다.

Q. API Error Response와 JavaScript Error는 같아?
A. 아니다. API Error Response는 서버 응답 데이터이고 JavaScript Error는 Runtime Error 객체다.

---

# 4. in Operator Narrowing

## 4.1 in Operator Definition

### [개념]

`in` operator Narrowing은 객체에 특정 property가 존재하는지 확인해 Type을 좁히는 방식이다.

```typescript
type Festival = {
  title: string;
};

function hasTitle(value: unknown): value is Festival {
  return typeof value === "object" && value !== null && "title" in value;
}
```

`in` operator는 객체 Union이나 unknown object의 property 존재 여부를 확인할 때 유용하다.

---

### [핵심]

`in` operator 사용 영역:

- object union narrowing
- unknown object validation
- optional property check
- API response shape check
- feature-specific object check

주의:

- object와 null check 선행 필요
- property 존재만 확인
- property value Type은 별도 검사 필요
- optional property는 존재하지 않을 수 있음
- prototype chain property도 포함될 수 있음

---

### [실무]

Object Union 예:

```typescript
type SuccessResponse = {
  data: string[];
};

type ErrorResponse = {
  message: string;
};

function getResponseText(response: SuccessResponse | ErrorResponse): string {
  if ("data" in response) {
    return `${response.data.length} items`;
  }

  return response.message;
}
```

unknown object 예:

```typescript
type Festival = {
  festivalId: number;
  title: string;
};

function isFestival(value: unknown): value is Festival {
  return (
    typeof value === "object" &&
    value !== null &&
    "festivalId" in value &&
    typeof value.festivalId === "number" &&
    "title" in value &&
    typeof value.title === "string"
  );
}
```

실무 기준:

- property 존재 확인에는 `in` 사용
- 외부 데이터는 value Type까지 검사
- Union Object는 공통 discriminant property가 있으면 그 값을 기준으로 Narrowing
- `in`만으로 안전하다고 단정하지 않음

---

### [FAQ]

Q. in operator Narrowing은 언제 써?
A. 객체에 특정 property가 있는지 확인해 Union Object나 unknown object를 좁힐 때 사용한다.

Q. `"title" in value`만 쓰면 안전해?
A. 아니다. value가 object이고 null이 아닌지 먼저 확인해야 한다.

Q. in operator는 property Type까지 확인해?
A. 아니다. property 존재만 확인하므로 value Type은 typeof 등으로 추가 확인해야 한다.

---

## 4.2 Property Existence vs Property Type

### [개념]

Property Existence Check는 property가 존재하는지만 확인하고, Property Type Check는 해당 property 값의 Type까지 확인한다.

```text
"title" in value
→ title property 존재 확인

typeof value.title === "string"
→ title 값이 string인지 확인
```

외부 데이터 검증에서는 존재 여부와 Type 확인을 함께 하는 것이 안전하다.

---

### [핵심]

구분:

- existence check
- value type check
- nullable check
- optional check
- nested property check

주의:

- property가 있어도 값 Type이 다를 수 있음
- property가 있어도 null일 수 있음
- API Response는 Type 정의와 다르게 올 수 있음
- Type Assertion으로 검증 생략 금지

---

### [실무]

부족한 검증:

```typescript
function hasUserId(value: unknown): boolean {
  return typeof value === "object" && value !== null && "userId" in value;
}
```

문제:

- `userId`가 number인지 확인하지 않는다.

개선:

```typescript
type User = {
  userId: number;
};

function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "userId" in value &&
    typeof value.userId === "number"
  );
}
```

Nullable property 검증:

```typescript
type Profile = {
  imageUrl: string | null;
};

function isProfile(value: unknown): value is Profile {
  return (
    typeof value === "object" &&
    value !== null &&
    "imageUrl" in value &&
    (typeof value.imageUrl === "string" || value.imageUrl === null)
  );
}
```

실무 기준:

- 중요한 외부 데이터는 property Type까지 확인
- nullable field는 `value === null` 조건 포함
- optional field는 존재하지 않는 경우도 허용
- 복잡한 검증은 Schema Validation 도구 고려

---

### [FAQ]

Q. property 존재 확인과 Type 확인은 달라?
A. 다르다. 존재 확인은 key가 있는지만 보고 Type 확인은 value의 Type까지 검사한다.

Q. API 응답 검증에서 둘 다 필요해?
A. 중요한 데이터라면 property 존재와 value Type을 모두 확인하는 것이 안전하다.

Q. nullable property는 어떻게 검증해?
A. `typeof value === "string" || value === null`처럼 null 가능성을 함께 확인한다.

---

# 5. Equality Narrowing

## 5.1 Equality Narrowing Definition

### [개념]

Equality Narrowing은 `===`, `!==`, `==`, `!=` 같은 비교를 통해 Type을 좁히는 방식이다.

실무에서는 명확성을 위해 `===`, `!==` 사용을 권장한다.

```typescript
function getTitle(title: string | null): string {
  if (title !== null) {
    return title;
  }

  return "제목 없음";
}
```

Equality Narrowing은 null check, literal value check, discriminated union에서 자주 사용된다.

---

### [핵심]

Equality Narrowing 사용 영역:

- null check
- undefined check
- literal value check
- status check
- role check
- discriminant property check
- optional value check

권장:

- `value === null`
- `value !== null`
- `value === undefined`
- `value !== undefined`
- `status === "success"`
- `role === "ROLE_ADMIN"`

---

### [실무]

Status Narrowing 예:

```typescript
type ApiState<T> =
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; message: string };

function getDataLength<T>(state: ApiState<T[]>): number {
  if (state.status === "success") {
    return state.data.length;
  }

  return 0;
}
```

Role Narrowing 예:

```typescript
type UserRole = "ROLE_USER" | "ROLE_ADMIN";

function canAccessAdmin(role: UserRole): boolean {
  return role === "ROLE_ADMIN";
}
```

null check 예:

```typescript
function getRatingText(rating: number | null): string {
  if (rating !== null) {
    return rating.toFixed(1);
  }

  return "평점 없음";
}
```

실무 기준:

- literal union은 equality check로 좁힘
- null과 undefined는 명확히 구분
- discriminated union은 status / type / kind 값을 기준으로 좁힘
- `== null` 패턴은 팀 컨벤션 확인 후 사용
- RAG 문서에서는 `===`, `!==` 우선

---

### [FAQ]

Q. Equality Narrowing은 언제 써?
A. null, undefined, literal status, role 값을 비교해 Type을 좁힐 때 사용한다.

Q. `===`와 `==` 중 뭐가 좋아?
A. 실무 TypeScript에서는 명확성을 위해 `===`, `!==`를 권장한다.

Q. Discriminated Union은 어떻게 좁혀?
A. `state.status === "success"`처럼 공통 구분 property 값을 비교해 좁힌다.

---

## 5.2 Null and Undefined Narrowing

### [개념]

Null and Undefined Narrowing은 값이 `null` 또는 `undefined`인지 확인해 안전하게 사용하는 방식이다.

```typescript
function getNickname(nickname?: string): string {
  if (nickname !== undefined) {
    return nickname;
  }

  return "Guest";
}
```

null과 undefined는 의미가 다르므로 Type에 맞는 조건을 사용해야 한다.

---

### [핵심]

Null Narrowing:

- `value !== null`
- `value === null`
- `value ?? fallback`
- `value?.property`

Undefined Narrowing:

- `value !== undefined`
- `value === undefined`
- optional property check
- optional parameter check
- `value ?? fallback`

주의:

- optional property는 undefined 가능
- nullable property는 null 가능
- `??`는 null 또는 undefined에 fallback 적용
- `||`는 falsy 값 전체에 fallback 적용

---

### [실무]

Optional Property 예:

```typescript
type SearchParams = {
  keyword?: string;
};

function getKeyword(params: SearchParams): string {
  return params.keyword ?? "";
}
```

Nullable Property 예:

```typescript
type UserProfile = {
  imageUrl: string | null;
};

function getProfileImageUrl(profile: UserProfile): string {
  return profile.imageUrl ?? "/default-profile.png";
}
```

`||` 주의:

```typescript
function getPage(page: number | null): number {
  return page ?? 1;
}
```

설명:

- `page`가 0일 수 있다면 `||`보다 `??`가 안전하다.
- `??`는 null / undefined에만 fallback을 적용한다.

실무 기준:

- optional은 undefined 가능성 처리
- nullable은 null 가능성 처리
- fallback에는 `??` 우선 고려
- 0, 빈 문자열, false를 유효 값으로 봐야 하면 `||` 사용 주의

---

### [FAQ]

Q. null과 undefined Narrowing은 어떻게 해?
A. `value !== null`, `value !== undefined`, optional chaining, nullish coalescing을 사용한다.

Q. `??`와 `||`는 뭐가 달라?
A. `??`는 null 또는 undefined에만 fallback을 적용하고, `||`는 0, 빈 문자열, false에도 fallback을 적용한다.

Q. optional property는 null이야 undefined야?
A. 기본적으로 property가 없거나 undefined일 수 있다는 의미다. null은 별도로 명시해야 한다.

---

# 6. Truthiness Narrowing

## 6.1 Truthiness Narrowing Definition

### [개념]

Truthiness Narrowing은 조건문에서 값의 truthy / falsy 여부를 기준으로 Type을 좁히는 방식이다.

```typescript
function getTitle(title: string | null): string {
  if (title) {
    return title;
  }

  return "제목 없음";
}
```

Truthy check는 간단하지만 빈 문자열, 0, false도 falsy로 처리되므로 주의가 필요하다.

---

### [핵심]

Falsy 값:

- `false`
- `0`
- `""`
- `null`
- `undefined`
- `NaN`

장점:

- 간결한 null / undefined 방어
- optional value 간단 처리
- UI fallback 처리에 편리

주의:

- 빈 문자열도 false로 처리
- 0도 false로 처리
- false도 false로 처리
- 정확한 null check가 필요한 경우 부적합
- 데이터 의미에 따라 오류 가능

---

### [실무]

간단한 문자열 fallback:

```typescript
function getDisplayName(name: string | null): string {
  return name || "이름 없음";
}
```

0이 유효한 경우 주의:

```typescript
function getReviewCount(count: number | null): number {
  return count ?? 0;
}
```

나쁜 예:

```typescript
function getReviewCount(count: number | null): number {
  return count || 10;
}
```

문제:

- count가 0이면 유효한 값인데 10으로 바뀐다.

실무 기준:

- null / undefined fallback은 `??` 우선
- 빈 문자열도 fallback 처리해야 하면 `||` 가능
- 숫자 값에는 truthy check 주의
- boolean 값에는 truthy check 의미 확인
- 명확한 조건이 필요한 경우 equality check 사용

---

### [FAQ]

Q. Truthiness Narrowing은 뭐야?
A. if 조건에서 값이 truthy인지 falsy인지 확인해 Type을 좁히는 방식이다.

Q. Truthiness Check는 항상 안전해?
A. 아니다. 0, 빈 문자열, false도 falsy로 처리되므로 데이터 의미에 따라 주의해야 한다.

Q. null fallback에는 `||`와 `??` 중 뭐가 좋아?
A. null 또는 undefined만 fallback 처리하려면 `??`가 더 안전하다.

---

## 6.2 Optional Chaining

### [개념]

Optional Chaining은 객체가 null 또는 undefined일 수 있을 때 안전하게 property나 method에 접근하는 문법이다.

```typescript
const imageUrl = user.profile?.imageUrl;
```

중간 값이 null 또는 undefined이면 Runtime Error 대신 undefined를 반환한다.

---

### [핵심]

Optional Chaining 형태:

- `object?.property`
- `object?.method()`
- `array?.[index]`
- `callback?.()`

사용 영역:

- nullable nested object
- optional callback
- optional props
- API response nested field
- array optional access

주의:

- undefined 반환 가능성 처리 필요
- null을 제거하는 것이 아니라 안전 접근만 수행
- 너무 긴 optional chain은 데이터 구조 재검토 필요
- fallback은 `??`와 함께 사용 가능

---

### [실무]

Nested Object 예:

```typescript
type UserResponse = {
  userId: number;
  profile: {
    imageUrl: string | null;
  } | null;
};

function getProfileImage(user: UserResponse): string {
  return user.profile?.imageUrl ?? "/default-profile.png";
}
```

Optional Callback 예:

```typescript
type ModalProps = {
  onClose?: () => void;
};

function closeModal(props: ModalProps): void {
  props.onClose?.();
}
```

Array Access 예:

```typescript
function getFirstTitle(festivals?: { title: string }[]): string {
  return festivals?.[0]?.title ?? "축제 없음";
}
```

실무 기준:

- nullable nested object 접근에 사용
- optional callback 호출에 사용
- fallback은 `??`로 처리
- optional chaining 결과 Type은 undefined 가능성 포함
- 중요한 필수 데이터가 계속 optional이면 API Type 재검토

---

### [FAQ]

Q. Optional Chaining은 뭐야?
A. null 또는 undefined 가능성이 있는 값에 안전하게 접근하는 문법이다.

Q. `user.profile?.imageUrl` 결과는 뭐야?
A. profile이 있으면 imageUrl이고, profile이 null 또는 undefined면 undefined다.

Q. Optional Callback은 어떻게 호출해?
A. `onClose?.()`처럼 호출한다.

---

# 7. Discriminated Union Narrowing

## 7.1 Discriminated Union Narrowing Definition

### [개념]

Discriminated Union Narrowing은 공통 구분 property 값을 기준으로 Union Object를 좁히는 방식이다.

```typescript
type ApiState<T> =
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; message: string };
```

`status` 값이 `"success"`이면 TypeScript는 해당 객체가 `data`를 가진 구조임을 알 수 있다.

---

### [핵심]

Discriminated Union Narrowing 요소:

- discriminant property
- literal value
- object union
- status check
- switch statement
- exhaustive check
- state-specific data

구분 property 후보:

- `status`
- `type`
- `kind`
- `mode`
- `variant`

---

### [실무]

if Narrowing 예:

```typescript
function getDataCount<T>(state: ApiState<T[]>): number {
  if (state.status === "success") {
    return state.data.length;
  }

  return 0;
}
```

switch Narrowing 예:

```typescript
function getStateMessage<T>(state: ApiState<T>): string {
  switch (state.status) {
    case "loading":
      return "로딩 중";
    case "success":
      return "완료";
    case "error":
      return state.message;
  }
}
```

실무 기준:

- 상태별 데이터 구조가 다르면 Discriminated Union 사용
- 구분 property 이름은 일관되게 유지
- `status` 값은 literal union으로 제한
- switch 분기는 Exhaustive Check 고려
- Boolean flag 여러 개보다 모순 상태를 줄임

---

### [FAQ]

Q. Discriminated Union Narrowing은 뭐야?
A. 공통 구분 property 값을 기준으로 Union Object를 안전하게 좁히는 방식이다.

Q. status property가 왜 중요해?
A. TypeScript가 status 값을 보고 해당 객체 구조를 판단할 수 있기 때문이다.

Q. loading / success / error 상태에 적합해?
A. 그렇다. 상태별 데이터 구조가 다르면 매우 적합하다.

---

## 7.2 Exhaustive Check with never

### [개념]

Exhaustive Check는 Discriminated Union 또는 Literal Union의 모든 가능한 값을 처리했는지 확인하는 방식이다.

`never` Type을 사용하면 누락된 분기를 TypeScript가 감지할 수 있다.

```typescript
type RequestStatus = "idle" | "loading" | "success" | "error";
```

---

### [핵심]

Exhaustive Check 목적:

- switch case 누락 방지
- 상태 값 추가 시 오류 감지
- Union Type 변경 추적
- Review 안정성 향상
- never Type 활용

---

### [실무]

예:

```typescript
type RequestStatus = "idle" | "loading" | "success" | "error";

function getStatusMessage(status: RequestStatus): string {
  switch (status) {
    case "idle":
      return "대기";
    case "loading":
      return "로딩 중";
    case "success":
      return "성공";
    case "error":
      return "오류";
    default: {
      const exhaustiveCheck: never = status;
      return exhaustiveCheck;
    }
  }
}
```

Discriminated Union 예:

```typescript
type ModalState =
  | { type: "closed" }
  | { type: "confirm"; message: string }
  | { type: "alert"; message: string };

function getModalMessage(state: ModalState): string {
  switch (state.type) {
    case "closed":
      return "";
    case "confirm":
      return state.message;
    case "alert":
      return state.message;
    default: {
      const exhaustiveCheck: never = state;
      return exhaustiveCheck;
    }
  }
}
```

실무 기준:

- 중요한 상태 분기는 Exhaustive Check 사용
- Union 값이 추가될 가능성이 있으면 유용
- default에서 무조건 fallback만 반환하면 누락을 숨길 수 있음
- Review Agent는 switch case 누락 확인

---

### [FAQ]

Q. Exhaustive Check는 왜 필요해?
A. Union Type의 모든 가능한 값을 처리했는지 확인해 분기 누락을 방지하기 위해 필요하다.

Q. never를 왜 써?
A. 처리되지 않은 값이 남아 있으면 never에 할당할 수 없어 Type Error를 발생시키기 위해 쓴다.

Q. 모든 switch에 never check를 넣어야 해?
A. 필수는 아니지만 중요한 상태 분기에는 유용하다.

---

# 8. Custom Type Guard

## 8.1 Type Guard Definition

### [개념]

Custom Type Guard는 함수가 특정 Type인지 검사하고, true일 때 TypeScript에 해당 Type임을 알려주는 함수다.

반환 Type에 `value is Type` 형태를 사용한다.

```typescript
function isString(value: unknown): value is string {
  return typeof value === "string";
}
```

Type Guard는 unknown, API Response, localStorage, URL Query 같은 외부 데이터를 안전하게 다룰 때 중요하다.

---

### [핵심]

Custom Type Guard 구성:

- input value
- Runtime check
- `value is Type`
- boolean result
- Type Narrowing effect
- property existence check
- property type check

사용 영역:

- unknown validation
- API Response validation
- localStorage parse
- URL Query validation
- Type-safe filter
- Runtime data guard

---

### [실무]

Primitive Guard 예:

```typescript
function isString(value: unknown): value is string {
  return typeof value === "string";
}
```

Object Guard 예:

```typescript
type Festival = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

function isFestival(value: unknown): value is Festival {
  return (
    typeof value === "object" &&
    value !== null &&
    "festivalId" in value &&
    typeof value.festivalId === "number" &&
    "title" in value &&
    typeof value.title === "string" &&
    "imageUrl" in value &&
    (typeof value.imageUrl === "string" || value.imageUrl === null)
  );
}
```

사용 예:

```typescript
function parseFestival(value: unknown): Festival | null {
  if (isFestival(value)) {
    return value;
  }

  return null;
}
```

실무 기준:

- Type Guard는 Runtime 조건과 Type 정의가 일치해야 함
- property 존재와 value Type을 함께 확인
- nullable field는 null 가능성 반영
- 복잡한 데이터는 Schema Validation 고려
- Type Assertion보다 Type Guard 우선

---

### [FAQ]

Q. Type Guard가 뭐야?
A. 값이 특정 Type인지 검사하고 true일 때 TypeScript에 그 Type임을 알려주는 함수다.

Q. `value is Type`은 뭐야?
A. 함수가 true를 반환하면 value가 해당 Type이라고 TypeScript에 알려주는 문법이다.

Q. Type Guard는 언제 써?
A. unknown 값, API Response, localStorage, URL Query처럼 Type을 확신할 수 없는 값에 사용한다.

---

## 8.2 API Response Type Guard

### [개념]

API Response Type Guard는 서버 응답 데이터가 기대한 Type 구조를 만족하는지 Runtime에서 확인하는 함수다.

```typescript
function isApiResponse(value: unknown): value is ApiResponse<unknown> {
  return (
    typeof value === "object" &&
    value !== null &&
    "success" in value &&
    typeof value.success === "boolean" &&
    "message" in value &&
    typeof value.message === "string"
  );
}
```

TypeScript Type은 Runtime API Response를 자동 검증하지 않으므로 중요한 외부 데이터에는 Type Guard가 필요할 수 있다.

---

### [핵심]

API Response Type Guard 확인 대상:

- response wrapper
- success field
- data field
- message field
- error code
- nullable field
- list field
- page / slice field
- field errors

주의:

- 모든 API에 수동 Guard를 작성하면 비용 증가
- 중요한 경계 데이터에 우선 적용
- 복잡한 구조는 Zod 같은 Schema Validation 도구 고려
- Type Guard와 Type Definition 불일치 주의

---

### [실무]

공통 응답 Guard 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};

function isApiResponse(value: unknown): value is ApiResponse<unknown> {
  return (
    typeof value === "object" &&
    value !== null &&
    "success" in value &&
    typeof value.success === "boolean" &&
    "data" in value &&
    "message" in value &&
    typeof value.message === "string"
  );
}
```

목록 데이터 Guard 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
};

function isFestivalInfoResponse(value: unknown): value is FestivalInfoResponse {
  return (
    typeof value === "object" &&
    value !== null &&
    "festivalId" in value &&
    typeof value.festivalId === "number" &&
    "title" in value &&
    typeof value.title === "string"
  );
}

function isFestivalList(value: unknown): value is FestivalInfoResponse[] {
  return Array.isArray(value) && value.every(isFestivalInfoResponse);
}
```

실무 기준:

- 외부 데이터 신뢰 수준에 따라 Guard 적용
- list는 `Array.isArray()`와 `every()` 활용
- wrapper와 data 내부 구조 모두 확인 가능
- API Client Layer에서 검증 위치 통일
- Validation 실패 시 fallback 또는 error 처리

---

### [FAQ]

Q. API Response도 Type Guard가 필요해?
A. TypeScript Type만으로 Runtime 응답이 검증되지는 않으므로 중요한 외부 데이터에는 필요할 수 있다.

Q. 모든 API Response에 Guard를 만들어야 해?
A. 필수는 아니다. 신뢰 경계, 중요 데이터, 오류 가능성이 높은 응답에 우선 적용한다.

Q. 배열 응답은 어떻게 Guard해?
A. `Array.isArray(value)`로 배열인지 확인하고 `value.every(itemGuard)`로 element를 검증한다.

---

## 8.3 Type Guard Naming

### [개념]

Type Guard 함수 이름은 값이 특정 Type인지 확인한다는 의미가 드러나야 한다.

일반적으로 `is`, `has`, `can` prefix를 사용한다.

```typescript
function isFestival(value: unknown): value is Festival {
  return true;
}
```

좋은 이름은 RAG 검색성과 Review Agent 검토 품질을 높인다.

---

### [핵심]

권장 Prefix:

- `is`
- `has`
- `can`
- `should`

권장 이름:

- `isFestival`
- `isUserResponse`
- `isApiErrorResponse`
- `hasFestivalImage`
- `isRequestStatus`
- `isUserRole`
- `canAccessAdmin`

주의:

- `checkData`처럼 모호한 이름 지양
- return Type이 boolean인지 Type Predicate인지 명확히 함
- Type Guard와 일반 Predicate 구분
- Runtime 조건과 이름이 일치해야 함

---

### [실무]

좋은 예:

```typescript
type UserRole = "ROLE_USER" | "ROLE_ADMIN";

function isUserRole(value: string): value is UserRole {
  return value === "ROLE_USER" || value === "ROLE_ADMIN";
}
```

Sort Option 예:

```typescript
type FestivalSortOption = "latest" | "popular" | "rating";

function isFestivalSortOption(value: string): value is FestivalSortOption {
  return value === "latest" || value === "popular" || value === "rating";
}
```

이미지 보유 여부 예:

```typescript
type Festival = {
  imageUrl: string | null;
};

type FestivalWithImage = Festival & {
  imageUrl: string;
};

function hasFestivalImage(festival: Festival): festival is FestivalWithImage {
  return festival.imageUrl !== null;
}
```

실무 기준:

- Type Guard 이름은 검사 목적을 명확히 작성
- Literal Union Guard는 `isXxx` 사용
- property 존재 Guard는 `hasXxx` 사용
- 권한 판단은 `canXxx` 사용
- Type Predicate 반환 여부 확인

---

### [FAQ]

Q. Type Guard 함수 이름은 어떻게 지어?
A. `isFestival`, `isUserRole`, `hasFestivalImage`처럼 검사 목적이 드러나게 짓는다.

Q. Predicate와 Type Guard 이름이 달라도 돼?
A. 가능하지만 Type Guard는 Type을 좁힌다는 의미가 드러나는 이름이 좋다.

Q. `checkData` 같은 이름은 왜 안 좋아?
A. 어떤 Type을 검증하는지 알기 어렵고 RAG 검색성이 낮다.

---

# 9. Type Guard with Array Filter

## 9.1 Filter Narrowing

### [개념]

Filter Narrowing은 배열에서 특정 조건을 만족하는 element만 남기면서 Type을 좁히는 방식이다.

일반 predicate만으로는 nullable property가 원하는 만큼 좁혀지지 않을 수 있어 Type Guard를 사용한다.

```typescript
const values: Array<string | null> = ["a", null, "b"];
```

---

### [핵심]

Filter Narrowing 사용 영역:

- null 제거
- undefined 제거
- 특정 object shape만 남기기
- imageUrl 있는 항목만 남기기
- 성공 응답만 남기기
- 유효한 form field만 남기기

주의:

- `filter(Boolean)`은 Type이 충분히 좁혀지지 않을 수 있음
- Type Guard Predicate 사용 권장
- falsy 값 제거 시 0, 빈 문자열도 제거될 수 있음
- nullable 제거와 truthy 제거 구분

---

### [실무]

null 제거 Guard:

```typescript
function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}

const values: Array<string | null> = ["a", null, "b"];
const strings: string[] = values.filter(isNotNull);
```

null / undefined 제거 Guard:

```typescript
function isDefined<T>(value: T | null | undefined): value is T {
  return value !== null && value !== undefined;
}
```

Image Filter 예:

```typescript
type Festival = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

type FestivalWithImage = Festival & {
  imageUrl: string;
};

function hasFestivalImage(festival: Festival): festival is FestivalWithImage {
  return festival.imageUrl !== null;
}

function getFestivalsWithImage(festivals: Festival[]): FestivalWithImage[] {
  return festivals.filter(hasFestivalImage);
}
```

실무 기준:

- nullable 배열은 Type Guard로 filter
- `filter(Boolean)` 남용 금지
- Type Guard 반환 Type 확인
- 필터링 후 Type이 의도대로 좁혀졌는지 확인
- Review Agent는 filter 결과 Type을 확인

---

### [FAQ]

Q. filter로 null을 제거하면 Type도 자동으로 string[]이 돼?
A. 일반 조건만으로는 부족할 수 있다. Type Guard Predicate를 사용하면 명확히 좁힐 수 있다.

Q. `filter(Boolean)`을 쓰면 안 돼?
A. 쓸 수 있지만 0, 빈 문자열도 제거되고 Type이 원하는 대로 좁혀지지 않을 수 있어 주의해야 한다.

Q. 배열에서 null과 undefined를 제거하려면 어떻게 해?
A. `isDefined<T>(value): value is T` 같은 Type Guard를 만들어 filter에 사용한다.

---

# 10. Type Assertion vs Type Guard

## 10.1 Type Assertion Problem

### [개념]

Type Assertion은 개발자가 TypeScript에게 특정 값의 Type을 강제로 믿게 하는 문법이다.

```typescript
const user = response as UserResponse;
```

Type Assertion은 Runtime 검증을 하지 않는다.
따라서 외부 데이터에 남용하면 Runtime Error를 숨길 수 있다.

---

### [핵심]

Type Assertion 특징:

- Compile Time 검사 우회
- Runtime 값 변환 없음
- Runtime 검증 없음
- 자동완성은 가능
- 잘못 사용하면 오류 은폐
- 외부 데이터에 남용 위험

위험한 사용:

- API Response 강제 단정
- localStorage 값 강제 단정
- URL Query 값 강제 단정
- nullable 값을 non-null로 단정
- DOM element 강제 단정

---

### [실무]

위험 예:

```typescript
type User = {
  userId: number;
  nickname: string;
};

const user = JSON.parse(localStorage.getItem("user") ?? "{}") as User;
console.log(user.nickname.toUpperCase());
```

문제:

- localStorage 데이터가 User 구조인지 검증하지 않음
- nickname이 없으면 Runtime Error 가능

개선:

```typescript
function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "userId" in value &&
    typeof value.userId === "number" &&
    "nickname" in value &&
    typeof value.nickname === "string"
  );
}
```

실무 기준:

- 외부 데이터에는 Type Guard 우선
- Assertion은 TypeScript가 알기 어려운 안전한 상황에 제한
- `as unknown as Type` 패턴 지양
- Assertion으로 Runtime 변환 대체 금지
- Review Agent는 `as` 남용 확인

---

### [FAQ]

Q. Type Assertion은 뭐야?
A. 개발자가 TypeScript에게 값의 Type을 강제로 알려주는 문법이다.

Q. Type Assertion은 Runtime 검증을 해?
A. 아니다. TypeScript 검사만 우회할 뿐 Runtime 검증이나 값 변환은 하지 않는다.

Q. API Response에 as를 써도 돼?
A. 신뢰할 수 있는 API Client 내부에서는 제한적으로 가능하지만, 중요한 외부 데이터는 Type Guard나 Schema Validation을 고려해야 한다.

---

## 10.2 Type Guard Preferred Pattern

### [개념]

Type Guard Preferred Pattern은 Type Assertion으로 강제 단정하기보다 Runtime 조건을 작성해 Type을 안전하게 좁히는 방식이다.

```text
Unknown Value
→ Type Guard
→ Safe Type
→ Safe Usage
```

Type Guard는 Runtime 검증과 TypeScript Narrowing을 연결한다.

---

### [핵심]

Type Guard 장점:

- Runtime 조건 기반
- Compile Time Narrowing 제공
- 외부 데이터 검증 가능
- nullable 처리 명확
- 오류 은폐 감소
- Review 가능성 향상

Type Guard 우선 상황:

- API Response
- localStorage
- JSON parse
- URL Query
- user input
- unknown error
- nullable object

---

### [실무]

URL Query Guard 예:

```typescript
type FestivalSortOption = "latest" | "popular" | "rating";

function isFestivalSortOption(value: string): value is FestivalSortOption {
  return value === "latest" || value === "popular" || value === "rating";
}

function parseSortOption(value: string | null): FestivalSortOption {
  if (value !== null && isFestivalSortOption(value)) {
    return value;
  }

  return "latest";
}
```

API Error Guard 예:

```typescript
type ApiErrorResponse = {
  success: false;
  message: string;
};

function isApiErrorResponse(value: unknown): value is ApiErrorResponse {
  return (
    typeof value === "object" &&
    value !== null &&
    "success" in value &&
    value.success === false &&
    "message" in value &&
    typeof value.message === "string"
  );
}
```

실무 기준:

- 외부 string을 literal union으로 바로 assertion하지 않음
- Query Parameter는 허용 값 검증 후 사용
- Error Response는 구조 검증 후 사용
- Type Guard는 reusable utility로 관리 가능
- 검증 실패 시 fallback 제공

---

### [FAQ]

Q. Type Guard가 Type Assertion보다 좋은 이유는?
A. Type Guard는 Runtime 조건을 확인하므로 잘못된 데이터 사용 위험을 줄인다.

Q. URL Query 값을 literal union으로 바꿀 때 as를 써도 돼?
A. 권장하지 않는다. 허용 값인지 Type Guard로 확인한 뒤 사용해야 한다.

Q. Type Guard는 모든 곳에 써야 해?
A. 모든 값에 필수는 아니다. 외부 데이터, unknown, 중요한 nullable 데이터에 우선 적용한다.

---

# 11. Common Mistakes

## 11.1 Narrowing Mistakes

### [개념]

Type Narrowing 실수는 Type을 충분히 좁히지 않았거나, truthy check를 잘못 사용하거나, Runtime 검증 없이 Type Assertion으로 우회할 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Union Type 사용 전 Narrowing 누락
- nullable value 직접 접근
- optional property 직접 접근
- `typeof value === "object"`에서 null check 누락
- `in` operator 사용 전 object check 누락
- property existence만 보고 value Type 미확인
- `filter(Boolean)`으로 Type Narrowing 기대
- 0, 빈 문자열을 truthy check로 잘못 처리
- URL Query 값을 literal union으로 단정
- catch error를 Error로 단정
- Type Assertion으로 검증 우회

---

### [실무]

나쁜 예:

```typescript
function getImageUrl(imageUrl: string | null): string {
  return imageUrl.toUpperCase();
}
```

문제:

- `imageUrl`이 null일 수 있다.

개선:

```typescript
function getImageUrl(imageUrl: string | null): string {
  return imageUrl ?? "/default-image.png";
}
```

나쁜 예:

```typescript
function getTitle(value: unknown): string {
  if ("title" in value) {
    return value.title;
  }

  return "";
}
```

문제:

- value가 object인지 확인하지 않았다.
- value가 null이면 Runtime Error 가능
- title Type을 확인하지 않았다.

개선:

```typescript
function getTitle(value: unknown): string {
  if (
    typeof value === "object" &&
    value !== null &&
    "title" in value &&
    typeof value.title === "string"
  ) {
    return value.title;
  }

  return "";
}
```

실무 기준:

- nullable 값은 직접 접근 금지
- object check에는 null check 포함
- in operator 전에 object 확인
- property Type까지 확인
- fallback 처리 명확화

---

### [FAQ]

Q. Type Narrowing에서 가장 흔한 실수는?
A. null check 누락, object check 누락, Type Assertion으로 검증을 우회하는 것이다.

Q. `in` operator 오류는 왜 나?
A. 대상 값이 object가 아니거나 null일 수 있는데 먼저 확인하지 않았기 때문이다.

Q. truthy check는 왜 조심해야 해?
A. 0, 빈 문자열, false도 falsy로 처리되어 유효한 값이 fallback으로 바뀔 수 있기 때문이다.

---

## 11.2 Type Guard Mistakes

### [개념]

Type Guard 실수는 Runtime 조건이 Type 정의와 다르거나, property 존재만 확인하고 실제 value Type을 확인하지 않을 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- `value is Type`만 쓰고 검증 조건 부실
- property 존재만 확인
- nullable field 검증 누락
- array element 검증 누락
- Type 정의 변경 후 Guard 미수정
- Guard 이름과 검증 내용 불일치
- `as Type`을 Guard 내부에서 무분별하게 사용
- 모든 API에 수동 Guard를 과도하게 작성
- Schema Validation 필요 상황에서 수동 Guard만 사용

---

### [실무]

부실한 Guard:

```typescript
type User = {
  userId: number;
  nickname: string;
};

function isUser(value: unknown): value is User {
  return typeof value === "object" && value !== null;
}
```

문제:

- userId 존재 확인 없음
- nickname 존재 확인 없음
- property Type 확인 없음

개선:

```typescript
function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "userId" in value &&
    typeof value.userId === "number" &&
    "nickname" in value &&
    typeof value.nickname === "string"
  );
}
```

배열 Guard:

```typescript
function isUserList(value: unknown): value is User[] {
  return Array.isArray(value) && value.every(isUser);
}
```

실무 기준:

- Type Guard는 Type Definition 변경 시 함께 수정
- property Type까지 검증
- nullable field는 null 가능성 포함
- array는 element guard 사용
- 복잡한 구조는 Schema Validation 검토

---

### [FAQ]

Q. Type Guard에서 가장 흔한 실수는?
A. property 존재만 확인하고 value Type을 확인하지 않는 것이다.

Q. Type Guard는 Type 정의가 바뀌면 수정해야 해?
A. 해야 한다. Guard 조건과 Type 정의가 불일치하면 잘못된 Narrowing이 발생한다.

Q. 복잡한 API Response도 수동 Type Guard로 처리해?
A. 가능하지만 구조가 복잡하면 Schema Validation 도구를 고려하는 것이 좋다.

---

# 12. Review Checklist

## 12.1 Part08 Checklist

### [개념]

TypeScript Foundation Part08 검수는 Type Narrowing, Type Guard, Runtime Validation, API Response Validation, Type Assertion 위험성을 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] Type Narrowing 정의가 포함되었는가?
- [ ] Narrowing Flow가 포함되었는가?
- [ ] typeof Narrowing 설명이 포함되었는가?
- [ ] typeof object null 주의가 포함되었는가?
- [ ] instanceof Narrowing 설명이 포함되었는가?
- [ ] Error Narrowing 설명이 포함되었는가?
- [ ] in operator Narrowing 설명이 포함되었는가?
- [ ] Property Existence와 Property Type 차이가 포함되었는가?
- [ ] Equality Narrowing 설명이 포함되었는가?
- [ ] Null / Undefined Narrowing 설명이 포함되었는가?
- [ ] Truthiness Narrowing 주의가 포함되었는가?
- [ ] Optional Chaining 설명이 포함되었는가?
- [ ] Discriminated Union Narrowing 설명이 포함되었는가?
- [ ] Exhaustive Check with never 설명이 포함되었는가?
- [ ] Custom Type Guard 설명이 포함되었는가?
- [ ] API Response Type Guard 예제가 포함되었는가?
- [ ] Type Guard Naming 기준이 포함되었는가?
- [ ] Filter Narrowing 예제가 포함되었는가?
- [ ] Type Assertion vs Type Guard 비교가 포함되었는가?
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
→ Narrowing Pattern Check
→ Runtime Validation Check
→ Type Guard Check
→ API Response Guard Check
→ Assertion Risk Check
→ Common Mistake Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

Part08은 이후 Generic, Utility Type, API Type, React TypeScript Readiness, Troubleshooting 문서의 안정성 기반이다.

---

### [FAQ]

Q. Part08에서 가장 중요한 검수 기준은?
A. Type Narrowing과 Type Guard를 통해 unknown, nullable, API Response를 안전하게 사용하는 기준이 명확한지 확인하는 것이다.

Q. Part08이 이후 문서와 어떻게 연결돼?
A. Generic Function, API Response Type, Error Response Type, React Event Type, Type Error Troubleshooting의 안정성 기준으로 연결된다.

---

# Retrieval Queries

### [FAQ]

Q. Type Narrowing이 뭐야?
A. 넓은 Type을 조건문과 검증 로직으로 더 구체적인 Type으로 좁히는 과정이다.

Q. Type Narrowing은 왜 필요해?
A. Union Type, unknown, null 가능 값을 안전하게 사용하기 위해 필요하다.

Q. Type Assertion 대신 Narrowing을 써야 해?
A. 가능하면 Narrowing이 더 안전하다. Assertion은 검증 없이 TypeScript를 우회할 수 있다.

Q. Type Narrowing은 Runtime 검증이야?
A. 조건문은 Runtime에서 실행되고, TypeScript는 그 조건을 근거로 Compile Time Type을 좁힌다.

Q. Narrowing Flow는 어떻게 잡아?
A. 값의 출처 확인 → Runtime 조건 확인 → Type 좁히기 → 안전한 사용 → fallback 처리 순서로 잡는다.

Q. typeof Narrowing은 언제 써?
A. string, number, boolean 같은 Primitive Type을 구분할 때 사용한다.

Q. `typeof null`은 뭐야?
A. JavaScript에서 `typeof null`은 `"object"`다. 그래서 object check에는 `value !== null`이 필요하다.

Q. 배열도 typeof로 확인해?
A. 아니다. 배열은 `Array.isArray()`로 확인하는 것이 좋다.

Q. object narrowing에서 왜 null check가 필요해?
A. JavaScript에서 `typeof null`이 `"object"`이기 때문이다.

Q. `typeof value === "object"`면 plain object야?
A. 아니다. null, array, Date 같은 값과 구분이 필요할 수 있다.

Q. instanceof Narrowing은 언제 써?
A. Date, Error, File, custom class처럼 instance 확인이 필요한 객체에 사용한다.

Q. API에서 받은 JSON 객체에 instanceof를 쓰면 돼?
A. 대부분 적합하지 않다. JSON 객체는 plain object이고 class instance가 아니다.

Q. catch error는 어떻게 Type Narrowing해?
A. `error instanceof Error`로 확인한 뒤 `error.message`를 사용할 수 있다.

Q. catch error는 항상 Error 객체야?
A. 아니다. JavaScript에서는 어떤 값이든 throw될 수 있으므로 unknown으로 보고 검증하는 것이 안전하다.

Q. error.message를 바로 쓰면 안 돼?
A. error가 Error instance가 아닐 수 있으므로 `instanceof Error` 확인 후 사용하는 것이 좋다.

Q. API Error Response와 JavaScript Error는 같아?
A. 아니다. API Error Response는 서버 응답 데이터이고 JavaScript Error는 Runtime Error 객체다.

Q. in operator Narrowing은 언제 써?
A. 객체에 특정 property가 있는지 확인해 Union Object나 unknown object를 좁힐 때 사용한다.

Q. `"title" in value`만 쓰면 안전해?
A. 아니다. value가 object이고 null이 아닌지 먼저 확인해야 한다.

Q. in operator는 property Type까지 확인해?
A. 아니다. property 존재만 확인하므로 value Type은 typeof 등으로 추가 확인해야 한다.

Q. property 존재 확인과 Type 확인은 달라?
A. 다르다. 존재 확인은 key가 있는지만 보고 Type 확인은 value의 Type까지 검사한다.

Q. API 응답 검증에서 property 존재와 Type 확인이 둘 다 필요해?
A. 중요한 데이터라면 property 존재와 value Type을 모두 확인하는 것이 안전하다.

Q. nullable property는 어떻게 검증해?
A. `typeof value === "string" || value === null`처럼 null 가능성을 함께 확인한다.

Q. Equality Narrowing은 언제 써?
A. null, undefined, literal status, role 값을 비교해 Type을 좁힐 때 사용한다.

Q. `===`와 `==` 중 뭐가 좋아?
A. 실무 TypeScript에서는 명확성을 위해 `===`, `!==`를 권장한다.

Q. Discriminated Union은 어떻게 좁혀?
A. `state.status === "success"`처럼 공통 구분 property 값을 비교해 좁힌다.

Q. null과 undefined Narrowing은 어떻게 해?
A. `value !== null`, `value !== undefined`, optional chaining, nullish coalescing을 사용한다.

Q. `??`와 `||`는 뭐가 달라?
A. `??`는 null 또는 undefined에만 fallback을 적용하고, `||`는 0, 빈 문자열, false에도 fallback을 적용한다.

Q. optional property는 null이야 undefined야?
A. 기본적으로 property가 없거나 undefined일 수 있다는 의미다. null은 별도로 명시해야 한다.

Q. Truthiness Narrowing은 뭐야?
A. if 조건에서 값이 truthy인지 falsy인지 확인해 Type을 좁히는 방식이다.

Q. Truthiness Check는 항상 안전해?
A. 아니다. 0, 빈 문자열, false도 falsy로 처리되므로 데이터 의미에 따라 주의해야 한다.

Q. null fallback에는 `||`와 `??` 중 뭐가 좋아?
A. null 또는 undefined만 fallback 처리하려면 `??`가 더 안전하다.

Q. Optional Chaining은 뭐야?
A. null 또는 undefined 가능성이 있는 값에 안전하게 접근하는 문법이다.

Q. `user.profile?.imageUrl` 결과는 뭐야?
A. profile이 있으면 imageUrl이고, profile이 null 또는 undefined면 undefined다.

Q. Optional Callback은 어떻게 호출해?
A. `onClose?.()`처럼 호출한다.

Q. Discriminated Union Narrowing은 뭐야?
A. 공통 구분 property 값을 기준으로 Union Object를 안전하게 좁히는 방식이다.

Q. status property가 왜 중요해?
A. TypeScript가 status 값을 보고 해당 객체 구조를 판단할 수 있기 때문이다.

Q. loading / success / error 상태에 적합해?
A. 그렇다. 상태별 데이터 구조가 다르면 매우 적합하다.

Q. Exhaustive Check는 왜 필요해?
A. Union Type의 모든 가능한 값을 처리했는지 확인해 분기 누락을 방지하기 위해 필요하다.

Q. never를 왜 써?
A. 처리되지 않은 값이 남아 있으면 never에 할당할 수 없어 Type Error를 발생시키기 위해 쓴다.

Q. Type Guard가 뭐야?
A. 값이 특정 Type인지 검사하고 true일 때 TypeScript에 그 Type임을 알려주는 함수다.

Q. `value is Type`은 뭐야?
A. 함수가 true를 반환하면 value가 해당 Type이라고 TypeScript에 알려주는 문법이다.

Q. Type Guard는 언제 써?
A. unknown 값, API Response, localStorage, URL Query처럼 Type을 확신할 수 없는 값에 사용한다.

Q. API Response도 Type Guard가 필요해?
A. TypeScript Type만으로 Runtime 응답이 검증되지는 않으므로 중요한 외부 데이터에는 필요할 수 있다.

Q. 모든 API Response에 Guard를 만들어야 해?
A. 필수는 아니다. 신뢰 경계, 중요 데이터, 오류 가능성이 높은 응답에 우선 적용한다.

Q. 배열 응답은 어떻게 Guard해?
A. `Array.isArray(value)`로 배열인지 확인하고 `value.every(itemGuard)`로 element를 검증한다.

Q. Type Guard 함수 이름은 어떻게 지어?
A. `isFestival`, `isUserRole`, `hasFestivalImage`처럼 검사 목적이 드러나게 짓는다.

Q. `checkData` 같은 이름은 왜 안 좋아?
A. 어떤 Type을 검증하는지 알기 어렵고 RAG 검색성이 낮다.

Q. filter로 null을 제거하면 Type도 자동으로 string[]이 돼?
A. 일반 조건만으로는 부족할 수 있다. Type Guard Predicate를 사용하면 명확히 좁힐 수 있다.

Q. `filter(Boolean)`을 쓰면 안 돼?
A. 쓸 수 있지만 0, 빈 문자열도 제거되고 Type이 원하는 대로 좁혀지지 않을 수 있어 주의해야 한다.

Q. 배열에서 null과 undefined를 제거하려면 어떻게 해?
A. `isDefined<T>(value): value is T` 같은 Type Guard를 만들어 filter에 사용한다.

Q. Type Assertion은 뭐야?
A. 개발자가 TypeScript에게 값의 Type을 강제로 알려주는 문법이다.

Q. Type Assertion은 Runtime 검증을 해?
A. 아니다. TypeScript 검사만 우회할 뿐 Runtime 검증이나 값 변환은 하지 않는다.

Q. Type Guard가 Type Assertion보다 좋은 이유는?
A. Type Guard는 Runtime 조건을 확인하므로 잘못된 데이터 사용 위험을 줄인다.

Q. URL Query 값을 literal union으로 바꿀 때 as를 써도 돼?
A. 권장하지 않는다. 허용 값인지 Type Guard로 확인한 뒤 사용해야 한다.

Q. Type Narrowing에서 가장 흔한 실수는?
A. null check 누락, object check 누락, Type Assertion으로 검증을 우회하는 것이다.

Q. `in` operator 오류는 왜 나?
A. 대상 값이 object가 아니거나 null일 수 있는데 먼저 확인하지 않았기 때문이다.

Q. Type Guard에서 가장 흔한 실수는?
A. property 존재만 확인하고 value Type을 확인하지 않는 것이다.

Q. Type Guard는 Type 정의가 바뀌면 수정해야 해?
A. 해야 한다. Guard 조건과 Type 정의가 불일치하면 잘못된 Narrowing이 발생한다.

Q. TypeScript Part08의 핵심은 뭐야?
A. Type Narrowing과 Type Guard로 unknown, nullable, API Response를 안전하게 사용하는 것이다.

Q. TypeScript Part08 다음 문서는 뭐가 좋아?
A. Generic and Utility Types 문서가 적합하다.
