# Error Handling & Loading UX Part09 - Final Integration & Retrieval Map

---

# 1. Final Integration Overview

## 1.1 Final Integration Purpose

### [개념]

Final Integration은 Error Handling & Loading UX 문서를 실제 Frontend Agent, Review Agent, PM Agent가 검색하고 적용할 수 있도록 전체 기준을 통합하는 최종 정리다.

이 문서는 개별 Part에서 다룬 Loading, Error, Empty, Success, TanStack Query, Form, Route, Accessibility, Security, Component Pattern 기준을 하나의 판단 흐름으로 연결한다.

---

### [핵심]

Final Integration 대상:

- UI State Classification
- Loading UX
- Error State
- Empty State
- Success Feedback
- TanStack Query UX
- Form Error UX
- Route Error UX
- Error Boundary
- Accessibility
- Security
- Troubleshooting
- Component Pattern
- Review Checklist
- Retrieval Query Map

핵심 규칙:

- 모든 화면은 Loading / Error / Empty / Success 상태를 명확히 가진다.
- 요청 실패를 Empty State로 숨기지 않는다.
- 초기 빈 배열을 Empty State로 오판하지 않는다.
- 사용자 메시지와 개발자 로그를 분리한다.
- 서버 원문 error message를 그대로 노출하지 않는다.
- TanStack Query 상태값을 UI State와 정확히 연결한다.
- Form Error는 Field Error와 Global Form Error로 분리한다.
- Route 404와 API Resource 404를 구분한다.
- Error Boundary와 API Error State 역할을 구분한다.
- Accessibility와 Security는 최종 검수 필수 항목이다.

---

### [실무]

최종 판단 흐름:

```text
Frontend 화면 구현 / 검수 요청
→ 요청 종류 확인
→ UI State 분류
→ Loading / Error / Empty / Success 설계
→ Query / Mutation 상태 연결
→ Form / Route / Boundary 예외 처리
→ Accessibility 검수
→ Security 검수
→ Troubleshooting 위험 확인
→ Review Agent 최종 판정
```

전체 상태 전환:

```text
Request Start
→ Loading State
→ Request Success
  → Data Empty
    → Empty State
  → Data Exists
    → Success State
→ Request Failed
  → Error Type Mapping
  → Error State / Login Redirect / Forbidden / NotFound / Form Error
```

---

### [FAQ]

Q. Final Integration은 왜 필요해?
A. 개별 UX 규칙을 실제 Agent 판단 흐름으로 연결해 코드 생성과 리뷰에서 일관되게 적용하기 위해 필요하다.

Q. Error Handling & Loading UX의 최종 목표는?
A. 사용자가 요청 상태를 이해하고, 실패 시 복구 가능하며, 접근성과 보안 기준을 만족하는 Frontend UX를 만드는 것이다.

Q. 가장 중요한 상태 구분은?
A. Loading, Error, Empty, Success를 혼동하지 않는 것이다.

Q. 최종 검수에서 반드시 봐야 하는 것은?
A. 상태 구분, Query/Mutation 연결, Error Mapping, Accessibility, Security, Troubleshooting 위험이다.

---

# 2. Agent Decision Flow

## 2.1 PM Agent Decision Flow

### [개념]

PM Agent는 사용자 요구사항을 기능 단위로 해석하고 Error Handling & Loading UX가 필요한 화면과 요청 흐름을 식별한다.

PM Agent는 구현 세부 코드보다 화면 상태, 사용자 행동, 실패 상황, 완료 기준을 정의하는 역할을 한다.

---

### [핵심]

PM Agent 판단 대상:

- 화면 종류
- 사용자 액션
- API 요청 여부
- 인증 필요 여부
- 권한 필요 여부
- 목록 / 상세 / Form / Route 여부
- Loading 필요 여부
- Error 복구 액션
- Empty State 필요 여부
- Success Feedback 필요 여부
- 완료 판정 기준

핵심 규칙:

- 기능 요구사항에 Loading / Error / Empty / Success 상태를 포함한다.
- 인증 필요 화면은 Auth Loading과 Login Redirect를 정의한다.
- 권한 필요 화면은 Forbidden UX를 정의한다.
- 목록 화면은 Empty State와 Error State를 포함한다.
- Form 화면은 Submit Loading과 Field Error를 포함한다.
- Mutation 액션은 Success Feedback과 데이터 동기화를 포함한다.
- 완료 기준에 Accessibility와 Security를 포함한다.

---

### [실무]

PM Agent 요구사항 분해 예:

```text
요구사항: 축제 목록 검색 화면

PM Agent 정의:
- Initial Loading 필요
- Search Result Empty 필요
- Filter Empty 필요
- API Error State + Retry 필요
- 검색 조건 변경 시 Refetch Loading 필요
- 필터 변경 시 page 초기화 필요
- Success State는 목록 렌더링
- Error Message는 사용자용 문구 사용
```

Form 요구사항 예:

```text
요구사항: 리뷰 작성 Form

PM Agent 정의:
- Submit Loading 필요
- rating / content Field Error 필요
- 서버 Validation Error Mapping 필요
- 등록 성공 Toast 필요
- reviews query invalidate 필요
- 실패 후 입력값 유지 필요
- 중복 제출 방지 필요
```

권장:

- 화면별 UX 상태를 요구사항에 포함한다.
- 실패 시 사용자가 할 수 있는 행동을 정의한다.
- 인증 / 권한 / 리소스 없음 상태를 미리 정의한다.
- Review Agent가 검수할 수 있는 완료 기준을 명시한다.

주의:

- “API 연결”만 요구사항으로 두지 않는다.
- Loading / Error / Empty 누락을 사소한 UI 문제가 아니라 기능 누락으로 본다.
- Success Feedback 없이 완료 처리하지 않는다.
- 민감정보 노출 방지 기준을 요구사항에서 제외하지 않는다.

---

### [FAQ]

Q. PM Agent는 Error Handling UX에서 무엇을 해야 해?
A. 기능 요구사항에 Loading, Error, Empty, Success, 인증, 권한, 완료 기준을 포함해야 한다.

Q. PM Agent가 코드까지 작성해야 해?
A. 아니다. PM Agent는 화면 상태와 UX 요구사항을 정의하고 구현은 Frontend Agent가 수행한다.

Q. 목록 화면 요구사항에는 무엇이 포함되어야 해?
A. Initial Loading, Error State, Empty State, Success List, Retry, Refetch 기준이 포함되어야 한다.

Q. Form 화면 요구사항에는 무엇이 포함되어야 해?
A. Submit Loading, Field Error, Global Error, Success Feedback, 실패 후 복구 기준이 포함되어야 한다.

---

## 2.2 Frontend Agent Decision Flow

### [개념]

Frontend Agent는 PM Agent가 정의한 요구사항을 실제 React 컴포넌트, TanStack Query 상태, Form 상태, Route Guard, State Component로 구현한다.

Frontend Agent는 단순히 데이터를 출력하는 것이 아니라 상태 전환과 사용자 피드백까지 구현해야 한다.

---

### [핵심]

Frontend Agent 구현 대상:

- LoadingState
- ErrorState
- EmptyState
- Success Feedback
- useQuery 상태 연결
- useMutation 상태 연결
- queryKey 설계
- invalidateQueries
- FieldError
- FormAlert
- ProtectedRoute
- ForbiddenPage
- NotFoundPage
- Error Boundary
- Accessibility Attribute
- Safe Error Message

핵심 규칙:

- 조건부 렌더링은 Loading → Error → Empty → Success 순서를 따른다.
- `isLoading`, `isFetching`, `isPending`을 구분한다.
- API Error는 ErrorState로 처리한다.
- Render Error는 Error Boundary로 처리한다.
- Mutation 성공 후 관련 Query를 invalidate한다.
- Form Error는 input 근처에 표시한다.
- Retry Button은 실제 refetch와 연결한다.
- 서버 원문 error를 그대로 출력하지 않는다.

---

### [실무]

Frontend Agent 기본 구현 흐름:

```text
화면 컴포넌트 생성
→ queryKey 설계
→ useQuery / useMutation 연결
→ LoadingState 구현
→ ErrorState 구현
→ EmptyState 구현
→ Success 렌더링
→ Mutation Success / Error 처리
→ Accessibility 적용
→ Security Message 확인
```

조회 화면 예:

```tsx
function ListPage() {
  const { data, isLoading, isFetching, isError, error, refetch } = useQuery({
    queryKey: ["items"],
    queryFn: getItems,
  });

  if (isLoading) {
    return <LoadingState message="목록을 불러오는 중입니다." />;
  }

  if (isError) {
    return <ErrorState message={getApiErrorMessage(error)} onRetry={refetch} />;
  }

  if (!data || data.length === 0) {
    return <EmptyState title="표시할 데이터가 없습니다." />;
  }

  return (
    <>
      {isFetching && <p role="status">최신 정보를 확인 중입니다.</p>}
      <ItemList items={data} />
    </>
  );
}
```

권장:

- 공통 State Component를 적극 사용한다.
- 화면별 메시지는 props로 전달한다.
- queryKey와 invalidate key를 같이 설계한다.
- 접근성 속성은 컴포넌트 기본값으로 포함한다.

주의:

- `console.log(error)`만 남기고 ErrorState를 생략하지 않는다.
- `data.length === 0`을 Loading보다 먼저 검사하지 않는다.
- Mutation 성공 후 Toast만 띄우고 cache 갱신을 누락하지 않는다.
- 401 / 403 / 404를 같은 ErrorState로 뭉개지 않는다.

---

### [FAQ]

Q. Frontend Agent는 어떤 순서로 구현해야 해?
A. Query/Mutation 상태를 연결한 뒤 Loading, Error, Empty, Success 순서로 UI를 구성해야 한다.

Q. Frontend Agent가 가장 많이 실수하는 부분은?
A. Error State 누락, Empty Flicker, isLoading/isFetching 혼동, mutation invalidate 누락이다.

Q. Error Boundary가 있으면 API ErrorState를 생략해도 돼?
A. 아니다. Error Boundary는 렌더링 오류용이고 API ErrorState는 별도로 필요하다.

Q. Mutation 성공 후 반드시 해야 하는 것은?
A. Success Feedback과 관련 Query invalidate 또는 cache update를 수행해야 한다.

---

## 2.3 Review Agent Decision Flow

### [개념]

Review Agent는 구현 결과가 Error Handling & Loading UX 기준을 만족하는지 검수한다.

Review Agent는 단순 동작 여부가 아니라 사용자 상태 전달, 복구 가능성, 접근성, 보안 노출, stale UI 위험을 기준으로 판단한다.

---

### [핵심]

Review Agent 검수 대상:

- UI State Completeness
- Conditional Rendering Order
- Loading UX
- Error Mapping
- Empty State Timing
- Success Feedback
- Query Key / Invalidation
- Mutation Pending
- Retry Connection
- Form Error Mapping
- Route Guard
- Error Boundary Role
- Accessibility
- Security
- Troubleshooting Risk

핵심 규칙:

- 보안 정보 노출은 Critical로 판단한다.
- Error/Empty 혼동은 Major 이상으로 판단한다.
- Loading 누락은 UX 결함으로 판단한다.
- Retry 미연결은 UX Bug로 판단한다.
- Field Error를 Toast로만 처리하면 수정 요청한다.
- 401 / 403 혼동은 수정 요청한다.
- Query invalidate 누락은 stale UI 위험으로 판단한다.
- Accessibility 누락은 Severity를 상황에 맞게 부여한다.

---

### [실무]

Review Agent 검수 순서:

```text
상태 UI 존재 확인
→ 조건부 렌더링 순서 확인
→ API Error 처리 확인
→ Empty 판정 시점 확인
→ Mutation 성공 처리 확인
→ Query Invalidation 확인
→ Form / Route / Boundary 확인
→ Accessibility 확인
→ Security 확인
→ Severity 판정
```

Severity 기준:

| Severity | 기준                            | 예                             |
| -------- | ------------------------------- | ------------------------------ |
| Critical | 보안 정보 노출 / 앱 전체 crash  | token 노출, stack trace 노출   |
| High     | 주요 상태 누락 / 인증 권한 오류 | ErrorState 없음, 401/403 혼동  |
| Medium   | UX 혼란 / stale UI              | Empty Flicker, invalidate 누락 |
| Low      | 문구 / CTA / 작은 접근성 개선   | Empty 문구 부족                |

Review 출력 예:

```md
## Review Result

### Critical

- 서버 원문 error.message를 Toast로 그대로 노출하고 있음.

### High

- API 실패 시 ErrorState가 없고 EmptyState로 처리됨.

### Medium

- mutation 성공 후 관련 query invalidate가 누락됨.

### Low

- EmptyState 문구에 다음 행동 안내가 부족함.
```

---

### [FAQ]

Q. Review Agent는 무엇을 가장 우선 봐야 해?
A. 보안 노출, 상태 UI 누락, Error/Empty 혼동, 인증/권한 처리, stale UI 위험을 우선 봐야 한다.

Q. Error/Empty 혼동은 왜 심각해?
A. 사용자가 실패 상태를 데이터 없음으로 오해하고 복구 행동을 할 수 없기 때문이다.

Q. Query Invalidation 누락은 왜 문제야?
A. 성공 후 화면이 오래된 데이터를 계속 보여줄 수 있기 때문이다.

Q. Review Agent는 접근성도 봐야 해?
A. 그렇다. 상태 UX는 모든 사용자가 이해할 수 있어야 하므로 접근성은 필수 검수 항목이다.

---

# 3. Final Code Generation Rules

## 3.1 Generated Code Requirements

### [개념]

Generated Code Requirements는 Frontend Agent가 Error Handling & Loading UX 기준을 반영한 코드를 생성할 때 반드시 포함해야 하는 최소 요건이다.

이 기준은 코드 생성 산출물이 바로 Review Agent 검수 기준을 통과할 수 있도록 하기 위한 필수 조건이다.

---

### [핵심]

생성 코드 필수 조건:

- Loading State
- Error State
- Empty State
- Success Render
- Safe Conditional Rendering
- Safe Error Message
- Retry Action optional
- TanStack Query Status Mapping
- Mutation Pending Button
- Query Invalidation
- Form Field Error
- Global Form Error
- Accessibility Attributes
- No Raw Server Error
- No Sensitive Log

핵심 규칙:

- 조회 화면은 Loading / Error / Empty / Success를 모두 고려한다.
- Form 화면은 Field Error / Global Error / Submit Loading을 포함한다.
- Mutation 코드는 onSuccess / onError를 포함한다.
- Error Message는 mapping 함수를 통해 사용자 메시지로 변환한다.
- Retry Button이 있으면 실제 함수와 연결한다.
- 성공 후 관련 데이터를 갱신한다.
- 접근성 속성을 기본 포함한다.
- 서버 내부 오류 원문을 출력하지 않는다.

---

### [실무]

조회 화면 최소 구조:

```tsx
if (isLoading) {
  return <LoadingState message="데이터를 불러오는 중입니다." />;
}

if (isError) {
  return <ErrorState message={getApiErrorMessage(error)} onRetry={refetch} />;
}

if (!data || data.length === 0) {
  return <EmptyState title="표시할 데이터가 없습니다." />;
}

return <List data={data} />;
```

Mutation 최소 구조:

```tsx
const mutation = useMutation({
  mutationFn: saveItem,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ["items"] });
    toast.success("저장되었습니다.");
  },
  onError: (error) => {
    setFormError(getApiErrorMessage(error));
  },
});
```

Form Field Error 최소 구조:

```tsx
<input
  name="email"
  aria-invalid={Boolean(errors.email)}
  aria-describedby={errors.email ? "email-error" : undefined}
/>
<FieldError id="email-error" message={errors.email} />
```

---

### [FAQ]

Q. 생성 코드에서 반드시 포함해야 하는 상태는?
A. 조회 화면 기준 Loading, Error, Empty, Success 상태를 모두 고려해야 한다.

Q. Mutation 코드에서 반드시 포함해야 하는 것은?
A. pending 처리, success feedback, query invalidate, error handling이 필요하다.

Q. Error Message는 어떻게 생성해야 해?
A. 서버 원문을 그대로 쓰지 말고 getApiErrorMessage 같은 mapping 함수를 통해 사용자 메시지로 변환해야 한다.

Q. Field Error는 어떻게 생성해야 해?
A. input 근처에 표시하고 aria-invalid, aria-describedby로 연결해야 한다.

---

## 3.2 Generated Code Anti-Patterns

### [개념]

Generated Code Anti-Patterns는 Frontend Agent가 생성하면 안 되는 Error Handling & Loading UX 코드 패턴이다.

이 패턴들은 Review Agent에서 수정 요청 또는 Fail 판정을 받아야 한다.

---

### [핵심]

금지 또는 지양 패턴:

- Loading State 없음
- Error State 없음
- Empty State 먼저 검사
- API 실패를 빈 배열로 변환
- `console.log(error)`만 사용
- 서버 원문 `error.message` 그대로 표시
- Retry Button 미연결
- Submit Button pending 미처리
- Mutation 성공 후 invalidate 누락
- Field Error를 Toast로만 표시
- 401 / 403 동일 처리
- API Error를 Error Boundary에 의존
- token / stack trace / SQL Error 노출
- queryKey에 filter 누락
- useEffect fetch와 useQuery 중복 사용

핵심 규칙:

- 상태 누락은 기능 누락으로 본다.
- 보안 노출은 Critical Issue로 본다.
- Error/Empty 혼동은 Major Issue로 본다.
- Query stale 위험은 Medium 이상으로 본다.
- 접근성 누락은 화면 중요도에 따라 Severity를 부여한다.

---

### [실무]

나쁜 예:

```tsx
if (items.length === 0) {
  return <EmptyState title="데이터 없음" />;
}

if (loading) {
  return <LoadingState />;
}
```

문제:

- Loading보다 Empty를 먼저 검사해 Empty Flicker가 발생한다.

나쁜 예:

```tsx
catch (error) {
  console.log(error);
}
```

문제:

- 사용자에게 Error State가 전달되지 않는다.

나쁜 예:

```tsx
toast.error(error.response.data.message);
```

문제:

- 서버 원문 메시지에 내부 정보가 포함될 수 있다.

나쁜 예:

```tsx
const mutation = useMutation({
  mutationFn: createReview,
  onSuccess: () => {
    toast.success("등록되었습니다.");
  },
});
```

문제:

- 관련 query invalidate가 없어 stale UI가 남을 수 있다.

---

### [FAQ]

Q. 가장 위험한 Anti-Pattern은?
A. token, stack trace, SQL Error, 서버 원문 message 같은 민감정보를 사용자에게 노출하는 것이다.

Q. 가장 흔한 UX Anti-Pattern은?
A. Loading / Error / Empty 상태 누락과 Empty Flicker다.

Q. console.log(error)만 있으면 안 돼?
A. 안 된다. 개발 로그와 별개로 사용자에게 Error State를 제공해야 한다.

Q. 성공 Toast만 있으면 Mutation 처리가 끝난 거야?
A. 아니다. 관련 Query invalidate 또는 cache update가 필요할 수 있다.

---

# 4. Retrieval Map by Scenario

## 4.1 List Page Retrieval Map

### [개념]

List Page Retrieval Map은 목록 화면을 구현하거나 검수할 때 검색해야 할 Error Handling & Loading UX 기준이다.

목록 화면은 Loading, Error, Empty, Success, Pagination, Refetch, Search / Filter 상태가 모두 자주 발생한다.

---

### [핵심]

검색 키워드:

- List Page Loading
- Initial Loading
- Refetch Loading
- Error State
- Empty State
- Search Result Empty
- Filter Empty
- Pagination Loading
- Infinite Scroll Loading
- Retry Button
- TanStack Query isLoading isFetching
- queryKey filter page sort
- placeholderData
- Empty Flicker
- Stale UI

핵심 규칙:

- 초기 로딩과 재조회 로딩을 구분한다.
- 검색 결과 없음과 API 실패를 구분한다.
- 필터 변경 시 page를 초기화한다.
- queryKey에 filter, sort, page를 포함한다.
- Refetch 중 기존 데이터 유지 여부를 결정한다.
- Empty State는 요청 성공 후에만 표시한다.

---

### [실무]

목록 화면 검수 기준:

```md
- [ ] isLoading → Initial Loading
- [ ] isError → ErrorState + Retry
- [ ] isSuccess + empty → EmptyState
- [ ] isFetching + data exists → Refetch Indicator
- [ ] queryKey includes filter / sort / page
- [ ] filter change resets page
- [ ] API failure is not shown as Empty
- [ ] Empty Flicker is prevented
```

추천 검색 쿼리:

```text
목록 화면 Loading Error Empty Success
TanStack Query isLoading isFetching 목록 UX
검색 결과 없음 Empty State
필터 변경 queryKey page reset
Empty Flicker 초기 빈 배열
```

---

### [FAQ]

Q. 목록 화면 구현 시 어떤 Part를 우선 검색해?
A. UI State Classification, Loading UX, Empty State, TanStack Query UX, Troubleshooting 기준을 우선 검색한다.

Q. 목록 화면에서 가장 흔한 오류는?
A. Empty Flicker, ErrorState 누락, isLoading/isFetching 혼동, queryKey 필터 누락이다.

Q. 검색 결과 없음과 API 실패는 어떻게 구분해?
A. API 요청이 성공했고 데이터가 없으면 Empty State이고, 요청이 실패하면 Error State다.

Q. 필터 변경 시 무엇을 확인해야 해?
A. queryKey에 필터가 포함되는지, page가 초기화되는지, Loading/Refetch UI가 있는지 확인해야 한다.

---

## 4.2 Detail Page Retrieval Map

### [개념]

Detail Page Retrieval Map은 상세 화면을 구현하거나 검수할 때 검색해야 할 Error Handling & Loading UX 기준이다.

상세 화면은 route param, API Resource 404, Detail Loading, ErrorState, Resource NotFoundState가 핵심이다.

---

### [핵심]

검색 키워드:

- Detail Page Loading
- Route Param
- enabled query
- Resource Not Found
- API 404
- Route 404 vs API 404
- Detail Skeleton
- Error State Retry
- NotFoundState
- TanStack Query enabled
- Error Boundary
- map undefined
- Blank Screen

핵심 규칙:

- route param이 준비된 뒤 Query를 실행한다.
- 잘못된 param은 Invalid State 또는 Not Found로 처리한다.
- API Resource 404와 Route 404를 구분한다.
- 상세 데이터 없음은 일반 Empty보다 Resource NotFoundState를 고려한다.
- Detail Loading 또는 Skeleton을 제공한다.
- 데이터 접근 전 null check를 수행한다.

---

### [실무]

상세 화면 검수 기준:

```md
- [ ] route param validation exists
- [ ] enabled uses valid param
- [ ] isLoading → Detail Loading / Skeleton
- [ ] API 404 → Resource NotFoundState
- [ ] isError non-404 → ErrorState
- [ ] data null access is guarded
- [ ] Route 404 and Resource 404 are separated
```

추천 검색 쿼리:

```text
상세 페이지 Loading Resource Not Found
API 404 Route 404 차이
TanStack Query enabled route param
Detail Skeleton ErrorState
Blank Screen data undefined
```

---

### [FAQ]

Q. 상세 화면 구현 시 가장 중요한 것은?
A. route param 기반 Query 실행, Detail Loading, API Resource 404, ErrorState를 구분하는 것이다.

Q. 상세 데이터가 없으면 Empty State야?
A. 일반 목록 Empty보다 Resource NotFoundState가 더 적합한 경우가 많다.

Q. route param이 undefined일 때 요청해도 돼?
A. 아니다. enabled 조건이나 param validation으로 잘못된 요청을 막아야 한다.

Q. 상세 화면에서 Blank Screen이 생기는 이유는?
A. data null 접근, ErrorState 누락, route mismatch, Error Boundary 누락이 원인일 수 있다.

---

## 4.3 Form Page Retrieval Map

### [개념]

Form Page Retrieval Map은 입력 Form, 제출 Form, 로그인 Form, 리뷰 작성 Form, 프로필 수정 Form을 구현하거나 검수할 때 검색해야 할 기준이다.

Form 화면은 Field Error, Global Form Error, Submit Loading, Validation Mapping, Success Feedback이 핵심이다.

---

### [핵심]

검색 키워드:

- Form Error UX
- Field Error
- Global Form Error
- Server Field Error Mapping
- Submit Loading
- Submit Button Stuck
- Form Recovery
- Login Error UX
- Validation Error 400 422
- useMutation isPending
- FormAlert
- FieldError
- aria-invalid aria-describedby
- Success Feedback
- Query Invalidation

핵심 규칙:

- Field Error와 Global Error를 구분한다.
- Field Error는 input 근처에 표시한다.
- 서버 Validation Error를 Form State로 매핑한다.
- Submit Loading 중 버튼을 disabled 처리한다.
- 실패 후 입력값을 유지한다.
- 성공 후 reset / redirect / invalidate 기준을 정한다.
- 로그인 실패는 일반적인 Global Error로 처리한다.

---

### [실무]

Form 화면 검수 기준:

```md
- [ ] Submit Loading exists
- [ ] Submit Button disabled while pending
- [ ] Field Error appears near input
- [ ] aria-invalid / aria-describedby connected
- [ ] Global Form Error exists
- [ ] Server Validation Error mapped
- [ ] Inputs preserved after failure
- [ ] Success Feedback exists
- [ ] Query invalidate or redirect handled
```

추천 검색 쿼리:

```text
Form Error Field Error Global Error
Server Validation Error Mapping
Submit Loading mutation isPending
Login Error UX Global Form Error
Form Recovery 실패 후 입력값 유지
```

---

### [FAQ]

Q. Form 화면 구현 시 어떤 Part를 우선 검색해?
A. Form Error UX, Submit Loading, TanStack Query Mutation UX, Accessibility 기준을 우선 검색한다.

Q. Form에서 가장 흔한 오류는?
A. Field Error를 Toast로만 처리하거나, 서버 errors key와 input name이 맞지 않아 오류가 표시되지 않는 문제다.

Q. Submit Loading은 어떻게 검수해?
A. mutation.isPending 또는 isSubmitting과 버튼 disabled / loadingText가 연결되는지 확인한다.

Q. Form 성공 후 무엇을 해야 해?
A. Success Feedback, Query Invalidation, Form Reset 또는 Redirect 기준을 처리해야 한다.

---

## 4.4 Auth / Route Retrieval Map

### [개념]

Auth / Route Retrieval Map은 로그인, 회원가입, Protected Route, PublicOnlyRoute, ForbiddenPage, NotFoundPage를 구현하거나 검수할 때 검색해야 할 기준이다.

Auth / Route 화면은 401, 403, Route 404, Resource 404, auth initialized, redirect flicker가 핵심이다.

---

### [핵심]

검색 키워드:

- 401 Unauthorized UX
- 403 Forbidden UX
- Protected Route
- PublicOnlyRoute
- Auth Initialized
- Login Redirect
- Redirect Flicker
- ForbiddenPage
- NotFoundPage
- Route 404
- API Resource 404
- Token Refresh
- Role Loading
- Route Guard
- OAuth Callback

핵심 규칙:

- auth initialized 전에는 redirect하지 않는다.
- token refresh 중에는 Auth Loading을 보여준다.
- 401은 Login Redirect 또는 Refresh Flow와 연결한다.
- 403은 ForbiddenPage로 처리하고 logout하지 않는다.
- Route 404와 API Resource 404를 구분한다.
- 로그인 후 원래 위치로 복귀할 수 있다.
- PublicOnlyRoute에서도 initialized 확인 후 redirect한다.

---

### [실무]

Auth / Route 검수 기준:

```md
- [ ] auth initialized exists
- [ ] ProtectedRoute waits for initialized
- [ ] PublicOnlyRoute waits for initialized
- [ ] 401 and 403 are separated
- [ ] 403 does not logout by default
- [ ] ForbiddenPage exists
- [ ] NotFoundPage catch-all exists
- [ ] Route 404 and API 404 are separated
- [ ] token refresh state handled
- [ ] redirect loop checked
```

추천 검색 쿼리:

```text
Protected Route auth initialized
401 403 차이 Frontend UX
ForbiddenPage logout 금지
PublicOnlyRoute 로그인 페이지 flicker
Route 404 API 404 차이
```

---

### [FAQ]

Q. Auth Route 구현 시 가장 중요한 것은?
A. auth initialized 전 redirect를 막고 401과 403을 구분하는 것이다.

Q. 403이면 로그아웃해야 해?
A. 대부분 아니다. 로그인은 유지하고 권한 없음 UI를 보여주는 것이 적합하다.

Q. 로그인 페이지가 깜빡이는 이유는?
A. auth initialized 전에 PublicOnlyRoute나 ProtectedRoute가 redirect 판단을 했을 수 있다.

Q. API 404와 Route 404는 어떻게 구분해?
A. URL route 자체가 없는지, route는 있지만 API 리소스가 없는지 Network와 Router를 통해 구분한다.

---

# 5. Retrieval Map by Failure Symptom

## 5.1 Loading Problem Retrieval Map

### [개념]

Loading Problem Retrieval Map은 Loading이 끝나지 않거나, 화면이 깜빡이거나, 버튼이 계속 처리 중인 문제를 해결하기 위한 검색 기준이다.

---

### [핵심]

검색 키워드:

- Infinite Loading
- Submit Button Stuck
- isLoading isFetching
- isPending
- finally setLoading false
- enabled false
- auth initialized
- mutationFn Promise
- useEffect dependency loop
- Suspense Fallback
- Refetch Flicker

핵심 규칙:

- 요청 완료 여부를 Network에서 확인한다.
- 성공과 실패 모두 Loading 종료 경로가 있어야 한다.
- `enabled: false` 상태를 Loading으로 계속 보여주지 않는다.
- mutationFn은 Promise를 반환해야 한다.
- auth initialized는 실패해도 종료되어야 한다.
- Refetch는 전체 Loading으로 덮지 않는다.

---

### [실무]

Loading 문제 Debug:

```text
Loading 문제 발생
→ Network 요청 완료 확인
→ Promise resolve / reject 확인
→ finally 확인
→ Query enabled 확인
→ auth initialized 확인
→ mutationFn Promise 반환 확인
→ 조건부 렌더링 확인
```

추천 검색 쿼리:

```text
Infinite Loading finally enabled auth initialized
Submit Button Stuck mutationFn Promise
isLoading isFetching 차이
Refetch Flicker 기존 데이터 유지
```

---

### [FAQ]

Q. Loading 문제는 무엇부터 확인해?
A. Network 요청 완료 여부, finally, enabled 조건, auth initialized, mutationFn Promise 반환을 확인한다.

Q. enabled false인데 Loading이 계속 보이면?
A. 요청이 시작되지 않은 상태일 수 있으므로 Idle 또는 Guide State가 필요하다.

Q. Submit Button이 계속 처리 중이면?
A. mutationFn이 Promise를 반환하는지, error를 삼키지 않는지, pending 상태가 종료되는지 확인한다.

Q. Refetch 때 화면이 깜빡이면?
A. isFetching을 전체 Loading으로 처리하거나 기존 데이터를 지우는 구조인지 확인한다.

---

## 5.2 Error Problem Retrieval Map

### [개념]

Error Problem Retrieval Map은 오류가 발생했지만 메시지가 보이지 않거나, Retry가 동작하지 않거나, 서버 원문이 노출되는 문제를 해결하기 위한 검색 기준이다.

---

### [핵심]

검색 키워드:

- Error Message Not Showing
- ErrorState
- Error Message Mapping
- Promise.reject
- AxiosError
- getApiErrorMessage
- Retry Not Working
- refetch
- Network Error
- Server Error
- 400 401 403 404 409 422 500
- Security Error Message
- raw server message

핵심 규칙:

- catch 또는 onError에서 오류 상태를 설정한다.
- interceptor는 Promise.reject를 반환한다.
- error object shape를 Network Response로 확인한다.
- Error Message는 mapping 함수를 통해 변환한다.
- Retry Button은 실제 refetch와 연결한다.
- 서버 원문 message를 그대로 노출하지 않는다.

---

### [실무]

Error 문제 Debug:

```text
Error 문제 발생
→ catch / onError 진입 확인
→ error.response.data 확인
→ mapping 함수 확인
→ setError 확인
→ ErrorState 렌더링 확인
→ Promise.reject 확인
→ Retry onClick / refetch 확인
→ raw message 노출 확인
```

추천 검색 쿼리:

```text
Error Message Not Showing Promise.reject
getApiErrorMessage 서버 원문 노출
Retry Not Working refetch enabled
Network Error Server Error 차이
HTTP Status UX 401 403 404 500
```

---

### [FAQ]

Q. Error 문제가 생기면 무엇부터 확인해?
A. catch/onError 진입 여부, error object 구조, ErrorState 렌더링 조건, Promise.reject를 확인한다.

Q. Retry가 안 되면 무엇을 확인해?
A. onRetry 연결, refetch 호출, enabled 조건, Network 요청 발생 여부를 확인한다.

Q. 서버 원문 메시지가 보이면 왜 문제야?
A. 내부 경로, SQL, stack trace, token 같은 민감정보가 포함될 수 있기 때문이다.

Q. 401과 403을 같이 처리하면 안 돼?
A. 권장하지 않는다. 401은 인증 필요이고 403은 권한 없음이다.

---

## 5.3 Empty / Success Problem Retrieval Map

### [개념]

Empty / Success Problem Retrieval Map은 Empty State가 잘못 표시되거나 성공 후 화면이 갱신되지 않는 문제를 해결하기 위한 검색 기준이다.

---

### [핵심]

검색 키워드:

- Empty Flicker
- Empty State
- Search Empty
- Filter Empty
- Initial Empty Array
- isSuccess data empty
- Success Feedback Missing
- Query Invalidation
- Stale UI
- optimistic update
- cache update
- Toast Success
- Success Message
- Button State Change

핵심 규칙:

- Empty는 요청 성공 후에만 표시한다.
- Loading과 Error를 Empty보다 먼저 검사한다.
- 검색어 입력 전 Guide State와 Search Empty를 구분한다.
- 성공 후 관련 Query를 invalidate한다.
- Toast만 띄우고 데이터 갱신을 누락하지 않는다.
- Optimistic UI에는 rollback 기준이 필요하다.

---

### [실무]

Empty / Success 문제 Debug:

```text
Empty / Success 문제 발생
→ Loading / Error 검사 순서 확인
→ 요청 성공 여부 확인
→ 초기 data 값 확인
→ isSuccess 확인
→ onSuccess 실행 확인
→ invalidate queryKey 확인
→ cache update 확인
→ Success Message 확인
```

추천 검색 쿼리:

```text
Empty Flicker 초기 빈 배열
Search Empty Filter Empty 차이
Success Feedback Missing
Query Invalidation stale UI
Optimistic UI rollback
```

---

### [FAQ]

Q. Empty State가 잠깐 보이면 무엇을 확인해?
A. Empty를 Loading보다 먼저 검사하는지, 요청 성공 여부를 확인하는지, 초기 data가 빈 배열인지 확인한다.

Q. 성공했는데 화면이 안 바뀌면?
A. onSuccess, invalidateQueries, queryKey 일치 여부, cache update 여부를 확인한다.

Q. Search Empty와 입력 전 안내는 달라?
A. 다르다. 검색 요청 성공 후 결과 없음과 아직 검색 조건을 입력하지 않은 상태는 구분해야 한다.

Q. Optimistic UI에서 가장 중요한 것은?
A. 실패 시 rollback하고 최종 서버 상태와 동기화하는 것이다.

---

# 6. Final Quality Gate

## 6.1 Quality Gate Criteria

### [개념]

Quality Gate는 Error Handling & Loading UX 구현물이 완료 가능한 수준인지 판단하는 최종 기준이다.

Quality Gate는 단순히 코드가 빌드되는지보다 사용자가 상태를 이해하고 복구할 수 있는지, 보안 정보가 노출되지 않는지, 접근성이 유지되는지를 기준으로 한다.

---

### [핵심]

Pass 조건:

- Loading / Error / Empty / Success 상태가 명확하다.
- Query / Mutation 상태가 올바르게 연결된다.
- Form Error와 Route Error가 분리된다.
- Error Boundary 역할이 정확하다.
- Accessibility 기준을 만족한다.
- Security 노출 위험이 없다.
- Troubleshooting 주요 위험이 제거되어 있다.
- Review Agent가 Critical / High 이슈를 발견하지 않는다.

Fail 조건:

- 서버 원문 오류 또는 민감정보 노출
- ErrorState 누락
- Loading이 끝나지 않는 구조
- Empty와 Error 혼동
- Field Error 미표시
- 401 / 403 혼동
- API Error를 Error Boundary에 의존
- Mutation 성공 후 stale UI 방치
- Retry Button 미연결
- 앱 전체 Blank Screen 가능성

---

### [실무]

Quality Gate 판정:

```text
Critical Issue 1개 이상
→ Fail

High Issue 1개 이상
→ Major Fix Required

Medium Issue 여러 개
→ Fix Required

Low Issue만 존재
→ Minor Fix 후 Pass 가능

모든 핵심 기준 충족
→ Pass
```

최종 검수 표:

| 영역          | Pass 기준                               |
| ------------- | --------------------------------------- |
| State         | Loading / Error / Empty / Success 분리  |
| Query         | isLoading / isFetching / isPending 구분 |
| Error         | Safe Message + Retry 기준               |
| Empty         | 요청 성공 후 표시                       |
| Success       | Feedback + Data Sync                    |
| Form          | Field / Global Error 분리               |
| Route         | 401 / 403 / 404 구분                    |
| Boundary      | Render Error 전용                       |
| Accessibility | Text + Keyboard + ARIA                  |
| Security      | No sensitive exposure                   |

---

### [FAQ]

Q. Quality Gate에서 Fail이 되는 기준은?
A. 보안 정보 노출, ErrorState 누락, Error/Empty 혼동, 401/403 혼동, 앱 crash 가능성은 Fail 또는 Major Fix 대상이다.

Q. Critical Issue가 있으면 완료 처리해도 돼?
A. 아니다. Critical Issue가 있으면 반드시 수정 후 재검수해야 한다.

Q. Low Issue만 있으면 통과 가능해?
A. 핵심 흐름에 문제가 없고 문구나 작은 접근성 보완 수준이면 Minor Fix 후 Pass 가능하다.

Q. Quality Gate의 핵심 목적은?
A. 코드가 동작하는 것뿐 아니라 사용자가 상태를 이해하고 안전하게 복구할 수 있는지 보장하는 것이다.

---

# 7. Document Set Completion

## 7.1 Error Handling & Loading UX Document Set

### [개념]

Error Handling & Loading UX 문서 세트는 Frontend Foundation 단계에서 화면 상태, 오류 처리, 로딩 UX, 접근성, 보안, 검수 기준을 통합적으로 다루는 Domain Rules 문서다.

이 Part09는 전체 세트의 검색 연결, Agent 판단 흐름, 최종 Quality Gate 역할을 한다.

---

### [핵심]

문서 세트 구성:

```text
Part01 - UI State Classification
Part02 - Loading UX Rules
Part03 - Error State Rules
Part04 - Empty State & Success Feedback Rules
Part05 - TanStack Query UX Rules
Part06 - Form, Route & Error Boundary Rules
Part07 - Accessibility, Security & Troubleshooting Rules
Part08 - Component Pattern & Review Rules
Part09 - Final Integration & Retrieval Map
```

각 Part 역할:

| Part   | 역할                                             |
| ------ | ------------------------------------------------ |
| Part01 | UI 상태 분류 기준                                |
| Part02 | Loading UX 상세 기준                             |
| Part03 | Error State / HTTP Status UX                     |
| Part04 | Empty / Success Feedback 기준                    |
| Part05 | TanStack Query 상태 연결                         |
| Part06 | Form / Route / Error Boundary                    |
| Part07 | Accessibility / Security / Troubleshooting       |
| Part08 | Component Pattern / Agent Review                 |
| Part09 | Final Integration / Retrieval Map / Quality Gate |

---

### [실무]

RAG 적용 기준:

```text
사용자 질문이 목록 화면 구현
→ Part01 + Part02 + Part04 + Part05 + Part09 검색

사용자 질문이 Form Error 구현
→ Part03 + Part05 + Part06 + Part07 + Part09 검색

사용자 질문이 Route Guard 구현
→ Part03 + Part06 + Part07 + Part09 검색

사용자 질문이 코드 리뷰
→ Part08 + Part09 + 관련 증상 Part 검색

사용자 질문이 오류 증상 해결
→ Part07 + Part09 + 해당 상태 Part 검색
```

권장:

- Part09는 검색 라우터 역할로 사용한다.
- 구체 구현은 해당 Part를 함께 검색한다.
- Review Agent는 Part08과 Part09를 우선 참조한다.
- Frontend Agent는 구현 화면 유형에 맞는 Part를 조합한다.
- PM Agent는 Part09의 Decision Flow와 Quality Gate를 참조한다.

---

### [FAQ]

Q. Part09는 어떤 역할이야?
A. 전체 Error Handling & Loading UX 문서 세트를 Agent 판단 흐름과 검색 기준으로 통합하는 최종 문서다.

Q. 코드 생성 시 어떤 Part를 검색해야 해?
A. 화면 유형에 따라 다르지만 Part09에서 Retrieval Map을 확인한 뒤 관련 Part를 함께 검색하는 것이 좋다.

Q. 코드 리뷰 시 어떤 Part를 우선 봐?
A. Part08 Component Pattern & Review Rules와 Part09 Final Integration & Quality Gate를 우선 본다.

Q. Error Handling & Loading UX 문서 세트는 여기서 완료야?
A. 기본 Domain Rules 기준으로는 Part01부터 Part09까지 구성하면 완료 가능한 세트다.

---

# Retrieval Queries

### [FAQ]

Q. Error Handling & Loading UX Part09는 무엇을 다뤄?
A. 전체 문서 세트의 Final Integration, Agent Decision Flow, Retrieval Map, Quality Gate, 최종 검수 기준을 다룬다.

Q. Final Integration은 왜 필요해?
A. 개별 UX 규칙을 실제 Agent 판단 흐름으로 연결해 코드 생성과 리뷰에서 일관되게 적용하기 위해 필요하다.

Q. Error Handling & Loading UX의 최종 목표는?
A. 사용자가 요청 상태를 이해하고, 실패 시 복구 가능하며, 접근성과 보안 기준을 만족하는 Frontend UX를 만드는 것이다.

Q. 가장 중요한 상태 구분은?
A. Loading, Error, Empty, Success를 혼동하지 않는 것이다.

Q. 최종 검수에서 반드시 봐야 하는 것은?
A. 상태 구분, Query/Mutation 연결, Error Mapping, Accessibility, Security, Troubleshooting 위험이다.

Q. PM Agent는 Error Handling UX에서 무엇을 해야 해?
A. 기능 요구사항에 Loading, Error, Empty, Success, 인증, 권한, 완료 기준을 포함해야 한다.

Q. PM Agent가 코드까지 작성해야 해?
A. 아니다. PM Agent는 화면 상태와 UX 요구사항을 정의하고 구현은 Frontend Agent가 수행한다.

Q. 목록 화면 요구사항에는 무엇이 포함되어야 해?
A. Initial Loading, Error State, Empty State, Success List, Retry, Refetch 기준이 포함되어야 한다.

Q. Form 화면 요구사항에는 무엇이 포함되어야 해?
A. Submit Loading, Field Error, Global Error, Success Feedback, 실패 후 복구 기준이 포함되어야 한다.

Q. Frontend Agent는 어떤 순서로 구현해야 해?
A. Query/Mutation 상태를 연결한 뒤 Loading, Error, Empty, Success 순서로 UI를 구성해야 한다.

Q. Frontend Agent가 가장 많이 실수하는 부분은?
A. Error State 누락, Empty Flicker, isLoading/isFetching 혼동, mutation invalidate 누락이다.

Q. Error Boundary가 있으면 API ErrorState를 생략해도 돼?
A. 아니다. Error Boundary는 렌더링 오류용이고 API ErrorState는 별도로 필요하다.

Q. Mutation 성공 후 반드시 해야 하는 것은?
A. Success Feedback과 관련 Query invalidate 또는 cache update를 수행해야 한다.

Q. Review Agent는 무엇을 가장 우선 봐야 해?
A. 보안 노출, 상태 UI 누락, Error/Empty 혼동, 인증/권한 처리, stale UI 위험을 우선 봐야 한다.

Q. Error/Empty 혼동은 왜 심각해?
A. 사용자가 실패 상태를 데이터 없음으로 오해하고 복구 행동을 할 수 없기 때문이다.

Q. Query Invalidation 누락은 왜 문제야?
A. 성공 후 화면이 오래된 데이터를 계속 보여줄 수 있기 때문이다.

Q. Review Agent는 접근성도 봐야 해?
A. 그렇다. 상태 UX는 모든 사용자가 이해할 수 있어야 하므로 접근성은 필수 검수 항목이다.

Q. 생성 코드에서 반드시 포함해야 하는 상태는?
A. 조회 화면 기준 Loading, Error, Empty, Success 상태를 모두 고려해야 한다.

Q. Mutation 코드에서 반드시 포함해야 하는 것은?
A. pending 처리, success feedback, query invalidate, error handling이 필요하다.

Q. Error Message는 어떻게 생성해야 해?
A. 서버 원문을 그대로 쓰지 말고 getApiErrorMessage 같은 mapping 함수를 통해 사용자 메시지로 변환해야 한다.

Q. Field Error는 어떻게 생성해야 해?
A. input 근처에 표시하고 aria-invalid, aria-describedby로 연결해야 한다.

Q. 가장 위험한 Anti-Pattern은?
A. token, stack trace, SQL Error, 서버 원문 message 같은 민감정보를 사용자에게 노출하는 것이다.

Q. 가장 흔한 UX Anti-Pattern은?
A. Loading / Error / Empty 상태 누락과 Empty Flicker다.

Q. console.log(error)만 있으면 안 돼?
A. 안 된다. 개발 로그와 별개로 사용자에게 Error State를 제공해야 한다.

Q. 성공 Toast만 있으면 Mutation 처리가 끝난 거야?
A. 아니다. 관련 Query invalidate 또는 cache update가 필요할 수 있다.

Q. 목록 화면 구현 시 어떤 Part를 우선 검색해?
A. UI State Classification, Loading UX, Empty State, TanStack Query UX, Troubleshooting 기준을 우선 검색한다.

Q. 목록 화면에서 가장 흔한 오류는?
A. Empty Flicker, ErrorState 누락, isLoading/isFetching 혼동, queryKey 필터 누락이다.

Q. 검색 결과 없음과 API 실패는 어떻게 구분해?
A. API 요청이 성공했고 데이터가 없으면 Empty State이고, 요청이 실패하면 Error State다.

Q. 필터 변경 시 무엇을 확인해야 해?
A. queryKey에 필터가 포함되는지, page가 초기화되는지, Loading/Refetch UI가 있는지 확인해야 한다.

Q. 상세 화면 구현 시 가장 중요한 것은?
A. route param 기반 Query 실행, Detail Loading, API Resource 404, ErrorState를 구분하는 것이다.

Q. 상세 데이터가 없으면 Empty State야?
A. 일반 목록 Empty보다 Resource NotFoundState가 더 적합한 경우가 많다.

Q. route param이 undefined일 때 요청해도 돼?
A. 아니다. enabled 조건이나 param validation으로 잘못된 요청을 막아야 한다.

Q. 상세 화면에서 Blank Screen이 생기는 이유는?
A. data null 접근, ErrorState 누락, route mismatch, Error Boundary 누락이 원인일 수 있다.

Q. Form 화면 구현 시 어떤 Part를 우선 검색해?
A. Form Error UX, Submit Loading, TanStack Query Mutation UX, Accessibility 기준을 우선 검색한다.

Q. Form에서 가장 흔한 오류는?
A. Field Error를 Toast로만 처리하거나, 서버 errors key와 input name이 맞지 않아 오류가 표시되지 않는 문제다.

Q. Submit Loading은 어떻게 검수해?
A. mutation.isPending 또는 isSubmitting과 버튼 disabled / loadingText가 연결되는지 확인한다.

Q. Form 성공 후 무엇을 해야 해?
A. Success Feedback, Query Invalidation, Form Reset 또는 Redirect 기준을 처리해야 한다.

Q. Auth Route 구현 시 가장 중요한 것은?
A. auth initialized 전 redirect를 막고 401과 403을 구분하는 것이다.

Q. 403이면 로그아웃해야 해?
A. 대부분 아니다. 로그인은 유지하고 권한 없음 UI를 보여주는 것이 적합하다.

Q. 로그인 페이지가 깜빡이는 이유는?
A. auth initialized 전에 PublicOnlyRoute나 ProtectedRoute가 redirect 판단을 했을 수 있다.

Q. API 404와 Route 404는 어떻게 구분해?
A. URL route 자체가 없는지, route는 있지만 API 리소스가 없는지 Network와 Router를 통해 구분한다.

Q. Loading 문제는 무엇부터 확인해?
A. Network 요청 완료 여부, finally, enabled 조건, auth initialized, mutationFn Promise 반환을 확인한다.

Q. enabled false인데 Loading이 계속 보이면?
A. 요청이 시작되지 않은 상태일 수 있으므로 Idle 또는 Guide State가 필요하다.

Q. Submit Button이 계속 처리 중이면?
A. mutationFn이 Promise를 반환하는지, error를 삼키지 않는지, pending 상태가 종료되는지 확인한다.

Q. Refetch 때 화면이 깜빡이면?
A. isFetching을 전체 Loading으로 처리하거나 기존 데이터를 지우는 구조인지 확인한다.

Q. Error 문제가 생기면 무엇부터 확인해?
A. catch/onError 진입 여부, error object 구조, ErrorState 렌더링 조건, Promise.reject를 확인한다.

Q. Retry가 안 되면 무엇을 확인해?
A. onRetry 연결, refetch 호출, enabled 조건, Network 요청 발생 여부를 확인한다.

Q. 서버 원문 메시지가 보이면 왜 문제야?
A. 내부 경로, SQL, stack trace, token 같은 민감정보가 포함될 수 있기 때문이다.

Q. 401과 403을 같이 처리하면 안 돼?
A. 권장하지 않는다. 401은 인증 필요이고 403은 권한 없음이다.

Q. Empty State가 잠깐 보이면 무엇을 확인해?
A. Empty를 Loading보다 먼저 검사하는지, 요청 성공 여부를 확인하는지, 초기 data가 빈 배열인지 확인한다.

Q. 성공했는데 화면이 안 바뀌면?
A. onSuccess, invalidateQueries, queryKey 일치 여부, cache update 여부를 확인한다.

Q. Search Empty와 입력 전 안내는 달라?
A. 다르다. 검색 요청 성공 후 결과 없음과 아직 검색 조건을 입력하지 않은 상태는 구분해야 한다.

Q. Optimistic UI에서 가장 중요한 것은?
A. 실패 시 rollback하고 최종 서버 상태와 동기화하는 것이다.

Q. Quality Gate에서 Fail이 되는 기준은?
A. 보안 정보 노출, ErrorState 누락, Error/Empty 혼동, 401/403 혼동, 앱 crash 가능성은 Fail 또는 Major Fix 대상이다.

Q. Critical Issue가 있으면 완료 처리해도 돼?
A. 아니다. Critical Issue가 있으면 반드시 수정 후 재검수해야 한다.

Q. Low Issue만 있으면 통과 가능해?
A. 핵심 흐름에 문제가 없고 문구나 작은 접근성 보완 수준이면 Minor Fix 후 Pass 가능하다.

Q. Quality Gate의 핵심 목적은?
A. 코드가 동작하는 것뿐 아니라 사용자가 상태를 이해하고 안전하게 복구할 수 있는지 보장하는 것이다.

Q. Part09는 어떤 역할이야?
A. 전체 Error Handling & Loading UX 문서 세트를 Agent 판단 흐름과 검색 기준으로 통합하는 최종 문서다.

Q. 코드 생성 시 어떤 Part를 검색해야 해?
A. 화면 유형에 따라 다르지만 Part09에서 Retrieval Map을 확인한 뒤 관련 Part를 함께 검색하는 것이 좋다.

Q. 코드 리뷰 시 어떤 Part를 우선 봐?
A. Part08 Component Pattern & Review Rules와 Part09 Final Integration & Quality Gate를 우선 본다.

Q. Error Handling & Loading UX 문서 세트는 여기서 완료야?
A. 기본 Domain Rules 기준으로는 Part01부터 Part09까지 구성하면 완료 가능한 세트다.
