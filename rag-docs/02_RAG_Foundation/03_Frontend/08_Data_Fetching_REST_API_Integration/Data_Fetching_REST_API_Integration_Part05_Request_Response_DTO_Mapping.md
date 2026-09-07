# Data Fetching & REST API Integration Part05 - Request / Response DTO Mapping

---

# 1. Request / Response DTO Mapping Overview

## 1.1 DTO Mapping 기본 개념

### [개념]

Request / Response DTO Mapping은 Frontend와 Backend가 주고받는 데이터 구조를 명확히 연결하는 작업이다.

Frontend Agent는 Backend API 명세를 기준으로 Request DTO, Response DTO, Params Type, ApiResponse Wrapper, Page Response, Slice Response를 구분해야 한다.

DTO Mapping의 목적은 API 요청과 응답 구조를 안정적으로 해석하고 UI에서 사용할 수 있는 데이터 형태로 연결하는 것이다.

기본 Flow:

```text
Backend API Spec
→ Request DTO 확인
→ Response DTO 확인
→ Frontend Type 정의
→ API Function 작성
→ Response Mapping
→ Component / Hook 사용
```

---

### [핵심]

DTO Mapping 핵심 키워드:

- Request DTO
- Response DTO
- Params Type
- Path Variable
- Query Parameter
- Request Body
- Response Body
- ApiResponse Wrapper
- Generic Response
- Page Response
- Slice Response
- Nullable Field
- Date String
- Enum Value
- Field Name Mapping
- TypeScript Type
- Response Shape Mismatch

DTO Mapping 목적:

- Request Body 필드명 일치
- Query Parameter 타입 명확화
- Response Body 구조 명확화
- ApiResponse Wrapper 처리
- Page / Slice content 위치 확인
- null 가능 필드 처리
- 날짜 / enum 값 처리
- Component 필드 접근 오류 감소
- `map is not a function` 오류 방지

---

### [실무]

2026 실무 기준에서 DTO Mapping은 단순히 `response.data`를 사용하는 작업이 아니다.

실무 기준:

- Backend Request DTO와 Frontend Request Type을 일치시킴
- Backend Response DTO와 Frontend Response Type을 일치시킴
- 요청 타입과 응답 타입을 분리
- Path Variable / Query Parameter / Request Body를 분리
- 공통 ApiResponse Wrapper 여부를 확인
- Page / Slice 응답 구조를 확인
- nullable field를 Type에 반영
- date string을 UI 표시용 format으로 변환
- enum string을 UI label로 mapping
- Network 탭에서 실제 Response Body를 최종 기준으로 확인

DTO Mapping 기본 예:

```typescript
export type ApiResponse<T> = {
  success: boolean;
  message: string;
  data: T;
};

export type ReviewCreateRequest = {
  festivalId: number;
  rating: number;
  content: string;
};

export type ReviewResponse = {
  reviewId: number;
  festivalId: number;
  rating: number;
  content: string;
  createdAt: string;
};
```

---

### [FAQ]

Q. DTO Mapping이 뭐야?
A. Backend API의 요청 / 응답 데이터 구조를 Frontend Type과 API 함수 반환 구조로 연결하는 작업이다.

Q. Request DTO와 Response DTO는 왜 나눠?
A. 요청과 응답의 필드가 다를 수 있기 때문이다. 생성 요청에는 없는 id, createdAt 같은 필드가 응답에는 포함될 수 있다.

Q. DTO Mapping에서 가장 중요한 것은 뭐야?
A. 실제 Backend 응답 구조, ApiResponse Wrapper, content 위치, null 가능성, 필드명을 정확히 맞추는 것이다.

Q. DTO Mapping은 어디서 확인해야 해?
A. Backend API 명세와 브라우저 Network 탭의 실제 Response Body를 함께 확인해야 한다.

---

# 2. Request DTO Rules

## 2.1 Request DTO 기본

### [개념]

Request DTO는 Frontend가 Backend로 보내는 요청 데이터 구조다.

POST / PUT / PATCH 요청의 Request Body, GET 요청의 Query Parameter, URL의 Path Variable이 Request DTO 설계와 연결된다.

---

### [핵심]

Request DTO 종류:

- Path Variable
- Query Parameter
- Request Body
- Header
- FormData
- Login Request
- Signup Request
- Create Request
- Update Request
- Search Params
- Pagination Params

Request DTO 기준:

- Backend Request DTO 필드명과 일치
- 필수값과 선택값 구분
- 숫자 / 문자열 / boolean 타입 확인
- 날짜 형식 확인
- enum 값 확인
- Request Body와 Query Parameter 혼동 금지
- Client Validation과 Backend Validation 구분

---

### [실무]

리뷰 작성 Request Type:

```typescript
export type ReviewCreateRequest = {
  festivalId: number;
  rating: number;
  content: string;
};
```

API 함수:

```typescript
export async function createReview(
  requestBody: ReviewCreateRequest,
): Promise<ReviewResponse> {
  const response = await authApi.post<ApiResponse<ReviewResponse>>(
    "/reviews",
    requestBody,
  );

  return response.data.data;
}
```

검색 Params Type:

```typescript
export type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  themeCode?: string;
  startDate?: string;
  endDate?: string;
  page?: number;
  size?: number;
  sort?: string;
};
```

검색 API 함수:

```typescript
export async function searchFestivals(
  params: FestivalSearchParams,
): Promise<PageResponse<FestivalSummaryResponse>> {
  const response = await publicApi.get<
    ApiResponse<PageResponse<FestivalSummaryResponse>>
  >("/festivals/search", {
    params: cleanParams(params),
  });

  return response.data.data;
}
```

주의:

- Request DTO에 UI 전용 필드를 그대로 보내지 않음
- Form State와 Request DTO는 다를 수 있음
- 비밀번호 확인 값은 Backend가 요구하지 않으면 제거
- 파일 업로드는 JSON Request DTO가 아니라 FormData 사용
- GET 조회 조건은 Request Body가 아니라 Query Parameter 사용

---

### [FAQ]

Q. Request DTO는 뭐야?
A. Frontend가 Backend로 보내는 요청 데이터 구조다.

Q. Form State를 그대로 Request Body로 보내도 돼?
A. 항상 그렇지 않다. UI 전용 필드나 검증용 필드는 제거하고 Backend DTO가 요구하는 필드만 보내야 한다.

Q. GET 요청의 검색 조건도 Request DTO야?
A. 넓게 보면 요청 데이터 구조지만 보통 Request Body가 아니라 Params Type으로 분리한다.

Q. Request DTO 필드명은 Frontend 마음대로 정해도 돼?
A. 아니다. Backend Request DTO가 기대하는 필드명과 타입에 맞춰야 한다.

---

# 3. Response DTO Rules

## 3.1 Response DTO 기본

### [개념]

Response DTO는 Backend가 Frontend로 내려주는 응답 데이터 구조다.

Frontend는 Response DTO를 기준으로 화면에 표시할 필드, 상태 갱신에 필요한 필드, 다음 요청에 사용할 id 값을 얻는다.

---

### [핵심]

Response DTO 포함 대상:

- id
- title
- content
- status
- createdAt
- updatedAt
- imageUrl
- nullable field
- enum value
- nested object
- list item
- page metadata
- slice metadata

Response DTO 기준:

- 실제 응답 필드명과 일치
- null 가능성 반영
- 날짜는 보통 string
- enum은 보통 string
- 숫자 id는 number
- 리스트 응답과 상세 응답 구분
- Backend DTO 변경 시 Frontend Type 동기화

---

### [실무]

축제 목록 Response Type:

```typescript
export type FestivalSummaryResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  regionName: string;
  eventStartDate: string | null;
  eventEndDate: string | null;
  averageRating: number | null;
};
```

축제 상세 Response Type:

```typescript
export type FestivalDetailResponse = {
  festivalId: number;
  title: string;
  description: string | null;
  imageUrls: string[];
  regionName: string;
  address: string | null;
  eventStartDate: string | null;
  eventEndDate: string | null;
  averageRating: number | null;
  likeCount: number;
  favoriteCount: number;
};
```

리뷰 Response Type:

```typescript
export type ReviewResponse = {
  reviewId: number;
  festivalId: number;
  userNickname: string;
  rating: number;
  content: string;
  createdAt: string;
  updatedAt: string | null;
};
```

주의:

- 목록 Response와 상세 Response를 무리하게 하나로 합치지 않음
- `imageUrl` 단일 값과 `imageUrls` 배열을 구분
- null 가능 필드는 `| null` 반영
- optional field와 nullable field를 구분
- 실제 응답 구조가 바뀌면 Type과 Component 접근 경로 수정

---

### [FAQ]

Q. Response DTO는 뭐야?
A. Backend가 Frontend에 응답으로 내려주는 데이터 구조다.

Q. 목록 Response와 상세 Response는 나눠야 해?
A. 나누는 것이 좋다. 목록은 요약 정보, 상세는 더 많은 필드를 포함하는 경우가 많다.

Q. null 가능 필드는 Type에 어떻게 반영해?
A. `string | null`, `number | null`처럼 null 가능성을 명시한다.

Q. Backend 응답 필드명이 바뀌면 어떻게 돼?
A. Frontend Type, API mapping, Component에서 사용하는 필드명을 함께 수정해야 한다.

---

# 4. ApiResponse Wrapper Rules

## 4.1 공통 응답 Wrapper 기준

### [개념]

ApiResponse Wrapper는 Backend가 모든 응답을 일정한 구조로 감싸서 내려주는 공통 응답 형식이다.

예:

```json
{
  "success": true,
  "message": "조회 성공",
  "data": {
    "festivalId": 1,
    "title": "Spring Festival"
  }
}
```

Axios 기준 실제 데이터 접근은 보통 `response.data.data`가 된다.

---

### [핵심]

ApiResponse Wrapper 구성:

- success
- message
- data
- errors
- timestamp
- status
- code

Frontend 확인 대상:

- `response.data`
- `response.data.data`
- `response.data.message`
- `response.data.errors`
- success boolean
- error response shape
- data nullable 여부

주의:

- Axios의 `response.data`와 Backend Wrapper의 `data`를 혼동하지 않음
- Wrapper unwrap 기준을 프로젝트 전체에서 통일
- 성공 응답과 실패 응답 구조가 다를 수 있음
- Error Response의 `errors` 필드 처리 기준 필요
- 204 No Content는 Wrapper가 없을 수 있음

---

### [실무]

공통 ApiResponse Type:

```typescript
export type ApiResponse<T> = {
  success: boolean;
  message: string;
  data: T;
};
```

Validation Error 포함 Type:

```typescript
export type ApiErrorResponse = {
  success: false;
  message: string;
  errors?: Record<string, string>;
};
```

API 함수 unwrap:

```typescript
export async function getFestivalDetail(
  festivalId: number,
): Promise<FestivalDetailResponse> {
  const response = await publicApi.get<ApiResponse<FestivalDetailResponse>>(
    `/festivals/${festivalId}`,
  );

  return response.data.data;
}
```

Wrapper 전체가 필요한 경우:

```typescript
export async function createReview(
  requestBody: ReviewCreateRequest,
): Promise<ApiResponse<ReviewResponse>> {
  const response = await authApi.post<ApiResponse<ReviewResponse>>(
    "/reviews",
    requestBody,
  );

  return response.data;
}
```

선택 기준:

```text
Component가 message 필요 없음 → data만 반환
Component가 success/message 필요 → ApiResponse 전체 반환
```

---

### [FAQ]

Q. response.data.data는 왜 나와?
A. Axios의 `response.data` 안에 Backend ApiResponse의 `data` 필드가 다시 있기 때문이다.

Q. ApiResponse<T>는 왜 써?
A. Backend 공통 응답 wrapper를 TypeScript Generic으로 표현하기 위해 사용한다.

Q. API 함수는 data만 반환해야 해?
A. 프로젝트 기준에 따라 다르다. 대부분 화면에서는 data만 필요하지만 성공 메시지가 필요하면 wrapper 전체를 반환할 수 있다.

Q. 성공 응답과 실패 응답 Type은 같아?
A. 항상 같지 않다. 실패 응답에는 errors, code, timestamp 같은 필드가 추가될 수 있다.

---

# 5. Page Response Mapping Rules

## 5.1 Page Response 기본

### [개념]

Page Response는 전체 데이터 개수와 전체 페이지 정보를 포함하는 페이지네이션 응답 구조다.

Spring Pageable 기반 API에서 자주 사용한다.

---

### [핵심]

Page Response 주요 필드:

- content
- number
- size
- totalPages
- totalElements
- first
- last
- sort
- pageable
- numberOfElements

Frontend 사용 대상:

- 페이지 버튼
- 전체 개수 표시
- 현재 페이지 표시
- 다음 / 이전 버튼 제어
- 검색 조건 변경 시 page reset

주의:

- Spring Pageable은 보통 0-based
- UI page는 1-based로 표시 가능
- `content`가 실제 목록 배열
- Page 객체 전체가 필요한 경우 content만 반환하지 않음
- Backend Page Response shape를 실제 응답으로 확인

---

### [실무]

PageResponse Type:

```typescript
export type PageResponse<T> = {
  content: T[];
  number: number;
  size: number;
  totalPages: number;
  totalElements: number;
  first: boolean;
  last: boolean;
};
```

ApiResponse + PageResponse:

```typescript
export async function getFestivals(
  params: FestivalSearchParams,
): Promise<PageResponse<FestivalSummaryResponse>> {
  const response = await publicApi.get<
    ApiResponse<PageResponse<FestivalSummaryResponse>>
  >("/festivals", {
    params,
  });

  return response.data.data;
}
```

Component 사용:

```typescript
const pageData = await getFestivals({ page: 0, size: 20 });

setFestivals(pageData.content);
setPageInfo({
  currentPage: pageData.number,
  totalPages: pageData.totalPages,
  totalElements: pageData.totalElements,
});
```

UI page 변환:

```typescript
export function toBackendPage(uiPage: number) {
  return Math.max(uiPage - 1, 0);
}

export function toUiPage(backendPage: number) {
  return backendPage + 1;
}
```

---

### [FAQ]

Q. Page Response에서 실제 목록은 어디에 있어?
A. 보통 `content` 필드에 실제 목록 배열이 들어 있다.

Q. Spring Pageable page는 0부터 시작해?
A. 일반적으로 0-based다. UI에서 1부터 보여주면 요청 시 변환이 필요할 수 있다.

Q. Page Response는 content만 반환해도 돼?
A. 페이지 버튼이나 전체 개수가 필요하면 totalPages, totalElements도 필요하므로 Page 객체 전체를 반환하는 것이 좋다.

Q. 검색 조건이 바뀌면 page는 어떻게 해?
A. 대부분 1페이지 또는 backend page 0으로 reset하는 것이 좋다.

---

# 6. Slice Response Mapping Rules

## 6.1 Slice Response 기본

### [개념]

Slice Response는 전체 개수보다 다음 페이지 존재 여부를 중심으로 데이터를 내려주는 응답 구조다.

Infinite Scroll, Load More, 알림 목록, 채팅 목록, 리뷰 더보기 UI에 적합하다.

---

### [핵심]

Slice Response 주요 필드:

- content
- number
- size
- first
- last
- hasNext
- numberOfElements

Frontend 사용 대상:

- Infinite Scroll
- Load More Button
- 다음 페이지 존재 여부
- 목록 append
- 중복 요청 방지
- 마지막 페이지 감지

주의:

- 전체 개수와 totalPages가 없을 수 있음
- 기존 목록에 새 content append
- 검색 조건 변경 시 목록 초기화
- hasNext / last 기준 통일
- page 증가 타이밍 주의
- 중복 데이터 방지

---

### [실무]

SliceResponse Type:

```typescript
export type SliceResponse<T> = {
  content: T[];
  number: number;
  size: number;
  first: boolean;
  last: boolean;
  hasNext: boolean;
};
```

알림 목록 API:

```typescript
export async function getNotifications(
  params: NotificationListParams,
): Promise<SliceResponse<NotificationResponse>> {
  const response = await authApi.get<
    ApiResponse<SliceResponse<NotificationResponse>>
  >("/notifications", {
    params,
  });

  return response.data.data;
}
```

Load More 처리:

```typescript
const sliceData = await getNotifications({ page, size: 20 });

setNotifications((prev) => [...prev, ...sliceData.content]);
setHasNext(sliceData.hasNext);
setPage(sliceData.number + 1);
```

Load More Flow:

```text
Initial Load
→ Render Content
→ User Click More or Scroll Bottom
→ Request Next Page
→ Append Content
→ Stop if hasNext false
```

---

### [FAQ]

Q. Slice Response는 언제 써?
A. 전체 개수보다 다음 페이지 존재 여부가 중요한 더보기, 무한 스크롤, 채팅, 알림 목록에 적합하다.

Q. Page와 Slice 차이는?
A. Page는 전체 개수와 totalPages를 제공하고 Slice는 다음 페이지 존재 여부 중심이라 더보기나 무한 스크롤에 적합하다.

Q. Infinite Scroll에서 content는 어떻게 처리해?
A. 기존 목록을 교체하지 않고 새 content를 append한다.

Q. Infinite Scroll에서 중복 데이터가 생겨?
A. page 증가 타이밍, 중복 요청, 검색 조건 변경 시 초기화 누락을 확인해야 한다.

---

# 7. List / Detail DTO Separation Rules

## 7.1 목록 DTO와 상세 DTO 분리

### [개념]

List DTO와 Detail DTO는 같은 Resource라도 목적이 다르다.

목록 화면은 카드나 리스트 표시용 요약 데이터가 필요하고, 상세 화면은 전체 설명, 이미지 목록, 통계, 상세 메타데이터가 필요하다.

---

### [핵심]

List DTO 특징:

- id
- title
- thumbnail
- short description
- summary field
- status
- date
- count
- list item optimized

Detail DTO 특징:

- id
- title
- full description
- image list
- detail metadata
- related data
- statistics
- permission flags
- owner info

분리 이유:

- 목록 응답 크기 감소
- 상세 화면 필드 확장 가능
- 불필요한 데이터 전송 방지
- Component 필드 접근 명확화
- RAG 검색 시 list/detail 구분 강화

---

### [실무]

List DTO:

```typescript
export type FestivalSummaryResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  regionName: string;
  eventStartDate: string | null;
};
```

Detail DTO:

```typescript
export type FestivalDetailResponse = {
  festivalId: number;
  title: string;
  description: string | null;
  imageUrls: string[];
  regionName: string;
  address: string | null;
  eventStartDate: string | null;
  eventEndDate: string | null;
  homepageUrl: string | null;
  likeCount: number;
  favoriteCount: number;
  averageRating: number | null;
};
```

API 함수 분리:

```typescript
export async function getFestivals(
  params: FestivalSearchParams,
): Promise<PageResponse<FestivalSummaryResponse>> {
  const response = await publicApi.get<
    ApiResponse<PageResponse<FestivalSummaryResponse>>
  >("/festivals", { params });

  return response.data.data;
}

export async function getFestivalDetail(
  festivalId: number,
): Promise<FestivalDetailResponse> {
  const response = await publicApi.get<ApiResponse<FestivalDetailResponse>>(
    `/festivals/${festivalId}`,
  );

  return response.data.data;
}
```

---

### [FAQ]

Q. 목록 DTO와 상세 DTO는 왜 나눠?
A. 목록은 요약 정보만 필요하고 상세는 더 많은 필드가 필요하므로 응답 크기와 역할을 분리하기 위해 나눈다.

Q. 같은 Festival이면 Type 하나만 써도 돼?
A. 가능은 하지만 목록과 상세의 필드가 다르면 optional이 많아지고 오류 가능성이 커진다.

Q. 목록에서 상세 필드를 쓰고 싶으면 어떻게 해?
A. Backend 목록 응답에 해당 필드가 있는지 확인해야 한다. 없으면 상세 API를 호출하거나 목록 DTO를 확장해야 한다.

Q. Detail DTO에 imageUrls가 있는데 List DTO에는 imageUrl만 있어도 돼?
A. 가능하다. 목록은 대표 이미지 하나, 상세는 이미지 배열을 사용하는 식으로 분리할 수 있다.

---

# 8. Nullable Field Rules

## 8.1 Nullable Field 처리 기준

### [개념]

Nullable Field는 Backend 응답에서 `null`이 될 수 있는 필드다.

Frontend는 nullable field를 Type에 반영하고 UI에서 안전하게 처리해야 한다.

---

### [핵심]

Nullable 대상 예:

- imageUrl
- description
- address
- homepageUrl
- averageRating
- eventStartDate
- eventEndDate
- updatedAt
- deletedAt
- optional profile image
- optional location

처리 기준:

- `string | null`
- `number | null`
- `Date` 직접 사용보다 string 후 변환
- fallback UI 제공
- null check
- optional chaining 남용 주의
- null과 undefined 구분

주의:

- Backend가 null을 줄 수 있으면 Type에 반영
- 빈 문자열과 null은 다름
- null 값을 그대로 렌더링하지 않음
- 숫자 null은 0과 다름
- 평균 평점 null과 0점은 다름

---

### [실무]

Nullable Type:

```typescript
export type FestivalSummaryResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  averageRating: number | null;
};
```

UI fallback:

```tsx
function FestivalCard({ festival }: { festival: FestivalSummaryResponse }) {
  return (
    <article>
      <h3>{festival.title}</h3>
      <p>{festival.averageRating ?? "평점 없음"}</p>
      {festival.imageUrl ? (
        <img src={festival.imageUrl} alt={festival.title} />
      ) : (
        <div>이미지 없음</div>
      )}
    </article>
  );
}
```

날짜 nullable 처리:

```typescript
export function formatDate(dateString: string | null) {
  if (!dateString) {
    return "날짜 미정";
  }

  return dateString.slice(0, 10);
}
```

주의:

- `averageRating || "평점 없음"`은 0도 fallback 처리할 수 있으므로 주의
- null 가능 필드에 바로 `.toFixed()` 호출 금지
- imageUrl null일 때 broken image 방지
- TypeScript strictNullChecks 활성화 권장

---

### [FAQ]

Q. null 가능 필드는 Type에 어떻게 써?
A. `string | null`, `number | null`처럼 명시한다.

Q. averageRating이 null이면 0점이야?
A. 아니다. null은 아직 평점이 없다는 뜻일 수 있고 0은 실제 값일 수 있다.

Q. optional chaining만 쓰면 안전해?
A. 오류는 줄일 수 있지만 UI fallback이 없으면 빈 화면이 될 수 있으므로 명시적 처리가 좋다.

Q. null과 undefined는 같아?
A. 다르다. Backend JSON 응답에서는 보통 값이 없을 때 null을 명시적으로 내려줄 수 있다.

---

# 9. Date / Time Mapping Rules

## 9.1 날짜 응답 처리 기준

### [개념]

Backend JSON 응답의 날짜와 시간은 보통 문자열로 전달된다.

Frontend는 Date 객체로 바로 받는 것이 아니라 string으로 받은 뒤 필요에 따라 formatting한다.

---

### [핵심]

날짜 관련 필드:

- createdAt
- updatedAt
- deletedAt
- eventStartDate
- eventEndDate
- startDate
- endDate
- targetMonth
- LocalDate
- LocalDateTime
- ISO string

처리 기준:

- Response Type은 string
- nullable date는 `string | null`
- 화면 표시 전 formatting
- API 요청 날짜 형식은 Backend 기준과 일치
- timezone 이슈 확인
- 월 단위 요청은 `yyyy-MM` 형식 가능
- 일 단위 요청은 `yyyy-MM-dd` 형식 가능

주의:

- JSON은 Date 객체를 직접 전달하지 않음
- `new Date()` 변환 시 timezone 변동 가능
- 문자열 자르기와 Date formatting 기준 선택
- Backend LocalDate / LocalDateTime 형식 확인
- targetMonth 형식 통일

---

### [실무]

Response Type:

```typescript
export type FestivalSummaryResponse = {
  festivalId: number;
  title: string;
  eventStartDate: string | null;
  eventEndDate: string | null;
};
```

날짜 표시 함수:

```typescript
export function formatDate(dateString: string | null) {
  if (!dateString) {
    return "날짜 미정";
  }

  return dateString.slice(0, 10);
}
```

월별 조회 Params:

```typescript
export type MonthlyFestivalParams = {
  targetMonth?: string;
};
```

월별 API:

```typescript
export async function getMonthlyFestivals(
  params: MonthlyFestivalParams,
): Promise<FestivalSummaryResponse[]> {
  const response = await publicApi.get<ApiResponse<FestivalSummaryResponse[]>>(
    "/calendar/monthly",
    {
      params: cleanParams(params),
    },
  );

  return response.data.data;
}
```

요청 예:

```text
GET /api/calendar/monthly?targetMonth=2026-07
```

---

### [FAQ]

Q. 날짜 타입은 Date로 받아?
A. JSON 응답은 보통 문자열로 받는다. 필요하면 Frontend에서 Date 객체나 formatting 함수로 변환한다.

Q. LocalDateTime은 Frontend에서 어떤 타입이야?
A. JSON으로 받으면 보통 string이다.

Q. targetMonth는 어떤 형식으로 보내?
A. Backend 명세에 따라 다르지만 월별 조회에서는 보통 `yyyy-MM` 형식을 사용할 수 있다.

Q. 날짜가 하루 밀려 보이면 뭘 확인해?
A. timezone 변환, Date 객체 변환 방식, Backend LocalDate / LocalDateTime 형식을 확인해야 한다.

---

# 10. Enum Mapping Rules

## 10.1 Enum Response Mapping 기준

### [개념]

Enum Mapping은 Backend enum 값을 Frontend에서 표시명, 색상, 필터 옵션, 조건 분기 등에 사용하는 방식이다.

Backend enum은 JSON 응답에서 보통 문자열로 전달된다.

---

### [핵심]

Enum 사용 대상:

- status
- category
- role
- notificationType
- postCategory
- certStatus
- paymentStatus
- reviewStatus

처리 기준:

- TypeScript union type 사용 가능
- enum value와 display label 분리
- Backend enum 값과 Frontend type 동기화
- 알 수 없는 enum 값 fallback 처리
- UI label mapping 함수 작성
- filter option과 enum value 일치

주의:

- Backend enum 이름 변경 시 Frontend mapping 수정
- label을 API 요청값으로 보내지 않음
- enum value와 화면 표시 한글명을 혼동하지 않음
- ROLE_USER / USER naming 불일치 주의

---

### [실무]

Union Type:

```typescript
export type NotificationType = "SYSTEM" | "FESTIVAL_START" | "REVIEW" | "CHAT";
```

Label Mapping:

```typescript
export const notificationTypeLabels: Record<NotificationType, string> = {
  SYSTEM: "시스템",
  FESTIVAL_START: "축제 시작",
  REVIEW: "리뷰",
  CHAT: "채팅",
};
```

사용:

```tsx
function NotificationTypeBadge({ type }: { type: NotificationType }) {
  return <span>{notificationTypeLabels[type] ?? "알 수 없음"}</span>;
}
```

카테고리 Filter Params:

```typescript
export type FestivalSearchParams = {
  themeCode?: string;
  regionCode?: string;
  page?: number;
  size?: number;
};
```

주의:

- enum value는 Backend가 기대하는 원본 문자열 사용
- 화면 label은 Frontend에서 별도 mapping
- Type에 없는 값이 올 수 있는 경우 fallback 설계
- API 명세 변경 시 enum mapping 검수

---

### [FAQ]

Q. Backend enum은 Frontend에서 어떤 타입으로 받아?
A. JSON 응답에서는 보통 string으로 받으며 TypeScript에서는 union type으로 표현할 수 있다.

Q. enum label은 Backend 값 그대로 보여줘도 돼?
A. 가능하지만 사용자 화면에는 label mapping을 통해 한글 표시명으로 보여주는 것이 좋다.

Q. enum value와 label은 뭐가 달라?
A. enum value는 API와 로직에서 사용하는 값이고 label은 사용자에게 보여주는 표시명이다.

Q. enum 값이 추가되면 Frontend도 수정해야 해?
A. 표시 label, filter option, 조건 분기, TypeScript union type을 함께 확인해야 한다.

---

# 11. Nested Object Mapping Rules

## 11.1 Nested Response 처리 기준

### [개념]

Nested Object Mapping은 Response DTO 안에 객체나 배열이 중첩되어 있는 구조를 Frontend에서 처리하는 방식이다.

예:

```json
{
  "festivalId": 1,
  "title": "Festival",
  "region": {
    "code": "11",
    "name": "서울"
  },
  "images": [
    {
      "imageId": 1,
      "imageUrl": "https://example.com/image.jpg"
    }
  ]
}
```

---

### [핵심]

Nested Mapping 대상:

- nested object
- nested array
- image list
- region object
- user summary
- review list
- comment list
- owner info
- metadata

처리 기준:

- 중첩 Type 분리
- null 가능성 확인
- 배열 기본값 처리
- optional chaining보다 명확한 fallback
- 필요한 경우 flat mapping
- UI Component props에 맞게 변환 가능

주의:

- 중첩 객체가 null일 수 있음
- 배열이 undefined일 수 있음
- Component에서 깊은 접근 반복 금지
- API 함수나 Hook에서 화면용 구조로 가공 가능
- Backend 응답 shape 변경에 취약

---

### [실무]

Nested Type 분리:

```typescript
export type RegionResponse = {
  code: string;
  name: string;
};

export type FestivalImageResponse = {
  imageId: number;
  imageUrl: string;
  sortOrder: number;
};

export type FestivalDetailResponse = {
  festivalId: number;
  title: string;
  region: RegionResponse | null;
  images: FestivalImageResponse[];
};
```

UI용 flat mapping:

```typescript
export function toFestivalDetailViewModel(response: FestivalDetailResponse) {
  return {
    festivalId: response.festivalId,
    title: response.title,
    regionName: response.region?.name ?? "지역 미정",
    imageUrls: response.images.map((image) => image.imageUrl),
  };
}
```

Hook에서 변환:

```typescript
const detail = await getFestivalDetail(festivalId);
const viewModel = toFestivalDetailViewModel(detail);

setFestival(viewModel);
```

주의:

- API Response Type과 View Model Type을 구분 가능
- 변환 함수는 테스트 가능하게 분리
- 배열 응답이 null인지 빈 배열인지 Backend 기준 확인
- `images.map` 호출 전 images가 배열인지 확인

---

### [FAQ]

Q. 중첩 객체는 Type을 따로 만들어야 해?
A. 재사용되거나 구조가 복잡하면 RegionResponse, ImageResponse처럼 따로 분리하는 것이 좋다.

Q. API 응답을 화면용으로 바꿔도 돼?
A. 가능하다. API Response Type과 View Model을 구분하면 Component가 더 단순해질 수 있다.

Q. images가 null이면 map 오류가 나?
A. 그렇다. 배열이 null일 수 있다면 fallback으로 빈 배열을 사용하거나 Type에 null을 반영해야 한다.

Q. 중첩 필드를 Component에서 계속 접근해도 돼?
A. 가능하지만 깊은 접근이 반복되면 Hook이나 mapping 함수에서 화면용 구조로 변환하는 것이 좋다.

---

# 12. Error Response DTO Rules

## 12.1 Error Response Mapping 기준

### [개념]

Error Response DTO는 API 요청 실패 시 Backend가 내려주는 오류 응답 구조다.

Frontend는 Error Response를 기준으로 사용자 메시지, field error, global error를 구분할 수 있다.

---

### [핵심]

Error Response 포함 가능 필드:

- success
- message
- errors
- code
- status
- timestamp
- path
- field
- reason

처리 대상:

- 400 Bad Request
- 401 Unauthenticated
- 403 Forbidden
- 404 Not Found
- 409 Conflict
- 422 Validation Error
- 500 Server Error

주의:

- 서버 오류 원문 직접 노출 금지
- Validation Error는 field별 표시 가능
- 401 / 403 구분
- 500은 일반 메시지 표시
- 개발 로그와 사용자 메시지 분리
- Error Response shape도 실제 Network Response로 확인

---

### [실무]

Error Response Type:

```typescript
export type ApiErrorResponse = {
  success: false;
  message: string;
  errors?: Record<string, string>;
  code?: string;
  status?: number;
};
```

Error Mapper:

```typescript
export function getApiErrorMessage(error: unknown): string {
  if (axios.isAxiosError<ApiErrorResponse>(error)) {
    const status = error.response?.status;
    const message = error.response?.data?.message;

    if (status === 401) {
      return "로그인이 필요합니다.";
    }

    if (status === 403) {
      return "접근 권한이 없습니다.";
    }

    if (status === 404) {
      return "요청한 데이터를 찾을 수 없습니다.";
    }

    if (status && status >= 500) {
      return "서버 오류가 발생했습니다.";
    }

    return message ?? "요청 값을 확인해 주세요.";
  }

  return "요청 처리 중 문제가 발생했습니다.";
}
```

Field Error 추출:

```typescript
export function getFieldErrors(error: unknown): Record<string, string> {
  if (axios.isAxiosError<ApiErrorResponse>(error)) {
    return error.response?.data?.errors ?? {};
  }

  return {};
}
```

---

### [FAQ]

Q. Error Response DTO도 Type이 필요해?
A. 필요하다. field error, message, code 구조를 안정적으로 처리할 수 있다.

Q. 서버 에러 메시지를 그대로 보여줘도 돼?
A. 민감한 정보가 포함될 수 있으므로 사용자 메시지와 개발자 로그를 구분하는 것이 좋다.

Q. Validation Error는 어떻게 보여줘?
A. field별 오류는 해당 input 근처에 표시하고 공통 오류는 form 상단에 표시하는 것이 좋다.

Q. Error Response 구조는 어디서 확인해?
A. Network 탭의 Response Body와 Backend 예외 처리 응답 명세를 확인한다.

---

# 13. Form State to Request DTO Rules

## 13.1 Form State 변환 기준

### [개념]

Form State to Request DTO는 화면 입력 상태를 Backend Request DTO 구조로 변환하는 작업이다.

Form State에는 UI 전용 필드, 임시 값, 확인용 값이 포함될 수 있으므로 그대로 Request Body로 보내지 않는 것이 좋다.

---

### [핵심]

Form State 포함 가능:

- input value
- confirm password
- checkbox state
- temporary file preview
- UI-only selected label
- error state
- touched state
- dirty state

Request DTO 포함 대상:

- Backend가 요구하는 필드
- 검증이 끝난 값
- 필요한 id
- 필요한 enum value
- 필요한 date string
- 필요한 file FormData

주의:

- UI 전용 필드 제거
- label이 아니라 value 전송
- 숫자 문자열 변환
- trim 처리 기준
- 빈 문자열과 null 처리 기준
- file은 JSON이 아니라 FormData 사용 가능

---

### [실무]

Form State:

```typescript
type ReviewFormState = {
  rating: string;
  content: string;
  isSpoilerChecked: boolean;
  errorMessage: string;
};
```

Request DTO:

```typescript
export type ReviewCreateRequest = {
  festivalId: number;
  rating: number;
  content: string;
};
```

변환 함수:

```typescript
export function toReviewCreateRequest(
  festivalId: number,
  formState: ReviewFormState,
): ReviewCreateRequest {
  return {
    festivalId,
    rating: Number(formState.rating),
    content: formState.content.trim(),
  };
}
```

Submit Flow:

```text
Form Submit
→ Client Validation
→ Form State to Request DTO
→ API Function
→ Backend Validation
→ Response DTO
→ UI Update
```

주의:

- 변환 함수는 API 함수 밖에서 분리 가능
- Request DTO 변환 후 validation 가능
- `Number("")`는 0이 될 수 있으므로 빈 값 검증 우선
- checkbox UI 값이 Backend에 필요 없으면 제거
- 확인용 passwordConfirm은 Backend가 요구하지 않으면 제거

---

### [FAQ]

Q. Form State를 그대로 Request Body로 보내도 돼?
A. 권장하지 않는다. UI 전용 필드와 검증용 필드를 제거하고 Backend Request DTO에 맞게 변환해야 한다.

Q. rating input 값은 string인데 Request DTO는 number면 어떻게 해?
A. 요청 전 Number 변환을 하고 NaN이나 빈 값 검증을 해야 한다.

Q. passwordConfirm도 Backend로 보내야 해?
A. Backend 명세에 따라 다르지만 보통 Frontend 검증용이면 Request DTO에서 제거한다.

Q. trim은 어디서 해?
A. 제출 직전 Request DTO 변환 단계에서 처리할 수 있다. 단, 의도적으로 공백이 필요한 필드는 주의한다.

---

# 14. DTO Mapping Validation Rules

## 14.1 DTO Mapping 검증 기준

### [개념]

DTO Mapping Validation은 Request DTO와 Response DTO가 Backend API 명세 및 실제 Network Request / Response와 일치하는지 검증하는 과정이다.

---

### [핵심]

검증 대상:

- Request URL
- HTTP Method
- Path Variable
- Query Parameter
- Request Body
- Request Header
- Response Body
- ApiResponse Wrapper
- content 위치
- null field
- enum value
- date format
- field error shape
- TypeScript Type

검증 도구:

- Backend API Spec
- Swagger UI
- Postman
- Browser Network Tab
- TypeScript Compiler
- Console Debug
- Mock Data
- Unit Test

---

### [실무]

검증 Flow:

```text
API Spec 확인
→ Request DTO Type 확인
→ API Function 인자 확인
→ Network Request Payload 확인
→ Response Body 확인
→ Response Type 확인
→ Component Field Access 확인
→ Error Response 확인
```

Request 검증 예:

```text
createReview(requestBody)
→ POST /api/reviews
→ Authorization Header 포함
→ Request Body: festivalId, rating, content
→ Backend Validation 통과
```

Response 검증 예:

```text
GET /api/festivals
→ ApiResponse<PageResponse<FestivalSummaryResponse>>
→ response.data.data.content 확인
→ content 배열 확인
→ totalPages 확인
```

TypeScript 검증:

```typescript
const pageData: PageResponse<FestivalSummaryResponse> =
  await getFestivals(params);

pageData.content.map((festival) => festival.title);
```

주의:

- TypeScript Type이 맞아도 실제 API 응답이 다르면 런타임 오류 발생
- Swagger 예시와 실제 응답이 다를 수 있음
- Network Response Body를 최종 기준으로 확인
- Mock Data와 실제 API Data shape를 동기화

---

### [FAQ]

Q. DTO Mapping은 어떻게 검수해?
A. API 명세, 실제 Network Request / Response, TypeScript Type, Component 접근 경로를 함께 비교한다.

Q. TypeScript 에러가 없으면 응답 구조도 맞는 거야?
A. 아니다. TypeScript Type은 개발자가 선언한 구조이므로 실제 API 응답과 다를 수 있다.

Q. Swagger 예시와 실제 응답이 다르면 뭘 기준으로 해?
A. 실제 Backend 응답과 Backend 팀 확인을 기준으로 Type과 mapping을 수정해야 한다.

Q. Response Body는 어디서 확인해?
A. 브라우저 개발자 도구 Network 탭에서 확인한다.

---

# 15. Response Shape Mismatch Troubleshooting

## 15.1 Response Shape Mismatch 기준

### [개념]

Response Shape Mismatch는 Frontend가 예상한 응답 구조와 실제 Backend 응답 구조가 달라 발생하는 문제다.

DTO Mapping 오류의 대표적인 증상이다.

---

### [핵심]

증상:

- Cannot read properties of undefined
- map is not a function
- 화면에 데이터가 안 나옴
- response.data.data 혼동
- content 위치 혼동
- null field 처리 오류
- enum label 표시 실패
- 날짜 표시 오류

원인:

- ApiResponse Wrapper 확인 누락
- Page / Slice content 위치 확인 누락
- 배열을 기대했는데 객체 응답
- 객체를 기대했는데 배열 응답
- null 가능성 미처리
- Backend DTO 변경
- Response Interceptor unwrap 기준 혼용
- Mock Data와 실제 응답 차이

---

### [실무]

Debug Flow:

```text
UI 데이터 오류
→ Network Response Body 확인
→ response.data 구조 확인
→ ApiResponse wrapper 확인
→ Page / Slice content 위치 확인
→ TypeScript Type 확인
→ API Function return 확인
→ Component 접근 경로 수정
```

문제 예:

```text
문제: map is not a function
예상: festivals가 배열
실제: festivals가 PageResponse 객체
해결: festivals = pageData.content
```

문제 예:

```text
문제: response.data.data가 undefined
원인: Response Interceptor에서 이미 response.data를 반환
해결: unwrap 기준 확인 후 body.data로 수정
```

문제 예:

```text
문제: Cannot read properties of null
원인: imageUrl 또는 region이 null
해결: null 가능 Type 반영 및 fallback UI 추가
```

주의:

- optional chaining만으로 문제를 숨기지 않음
- 실제 Response Body를 먼저 확인
- Component에서 사용하는 값이 배열인지 객체인지 확인
- API 함수 반환 기준을 문서화

---

### [FAQ]

Q. map is not a function 오류는 왜 나?
A. 배열이라고 생각한 값이 실제로는 객체이거나 undefined일 수 있다. 응답 구조와 content 위치를 확인해야 한다.

Q. response.data.data가 undefined면 뭘 확인해?
A. ApiResponse Wrapper 여부와 Response Interceptor unwrap 기준을 확인해야 한다.

Q. Cannot read properties of undefined는 DTO 문제야?
A. 응답 구조, null 가능성, 초기 state, 비동기 로딩 상태 문제일 수 있으므로 Response Body와 State 초기값을 확인한다.

Q. Response Shape Mismatch는 어떻게 해결해?
A. Network Response Body를 기준으로 Type, API Function return, Component 접근 경로를 맞춘다.

---

# 16. Common Mistakes

## 16.1 DTO Mapping 공통 실수

### [개념]

DTO Mapping 실수는 Backend API 명세, 실제 응답, Frontend Type, Component 접근 경로가 서로 맞지 않을 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Request Type과 Response Type을 하나로 사용
- Backend Request DTO 필드명과 Frontend 필드명 불일치
- Form State를 그대로 Request Body로 전송
- Query Parameter와 Request Body 혼동
- Path Variable을 Request Body에만 넣음
- response.data와 response.data.data 혼동
- ApiResponse Wrapper 확인 누락
- Page Response에서 content 위치 착각
- Slice Response에서 hasNext / last 혼동
- 목록 DTO와 상세 DTO를 무리하게 통합
- nullable field를 Type에 반영하지 않음
- averageRating null을 0으로 처리
- 날짜를 Date 타입으로 선언하고 string 응답을 받음
- enum value와 label 혼동
- nested object null 가능성 미처리
- Error Response Type 미정의
- Response Interceptor unwrap 기준 혼용
- TypeScript Type만 믿고 실제 Network Response 미확인
- Mock Data와 실제 API 응답 불일치

---

### [실무]

문제 예:

```text
문제: 리뷰 작성 실패
원인: requestBody 필드명이 Backend DTO와 다름
해결: Backend Request DTO 기준으로 ReviewCreateRequest 수정
```

문제 예:

```text
문제: 목록 화면에서 map 오류
원인: PageResponse 전체를 배열처럼 사용
해결: pageData.content를 배열로 사용
```

문제 예:

```text
문제: 평점 없음인데 0점으로 표시
원인: averageRating null과 0을 구분하지 않음
해결: averageRating === null 기준으로 fallback 처리
```

문제 예:

```text
문제: enum label이 undefined
원인: Backend enum 값이 Frontend mapping에 없음
해결: union type과 label mapping 업데이트
```

해결 우선순위:

```text
Network Response Body 확인
→ Backend API Spec 확인
→ Frontend Type 확인
→ API Function return 확인
→ Component 접근 경로 확인
→ Fallback UI 확인
```

---

### [FAQ]

Q. DTO Mapping에서 가장 흔한 실수는?
A. response.data.data 구조를 착각하거나 Page Response의 content 위치를 잘못 사용하는 것이다.

Q. TypeScript Type만 맞으면 안전해?
A. 아니다. 실제 API 응답이 Type과 다르면 런타임 오류가 발생할 수 있다.

Q. Request Type과 Response Type을 하나로 쓰면 안 돼?
A. 필드가 완전히 같다면 가능하지만 대부분 요청과 응답은 다르므로 분리하는 것이 안전하다.

Q. DTO 오류는 어떻게 찾는 게 좋아?
A. Network 탭의 실제 Request Payload와 Response Body를 Type, API 함수, Component 접근 경로와 비교한다.

---

# 17. Part05 Checklist

## 17.1 Request / Response DTO Mapping 검수 기준

### [개념]

Part05 Request / Response DTO Mapping 문서는 Frontend Agent가 Backend API 명세와 실제 응답 구조를 기준으로 Request Type, Response Type, ApiResponse Wrapper, Page / Slice Response를 정확히 연결하도록 만드는 문서다.

---

### [핵심]

Checklist:

```md
- [ ] Request / Response DTO Mapping 개념이 포함되었는가?
- [ ] Request DTO 기준이 포함되었는가?
- [ ] Response DTO 기준이 포함되었는가?
- [ ] ApiResponse Wrapper 기준이 포함되었는가?
- [ ] Page Response Mapping 기준이 포함되었는가?
- [ ] Slice Response Mapping 기준이 포함되었는가?
- [ ] List / Detail DTO 분리 기준이 포함되었는가?
- [ ] Nullable Field 처리 기준이 포함되었는가?
- [ ] Date / Time Mapping 기준이 포함되었는가?
- [ ] Enum Mapping 기준이 포함되었는가?
- [ ] Nested Object Mapping 기준이 포함되었는가?
- [ ] Error Response DTO 기준이 포함되었는가?
- [ ] Form State to Request DTO 기준이 포함되었는가?
- [ ] DTO Mapping Validation 기준이 포함되었는가?
- [ ] Response Shape Mismatch Troubleshooting이 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Request DTO Check
→ Response DTO Check
→ ApiResponse Wrapper Check
→ Page / Slice Check
→ Nullable Field Check
→ Date / Enum Check
→ Nested Object Check
→ Error Response Check
→ Form Mapping Check
→ Network Response Validation
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

최종 기준:

- Request Type과 Response Type 분리 가능
- Backend DTO와 Frontend Type 동기화 가능
- ApiResponse Wrapper 처리 가능
- Page / Slice Response Mapping 가능
- null / date / enum / nested object 처리 가능
- Error Response와 Validation Error 처리 가능
- Response Shape Mismatch 분석 가능
- Frontend Agent가 타입 안정적인 API Layer 코드를 생성 가능

---

### [FAQ]

Q. Part05의 목적은 뭐야?
A. Frontend Agent가 Backend API 명세와 실제 응답 구조를 기준으로 Request / Response DTO를 정확히 mapping하게 만드는 것이다.

Q. Part05에서 가장 중요한 기준은 뭐야?
A. Request Type과 Response Type 분리, ApiResponse Wrapper 처리, Page / Slice content 위치 확인, null 가능성 반영이다.

Q. Part05 다음에는 어떤 문서가 이어지면 좋아?
A. Loading / Error / Empty UI State, TanStack Query, Pagination and Infinite Scroll, File Upload 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. DTO Mapping이 뭐야?
A. Backend API의 요청 / 응답 데이터 구조를 Frontend Type과 API 함수 반환 구조로 연결하는 작업이다.

Q. Request DTO와 Response DTO는 왜 나눠?
A. 요청과 응답의 필드가 다를 수 있기 때문이다. 생성 요청에는 없는 id, createdAt 같은 필드가 응답에는 포함될 수 있다.

Q. DTO Mapping에서 가장 중요한 것은 뭐야?
A. 실제 Backend 응답 구조, ApiResponse Wrapper, content 위치, null 가능성, 필드명을 정확히 맞추는 것이다.

Q. DTO Mapping은 어디서 확인해야 해?
A. Backend API 명세와 브라우저 Network 탭의 실제 Response Body를 함께 확인해야 한다.

Q. Request DTO는 뭐야?
A. Frontend가 Backend로 보내는 요청 데이터 구조다.

Q. Form State를 그대로 Request Body로 보내도 돼?
A. 항상 그렇지 않다. UI 전용 필드나 검증용 필드는 제거하고 Backend DTO가 요구하는 필드만 보내야 한다.

Q. GET 요청의 검색 조건도 Request DTO야?
A. 넓게 보면 요청 데이터 구조지만 보통 Request Body가 아니라 Params Type으로 분리한다.

Q. Request DTO 필드명은 Frontend 마음대로 정해도 돼?
A. 아니다. Backend Request DTO가 기대하는 필드명과 타입에 맞춰야 한다.

Q. Response DTO는 뭐야?
A. Backend가 Frontend에 응답으로 내려주는 데이터 구조다.

Q. 목록 Response와 상세 Response는 나눠야 해?
A. 나누는 것이 좋다. 목록은 요약 정보, 상세는 더 많은 필드를 포함하는 경우가 많다.

Q. null 가능 필드는 Type에 어떻게 반영해?
A. `string | null`, `number | null`처럼 null 가능성을 명시한다.

Q. Backend 응답 필드명이 바뀌면 어떻게 돼?
A. Frontend Type, API mapping, Component에서 사용하는 필드명을 함께 수정해야 한다.

Q. response.data.data는 왜 나와?
A. Axios의 `response.data` 안에 Backend ApiResponse의 `data` 필드가 다시 있기 때문이다.

Q. ApiResponse<T>는 왜 써?
A. Backend 공통 응답 wrapper를 TypeScript Generic으로 표현하기 위해 사용한다.

Q. API 함수는 data만 반환해야 해?
A. 프로젝트 기준에 따라 다르다. 대부분 화면에서는 data만 필요하지만 성공 메시지가 필요하면 wrapper 전체를 반환할 수 있다.

Q. 성공 응답과 실패 응답 Type은 같아?
A. 항상 같지 않다. 실패 응답에는 errors, code, timestamp 같은 필드가 추가될 수 있다.

Q. Page Response에서 실제 목록은 어디에 있어?
A. 보통 `content` 필드에 실제 목록 배열이 들어 있다.

Q. Spring Pageable page는 0부터 시작해?
A. 일반적으로 0-based다. UI에서 1부터 보여주면 요청 시 변환이 필요할 수 있다.

Q. Page Response는 content만 반환해도 돼?
A. 페이지 버튼이나 전체 개수가 필요하면 totalPages, totalElements도 필요하므로 Page 객체 전체를 반환하는 것이 좋다.

Q. 검색 조건이 바뀌면 page는 어떻게 해?
A. 대부분 1페이지 또는 backend page 0으로 reset하는 것이 좋다.

Q. Slice Response는 언제 써?
A. 전체 개수보다 다음 페이지 존재 여부가 중요한 더보기, 무한 스크롤, 채팅, 알림 목록에 적합하다.

Q. Page와 Slice 차이는?
A. Page는 전체 개수와 totalPages를 제공하고 Slice는 다음 페이지 존재 여부 중심이라 더보기나 무한 스크롤에 적합하다.

Q. Infinite Scroll에서 content는 어떻게 처리해?
A. 기존 목록을 교체하지 않고 새 content를 append한다.

Q. Infinite Scroll에서 중복 데이터가 생겨?
A. page 증가 타이밍, 중복 요청, 검색 조건 변경 시 초기화 누락을 확인해야 한다.

Q. 목록 DTO와 상세 DTO는 왜 나눠?
A. 목록은 요약 정보만 필요하고 상세는 더 많은 필드가 필요하므로 응답 크기와 역할을 분리하기 위해 나눈다.

Q. 같은 Festival이면 Type 하나만 써도 돼?
A. 가능은 하지만 목록과 상세의 필드가 다르면 optional이 많아지고 오류 가능성이 커진다.

Q. 목록에서 상세 필드를 쓰고 싶으면 어떻게 해?
A. Backend 목록 응답에 해당 필드가 있는지 확인해야 한다. 없으면 상세 API를 호출하거나 목록 DTO를 확장해야 한다.

Q. Detail DTO에 imageUrls가 있는데 List DTO에는 imageUrl만 있어도 돼?
A. 가능하다. 목록은 대표 이미지 하나, 상세는 이미지 배열을 사용하는 식으로 분리할 수 있다.

Q. averageRating이 null이면 0점이야?
A. 아니다. null은 아직 평점이 없다는 뜻일 수 있고 0은 실제 값일 수 있다.

Q. optional chaining만 쓰면 안전해?
A. 오류는 줄일 수 있지만 UI fallback이 없으면 빈 화면이 될 수 있으므로 명시적 처리가 좋다.

Q. null과 undefined는 같아?
A. 다르다. Backend JSON 응답에서는 보통 값이 없을 때 null을 명시적으로 내려줄 수 있다.

Q. 날짜 타입은 Date로 받아?
A. JSON 응답은 보통 문자열로 받는다. 필요하면 Frontend에서 Date 객체나 formatting 함수로 변환한다.

Q. LocalDateTime은 Frontend에서 어떤 타입이야?
A. JSON으로 받으면 보통 string이다.

Q. targetMonth는 어떤 형식으로 보내?
A. Backend 명세에 따라 다르지만 월별 조회에서는 보통 `yyyy-MM` 형식을 사용할 수 있다.

Q. 날짜가 하루 밀려 보이면 뭘 확인해?
A. timezone 변환, Date 객체 변환 방식, Backend LocalDate / LocalDateTime 형식을 확인해야 한다.

Q. Backend enum은 Frontend에서 어떤 타입으로 받아?
A. JSON 응답에서는 보통 string으로 받으며 TypeScript에서는 union type으로 표현할 수 있다.

Q. enum label은 Backend 값 그대로 보여줘도 돼?
A. 가능하지만 사용자 화면에는 label mapping을 통해 한글 표시명으로 보여주는 것이 좋다.

Q. enum value와 label은 뭐가 달라?
A. enum value는 API와 로직에서 사용하는 값이고 label은 사용자에게 보여주는 표시명이다.

Q. enum 값이 추가되면 Frontend도 수정해야 해?
A. 표시 label, filter option, 조건 분기, TypeScript union type을 함께 확인해야 한다.

Q. 중첩 객체는 Type을 따로 만들어야 해?
A. 재사용되거나 구조가 복잡하면 RegionResponse, ImageResponse처럼 따로 분리하는 것이 좋다.

Q. API 응답을 화면용으로 바꿔도 돼?
A. 가능하다. API Response Type과 View Model을 구분하면 Component가 더 단순해질 수 있다.

Q. images가 null이면 map 오류가 나?
A. 그렇다. 배열이 null일 수 있다면 fallback으로 빈 배열을 사용하거나 Type에 null을 반영해야 한다.

Q. 중첩 필드를 Component에서 계속 접근해도 돼?
A. 가능하지만 깊은 접근이 반복되면 Hook이나 mapping 함수에서 화면용 구조로 변환하는 것이 좋다.

Q. Error Response DTO도 Type이 필요해?
A. 필요하다. field error, message, code 구조를 안정적으로 처리할 수 있다.

Q. 서버 에러 메시지를 그대로 보여줘도 돼?
A. 민감한 정보가 포함될 수 있으므로 사용자 메시지와 개발자 로그를 구분하는 것이 좋다.

Q. Validation Error는 어떻게 보여줘?
A. field별 오류는 해당 input 근처에 표시하고 공통 오류는 form 상단에 표시하는 것이 좋다.

Q. Error Response 구조는 어디서 확인해?
A. Network 탭의 Response Body와 Backend 예외 처리 응답 명세를 확인한다.

Q. rating input 값은 string인데 Request DTO는 number면 어떻게 해?
A. 요청 전 Number 변환을 하고 NaN이나 빈 값 검증을 해야 한다.

Q. passwordConfirm도 Backend로 보내야 해?
A. Backend 명세에 따라 다르지만 보통 Frontend 검증용이면 Request DTO에서 제거한다.

Q. trim은 어디서 해?
A. 제출 직전 Request DTO 변환 단계에서 처리할 수 있다. 단, 의도적으로 공백이 필요한 필드는 주의한다.

Q. DTO Mapping은 어떻게 검수해?
A. API 명세, 실제 Network Request / Response, TypeScript Type, Component 접근 경로를 함께 비교한다.

Q. TypeScript 에러가 없으면 응답 구조도 맞는 거야?
A. 아니다. TypeScript Type은 개발자가 선언한 구조이므로 실제 API 응답과 다를 수 있다.

Q. Swagger 예시와 실제 응답이 다르면 뭘 기준으로 해?
A. 실제 Backend 응답과 Backend 팀 확인을 기준으로 Type과 mapping을 수정해야 한다.

Q. Response Body는 어디서 확인해?
A. 브라우저 개발자 도구 Network 탭에서 확인한다.

Q. map is not a function 오류는 왜 나?
A. 배열이라고 생각한 값이 실제로는 객체이거나 undefined일 수 있다. 응답 구조와 content 위치를 확인해야 한다.

Q. response.data.data가 undefined면 뭘 확인해?
A. ApiResponse Wrapper 여부와 Response Interceptor unwrap 기준을 확인해야 한다.

Q. Cannot read properties of undefined는 DTO 문제야?
A. 응답 구조, null 가능성, 초기 state, 비동기 로딩 상태 문제일 수 있으므로 Response Body와 State 초기값을 확인한다.

Q. Response Shape Mismatch는 어떻게 해결해?
A. Network Response Body를 기준으로 Type, API Function return, Component 접근 경로를 맞춘다.

Q. DTO Mapping에서 가장 흔한 실수는?
A. response.data.data 구조를 착각하거나 Page Response의 content 위치를 잘못 사용하는 것이다.

Q. TypeScript Type만 맞으면 안전해?
A. 아니다. 실제 API 응답이 Type과 다르면 런타임 오류가 발생할 수 있다.

Q. Request Type과 Response Type을 하나로 쓰면 안 돼?
A. 필드가 완전히 같다면 가능하지만 대부분 요청과 응답은 다르므로 분리하는 것이 안전하다.

Q. DTO 오류는 어떻게 찾는 게 좋아?
A. Network 탭의 실제 Request Payload와 Response Body를 Type, API 함수, Component 접근 경로와 비교한다.

Q. Part05 Request / Response DTO Mapping의 목적은 뭐야?
A. Frontend Agent가 Backend API 명세와 실제 응답 구조를 기준으로 Request / Response DTO를 정확히 mapping하게 만드는 것이다.

Q. Part05 다음에는 어떤 문서가 이어지면 좋아?
A. Loading / Error / Empty UI State, TanStack Query, Pagination and Infinite Scroll, File Upload 순서로 이어지는 것이 좋다.
