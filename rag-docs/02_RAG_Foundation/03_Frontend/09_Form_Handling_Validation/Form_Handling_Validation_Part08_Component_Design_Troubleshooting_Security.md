# Form Handling & Validation Part08 - Component Design, Troubleshooting, Security, Checklist

---

# 1. Form Component Design Foundation

## 1.1 Form Component Design Definition

### [개념]

Form Component Design은 Form UI, Form State, Validation, Submit Flow, Error UI, Request Mapping을 유지보수 가능한 Component 구조로 분리하는 설계 기준이다.

Form Component는 단순 input 묶음이 아니라 사용자 입력 흐름과 Backend API Contract를 연결하는 Frontend 경계 계층이다.

---

### [핵심]

Form Component Design 핵심 요소:

- Form Container
- Form Field Component
- Field Group
- Form State
- Validation
- Submit Handler
- Request Mapper
- Error Mapping
- Accessibility
- Reusable Field
- Domain Form
- Presentational Component
- Container Component
- Custom Hook
- API Contract

---

### [실무]

2026 실무 기준 Form Component는 아래 책임으로 분리한다.

```text
Form Container
→ data fetch
→ initial values
→ submit handler
→ API request
→ server error mapping

Form Component
→ form layout
→ field rendering
→ validation connection
→ submit button

Field Component
→ label
→ input
→ error message
→ accessibility props

Mapper
→ Form Values to Request DTO

Validator
→ Form Values to Error Object
```

권장 구조:

```text
features/signup/
├ components/
│ ├ SignupForm.tsx
│ ├ SignupFields.tsx
│ └ FormTextField.tsx
├ hooks/
│ └ useSignupForm.ts
├ mappers/
│ └ signupMapper.ts
├ validators/
│ └ signupValidator.ts
└ api/
  └ signupApi.ts
```

---

### [FAQ]

Q. Form Component Design이 뭐야?
A. Form 입력, 검증, 제출, 에러 처리, API 요청을 유지보수 가능한 구조로 분리하는 설계 기준이다.

Q. Form Component는 input만 모아둔 컴포넌트야?
A. 아니다. 사용자 입력과 Backend API Contract를 연결하는 중요한 Frontend 경계 계층이다.

Q. Form Component Design에서 가장 중요한 것은 뭐야?
A. UI, State, Validation, Mapping, API 요청 책임을 명확히 분리하는 것이다.

Q. 모든 Form을 복잡하게 분리해야 해?
A. 아니다. 단순 Form은 한 컴포넌트로 충분하고 복잡해질 때 분리한다.

---

# 2. Component Responsibility Rules

## 2.1 Form Container Responsibility

### [개념]

Form Container는 Form의 외부 데이터와 API 흐름을 담당하는 상위 Component다.

수정 Form의 상세 데이터 조회, 생성/수정 API 호출, 성공 후 이동, 서버 에러 mapping, Query Cache 갱신 등을 처리한다.

---

### [핵심]

Form Container 책임:

- fetch initial data
- build initial values
- submit API call
- server error mapping
- success handling
- redirect
- refetch
- cache invalidation
- permission check
- route param handling
- page-level state

---

### [실무]

Form Container 예:

```tsx
function ProfileEditContainer() {
  const { data: profile, refetch } = useProfileQuery();

  async function handleSubmit(requestBody) {
    await updateProfile(requestBody);
    await refetch();
  }

  if (!profile) {
    return <Loading />;
  }

  return (
    <ProfileEditForm
      initialValues={toProfileFormValues(profile)}
      onSubmit={handleSubmit}
    />
  );
}
```

권장:

- 서버 데이터 조회는 Container에서 처리
- Form Component에는 initialValues와 onSubmit 전달
- API 성공 후 refetch / redirect / toast 처리
- route param과 권한 체크는 Container에서 처리
- Form UI와 API 세부 구현 결합 최소화

---

### [FAQ]

Q. Form Container는 무엇을 담당해?
A. 서버 데이터 조회, API 요청, 성공 처리, 페이지 이동, 서버 에러 연결 같은 외부 흐름을 담당한다.

Q. Form Component 안에서 직접 API를 호출해도 돼?
A. 가능하지만 복잡한 Form은 Container와 Form을 분리하면 유지보수성이 좋아진다.

Q. 수정 Form의 초기값은 어디서 만들어?
A. Container에서 Server State를 Form Values로 변환해 전달하는 방식이 좋다.

Q. 권한 체크는 어디서 해?
A. 페이지 접근이나 route와 관련된 권한 체크는 Container에서 처리하는 것이 적합하다.

---

## 2.2 Form Component Responsibility

### [개념]

Form Component는 Form UI와 Form 내부 흐름을 담당한다.

입력 Field 렌더링, Client Validation 연결, Submit Button 상태, Field Error 표시, Accessibility 속성 연결을 처리한다.

---

### [핵심]

Form Component 책임:

- render form
- render fields
- manage form state
- connect validation
- handle submit event
- show field errors
- show global error
- submit button state
- accessibility props
- call onSubmit

---

### [실무]

Form Component 예:

```tsx
function ReviewForm({ initialValues, onSubmit }) {
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState({});
  const [submitError, setSubmitError] = useState("");
  const [submitting, setSubmitting] = useState(false);

  async function handleSubmit(event) {
    event.preventDefault();

    const nextErrors = validateReview(values);
    setErrors(nextErrors);

    if (Object.keys(nextErrors).length > 0) {
      return;
    }

    setSubmitting(true);

    try {
      await onSubmit(toCreateReviewRequest(values));
    } catch (error) {
      const mappedError = mapApiError(error);
      setErrors(mappedError.fieldErrors);
      setSubmitError(mappedError.globalError);
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <ReviewFields values={values} errors={errors} setValues={setValues} />
      {submitError && <p role="alert">{submitError}</p>}
      <button type="submit" disabled={submitting}>
        저장
      </button>
    </form>
  );
}
```

권장:

- Form UI와 Submit Flow 담당
- API 함수 자체보다 onSubmit callback 호출
- Field Component에 value/error/onChange 전달
- Error UI와 Accessibility 연결
- 너무 커지면 Fields, Button, Summary로 분리

---

### [FAQ]

Q. Form Component는 무엇을 담당해?
A. Form UI, 입력 상태, 검증 연결, submit 처리, 에러 표시를 담당한다.

Q. Form Component가 API URL을 알아야 해?
A. 가능하면 모르는 것이 좋다. onSubmit callback으로 분리하면 재사용성이 좋아진다.

Q. Form Component가 너무 커지면 어떻게 해?
A. Field Component, Field Group, custom hook, mapper, validator로 분리한다.

Q. Form Component에서 Accessibility도 처리해야 해?
A. 그렇다. label, aria-invalid, aria-describedby, error message 연결을 포함해야 한다.

---

## 2.3 Field Component Responsibility

### [개념]

Field Component는 하나의 입력 Field에 필요한 label, input, helper text, error message, 접근성 속성을 재사용 가능한 단위로 묶은 Component다.

Field Component는 Form 전체 Submit Flow를 알 필요가 없다.

---

### [핵심]

Field Component 책임:

- label rendering
- input rendering
- error rendering
- helper text
- id/htmlFor connection
- aria-invalid
- aria-describedby
- disabled
- required
- value/onChange
- checked/onChange
- field-level UI

---

### [실무]

TextField 예:

```tsx
type TextFieldProps = {
  id: string;
  name: string;
  label: string;
  value: string;
  error?: string;
  helperText?: string;
  required?: boolean;
  disabled?: boolean;
  onChange: (event: ChangeEvent<HTMLInputElement>) => void;
  onBlur?: (event: FocusEvent<HTMLInputElement>) => void;
};

function TextField({
  id,
  name,
  label,
  value,
  error,
  helperText,
  required = false,
  disabled = false,
  onChange,
  onBlur,
}: TextFieldProps) {
  const errorId = `${id}-error`;
  const helperId = `${id}-helper`;

  const describedBy =
    [helperText ? helperId : null, error ? errorId : null]
      .filter(Boolean)
      .join(" ") || undefined;

  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input
        id={id}
        name={name}
        value={value}
        required={required}
        disabled={disabled}
        onChange={onChange}
        onBlur={onBlur}
        aria-invalid={Boolean(error)}
        aria-describedby={describedBy}
      />
      {helperText && <p id={helperId}>{helperText}</p>}
      {error && (
        <p id={errorId} role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
```

권장:

- Field Component는 API 호출을 모름
- id와 label 연결을 반드시 처리
- error와 helper text 연결 기준 포함
- text, checkbox, select, file은 각각 별도 Component 검토
- Form Library를 쓰는 경우 register 또는 Controller 계약 명확화

---

### [FAQ]

Q. Field Component는 무엇을 담당해?
A. label, input, helper text, error message, 접근성 속성을 담당한다.

Q. Field Component가 submit handler를 알아야 해?
A. 아니다. Field Component는 field-level UI와 event 전달만 담당하는 것이 좋다.

Q. 모든 input을 하나의 Field Component로 만들면 좋아?
A. text 계열은 가능하지만 checkbox, radio, select, file은 제어 방식이 달라 분리하는 것이 좋다.

Q. Field Component에서 가장 중요한 접근성은 뭐야?
A. label 연결, aria-invalid, aria-describedby, error id 연결이다.

---

# 3. Custom Hook Rules

## 3.1 useForm Custom Hook

### [개념]

useForm Custom Hook은 Form State, Change Handler, Validation, Submit Flow를 Component 밖으로 분리하는 패턴이다.

Form Component의 JSX가 너무 길어지거나 동일한 Form Logic을 재사용해야 할 때 사용할 수 있다.

---

### [핵심]

Custom Hook 분리 대상:

- values
- errors
- touched
- submitting
- handleChange
- handleBlur
- handleSubmit
- resetForm
- setFieldError
- validate
- map server error

---

### [실무]

Custom Hook 예:

```tsx
function useReviewForm({ initialValues, onSubmit }) {
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState({});
  const [submitError, setSubmitError] = useState("");
  const [submitting, setSubmitting] = useState(false);

  function handleChange(event) {
    const { name, value } = event.target;

    setValues((prevValues) => ({
      ...prevValues,
      [name]: value,
    }));

    setErrors((prevErrors) => {
      const nextErrors = { ...prevErrors };
      delete nextErrors[name];
      return nextErrors;
    });
  }

  async function handleSubmit(event) {
    event.preventDefault();

    const nextErrors = validateReview(values);
    setErrors(nextErrors);

    if (Object.keys(nextErrors).length > 0) {
      return;
    }

    setSubmitting(true);

    try {
      await onSubmit(toCreateReviewRequest(values));
    } catch (error) {
      const mappedError = mapApiError(error);
      setErrors(mappedError.fieldErrors);
      setSubmitError(mappedError.globalError);
    } finally {
      setSubmitting(false);
    }
  }

  return {
    values,
    errors,
    submitError,
    submitting,
    handleChange,
    handleSubmit,
  };
}
```

권장:

- JSX와 Form Logic 분리
- Hook 이름은 `useXxxForm`
- Hook은 UI 렌더링하지 않음
- API callback은 인자로 주입
- 너무 범용적인 Hook보다 도메인별 Hook 우선

---

### [FAQ]

Q. Form Custom Hook은 언제 만들어?
A. Form Logic이 길어지거나 여러 Component에서 재사용해야 할 때 만든다.

Q. Custom Hook 안에서 JSX를 반환해도 돼?
A. 권장하지 않는다. Hook은 상태와 handler를 반환하고 UI는 Component가 담당한다.

Q. Custom Hook이 API를 직접 호출해도 돼?
A. 가능하지만 테스트와 재사용성을 위해 onSubmit callback을 주입하는 방식이 좋다.

Q. 모든 Form에 Custom Hook을 만들어야 해?
A. 아니다. 단순 Form은 Component 내부 state로 충분하다.

---

## 3.2 Mapper and Validator Separation

### [개념]

Mapper and Validator Separation은 Request Body 변환 함수와 Validation 함수를 Form Component 밖으로 분리하는 기준이다.

이 분리는 Backend DTO 변경, Validation 기준 변경, 테스트, RAG Retrieval에 유리하다.

---

### [핵심]

분리 대상:

- validateForm
- validateField
- toRequestBody
- toSearchParams
- toFormData
- toFormValues
- toInitialValues
- mapApiError
- fieldNameMap

---

### [실무]

파일 구조 예:

```text
review/
├ ReviewForm.tsx
├ reviewValidator.ts
├ reviewMapper.ts
└ reviewErrorMapper.ts
```

Validator:

```typescript
function validateReview(values: ReviewFormValues): ReviewFormErrors {
  const errors: ReviewFormErrors = {};

  if (!values.content.trim()) {
    errors.content = "리뷰 내용을 입력해 주세요.";
  }

  return errors;
}
```

Mapper:

```typescript
function toCreateReviewRequest(values: ReviewFormValues): CreateReviewRequest {
  return {
    content: values.content.trim(),
    rating: Number(values.rating),
  };
}
```

권장:

- validator는 검증만 담당
- mapper는 변환만 담당
- API 호출과 mapper 분리
- Backend DTO 이름과 mapper 이름 정렬
- 변경 영향 범위를 줄이기 위해 파일 분리

---

### [FAQ]

Q. Validator와 Mapper를 왜 분리해?
A. 검증 책임과 Request 변환 책임이 다르기 때문이다.

Q. validateForm 안에서 Request Body를 만들어도 돼?
A. 권장하지 않는다. 검증과 mapping이 섞이면 유지보수가 어려워진다.

Q. mapper 안에서 validation을 해도 돼?
A. 원칙적으로 validation 통과 후 mapper를 호출하는 것이 좋다.

Q. Mapper 파일 이름은 어떻게 짓는 게 좋아?
A. 도메인 기준으로 `reviewMapper`, `signupMapper`처럼 명확히 짓는 것이 좋다.

---

# 4. Reusable Field Component Rules

## 4.1 Text Field Component

### [개념]

Text Field Component는 text, email, password, search 같은 문자열 입력 Field를 재사용하기 위한 Component다.

label, input, error, helper text, disabled, required, accessibility props를 일관되게 제공한다.

---

### [핵심]

Text Field Props:

- id
- name
- type
- label
- value
- error
- helperText
- placeholder
- required
- disabled
- autoComplete
- maxLength
- onChange
- onBlur

---

### [실무]

TextField Props 예:

```typescript
type TextFieldProps = {
  id: string;
  name: string;
  type?: "text" | "email" | "password" | "search";
  label: string;
  value: string;
  error?: string;
  helperText?: string;
  required?: boolean;
  disabled?: boolean;
  autoComplete?: string;
  maxLength?: number;
  onChange: (event: ChangeEvent<HTMLInputElement>) => void;
  onBlur?: (event: FocusEvent<HTMLInputElement>) => void;
};
```

사용 예:

```tsx
<TextField
  id="email"
  name="email"
  type="email"
  label="이메일"
  value={values.email}
  error={errors.email}
  required
  autoComplete="email"
  onChange={handleChange}
/>
```

권장:

- type 기본값은 text
- password, email, search type 지원
- label 필수
- error와 helperText 접근성 연결
- autoComplete 명시
- Form Library register 방식과 일반 controlled 방식 중 하나 선택

---

### [FAQ]

Q. TextField Component는 무엇을 재사용해?
A. label, input, error message, helper text, accessibility props를 재사용한다.

Q. TextField에 label을 필수로 해야 해?
A. 권장한다. 접근성 기준을 기본으로 강제할 수 있다.

Q. password input도 TextField로 처리해도 돼?
A. 가능하다. type을 password로 전달하면 된다.

Q. TextField에 API 요청 로직을 넣어도 돼?
A. 넣지 않는 것이 좋다. Field Component는 UI와 event 전달만 담당한다.

---

## 4.2 Select Field Component

### [개념]

Select Field Component는 option 목록 중 하나를 선택하는 Field를 재사용하기 위한 Component다.

Frontend label과 Backend value를 분리하고, error와 접근성 속성을 포함한다.

---

### [핵심]

Select Field Props:

- id
- name
- label
- value
- options
- error
- placeholder option
- required
- disabled
- onChange
- option label
- option value

---

### [실무]

SelectField 예:

```tsx
type SelectOption = {
  label: string;
  value: string;
};

type SelectFieldProps = {
  id: string;
  name: string;
  label: string;
  value: string;
  options: SelectOption[];
  error?: string;
  required?: boolean;
  disabled?: boolean;
  placeholder?: string;
  onChange: (event: ChangeEvent<HTMLSelectElement>) => void;
};

function SelectField({
  id,
  name,
  label,
  value,
  options,
  error,
  required,
  disabled,
  placeholder = "선택해 주세요.",
  onChange,
}: SelectFieldProps) {
  const errorId = `${id}-error`;

  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <select
        id={id}
        name={name}
        value={value}
        required={required}
        disabled={disabled}
        onChange={onChange}
        aria-invalid={Boolean(error)}
        aria-describedby={error ? errorId : undefined}
      >
        <option value="">{placeholder}</option>
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
      {error && (
        <p id={errorId} role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
```

권장:

- option value는 Backend enum/code와 일치
- placeholder option은 빈 문자열 기준
- required 표시와 validation 일치
- label과 error 연결
- disabled 상태 기준 명확화

---

### [FAQ]

Q. SelectField options에는 무엇이 필요해?
A. 화면 표시용 label과 Backend 전송용 value가 필요하다.

Q. placeholder option value는 무엇이 좋아?
A. 보통 빈 문자열 `""`을 사용한다.

Q. SelectField value는 한글 label로 관리해도 돼?
A. 권장하지 않는다. Backend enum 또는 code 값을 value로 관리하는 것이 좋다.

Q. SelectField도 aria-invalid를 써야 해?
A. Field Error가 있으면 사용하는 것이 좋다.

---

## 4.3 Checkbox Field Component

### [개념]

Checkbox Field Component는 단일 boolean checkbox를 재사용하기 위한 Component다.

약관 동의, 알림 수신 여부, 공개 여부 같은 boolean 값에 사용한다.

---

### [핵심]

Checkbox Field Props:

- name
- label
- checked
- error
- helperText
- required
- disabled
- onChange
- boolean state
- aria-describedby

---

### [실무]

CheckboxField 예:

```tsx
type CheckboxFieldProps = {
  id: string;
  name: string;
  label: string;
  checked: boolean;
  error?: string;
  helperText?: string;
  required?: boolean;
  disabled?: boolean;
  onChange: (event: ChangeEvent<HTMLInputElement>) => void;
};

function CheckboxField({
  id,
  name,
  label,
  checked,
  error,
  helperText,
  required,
  disabled,
  onChange,
}: CheckboxFieldProps) {
  const errorId = `${id}-error`;
  const helperId = `${id}-helper`;

  const describedBy =
    [helperText ? helperId : null, error ? errorId : null]
      .filter(Boolean)
      .join(" ") || undefined;

  return (
    <div>
      <label htmlFor={id}>
        <input
          id={id}
          name={name}
          type="checkbox"
          checked={checked}
          required={required}
          disabled={disabled}
          onChange={onChange}
          aria-invalid={Boolean(error)}
          aria-describedby={describedBy}
        />
        {label}
      </label>

      {helperText && <p id={helperId}>{helperText}</p>}
      {error && (
        <p id={errorId} role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
```

권장:

- checked로 제어
- value로 boolean 제어 금지
- 필수 동의는 validation과 일치
- label로 클릭 영역 확장
- 단일 checkbox와 checkbox group 분리

---

### [FAQ]

Q. CheckboxField는 value를 써야 해 checked를 써야 해?
A. 선택 여부 제어에는 checked를 사용해야 한다.

Q. 약관 동의 checkbox는 CheckboxField로 만들 수 있어?
A. 가능하다. checked boolean과 required validation을 연결하면 된다.

Q. 여러 checkbox group도 같은 CheckboxField로 처리해?
A. 개별 항목은 재사용 가능하지만 group 상태는 배열 추가/제거 로직이 필요하다.

Q. CheckboxField에서 label이 input을 감싸도 돼?
A. 가능하다. 클릭 영역이 넓어져 UX가 좋아진다.

---

# 5. Domain Form Pattern Rules

## 5.1 Login Form Pattern

### [개념]

Login Form Pattern은 이메일과 비밀번호를 입력받아 인증 API에 제출하는 Form 패턴이다.

로그인 실패는 보통 Field Error보다 Global Error로 처리한다.

---

### [핵심]

Login Form 요소:

- email
- password
- Client Validation
- login request
- access token
- auth state
- global error
- 401 handling
- no password log
- submit loading

---

### [실무]

Login Submit Flow:

```text
Input Email / Password
→ Client Validation
→ Login Request
→ Success: Save Auth State
→ Failure 401: Show Global Error
→ Failure Network: Show Retry Message
```

Request Mapping:

```typescript
function toLoginRequest(values: LoginFormValues): LoginRequest {
  return {
    email: values.email.trim(),
    password: values.password,
  };
}
```

권장:

- email은 trim 가능
- password 임의 trim 주의
- 로그인 실패는 Global Error
- password console.log 금지
- 성공 후 Auth State 업데이트
- 인증 심화는 Authentication Frontend Flow Domain Rules로 연결

---

### [FAQ]

Q. 로그인 실패는 Field Error로 보여줘?
A. 보통 Global Error로 보여준다.

Q. 이메일 형식 오류는 어디에 보여줘?
A. email Field Error로 보여준다.

Q. password는 trim해서 보내?
A. 임의 trim은 권장하지 않는다. 서비스 정책에 따라 결정한다.

Q. 로그인 Form에서 가장 중요한 보안 기준은?
A. password와 token을 로그에 남기지 않는 것이다.

---

## 5.2 Signup Form Pattern

### [개념]

Signup Form Pattern은 회원가입에 필요한 여러 Field를 입력받고 Client Validation, 중복 확인, Server Validation Error를 처리하는 Form 패턴이다.

회원가입은 Form Handling에서 가장 대표적인 복합 Form이다.

---

### [핵심]

Signup Form 요소:

- email
- password
- confirmPassword
- nickname
- terms agreement
- duplicate email
- duplicate nickname
- Client Validation
- Server Validation
- Request Mapping
- 409 Conflict
- setError

---

### [실무]

Signup Flow:

```text
Input Signup Values
→ Client Validation
→ Password Confirm Validation
→ Optional Duplicate Check
→ Submit
→ Server Validation
→ Duplicate Error Mapping
→ Success Redirect Login
```

Request Mapping:

```typescript
function toSignupRequest(values: SignupFormValues): SignupRequest {
  return {
    email: values.email.trim(),
    password: values.password,
    nickname: values.nickname.trim(),
    termsAgreed: values.termsAgreed,
    marketingAgreed: values.marketingAgreed,
  };
}
```

권장:

- password confirm은 Request Body에서 제외 가능
- 필수 약관 동의 검증
- 중복 확인 결과 stale 처리
- submit 시 Backend 최종 중복 검증
- 409 duplicate error는 Field Error로 mapping
- 성공 후 로그인 페이지 이동 또는 자동 로그인 정책 결정

---

### [FAQ]

Q. Signup Form에서 confirmPassword도 API로 보내?
A. Backend 정책에 따라 다르지만 Frontend 검증용이면 Request Body에서 제외할 수 있다.

Q. 이메일 중복 확인을 했으면 submit 중복 검증은 생략해도 돼?
A. 아니다. submit 시 Backend 최종 검증은 유지해야 한다.

Q. 약관 동의는 Frontend만 검증하면 돼?
A. 아니다. 필수 동의는 Backend에서도 검증해야 한다.

Q. Signup Form에서 가장 중요한 에러 처리는?
A. Field Error, Duplicate Error, Global Error를 구분해 표시하는 것이다.

---

## 5.3 Search Filter Form Pattern

### [개념]

Search Filter Form Pattern은 키워드, 카테고리, 지역, 기간, 정렬 조건을 Query Params로 변환해 목록 조회에 사용하는 Form 패턴이다.

입력 중 값과 제출된 검색 조건을 분리할 수 있다.

---

### [핵심]

Search Filter 요소:

- keyword
- category
- regionCode
- themeCodes
- startDate
- endDate
- sort
- page reset
- Query Params
- empty omit
- URL State
- list fetch

---

### [실무]

Search Flow:

```text
User Input Filter
→ Submit Search Form
→ Validate Date Range
→ Build URLSearchParams
→ Omit Empty Values
→ Reset Page to 1
→ Update URL
→ Fetch List
```

Query Params Mapper:

```typescript
function toFestivalSearchParams(values: FestivalSearchValues): URLSearchParams {
  const params = new URLSearchParams();

  if (values.keyword.trim()) {
    params.set("keyword", values.keyword.trim());
  }

  if (values.regionCode) {
    params.set("regionCode", values.regionCode);
  }

  values.themeCodes.forEach((themeCode) => {
    params.append("themeCodes", themeCode);
  });

  if (values.startDate) {
    params.set("startDate", values.startDate);
  }

  if (values.endDate) {
    params.set("endDate", values.endDate);
  }

  params.set("page", "1");

  return params;
}
```

권장:

- 빈 값은 Query Params에서 제외
- 검색 조건 변경 시 page reset
- 날짜 범위 검증
- URL State와 Form State 동기화 기준 명확화
- Array Query Params 방식은 Backend와 통일

---

### [FAQ]

Q. Search Filter Form은 Request Body를 사용해?
A. 일반적인 목록 검색은 Query Params를 사용한다.

Q. 검색 조건 변경 시 page는 어떻게 해?
A. 대부분 1페이지로 reset한다.

Q. 빈 필터 값도 Query Params에 넣어?
A. 보통 제외한다.

Q. 다중 테마 필터는 어떻게 보내?
A. Backend 규칙에 따라 같은 key 반복 또는 comma-separated 방식으로 보낸다.

---

## 5.4 Review Form Pattern

### [개념]

Review Form Pattern은 평점, 내용, 이미지 등을 입력받아 리뷰 생성 또는 수정 API에 제출하는 Form 패턴이다.

숫자 검증, textarea 검증, 파일 검증, FormData Mapping이 함께 필요할 수 있다.

---

### [핵심]

Review Form 요소:

- rating
- content
- textarea
- maxLength
- image files
- file size
- file type
- FormData
- create review
- update review
- server field error

---

### [실무]

Review Validation:

```typescript
function validateReview(values: ReviewFormValues): ReviewFormErrors {
  const errors: ReviewFormErrors = {};

  const rating = Number(values.rating);

  if (Number.isNaN(rating) || rating < 1 || rating > 5) {
    errors.rating = "평점은 1점에서 5점 사이여야 합니다.";
  }

  if (!values.content.trim()) {
    errors.content = "리뷰 내용을 입력해 주세요.";
  }

  if (values.content.trim().length > 500) {
    errors.content = "리뷰 내용은 500자 이하로 입력해 주세요.";
  }

  return errors;
}
```

Review Request Mapping:

```typescript
function toCreateReviewRequest(values: ReviewFormValues): CreateReviewRequest {
  return {
    rating: Number(values.rating),
    content: values.content.trim(),
  };
}
```

Review FormData Mapping:

```typescript
function toReviewFormData(values: ReviewFormValues): FormData {
  const formData = new FormData();

  formData.append("rating", String(Number(values.rating)));
  formData.append("content", values.content.trim());

  values.images.forEach((image) => {
    formData.append("images", image);
  });

  return formData;
}
```

권장:

- rating은 Number 변환 전 validation
- content는 trim 후 required / max length 검증
- 이미지 optional 여부 명확화
- 파일 크기와 타입 검증
- multipart field name과 Backend 일치
- 수정 성공 후 최신 리뷰 데이터 반영

---

### [FAQ]

Q. Review Form에서 rating은 문자열이야 숫자야?
A. input 값은 문자열일 수 있으므로 validation 후 Number로 변환해 Request에 담는다.

Q. 리뷰 내용은 trim해야 해?
A. 보통 submit 시 trim하고 공백만 입력한 값은 invalid 처리한다.

Q. 리뷰 이미지가 있으면 JSON으로 보내?
A. 파일이 포함되면 보통 FormData multipart 요청을 사용한다.

Q. Review Form에서 가장 중요한 검증은?
A. rating 범위, content 필수/길이, 파일 크기/타입 검증이다.

---

# 6. Form Troubleshooting Rules

## 6.1 Input Not Updating

### [개념]

Input Not Updating은 사용자가 입력해도 화면 값이 바뀌지 않는 문제다.

Controlled Component에서 value와 onChange 연결이 잘못되었거나 name-key mapping이 어긋났을 때 자주 발생한다.

---

### [핵심]

주요 원인:

- value exists but onChange missing
- setState missing
- name mismatch
- values key mismatch
- direct mutation
- disabled true
- readOnly true
- undefined initial value
- wrong checked/value usage
- custom component event missing

---

### [실무]

Debug Flow:

```text
value 확인
→ onChange 연결 확인
→ setState 호출 확인
→ event.target.name 확인
→ values key 확인
→ direct mutation 확인
→ disabled/readOnly 확인
→ checkbox checked 확인
→ custom component props 확인
```

문제 예:

```tsx
<input value={values.email} />
```

수정:

```tsx
<input name="email" value={values.email} onChange={handleChange} />
```

name 불일치 문제:

```tsx
<input name="userEmail" value={values.email} onChange={handleChange} />
```

공통 handler는 `values.userEmail`을 업데이트하고 `values.email`은 유지될 수 있다.

---

### [FAQ]

Q. input에 입력이 안 되는 이유는?
A. value만 있고 onChange가 없거나 setState가 올바르게 실행되지 않을 가능성이 크다.

Q. name과 values key가 다르면 왜 문제야?
A. 공통 handler가 다른 key를 업데이트해 화면 value가 바뀌지 않을 수 있다.

Q. setState를 했는데 화면이 안 바뀌어?
A. State를 직접 mutation하고 같은 객체를 다시 넣었는지 확인해야 한다.

Q. checkbox가 안 바뀌는 이유는?
A. checked가 아니라 value로 제어했거나 onChange에서 checked를 반영하지 않았을 수 있다.

---

## 6.2 Submit Not Working

### [개념]

Submit Not Working은 Form 제출 이벤트가 실행되지 않거나 API 요청이 발생하지 않는 문제다.

form onSubmit 누락, button type 오류, validation early return, disabled 상태가 주요 원인이다.

---

### [핵심]

주요 원인:

- form onSubmit missing
- button type button
- disabled submit button
- handleSubmit not connected
- preventDefault issue
- validation always fails
- early return
- API call missing
- immediate function call
- Network Tab no request

---

### [실무]

Debug Flow:

```text
form onSubmit 확인
→ button type 확인
→ handleSubmit 실행 로그 확인
→ disabled 조건 확인
→ validation result 확인
→ early return 확인
→ API function 호출 확인
→ Network 요청 확인
```

문제 예:

```tsx
<form onSubmit={handleSubmit()}>
```

수정:

```tsx
<form onSubmit={handleSubmit}>
```

문제 예:

```tsx
<button type="button">저장</button>
```

수정:

```tsx
<button type="submit">저장</button>
```

---

### [FAQ]

Q. 버튼을 눌러도 submit이 안 돼?
A. form onSubmit, button type, disabled 상태, validation return을 확인해야 한다.

Q. Network 요청이 안 보여?
A. submit handler가 실행되지 않았거나 validation에서 중단되었을 수 있다.

Q. onSubmit={handleSubmit()}은 왜 문제야?
A. 렌더링 시 함수가 즉시 실행될 수 있으므로 함수 참조를 전달해야 한다.

Q. submit button이 type="button"이면 어떻게 돼?
A. Form submit이 발생하지 않는다.

---

## 6.3 Validation Error Not Showing

### [개념]

Validation Error Not Showing은 검증 실패가 발생했지만 Field Error 또는 Global Error가 UI에 표시되지 않는 문제다.

errors key 불일치, rendering 조건 오류, touched/submitted 조건, server error mapping 실패가 주요 원인이다.

---

### [핵심]

주요 원인:

- setErrors missing
- setError missing
- errors key mismatch
- input name mismatch
- error rendering condition false
- touched condition false
- submitted missing
- server response path mismatch
- error.message missing

---

### [실무]

Debug Flow:

```text
Validation Result 확인
→ setErrors/setError 호출 확인
→ errors 객체 확인
→ errors key와 input name 비교
→ rendering 조건 확인
→ touched/submitted 조건 확인
→ Server Error Mapping 확인
```

문제 예:

```typescript
errors.userEmail = "이메일을 입력해 주세요.";
```

UI:

```tsx
{
  errors.email && <p>{errors.email}</p>;
}
```

수정:

```typescript
errors.email = "이메일을 입력해 주세요.";
```

---

### [FAQ]

Q. Validation은 실패했는데 에러가 안 보여?
A. errors key와 UI에서 참조하는 key가 일치하는지 확인해야 한다.

Q. touched 때문에 에러가 안 보일 수 있어?
A. 가능하다. submit 후에는 submitted 기준으로 전체 에러를 표시할 수 있다.

Q. React Hook Form에서 error.message가 안 보여?
A. validation rule에 message가 없거나 setError에 message가 누락되었을 수 있다.

Q. 서버 에러가 안 보이면 무엇을 확인해?
A. 서버 응답 구조, Error Mapping 함수, setErrors/setError 호출 여부를 확인한다.

---

## 6.4 Request Body Wrong

### [개념]

Request Body Wrong은 Frontend가 Backend DTO와 다른 field name, type, structure로 요청을 보내는 문제다.

Backend Validation Error, 400 Bad Request, 값 null 저장의 원인이 된다.

---

### [핵심]

주요 원인:

- field name mismatch
- type mismatch
- number string issue
- boolean string issue
- enum mismatch
- date format mismatch
- nested object mismatch
- array params mismatch
- FormData key mismatch
- null handling mismatch

---

### [실무]

Debug Flow:

```text
Network Payload 확인
→ Backend DTO 확인
→ field name 비교
→ type 비교
→ required field 누락 확인
→ enum/code 확인
→ null/empty 기준 확인
→ FormData key 확인
```

문제 예:

```typescript
const requestBody = {
  reviewContent: values.content,
  score: values.rating,
};
```

Backend DTO:

```java
private String content;
private Integer rating;
```

수정:

```typescript
const requestBody = {
  content: values.content.trim(),
  rating: Number(values.rating),
};
```

---

### [FAQ]

Q. Request Body가 틀렸는지 어떻게 확인해?
A. 브라우저 Network 탭의 Payload와 Backend DTO를 비교한다.

Q. field name이 다르면 어떻게 돼?
A. Backend에서 값이 null로 들어가거나 validation error가 발생할 수 있다.

Q. 숫자를 문자열로 보내도 돼?
A. Backend가 변환할 수도 있지만 DTO가 number를 기대하면 명시 변환이 안전하다.

Q. FormData key가 틀리면 어떻게 돼?
A. Backend가 파일이나 값을 받지 못할 수 있다.

---

# 7. Server Error Troubleshooting Rules

## 7.1 Server Error Not Showing

### [개념]

Server Error Not Showing은 Backend가 오류 응답을 반환했지만 Frontend Form UI에 메시지가 표시되지 않는 문제다.

Error Response 구조와 Frontend Error Mapping 기준이 맞지 않을 때 발생한다.

---

### [핵심]

주요 원인:

- response.data path mismatch
- errors object missing
- message missing
- catch block missing
- interceptor swallowed error
- field name mismatch
- setErrors not called
- setSubmitError not called
- setError wrong name

---

### [실무]

Debug Flow:

```text
Network Response 확인
→ status 확인
→ response.data 확인
→ mapApiError 결과 확인
→ catch 실행 확인
→ setErrors/setSubmitError 확인
→ UI rendering 확인
→ interceptor throw 확인
```

문제 예:

```typescript
const fieldErrors = error.response?.data?.fieldErrors;
```

서버 응답:

```json
{
  "errors": {
    "email": "이미 사용 중인 이메일입니다."
  },
  "message": "검증 실패"
}
```

수정:

```typescript
const fieldErrors = error.response?.data?.errors ?? {};
```

---

### [FAQ]

Q. 서버 에러가 화면에 안 보여?
A. 서버 응답 구조와 Frontend Error Mapping 경로가 맞는지 확인해야 한다.

Q. Network 탭에는 에러가 있는데 UI에는 없어?
A. catch block, mapping 함수, setErrors/setSubmitError, rendering 조건을 확인해야 한다.

Q. interceptor 때문에 Form catch가 실행되지 않을 수 있어?
A. 가능하다. interceptor가 error를 처리한 뒤 throw하지 않으면 catch에 도달하지 않을 수 있다.

Q. 서버 message만 있고 errors가 없으면?
A. submitError 같은 Global Error로 표시해야 한다.

---

## 7.2 HTTP Status Misclassification

### [개념]

HTTP Status Misclassification은 Backend가 오류 상황에 맞지 않는 status code를 반환하거나 Frontend가 status code를 잘못 해석하는 문제다.

Error UX와 분기 처리가 불안정해진다.

---

### [핵심]

상태 코드 기준:

- 400 validation
- 401 unauthenticated
- 403 forbidden
- 404 not found
- 409 conflict
- 422 semantic validation
- 500 server error
- status mapping
- API convention

---

### [실무]

권장 mapping:

```text
400
→ DTO Validation / Bad Request
→ Field Error 가능

401
→ 인증 없음 / 토큰 만료 / 로그인 실패
→ Auth Flow 또는 Global Error

403
→ 권한 없음
→ Global Error 또는 Redirect

404
→ 대상 없음
→ Not Found UI 또는 Global Error

409
→ 중복 / 상태 충돌
→ Field Error 또는 Global Error

500
→ 서버 오류
→ Fallback Global Error
```

주의:

- 팀 API 컨벤션 통일
- 모든 validation error를 200으로 반환하지 않음
- Frontend는 status와 code를 함께 활용 가능
- 로그인 실패와 토큰 만료 code 구분 권장
- 내부 서버 오류는 사용자에게 상세 노출 금지

---

### [FAQ]

Q. Validation Error를 200으로 반환해도 돼?
A. 권장하지 않는다. 실패는 적절한 4xx status로 표현하는 것이 좋다.

Q. 중복 이메일은 어떤 status가 좋아?
A. 팀 규칙에 따라 400 또는 409를 사용할 수 있지만 409 Conflict가 의미상 적합한 경우가 많다.

Q. 401과 403 차이는 뭐야?
A. 401은 인증이 없거나 유효하지 않은 상태이고 403은 인증은 되었지만 권한이 없는 상태다.

Q. Frontend는 status만 보고 처리하면 돼?
A. status와 code를 함께 보면 더 명확한 분기 처리가 가능하다.

---

# 8. Security Rules

## 8.1 Sensitive Input Protection

### [개념]

Sensitive Input Protection은 password, token, 개인정보, 결제 정보, 파일 내용 같은 민감한 Form 입력값을 노출하지 않는 기준이다.

Form Debugging, Error Logging, Console Logging, UI Error Message에서 민감정보가 새지 않도록 한다.

---

### [핵심]

보호 대상:

- password
- confirmPassword
- access token
- refresh token
- authorization header
- phone
- address
- personal information
- payment information
- file content
- resident number
- private message

---

### [실무]

나쁜 예:

```typescript
console.log(values);
console.log(values.password);
console.log(error.config.headers.Authorization);
```

좋은 예:

```typescript
console.log({
  formName: "SignupForm",
  status: error.response?.status,
  code: error.response?.data?.code,
});
```

권장:

- Form 전체 values 로그 금지
- password/token 로그 금지
- Authorization header 로그 금지
- 개발 중에도 민감정보 마스킹
- 운영 환경 console log 제거
- Error 객체 전체 출력 주의

---

### [FAQ]

Q. Form values를 console.log 해도 돼?
A. 권장하지 않는다. password나 개인정보가 포함될 수 있다.

Q. password를 디버깅 로그로 찍어도 돼?
A. 안 된다. 민감정보는 로그에 남기지 않는다.

Q. Authorization header를 로그로 남겨도 돼?
A. 안 된다. Access Token이 노출될 수 있다.

Q. 디버깅할 때는 무엇을 로그로 남겨?
A. status, code, form name처럼 민감하지 않은 정보만 남긴다.

---

## 8.2 Error Message Security

### [개념]

Error Message Security는 Form Error UI에 서버 내부 정보, 예외명, SQL 정보, 인증 상세 정보를 노출하지 않는 기준이다.

사용자에게 필요한 수정 정보만 전달하고 내부 구현 정보는 숨겨야 한다.

---

### [핵심]

노출 금지:

- stack trace
- exception class
- SQL error
- table name
- column name
- package name
- server file path
- token detail
- password rule internal detail
- infrastructure detail

---

### [실무]

나쁜 메시지:

```text
SQLIntegrityConstraintViolationException: Duplicate entry...
NullPointerException at com.example.UserService...
JWT signature does not match locally computed signature...
```

좋은 메시지:

```text
이미 사용 중인 이메일입니다.
요청을 처리하지 못했습니다. 잠시 후 다시 시도해 주세요.
로그인 세션이 만료되었습니다. 다시 로그인해 주세요.
```

권장:

- Backend에서 사용자용 message 생성
- Frontend에서 fallback message 제공
- 내부 오류 상세 노출 금지
- 인증 실패 메시지는 과도하게 구체화하지 않음
- traceId는 운영 문의용으로 제한적 표시 가능

---

### [FAQ]

Q. 서버 예외 메시지를 그대로 보여줘도 돼?
A. 안 된다. 내부 정보와 보안 정보가 노출될 수 있다.

Q. SQL 오류를 사용자에게 보여줘도 돼?
A. 안 된다. 사용자 친화 메시지로 변환해야 한다.

Q. 로그인 실패 원인을 자세히 보여줘도 돼?
A. 보안 정책에 따라 제한하는 것이 좋다.

Q. 500 오류는 어떻게 보여줘?
A. “서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.” 같은 fallback 메시지가 적합하다.

---

## 8.3 Client Validation Security Limitation

### [개념]

Client Validation Security Limitation은 Frontend Validation이 보안 검증이 될 수 없다는 기준이다.

사용자는 브라우저 DevTools, API Client, Script를 통해 Frontend Validation을 우회할 수 있다.

---

### [핵심]

Client Validation 한계:

- can be bypassed
- DevTools modification
- API direct request
- disabled button bypass
- hidden input manipulation
- maxLength bypass
- file accept bypass
- Backend validation required
- authorization required

---

### [실무]

우회 가능한 Frontend 제한:

```text
input maxLength
button disabled
hidden field
select option
checkbox required
file accept
Client Validation Function
```

Backend 필수 검증:

```text
DTO Validation
Business Rule Validation
Authorization Check
Duplicate Check
File Validation
Rate Limit
Ownership Check
Payment Validation
```

권장:

- Frontend Validation은 UX 개선용
- Backend Validation은 최종 기준
- 권한 검증은 Backend 필수
- 파일 검증은 Backend 필수
- 결제/주문/예약은 Backend 중복 방지 필수

---

### [FAQ]

Q. Client Validation은 보안 검증이야?
A. 아니다. Client Validation은 UX용이며 쉽게 우회될 수 있다.

Q. button disabled로 요청을 막으면 안전해?
A. 아니다. API 직접 요청으로 우회할 수 있다.

Q. maxLength를 걸면 Backend 길이 검증은 없어도 돼?
A. 아니다. maxLength는 우회될 수 있으므로 Backend 검증이 필요하다.

Q. 파일 accept 속성으로 파일 타입 검증은 충분해?
A. 아니다. Backend에서 파일 타입과 크기 검증을 반드시 해야 한다.

---

# 9. Performance and UX Rules

## 9.1 Re-render Control

### [개념]

Re-render Control은 Form 입력 중 불필요한 렌더링을 줄이고 입력 UX를 안정적으로 유지하는 기준이다.

필드가 많은 Form에서는 State 위치, Form Library 사용, Component 분리가 중요해진다.

---

### [핵심]

Re-render 원인:

- large form state object
- parent state update
- watch all fields
- inline object props
- heavy validation onChange
- expensive derived UI
- uncontrolled library benefit
- memoization caution

---

### [실무]

권장:

```text
간단한 Form
→ useState로 충분

필드 많은 Form
→ React Hook Form 검토

onChange 검증 무거움
→ debounce 또는 submit/onBlur 검증

미리보기 무거움
→ 필요한 field만 watch/useWatch

Field Component 많음
→ props 구조 단순화
```

주의:

- 성능 최적화보다 correctness 우선
- 불필요한 전역 상태 저장 금지
- watch 전체 Form 남용 금지
- validation function이 매 입력마다 무겁게 돌지 않게 함
- API validation은 debounce 또는 명시 버튼 검토

---

### [FAQ]

Q. Form 입력이 느리면 무엇을 확인해?
A. onChange마다 무거운 validation, 전체 Form re-render, watch 남용, 큰 Component 구조를 확인한다.

Q. React Hook Form이 성능에 유리한 이유는?
A. uncontrolled 기반 관리로 불필요한 re-render를 줄일 수 있기 때문이다.

Q. 모든 Form에서 memo를 써야 해?
A. 아니다. 문제가 있는 지점을 확인한 뒤 적용하는 것이 좋다.

Q. onChange마다 API 검증을 해도 돼?
A. 가능하지만 debounce나 명시적 확인 버튼을 고려해야 한다.

---

## 9.2 User Feedback UX

### [개념]

User Feedback UX는 Form 제출, 검증, 성공, 실패 상태를 사용자가 명확히 이해할 수 있도록 알려주는 기준이다.

Form은 사용자가 지금 무엇을 해야 하는지 알려줘야 한다.

---

### [핵심]

Feedback 요소:

- field error
- global error
- loading state
- disabled state
- success message
- toast
- helper text
- character count
- duplicate check status
- focus invalid field
- retry message

---

### [실무]

권장 Feedback:

```text
입력 전
→ helper text / required 표시

입력 중
→ character count / optional validation

blur 후
→ field validation error

submit 중
→ disabled button / loading label

submit 실패
→ field error / global error / keep values

submit 성공
→ toast / redirect / reset / list refresh
```

주의:

- 에러만 보여주고 해결 방법을 숨기지 않음
- loading 상태 없이 요청 보내지 않음
- 성공 후 변화가 없으면 사용자가 혼란스러움
- 실패 후 입력값 reset 금지
- 중복 확인 상태는 현재 입력값과 일치해야 함

---

### [FAQ]

Q. Form UX에서 가장 중요한 피드백은 뭐야?
A. 에러 메시지, 제출 중 상태, 성공 후 결과, 재시도 가능 여부다.

Q. submit 중에는 무엇을 보여줘?
A. 버튼 disabled와 “처리 중...” 같은 loading label을 제공하는 것이 좋다.

Q. submit 성공 후 아무 변화가 없어도 돼?
A. 권장하지 않는다. toast, reset, redirect, 목록 갱신 등 결과를 알려야 한다.

Q. 중복 확인 결과는 언제 무효화해?
A. 사용자가 해당 값을 수정하면 기존 중복 확인 결과를 무효화해야 한다.

---

# 10. File and Directory Naming Rules

## 10.1 Naming Convention

### [개념]

Naming Convention은 Form 관련 파일과 함수의 이름을 일관되게 정하는 기준이다.

RAG Retrieval과 Agent 코드 생성 정확도를 높이기 위해 도메인명, 목적, 역할이 드러나는 이름을 사용한다.

---

### [핵심]

이름 기준:

- DomainForm
- DomainFormValues
- DomainFormErrors
- DomainRequest
- validateDomain
- toDomainRequest
- mapDomainError
- useDomainForm
- DomainField
- initialValues
- defaultValues

---

### [실무]

권장 이름:

```text
SignupForm.tsx
SignupFormValues
SignupFormErrors
SignupRequest
validateSignup
toSignupRequest
mapSignupServerErrors
useSignupForm
```

Review 예:

```text
ReviewForm.tsx
ReviewFormValues
ReviewFormErrors
CreateReviewRequest
validateReview
toCreateReviewRequest
toReviewFormData
```

주의:

- `data`, `form`, `submitData` 같은 모호한 이름 지양
- Request DTO와 Form Values 이름 구분
- mapper 함수는 `toXxxRequest`
- validator 함수는 `validateXxx`
- Server State 변환은 `toXxxFormValues`

---

### [FAQ]

Q. Form 관련 이름은 어떻게 짓는 게 좋아?
A. 도메인명과 역할이 드러나게 `SignupForm`, `validateSignup`, `toSignupRequest`처럼 짓는다.

Q. Form Values와 Request DTO 이름을 구분해야 해?
A. 구분하는 것이 좋다. 화면 입력 상태와 API 요청 구조는 다를 수 있다.

Q. mapper 함수 이름은 어떻게 짓는 게 좋아?
A. `toCreateReviewRequest`, `toSignupRequest`처럼 Request DTO 변환 목적을 드러낸다.

Q. validator 함수 이름은 어떻게 짓는 게 좋아?
A. `validateReview`, `validateSignup`처럼 도메인 기준으로 짓는다.

---

# 11. Final Integration Checklist

## 11.1 Form Handling Final Checklist

### [개념]

Form Handling Final Checklist는 Form Basics, Form State, Input Handling, Validation, Server Error Handling, Submit Flow, React Hook Form, Accessibility, Component Design을 최종 통합 검수하는 기준이다.

---

### [핵심]

Final Checklist:

```md
- [ ] form onSubmit이 사용되었는가?
- [ ] preventDefault 또는 handleSubmit wrapper가 적용되었는가?
- [ ] submit button type="submit"이 명시되었는가?
- [ ] 일반 button type="button"이 명시되었는가?
- [ ] 모든 Controlled Input에 value/onChange가 연결되었는가?
- [ ] checkbox는 checked 기준으로 처리되는가?
- [ ] radio group은 같은 name을 사용하는가?
- [ ] select option value가 Backend enum/code와 일치하는가?
- [ ] file input은 files/FormData 기준으로 처리되는가?
- [ ] Form Values 초기값이 명확한가?
- [ ] values와 errors가 분리되어 있는가?
- [ ] touched/dirty/submitting 상태가 필요한 경우 정의되었는가?
- [ ] Client Validation이 API 요청 전에 실행되는가?
- [ ] Client Validation 실패 시 API 요청이 중단되는가?
- [ ] Server Validation Error Mapping 기준이 있는가?
- [ ] Field Error와 Global Error가 구분되는가?
- [ ] Backend DTO field와 Frontend field name이 정렬되어 있는가?
- [ ] Request Body Mapping 함수가 분리되었는가?
- [ ] trim/type conversion/null handling 기준이 명확한가?
- [ ] Query Params에서 빈 값 제외와 page reset 기준이 있는가?
- [ ] FormData key가 Backend multipart field name과 일치하는가?
- [ ] submitting 또는 isSubmitting으로 중복 제출을 방지하는가?
- [ ] API 성공 후 reset/refetch/redirect/toast 기준이 있는가?
- [ ] API 실패 후 Form Values를 유지하는가?
- [ ] label htmlFor와 input id가 연결되어 있는가?
- [ ] placeholder를 label 대체로 사용하지 않는가?
- [ ] aria-invalid와 aria-describedby가 error와 연결되어 있는가?
- [ ] role alert가 필요한 Error Message에 적용되어 있는가?
- [ ] keyboard navigation이 가능한가?
- [ ] focus visible이 유지되는가?
- [ ] password/token/개인정보를 console.log 하지 않는가?
- [ ] 서버 예외명, SQL 오류, stack trace를 사용자에게 노출하지 않는가?
- [ ] Form Component 책임이 너무 커지면 Field/Hook/Mapper/Validator로 분리했는가?
```

---

### [실무]

최종 검수 Flow:

```text
Structure Check
→ State Check
→ Input Handling Check
→ Validation Check
→ Submit Flow Check
→ Request Mapping Check
→ Server Error Mapping Check
→ Accessibility Check
→ Security Check
→ Troubleshooting Check
→ Retrieval Query Check
```

---

### [FAQ]

Q. Form 최종 검수에서 가장 중요한 것은?
A. 입력 처리, 검증, 요청 변환, 서버 에러 처리, 접근성, 보안 기준이 모두 연결되어 있는지 확인하는 것이다.

Q. Form이 작으면 모든 체크리스트를 적용해야 해?
A. 핵심 항목은 적용하되, 복잡한 상태나 분리는 필요할 때만 적용한다.

Q. Form 검수에서 자주 놓치는 것은?
A. button type, checkbox checked, Request Body type conversion, server error mapping, aria-describedby, password log 금지다.

Q. Form 문서가 끝난 뒤 다음 Domain은 뭐가 좋아?
A. Authentication Frontend Flow 또는 Error Handling & Loading UX로 연결하는 것이 적합하다.

---

# 12. RAG Retrieval Optimization Rules

## 12.1 Retrieval Keyword Coverage

### [개념]

Retrieval Keyword Coverage는 Agent가 Form 관련 문제를 검색할 때 다양한 표현으로 정확히 문서를 찾을 수 있도록 핵심 용어와 동의어를 문서에 포함하는 기준이다.

Form Handling 문서는 코드 생성, 디버깅, 검수, 리팩터링 요청에서 자주 검색된다.

---

### [핵심]

검색 키워드 묶음:

- React Form
- Form Handling
- Form State
- Controlled Component
- Uncontrolled Component
- onChange
- onBlur
- onSubmit
- preventDefault
- Validation
- Client Validation
- Server Validation Error
- Request Body Mapping
- FormData
- React Hook Form
- Accessibility
- aria-invalid
- aria-describedby
- role alert
- Duplicate Submit
- Error Mapping
- Field Error
- Global Error

---

### [실무]

Agent Retrieval 예상 질의:

```text
React input 값이 안 바뀜
React form submit 안 됨
checkbox 값 이상함
React Hook Form 서버 에러 표시
FormData 파일 업로드 안 됨
Request Body DTO 안 맞음
Validation 에러 안 보임
button 누르면 페이지 새로고침됨
select enum mapping 문제
검색 조건 query param 변환
회원가입 이메일 중복 에러 표시
Form 접근성 label aria-describedby
```

문서 작성 기준:

- 문제 표현과 해결 표현을 FAQ에 함께 포함
- Backend DTO, Request Body, Error Response 키워드 포함
- React Hook Form과 useState Form을 모두 검색 가능하게 작성
- Field Error / Global Error 용어 반복
- Troubleshooting 질문을 Retrieval Queries에 강화

---

### [FAQ]

Q. RAG Retrieval Optimization은 왜 필요해?
A. Agent가 Form 관련 문제를 정확한 chunk에서 찾도록 검색 키워드와 FAQ를 강화하기 위해 필요하다.

Q. Form 문서에서 꼭 들어가야 할 검색 키워드는?
A. onChange, onSubmit, Validation, Request Body Mapping, Server Error, React Hook Form, Accessibility가 중요하다.

Q. Troubleshooting FAQ가 중요한 이유는?
A. 실제 Agent 요청은 “submit 안 됨”, “input 안 바뀜” 같은 문제 상황으로 들어오는 경우가 많기 때문이다.

Q. Form Handling 문서는 어떤 다음 문서와 연결돼?
A. Authentication Frontend Flow, Error Handling & Loading UX, Data Fetching & REST API Integration과 연결된다.

---

# Retrieval Queries

### [FAQ]

Q. Form Component Design이 뭐야?
A. Form 입력, 검증, 제출, 에러 처리, API 요청을 유지보수 가능한 구조로 분리하는 설계 기준이다.

Q. Form Component는 input만 모아둔 컴포넌트야?
A. 아니다. 사용자 입력과 Backend API Contract를 연결하는 중요한 Frontend 경계 계층이다.

Q. Form Component Design에서 가장 중요한 것은 뭐야?
A. UI, State, Validation, Mapping, API 요청 책임을 명확히 분리하는 것이다.

Q. 모든 Form을 복잡하게 분리해야 해?
A. 아니다. 단순 Form은 한 컴포넌트로 충분하고 복잡해질 때 분리한다.

Q. Form Container는 무엇을 담당해?
A. 서버 데이터 조회, API 요청, 성공 처리, 페이지 이동, 서버 에러 연결 같은 외부 흐름을 담당한다.

Q. Form Component 안에서 직접 API를 호출해도 돼?
A. 가능하지만 복잡한 Form은 Container와 Form을 분리하면 유지보수성이 좋아진다.

Q. 수정 Form의 초기값은 어디서 만들어?
A. Container에서 Server State를 Form Values로 변환해 전달하는 방식이 좋다.

Q. Form Component는 무엇을 담당해?
A. Form UI, 입력 상태, 검증 연결, submit 처리, 에러 표시를 담당한다.

Q. Form Component가 API URL을 알아야 해?
A. 가능하면 모르는 것이 좋다. onSubmit callback으로 분리하면 재사용성이 좋아진다.

Q. Form Component가 너무 커지면 어떻게 해?
A. Field Component, Field Group, custom hook, mapper, validator로 분리한다.

Q. Field Component는 무엇을 담당해?
A. label, input, helper text, error message, 접근성 속성을 담당한다.

Q. Field Component가 submit handler를 알아야 해?
A. 아니다. Field Component는 field-level UI와 event 전달만 담당하는 것이 좋다.

Q. 모든 input을 하나의 Field Component로 만들면 좋아?
A. text 계열은 가능하지만 checkbox, radio, select, file은 제어 방식이 달라 분리하는 것이 좋다.

Q. Field Component에서 가장 중요한 접근성은 뭐야?
A. label 연결, aria-invalid, aria-describedby, error id 연결이다.

Q. Form Custom Hook은 언제 만들어?
A. Form Logic이 길어지거나 여러 Component에서 재사용해야 할 때 만든다.

Q. Custom Hook 안에서 JSX를 반환해도 돼?
A. 권장하지 않는다. Hook은 상태와 handler를 반환하고 UI는 Component가 담당한다.

Q. Custom Hook이 API를 직접 호출해도 돼?
A. 가능하지만 테스트와 재사용성을 위해 onSubmit callback을 주입하는 방식이 좋다.

Q. Validator와 Mapper를 왜 분리해?
A. 검증 책임과 Request 변환 책임이 다르기 때문이다.

Q. validateForm 안에서 Request Body를 만들어도 돼?
A. 권장하지 않는다. 검증과 mapping이 섞이면 유지보수가 어려워진다.

Q. mapper 안에서 validation을 해도 돼?
A. 원칙적으로 validation 통과 후 mapper를 호출하는 것이 좋다.

Q. TextField Component는 무엇을 재사용해?
A. label, input, error message, helper text, accessibility props를 재사용한다.

Q. TextField에 label을 필수로 해야 해?
A. 권장한다. 접근성 기준을 기본으로 강제할 수 있다.

Q. password input도 TextField로 처리해도 돼?
A. 가능하다. type을 password로 전달하면 된다.

Q. SelectField options에는 무엇이 필요해?
A. 화면 표시용 label과 Backend 전송용 value가 필요하다.

Q. SelectField value는 한글 label로 관리해도 돼?
A. 권장하지 않는다. Backend enum 또는 code 값을 value로 관리하는 것이 좋다.

Q. CheckboxField는 value를 써야 해 checked를 써야 해?
A. 선택 여부 제어에는 checked를 사용해야 한다.

Q. 여러 checkbox group도 같은 CheckboxField로 처리해?
A. 개별 항목은 재사용 가능하지만 group 상태는 배열 추가/제거 로직이 필요하다.

Q. 로그인 실패는 Field Error로 보여줘?
A. 보통 Global Error로 보여준다.

Q. 이메일 형식 오류는 어디에 보여줘?
A. email Field Error로 보여준다.

Q. password는 trim해서 보내?
A. 임의 trim은 권장하지 않는다. 서비스 정책에 따라 결정한다.

Q. 로그인 Form에서 가장 중요한 보안 기준은?
A. password와 token을 로그에 남기지 않는 것이다.

Q. Signup Form에서 confirmPassword도 API로 보내?
A. Backend 정책에 따라 다르지만 Frontend 검증용이면 Request Body에서 제외할 수 있다.

Q. 이메일 중복 확인을 했으면 submit 중복 검증은 생략해도 돼?
A. 아니다. submit 시 Backend 최종 검증은 유지해야 한다.

Q. 약관 동의는 Frontend만 검증하면 돼?
A. 아니다. 필수 동의는 Backend에서도 검증해야 한다.

Q. Search Filter Form은 Request Body를 사용해?
A. 일반적인 목록 검색은 Query Params를 사용한다.

Q. 검색 조건 변경 시 page는 어떻게 해?
A. 대부분 1페이지로 reset한다.

Q. 빈 필터 값도 Query Params에 넣어?
A. 보통 제외한다.

Q. Review Form에서 rating은 문자열이야 숫자야?
A. input 값은 문자열일 수 있으므로 validation 후 Number로 변환해 Request에 담는다.

Q. 리뷰 내용은 trim해야 해?
A. 보통 submit 시 trim하고 공백만 입력한 값은 invalid 처리한다.

Q. 리뷰 이미지가 있으면 JSON으로 보내?
A. 파일이 포함되면 보통 FormData multipart 요청을 사용한다.

Q. input에 입력이 안 되는 이유는?
A. value만 있고 onChange가 없거나 setState가 올바르게 실행되지 않을 가능성이 크다.

Q. name과 values key가 다르면 왜 문제야?
A. 공통 handler가 다른 key를 업데이트해 화면 value가 바뀌지 않을 수 있다.

Q. checkbox가 안 바뀌는 이유는?
A. checked가 아니라 value로 제어했거나 onChange에서 checked를 반영하지 않았을 수 있다.

Q. 버튼을 눌러도 submit이 안 돼?
A. form onSubmit, button type, disabled 상태, validation return을 확인해야 한다.

Q. Network 요청이 안 보여?
A. submit handler가 실행되지 않았거나 validation에서 중단되었을 수 있다.

Q. Validation은 실패했는데 에러가 안 보여?
A. errors key와 UI에서 참조하는 key가 일치하는지 확인해야 한다.

Q. React Hook Form에서 error.message가 안 보여?
A. validation rule에 message가 없거나 setError에 message가 누락되었을 수 있다.

Q. Request Body가 틀렸는지 어떻게 확인해?
A. 브라우저 Network 탭의 Payload와 Backend DTO를 비교한다.

Q. field name이 다르면 어떻게 돼?
A. Backend에서 값이 null로 들어가거나 validation error가 발생할 수 있다.

Q. 서버 에러가 화면에 안 보여?
A. 서버 응답 구조와 Frontend Error Mapping 경로가 맞는지 확인해야 한다.

Q. interceptor 때문에 Form catch가 실행되지 않을 수 있어?
A. 가능하다. interceptor가 error를 처리한 뒤 throw하지 않으면 catch에 도달하지 않을 수 있다.

Q. Validation Error를 200으로 반환해도 돼?
A. 권장하지 않는다. 실패는 적절한 4xx status로 표현하는 것이 좋다.

Q. 중복 이메일은 어떤 status가 좋아?
A. 팀 규칙에 따라 400 또는 409를 사용할 수 있지만 409 Conflict가 의미상 적합한 경우가 많다.

Q. 401과 403 차이는 뭐야?
A. 401은 인증이 없거나 유효하지 않은 상태이고 403은 인증은 되었지만 권한이 없는 상태다.

Q. Form values를 console.log 해도 돼?
A. 권장하지 않는다. password나 개인정보가 포함될 수 있다.

Q. password를 디버깅 로그로 찍어도 돼?
A. 안 된다. 민감정보는 로그에 남기지 않는다.

Q. 서버 예외 메시지를 그대로 보여줘도 돼?
A. 안 된다. 내부 정보와 보안 정보가 노출될 수 있다.

Q. SQL 오류를 사용자에게 보여줘도 돼?
A. 안 된다. 사용자 친화 메시지로 변환해야 한다.

Q. Client Validation은 보안 검증이야?
A. 아니다. Client Validation은 UX용이며 쉽게 우회될 수 있다.

Q. button disabled로 요청을 막으면 안전해?
A. 아니다. API 직접 요청으로 우회할 수 있다.

Q. maxLength를 걸면 Backend 길이 검증은 없어도 돼?
A. 아니다. maxLength는 우회될 수 있으므로 Backend 검증이 필요하다.

Q. Form 입력이 느리면 무엇을 확인해?
A. onChange마다 무거운 validation, 전체 Form re-render, watch 남용, 큰 Component 구조를 확인한다.

Q. React Hook Form이 성능에 유리한 이유는?
A. uncontrolled 기반 관리로 불필요한 re-render를 줄일 수 있기 때문이다.

Q. Form UX에서 가장 중요한 피드백은 뭐야?
A. 에러 메시지, 제출 중 상태, 성공 후 결과, 재시도 가능 여부다.

Q. submit 중에는 무엇을 보여줘?
A. 버튼 disabled와 “처리 중...” 같은 loading label을 제공하는 것이 좋다.

Q. Form 관련 이름은 어떻게 짓는 게 좋아?
A. 도메인명과 역할이 드러나게 `SignupForm`, `validateSignup`, `toSignupRequest`처럼 짓는다.

Q. Form Values와 Request DTO 이름을 구분해야 해?
A. 구분하는 것이 좋다. 화면 입력 상태와 API 요청 구조는 다를 수 있다.

Q. Form 최종 검수에서 가장 중요한 것은?
A. 입력 처리, 검증, 요청 변환, 서버 에러 처리, 접근성, 보안 기준이 모두 연결되어 있는지 확인하는 것이다.

Q. Form 검수에서 자주 놓치는 것은?
A. button type, checkbox checked, Request Body type conversion, server error mapping, aria-describedby, password log 금지다.

Q. RAG Retrieval Optimization은 왜 필요해?
A. Agent가 Form 관련 문제를 정확한 chunk에서 찾도록 검색 키워드와 FAQ를 강화하기 위해 필요하다.

Q. Form Handling 문서는 어떤 다음 문서와 연결돼?
A. Authentication Frontend Flow, Error Handling & Loading UX, Data Fetching & REST API Integration과 연결된다.
