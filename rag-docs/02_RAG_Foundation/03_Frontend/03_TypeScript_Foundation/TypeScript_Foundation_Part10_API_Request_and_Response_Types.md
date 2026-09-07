# TypeScript Foundation Part10 - API Request and Response Types

---

# 1. API Type Modeling

## 1.1 API Type Modeling Definition

### [개념]

API Type Modeling은 Frontend가 Backend와 주고받는 Request / Response / Error 데이터를 TypeScript Type으로 정의하는 작업이다.

API Type은 Frontend와 Backend 사이의 데이터 계약이다.

```text
Backend DTO
→ API Response JSON
→ Frontend Response Type
→ UI Rendering
```

```text
Form Data
→ Request Type
→ API Request Body
→ Backend Request DTO
```

API Type Modeling은 Runtime 동작을 바꾸지 않는다.
TypeScript Type은 Compile Time 기준이며 실제 API Response 검증은 별도로 필요할 수 있다.

---

### [핵심]

API Type Modeling 대상:

- API Request Type
- API Response Type
- Error Response Type
- Query Parameter Type
- Path Parameter Type
- Form Data Type
- Common Response Wrapper
- List Response Type
- Slice Response Type
- Page Response Type
- Nullable Field
- Optional Field
- API Enum Type

핵심 기준:

- Backend DTO와 field name 정합성 유지
- nullable field 정확히 반영
- optional field 정확히 반영
- 날짜는 대부분 string으로 수신
- Request Type과 Response Type 분리
- 화면 전용 ViewModel Type 분리 가능
- `any` 사용 지양

---

### [실무]

2026 Frontend 실무 기준에서 API Type은 Frontend 안정성의 핵심이다.

API Type이 없으면 아래 문제가 자주 발생한다.

- 화면에서 undefined 출력
- 잘못된 property 접근
- null Runtime Error
- Backend DTO 변경 감지 실패
- Request Body field 오타
- Query Parameter 오타
- Error Response 처리 불안정
- API Wrapper 구조 혼동

기본 예:

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
  eventStartDate: string;
  eventEndDate: string;
};

type FestivalListResponse = ApiResponse<FestivalInfoResponse[]>;
```

실무 기준:

- API Layer에서 Request / Response Type을 명확히 정의
- Backend DTO 변경 시 Frontend Type도 함께 수정
- API Type과 UI ViewModel Type을 혼동하지 않음
- Response Wrapper 구조를 Type에 반영
- Network Response Body 확인 후 Type 작성

---

### [FAQ]

Q. API Type Modeling이 뭐야?
A. Frontend와 Backend가 주고받는 Request, Response, Error 데이터를 TypeScript Type으로 정의하는 작업이다.

Q. API Type은 왜 필요해?
A. 서버 응답과 요청 구조를 Type으로 고정해 field 누락, 오타, null 오류를 줄이기 위해 필요하다.

Q. API Type은 Runtime 검증도 해줘?
A. 아니다. TypeScript Type은 Compile Time 기준이며 실제 Runtime 응답 검증은 별도로 필요할 수 있다.

Q. Backend DTO가 바뀌면 Frontend Type도 바꿔야 해?
A. 바꿔야 한다. Frontend API Type은 Backend DTO와 정합성을 유지해야 한다.

---

## 1.2 API Type Location

### [개념]

API Type Location은 Request / Response / Error Type을 프로젝트 어디에 배치할지 정하는 기준이다.

Type 위치가 명확해야 Frontend Agent와 Review Agent가 API Type을 쉽게 찾고 재사용할 수 있다.

```text
src
├ api
├ types
├ models
├ features
└ components
```

---

### [핵심]

API Type 배치 후보:

- `src/types`
- `src/types/api`
- `src/models`
- `src/api/types`
- `src/features/{domain}/types`
- `src/features/{domain}/api`

선택 기준:

- 프로젝트 규모
- Feature 기반 구조 여부
- Domain별 Type 분리 여부
- API Client 위치
- 팀 컨벤션

---

### [실무]

Domain 기반 예:

```text
src
├ features
│ ├ festivals
│ │ ├ api
│ │ │ └ festivalApi.ts
│ │ ├ types
│ │ │ └ festivalTypes.ts
│ │ └ components
│ └ reviews
│   ├ api
│   └ types
```

공통 Type 예:

```text
src
├ types
│ ├ api.ts
│ ├ pagination.ts
│ └ error.ts
```

Type 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};

type SliceResponse<T> = {
  content: T[];
  hasNext: boolean;
  number: number;
  size: number;
};
```

실무 기준:

- 공통 Wrapper Type은 공통 위치에 둠
- Domain Response Type은 Domain별 위치에 둠
- Props Type은 Component 가까이에 둘 수 있음
- 여러 곳에서 공유되는 Type은 별도 파일로 분리
- Type 파일 이름은 검색 가능하게 작성

---

### [FAQ]

Q. API Type은 어디에 두는 게 좋아?
A. 프로젝트 구조에 따라 다르지만 공통 Type은 `types`, Domain Type은 feature별 `types`에 두는 방식이 좋다.

Q. Props Type도 API Type 파일에 넣어?
A. 보통 분리한다. API Type은 서버 데이터 구조이고 Props Type은 Component 입력 구조다.

Q. 공통 ApiResponse Type은 어디에 둬?
A. 여러 API에서 사용하므로 `types/api.ts` 또는 `api/types.ts` 같은 공통 위치가 적합하다.

---

# 2. API Request Type

## 2.1 Request Body Type

### [개념]

Request Body Type은 Frontend가 Backend로 보내는 JSON Body 구조를 정의하는 Type이다.

```typescript
type ReviewCreateRequest = {
  festivalId: number;
  rating: number;
  content: string;
};
```

Request Body Type은 Backend Request DTO와 field name, Type, required 여부가 맞아야 한다.

---

### [핵심]

Request Body Type 확인 대상:

- required field
- optional field
- nullable field
- string field
- number field
- boolean field
- enum field
- nested object
- array field
- sensitive field

주의:

- Response Type에서 무리하게 Omit하지 않음
- server-generated field 포함 금지
- password / token 로그 출력 금지
- Backend Validation 기준 확인
- Create Request와 Update Request 분리 가능

---

### [실무]

Create Request 예:

```typescript
type PostCreateRequest = {
  title: string;
  content: string;
  category: "NOTICE" | "FREE" | "QNA";
};
```

Review Request 예:

```typescript
type ReviewCreateRequest = {
  festivalId: number;
  rating: 1 | 2 | 3 | 4 | 5;
  content: string;
};
```

API Function 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
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
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(request),
  });

  if (!response.ok) {
    throw new Error("Failed to create review");
  }

  return await response.json();
}
```

실무 기준:

- Request Body Type은 명시적으로 작성
- Backend Request DTO와 field name 일치
- Create / Update / Search Request 분리
- `any` request 금지
- 민감정보는 Type에 포함되더라도 로그 출력 금지

---

### [FAQ]

Q. Request Body Type이 뭐야?
A. Frontend가 Backend로 보내는 JSON Body 구조를 정의하는 Type이다.

Q. Request Type은 Response Type에서 Omit으로 만들면 돼?
A. 가능은 하지만 Request와 Response는 목적이 다르므로 명시적 Request Type이 더 안전한 경우가 많다.

Q. Create Request와 Update Request는 분리해야 해?
A. 필수는 아니지만 required field와 optional field 기준이 다르면 분리하는 것이 좋다.

---

## 2.2 Create Request Type

### [개념]

Create Request Type은 새로운 데이터를 생성할 때 Backend로 보내는 요청 구조다.

Create Request는 생성에 필요한 필수 field를 명확히 표현해야 한다.

```typescript
type UserCreateRequest = {
  email: string;
  password: string;
  nickname: string;
};
```

---

### [핵심]

Create Request Type 특징:

- 필수 입력값 중심
- server-generated field 제외
- id 제외
- createdAt 제외
- updatedAt 제외
- Backend Validation과 연결
- Form Data와 유사하지만 항상 같지는 않음

주의:

- `Partial<T>` 남용 금지
- Response Type에서 무리하게 파생 금지
- 민감정보 관리 주의
- API 필수 field 누락 금지

---

### [실무]

Signup Request 예:

```typescript
type SignupRequest = {
  email: string;
  password: string;
  nickname: string;
};
```

Festival Create Request 예:

```typescript
type FestivalCreateRequest = {
  title: string;
  description: string;
  eventStartDate: string;
  eventEndDate: string;
  regionCode: string;
  categoryCode: string;
};
```

잘못된 예:

```typescript
type FestivalCreateRequest = Partial<FestivalResponse>;
```

문제:

- 생성 요청에 필요 없는 `festivalId`, `createdAt`이 포함될 수 있다.
- 생성에 필요한 field가 optional이 될 수 있다.
- API 계약이 불명확해진다.

실무 기준:

- Create Request는 명시적 Type 우선
- id / createdAt / updatedAt 제외
- Backend 필수 validation field 반영
- Form Data에서 Request로 Mapping 가능
- 날짜는 API 정책에 맞춰 string 사용

---

### [FAQ]

Q. Create Request Type은 뭐야?
A. 새로운 데이터를 생성할 때 Backend로 보내는 요청 Body 구조다.

Q. Create Request에 id를 넣어?
A. 보통 넣지 않는다. id는 서버에서 생성되는 field인 경우가 많다.

Q. Create Request에 Partial을 쓰면 왜 위험해?
A. 필수 입력값까지 optional이 되어 API 계약이 약해질 수 있다.

---

## 2.3 Update Request Type

### [개념]

Update Request Type은 기존 데이터를 수정할 때 Backend로 보내는 요청 구조다.

전체 수정인지 부분 수정인지에 따라 required / optional 기준이 달라진다.

```typescript
type UserUpdateRequest = {
  nickname?: string;
  profileImageUrl?: string | null;
};
```

---

### [핵심]

Update Request Type 종류:

- full update request
- partial update request
- patch request
- profile update
- status update
- password update

부분 수정 특징:

- optional field 많음
- `Partial<T>` 사용 가능
- 하지만 API 계약 명확성 필요
- server-generated field 제외
- null 허용 여부 명확히 표현

---

### [실무]

Profile Update 예:

```typescript
type UserProfileUpdateRequest = {
  nickname?: string;
  profileImageUrl?: string | null;
};
```

Review Update 예:

```typescript
type ReviewUpdateRequest = {
  rating?: 1 | 2 | 3 | 4 | 5;
  content?: string;
};
```

Password Update 예:

```typescript
type PasswordUpdateRequest = {
  currentPassword: string;
  newPassword: string;
};
```

실무 기준:

- PATCH 요청은 optional field 사용 가능
- PUT 전체 수정은 required field가 많을 수 있음
- `null`로 삭제를 표현하는지 확인
- `undefined` field는 JSON.stringify에서 생략될 수 있음
- Backend Update DTO와 정합성 유지
- 중요한 Update Type은 명시적 작성 권장

---

### [FAQ]

Q. Update Request Type은 전부 optional로 만들면 돼?
A. 부분 수정이면 optional이 많을 수 있지만, API 계약에 따라 필수 field가 있을 수 있다.

Q. PATCH Request에는 Partial을 써도 돼?
A. 가능하지만 server-generated field가 포함되지 않도록 주의해야 한다.

Q. null과 undefined는 Update Request에서 의미가 같아?
A. 아니다. null은 값 삭제 의도로 쓰일 수 있고 undefined는 field 생략으로 처리될 수 있다.

---

## 2.4 Query Parameter Type

### [개념]

Query Parameter Type은 URL Query String으로 전달되는 검색 조건, 필터 조건, 페이지 조건을 정의하는 Type이다.

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

Query Parameter는 대부분 optional field가 많다.

---

### [핵심]

Query Parameter Type 사용 영역:

- search keyword
- region filter
- theme filter
- target month
- sort option
- page
- size
- date range
- category
- status

주의:

- Query 값은 URL에서는 string 기반
- number 값은 string 변환 필요
- undefined 값은 query에서 제외
- null 처리 정책 확인
- literal union query 값은 검증 필요

---

### [실무]

Search Params 예:

```typescript
type FestivalSortOption = "latest" | "popular" | "rating";

type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  themeCode?: string;
  targetMonth?: string;
  sort?: FestivalSortOption;
  page?: number;
  size?: number;
};
```

Query String 생성 예:

```typescript
function createFestivalSearchQuery(params: FestivalSearchParams): string {
  const searchParams = new URLSearchParams();

  Object.entries(params).forEach(([key, value]) => {
    if (value !== undefined && value !== null) {
      searchParams.set(key, String(value));
    }
  });

  return searchParams.toString();
}
```

실무 기준:

- Query Parameter Type은 optional field 중심
- `number`는 URL 생성 시 string 변환
- `undefined` field는 제외
- Sort / Status 값은 literal union 사용
- URL에서 읽은 Query 값은 Runtime Validation 필요

---

### [FAQ]

Q. Query Parameter Type은 왜 필요해?
A. 검색 조건, 필터, 페이지 조건의 field 오타와 Type 오류를 줄이기 위해 필요하다.

Q. Query Parameter는 전부 string이야?
A. URL에서는 string으로 전달되지만 Frontend 내부 Type은 number나 literal union으로 모델링할 수 있다.

Q. undefined Query Parameter는 어떻게 처리해?
A. 보통 query string 생성 시 제외한다.

---

## 2.5 Path Parameter Type

### [개념]

Path Parameter Type은 URL 경로에 포함되는 식별자 값을 정의하는 Type이다.

```typescript
async function getFestivalDetail(
  festivalId: number,
): Promise<FestivalDetailResponse> {
  const response = await fetch(`/api/festivals/${festivalId}`);
  return await response.json();
}
```

Path Parameter는 대부분 required parameter다.

---

### [핵심]

Path Parameter 사용 영역:

- resource id
- user id
- post id
- festival id
- review id
- comment id
- slug

주의:

- 대부분 required parameter
- string slug와 number id 구분
- route param은 string으로 들어올 수 있음
- number id가 필요하면 Runtime 변환 필요
- 잘못된 id 값 방어 필요

---

### [실무]

number id 예:

```typescript
type FestivalId = number;

async function getFestivalDetail(
  festivalId: FestivalId,
): Promise<ApiResponse<FestivalDetailResponse>> {
  const response = await fetch(`/api/festivals/${festivalId}`);

  if (!response.ok) {
    throw new Error("Failed to load festival detail");
  }

  return await response.json();
}
```

route param 변환 예:

```typescript
function parseFestivalId(value: string | undefined): number | null {
  if (value === undefined) {
    return null;
  }

  const festivalId = Number(value);

  if (Number.isNaN(festivalId)) {
    return null;
  }

  return festivalId;
}
```

실무 기준:

- API Function의 path id는 required parameter
- React Router param은 string 가능성을 고려
- 숫자 id는 Number 변환과 NaN 방어
- slug는 string으로 유지
- path parameter 이름은 Backend route와 일치

---

### [FAQ]

Q. Path Parameter Type은 뭐야?
A. URL 경로에 포함되는 id나 slug 같은 값을 정의하는 Type이다.

Q. API path id는 optional이야?
A. 대부분 required다. id가 없으면 특정 resource를 조회할 수 없다.

Q. React Router에서 받은 id는 number야?
A. 보통 string으로 들어온다. number id가 필요하면 Number 변환과 NaN 방어가 필요하다.

---

# 3. API Response Type

## 3.1 Response Body Type

### [개념]

Response Body Type은 Backend가 Frontend로 반환하는 JSON 응답 구조를 정의하는 Type이다.

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};
```

Response Body Type은 실제 API Response Body와 정확히 일치해야 한다.

---

### [핵심]

Response Body Type 확인 대상:

- field name
- field type
- nullable field
- optional field
- date string
- list data
- nested object
- enum string
- wrapper structure
- page / slice structure

주의:

- API 날짜는 대부분 string
- nullable field 누락 금지
- Response Type과 ViewModel Type 혼동 금지
- snake_case / camelCase 정합성 확인
- Backend DTO 변경 추적 필요

---

### [실무]

단건 응답 예:

```typescript
type UserResponse = {
  userId: number;
  nickname: string;
  profileImageUrl: string | null;
  role: "ROLE_USER" | "ROLE_ADMIN";
};
```

상세 응답 예:

```typescript
type FestivalDetailResponse = {
  festivalId: number;
  title: string;
  description: string;
  address: string;
  imageUrl: string | null;
  eventStartDate: string;
  eventEndDate: string;
  averageRating: number | null;
};
```

실무 기준:

- 실제 Network Response Body 확인
- Backend Response DTO 확인
- null 가능 field 반영
- 날짜 string으로 수신 후 필요 시 Mapping
- Backend enum 값은 literal union으로 표현
- API Response Type은 서버 데이터 구조를 그대로 표현

---

### [FAQ]

Q. Response Body Type이 뭐야?
A. Backend가 Frontend로 반환하는 JSON 데이터 구조를 정의하는 Type이다.

Q. API 날짜 field는 Date로 받아?
A. 대부분 JSON 응답에서는 string으로 받고 필요하면 Frontend에서 Date로 변환한다.

Q. nullable field를 Type에 안 쓰면 어떻게 돼?
A. null 값이 올 때 Runtime Error나 잘못된 UI 출력이 발생할 수 있다.

---

## 3.2 Common Response Wrapper

### [개념]

Common Response Wrapper는 API 응답의 공통 구조를 Generic Type으로 정의한 것이다.

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};
```

Wrapper Type은 모든 API 응답의 공통 field를 일관되게 처리하게 한다.

---

### [핵심]

Common Response Wrapper 구성 예:

- `success`
- `data`
- `message`
- `code`
- `timestamp`
- `path`

주의:

- Backend 실제 wrapper 구조와 일치
- success field 이름 확인
- data field null 가능성 확인
- error response와 success response 구조 차이 확인
- API마다 wrapper가 다른지 확인

---

### [실무]

기본 Wrapper 예:

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

type FestivalInfoApiResponse = ApiResponse<FestivalInfoResponse>;
type FestivalListApiResponse = ApiResponse<FestivalInfoResponse[]>;
```

data가 null인 경우:

```typescript
type DeleteFestivalResponse = ApiResponse<null>;
```

Wrapper 확장 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
  timestamp?: string;
};
```

실무 기준:

- Backend ApiResponse 구조를 그대로 반영
- data가 없는 응답 정책 확인
- Generic `T`로 data Type 지정
- Error Response 구조는 별도 Type으로 분리 가능
- Axios / Fetch API Client에서 공통 처리 가능

---

### [FAQ]

Q. ApiResponse<T>는 왜 Generic으로 만들어?
A. 공통 응답 구조는 같고 data Type만 API마다 다르기 때문이다.

Q. data가 없으면 ApiResponse<null>로 써도 돼?
A. Backend가 null을 반환한다면 가능하다. 실제 응답 정책을 확인해야 한다.

Q. Error Response도 ApiResponse<T>로 처리해?
A. Backend 구조에 따라 다르다. Error Response 구조가 다르면 별도 Type으로 분리하는 것이 좋다.

---

## 3.3 List Response Type

### [개념]

List Response Type은 여러 개의 데이터를 배열로 반환하는 API 응답 Type이다.

```typescript
type FestivalListResponse = ApiResponse<FestivalInfoResponse[]>;
```

List Response는 목록 화면, 카드 리스트, 옵션 리스트, 검색 결과에 자주 사용된다.

---

### [핵심]

List Response Type 요소:

- array data
- element response type
- common wrapper
- empty array
- nullable field inside element
- list rendering
- map / filter / find

주의:

- 빈 목록은 null보다 `[]`인지 확인
- element Type을 명확히 정의
- List Wrapper와 Page / Slice 구분
- find 결과는 undefined 가능
- filter 후 Type Narrowing 필요 가능

---

### [실무]

목록 응답 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

type FestivalListResponse = ApiResponse<FestivalInfoResponse[]>;
```

목록 사용 예:

```typescript
function getFestivalTitles(response: FestivalListResponse): string[] {
  return response.data.map((festival) => festival.title);
}
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

- 목록 data는 `T[]`로 표현
- 빈 목록 응답 정책 확인
- `content`가 있으면 Slice / Page Response 검토
- List element nullable field 처리
- UI에서 map 사용 전 data 구조 확인

---

### [FAQ]

Q. List Response Type은 어떻게 써?
A. `ApiResponse<FestivalInfoResponse[]>`처럼 data Type에 배열을 넣는다.

Q. 빈 목록은 null로 와?
A. API 정책에 따라 다르지만 보통 빈 배열 `[]`이 권장된다. 실제 응답을 확인해야 한다.

Q. find 결과는 왜 undefined가 가능해?
A. 조건에 맞는 item이 없을 수 있기 때문이다.

---

## 3.4 Slice Response Type

### [개념]

Slice Response Type은 무한 스크롤 또는 더보기 목록에 사용하는 응답 구조다.

```typescript
type SliceResponse<T> = {
  content: T[];
  hasNext: boolean;
  number: number;
  size: number;
};
```

Slice는 전체 개수보다 다음 페이지 존재 여부가 중요할 때 사용한다.

---

### [핵심]

Slice Response 주요 field:

- `content`
- `hasNext`
- `number`
- `size`
- `first`
- `last`

사용 영역:

- infinite scroll
- load more
- chat messages
- notifications
- reviews
- comments

주의:

- Backend Slice field 이름 확인
- hasNext 기준 확인
- content element Type 명확화
- Page Response와 구분
- number가 0-based인지 확인

---

### [실무]

Review Slice 예:

```typescript
type ReviewResponse = {
  reviewId: number;
  rating: number;
  content: string;
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

type ChatMessageSliceApiResponse = ApiResponse<
  SliceResponse<ChatMessageResponse>
>;
```

실무 기준:

- 무한 스크롤은 SliceResponse 우선
- 다음 요청 여부는 `hasNext` 사용
- content 배열은 `T[]`
- message-only / image-only 데이터는 nullable field 반영
- Chat / Notification / Review 목록에 적합

---

### [FAQ]

Q. Slice Response Type은 언제 써?
A. 무한 스크롤이나 더보기처럼 다음 목록 존재 여부가 중요한 API에 사용한다.

Q. SliceResponse<T>의 content는 뭐야?
A. 현재 요청에서 받은 목록 데이터 배열이다.

Q. SliceResponse와 PageResponse 차이는?
A. Slice는 hasNext 중심이고 Page는 totalElements, totalPages 같은 전체 개수 정보를 포함한다.

---

## 3.5 Page Response Type

### [개념]

Page Response Type은 페이지 번호 기반 목록 응답 구조다.

전체 개수와 전체 페이지 수가 필요한 화면에 사용한다.

```typescript
type PageResponse<T> = {
  content: T[];
  totalElements: number;
  totalPages: number;
  number: number;
  size: number;
};
```

---

### [핵심]

Page Response 주요 field:

- `content`
- `totalElements`
- `totalPages`
- `number`
- `size`
- `first`
- `last`

사용 영역:

- admin table
- search result page
- page number navigation
- management list
- full pagination UI

주의:

- Backend Page field 이름 확인
- total count 필요 여부 확인
- number가 0-based인지 확인
- Slice보다 응답 정보가 많음
- 무한 스크롤에는 Slice가 더 적합할 수 있음

---

### [실무]

Festival Page 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

type FestivalPageResponse = PageResponse<FestivalInfoResponse>;
type FestivalPageApiResponse = ApiResponse<FestivalPageResponse>;
```

Page Navigation 예:

```typescript
function canMoveNextPage<T>(page: PageResponse<T>): boolean {
  return page.number + 1 < page.totalPages;
}
```

실무 기준:

- 전체 개수 표시가 필요하면 PageResponse 사용
- 단순 더보기는 SliceResponse 사용
- Table UI는 PageResponse가 적합
- Backend Pageable 응답 구조와 정합성 유지
- Page index 기준 확인

---

### [FAQ]

Q. Page Response Type은 언제 써?
A. 전체 개수, 전체 페이지 수, 페이지 번호 UI가 필요한 목록 API에 사용한다.

Q. PageResponse<T>의 totalElements는 뭐야?
A. 전체 데이터 개수를 의미한다.

Q. 무한 스크롤에도 PageResponse를 써야 해?
A. 꼭 그렇지 않다. 무한 스크롤은 SliceResponse가 더 가볍고 적합할 수 있다.

---

# 4. Error Response Type

## 4.1 Error Response Type Definition

### [개념]

Error Response Type은 API 요청 실패 시 Backend가 반환하는 오류 응답 구조를 정의하는 Type이다.

```typescript
type ApiErrorResponse = {
  success: false;
  message: string;
  code?: string;
  errors?: Record<string, string>;
};
```

Error Response Type은 사용자 메시지, field validation, fallback 처리에 중요하다.

---

### [핵심]

Error Response Type 구성 요소:

- `success`
- `message`
- `code`
- `status`
- `errors`
- `timestamp`
- `path`
- `fieldErrors`

오류 종류:

- validation error
- unauthorized
- forbidden
- not found
- conflict
- server error
- network error

주의:

- Backend GlobalExceptionHandler 구조 확인
- 사용자 메시지와 개발자 로그 구분
- 민감한 서버 오류 노출 금지
- field error 구조 확인
- 알 수 없는 오류 fallback 필요

---

### [실무]

기본 Error Type 예:

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

Error Message Map 예:

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

- Error Response Type은 Backend 오류 응답 구조와 맞춤
- code는 literal union 가능
- validation errors는 `Record<string, string>` 가능
- 사용자에게 보여줄 메시지는 fallback 처리
- 서버 내부 detail 노출 금지

---

### [FAQ]

Q. Error Response Type은 왜 필요해?
A. 실패 응답 구조를 Type으로 정의해 사용자 메시지와 validation 오류를 안정적으로 처리하기 위해 필요하다.

Q. errors는 왜 Record<string, string>으로 정의해?
A. field name과 error message의 key-value 구조를 표현하기 좋기 때문이다.

Q. 서버 오류 message를 그대로 보여줘도 돼?
A. 민감한 서버 detail이 포함될 수 있으므로 사용자용 메시지와 개발자 로그를 구분해야 한다.

---

## 4.2 Validation Error Type

### [개념]

Validation Error Type은 Form 입력값이나 Request Body 검증 실패 시 field별 오류 메시지를 표현하는 Type이다.

```typescript
type FieldErrors = Record<string, string>;
```

Validation Error는 회원가입, 로그인, 리뷰 작성, 게시글 작성 같은 Form UI에서 자주 사용된다.

---

### [핵심]

Validation Error 구성:

- field name
- error message
- global message
- code
- field errors map
- form error state

사용 영역:

- signup form
- login form
- review form
- post form
- profile update form
- password change form

---

### [실무]

Field Error Type 예:

```typescript
type FieldErrors = Record<string, string>;

type ValidationErrorResponse = {
  success: false;
  code: "VALIDATION_ERROR";
  message: string;
  errors: FieldErrors;
};
```

Form Error State 예:

```typescript
type LoginFormErrors = {
  email?: string;
  password?: string;
  global?: string;
};
```

Error 사용 예:

```typescript
function getFieldError(
  errors: Record<string, string> | undefined,
  fieldName: string,
): string {
  return errors?.[fieldName] ?? "";
}
```

실무 기준:

- Backend validation error field 구조 확인
- field name은 Form field name과 일치
- global error와 field error 구분
- errors가 optional인지 required인지 확인
- 사용자 메시지는 안전한 문구로 변환 가능

---

### [FAQ]

Q. Validation Error Type은 뭐야?
A. Form field별 검증 오류 메시지를 표현하는 Error Response Type이다.

Q. FieldErrors는 어떻게 정의해?
A. 일반적으로 `Record<string, string>` 또는 Form field별 optional object로 정의한다.

Q. global error와 field error는 달라?
A. 다르다. global error는 전체 요청 오류이고 field error는 특정 입력 field 오류다.

---

## 4.3 Network Error and Unknown Error

### [개념]

Network Error와 Unknown Error는 Backend Error Response가 아닌 Fetch 실패, 연결 실패, 알 수 없는 Runtime Error를 처리하는 영역이다.

API Error Response와 JavaScript Error는 구분해야 한다.

```typescript
function getErrorMessage(error: unknown): string {
  if (error instanceof Error) {
    return error.message;
  }

  return "알 수 없는 오류가 발생했습니다.";
}
```

---

### [핵심]

오류 구분:

- API Error Response
- Network Error
- JavaScript Error
- Unknown Error
- Validation Error
- Timeout Error

처리 기준:

- unknown으로 수신
- instanceof Error 확인
- ApiErrorResponse Type Guard 사용
- fallback message 제공
- 사용자 메시지와 로그 구분

---

### [실무]

Error Message 처리 예:

```typescript
function getUnknownErrorMessage(error: unknown): string {
  if (error instanceof Error) {
    return error.message;
  }

  return "요청 처리 중 오류가 발생했습니다.";
}
```

ApiErrorResponse Guard 예:

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

- catch error는 unknown으로 처리
- Error instance 확인 후 message 사용
- API Error Response는 Type Guard로 확인
- Network Error는 fallback message 제공
- 민감한 detail은 사용자에게 직접 노출하지 않음

---

### [FAQ]

Q. API Error Response와 Network Error는 같아?
A. 아니다. API Error Response는 서버가 반환한 오류 데이터이고 Network Error는 요청 자체 실패나 Runtime Error다.

Q. catch error는 항상 Error 객체야?
A. 아니다. JavaScript에서는 어떤 값이든 throw될 수 있으므로 unknown으로 보고 확인하는 것이 안전하다.

Q. 알 수 없는 오류는 어떻게 처리해?
A. fallback message를 제공하고 개발자 로그와 사용자 메시지를 구분한다.

---

# 5. API Enum and Status Type

## 5.1 API Enum Response Type

### [개념]

API Enum Response Type은 Backend enum 문자열 값을 Frontend literal union으로 표현하는 방식이다.

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
- chat message type
- donation status
- review status

주의:

- 대소문자 일치
- Backend enum 값 추가 시 Frontend Type 수정
- `ROLE_ADMIN` / `ADMIN` 혼용 금지
- Label Map도 함께 수정
- 알 수 없는 값 방어 필요 가능

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

Status Type 예:

```typescript
type CertStatus = "PENDING" | "APPROVED" | "REJECTED";

type CertificationResponse = {
  certificationId: number;
  status: CertStatus;
  rejectReason: string | null;
};
```

Label Map 예:

```typescript
const certStatusLabel: Record<CertStatus, string> = {
  PENDING: "대기",
  APPROVED: "승인",
  REJECTED: "반려",
};
```

실무 기준:

- Backend enum value와 Frontend union value 일치
- enum 값 추가 시 Type / Label / Switch 함께 수정
- API enum 값을 string으로 넓게 두지 않음
- 권한 값은 Backend Security naming과 통일
- UI Label은 Record로 관리 가능

---

### [FAQ]

Q. Backend enum 응답은 Frontend에서 어떻게 Type으로 표현해?
A. 문자열 enum 응답은 literal union으로 표현할 수 있다.

Q. Backend enum 값이 추가되면 뭐를 수정해야 해?
A. Frontend union Type, label map, switch 분기, 테스트를 함께 수정해야 한다.

Q. Role Type을 string으로 두면 안 돼?
A. 가능하지만 오타와 잘못된 권한 값을 막기 어렵기 때문에 literal union이 더 안전하다.

---

## 5.2 API Success Status Type

### [개념]

API Success Status Type은 API 요청 상태나 응답 성공 여부를 표현하는 Type이다.

Backend 응답의 `success: boolean`과 Frontend 요청 상태의 `AsyncStatus`는 역할이 다르다.

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";
```

---

### [핵심]

구분:

- `success: boolean` → 서버 응답 성공 여부
- `AsyncStatus` → Frontend 요청 상태
- `ApiState<T>` → 상태별 data / error 구조
- HTTP status → 네트워크 응답 상태 코드

주의:

- success boolean과 UI loading status 혼동 금지
- HTTP status와 body success field 구분
- 상태별 data 구조가 다르면 Discriminated Union 사용
- error 상태 message 처리 필요

---

### [실무]

Response Wrapper:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};
```

Frontend Request State:

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";

type RequestState = {
  status: AsyncStatus;
  errorMessage: string | null;
};
```

Discriminated Union State:

```typescript
type ApiState<T> =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; message: string };
```

실무 기준:

- 서버 응답 success와 프론트 요청 status 구분
- UI 상태는 AsyncStatus 또는 ApiState로 관리
- 응답 wrapper success는 Backend 정책에 맞춤
- HTTP status check와 body success check 모두 고려
- 모순 상태가 많으면 Discriminated Union 사용

---

### [FAQ]

Q. success boolean과 AsyncStatus는 같아?
A. 아니다. success는 서버 응답 성공 여부이고 AsyncStatus는 Frontend 요청 진행 상태다.

Q. HTTP status와 ApiResponse.success는 같아?
A. 아니다. HTTP status는 네트워크 응답 코드이고 success는 response body field일 수 있다.

Q. API 요청 상태는 어떻게 Type으로 관리해?
A. `AsyncStatus` 또는 `ApiState<T>` 같은 literal union / discriminated union으로 관리할 수 있다.

---

# 6. API Type and ViewModel

## 6.1 Response Type vs ViewModel Type

### [개념]

Response Type은 Backend API가 반환한 데이터 구조이고 ViewModel Type은 화면에서 사용하기 좋게 가공한 데이터 구조다.

```text
API Response Type
→ 서버 응답 구조 그대로

ViewModel Type
→ 화면 표시 목적 구조
```

Response Type과 ViewModel Type을 분리하면 API 변경과 UI 요구사항을 더 명확히 관리할 수 있다.

---

### [핵심]

Response Type 특징:

- Backend DTO와 일치
- 날짜는 string
- nullable field 포함
- server field name 사용
- 원본 API 구조 보존

ViewModel Type 특징:

- UI 출력에 적합
- fallback 처리 완료
- display text 포함
- Date format 변환 가능
- label 변환 가능
- camelCase 정리 가능

---

### [실무]

Response Type:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  eventStartDate: string;
};
```

ViewModel Type:

```typescript
type FestivalCardViewModel = {
  id: number;
  title: string;
  imageUrl: string;
  displayDate: string;
};
```

Mapping Function:

```typescript
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

실무 기준:

- API Response Type은 서버 구조 그대로 유지
- ViewModel에서 fallback / formatting 처리
- 날짜 string 변환은 Mapping Function에서 수행
- null 제거가 필요한 UI 구조는 ViewModel에서 처리
- Response Type과 ViewModel Type Naming 구분

---

### [FAQ]

Q. Response Type과 ViewModel Type은 뭐가 달라?
A. Response Type은 서버 응답 구조이고 ViewModel Type은 화면에서 쓰기 좋게 변환한 구조다.

Q. 날짜 string을 displayDate로 바꾸는 건 어디서 해?
A. Mapping Function에서 Runtime 변환으로 처리한다.

Q. imageUrl null fallback은 Type이 해줘?
A. 아니다. Mapping Function 또는 UI Rendering에서 fallback 처리를 해야 한다.

---

## 6.2 Mapping Function

### [개념]

Mapping Function은 API Response를 ViewModel 또는 Form Data로 변환하는 함수다.

```typescript
function toViewModel(response: ResponseType): ViewModelType {
  return mappedValue;
}
```

Mapping Function은 Runtime 변환, fallback 처리, label 변환을 담당한다.

---

### [핵심]

Mapping Function 역할:

- nullable fallback
- date formatting
- enum label mapping
- field name 변환
- number parsing
- string trimming
- image fallback
- response to view model
- form data to request

주의:

- Type Annotation은 Runtime 변환이 아님
- Mapping Function Return Type 명시 권장
- API Response Type과 ViewModel Type 분리
- 변환 실패 가능성 고려
- Locale formatting 기준 확인

---

### [실무]

Enum Label Mapping:

```typescript
type CertStatus = "PENDING" | "APPROVED" | "REJECTED";

const certStatusLabel: Record<CertStatus, string> = {
  PENDING: "대기",
  APPROVED: "승인",
  REJECTED: "반려",
};

function getCertStatusLabel(status: CertStatus): string {
  return certStatusLabel[status];
}
```

Form Data to Request:

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

- Form input value는 string으로 보고 변환
- 숫자 변환 후 NaN 방어
- literal number Type은 Runtime validation 후 사용
- Mapping 실패 시 null 또는 Result Type 고려
- 중요한 mapping은 테스트 대상

---

### [FAQ]

Q. Mapping Function은 왜 필요해?
A. API Response나 Form Data를 화면 또는 Request에 맞는 구조로 변환하기 위해 필요하다.

Q. input 값 숫자 변환은 Type이 해줘?
A. 아니다. `Number()` 같은 Runtime 변환과 validation이 필요하다.

Q. Mapping Function Return Type은 명시해야 해?
A. 권장한다. 변환 결과 구조를 명확히 검증할 수 있다.

---

# 7. API Client Function Type

## 7.1 Fetch API Function Type

### [개념]

Fetch API Function Type은 `fetch`를 사용하는 API 호출 함수의 Request / Response Type을 명확히 정의하는 방식이다.

```typescript
async function getFestivals(): Promise<ApiResponse<FestivalInfoResponse[]>> {
  const response = await fetch("/api/festivals");
  return await response.json();
}
```

Fetch의 `response.json()`은 기본적으로 Type을 자동 보장하지 않는다.

---

### [핵심]

Fetch API Function 확인 대상:

- URL
- method
- headers
- request body type
- response type
- error handling
- response.ok check
- json parse
- unknown response risk

주의:

- `response.json()` 결과는 Runtime Data
- TypeScript Type만으로 검증되지 않음
- `Promise<any>` 지양
- Error Response 처리 필요
- Authorization Header 필요 여부 확인

---

### [실무]

GET 예:

```typescript
async function getFestivalList(): Promise<ApiResponse<FestivalInfoResponse[]>> {
  const response = await fetch("/api/festivals");

  if (!response.ok) {
    throw new Error("Failed to load festival list");
  }

  return await response.json();
}
```

POST 예:

```typescript
async function createPost(
  request: PostCreateRequest,
): Promise<ApiResponse<PostResponse>> {
  const response = await fetch("/api/posts", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(request),
  });

  if (!response.ok) {
    throw new Error("Failed to create post");
  }

  return await response.json();
}
```

실무 기준:

- API Function Return Type 명시
- Request Body Type 명시
- response.ok 처리
- JSON parse 결과 검증 필요 가능
- Error Response 구조와 연결
- 공통 API Client 추상화 가능

---

### [FAQ]

Q. fetch response.json()은 Type을 자동으로 알아?
A. 아니다. Runtime Data이므로 TypeScript가 실제 구조를 검증하지 않는다.

Q. Fetch API Function Return Type은 어떻게 써?
A. `Promise<ApiResponse<T>>` 또는 `Promise<ResponseType>` 형태로 명시한다.

Q. response.ok check는 왜 필요해?
A. HTTP 실패 응답을 성공 데이터처럼 처리하지 않기 위해 필요하다.

---

## 7.2 Axios API Function Type

### [개념]

Axios API Function Type은 Axios 호출의 Request / Response Type을 명확히 지정하는 방식이다.

Axios는 Generic Type Parameter를 통해 response data Type을 지정할 수 있다.

```typescript
const response =
  await api.get<ApiResponse<FestivalInfoResponse[]>>("/festivals");
```

---

### [핵심]

Axios API Type 구성:

- request params type
- request body type
- response data type
- generic response type
- axios instance
- public api
- authenticated api
- error response type

주의:

- Axios Generic도 Runtime 검증은 아님
- response.data 구조 확인 필요
- params field 오타 주의
- 인증 API와 비인증 API 구분
- Error Response는 별도 처리

---

### [실무]

GET with Params 예:

```typescript
type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  targetMonth?: string;
};

async function searchFestivals(
  params: FestivalSearchParams,
): Promise<ApiResponse<FestivalInfoResponse[]>> {
  const response = await publicApi.get<ApiResponse<FestivalInfoResponse[]>>(
    "/festivals/search",
    { params },
  );

  return response.data;
}
```

POST 예:

```typescript
async function createReview(
  request: ReviewCreateRequest,
): Promise<ApiResponse<ReviewResponse>> {
  const response = await api.post<ApiResponse<ReviewResponse>>(
    "/reviews",
    request,
  );

  return response.data;
}
```

실무 기준:

- Axios Generic에 Response Type 지정
- params Type 명확히 정의
- request body Type 명확히 정의
- publicApi / authApi 구분
- Error Response Type은 interceptor 또는 catch에서 처리
- Axios Generic은 Runtime Validation이 아님

---

### [FAQ]

Q. Axios에서 Response Type은 어떻게 지정해?
A. `api.get<ApiResponse<T>>(url)`처럼 Generic Type Parameter를 사용한다.

Q. Axios Generic을 쓰면 Runtime 검증도 돼?
A. 아니다. TypeScript Type 지정일 뿐 실제 응답 구조 검증은 아니다.

Q. Axios params도 Type으로 정의해야 해?
A. 정의하는 것이 좋다. 검색 조건이나 필터 field 오타를 줄일 수 있다.

---

# 8. API Type Common Mistakes

## 8.1 Request Type Mistakes

### [개념]

Request Type 실수는 Backend Request DTO와 Frontend Type이 불일치하거나, Create / Update / Query Type을 구분하지 않을 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Request Type을 Response Type에서 무리하게 Omit
- Create Request에 Partial 사용
- Update Request required / optional 기준 오류
- Query Parameter Type 미정의
- Path Parameter string / number 혼동
- Form input value를 number로 단정
- server-generated field를 Request에 포함
- password / token 로그 출력
- Backend DTO field name 불일치
- optional과 nullable 혼동

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

- SignupRequest에 password가 누락될 수 있다.
- Response와 Request는 목적이 다르다.

개선:

```typescript
type SignupRequest = {
  email: string;
  password: string;
  nickname: string;
};
```

Query 실수 예:

```typescript
function searchFestivals(params: any) {
  return publicApi.get("/festivals/search", { params });
}
```

개선:

```typescript
type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  targetMonth?: string;
};

function searchFestivals(params: FestivalSearchParams) {
  return publicApi.get("/festivals/search", { params });
}
```

실무 기준:

- Request Type은 Backend Request DTO 기준
- Create / Update / Search Type 분리
- Form Data와 Request Type 구분
- 민감정보 로그 금지
- any params 금지

---

### [FAQ]

Q. Request Type에서 가장 흔한 실수는?
A. Response Type을 억지로 재사용하거나 Create / Update / Query Type을 구분하지 않는 것이다.

Q. Form Data Type과 Request Type은 같아?
A. 항상 같지 않다. Form input은 string일 수 있고 Request에서는 number로 변환해야 할 수 있다.

Q. server-generated field를 Request에 넣어도 돼?
A. 보통 넣지 않는다. id, createdAt, updatedAt은 서버가 생성하는 field인 경우가 많다.

---

## 8.2 Response Type Mistakes

### [개념]

Response Type 실수는 실제 API Response Body와 Frontend Type 정의가 다를 때 발생한다.

이 문제는 undefined 표시, null 오류, 화면 렌더링 실패로 이어진다.

---

### [핵심]

자주 발생하는 실수:

- nullable field 누락
- 날짜를 Date로 단정
- wrapper 구조 누락
- data field 내부 구조 오해
- list / slice / page 구조 혼동
- snake_case / camelCase 불일치
- Backend enum 값과 union 불일치
- averageRating 같은 nullable number 누락
- message-only / image-only nullable field 누락
- Response Type과 ViewModel Type 혼동

---

### [실무]

나쁜 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string;
  eventStartDate: Date;
};
```

문제:

- imageUrl이 null 가능하면 Type이 틀림
- JSON 날짜는 대부분 string
- Runtime에서 Date instance가 아님

개선:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  eventStartDate: string;
};
```

Wrapper 누락 예:

```typescript
type FestivalListResponse = FestivalInfoResponse[];
```

실제 Backend가 아래 구조면 틀림:

```typescript
type FestivalListResponse = ApiResponse<FestivalInfoResponse[]>;
```

실무 기준:

- Network Response Body 확인
- Backend DTO 확인
- wrapper 구조 반영
- nullable field 반영
- 날짜 string 처리
- ViewModel 변환은 별도 Mapping Function 사용

---

### [FAQ]

Q. Response Type에서 가장 흔한 실수는?
A. nullable field 누락, wrapper 구조 누락, 날짜를 Date로 단정하는 것이다.

Q. Type은 맞는데 화면에서 undefined가 나와?
A. 실제 API Response 구조와 Frontend Type 정의가 다를 수 있다. Network Response Body를 확인해야 한다.

Q. API Response Type과 ViewModel Type을 섞어도 돼?
A. 권장하지 않는다. 서버 구조와 화면 구조는 분리하는 것이 안전하다.

---

## 8.3 Error Type Mistakes

### [개념]

Error Type 실수는 API Error Response, Network Error, JavaScript Error를 구분하지 않거나 fallback 메시지가 없을 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Error Response Type 미정의
- catch error를 any로 처리
- error.message 직접 접근
- Backend validation errors 구조 미반영
- 서버 detail message 그대로 노출
- field error와 global error 혼동
- HTTP status와 response body code 혼동
- 알 수 없는 오류 fallback 없음
- Axios error response 구조 미확인

---

### [실무]

나쁜 예:

```typescript
try {
  await createReview(request);
} catch (error: any) {
  alert(error.message);
}
```

문제:

- error가 어떤 구조인지 불명확
- 서버 detail을 그대로 노출할 수 있음
- any 사용으로 Type Safety 저하

개선:

```typescript
function getSafeErrorMessage(error: unknown): string {
  if (error instanceof Error) {
    return error.message;
  }

  return "요청 처리 중 오류가 발생했습니다.";
}
```

Validation Error 처리:

```typescript
type ValidationErrorResponse = {
  success: false;
  code: "VALIDATION_ERROR";
  message: string;
  errors: Record<string, string>;
};
```

실무 기준:

- catch error는 unknown으로 처리
- Error Response Type 정의
- Field Error Type 정의
- fallback message 제공
- 사용자 메시지와 개발자 로그 분리
- 민감한 오류 detail 노출 금지

---

### [FAQ]

Q. Error Type에서 가장 흔한 실수는?
A. API Error Response와 Network Error를 구분하지 않고 catch error를 any로 처리하는 것이다.

Q. error.message를 바로 보여줘도 돼?
A. 민감한 정보가 포함될 수 있으므로 사용자용 메시지로 변환하거나 fallback을 제공하는 것이 좋다.

Q. Validation Error는 어떻게 Type으로 정의해?
A. `errors: Record<string, string>` 또는 field별 optional object로 정의할 수 있다.

---

# 9. Review Checklist

## 9.1 Part10 Checklist

### [개념]

TypeScript Foundation Part10 검수는 API Request Type, API Response Type, Error Response Type, API Wrapper, Query Parameter, Path Parameter, ViewModel Mapping 기준을 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] API Type Modeling 정의가 포함되었는가?
- [ ] API Type 위치 기준이 포함되었는가?
- [ ] Request Body Type 설명이 포함되었는가?
- [ ] Create Request Type 설명이 포함되었는가?
- [ ] Update Request Type 설명이 포함되었는가?
- [ ] Query Parameter Type 설명이 포함되었는가?
- [ ] Path Parameter Type 설명이 포함되었는가?
- [ ] Response Body Type 설명이 포함되었는가?
- [ ] Common Response Wrapper 설명이 포함되었는가?
- [ ] List Response Type 설명이 포함되었는가?
- [ ] Slice Response Type 설명이 포함되었는가?
- [ ] Page Response Type 설명이 포함되었는가?
- [ ] Error Response Type 설명이 포함되었는가?
- [ ] Validation Error Type 설명이 포함되었는가?
- [ ] Network Error / Unknown Error 설명이 포함되었는가?
- [ ] API Enum Response Type 설명이 포함되었는가?
- [ ] API Success Status와 AsyncStatus 차이가 포함되었는가?
- [ ] Response Type vs ViewModel Type 차이가 포함되었는가?
- [ ] Mapping Function 설명이 포함되었는가?
- [ ] Fetch API Function Type 예제가 포함되었는가?
- [ ] Axios API Function Type 예제가 포함되었는가?
- [ ] Request / Response / Error Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Required Section Check
→ Request Type Check
→ Response Type Check
→ Error Type Check
→ Wrapper Type Check
→ Query Path Parameter Check
→ ViewModel Mapping Check
→ API Client Function Check
→ Common Mistake Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

Part10은 이후 React TypeScript Readiness, tsconfig, Migration, Troubleshooting 문서의 API Type 기반이다.

---

### [FAQ]

Q. Part10에서 가장 중요한 검수 기준은?
A. API Request / Response / Error Type이 Backend DTO와 정합성을 유지하고 nullable, wrapper, query, path parameter를 정확히 반영했는지 확인하는 것이다.

Q. Part10이 이후 문서와 어떻게 연결돼?
A. React TypeScript Props, State, Data Fetching, Error Handling, Migration, Troubleshooting의 API Type 기반이 된다.

---

# Retrieval Queries

### [FAQ]

Q. API Type Modeling이 뭐야?
A. Frontend와 Backend가 주고받는 Request, Response, Error 데이터를 TypeScript Type으로 정의하는 작업이다.

Q. API Type은 왜 필요해?
A. 서버 응답과 요청 구조를 Type으로 고정해 field 누락, 오타, null 오류를 줄이기 위해 필요하다.

Q. API Type은 Runtime 검증도 해줘?
A. 아니다. TypeScript Type은 Compile Time 기준이며 실제 Runtime 응답 검증은 별도로 필요할 수 있다.

Q. Backend DTO가 바뀌면 Frontend Type도 바꿔야 해?
A. 바꿔야 한다. Frontend API Type은 Backend DTO와 정합성을 유지해야 한다.

Q. API Type은 어디에 두는 게 좋아?
A. 공통 Type은 `types`, Domain Type은 feature별 `types`에 두는 방식이 좋다.

Q. 공통 ApiResponse Type은 어디에 둬?
A. 여러 API에서 사용하므로 `types/api.ts` 또는 `api/types.ts` 같은 공통 위치가 적합하다.

Q. Request Body Type이 뭐야?
A. Frontend가 Backend로 보내는 JSON Body 구조를 정의하는 Type이다.

Q. Request Type은 Response Type에서 Omit으로 만들면 돼?
A. 가능은 하지만 Request와 Response는 목적이 다르므로 명시적 Request Type이 더 안전한 경우가 많다.

Q. Create Request Type은 뭐야?
A. 새로운 데이터를 생성할 때 Backend로 보내는 요청 Body 구조다.

Q. Create Request에 id를 넣어?
A. 보통 넣지 않는다. id는 서버에서 생성되는 field인 경우가 많다.

Q. Create Request에 Partial을 쓰면 왜 위험해?
A. 필수 입력값까지 optional이 되어 API 계약이 약해질 수 있다.

Q. Update Request Type은 전부 optional로 만들면 돼?
A. 부분 수정이면 optional이 많을 수 있지만 API 계약에 따라 필수 field가 있을 수 있다.

Q. PATCH Request에는 Partial을 써도 돼?
A. 가능하지만 server-generated field가 포함되지 않도록 주의해야 한다.

Q. null과 undefined는 Update Request에서 의미가 같아?
A. 아니다. null은 값 삭제 의도로 쓰일 수 있고 undefined는 field 생략으로 처리될 수 있다.

Q. Query Parameter Type은 왜 필요해?
A. 검색 조건, 필터, 페이지 조건의 field 오타와 Type 오류를 줄이기 위해 필요하다.

Q. Query Parameter는 전부 string이야?
A. URL에서는 string으로 전달되지만 Frontend 내부 Type은 number나 literal union으로 모델링할 수 있다.

Q. undefined Query Parameter는 어떻게 처리해?
A. 보통 query string 생성 시 제외한다.

Q. Path Parameter Type은 뭐야?
A. URL 경로에 포함되는 id나 slug 같은 값을 정의하는 Type이다.

Q. API path id는 optional이야?
A. 대부분 required다. id가 없으면 특정 resource를 조회할 수 없다.

Q. React Router에서 받은 id는 number야?
A. 보통 string으로 들어온다. number id가 필요하면 Number 변환과 NaN 방어가 필요하다.

Q. Response Body Type이 뭐야?
A. Backend가 Frontend로 반환하는 JSON 데이터 구조를 정의하는 Type이다.

Q. API 날짜 field는 Date로 받아?
A. 대부분 JSON 응답에서는 string으로 받고 필요하면 Frontend에서 Date로 변환한다.

Q. nullable field를 Type에 안 쓰면 어떻게 돼?
A. null 값이 올 때 Runtime Error나 잘못된 UI 출력이 발생할 수 있다.

Q. ApiResponse<T>는 왜 Generic으로 만들어?
A. 공통 응답 구조는 같고 data Type만 API마다 다르기 때문이다.

Q. data가 없으면 ApiResponse<null>로 써도 돼?
A. Backend가 null을 반환한다면 가능하다. 실제 응답 정책을 확인해야 한다.

Q. Error Response도 ApiResponse<T>로 처리해?
A. Backend 구조에 따라 다르다. Error Response 구조가 다르면 별도 Type으로 분리하는 것이 좋다.

Q. List Response Type은 어떻게 써?
A. `ApiResponse<FestivalInfoResponse[]>`처럼 data Type에 배열을 넣는다.

Q. 빈 목록은 null로 와?
A. API 정책에 따라 다르지만 보통 빈 배열 `[]`이 권장된다. 실제 응답을 확인해야 한다.

Q. Slice Response Type은 언제 써?
A. 무한 스크롤이나 더보기처럼 다음 목록 존재 여부가 중요한 API에 사용한다.

Q. SliceResponse<T>의 content는 뭐야?
A. 현재 요청에서 받은 목록 데이터 배열이다.

Q. SliceResponse와 PageResponse 차이는?
A. Slice는 hasNext 중심이고 Page는 totalElements, totalPages 같은 전체 개수 정보를 포함한다.

Q. Page Response Type은 언제 써?
A. 전체 개수, 전체 페이지 수, 페이지 번호 UI가 필요한 목록 API에 사용한다.

Q. PageResponse<T>의 totalElements는 뭐야?
A. 전체 데이터 개수를 의미한다.

Q. 무한 스크롤에도 PageResponse를 써야 해?
A. 꼭 그렇지 않다. 무한 스크롤은 SliceResponse가 더 가볍고 적합할 수 있다.

Q. Error Response Type은 왜 필요해?
A. 실패 응답 구조를 Type으로 정의해 사용자 메시지와 validation 오류를 안정적으로 처리하기 위해 필요하다.

Q. errors는 왜 Record<string, string>으로 정의해?
A. field name과 error message의 key-value 구조를 표현하기 좋기 때문이다.

Q. 서버 오류 message를 그대로 보여줘도 돼?
A. 민감한 서버 detail이 포함될 수 있으므로 사용자용 메시지와 개발자 로그를 구분해야 한다.

Q. Validation Error Type은 뭐야?
A. Form field별 검증 오류 메시지를 표현하는 Error Response Type이다.

Q. FieldErrors는 어떻게 정의해?
A. 일반적으로 `Record<string, string>` 또는 Form field별 optional object로 정의한다.

Q. global error와 field error는 달라?
A. 다르다. global error는 전체 요청 오류이고 field error는 특정 입력 field 오류다.

Q. API Error Response와 Network Error는 같아?
A. 아니다. API Error Response는 서버가 반환한 오류 데이터이고 Network Error는 요청 자체 실패나 Runtime Error다.

Q. catch error는 항상 Error 객체야?
A. 아니다. JavaScript에서는 어떤 값이든 throw될 수 있으므로 unknown으로 보고 확인하는 것이 안전하다.

Q. 알 수 없는 오류는 어떻게 처리해?
A. fallback message를 제공하고 개발자 로그와 사용자 메시지를 구분한다.

Q. Backend enum 응답은 Frontend에서 어떻게 Type으로 표현해?
A. 문자열 enum 응답은 literal union으로 표현할 수 있다.

Q. Backend enum 값이 추가되면 뭐를 수정해야 해?
A. Frontend union Type, label map, switch 분기, 테스트를 함께 수정해야 한다.

Q. Role Type을 string으로 두면 안 돼?
A. 가능하지만 오타와 잘못된 권한 값을 막기 어렵기 때문에 literal union이 더 안전하다.

Q. success boolean과 AsyncStatus는 같아?
A. 아니다. success는 서버 응답 성공 여부이고 AsyncStatus는 Frontend 요청 진행 상태다.

Q. HTTP status와 ApiResponse.success는 같아?
A. 아니다. HTTP status는 네트워크 응답 코드이고 success는 response body field일 수 있다.

Q. API 요청 상태는 어떻게 Type으로 관리해?
A. `AsyncStatus` 또는 `ApiState<T>` 같은 literal union / discriminated union으로 관리할 수 있다.

Q. Response Type과 ViewModel Type은 뭐가 달라?
A. Response Type은 서버 응답 구조이고 ViewModel Type은 화면에서 쓰기 좋게 변환한 구조다.

Q. 날짜 string을 displayDate로 바꾸는 건 어디서 해?
A. Mapping Function에서 Runtime 변환으로 처리한다.

Q. imageUrl null fallback은 Type이 해줘?
A. 아니다. Mapping Function 또는 UI Rendering에서 fallback 처리를 해야 한다.

Q. Mapping Function은 왜 필요해?
A. API Response나 Form Data를 화면 또는 Request에 맞는 구조로 변환하기 위해 필요하다.

Q. input 값 숫자 변환은 Type이 해줘?
A. 아니다. `Number()` 같은 Runtime 변환과 validation이 필요하다.

Q. Mapping Function Return Type은 명시해야 해?
A. 권장한다. 변환 결과 구조를 명확히 검증할 수 있다.

Q. fetch response.json()은 Type을 자동으로 알아?
A. 아니다. Runtime Data이므로 TypeScript가 실제 구조를 검증하지 않는다.

Q. Fetch API Function Return Type은 어떻게 써?
A. `Promise<ApiResponse<T>>` 또는 `Promise<ResponseType>` 형태로 명시한다.

Q. response.ok check는 왜 필요해?
A. HTTP 실패 응답을 성공 데이터처럼 처리하지 않기 위해 필요하다.

Q. Axios에서 Response Type은 어떻게 지정해?
A. `api.get<ApiResponse<T>>(url)`처럼 Generic Type Parameter를 사용한다.

Q. Axios Generic을 쓰면 Runtime 검증도 돼?
A. 아니다. TypeScript Type 지정일 뿐 실제 응답 구조 검증은 아니다.

Q. Axios params도 Type으로 정의해야 해?
A. 정의하는 것이 좋다. 검색 조건이나 필터 field 오타를 줄일 수 있다.

Q. Request Type에서 가장 흔한 실수는?
A. Response Type을 억지로 재사용하거나 Create / Update / Query Type을 구분하지 않는 것이다.

Q. Form Data Type과 Request Type은 같아?
A. 항상 같지 않다. Form input은 string일 수 있고 Request에서는 number로 변환해야 할 수 있다.

Q. server-generated field를 Request에 넣어도 돼?
A. 보통 넣지 않는다. id, createdAt, updatedAt은 서버가 생성하는 field인 경우가 많다.

Q. Response Type에서 가장 흔한 실수는?
A. nullable field 누락, wrapper 구조 누락, 날짜를 Date로 단정하는 것이다.

Q. Type은 맞는데 화면에서 undefined가 나와?
A. 실제 API Response 구조와 Frontend Type 정의가 다를 수 있다. Network Response Body를 확인해야 한다.

Q. API Response Type과 ViewModel Type을 섞어도 돼?
A. 권장하지 않는다. 서버 구조와 화면 구조는 분리하는 것이 안전하다.

Q. Error Type에서 가장 흔한 실수는?
A. API Error Response와 Network Error를 구분하지 않고 catch error를 any로 처리하는 것이다.

Q. error.message를 바로 보여줘도 돼?
A. 민감한 정보가 포함될 수 있으므로 사용자용 메시지로 변환하거나 fallback을 제공하는 것이 좋다.

Q. TypeScript Part10의 핵심은 뭐야?
A. API Request / Response / Error Type을 Backend DTO와 정합성 있게 정의하고 nullable, wrapper, query, path parameter를 정확히 반영하는 것이다.

Q. TypeScript Part10 다음 문서는 뭐가 좋아?
A. React TypeScript Readiness 문서가 적합하다.
