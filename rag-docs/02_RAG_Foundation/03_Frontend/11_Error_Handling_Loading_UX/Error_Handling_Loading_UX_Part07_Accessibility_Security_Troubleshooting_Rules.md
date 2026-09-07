# Error Handling & Loading UX Part07 - Accessibility, Security & Troubleshooting Rules

---

# 1. Accessibility Overview

## 1.1 Accessibility Purpose

### [개념]

Accessibility는 Loading, Error, Empty, Success 상태를 시각 사용자뿐 아니라 키보드 사용자, 스크린 리더 사용자, 보조 기술 사용자도 이해하고 조작할 수 있게 만드는 기준이다.

Error Handling & Loading UX에서 접근성은 선택 사항이 아니라 상태 전달의 핵심 기준이다.

---

### [핵심]

Accessibility 주요 대상:

- Loading State Accessibility
- Error State Accessibility
- Empty State Accessibility
- Success Feedback Accessibility
- Form Error Accessibility
- Route Error Accessibility
- Fallback UI Accessibility
- Toast Accessibility
- Retry Button Accessibility
- Disabled State Accessibility
- Focus Management
- Keyboard Navigation
- ARIA Attributes

핵심 규칙:

- 시각적 표시만으로 상태를 전달하지 않는다.
- Loading, Error, Success 메시지는 텍스트로 제공한다.
- Spinner, Skeleton, Icon은 보조 설명이 필요할 수 있다.
- Field Error는 input과 연결한다.
- Retry Button, CTA, Link는 키보드로 접근 가능해야 한다.
- 색상만으로 성공 / 실패 / 경고를 구분하지 않는다.
- role과 aria 속성은 필요한 곳에만 사용한다.
- aria-live는 과도하게 남발하지 않는다.

---

### [실무]

상태별 접근성 기준:

| 상태             | 접근성 기준                                   |
| ---------------- | --------------------------------------------- |
| Loading State    | `role="status"`, `aria-busy`, Loading Message |
| Error State      | `role="alert"`, Retry Button, Text Message    |
| Empty State      | Heading, Description, CTA                     |
| Success Feedback | `role="status"`, Text Message                 |
| Field Error      | `aria-invalid`, `aria-describedby`            |
| Fallback UI      | Heading, Safe Message, Navigation Action      |
| Toast            | Screen Reader Announcement, 충분한 표시 시간  |

접근성 처리 흐름:

```text
UI State 발생
→ 시각 표시 제공
→ 텍스트 메시지 제공
→ 보조 기술 전달 방식 확인
→ 키보드 조작 가능성 확인
→ Focus 흐름 확인
→ 색상 의존성 제거
```

---

### [FAQ]

Q. Error Handling & Loading UX에서 접근성이 왜 중요해?
A. Loading, Error, Empty, Success 상태를 모든 사용자가 이해하고 다음 행동을 할 수 있어야 하기 때문이다.

Q. Spinner만 보여주면 접근성에 충분해?
A. 아니다. 스크린 리더가 이해할 수 있는 텍스트나 `role="status"` 같은 속성이 필요하다.

Q. Error Message는 색상만 빨갛게 하면 돼?
A. 아니다. 텍스트, 아이콘, ARIA 속성 등 색상 외 정보가 필요하다.

Q. 접근성 속성은 많이 넣을수록 좋아?
A. 아니다. 필요한 곳에 정확히 사용하는 것이 중요하다.

---

# 2. Loading Accessibility Rules

## 2.1 Loading Message Accessibility

### [개념]

Loading Message Accessibility는 사용자가 현재 요청이 진행 중임을 보조 기술로도 알 수 있게 하는 기준이다.

Loading UI는 Spinner나 Skeleton 같은 시각적 요소만으로 구성하지 않고 텍스트 또는 접근 가능한 label을 함께 제공해야 한다.

---

### [핵심]

Loading 접근성 대상:

- Page Loading
- Section Loading
- Button Loading
- Refetch Loading
- Infinite Loading
- Auth Loading
- Suspense Fallback
- Skeleton UI
- Spinner UI

핵심 규칙:

- Loading 상태를 텍스트로 설명한다.
- 중요한 Loading에는 `role="status"`를 고려한다.
- 콘텐츠 영역에는 `aria-busy`를 사용할 수 있다.
- Spinner 아이콘은 장식이면 `aria-hidden` 처리한다.
- Skeleton은 대체로 장식 요소로 처리한다.
- Button Loading은 버튼 문구를 변경한다.
- Refetch처럼 자주 발생하는 상태는 live announcement를 최소화한다.

---

### [실무]

Page Loading 예:

```tsx
function PageLoading() {
  return (
    <section aria-busy="true">
      <p role="status">데이터를 불러오는 중입니다.</p>
    </section>
  );
}
```

Button Loading 예:

```tsx
<button type="submit" disabled={isSubmitting}>
  {isSubmitting ? "저장 중..." : "저장"}
</button>
```

Skeleton 예:

```tsx
<section aria-busy="true" aria-label="축제 목록을 불러오는 중입니다.">
  <div aria-hidden="true">
    <FestivalCardSkeleton />
    <FestivalCardSkeleton />
    <FestivalCardSkeleton />
  </div>
</section>
```

Refetch 예:

```tsx
{
  isFetching && (
    <p role="status" aria-live="polite">
      최신 정보를 확인 중입니다.
    </p>
  );
}
```

권장:

- 사용자에게 현재 무엇을 기다리는지 알려준다.
- 버튼 내부 Loading은 문구 변경으로 전달한다.
- Skeleton은 읽히지 않게 하고 전체 Loading Message를 제공한다.
- 긴 Loading에는 의미 있는 메시지를 제공한다.
- Auth Loading은 “인증 상태를 확인 중입니다.”처럼 구체적으로 작성한다.

주의:

- Spinner icon만 있고 텍스트가 없으면 상태 전달이 부족하다.
- Skeleton item 여러 개가 모두 읽히면 스크린 리더 사용자에게 방해가 된다.
- `aria-live`가 너무 자주 바뀌면 피로감을 준다.
- Loading 때문에 사용자의 focus를 강제로 이동하지 않는다.

---

### [FAQ]

Q. Loading Message는 꼭 필요해?
A. 시각적 표시만으로 상태 전달이 어려우므로 텍스트나 접근성 label을 제공하는 것이 좋다.

Q. Spinner에는 어떤 접근성 처리가 필요해?
A. Spinner 자체는 장식이면 `aria-hidden` 처리하고, 주변에 `role="status"`나 텍스트 메시지를 제공한다.

Q. Skeleton은 스크린 리더가 읽어야 해?
A. 대부분 장식 요소로 보고 `aria-hidden` 처리하거나 별도 Loading Message를 제공하는 것이 좋다.

Q. Refetch 메시지를 항상 읽히게 해야 해?
A. 아니다. 너무 자주 발생하면 방해가 될 수 있으므로 필요한 경우만 사용한다.

---

## 2.2 aria-busy / role status Rules

### [개념]

`aria-busy`는 특정 영역이 업데이트 중임을 나타내고, `role="status"`는 사용자에게 상태 변화를 부드럽게 전달하는 데 사용한다.

Loading UX에서는 두 속성을 상황에 맞게 사용해야 한다.

---

### [핵심]

사용 대상:

- Content Region Loading
- Data Table Loading
- List Loading
- Form Submit Loading
- Page Section Refresh
- Background Update Indicator

핵심 규칙:

- `aria-busy`는 업데이트 중인 영역에 적용한다.
- `role="status"`는 상태 메시지를 전달할 때 사용한다.
- `role="status"`는 보통 `aria-live="polite"` 성격을 가진다.
- 모든 작은 Loading에 무조건 적용하지 않는다.
- 반복 갱신되는 영역에는 과도한 announcement를 피한다.
- Loading 종료 후 상태가 갱신되어야 한다.

---

### [실무]

콘텐츠 영역 예:

```tsx
<section aria-busy={isLoading}>
  {isLoading ? (
    <p role="status">목록을 불러오는 중입니다.</p>
  ) : (
    <FestivalList festivals={festivals} />
  )}
</section>
```

Refetch 영역 예:

```tsx
<section aria-busy={isFetching}>
  {isFetching && <p role="status">최신 정보를 확인 중입니다.</p>}
  <FestivalList festivals={festivals} />
</section>
```

Form Submit 예:

```tsx
<form aria-busy={mutation.isPending}>
  <button type="submit" disabled={mutation.isPending}>
    {mutation.isPending ? "제출 중..." : "제출"}
  </button>
</form>
```

권장:

- 페이지 전체보다 실제 업데이트되는 영역에 적용한다.
- Loading Message는 짧고 구체적으로 작성한다.
- 버튼 처리 중에는 버튼 문구 변경이 가장 직접적이다.
- 자주 바뀌는 백그라운드 refetch에는 신중히 적용한다.

주의:

- `aria-busy=true`가 계속 유지되면 보조 기술 사용자가 상태를 오해할 수 있다.
- 불필요한 status message 반복은 방해가 된다.
- Loading 종료 후 화면 상태가 실제로 바뀌는지 확인한다.
- aria 속성만 넣고 시각적 Loading을 생략하지 않는다.

---

### [FAQ]

Q. aria-busy는 언제 써?
A. 특정 콘텐츠 영역이 데이터를 불러오거나 업데이트 중일 때 사용할 수 있다.

Q. role status는 언제 써?
A. 사용자에게 Loading이나 Success 같은 상태 변화를 부드럽게 알릴 때 사용한다.

Q. 모든 Loading에 aria-busy를 넣어야 해?
A. 아니다. 실제 업데이트 중인 영역에 필요한 경우만 적용하는 것이 좋다.

Q. role status와 role alert는 달라?
A. 다르다. status는 일반 상태 안내이고 alert는 중요한 오류나 즉시 알려야 하는 메시지에 적합하다.

---

# 3. Error Accessibility Rules

## 3.1 Error Message Accessibility

### [개념]

Error Message Accessibility는 사용자가 오류 메시지를 시각적으로뿐 아니라 보조 기술로도 인지하고 다음 행동을 할 수 있게 하는 기준이다.

Error Message는 텍스트, 위치, 역할, focus 흐름, 조작 가능한 Retry Action을 포함해야 한다.

---

### [핵심]

Error 접근성 대상:

- Page Error
- Inline Error
- Form Alert
- Field Error
- Toast Error
- Error Boundary Fallback
- NotFoundPage
- ForbiddenPage
- Retry Button

핵심 규칙:

- 오류 메시지는 텍스트로 제공한다.
- 중요한 오류는 `role="alert"`를 고려한다.
- Field Error는 input과 연결한다.
- Retry Button은 실제 button 요소로 구현한다.
- 색상만으로 오류를 표시하지 않는다.
- 오류 발생 위치와 메시지 위치를 가깝게 둔다.
- ErrorState는 다음 행동을 제공한다.
- 서버 내부 메시지를 그대로 읽히게 하지 않는다.

---

### [실무]

Page Error 예:

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

Field Error 예:

```tsx
<input
  id="email"
  name="email"
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

Forbidden Page 예:

```tsx
<main>
  <h1>접근 권한이 없습니다.</h1>
  <p>현재 계정으로는 이 페이지를 이용할 수 없습니다.</p>
  <Link to="/">메인으로 이동</Link>
</main>
```

권장:

- 오류 메시지는 문제와 다음 행동을 포함한다.
- Retry Button은 명확한 label을 가진다.
- Form 오류는 input과 직접 연결한다.
- 페이지 단위 오류는 heading을 포함한다.
- Error Boundary Fallback에는 안전한 메시지만 제공한다.

주의:

- 오류를 빨간색만으로 표시하지 않는다.
- 클릭 가능한 div를 Retry Button처럼 사용하지 않는다.
- stack trace, SQL Error, token 값이 screen reader에 읽히지 않게 한다.
- role alert를 너무 많은 요소에 중복 사용하지 않는다.

---

### [FAQ]

Q. Error Message에는 role alert가 필요해?
A. 중요한 오류 메시지에는 고려할 수 있지만, 모든 오류에 남발하지 않는 것이 좋다.

Q. Retry Button은 div로 만들어도 돼?
A. 권장하지 않는다. 실제 button 요소를 사용해야 키보드와 보조 기술 접근성이 좋다.

Q. Field Error는 왜 input과 연결해야 해?
A. 보조 기술 사용자가 어떤 입력값에 오류가 있는지 이해하고 수정할 수 있게 하기 위해서다.

Q. Error Message를 색상만으로 표시해도 돼?
A. 아니다. 텍스트, 아이콘, ARIA 속성 등 색상 외 정보가 필요하다.

---

## 3.2 Focus Management for Error

### [개념]

Focus Management는 오류 발생 후 사용자의 키보드 focus 흐름을 적절히 유지하거나 필요한 위치로 이동시키는 기준이다.

오류가 발생했다고 무조건 focus를 이동하면 사용자의 현재 작업을 방해할 수 있으므로 상황별 판단이 필요하다.

---

### [핵심]

Focus 이동 고려 상황:

- Form Submit Failed
- Long Form Field Error
- Page Error
- Modal Error
- Route Change Error
- Error Boundary Fallback
- Payment Failure
- Login Redirect

핵심 규칙:

- Form 제출 실패 시 첫 오류 field 또는 Error Summary로 focus 이동을 고려한다.
- 페이지 전환 후에는 heading focus를 고려할 수 있다.
- 오류 Toast만으로 focus를 이동하지 않는다.
- 입력 중인 사용자의 focus를 불필요하게 빼앗지 않는다.
- Modal Error는 modal 내부 focus trap을 유지한다.
- Error Boundary Fallback은 fallback heading 또는 action 접근성을 확인한다.

---

### [실무]

첫 오류 field focus 예:

```typescript
function focusFirstError(errors: Record<string, string>) {
  const firstField = Object.keys(errors)[0];

  if (!firstField) {
    return;
  }

  document.querySelector<HTMLElement>(`[name="${firstField}"]`)?.focus();
}
```

Error Summary focus 예:

```tsx
function ErrorSummary({ errors }) {
  const summaryRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (Object.keys(errors).length > 0) {
      summaryRef.current?.focus();
    }
  }, [errors]);

  return (
    <section
      ref={summaryRef}
      tabIndex={-1}
      role="alert"
      aria-labelledby="error-summary-title"
    >
      <h2 id="error-summary-title">입력 내용을 확인해 주세요.</h2>
    </section>
  );
}
```

Fallback heading 예:

```tsx
<main>
  <h1 tabIndex={-1}>문제가 발생했습니다.</h1>
  <p>화면을 표시하는 중 오류가 발생했습니다.</p>
</main>
```

권장:

- 긴 Form은 Error Summary로 focus 이동을 고려한다.
- 짧은 Form은 첫 오류 field focus가 유용할 수 있다.
- 페이지 단위 전환은 heading 기준 focus를 검토한다.
- 자동 focus 이동은 사용자의 입력 흐름을 방해하지 않게 한다.

주의:

- 입력 중 오류가 생길 때마다 focus를 강제로 이동하지 않는다.
- Toast 발생 시 focus를 Toast로 강제 이동하지 않는다.
- focus 대상에 `tabIndex={-1}`이 필요할 수 있다.
- focus 이동은 시각적 이동과 스크린 리더 안내를 함께 고려한다.

---

### [FAQ]

Q. 오류가 발생하면 무조건 focus를 이동해야 해?
A. 아니다. Form 제출 실패나 페이지 전환처럼 사용자가 위치를 잃기 쉬운 경우에만 신중히 적용한다.

Q. 긴 Form에서 오류가 많으면 어디로 focus를 보내?
A. Error Summary로 focus를 이동하고 각 오류에서 해당 field로 이동할 수 있게 하는 방식이 유용하다.

Q. Toast Error에 focus를 이동해야 해?
A. 보통 하지 않는다. Toast는 일시적 알림이며 focus 이동은 사용자 작업을 방해할 수 있다.

Q. 첫 오류 field로 focus 이동은 언제 좋아?
A. 짧은 Form이나 제출 실패 후 사용자가 바로 수정해야 하는 경우에 유용하다.

---

# 4. Empty / Success Accessibility Rules

## 4.1 Empty State Accessibility

### [개념]

Empty State Accessibility는 데이터가 없는 상태와 다음 행동을 모든 사용자가 이해할 수 있게 하는 기준이다.

Empty State는 일러스트나 아이콘에 의존하지 않고 텍스트와 의미 있는 구조를 제공해야 한다.

---

### [핵심]

Empty 접근성 대상:

- Search Empty
- First Use Empty
- Filter Empty
- Favorite Empty
- Review Empty
- Notification Empty
- Chat Empty
- Table Empty
- Dashboard Empty

핵심 규칙:

- Empty State 제목을 heading으로 제공한다.
- 설명 문구를 텍스트로 제공한다.
- CTA는 button 또는 link 역할에 맞게 사용한다.
- 장식용 icon은 `aria-hidden` 처리한다.
- 색상이나 그림만으로 의미를 전달하지 않는다.
- Empty State는 Error처럼 `role="alert"`를 남발하지 않는다.
- CTA는 키보드로 접근 가능해야 한다.

---

### [실무]

EmptyState 예:

```tsx
function EmptyState({ title, description, action }: EmptyStateProps) {
  return (
    <section aria-labelledby="empty-state-title">
      <h2 id="empty-state-title">{title}</h2>
      {description && <p>{description}</p>}
      {action}
    </section>
  );
}
```

Search Empty CTA 예:

```tsx
<EmptyState
  title="검색 결과가 없습니다."
  description="검색어를 바꾸거나 필터를 초기화해 보세요."
  action={
    <button type="button" onClick={resetFilters}>
      필터 초기화
    </button>
  }
/>
```

First Use CTA 예:

```tsx
<EmptyState
  title="아직 찜한 축제가 없습니다."
  description="마음에 드는 축제를 찾아 찜해 보세요."
  action={<Link to="/festivals">축제 둘러보기</Link>}
/>
```

권장:

- Empty State는 명확한 heading과 description을 가진다.
- 화면 내 상태 변경 action은 button을 사용한다.
- 페이지 이동 action은 link를 사용한다.
- 일러스트는 보조 요소로만 사용한다.
- Empty CTA label은 구체적으로 작성한다.

주의:

- Empty State를 단순 icon 하나로 표시하지 않는다.
- “여기 클릭” 같은 모호한 link text를 피한다.
- Empty State를 Error State처럼 alert 처리하지 않는다.
- 권한 없는 CTA를 제공하지 않는다.

---

### [FAQ]

Q. Empty State에도 접근성이 필요해?
A. 필요하다. 데이터가 없는 상태와 다음 행동을 모든 사용자가 이해할 수 있어야 한다.

Q. Empty State CTA는 button이 좋아 link가 좋아?
A. 화면 내 동작이면 button, 다른 페이지 이동이면 link가 적합하다.

Q. Empty State icon은 스크린 리더가 읽어야 해?
A. 대부분 장식 요소라면 `aria-hidden` 처리하는 것이 좋다.

Q. Empty State에 role alert를 써도 돼?
A. 보통은 필요하지 않다. Error State와 달리 긴급 오류가 아니기 때문이다.

---

## 4.2 Success Feedback Accessibility

### [개념]

Success Feedback Accessibility는 사용자가 요청 성공 상태를 보조 기술로도 인지할 수 있게 하는 기준이다.

Success Feedback은 Toast, Inline Message, Button State Change, Redirect Complete Page에서 각각 접근성 기준을 가져야 한다.

---

### [핵심]

Success 접근성 대상:

- Toast Success
- Inline Success Message
- Button Success State
- Form Save Success
- Payment Complete Page
- Signup Complete Page
- Upload Success
- Copy Success
- Optimistic UI Success

핵심 규칙:

- 성공 메시지는 텍스트로 제공한다.
- Inline Success에는 `role="status"`를 고려한다.
- Toast는 스크린 리더 인식과 표시 시간을 고려한다.
- 색상만으로 성공을 표현하지 않는다.
- 버튼 상태 변화에는 label 변화가 필요할 수 있다.
- 중요한 성공 결과는 화면에 남는 방식으로 제공한다.
- 페이지 이동 후 heading을 명확히 제공한다.

---

### [실무]

Inline Success 예:

```tsx
{
  successMessage && (
    <p role="status" aria-live="polite">
      {successMessage}
    </p>
  );
}
```

Button State 예:

```tsx
<button type="button" aria-pressed={liked} onClick={toggleLike}>
  {liked ? "좋아요 취소" : "좋아요"}
</button>
```

Complete Page 예:

```tsx
<main>
  <h1>결제가 완료되었습니다.</h1>
  <p>후원 내역에서 상세 정보를 확인할 수 있습니다.</p>
  <Link to="/donations">후원 내역 보기</Link>
</main>
```

권장:

- Toast Success는 너무 빨리 사라지지 않게 한다.
- 중요한 성공은 완료 페이지 또는 Inline Message로 제공한다.
- 버튼 상태 변화는 텍스트, `aria-pressed`, icon label을 함께 고려한다.
- 자동 저장 성공은 과도한 live announcement를 피한다.

주의:

- 초록색만으로 성공을 표시하지 않는다.
- Toast만으로 중요한 완료 정보를 전달하지 않는다.
- 좋아요 상태가 icon만 바뀌면 스크린 리더가 알기 어렵다.
- 자동 반복 성공 메시지는 보조 기술 사용자에게 방해가 될 수 있다.

---

### [FAQ]

Q. Success Message에도 접근성이 필요해?
A. 필요하다. 보조 기술 사용자도 요청이 성공했음을 인지할 수 있어야 한다.

Q. Inline Success에는 어떤 role이 좋아?
A. 일반적인 성공 알림에는 `role="status"`와 `aria-live="polite"`를 고려할 수 있다.

Q. 좋아요 버튼 상태는 어떻게 전달해?
A. 버튼 문구를 바꾸거나 `aria-pressed`를 사용해 눌림 상태를 전달할 수 있다.

Q. 결제 완료는 Toast로 충분해?
A. 보통은 완료 페이지처럼 화면에 남는 접근 가능한 확인 UX가 더 적합하다.

---

# 5. Security Overview

## 5.1 Error Message Security Purpose

### [개념]

Error Message Security는 오류 메시지, 로그, Toast, Fallback UI를 통해 민감한 내부 정보가 사용자에게 노출되지 않도록 하는 기준이다.

Frontend Error UX는 사용자가 이해할 수 있는 안전한 메시지를 제공하고, 개발자 디버깅 정보는 별도 로그로 분리해야 한다.

---

### [핵심]

보안상 노출 금지 대상:

- Stack Trace
- SQL Error
- Server Path
- File System Path
- Access Token
- Refresh Token
- Password
- Personal Data
- API Secret
- Internal Role Policy
- Database Schema
- Infrastructure Detail
- External API Key
- Debug Object

핵심 규칙:

- 사용자 메시지와 개발자 로그를 분리한다.
- 서버 원문 message를 무조건 사용자에게 노출하지 않는다.
- 운영 환경에서 stack trace를 표시하지 않는다.
- token, password, personal data를 UI나 console에 남기지 않는다.
- 403에서 내부 role 정책을 과도하게 노출하지 않는다.
- 500 Error는 generic message를 사용한다.
- Validation Error는 사용자 수정에 필요한 수준만 제공한다.

---

### [실무]

나쁜 메시지 예:

```text
SQLSyntaxErrorException: Unknown column users.password_hash
```

좋은 메시지 예:

```text
서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.
```

나쁜 403 메시지 예:

```text
ROLE_ADMIN 권한이 필요하며 SecurityConfig /admin/** 정책에 의해 차단되었습니다.
```

좋은 403 메시지 예:

```text
현재 계정으로는 이 기능을 이용할 수 없습니다.
```

개발 로그 예:

```text
status=500
endpoint=/api/festivals
errorCode=INTERNAL_SERVER_ERROR
timestamp=2026-07-05T10:00:00
```

권장:

- 사용자 UI에는 안전한 메시지만 표시한다.
- 개발 로그에는 원인 분석에 필요한 최소 정보만 남긴다.
- 민감정보는 로그에서도 마스킹한다.
- 운영 환경과 개발 환경의 오류 표시 수준을 분리한다.
- 공통 Error Message Mapping을 사용한다.

주의:

- `error.response.data.message`를 그대로 Toast로 띄우지 않는다.
- console.log로 token이나 사용자 정보를 출력하지 않는다.
- Error Boundary Fallback에 stack trace를 표시하지 않는다.
- 권한 오류에서 내부 role 이름과 정책을 자세히 노출하지 않는다.

---

### [FAQ]

Q. 서버 에러 원문을 그대로 보여주면 안 되는 이유는?
A. 내부 구조, SQL, 서버 경로, 보안 정보가 노출될 수 있기 때문이다.

Q. 개발자 로그와 사용자 메시지는 왜 나눠?
A. 사용자는 이해 가능한 해결 안내가 필요하고 개발자는 원인 분석 정보가 필요하기 때문이다.

Q. Stack Trace를 사용자에게 보여줘도 돼?
A. 운영 환경에서는 보여주지 않는 것이 좋다.

Q. 403에서 필요한 role 정보를 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 권한 정책을 과도하게 노출하지 않는 메시지가 좋다.

---

# 6. User Message vs Developer Log Rules

## 6.1 Message Separation Rules

### [개념]

User Message와 Developer Log 분리는 사용자에게 보여줄 안내 문구와 개발자가 원인 분석에 사용할 정보를 분리하는 기준이다.

두 정보를 분리하지 않으면 사용자에게 불필요하거나 위험한 내부 정보가 노출될 수 있다.

---

### [핵심]

User Message 포함 정보:

- 현재 상태
- 사용자가 할 수 있는 행동
- 안전한 오류 안내
- 재시도 여부
- 로그인 필요 안내
- 권한 없음 안내
- 입력 수정 안내

Developer Log 포함 정보:

- HTTP Status
- Endpoint
- Error Code
- Request ID
- Timestamp
- Safe Context
- Stack Trace development only
- Debug Data masked

핵심 규칙:

- User Message는 짧고 안전하게 작성한다.
- Developer Log는 원인 분석에 필요한 최소 정보만 남긴다.
- 민감정보는 로그에서도 마스킹한다.
- 운영 UI에 debug object를 출력하지 않는다.
- 개발 환경 console과 운영 환경 monitoring을 구분한다.
- Error Code는 사용자에게 필요한 경우만 제한적으로 표시한다.

---

### [실무]

분리 예:

```typescript
function handleApiError(error: unknown) {
  const userMessage = getApiErrorMessage(error);

  logErrorForDeveloper(error, {
    feature: "FestivalList",
    action: "fetchFestivals",
  });

  return userMessage;
}
```

사용자 메시지 예:

```text
축제 목록을 불러오지 못했습니다. 다시 시도해 주세요.
```

개발 로그 예:

```json
{
  "feature": "FestivalList",
  "action": "fetchFestivals",
  "status": 500,
  "endpoint": "/api/festivals",
  "requestId": "req-123"
}
```

권장:

- 공통 error handler에서 사용자 메시지와 개발 로그를 동시에 분리한다.
- 개발 로그에는 feature, action, status를 포함할 수 있다.
- 사용자 메시지는 화면 문맥에 맞게 override 가능하게 둔다.
- Error Code를 고객센터 문의용으로 제공할 수 있다.

주의:

- Developer Log를 그대로 UI에 렌더링하지 않는다.
- 사용자 메시지에 endpoint, DTO, table name을 넣지 않는다.
- console.log가 운영 번들에서 노출될 수 있는지 확인한다.
- token, password, 주민번호, 이메일 등 개인정보는 로그에서도 주의한다.

---

### [FAQ]

Q. User Message와 Developer Log는 어떻게 달라?
A. User Message는 사용자 안내용이고 Developer Log는 개발자 원인 분석용이다.

Q. Developer Log를 화면에 보여줘도 돼?
A. 운영 환경에서는 보여주지 않는 것이 좋다.

Q. 사용자 메시지에 status code를 넣어도 돼?
A. 필요한 경우 제한적으로 가능하지만 대부분은 이해 가능한 문장으로 바꾸는 것이 좋다.

Q. 로그에도 민감정보를 남기면 안 돼?
A. 그렇다. 로그도 유출될 수 있으므로 token, password, 개인정보는 마스킹하거나 기록하지 않는다.

---

# 7. Troubleshooting Overview

## 7.1 Troubleshooting Purpose

### [개념]

Troubleshooting은 Loading, Error, Empty, Success UX에서 발생하는 문제를 원인별로 추적하고 수정하는 기준이다.

Frontend Agent와 Review Agent는 증상만 보고 수정하지 않고, 상태값, 요청 흐름, 렌더링 조건, 접근성, 보안 노출 여부를 함께 확인해야 한다.

---

### [핵심]

Troubleshooting 주요 증상:

- Infinite Loading
- Blank Screen
- Error Message Not Showing
- Empty Flicker
- Duplicate Request
- Refetch Flicker
- Submit Button Stuck
- Retry Not Working
- Toast Not Showing
- Form Error Not Showing
- Route Flicker
- Error Boundary Not Catching
- Stale UI
- Query Not Refetching
- Unauthorized Redirect Loop
- Forbidden Flicker

핵심 규칙:

- 증상을 Loading / Error / Empty / Success / Route / Boundary로 분류한다.
- Network 탭과 Console을 함께 확인한다.
- 상태값과 조건부 렌더링 순서를 확인한다.
- Query Key와 Mutation 상태를 확인한다.
- Error Mapping과 UI 연결을 확인한다.
- 접근성 / 보안 문제도 함께 검수한다.
- 원인을 모르면 빈 화면이나 catch 무시로 숨기지 않는다.

---

### [실무]

공통 Debug Flow:

```text
문제 발생
→ 증상 분류
→ Network 확인
→ Console 확인
→ State 확인
→ Conditional Rendering 확인
→ Query / Mutation 상태 확인
→ Error Mapping 확인
→ Accessibility / Security 확인
→ 수정
```

증상별 1차 확인:

| 증상              | 우선 확인                                  |
| ----------------- | ------------------------------------------ |
| Infinite Loading  | finally, query enabled, pending request    |
| Blank Screen      | Console Error, return null, Error Boundary |
| Error 안 보임     | catch, setError, isError, Promise.reject   |
| Empty Flicker     | loading보다 empty 먼저 검사                |
| Duplicate Request | StrictMode, queryKey, useEffect            |
| Submit Stuck      | mutationFn Promise, isPending              |
| Stale UI          | invalidate queryKey                        |
| Route Flicker     | auth initialized                           |
| Boundary 미작동   | async error인지 확인                       |

---

### [FAQ]

Q. Troubleshooting에서 가장 먼저 확인할 것은?
A. 증상을 분류하고 Network, Console, 상태값, 조건부 렌더링 순서를 확인하는 것이다.

Q. Error Handling 문제는 어디서 많이 생겨?
A. catch 누락, Error State 미연결, interceptor Promise.reject 누락, 서버 message mapping 실패에서 자주 생긴다.

Q. Loading 문제는 어디서 많이 생겨?
A. finally 누락, query enabled 조건 오류, pending request, useEffect dependency loop에서 자주 생긴다.

Q. 빈 화면 문제는 어디서 많이 생겨?
A. Runtime render error, data undefined 접근, Route mismatch, Loading/Error/Empty 처리 누락에서 자주 생긴다.

---

# 8. Loading Troubleshooting Rules

## 8.1 Infinite Loading Troubleshooting

### [개념]

Infinite Loading은 Loading UI가 끝나지 않고 계속 표시되는 문제다.

Infinite Loading은 요청 완료 처리 누락, Error State 전환 누락, `enabled` 조건 오류, 인증 초기화 오류, Promise 미해결에서 자주 발생한다.

---

### [핵심]

주요 원인:

- `finally`에서 loading false 누락
- API Promise가 resolve / reject 되지 않음
- catch에서 error 처리 누락
- Error State 전환 누락
- `enabled`가 계속 false
- auth initialized가 true로 바뀌지 않음
- useEffect dependency loop
- interceptor에서 응답을 반환하지 않음
- Suspense fallback 종료 조건 없음
- mutation pending stuck

핵심 규칙:

- 성공과 실패 모두 Loading을 종료한다.
- 실패 시 Error State로 전환한다.
- `finally`를 사용해 수동 loading을 해제한다.
- TanStack Query 상태를 사용하면 별도 loading state를 줄인다.
- `enabled` false 상태와 Loading 상태를 구분한다.
- auth initialized는 성공 / 실패와 관계없이 종료되어야 한다.

---

### [실무]

Debug Flow:

```text
Loading 계속 표시
→ Network 요청 완료 여부 확인
→ Promise resolve / reject 확인
→ catch / finally 실행 확인
→ loading false 확인
→ Error State 렌더링 확인
→ enabled 조건 확인
→ auth initialized 확인
→ dependency loop 확인
```

수동 loading 나쁜 예:

```typescript
async function loadData() {
  setLoading(true);
  await getData();
  setLoading(false);
}
```

개선 예:

```typescript
async function loadData() {
  setLoading(true);

  try {
    await getData();
  } catch (error) {
    setError(getApiErrorMessage(error));
  } finally {
    setLoading(false);
  }
}
```

Query enabled 확인:

```tsx
const query = useQuery({
  queryKey: ["profile", userId],
  queryFn: () => getProfile(userId),
  enabled: Boolean(userId),
});
```

권장:

- Loading UI에는 실패 경로가 반드시 있어야 한다.
- enabled false일 때는 Guide State 또는 Auth Loading을 별도로 처리한다.
- auth 초기화 로직은 실패해도 initialized를 true로 바꾼다.
- mutationFn이 Promise를 반환하는지 확인한다.

주의:

- `enabled: false`를 Loading으로 계속 보여주면 무한 Loading처럼 보인다.
- API 실패를 catch에서 삼키면 Query나 Mutation이 성공처럼 끝날 수 있다.
- interceptor에서 response 또는 Promise.reject를 반환하지 않으면 흐름이 끊긴다.
- Suspense fallback만 있고 Error Boundary가 없으면 복구가 어렵다.

---

### [FAQ]

Q. Loading이 계속 끝나지 않아?
A. finally에서 loading false를 호출하는지, API 요청이 완료되는지, Error State로 전환되는지 확인해야 한다.

Q. API 실패 후에도 Loading이 계속돼?
A. catch 또는 finally에서 상태를 종료하지 않았거나 Error State 전환이 누락되었을 수 있다.

Q. enabled false인데 Loading이 계속 보여?
A. 요청이 시작되지 않은 상태일 수 있으므로 Idle 또는 Guide State를 별도로 설계해야 한다.

Q. auth loading이 계속되면?
A. 인증 초기화 로직에서 성공 / 실패와 관계없이 initialized를 true로 바꾸는지 확인해야 한다.

---

## 8.2 Submit Button Stuck Troubleshooting

### [개념]

Submit Button Stuck은 Form 제출이나 Mutation 이후 버튼이 계속 disabled 또는 “처리 중” 상태로 남는 문제다.

이 문제는 mutationFn Promise 미반환, error 삼킴, 별도 loading state 해제 누락, 요청 미완료에서 자주 발생한다.

---

### [핵심]

주요 원인:

- mutationFn Promise 미반환
- catch에서 error를 삼킴
- `isSubmitting` state 해제 누락
- API 요청 pending
- timeout 설정 없음
- onError / onSettled 미실행
- form submit handler 중복 blocking
- disabled 조건이 잘못됨
- 컴포넌트 unmount 후 state 꼬임

핵심 규칙:

- mutationFn은 Promise를 반환해야 한다.
- error를 catch하면 다시 throw하거나 Error State로 연결한다.
- 별도 loading state는 finally에서 해제한다.
- disabled 조건을 mutation 상태와 일치시킨다.
- 실패 후 사용자가 다시 제출할 수 있어야 한다.
- timeout 또는 오류 fallback을 고려한다.

---

### [실무]

나쁜 mutationFn:

```tsx
const mutation = useMutation({
  mutationFn: (values) => {
    api.post("/reviews", values);
  },
});
```

개선:

```tsx
const mutation = useMutation({
  mutationFn: (values) => {
    return api.post("/reviews", values);
  },
});
```

catch에서 error 삼키는 예:

```typescript
async function saveProfile(values) {
  try {
    return await api.put("/profile", values);
  } catch (error) {
    console.log(error);
  }
}
```

개선:

```typescript
async function saveProfile(values) {
  try {
    return await api.put("/profile", values);
  } catch (error) {
    console.error(error);
    throw error;
  }
}
```

별도 state 예:

```typescript
async function handleSubmit(values) {
  setSubmitting(true);

  try {
    await saveProfile(values);
  } catch (error) {
    setFormError(getApiErrorMessage(error));
  } finally {
    setSubmitting(false);
  }
}
```

권장:

- 가능하면 `mutation.isPending`을 사용한다.
- 별도 submitting state는 필요한 경우에만 사용한다.
- 실패 후 버튼이 다시 활성화되는지 테스트한다.
- 요청 timeout과 네트워크 실패 케이스를 확인한다.
- onSettled에서 공통 cleanup을 처리할 수 있다.

주의:

- disabled 조건이 `isValid === false || isPending`인지, `isValid === false && isPending`인지 확인한다.
- catch에서 error를 삼키면 onError가 실행되지 않을 수 있다.
- 버튼 문구만 바뀌고 실제 disabled가 안 되면 중복 제출이 가능하다.
- disabled만 되고 메시지가 없으면 사용자가 이유를 모른다.

---

### [FAQ]

Q. Submit Button이 계속 처리 중이야?
A. mutationFn이 Promise를 반환하는지, 요청이 완료되는지, error를 삼키지 않는지, loading state를 해제하는지 확인해야 한다.

Q. mutationFn에서 api.post를 return해야 해?
A. 그렇다. Promise를 반환해야 pending, success, error 상태를 정확히 추적할 수 있다.

Q. catch에서 console.log만 하면 안 돼?
A. error를 다시 throw하지 않으면 onError가 실행되지 않거나 실패 상태가 사라질 수 있다.

Q. 버튼 Loading은 별도 state로 관리해야 해?
A. 보통은 mutation.isPending을 사용하는 것이 더 안전하다.

---

# 9. Error Troubleshooting Rules

## 9.1 Error Message Not Showing

### [개념]

Error Message Not Showing은 요청이나 렌더링에서 오류가 발생했지만 사용자에게 오류 메시지가 표시되지 않는 문제다.

이 문제는 catch 처리 누락, Error State 조건 오류, interceptor 반환 누락, error object shape 착각에서 자주 발생한다.

---

### [핵심]

주요 원인:

- catch에서 error를 삼킴
- setError 누락
- Error UI 렌더링 조건 오류
- `isError` 미사용
- error object shape 착각
- AxiosError Mapping 실패
- interceptor에서 Promise.reject 누락
- Toast Provider 미설정
- Field Error key 불일치
- role이나 CSS로 숨겨짐

핵심 규칙:

- catch 또는 onError에서 오류 상태를 설정한다.
- Error UI 조건부 렌더링을 확인한다.
- `error.response?.data` 구조를 확인한다.
- interceptor는 처리 후 Promise.reject를 반환한다.
- fallback message를 제공한다.
- Toast 사용 시 provider와 렌더링 위치를 확인한다.

---

### [실무]

Debug Flow:

```text
Error 발생
→ catch / onError 진입 확인
→ error 객체 구조 확인
→ message mapping 확인
→ setError / setFormError 확인
→ Error UI 렌더링 조건 확인
→ interceptor Promise.reject 확인
→ CSS display 여부 확인
```

나쁜 interceptor:

```typescript
api.interceptors.response.use(
  (response) => response,
  (error) => {
    toast.error("요청 실패");
  },
);
```

개선:

```typescript
api.interceptors.response.use(
  (response) => response,
  (error) => {
    toast.error("요청 실패");
    return Promise.reject(error);
  },
);
```

ErrorState 연결 예:

```tsx
if (isError) {
  return <ErrorState message={getApiErrorMessage(error)} onRetry={refetch} />;
}
```

권장:

- error mapping 함수는 unknown error fallback을 가진다.
- interceptor와 화면별 error handling 역할을 분리한다.
- Form Error와 Page Error 위치를 구분한다.
- 테스트에서 400 / 401 / 403 / 500 케이스를 확인한다.

주의:

- catch에서 console.log만 하고 끝내지 않는다.
- error 객체 구조를 추측하지 말고 Network Response를 확인한다.
- Toast만 띄우고 화면 ErrorState를 누락하지 않는다.
- 서버 원문 message를 그대로 출력하지 않는다.

---

### [FAQ]

Q. API는 실패했는데 에러 메시지가 안 보여?
A. catch에서 에러를 상태로 저장하는지, Error UI 조건이 맞는지, error mapping 함수가 올바른지 확인해야 한다.

Q. interceptor에서 Toast는 뜨는데 화면 ErrorState가 안 떠?
A. Promise.reject를 반환하지 않아 호출부가 error를 받지 못할 수 있다.

Q. Form Field Error가 안 보여?
A. 서버 errors key와 Frontend input name이 일치하는지 확인해야 한다.

Q. Error Message가 DOM에는 있는데 안 보여?
A. CSS display, visibility, z-index, conditional rendering 조건을 확인해야 한다.

---

## 9.2 Retry Not Working Troubleshooting

### [개념]

Retry Not Working은 다시 시도 버튼을 눌러도 요청이 재실행되지 않거나 같은 오류 상태가 유지되는 문제다.

Retry UX는 버튼과 실제 재요청 함수가 연결되어야 하며, 요청 조건과 queryKey도 올바르게 유지되어야 한다.

---

### [핵심]

주요 원인:

- Retry Button onClick 미연결
- refetch 함수 미전달
- enabled 조건 false
- queryKey 오류
- retry 중 button disabled 고정
- error state 초기화 누락
- request params 누락
- auth token 만료
- 401 / 403처럼 retry 부적합 오류
- 네트워크 원인 지속

핵심 규칙:

- Retry Button은 실제 refetch 또는 재요청 함수와 연결한다.
- Retry 중 Loading 또는 disabled 상태를 표시한다.
- Retry 가능한 오류인지 판단한다.
- enabled 조건이 true인지 확인한다.
- 요청 parameter가 유지되는지 확인한다.
- Retry 실패 후 Error State를 유지한다.

---

### [실무]

Retry 연결 예:

```tsx
<ErrorState
  message="축제 목록을 불러오지 못했습니다."
  onRetry={() => refetch()}
/>
```

Retry Button 예:

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

Debug Flow:

```text
Retry 클릭
→ onClick 실행 확인
→ refetch 호출 확인
→ enabled 조건 확인
→ Network 요청 발생 확인
→ queryKey / params 확인
→ Error State 갱신 확인
```

권장:

- Retry Button은 ErrorState props로 명확히 전달한다.
- Retry 중 버튼을 disabled 처리할 수 있다.
- 인증 오류는 로그인 이동과 연결한다.
- 권한 오류는 Retry보다 Forbidden UX가 적합하다.
- 404 Resource Not Found는 목록 이동이 더 적합할 수 있다.

주의:

- Retry Button만 있고 onRetry가 비어 있으면 UX가 깨진다.
- enabled false면 refetch 동작이 기대와 다를 수 있다.
- 같은 네트워크 오류가 지속되면 Retry해도 실패한다.
- Retry가 모든 오류의 해결책은 아니다.

---

### [FAQ]

Q. 다시 시도 버튼이 눌리는데 요청이 안 나가?
A. onRetry 연결, refetch 호출, enabled 조건, Network 요청 발생 여부를 확인해야 한다.

Q. Retry Button은 모든 ErrorState에 넣어야 해?
A. 아니다. 네트워크나 일시적 서버 오류에는 적합하지만 401, 403, 404에는 다른 액션이 더 적합할 수 있다.

Q. retry 중 버튼을 disabled 해야 해?
A. 중복 재시도를 막기 위해 disabled 처리할 수 있다.

Q. retry해도 계속 실패하면?
A. ErrorState를 유지하고 네트워크, 서버 상태, 인증 상태, 요청 파라미터를 확인해야 한다.

---

# 10. Empty / Success Troubleshooting Rules

## 10.1 Empty Flicker Troubleshooting

### [개념]

Empty Flicker는 요청 완료 전에 Empty State가 잠깐 표시된 뒤 실제 데이터가 표시되는 문제다.

이 문제는 Loading보다 Empty를 먼저 검사하거나 초기 data를 빈 배열로 두고 요청 완료 여부를 구분하지 않을 때 발생한다.

---

### [핵심]

주요 원인:

- Empty 판정을 Loading보다 먼저 실행
- 초기 data 빈 배열
- 요청 완료 여부 구분 없음
- `isSuccess` 확인 없이 data length만 검사
- auth initialized 전 Empty 표시
- filter change 중 Empty 표시
- placeholderData / previous data 기준 없음
- page index 미초기화

핵심 규칙:

- Loading을 Empty보다 먼저 검사한다.
- Error를 Empty보다 먼저 검사한다.
- 요청 성공 후 Empty를 검사한다.
- `isSuccess && data.length === 0`처럼 성공 상태를 포함한다.
- 필터 변경 중에는 Loading 또는 Refetch Indicator를 표시한다.
- auth 초기화 전에는 Empty를 표시하지 않는다.

---

### [실무]

나쁜 예:

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

if (error) {
  return <ErrorState message="데이터를 불러오지 못했습니다." />;
}

if (items.length === 0) {
  return <EmptyState title="결과가 없습니다." />;
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

if (isSuccess && data.length === 0) {
  return <EmptyState title="결과가 없습니다." />;
}
```

권장:

- 조건부 렌더링 순서를 문서화한다.
- Empty State는 요청 성공 이후에만 표시한다.
- filter 변경 중 이전 데이터를 유지할지 Skeleton을 보여줄지 정한다.
- page index 또는 cursor 초기화 여부를 확인한다.

주의:

- `data?.length === 0`만으로 Empty를 판단하면 Flicker가 생길 수 있다.
- 초기값 `[]`는 실제 빈 결과와 구분해야 한다.
- API 실패를 빈 배열로 변환하면 Error State가 사라진다.
- Search Empty와 입력 전 Guide State를 구분한다.

---

### [FAQ]

Q. Empty State가 잠깐 보였다가 목록이 보여?
A. 요청 완료 전 빈 배열을 Empty로 판정했을 가능성이 있다.

Q. Empty Flicker를 막으려면?
A. Loading과 Error를 먼저 검사하고 요청 성공 후에만 Empty를 표시해야 한다.

Q. TanStack Query에서 Empty는 언제 검사해?
A. isLoading과 isError를 처리한 뒤 isSuccess 상태에서 data가 비었는지 검사하는 것이 안전하다.

Q. 검색어 입력 전 화면을 Empty로 보여줘도 돼?
A. 검색 결과 없음과 입력 전 Guide State는 다르므로 구분하는 것이 좋다.

---

## 10.2 Success Feedback Missing Troubleshooting

### [개념]

Success Feedback Missing은 요청은 성공했지만 사용자가 성공 여부를 인지하지 못하거나 화면 데이터가 바뀌지 않는 문제다.

이 문제는 onSuccess 누락, 성공 메시지 누락, Query Invalidation 누락, cache update 누락에서 자주 발생한다.

---

### [핵심]

주요 원인:

- onSuccess 처리 누락
- Toast / Inline Message 누락
- Query Invalidation 누락
- queryKey 불일치
- Button State 복구 누락
- Form Reset 기준 없음
- Redirect 기준 없음
- cache update 누락
- optimistic rollback 누락
- stale UI 유지

핵심 규칙:

- 성공 후 사용자에게 결과를 인지시킨다.
- 관련 데이터를 동기화한다.
- 버튼 pending 상태를 복구한다.
- 필요한 경우 form reset 또는 redirect를 수행한다.
- 성공 후 화면 변화가 충분하면 Toast를 생략할 수 있다.
- 중요한 성공은 화면에 남는 방식으로 제공한다.

---

### [실무]

나쁜 예:

```tsx
const mutation = useMutation({
  mutationFn: createReview,
});
```

개선 예:

```tsx
const mutation = useMutation({
  mutationFn: createReview,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ["reviews", festivalId] });
    queryClient.invalidateQueries({
      queryKey: ["festival-detail", festivalId],
    });
    toast.success("리뷰가 등록되었습니다.");
    resetForm();
  },
});
```

Debug Flow:

```text
요청 성공
→ onSuccess 실행 확인
→ Success Message 확인
→ Query Invalidation 확인
→ queryKey 일치 확인
→ UI 데이터 갱신 확인
→ Button State 확인
→ Redirect / Reset 확인
```

권장:

- Mutation별 성공 후 영향 Query를 정리한다.
- Toast, Inline Message, Redirect 중 적절한 방식을 선택한다.
- 좋아요 / 찜은 버튼 상태 변화로 충분할 수 있다.
- 결제 / 가입 완료는 완료 페이지를 고려한다.
- stale UI 발생 시 queryKey를 우선 확인한다.

주의:

- Toast만 있고 데이터 갱신이 없으면 신뢰가 떨어진다.
- queryKey 불일치로 invalidate가 동작하지 않을 수 있다.
- 성공 후 redirect가 너무 빠르면 사용자가 결과를 놓칠 수 있다.
- optimistic UI 실패 시 rollback 없으면 화면이 틀어질 수 있다.

---

### [FAQ]

Q. 요청은 성공했는데 사용자가 성공했는지 몰라?
A. Success Message, 화면 갱신, redirect, 버튼 상태 복구가 누락되었을 수 있다.

Q. 성공 Toast는 있는데 목록이 그대로야?
A. Query Invalidation 또는 cache update가 누락되었을 가능성이 높다.

Q. 성공 후 버튼이 계속 disabled야?
A. pending 상태가 정상적으로 종료되는지, mutation 상태를 올바르게 사용하는지 확인해야 한다.

Q. 성공 후 Form을 reset해야 해?
A. 상황에 따라 다르다. 작성 완료 후 새 입력을 받을 때는 reset하고, 설정 저장은 입력값을 유지하는 경우가 많다.

---

# 11. Route / Boundary Troubleshooting Rules

## 11.1 Route Flicker Troubleshooting

### [개념]

Route Flicker는 로그인 페이지, 메인 페이지, 권한 페이지, Loading 화면이 짧게 깜빡이며 잘못 보이는 문제다.

Route Flicker는 auth initialized 구분 없음, token refresh 중 redirect, role loading 전 forbidden 판단에서 자주 발생한다.

---

### [핵심]

주요 원인:

- auth initialized 없음
- user null을 즉시 unauthenticated로 판단
- token refresh 중 Login Redirect
- PublicOnlyRoute 조기 redirect
- ProtectedRoute 조기 redirect
- role loading 전 Forbidden 처리
- auth query enabled 조건 오류
- login redirect state 처리 오류
- redirect loop

핵심 규칙:

- auth initialized 전에는 redirect하지 않는다.
- token refresh 중에는 Auth Loading을 보여준다.
- role 정보가 필요한 경우 권한 판정 전 Loading을 표시한다.
- PublicOnlyRoute와 ProtectedRoute 조건을 일관되게 작성한다.
- Login 후 복귀 경로를 명확히 처리한다.
- auth 기반 query는 auth 확인 후 enabled한다.

---

### [실무]

나쁜 예:

```tsx
if (!user) {
  return <Navigate to="/login" />;
}
```

개선 예:

```tsx
if (!initialized) {
  return <LoadingState message="인증 상태를 확인 중입니다." />;
}

if (!user) {
  return <Navigate to="/login" replace />;
}
```

Role Loading 예:

```tsx
if (!authInitialized || roleLoading) {
  return <LoadingState message="권한 정보를 확인 중입니다." />;
}

if (!hasPermission) {
  return <ForbiddenPage />;
}
```

Debug Flow:

```text
Route Flicker 발생
→ auth initialized 확인
→ user 초기값 확인
→ token refresh 상태 확인
→ role loading 확인
→ redirect 조건 순서 확인
→ location state 확인
→ redirect loop 확인
```

권장:

- auth initialized, user, role loading을 분리한다.
- redirect 조건은 loading 상태 이후에 실행한다.
- 로그인 후 이동 위치를 location state로 관리한다.
- Protected query는 auth 확인 후 enabled한다.

주의:

- 인증 확인 전 login redirect를 실행하지 않는다.
- 권한 정보 로딩 전 ForbiddenPage를 보여주지 않는다.
- Login Page와 ProtectedRoute가 서로 redirect loop를 만들 수 있다.
- token refresh 실패와 refresh 진행 중 상태를 구분한다.

---

### [FAQ]

Q. 로그인 페이지가 잠깐 보였다가 메인으로 가?
A. auth initialized 전에 PublicOnlyRoute 또는 ProtectedRoute가 redirect 판단을 실행했을 수 있다.

Q. 권한 없음 페이지가 잠깐 보였다가 정상 페이지가 보여?
A. role 정보가 로딩되기 전에 Forbidden 판단을 했을 수 있다.

Q. Route Flicker를 막으려면?
A. auth initialized와 role loading 상태를 먼저 확인하고 그 이후 redirect나 forbidden 판단을 해야 한다.

Q. token refresh 중에는 어떤 UI를 보여줘?
A. 인증 상태를 확인 중이라는 Auth Loading UI를 보여주는 것이 적합하다.

---

## 11.2 Error Boundary Not Catching

### [개념]

Error Boundary Not Catching은 오류가 발생했지만 Error Boundary Fallback이 표시되지 않는 문제다.

주요 원인은 API Error, Event Handler Error, Async Promise Error처럼 Error Boundary가 처리하지 않는 오류를 Boundary가 잡을 것으로 기대하는 경우다.

---

### [핵심]

Error Boundary가 잡지 못하는 오류:

- API Request Failure
- Async Promise Rejection
- Event Handler Error
- setTimeout 내부 Error
- Form Validation Error
- Network Error
- 401 / 403 Error
- Route 404

핵심 규칙:

- 렌더링 중 오류만 Error Boundary가 처리한다.
- API Error는 Error State로 처리한다.
- Event Handler Error는 try/catch로 처리한다.
- Promise Error는 catch 또는 async/await try/catch로 처리한다.
- Boundary는 오류 발생 컴포넌트의 상위에 있어야 한다.
- Fallback UI 자체가 crash되지 않아야 한다.

---

### [실무]

잡히지 않는 async error:

```tsx
async function handleClick() {
  const result = await api.get("/fail");
  setData(result.data);
}
```

개선:

```tsx
async function handleClick() {
  try {
    const result = await api.get("/fail");
    setData(result.data);
  } catch (error) {
    setError(getApiErrorMessage(error));
  }
}
```

렌더링 오류 예:

```tsx
function UserProfile({ user }) {
  return <h1>{user.name.toUpperCase()}</h1>;
}
```

`user`가 undefined면 렌더링 중 오류가 발생할 수 있으며, 상위 Error Boundary가 Fallback UI를 보여줄 수 있다.

Debug Flow:

```text
오류 발생
→ render error인지 확인
→ async / event error인지 확인
→ Boundary 위치 확인
→ Fallback UI 오류 여부 확인
→ API Error State 필요 여부 확인
```

권장:

- 오류 발생 위치를 먼저 분류한다.
- 렌더링 오류는 Boundary로 격리한다.
- 비동기 오류는 Error State로 처리한다.
- Fallback UI는 단순하고 안전하게 작성한다.

주의:

- Error Boundary를 API 에러 처리기로 사용하지 않는다.
- Promise rejection은 Error Boundary로 자동 처리되지 않는다.
- 이벤트 핸들러 오류도 자동으로 잡히지 않는다.
- Fallback UI에서 다시 오류가 나면 복구가 어렵다.

---

### [FAQ]

Q. Error Boundary가 오류를 못 잡아?
A. 오류가 API error, event handler error, async promise error라면 Error Boundary가 자동으로 잡지 못한다.

Q. API Error는 Error Boundary로 처리하면 안 돼?
A. 아니다. API Error는 Query Error State나 try/catch 기반 Error State로 처리해야 한다.

Q. Error Boundary가 잡는 오류는 뭐야?
A. 주로 React 렌더링 중 발생한 오류와 child component crash를 처리한다.

Q. Fallback UI도 오류가 날 수 있어?
A. 가능하다. Fallback UI는 의존성을 줄이고 단순하게 작성해야 한다.

---

# 12. Security / Accessibility Checklist

## 12.1 Accessibility Review Checklist

### [개념]

Accessibility Review Checklist는 Loading, Error, Empty, Success 상태가 보조 기술 사용자와 키보드 사용자에게도 이해 가능하고 조작 가능한지 검수하는 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] Loading 상태에 텍스트 메시지 또는 접근 가능한 label이 있는가?
- [ ] Spinner만으로 Loading을 표현하지 않는가?
- [ ] Skeleton 장식 요소가 불필요하게 읽히지 않는가?
- [ ] 필요한 영역에 aria-busy를 적용했는가?
- [ ] 중요한 상태 메시지에 role="status"를 고려했는가?
- [ ] Error Message가 텍스트로 제공되는가?
- [ ] 중요한 Error Message에 role="alert"를 고려했는가?
- [ ] Field Error가 input과 aria-describedby로 연결되는가?
- [ ] Field Error에 aria-invalid가 적용되는가?
- [ ] Retry Button이 실제 button 요소인가?
- [ ] CTA가 button/link 역할에 맞게 구현되었는가?
- [ ] 색상만으로 성공/오류/경고를 표현하지 않는가?
- [ ] Empty State에 heading과 description이 있는가?
- [ ] Success Message가 텍스트로 제공되는가?
- [ ] Toast가 너무 빨리 사라지거나 접근성에서 누락되지 않는가?
- [ ] Focus 이동이 필요한 상황에만 적용되는가?
- [ ] Route Error와 Fallback UI에 heading과 action이 있는가?
```

---

### [실무]

검수 흐름:

```text
UI State 확인
→ Text Message 확인
→ ARIA 필요성 확인
→ Keyboard 접근 확인
→ Focus 흐름 확인
→ Color-only 여부 확인
→ Toast / Fallback 접근성 확인
```

상태별 필수 확인:

| 상태        | 검수 기준                            |
| ----------- | ------------------------------------ |
| Loading     | Text, role status, aria-busy         |
| Error       | role alert, Retry Button, safe text  |
| Empty       | Heading, description, CTA            |
| Success     | role status, visible text            |
| Form Error  | aria-invalid, aria-describedby       |
| Route Error | main, heading, link                  |
| Fallback UI | safe message, action, no stack trace |

---

### [FAQ]

Q. Accessibility 검수에서 가장 중요한 것은?
A. 상태가 시각적으로만 전달되지 않고 텍스트, 키보드, 보조 기술로도 전달되는지 확인하는 것이다.

Q. Loading 접근성 검수 핵심은?
A. Spinner나 Skeleton만 사용하지 않고 Loading Message와 적절한 role을 제공하는지 확인하는 것이다.

Q. Error 접근성 검수 핵심은?
A. 오류 메시지가 텍스트로 제공되고 사용자가 Retry나 수정 행동을 수행할 수 있는지 확인하는 것이다.

Q. Form Error 접근성 검수 핵심은?
A. Field Error가 input과 연결되고 키보드 사용자가 오류를 찾아 수정할 수 있는지 확인하는 것이다.

---

## 12.2 Security Review Checklist

### [개념]

Security Review Checklist는 Error UX가 사용자에게 필요한 안내만 제공하고 민감한 내부 정보를 노출하지 않는지 검수하는 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] 서버 원문 message를 그대로 사용자에게 노출하지 않는가?
- [ ] Stack Trace가 운영 UI에 표시되지 않는가?
- [ ] SQL Error가 사용자에게 노출되지 않는가?
- [ ] Server Path / File System Path가 노출되지 않는가?
- [ ] Access Token / Refresh Token이 UI나 console에 출력되지 않는가?
- [ ] Password나 개인정보가 오류 메시지에 포함되지 않는가?
- [ ] API Secret / External API Key가 노출되지 않는가?
- [ ] 403 Error에서 내부 role 정책을 과도하게 노출하지 않는가?
- [ ] Login Error가 계정 존재 여부를 과도하게 노출하지 않는가?
- [ ] User Message와 Developer Log를 분리했는가?
- [ ] Developer Log에서도 민감정보를 마스킹하는가?
- [ ] 500 Error에 generic message를 사용하는가?
- [ ] Validation Error가 사용자 수정에 필요한 정보만 제공하는가?
- [ ] Error Boundary Fallback이 stack trace를 표시하지 않는가?
```

---

### [실무]

검수 흐름:

```text
Error Message 확인
→ Server Raw Message 노출 확인
→ Token / Password / Personal Data 확인
→ Stack Trace / SQL Error 확인
→ 401 / 403 메시지 확인
→ User Message / Developer Log 분리 확인
→ 운영 환경 표시 수준 확인
```

노출 금지 예:

```text
JWT expired at 2026-07-05T12:00:00 with token eyJhbGciOi...
```

안전한 예:

```text
로그인이 만료되었습니다. 다시 로그인해 주세요.
```

권장:

- 공통 Error Message Mapping을 사용한다.
- 운영 환경에서는 generic message를 기본으로 한다.
- 문의용 Error Code는 민감하지 않은 값으로 제한한다.
- 개발 로그도 민감정보를 마스킹한다.

주의:

- console.log도 사용자 브라우저에서 확인 가능하다.
- Frontend 번들에 API Secret을 포함하지 않는다.
- token 만료 상세값을 사용자 메시지로 노출하지 않는다.
- 403에서 내부 role 이름이나 SecurityConfig 경로를 노출하지 않는다.

---

### [FAQ]

Q. Security 검수에서 가장 중요한 것은?
A. 오류 메시지와 로그를 통해 stack trace, SQL Error, token, password, 내부 경로가 노출되지 않는지 확인하는 것이다.

Q. 서버 message를 그대로 쓰면 안 돼?
A. 내부 정보가 포함될 수 있으므로 사용자용 메시지로 변환하는 것이 안전하다.

Q. console.log도 보안 문제가 될 수 있어?
A. 가능하다. 브라우저 콘솔에서 확인 가능하므로 token, 개인정보, 내부 정보를 출력하지 않아야 한다.

Q. 500 Error 메시지는 어떻게 쓰는 게 안전해?
A. “서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.” 같은 generic message가 안전하다.

---

# 13. Final Troubleshooting Checklist

## 13.1 Troubleshooting Review Checklist

### [개념]

Troubleshooting Review Checklist는 Error Handling & Loading UX 문제를 증상별로 빠르게 분류하고 점검하는 최종 검수 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] Infinite Loading 발생 시 finally / enabled / auth initialized를 확인했는가?
- [ ] Blank Screen 발생 시 Console / Network / Route / Error Boundary를 확인했는가?
- [ ] Error Message 미표시 시 catch / setError / Promise.reject를 확인했는가?
- [ ] Retry 미동작 시 onRetry / refetch / enabled 조건을 확인했는가?
- [ ] Empty Flicker 발생 시 Loading과 Error를 먼저 검사하는가?
- [ ] Duplicate Request 발생 시 StrictMode / queryKey / useEffect를 확인했는가?
- [ ] Submit Button Stuck 발생 시 mutationFn Promise 반환을 확인했는가?
- [ ] Success Feedback Missing 발생 시 onSuccess / invalidateQueries를 확인했는가?
- [ ] Stale UI 발생 시 queryKey와 invalidate key를 확인했는가?
- [ ] Route Flicker 발생 시 auth initialized와 role loading을 확인했는가?
- [ ] Error Boundary 미작동 시 async error인지 render error인지 분류했는가?
- [ ] Form Error 미표시 시 server errors key와 input name을 확인했는가?
- [ ] Network Error 발생 시 CORS / baseURL / server running을 확인했는가?
- [ ] Security 노출 가능성을 함께 확인했는가?
- [ ] Accessibility 누락 가능성을 함께 확인했는가?
```

---

### [실무]

최종 Debug Flow:

```text
증상 확인
→ UI State 분류
→ Network / Console 확인
→ State / Query / Mutation 확인
→ Conditional Rendering 확인
→ Error Mapping 확인
→ Route / Boundary 확인
→ Accessibility 확인
→ Security 확인
→ 수정 및 재검수
```

증상별 핵심 키워드:

| 증상             | 검색 키워드                                 |
| ---------------- | ------------------------------------------- |
| Loading 안 끝남  | Infinite Loading, finally, enabled          |
| 화면 비어 있음   | Blank Screen, Error Boundary, map undefined |
| Error 안 보임    | Error Message Not Showing, Promise.reject   |
| Empty 깜빡임     | Empty Flicker, initial empty array          |
| 요청 중복        | Duplicate Request, StrictMode, queryKey     |
| 버튼 멈춤        | Submit Button Stuck, mutationFn Promise     |
| 성공 미표시      | Success Feedback Missing, invalidateQueries |
| 화면 stale       | Stale UI, queryKey mismatch                 |
| 라우트 깜빡임    | Route Flicker, auth initialized             |
| Boundary 안 잡음 | Error Boundary Not Catching, async error    |

---

### [FAQ]

Q. Troubleshooting Review에서 가장 중요한 것은?
A. 증상을 먼저 분류하고 Network, Console, State, Query, Rendering 조건을 순서대로 확인하는 것이다.

Q. Loading 문제와 Empty 문제는 어떻게 구분해?
A. Loading은 요청 진행 또는 종료 문제이고 Empty는 요청 성공 후 데이터 없음 판정 문제다.

Q. Error 문제와 Boundary 문제는 어떻게 구분해?
A. API 요청 실패는 Error State 문제이고 렌더링 중 crash는 Error Boundary 문제다.

Q. 최종 검수에서 Accessibility와 Security도 봐야 해?
A. 그렇다. Error Handling & Loading UX는 사용자 상태 전달뿐 아니라 접근성과 보안 노출까지 함께 검수해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Error Handling & Loading UX Part07은 무엇을 다뤄?
A. Accessibility, Security, User Message와 Developer Log 분리, Loading/Error/Empty/Success Troubleshooting 기준을 다룬다.

Q. Error Handling & Loading UX에서 접근성이 왜 중요해?
A. Loading, Error, Empty, Success 상태를 모든 사용자가 이해하고 다음 행동을 할 수 있어야 하기 때문이다.

Q. Spinner만 보여주면 접근성에 충분해?
A. 아니다. 스크린 리더가 이해할 수 있는 텍스트나 role status 같은 속성이 필요하다.

Q. Error Message는 색상만 빨갛게 하면 돼?
A. 아니다. 텍스트, 아이콘, ARIA 속성 등 색상 외 정보가 필요하다.

Q. Loading Message는 꼭 필요해?
A. 시각적 표시만으로 상태 전달이 어려우므로 텍스트나 접근성 label을 제공하는 것이 좋다.

Q. Spinner에는 어떤 접근성 처리가 필요해?
A. Spinner 자체는 장식이면 aria-hidden 처리하고, 주변에 role status나 텍스트 메시지를 제공한다.

Q. Skeleton은 스크린 리더가 읽어야 해?
A. 대부분 장식 요소로 보고 aria-hidden 처리하거나 별도 Loading Message를 제공하는 것이 좋다.

Q. aria-busy는 언제 써?
A. 특정 콘텐츠 영역이 데이터를 불러오거나 업데이트 중일 때 사용할 수 있다.

Q. role status는 언제 써?
A. 사용자에게 Loading이나 Success 같은 상태 변화를 부드럽게 알릴 때 사용한다.

Q. role status와 role alert는 달라?
A. 다르다. status는 일반 상태 안내이고 alert는 중요한 오류나 즉시 알려야 하는 메시지에 적합하다.

Q. Error Message에는 role alert가 필요해?
A. 중요한 오류 메시지에는 고려할 수 있지만, 모든 오류에 남발하지 않는 것이 좋다.

Q. Retry Button은 div로 만들어도 돼?
A. 권장하지 않는다. 실제 button 요소를 사용해야 키보드와 보조 기술 접근성이 좋다.

Q. Field Error는 왜 input과 연결해야 해?
A. 보조 기술 사용자가 어떤 입력값에 오류가 있는지 이해하고 수정할 수 있게 하기 위해서다.

Q. 오류가 발생하면 무조건 focus를 이동해야 해?
A. 아니다. Form 제출 실패나 페이지 전환처럼 사용자가 위치를 잃기 쉬운 경우에만 신중히 적용한다.

Q. 긴 Form에서 오류가 많으면 어디로 focus를 보내?
A. Error Summary로 focus를 이동하고 각 오류에서 해당 field로 이동할 수 있게 하는 방식이 유용하다.

Q. Toast Error에 focus를 이동해야 해?
A. 보통 하지 않는다. Toast는 일시적 알림이며 focus 이동은 사용자 작업을 방해할 수 있다.

Q. Empty State에도 접근성이 필요해?
A. 필요하다. 데이터가 없는 상태와 다음 행동을 모든 사용자가 이해할 수 있어야 한다.

Q. Empty State CTA는 button이 좋아 link가 좋아?
A. 화면 내 동작이면 button, 다른 페이지 이동이면 link가 적합하다.

Q. Empty State icon은 스크린 리더가 읽어야 해?
A. 대부분 장식 요소라면 aria-hidden 처리하는 것이 좋다.

Q. Success Message에도 접근성이 필요해?
A. 필요하다. 보조 기술 사용자도 요청이 성공했음을 인지할 수 있어야 한다.

Q. 좋아요 버튼 상태는 어떻게 전달해?
A. 버튼 문구를 바꾸거나 aria-pressed를 사용해 눌림 상태를 전달할 수 있다.

Q. 결제 완료는 Toast로 충분해?
A. 보통은 완료 페이지처럼 화면에 남는 접근 가능한 확인 UX가 더 적합하다.

Q. 서버 에러 원문을 그대로 보여주면 안 되는 이유는?
A. 내부 구조, SQL, 서버 경로, 보안 정보가 노출될 수 있기 때문이다.

Q. 개발자 로그와 사용자 메시지는 왜 나눠?
A. 사용자는 이해 가능한 해결 안내가 필요하고 개발자는 원인 분석 정보가 필요하기 때문이다.

Q. Stack Trace를 사용자에게 보여줘도 돼?
A. 운영 환경에서는 보여주지 않는 것이 좋다.

Q. 403에서 필요한 role 정보를 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 권한 정책을 과도하게 노출하지 않는 메시지가 좋다.

Q. User Message와 Developer Log는 어떻게 달라?
A. User Message는 사용자 안내용이고 Developer Log는 개발자 원인 분석용이다.

Q. 사용자 메시지에 status code를 넣어도 돼?
A. 필요한 경우 제한적으로 가능하지만 대부분은 이해 가능한 문장으로 바꾸는 것이 좋다.

Q. 로그에도 민감정보를 남기면 안 돼?
A. 그렇다. 로그도 유출될 수 있으므로 token, password, 개인정보는 마스킹하거나 기록하지 않는다.

Q. Troubleshooting에서 가장 먼저 확인할 것은?
A. 증상을 분류하고 Network, Console, 상태값, 조건부 렌더링 순서를 확인하는 것이다.

Q. Error Handling 문제는 어디서 많이 생겨?
A. catch 누락, Error State 미연결, interceptor Promise.reject 누락, 서버 message mapping 실패에서 자주 생긴다.

Q. Loading 문제는 어디서 많이 생겨?
A. finally 누락, query enabled 조건 오류, pending request, useEffect dependency loop에서 자주 생긴다.

Q. 빈 화면 문제는 어디서 많이 생겨?
A. Runtime render error, data undefined 접근, Route mismatch, Loading/Error/Empty 처리 누락에서 자주 생긴다.

Q. Loading이 계속 끝나지 않아?
A. finally에서 loading false를 호출하는지, API 요청이 완료되는지, Error State로 전환되는지 확인해야 한다.

Q. API 실패 후에도 Loading이 계속돼?
A. catch 또는 finally에서 상태를 종료하지 않았거나 Error State 전환이 누락되었을 수 있다.

Q. enabled false인데 Loading이 계속 보여?
A. 요청이 시작되지 않은 상태일 수 있으므로 Idle 또는 Guide State를 별도로 설계해야 한다.

Q. auth loading이 계속되면?
A. 인증 초기화 로직에서 성공 / 실패와 관계없이 initialized를 true로 바꾸는지 확인해야 한다.

Q. Submit Button이 계속 처리 중이야?
A. mutationFn이 Promise를 반환하는지, 요청이 완료되는지, error를 삼키지 않는지, loading state를 해제하는지 확인해야 한다.

Q. mutationFn에서 api.post를 return해야 해?
A. 그렇다. Promise를 반환해야 pending, success, error 상태를 정확히 추적할 수 있다.

Q. catch에서 console.log만 하면 안 돼?
A. error를 다시 throw하지 않으면 onError가 실행되지 않거나 실패 상태가 사라질 수 있다.

Q. API는 실패했는데 에러 메시지가 안 보여?
A. catch에서 에러를 상태로 저장하는지, Error UI 조건이 맞는지, error mapping 함수가 올바른지 확인해야 한다.

Q. interceptor에서 Toast는 뜨는데 화면 ErrorState가 안 떠?
A. Promise.reject를 반환하지 않아 호출부가 error를 받지 못할 수 있다.

Q. Error Message가 DOM에는 있는데 안 보여?
A. CSS display, visibility, z-index, conditional rendering 조건을 확인해야 한다.

Q. 다시 시도 버튼이 눌리는데 요청이 안 나가?
A. onRetry 연결, refetch 호출, enabled 조건, Network 요청 발생 여부를 확인해야 한다.

Q. Retry Button은 모든 ErrorState에 넣어야 해?
A. 아니다. 네트워크나 일시적 서버 오류에는 적합하지만 401, 403, 404에는 다른 액션이 더 적합할 수 있다.

Q. Empty State가 잠깐 보였다가 목록이 보여?
A. 요청 완료 전 빈 배열을 Empty로 판정했을 가능성이 있다.

Q. Empty Flicker를 막으려면?
A. Loading과 Error를 먼저 검사하고 요청 성공 후에만 Empty를 표시해야 한다.

Q. 검색어 입력 전 화면을 Empty로 보여줘도 돼?
A. 검색 결과 없음과 입력 전 Guide State는 다르므로 구분하는 것이 좋다.

Q. 요청은 성공했는데 사용자가 성공했는지 몰라?
A. Success Message, 화면 갱신, redirect, 버튼 상태 복구가 누락되었을 수 있다.

Q. 성공 Toast는 있는데 목록이 그대로야?
A. Query Invalidation 또는 cache update가 누락되었을 가능성이 높다.

Q. 로그인 페이지가 잠깐 보였다가 메인으로 가?
A. auth initialized 전에 PublicOnlyRoute 또는 ProtectedRoute가 redirect 판단을 실행했을 수 있다.

Q. 권한 없음 페이지가 잠깐 보였다가 정상 페이지가 보여?
A. role 정보가 로딩되기 전에 Forbidden 판단을 했을 수 있다.

Q. Route Flicker를 막으려면?
A. auth initialized와 role loading 상태를 먼저 확인하고 그 이후 redirect나 forbidden 판단을 해야 한다.

Q. Error Boundary가 오류를 못 잡아?
A. 오류가 API error, event handler error, async promise error라면 Error Boundary가 자동으로 잡지 못한다.

Q. API Error는 Error Boundary로 처리하면 안 돼?
A. 아니다. API Error는 Query Error State나 try/catch 기반 Error State로 처리해야 한다.

Q. Accessibility 검수에서 가장 중요한 것은?
A. 상태가 시각적으로만 전달되지 않고 텍스트, 키보드, 보조 기술로도 전달되는지 확인하는 것이다.

Q. Security 검수에서 가장 중요한 것은?
A. 오류 메시지와 로그를 통해 stack trace, SQL Error, token, password, 내부 경로가 노출되지 않는지 확인하는 것이다.

Q. Troubleshooting Review에서 가장 중요한 것은?
A. 증상을 먼저 분류하고 Network, Console, State, Query, Rendering 조건을 순서대로 확인하는 것이다.
