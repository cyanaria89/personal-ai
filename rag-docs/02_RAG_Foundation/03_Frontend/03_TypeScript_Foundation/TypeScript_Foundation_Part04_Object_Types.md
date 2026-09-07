# TypeScript Foundation Part04 - Object Types

---

# 1. Object Type

## 1.1 Object Type Definition

### [개념]

Object Type은 객체의 property 이름과 property Type을 정의하는 TypeScript Type이다.

Object Type은 Frontend에서 API Response, Request Body, Component Props, Form Data, State Model을 표현하는 핵심 방식이다.

```typescript
type User = {
  userId: number;
  nickname: string;
  active: boolean;
};
```

Object Type은 객체가 어떤 property를 가져야 하는지 Compile Time에 검사한다.

---

### [핵심]

Object Type 핵심 요소:

- property name
- property type
- required property
- optional property
- nullable property
- readonly property
- nested object
- object array
- method property
- excess property check

Object Type 사용 영역:

- API Response Type
- API Request Type
- React Props Type
- React State Type
- Form Data Type
- ViewModel Type
- Error Response Type

---

### [실무]

2026 Frontend 실무 기준에서 Object Type은 Backend DTO와 Frontend 화면 데이터 구조를 연결하는 핵심 계약이다.

API Response 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  regionName: string;
  imageUrl: string | null;
  averageRating: number | null;
};
```

Request Body 예:

```typescript
type ReviewCreateRequest = {
  festivalId: number;
  rating: number;
  content: string;
};
```

React Props 예:

```typescript
type FestivalCardProps = {
  festival: FestivalInfoResponse;
  onClick: (festivalId: number) => void;
};
```

실무 기준:

- Backend DTO와 Frontend Type 필드명 정합성 유지
- nullable field는 `T | null`로 명시
- 생략 가능한 field는 optional property 사용
- 화면 전용 데이터는 ViewModel Type으로 분리 가능
- Object Type은 의미 있는 이름으로 정의

---

### [FAQ]

Q. Object Type이 뭐야?
A. 객체의 property 이름과 Type을 정의하는 TypeScript Type이다.

Q. Object Type은 어디에 많이 써?
A. API Response, Request Body, Props, State, Form Data를 표현할 때 많이 쓴다.

Q. API Response Type은 Object Type으로 정의해?
A. 대부분 그렇다. Backend 응답 구조를 Object Type으로 정의해 Frontend에서 안전하게 사용한다.

Q. Object Type은 Runtime 검증도 해줘?
A. 아니다. Object Type은 Compile Time 검사 기준이며 Runtime 데이터 검증은 별도로 필요할 수 있다.

---

## 1.2 Required Property

### [개념]

Required Property는 객체에 반드시 존재해야 하는 property다.

Object Type에서 `?`가 없는 property는 기본적으로 Required Property다.

```typescript
type User = {
  userId: number;
  nickname: string;
};
```

위 Type에서 `userId`, `nickname`은 반드시 존재해야 한다.

---

### [핵심]

Required Property 특징:

- 객체 생성 시 반드시 필요
- property 누락 시 Type Error 발생
- API Response 필수 field 표현에 사용
- Request Body 필수 field 표현에 사용
- Props 필수 입력값 표현에 사용

---

### [실무]

Request Body 예:

```typescript
type LoginRequest = {
  email: string;
  password: string;
};
```

사용 예:

```typescript
const request: LoginRequest = {
  email: "test@example.com",
  password: "1234",
};
```

잘못된 예:

```typescript
const invalidRequest: LoginRequest = {
  email: "test@example.com",
};
```

문제:

- `password` property가 누락되었다.
- Required Property 누락으로 Type Error가 발생한다.

실무 기준:

- Backend Validation에서 필수인 field는 Required Property로 정의
- 화면 Component가 반드시 받아야 하는 Props는 Required Property로 정의
- API에서 항상 내려오는 field만 Required로 정의
- 실제 응답에서 누락될 수 있으면 optional 또는 nullable 검토

---

### [FAQ]

Q. Required Property는 뭐야?
A. 객체에 반드시 존재해야 하는 property다.

Q. property에 ?가 없으면 필수야?
A. 그렇다. Object Type에서 ?가 없는 property는 기본적으로 필수다.

Q. API에서 항상 내려오는 값은 Required로 정의하면 돼?
A. 실제 응답에서 항상 존재한다면 Required Property로 정의할 수 있다.

---

# 2. Optional Property and Nullable Property

## 2.1 Optional Property

### [개념]

Optional Property는 객체에 property가 없을 수 있음을 표현하는 문법이다.

property 이름 뒤에 `?`를 붙여 작성한다.

```typescript
type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  themeCode?: string;
};
```

`keyword?: string`은 `keyword` property가 없거나 `undefined`일 수 있다는 의미다.

---

### [핵심]

Optional Property 특징:

- property 누락 가능
- 값은 기본적으로 `T | undefined`
- Query Parameter Type에 자주 사용
- Optional Props에 자주 사용
- Partial Update Request에 사용 가능
- 사용 전 기본값 처리 필요

주의:

- optional은 null과 다름
- optional property는 property 자체가 없을 수 있음
- optional 남용 시 데이터 계약이 약해짐
- API 필수 field를 optional로 정의하지 않음

---

### [실무]

검색 조건 Type 예:

```typescript
type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  targetMonth?: string;
  page?: number;
};
```

Optional Props 예:

```typescript
type EmptyStateProps = {
  message?: string;
};

function getEmptyMessage(props: EmptyStateProps): string {
  return props.message ?? "데이터가 없습니다.";
}
```

Patch Request 예:

```typescript
type UserUpdateRequest = {
  nickname?: string;
  profileImageUrl?: string | null;
};
```

실무 기준:

- 검색 조건처럼 생략 가능한 값은 optional 사용
- Optional Props는 default value 처리
- Partial Update Request는 optional field 사용 가능
- optional 값을 사용할 때 `??` 또는 guard 처리
- Backend DTO와 optional 여부 정합성 유지

---

### [FAQ]

Q. Optional Property는 어떻게 써?
A. property 이름 뒤에 `?`를 붙인다. 예: `keyword?: string`.

Q. Optional Property는 null도 허용해?
A. 아니다. 기본적으로 property가 없거나 undefined일 수 있다는 의미다. null도 허용하려면 `string | null`을 추가해야 한다.

Q. Query Parameter Type에는 optional을 많이 써?
A. 그렇다. 검색 조건이나 필터 값은 생략 가능한 경우가 많아 optional property를 자주 사용한다.

---

## 2.2 Nullable Property

### [개념]

Nullable Property는 property는 존재하지만 값이 `null`일 수 있음을 표현하는 Type이다.

```typescript
type UserProfile = {
  userId: number;
  nickname: string;
  profileImageUrl: string | null;
};
```

`profileImageUrl: string | null`은 property는 존재하지만 값이 null일 수 있다는 의미다.

---

### [핵심]

Nullable Property 특징:

- property는 존재함
- 값이 null일 수 있음
- API Response에서 자주 사용
- 초기 State에서 자주 사용
- Optional Property와 의미가 다름
- 사용 전 null 처리 필요

사용 영역:

- profileImageUrl
- imageUrl
- averageRating
- deletedAt
- selectedUser
- currentUser
- optional relation response

---

### [실무]

API Response 예:

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
function getFestivalImageUrl(imageUrl: string | null): string {
  return imageUrl ?? "/default-festival.png";
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

- Backend가 null을 반환하면 nullable로 정의
- null 가능 값은 사용 전 fallback 처리
- nullable field를 required non-null로 단정하지 않음
- `as string`으로 null 제거 금지
- API Response Body 확인 후 nullable 반영

---

### [FAQ]

Q. Nullable Property는 뭐야?
A. property는 존재하지만 값이 null일 수 있는 property다.

Q. `imageUrl: string | null`은 무슨 뜻이야?
A. imageUrl property는 있지만 값이 string 또는 null일 수 있다는 뜻이다.

Q. null 가능 값은 어떻게 사용해?
A. null check, optional chaining, nullish coalescing으로 기본값이나 분기 처리를 한다.

---

## 2.3 Optional vs Nullable

### [개념]

Optional과 Nullable은 모두 값이 없을 가능성을 표현하지만 의미가 다르다.

```text
Optional
→ property가 없을 수 있음

Nullable
→ property는 있지만 값이 null일 수 있음
```

---

### [핵심]

| 비교         | Optional Property  | Nullable Property |       |
| ------------ | ------------------ | ----------------- | ----- |
| 문법         | `name?: string`    | `name: string     | null` |
| 의미         | property 누락 가능 | 값이 null 가능    |       |
| 기본 값      | undefined 가능     | null 가능         |       |
| API Response | 상황별 사용        | 자주 사용         |       |
| Query Params | 자주 사용          | 드묾              |       |
| 사용 전 처리 | undefined 처리     | null 처리         |       |

---

### [실무]

예:

```typescript
type Example = {
  keyword?: string;
  profileImageUrl: string | null;
};
```

의미:

```text
keyword?: string
→ 검색어 조건이 없을 수 있음

profileImageUrl: string | null
→ 응답 field는 있지만 이미지가 없으면 null
```

잘못된 예:

```typescript
type Festival = {
  imageUrl?: string;
};
```

문제:

- 실제 API가 `imageUrl: null`을 내려준다면 optional이 아니라 nullable로 표현해야 한다.

개선:

```typescript
type Festival = {
  imageUrl: string | null;
};
```

실무 기준:

- Query Parameter → optional 우선
- API nullable field → nullable 우선
- Partial Update Request → optional 가능
- Backend 응답 정책 확인
- Optional과 Nullable을 의미 없이 혼용 금지

---

### [FAQ]

Q. Optional과 Nullable 차이는?
A. Optional은 property 누락 가능성이고 Nullable은 property 값이 null일 가능성이다.

Q. `name?: string`과 `name: string | null`은 같아?
A. 아니다. optional은 없거나 undefined 가능이고 nullable은 값이 null 가능이다.

Q. API에서 null이 오면 optional로 써도 돼?
A. 권장하지 않는다. 실제로 null이 오면 `T | null`로 명시하는 것이 정확하다.

---

# 3. Readonly Property

## 3.1 Readonly Property Definition

### [개념]

Readonly Property는 객체 property를 직접 재할당하지 못하도록 TypeScript Type 단계에서 제한하는 문법이다.

```typescript
type User = {
  readonly userId: number;
  nickname: string;
};
```

`readonly`는 Runtime 불변성을 완전히 보장하지 않고 Compile Time 변경을 제한한다.

---

### [핵심]

Readonly Property 특징:

- property 직접 재할당 방지
- Type Check 단계에서 제한
- Runtime freeze가 아님
- ID, 생성일, 외부 변경 금지 값에 유용
- React State 직접 mutation 방지에 도움
- API Response의 식별자에 적용 가능

---

### [실무]

API Model 예:

```typescript
type Festival = {
  readonly festivalId: number;
  title: string;
  imageUrl: string | null;
};
```

잘못된 수정:

```typescript
const festival: Festival = {
  festivalId: 1,
  title: "Spring Festival",
  imageUrl: null,
};

festival.festivalId = 2;
```

문제:

- `festivalId`는 readonly property이므로 재할당할 수 없다.

실무 기준:

- ID는 readonly 고려
- createdAt은 readonly 고려
- 서버에서 생성되는 값은 readonly 고려
- 화면에서 수정 가능한 form field에는 readonly 사용 지양
- readonly는 깊은 불변성을 자동 보장하지 않음

---

### [FAQ]

Q. readonly property는 뭐야?
A. 객체 property를 직접 재할당하지 못하도록 Type 단계에서 제한하는 property다.

Q. readonly를 쓰면 Runtime에서도 값이 안 바뀌어?
A. 아니다. readonly는 TypeScript Type Check 단계의 제한이다.

Q. readonly는 언제 써?
A. ID, 생성일, 서버에서 생성된 값처럼 직접 수정하면 안 되는 값에 사용한다.

---

## 3.2 Readonly and Immutability

### [개념]

Readonly는 TypeScript의 Type Level 제한이고 Immutability는 Runtime 또는 코드 작성 방식에서 값을 변경하지 않는 원칙이다.

```text
readonly
→ Compile Time 재할당 제한

immutability
→ 원본 데이터를 직접 변경하지 않는 설계 원칙
```

---

### [핵심]

Readonly 관련 주의:

- readonly는 얕은 제한이다.
- nested object 내부 변경까지 자동 차단하지 않을 수 있다.
- Runtime Object.freeze와 다르다.
- React State에서는 원본 변경 금지 원칙이 중요하다.
- 배열은 readonly array로 입력 보호 가능하다.

---

### [실무]

얕은 readonly 예:

```typescript
type User = {
  readonly userId: number;
  profile: {
    nickname: string;
  };
};

const user: User = {
  userId: 1,
  profile: {
    nickname: "jun",
  },
};

user.profile.nickname = "kim";
```

설명:

- `userId`는 재할당할 수 없다.
- 하지만 nested object인 `profile.nickname`은 별도 readonly가 아니면 변경 가능하다.

React State 업데이트 기준:

```typescript
type Festival = {
  festivalId: number;
  title: string;
};

function renameFestival(
  festivals: readonly Festival[],
  festivalId: number,
): Festival[] {
  return festivals.map((festival) =>
    festival.festivalId === festivalId
      ? { ...festival, title: "Updated Festival" }
      : festival,
  );
}
```

실무 기준:

- readonly와 immutable update를 구분
- React State는 spread, map, filter로 새 객체 / 새 배열 생성
- nested object도 변경 금지하려면 nested readonly 설계 필요
- Review Agent는 직접 mutation 여부 확인

---

### [FAQ]

Q. readonly와 immutability는 같아?
A. 아니다. readonly는 Type Check 제한이고 immutability는 원본을 직접 변경하지 않는 설계 원칙이다.

Q. readonly는 nested object까지 막아?
A. 기본 readonly는 얕은 제한이다. nested property까지 막으려면 별도 readonly 설계가 필요하다.

Q. React State에서 readonly가 도움이 돼?
A. 원본 변경 실수를 줄이는 데 도움이 된다. 하지만 새 객체 / 새 배열로 업데이트하는 습관이 중요하다.

---

# 4. Nested Object Type

## 4.1 Nested Object Definition

### [개념]

Nested Object Type은 객체 property 안에 또 다른 객체 구조가 포함된 Type이다.

```typescript
type FestivalDetailResponse = {
  festivalId: number;
  title: string;
  location: {
    address: string;
    latitude: number;
    longitude: number;
  };
};
```

Nested Object는 API Response에서 상세 정보, 사용자 프로필, 위치 정보, 통계 정보 등을 표현할 때 사용한다.

---

### [핵심]

Nested Object 사용 영역:

- location
- profile
- author
- category
- region
- statistics
- payment
- notification setting

주의:

- 중첩이 깊으면 가독성 저하
- 재사용 가능한 구조는 별도 Type으로 분리
- nullable nested object 처리 필요
- optional nested object 접근 시 optional chaining 필요
- Backend DTO 구조와 정합성 유지

---

### [실무]

별도 Type 분리 예:

```typescript
type LocationInfo = {
  address: string;
  latitude: number;
  longitude: number;
};

type FestivalDetailResponse = {
  festivalId: number;
  title: string;
  location: LocationInfo;
};
```

Nullable Nested Object 예:

```typescript
type UserResponse = {
  userId: number;
  nickname: string;
  profile: {
    imageUrl: string | null;
    bio: string | null;
  } | null;
};
```

사용 예:

```typescript
function getProfileImage(user: UserResponse): string {
  return user.profile?.imageUrl ?? "/default-profile.png";
}
```

실무 기준:

- 재사용되는 nested object는 Type 분리
- nullable nested object는 `T | null`로 명시
- 접근 시 optional chaining 활용
- 너무 깊은 중첩은 ViewModel Mapping 고려
- API Response Type과 ViewModel Type 분리 가능

---

### [FAQ]

Q. Nested Object Type은 언제 써?
A. location, profile, author처럼 객체 안에 또 다른 객체 구조가 포함될 때 사용한다.

Q. Nested Object는 무조건 inline으로 써도 돼?
A. 가능하지만 재사용되거나 구조가 커지면 별도 Type으로 분리하는 것이 좋다.

Q. nullable nested object는 어떻게 처리해?
A. `Profile | null`처럼 Type에 반영하고 optional chaining 또는 null check로 접근한다.

---

## 4.2 Object Array

### [개념]

Object Array는 객체 Type을 element로 가지는 배열 Type이다.

```typescript
type Festival = {
  festivalId: number;
  title: string;
};

const festivals: Festival[] = [];
```

Frontend에서는 목록 API Response, 카드 리스트, 채팅 메시지 목록, 알림 목록에서 자주 사용한다.

---

### [핵심]

Object Array 사용 영역:

- festival list
- review list
- comment list
- chat message list
- notification list
- option list
- table row list

주의:

- 빈 배열은 element Type 명시
- API list는 `T[]` 또는 wrapper Type 사용
- find 결과는 `T | undefined`
- map / filter 결과 Type 확인
- sort는 원본 변경 주의

---

### [실무]

목록 응답 예:

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

find 사용 예:

```typescript
function findFestival(
  festivals: FestivalInfoResponse[],
  festivalId: number,
): FestivalInfoResponse | undefined {
  return festivals.find((festival) => festival.festivalId === festivalId);
}
```

실무 기준:

- Object Array는 명확한 Type Alias 또는 Interface 사용
- API wrapper 구조와 목록 구조 구분
- Page / Slice 응답은 별도 Generic Type 사용
- 빈 배열 State는 Type 명시
- 원본 변경 method 사용 주의

---

### [FAQ]

Q. Object Array Type은 어떻게 써?
A. 객체 Type을 정의한 뒤 `Festival[]`처럼 배열 Type으로 사용한다.

Q. API 목록 응답은 어떻게 Type으로 정의해?
A. `ApiResponse<FestivalInfoResponse[]>`처럼 공통 wrapper와 배열 Type을 함께 사용할 수 있다.

Q. find 결과는 왜 undefined가 붙어?
A. 조건에 맞는 요소가 없을 수 있으므로 `T | undefined`가 된다.

---

# 5. Index Signature and Record

## 5.1 Index Signature Basics

### [개념]

Index Signature는 객체의 key 이름이 고정되어 있지 않고 동적으로 결정될 때 사용하는 TypeScript 문법이다.

```typescript
type ErrorMap = {
  [fieldName: string]: string;
};
```

위 Type은 문자열 key와 문자열 value를 가지는 객체를 의미한다.

---

### [핵심]

Index Signature 사용 영역:

- validation error map
- dynamic field errors
- dictionary object
- lookup table
- key-value config
- response field map

주의:

- key Type은 보통 string 또는 number
- value Type을 너무 넓게 잡지 않음
- 고정 property가 있다면 일반 Object Type 우선
- 남용하면 Type 안정성이 약해짐

---

### [실무]

Validation Error 예:

```typescript
type FieldErrors = {
  [fieldName: string]: string;
};

const errors: FieldErrors = {
  email: "이메일 형식이 올바르지 않습니다.",
  password: "비밀번호는 필수입니다.",
};
```

API Error Response 예:

```typescript
type ApiErrorResponse = {
  success: false;
  message: string;
  errors?: {
    [fieldName: string]: string;
  };
};
```

실무 기준:

- 필드명이 동적인 오류 객체에 사용
- value Type은 구체적으로 유지
- 명확한 property 구조가 있으면 일반 Object Type 사용
- Error Response Type과 연결해 관리

---

### [FAQ]

Q. Index Signature는 언제 써?
A. 객체 key가 고정되어 있지 않고 동적으로 결정되는 key-value 구조에 사용한다.

Q. 모든 객체를 Index Signature로 만들면 돼?
A. 아니다. property가 명확한 객체는 일반 Object Type이 더 안전하다.

Q. Validation Error 객체에 Index Signature를 써도 돼?
A. 가능하다. field name이 동적으로 올 수 있으므로 적합하다.

---

## 5.2 Record Type Basics

### [개념]

`Record<K, V>`는 key Type과 value Type을 지정해 객체 Type을 만드는 TypeScript Utility Type이다.

```typescript
type FieldErrors = Record<string, string>;
```

위 Type은 string key와 string value를 가지는 객체를 의미한다.

---

### [핵심]

Record Type 특징:

- key-value object 표현
- dictionary object 표현
- lookup table 표현
- Index Signature 대체 가능
- Utility Type 기반
- 제한된 key union과 함께 사용 가능

---

### [실무]

Field Error 예:

```typescript
type FieldErrors = Record<string, string>;

const errors: FieldErrors = {
  email: "이메일 형식이 올바르지 않습니다.",
  password: "비밀번호는 필수입니다.",
};
```

Status Label 예:

```typescript
type RequestStatus = "idle" | "loading" | "success" | "error";

const statusLabel: Record<RequestStatus, string> = {
  idle: "대기",
  loading: "로딩 중",
  success: "성공",
  error: "오류",
};
```

실무 기준:

- 제한된 key set이 있으면 `Record<Union, Value>` 사용
- 동적 key-value error map에는 `Record<string, string>` 사용 가능
- 복잡한 객체 구조에는 명시적 Object Type 우선
- Record 남용 금지

---

### [FAQ]

Q. Record는 뭐야?
A. key Type과 value Type을 지정해 객체 Type을 만드는 Utility Type이다.

Q. Record<string, string>은 무슨 뜻이야?
A. 문자열 key와 문자열 value를 가지는 객체 Type이라는 뜻이다.

Q. Record는 언제 유용해?
A. 상태별 label map, validation error map, lookup table을 표현할 때 유용하다.

---

# 6. Excess Property Check

## 6.1 Excess Property Check Definition

### [개념]

Excess Property Check는 Object Literal이 Type에 정의되지 않은 property를 포함할 때 TypeScript가 오류를 감지하는 검사다.

```typescript
type User = {
  userId: number;
  nickname: string;
};

const user: User = {
  userId: 1,
  nickname: "jun",
  age: 20,
};
```

위 코드에서 `age`는 User Type에 없는 property이므로 오류가 발생한다.

---

### [핵심]

Excess Property Check 특징:

- Object Literal 직접 할당 시 강하게 동작
- 잘못된 property 이름 감지
- API Request Body 오류 방지에 유용
- Props 전달 오류 방지에 유용
- 오타 property 감지 가능

주의:

- 변수에 먼저 담으면 검사 방식이 달라질 수 있음
- Type Assertion으로 우회 가능하지만 위험
- Backend DTO와 field name 정합성 확인 필요

---

### [실무]

Request Body 오타 예:

```typescript
type ReviewCreateRequest = {
  festivalId: number;
  rating: number;
  content: string;
};

const request: ReviewCreateRequest = {
  festivalId: 1,
  rating: 5,
  contents: "좋아요",
};
```

문제:

- `contents`는 Type에 없는 property다.
- 올바른 property는 `content`다.

개선:

```typescript
const request: ReviewCreateRequest = {
  festivalId: 1,
  rating: 5,
  content: "좋아요",
};
```

실무 기준:

- Request Body Type으로 field 오타 방지
- Props Type으로 잘못된 props 전달 방지
- `as`로 Excess Property Check 우회 금지
- API 명세와 DTO 확인

---

### [FAQ]

Q. Excess Property Check가 뭐야?
A. Object Literal에 Type에 없는 property가 들어가면 TypeScript가 오류로 감지하는 검사다.

Q. Excess Property Check는 왜 유용해?
A. Request Body field 오타나 Props 이름 오타를 미리 잡을 수 있다.

Q. as로 오류를 없애도 돼?
A. 권장하지 않는다. 실제 Type 정의와 property 이름을 먼저 확인해야 한다.

---

# 7. Object Type and API Modeling

## 7.1 API Response Object Type

### [개념]

API Response Object Type은 Backend가 Frontend로 반환하는 응답 데이터 구조를 Object Type으로 표현한 것이다.

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  eventStartDate: string;
  eventEndDate: string;
};
```

API Response Type은 화면 코드에서 잘못된 property 접근을 줄이고 Backend DTO 변경을 추적하는 기준이 된다.

---

### [핵심]

API Response Type 필수 확인:

- field name
- field type
- nullable field
- list response
- wrapper response
- page response
- slice response
- error response
- date string
- numeric field
- optional field 여부

---

### [실무]

공통 응답 wrapper 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};
```

목록 응답 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  regionName: string;
  imageUrl: string | null;
  averageRating: number | null;
};

type FestivalListResponse = ApiResponse<FestivalInfoResponse[]>;
```

Slice 응답 예:

```typescript
type SliceResponse<T> = {
  content: T[];
  hasNext: boolean;
  number: number;
  size: number;
};
```

실무 기준:

- Backend DTO와 field name 일치
- 날짜는 대부분 string으로 수신
- nullable field 명시
- wrapper 구조 반영
- list / page / slice 구조 구분
- 화면 전용 Type은 ViewModel로 분리 가능

---

### [FAQ]

Q. API Response Object Type은 왜 중요해?
A. 서버 응답 구조를 Type으로 고정해 잘못된 property 접근과 화면 오류를 줄일 수 있다.

Q. API 날짜 field는 Date로 정의해?
A. 대부분 JSON 응답에서는 string으로 받고 필요하면 Frontend에서 Date로 변환한다.

Q. Backend DTO가 바뀌면 Frontend Type도 바꿔야 해?
A. 바꿔야 한다. Frontend API Response Type은 Backend 응답 구조와 정합성을 유지해야 한다.

---

## 7.2 API Request Object Type

### [개념]

API Request Object Type은 Frontend가 Backend로 보내는 요청 데이터 구조를 Object Type으로 표현한 것이다.

```typescript
type ReviewCreateRequest = {
  festivalId: number;
  rating: number;
  content: string;
};
```

Request Type은 필수 field 누락, 잘못된 field 이름, 잘못된 Type 전달을 줄인다.

---

### [핵심]

API Request Type 사용 영역:

- create request
- update request
- search params
- login request
- signup request
- form submit request
- query parameter object
- request body object

주의:

- Backend Request DTO와 field name 일치
- 필수 field는 Required Property
- 선택 field는 Optional Property
- nullable 가능 field는 `T | null`
- 민감정보 로그 출력 금지

---

### [실무]

Create Request 예:

```typescript
type PostCreateRequest = {
  title: string;
  content: string;
  category: string;
};
```

Update Request 예:

```typescript
type UserUpdateRequest = {
  nickname?: string;
  profileImageUrl?: string | null;
};
```

Search Params 예:

```typescript
type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  themeCode?: string;
  targetMonth?: string;
  page?: number;
  size?: number;
};
```

실무 기준:

- Form Data와 Request Type 차이 확인
- Backend validation 기준 반영
- Query Parameter는 optional field가 많음
- Create와 Update Type 분리
- Request Type에 불필요한 server-generated field 포함 금지

---

### [FAQ]

Q. API Request Object Type은 왜 필요해?
A. Frontend가 Backend로 보내는 데이터의 field 누락, 오타, Type 오류를 줄이기 위해 필요하다.

Q. Create Request와 Update Request Type은 같아도 돼?
A. 상황에 따라 다르다. Update는 optional field가 많으므로 분리하는 것이 좋은 경우가 많다.

Q. Query Parameter Type은 어떻게 정의해?
A. 검색 조건처럼 생략 가능한 값은 optional property로 정의한다.

---

# 8. Object Type Common Mistakes

## 8.1 Common Mistakes

### [개념]

Object Type 실수는 API 구조, optional / nullable 의미, property 이름, nested object 처리 기준이 맞지 않을 때 발생한다.

Object Type 오류는 화면 undefined, null runtime error, 잘못된 request body, props 전달 오류로 이어질 수 있다.

---

### [핵심]

자주 발생하는 실수:

- API nullable field를 non-null로 정의
- optional과 nullable 혼동
- Backend DTO field name과 Frontend Type field name 불일치
- snake_case / camelCase 불일치
- Required Property를 optional로 약하게 정의
- optional 값을 null처럼 처리
- nullable 값을 undefined처럼 처리
- nested object null 가능성 누락
- Object Array 빈 배열 Type 누락
- Record 남용
- Index Signature 남용
- Type Assertion으로 excess property error 우회
- API Response Type과 ViewModel Type 혼동

---

### [실무]

나쁜 예:

```typescript
type Festival = {
  festival_id: number;
  title: string;
  imageUrl: string;
  location?: {
    address: string;
  };
};
```

문제:

- Backend DTO가 `festivalId`라면 field name 불일치
- `imageUrl`이 null 가능하면 Type 오류
- `location`이 null로 올 수 있다면 optional이 아니라 nullable일 수 있음

개선:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  location: {
    address: string;
  } | null;
};
```

사용 예:

```typescript
function getFestivalAddress(festival: FestivalInfoResponse): string {
  return festival.location?.address ?? "주소 없음";
}
```

실무 기준:

- Network Response Body 확인
- Backend DTO 확인
- optional / nullable 의미 구분
- field name 정합성 유지
- null guard 작성
- Type Assertion보다 Type 정의 수정 우선

---

### [FAQ]

Q. Object Type에서 가장 흔한 실수는?
A. optional과 nullable 혼동, API field name 불일치, nullable field 누락이다.

Q. 타입은 맞는데 화면에서 undefined가 나와?
A. 실제 API Response 구조와 Frontend Type 정의가 다를 수 있다. Network Response Body를 확인해야 한다.

Q. snake_case와 camelCase가 다르면 어떻게 해?
A. Backend 응답이 snake_case면 Type도 맞추거나 mapping function으로 camelCase ViewModel로 변환한다.

---

# 9. Review Checklist

## 9.1 Part04 Checklist

### [개념]

TypeScript Foundation Part04 검수는 Object Type, Optional Property, Nullable Property, Readonly Property, Nested Object, Index Signature, Record, API Modeling 기준을 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] Object Type 정의가 포함되었는가?
- [ ] Required Property 설명이 포함되었는가?
- [ ] Optional Property 설명이 포함되었는가?
- [ ] Nullable Property 설명이 포함되었는가?
- [ ] Optional vs Nullable 비교가 포함되었는가?
- [ ] Readonly Property 설명이 포함되었는가?
- [ ] Readonly와 Immutability 차이가 포함되었는가?
- [ ] Nested Object Type 설명이 포함되었는가?
- [ ] Object Array 설명이 포함되었는가?
- [ ] Index Signature 설명이 포함되었는가?
- [ ] Record Type 설명이 포함되었는가?
- [ ] Excess Property Check 설명이 포함되었는가?
- [ ] API Response Object Type 예제가 포함되었는가?
- [ ] API Request Object Type 예제가 포함되었는가?
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
→ Object Type Check
→ Optional Nullable Check
→ Readonly Check
→ Nested Object Check
→ Index Signature Record Check
→ API Modeling Check
→ Common Mistake Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

Part04는 이후 Union Type, Type Alias, Interface, API Type, React Props Type 문서의 기반이다.

---

### [FAQ]

Q. Part04에서 가장 중요한 검수 기준은?
A. Object Type을 API Response, Request Body, Props, State와 연결하고 optional / nullable을 정확히 구분했는지 확인하는 것이다.

Q. Part04가 이후 문서와 어떻게 연결돼?
A. Union Type, Interface, Type Alias, API Response Type, React Props Type의 객체 모델링 기반이 된다.

---

# Retrieval Queries

### [FAQ]

Q. Object Type이 뭐야?
A. 객체의 property 이름과 Type을 정의하는 TypeScript Type이다.

Q. Object Type은 어디에 많이 써?
A. API Response, Request Body, Props, State, Form Data를 표현할 때 많이 쓴다.

Q. API Response Type은 Object Type으로 정의해?
A. 대부분 그렇다. Backend 응답 구조를 Object Type으로 정의해 Frontend에서 안전하게 사용한다.

Q. Object Type은 Runtime 검증도 해줘?
A. 아니다. Object Type은 Compile Time 검사 기준이며 Runtime 데이터 검증은 별도로 필요할 수 있다.

Q. Required Property는 뭐야?
A. 객체에 반드시 존재해야 하는 property다.

Q. property에 ?가 없으면 필수야?
A. 그렇다. Object Type에서 ?가 없는 property는 기본적으로 필수다.

Q. Optional Property는 어떻게 써?
A. property 이름 뒤에 `?`를 붙인다. 예: `keyword?: string`.

Q. Optional Property는 null도 허용해?
A. 아니다. 기본적으로 property가 없거나 undefined일 수 있다는 의미다. null도 허용하려면 `string | null`을 추가해야 한다.

Q. Query Parameter Type에는 optional을 많이 써?
A. 그렇다. 검색 조건이나 필터 값은 생략 가능한 경우가 많아 optional property를 자주 사용한다.

Q. Nullable Property는 뭐야?
A. property는 존재하지만 값이 null일 수 있는 property다.

Q. `imageUrl: string | null`은 무슨 뜻이야?
A. imageUrl property는 있지만 값이 string 또는 null일 수 있다는 뜻이다.

Q. null 가능 값은 어떻게 사용해?
A. null check, optional chaining, nullish coalescing으로 기본값이나 분기 처리를 한다.

Q. Optional과 Nullable 차이는?
A. Optional은 property 누락 가능성이고 Nullable은 property 값이 null일 가능성이다.

Q. `name?: string`과 `name: string | null`은 같아?
A. 아니다. optional은 없거나 undefined 가능이고 nullable은 값이 null 가능이다.

Q. API에서 null이 오면 optional로 써도 돼?
A. 권장하지 않는다. 실제로 null이 오면 `T | null`로 명시하는 것이 정확하다.

Q. readonly property는 뭐야?
A. 객체 property를 직접 재할당하지 못하도록 Type 단계에서 제한하는 property다.

Q. readonly를 쓰면 Runtime에서도 값이 안 바뀌어?
A. 아니다. readonly는 TypeScript Type Check 단계의 제한이다.

Q. readonly는 언제 써?
A. ID, 생성일, 서버에서 생성된 값처럼 직접 수정하면 안 되는 값에 사용한다.

Q. readonly와 immutability는 같아?
A. 아니다. readonly는 Type Check 제한이고 immutability는 원본을 직접 변경하지 않는 설계 원칙이다.

Q. readonly는 nested object까지 막아?
A. 기본 readonly는 얕은 제한이다. nested property까지 막으려면 별도 readonly 설계가 필요하다.

Q. Nested Object Type은 언제 써?
A. location, profile, author처럼 객체 안에 또 다른 객체 구조가 포함될 때 사용한다.

Q. Nested Object는 무조건 inline으로 써도 돼?
A. 가능하지만 재사용되거나 구조가 커지면 별도 Type으로 분리하는 것이 좋다.

Q. nullable nested object는 어떻게 처리해?
A. `Profile | null`처럼 Type에 반영하고 optional chaining 또는 null check로 접근한다.

Q. Object Array Type은 어떻게 써?
A. 객체 Type을 정의한 뒤 `Festival[]`처럼 배열 Type으로 사용한다.

Q. API 목록 응답은 어떻게 Type으로 정의해?
A. `ApiResponse<FestivalInfoResponse[]>`처럼 공통 wrapper와 배열 Type을 함께 사용할 수 있다.

Q. find 결과는 왜 undefined가 붙어?
A. 조건에 맞는 요소가 없을 수 있으므로 `T | undefined`가 된다.

Q. Index Signature는 언제 써?
A. 객체 key가 고정되어 있지 않고 동적으로 결정되는 key-value 구조에 사용한다.

Q. 모든 객체를 Index Signature로 만들면 돼?
A. 아니다. property가 명확한 객체는 일반 Object Type이 더 안전하다.

Q. Validation Error 객체에 Index Signature를 써도 돼?
A. 가능하다. field name이 동적으로 올 수 있으므로 적합하다.

Q. Record는 뭐야?
A. key Type과 value Type을 지정해 객체 Type을 만드는 Utility Type이다.

Q. Record<string, string>은 무슨 뜻이야?
A. 문자열 key와 문자열 value를 가지는 객체 Type이라는 뜻이다.

Q. Record는 언제 유용해?
A. 상태별 label map, validation error map, lookup table을 표현할 때 유용하다.

Q. Excess Property Check가 뭐야?
A. Object Literal에 Type에 없는 property가 들어가면 TypeScript가 오류로 감지하는 검사다.

Q. Excess Property Check는 왜 유용해?
A. Request Body field 오타나 Props 이름 오타를 미리 잡을 수 있다.

Q. API Response Object Type은 왜 중요해?
A. 서버 응답 구조를 Type으로 고정해 잘못된 property 접근과 화면 오류를 줄일 수 있다.

Q. API 날짜 field는 Date로 정의해?
A. 대부분 JSON 응답에서는 string으로 받고 필요하면 Frontend에서 Date로 변환한다.

Q. Backend DTO가 바뀌면 Frontend Type도 바꿔야 해?
A. 바꿔야 한다. Frontend API Response Type은 Backend 응답 구조와 정합성을 유지해야 한다.

Q. API Request Object Type은 왜 필요해?
A. Frontend가 Backend로 보내는 데이터의 field 누락, 오타, Type 오류를 줄이기 위해 필요하다.

Q. Create Request와 Update Request Type은 같아도 돼?
A. 상황에 따라 다르다. Update는 optional field가 많으므로 분리하는 것이 좋은 경우가 많다.

Q. Query Parameter Type은 어떻게 정의해?
A. 검색 조건처럼 생략 가능한 값은 optional property로 정의한다.

Q. Object Type에서 가장 흔한 실수는?
A. optional과 nullable 혼동, API field name 불일치, nullable field 누락이다.

Q. 타입은 맞는데 화면에서 undefined가 나와?
A. 실제 API Response 구조와 Frontend Type 정의가 다를 수 있다. Network Response Body를 확인해야 한다.

Q. snake_case와 camelCase가 다르면 어떻게 해?
A. Backend 응답이 snake_case면 Type도 맞추거나 mapping function으로 camelCase ViewModel로 변환한다.

Q. TypeScript Part04의 핵심은 뭐야?
A. Object Type을 API Response, Request Body, Props, State와 연결하고 optional / nullable을 정확히 구분하는 것이다.

Q. TypeScript Part04 다음 문서는 뭐가 좋아?
A. Union Type, Literal Type, Discriminated Union 문서가 적합하다.
