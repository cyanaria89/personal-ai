# Error Handling & Loading UX Part02 - Loading UX Rules

---

# 1. Loading UX Overview

## 1.1 Loading UX Purpose

### [개념]

Loading UX는 API 요청, 화면 전환, 사용자 액션 처리 중에 사용자가 현재 상태를 이해할 수 있도록 제공하는 대기 상태 UI 기준이다.

Loading UX는 단순히 Spinner를 보여주는 것이 아니라 요청 종류, 데이터 존재 여부, 사용자 액션 종류에 따라 적절한 Loading State를 선택하는 것이다.

---

### [핵심]

Loading UX 주요 대상:

- Initial Loading
- Refetch Loading
- Submit Loading
- Pagination Loading
- Infinite Scroll Loading
- Skeleton UI
- Spinner
- Disabled State
- Loading Message
- Flicker Prevention
- Infinite Loading Prevention

핵심 규칙:

- Loading State와 Empty State를 혼동하지 않는다.
- Initial Loading과 Refetch Loading을 구분한다.
- Submit Loading과 Page Loading을 구분한다.
- 기존 데이터가 있는 Refetch에서는 전체 화면을 덮지 않는다.
- 사용자 액션 처리 중에는 중복 요청을 방지한다.
- Loading UI는 끝날 수 있어야 한다.
- Loading 실패 시 Error State로 전환 가능해야 한다.
- Spinner만 오래 보여주지 않고 필요한 메시지를 제공한다.

---

### [실무]

2026 실무 기준에서 Loading UX는 요청 흐름과 UI 상태를 연결하는 기준이다.

```text
Request Start
→ Loading Type 판단
→ Loading UI 표시
→ Success / Error / Empty 전환
→ Loading 종료 보장
```

Loading UX 선택 기준:

| 상황                    | 권장 Loading UX                         |
| ----------------------- | --------------------------------------- |
| 초기 페이지 데이터 조회 | Page Loading / Skeleton                 |
| 카드 목록 초기 조회     | Skeleton UI                             |
| 상세 페이지 초기 조회   | Detail Skeleton / Page Loading          |
| 기존 데이터 재조회      | 작은 Spinner / 갱신 Text                |
| Form 제출               | Disabled Button / Button Loading        |
| 더보기 요청             | 하단 Spinner / Load More Button Loading |
| 무한 스크롤 다음 페이지 | 하단 Loading Indicator                  |
| 인증 상태 복원          | Auth Loading / Route Guard Loading      |

---

### [FAQ]

Q. Loading UX는 Spinner만 보여주면 끝이야?
A. 아니다. 요청 종류와 화면 상황에 따라 Skeleton, Button Loading, Refetch Indicator, Page Loading을 선택해야 한다.

Q. Loading UX에서 가장 중요한 기준은?
A. Loading, Error, Empty, Success 상태를 구분하고 요청 완료 또는 실패 시 Loading을 종료하는 것이다.

Q. Loading State와 Empty State는 왜 구분해야 해?
A. Loading은 요청 중이고 Empty는 요청 성공 후 데이터가 없는 상태라 사용자에게 주는 의미가 다르기 때문이다.

---

# 2. Initial Loading Rules

## 2.1 Page Initial Loading

### [개념]

Page Initial Loading은 사용자가 페이지에 처음 진입했을 때 필요한 데이터를 불러오는 상태다.

초기 로딩은 빈 화면을 방지하고 사용자가 화면이 정상적으로 동작 중임을 알 수 있게 한다.

---

### [핵심]

Page Initial Loading 사용 상황:

- Page Mount Fetch
- List Page Initial Fetch
- Detail Page Fetch
- Dashboard Initial Fetch
- Profile Fetch
- Route Param Fetch
- Protected Page Data Fetch

핵심 규칙:

- 페이지 진입 직후 필요한 요청에는 Loading UI를 제공한다.
- 요청 완료 전 Empty State를 먼저 보여주지 않는다.
- Error State로 전환 가능한 구조를 만든다.
- Loading이 끝나지 않는 무한 로딩을 방지한다.
- 핵심 Layout은 유지하고 Content 영역만 Loading 처리할 수 있다.
- 너무 짧은 Loading은 Flicker 방지를 고려한다.

---

### [실무]

기본 예:

```jsx
function PageLoading() {
  return (
    <section aria-busy="true">
      <p>데이터를 불러오는 중입니다.</p>
    </section>
  );
}
```

페이지 초기 로딩 예:

```tsx
function FestivalListPage() {
  const { data, isLoading, isError, error } = useQuery({
    queryKey: ["festivals"],
    queryFn: getFestivals,
  });

  if (isLoading) {
    return <PageLoading />;
  }

  if (isError) {
    return <ErrorState message="축제 목록을 불러오지 못했습니다." />;
  }

  if (!data || data.length === 0) {
    return <EmptyState title="축제 정보가 없습니다." />;
  }

  return <FestivalList festivals={data} />;
}
```

권장:

- 초기 요청 중에는 Loading State를 우선 렌더링한다.
- 응답 실패 시 Error State를 제공한다.
- 응답 성공 후 데이터가 없을 때만 Empty State를 제공한다.
- 페이지 전체 Loading과 콘텐츠 영역 Loading을 상황에 맞게 선택한다.

주의:

- `data.length === 0`을 `isLoading`보다 먼저 검사하지 않는다.
- 초기 상태를 빈 배열로 두었다면 요청 완료 여부를 별도로 판단한다.
- 빈 화면만 보여주는 구조는 피한다.

---

### [FAQ]

Q. Page Initial Loading은 언제 필요해?
A. 페이지 진입 직후 필요한 데이터를 불러올 때 필요하다.

Q. 페이지 처음 들어갔을 때 빈 화면이 보여도 돼?
A. 권장하지 않는다. 요청 중이면 Loading UI를 보여주는 것이 좋다.

Q. 초기 데이터가 빈 배열이면 바로 Empty State를 보여줘도 돼?
A. 아니다. 요청 완료 전인지 요청 완료 후인지 구분해야 한다.

Q. Page Initial Loading에서 Error State도 같이 설계해야 해?
A. 그렇다. 요청 실패 시 Loading에서 Error State로 전환되어야 한다.

---

## 2.2 Detail Page Loading

### [개념]

Detail Page Loading은 특정 리소스의 상세 정보를 조회할 때 표시하는 Loading State다.

상세 페이지는 데이터가 없을 때 일반 Empty State보다 Resource Not Found UI와 연결되는 경우가 많다.

---

### [핵심]

Detail Page Loading 사용 상황:

- Festival Detail Fetch
- User Profile Detail Fetch
- Post Detail Fetch
- Review Detail Fetch
- Order Detail Fetch
- Route Param Based Resource Fetch

핵심 규칙:

- 상세 페이지는 `id` 또는 route param 기반으로 조회한다.
- 요청 중에는 Detail Loading 또는 Detail Skeleton을 보여준다.
- API 404는 Resource Not Found UI로 처리한다.
- API 실패는 Error State로 처리한다.
- 데이터가 없을 때 목록 Empty State와 혼동하지 않는다.

---

### [실무]

상세 페이지 예:

```tsx
function FestivalDetailPage({ festivalId }) {
  const { data, isLoading, isError, error, refetch } = useQuery({
    queryKey: ["festival", festivalId],
    queryFn: () => getFestivalDetail(festivalId),
    enabled: Boolean(festivalId),
  });

  if (isLoading) {
    return <FestivalDetailSkeleton />;
  }

  if (isError) {
    return (
      <ErrorState
        message="축제 상세 정보를 불러오지 못했습니다."
        onRetry={refetch}
      />
    );
  }

  if (!data) {
    return (
      <NotFoundState
        title="축제 정보를 찾을 수 없습니다."
        actionText="목록으로 이동"
      />
    );
  }

  return <FestivalDetail festival={data} />;
}
```

권장:

- 상세 화면 구조가 명확하면 Skeleton UI를 사용한다.
- `enabled` 조건으로 잘못된 param 요청을 방지한다.
- 404 Not Found와 500 Server Error를 구분한다.
- 상세 리소스 없음은 목록 Empty와 다른 UI로 처리한다.

주의:

- 잘못된 ID로 조회한 결과를 단순 Empty State로 처리하지 않는다.
- API 404와 Route 404를 혼동하지 않는다.
- `festival.title` 접근 전에 `festival` 존재 여부를 확인한다.

---

### [FAQ]

Q. 상세 페이지 Loading은 목록 Loading과 달라?
A. 다르다. 상세 페이지는 특정 리소스 조회이므로 데이터 없음이 Resource Not Found로 이어질 수 있다.

Q. 상세 페이지 데이터가 없으면 Empty State야?
A. 일반 목록 Empty보다는 Resource Not Found UI가 더 적합한 경우가 많다.

Q. 상세 페이지에는 Skeleton이 좋아?
A. 콘텐츠 구조가 명확하면 Detail Skeleton이 적합하다.

Q. route param이 없을 때도 요청해야 해?
A. 아니다. `enabled` 조건 등으로 유효한 param이 있을 때만 요청하는 것이 좋다.

---

# 3. Refetch Loading Rules

## 3.1 Refetch Loading Basics

### [개념]

Refetch Loading은 이미 화면에 데이터가 있는 상태에서 최신 데이터를 다시 가져오는 Loading State다.

Refetch Loading은 Initial Loading과 다르게 기존 데이터를 유지하면서 갱신 중임을 작게 표시하는 경우가 많다.

---

### [핵심]

Refetch Loading 사용 상황:

- Manual Refresh
- Window Focus Refetch
- Background Refetch
- Filter Change
- Sort Change
- Stale Data Update
- Pull To Refresh
- Query Invalidation 후 재조회

핵심 규칙:

- 기존 데이터가 있으면 전체 화면 Loading으로 덮지 않는다.
- 기존 콘텐츠를 유지하면서 갱신 표시를 제공한다.
- `isLoading`과 `isFetching`을 구분한다.
- Refetch 실패 시 기존 데이터 유지 여부를 결정한다.
- 사용자가 입력 중인 화면을 방해하지 않는다.
- Stale UI와 Fresh UI 표시 기준을 정한다.

---

### [실무]

TanStack Query 기준:

```tsx
const { data, isLoading, isFetching, isError, error, refetch } = useQuery({
  queryKey: ["festivals", params],
  queryFn: () => getFestivals(params),
});
```

상태 연결:

```text
isLoading true
→ 초기 데이터 없음
→ Initial Loading UI

isFetching true + data exists
→ 기존 데이터 있음
→ Refetch Loading Indicator
```

예:

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
    return (
      <ErrorState
        message="축제 목록을 불러오지 못했습니다."
        onRetry={refetch}
      />
    );
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

권장:

- `isFetching` 중에도 기존 목록을 유지한다.
- 상단 또는 버튼 주변에 작은 갱신 표시를 둔다.
- 사용자가 클릭한 Refresh Button에 Loading을 표시할 수 있다.
- Refetch 실패 시 Toast 또는 Inline Message로 최신화 실패를 알릴 수 있다.

주의:

- Refetch마다 전체 Skeleton으로 덮으면 화면이 불안정해진다.
- 기존 데이터를 매번 지우면 Flicker가 발생할 수 있다.
- `isFetching`을 `isLoading`처럼 사용하지 않는다.

---

### [FAQ]

Q. Refetch Loading은 뭐야?
A. 이미 데이터가 있는 상태에서 최신 데이터를 다시 가져오는 Loading State다.

Q. isLoading과 isFetching은 뭐가 달라?
A. isLoading은 초기 데이터가 없는 로딩이고 isFetching은 기존 데이터가 있어도 재조회 중이면 true가 될 수 있다.

Q. Refetch 중 기존 데이터를 지워야 해?
A. 항상 지울 필요는 없다. 기존 데이터를 유지하면서 갱신 표시를 보여주는 것이 자연스러운 경우가 많다.

Q. Refetch 실패 시 기존 데이터를 계속 보여줘도 돼?
A. 가능하다. 다만 최신화 실패 메시지나 재시도 액션을 제공할 수 있다.

---

## 3.2 Filter Change Loading

### [개념]

Filter Change Loading은 검색 조건, 필터, 정렬, 페이지 조건이 변경되어 데이터를 다시 조회할 때 발생하는 Loading State다.

Filter Change는 Refetch처럼 기존 데이터를 유지할 수도 있고, 조건이 크게 바뀌면 새로운 Loading UI를 보여줄 수도 있다.

---

### [핵심]

Filter Change Loading 사용 상황:

- Keyword Search
- Category Filter
- Region Filter
- Date Range Filter
- Sort Change
- Tab Change
- Query Param Change

핵심 규칙:

- 조건 변경 범위에 따라 기존 데이터 유지 여부를 결정한다.
- 완전히 다른 검색 조건이면 Skeleton 또는 Loading State를 사용할 수 있다.
- 기존 데이터가 새 조건의 결과처럼 보이지 않게 주의한다.
- 검색 입력 중에는 Debounce를 고려한다.
- 필터 변경 실패 시 이전 결과 유지 여부를 결정한다.
- 요청 중 중복 필터 요청을 줄인다.

---

### [실무]

선택 기준:

```text
작은 갱신 / 같은 목록 최신화
→ 기존 데이터 유지 + isFetching 표시

완전히 다른 검색 조건
→ 목록 영역 Loading / Skeleton

검색어 입력 중
→ Debounce + 최소 Loading 표시
```

예:

```tsx
function FestivalSearchPage({ filters }) {
  const { data, isLoading, isFetching } = useQuery({
    queryKey: ["festival-search", filters],
    queryFn: () => searchFestivals(filters),
    placeholderData: (previousData) => previousData,
  });

  if (isLoading) {
    return <FestivalListSkeleton />;
  }

  return (
    <>
      {isFetching && <p role="status">검색 결과를 갱신 중입니다.</p>}
      <FestivalList festivals={data ?? []} />
    </>
  );
}
```

권장:

- 필터 조건은 queryKey에 안정적으로 포함한다.
- 입력 검색은 Debounce 후 요청한다.
- 조건 변경 중 기존 결과를 유지할지 명확히 정한다.
- 새 조건으로 검색 중임을 사용자에게 표시한다.

주의:

- 이전 조건의 결과가 새 조건의 결과처럼 보이면 UX 혼란이 생긴다.
- queryKey 객체가 매 렌더마다 불안정하면 중복 요청이 발생할 수 있다.
- 필터 변경 시 page index 또는 cursor 초기화를 고려한다.

---

### [FAQ]

Q. 필터 변경 시 기존 데이터를 유지해도 돼?
A. 가능하다. 다만 기존 결과가 새 조건 결과처럼 오해되지 않도록 갱신 표시를 제공해야 한다.

Q. 검색 조건이 완전히 바뀌면 Skeleton을 써도 돼?
A. 가능하다. 완전히 다른 데이터 조회라면 목록 영역 Loading이나 Skeleton이 적합할 수 있다.

Q. 검색 입력마다 요청해도 돼?
A. 권장하지 않는다. Debounce를 적용해 불필요한 요청을 줄이는 것이 좋다.

Q. 필터 변경 시 페이지 번호는 유지해?
A. 보통 검색 조건이 바뀌면 page index나 cursor를 초기화하는 것이 안전하다.

---

# 4. Submit Loading Rules

## 4.1 Form Submit Loading

### [개념]

Form Submit Loading은 사용자가 Form을 제출한 뒤 서버 처리가 끝날 때까지 표시하는 Loading State다.

Form Submit Loading은 중복 제출 방지, 처리 중 안내, 실패 후 복구를 포함한다.

---

### [핵심]

Form Submit Loading 사용 상황:

- Login Submit
- Signup Submit
- Profile Update
- Review Create
- Post Create
- Password Reset
- Payment Submit
- File Upload Submit

핵심 규칙:

- 제출 중 Submit Button을 Disabled 처리한다.
- 버튼 문구를 처리 중 상태로 변경한다.
- 실패 시 다시 제출 가능하게 복구한다.
- 성공 후 reset / redirect / refetch 기준을 정한다.
- Field Error와 Global Error를 분리한다.
- Submit Loading과 Page Loading을 분리한다.
- 중요한 요청은 Backend 중복 방지도 필요하다.

---

### [실무]

기본 예:

```jsx
function SubmitButton({ submitting }) {
  return (
    <button type="submit" disabled={submitting}>
      {submitting ? "처리 중..." : "저장"}
    </button>
  );
}
```

useMutation 예:

```tsx
function ReviewForm() {
  const mutation = useMutation({
    mutationFn: createReview,
    onSuccess: () => {
      toast.success("리뷰가 등록되었습니다.");
    },
    onError: (error) => {
      showFormError(getApiErrorMessage(error));
    },
  });

  return (
    <form onSubmit={handleSubmit((values) => mutation.mutate(values))}>
      <button type="submit" disabled={mutation.isPending}>
        {mutation.isPending ? "등록 중..." : "리뷰 등록"}
      </button>
    </form>
  );
}
```

권장:

- `mutation.isPending`으로 중복 제출을 방지한다.
- Button Text를 변경해 처리 중임을 알린다.
- Form 입력값은 실패 후에도 유지한다.
- 서버 Validation Error는 Field Error로 연결한다.
- 로그인 실패 같은 인증 실패는 Global Form Error로 처리한다.

주의:

- Disabled Button만으로 서버 중복 요청을 완전히 막을 수 없다.
- 결제, 삭제, 후원 요청은 서버 측 idempotency 또는 중복 방지가 필요하다.
- 실패했는데 버튼이 계속 disabled 상태면 UX 장애가 된다.

---

### [FAQ]

Q. Form Submit Loading은 왜 필요해?
A. 중복 제출을 방지하고 사용자가 처리 중임을 알 수 있게 하기 위해 필요하다.

Q. 제출 중 버튼을 disabled 해야 해?
A. 권장한다. 중복 제출을 줄이고 사용자가 처리 중임을 이해할 수 있다.

Q. 저장 실패 후 입력값은 지워야 해?
A. 보통 지우지 않는다. 사용자가 오류를 수정할 수 있도록 유지하는 것이 좋다.

Q. Submit Loading과 Page Loading은 같아?
A. 다르다. Submit Loading은 사용자 액션 처리 중이고 Page Loading은 화면 데이터 조회 상태다.

---

## 4.2 Action Button Loading

### [개념]

Action Button Loading은 좋아요, 찜, 삭제, 저장, 팔로우 같은 단일 버튼 액션 처리 중에 표시하는 Loading State다.

Action Button Loading은 버튼 단위로 처리하여 페이지 전체 Loading과 분리하는 것이 좋다.

---

### [핵심]

Action Button Loading 사용 상황:

- Like Button
- Favorite Button
- Follow Button
- Delete Button
- Save Button
- Refresh Button
- Upload Button
- Payment Button

핵심 규칙:

- 버튼 단위 Loading을 사용한다.
- 요청 중 해당 버튼을 Disabled 처리한다.
- 요청 실패 시 이전 상태로 복구한다.
- Optimistic UI 사용 시 Rollback 기준을 둔다.
- 같은 버튼을 여러 번 눌러 중복 요청이 나가지 않게 한다.
- 전체 페이지 Loading으로 버튼 액션을 대체하지 않는다.

---

### [실무]

좋아요 버튼 예:

```tsx
function LikeButton({ liked, onToggle, loading }) {
  return (
    <button type="button" disabled={loading} onClick={onToggle}>
      {loading ? "처리 중..." : liked ? "좋아요 취소" : "좋아요"}
    </button>
  );
}
```

Mutation 예:

```tsx
const likeMutation = useMutation({
  mutationFn: toggleLike,
  onSuccess: () => {
    queryClient.invalidateQueries({
      queryKey: ["festival-detail", festivalId],
    });
  },
  onError: () => {
    toast.error("좋아요 처리에 실패했습니다.");
  },
});
```

권장:

- 버튼별 pending 상태를 분리한다.
- 목록의 여러 아이템에서는 item id별 loading 상태를 관리한다.
- 요청 성공 후 서버 상태와 UI를 동기화한다.
- 실패 시 사용자 메시지를 제공한다.
- 409 Conflict 발생 시 최신 상태를 refetch한다.

주의:

- 리스트 전체 버튼이 동시에 Disabled 되지 않도록 한다.
- Optimistic UI는 실패 rollback을 반드시 고려한다.
- 빠른 연속 클릭으로 상태가 꼬이지 않게 한다.

---

### [FAQ]

Q. 좋아요 버튼 누를 때 페이지 전체 Loading을 보여줘야 해?
A. 아니다. 버튼 단위 Loading으로 처리하는 것이 자연스럽다.

Q. 버튼 중복 클릭은 어떻게 막아?
A. 요청 중 해당 버튼을 disabled 처리하고 서버에서도 중복 요청을 안전하게 처리해야 한다.

Q. 목록에서 특정 아이템 버튼만 Loading 처리할 수 있어?
A. 가능하다. item id별 pending 상태를 관리하면 된다.

Q. Action Button 실패 시 어떻게 해?
A. 오류 메시지를 보여주고 기존 상태로 복구하거나 서버 상태를 다시 조회한다.

---

# 5. Pagination Loading Rules

## 5.1 Page Change Loading

### [개념]

Page Change Loading은 페이지 번호를 변경하거나 다음 페이지 데이터를 조회할 때 발생하는 Loading State다.

Pagination Loading은 기존 목록을 유지할지, 새 페이지 로딩으로 전환할지 기준을 정해야 한다.

---

### [핵심]

Page Change Loading 사용 상황:

- Page Number Click
- Next Page Click
- Previous Page Click
- Page Size Change
- Sort With Pagination
- Filter With Pagination

핵심 규칙:

- 페이지 변경 중 Loading 표시를 제공한다.
- 기존 페이지 데이터를 유지할지 결정한다.
- 새 페이지 요청 실패 시 재시도 액션을 제공한다.
- 페이지 변경 중 중복 클릭을 방지한다.
- 필터 변경 시 page index 초기화를 고려한다.
- Pagination 상태와 검색 조건 상태를 함께 관리한다.

---

### [실무]

예:

```tsx
function PaginatedFestivalList({ page }) {
  const { data, isLoading, isFetching } = useQuery({
    queryKey: ["festivals", page],
    queryFn: () => getFestivals({ page }),
    placeholderData: (previousData) => previousData,
  });

  if (isLoading) {
    return <FestivalListSkeleton />;
  }

  return (
    <>
      {isFetching && <p role="status">페이지를 불러오는 중입니다.</p>}
      <FestivalList festivals={data?.items ?? []} />
      <Pagination disabled={isFetching} currentPage={page} />
    </>
  );
}
```

권장:

- 페이지 이동 중 Pagination Button을 disabled 처리할 수 있다.
- 기존 데이터를 유지하면 화면 안정성이 좋아진다.
- 완전히 다른 페이지라는 느낌이 필요하면 목록 영역 Skeleton을 사용할 수 있다.
- 실패 시 현재 페이지 유지와 Error Message 표시를 고려한다.

주의:

- 페이지 변경 시 이전 페이지 결과가 새 페이지 결과처럼 보이지 않게 한다.
- 검색 조건 변경 시 page를 1로 초기화하지 않으면 빈 결과가 나올 수 있다.
- page, size, sort, filter는 queryKey에 포함되어야 한다.

---

### [FAQ]

Q. 페이지 번호 변경 중 기존 목록을 유지해도 돼?
A. 가능하다. 다만 새 페이지를 불러오는 중임을 표시해야 한다.

Q. 페이지 변경 중 버튼을 disabled 해야 해?
A. 중복 요청을 줄이기 위해 disabled 처리하는 것이 좋다.

Q. 필터 변경 시 현재 페이지를 유지해도 돼?
A. 보통은 1페이지로 초기화하는 것이 안전하다.

Q. Pagination Loading은 Skeleton이 좋아?
A. 상황에 따라 다르다. 기존 데이터를 유지하면 작은 Loading 표시가 자연스럽고, 새 페이지 느낌이 강하면 Skeleton도 가능하다.

---

## 5.2 Load More Button Loading

### [개념]

Load More Button Loading은 더보기 버튼을 눌러 다음 데이터를 추가로 가져올 때 표시하는 Loading State다.

기존 목록은 유지하고 버튼 영역 또는 목록 하단에 Loading을 표시하는 것이 일반적이다.

---

### [핵심]

Load More Loading 사용 상황:

- Load More Button
- Next Cursor Fetch
- More Reviews Fetch
- More Notifications Fetch
- More Chat Messages Fetch
- More Festival List Fetch

핵심 규칙:

- 기존 목록을 유지한다.
- 다음 페이지 요청 중 버튼을 Disabled 처리한다.
- 하단에 Loading Indicator를 표시한다.
- `hasNext`가 false면 더보기 버튼을 숨긴다.
- 실패 시 다시 시도 가능하게 한다.
- 중복 append를 방지한다.

---

### [실무]

Load More Button 예:

```jsx
function LoadMoreButton({ loading, hasNext, onClick }) {
  if (!hasNext) {
    return null;
  }

  return (
    <button type="button" onClick={onClick} disabled={loading}>
      {loading ? "불러오는 중..." : "더보기"}
    </button>
  );
}
```

useInfiniteQuery 예:

```tsx
function ReviewList() {
  const { data, fetchNextPage, hasNextPage, isFetchingNextPage } =
    useInfiniteQuery({
      queryKey: ["reviews"],
      queryFn: fetchReviews,
      getNextPageParam: (lastPage) => lastPage.nextCursor,
    });

  return (
    <>
      <ReviewItems pages={data?.pages ?? []} />
      <LoadMoreButton
        loading={isFetchingNextPage}
        hasNext={Boolean(hasNextPage)}
        onClick={() => fetchNextPage()}
      />
    </>
  );
}
```

권장:

- 기존 목록은 그대로 유지한다.
- Loading 중 더보기 버튼을 비활성화한다.
- 실패 시 같은 버튼으로 재시도할 수 있게 한다.
- 마지막 페이지 도달 시 버튼을 숨기거나 완료 메시지를 제공한다.
- append 데이터 중복 여부를 확인한다.

주의:

- Loading 중 버튼을 여러 번 누르면 중복 페이지가 추가될 수 있다.
- `hasNext` 계산이 틀리면 무한 요청 또는 버튼 미표시 문제가 생긴다.
- cursor 기반 페이지네이션은 nextCursor null 여부를 명확히 처리한다.

---

### [FAQ]

Q. 더보기 버튼을 누를 때 기존 목록을 지워야 해?
A. 아니다. 기존 목록을 유지하고 하단에 다음 데이터를 추가하는 것이 일반적이다.

Q. 더보기 버튼을 여러 번 누르면 중복 요청이 나가?
A. loading 중 disabled 처리를 하지 않으면 중복 요청이 발생할 수 있다.

Q. hasNext가 false면 버튼은 어떻게 해?
A. 더보기 버튼을 숨기거나 더 이상 데이터가 없다는 메시지를 제공할 수 있다.

Q. 더보기 실패 시 어떻게 해?
A. 기존 목록은 유지하고 다시 시도 버튼이나 오류 메시지를 제공한다.

---

# 6. Infinite Scroll Loading Rules

## 6.1 Infinite Scroll Loading Basics

### [개념]

Infinite Scroll Loading은 사용자가 목록 하단에 도달했을 때 다음 데이터를 자동으로 가져오는 Loading State다.

Infinite Scroll은 중복 요청, observer cleanup, hasNext 판단이 중요하다.

---

### [핵심]

Infinite Scroll Loading 사용 상황:

- Feed List
- Notification List
- Chat Message History
- Review List
- Festival List
- Search Result List

핵심 규칙:

- 기존 목록을 유지한다.
- 하단에 Loading Indicator를 표시한다.
- `isFetchingNextPage` 중에는 추가 요청을 막는다.
- `hasNextPage`가 false면 요청하지 않는다.
- Observer cleanup을 처리한다.
- 검색 조건 변경 시 목록과 cursor를 초기화한다.
- 실패 시 재시도 수단을 제공한다.

---

### [실무]

기본 흐름:

```text
List Render
→ Bottom Sentinel Visible
→ hasNextPage 확인
→ isFetchingNextPage false 확인
→ fetchNextPage
→ Append Items
→ Update nextCursor
```

예:

```tsx
function InfiniteFestivalList() {
  const { data, fetchNextPage, hasNextPage, isFetchingNextPage } =
    useInfiniteQuery({
      queryKey: ["festivals"],
      queryFn: fetchFestivals,
      getNextPageParam: (lastPage) => lastPage.nextCursor,
    });

  function handleIntersect() {
    if (!hasNextPage || isFetchingNextPage) {
      return;
    }

    fetchNextPage();
  }

  return (
    <>
      <FestivalItems pages={data?.pages ?? []} />
      {isFetchingNextPage && (
        <p role="status">더 많은 축제를 불러오는 중입니다.</p>
      )}
      <div ref={observerRef} />
    </>
  );
}
```

권장:

- 하단 Sentinel Element를 사용한다.
- observer callback에서 `hasNextPage`와 `isFetchingNextPage`를 확인한다.
- 검색 조건 변경 시 queryKey를 명확히 바꾼다.
- 실패 시 하단에 Retry UI를 제공한다.
- 목록 끝에 도달했을 때 완료 상태를 표시할 수 있다.

주의:

- observer가 중복 등록되면 API가 여러 번 호출될 수 있다.
- StrictMode 개발 환경에서 effect가 두 번 실행될 수 있다.
- hasNextPage 계산 오류는 무한 요청으로 이어진다.
- 너무 빠른 연속 요청은 throttle 또는 guard가 필요할 수 있다.

---

### [FAQ]

Q. 무한 스크롤에서 로딩은 어디에 보여줘?
A. 보통 기존 목록은 유지하고 하단에 다음 데이터를 불러오는 표시를 보여준다.

Q. Infinite Scroll에서 중복 요청은 어떻게 막아?
A. hasNextPage와 isFetchingNextPage를 확인하고 observer cleanup을 처리해야 한다.

Q. hasNextPage가 false면 어떻게 해?
A. 더 이상 요청하지 않고 필요하면 마지막 안내 메시지를 보여준다.

Q. Infinite Scroll 실패 시 어떻게 해?
A. 기존 목록은 유지하고 하단에 다시 시도 버튼이나 오류 메시지를 제공한다.

---

# 7. Skeleton UI Rules

## 7.1 Skeleton UI Basics

### [개념]

Skeleton UI는 실제 콘텐츠가 들어올 자리의 형태를 미리 보여주는 Loading UI다.

콘텐츠 구조가 예측 가능한 목록, 카드, 상세 페이지에서 사용자가 레이아웃을 미리 이해할 수 있게 한다.

---

### [핵심]

Skeleton UI 사용 대상:

- Card List
- Detail Page
- Profile Area
- Table Row
- Image Grid
- Feed Item
- Dashboard Widget
- Content Placeholder

핵심 규칙:

- 실제 콘텐츠 구조와 비슷해야 한다.
- 초기 로딩에서 특히 적합하다.
- 너무 짧은 요청에는 과할 수 있다.
- 장식 요소는 `aria-hidden`을 고려한다.
- 별도 Loading Message를 함께 제공할 수 있다.
- Skeleton Animation 남발을 피한다.

---

### [실무]

카드 Skeleton 예:

```jsx
function FestivalCardSkeleton() {
  return (
    <article aria-hidden="true" className="card-skeleton">
      <div className="image-placeholder" />
      <div className="title-placeholder" />
      <div className="text-placeholder" />
    </article>
  );
}
```

목록 Skeleton 예:

```jsx
function FestivalListSkeleton() {
  return (
    <section aria-busy="true" aria-label="축제 목록을 불러오는 중입니다.">
      {Array.from({ length: 6 }).map((_, index) => (
        <FestivalCardSkeleton key={index} />
      ))}
    </section>
  );
}
```

권장:

- 카드 목록에는 여러 개의 Skeleton Item을 제공한다.
- 상세 페이지에는 제목, 이미지, 본문 영역 형태를 맞춘다.
- 실제 레이아웃과 크기 차이를 줄여 Layout Shift를 줄인다.
- Skeleton은 스크린 리더에 불필요하게 읽히지 않게 한다.

주의:

- 실제 콘텐츠와 전혀 다른 Skeleton은 사용자를 혼란스럽게 한다.
- 과도한 shimmer animation은 피로감을 줄 수 있다.
- 버튼 처리 중 Loading에는 Skeleton보다 Button Loading이 적합하다.

---

### [FAQ]

Q. Skeleton UI는 언제 써?
A. 카드 목록이나 상세 페이지처럼 콘텐츠 구조가 예측 가능할 때 적합하다.

Q. Skeleton이 Spinner보다 항상 좋아?
A. 아니다. 짧은 요청이나 단순 액션에는 Spinner나 Button Loading이 더 적합할 수 있다.

Q. Skeleton은 실제 UI와 비슷해야 해?
A. 그렇다. 실제 콘텐츠 구조와 비슷해야 Layout Shift와 혼란을 줄일 수 있다.

Q. Skeleton은 스크린 리더가 읽어야 해?
A. 대부분 장식 요소로 보고 aria-hidden 처리하거나 별도 Loading Message를 제공하는 것이 좋다.

---

## 7.2 Skeleton Selection Rules

### [개념]

Skeleton Selection Rules는 어떤 화면에서 Skeleton을 사용할지 결정하는 기준이다.

Skeleton은 모든 Loading에 사용하는 것이 아니라 콘텐츠 구조가 예측 가능하고 초기 데이터 조회 시간이 의미 있게 느껴질 때 적합하다.

---

### [핵심]

Skeleton 적합 상황:

- 목록 구조가 명확함
- 카드 구조가 반복됨
- 상세 페이지 레이아웃이 고정됨
- 이미지와 텍스트 영역이 예측 가능함
- 초기 데이터 조회 시간이 체감됨
- Layout Shift를 줄이고 싶음

Skeleton 부적합 상황:

- 버튼 제출 처리
- 짧은 액션 요청
- 구조를 예측하기 어려운 데이터
- 모달 내부 짧은 처리
- 더보기 하단 요청
- 단순 refresh indicator

---

### [실무]

선택 기준:

```text
콘텐츠 레이아웃 명확 + 초기 로딩
→ Skeleton UI

사용자 액션 처리 중
→ Button Loading / Disabled State

기존 데이터 재조회
→ 작은 Spinner / Refresh Text

무한 스크롤 다음 페이지
→ 하단 Spinner

짧은 요청
→ Loading 생략 또는 Button Text 변경
```

비교:

| 상황                  | Skeleton 적합도 | 권장            |
| --------------------- | --------------: | --------------- |
| 카드 목록 초기 로딩   |            높음 | Skeleton        |
| 상세 페이지 초기 로딩 |            높음 | Detail Skeleton |
| 저장 버튼 처리        |            낮음 | Button Loading  |
| 좋아요 처리           |            낮음 | Button Disabled |
| 더보기 요청           |            낮음 | 하단 Spinner    |
| 기존 목록 Refetch     |            낮음 | 작은 갱신 표시  |

---

### [FAQ]

Q. 목록 로딩에는 Skeleton이 좋아 Spinner가 좋아?
A. 카드나 테이블 구조가 명확하면 Skeleton이 좋고 단순한 경우에는 Spinner도 가능하다.

Q. 저장 버튼에는 Skeleton을 써?
A. 아니다. 저장 버튼에는 disabled 상태와 버튼 내부 loading 문구 또는 spinner가 적합하다.

Q. Refetch 중 Skeleton을 다시 보여줘야 해?
A. 기존 데이터가 있으면 전체 Skeleton보다 작은 갱신 표시가 더 자연스러운 경우가 많다.

Q. Skeleton을 너무 많이 쓰면 문제야?
A. 가능하다. 구현 비용과 과도한 animation 부담이 생길 수 있다.

---

# 8. Spinner Rules

## 8.1 Spinner Basics

### [개념]

Spinner는 작업이 진행 중임을 간단히 표시하는 Loading UI다.

Spinner는 짧은 처리, 버튼 내부 로딩, 작은 영역 로딩, 더보기 로딩, 재조회 표시 등에 적합하다.

---

### [핵심]

Spinner 사용 대상:

- Submit Button
- Small Area Loading
- Modal Action
- Refresh Indicator
- Load More Indicator
- Infinite Scroll Bottom Loading
- Unknown Wait Time
- Inline Processing

핵심 규칙:

- 접근성 label을 제공한다.
- Spinner만 오래 보여주지 않는다.
- 필요한 경우 Loading Message를 함께 제공한다.
- 화면 전체를 막을지 부분만 표시할지 결정한다.
- 실패 가능성이 있는 요청에는 Error State가 필요하다.
- 무한 Spinner가 되지 않도록 종료 조건을 보장한다.

---

### [실무]

기본 예:

```jsx
function Spinner({ label = "불러오는 중입니다." }) {
  return (
    <div role="status" aria-live="polite">
      <span className="spinner" aria-hidden="true" />
      <span>{label}</span>
    </div>
  );
}
```

버튼 내부 예:

```jsx
function SaveButton({ loading }) {
  return (
    <button type="submit" disabled={loading}>
      {loading ? "저장 중..." : "저장"}
    </button>
  );
}
```

하단 로딩 예:

```jsx
function BottomLoading() {
  return <div role="status">더 많은 데이터를 불러오는 중입니다.</div>;
}
```

권장:

- Spinner에는 텍스트 또는 `aria-label`을 제공한다.
- 버튼 내부 Spinner는 버튼 문구 변경과 함께 사용한다.
- 긴 작업에는 진행 이유를 설명한다.
- 페이지 전체 Spinner는 꼭 필요한 경우에만 사용한다.

주의:

- Spinner만 오래 표시되면 사용자 불안이 증가한다.
- Loading 종료 실패 시 무한 Spinner가 된다.
- Error fallback 없이 Spinner만 있으면 실패 상황을 알 수 없다.

---

### [FAQ]

Q. Spinner는 언제 써?
A. 버튼 제출, 작은 영역 로딩, 짧은 처리 작업, 더보기 로딩에 적합하다.

Q. Spinner에는 텍스트가 꼭 필요해?
A. 접근성을 위해 진행 상태를 설명하는 텍스트나 aria label을 제공하는 것이 좋다.

Q. Spinner가 계속 돌면 어떻게 해?
A. 요청 완료, 실패, finally 처리, timeout, dependency loop를 확인해야 한다.

Q. 전체 화면 Spinner를 써도 돼?
A. 가능하지만 전체 화면을 막아야 하는 상황인지 검토해야 한다.

---

## 8.2 Spinner vs Skeleton

### [개념]

Spinner와 Skeleton은 모두 Loading UI지만 목적과 적합한 상황이 다르다.

Spinner는 처리 중임을 간단히 보여주고 Skeleton은 콘텐츠 구조를 미리 보여준다.

---

### [핵심]

비교:

| 비교 | Spinner                    | Skeleton         |
| ---- | -------------------------- | ---------------- |
| 목적 | 처리 중 표시               | 콘텐츠 자리 예측 |
| 적합 | 버튼, 작은 영역, 짧은 작업 | 목록, 카드, 상세 |
| 장점 | 구현 간단                  | 레이아웃 안정감  |
| 단점 | 오래 보이면 답답함         | 구현 비용        |
| 예   | 저장 중, 더보기 중         | 카드 목록 로딩   |

핵심 규칙:

- 콘텐츠 레이아웃이 명확한 초기 로딩은 Skeleton을 고려한다.
- 버튼 제출이나 작은 액션에는 Spinner 또는 Button Text가 적합하다.
- 기존 데이터 재조회에는 작은 Spinner가 적합하다.
- 무한 스크롤 다음 페이지에는 하단 Spinner가 적합하다.
- Skeleton과 Spinner를 무분별하게 동시에 사용하지 않는다.

---

### [실무]

선택 Flow:

```text
Loading 발생
→ 콘텐츠 구조가 명확한가?
  → Yes
    → 초기 로딩인가?
      → Yes: Skeleton
      → No: 작은 Spinner / 갱신 표시
  → No
    → 사용자 액션인가?
      → Yes: Button Loading
      → No: Spinner + Message
```

예:

```text
축제 카드 목록 첫 조회
→ FestivalCardSkeleton

리뷰 등록 버튼 클릭
→ Button Disabled + "등록 중..."

더보기 버튼 클릭
→ 하단 Spinner

기존 목록 최신화
→ "최신 정보를 확인 중입니다."
```

---

### [FAQ]

Q. Spinner와 Skeleton 중 뭐가 좋아?
A. 상황에 따라 다르다. 구조가 명확한 초기 로딩은 Skeleton, 짧은 처리나 버튼 액션은 Spinner가 적합하다.

Q. Skeleton이 Spinner보다 항상 사용자 경험이 좋아?
A. 아니다. 요청이 짧거나 구조가 단순하면 Spinner나 Button Loading이 더 적합할 수 있다.

Q. Spinner와 Skeleton을 같이 써도 돼?
A. 가능하지만 중복 표시가 과하면 혼란스럽기 때문에 역할을 분리해야 한다.

Q. 무한 스크롤에는 Skeleton이 좋아?
A. 보통 기존 목록 하단에 Spinner나 Loading Text를 표시하는 것이 더 자연스럽다.

---

# 9. Disabled State Rules

## 9.1 Disabled Button Rules

### [개념]

Disabled State는 요청 처리 중 버튼이나 입력을 비활성화하여 중복 요청과 잘못된 조작을 줄이는 UI 상태다.

Disabled State는 Submit Loading, Action Button Loading, Pagination Loading에서 자주 사용한다.

---

### [핵심]

Disabled State 사용 상황:

- Form Submit 중
- 저장 요청 중
- 삭제 요청 중
- 좋아요 요청 중
- 찜 요청 중
- 결제 요청 중
- 더보기 요청 중
- 페이지 이동 요청 중

핵심 규칙:

- 요청 중 중복 클릭을 방지한다.
- 버튼 문구를 처리 중 상태로 변경한다.
- 실패 후 다시 활성화한다.
- Disabled 이유를 사용자가 이해할 수 있게 한다.
- 보안이나 서버 중복 방지를 Disabled에만 의존하지 않는다.
- 중요한 요청은 Backend idempotency 또는 중복 방지와 함께 처리한다.

---

### [실무]

기본 예:

```jsx
<button type="submit" disabled={isSubmitting}>
  {isSubmitting ? "처리 중..." : "제출"}
</button>
```

삭제 버튼 예:

```jsx
<button type="button" disabled={deleteMutation.isPending}>
  {deleteMutation.isPending ? "삭제 중..." : "삭제"}
</button>
```

Pagination 예:

```jsx
<button type="button" disabled={isFetching || currentPage === 1}>
  이전
</button>
```

권장:

- Disabled와 Loading Text를 함께 사용한다.
- 처리 실패 시 Disabled를 해제한다.
- 위험한 액션은 Confirm Modal과 함께 사용할 수 있다.
- Disabled 버튼만 보이지 않게 하기보다 상태를 설명한다.
- Form 유효성 실패와 요청 처리 중 Disabled를 구분한다.

주의:

- Disabled 버튼은 focus나 접근성 측면에서 주의가 필요하다.
- Disabled만 사용하고 상태 문구가 없으면 이유를 알기 어렵다.
- Frontend Disabled는 네트워크 재전송이나 직접 호출을 막지 못한다.

---

### [FAQ]

Q. 요청 중 버튼을 disabled 해야 해?
A. 권장한다. 중복 요청을 줄이고 사용자가 처리 중임을 이해할 수 있다.

Q. Disabled Button만으로 중복 요청이 완전히 막혀?
A. 아니다. Frontend UX 방지일 뿐이고 중요한 요청은 Backend에서도 안전하게 처리해야 한다.

Q. Disabled 상태에서 버튼 문구도 바꿔야 해?
A. 바꾸는 것이 좋다. 사용자가 왜 클릭할 수 없는지 이해하기 쉽다.

Q. Form validation 실패와 제출 중 disabled는 같아?
A. 다르다. validation 실패는 입력 조건 문제이고 제출 중 disabled는 요청 처리 상태다.

---

# 10. Loading Accessibility Rules

## 10.1 Accessible Loading UI

### [개념]

Loading Accessibility는 스크린 리더와 키보드 사용자도 현재 요청 상태를 이해할 수 있게 하는 기준이다.

Loading UI는 시각적 Spinner나 Skeleton에만 의존하지 않고 텍스트와 ARIA 속성을 함께 고려해야 한다.

---

### [핵심]

사용 속성:

- `aria-busy`
- `role="status"`
- `aria-live="polite"`
- `aria-hidden`
- Accessible Label
- Focus Preservation
- Button Text Change

핵심 규칙:

- Spinner 아이콘에만 의존하지 않는다.
- Loading Message를 제공한다.
- Skeleton 장식 요소는 `aria-hidden`을 고려한다.
- 업데이트 알림은 과도하게 반복하지 않는다.
- 버튼 Loading은 버튼 문구로 상태를 전달한다.
- Loading 중 불필요한 focus 이동을 피한다.

---

### [실무]

접근 가능한 Loading 예:

```jsx
function AccessibleLoading() {
  return (
    <div role="status" aria-live="polite">
      데이터를 불러오는 중입니다.
    </div>
  );
}
```

콘텐츠 영역 예:

```jsx
<section aria-busy={isLoading}>
  {isLoading ? <LoadingState /> : <Content />}
</section>
```

Skeleton 예:

```jsx
<div aria-label="축제 목록을 불러오는 중입니다.">
  <FestivalCardSkeleton aria-hidden="true" />
</div>
```

버튼 예:

```jsx
<button type="submit" disabled={isSubmitting}>
  {isSubmitting ? "저장 중..." : "저장"}
</button>
```

권장:

- 상태 변화가 필요한 영역에는 `role="status"`를 사용한다.
- 중요한 Loading Message는 텍스트로 제공한다.
- 장식용 Spinner에는 `aria-hidden="true"`를 사용할 수 있다.
- Skeleton 자체보다 Loading 상태 메시지를 읽히게 한다.

주의:

- `aria-live`가 너무 자주 변경되면 스크린 리더 사용자에게 방해가 된다.
- Skeleton Item 여러 개가 모두 읽히면 불필요한 정보가 된다.
- Loading 때문에 사용자의 현재 focus를 강제로 빼앗지 않는다.

---

### [FAQ]

Q. Spinner만 보여주면 접근성에 충분해?
A. 아니다. 스크린 리더가 이해할 수 있는 텍스트나 role status를 제공하는 것이 좋다.

Q. Loading Message는 꼭 필요해?
A. 시각적 표시만으로 상태 전달이 어려우므로 텍스트나 접근성 label을 제공하는 것이 좋다.

Q. Skeleton은 스크린 리더가 읽어야 해?
A. 대부분 장식 요소로 보고 aria-hidden 처리하거나 별도 Loading Message를 제공하는 것이 좋다.

Q. Loading 중 focus를 이동해야 해?
A. 대부분 이동하지 않는 것이 좋다. 사용자의 현재 작업 흐름을 방해할 수 있다.

---

# 11. Loading Troubleshooting Rules

## 11.1 Infinite Loading Troubleshooting

### [개념]

Infinite Loading은 Loading UI가 끝나지 않고 계속 표시되는 문제다.

Infinite Loading은 요청 실패 처리 누락, finally 누락, useEffect dependency loop, query enabled 조건 오류에서 자주 발생한다.

---

### [핵심]

주요 원인:

- `finally`에서 loading false 누락
- `catch` 처리 누락
- API Promise Pending
- useEffect Dependency Loop
- 조건부 return 오류
- request never resolves
- auth initialized false 유지
- query enabled 조건 오류
- interceptor에서 Promise 반환 누락
- Error State 전환 누락

핵심 규칙:

- 성공과 실패 모두 Loading을 종료해야 한다.
- 요청 실패 시 Error State로 전환해야 한다.
- useEffect dependency를 확인한다.
- query enabled 조건이 계속 false인지 확인한다.
- Network 요청이 완료되는지 확인한다.
- Auth 초기화 상태가 true로 전환되는지 확인한다.

---

### [실무]

Debug Flow:

```text
Loading 계속 표시
→ Network 요청 완료 여부 확인
→ catch / finally 실행 확인
→ setLoading(false) 확인
→ useEffect dependency 확인
→ 조건부 렌더링 순서 확인
→ auth initialized 확인
→ query enabled 조건 확인
```

나쁜 예:

```jsx
async function loadData() {
  setLoading(true);
  await getData();
  setLoading(false);
}
```

문제:

- `getData()` 실패 시 `setLoading(false)`가 실행되지 않는다.

개선 예:

```jsx
async function loadData() {
  setLoading(true);

  try {
    await getData();
  } catch (error) {
    setError(error);
  } finally {
    setLoading(false);
  }
}
```

TanStack Query 확인:

```tsx
const query = useQuery({
  queryKey: ["profile", userId],
  queryFn: () => getProfile(userId),
  enabled: Boolean(userId),
});
```

확인 항목:

- `userId`가 실제로 존재하는가?
- queryFn이 resolve 또는 reject 되는가?
- Error State를 렌더링하고 있는가?
- Suspense 사용 시 fallback이 끝날 조건이 있는가?

---

### [FAQ]

Q. Loading이 계속 끝나지 않아?
A. finally에서 loading false를 호출하는지, API 요청이 완료되는지, useEffect가 반복 실행되는지 확인해야 한다.

Q. API 실패 후에도 Loading이 계속돼?
A. catch 또는 finally에서 상태를 종료하지 않았거나 Error State 전환이 누락되었을 수 있다.

Q. auth loading이 계속되면?
A. 인증 초기화 로직에서 성공/실패와 관계없이 initialized를 true로 바꾸는지 확인해야 한다.

Q. query enabled가 false면 Loading이 계속돼?
A. 조건에 따라 요청이 시작되지 않을 수 있다. enabled 조건과 초기 상태 렌더링을 함께 확인해야 한다.

---

## 11.2 Flicker Troubleshooting

### [개념]

Flicker는 Loading, Empty, Content, Redirect 화면이 짧게 깜빡이는 문제다.

Flicker는 초기 상태 설계, Empty 판정 시점, 인증 초기화, 기존 데이터 제거에서 자주 발생한다.

---

### [핵심]

주요 원인:

- Auth Initialized 구분 없음
- 초기 data 빈 배열로 Empty 먼저 표시
- loading false 초기값
- query enabled 조건 누락
- redirect 조건이 너무 빨리 실행
- 기존 데이터 제거 후 Refetch
- Suspense / Lazy Loading fallback 과다
- Filter Change 시 이전 데이터 처리 기준 없음

핵심 규칙:

- 요청 완료 전 Empty State를 보여주지 않는다.
- 인증 확인 전 redirect 판단을 하지 않는다.
- 기존 데이터 refetch 시 유지 여부를 결정한다.
- 초기 loading 상태를 신중하게 설정한다.
- PublicOnlyRoute / ProtectedRoute에서 auth initialized를 확인한다.
- 조건부 렌더링 순서를 통일한다.

---

### [실무]

Debug Flow:

```text
Flicker 발생
→ 초기 상태 확인
→ loading / initialized 확인
→ empty 판정 시점 확인
→ redirect 조건 확인
→ 기존 data 유지 여부 확인
→ query enabled 확인
```

나쁜 예:

```tsx
if (!user) {
  return <Navigate to="/login" />;
}
```

문제:

- Auth 확인이 끝나기 전에 `user`가 null이라 로그인 페이지로 잠깐 이동할 수 있다.

개선 예:

```tsx
if (!authInitialized) {
  return <LoadingState message="인증 상태를 확인 중입니다." />;
}

if (!user) {
  return <Navigate to="/login" />;
}
```

Empty Flicker 나쁜 예:

```tsx
if (items.length === 0) {
  return <EmptyState title="결과가 없습니다." />;
}

if (loading) {
  return <LoadingState />;
}
```

개선 예:

```tsx
if (loading) {
  return <LoadingState />;
}

if (items.length === 0) {
  return <EmptyState title="결과가 없습니다." />;
}
```

---

### [FAQ]

Q. Empty State가 잠깐 보였다가 목록이 보여?
A. 요청 완료 전 빈 배열을 Empty로 판정했을 가능성이 있다.

Q. 로그인 페이지가 잠깐 보였다가 메인으로 가?
A. auth initialized 전에 redirect 판단이 실행되었을 수 있다.

Q. Refetch 할 때 화면이 깜빡여?
A. 기존 데이터를 지우고 다시 Loading을 보여주는 구조일 수 있다. 기존 데이터 유지 여부를 검토해야 한다.

Q. Flicker를 줄이려면 어떻게 해?
A. 초기 상태, Loading 판정 순서, Empty 판정 시점, Auth Initialized 상태를 명확히 관리해야 한다.

---

## 11.3 Duplicate Request Troubleshooting

### [개념]

Duplicate Request는 같은 API 요청이 의도보다 여러 번 발생하는 문제다.

Loading UX에서는 중복 요청으로 인해 중복 제출, 중복 append, 잘못된 버튼 상태, 과도한 Loading이 발생할 수 있다.

---

### [핵심]

주요 원인:

- React StrictMode Development Double Effect
- useEffect Dependency 오류
- Button 중복 클릭
- Submit Disabled 없음
- QueryKey 변경 반복
- State Update Loop
- Interceptor 중복 등록
- Infinite Scroll Observer 중복 실행
- Filter 입력마다 즉시 요청
- Pagination 중복 클릭

핵심 규칙:

- 중복 클릭은 Disabled State로 줄인다.
- useEffect dependency를 안정화한다.
- QueryKey에 불안정한 객체를 넣지 않는다.
- interceptor는 앱 초기화 시 한 번만 등록한다.
- observer cleanup을 처리한다.
- 개발 StrictMode 중복과 운영 중복을 구분한다.

---

### [실무]

Debug Flow:

```text
Network 중복 요청 확인
→ Trigger 확인
→ useEffect dependency 확인
→ StrictMode 여부 확인
→ button disabled 확인
→ queryKey 안정성 확인
→ interceptor 중복 등록 확인
→ observer cleanup 확인
```

버튼 중복 방지:

```tsx
<button type="submit" disabled={mutation.isPending}>
  {mutation.isPending ? "처리 중..." : "제출"}
</button>
```

Infinite Scroll guard:

```tsx
function handleIntersect() {
  if (!hasNextPage || isFetchingNextPage) {
    return;
  }

  fetchNextPage();
}
```

useEffect 주의:

```tsx
useEffect(() => {
  loadData();
}, [stableId]);
```

권장:

- 요청 트리거를 명확히 찾는다.
- StrictMode 개발 중복인지 확인한다.
- 운영에서도 중복 발생하면 guard를 추가한다.
- Form Submit은 Enter와 Button Click 모두 고려한다.
- 무한 스크롤은 observer cleanup을 반드시 확인한다.

---

### [FAQ]

Q. API가 두 번 호출돼?
A. useEffect dependency, StrictMode, 버튼 중복 클릭, queryKey 변경, interceptor 중복 등록을 확인해야 한다.

Q. StrictMode 때문에 두 번 호출되는 건 문제야?
A. 개발 환경에서 부작용을 찾기 위한 동작일 수 있다. 다만 실제 중복 요청을 막는 구조는 필요하다.

Q. Submit 요청이 두 번 나가?
A. 버튼 disabled, form submit 중복, Enter 제출, mutation pending 상태를 확인해야 한다.

Q. Infinite Scroll에서 다음 페이지가 여러 번 불러와져?
A. observer 중복 실행, hasNextPage 조건, isFetchingNextPage guard, cleanup 여부를 확인해야 한다.

---

# 12. Loading UX Checklist

## 12.1 Loading UX Review Checklist

### [개념]

Loading UX Review Checklist는 화면의 Loading State가 요청 흐름과 사용자 경험에 맞게 설계되었는지 검수하는 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] Initial Loading State가 존재하는가?
- [ ] Refetch Loading State가 Initial Loading과 구분되는가?
- [ ] Submit Loading State가 Page Loading과 구분되는가?
- [ ] Pagination Loading이 중복 요청을 방지하는가?
- [ ] Infinite Scroll Loading에서 hasNext 조건을 확인하는가?
- [ ] Loading State와 Empty State를 혼동하지 않는가?
- [ ] Loading State와 Error State 전환이 가능한가?
- [ ] Skeleton UI 사용 기준이 적절한가?
- [ ] Spinner 사용 기준이 적절한가?
- [ ] Disabled Button이 중복 제출을 줄이는가?
- [ ] Loading Message 또는 접근성 Label이 존재하는가?
- [ ] 무한 Loading 가능성이 없는가?
- [ ] Flicker 가능성이 없는가?
- [ ] Duplicate Request 가능성이 없는가?
- [ ] 기존 데이터 Refetch 시 유지 여부가 명확한가?
- [ ] 실패 후 다시 시도 가능한 구조인가?
```

---

### [실무]

검수 흐름:

```text
Loading Trigger 확인
→ Loading Type 분류
→ UI Pattern 선택
→ Error / Empty / Success 전환 확인
→ 중복 요청 방지 확인
→ Accessibility 확인
→ Troubleshooting 가능성 확인
```

화면별 기준:

| 화면         | 필수 Loading UX                                 |
| ------------ | ----------------------------------------------- |
| 목록 화면    | Initial Loading, Refetch Loading, Empty 분리    |
| 상세 화면    | Detail Loading, Error, Resource Not Found       |
| Form 화면    | Submit Loading, Field Error, Global Error       |
| 버튼 액션    | Button Loading, Disabled State                  |
| 페이지네이션 | Page Change Loading, 중복 클릭 방지             |
| 무한 스크롤  | Bottom Loading, hasNext guard                   |
| 인증 화면    | Auth Initialized Loading, Redirect Flicker 방지 |

---

### [FAQ]

Q. Loading UX 검수에서 가장 중요한 것은?
A. Loading 종류를 구분하고 Error, Empty, Success로 안전하게 전환되는지 확인하는 것이다.

Q. 목록 화면에서 필요한 Loading UX는?
A. Initial Loading, Refetch Loading, Empty State 분리, Error State 전환이 필요하다.

Q. Form 화면에서 필요한 Loading UX는?
A. Submit Loading, Disabled Button, 실패 후 복구, Field Error와 Global Error 처리가 필요하다.

Q. Infinite Scroll Loading 검수 핵심은?
A. hasNext 조건, isFetchingNextPage guard, observer cleanup, 하단 Loading 표시 여부다.

---

# Retrieval Queries

### [FAQ]

Q. Error Handling & Loading UX Part02는 무엇을 다뤄?
A. Initial Loading, Refetch Loading, Submit Loading, Pagination Loading, Infinite Scroll Loading, Skeleton, Spinner, Disabled State 기준을 다룬다.

Q. Loading UX는 뭐야?
A. API 요청, 화면 전환, 사용자 액션 처리 중 사용자가 현재 상태를 이해할 수 있도록 제공하는 대기 상태 UI 기준이다.

Q. Loading UX는 Spinner만 보여주면 끝이야?
A. 아니다. 요청 종류와 화면 상황에 따라 Skeleton, Button Loading, Refetch Indicator, Page Loading을 선택해야 한다.

Q. Loading State와 Empty State 차이는?
A. Loading State는 요청 중인 상태이고 Empty State는 요청 성공 후 데이터가 없는 상태다.

Q. Initial Loading이 뭐야?
A. 화면이 처음 렌더링될 때 필요한 데이터를 불러오는 상태다.

Q. Page Initial Loading은 언제 필요해?
A. 페이지 진입 직후 필요한 데이터를 불러올 때 필요하다.

Q. 페이지 처음 들어갔을 때 빈 화면이 보여도 돼?
A. 권장하지 않는다. 요청 중이면 Loading UI를 보여주는 것이 좋다.

Q. 초기 데이터가 빈 배열이면 바로 Empty State를 보여줘도 돼?
A. 아니다. 요청 완료 전인지 요청 완료 후인지 구분해야 한다.

Q. Detail Page Loading은 뭐야?
A. 특정 리소스의 상세 정보를 조회할 때 표시하는 Loading State다.

Q. 상세 페이지 데이터가 없으면 Empty State야?
A. 일반 목록 Empty보다는 Resource Not Found UI가 더 적합한 경우가 많다.

Q. 상세 페이지에는 Skeleton이 좋아?
A. 콘텐츠 구조가 명확하면 Detail Skeleton이 적합하다.

Q. Refetch Loading은 뭐야?
A. 이미 데이터가 있는 상태에서 최신 데이터를 다시 가져오는 Loading State다.

Q. isLoading과 isFetching은 뭐가 달라?
A. isLoading은 초기 데이터가 없는 로딩이고 isFetching은 기존 데이터가 있어도 재조회 중이면 true가 될 수 있다.

Q. Refetch 중 기존 데이터를 지워야 해?
A. 항상 지울 필요는 없다. 기존 데이터를 유지하면서 갱신 표시를 보여주는 것이 자연스러운 경우가 많다.

Q. Refetch 실패 시 기존 데이터를 계속 보여줘도 돼?
A. 가능하다. 다만 최신화 실패 메시지나 재시도 액션을 제공할 수 있다.

Q. 필터 변경 시 기존 데이터를 유지해도 돼?
A. 가능하다. 다만 기존 결과가 새 조건 결과처럼 오해되지 않도록 갱신 표시를 제공해야 한다.

Q. 검색 조건이 완전히 바뀌면 Skeleton을 써도 돼?
A. 가능하다. 완전히 다른 데이터 조회라면 목록 영역 Loading이나 Skeleton이 적합할 수 있다.

Q. 검색 입력마다 요청해도 돼?
A. 권장하지 않는다. Debounce를 적용해 불필요한 요청을 줄이는 것이 좋다.

Q. Submit Loading이 뭐야?
A. Form 제출, 저장, 삭제, 좋아요, 찜 같은 사용자 액션 요청이 처리 중인 상태다.

Q. Form Submit Loading은 왜 필요해?
A. 중복 제출을 방지하고 사용자가 처리 중임을 알 수 있게 하기 위해 필요하다.

Q. 제출 중 버튼을 disabled 해야 해?
A. 권장한다. 중복 제출을 줄이고 사용자가 처리 중임을 이해할 수 있다.

Q. 저장 실패 후 입력값은 지워야 해?
A. 보통 지우지 않는다. 사용자가 오류를 수정할 수 있도록 유지하는 것이 좋다.

Q. Submit Loading과 Page Loading은 같아?
A. 다르다. Submit Loading은 사용자 액션 처리 중이고 Page Loading은 화면 데이터 조회 상태다.

Q. 좋아요 버튼 누를 때 페이지 전체 Loading을 보여줘야 해?
A. 아니다. 버튼 단위 Loading으로 처리하는 것이 자연스럽다.

Q. 버튼 중복 클릭은 어떻게 막아?
A. 요청 중 해당 버튼을 disabled 처리하고 서버에서도 중복 요청을 안전하게 처리해야 한다.

Q. 목록에서 특정 아이템 버튼만 Loading 처리할 수 있어?
A. 가능하다. item id별 pending 상태를 관리하면 된다.

Q. Pagination Loading은 뭐야?
A. 페이지 번호 변경이나 다음 페이지 데이터를 조회할 때 발생하는 Loading State다.

Q. 페이지 번호 변경 중 기존 목록을 유지해도 돼?
A. 가능하다. 다만 새 페이지를 불러오는 중임을 표시해야 한다.

Q. 필터 변경 시 현재 페이지를 유지해도 돼?
A. 보통은 1페이지로 초기화하는 것이 안전하다.

Q. 더보기 버튼을 누를 때 기존 목록을 지워야 해?
A. 아니다. 기존 목록을 유지하고 하단에 다음 데이터를 추가하는 것이 일반적이다.

Q. 더보기 버튼을 여러 번 누르면 중복 요청이 나가?
A. loading 중 disabled 처리를 하지 않으면 중복 요청이 발생할 수 있다.

Q. hasNext가 false면 버튼은 어떻게 해?
A. 더보기 버튼을 숨기거나 더 이상 데이터가 없다는 메시지를 제공할 수 있다.

Q. Infinite Scroll Loading은 뭐야?
A. 사용자가 목록 하단에 도달했을 때 다음 데이터를 자동으로 가져오는 Loading State다.

Q. 무한 스크롤에서 로딩은 어디에 보여줘?
A. 보통 기존 목록은 유지하고 하단에 다음 데이터를 불러오는 표시를 보여준다.

Q. Infinite Scroll에서 중복 요청은 어떻게 막아?
A. hasNextPage와 isFetchingNextPage를 확인하고 observer cleanup을 처리해야 한다.

Q. Infinite Scroll 실패 시 어떻게 해?
A. 기존 목록은 유지하고 하단에 다시 시도 버튼이나 오류 메시지를 제공한다.

Q. Skeleton UI는 언제 써?
A. 카드 목록이나 상세 페이지처럼 콘텐츠 구조가 예측 가능할 때 적합하다.

Q. Skeleton이 Spinner보다 항상 좋아?
A. 아니다. 짧은 요청이나 단순 액션에는 Spinner나 Button Loading이 더 적합할 수 있다.

Q. Skeleton은 실제 UI와 비슷해야 해?
A. 그렇다. 실제 콘텐츠 구조와 비슷해야 Layout Shift와 혼란을 줄일 수 있다.

Q. 저장 버튼에는 Skeleton을 써?
A. 아니다. 저장 버튼에는 disabled 상태와 버튼 내부 loading 문구 또는 spinner가 적합하다.

Q. Refetch 중 Skeleton을 다시 보여줘야 해?
A. 기존 데이터가 있으면 전체 Skeleton보다 작은 갱신 표시가 더 자연스러운 경우가 많다.

Q. Spinner는 언제 써?
A. 버튼 제출, 작은 영역 로딩, 짧은 처리 작업, 더보기 로딩에 적합하다.

Q. Spinner에는 텍스트가 꼭 필요해?
A. 접근성을 위해 진행 상태를 설명하는 텍스트나 aria label을 제공하는 것이 좋다.

Q. Spinner가 계속 돌면 어떻게 해?
A. 요청 완료, 실패, finally 처리, timeout, dependency loop를 확인해야 한다.

Q. Spinner와 Skeleton 중 뭐가 좋아?
A. 상황에 따라 다르다. 구조가 명확한 초기 로딩은 Skeleton, 짧은 처리나 버튼 액션은 Spinner가 적합하다.

Q. 무한 스크롤에는 Skeleton이 좋아?
A. 보통 기존 목록 하단에 Spinner나 Loading Text를 표시하는 것이 더 자연스럽다.

Q. Disabled State는 뭐야?
A. 요청 처리 중 버튼이나 입력을 비활성화하여 중복 요청과 잘못된 조작을 줄이는 UI 상태다.

Q. Disabled Button만으로 중복 요청이 완전히 막혀?
A. 아니다. Frontend UX 방지일 뿐이고 중요한 요청은 Backend에서도 안전하게 처리해야 한다.

Q. Disabled 상태에서 버튼 문구도 바꿔야 해?
A. 바꾸는 것이 좋다. 사용자가 왜 클릭할 수 없는지 이해하기 쉽다.

Q. Spinner만 보여주면 접근성에 충분해?
A. 아니다. 스크린 리더가 이해할 수 있는 텍스트나 role status를 제공하는 것이 좋다.

Q. Loading Message는 꼭 필요해?
A. 시각적 표시만으로 상태 전달이 어려우므로 텍스트나 접근성 label을 제공하는 것이 좋다.

Q. Skeleton은 스크린 리더가 읽어야 해?
A. 대부분 장식 요소로 보고 aria-hidden 처리하거나 별도 Loading Message를 제공하는 것이 좋다.

Q. Loading이 계속 끝나지 않아?
A. finally에서 loading false를 호출하는지, API 요청이 완료되는지, useEffect가 반복 실행되는지 확인해야 한다.

Q. API 실패 후에도 Loading이 계속돼?
A. catch 또는 finally에서 상태를 종료하지 않았거나 Error State 전환이 누락되었을 수 있다.

Q. auth loading이 계속되면?
A. 인증 초기화 로직에서 성공/실패와 관계없이 initialized를 true로 바꾸는지 확인해야 한다.

Q. Empty State가 잠깐 보였다가 목록이 보여?
A. 요청 완료 전 빈 배열을 Empty로 판정했을 가능성이 있다.

Q. 로그인 페이지가 잠깐 보였다가 메인으로 가?
A. auth initialized 전에 redirect 판단이 실행되었을 수 있다.

Q. Refetch 할 때 화면이 깜빡여?
A. 기존 데이터를 지우고 다시 Loading을 보여주는 구조일 수 있다. 기존 데이터 유지 여부를 검토해야 한다.

Q. API가 두 번 호출돼?
A. useEffect dependency, StrictMode, 버튼 중복 클릭, queryKey 변경, interceptor 중복 등록을 확인해야 한다.

Q. Submit 요청이 두 번 나가?
A. 버튼 disabled, form submit 중복, Enter 제출, mutation pending 상태를 확인해야 한다.

Q. Infinite Scroll에서 다음 페이지가 여러 번 불러와져?
A. observer 중복 실행, hasNextPage 조건, isFetchingNextPage guard, cleanup 여부를 확인해야 한다.

Q. Loading UX 검수에서 가장 중요한 것은?
A. Loading 종류를 구분하고 Error, Empty, Success로 안전하게 전환되는지 확인하는 것이다.
