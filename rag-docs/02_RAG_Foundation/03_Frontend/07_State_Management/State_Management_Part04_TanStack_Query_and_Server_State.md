# State Management Part04 - TanStack Query and Server State

---

# 1. Server State Overview

## 1.1 Server State Purpose

### [개념]

Server State는 서버가 원본을 소유하고 Frontend가 조회, 표시, 캐싱, 갱신, 동기화하는 데이터다.

Server State는 Client State와 다르게 cache, stale data, refetch, mutation, invalidation, pagination 문제가 있다.

Server State는 일반적인 Global Store에 무분별하게 복사하지 않는다.

---

### [핵심]

Server State 핵심 요소:

- API Data
- Server Ownership
- Async Loading
- Error State
- Cache
- Stale Data
- Refetch
- Mutation
- Invalidation
- Pagination
- Background Update
- Query Cache
- Optimistic Update

---

### [실무]

2026 실무 기준에서 API 응답 데이터는 대부분 Server State로 분류한다.

```text
API 응답 데이터 발견
→ 서버가 원본인지 확인
→ 캐시 필요 여부 확인
→ stale data 가능성 확인
→ refetch 필요 여부 확인
→ mutation 후 갱신 필요 여부 확인
→ TanStack Query 검토
```

Server State 예:

```text
festival list
festival detail
review list
notification list
favorite list
user profile
donation history
chat room list
server pagination result
```

주의:

- API 데이터를 Zustand나 Redux Toolkit에 기본 저장하지 않는다.
- Query Cache와 Global Store에 같은 서버 데이터를 중복 저장하지 않는다.
- Server State는 서버 동기화 기준이 중요하다.
- UI 선택값은 Client State, 선택값으로 조회한 데이터는 Server State로 분리할 수 있다.

---

### [FAQ]

Q. Server State가 뭐야?
A. 서버가 원본으로 소유하고 Frontend가 조회, 캐싱, 갱신, 동기화하는 데이터다.

Q. API 응답 데이터는 대부분 Server State야?
A. 맞다. 서버가 원본을 소유하고 Frontend는 이를 가져와 표시하거나 캐싱한다.

Q. Server State를 Global Store에 넣으면 안 돼?
A. 가능은 하지만 cache, stale data, refetch, invalidation을 직접 관리해야 하므로 TanStack Query 같은 도구가 더 적합한 경우가 많다.

---

# 2. Client State vs Server State

## 2.1 Ownership Difference

### [개념]

Client State와 Server State의 가장 큰 차이는 원본 소유자다.

Client State는 Frontend가 원본을 소유하고, Server State는 Backend 또는 Server가 원본을 소유한다.

---

### [핵심]

Client State 예:

- modal open
- selected tab
- input value
- sidebar open
- theme
- local filter draft
- selected item id
- form value

Server State 예:

- user profile
- festival list
- festival detail
- review list
- notification list
- favorite list
- server page result
- API response data

---

### [실무]

Client State vs Server State:

| 비교           | Client State                     | Server State                |
| -------------- | -------------------------------- | --------------------------- |
| 원본 소유자    | Frontend                         | Backend / Server            |
| 예시           | modal open, input value          | festival list, user profile |
| 관리 도구      | useState, Zustand, Redux Toolkit | TanStack Query              |
| 주요 문제      | State 위치, Props Drilling       | cache, stale data, refetch  |
| 갱신 방식      | setState / Store Action          | mutation / invalidation     |
| 새로고침       | 기본적으로 사라짐                | 서버에서 다시 조회          |
| 중복 저장 위험 | Derived State                    | Query Cache와 Store 불일치  |

판단 기준:

```text
서버 DB 또는 API가 원본이다
→ Server State

브라우저 UI가 원본이다
→ Client State

목록에서 선택한 id
→ Client State

선택한 id로 조회한 상세 데이터
→ Server State
```

---

### [FAQ]

Q. Client State와 Server State를 왜 구분해?
A. 소유자와 갱신 방식이 다르기 때문이다. Server State는 캐시와 서버 동기화가 중요하다.

Q. selectedFestivalId는 Server State야?
A. 보통 selectedFestivalId는 Client State이고, 해당 id로 조회한 festival detail은 Server State다.

Q. user profile은 Client State야 Server State야?
A. 서버에서 조회한 원본 프로필은 Server State이고, 로그인 여부나 사용자 요약은 Auth State로 분리할 수 있다.

---

## 2.2 Server State Misclassification

### [개념]

Server State Misclassification은 API 데이터를 Client State처럼 Store나 Component State에 복사해 관리하는 문제다.

Server State를 잘못 분류하면 stale data, mutation 후 미갱신, 중복 loading/error 상태 문제가 발생한다.

---

### [핵심]

잘못된 분류 예:

- festivalList를 Zustand Store에 저장
- reviewList를 Redux Slice에 저장
- userProfile을 authStore와 query cache에 중복 저장
- API pagination result를 local state에 장기 저장
- 서버 filter 결과를 derived state처럼 중복 저장
- mutation 후 Store 일부만 수동 갱신

---

### [실무]

문제 Flow:

```text
API Data를 Store에 저장
→ 다른 화면에서도 같은 데이터 조회
→ mutation 발생
→ Store 갱신 누락
→ Query Cache와 Store 불일치
→ stale UI 발생
```

개선 Flow:

```text
API Data
→ TanStack Query Cache
→ queryKey로 식별
→ mutation 후 invalidateQueries
→ 필요한 UI State만 Store에 분리
```

예:

```text
festivalList
→ TanStack Query

searchKeyword
→ URL State

selectedFestivalId
→ Client State 또는 URL State

favoriteButtonLoading
→ Mutation State 또는 Local UI State
```

---

### [FAQ]

Q. Server State를 Client State로 잘못 관리하면 어떤 문제가 생겨?
A. 오래된 데이터, 중복 저장, mutation 후 미갱신, loading/error 중복 관리 문제가 생긴다.

Q. API 데이터를 Store에 저장하면 무조건 틀려?
A. 무조건은 아니지만 캐시와 동기화가 필요하면 TanStack Query 같은 Server State 도구가 더 적합하다.

Q. Server State와 Client State를 같이 써도 돼?
A. 가능하다. 서버 데이터는 Query Cache에 두고 화면 선택값이나 UI 상태는 Client State로 분리한다.

---

# 3. TanStack Query Overview

## 3.1 TanStack Query Purpose

### [개념]

TanStack Query는 API 데이터 같은 Server State를 조회, 캐싱, 갱신, 동기화하는 도구다.

TanStack Query는 일반 Client State 전역 관리 도구가 아니라 Server State 관리 도구에 가깝다.

---

### [핵심]

TanStack Query 핵심 기능:

- QueryClient
- QueryClientProvider
- useQuery
- useMutation
- queryKey
- queryFn
- mutationFn
- Query Cache
- invalidateQueries
- refetch
- staleTime
- gcTime
- loading state
- error state
- pagination support
- optimistic update

---

### [실무]

TanStack Query 적용 Flow:

```text
API Data 필요
→ queryKey 설계
→ queryFn 작성
→ useQuery로 조회
→ loading / error / empty 처리
→ mutation 작성
→ invalidateQueries로 갱신
```

TanStack Query 적합 예:

```text
festival list 조회
festival detail 조회
review list 조회
notification list 조회
favorite list 조회
user profile 조회
donation history 조회
server pagination 조회
```

TanStack Query 부적합 예:

```text
modal open
selected tab
input value
theme
sidebar open
form dirty state
local validation message
```

---

### [FAQ]

Q. TanStack Query는 전역 상태관리야?
A. 일반 Client State 전역 관리 도구라기보다 Server State와 API 캐시 관리 도구에 가깝다.

Q. TanStack Query는 언제 써?
A. API 데이터 조회, 캐싱, refetch, mutation, stale data 관리가 필요할 때 사용한다.

Q. TanStack Query로 modal open 같은 UI State도 관리해?
A. 권장하지 않는다. modal open은 Client UI State이므로 useState나 Store가 적합하다.

---

## 3.2 QueryClient and Provider

### [개념]

QueryClient는 TanStack Query의 Query Cache와 기본 동작을 관리하는 객체다.

QueryClientProvider는 React App에 QueryClient를 공급해 useQuery와 useMutation이 Query Cache를 사용할 수 있게 한다.

---

### [핵심]

구성 요소:

- QueryClient
- QueryClientProvider
- defaultOptions
- queries option
- mutations option
- Query Cache
- Mutation Cache
- App Root Provider

---

### [실무]

기본 구조 예:

```tsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient();

root.render(
  <QueryClientProvider client={queryClient}>
    <App />
  </QueryClientProvider>,
);
```

기본 옵션 예:

```tsx
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60,
      retry: 1,
    },
  },
});
```

권장 기준:

- QueryClient는 App Root 근처에서 생성한다.
- 매 렌더링마다 QueryClient를 새로 만들지 않는다.
- 기본 staleTime, retry 정책을 프로젝트 기준으로 정한다.
- 개발 시 TanStack Query Devtools를 검토한다.
- logout 시 Query Cache clear 또는 invalidate 기준을 정한다.

---

### [FAQ]

Q. QueryClient는 뭐야?
A. TanStack Query의 cache, query, mutation 동작을 관리하는 핵심 객체다.

Q. QueryClientProvider는 왜 필요해?
A. App 하위에서 useQuery와 useMutation이 QueryClient와 Query Cache를 사용할 수 있게 하기 위해 필요하다.

Q. QueryClient를 Component 안에서 매번 생성해도 돼?
A. 권장하지 않는다. 매 렌더링마다 Cache가 초기화될 수 있으므로 안정적인 위치에서 생성해야 한다.

---

# 4. useQuery Rules

## 4.1 useQuery Purpose

### [개념]

useQuery는 서버 데이터를 조회하고 Query Cache에 저장하는 TanStack Query Hook이다.

GET 요청 기반 데이터 조회, loading 상태, error 상태, refetch, cache 관리를 담당한다.

---

### [핵심]

useQuery 구성:

- queryKey
- queryFn
- data
- isLoading
- isPending
- isFetching
- error
- refetch
- enabled
- staleTime
- select
- placeholderData
- initialData

---

### [실무]

기본 예:

```tsx
function FestivalListPage() {
  const { data, isLoading, error } = useQuery({
    queryKey: ["festivals"],
    queryFn: getFestivals,
  });

  if (isLoading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Failed to load festivals.</p>;
  }

  return <FestivalList festivals={data ?? []} />;
}
```

권장 기준:

- queryKey는 데이터 식별 기준으로 설계한다.
- queryFn은 API 요청 함수로 분리한다.
- UI State와 Server State를 분리한다.
- loading / error / empty 상태를 명시적으로 처리한다.
- queryKey에 검색 조건, page, id 같은 식별값을 포함한다.
- queryFn 내부에서 UI State를 변경하지 않는다.

---

### [FAQ]

Q. useQuery는 뭐야?
A. 서버 데이터를 조회하고 cache, loading, error, refetch 상태를 관리하는 TanStack Query Hook이다.

Q. useQuery에는 무엇이 필요해?
A. 데이터를 식별하는 queryKey와 API 요청을 수행하는 queryFn이 필요하다.

Q. useQuery data를 Zustand에 다시 저장해야 해?
A. 보통 필요 없다. Query Cache가 Server State의 Source of Truth가 되도록 두는 것이 좋다.

---

## 4.2 Query Function Rules

### [개념]

Query Function은 useQuery가 서버 데이터를 가져올 때 실행하는 API 요청 함수다.

Query Function은 같은 queryKey 조건에서 예측 가능한 데이터를 반환해야 한다.

---

### [핵심]

queryFn 규칙:

- API request 담당
- Promise 반환
- queryKey 조건과 일치
- UI Side Effect 금지
- setState 남용 금지
- Error throw 기준 명확화
- Response mapping 가능
- API Client 분리

---

### [실무]

API 함수 예:

```typescript
async function getFestivalDetail(festivalId: number) {
  const response = await publicApi.get(`/festival/detail/${festivalId}`);
  return response.data.data;
}
```

useQuery 예:

```tsx
const { data } = useQuery({
  queryKey: ["festival", festivalId],
  queryFn: () => getFestivalDetail(festivalId),
  enabled: Boolean(festivalId),
});
```

권장 기준:

- queryFn은 API 호출만 담당한다.
- queryFn에서 toast, navigation, modal open 같은 UI Side Effect를 하지 않는다.
- response 구조 변환은 API layer 또는 select에서 일관되게 처리한다.
- queryKey에 포함된 값과 queryFn 인자가 일치해야 한다.
- Error 처리는 API Client와 UI Error State 기준을 통일한다.

---

### [FAQ]

Q. queryFn은 뭐야?
A. useQuery가 서버 데이터를 가져올 때 실행하는 API 요청 함수다.

Q. queryFn 안에서 setState를 해도 돼?
A. 권장하지 않는다. queryFn은 서버 데이터 조회에 집중하고 UI 상태 변경은 외부에서 처리하는 것이 좋다.

Q. queryKey 값과 queryFn 인자는 같아야 해?
A. queryKey가 cache 식별 기준이므로 queryFn이 사용하는 조건과 일치해야 한다.

---

# 5. queryKey Rules

## 5.1 queryKey Purpose

### [개념]

queryKey는 TanStack Query Cache에서 데이터를 식별하는 고유 기준이다.

queryKey가 정확해야 cache hit, refetch, invalidation, pagination이 올바르게 동작한다.

---

### [핵심]

queryKey 역할:

- Cache 식별
- Refetch 대상 식별
- Invalidation 대상 식별
- Query Data 구분
- Parameter 반영
- Pagination 반영
- Filter 반영
- Detail ID 반영

---

### [실무]

queryKey 예:

```tsx
["festivals"][("festivals", { keyword, region, page })][
  ("festival", festivalId)
][("reviews", festivalId)][("notifications", userId)][("favorites", userId)];
```

권장 기준:

- queryKey는 배열로 작성한다.
- 첫 번째 값은 도메인 이름으로 작성한다.
- 상세 조회는 id를 queryKey에 포함한다.
- 목록 조회는 filter, sort, page를 포함한다.
- queryFn에서 사용하는 조건은 queryKey에도 포함한다.
- queryKey naming을 프로젝트 전체에서 통일한다.

---

### [FAQ]

Q. queryKey는 왜 중요해?
A. 캐시에서 데이터를 식별하고 refetch와 invalidation 대상을 결정하기 때문이다.

Q. queryKey에 id를 넣어야 해?
A. 상세 조회처럼 id별 데이터가 다르면 반드시 id를 포함해야 한다.

Q. 검색 조건도 queryKey에 넣어야 해?
A. 맞다. keyword, filter, page 같은 조회 조건이 다르면 서로 다른 cache로 구분해야 한다.

---

## 5.2 Query Key Factory

### [개념]

Query Key Factory는 queryKey를 일관되게 생성하는 함수 또는 객체 패턴이다.

queryKey 문자열과 구조가 흩어지면 invalidation 대상 지정이 어려워질 수 있다.

---

### [핵심]

Query Key Factory 목적:

- queryKey 일관성
- 오타 방지
- Invalidation 안정성
- 도메인별 key 관리
- Parameter 구조 통일
- Query Hook 재사용성 향상

---

### [실무]

Query Key Factory 예:

```typescript
export const festivalKeys = {
  all: ["festivals"] as const,
  lists: () => [...festivalKeys.all, "list"] as const,
  list: (params: FestivalSearchParams) =>
    [...festivalKeys.lists(), params] as const,
  details: () => [...festivalKeys.all, "detail"] as const,
  detail: (festivalId: number) =>
    [...festivalKeys.details(), festivalId] as const,
};
```

사용 예:

```tsx
useQuery({
  queryKey: festivalKeys.detail(festivalId),
  queryFn: () => getFestivalDetail(festivalId),
});
```

권장 기준:

- 반복되는 queryKey는 Factory로 관리한다.
- 도메인별 key 파일을 만들 수 있다.
- invalidation에서 Factory를 재사용한다.
- queryKey 구조 변경 시 한 곳에서 수정 가능하게 한다.

---

### [FAQ]

Q. Query Key Factory는 왜 필요해?
A. queryKey 구조를 일관되게 관리해 오타와 invalidation 오류를 줄이기 위해 필요하다.

Q. 모든 queryKey에 Factory가 필요해?
A. 작은 프로젝트에서는 필수는 아니지만 query가 많아지면 Factory가 유지보수에 유리하다.

Q. queryKey 문자열을 직접 여러 곳에 쓰면 안 돼?
A. 가능하지만 오타와 구조 불일치가 생기기 쉬워 Factory 사용을 검토하는 것이 좋다.

---

# 6. Query Parameters and URL State

## 6.1 URL State with Query Key

### [개념]

URL State와 queryKey는 목록 조회에서 함께 사용되는 경우가 많다.

검색 조건, 필터, 정렬, 페이지 번호는 URL에 저장하고 queryKey에 포함해 Server State 조회 조건으로 사용한다.

---

### [핵심]

URL State 대상:

- keyword
- region
- category
- sort
- page
- size
- date range
- selected tab

queryKey 반영 대상:

- URL keyword
- URL filter
- URL sort
- URL page
- URL size
- path parameter id

---

### [실무]

Flow:

```text
URL Query String
→ keyword / region / page 파싱
→ queryKey에 params 포함
→ useQuery 실행
→ Server State Cache 식별
→ URL 변경 시 다른 queryKey로 refetch
```

예:

```tsx
const params = {
  keyword: searchParams.get("keyword") ?? "",
  region: searchParams.get("region") ?? "",
  page: Number(searchParams.get("page") ?? 1),
};

const { data } = useQuery({
  queryKey: ["festivals", params],
  queryFn: () => getFestivals(params),
});
```

권장 기준:

- 검색 결과 공유가 필요하면 URL State를 사용한다.
- queryFn 조건은 queryKey와 일치시킨다.
- page, sort, filter 변경 시 queryKey가 바뀌게 한다.
- URL 값은 문자열이므로 타입 변환이 필요하다.
- Form 입력 중 임시값과 제출된 URL State를 구분한다.

---

### [FAQ]

Q. 검색 조건은 queryKey에 넣어야 해?
A. 맞다. 검색 조건이 다르면 다른 서버 데이터이므로 queryKey에 포함해야 한다.

Q. 검색 조건은 Store에 넣어야 해 URL에 넣어야 해?
A. 공유와 새로고침 복원이 필요하면 URL State가 적합하고, 그 값을 queryKey에 반영하는 것이 좋다.

Q. URL State와 TanStack Query를 같이 써도 돼?
A. 가능하다. URL State는 조회 조건을 관리하고 TanStack Query는 해당 조건의 Server State를 관리한다.

---

## 6.2 Form Draft vs Applied Query State

### [개념]

Form Draft State는 사용자가 입력 중인 임시값이고 Applied Query State는 실제 서버 조회에 사용되는 확정 조건이다.

검색 화면에서는 입력 중 값과 조회 조건을 분리하는 것이 중요하다.

---

### [핵심]

State 구분:

- Form Draft State
- Applied Search State
- URL State
- Query Key Params
- Server State
- Debounced Query
- Submit Search

---

### [실무]

검색 Flow:

```text
Input 입력 중
→ Form Local State

검색 Submit
→ URL Search Params 업데이트

URL Params 변경
→ queryKey 변경

queryKey 변경
→ Server State refetch
```

예:

```text
draftKeyword = "react"
→ 아직 서버 조회 X

submit
→ /festivals?keyword=react&page=1

queryKey = ["festivals", { keyword: "react", page: 1 }]
→ 서버 조회
```

권장 기준:

- 입력 중 임시값은 Local State로 둔다.
- 실제 검색 조건은 URL State로 둔다.
- queryKey는 실제 검색 조건 기준으로 만든다.
- debounce 검색은 별도 정책으로 설계한다.
- 검색 submit 시 page를 1로 초기화할 수 있다.

---

### [FAQ]

Q. 검색 input 값을 입력할 때마다 서버 조회해야 해?
A. 필수는 아니다. 입력 중 값은 Local State로 두고 submit 후 URL State를 변경해 조회할 수 있다.

Q. Form Draft State와 URL State를 왜 나눠?
A. 입력 중 임시값과 실제 검색 결과를 결정하는 조건이 다르기 때문이다.

Q. 검색 submit 후 page는 어떻게 해?
A. 검색 조건이 바뀌면 보통 page를 1로 초기화한다.

---

# 7. Loading, Error, Empty State

## 7.1 Loading State

### [개념]

Loading State는 서버 데이터를 조회하는 동안 UI가 대기 상태임을 표현하는 상태다.

TanStack Query는 isLoading, isPending, isFetching 같은 상태를 제공한다.

---

### [핵심]

Loading 관련 상태:

- isLoading
- isPending
- isFetching
- isRefetching
- initial loading
- background fetching
- skeleton UI
- spinner UI
- disabled action

---

### [실무]

기본 예:

```tsx
const { data, isLoading, isFetching } = useQuery({
  queryKey: ["festivals"],
  queryFn: getFestivals,
});

if (isLoading) {
  return <FestivalListSkeleton />;
}

return (
  <>
    {isFetching && <SmallLoadingIndicator />}
    <FestivalList festivals={data ?? []} />
  </>
);
```

권장 기준:

- 최초 로딩과 background fetching을 구분한다.
- 목록은 Skeleton UI를 검토한다.
- 버튼 action은 mutation loading 상태와 연결한다.
- loading 상태를 별도 Global Store에 중복 저장하지 않는다.
- Query 상태를 그대로 활용한다.

---

### [FAQ]

Q. TanStack Query loading 상태는 Store에 저장해야 해?
A. 보통 필요 없다. useQuery가 제공하는 loading 상태를 사용하면 된다.

Q. isLoading과 isFetching은 뭐가 달라?
A. isLoading은 초기 조회 상태에 가깝고, isFetching은 background refetch까지 포함하는 조회 중 상태로 볼 수 있다.

Q. 목록 조회 중에는 어떤 UI가 좋아?
A. 목록 Skeleton, 작은 loading indicator, 기존 데이터 유지 정책을 상황에 맞게 선택한다.

---

## 7.2 Error State

### [개념]

Error State는 서버 데이터 조회나 변경 요청이 실패했을 때 UI에 실패 상태를 표현하는 상태다.

TanStack Query는 error, isError, mutation error 상태를 제공한다.

---

### [핵심]

Error 처리 요소:

- error
- isError
- error message
- retry
- fallback UI
- toast
- boundary
- API Error mapping
- validation error
- network error

---

### [실무]

기본 예:

```tsx
const { data, isLoading, isError, error } = useQuery({
  queryKey: ["festival", festivalId],
  queryFn: () => getFestivalDetail(festivalId),
});

if (isError) {
  return <ErrorMessage message="Failed to load festival detail." />;
}
```

권장 기준:

- 사용자에게 보여줄 메시지와 개발자용 Error를 구분한다.
- API Error Response mapping 기준을 정한다.
- 재시도 버튼을 제공할 수 있다.
- 인증 오류는 Auth Flow와 연결한다.
- Error State를 무조건 Global Store에 저장하지 않는다.
- mutation error는 Form 또는 Toast와 연결할 수 있다.

---

### [FAQ]

Q. Query error도 Store에 저장해야 해?
A. 보통 필요 없다. useQuery와 useMutation이 제공하는 error 상태를 사용하고 필요 시 UI에서 메시지로 변환한다.

Q. 서버 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자용 메시지와 내부 로그용 메시지를 구분하는 것이 좋다.

Q. 인증 오류가 나면 어떻게 해?
A. Auth Flow와 연결해 refresh, logout, login redirect 기준을 적용한다.

---

## 7.3 Empty State

### [개념]

Empty State는 서버 조회는 성공했지만 표시할 데이터가 없는 상태다.

Empty State는 Loading State, Error State와 구분해야 한다.

---

### [핵심]

Empty State 예:

- 검색 결과 없음
- 리뷰 없음
- 알림 없음
- 찜 목록 없음
- 후원 내역 없음
- 채팅 메시지 없음

---

### [실무]

Empty State 판단 Flow:

```text
isLoading
→ Loading UI

isError
→ Error UI

data exists but empty
→ Empty UI

data exists
→ Content UI
```

예:

```tsx
if (festivals.length === 0) {
  return <EmptyMessage message="No festivals found." />;
}
```

권장 기준:

- Empty State는 Error가 아니다.
- 검색 조건이 있을 때와 없을 때 Empty 메시지를 다르게 할 수 있다.
- Empty UI는 다음 행동을 안내할 수 있다.
- Empty 여부 판단은 응답 구조에 맞게 통일한다.

---

### [FAQ]

Q. Empty State는 Error State야?
A. 아니다. 요청은 성공했지만 표시할 데이터가 없는 정상 상태다.

Q. 검색 결과가 없을 때는 어떻게 표시해?
A. 검색 조건에 맞는 결과가 없다는 메시지와 필터 초기화 같은 다음 행동을 제공할 수 있다.

Q. Empty State도 loading 이후에 판단해야 해?
A. 맞다. loading과 error가 아닌 상태에서 data가 비어 있는지 판단해야 한다.

---

# 8. Mutation Rules

## 8.1 useMutation Purpose

### [개념]

useMutation은 서버 데이터를 생성, 수정, 삭제하거나 서버 상태를 변경하는 요청을 관리하는 TanStack Query Hook이다.

Mutation은 POST, PUT, PATCH, DELETE 요청과 연결되는 경우가 많다.

---

### [핵심]

useMutation 구성:

- mutationFn
- mutate
- mutateAsync
- isPending
- isError
- isSuccess
- onSuccess
- onError
- onSettled
- invalidateQueries
- optimistic update

---

### [실무]

기본 예:

```tsx
const queryClient = useQueryClient();

const mutation = useMutation({
  mutationFn: likeFestival,
  onSuccess: () => {
    queryClient.invalidateQueries({
      queryKey: ["festival", festivalId],
    });
  },
});

function handleLike() {
  mutation.mutate(festivalId);
}
```

권장 기준:

- mutationFn은 API 변경 요청 함수로 분리한다.
- mutation 성공 후 관련 query를 invalidate한다.
- mutation loading 상태로 버튼 중복 클릭을 막을 수 있다.
- onError에서 사용자 메시지를 표시할 수 있다.
- mutation 결과를 Store에 수동으로 중복 저장하지 않는다.

---

### [FAQ]

Q. useMutation은 언제 써?
A. 서버 데이터를 생성, 수정, 삭제하거나 좋아요, 찜하기처럼 서버 상태를 변경할 때 사용한다.

Q. mutation 후 목록을 어떻게 갱신해?
A. 관련 queryKey를 invalidate해서 다시 조회하도록 처리할 수 있다.

Q. mutation loading 상태도 Store에 저장해야 해?
A. 보통 필요 없다. useMutation이 제공하는 isPending 같은 상태를 사용하면 된다.

---

## 8.2 Invalidation Rules

### [개념]

Invalidation은 mutation 이후 관련 Query Cache를 stale 상태로 만들고 다시 조회하도록 유도하는 작업이다.

Invalidation은 Server State 동기화의 핵심이다.

---

### [핵심]

Invalidation 대상:

- detail query
- list query
- count query
- related summary query
- user-specific query
- notification query
- favorite query

---

### [실무]

예:

```tsx
const queryClient = useQueryClient();

const mutation = useMutation({
  mutationFn: createReview,
  onSuccess: () => {
    queryClient.invalidateQueries({
      queryKey: ["reviews", festivalId],
    });

    queryClient.invalidateQueries({
      queryKey: ["festival", festivalId],
    });
  },
});
```

Invalidation 판단 Flow:

```text
Mutation 성공
→ 어떤 서버 데이터가 바뀌었는가?
→ 어떤 화면이 그 데이터를 사용하는가?
→ 어떤 queryKey가 관련되는가?
→ 관련 Query invalidate
```

주의:

- 너무 넓은 invalidation은 불필요한 refetch를 늘린다.
- 너무 좁은 invalidation은 stale UI를 남긴다.
- Query Key Factory를 사용하면 대상 지정이 안정적이다.
- mutation 결과로 직접 cache update할지 invalidate할지 기준을 정한다.

---

### [FAQ]

Q. invalidateQueries는 왜 써?
A. mutation 이후 관련 cache를 stale로 만들어 최신 서버 데이터를 다시 가져오기 위해 사용한다.

Q. 어떤 queryKey를 invalidate해야 해?
A. mutation으로 변경된 서버 데이터를 사용하는 list, detail, summary queryKey를 확인해야 한다.

Q. 모든 query를 invalidate하면 안 돼?
A. 가능은 하지만 불필요한 refetch가 많아질 수 있으므로 관련 query만 지정하는 것이 좋다.

---

## 8.3 Direct Cache Update

### [개념]

Direct Cache Update는 mutation 성공 후 refetch 없이 Query Cache 값을 직접 수정하는 방식이다.

즉시 UI 반영이 필요하거나 서버 응답에 최신 데이터가 포함된 경우 사용할 수 있다.

---

### [핵심]

사용 후보:

- setQueryData
- update detail cache
- update list cache
- mutation response
- immediate UI sync
- cache consistency
- optimistic update relation

---

### [실무]

예:

```tsx
const queryClient = useQueryClient();

const mutation = useMutation({
  mutationFn: updateFestivalTitle,
  onSuccess: (updatedFestival) => {
    queryClient.setQueryData(
      ["festival", updatedFestival.festivalId],
      updatedFestival,
    );
  },
});
```

판단 기준:

```text
mutation response에 최신 데이터가 있음
→ setQueryData 검토

관련 데이터가 복잡하게 여러 곳에 있음
→ invalidateQueries가 더 안전

즉시 UI 반영이 중요함
→ direct cache update 또는 optimistic update 검토
```

주의:

- list cache와 detail cache를 모두 고려해야 한다.
- 직접 수정 로직이 복잡하면 invalidation이 더 안전하다.
- Query Cache 구조를 정확히 알아야 한다.
- 서버 응답이 최신 데이터인지 확인해야 한다.

---

### [FAQ]

Q. mutation 후 refetch 대신 cache를 직접 바꿔도 돼?
A. 가능하다. 서버 응답에 최신 데이터가 있고 cache 구조가 명확하면 setQueryData를 사용할 수 있다.

Q. direct cache update와 invalidation 중 뭐가 좋아?
A. 단순하고 즉시 반영이 필요하면 direct update가 가능하고, 복잡한 연관 데이터는 invalidation이 더 안전하다.

Q. setQueryData를 쓸 때 주의할 점은?
A. 관련 list/detail cache 불일치가 생기지 않도록 cache 구조를 정확히 확인해야 한다.

---

# 9. Optimistic Update

## 9.1 Optimistic Update Purpose

### [개념]

Optimistic Update는 서버 응답을 기다리지 않고 성공할 것으로 가정해 UI를 먼저 갱신하는 방식이다.

좋아요, 찜하기처럼 빠른 피드백이 중요한 상호작용에서 사용할 수 있다.

---

### [핵심]

Optimistic Update 요소:

- onMutate
- cancelQueries
- previous data snapshot
- setQueryData
- rollback
- onError
- onSettled
- invalidateQueries

---

### [실무]

사용 후보:

```text
like toggle
favorite toggle
cart quantity update
simple status toggle
notification read status
```

적용 Flow:

```text
mutation 시작
→ 진행 중 query cancel
→ 이전 cache snapshot 저장
→ cache를 낙관적으로 변경
→ 실패 시 rollback
→ 성공/실패 후 invalidate 또는 refetch
```

주의:

- 실패 시 rollback 기준이 필요하다.
- 복잡한 데이터에는 적용을 신중히 한다.
- 중복 클릭, race condition을 고려한다.
- 서버 정책과 충돌할 수 있는 작업에는 주의한다.
- 낙관적 UI와 실제 서버 결과가 다를 수 있다.

---

### [FAQ]

Q. Optimistic Update는 언제 써?
A. 좋아요, 찜하기처럼 성공 가능성이 높고 빠른 UI 피드백이 중요한 작업에 사용할 수 있다.

Q. Optimistic Update가 항상 좋은가?
A. 아니다. 실패 가능성이 높거나 데이터 정합성이 중요한 작업에는 신중해야 한다.

Q. Optimistic Update에서 가장 중요한 것은 뭐야?
A. 실패 시 이전 상태로 되돌리는 rollback 기준이다.

---

## 9.2 Optimistic Update Caution

### [개념]

Optimistic Update Caution은 낙관적 업데이트가 데이터 불일치와 race condition을 만들 수 있다는 주의사항이다.

Optimistic Update는 UX 개선 도구지만 정합성 관리 비용이 있다.

---

### [핵심]

주의 상황:

- 결제
- 권한 변경
- 재고 차감
- 신청 마감
- 중복 요청 위험
- 서버 검증이 중요한 작업
- 여러 사용자가 동시에 수정하는 데이터
- 복잡한 nested list update

---

### [실무]

Optimistic Update 부적합 예:

```text
payment success
admin permission change
limited inventory reservation
festival application close
security-sensitive action
complex multi-entity update
```

대안:

```text
mutation loading 표시
버튼 disabled
서버 응답 후 invalidate
성공 toast
실패 message
refetch로 정합성 확보
```

판단 기준:

```text
성공 가능성이 매우 높음
→ optimistic update 가능

실패 시 영향이 작음
→ optimistic update 가능

정합성이 매우 중요함
→ 서버 응답 후 update

rollback이 복잡함
→ invalidation 우선
```

---

### [FAQ]

Q. 결제도 Optimistic Update로 처리해도 돼?
A. 권장하지 않는다. 결제는 서버 검증과 정합성이 중요하므로 서버 응답 후 상태를 반영해야 한다.

Q. Optimistic Update 실패 시 어떻게 해?
A. 이전 cache snapshot으로 rollback하고 사용자에게 실패 메시지를 제공해야 한다.

Q. 복잡한 목록 업데이트에도 Optimistic Update를 써도 돼?
A. 가능은 하지만 cache 수정과 rollback이 복잡하면 invalidateQueries가 더 안전하다.

---

# 10. Stale Time and Cache Time

## 10.1 staleTime Rules

### [개념]

staleTime은 Query Data가 fresh 상태로 간주되는 시간이다.

staleTime 동안에는 같은 queryKey 데이터가 신선하다고 보고 불필요한 refetch를 줄일 수 있다.

---

### [핵심]

staleTime 관련 개념:

- fresh data
- stale data
- refetch trigger
- cache reuse
- background refetch
- data freshness
- API traffic control

---

### [실무]

예:

```tsx
useQuery({
  queryKey: ["festivals"],
  queryFn: getFestivals,
  staleTime: 1000 * 60,
});
```

staleTime 판단 기준:

```text
자주 바뀌는 데이터
→ 짧은 staleTime

거의 안 바뀌는 코드성 데이터
→ 긴 staleTime

사용자 액션 후 즉시 갱신 필요
→ mutation 후 invalidate

실시간성이 중요함
→ 짧은 staleTime 또는 polling 검토
```

예시:

```text
festival category code
→ staleTime 길게 가능

festival detail
→ 중간

notification list
→ 짧게 또는 refetch 전략

chat message
→ Query보다 WebSocket / realtime strategy 검토
```

---

### [FAQ]

Q. staleTime은 뭐야?
A. Query Data를 fresh 상태로 간주하는 시간이다.

Q. staleTime을 길게 주면 뭐가 좋아?
A. 불필요한 refetch를 줄일 수 있지만 오래된 데이터가 보일 수 있다.

Q. 자주 바뀌는 데이터는 staleTime을 어떻게 해?
A. 짧게 설정하거나 mutation invalidation, polling, realtime 전략을 검토한다.

---

## 10.2 gcTime Rules

### [개념]

gcTime은 사용되지 않는 Query Cache가 메모리에 유지되는 시간이다.

이전 버전의 cacheTime 개념과 연결되며, Query가 inactive 된 뒤 cache가 제거되는 기준이다.

---

### [핵심]

gcTime 관련 개념:

- inactive query
- garbage collection
- cache retention
- memory usage
- return navigation
- cache reuse

---

### [실무]

판단 기준:

```text
사용자가 자주 돌아오는 화면
→ gcTime 길게 검토

데이터가 무겁고 재사용 적음
→ gcTime 짧게 검토

목록과 상세 왕복 많음
→ gcTime 기본값 또는 길게 검토

메모리 사용량 중요
→ gcTime 조정 검토
```

주의:

- gcTime은 fresh/stale 여부를 결정하지 않는다.
- fresh 여부는 staleTime이 결정한다.
- gcTime은 inactive cache 보관 기간과 관련된다.
- 무조건 길게 두면 메모리 사용량이 증가할 수 있다.

---

### [FAQ]

Q. gcTime은 뭐야?
A. 사용되지 않는 inactive Query Cache가 메모리에 유지되는 시간이다.

Q. staleTime과 gcTime은 뭐가 달라?
A. staleTime은 데이터 신선도 기준이고 gcTime은 inactive cache 보관 시간 기준이다.

Q. gcTime을 길게 하면 항상 좋아?
A. 아니다. cache 재사용에는 좋지만 메모리 사용량이 증가할 수 있다.

---

# 11. Pagination and Infinite Query

## 11.1 Pagination Query Rules

### [개념]

Pagination Query는 page, size, sort, filter 조건을 queryKey에 포함해 서버 페이지 데이터를 조회하는 방식이다.

페이지별 데이터는 서로 다른 Server State로 구분되어야 한다.

---

### [핵심]

Pagination Query 구성:

- page
- size
- sort
- filter
- queryKey params
- server page response
- totalCount
- hasNext
- keep previous data
- placeholderData

---

### [실무]

예:

```tsx
const { data, isLoading } = useQuery({
  queryKey: ["festivals", { keyword, region, page, size }],
  queryFn: () => getFestivals({ keyword, region, page, size }),
});
```

권장 기준:

- page, size, sort, filter를 queryKey에 포함한다.
- page는 URL State와 연결하는 경우가 많다.
- 검색 조건 변경 시 page를 1로 초기화한다.
- server response 구조를 통일한다.
- 이전 페이지 데이터 유지 정책을 검토한다.
- 페이지 데이터를 Zustand/Redux에 복사하지 않는다.

---

### [FAQ]

Q. page 번호도 queryKey에 넣어야 해?
A. 맞다. page가 다르면 서버 응답 데이터가 다르므로 queryKey에 포함해야 한다.

Q. 페이지네이션 상태는 Store에 둬야 해?
A. 공유와 새로고침 복원이 필요하면 URL State가 적합하고, 서버 데이터는 TanStack Query가 관리한다.

Q. 검색 조건이 바뀌면 page는 어떻게 해?
A. 보통 page를 1로 초기화한다.

---

## 11.2 Infinite Query Rules

### [개념]

Infinite Query는 무한 스크롤이나 더보기 UI처럼 여러 페이지 데이터를 누적 조회할 때 사용하는 방식이다.

useInfiniteQuery는 pageParam을 기반으로 다음 페이지를 조회한다.

---

### [핵심]

Infinite Query 구성:

- useInfiniteQuery
- initialPageParam
- getNextPageParam
- hasNextPage
- fetchNextPage
- isFetchingNextPage
- pages
- pageParam
- load more
- infinite scroll

---

### [실무]

사용 후보:

```text
notification list
review list
chat history
feed list
festival list load more
comment list
```

판단 기준:

```text
페이지 번호 UI가 필요함
→ useQuery pagination

더보기 / 무한 스크롤 필요
→ useInfiniteQuery

실시간 메시지 필요
→ WebSocket 또는 realtime strategy 함께 검토
```

주의:

- getNextPageParam 기준을 서버 응답과 맞춘다.
- 중복 fetch 방지를 고려한다.
- observer trigger가 과도하게 호출되지 않게 한다.
- 삭제/수정 mutation 후 pages cache 갱신 또는 invalidation을 고려한다.
- 무한 스크롤은 접근성과 UX를 함께 고려한다.

---

### [FAQ]

Q. useInfiniteQuery는 언제 써?
A. 무한 스크롤이나 더보기 버튼처럼 여러 페이지를 누적 조회할 때 사용한다.

Q. 일반 pagination과 infinite query는 뭐가 달라?
A. 일반 pagination은 현재 page 중심이고 infinite query는 여러 page 데이터를 누적해서 보여준다.

Q. 채팅 메시지는 useInfiniteQuery만 쓰면 돼?
A. 과거 메시지 조회에는 가능하지만 실시간 수신은 WebSocket 같은 realtime 전략이 필요할 수 있다.

---

# 12. Server State and Global Store Separation

## 12.1 TanStack Query with Zustand

### [개념]

TanStack Query와 Zustand는 함께 사용할 수 있지만 역할을 분리해야 한다.

TanStack Query는 Server State를 관리하고 Zustand는 Client Global State를 관리한다.

---

### [핵심]

역할 분리:

- TanStack Query → API Data
- TanStack Query → cache / refetch / invalidation
- Zustand → Auth Summary
- Zustand → UI Global State
- Zustand → User Preference
- Zustand → selected client option
- URL State → search / filter / page

---

### [실무]

역할 분리 예:

```text
Festival Search Page

URL State:
- keyword
- region
- page

TanStack Query:
- festival list
- loading
- error
- server pagination result

Zustand:
- global toast
- sidebarOpen
- authenticated
```

주의:

- Query data를 Zustand에 복사하지 않는다.
- Zustand Store 값을 queryKey 조건으로 사용할 수는 있다.
- mutation 성공 후 Zustand가 아니라 Query Cache를 invalidate한다.
- logout 시 Zustand reset과 Query Cache cleanup을 함께 고려한다.

---

### [FAQ]

Q. TanStack Query와 Zustand를 같이 써도 돼?
A. 가능하다. TanStack Query는 Server State, Zustand는 Client Global State를 담당하게 분리하면 된다.

Q. Query data를 Zustand에 복사해야 해?
A. 보통 필요 없다. Query Cache를 Server State의 Source of Truth로 두는 것이 좋다.

Q. Zustand 값으로 queryKey를 만들 수 있어?
A. 가능하다. 단 queryFn 조건과 queryKey가 일치해야 한다.

---

## 12.2 TanStack Query with Redux Toolkit

### [개념]

TanStack Query와 Redux Toolkit은 함께 사용할 수 있지만 역할을 분리해야 한다.

Redux Toolkit은 복잡한 Client Global State를 관리하고 TanStack Query는 API Server State를 관리한다.

---

### [핵심]

역할 분리:

- TanStack Query → Server State
- Redux Toolkit → Client Global State
- Redux Toolkit → complex UI/domain client state
- Redux Toolkit → Auth Summary
- TanStack Query → user profile detail
- URL State → query condition
- Selector → Client Derived Value

---

### [실무]

역할 분리 예:

```text
Redux Toolkit:
- auth summary
- global UI state
- complex cart client rule
- permission summary

TanStack Query:
- product list
- product detail
- order history
- user profile detail
- notification list

URL State:
- search keyword
- filter
- page
```

주의:

- API data를 Redux Slice에 중복 저장하지 않는다.
- mutation 후 Redux State가 아니라 Query Cache를 갱신한다.
- Redux selector와 Query data의 책임을 구분한다.
- RTK Query를 선택하는 경우 TanStack Query와 중복 도입을 검토한다.

---

### [FAQ]

Q. TanStack Query와 Redux Toolkit을 같이 써도 돼?
A. 가능하다. Redux Toolkit은 Client Global State, TanStack Query는 Server State를 담당하도록 분리하면 된다.

Q. API 데이터를 Redux Slice에도 저장해야 해?
A. 보통 필요 없다. Query Cache를 기준으로 두고 필요한 Client State만 Redux에 둔다.

Q. RTK Query와 TanStack Query를 동시에 써야 해?
A. 보통 둘 중 하나를 선택하는 것이 단순하다. 프로젝트 기준에 따라 Server State 도구를 통일하는 것이 좋다.

---

# 13. Auth and User-Specific Cache

## 13.1 User-Specific Query Cache

### [개념]

User-Specific Query Cache는 특정 로그인 사용자에게 종속된 Server State cache다.

로그아웃, 계정 전환, 토큰 만료 시 사용자별 cache cleanup이 필요할 수 있다.

---

### [핵심]

User-Specific Query 예:

- user profile
- notification list
- favorite list
- donation history
- private dashboard
- user settings
- my reviews
- my posts
- cart from server

---

### [실무]

logout cleanup Flow:

```text
Logout
→ authStore / authSlice reset
→ token cleanup
→ user-specific Query Cache clear 또는 remove
→ notificationStore reset
→ private route redirect
```

Query Cache cleanup 후보:

```text
queryClient.clear()
queryClient.removeQueries({ queryKey: ["notifications"] })
queryClient.removeQueries({ queryKey: ["favorites"] })
queryClient.invalidateQueries({ queryKey: ["user"] })
```

주의:

- 전체 clear는 간단하지만 public cache도 제거된다.
- removeQueries는 사용자별 queryKey를 명확히 알아야 한다.
- 계정 전환 시 이전 사용자 데이터가 보이면 안 된다.
- userId를 queryKey에 포함하면 cache 분리에 도움이 된다.

---

### [FAQ]

Q. logout 시 Query Cache도 지워야 해?
A. 사용자별 API 데이터가 포함되어 있으면 clear, remove, invalidate를 검토해야 한다.

Q. queryClient.clear를 쓰면 돼?
A. 가능하지만 public cache까지 모두 제거되므로 프로젝트 정책에 따라 선택해야 한다.

Q. userId를 queryKey에 넣는 게 좋아?
A. 사용자별 cache를 분리해야 하는 데이터라면 userId를 queryKey에 포함하는 것이 도움이 될 수 있다.

---

## 13.2 Auth Error and Query

### [개념]

Auth Error and Query는 API 조회 중 인증 오류가 발생했을 때 Auth Flow와 Query 상태를 연결하는 기준이다.

401, 403 같은 응답은 단순 Query Error가 아니라 인증/인가 흐름과 연결될 수 있다.

---

### [핵심]

인증 오류 상태:

- 401 Unauthorized
- 403 Forbidden
- token expired
- refresh failed
- session expired
- permission denied
- protected route redirect
- auth reset

---

### [실무]

Auth Error 처리 Flow:

```text
API 401 발생
→ refresh token 가능 여부 확인
→ refresh 성공 시 original request 재시도
→ refresh 실패 시 auth reset
→ user-specific Query Cache cleanup
→ login redirect
```

권장 기준:

- API Client interceptor에서 공통 처리할 수 있다.
- Query Error UI와 Auth Error Flow를 구분한다.
- 403은 권한 부족 UI 또는 접근 차단으로 처리한다.
- token expired는 refresh 흐름과 연결한다.
- refresh 실패 시 Store reset과 Query Cache cleanup을 함께 처리한다.

주의:

- 모든 error를 logout으로 처리하지 않는다.
- 401과 403을 구분한다.
- refresh 무한 루프를 방지한다.
- 인증 오류 메시지는 사용자 친화적으로 제공한다.

---

### [FAQ]

Q. Query에서 401 오류가 나면 어떻게 해?
A. refresh 가능 여부를 확인하고 실패하면 Auth State reset, Query Cache cleanup, login redirect를 처리한다.

Q. 401과 403은 같아?
A. 아니다. 401은 인증 문제이고 403은 인증은 되었지만 권한이 부족한 경우다.

Q. 모든 API Error를 Auth Error로 처리해도 돼?
A. 아니다. network error, validation error, server error, auth error를 구분해야 한다.

---

# 14. Query Data Transformation

## 14.1 select Option Rules

### [개념]

select option은 useQuery의 data를 Component에 전달하기 전에 변환하는 기능이다.

서버 응답 구조를 화면에 필요한 형태로 변환할 때 사용할 수 있다.

---

### [핵심]

select 사용 대상:

- response wrapper 제거
- list mapping
- field rename
- sorting basics
- filtering basics
- summary extraction
- view model conversion

---

### [실무]

예:

```tsx
const { data: festivals } = useQuery({
  queryKey: ["festivals"],
  queryFn: getFestivals,
  select: (response) => response.items,
});
```

권장 기준:

- 서버 응답 wrapper 제거에 사용할 수 있다.
- 화면에서 반복되는 mapping을 줄일 수 있다.
- 무거운 변환은 별도 mapper를 검토한다.
- 원본 cache와 select 결과의 차이를 이해한다.
- select에서 side effect를 수행하지 않는다.

주의:

- select는 Derived View Data를 만드는 용도다.
- select 결과를 다시 Store에 저장하지 않는다.
- 복잡한 domain mapping은 API layer 또는 mapper 함수로 분리한다.
- filter 조건이 서버 조회 조건이면 queryKey와 API parameter로 처리한다.

---

### [FAQ]

Q. useQuery select는 뭐야?
A. queryFn 결과를 Component가 사용하기 전에 변환하는 옵션이다.

Q. select에서 filtering을 해도 돼?
A. 화면 표시용 간단한 변환은 가능하지만 서버 조회 조건인 filter는 queryKey와 API parameter로 처리하는 것이 좋다.

Q. select 결과를 Store에 저장해야 해?
A. 보통 필요 없다. Query data 또는 select 결과를 그대로 사용하면 된다.

---

## 14.2 Mapping Function Rules

### [개념]

Mapping Function은 API 응답 데이터를 화면 또는 도메인 사용 형태로 변환하는 함수다.

Mapping 기준을 분리하면 Component와 API 응답 구조의 결합을 줄일 수 있다.

---

### [핵심]

Mapping 대상:

- API Response DTO
- View Model
- date format
- enum label
- image url
- rating summary
- status label
- normalized item
- display field

---

### [실무]

예:

```typescript
function toFestivalCard(dto: FestivalResponseDto): FestivalCardViewModel {
  return {
    festivalId: dto.festivalId,
    title: dto.title,
    imageUrl: dto.thumbnailUrl ?? "/default-festival.png",
    periodText: `${dto.startDate} ~ ${dto.endDate}`,
    regionLabel: dto.regionName,
  };
}
```

사용 예:

```tsx
const { data: festivalCards } = useQuery({
  queryKey: ["festivals", params],
  queryFn: () => getFestivals(params),
  select: (data) => data.items.map(toFestivalCard),
});
```

권장 기준:

- API DTO와 View Model을 구분한다.
- 반복되는 display 변환은 mapper로 분리한다.
- 날짜, enum, image fallback 변환 기준을 통일한다.
- mapping 함수는 순수 함수로 작성한다.
- mapping 결과를 별도 State에 중복 저장하지 않는다.

---

### [FAQ]

Q. API 응답 변환은 어디서 해?
A. 간단한 변환은 select에서 가능하고 반복되는 변환은 mapping function으로 분리하는 것이 좋다.

Q. View Model은 왜 필요해?
A. API 응답 구조와 화면 표시 구조를 분리해 Component 변경 비용을 줄이기 위해 필요하다.

Q. mapping 결과를 State로 저장해야 해?
A. 보통 필요 없다. Query data 기반 Derived Value로 사용하면 된다.

---

# 15. Query Anti Patterns

## 15.1 Query Data Copy to Store

### [개념]

Query Data Copy to Store는 TanStack Query로 조회한 서버 데이터를 다시 Zustand나 Redux Store에 복사하는 문제다.

이 방식은 Server State의 Source of Truth를 두 개로 만들어 데이터 불일치를 유발한다.

---

### [핵심]

문제:

- Query Cache와 Store 불일치
- mutation 후 한쪽만 갱신
- stale data 증가
- loading / error 중복 관리
- Store 비대화
- Source of Truth 붕괴
- 디버깅 어려움

---

### [실무]

나쁜 Flow:

```text
useQuery로 festivalList 조회
→ onSuccess에서 Zustand setFestivals
→ Component는 Zustand festivals 사용
→ mutation 후 Query Cache만 invalidate
→ Zustand festivals stale
```

좋은 Flow:

```text
useQuery로 festivalList 조회
→ Component는 query data 사용
→ mutation 후 관련 query invalidate
→ Query Cache가 Source of Truth
```

예외 후보:

```text
서버 데이터 중 일부를 Client Preference로 저장해야 함
서버 응답에서 인증 요약만 별도 Auth Store에 반영
WebSocket과 Query Cache를 통합하는 특수 구조
```

주의:

- 예외는 명확한 이유와 sync 전략이 있어야 한다.
- 기본은 Query Cache를 Source of Truth로 둔다.
- Store에는 UI State나 Auth Summary 같은 Client State만 둔다.

---

### [FAQ]

Q. useQuery data를 Zustand에 복사하면 안 돼?
A. 보통 권장하지 않는다. Query Cache와 Store가 서로 달라져 stale data 문제가 생길 수 있다.

Q. Query data를 Redux Store에 복사하면 안 돼?
A. 대부분 필요 없다. Server State는 Query Cache를 기준으로 관리하는 것이 좋다.

Q. Query data 일부를 Store에 넣는 예외가 있어?
A. 인증 요약처럼 Client Global State로 필요한 최소 정보만 명확한 sync 기준을 두고 반영할 수 있다.

---

## 15.2 Missing Query Key Parameter

### [개념]

Missing Query Key Parameter는 queryFn이 사용하는 조건을 queryKey에 포함하지 않아 cache가 잘못 재사용되는 문제다.

조회 조건이 다르면 queryKey도 달라져야 한다.

---

### [핵심]

누락하기 쉬운 값:

- id
- keyword
- filter
- sort
- page
- size
- date range
- userId
- role
- locale
- enabled condition

---

### [실무]

나쁜 예:

```tsx
useQuery({
  queryKey: ["festivals"],
  queryFn: () => getFestivals({ keyword, page }),
});
```

좋은 예:

```tsx
useQuery({
  queryKey: ["festivals", { keyword, page }],
  queryFn: () => getFestivals({ keyword, page }),
});
```

Debug Flow:

```text
검색 조건이 바뀌었는데 데이터가 그대로임
→ queryFn parameter 확인
→ queryKey parameter 확인
→ queryKey 누락 값 추가
```

주의:

- queryFn에서 사용하는 외부 변수는 queryKey에 포함한다.
- 객체 params는 안정적인 구조로 만든다.
- Query Key Factory를 사용하면 누락을 줄일 수 있다.

---

### [FAQ]

Q. queryKey에 parameter를 빼먹으면 어떻게 돼?
A. 다른 조건의 데이터를 같은 cache로 인식해 잘못된 데이터가 표시될 수 있다.

Q. queryFn에서 keyword를 쓰면 queryKey에도 keyword를 넣어야 해?
A. 맞다. queryFn 결과가 keyword에 따라 달라지면 queryKey에도 포함해야 한다.

Q. page 값도 queryKey에 넣어야 해?
A. 맞다. page가 다르면 서버 응답이 다르므로 반드시 포함해야 한다.

---

## 15.3 Over Invalidation and Under Invalidation

### [개념]

Over Invalidation은 너무 많은 Query를 무분별하게 invalidate하는 문제다.

Under Invalidation은 mutation 후 필요한 Query를 invalidate하지 않아 오래된 데이터가 남는 문제다.

---

### [핵심]

Over Invalidation 문제:

- 불필요한 refetch 증가
- API 요청 증가
- 성능 저하
- 사용자 경험 저하

Under Invalidation 문제:

- stale UI
- 수정 후 이전 데이터 표시
- count 불일치
- detail/list 불일치
- 사용자 신뢰도 저하

---

### [실무]

Invalidation 설계 Flow:

```text
Mutation 종류 확인
→ 변경된 서버 데이터 확인
→ 영향받는 Query 목록화
→ list/detail/summary 구분
→ 정확한 queryKey invalidate
```

예:

```text
리뷰 작성
→ reviews list invalidate
→ festival detail rating summary invalidate

좋아요 토글
→ festival detail invalidate
→ festival list summary invalidate 가능

알림 읽음 처리
→ notification list invalidate
→ unread count invalidate
```

주의:

- queryKey 계층 구조를 잘 설계한다.
- Query Key Factory로 invalidation 기준을 통일한다.
- 너무 넓은 invalidate는 피한다.
- stale UI가 남으면 under invalidation을 의심한다.

---

### [FAQ]

Q. Over Invalidation은 뭐야?
A. mutation 후 관련 없는 Query까지 과도하게 invalidate해서 불필요한 refetch가 늘어나는 문제다.

Q. Under Invalidation은 뭐야?
A. mutation 후 필요한 Query를 갱신하지 않아 오래된 데이터가 화면에 남는 문제다.

Q. Invalidation 기준은 어떻게 정해?
A. mutation으로 변경된 서버 데이터가 어떤 list, detail, summary query에 영향을 주는지 기준으로 정한다.

---

# 16. Query Debugging Rules

## 16.1 Query Debug Flow

### [개념]

Query Debugging은 Server State 조회, cache, queryKey, refetch, invalidation, mutation 흐름을 추적하는 과정이다.

TanStack Query 문제는 queryKey와 cache 상태 확인이 핵심이다.

---

### [핵심]

확인 대상:

- queryKey
- queryFn parameter
- query data
- loading state
- error state
- stale status
- cache status
- invalidation target
- mutation lifecycle
- enabled condition
- URL State sync

---

### [실무]

Debug Flow:

```text
UI 데이터 문제 발생
→ Network 응답 확인
→ queryKey 확인
→ queryFn parameter 확인
→ Query Cache data 확인
→ URL State와 queryKey sync 확인
→ staleTime 확인
→ invalidation 여부 확인
→ Store 중복 저장 여부 확인
```

문제별 점검:

```text
검색 조건 바뀌어도 데이터 그대로
→ queryKey parameter 누락 확인

mutation 후 데이터 그대로
→ invalidateQueries 누락 확인

로그아웃 후 이전 사용자 데이터 표시
→ user-specific Query Cache cleanup 확인

loading이 이상함
→ enabled 조건, initialData, placeholderData 확인
```

---

### [FAQ]

Q. TanStack Query 문제는 어디부터 확인해?
A. queryKey, queryFn parameter, Network 응답, Query Cache, invalidation 여부를 먼저 확인한다.

Q. 검색 조건이 바뀌어도 데이터가 안 바뀌면?
A. queryKey에 검색 조건이 포함되어 있는지 확인한다.

Q. mutation 후 화면이 안 바뀌면?
A. 관련 queryKey를 invalidate했는지 또는 cache update가 올바른지 확인한다.

---

## 16.2 Query Devtools

### [개념]

TanStack Query Devtools는 Query Cache, queryKey, status, stale 상태, refetch 상태를 확인할 수 있는 개발 도구다.

Server State 디버깅에 유용하다.

---

### [핵심]

Devtools 확인 대상:

- queryKey list
- query status
- cached data
- stale / fresh
- inactive query
- refetch trigger
- observers
- last updated
- error state

---

### [실무]

활용 상황:

```text
queryKey가 예상대로 생성되는지 확인
cache data가 최신인지 확인
mutation 후 invalidation이 되었는지 확인
inactive cache가 남아 있는지 확인
staleTime 동작 확인
```

주의:

- Devtools는 개발 환경에서 사용한다.
- 운영 환경 노출 여부는 설정으로 관리한다.
- Devtools 결과와 Network 탭을 함께 확인한다.
- Query data를 Store에 복사하면 Devtools와 화면 데이터가 다를 수 있다.

---

### [FAQ]

Q. TanStack Query Devtools는 왜 써?
A. Query Cache, queryKey, stale 상태, refetch 여부를 직접 확인하기 위해 사용한다.

Q. Devtools에서 queryKey를 확인해야 하는 이유는?
A. queryKey가 잘못되면 cache 재사용과 invalidation이 잘못 동작할 수 있기 때문이다.

Q. Devtools만 보면 충분해?
A. 아니다. Network 응답, Component props, URL State, Store 중복 저장 여부도 함께 확인해야 한다.

---

# 17. Server State Checklist

## 17.1 TanStack Query Checklist

### [개념]

TanStack Query Checklist는 Server State 조회와 갱신 구현 전에 검수해야 하는 기준이다.

Query 구현 전 State Type, queryKey, queryFn, loading/error/empty, invalidation 기준을 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] 이 데이터는 Server State인가?
- [ ] Query Cache가 Source of Truth인가?
- [ ] queryKey가 도메인과 parameter를 포함하는가?
- [ ] queryFn이 queryKey 조건과 일치하는가?
- [ ] API 함수가 분리되어 있는가?
- [ ] loading 상태를 처리하는가?
- [ ] error 상태를 처리하는가?
- [ ] empty 상태를 처리하는가?
- [ ] mutation 후 invalidation 기준이 있는가?
- [ ] Server State를 Store에 중복 저장하지 않는가?
- [ ] URL State와 queryKey가 동기화되는가?
- [ ] staleTime 기준이 적절한가?
- [ ] user-specific cache cleanup 기준이 있는가?
```

---

### [실무]

TanStack Query 구현 Flow:

```text
API Data 요구
→ Server State 확인
→ queryKey 설계
→ API queryFn 작성
→ useQuery 작성
→ Loading/Error/Empty UI 작성
→ Mutation 작성
→ Invalidation 기준 작성
→ Debug 기준 확인
```

결과 예:

```text
festivalList
→ Server State
→ queryKey ["festivals", params]
→ URL State params 연동
→ loading/error/empty 처리
→ create/update/delete 후 invalidate

reviewFormContent
→ Form Local State
→ TanStack Query 대상 아님

modalOpen
→ UI Client State
→ TanStack Query 대상 아님
```

---

### [FAQ]

Q. TanStack Query 도입 전에 무엇을 확인해야 해?
A. 해당 데이터가 Server State인지, queryKey와 queryFn 조건이 일치하는지, invalidation 기준이 있는지 확인해야 한다.

Q. TanStack Query Checklist에서 가장 중요한 것은 뭐야?
A. queryKey 설계와 Server State를 Store에 중복 저장하지 않는 것이다.

Q. Query 구현 후 반드시 확인할 것은 뭐야?
A. loading, error, empty 상태와 mutation 후 invalidation이 올바르게 동작하는지 확인해야 한다.

---

## 17.2 Server State Review Checklist

### [개념]

Server State Review Checklist는 코드 리뷰 시 API 데이터 관리 방식이 올바른지 검수하는 기준이다.

Server State가 Client Store에 섞이지 않았는지, queryKey가 누락되지 않았는지 확인한다.

---

### [핵심]

Review Checklist:

```md
- [ ] API 데이터가 Zustand / Redux에 중복 저장되지 않았는가?
- [ ] Query data가 Component에서 직접 사용되는가?
- [ ] queryKey에 id / filter / page가 포함되었는가?
- [ ] queryFn parameter와 queryKey가 일치하는가?
- [ ] mutation 후 관련 list/detail/summary가 갱신되는가?
- [ ] Query Cache cleanup이 logout 정책과 연결되는가?
- [ ] URL State와 Server State 책임이 분리되었는가?
- [ ] Derived View Data를 중복 State로 저장하지 않는가?
- [ ] Error State와 Auth Error가 구분되는가?
- [ ] Optimistic Update에 rollback 기준이 있는가?
```

---

### [실무]

Review Flow:

```text
Server Data 코드 확인
→ queryKey 확인
→ queryFn 확인
→ Store 중복 저장 확인
→ mutation invalidation 확인
→ loading/error/empty UI 확인
→ logout cleanup 확인
→ optimistic update rollback 확인
```

위험 신호:

```text
useQuery onSuccess에서 setStore 호출
queryKey가 ["list"]로만 되어 있음
page가 queryFn에만 있고 queryKey에는 없음
mutation 후 refetch 기준 없음
logout 후 Query Cache 유지
API data를 filteredData State로 중복 저장
```

---

### [FAQ]

Q. Server State 코드 리뷰에서 가장 먼저 볼 것은?
A. API 데이터가 Query Cache 기준으로 관리되는지, Store에 중복 저장되지 않았는지 확인한다.

Q. queryKey 리뷰에서 중요한 것은?
A. queryFn이 사용하는 id, filter, page, sort 같은 조건이 queryKey에 포함되었는지 확인하는 것이다.

Q. mutation 리뷰에서 중요한 것은?
A. 변경된 서버 데이터와 관련된 list, detail, summary query를 적절히 갱신하는지 확인하는 것이다.

---

# 18. Part04 Final Review

## 18.1 Part04 Scope Summary

### [개념]

Part04는 Server State와 TanStack Query의 사용 기준, queryKey 설계, useQuery, useMutation, invalidation, cache 관리, anti pattern을 다룬다.

이 문서는 API 데이터를 Global Store에 무분별하게 저장하지 않고 Query Cache 중심으로 관리하도록 지원한다.

---

### [핵심]

Part04 포함 범위:

- Server State Purpose
- Client State vs Server State
- TanStack Query Purpose
- QueryClient
- QueryClientProvider
- useQuery
- queryFn
- queryKey
- Query Key Factory
- URL State with queryKey
- Loading / Error / Empty State
- useMutation
- invalidateQueries
- Direct Cache Update
- Optimistic Update
- staleTime
- gcTime
- Pagination Query
- Infinite Query
- Query with Zustand
- Query with Redux Toolkit
- User-Specific Query Cache
- Auth Error and Query
- Query Data Transformation
- Query Anti Patterns
- Query Debugging
- Server State Checklist

---

### [실무]

Part04 이후 문서 연결:

```text
Part01 State Classification and Ownership
→ Part02 Context API and useReducer
→ Part03 Zustand and Redux Toolkit
→ Part04 TanStack Query and Server State
→ Part05 Form State and Auth State
→ Part06 State Debugging and Anti Patterns
```

Agent 사용 기준:

```text
User API Data Request
→ Part01로 Server State 여부 판단
→ Part04로 queryKey / useQuery / mutation / invalidation 설계
→ Global Store가 필요하면 Part03으로 이동
→ Form/Auth 세부 상태가 필요하면 Part05로 이동
→ 문제 분석이면 Part06으로 이동
```

---

### [FAQ]

Q. Part04의 핵심 목적은 뭐야?
A. API 데이터를 Server State로 분류하고 TanStack Query로 cache, refetch, mutation, invalidation을 관리하게 하는 것이다.

Q. Part04는 Global Store 문서야?
A. 아니다. Part04는 Server State와 TanStack Query 문서이며 Global Store는 Part03에서 다룬다.

Q. Part04 다음에는 무엇을 다뤄야 해?
A. Form State와 Auth State의 세부 흐름을 다루는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Server State가 뭐야?
A. 서버가 원본으로 소유하고 Frontend가 조회, 캐싱, 갱신, 동기화하는 데이터다.

Q. API 응답 데이터는 대부분 Server State야?
A. 맞다. 서버가 원본을 소유하고 Frontend는 이를 가져와 표시하거나 캐싱한다.

Q. Server State를 Global Store에 넣으면 안 돼?
A. 가능은 하지만 cache, stale data, refetch, invalidation을 직접 관리해야 하므로 TanStack Query 같은 도구가 더 적합한 경우가 많다.

Q. Client State와 Server State를 왜 구분해?
A. 소유자와 갱신 방식이 다르기 때문이다. Server State는 캐시와 서버 동기화가 중요하다.

Q. selectedFestivalId는 Server State야?
A. 보통 selectedFestivalId는 Client State이고, 해당 id로 조회한 festival detail은 Server State다.

Q. user profile은 Client State야 Server State야?
A. 서버에서 조회한 원본 프로필은 Server State이고, 로그인 여부나 사용자 요약은 Auth State로 분리할 수 있다.

Q. Server State를 Client State로 잘못 관리하면 어떤 문제가 생겨?
A. 오래된 데이터, 중복 저장, mutation 후 미갱신, loading/error 중복 관리 문제가 생긴다.

Q. API 데이터를 Store에 저장하면 무조건 틀려?
A. 무조건은 아니지만 캐시와 동기화가 필요하면 TanStack Query 같은 Server State 도구가 더 적합하다.

Q. Server State와 Client State를 같이 써도 돼?
A. 가능하다. 서버 데이터는 Query Cache에 두고 화면 선택값이나 UI 상태는 Client State로 분리한다.

Q. TanStack Query는 전역 상태관리야?
A. 일반 Client State 전역 관리 도구라기보다 Server State와 API 캐시 관리 도구에 가깝다.

Q. TanStack Query는 언제 써?
A. API 데이터 조회, 캐싱, refetch, mutation, stale data 관리가 필요할 때 사용한다.

Q. TanStack Query로 modal open 같은 UI State도 관리해?
A. 권장하지 않는다. modal open은 Client UI State이므로 useState나 Store가 적합하다.

Q. QueryClient는 뭐야?
A. TanStack Query의 cache, query, mutation 동작을 관리하는 핵심 객체다.

Q. QueryClientProvider는 왜 필요해?
A. App 하위에서 useQuery와 useMutation이 QueryClient와 Query Cache를 사용할 수 있게 하기 위해 필요하다.

Q. QueryClient를 Component 안에서 매번 생성해도 돼?
A. 권장하지 않는다. 매 렌더링마다 Cache가 초기화될 수 있으므로 안정적인 위치에서 생성해야 한다.

Q. useQuery는 뭐야?
A. 서버 데이터를 조회하고 cache, loading, error, refetch 상태를 관리하는 TanStack Query Hook이다.

Q. useQuery에는 무엇이 필요해?
A. 데이터를 식별하는 queryKey와 API 요청을 수행하는 queryFn이 필요하다.

Q. useQuery data를 Zustand에 다시 저장해야 해?
A. 보통 필요 없다. Query Cache가 Server State의 Source of Truth가 되도록 두는 것이 좋다.

Q. queryFn은 뭐야?
A. useQuery가 서버 데이터를 가져올 때 실행하는 API 요청 함수다.

Q. queryFn 안에서 setState를 해도 돼?
A. 권장하지 않는다. queryFn은 서버 데이터 조회에 집중하고 UI 상태 변경은 외부에서 처리하는 것이 좋다.

Q. queryKey 값과 queryFn 인자는 같아야 해?
A. queryKey가 cache 식별 기준이므로 queryFn이 사용하는 조건과 일치해야 한다.

Q. queryKey는 왜 중요해?
A. 캐시에서 데이터를 식별하고 refetch와 invalidation 대상을 결정하기 때문이다.

Q. queryKey에 id를 넣어야 해?
A. 상세 조회처럼 id별 데이터가 다르면 반드시 id를 포함해야 한다.

Q. 검색 조건도 queryKey에 넣어야 해?
A. 맞다. keyword, filter, page 같은 조회 조건이 다르면 서로 다른 cache로 구분해야 한다.

Q. Query Key Factory는 왜 필요해?
A. queryKey 구조를 일관되게 관리해 오타와 invalidation 오류를 줄이기 위해 필요하다.

Q. 모든 queryKey에 Factory가 필요해?
A. 작은 프로젝트에서는 필수는 아니지만 query가 많아지면 Factory가 유지보수에 유리하다.

Q. queryKey 문자열을 직접 여러 곳에 쓰면 안 돼?
A. 가능하지만 오타와 구조 불일치가 생기기 쉬워 Factory 사용을 검토하는 것이 좋다.

Q. 검색 조건은 queryKey에 넣어야 해?
A. 맞다. 검색 조건이 다르면 다른 서버 데이터이므로 queryKey에 포함해야 한다.

Q. 검색 조건은 Store에 넣어야 해 URL에 넣어야 해?
A. 공유와 새로고침 복원이 필요하면 URL State가 적합하고, 그 값을 queryKey에 반영하는 것이 좋다.

Q. URL State와 TanStack Query를 같이 써도 돼?
A. 가능하다. URL State는 조회 조건을 관리하고 TanStack Query는 해당 조건의 Server State를 관리한다.

Q. 검색 input 값을 입력할 때마다 서버 조회해야 해?
A. 필수는 아니다. 입력 중 값은 Local State로 두고 submit 후 URL State를 변경해 조회할 수 있다.

Q. Form Draft State와 URL State를 왜 나눠?
A. 입력 중 임시값과 실제 검색 결과를 결정하는 조건이 다르기 때문이다.

Q. 검색 submit 후 page는 어떻게 해?
A. 검색 조건이 바뀌면 보통 page를 1로 초기화한다.

Q. TanStack Query loading 상태는 Store에 저장해야 해?
A. 보통 필요 없다. useQuery가 제공하는 loading 상태를 사용하면 된다.

Q. isLoading과 isFetching은 뭐가 달라?
A. isLoading은 초기 조회 상태에 가깝고, isFetching은 background refetch까지 포함하는 조회 중 상태로 볼 수 있다.

Q. 목록 조회 중에는 어떤 UI가 좋아?
A. 목록 Skeleton, 작은 loading indicator, 기존 데이터 유지 정책을 상황에 맞게 선택한다.

Q. Query error도 Store에 저장해야 해?
A. 보통 필요 없다. useQuery와 useMutation이 제공하는 error 상태를 사용하고 필요 시 UI에서 메시지로 변환한다.

Q. 서버 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자용 메시지와 내부 로그용 메시지를 구분하는 것이 좋다.

Q. 인증 오류가 나면 어떻게 해?
A. Auth Flow와 연결해 refresh, logout, login redirect 기준을 적용한다.

Q. Empty State는 Error State야?
A. 아니다. 요청은 성공했지만 표시할 데이터가 없는 정상 상태다.

Q. 검색 결과가 없을 때는 어떻게 표시해?
A. 검색 조건에 맞는 결과가 없다는 메시지와 필터 초기화 같은 다음 행동을 제공할 수 있다.

Q. Empty State도 loading 이후에 판단해야 해?
A. 맞다. loading과 error가 아닌 상태에서 data가 비어 있는지 판단해야 한다.

Q. useMutation은 언제 써?
A. 서버 데이터를 생성, 수정, 삭제하거나 좋아요, 찜하기처럼 서버 상태를 변경할 때 사용한다.

Q. mutation 후 목록을 어떻게 갱신해?
A. 관련 queryKey를 invalidate해서 다시 조회하도록 처리할 수 있다.

Q. mutation loading 상태도 Store에 저장해야 해?
A. 보통 필요 없다. useMutation이 제공하는 isPending 같은 상태를 사용하면 된다.

Q. invalidateQueries는 왜 써?
A. mutation 이후 관련 cache를 stale로 만들어 최신 서버 데이터를 다시 가져오기 위해 사용한다.

Q. 어떤 queryKey를 invalidate해야 해?
A. mutation으로 변경된 서버 데이터를 사용하는 list, detail, summary queryKey를 확인해야 한다.

Q. 모든 query를 invalidate하면 안 돼?
A. 가능은 하지만 불필요한 refetch가 많아질 수 있으므로 관련 query만 지정하는 것이 좋다.

Q. mutation 후 refetch 대신 cache를 직접 바꿔도 돼?
A. 가능하다. 서버 응답에 최신 데이터가 있고 cache 구조가 명확하면 setQueryData를 사용할 수 있다.

Q. direct cache update와 invalidation 중 뭐가 좋아?
A. 단순하고 즉시 반영이 필요하면 direct update가 가능하고, 복잡한 연관 데이터는 invalidation이 더 안전하다.

Q. setQueryData를 쓸 때 주의할 점은?
A. 관련 list/detail cache 불일치가 생기지 않도록 cache 구조를 정확히 확인해야 한다.

Q. Optimistic Update는 언제 써?
A. 좋아요, 찜하기처럼 성공 가능성이 높고 빠른 UI 피드백이 중요한 작업에 사용할 수 있다.

Q. Optimistic Update가 항상 좋은가?
A. 아니다. 실패 가능성이 높거나 데이터 정합성이 중요한 작업에는 신중해야 한다.

Q. Optimistic Update에서 가장 중요한 것은 뭐야?
A. 실패 시 이전 상태로 되돌리는 rollback 기준이다.

Q. 결제도 Optimistic Update로 처리해도 돼?
A. 권장하지 않는다. 결제는 서버 검증과 정합성이 중요하므로 서버 응답 후 상태를 반영해야 한다.

Q. Optimistic Update 실패 시 어떻게 해?
A. 이전 cache snapshot으로 rollback하고 사용자에게 실패 메시지를 제공해야 한다.

Q. 복잡한 목록 업데이트에도 Optimistic Update를 써도 돼?
A. 가능은 하지만 cache 수정과 rollback이 복잡하면 invalidateQueries가 더 안전하다.

Q. staleTime은 뭐야?
A. Query Data를 fresh 상태로 간주하는 시간이다.

Q. staleTime을 길게 주면 뭐가 좋아?
A. 불필요한 refetch를 줄일 수 있지만 오래된 데이터가 보일 수 있다.

Q. 자주 바뀌는 데이터는 staleTime을 어떻게 해?
A. 짧게 설정하거나 mutation invalidation, polling, realtime 전략을 검토한다.

Q. gcTime은 뭐야?
A. 사용되지 않는 inactive Query Cache가 메모리에 유지되는 시간이다.

Q. staleTime과 gcTime은 뭐가 달라?
A. staleTime은 데이터 신선도 기준이고 gcTime은 inactive cache 보관 시간 기준이다.

Q. gcTime을 길게 하면 항상 좋아?
A. 아니다. cache 재사용에는 좋지만 메모리 사용량이 증가할 수 있다.

Q. page 번호도 queryKey에 넣어야 해?
A. 맞다. page가 다르면 서버 응답 데이터가 다르므로 queryKey에 포함해야 한다.

Q. 페이지네이션 상태는 Store에 둬야 해?
A. 공유와 새로고침 복원이 필요하면 URL State가 적합하고, 서버 데이터는 TanStack Query가 관리한다.

Q. 검색 조건이 바뀌면 page는 어떻게 해?
A. 보통 page를 1로 초기화한다.

Q. useInfiniteQuery는 언제 써?
A. 무한 스크롤이나 더보기 버튼처럼 여러 페이지를 누적 조회할 때 사용한다.

Q. 일반 pagination과 infinite query는 뭐가 달라?
A. 일반 pagination은 현재 page 중심이고 infinite query는 여러 page 데이터를 누적해서 보여준다.

Q. 채팅 메시지는 useInfiniteQuery만 쓰면 돼?
A. 과거 메시지 조회에는 가능하지만 실시간 수신은 WebSocket 같은 realtime 전략이 필요할 수 있다.

Q. TanStack Query와 Zustand를 같이 써도 돼?
A. 가능하다. TanStack Query는 Server State, Zustand는 Client Global State를 담당하게 분리하면 된다.

Q. Query data를 Zustand에 복사해야 해?
A. 보통 필요 없다. Query Cache를 Server State의 Source of Truth로 두는 것이 좋다.

Q. Zustand 값으로 queryKey를 만들 수 있어?
A. 가능하다. 단 queryFn 조건과 queryKey가 일치해야 한다.

Q. TanStack Query와 Redux Toolkit을 같이 써도 돼?
A. 가능하다. Redux Toolkit은 Client Global State, TanStack Query는 Server State를 담당하도록 분리하면 된다.

Q. API 데이터를 Redux Slice에도 저장해야 해?
A. 보통 필요 없다. Query Cache를 기준으로 두고 필요한 Client State만 Redux에 둔다.

Q. RTK Query와 TanStack Query를 동시에 써야 해?
A. 보통 둘 중 하나를 선택하는 것이 단순하다. 프로젝트 기준에 따라 Server State 도구를 통일하는 것이 좋다.

Q. logout 시 Query Cache도 지워야 해?
A. 사용자별 API 데이터가 포함되어 있으면 clear, remove, invalidate를 검토해야 한다.

Q. queryClient.clear를 쓰면 돼?
A. 가능하지만 public cache까지 모두 제거되므로 프로젝트 정책에 따라 선택해야 한다.

Q. userId를 queryKey에 넣는 게 좋아?
A. 사용자별 cache를 분리해야 하는 데이터라면 userId를 queryKey에 포함하는 것이 도움이 될 수 있다.

Q. Query에서 401 오류가 나면 어떻게 해?
A. refresh 가능 여부를 확인하고 실패하면 Auth State reset, Query Cache cleanup, login redirect를 처리한다.

Q. 401과 403은 같아?
A. 아니다. 401은 인증 문제이고 403은 인증은 되었지만 권한이 부족한 경우다.

Q. 모든 API Error를 Auth Error로 처리해도 돼?
A. 아니다. network error, validation error, server error, auth error를 구분해야 한다.

Q. useQuery select는 뭐야?
A. queryFn 결과를 Component가 사용하기 전에 변환하는 옵션이다.

Q. select에서 filtering을 해도 돼?
A. 화면 표시용 간단한 변환은 가능하지만 서버 조회 조건인 filter는 queryKey와 API parameter로 처리하는 것이 좋다.

Q. select 결과를 Store에 저장해야 해?
A. 보통 필요 없다. Query data 또는 select 결과를 그대로 사용하면 된다.

Q. API 응답 변환은 어디서 해?
A. 간단한 변환은 select에서 가능하고 반복되는 변환은 mapping function으로 분리하는 것이 좋다.

Q. View Model은 왜 필요해?
A. API 응답 구조와 화면 표시 구조를 분리해 Component 변경 비용을 줄이기 위해 필요하다.

Q. mapping 결과를 State로 저장해야 해?
A. 보통 필요 없다. Query data 기반 Derived Value로 사용하면 된다.

Q. useQuery data를 Zustand에 복사하면 안 돼?
A. 보통 권장하지 않는다. Query Cache와 Store가 서로 달라져 stale data 문제가 생길 수 있다.

Q. Query data를 Redux Store에 복사하면 안 돼?
A. 대부분 필요 없다. Server State는 Query Cache를 기준으로 관리하는 것이 좋다.

Q. Query data 일부를 Store에 넣는 예외가 있어?
A. 인증 요약처럼 Client Global State로 필요한 최소 정보만 명확한 sync 기준을 두고 반영할 수 있다.

Q. queryKey에 parameter를 빼먹으면 어떻게 돼?
A. 다른 조건의 데이터를 같은 cache로 인식해 잘못된 데이터가 표시될 수 있다.

Q. queryFn에서 keyword를 쓰면 queryKey에도 keyword를 넣어야 해?
A. 맞다. queryFn 결과가 keyword에 따라 달라지면 queryKey에도 포함해야 한다.

Q. page 값도 queryKey에 넣어야 해?
A. 맞다. page가 다르면 서버 응답이 다르므로 반드시 포함해야 한다.

Q. Over Invalidation은 뭐야?
A. mutation 후 관련 없는 Query까지 과도하게 invalidate해서 불필요한 refetch가 늘어나는 문제다.

Q. Under Invalidation은 뭐야?
A. mutation 후 필요한 Query를 갱신하지 않아 오래된 데이터가 화면에 남는 문제다.

Q. Invalidation 기준은 어떻게 정해?
A. mutation으로 변경된 서버 데이터가 어떤 list, detail, summary query에 영향을 주는지 기준으로 정한다.

Q. TanStack Query 문제는 어디부터 확인해?
A. queryKey, queryFn parameter, Network 응답, Query Cache, invalidation 여부를 먼저 확인한다.

Q. 검색 조건이 바뀌어도 데이터가 안 바뀌면?
A. queryKey에 검색 조건이 포함되어 있는지 확인한다.

Q. mutation 후 화면이 안 바뀌면?
A. 관련 queryKey를 invalidate했는지 또는 cache update가 올바른지 확인한다.

Q. TanStack Query Devtools는 왜 써?
A. Query Cache, queryKey, stale 상태, refetch 여부를 직접 확인하기 위해 사용한다.

Q. Devtools에서 queryKey를 확인해야 하는 이유는?
A. queryKey가 잘못되면 cache 재사용과 invalidation이 잘못 동작할 수 있기 때문이다.

Q. Devtools만 보면 충분해?
A. 아니다. Network 응답, Component props, URL State, Store 중복 저장 여부도 함께 확인해야 한다.

Q. TanStack Query 도입 전에 무엇을 확인해야 해?
A. 해당 데이터가 Server State인지, queryKey와 queryFn 조건이 일치하는지, invalidation 기준이 있는지 확인해야 한다.

Q. TanStack Query Checklist에서 가장 중요한 것은 뭐야?
A. queryKey 설계와 Server State를 Store에 중복 저장하지 않는 것이다.

Q. Query 구현 후 반드시 확인할 것은 뭐야?
A. loading, error, empty 상태와 mutation 후 invalidation이 올바르게 동작하는지 확인해야 한다.

Q. Server State 코드 리뷰에서 가장 먼저 볼 것은?
A. API 데이터가 Query Cache 기준으로 관리되는지, Store에 중복 저장되지 않았는지 확인한다.

Q. queryKey 리뷰에서 중요한 것은?
A. queryFn이 사용하는 id, filter, page, sort 같은 조건이 queryKey에 포함되었는지 확인하는 것이다.

Q. mutation 리뷰에서 중요한 것은?
A. 변경된 서버 데이터와 관련된 list, detail, summary query를 적절히 갱신하는지 확인하는 것이다.

Q. Part04의 핵심 목적은 뭐야?
A. API 데이터를 Server State로 분류하고 TanStack Query로 cache, refetch, mutation, invalidation을 관리하게 하는 것이다.

Q. Part04는 Global Store 문서야?
A. 아니다. Part04는 Server State와 TanStack Query 문서이며 Global Store는 Part03에서 다룬다.

Q. Part04 다음에는 무엇을 다뤄야 해?
A. Form State와 Auth State의 세부 흐름을 다루는 것이 좋다.
