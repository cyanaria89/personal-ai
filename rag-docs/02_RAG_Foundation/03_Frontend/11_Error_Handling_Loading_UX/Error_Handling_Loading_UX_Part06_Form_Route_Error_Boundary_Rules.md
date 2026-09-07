# Error Handling & Loading UX Part06 - Form, Route & Error Boundary Rules

---

# 1. Form Error UX Overview

## 1.1 Form Error UX Purpose

### [개념]

Form Error UX는 사용자가 입력한 값, 제출 요청, 서버 검증 결과에서 발생하는 오류를 Form 화면에 적절히 표시하는 기준이다.

Form Error UX는 Field Error, Global Form Error, Submit Loading, Success Feedback을 함께 설계해야 한다.

---

### [핵심]

Form Error UX 주요 대상:

- Field Error
- Global Form Error
- Client Validation Error
- Server Validation Error
- Submit Loading
- Submit Disabled State
- Validation Response Mapping
- Form Alert
- Error Focus
- Form Success Feedback
- 400 Bad Request
- 422 Validation Error
- Login Failed
- Signup Failed
- Duplicate Value Error

핵심 규칙:

- Field Error와 Global Form Error를 구분한다.
- Field Error는 input 근처에 표시한다.
- Global Form Error는 Form 상단 또는 Submit Button 근처에 표시한다.
- 서버 Validation Error는 Form State로 매핑한다.
- Submit Loading 중 중복 제출을 방지한다.
- 실패 후 입력값을 유지한다.
- 실패 후 Submit Button을 다시 활성화한다.
- 성공 후 reset / redirect / refetch 기준을 정한다.
- 오류 메시지는 사용자가 수정 가능한 문장으로 작성한다.

---

### [실무]

Form Error 처리 흐름:

```text
User Submit
→ Client Validation
→ Field Error or Submit
→ API Request
→ Submit Loading
→ Server Validation Error
  → Field Error / Global Form Error
→ API Error
  → Form Alert / Toast / Page Error
→ Success
  → Success Feedback / Reset / Redirect / Refetch
```

Form Error UI 선택 기준:

| 오류 유형            | UI 위치                         | 예                                   |
| -------------------- | ------------------------------- | ------------------------------------ |
| 이메일 형식 오류     | Field Error                     | 이메일 형식을 확인해 주세요          |
| 비밀번호 길이 오류   | Field Error                     | 비밀번호는 8자 이상이어야 합니다     |
| 비밀번호 확인 불일치 | Field Error                     | 비밀번호가 일치하지 않습니다         |
| 로그인 실패          | Global Form Error               | 이메일 또는 비밀번호를 확인해 주세요 |
| 서버 장애            | Global Form Error / Toast       | 잠시 후 다시 시도해 주세요           |
| 권한 없음            | Form Alert / Permission Message | 접근 권한이 없습니다                 |
| 중복 닉네임          | Field Error                     | 이미 사용 중인 닉네임입니다          |

---

### [FAQ]

Q. Form Error UX는 뭐야?
A. 사용자의 입력 오류와 제출 실패를 Form 화면에서 수정 가능하게 보여주는 오류 UX 기준이다.

Q. Form Error에서 가장 중요한 구분은?
A. 특정 input 문제인 Field Error와 Form 전체 문제인 Global Form Error를 구분하는 것이다.

Q. 서버 Validation Error도 Frontend에서 처리해야 해?
A. 그렇다. 서버 field errors를 Form State로 매핑해 사용자에게 수정 위치를 알려줘야 한다.

Q. 제출 실패 후 입력값은 지워야 해?
A. 보통 지우지 않는다. 사용자가 오류를 수정할 수 있도록 유지하는 것이 좋다.

---

# 2. Field Error Rules

## 2.1 Field Error Basics

### [개념]

Field Error는 특정 input 값에 직접 연결되는 오류 메시지다.

Field Error는 사용자가 어떤 값을 어떻게 수정해야 하는지 바로 알 수 있도록 해당 input 근처에 표시한다.

---

### [핵심]

Field Error 사용 상황:

- Required Error
- Email Format Error
- Password Length Error
- Password Confirm Mismatch
- Nickname Duplicate Error
- Rating Range Error
- Date Range Error
- File Type Error
- File Size Error
- Server Field Validation Error

핵심 규칙:

- input 근처에 표시한다.
- `aria-invalid`를 적용한다.
- `aria-describedby`로 input과 error message를 연결한다.
- 오류 문구는 수정 행동을 안내한다.
- 색상만으로 오류를 표시하지 않는다.
- 서버 Field Error와 Client Field Error를 통합한다.
- Submit 후 또는 touched 이후 표시 기준을 정한다.
- Field Error를 Toast로만 보여주지 않는다.

---

### [실무]

Field Error 기본 예:

```tsx
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

좋은 문구:

```text
이메일 형식을 확인해 주세요.
비밀번호는 8자 이상 입력해 주세요.
닉네임은 2자 이상 입력해 주세요.
이미 사용 중인 닉네임입니다.
종료일은 시작일 이후로 선택해 주세요.
```

나쁜 문구:

```text
오류입니다.
잘못됨.
Invalid.
입력 실패.
```

권장:

- 사용자가 수정할 수 있는 구체적인 메시지를 작성한다.
- 오류가 있는 input을 시각적으로 구분한다.
- 색상 외에 텍스트나 아이콘을 함께 사용한다.
- 첫 번째 오류 필드로 focus 이동을 고려한다.
- 서버 field name과 Frontend input name을 매핑한다.

주의:

- 모든 field error를 Form 상단에만 표시하지 않는다.
- Field Error를 Toast로만 보여주면 수정 위치를 찾기 어렵다.
- 오류 메시지 id가 중복되면 접근성 문제가 생긴다.
- Client Validation과 Server Validation 메시지가 충돌하지 않게 한다.

---

### [FAQ]

Q. Field Error는 어디에 보여줘?
A. 해당 input 근처에 보여주는 것이 좋다.

Q. Field Error를 Toast로만 보여줘도 돼?
A. 권장하지 않는다. 사용자가 어떤 필드를 수정해야 하는지 알기 어렵다.

Q. Field Error 문구는 어떻게 써야 해?
A. 사용자가 어떤 값을 어떻게 수정해야 하는지 알 수 있게 구체적으로 작성해야 한다.

Q. Field Error 접근성은 어떻게 처리해?
A. `aria-invalid`와 `aria-describedby`를 사용해 input과 오류 메시지를 연결하는 것이 좋다.

---

## 2.2 Server Field Error Mapping

### [개념]

Server Field Error Mapping은 서버 Validation Response의 field errors를 Frontend Form State에 연결하는 작업이다.

서버 field name과 Frontend input name이 다르면 오류가 표시되지 않을 수 있으므로 mapping 기준이 필요하다.

---

### [핵심]

Mapping 대상:

- Backend Validation Errors
- Field Error Object
- Error Code
- Field Name
- Form State
- Input Name
- Nested Field
- Array Field
- Global Error Fallback

핵심 규칙:

- 서버 errors key와 Frontend input name을 일치시킨다.
- key가 다르면 mapping table을 둔다.
- field에 연결할 수 없는 오류는 Global Form Error로 처리한다.
- 서버 message를 그대로 보여줄지 검토한다.
- 내부 정보가 포함된 message는 사용자 메시지로 변환한다.
- unknown field error fallback을 제공한다.

---

### [실무]

서버 응답 예:

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

Mapping 예:

```typescript
type FieldErrors = Record<string, string>;

function mapServerFieldErrors(error: unknown): FieldErrors {
  if (!axios.isAxiosError(error)) {
    return {};
  }

  const errors = error.response?.data?.errors;

  if (!errors || typeof errors !== "object") {
    return {};
  }

  return {
    email: errors.email,
    password: errors.password,
    nickname: errors.nickname,
  };
}
```

field name 변환 예:

```typescript
const fieldNameMap = {
  userEmail: "email",
  userPassword: "password",
  userNickname: "nickname",
};

function normalizeFieldErrors(serverErrors) {
  return Object.entries(serverErrors).reduce((acc, [serverField, message]) => {
    const clientField = fieldNameMap[serverField] ?? serverField;
    acc[clientField] = message;
    return acc;
  }, {});
}
```

권장:

- Backend DTO field와 Frontend input name을 가능하면 맞춘다.
- mapping 함수는 Form마다 중복 작성하지 않는다.
- field error가 없으면 global message를 표시한다.
- 서버 error response shape를 문서화한다.

주의:

- `errors.email`인데 input name이 `userEmail`이면 오류가 표시되지 않을 수 있다.
- 서버 message에 내부 정보가 포함될 수 있으므로 검토한다.
- nested field와 array field는 별도 mapping 기준이 필요하다.
- field error를 무시하고 Toast만 띄우면 Form UX가 나빠진다.

---

### [FAQ]

Q. Server Field Error Mapping은 뭐야?
A. 서버 검증 오류의 field errors를 Frontend Form State와 input 오류 메시지로 연결하는 작업이다.

Q. 서버 errors key와 input name이 다르면 어떻게 해?
A. mapping table이나 normalize 함수를 사용해 Frontend field name으로 변환해야 한다.

Q. field에 연결할 수 없는 서버 오류는 어떻게 해?
A. Global Form Error로 표시하는 것이 좋다.

Q. 서버 validation message를 그대로 써도 돼?
A. 사용자에게 안전하고 이해 가능한 메시지라면 가능하지만 내부 정보가 포함되면 변환해야 한다.

---

# 3. Global Form Error Rules

## 3.1 Global Form Error Basics

### [개념]

Global Form Error는 Form 전체에 해당하는 오류 메시지다.

특정 input 하나로 귀속하기 어려운 로그인 실패, 권한 문제, 서버 오류, 제출 실패에 사용한다.

---

### [핵심]

Global Form Error 사용 상황:

- Login Failed
- Signup Failed
- Submit Failed
- Permission Denied
- Server Unavailable
- Network Error
- Duplicate Request
- Business Rule Error
- Unknown Error
- Refresh Token Failed

핵심 규칙:

- Form 상단 또는 Submit Button 근처에 표시한다.
- Field Error와 구분한다.
- 사용자가 다음 행동을 알 수 있게 작성한다.
- 서버 내부 message를 그대로 노출하지 않는다.
- Submit Loading을 해제한다.
- 입력값은 유지한다.
- 재시도 가능성을 제공할 수 있다.
- Global Form Error도 접근성을 고려한다.

---

### [실무]

Form Alert 예:

```tsx
function FormAlert({ message }: { message?: string }) {
  if (!message) {
    return null;
  }

  return <div role="alert">{message}</div>;
}
```

Login Form 예:

```tsx
function LoginForm() {
  const [formError, setFormError] = useState("");

  async function handleLogin(values) {
    try {
      await login(values);
    } catch (error) {
      setFormError("이메일 또는 비밀번호를 확인해 주세요.");
    }
  }

  return (
    <form onSubmit={handleSubmit(handleLogin)}>
      <FormAlert message={formError} />
      <LoginFields />
      <button type="submit">로그인</button>
    </form>
  );
}
```

권장:

- 로그인 실패는 보통 Global Form Error로 처리한다.
- 서버 장애는 Form 상단 또는 Submit Button 근처에 표시한다.
- 사용자에게 다시 시도 또는 입력 확인을 안내한다.
- Submit 실패 후 버튼을 다시 활성화한다.
- Field Error와 Global Error가 동시에 존재할 수 있음을 고려한다.

주의:

- 로그인 실패를 password field error로만 표시하면 보안상 정보 추론 문제가 생길 수 있다.
- Global Error를 alert popup으로만 보여주면 사용자가 놓칠 수 있다.
- Submit Loading이 계속 유지되지 않게 한다.
- 서버 stack trace를 Form Error로 표시하지 않는다.

---

### [FAQ]

Q. Global Form Error는 뭐야?
A. Form 전체에 해당하며 특정 field 하나로 귀속하기 어려운 오류 메시지다.

Q. 로그인 실패는 Field Error야 Global Error야?
A. 이메일 형식 오류는 Field Error이고 계정 정보 불일치 같은 인증 실패는 Global Error로 처리하는 경우가 많다.

Q. Global Error는 어디에 보여줘?
A. Form 상단이나 제출 버튼 근처처럼 사용자가 쉽게 인식할 수 있는 위치에 보여준다.

Q. Global Error가 있어도 입력값은 유지해야 해?
A. 보통 유지한다. 사용자가 수정하거나 다시 제출할 수 있어야 한다.

---

## 3.2 Login Error UX

### [개념]

Login Error UX는 로그인 Form에서 발생하는 인증 실패, 입력 오류, 네트워크 오류, 세션 관련 오류를 처리하는 기준이다.

로그인 실패는 보안상 이메일 존재 여부나 비밀번호 오류 여부를 과도하게 노출하지 않는 것이 좋다.

---

### [핵심]

Login Error 유형:

- Email Format Error
- Password Required Error
- Invalid Credentials
- Account Locked
- Network Error
- Server Error
- 401 Login Failed
- Session Expired
- OAuth Login Failed

핵심 규칙:

- 이메일 형식 오류는 Field Error로 표시한다.
- 비밀번호 필수 오류는 Field Error로 표시한다.
- 계정 정보 불일치는 Global Form Error로 표시한다.
- 이메일 존재 여부를 과도하게 노출하지 않는다.
- 로그인 실패 후 입력값은 유지한다.
- 비밀번호 입력값 유지 여부는 서비스 정책에 따라 결정한다.
- Submit Loading을 해제한다.
- 반복 실패 정책은 Backend / Security 정책과 연동한다.

---

### [실무]

로그인 실패 메시지 예:

```text
이메일 또는 비밀번호를 확인해 주세요.
```

나쁜 예:

```text
존재하지 않는 이메일입니다.
비밀번호가 틀렸습니다.
DB에 사용자가 없습니다.
```

Login Form 예:

```tsx
const loginMutation = useMutation({
  mutationFn: login,
  onError: (error) => {
    if (isValidationError(error)) {
      setFieldErrors(mapServerFieldErrors(error));
      return;
    }

    setFormError("이메일 또는 비밀번호를 확인해 주세요.");
  },
});
```

권장:

- 입력 형식 오류와 인증 실패를 분리한다.
- 인증 실패는 일반적인 Global Error로 처리한다.
- 세션 만료 후 로그인 페이지로 이동한 경우 안내 메시지를 제공할 수 있다.
- OAuth 실패는 외부 로그인 실패 메시지로 구분한다.

주의:

- “이 이메일은 가입되어 있습니다 / 없습니다” 같은 계정 열거 위험 문구를 신중히 사용한다.
- 로그인 실패를 Toast로만 보여주면 사용자가 놓칠 수 있다.
- 401 Login Failed와 기존 세션 만료 401을 같은 흐름으로 처리하지 않는다.
- 반복 실패 lock 정책을 Frontend만으로 구현하지 않는다.

---

### [FAQ]

Q. 로그인 실패 메시지는 어떻게 쓰는 게 좋아?
A. 보안상 “이메일 또는 비밀번호를 확인해 주세요.”처럼 일반적인 메시지가 적합한 경우가 많다.

Q. 로그인 실패는 Field Error로 보여줘?
A. 이메일 형식 오류는 Field Error이고 계정 정보 불일치는 Global Form Error가 적합하다.

Q. 로그인 실패 후 비밀번호를 지워야 해?
A. 서비스 정책에 따라 다르다. 보안과 사용성 기준을 함께 고려해야 한다.

Q. 로그인 실패 401과 세션 만료 401은 같아?
A. 다르다. 로그인 실패는 Form Error이고 세션 만료는 Auth State 정리와 Login Redirect가 필요하다.

---

# 4. Submit Loading & Form Recovery Rules

## 4.1 Submit Loading Rules

### [개념]

Submit Loading은 사용자가 Form을 제출한 뒤 서버 처리가 끝날 때까지 표시하는 처리 중 상태다.

Submit Loading은 중복 제출 방지, 처리 중 안내, 실패 후 복구를 포함한다.

---

### [핵심]

Submit Loading 사용 상황:

- Login Submit
- Signup Submit
- Profile Update
- Review Create
- Post Create
- Password Change
- Password Reset
- Payment Submit
- File Upload Submit

핵심 규칙:

- 제출 중 Submit Button을 disabled 처리한다.
- 버튼 문구를 처리 중 상태로 변경한다.
- 중복 제출을 방지한다.
- 실패 후 다시 제출 가능하게 복구한다.
- 성공 후 reset / redirect / refetch 기준을 정한다.
- Field Error와 Global Error 표시 후 loading을 종료한다.
- 중요한 요청은 Backend 중복 방지도 필요하다.

---

### [실무]

기본 버튼 예:

```tsx
<button type="submit" disabled={mutation.isPending}>
  {mutation.isPending ? "처리 중..." : "저장"}
</button>
```

Form Submit 예:

```tsx
function ReviewForm() {
  const mutation = useMutation({
    mutationFn: createReview,
    onSuccess: () => {
      toast.success("리뷰가 등록되었습니다.");
      resetForm();
    },
    onError: (error) => {
      setFormError(getApiErrorMessage(error));
    },
  });

  return (
    <form onSubmit={handleSubmit((values) => mutation.mutate(values))}>
      <FormAlert message={formError} />
      <ReviewFields />
      <button type="submit" disabled={mutation.isPending}>
        {mutation.isPending ? "등록 중..." : "리뷰 등록"}
      </button>
    </form>
  );
}
```

권장:

- `mutation.isPending`을 Submit Loading 기준으로 사용한다.
- 버튼 문구를 “저장 중...”, “등록 중...”, “로그인 중...”처럼 변경한다.
- 실패 후 입력값을 유지한다.
- 실패 후 오류 메시지를 표시한다.
- 성공 후 필요한 query invalidate를 수행한다.

주의:

- Disabled Button만으로 중복 요청이 완전히 막히지 않는다.
- 결제 / 후원 / 삭제 같은 요청은 서버 중복 방지가 필요하다.
- 별도 `isSubmitting` state와 mutation state를 중복 관리하면 꼬일 수 있다.
- 실패 후 버튼이 계속 disabled 상태로 남으면 UX 장애다.

---

### [FAQ]

Q. Submit Loading은 왜 필요해?
A. 중복 제출을 방지하고 사용자가 처리 중임을 알 수 있게 하기 위해 필요하다.

Q. 제출 중 버튼을 disabled 해야 해?
A. 권장한다. 중복 제출을 줄이고 사용자가 처리 중임을 이해할 수 있다.

Q. 저장 실패 후 입력값은 지워야 해?
A. 보통 지우지 않는다. 사용자가 오류를 수정할 수 있도록 유지하는 것이 좋다.

Q. Submit Loading과 Page Loading은 같아?
A. 다르다. Submit Loading은 사용자 액션 처리 중이고 Page Loading은 화면 데이터 조회 상태다.

---

## 4.2 Form Recovery After Error

### [개념]

Form Recovery After Error는 제출 실패 후 사용자가 오류를 수정하고 다시 제출할 수 있게 Form 상태를 복구하는 기준이다.

Form은 실패 후에도 입력값, 오류 메시지, 버튼 상태가 사용자 행동에 맞게 유지되어야 한다.

---

### [핵심]

복구 대상:

- Input Values
- Field Errors
- Global Form Error
- Submit Button State
- Focus Position
- Touched State
- Dirty State
- Retry Submit
- Server Validation Errors

핵심 규칙:

- 실패 후 입력값을 유지한다.
- Submit Loading을 종료한다.
- Submit Button을 다시 활성화한다.
- Field Error를 수정하면 해당 오류를 제거할 수 있다.
- Global Error는 재제출 또는 입력 변경 시 초기화할 수 있다.
- 첫 오류 field로 focus 이동을 고려한다.
- 서버 검증 오류를 사용자가 수정할 수 있게 표시한다.

---

### [실무]

에러 후 복구 예:

```tsx
function handleFieldChange(name, value) {
  setValues((prev) => ({ ...prev, [name]: value }));

  if (errors[name]) {
    setErrors((prev) => ({ ...prev, [name]: undefined }));
  }

  if (formError) {
    setFormError("");
  }
}
```

첫 오류 focus 예:

```tsx
function focusFirstError(errors) {
  const firstErrorField = Object.keys(errors)[0];

  if (firstErrorField) {
    document.querySelector(`[name="${firstErrorField}"]`)?.focus();
  }
}
```

권장:

- 사용자가 field를 수정하면 관련 field error를 제거한다.
- 재제출 시 기존 global error를 초기화할 수 있다.
- 서버 에러가 반복되면 문의 또는 나중에 다시 시도 안내를 제공한다.
- 제출 실패 후 focus 위치를 적절히 유지하거나 첫 오류로 이동한다.

주의:

- 실패 후 Form 전체를 reset하면 사용자가 다시 입력해야 한다.
- 오류 수정 중에도 오래된 Global Error가 계속 남으면 혼란스럽다.
- 실패 후 pending state가 유지되면 재제출이 불가능하다.
- 자동 focus 이동은 사용자의 현재 입력을 방해하지 않게 신중히 적용한다.

---

### [FAQ]

Q. Form 제출 실패 후 무엇을 복구해야 해?
A. 입력값, 버튼 상태, 오류 메시지, focus 흐름을 사용자가 다시 제출할 수 있게 복구해야 한다.

Q. 실패 후 Form을 reset해도 돼?
A. 권장하지 않는다. 사용자가 오류를 수정할 수 있도록 입력값을 유지하는 것이 좋다.

Q. 사용자가 입력을 수정하면 에러 메시지를 지워도 돼?
A. 가능하다. 해당 field error를 제거하고 재검증 시 다시 표시할 수 있다.

Q. 첫 오류 field로 focus 이동이 필요해?
A. 필수는 아니지만 긴 Form에서는 사용자가 빠르게 수정할 수 있어 도움이 된다.

---

# 5. Route Error UX Overview

## 5.1 Route Error Purpose

### [개념]

Route Error UX는 사용자가 존재하지 않는 URL, 권한 없는 페이지, 인증이 필요한 페이지, 잘못된 route param에 접근했을 때 보여주는 화면 기준이다.

Route Error는 API Error와 구분해야 하며, React Router 구조와 Protected Route 흐름에 연결된다.

---

### [핵심]

Route Error UX 주요 대상:

- NotFoundPage
- ForbiddenPage
- Login Required Redirect
- Protected Route
- Public Only Route
- Invalid Route Param
- Resource Not Found
- Route Loader Error
- SPA Fallback Problem
- Redirect Flicker

핵심 규칙:

- Route 404와 API 404를 구분한다.
- 401 인증 필요와 403 권한 없음을 구분한다.
- Protected Route는 auth initialized 이후 판단한다.
- PublicOnlyRoute는 로그인 상태 확인 후 redirect한다.
- 잘못된 route param은 Not Found 또는 Invalid State로 처리한다.
- Route Error에도 다음 행동을 제공한다.
- SPA fallback 문제와 API 404를 구분한다.

---

### [실무]

Route Error 처리 흐름:

```text
User enters URL
→ Route Match 확인
→ Auth Required 확인
→ Auth Initialized 확인
→ Permission 확인
→ Route Param 검증
→ Page Data Fetch
→ Route UI / NotFound / Forbidden / Login Redirect
```

Route Error 구분:

| 상황                      | 처리                     |
| ------------------------- | ------------------------ |
| 존재하지 않는 URL         | NotFoundPage             |
| 로그인 필요               | Login Redirect           |
| 로그인은 됐지만 권한 없음 | ForbiddenPage            |
| 잘못된 ID 형식            | Invalid State / NotFound |
| 삭제된 리소스             | Resource Not Found       |
| API endpoint 없음         | 개발자 URL 확인          |
| SPA fallback 미설정       | 서버 routing 설정 확인   |

---

### [FAQ]

Q. Route Error UX는 뭐야?
A. 잘못된 URL, 권한 없는 페이지, 인증 필요 페이지, 잘못된 route param 접근을 처리하는 UX 기준이다.

Q. Route 404와 API 404는 달라?
A. 다르다. Route 404는 URL 매칭 실패이고 API 404는 서버 리소스나 endpoint를 찾지 못한 것이다.

Q. 401과 403 Route UX는 어떻게 달라?
A. 401은 로그인 필요 흐름이고 403은 로그인은 되었지만 권한이 없는 상태다.

Q. Route Error에도 버튼이 필요해?
A. 메인 이동, 이전 페이지 이동, 목록 이동 같은 다음 행동을 제공하는 것이 좋다.

---

# 6. Not Found Page Rules

## 6.1 Route NotFoundPage

### [개념]

NotFoundPage는 사용자가 존재하지 않는 URL에 접근했을 때 보여주는 404 페이지다.

Route NotFoundPage는 React Router의 catch-all route와 연결된다.

---

### [핵심]

NotFoundPage 구성 요소:

- 404 Title
- Friendly Message
- Home Link
- Back Button optional
- Search Action optional
- Route Fallback
- Invalid URL 안내

핵심 규칙:

- 페이지를 찾을 수 없다는 메시지를 제공한다.
- 메인 이동 또는 이전 페이지 이동 액션을 제공한다.
- 서비스 톤에 맞는 문구를 사용한다.
- API Resource 404와 구분한다.
- 잘못된 URL이라고 명확히 안내한다.
- 기술적인 route path를 과도하게 노출하지 않는다.

---

### [실무]

NotFoundPage 예:

```tsx
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

React Router 예:

```tsx
<Routes>
  <Route path="/" element={<HomePage />} />
  <Route path="/festivals" element={<FestivalListPage />} />
  <Route path="*" element={<NotFoundPage />} />
</Routes>
```

권장:

- catch-all route를 명시한다.
- NotFoundPage에 heading을 제공한다.
- 사용자가 빠져나갈 수 있는 링크를 제공한다.
- 이전 페이지 이동 버튼은 history가 있을 때만 의미가 있다.

주의:

- NotFoundPage를 API 404 처리에 무조건 사용하지 않는다.
- SPA 배포 환경에서 서버 fallback 설정이 없으면 새로고침 404가 발생할 수 있다.
- 존재하지 않는 URL을 빈 화면으로 두지 않는다.
- 사용자에게 내부 route config를 노출하지 않는다.

---

### [FAQ]

Q. NotFoundPage에는 뭘 넣어야 해?
A. 페이지를 찾을 수 없다는 안내와 메인 이동 또는 이전 페이지 이동 같은 다음 행동을 제공한다.

Q. React Router에서 NotFoundPage는 어떻게 연결해?
A. `path="*"` catch-all route를 추가해 연결할 수 있다.

Q. API 404도 NotFoundPage로 보내?
A. 상황에 따라 다르다. 상세 리소스 없음은 해당 페이지 안에서 Resource Not Found UI를 보여줄 수 있다.

Q. 새로고침했더니 서버 404가 나와?
A. SPA fallback 설정이 없을 수 있으므로 서버가 `/index.html`로 fallback하는지 확인해야 한다.

---

## 6.2 API Resource Not Found

### [개념]

API Resource Not Found는 route는 정상적으로 매칭되었지만 API가 특정 리소스를 찾지 못한 상태다.

예를 들어 `/festivals/999` 페이지는 존재하지만 festivalId 999 데이터가 삭제되었거나 존재하지 않을 수 있다.

---

### [핵심]

Resource Not Found 사용 상황:

- Deleted Resource
- Invalid ID
- Private Resource Missing
- Detail API 404
- Wrong Resource ID
- Expired Resource
- Hidden Resource

핵심 규칙:

- Route 404와 구분한다.
- 상세 화면 안에서 Resource Not Found UI를 제공할 수 있다.
- 목록 이동 또는 메인 이동 액션을 제공한다.
- 잘못된 ID parameter를 검증한다.
- 삭제된 리소스는 친절하게 안내한다.
- API endpoint 오류와 resource 없음 오류를 구분한다.

---

### [실무]

Resource Not Found 예:

```tsx
function FestivalNotFound() {
  return (
    <section>
      <h2>축제 정보를 찾을 수 없습니다.</h2>
      <p>삭제되었거나 더 이상 제공되지 않는 축제일 수 있습니다.</p>
      <Link to="/festivals">축제 목록으로 이동</Link>
    </section>
  );
}
```

상세 페이지 처리 예:

```tsx
if (isNotFoundError(error)) {
  return <FestivalNotFound />;
}

if (isError) {
  return <ErrorState message={getApiErrorMessage(error)} onRetry={refetch} />;
}
```

권장:

- 404 Resource Error를 별도로 감지한다.
- 상세 페이지 안에서 자연스럽게 안내한다.
- 목록 이동 CTA를 제공한다.
- Network 탭에서 endpoint 404인지 resource 404인지 확인한다.

주의:

- Resource Not Found를 일반 Empty State와 혼동하지 않는다.
- API endpoint path 오류를 사용자용 Not Found로 숨기지 않는다.
- 권한 때문에 숨긴 resource인지 실제 없는 resource인지 정책을 확인한다.
- 삭제된 데이터를 계속 캐시로 보여주지 않는다.

---

### [FAQ]

Q. API Resource Not Found는 뭐야?
A. 페이지 route는 존재하지만 API가 특정 리소스를 찾지 못한 상태다.

Q. 상세 페이지 데이터가 없으면 어떻게 보여줘?
A. 해당 리소스를 찾을 수 없다는 메시지와 목록으로 돌아가는 버튼을 제공하는 것이 좋다.

Q. Resource Not Found와 Empty State는 달라?
A. 다르다. Empty State는 목록 데이터 없음이고 Resource Not Found는 특정 리소스가 없는 상태다.

Q. API endpoint 404와 resource 404는 어떻게 구분해?
A. Network 탭에서 요청 URL, Backend route, response message를 확인해야 한다.

---

# 7. Forbidden Page Rules

## 7.1 ForbiddenPage UX

### [개념]

ForbiddenPage는 사용자가 인증은 되었지만 접근 권한이 없는 페이지에 접근했을 때 보여주는 403 페이지다.

ForbiddenPage는 Login Page와 다르며, 사용자를 기본적으로 로그아웃하지 않는다.

---

### [핵심]

ForbiddenPage 구성 요소:

- 403 Title
- Permission Message
- Home Link
- Previous Page Action optional
- Login State Maintained
- No Logout By Default
- Minimal Role Detail

핵심 규칙:

- 권한 없음과 로그인 필요를 구분한다.
- 사용자를 기본적으로 logout하지 않는다.
- 메인 이동 또는 이전 페이지 이동 액션을 제공한다.
- 내부 role 정책을 과도하게 노출하지 않는다.
- 인증 상태는 유지한다.
- 접근 권한이 없는 이유를 사용자 친화적으로 안내한다.

---

### [실무]

ForbiddenPage 예:

```tsx
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

403 처리 Flow:

```text
403 발생
→ Auth State 유지
→ 권한 없음 메시지 표시
→ ForbiddenPage 이동 가능
→ 이전 페이지 / 메인 이동 제공
```

권장:

- 관리자 전용 페이지 접근 시 ForbiddenPage를 보여준다.
- 소유자만 수정 가능한 기능은 버튼 숨김 또는 권한 없음 메시지로 처리한다.
- API 403 발생 시 Login Redirect가 아니라 Forbidden UX를 사용한다.
- 권한 상세 정책은 일반화된 문구로 표현한다.

주의:

- 403에서 로그아웃하지 않는다.
- 403을 401처럼 Login Redirect로 처리하지 않는다.
- “ROLE_ADMIN이 필요합니다”처럼 내부 role 이름을 그대로 노출하지 않는다.
- 권한 없는 기능을 보여줄지 숨길지 정책을 정한다.

---

### [FAQ]

Q. ForbiddenPage는 뭐야?
A. 로그인은 되었지만 해당 페이지나 기능에 접근 권한이 없을 때 보여주는 화면이다.

Q. 403이면 로그아웃해야 해?
A. 대부분 아니다. 로그인은 되어 있지만 권한이 부족한 상태이므로 권한 없음 UI를 보여주는 것이 일반적이다.

Q. 403이면 로그인 페이지로 보내야 해?
A. 보통은 권한 없음 페이지나 메시지를 보여주는 것이 더 적절하다.

Q. ForbiddenPage와 Login Page는 달라?
A. 다르다. Forbidden은 로그인은 되었지만 권한이 없는 상태이고 Login은 인증이 필요한 상태다.

---

# 8. Protected Route Rules

## 8.1 Protected Route Loading / Redirect

### [개념]

Protected Route는 로그인된 사용자만 접근할 수 있는 route를 보호하는 구조다.

Protected Route UX에서는 auth initialized 상태를 확인한 뒤 Loading, Login Redirect, Content Render를 결정해야 한다.

---

### [핵심]

Protected Route 상태:

- Auth Initializing
- Authenticated
- Unauthenticated
- Token Refreshing
- Login Redirect
- Original Location Save
- Redirect Flicker Prevention

핵심 규칙:

- auth initialized 전에는 redirect 판단을 하지 않는다.
- 인증 확인 중에는 Auth Loading을 보여준다.
- 로그인되지 않았으면 Login Page로 이동한다.
- 원래 접근하려던 위치를 저장할 수 있다.
- 로그인 후 원래 위치로 복귀할 수 있다.
- redirect loop를 방지한다.
- 401 API Error와 route guard 흐름을 연결한다.

---

### [실무]

Protected Route 예:

```tsx
function ProtectedRoute({ children }) {
  const { user, initialized } = useAuth();
  const location = useLocation();

  if (!initialized) {
    return <LoadingState message="인증 상태를 확인 중입니다." />;
  }

  if (!user) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return children;
}
```

로그인 후 복귀 예:

```tsx
const from = location.state?.from?.pathname ?? "/";

navigate(from, { replace: true });
```

권장:

- auth initialized 상태를 별도로 관리한다.
- Loading과 Redirect를 명확히 구분한다.
- Protected Route 내부에서 사용자별 query는 auth 확인 후 실행한다.
- 로그인 후 복귀 경로를 지원할 수 있다.

주의:

- initialized 없이 `!user`만 보고 redirect하면 로그인 페이지가 깜빡일 수 있다.
- token refresh 중 redirect하면 UX가 불안정해진다.
- 로그인 페이지 자체가 ProtectedRoute에 걸리면 redirect loop가 생길 수 있다.
- auth state와 server session state 불일치를 확인한다.

---

### [FAQ]

Q. Protected Route에서 왜 auth initialized가 필요해?
A. 인증 상태 확인 전 user가 null일 수 있으므로 잘못된 redirect와 flicker를 막기 위해 필요하다.

Q. 로그인 페이지가 잠깐 보였다가 메인으로 가?
A. auth initialized 전에 redirect 판단이 실행되었을 수 있다.

Q. 로그인 후 원래 페이지로 돌아가려면?
A. Login Redirect 시 location state에 from 경로를 저장하고 로그인 성공 후 해당 경로로 navigate하면 된다.

Q. Protected Route에서 Loading은 언제 보여줘?
A. 인증 상태를 확인 중이거나 token refresh 중일 때 보여준다.

---

## 8.2 Public Only Route Rules

### [개념]

Public Only Route는 로그인하지 않은 사용자만 접근해야 하는 route를 처리하는 구조다.

예를 들어 로그인 페이지, 회원가입 페이지는 이미 로그인한 사용자가 접근하면 메인 또는 이전 페이지로 이동시킬 수 있다.

---

### [핵심]

Public Only Route 대상:

- Login Page
- Signup Page
- Find Password Page optional
- OAuth Callback Page optional
- Public Auth Pages

핵심 규칙:

- auth initialized 전에는 redirect 판단을 하지 않는다.
- 로그인된 사용자는 메인 또는 이전 페이지로 이동한다.
- 로그인되지 않은 사용자는 페이지를 보여준다.
- redirect flicker를 방지한다.
- OAuth callback 같은 예외 route는 별도 처리한다.
- Login Redirect loop를 방지한다.

---

### [실무]

Public Only Route 예:

```tsx
function PublicOnlyRoute({ children }) {
  const { user, initialized } = useAuth();

  if (!initialized) {
    return <LoadingState message="인증 상태를 확인 중입니다." />;
  }

  if (user) {
    return <Navigate to="/" replace />;
  }

  return children;
}
```

권장:

- 로그인 페이지 접근 전 auth initialized를 확인한다.
- 이미 로그인한 사용자는 자연스러운 위치로 이동한다.
- Login Page가 잠깐 보이는 flicker를 막는다.
- auth loading UI는 짧고 명확하게 작성한다.

주의:

- initialized 없이 user만 보고 판단하면 flicker가 발생한다.
- OAuth callback route는 PublicOnlyRoute에서 제외해야 할 수 있다.
- 로그인 성공 후 redirect 기준과 PublicOnlyRoute redirect 기준이 충돌하지 않게 한다.
- 회원가입 페이지 접근 정책은 서비스에 맞게 정한다.

---

### [FAQ]

Q. PublicOnlyRoute는 뭐야?
A. 로그인하지 않은 사용자만 접근해야 하는 로그인, 회원가입 같은 페이지를 처리하는 route guard다.

Q. 로그인된 사용자가 로그인 페이지에 접근하면?
A. 메인 페이지나 적절한 기본 페이지로 redirect할 수 있다.

Q. PublicOnlyRoute에도 auth initialized가 필요해?
A. 필요하다. 인증 상태 확인 전 redirect하면 로그인 페이지 flicker가 발생할 수 있다.

Q. OAuth Callback도 PublicOnlyRoute에 넣어도 돼?
A. 서비스 구조에 따라 다르다. callback 처리 중 redirect가 방해될 수 있으므로 별도 route로 두는 경우가 많다.

---

# 9. Error Boundary Overview

## 9.1 Error Boundary Purpose

### [개념]

Error Boundary는 React 렌더링 중 발생한 JavaScript 오류로 인해 전체 앱이 깨지는 것을 막고 Fallback UI를 보여주는 구조다.

Error Boundary는 API 요청 실패, Form Validation Error, Route 404를 처리하는 도구가 아니다.

---

### [핵심]

Error Boundary 처리 대상:

- Render Error
- Component Crash
- Lifecycle Error
- Child Component Error
- Unexpected UI Error
- Lazy Component Render Failure
- Fallback UI
- Error Logging

Error Boundary가 처리하지 못하는 대상:

- API Request Failure
- Async Promise Rejection
- Event Handler Error
- Form Validation Error
- 401 / 403 API Error
- Route 404
- Network Error
- Timeout Error

핵심 규칙:

- Render Error는 Error Boundary로 처리한다.
- API Error는 Error State로 처리한다.
- Form Error는 Field Error / Global Error로 처리한다.
- Route 404는 NotFoundPage로 처리한다.
- 사용자에게 stack trace를 노출하지 않는다.
- Root 단위와 Route 단위 Error Boundary를 고려한다.
- Fallback UI에는 다음 행동을 제공한다.

---

### [실무]

역할 구분:

```text
Component 렌더링 오류
→ Error Boundary

API 요청 실패
→ Error State

Form 검증 실패
→ Field Error / Global Form Error

Route 없음
→ NotFoundPage

권한 없음
→ ForbiddenPage
```

Fallback UI 예:

```tsx
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

- 앱 전체 Root Error Boundary를 둔다.
- 주요 route 단위 Error Boundary를 둘 수 있다.
- Fallback UI에 홈 이동 또는 다시 시도 버튼을 제공한다.
- 오류 로깅은 사용자 메시지와 분리한다.
- 개발 환경과 운영 환경의 오류 표시 수준을 분리한다.

주의:

- Error Boundary가 API Error를 자동으로 잡는다고 착각하지 않는다.
- Event Handler 내부 오류는 try/catch 또는 상태 처리로 관리한다.
- 비동기 Promise 오류는 별도로 catch 처리해야 한다.
- Fallback UI도 접근성을 고려한다.

---

### [FAQ]

Q. Error Boundary는 뭐야?
A. React 렌더링 중 발생한 오류로 전체 앱이 깨지는 것을 막고 Fallback UI를 보여주는 구조다.

Q. Error Boundary가 API 에러도 잡아줘?
A. 아니다. API 요청 실패는 Error State로 직접 처리해야 한다.

Q. Error Boundary만 있으면 모든 에러 처리가 끝나?
A. 아니다. API 요청 실패, Form Validation, 인증 오류, Route 404는 별도로 처리해야 한다.

Q. Error Boundary는 언제 필요해?
A. 예상하지 못한 렌더링 오류로 전체 앱이 깨지는 것을 막기 위해 필요하다.

---

# 10. Error Boundary Placement Rules

## 10.1 Root Error Boundary

### [개념]

Root Error Boundary는 앱 최상위에 배치하여 예상하지 못한 렌더링 오류로 전체 앱이 빈 화면이 되는 것을 방지하는 구조다.

Root Error Boundary는 최후의 안전망 역할을 한다.

---

### [핵심]

Root Error Boundary 역할:

- App Crash 방지
- Global Fallback UI
- Error Logging
- Home Navigation
- Reload Action
- User Safe Message
- Stack Trace Hide

핵심 규칙:

- 앱 최상위에 하나 이상 배치한다.
- 사용자에게 안전한 메시지를 제공한다.
- 홈 이동 또는 새로고침 액션을 제공할 수 있다.
- stack trace를 운영 사용자에게 노출하지 않는다.
- 오류 로깅 시스템과 연결할 수 있다.
- Fallback UI도 정상적으로 렌더링 가능해야 한다.

---

### [실무]

배치 예:

```tsx
function AppRoot() {
  return (
    <ErrorBoundary fallback={<RootFallback />}>
      <App />
    </ErrorBoundary>
  );
}
```

Root Fallback 예:

```tsx
function RootFallback() {
  return (
    <main role="alert">
      <h1>문제가 발생했습니다.</h1>
      <p>화면을 표시하는 중 오류가 발생했습니다.</p>
      <a href="/">메인으로 이동</a>
    </main>
  );
}
```

권장:

- Root Error Boundary는 앱 전체 crash 방지용으로 둔다.
- Fallback UI는 의존성을 최소화한다.
- Router나 QueryClient 내부/외부 배치는 라이브러리 구조에 맞게 정한다.
- Error Logging은 사용자 메시지와 분리한다.

주의:

- Root Fallback에서 다시 오류가 나면 복구가 어렵다.
- Fallback UI에 복잡한 상태 의존성을 넣지 않는다.
- Root Boundary만 있고 route별 boundary가 없으면 특정 화면 복구가 제한적일 수 있다.
- Root Error Boundary를 API Error 처리용으로 사용하지 않는다.

---

### [FAQ]

Q. Root Error Boundary는 왜 필요해?
A. 예상하지 못한 렌더링 오류로 앱 전체가 빈 화면이 되는 것을 막기 위해 필요하다.

Q. Root Fallback에는 무엇을 넣어야 해?
A. 문제 안내 메시지와 메인 이동 또는 새로고침 같은 다음 행동을 제공하는 것이 좋다.

Q. Root Error Boundary 하나면 충분해?
A. 최후의 안전망으로 필요하지만 주요 route 단위 boundary를 추가하면 복구 UX가 더 좋아질 수 있다.

Q. Root Error Boundary가 API 실패도 처리해?
A. 아니다. API 실패는 각 화면의 Error State에서 처리해야 한다.

---

## 10.2 Route Level Error Boundary

### [개념]

Route Level Error Boundary는 특정 route 또는 page 단위에서 발생한 렌더링 오류를 해당 화면 범위 안에서 처리하는 구조다.

Route Level Boundary는 전체 앱을 무너뜨리지 않고 문제가 있는 화면만 Fallback UI로 대체할 수 있다.

---

### [핵심]

Route Level Boundary 사용 상황:

- Dashboard Route
- Detail Page Route
- Admin Page Route
- Payment Page Route
- Large Feature Route
- Lazy Loaded Route
- Risky Component Tree

핵심 규칙:

- 큰 route 또는 feature 단위에 배치한다.
- 해당 화면에 맞는 fallback message를 제공한다.
- 홈 이동, 이전 페이지 이동, 다시 시도 액션을 제공할 수 있다.
- Root Boundary보다 구체적인 복구 UX를 제공한다.
- API Error State와 역할을 구분한다.
- lazy loading 실패와 render failure를 고려한다.

---

### [실무]

Route Boundary 예:

```tsx
function FestivalRoute() {
  return (
    <ErrorBoundary fallback={<FestivalFallback />}>
      <FestivalPage />
    </ErrorBoundary>
  );
}
```

Fallback 예:

```tsx
function FestivalFallback() {
  return (
    <section role="alert">
      <h2>축제 화면을 표시하지 못했습니다.</h2>
      <p>잠시 후 다시 시도하거나 메인으로 이동해 주세요.</p>
      <Link to="/">메인으로 이동</Link>
    </section>
  );
}
```

권장:

- 복잡한 화면이나 외부 데이터가 많은 route에 적용한다.
- route별 fallback 문구를 문맥에 맞게 작성한다.
- reset 또는 retry 액션을 제공할 수 있다.
- Root Boundary와 함께 계층적으로 사용할 수 있다.

주의:

- Route Boundary도 API 404 / 500을 대신 처리하지 않는다.
- Fallback UI가 해당 route 내부 상태에 과도하게 의존하지 않게 한다.
- 너무 작은 컴포넌트마다 boundary를 남발하지 않는다.
- Error Boundary reset 기준을 명확히 한다.

---

### [FAQ]

Q. Route Level Error Boundary는 왜 필요해?
A. 특정 화면 오류가 앱 전체를 깨뜨리지 않도록 해당 route 범위에서 fallback UI를 보여주기 위해 필요하다.

Q. 모든 컴포넌트마다 Error Boundary를 넣어야 해?
A. 아니다. 주요 route, 큰 feature, 오류 위험이 큰 영역 중심으로 배치하는 것이 좋다.

Q. Route Boundary와 Page Error State는 달라?
A. 다르다. Route Boundary는 렌더링 오류를 처리하고 Page Error State는 API 요청 실패를 처리한다.

Q. Lazy Loaded Route에도 Error Boundary가 필요해?
A. lazy component 로딩이나 렌더링 실패가 있을 수 있으므로 적용을 고려할 수 있다.

---

# 11. Fallback UI Rules

## 11.1 Fallback UI Design

### [개념]

Fallback UI는 정상 화면을 보여줄 수 없을 때 대신 보여주는 안전한 UI다.

Fallback UI는 Error Boundary, 권한 없음, 리소스 없음, 화면 표시 실패 같은 상황에서 사용된다.

---

### [핵심]

Fallback UI 구성 요소:

- Clear Title
- User Friendly Message
- Retry Action optional
- Home Link
- Back Link optional
- Safe Layout
- No Stack Trace
- Error Logging Separate

핵심 규칙:

- 사용자가 이해할 수 있는 메시지를 제공한다.
- 다음 행동을 제공한다.
- 내부 오류 상세를 노출하지 않는다.
- 접근성 role을 고려한다.
- Fallback 자체가 crash되지 않게 단순하게 만든다.
- 화면 문맥에 맞는 fallback을 제공한다.

---

### [실무]

Fallback UI 예:

```tsx
function FallbackUI({ onReset }) {
  return (
    <main role="alert">
      <h1>문제가 발생했습니다.</h1>
      <p>화면을 표시하는 중 오류가 발생했습니다.</p>
      <button type="button" onClick={onReset}>
        다시 시도
      </button>
      <Link to="/">메인으로 이동</Link>
    </main>
  );
}
```

문맥별 문구:

```text
Root Fallback
→ 화면을 표시하는 중 오류가 발생했습니다.

Festival Route Fallback
→ 축제 화면을 표시하지 못했습니다.

Admin Route Fallback
→ 관리자 화면을 표시하지 못했습니다.

Payment Fallback
→ 결제 화면을 표시하지 못했습니다. 결제 상태를 다시 확인해 주세요.
```

권장:

- Title, Description, Action 구조를 사용한다.
- Home Link 또는 Retry Button을 제공한다.
- 운영 환경에서 stack trace를 숨긴다.
- Fallback UI는 최소 의존성으로 작성한다.
- 중요한 도메인에서는 상태 확인 안내를 제공한다.

주의:

- Fallback UI에 복잡한 API 요청을 넣지 않는다.
- stack trace를 사용자에게 보여주지 않는다.
- 단순 빈 화면으로 대체하지 않는다.
- Error Boundary Fallback과 API ErrorState 문구를 혼동하지 않는다.

---

### [FAQ]

Q. Fallback UI에는 뭘 넣어야 해?
A. 문제 안내 메시지와 사용자가 할 수 있는 다음 행동을 제공하는 것이 좋다.

Q. 오류 stack trace를 보여줘도 돼?
A. 운영 환경에서는 사용자에게 보여주지 않는 것이 좋다.

Q. Fallback UI에 다시 시도 버튼을 넣어도 돼?
A. 가능하다. reset이나 reload가 의미 있는 경우 다시 시도 버튼을 제공할 수 있다.

Q. Fallback UI와 ErrorState는 같아?
A. 다르다. Fallback UI는 주로 렌더링 실패 대체 화면이고 ErrorState는 API 요청 실패 UI다.

---

# 12. Form / Route / Boundary Accessibility Rules

## 12.1 Form Error Accessibility

### [개념]

Form Error Accessibility는 보조 기술 사용자도 Form 오류를 인지하고 수정할 수 있게 하는 기준이다.

Field Error와 Global Form Error는 텍스트, ARIA 속성, focus 흐름을 통해 접근 가능해야 한다.

---

### [핵심]

접근성 기준:

- `aria-invalid`
- `aria-describedby`
- `role="alert"`
- Error Message ID
- Error Summary
- Focus Management
- Keyboard Navigation
- Non-color-only Error

핵심 규칙:

- Field Error를 input과 연결한다.
- 오류를 색상만으로 표시하지 않는다.
- Global Error는 `role="alert"`를 고려한다.
- 긴 Form은 Error Summary를 고려한다.
- Submit 실패 시 첫 오류 field로 focus 이동을 고려한다.
- 오류 메시지 id를 중복하지 않는다.

---

### [실무]

Field Error 예:

```tsx
<input
  id="nickname"
  name="nickname"
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

Error Summary 예:

```tsx
function ErrorSummary({ errors }) {
  const errorEntries = Object.entries(errors);

  if (errorEntries.length === 0) {
    return null;
  }

  return (
    <section role="alert" aria-labelledby="error-summary-title">
      <h2 id="error-summary-title">입력 내용을 확인해 주세요.</h2>
      <ul>
        {errorEntries.map(([field, message]) => (
          <li key={field}>{message}</li>
        ))}
      </ul>
    </section>
  );
}
```

권장:

- input과 error message를 명시적으로 연결한다.
- Error Summary는 긴 Form에서 유용하다.
- 색상, 아이콘, 텍스트를 함께 사용한다.
- focus 이동은 사용자 작업을 방해하지 않게 신중히 적용한다.

주의:

- 빨간색 테두리만으로 오류를 전달하지 않는다.
- role alert를 너무 많이 중복 사용하지 않는다.
- focus를 매 입력마다 강제로 이동하지 않는다.
- 오류 메시지 id가 여러 input에서 중복되면 안 된다.

---

### [FAQ]

Q. Form Error 접근성에서 가장 중요한 것은?
A. Field Error를 input과 연결하고 사용자가 오류를 인지하고 수정할 수 있게 하는 것이다.

Q. Error Message는 색상만 빨갛게 하면 돼?
A. 아니다. 색상 외에도 텍스트, aria 속성, 아이콘 등을 사용해 오류를 명확히 전달해야 한다.

Q. submit 실패 시 focus 이동이 필요해?
A. 필수는 아니지만 첫 오류 field로 focus를 이동하면 사용자가 빠르게 수정할 수 있다.

Q. 긴 Form에서는 Error Summary가 필요해?
A. 유용할 수 있다. 여러 오류를 한 번에 안내하고 각 필드로 이동하게 만들 수 있다.

---

## 12.2 Route / Fallback Accessibility

### [개념]

Route / Fallback Accessibility는 NotFoundPage, ForbiddenPage, Fallback UI 같은 대체 화면을 보조 기술 사용자도 이해하고 이동할 수 있게 하는 기준이다.

Route Error와 Fallback UI는 명확한 heading, 설명, 접근 가능한 action을 제공해야 한다.

---

### [핵심]

접근성 기준:

- Semantic Main
- Heading
- Description
- Accessible Link
- Accessible Button
- Focus Management
- `role="alert"` optional
- Keyboard Navigation
- No Color-only Message

핵심 규칙:

- 페이지 단위 오류에는 heading을 제공한다.
- 메인 이동, 이전 페이지 이동 같은 action은 link 또는 button으로 구현한다.
- 렌더링 오류 Fallback은 `role="alert"`를 고려한다.
- NotFoundPage는 긴급 오류가 아니므로 alert 남발을 피한다.
- 페이지 이동 후 focus 위치를 고려한다.
- 버튼처럼 보이는 div를 사용하지 않는다.

---

### [실무]

NotFound 접근성 예:

```tsx
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

Fallback 접근성 예:

```tsx
function RootFallback() {
  return (
    <main role="alert">
      <h1>문제가 발생했습니다.</h1>
      <p>화면을 표시하는 중 오류가 발생했습니다.</p>
      <a href="/">메인으로 이동</a>
    </main>
  );
}
```

권장:

- 대체 화면은 `main`과 heading을 포함한다.
- action label은 구체적으로 작성한다.
- link와 button 역할을 구분한다.
- Fallback UI는 키보드로 조작 가능해야 한다.
- Error Boundary fallback은 사용자에게 안전한 문구를 사용한다.

주의:

- Route Error를 빈 div로 처리하지 않는다.
- 클릭 가능한 div를 button처럼 쓰지 않는다.
- 오류 상태를 색상이나 아이콘만으로 전달하지 않는다.
- stack trace를 screen reader에 노출하지 않는다.

---

### [FAQ]

Q. NotFoundPage에도 접근성이 필요해?
A. 필요하다. 사용자가 페이지를 찾을 수 없다는 상태와 다음 이동 방법을 이해해야 한다.

Q. Fallback UI에는 role alert가 필요해?
A. 렌더링 오류처럼 중요한 오류에는 고려할 수 있지만 모든 대체 화면에 남발하지 않는다.

Q. Route Error 화면에는 heading이 필요해?
A. 권장한다. 사용자가 현재 페이지 상태를 빠르게 이해할 수 있다.

Q. 메인 이동은 button이야 link야?
A. 다른 페이지로 이동하는 동작이므로 link가 적합하다.

---

# 13. Form / Route / Boundary Troubleshooting Rules

## 13.1 Form Error Not Showing

### [개념]

Form Error Not Showing은 서버나 클라이언트에서 오류가 발생했지만 Form 화면에 오류 메시지가 표시되지 않는 문제다.

주요 원인은 errors key 불일치, catch 처리 누락, Form State 연결 누락, interceptor Promise.reject 누락이다.

---

### [핵심]

주요 원인:

- Server errors key와 input name 불일치
- setFieldErrors 누락
- setFormError 누락
- catch에서 error를 삼킴
- interceptor에서 Promise.reject 누락
- Validation Response Shape 착각
- Field Error 렌더링 조건 오류
- Form Provider 범위 문제
- Error Message Component 미렌더링

핵심 규칙:

- 서버 errors key와 input name을 확인한다.
- catch 또는 onError에서 오류 상태를 설정한다.
- Error UI 렌더링 조건을 확인한다.
- interceptor가 error를 다시 reject하는지 확인한다.
- fallback global error를 제공한다.
- Network Response의 error body를 확인한다.

---

### [실무]

Debug Flow:

```text
Form Error 발생
→ Network Response 확인
→ error.response.data.errors 확인
→ field name mapping 확인
→ setFieldErrors 실행 확인
→ FormError 렌더링 조건 확인
→ interceptor Promise.reject 확인
```

나쁜 interceptor 예:

```typescript
api.interceptors.response.use(
  (response) => response,
  (error) => {
    toast.error("요청 실패");
  },
);
```

개선 예:

```typescript
api.interceptors.response.use(
  (response) => response,
  (error) => {
    toast.error("요청 실패");
    return Promise.reject(error);
  },
);
```

field mapping 확인:

```text
Backend: errors.userEmail
Frontend: input name="email"
→ mapping 필요
```

권장:

- field error가 없으면 global error로 fallback한다.
- validation response shape를 API 문서와 맞춘다.
- error mapping 함수를 테스트한다.
- Form submit 실패 케이스를 수동으로 확인한다.

주의:

- 오류를 console.log만 하고 끝내지 않는다.
- Toast만 띄우고 field error를 누락하지 않는다.
- interceptor에서 error를 삼키면 화면별 onError가 실행되지 않는다.
- field name 불일치는 매우 흔한 원인이다.

---

### [FAQ]

Q. Form Error가 안 보여?
A. 서버 errors key와 input name, setFieldErrors 실행 여부, Error UI 조건, interceptor Promise.reject를 확인해야 한다.

Q. 서버는 errors를 보냈는데 input 밑에 안 나와?
A. 서버 field name과 Frontend input name이 다를 가능성이 높다.

Q. interceptor에서 Toast는 뜨는데 Form Error는 안 떠?
A. interceptor가 Promise.reject를 반환하지 않아 호출부가 error를 받지 못할 수 있다.

Q. Field Error가 없을 때는 어떻게 해?
A. Global Form Error로 fallback 메시지를 보여주는 것이 좋다.

---

## 13.2 Route Flicker Troubleshooting

### [개념]

Route Flicker는 로그인 페이지, 메인 페이지, 권한 페이지, Loading 화면이 짧게 깜빡이며 잘못 보이는 문제다.

주요 원인은 auth initialized 구분 없음, redirect 조건 조기 실행, token refresh 중 redirect, PublicOnlyRoute 판단 오류다.

---

### [핵심]

주요 원인:

- auth initialized 없음
- `user === null`을 즉시 unauthenticated로 판단
- token refresh 중 Login Redirect
- PublicOnlyRoute가 먼저 렌더링됨
- ProtectedRoute와 Login Redirect 충돌
- enabled query가 auth 전에 실행됨
- role 정보 로딩 전 Forbidden 처리
- location state 처리 오류

핵심 규칙:

- auth initialized 전에는 redirect하지 않는다.
- token refresh 중에는 Auth Loading을 보여준다.
- role 정보가 필요한 경우 권한 판정 전 Loading을 표시한다.
- PublicOnlyRoute와 ProtectedRoute 조건을 일관되게 작성한다.
- Login 후 redirect location을 명확히 처리한다.
- auth query와 route guard 흐름을 연결한다.

---

### [실무]

나쁜 예:

```tsx
if (!user) {
  return <Navigate to="/login" />;
}
```

문제:

- 인증 확인 전 user가 null이면 로그인 페이지가 잠깐 보일 수 있다.

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

권장:

- auth initialized, user, role loading을 분리한다.
- redirect 조건은 loading 상태 이후에 실행한다.
- 로그인 후 이동 위치를 location state로 관리한다.
- Protected query는 auth 확인 후 enabled한다.

주의:

- 인증 확인 전 login redirect를 실행하지 않는다.
- 권한 정보 로딩 전 ForbiddenPage를 보여주지 않는다.
- PublicOnlyRoute에서 로그인 페이지 flicker를 방치하지 않는다.
- redirect loop를 확인한다.

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

## 13.3 Error Boundary Not Catching

### [개념]

Error Boundary Not Catching은 오류가 발생했지만 Error Boundary Fallback이 표시되지 않는 문제다.

주요 원인은 Error Boundary가 처리하지 못하는 async error, event handler error, API error를 Error Boundary가 잡을 것으로 기대하는 경우다.

---

### [핵심]

Error Boundary가 잡지 못하는 오류:

- Event Handler Error
- Async API Error
- Promise Rejection
- setTimeout 내부 Error
- Server Response Error
- Form Validation Error
- Network Error
- Route 404

핵심 규칙:

- API Error는 Error State로 처리한다.
- Event Handler Error는 try/catch로 처리한다.
- Promise Error는 catch 또는 async/await try/catch로 처리한다.
- 렌더링 중 발생한 오류만 Error Boundary가 처리한다.
- Boundary가 오류 발생 컴포넌트의 상위에 있어야 한다.
- Fallback UI 자체가 crash되지 않아야 한다.

---

### [실무]

잡히지 않는 예:

```tsx
async function handleClick() {
  const result = await api.get("/fail");
  setData(result.data);
}
```

개선 예:

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

`user`가 undefined면 렌더링 중 오류가 발생할 수 있으며 Error Boundary가 상위에 있으면 Fallback UI를 보여줄 수 있다.

Debug Flow:

```text
오류 발생
→ 오류 위치 확인
→ render error인지 async error인지 분류
→ Boundary 배치 위치 확인
→ Fallback UI 오류 여부 확인
→ API Error State 필요 여부 확인
```

권장:

- 렌더링 오류와 API 오류를 먼저 분류한다.
- Error Boundary를 오류 발생 컴포넌트 상위에 배치한다.
- 비동기 오류는 try/catch 또는 Query Error State로 처리한다.
- Fallback UI를 단순하고 안전하게 작성한다.

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

# 14. Form / Route / Boundary Checklist

## 14.1 Form Error UX Checklist

### [개념]

Form Error UX Checklist는 Form 입력, 검증, 제출, 실패 복구가 사용자에게 수정 가능한 방식으로 제공되는지 검수하는 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] Field Error와 Global Form Error를 구분했는가?
- [ ] Field Error가 input 근처에 표시되는가?
- [ ] Field Error에 aria-invalid와 aria-describedby가 적용되었는가?
- [ ] 서버 Validation Error를 Form State로 매핑하는가?
- [ ] 서버 errors key와 input name이 일치하는가?
- [ ] field에 연결할 수 없는 오류는 Global Error로 처리하는가?
- [ ] 로그인 실패는 과도한 계정 정보를 노출하지 않는가?
- [ ] Submit Loading 중 버튼을 disabled 처리하는가?
- [ ] 실패 후 입력값을 유지하는가?
- [ ] 실패 후 버튼이 다시 활성화되는가?
- [ ] 오류 수정 후 관련 error를 제거하는가?
- [ ] 첫 오류 focus 이동을 검토했는가?
- [ ] 서버 원문 message를 그대로 노출하지 않는가?
```

---

### [실무]

검수 흐름:

```text
Form Submit Scenario 확인
→ Client Validation 확인
→ Server Validation Mapping 확인
→ Field / Global Error 위치 확인
→ Submit Loading 확인
→ Failure Recovery 확인
→ Accessibility 확인
→ Security Message 확인
```

Form별 기준:

| Form          | 핵심 검수                                     |
| ------------- | --------------------------------------------- |
| Login Form    | Global Error, Submit Loading, 보안 메시지     |
| Signup Form   | Field Error Mapping, 중복 값 오류             |
| Profile Form  | Inline Success, Field Error                   |
| Review Form   | Rating Error, Submit Loading, Success Refetch |
| Password Form | Field Error, Global Error, Success Message    |
| Payment Form  | Submit Loading, 처리 여부 확인, 중복 방지     |

---

### [FAQ]

Q. Form Error UX 검수에서 가장 중요한 것은?
A. Field Error와 Global Form Error를 구분하고 사용자가 오류를 수정할 수 있게 만드는 것이다.

Q. 서버 Validation Error 검수 핵심은?
A. 서버 errors key가 Frontend input name과 연결되어 input 근처에 표시되는지 확인하는 것이다.

Q. Submit Loading 검수 핵심은?
A. 중복 제출 방지, 처리 중 문구, 실패 후 버튼 복구 여부를 확인하는 것이다.

Q. 로그인 Form Error 검수 핵심은?
A. 인증 실패를 Global Error로 처리하고 계정 존재 여부 같은 민감한 정보를 과도하게 노출하지 않는 것이다.

---

## 14.2 Route Error UX Checklist

### [개념]

Route Error UX Checklist는 URL, 인증, 권한, route param, 리소스 없음 상태가 적절한 화면으로 처리되는지 검수하는 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] Route 404와 API 404를 구분했는가?
- [ ] catch-all NotFoundPage가 존재하는가?
- [ ] NotFoundPage에 메인 이동 또는 이전 이동이 있는가?
- [ ] API Resource Not Found UI가 존재하는가?
- [ ] 401 Login Required와 403 Forbidden을 구분했는가?
- [ ] ForbiddenPage에서 logout하지 않는가?
- [ ] ProtectedRoute가 auth initialized 이후 redirect하는가?
- [ ] PublicOnlyRoute가 auth initialized 이후 redirect하는가?
- [ ] token refresh 중 Auth Loading을 표시하는가?
- [ ] role loading 전 ForbiddenPage를 표시하지 않는가?
- [ ] login redirect 후 원래 위치 복귀 기준이 있는가?
- [ ] redirect loop 가능성을 점검했는가?
- [ ] SPA fallback 새로고침 404 가능성을 확인했는가?
```

---

### [실무]

검수 흐름:

```text
URL 접근 시나리오 확인
→ Route Match 확인
→ Auth Guard 확인
→ Permission Guard 확인
→ Route Param 검증
→ API Resource 404 확인
→ Redirect Flicker 확인
→ Next Action 확인
```

Route별 기준:

| Route 상황                           | 권장 UX                        |
| ------------------------------------ | ------------------------------ |
| 알 수 없는 URL                       | NotFoundPage                   |
| 로그인 필요 페이지                   | Auth Loading 후 Login Redirect |
| 권한 없는 페이지                     | ForbiddenPage                  |
| 잘못된 상세 ID                       | Resource Not Found             |
| 삭제된 리소스                        | Resource Not Found + 목록 이동 |
| 로그인된 사용자의 로그인 페이지 접근 | PublicOnlyRoute Redirect       |
| 새로고침 서버 404                    | SPA fallback 설정 확인         |

---

### [FAQ]

Q. Route Error UX 검수에서 가장 중요한 것은?
A. Route 404, API 404, 401, 403을 구분하고 적절한 이동 또는 안내를 제공하는 것이다.

Q. ProtectedRoute 검수 핵심은?
A. auth initialized 전에는 redirect하지 않고 인증 확인 후 Login Redirect 또는 Content Render를 결정하는 것이다.

Q. ForbiddenPage 검수 핵심은?
A. 로그인 상태를 유지하고 권한 없음 메시지와 다음 행동을 제공하는 것이다.

Q. 새로고침 404는 Frontend 문제야?
A. SPA fallback 서버 설정 문제일 수 있으므로 배포 서버가 index.html fallback을 제공하는지 확인해야 한다.

---

## 14.3 Error Boundary Checklist

### [개념]

Error Boundary Checklist는 렌더링 오류로 전체 앱이 깨지는 것을 방지하고 사용자에게 안전한 Fallback UI를 제공하는지 검수하는 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] Root Error Boundary가 존재하는가?
- [ ] 주요 route 또는 feature 단위 Boundary를 검토했는가?
- [ ] Fallback UI가 사용자 친화적인 메시지를 제공하는가?
- [ ] Fallback UI에 다음 행동이 있는가?
- [ ] 운영 환경에서 stack trace를 노출하지 않는가?
- [ ] Error Boundary와 API Error State 역할을 구분했는가?
- [ ] Event Handler Error를 Boundary가 잡는다고 착각하지 않는가?
- [ ] Async API Error를 Boundary가 잡는다고 착각하지 않는가?
- [ ] Fallback UI 자체가 crash되지 않게 단순한가?
- [ ] Error Logging과 사용자 메시지를 분리했는가?
- [ ] Fallback UI 접근성을 고려했는가?
```

---

### [실무]

검수 흐름:

```text
Render Error Scenario 확인
→ Boundary Placement 확인
→ Fallback UI 확인
→ API Error와 역할 분리 확인
→ Logging 분리 확인
→ Accessibility 확인
→ Fallback Crash 가능성 확인
```

Boundary별 기준:

| Boundary         | 역할                           |
| ---------------- | ------------------------------ |
| Root Boundary    | 앱 전체 crash 방지             |
| Route Boundary   | 특정 화면 crash 격리           |
| Feature Boundary | 큰 기능 단위 crash 격리        |
| Widget Boundary  | 외부 위젯 / 위험 컴포넌트 격리 |

---

### [FAQ]

Q. Error Boundary 검수에서 가장 중요한 것은?
A. 렌더링 오류와 API 오류 역할을 구분하고 Fallback UI가 안전하게 표시되는지 확인하는 것이다.

Q. Root Error Boundary는 필수야?
A. 앱 전체 빈 화면을 방지하기 위해 강하게 권장된다.

Q. Fallback UI 검수 핵심은?
A. 사용자 친화적 메시지, 다음 행동, stack trace 비노출, 접근성, 단순성을 확인하는 것이다.

Q. Error Boundary가 모든 오류를 잡는지 검수하면 돼?
A. 아니다. Error Boundary는 렌더링 오류 중심이며 API, async, event handler 오류는 별도로 처리해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Error Handling & Loading UX Part06은 무엇을 다뤄?
A. Form Error UX, Route Error UX, Protected Route, ForbiddenPage, NotFoundPage, Error Boundary, Fallback UI 기준을 다룬다.

Q. Form Error UX는 뭐야?
A. 사용자의 입력 오류와 제출 실패를 Form 화면에서 수정 가능하게 보여주는 오류 UX 기준이다.

Q. Form Error에서 가장 중요한 구분은?
A. 특정 input 문제인 Field Error와 Form 전체 문제인 Global Form Error를 구분하는 것이다.

Q. 서버 Validation Error도 Frontend에서 처리해야 해?
A. 그렇다. 서버 field errors를 Form State로 매핑해 사용자에게 수정 위치를 알려줘야 한다.

Q. 제출 실패 후 입력값은 지워야 해?
A. 보통 지우지 않는다. 사용자가 오류를 수정할 수 있도록 유지하는 것이 좋다.

Q. Field Error는 어디에 보여줘?
A. 해당 input 근처에 보여주는 것이 좋다.

Q. Field Error를 Toast로만 보여줘도 돼?
A. 권장하지 않는다. 사용자가 어떤 필드를 수정해야 하는지 알기 어렵다.

Q. Field Error 문구는 어떻게 써야 해?
A. 사용자가 어떤 값을 어떻게 수정해야 하는지 알 수 있게 구체적으로 작성해야 한다.

Q. Field Error 접근성은 어떻게 처리해?
A. aria-invalid와 aria-describedby를 사용해 input과 오류 메시지를 연결하는 것이 좋다.

Q. Server Field Error Mapping은 뭐야?
A. 서버 검증 오류의 field errors를 Frontend Form State와 input 오류 메시지로 연결하는 작업이다.

Q. 서버 errors key와 input name이 다르면 어떻게 해?
A. mapping table이나 normalize 함수를 사용해 Frontend field name으로 변환해야 한다.

Q. field에 연결할 수 없는 서버 오류는 어떻게 해?
A. Global Form Error로 표시하는 것이 좋다.

Q. 서버 validation message를 그대로 써도 돼?
A. 사용자에게 안전하고 이해 가능한 메시지라면 가능하지만 내부 정보가 포함되면 변환해야 한다.

Q. Global Form Error는 뭐야?
A. Form 전체에 해당하며 특정 field 하나로 귀속하기 어려운 오류 메시지다.

Q. 로그인 실패는 Field Error야 Global Error야?
A. 이메일 형식 오류는 Field Error이고 계정 정보 불일치 같은 인증 실패는 Global Error로 처리하는 경우가 많다.

Q. Global Error는 어디에 보여줘?
A. Form 상단이나 제출 버튼 근처처럼 사용자가 쉽게 인식할 수 있는 위치에 보여준다.

Q. Global Error가 있어도 입력값은 유지해야 해?
A. 보통 유지한다. 사용자가 수정하거나 다시 제출할 수 있어야 한다.

Q. 로그인 실패 메시지는 어떻게 쓰는 게 좋아?
A. 보안상 “이메일 또는 비밀번호를 확인해 주세요.”처럼 일반적인 메시지가 적합한 경우가 많다.

Q. 로그인 실패 후 비밀번호를 지워야 해?
A. 서비스 정책에 따라 다르다. 보안과 사용성 기준을 함께 고려해야 한다.

Q. 로그인 실패 401과 세션 만료 401은 같아?
A. 다르다. 로그인 실패는 Form Error이고 세션 만료는 Auth State 정리와 Login Redirect가 필요하다.

Q. Submit Loading은 왜 필요해?
A. 중복 제출을 방지하고 사용자가 처리 중임을 알 수 있게 하기 위해 필요하다.

Q. 제출 중 버튼을 disabled 해야 해?
A. 권장한다. 중복 제출을 줄이고 사용자가 처리 중임을 이해할 수 있다.

Q. Submit Loading과 Page Loading은 같아?
A. 다르다. Submit Loading은 사용자 액션 처리 중이고 Page Loading은 화면 데이터 조회 상태다.

Q. Form 제출 실패 후 무엇을 복구해야 해?
A. 입력값, 버튼 상태, 오류 메시지, focus 흐름을 사용자가 다시 제출할 수 있게 복구해야 한다.

Q. 실패 후 Form을 reset해도 돼?
A. 권장하지 않는다. 사용자가 오류를 수정할 수 있도록 입력값을 유지하는 것이 좋다.

Q. 사용자가 입력을 수정하면 에러 메시지를 지워도 돼?
A. 가능하다. 해당 field error를 제거하고 재검증 시 다시 표시할 수 있다.

Q. 첫 오류 field로 focus 이동이 필요해?
A. 필수는 아니지만 긴 Form에서는 사용자가 빠르게 수정할 수 있어 도움이 된다.

Q. Route Error UX는 뭐야?
A. 잘못된 URL, 권한 없는 페이지, 인증 필요 페이지, 잘못된 route param 접근을 처리하는 UX 기준이다.

Q. Route 404와 API 404는 달라?
A. 다르다. Route 404는 URL 매칭 실패이고 API 404는 서버 리소스나 endpoint를 찾지 못한 것이다.

Q. 401과 403 Route UX는 어떻게 달라?
A. 401은 로그인 필요 흐름이고 403은 로그인은 되었지만 권한이 없는 상태다.

Q. Route Error에도 버튼이 필요해?
A. 메인 이동, 이전 페이지 이동, 목록 이동 같은 다음 행동을 제공하는 것이 좋다.

Q. NotFoundPage에는 뭘 넣어야 해?
A. 페이지를 찾을 수 없다는 안내와 메인 이동 또는 이전 페이지 이동 같은 다음 행동을 제공한다.

Q. React Router에서 NotFoundPage는 어떻게 연결해?
A. path="\*" catch-all route를 추가해 연결할 수 있다.

Q. API 404도 NotFoundPage로 보내?
A. 상황에 따라 다르다. 상세 리소스 없음은 해당 페이지 안에서 Resource Not Found UI를 보여줄 수 있다.

Q. 새로고침했더니 서버 404가 나와?
A. SPA fallback 설정이 없을 수 있으므로 서버가 index.html로 fallback하는지 확인해야 한다.

Q. API Resource Not Found는 뭐야?
A. 페이지 route는 존재하지만 API가 특정 리소스를 찾지 못한 상태다.

Q. 상세 페이지 데이터가 없으면 어떻게 보여줘?
A. 해당 리소스를 찾을 수 없다는 메시지와 목록으로 돌아가는 버튼을 제공하는 것이 좋다.

Q. Resource Not Found와 Empty State는 달라?
A. 다르다. Empty State는 목록 데이터 없음이고 Resource Not Found는 특정 리소스가 없는 상태다.

Q. API endpoint 404와 resource 404는 어떻게 구분해?
A. Network 탭에서 요청 URL, Backend route, response message를 확인해야 한다.

Q. ForbiddenPage는 뭐야?
A. 로그인은 되었지만 해당 페이지나 기능에 접근 권한이 없을 때 보여주는 화면이다.

Q. 403이면 로그아웃해야 해?
A. 대부분 아니다. 로그인은 되어 있지만 권한이 부족한 상태이므로 권한 없음 UI를 보여주는 것이 일반적이다.

Q. 403이면 로그인 페이지로 보내야 해?
A. 보통은 권한 없음 페이지나 메시지를 보여주는 것이 더 적절하다.

Q. ForbiddenPage와 Login Page는 달라?
A. 다르다. Forbidden은 로그인은 되었지만 권한이 없는 상태이고 Login은 인증이 필요한 상태다.

Q. Protected Route에서 왜 auth initialized가 필요해?
A. 인증 상태 확인 전 user가 null일 수 있으므로 잘못된 redirect와 flicker를 막기 위해 필요하다.

Q. 로그인 페이지가 잠깐 보였다가 메인으로 가?
A. auth initialized 전에 PublicOnlyRoute 또는 ProtectedRoute가 redirect 판단을 실행했을 수 있다.

Q. 로그인 후 원래 페이지로 돌아가려면?
A. Login Redirect 시 location state에 from 경로를 저장하고 로그인 성공 후 해당 경로로 navigate하면 된다.

Q. Protected Route에서 Loading은 언제 보여줘?
A. 인증 상태를 확인 중이거나 token refresh 중일 때 보여준다.

Q. PublicOnlyRoute는 뭐야?
A. 로그인하지 않은 사용자만 접근해야 하는 로그인, 회원가입 같은 페이지를 처리하는 route guard다.

Q. 로그인된 사용자가 로그인 페이지에 접근하면?
A. 메인 페이지나 적절한 기본 페이지로 redirect할 수 있다.

Q. PublicOnlyRoute에도 auth initialized가 필요해?
A. 필요하다. 인증 상태 확인 전 redirect하면 로그인 페이지 flicker가 발생할 수 있다.

Q. OAuth Callback도 PublicOnlyRoute에 넣어도 돼?
A. 서비스 구조에 따라 다르다. callback 처리 중 redirect가 방해될 수 있으므로 별도 route로 두는 경우가 많다.

Q. Error Boundary는 뭐야?
A. React 렌더링 중 발생한 오류로 전체 앱이 깨지는 것을 막고 Fallback UI를 보여주는 구조다.

Q. Error Boundary가 API 에러도 잡아줘?
A. 아니다. API 요청 실패는 Error State로 직접 처리해야 한다.

Q. Error Boundary만 있으면 모든 에러 처리가 끝나?
A. 아니다. API 요청 실패, Form Validation, 인증 오류, Route 404는 별도로 처리해야 한다.

Q. Error Boundary는 언제 필요해?
A. 예상하지 못한 렌더링 오류로 전체 앱이 깨지는 것을 막기 위해 필요하다.

Q. Root Error Boundary는 왜 필요해?
A. 예상하지 못한 렌더링 오류로 앱 전체가 빈 화면이 되는 것을 막기 위해 필요하다.

Q. Root Fallback에는 무엇을 넣어야 해?
A. 문제 안내 메시지와 메인 이동 또는 새로고침 같은 다음 행동을 제공하는 것이 좋다.

Q. Root Error Boundary 하나면 충분해?
A. 최후의 안전망으로 필요하지만 주요 route 단위 boundary를 추가하면 복구 UX가 더 좋아질 수 있다.

Q. Route Level Error Boundary는 왜 필요해?
A. 특정 화면 오류가 앱 전체를 깨뜨리지 않도록 해당 route 범위에서 fallback UI를 보여주기 위해 필요하다.

Q. 모든 컴포넌트마다 Error Boundary를 넣어야 해?
A. 아니다. 주요 route, 큰 feature, 오류 위험이 큰 영역 중심으로 배치하는 것이 좋다.

Q. Route Boundary와 Page Error State는 달라?
A. 다르다. Route Boundary는 렌더링 오류를 처리하고 Page Error State는 API 요청 실패를 처리한다.

Q. Lazy Loaded Route에도 Error Boundary가 필요해?
A. lazy component 로딩이나 렌더링 실패가 있을 수 있으므로 적용을 고려할 수 있다.

Q. Fallback UI에는 뭘 넣어야 해?
A. 문제 안내 메시지와 사용자가 할 수 있는 다음 행동을 제공하는 것이 좋다.

Q. 오류 stack trace를 보여줘도 돼?
A. 운영 환경에서는 사용자에게 보여주지 않는 것이 좋다.

Q. Fallback UI에 다시 시도 버튼을 넣어도 돼?
A. 가능하다. reset이나 reload가 의미 있는 경우 다시 시도 버튼을 제공할 수 있다.

Q. Fallback UI와 ErrorState는 같아?
A. 다르다. Fallback UI는 주로 렌더링 실패 대체 화면이고 ErrorState는 API 요청 실패 UI다.

Q. Form Error 접근성에서 가장 중요한 것은?
A. Field Error를 input과 연결하고 사용자가 오류를 인지하고 수정할 수 있게 하는 것이다.

Q. Error Message는 색상만 빨갛게 하면 돼?
A. 아니다. 색상 외에도 텍스트, aria 속성, 아이콘 등을 사용해 오류를 명확히 전달해야 한다.

Q. 긴 Form에서는 Error Summary가 필요해?
A. 유용할 수 있다. 여러 오류를 한 번에 안내하고 각 필드로 이동하게 만들 수 있다.

Q. NotFoundPage에도 접근성이 필요해?
A. 필요하다. 사용자가 페이지를 찾을 수 없다는 상태와 다음 이동 방법을 이해해야 한다.

Q. Fallback UI에는 role alert가 필요해?
A. 렌더링 오류처럼 중요한 오류에는 고려할 수 있지만 모든 대체 화면에 남발하지 않는다.

Q. Route Error 화면에는 heading이 필요해?
A. 권장한다. 사용자가 현재 페이지 상태를 빠르게 이해할 수 있다.

Q. 메인 이동은 button이야 link야?
A. 다른 페이지로 이동하는 동작이므로 link가 적합하다.

Q. Form Error가 안 보여?
A. 서버 errors key와 input name, setFieldErrors 실행 여부, Error UI 조건, interceptor Promise.reject를 확인해야 한다.

Q. 서버는 errors를 보냈는데 input 밑에 안 나와?
A. 서버 field name과 Frontend input name이 다를 가능성이 높다.

Q. interceptor에서 Toast는 뜨는데 Form Error는 안 떠?
A. interceptor가 Promise.reject를 반환하지 않아 호출부가 error를 받지 못할 수 있다.

Q. 권한 없음 페이지가 잠깐 보였다가 정상 페이지가 보여?
A. role 정보가 로딩되기 전에 Forbidden 판단을 했을 수 있다.

Q. Route Flicker를 막으려면?
A. auth initialized와 role loading 상태를 먼저 확인하고 그 이후 redirect나 forbidden 판단을 해야 한다.

Q. token refresh 중에는 어떤 UI를 보여줘?
A. 인증 상태를 확인 중이라는 Auth Loading UI를 보여주는 것이 적합하다.

Q. Error Boundary가 오류를 못 잡아?
A. 오류가 API error, event handler error, async promise error라면 Error Boundary가 자동으로 잡지 못한다.

Q. API Error는 Error Boundary로 처리하면 안 돼?
A. 아니다. API Error는 Query Error State나 try/catch 기반 Error State로 처리해야 한다.

Q. Error Boundary가 잡는 오류는 뭐야?
A. 주로 React 렌더링 중 발생한 오류와 child component crash를 처리한다.

Q. Fallback UI도 오류가 날 수 있어?
A. 가능하다. Fallback UI는 의존성을 줄이고 단순하게 작성해야 한다.

Q. Form Error UX 검수에서 가장 중요한 것은?
A. Field Error와 Global Form Error를 구분하고 사용자가 오류를 수정할 수 있게 만드는 것이다.

Q. Route Error UX 검수에서 가장 중요한 것은?
A. Route 404, API 404, 401, 403을 구분하고 적절한 이동 또는 안내를 제공하는 것이다.

Q. Error Boundary 검수에서 가장 중요한 것은?
A. 렌더링 오류와 API 오류 역할을 구분하고 Fallback UI가 안전하게 표시되는지 확인하는 것이다.
