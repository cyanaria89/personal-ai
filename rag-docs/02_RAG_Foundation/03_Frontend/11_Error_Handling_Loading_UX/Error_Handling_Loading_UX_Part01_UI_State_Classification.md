# Error Handling & Loading UX Part01 - UI State Classification

---

# 1. UI State Classification

## 1.1 Loading / Error / Empty / Success

### [개념]

UI State Classification은 API 요청 결과와 사용자 액션 결과를 화면 상태로 분류하는 기준이다.

Frontend 화면은 데이터를 요청할 때 보통 아래 네 가지 상태 중 하나로 표현된다.

- Loading State
- Error State
- Empty State
- Success State

이 상태를 분리하지 않으면 사용자는 현재 화면이 로딩 중인지, 실패한 것인지, 데이터가 없는 것인지 구분하기 어렵다.

---

### [핵심]

상태 구분:

| 상태          | 의미                   | 예                       |
| ------------- | ---------------------- | ------------------------ |
| Loading State | 요청 진행 중           | 축제 목록 불러오는 중    |
| Error State   | 요청 실패              | 서버 오류, 네트워크 오류 |
| Empty State   | 요청 성공, 데이터 없음 | 검색 결과 없음           |
| Success State | 요청 성공, 데이터 있음 | 축제 목록 표시           |

핵심 규칙:

- Loading State와 Empty State를 혼동하지 않는다.
- Error State와 Empty State를 혼동하지 않는다.
- 요청 전 상태와 요청 완료 후 상태를 구분한다.
- 초기 배열이 빈 배열이라는 이유만으로 Empty State를 바로 보여주지 않는다.
- 요청 실패는 Error State로 처리한다.
- 요청 성공 후 데이터가 없을 때만 Empty State로 처리한다.
- 요청 성공 후 데이터가 있으면 Success State로 처리한다.
- 조건부 렌더링 순서를 통일한다.

---

### [실무]

2026 실무 기준에서 API 기반 화면은 최소한 아래 상태를 구분해야 한다.

```text
Page Render
→ Request Start
→ Loading State
→ Request Success
  → Data Empty
    → Empty State
  → Data Exists
    → Success State
→ Request Failed
  → Error State
```

기본 렌더링 예:

```jsx
function FestivalListPage() {
  if (loading) {
    return <LoadingState message="축제 정보를 불러오는 중입니다." />;
  }

  if (error) {
    return <ErrorState message="축제 정보를 불러오지 못했습니다." />;
  }

  if (festivals.length === 0) {
    return <EmptyState message="검색 결과가 없습니다." />;
  }

  return <FestivalList festivals={festivals} />;
}
```

권장 조건부 렌더링 순서:

```text
1. Loading 확인
2. Error 확인
3. Empty 확인
4. Success 렌더링
```

주의:

- `festivals.length === 0`만 먼저 검사하면 요청 중에도 Empty State가 보일 수 있다.
- API 실패를 빈 배열로 변환하면 Error State가 사라질 수 있다.
- Error State 없이 `console.log(error)`만 남기면 사용자는 실패 원인을 알 수 없다.
- Loading State 없이 빈 화면을 보여주면 사용자는 화면이 멈춘 것으로 오해할 수 있다.

---

### [FAQ]

Q. Loading State와 Empty State 차이는?
A. Loading State는 요청이 진행 중인 상태이고 Empty State는 요청이 성공했지만 표시할 데이터가 없는 상태다.

Q. Error State와 Empty State 차이는?
A. Error State는 요청 실패이고 Empty State는 요청 성공 후 데이터가 없는 상태다.

Q. 초기 배열이 빈 배열이면 바로 Empty State를 보여줘도 돼?
A. 아니다. 요청 전인지 요청 완료 후인지 구분해야 한다.

Q. 검색 결과가 없으면 Error State야?
A. 아니다. API 요청이 성공했고 결과만 없다면 Empty State다.

Q. 서버 요청이 실패했는데 빈 배열을 보여줘도 돼?
A. 권장하지 않는다. 실패 상태는 Error State로 분리해야 한다.

---

# 2. Loading State Rules

## 2.1 Initial Loading

### [개념]

Initial Loading은 화면이 처음 렌더링될 때 필요한 데이터를 불러오는 상태다.

초기 로딩은 사용자가 빈 화면을 오류로 오해하지 않도록 명확한 Loading UI를 제공해야 한다.

---

### [핵심]

Initial Loading 사용 상황:

- Page Mount Data Fetch
- Detail Page Fetch
- List Page Initial Fetch
- User Profile Fetch
- Auth Restore
- Route Param Based Fetch
- Initial Query Loading

핵심 규칙:

- 화면 진입 직후 필요한 데이터 요청에는 Loading State를 제공한다.
- 초기 데이터가 없다는 이유로 Empty State를 먼저 보여주지 않는다.
- 인증 초기화 Loading과 페이지 데이터 Loading을 구분한다.
- 긴 로딩에는 사용자 메시지를 제공한다.
- 무한 로딩 방지를 위해 Error State를 함께 설계한다.

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

Initial Loading 처리 예:

```jsx
function FestivalDetailPage({ festivalId }) {
  const { data, loading, error } = useFestivalDetail(festivalId);

  if (loading) {
    return <PageLoading />;
  }

  if (error) {
    return <ErrorState message="축제 상세 정보를 불러오지 못했습니다." />;
  }

  if (!data) {
    return <EmptyState message="축제 정보를 찾을 수 없습니다." />;
  }

  return <FestivalDetail festival={data} />;
}
```

권장:

- 페이지 전체를 막을지 콘텐츠 영역만 로딩 처리할지 결정한다.
- Skeleton UI 또는 Loading Message를 상황에 맞게 사용한다.
- 너무 짧은 로딩에는 Flicker 방지를 고려한다.
- 요청 실패 시 Error State로 빠질 수 있어야 한다.
- `finally` 또는 Query 상태값으로 Loading 종료를 보장한다.

---

### [FAQ]

Q. 페이지 처음 들어갔을 때 빈 화면이 보여도 돼?
A. 권장하지 않는다. 요청 중이면 Loading State를 보여주는 것이 좋다.

Q. Initial Loading과 Empty State는 어떻게 구분해?
A. 요청이 완료되기 전이면 Loading State이고 요청 성공 후 데이터가 없으면 Empty State다.

Q. 인증 확인 중 Loading과 데이터 Loading은 같아?
A. 다르다. 인증 확인은 Auth Loading이고 화면 데이터 조회는 Page Loading이다.

Q. Initial Loading에서 Skeleton을 써도 돼?
A. 가능하다. 목록, 카드, 상세 화면처럼 레이아웃이 예측 가능하면 Skeleton이 적합하다.

---

## 2.2 Refetch Loading

### [개념]

Refetch Loading은 이미 데이터가 있는 상태에서 최신 데이터를 다시 가져오는 상태다.

Initial Loading과 달리 기존 데이터를 유지하면서 작은 갱신 표시를 보여주는 경우가 많다.

---

### [핵심]

Refetch Loading 사용 상황:

- Manual Refresh
- Window Focus Refetch
- Filter Change
- Background Refetch
- Stale Data Update
- Pull To Refresh

핵심 규칙:

- 기존 데이터가 있으면 전체 화면 Loading으로 덮지 않는다.
- 재조회 중임을 작은 Spinner나 Text로 표시할 수 있다.
- 사용자 입력 중인 값을 방해하지 않는다.
- 재조회 실패 시 기존 데이터를 유지할지 결정한다.
- Initial Loading과 Refetch Loading을 구분한다.

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
→ 작은 갱신 표시
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
    return <EmptyState message="축제 정보가 없습니다." />;
  }

  return (
    <>
      {isFetching && <p>최신 정보를 확인 중입니다.</p>}
      <FestivalList festivals={data} />
    </>
  );
}
```

권장:

- `isLoading`은 초기 로딩 UI에 사용한다.
- `isFetching`은 재조회 표시로 사용한다.
- 기존 데이터가 있을 때는 전체 Skeleton으로 덮지 않는다.
- 검색 조건이 완전히 바뀌는 경우 Skeleton 또는 목록 초기화를 검토한다.

---

### [FAQ]

Q. isLoading과 isFetching은 뭐가 달라?
A. isLoading은 초기 데이터가 없는 로딩이고 isFetching은 데이터 재조회 중에도 true가 될 수 있다.

Q. Refetch 중 기존 데이터를 지워야 해?
A. 항상 지울 필요는 없다. 기존 데이터를 유지하면서 갱신 표시를 보여주는 것이 자연스러운 경우가 많다.

Q. 재조회 실패 시 기존 데이터를 계속 보여줘도 돼?
A. 가능하다. 다만 최신화 실패 메시지나 재시도 액션을 제공할 수 있다.

Q. 필터 변경 시에도 기존 데이터를 유지해도 돼?
A. 상황에 따라 다르다. 완전히 다른 조건이면 Skeleton이나 새로운 Loading State가 더 적합할 수 있다.

---

## 2.3 Submit Loading

### [개념]

Submit Loading은 Form 제출, 저장, 삭제, 좋아요, 찜 같은 사용자 액션 요청이 처리 중인 상태다.

Submit Loading은 중복 요청을 방지하고 사용자가 처리 중임을 알 수 있게 한다.

---

### [핵심]

Submit Loading 사용 상황:

- Login Submit
- Signup Submit
- Review Create
- Profile Update
- Delete Request
- Like Request
- Favorite Request
- Payment Request
- Upload Request

핵심 규칙:

- 제출 중 버튼을 Disabled 처리한다.
- 버튼 문구를 처리 중 상태로 변경한다.
- 실패 시 다시 제출 가능하게 복구한다.
- 성공 후 화면 상태 갱신 기준을 정한다.
- 중요한 요청은 Backend 중복 방지도 필요하다.
- Submit Loading과 Page Loading을 분리한다.

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

Mutation 예:

```tsx
function ReviewSubmitButton() {
  const mutation = useMutation({
    mutationFn: createReview,
    onSuccess: () => {
      toast.success("리뷰가 등록되었습니다.");
    },
    onError: () => {
      toast.error("리뷰 등록에 실패했습니다.");
    },
  });

  return (
    <button type="button" disabled={mutation.isPending}>
      {mutation.isPending ? "등록 중..." : "리뷰 등록"}
    </button>
  );
}
```

권장:

- `isPending` 또는 `submitting` 상태로 버튼을 비활성화한다.
- 버튼 문구로 처리 중임을 알려준다.
- 성공 시 관련 Query를 invalidate 또는 refetch한다.
- 실패 시 Error Message를 보여주고 버튼을 다시 활성화한다.
- 삭제, 결제, 후원 같은 요청은 서버에서도 중복 요청을 방지한다.

주의:

- Disabled Button만으로 보안이나 중복 처리가 완전하지 않다.
- 사용자가 같은 요청을 여러 번 보내도 서버 상태가 안전해야 한다.
- Page Loading으로 Submit Loading을 대체하지 않는다.

---

### [FAQ]

Q. 제출 중 버튼을 disabled 해야 해?
A. 권장한다. 중복 제출을 줄이고 사용자가 처리 중임을 이해할 수 있다.

Q. Submit Loading과 Initial Loading은 달라?
A. 다르다. Submit Loading은 사용자 액션 처리 중이고 Initial Loading은 화면 데이터 초기 조회 중이다.

Q. 버튼 disabled만 하면 중복 요청이 완전히 막혀?
A. 아니다. Frontend UX 방지일 뿐이고 중요한 요청은 Backend에서도 중복 방지가 필요하다.

Q. 저장 실패 후 버튼은 어떻게 해야 해?
A. 다시 제출할 수 있도록 loading을 해제하고 오류 메시지를 보여줘야 한다.

---

# 3. Error State Rules

## 3.1 API Error State

### [개념]

API Error State는 서버 요청이 실패했을 때 사용자에게 실패 상황을 알려주는 상태다.

API Error는 Empty State와 다르며, 사용자가 이해할 수 있는 메시지와 필요한 경우 Retry Action을 제공해야 한다.

---

### [핵심]

API Error 처리 대상:

- Network Error
- Timeout
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 409 Conflict
- 422 Validation Error
- 500 Server Error

핵심 규칙:

- API 요청 실패는 Error State로 분리한다.
- 서버 내부 오류 메시지를 그대로 노출하지 않는다.
- 사용자 메시지와 개발자 로그를 분리한다.
- 재시도 가능한 오류에는 Retry Button을 제공할 수 있다.
- 인증 오류와 권한 오류를 구분한다.
- Validation Error는 Field Error와 Global Error로 분리한다.

---

### [실무]

공통 Error State 예:

```tsx
function ErrorState({ message, onRetry }) {
  return (
    <section role="alert">
      <p>{message}</p>
      {onRetry && (
        <button type="button" onClick={onRetry}>
          다시 시도
        </button>
      )}
    </section>
  );
}
```

API Error Mapping 예:

```typescript
function getApiErrorMessage(error: unknown): string {
  if (axios.isAxiosError(error)) {
    const status = error.response?.status;

    if (status === 400) {
      return "요청 값을 확인해 주세요.";
    }

    if (status === 401) {
      return "로그인이 필요합니다.";
    }

    if (status === 403) {
      return "접근 권한이 없습니다.";
    }

    if (status === 404) {
      return "요청한 데이터를 찾을 수 없습니다.";
    }

    if (status === 500) {
      return "서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.";
    }
  }

  return "요청 처리 중 문제가 발생했습니다.";
}
```

권장:

- 공통 Error Message Mapping 함수를 만든다.
- 화면별 세부 메시지는 override 가능하게 둔다.
- 개발자 로그에는 status, endpoint, error code 정도를 남긴다.
- 사용자에게 stack trace, SQL Error, token 값을 노출하지 않는다.
- Retry Button은 실제 refetch 또는 재요청 함수와 연결한다.

---

### [FAQ]

Q. API 에러는 어떻게 보여줘?
A. 사용자가 이해할 수 있는 메시지와 필요한 경우 다시 시도 버튼을 제공한다.

Q. 서버 에러 원문을 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 정보가 포함될 수 있으므로 사용자용 메시지로 변환해야 한다.

Q. Error State와 Empty State를 같은 UI로 처리해도 돼?
A. 권장하지 않는다. 실패와 데이터 없음은 사용자 행동이 다르기 때문에 분리해야 한다.

Q. Retry Button은 언제 제공해?
A. 네트워크 오류, 일시적 서버 오류, 조회 실패처럼 재시도 가능성이 있는 오류에 제공한다.

---

## 3.2 Network Error vs Server Error

### [개념]

Network Error는 서버 응답 자체를 받지 못한 상태이고 Server Error는 서버가 응답했지만 내부 오류가 발생한 상태다.

Frontend는 Network Error와 500 Server Error를 구분해야 한다.

---

### [핵심]

Network Error 원인:

- Internet Disconnected
- Server Down
- DNS Problem
- CORS Failure
- Timeout
- Wrong BaseURL
- Mixed Content
- Request Blocked

Server Error 원인:

- Backend Exception
- Database Error
- Internal Logic Error
- External API Failure
- Unexpected Server Failure

핵심 규칙:

- Network Error는 연결 확인 메시지를 제공한다.
- Server Error는 일반적인 서버 오류 메시지를 제공한다.
- CORS Error는 브라우저에서 Network Error처럼 보일 수 있다.
- Postman 성공과 Browser 성공은 다를 수 있다.
- Network 탭으로 실제 status code 존재 여부를 확인한다.

---

### [실무]

UX 기준:

```text
Network Error
→ "네트워크 연결을 확인해 주세요."
→ Retry Button

500 Server Error
→ "서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요."
→ Retry Button or 문의 안내
```

Debug Flow:

```text
API Error 발생
→ Network 탭 확인
→ 요청 발생 여부 확인
→ status code 존재 여부 확인
→ response body 확인
→ CORS message 확인
→ baseURL 확인
→ server 실행 여부 확인
```

Axios 기준:

```typescript
function isNetworkError(error: unknown): boolean {
  return axios.isAxiosError(error) && !error.response;
}
```

주의:

- `error.response`가 없으면 서버 응답을 받지 못한 상태일 수 있다.
- CORS 실패는 서버가 정상이어도 브라우저에서 요청이 차단될 수 있다.
- 500 Error는 응답이 존재하므로 Network Error와 다르게 처리한다.

---

### [FAQ]

Q. Network Error와 500 에러는 달라?
A. 다르다. Network Error는 응답 자체를 받지 못한 경우이고 500은 서버가 응답한 내부 오류다.

Q. Postman에서는 되는데 브라우저에서는 Network Error가 나?
A. CORS, Mixed Content, 브라우저 보안 정책 문제일 수 있다.

Q. Network Error에는 어떤 메시지를 보여줘?
A. 네트워크 연결을 확인해 달라는 메시지와 다시 시도 버튼을 제공하는 것이 좋다.

Q. 500 Error 상세 내용을 보여줘도 돼?
A. 운영 환경에서는 내부 정보를 노출하지 않고 일반적인 서버 오류 메시지를 보여준다.

---

# 4. Empty State Rules

## 4.1 Empty State Basics

### [개념]

Empty State는 요청이 성공했지만 표시할 데이터가 없는 상태다.

Empty State는 실패가 아니며, 사용자에게 현재 상태와 다음 행동을 안내해야 한다.

---

### [핵심]

Empty State 사용 상황:

- Search Result Empty
- Review List Empty
- Notification Empty
- Favorite List Empty
- Chat Room Empty
- Visit History Empty
- Uploaded File Empty
- First Use Empty

핵심 규칙:

- 요청 성공 후 데이터가 없을 때만 Empty State를 보여준다.
- Error State와 혼동하지 않는다.
- 데이터 없음의 이유를 설명한다.
- 사용자가 할 수 있는 다음 행동을 제공한다.
- 검색 결과 없음과 첫 사용 Empty를 구분한다.
- 초기 로딩 중에는 Empty State를 보여주지 않는다.

---

### [실무]

공통 Empty State 예:

```jsx
function EmptyState({ title, description, action }) {
  return (
    <section>
      <h2>{title}</h2>
      {description && <p>{description}</p>}
      {action}
    </section>
  );
}
```

검색 결과 없음 예:

```jsx
<EmptyState
  title="검색 결과가 없습니다."
  description="검색어를 바꾸거나 필터를 초기화해 보세요."
  action={<button type="button">필터 초기화</button>}
/>
```

첫 사용 Empty 예:

```jsx
<EmptyState
  title="아직 찜한 축제가 없습니다."
  description="마음에 드는 축제를 찾아 찜해 보세요."
  action={<Link to="/festivals">축제 둘러보기</Link>}
/>
```

권장:

- 검색 결과 없음에는 필터 초기화 액션을 제공할 수 있다.
- 첫 사용 Empty에는 핵심 기능으로 이동하는 CTA를 제공할 수 있다.
- 부정적인 문구보다 다음 행동 중심 문구를 사용한다.
- 사용자를 탓하는 문구를 피한다.
- Empty State는 성공 응답 이후에만 표시한다.

---

### [FAQ]

Q. Empty State에는 뭘 보여줘야 해?
A. 데이터가 없다는 메시지, 이유, 사용자가 할 수 있는 다음 행동을 보여주는 것이 좋다.

Q. 검색 결과 없음은 Error State야?
A. 아니다. 요청이 성공했다면 Empty State다.

Q. 첫 사용 Empty State와 검색 결과 없음은 달라?
A. 다르다. 첫 사용 Empty는 아직 데이터가 없는 상태이고 검색 결과 없음은 조건에 맞는 결과가 없는 상태다.

Q. Empty State에 버튼을 넣어도 돼?
A. 좋다. 사용자가 다음 행동을 쉽게 할 수 있다.

---

# 5. Success State Rules

## 5.1 Success State Basics

### [개념]

Success State는 요청이 성공했고 표시할 데이터나 완료 결과가 있는 상태다.

Success State에서는 데이터 표시, 화면 갱신, 성공 피드백을 통해 사용자가 요청 결과를 이해할 수 있어야 한다.

---

### [핵심]

Success State 사용 상황:

- List Data Display
- Detail Data Display
- Create Success
- Update Success
- Delete Success
- Login Success
- Signup Success
- Favorite Success
- Upload Success

핵심 규칙:

- 요청 성공 후 데이터가 있으면 Success State를 렌더링한다.
- 사용자 액션 성공 후 필요한 피드백을 제공한다.
- 성공 후 관련 데이터를 갱신한다.
- 화면 변화만으로 충분한 경우 Toast를 남발하지 않는다.
- 중요한 액션에는 성공 메시지를 제공할 수 있다.
- 삭제 성공 후 목록에서 제거하거나 refetch한다.

---

### [실무]

Success Feedback 방식:

| 방식                | 사용 상황         | 예                         |
| ------------------- | ----------------- | -------------------------- |
| Toast               | 짧은 성공 알림    | 저장 완료                  |
| Inline Message      | 특정 영역 결과    | 프로필 저장 완료           |
| Redirect            | 생성 후 상세 이동 | 게시글 작성 후 상세 페이지 |
| Modal Close         | 수정 완료         | 프로필 수정 모달 닫기      |
| Data Refetch        | 목록 최신화       | 리뷰 등록 후 목록 갱신     |
| Button State Change | 찜/좋아요         | 선택 상태 변경             |

Mutation 성공 예:

```tsx
const mutation = useMutation({
  mutationFn: createReview,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ["reviews"] });
    toast.success("리뷰가 등록되었습니다.");
  },
});
```

권장:

- 성공 후 사용자에게 결과를 인지시킨다.
- 관련 Query를 invalidate 또는 refetch한다.
- Form 성공 후 reset 여부를 결정한다.
- 성공 후 redirect 기준을 명확히 한다.
- Toast는 중요한 결과 중심으로 사용한다.

주의:

- 성공했는데 화면이 변하지 않으면 사용자는 실패로 오해할 수 있다.
- 성공 Toast만 띄우고 데이터 갱신을 하지 않으면 stale UI가 남을 수 있다.
- 성공 후 redirect가 너무 빠르면 사용자가 결과를 인지하지 못할 수 있다.

---

### [FAQ]

Q. Success State는 뭐야?
A. 요청이 성공하고 표시할 데이터나 완료 결과가 있는 상태다.

Q. 성공할 때마다 Toast를 띄워야 해?
A. 아니다. 화면 변화만으로 충분한 경우도 있고 중요한 액션에는 Toast가 도움이 된다.

Q. 저장 성공 후 바로 이동해도 돼?
A. 가능하다. 다만 사용자가 성공 여부를 이해할 수 있도록 메시지나 자연스러운 화면 전환을 제공하는 것이 좋다.

Q. 성공 후 데이터를 다시 불러와야 해?
A. 관련 화면이 서버 상태에 의존한다면 refetch 또는 query invalidate를 고려해야 한다.

---

# 6. Status Modeling Rules

## 6.1 Boolean State vs Status Union

### [개념]

Status Modeling은 loading, error, success 같은 UI 상태를 명확한 상태값으로 모델링하는 방식이다.

상태가 많아질수록 여러 boolean 값을 따로 관리하면 충돌이 발생할 수 있다.

---

### [핵심]

Boolean 상태 예:

- `loading`
- `error`
- `success`
- `submitting`
- `empty`

Status Union 후보:

- `idle`
- `loading`
- `success`
- `error`
- `empty`
- `submitting`
- `refetching`

핵심 규칙:

- 단순 화면은 boolean 상태로 충분할 수 있다.
- 상태가 충돌하면 Status Union을 사용한다.
- `loading=true`와 `error=true`가 동시에 되는 구조를 피한다.
- idle 상태와 loading 상태를 구분한다.
- submit status와 page loading status를 분리한다.
- 상태 전환 흐름을 명확히 한다.

---

### [실무]

TypeScript 예:

```typescript
type RequestStatus = "idle" | "loading" | "success" | "error";

type RequestState<T> = {
  status: RequestStatus;
  data: T | null;
  errorMessage: string;
};
```

렌더링 예:

```tsx
if (state.status === "loading") {
  return <LoadingState />;
}

if (state.status === "error") {
  return <ErrorState message={state.errorMessage} />;
}

if (state.status === "success" && state.data.length === 0) {
  return <EmptyState message="데이터가 없습니다." />;
}
```

Reducer 기반 예:

```typescript
type State<T> =
  | { status: "idle"; data: null; error: null }
  | { status: "loading"; data: null; error: null }
  | { status: "success"; data: T; error: null }
  | { status: "error"; data: null; error: string };
```

권장:

- API 요청 상태가 복잡하면 status 기반으로 관리한다.
- `empty`를 status로 둘지 success 내부 조건으로 둘지 팀 기준을 정한다.
- Form Submit 상태는 별도 `isSubmitting` 또는 mutation 상태로 관리한다.
- TanStack Query 사용 시 Query 상태값을 우선 활용한다.

---

### [FAQ]

Q. loading, error boolean을 따로 두면 안 돼?
A. 가능하다. 하지만 상태가 많아져 서로 충돌하면 status 문자열이나 reducer로 모델링하는 것이 더 안전하다.

Q. idle 상태는 왜 필요해?
A. 아직 요청을 시작하지 않은 상태와 요청 중인 상태를 구분하기 위해 필요하다.

Q. Empty State를 status로 만들어야 해?
A. 팀 기준에 따라 다르다. 요청 성공 후 데이터 없음 조건으로 처리해도 되고 별도 empty status로 모델링해도 된다.

Q. Submit Loading도 같은 status에 넣어?
A. 보통 Page Loading과 Submit Loading은 분리해서 관리하는 것이 안전하다.

---

# 7. Conditional Rendering Rules

## 7.1 Safe Rendering Order

### [개념]

Safe Rendering Order는 Loading, Error, Empty, Success 상태를 안전한 순서로 렌더링하는 기준이다.

조건부 렌더링 순서가 잘못되면 Empty Flicker, Blank Screen, Error Message Missing 문제가 발생할 수 있다.

---

### [핵심]

권장 순서:

```text
1. Loading State
2. Error State
3. Empty State
4. Success State
```

핵심 규칙:

- Loading 판정을 Empty 판정보다 먼저 한다.
- Error 판정을 Empty 판정보다 먼저 한다.
- Empty 판정은 요청 성공 이후에만 한다.
- Success 렌더링 전에 data null 여부를 확인한다.
- `map` 실행 전 배열 여부를 확인한다.
- 잘못된 응답 구조에 대비한다.

---

### [실무]

나쁜 예:

```jsx
function FestivalListPage({ festivals, loading }) {
  if (festivals.length === 0) {
    return <EmptyState message="검색 결과가 없습니다." />;
  }

  if (loading) {
    return <LoadingState />;
  }

  return <FestivalList festivals={festivals} />;
}
```

문제:

- 요청 중에도 `festivals`가 빈 배열이면 Empty State가 먼저 표시된다.
- Empty Flicker가 발생할 수 있다.

개선 예:

```jsx
function FestivalListPage({ festivals, loading, error }) {
  if (loading) {
    return <LoadingState />;
  }

  if (error) {
    return <ErrorState message="축제 정보를 불러오지 못했습니다." />;
  }

  if (!festivals || festivals.length === 0) {
    return <EmptyState message="검색 결과가 없습니다." />;
  }

  return <FestivalList festivals={festivals} />;
}
```

TanStack Query 예:

```tsx
if (isLoading) {
  return <LoadingState />;
}

if (isError) {
  return <ErrorState message={getApiErrorMessage(error)} />;
}

if (!data || data.length === 0) {
  return <EmptyState message="데이터가 없습니다." />;
}

return <Content data={data} />;
```

---

### [FAQ]

Q. 조건부 렌더링에서 Empty를 먼저 검사하면 안 돼?
A. 요청 중 빈 배열을 Empty로 오판할 수 있으므로 Loading과 Error를 먼저 검사하는 것이 안전하다.

Q. Blank Screen은 왜 생겨?
A. Loading, Error, Empty 처리가 누락되었거나 렌더링 오류가 발생했거나 data 구조를 잘못 가정했을 수 있다.

Q. map on undefined 오류는 어떻게 막아?
A. data가 배열인지 확인하거나 기본값을 안전하게 설정해야 한다.

Q. Error State 없이 Success만 렌더링해도 돼?
A. 권장하지 않는다. 요청 실패 시 사용자에게 실패 상황을 알려야 한다.

---

# 8. Common Mistakes

## 8.1 UI State Classification Common Mistakes

### [개념]

UI State Classification Common Mistakes는 Loading, Error, Empty, Success 상태를 잘못 구분해서 발생하는 대표적인 UX 문제다.

---

### [핵심]

자주 발생하는 실수:

- Loading State 없이 빈 화면 표시
- Error State 없이 `console.log`만 출력
- Empty State와 Error State 혼동
- 초기 빈 배열을 바로 Empty State로 표시
- 요청 실패를 빈 배열로 대체
- Submit Loading 없이 중복 요청 허용
- `finally` 누락으로 무한 Loading 발생
- Error Message Mapping 없이 서버 원문 노출
- Retry Button이 실제 refetch와 연결되지 않음
- `isLoading`과 `isFetching` 혼동
- API 404와 Route 404 혼동
- 401과 403을 같은 UX로 처리
- Field Error를 Toast로만 표시
- Error Boundary가 API Error를 잡는다고 착각
- StrictMode 중복 요청을 운영 버그로 착각

---

### [실무]

문제별 수정 기준:

| 문제                 | 원인                      | 해결                     |
| -------------------- | ------------------------- | ------------------------ |
| Empty가 잠깐 보임    | 요청 완료 전 빈 배열 판정 | Loading 먼저 검사        |
| 화면이 비어 있음     | 상태 UI 누락              | Loading/Error/Empty 추가 |
| 에러가 안 보임       | catch에서 error 저장 누락 | Error State 연결         |
| 버튼 중복 클릭       | Submit Loading 없음       | disabled 처리            |
| 계속 로딩            | finally 누락              | try/catch/finally 사용   |
| 서버 원문 노출       | message mapping 없음      | 사용자 메시지 변환       |
| refetch 중 화면 덮임 | isFetching 오용           | 기존 데이터 유지         |

Debug Flow:

```text
UX 문제 발생
→ 현재 상태값 확인
→ Network 응답 확인
→ Loading 종료 확인
→ Error 저장 확인
→ Empty 판정 시점 확인
→ 조건부 렌더링 순서 확인
→ 사용자 메시지 확인
```

---

### [FAQ]

Q. Error Handling 초보가 가장 많이 하는 실수는?
A. Loading / Error / Empty 상태를 구분하지 않고 빈 화면이나 console.log만 남기는 실수가 많다.

Q. Empty State가 잠깐 보였다가 목록이 보여?
A. 요청 완료 전 빈 배열을 Empty로 판정했을 가능성이 있다.

Q. Loading이 계속 끝나지 않아?
A. finally에서 loading false를 호출하는지, API 요청이 완료되는지, useEffect가 반복 실행되는지 확인해야 한다.

Q. API는 실패했는데 에러 메시지가 안 보여?
A. catch에서 에러를 상태로 저장하는지, Error UI 조건이 맞는지, error mapping 함수가 올바른지 확인해야 한다.

---

# 9. Checklist

## 9.1 UI State Classification Checklist

### [개념]

UI State Classification Checklist는 Frontend 화면에서 Loading, Error, Empty, Success 상태가 안정적으로 분리되었는지 검수하는 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] Loading State가 존재하는가?
- [ ] Error State가 존재하는가?
- [ ] Empty State가 존재하는가?
- [ ] Success State가 존재하는가?
- [ ] Loading State와 Empty State를 구분했는가?
- [ ] Error State와 Empty State를 구분했는가?
- [ ] 요청 완료 전 Empty State가 표시되지 않는가?
- [ ] API 실패를 빈 배열로 숨기지 않는가?
- [ ] 사용자 메시지와 개발자 로그를 분리했는가?
- [ ] Retry 가능한 오류에 Retry Action이 있는가?
- [ ] Submit Loading으로 중복 제출을 방지했는가?
- [ ] Initial Loading과 Refetch Loading을 구분했는가?
- [ ] isLoading과 isFetching을 구분했는가?
- [ ] 조건부 렌더링 순서가 안전한가?
- [ ] map on undefined 가능성이 없는가?
- [ ] Blank Screen 가능성이 없는가?
```

---

### [실무]

검수 흐름:

```text
Component Review
→ State Value Check
→ Conditional Rendering Check
→ Loading UX Check
→ Error UX Check
→ Empty UX Check
→ Success Feedback Check
→ Retry / Refetch Check
→ Accessibility Basic Check
→ Final Review
```

적용 기준:

- 목록 화면은 Loading / Error / Empty / Success 상태를 모두 가진다.
- 상세 화면은 Loading / Error / Not Found / Success 상태를 가진다.
- Form 화면은 Field Error / Global Error / Submit Loading을 가진다.
- Mutation 액션은 Pending / Success / Error 상태를 가진다.
- Refetch 화면은 기존 데이터 유지 여부를 결정한다.

---

### [FAQ]

Q. UI State Classification 검수에서 가장 중요한 것은?
A. Loading, Error, Empty, Success 상태를 혼동하지 않고 요청 흐름에 맞게 분리하는 것이다.

Q. 목록 화면에는 어떤 상태가 필요해?
A. Loading, Error, Empty, Success 상태가 필요하다.

Q. 상세 화면에서 데이터가 없으면 Empty State야?
A. 일반 목록 Empty와 다르다. 상세 리소스가 없으면 Resource Not Found UI로 처리하는 것이 적합하다.

Q. Form 화면에는 어떤 상태가 필요해?
A. Submit Loading, Field Error, Global Error, Success Feedback이 필요하다.

---

# Retrieval Queries

### [FAQ]

Q. Error Handling & Loading UX Part01은 무엇을 다뤄?
A. Loading State, Error State, Empty State, Success State를 구분하는 UI State Classification 기준을 다룬다.

Q. UI State Classification이 뭐야?
A. API 요청 결과와 사용자 액션 결과를 Loading, Error, Empty, Success 같은 화면 상태로 분류하는 기준이다.

Q. Loading State와 Empty State 차이는?
A. Loading State는 요청이 진행 중인 상태이고 Empty State는 요청이 성공했지만 표시할 데이터가 없는 상태다.

Q. Error State와 Empty State 차이는?
A. Error State는 요청 실패이고 Empty State는 요청 성공 후 데이터가 없는 상태다.

Q. Success State는 뭐야?
A. 요청이 성공하고 표시할 데이터나 완료 결과가 있는 상태다.

Q. 초기 배열이 빈 배열이면 바로 Empty State를 보여줘도 돼?
A. 아니다. 요청 전인지 요청 완료 후인지 구분해야 하며 요청 중에는 Loading State를 보여줘야 한다.

Q. 검색 결과가 없으면 Error State야?
A. 아니다. 요청이 성공했고 결과만 없다면 Empty State다.

Q. API 요청 실패를 빈 배열로 처리해도 돼?
A. 권장하지 않는다. 실패 상태가 사라져 사용자가 오류를 알 수 없으므로 Error State로 분리해야 한다.

Q. 조건부 렌더링 순서는 어떻게 잡아야 해?
A. Loading State, Error State, Empty State, Success State 순서로 검사하는 것이 안전하다.

Q. Empty State를 Loading State보다 먼저 검사하면 어떤 문제가 생겨?
A. 요청 중 초기 빈 배열을 Empty로 오판해 Empty Flicker가 발생할 수 있다.

Q. Initial Loading이 뭐야?
A. 화면이 처음 렌더링될 때 필요한 데이터를 불러오는 상태다.

Q. Refetch Loading이 뭐야?
A. 이미 데이터가 있는 상태에서 최신 데이터를 다시 가져오는 상태다.

Q. Submit Loading이 뭐야?
A. Form 제출, 저장, 삭제, 좋아요, 찜 같은 사용자 액션 요청이 처리 중인 상태다.

Q. Submit Loading과 Page Loading은 달라?
A. 다르다. Submit Loading은 사용자 액션 처리 중이고 Page Loading은 화면 데이터 조회 중이다.

Q. 제출 중 버튼을 disabled 해야 해?
A. 권장한다. 중복 제출을 줄이고 사용자가 처리 중임을 이해할 수 있다.

Q. 버튼 disabled만 하면 중복 요청이 완전히 막혀?
A. 아니다. Frontend UX 방지일 뿐이고 중요한 요청은 Backend에서도 중복 방지가 필요하다.

Q. isLoading과 isFetching은 뭐가 달라?
A. isLoading은 초기 데이터가 없는 로딩이고 isFetching은 데이터 재조회 중에도 true가 될 수 있다.

Q. Refetch 중 기존 데이터를 지워야 해?
A. 항상 지울 필요는 없다. 기존 데이터를 유지하면서 작은 갱신 표시를 보여주는 것이 자연스러운 경우가 많다.

Q. API 에러는 어떻게 보여줘?
A. 사용자가 이해할 수 있는 메시지와 필요한 경우 다시 시도 버튼을 제공한다.

Q. 서버 에러 원문을 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 정보가 포함될 수 있으므로 사용자용 메시지로 변환해야 한다.

Q. Network Error와 500 에러는 달라?
A. 다르다. Network Error는 응답 자체를 받지 못한 경우이고 500은 서버가 응답한 내부 오류다.

Q. Postman에서는 되는데 브라우저에서는 Network Error가 나?
A. CORS, Mixed Content, 브라우저 보안 정책 문제일 수 있다.

Q. Empty State에는 뭘 보여줘야 해?
A. 데이터가 없다는 메시지, 이유, 사용자가 할 수 있는 다음 행동을 보여주는 것이 좋다.

Q. 첫 사용 Empty State와 검색 결과 없음은 달라?
A. 다르다. 첫 사용 Empty는 아직 데이터가 없는 상태이고 검색 결과 없음은 조건에 맞는 결과가 없는 상태다.

Q. Success State에서 Toast는 항상 필요해?
A. 아니다. 화면 변화만으로 충분한 경우도 있고 중요한 액션에는 Toast가 도움이 된다.

Q. Status Modeling이 뭐야?
A. loading, error, success 같은 UI 상태를 명확한 상태값으로 모델링하는 방식이다.

Q. loading, error boolean을 따로 두면 안 돼?
A. 가능하다. 하지만 상태가 많아져 서로 충돌하면 status 문자열이나 reducer로 모델링하는 것이 더 안전하다.

Q. idle 상태는 왜 필요해?
A. 아직 요청을 시작하지 않은 상태와 요청 중인 상태를 구분하기 위해 필요하다.

Q. Blank Screen은 왜 생겨?
A. Loading, Error, Empty 처리가 누락되었거나 렌더링 오류가 발생했거나 data 구조를 잘못 가정했을 수 있다.

Q. map on undefined 오류는 어떻게 막아?
A. data가 배열인지 확인하거나 기본값을 안전하게 설정해야 한다.

Q. Empty State가 잠깐 보였다가 목록이 보여?
A. 요청 완료 전 빈 배열을 Empty로 판정했을 가능성이 있다.

Q. Loading이 계속 끝나지 않아?
A. finally에서 loading false를 호출하는지, API 요청이 완료되는지, useEffect가 반복 실행되는지 확인해야 한다.

Q. API는 실패했는데 에러 메시지가 안 보여?
A. catch에서 에러를 상태로 저장하는지, Error UI 조건이 맞는지, error mapping 함수가 올바른지 확인해야 한다.

Q. UI State Classification 검수에서 가장 중요한 것은?
A. Loading, Error, Empty, Success 상태를 혼동하지 않고 요청 흐름에 맞게 분리하는 것이다.
