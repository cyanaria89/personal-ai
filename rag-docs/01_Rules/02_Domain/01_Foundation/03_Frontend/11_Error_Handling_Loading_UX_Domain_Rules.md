# Error Handling & Loading UX Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

Error Handling & Loading UX Domain 문서는 Frontend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- Frontend 오류 처리 기준 제공
- Loading / Error / Empty / Success 상태 구분 지원
- API 요청 상태별 UI 설계 지원
- 사용자 친화적 오류 메시지 작성 기준 제공
- Retry / Refetch / Fallback UI 기준 제공
- Error Boundary 적용 판단 기준 제공
- Form Error / API Error / Route Error 구분 지원
- 인증 오류 401 / 권한 오류 403 처리 기준 제공
- Network Error / Server Error / Validation Error 구분 지원
- Skeleton / Spinner / Disabled Button 사용 기준 제공
- TanStack Query 상태값 사용 기준 제공
- 유지보수 가능한 상태 UX 구조 설계 지원

---

### [핵심]

우선순위:

1. Loading State
2. Error State
3. Empty State
4. Success State
5. API Error Handling
6. Validation Error
7. Network Error
8. Retry UX
9. Error Boundary
10. Fallback UI
11. Skeleton UI
12. Disabled State
13. Toast / Alert
14. TanStack Query Status
15. 401 / 403 / 404 / 500 UX
16. User Message
17. Troubleshooting

---

### [실무]

2026 실무 기준에서 Error Handling & Loading UX 문서는 단순 에러 출력 문서가 아니다.

Frontend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- API 요청 상태를 UI 상태로 변환
- Loading / Error / Empty / Success 상태를 분리
- 사용자에게 이해 가능한 오류 메시지 제공
- 개발자 로그와 사용자 메시지 구분
- 재시도 가능한 오류와 불가능한 오류 구분
- 인증 오류와 권한 오류 구분
- Form Field Error와 Global Error 구분
- 페이지 단위 Error UI 설계
- Component 단위 Fallback UI 설계
- Error Boundary 적용 여부 판단
- TanStack Query의 isLoading / isFetching / isError / error 처리
- UX flicker / 중복 로딩 / 무한 로딩 문제 검토

---

### [FAQ]

Q. Error Handling & Loading UX 문서는 Data Fetching과 뭐가 달라?

A.
Data Fetching은 API 요청 구조와 응답 처리 중심이고 Error Handling & Loading UX는 요청 결과를 사용자 경험 상태로 표현하는 기준에 집중한다.

Q. Error Handling에서 가장 중요한 기준은 뭐야?

A.
Loading, Error, Empty, Success 상태를 구분하고 사용자 메시지와 개발자 로그를 분리하는 것이다.

Q. 에러가 나면 그냥 alert로 보여주면 안 돼?

A.
간단한 실습은 가능하지만 실무에서는 화면 위치, 오류 종류, 재시도 가능 여부, 접근성을 고려해 메시지를 설계하는 것이 좋다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Error Handling & Loading UX 문서는 Frontend 오류 처리와 상태 UX 설계에 필요한 범위를 포함한다.

포함 범위:

- Loading State
- Initial Loading
- Refetch Loading
- Submit Loading
- Pagination Loading
- Infinite Scroll Loading
- Skeleton UI
- Spinner
- Disabled Button
- Error State
- API Error
- Network Error
- Server Error
- Validation Error
- Auth Error
- Permission Error
- Not Found Error
- Empty State
- Success State
- Toast
- Alert
- Inline Error
- Page Error
- Error Boundary
- Fallback UI
- Retry Button
- Refetch UX
- TanStack Query Status
- useQuery Error Handling
- useMutation Error Handling
- 400 / 401 / 403 / 404 / 409 / 422 / 500 UX
- Error Message Mapping
- Error Logging Basics
- UX Flicker Prevention
- Infinite Loading Troubleshooting

---

### [핵심]

반드시 포함:

- Loading State와 Empty State를 혼동하지 않음
- Error State와 Empty State를 혼동하지 않음
- 사용자 메시지와 개발자 로그를 분리
- 401 / 403 / 404 / 500 상태별 UX를 구분
- Validation Error는 Field Error와 Global Error로 분리
- Submit Loading으로 중복 제출 방지
- Retry 가능 오류에는 재시도 액션 제공 가능
- Error Boundary는 렌더링 오류 대응용이며 API 실패 처리와 다름
- Skeleton과 Spinner는 상황에 맞게 선택
- TanStack Query 상태값을 정확히 구분
- 무한 로딩 / 깜빡임 / stale UI 문제를 검토

---

### [실무]

Error Handling & Loading UX는 Data Fetching, Form Handling, Authentication Flow 뒤에서 사용자 경험을 완성한다.

실무 연결:

```text
Data Fetching
→ API Status
→ Loading / Error / Empty / Success
→ User Message
→ Retry / Redirect / Fallback
→ UX Review
```

---

### [FAQ]

Q. Error Boundary도 여기서 다뤄?

A.
기초 적용 기준은 포함한다. React Error Boundary 심화와 로깅 시스템 연동은 Advanced Frontend Error 문서에서 다룬다.

Q. Toast UI도 여기서 다뤄?

A.
기본 사용 기준은 포함한다. 디자인 시스템 수준의 Toast 컴포넌트 설계는 UI Design System 문서에서 다룬다.

Q. API 에러와 렌더링 에러를 같이 처리해도 돼?

A.
역할이 다르다. API 에러는 요청 실패 상태로 처리하고 렌더링 에러는 Error Boundary로 처리하는 것이 일반적이다.

---

## 2.2 Excluded Scope

### [개념]

Error Handling & Loading UX 문서에서는 고급 모니터링과 복잡한 장애 대응 시스템을 제외한다.

제외 범위:

- Sentry / Datadog / LogRocket 심화
- Observability Architecture
- Distributed Tracing
- Backend Exception Handling 심화
- Global Error Reporting Pipeline
- Advanced Error Boundary Architecture
- React Suspense 심화
- Streaming UI 심화
- Offline-first Error Recovery
- Service Worker Retry Queue
- Complex Optimistic Rollback
- Real-time Error Recovery
- Payment Failure Recovery 심화
- Accessibility Full Audit 심화

---

### [핵심]

제외 이유:

- Foundation 범위 초과
- Frontend Monitoring / Advanced React / Backend Exception 문서와 분리 필요
- Agent Retrieval 혼선 방지
- Chunk 품질 유지
- 일반적인 Frontend 상태 UX 처리에 집중

---

### [실무]

고급 기술은 별도 Domain Rules에서 관리한다.

예:

```text
Error Handling & Loading UX
→ Frontend Accessibility
→ Frontend Testing
→ Advanced Error Boundary
→ Frontend Monitoring
```

---

### [FAQ]

Q. Sentry 연동도 여기서 다뤄?

A.
기초 언급은 가능하지만 Sentry 설정, release tracking, source map upload 등은 Frontend Monitoring 문서에서 다룬다.

Q. Backend 예외 처리도 여기서 다뤄?

A.
아니다. Backend Exception Handling은 Backend API 또는 Spring Boot 문서에서 다룬다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

Error Handling & Loading UX RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

Required:

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

### [핵심]

필수 Section 목적:

- [개념]: 정의와 역할
- [핵심]: 검색 친화 키워드
- [실무]: 실제 UX 적용 기준
- [FAQ]: 사용자 질문 매칭 강화

---

### [실무]

각 문서는 아래 구조를 기본으로 한다.

```md
# Topic

## Sub Topic

### [개념]

### [핵심]

### [실무]

### [FAQ]
```

---

### [FAQ]

Q. 모든 Error Handling 문서에 FAQ가 필요해?

A.
필요하다. FAQ는 사용자 질문과 RAG 검색 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

Error Handling & Loading UX 문서에는 상태 흐름과 오류 검증을 위해 추가 Section을 포함할 수 있다.

Strongly Recommended:

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

### [핵심]

추천 Section 사용 기준:

- Loading Flow 설명 → [Flow], [예제]
- Error Message 설계 → [Best Practice], [주의]
- API Error 처리 → [Troubleshooting]
- Empty State 처리 → [예제]
- Error Boundary 설명 → [Comparison], [주의]
- TanStack Query 상태 설명 → [Comparison], [예제]

---

### [실무]

예시:

```md
### [Flow]

API Request Start
→ Show Loading
→ Success
→ If Data Empty Show Empty State
→ If Data Exists Show Content
→ If Failed Show Error State
→ Provide Retry if Possible
```

---

### [FAQ]

Q. Error Handling 문서에 Troubleshooting이 중요한 이유는?

A.
무한 로딩, 빈 화면, 에러 메시지 미표시, 401/403 혼동, 응답 구조 불일치 같은 문제가 자주 발생하기 때문이다.

Q. Comparison은 언제 쓰면 좋아?

A.
Loading vs Empty, Error Boundary vs API Error, Spinner vs Skeleton, isLoading vs isFetching처럼 헷갈리는 개념을 비교할 때 사용한다.

---

# 4. UI State Classification Rules

## 4.1 Loading / Error / Empty / Success

### [개념]

API 기반 화면은 보통 Loading, Error, Empty, Success 상태 중 하나로 표현된다.

이 상태들을 명확히 구분해야 사용자가 현재 상황을 이해할 수 있다.

---

### [핵심]

상태 구분:

| 상태    | 의미                   | 예                       |
| ------- | ---------------------- | ------------------------ |
| Loading | 요청 진행 중           | 축제 목록 불러오는 중    |
| Error   | 요청 실패              | 서버 오류, 네트워크 오류 |
| Empty   | 요청 성공, 데이터 없음 | 검색 결과 없음           |
| Success | 요청 성공, 데이터 있음 | 목록 표시                |

---

### [실무]

기본 렌더링 순서:

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

권장:

- Loading과 Empty를 분리
- Error와 Empty를 분리
- 성공했지만 데이터가 없으면 Empty
- 실패했으면 Error
- 초기값이 빈 배열이라는 이유로 바로 Empty를 보여주지 않음
- 상태 판정 순서 통일

---

### [FAQ]

Q. Loading State와 Empty State 차이는?

A.
Loading은 요청 중인 상태이고 Empty는 요청이 성공했지만 표시할 데이터가 없는 상태다.

Q. Error State와 Empty State 차이는?

A.
Error는 요청 실패이고 Empty는 요청 성공 후 데이터가 없는 상태다.

Q. 초기 배열이 빈 배열이면 바로 Empty를 보여줘도 돼?

A.
요청 전인지 요청 완료 후인지 구분해야 한다. 요청 중에는 Loading을 보여주는 것이 좋다.

---

## 4.2 Status Modeling Rules

### [개념]

Status Modeling은 loading, error, success 같은 상태를 명확한 상태값으로 모델링하는 방식이다.

boolean 상태가 많아질 때 유용하다.

---

### [핵심]

상태 후보:

- idle
- loading
- success
- error
- empty
- submitting
- refetching

---

### [실무]

예:

```typescript
type RequestStatus = "idle" | "loading" | "success" | "error";

type RequestState<T> = {
  status: RequestStatus;
  data: T | null;
  errorMessage: string;
};
```

사용 예:

```tsx
if (state.status === "loading") {
  return <LoadingState />;
}

if (state.status === "error") {
  return <ErrorState message={state.errorMessage} />;
}
```

권장:

- boolean 여러 개가 충돌하면 status union 사용
- `loading=true`와 `error=true`가 동시에 되는 구조 방지
- idle 상태와 loading 상태 구분
- submit status와 page loading status 분리
- 상태 전환 흐름 명확화

---

### [FAQ]

Q. loading, error boolean을 따로 두면 안 돼?

A.
가능하다. 하지만 상태가 많아져 서로 충돌하면 status 문자열이나 reducer로 모델링하는 것이 더 안전하다.

Q. idle 상태는 왜 필요해?

A.
아직 요청을 시작하지 않은 상태와 요청 중인 상태를 구분하기 위해 필요하다.

---

# 5. Loading UX Rules

## 5.1 Initial Loading Rules

### [개념]

Initial Loading은 화면이 처음 렌더링되면서 필요한 데이터를 불러오는 상태다.

사용자가 빈 화면을 오류로 오해하지 않도록 명확한 Loading UI를 제공한다.

---

### [핵심]

사용 상황:

- page mount data fetch
- route param based fetch
- user profile fetch
- auth restore
- initial list fetch
- detail page fetch

---

### [실무]

예:

```jsx
function PageLoading() {
  return (
    <section aria-busy="true">
      <p>데이터를 불러오는 중입니다.</p>
    </section>
  );
}
```

권장:

- 페이지 단위 로딩은 화면 중앙 또는 콘텐츠 영역에 표시
- 사용자가 기다려야 하는 이유를 짧게 설명
- 너무 짧은 로딩에는 flicker 방지 고려
- 핵심 layout은 유지하고 content 영역만 loading 처리 가능
- 인증 초기화 loading과 데이터 loading을 구분

주의:

- Loading UI 없이 빈 화면 방치 금지
- 초기 데이터가 없다는 이유로 즉시 Empty 표시 금지
- 무한 로딩 방지를 위해 error / timeout 처리 필요

---

### [FAQ]

Q. 페이지 처음 들어갔을 때 빈 화면이 보여도 돼?

A.
권장하지 않는다. 데이터 요청 중이면 Loading UI를 보여주는 것이 좋다.

Q. auth loading과 page loading은 같아?

A.
다르다. auth loading은 인증 상태 확인이고 page loading은 화면 데이터 조회 상태다.

---

## 5.2 Refetch Loading Rules

### [개념]

Refetch Loading은 이미 데이터가 있는 상태에서 최신 데이터를 다시 가져오는 상태다.

Initial Loading과 다르게 기존 데이터를 유지하면서 작은 갱신 표시를 보여줄 수 있다.

---

### [핵심]

사용 상황:

- pull to refresh
- filter change
- background refetch
- window focus refetch
- manual refresh
- stale data update

---

### [실무]

TanStack Query 기준:

```tsx
const { data, isLoading, isFetching } = useQuery({
  queryKey: ["festivals", params],
  queryFn: () => getFestivals(params),
});
```

UX 기준:

```text
isLoading true → 초기 로딩 UI
isFetching true + data exists → 기존 데이터 유지 + 작은 갱신 표시
```

권장:

- 기존 데이터가 있으면 전체 화면 loading으로 덮지 않음
- 새로고침 중임을 작은 spinner나 text로 표시
- 필터 변경으로 완전히 다른 데이터라면 skeleton 고려
- stale data 표시 기준 결정
- 사용자가 작업 중인 입력값을 방해하지 않음

---

### [FAQ]

Q. isLoading과 isFetching은 뭐가 달라?

A.
isLoading은 주로 초기 데이터가 없는 로딩이고 isFetching은 데이터 재조회 중에도 true가 될 수 있다.

Q. 재조회할 때 기존 데이터를 지워야 해?

A.
항상 지울 필요는 없다. 기존 데이터를 유지하면서 갱신 표시를 보여주는 것이 더 자연스러운 경우가 많다.

---

## 5.3 Submit Loading Rules

### [개념]

Submit Loading은 Form 제출, 저장, 삭제, 좋아요, 찜 같은 사용자 액션 요청이 처리 중인 상태다.

중복 요청을 방지하고 사용자가 처리 중임을 알 수 있게 한다.

---

### [핵심]

사용 상황:

- login submit
- signup submit
- review create
- profile update
- delete request
- like request
- favorite request
- payment request

---

### [실무]

예:

```jsx
function SubmitButton({ submitting }) {
  return (
    <button type="submit" disabled={submitting}>
      {submitting ? "처리 중..." : "저장"}
    </button>
  );
}
```

권장:

- 제출 중 버튼 disabled
- 버튼 문구 변경
- 중복 클릭 방지
- 실패 시 다시 제출 가능하게 복구
- 성공 후 reset / redirect / refetch 기준 명확화
- 요청이 중요한 경우 Backend 중복 방지 필요

주의:

- disabled만으로 보안이나 중복 처리가 완전하지 않음
- 삭제 / 결제 / 후원 같은 요청은 서버 중복 방지 필수
- submit loading과 page loading을 구분

---

### [FAQ]

Q. 제출 중 버튼을 disabled 해야 해?

A.
권장한다. 중복 제출을 줄이고 사용자가 처리 중임을 이해할 수 있다.

Q. submit loading과 initial loading은 달라?

A.
다르다. submit loading은 사용자 액션 처리 중이고 initial loading은 화면 데이터 초기 조회 중이다.

---

## 5.4 Pagination and Infinite Loading Rules

### [개념]

Pagination Loading은 페이지 번호 변경 시 발생하는 로딩이고 Infinite Loading은 더보기나 무한 스크롤에서 다음 데이터를 가져오는 상태다.

---

### [핵심]

사용 상황:

- page change
- load more
- infinite scroll
- next cursor
- hasNext
- isFetchingNextPage
- duplicate request prevention
- append loading

---

### [실무]

Load More 버튼 예:

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

권장:

- 다음 페이지 요청 중 중복 요청 방지
- 기존 목록 유지 후 하단에 loading 표시
- hasNext가 false면 더보기 버튼 숨김
- 검색 조건 변경 시 목록 초기화
- 실패 시 다시 시도 버튼 제공
- Skeleton보다 하단 spinner가 적합한 경우 많음

---

### [FAQ]

Q. 무한 스크롤에서 로딩은 어디에 보여줘?

A.
보통 기존 목록은 유지하고 하단에 다음 데이터를 불러오는 표시를 보여준다.

Q. 더보기 버튼을 여러 번 누르면 중복 요청이 나가?

A.
loading 중 disabled 처리를 하지 않으면 중복 요청이 발생할 수 있다.

---

# 6. Skeleton / Spinner Rules

## 6.1 Skeleton UI Rules

### [개념]

Skeleton UI는 실제 콘텐츠가 들어올 자리의 형태를 미리 보여주는 Loading UI다.

목록, 카드, 상세 화면처럼 레이아웃이 예측 가능한 경우에 적합하다.

---

### [핵심]

사용 대상:

- card list
- detail page
- profile area
- table row
- image grid
- content placeholder

---

### [실무]

권장 상황:

```text
콘텐츠 구조가 명확함
→ 사용자가 레이아웃을 예측 가능
→ Skeleton UI 적합
```

예:

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

주의:

- skeleton은 실제 콘텐츠 구조와 비슷해야 함
- 너무 많은 skeleton animation은 부담 가능
- 접근성상 장식 요소는 aria-hidden 고려
- loading message와 함께 사용할 수 있음
- 짧은 요청에는 과할 수 있음

---

### [FAQ]

Q. Skeleton UI는 언제 써?

A.
카드 목록이나 상세 페이지처럼 콘텐츠 구조가 예측 가능할 때 적합하다.

Q. Skeleton이 Spinner보다 항상 좋아?

A.
아니다. 짧은 요청이나 단순 액션에는 Spinner나 버튼 loading이 더 적합할 수 있다.

---

## 6.2 Spinner Rules

### [개념]

Spinner는 작업이 진행 중임을 간단히 표시하는 Loading UI다.

처리 시간이 짧거나 콘텐츠 구조를 예측하기 어려운 경우에 사용할 수 있다.

---

### [핵심]

사용 대상:

- submit button
- small area loading
- modal action
- unknown wait time
- refresh indicator
- load more indicator

---

### [실무]

예:

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

권장:

- 접근성 label 제공
- 버튼 내부 spinner에는 문구도 함께 제공
- 화면 전체를 막을지 부분만 표시할지 결정
- 무한 spinner 방지
- 사용자가 취소할 수 있는 긴 작업인지 검토

주의:

- Spinner만 오래 표시되면 사용자 불안 증가
- 가능하면 상태 메시지 제공
- 실패 가능성이 있는 요청에는 error fallback 필요

---

### [FAQ]

Q. Spinner에는 텍스트가 꼭 필요해?

A.
접근성을 위해 진행 상태를 설명하는 텍스트나 aria label을 제공하는 것이 좋다.

Q. Spinner가 계속 돌면 어떻게 해?

A.
요청 완료, 실패, finally 처리, timeout, dependency loop를 확인해야 한다.

---

## 6.3 Skeleton vs Spinner

### [개념]

Skeleton과 Spinner는 모두 Loading UI지만 적합한 상황이 다르다.

---

### [핵심]

비교:

| 비교 | Skeleton         | Spinner                    |
| ---- | ---------------- | -------------------------- |
| 목적 | 콘텐츠 자리 예측 | 처리 중 표시               |
| 적합 | 목록, 카드, 상세 | 버튼, 작은 영역, 짧은 작업 |
| 장점 | 레이아웃 안정감  | 구현 간단                  |
| 단점 | 구현 비용        | 오래 보이면 답답함         |
| 예   | 카드 목록 로딩   | 저장 버튼 처리 중          |

---

### [실무]

선택 기준:

```text
콘텐츠 레이아웃이 명확하고 초기 로딩 → Skeleton
사용자 액션 처리 중 → Button Loading / Spinner
기존 데이터 재조회 → 작은 Spinner
무한 스크롤 다음 페이지 → 하단 Spinner
```

---

### [FAQ]

Q. 목록 로딩에는 Skeleton이 좋아 Spinner가 좋아?

A.
카드나 테이블 구조가 명확하면 Skeleton이 좋고 단순한 경우에는 Spinner도 가능하다.

Q. 저장 버튼에는 Skeleton을 써?

A.
아니다. 저장 버튼에는 disabled 상태와 버튼 내부 loading 문구 또는 spinner가 적합하다.

---

# 7. Error State Rules

## 7.1 API Error State

### [개념]

API Error State는 서버 요청이 실패했을 때 사용자에게 실패 상황을 알려주는 상태다.

---

### [핵심]

처리 대상:

- network error
- timeout
- 400 bad request
- 401 unauthorized
- 403 forbidden
- 404 not found
- 409 conflict
- 422 validation error
- 500 server error

---

### [실무]

예:

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

권장:

- 오류 원인별 사용자 메시지 제공
- 재시도 가능한 오류는 Retry 버튼 제공
- 권한 문제는 로그인 / 권한 안내로 연결
- Not Found는 별도 안내 가능
- 서버 내부 오류 메시지는 그대로 노출하지 않음
- 개발 로그는 console 또는 monitoring으로 분리

---

### [FAQ]

Q. API 에러는 어떻게 보여줘?

A.
사용자가 이해할 수 있는 메시지와 필요한 경우 다시 시도 버튼을 제공한다.

Q. 서버 에러 원문을 그대로 보여줘도 돼?

A.
권장하지 않는다. 내부 정보가 포함될 수 있으므로 사용자용 메시지로 변환하는 것이 좋다.

---

## 7.2 Error Message Mapping

### [개념]

Error Message Mapping은 API 에러 객체나 HTTP Status Code를 사용자에게 보여줄 메시지로 변환하는 작업이다.

---

### [핵심]

Mapping 대상:

- status code
- error code
- server message
- validation errors
- network error
- timeout
- unknown error
- user-friendly message

---

### [실무]

예:

```typescript
export function getApiErrorMessage(error: unknown): string {
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

- 공통 에러 메시지 함수 제공
- 화면별 상세 메시지 override 가능
- field error와 global error 구분
- 서버 message 사용 여부 기준 마련
- unknown error fallback 제공

---

### [FAQ]

Q. 에러 메시지 mapping 함수는 왜 필요해?

A.
API 에러 구조를 화면마다 직접 해석하면 중복이 생기고 메시지 기준이 달라질 수 있기 때문이다.

Q. 서버 message를 항상 사용해도 돼?

A.
서비스 정책에 따라 다르다. 내부 정보가 포함될 수 있으면 사용자용 메시지로 변환해야 한다.

---

## 7.3 Network Error Rules

### [개념]

Network Error는 서버가 응답을 주지 못했거나 브라우저가 요청을 완료하지 못한 상태다.

HTTP 400 / 500 응답과 구분해야 한다.

---

### [핵심]

원인:

- internet disconnected
- server down
- DNS problem
- CORS failure
- timeout
- request blocked
- mixed content
- wrong baseURL

---

### [실무]

UX 기준:

```text
Network Error
→ "네트워크 연결을 확인해 주세요."
→ Retry Button
→ Offline 안내 가능
```

Debug 기준:

```text
Network 탭 확인
→ 요청 발생 여부 확인
→ status code 존재 여부 확인
→ CORS message 확인
→ baseURL 확인
→ 서버 실행 여부 확인
```

주의:

- Network Error와 500 Server Error를 구분
- CORS Error도 브라우저에서는 Network Error처럼 보일 수 있음
- Postman 성공과 Browser 성공은 다름
- 사용자가 해결할 수 있는 메시지와 개발자가 확인할 메시지 구분

---

### [FAQ]

Q. Network Error와 500 에러는 달라?

A.
다르다. Network Error는 응답 자체를 받지 못한 경우이고 500은 서버가 응답한 내부 오류다.

Q. Postman에서는 되는데 브라우저에서는 Network Error가 나?

A.
CORS, mixed content, 브라우저 보안 정책 문제일 수 있다.

---

# 8. HTTP Status UX Rules

## 8.1 400 / 422 Validation UX

### [개념]

400 Bad Request와 422 Unprocessable Entity는 요청 값이 잘못되었거나 검증에 실패했을 때 사용될 수 있다.

Frontend는 이를 Form Field Error 또는 Global Error로 표시한다.

---

### [핵심]

처리 대상:

- required missing
- invalid format
- length violation
- duplicate email
- invalid rating
- invalid date range
- validation response
- field errors

---

### [실무]

응답 예:

```json
{
  "success": false,
  "message": "검증 실패",
  "errors": {
    "email": "이미 사용 중인 이메일입니다.",
    "password": "비밀번호는 8자 이상이어야 합니다."
  }
}
```

UX 기준:

- field error는 input 근처 표시
- global error는 form 상단 표시
- 입력값 유지
- 사용자가 수정 가능한 메시지 제공
- submit loading 해제
- 첫 에러 field focus 고려

---

### [FAQ]

Q. Validation Error는 alert로만 보여줘도 돼?

A.
권장하지 않는다. 필드별 오류는 해당 input 근처에 보여주는 것이 사용자가 수정하기 쉽다.

Q. 서버 검증 실패 후 입력값은 지워야 해?

A.
보통 지우지 않는다. 사용자가 오류를 수정할 수 있도록 유지하는 것이 좋다.

---

## 8.2 401 Unauthorized UX

### [개념]

401 Unauthorized는 인증되지 않았거나 access token이 유효하지 않을 때 발생한다.

---

### [핵심]

원인:

- not logged in
- access token missing
- access token expired
- invalid token
- Authorization Header missing
- refresh failed

---

### [실무]

UX 기준:

```text
401 발생
→ refresh 가능하면 token refresh
→ refresh 성공 시 원래 요청 재시도
→ refresh 실패 시 auth state clear
→ login redirect
→ 필요한 경우 "로그인이 필요합니다." 메시지 표시
```

주의:

- 로그인 실패 401과 세션 만료 401 구분
- 무조건 alert 반복 금지
- Protected Route와 연동
- redirect loop 방지
- 원래 위치 저장 가능

---

### [FAQ]

Q. 401이면 무조건 로그인 페이지로 보내?

A.
refresh token flow가 있으면 먼저 재발급을 시도할 수 있다. 재발급 실패 시 로그인 페이지로 이동한다.

Q. 로그인 실패도 401이야?

A.
Backend 설계에 따라 가능하다. 로그인 실패 401과 기존 인증 만료 401의 UX를 구분해야 한다.

---

## 8.3 403 Forbidden UX

### [개념]

403 Forbidden은 인증은 되었지만 권한이 부족해 요청이 거부된 상태다.

---

### [핵심]

원인:

- role insufficient
- not owner
- admin only
- resource forbidden
- backend authorization failed

---

### [실무]

UX 기준:

```text
403 발생
→ auth state 유지
→ 권한 없음 메시지 표시
→ forbidden page 이동 가능
→ 이전 페이지 이동 버튼 제공 가능
```

예:

```jsx
function ForbiddenPage() {
  return (
    <main>
      <h1>접근 권한이 없습니다.</h1>
      <Link to="/">메인으로 이동</Link>
    </main>
  );
}
```

주의:

- 403에서 기본적으로 logout하지 않음
- login redirect와 구분
- 내부 권한 정책을 과도하게 노출하지 않음
- role 정보 stale 여부 확인 가능

---

### [FAQ]

Q. 403이면 로그아웃해야 해?

A.
대부분 아니다. 로그인은 되어 있지만 권한이 부족한 상태이므로 권한 없음 UI를 보여주는 것이 일반적이다.

Q. 401과 403 메시지를 같게 해도 돼?

A.
권장하지 않는다. 401은 로그인 필요, 403은 권한 없음으로 구분하는 것이 좋다.

---

## 8.4 404 Not Found UX

### [개념]

404 Not Found는 요청한 페이지나 API 리소스를 찾을 수 없는 상태다.

Frontend에서는 Route 404와 API Resource 404를 구분해야 한다.

---

### [핵심]

구분:

- Route 404
- API 404
- Resource Not Found
- Invalid ID
- Deleted Resource
- Wrong Endpoint
- SPA Fallback Problem

---

### [실무]

API 404 UX:

```text
GET /festivals/999
→ Resource Not Found
→ "축제 정보를 찾을 수 없습니다."
→ 목록으로 이동 버튼 제공
```

Route 404 UX:

```text
Unknown URL
→ NotFoundPage
→ 메인으로 이동 / 이전 페이지 이동
```

주의:

- API 404와 Route 404를 혼동하지 않음
- 상세 페이지에서 리소스 없음 UI 제공
- 잘못된 ID parameter 검증
- Network 탭에서 실제 요청 URL 확인
- SPA fallback 문제와 API 404 구분

---

### [FAQ]

Q. 페이지 404와 API 404는 달라?

A.
다르다. 페이지 404는 Route 매칭 실패이고 API 404는 서버 리소스나 endpoint를 찾지 못한 것이다.

Q. 상세 페이지 데이터가 없으면 어떻게 보여줘?

A.
해당 리소스를 찾을 수 없다는 메시지와 목록으로 돌아가는 버튼을 제공하는 것이 좋다.

---

## 8.5 409 Conflict UX

### [개념]

409 Conflict는 요청이 현재 서버 상태와 충돌할 때 발생한다.

중복 요청, 이미 처리된 요청, 상태 충돌에서 사용할 수 있다.

---

### [핵심]

사용 상황:

- duplicate favorite
- duplicate like
- duplicate signup value
- already processed request
- version conflict
- reservation conflict
- payment conflict basics

---

### [실무]

UX 기준:

```text
409 Conflict
→ "이미 처리된 요청입니다."
→ 현재 상태 refetch
→ 버튼 상태 갱신
```

예:

```text
찜 추가 요청
→ 이미 찜한 축제
→ 409
→ 찜 상태를 true로 갱신하거나 목록 refetch
```

주의:

- 사용자에게 책임을 돌리는 문구 지양
- 서버 상태와 UI 상태를 다시 동기화
- 중복 클릭 방지와 함께 사용
- 결제 / 예약 충돌은 별도 정책 필요

---

### [FAQ]

Q. 409 Conflict는 언제 발생해?

A.
이미 처리된 요청이거나 서버의 현재 상태와 요청이 충돌할 때 발생한다.

Q. 409가 나면 어떻게 해?

A.
사용자에게 상태 충돌을 안내하고 최신 서버 상태를 다시 조회하는 것이 좋다.

---

## 8.6 500 Server Error UX

### [개념]

500 Server Error는 서버 내부 오류로 요청 처리가 실패한 상태다.

Frontend는 내부 오류 상세를 노출하지 않고 일반적인 안내와 재시도 옵션을 제공한다.

---

### [핵심]

처리 기준:

- generic message
- retry
- later try again
- developer log
- monitoring
- no internal detail exposure
- fallback UI

---

### [실무]

UX 문구 예:

```text
서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.
```

권장:

- 서버 stack trace 노출 금지
- 사용자에게 재시도 안내
- 장애가 반복되면 문의 안내 가능
- 개발 환경에서는 console log 가능
- 운영 환경에서는 monitoring 연동 고려
- 중요한 요청은 처리 여부 확인 가능성 고려

---

### [FAQ]

Q. 500 에러 상세 내용을 사용자에게 보여줘도 돼?

A.
권장하지 않는다. 내부 구현 정보가 노출될 수 있으므로 일반적인 오류 메시지를 보여준다.

Q. 500이 나면 Frontend에서 해결할 수 있어?

A.
대부분 Backend 문제이지만 Frontend 요청 body나 endpoint가 잘못되어 서버 오류를 유발했는지도 확인해야 한다.

---

# 9. Empty State Rules

## 9.1 Empty State Basics

### [개념]

Empty State는 요청이 성공했지만 표시할 데이터가 없는 상태다.

사용자에게 현재 상태와 다음 행동을 안내해야 한다.

---

### [핵심]

사용 상황:

- search result empty
- review list empty
- notification empty
- favorite list empty
- chat room empty
- visit history empty
- uploaded file empty

---

### [실무]

예:

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

검색 결과 없음:

```jsx
<EmptyState
  title="검색 결과가 없습니다."
  description="검색어를 바꾸거나 필터를 초기화해 보세요."
  action={<button type="button">필터 초기화</button>}
/>
```

권장:

- 데이터 없음의 이유 설명
- 다음 행동 제안
- 검색 / 필터 초기화 버튼 제공 가능
- Error State와 구분
- 첫 사용 상태와 검색 결과 없음 상태를 구분 가능

---

### [FAQ]

Q. Empty State에는 뭘 보여줘야 해?

A.
데이터가 없다는 메시지, 이유, 사용자가 할 수 있는 다음 행동을 보여주는 것이 좋다.

Q. 검색 결과 없음은 Error야?

A.
아니다. 요청이 성공했다면 Empty State다.

---

## 9.2 First Use Empty State

### [개념]

First Use Empty State는 사용자가 아직 데이터를 만들거나 저장하지 않은 초기 상태를 안내하는 Empty State다.

---

### [핵심]

사용 상황:

- 찜 목록 없음
- 리뷰 작성 내역 없음
- 알림 없음
- 방문 기록 없음
- 업로드 이미지 없음

---

### [실무]

예:

```text
아직 찜한 축제가 없습니다.
마음에 드는 축제를 찾아 찜해 보세요.
```

권장:

- 부정적인 문구보다 다음 행동 중심 문구 사용
- CTA 제공 가능
- 서비스 핵심 기능으로 이동 유도
- 검색 결과 없음과 구분
- 사용자 탓처럼 들리는 문구 지양

---

### [FAQ]

Q. 첫 사용 Empty State와 검색 결과 없음은 달라?

A.
다르다. 첫 사용 Empty는 아직 데이터가 없는 상태이고 검색 결과 없음은 조건에 맞는 결과가 없는 상태다.

Q. Empty State에 버튼을 넣어도 돼?

A.
좋다. 사용자가 다음 행동을 쉽게 할 수 있다.

---

# 10. Success UX Rules

## 10.1 Success Feedback

### [개념]

Success Feedback은 사용자 요청이 성공적으로 처리되었음을 알려주는 UX다.

저장, 삭제, 로그인, 리뷰 작성 같은 액션 후 필요할 수 있다.

---

### [핵심]

사용 상황:

- create success
- update success
- delete success
- login success
- signup success
- favorite success
- upload success
- payment success basics

---

### [실무]

표현 방식:

- Toast
- Inline Message
- Redirect
- Modal Close
- Button State Change
- Data Refetch
- Optimistic UI Confirmation

예:

```text
리뷰가 등록되었습니다.
```

권장:

- 사용자가 결과를 알 수 있게 함
- 너무 사소한 액션에는 과도한 toast 남발 금지
- 성공 후 화면 상태 갱신
- 성공 후 redirect 기준 명확화
- 삭제 성공 후 목록에서 제거
- 저장 성공 후 버튼 상태 복구

---

### [FAQ]

Q. 성공할 때마다 Toast를 띄워야 해?

A.
항상은 아니다. 화면 변화만으로 충분한 경우도 있고 중요한 액션에는 Toast가 도움이 된다.

Q. 저장 성공 후 바로 이동해도 돼?

A.
가능하다. 다만 사용자가 성공 여부를 이해할 수 있도록 메시지나 자연스러운 화면 전환을 제공하는 것이 좋다.

---

## 10.2 Toast / Alert / Inline Message Rules

### [개념]

Toast, Alert, Inline Message는 사용자에게 상태나 결과를 알려주는 UI 방식이다.

상황에 따라 적절한 방식이 다르다.

---

### [핵심]

비교:

| 방식           | 사용 상황              | 예          |
| -------------- | ---------------------- | ----------- |
| Toast          | 짧은 성공/실패 알림    | 저장 완료   |
| Alert Box      | 화면 내 중요한 안내    | 권한 없음   |
| Inline Message | 특정 field나 영역 오류 | 이메일 오류 |
| Modal          | 중요한 확인 / 차단     | 삭제 확인   |

---

### [실무]

선택 기준:

```text
Field 문제 → Inline Error
Form 전체 문제 → Form Alert
짧은 성공 알림 → Toast
권한 없음 / 리소스 없음 → Page Error
위험한 액션 확인 → Confirm Modal
```

주의:

- Toast에 중요한 정보를 오래 의존하지 않음
- Field Error를 Toast로만 보여주지 않음
- Alert는 접근성 role 고려
- Modal 남용 금지
- 메시지 위치 일관성 유지

---

### [FAQ]

Q. Form 입력 오류를 Toast로 보여줘도 돼?

A.
권장하지 않는다. 특정 field 오류는 해당 input 근처에 보여주는 것이 좋다.

Q. Toast는 언제 쓰는 게 좋아?

A.
저장 완료, 삭제 완료처럼 짧게 알려도 되는 결과 알림에 적합하다.

---

# 11. Error Boundary Rules

## 11.1 Error Boundary Basics

### [개념]

Error Boundary는 React 렌더링 중 발생한 JavaScript 오류로 인해 전체 앱이 깨지는 것을 막고 fallback UI를 보여주는 구조다.

API 요청 실패 상태와는 역할이 다르다.

---

### [핵심]

처리 대상:

- render error
- lifecycle error
- child component crash
- unexpected UI error
- fallback UI
- error logging

처리하지 못하는 대상:

- event handler error
- async API error
- server response error
- promise rejection without handling
- validation error

---

### [실무]

기준:

```text
Component 렌더링 오류 → Error Boundary
API 요청 실패 → Error State
Form 검증 실패 → Field Error
Route 없음 → NotFoundPage
```

권장:

- 앱 전체 Root Error Boundary
- 주요 route 단위 Error Boundary
- fallback UI 제공
- 다시 시도 / 홈 이동 버튼 제공 가능
- 오류 로깅 연동 가능
- 사용자에게 stack trace 노출 금지

---

### [FAQ]

Q. Error Boundary가 API 에러도 잡아줘?

A.
아니다. API 요청 실패는 Error State로 직접 처리해야 한다.

Q. Error Boundary는 언제 필요해?

A.
예상하지 못한 렌더링 오류로 전체 앱이 깨지는 것을 막고 fallback UI를 보여주기 위해 필요하다.

---

## 11.2 Fallback UI Rules

### [개념]

Fallback UI는 정상 화면을 보여줄 수 없을 때 대신 보여주는 안전한 UI다.

Error Boundary, 데이터 없음, 권한 없음, 리소스 없음 등에서 사용한다.

---

### [핵심]

사용 상황:

- render crash
- route error
- permission denied
- resource missing
- component load failed
- feature unavailable

---

### [실무]

예:

```jsx
function FallbackUI({ onReset }) {
  return (
    <main role="alert">
      <h1>문제가 발생했습니다.</h1>
      <p>화면을 표시하는 중 오류가 발생했습니다.</p>
      <button type="button" onClick={onReset}>
        다시 시도
      </button>
    </main>
  );
}
```

권장:

- 사용자가 이해할 수 있는 메시지
- 다음 행동 제공
- 홈 이동 / 다시 시도 버튼 제공
- 내부 오류 상세 노출 금지
- 접근성 role 고려
- 반복 오류 시 문의 안내 가능

---

### [FAQ]

Q. Fallback UI에는 뭘 넣어야 해?

A.
문제 안내 메시지와 사용자가 할 수 있는 다음 행동을 제공하는 것이 좋다.

Q. 오류 stack trace를 보여줘도 돼?

A.
운영 환경에서는 사용자에게 보여주지 않는 것이 좋다.

---

# 12. TanStack Query UX Rules

## 12.1 useQuery Status UX

### [개념]

useQuery는 서버 데이터 조회 상태를 isLoading, isFetching, isError, data, error 등으로 제공한다.

이 상태값을 UI 상태로 정확히 연결해야 한다.

---

### [핵심]

상태값:

- isLoading
- isFetching
- isError
- error
- data
- isSuccess
- refetch
- status
- fetchStatus

---

### [실무]

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
    return <ErrorState message={getApiErrorMessage(error)} onRetry={refetch} />;
  }

  if (!data || data.length === 0) {
    return <EmptyState title="축제 정보가 없습니다." />;
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

- isLoading은 초기 로딩 UI
- isFetching은 재조회 표시
- isError는 Error State
- data empty는 Empty State
- refetch를 Retry 버튼에 연결 가능
- error message mapping 사용

---

### [FAQ]

Q. TanStack Query에서 에러 UI는 어떻게 보여줘?

A.
isError가 true일 때 error 객체를 메시지로 변환해 ErrorState를 보여주고 refetch로 재시도 버튼을 연결할 수 있다.

Q. isFetching일 때 전체 skeleton을 다시 보여줘야 해?

A.
항상은 아니다. 기존 데이터가 있으면 유지하고 작은 갱신 표시만 보여주는 것이 자연스러운 경우가 많다.

---

## 12.2 useMutation Status UX

### [개념]

useMutation은 서버 데이터를 생성, 수정, 삭제하는 요청 상태를 관리한다.

mutation pending, success, error 상태를 사용자 액션 UX와 연결해야 한다.

---

### [핵심]

상태값:

- mutate
- mutateAsync
- isPending
- isError
- error
- isSuccess
- onSuccess
- onError
- onSettled
- reset

---

### [실무]

예:

```tsx
function ReviewSubmitButton() {
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

권장:

- isPending으로 버튼 disabled
- onSuccess에서 refetch / invalidate / toast 처리
- onError에서 사용자 메시지 처리
- onSettled에서 공통 정리 가능
- 중복 제출 방지
- 실패 후 재시도 가능하게 상태 복구

---

### [FAQ]

Q. mutation 중 버튼을 disabled 해야 해?

A.
권장한다. 중복 요청을 줄이고 사용자가 처리 중임을 알 수 있다.

Q. mutation 성공 후 뭘 해야 해?

A.
관련 query invalidate, 화면 이동, form reset, 성공 메시지 표시 중 필요한 처리를 수행한다.

---

# 13. Form Error UX Rules

## 13.1 Field Error Rules

### [개념]

Field Error는 특정 input 값에 연결되는 오류 메시지다.

사용자가 어느 값을 수정해야 하는지 바로 알 수 있게 input 근처에 표시한다.

---

### [핵심]

사용 상황:

- required error
- email format error
- password length error
- confirm password mismatch
- rating range error
- duplicate nickname
- server validation field error

---

### [실무]

예:

```jsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  name="email"
  value={values.email}
  onChange={handleChange}
  aria-invalid={Boolean(errors.email)}
  aria-describedby={errors.email ? "email-error" : undefined}
/>
{errors.email && (
  <p id="email-error" role="alert">
    {errors.email}
  </p>
)}
```

권장:

- input 근처에 표시
- aria-invalid 적용
- aria-describedby 연결
- 에러 문구는 수정 행동을 안내
- 서버 field error와 client field error 통합
- submit 후 또는 touched 이후 표시

---

### [FAQ]

Q. Field Error는 어디에 보여줘?

A.
해당 input 근처에 보여주는 것이 좋다.

Q. Field Error를 Toast로만 보여줘도 돼?

A.
권장하지 않는다. 사용자가 어떤 필드를 수정해야 하는지 알기 어렵다.

---

## 13.2 Global Form Error Rules

### [개념]

Global Form Error는 Form 전체에 해당하는 오류 메시지다.

로그인 실패, 권한 문제, 서버 오류처럼 특정 field 하나로 귀속하기 어려운 오류에 사용한다.

---

### [핵심]

사용 상황:

- login failed
- signup failed
- server unavailable
- permission denied
- submit failed
- duplicate request
- unknown error

---

### [실무]

예:

```jsx
function FormAlert({ message }) {
  if (!message) {
    return null;
  }

  return <div role="alert">{message}</div>;
}
```

권장:

- Form 상단 또는 submit 버튼 근처 표시
- field error와 구분
- 사용자에게 다음 행동 안내
- 서버 내부 메시지 그대로 노출 지양
- submit 재시도 가능성 표시

---

### [FAQ]

Q. 로그인 실패는 Field Error야 Global Error야?

A.
이메일 형식 오류는 Field Error이고 계정 정보 불일치 같은 인증 실패는 Global Error로 처리하는 경우가 많다.

Q. Global Error는 어디에 보여줘?

A.
Form 상단이나 제출 버튼 근처처럼 사용자가 쉽게 인식할 수 있는 위치에 보여준다.

---

# 14. Route Error UX Rules

## 14.1 Not Found Page UX

### [개념]

Not Found Page는 사용자가 존재하지 않는 URL에 접근했을 때 보여주는 404 페이지다.

React Router의 catch-all route와 연결된다.

---

### [핵심]

포함 요소:

- 404 title
- friendly message
- home link
- back button
- search action
- route fallback
- invalid URL

---

### [실무]

예:

```jsx
function NotFoundPage() {
  return (
    <main>
      <h1>페이지를 찾을 수 없습니다.</h1>
      <p>주소가 잘못되었거나 페이지가 이동되었을 수 있습니다.</p>
      <Link to="/">메인으로 이동</Link>
    </main>
  );
}
```

권장:

- 메인 이동 링크 제공
- 이전 페이지 이동 버튼 제공 가능
- 잘못된 URL이라고 명확히 안내
- 서비스 톤에 맞는 문구 사용
- API Resource 404와 구분

---

### [FAQ]

Q. Not Found Page에는 뭘 넣어야 해?

A.
페이지를 찾을 수 없다는 안내와 메인 이동 또는 이전 페이지 이동 같은 다음 행동을 제공한다.

Q. API 404도 NotFoundPage로 보내?

A.
상황에 따라 다르다. 상세 리소스 없음은 해당 페이지 안에서 Resource Not Found UI를 보여줄 수 있다.

---

## 14.2 Forbidden Page UX

### [개념]

Forbidden Page는 사용자가 인증은 되었지만 접근 권한이 없는 페이지에 접근했을 때 보여주는 화면이다.

---

### [핵심]

포함 요소:

- 403 title
- permission message
- home link
- previous page action
- login state maintained
- no logout by default

---

### [실무]

예:

```jsx
function ForbiddenPage() {
  return (
    <main>
      <h1>접근 권한이 없습니다.</h1>
      <p>현재 계정으로는 이 페이지를 이용할 수 없습니다.</p>
      <Link to="/">메인으로 이동</Link>
    </main>
  );
}
```

권장:

- 권한 없음과 로그인 필요를 구분
- 사용자를 logout하지 않음
- 너무 상세한 권한 정책 노출 금지
- 이전 페이지 이동 제공 가능
- 관리자 문의 안내 가능

---

### [FAQ]

Q. Forbidden Page와 Login Page는 달라?

A.
다르다. Forbidden은 로그인은 되었지만 권한이 없는 상태이고 Login은 인증이 필요한 상태다.

Q. 403이면 로그인 페이지로 보내야 해?

A.
보통은 권한 없음 페이지나 메시지를 보여주는 것이 더 적절하다.

---

# 15. Accessibility Rules

## 15.1 Loading Accessibility

### [개념]

Loading Accessibility는 스크린 리더와 키보드 사용자도 현재 요청 상태를 이해할 수 있게 하는 기준이다.

---

### [핵심]

사용 속성:

- aria-busy
- role status
- aria-live
- aria-hidden
- accessible label
- focus preservation

---

### [실무]

예:

```jsx
function AccessibleLoading() {
  return (
    <div role="status" aria-live="polite">
      데이터를 불러오는 중입니다.
    </div>
  );
}
```

권장:

- spinner 아이콘에만 의존하지 않음
- loading message 제공
- 반복적으로 aria-live가 시끄럽게 울리지 않게 주의
- 버튼 loading은 버튼 text 변경
- skeleton 장식 요소는 aria-hidden 고려

---

### [FAQ]

Q. Spinner만 보여주면 접근성에 충분해?

A.
아니다. 스크린 리더가 이해할 수 있는 텍스트나 role status를 제공하는 것이 좋다.

Q. Skeleton은 스크린 리더가 읽어야 해?

A.
대부분 장식 요소로 보고 aria-hidden 처리하거나 별도 loading message를 제공하는 것이 좋다.

---

## 15.2 Error Accessibility

### [개념]

Error Accessibility는 오류 메시지를 보조 기술 사용자가 인식하고 수정할 수 있게 하는 기준이다.

---

### [핵심]

사용 속성:

- role alert
- aria-invalid
- aria-describedby
- focus management
- field error id
- error summary
- keyboard navigation

---

### [실무]

예:

```jsx
<input
  id="nickname"
  aria-invalid={Boolean(errors.nickname)}
  aria-describedby={errors.nickname ? "nickname-error" : undefined}
/>;
{
  errors.nickname && (
    <p id="nickname-error" role="alert">
      {errors.nickname}
    </p>
  );
}
```

권장:

- Field Error를 input과 연결
- submit 실패 시 첫 오류 field로 focus 이동 고려
- Global Error는 role alert 사용 가능
- 색상만으로 오류 표시하지 않음
- 오류 문구는 구체적이고 수정 가능하게 작성

---

### [FAQ]

Q. Error Message는 색상만 빨갛게 하면 돼?

A.
아니다. 색상 외에도 텍스트, aria 속성, 아이콘 등을 사용해 오류를 명확히 전달해야 한다.

Q. submit 실패 시 focus 이동이 필요해?

A.
필수는 아니지만 첫 오류 field로 focus를 이동하면 사용자가 빠르게 수정할 수 있다.

---

# 16. Troubleshooting Rules

## 16.1 Infinite Loading Troubleshooting

### [개념]

Infinite Loading은 Loading UI가 끝나지 않고 계속 표시되는 문제다.

---

### [핵심]

원인:

- finally에서 loading false 누락
- catch 처리 누락
- API promise pending
- useEffect dependency loop
- 조건부 return 오류
- request never resolves
- auth initialized false 유지
- query enabled 조건 오류

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

---

### [FAQ]

Q. Loading이 계속 끝나지 않아?

A.
finally에서 loading false를 호출하는지, API 요청이 완료되는지, useEffect가 반복 실행되는지 확인해야 한다.

Q. auth loading이 계속되면?

A.
인증 초기화 로직에서 성공/실패와 관계없이 initialized를 true로 바꾸는지 확인해야 한다.

---

## 16.2 Blank Screen Troubleshooting

### [개념]

Blank Screen은 오류 메시지나 로딩 표시 없이 화면이 비어 보이는 문제다.

---

### [핵심]

원인:

- loading / error / empty 처리 누락
- runtime render error
- map on undefined
- route mismatch
- component return null
- CSS display none
- API response shape mismatch
- Error Boundary 없음

---

### [실무]

Debug Flow:

```text
Blank Screen
→ Console Error 확인
→ Network Response 확인
→ Loading State 확인
→ Error State 확인
→ Empty State 확인
→ Route Match 확인
→ Component Return 확인
→ CSS 확인
```

주의:

- 빈 화면은 사용자에게 가장 나쁜 UX 중 하나
- 최소한 Loading, Error, Empty 중 하나를 보여야 함
- Error Boundary가 없으면 렌더링 오류로 앱 전체가 깨질 수 있음
- response shape mismatch 확인

---

### [FAQ]

Q. 화면이 아무것도 안 나와?

A.
Console Error, Network Response, Route Match, Loading/Error/Empty 처리, Component return 값을 확인해야 한다.

Q. 빈 화면 대신 뭘 보여줘야 해?

A.
상황에 따라 Loading, Error, Empty, Not Found, Forbidden 같은 상태 UI를 보여줘야 한다.

---

## 16.3 Error Message Not Showing

### [개념]

Error Message Not Showing은 오류가 발생했지만 사용자에게 메시지가 표시되지 않는 문제다.

---

### [핵심]

원인:

- catch에서 에러를 삼킴
- setError 누락
- Error State 렌더링 조건 오류
- error 객체 구조 착각
- AxiosError mapping 실패
- TanStack Query isError 미사용
- Form errors key 불일치
- Promise.reject 누락

---

### [실무]

Debug Flow:

```text
Error 발생
→ catch 진입 확인
→ error 객체 확인
→ message mapping 확인
→ setError 확인
→ Error UI 렌더링 조건 확인
→ role alert 확인
```

주의:

- interceptor에서 에러를 처리한 뒤 Promise.reject 필요
- error.response?.data 구조 확인
- 사용자 메시지 fallback 제공
- field error와 global error 구분

---

### [FAQ]

Q. API는 실패했는데 에러 메시지가 안 보여?

A.
catch에서 에러를 상태로 저장하는지, Error UI 조건이 맞는지, error mapping 함수가 올바른지 확인해야 한다.

Q. interceptor에서 에러 처리하면 화면에서는 못 받아?

A.
Promise.reject를 반환하지 않으면 호출부가 에러를 인식하지 못할 수 있다.

---

## 16.4 Flicker Troubleshooting

### [개념]

Flicker는 loading, empty, content, redirect 화면이 짧게 깜빡이는 문제다.

인증 초기화와 데이터 조회에서 자주 발생한다.

---

### [핵심]

원인:

- auth initialized 구분 없음
- 초기 data 빈 배열로 Empty 먼저 표시
- loading false 초기값
- query enabled 조건 누락
- redirect 조건이 너무 빨리 실행
- 기존 데이터 제거 후 refetch
- Suspense / lazy loading fallback 과다

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

권장:

- 인증 확인 전 Protected Route redirect 금지
- 요청 완료 전 Empty 표시 금지
- 기존 데이터 refetch 시 유지 가능
- loading 상태 초기값 신중히 설정
- route transition fallback 최소화

---

### [FAQ]

Q. 로그인 페이지가 잠깐 보였다가 메인으로 가?

A.
auth initialized 전에 PublicOnlyRoute가 렌더링되어 redirect 판단이 빨리 실행되었을 수 있다.

Q. Empty State가 잠깐 보였다가 목록이 보여?

A.
요청 완료 전 빈 배열을 Empty로 판정했을 가능성이 있다.

---

## 16.5 Duplicate Request Troubleshooting

### [개념]

Duplicate Request는 같은 API 요청이 의도보다 여러 번 발생하는 문제다.

---

### [핵심]

원인:

- React StrictMode development double effect
- useEffect dependency 오류
- button 중복 클릭
- submit disabled 없음
- queryKey 변경 반복
- state update loop
- interceptor 중복 등록
- infinite scroll observer 중복 실행

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

주의:

- 개발 환경 StrictMode에서 effect가 두 번 보일 수 있음
- 운영 중복인지 개발 전용인지 구분
- 중복 제출은 UX와 Backend 모두에서 방지
- interceptor는 앱 초기화 시 한 번만 등록
- infinite scroll observer cleanup 필요

---

### [FAQ]

Q. API가 두 번 호출돼?

A.
useEffect dependency, StrictMode, 버튼 중복 클릭, queryKey 변경, interceptor 중복 등록을 확인해야 한다.

Q. StrictMode 때문에 두 번 호출되는 건 문제야?

A.
개발 환경에서 부작용을 찾기 위한 동작일 수 있다. 다만 실제 중복 요청을 막는 구조는 필요하다.

---

# 17. Security Rules

## 17.1 Error Message Security

### [개념]

Error Message Security는 오류 메시지를 통해 민감한 내부 정보가 사용자에게 노출되지 않도록 하는 기준이다.

---

### [핵심]

노출 주의:

- stack trace
- SQL error
- server path
- token value
- password
- personal data
- internal role policy
- API secret
- infrastructure detail

---

### [실무]

사용자 메시지:

```text
요청 처리 중 문제가 발생했습니다.
```

개발자 로그:

```text
status, endpoint, error code, timestamp
```

주의:

- 운영 환경에서 stack trace 노출 금지
- token / password 로그 금지
- 서버 원문 message를 그대로 노출하기 전 검토
- 403에서 내부 권한 정책 상세 노출 주의
- Validation Error는 사용자 수정에 필요한 수준만 제공

---

### [FAQ]

Q. 서버 에러 원문을 그대로 보여주면 안 되는 이유는?

A.
내부 구조, SQL, 서버 경로, 보안 정보가 노출될 수 있기 때문이다.

Q. 개발자 로그와 사용자 메시지는 왜 나눠?

A.
사용자는 이해 가능한 해결 안내가 필요하고 개발자는 원인 분석 정보가 필요하기 때문이다.

---

# 18. Component Design Rules

## 18.1 State Component Separation

### [개념]

State Component Separation은 LoadingState, ErrorState, EmptyState 같은 상태 UI를 재사용 가능한 Component로 분리하는 기준이다.

---

### [핵심]

분리 대상:

- LoadingState
- ErrorState
- EmptyState
- SuccessMessage
- PageError
- FieldError
- FormAlert
- RetryButton
- Skeleton Component

---

### [실무]

파일 구조 예:

```text
src
├ components
│  └ states
│     ├ LoadingState.tsx
│     ├ ErrorState.tsx
│     ├ EmptyState.tsx
│     └ ForbiddenState.tsx
├ features
└ pages
```

권장:

- 반복되는 상태 UI는 공통 Component화
- 도메인별 메시지는 props로 전달
- 공통 ErrorState에 Retry 버튼 지원
- EmptyState에 action slot 제공
- 너무 추상화하지 않음
- 페이지 전체 상태와 작은 영역 상태 구분

---

### [FAQ]

Q. LoadingState, ErrorState를 Component로 만들면 좋아?

A.
반복되는 상태 UI를 일관되게 관리할 수 있어 좋다. 다만 너무 이른 추상화는 피한다.

Q. EmptyState는 공통으로 만들 수 있어?

A.
가능하다. title, description, action을 props로 받으면 여러 화면에서 재사용할 수 있다.

---

## 18.2 Error Hook Rules

### [개념]

Error Hook은 API 에러 메시지 mapping, toast 처리, retry 로직 등을 재사용하기 위한 Custom Hook이다.

---

### [핵심]

사용 대상:

- API error mapping
- mutation error toast
- common retry
- auth error handling
- form server error mapping
- network status

---

### [실무]

예:

```typescript
function useApiErrorMessage() {
  function getMessage(error: unknown) {
    return getApiErrorMessage(error);
  }

  return { getMessage };
}
```

주의:

- 단순 함수로 충분하면 Hook으로 만들지 않음
- Hook 안에서 UI side effect를 남발하지 않음
- Toast 발생 위치를 명확히 함
- Form field error mapping과 global error mapping 구분
- Auth error는 Authentication Flow와 연결

---

### [FAQ]

Q. Error mapping은 Hook으로 만들어야 해?

A.
항상은 아니다. 단순 변환은 함수로 충분하고 React 상태나 side effect가 필요할 때 Hook을 검토한다.

Q. 모든 API 에러를 Toast로 처리하면 돼?

A.
아니다. Form field error, page error, permission error처럼 위치가 중요한 오류는 적절한 UI 위치에 표시해야 한다.

---

# 19. Comparison Rules

## 19.1 Required Comparisons

### [개념]

Error Handling & Loading UX 문서는 헷갈리는 상태와 UI 방식을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- Loading State vs Empty State
- Error State vs Empty State
- Initial Loading vs Refetch Loading
- Submit Loading vs Page Loading
- Spinner vs Skeleton
- Toast vs Inline Error
- Field Error vs Global Error
- API Error vs Render Error
- Error Boundary vs Try Catch
- 401 vs 403
- 404 Route Error vs 404 API Error
- Network Error vs Server Error
- isLoading vs isFetching
- useQuery Error vs useMutation Error
- Retry vs Redirect
- Disabled vs ReadOnly

---

### [실무]

예시:

| 비교      | API Error        | Render Error            |
| --------- | ---------------- | ----------------------- |
| 발생 위치 | 서버 요청        | React 렌더링            |
| 처리 방식 | Error State      | Error Boundary          |
| 예        | 500 응답         | undefined property 접근 |
| 사용자 UI | 요청 실패 메시지 | Fallback UI             |
| 재시도    | refetch 가능     | reset / reload 가능     |

---

### [FAQ]

Q. 비교 표는 왜 필요해?

A.
사용자가 자주 헷갈리는 Error / Loading UX 질문에서 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. Error Handling 비교 문서에서 가장 중요한 것은?

A.
오류 종류와 사용자에게 보여줄 UI 위치를 정확히 구분하는 것이다.

---

# 20. Checklist Rules

## 20.1 Error Handling & Loading UX Checklist

### [개념]

Error Handling & Loading UX 문서 검수 시 상태 UX 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] Loading / Error / Empty / Success 상태 구분이 포함되었는가?
- [ ] Initial Loading / Refetch Loading / Submit Loading 차이가 포함되었는가?
- [ ] Skeleton / Spinner 선택 기준이 포함되었는가?
- [ ] API Error State 기준이 포함되었는가?
- [ ] Error Message Mapping 기준이 포함되었는가?
- [ ] Network Error / Server Error 구분이 포함되었는가?
- [ ] 400 / 401 / 403 / 404 / 409 / 500 UX 기준이 포함되었는가?
- [ ] Empty State 기준이 포함되었는가?
- [ ] Success Feedback 기준이 포함되었는가?
- [ ] Toast / Alert / Inline Message 기준이 포함되었는가?
- [ ] Error Boundary 기준이 포함되었는가?
- [ ] TanStack Query 상태 UX 기준이 포함되었는가?
- [ ] Form Error UX 기준이 포함되었는가?
- [ ] Route Error UX 기준이 포함되었는가?
- [ ] Accessibility 기준이 포함되었는가?
- [ ] Troubleshooting이 포함되었는가?
- [ ] Security 주의사항이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 기준:

```text
Draft
→ State Classification Check
→ Loading UX Check
→ Error UX Check
→ Empty UX Check
→ Status Code UX Check
→ Accessibility Check
→ Troubleshooting Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. Error Handling 문서 검수에서 가장 중요한 것은?

A.
상태 구분, 오류 종류별 UX, 사용자 메시지, 재시도 기준, 접근성, Troubleshooting 포함 여부다.

---

# 21. Retrieval Optimization Rules

## 21.1 Keyword Rules

### [개념]

Error Handling & Loading UX 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- Error Handling
- Loading UX
- Error UX
- Loading State
- Error State
- Empty State
- Success State
- Initial Loading
- Refetch Loading
- Submit Loading
- Skeleton UI
- Spinner
- Disabled Button
- Retry Button
- Fallback UI
- Error Boundary
- API Error
- Network Error
- Server Error
- Validation Error
- Field Error
- Global Error
- Toast
- Alert
- Inline Error
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 409 Conflict
- 422 Validation Error
- 500 Server Error
- TanStack Query
- isLoading
- isFetching
- isError
- useMutation
- Infinite Loading
- Blank Screen
- Flicker
- Duplicate Request

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- Loading State와 Empty State 차이는?
- API 에러는 어떻게 보여줘?
- Spinner와 Skeleton 중 뭐가 좋아?
- isLoading과 isFetching 차이는?
- 401과 403은 어떻게 처리해?
- 500 에러 메시지는 어떻게 보여줘?
- Error Boundary가 API 에러도 잡아?
- Loading이 계속 끝나지 않아?
- 화면이 빈 화면으로 나와?
- 에러 메시지가 안 보여?
- API가 두 번 호출돼?
- Empty State에는 뭘 보여줘?
- Field Error와 Global Error 차이는?
- Toast는 언제 써?
- 서버 에러 원문을 보여줘도 돼?

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. FAQ 질문은 어떤 스타일이 좋아?

A.
실제 사용자가 검색하거나 질문할 법한 문장형 질문이 좋다.

---

# 22. Version Rules

## 22.1 Modern Error Handling 기준

### [개념]

Error Handling & Loading UX 문서는 Modern React Frontend 기준으로 작성한다.

---

### [핵심]

기준:

- React 18+
- React 19 호환 고려
- Functional Component
- Hook 기반 상태 처리
- React Router v6+
- TanStack Query 상태값 고려
- API Error State 분리
- Error Boundary 기초 포함
- Accessibility 포함
- TypeScript Ready Error Type
- User-friendly Message
- Developer Log Separation

Legacy 제외:

- alert 남발
- 빈 화면 방치
- Loading State 생략
- Error State 생략
- Empty State 미구분
- 서버 에러 원문 노출
- stack trace 사용자 노출
- 모든 오류를 Toast로만 처리
- 401 / 403 동일 처리
- Error Boundary를 API 에러 처리로 오해
- jQuery ajax error 중심 설명

---

### [실무]

실무 기준:

```text
Modern Error UX
→ Classify State
→ Show Loading
→ Map Error
→ Show User Message
→ Provide Retry or Redirect
→ Preserve Accessibility
→ Log for Debugging
```

---

### [FAQ]

Q. 그냥 alert로 에러를 보여줘도 돼?

A.
간단한 테스트는 가능하지만 실무 문서에서는 Inline Error, Page Error, Toast, Fallback UI를 상황별로 구분한다.

Q. Error Boundary만 있으면 모든 에러 처리가 끝나?

A.
아니다. API 요청 실패, Form Validation, 인증 오류는 별도로 처리해야 한다.

---

# 23. Common Mistakes

## 23.1 Error Handling Common Mistakes

### [개념]

Error Handling & Loading UX 문서는 자주 발생하는 상태 UX 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

- Loading State 없이 빈 화면 표시
- Error State 없이 console.log만 출력
- Empty State와 Error State 혼동
- 초기 빈 배열을 바로 Empty로 표시
- submit loading 없이 중복 요청 허용
- fetch finally 누락으로 무한 로딩 발생
- catch에서 에러를 삼킴
- interceptor에서 Promise.reject 누락
- 서버 에러 원문을 사용자에게 그대로 노출
- 401과 403을 같은 메시지로 처리
- 403에서 무조건 logout 처리
- API 404와 Route 404 혼동
- Field Error를 Toast로만 표시
- Error Boundary가 API 에러를 잡는다고 착각
- Spinner만 오래 보여주고 설명 없음
- Skeleton 구조가 실제 UI와 다름
- isLoading과 isFetching 혼동
- mutation pending 상태로 버튼 disabled 하지 않음
- Retry 버튼이 실제 refetch와 연결되지 않음
- Network 탭 확인 없이 UI만 수정
- StrictMode 중복 요청을 운영 버그로 착각

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: Loading이 계속 끝나지 않음
원인: API 실패 시 catch에서 error는 잡았지만 finally에서 setLoading(false)를 호출하지 않음
해결: try / catch / finally 구조로 loading 종료를 보장
```

---

### [FAQ]

Q. Error Handling 초보가 가장 많이 하는 실수는?

A.
Loading / Error / Empty 상태를 구분하지 않고 빈 화면이나 console.log만 남기는 실수가 많다.

Q. Error UX 문제는 어떻게 찾는 게 좋아?

A.
Network 응답, 상태값, 조건부 렌더링 순서, error mapping, loading 종료 여부를 순서대로 확인한다.

---

# 24. Final Goal

## 24.1 Domain Final Goal

### [개념]

Error Handling & Loading UX RAG 문서는 Frontend Agent가 API 요청과 사용자 액션의 성공 / 실패 / 대기 상태를 안정적이고 이해 가능한 UX로 표현하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- Loading / Error / Empty / Success 상태 구분
- Initial Loading 처리
- Refetch Loading 처리
- Submit Loading 처리
- Skeleton / Spinner 선택
- API Error 처리
- Error Message Mapping
- Network Error 처리
- Server Error 처리
- Validation Error 처리
- 401 / 403 / 404 / 409 / 500 UX 처리
- Empty State 작성
- Success Feedback 작성
- Toast / Alert / Inline Message 선택
- Error Boundary 적용 판단
- Fallback UI 작성
- TanStack Query 상태값 연결
- Form Error UX 작성
- Route Error UX 작성
- Accessibility 기준 적용
- Infinite Loading / Blank Screen / Flicker / Duplicate Request 디버깅
- 보안상 안전한 Error Message 작성

---

### [실무]

Agent 수행 가능 작업:

```text
User Error UX Request
→ Identify Request State
→ Classify Loading / Error / Empty / Success
→ Map Error Type
→ Choose UI Pattern
→ Add Retry / Redirect if Needed
→ Add Accessibility Attributes
→ Check Security Exposure
→ Error Handling & Loading UX Output
```

---

### [FAQ]

Q. Error Handling & Loading UX 문서의 최종 목적은 뭐야?

A.
Frontend Agent가 사용자가 이해할 수 있는 Loading, Error, Empty, Success UI를 설계하고 오류 상황을 안정적으로 처리하게 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
Frontend Testing, Frontend Accessibility, Frontend Build & Deploy, Frontend Code Review 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Error Handling & Loading UX 문서는 왜 필요해?
A. Frontend Agent가 API 요청과 사용자 액션의 대기, 성공, 실패, 빈 데이터 상태를 사용자에게 명확히 보여줘야 하기 때문이다.

Q. Loading State와 Empty State 차이는?
A. Loading은 요청 중인 상태이고 Empty는 요청이 성공했지만 표시할 데이터가 없는 상태다.

Q. Error State와 Empty State 차이는?
A. Error는 요청 실패이고 Empty는 요청 성공 후 데이터가 없는 상태다.

Q. Success State는 뭐야?
A. 요청이 성공하고 표시할 데이터나 완료 결과가 있는 상태다.

Q. 초기 배열이 빈 배열이면 바로 Empty를 보여줘도 돼?
A. 요청 전인지 요청 완료 후인지 구분해야 한다. 요청 중에는 Loading을 보여주는 것이 좋다.

Q. loading, error boolean을 따로 두면 안 돼?
A. 가능하다. 하지만 상태가 많아져 서로 충돌하면 status 문자열이나 reducer로 모델링하는 것이 더 안전하다.

Q. idle 상태는 왜 필요해?
A. 아직 요청을 시작하지 않은 상태와 요청 중인 상태를 구분하기 위해 필요하다.

Q. 페이지 처음 들어갔을 때 빈 화면이 보여도 돼?
A. 권장하지 않는다. 데이터 요청 중이면 Loading UI를 보여주는 것이 좋다.

Q. auth loading과 page loading은 같아?
A. 다르다. auth loading은 인증 상태 확인이고 page loading은 화면 데이터 조회 상태다.

Q. isLoading과 isFetching은 뭐가 달라?
A. isLoading은 주로 초기 데이터가 없는 로딩이고 isFetching은 데이터 재조회 중에도 true가 될 수 있다.

Q. 재조회할 때 기존 데이터를 지워야 해?
A. 항상 지울 필요는 없다. 기존 데이터를 유지하면서 갱신 표시를 보여주는 것이 더 자연스러운 경우가 많다.

Q. 제출 중 버튼을 disabled 해야 해?
A. 권장한다. 중복 제출을 줄이고 사용자가 처리 중임을 이해할 수 있다.

Q. submit loading과 initial loading은 달라?
A. 다르다. submit loading은 사용자 액션 처리 중이고 initial loading은 화면 데이터 초기 조회 중이다.

Q. 무한 스크롤에서 로딩은 어디에 보여줘?
A. 보통 기존 목록은 유지하고 하단에 다음 데이터를 불러오는 표시를 보여준다.

Q. 더보기 버튼을 여러 번 누르면 중복 요청이 나가?
A. loading 중 disabled 처리를 하지 않으면 중복 요청이 발생할 수 있다.

Q. Skeleton UI는 언제 써?
A. 카드 목록이나 상세 페이지처럼 콘텐츠 구조가 예측 가능할 때 적합하다.

Q. Spinner는 언제 써?
A. 버튼 제출, 작은 영역 로딩, 짧은 처리 작업, 더보기 로딩에 적합하다.

Q. Skeleton이 Spinner보다 항상 좋아?
A. 아니다. 짧은 요청이나 단순 액션에는 Spinner나 버튼 loading이 더 적합할 수 있다.

Q. Spinner에는 텍스트가 꼭 필요해?
A. 접근성을 위해 진행 상태를 설명하는 텍스트나 aria label을 제공하는 것이 좋다.

Q. Spinner가 계속 돌면 어떻게 해?
A. 요청 완료, 실패, finally 처리, timeout, dependency loop를 확인해야 한다.

Q. 목록 로딩에는 Skeleton이 좋아 Spinner가 좋아?
A. 카드나 테이블 구조가 명확하면 Skeleton이 좋고 단순한 경우에는 Spinner도 가능하다.

Q. 저장 버튼에는 Skeleton을 써?
A. 아니다. 저장 버튼에는 disabled 상태와 버튼 내부 loading 문구 또는 spinner가 적합하다.

Q. API 에러는 어떻게 보여줘?
A. 사용자가 이해할 수 있는 메시지와 필요한 경우 다시 시도 버튼을 제공한다.

Q. 서버 에러 원문을 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 정보가 포함될 수 있으므로 사용자용 메시지로 변환하는 것이 좋다.

Q. 에러 메시지 mapping 함수는 왜 필요해?
A. API 에러 구조를 화면마다 직접 해석하면 중복이 생기고 메시지 기준이 달라질 수 있기 때문이다.

Q. Network Error와 500 에러는 달라?
A. 다르다. Network Error는 응답 자체를 받지 못한 경우이고 500은 서버가 응답한 내부 오류다.

Q. Postman에서는 되는데 브라우저에서는 Network Error가 나?
A. CORS, mixed content, 브라우저 보안 정책 문제일 수 있다.

Q. Validation Error는 alert로만 보여줘도 돼?
A. 권장하지 않는다. 필드별 오류는 해당 input 근처에 보여주는 것이 사용자가 수정하기 쉽다.

Q. 서버 검증 실패 후 입력값은 지워야 해?
A. 보통 지우지 않는다. 사용자가 오류를 수정할 수 있도록 유지하는 것이 좋다.

Q. 401이면 무조건 로그인 페이지로 보내?
A. refresh token flow가 있으면 먼저 재발급을 시도할 수 있다. 재발급 실패 시 로그인 페이지로 이동한다.

Q. 로그인 실패도 401이야?
A. Backend 설계에 따라 가능하다. 로그인 실패 401과 기존 인증 만료 401의 UX를 구분해야 한다.

Q. 403이면 로그아웃해야 해?
A. 대부분 아니다. 로그인은 되어 있지만 권한이 부족한 상태이므로 권한 없음 UI를 보여주는 것이 일반적이다.

Q. 401과 403 메시지를 같게 해도 돼?
A. 권장하지 않는다. 401은 로그인 필요, 403은 권한 없음으로 구분하는 것이 좋다.

Q. 페이지 404와 API 404는 달라?
A. 다르다. 페이지 404는 Route 매칭 실패이고 API 404는 서버 리소스나 endpoint를 찾지 못한 것이다.

Q. 상세 페이지 데이터가 없으면 어떻게 보여줘?
A. 해당 리소스를 찾을 수 없다는 메시지와 목록으로 돌아가는 버튼을 제공하는 것이 좋다.

Q. 409 Conflict는 언제 발생해?
A. 이미 처리된 요청이거나 서버의 현재 상태와 요청이 충돌할 때 발생한다.

Q. 409가 나면 어떻게 해?
A. 사용자에게 상태 충돌을 안내하고 최신 서버 상태를 다시 조회하는 것이 좋다.

Q. 500 에러 상세 내용을 사용자에게 보여줘도 돼?
A. 권장하지 않는다. 내부 구현 정보가 노출될 수 있으므로 일반적인 오류 메시지를 보여준다.

Q. 500이 나면 Frontend에서 해결할 수 있어?
A. 대부분 Backend 문제이지만 Frontend 요청 body나 endpoint가 잘못되어 서버 오류를 유발했는지도 확인해야 한다.

Q. Empty State에는 뭘 보여줘야 해?
A. 데이터가 없다는 메시지, 이유, 사용자가 할 수 있는 다음 행동을 보여주는 것이 좋다.

Q. 검색 결과 없음은 Error야?
A. 아니다. 요청이 성공했다면 Empty State다.

Q. 첫 사용 Empty State와 검색 결과 없음은 달라?
A. 다르다. 첫 사용 Empty는 아직 데이터가 없는 상태이고 검색 결과 없음은 조건에 맞는 결과가 없는 상태다.

Q. Empty State에 버튼을 넣어도 돼?
A. 좋다. 사용자가 다음 행동을 쉽게 할 수 있다.

Q. 성공할 때마다 Toast를 띄워야 해?
A. 항상은 아니다. 화면 변화만으로 충분한 경우도 있고 중요한 액션에는 Toast가 도움이 된다.

Q. 저장 성공 후 바로 이동해도 돼?
A. 가능하다. 다만 사용자가 성공 여부를 이해할 수 있도록 메시지나 자연스러운 화면 전환을 제공하는 것이 좋다.

Q. Form 입력 오류를 Toast로 보여줘도 돼?
A. 권장하지 않는다. 특정 field 오류는 해당 input 근처에 보여주는 것이 좋다.

Q. Toast는 언제 쓰는 게 좋아?
A. 저장 완료, 삭제 완료처럼 짧게 알려도 되는 결과 알림에 적합하다.

Q. Error Boundary가 API 에러도 잡아줘?
A. 아니다. API 요청 실패는 Error State로 직접 처리해야 한다.

Q. Error Boundary는 언제 필요해?
A. 예상하지 못한 렌더링 오류로 전체 앱이 깨지는 것을 막고 fallback UI를 보여주기 위해 필요하다.

Q. Fallback UI에는 뭘 넣어야 해?
A. 문제 안내 메시지와 사용자가 할 수 있는 다음 행동을 제공하는 것이 좋다.

Q. 오류 stack trace를 보여줘도 돼?
A. 운영 환경에서는 사용자에게 보여주지 않는 것이 좋다.

Q. TanStack Query에서 에러 UI는 어떻게 보여줘?
A. isError가 true일 때 error 객체를 메시지로 변환해 ErrorState를 보여주고 refetch로 재시도 버튼을 연결할 수 있다.

Q. isFetching일 때 전체 skeleton을 다시 보여줘야 해?
A. 항상은 아니다. 기존 데이터가 있으면 유지하고 작은 갱신 표시만 보여주는 것이 자연스러운 경우가 많다.

Q. mutation 중 버튼을 disabled 해야 해?
A. 권장한다. 중복 요청을 줄이고 사용자가 처리 중임을 알 수 있다.

Q. mutation 성공 후 뭘 해야 해?
A. 관련 query invalidate, 화면 이동, form reset, 성공 메시지 표시 중 필요한 처리를 수행한다.

Q. Field Error는 어디에 보여줘?
A. 해당 input 근처에 보여주는 것이 좋다.

Q. Field Error를 Toast로만 보여줘도 돼?
A. 권장하지 않는다. 사용자가 어떤 필드를 수정해야 하는지 알기 어렵다.

Q. 로그인 실패는 Field Error야 Global Error야?
A. 이메일 형식 오류는 Field Error이고 계정 정보 불일치 같은 인증 실패는 Global Error로 처리하는 경우가 많다.

Q. Global Error는 어디에 보여줘?
A. Form 상단이나 제출 버튼 근처처럼 사용자가 쉽게 인식할 수 있는 위치에 보여준다.

Q. Not Found Page에는 뭘 넣어야 해?
A. 페이지를 찾을 수 없다는 안내와 메인 이동 또는 이전 페이지 이동 같은 다음 행동을 제공한다.

Q. Forbidden Page와 Login Page는 달라?
A. 다르다. Forbidden은 로그인은 되었지만 권한이 없는 상태이고 Login은 인증이 필요한 상태다.

Q. Spinner만 보여주면 접근성에 충분해?
A. 아니다. 스크린 리더가 이해할 수 있는 텍스트나 role status를 제공하는 것이 좋다.

Q. Skeleton은 스크린 리더가 읽어야 해?
A. 대부분 장식 요소로 보고 aria-hidden 처리하거나 별도 loading message를 제공하는 것이 좋다.

Q. Error Message는 색상만 빨갛게 하면 돼?
A. 아니다. 색상 외에도 텍스트, aria 속성, 아이콘 등을 사용해 오류를 명확히 전달해야 한다.

Q. submit 실패 시 focus 이동이 필요해?
A. 필수는 아니지만 첫 오류 field로 focus를 이동하면 사용자가 빠르게 수정할 수 있다.

Q. Loading이 계속 끝나지 않아?
A. finally에서 loading false를 호출하는지, API 요청이 완료되는지, useEffect가 반복 실행되는지 확인해야 한다.

Q. auth loading이 계속되면?
A. 인증 초기화 로직에서 성공/실패와 관계없이 initialized를 true로 바꾸는지 확인해야 한다.

Q. 화면이 아무것도 안 나와?
A. Console Error, Network Response, Route Match, Loading/Error/Empty 처리, Component return 값을 확인해야 한다.

Q. 빈 화면 대신 뭘 보여줘야 해?
A. 상황에 따라 Loading, Error, Empty, Not Found, Forbidden 같은 상태 UI를 보여줘야 한다.

Q. API는 실패했는데 에러 메시지가 안 보여?
A. catch에서 에러를 상태로 저장하는지, Error UI 조건이 맞는지, error mapping 함수가 올바른지 확인해야 한다.

Q. interceptor에서 에러 처리하면 화면에서는 못 받아?
A. Promise.reject를 반환하지 않으면 호출부가 에러를 인식하지 못할 수 있다.

Q. 로그인 페이지가 잠깐 보였다가 메인으로 가?
A. auth initialized 전에 PublicOnlyRoute가 렌더링되어 redirect 판단이 빨리 실행되었을 수 있다.

Q. Empty State가 잠깐 보였다가 목록이 보여?
A. 요청 완료 전 빈 배열을 Empty로 판정했을 가능성이 있다.

Q. API가 두 번 호출돼?
A. useEffect dependency, StrictMode, 버튼 중복 클릭, queryKey 변경, interceptor 중복 등록을 확인해야 한다.

Q. StrictMode 때문에 두 번 호출되는 건 문제야?
A. 개발 환경에서 부작용을 찾기 위한 동작일 수 있다. 다만 실제 중복 요청을 막는 구조는 필요하다.

Q. 서버 에러 원문을 그대로 보여주면 안 되는 이유는?
A. 내부 구조, SQL, 서버 경로, 보안 정보가 노출될 수 있기 때문이다.

Q. 개발자 로그와 사용자 메시지는 왜 나눠?
A. 사용자는 이해 가능한 해결 안내가 필요하고 개발자는 원인 분석 정보가 필요하기 때문이다.

Q. LoadingState, ErrorState를 Component로 만들면 좋아?
A. 반복되는 상태 UI를 일관되게 관리할 수 있어 좋다. 다만 너무 이른 추상화는 피한다.

Q. EmptyState는 공통으로 만들 수 있어?
A. 가능하다. title, description, action을 props로 받으면 여러 화면에서 재사용할 수 있다.

Q. 모든 API 에러를 Toast로 처리하면 돼?
A. 아니다. Form field error, page error, permission error처럼 위치가 중요한 오류는 적절한 UI 위치에 표시해야 한다.

Q. 그냥 alert로 에러를 보여줘도 돼?
A. 간단한 테스트는 가능하지만 실무 문서에서는 Inline Error, Page Error, Toast, Fallback UI를 상황별로 구분한다.

Q. Error Handling 초보가 가장 많이 하는 실수는?
A. Loading / Error / Empty 상태를 구분하지 않고 빈 화면이나 console.log만 남기는 실수가 많다.

Q. Error UX 문제는 어떻게 찾는 게 좋아?
A. Network 응답, 상태값, 조건부 렌더링 순서, error mapping, loading 종료 여부를 순서대로 확인한다.

Q. Error Handling & Loading UX 다음 문서는 뭐가 좋아?
A. Frontend Testing, Frontend Accessibility, Frontend Build & Deploy, Frontend Code Review 순서가 좋다.
