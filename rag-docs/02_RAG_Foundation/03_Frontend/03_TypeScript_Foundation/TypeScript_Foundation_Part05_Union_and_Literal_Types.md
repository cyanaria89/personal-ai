# TypeScript Foundation Part05 - Union Type and Literal Type

---

# 1. Union Type

## 1.1 Union Type Definition

### [개념]

Union Type은 값이 여러 Type 중 하나일 수 있음을 표현하는 TypeScript Type이다.

```typescript
type Id = number | string;
```

Union Type은 API nullable field, 상태 값, 선택 값, 여러 형태의 parameter를 표현할 때 사용한다.

```typescript
type FestivalImageUrl = string | null;
type RequestStatus = "idle" | "loading" | "success" | "error";
```

Union Type은 값의 가능성을 넓히지만, 사용할 때는 Type Narrowing으로 안전하게 좁혀야 한다.

---

### [핵심]

Union Type 핵심:

- 여러 Type 중 하나 허용
- `|` 연산자로 작성
- nullable value 표현
- 상태 값 표현
- literal union 표현
- parameter flexibility 제공
- 사용 전 Type Narrowing 필요
- 너무 넓은 union은 코드 복잡도 증가

주요 사용 영역:

- `string | null`
- `number | null`
- `User | null`
- `string | number`
- `"idle" | "loading" | "success" | "error"`
- `"ROLE_USER" | "ROLE_ADMIN"`

---

### [실무]

API nullable field 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  averageRating: number | null;
};
```

선택된 값 State 예:

```typescript
let selectedFestivalId: number | null = null;
```

parameter union 예:

```typescript
function formatId(id: number | string): string {
  return String(id);
}
```

실무 기준:

- API에서 null 가능하면 `T | null`로 표현
- 상태 값은 literal union으로 제한
- Union Type 값은 사용 전 Narrowing 고려
- `string | number | boolean | object`처럼 너무 넓은 union 지양
- 복잡한 union object는 Discriminated Union 고려

---

### [FAQ]

Q. Union Type이 뭐야?
A. 값이 여러 Type 중 하나일 수 있음을 표현하는 TypeScript Type이다.

Q. Union Type은 어떻게 써?
A. `string | null`, `number | string`처럼 `|` 연산자로 Type을 연결한다.

Q. Union Type은 언제 써?
A. 값이 여러 Type 또는 여러 상태 중 하나일 수 있을 때 사용한다.

Q. Union Type을 쓰면 바로 모든 property를 사용할 수 있어?
A. 아니다. TypeScript가 안전하다고 판단할 수 있도록 Type Narrowing이 필요하다.

---

## 1.2 Nullable Union

### [개념]

Nullable Union은 값이 특정 Type이거나 `null`일 수 있음을 표현하는 Union Type이다.

```typescript
type ProfileImageUrl = string | null;
```

Nullable Union은 API Response, React State, 선택 값, optional relation에서 자주 사용된다.

---

### [핵심]

Nullable Union 사용 영역:

- API nullable field
- selected item
- current user
- profile image
- average rating
- deletedAt
- relation response
- initial state

주의:

- `T | null`은 Optional Property와 다름
- 사용 전 null check 필요
- `as T`로 null 제거 금지
- Backend Response Body 기준으로 nullable 여부 판단
- null 가능성을 Type에 정확히 반영

---

### [실무]

API Response 예:

```typescript
type UserResponse = {
  userId: number;
  nickname: string;
  profileImageUrl: string | null;
};
```

fallback 처리:

```typescript
function getProfileImageUrl(profileImageUrl: string | null): string {
  return profileImageUrl ?? "/default-profile.png";
}
```

State 예:

```typescript
type User = {
  userId: number;
  nickname: string;
};

let currentUser: User | null = null;
```

실무 기준:

- null 가능 값은 Type에 반영
- UI 출력 전 기본값 처리
- Optional Chaining과 Nullish Coalescing 활용
- API Response Type과 Backend DTO 정합성 유지

---

### [FAQ]

Q. `string | null`은 무슨 뜻이야?
A. 값이 string이거나 null일 수 있다는 뜻이다.

Q. null 가능 값은 어떻게 사용해?
A. null check, optional chaining, nullish coalescing으로 처리한다.

Q. `T | null`과 `T | undefined`는 같아?
A. 아니다. null은 의도적 값 없음이고 undefined는 미할당 또는 생략 가능성을 의미한다.

---

## 1.3 Union Type Narrowing Need

### [개념]

Union Type은 여러 Type 가능성을 허용하기 때문에 실제 사용 시 Type을 좁히는 과정이 필요하다.

Type Narrowing은 조건문을 통해 더 구체적인 Type으로 좁히는 방식이다.

```typescript
function formatValue(value: string | number): string {
  if (typeof value === "number") {
    return value.toLocaleString();
  }

  return value.toUpperCase();
}
```

---

### [핵심]

Narrowing이 필요한 이유:

- Union Type에는 공통 property만 안전하게 접근 가능
- Type별 method가 다를 수 있음
- null 가능 값은 직접 접근 불가
- unknown 값은 검증 전 사용 불가
- 상태별 데이터 구조가 다를 수 있음

주요 Narrowing 방식:

- `typeof`
- `instanceof`
- `in`
- equality check
- null check
- discriminant property check
- custom type guard

---

### [실무]

잘못된 예:

```typescript
function getLength(value: string | number): number {
  return value.length;
}
```

문제:

- number에는 `length` property가 없다.

개선:

```typescript
function getLength(value: string | number): number {
  if (typeof value === "string") {
    return value.length;
  }

  return value.toString().length;
}
```

nullable 처리:

```typescript
function getTitle(title: string | null): string {
  return title ?? "제목 없음";
}
```

실무 기준:

- Union Type은 사용 위치에서 안전하게 분기
- Type Assertion보다 Narrowing 우선
- null 가능 값은 fallback 처리
- 복잡한 union object는 Discriminated Union 사용

---

### [FAQ]

Q. Union Type에는 왜 Narrowing이 필요해?
A. 값이 여러 Type 중 하나일 수 있으므로 Type별 안전한 사용을 위해 Type을 좁혀야 한다.

Q. `string | number`에서 string method를 바로 쓸 수 있어?
A. 아니다. 먼저 `typeof value === "string"` 같은 Narrowing이 필요하다.

Q. null 가능 값은 어떻게 Narrowing해?
A. `value !== null`, optional chaining, nullish coalescing을 사용한다.

---

# 2. Literal Type

## 2.1 Literal Type Definition

### [개념]

Literal Type은 특정 값만 허용하는 TypeScript Type이다.

```typescript
type Theme = "light" | "dark";
type UserRole = "ROLE_USER" | "ROLE_ADMIN";
```

Literal Type은 단순 `string`보다 허용 가능한 값을 좁혀 오타와 잘못된 상태 값을 방지한다.

---

### [핵심]

Literal Type 종류:

- string literal type
- number literal type
- boolean literal type
- literal union
- status type
- role type
- theme type
- route type

효과:

- 허용 값 제한
- 자동완성 강화
- 오타 방지
- 조건 분기 안정성 향상
- 상태 모델 명확화

---

### [실무]

Role Type 예:

```typescript
type UserRole = "ROLE_USER" | "ROLE_ADMIN";

function canAccessAdmin(role: UserRole): boolean {
  return role === "ROLE_ADMIN";
}
```

Theme Type 예:

```typescript
type Theme = "light" | "dark";

let currentTheme: Theme = "light";
```

Status Type 예:

```typescript
type RequestStatus = "idle" | "loading" | "success" | "error";
```

실무 기준:

- 제한 가능한 문자열은 literal union 고려
- Role, Status, Theme, Route는 literal type에 적합
- 단순 string보다 안전한 상태 모델링 가능
- Backend enum 응답과 Frontend literal union 정합성 유지

---

### [FAQ]

Q. Literal Type이 뭐야?
A. 특정 값만 허용하는 TypeScript Type이다.

Q. Literal Type은 왜 써?
A. 허용 가능한 문자열이나 숫자 값을 제한해 오타와 잘못된 상태 값을 줄이기 위해 사용한다.

Q. string 대신 literal union을 쓰는 이유는?
A. 모든 문자열이 아니라 정해진 문자열만 허용해 Type Safety와 자동완성을 높이기 위해서다.

---

## 2.2 String Literal Union

### [개념]

String Literal Union은 여러 문자열 literal을 Union Type으로 묶어 허용 가능한 문자열 값을 제한하는 방식이다.

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";
```

Frontend 상태, 권한, 필터, 정렬 조건, 화면 모드에서 자주 사용된다.

---

### [핵심]

String Literal Union 사용 영역:

- async status
- user role
- theme mode
- sort option
- filter type
- tab key
- modal type
- route name
- notification type

장점:

- 문자열 오타 방지
- 자동완성 제공
- switch 분기 안정성
- 잘못된 상태 값 방지
- enum보다 가벼운 상태 표현 가능

---

### [실무]

비동기 상태 예:

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";

function getStatusMessage(status: AsyncStatus): string {
  switch (status) {
    case "idle":
      return "대기";
    case "loading":
      return "로딩 중";
    case "success":
      return "성공";
    case "error":
      return "오류";
  }
}
```

정렬 옵션 예:

```typescript
type FestivalSortOption = "latest" | "popular" | "rating";

function createSortQuery(sort: FestivalSortOption): string {
  return `sort=${sort}`;
}
```

실무 기준:

- 상태 문자열은 string보다 literal union 권장
- API enum string과 동일하게 맞춤
- UI tab key, modal key에 유용
- 허용 값이 많아지면 별도 Type으로 분리

---

### [FAQ]

Q. String Literal Union은 언제 써?
A. 정해진 문자열 값만 허용해야 하는 상태, 권한, 모드, 정렬 조건에 사용한다.

Q. 상태 값을 그냥 string으로 두면 안 돼?
A. 가능하지만 오타나 잘못된 상태 값이 들어갈 수 있어 literal union이 더 안전하다.

Q. Backend enum 값도 literal union으로 표현해?
A. 가능하다. Backend가 문자열 enum을 내려준다면 Frontend에서 literal union으로 맞추는 것이 좋다.

---

## 2.3 Number and Boolean Literal

### [개념]

Number Literal Type은 특정 숫자 값만 허용하고 Boolean Literal Type은 `true` 또는 `false` 특정 값만 허용한다.

```typescript
type Rating = 1 | 2 | 3 | 4 | 5;
type AlwaysTrue = true;
```

Foundation 실무에서는 String Literal Union보다 사용 빈도는 낮지만 제한된 숫자 값 표현에 유용하다.

---

### [핵심]

Number Literal 사용 영역:

- rating score
- step number
- page size option
- priority level
- tab index

Boolean Literal 사용 영역:

- discriminated union
- fixed option
- type-level flag
- strict config value

주의:

- 너무 많은 숫자 범위는 literal union으로 관리하기 어려움
- validation은 Type만으로 대체 불가
- API 입력값은 Runtime Validation 필요

---

### [실무]

Rating 예:

```typescript
type Rating = 1 | 2 | 3 | 4 | 5;

type ReviewCreateRequest = {
  festivalId: number;
  rating: Rating;
  content: string;
};
```

Page Size 예:

```typescript
type PageSize = 10 | 20 | 50;

function createPageSizeQuery(size: PageSize): string {
  return `size=${size}`;
}
```

주의:

```typescript
const rating = Number(inputValue) as Rating;
```

문제:

- Type Assertion은 Runtime Validation이 아니다.
- 실제 값이 7이어도 TypeScript 검사만 우회할 수 있다.

개선 방향:

```typescript
function isRating(value: number): value is Rating {
  return value >= 1 && value <= 5 && Number.isInteger(value);
}
```

---

### [FAQ]

Q. Number Literal Type은 언제 써?
A. 별점 1~5, page size option처럼 허용 숫자가 제한적일 때 사용할 수 있다.

Q. 숫자 범위 검증을 TypeScript Type만으로 할 수 있어?
A. 완전히는 어렵다. 외부 입력은 Runtime Validation이 필요하다.

Q. Boolean Literal Type은 자주 써?
A. Foundation 수준에서는 자주 쓰지 않지만 Discriminated Union이나 고정 옵션에서 사용할 수 있다.

---

# 3. Status Type Modeling

## 3.1 Async Status Type

### [개념]

Async Status Type은 비동기 요청 상태를 literal union으로 표현하는 방식이다.

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";
```

Boolean flag 여러 개보다 상태 전이를 명확하게 표현할 수 있다.

---

### [핵심]

Async Status 주요 값:

- `idle`
- `loading`
- `success`
- `error`

장점:

- 상태 값 제한
- 조건 분기 명확
- 잘못된 상태 조합 방지
- UI 상태 모델링 용이
- Loading / Error / Success 처리 일관화

---

### [실무]

나쁜 예:

```typescript
type RequestState = {
  isLoading: boolean;
  isSuccess: boolean;
  isError: boolean;
};
```

문제:

- `isLoading: true`, `isSuccess: true` 같은 모순 상태 가능

개선:

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";

type RequestState = {
  status: AsyncStatus;
  errorMessage: string | null;
};
```

사용 예:

```typescript
function canSubmit(status: AsyncStatus): boolean {
  return status !== "loading";
}
```

실무 기준:

- 단순 loading 여부만 필요하면 boolean 가능
- 요청 상태 단계가 3개 이상이면 literal union 권장
- 상태와 데이터 구조가 함께 달라지면 Discriminated Union 고려
- errorMessage는 `string | null`로 관리 가능

---

### [FAQ]

Q. Async Status Type은 뭐야?
A. idle, loading, success, error 같은 비동기 요청 상태를 literal union으로 표현한 Type이다.

Q. loading은 boolean으로 충분하지 않아?
A. 단순 loading 여부만 필요하면 충분하다. 성공, 실패, 대기 상태까지 표현하면 literal union이 더 명확하다.

Q. boolean flag 여러 개가 왜 위험해?
A. 동시에 true가 되는 모순 상태가 생길 수 있기 때문이다.

---

## 3.2 Role Type

### [개념]

Role Type은 사용자 권한 값을 literal union으로 제한하는 Type이다.

```typescript
type UserRole = "ROLE_USER" | "ROLE_ADMIN";
```

Role Type은 Frontend 권한 분기, 메뉴 노출, 관리자 페이지 접근 조건에서 사용된다.

---

### [핵심]

Role Type 사용 영역:

- authorization UI
- admin menu
- protected route
- button visibility
- feature access
- user profile response

주의:

- Frontend Role Type은 보안 자체가 아님
- 실제 권한 검사는 Backend에서 수행
- Backend Role Naming과 정합성 유지
- `ROLE_USER`, `ROLE_ADMIN`처럼 용어 통일

---

### [실무]

Role Type 예:

```typescript
type UserRole = "ROLE_USER" | "ROLE_ADMIN";

type LoginUserResponse = {
  userId: number;
  nickname: string;
  role: UserRole;
};
```

권한 분기 예:

```typescript
function canAccessAdmin(role: UserRole): boolean {
  return role === "ROLE_ADMIN";
}
```

주의:

```typescript
function canAccessAdmin(role: string): boolean {
  return role === "ADMIN";
}
```

문제:

- Backend가 `ROLE_ADMIN`을 사용한다면 naming 불일치
- string 전체를 허용해 오타 방지 불가

실무 기준:

- Backend Security Role Naming과 일치
- Frontend UI 제어에는 Role Type 활용
- Backend API 권한 검사를 대체하지 않음
- Role 값은 literal union으로 제한

---

### [FAQ]

Q. Role Type은 왜 literal union으로 정의해?
A. 허용 가능한 권한 문자열을 제한해 오타와 잘못된 권한 값을 줄이기 위해서다.

Q. Frontend에서 Role 체크하면 보안이 되는 거야?
A. 아니다. Frontend Role 체크는 UI 제어용이고 실제 보안 검사는 Backend에서 해야 한다.

Q. ROLE_USER와 USER를 섞어 써도 돼?
A. 권장하지 않는다. Backend와 Frontend에서 Role Naming을 통일해야 한다.

---

## 3.3 Filter and Sort Type

### [개념]

Filter Type과 Sort Type은 화면에서 사용하는 필터 조건, 정렬 조건, 탭 상태를 literal union으로 제한하는 Type이다.

```typescript
type FestivalSortOption = "latest" | "popular" | "rating";
```

잘못된 필터 값이나 정렬 값을 사전에 방지할 수 있다.

---

### [핵심]

사용 영역:

- sort option
- filter type
- tab key
- category key
- theme key
- search mode
- display mode

장점:

- Query 생성 안정성 향상
- UI 상태 값 제한
- API parameter 오타 방지
- 자동완성 지원
- 조건 분기 명확화

---

### [실무]

Sort Type 예:

```typescript
type FestivalSortOption = "latest" | "popular" | "rating";

type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  sort?: FestivalSortOption;
};
```

Tab Type 예:

```typescript
type MyPageTab = "profile" | "favorites" | "reviews";

function getTabTitle(tab: MyPageTab): string {
  switch (tab) {
    case "profile":
      return "프로필";
    case "favorites":
      return "찜 목록";
    case "reviews":
      return "리뷰";
  }
}
```

실무 기준:

- 정해진 UI 상태 값은 literal union 사용
- API Query Parameter 허용 값과 정합성 유지
- URL Query에서 들어온 값은 Runtime Validation 필요
- 사용자 입력 string을 바로 literal union으로 단정하지 않음

---

### [FAQ]

Q. Sort Option도 Type으로 정의해?
A. 정의하는 것이 좋다. 정렬 조건 오타와 잘못된 Query Parameter를 줄일 수 있다.

Q. Tab 상태도 literal union으로 만들 수 있어?
A. 가능하다. 정해진 탭 key만 허용하게 만들 수 있다.

Q. URL Query에서 받은 sort 값을 바로 Sort Type으로 써도 돼?
A. 권장하지 않는다. URL Query는 Runtime Data이므로 허용 값 검증이 필요하다.

---

# 4. Enum vs Union

## 4.1 Enum Basics

### [개념]

Enum은 이름 있는 상수 집합을 정의하는 TypeScript 문법이다.

```typescript
enum RequestStatus {
  Idle = "idle",
  Loading = "loading",
  Success = "success",
  Error = "error",
}
```

Enum은 사용할 수 있지만 Foundation 수준의 Frontend 상태 값에는 string literal union이 더 간단한 경우가 많다.

---

### [핵심]

Enum 특징:

- 이름 있는 상수 집합
- Runtime Code로 남을 수 있음
- 자동완성 가능
- Backend enum과 개념적으로 연결 가능
- 설정에 따라 Bundle 영향 고려 필요

주의:

- 단순 상태 값에는 literal union이 더 가벼움
- enum 남용 지양
- string enum과 number enum 차이 주의
- Backend 응답 문자열과 값 정합성 필요

---

### [실무]

Enum 예:

```typescript
enum UserRole {
  User = "ROLE_USER",
  Admin = "ROLE_ADMIN",
}
```

Literal Union 대안:

```typescript
type UserRole = "ROLE_USER" | "ROLE_ADMIN";
```

실무 기준:

- 단순 Frontend 상태 값은 literal union 우선
- 외부 라이브러리나 기존 프로젝트 컨벤션이 enum이면 따름
- Backend enum 응답이 string이면 literal union으로 충분한 경우 많음
- enum 사용 시 Runtime Output과 Tree Shaking 영향 고려

---

### [FAQ]

Q. enum은 쓰면 안 돼?
A. 쓸 수 있다. 다만 단순 상태 값은 string literal union이 더 가볍고 직관적인 경우가 많다.

Q. enum과 union 중 뭐가 좋아?
A. 단순 문자열 상태는 union이 좋고, 프로젝트 컨벤션이나 런타임 상수가 필요하면 enum을 사용할 수 있다.

Q. Backend enum 응답은 Frontend에서 어떻게 표현해?
A. 문자열 응답이면 literal union으로 표현하는 방식이 간단하고 안전하다.

---

## 4.2 Union Type vs Enum

### [개념]

Union Type과 Enum은 모두 제한된 값을 표현할 수 있지만 목적과 Runtime 동작이 다르다.

```text
Union Type
→ Type Level 제한

Enum
→ Runtime Value로 남을 수 있는 상수 집합
```

---

### [핵심]

| 비교                | Literal Union | Enum         |
| ------------------- | ------------- | ------------ |
| Runtime 존재        | 없음          | 있음         |
| Bundle 영향         | 거의 없음     | 있을 수 있음 |
| 단순 상태 표현      | 적합          | 가능         |
| 자동완성            | 가능          | 가능         |
| 값 제한             | 가능          | 가능         |
| Backend 문자열 응답 | 적합          | 가능         |
| Runtime 상수 필요   | 제한적        | 적합         |

---

### [실무]

Union 권장 예:

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";
```

Enum 가능 예:

```typescript
enum NotificationType {
  Comment = "COMMENT",
  Like = "LIKE",
  System = "SYSTEM",
}
```

실무 기준:

- Foundation 문서에서는 literal union 우선 설명
- enum은 프로젝트 컨벤션이 있을 때 사용
- 상태 값, Role, Theme는 union으로 충분한 경우 많음
- Runtime 상수 객체가 필요하면 enum 또는 const object 검토

---

### [FAQ]

Q. Literal Union과 Enum의 가장 큰 차이는?
A. Literal Union은 Type Level 제한이고 Enum은 Runtime 값으로 남을 수 있다는 점이다.

Q. 상태 Type은 enum보다 union이 좋아?
A. 단순 상태 값은 union이 더 간단하고 가볍다.

Q. enum을 쓰면 Bundle에 영향이 있어?
A. 일반 enum은 Runtime Code로 남을 수 있어 영향이 있을 수 있다.

---

# 5. Discriminated Union

## 5.1 Discriminated Union Definition

### [개념]

Discriminated Union은 공통 구분 property를 기준으로 여러 객체 형태를 안전하게 구분하는 Type Pattern이다.

```typescript
type ApiState<T> =
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; message: string };
```

공통 property인 `status`를 기준으로 TypeScript가 객체 구조를 좁힐 수 있다.

---

### [핵심]

Discriminated Union 구성 요소:

- discriminant property
- literal value
- object union
- type narrowing
- state-specific data
- exhaustive check

적합한 상황:

- loading / success / error
- modal state
- form step state
- payment status
- notification variant
- message type

---

### [실무]

API 상태 예:

```typescript
type ApiState<T> =
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; message: string };

function getItemCount<T>(state: ApiState<T[]>): number {
  if (state.status === "success") {
    return state.data.length;
  }

  return 0;
}
```

효과:

- `status === "success"` 분기에서만 `data` 접근 가능
- `status === "error"` 분기에서만 `message` 접근 가능
- 상태별 데이터 구조가 명확해짐

실무 기준:

- 상태별 필요한 데이터가 다르면 Discriminated Union 사용
- 공통 구분 property 이름 통일
- `status`, `type`, `kind` 중 하나를 일관되게 사용
- UI 상태 모델링에 유용

---

### [FAQ]

Q. Discriminated Union이 뭐야?
A. 공통 구분 property를 기준으로 여러 객체 형태를 안전하게 구분하는 Type Pattern이다.

Q. Discriminated Union은 언제 써?
A. loading, success, error처럼 상태별 데이터 구조가 다를 때 사용하면 좋다.

Q. status property가 왜 중요해?
A. TypeScript가 status 값을 기준으로 안전하게 Type을 좁힐 수 있기 때문이다.

---

## 5.2 API State Modeling

### [개념]

API State Modeling은 비동기 요청의 상태와 데이터를 Discriminated Union으로 표현하는 방식이다.

```text
loading
→ data 없음

success
→ data 있음

error
→ error message 있음
```

상태별로 필요한 property를 다르게 정의할 수 있다.

---

### [핵심]

API State 구성:

- loading state
- success state
- error state
- data field
- message field
- status discriminant
- generic data type

장점:

- 모순 상태 방지
- 상태별 데이터 접근 안전
- UI 분기 명확
- Review Agent 검토 용이
- Boolean flag 대체 가능

---

### [실무]

나쁜 예:

```typescript
type BadApiState<T> = {
  loading: boolean;
  data: T | null;
  errorMessage: string | null;
};
```

문제:

- loading이 true인데 data가 존재할 수 있음
- data와 errorMessage가 동시에 존재할 수 있음
- 상태 조합이 모호함

개선:

```typescript
type ApiState<T> =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; message: string };
```

사용 예:

```typescript
function getStatusText<T>(state: ApiState<T>): string {
  switch (state.status) {
    case "idle":
      return "대기";
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

- 단순 요청은 AsyncStatus만 사용 가능
- data / error 구조가 중요하면 Discriminated Union 사용
- React State 모델링에 적합
- 상태별 field 접근 오류를 줄임

---

### [FAQ]

Q. API State를 Discriminated Union으로 만들면 뭐가 좋아?
A. 상태별로 필요한 데이터만 허용해 모순 상태와 잘못된 property 접근을 줄일 수 있다.

Q. loading boolean과 data null 조합보다 좋은 이유는?
A. 여러 boolean과 nullable field 조합은 모순 상태가 생길 수 있지만 Discriminated Union은 상태 구조를 제한한다.

Q. 모든 API 상태를 Discriminated Union으로 만들어야 해?
A. 아니다. 단순한 경우는 AsyncStatus로 충분하고 복잡한 상태에서 유용하다.

---

## 5.3 Exhaustive Check

### [개념]

Exhaustive Check는 Union Type의 모든 가능한 상태를 처리했는지 확인하는 검증 방식이다.

`never` Type을 사용하면 switch 분기 누락을 TypeScript가 감지할 수 있다.

```typescript
type RequestStatus = "loading" | "success" | "error";
```

---

### [핵심]

Exhaustive Check 목적:

- 상태 분기 누락 방지
- literal union 변경 감지
- Review 안정성 향상
- switch case 검증
- never type 활용

---

### [실무]

예:

```typescript
type RequestStatus = "loading" | "success" | "error";

function getStatusMessage(status: RequestStatus): string {
  switch (status) {
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

상태 추가 예:

```typescript
type RequestStatus = "idle" | "loading" | "success" | "error";
```

`idle`이 추가되면 기존 switch에서 default의 `never` 검사가 오류를 발생시킬 수 있다.

실무 기준:

- 중요한 상태 분기에는 exhaustive check 고려
- Discriminated Union switch에서 유용
- Review Agent는 switch case 누락 확인
- default에서 오류를 숨기지 않도록 주의

---

### [FAQ]

Q. Exhaustive Check가 뭐야?
A. Union Type의 모든 가능한 값을 분기에서 처리했는지 확인하는 방식이다.

Q. never를 왜 써?
A. 처리되지 않은 Union 값이 남아 있으면 never에 할당할 수 없어 오류를 발생시키기 위해 사용한다.

Q. 모든 switch에 Exhaustive Check를 넣어야 해?
A. 필수는 아니지만 중요한 상태 값이나 Discriminated Union 분기에는 유용하다.

---

# 6. Union Type and API Modeling

## 6.1 API Enum Response Type

### [개념]

API Enum Response Type은 Backend가 문자열 enum 값을 반환할 때 Frontend에서 literal union으로 표현하는 방식이다.

```typescript
type CertStatus = "PENDING" | "APPROVED" | "REJECTED";
```

Backend enum 값과 Frontend literal union 값은 정확히 일치해야 한다.

---

### [핵심]

API Enum Response 사용 영역:

- user role
- certification status
- post category
- notification type
- payment status
- donation status
- review status
- message type

주의:

- Backend enum naming 확인
- 대소문자 일치
- `ROLE_ADMIN` vs `ADMIN` 혼용 금지
- enum 값 추가 시 Frontend Type 업데이트
- 알 수 없는 값 방어 필요 가능

---

### [실무]

Backend enum 응답 예:

```typescript
type CertStatus = "PENDING" | "APPROVED" | "REJECTED";

type CertificationResponse = {
  certificationId: number;
  status: CertStatus;
  rejectReason: string | null;
};
```

UI Label Map 예:

```typescript
const certStatusLabel: Record<CertStatus, string> = {
  PENDING: "대기",
  APPROVED: "승인",
  REJECTED: "반려",
};
```

실무 기준:

- Backend enum value와 Frontend union value 일치
- 상태별 label은 `Record<Status, string>` 활용
- Backend enum 변경 시 Frontend Type과 label map 수정
- Runtime unknown value 처리 필요 시 fallback 고려

---

### [FAQ]

Q. Backend enum 응답은 Frontend에서 어떻게 Type으로 표현해?
A. 문자열 enum 응답은 literal union으로 표현할 수 있다.

Q. Backend enum 값이 추가되면 어떻게 해?
A. Frontend literal union, label map, switch 분기를 함께 업데이트해야 한다.

Q. ROLE_ADMIN과 ADMIN을 섞어 써도 돼?
A. 안 된다. Backend와 Frontend에서 권한 문자열 Naming을 통일해야 한다.

---

## 6.2 Error Code Union

### [개념]

Error Code Union은 API 오류 코드 값을 literal union으로 제한하는 Type이다.

```typescript
type ApiErrorCode =
  | "VALIDATION_ERROR"
  | "UNAUTHORIZED"
  | "FORBIDDEN"
  | "NOT_FOUND"
  | "SERVER_ERROR";
```

Error Code Union은 오류 메시지 처리, 사용자 안내, 분기 처리에 유용하다.

---

### [핵심]

Error Code Union 사용 영역:

- validation error
- auth error
- forbidden error
- not found error
- conflict error
- server error
- network fallback

장점:

- 오류 코드 오타 방지
- 오류별 메시지 매핑
- switch 분기 안정성
- API Error Response Type 강화

---

### [실무]

Error Response Type 예:

```typescript
type ApiErrorCode =
  | "VALIDATION_ERROR"
  | "UNAUTHORIZED"
  | "FORBIDDEN"
  | "NOT_FOUND"
  | "SERVER_ERROR";

type ApiErrorResponse = {
  success: false;
  code: ApiErrorCode;
  message: string;
  errors?: Record<string, string>;
};
```

Message Map 예:

```typescript
const errorMessageMap: Record<ApiErrorCode, string> = {
  VALIDATION_ERROR: "입력값을 확인해 주세요.",
  UNAUTHORIZED: "로그인이 필요합니다.",
  FORBIDDEN: "접근 권한이 없습니다.",
  NOT_FOUND: "요청한 데이터를 찾을 수 없습니다.",
  SERVER_ERROR: "서버 오류가 발생했습니다.",
};
```

실무 기준:

- Backend Error Code와 정합성 유지
- field validation errors는 `Record<string, string>` 사용 가능
- 알 수 없는 오류는 fallback message 제공
- 민감한 서버 오류를 그대로 노출하지 않음

---

### [FAQ]

Q. Error Code도 Union Type으로 정의해?
A. 정의하는 것이 좋다. 오류 코드 오타를 줄이고 메시지 매핑을 안정적으로 만들 수 있다.

Q. Error Response Type에는 뭐가 들어가?
A. success, code, message, field errors 같은 구조를 포함할 수 있다.

Q. 알 수 없는 오류 코드는 어떻게 처리해?
A. fallback message를 제공하고 필요하면 unknown code 방어 로직을 둔다.

---

# 7. Common Mistakes

## 7.1 Union and Literal Mistakes

### [개념]

Union Type과 Literal Type 실수는 허용 범위를 너무 넓게 잡거나, Runtime Data를 검증하지 않거나, Backend 값과 Naming이 불일치할 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- 상태 값을 단순 string으로 정의
- Role 값을 string으로 정의
- Backend enum 값과 Frontend union 불일치
- `ROLE_ADMIN` / `ADMIN` 혼용
- nullable field를 Union으로 표현하지 않음
- Union Type 사용 후 Narrowing 누락
- 너무 넓은 Union Type 사용
- enum과 union 기준 없이 혼용
- URL Query 값을 바로 literal union으로 단정
- Type Assertion으로 Runtime 값 검증 우회
- Discriminated Union의 구분 property 이름 불일치
- switch 분기 누락

---

### [실무]

나쁜 예:

```typescript
type UserResponse = {
  userId: number;
  role: string;
};

function canAccessAdmin(role: string): boolean {
  return role === "ADMIN";
}
```

문제:

- 모든 string을 role로 허용
- Backend가 `ROLE_ADMIN`을 사용하면 Naming 불일치
- 오타를 TypeScript가 잡을 수 없음

개선:

```typescript
type UserRole = "ROLE_USER" | "ROLE_ADMIN";

type UserResponse = {
  userId: number;
  role: UserRole;
};

function canAccessAdmin(role: UserRole): boolean {
  return role === "ROLE_ADMIN";
}
```

URL Query 방어 예:

```typescript
type FestivalSortOption = "latest" | "popular" | "rating";

function isFestivalSortOption(value: string): value is FestivalSortOption {
  return value === "latest" || value === "popular" || value === "rating";
}
```

실무 기준:

- 제한 가능한 문자열은 literal union 사용
- 외부 입력은 Runtime Validation 후 사용
- Backend enum naming과 일치
- 상태별 데이터 구조가 다르면 Discriminated Union 사용
- Type Assertion보다 Type Guard 우선

---

### [FAQ]

Q. Union Type에서 가장 흔한 실수는?
A. Type을 너무 넓게 잡거나 Narrowing 없이 Type별 property를 사용하는 것이다.

Q. Literal Type에서 가장 흔한 실수는?
A. Backend enum 값과 Frontend literal union 값이 불일치하는 것이다.

Q. URL Query 값을 바로 literal union으로 써도 돼?
A. 권장하지 않는다. URL Query는 Runtime Data이므로 허용 값인지 검증해야 한다.

---

# 8. Review Checklist

## 8.1 Part05 Checklist

### [개념]

TypeScript Foundation Part05 검수는 Union Type, Literal Type, Status Modeling, Enum 비교, Discriminated Union, API enum modeling 기준을 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] Union Type 정의가 포함되었는가?
- [ ] Nullable Union 설명이 포함되었는가?
- [ ] Union Type Narrowing 필요성이 포함되었는가?
- [ ] Literal Type 정의가 포함되었는가?
- [ ] String Literal Union 설명이 포함되었는가?
- [ ] Number Literal Type 설명이 포함되었는가?
- [ ] Async Status Type 모델링이 포함되었는가?
- [ ] Role Type 모델링이 포함되었는가?
- [ ] Filter / Sort Type 모델링이 포함되었는가?
- [ ] Enum 기본 설명이 포함되었는가?
- [ ] Union Type vs Enum 비교가 포함되었는가?
- [ ] Discriminated Union 설명이 포함되었는가?
- [ ] API State Modeling 예제가 포함되었는가?
- [ ] Exhaustive Check 설명이 포함되었는가?
- [ ] API Enum Response Type 예제가 포함되었는가?
- [ ] Error Code Union 예제가 포함되었는가?
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
→ Union Type Check
→ Literal Type Check
→ Status Modeling Check
→ Enum Comparison Check
→ Discriminated Union Check
→ API Enum Modeling Check
→ Common Mistake Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

Part05는 이후 Type Alias, Interface, Function Type, Type Narrowing, API Type 문서의 기반이다.

---

### [FAQ]

Q. Part05에서 가장 중요한 검수 기준은?
A. Union Type과 Literal Type을 API nullable field, 상태 값, Role, Backend enum과 정확히 연결했는지 확인하는 것이다.

Q. Part05가 이후 문서와 어떻게 연결돼?
A. Type Alias, Interface, Function Type, Type Narrowing, Discriminated Union, API Error Type의 기반이 된다.

---

# Retrieval Queries

### [FAQ]

Q. Union Type이 뭐야?
A. 값이 여러 Type 중 하나일 수 있음을 표현하는 TypeScript Type이다.

Q. Union Type은 어떻게 써?
A. `string | null`, `number | string`처럼 `|` 연산자로 Type을 연결한다.

Q. Union Type은 언제 써?
A. 값이 여러 Type 또는 여러 상태 중 하나일 수 있을 때 사용한다.

Q. Union Type을 쓰면 바로 모든 property를 사용할 수 있어?
A. 아니다. TypeScript가 안전하다고 판단할 수 있도록 Type Narrowing이 필요하다.

Q. `string | null`은 무슨 뜻이야?
A. 값이 string이거나 null일 수 있다는 뜻이다.

Q. null 가능 값은 어떻게 사용해?
A. null check, optional chaining, nullish coalescing으로 처리한다.

Q. `T | null`과 `T | undefined`는 같아?
A. 아니다. null은 의도적 값 없음이고 undefined는 미할당 또는 생략 가능성을 의미한다.

Q. Union Type에는 왜 Narrowing이 필요해?
A. 값이 여러 Type 중 하나일 수 있으므로 Type별 안전한 사용을 위해 Type을 좁혀야 한다.

Q. `string | number`에서 string method를 바로 쓸 수 있어?
A. 아니다. 먼저 `typeof value === "string"` 같은 Narrowing이 필요하다.

Q. Literal Type이 뭐야?
A. 특정 값만 허용하는 TypeScript Type이다.

Q. Literal Type은 왜 써?
A. 허용 가능한 문자열이나 숫자 값을 제한해 오타와 잘못된 상태 값을 줄이기 위해 사용한다.

Q. string 대신 literal union을 쓰는 이유는?
A. 모든 문자열이 아니라 정해진 문자열만 허용해 Type Safety와 자동완성을 높이기 위해서다.

Q. String Literal Union은 언제 써?
A. 정해진 문자열 값만 허용해야 하는 상태, 권한, 모드, 정렬 조건에 사용한다.

Q. 상태 값을 그냥 string으로 두면 안 돼?
A. 가능하지만 오타나 잘못된 상태 값이 들어갈 수 있어 literal union이 더 안전하다.

Q. Backend enum 값도 literal union으로 표현해?
A. 가능하다. Backend가 문자열 enum을 내려준다면 Frontend에서 literal union으로 맞추는 것이 좋다.

Q. Number Literal Type은 언제 써?
A. 별점 1~5, page size option처럼 허용 숫자가 제한적일 때 사용할 수 있다.

Q. 숫자 범위 검증을 TypeScript Type만으로 할 수 있어?
A. 완전히는 어렵다. 외부 입력은 Runtime Validation이 필요하다.

Q. Async Status Type은 뭐야?
A. idle, loading, success, error 같은 비동기 요청 상태를 literal union으로 표현한 Type이다.

Q. loading은 boolean으로 충분하지 않아?
A. 단순 loading 여부만 필요하면 충분하다. 성공, 실패, 대기 상태까지 표현하면 literal union이 더 명확하다.

Q. boolean flag 여러 개가 왜 위험해?
A. 동시에 true가 되는 모순 상태가 생길 수 있기 때문이다.

Q. Role Type은 왜 literal union으로 정의해?
A. 허용 가능한 권한 문자열을 제한해 오타와 잘못된 권한 값을 줄이기 위해서다.

Q. Frontend에서 Role 체크하면 보안이 되는 거야?
A. 아니다. Frontend Role 체크는 UI 제어용이고 실제 보안 검사는 Backend에서 해야 한다.

Q. ROLE_USER와 USER를 섞어 써도 돼?
A. 권장하지 않는다. Backend와 Frontend에서 Role Naming을 통일해야 한다.

Q. Sort Option도 Type으로 정의해?
A. 정의하는 것이 좋다. 정렬 조건 오타와 잘못된 Query Parameter를 줄일 수 있다.

Q. Tab 상태도 literal union으로 만들 수 있어?
A. 가능하다. 정해진 탭 key만 허용하게 만들 수 있다.

Q. URL Query에서 받은 sort 값을 바로 Sort Type으로 써도 돼?
A. 권장하지 않는다. URL Query는 Runtime Data이므로 허용 값 검증이 필요하다.

Q. enum은 쓰면 안 돼?
A. 쓸 수 있다. 다만 단순 상태 값은 string literal union이 더 가볍고 직관적인 경우가 많다.

Q. enum과 union 중 뭐가 좋아?
A. 단순 문자열 상태는 union이 좋고, 프로젝트 컨벤션이나 런타임 상수가 필요하면 enum을 사용할 수 있다.

Q. Literal Union과 Enum의 가장 큰 차이는?
A. Literal Union은 Type Level 제한이고 Enum은 Runtime 값으로 남을 수 있다는 점이다.

Q. 상태 Type은 enum보다 union이 좋아?
A. 단순 상태 값은 union이 더 간단하고 가볍다.

Q. enum을 쓰면 Bundle에 영향이 있어?
A. 일반 enum은 Runtime Code로 남을 수 있어 영향이 있을 수 있다.

Q. Discriminated Union이 뭐야?
A. 공통 구분 property를 기준으로 여러 객체 형태를 안전하게 구분하는 Type Pattern이다.

Q. Discriminated Union은 언제 써?
A. loading, success, error처럼 상태별 데이터 구조가 다를 때 사용하면 좋다.

Q. status property가 왜 중요해?
A. TypeScript가 status 값을 기준으로 안전하게 Type을 좁힐 수 있기 때문이다.

Q. API State를 Discriminated Union으로 만들면 뭐가 좋아?
A. 상태별로 필요한 데이터만 허용해 모순 상태와 잘못된 property 접근을 줄일 수 있다.

Q. loading boolean과 data null 조합보다 좋은 이유는?
A. 여러 boolean과 nullable field 조합은 모순 상태가 생길 수 있지만 Discriminated Union은 상태 구조를 제한한다.

Q. 모든 API 상태를 Discriminated Union으로 만들어야 해?
A. 아니다. 단순한 경우는 AsyncStatus로 충분하고 복잡한 상태에서 유용하다.

Q. Exhaustive Check가 뭐야?
A. Union Type의 모든 가능한 값을 분기에서 처리했는지 확인하는 방식이다.

Q. never를 왜 써?
A. 처리되지 않은 Union 값이 남아 있으면 never에 할당할 수 없어 오류를 발생시키기 위해 사용한다.

Q. Backend enum 응답은 Frontend에서 어떻게 Type으로 표현해?
A. 문자열 enum 응답은 literal union으로 표현할 수 있다.

Q. Backend enum 값이 추가되면 어떻게 해?
A. Frontend literal union, label map, switch 분기를 함께 업데이트해야 한다.

Q. Error Code도 Union Type으로 정의해?
A. 정의하는 것이 좋다. 오류 코드 오타를 줄이고 메시지 매핑을 안정적으로 만들 수 있다.

Q. Error Response Type에는 뭐가 들어가?
A. success, code, message, field errors 같은 구조를 포함할 수 있다.

Q. Union Type에서 가장 흔한 실수는?
A. Type을 너무 넓게 잡거나 Narrowing 없이 Type별 property를 사용하는 것이다.

Q. Literal Type에서 가장 흔한 실수는?
A. Backend enum 값과 Frontend literal union 값이 불일치하는 것이다.

Q. TypeScript Part05의 핵심은 뭐야?
A. Union Type과 Literal Type을 API nullable field, 상태 값, Role, Backend enum과 정확히 연결하는 것이다.

Q. TypeScript Part05 다음 문서는 뭐가 좋아?
A. Type Alias and Interface 문서가 적합하다.
