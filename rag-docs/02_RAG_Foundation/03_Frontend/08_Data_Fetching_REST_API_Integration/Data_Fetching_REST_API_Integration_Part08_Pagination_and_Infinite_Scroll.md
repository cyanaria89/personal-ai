# Data Fetching & REST API Integration Part08 - Pagination and Infinite Scroll

---

# 1. Pagination and Infinite Scroll Overview

## 1.1 Pagination / Infinite Scroll 기본 개념

### [개념]

Pagination과 Infinite Scroll은 서버의 목록 데이터를 한 번에 모두 가져오지 않고 여러 단위로 나누어 조회하는 Data Fetching 방식이다.

Frontend Agent는 Backend 응답이 Page Response인지 Slice Response인지 Cursor Response인지 구분하고, UI 요구사항에 맞는 목록 로딩 전략을 선택해야 한다.

기본 구분:

```text
Pagination
→ page / size 기반 목록 조회
→ 전체 페이지 번호 또는 이전 / 다음 버튼으로 목록 교체

Load More
→ page / cursor 기반 추가 조회
→ 버튼 클릭 시 content append

Infinite Scroll
→ page / cursor 기반 추가 조회
→ 스크롤 하단 감지 시 content append
```

---

### [핵심]

핵심 키워드:

- Pagination
- Load More
- Infinite Scroll
- Page Response
- Slice Response
- Cursor Response
- page
- size
- sort
- totalPages
- totalElements
- content
- hasNext
- last
- cursor
- nextCursor
- offset pagination
- cursor pagination
- append
- replace
- reset
- duplicate request prevention
- queryKey
- useInfiniteQuery

선택 기준:

```text
전체 페이지 수 / 페이지 번호 UI 필요 → Page Response + Pagination
더보기 / 무한 스크롤 / 전체 개수 불필요 → Slice Response
대용량 / 실시간성 / 정렬 안정성 필요 → Cursor Response
```

---

### [실무]

2026 실무 기준에서 목록 API는 데이터 크기, UX, 성능, 정렬 안정성에 따라 Pagination, Load More, Infinite Scroll 중 하나를 선택한다.

Pagination 적합:

- 관리자 목록
- 검색 결과 페이지
- 게시글 목록
- 축제 목록
- 페이지 번호 UI가 필요한 화면
- 전체 개수 표시가 필요한 화면

Load More 적합:

- 리뷰 더보기
- 댓글 더보기
- 알림 더보기
- 모바일 목록
- 접근성 제어가 필요한 추가 조회 UI

Infinite Scroll 적합:

- 알림 목록
- 피드 목록
- 채팅 과거 메시지
- 방문 기록
- 모바일 중심 연속 탐색 UI

기본 Flow:

```text
List Page Mount
→ Request page=0,size=20
→ Response content
→ Render List
→ User Changes Page or Load More or Scroll Bottom
→ Request Next Data
→ Replace or Append
```

---

### [FAQ]

Q. Pagination과 Infinite Scroll 차이는?
A. Pagination은 페이지 번호를 기준으로 목록을 교체하고 Infinite Scroll은 다음 데이터를 계속 append한다.

Q. Page Response와 Slice Response 차이는?
A. Page는 totalPages와 totalElements를 포함하고 Slice는 다음 페이지 존재 여부 중심으로 동작한다.

Q. 전체 페이지 수가 필요하면 뭘 써?
A. Page Response 기반 Pagination을 사용하는 것이 좋다.

Q. 무한 스크롤에는 Page보다 Slice가 좋아?
A. 전체 개수가 필요 없다면 Slice가 더 가볍고 무한 스크롤에 적합하다.

---

# 2. Page Response Rules

## 2.1 Page Response 기본

### [개념]

Page Response는 목록 데이터와 전체 페이지 정보를 함께 내려주는 응답 구조다.

Spring Pageable 기반 API에서 자주 사용하며, 페이지 번호 UI를 만들 때 적합하다.

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
- numberOfElements
- sort
- pageable

Frontend 사용 대상:

- 페이지 번호 버튼
- 이전 / 다음 버튼
- 전체 데이터 개수 표시
- 현재 페이지 표시
- 검색 결과 개수 표시
- 페이지 이동
- 마지막 페이지 판단

주의:

- Spring Pageable은 보통 0-based
- UI page는 보통 1-based
- `content`가 실제 목록 배열
- totalPages가 0일 수 있음
- 검색 조건 변경 시 page reset 필요
- Page Response 전체가 필요한 경우 content만 반환하지 않음

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
  numberOfElements?: number;
};
```

API Function:

```typescript
export async function getFestivals(
  params: FestivalSearchParams,
): Promise<PageResponse<FestivalSummaryResponse>> {
  const response = await publicApi.get<
    ApiResponse<PageResponse<FestivalSummaryResponse>>
  >("/festivals", {
    params: cleanParams(params),
  });

  return response.data.data;
}
```

Component Mapping:

```typescript
const pageData = await getFestivals({
  keyword: "flower",
  page: 0,
  size: 20,
});

setItems(pageData.content);
setPageInfo({
  currentPage: pageData.number + 1,
  totalPages: pageData.totalPages,
  totalElements: pageData.totalElements,
  first: pageData.first,
  last: pageData.last,
});
```

---

### [FAQ]

Q. Page Response에서 실제 목록은 어디에 있어?
A. 보통 `content` 필드에 실제 목록 배열이 들어 있다.

Q. totalPages는 언제 필요해?
A. 페이지 번호 버튼이나 마지막 페이지 여부를 표시할 때 필요하다.

Q. totalElements는 언제 필요해?
A. 전체 검색 결과 개수나 전체 항목 수를 보여줄 때 필요하다.

Q. Page Response에서 content만 반환해도 돼?
A. 페이지 UI에 totalPages, totalElements가 필요하면 Page 객체 전체를 반환해야 한다.

---

# 3. Slice Response Rules

## 3.1 Slice Response 기본

### [개념]

Slice Response는 전체 개수보다 다음 페이지 존재 여부를 중심으로 내려주는 응답 구조다.

전체 count 쿼리를 줄일 수 있어 더보기, 무한 스크롤, 알림 목록, 채팅 목록에 적합하다.

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

- 더보기 버튼
- 무한 스크롤
- 알림 목록
- 리뷰 더보기
- 댓글 더보기
- 채팅 과거 메시지

주의:

- totalPages가 없을 수 있음
- totalElements가 없을 수 있음
- 기존 목록에 content append
- hasNext / last 기준 통일
- 검색 조건 변경 시 items reset
- loadingMore 중복 요청 방지

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
  numberOfElements?: number;
};
```

API Function:

```typescript
export async function getNotifications(
  params: NotificationListParams,
): Promise<SliceResponse<NotificationResponse>> {
  const response = await authApi.get<
    ApiResponse<SliceResponse<NotificationResponse>>
  >("/notifications", {
    params: cleanParams(params),
  });

  return response.data.data;
}
```

Load More 적용:

```typescript
const sliceData = await getNotifications({
  page,
  size: 20,
});

setItems((prev) => [...prev, ...sliceData.content]);
setHasNext(sliceData.hasNext);
setPage(sliceData.number + 1);
```

---

### [FAQ]

Q. Slice Response는 언제 써?
A. 전체 개수보다 다음 페이지 존재 여부가 중요한 더보기, 무한 스크롤, 채팅, 알림 목록에 적합하다.

Q. Slice Response에는 totalPages가 없어?
A. 없을 수 있다. Slice는 전체 페이지 수보다 다음 데이터 존재 여부를 중심으로 한다.

Q. Slice Response의 content는 어떻게 처리해?
A. 더보기나 무한 스크롤에서는 기존 items에 append한다.

Q. hasNext와 last는 어떻게 써?
A. hasNext가 false이거나 last가 true이면 다음 요청을 중단한다.

---

# 4. Cursor Response Rules

## 4.1 Cursor 기반 Response

### [개념]

Cursor Response는 page 번호 대신 마지막으로 조회한 데이터의 cursor 값을 기준으로 다음 데이터를 조회하는 응답 구조다.

대용량 목록, 실시간성이 있는 목록, 정렬 안정성이 중요한 목록에 적합하다.

---

### [핵심]

Cursor Response 핵심 필드:

- content
- nextCursor
- hasNext
- cursor
- limit

Cursor 기준 예:

- lastId
- lastCreatedAt
- lastScore
- encoded cursor
- nextCursor token

특징:

- 대용량 데이터에 유리
- 데이터 추가 / 삭제에 비교적 안정적
- 특정 페이지 번호 이동은 어려움
- 더보기 / 무한 스크롤에 적합

주의:

- 정렬 기준이 안정적이어야 함
- cursor 값은 마지막 item 기준
- nextCursor가 없으면 추가 요청 중단
- 검색 조건 변경 시 cursor reset
- cursor를 queryKey에 직접 넣을지 useInfiniteQuery pageParam으로 관리할지 결정

---

### [실무]

CursorResponse Type:

```typescript
export type CursorResponse<T> = {
  content: T[];
  nextCursor: string | null;
  hasNext: boolean;
};
```

API Function:

```typescript
export async function getNotificationsByCursor(params: {
  cursor?: string;
  size: number;
}): Promise<CursorResponse<NotificationResponse>> {
  const response = await authApi.get<
    ApiResponse<CursorResponse<NotificationResponse>>
  >("/notifications", {
    params: cleanParams(params),
  });

  return response.data.data;
}
```

요청 예:

```text
GET /api/notifications?cursor=eyJpZCI6MTAwfQ&size=20
```

Load More:

```typescript
const response = await getNotificationsByCursor({
  cursor: nextCursor ?? undefined,
  size: 20,
});

setItems((prev) => [...prev, ...response.content]);
setNextCursor(response.nextCursor);
setHasNext(response.hasNext);
```

---

### [FAQ]

Q. Cursor Pagination은 뭐야?
A. page 번호 대신 마지막 데이터의 cursor를 기준으로 다음 데이터를 조회하는 방식이다.

Q. Cursor Pagination은 언제 좋아?
A. 대용량 목록, 실시간으로 데이터가 추가되는 목록, 무한 스크롤에 적합하다.

Q. Cursor 방식은 특정 페이지로 바로 이동할 수 있어?
A. 일반적으로 어렵다. Cursor 방식은 순차적인 더보기 흐름에 적합하다.

Q. nextCursor가 null이면 어떻게 해?
A. 더 이상 가져올 데이터가 없으므로 추가 요청을 중단한다.

---

# 5. Offset Pagination Rules

## 5.1 page / size 기반 Pagination

### [개념]

Offset Pagination은 `page`와 `size`를 사용해 특정 위치의 목록 데이터를 조회하는 방식이다.

Spring Pageable 기반 API는 보통 `page`, `size`, `sort` Query Parameter를 사용한다.

---

### [핵심]

Offset Pagination Query Parameter:

- page
- size
- sort
- keyword
- filter
- startDate
- endDate

특징:

- 페이지 번호 이동이 쉬움
- totalPages와 함께 사용 가능
- 검색 결과 페이지에 적합
- 데이터 변경이 많은 목록에서는 중복 / 누락 가능성 있음
- 큰 page로 갈수록 DB offset 비용 증가 가능

주의:

- Backend page 0-based 확인
- UI page 1-based 변환
- page 변경 시 queryKey 변경
- 검색 조건 변경 시 page reset
- size 변경 시 page reset
- sort 변경 시 page reset

---

### [실무]

Params Type:

```typescript
export type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  themeCode?: string;
  page?: number;
  size?: number;
  sort?: string;
};
```

API 요청:

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

요청 예:

```text
GET /api/festivals/search?keyword=flower&page=0&size=20&sort=eventStartDate,asc
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

Q. Offset Pagination은 뭐야?
A. page와 size를 기준으로 특정 페이지의 데이터를 조회하는 방식이다.

Q. Spring Pageable page는 0부터 시작해?
A. 일반적으로 0-based다. UI에서 1부터 보여주면 요청 시 변환이 필요하다.

Q. sort는 Query Parameter로 보내?
A. Spring Pageable에서는 보통 `sort=field,direction` 형태로 보낸다.

Q. 검색 조건이 바뀌면 page는 어떻게 해?
A. 대부분 backend page 0 또는 UI page 1로 reset한다.

---

# 6. Pagination UI State Rules

## 6.1 페이지 번호 UI 상태

### [개념]

Pagination UI State는 현재 페이지, 전체 페이지, 이전 / 다음 가능 여부, 로딩 상태를 관리하는 기준이다.

Page Response의 metadata를 UI 상태로 mapping한다.

---

### [핵심]

Pagination UI State:

- currentPage
- backendPage
- pageSize
- totalPages
- totalElements
- first
- last
- loading
- refetching
- disabled
- selected page

판단 기준:

```text
first true → Prev disabled
last true → Next disabled
loading true → Page Button disabled
totalPages 0 → Empty State
```

주의:

- UI page와 backend page 변환
- page button 클릭 중 중복 요청 방지
- 현재 page 표시
- totalPages가 0일 때 처리
- 검색 조건 변경 시 currentPage reset
- size 변경 시 currentPage reset

---

### [실무]

PageInfo Type:

```typescript
export type PageInfo = {
  currentPage: number;
  pageSize: number;
  totalPages: number;
  totalElements: number;
  first: boolean;
  last: boolean;
};
```

PageInfo Mapping:

```typescript
export function toPageInfo<T>(pageData: PageResponse<T>): PageInfo {
  return {
    currentPage: pageData.number + 1,
    pageSize: pageData.size,
    totalPages: pageData.totalPages,
    totalElements: pageData.totalElements,
    first: pageData.first,
    last: pageData.last,
  };
}
```

Pagination UI:

```tsx
function Pagination({
  pageInfo,
  loading,
  onPageChange,
}: {
  pageInfo: PageInfo;
  loading: boolean;
  onPageChange: (page: number) => void;
}) {
  return (
    <nav aria-label="Pagination">
      <button
        type="button"
        disabled={pageInfo.first || loading}
        onClick={() => onPageChange(pageInfo.currentPage - 1)}
      >
        이전
      </button>

      <span aria-current="page">
        {pageInfo.currentPage} / {pageInfo.totalPages}
      </span>

      <button
        type="button"
        disabled={pageInfo.last || loading}
        onClick={() => onPageChange(pageInfo.currentPage + 1)}
      >
        다음
      </button>
    </nav>
  );
}
```

---

### [FAQ]

Q. Pagination UI에서 currentPage는 backend page 그대로 써?
A. 보통 UI는 1-based로 표시하므로 backend page에 1을 더해 사용한다.

Q. 이전 버튼은 언제 disabled 해?
A. Page Response의 first가 true이거나 현재 요청이 loading 중일 때 disabled 한다.

Q. 다음 버튼은 언제 disabled 해?
A. Page Response의 last가 true이거나 현재 요청이 loading 중일 때 disabled 한다.

Q. totalPages가 0이면 어떻게 보여줘?
A. 목록은 Empty State로 처리하고 페이지 버튼은 숨기거나 비활성화할 수 있다.

---

# 7. Search Params and Page Reset Rules

## 7.1 검색 조건 변경 시 Page Reset

### [개념]

검색 조건, 필터, 정렬, page size가 변경되면 기존 page 번호가 더 이상 유효하지 않을 수 있다.

따라서 조건 변경 시 page를 초기값으로 reset하는 것이 안전하다.

---

### [핵심]

Page Reset 대상:

- keyword 변경
- region filter 변경
- theme filter 변경
- date range 변경
- sort 변경
- page size 변경
- submitted search params 변경

Reset 기준:

```text
Search Params Change
→ UI page 1
→ Backend page 0
→ Fetch New Result
```

주의:

- 입력 중인 검색어와 제출된 검색 조건 구분
- 검색 버튼 클릭 시 submittedParams 업데이트
- 필터 변경 즉시 검색할지 submit 후 검색할지 결정
- page reset 누락 시 빈 페이지가 나올 수 있음
- TanStack Query queryKey에 submittedParams와 page 포함

---

### [실무]

검색 Form State와 Submitted Params 분리:

```typescript
const [keywordInput, setKeywordInput] = useState("");
const [submittedParams, setSubmittedParams] = useState<FestivalSearchParams>({
  page: 0,
  size: 20,
});
```

Submit 시 page reset:

```typescript
function handleSearchSubmit() {
  setSubmittedParams({
    keyword: keywordInput,
    page: 0,
    size: 20,
  });

  setUiPage(1);
}
```

Page 변경:

```typescript
function handlePageChange(nextUiPage: number) {
  setUiPage(nextUiPage);

  setSubmittedParams((prev) => ({
    ...prev,
    page: nextUiPage - 1,
  }));
}
```

Flow:

```text
Search Submit
→ submittedParams update
→ page 0 reset
→ queryKey changes
→ New Page Response
```

---

### [FAQ]

Q. 검색 조건이 바뀌면 page를 왜 reset해?
A. 기존 page 번호가 새 검색 결과에서는 존재하지 않을 수 있기 때문이다.

Q. 검색어 입력마다 API 요청을 보내야 해?
A. UX 기준에 따라 다르다. 검색 버튼 submit 방식이나 debounce 방식을 사용할 수 있다.

Q. 입력 중인 keyword와 submitted keyword는 왜 나눠?
A. 사용자가 입력 중인 값과 실제 API 요청에 사용되는 조건을 분리하기 위해서다.

Q. page reset을 안 하면 어떤 문제가 생겨?
A. 새 검색 결과에서 존재하지 않는 page를 요청해 빈 화면이 나올 수 있다.

---

# 8. Replace vs Append Rules

## 8.1 목록 교체와 추가 기준

### [개념]

Replace는 기존 목록을 새 응답 content로 교체하는 방식이다.

Append는 기존 목록 뒤에 새 응답 content를 추가하는 방식이다.

Pagination은 보통 Replace를 사용하고, Load More와 Infinite Scroll은 Append를 사용한다.

---

### [핵심]

Replace 사용 상황:

- 페이지 번호 이동
- 검색 조건 변경
- 필터 변경
- 정렬 변경
- size 변경
- 새 Page Response 조회

Append 사용 상황:

- 더보기 버튼
- 무한 스크롤
- 이전 채팅 내역 추가
- 알림 추가 조회
- 리뷰 추가 조회

주의:

- Pagination에서 append하면 다른 페이지 데이터가 섞일 수 있음
- Load More에서 replace하면 기존 목록이 사라짐
- 검색 조건 변경 시 append 전에 reset 필요
- Cursor 변경 시 기존 cursor 기준을 명확히 함

---

### [실무]

Pagination Replace:

```typescript
const pageData = await getFestivals(params);

setItems(pageData.content);
setPageInfo(toPageInfo(pageData));
```

Load More Append:

```typescript
const sliceData = await getReviews({
  page,
  size: 20,
});

setItems((prev) => [...prev, ...sliceData.content]);
```

검색 조건 변경 시 Reset + Replace:

```typescript
function handleSearch(nextParams: FestivalSearchParams) {
  setSubmittedParams({
    ...nextParams,
    page: 0,
    size: 20,
  });

  setUiPage(1);
}
```

---

### [FAQ]

Q. Pagination은 append야 replace야?
A. 보통 replace다. 페이지를 이동하면 해당 페이지 content로 목록을 교체한다.

Q. Load More는 append야 replace야?
A. append다. 기존 items 뒤에 새 content를 추가한다.

Q. 검색 조건 변경 후 append하면 안 돼?
A. 조건이 다른 데이터가 섞일 수 있으므로 reset 후 새 결과를 사용해야 한다.

Q. 더보기 클릭 후 기존 목록이 사라지면?
A. append가 아니라 replace로 처리했을 가능성이 높다.

---

# 9. Load More Rules

## 9.1 더보기 버튼 기준

### [개념]

Load More는 사용자가 버튼을 눌렀을 때 다음 목록 데이터를 추가로 요청하고 기존 목록 아래에 append하는 방식이다.

무한 스크롤보다 제어가 쉽고 접근성이 좋은 경우가 많다.

---

### [핵심]

Load More State:

- items
- page
- size
- hasNext
- loadingMore
- errorMessage
- last
- nextCursor

처리 기준:

- loadingMore 중복 요청 방지
- hasNext false면 버튼 숨김 또는 disabled
- 성공 시 content append
- 실패 시 기존 items 유지
- 검색 조건 변경 시 items reset
- page 또는 cursor 업데이트

주의:

- 기존 목록을 교체하지 않음
- loadingMore false를 finally에서 처리
- 실패 후 Retry 가능
- 중복 데이터 방지
- Button disabled 처리

---

### [실무]

Page 기반 Load More:

```typescript
async function loadMore() {
  if (loadingMore || !hasNext) {
    return;
  }

  try {
    setLoadingMore(true);

    const sliceData = await getReviews({
      page,
      size: 20,
    });

    setItems((prev) => [...prev, ...sliceData.content]);
    setHasNext(sliceData.hasNext);
    setPage(sliceData.number + 1);
  } finally {
    setLoadingMore(false);
  }
}
```

Load More Button:

```tsx
{
  hasNext && (
    <button type="button" disabled={loadingMore} onClick={loadMore}>
      {loadingMore ? "불러오는 중..." : "더보기"}
    </button>
  );
}
```

Cursor 기반 Load More:

```typescript
async function loadMoreByCursor() {
  if (loadingMore || !hasNext) {
    return;
  }

  try {
    setLoadingMore(true);

    const response = await getNotificationsByCursor({
      cursor: nextCursor ?? undefined,
      size: 20,
    });

    setItems((prev) => [...prev, ...response.content]);
    setNextCursor(response.nextCursor);
    setHasNext(response.hasNext);
  } finally {
    setLoadingMore(false);
  }
}
```

---

### [FAQ]

Q. Load More는 Infinite Scroll과 뭐가 달라?
A. Load More는 사용자가 버튼을 눌러 추가 데이터를 가져오고 Infinite Scroll은 스크롤 위치에 따라 자동 요청한다.

Q. Load More에서는 기존 목록을 교체해?
A. 아니다. 기존 items에 새 content를 append한다.

Q. Load More 버튼은 언제 숨겨?
A. hasNext가 false이거나 last가 true이면 숨기거나 disabled 할 수 있다.

Q. Load More 실패 시 기존 목록은 지워?
A. 보통 지우지 않는다. 기존 목록은 유지하고 오류 메시지나 재시도 버튼을 제공한다.

---

# 10. Infinite Scroll Rules

## 10.1 무한 스크롤 기준

### [개념]

Infinite Scroll은 사용자가 목록 하단에 가까워지면 다음 데이터를 자동으로 요청하고 append하는 UI 방식이다.

Intersection Observer 또는 scroll event를 사용할 수 있다.

---

### [핵심]

Infinite Scroll 핵심 요소:

- Intersection Observer
- sentinel element
- hasNext
- loadingMore
- fetchNextPage
- append content
- duplicate prevention
- reset on filter change
- cleanup observer
- accessibility fallback

주의:

- loadingMore 중복 요청 방지
- hasNext false면 observer 동작 중단
- 검색 조건 변경 시 items reset
- 스크롤 이벤트보다 Intersection Observer 권장
- 너무 잦은 요청 방지
- 접근성을 위해 Load More fallback 고려
- footer 접근 어려움 문제 고려

---

### [실무]

Intersection Observer 개념 Flow:

```text
Render List
→ Render Sentinel Element
→ Sentinel Visible
→ hasNext and not loadingMore
→ Fetch Next Page
→ Append Content
```

기본 구현 예:

```tsx
const observerRef = useRef<IntersectionObserver | null>(null);
const sentinelRef = useRef<HTMLDivElement | null>(null);

useEffect(() => {
  if (!sentinelRef.current) {
    return;
  }

  observerRef.current = new IntersectionObserver((entries) => {
    const firstEntry = entries[0];

    if (firstEntry.isIntersecting && hasNext && !loadingMore) {
      loadMore();
    }
  });

  observerRef.current.observe(sentinelRef.current);

  return () => {
    observerRef.current?.disconnect();
  };
}, [hasNext, loadingMore]);
```

Sentinel UI:

```tsx
<div ref={sentinelRef} aria-hidden="true" />;

{
  loadingMore && <p>더 불러오는 중...</p>;
}

{
  !hasNext && <p>마지막 항목입니다.</p>;
}
```

---

### [FAQ]

Q. Infinite Scroll은 언제 써?
A. 피드, 알림, 댓글, 리뷰처럼 계속 이어지는 목록 UI에 사용한다.

Q. Infinite Scroll에서 중복 요청은 어떻게 막아?
A. loadingMore 상태와 hasNext 상태를 확인해 요청 중이거나 다음 데이터가 없으면 호출하지 않는다.

Q. Intersection Observer를 쓰는 이유는?
A. scroll event보다 효율적으로 특정 요소가 화면에 들어왔는지 감지할 수 있기 때문이다.

Q. Infinite Scroll에도 더보기 버튼이 필요해?
A. 접근성과 제어성을 위해 fallback으로 제공하는 것이 좋을 수 있다.

---

# 11. useInfiniteQuery Rules

## 11.1 TanStack Query Infinite Query 기준

### [개념]

`useInfiniteQuery`는 여러 페이지 데이터를 누적해서 관리하는 TanStack Query Hook이다.

PageParam을 기준으로 다음 데이터를 가져오고 `data.pages`에 누적한다.

---

### [핵심]

useInfiniteQuery 핵심 요소:

- queryKey
- queryFn
- initialPageParam
- pageParam
- getNextPageParam
- fetchNextPage
- hasNextPage
- isFetchingNextPage
- data.pages
- flatMap

주의:

- getNextPageParam에서 다음 page 또는 cursor 반환
- 다음 값이 없으면 undefined 반환
- data.pages를 flatMap해서 content 배열 생성
- queryKey에 검색 조건 포함
- 검색 조건 변경 시 새 queryKey로 초기화
- 중복 fetchNextPage 방지

---

### [실무]

Slice 기반 useInfiniteQuery:

```typescript
const query = useInfiniteQuery({
  queryKey: ["reviews", festivalId, params],
  initialPageParam: 0,
  queryFn: ({ pageParam }) =>
    getReviews(festivalId, {
      ...params,
      page: pageParam,
      size: 20,
    }),
  getNextPageParam: (lastPage) => {
    if (!lastPage.hasNext) {
      return undefined;
    }

    return lastPage.number + 1;
  },
});
```

Flatten:

```typescript
const reviews = query.data?.pages.flatMap((page) => page.content) ?? [];
```

Button:

```tsx
<button
  type="button"
  disabled={!query.hasNextPage || query.isFetchingNextPage}
  onClick={() => query.fetchNextPage()}
>
  {query.isFetchingNextPage ? "불러오는 중..." : "더보기"}
</button>
```

Cursor 기반 useInfiniteQuery:

```typescript
const query = useInfiniteQuery({
  queryKey: ["notifications", params],
  initialPageParam: null as string | null,
  queryFn: ({ pageParam }) =>
    getNotificationsByCursor({
      cursor: pageParam ?? undefined,
      size: 20,
    }),
  getNextPageParam: (lastPage) => lastPage.nextCursor ?? undefined,
});
```

---

### [FAQ]

Q. useInfiniteQuery는 언제 써?
A. 더보기 버튼이나 무한 스크롤처럼 여러 페이지 데이터를 누적해서 보여줄 때 사용한다.

Q. data.pages는 뭐야?
A. 각 페이지 응답이 순서대로 들어 있는 배열이다.

Q. 목록 배열은 어떻게 만들어?
A. `data.pages.flatMap(page => page.content)`처럼 각 페이지의 content를 합친다.

Q. getNextPageParam은 뭘 반환해야 해?
A. 다음 요청에 사용할 page 번호나 cursor를 반환하고, 다음 데이터가 없으면 undefined를 반환한다.

---

# 12. Duplicate Request Prevention Rules

## 12.1 중복 요청 방지 기준

### [개념]

Duplicate Request Prevention은 같은 페이지나 같은 mutation이 여러 번 요청되지 않도록 막는 기준이다.

Pagination, Load More, Infinite Scroll에서 중요하다.

---

### [핵심]

중복 요청 발생 상황:

- 더보기 버튼 연속 클릭
- Infinite Scroll sentinel 반복 감지
- page button 연속 클릭
- useEffect dependency 오류
- queryKey 불안정
- loading guard 누락
- hasNext check 누락

방지 기준:

- loadingMore guard
- disabled button
- hasNext check
- debounce / throttle
- stable queryKey
- correct dependency array
- TanStack Query isFetchingNextPage 활용

---

### [실무]

Load More Guard:

```typescript
async function loadMore() {
  if (loadingMore || !hasNext) {
    return;
  }

  try {
    setLoadingMore(true);
    await requestNextPage();
  } finally {
    setLoadingMore(false);
  }
}
```

Page Button Guard:

```tsx
<button
  type="button"
  disabled={loading || pageInfo.last}
  onClick={() => onPageChange(pageInfo.currentPage + 1)}
>
  다음
</button>
```

TanStack Query Guard:

```tsx
<button
  type="button"
  disabled={!query.hasNextPage || query.isFetchingNextPage}
  onClick={() => query.fetchNextPage()}
>
  더보기
</button>
```

---

### [FAQ]

Q. 더보기 버튼을 여러 번 누르면 어떻게 막아?
A. loadingMore 상태와 disabled 버튼을 사용해 요청 중에는 추가 클릭을 막는다.

Q. Infinite Scroll에서 같은 페이지가 여러 번 호출돼?
A. loadingMore guard, hasNext check, observer cleanup, page update 타이밍을 확인해야 한다.

Q. Pagination 버튼 중복 요청은 어떻게 막아?
A. loading 중 page button을 disabled 처리하고 page 변경 요청을 중복 실행하지 않도록 한다.

Q. 중복 요청 여부는 어디서 확인해?
A. 브라우저 Network 탭에서 같은 API 요청이 여러 번 나갔는지 확인한다.

---

# 13. Reset Rules

## 13.1 검색 / 필터 변경 시 목록 Reset

### [개념]

Reset은 검색 조건, 필터, 정렬, page size가 바뀌었을 때 기존 목록과 page / cursor 상태를 초기화하는 작업이다.

Pagination과 Infinite Scroll 모두 Reset 기준이 필요하다.

---

### [핵심]

Reset 대상:

- items
- page
- cursor
- nextCursor
- hasNext
- errorMessage
- selected filter
- submitted params
- scroll position

Reset 상황:

- keyword 변경 후 submit
- filter 변경
- sort 변경
- page size 변경
- tab 변경
- resource id 변경
- logout / user change

주의:

- 기존 조건의 데이터와 새 조건의 데이터 혼합 금지
- Infinite Scroll에서 items reset 누락 시 데이터 섞임
- Cursor 방식에서 nextCursor reset 필수
- page 방식에서 page 0 reset 필수
- TanStack Query는 queryKey 변경으로 cache 분리 가능

---

### [실무]

수동 Infinite Scroll Reset:

```typescript
function resetInfiniteList() {
  setItems([]);
  setPage(0);
  setHasNext(true);
  setErrorMessage("");
}
```

Cursor Reset:

```typescript
function resetCursorList() {
  setItems([]);
  setNextCursor(null);
  setHasNext(true);
}
```

검색 Submit:

```typescript
function handleSearchSubmit(nextParams: SearchParams) {
  resetInfiniteList();

  setSubmittedParams({
    ...nextParams,
    page: 0,
    size: 20,
  });
}
```

TanStack Query 방식:

```typescript
const query = useInfiniteQuery({
  queryKey: ["reviews", festivalId, submittedParams],
  initialPageParam: 0,
  queryFn: ({ pageParam }) =>
    getReviews(festivalId, {
      ...submittedParams,
      page: pageParam,
      size: 20,
    }),
  getNextPageParam: (lastPage) =>
    lastPage.hasNext ? lastPage.number + 1 : undefined,
});
```

---

### [FAQ]

Q. 검색 조건이 바뀌면 기존 items를 지워야 해?
A. Infinite Scroll이나 Load More에서는 지우는 것이 안전하다. Pagination은 새 Page Response로 교체한다.

Q. Cursor 방식에서 reset할 것은 뭐야?
A. items, nextCursor, hasNext를 초기화해야 한다.

Q. TanStack Query에서는 reset을 직접 해야 해?
A. queryKey가 변경되면 별도 cache로 관리된다. 다만 로컬 items를 직접 관리한다면 reset이 필요하다.

Q. 필터 변경 후 이전 데이터가 섞여 보여?
A. items reset이나 queryKey 변경이 누락되었을 가능성이 있다.

---

# 14. Sorting and Page Size Rules

## 14.1 Sort / Size Parameter 기준

### [개념]

Sorting은 목록 데이터를 특정 필드와 방향 기준으로 정렬하는 기능이다.

Page Size는 한 번의 목록 API 요청에서 가져올 데이터 개수다.

정렬 조건이나 page size가 바뀌면 기존 page 번호가 유효하지 않을 수 있으므로 page reset이 필요하다.

---

### [핵심]

Sort 대상:

- createdAt
- updatedAt
- eventStartDate
- popularity
- rating
- likeCount
- title

Sort Direction:

- asc
- desc

Page Size 기준:

- 기본 목록: 10 / 20
- 카드 목록: 12 / 20
- 테이블 목록: 20 / 50
- 모바일 목록: 10 / 20
- 더보기: 10 / 20

주의:

- Backend 허용 sort field 확인
- UI label과 API sort value 구분
- sort 변경 시 page reset
- size 변경 시 page reset
- queryKey에 sort / size 포함
- 잘못된 sort field는 400 가능
- 너무 큰 size는 초기 로딩 지연

---

### [실무]

Sort Option Type:

```typescript
export type SortOption = {
  label: string;
  value: string;
};

export const festivalSortOptions: SortOption[] = [
  { label: "시작일 빠른순", value: "eventStartDate,asc" },
  { label: "평점 높은순", value: "averageRating,desc" },
  { label: "인기순", value: "likeCount,desc" },
];
```

Sort 변경:

```typescript
function handleSortChange(sort: string) {
  setSubmittedParams((prev) => ({
    ...prev,
    sort,
    page: 0,
  }));

  setUiPage(1);
}
```

Size 변경:

```typescript
function handlePageSizeChange(size: number) {
  setSubmittedParams((prev) => ({
    ...prev,
    page: 0,
    size,
  }));

  setUiPage(1);
}
```

---

### [FAQ]

Q. sort parameter는 어떻게 보내?
A. Backend 기준에 따라 다르지만 Spring Pageable에서는 보통 `sort=field,direction` 형식을 사용한다.

Q. 정렬 조건이 바뀌면 page를 reset해야 해?
A. 보통 reset하는 것이 좋다. 기존 page 번호가 새 정렬 결과에서 의미가 달라질 수 있다.

Q. page size는 몇 개가 좋아?
A. 화면과 데이터 성격에 따라 다르지만 목록은 10~20개, 테이블은 20~50개를 자주 사용한다.

Q. size 변경 시 page는 어떻게 해?
A. 보통 page 0 또는 UI page 1로 reset한다.

---

# 15. Accessibility and UX Rules

## 15.1 Pagination / Infinite Scroll 접근성 기준

### [개념]

Pagination과 Infinite Scroll은 사용자가 목록 탐색 상태를 이해하고 제어할 수 있게 설계해야 한다.

특히 Infinite Scroll은 Footer 접근, 키보드 탐색, 보조 기술 사용자에게 문제가 될 수 있으므로 fallback UI를 고려한다.

---

### [핵심]

Pagination 접근성:

- nav aria-label
- 현재 페이지 표시
- button disabled
- keyboard focus
- 페이지 변경 후 focus 관리 가능
- 명확한 버튼 label

Infinite Scroll 접근성:

- Load More fallback
- loading text 제공
- 마지막 항목 안내
- footer 접근성 고려
- 자동 로딩 남발 방지
- 스크린 리더 상태 안내 가능

주의:

- 버튼을 div로 만들지 않음
- 색상만으로 현재 페이지 표시 금지
- disabled 상태 시각적 표시
- Infinite Scroll에서 사용자가 제어할 수 있는 대안 제공
- Skeleton만 있고 텍스트가 없으면 접근성 부족 가능

---

### [실무]

Pagination nav:

```tsx
<nav aria-label="검색 결과 페이지">
  <button type="button" disabled={pageInfo.first} onClick={goPrev}>
    이전 페이지
  </button>

  <span aria-current="page">
    {pageInfo.currentPage} / {pageInfo.totalPages}
  </span>

  <button type="button" disabled={pageInfo.last} onClick={goNext}>
    다음 페이지
  </button>
</nav>
```

Infinite Scroll fallback:

```tsx
{
  hasNext && (
    <button type="button" disabled={loadingMore} onClick={loadMore}>
      {loadingMore ? "불러오는 중..." : "더보기"}
    </button>
  );
}

{
  !hasNext && <p>마지막 항목입니다.</p>;
}
```

Loading 안내:

```tsx
{
  loadingMore && <p aria-live="polite">추가 데이터를 불러오는 중입니다.</p>;
}
```

---

### [FAQ]

Q. Pagination에 nav를 써야 해?
A. 페이지 이동 영역임을 명확히 하기 위해 `nav aria-label`을 사용할 수 있다.

Q. Infinite Scroll은 접근성 문제가 있어?
A. 자동 로딩으로 footer 접근이나 키보드 탐색이 어려울 수 있어 Load More fallback을 고려하는 것이 좋다.

Q. 현재 페이지는 어떻게 표시해?
A. 시각적 표시와 함께 `aria-current="page"`를 사용할 수 있다.

Q. 무한 스크롤에서 마지막 항목 안내가 필요해?
A. 사용자가 더 이상 불러올 데이터가 없음을 알 수 있도록 안내하는 것이 좋다.

---

# 16. Testing and Debugging Rules

## 16.1 Pagination / Infinite Scroll 검수 기준

### [개념]

Pagination과 Infinite Scroll 검수는 page, size, sort, filter, hasNext, content append, reset, 중복 요청이 정상 동작하는지 확인하는 과정이다.

---

### [핵심]

검수 대상:

- Request URL
- Query Parameter
- page
- size
- sort
- Response content
- totalPages
- totalElements
- hasNext
- last
- nextCursor
- append
- replace
- reset
- duplicate request
- loadingMore
- Empty State
- Error State

검수 도구:

- Browser Network Tab
- Backend API Spec
- Swagger UI
- Mock Data
- Network throttling
- React Query Devtools
- Console Debug

---

### [실무]

Pagination 검수 Flow:

```text
Page Button Click
→ Network Request page 확인
→ Response number 확인
→ content 교체 확인
→ currentPage 표시 확인
→ first / last 버튼 disabled 확인
```

Load More 검수 Flow:

```text
Load More Click
→ Network Request page or cursor 확인
→ Response content 확인
→ 기존 items append 확인
→ hasNext 업데이트 확인
→ 중복 요청 없음 확인
```

Search Reset 검수:

```text
Search Condition Change
→ page 0 request 확인
→ 기존 Infinite Items 초기화 확인
→ 새 content만 표시 확인
```

문제 해결 우선순위:

```text
Network Request Query 확인
→ Response Body 확인
→ content 위치 확인
→ append / replace 확인
→ page / cursor update 확인
→ hasNext / last 확인
→ UI State 확인
```

---

### [FAQ]

Q. Pagination은 어떻게 테스트해?
A. 페이지 버튼 클릭 후 Network 요청의 page, size, sort와 Response의 content, number, totalPages를 확인한다.

Q. Infinite Scroll은 어떻게 테스트해?
A. 더보기 또는 스크롤 하단 진입 시 다음 요청이 한 번만 나가고 content가 append되는지 확인한다.

Q. 검색 조건 변경 후 이전 데이터가 섞이면 뭘 봐?
A. items reset, queryKey 변경, page 또는 cursor 초기화 여부를 확인해야 한다.

Q. 중복 요청은 어디서 확인해?
A. 브라우저 Network 탭에서 같은 API가 연속으로 여러 번 호출되는지 확인한다.

---

# 17. Common Mistakes

## 17.1 Pagination / Infinite Scroll 공통 실수

### [개념]

Pagination과 Infinite Scroll 실수는 page index, response mapping, append / replace 기준, reset 기준, 중복 요청 방지 기준이 불명확할 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Spring Pageable 0-based를 UI 1-based와 혼동
- queryKey에 page 누락
- queryKey에 size 누락
- queryKey에 sort / filter 누락
- 검색 조건 변경 시 page reset 누락
- size 변경 시 page reset 누락
- Page Response에서 content 위치 착각
- Page Response 전체를 배열처럼 사용
- Slice Response에서 totalPages 기대
- Pagination에서 append 처리
- Load More에서 replace 처리
- Infinite Scroll에서 기존 items 교체
- hasNext false인데 계속 요청
- loadingMore guard 누락
- Intersection Observer cleanup 누락
- 같은 page 중복 요청
- cursor reset 누락
- nextCursor null인데 요청
- sort label을 API로 전송
- `/api` path 문제를 pagination 문제로 착각
- Network 탭 확인 없이 state만 수정

---

### [실무]

문제 예:

```text
문제: 2페이지를 눌렀는데 3페이지 데이터가 나옴
원인: UI page 1-based와 Backend page 0-based 변환 오류
해결: API 요청 시 page = uiPage - 1 적용
```

문제 예:

```text
문제: 검색 조건 변경 후 결과가 비어 있음
원인: 기존 page가 높은 번호로 유지됨
해결: 검색 조건 변경 시 page 0으로 reset
```

문제 예:

```text
문제: 더보기 클릭 시 기존 목록이 사라짐
원인: append가 아니라 replace 처리
해결: setItems(prev => [...prev, ...content]) 적용
```

문제 예:

```text
문제: 무한 스크롤에서 같은 데이터 반복
원인: page 증가 또는 cursor 업데이트 누락
해결: response.number + 1 또는 nextCursor 저장 기준 확인
```

해결 우선순위:

```text
Request page / cursor 확인
→ Response content 확인
→ append / replace 확인
→ hasNext / last 확인
→ reset 기준 확인
→ 중복 요청 확인
```

---

### [FAQ]

Q. Pagination에서 가장 흔한 실수는?
A. UI page 1-based와 Backend page 0-based를 혼동하는 것이다.

Q. Infinite Scroll에서 가장 흔한 실수는?
A. content append를 하지 않거나 loadingMore guard 없이 중복 요청을 보내는 것이다.

Q. 검색 조건 변경 후 빈 화면이 나와?
A. 기존 page 번호가 유지되어 존재하지 않는 페이지를 요청했을 수 있다. page reset을 확인해야 한다.

Q. 같은 데이터가 반복해서 보여?
A. page 증가, cursor 업데이트, 중복 요청 방지, key 중복 여부를 확인해야 한다.

---

# 18. Part08 Checklist

## 18.1 Pagination and Infinite Scroll 검수 기준

### [개념]

Part08 Pagination and Infinite Scroll 문서는 Frontend Agent가 Page / Slice / Cursor Response를 구분하고, 목록 데이터를 교체하거나 append하는 UI를 안정적으로 구현하도록 만드는 문서다.

---

### [핵심]

Checklist:

```md
- [ ] Pagination / Infinite Scroll 개념이 포함되었는가?
- [ ] Page Response 기준이 포함되었는가?
- [ ] Slice Response 기준이 포함되었는가?
- [ ] Cursor Response 기준이 포함되었는가?
- [ ] Offset Pagination 기준이 포함되었는가?
- [ ] Pagination UI State 기준이 포함되었는가?
- [ ] 검색 조건 변경 시 Page Reset 기준이 포함되었는가?
- [ ] Replace vs Append 기준이 포함되었는가?
- [ ] Load More 기준이 포함되었는가?
- [ ] Infinite Scroll 기준이 포함되었는가?
- [ ] useInfiniteQuery 기준이 포함되었는가?
- [ ] Duplicate Request Prevention 기준이 포함되었는가?
- [ ] Reset 기준이 포함되었는가?
- [ ] Sorting and Page Size 기준이 포함되었는가?
- [ ] Accessibility and UX 기준이 포함되었는가?
- [ ] Testing and Debugging 기준이 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Page Response Check
→ Slice Response Check
→ Cursor Response Check
→ page / size / sort Check
→ UI page Conversion Check
→ Replace / Append Check
→ Reset Check
→ Duplicate Request Check
→ Accessibility Check
→ Network Debugging Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

최종 기준:

- Page / Slice / Cursor Response 구분 가능
- UI page와 Backend page 변환 가능
- 검색 조건 변경 시 page reset 가능
- Page Response 기반 Pagination 구현 가능
- Slice Response 기반 Load More 구현 가능
- Cursor 기반 더보기 구현 가능
- useInfiniteQuery로 Infinite Scroll 구현 가능
- 중복 요청과 데이터 섞임 문제를 방지 가능
- Frontend Agent가 안정적인 목록 Data Fetching UI를 생성 가능

---

### [FAQ]

Q. Part08의 목적은 뭐야?
A. Frontend Agent가 Page / Slice / Cursor Response를 구분하고 Pagination, Load More, Infinite Scroll UI를 안정적으로 구현하게 만드는 것이다.

Q. Part08에서 가장 중요한 기준은 뭐야?
A. UI page와 Backend page 변환, content append / replace 구분, 검색 조건 변경 시 reset, 중복 요청 방지다.

Q. Part08은 Part06과 어떻게 달라?
A. Part06은 Loading / Error / Empty 같은 UI State 중심이고, Part08은 Page / Slice / Cursor 기반 목록 분할 조회 구현 중심이다.

---

# Retrieval Queries

### [FAQ]

Q. Pagination과 Infinite Scroll 차이는?
A. Pagination은 페이지 번호를 기준으로 목록을 교체하고 Infinite Scroll은 다음 데이터를 계속 append한다.

Q. Page Response와 Slice Response 차이는?
A. Page는 totalPages와 totalElements를 포함하고 Slice는 다음 페이지 존재 여부 중심으로 동작한다.

Q. 전체 페이지 수가 필요하면 뭘 써?
A. Page Response 기반 Pagination을 사용하는 것이 좋다.

Q. 무한 스크롤에는 Page보다 Slice가 좋아?
A. 전체 개수가 필요 없다면 Slice가 더 가볍고 무한 스크롤에 적합하다.

Q. Page Response에서 실제 목록은 어디에 있어?
A. 보통 `content` 필드에 실제 목록 배열이 들어 있다.

Q. totalPages는 언제 필요해?
A. 페이지 번호 버튼이나 마지막 페이지 여부를 표시할 때 필요하다.

Q. totalElements는 언제 필요해?
A. 전체 검색 결과 개수나 전체 항목 수를 보여줄 때 필요하다.

Q. Page Response에서 content만 반환해도 돼?
A. 페이지 UI에 totalPages, totalElements가 필요하면 Page 객체 전체를 반환해야 한다.

Q. Slice Response는 언제 써?
A. 전체 개수보다 다음 페이지 존재 여부가 중요한 더보기, 무한 스크롤, 채팅, 알림 목록에 적합하다.

Q. Slice Response에는 totalPages가 없어?
A. 없을 수 있다. Slice는 전체 페이지 수보다 다음 데이터 존재 여부를 중심으로 한다.

Q. Slice Response의 content는 어떻게 처리해?
A. 더보기나 무한 스크롤에서는 기존 items에 append한다.

Q. hasNext와 last는 어떻게 써?
A. hasNext가 false이거나 last가 true이면 다음 요청을 중단한다.

Q. Cursor Pagination은 뭐야?
A. page 번호 대신 마지막 데이터의 cursor를 기준으로 다음 데이터를 조회하는 방식이다.

Q. Cursor Pagination은 언제 좋아?
A. 대용량 목록, 실시간으로 데이터가 추가되는 목록, 무한 스크롤에 적합하다.

Q. Cursor 방식은 특정 페이지로 바로 이동할 수 있어?
A. 일반적으로 어렵다. Cursor 방식은 순차적인 더보기 흐름에 적합하다.

Q. nextCursor가 null이면 어떻게 해?
A. 더 이상 가져올 데이터가 없으므로 추가 요청을 중단한다.

Q. Offset Pagination은 뭐야?
A. page와 size를 기준으로 특정 페이지의 데이터를 조회하는 방식이다.

Q. Spring Pageable page는 0부터 시작해?
A. 일반적으로 0-based다. UI에서 1부터 보여주면 요청 시 변환이 필요하다.

Q. sort는 Query Parameter로 보내?
A. Spring Pageable에서는 보통 `sort=field,direction` 형태로 보낸다.

Q. 검색 조건이 바뀌면 page는 어떻게 해?
A. 대부분 backend page 0 또는 UI page 1로 reset한다.

Q. Pagination UI에서 currentPage는 backend page 그대로 써?
A. 보통 UI는 1-based로 표시하므로 backend page에 1을 더해 사용한다.

Q. 이전 버튼은 언제 disabled 해?
A. Page Response의 first가 true이거나 현재 요청이 loading 중일 때 disabled 한다.

Q. 다음 버튼은 언제 disabled 해?
A. Page Response의 last가 true이거나 현재 요청이 loading 중일 때 disabled 한다.

Q. totalPages가 0이면 어떻게 보여줘?
A. 목록은 Empty State로 처리하고 페이지 버튼은 숨기거나 비활성화할 수 있다.

Q. 검색 조건이 바뀌면 page를 왜 reset해?
A. 기존 page 번호가 새 검색 결과에서는 존재하지 않을 수 있기 때문이다.

Q. 검색어 입력마다 API 요청을 보내야 해?
A. UX 기준에 따라 다르다. 검색 버튼 submit 방식이나 debounce 방식을 사용할 수 있다.

Q. 입력 중인 keyword와 submitted keyword는 왜 나눠?
A. 사용자가 입력 중인 값과 실제 API 요청에 사용되는 조건을 분리하기 위해서다.

Q. page reset을 안 하면 어떤 문제가 생겨?
A. 새 검색 결과에서 존재하지 않는 page를 요청해 빈 화면이 나올 수 있다.

Q. Pagination은 append야 replace야?
A. 보통 replace다. 페이지를 이동하면 해당 페이지 content로 목록을 교체한다.

Q. Load More는 append야 replace야?
A. append다. 기존 items 뒤에 새 content를 추가한다.

Q. 검색 조건 변경 후 append하면 안 돼?
A. 조건이 다른 데이터가 섞일 수 있으므로 reset 후 새 결과를 사용해야 한다.

Q. 더보기 클릭 후 기존 목록이 사라지면?
A. append가 아니라 replace로 처리했을 가능성이 높다.

Q. Load More는 Infinite Scroll과 뭐가 달라?
A. Load More는 사용자가 버튼을 눌러 추가 데이터를 가져오고 Infinite Scroll은 스크롤 위치에 따라 자동 요청한다.

Q. Load More에서는 기존 목록을 교체해?
A. 아니다. 기존 items에 새 content를 append한다.

Q. Load More 버튼은 언제 숨겨?
A. hasNext가 false이거나 last가 true이면 숨기거나 disabled 할 수 있다.

Q. Load More 실패 시 기존 목록은 지워?
A. 보통 지우지 않는다. 기존 목록은 유지하고 오류 메시지나 재시도 버튼을 제공한다.

Q. Infinite Scroll은 언제 써?
A. 피드, 알림, 댓글, 리뷰처럼 계속 이어지는 목록 UI에 사용한다.

Q. Infinite Scroll에서 중복 요청은 어떻게 막아?
A. loadingMore 상태와 hasNext 상태를 확인해 요청 중이거나 다음 데이터가 없으면 호출하지 않는다.

Q. Intersection Observer를 쓰는 이유는?
A. scroll event보다 효율적으로 특정 요소가 화면에 들어왔는지 감지할 수 있기 때문이다.

Q. Infinite Scroll에도 더보기 버튼이 필요해?
A. 접근성과 제어성을 위해 fallback으로 제공하는 것이 좋을 수 있다.

Q. useInfiniteQuery는 언제 써?
A. 더보기 버튼이나 무한 스크롤처럼 여러 페이지 데이터를 누적해서 보여줄 때 사용한다.

Q. data.pages는 뭐야?
A. 각 페이지 응답이 순서대로 들어 있는 배열이다.

Q. 목록 배열은 어떻게 만들어?
A. `data.pages.flatMap(page => page.content)`처럼 각 페이지의 content를 합친다.

Q. getNextPageParam은 뭘 반환해야 해?
A. 다음 요청에 사용할 page 번호나 cursor를 반환하고, 다음 데이터가 없으면 undefined를 반환한다.

Q. 더보기 버튼을 여러 번 누르면 어떻게 막아?
A. loadingMore 상태와 disabled 버튼을 사용해 요청 중에는 추가 클릭을 막는다.

Q. Infinite Scroll에서 같은 페이지가 여러 번 호출돼?
A. loadingMore guard, hasNext check, observer cleanup, page update 타이밍을 확인해야 한다.

Q. Pagination 버튼 중복 요청은 어떻게 막아?
A. loading 중 page button을 disabled 처리하고 page 변경 요청을 중복 실행하지 않도록 한다.

Q. 중복 요청 여부는 어디서 확인해?
A. 브라우저 Network 탭에서 같은 API 요청이 여러 번 나갔는지 확인한다.

Q. 검색 조건이 바뀌면 기존 items를 지워야 해?
A. Infinite Scroll이나 Load More에서는 지우는 것이 안전하다. Pagination은 새 Page Response로 교체한다.

Q. Cursor 방식에서 reset할 것은 뭐야?
A. items, nextCursor, hasNext를 초기화해야 한다.

Q. TanStack Query에서는 reset을 직접 해야 해?
A. queryKey가 변경되면 별도 cache로 관리된다. 다만 로컬 items를 직접 관리한다면 reset이 필요하다.

Q. 필터 변경 후 이전 데이터가 섞여 보여?
A. items reset이나 queryKey 변경이 누락되었을 가능성이 있다.

Q. sort parameter는 어떻게 보내?
A. Backend 기준에 따라 다르지만 Spring Pageable에서는 보통 `sort=field,direction` 형식을 사용한다.

Q. 정렬 조건이 바뀌면 page를 reset해야 해?
A. 보통 reset하는 것이 좋다. 기존 page 번호가 새 정렬 결과에서 의미가 달라질 수 있다.

Q. page size는 몇 개가 좋아?
A. 화면과 데이터 성격에 따라 다르지만 목록은 10~20개, 테이블은 20~50개를 자주 사용한다.

Q. size 변경 시 page는 어떻게 해?
A. 보통 page 0 또는 UI page 1로 reset한다.

Q. Pagination에 nav를 써야 해?
A. 페이지 이동 영역임을 명확히 하기 위해 `nav aria-label`을 사용할 수 있다.

Q. Infinite Scroll은 접근성 문제가 있어?
A. 자동 로딩으로 footer 접근이나 키보드 탐색이 어려울 수 있어 Load More fallback을 고려하는 것이 좋다.

Q. 현재 페이지는 어떻게 표시해?
A. 시각적 표시와 함께 `aria-current="page"`를 사용할 수 있다.

Q. 무한 스크롤에서 마지막 항목 안내가 필요해?
A. 사용자가 더 이상 불러올 데이터가 없음을 알 수 있도록 안내하는 것이 좋다.

Q. Pagination은 어떻게 테스트해?
A. 페이지 버튼 클릭 후 Network 요청의 page, size, sort와 Response의 content, number, totalPages를 확인한다.

Q. Infinite Scroll은 어떻게 테스트해?
A. 더보기 또는 스크롤 하단 진입 시 다음 요청이 한 번만 나가고 content가 append되는지 확인한다.

Q. 검색 조건 변경 후 이전 데이터가 섞이면 뭘 봐?
A. items reset, queryKey 변경, page 또는 cursor 초기화 여부를 확인해야 한다.

Q. 중복 요청은 어디서 확인해?
A. 브라우저 Network 탭에서 같은 API가 연속으로 여러 번 호출되는지 확인한다.

Q. Pagination에서 가장 흔한 실수는?
A. UI page 1-based와 Backend page 0-based를 혼동하는 것이다.

Q. Infinite Scroll에서 가장 흔한 실수는?
A. content append를 하지 않거나 loadingMore guard 없이 중복 요청을 보내는 것이다.

Q. 검색 조건 변경 후 빈 화면이 나와?
A. 기존 page 번호가 유지되어 존재하지 않는 페이지를 요청했을 수 있다. page reset을 확인해야 한다.

Q. 같은 데이터가 반복해서 보여?
A. page 증가, cursor 업데이트, 중복 요청 방지, key 중복 여부를 확인해야 한다.

Q. Part08 Pagination and Infinite Scroll의 목적은 뭐야?
A. Frontend Agent가 Page / Slice / Cursor Response를 구분하고 Pagination, Load More, Infinite Scroll UI를 안정적으로 구현하게 만드는 것이다.

Q. Part08은 Part06과 어떻게 달라?
A. Part06은 Loading / Error / Empty 같은 UI State 중심이고, Part08은 Page / Slice / Cursor 기반 목록 분할 조회 구현 중심이다.
