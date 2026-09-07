# TypeScript Foundation Part06 - Type Alias and Interface

---

# 1. Type Alias

## 1.1 Type Alias Definition

### [개념]

Type Alias는 TypeScript Type에 이름을 붙여 재사용할 수 있게 만드는 문법이다.

```typescript
type UserId = number;

type User = {
  userId: UserId;
  nickname: string;
};
```

Type Alias는 Primitive Type, Object Type, Union Type, Literal Type, Function Type, Generic Type 등 다양한 Type에 이름을 붙일 수 있다.

---

### [핵심]

Type Alias 사용 대상:

- primitive alias
- object type
- union type
- literal union
- function type
- tuple type
- generic type
- intersection type
- API request type
- API response type
- React props type
- state type

Type Alias 장점:

- Type 재사용
- 의미 있는 Type 이름 부여
- API Type 관리
- 상태 Type 관리
- 코드 자동완성 향상
- Review Agent 검토 용이

---

### [실무]

2026 Frontend 실무 기준에서 Type Alias는 API Type, State Type, Literal Union, Props Type에 자주 사용된다.

API Response Type 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  averageRating: number | null;
};
```

Literal Union 예:

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";
type UserRole = "ROLE_USER" | "ROLE_ADMIN";
```

Function Type 예:

```typescript
type FestivalClickHandler = (festivalId: number) => void;
```

실무 기준:

- API Request / Response는 Type Alias로 명확히 정의 가능
- Union Type과 Literal Type은 Type Alias 사용 권장
- Function Type 재사용 시 Type Alias 사용
- React Props는 Type Alias 또는 Interface 모두 가능
- 팀 컨벤션에 맞춰 일관성 유지

---

### [FAQ]

Q. Type Alias가 뭐야?
A. TypeScript Type에 이름을 붙여 재사용할 수 있게 만드는 문법이다.

Q. Type Alias는 언제 써?
A. Object Type, Union Type, Literal Type, Function Type, API Type에 이름을 붙여 재사용할 때 쓴다.

Q. Type Alias로 객체 Type도 만들 수 있어?
A. 가능하다. `type User = { id: number; name: string }`처럼 작성한다.

Q. Type Alias는 Runtime에 남아?
A. 아니다. Type Alias는 Compile Time Type Check에만 사용되고 Runtime에는 남지 않는다.

---

## 1.2 Primitive and Literal Alias

### [개념]

Primitive Alias는 Primitive Type에 의미 있는 이름을 붙이는 방식이다.

Literal Alias는 제한된 문자열 또는 숫자 값에 이름을 붙이는 방식이다.

```typescript
type UserId = number;
type UserRole = "ROLE_USER" | "ROLE_ADMIN";
```

Primitive Alias는 의미를 표현하고 Literal Alias는 허용 값을 제한한다.

---

### [핵심]

Primitive Alias 사용 예:

- UserId
- FestivalId
- ReviewId
- Email
- Token
- ImageUrl

Literal Alias 사용 예:

- UserRole
- RequestStatus
- ThemeMode
- SortOption
- NotificationType
- ErrorCode

주의:

- Primitive Alias는 Runtime 구분을 만들지 않음
- `type UserId = number`와 `number`는 Runtime에서 동일
- 과도한 Primitive Alias는 복잡도를 높일 수 있음
- Literal Alias는 상태 값 제한에 유용

---

### [실무]

ID Alias 예:

```typescript
type FestivalId = number;

type FestivalInfoResponse = {
  festivalId: FestivalId;
  title: string;
};
```

Status Alias 예:

```typescript
type RequestStatus = "idle" | "loading" | "success" | "error";

function isLoading(status: RequestStatus): boolean {
  return status === "loading";
}
```

Role Alias 예:

```typescript
type UserRole = "ROLE_USER" | "ROLE_ADMIN";

function canAccessAdmin(role: UserRole): boolean {
  return role === "ROLE_ADMIN";
}
```

실무 기준:

- Literal Union은 Type Alias로 이름 부여
- ID Alias는 프로젝트 컨벤션에 따라 사용
- Role / Status / Sort / ErrorCode는 Alias 사용 권장
- Backend enum string과 Frontend Literal Alias 정합성 유지

---

### [FAQ]

Q. `type UserId = number`를 쓰면 number와 달라져?
A. Runtime에서는 달라지지 않는다. Compile Time 의미를 명확히 하기 위한 Alias다.

Q. Literal Union은 Type Alias로 만드는 게 좋아?
A. 좋다. `RequestStatus`, `UserRole`처럼 의미 있는 이름을 붙이면 재사용과 검색에 유리하다.

Q. 모든 Primitive Type에 Alias를 붙여야 해?
A. 아니다. 의미가 중요하거나 재사용이 많은 경우에만 사용한다.

---

## 1.3 Object Type Alias

### [개념]

Object Type Alias는 객체 구조에 이름을 붙이는 방식이다.

```typescript
type User = {
  userId: number;
  nickname: string;
};
```

Object Type Alias는 API Response, Request Body, Props, State, ViewModel 구조를 표현할 때 자주 사용한다.

---

### [핵심]

Object Type Alias 구성 요소:

- required property
- optional property
- nullable property
- readonly property
- nested object
- object array
- function property
- generic property

사용 영역:

- API Response Type
- API Request Type
- React Props Type
- Form Data Type
- Error Response Type
- ViewModel Type

---

### [실무]

API Response 예:

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

type FestivalListResponse = ApiResponse<FestivalInfoResponse[]>;
```

Props Type 예:

```typescript
type FestivalCardProps = {
  festival: FestivalInfoResponse;
  onClick: (festivalId: number) => void;
};
```

Form Data Type 예:

```typescript
type LoginFormData = {
  email: string;
  password: string;
};
```

실무 기준:

- API 응답 구조는 명확한 Object Type Alias로 정의
- nullable field는 `T | null`로 명시
- Optional Property와 Nullable Property 구분
- 화면 전용 데이터는 ViewModel Type Alias로 분리 가능
- 공통 wrapper는 Generic Type Alias 활용

---

### [FAQ]

Q. Object Type Alias는 어디에 많이 써?
A. API Response, Request Body, Props, Form Data, State Type에 많이 쓴다.

Q. API Response Type을 Type Alias로 정의해도 돼?
A. 된다. 실무에서 자주 사용하는 방식이다.

Q. Props Type도 Type Alias로 정의해도 돼?
A. 가능하다. React Props는 Type Alias와 Interface 모두 사용할 수 있다.

---

## 1.4 Union and Function Type Alias

### [개념]

Type Alias는 Union Type과 Function Type에 이름을 붙일 수 있다.

```typescript
type RequestStatus = "idle" | "loading" | "success" | "error";
type ClickHandler = (id: number) => void;
```

Union Type Alias는 허용 값을 제한하고 Function Type Alias는 callback 구조를 재사용하게 만든다.

---

### [핵심]

Union Type Alias 사용 영역:

- async status
- user role
- sort option
- error code
- notification type
- discriminated union

Function Type Alias 사용 영역:

- callback props
- event handler
- utility callback
- mapper function
- predicate function
- async function type

---

### [실무]

Callback Props 예:

```typescript
type FestivalClickHandler = (festivalId: number) => void;

type FestivalCardProps = {
  festivalId: number;
  title: string;
  onClick: FestivalClickHandler;
};
```

Predicate Function 예:

```typescript
type FestivalPredicate = (festival: FestivalInfoResponse) => boolean;

const hasImage: FestivalPredicate = (festival) => {
  return festival.imageUrl !== null;
};
```

Discriminated Union 예:

```typescript
type ApiState<T> =
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; message: string };
```

실무 기준:

- Callback Type이 여러 곳에서 반복되면 Type Alias로 분리
- Function Parameter와 Return Type 명확화
- Literal Union은 Type Alias로 이름 부여
- 복잡한 상태 구조는 Discriminated Union Type Alias 활용

---

### [FAQ]

Q. Union Type은 Type Alias로만 만들 수 있어?
A. 일반적으로 Type Alias로 만든다. Interface는 Union Type 자체를 직접 정의할 수 없다.

Q. Function Type Alias는 언제 써?
A. Callback Props나 반복되는 함수 구조를 재사용할 때 사용한다.

Q. Discriminated Union도 Type Alias로 정의해?
A. 그렇다. 객체 Union은 Type Alias로 정의하는 것이 일반적이다.

---

# 2. Interface

## 2.1 Interface Definition

### [개념]

Interface는 객체의 구조를 정의하는 TypeScript 문법이다.

```typescript
interface User {
  userId: number;
  nickname: string;
}
```

Interface는 Object Shape를 표현하고 확장 가능한 객체 모델을 정의할 때 사용한다.

---

### [핵심]

Interface 핵심 요소:

- object shape
- property type
- required property
- optional property
- readonly property
- method signature
- extends
- declaration merging
- class implements

Interface 사용 영역:

- 객체 구조 정의
- React Props Type
- 확장 가능한 모델
- Class 계약
- 외부 라이브러리 Type 확장

---

### [실무]

객체 구조 예:

```typescript
interface Festival {
  festivalId: number;
  title: string;
  imageUrl: string | null;
}
```

확장 예:

```typescript
interface FestivalDetail extends Festival {
  description: string;
  address: string;
}
```

Props 예:

```typescript
interface FestivalCardProps {
  festival: Festival;
  onClick: (festivalId: number) => void;
}
```

실무 기준:

- 객체 구조 중심이면 Interface 사용 가능
- 확장 가능한 모델에는 Interface 적합
- React Props는 Interface 또는 Type Alias 모두 가능
- Union / Literal Type은 Interface가 아니라 Type Alias 사용
- 팀 컨벤션 우선

---

### [FAQ]

Q. Interface가 뭐야?
A. 객체의 구조를 정의하는 TypeScript 문법이다.

Q. Interface는 언제 써?
A. 객체 구조를 정의하고 확장 가능성을 고려할 때 사용한다.

Q. Interface도 Optional Property를 지원해?
A. 지원한다. property 이름 뒤에 `?`를 붙이면 된다.

Q. Interface는 Runtime에 남아?
A. 아니다. Interface는 Compile Time Type Check에만 사용되고 Runtime에는 남지 않는다.

---

## 2.2 Interface Property Rules

### [개념]

Interface는 Required Property, Optional Property, Nullable Property, Readonly Property, Method Signature를 정의할 수 있다.

```typescript
interface UserProfile {
  readonly userId: number;
  nickname: string;
  profileImageUrl?: string | null;
  updateNickname: (nickname: string) => void;
}
```

Interface Property Rule은 Object Type Rule과 동일하게 Optional과 Nullable을 명확히 구분해야 한다.

---

### [핵심]

Interface Property 종류:

- required property
- optional property
- nullable property
- readonly property
- method signature
- function property
- nested object property

주의:

- optional은 property 누락 가능성
- nullable은 값이 null 가능성
- readonly는 Type Check 단계 제한
- method signature와 function property는 표현 방식이 다름
- Interface는 객체 구조 표현에 집중

---

### [실무]

Optional Property 예:

```typescript
interface FestivalSearchParams {
  keyword?: string;
  regionCode?: string;
  targetMonth?: string;
}
```

Nullable Property 예:

```typescript
interface UserResponse {
  userId: number;
  nickname: string;
  profileImageUrl: string | null;
}
```

Method Signature 예:

```typescript
interface FestivalRepository {
  findById(festivalId: number): Festival | undefined;
  findAll(): Festival[];
}
```

Function Property 예:

```typescript
interface FestivalCardProps {
  onClick: (festivalId: number) => void;
}
```

실무 기준:

- API Response Interface에서도 nullable 정확히 반영
- Optional과 Nullable 혼동 금지
- Method 구조가 필요하면 Interface 사용 가능
- Props callback은 function property 형태가 자주 사용됨

---

### [FAQ]

Q. Interface에서 optional property는 어떻게 써?
A. property 이름 뒤에 `?`를 붙인다.

Q. Interface에서 nullable property는 어떻게 써?
A. `profileImageUrl: string | null`처럼 Union Type으로 작성한다.

Q. Interface에 함수도 정의할 수 있어?
A. 가능하다. method signature 또는 function property 형태로 정의할 수 있다.

---

## 2.3 Interface Extends

### [개념]

Interface Extends는 기존 Interface를 확장해 새로운 Interface를 만드는 문법이다.

```typescript
interface Festival {
  festivalId: number;
  title: string;
}

interface FestivalDetail extends Festival {
  description: string;
  address: string;
}
```

Extends는 공통 객체 구조를 재사용하고 상세 구조를 추가할 때 유용하다.

---

### [핵심]

Interface Extends 사용 영역:

- base model 확장
- summary response to detail response
- common props 확장
- shared field 재사용
- class contract 확장

장점:

- 객체 구조 재사용
- 중복 property 감소
- 확장 관계 명확
- 자동완성 유지

주의:

- 무리한 상속 구조 지양
- API Response 구조가 실제로 확장 관계인지 확인
- 이름만 비슷한 Type을 억지로 extends하지 않음
- 복잡한 조합은 composition 또는 Type Alias 고려

---

### [실무]

Summary / Detail 예:

```typescript
interface FestivalSummaryResponse {
  festivalId: number;
  title: string;
  imageUrl: string | null;
}

interface FestivalDetailResponse extends FestivalSummaryResponse {
  description: string;
  address: string;
  eventStartDate: string;
  eventEndDate: string;
}
```

Props 확장 예:

```typescript
interface BaseButtonProps {
  disabled?: boolean;
  onClick: () => void;
}

interface PrimaryButtonProps extends BaseButtonProps {
  label: string;
}
```

실무 기준:

- Summary와 Detail이 실제 포함 관계면 extends 사용 가능
- 공통 Props 확장에 유용
- API DTO가 독립 구조라면 별도 Type으로 유지 가능
- 과도한 extends chain은 RAG 검색과 코드 이해를 어렵게 함

---

### [FAQ]

Q. Interface extends는 뭐야?
A. 기존 Interface의 property를 물려받아 새로운 Interface를 만드는 문법이다.

Q. Summary Response와 Detail Response에 extends를 써도 돼?
A. Detail이 Summary의 모든 field를 포함한다면 사용할 수 있다.

Q. extends를 많이 쓰면 좋아?
A. 아니다. 과도한 상속 구조는 이해와 유지보수를 어렵게 할 수 있다.

---

## 2.4 Declaration Merging

### [개념]

Declaration Merging은 같은 이름의 Interface 선언이 자동으로 합쳐지는 TypeScript 특징이다.

```typescript
interface User {
  userId: number;
}

interface User {
  nickname: string;
}
```

위 두 Interface는 하나로 합쳐져 `userId`와 `nickname`을 모두 가진 Interface가 된다.

---

### [핵심]

Declaration Merging 특징:

- 같은 이름의 Interface가 병합됨
- Type Alias는 Declaration Merging 불가
- Library Type 확장에 사용 가능
- 전역 Type 확장에 사용 가능
- 의도하지 않은 병합 주의

주의:

- 일반 앱 코드에서 무분별하게 사용 지양
- 같은 이름 Interface 중복 선언 주의
- 예기치 않은 Type 확장 가능
- RAG 문서에서는 개념 수준만 다룸

---

### [실무]

병합 예:

```typescript
interface AppConfig {
  apiBaseUrl: string;
}

interface AppConfig {
  enableLogging: boolean;
}

const config: AppConfig = {
  apiBaseUrl: "/api",
  enableLogging: true,
};
```

주의:

```typescript
interface User {
  userId: number;
}

interface User {
  role: string;
}
```

문제:

- 의도하지 않게 User 구조가 확장될 수 있다.
- 파일이 많아지면 추적이 어려울 수 있다.

실무 기준:

- 일반 도메인 Type은 중복 Interface 이름 주의
- Library augmentation 목적이 아니면 Declaration Merging 의존 지양
- Type Alias는 동일 이름 중복 선언 불가
- 팀 컨벤션에서 Interface 중복 선언 금지 권장

---

### [FAQ]

Q. Declaration Merging이 뭐야?
A. 같은 이름의 Interface 선언이 자동으로 합쳐지는 TypeScript 특징이다.

Q. Type Alias도 Declaration Merging이 돼?
A. 아니다. Type Alias는 같은 이름으로 중복 선언할 수 없다.

Q. Declaration Merging은 실무에서 많이 써?
A. 일반 앱 코드에서는 자주 쓰지 않고, Library Type 확장이나 전역 Type 보강에서 사용된다.

---

# 3. Type Alias vs Interface

## 3.1 Core Difference

### [개념]

Type Alias와 Interface는 모두 Type에 이름을 붙이고 객체 구조를 정의할 수 있지만 표현 가능한 범위와 확장 방식이 다르다.

```typescript
type UserType = {
  userId: number;
  nickname: string;
};

interface UserInterface {
  userId: number;
  nickname: string;
}
```

객체 Type만 보면 둘 다 가능하다.
하지만 Union Type, Literal Type, Function Type은 Type Alias가 적합하다.

---

### [핵심]

| 비교                | Type Alias        | Interface    |
| ------------------- | ----------------- | ------------ |
| Object Type         | 가능              | 가능         |
| Union Type          | 가능              | 불가         |
| Literal Type        | 가능              | 불가         |
| Function Type       | 가능              | 가능         |
| Tuple Type          | 가능              | 제한적       |
| Extends             | Intersection 사용 | extends 사용 |
| Declaration Merging | 불가              | 가능         |
| Class implements    | 가능              | 가능         |
| React Props         | 가능              | 가능         |
| 상태 Type           | 적합              | 제한적       |
| API Type            | 가능              | 가능         |

---

### [실무]

Type Alias가 적합한 경우:

```typescript
type RequestStatus = "idle" | "loading" | "success" | "error";

type ApiState<T> =
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; message: string };
```

Interface가 적합한 경우:

```typescript
interface Festival {
  festivalId: number;
  title: string;
}

interface FestivalDetail extends Festival {
  description: string;
}
```

실무 기준:

- Union / Literal / Discriminated Union → Type Alias
- 객체 구조 / 확장 가능 모델 → Interface 가능
- API Request / Response → 둘 다 가능
- React Props → 둘 다 가능
- 팀 컨벤션 우선
- 한 프로젝트 내 일관성 유지

---

### [FAQ]

Q. Type Alias와 Interface 차이는 뭐야?
A. 둘 다 객체 Type을 정의할 수 있지만 Type Alias는 Union / Literal Type에 적합하고 Interface는 객체 확장에 적합하다.

Q. 객체 Type은 type과 interface 중 뭐로 정의해야 해?
A. 둘 다 가능하다. 팀 컨벤션과 확장 필요성을 기준으로 선택한다.

Q. Union Type은 Interface로 만들 수 있어?
A. 아니다. Union Type은 Type Alias로 정의한다.

---

## 3.2 Extension Difference

### [개념]

Type Alias는 Intersection Type으로 확장하고 Interface는 `extends`로 확장한다.

```typescript
type BaseUser = {
  userId: number;
};

type AdminUser = BaseUser & {
  adminLevel: number;
};
```

```typescript
interface BaseUser {
  userId: number;
}

interface AdminUser extends BaseUser {
  adminLevel: number;
}
```

---

### [핵심]

Type Alias 확장:

- intersection `&` 사용
- Union Type과 조합 가능
- 복합 Type 표현에 강함
- 과도한 intersection은 가독성 저하

Interface 확장:

- `extends` 사용
- 객체 구조 확장에 명확함
- 여러 Interface 확장 가능
- 상속 관계가 직관적

---

### [실무]

Type Alias Intersection 예:

```typescript
type TimestampFields = {
  createdAt: string;
  updatedAt: string;
};

type PostResponse = {
  postId: number;
  title: string;
} & TimestampFields;
```

Interface Extends 예:

```typescript
interface TimestampFields {
  createdAt: string;
  updatedAt: string;
}

interface PostResponse extends TimestampFields {
  postId: number;
  title: string;
}
```

실무 기준:

- 단순 객체 확장은 Interface extends가 읽기 쉬움
- Union과 결합된 복잡한 Type은 Type Alias가 유리
- API Type에서는 과도한 조합보다 명시적 Type이 검색에 유리
- RAG 문서에서는 명확한 Type 이름과 단순 구조 우선

---

### [FAQ]

Q. Type Alias는 어떻게 확장해?
A. `&` Intersection Type으로 확장할 수 있다.

Q. Interface는 어떻게 확장해?
A. `extends` 키워드를 사용해 확장한다.

Q. Intersection과 extends 중 뭐가 좋아?
A. 객체 확장은 extends가 직관적이고, Union 등 복합 Type 조합은 Intersection이 유용하다.

---

## 3.3 React Props Type Selection

### [개념]

React Props Type은 Type Alias와 Interface 모두로 정의할 수 있다.

```typescript
type ButtonProps = {
  label: string;
  onClick: () => void;
};
```

```typescript
interface ButtonProps {
  label: string;
  onClick: () => void;
}
```

중요한 것은 Type Alias와 Interface 중 하나만 절대적으로 고르는 것이 아니라 프로젝트 컨벤션과 일관성이다.

---

### [핵심]

React Props Type 기준:

- Type Alias 가능
- Interface 가능
- callback props 명확화
- optional props 기본값 처리
- children 사용 여부 명확화
- shared props는 별도 Type으로 분리 가능
- 팀 컨벤션 우선

Type Alias 장점:

- Union Props 표현에 유리
- Discriminated Union Props 가능
- Function Type과 조합 쉬움

Interface 장점:

- 객체 Props 구조 표현 직관적
- extends로 공통 Props 확장 가능
- Library Type 확장과 친화적

---

### [실무]

일반 Props 예:

```typescript
type FestivalCardProps = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  onClick: (festivalId: number) => void;
};
```

확장 Props 예:

```typescript
interface BaseButtonProps {
  disabled?: boolean;
  onClick: () => void;
}

interface SubmitButtonProps extends BaseButtonProps {
  label: string;
}
```

Union Props 예:

```typescript
type AlertProps =
  | { type: "success"; message: string }
  | { type: "error"; message: string; retry: () => void };
```

실무 기준:

- 일반 Props는 type 또는 interface 모두 가능
- Union Props는 Type Alias 사용
- 공통 Props 확장은 Interface 또는 Intersection 사용
- Optional Props는 default value 처리
- Callback Props는 parameter와 return type 명시

---

### [FAQ]

Q. React Props는 type과 interface 중 뭐가 좋아?
A. 둘 다 가능하다. 프로젝트 컨벤션에 맞춰 일관되게 사용하는 것이 좋다.

Q. Union Props는 interface로 만들 수 있어?
A. Union 형태의 Props는 Type Alias가 적합하다.

Q. Props 확장이 많으면 interface가 좋아?
A. 객체 확장이 많다면 interface extends가 직관적일 수 있다.

---

## 3.4 API Type Selection

### [개념]

API Request Type과 API Response Type은 Type Alias와 Interface 모두로 정의할 수 있다.

실무에서는 팀 컨벤션, 확장 여부, Union 필요 여부에 따라 선택한다.

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};
```

---

### [핵심]

API Type에 Type Alias가 적합한 경우:

- Generic Response Wrapper
- Union Error Type
- Literal Status Type
- Discriminated Union State
- Utility Type 조합

API Type에 Interface가 적합한 경우:

- 확장 가능한 객체 모델
- Summary / Detail Response 구조
- 공통 Field 확장
- Class Contract가 필요한 경우

---

### [실무]

Type Alias API 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};

type FestivalListResponse = ApiResponse<FestivalInfoResponse[]>;
```

Interface API 예:

```typescript
interface FestivalSummaryResponse {
  festivalId: number;
  title: string;
  imageUrl: string | null;
}

interface FestivalDetailResponse extends FestivalSummaryResponse {
  description: string;
  address: string;
}
```

Error Union 예:

```typescript
type ApiErrorCode =
  | "VALIDATION_ERROR"
  | "UNAUTHORIZED"
  | "FORBIDDEN"
  | "NOT_FOUND";
```

실무 기준:

- API wrapper는 Generic Type Alias가 간결
- Summary / Detail 확장 관계는 Interface 가능
- Backend DTO 구조와 Type 이름 정합성 유지
- Response Type과 ViewModel Type 분리 가능
- Union이 필요하면 Type Alias 사용

---

### [FAQ]

Q. API Response Type은 type과 interface 중 뭐로 정의해?
A. 둘 다 가능하다. Generic wrapper나 union이 필요하면 type이 편하고, 확장 구조는 interface도 좋다.

Q. ApiResponse<T>는 type으로 만드는 게 좋아?
A. Generic wrapper는 Type Alias로 정의하는 방식이 간결하고 자주 사용된다.

Q. Backend DTO가 바뀌면 type이나 interface도 바꿔야 해?
A. 바꿔야 한다. Frontend API Type은 Backend 응답 구조와 정합성을 유지해야 한다.

---

# 4. Naming Rules

## 4.1 Type Naming Convention

### [개념]

Type Naming Convention은 Type Alias와 Interface 이름을 일관되게 작성하는 규칙이다.

RAG Retrieval 품질을 위해 Type 이름은 역할과 사용 범위를 명확히 드러내야 한다.

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
};
```

---

### [핵심]

권장 Naming:

- PascalCase 사용
- API Response는 `Response` suffix
- API Request는 `Request` suffix
- Form Data는 `FormData` suffix
- Props는 `Props` suffix
- State는 `State` suffix
- Params는 `Params` suffix
- Error는 `ErrorResponse` 또는 `ErrorCode`
- ViewModel은 `ViewModel` suffix

예:

- FestivalInfoResponse
- FestivalDetailResponse
- ReviewCreateRequest
- FestivalSearchParams
- LoginFormData
- FestivalCardProps
- ApiErrorResponse
- FestivalViewModel

---

### [실무]

좋은 예:

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

type ReviewCardProps = {
  review: ReviewResponse;
};
```

나쁜 예:

```typescript
type Data = {
  id: number;
};

type Props = {
  data: Data;
};
```

문제:

- 검색성이 낮음
- 어떤 Domain의 Type인지 불명확
- Agent Retrieval에서 혼선 발생

실무 기준:

- Type 이름에 Domain 포함
- Request / Response / Props / State 구분
- Generic Type은 의미 있는 이름 사용
- 너무 짧은 이름 지양
- RAG 문서에서는 검색 가능한 Type Name 우선

---

### [FAQ]

Q. Type 이름은 어떻게 짓는 게 좋아?
A. PascalCase로 작성하고 Response, Request, Props, State, Params 같은 역할 suffix를 붙이는 것이 좋다.

Q. Data, Props 같은 짧은 이름은 안 좋아?
A. 단일 파일 내부에서는 가능하지만 RAG와 협업 기준에서는 의미가 부족해 혼선이 생길 수 있다.

Q. API Type 이름에는 Response나 Request를 붙이는 게 좋아?
A. 좋다. Backend DTO와 Frontend Type 역할을 명확히 구분할 수 있다.

---

## 4.2 Interface Prefix Rule

### [개념]

Interface 이름 앞에 `I` prefix를 붙이는 방식은 과거 스타일에서 사용되었지만, Modern TypeScript에서는 필수 규칙이 아니다.

```typescript
interface User {
  userId: number;
  nickname: string;
}
```

현대 TypeScript에서는 `IUser`보다 `User`처럼 의미 중심 Naming을 선호하는 프로젝트가 많다.

---

### [핵심]

Modern TypeScript 기준:

- `I` prefix 필수 아님
- 팀 컨벤션 우선
- 의미 있는 Domain 이름 우선
- Type Alias와 Interface 이름 충돌 주의
- API Type suffix 활용 권장

예:

권장:

- UserResponse
- FestivalDetailResponse
- ReviewCreateRequest
- ButtonProps

지양 가능:

- IUser
- IFestival
- IProps

---

### [실무]

권장 예:

```typescript
interface FestivalResponse {
  festivalId: number;
  title: string;
}
```

지양 예:

```typescript
interface IFestivalResponse {
  festivalId: number;
  title: string;
}
```

실무 기준:

- 프로젝트 컨벤션이 `I` prefix를 사용하면 따름
- 신규 프로젝트는 의미 중심 Naming 권장
- Type Alias와 Interface 이름을 동일하게 만들지 않음
- RAG Retrieval을 위해 suffix 명확화

---

### [FAQ]

Q. Interface 이름 앞에 I를 붙여야 해?
A. 필수는 아니다. Modern TypeScript에서는 의미 중심 이름을 많이 사용한다.

Q. IUser 같은 이름은 틀린 거야?
A. 틀린 것은 아니지만 팀 컨벤션이 아니라면 굳이 사용할 필요는 없다.

Q. Type Alias와 Interface 이름이 같아도 돼?
A. 안 된다. 같은 scope에서 이름 충돌이 발생한다.

---

# 5. Common Mistakes

## 5.1 Type Alias Mistakes

### [개념]

Type Alias 실수는 Type Alias를 너무 넓게 정의하거나, 의미 없는 이름을 사용하거나, Runtime 값으로 오해할 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- `type Data`처럼 의미 없는 이름 사용
- `type Response`처럼 너무 일반적인 이름 사용
- Union Type을 string으로 대체
- API nullable field 누락
- Type Alias를 Runtime 값처럼 사용하려고 함
- Generic Type Alias에 any 사용
- 복잡한 Intersection 남용
- Type Alias와 Interface 이름 충돌
- Request / Response Type 구분 없음

---

### [실무]

나쁜 예:

```typescript
type Data = {
  id: number;
  name: string;
};

type Response = {
  data: Data;
};
```

문제:

- Domain이 불명확
- API 응답인지 화면 데이터인지 알기 어려움
- Retrieval 검색성이 낮음

개선:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
};

type FestivalListResponse = ApiResponse<FestivalInfoResponse[]>;
```

실무 기준:

- Domain + Role suffix 사용
- Response / Request / Props 이름 구분
- Literal Union은 Type Alias로 제한
- `any` 기반 Alias 지양
- Type Alias를 Runtime 값으로 사용하지 않음

---

### [FAQ]

Q. Type Alias에서 가장 흔한 실수는?
A. 의미 없는 이름, any 남용, nullable 누락, Runtime 값으로 오해하는 것이다.

Q. type은 Runtime에서 사용할 수 있어?
A. 아니다. type은 Compile Time Type Check 전용이다.

Q. Generic Type Alias에 any를 써도 돼?
A. 가능은 하지만 Type Safety가 약해진다. Generic Parameter를 사용하는 것이 좋다.

---

## 5.2 Interface Mistakes

### [개념]

Interface 실수는 Interface를 Union Type처럼 사용하려 하거나, Declaration Merging을 의도치 않게 발생시키거나, optional / nullable을 혼동할 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Interface로 Union Type을 정의하려고 함
- 같은 이름 Interface 중복 선언
- Declaration Merging을 모르고 이름 충돌 발생
- optional과 nullable 혼동
- extends를 과도하게 사용
- 실제 API 구조와 맞지 않는 확장 관계 생성
- `I` prefix를 컨벤션 없이 혼용
- Interface와 Type Alias 선택 기준 없음

---

### [실무]

나쁜 예:

```typescript
interface User {
  userId: number;
}

interface User {
  role: string;
}
```

문제:

- 두 Interface가 병합된다.
- 의도하지 않게 User 구조가 확장될 수 있다.

개선:

```typescript
interface UserResponse {
  userId: number;
  role: UserRole;
}
```

잘못된 확장 예:

```typescript
interface FestivalDetailResponse extends FestivalSearchParams {
  description: string;
}
```

문제:

- SearchParams와 DetailResponse는 의미상 확장 관계가 아니다.

실무 기준:

- Interface 이름 중복 주의
- extends는 실제 포함 관계에만 사용
- Union / Literal Type은 Type Alias 사용
- optional / nullable 정확히 구분
- 팀 컨벤션 통일

---

### [FAQ]

Q. Interface에서 가장 흔한 실수는?
A. 의도하지 않은 Declaration Merging, 과도한 extends, optional / nullable 혼동이다.

Q. Interface로 Union Type을 만들 수 있어?
A. 아니다. Union Type은 Type Alias로 정의해야 한다.

Q. 같은 이름 Interface를 여러 번 선언하면 어떻게 돼?
A. 자동으로 병합된다. 의도하지 않은 병합에 주의해야 한다.

---

## 5.3 Type Alias vs Interface Mistakes

### [개념]

Type Alias와 Interface 선택 실수는 기준 없이 혼용하거나, 한 문서 또는 프로젝트 안에서 일관성을 잃을 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- 같은 목적에 type과 interface 혼용
- Union Type을 interface로 표현하려 함
- Props Type 기준이 파일마다 다름
- API Type Naming 기준 없음
- 확장 관계가 아닌데 extends 사용
- 복잡한 Type을 무리하게 Interface로 표현
- 객체 Type은 무조건 Interface라고 오해
- Type Alias는 객체에 못 쓴다고 오해

---

### [실무]

선택 기준 예:

```text
Union / Literal / Discriminated Union
→ Type Alias

확장 가능한 Object Shape
→ Interface 가능

API Generic Wrapper
→ Type Alias 권장

React Props
→ Type Alias 또는 Interface 가능
→ 팀 컨벤션 우선
```

실무 기준:

- 팀 컨벤션을 문서화
- Domain별 Type Naming 통일
- RAG 문서에서는 Type Alias와 Interface 선택 이유 명시
- Review Agent는 혼용보다 일관성 확인
- 기능보다 검색성과 유지보수성 우선

---

### [FAQ]

Q. type과 interface를 섞어 쓰면 안 돼?
A. 섞어 쓸 수 있지만 기준 없이 혼용하면 유지보수와 검색성이 떨어진다.

Q. 객체 Type은 무조건 interface야?
A. 아니다. Type Alias로 객체 Type을 정의할 수 있다.

Q. React Props는 type으로 통일해도 돼?
A. 가능하다. 프로젝트 컨벤션으로 정하면 일관되게 사용하는 것이 중요하다.

---

# 6. Review Checklist

## 6.1 Part06 Checklist

### [개념]

TypeScript Foundation Part06 검수는 Type Alias, Interface, Type Alias vs Interface 선택 기준, Naming Convention, Common Mistakes를 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] Type Alias 정의가 포함되었는가?
- [ ] Primitive Alias와 Literal Alias 설명이 포함되었는가?
- [ ] Object Type Alias 설명이 포함되었는가?
- [ ] Union Type Alias 설명이 포함되었는가?
- [ ] Function Type Alias 설명이 포함되었는가?
- [ ] Interface 정의가 포함되었는가?
- [ ] Interface Property Rule 설명이 포함되었는가?
- [ ] Interface Extends 설명이 포함되었는가?
- [ ] Declaration Merging 설명이 포함되었는가?
- [ ] Type Alias vs Interface 비교가 포함되었는가?
- [ ] Extension Difference 설명이 포함되었는가?
- [ ] React Props Type 선택 기준이 포함되었는가?
- [ ] API Type 선택 기준이 포함되었는가?
- [ ] Naming Convention이 포함되었는가?
- [ ] Interface Prefix Rule이 포함되었는가?
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
→ Type Alias Check
→ Interface Check
→ Comparison Check
→ API Type Selection Check
→ React Props Selection Check
→ Naming Check
→ Common Mistake Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

Part06은 이후 Function Type, Generic, Utility Type, API Type, React Props Type 문서의 기반이다.

---

### [FAQ]

Q. Part06에서 가장 중요한 검수 기준은?
A. Type Alias와 Interface의 차이, 선택 기준, Naming Convention이 명확한지 확인하는 것이다.

Q. Part06이 이후 문서와 어떻게 연결돼?
A. Function Type Alias, Generic Type Alias, API Response Type, React Props Type 작성 기준으로 연결된다.

---

# Retrieval Queries

### [FAQ]

Q. Type Alias가 뭐야?
A. TypeScript Type에 이름을 붙여 재사용할 수 있게 만드는 문법이다.

Q. Type Alias는 언제 써?
A. Object Type, Union Type, Literal Type, Function Type, API Type에 이름을 붙여 재사용할 때 쓴다.

Q. Type Alias로 객체 Type도 만들 수 있어?
A. 가능하다. `type User = { id: number; name: string }`처럼 작성한다.

Q. Type Alias는 Runtime에 남아?
A. 아니다. Type Alias는 Compile Time Type Check에만 사용되고 Runtime에는 남지 않는다.

Q. `type UserId = number`를 쓰면 number와 달라져?
A. Runtime에서는 달라지지 않는다. Compile Time 의미를 명확히 하기 위한 Alias다.

Q. Literal Union은 Type Alias로 만드는 게 좋아?
A. 좋다. `RequestStatus`, `UserRole`처럼 의미 있는 이름을 붙이면 재사용과 검색에 유리하다.

Q. Object Type Alias는 어디에 많이 써?
A. API Response, Request Body, Props, Form Data, State Type에 많이 쓴다.

Q. API Response Type을 Type Alias로 정의해도 돼?
A. 된다. 실무에서 자주 사용하는 방식이다.

Q. Props Type도 Type Alias로 정의해도 돼?
A. 가능하다. React Props는 Type Alias와 Interface 모두 사용할 수 있다.

Q. Union Type은 Type Alias로만 만들 수 있어?
A. 일반적으로 Type Alias로 만든다. Interface는 Union Type 자체를 직접 정의할 수 없다.

Q. Function Type Alias는 언제 써?
A. Callback Props나 반복되는 함수 구조를 재사용할 때 사용한다.

Q. Discriminated Union도 Type Alias로 정의해?
A. 그렇다. 객체 Union은 Type Alias로 정의하는 것이 일반적이다.

Q. Interface가 뭐야?
A. 객체의 구조를 정의하는 TypeScript 문법이다.

Q. Interface는 언제 써?
A. 객체 구조를 정의하고 확장 가능성을 고려할 때 사용한다.

Q. Interface도 Optional Property를 지원해?
A. 지원한다. property 이름 뒤에 `?`를 붙이면 된다.

Q. Interface는 Runtime에 남아?
A. 아니다. Interface는 Compile Time Type Check에만 사용되고 Runtime에는 남지 않는다.

Q. Interface에서 nullable property는 어떻게 써?
A. `profileImageUrl: string | null`처럼 Union Type으로 작성한다.

Q. Interface에 함수도 정의할 수 있어?
A. 가능하다. method signature 또는 function property 형태로 정의할 수 있다.

Q. Interface extends는 뭐야?
A. 기존 Interface의 property를 물려받아 새로운 Interface를 만드는 문법이다.

Q. Summary Response와 Detail Response에 extends를 써도 돼?
A. Detail이 Summary의 모든 field를 포함한다면 사용할 수 있다.

Q. extends를 많이 쓰면 좋아?
A. 아니다. 과도한 상속 구조는 이해와 유지보수를 어렵게 할 수 있다.

Q. Declaration Merging이 뭐야?
A. 같은 이름의 Interface 선언이 자동으로 합쳐지는 TypeScript 특징이다.

Q. Type Alias도 Declaration Merging이 돼?
A. 아니다. Type Alias는 같은 이름으로 중복 선언할 수 없다.

Q. Declaration Merging은 실무에서 많이 써?
A. 일반 앱 코드에서는 자주 쓰지 않고, Library Type 확장이나 전역 Type 보강에서 사용된다.

Q. Type Alias와 Interface 차이는 뭐야?
A. 둘 다 객체 Type을 정의할 수 있지만 Type Alias는 Union / Literal Type에 적합하고 Interface는 객체 확장에 적합하다.

Q. 객체 Type은 type과 interface 중 뭐로 정의해야 해?
A. 둘 다 가능하다. 팀 컨벤션과 확장 필요성을 기준으로 선택한다.

Q. Union Type은 Interface로 만들 수 있어?
A. 아니다. Union Type은 Type Alias로 정의한다.

Q. Type Alias는 어떻게 확장해?
A. `&` Intersection Type으로 확장할 수 있다.

Q. Interface는 어떻게 확장해?
A. `extends` 키워드를 사용해 확장한다.

Q. Intersection과 extends 중 뭐가 좋아?
A. 객체 확장은 extends가 직관적이고, Union 등 복합 Type 조합은 Intersection이 유용하다.

Q. React Props는 type과 interface 중 뭐가 좋아?
A. 둘 다 가능하다. 프로젝트 컨벤션에 맞춰 일관되게 사용하는 것이 좋다.

Q. Union Props는 interface로 만들 수 있어?
A. Union 형태의 Props는 Type Alias가 적합하다.

Q. Props 확장이 많으면 interface가 좋아?
A. 객체 확장이 많다면 interface extends가 직관적일 수 있다.

Q. API Response Type은 type과 interface 중 뭐로 정의해?
A. 둘 다 가능하다. Generic wrapper나 union이 필요하면 type이 편하고, 확장 구조는 interface도 좋다.

Q. ApiResponse<T>는 type으로 만드는 게 좋아?
A. Generic wrapper는 Type Alias로 정의하는 방식이 간결하고 자주 사용된다.

Q. Backend DTO가 바뀌면 type이나 interface도 바꿔야 해?
A. 바꿔야 한다. Frontend API Type은 Backend 응답 구조와 정합성을 유지해야 한다.

Q. Type 이름은 어떻게 짓는 게 좋아?
A. PascalCase로 작성하고 Response, Request, Props, State, Params 같은 역할 suffix를 붙이는 것이 좋다.

Q. Data, Props 같은 짧은 이름은 안 좋아?
A. 단일 파일 내부에서는 가능하지만 RAG와 협업 기준에서는 의미가 부족해 혼선이 생길 수 있다.

Q. API Type 이름에는 Response나 Request를 붙이는 게 좋아?
A. 좋다. Backend DTO와 Frontend Type 역할을 명확히 구분할 수 있다.

Q. Interface 이름 앞에 I를 붙여야 해?
A. 필수는 아니다. Modern TypeScript에서는 의미 중심 이름을 많이 사용한다.

Q. IUser 같은 이름은 틀린 거야?
A. 틀린 것은 아니지만 팀 컨벤션이 아니라면 굳이 사용할 필요는 없다.

Q. Type Alias에서 가장 흔한 실수는?
A. 의미 없는 이름, any 남용, nullable 누락, Runtime 값으로 오해하는 것이다.

Q. type은 Runtime에서 사용할 수 있어?
A. 아니다. type은 Compile Time Type Check 전용이다.

Q. Interface에서 가장 흔한 실수는?
A. 의도하지 않은 Declaration Merging, 과도한 extends, optional / nullable 혼동이다.

Q. Interface로 Union Type을 만들 수 있어?
A. 아니다. Union Type은 Type Alias로 정의해야 한다.

Q. 같은 이름 Interface를 여러 번 선언하면 어떻게 돼?
A. 자동으로 병합된다. 의도하지 않은 병합에 주의해야 한다.

Q. type과 interface를 섞어 쓰면 안 돼?
A. 섞어 쓸 수 있지만 기준 없이 혼용하면 유지보수와 검색성이 떨어진다.

Q. 객체 Type은 무조건 interface야?
A. 아니다. Type Alias로 객체 Type을 정의할 수 있다.

Q. React Props는 type으로 통일해도 돼?
A. 가능하다. 프로젝트 컨벤션으로 정하면 일관되게 사용하는 것이 중요하다.

Q. TypeScript Part06의 핵심은 뭐야?
A. Type Alias와 Interface의 차이, 선택 기준, Naming Convention을 명확히 구분하는 것이다.

Q. TypeScript Part06 다음 문서는 뭐가 좋아?
A. Function Type, Callback Type, Optional Parameter, Async Function Type 문서가 적합하다.
