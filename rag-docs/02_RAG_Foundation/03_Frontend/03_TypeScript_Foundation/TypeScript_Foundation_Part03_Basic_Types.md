# TypeScript Foundation Part03 - Basic Types

---

# 1. Primitive Type

## 1.1 Primitive Type Definition

### [개념]

Primitive Type은 JavaScript 기본 값에 대응하는 TypeScript Type이다.

TypeScript의 Primitive Type은 Runtime 값을 새로 만드는 기능이 아니라 JavaScript 값의 Type을 Compile Time에 검사하기 위한 기준이다.

```typescript
const title: string = "Festival";
const count: number = 10;
const active: boolean = true;
```

Primitive Type은 TypeScript Foundation의 가장 기본 단위이며 Object Type, Function Type, API Type, React Props Type의 기반이 된다.

---

### [핵심]

TypeScript 주요 Primitive Type:

- `string`
- `number`
- `boolean`
- `null`
- `undefined`
- `symbol`
- `bigint`

실무 핵심:

- 문자열 값은 `string`
- 숫자 값은 `number`
- 참 / 거짓 값은 `boolean`
- 의도적 값 없음은 `null`
- 값 미할당은 `undefined`
- 객체 Wrapper Type인 `String`, `Number`, `Boolean` 사용 지양
- API nullable field는 `string | null`처럼 Union Type으로 명시

---

### [실무]

2026 Frontend 실무 기준에서는 Primitive Type을 단순 암기보다 API Response, Form Data, Props, State와 연결해 사용한다.

예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  active: boolean;
};
```

사용 기준:

- `festivalId: number` → 식별자
- `title: string` → 텍스트
- `imageUrl: string | null` → 이미지 URL이 없을 수 있음
- `active: boolean` → 활성 여부

주의:

- API에서 숫자가 문자열로 오는 경우 `number`로 단정하지 않는다.
- JSON 날짜 값은 대부분 `string`으로 수신한다.
- `null` 가능성은 반드시 Type에 반영한다.
- Runtime 변환은 Type이 아니라 Mapping Function에서 처리한다.

---

### [FAQ]

Q. Primitive Type이 뭐야?
A. string, number, boolean, null, undefined처럼 JavaScript 기본 값에 대응하는 TypeScript Type이다.

Q. string과 String은 같아?
A. 아니다. string은 Primitive Type이고 String은 객체 Wrapper Type이다. 실무에서는 string을 사용한다.

Q. number는 정수와 실수를 구분해?
A. 아니다. JavaScript number는 정수와 실수를 모두 표현한다.

Q. API에서 null이 올 수 있으면 어떻게 써?
A. `string | null`, `number | null`처럼 Union Type으로 명시한다.

---

## 1.2 String Type

### [개념]

`string` Type은 문자열 값을 표현하는 TypeScript Primitive Type이다.

```typescript
const userName: string = "jun";
const festivalTitle: string = "Spring Festival";
```

문자열은 화면 텍스트, API 필드, Form 입력값, URL, 상태 메시지에서 자주 사용된다.

---

### [핵심]

`string` 사용 영역:

- title
- name
- email
- address
- imageUrl
- date string
- message
- token
- query parameter
- route parameter

주의:

- `String` 대신 `string` 사용
- 숫자 문자열과 number 구분
- JSON 날짜 값은 일반적으로 string
- 빈 문자열과 null은 다른 의미
- literal union으로 허용 문자열 제한 가능

---

### [실무]

API Response 예:

```typescript
type UserResponse = {
  userId: number;
  nickname: string;
  email: string;
  profileImageUrl: string | null;
};
```

Form Data 예:

```typescript
type LoginForm = {
  email: string;
  password: string;
};
```

날짜 문자열 예:

```typescript
type FestivalDateResponse = {
  eventStartDate: string;
  eventEndDate: string;
};
```

실무 기준:

- 사용자 입력값은 대부분 string으로 시작한다.
- 숫자 입력도 input value 단계에서는 string일 수 있다.
- API 날짜는 string으로 받은 뒤 필요하면 Date로 변환한다.
- Token 값은 string이지만 로그 출력 금지 대상이다.

---

### [FAQ]

Q. input에서 받은 숫자는 number야?
A. 대부분 input value는 string이다. 숫자로 쓰려면 Number 같은 Runtime 변환이 필요하다.

Q. 날짜는 string이야 Date야?
A. JSON API 응답에서는 대부분 string으로 받고 필요하면 Frontend에서 Date로 변환한다.

Q. 빈 문자열과 null은 같아?
A. 아니다. 빈 문자열은 값이 있는 string이고 null은 값이 없음을 의미한다.

---

## 1.3 Number Type

### [개념]

`number` Type은 JavaScript의 숫자 값을 표현하는 TypeScript Primitive Type이다.

```typescript
const price: number = 10000;
const rating: number = 4.5;
const count: number = 0;
```

TypeScript의 `number`는 정수와 실수를 구분하지 않는다.

---

### [핵심]

`number` 사용 영역:

- id
- count
- price
- rating
- page
- size
- index
- latitude
- longitude
- average score

주의:

- TypeScript `number`는 정수 / 실수 구분 없음
- API에서 숫자가 string으로 올 수 있음
- input value는 string으로 들어올 수 있음
- `Number` 객체 Type 사용 지양
- NaN 가능성 주의
- 금액, 평점, 좌표는 validation 필요

---

### [실무]

API Response 예:

```typescript
type ReviewResponse = {
  reviewId: number;
  rating: number;
  likeCount: number;
};
```

Pagination 예:

```typescript
type SliceResponse<T> = {
  content: T[];
  number: number;
  size: number;
  hasNext: boolean;
};
```

Runtime 변환 예:

```typescript
function parsePage(value: string): number {
  return Number(value);
}
```

주의:

```typescript
const page: number = "1" as unknown as number;
```

문제:

- Runtime 값이 실제 number로 변환되지 않는다.
- Type Assertion은 값 변환이 아니다.
- 실제 변환은 `Number()`로 처리해야 한다.

---

### [FAQ]

Q. TypeScript number는 int와 float을 구분해?
A. 아니다. number 하나로 정수와 실수를 모두 표현한다.

Q. 문자열 숫자를 number Type으로 쓰면 자동 변환돼?
A. 아니다. `Number()` 같은 Runtime 변환이 필요하다.

Q. API id 값은 보통 number야?
A. Backend 응답 구조에 따라 다르다. 실제 API Response와 DTO를 확인해야 한다.

---

## 1.4 Boolean Type

### [개념]

`boolean` Type은 `true` 또는 `false` 값을 표현하는 TypeScript Primitive Type이다.

```typescript
const isLogin: boolean = true;
const isLoading: boolean = false;
```

Boolean Type은 상태 플래그, 권한 체크, 조건 분기에서 자주 사용된다.

---

### [핵심]

`boolean` 사용 영역:

- isLoading
- isLogin
- isFavorite
- hasNext
- active
- success
- checked
- disabled
- visible

주의:

- `Boolean` 객체 Type 사용 지양
- 복잡한 비동기 상태는 boolean보다 literal union 고려
- `success: boolean`과 `status: "success"`는 목적이 다름
- boolean이 많아지면 상태 조합 오류 가능

---

### [실무]

API Response Wrapper 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};
```

UI 상태 예:

```typescript
type ButtonState = {
  disabled: boolean;
  loading: boolean;
};
```

비동기 상태가 복잡한 경우:

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";

let status: AsyncStatus = "idle";
```

실무 기준:

- 단순 true / false 상태는 boolean 사용
- 상태 단계가 3개 이상이면 literal union 고려
- `is`, `has`, `can`, `should` prefix로 의미 명확화
- boolean flag가 여러 개면 상태 모델 재검토

---

### [FAQ]

Q. boolean은 언제 써?
A. true 또는 false로 표현되는 단순 상태에 사용한다.

Q. loading 상태는 boolean으로 충분해?
A. 단순 loading 여부만 필요하면 충분하다. idle, success, error까지 필요하면 literal union이 좋다.

Q. Boolean과 boolean 차이는?
A. boolean은 Primitive Type이고 Boolean은 객체 Wrapper Type이다. 실무에서는 boolean을 사용한다.

---

# 2. Null and Undefined

## 2.1 Null Type

### [개념]

`null`은 의도적으로 값이 없음을 표현하는 JavaScript 값이며 TypeScript에서도 Type으로 다룰 수 있다.

```typescript
let selectedUserId: number | null = null;
```

`null`은 API Response, 선택된 값, 초기 State, optional relation에서 자주 등장한다.

---

### [핵심]

`null` 사용 상황:

- 선택된 값 없음
- API field 값 없음
- 초기 State 값 없음
- 이미지 URL 없음
- 로그인 사용자 정보 없음
- 검색 결과 없음

주의:

- `null`은 빈 문자열과 다름
- `null`은 0과 다름
- `null`은 false와 다름
- `strictNullChecks`에서 null 가능성 명시 필요
- 사용 전 null check 필요

---

### [실무]

nullable API field 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  averageRating: number | null;
};
```

null 처리 예:

```typescript
function getImageUrl(imageUrl: string | null): string {
  return imageUrl ?? "/default-image.png";
}
```

React State 초기값 예:

```typescript
type User = {
  userId: number;
  nickname: string;
};

const initialUser: User | null = null;
```

실무 기준:

- API에서 null 가능하면 Type에 반영
- null 가능 값은 사용 전 fallback 처리
- `??` nullish coalescing 활용
- `?.` optional chaining 활용
- Type Assertion으로 null 가능성 제거 금지

---

### [FAQ]

Q. null은 언제 써?
A. 의도적으로 값이 없음을 표현해야 할 때 사용한다.

Q. null 가능 값은 어떻게 Type으로 써?
A. `User | null`, `string | null`, `number | null`처럼 Union Type으로 쓴다.

Q. Object is possibly null 오류는 왜 나?
A. 값이 null일 수 있는데 null check 없이 사용하려고 해서 발생한다.

---

## 2.2 Undefined Type

### [개념]

`undefined`는 값이 아직 할당되지 않았거나 property / parameter가 생략되었을 때 나타나는 JavaScript 값이다.

```typescript
let keyword: string | undefined = undefined;
```

Optional Property와 Optional Parameter는 기본적으로 `undefined` 가능성을 가진다.

---

### [핵심]

`undefined` 발생 상황:

- 값 미할당
- optional property 누락
- optional parameter 생략
- 배열 index 접근 결과 없음
- object property 없음
- 함수 return 누락

주의:

- `undefined`와 `null`은 다른 의미
- Optional Property는 undefined 가능
- Optional Parameter는 undefined 가능
- 사용 전 기본값 처리 필요

---

### [실무]

Optional Property 예:

```typescript
type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
};
```

Optional Parameter 예:

```typescript
function createPageUrl(page?: number): string {
  return `/page/${page ?? 1}`;
}
```

배열 접근 예:

```typescript
function getFirst<T>(items: T[]): T | undefined {
  return items[0];
}
```

실무 기준:

- 생략 가능한 값은 optional property 사용
- 값이 없음을 명시적으로 내려주는 API는 null 사용 가능
- optional 값은 `??`로 기본값 처리
- undefined 가능성을 무시하지 않음

---

### [FAQ]

Q. undefined는 언제 생겨?
A. 값이 할당되지 않았거나 optional property / parameter가 생략되었을 때 생긴다.

Q. optional property는 null이야 undefined야?
A. 기본적으로 property가 없거나 undefined일 수 있다는 의미다. null도 허용하려면 별도로 `| null`을 써야 한다.

Q. undefined 가능 값은 어떻게 처리해?
A. 기본값 처리, optional chaining, nullish coalescing을 사용한다.

---

## 2.3 Null vs Undefined

### [개념]

`null`과 `undefined`는 모두 값이 없음을 표현할 수 있지만 의미가 다르다.

```text
null
→ 의도적으로 값 없음

undefined
→ 값 미할당 또는 생략
```

TypeScript에서는 두 값을 구분해 Type으로 명시하는 것이 중요하다.

---

### [핵심]

| 비교              | null           | undefined          |
| ----------------- | -------------- | ------------------ |
| 의미              | 의도적 값 없음 | 미할당 / 생략      |
| API Response      | 자주 사용      | 상대적으로 적음    |
| Optional Property | 직접 명시 필요 | 기본 가능          |
| State 초기값      | 자주 사용      | 상황별 사용        |
| 기본 처리         | `??` 사용      | `??` 사용          |
| strictNullChecks  | 명시 필요      | 명시 또는 optional |

---

### [실무]

Optional과 Nullable 구분:

```typescript
type UserProfile = {
  nickname?: string;
  profileImageUrl: string | null;
};
```

의미:

```text
nickname?: string
→ nickname property가 없거나 undefined 가능

profileImageUrl: string | null
→ property는 있지만 값이 null 가능
```

실무 기준:

- Backend API가 null을 반환하면 `| null`로 표현
- Frontend 내부 optional config는 `?` 사용 가능
- optional과 nullable을 혼용하지 않도록 의미 통일
- API DTO 기준과 TypeScript Type 정합성 유지

---

### [FAQ]

Q. null과 undefined는 같아?
A. 아니다. null은 의도적 값 없음이고 undefined는 미할당 또는 생략을 의미한다.

Q. `name?: string`과 `name: string | null`은 같아?
A. 아니다. optional은 property 누락 가능성이고 nullable은 값이 null일 가능성이다.

Q. API 응답에서 값이 없으면 null과 undefined 중 뭐가 좋아?
A. Backend 응답 정책에 따라 다르다. 실제 응답 구조에 맞춰 Frontend Type을 정의해야 한다.

---

# 3. Array Type

## 3.1 Array Type Definition

### [개념]

Array Type은 같은 형태의 여러 값을 담는 배열 Type이다.

```typescript
const names: string[] = ["jun", "kim"];
const scores: number[] = [90, 80, 70];
```

TypeScript 배열은 element Type을 기준으로 Type Check를 수행한다.

---

### [핵심]

Array Type 작성 방식:

- `string[]`
- `number[]`
- `boolean[]`
- `Festival[]`
- `Array<T>`
- `readonly T[]`
- `ReadonlyArray<T>`

주의:

- 빈 배열은 Type 명시 권장
- API 목록 응답은 `ResponseType[]`로 명시
- 배열 method 결과 Type 확인
- 원본 변경 method 주의
- 객체 배열은 별도 Type 정의 권장

---

### [실무]

객체 배열 예:

```typescript
type Festival = {
  festivalId: number;
  title: string;
};

const festivals: Festival[] = [
  { festivalId: 1, title: "Spring Festival" },
  { festivalId: 2, title: "Summer Festival" },
];
```

API 목록 응답 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};

type FestivalListResponse = ApiResponse<Festival[]>;
```

실무 기준:

- 목록 API는 `T[]` 또는 Page / Slice wrapper로 표현
- 빈 배열 State는 Type 명시
- map / filter / find 결과 Type 확인
- find 결과는 `T | undefined` 가능
- sort / push / splice는 원본 변경 주의

---

### [FAQ]

Q. Array Type은 어떻게 써?
A. `string[]`, `number[]`, `Festival[]` 또는 `Array<T>` 형태로 작성한다.

Q. string[]와 Array<string> 중 뭐가 좋아?
A. 둘 다 가능하다. 일반 배열은 string[] 형태가 간결하고 자주 사용된다.

Q. 객체 배열 Type은 어떻게 정의해?
A. 객체 Type을 type 또는 interface로 정의한 뒤 `Festival[]`처럼 사용한다.

---

## 3.2 Empty Array Type

### [개념]

빈 배열은 TypeScript가 element Type을 정확히 알기 어려운 경우가 많다.

```typescript
const festivals = [];
```

위 코드만으로는 배열에 어떤 Type의 값이 들어갈지 의도가 명확하지 않다.

---

### [핵심]

빈 배열 Type 명시가 필요한 상황:

- React State 초기값
- API 목록 초기값
- 누적 결과 배열
- Form field list
- Table row list
- Option list
- Message list
- Notification list

---

### [실무]

권장:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
};

const festivals: FestivalInfoResponse[] = [];
```

Generic 함수 예:

```typescript
function createEmptyList<T>(): T[] {
  return [];
}
```

React State 준비 예:

```typescript
type ChatMessage = {
  messageId: number;
  content: string;
};

const initialMessages: ChatMessage[] = [];
```

실무 기준:

- 빈 배열은 element Type을 명시한다.
- API Response List Type을 재사용한다.
- 임시로 `any[]` 사용 금지
- 초기값과 실제 사용 데이터 Type을 일치시킨다.

---

### [FAQ]

Q. 빈 배열에는 왜 Type을 써야 해?
A. TypeScript가 배열에 어떤 element가 들어갈지 정확히 추론하기 어렵기 때문이다.

Q. 빈 배열을 any[]로 두면 안 돼?
A. 가능은 하지만 Type Safety가 무너지므로 구체적 Type을 사용하는 것이 좋다.

Q. React State 빈 배열도 Type이 필요해?
A. 쓰는 것이 좋다. 초기값만으로 element Type을 알기 어렵기 때문이다.

---

## 3.3 Readonly Array

### [개념]

Readonly Array는 배열 원본을 직접 변경하지 못하도록 Type 단계에서 제한하는 배열 Type이다.

```typescript
function getTitles(festivals: readonly Festival[]): string[] {
  return festivals.map((festival) => festival.title);
}
```

Readonly는 Runtime 불변성을 완전히 보장하지 않고 TypeScript Type Check 단계에서 변경을 제한한다.

---

### [핵심]

Readonly Array 작성 방식:

- `readonly T[]`
- `ReadonlyArray<T>`

원본 변경 method 주의:

- `push`
- `pop`
- `shift`
- `unshift`
- `splice`
- `sort`
- `reverse`

비변경 method:

- `map`
- `filter`
- `slice`
- `find`
- `some`
- `every`

---

### [실무]

입력 배열 보호 예:

```typescript
type Festival = {
  festivalId: number;
  title: string;
};

function getFestivalTitles(festivals: readonly Festival[]): string[] {
  return festivals.map((festival) => festival.title);
}
```

React State 관련 기준:

- State 배열 직접 변경 금지
- 새 배열을 생성해 업데이트
- 함수 입력 배열은 readonly로 보호 가능
- Review Agent는 원본 변경 method 사용 여부 확인

주의:

```typescript
function sortFestivals(festivals: Festival[]): Festival[] {
  return festivals.sort((a, b) => a.festivalId - b.festivalId);
}
```

문제:

- `sort`는 원본 배열을 변경한다.

개선:

```typescript
function sortFestivals(festivals: readonly Festival[]): Festival[] {
  return [...festivals].sort((a, b) => a.festivalId - b.festivalId);
}
```

---

### [FAQ]

Q. readonly array는 Runtime에서도 변경을 막아?
A. 아니다. TypeScript Type Check 단계에서 직접 변경을 제한한다.

Q. readonly array는 언제 써?
A. 함수 입력 배열을 보호하거나 React State 원본 변경을 막고 싶을 때 유용하다.

Q. sort는 원본 배열을 바꿔?
A. 그렇다. 원본 변경을 피하려면 복사 후 sort를 사용한다.

---

# 4. Tuple Type

## 4.1 Tuple Type Definition

### [개념]

Tuple Type은 길이와 위치별 Type이 정해진 배열 Type이다.

```typescript
const point: [number, number] = [127.0276, 37.4979];
```

Tuple은 일반 배열보다 구조가 고정되어 있으며 위치별 의미가 중요할 때 사용한다.

---

### [핵심]

Tuple 핵심:

- fixed length array
- position-based type
- coordinate
- pair data
- readonly tuple
- destructuring
- array와 구분

주의:

- 긴 tuple은 가독성 저하
- 위치 순서 실수 가능
- 필드 의미가 많으면 object type 권장
- API Response에 긴 tuple 사용 지양

---

### [실무]

좌표 예:

```typescript
type Coordinate = [number, number];

const gangnam: Coordinate = [127.0276, 37.4979];
```

Destructuring 예:

```typescript
const [longitude, latitude] = gangnam;
```

readonly tuple 예:

```typescript
type ReadonlyCoordinate = readonly [number, number];
```

실무 기준:

- 좌표, pair, fixed result에 제한적으로 사용
- 의미 있는 필드가 많으면 object type 사용
- Frontend API Response는 object type이 더 명확한 경우가 많다

---

### [FAQ]

Q. Tuple은 언제 써?
A. 좌표나 쌍 데이터처럼 길이와 위치 의미가 명확한 짧은 데이터에 사용한다.

Q. Tuple 대신 object를 써도 돼?
A. 가능하다. 필드 의미를 명확히 보여줘야 하면 object가 더 좋다.

Q. Tuple은 배열이야?
A. 배열 기반이지만 길이와 위치별 Type이 고정된 특수한 배열 Type이다.

---

## 4.2 Tuple vs Array

### [개념]

Array는 같은 Type의 여러 값을 담는 구조이고 Tuple은 위치마다 Type과 의미가 정해진 구조다.

```typescript
const scores: number[] = [90, 80, 70];
const point: [number, number] = [127.0276, 37.4979];
```

---

### [핵심]

| 비교      | Array             | Tuple                 |
| --------- | ----------------- | --------------------- |
| 길이      | 가변              | 고정                  |
| Type      | element Type 중심 | 위치별 Type 중심      |
| 의미      | 목록 데이터       | 고정 구조 데이터      |
| 예        | Festival[]        | [longitude, latitude] |
| 가독성    | 목록에 적합       | 짧은 구조에 적합      |
| 실무 권장 | API list          | 좌표 / pair           |

---

### [실무]

Array가 적합한 경우:

```typescript
type Festival = {
  festivalId: number;
  title: string;
};

const festivals: Festival[] = [];
```

Tuple이 적합한 경우:

```typescript
type Coordinate = [number, number];

function moveToMapCenter(coordinate: Coordinate): void {
  const [longitude, latitude] = coordinate;
  console.log(longitude, latitude);
}
```

Object가 더 좋은 경우:

```typescript
type CoordinateObject = {
  longitude: number;
  latitude: number;
};
```

실무 기준:

- 목록은 Array
- 짧고 위치 의미가 명확하면 Tuple
- 협업 가독성이 중요하면 Object
- API DTO는 Object Type 우선 고려

---

### [FAQ]

Q. Array와 Tuple 차이는?
A. Array는 길이가 가변인 목록이고 Tuple은 길이와 위치별 Type이 고정된 배열이다.

Q. 좌표는 Tuple과 Object 중 뭐가 좋아?
A. 짧은 내부 데이터는 Tuple도 가능하지만 API나 협업 코드에서는 Object가 더 명확할 수 있다.

Q. 긴 Tuple을 써도 돼?
A. 가능하지만 가독성이 떨어지므로 object type을 권장한다.

---

# 5. Special Types

## 5.1 Any Type

### [개념]

`any` Type은 TypeScript의 Type Check를 사실상 비활성화하는 Type이다.

```typescript
let value: any = "hello";

value.toUnknownMethod();
```

`any`는 모든 property 접근과 함수 호출을 허용하므로 Type Safety를 크게 낮춘다.

---

### [핵심]

`any` 특징:

- 모든 Type 할당 가능
- 모든 property 접근 가능
- 모든 function call 가능
- Type Check 우회
- 자동완성 품질 저하
- Runtime Error 증가 가능
- API 구조 변경 감지 어려움

사용 지양 대상:

- API Response
- Component Props
- Event Handler
- Form Data
- State
- Utility Function Parameter

---

### [실무]

나쁜 예:

```typescript
function renderFestival(festival: any): string {
  return festival.title;
}
```

개선:

```typescript
type Festival = {
  title: string;
};

function renderFestival(festival: Festival): string {
  return festival.title;
}
```

Migration 임시 사용 기준:

```typescript
// TODO: replace any with FestivalInfoResponse
let tempData: any;
```

실무 기준:

- 최종 코드에서 any 제거
- 외부 입력은 unknown 우선
- API Response Type 정의
- any 사용 시 범위 최소화
- TODO로 추적 가능하게 관리

---

### [FAQ]

Q. any는 왜 피해야 해?
A. TypeScript의 Type Check를 우회해서 오류를 미리 잡기 어렵게 만든다.

Q. any를 아예 쓰면 안 돼?
A. 임시 Migration에서는 제한적으로 사용할 수 있지만 최종 코드에서는 제거하는 것이 좋다.

Q. any 대신 뭘 써?
A. 구체적 Type을 정의하거나, Type을 모르는 외부 입력은 unknown을 사용한다.

---

## 5.2 Unknown Type

### [개념]

`unknown` Type은 어떤 값인지 알 수 없음을 표현하지만, 사용하기 전에 Type 검사를 요구하는 안전한 Type이다.

```typescript
function parseValue(value: unknown): string {
  if (typeof value === "string") {
    return value;
  }

  return "";
}
```

`unknown`은 `any`보다 안전한 외부 입력 Type이다.

---

### [핵심]

`unknown` 특징:

- 모든 값을 받을 수 있음
- 바로 property 접근 불가
- 바로 function call 불가
- 사용 전 Type Narrowing 필요
- Type Guard와 함께 사용
- 외부 API, localStorage, JSON parse 결과에 유용

---

### [실무]

외부 입력 검증 예:

```typescript
type User = {
  id: number;
  name: string;
};

function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    "name" in value
  );
}

function parseUser(value: unknown): User | null {
  if (isUser(value)) {
    return value;
  }

  return null;
}
```

실무 기준:

- 검증 전 외부 데이터는 unknown 사용 가능
- Type Guard로 구조 확인
- 검증 후 구체적 Type으로 사용
- any보다 unknown 우선
- Runtime Validation Tool과 함께 사용 가능

---

### [FAQ]

Q. unknown은 any랑 뭐가 달라?
A. unknown은 사용 전 Type 검사가 필요하지만 any는 검사 없이 사용할 수 있다.

Q. unknown은 언제 써?
A. 외부 API 응답, localStorage, JSON parse, 사용자 입력처럼 Type을 확신할 수 없는 값에 사용한다.

Q. unknown 값을 어떻게 사용해?
A. typeof, in operator, Type Guard 등으로 Type Narrowing 후 사용한다.

---

## 5.3 Void Type

### [개념]

`void` Type은 함수가 의미 있는 반환값을 반환하지 않음을 표현하는 Type이다.

```typescript
function logMessage(message: string): void {
  console.log(message);
}
```

`void`는 Event Handler, Logging Function, Side Effect Function에서 자주 사용된다.

---

### [핵심]

`void` 사용 영역:

- event handler
- console logging
- state update function
- callback return
- side effect function
- command function

주의:

- void는 반환값 없음 의미
- undefined와 완전히 같은 사용 목적이 아님
- async function의 void는 `Promise<void>`로 표현
- callback props에서 자주 사용

---

### [실무]

Event Handler 예:

```typescript
type ClickHandler = (festivalId: number) => void;

const handleClick: ClickHandler = (festivalId) => {
  console.log(festivalId);
};
```

Async void 예:

```typescript
async function saveLog(message: string): Promise<void> {
  await fetch("/api/logs", {
    method: "POST",
    body: JSON.stringify({ message }),
  });
}
```

실무 기준:

- 반환값 없는 함수는 `void`
- async 반환값 없는 함수는 `Promise<void>`
- callback prop은 `() => void` 형태 자주 사용
- 실제 반환값이 필요한 함수에 void 사용 금지

---

### [FAQ]

Q. void는 언제 써?
A. 반환값이 없는 함수의 Return Type에 사용한다.

Q. async 함수에서 반환값이 없으면 void야?
A. async 함수는 항상 Promise를 반환하므로 `Promise<void>`로 쓴다.

Q. Event Handler Return Type은 보통 뭐야?
A. 대부분 `void`를 사용한다.

---

## 5.4 Never Type

### [개념]

`never` Type은 절대 발생할 수 없는 값 또는 정상적으로 반환되지 않는 함수의 Type이다.

```typescript
function throwError(message: string): never {
  throw new Error(message);
}
```

`never`는 Exhaustive Check에서 유용하다.

---

### [핵심]

`never` 사용 영역:

- 항상 throw하는 함수
- 무한 루프 함수
- 도달 불가능한 코드
- exhaustive check
- discriminated union 검증

주의:

- Foundation에서는 기본 개념 중심
- 일반 변수 Type으로 직접 사용할 일은 적음
- 상태 분기 누락 검토에 유용

---

### [실무]

Exhaustive Check 예:

```typescript
type RequestStatus = "loading" | "success" | "error";

function getStatusMessage(status: RequestStatus): string {
  switch (status) {
    case "loading":
      return "Loading...";
    case "success":
      return "Success";
    case "error":
      return "Error";
    default: {
      const exhaustiveCheck: never = status;
      return exhaustiveCheck;
    }
  }
}
```

효과:

- RequestStatus에 새 값이 추가되면 switch 누락을 TypeScript가 감지할 수 있다.
- Review Agent가 상태 분기 누락을 확인하기 좋다.

---

### [FAQ]

Q. never는 언제 써?
A. 절대 반환되지 않는 함수나 도달할 수 없는 상태를 표현할 때 사용한다.

Q. never를 자주 써?
A. Foundation 수준에서는 자주 쓰지 않지만 상태 분기 Exhaustive Check에서 유용하다.

Q. never와 void는 같아?
A. 아니다. void는 반환값이 없다는 뜻이고 never는 정상적으로 반환될 수 없다는 뜻이다.

---

# 6. Primitive Wrapper Type Caution

## 6.1 string vs String

### [개념]

`string`은 Primitive Type이고 `String`은 객체 Wrapper Type이다.

TypeScript 실무에서는 `String`, `Number`, `Boolean`보다 `string`, `number`, `boolean`을 사용한다.

```typescript
const title: string = "Festival";
```

---

### [핵심]

권장:

- `string`
- `number`
- `boolean`

지양:

- `String`
- `Number`
- `Boolean`

이유:

- Primitive Type이 일반 값에 적합
- Wrapper Type은 객체 타입
- 예상치 못한 Type 혼선 가능
- TypeScript 공식 스타일에서도 primitive type 권장

---

### [실무]

나쁜 예:

```typescript
const title: String = "Festival";
const count: Number = 10;
const active: Boolean = true;
```

좋은 예:

```typescript
const title: string = "Festival";
const count: number = 10;
const active: boolean = true;
```

Review 기준:

- `String`, `Number`, `Boolean` 사용 여부 확인
- API Type에서 Wrapper Type 사용 금지
- Props Type에서 Wrapper Type 사용 금지
- State Type에서 Wrapper Type 사용 금지

---

### [FAQ]

Q. string과 String 차이는?
A. string은 Primitive Type이고 String은 객체 Wrapper Type이다. 실무에서는 string을 사용한다.

Q. Number와 number 중 뭐를 써?
A. number를 사용한다.

Q. Boolean과 boolean 중 뭐를 써?
A. boolean을 사용한다.

---

# 7. Basic Type Common Mistakes

## 7.1 Common Mistakes

### [개념]

Basic Type 실수는 Primitive Type, null / undefined, Array Type, any / unknown을 잘못 구분할 때 발생한다.

이 문제는 API Type, Props Type, State Type 전체로 확산되기 쉽다.

---

### [핵심]

자주 발생하는 실수:

- `String`, `Number`, `Boolean` 사용
- API nullable field를 `string`으로 단정
- input value 숫자를 `number`로 단정
- 날짜 string을 `Date`로 단정
- 빈 배열 Type 미정의
- `any[]`로 목록 처리
- `unknown` 없이 외부 데이터 바로 사용
- `as`로 Runtime 변환을 대신함
- `void`와 `undefined` 혼동
- `never`를 일반 반환값 없음으로 오해
- null과 undefined 혼동
- Optional과 Nullable 혼동

---

### [실무]

나쁜 예:

```typescript
type Festival = {
  festivalId: Number;
  title: String;
  imageUrl: string;
  eventStartDate: Date;
};
```

문제:

- `Number`, `String` Wrapper Type 사용
- `imageUrl` nullable 가능성 미반영
- JSON 날짜를 Date로 단정

개선:

```typescript
type Festival = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  eventStartDate: string;
};
```

숫자 변환 예:

```typescript
function parseRating(value: string): number {
  return Number(value);
}
```

실무 기준:

- 실제 API Response Body 확인
- Backend DTO와 Type 정합성 유지
- nullable 여부 확인
- Runtime 변환은 명시적 함수로 처리
- any보다 구체적 Type 또는 unknown 사용

---

### [FAQ]

Q. Basic Type에서 가장 흔한 실수는?
A. Wrapper Type 사용, nullable 누락, 빈 배열 Type 누락, any 남용, 날짜 값을 Date로 단정하는 것이다.

Q. API 타입은 어떻게 검수해?
A. 실제 Response Body와 Backend DTO를 확인하고 null, string date, number field를 Type에 정확히 반영한다.

Q. Type Assertion으로 Basic Type 오류를 해결해도 돼?
A. 권장하지 않는다. 실제 값 구조와 Runtime 변환 필요 여부를 먼저 확인해야 한다.

---

# 8. Review Checklist

## 8.1 Part03 Checklist

### [개념]

TypeScript Foundation Part03 검수는 Primitive Type, null / undefined, Array Type, Tuple Type, Special Type의 실무 적용 기준을 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] Primitive Type 정의가 포함되었는가?
- [ ] string / number / boolean 설명이 포함되었는가?
- [ ] null / undefined 차이가 포함되었는가?
- [ ] Optional과 Nullable 구분이 포함되었는가?
- [ ] Array Type 작성 방식이 포함되었는가?
- [ ] Empty Array Type 주의가 포함되었는가?
- [ ] Readonly Array 설명이 포함되었는가?
- [ ] Tuple Type 설명이 포함되었는가?
- [ ] Tuple vs Array 비교가 포함되었는가?
- [ ] any 위험성이 포함되었는가?
- [ ] unknown 사용 기준이 포함되었는가?
- [ ] void / never 설명이 포함되었는가?
- [ ] string vs String 주의가 포함되었는가?
- [ ] API Response Type 예제가 포함되었는가?
- [ ] React State 초기값과 연결되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Required Section Check
→ Primitive Type Check
→ Null Undefined Check
→ Array Tuple Check
→ Special Type Check
→ API Type Example Check
→ Common Mistake Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

Part03은 이후 Object Type, Union Type, Function Type, API Response Type 문서의 기반이다.

---

### [FAQ]

Q. Part03에서 가장 중요한 검수 기준은?
A. Basic Type을 API Response, React State, Props, Runtime 변환과 연결해 설명했는지 확인하는 것이다.

Q. Part03이 이후 문서와 어떻게 연결돼?
A. Object Type, Union Type, Function Type, API Type, React Props Type의 기본 Type 재료가 된다.

---

# Retrieval Queries

### [FAQ]

Q. Primitive Type이 뭐야?
A. string, number, boolean, null, undefined처럼 JavaScript 기본 값에 대응하는 TypeScript Type이다.

Q. TypeScript Basic Type에는 뭐가 있어?
A. string, number, boolean, null, undefined, symbol, bigint, array, tuple, any, unknown, void, never가 있다.

Q. string과 String 차이는?
A. string은 Primitive Type이고 String은 객체 Wrapper Type이다. 실무에서는 string을 사용한다.

Q. number와 Number 차이는?
A. number는 Primitive Type이고 Number는 객체 Wrapper Type이다. 실무에서는 number를 사용한다.

Q. boolean과 Boolean 차이는?
A. boolean은 Primitive Type이고 Boolean은 객체 Wrapper Type이다. 실무에서는 boolean을 사용한다.

Q. number는 정수와 실수를 구분해?
A. 아니다. JavaScript number는 정수와 실수를 모두 표현한다.

Q. input에서 받은 숫자는 number야?
A. 대부분 input value는 string이다. 숫자로 쓰려면 Number 같은 Runtime 변환이 필요하다.

Q. JSON 날짜는 Date Type으로 받아?
A. 대부분 JSON 응답에서는 string으로 받고 필요하면 Frontend에서 Date로 변환한다.

Q. null은 언제 써?
A. 의도적으로 값이 없음을 표현해야 할 때 사용한다.

Q. undefined는 언제 생겨?
A. 값이 할당되지 않았거나 optional property / parameter가 생략되었을 때 생긴다.

Q. null과 undefined는 같아?
A. 아니다. null은 의도적 값 없음이고 undefined는 미할당 또는 생략을 의미한다.

Q. Optional과 Nullable 차이는?
A. Optional은 property가 없거나 undefined일 수 있다는 뜻이고 Nullable은 값이 null일 수 있다는 뜻이다.

Q. `name?: string`과 `name: string | null`은 같아?
A. 아니다. optional은 property 누락 가능성이고 nullable은 값이 null일 가능성이다.

Q. null 가능 값은 어떻게 Type으로 써?
A. `User | null`, `string | null`, `number | null`처럼 Union Type으로 쓴다.

Q. Object is possibly null 오류는 왜 나?
A. 값이 null일 수 있는데 null check 없이 사용하려고 해서 발생한다.

Q. undefined 가능 값은 어떻게 처리해?
A. 기본값 처리, optional chaining, nullish coalescing을 사용한다.

Q. Array Type은 어떻게 써?
A. `string[]`, `number[]`, `Festival[]` 또는 `Array<T>` 형태로 작성한다.

Q. string[]와 Array<string> 중 뭐가 좋아?
A. 둘 다 가능하다. 일반 배열은 string[] 형태가 간결하고 자주 사용된다.

Q. 객체 배열 Type은 어떻게 정의해?
A. 객체 Type을 type 또는 interface로 정의한 뒤 `Festival[]`처럼 사용한다.

Q. 빈 배열에는 왜 Type을 써야 해?
A. TypeScript가 배열에 어떤 element가 들어갈지 정확히 추론하기 어렵기 때문이다.

Q. 빈 배열을 any[]로 두면 안 돼?
A. 가능은 하지만 Type Safety가 무너지므로 구체적 Type을 사용하는 것이 좋다.

Q. React State 빈 배열도 Type이 필요해?
A. 쓰는 것이 좋다. 초기값만으로 element Type을 알기 어렵기 때문이다.

Q. readonly array는 Runtime에서도 변경을 막아?
A. 아니다. TypeScript Type Check 단계에서 직접 변경을 제한한다.

Q. readonly array는 언제 써?
A. 함수 입력 배열을 보호하거나 React State 원본 변경을 막고 싶을 때 유용하다.

Q. sort는 원본 배열을 바꿔?
A. 그렇다. 원본 변경을 피하려면 복사 후 sort를 사용한다.

Q. Tuple은 언제 써?
A. 좌표나 쌍 데이터처럼 길이와 위치 의미가 명확한 짧은 데이터에 사용한다.

Q. Array와 Tuple 차이는?
A. Array는 길이가 가변인 목록이고 Tuple은 길이와 위치별 Type이 고정된 배열이다.

Q. 좌표는 Tuple과 Object 중 뭐가 좋아?
A. 짧은 내부 데이터는 Tuple도 가능하지만 API나 협업 코드에서는 Object가 더 명확할 수 있다.

Q. any는 왜 피해야 해?
A. TypeScript의 Type Check를 우회해서 오류를 미리 잡기 어렵게 만든다.

Q. any를 아예 쓰면 안 돼?
A. 임시 Migration에서는 제한적으로 사용할 수 있지만 최종 코드에서는 제거하는 것이 좋다.

Q. any 대신 뭘 써?
A. 구체적 Type을 정의하거나 Type을 모르는 외부 입력은 unknown을 사용한다.

Q. unknown은 any랑 뭐가 달라?
A. unknown은 사용 전 Type 검사가 필요하지만 any는 검사 없이 사용할 수 있다.

Q. unknown은 언제 써?
A. 외부 API 응답, localStorage, JSON parse, 사용자 입력처럼 Type을 확신할 수 없는 값에 사용한다.

Q. unknown 값을 어떻게 사용해?
A. typeof, in operator, Type Guard 등으로 Type Narrowing 후 사용한다.

Q. void는 언제 써?
A. 반환값이 없는 함수의 Return Type에 사용한다.

Q. async 함수에서 반환값이 없으면 void야?
A. async 함수는 항상 Promise를 반환하므로 `Promise<void>`로 쓴다.

Q. Event Handler Return Type은 보통 뭐야?
A. 대부분 `void`를 사용한다.

Q. never는 언제 써?
A. 절대 반환되지 않는 함수나 도달할 수 없는 상태를 표현할 때 사용한다.

Q. never와 void는 같아?
A. 아니다. void는 반환값이 없다는 뜻이고 never는 정상적으로 반환될 수 없다는 뜻이다.

Q. Basic Type에서 가장 흔한 실수는?
A. Wrapper Type 사용, nullable 누락, 빈 배열 Type 누락, any 남용, 날짜 값을 Date로 단정하는 것이다.

Q. API 타입은 어떻게 검수해?
A. 실제 Response Body와 Backend DTO를 확인하고 null, string date, number field를 Type에 정확히 반영한다.

Q. TypeScript Part03의 핵심은 뭐야?
A. Basic Type을 API Response, React State, Props, Runtime 변환과 연결해 정확히 사용하는 것이다.

Q. TypeScript Part03 다음 문서는 뭐가 좋아?
A. Object Type, Optional Property, Readonly Property, Index Signature, Excess Property Check 문서가 적합하다.
