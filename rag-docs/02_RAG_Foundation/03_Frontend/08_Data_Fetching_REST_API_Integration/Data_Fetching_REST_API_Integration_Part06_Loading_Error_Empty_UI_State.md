# Data Fetching & REST API Integration Part06 - Loading / Error / Empty UI State

---

# 1. API UI State Overview

## 1.1 API UI State 기본 개념

### [개념]

API UI State는 Frontend가 API 요청 생명주기에 따라 화면에 표시해야 하는 상태를 의미한다.

Data Fetching 화면은 단순히 데이터만 표시하는 것이 아니라, 요청 중인지, 실패했는지, 데이터가 없는지, 성공적으로 표시할 데이터가 있는지를 명확하게 구분해야 한다.

기본 상태 구분:

```text
API Request Start
→ Loading State
→ API Success or API Error
→ Empty State or Success State or Error State
→ UI Render
```

---

### [핵심]

API UI State 핵심 키워드:

- Loading State
- Error State
- Empty State
- Success State
- Initial Loading
- Refetch Loading
- Submit Loading
- Button Disabled
- Skeleton UI
- Spinner
- Error Message
- Retry Button
- Empty Message
- Data Render
- Server State
- Response DTO
- Error Mapping

기본 판단 기준:

```text
loading true → Loading UI
error exists → Error UI
request success and data empty → Empty UI
request success and data exists → Success UI
```

---

### [실무]

2026 실무 기준에서 API UI State는 다음 기준으로 분리한다.

- 최초 로딩과 재조회 로딩 구분
- 조회 로딩과 제출 로딩 구분
- Error State와 Empty State 구분
- 사용자 메시지와 개발 로그 구분
- Error 객체 전체를 화면에 노출하지 않음
- Submit 중 Button Disabled 처리
- Retry 가능한 오류에는 Retry UI 제공 가능
- TanStack Query 사용 시 query state를 UI state로 연결
- Manual Fetch 사용 시 `finally`에서 loading 종료

기본 상태 구조:

```typescript
type ApiUiState<T> = {
  data: T | null;
  loading: boolean;
  errorMessage: string;
};
```

기본 렌더링 순서:

```tsx
if (loading) {
  return <p>Loading...</p>;
}

if (errorMessage) {
  return <p role="alert">{errorMessage}</p>;
}

if (!data) {
  return <p>데이터가 없습니다.</p>;
}

return <DataView data={data} />;
```

---

### [FAQ]

Q. API UI State가 뭐야?
A. API 요청 중, 실패, 성공했지만 데이터 없음, 성공 후 데이터 있음 같은 화면 상태를 구분하는 기준이다.

Q. Loading / Error / Empty / Success를 왜 나눠?
A. 요청 중인지, 실패인지, 데이터가 없는 정상 상태인지, 표시할 데이터가 있는지 사용자에게 명확히 보여주기 위해 나눈다.

Q. Empty State와 Error State는 뭐가 달라?
A. Empty State는 요청 성공 후 데이터가 없는 상태이고 Error State는 요청 자체가 실패한 상태다.

Q. API UI State는 어디서 관리해?
A. Component, Custom Hook, TanStack Query Hook에서 관리할 수 있다.

---

# 2. Rendering Priority Rules

## 2.1 상태 렌더링 우선순위

### [개념]

Rendering Priority는 Loading, Error, Empty, Success 상태를 어떤 순서로 화면에 표시할지 결정하는 기준이다.

상태 우선순위가 불명확하면 Loading 중에 Empty가 보이거나, Error가 발생했는데 빈 목록처럼 보이는 문제가 생긴다.

---

### [핵심]

기본 우선순위:

```text
1. Initial Loading
2. Error
3. Empty
4. Success
```

Refetch가 있는 경우:

```text
Initial Loading → 전체 Skeleton
Refetch Loading → 기존 데이터 유지 + 작은 Loading Indicator
Error → 사용자 안전 메시지
Empty → 성공했지만 데이터 없음
Success → 데이터 렌더링
```

주의:

- Loading과 Empty를 동시에 보여주지 않음
- Error와 Empty를 혼동하지 않음
- 최초 로딩 중 data가 비어 있어도 Empty State로 판단하지 않음
- Error 객체 대신 사용자 메시지 표시
- Refetch 중 기존 데이터 유지 가능

---

### [실무]

기본 렌더링 예:

```tsx
function ApiStateView({ loading, errorMessage, items }) {
  if (loading) {
    return <ListSkeleton />;
  }

  if (errorMessage) {
    return <ErrorState message={errorMessage} />;
  }

  if (items.length === 0) {
    return <EmptyState title="데이터가 없습니다." />;
  }

  return <ItemList items={items} />;
}
```

TanStack Query 기준:

```tsx
if (query.isLoading) {
  return <ListSkeleton />;
}

if (query.isError) {
  return (
    <ErrorState
      message={getApiErrorMessage(query.error)}
      onRetry={() => query.refetch()}
    />
  );
}

if (!query.data || query.data.content.length === 0) {
  return <EmptyState title="검색 결과가 없습니다." />;
}

return (
  <>
    {query.isFetching && <p>새로고침 중...</p>}
    <List items={query.data.content} />
  </>
);
```

---

### [FAQ]

Q. 렌더링 우선순위는 왜 필요해?
A. Loading, Error, Empty, Success 상태가 동시에 섞여 보이는 문제를 막기 위해 필요하다.

Q. 최초 로딩 중 data가 비어 있으면 Empty State야?
A. 아니다. 최초 로딩 중에는 Loading State가 우선이다.

Q. Error와 Empty 중 무엇을 먼저 판단해?
A. 요청 실패가 있으면 Error State를 먼저 처리하고, 요청 성공 후 데이터가 없을 때 Empty State를 처리한다.

Q. Refetch 중에는 화면을 비워야 해?
A. 항상 그렇지 않다. 기존 데이터를 유지하고 작은 로딩 표시만 보여줄 수 있다.

---

# 3. Loading State Rules

## 3.1 Loading State 기본

### [개념]

Loading State는 API 요청이 진행 중임을 사용자에게 알려주는 상태다.

Loading State는 화면이 멈춘 것처럼 보이지 않게 하고, 중복 클릭이나 중복 제출을 방지한다.

---

### [핵심]

Loading State 사용 상황:

- Page Initial Loading
- List Loading
- Detail Loading
- Refetch Loading
- Submit Loading
- Mutation Loading
- Button Loading
- File Upload Loading

Loading UI 유형:

- text loading
- spinner
- skeleton
- button disabled
- inline loading
- overlay loading

주의:

- Loading 시작과 종료를 명확히 처리
- `finally`에서 loading false 처리
- Error 발생 시에도 loading 종료
- 제출 중 버튼 disabled 처리
- 무한 Loading 방지
- 조회 loading과 제출 loading 구분

---

### [실무]

Manual Fetch Loading:

```tsx
function FestivalListPage() {
  const [loading, setLoading] = useState(false);
  const [festivals, setFestivals] = useState<FestivalSummaryResponse[]>([]);
  const [errorMessage, setErrorMessage] = useState("");

  async function loadFestivals() {
    try {
      setLoading(true);
      setErrorMessage("");

      const pageData = await getFestivals({ page: 0, size: 20 });
      setFestivals(pageData.content);
    } catch (error) {
      setErrorMessage(getApiErrorMessage(error));
    } finally {
      setLoading(false);
    }
  }

  if (loading) {
    return <FestivalListSkeleton />;
  }

  return <FestivalList festivals={festivals} />;
}
```

Submit Loading:

```tsx
function ReviewSubmitButton({ submitting }: { submitting: boolean }) {
  return (
    <button type="submit" disabled={submitting}>
      {submitting ? "작성 중..." : "리뷰 작성"}
    </button>
  );
}
```

Flow:

```text
API Request Start
→ loading true
→ Success or Error
→ finally
→ loading false
```

---

### [FAQ]

Q. Loading State는 왜 필요해?
A. API 요청 중 사용자에게 진행 상태를 알려주고 중복 클릭이나 빈 화면 혼란을 줄이기 위해 필요하다.

Q. loading은 언제 false로 바꿔?
A. API 성공이나 실패와 관계없이 요청이 끝나는 `finally`에서 false로 바꾸는 것이 안전하다.

Q. 제출 버튼은 loading 중에 disabled 해야 해?
A. 중복 제출을 막기 위해 submit loading 중에는 버튼을 disabled 처리하는 것이 좋다.

Q. Loading UI는 Spinner와 Skeleton 중 뭐가 좋아?
A. 화면 구조를 미리 보여주고 싶으면 Skeleton, 짧은 작업이나 버튼 내부 상태는 Spinner나 text loading이 적합하다.

---

# 4. Initial Loading vs Refetch Loading

## 4.1 최초 로딩과 재조회 로딩 구분

### [개념]

Initial Loading은 데이터가 아직 없는 상태에서 최초 API 요청 중인 상태다.

Refetch Loading은 기존 데이터가 있는 상태에서 새 데이터를 다시 가져오는 상태다.

두 상태를 구분하면 화면 깜빡임을 줄이고 사용자 경험을 개선할 수 있다.

---

### [핵심]

Initial Loading:

- Page Mount
- No Existing Data
- Skeleton UI 적합
- 전체 화면 Loading 가능

Refetch Loading:

- Existing Data 있음
- 검색 조건 변경
- 새로고침
- background update
- 작은 loading indicator 적합
- 기존 UI 유지 가능

TanStack Query 기준:

- `isLoading`: 최초 로딩
- `isFetching`: fetching 진행 중
- `isRefetching`: 재조회 상태

주의:

- refetch 때 기존 데이터를 무조건 비우지 않음
- 검색 조건이 완전히 바뀌면 목록 초기화 가능
- loading 상태 이름을 명확히 함
- submit loading과 fetch loading 구분

---

### [실무]

상태 구분 Type:

```typescript
type FetchState<T> = {
  data: T | null;
  initialLoading: boolean;
  refetching: boolean;
};
```

TanStack Query 예:

```tsx
const { data, isLoading, isFetching, error } = useQuery({
  queryKey: ["festivals", params],
  queryFn: () => getFestivals(params),
});

if (isLoading) {
  return <FestivalListSkeleton />;
}

return (
  <>
    {isFetching && <p>새로고침 중...</p>}
    <FestivalList festivals={data?.content ?? []} />
  </>
);
```

Flow:

```text
Initial Page Mount
→ isLoading true
→ Skeleton Render
→ Data Loaded
→ List Render
```

```text
Refetch
→ Existing Data 유지 가능
→ isFetching true
→ Small Loading Indicator
→ New Data Render
```

---

### [FAQ]

Q. isLoading과 isFetching은 달라?
A. TanStack Query에서는 최초 로딩과 백그라운드 재조회 상태를 구분할 수 있다.

Q. Refetch 중에는 기존 목록을 지워야 해?
A. 항상 그렇지 않다. 기존 목록을 유지하면서 작은 로딩 표시를 보여줄 수 있다.

Q. Skeleton은 언제 쓰는 게 좋아?
A. 최초 로딩처럼 아직 보여줄 데이터가 없을 때 적합하다.

Q. 검색 조건이 바뀌면 기존 데이터를 유지해도 돼?
A. UX 기준에 따라 가능하지만 이전 조건의 데이터와 새 조건의 데이터가 혼동되지 않도록 주의한다.

---

# 5. Error State Rules

## 5.1 Error State 기본

### [개념]

Error State는 API 요청 실패나 응답 처리 실패를 사용자에게 알려주는 상태다.

Frontend는 Error 객체를 그대로 보여주지 않고 사용자에게 안전한 메시지로 변환해야 한다.

---

### [핵심]

Error State 처리 대상:

- Network Error
- Timeout Error
- CORS Error
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 409 Conflict
- 415 Unsupported Media Type
- 422 Validation Error
- 500 Server Error
- Response Shape Mismatch

Error UI 요소:

- Error Message
- Retry Button
- Login Redirect Button
- Forbidden Notice
- Not Found UI
- Field Error
- Global Error

주의:

- Error 객체 전체 노출 금지
- 서버 원문 메시지 직접 노출 주의
- 사용자 메시지와 개발 로그 구분
- 401 / 403 구분
- Validation Error와 General Error 구분
- Error State와 Empty State 구분
- catch에서 에러를 삼키지 않음

---

### [실무]

Error Mapper:

```typescript
export function getApiErrorMessage(error: unknown): string {
  if (axios.isAxiosError(error)) {
    const status = error.response?.status;

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

    if (!error.response) {
      return "네트워크 연결을 확인해 주세요.";
    }
  }

  return "요청 처리 중 문제가 발생했습니다.";
}
```

Error UI:

```tsx
function ErrorState({
  message,
  onRetry,
}: {
  message: string;
  onRetry?: () => void;
}) {
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

API 호출부:

```typescript
async function loadFestivals() {
  try {
    setLoading(true);
    setErrorMessage("");

    const pageData = await getFestivals(params);
    setFestivals(pageData.content);
  } catch (error) {
    setErrorMessage(getApiErrorMessage(error));
  } finally {
    setLoading(false);
  }
}
```

---

### [FAQ]

Q. Error State는 언제 보여줘?
A. API 요청 실패, 인증 실패, 권한 없음, 서버 오류, 네트워크 오류처럼 요청이 정상 완료되지 않았을 때 보여준다.

Q. API 에러 메시지는 그대로 보여줘도 돼?
A. 민감한 정보가 포함될 수 있으므로 사용자에게 보여줄 메시지와 개발자 로그를 구분하는 것이 좋다.

Q. 401과 403은 어떻게 다르게 보여줘?
A. 401은 로그인 필요 또는 토큰 만료로 안내하고 403은 접근 권한 없음으로 안내한다.

Q. Retry Button은 언제 제공해?
A. 네트워크 오류, 일시적 서버 오류, 목록 조회 실패처럼 사용자가 다시 시도할 수 있는 상황에서 제공할 수 있다.

---

# 6. Empty State Rules

## 6.1 Empty State 기본

### [개념]

Empty State는 API 요청은 성공했지만 화면에 표시할 데이터가 없는 상태다.

검색 결과 없음, 목록 없음, 리뷰 없음, 알림 없음은 대부분 Error가 아니라 Empty State다.

---

### [핵심]

Empty State 사용 상황:

- 검색 결과 없음
- 목록 데이터 없음
- 리뷰 없음
- 알림 없음
- 찜 목록 없음
- 방문 기록 없음
- 댓글 없음
- 첨부파일 없음
- 필터 결과 없음

Empty State UI 요소:

- Empty Message
- Empty Description
- Reset Filter Button
- Create Button
- Search Again Button
- Guide Text

주의:

- Empty State와 Error State를 구분
- 빈 배열은 정상 응답일 수 있음
- `content.length === 0` 확인
- null과 empty array 구분
- 검색 조건 초기화 버튼 제공 가능
- 사용자의 다음 행동 제안 가능

---

### [실무]

List Empty State:

```tsx
function FestivalList({ festivals }: { festivals: FestivalSummaryResponse[] }) {
  if (festivals.length === 0) {
    return <EmptyState title="검색 결과가 없습니다." />;
  }

  return (
    <section>
      {festivals.map((festival) => (
        <FestivalCard key={festival.festivalId} festival={festival} />
      ))}
    </section>
  );
}
```

EmptyState Component:

```tsx
type EmptyStateProps = {
  title: string;
  description?: string;
  action?: React.ReactNode;
};

function EmptyState({ title, description, action }: EmptyStateProps) {
  return (
    <section>
      <h3>{title}</h3>
      {description && <p>{description}</p>}
      {action}
    </section>
  );
}
```

검색 결과 없음:

```tsx
<EmptyState
  title="검색 결과가 없습니다."
  description="검색어 또는 필터 조건을 변경해 보세요."
  action={<button onClick={resetFilters}>필터 초기화</button>}
/>
```

---

### [FAQ]

Q. Empty State는 언제 보여줘?
A. API 요청은 성공했지만 표시할 데이터가 없을 때 보여준다.

Q. 검색 결과가 없을 때는 에러야?
A. 아니다. 보통 정상 응답이지만 content가 비어 있는 Empty State다.

Q. Empty State에서 버튼을 제공해도 돼?
A. 가능하다. 검색 조건 초기화, 새 항목 작성, 다시 검색 같은 다음 행동을 제공할 수 있다.

Q. null과 빈 배열은 같아?
A. 다르다. 목록 응답은 보통 빈 배열이 정상이고 null은 응답 구조나 mapping 기준을 확인해야 한다.

---

# 7. Success State Rules

## 7.1 Success State 기본

### [개념]

Success State는 API 요청이 성공했고 화면에 표시할 데이터가 있는 상태다.

Success State에서는 Response DTO를 UI Component에 전달하고 사용자가 실제 데이터를 볼 수 있게 렌더링한다.

---

### [핵심]

Success State 조건:

- API Request 성공
- Error 없음
- Loading 종료
- Response DTO Mapping 완료
- 데이터 존재
- UI Render 가능

Success State 처리 대상:

- List Render
- Detail Render
- Form Submit Success
- Mutation Success
- Toast Message
- Cache Update
- Refetch
- Navigation
- Modal Close

주의:

- 성공 후 필요한 데이터 갱신
- Mutation 성공 후 목록 refetch 또는 invalidate
- Success Message 남발 주의
- 생성 / 수정 / 삭제 후 UI 상태 동기화
- Response DTO 구조 확인 후 렌더링

---

### [실무]

조회 성공 UI:

```tsx
function FestivalListPage() {
  if (loading) {
    return <FestivalListSkeleton />;
  }

  if (errorMessage) {
    return <ErrorState message={errorMessage} onRetry={loadFestivals} />;
  }

  if (festivals.length === 0) {
    return <EmptyState title="검색 결과가 없습니다." />;
  }

  return <FestivalList festivals={festivals} />;
}
```

작성 성공 Flow:

```text
ReviewForm Submit
→ createReview(requestBody)
→ Success
→ Form Reset
→ Review List Refetch or Query Invalidate
→ Success Message
```

Mutation Success 예:

```typescript
async function handleSubmit(requestBody: ReviewCreateRequest) {
  try {
    setSubmitting(true);

    await createReview(requestBody);
    resetForm();
    await loadReviews();
    setSuccessMessage("리뷰가 작성되었습니다.");
  } finally {
    setSubmitting(false);
  }
}
```

---

### [FAQ]

Q. Success State는 언제야?
A. API 요청이 성공했고 화면에 표시할 데이터가 있거나 성공 후 후속 UI 처리가 필요한 상태다.

Q. 작성 성공 후에는 뭘 해야 해?
A. Form 초기화, 목록 재조회, 성공 메시지 표시, Modal 닫기, 페이지 이동 등을 프로젝트 기준에 맞게 처리한다.

Q. 삭제 성공 후 목록은 어떻게 바꿔?
A. 목록을 다시 조회하거나 현재 목록에서 삭제된 항목을 제거한다. TanStack Query 사용 시 invalidate한다.

Q. 성공 메시지는 항상 보여줘야 해?
A. 아니다. 사용자 행동에 따라 필요한 경우만 보여주는 것이 좋다.

---

# 8. Submit Loading Rules

## 8.1 Submit Loading과 중복 제출 방지

### [개념]

Submit Loading은 Form 제출, 생성, 수정, 삭제 같은 Mutation 요청이 진행 중인 상태다.

Submit Loading은 중복 제출, 중복 결제, 중복 리뷰 작성 같은 문제를 막기 위해 중요하다.

---

### [핵심]

Submit Loading 사용 대상:

- login submit
- signup submit
- review create
- review update
- profile update
- favorite toggle
- payment request
- file upload
- notification read

처리 기준:

- submit 시작 시 submitting true
- 성공 / 실패 후 submitting false
- 버튼 disabled 처리
- handler에서도 중복 요청 방지
- 성공 후 Form reset 가능
- 실패 후 입력값 유지
- Validation Error 표시 가능

주의:

- 실패 시에도 submitting false 처리
- submit 중 같은 요청 재실행 방지
- Button만 disabled하면 Enter 제출은 가능할 수 있음
- 결제 / 주문 요청은 특히 중복 방지 중요
- Mutation 성공 후 관련 데이터 갱신 필요

---

### [실무]

Submit Loading State:

```tsx
function ReviewForm() {
  const [submitting, setSubmitting] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();

    if (submitting) {
      return;
    }

    try {
      setSubmitting(true);
      setErrorMessage("");

      await createReview(toReviewCreateRequest());
    } catch (error) {
      setErrorMessage(getApiErrorMessage(error));
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <button type="submit" disabled={submitting}>
        {submitting ? "작성 중..." : "작성"}
      </button>
      {errorMessage && <p role="alert">{errorMessage}</p>}
    </form>
  );
}
```

TanStack Query Mutation:

```tsx
const mutation = useMutation({
  mutationFn: createReview,
});

<button type="submit" disabled={mutation.isPending}>
  {mutation.isPending ? "작성 중..." : "작성"}
</button>;
```

---

### [FAQ]

Q. Submit Loading은 왜 필요해?
A. 중복 제출과 중복 요청을 막고 사용자가 요청 진행 중임을 알 수 있게 하기 위해 필요하다.

Q. 버튼 disabled만 하면 중복 제출이 완전히 막혀?
A. 대부분 줄어들지만 Enter 제출이나 빠른 이벤트를 고려해 handler에서도 submitting 상태를 확인하는 것이 좋다.

Q. 제출 실패 후 입력값은 지워야 해?
A. 보통 유지하는 것이 좋다. 사용자가 수정 후 다시 제출할 수 있어야 한다.

Q. 제출 성공 후에는 뭘 해야 해?
A. Form reset, 목록 갱신, 성공 메시지, Modal 닫기 등을 프로젝트 UX 기준에 맞게 처리한다.

---

# 9. Field Error and Global Error Rules

## 9.1 Validation Error UI 기준

### [개념]

Field Error는 특정 입력 필드와 연결된 오류다.

Global Error는 Form 전체 또는 API 요청 전체에 대한 오류다.

Validation Error Response를 받으면 field별 오류와 공통 오류를 구분해 표시해야 한다.

---

### [핵심]

Field Error 대상:

- email
- password
- nickname
- rating
- content
- title
- date
- file

Global Error 대상:

- 로그인 실패
- 서버 오류
- 권한 없음
- 네트워크 오류
- 중복 요청
- 알 수 없는 오류

처리 기준:

- field error는 input 근처 표시
- global error는 form 상단 또는 하단 표시
- submit 실패 후 입력값 유지
- 사용자가 수정하면 해당 field error 제거 가능
- 서버 Validation과 Client Validation 충돌 방지

---

### [실무]

Error Response Type:

```typescript
export type ApiErrorResponse = {
  success: false;
  message: string;
  errors?: Record<string, string>;
};
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

Form State:

```typescript
const [fieldErrors, setFieldErrors] = useState<Record<string, string>>({});
const [globalError, setGlobalError] = useState("");
```

UI 표시:

```tsx
<input name="email" aria-invalid={Boolean(fieldErrors.email)} />;

{
  fieldErrors.email && <p role="alert">{fieldErrors.email}</p>;
}
{
  globalError && <p role="alert">{globalError}</p>;
}
```

---

### [FAQ]

Q. Field Error는 어디에 보여줘?
A. 해당 input 근처에 보여주는 것이 좋다.

Q. Global Error는 어디에 보여줘?
A. Form 상단이나 제출 버튼 근처처럼 사용자가 쉽게 볼 수 있는 위치에 보여준다.

Q. 서버 Validation Error는 그대로 보여줘도 돼?
A. 사용자 입력 오류 메시지는 보여줄 수 있지만 민감한 내부 오류 메시지는 노출하지 않아야 한다.

Q. 입력값을 수정하면 field error를 지워도 돼?
A. 가능하다. 사용자가 해당 필드를 수정하면 기존 오류를 제거하는 UX를 사용할 수 있다.

---

# 10. Detail UI State Rules

## 10.1 상세 조회 UI State 기준

### [개념]

Detail UI State는 특정 Resource 상세 API 조회 결과에 따라 Loading, Error, Not Found, Success를 처리하는 기준이다.

상세 화면은 Path Variable 검증과 404 처리도 중요하다.

---

### [핵심]

상세 State 요소:

- data
- loading
- errorMessage
- notFound
- resourceId
- routeParam
- permission
- nullable field

판단 기준:

```text
routeParam invalid → Error or Redirect
loading true → Detail Loading UI
404 → Not Found UI
errorMessage exists → Error UI
data exists → Detail Success UI
```

주의:

- Path Variable undefined 방지
- `useParams()` 값은 문자열일 수 있음
- 숫자 id 변환과 검증
- 404와 500 구분
- null 가능 필드 fallback
- 상세 데이터 초기값 null 처리

---

### [실무]

Detail Hook:

```typescript
export function useFestivalDetail(festivalId: number | null) {
  const [data, setData] = useState<FestivalDetailResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  async function load() {
    if (!festivalId) {
      setErrorMessage("잘못된 요청입니다.");
      return;
    }

    try {
      setLoading(true);
      setErrorMessage("");

      const detail = await getFestivalDetail(festivalId);
      setData(detail);
    } catch (error) {
      setErrorMessage(getApiErrorMessage(error));
    } finally {
      setLoading(false);
    }
  }

  return { data, loading, errorMessage, load };
}
```

Route Param 처리:

```tsx
const { festivalId } = useParams();
const numericFestivalId = festivalId ? Number(festivalId) : null;

const { data, loading, errorMessage, load } =
  useFestivalDetail(numericFestivalId);
```

Detail Component:

```tsx
if (loading) {
  return <FestivalDetailSkeleton />;
}

if (errorMessage) {
  return <ErrorState message={errorMessage} onRetry={load} />;
}

if (!data) {
  return <EmptyState title="축제 정보를 찾을 수 없습니다." />;
}

return <FestivalDetail festival={data} />;
```

---

### [FAQ]

Q. 상세 조회에서 가장 먼저 확인할 것은 뭐야?
A. Route Param 또는 Path Variable 값이 유효한지 확인해야 한다.

Q. useParams 값은 number야?
A. 보통 string이므로 필요한 경우 Number 변환과 검증을 해야 한다.

Q. 상세 API 404는 어떻게 보여줘?
A. 요청한 Resource가 없다는 Not Found UI를 보여주는 것이 좋다.

Q. 상세 데이터 초기값은 뭘로 둬?
A. 보통 `null`로 두고 Loading 종료 후 data 존재 여부를 확인한다.

---

# 11. Accessibility Rules for API UI State

## 11.1 접근성 기준

### [개념]

API UI State 접근성은 Loading, Error, Empty, Success 상태를 보조 기술 사용자도 이해할 수 있게 표시하는 기준이다.

Error Message, Loading Message, 상태 변화는 semantic HTML과 ARIA 속성을 고려한다.

---

### [핵심]

접근성 키워드:

- role="alert"
- aria-live
- aria-busy
- disabled
- focus management
- semantic HTML
- error message association
- loading text
- empty message

처리 기준:

- Error Message에 `role="alert"` 사용 가능
- Loading 영역에 `aria-busy` 사용 가능
- Button disabled는 실제 disabled 속성 사용
- Form Field Error는 input과 연결 가능
- 색상만으로 상태 전달 금지
- Skeleton만 있고 텍스트가 없으면 접근성 부족 가능

---

### [실무]

Error Message:

```tsx
<p role="alert">요청 처리 중 문제가 발생했습니다.</p>
```

Loading Region:

```tsx
<section aria-busy={loading}>
  {loading ? <p>Loading...</p> : <FestivalList festivals={festivals} />}
</section>
```

Field Error 연결:

```tsx
<input
  id="email"
  aria-invalid={Boolean(fieldErrors.email)}
  aria-describedby={fieldErrors.email ? "email-error" : undefined}
/>;

{
  fieldErrors.email && (
    <p id="email-error" role="alert">
      {fieldErrors.email}
    </p>
  );
}
```

Submit Button:

```tsx
<button type="submit" disabled={submitting}>
  {submitting ? "제출 중..." : "제출"}
</button>
```

---

### [FAQ]

Q. Error Message에 role="alert"를 써도 돼?
A. 가능하다. 오류 메시지를 보조 기술이 즉시 인지할 수 있게 하는 데 도움이 된다.

Q. Loading Spinner만 보여줘도 돼?
A. 가능하지만 접근성을 위해 텍스트나 aria 속성을 함께 고려하는 것이 좋다.

Q. Disabled Button에는 설명이 필요해?
A. 상황에 따라 필요하다. 제출 중 텍스트를 바꿔 사용자가 이유를 알 수 있게 하면 좋다.

Q. API UI State 접근성은 별도 문서에서 더 다뤄?
A. 심화 기준은 Frontend Accessibility Domain Rules에서 다루는 것이 좋다.

---

# 12. UI State Testing and Debugging Rules

## 12.1 API UI State 검수 기준

### [개념]

API UI State Testing은 API 요청의 성공, 실패, 빈 데이터, 로딩 상태가 화면에서 올바르게 표현되는지 검증하는 과정이다.

---

### [핵심]

검수 대상:

- Initial Loading UI
- Refetch Loading UI
- Submit Loading UI
- Error UI
- Empty UI
- Success UI
- Button Disabled
- Retry Button
- Field Error
- Global Error
- Detail Not Found UI

검수 방법:

- Network throttling
- API 실패 상황 테스트
- 빈 배열 응답 테스트
- 401 / 403 / 404 / 500 테스트
- Validation Error 테스트
- 중복 클릭 테스트
- 느린 응답 테스트
- Mock Service Worker 사용 가능

---

### [실무]

검수 Flow:

```text
API UI State Review
→ Loading 상황 확인
→ Success 데이터 표시 확인
→ Empty 데이터 표시 확인
→ Error 응답 표시 확인
→ Retry 동작 확인
→ Submit 중복 방지 확인
→ Network Response와 UI 비교
```

테스트 시나리오:

```text
목록 조회 성공 + content 있음
→ Success State
```

```text
목록 조회 성공 + content []
→ Empty State
```

```text
목록 조회 실패 500
→ Error State + Retry Button
```

```text
리뷰 작성 중 버튼 연속 클릭
→ 중복 요청 방지
```

```text
로그인 만료 401
→ 로그인 필요 메시지 or redirect
```

---

### [FAQ]

Q. API UI State는 어떻게 테스트해?
A. 성공, 실패, 빈 데이터, 느린 응답, 중복 제출 상황을 만들어 Loading / Error / Empty / Success UI를 확인한다.

Q. Empty State 테스트는 어떻게 해?
A. Backend나 Mock API에서 빈 배열 또는 빈 content를 응답하게 해서 확인한다.

Q. Loading State는 어떻게 테스트해?
A. Network throttling이나 Mock delay를 사용해 느린 응답 상황을 만든다.

Q. 중복 제출은 어떻게 확인해?
A. submit 버튼을 빠르게 여러 번 눌러 Network 요청이 중복 발생하는지 확인한다.

---

# 13. Common Mistakes

## 13.1 API UI State 공통 실수

### [개념]

API UI State 실수는 Loading, Error, Empty, Success 상태를 구분하지 않거나 요청 생명주기를 제대로 관리하지 않을 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Loading State 누락
- Error State 누락
- Empty State와 Error State 혼동
- API 실패 시 loading false 누락
- catch에서 에러를 삼킴
- Error 객체 전체를 화면에 출력
- 서버 에러 원문 노출
- 401과 403을 같은 메시지로 처리
- 검색 결과 없음은 에러로 처리
- 빈 배열을 null처럼 처리
- 초기 data null에서 필드 접근
- `.map()` 전에 배열 확인 누락
- submit 중 버튼 disabled 누락
- 중복 제출 방지 누락
- refetch 때 기존 데이터를 무조건 삭제
- mutation 성공 후 목록 갱신 누락
- TanStack Query의 isLoading / isFetching 혼동
- Retry Button이 같은 요청을 재실행하지 않음
- Network 탭에서 실제 요청 횟수 미확인

---

### [실무]

문제 예:

```text
문제: API 실패 후 계속 Loading 표시
원인: catch 발생 시 loading false 처리 누락
해결: finally에서 setLoading(false) 처리
```

문제 예:

```text
문제: 검색 결과가 없는데 오류 메시지 표시
원인: Empty State와 Error State 혼동
해결: 요청 성공 + content.length === 0이면 Empty State 처리
```

문제 예:

```text
문제: 리뷰가 두 번 작성됨
원인: submit 중 버튼 disabled와 handler guard 누락
해결: submitting 상태로 중복 제출 방지
```

문제 예:

```text
문제: Error Message에 [object Object] 표시
원인: Error 객체 전체를 화면에 출력
해결: getApiErrorMessage로 사용자 메시지 변환
```

해결 우선순위:

```text
Network Request 확인
→ API Response 확인
→ loading lifecycle 확인
→ error mapping 확인
→ empty condition 확인
→ success render 확인
→ duplicate request 확인
```

---

### [FAQ]

Q. API UI State에서 가장 흔한 실수는?
A. Loading, Error, Empty를 구분하지 않거나 실패 시 loading을 종료하지 않는 것이다.

Q. 검색 결과가 없으면 Error State야?
A. 아니다. API 요청이 성공했다면 Empty State다.

Q. API 실패 후 화면이 계속 로딩이면 뭘 봐?
A. `finally`에서 loading false 처리가 있는지 확인해야 한다.

Q. 중복 제출은 어떻게 막아?
A. submitting 상태를 두고 버튼 disabled와 handler guard를 함께 적용한다.

---

# 14. Part06 Checklist

## 14.1 Loading / Error / Empty UI State 검수 기준

### [개념]

Part06 Loading / Error / Empty UI State 문서는 Frontend Agent가 API 요청 생명주기에 따라 화면 상태를 정확히 구분하고, 사용자에게 안정적인 UI 피드백을 제공하도록 만드는 문서다.

---

### [핵심]

Checklist:

```md
- [ ] API UI State 개념이 포함되었는가?
- [ ] Rendering Priority 기준이 포함되었는가?
- [ ] Loading State 기준이 포함되었는가?
- [ ] Initial Loading / Refetch Loading 구분이 포함되었는가?
- [ ] Error State 기준이 포함되었는가?
- [ ] Empty State 기준이 포함되었는가?
- [ ] Success State 기준이 포함되었는가?
- [ ] Submit Loading 기준이 포함되었는가?
- [ ] Field Error / Global Error 기준이 포함되었는가?
- [ ] Detail UI State 기준이 포함되었는가?
- [ ] Accessibility 기준이 포함되었는가?
- [ ] UI State Testing 기준이 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Rendering Priority Check
→ Loading State Check
→ Error State Check
→ Empty State Check
→ Success State Check
→ Submit Loading Check
→ Field / Global Error Check
→ Detail UI State Check
→ Accessibility Check
→ Testing Scenario Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

최종 기준:

- Loading / Error / Empty / Success 구분 가능
- Initial Loading과 Refetch Loading 구분 가능
- Submit Loading과 중복 제출 방지 가능
- Field Error와 Global Error 구분 가능
- Detail 화면의 Not Found / Error / Success 처리 가능
- TanStack Query 상태와 UI 연결 가능
- API UI State 테스트 시나리오 구성 가능
- Frontend Agent가 사용자 친화적인 Data Fetching UI를 생성 가능

---

### [FAQ]

Q. Part06의 목적은 뭐야?
A. Frontend Agent가 API 요청 생명주기에 따라 Loading, Error, Empty, Success UI를 정확히 처리하게 만드는 것이다.

Q. Part06에서 가장 중요한 기준은 뭐야?
A. Empty State와 Error State 구분, 실패 시 loading 종료, submit 중복 방지, 실제 Response 기준 UI 판단이다.

Q. Part06에서 Pagination / Infinite Scroll 상세 구현을 다뤄?
A. 아니다. Part06은 UI State 관점만 다루고 Pagination / Infinite Scroll 상세 구현은 Part08에서 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. API UI State가 뭐야?
A. API 요청 중, 실패, 성공했지만 데이터 없음, 성공 후 데이터 있음 같은 화면 상태를 구분하는 기준이다.

Q. Loading / Error / Empty / Success를 왜 나눠?
A. 요청 중인지, 실패인지, 데이터가 없는 정상 상태인지, 표시할 데이터가 있는지 사용자에게 명확히 보여주기 위해 나눈다.

Q. Empty State와 Error State는 뭐가 달라?
A. Empty State는 요청 성공 후 데이터가 없는 상태이고 Error State는 요청 자체가 실패한 상태다.

Q. API UI State는 어디서 관리해?
A. Component, Custom Hook, TanStack Query Hook에서 관리할 수 있다.

Q. 렌더링 우선순위는 왜 필요해?
A. Loading, Error, Empty, Success 상태가 동시에 섞여 보이는 문제를 막기 위해 필요하다.

Q. 최초 로딩 중 data가 비어 있으면 Empty State야?
A. 아니다. 최초 로딩 중에는 Loading State가 우선이다.

Q. Error와 Empty 중 무엇을 먼저 판단해?
A. 요청 실패가 있으면 Error State를 먼저 처리하고, 요청 성공 후 데이터가 없을 때 Empty State를 처리한다.

Q. Refetch 중에는 화면을 비워야 해?
A. 항상 그렇지 않다. 기존 데이터를 유지하고 작은 로딩 표시만 보여줄 수 있다.

Q. Loading State는 왜 필요해?
A. API 요청 중 사용자에게 진행 상태를 알려주고 중복 클릭이나 빈 화면 혼란을 줄이기 위해 필요하다.

Q. loading은 언제 false로 바꿔?
A. API 성공이나 실패와 관계없이 요청이 끝나는 `finally`에서 false로 바꾸는 것이 안전하다.

Q. 제출 버튼은 loading 중에 disabled 해야 해?
A. 중복 제출을 막기 위해 submit loading 중에는 버튼을 disabled 처리하는 것이 좋다.

Q. Loading UI는 Spinner와 Skeleton 중 뭐가 좋아?
A. 화면 구조를 미리 보여주고 싶으면 Skeleton, 짧은 작업이나 버튼 내부 상태는 Spinner나 text loading이 적합하다.

Q. isLoading과 isFetching은 달라?
A. TanStack Query에서는 최초 로딩과 백그라운드 재조회 상태를 구분할 수 있다.

Q. Refetch 중에는 기존 목록을 지워야 해?
A. 항상 그렇지 않다. 기존 목록을 유지하면서 작은 로딩 표시를 보여줄 수 있다.

Q. Skeleton은 언제 쓰는 게 좋아?
A. 최초 로딩처럼 아직 보여줄 데이터가 없을 때 적합하다.

Q. 검색 조건이 바뀌면 기존 데이터를 유지해도 돼?
A. UX 기준에 따라 가능하지만 이전 조건의 데이터와 새 조건의 데이터가 혼동되지 않도록 주의한다.

Q. Error State는 언제 보여줘?
A. API 요청 실패, 인증 실패, 권한 없음, 서버 오류, 네트워크 오류처럼 요청이 정상 완료되지 않았을 때 보여준다.

Q. API 에러 메시지는 그대로 보여줘도 돼?
A. 민감한 정보가 포함될 수 있으므로 사용자에게 보여줄 메시지와 개발자 로그를 구분하는 것이 좋다.

Q. 401과 403은 어떻게 다르게 보여줘?
A. 401은 로그인 필요 또는 토큰 만료로 안내하고 403은 접근 권한 없음으로 안내한다.

Q. Retry Button은 언제 제공해?
A. 네트워크 오류, 일시적 서버 오류, 목록 조회 실패처럼 사용자가 다시 시도할 수 있는 상황에서 제공할 수 있다.

Q. Empty State는 언제 보여줘?
A. API 요청은 성공했지만 표시할 데이터가 없을 때 보여준다.

Q. 검색 결과가 없을 때는 에러야?
A. 아니다. 보통 정상 응답이지만 content가 비어 있는 Empty State다.

Q. Empty State에서 버튼을 제공해도 돼?
A. 가능하다. 검색 조건 초기화, 새 항목 작성, 다시 검색 같은 다음 행동을 제공할 수 있다.

Q. null과 빈 배열은 같아?
A. 다르다. 목록 응답은 보통 빈 배열이 정상이고 null은 응답 구조나 mapping 기준을 확인해야 한다.

Q. Success State는 언제야?
A. API 요청이 성공했고 화면에 표시할 데이터가 있거나 성공 후 후속 UI 처리가 필요한 상태다.

Q. 작성 성공 후에는 뭘 해야 해?
A. Form 초기화, 목록 재조회, 성공 메시지 표시, Modal 닫기, 페이지 이동 등을 프로젝트 기준에 맞게 처리한다.

Q. 삭제 성공 후 목록은 어떻게 바꿔?
A. 목록을 다시 조회하거나 현재 목록에서 삭제된 항목을 제거한다. TanStack Query 사용 시 invalidate한다.

Q. 성공 메시지는 항상 보여줘야 해?
A. 아니다. 사용자 행동에 따라 필요한 경우만 보여주는 것이 좋다.

Q. Submit Loading은 왜 필요해?
A. 중복 제출과 중복 요청을 막고 사용자가 요청 진행 중임을 알 수 있게 하기 위해 필요하다.

Q. 버튼 disabled만 하면 중복 제출이 완전히 막혀?
A. 대부분 줄어들지만 Enter 제출이나 빠른 이벤트를 고려해 handler에서도 submitting 상태를 확인하는 것이 좋다.

Q. 제출 실패 후 입력값은 지워야 해?
A. 보통 유지하는 것이 좋다. 사용자가 수정 후 다시 제출할 수 있어야 한다.

Q. 제출 성공 후에는 뭘 해야 해?
A. Form reset, 목록 갱신, 성공 메시지, Modal 닫기 등을 프로젝트 UX 기준에 맞게 처리한다.

Q. Field Error는 어디에 보여줘?
A. 해당 input 근처에 보여주는 것이 좋다.

Q. Global Error는 어디에 보여줘?
A. Form 상단이나 제출 버튼 근처처럼 사용자가 쉽게 볼 수 있는 위치에 보여준다.

Q. 서버 Validation Error는 그대로 보여줘도 돼?
A. 사용자 입력 오류 메시지는 보여줄 수 있지만 민감한 내부 오류 메시지는 노출하지 않아야 한다.

Q. 입력값을 수정하면 field error를 지워도 돼?
A. 가능하다. 사용자가 해당 필드를 수정하면 기존 오류를 제거하는 UX를 사용할 수 있다.

Q. 상세 조회에서 가장 먼저 확인할 것은 뭐야?
A. Route Param 또는 Path Variable 값이 유효한지 확인해야 한다.

Q. useParams 값은 number야?
A. 보통 string이므로 필요한 경우 Number 변환과 검증을 해야 한다.

Q. 상세 API 404는 어떻게 보여줘?
A. 요청한 Resource가 없다는 Not Found UI를 보여주는 것이 좋다.

Q. 상세 데이터 초기값은 뭘로 둬?
A. 보통 `null`로 두고 Loading 종료 후 data 존재 여부를 확인한다.

Q. Error Message에 role="alert"를 써도 돼?
A. 가능하다. 오류 메시지를 보조 기술이 즉시 인지할 수 있게 하는 데 도움이 된다.

Q. Loading Spinner만 보여줘도 돼?
A. 가능하지만 접근성을 위해 텍스트나 aria 속성을 함께 고려하는 것이 좋다.

Q. Disabled Button에는 설명이 필요해?
A. 상황에 따라 필요하다. 제출 중 텍스트를 바꿔 사용자가 이유를 알 수 있게 하면 좋다.

Q. API UI State 접근성은 별도 문서에서 더 다뤄?
A. 심화 기준은 Frontend Accessibility Domain Rules에서 다루는 것이 좋다.

Q. API UI State는 어떻게 테스트해?
A. 성공, 실패, 빈 데이터, 느린 응답, 중복 제출 상황을 만들어 Loading / Error / Empty / Success UI를 확인한다.

Q. Empty State 테스트는 어떻게 해?
A. Backend나 Mock API에서 빈 배열 또는 빈 content를 응답하게 해서 확인한다.

Q. Loading State는 어떻게 테스트해?
A. Network throttling이나 Mock delay를 사용해 느린 응답 상황을 만든다.

Q. 중복 제출은 어떻게 확인해?
A. submit 버튼을 빠르게 여러 번 눌러 Network 요청이 중복 발생하는지 확인한다.

Q. API UI State에서 가장 흔한 실수는?
A. Loading, Error, Empty를 구분하지 않거나 실패 시 loading을 종료하지 않는 것이다.

Q. 검색 결과가 없으면 Error State야?
A. 아니다. API 요청이 성공했다면 Empty State다.

Q. API 실패 후 화면이 계속 로딩이면 뭘 봐?
A. `finally`에서 loading false 처리가 있는지 확인해야 한다.

Q. 중복 제출은 어떻게 막아?
A. submitting 상태를 두고 버튼 disabled와 handler guard를 함께 적용한다.

Q. Part06 Loading / Error / Empty UI State의 목적은 뭐야?
A. Frontend Agent가 API 요청 생명주기에 따라 Loading, Error, Empty, Success UI를 정확히 처리하게 만드는 것이다.

Q. Part06에서 Pagination / Infinite Scroll 상세 구현을 다뤄?
A. 아니다. Part06은 UI State 관점만 다루고 Pagination / Infinite Scroll 상세 구현은 Part08에서 다룬다.
