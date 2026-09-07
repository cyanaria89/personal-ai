# Error Handling & Loading UX Part08 - Component Pattern & Review Rules

---

# 1. State Component Pattern Overview

## 1.1 State Component Pattern Purpose

### [개념]

State Component Pattern은 Loading, Error, Empty, Success, Fallback 상태를 반복 가능한 UI 컴포넌트로 분리하는 기준이다.

Frontend Agent는 화면마다 임시로 상태 UI를 작성하지 않고, 공통 State Component를 활용해 일관된 UX와 검수 가능한 구조를 만들어야 한다.

---

### [핵심]

State Component 주요 대상:

- LoadingState
- ErrorState
- EmptyState
- SuccessMessage
- PageError
- FieldError
- FormAlert
- RetryButton
- Skeleton
- FallbackUI
- NotFoundState
- ForbiddenState
- SubmitButton
- LoadMoreButton

핵심 규칙:

- Loading / Error / Empty / Success 컴포넌트를 분리한다.
- ErrorState와 EmptyState를 하나로 합치지 않는다.
- FieldError와 FormAlert를 구분한다.
- Page Error와 Form Error를 구분한다.
- RetryButton은 실제 retry 함수와 연결한다.
- Skeleton은 콘텐츠 구조가 명확한 곳에 사용한다.
- 공통 컴포넌트는 문구를 하드코딩하지 않고 props로 전달받는다.
- 접근성과 보안 기준을 컴포넌트 수준에서 기본 제공한다.

---

### [실무]

권장 파일 구조:

```text
src
├ components
│  ├ states
│  │  ├ LoadingState.tsx
│  │  ├ ErrorState.tsx
│  │  ├ EmptyState.tsx
│  │  ├ SuccessMessage.tsx
│  │  ├ PageError.tsx
│  │  ├ NotFoundState.tsx
│  │  ├ ForbiddenState.tsx
│  │  └ FallbackUI.tsx
│  ├ forms
│  │  ├ FieldError.tsx
│  │  ├ FormAlert.tsx
│  │  └ SubmitButton.tsx
│  └ loading
│     ├ Spinner.tsx
│     ├ Skeleton.tsx
│     └ LoadMoreButton.tsx
```

기본 설계 흐름:

```text
UI 상태 분류
→ 공통 State Component 선택
→ 화면별 message 전달
→ action / retry / CTA 연결
→ accessibility 속성 확인
→ security message 확인
```

---

### [FAQ]

Q. State Component Pattern은 뭐야?
A. Loading, Error, Empty, Success 같은 화면 상태를 재사용 가능한 컴포넌트로 분리하는 기준이다.

Q. ErrorState와 EmptyState를 하나로 합쳐도 돼?
A. 권장하지 않는다. 요청 실패와 데이터 없음은 의미와 사용자 행동이 다르기 때문이다.

Q. 공통 컴포넌트에 문구를 하드코딩해도 돼?
A. 권장하지 않는다. 화면 문맥에 맞는 message를 props로 전달하는 것이 좋다.

Q. State Component Pattern의 장점은?
A. UX 일관성, 접근성 기본값, 중복 제거, Review Agent 검수 용이성이 좋아진다.

---

# 2. LoadingState Component Rules

## 2.1 LoadingState Design

### [개념]

LoadingState는 페이지, 섹션, 목록, 버튼, 인증 상태에서 요청이 진행 중임을 표현하는 컴포넌트다.

LoadingState는 단순 시각 표시가 아니라 사용자가 무엇을 기다리는지 이해할 수 있게 해야 한다.

---

### [핵심]

LoadingState 구성 요소:

- message
- variant
- size
- aria-busy
- role status
- spinner optional
- skeleton optional
- label
- className optional

핵심 규칙:

- Loading Message를 제공한다.
- Spinner만 단독으로 사용하지 않는다.
- Page Loading과 Section Loading을 구분한다.
- Skeleton은 별도 컴포넌트로 분리할 수 있다.
- `role="status"`를 고려한다.
- Loading 종료 후 Error / Empty / Success로 전환 가능해야 한다.
- Auth Loading은 일반 Page Loading과 문구를 구분한다.

---

### [실무]

LoadingState 예:

```tsx
type LoadingStateProps = {
  message?: string;
};

function LoadingState({ message = "불러오는 중입니다." }: LoadingStateProps) {
  return (
    <section aria-busy="true">
      <p role="status">{message}</p>
    </section>
  );
}
```

사용 예:

```tsx
<LoadingState message="축제 목록을 불러오는 중입니다." />
```

Auth Loading 예:

```tsx
<LoadingState message="인증 상태를 확인 중입니다." />
```

권장:

- 로딩 대상이 무엇인지 message에 포함한다.
- 페이지 전체를 막는 Loading과 일부 영역 Loading을 구분한다.
- 반복되는 작은 로딩은 Spinner 또는 Button Loading으로 처리한다.
- Skeleton UI와 같이 사용할 때는 Skeleton이 장식 요소인지 확인한다.

주의:

- 무한 Loading에 빠질 수 있으므로 Error State 전환 경로를 둔다.
- `aria-busy=true`가 계속 유지되지 않게 한다.
- Loading 문구 없이 시각적 animation만 보여주지 않는다.
- Submit Loading을 Page Loading으로 대체하지 않는다.

---

### [FAQ]

Q. LoadingState에는 message가 꼭 필요해?
A. 권장된다. 사용자가 무엇을 기다리는지 알 수 있어야 한다.

Q. LoadingState에 Spinner만 넣어도 돼?
A. 권장하지 않는다. 텍스트나 접근 가능한 label을 함께 제공하는 것이 좋다.

Q. Auth Loading 문구는 따로 써야 해?
A. 좋다. “인증 상태를 확인 중입니다.”처럼 일반 데이터 조회와 구분하는 것이 명확하다.

Q. LoadingState가 계속 보이면 무엇을 확인해야 해?
A. 요청 완료 여부, finally, enabled 조건, auth initialized, Error State 전환 여부를 확인해야 한다.

---

## 2.2 Skeleton Component Rules

### [개념]

Skeleton Component는 실제 콘텐츠 레이아웃을 미리 보여주는 Loading UI다.

Skeleton은 카드 목록, 상세 페이지, 테이블, 프로필 영역처럼 구조가 예측 가능한 화면에 적합하다.

---

### [핵심]

Skeleton Component 대상:

- Card Skeleton
- List Skeleton
- Detail Skeleton
- Table Row Skeleton
- Profile Skeleton
- Image Grid Skeleton
- Dashboard Widget Skeleton

핵심 규칙:

- 실제 콘텐츠 구조와 유사해야 한다.
- 장식 요소는 `aria-hidden` 처리한다.
- 상위 Loading Message를 제공한다.
- 초기 로딩에 적합하다.
- 버튼 제출이나 짧은 액션에는 사용하지 않는다.
- 실제 콘텐츠와 크기 차이를 줄여 Layout Shift를 방지한다.

---

### [실무]

Card Skeleton 예:

```tsx
function FestivalCardSkeleton() {
  return (
    <article aria-hidden="true" className="festival-card-skeleton">
      <div className="image-placeholder" />
      <div className="title-placeholder" />
      <div className="text-placeholder" />
    </article>
  );
}
```

List Skeleton 예:

```tsx
function FestivalListSkeleton() {
  return (
    <section aria-busy="true" aria-label="축제 목록을 불러오는 중입니다.">
      <div aria-hidden="true">
        {Array.from({ length: 6 }).map((_, index) => (
          <FestivalCardSkeleton key={index} />
        ))}
      </div>
    </section>
  );
}
```

권장:

- 카드 목록은 여러 개의 Skeleton Item을 렌더링한다.
- 상세 페이지는 title, image, content 영역을 비슷하게 구성한다.
- Skeleton은 공통 컴포넌트와 도메인별 skeleton을 분리할 수 있다.
- 반복 animation은 과도하지 않게 한다.

주의:

- Skeleton이 실제 화면과 다르면 오히려 혼란을 준다.
- Skeleton Item이 스크린 리더에 모두 읽히지 않게 한다.
- Refetch 중 기존 데이터가 있으면 Skeleton보다 작은 갱신 표시가 적합할 수 있다.
- Skeleton으로 Error State를 대체하지 않는다.

---

### [FAQ]

Q. Skeleton Component는 언제 써?
A. 카드 목록, 상세 페이지, 테이블처럼 콘텐츠 구조가 예측 가능한 초기 로딩에 적합하다.

Q. Skeleton은 LoadingState와 같은 컴포넌트야?
A. 다르다. LoadingState는 상태 안내이고 Skeleton은 콘텐츠 자리 표시 UI다.

Q. Skeleton에 aria-hidden을 써도 돼?
A. 장식용 placeholder라면 `aria-hidden` 처리하고 별도 Loading Message를 제공하는 것이 좋다.

Q. Submit Button에도 Skeleton을 써?
A. 아니다. Submit Button에는 Button Loading이나 Disabled State가 적합하다.

---

# 3. ErrorState Component Rules

## 3.1 ErrorState Design

### [개념]

ErrorState는 API 요청 실패, 네트워크 오류, 서버 오류, 조회 실패 같은 상태를 사용자에게 안내하는 컴포넌트다.

ErrorState는 사용자 메시지와 Retry Action을 포함할 수 있으며, 서버 내부 오류 원문을 그대로 노출하지 않아야 한다.

---

### [핵심]

ErrorState 구성 요소:

- message
- description optional
- onRetry optional
- retrying optional
- action optional
- role alert
- safe user message
- no raw server error
- className optional

핵심 규칙:

- 사용자에게 안전한 message를 제공한다.
- Retry 가능한 오류에는 onRetry를 제공한다.
- Retry Button은 실제 함수와 연결한다.
- ErrorState는 EmptyState와 분리한다.
- ErrorState는 Form Field Error와 분리한다.
- 서버 stack trace, SQL Error, token 값을 노출하지 않는다.
- `role="alert"`를 고려한다.

---

### [실무]

ErrorState 예:

```tsx
type ErrorStateProps = {
  message: string;
  description?: string;
  onRetry?: () => void;
  retrying?: boolean;
};

function ErrorState({
  message,
  description,
  onRetry,
  retrying,
}: ErrorStateProps) {
  return (
    <section role="alert">
      <p>{message}</p>
      {description && <p>{description}</p>}
      {onRetry && (
        <button type="button" onClick={onRetry} disabled={retrying}>
          {retrying ? "다시 시도 중..." : "다시 시도"}
        </button>
      )}
    </section>
  );
}
```

사용 예:

```tsx
<ErrorState
  message="축제 목록을 불러오지 못했습니다."
  description="잠시 후 다시 시도해 주세요."
  onRetry={refetch}
/>
```

권장:

- message는 화면 문맥에 맞게 전달한다.
- 네트워크 오류와 서버 오류 메시지를 구분할 수 있다.
- Retry Button은 조회 실패에 우선 적용한다.
- 401 / 403 / 404는 ErrorState 외 Login / Forbidden / NotFound UX를 고려한다.

주의:

- 모든 Error를 같은 ErrorState 문구로 처리하지 않는다.
- Field Error를 Page ErrorState로만 보여주지 않는다.
- Retry Button만 있고 onRetry가 비어 있으면 안 된다.
- raw error object를 JSX로 그대로 출력하지 않는다.

---

### [FAQ]

Q. ErrorState에는 어떤 props가 필요해?
A. 기본적으로 message가 필요하고, 필요하면 description, onRetry, retrying, action을 받을 수 있다.

Q. ErrorState에 Retry Button은 항상 필요해?
A. 아니다. 재시도 가능한 오류에만 제공하는 것이 좋다.

Q. ErrorState가 Field Error도 처리해도 돼?
A. 권장하지 않는다. Field Error는 input 근처에 별도 컴포넌트로 표시하는 것이 좋다.

Q. ErrorState 메시지에 서버 원문을 넣어도 돼?
A. 권장하지 않는다. 사용자용 안전 메시지로 변환해야 한다.

---

## 3.2 PageError / Resource Error Component Rules

### [개념]

PageError는 페이지나 주요 콘텐츠 조회 실패를 처리하는 컴포넌트다.

Resource Error Component는 상세 리소스가 존재하지 않거나 삭제되었을 때 사용하는 NotFoundState와 구분된다.

---

### [핵심]

PageError 사용 상황:

- List Fetch Failed
- Detail Fetch Failed
- Dashboard Fetch Failed
- Search Request Failed
- Server Error
- Network Error

Resource Error 사용 상황:

- API Resource 404
- Deleted Resource
- Invalid ID
- Hidden Resource
- Expired Resource

핵심 규칙:

- PageError는 요청 실패를 표현한다.
- Resource NotFoundState는 특정 리소스 없음 상태를 표현한다.
- Route NotFoundPage와 API Resource NotFoundState를 구분한다.
- PageError에는 Retry Action이 적합할 수 있다.
- Resource NotFound에는 목록 이동 Action이 적합할 수 있다.
- 사용자에게 내부 endpoint path를 노출하지 않는다.

---

### [실무]

PageError 예:

```tsx
function PageError({ message, onRetry }) {
  return (
    <main role="alert">
      <h1>문제가 발생했습니다.</h1>
      <p>{message}</p>
      {onRetry && (
        <button type="button" onClick={onRetry}>
          다시 시도
        </button>
      )}
    </main>
  );
}
```

Resource NotFoundState 예:

```tsx
function FestivalNotFoundState() {
  return (
    <section>
      <h2>축제 정보를 찾을 수 없습니다.</h2>
      <p>삭제되었거나 더 이상 제공되지 않는 축제일 수 있습니다.</p>
      <Link to="/festivals">축제 목록으로 이동</Link>
    </section>
  );
}
```

권장:

- PageError는 페이지 단위 실패에 사용한다.
- Resource NotFoundState는 상세 리소스 없음에 사용한다.
- Route NotFoundPage는 catch-all route에 사용한다.
- 각각의 action을 상황에 맞게 다르게 둔다.

주의:

- API 404를 무조건 Route NotFoundPage로 보내지 않는다.
- Resource 없음과 목록 Empty를 혼동하지 않는다.
- PageError에서 stack trace를 노출하지 않는다.
- PageError와 Error Boundary Fallback을 혼동하지 않는다.

---

### [FAQ]

Q. PageError와 ErrorState는 달라?
A. PageError는 페이지 단위 실패에 특화된 ErrorState로 볼 수 있다.

Q. Resource NotFoundState와 EmptyState는 달라?
A. 다르다. EmptyState는 목록 데이터 없음이고 Resource NotFoundState는 특정 리소스가 없는 상태다.

Q. API 404는 PageError야 Resource NotFound야?
A. endpoint 오류인지 특정 리소스 없음인지에 따라 다르다. 상세 리소스가 없으면 Resource NotFound가 적합하다.

Q. Resource NotFound에는 Retry가 필요해?
A. 보통은 목록 이동이나 메인 이동이 더 적합하다. 일시적 오류가 아니라면 Retry 효과가 낮다.

---

# 4. EmptyState Component Rules

## 4.1 EmptyState Design

### [개념]

EmptyState는 요청이 성공했지만 표시할 데이터가 없는 상태를 안내하는 컴포넌트다.

EmptyState는 데이터 없음의 이유와 다음 행동을 제공하며, ErrorState와 의미적으로 분리되어야 한다.

---

### [핵심]

EmptyState 구성 요소:

- title
- description optional
- action optional
- icon optional
- heading
- CTA
- context message
- accessible section

핵심 규칙:

- 요청 성공 후 데이터가 없을 때만 사용한다.
- ErrorState와 분리한다.
- title은 현재 상태를 명확히 설명한다.
- description은 이유 또는 다음 행동을 안내한다.
- action은 필요한 경우에만 제공한다.
- CTA는 button 또는 link 역할에 맞게 사용한다.
- 일러스트나 icon은 보조 요소로만 사용한다.

---

### [실무]

EmptyState 예:

```tsx
type EmptyStateProps = {
  title: string;
  description?: string;
  action?: React.ReactNode;
};

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

Search Empty 예:

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

First Use Empty 예:

```tsx
<EmptyState
  title="아직 찜한 축제가 없습니다."
  description="마음에 드는 축제를 찾아 찜해 보세요."
  action={<Link to="/festivals">축제 둘러보기</Link>}
/>
```

권장:

- Search Empty와 First Use Empty 문구를 구분한다.
- CTA는 하나 또는 두 개 이하로 제한한다.
- action은 Empty 원인과 직접 연결한다.
- EmptyState는 재사용하되 문구는 화면에서 전달한다.

주의:

- EmptyState를 요청 실패에 사용하지 않는다.
- “데이터 없음”만 표시하지 않는다.
- 모든 EmptyState에 무조건 CTA를 넣지 않는다.
- 초기 빈 배열을 EmptyState로 바로 처리하지 않는다.

---

### [FAQ]

Q. EmptyState는 언제 사용해?
A. 요청이 성공했고 표시할 데이터가 없을 때 사용한다.

Q. EmptyState와 ErrorState는 왜 분리해야 해?
A. 데이터 없음과 요청 실패는 원인과 사용자 행동이 다르기 때문이다.

Q. EmptyState CTA는 항상 필요해?
A. 아니다. 사용자가 할 수 있는 의미 있는 다음 행동이 있을 때만 제공하면 된다.

Q. EmptyState 문구는 어디서 정하는 게 좋아?
A. 공통 컴포넌트 내부가 아니라 화면 문맥에서 props로 전달하는 것이 좋다.

---

# 5. Form State Component Rules

## 5.1 FieldError Component Rules

### [개념]

FieldError Component는 특정 input에 연결되는 오류 메시지를 일관되게 표시하는 컴포넌트다.

FieldError는 접근성을 위해 input과 `aria-describedby`로 연결될 수 있도록 id 기준을 가져야 한다.

---

### [핵심]

FieldError 구성 요소:

- id
- message
- role alert
- input association
- accessible text
- optional className

핵심 규칙:

- 특정 input 근처에 표시한다.
- error message id를 input의 `aria-describedby`와 연결한다.
- input에는 `aria-invalid`를 적용한다.
- 메시지는 수정 가능한 문장으로 작성한다.
- FieldError를 Toast로 대체하지 않는다.
- error id 중복을 피한다.

---

### [실무]

FieldError 예:

```tsx
type FieldErrorProps = {
  id: string;
  message?: string;
};

function FieldError({ id, message }: FieldErrorProps) {
  if (!message) {
    return null;
  }

  return (
    <p id={id} role="alert">
      {message}
    </p>
  );
}
```

사용 예:

```tsx
<input
  id="email"
  name="email"
  aria-invalid={Boolean(errors.email)}
  aria-describedby={errors.email ? "email-error" : undefined}
/>
<FieldError id="email-error" message={errors.email} />
```

권장:

- field name 기반으로 error id를 생성한다.
- 서버 field error와 client field error를 같은 컴포넌트로 표시한다.
- 긴 Form에서는 Error Summary와 함께 사용할 수 있다.
- 색상 외 텍스트로 오류를 제공한다.

주의:

- id가 중복되면 input 연결이 깨진다.
- FieldError가 input과 너무 멀리 떨어지면 수정 위치를 찾기 어렵다.
- 서버 message에 내부 정보가 포함되면 변환 후 전달한다.
- FieldError를 global alert로만 처리하지 않는다.

---

### [FAQ]

Q. FieldError Component는 왜 필요해?
A. input 오류 표시와 접근성 연결을 일관되게 처리하기 위해 필요하다.

Q. FieldError id는 왜 필요해?
A. input의 `aria-describedby`와 연결해 보조 기술 사용자가 오류를 이해할 수 있게 하기 위해 필요하다.

Q. FieldError에 role alert를 써도 돼?
A. 중요한 입력 오류라면 사용할 수 있지만 너무 과도하게 중복되지 않게 해야 한다.

Q. FieldError를 Toast로 대체해도 돼?
A. 권장하지 않는다. 사용자가 어떤 input을 수정해야 하는지 알기 어렵다.

---

## 5.2 FormAlert Component Rules

### [개념]

FormAlert Component는 Form 전체에 해당하는 오류나 성공 메시지를 표시하는 컴포넌트다.

FormAlert는 로그인 실패, 제출 실패, 서버 장애, 권한 문제처럼 특정 input 하나로 귀속하기 어려운 상태에 사용한다.

---

### [핵심]

FormAlert 구성 요소:

- message
- variant
- role alert or status
- title optional
- action optional
- safe message
- form-level position

핵심 규칙:

- Form 상단 또는 Submit Button 근처에 배치한다.
- FieldError와 구분한다.
- Error variant는 `role="alert"`를 고려한다.
- Success variant는 `role="status"`를 고려한다.
- 서버 내부 message를 그대로 노출하지 않는다.
- Form 제출 실패 후 입력값은 유지한다.

---

### [실무]

FormAlert 예:

```tsx
type FormAlertProps = {
  message?: string;
  variant?: "error" | "success" | "info";
};

function FormAlert({ message, variant = "error" }: FormAlertProps) {
  if (!message) {
    return null;
  }

  const role = variant === "error" ? "alert" : "status";

  return <div role={role}>{message}</div>;
}
```

사용 예:

```tsx
<FormAlert message={formError} variant="error" />
<FormAlert message={successMessage} variant="success" />
```

권장:

- 로그인 실패는 FormAlert error로 처리한다.
- 설정 저장 성공은 FormAlert success로 처리할 수 있다.
- 메시지는 짧고 안전하게 작성한다.
- FormAlert와 FieldError가 동시에 표시될 수 있음을 고려한다.

주의:

- FormAlert를 모든 Field Error 대신 사용하지 않는다.
- Toast만 띄우고 FormAlert를 누락하면 사용자가 오류를 놓칠 수 있다.
- 성공 메시지가 오래 남아 현재 상태와 불일치하지 않게 한다.
- Error variant와 Success variant의 role을 구분한다.

---

### [FAQ]

Q. FormAlert는 언제 써?
A. 로그인 실패, 제출 실패, 서버 장애처럼 Form 전체에 해당하는 메시지를 표시할 때 사용한다.

Q. FormAlert와 FieldError는 뭐가 달라?
A. FormAlert는 Form 전체 메시지이고 FieldError는 특정 input 오류 메시지다.

Q. FormAlert에 success 메시지도 넣어도 돼?
A. 가능하다. variant를 구분하고 success에는 `role="status"`를 고려한다.

Q. 로그인 실패는 FormAlert가 적합해?
A. 보통 적합하다. 계정 정보 불일치는 특정 field 하나의 문제가 아니라 Form 전체 오류로 보는 경우가 많다.

---

# 6. Action Component Rules

## 6.1 RetryButton Rules

### [개념]

RetryButton은 요청 실패 후 사용자가 다시 시도할 수 있게 하는 액션 컴포넌트다.

RetryButton은 단순 버튼이 아니라 실제 refetch 또는 재요청 함수와 연결되어야 한다.

---

### [핵심]

RetryButton 사용 상황:

- Network Error
- Timeout Error
- 500 Server Error
- List Fetch Failed
- Detail Fetch Failed
- Search Request Failed
- Refetch Failed

핵심 규칙:

- 실제 retry 함수와 연결한다.
- retrying 중 disabled 처리할 수 있다.
- 버튼 label은 명확해야 한다.
- Retry가 적합한 오류에만 제공한다.
- 401 / 403 / Resource 404는 다른 액션이 적합할 수 있다.
- 키보드로 접근 가능한 button 요소를 사용한다.

---

### [실무]

RetryButton 예:

```tsx
type RetryButtonProps = {
  onRetry: () => void;
  retrying?: boolean;
};

function RetryButton({ onRetry, retrying }: RetryButtonProps) {
  return (
    <button type="button" onClick={onRetry} disabled={retrying}>
      {retrying ? "다시 시도 중..." : "다시 시도"}
    </button>
  );
}
```

ErrorState 사용 예:

```tsx
<ErrorState message="데이터를 불러오지 못했습니다." onRetry={refetch} />
```

권장:

- RetryButton은 ErrorState 내부에서 사용할 수 있다.
- Retry 중 버튼을 disabled 처리한다.
- Network Error와 500 Error에 우선 제공한다.
- Retry 후 실패하면 ErrorState를 유지한다.

주의:

- RetryButton만 있고 `onRetry`가 실제 요청을 하지 않으면 안 된다.
- Retry가 불가능한 오류에 제공하면 사용자 혼란이 생긴다.
- Retry 중 Loading 표시가 없으면 버튼이 눌렸는지 알기 어렵다.
- 버튼 대신 div를 사용하지 않는다.

---

### [FAQ]

Q. RetryButton은 언제 필요해?
A. 네트워크 오류, 일시적 서버 오류, 조회 실패처럼 재시도 가능성이 있는 오류에 필요하다.

Q. RetryButton은 모든 오류에 넣어도 돼?
A. 아니다. 401, 403, 삭제된 리소스 404에는 로그인, 권한 안내, 목록 이동이 더 적합할 수 있다.

Q. RetryButton은 무엇과 연결해야 해?
A. `refetch`, `fetchNextPage`, 수동 재요청 함수 같은 실제 retry 함수와 연결해야 한다.

Q. Retry 중 버튼을 disabled 해야 해?
A. 중복 재시도를 줄이기 위해 disabled 처리하는 것이 좋다.

---

## 6.2 SubmitButton Rules

### [개념]

SubmitButton은 Form 제출 상태를 표시하고 중복 제출을 줄이는 액션 컴포넌트다.

SubmitButton은 `isPending`, `isSubmitting`, `disabled`, loading label을 함께 처리한다.

---

### [핵심]

SubmitButton 구성 요소:

- loading
- disabled
- children
- loadingText
- type submit
- accessible label
- duplicate prevention
- form state integration

핵심 규칙:

- 제출 중 disabled 처리한다.
- 제출 중 문구를 변경한다.
- disabled 이유가 사용자에게 이해 가능해야 한다.
- Form validation disabled와 submit pending disabled를 구분한다.
- 실패 후 다시 활성화되어야 한다.
- 보안이나 중복 처리 전체를 Frontend disabled에만 의존하지 않는다.

---

### [실무]

SubmitButton 예:

```tsx
type SubmitButtonProps = {
  loading?: boolean;
  disabled?: boolean;
  children: React.ReactNode;
  loadingText?: string;
};

function SubmitButton({
  loading,
  disabled,
  children,
  loadingText = "처리 중...",
}: SubmitButtonProps) {
  return (
    <button type="submit" disabled={disabled || loading}>
      {loading ? loadingText : children}
    </button>
  );
}
```

사용 예:

```tsx
<SubmitButton loading={mutation.isPending} loadingText="등록 중...">
  리뷰 등록
</SubmitButton>
```

권장:

- Mutation 상태와 직접 연결한다.
- loadingText는 액션에 맞게 작성한다.
- 실패 후 pending 상태가 해제되는지 확인한다.
- 결제 / 삭제 같은 요청은 서버 중복 방지도 함께 설계한다.

주의:

- disabled만 있고 문구 변경이 없으면 처리 중인지 알기 어렵다.
- 별도 state와 mutation state를 중복 관리하면 꼬일 수 있다.
- Enter 제출과 버튼 클릭 중복도 고려한다.
- disabled는 보안 장치가 아니라 UX 장치다.

---

### [FAQ]

Q. SubmitButton은 왜 분리해?
A. 제출 중 disabled, loading text, 중복 제출 방지 패턴을 일관되게 적용하기 위해 분리한다.

Q. SubmitButton의 loading은 무엇과 연결해?
A. 보통 `mutation.isPending` 또는 Form의 `isSubmitting`과 연결한다.

Q. disabled와 loading은 달라?
A. 다르다. disabled는 클릭 불가 상태이고 loading은 요청 처리 중 상태다. loading은 보통 disabled를 포함한다.

Q. SubmitButton만 있으면 중복 제출이 완전히 막혀?
A. 아니다. 중요한 요청은 Backend에서도 중복 처리 방지가 필요하다.

---

# 7. Error Handling Utility Rules

## 7.1 Error Message Utility Rules

### [개념]

Error Message Utility는 API Error 객체를 사용자에게 보여줄 안전한 메시지로 변환하는 함수다.

Frontend Agent는 화면마다 error 객체를 직접 해석하지 말고 공통 utility를 우선 사용해야 한다.

---

### [핵심]

Utility 대상:

- getApiErrorMessage
- isNetworkError
- isTimeoutError
- isUnauthorizedError
- isForbiddenError
- isNotFoundError
- isConflictError
- isValidationError
- mapServerFieldErrors
- normalizeFieldErrors
- logErrorForDeveloper

핵심 규칙:

- HTTP Status Code를 기준으로 기본 메시지를 제공한다.
- Network Error와 Server Error를 구분한다.
- 401 / 403 / 404 / 409 / 422 / 500을 구분한다.
- Unknown Error fallback을 제공한다.
- 서버 원문 message를 무조건 노출하지 않는다.
- Field Error mapping은 별도 함수로 분리한다.
- 개발 로그와 사용자 메시지를 분리한다.

---

### [실무]

Utility 예:

```typescript
export function getApiErrorMessage(error: unknown): string {
  if (axios.isAxiosError(error)) {
    const status = error.response?.status;

    if (!error.response) {
      return "네트워크 연결을 확인해 주세요.";
    }

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

    if (status === 409) {
      return "이미 처리되었거나 현재 상태와 충돌한 요청입니다.";
    }

    if (status === 422) {
      return "입력 값을 다시 확인해 주세요.";
    }

    if (status >= 500) {
      return "서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.";
    }
  }

  return "요청 처리 중 문제가 발생했습니다.";
}
```

Status Helper 예:

```typescript
export function isUnauthorizedError(error: unknown): boolean {
  return axios.isAxiosError(error) && error.response?.status === 401;
}

export function isForbiddenError(error: unknown): boolean {
  return axios.isAxiosError(error) && error.response?.status === 403;
}

export function isNotFoundError(error: unknown): boolean {
  return axios.isAxiosError(error) && error.response?.status === 404;
}
```

권장:

- utility 함수는 `utils/error` 또는 `lib/error`에 분리한다.
- 화면별 도메인 메시지는 공통 utility 위에 wrapper를 둔다.
- Form Field Error mapping은 별도 함수로 분리한다.
- utility는 unknown error를 안전하게 처리해야 한다.

주의:

- `error as any`로 강제 접근을 남발하지 않는다.
- 서버 message를 항상 신뢰하지 않는다.
- utility에서 token이나 민감정보를 로그로 남기지 않는다.
- 모든 오류를 하나의 generic message로 뭉개면 UX가 나빠진다.

---

### [FAQ]

Q. Error Message Utility는 왜 필요해?
A. API Error 해석과 사용자 메시지 기준을 통일하고 중복 코드를 줄이기 위해 필요하다.

Q. getApiErrorMessage는 무엇을 해야 해?
A. HTTP Status, Network Error, Unknown Error를 안전한 사용자 메시지로 변환해야 한다.

Q. 서버 message를 utility에서 그대로 반환해도 돼?
A. 권장하지 않는다. 내부 정보가 포함될 수 있으므로 안전한 메시지로 변환해야 한다.

Q. 화면별 메시지는 어떻게 바꿔?
A. 공통 utility를 기본으로 쓰고 화면별 wrapper 함수에서 도메인 문구로 override한다.

---

## 7.2 Error Hook Rules

### [개념]

Error Hook은 Error Message Mapping, Toast, Form Error, Auth Redirect, Retry 같은 error handling 로직을 재사용하기 위한 React Hook이다.

단순한 message mapping만 필요하면 utility 함수로 충분하며, side effect가 필요할 때 hook을 고려한다.

---

### [핵심]

Error Hook 사용 상황:

- Toast Error 처리
- Auth Error Redirect
- Form Error Mapping
- Network Status Handling
- Retry State Handling
- Error Logging
- 공통 Mutation Error 처리

핵심 규칙:

- 단순 변환은 utility 함수로 처리한다.
- React state나 side effect가 필요하면 hook을 사용한다.
- hook 내부에서 서버 원문 message를 그대로 노출하지 않는다.
- hook이 너무 많은 책임을 갖지 않게 한다.
- Form Error와 Page Error는 hook에서 분기할 수 있다.
- Auth Redirect는 router 의존성을 명확히 한다.

---

### [실무]

간단한 Hook 예:

```typescript
function useApiErrorHandler() {
  function getMessage(error: unknown) {
    return getApiErrorMessage(error);
  }

  function showErrorToast(error: unknown) {
    toast.error(getApiErrorMessage(error));
  }

  return {
    getMessage,
    showErrorToast,
  };
}
```

Form Error Hook 예:

```typescript
function useFormErrorHandler() {
  const [fieldErrors, setFieldErrors] = useState<Record<string, string>>({});
  const [formError, setFormError] = useState("");

  function handleError(error: unknown) {
    if (isValidationError(error)) {
      setFieldErrors(mapServerFieldErrors(error));
      return;
    }

    setFormError(getApiErrorMessage(error));
  }

  return {
    fieldErrors,
    formError,
    handleError,
  };
}
```

권장:

- 공통 처리와 화면 특화 처리를 분리한다.
- hook은 side effect가 필요한 경우에만 사용한다.
- 여러 Form에서 반복되는 Validation Error Mapping은 hook으로 분리할 수 있다.
- Toast 처리는 hook에서 감쌀 수 있다.

주의:

- 모든 Error Handling을 하나의 거대한 hook으로 만들지 않는다.
- hook 내부에서 navigate, toast, form state를 모두 처리하면 결합도가 커진다.
- 단순 함수로 충분한 로직을 hook으로 만들 필요는 없다.
- hook 이름과 책임을 명확히 한다.

---

### [FAQ]

Q. Error Hook은 언제 필요해?
A. Error 처리 과정에서 React state, Toast, Redirect 같은 side effect가 필요할 때 유용하다.

Q. 단순 메시지 변환도 hook으로 만들어야 해?
A. 아니다. 단순 변환은 utility 함수가 더 적합하다.

Q. Form Error 처리는 hook으로 분리해도 돼?
A. 가능하다. 여러 Form에서 서버 Field Error Mapping이 반복된다면 유용하다.

Q. Error Hook이 너무 커지면 문제야?
A. 그렇다. Toast, Redirect, Form, Logging을 모두 한 hook에 넣으면 유지보수가 어려워질 수 있다.

---

# 8. Agent Review Rules

## 8.1 Frontend Agent Review Rules

### [개념]

Frontend Agent Review Rules는 Frontend Agent가 생성한 컴포넌트와 화면이 Error Handling & Loading UX 기준을 만족하는지 검수하는 기준이다.

Frontend Agent는 기능 구현만 확인하지 않고 UI State, Accessibility, Security, Query 상태 연결까지 함께 검토해야 한다.

---

### [핵심]

Frontend Agent 검수 대상:

- Loading State 존재 여부
- Error State 존재 여부
- Empty State 존재 여부
- Success Feedback 존재 여부
- Conditional Rendering Order
- TanStack Query 상태 연결
- Submit Loading
- Retry Action
- Field Error
- Global Form Error
- Route Error
- Error Boundary
- Accessibility
- Security Message
- Duplicate Request

핵심 규칙:

- Loading → Error → Empty → Success 순서를 확인한다.
- API 실패를 Empty로 숨기지 않는다.
- Error Message는 사용자용 메시지인지 확인한다.
- Retry Button이 실제 함수와 연결되는지 확인한다.
- Mutation 성공 후 Query Invalidation이 있는지 확인한다.
- Field Error가 input 근처에 표시되는지 확인한다.
- 401 / 403 / 404 UX가 분리되는지 확인한다.
- 접근성과 보안 노출 여부를 함께 확인한다.

---

### [실무]

Frontend Agent Review Flow:

```text
Component 확인
→ Query / Mutation 확인
→ Loading State 확인
→ Error State 확인
→ Empty State 확인
→ Success Feedback 확인
→ Form / Route Error 확인
→ Accessibility 확인
→ Security 확인
→ Troubleshooting 위험 확인
```

검수 질문:

```md
- 이 화면은 요청 중 무엇을 보여주는가?
- 요청 실패 시 무엇을 보여주는가?
- 데이터가 없을 때 무엇을 보여주는가?
- 성공 후 사용자가 결과를 인지하는가?
- Retry가 실제 동작하는가?
- Form Error가 수정 가능한 위치에 표시되는가?
- 서버 내부 메시지가 노출되지 않는가?
- 키보드와 스크린 리더 사용자가 상태를 이해할 수 있는가?
```

권장:

- 코드 리뷰에서 UX 상태 누락을 기능 버그로 본다.
- Loading / Error / Empty / Success 중 하나라도 빠지면 수정 대상으로 본다.
- TanStack Query 상태값과 UI 연결을 함께 검토한다.
- Mutation 성공 후 stale UI 가능성을 확인한다.

주의:

- “기능은 동작함”만으로 완료 처리하지 않는다.
- console.log만 있는 Error 처리로 통과시키지 않는다.
- Spinner만 있는 Loading으로 통과시키지 않는다.
- API Error를 Error Boundary로 처리했다고 판단하지 않는다.

---

### [FAQ]

Q. Frontend Agent는 Error Handling UX에서 무엇을 검수해야 해?
A. Loading, Error, Empty, Success 상태와 Query/Mutation 연결, 접근성, 보안 메시지를 함께 검수해야 한다.

Q. Loading / Error / Empty 중 하나가 빠지면 문제야?
A. 대부분 문제다. 사용자가 요청 상태를 이해하지 못할 수 있으므로 수정 대상이다.

Q. Retry Button은 어떻게 검수해?
A. 실제 refetch 또는 재요청 함수와 연결되어 있는지 확인해야 한다.

Q. Error Boundary가 있으면 API ErrorState 검수를 생략해도 돼?
A. 아니다. Error Boundary는 렌더링 오류용이고 API ErrorState는 별도로 필요하다.

---

## 8.2 Review Agent Checklist Rules

### [개념]

Review Agent Checklist Rules는 Review Agent가 Error Handling & Loading UX 문서를 기준으로 코드 산출물을 검수할 때 사용하는 최종 체크 기준이다.

Review Agent는 단순 문법 오류보다 사용자 상태 전달 실패, 잘못된 오류 처리, stale UI, 접근성 누락, 보안 노출을 중점적으로 확인해야 한다.

---

### [핵심]

Review Agent 핵심 검수 항목:

- UI State Completeness
- Conditional Rendering Safety
- API Error Mapping
- HTTP Status UX
- TanStack Query Status
- Mutation UX
- Form Error UX
- Route Error UX
- Error Boundary Role
- Accessibility
- Security
- Troubleshooting Risk

핵심 규칙:

- 상태 UI 누락을 Review Fail로 판단한다.
- Error와 Empty 혼동을 Review Fail로 판단한다.
- 서버 원문 오류 노출을 Critical Issue로 판단한다.
- token / password / stack trace 노출을 Critical Issue로 판단한다.
- Retry 미연결을 UX Bug로 판단한다.
- Field Error를 Toast로만 처리하면 수정 요청한다.
- 401 / 403 혼동은 수정 요청한다.
- Mutation 성공 후 invalidate 누락은 stale UI 위험으로 판단한다.

---

### [실무]

Review Agent 판정 기준:

| 심각도   | 기준                          | 예                             |
| -------- | ----------------------------- | ------------------------------ |
| Critical | 보안 정보 노출 / 앱 crash     | token 노출, stack trace 노출   |
| High     | 상태 UI 누락 / 인증 권한 오류 | ErrorState 없음, 401/403 혼동  |
| Medium   | UX 혼란 / stale UI            | Empty Flicker, invalidate 누락 |
| Low      | 문구 개선 / 일관성 개선       | message tone 불일치            |

Review Output 예:

```md
## Review Result

### Critical

- 서버 원문 error.message를 Toast로 그대로 노출하고 있음.
- token 값이 console.log에 출력될 가능성이 있음.

### High

- API 실패 시 ErrorState가 없고 EmptyState로 처리됨.
- 401과 403을 모두 Login Redirect로 처리함.

### Medium

- mutation 성공 후 reviews query invalidate가 누락됨.
- refetch 중 전체 Skeleton으로 덮여 Flicker 가능성이 있음.

### Low

- EmptyState 문구가 “데이터 없음”으로만 표시되어 다음 행동 안내가 부족함.
```

권장:

- Review Agent는 심각도별로 문제를 분류한다.
- 수정 방향을 짧고 명확히 제공한다.
- 코드 생성 Agent가 바로 수정할 수 있는 단위로 지적한다.
- 보안 노출은 항상 최우선으로 처리한다.

주의:

- 단순 취향 문제와 UX 결함을 구분한다.
- 문구 개선보다 상태 처리 누락을 우선한다.
- Critical Issue가 있으면 완료 처리하지 않는다.
- Review 결과에 불필요한 장문 설명을 넣지 않는다.

---

### [FAQ]

Q. Review Agent는 무엇을 가장 우선 검수해야 해?
A. 보안 정보 노출, 상태 UI 누락, Error/Empty 혼동, 인증/권한 오류 처리, stale UI 위험을 우선 검수해야 한다.

Q. 서버 원문 error.message 노출은 어느 정도 심각해?
A. 내부 정보나 민감정보가 포함될 수 있으므로 Critical 또는 High로 판단한다.

Q. Mutation 성공 후 invalidate 누락은 문제야?
A. 그렇다. 화면이 오래된 데이터를 보여줄 수 있으므로 stale UI 위험으로 판단한다.

Q. Review Agent는 문구도 검수해야 해?
A. 해야 한다. 다만 문구 개선보다 상태 처리 누락, 보안, 접근성 문제를 우선한다.

---

# 9. Final Implementation Checklist

## 9.1 Component Pattern Checklist

### [개념]

Component Pattern Checklist는 Error Handling & Loading UX 상태 컴포넌트가 재사용 가능하고 접근성, 보안, 상태 전환 기준을 만족하는지 검수하는 최종 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] LoadingState가 존재하는가?
- [ ] ErrorState가 존재하는가?
- [ ] EmptyState가 존재하는가?
- [ ] SuccessMessage 또는 Success Feedback 패턴이 존재하는가?
- [ ] FieldError와 FormAlert가 분리되어 있는가?
- [ ] PageError와 Resource NotFoundState가 구분되어 있는가?
- [ ] ForbiddenState 또는 ForbiddenPage가 존재하는가?
- [ ] NotFoundPage와 Resource NotFoundState가 구분되어 있는가?
- [ ] RetryButton이 실제 retry 함수와 연결되는가?
- [ ] SubmitButton이 loading / disabled / loadingText를 처리하는가?
- [ ] Skeleton이 실제 콘텐츠 구조와 유사한가?
- [ ] Error Message Utility가 존재하는가?
- [ ] Field Error Mapping Utility가 존재하는가?
- [ ] Error Hook은 필요한 책임만 가지는가?
- [ ] State Component가 서버 원문 error를 그대로 출력하지 않는가?
- [ ] State Component가 접근성 속성을 고려하는가?
```

---

### [실무]

최종 Component Review Flow:

```text
State Component 존재 확인
→ Props 설계 확인
→ 상태별 역할 분리 확인
→ Accessibility 기본값 확인
→ Security message 확인
→ Query / Mutation 연결 확인
→ Form / Route 연결 확인
→ Review Agent Checklist 적용
```

권장 구성:

```text
states/
- LoadingState
- ErrorState
- EmptyState
- SuccessMessage
- PageError
- NotFoundState
- ForbiddenState
- FallbackUI

forms/
- FieldError
- FormAlert
- SubmitButton

utils/
- getApiErrorMessage
- mapServerFieldErrors
- error status helpers
```

---

### [FAQ]

Q. Component Pattern Checklist에서 가장 중요한 것은?
A. Loading, Error, Empty, Success 상태를 분리하고 각 상태 컴포넌트가 접근성과 보안 기준을 만족하는지 확인하는 것이다.

Q. ErrorState와 EmptyState를 분리하지 않으면 왜 문제야?
A. 요청 실패와 데이터 없음은 원인과 사용자 행동이 다르기 때문에 같은 컴포넌트로 처리하면 UX 판단이 흐려진다.

Q. Error Utility는 꼭 필요해?
A. API Error가 여러 화면에서 반복된다면 강하게 권장된다. 메시지 기준과 보안 처리를 통일할 수 있다.

Q. State Component 검수에서 접근성을 봐야 해?
A. 그렇다. Loading, Error, Empty, Success 상태는 보조 기술 사용자에게도 전달되어야 한다.

---

## 9.2 Final Review Checklist

### [개념]

Final Review Checklist는 Error Handling & Loading UX 전체 구현 또는 문서를 최종 검수할 때 사용하는 통합 기준이다.

이 Checklist는 Frontend Agent, Review Agent, PM Agent가 공통으로 사용할 수 있는 RAG 검색 기준이다.

---

### [핵심]

최종 검수 항목:

```md
- [ ] Loading / Error / Empty / Success 상태가 모두 정의되어 있는가?
- [ ] 조건부 렌더링 순서가 Loading → Error → Empty → Success인가?
- [ ] Initial Loading과 Refetch Loading을 구분했는가?
- [ ] Submit Loading과 Page Loading을 구분했는가?
- [ ] API 실패를 Empty State로 숨기지 않는가?
- [ ] Error Message Mapping 기준이 존재하는가?
- [ ] Network Error와 Server Error를 구분했는가?
- [ ] 400 / 401 / 403 / 404 / 409 / 422 / 500 UX가 구분되는가?
- [ ] Field Error와 Global Form Error를 구분했는가?
- [ ] Route 404와 API Resource 404를 구분했는가?
- [ ] Error Boundary와 API Error State 역할을 구분했는가?
- [ ] TanStack Query의 isLoading / isFetching / isPending을 구분했는가?
- [ ] Query Key와 invalidate key가 일치하는가?
- [ ] Mutation 성공 후 관련 Query를 invalidate하는가?
- [ ] Retry Button이 실제 refetch와 연결되어 있는가?
- [ ] Empty State가 요청 성공 후에만 표시되는가?
- [ ] Success Feedback이 사용자에게 결과를 인지시키는가?
- [ ] Accessibility 기준을 만족하는가?
- [ ] Security 노출 위험이 없는가?
- [ ] Infinite Loading / Empty Flicker / Duplicate Request / Stale UI 가능성을 점검했는가?
```

---

### [실무]

최종 검수 흐름:

```text
화면 상태 분류
→ Loading 검수
→ Error 검수
→ Empty 검수
→ Success 검수
→ Query / Mutation 검수
→ Form / Route / Boundary 검수
→ Accessibility 검수
→ Security 검수
→ Troubleshooting 검수
→ 완료 판정
```

완료 판정 기준:

| 판정         | 기준                                                       |
| ------------ | ---------------------------------------------------------- |
| Pass         | 모든 핵심 상태와 보안 / 접근성 기준 충족                   |
| Minor Fix    | 문구, CTA, 작은 접근성 개선 필요                           |
| Major Fix    | Error / Empty 혼동, Loading 누락, Query stale 가능성       |
| Critical Fix | token, stack trace, SQL Error, 민감정보 노출 또는 앱 crash |

---

### [FAQ]

Q. Final Review에서 가장 중요한 것은?
A. 상태 구분, Error Mapping, Query/Mutation 동기화, 접근성, 보안 노출 여부를 함께 확인하는 것이다.

Q. Critical Fix 기준은 뭐야?
A. token, password, stack trace, SQL Error, 민감정보 노출 또는 앱 전체 crash 가능성이다.

Q. Major Fix 기준은 뭐야?
A. Error/Empty 혼동, Loading State 누락, Query invalidate 누락, 401/403 혼동 같은 사용자 흐름 결함이다.

Q. Minor Fix 기준은 뭐야?
A. 문구 개선, CTA 위치 조정, 작은 접근성 속성 보완처럼 핵심 흐름은 유지되는 개선 사항이다.

---

# Retrieval Queries

### [FAQ]

Q. Error Handling & Loading UX Part08은 무엇을 다뤄?
A. State Component Pattern, LoadingState, ErrorState, EmptyState, FieldError, FormAlert, RetryButton, SubmitButton, Error Utility, Agent Review 기준을 다룬다.

Q. State Component Pattern은 뭐야?
A. Loading, Error, Empty, Success 같은 화면 상태를 재사용 가능한 컴포넌트로 분리하는 기준이다.

Q. State Component Pattern의 장점은?
A. UX 일관성, 접근성 기본값, 중복 제거, Review Agent 검수 용이성이 좋아진다.

Q. ErrorState와 EmptyState를 하나로 합쳐도 돼?
A. 권장하지 않는다. 요청 실패와 데이터 없음은 의미와 사용자 행동이 다르기 때문이다.

Q. LoadingState에는 message가 꼭 필요해?
A. 권장된다. 사용자가 무엇을 기다리는지 알 수 있어야 한다.

Q. LoadingState에 Spinner만 넣어도 돼?
A. 권장하지 않는다. 텍스트나 접근 가능한 label을 함께 제공하는 것이 좋다.

Q. Auth Loading 문구는 따로 써야 해?
A. 좋다. “인증 상태를 확인 중입니다.”처럼 일반 데이터 조회와 구분하는 것이 명확하다.

Q. Skeleton Component는 언제 써?
A. 카드 목록, 상세 페이지, 테이블처럼 콘텐츠 구조가 예측 가능한 초기 로딩에 적합하다.

Q. Skeleton은 LoadingState와 같은 컴포넌트야?
A. 다르다. LoadingState는 상태 안내이고 Skeleton은 콘텐츠 자리 표시 UI다.

Q. Skeleton에 aria-hidden을 써도 돼?
A. 장식용 placeholder라면 aria-hidden 처리하고 별도 Loading Message를 제공하는 것이 좋다.

Q. Submit Button에도 Skeleton을 써?
A. 아니다. Submit Button에는 Button Loading이나 Disabled State가 적합하다.

Q. ErrorState에는 어떤 props가 필요해?
A. 기본적으로 message가 필요하고, 필요하면 description, onRetry, retrying, action을 받을 수 있다.

Q. ErrorState에 Retry Button은 항상 필요해?
A. 아니다. 재시도 가능한 오류에만 제공하는 것이 좋다.

Q. ErrorState가 Field Error도 처리해도 돼?
A. 권장하지 않는다. Field Error는 input 근처에 별도 컴포넌트로 표시하는 것이 좋다.

Q. ErrorState 메시지에 서버 원문을 넣어도 돼?
A. 권장하지 않는다. 사용자용 안전 메시지로 변환해야 한다.

Q. PageError와 ErrorState는 달라?
A. PageError는 페이지 단위 실패에 특화된 ErrorState로 볼 수 있다.

Q. Resource NotFoundState와 EmptyState는 달라?
A. 다르다. EmptyState는 목록 데이터 없음이고 Resource NotFoundState는 특정 리소스가 없는 상태다.

Q. API 404는 PageError야 Resource NotFound야?
A. endpoint 오류인지 특정 리소스 없음인지에 따라 다르다. 상세 리소스가 없으면 Resource NotFound가 적합하다.

Q. Resource NotFound에는 Retry가 필요해?
A. 보통은 목록 이동이나 메인 이동이 더 적합하다. 일시적 오류가 아니라면 Retry 효과가 낮다.

Q. EmptyState는 언제 사용해?
A. 요청이 성공했고 표시할 데이터가 없을 때 사용한다.

Q. EmptyState와 ErrorState는 왜 분리해야 해?
A. 데이터 없음과 요청 실패는 원인과 사용자 행동이 다르기 때문이다.

Q. EmptyState CTA는 항상 필요해?
A. 아니다. 사용자가 할 수 있는 의미 있는 다음 행동이 있을 때만 제공하면 된다.

Q. EmptyState 문구는 어디서 정하는 게 좋아?
A. 공통 컴포넌트 내부가 아니라 화면 문맥에서 props로 전달하는 것이 좋다.

Q. FieldError Component는 왜 필요해?
A. input 오류 표시와 접근성 연결을 일관되게 처리하기 위해 필요하다.

Q. FieldError id는 왜 필요해?
A. input의 aria-describedby와 연결해 보조 기술 사용자가 오류를 이해할 수 있게 하기 위해 필요하다.

Q. FieldError에 role alert를 써도 돼?
A. 중요한 입력 오류라면 사용할 수 있지만 너무 과도하게 중복되지 않게 해야 한다.

Q. FieldError를 Toast로 대체해도 돼?
A. 권장하지 않는다. 사용자가 어떤 input을 수정해야 하는지 알기 어렵다.

Q. FormAlert는 언제 써?
A. 로그인 실패, 제출 실패, 서버 장애처럼 Form 전체에 해당하는 메시지를 표시할 때 사용한다.

Q. FormAlert와 FieldError는 뭐가 달라?
A. FormAlert는 Form 전체 메시지이고 FieldError는 특정 input 오류 메시지다.

Q. FormAlert에 success 메시지도 넣어도 돼?
A. 가능하다. variant를 구분하고 success에는 role status를 고려한다.

Q. 로그인 실패는 FormAlert가 적합해?
A. 보통 적합하다. 계정 정보 불일치는 특정 field 하나의 문제가 아니라 Form 전체 오류로 보는 경우가 많다.

Q. RetryButton은 언제 필요해?
A. 네트워크 오류, 일시적 서버 오류, 조회 실패처럼 재시도 가능성이 있는 오류에 필요하다.

Q. RetryButton은 모든 오류에 넣어도 돼?
A. 아니다. 401, 403, 삭제된 리소스 404에는 로그인, 권한 안내, 목록 이동이 더 적합할 수 있다.

Q. RetryButton은 무엇과 연결해야 해?
A. refetch, fetchNextPage, 수동 재요청 함수 같은 실제 retry 함수와 연결해야 한다.

Q. Retry 중 버튼을 disabled 해야 해?
A. 중복 재시도를 줄이기 위해 disabled 처리하는 것이 좋다.

Q. SubmitButton은 왜 분리해?
A. 제출 중 disabled, loading text, 중복 제출 방지 패턴을 일관되게 적용하기 위해 분리한다.

Q. SubmitButton의 loading은 무엇과 연결해?
A. 보통 mutation.isPending 또는 Form의 isSubmitting과 연결한다.

Q. disabled와 loading은 달라?
A. 다르다. disabled는 클릭 불가 상태이고 loading은 요청 처리 중 상태다. loading은 보통 disabled를 포함한다.

Q. SubmitButton만 있으면 중복 제출이 완전히 막혀?
A. 아니다. 중요한 요청은 Backend에서도 중복 처리 방지가 필요하다.

Q. Error Message Utility는 왜 필요해?
A. API Error 해석과 사용자 메시지 기준을 통일하고 중복 코드를 줄이기 위해 필요하다.

Q. getApiErrorMessage는 무엇을 해야 해?
A. HTTP Status, Network Error, Unknown Error를 안전한 사용자 메시지로 변환해야 한다.

Q. 서버 message를 utility에서 그대로 반환해도 돼?
A. 권장하지 않는다. 내부 정보가 포함될 수 있으므로 안전한 메시지로 변환해야 한다.

Q. 화면별 메시지는 어떻게 바꿔?
A. 공통 utility를 기본으로 쓰고 화면별 wrapper 함수에서 도메인 문구로 override한다.

Q. Error Hook은 언제 필요해?
A. Error 처리 과정에서 React state, Toast, Redirect 같은 side effect가 필요할 때 유용하다.

Q. 단순 메시지 변환도 hook으로 만들어야 해?
A. 아니다. 단순 변환은 utility 함수가 더 적합하다.

Q. Form Error 처리는 hook으로 분리해도 돼?
A. 가능하다. 여러 Form에서 서버 Field Error Mapping이 반복된다면 유용하다.

Q. Error Hook이 너무 커지면 문제야?
A. 그렇다. Toast, Redirect, Form, Logging을 모두 한 hook에 넣으면 유지보수가 어려워질 수 있다.

Q. Frontend Agent는 Error Handling UX에서 무엇을 검수해야 해?
A. Loading, Error, Empty, Success 상태와 Query/Mutation 연결, 접근성, 보안 메시지를 함께 검수해야 한다.

Q. Loading / Error / Empty 중 하나가 빠지면 문제야?
A. 대부분 문제다. 사용자가 요청 상태를 이해하지 못할 수 있으므로 수정 대상이다.

Q. Retry Button은 어떻게 검수해?
A. 실제 refetch 또는 재요청 함수와 연결되어 있는지 확인해야 한다.

Q. Error Boundary가 있으면 API ErrorState 검수를 생략해도 돼?
A. 아니다. Error Boundary는 렌더링 오류용이고 API ErrorState는 별도로 필요하다.

Q. Review Agent는 무엇을 가장 우선 검수해야 해?
A. 보안 정보 노출, 상태 UI 누락, Error/Empty 혼동, 인증/권한 오류 처리, stale UI 위험을 우선 검수해야 한다.

Q. 서버 원문 error.message 노출은 어느 정도 심각해?
A. 내부 정보나 민감정보가 포함될 수 있으므로 Critical 또는 High로 판단한다.

Q. Mutation 성공 후 invalidate 누락은 문제야?
A. 그렇다. 화면이 오래된 데이터를 보여줄 수 있으므로 stale UI 위험으로 판단한다.

Q. Review Agent는 문구도 검수해야 해?
A. 해야 한다. 다만 문구 개선보다 상태 처리 누락, 보안, 접근성 문제를 우선한다.

Q. Component Pattern Checklist에서 가장 중요한 것은?
A. Loading, Error, Empty, Success 상태를 분리하고 각 상태 컴포넌트가 접근성과 보안 기준을 만족하는지 확인하는 것이다.

Q. Error Utility는 꼭 필요해?
A. API Error가 여러 화면에서 반복된다면 강하게 권장된다. 메시지 기준과 보안 처리를 통일할 수 있다.

Q. Final Review에서 가장 중요한 것은?
A. 상태 구분, Error Mapping, Query/Mutation 동기화, 접근성, 보안 노출 여부를 함께 확인하는 것이다.

Q. Critical Fix 기준은 뭐야?
A. token, password, stack trace, SQL Error, 민감정보 노출 또는 앱 전체 crash 가능성이다.

Q. Major Fix 기준은 뭐야?
A. Error/Empty 혼동, Loading State 누락, Query invalidate 누락, 401/403 혼동 같은 사용자 흐름 결함이다.

Q. Minor Fix 기준은 뭐야?
A. 문구 개선, CTA 위치 조정, 작은 접근성 속성 보완처럼 핵심 흐름은 유지되는 개선 사항이다.
