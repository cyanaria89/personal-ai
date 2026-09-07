# Error Handling & Loading UX Part05 - TanStack Query UX Rules

---

# 1. TanStack Query UX Overview

## 1.1 TanStack Query UX Purpose

### [개념]

TanStack Query UX Rules는 서버 상태 조회와 변경 요청에서 발생하는 Loading, Error, Empty, Success 상태를 UI와 연결하는 기준이다.

TanStack Query는 `useQuery`, `useMutation`, `useInfiniteQuery`를 통해 서버 데이터 요청 상태를 제공하며, Frontend는 이 상태값을 사용자 경험으로 변환해야 한다.

---

### [핵심]

TanStack Query UX 주요 대상:

- `useQuery`
- `useMutation`
- `useInfiniteQuery`
- `isLoading`
- `isFetching`
- `isError`
- `isSuccess`
- `isPending`
- `error`
- `data`
- `refetch`
- `fetchNextPage`
- `hasNextPage`
- `isFetchingNextPage`
- `queryKey`
- `enabled`
- `placeholderData`
- `initialData`
- `staleTime`
- `invalidateQueries`

핵심 규칙:

- `isLoading`과 `isFetching`을 구분한다.
- `isPending`은 Mutation 처리 중 상태로 사용한다.
- 조회 실패는 Error State로 연결한다.
- 요청 성공 후 데이터가 없으면 Empty State로 연결한다.
- 재조회 중 기존 데이터를 유지할지 결정한다.
- Retry Button은 `refetch`와 연결한다.
- Mutation 성공 후 관련 Query를 invalidate한다.
- `queryKey`는 서버 상태 식별 기준이므로 안정적으로 설계한다.
- `enabled` 조건으로 불필요하거나 잘못된 요청을 막는다.
- Infinite Query는 `hasNextPage`와 `isFetchingNextPage`를 함께 확인한다.

---

### [실무]

TanStack Query 기반 UX 흐름:

```text
User enters page
→ useQuery 실행
→ isLoading
  → Initial Loading UI
→ isError
  → Error State + Retry
→ isSuccess + data empty
  → Empty State
→ isSuccess + data exists
  → Success State
→ isFetching + data exists
  → Refetch Indicator
```

Mutation UX 흐름:

```text
User submits action
→ useMutation.mutate
→ isPending
  → Disabled Button / Button Loading
→ onSuccess
  → Success Feedback
  → Query Invalidation
→ onError
  → Error Message
→ onSettled
  → Cleanup
```

---

### [FAQ]

Q. TanStack Query UX Rules는 왜 필요해?
A. Query 상태값을 Loading, Error, Empty, Success UI로 안정적으로 연결하기 위해 필요하다.

Q. TanStack Query를 쓰면 Loading / Error 처리가 자동으로 끝나?
A. 아니다. 상태값은 제공되지만 이를 어떤 UI로 보여줄지는 Frontend에서 설계해야 한다.

Q. TanStack Query에서 가장 헷갈리는 상태값은?
A. `isLoading`과 `isFetching`, `isPending`의 역할 구분이 가장 자주 헷갈린다.

Q. Query 성공 후 데이터가 없으면 어떻게 해?
A. 요청은 성공했으므로 Error State가 아니라 Empty State로 처리한다.

---

# 2. useQuery Status UX Rules

## 2.1 useQuery Loading / Error / Empty / Success

### [개념]

`useQuery`는 서버 데이터 조회 상태를 `isLoading`, `isFetching`, `isError`, `isSuccess`, `data`, `error`, `refetch` 등으로 제공한다.

Frontend는 이 상태값을 화면 상태로 변환해야 한다.

---

### [핵심]

`useQuery` 주요 상태:

- `isLoading`
- `isFetching`
- `isError`
- `isSuccess`
- `data`
- `error`
- `refetch`
- `status`
- `fetchStatus`

상태 연결:

| TanStack Query 상태        | UI 상태         | 설명                   |
| -------------------------- | --------------- | ---------------------- |
| `isLoading`                | Initial Loading | 초기 데이터 없음       |
| `isError`                  | Error State     | 요청 실패              |
| `isSuccess` + empty data   | Empty State     | 요청 성공, 데이터 없음 |
| `isSuccess` + data exists  | Success State   | 요청 성공, 데이터 있음 |
| `isFetching` + data exists | Refetch Loading | 기존 데이터 재조회 중  |

핵심 규칙:

- `isLoading`은 초기 로딩에 사용한다.
- `isFetching`은 재조회 표시로 사용한다.
- `isError`는 Error State와 연결한다.
- Empty State는 `isLoading`, `isError` 처리 후 검사한다.
- Retry Button은 `refetch`와 연결한다.
- `error`는 사용자 메시지로 mapping한다.

---

### [실무]

기본 예:

```tsx
function FestivalListPage() {
  const { data, isLoading, isFetching, isError, error, refetch } = useQuery({
    queryKey: ["festivals"],
    queryFn: getFestivals,
  });

  if (isLoading) {
    return <FestivalListSkeleton />;
  }

  if (isError) {
    return <ErrorState message={getApiErrorMessage(error)} onRetry={refetch} />;
  }

  if (!data || data.length === 0) {
    return <EmptyState title="축제 정보가 없습니다." />;
  }

  return (
    <>
      {isFetching && <p role="status">최신 정보를 확인 중입니다.</p>}
      <FestivalList festivals={data} />
    </>
  );
}
```

권장 조건부 렌더링 순서:

```text
1. isLoading
2. isError
3. data empty
4. success render
5. isFetching indicator
```

권장:

- 초기 조회는 Skeleton 또는 LoadingState로 처리한다.
- 조회 실패는 ErrorState로 처리한다.
- Empty는 요청 성공 이후에만 처리한다.
- 기존 데이터가 있는 재조회는 전체 Skeleton으로 덮지 않는다.
- ErrorState의 Retry Button은 `refetch`와 연결한다.

주의:

- `isFetching`을 `isLoading`처럼 사용하면 Refetch마다 화면이 덮인다.
- `data?.length === 0`을 `isLoading`보다 먼저 검사하지 않는다.
- `error.message`를 그대로 사용자에게 보여주지 않는다.
- API 실패를 빈 배열로 변환하면 Error State가 사라진다.

---

### [FAQ]

Q. useQuery에서 Loading UI는 어떻게 보여줘?
A. `isLoading`이 true일 때 Initial Loading UI 또는 Skeleton UI를 보여준다.

Q. TanStack Query에서 에러 UI는 어떻게 보여줘?
A. `isError`가 true일 때 error 객체를 메시지로 변환해 ErrorState를 보여주고 `refetch`로 재시도 버튼을 연결할 수 있다.

Q. useQuery 성공 후 데이터가 없으면?
A. 요청은 성공했으므로 Empty State를 보여준다.

Q. `isFetching`일 때 전체 Skeleton을 다시 보여줘야 해?
A. 항상은 아니다. 기존 데이터가 있으면 유지하고 작은 갱신 표시만 보여주는 것이 자연스러운 경우가 많다.

---

## 2.2 isLoading vs isFetching

### [개념]

`isLoading`은 초기 데이터가 없는 상태에서 요청 중임을 의미하고, `isFetching`은 초기 요청과 재요청을 포함해 Query Function이 실행 중임을 의미한다.

`isLoading`과 `isFetching`을 구분하지 않으면 Refetch 때마다 화면이 깜빡이거나 전체 Loading으로 덮일 수 있다.

---

### [핵심]

비교:

| 비교        | `isLoading`             | `isFetching`                    |
| ----------- | ----------------------- | ------------------------------- |
| 의미        | 초기 로딩               | 요청 실행 중                    |
| 데이터 존재 | 보통 없음               | 있을 수도 있음                  |
| 사용 UI     | Skeleton / Page Loading | 작은 Spinner / 갱신 문구        |
| 발생 상황   | 첫 조회                 | 첫 조회, refetch, focus refetch |
| UX 주의     | Empty보다 먼저 처리     | 기존 데이터 덮지 않기           |

핵심 규칙:

- Initial Loading은 `isLoading`으로 처리한다.
- Background Refetch는 `isFetching`으로 처리한다.
- `isFetching`이 true여도 기존 데이터가 있으면 콘텐츠를 유지한다.
- `isLoading`과 `isFetching`을 같은 UI로 처리하지 않는다.
- Refetch UX는 Flicker 방지를 우선한다.

---

### [실무]

나쁜 예:

```tsx
if (isFetching) {
  return <FestivalListSkeleton />;
}
```

문제:

- 기존 데이터가 있어도 refetch 때마다 전체 Skeleton으로 바뀐다.
- 화면 Flicker가 발생할 수 있다.

개선 예:

```tsx
if (isLoading) {
  return <FestivalListSkeleton />;
}

return (
  <>
    {isFetching && <p role="status">최신 정보를 확인 중입니다.</p>}
    <FestivalList festivals={data ?? []} />
  </>
);
```

선택 기준:

```text
isLoading true
→ 화면 첫 조회
→ Skeleton / Page Loading

isFetching true + data exists
→ 기존 데이터 유지
→ 작은 갱신 표시

isFetching true + no data
→ Initial Loading과 유사하게 처리
```

권장:

- 목록 재조회 중 기존 목록을 유지한다.
- 상세 페이지 refetch 중 기존 상세 정보를 유지한다.
- Refresh Button 주변에 loading 표시를 줄 수 있다.
- `isFetching` 메시지는 과도하게 눈에 띄지 않게 한다.

주의:

- `isFetching`을 기준으로 전체 return을 막으면 UI가 불안정해진다.
- `isLoading`만 처리하고 `isFetching`을 무시하면 재조회 중인지 알 수 없다.
- Window Focus Refetch가 켜져 있으면 `isFetching`이 자주 true가 될 수 있다.

---

### [FAQ]

Q. isLoading과 isFetching은 뭐가 달라?
A. isLoading은 초기 데이터가 없는 로딩이고 isFetching은 기존 데이터가 있어도 재조회 중이면 true가 될 수 있다.

Q. isFetching일 때 화면 전체를 로딩으로 바꿔야 해?
A. 보통 아니다. 기존 데이터를 유지하고 작은 갱신 표시를 보여주는 것이 좋다.

Q. isLoading과 isFetching이 동시에 true일 수 있어?
A. 초기 요청 중에는 둘 다 true처럼 동작할 수 있다. UX에서는 초기 로딩과 재조회 로딩을 구분해 처리한다.

Q. Refetch 중 기존 데이터를 지워야 해?
A. 항상 지울 필요는 없다. 기존 데이터를 유지하는 것이 자연스러운 경우가 많다.

---

## 2.3 Query Error Retry UX

### [개념]

Query Error Retry UX는 조회 요청 실패 시 사용자가 다시 시도할 수 있도록 `refetch`와 ErrorState를 연결하는 기준이다.

Retry UX는 일시적인 네트워크 오류, 서버 오류, 조회 실패에서 사용자가 복구 행동을 할 수 있게 한다.

---

### [핵심]

Retry UX 사용 상황:

- Network Error
- Timeout Error
- 500 Server Error
- List Fetch Failed
- Detail Fetch Failed
- Refetch Failed
- Search Request Failed

핵심 규칙:

- Retry Button은 실제 `refetch`와 연결한다.
- Retry 중 Loading 상태를 표시한다.
- 재시도 가능한 오류와 불가능한 오류를 구분한다.
- 401 / 403은 Retry보다 Login / Forbidden UX가 적합할 수 있다.
- 404 Resource Not Found는 Retry보다 목록 이동이 적합할 수 있다.
- Retry 실패 시 ErrorState가 유지되어야 한다.

---

### [실무]

Retry 예:

```tsx
function FestivalListPage() {
  const { data, isLoading, isFetching, isError, error, refetch } = useQuery({
    queryKey: ["festivals"],
    queryFn: getFestivals,
  });

  if (isLoading) {
    return <LoadingState message="축제 정보를 불러오는 중입니다." />;
  }

  if (isError) {
    return (
      <ErrorState
        message={getApiErrorMessage(error)}
        onRetry={() => refetch()}
      />
    );
  }

  return <FestivalList festivals={data ?? []} refreshing={isFetching} />;
}
```

ErrorState 예:

```tsx
function ErrorState({ message, onRetry, retrying }) {
  return (
    <section role="alert">
      <p>{message}</p>
      {onRetry && (
        <button type="button" onClick={onRetry} disabled={retrying}>
          {retrying ? "다시 시도 중..." : "다시 시도"}
        </button>
      )}
    </section>
  );
}
```

권장:

- Retry Button 문구는 명확하게 작성한다.
- Retry 중 버튼을 disabled 처리할 수 있다.
- Error Message는 사용자용 메시지로 mapping한다.
- Retry 후 성공하면 Success State로 전환한다.
- Retry 후에도 실패하면 Error State를 유지한다.

주의:

- Retry Button이 있지만 실제 재요청 함수가 없으면 안 된다.
- 인증 오류는 단순 Retry보다 로그인 이동이 필요할 수 있다.
- 권한 오류는 Retry해도 해결되지 않는 경우가 많다.
- 삭제된 리소스 404에 Retry만 제공하면 UX가 어색하다.

---

### [FAQ]

Q. Query 실패 시 다시 시도 버튼은 어떻게 연결해?
A. `useQuery`가 제공하는 `refetch` 함수를 ErrorState의 onRetry에 연결하면 된다.

Q. 모든 오류에 Retry Button을 제공해도 돼?
A. 아니다. 네트워크나 일시적 서버 오류에는 적합하지만 401, 403, 404는 Login, Forbidden, Not Found UX가 더 적합할 수 있다.

Q. Retry 중 버튼을 disabled 해야 해?
A. 중복 재시도를 줄이기 위해 Retry 중 disabled 처리할 수 있다.

Q. Retry 후 실패하면 어떻게 해?
A. ErrorState를 유지하고 사용자에게 다시 시도하거나 다른 행동을 선택할 수 있게 한다.

---

# 3. Query Key Rules

## 3.1 Query Key Design

### [개념]

`queryKey`는 TanStack Query가 서버 상태를 식별하고 캐시하는 기준이다.

`queryKey` 설계가 불안정하면 중복 요청, 캐시 불일치, invalidate 실패, stale UI 문제가 발생한다.

---

### [핵심]

Query Key 구성 요소:

- Domain Name
- Resource ID
- Search Params
- Filter Params
- Pagination Params
- Sort Params
- User Scope
- Locale optional

핵심 규칙:

- queryKey는 안정적이고 예측 가능해야 한다.
- 목록과 상세 queryKey를 구분한다.
- 검색 조건, 필터, 정렬, 페이지 값을 queryKey에 포함한다.
- Mutation 성공 후 invalidate할 queryKey와 일치해야 한다.
- 객체를 사용할 때는 구조를 안정적으로 유지한다.
- 권한 또는 사용자별 데이터는 user scope를 고려한다.

---

### [실무]

목록 Query Key:

```tsx
useQuery({
  queryKey: ["festivals", { page, size, sort, filters }],
  queryFn: () => getFestivals({ page, size, sort, filters }),
});
```

상세 Query Key:

```tsx
useQuery({
  queryKey: ["festival-detail", festivalId],
  queryFn: () => getFestivalDetail(festivalId),
});
```

사용자별 Query Key:

```tsx
useQuery({
  queryKey: ["favorites", userId],
  queryFn: () => getFavorites(userId),
  enabled: Boolean(userId),
});
```

Mutation 후 invalidate:

```tsx
queryClient.invalidateQueries({ queryKey: ["festival-detail", festivalId] });
queryClient.invalidateQueries({ queryKey: ["favorites", userId] });
```

권장:

- Query Key Naming을 팀 기준으로 통일한다.
- 목록은 `["resource", params]` 구조를 사용할 수 있다.
- 상세는 `["resource-detail", id]` 또는 `["resource", id]` 중 하나로 통일한다.
- queryFn에서 사용하는 params는 queryKey에도 포함한다.
- invalidate 대상 queryKey를 미리 설계한다.

주의:

- queryFn에서 사용하는 filter가 queryKey에 없으면 캐시가 꼬일 수 있다.
- queryKey가 매번 불안정하면 불필요한 refetch가 발생한다.
- invalidate queryKey가 실제 queryKey와 다르면 화면이 갱신되지 않는다.
- 사용자별 데이터를 공통 key로 캐시하면 다른 사용자 데이터가 섞일 수 있다.

---

### [FAQ]

Q. queryKey는 왜 중요해?
A. 서버 상태 캐시, 재조회, invalidate 기준이 되기 때문에 Query UX 안정성에 직접 영향을 준다.

Q. 검색 조건도 queryKey에 넣어야 해?
A. 넣어야 한다. 검색어, 필터, 정렬, 페이지 조건이 다르면 다른 서버 상태로 봐야 한다.

Q. queryKey가 틀리면 어떤 문제가 생겨?
A. invalidate가 동작하지 않거나 stale UI, 중복 요청, 잘못된 캐시 사용 문제가 생길 수 있다.

Q. 사용자별 데이터에는 userId를 queryKey에 넣어야 해?
A. 사용자별로 결과가 다르다면 userId 또는 사용자 scope를 queryKey에 포함하는 것이 안전하다.

---

## 3.2 Query Key and Filter UX

### [개념]

Filter UX에서 queryKey는 검색 조건과 필터 조건을 서버 상태와 연결하는 핵심 기준이다.

필터 조건이 바뀌었는데 queryKey가 바뀌지 않으면 새 요청이 발생하지 않거나 이전 데이터가 잘못 표시될 수 있다.

---

### [핵심]

Filter Query Key 대상:

- keyword
- category
- region
- theme
- dateRange
- status
- sort
- page
- size
- cursor

핵심 규칙:

- 서버 요청에 사용하는 모든 필터 값을 queryKey에 포함한다.
- 필터 변경 시 page index를 초기화한다.
- 필터 객체 구조를 안정적으로 유지한다.
- 빈 값과 undefined 기준을 통일한다.
- URL Query Param과 내부 filter state를 동기화할 수 있다.
- 필터 변경 중 Loading / Refetch UX를 분리한다.

---

### [실무]

검색 Query 예:

```tsx
const queryParams = {
  keyword,
  region,
  theme,
  startDate,
  endDate,
  page,
  size,
};

const query = useQuery({
  queryKey: ["festival-search", queryParams],
  queryFn: () => searchFestivals(queryParams),
});
```

필터 변경 시 page 초기화:

```tsx
function handleFilterChange(nextFilters) {
  setFilters(nextFilters);
  setPage(1);
}
```

빈 값 정규화 예:

```tsx
const normalizedFilters = {
  keyword: keyword.trim() || null,
  region: region || null,
  theme: theme || null,
};
```

권장:

- 필터 상태를 요청 직전에 정규화한다.
- queryKey에 들어가는 객체 shape를 일정하게 유지한다.
- page, size, sort를 queryKey에 포함한다.
- 필터 초기화 CTA와 queryKey 변경이 연결되어야 한다.
- 필터 변경 중 `isFetching` 표시를 제공할 수 있다.

주의:

- queryKey에 포함되지 않은 필터는 캐시 기준에 반영되지 않는다.
- 객체를 매번 다르게 구성하면 refetch가 과도하게 발생할 수 있다.
- page를 초기화하지 않으면 새 조건의 3페이지를 요청해 빈 결과처럼 보일 수 있다.
- 필터 요청 실패를 Empty State로 보여주지 않는다.

---

### [FAQ]

Q. 필터 조건이 바뀌면 queryKey도 바뀌어야 해?
A. 그렇다. 서버 요청 결과가 달라지는 조건은 queryKey에 포함해야 한다.

Q. 필터 변경 시 page를 왜 초기화해?
A. 이전 page index가 새 조건에서는 유효하지 않아 빈 결과처럼 보일 수 있기 때문이다.

Q. queryKey에 객체를 넣어도 돼?
A. 가능하다. 다만 객체 구조와 값 정규화 기준을 안정적으로 유지해야 한다.

Q. 필터 초기화 버튼은 TanStack Query와 어떻게 연결돼?
A. 필터 상태를 초기화하면 queryKey가 바뀌고 새 조건으로 query가 실행되어야 한다.

---

# 4. Enabled Query Rules

## 4.1 enabled Option UX

### [개념]

`enabled`는 특정 조건이 충족될 때만 Query를 실행하게 하는 TanStack Query 옵션이다.

`enabled`는 route param, userId, auth state, dependent query가 준비되지 않았을 때 잘못된 요청을 막기 위해 사용한다.

---

### [핵심]

`enabled` 사용 상황:

- route param 필요
- userId 필요
- auth initialized 필요
- access token 필요
- dependent query data 필요
- search keyword length 조건
- modal open 시점 조회
- optional section fetch

핵심 규칙:

- 필요한 값이 없을 때 요청하지 않는다.
- `enabled`가 false일 때 보여줄 UI를 별도로 설계한다.
- auth initialized 전에는 protected query를 실행하지 않는다.
- route param이 유효할 때만 상세 조회한다.
- dependent query는 선행 데이터가 준비된 뒤 실행한다.
- `enabled` 조건 오류로 무한 대기하지 않게 한다.

---

### [실무]

route param 예:

```tsx
const { festivalId } = useParams();

const query = useQuery({
  queryKey: ["festival-detail", festivalId],
  queryFn: () => getFestivalDetail(festivalId),
  enabled: Boolean(festivalId),
});
```

auth initialized 예:

```tsx
const query = useQuery({
  queryKey: ["my-profile"],
  queryFn: getMyProfile,
  enabled: authInitialized && isLoggedIn,
});
```

dependent query 예:

```tsx
const userQuery = useQuery({
  queryKey: ["user", userId],
  queryFn: () => getUser(userId),
  enabled: Boolean(userId),
});

const ordersQuery = useQuery({
  queryKey: ["orders", userQuery.data?.id],
  queryFn: () => getOrders(userQuery.data.id),
  enabled: Boolean(userQuery.data?.id),
});
```

권장:

- `enabled` 조건이 false일 때 상태 UI를 명확히 한다.
- auth loading과 query loading을 구분한다.
- param이 잘못되었으면 Not Found 또는 Invalid State를 제공한다.
- 검색어 길이 조건이 있으면 안내 문구를 제공한다.

주의:

- `enabled: false` 상태를 Loading으로 계속 보여주면 무한 Loading처럼 보인다.
- param이 undefined인데 queryFn에서 강제로 요청하면 400 / 404가 발생할 수 있다.
- authInitialized 없이 query를 실행하면 401이 먼저 발생할 수 있다.
- dependent query에서 선행 데이터 null 접근을 조심한다.

---

### [FAQ]

Q. enabled 옵션은 언제 써?
A. route param, userId, auth state처럼 필요한 값이 준비된 뒤에만 query를 실행해야 할 때 사용한다.

Q. enabled가 false면 Loading이야?
A. 항상 아니다. 요청이 시작되지 않은 상태이므로 별도 idle 또는 안내 UI를 고려해야 한다.

Q. authInitialized 전에 query를 실행하면 안 돼?
A. 인증 상태가 확정되기 전에 요청하면 불필요한 401이나 redirect flicker가 발생할 수 있다.

Q. route param이 없을 때도 상세 조회를 해야 해?
A. 아니다. 유효한 param이 있을 때만 요청하고, 없으면 Not Found 또는 잘못된 접근 UI를 제공하는 것이 좋다.

---

## 4.2 Idle State with enabled false

### [개념]

Idle State는 아직 요청을 시작하지 않은 상태다.

`enabled: false`로 Query가 실행되지 않는 경우, 사용자는 Loading 중인지 입력을 기다리는 상태인지 구분할 수 있어야 한다.

---

### [핵심]

Idle State 사용 상황:

- 검색어 입력 전
- 필수 필터 선택 전
- 모달 열기 전
- 로그인 전
- route param 없음
- dependent data 없음
- auth initialized 전

핵심 규칙:

- Idle State와 Loading State를 구분한다.
- 사용자가 해야 할 행동이 있으면 안내한다.
- 요청이 시작되지 않았는데 Spinner를 계속 보여주지 않는다.
- 검색 조건이 부족하면 검색 안내 Empty 또는 Guide State를 제공한다.
- auth 확인 전이면 Auth Loading을 별도로 표시한다.
- 잘못된 접근이면 Not Found / Redirect 기준을 따른다.

---

### [실무]

검색어 입력 전 예:

```tsx
const canSearch = keyword.trim().length >= 2;

const query = useQuery({
  queryKey: ["search", keyword],
  queryFn: () => search(keyword),
  enabled: canSearch,
});

if (!canSearch) {
  return <GuideState message="검색어를 2자 이상 입력해 주세요." />;
}
```

모달 open 시 조회 예:

```tsx
const query = useQuery({
  queryKey: ["user-detail", userId],
  queryFn: () => getUserDetail(userId),
  enabled: isOpen && Boolean(userId),
});
```

권장:

- 검색 전 상태는 Loading보다 Guide State가 적합하다.
- 조건 부족 상태는 Empty State와도 구분할 수 있다.
- enabled false의 이유가 사용자 행동 때문인지 시스템 대기 때문인지 구분한다.
- dependent query는 선행 query loading과 연결해 표시한다.

주의:

- enabled false 상태를 무조건 Empty로 처리하면 요청 결과 없음과 혼동된다.
- enabled false 상태를 무조건 Loading으로 처리하면 무한 Loading처럼 보인다.
- 검색어 조건이 부족한 상태와 검색 결과 없음은 다르다.
- auth loading과 login required를 구분한다.

---

### [FAQ]

Q. Idle State는 뭐야?
A. 아직 요청을 시작하지 않은 상태다.

Q. 검색어 입력 전에는 Loading을 보여줘야 해?
A. 아니다. 검색어 입력 안내 같은 Guide State가 더 적합하다.

Q. enabled false 상태를 Empty State로 봐도 돼?
A. 보통 다르다. 요청을 하지 않은 상태와 요청 성공 후 데이터가 없는 상태는 구분해야 한다.

Q. enabled false 때문에 화면이 계속 비어 있으면?
A. 요청 조건이 충족되지 않았을 때 보여줄 Guide State, Auth Loading, Not Found UI를 설계해야 한다.

---

# 5. Placeholder Data / Initial Data UX Rules

## 5.1 placeholderData UX

### [개념]

`placeholderData`는 새 Query가 데이터를 가져오는 동안 이전 데이터나 임시 데이터를 화면에 유지할 수 있게 하는 옵션이다.

`placeholderData`는 Pagination, Filter Change, Refetch UX에서 Flicker를 줄이는 데 사용할 수 있다.

---

### [핵심]

`placeholderData` 사용 상황:

- Pagination Page Change
- Filter Change
- Sort Change
- Search Result Refetch
- List Refresh
- Detail Refresh

핵심 규칙:

- 기존 데이터를 유지해 Flicker를 줄인다.
- 새 조건의 결과가 아닌 이전 데이터임을 표시할 수 있다.
- `isFetching`으로 갱신 중임을 알려준다.
- 완전히 다른 조건에서는 Skeleton이 더 적합할 수 있다.
- stale UI로 오해되지 않게 한다.
- Empty State 판정 시 placeholder 여부를 고려한다.

---

### [실무]

페이지 변경 예:

```tsx
const query = useQuery({
  queryKey: ["festivals", page],
  queryFn: () => getFestivals({ page }),
  placeholderData: (previousData) => previousData,
});
```

검색 목록 예:

```tsx
const query = useQuery({
  queryKey: ["festival-search", filters],
  queryFn: () => searchFestivals(filters),
  placeholderData: (previousData) => previousData,
});
```

UI 표시 예:

```tsx
return (
  <>
    {query.isFetching && <p role="status">검색 결과를 갱신 중입니다.</p>}
    <FestivalList festivals={query.data?.items ?? []} />
  </>
);
```

권장:

- pagination에서 화면 안정성을 위해 사용할 수 있다.
- 기존 데이터 유지 중에는 갱신 중 표시를 제공한다.
- 필터 조건이 크게 바뀌는 경우 사용자 혼란을 검토한다.
- 이전 데이터가 새 조건 결과처럼 보이지 않게 한다.

주의:

- 이전 데이터가 새 필터 결과처럼 오해될 수 있다.
- placeholderData가 있으면 Empty State 타이밍이 달라질 수 있다.
- 데이터가 오래된 상태인지 사용자가 알 수 있어야 한다.
- 모든 검색 조건 변경에 무조건 적용하지 않는다.

---

### [FAQ]

Q. placeholderData는 뭐야?
A. 새 Query가 데이터를 가져오는 동안 이전 데이터나 임시 데이터를 화면에 유지할 수 있게 하는 옵션이다.

Q. placeholderData는 언제 좋아?
A. 페이지 변경, 정렬 변경, 가벼운 필터 변경처럼 기존 데이터를 유지해 Flicker를 줄이고 싶을 때 좋다.

Q. placeholderData를 쓰면 Empty State는 어떻게 판단해?
A. 이전 데이터가 남아 있을 수 있으므로 실제 새 요청 완료 여부와 `isFetching` 상태를 함께 고려해야 한다.

Q. 필터가 완전히 바뀌어도 placeholderData를 써도 돼?
A. 가능하지만 이전 결과가 새 조건 결과처럼 보일 수 있으므로 갱신 중 표시가 필요하다.

---

## 5.2 initialData UX

### [개념]

`initialData`는 Query가 처음부터 특정 데이터를 가진 상태로 시작하게 하는 옵션이다.

`initialData`는 서버에서 미리 받은 데이터, 부모 화면에서 전달받은 데이터, 캐시 기반 초기값을 사용할 때 적용할 수 있다.

---

### [핵심]

`initialData` 사용 상황:

- SSR / Hydration
- Parent List Data to Detail
- Preloaded Data
- Cached Initial View
- Static Seed Data
- Known Default Data

핵심 규칙:

- `initialData`는 실제 데이터처럼 취급된다.
- 초기 Loading이 생략될 수 있다.
- 데이터 신선도 기준을 함께 설계한다.
- staleTime과 함께 고려한다.
- 잘못된 initialData는 stale UI를 만들 수 있다.
- Empty 초기값과 실제 Empty 결과를 혼동하지 않는다.

---

### [실무]

초기 데이터 예:

```tsx
const query = useQuery({
  queryKey: ["festival-detail", festivalId],
  queryFn: () => getFestivalDetail(festivalId),
  initialData: initialFestival,
});
```

캐시에서 초기값 사용 예:

```tsx
const query = useQuery({
  queryKey: ["festival-detail", festivalId],
  queryFn: () => getFestivalDetail(festivalId),
  initialData: () => {
    return queryClient
      .getQueryData(["festivals"])
      ?.find((festival) => festival.id === festivalId);
  },
});
```

권장:

- list에서 detail로 이동할 때 초기 표시용으로 사용할 수 있다.
- 신선한 데이터가 필요한 경우 background refetch를 허용한다.
- 초기 데이터가 실제 최신 데이터인지 사용자에게 중요한 경우 refetch 기준을 둔다.
- SSR / Hydration 구조에서는 initialData와 cache hydration 전략을 명확히 한다.

주의:

- initialData가 있으면 `isLoading`이 false일 수 있다.
- 오래된 데이터를 최신 데이터처럼 보여줄 수 있다.
- 빈 배열 initialData는 실제 Empty State처럼 보일 수 있다.
- 중요한 데이터는 서버 최신 확인을 고려한다.

---

### [FAQ]

Q. initialData는 뭐야?
A. Query가 처음부터 특정 데이터를 가진 상태로 시작하게 하는 옵션이다.

Q. initialData가 있으면 Loading이 안 보여?
A. 보통 초기 데이터가 있으므로 `isLoading`이 false가 될 수 있다.

Q. initialData와 placeholderData는 달라?
A. 다르다. initialData는 초기 실제 데이터처럼 사용되고 placeholderData는 새 요청 중 임시 표시용으로 사용된다.

Q. initialData가 stale UI를 만들 수 있어?
A. 가능하다. 오래된 데이터를 최신처럼 보여줄 수 있으므로 refetch와 staleTime 기준을 함께 설계해야 한다.

---

# 6. useMutation UX Rules

## 6.1 useMutation Status UX

### [개념]

`useMutation`은 서버 데이터를 생성, 수정, 삭제하는 요청 상태를 관리한다.

Mutation UX는 `isPending`, `isError`, `error`, `isSuccess`, `onSuccess`, `onError`, `onSettled`를 사용자 액션 UI와 연결하는 기준이다.

---

### [핵심]

`useMutation` 주요 상태:

- `mutate`
- `mutateAsync`
- `isPending`
- `isError`
- `isSuccess`
- `error`
- `onMutate`
- `onSuccess`
- `onError`
- `onSettled`
- `reset`

핵심 규칙:

- `isPending`으로 Submit Loading을 표시한다.
- `isPending` 중 버튼을 disabled 처리한다.
- `onSuccess`에서 Success Feedback을 제공한다.
- `onSuccess`에서 관련 Query를 invalidate한다.
- `onError`에서 사용자 메시지를 제공한다.
- `onSettled`에서 공통 정리를 할 수 있다.
- 실패 후 다시 시도 가능하게 UI를 복구한다.

---

### [실무]

기본 예:

```tsx
function ReviewForm() {
  const mutation = useMutation({
    mutationFn: createReview,
    onSuccess: () => {
      toast.success("리뷰가 등록되었습니다.");
    },
    onError: (error) => {
      toast.error(getApiErrorMessage(error));
    },
  });

  return (
    <button type="button" disabled={mutation.isPending}>
      {mutation.isPending ? "등록 중..." : "리뷰 등록"}
    </button>
  );
}
```

Query Invalidation 포함 예:

```tsx
const mutation = useMutation({
  mutationFn: createReview,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ["reviews", festivalId] });
    queryClient.invalidateQueries({
      queryKey: ["festival-detail", festivalId],
    });
    toast.success("리뷰가 등록되었습니다.");
  },
  onError: (error) => {
    toast.error(getApiErrorMessage(error));
  },
});
```

권장:

- Mutation 버튼은 `isPending`과 연결한다.
- 중복 요청을 막기 위해 pending 중 disabled 처리한다.
- 성공 메시지와 데이터 갱신을 함께 처리한다.
- 실패 메시지는 사용자용 메시지로 mapping한다.
- Form Validation Error는 Field Error로 연결한다.

주의:

- Mutation 성공 후 invalidate를 누락하면 stale UI가 남는다.
- `isPending`을 사용하지 않으면 중복 제출이 발생할 수 있다.
- 모든 mutation error를 Toast로만 처리하지 않는다.
- Field Error와 Global Error를 구분한다.

---

### [FAQ]

Q. useMutation에서 버튼 Loading은 어떻게 처리해?
A. `mutation.isPending`으로 버튼을 disabled 처리하고 문구를 “처리 중” 상태로 바꾼다.

Q. mutation 중 버튼을 disabled 해야 해?
A. 권장한다. 중복 요청을 줄이고 사용자가 처리 중임을 알 수 있다.

Q. mutation 성공 후 뭘 해야 해?
A. 관련 query invalidate, 화면 이동, form reset, 성공 메시지 표시 중 필요한 처리를 수행한다.

Q. mutation 실패 후 어떻게 해?
A. Error Message를 보여주고 사용자가 다시 시도할 수 있게 pending 상태를 해제해야 한다.

---

## 6.2 mutate vs mutateAsync UX

### [개념]

`mutate`는 callback 기반으로 mutation을 실행하고, `mutateAsync`는 Promise 기반으로 mutation 결과를 await할 수 있게 한다.

UX 기준에서는 둘 중 하나를 선택하되 Loading, Success, Error 처리 흐름이 명확해야 한다.

---

### [핵심]

비교:

| 비교      | `mutate`       | `mutateAsync`           |
| --------- | -------------- | ----------------------- |
| 방식      | callback 기반  | Promise 기반            |
| 성공 처리 | onSuccess      | try / await / onSuccess |
| 실패 처리 | onError        | try/catch / onError     |
| 적합      | 일반 버튼 액션 | 순차 처리 필요          |
| 주의      | callback 위치  | try/catch 누락          |

핵심 규칙:

- 단순 Mutation은 `mutate`와 callback으로 충분하다.
- 순차 처리가 필요하면 `mutateAsync`를 사용할 수 있다.
- `mutateAsync` 사용 시 try/catch를 누락하지 않는다.
- Loading은 mutation state를 사용한다.
- 중복 요청 방지는 방식과 관계없이 필요하다.

---

### [실무]

`mutate` 예:

```tsx
const mutation = useMutation({
  mutationFn: createPost,
  onSuccess: () => {
    toast.success("게시글이 등록되었습니다.");
  },
  onError: (error) => {
    toast.error(getApiErrorMessage(error));
  },
});

function handleSubmit(values) {
  mutation.mutate(values);
}
```

`mutateAsync` 예:

```tsx
const mutation = useMutation({
  mutationFn: createPost,
});

async function handleSubmit(values) {
  try {
    const createdPost = await mutation.mutateAsync(values);
    toast.success("게시글이 등록되었습니다.");
    navigate(`/posts/${createdPost.id}`);
  } catch (error) {
    setFormError(getApiErrorMessage(error));
  }
}
```

권장:

- redirect처럼 결과값이 필요한 흐름에는 `mutateAsync`가 편할 수 있다.
- Form에서는 try/catch로 Field Error와 Global Error를 나눌 수 있다.
- 단순 등록 / 삭제는 `mutate` + callback 구조가 명확하다.
- 팀 기준으로 한 방식을 우선 정하면 일관성이 좋아진다.

주의:

- `mutateAsync`에서 catch를 빼면 Unhandled Promise Rejection이 발생할 수 있다.
- `mutate`와 `mutateAsync` 성공 처리를 중복으로 작성하지 않는다.
- `onSuccess`와 try block에서 같은 Toast를 두 번 띄우지 않는다.
- 성공 후 이동과 invalidate 순서를 고려한다.

---

### [FAQ]

Q. mutate와 mutateAsync는 뭐가 달라?
A. mutate는 callback 기반이고 mutateAsync는 Promise 기반으로 await할 수 있다.

Q. Form 제출에는 mutate와 mutateAsync 중 뭐가 좋아?
A. 단순 제출은 mutate로 충분하고, 성공 결과를 받아 이동하거나 순차 처리가 필요하면 mutateAsync가 편하다.

Q. mutateAsync 쓸 때 주의할 점은?
A. try/catch를 사용해 실패를 처리하고 중복 성공 메시지가 발생하지 않게 해야 한다.

Q. mutateAsync에서도 isPending을 쓸 수 있어?
A. 사용할 수 있다. mutation 상태는 mutate와 mutateAsync 모두에서 동일하게 활용할 수 있다.

---

## 6.3 Mutation Error Mapping

### [개념]

Mutation Error Mapping은 생성, 수정, 삭제 요청 실패를 사용자 메시지, Field Error, Global Error, Toast Error로 변환하는 기준이다.

Mutation Error는 사용자 입력 문제, 권한 문제, 중복 요청, 서버 오류 등으로 나뉘며 UI 위치가 달라져야 한다.

---

### [핵심]

Mutation Error 유형:

- Field Validation Error
- Global Form Error
- Authentication Error
- Permission Error
- Conflict Error
- Network Error
- Timeout Error
- Server Error
- Unknown Error

핵심 규칙:

- Field Validation Error는 input 근처에 표시한다.
- Form 전체 오류는 Form Alert로 표시한다.
- 짧은 액션 실패는 Toast로 표시할 수 있다.
- 권한 오류는 Permission Message 또는 Forbidden UX로 처리한다.
- 409 Conflict는 서버 상태 refetch를 고려한다.
- Timeout은 처리 여부 확인이 필요할 수 있다.
- 서버 원문 메시지를 그대로 노출하지 않는다.

---

### [실무]

Form Mutation Error 예:

```tsx
const mutation = useMutation({
  mutationFn: signup,
  onError: (error) => {
    if (isValidationError(error)) {
      setFieldErrors(mapFieldErrors(error));
      return;
    }

    setFormError(getApiErrorMessage(error));
  },
});
```

Button Action Error 예:

```tsx
const favoriteMutation = useMutation({
  mutationFn: toggleFavorite,
  onError: (error) => {
    if (isConflictError(error)) {
      queryClient.invalidateQueries({
        queryKey: ["festival-detail", festivalId],
      });
      return;
    }

    toast.error(getApiErrorMessage(error));
  },
});
```

삭제 요청 Error 예:

```tsx
const deleteMutation = useMutation({
  mutationFn: deletePost,
  onError: (error) => {
    toast.error("게시글 삭제에 실패했습니다.");
  },
});
```

권장:

- Form Error와 Toast Error를 구분한다.
- 400 / 422는 Field Error로 우선 검토한다.
- 401은 로그인 UX와 연결한다.
- 403은 권한 없음 UX와 연결한다.
- 409는 refetch 또는 상태 동기화로 복구한다.
- 500은 generic message를 사용한다.

주의:

- 모든 Mutation Error를 Toast로 처리하면 Form UX가 나빠진다.
- Field Error를 Global Error로만 보여주면 수정 위치를 알기 어렵다.
- 409 Conflict를 무시하면 UI 상태가 서버와 어긋날 수 있다.
- 결제 Timeout을 단순 재시도로 안내하면 중복 결제 위험이 있다.

---

### [FAQ]

Q. Mutation Error는 어디에 보여줘?
A. Field 오류는 input 근처, Form 전체 오류는 Form Alert, 짧은 액션 실패는 Toast로 보여주는 것이 좋다.

Q. useMutation에서 Validation Error는 어떻게 처리해?
A. 서버 field errors를 Form field errors로 매핑해 input 근처에 표시한다.

Q. 좋아요 실패는 Toast로 보여줘도 돼?
A. 가능하다. 짧은 액션 실패이므로 Toast가 적합한 경우가 많다.

Q. 409 Conflict가 나면 어떻게 해?
A. 최신 서버 상태를 refetch하거나 UI 상태를 서버 상태에 맞게 동기화하는 것이 좋다.

---

# 7. Query Invalidation Rules

## 7.1 Invalidate After Mutation Success

### [개념]

Query Invalidation은 Mutation 성공 후 관련 Query를 stale 상태로 표시하고 다시 조회하도록 만드는 작업이다.

TanStack Query UX에서 Success Feedback은 메시지만 보여주는 것이 아니라 서버 상태와 화면 데이터를 동기화해야 완성된다.

---

### [핵심]

Invalidate 대상:

- List Query
- Detail Query
- Count Query
- Summary Query
- User Scope Query
- Notification Badge Query
- Favorite List Query
- Review List Query
- Search Result Query

핵심 규칙:

- Mutation이 영향을 주는 Query를 식별한다.
- 목록과 상세 데이터를 함께 고려한다.
- count, badge, summary 데이터도 고려한다.
- queryKey가 실제 사용 key와 일치해야 한다.
- 불필요한 전체 invalidate를 피한다.
- 성공 Toast만 띄우고 invalidate를 생략하지 않는다.

---

### [실무]

리뷰 등록 예:

```tsx
const mutation = useMutation({
  mutationFn: createReview,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ["reviews", festivalId] });
    queryClient.invalidateQueries({
      queryKey: ["festival-detail", festivalId],
    });
    toast.success("리뷰가 등록되었습니다.");
  },
});
```

찜 토글 예:

```tsx
const mutation = useMutation({
  mutationFn: toggleFavorite,
  onSuccess: () => {
    queryClient.invalidateQueries({
      queryKey: ["festival-detail", festivalId],
    });
    queryClient.invalidateQueries({ queryKey: ["favorites", userId] });
  },
});
```

알림 읽음 예:

```tsx
const mutation = useMutation({
  mutationFn: markNotificationAsRead,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ["notifications", userId] });
    queryClient.invalidateQueries({ queryKey: ["notification-count", userId] });
  },
});
```

권장:

- 액션별 영향 범위를 표로 정리한다.
- 목록, 상세, 카운트 동기화를 함께 검토한다.
- userId가 포함된 queryKey는 invalidate에도 포함한다.
- 성공 후 즉시 화면 변화가 필요하면 cache update를 고려한다.

주의:

- queryKey 불일치로 invalidate가 실패할 수 있다.
- 좋아요 수, 리뷰 수, 알림 수 갱신을 놓치기 쉽다.
- 전체 query invalidate는 네트워크 비용을 늘릴 수 있다.
- invalidate 후 `isFetching` UX가 적절한지 확인한다.

---

### [FAQ]

Q. Mutation 성공 후 Query Invalidation은 왜 필요해?
A. 서버 상태가 바뀐 뒤 화면의 캐시 데이터도 최신 상태로 동기화해야 하기 때문이다.

Q. 어떤 Query를 invalidate해야 해?
A. Mutation이 영향을 주는 목록, 상세, 카운트, 요약 데이터를 기준으로 결정한다.

Q. queryKey가 틀리면 어떻게 돼?
A. invalidate가 제대로 동작하지 않아 화면이 오래된 데이터를 계속 보여줄 수 있다.

Q. 성공 Toast는 있는데 목록이 그대로야?
A. Query Invalidation 또는 cache update가 누락되었을 가능성이 높다.

---

## 7.2 Direct Cache Update UX

### [개념]

Direct Cache Update는 Mutation 성공 후 refetch 없이 Query Cache를 직접 수정해 UI를 즉시 갱신하는 방식이다.

Direct Cache Update는 좋아요 수, 찜 상태, 알림 읽음 상태처럼 작은 변경에 사용할 수 있다.

---

### [핵심]

Direct Cache Update 사용 상황:

- Like Count Update
- Favorite State Toggle
- Notification Read State
- Small Status Change
- Local List Item Update
- Simple Count Update

핵심 규칙:

- Cache 구조를 정확히 알고 있어야 한다.
- Query Key가 정확해야 한다.
- 복잡한 변경은 invalidate가 더 안전할 수 있다.
- 서버 응답 값을 기준으로 cache를 갱신하는 것이 안전하다.
- Optimistic Update와 구분한다.
- 최종 동기화를 위해 invalidate를 함께 사용할 수 있다.

---

### [실무]

서버 응답 기반 cache update:

```tsx
const mutation = useMutation({
  mutationFn: toggleFavorite,
  onSuccess: (result) => {
    queryClient.setQueryData(["festival-detail", festivalId], (old) => {
      if (!old) {
        return old;
      }

      return {
        ...old,
        favorited: result.favorited,
        favoriteCount: result.favoriteCount,
      };
    });
  },
});
```

알림 읽음 update:

```tsx
queryClient.setQueryData(["notifications", userId], (old) => {
  if (!old) {
    return old;
  }

  return {
    ...old,
    items: old.items.map((item) =>
      item.id === notificationId ? { ...item, read: true } : item,
    ),
  };
});
```

권장:

- 서버 응답이 최신 상태를 포함하면 cache update에 활용한다.
- 작은 상태 변경에는 직접 update가 UX상 빠르다.
- 복잡한 목록 / 검색 / 페이지네이션은 invalidate가 안전하다.
- 직접 update 후 필요한 경우 invalidate로 최종 동기화한다.

주의:

- cache shape를 잘못 가정하면 runtime error가 발생할 수 있다.
- 페이지네이션 / infinite query cache는 구조가 복잡하다.
- 여러 queryKey에 같은 데이터가 있으면 모두 갱신해야 할 수 있다.
- 직접 update만 하고 서버 상태와 불일치하면 stale UI가 생긴다.

---

### [FAQ]

Q. Direct Cache Update는 뭐야?
A. Mutation 성공 후 refetch 없이 Query Cache를 직접 수정해 UI를 즉시 갱신하는 방식이다.

Q. Direct Cache Update와 invalidate 중 뭐가 좋아?
A. 작은 상태 변경은 Direct Cache Update가 빠르고, 복잡한 데이터는 invalidate가 안전하다.

Q. Cache Update할 때 가장 조심할 점은?
A. queryKey와 cache data shape를 정확히 알아야 한다.

Q. Direct Cache Update 후에도 invalidate가 필요해?
A. 최종 서버 상태 동기화가 중요하면 invalidate를 함께 사용할 수 있다.

---

# 8. useInfiniteQuery UX Rules

## 8.1 Infinite Query Loading UX

### [개념]

`useInfiniteQuery`는 무한 스크롤이나 더보기 목록처럼 페이지 단위 데이터를 누적해서 조회할 때 사용하는 Query 방식이다.

Infinite Query UX는 초기 로딩, 다음 페이지 로딩, 마지막 페이지, 다음 페이지 실패 상태를 구분해야 한다.

---

### [핵심]

Infinite Query 주요 상태:

- `data.pages`
- `fetchNextPage`
- `hasNextPage`
- `isFetchingNextPage`
- `isLoading`
- `isError`
- `error`
- `refetch`
- `getNextPageParam`

핵심 규칙:

- 초기 로딩은 `isLoading`으로 처리한다.
- 다음 페이지 로딩은 `isFetchingNextPage`로 처리한다.
- 기존 목록은 유지한다.
- `hasNextPage`가 false면 추가 요청하지 않는다.
- `isFetchingNextPage` 중 중복 요청을 막는다.
- `getNextPageParam` 기준을 명확히 한다.
- 다음 페이지 실패 시 하단 Error UI를 제공할 수 있다.

---

### [실무]

기본 예:

```tsx
function ReviewList() {
  const {
    data,
    isLoading,
    isError,
    error,
    refetch,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage,
  } = useInfiniteQuery({
    queryKey: ["reviews"],
    queryFn: fetchReviews,
    getNextPageParam: (lastPage) => lastPage.nextCursor,
  });

  if (isLoading) {
    return <ReviewListSkeleton />;
  }

  if (isError) {
    return <ErrorState message={getApiErrorMessage(error)} onRetry={refetch} />;
  }

  const reviews = data?.pages.flatMap((page) => page.items) ?? [];

  if (reviews.length === 0) {
    return <EmptyState title="아직 리뷰가 없습니다." />;
  }

  return (
    <>
      <ReviewItems reviews={reviews} />
      {hasNextPage && (
        <button
          type="button"
          onClick={() => fetchNextPage()}
          disabled={isFetchingNextPage}
        >
          {isFetchingNextPage ? "불러오는 중..." : "더보기"}
        </button>
      )}
    </>
  );
}
```

권장:

- `pages.flatMap`으로 목록을 안전하게 만든다.
- 초기 Empty와 다음 페이지 없음 상태를 구분한다.
- 더보기 버튼은 `hasNextPage`가 있을 때만 보여준다.
- 다음 페이지 요청 중 버튼을 disabled 처리한다.
- 마지막 페이지 도달 시 버튼을 숨기거나 완료 메시지를 제공한다.

주의:

- `hasNextPage` 없이 `fetchNextPage`를 호출하면 불필요한 요청이 발생할 수 있다.
- `isFetchingNextPage` guard가 없으면 중복 페이지가 append될 수 있다.
- `getNextPageParam`이 잘못되면 무한 요청이 발생한다.
- 초기 Error와 다음 페이지 Error를 같은 UI로 처리할지 검토한다.

---

### [FAQ]

Q. useInfiniteQuery에서 초기 Loading과 다음 페이지 Loading은 어떻게 달라?
A. 초기 Loading은 `isLoading`, 다음 페이지 Loading은 `isFetchingNextPage`로 처리한다.

Q. 더보기 버튼은 언제 숨겨?
A. `hasNextPage`가 false이면 더보기 버튼을 숨기거나 마지막 안내 메시지를 보여준다.

Q. 더보기 중 중복 요청은 어떻게 막아?
A. `isFetchingNextPage` 중에는 버튼을 disabled 처리하고 fetchNextPage 호출을 막는다.

Q. Infinite Query에서 Empty State는 언제 보여줘?
A. 초기 요청 성공 후 전체 items가 비어 있을 때 Empty State를 보여준다.

---

## 8.2 Infinite Scroll Query UX

### [개념]

Infinite Scroll Query UX는 사용자가 목록 하단에 도달했을 때 `fetchNextPage`를 자동 호출하는 구조다.

Infinite Scroll은 `hasNextPage`, `isFetchingNextPage`, observer cleanup, queryKey 변경 처리가 중요하다.

---

### [핵심]

Infinite Scroll 구성:

- Bottom Sentinel
- IntersectionObserver
- `fetchNextPage`
- `hasNextPage`
- `isFetchingNextPage`
- Observer Cleanup
- QueryKey Reset
- Bottom Loading Indicator

핵심 규칙:

- `hasNextPage`가 false면 요청하지 않는다.
- `isFetchingNextPage`가 true면 요청하지 않는다.
- observer를 중복 등록하지 않는다.
- 컴포넌트 unmount 시 cleanup한다.
- 검색 조건 변경 시 목록과 cursor를 초기화한다.
- 하단 Loading Indicator를 제공한다.
- 실패 시 재시도 UI를 제공한다.

---

### [실무]

Observer Guard 예:

```tsx
function handleIntersect() {
  if (!hasNextPage || isFetchingNextPage) {
    return;
  }

  fetchNextPage();
}
```

UI 예:

```tsx
return (
  <>
    <FestivalItems items={items} />
    {isFetchingNextPage && (
      <p role="status">더 많은 축제를 불러오는 중입니다.</p>
    )}
    <div ref={sentinelRef} />
  </>
);
```

Flow:

```text
List Render
→ Sentinel Visible
→ hasNextPage 확인
→ isFetchingNextPage 확인
→ fetchNextPage
→ Append Items
→ nextCursor 갱신
```

권장:

- 하단 sentinel element를 명확히 둔다.
- observer callback에서 guard를 먼저 확인한다.
- 검색 조건이 변경되면 queryKey를 변경한다.
- 다음 페이지 실패 시 하단 Retry UI를 제공한다.
- 너무 빠른 연속 호출은 throttle 또는 guard를 검토한다.

주의:

- StrictMode 개발 환경에서 effect가 두 번 실행될 수 있다.
- observer cleanup 누락은 중복 요청으로 이어질 수 있다.
- cursor가 null인데 계속 요청하면 무한 요청이 된다.
- queryKey가 바뀌지 않으면 이전 조건 목록이 남을 수 있다.

---

### [FAQ]

Q. Infinite Scroll에서 fetchNextPage는 언제 호출해?
A. 하단 sentinel이 보이고 `hasNextPage`가 true이며 `isFetchingNextPage`가 false일 때 호출한다.

Q. Infinite Scroll에서 API가 여러 번 호출돼?
A. observer 중복 등록, cleanup 누락, guard 조건 누락, StrictMode 영향을 확인해야 한다.

Q. 검색 조건 변경 시 Infinite Query는 어떻게 해?
A. queryKey가 새 조건으로 바뀌어야 하고 cursor 또는 page 상태가 초기화되어야 한다.

Q. Infinite Scroll 실패 시 어떻게 해?
A. 기존 목록은 유지하고 하단에 다시 시도 버튼이나 오류 메시지를 제공한다.

---

# 9. Query Accessibility Rules

## 9.1 Query Loading Accessibility

### [개념]

Query Loading Accessibility는 TanStack Query로 발생하는 로딩 상태를 보조 기술 사용자도 인지할 수 있게 하는 기준이다.

`isLoading`, `isFetching`, `isPending`, `isFetchingNextPage` 상태는 시각적 UI뿐 아니라 텍스트와 ARIA 속성으로도 표현해야 한다.

---

### [핵심]

접근성 대상:

- Initial Loading
- Refetch Loading
- Submit Loading
- Infinite Loading
- Button Loading
- Error Retry Loading
- Background Fetching

핵심 규칙:

- Loading Message를 텍스트로 제공한다.
- `role="status"`를 고려한다.
- `aria-live="polite"`를 과도하게 남발하지 않는다.
- Skeleton은 장식 요소로 처리할 수 있다.
- 버튼 Loading은 버튼 문구를 변경한다.
- Refetch 상태는 과도하게 반복 공지하지 않는다.

---

### [실무]

Initial Loading 예:

```tsx
if (isLoading) {
  return (
    <section aria-busy="true">
      <p role="status">데이터를 불러오는 중입니다.</p>
    </section>
  );
}
```

Refetch 표시 예:

```tsx
{
  isFetching && (
    <p role="status" aria-live="polite">
      최신 정보를 확인 중입니다.
    </p>
  );
}
```

Mutation Button 예:

```tsx
<button type="submit" disabled={mutation.isPending}>
  {mutation.isPending ? "저장 중..." : "저장"}
</button>
```

Infinite Loading 예:

```tsx
{
  isFetchingNextPage && <p role="status">다음 목록을 불러오는 중입니다.</p>;
}
```

권장:

- 상태 변화 메시지는 짧게 작성한다.
- 버튼 내부 로딩은 버튼 텍스트로 전달한다.
- Skeleton만 보여주지 말고 loading label을 제공한다.
- Refetch가 자주 발생하면 aria-live 공지를 최소화한다.

주의:

- Window Focus Refetch마다 aria-live가 반복되면 방해가 될 수 있다.
- Spinner icon만 있으면 스크린 리더가 상태를 알기 어렵다.
- Disabled Button만 있고 설명이 없으면 상태를 이해하기 어렵다.
- Skeleton 여러 개가 모두 읽히지 않게 한다.

---

### [FAQ]

Q. TanStack Query Loading에도 접근성이 필요해?
A. 필요하다. 보조 기술 사용자도 요청 상태를 이해할 수 있어야 한다.

Q. isFetching 메시지를 항상 aria-live로 알려야 해?
A. 항상은 아니다. 너무 자주 발생하면 방해가 될 수 있으므로 필요한 경우만 사용한다.

Q. Mutation 버튼 로딩은 접근성상 어떻게 처리해?
A. 버튼 문구를 “저장 중...”처럼 변경하고 disabled 상태를 함께 사용할 수 있다.

Q. Skeleton은 스크린 리더가 읽어야 해?
A. 대부분 장식 요소로 보고 aria-hidden 처리하거나 별도 Loading Message를 제공하는 것이 좋다.

---

## 9.2 Query Error Accessibility

### [개념]

Query Error Accessibility는 `isError` 상태에서 오류 메시지를 보조 기술 사용자가 인지하고 다음 행동을 수행할 수 있게 하는 기준이다.

ErrorState는 텍스트 메시지, role, Retry Button 접근성을 포함해야 한다.

---

### [핵심]

접근성 대상:

- ErrorState
- Retry Button
- Form Error
- Field Error
- Global Error
- Page Error
- Not Found State
- Forbidden State

핵심 규칙:

- Error Message를 텍스트로 제공한다.
- 중요한 오류에는 `role="alert"`를 고려한다.
- Retry Button은 키보드로 접근 가능해야 한다.
- Field Error는 `aria-invalid`, `aria-describedby`와 연결한다.
- 색상만으로 오류를 전달하지 않는다.
- ErrorState에 다음 행동을 제공한다.

---

### [실무]

Query ErrorState 예:

```tsx
function QueryErrorState({ message, onRetry }) {
  return (
    <section role="alert">
      <p>{message}</p>
      <button type="button" onClick={onRetry}>
        다시 시도
      </button>
    </section>
  );
}
```

사용 예:

```tsx
if (isError) {
  return (
    <QueryErrorState message={getApiErrorMessage(error)} onRetry={refetch} />
  );
}
```

Field Error 예:

```tsx
<input
  id="email"
  aria-invalid={Boolean(errors.email)}
  aria-describedby={errors.email ? "email-error" : undefined}
/>;
{
  errors.email && (
    <p id="email-error" role="alert">
      {errors.email}
    </p>
  );
}
```

권장:

- ErrorState 메시지는 사용자에게 이해 가능한 문구로 작성한다.
- Retry Button label은 명확히 작성한다.
- Not Found와 Forbidden도 heading과 action을 제공한다.
- Form Error는 field와 연결한다.

주의:

- 오류를 색상만으로 표시하지 않는다.
- Retry Button이 div로 구현되면 키보드 접근성이 낮다.
- 서버 원문 오류를 그대로 노출하지 않는다.
- role alert를 너무 많은 곳에 남발하지 않는다.

---

### [FAQ]

Q. Query ErrorState에는 role alert가 필요해?
A. 중요한 오류 메시지는 role alert를 고려할 수 있다. 다만 과도하게 남발하지 않는다.

Q. Retry Button은 접근성상 어떻게 구현해?
A. 실제 button 요소를 사용하고 명확한 label을 제공하는 것이 좋다.

Q. Error Message는 색상만 빨갛게 하면 돼?
A. 아니다. 텍스트, 아이콘, ARIA 속성 등 색상 외 정보가 필요하다.

Q. Field Error는 Query Error와 다르게 처리해?
A. 그렇다. Field Error는 input과 직접 연결해야 한다.

---

# 10. TanStack Query Troubleshooting Rules

## 10.1 Query Not Refetching

### [개념]

Query Not Refetching은 데이터가 바뀌었는데 Query가 다시 실행되지 않거나 화면이 오래된 데이터를 계속 보여주는 문제다.

주요 원인은 queryKey 누락, invalidate queryKey 불일치, enabled 조건, staleTime, cache update 누락이다.

---

### [핵심]

주요 원인:

- queryKey에 filter 누락
- queryKey에 page / sort 누락
- invalidate queryKey 불일치
- `enabled`가 계속 false
- `staleTime`이 너무 김
- mutation onSuccess 누락
- queryClient 범위 문제
- 직접 cache update 누락
- QueryClientProvider 설정 문제

핵심 규칙:

- queryFn에서 사용하는 조건은 queryKey에도 포함한다.
- Mutation 성공 후 영향 받는 Query를 invalidate한다.
- invalidate queryKey가 실제 queryKey와 맞는지 확인한다.
- enabled 조건이 true가 되는지 확인한다.
- staleTime 기준을 확인한다.
- QueryClientProvider가 올바르게 감싸는지 확인한다.

---

### [실무]

Debug Flow:

```text
데이터가 갱신되지 않음
→ queryKey 확인
→ queryFn params 확인
→ invalidateQueries key 확인
→ enabled 조건 확인
→ staleTime 확인
→ onSuccess 실행 확인
→ QueryClientProvider 확인
```

나쁜 예:

```tsx
useQuery({
  queryKey: ["festivals"],
  queryFn: () => getFestivals({ region, theme }),
});
```

문제:

- region, theme이 queryKey에 없어 필터 변경이 캐시에 반영되지 않는다.

개선 예:

```tsx
useQuery({
  queryKey: ["festivals", { region, theme }],
  queryFn: () => getFestivals({ region, theme }),
});
```

invalidate 불일치 예:

```tsx
// 실제 queryKey
["festival-detail", festivalId];

// 잘못된 invalidate
queryClient.invalidateQueries({ queryKey: ["festival", festivalId] });
```

권장:

- queryKey를 상수 함수로 관리할 수 있다.
- invalidation 대상은 mutation 설계 시 함께 정의한다.
- filter, sort, pagination은 queryKey에 포함한다.
- Devtools로 Query Key와 상태를 확인한다.

주의:

- queryKey 불일치는 stale UI의 대표 원인이다.
- enabled false는 query 미실행 상태다.
- staleTime이 길면 예상보다 refetch가 늦을 수 있다.
- mutation 성공 후 Toast만 띄우면 데이터는 갱신되지 않는다.

---

### [FAQ]

Q. 데이터가 바뀌었는데 화면이 그대로야?
A. queryKey, invalidate queryKey, onSuccess, staleTime, enabled 조건을 확인해야 한다.

Q. 필터를 바꿨는데 API가 다시 호출되지 않아?
A. 필터 값이 queryKey에 포함되어 있는지 확인해야 한다.

Q. invalidateQueries를 했는데 화면이 안 바뀌어?
A. invalidate한 queryKey가 실제 useQuery의 queryKey와 일치하는지 확인해야 한다.

Q. staleTime이 길면 refetch가 안 돼?
A. fresh 상태로 간주되어 자동 refetch가 예상보다 늦게 발생할 수 있다.

---

## 10.2 Duplicate Query Request

### [개념]

Duplicate Query Request는 동일한 Query 요청이 의도보다 여러 번 발생하는 문제다.

주요 원인은 StrictMode, queryKey 불안정, useEffect와 Query 중복 사용, enabled 조건 변화, observer 중복 실행이다.

---

### [핵심]

주요 원인:

- React StrictMode 개발 중복 실행
- queryKey 객체 불안정
- useEffect에서 별도 fetch 중복 실행
- enabled 조건이 반복 변경
- component remount
- refetchOnWindowFocus
- retry 옵션
- interceptor 중복 등록
- Infinite Scroll observer 중복 실행

핵심 규칙:

- 개발 StrictMode 중복과 운영 중복을 구분한다.
- queryKey를 안정적으로 설계한다.
- TanStack Query와 수동 fetch를 중복 사용하지 않는다.
- enabled 조건이 불필요하게 흔들리지 않게 한다.
- refetchOnWindowFocus 동작을 이해한다.
- Infinite Scroll observer cleanup을 처리한다.

---

### [실무]

Debug Flow:

```text
중복 요청 발생
→ StrictMode 여부 확인
→ Query Key 변경 여부 확인
→ 컴포넌트 remount 확인
→ useEffect fetch 중복 확인
→ refetchOnWindowFocus 확인
→ retry 옵션 확인
→ observer cleanup 확인
```

중복 fetch 나쁜 예:

```tsx
const query = useQuery({
  queryKey: ["festivals"],
  queryFn: getFestivals,
});

useEffect(() => {
  getFestivals();
}, []);
```

문제:

- TanStack Query와 useEffect fetch가 동시에 실행된다.

queryKey 불안정 예:

```tsx
useQuery({
  queryKey: ["search", { keyword: keyword.trim(), createdAt: Date.now() }],
  queryFn: search,
});
```

문제:

- Date.now() 때문에 매번 다른 queryKey가 된다.

권장:

- 서버 데이터 요청은 TanStack Query로 일원화한다.
- queryKey에 시간값, 랜덤값, 매번 바뀌는 객체를 넣지 않는다.
- refetchOnWindowFocus 기본 동작을 팀 기준에 맞게 조정한다.
- Retry 옵션으로 인한 재요청을 오류와 구분한다.

주의:

- 개발 환경 StrictMode에서 effect가 두 번 보일 수 있다.
- Query retry 때문에 실패 요청이 여러 번 보일 수 있다.
- Window Focus Refetch는 탭 전환 시 요청을 발생시킬 수 있다.
- 중복 요청을 무조건 버그로 단정하지 말고 원인을 분류한다.

---

### [FAQ]

Q. TanStack Query API가 두 번 호출돼?
A. StrictMode, retry 옵션, refetchOnWindowFocus, queryKey 변경, 수동 fetch 중복을 확인해야 한다.

Q. useQuery를 쓰면서 useEffect fetch도 같이 써도 돼?
A. 권장하지 않는다. 같은 데이터를 두 방식으로 가져오면 중복 요청과 상태 불일치가 생긴다.

Q. refetchOnWindowFocus 때문에 요청이 다시 나갈 수 있어?
A. 그렇다. 창 포커스가 돌아올 때 stale query가 refetch될 수 있다.

Q. queryKey에 Date.now를 넣으면 안 돼?
A. 보통 안 된다. 매 렌더마다 새로운 key가 되어 계속 요청될 수 있다.

---

## 10.3 Mutation Pending Stuck

### [개념]

Mutation Pending Stuck은 Mutation 요청 후 버튼이 계속 처리 중 상태로 남거나 UI가 복구되지 않는 문제다.

주요 원인은 Promise가 resolve / reject 되지 않거나 mutationFn이 잘못 작성되었거나 Error 처리가 누락된 경우다.

---

### [핵심]

주요 원인:

- mutationFn Promise 미반환
- API 요청이 pending 상태로 멈춤
- catch에서 error를 삼키고 resolve 처리
- 네트워크 timeout 없음
- 버튼 상태를 별도 state로 관리하다 해제 누락
- onError / onSettled 처리 누락
- unhandled promise 문제
- submit handler 중복 blocking

핵심 규칙:

- mutationFn은 Promise를 반환해야 한다.
- 실패는 reject로 전달되어야 한다.
- pending 상태는 mutation state를 우선 사용한다.
- 별도 loading state를 쓰면 finally에서 해제한다.
- Timeout 또는 Error State를 설계한다.
- 실패 후 버튼이 다시 활성화되어야 한다.

---

### [실무]

나쁜 예:

```tsx
const mutation = useMutation({
  mutationFn: (values) => {
    api.post("/reviews", values);
  },
});
```

문제:

- Promise를 return하지 않아 mutation 상태 추적이 부정확해질 수 있다.

개선 예:

```tsx
const mutation = useMutation({
  mutationFn: (values) => {
    return api.post("/reviews", values);
  },
});
```

catch에서 에러 삼키는 예:

```typescript
async function createReview(values) {
  try {
    return await api.post("/reviews", values);
  } catch (error) {
    console.log(error);
  }
}
```

개선 예:

```typescript
async function createReview(values) {
  try {
    return await api.post("/reviews", values);
  } catch (error) {
    console.error(error);
    throw error;
  }
}
```

권장:

- mutationFn에서 API Promise를 return한다.
- error를 catch했다면 다시 throw한다.
- 버튼 Loading은 `mutation.isPending`을 사용한다.
- 별도 state 사용 시 `finally`로 해제한다.
- timeout과 error fallback을 제공한다.

주의:

- catch에서 error를 삼키면 onError가 실행되지 않을 수 있다.
- mutationFn이 resolve되지 않으면 pending이 끝나지 않는다.
- 버튼 disabled 상태가 별도 state와 mutation state로 중복 관리되면 꼬일 수 있다.
- 요청 실패 후 UI 복구를 반드시 확인한다.

---

### [FAQ]

Q. Mutation 버튼이 계속 처리 중이야?
A. mutationFn이 Promise를 반환하는지, 요청이 완료되는지, error를 삼키지 않는지 확인해야 한다.

Q. mutationFn에서 api.post를 return해야 해?
A. 그렇다. Promise를 반환해야 TanStack Query가 pending, success, error 상태를 추적할 수 있다.

Q. catch에서 console.log만 하면 안 돼?
A. error를 다시 throw하지 않으면 onError가 실행되지 않을 수 있다.

Q. 버튼 Loading은 별도 state로 관리해야 해?
A. 보통은 mutation.isPending을 사용하는 것이 더 안전하다.

---

# 11. TanStack Query Checklist

## 11.1 TanStack Query UX Review Checklist

### [개념]

TanStack Query UX Review Checklist는 Query와 Mutation 상태가 Loading, Error, Empty, Success UX와 안정적으로 연결되었는지 검수하는 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] useQuery의 isLoading을 Initial Loading UI와 연결했는가?
- [ ] useQuery의 isError를 Error State와 연결했는가?
- [ ] error 객체를 사용자 메시지로 mapping했는가?
- [ ] refetch를 Retry Button과 연결했는가?
- [ ] 요청 성공 후 데이터 없음은 Empty State로 처리했는가?
- [ ] isLoading과 isFetching을 구분했는가?
- [ ] Refetch 중 기존 데이터를 유지할지 결정했는가?
- [ ] queryKey에 filter / sort / page 조건이 포함되었는가?
- [ ] queryKey와 invalidateQueries key가 일치하는가?
- [ ] enabled 조건이 필요한 Query에 적용되었는가?
- [ ] enabled false 상태의 Idle UI가 설계되었는가?
- [ ] placeholderData 사용 시 stale UI 안내가 있는가?
- [ ] initialData 사용 시 refetch / staleTime 기준이 있는가?
- [ ] useMutation의 isPending을 Button Loading과 연결했는가?
- [ ] Mutation 성공 후 Success Feedback이 있는가?
- [ ] Mutation 성공 후 관련 Query를 invalidate했는가?
- [ ] Mutation Error를 Field / Global / Toast Error로 분류했는가?
- [ ] useInfiniteQuery에서 hasNextPage를 확인하는가?
- [ ] isFetchingNextPage 중 중복 요청을 막는가?
- [ ] Query Loading / Error 접근성을 고려했는가?
- [ ] 중복 요청 가능성을 점검했는가?
- [ ] Pending Stuck 가능성을 점검했는가?
```

---

### [실무]

검수 흐름:

```text
Query 상태 확인
→ Loading / Error / Empty / Success 연결 확인
→ queryKey 확인
→ enabled 조건 확인
→ Mutation 성공 / 실패 처리 확인
→ Invalidation 확인
→ Infinite Query guard 확인
→ Accessibility 확인
→ Troubleshooting 가능성 확인
```

화면별 기준:

| 화면        | TanStack Query UX 기준                            |
| ----------- | ------------------------------------------------- |
| 목록 화면   | isLoading / isError / Empty / isFetching          |
| 상세 화면   | enabled param / Not Found / Error / Success       |
| 검색 화면   | filter queryKey / page reset / Empty              |
| Form 화면   | mutation.isPending / Field Error / Success        |
| 좋아요 버튼 | isPending / cache update / invalidate             |
| 무한 스크롤 | hasNextPage / isFetchingNextPage / bottom loading |
| 인증 화면   | authInitialized + enabled / 401 처리              |

---

### [FAQ]

Q. TanStack Query UX 검수에서 가장 중요한 것은?
A. Query 상태값을 Loading, Error, Empty, Success UI와 정확히 연결하는 것이다.

Q. queryKey 검수 핵심은?
A. queryFn에서 사용하는 조건이 queryKey에 포함되어 있고 invalidate 대상 key와 일치하는지 확인하는 것이다.

Q. Mutation 검수 핵심은?
A. isPending으로 중복 요청을 막고 onSuccess에서 Success Feedback과 Query Invalidation을 처리하는 것이다.

Q. Infinite Query 검수 핵심은?
A. hasNextPage와 isFetchingNextPage를 확인해 중복 요청과 무한 요청을 막는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Error Handling & Loading UX Part05는 무엇을 다뤄?
A. TanStack Query의 useQuery, useMutation, useInfiniteQuery 상태값을 Loading, Error, Empty, Success UX와 연결하는 기준을 다룬다.

Q. TanStack Query UX Rules는 왜 필요해?
A. Query 상태값을 Loading, Error, Empty, Success UI로 안정적으로 연결하기 위해 필요하다.

Q. TanStack Query를 쓰면 Loading / Error 처리가 자동으로 끝나?
A. 아니다. 상태값은 제공되지만 이를 어떤 UI로 보여줄지는 Frontend에서 설계해야 한다.

Q. TanStack Query에서 가장 헷갈리는 상태값은?
A. isLoading과 isFetching, isPending의 역할 구분이 가장 자주 헷갈린다.

Q. useQuery에서 Loading UI는 어떻게 보여줘?
A. isLoading이 true일 때 Initial Loading UI 또는 Skeleton UI를 보여준다.

Q. TanStack Query에서 에러 UI는 어떻게 보여줘?
A. isError가 true일 때 error 객체를 메시지로 변환해 ErrorState를 보여주고 refetch로 재시도 버튼을 연결할 수 있다.

Q. useQuery 성공 후 데이터가 없으면?
A. 요청은 성공했으므로 Empty State를 보여준다.

Q. isFetching일 때 전체 Skeleton을 다시 보여줘야 해?
A. 항상은 아니다. 기존 데이터가 있으면 유지하고 작은 갱신 표시만 보여주는 것이 자연스러운 경우가 많다.

Q. isLoading과 isFetching은 뭐가 달라?
A. isLoading은 초기 데이터가 없는 로딩이고 isFetching은 기존 데이터가 있어도 재조회 중이면 true가 될 수 있다.

Q. isFetching일 때 화면 전체를 로딩으로 바꿔야 해?
A. 보통 아니다. 기존 데이터를 유지하고 작은 갱신 표시를 보여주는 것이 좋다.

Q. isLoading과 isFetching이 동시에 true일 수 있어?
A. 초기 요청 중에는 둘 다 true처럼 동작할 수 있다. UX에서는 초기 로딩과 재조회 로딩을 구분해 처리한다.

Q. Refetch 중 기존 데이터를 지워야 해?
A. 항상 지울 필요는 없다. 기존 데이터를 유지하는 것이 자연스러운 경우가 많다.

Q. Query 실패 시 다시 시도 버튼은 어떻게 연결해?
A. useQuery가 제공하는 refetch 함수를 ErrorState의 onRetry에 연결하면 된다.

Q. 모든 오류에 Retry Button을 제공해도 돼?
A. 아니다. 네트워크나 일시적 서버 오류에는 적합하지만 401, 403, 404는 Login, Forbidden, Not Found UX가 더 적합할 수 있다.

Q. Retry 중 버튼을 disabled 해야 해?
A. 중복 재시도를 줄이기 위해 Retry 중 disabled 처리할 수 있다.

Q. Retry 후 실패하면 어떻게 해?
A. ErrorState를 유지하고 사용자에게 다시 시도하거나 다른 행동을 선택할 수 있게 한다.

Q. queryKey는 왜 중요해?
A. 서버 상태 캐시, 재조회, invalidate 기준이 되기 때문에 Query UX 안정성에 직접 영향을 준다.

Q. 검색 조건도 queryKey에 넣어야 해?
A. 넣어야 한다. 검색어, 필터, 정렬, 페이지 조건이 다르면 다른 서버 상태로 봐야 한다.

Q. queryKey가 틀리면 어떤 문제가 생겨?
A. invalidate가 동작하지 않거나 stale UI, 중복 요청, 잘못된 캐시 사용 문제가 생길 수 있다.

Q. 사용자별 데이터에는 userId를 queryKey에 넣어야 해?
A. 사용자별로 결과가 다르다면 userId 또는 사용자 scope를 queryKey에 포함하는 것이 안전하다.

Q. 필터 조건이 바뀌면 queryKey도 바뀌어야 해?
A. 그렇다. 서버 요청 결과가 달라지는 조건은 queryKey에 포함해야 한다.

Q. 필터 변경 시 page를 왜 초기화해?
A. 이전 page index가 새 조건에서는 유효하지 않아 빈 결과처럼 보일 수 있기 때문이다.

Q. queryKey에 객체를 넣어도 돼?
A. 가능하다. 다만 객체 구조와 값 정규화 기준을 안정적으로 유지해야 한다.

Q. 필터 초기화 버튼은 TanStack Query와 어떻게 연결돼?
A. 필터 상태를 초기화하면 queryKey가 바뀌고 새 조건으로 query가 실행되어야 한다.

Q. enabled 옵션은 언제 써?
A. route param, userId, auth state처럼 필요한 값이 준비된 뒤에만 query를 실행해야 할 때 사용한다.

Q. enabled가 false면 Loading이야?
A. 항상 아니다. 요청이 시작되지 않은 상태이므로 별도 idle 또는 안내 UI를 고려해야 한다.

Q. authInitialized 전에 query를 실행하면 안 돼?
A. 인증 상태가 확정되기 전에 요청하면 불필요한 401이나 redirect flicker가 발생할 수 있다.

Q. route param이 없을 때도 상세 조회를 해야 해?
A. 아니다. 유효한 param이 있을 때만 요청하고, 없으면 Not Found 또는 잘못된 접근 UI를 제공하는 것이 좋다.

Q. Idle State는 뭐야?
A. 아직 요청을 시작하지 않은 상태다.

Q. 검색어 입력 전에는 Loading을 보여줘야 해?
A. 아니다. 검색어 입력 안내 같은 Guide State가 더 적합하다.

Q. enabled false 상태를 Empty State로 봐도 돼?
A. 보통 다르다. 요청을 하지 않은 상태와 요청 성공 후 데이터가 없는 상태는 구분해야 한다.

Q. enabled false 때문에 화면이 계속 비어 있으면?
A. 요청 조건이 충족되지 않았을 때 보여줄 Guide State, Auth Loading, Not Found UI를 설계해야 한다.

Q. placeholderData는 뭐야?
A. 새 Query가 데이터를 가져오는 동안 이전 데이터나 임시 데이터를 화면에 유지할 수 있게 하는 옵션이다.

Q. placeholderData는 언제 좋아?
A. 페이지 변경, 정렬 변경, 가벼운 필터 변경처럼 기존 데이터를 유지해 Flicker를 줄이고 싶을 때 좋다.

Q. placeholderData를 쓰면 Empty State는 어떻게 판단해?
A. 이전 데이터가 남아 있을 수 있으므로 실제 새 요청 완료 여부와 isFetching 상태를 함께 고려해야 한다.

Q. 필터가 완전히 바뀌어도 placeholderData를 써도 돼?
A. 가능하지만 이전 결과가 새 조건 결과처럼 보일 수 있으므로 갱신 중 표시가 필요하다.

Q. initialData는 뭐야?
A. Query가 처음부터 특정 데이터를 가진 상태로 시작하게 하는 옵션이다.

Q. initialData가 있으면 Loading이 안 보여?
A. 보통 초기 데이터가 있으므로 isLoading이 false가 될 수 있다.

Q. initialData와 placeholderData는 달라?
A. 다르다. initialData는 초기 실제 데이터처럼 사용되고 placeholderData는 새 요청 중 임시 표시용으로 사용된다.

Q. initialData가 stale UI를 만들 수 있어?
A. 가능하다. 오래된 데이터를 최신처럼 보여줄 수 있으므로 refetch와 staleTime 기준을 함께 설계해야 한다.

Q. useMutation에서 버튼 Loading은 어떻게 처리해?
A. mutation.isPending으로 버튼을 disabled 처리하고 문구를 “처리 중” 상태로 바꾼다.

Q. mutation 중 버튼을 disabled 해야 해?
A. 권장한다. 중복 요청을 줄이고 사용자가 처리 중임을 알 수 있다.

Q. mutation 성공 후 뭘 해야 해?
A. 관련 query invalidate, 화면 이동, form reset, 성공 메시지 표시 중 필요한 처리를 수행한다.

Q. mutation 실패 후 어떻게 해?
A. Error Message를 보여주고 사용자가 다시 시도할 수 있게 pending 상태를 해제해야 한다.

Q. mutate와 mutateAsync는 뭐가 달라?
A. mutate는 callback 기반이고 mutateAsync는 Promise 기반으로 await할 수 있다.

Q. Form 제출에는 mutate와 mutateAsync 중 뭐가 좋아?
A. 단순 제출은 mutate로 충분하고, 성공 결과를 받아 이동하거나 순차 처리가 필요하면 mutateAsync가 편하다.

Q. mutateAsync 쓸 때 주의할 점은?
A. try/catch를 사용해 실패를 처리하고 중복 성공 메시지가 발생하지 않게 해야 한다.

Q. mutateAsync에서도 isPending을 쓸 수 있어?
A. 사용할 수 있다. mutation 상태는 mutate와 mutateAsync 모두에서 동일하게 활용할 수 있다.

Q. Mutation Error는 어디에 보여줘?
A. Field 오류는 input 근처, Form 전체 오류는 Form Alert, 짧은 액션 실패는 Toast로 보여주는 것이 좋다.

Q. useMutation에서 Validation Error는 어떻게 처리해?
A. 서버 field errors를 Form field errors로 매핑해 input 근처에 표시한다.

Q. 좋아요 실패는 Toast로 보여줘도 돼?
A. 가능하다. 짧은 액션 실패이므로 Toast가 적합한 경우가 많다.

Q. 409 Conflict가 나면 어떻게 해?
A. 최신 서버 상태를 refetch하거나 UI 상태를 서버 상태에 맞게 동기화하는 것이 좋다.

Q. Mutation 성공 후 Query Invalidation은 왜 필요해?
A. 서버 상태가 바뀐 뒤 화면의 캐시 데이터도 최신 상태로 동기화해야 하기 때문이다.

Q. 어떤 Query를 invalidate해야 해?
A. Mutation이 영향을 주는 목록, 상세, 카운트, 요약 데이터를 기준으로 결정한다.

Q. queryKey가 틀리면 어떻게 돼?
A. invalidate가 제대로 동작하지 않아 화면이 오래된 데이터를 계속 보여줄 수 있다.

Q. 성공 Toast는 있는데 목록이 그대로야?
A. Query Invalidation 또는 cache update가 누락되었을 가능성이 높다.

Q. Direct Cache Update는 뭐야?
A. Mutation 성공 후 refetch 없이 Query Cache를 직접 수정해 UI를 즉시 갱신하는 방식이다.

Q. Direct Cache Update와 invalidate 중 뭐가 좋아?
A. 작은 상태 변경은 Direct Cache Update가 빠르고, 복잡한 데이터는 invalidate가 안전하다.

Q. Cache Update할 때 가장 조심할 점은?
A. queryKey와 cache data shape를 정확히 알아야 한다.

Q. Direct Cache Update 후에도 invalidate가 필요해?
A. 최종 서버 상태 동기화가 중요하면 invalidate를 함께 사용할 수 있다.

Q. useInfiniteQuery에서 초기 Loading과 다음 페이지 Loading은 어떻게 달라?
A. 초기 Loading은 isLoading, 다음 페이지 Loading은 isFetchingNextPage로 처리한다.

Q. 더보기 버튼은 언제 숨겨?
A. hasNextPage가 false이면 더보기 버튼을 숨기거나 마지막 안내 메시지를 보여준다.

Q. 더보기 중 중복 요청은 어떻게 막아?
A. isFetchingNextPage 중에는 버튼을 disabled 처리하고 fetchNextPage 호출을 막는다.

Q. Infinite Query에서 Empty State는 언제 보여줘?
A. 초기 요청 성공 후 전체 items가 비어 있을 때 Empty State를 보여준다.

Q. Infinite Scroll에서 fetchNextPage는 언제 호출해?
A. 하단 sentinel이 보이고 hasNextPage가 true이며 isFetchingNextPage가 false일 때 호출한다.

Q. Infinite Scroll에서 API가 여러 번 호출돼?
A. observer 중복 등록, cleanup 누락, guard 조건 누락, StrictMode 영향을 확인해야 한다.

Q. 검색 조건 변경 시 Infinite Query는 어떻게 해?
A. queryKey가 새 조건으로 바뀌어야 하고 cursor 또는 page 상태가 초기화되어야 한다.

Q. Infinite Scroll 실패 시 어떻게 해?
A. 기존 목록은 유지하고 하단에 다시 시도 버튼이나 오류 메시지를 제공한다.

Q. TanStack Query Loading에도 접근성이 필요해?
A. 필요하다. 보조 기술 사용자도 요청 상태를 이해할 수 있어야 한다.

Q. isFetching 메시지를 항상 aria-live로 알려야 해?
A. 항상은 아니다. 너무 자주 발생하면 방해가 될 수 있으므로 필요한 경우만 사용한다.

Q. Mutation 버튼 로딩은 접근성상 어떻게 처리해?
A. 버튼 문구를 “저장 중...”처럼 변경하고 disabled 상태를 함께 사용할 수 있다.

Q. Query ErrorState에는 role alert가 필요해?
A. 중요한 오류 메시지는 role alert를 고려할 수 있다. 다만 과도하게 남발하지 않는다.

Q. Retry Button은 접근성상 어떻게 구현해?
A. 실제 button 요소를 사용하고 명확한 label을 제공하는 것이 좋다.

Q. 데이터가 바뀌었는데 화면이 그대로야?
A. queryKey, invalidate queryKey, onSuccess, staleTime, enabled 조건을 확인해야 한다.

Q. 필터를 바꿨는데 API가 다시 호출되지 않아?
A. 필터 값이 queryKey에 포함되어 있는지 확인해야 한다.

Q. invalidateQueries를 했는데 화면이 안 바뀌어?
A. invalidate한 queryKey가 실제 useQuery의 queryKey와 일치하는지 확인해야 한다.

Q. TanStack Query API가 두 번 호출돼?
A. StrictMode, retry 옵션, refetchOnWindowFocus, queryKey 변경, 수동 fetch 중복을 확인해야 한다.

Q. useQuery를 쓰면서 useEffect fetch도 같이 써도 돼?
A. 권장하지 않는다. 같은 데이터를 두 방식으로 가져오면 중복 요청과 상태 불일치가 생긴다.

Q. refetchOnWindowFocus 때문에 요청이 다시 나갈 수 있어?
A. 그렇다. 창 포커스가 돌아올 때 stale query가 refetch될 수 있다.

Q. Mutation 버튼이 계속 처리 중이야?
A. mutationFn이 Promise를 반환하는지, 요청이 완료되는지, error를 삼키지 않는지 확인해야 한다.

Q. mutationFn에서 api.post를 return해야 해?
A. 그렇다. Promise를 반환해야 TanStack Query가 pending, success, error 상태를 추적할 수 있다.

Q. catch에서 console.log만 하면 안 돼?
A. error를 다시 throw하지 않으면 onError가 실행되지 않을 수 있다.

Q. 버튼 Loading은 별도 state로 관리해야 해?
A. 보통은 mutation.isPending을 사용하는 것이 더 안전하다.

Q. TanStack Query UX 검수에서 가장 중요한 것은?
A. Query 상태값을 Loading, Error, Empty, Success UI와 정확히 연결하는 것이다.
