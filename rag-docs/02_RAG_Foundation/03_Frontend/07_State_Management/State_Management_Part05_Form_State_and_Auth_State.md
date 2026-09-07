# State Management Part05 - Form State and Auth State

---

# 1. Form State Overview

## 1.1 Form State Purpose

### [개념]

Form State는 사용자의 입력값, 검증 상태, 제출 상태, 서버 검증 오류를 관리하는 상태다.

Form State는 대부분 Form 내부에서 관리하며, 무조건 Global Store로 올리지 않는다.

Form State는 UI State, Server State, URL State와 분리해서 설계해야 한다.

---

### [핵심]

Form State 핵심 요소:

- input value
- controlled input
- uncontrolled input
- validation error
- touched
- dirty
- submit status
- server validation error
- disabled state
- reset
- field state
- form-level state
- submit payload

---

### [실무]

2026 실무 기준에서 Form State는 아래 순서로 판단한다.

```text
Form 입력값 발견
→ Form 내부에서만 필요한가?
→ 입력 중 다른 Component가 필요한가?
→ 제출 결과만 부모에 필요한가?
→ 검증 규칙이 복잡한가?
→ 서버 검증 오류가 필요한가?
→ Local State / useReducer / Form Library 선택
```

Form State 관리 원칙:

```text
간단한 Form
→ useState

상태 전환이 복잡한 Form
→ useReducer

입력 필드와 검증이 많은 Form
→ Form Library

검색 조건으로 확정되는 Form
→ submit 후 URL State

서버 제출 결과
→ useMutation

서버 검증 오류
→ Form Error State
```

주의:

- Form 입력값을 기본적으로 Global Store에 넣지 않는다.
- Form State와 Server State를 섞지 않는다.
- Form Draft State와 Applied Query State를 구분한다.
- 민감한 입력값은 persist하지 않는다.
- 제출 후 API 응답 상태는 mutation state로 관리한다.

---

### [FAQ]

Q. Form State는 뭐야?
A. 사용자의 입력값, 검증 상태, 제출 상태, 서버 검증 오류를 관리하는 상태다.

Q. Form State는 전역으로 둬야 해?
A. 대부분 아니다. Form 내부에서만 필요한 입력값은 Local State나 Form Library로 관리하는 것이 좋다.

Q. Form State와 Server State는 어떻게 달라?
A. Form State는 사용자가 입력 중인 클라이언트 상태이고 Server State는 서버가 원본으로 소유하는 API 데이터다.

---

# 2. Form State Classification

## 2.1 Form Local State

### [개념]

Form Local State는 특정 Form Component 내부에서만 필요한 입력값과 검증 상태다.

Form Component가 사라지면 함께 초기화되어도 되는 값에 적합하다.

---

### [핵심]

Form Local State 예:

- login email
- login password
- review content
- review rating
- comment input
- search draft keyword
- checkbox checked
- local validation message
- confirm password input

---

### [실무]

간단한 Form 예:

```jsx
function ReviewForm({ onSubmit }) {
  const [content, setContent] = useState("");
  const [rating, setRating] = useState(5);
  const [error, setError] = useState("");

  function handleSubmit(event) {
    event.preventDefault();

    if (!content.trim()) {
      setError("Content is required.");
      return;
    }

    onSubmit({
      content: content.trim(),
      rating,
    });
  }

  return null;
}
```

Form Local State 적합 조건:

```text
Form 내부에서만 사용
부모는 제출 결과만 필요
다른 Component와 입력 중 공유 불필요
URL 복원 불필요
새로고침 후 유지 불필요
민감정보 persist 불필요
```

주의:

- Login Form password는 Local State로 두고 persist하지 않는다.
- Review Form content는 작성 중 Form 내부에서만 관리한다.
- 제출 후 서버 상태 변경은 useMutation으로 처리한다.
- 제출 성공 후 Form reset 기준을 정한다.

---

### [FAQ]

Q. Form input 값은 Local State로 둬도 돼?
A. Form 내부에서만 필요하면 Local State가 적합하다.

Q. Login Form password를 Store에 넣어도 돼?
A. 권장하지 않는다. password 같은 민감 입력값은 Form Local State로만 관리하고 persist하지 않는다.

Q. 부모 Component가 제출 결과만 필요하면 어떻게 해?
A. Form 내부에서 입력값을 관리하고 submit 시 callback으로 결과만 전달하면 된다.

---

## 2.2 Form Shared State

### [개념]

Form Shared State는 Form 입력값이나 검증 결과를 여러 Component가 함께 읽어야 할 때 사용하는 상태다.

Form 입력 중 Preview, Step Form, 부모 Layout 제어가 필요한 경우 공통 부모로 State를 올릴 수 있다.

---

### [핵심]

Form Shared State 사용 상황:

- 입력값을 Preview Component가 사용
- Step Form 간 입력값 공유
- 부모가 submit 가능 여부를 알아야 함
- Form 입력에 따라 다른 Section 표시
- Draft 값을 여러 Child Component가 사용
- Wizard Form 전체 상태 관리

---

### [실무]

Form Shared State 예:

```jsx
function ProfileEditPage() {
  const [profileDraft, setProfileDraft] = useState({
    nickname: "",
    introduction: "",
  });

  return (
    <>
      <ProfileForm value={profileDraft} onChange={setProfileDraft} />
      <ProfilePreview profile={profileDraft} />
    </>
  );
}
```

판단 기준:

```text
Form 입력값을 다른 Component가 읽는가?
→ Shared State 검토

입력 중 Preview가 필요한가?
→ 공통 부모 State 검토

여러 Step이 같은 Draft를 공유하는가?
→ useReducer 또는 Form Library 검토

여러 Page에서 Form Draft가 이어지는가?
→ Store 검토 가능
```

주의:

- Shared State라고 바로 Global Store로 보내지 않는다.
- 가장 가까운 공통 부모를 우선 검토한다.
- Step Form이 복잡하면 useReducer 또는 Form Library가 적합할 수 있다.
- 민감한 Form Draft는 저장 범위를 제한한다.

---

### [FAQ]

Q. Form 입력값을 다른 Component가 미리보기로 써야 하면 어떻게 해?
A. 가장 가까운 공통 부모로 Form State를 올려 Shared State로 관리한다.

Q. Step Form은 무조건 Global Store가 필요해?
A. 아니다. Step이 같은 Page 내부라면 공통 부모 State나 useReducer로 충분할 수 있다.

Q. Form Shared State와 Global State 차이는?
A. Shared State는 특정 Form/Page 범위에서 공유되고 Global State는 여러 Page 또는 앱 전체에서 공유된다.

---

## 2.3 Form Global State Exception

### [개념]

Form Global State Exception은 일반적으로 Form State를 전역화하지 않지만 예외적으로 Store를 검토할 수 있는 상황이다.

여러 Page에 걸친 Wizard, 임시저장 정책, 장기 Draft가 필요한 경우 Store가 후보가 될 수 있다.

---

### [핵심]

Global Store 검토 예외:

- Multi-page Wizard Form
- Checkout Flow Draft
- Onboarding Flow
- Long Draft Editor
- Cross-page Form Step
- Temporary autosave draft
- Complex Form Workflow
- Recoverable Non-sensitive Draft

---

### [실무]

Store 검토 Flow:

```text
Form State 발견
→ 단일 Form 내부인가?
→ 여러 Step인가?
→ 여러 Page에 걸쳐 유지해야 하는가?
→ 새로고침 복원이 필요한가?
→ 민감정보가 포함되는가?
→ Store / Persistence 여부 결정
```

예시:

```text
리뷰 작성 content
→ Local State

회원가입 Step Form
→ Page Shared State 또는 useReducer

여러 Page 결제 Flow
→ Store 검토 가능
→ 민감정보 persist 금지

긴 게시글 Draft
→ autosave 정책 검토
→ localStorage 저장 시 민감정보 주의
```

주의:

- Form Global State는 예외로만 사용한다.
- password, payment data, personal sensitive data는 persist하지 않는다.
- Store reset 기준을 명확히 한다.
- submit success 후 draft cleanup을 수행한다.
- account switch / logout 시 cleanup한다.

---

### [FAQ]

Q. Form State를 Zustand에 넣어도 돼?
A. Wizard처럼 여러 Page나 Step에서 공유해야 하는 특수한 경우가 아니면 권장하지 않는다.

Q. 긴 글 작성 Draft는 Store에 둬도 돼?
A. 가능하지만 autosave, persist, cleanup, 민감정보 여부를 명확히 검토해야 한다.

Q. Form Global State를 쓰면 무엇을 조심해야 해?
A. 민감정보 저장, reset 누락, 사용자별 Draft 노출, submit 후 cleanup을 주의해야 한다.

---

# 3. Controlled and Uncontrolled Form

## 3.1 Controlled Input

### [개념]

Controlled Input은 input value를 React State가 소유하고 onChange로 변경하는 방식이다.

React State가 입력값의 Source of Truth가 된다.

---

### [핵심]

Controlled Input 요소:

- value
- onChange
- useState
- state as source of truth
- validation
- conditional UI
- submit payload
- real-time preview

---

### [실무]

예:

```jsx
function LoginForm() {
  const [email, setEmail] = useState("");

  return (
    <input value={email} onChange={(event) => setEmail(event.target.value)} />
  );
}
```

Controlled Input 적합 상황:

```text
입력값으로 실시간 검증 필요
입력값으로 UI 조건 분기 필요
Preview 필요
submit 전 payload 가공 필요
입력값을 다른 Component와 공유 필요
```

주의:

- 입력 필드가 많으면 Re-render 비용을 고려한다.
- 복잡한 Form은 Form Library를 검토한다.
- 모든 input을 무조건 Controlled로 만들 필요는 없다.
- 민감 입력값은 persist하지 않는다.

---

### [FAQ]

Q. Controlled Input이 뭐야?
A. input value를 React State가 소유하고 onChange로 변경하는 입력 방식이다.

Q. Controlled Input은 언제 써?
A. 입력값으로 검증, 조건부 UI, Preview, submit payload 가공이 필요할 때 적합하다.

Q. Controlled Input은 항상 좋은가?
A. 아니다. 입력 필드가 많고 복잡하면 Form Library나 Uncontrolled 방식도 검토할 수 있다.

---

## 3.2 Uncontrolled Input

### [개념]

Uncontrolled Input은 입력값을 DOM이 소유하고 필요할 때 ref나 FormData로 읽는 방식이다.

React State 업데이트를 줄일 수 있지만 실시간 검증과 UI 반영에는 제한이 있다.

---

### [핵심]

Uncontrolled Input 요소:

- defaultValue
- ref
- FormData
- DOM as source of truth
- submit-time read
- less state update
- simple form

---

### [실무]

예:

```jsx
function SearchForm({ onSearch }) {
  const inputRef = useRef(null);

  function handleSubmit(event) {
    event.preventDefault();
    onSearch(inputRef.current.value.trim());
  }

  return (
    <form onSubmit={handleSubmit}>
      <input ref={inputRef} defaultValue="" />
      <button type="submit">Search</button>
    </form>
  );
}
```

Uncontrolled Input 적합 상황:

```text
단순 submit만 필요
입력 중 실시간 검증 불필요
입력값으로 UI 분기 불필요
State 업데이트 최소화 필요
Form Library 내부 방식 사용
```

주의:

- 입력값을 React State와 동시에 관리하면 중복 Source of Truth가 생긴다.
- 실시간 Validation에는 Controlled Input이 더 명확하다.
- 복잡한 Form에서는 Form Library 기준을 따른다.
- defaultValue와 value를 혼동하지 않는다.

---

### [FAQ]

Q. Uncontrolled Input이 뭐야?
A. 입력값을 React State가 아니라 DOM이 소유하고 필요할 때 ref나 FormData로 읽는 방식이다.

Q. Uncontrolled Input은 언제 써?
A. 단순 submit 중심 Form이고 입력 중 실시간 검증이나 UI 반영이 필요 없을 때 사용할 수 있다.

Q. Controlled와 Uncontrolled를 섞어도 돼?
A. 같은 input에 value와 defaultValue를 혼용하면 안 된다. Source of Truth를 하나로 정해야 한다.

---

# 4. Form Validation State

## 4.1 Client Validation State

### [개념]

Client Validation State는 Frontend에서 입력값 규칙을 검사하고 사용자에게 즉시 피드백을 제공하는 상태다.

Client Validation은 UX 개선용이며 최종 검증은 Backend에서 반드시 수행해야 한다.

---

### [핵심]

Client Validation 대상:

- required
- min length
- max length
- email format
- password confirm
- number range
- date range
- file size
- file type
- local business rule

---

### [실무]

예:

```tsx
function validateReview(content: string) {
  if (!content.trim()) {
    return "Content is required.";
  }

  if (content.length > 1000) {
    return "Content must be 1000 characters or less.";
  }

  return null;
}
```

Validation Flow:

```text
Input Change
→ Local Validation
→ Error State Update
→ Submit Disabled 여부 계산
→ Submit 시 재검증
→ API Request
→ Server Validation Error 반영
```

권장 기준:

- Client Validation은 빠른 피드백을 위해 사용한다.
- Submit 시 다시 검증한다.
- Backend Validation을 최종 기준으로 둔다.
- Error Message 기준을 통일한다.
- Form Library 또는 Schema Validation을 검토할 수 있다.

---

### [FAQ]

Q. Client Validation만 있으면 충분해?
A. 아니다. Client Validation은 UX용이고 최종 검증은 Backend에서 반드시 수행해야 한다.

Q. Submit 전에 validation을 다시 해야 해?
A. 하는 것이 좋다. 입력 중 검증 상태가 오래되었거나 누락될 수 있기 때문이다.

Q. Validation Error는 어디에 둬?
A. 해당 Form 내부에서만 쓰이면 Form Local State나 Form Library 상태로 관리한다.

---

## 4.2 Server Validation Error

### [개념]

Server Validation Error는 Backend 검증 실패 결과를 Frontend Form에 반영하는 오류 상태다.

서버 검증 오류는 mutation error 또는 API Error Response에서 추출해 Field Error나 Form Error로 표시한다.

---

### [핵심]

Server Validation Error 구성:

- field error
- global form error
- error code
- error message
- API Error Response
- mutation error
- submit failure
- backend validation

---

### [실무]

서버 오류 구조 예:

```json
{
  "code": "VALIDATION_ERROR",
  "message": "Invalid request.",
  "fieldErrors": {
    "email": "Email already exists.",
    "password": "Password is too short."
  }
}
```

반영 Flow:

```text
Submit
→ useMutation 실행
→ Backend Validation 실패
→ Error Response parsing
→ fieldErrors 반영
→ Form Error UI 표시
```

권장 기준:

- Field Error와 Form-level Error를 구분한다.
- 서버 메시지를 사용자 친화적으로 변환한다.
- Error Response 구조를 API Client에서 표준화한다.
- 재입력 시 해당 field error를 제거할 수 있다.
- 서버 검증 실패를 단순 network error와 구분한다.

---

### [FAQ]

Q. Server Validation Error는 어디서 처리해?
A. useMutation onError 또는 API Error mapping 후 Form Error State에 반영한다.

Q. Field Error와 Form Error 차이는?
A. Field Error는 특정 input에 연결된 오류이고 Form Error는 전체 제출 실패나 공통 오류다.

Q. Backend Error Message를 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자에게 이해하기 쉬운 메시지로 변환하는 것이 좋다.

---

## 4.3 Derived Validation State

### [개념]

Derived Validation State는 Form 입력값으로 계산 가능한 유효성 상태다.

canSubmit, isValid 같은 값은 기존 Form State로 계산 가능하면 별도 State로 저장하지 않는다.

---

### [핵심]

Derived Validation 예:

- isValid
- canSubmit
- hasError
- isPasswordMatched
- isEmpty
- isRequiredFilled
- isDirty
- isSubmitDisabled

---

### [실무]

나쁜 예:

```tsx
const [email, setEmail] = useState("");
const [password, setPassword] = useState("");
const [canSubmit, setCanSubmit] = useState(false);
```

좋은 예:

```tsx
const canSubmit =
  email.trim().length > 0 && password.trim().length >= 8 && !mutation.isPending;
```

판단 기준:

```text
Form values로 계산 가능한가?
→ 별도 State 저장 금지

Validation Errors로 계산 가능한가?
→ 별도 State 저장 금지

계산 비용이 큰가?
→ useMemo 검토

Form Library가 제공하는가?
→ library state 사용
```

주의:

- canSubmit을 State로 저장하면 입력값과 불일치할 수 있다.
- isValid는 validation result로 계산한다.
- submit disabled는 form state와 mutation state를 함께 고려한다.

---

### [FAQ]

Q. canSubmit을 State로 저장해야 해?
A. 대부분 아니다. Form values와 error 상태로 계산 가능하면 Derived Value로 두는 것이 좋다.

Q. isValid도 Derived State야?
A. 입력값과 validation error로 계산 가능하면 Derived State다.

Q. Derived Validation State가 위험한 이유는?
A. 원본 입력값이나 오류 상태와 동기화되지 않아 잘못된 submit 가능 상태가 될 수 있다.

---

# 5. Form Submission State

## 5.1 Submit State with Mutation

### [개념]

Submit State는 Form 제출 중, 성공, 실패 상태를 표현하는 상태다.

서버 제출은 Server State 변경 요청이므로 useMutation으로 관리하는 것이 적합하다.

---

### [핵심]

Submit State 요소:

- isPending
- isSuccess
- isError
- error
- mutate
- mutateAsync
- onSuccess
- onError
- disabled submit
- duplicate submit prevention

---

### [실무]

예:

```tsx
const mutation = useMutation({
  mutationFn: createReview,
  onSuccess: () => {
    resetForm();
    queryClient.invalidateQueries({
      queryKey: ["reviews", festivalId],
    });
  },
  onError: (error) => {
    setFormError(toUserMessage(error));
  },
});

function handleSubmit(formValues) {
  mutation.mutate(formValues);
}
```

Submit Flow:

```text
Form Submit
→ Client Validation
→ useMutation mutate
→ isPending으로 버튼 disabled
→ Success 시 reset / invalidate / redirect
→ Error 시 Form Error 표시
```

권장 기준:

- 제출 중 버튼 중복 클릭을 막는다.
- mutation state를 별도 Store에 중복 저장하지 않는다.
- 성공 후 관련 Server State를 invalidate한다.
- 실패 시 Form Error로 표시한다.
- 성공 후 Form reset 기준을 정한다.

---

### [FAQ]

Q. Form submit 상태는 Store에 저장해야 해?
A. 보통 필요 없다. useMutation이 제공하는 isPending, isError, error 상태를 사용하면 된다.

Q. submit 중 버튼은 어떻게 처리해?
A. mutation.isPending 상태로 disabled 처리해 중복 제출을 막는다.

Q. submit 성공 후 목록은 어떻게 갱신해?
A. 관련 queryKey를 invalidate해서 Server State를 다시 조회한다.

---

## 5.2 Submit Success Handling

### [개념]

Submit Success Handling은 Form 제출 성공 후 UI와 Server State를 정리하는 기준이다.

성공 후 reset, redirect, toast, cache invalidation, modal close 등이 필요할 수 있다.

---

### [핵심]

성공 후 처리 후보:

- form reset
- modal close
- success toast
- redirect
- invalidateQueries
- setQueryData
- draft cleanup
- persisted draft remove
- focus reset

---

### [실무]

성공 처리 Flow:

```text
Mutation Success
→ 관련 Query invalidate 또는 cache update
→ Form reset
→ Draft cleanup
→ Success Message 표시
→ 필요 시 modal close / redirect
```

예:

```tsx
const mutation = useMutation({
  mutationFn: updateProfile,
  onSuccess: () => {
    queryClient.invalidateQueries({
      queryKey: ["userProfile"],
    });

    showToast({
      type: "success",
      message: "Profile updated.",
    });
  },
});
```

주의:

- Server State 갱신을 누락하지 않는다.
- Form Draft가 남지 않게 한다.
- modal close 전에 error 표시가 필요한지 확인한다.
- redirect 시 Query Cache 상태를 고려한다.
- 성공 메시지는 Global Toast로 처리할 수 있다.

---

### [FAQ]

Q. submit 성공 후 Form은 항상 reset해야 해?
A. 작성 Form은 reset하는 경우가 많지만 수정 Form은 최신 서버 데이터 반영이나 유지 정책을 따를 수 있다.

Q. 성공 후 toast는 어디서 관리해?
A. Global Toast가 필요한 경우 Zustand UI Store나 Redux UI Slice로 관리할 수 있다.

Q. submit 성공 후 invalidate를 빼먹으면 어떻게 돼?
A. 목록이나 상세 화면에 오래된 Server State가 남을 수 있다.

---

## 5.3 Submit Error Handling

### [개념]

Submit Error Handling은 Form 제출 실패 시 사용자에게 오류를 표시하고 재시도 가능 상태로 되돌리는 기준이다.

Error는 validation error, auth error, network error, server error로 구분해야 한다.

---

### [핵심]

Error 유형:

- client validation error
- server validation error
- auth error
- permission error
- network error
- server error
- duplicated request
- timeout

---

### [실무]

Error 처리 Flow:

```text
Mutation Error
→ Error Type 분류
→ Field Error인지 확인
→ Form-level Error인지 확인
→ Auth Error인지 확인
→ 사용자 메시지 표시
→ 재시도 가능 상태 유지
```

예:

```tsx
onError: (error) => {
  if (isValidationError(error)) {
    setFieldErrors(error.fieldErrors);
    return;
  }

  if (isAuthError(error)) {
    handleAuthError(error);
    return;
  }

  setFormError("Request failed. Please try again.");
};
```

주의:

- 모든 오류를 같은 메시지로 처리하지 않는다.
- 서버 오류를 그대로 노출하지 않는다.
- 인증 오류는 Auth Flow와 연결한다.
- validation error는 field별로 표시할 수 있다.
- 제출 실패 후 입력값을 임의로 지우지 않는다.

---

### [FAQ]

Q. submit 실패 시 입력값을 지워야 해?
A. 보통 아니다. 사용자가 수정 후 재시도할 수 있도록 입력값을 유지하는 것이 좋다.

Q. 서버 validation error는 어떻게 표시해?
A. fieldErrors는 해당 input 아래에 표시하고 form-level error는 Form 상단에 표시할 수 있다.

Q. 모든 submit error를 toast로 보여줘도 돼?
A. 가능하지만 Field Error는 input 근처에 표시하는 것이 더 적합한 경우가 많다.

---

# 6. Form Library Decision

## 6.1 Form Library Selection

### [개념]

Form Library는 복잡한 Form 입력, 검증, dirty/touched, error, submit 상태를 구조적으로 관리하는 도구다.

입력 필드와 검증 규칙이 많아지면 useState나 useReducer보다 Form Library가 적합할 수 있다.

---

### [핵심]

Form Library 검토 조건:

- field 수가 많음
- validation rule이 많음
- nested field 존재
- dynamic field array 존재
- touched / dirty 필요
- server validation 연동 필요
- submit 상태 관리 복잡
- 성능 최적화 필요
- 재사용 Form Component 필요

---

### [실무]

도구 선택 Flow:

```text
단순 Form
→ useState

상태 전환이 명확한 중간 Form
→ useReducer

입력 필드와 검증이 많은 Form
→ React Hook Form 같은 Form Library 검토

Schema 기반 검증 필요
→ Zod / Yup 같은 Schema Validation 검토
```

예시:

```text
Login Form
→ useState 가능

Review Form
→ useState 가능

Signup Form
→ Form Library 검토

Admin Complex Form
→ Form Library + Schema Validation 검토

Dynamic Survey Form
→ Form Library 권장
```

주의:

- 작은 Form에 Library를 과도하게 도입하지 않는다.
- 프로젝트 전체 Form 규칙을 통일한다.
- Server Validation Error 반영 기준을 정한다.
- Form Library State와 Global Store를 중복 사용하지 않는다.

---

### [FAQ]

Q. React Hook Form은 언제 써?
A. 입력 필드와 검증 규칙이 많고 touched, dirty, error 상태 관리가 복잡할 때 검토한다.

Q. 모든 Form에 Form Library를 써야 해?
A. 아니다. 단순 Form은 useState만으로 충분하다.

Q. Form Library를 쓰면 Global Store가 필요 없어?
A. 대부분 Form 내부 상태는 Form Library가 관리하므로 Global Store가 필요 없다.

---

## 6.2 Schema Validation Rules

### [개념]

Schema Validation은 Form 입력값 검증 규칙을 Schema로 정의하고 재사용하는 방식이다.

Zod, Yup 같은 도구를 사용해 타입과 검증 규칙을 일관되게 관리할 수 있다.

---

### [핵심]

Schema Validation 대상:

- required
- min / max length
- email
- password rule
- enum
- number range
- date range
- nested object
- array field
- cross-field validation

---

### [실무]

Schema Validation 적용 후보:

```text
회원가입 Form
프로필 수정 Form
결제 전 입력 Form
관리자 등록 Form
복잡한 검색 필터 Form
다단계 Wizard Form
```

권장 기준:

- Form Library와 Schema Resolver를 연결할 수 있다.
- Frontend Schema와 Backend Validation 규칙을 최대한 일치시킨다.
- Client Schema는 UX용이고 Backend Validation이 최종 기준이다.
- Error Message 기준을 통일한다.
- TypeScript 타입 추론과 함께 사용할 수 있다.

주의:

- Schema가 Backend 규칙과 달라지면 사용자 혼란이 생긴다.
- 비즈니스 규칙이 자주 바뀌면 Schema 관리 위치를 명확히 한다.
- 민감정보 검증 결과를 로그에 남기지 않는다.

---

### [FAQ]

Q. Schema Validation은 왜 써?
A. Form 검증 규칙을 일관되게 관리하고 재사용하기 위해 사용한다.

Q. Frontend Schema만 있으면 Backend Validation은 필요 없어?
A. 아니다. Frontend Validation은 UX용이고 Backend Validation이 최종 기준이다.

Q. Zod 같은 도구는 언제 검토해?
A. TypeScript 기반 Form에서 타입 추론과 검증 규칙을 함께 관리하고 싶을 때 검토한다.

---

# 7. Search Form and URL State

## 7.1 Search Form Draft State

### [개념]

Search Form Draft State는 사용자가 검색창에 입력 중인 임시값이다.

입력 중 Draft와 실제 검색 결과를 결정하는 Applied Query State는 분리하는 것이 좋다.

---

### [핵심]

Search State 구분:

- draftKeyword
- draftFilter
- appliedKeyword
- URL Search Params
- queryKey params
- Server State result
- page reset
- submit search

---

### [실무]

검색 흐름:

```text
사용자 입력
→ draftKeyword Local State

검색 Submit
→ URL Search Params 업데이트

URL 변경
→ queryKey params 변경

queryKey 변경
→ useQuery refetch
```

예:

```text
draftKeyword = "react"
→ 아직 서버 조회 X

Submit
→ /festivals?keyword=react&page=1

queryKey = ["festivals", { keyword: "react", page: 1 }]
→ 서버 조회
```

권장 기준:

- 입력 중 값은 Local State로 둔다.
- 실제 검색 조건은 URL State로 둔다.
- queryKey는 URL State 기준으로 만든다.
- 검색 조건 변경 시 page를 1로 초기화한다.
- 검색 결과 데이터는 Server State로 관리한다.

---

### [FAQ]

Q. 검색 input 값은 Form State야 URL State야?
A. 입력 중 값은 Form Draft State이고, 제출되어 검색 결과를 결정하는 값은 URL State가 적합하다.

Q. 검색할 때마다 Store에 keyword를 넣어야 해?
A. 보통 아니다. 공유와 새로고침 복원이 필요하면 URL State가 더 적합하다.

Q. 검색 조건이 바뀌면 page는 어떻게 해?
A. 보통 page를 1로 초기화한다.

---

## 7.2 Debounced Search State

### [개념]

Debounced Search State는 사용자가 입력을 멈춘 뒤 일정 시간이 지나면 검색 조건을 반영하는 상태다.

자동 검색 UI에서 API 요청을 줄이고 UX를 개선하는 데 사용할 수 있다.

---

### [핵심]

Debounced Search 요소:

- input draft
- debounce delay
- debounced value
- queryKey
- enabled
- request frequency
- stale result
- loading indicator

---

### [실무]

Debounced Search Flow:

```text
Input Change
→ draftKeyword 변경
→ debounce delay
→ debouncedKeyword 변경
→ queryKey 변경
→ useQuery 실행
```

판단 기준:

```text
검색 버튼이 있음
→ submit-based search

자동 완성 / 실시간 검색 필요
→ debounced search

입력마다 즉시 요청하면 부담 큼
→ debounce 적용

검색 결과 URL 공유 필요
→ debounce 결과를 URL에 반영할지 정책 결정
```

주의:

- debounce 값과 URL State 동기화 정책을 명확히 한다.
- 너무 짧은 delay는 요청을 많이 만든다.
- 너무 긴 delay는 UX가 답답해질 수 있다.
- stale result 표시와 loading 표시를 구분한다.
- abort / cancellation 전략을 고려할 수 있다.

---

### [FAQ]

Q. 검색 input이 바뀔 때마다 API 요청해도 돼?
A. 가능하지만 요청이 많아질 수 있으므로 자동 검색은 debounce를 검토하는 것이 좋다.

Q. Debounced Search에서도 queryKey가 필요해?
A. 맞다. debounced value가 실제 조회 조건이면 queryKey에 포함해야 한다.

Q. Debounced Search와 URL State를 같이 써도 돼?
A. 가능하지만 URL을 언제 업데이트할지 정책을 명확히 해야 한다.

---

# 8. Auth State Overview

## 8.1 Auth State Purpose

### [개념]

Auth State는 사용자의 인증 여부, 인증 확인 중 상태, 사용자 요약 정보, 권한 요약을 표현하는 상태다.

Auth State는 여러 Page와 Component에서 필요하므로 Context, Zustand, Redux Toolkit 같은 전역 상태 후보가 된다.

Frontend Auth State는 UX용이며 실제 보안 판단은 Backend가 담당해야 한다.

---

### [핵심]

Auth State 핵심 요소:

- authenticated
- auth loading
- user summary
- role
- permission summary
- login
- logout
- token expired
- refresh failed
- protected route
- guest route
- auth initialized
- user-specific cleanup

---

### [실무]

Auth State Flow:

```text
App Start
→ Auth Initialization
→ Token / Session 확인
→ User Summary 조회 또는 검증
→ authenticated 결정
→ Protected Route 렌더링
→ Token 만료 시 refresh
→ refresh 실패 시 logout cleanup
```

Auth State 관리 후보:

```text
단순 인증 여부 / 사용자 요약
→ Context 또는 Zustand

복잡한 인증 Lifecycle / DevTools 필요
→ Redux Toolkit

상세 user profile 조회
→ TanStack Query

실제 인증/인가 검증
→ Backend
```

주의:

- JWT 존재만으로 authenticated를 완전히 신뢰하지 않는다.
- Frontend role check는 UX용이다.
- Backend Authorization이 최종 보안 기준이다.
- logout 시 Store와 Query Cache cleanup을 고려한다.
- 민감정보를 Auth State에 과도하게 저장하지 않는다.

---

### [FAQ]

Q. Auth State는 뭐야?
A. 사용자의 인증 여부, 인증 확인 중 상태, 사용자 요약 정보, 권한 요약을 표현하는 상태다.

Q. Auth State는 전역 상태가 좋아?
A. 대부분 여러 Page와 Component에서 필요하므로 전역 상태나 Context로 관리하는 경우가 많다.

Q. Frontend Auth State만 있으면 보안이 돼?
A. 아니다. Frontend Auth State는 UX용이고 실제 보안은 Backend 인증/인가가 반드시 필요하다.

---

## 8.2 Auth State Classification

### [개념]

Auth State Classification은 인증 관련 값을 Auth State, Server State, Client UI State, Persistence State로 분리하는 작업이다.

Auth 관련 값이라고 모두 같은 Store에 넣지 않는다.

---

### [핵심]

Auth 관련 State 분류:

- authenticated → Auth Global State
- authLoading → Auth Global State
- user summary → Auth Global State
- user profile detail → Server State
- role summary → Auth Global State
- token expired flag → Auth Flow State
- login form input → Form Local State
- protected route redirect → Router State
- auth modal open → UI State
- token storage → Persistence / Security Policy

---

### [실무]

분류표:

| Auth 관련 값        | State Type            | 권장 위치                 |
| ------------------- | --------------------- | ------------------------- |
| authenticated       | Auth State            | Context / Zustand / Redux |
| authLoading         | Auth State            | Context / Zustand / Redux |
| user summary        | Auth State            | Auth Store                |
| user profile detail | Server State          | TanStack Query            |
| login email         | Form State            | LoginForm Local           |
| login password      | Form State            | LoginForm Local           |
| login error         | Form Error State      | LoginForm                 |
| access token        | Security Sensitive    | 인증 정책 기준            |
| protected redirect  | Router State          | Router                    |
| notification count  | Global / Server State | Store 또는 Query          |

---

### [FAQ]

Q. Auth 관련 값은 전부 authStore에 넣어?
A. 아니다. 로그인 Form 입력값은 Form State, user detail은 Server State, authenticated는 Auth State로 분리한다.

Q. user profile detail은 Auth State야?
A. 상세 프로필은 서버에서 조회하는 Server State로 관리하는 것이 적합할 수 있다.

Q. login password는 Auth Store에 넣어도 돼?
A. 권장하지 않는다. password는 Login Form Local State로만 관리하고 저장하지 않는다.

---

# 9. Auth Store Design

## 9.1 Auth Store Core Fields

### [개념]

Auth Store Core Fields는 Frontend에서 인증 UX를 제어하기 위해 전역으로 필요한 최소 인증 상태다.

Auth Store는 사용자 인증 요약만 유지하고 민감정보와 상세 서버 데이터를 과도하게 저장하지 않는다.

---

### [핵심]

Auth Store 핵심 필드:

- authenticated
- loading
- initialized
- user
- role
- setUser
- clearAuth
- setLoading
- setInitialized
- logout
- resetAuth

---

### [실무]

Zustand Auth Store 예:

```typescript
type AuthUser = {
  userId: number;
  nickname: string;
  role: "ROLE_USER" | "ROLE_ADMIN";
};

type AuthStore = {
  user: AuthUser | null;
  authenticated: boolean;
  loading: boolean;
  initialized: boolean;
  setUser: (user: AuthUser) => void;
  clearAuth: () => void;
  setLoading: (loading: boolean) => void;
  setInitialized: (initialized: boolean) => void;
};

export const useAuthStore = create<AuthStore>((set) => ({
  user: null,
  authenticated: false,
  loading: true,
  initialized: false,

  setUser: (user) =>
    set({
      user,
      authenticated: true,
      loading: false,
      initialized: true,
    }),

  clearAuth: () =>
    set({
      user: null,
      authenticated: false,
      loading: false,
      initialized: true,
    }),

  setLoading: (loading) => set({ loading }),
  setInitialized: (initialized) => set({ initialized }),
}));
```

권장 기준:

- Auth Store는 최소 필드만 둔다.
- user detail 전체를 저장하지 않는다.
- loading과 initialized를 구분할 수 있다.
- clearAuth는 user와 authenticated를 함께 초기화한다.
- logout 시 관련 Store reset과 Query Cache cleanup을 연결한다.

---

### [FAQ]

Q. Auth Store에 어떤 값을 넣어야 해?
A. authenticated, auth loading, initialized, user summary, role처럼 전역 UX에 필요한 최소 값만 넣는 것이 좋다.

Q. initialized는 왜 필요해?
A. 앱 시작 시 인증 확인이 끝났는지 구분해 Protected Route가 잘못 깜빡이는 문제를 줄이기 위해 사용할 수 있다.

Q. Auth Store에 user detail 전체를 넣으면 안 돼?
A. 권장하지 않는다. 상세 데이터는 Server State로 조회하고 Auth Store에는 요약 정보만 두는 것이 좋다.

---

## 9.2 Auth Action Rules

### [개념]

Auth Action은 로그인 성공, 인증 초기화, 로그아웃, 토큰 만료 같은 인증 상태 변화를 표현하는 함수다.

Auth Action은 상태 변경 의도를 명확하게 드러내야 한다.

---

### [핵심]

Auth Action 예:

- setUser
- clearAuth
- setAuthLoading
- setInitialized
- loginSuccess
- logout
- expireAuth
- refreshSuccess
- refreshFailure
- resetAuth

---

### [실무]

Action Naming 기준:

```text
로그인 성공
→ setUser 또는 loginSuccess

로그아웃 / 인증 제거
→ clearAuth 또는 logout

토큰 만료
→ expireAuth

인증 확인 중
→ setAuthLoading

초기화 완료
→ setInitialized
```

주의:

- setData 같은 모호한 이름을 피한다.
- Auth Action은 token 저장소 정책과 분리할 수 있다.
- logout action은 Store reset과 Query Cache cleanup을 호출하는 상위 service와 연결될 수 있다.
- Auth Action 내부에 너무 많은 side effect를 넣지 않는다.
- Refresh Flow는 무한 루프 방지가 필요하다.

---

### [FAQ]

Q. Auth Action 이름은 어떻게 지어?
A. setUser, clearAuth, loginSuccess, refreshFailure처럼 인증 상태 변화 의도를 드러내는 이름이 좋다.

Q. clearAuth와 logout은 같은 거야?
A. clearAuth는 Store 상태 초기화이고 logout은 token cleanup, Query Cache cleanup, redirect까지 포함할 수 있는 더 큰 흐름이다.

Q. Auth Action 안에서 API 호출해도 돼?
A. Store action에 API 호출을 넣을 수도 있지만 복잡해지면 auth service나 API layer로 분리하는 것이 좋다.

---

# 10. Auth Initialization

## 10.1 Auth Initialization Purpose

### [개념]

Auth Initialization은 App 시작 시 사용자가 이미 로그인되어 있는지 확인하고 Auth State를 초기화하는 과정이다.

인증 초기화가 끝나기 전에는 Protected Route 판단을 유보해야 한다.

---

### [핵심]

Auth Initialization 요소:

- app start
- token exists
- session check
- get current user
- refresh token check
- loading
- initialized
- authenticated
- guest state
- protected route guard

---

### [실무]

Initialization Flow:

```text
App Mount
→ Auth Loading true
→ Token / Session 존재 확인
→ Current User API 또는 Token 검증
→ 성공 시 setUser
→ 실패 시 clearAuth
→ initialized true
→ Route Rendering
```

예:

```text
initialized = false
→ 인증 확인 중
→ Protected Route render 보류

initialized = true + authenticated = true
→ Protected Page render

initialized = true + authenticated = false
→ Login redirect
```

권장 기준:

- initialized와 loading을 명확히 관리한다.
- 인증 확인 전 Protected Route redirect를 성급히 실행하지 않는다.
- token만 보고 authenticated true를 확정하지 않는다.
- Current User API 또는 검증 흐름을 고려한다.
- 실패 시 clearAuth와 cleanup을 수행한다.

---

### [FAQ]

Q. Auth Initialization은 왜 필요해?
A. 새로고침 후 사용자의 기존 로그인 상태를 확인하고 화면 접근 여부를 정확히 판단하기 위해 필요하다.

Q. initialized 없이 authenticated만 쓰면 안 돼?
A. 인증 확인 전 false로 판단되어 Protected Route가 잘못 redirect될 수 있다.

Q. App 시작 시 token이 있으면 바로 로그인 상태로 보면 돼?
A. UX상 임시 처리는 가능하지만 만료나 위조 가능성이 있어 검증 흐름이 필요하다.

---

## 10.2 Current User Query

### [개념]

Current User Query는 현재 로그인 사용자의 요약 또는 프로필 정보를 서버에서 조회해 Auth State를 확정하는 요청이다.

서버가 사용자 정보를 원본으로 소유하므로 Current User 정보는 Server State 성격도 가진다.

---

### [핵심]

Current User Query 요소:

- /me endpoint
- current user
- auth check
- user summary
- profile detail
- query enabled
- retry policy
- auth error
- cache cleanup

---

### [실무]

분리 기준:

```text
Current User Summary
→ Auth Store에 반영 가능

Current User Profile Detail
→ TanStack Query Server State

Auth Verification Result
→ authenticated / initialized 업데이트
```

Flow:

```text
Token exists
→ getCurrentUser 호출
→ 성공 시 Auth Store setUser
→ 실패 시 clearAuth
→ Query Cache cleanup
```

주의:

- Current User Query 실패 이유를 구분한다.
- 401은 Auth Flow로 연결한다.
- retry를 무분별하게 많이 하지 않는다.
- user detail 전체를 Auth Store에 저장하지 않는다.
- logout 시 current user query cache를 제거한다.

---

### [FAQ]

Q. /me API 결과는 Auth Store에 넣어도 돼?
A. 사용자 요약 정보는 Auth Store에 반영할 수 있지만 상세 프로필은 Server State로 관리하는 것이 좋다.

Q. Current User Query가 실패하면 어떻게 해?
A. 인증 실패라면 clearAuth, Query Cache cleanup, login redirect를 처리한다.

Q. Current User Query도 TanStack Query로 관리해?
A. 가능하다. 단 Auth Store와 동기화 기준을 명확히 해야 한다.

---

# 11. Protected Route and Auth UI

## 11.1 Protected Route State

### [개념]

Protected Route State는 인증이 필요한 페이지에 접근할 수 있는지 결정하는 상태다.

Frontend Protected Route는 UX 제어이며 실제 접근 제어는 Backend Authorization이 담당한다.

---

### [핵심]

Protected Route 요소:

- authenticated
- initialized
- auth loading
- required role
- redirect
- fallback loading
- forbidden page
- login page
- return URL

---

### [실무]

Protected Route 판단 Flow:

```text
initialized false
→ Loading 또는 Suspense UI

initialized true + authenticated false
→ Login Redirect

authenticated true + role 부족
→ Forbidden UI

authenticated true + role 충족
→ Protected Content Render
```

권장 기준:

- initialized 전 redirect를 막는다.
- role check는 UX용으로 사용한다.
- Backend 권한 검증을 반드시 유지한다.
- return URL을 저장해 로그인 후 복귀할 수 있다.
- loading UI와 forbidden UI를 구분한다.

주의:

- Frontend role 값은 조작 가능하다고 가정한다.
- 보안은 Backend에서 처리한다.
- 인증 오류와 권한 부족을 구분한다.
- Protected Route에서 무한 redirect를 방지한다.

---

### [FAQ]

Q. Protected Route는 보안 기능이야?
A. Frontend Protected Route는 UX 제어이며 실제 보안은 Backend 인증/인가가 담당해야 한다.

Q. initialized 전에는 Protected Route를 어떻게 처리해?
A. 인증 확인이 끝날 때까지 Loading UI를 보여주고 redirect를 유보하는 것이 좋다.

Q. role check를 Frontend에서만 해도 돼?
A. 아니다. Frontend role check는 UX용이고 Backend에서도 반드시 권한을 검증해야 한다.

---

## 11.2 Guest Route State

### [개념]

Guest Route State는 로그인하지 않은 사용자에게만 보여야 하는 페이지 접근을 제어하는 상태다.

로그인 페이지, 회원가입 페이지는 이미 인증된 사용자에게는 접근 제한하거나 홈으로 보내는 경우가 많다.

---

### [핵심]

Guest Route 대상:

- login page
- signup page
- find password page
- public auth page
- onboarding guest page

---

### [실무]

Guest Route 판단 Flow:

```text
initialized false
→ Loading UI

initialized true + authenticated true
→ Home Redirect 또는 Previous Page

initialized true + authenticated false
→ Guest Page Render
```

주의:

- 인증 확인 전 redirect를 실행하지 않는다.
- return URL과 충돌하지 않게 설계한다.
- logout 직후 Guest Route 접근 흐름을 검토한다.
- OAuth callback route는 별도 처리할 수 있다.

---

### [FAQ]

Q. Guest Route는 뭐야?
A. 로그인하지 않은 사용자에게만 보여야 하는 로그인, 회원가입 같은 페이지 접근 제어다.

Q. 로그인한 사용자가 login page에 접근하면 어떻게 해?
A. 보통 홈이나 이전 페이지로 redirect한다.

Q. Guest Route도 initialized가 필요해?
A. 필요하다. 인증 확인 전에는 로그인 여부를 확정할 수 없기 때문이다.

---

# 12. Token State and Persistence

## 12.1 Token Storage Caution

### [개념]

Token Storage는 access token, refresh token을 어디에 저장할지 결정하는 보안 설계 영역이다.

이 섹션은 보안 구현 세부를 다루는 문서가 아니라, State Management 관점에서 Token과 Auth State를 어디까지 상태로 볼지 구분하기 위한 기준이다.

Token은 민감정보이므로 State Management 편의성보다 보안 기준을 우선해야 한다.

---

### [핵심]

Token Storage 후보:

- memory
- httpOnly cookie
- secure cookie
- sessionStorage
- localStorage
- in-memory auth service
- backend session

Token Storage 위험:

- XSS
- CSRF
- token leakage
- refresh token theft
- persistent compromise
- logout cleanup 누락

---

### [실무]

판단 기준:

```text
Token 저장 필요
→ 민감정보 여부 확인
→ XSS / CSRF 위협 모델 확인
→ Backend 인증 구조 확인
→ refresh 전략 확인
→ 저장소 결정
→ logout cleanup 기준 작성
```

주의:

- localStorage는 JavaScript에서 접근 가능하다.
- XSS 발생 시 token이 노출될 수 있다.
- refresh token 저장은 특히 신중해야 한다.
- httpOnly cookie는 JavaScript 접근이 불가능하지만 CSRF 대응이 필요할 수 있다.
- 프로젝트 보안 요구사항에 따라 선택한다.
- Token을 Global Store에 과도하게 노출하지 않는다.

---

### [FAQ]

Q. localStorage에 token을 저장해도 돼?
A. 보안 위험이 있다. 프로젝트 인증 구조와 보안 요구사항에 따라 신중히 결정해야 한다.

Q. refresh token을 Frontend Store에 저장해도 돼?
A. 권장하지 않는다. refresh token은 탈취 시 위험이 크므로 저장 정책을 매우 신중히 정해야 한다.

Q. Token Storage는 State Management 문서에서 어떻게 다뤄?
A. 구현 세부보다 민감정보 저장 주의와 Auth State와의 분리 기준을 중심으로 다룬다.

---

## 12.2 Auth Persistence Rules

### [개념]

Auth Persistence는 새로고침 후 인증 관련 상태를 복원하는 전략이다.

Auth Persistence는 token storage, current user check, auth initialization과 함께 설계해야 한다.

---

### [핵심]

Persistence 대상 검토:

- authenticated flag
- user summary
- access token
- refresh token
- auth initialized
- role
- preference
- return URL

---

### [실무]

권장 Flow:

```text
새로고침
→ 저장소에 token/session 존재 확인
→ Auth Store를 무조건 신뢰하지 않음
→ Current User 또는 Token 검증
→ 성공 시 Auth State 복원
→ 실패 시 Auth State reset
```

주의:

- authenticated boolean만 persist하고 신뢰하지 않는다.
- user summary persist는 stale 가능성이 있다.
- token 저장은 보안 기준을 따른다.
- role persist는 UX 최적화용이며 최종 권한 기준이 아니다.
- Auth Persistence보다 Auth Verification이 중요하다.

---

### [FAQ]

Q. authenticated 값을 localStorage에 저장하면 돼?
A. 저장할 수는 있지만 신뢰 기준으로 쓰면 안 된다. 서버 검증이나 current user check가 필요하다.

Q. user summary를 persist해도 돼?
A. UX 최적화로 가능하지만 stale 가능성이 있으므로 서버 검증 기준을 함께 둬야 한다.

Q. Auth Persistence에서 가장 중요한 것은 뭐야?
A. 저장된 값을 맹신하지 않고 서버 검증 또는 인증 확인 흐름으로 Auth State를 확정하는 것이다.

---

# 13. Logout and Cleanup

## 13.1 Logout Flow

### [개념]

Logout Flow는 인증 상태 제거, token cleanup, Store reset, Query Cache cleanup, redirect를 포함하는 인증 종료 과정이다.

Logout은 Auth Store만 초기화하는 작업이 아니다.

---

### [핵심]

Logout 처리 요소:

- backend logout
- token cleanup
- authStore reset
- notificationStore reset
- user-specific store reset
- query cache cleanup
- persisted data cleanup
- redirect login
- websocket disconnect

---

### [실무]

Logout Flow:

```text
User Logout Click
→ Backend Logout API 호출 가능
→ Token / Session cleanup
→ Auth Store clearAuth
→ User-Specific Store reset
→ Query Cache clear / remove / invalidate
→ WebSocket disconnect
→ Login 또는 Public Page redirect
```

주의:

- Auth Store만 reset하면 이전 사용자 데이터가 남을 수 있다.
- Query Cache에 user-specific data가 남을 수 있다.
- persisted user data를 제거해야 할 수 있다.
- WebSocket 연결이 있으면 disconnect한다.
- logout 실패 시에도 local cleanup 정책을 정한다.

---

### [FAQ]

Q. logout 시 Auth Store만 초기화하면 돼?
A. 부족할 수 있다. user-specific Store, Query Cache, token, WebSocket 연결도 함께 정리해야 한다.

Q. logout 실패 시 local cleanup을 해야 해?
A. 프로젝트 정책에 따라 다르지만 사용자 입장에서는 로컬 인증 상태 제거가 필요할 수 있다.

Q. logout 후 Query Cache는 어떻게 해?
A. 사용자별 데이터가 있으면 clear, removeQueries, invalidateQueries 중 정책에 맞게 처리한다.

---

## 13.2 Account Switch Cleanup

### [개념]

Account Switch Cleanup은 한 사용자에서 다른 사용자로 전환할 때 이전 사용자 상태와 cache를 제거하는 규칙이다.

Account Switch는 logout보다 더 엄격하게 사용자별 데이터 노출을 막아야 한다.

---

### [핵심]

Cleanup 대상:

- auth user
- notification count
- favorite list
- private dashboard
- user profile cache
- my posts
- my reviews
- user-specific persisted state
- websocket subscription
- form draft

---

### [실무]

Account Switch Flow:

```text
Current User A
→ Logout 또는 Switch Start
→ User A Store / Query Cache cleanup
→ Token cleanup
→ User B Login
→ User B Auth Initialization
→ User B Query Cache 생성
```

주의:

- userId를 queryKey에 포함하면 cache 분리에 도움이 된다.
- 이전 사용자 private data가 잠깐이라도 보이지 않게 한다.
- account switch 중 loading UI를 제공한다.
- user-specific persisted data를 제거하거나 사용자별 namespace를 사용한다.
- WebSocket 구독을 재설정한다.

---

### [FAQ]

Q. 계정 전환 시 가장 중요한 것은 뭐야?
A. 이전 사용자 Store와 Query Cache가 다음 사용자에게 보이지 않도록 cleanup하는 것이다.

Q. userId를 queryKey에 넣으면 뭐가 좋아?
A. 사용자별 cache를 분리해 계정 전환 시 데이터 혼동을 줄일 수 있다.

Q. Account Switch와 logout은 같아?
A. 비슷하지만 Account Switch는 이전 사용자 데이터 노출 방지가 더 중요하다.

---

# 14. Auth Error Handling

## 14.1 Auth Error Classification

### [개념]

Auth Error Classification은 인증/인가 관련 오류를 401, 403, token expired, refresh failed 등으로 분류하는 기준이다.

Auth Error를 일반 API Error와 구분해야 적절한 UX와 보안 흐름을 만들 수 있다.

---

### [핵심]

Auth Error 유형:

- 401 Unauthorized
- 403 Forbidden
- token expired
- refresh failed
- session expired
- invalid token
- permission denied
- account disabled
- login failed

---

### [실무]

분류 기준:

```text
401 Unauthorized
→ 인증 필요 / token 만료 / invalid token 가능

403 Forbidden
→ 인증은 되었지만 권한 부족

refresh failed
→ Auth reset + login redirect

login failed
→ Login Form Error

account disabled
→ Account Status Error UI
```

주의:

- 401과 403을 구분한다.
- login 실패는 Form Error로 처리한다.
- refresh 실패는 logout cleanup과 연결한다.
- 403은 Forbidden UI 또는 접근 차단으로 처리한다.
- 모든 API Error를 Auth Error로 처리하지 않는다.

---

### [FAQ]

Q. 401과 403은 뭐가 달라?
A. 401은 인증 문제이고 403은 인증은 되었지만 권한이 부족한 경우다.

Q. login failed는 Auth Store Error야?
A. 보통 Login Form Error로 처리하고 Auth Store에는 authenticated false 상태를 유지한다.

Q. refresh failed는 어떻게 처리해?
A. clearAuth, Query Cache cleanup, login redirect를 수행한다.

---

## 14.2 Refresh Flow State

### [개념]

Refresh Flow State는 access token 만료 후 refresh token 또는 session을 통해 인증을 갱신하는 흐름의 상태다.

Refresh Flow는 무한 루프, 중복 요청, 실패 cleanup 기준이 중요하다.

---

### [핵심]

Refresh Flow 요소:

- token expired
- refresh request
- refresh success
- refresh failure
- retry original request
- request queue
- auth reset
- infinite loop prevention
- concurrent request control

---

### [실무]

Refresh Flow:

```text
API Request
→ 401 token expired
→ refresh 가능 여부 확인
→ refresh request
→ 성공 시 original request retry
→ 실패 시 clearAuth + cleanup + login redirect
```

주의:

- refresh 요청 자체가 401일 때 무한 루프를 막는다.
- 동시에 여러 요청이 401을 받을 때 중복 refresh를 제어한다.
- refresh 실패 시 user-specific cache cleanup을 수행한다.
- refresh token 저장 정책은 보안 기준을 따른다.
- refresh 중 Auth Loading UI가 필요할 수 있다.

---

### [FAQ]

Q. Access Token이 만료되면 어떻게 해?
A. refresh 흐름이 있으면 갱신을 시도하고 실패하면 Auth State reset과 login redirect를 처리한다.

Q. refresh 무한 루프는 어떻게 막아?
A. refresh 요청에는 재시도 제한을 두고 refresh 실패 시 즉시 Auth cleanup을 수행한다.

Q. 여러 API가 동시에 401이면 어떻게 해?
A. refresh request를 하나로 묶거나 queue 처리해 중복 refresh를 방지하는 전략을 검토한다.

---

# 15. Auth State and Server State Separation

## 15.1 User Summary vs User Profile

### [개념]

User Summary는 인증 UX에 필요한 최소 사용자 정보이고 User Profile은 서버가 원본으로 소유하는 상세 사용자 데이터다.

둘을 구분해야 Auth Store가 비대해지지 않는다.

---

### [핵심]

User Summary 예:

- userId
- nickname
- role
- profileImageUrl summary
- authenticated

User Profile 예:

- email
- phone
- address
- detailed settings
- activity history
- profile detail
- editable user information

---

### [실무]

분리 기준:

```text
Header / Layout / Route Guard에 필요
→ User Summary
→ Auth Store

Profile Page에서 조회 / 수정
→ User Profile
→ TanStack Query

Profile 수정 성공
→ user profile query invalidate
→ 필요한 경우 user summary도 갱신
```

주의:

- Auth Store에 모든 user detail을 넣지 않는다.
- User Profile은 Server State로 관리한다.
- Summary와 Profile이 중복되면 갱신 기준이 필요하다.
- profile image나 nickname이 Header에 필요하면 summary 업데이트 기준을 정한다.

---

### [FAQ]

Q. User Summary와 User Profile은 뭐가 달라?
A. User Summary는 인증 UX에 필요한 최소 정보이고 User Profile은 서버 원본의 상세 사용자 데이터다.

Q. Header에 nickname이 필요하면 어디에 둬?
A. Auth Store의 User Summary에 둘 수 있다.

Q. Profile Page 데이터는 Auth Store에서 가져와?
A. 상세 Profile 데이터는 TanStack Query로 조회하는 것이 적합하다.

---

## 15.2 Auth Store and Query Cache Sync

### [개념]

Auth Store and Query Cache Sync는 사용자 요약 정보와 서버 프로필 캐시가 함께 존재할 때 동기화 기준을 정하는 작업이다.

동기화 기준이 없으면 Header와 Profile Page에 다른 사용자 정보가 표시될 수 있다.

---

### [핵심]

Sync 필요 상황:

- nickname 변경
- profile image 변경
- role 변경
- account status 변경
- logout
- account switch
- current user refetch

---

### [실무]

Sync Flow:

```text
Profile Update Success
→ userProfile query invalidate
→ currentUser query invalidate
→ Auth Store user summary 업데이트 또는 refetch
→ Header UI 갱신
```

정책 후보:

```text
서버 응답에 최신 summary 포함
→ Auth Store 직접 업데이트 가능

서버 응답 불충분
→ currentUser query invalidate 후 재조회

role 변경
→ Auth Store refresh + route permission 재평가

logout
→ Auth Store reset + Query Cache cleanup
```

주의:

- Auth Store와 Query Cache 중복 필드가 있으면 갱신 기준이 필요하다.
- 가능한 중복 필드를 최소화한다.
- nickname/profile image처럼 Header에 필요한 최소 필드만 summary로 둔다.
- role 변경은 보안상 Backend 기준을 우선한다.

---

### [FAQ]

Q. Profile 수정 후 Header nickname이 안 바뀌면 뭘 확인해?
A. Auth Store user summary와 current user query가 갱신되는지 확인해야 한다.

Q. Auth Store와 Query Cache에 같은 user 정보가 있으면 안 돼?
A. 최소한으로 중복될 수 있지만 sync 기준을 명확히 해야 한다.

Q. role이 바뀌면 Frontend에서 무엇을 해야 해?
A. Auth Store를 갱신하고 Protected Route 권한 판단을 다시 수행하되, 최종 권한은 Backend 기준으로 둔다.

---

# 16. Form and Auth Anti Patterns

## 16.1 Form State in Global Store Problem

### [개념]

Form State in Global Store Problem은 단일 Form 입력값을 Zustand나 Redux 같은 Global Store에 저장하는 문제다.

Form State를 전역화하면 민감정보 노출, reset 누락, 불필요한 전역 의존성이 생긴다.

---

### [핵심]

문제:

- Store 비대화
- 입력값 reset 누락
- 민감정보 노출
- Component 재사용성 저하
- 불필요한 Re-render
- 사용자별 Draft 누출
- submit 후 stale draft 유지

잘못된 예:

- login password in authStore
- review content in globalStore
- comment input in Redux Slice
- signup field values in persisted Store
- payment form in localStorage

---

### [실무]

개선 기준:

```text
단일 Form 입력값
→ Form Local State

복잡한 Form
→ Form Library

Step Form
→ Page Shared State 또는 useReducer

여러 Page Draft
→ Store 예외 검토

민감 Form
→ persist 금지
```

Debug Flow:

```text
Store Field Review
→ Form input 여부 확인
→ Form 사용 범위 확인
→ 민감정보 여부 확인
→ Local State / Form Library로 이동
→ submit/reset cleanup 확인
```

---

### [FAQ]

Q. Form input을 Global Store에 넣으면 왜 문제야?
A. 민감정보 노출, reset 누락, Store 비대화, 불필요한 전역 의존성이 생길 수 있다.

Q. login password를 Store에 넣으면 안 돼?
A. 안 된다. password는 Form Local State로만 관리하고 저장하지 않는 것이 좋다.

Q. Form State를 Store에서 제거하려면 어떻게 해?
A. Form 내부 Local State나 Form Library로 옮기고 submit 시 필요한 payload만 전달한다.

---

## 16.2 Auth State Overtrust Problem

### [개념]

Auth State Overtrust Problem은 Frontend Auth State를 실제 보안 기준처럼 신뢰하는 문제다.

Frontend State는 사용자가 조작할 수 있으므로 Backend Authorization을 반드시 유지해야 한다.

---

### [핵심]

문제:

- Frontend role만으로 관리자 기능 허용
- JWT 존재만으로 인증 완료 처리
- 만료 token 검증 누락
- Backend 권한 검증 누락
- UI 숨김을 보안으로 착각
- localStorage auth flag 신뢰

---

### [실무]

보안 기준:

```text
Frontend Auth State
→ UX 제어
→ 메뉴 표시 / Route Guard / 화면 분기

Backend Authentication / Authorization
→ 실제 보안
→ API 접근 제어
→ role 검증
→ resource ownership 검증
```

주의:

- 버튼을 숨겨도 API 직접 호출은 가능하다고 가정한다.
- Frontend role은 표시 제어용이다.
- Backend에서 userId ownership을 검증한다.
- token은 만료와 위조 가능성을 고려한다.
- localStorage 값은 신뢰 기준이 아니다.

---

### [FAQ]

Q. Frontend에서 관리자 버튼을 숨기면 보안이 돼?
A. 아니다. UI 숨김은 UX 제어일 뿐이고 Backend에서 관리자 권한을 반드시 검증해야 한다.

Q. authenticated가 true면 API 접근을 허용해도 돼?
A. Frontend에서는 화면 제어에 사용할 수 있지만 API 접근 허용은 Backend 인증/인가 기준으로 판단해야 한다.

Q. localStorage의 role 값을 믿어도 돼?
A. 안 된다. localStorage 값은 조작 가능하므로 최종 권한 기준으로 사용할 수 없다.

---

## 16.3 Duplicate Auth State Problem

### [개념]

Duplicate Auth State Problem은 같은 인증 정보를 Auth Store, Query Cache, Component State, localStorage에 중복 저장해 불일치가 발생하는 문제다.

Auth 관련 정보는 Source of Truth와 sync 기준을 명확히 해야 한다.

---

### [핵심]

중복 예:

- authenticated flag in Store and localStorage
- user in Auth Store and Query Cache
- role in token and Store and Component
- profileImage in Auth Store and Profile Query
- notification count in Store and Query

문제:

- Header와 Profile Page 정보 불일치
- logout 후 일부 데이터 남음
- role 변경 반영 누락
- user switch 시 이전 정보 표시
- stale auth UI

---

### [실무]

Debug Flow:

```text
Auth 정보 불일치 발생
→ Auth Store 확인
→ Current User Query 확인
→ localStorage / sessionStorage 확인
→ Component Local State 확인
→ Query Cache 확인
→ Source of Truth 결정
→ sync 또는 중복 제거
```

권장 기준:

```text
authenticated
→ Auth Store

user summary
→ Auth Store

user profile detail
→ Query Cache

token/session
→ Security Storage Policy

login form input
→ Form Local State
```

---

### [FAQ]

Q. Auth 정보가 화면마다 다르면 뭘 확인해?
A. Auth Store, Query Cache, localStorage, Component State에 중복 저장된 값이 있는지 확인한다.

Q. user 정보를 Store와 Query에 둘 다 두면 안 돼?
A. 요약 정보와 상세 정보를 분리할 수는 있지만 sync 기준을 명확히 해야 한다.

Q. Duplicate Auth State를 줄이는 방법은?
A. authenticated와 user summary는 Auth Store, profile detail은 Query Cache처럼 책임을 나눈다.

---

# 17. Form and Auth Checklist

## 17.1 Form State Checklist

### [개념]

Form State Checklist는 Form 구현 전 입력값, 검증, 제출, 오류 처리, reset 기준을 검수하는 목록이다.

Form State는 Local State, useReducer, Form Library, URL State, Mutation State로 분리해서 판단한다.

---

### [핵심]

Checklist:

```md
- [ ] Form 입력값은 Form 내부에서만 필요한가?
- [ ] 입력 중 다른 Component와 공유해야 하는가?
- [ ] 제출 결과만 부모에 전달하면 되는가?
- [ ] 입력값이 URL State로 확정되어야 하는가?
- [ ] 검증 규칙이 단순한가?
- [ ] Form Library가 필요한 복잡도인가?
- [ ] Server Validation Error 처리 기준이 있는가?
- [ ] submit 상태를 useMutation으로 관리하는가?
- [ ] submit 중 중복 클릭을 막는가?
- [ ] 성공 후 reset / redirect / invalidate 기준이 있는가?
- [ ] 실패 후 입력값을 유지하는가?
- [ ] 민감정보를 persist하지 않는가?
- [ ] Derived Validation State를 중복 저장하지 않는가?
```

---

### [실무]

Form 구현 Flow:

```text
Form 요구사항 확인
→ Field 목록화
→ State 범위 결정
→ Validation 기준 작성
→ Submit Mutation 작성
→ Server Error Mapping 작성
→ Success Handling 작성
→ Reset / Cleanup 작성
```

결과 예:

```text
Login Form
→ Local State
→ useMutation
→ Login Error는 Form Error
→ 성공 시 Auth Initialization 또는 setUser

Review Form
→ Local State
→ useMutation createReview
→ 성공 시 reviews query invalidate
→ Form reset

Search Form
→ Draft Local State
→ Submit 후 URL State
→ queryKey 변경
```

---

### [FAQ]

Q. Form 구현 전 가장 먼저 확인할 것은?
A. 입력값이 Form 내부 상태인지, 공유 상태인지, URL State인지 먼저 분류해야 한다.

Q. Form State Checklist에서 가장 중요한 것은 뭐야?
A. Form 입력값을 불필요하게 Global Store에 넣지 않고 submit과 Server Error 처리를 명확히 하는 것이다.

Q. Form submit 구현 후 무엇을 확인해야 해?
A. 중복 제출 방지, 성공 후 invalidation, 실패 시 error 표시, reset 기준을 확인해야 한다.

---

## 17.2 Auth State Checklist

### [개념]

Auth State Checklist는 인증 상태 구현 전 Auth Store, 초기화, Route Guard, token storage, cleanup 기준을 검수하는 목록이다.

Auth State는 UX 상태와 보안 검증을 분리해서 판단해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] authenticated와 auth loading이 분리되었는가?
- [ ] initialized 상태가 필요한가?
- [ ] user summary와 user profile detail이 분리되었는가?
- [ ] login form input을 Auth Store에 넣지 않았는가?
- [ ] password를 저장하지 않는가?
- [ ] token storage 보안 기준이 있는가?
- [ ] Current User 검증 흐름이 있는가?
- [ ] Protected Route가 initialized를 고려하는가?
- [ ] role check를 Backend에서도 수행하는가?
- [ ] 401과 403을 구분하는가?
- [ ] refresh 실패 시 cleanup 기준이 있는가?
- [ ] logout 시 Store reset과 Query Cache cleanup이 있는가?
- [ ] account switch 시 이전 사용자 데이터가 보이지 않는가?
- [ ] Auth Store와 Query Cache sync 기준이 있는가?
```

---

### [실무]

Auth 구현 Flow:

```text
Auth 요구사항 확인
→ Auth State 분류
→ Auth Store 최소 필드 설계
→ Token Storage 정책 확인
→ Auth Initialization 작성
→ Protected Route 작성
→ Refresh Flow 작성
→ Logout Cleanup 작성
→ Query Cache Cleanup 작성
```

결과 예:

```text
authenticated / user summary
→ Auth Store

login email / password
→ Login Form Local State

current user profile
→ TanStack Query

token storage
→ 보안 정책 기준

logout
→ Auth reset + Query Cache cleanup + redirect
```

---

### [FAQ]

Q. Auth 구현 전 가장 먼저 확인할 것은?
A. Auth State, Form State, Server State, Token Storage를 분리하는 것이다.

Q. Auth State Checklist에서 가장 중요한 것은 뭐야?
A. Frontend Auth State를 보안 기준으로 과신하지 않고 Backend 인증/인가와 cleanup 기준을 유지하는 것이다.

Q. logout 구현 후 무엇을 확인해야 해?
A. Auth Store reset, user-specific Store reset, Query Cache cleanup, token cleanup, redirect가 올바른지 확인해야 한다.

---

# 18. Part05 Final Review

## 18.1 Part05 Scope Summary

### [개념]

Part05는 Form State와 Auth State의 세부 분류, 입력 상태, 검증 상태, 제출 상태, 인증 상태, 초기화, 보호 라우팅, 로그아웃 정리 기준을 다룬다.

이 문서는 Form 입력값을 무분별하게 전역화하지 않고 Auth State를 보안 기준으로 과신하지 않도록 지원한다.

---

### [핵심]

Part05 포함 범위:

- Form State Purpose
- Form Local State
- Form Shared State
- Form Global State Exception
- Controlled Input
- Uncontrolled Input
- Client Validation State
- Server Validation Error
- Derived Validation State
- Submit State with Mutation
- Submit Success Handling
- Submit Error Handling
- Form Library Decision
- Schema Validation
- Search Form and URL State
- Debounced Search State
- Auth State Purpose
- Auth State Classification
- Auth Store Core Fields
- Auth Action Rules
- Auth Initialization
- Current User Query
- Protected Route
- Guest Route
- Token Storage Caution
- Auth Persistence
- Logout Cleanup
- Account Switch Cleanup
- Auth Error Handling
- Refresh Flow State
- User Summary vs User Profile
- Auth Store and Query Cache Sync
- Form and Auth Anti Patterns
- Form and Auth Checklist

---

### [실무]

Part05 이후 문서 연결:

```text
Part01 State Classification and Ownership
→ Part02 Context API and useReducer
→ Part03 Zustand and Redux Toolkit
→ Part04 TanStack Query and Server State
→ Part05 Form State and Auth State
→ Part06 State Debugging and Anti Patterns
```

Agent 사용 기준:

```text
User Form Request
→ Part01로 State Type 판단
→ Part05로 Form State / Validation / Submit / Error 설계
→ Server Submit은 Part04 Mutation 연결
→ Global Store 필요 시 Part03 검토

User Auth Request
→ Part05로 Auth State / Init / Route / Logout 설계
→ Auth Store는 Part03 연결
→ Current User Query는 Part04 연결
→ 문제 분석은 Part06 연결
```

---

### [FAQ]

Q. Part05의 핵심 목적은 뭐야?
A. Form State와 Auth State를 Local, Global, Server, URL State와 구분해 안전하게 설계하게 하는 것이다.

Q. Part05는 보안 문서야?
A. 아니다. Auth State Management 문서이며 보안 판단은 Backend 인증/인가와 별도 보안 문서에서 최종 검토해야 한다.

Q. Part05 다음에는 무엇을 다뤄야 해?
A. State Debugging, Stale State, Duplicate State, Overused Global State 같은 Anti Pattern과 Troubleshooting을 다루는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Form State는 뭐야?
A. 사용자의 입력값, 검증 상태, 제출 상태, 서버 검증 오류를 관리하는 상태다.

Q. Form State는 전역으로 둬야 해?
A. 대부분 아니다. Form 내부에서만 필요한 입력값은 Local State나 Form Library로 관리하는 것이 좋다.

Q. Form State와 Server State는 어떻게 달라?
A. Form State는 사용자가 입력 중인 클라이언트 상태이고 Server State는 서버가 원본으로 소유하는 API 데이터다.

Q. Form input 값은 Local State로 둬도 돼?
A. Form 내부에서만 필요하면 Local State가 적합하다.

Q. Login Form password를 Store에 넣어도 돼?
A. 권장하지 않는다. password 같은 민감 입력값은 Form Local State로만 관리하고 persist하지 않는다.

Q. 부모 Component가 제출 결과만 필요하면 어떻게 해?
A. Form 내부에서 입력값을 관리하고 submit 시 callback으로 결과만 전달하면 된다.

Q. Form 입력값을 다른 Component가 미리보기로 써야 하면 어떻게 해?
A. 가장 가까운 공통 부모로 Form State를 올려 Shared State로 관리한다.

Q. Step Form은 무조건 Global Store가 필요해?
A. 아니다. Step이 같은 Page 내부라면 공통 부모 State나 useReducer로 충분할 수 있다.

Q. Form Shared State와 Global State 차이는?
A. Shared State는 특정 Form/Page 범위에서 공유되고 Global State는 여러 Page 또는 앱 전체에서 공유된다.

Q. Form State를 Zustand에 넣어도 돼?
A. Wizard처럼 여러 Page나 Step에서 공유해야 하는 특수한 경우가 아니면 권장하지 않는다.

Q. 긴 글 작성 Draft는 Store에 둬도 돼?
A. 가능하지만 autosave, persist, cleanup, 민감정보 여부를 명확히 검토해야 한다.

Q. Form Global State를 쓰면 무엇을 조심해야 해?
A. 민감정보 저장, reset 누락, 사용자별 Draft 노출, submit 후 cleanup을 주의해야 한다.

Q. Controlled Input이 뭐야?
A. input value를 React State가 소유하고 onChange로 변경하는 입력 방식이다.

Q. Controlled Input은 언제 써?
A. 입력값으로 검증, 조건부 UI, Preview, submit payload 가공이 필요할 때 적합하다.

Q. Controlled Input은 항상 좋은가?
A. 아니다. 입력 필드가 많고 복잡하면 Form Library나 Uncontrolled 방식도 검토할 수 있다.

Q. Uncontrolled Input이 뭐야?
A. 입력값을 React State가 아니라 DOM이 소유하고 필요할 때 ref나 FormData로 읽는 방식이다.

Q. Uncontrolled Input은 언제 써?
A. 단순 submit 중심 Form이고 입력 중 실시간 검증이나 UI 반영이 필요 없을 때 사용할 수 있다.

Q. Controlled와 Uncontrolled를 섞어도 돼?
A. 같은 input에 value와 defaultValue를 혼용하면 안 된다. Source of Truth를 하나로 정해야 한다.

Q. Client Validation만 있으면 충분해?
A. 아니다. Client Validation은 UX용이고 최종 검증은 Backend에서 반드시 수행해야 한다.

Q. Submit 전에 validation을 다시 해야 해?
A. 하는 것이 좋다. 입력 중 검증 상태가 오래되었거나 누락될 수 있기 때문이다.

Q. Validation Error는 어디에 둬?
A. 해당 Form 내부에서만 쓰이면 Form Local State나 Form Library 상태로 관리한다.

Q. Server Validation Error는 어디서 처리해?
A. useMutation onError 또는 API Error mapping 후 Form Error State에 반영한다.

Q. Field Error와 Form Error 차이는?
A. Field Error는 특정 input에 연결된 오류이고 Form Error는 전체 제출 실패나 공통 오류다.

Q. Backend Error Message를 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자에게 이해하기 쉬운 메시지로 변환하는 것이 좋다.

Q. canSubmit을 State로 저장해야 해?
A. 대부분 아니다. Form values와 error 상태로 계산 가능하면 Derived Value로 두는 것이 좋다.

Q. isValid도 Derived State야?
A. 입력값과 validation error로 계산 가능하면 Derived State다.

Q. Derived Validation State가 위험한 이유는?
A. 원본 입력값이나 오류 상태와 동기화되지 않아 잘못된 submit 가능 상태가 될 수 있다.

Q. Form submit 상태는 Store에 저장해야 해?
A. 보통 필요 없다. useMutation이 제공하는 isPending, isError, error 상태를 사용하면 된다.

Q. submit 중 버튼은 어떻게 처리해?
A. mutation.isPending 상태로 disabled 처리해 중복 제출을 막는다.

Q. submit 성공 후 목록은 어떻게 갱신해?
A. 관련 queryKey를 invalidate해서 Server State를 다시 조회한다.

Q. submit 성공 후 Form은 항상 reset해야 해?
A. 작성 Form은 reset하는 경우가 많지만 수정 Form은 최신 서버 데이터 반영이나 유지 정책을 따를 수 있다.

Q. 성공 후 toast는 어디서 관리해?
A. Global Toast가 필요한 경우 Zustand UI Store나 Redux UI Slice로 관리할 수 있다.

Q. submit 성공 후 invalidate를 빼먹으면 어떻게 돼?
A. 목록이나 상세 화면에 오래된 Server State가 남을 수 있다.

Q. submit 실패 시 입력값을 지워야 해?
A. 보통 아니다. 사용자가 수정 후 재시도할 수 있도록 입력값을 유지하는 것이 좋다.

Q. 서버 validation error는 어떻게 표시해?
A. fieldErrors는 해당 input 아래에 표시하고 form-level error는 Form 상단에 표시할 수 있다.

Q. 모든 submit error를 toast로 보여줘도 돼?
A. 가능하지만 Field Error는 input 근처에 표시하는 것이 더 적합한 경우가 많다.

Q. React Hook Form은 언제 써?
A. 입력 필드와 검증 규칙이 많고 touched, dirty, error 상태 관리가 복잡할 때 검토한다.

Q. 모든 Form에 Form Library를 써야 해?
A. 아니다. 단순 Form은 useState만으로 충분하다.

Q. Form Library를 쓰면 Global Store가 필요 없어?
A. 대부분 Form 내부 상태는 Form Library가 관리하므로 Global Store가 필요 없다.

Q. Schema Validation은 왜 써?
A. Form 검증 규칙을 일관되게 관리하고 재사용하기 위해 사용한다.

Q. Frontend Schema만 있으면 Backend Validation은 필요 없어?
A. 아니다. Frontend Validation은 UX용이고 Backend Validation이 최종 기준이다.

Q. Zod 같은 도구는 언제 검토해?
A. TypeScript 기반 Form에서 타입 추론과 검증 규칙을 함께 관리하고 싶을 때 검토한다.

Q. 검색 input 값은 Form State야 URL State야?
A. 입력 중 값은 Form Draft State이고, 제출되어 검색 결과를 결정하는 값은 URL State가 적합하다.

Q. 검색할 때마다 Store에 keyword를 넣어야 해?
A. 보통 아니다. 공유와 새로고침 복원이 필요하면 URL State가 더 적합하다.

Q. 검색 조건이 바뀌면 page는 어떻게 해?
A. 보통 page를 1로 초기화한다.

Q. 검색 input이 바뀔 때마다 API 요청해도 돼?
A. 가능하지만 요청이 많아질 수 있으므로 자동 검색은 debounce를 검토하는 것이 좋다.

Q. Debounced Search에서도 queryKey가 필요해?
A. 맞다. debounced value가 실제 조회 조건이면 queryKey에 포함해야 한다.

Q. Debounced Search와 URL State를 같이 써도 돼?
A. 가능하지만 URL을 언제 업데이트할지 정책을 명확히 해야 한다.

Q. Auth State는 뭐야?
A. 사용자의 인증 여부, 인증 확인 중 상태, 사용자 요약 정보, 권한 요약을 표현하는 상태다.

Q. Auth State는 전역 상태가 좋아?
A. 대부분 여러 Page와 Component에서 필요하므로 전역 상태나 Context로 관리하는 경우가 많다.

Q. Frontend Auth State만 있으면 보안이 돼?
A. 아니다. Frontend Auth State는 UX용이고 실제 보안은 Backend 인증/인가가 반드시 필요하다.

Q. Auth 관련 값은 전부 authStore에 넣어?
A. 아니다. 로그인 Form 입력값은 Form State, user detail은 Server State, authenticated는 Auth State로 분리한다.

Q. user profile detail은 Auth State야?
A. 상세 프로필은 서버에서 조회하는 Server State로 관리하는 것이 적합할 수 있다.

Q. login password는 Auth Store에 넣어도 돼?
A. 권장하지 않는다. password는 Login Form Local State로만 관리하고 저장하지 않는다.

Q. Auth Store에 어떤 값을 넣어야 해?
A. authenticated, auth loading, initialized, user summary, role처럼 전역 UX에 필요한 최소 값만 넣는 것이 좋다.

Q. initialized는 왜 필요해?
A. 앱 시작 시 인증 확인이 끝났는지 구분해 Protected Route가 잘못 깜빡이는 문제를 줄이기 위해 사용할 수 있다.

Q. Auth Store에 user detail 전체를 넣으면 안 돼?
A. 권장하지 않는다. 상세 데이터는 Server State로 조회하고 Auth Store에는 요약 정보만 두는 것이 좋다.

Q. Auth Action 이름은 어떻게 지어?
A. setUser, clearAuth, loginSuccess, refreshFailure처럼 인증 상태 변화 의도를 드러내는 이름이 좋다.

Q. clearAuth와 logout은 같은 거야?
A. clearAuth는 Store 상태 초기화이고 logout은 token cleanup, Query Cache cleanup, redirect까지 포함할 수 있는 더 큰 흐름이다.

Q. Auth Action 안에서 API 호출해도 돼?
A. Store action에 API 호출을 넣을 수도 있지만 복잡해지면 auth service나 API layer로 분리하는 것이 좋다.

Q. Auth Initialization은 왜 필요해?
A. 새로고침 후 사용자의 기존 로그인 상태를 확인하고 화면 접근 여부를 정확히 판단하기 위해 필요하다.

Q. initialized 없이 authenticated만 쓰면 안 돼?
A. 인증 확인 전 false로 판단되어 Protected Route가 잘못 redirect될 수 있다.

Q. App 시작 시 token이 있으면 바로 로그인 상태로 보면 돼?
A. UX상 임시 처리는 가능하지만 만료나 위조 가능성이 있어 검증 흐름이 필요하다.

Q. /me API 결과는 Auth Store에 넣어도 돼?
A. 사용자 요약 정보는 Auth Store에 반영할 수 있지만 상세 프로필은 Server State로 관리하는 것이 좋다.

Q. Current User Query가 실패하면 어떻게 해?
A. 인증 실패라면 clearAuth, Query Cache cleanup, login redirect를 처리한다.

Q. Current User Query도 TanStack Query로 관리해?
A. 가능하다. 단 Auth Store와 동기화 기준을 명확히 해야 한다.

Q. Protected Route는 보안 기능이야?
A. Frontend Protected Route는 UX 제어이며 실제 보안은 Backend 인증/인가가 담당해야 한다.

Q. initialized 전에는 Protected Route를 어떻게 처리해?
A. 인증 확인이 끝날 때까지 Loading UI를 보여주고 redirect를 유보하는 것이 좋다.

Q. role check를 Frontend에서만 해도 돼?
A. 아니다. Frontend role check는 UX용이고 Backend에서도 반드시 권한을 검증해야 한다.

Q. Guest Route는 뭐야?
A. 로그인하지 않은 사용자에게만 보여야 하는 로그인, 회원가입 같은 페이지 접근 제어다.

Q. 로그인한 사용자가 login page에 접근하면 어떻게 해?
A. 보통 홈이나 이전 페이지로 redirect한다.

Q. Guest Route도 initialized가 필요해?
A. 필요하다. 인증 확인 전에는 로그인 여부를 확정할 수 없기 때문이다.

Q. localStorage에 token을 저장해도 돼?
A. 보안 위험이 있다. 프로젝트 인증 구조와 보안 요구사항에 따라 신중히 결정해야 한다.

Q. refresh token을 Frontend Store에 저장해도 돼?
A. 권장하지 않는다. refresh token은 탈취 시 위험이 크므로 저장 정책을 매우 신중히 정해야 한다.

Q. Token Storage는 State Management 문서에서 어떻게 다뤄?
A. 구현 세부보다 민감정보 저장 주의와 Auth State와의 분리 기준을 중심으로 다룬다.

Q. authenticated 값을 localStorage에 저장하면 돼?
A. 저장할 수는 있지만 신뢰 기준으로 쓰면 안 된다. 서버 검증이나 current user check가 필요하다.

Q. user summary를 persist해도 돼?
A. UX 최적화로 가능하지만 stale 가능성이 있으므로 서버 검증 기준을 함께 둬야 한다.

Q. Auth Persistence에서 가장 중요한 것은 뭐야?
A. 저장된 값을 맹신하지 않고 서버 검증 또는 인증 확인 흐름으로 Auth State를 확정하는 것이다.

Q. logout 시 Auth Store만 초기화하면 돼?
A. 부족할 수 있다. user-specific Store, Query Cache, token, WebSocket 연결도 함께 정리해야 한다.

Q. logout 실패 시 local cleanup을 해야 해?
A. 프로젝트 정책에 따라 다르지만 사용자 입장에서는 로컬 인증 상태 제거가 필요할 수 있다.

Q. logout 후 Query Cache는 어떻게 해?
A. 사용자별 데이터가 있으면 clear, removeQueries, invalidateQueries 중 정책에 맞게 처리한다.

Q. 계정 전환 시 가장 중요한 것은 뭐야?
A. 이전 사용자 Store와 Query Cache가 다음 사용자에게 보이지 않도록 cleanup하는 것이다.

Q. userId를 queryKey에 넣으면 뭐가 좋아?
A. 사용자별 cache를 분리해 계정 전환 시 데이터 혼동을 줄일 수 있다.

Q. Account Switch와 logout은 같아?
A. 비슷하지만 Account Switch는 이전 사용자 데이터 노출 방지가 더 중요하다.

Q. 401과 403은 뭐가 달라?
A. 401은 인증 문제이고 403은 인증은 되었지만 권한이 부족한 경우다.

Q. login failed는 Auth Store Error야?
A. 보통 Login Form Error로 처리하고 Auth Store에는 authenticated false 상태를 유지한다.

Q. refresh failed는 어떻게 처리해?
A. clearAuth, Query Cache cleanup, login redirect를 수행한다.

Q. Access Token이 만료되면 어떻게 해?
A. refresh 흐름이 있으면 갱신을 시도하고 실패하면 Auth State reset과 login redirect를 처리한다.

Q. refresh 무한 루프는 어떻게 막아?
A. refresh 요청에는 재시도 제한을 두고 refresh 실패 시 즉시 Auth cleanup을 수행한다.

Q. 여러 API가 동시에 401이면 어떻게 해?
A. refresh request를 하나로 묶거나 queue 처리해 중복 refresh를 방지하는 전략을 검토한다.

Q. User Summary와 User Profile은 뭐가 달라?
A. User Summary는 인증 UX에 필요한 최소 정보이고 User Profile은 서버 원본의 상세 사용자 데이터다.

Q. Header에 nickname이 필요하면 어디에 둬?
A. Auth Store의 User Summary에 둘 수 있다.

Q. Profile Page 데이터는 Auth Store에서 가져와?
A. 상세 Profile 데이터는 TanStack Query로 조회하는 것이 적합하다.

Q. Profile 수정 후 Header nickname이 안 바뀌면 뭘 확인해?
A. Auth Store user summary와 current user query가 갱신되는지 확인해야 한다.

Q. Auth Store와 Query Cache에 같은 user 정보가 있으면 안 돼?
A. 최소한으로 중복될 수 있지만 sync 기준을 명확히 해야 한다.

Q. role이 바뀌면 Frontend에서 무엇을 해야 해?
A. Auth Store를 갱신하고 Protected Route 권한 판단을 다시 수행하되, 최종 권한은 Backend 기준으로 둔다.

Q. Form input을 Global Store에 넣으면 왜 문제야?
A. 민감정보 노출, reset 누락, Store 비대화, 불필요한 전역 의존성이 생길 수 있다.

Q. login password를 Store에 넣으면 안 돼?
A. 안 된다. password는 Form Local State로만 관리하고 저장하지 않는 것이 좋다.

Q. Form State를 Store에서 제거하려면 어떻게 해?
A. Form 내부 Local State나 Form Library로 옮기고 submit 시 필요한 payload만 전달한다.

Q. Frontend에서 관리자 버튼을 숨기면 보안이 돼?
A. 아니다. UI 숨김은 UX 제어일 뿐이고 Backend에서 관리자 권한을 반드시 검증해야 한다.

Q. authenticated가 true면 API 접근을 허용해도 돼?
A. Frontend에서는 화면 제어에 사용할 수 있지만 API 접근 허용은 Backend 인증/인가 기준으로 판단해야 한다.

Q. localStorage의 role 값을 믿어도 돼?
A. 안 된다. localStorage 값은 조작 가능하므로 최종 권한 기준으로 사용할 수 없다.

Q. Auth 정보가 화면마다 다르면 뭘 확인해?
A. Auth Store, Query Cache, localStorage, Component State에 중복 저장된 값이 있는지 확인한다.

Q. user 정보를 Store와 Query에 둘 다 두면 안 돼?
A. 요약 정보와 상세 정보를 분리할 수는 있지만 sync 기준을 명확히 해야 한다.

Q. Duplicate Auth State를 줄이는 방법은?
A. authenticated와 user summary는 Auth Store, profile detail은 Query Cache처럼 책임을 나눈다.

Q. Form 구현 전 가장 먼저 확인할 것은?
A. 입력값이 Form 내부 상태인지, 공유 상태인지, URL State인지 먼저 분류해야 한다.

Q. Form State Checklist에서 가장 중요한 것은 뭐야?
A. Form 입력값을 불필요하게 Global Store에 넣지 않고 submit과 Server Error 처리를 명확히 하는 것이다.

Q. Form submit 구현 후 무엇을 확인해야 해?
A. 중복 제출 방지, 성공 후 invalidation, 실패 시 error 표시, reset 기준을 확인해야 한다.

Q. Auth 구현 전 가장 먼저 확인할 것은?
A. Auth State, Form State, Server State, Token Storage를 분리하는 것이다.

Q. Auth State Checklist에서 가장 중요한 것은 뭐야?
A. Frontend Auth State를 보안 기준으로 과신하지 않고 Backend 인증/인가와 cleanup 기준을 유지하는 것이다.

Q. logout 구현 후 무엇을 확인해야 해?
A. Auth Store reset, user-specific Store reset, Query Cache cleanup, token cleanup, redirect가 올바른지 확인해야 한다.

Q. Part05의 핵심 목적은 뭐야?
A. Form State와 Auth State를 Local, Global, Server, URL State와 구분해 안전하게 설계하게 하는 것이다.

Q. Part05는 보안 문서야?
A. 아니다. Auth State Management 문서이며 보안 판단은 Backend 인증/인가와 별도 보안 문서에서 최종 검토해야 한다.

Q. Part05 다음에는 무엇을 다뤄야 해?
A. State Debugging, Stale State, Duplicate State, Overused Global State 같은 Anti Pattern과 Troubleshooting을 다루는 것이 좋다.
