# UI Component Pattern Part06 - State UI Components

---

# 1. State UI Component Overview

## 1.1 State UI Component Purpose

### [개념]

State UI Component는 데이터 요청, 사용자 작업, 화면 상태에 따라 표시되는 공통 상태 UI Component다.

State UI Component는 LoadingState, ErrorState, EmptyState, Skeleton 같은 UI를 의미한다.

State UI Component는 사용자가 현재 화면 상태를 이해하고 다음 행동을 선택할 수 있도록 돕는다.

---

### [핵심]

State UI Component 핵심 대상:

- LoadingState
- ErrorState
- EmptyState
- Skeleton
- InlineLoading
- PageLoading
- InlineError
- PageError
- Retry Action
- Empty Action

핵심 기준:

- loading / error / empty 상태를 명확히 구분
- 사용자 친화 메시지 사용
- 내부 에러 원문 노출 금지
- Retry 가능 여부에 따라 action 제공
- EmptyState에는 다음 행동 제공
- LoadingState에는 접근성 role status 고려
- ErrorState에는 role alert 고려
- Skeleton은 레이아웃 예측 가능할 때 사용
- Page 상태와 Inline 상태를 구분
- API 호출은 State UI Component가 직접 처리하지 않음

---

### [실무]

2026 실무 기준에서 State UI Component는 단순 메시지 출력이 아니다.

Frontend Agent는 데이터 상태를 아래 흐름으로 판단해야 한다.

```text
Request Start
→ LoadingState
→ Request Success
→ EmptyState or Data UI
→ Request Fail
→ ErrorState
→ Retry or Recovery Action
```

책임 분리:

```text
Page / Feature Container
→ loading / error / empty 상태 판단
→ retry / reset / refetch 함수 보유

State UI Component
→ 상태 메시지 표시
→ action UI 렌더링
→ 접근성 속성 제공

Common Button / Link
→ action UI로 조합
```

---

### [FAQ]

Q. State UI Component는 왜 필요해?
A. Loading, Error, Empty 상태를 일관되게 보여주고 사용자가 다음 행동을 이해하게 만들기 위해 필요하다.

Q. LoadingState, ErrorState, EmptyState는 어디에서 조합해?
A. 보통 Page나 Feature Container에서 데이터 상태를 판단한 뒤 조합한다.

Q. State UI Component 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. Retry 이벤트만 외부로 전달하고 실제 API 호출은 Page나 Hook에서 처리하는 것이 좋다.

---

# 2. LoadingState Component Pattern

## 2.1 LoadingState Responsibility

### [개념]

LoadingState Component는 데이터를 불러오거나 작업을 처리하는 중임을 사용자에게 알려주는 공통 UI Component다.

LoadingState는 사용자가 화면이 멈춘 것이 아니라 처리 중임을 알 수 있게 해야 한다.

---

### [핵심]

LoadingState 기본 책임:

- loading message 표시
- spinner 또는 progress 표시
- role status 제공
- aria-live polite 고려
- fullPage / inline 구분
- loading 크기 size 지원 가능
- children 또는 message 지원 가능
- 중복 클릭 방지 UI와 연결 가능

Props 후보:

- message
- size
- fullPage
- variant
- ariaLabel
- children
- className

주의:

- spinner만 단독 표시 지양
- 너무 긴 message 지양
- loading 상태에서 기존 콘텐츠 유지 여부 결정
- Page Loading과 Inline Loading 구분
- Button Loading과 Page Loading 구분

---

### [실무]

LoadingState 예:

```tsx
type LoadingStateProps = {
  message?: string;
  fullPage?: boolean;
  className?: string;
};

function LoadingState({
  message = "불러오는 중입니다.",
  fullPage = false,
  className = "",
}: LoadingStateProps) {
  return (
    <section
      className={`loading-state ${fullPage ? "loading-state-full" : ""} ${className}`}
      role="status"
      aria-live="polite"
    >
      <span className="spinner" aria-hidden="true" />
      <p>{message}</p>
    </section>
  );
}
```

Page Loading 예:

```tsx
function FestivalListPage() {
  const { data, loading } = useFestivals();

  if (loading) {
    return <LoadingState fullPage message="축제 정보를 불러오는 중입니다." />;
  }

  return <FestivalList festivals={data} />;
}
```

Inline Loading 예:

```tsx
function LoadMoreArea({ loading }: { loading: boolean }) {
  if (!loading) {
    return null;
  }

  return <LoadingState message="더 불러오는 중입니다." />;
}
```

---

### [FAQ]

Q. LoadingState에는 텍스트가 필요해?
A. 접근성과 사용자 이해를 위해 짧은 loading message를 제공하는 것이 좋다.

Q. 모든 로딩에 같은 LoadingState를 써도 돼?
A. 가능하지만 페이지 로딩, 버튼 로딩, 하단 더보기 로딩은 크기와 위치가 다를 수 있다.

Q. LoadingState에 role status를 쓰는 이유는?
A. 보조기술이 현재 화면이 처리 중임을 사용자에게 알릴 수 있게 하기 위해서다.

---

## 2.2 Page Loading vs Inline Loading

### [개념]

Page Loading은 화면 전체 데이터가 준비되지 않았을 때 표시하는 loading UI다.

Inline Loading은 특정 영역, 목록 하단, 버튼 주변처럼 일부 UI만 처리 중일 때 표시하는 loading UI다.

---

### [핵심]

Page Loading 사용:

- 초기 페이지 데이터 요청
- 상세 페이지 전체 데이터 요청
- 인증 상태 확인
- 전체 화면이 아직 렌더링 불가능한 경우

Inline Loading 사용:

- 목록 더보기
- 댓글 추가 로딩
- 특정 섹션만 갱신
- 필터 변경 중 일부 영역 갱신
- 이미 기존 콘텐츠가 있는 상태에서 추가 요청

비교:

| 기준        | Page Loading          | Inline Loading   |
| ----------- | --------------------- | ---------------- |
| 범위        | 화면 전체             | 일부 영역        |
| 기존 콘텐츠 | 없음 또는 숨김        | 유지 가능        |
| 예          | 상세 페이지 초기 로딩 | 무한 스크롤 하단 |
| Props       | fullPage              | inline 기본      |
| UX          | 기다림 안내           | 기존 흐름 유지   |

---

### [실무]

Page Loading 예:

```tsx
if (loading && !data) {
  return <LoadingState fullPage message="페이지를 불러오는 중입니다." />;
}
```

Inline Loading 예:

```tsx
return (
  <>
    <FestivalList festivals={festivals} />
    {loadingMore && <LoadingState message="축제를 더 불러오는 중입니다." />}
  </>
);
```

권장:

```text
초기 데이터 없음
→ Page Loading

기존 데이터 있음
→ Inline Loading or Skeleton Update

버튼 작업 중
→ Button loading prop
```

---

### [FAQ]

Q. Page Loading과 Inline Loading은 어떻게 구분해?
A. 화면 전체가 준비되지 않았으면 Page Loading, 기존 콘텐츠가 있고 일부 영역만 처리 중이면 Inline Loading이 적합하다.

Q. 데이터가 이미 있는데 refetch 중이면 전체 LoadingState를 보여줘야 해?
A. 보통 기존 콘텐츠를 유지하고 Inline Loading이나 refresh indicator를 보여주는 것이 좋다.

Q. Button 클릭 처리 중에도 LoadingState를 써?
A. 버튼 내부 처리 중이면 Button의 loading prop을 사용하는 것이 더 적합하다.

---

# 3. ErrorState Component Pattern

## 3.1 ErrorState Responsibility

### [개념]

ErrorState Component는 요청 실패나 화면 표시 실패 상황에서 사용자에게 오류 안내와 다음 행동을 제공하는 Component다.

ErrorState는 개발자용 에러 원문이 아니라 사용자 친화적인 메시지를 표시해야 한다.

---

### [핵심]

ErrorState 기본 책임:

- 오류 title 표시
- 사용자 친화 message 표시
- retry action 제공 가능
- role alert 제공
- statusCode 기반 문구 가능
- page error / inline error 구분
- 내부 에러 상세 노출 방지
- recovery action 제공 가능

Props 후보:

- title
- message
- action
- onRetry
- retryText
- statusCode
- variant
- fullPage
- className

주의:

- 서버 에러 원문 그대로 노출 금지
- stack trace 노출 금지
- 민감 정보 노출 금지
- 재시도 불가능한 오류에 Retry 버튼 남발 금지
- ErrorState와 EmptyState 혼동 금지

---

### [실무]

ErrorState 예:

```tsx
type ErrorStateProps = {
  title?: string;
  message: string;
  onRetry?: () => void;
  retryText?: string;
  fullPage?: boolean;
};

function ErrorState({
  title = "문제가 발생했습니다.",
  message,
  onRetry,
  retryText = "다시 시도",
  fullPage = false,
}: ErrorStateProps) {
  return (
    <section
      className={`error-state ${fullPage ? "error-state-full" : ""}`}
      role="alert"
    >
      <h2>{title}</h2>
      <p>{message}</p>
      {onRetry && (
        <Button type="button" variant="secondary" onClick={onRetry}>
          {retryText}
        </Button>
      )}
    </section>
  );
}
```

Page Error 예:

```tsx
if (error) {
  return (
    <ErrorState
      fullPage
      message="축제 정보를 불러오지 못했습니다."
      onRetry={refetch}
    />
  );
}
```

Inline Error 예:

```tsx
{
  commentError && (
    <ErrorState
      message="댓글을 불러오지 못했습니다."
      onRetry={refetchComments}
    />
  );
}
```

---

### [FAQ]

Q. ErrorState에는 항상 Retry 버튼이 있어야 해?
A. 아니다. 재시도 가능한 오류에만 제공하는 것이 좋다.

Q. 서버 에러 원문을 ErrorState에 그대로 넣어도 돼?
A. 권장하지 않는다. 사용자용 메시지로 변환하는 것이 안전하다.

Q. ErrorState와 EmptyState는 뭐가 달라?
A. ErrorState는 요청 실패 상태이고 EmptyState는 요청 성공 후 데이터가 없는 상태다.

---

## 3.2 Error Message Mapping

### [개념]

Error Message Mapping은 서버 에러, 네트워크 에러, 권한 에러를 사용자 친화적인 UI 메시지로 변환하는 기준이다.

ErrorState는 상세한 내부 원인을 노출하기보다 사용자가 이해할 수 있는 안내와 가능한 다음 행동을 제공해야 한다.

---

### [핵심]

Mapping 대상:

- Network Error
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 409 Conflict
- 500 Server Error
- Timeout
- Unknown Error

권장 메시지 기준:

- 짧고 명확함
- 사용자 행동 가능성 제공
- 내부 구현 정보 노출 금지
- 민감 데이터 노출 금지
- 재시도 가능 여부 구분
- 로그인 필요 여부 구분

---

### [실무]

Error Mapping 예:

```tsx
function getErrorMessage(statusCode?: number) {
  switch (statusCode) {
    case 401:
      return "로그인이 필요합니다.";
    case 403:
      return "접근 권한이 없습니다.";
    case 404:
      return "요청한 정보를 찾을 수 없습니다.";
    case 409:
      return "이미 처리된 요청입니다.";
    case 500:
      return "서버에 문제가 발생했습니다. 잠시 후 다시 시도해 주세요.";
    default:
      return "요청을 처리하지 못했습니다. 다시 시도해 주세요.";
  }
}
```

사용 예:

```tsx
<ErrorState
  message={getErrorMessage(error?.statusCode)}
  onRetry={error?.retryable ? refetch : undefined}
/>
```

주의:

```text
Internal Server Error at UserService.java:52
SQL syntax error
JWT signature stack trace
database connection string
```

위와 같은 내부 상세는 사용자 UI에 직접 노출하지 않는다.

---

### [FAQ]

Q. 서버 에러 코드를 그대로 보여줘도 돼?
A. 상태 코드를 참고할 수는 있지만 사용자에게는 이해 가능한 메시지로 변환하는 것이 좋다.

Q. 401 오류는 어떻게 보여줘?
A. 로그인이 필요하다는 안내와 로그인 이동 action을 제공할 수 있다.

Q. 500 오류는 어떻게 보여줘?
A. 서버 문제 안내와 잠시 후 재시도 메시지를 제공하는 것이 좋다.

---

# 4. EmptyState Component Pattern

## 4.1 EmptyState Responsibility

### [개념]

EmptyState Component는 요청 성공 후 표시할 데이터가 없거나 사용자가 아직 데이터를 만들지 않은 상태를 안내하는 Component다.

EmptyState는 데이터 없음의 이유와 사용자가 할 수 있는 다음 행동을 함께 제공하는 것이 좋다.

---

### [핵심]

EmptyState 기본 책임:

- empty title 표시
- description 표시 가능
- action 제공 가능
- icon 제공 가능
- 검색 결과 없음과 첫 사용 상태 구분
- 사용자 다음 행동 안내
- 부정적인 문구 지양
- ErrorState와 구분

Props 후보:

- title
- description
- action
- icon
- variant
- align
- className

EmptyState 사용 대상:

- 검색 결과 없음
- 목록 데이터 없음
- 아직 작성한 리뷰 없음
- 알림 없음
- 장바구니 없음
- 필터 결과 없음
- 첫 사용 onboarding

---

### [실무]

EmptyState 예:

```tsx
type EmptyStateProps = {
  title: string;
  description?: string;
  action?: React.ReactNode;
  icon?: React.ReactNode;
};

function EmptyState({ title, description, action, icon }: EmptyStateProps) {
  return (
    <section className="empty-state">
      {icon && <div aria-hidden="true">{icon}</div>}
      <h2>{title}</h2>
      {description && <p>{description}</p>}
      {action}
    </section>
  );
}
```

검색 결과 없음 예:

```tsx
<EmptyState
  title="검색 결과가 없습니다."
  description="검색어를 바꾸거나 필터를 초기화해 보세요."
  action={<Button onClick={resetFilter}>필터 초기화</Button>}
/>
```

첫 사용 상태 예:

```tsx
<EmptyState
  title="아직 작성한 리뷰가 없습니다."
  description="방문한 축제에 첫 리뷰를 남겨보세요."
  action={<Button onClick={goToFestivals}>축제 둘러보기</Button>}
/>
```

---

### [FAQ]

Q. EmptyState에는 뭘 넣어야 해?
A. 데이터가 없다는 안내, 이유, 사용자가 할 수 있는 다음 행동을 넣는 것이 좋다.

Q. 목록이 비어 있으면 그냥 아무것도 안 보여줘도 돼?
A. 권장하지 않는다. EmptyState를 보여주는 것이 사용자 경험에 좋다.

Q. EmptyState와 ErrorState는 뭐가 달라?
A. EmptyState는 요청 성공 후 데이터가 없는 상태이고 ErrorState는 요청 실패 상태다.

---

## 4.2 EmptyState Type

### [개념]

EmptyState Type은 데이터가 없는 이유에 따라 EmptyState 메시지와 action을 다르게 설계하는 기준이다.

모든 빈 상태를 같은 문구로 처리하면 사용자가 다음 행동을 이해하기 어렵다.

---

### [핵심]

EmptyState 유형:

- First Use Empty
- Search Result Empty
- Filter Result Empty
- User Content Empty
- Notification Empty
- Permission Empty
- Removed Content Empty

유형별 기준:

| 유형                  | 상황               | 권장 Action         |
| --------------------- | ------------------ | ------------------- |
| First Use Empty       | 처음 사용          | 생성 / 둘러보기     |
| Search Result Empty   | 검색 결과 없음     | 검색어 변경         |
| Filter Result Empty   | 필터 결과 없음     | 필터 초기화         |
| User Content Empty    | 작성한 데이터 없음 | 작성하기            |
| Notification Empty    | 알림 없음          | 없음 또는 설정 보기 |
| Permission Empty      | 권한 없음          | 로그인 / 권한 요청  |
| Removed Content Empty | 삭제된 콘텐츠      | 목록으로 이동       |

---

### [실무]

Search Empty 예:

```tsx
<EmptyState
  title="검색 결과가 없습니다."
  description="다른 검색어를 입력하거나 필터를 초기화해 보세요."
  action={<Button onClick={resetSearch}>검색 초기화</Button>}
/>
```

Notification Empty 예:

```tsx
<EmptyState
  title="새 알림이 없습니다."
  description="중요한 소식이 생기면 이곳에 표시됩니다."
/>
```

Permission Empty 예:

```tsx
<EmptyState
  title="로그인이 필요합니다."
  description="찜한 축제를 보려면 로그인해 주세요."
  action={<Button onClick={goToLogin}>로그인하기</Button>}
/>
```

---

### [FAQ]

Q. 검색 결과 없음과 첫 사용 EmptyState는 다르게 써야 해?
A. 다르게 쓰는 것이 좋다. 검색 결과 없음은 검색어 변경이나 필터 초기화를 안내하고, 첫 사용 상태는 생성이나 탐색을 안내한다.

Q. EmptyState action은 항상 필요해?
A. 항상 필요하지는 않지만 사용자가 다음 행동을 취할 수 있는 상황이면 제공하는 것이 좋다.

Q. 알림 없음에도 action이 필요해?
A. 보통은 필요 없지만 알림 설정으로 이동하는 action을 제공할 수 있다.

---

# 5. Skeleton Component Pattern

## 5.1 Skeleton Responsibility

### [개념]

Skeleton Component는 실제 데이터가 로딩되기 전 콘텐츠 구조를 예상 가능한 placeholder 형태로 보여주는 UI Component다.

Skeleton은 사용자가 레이아웃을 예측할 수 있게 하고, 짧은 로딩에서 체감 대기 시간을 줄이는 데 사용한다.

---

### [핵심]

Skeleton 기본 책임:

- 콘텐츠 구조 placeholder 제공
- text / image / card 형태 제공
- aria-hidden 처리 가능
- loading message와 함께 사용 가능
- 반복 skeleton 지원
- 실제 layout과 유사한 구조 유지

Skeleton 사용 대상:

- Card list loading
- Table row loading
- Profile loading
- Image loading
- Detail page loading
- Feed loading

주의:

- 실제 구조와 너무 다르면 혼란 발생
- 긴 로딩에는 message도 필요할 수 있음
- 중요한 상태 안내를 Skeleton만으로 대체하지 않음
- 지나치게 많은 Skeleton은 시각적 피로 유발
- prefers-reduced-motion 고려 가능

---

### [실무]

Skeleton 기본 예:

```tsx
type SkeletonProps = {
  width?: string;
  height?: string;
  rounded?: boolean;
  className?: string;
};

function Skeleton({
  width = "100%",
  height = "1rem",
  rounded = false,
  className = "",
}: SkeletonProps) {
  return (
    <span
      className={`skeleton ${rounded ? "skeleton-rounded" : ""} ${className}`}
      style={{ width, height }}
      aria-hidden="true"
    />
  );
}
```

Card Skeleton 예:

```tsx
function FestivalCardSkeleton() {
  return (
    <Card>
      <Skeleton height="160px" />
      <Skeleton width="70%" />
      <Skeleton width="40%" />
      <Skeleton width="30%" />
    </Card>
  );
}
```

List Skeleton 예:

```tsx
function FestivalListSkeleton() {
  return (
    <ul>
      {Array.from({ length: 6 }, (_, index) => (
        <li key={index}>
          <FestivalCardSkeleton />
        </li>
      ))}
    </ul>
  );
}
```

---

### [FAQ]

Q. Skeleton은 언제 써?
A. 콘텐츠 구조가 예측 가능하고 로딩 중에도 레이아웃을 미리 보여주고 싶을 때 사용한다.

Q. Skeleton만 있으면 LoadingState는 필요 없어?
A. 항상 그렇지는 않다. 긴 로딩이나 접근성 안내가 필요하면 LoadingState message를 함께 고려한다.

Q. Skeleton key로 index를 써도 돼?
A. 실제 데이터 목록이 아니라 고정 개수 placeholder라면 index 사용이 큰 문제가 되지 않는다.

---

## 5.2 Skeleton vs Spinner

### [개념]

Skeleton vs Spinner는 로딩 UI를 콘텐츠 구조 기반으로 보여줄지, 단순 처리 중 표시로 보여줄지 구분하는 기준이다.

Skeleton은 레이아웃 예측에 적합하고 Spinner는 짧은 처리 상태 표현에 적합하다.

---

### [핵심]

Skeleton 적합:

- 카드 목록
- 피드
- 테이블 행
- 상세 페이지 구조
- 이미지 영역
- 예측 가능한 layout

Spinner 적합:

- 버튼 작업
- 짧은 요청
- 작은 inline 영역
- 로딩 구조를 예측하기 어려운 경우
- 단순 처리 상태

비교:

| 기준   | Skeleton               | Spinner                    |
| ------ | ---------------------- | -------------------------- |
| 목적   | 레이아웃 예측          | 처리 중 표시               |
| 적합   | 목록 / 카드 / 상세     | 버튼 / 짧은 로딩           |
| 정보량 | 구조 제공              | 상태 제공                  |
| 접근성 | 별도 message 필요 가능 | role status와 message 권장 |
| 주의   | 실제 구조와 일치 필요  | 단독 사용 지양             |

---

### [실무]

Skeleton 적합 예:

```tsx
if (loading) {
  return <FestivalListSkeleton />;
}
```

Spinner 적합 예:

```tsx
<Button loading={saving}>저장</Button>
```

LoadingState 적합 예:

```tsx
if (loading && !hasKnownLayout) {
  return <LoadingState message="데이터를 불러오는 중입니다." />;
}
```

판단 Flow:

```text
콘텐츠 구조가 예측 가능한가?
→ Skeleton

짧은 작업 상태인가?
→ Spinner / Button loading

전체 화면 대기인가?
→ LoadingState

기존 콘텐츠가 있는 refetch인가?
→ Inline Loading
```

---

### [FAQ]

Q. Skeleton과 Spinner는 어떻게 구분해?
A. 콘텐츠 구조를 미리 보여줄 수 있으면 Skeleton, 단순 처리 중 상태를 보여주면 Spinner가 적합하다.

Q. 버튼 저장 중에는 Skeleton을 써?
A. 아니다. 버튼 저장 중에는 Button loading이나 spinner가 적합하다.

Q. 카드 목록 로딩에는 뭐가 좋아?
A. 카드 구조를 예측할 수 있다면 Skeleton이 사용자 경험에 좋다.

---

# 6. State UI Composition

## 6.1 Page State Composition

### [개념]

Page State Composition은 Page Component나 Feature Container가 loading, error, empty, success 상태를 판단하고 적절한 State UI Component를 조합하는 방식이다.

State UI Component는 상태를 표시하고, 상태 판단과 데이터 요청은 Page나 Hook이 담당한다.

---

### [핵심]

Page State 순서:

- loading
- error
- empty
- success

기본 Flow:

```text
loading && no data
→ LoadingState or Skeleton

error
→ ErrorState

success && empty
→ EmptyState

success && data
→ Data UI
```

주의:

- loading과 data가 함께 있으면 기존 데이터 유지 가능
- error와 stale data가 함께 있으면 inline error 고려
- empty는 요청 성공 후 데이터 없음
- error를 empty로 처리하지 않음
- empty를 error로 처리하지 않음

---

### [실무]

기본 Page Composition 예:

```tsx
function FestivalListPage() {
  const { data, loading, error, refetch } = useFestivals();

  if (loading && !data) {
    return <FestivalListSkeleton />;
  }

  if (error && !data) {
    return (
      <ErrorState
        fullPage
        message="축제 정보를 불러오지 못했습니다."
        onRetry={refetch}
      />
    );
  }

  if (data && data.length === 0) {
    return (
      <EmptyState
        title="축제 정보가 없습니다."
        description="검색 조건을 변경해 보세요."
      />
    );
  }

  return (
    <>
      {error && (
        <ErrorState
          message="최신 정보를 다시 불러오지 못했습니다."
          onRetry={refetch}
        />
      )}
      <FestivalList festivals={data ?? []} />
      {loading && <LoadingState message="최신 정보를 불러오는 중입니다." />}
    </>
  );
}
```

권장:

```text
초기 로딩
→ Skeleton or fullPage LoadingState

초기 실패
→ fullPage ErrorState

결과 없음
→ EmptyState

기존 데이터 refetch 실패
→ Inline ErrorState

기존 데이터 refetch 중
→ Inline LoadingState
```

---

### [FAQ]

Q. loading, error, empty 상태는 어떤 순서로 처리해?
A. 보통 초기 loading, error, empty, success 순서로 처리한다. stale data가 있으면 inline 상태를 고려한다.

Q. error가 있는데 기존 데이터도 있으면 어떻게 해?
A. 기존 데이터는 유지하고 inline ErrorState나 toast로 최신화 실패를 안내할 수 있다.

Q. empty는 언제 판단해?
A. 요청이 성공했고 데이터 배열이 비어 있을 때 EmptyState로 판단한다.

---

## 6.2 State UI with Action

### [개념]

State UI with Action은 ErrorState나 EmptyState에 사용자가 회복하거나 다음 행동을 할 수 있는 action을 제공하는 패턴이다.

Action은 Button, Link, ReactNode로 조합하는 것이 유연하다.

---

### [핵심]

Action 사용 대상:

- Error retry
- Filter reset
- Search reset
- Create item
- Login redirect
- Back to list
- Permission request
- Refresh

Action 설계 기준:

- action은 선택적
- 가능한 경우 구체적 텍스트 사용
- Retry 가능할 때만 Retry 제공
- EmptyState에는 다음 행동 권장
- action은 ReactNode로 받을 수 있음
- 실제 로직은 부모에서 처리
- Navigation action은 Link 또는 router handler 사용

---

### [실무]

EmptyState action 예:

```tsx
<EmptyState
  title="검색 결과가 없습니다."
  description="필터를 초기화하거나 다른 검색어를 입력해 보세요."
  action={
    <Button variant="secondary" onClick={resetFilter}>
      필터 초기화
    </Button>
  }
/>
```

ErrorState retry 예:

```tsx
<ErrorState
  message="목록을 불러오지 못했습니다."
  onRetry={refetch}
  retryText="다시 불러오기"
/>
```

Login action 예:

```tsx
<EmptyState
  title="로그인이 필요합니다."
  description="찜한 축제를 보려면 로그인해 주세요."
  action={<Button onClick={goToLogin}>로그인하기</Button>}
/>
```

---

### [FAQ]

Q. EmptyState action은 왜 ReactNode로 받아?
A. 버튼, 링크, 필터 초기화 등 다양한 다음 행동을 유연하게 넣기 위해서다.

Q. ErrorState action은 onRetry만 있으면 충분해?
A. 단순 재시도는 onRetry로 충분하지만 로그인 이동이나 목록 이동은 action ReactNode가 더 유연할 수 있다.

Q. State UI action 안에서 API 호출을 직접 해도 돼?
A. State UI Component가 직접 호출하지 말고 부모에서 전달한 callback을 실행하는 것이 좋다.

---

# 7. State UI Anti Pattern

## 7.1 State UI Common Mistakes

### [개념]

State UI Common Mistakes는 loading, error, empty 상태를 잘못 구분하거나 사용자에게 부정확한 상태를 보여주는 문제다.

State UI는 UX와 접근성에 직접 영향을 주므로 상태 구분이 명확해야 한다.

---

### [핵심]

자주 발생하는 실수:

- loading spinner만 표시하고 텍스트 없음
- empty 상태를 아무것도 표시하지 않음
- error를 empty로 처리
- empty를 error로 처리
- 서버 에러 원문 노출
- stack trace 노출
- Retry 불가능한 오류에 Retry 버튼 제공
- EmptyState에 다음 행동 없음
- Skeleton이 실제 layout과 다름
- 기존 데이터 refetch 중 전체 화면 loading 표시
- State UI 안에서 API 직접 호출
- role status / role alert 누락
- Button loading과 Page Loading 혼동

---

### [실무]

나쁜 예:

```tsx
if (loading) {
  return <Spinner />;
}

if (error) {
  return <div>{error.message}</div>;
}

if (data.length === 0) {
  return null;
}
```

문제점:

```text
loading message 없음
서버 에러 원문 노출 가능
empty 상태 사용자 안내 없음
접근성 role 없음
```

개선:

```tsx
if (loading) {
  return <LoadingState message="데이터를 불러오는 중입니다." />;
}

if (error) {
  return (
    <ErrorState message="데이터를 불러오지 못했습니다." onRetry={refetch} />
  );
}

if (data.length === 0) {
  return (
    <EmptyState
      title="표시할 데이터가 없습니다."
      description="조건을 변경하거나 다시 시도해 보세요."
    />
  );
}
```

---

### [FAQ]

Q. 빈 목록은 null로 처리해도 돼?
A. 권장하지 않는다. 사용자가 상태를 이해할 수 있도록 EmptyState를 제공하는 것이 좋다.

Q. 에러 메시지에 error.message를 그대로 보여줘도 돼?
A. 권장하지 않는다. 서버 내부 메시지나 민감 정보가 포함될 수 있어 사용자용 메시지로 변환해야 한다.

Q. 로딩 중 spinner만 보여줘도 돼?
A. 가능은 하지만 접근성과 사용자 이해를 위해 message와 role status를 함께 제공하는 것이 좋다.

---

## 7.2 State UI Review Checklist

### [개념]

State UI Review Checklist는 LoadingState, ErrorState, EmptyState, Skeleton이 적절히 설계되었는지 검수하는 기준이다.

Frontend Agent와 Review Agent는 데이터 요청 화면마다 상태 UI 누락 여부를 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] loading / error / empty / success 상태가 구분되었는가?
- [ ] LoadingState에 message가 있는가?
- [ ] LoadingState에 role status가 있는가?
- [ ] Page Loading과 Inline Loading이 구분되었는가?
- [ ] ErrorState에 사용자 친화 메시지가 있는가?
- [ ] 서버 에러 원문이 노출되지 않는가?
- [ ] ErrorState에 role alert가 있는가?
- [ ] Retry 가능 여부에 따라 action이 제공되는가?
- [ ] EmptyState가 null 대신 제공되는가?
- [ ] EmptyState에 title과 description이 있는가?
- [ ] EmptyState에 필요한 다음 action이 있는가?
- [ ] Search Empty와 First Use Empty가 구분되었는가?
- [ ] Skeleton이 실제 layout과 유사한가?
- [ ] Skeleton과 Spinner 사용 기준이 적절한가?
- [ ] 기존 데이터 refetch 중 전체 화면 loading을 남용하지 않는가?
- [ ] State UI Component가 API를 직접 호출하지 않는가?
- [ ] State UI action은 부모 callback을 실행하는가?
```

---

### [실무]

검수 Flow:

```text
Page Draft
→ Loading Check
→ Error Check
→ Empty Check
→ Success Check
→ Action Check
→ Accessibility Check
→ Anti Pattern Check
→ Final Review
```

치명적 문제:

```text
error를 empty로 처리
empty 상태 null 반환
서버 에러 원문 노출
stack trace 노출
LoadingState message 없음
State UI 내부 API 호출
Retry 불가능한 오류에 Retry 제공
접근성 role 누락
```

---

### [FAQ]

Q. State UI 검수에서 가장 중요한 것은 뭐야?
A. loading, error, empty, success 상태가 명확히 구분되고 사용자에게 다음 행동이 제공되는지 확인하는 것이다.

Q. State UI에서 치명적인 문제는 뭐야?
A. 서버 에러 원문 노출, empty 상태 null 처리, error와 empty 혼동, State UI 내부 API 호출이 치명적이다.

Q. Review Agent는 State UI를 어떻게 검토해야 해?
A. 상태 구분, 메시지, action, 접근성 role, API 호출 위치, Skeleton 사용 기준을 순서대로 확인해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. State UI Component는 왜 필요해?
A. Loading, Error, Empty 상태를 일관되게 보여주고 사용자가 다음 행동을 이해하게 만들기 위해 필요하다.

Q. LoadingState, ErrorState, EmptyState는 어디에서 조합해?
A. 보통 Page나 Feature Container에서 데이터 상태를 판단한 뒤 조합한다.

Q. State UI Component 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. Retry 이벤트만 외부로 전달하고 실제 API 호출은 Page나 Hook에서 처리하는 것이 좋다.

Q. LoadingState Component는 어떻게 설계해?
A. message, fullPage, role status, aria-live, spinner, className 기준으로 설계한다.

Q. LoadingState에는 텍스트가 필요해?
A. 접근성과 사용자 이해를 위해 짧은 loading message를 제공하는 것이 좋다.

Q. 모든 로딩에 같은 LoadingState를 써도 돼?
A. 가능하지만 페이지 로딩, 버튼 로딩, 하단 더보기 로딩은 크기와 위치가 다를 수 있다.

Q. LoadingState에 role status를 쓰는 이유는?
A. 보조기술이 현재 화면이 처리 중임을 사용자에게 알릴 수 있게 하기 위해서다.

Q. Page Loading과 Inline Loading은 어떻게 구분해?
A. 화면 전체가 준비되지 않았으면 Page Loading, 기존 콘텐츠가 있고 일부 영역만 처리 중이면 Inline Loading이 적합하다.

Q. 데이터가 이미 있는데 refetch 중이면 전체 LoadingState를 보여줘야 해?
A. 보통 기존 콘텐츠를 유지하고 Inline Loading이나 refresh indicator를 보여주는 것이 좋다.

Q. Button 클릭 처리 중에도 LoadingState를 써?
A. 버튼 내부 처리 중이면 Button의 loading prop을 사용하는 것이 더 적합하다.

Q. ErrorState Component는 어떻게 설계해?
A. title, message, onRetry, retryText, role alert, fullPage 기준으로 설계한다.

Q. ErrorState에는 항상 Retry 버튼이 있어야 해?
A. 아니다. 재시도 가능한 오류에만 제공하는 것이 좋다.

Q. 서버 에러 원문을 ErrorState에 그대로 넣어도 돼?
A. 권장하지 않는다. 사용자용 메시지로 변환하는 것이 안전하다.

Q. ErrorState와 EmptyState는 뭐가 달라?
A. ErrorState는 요청 실패 상태이고 EmptyState는 요청 성공 후 데이터가 없는 상태다.

Q. 서버 에러 코드를 그대로 보여줘도 돼?
A. 상태 코드를 참고할 수는 있지만 사용자에게는 이해 가능한 메시지로 변환하는 것이 좋다.

Q. 401 오류는 어떻게 보여줘?
A. 로그인이 필요하다는 안내와 로그인 이동 action을 제공할 수 있다.

Q. 500 오류는 어떻게 보여줘?
A. 서버 문제 안내와 잠시 후 재시도 메시지를 제공하는 것이 좋다.

Q. EmptyState Component는 어떻게 설계해?
A. title, description, action, icon, variant를 기준으로 데이터 없음의 이유와 다음 행동을 제공한다.

Q. EmptyState에는 뭘 넣어야 해?
A. 데이터가 없다는 안내, 이유, 사용자가 할 수 있는 다음 행동을 넣는 것이 좋다.

Q. 목록이 비어 있으면 그냥 아무것도 안 보여줘도 돼?
A. 권장하지 않는다. EmptyState를 보여주는 것이 사용자 경험에 좋다.

Q. 검색 결과 없음과 첫 사용 EmptyState는 다르게 써야 해?
A. 다르게 쓰는 것이 좋다. 검색 결과 없음은 검색어 변경이나 필터 초기화를 안내하고, 첫 사용 상태는 생성이나 탐색을 안내한다.

Q. EmptyState action은 항상 필요해?
A. 항상 필요하지는 않지만 사용자가 다음 행동을 취할 수 있는 상황이면 제공하는 것이 좋다.

Q. 알림 없음에도 action이 필요해?
A. 보통은 필요 없지만 알림 설정으로 이동하는 action을 제공할 수 있다.

Q. Skeleton은 언제 써?
A. 콘텐츠 구조가 예측 가능하고 로딩 중에도 레이아웃을 미리 보여주고 싶을 때 사용한다.

Q. Skeleton만 있으면 LoadingState는 필요 없어?
A. 항상 그렇지는 않다. 긴 로딩이나 접근성 안내가 필요하면 LoadingState message를 함께 고려한다.

Q. Skeleton key로 index를 써도 돼?
A. 실제 데이터 목록이 아니라 고정 개수 placeholder라면 index 사용이 큰 문제가 되지 않는다.

Q. Skeleton과 Spinner는 어떻게 구분해?
A. 콘텐츠 구조를 미리 보여줄 수 있으면 Skeleton, 단순 처리 중 상태를 보여주면 Spinner가 적합하다.

Q. 버튼 저장 중에는 Skeleton을 써?
A. 아니다. 버튼 저장 중에는 Button loading이나 spinner가 적합하다.

Q. 카드 목록 로딩에는 뭐가 좋아?
A. 카드 구조를 예측할 수 있다면 Skeleton이 사용자 경험에 좋다.

Q. loading, error, empty 상태는 어떤 순서로 처리해?
A. 보통 초기 loading, error, empty, success 순서로 처리한다. stale data가 있으면 inline 상태를 고려한다.

Q. error가 있는데 기존 데이터도 있으면 어떻게 해?
A. 기존 데이터는 유지하고 inline ErrorState나 toast로 최신화 실패를 안내할 수 있다.

Q. empty는 언제 판단해?
A. 요청이 성공했고 데이터 배열이 비어 있을 때 EmptyState로 판단한다.

Q. EmptyState action은 왜 ReactNode로 받아?
A. 버튼, 링크, 필터 초기화 등 다양한 다음 행동을 유연하게 넣기 위해서다.

Q. ErrorState action은 onRetry만 있으면 충분해?
A. 단순 재시도는 onRetry로 충분하지만 로그인 이동이나 목록 이동은 action ReactNode가 더 유연할 수 있다.

Q. State UI action 안에서 API 호출을 직접 해도 돼?
A. State UI Component가 직접 호출하지 말고 부모에서 전달한 callback을 실행하는 것이 좋다.

Q. 빈 목록은 null로 처리해도 돼?
A. 권장하지 않는다. 사용자가 상태를 이해할 수 있도록 EmptyState를 제공하는 것이 좋다.

Q. 에러 메시지에 error.message를 그대로 보여줘도 돼?
A. 권장하지 않는다. 서버 내부 메시지나 민감 정보가 포함될 수 있어 사용자용 메시지로 변환해야 한다.

Q. 로딩 중 spinner만 보여줘도 돼?
A. 가능은 하지만 접근성과 사용자 이해를 위해 message와 role status를 함께 제공하는 것이 좋다.

Q. State UI 검수에서 가장 중요한 것은 뭐야?
A. loading, error, empty, success 상태가 명확히 구분되고 사용자에게 다음 행동이 제공되는지 확인하는 것이다.

Q. State UI에서 치명적인 문제는 뭐야?
A. 서버 에러 원문 노출, empty 상태 null 처리, error와 empty 혼동, State UI 내부 API 호출이 치명적이다.

Q. Review Agent는 State UI를 어떻게 검토해야 해?
A. 상태 구분, 메시지, action, 접근성 role, API 호출 위치, Skeleton 사용 기준을 순서대로 확인해야 한다.
