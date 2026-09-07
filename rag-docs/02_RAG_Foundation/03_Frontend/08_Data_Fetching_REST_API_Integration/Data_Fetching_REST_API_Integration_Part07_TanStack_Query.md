# Data Fetching & REST API Integration Part07 - TanStack Query

---

# 1. TanStack Query Overview

## 1.1 TanStack Query 기본 개념

### [개념]

TanStack Query는 Server State를 조회, 캐싱, 동기화, 재조회, 변경 처리하기 위한 라이브러리다.

Frontend Agent는 API 데이터가 많고 Loading / Error / Cache / Refetch / Mutation / Pagination 관리가 복잡해질 때 TanStack Query 사용을 검토해야 한다.

TanStack Query는 Client State 관리 도구가 아니라 Server State 관리 도구다.

기본 Flow:

```text
Component Render
→ useQuery
→ queryKey 확인
→ queryFn 실행
→ API Function 호출
→ Query Cache 저장
→ UI State 반환
```

---

### [핵심]

TanStack Query 핵심 키워드:

- TanStack Query
- Server State
- Query Cache
- useQuery
- useMutation
- queryKey
- queryFn
- mutationFn
- invalidateQueries
- refetch
- staleTime
- gcTime
- isLoading
- isFetching
- isPending
- isError
- isSuccess
- QueryClient
- QueryClientProvider

TanStack Query 목적:

- API 데이터 캐싱
- Loading / Error 상태 관리
- Refetch 관리
- Mutation 상태 관리
- Mutation 성공 후 목록 갱신
- Pagination / Infinite Scroll 관리
- Server State와 Client State 분리
- 중복 요청 감소
- 동일 데이터 재사용

---

### [실무]

2026 실무 기준에서 TanStack Query는 API 데이터가 많고 여러 화면에서 동일 서버 데이터를 사용하는 React 프로젝트에 적합하다.

적합한 상황:

- 같은 API 데이터를 여러 Component에서 사용
- 목록 / 상세 데이터 캐싱 필요
- 검색 조건별 데이터 캐싱 필요
- mutation 후 자동 재조회 필요
- refetch / stale data 관리 필요
- pagination / infinite scroll 관리 필요
- Loading / Error 상태를 일관되게 처리하고 싶음

기본 구조:

```text
API Function
→ Query Hook
→ Component
→ Query Cache
→ UI Render
```

API Function:

```typescript
export async function getFestivals(params: FestivalSearchParams) {
  const response = await publicApi.get<
    ApiResponse<PageResponse<FestivalSummaryResponse>>
  >("/festivals", {
    params,
  });

  return response.data.data;
}
```

Query Hook:

```typescript
export function useFestivalQuery(params: FestivalSearchParams) {
  return useQuery({
    queryKey: ["festivals", params],
    queryFn: () => getFestivals(params),
  });
}
```

---

### [FAQ]

Q. TanStack Query는 뭐야?
A. API로 가져온 Server State를 조회, 캐싱, 재조회, 변경 처리하기 위한 라이브러리다.

Q. TanStack Query는 전역 상태관리 도구야?
A. 일반 Client State 전역 관리 도구라기보다 Server State와 API Cache 관리 도구다.

Q. TanStack Query는 언제 써?
A. API 데이터 캐싱, refetch, mutation, stale data 관리가 필요할 때 사용한다.

Q. TanStack Query를 쓰면 API Layer가 필요 없어?
A. 아니다. queryFn과 mutationFn에서 재사용할 API Function이 필요하다.

---

# 2. Server State vs Client State

## 2.1 Server State와 Client State 구분

### [개념]

Server State는 Backend에서 소유하고 Frontend가 API로 가져오는 데이터다.

Client State는 Frontend 내부에서만 관리하는 UI 상태다.

TanStack Query는 Server State 관리에 적합하고, modal open, input value, tab state 같은 Client State는 React State나 전역 상태 관리 도구로 관리한다.

---

### [핵심]

Server State 예:

- festival list
- festival detail
- review list
- notification list
- user profile
- favorite list
- search result
- page response
- slice response

Client State 예:

- modal open
- selected tab
- input value
- form state
- dropdown open
- local filter draft
- temporary UI state
- theme
- sidebar open

구분 기준:

```text
Backend가 원본 소유 → Server State
Frontend UI가 원본 소유 → Client State
```

주의:

- Server State를 Redux / Zustand 등에 중복 저장하지 않음
- API Cache와 UI State를 구분
- Form 입력 중인 값은 Client State
- Submit 후 서버에 저장된 값은 Server State
- 검색 조건 자체는 Client State일 수 있고 검색 결과는 Server State

---

### [실무]

Server State:

```typescript
const { data, isLoading } = useQuery({
  queryKey: ["festival", festivalId],
  queryFn: () => getFestivalDetail(festivalId),
});
```

Client State:

```typescript
const [isModalOpen, setModalOpen] = useState(false);
const [keyword, setKeyword] = useState("");
```

검색 흐름:

```text
keyword input value → Client State
submitted params → Query Key
search result page data → Server State
```

주의:

- input 입력마다 즉시 queryKey를 바꿀지 submit 후 바꿀지 UX 기준 필요
- modal 상태를 TanStack Query에 넣지 않음
- API 응답 데이터를 로컬 state에 복사할 때 동기화 문제 주의
- 서버 데이터 변경 후 invalidate로 최신화

---

### [FAQ]

Q. Server State는 뭐야?
A. Backend가 원본을 소유하고 Frontend가 API로 가져오는 데이터다.

Q. Client State는 뭐야?
A. modal open, input value, tab state처럼 Frontend UI 내부에서 관리하는 상태다.

Q. API 데이터를 Redux에 넣어도 돼?
A. 가능은 하지만 TanStack Query를 사용한다면 API Cache와 중복 저장되어 동기화 비용이 커질 수 있다.

Q. 검색어 input은 Server State야?
A. 아니다. 입력 중인 검색어는 Client State이고 검색 결과는 Server State다.

---

# 3. QueryClient Setup Rules

## 3.1 QueryClient 기본 설정

### [개념]

QueryClient는 TanStack Query의 Cache와 기본 동작을 관리하는 객체다.

React App에서 TanStack Query를 사용하려면 QueryClient를 생성하고 QueryClientProvider로 App을 감싸야 한다.

---

### [핵심]

필수 요소:

- QueryClient
- QueryClientProvider
- defaultOptions
- queries
- mutations
- staleTime
- gcTime
- retry
- refetchOnWindowFocus

설정 기준:

- 프로젝트 기본 staleTime 설정 가능
- retry 정책 설정 가능
- 개발 중 React Query Devtools 사용 가능
- QueryClient는 App 전체에서 하나 사용
- Component 내부에서 매번 QueryClient 생성 금지

---

### [실무]

기본 설정:

```tsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router />
    </QueryClientProvider>
  );
}
```

기본 옵션 설정:

```tsx
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60,
      retry: 1,
      refetchOnWindowFocus: false,
    },
    mutations: {
      retry: 0,
    },
  },
});
```

주의:

- `queryClient`를 Component 함수 안에서 생성하면 렌더링마다 새로 만들어질 수 있음
- retry가 너무 많으면 서버 오류 상황에서 요청이 반복될 수 있음
- staleTime은 데이터 특성에 따라 조정
- 인증 상태 변경 시 관련 query cache clear 필요 가능

---

### [FAQ]

Q. QueryClient는 왜 필요해?
A. TanStack Query의 Query Cache와 기본 옵션을 관리하기 위해 필요하다.

Q. QueryClientProvider는 어디에 둬?
A. 보통 App 최상단에서 Router나 주요 Component를 감싸도록 둔다.

Q. QueryClient를 Component 안에서 만들어도 돼?
A. 권장하지 않는다. 렌더링마다 새 QueryClient가 생성될 수 있어 Cache가 유지되지 않을 수 있다.

Q. retry는 기본값 그대로 써도 돼?
A. 가능하지만 401, 403, validation error 같은 요청은 무의미한 재시도가 될 수 있어 프로젝트 기준 설정이 필요하다.

---

# 4. useQuery Rules

## 4.1 useQuery 기본

### [개념]

`useQuery`는 서버 데이터를 조회하는 Hook이다.

GET 요청 기반의 목록 조회, 상세 조회, 필터 조회, 내 정보 조회에 사용한다.

---

### [핵심]

useQuery 구성 요소:

- queryKey
- queryFn
- enabled
- staleTime
- select
- placeholderData
- initialData
- refetch

useQuery 반환 상태:

- data
- error
- isLoading
- isFetching
- isError
- isSuccess
- refetch

주의:

- queryFn은 Promise를 반환해야 함
- queryFn 안에서 API Function 호출
- queryKey에 데이터 식별 기준 포함
- queryKey에 params / id 포함
- enabled로 조건부 조회 제어
- queryFn이 undefined를 반환하지 않도록 주의

---

### [실무]

목록 조회:

```tsx
export function useFestivalQuery(params: FestivalSearchParams) {
  return useQuery({
    queryKey: ["festivals", params],
    queryFn: () => getFestivals(params),
  });
}
```

상세 조회:

```tsx
export function useFestivalDetailQuery(festivalId: number) {
  return useQuery({
    queryKey: ["festival", festivalId],
    queryFn: () => getFestivalDetail(festivalId),
    enabled: Boolean(festivalId),
  });
}
```

Component 사용:

```tsx
function FestivalListPage() {
  const { data, error, isLoading, isFetching, refetch } = useFestivalQuery({
    page: 0,
    size: 20,
  });

  if (isLoading) {
    return <FestivalListSkeleton />;
  }

  if (error) {
    return (
      <ErrorState
        message={getApiErrorMessage(error)}
        onRetry={() => refetch()}
      />
    );
  }

  if (!data || data.content.length === 0) {
    return <EmptyState title="검색 결과가 없습니다." />;
  }

  return (
    <>
      {isFetching && <p>새로고침 중...</p>}
      <FestivalList festivals={data.content} />
    </>
  );
}
```

---

### [FAQ]

Q. useQuery는 언제 써?
A. 서버 데이터를 조회하는 GET API에 사용한다. 목록, 상세, 필터, 내 정보 조회에 적합하다.

Q. queryFn에는 뭘 넣어?
A. API Function을 호출하는 함수를 넣는다. 예: `() => getFestivals(params)`.

Q. useQuery의 data는 언제 undefined일 수 있어?
A. 최초 로딩 전이나 요청 실패 상황에서 undefined일 수 있으므로 방어 처리가 필요하다.

Q. enabled는 언제 써?
A. id나 token 같은 필수 조건이 준비된 뒤에만 조회해야 할 때 사용한다.

---

# 5. Query Key Rules

## 5.1 Query Key 설계 기준

### [개념]

Query Key는 TanStack Query가 Cache 데이터를 식별하는 기준이다.

같은 queryKey는 같은 데이터로 취급된다.

검색 조건, page, size, id가 달라지면 queryKey도 달라져야 한다.

---

### [핵심]

Query Key 포함 대상:

- resource name
- resource id
- params
- page
- size
- sort
- filter
- search keyword
- user scope
- locale

좋은 Query Key:

```text
["festivals", params]
["festival", festivalId]
["reviews", festivalId, params]
["notifications", params]
["myProfile"]
```

나쁜 Query Key:

```text
["data"]
["list"]
["festival"]
["reviews"]
```

주의:

- queryKey에 검색 조건 포함
- queryKey에 page / size 포함
- 상세 id 포함
- 민감정보를 queryKey에 넣지 않음
- invalidate 대상과 queryKey 구조 일치
- 객체 params 안정성 고려

---

### [실무]

목록 Query Key:

```tsx
useQuery({
  queryKey: ["festivals", params],
  queryFn: () => getFestivals(params),
});
```

상세 Query Key:

```tsx
useQuery({
  queryKey: ["festival", festivalId],
  queryFn: () => getFestivalDetail(festivalId),
});
```

리뷰 목록 Query Key:

```tsx
useQuery({
  queryKey: ["reviews", festivalId, params],
  queryFn: () => getReviews(festivalId, params),
});
```

Query Key 상수:

```typescript
export const festivalQueryKeys = {
  all: ["festivals"] as const,
  list: (params: FestivalSearchParams) => ["festivals", params] as const,
  detail: (festivalId: number) => ["festival", festivalId] as const,
};
```

주의:

- `params` 객체가 매 렌더마다 새로 생성되면 불필요한 query 변경이 발생할 수 있음
- form draft와 submitted params를 구분
- queryKey 설계는 invalidate 전략과 함께 설계
- list와 detail key를 명확히 구분

---

### [FAQ]

Q. queryKey는 왜 중요해?
A. TanStack Query가 어떤 Cache 데이터를 재사용하고 무효화할지 판단하는 기준이기 때문이다.

Q. queryKey에 params를 넣어야 해?
A. 검색 조건이나 페이지 번호가 바뀌면 다른 데이터이므로 queryKey에 포함해야 한다.

Q. queryKey가 틀리면 어떤 문제가 생겨?
A. 캐시가 중복되거나 invalidate가 제대로 되지 않아 화면 데이터가 갱신되지 않을 수 있다.

Q. queryKey에 token을 넣어도 돼?
A. 권장하지 않는다. 민감정보를 queryKey에 넣지 않는 것이 좋다.

---

# 6. Query Function Rules

## 6.1 queryFn 작성 기준

### [개념]

queryFn은 useQuery가 데이터를 가져오기 위해 실행하는 함수다.

queryFn은 API Function을 호출하고 Promise를 반환해야 한다.

---

### [핵심]

queryFn 기준:

- Promise 반환
- API Function 호출
- URL 직접 하드코딩 금지 권장
- queryKey와 인자 일치
- undefined 반환 금지
- Error를 삼키지 않음
- enabled로 조건부 실행 제어

주의:

- queryFn에서 setState 남발 금지
- queryFn에서 Component UI 처리 금지
- queryFn에서 alert 남발 금지
- queryFn이 실패하면 error 상태로 전달되게 함
- queryKey에 포함된 조건과 실제 요청 조건 일치

---

### [실무]

좋은 예:

```tsx
useQuery({
  queryKey: ["festival", festivalId],
  queryFn: () => getFestivalDetail(festivalId),
  enabled: Boolean(festivalId),
});
```

나쁜 예:

```tsx
useQuery({
  queryKey: ["festival"],
  queryFn: async () => {
    const response = await publicApi.get(`/festivals/${festivalId}`);
    setFestival(response.data);
  },
});
```

queryKey와 queryFn 인자 일치:

```tsx
useQuery({
  queryKey: ["festivals", params],
  queryFn: () => getFestivals(params),
});
```

조건부 실행:

```tsx
useQuery({
  queryKey: ["festival", festivalId],
  queryFn: () => getFestivalDetail(festivalId),
  enabled: festivalId !== null,
});
```

---

### [FAQ]

Q. queryFn 안에서 axios를 직접 써도 돼?
A. 가능하지만 API Layer 분리 원칙상 API Function을 호출하는 방식이 좋다.

Q. queryFn에서 setState를 해도 돼?
A. 권장하지 않는다. queryFn은 데이터를 반환하고 UI 상태는 useQuery 반환값으로 처리하는 것이 좋다.

Q. queryFn이 undefined를 반환하면 안 돼?
A. 안 된다. queryFn은 정상 데이터나 Promise reject를 반환해야 한다.

Q. queryFn의 인자와 queryKey가 달라도 돼?
A. 달라지면 Cache와 실제 요청 데이터가 불일치할 수 있으므로 맞춰야 한다.

---

# 7. Query State Rules

## 7.1 useQuery 상태 처리 기준

### [개념]

useQuery는 API 조회 상태를 나타내는 여러 상태 값을 제공한다.

Frontend Agent는 `isLoading`, `isFetching`, `isError`, `isSuccess`, `data`, `error`를 UI State에 연결해야 한다.

---

### [핵심]

주요 상태:

- `isLoading`: 최초 로딩
- `isFetching`: fetching 진행 중
- `isError`: 오류 발생
- `isSuccess`: 성공
- `data`: 응답 데이터
- `error`: 오류 객체
- `refetch`: 수동 재조회 함수

상태 연결:

```text
isLoading → Initial Loading UI
isFetching → Refetch Indicator
isError → Error State
data empty → Empty State
data exists → Success State
```

주의:

- `isLoading`과 `isFetching` 혼동 금지
- `data` undefined 방어 처리
- Error 객체 직접 노출 금지
- Empty State는 성공 후 data 내용 기준
- Refetch 중 기존 data 유지 가능

---

### [실무]

기본 UI State:

```tsx
const { data, error, isLoading, isFetching, isError, refetch } =
  useFestivalQuery(params);

if (isLoading) {
  return <FestivalListSkeleton />;
}

if (isError) {
  return (
    <ErrorState message={getApiErrorMessage(error)} onRetry={() => refetch()} />
  );
}

if (!data || data.content.length === 0) {
  return <EmptyState title="검색 결과가 없습니다." />;
}

return (
  <>
    {isFetching && <p>새로고침 중...</p>}
    <FestivalList festivals={data.content} />
  </>
);
```

상태 Flow:

```text
Page Mount
→ isLoading true
→ data loaded
→ isSuccess true
→ UI Render
```

```text
Params Change
→ isFetching true
→ new data loaded
→ UI Update
```

---

### [FAQ]

Q. isLoading과 isFetching은 달라?
A. isLoading은 최초 로딩이고 isFetching은 최초 로딩과 재조회 모두를 포함하는 fetching 상태다.

Q. data가 undefined일 수 있어?
A. 있다. 최초 로딩 전이나 오류 상황에서는 undefined일 수 있다.

Q. Empty State는 isSuccess로만 판단해도 돼?
A. 아니다. 요청 성공 후 실제 data content가 비어 있는지 확인해야 한다.

Q. refetch는 언제 써?
A. Retry Button, 새로고침 버튼, 수동 재조회가 필요할 때 사용할 수 있다.

---

# 8. useMutation Rules

## 8.1 useMutation 기본

### [개념]

`useMutation`은 서버 데이터를 생성, 수정, 삭제하는 API 요청에 사용한다.

POST / PUT / PATCH / DELETE 요청은 대부분 mutation으로 처리한다.

---

### [핵심]

useMutation 구성 요소:

- mutationFn
- mutate
- mutateAsync
- onSuccess
- onError
- onSettled
- isPending
- isError
- isSuccess
- error
- variables

사용 대상:

- create review
- update review
- delete review
- login
- signup
- update profile
- toggle favorite
- mark notification read
- file upload

주의:

- mutationFn은 API Function 사용
- 성공 후 관련 query invalidate
- 실패 시 Error State 표시
- isPending으로 중복 제출 방지
- mutation 성공 후 Form reset 가능
- mutation은 자동으로 관련 query를 갱신하지 않음

---

### [실무]

리뷰 작성 Mutation:

```tsx
export function useCreateReviewMutation() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: createReview,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["reviews"] });
    },
  });
}
```

Component 사용:

```tsx
const mutation = useCreateReviewMutation();

function handleSubmit(requestBody: ReviewCreateRequest) {
  mutation.mutate(requestBody);
}

<button type="submit" disabled={mutation.isPending}>
  {mutation.isPending ? "작성 중..." : "작성"}
</button>;

{
  mutation.error && <p role="alert">{getApiErrorMessage(mutation.error)}</p>;
}
```

mutateAsync 사용:

```tsx
async function handleSubmit(requestBody: ReviewCreateRequest) {
  try {
    await mutation.mutateAsync(requestBody);
    resetForm();
  } catch (error) {
    // error UI or field error handling
  }
}
```

---

### [FAQ]

Q. useMutation은 언제 써?
A. 서버 데이터를 생성, 수정, 삭제하는 POST, PUT, PATCH, DELETE 요청에 사용한다.

Q. mutationFn에는 뭘 넣어?
A. createReview, updateReview, deleteReview 같은 API Function을 넣는다.

Q. mutate와 mutateAsync 차이는?
A. mutate는 callback 중심이고 mutateAsync는 Promise를 반환해 async/await로 처리할 수 있다.

Q. Mutation 성공 후 목록이 자동으로 갱신돼?
A. 자동으로 관련 목록을 알 수 없으므로 invalidateQueries나 직접 cache update가 필요하다.

---

# 9. Invalidation Rules

## 9.1 invalidateQueries 기준

### [개념]

Invalidation은 서버 데이터가 변경되었을 때 관련 Query Cache를 무효화하고 다시 가져오게 만드는 작업이다.

Mutation 성공 후 목록이나 상세 데이터가 바뀌어야 한다면 `invalidateQueries`를 사용한다.

---

### [핵심]

Invalidation 사용 상황:

- create review 후 review list 갱신
- update review 후 review detail / list 갱신
- delete review 후 review list 갱신
- favorite toggle 후 festival detail / favorite list 갱신
- notification read 후 notification list / unread count 갱신
- profile update 후 myProfile 갱신

핵심 기준:

- queryKey 구조와 invalidate 대상 일치
- 너무 넓은 invalidate 남발 주의
- 필요한 관련 query만 invalidate
- list와 detail 관계 고려
- mutation 성공 후 실행

---

### [실무]

리뷰 작성 후 리뷰 목록 갱신:

```tsx
const queryClient = useQueryClient();

const mutation = useMutation({
  mutationFn: createReview,
  onSuccess: (_, variables) => {
    queryClient.invalidateQueries({
      queryKey: ["reviews", variables.festivalId],
    });
  },
});
```

찜 토글 후 관련 데이터 갱신:

```tsx
const mutation = useMutation({
  mutationFn: toggleFavorite,
  onSuccess: (_, festivalId) => {
    queryClient.invalidateQueries({ queryKey: ["festival", festivalId] });
    queryClient.invalidateQueries({ queryKey: ["myFavorites"] });
    queryClient.invalidateQueries({ queryKey: ["festivals"] });
  },
});
```

알림 읽음 처리:

```tsx
const mutation = useMutation({
  mutationFn: markNotificationRead,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ["notifications"] });
    queryClient.invalidateQueries({ queryKey: ["notificationUnreadCount"] });
  },
});
```

주의:

- queryKey가 `["reviews", festivalId, params]`라면 `["reviews", festivalId]`로 부분 invalidate 가능
- invalidate가 안 되면 queryKey 구조를 먼저 확인
- mutation variables를 활용해 정확한 queryKey 지정
- 필요한 경우 setQueryData로 직접 업데이트 가능

---

### [FAQ]

Q. invalidateQueries는 왜 써?
A. 서버 데이터가 변경되었으므로 기존 캐시를 무효화하고 최신 데이터를 다시 가져오기 위해 사용한다.

Q. mutation 후 목록이 안 바뀌어?
A. 관련 queryKey를 invalidate하지 않았거나 queryKey가 일치하지 않을 수 있다.

Q. invalidateQueries는 모든 query에 해도 돼?
A. 가능하지만 비효율적이다. 변경된 데이터와 관련된 query만 무효화하는 것이 좋다.

Q. queryKey 일부만 넣어도 invalidate돼?
A. TanStack Query는 부분 queryKey 기준으로 관련 query를 무효화할 수 있다. 프로젝트 queryKey 구조를 일관되게 설계해야 한다.

---

# 10. Query Key Factory Rules

## 10.1 Query Key Factory 기준

### [개념]

Query Key Factory는 queryKey를 함수나 객체로 표준화하는 방식이다.

queryKey 문자열이 여러 파일에 흩어지면 invalidate 대상이 틀어질 수 있으므로 Query Key Factory를 사용할 수 있다.

---

### [핵심]

Query Key Factory 목적:

- queryKey 구조 통일
- 오타 방지
- invalidate 기준 통일
- list / detail key 구분
- params 포함 기준 명확화
- 도메인별 queryKey 관리

Query Key Factory 대상:

- festivalQueryKeys
- reviewQueryKeys
- notificationQueryKeys
- userQueryKeys
- authQueryKeys

주의:

- 너무 복잡하게 만들지 않음
- domain별로 분리
- queryKey에 민감정보 넣지 않음
- params 안정성 고려
- invalidate와 useQuery에서 같은 factory 사용

---

### [실무]

Festival Query Keys:

```typescript
export const festivalQueryKeys = {
  all: ["festivals"] as const,
  lists: () => [...festivalQueryKeys.all, "list"] as const,
  list: (params: FestivalSearchParams) =>
    [...festivalQueryKeys.lists(), params] as const,
  details: () => [...festivalQueryKeys.all, "detail"] as const,
  detail: (festivalId: number) =>
    [...festivalQueryKeys.details(), festivalId] as const,
};
```

useQuery 적용:

```typescript
useQuery({
  queryKey: festivalQueryKeys.list(params),
  queryFn: () => getFestivals(params),
});
```

invalidate 적용:

```typescript
queryClient.invalidateQueries({
  queryKey: festivalQueryKeys.lists(),
});
```

Review Query Keys:

```typescript
export const reviewQueryKeys = {
  all: ["reviews"] as const,
  list: (festivalId: number, params?: ReviewListParams) =>
    ["reviews", festivalId, params] as const,
};
```

---

### [FAQ]

Q. Query Key Factory는 왜 써?
A. queryKey 오타를 줄이고 useQuery와 invalidateQueries에서 같은 기준을 사용하기 위해 쓴다.

Q. 모든 프로젝트에서 Query Key Factory가 필요해?
A. 필수는 아니다. query가 많아지고 invalidate가 복잡해질 때 유용하다.

Q. Query Key Factory는 어디에 둬?
A. 도메인별 api 또는 query 폴더에 둘 수 있다. 예: `festivalQueryKeys.ts`.

Q. invalidate에도 Query Key Factory를 써야 해?
A. 쓰는 것이 좋다. 조회와 무효화 기준이 일치해야 캐시 갱신 오류를 줄일 수 있다.

---

# 11. Conditional Query Rules

## 11.1 enabled 조건부 조회 기준

### [개념]

Conditional Query는 필수 값이 준비된 후에만 API 조회를 실행하는 방식이다.

TanStack Query에서는 `enabled` 옵션으로 조건부 실행을 제어한다.

---

### [핵심]

enabled 사용 상황:

- route param 준비 후 조회
- login user id 준비 후 조회
- access token 준비 후 조회
- dependent query
- optional filter selected
- modal open 시 조회
- search submitted 후 조회

주의:

- 필수 id가 undefined인데 API 호출하지 않음
- enabled false면 queryFn 실행 안 됨
- queryKey에는 조건값을 포함
- enabled 조건과 queryFn 인자 검증 일치
- TypeScript에서 null 가능성 처리 필요

---

### [실무]

festivalId 조건부 조회:

```tsx
const { festivalId } = useParams();
const numericFestivalId = festivalId ? Number(festivalId) : null;

const query = useQuery({
  queryKey: ["festival", numericFestivalId],
  queryFn: () => getFestivalDetail(numericFestivalId as number),
  enabled: numericFestivalId !== null,
});
```

로그인 사용자 조회:

```tsx
const { userId } = useAuth();

const query = useQuery({
  queryKey: ["myProfile", userId],
  queryFn: () => getMyProfile(),
  enabled: Boolean(userId),
});
```

검색 Submit 후 조회:

```tsx
const [submittedParams, setSubmittedParams] =
  useState<FestivalSearchParams | null>(null);

const query = useQuery({
  queryKey: ["festivals", submittedParams],
  queryFn: () => searchFestivals(submittedParams as FestivalSearchParams),
  enabled: submittedParams !== null,
});
```

---

### [FAQ]

Q. enabled는 언제 써?
A. id, token, 검색 조건 같은 필수 값이 준비된 뒤에만 API를 호출해야 할 때 사용한다.

Q. enabled false면 queryFn이 실행돼?
A. 실행되지 않는다.

Q. route param이 undefined인데 API가 호출돼?
A. enabled 조건을 설정하지 않았거나 API 함수에서 검증하지 않았을 가능성이 있다.

Q. 검색 버튼을 누른 뒤에만 조회하려면 어떻게 해?
A. 입력 중인 form state와 submittedParams를 분리하고 submittedParams가 있을 때 enabled true로 조회한다.

---

# 12. Select and Data Transform Rules

## 12.1 select 데이터 변환 기준

### [개념]

`select`는 queryFn으로 받은 데이터를 Component가 사용하기 좋은 형태로 변환하는 옵션이다.

API Function은 Backend 응답 구조를 반환하고, select는 화면에 필요한 데이터만 추출하거나 View Model로 변환할 때 사용할 수 있다.

---

### [핵심]

select 사용 대상:

- PageResponse에서 content만 추출
- DTO를 ViewModel로 변환
- nullable fallback 처리
- enum label mapping
- date formatting
- nested object flatten
- derived data 계산

주의:

- select는 cache data 관점에서 변환된 결과를 반환
- 너무 복잡한 UI 로직을 넣지 않음
- 변환 함수는 분리 가능
- 원본 Page Metadata가 필요한 경우 content만 추출하지 않음
- select 결과 타입을 Component가 사용

---

### [실무]

content만 추출:

```tsx
const query = useQuery({
  queryKey: ["festivals", params],
  queryFn: () => getFestivals(params),
  select: (pageData) => pageData.content,
});
```

ViewModel 변환:

```typescript
function toFestivalCardViewModel(festival: FestivalSummaryResponse) {
  return {
    id: festival.festivalId,
    title: festival.title,
    imageUrl: festival.imageUrl ?? "/default-image.png",
    ratingText:
      festival.averageRating === null
        ? "평점 없음"
        : festival.averageRating.toFixed(1),
  };
}
```

select 적용:

```tsx
const query = useQuery({
  queryKey: ["festivals", params],
  queryFn: () => getFestivals(params),
  select: (pageData) => ({
    ...pageData,
    content: pageData.content.map(toFestivalCardViewModel),
  }),
});
```

주의:

- Pagination UI가 필요하면 pageData 전체 유지
- select에서 throw하면 query error가 될 수 있음
- formatting 정책은 공통 util로 분리 가능
- Backend DTO와 ViewModel Type을 구분

---

### [FAQ]

Q. select는 언제 써?
A. API 응답 데이터를 Component가 쓰기 좋은 구조로 변환하고 싶을 때 사용한다.

Q. PageResponse에서 content만 select해도 돼?
A. 가능하지만 totalPages나 totalElements가 필요하면 PageResponse 전체를 유지해야 한다.

Q. select에서 날짜 formatting을 해도 돼?
A. 가능하다. 다만 공통 formatting 기준은 util 함수로 분리하는 것이 좋다.

Q. select와 API Function mapping은 뭐가 달라?
A. API Function은 응답 wrapper를 처리하고, select는 화면에 필요한 형태로 추가 변환하는 역할에 가깝다.

---

# 13. Stale Time and Cache Rules

## 13.1 staleTime / gcTime 기준

### [개념]

`staleTime`은 데이터가 fresh 상태로 간주되는 시간이다.

`gcTime`은 사용되지 않는 query cache가 메모리에 남아 있는 시간이다.

Frontend Agent는 데이터 성격에 따라 cache 정책을 선택해야 한다.

---

### [핵심]

staleTime 기준:

- 자주 바뀌지 않는 데이터 → 길게 가능
- 자주 바뀌는 데이터 → 짧게
- 사용자 직접 새로고침 가능
- stale 상태가 되면 refetch 가능

데이터별 예:

- region filters → staleTime 길게
- theme filters → staleTime 길게
- festival detail → 중간
- notification count → 짧게
- chat messages → TanStack Query보다 realtime 고려
- popular list → 짧게 가능

주의:

- staleTime 0은 즉시 stale
- 너무 긴 staleTime은 오래된 데이터 표시 가능
- 너무 짧으면 refetch가 잦음
- 서버 부하와 UX 균형 고려
- cache 정책은 데이터 변경 빈도 기준

---

### [실무]

필터 데이터:

```tsx
useQuery({
  queryKey: ["festivalFilters", "themes"],
  queryFn: getFestivalThemeFilters,
  staleTime: 1000 * 60 * 30,
});
```

상세 데이터:

```tsx
useQuery({
  queryKey: ["festival", festivalId],
  queryFn: () => getFestivalDetail(festivalId),
  staleTime: 1000 * 60,
});
```

알림 카운트:

```tsx
useQuery({
  queryKey: ["notificationUnreadCount"],
  queryFn: getNotificationUnreadCount,
  staleTime: 1000 * 10,
});
```

기본 옵션:

```tsx
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60,
      gcTime: 1000 * 60 * 5,
    },
  },
});
```

---

### [FAQ]

Q. staleTime은 뭐야?
A. 가져온 데이터가 fresh 상태로 간주되는 시간이다.

Q. staleTime을 길게 하면 뭐가 좋아?
A. 불필요한 재요청이 줄어든다. 대신 오래된 데이터가 표시될 수 있다.

Q. 필터 목록은 staleTime을 길게 해도 돼?
A. 지역, 테마 필터처럼 자주 바뀌지 않는 데이터는 길게 설정할 수 있다.

Q. 알림 카운트도 staleTime을 길게 해도 돼?
A. 알림 카운트는 자주 변할 수 있으므로 짧게 하거나 별도 실시간 전략을 검토한다.

---

# 14. Pagination Query Rules

## 14.1 Pagination과 TanStack Query

### [개념]

Pagination Query는 page, size, sort, filter 조건을 queryKey에 포함하여 페이지 단위 데이터를 조회하는 방식이다.

Page Response 기반 목록 UI에 적합하다.

---

### [핵심]

Pagination queryKey 포함 대상:

- resource name
- page
- size
- sort
- keyword
- filter
- submitted params

처리 기준:

- page 변경 시 queryKey 변경
- 검색 조건 변경 시 page reset
- UI page와 backend page 변환
- 이전 데이터 유지 여부 결정
- PageResponse 전체 반환
- Empty State는 content length 기준

주의:

- queryKey에 page 누락 금지
- queryFn params와 queryKey params 일치
- page가 0-based인지 확인
- 검색 form draft와 submitted params 구분
- totalPages가 0일 수 있음

---

### [실무]

Pagination Query:

```tsx
const params = {
  keyword,
  page: uiPage - 1,
  size: 20,
};

const query = useQuery({
  queryKey: ["festivals", params],
  queryFn: () => getFestivals(params),
});
```

Page UI:

```tsx
const pageData = query.data;

<Pagination
  currentPage={(pageData?.number ?? 0) + 1}
  totalPages={pageData?.totalPages ?? 0}
  onPageChange={setUiPage}
/>;
```

검색 조건 변경:

```typescript
function handleSearch(nextParams: FestivalSearchParams) {
  setSubmittedParams(nextParams);
  setUiPage(1);
}
```

유지 기준:

```text
Search Params Change
→ uiPage reset to 1
→ queryKey changes
→ API Request
→ PageResponse update
```

---

### [FAQ]

Q. Pagination queryKey에 page를 넣어야 해?
A. 넣어야 한다. page가 다르면 다른 데이터이므로 queryKey에 포함해야 한다.

Q. 검색 조건이 바뀌면 page는 어떻게 해?
A. 대부분 UI page 1 또는 backend page 0으로 reset한다.

Q. PageResponse에서 content만 반환해도 돼?
A. Pagination UI에 totalPages가 필요하면 PageResponse 전체를 유지해야 한다.

Q. UI page와 backend page가 다르면 어떻게 해?
A. UI는 1-based로 보여주고 API 요청 시 backend 0-based로 변환할 수 있다.

---

# 15. Infinite Query Rules

## 15.1 useInfiniteQuery 기준

### [개념]

`useInfiniteQuery`는 무한 스크롤이나 더보기 UI처럼 여러 페이지를 누적해서 조회할 때 사용하는 TanStack Query Hook이다.

Slice Response 또는 Cursor Response와 함께 사용한다.

---

### [핵심]

useInfiniteQuery 핵심:

- initialPageParam
- getNextPageParam
- fetchNextPage
- hasNextPage
- isFetchingNextPage
- pages
- pageParam
- Slice Response
- Cursor Response

사용 대상:

- notification list
- review load more
- chat history
- infinite festival list
- comment list

주의:

- 다음 pageParam 계산 기준 명확화
- hasNext / last 기준 통일
- pages를 flatMap해서 content 추출
- 검색 조건 변경 시 queryKey 변경
- 중복 요청 방지
- cursor 방식과 page 방식 구분

---

### [실무]

Slice API Function:

```typescript
export async function getNotifications(params: {
  page: number;
  size: number;
}): Promise<SliceResponse<NotificationResponse>> {
  const response = await authApi.get<
    ApiResponse<SliceResponse<NotificationResponse>>
  >("/notifications", {
    params,
  });

  return response.data.data;
}
```

useInfiniteQuery:

```tsx
const query = useInfiniteQuery({
  queryKey: ["notifications"],
  initialPageParam: 0,
  queryFn: ({ pageParam }) => getNotifications({ page: pageParam, size: 20 }),
  getNextPageParam: (lastPage) => {
    if (!lastPage.hasNext) {
      return undefined;
    }

    return lastPage.number + 1;
  },
});
```

목록 flatten:

```tsx
const notifications = query.data?.pages.flatMap((page) => page.content) ?? [];
```

더보기 버튼:

```tsx
<button
  type="button"
  disabled={!query.hasNextPage || query.isFetchingNextPage}
  onClick={() => query.fetchNextPage()}
>
  {query.isFetchingNextPage ? "불러오는 중..." : "더보기"}
</button>
```

---

### [FAQ]

Q. useInfiniteQuery는 언제 써?
A. 더보기 버튼이나 무한 스크롤처럼 여러 페이지 데이터를 누적해서 보여줄 때 사용한다.

Q. getNextPageParam은 뭐야?
A. 다음 페이지 요청에 사용할 pageParam을 계산하는 함수다.

Q. hasNextPage는 어디서 와?
A. getNextPageParam이 undefined를 반환하지 않으면 다음 페이지가 있다고 판단한다.

Q. Infinite Query의 데이터는 어디에 있어?
A. `data.pages` 배열에 각 페이지 응답이 들어 있고, 보통 flatMap으로 content를 합친다.

---

# 16. Common Mistakes

## 16.1 TanStack Query 공통 실수

### [개념]

TanStack Query 실수는 queryKey, queryFn, mutation, invalidation, Server State 개념을 혼동할 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- queryKey에 params 누락
- queryKey에 page 누락
- queryKey와 queryFn 인자 불일치
- queryFn에서 API Function 대신 URL 하드코딩
- queryFn에서 setState 실행
- queryFn이 undefined 반환
- enabled 없이 undefined id로 API 호출
- mutation 성공 후 invalidate 누락
- invalidate queryKey 불일치
- isLoading과 isFetching 혼동
- data undefined 방어 누락
- Empty State를 isSuccess만으로 판단
- Server State를 전역 Client Store에 중복 저장
- QueryClient를 Component 내부에서 생성
- queryKey에 민감정보 포함
- staleTime을 데이터 특성과 무관하게 설정
- useInfiniteQuery pages flatten 누락
- hasNext / last 기준 혼동
- Retry가 401 / 403에도 반복됨
- Network 탭 확인 없이 Cache 문제로만 판단

---

### [실무]

문제 예:

```text
문제: 검색어를 바꿨는데 목록이 그대로임
원인: queryKey에 keyword params 누락
해결: queryKey에 params 포함
```

문제 예:

```text
문제: 리뷰 작성 후 목록이 안 바뀜
원인: createReview mutation 후 reviews query invalidate 누락
해결: onSuccess에서 reviewQueryKeys list invalidate
```

문제 예:

```text
문제: 상세 API가 /festivals/undefined로 호출됨
원인: enabled 조건 없이 undefined id로 queryFn 실행
해결: enabled: Boolean(festivalId) 추가
```

문제 예:

```text
문제: 더보기 데이터가 화면에 안 나옴
원인: data.pages를 flatMap하지 않고 직접 렌더링
해결: data.pages.flatMap(page => page.content)
```

해결 우선순위:

```text
Query Key 확인
→ Query Function 인자 확인
→ Network Request 확인
→ Response Body 확인
→ Cache 상태 확인
→ Invalidation 대상 확인
→ UI State 확인
```

---

### [FAQ]

Q. TanStack Query에서 가장 흔한 실수는?
A. queryKey에 params를 빠뜨리거나 mutation 후 invalidate를 하지 않는 것이다.

Q. 검색 조건이 바뀌었는데 API가 다시 안 나가?
A. queryKey에 검색 조건이 포함되어 있는지 확인해야 한다.

Q. Mutation 성공 후 화면이 그대로야?
A. 관련 query를 invalidate하지 않았거나 queryKey가 일치하지 않을 수 있다.

Q. undefined id로 API가 호출돼?
A. enabled 조건을 추가하고 queryFn 실행 전 필수 값이 준비되었는지 확인해야 한다.

---

# 17. Part07 Checklist

## 17.1 TanStack Query 검수 기준

### [개념]

Part07 TanStack Query 문서는 Frontend Agent가 Server State를 API Layer와 연결하고, queryKey / queryFn / mutation / invalidation / pagination / infinite query를 안정적으로 설계하도록 만드는 문서다.

---

### [핵심]

Checklist:

```md
- [ ] TanStack Query 기본 개념이 포함되었는가?
- [ ] Server State와 Client State 구분이 포함되었는가?
- [ ] QueryClient 설정 기준이 포함되었는가?
- [ ] useQuery 기준이 포함되었는가?
- [ ] Query Key 설계 기준이 포함되었는가?
- [ ] Query Function 기준이 포함되었는가?
- [ ] Query State 처리 기준이 포함되었는가?
- [ ] useMutation 기준이 포함되었는가?
- [ ] invalidateQueries 기준이 포함되었는가?
- [ ] Query Key Factory 기준이 포함되었는가?
- [ ] Conditional Query enabled 기준이 포함되었는가?
- [ ] select 데이터 변환 기준이 포함되었는가?
- [ ] staleTime / gcTime 기준이 포함되었는가?
- [ ] Pagination Query 기준이 포함되었는가?
- [ ] useInfiniteQuery 기준이 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Server State Check
→ QueryClient Check
→ useQuery Check
→ queryKey Check
→ queryFn Check
→ Query State Check
→ Mutation Check
→ Invalidation Check
→ Conditional Query Check
→ Pagination Query Check
→ Infinite Query Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

최종 기준:

- Server State와 Client State 구분 가능
- QueryClient 설정 가능
- useQuery로 조회 API 연결 가능
- queryKey에 params / id / page 포함 가능
- useMutation으로 변경 API 연결 가능
- mutation 성공 후 invalidate 가능
- enabled로 조건부 조회 가능
- select로 응답 데이터 변환 가능
- Pagination Query와 Infinite Query 설계 가능
- Frontend Agent가 TanStack Query 기반 Data Fetching 코드를 생성 가능

---

### [FAQ]

Q. Part07의 목적은 뭐야?
A. Frontend Agent가 TanStack Query로 Server State 조회, 캐싱, mutation, invalidation, pagination, infinite query를 설계하게 만드는 것이다.

Q. Part07에서 가장 중요한 기준은 뭐야?
A. queryKey 설계, queryFn과 API Function 분리, mutation 후 invalidate, Server State와 Client State 구분이다.

Q. Part07 다음에는 어떤 문서가 이어지면 좋아?
A. Pagination and Infinite Scroll, File Upload, API Troubleshooting, CORS / 401 / 403 / 404 Debugging 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. TanStack Query는 뭐야?
A. API로 가져온 Server State를 조회, 캐싱, 재조회, 변경 처리하기 위한 라이브러리다.

Q. TanStack Query는 전역 상태관리 도구야?
A. 일반 Client State 전역 관리 도구라기보다 Server State와 API Cache 관리 도구다.

Q. TanStack Query는 언제 써?
A. API 데이터 캐싱, refetch, mutation, stale data 관리가 필요할 때 사용한다.

Q. TanStack Query를 쓰면 API Layer가 필요 없어?
A. 아니다. queryFn과 mutationFn에서 재사용할 API Function이 필요하다.

Q. Server State는 뭐야?
A. Backend가 원본을 소유하고 Frontend가 API로 가져오는 데이터다.

Q. Client State는 뭐야?
A. modal open, input value, tab state처럼 Frontend UI 내부에서 관리하는 상태다.

Q. API 데이터를 Redux에 넣어도 돼?
A. 가능은 하지만 TanStack Query를 사용한다면 API Cache와 중복 저장되어 동기화 비용이 커질 수 있다.

Q. 검색어 input은 Server State야?
A. 아니다. 입력 중인 검색어는 Client State이고 검색 결과는 Server State다.

Q. QueryClient는 왜 필요해?
A. TanStack Query의 Query Cache와 기본 옵션을 관리하기 위해 필요하다.

Q. QueryClientProvider는 어디에 둬?
A. 보통 App 최상단에서 Router나 주요 Component를 감싸도록 둔다.

Q. QueryClient를 Component 안에서 만들어도 돼?
A. 권장하지 않는다. 렌더링마다 새 QueryClient가 생성될 수 있어 Cache가 유지되지 않을 수 있다.

Q. retry는 기본값 그대로 써도 돼?
A. 가능하지만 401, 403, validation error 같은 요청은 무의미한 재시도가 될 수 있어 프로젝트 기준 설정이 필요하다.

Q. useQuery는 언제 써?
A. 서버 데이터를 조회하는 GET API에 사용한다. 목록, 상세, 필터, 내 정보 조회에 적합하다.

Q. queryFn에는 뭘 넣어?
A. API Function을 호출하는 함수를 넣는다. 예: `() => getFestivals(params)`.

Q. useQuery의 data는 언제 undefined일 수 있어?
A. 최초 로딩 전이나 요청 실패 상황에서 undefined일 수 있으므로 방어 처리가 필요하다.

Q. enabled는 언제 써?
A. id나 token 같은 필수 조건이 준비된 뒤에만 조회해야 할 때 사용한다.

Q. queryKey는 왜 중요해?
A. TanStack Query가 어떤 Cache 데이터를 재사용하고 무효화할지 판단하는 기준이기 때문이다.

Q. queryKey에 params를 넣어야 해?
A. 검색 조건이나 페이지 번호가 바뀌면 다른 데이터이므로 queryKey에 포함해야 한다.

Q. queryKey가 틀리면 어떤 문제가 생겨?
A. 캐시가 중복되거나 invalidate가 제대로 되지 않아 화면 데이터가 갱신되지 않을 수 있다.

Q. queryKey에 token을 넣어도 돼?
A. 권장하지 않는다. 민감정보를 queryKey에 넣지 않는 것이 좋다.

Q. queryFn 안에서 axios를 직접 써도 돼?
A. 가능하지만 API Layer 분리 원칙상 API Function을 호출하는 방식이 좋다.

Q. queryFn에서 setState를 해도 돼?
A. 권장하지 않는다. queryFn은 데이터를 반환하고 UI 상태는 useQuery 반환값으로 처리하는 것이 좋다.

Q. queryFn이 undefined를 반환하면 안 돼?
A. 안 된다. queryFn은 정상 데이터나 Promise reject를 반환해야 한다.

Q. queryFn의 인자와 queryKey가 달라도 돼?
A. 달라지면 Cache와 실제 요청 데이터가 불일치할 수 있으므로 맞춰야 한다.

Q. isLoading과 isFetching은 달라?
A. isLoading은 최초 로딩이고 isFetching은 최초 로딩과 재조회 모두를 포함하는 fetching 상태다.

Q. data가 undefined일 수 있어?
A. 있다. 최초 로딩 전이나 오류 상황에서는 undefined일 수 있다.

Q. Empty State는 isSuccess로만 판단해도 돼?
A. 아니다. 요청 성공 후 실제 data content가 비어 있는지 확인해야 한다.

Q. refetch는 언제 써?
A. Retry Button, 새로고침 버튼, 수동 재조회가 필요할 때 사용할 수 있다.

Q. useMutation은 언제 써?
A. 서버 데이터를 생성, 수정, 삭제하는 POST, PUT, PATCH, DELETE 요청에 사용한다.

Q. mutationFn에는 뭘 넣어?
A. createReview, updateReview, deleteReview 같은 API Function을 넣는다.

Q. mutate와 mutateAsync 차이는?
A. mutate는 callback 중심이고 mutateAsync는 Promise를 반환해 async/await로 처리할 수 있다.

Q. Mutation 성공 후 목록이 자동으로 갱신돼?
A. 자동으로 관련 목록을 알 수 없으므로 invalidateQueries나 직접 cache update가 필요하다.

Q. invalidateQueries는 왜 써?
A. 서버 데이터가 변경되었으므로 기존 캐시를 무효화하고 최신 데이터를 다시 가져오기 위해 사용한다.

Q. mutation 후 목록이 안 바뀌어?
A. 관련 queryKey를 invalidate하지 않았거나 queryKey가 일치하지 않을 수 있다.

Q. invalidateQueries는 모든 query에 해도 돼?
A. 가능하지만 비효율적이다. 변경된 데이터와 관련된 query만 무효화하는 것이 좋다.

Q. queryKey 일부만 넣어도 invalidate돼?
A. TanStack Query는 부분 queryKey 기준으로 관련 query를 무효화할 수 있다. 프로젝트 queryKey 구조를 일관되게 설계해야 한다.

Q. Query Key Factory는 왜 써?
A. queryKey 오타를 줄이고 useQuery와 invalidateQueries에서 같은 기준을 사용하기 위해 쓴다.

Q. 모든 프로젝트에서 Query Key Factory가 필요해?
A. 필수는 아니다. query가 많아지고 invalidate가 복잡해질 때 유용하다.

Q. Query Key Factory는 어디에 둬?
A. 도메인별 api 또는 query 폴더에 둘 수 있다. 예: `festivalQueryKeys.ts`.

Q. invalidate에도 Query Key Factory를 써야 해?
A. 쓰는 것이 좋다. 조회와 무효화 기준이 일치해야 캐시 갱신 오류를 줄일 수 있다.

Q. enabled false면 queryFn이 실행돼?
A. 실행되지 않는다.

Q. route param이 undefined인데 API가 호출돼?
A. enabled 조건을 설정하지 않았거나 API 함수에서 검증하지 않았을 가능성이 있다.

Q. 검색 버튼을 누른 뒤에만 조회하려면 어떻게 해?
A. 입력 중인 form state와 submittedParams를 분리하고 submittedParams가 있을 때 enabled true로 조회한다.

Q. select는 언제 써?
A. API 응답 데이터를 Component가 쓰기 좋은 구조로 변환하고 싶을 때 사용한다.

Q. PageResponse에서 content만 select해도 돼?
A. 가능하지만 totalPages나 totalElements가 필요하면 PageResponse 전체를 유지해야 한다.

Q. select에서 날짜 formatting을 해도 돼?
A. 가능하다. 다만 공통 formatting 기준은 util 함수로 분리하는 것이 좋다.

Q. select와 API Function mapping은 뭐가 달라?
A. API Function은 응답 wrapper를 처리하고, select는 화면에 필요한 형태로 추가 변환하는 역할에 가깝다.

Q. staleTime은 뭐야?
A. 가져온 데이터가 fresh 상태로 간주되는 시간이다.

Q. staleTime을 길게 하면 뭐가 좋아?
A. 불필요한 재요청이 줄어든다. 대신 오래된 데이터가 표시될 수 있다.

Q. 필터 목록은 staleTime을 길게 해도 돼?
A. 지역, 테마 필터처럼 자주 바뀌지 않는 데이터는 길게 설정할 수 있다.

Q. 알림 카운트도 staleTime을 길게 해도 돼?
A. 알림 카운트는 자주 변할 수 있으므로 짧게 하거나 별도 실시간 전략을 검토한다.

Q. Pagination queryKey에 page를 넣어야 해?
A. 넣어야 한다. page가 다르면 다른 데이터이므로 queryKey에 포함해야 한다.

Q. 검색 조건이 바뀌면 page는 어떻게 해?
A. 대부분 UI page 1 또는 backend page 0으로 reset한다.

Q. PageResponse에서 content만 반환해도 돼?
A. Pagination UI에 totalPages가 필요하면 PageResponse 전체를 유지해야 한다.

Q. UI page와 backend page가 다르면 어떻게 해?
A. UI는 1-based로 보여주고 API 요청 시 backend 0-based로 변환할 수 있다.

Q. useInfiniteQuery는 언제 써?
A. 더보기 버튼이나 무한 스크롤처럼 여러 페이지 데이터를 누적해서 보여줄 때 사용한다.

Q. getNextPageParam은 뭐야?
A. 다음 페이지 요청에 사용할 pageParam을 계산하는 함수다.

Q. hasNextPage는 어디서 와?
A. getNextPageParam이 undefined를 반환하지 않으면 다음 페이지가 있다고 판단한다.

Q. Infinite Query의 데이터는 어디에 있어?
A. `data.pages` 배열에 각 페이지 응답이 들어 있고, 보통 flatMap으로 content를 합친다.

Q. TanStack Query에서 가장 흔한 실수는?
A. queryKey에 params를 빠뜨리거나 mutation 후 invalidate를 하지 않는 것이다.

Q. 검색 조건이 바뀌었는데 API가 다시 안 나가?
A. queryKey에 검색 조건이 포함되어 있는지 확인해야 한다.

Q. Mutation 성공 후 화면이 그대로야?
A. 관련 query를 invalidate하지 않았거나 queryKey가 일치하지 않을 수 있다.

Q. undefined id로 API가 호출돼?
A. enabled 조건을 추가하고 queryFn 실행 전 필수 값이 준비되었는지 확인해야 한다.

Q. Part07 TanStack Query의 목적은 뭐야?
A. Frontend Agent가 TanStack Query로 Server State 조회, 캐싱, mutation, invalidation, pagination, infinite query를 설계하게 만드는 것이다.

Q. Part07 다음에는 어떤 문서가 이어지면 좋아?
A. Pagination and Infinite Scroll, File Upload, API Troubleshooting, CORS / 401 / 403 / 404 Debugging 순서로 이어지는 것이 좋다.
