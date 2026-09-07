# Form Handling & Validation Part07 - React Hook Form & Form Accessibility

---

# 1. React Hook Form Foundation

## 1.1 React Hook Form Definition

### [개념]

React Hook Form은 React Form의 입력값, 검증, 에러, touched, dirty, submitting 상태를 효율적으로 관리하기 위한 Form Library다.

React Hook Form은 `register`, `handleSubmit`, `formState`, `setError`, `reset`, `watch`, `Controller`를 중심으로 Form을 구성한다.

---

### [핵심]

React Hook Form 핵심 요소:

- React Hook Form
- useForm
- register
- handleSubmit
- formState
- errors
- isSubmitting
- touchedFields
- dirtyFields
- isDirty
- isValid
- setError
- clearErrors
- reset
- watch
- Controller
- defaultValues
- Server Error Mapping

---

### [실무]

2026 실무 기준에서 React Hook Form은 아래 상황에서 검토한다.

```text
Field 개수 많음
→ Validation 복잡
→ touched / dirty 필요
→ Server Error Mapping 필요
→ 재사용 Field 많음
→ React Hook Form 검토
```

간단한 Form은 `useState`로 충분할 수 있다.

```text
간단한 검색 Form
→ useState 가능

간단한 리뷰 Form
→ useState 가능

회원가입 Form
→ React Hook Form 검토

관리자 등록 Form
→ React Hook Form 검토

동적 필드 Form
→ React Hook Form 심화 검토
```

---

### [FAQ]

Q. React Hook Form이 뭐야?
A. React Form의 입력값, 검증, 에러, 제출 상태를 효율적으로 관리하는 Form Library다.

Q. 모든 Form에 React Hook Form을 써야 해?
A. 아니다. 간단한 Form은 useState로 충분하고 복잡한 Form에서 도입을 검토한다.

Q. React Hook Form은 언제 쓰는 게 좋아?
A. 필드가 많고 검증, touched, dirty, server error 관리가 복잡할 때 좋다.

Q. React Hook Form은 Controlled Component야?
A. 기본적으로 uncontrolled 기반으로 효율적으로 동작하지만 Controller를 통해 controlled component도 연결할 수 있다.

---

## 1.2 React Hook Form Use Criteria

### [개념]

React Hook Form Use Criteria는 Form 복잡도, 검증 요구사항, 팀 컨벤션, 유지보수성을 기준으로 React Hook Form 도입 여부를 판단하는 기준이다.

작은 Form에 무조건 도입하면 오히려 구조가 과해질 수 있다.

---

### [핵심]

도입 검토 기준:

- field count 많음
- validation 복잡
- touched 관리 필요
- dirty 관리 필요
- server error mapping 필요
- reusable field component 많음
- performance concern
- schema validation 연동 필요
- nested form
- dynamic field
- team convention

---

### [실무]

도입 권장:

```text
회원가입 Form
프로필 수정 Form
관리자 등록 Form
복잡한 검색 필터 Form
다중 Step Form
필드가 많은 설정 Form
Server Error Mapping이 많은 Form
```

도입 신중:

```text
검색어 하나 입력하는 Form
댓글 한 줄 입력 Form
단순 toggle Form
필드 1~2개 Form
```

주의:

- 팀이 React Hook Form을 사용하지 않는다면 컨벤션 확인
- 작은 Form에 과도한 추상화 지양
- schema resolver는 별도 학습 비용 있음
- Controller 사용이 많으면 구조 복잡도 증가
- Server Error Mapping 기준을 미리 정함

---

### [FAQ]

Q. React Hook Form 도입 기준은 뭐야?
A. 필드 수, 검증 복잡도, touched/dirty 필요성, server error 처리 복잡도를 기준으로 판단한다.

Q. 작은 검색 Form에도 React Hook Form이 필요해?
A. 필수는 아니다. keyword 하나 정도는 useState가 더 단순할 수 있다.

Q. 회원가입 Form은 React Hook Form을 써도 좋아?
A. 필드와 검증이 많기 때문에 도입을 검토하기 좋다.

Q. React Hook Form을 쓰면 코드가 항상 줄어들어?
A. 항상은 아니다. Form 구조와 팀 숙련도에 따라 오히려 복잡해질 수 있다.

---

# 2. useForm Rules

## 2.1 useForm Basic Structure

### [개념]

`useForm`은 React Hook Form의 핵심 Hook이다.

Form 등록, 제출 처리, 에러 상태, 기본값, reset, watch, server error 연결 기능을 제공한다.

---

### [핵심]

useForm 핵심 반환값:

- register
- handleSubmit
- formState
- errors
- isSubmitting
- reset
- setError
- clearErrors
- watch
- getValues
- setValue
- control

---

### [실무]

기본 구조:

```tsx
function LoginForm({ onLogin }) {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
    setError,
    reset,
  } = useForm({
    defaultValues: {
      email: "",
      password: "",
    },
  });

  async function submitForm(values) {
    await onLogin(values);
  }

  return (
    <form onSubmit={handleSubmit(submitForm)}>
      <input
        {...register("email", {
          required: "이메일을 입력해 주세요.",
        })}
      />
      {errors.email && <p role="alert">{errors.email.message}</p>}

      <input
        type="password"
        {...register("password", {
          required: "비밀번호를 입력해 주세요.",
        })}
      />
      {errors.password && <p role="alert">{errors.password.message}</p>}

      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? "로그인 중..." : "로그인"}
      </button>
    </form>
  );
}
```

권장:

- `defaultValues` 명시
- `handleSubmit`으로 submit 처리
- `errors.fieldName.message` 표시
- `isSubmitting`으로 버튼 disabled 처리
- 서버 에러는 `setError` 또는 별도 global error로 mapping

---

### [FAQ]

Q. useForm은 뭐야?
A. React Hook Form에서 Form 상태와 제출, 검증을 관리하는 핵심 Hook이다.

Q. useForm에서 defaultValues는 꼭 필요해?
A. 권장한다. 초기값을 명확히 하면 reset과 dirty 관리가 안정적이다.

Q. formState.errors는 뭐야?
A. register validation 또는 setError로 발생한 field error를 담는 객체다.

Q. isSubmitting은 언제 true가 돼?
A. handleSubmit으로 실행된 async submit 함수가 진행 중일 때 true가 된다.

---

## 2.2 defaultValues Rules

### [개념]

`defaultValues`는 React Hook Form의 초기값이자 reset, dirty check, form state 비교 기준이다.

Controlled Component의 initialValues와 같은 역할을 한다.

---

### [핵심]

defaultValues 기준:

- text: `""`
- textarea: `""`
- select: `""`
- checkbox: `false`
- multiple checkbox: `[]`
- number input: `""` 또는 숫자 기준 명확화
- edit form server data
- reset 기준
- dirty 비교 기준

---

### [실무]

생성 Form defaultValues:

```tsx
const form = useForm({
  defaultValues: {
    title: "",
    content: "",
    category: "",
    published: false,
  },
});
```

수정 Form defaultValues:

```tsx
const form = useForm({
  defaultValues: {
    nickname: profile.nickname ?? "",
    bio: profile.bio ?? "",
  },
});
```

서버 데이터 로딩 후 reset:

```tsx
useEffect(() => {
  if (profile) {
    reset({
      nickname: profile.nickname ?? "",
      bio: profile.bio ?? "",
    });
  }
}, [profile, reset]);
```

주의:

- API 데이터가 나중에 오면 `reset`으로 반영
- defaultValues가 undefined가 되지 않게 처리
- 수정 Form에서는 서버 최신값으로 reset
- dirty check 기준이 defaultValues에 의존
- 파일 input은 별도 기준 필요

---

### [FAQ]

Q. defaultValues는 왜 중요해?
A. 초기값, reset 기준, dirty check 기준이 되기 때문이다.

Q. 서버 데이터가 늦게 오면 defaultValues가 자동으로 바뀌어?
A. 아니다. 보통 reset을 호출해 서버 데이터를 Form에 반영한다.

Q. defaultValues에 undefined를 넣어도 돼?
A. 권장하지 않는다. 빈 문자열, false, [] 같은 명확한 값이 좋다.

Q. 수정 Form 성공 후에는 어떻게 해?
A. 서버 최신값으로 reset해서 defaultValues와 현재 values를 맞추는 것이 좋다.

---

# 3. register Rules

## 3.1 register Basic Rules

### [개념]

`register`는 input을 React Hook Form에 등록하는 함수다.

등록된 input은 React Hook Form이 값, validation, dirty, touched, error 상태를 관리할 수 있다.

---

### [핵심]

register 핵심 요소:

- field name
- validation rules
- required
- minLength
- maxLength
- pattern
- valueAsNumber
- setValueAs
- onChange
- onBlur
- ref
- error message

---

### [실무]

기본 register:

```tsx
<input
  {...register("email", {
    required: "이메일을 입력해 주세요.",
  })}
/>
```

Validation 포함:

```tsx
<input
  {...register("nickname", {
    required: "닉네임을 입력해 주세요.",
    minLength: {
      value: 2,
      message: "닉네임은 2자 이상이어야 합니다.",
    },
    maxLength: {
      value: 20,
      message: "닉네임은 20자 이하로 입력해 주세요.",
    },
  })}
/>
```

주의:

- register field name과 Request Mapping key 일치 권장
- validation message를 명확히 작성
- register가 제공하는 ref/onChange/onBlur를 input에 전달
- custom component는 register 전달 방식 주의
- controlled custom component는 Controller 검토

---

### [FAQ]

Q. register는 뭐야?
A. input을 React Hook Form에 등록해 값과 검증 상태를 관리하게 하는 함수다.

Q. register 이름은 무엇과 맞춰야 해?
A. Form Values key, Request DTO mapping, Error Mapping 기준과 맞추는 것이 좋다.

Q. register 안에 validation 규칙을 넣어도 돼?
A. 가능하다. required, minLength, pattern 같은 기본 검증을 넣을 수 있다.

Q. register를 custom component에 그대로 넘겨도 돼?
A. 가능하지만 내부 input에 ref, name, onChange, onBlur가 제대로 전달되어야 한다.

---

## 3.2 register Validation Rules

### [개념]

register Validation Rules는 input 등록 시 필드별 검증 규칙을 함께 선언하는 방식이다.

간단한 required, length, pattern 검증에 적합하다.

---

### [핵심]

register validation 대상:

- required
- minLength
- maxLength
- min
- max
- pattern
- validate
- valueAsNumber
- setValueAs
- custom message
- field-level validation

---

### [실무]

Email validation:

```tsx
<input
  type="email"
  {...register("email", {
    required: "이메일을 입력해 주세요.",
    pattern: {
      value: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
      message: "이메일 형식이 올바르지 않습니다.",
    },
  })}
/>
```

Number validation:

```tsx
<input
  type="number"
  {...register("rating", {
    required: "평점을 입력해 주세요.",
    valueAsNumber: true,
    min: {
      value: 1,
      message: "평점은 1점 이상이어야 합니다.",
    },
    max: {
      value: 5,
      message: "평점은 5점 이하이어야 합니다.",
    },
  })}
/>
```

Custom validate:

```tsx
<input
  {...register("title", {
    validate: (value) => (value.trim() ? true : "제목을 입력해 주세요."),
  })}
/>
```

주의:

- password 임의 trim 주의
- valueAsNumber 사용 시 NaN 처리 확인
- 복잡한 cross field validation은 validate 또는 submit validator 검토
- Backend Validation 기준과 메시지 일치
- schema validation 도입 시 중복 규칙 관리 주의

---

### [FAQ]

Q. register validation은 언제 적합해?
A. required, minLength, pattern 같은 간단한 field-level validation에 적합하다.

Q. 공백만 입력한 값은 required로 막을 수 있어?
A. required만으로는 부족할 수 있어 validate에서 trim 검증을 추가할 수 있다.

Q. valueAsNumber는 뭐야?
A. input 값을 number로 변환해 Form Values에 저장하는 옵션이다.

Q. register validation과 별도 validateForm을 같이 써도 돼?
A. 가능하지만 규칙 중복과 메시지 불일치를 주의해야 한다.

---

# 4. handleSubmit Rules

## 4.1 handleSubmit Flow

### [개념]

`handleSubmit`은 React Hook Form의 Submit Handler wrapper다.

기본 Form submit 동작을 처리하고, 등록된 validation을 통과한 경우 submit 함수를 호출한다.

---

### [핵심]

handleSubmit 핵심 요소:

- form onSubmit
- handleSubmit(submitForm)
- preventDefault handled
- validation before submit
- valid callback
- invalid callback
- async submit
- isSubmitting
- error handling

---

### [실무]

기본 submit:

```tsx
function ReviewForm({ onSubmitReview }) {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm({
    defaultValues: {
      content: "",
      rating: 5,
    },
  });

  async function submitForm(values) {
    const requestBody = toCreateReviewRequest(values);

    await onSubmitReview(requestBody);
  }

  return (
    <form onSubmit={handleSubmit(submitForm)}>
      <textarea
        {...register("content", {
          required: "리뷰 내용을 입력해 주세요.",
        })}
      />
      {errors.content && <p role="alert">{errors.content.message}</p>}

      <button type="submit" disabled={isSubmitting}>
        저장
      </button>
    </form>
  );
}
```

Invalid callback:

```tsx
<form onSubmit={handleSubmit(submitForm, handleInvalid)}>
```

권장:

- `onSubmit={handleSubmit(submitForm)}` 사용
- `onSubmit={handleSubmit(submitForm())}` 금지
- submitForm에서는 Request Body Mapping 수행
- 서버 에러는 catch에서 setError 또는 global error 처리
- isSubmitting으로 중복 제출 방지

---

### [FAQ]

Q. handleSubmit은 뭐야?
A. React Hook Form에서 validation 후 submit 함수를 실행하는 submit wrapper다.

Q. handleSubmit은 preventDefault를 대신 해?
A. 기본 submit 이벤트 처리를 포함하므로 별도 preventDefault를 직접 작성하지 않아도 된다.

Q. onSubmit={handleSubmit(submitForm())}은 왜 문제야?
A. submitForm이 렌더링 중 즉시 실행될 수 있으므로 함수 참조를 전달해야 한다.

Q. handleSubmit에서 validation 실패하면 submitForm이 실행돼?
A. 아니다. validation 실패 시 valid submit 함수는 실행되지 않는다.

---

## 4.2 Async Submit and isSubmitting

### [개념]

React Hook Form의 `isSubmitting`은 `handleSubmit`으로 실행된 async submit 함수가 진행 중인지 나타낸다.

제출 중 버튼 비활성화와 중복 제출 방지에 사용한다.

---

### [핵심]

Async Submit 요소:

- async submit
- await API
- isSubmitting
- disabled button
- loading label
- try catch
- server error
- duplicate submit prevention

---

### [실무]

async submit 예:

```tsx
async function submitForm(values) {
  try {
    const requestBody = toSignupRequest(values);

    await signup(requestBody);

    reset();
  } catch (error) {
    const mappedError = mapApiError(error);

    applyServerErrors(mappedError);
  }
}
```

button 처리:

```tsx
<button type="submit" disabled={isSubmitting}>
  {isSubmitting ? "가입 중..." : "가입하기"}
</button>
```

주의:

- submitForm이 Promise를 반환해야 isSubmitting 관리가 안정적
- catch에서 error를 삼켜도 UI 처리는 명확히 수행
- 서버 에러 발생 후 입력값 유지
- React Hook Form isSubmitting과 별도 API loading state 중복 주의
- 결제/주문은 Backend idempotency 필요

---

### [FAQ]

Q. isSubmitting은 언제 사용해?
A. 제출 중 버튼 비활성화, 로딩 문구, 중복 제출 방지에 사용한다.

Q. isSubmitting을 쓰면 별도 submitting state가 필요 없어?
A. 대부분 handleSubmit 기반 Form에서는 isSubmitting으로 충분하다.

Q. async submit에서 try/catch가 필요해?
A. 필요하다. 서버 에러를 Form UI에 mapping해야 한다.

Q. isSubmitting만으로 중요한 중복 요청을 완전히 막을 수 있어?
A. 아니다. 중요한 요청은 Backend 중복 방지도 필요하다.

---

# 5. formState Rules

## 5.1 errors Rules

### [개념]

`formState.errors`는 React Hook Form이 관리하는 Field Error 객체다.

register validation, resolver validation, setError로 발생한 오류가 저장된다.

---

### [핵심]

errors 사용 기준:

- formState.errors
- field error
- errors.email.message
- role alert
- aria-invalid
- aria-describedby
- validation message
- server error setError
- nested error

---

### [실무]

Error 표시:

```tsx
<input
  {...register("email", {
    required: "이메일을 입력해 주세요.",
  })}
  aria-invalid={Boolean(errors.email)}
  aria-describedby={errors.email ? "email-error" : undefined}
/>;
{
  errors.email && (
    <p id="email-error" role="alert">
      {errors.email.message}
    </p>
  );
}
```

권장:

- field 근처에 error message 표시
- `errors.field?.message` 사용
- error message 없는 error 처리 주의
- aria-invalid와 aria-describedby 연결
- 서버 field error도 setError로 같은 위치에 표시 가능

---

### [FAQ]

Q. formState.errors는 뭐야?
A. React Hook Form이 관리하는 Field Error 객체다.

Q. 에러 메시지는 어떻게 꺼내?
A. 보통 `errors.email?.message`처럼 field별 message를 사용한다.

Q. errors를 직접 setState로 바꿔도 돼?
A. React Hook Form에서는 setError, clearErrors 같은 API를 사용한다.

Q. 서버 에러도 errors에 넣을 수 있어?
A. 가능하다. setError를 사용해 field error로 넣을 수 있다.

---

## 5.2 touchedFields and dirtyFields Rules

### [개념]

`touchedFields`는 사용자가 방문한 Field를 나타내고, `dirtyFields`는 defaultValues와 달라진 Field를 나타낸다.

에러 표시 타이밍, 저장 버튼 활성화, 변경사항 경고에 사용할 수 있다.

---

### [핵심]

상태 기준:

- touchedFields
- dirtyFields
- isDirty
- defaultValues
- onBlur
- field visited
- field changed
- edit form
- save button
- unsaved changes

---

### [실무]

dirty 버튼 처리:

```tsx
const {
  formState: { isDirty, isSubmitting },
} = useForm({
  defaultValues,
});

<button type="submit" disabled={!isDirty || isSubmitting}>
  변경사항 저장
</button>;
```

touched 기반 error 표시:

```tsx
const {
  formState: { touchedFields, errors },
} = useForm();

const showEmailError = touchedFields.email && errors.email;
```

권장:

- 수정 Form에서 isDirty 활용
- defaultValues를 정확히 설정
- reset 후 dirty 기준 갱신
- touchedFields는 에러 표시 타이밍에 활용 가능
- dirtyFields는 PATCH Request 생성에 활용 가능

---

### [FAQ]

Q. touchedFields는 뭐야?
A. 사용자가 blur 등으로 방문한 field를 나타내는 상태다.

Q. dirtyFields는 뭐야?
A. defaultValues와 달라진 field를 나타내는 상태다.

Q. isDirty는 언제 유용해?
A. 수정 Form에서 변경사항 저장 버튼 활성화나 이탈 경고에 유용하다.

Q. reset하면 isDirty는 어떻게 돼?
A. reset된 값이 새 기준이 되면 isDirty가 false가 된다.

---

# 6. setError and Server Error Mapping

## 6.1 setError Rules

### [개념]

`setError`는 React Hook Form에서 수동으로 Field Error 또는 Root Error를 설정하는 함수다.

Server Validation Error를 Form Error UI에 연결할 때 자주 사용한다.

---

### [핵심]

setError 사용 대상:

- server field error
- duplicate email
- duplicate nickname
- root error
- global error
- API validation failed
- manual error
- backend error mapping

---

### [실무]

Field Error 설정:

```tsx
setError("email", {
  type: "server",
  message: "이미 사용 중인 이메일입니다.",
});
```

여러 field error mapping:

```tsx
function applyServerFieldErrors(fieldErrors) {
  Object.entries(fieldErrors).forEach(([fieldName, message]) => {
    setError(fieldName, {
      type: "server",
      message,
    });
  });
}
```

Root Error 설정:

```tsx
setError("root.server", {
  type: "server",
  message: "요청 처리에 실패했습니다.",
});
```

권장:

- 서버 field error는 setError로 연결
- field name이 register name과 일치해야 함
- Global Error는 root error 또는 별도 state 사용
- 입력 수정 시 해당 field error가 자동/수동으로 정리되는지 확인
- 서버 응답 구조와 mapping 기준 통일

---

### [FAQ]

Q. setError는 언제 써?
A. 서버 검증 오류나 수동 검증 오류를 React Hook Form errors에 넣을 때 사용한다.

Q. 서버 Field Error를 setError로 넣을 수 있어?
A. 가능하다. field name과 message를 mapping하면 된다.

Q. setError field name은 무엇과 맞춰야 해?
A. register에 사용한 field name과 맞춰야 한다.

Q. Global Error도 setError로 처리할 수 있어?
A. root error로 처리할 수 있지만 별도 submitError state를 사용하는 방식도 가능하다.

---

## 6.2 Server Error Mapping with React Hook Form

### [개념]

Server Error Mapping with React Hook Form은 Backend Error Response를 `setError` 또는 Global Error State로 변환하는 처리다.

Field Error는 `setError`, Global Error는 `root` 또는 별도 state에 저장한다.

---

### [핵심]

Mapping 대상:

- Backend errors object
- Field Error
- Global Error
- setError
- root.server
- submitError state
- response code
- response message
- fallback message

---

### [실무]

Server Error 적용 예:

```tsx
async function submitForm(values) {
  try {
    const requestBody = toSignupRequest(values);

    await signup(requestBody);

    reset();
  } catch (error) {
    const { fieldErrors, globalError } = mapApiError(error);

    Object.entries(fieldErrors).forEach(([fieldName, message]) => {
      setError(fieldName, {
        type: "server",
        message,
      });
    });

    if (globalError) {
      setError("root.server", {
        type: "server",
        message: globalError,
      });
    }
  }
}
```

Root Error 출력:

```tsx
{
  errors.root?.server && <p role="alert">{errors.root.server.message}</p>;
}
```

별도 Global Error State 방식:

```tsx
const [submitError, setSubmitError] = useState("");

setSubmitError(globalError);
```

권장:

- field error는 setError 사용
- global error는 root error 또는 별도 state 중 팀 기준 선택
- field name mapping table 필요 시 적용
- Network Error는 global error 처리
- 서버 내부 메시지 노출 금지

---

### [FAQ]

Q. React Hook Form에서 서버 에러는 어떻게 넣어?
A. setError를 사용해 field error 또는 root error로 넣는다.

Q. 서버 errors 객체를 그대로 setError에 넣을 수 있어?
A. 반복문으로 fieldName과 message를 하나씩 setError에 전달해야 한다.

Q. Global Error는 root error가 좋아 별도 state가 좋아?
A. 팀 컨벤션에 따라 선택한다. root error는 RHF 내부 관리, 별도 state는 명시적 관리가 쉽다.

Q. 서버 field name이 register name과 다르면?
A. mapping table로 변환해야 한다.

---

# 7. reset and Form Lifecycle Rules

## 7.1 reset Rules

### [개념]

`reset`은 React Hook Form의 Form Values, errors, dirty, touched 상태를 초기화하거나 새 값으로 재설정하는 함수다.

생성 성공 후 초기화, 수정 성공 후 최신 서버값 반영, 취소 버튼 처리에 사용한다.

---

### [핵심]

reset 사용 대상:

- create success
- edit success
- cancel edit
- server data loaded
- clear errors
- reset dirty state
- reset touched state
- latest values
- defaultValues update

---

### [실무]

생성 Form reset:

```tsx
await createPost(requestBody);

reset({
  title: "",
  content: "",
  category: "",
});
```

수정 Form reset:

```tsx
const latestProfile = await updateProfile(requestBody);

reset({
  nickname: latestProfile.nickname ?? "",
  bio: latestProfile.bio ?? "",
});
```

취소 reset:

```tsx
<button type="button" onClick={() => reset()}>
  취소
</button>
```

권장:

- 성공 후 reset 기준 명확화
- 실패 후 reset 금지
- 수정 Form은 서버 최신값으로 reset
- reset 후 isDirty false 확인
- file input은 별도 처리 필요 가능

---

### [FAQ]

Q. reset은 뭐야?
A. React Hook Form의 값과 formState를 초기화하거나 새 값으로 재설정하는 함수다.

Q. Submit 성공 후 reset해도 돼?
A. 생성 Form은 가능하고 수정 Form은 서버 최신값으로 reset하는 것이 좋다.

Q. Submit 실패 후 reset해도 돼?
A. 보통 하지 않는다. 사용자가 수정 후 다시 제출할 수 있어야 한다.

Q. reset하면 errors도 사라져?
A. 기본적으로 errors와 dirty/touched 상태도 초기화된다.

---

## 7.2 watch Rules

### [개념]

`watch`는 특정 Field 또는 전체 Form Values의 현재 값을 구독하는 함수다.

비밀번호 확인, 실시간 미리보기, 조건부 field 표시, 글자 수 표시 등에 사용할 수 있다.

---

### [핵심]

watch 사용 대상:

- password confirm
- live preview
- conditional field
- character count
- dependent select
- dynamic UI
- caution re-render
- form value subscription

---

### [실무]

글자 수 표시:

```tsx
const content = watch("content", "");

<p>{content.length}/500</p>;
```

조건부 Field:

```tsx
const hasLink = watch("hasLink", false);

{
  hasLink && (
    <input
      {...register("url", {
        required: "URL을 입력해 주세요.",
      })}
    />
  );
}
```

비밀번호 확인 validate:

```tsx
const password = watch("password");

<input
  type="password"
  {...register("confirmPassword", {
    validate: (value) => value === password || "비밀번호가 일치하지 않습니다.",
  })}
/>;
```

주의:

- watch 남용 시 re-render 증가 가능
- 복잡한 구독은 useWatch 검토
- 조건부 field unmount 시 값 유지/제거 기준 확인
- Cross Field Validation과 함께 사용 가능

---

### [FAQ]

Q. watch는 뭐야?
A. Form Field의 현재 값을 구독해 UI나 validation에 사용할 수 있는 함수다.

Q. watch는 언제 써?
A. 글자 수 표시, 비밀번호 확인, 조건부 field 표시, 실시간 미리보기에 사용한다.

Q. watch를 많이 쓰면 문제야?
A. re-render가 늘어날 수 있어 필요한 field만 구독하는 것이 좋다.

Q. 조건부 field가 사라지면 값도 사라져?
A. 설정과 구현에 따라 다르므로 unregister 기준을 확인해야 한다.

---

# 8. Controller Rules

## 8.1 Controller Definition

### [개념]

`Controller`는 React Hook Form에서 외부 Controlled Component를 연결하기 위한 컴포넌트다.

Custom Select, DatePicker, UI Library Input처럼 `register`만으로 연결하기 어려운 Component에 사용한다.

---

### [핵심]

Controller 사용 대상:

- controlled component
- custom select
- date picker
- UI library input
- rich input
- value/onChange contract
- control
- render props
- field
- fieldState

---

### [실무]

Controller 예:

```tsx
<Controller
  name="category"
  control={control}
  rules={{
    required: "카테고리를 선택해 주세요.",
  }}
  render={({ field, fieldState }) => (
    <>
      <CustomSelect
        value={field.value}
        onChange={field.onChange}
        onBlur={field.onBlur}
        options={categoryOptions}
      />
      {fieldState.error && <p role="alert">{fieldState.error.message}</p>}
    </>
  )}
/>
```

권장:

- register로 연결 가능한 input은 register 우선
- 외부 controlled component는 Controller 사용
- value/onChange contract 확인
- defaultValues에 해당 field 포함
- fieldState.error로 에러 표시 가능

---

### [FAQ]

Q. Controller는 뭐야?
A. React Hook Form에서 controlled custom component를 연결하기 위한 컴포넌트다.

Q. 언제 Controller를 써?
A. register만으로 연결하기 어려운 Custom Select, DatePicker, UI Library Input에 사용한다.

Q. 기본 input에도 Controller를 써야 해?
A. 보통 기본 input은 register로 충분하다.

Q. Controller에서도 validation rules를 쓸 수 있어?
A. 가능하다. rules prop에 required나 validate를 정의할 수 있다.

---

## 8.2 Controller Common Mistakes

### [개념]

Controller Common Mistakes는 외부 controlled component를 React Hook Form과 연결할 때 자주 발생하는 실수다.

value/onChange mapping, defaultValues 누락, name 불일치가 대표적이다.

---

### [핵심]

자주 발생하는 실수:

- defaultValues 누락
- field.value 미전달
- field.onChange 미전달
- onChange value shape 불일치
- fieldState.error 미표시
- name mismatch
- controlled/uncontrolled warning
- unnecessary Controller

---

### [실무]

문제 예:

```tsx
<Controller
  name="category"
  control={control}
  render={() => <CustomSelect options={categoryOptions} />}
/>
```

수정 예:

```tsx
<Controller
  name="category"
  control={control}
  render={({ field }) => (
    <CustomSelect
      value={field.value}
      onChange={field.onChange}
      options={categoryOptions}
    />
  )}
/>
```

onChange shape 변환:

```tsx
<Controller
  name="category"
  control={control}
  render={({ field }) => (
    <CustomSelect
      value={field.value}
      onChange={(option) => field.onChange(option.value)}
    />
  )}
/>
```

주의:

- Custom Component의 onChange가 event를 주는지 value를 주는지 확인
- defaultValues에 Controller field 포함
- register와 Controller 중복 사용 금지
- 단순 input에 Controller 남용 금지

---

### [FAQ]

Q. Controller에서 값이 안 바뀌는 이유는?
A. field.value 또는 field.onChange를 Custom Component에 제대로 전달하지 않았을 수 있다.

Q. Custom Select onChange가 option 객체를 주면 어떻게 해?
A. field.onChange에 option.value처럼 필요한 값만 넘기도록 변환한다.

Q. Controller field도 defaultValues에 넣어야 해?
A. 권장한다. 초기값과 dirty 관리가 안정적이다.

Q. register와 Controller를 같은 input에 같이 써도 돼?
A. 권장하지 않는다. 하나의 방식만 사용한다.

---

# 9. Schema Validation Basics

## 9.1 Schema Validation Use Criteria

### [개념]

Schema Validation은 Zod, Yup 같은 schema library를 사용해 Form Validation 규칙을 선언적으로 관리하는 방식이다.

React Hook Form과 resolver를 통해 연결할 수 있다.

---

### [핵심]

Schema Validation 검토 기준:

- complex validation
- reusable schema
- TypeScript type inference
- backend contract
- field rules centralized
- resolver
- zod
- yup
- cross field validation
- error message consistency

---

### [실무]

도입 검토 상황:

```text
회원가입 Form
→ 필드 많음
→ password confirm
→ email format
→ nickname length
→ schema validation 검토
```

도입 신중 상황:

```text
간단한 검색 Form
→ keyword 하나
→ schema validation 불필요 가능
```

주의:

- schema validation 심화는 Advanced Form Validation 문서에서 관리
- Backend DTO와 schema 기준 일치
- schema와 register validation 중복 주의
- resolver 도입 시 팀 의존성 확인
- 에러 메시지 localization 기준 필요 가능

---

### [FAQ]

Q. Schema Validation이 뭐야?
A. Zod나 Yup 같은 schema로 Form Validation 규칙을 선언하는 방식이다.

Q. React Hook Form과 schema validation을 같이 쓸 수 있어?
A. 가능하다. resolver를 사용해 연결할 수 있다.

Q. 모든 Form에 Zod를 써야 해?
A. 아니다. 복잡한 Form에서 도입을 검토한다.

Q. register validation과 schema validation을 같이 써도 돼?
A. 가능하지만 규칙 중복과 메시지 불일치에 주의해야 한다.

---

# 10. Form Accessibility Foundation

## 10.1 Form Accessibility Definition

### [개념]

Form Accessibility는 사용자가 키보드, 스크린 리더, 보조기술 등 다양한 방식으로 Form을 이해하고 입력하고 오류를 수정할 수 있도록 만드는 기준이다.

Form Accessibility는 선택 사항이 아니라 기본 품질 기준이다.

---

### [핵심]

Form Accessibility 핵심 요소:

- label
- htmlFor
- id
- aria-invalid
- aria-describedby
- role alert
- required indication
- fieldset
- legend
- keyboard navigation
- focus management
- error message
- first invalid field
- no placeholder-only label
- no color-only error

---

### [실무]

접근성 기본 Flow:

```text
Input Purpose 제공
→ Label 연결
→ Required 표시
→ Error 발생
→ aria-invalid 설정
→ aria-describedby로 Error 연결
→ role alert로 Error 알림
→ Submit 실패 시 Focus 관리
```

접근성 있는 Field:

```tsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  type="email"
  aria-invalid={Boolean(errors.email)}
  aria-describedby={errors.email ? "email-error" : undefined}
  {...register("email")}
/>
{errors.email && (
  <p id="email-error" role="alert">
    {errors.email.message}
  </p>
)}
```

---

### [FAQ]

Q. Form Accessibility가 뭐야?
A. 모든 사용자가 Form을 이해하고 입력하고 오류를 수정할 수 있도록 만드는 접근성 기준이다.

Q. Form 접근성에서 가장 기본은 뭐야?
A. label과 input을 연결하고 error message를 input과 연결하는 것이다.

Q. placeholder만 있으면 label은 없어도 돼?
A. 권장하지 않는다. placeholder는 label을 대체하기 어렵다.

Q. 에러를 색상만으로 표시해도 돼?
A. 안 된다. 텍스트 메시지와 접근성 속성을 함께 제공해야 한다.

---

# 11. Label and Input Rules

## 11.1 Label Connection Rules

### [개념]

Label Connection은 `label htmlFor`와 `input id`를 연결해 input의 목적을 명확히 전달하는 기준이다.

스크린 리더와 클릭 UX 모두에 중요하다.

---

### [핵심]

Label 연결 요소:

- label
- htmlFor
- id
- input purpose
- visible label
- accessible name
- click target
- no placeholder-only
- unique id

---

### [실무]

좋은 예:

```tsx
<label htmlFor="nickname">닉네임</label>
<input
  id="nickname"
  {...register("nickname")}
/>
```

나쁜 예:

```tsx
<input placeholder="닉네임" {...register("nickname")} />
```

권장:

- 모든 input에 visible label 제공
- htmlFor와 id 일치
- id 중복 금지
- placeholder는 보조 문구로 사용
- checkbox/radio는 label로 클릭 영역 확장
- Custom Field에서도 id를 명시적으로 전달

---

### [FAQ]

Q. label은 꼭 필요해?
A. 권장한다. input의 목적을 명확히 하고 접근성과 클릭 UX를 개선한다.

Q. htmlFor는 무엇과 맞춰?
A. input의 id와 맞춘다.

Q. id가 중복되면 어떻게 돼?
A. label 연결과 aria-describedby 연결이 잘못될 수 있다.

Q. placeholder를 label 대신 쓰면 안 돼?
A. 권장하지 않는다. 입력 중 사라지고 접근성 측면에서 부족하다.

---

## 11.2 Required Field Indication

### [개념]

Required Field Indication은 필수 입력값을 사용자에게 명확히 알려주는 표시 기준이다.

필수 표시와 실제 validation 규칙은 일치해야 한다.

---

### [핵심]

필수 표시 요소:

- required field
- visual indication
- required text
- aria-required
- required attribute
- validation message
- consistency
- no color-only indication

---

### [실무]

필수 표시 예:

```tsx
<label htmlFor="email">
  이메일 <span aria-hidden="true">*</span>
</label>
<input
  id="email"
  aria-required="true"
  {...register("email", {
    required: "이메일을 입력해 주세요.",
  })}
/>
```

설명 문구 예:

```tsx
<p id="required-help">* 표시는 필수 입력 항목입니다.</p>
```

권장:

- 필수 field를 시각적으로 표시
- `*`만 사용하면 의미 설명 제공
- 색상만으로 필수 여부 표시 금지
- required 표시와 validation rule 일치
- optional field도 필요한 경우 명확히 표시

---

### [FAQ]

Q. 필수 입력 표시는 꼭 해야 해?
A. 권장한다. 사용자가 제출 전에 필수값을 알 수 있어야 한다.

Q. * 표시만 하면 충분해?
A. *의 의미를 설명하거나 필수 입력 문구를 함께 제공하는 것이 좋다.

Q. required 표시와 validation 규칙이 달라도 돼?
A. 안 된다. 표시와 실제 검증이 다르면 사용자 혼란이 생긴다.

Q. aria-required는 언제 써?
A. 필수 입력임을 보조기술에 전달하고 싶을 때 사용할 수 있다.

---

# 12. Error Accessibility Rules

## 12.1 aria-invalid Rules

### [개념]

`aria-invalid`는 특정 input의 현재 값이 유효하지 않음을 보조기술에 전달하는 속성이다.

Validation Error가 있을 때 `true`로 설정한다.

---

### [핵심]

aria-invalid 기준:

- invalid field
- Boolean error
- validation failed
- server error
- field error
- screen reader
- error state sync

---

### [실무]

예:

```tsx
<input id="email" aria-invalid={Boolean(errors.email)} {...register("email")} />
```

서버 에러도 동일:

```tsx
setError("email", {
  type: "server",
  message: "이미 사용 중인 이메일입니다.",
});
```

`errors.email`이 존재하면 `aria-invalid`는 true가 된다.

권장:

- Field Error가 있을 때 true
- Error가 없을 때 false 또는 undefined
- Client Error와 Server Error 모두 반영
- Custom Field에서 error prop으로 연결
- 색상 표시와 함께 aria-invalid 제공

---

### [FAQ]

Q. aria-invalid는 언제 써?
A. 해당 field에 validation error가 있을 때 사용한다.

Q. 서버 에러에도 aria-invalid를 적용해?
A. 적용하는 것이 좋다. 서버 Field Error도 해당 input의 오류이기 때문이다.

Q. aria-invalid만 있으면 에러 설명이 충분해?
A. 아니다. aria-describedby로 에러 메시지도 연결해야 한다.

Q. Error가 없을 때 aria-invalid는 true로 두면 안 돼?
A. 안 된다. 실제 오류 상태와 일치해야 한다.

---

## 12.2 aria-describedby Rules

### [개념]

`aria-describedby`는 input과 설명 문구 또는 에러 메시지를 연결하는 속성이다.

Validation Error가 발생했을 때 input이 어떤 오류를 갖는지 보조기술이 읽을 수 있게 한다.

---

### [핵심]

aria-describedby 사용 대상:

- error message
- helper text
- description text
- character count
- password policy
- field hint
- unique id
- multiple descriptions

---

### [실무]

Error 연결:

```tsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  aria-invalid={Boolean(errors.email)}
  aria-describedby={errors.email ? "email-error" : undefined}
  {...register("email")}
/>
{errors.email && (
  <p id="email-error" role="alert">
    {errors.email.message}
  </p>
)}
```

Helper Text와 Error 동시 연결:

```tsx
<input
  id="password"
  aria-describedby={
    errors.password
      ? "password-help password-error"
      : "password-help"
  }
/>
<p id="password-help">비밀번호는 8자 이상이어야 합니다.</p>
{errors.password && (
  <p id="password-error" role="alert">
    {errors.password.message}
  </p>
)}
```

권장:

- error message에 id 부여
- input aria-describedby와 error id 연결
- helper text도 연결 가능
- id 중복 금지
- Error가 없을 때 없는 id를 참조하지 않음

---

### [FAQ]

Q. aria-describedby는 왜 필요해?
A. input과 에러 메시지 또는 설명 문구를 연결해 보조기술이 읽을 수 있게 한다.

Q. helper text와 error를 동시에 연결할 수 있어?
A. 가능하다. 공백으로 여러 id를 연결할 수 있다.

Q. error가 없는데 aria-describedby가 error id를 참조해도 돼?
A. 권장하지 않는다. 존재하는 설명 id만 참조하는 것이 좋다.

Q. aria-describedby와 label은 같은 역할이야?
A. 아니다. label은 input 이름이고 aria-describedby는 추가 설명이다.

---

## 12.3 role alert Rules

### [개념]

`role="alert"`는 중요한 오류 메시지가 동적으로 나타났을 때 보조기술에 이를 알리는 역할을 한다.

Form Error Message에 자주 사용된다.

---

### [핵심]

role alert 사용 대상:

- validation error
- global error
- submit error
- server error
- dynamic error
- important feedback
- screen reader announcement

---

### [실무]

Field Error:

```tsx
{
  errors.email && (
    <p id="email-error" role="alert">
      {errors.email.message}
    </p>
  );
}
```

Global Error:

```tsx
{
  errors.root?.server && <p role="alert">{errors.root.server.message}</p>;
}
```

주의:

- 너무 많은 alert를 동시에 발생시키면 사용자 경험 저하 가능
- 중요한 오류 메시지에 사용
- 정적 도움말에는 role alert 불필요
- alert 메시지는 짧고 명확하게 작성
- Error Summary와 함께 사용 가능

---

### [FAQ]

Q. role alert는 언제 써?
A. validation error나 submit error처럼 중요한 동적 메시지를 알릴 때 사용한다.

Q. 모든 설명 문구에 role alert를 써야 해?
A. 아니다. 도움말이나 정적 설명에는 필요 없다.

Q. Field Error에 role alert를 써도 돼?
A. 가능하다. 오류가 동적으로 나타날 때 보조기술에 전달할 수 있다.

Q. alert가 너무 많으면 문제야?
A. 가능하다. 긴 Form에서는 Error Summary와 focus 관리 기준을 함께 고려한다.

---

# 13. Fieldset and Group Rules

## 13.1 Checkbox and Radio Group Accessibility

### [개념]

Checkbox Group과 Radio Group은 여러 선택지가 하나의 의미 단위로 묶인 Form Field다.

그룹 목적을 전달하기 위해 `fieldset`과 `legend`를 사용하는 것이 좋다.

---

### [핵심]

Group 접근성 요소:

- fieldset
- legend
- radio group
- checkbox group
- group label
- same name
- selected option
- group error
- aria-describedby

---

### [실무]

Radio Group 예:

```tsx
<fieldset>
  <legend>공개 범위</legend>

  <label>
    <input
      type="radio"
      value="PUBLIC"
      {...register("visibility", {
        required: "공개 범위를 선택해 주세요.",
      })}
    />
    공개
  </label>

  <label>
    <input type="radio" value="PRIVATE" {...register("visibility")} />
    비공개
  </label>

  {errors.visibility && <p role="alert">{errors.visibility.message}</p>}
</fieldset>
```

Checkbox Group 예:

```tsx
<fieldset>
  <legend>관심 테마</legend>

  {themeOptions.map((option) => (
    <label key={option.value}>
      <input type="checkbox" value={option.value} {...register("themeCodes")} />
      {option.label}
    </label>
  ))}
</fieldset>
```

권장:

- radio group에는 같은 field name 사용
- group 목적은 legend로 제공
- group error는 fieldset 내부에 표시
- 선택지 label을 명확히 작성
- checkbox group은 배열 값 처리 기준 확인

---

### [FAQ]

Q. radio group에는 fieldset이 필요해?
A. 권장한다. 그룹의 목적을 legend로 전달할 수 있다.

Q. checkbox group도 fieldset을 써야 해?
A. 여러 선택지가 하나의 질문이면 fieldset과 legend를 사용하는 것이 좋다.

Q. group error는 어디에 표시해?
A. fieldset 내부에서 group 선택지 근처에 표시하는 것이 좋다.

Q. radio option들은 같은 name을 써야 해?
A. 그렇다. 같은 그룹에서 하나만 선택되도록 같은 name을 사용한다.

---

# 14. Focus Management Rules

## 14.1 Focus on First Invalid Field

### [개념]

Focus on First Invalid Field는 Form 제출 실패 시 첫 번째 오류 Field로 focus를 이동시키는 접근성 및 UX 패턴이다.

긴 Form이나 회원가입 Form에서 사용자가 오류를 빠르게 수정할 수 있게 한다.

---

### [핵심]

Focus Management 요소:

- first invalid field
- submit failed
- setFocus
- keyboard user
- screen reader
- long form
- error summary
- no focus stealing during typing

---

### [실무]

React Hook Form `setFocus` 예:

```tsx
const {
  register,
  handleSubmit,
  setFocus,
} = useForm();

function handleInvalid(errors) {
  const firstErrorField = Object.keys(errors)[0];

  if (firstErrorField) {
    setFocus(firstErrorField);
  }
}

<form onSubmit={handleSubmit(submitForm, handleInvalid)}>
```

주의:

- submit 실패 시에만 focus 이동 권장
- onChange마다 focus 이동 금지
- Custom Component는 focus 연결이 필요할 수 있음
- 숨겨진 field로 focus 이동하지 않도록 주의
- Error Summary와 함께 사용 가능

---

### [FAQ]

Q. submit 실패 시 첫 오류 field로 focus 이동해야 해?
A. 필수는 아니지만 긴 Form에서는 사용자가 오류를 빠르게 수정할 수 있어 좋다.

Q. React Hook Form에서 focus 이동은 어떻게 해?
A. setFocus(fieldName)를 사용할 수 있다.

Q. 입력 중 validation 오류가 날 때마다 focus 이동해도 돼?
A. 권장하지 않는다. 사용자의 입력 흐름을 방해한다.

Q. Custom Component에서 setFocus가 안 되면?
A. ref forwarding 또는 Controller 연결 상태를 확인해야 한다.

---

## 14.2 Modal Form Focus Rules

### [개념]

Modal Form Focus Rules는 Modal 내부 Form이 열리고 닫힐 때 focus를 적절히 이동시키는 기준이다.

Modal Form에서는 focus trap, initial focus, close focus return이 중요하다.

---

### [핵심]

Modal Focus 요소:

- modal open focus
- initial focus
- focus trap
- close button
- return focus
- keyboard navigation
- escape close
- submit error focus

---

### [실무]

Modal Form Focus Flow:

```text
Open Modal
→ Move Focus into Modal
→ Keep Keyboard Focus inside Modal
→ Submit Failed
→ Focus First Invalid Field
→ Close Modal
→ Return Focus to Trigger Button
```

권장:

- Modal 열릴 때 제목 또는 첫 입력으로 focus 이동
- Modal 닫힐 때 열었던 버튼으로 focus 복귀
- Tab 이동이 Modal 밖으로 나가지 않도록 관리
- Escape close 지원 여부 명확화
- Modal 내부 Error도 aria-describedby로 연결

---

### [FAQ]

Q. Modal Form이 열리면 focus를 어디로 보내?
A. Modal 제목 또는 첫 번째 의미 있는 입력 요소로 보내는 것이 좋다.

Q. Modal을 닫으면 focus는 어디로 가야 해?
A. Modal을 연 trigger button으로 돌아가는 것이 좋다.

Q. Modal Form에서도 첫 오류 focus 이동이 필요해?
A. 긴 Modal Form에서는 유용하다.

Q. Modal 안에서 Tab이 밖으로 나가도 돼?
A. 일반적으로 Modal 내부에 focus가 머물도록 focus trap을 적용한다.

---

# 15. Keyboard Accessibility Rules

## 15.1 Keyboard Navigation

### [개념]

Keyboard Navigation은 마우스 없이 키보드만으로 Form을 입력, 선택, 제출, 취소할 수 있어야 한다는 기준이다.

모든 interactive element는 키보드로 접근 가능해야 한다.

---

### [핵심]

Keyboard 기준:

- Tab order
- focus visible
- Enter submit
- Space checkbox
- Arrow radio
- Escape modal
- button focus
- no keyboard trap
- logical order

---

### [실무]

권장:

```text
Tab
→ 다음 Form Field 이동

Shift + Tab
→ 이전 Form Field 이동

Enter
→ Form Submit

Space
→ Checkbox Toggle / Button Activate

Arrow Key
→ Radio Option 이동

Escape
→ Modal Close 정책에 따라 처리
```

주의:

- div를 button처럼 쓰지 않음
- custom button은 keyboard event 처리 필요
- focus outline 제거 금지 또는 대체 스타일 제공
- disabled 요소는 focus 불가
- 읽는 순서와 tab 순서 일치

---

### [FAQ]

Q. Form은 키보드만으로 사용할 수 있어야 해?
A. 그렇다. 모든 입력, 선택, 제출이 키보드로 가능해야 한다.

Q. Enter key로 submit이 되어야 해?
A. form onSubmit을 사용하면 자연스럽게 지원된다.

Q. focus outline을 없애도 돼?
A. 그냥 제거하면 안 된다. 대체 focus 표시가 필요하다.

Q. div를 버튼처럼 써도 돼?
A. 권장하지 않는다. 가능하면 button 요소를 사용한다.

---

# 16. Accessible Error Summary Rules

## 16.1 Error Summary

### [개념]

Error Summary는 Form 제출 실패 시 전체 오류 목록을 Form 상단에 요약해서 보여주는 패턴이다.

긴 Form, 회원가입 Form, 관리자 Form처럼 field가 많은 경우 유용하다.

---

### [핵심]

Error Summary 요소:

- error list
- form top
- field links
- focus summary
- first invalid field
- role alert
- accessible navigation
- long form

---

### [실무]

Error Summary 예:

```tsx
{
  Object.keys(errors).length > 0 && (
    <div role="alert" aria-labelledby="form-error-title">
      <h2 id="form-error-title">입력 내용을 확인해 주세요.</h2>
      <ul>
        {Object.entries(errors).map(([fieldName, error]) => (
          <li key={fieldName}>
            <button type="button" onClick={() => setFocus(fieldName)}>
              {error?.message}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
```

권장:

- 긴 Form에서 사용
- 각 오류를 해당 field focus로 연결
- Form 상단에 표시
- Field Error도 input 근처에 별도 표시
- Error Summary만 제공하고 Field Error를 생략하지 않음

---

### [FAQ]

Q. Error Summary는 언제 필요해?
A. field가 많은 긴 Form에서 전체 오류를 한 번에 보여줄 때 유용하다.

Q. Error Summary만 있으면 Field Error는 없어도 돼?
A. 권장하지 않는다. 각 field 근처에도 오류를 표시하는 것이 좋다.

Q. Error Summary 항목을 클릭하면 어떻게 해?
A. 해당 field로 focus 이동하는 것이 좋다.

Q. 짧은 Form에도 Error Summary가 필요해?
A. 필수는 아니다. 짧은 Form은 Field Error만으로 충분할 수 있다.

---

# 17. React Hook Form Troubleshooting

## 17.1 register Not Working

### [개념]

register Not Working은 input이 React Hook Form에 등록되지 않거나 값과 validation이 정상 처리되지 않는 문제다.

Custom Component에서 register props가 내부 input까지 전달되지 않을 때 자주 발생한다.

---

### [핵심]

주요 원인:

- register spread 누락
- name mismatch
- custom component ref missing
- onChange override
- disabled field
- unmounted field
- defaultValues missing
- register and Controller mixed

---

### [실무]

문제 예:

```tsx
<TextField {...register("email")} />
```

TextField 내부에서 register props를 input에 전달하지 않으면 동작하지 않는다.

수정 예:

```tsx
function TextField({ name, onChange, onBlur, ref, ...rest }) {
  return (
    <input
      name={name}
      onChange={onChange}
      onBlur={onBlur}
      ref={ref}
      {...rest}
    />
  );
}
```

권장:

- register props가 실제 input에 전달되는지 확인
- custom component는 forwardRef 고려
- register와 Controller 중 하나만 사용
- field name 오타 확인
- DevTools 또는 console로 values 확인

---

### [FAQ]

Q. register를 했는데 값이 안 들어와?
A. register props가 실제 input에 전달되는지 확인해야 한다.

Q. Custom Component에서 register가 안 먹는 이유는?
A. 내부 input에 name, onChange, onBlur, ref가 전달되지 않았을 수 있다.

Q. register와 Controller를 같이 쓰면 안 돼?
A. 같은 field에는 하나만 사용하는 것이 좋다.

Q. register field name 오타도 문제가 돼?
A. 그렇다. errors, values, request mapping이 모두 어긋날 수 있다.

---

## 17.2 Server Error Not Displayed

### [개념]

Server Error Not Displayed는 서버 오류를 받았지만 React Hook Form Field Error 또는 Global Error UI에 표시되지 않는 문제다.

setError field name 불일치, root error 출력 누락, mapping 실패가 주요 원인이다.

---

### [핵심]

주요 원인:

- setError not called
- wrong field name
- register name mismatch
- root error not rendered
- error.message missing
- server response path mismatch
- catch block missing

---

### [실무]

Debug Flow:

```text
Network Response 확인
→ mapApiError 결과 확인
→ setError 호출 확인
→ fieldName과 register name 확인
→ errors 출력 확인
→ Error UI rendering 확인
```

문제 예:

```tsx
setError("userEmail", {
  type: "server",
  message: "이미 사용 중인 이메일입니다.",
});
```

register field:

```tsx
<input {...register("email")} />
```

수정:

```tsx
setError("email", {
  type: "server",
  message: "이미 사용 중인 이메일입니다.",
});
```

---

### [FAQ]

Q. 서버 에러가 React Hook Form에 표시되지 않아?
A. setError field name과 register name이 일치하는지 확인해야 한다.

Q. root.server error가 안 보여?
A. errors.root?.server를 렌더링하고 있는지 확인해야 한다.

Q. 서버 응답에는 errors가 있는데 setError가 안 돼?
A. response mapping 경로와 반복문 적용 여부를 확인해야 한다.

Q. setError에 message가 없으면?
A. UI에서 표시할 메시지가 없을 수 있으므로 fallback message를 제공해야 한다.

---

## 17.3 isDirty Not Working

### [개념]

isDirty Not Working은 Form 값이 변경되었는데도 `isDirty`가 예상과 다르게 동작하는 문제다.

defaultValues 누락, reset 기준 오류, 타입 불일치가 주요 원인이다.

---

### [핵심]

주요 원인:

- defaultValues missing
- reset not called
- async data not reflected
- value type mismatch
- number string mismatch
- file input
- object reference
- uncontrolled custom component

---

### [실무]

문제 Flow:

```text
Server Data Loaded
→ defaultValues는 초기 렌더 기준
→ reset 미호출
→ isDirty 기준 불일치
```

수정:

```tsx
useEffect(() => {
  if (profile) {
    reset({
      nickname: profile.nickname ?? "",
      bio: profile.bio ?? "",
    });
  }
}, [profile, reset]);
```

주의:

- async server data는 reset으로 반영
- number/string 타입이 defaultValues와 현재값에서 일치해야 함
- file input dirty는 별도 기준 필요
- 수정 성공 후 latest values로 reset
- defaultValues 없이 dirty 판단 기대 금지

---

### [FAQ]

Q. isDirty가 true가 안 돼?
A. defaultValues가 없거나 field 값 변경이 React Hook Form에 반영되지 않았을 수 있다.

Q. 서버 데이터 로딩 후 isDirty가 이상해?
A. reset으로 서버 데이터를 Form 기준값으로 반영해야 한다.

Q. 수정 성공 후 isDirty가 계속 true야?
A. 저장된 최신 값으로 reset하지 않았을 가능성이 크다.

Q. file input도 isDirty가 정확해?
A. 파일은 별도 dirty 기준을 두는 것이 안전할 수 있다.

---

# 18. Accessibility Troubleshooting

## 18.1 Label Not Connected

### [개념]

Label Not Connected는 label과 input이 연결되지 않아 스크린 리더나 클릭 UX가 제대로 동작하지 않는 문제다.

`htmlFor`와 `id` 불일치, id 중복, label 누락이 원인이다.

---

### [핵심]

주요 원인:

- label missing
- htmlFor mismatch
- input id missing
- duplicate id
- custom field id not passed
- placeholder-only
- hidden label issue

---

### [실무]

Debug Flow:

```text
label 존재 확인
→ htmlFor 확인
→ input id 확인
→ htmlFor와 id 일치 확인
→ id 중복 확인
→ Custom Field id 전달 확인
```

문제 예:

```tsx
<label htmlFor="email">이메일</label>
<input id="userEmail" />
```

수정:

```tsx
<label htmlFor="email">이메일</label>
<input id="email" />
```

---

### [FAQ]

Q. label을 클릭해도 input focus가 안 가?
A. label htmlFor와 input id가 일치하는지 확인해야 한다.

Q. id가 없어도 label이 연결돼?
A. wrapping label 방식도 가능하지만 htmlFor/id 연결이 명확하다.

Q. id 중복이 문제가 돼?
A. 문제가 된다. label과 aria 연결이 잘못될 수 있다.

Q. placeholder만 있으면 접근성 문제가 생겨?
A. 생길 수 있다. visible label을 제공하는 것이 좋다.

---

## 18.2 Error Not Announced

### [개념]

Error Not Announced는 에러 메시지가 화면에는 보이지만 스크린 리더 사용자에게 제대로 전달되지 않는 문제다.

aria-describedby 누락, role alert 누락, id 불일치가 주요 원인이다.

---

### [핵심]

주요 원인:

- aria-describedby missing
- error id mismatch
- role alert missing
- aria-invalid missing
- error rendered far away
- dynamic message not announced
- hidden error text

---

### [실무]

Debug Flow:

```text
Error message id 확인
→ input aria-describedby 확인
→ id 일치 확인
→ aria-invalid 확인
→ role alert 확인
→ Error rendering 조건 확인
```

좋은 예:

```tsx
<input
  id="email"
  aria-invalid={Boolean(errors.email)}
  aria-describedby={errors.email ? "email-error" : undefined}
/>;
{
  errors.email && (
    <p id="email-error" role="alert">
      {errors.email.message}
    </p>
  );
}
```

권장:

- Field Error는 input과 연결
- Global Error는 role alert 적용
- Error Summary는 Form 상단에 제공 가능
- 색상만으로 오류 표시 금지
- error id 중복 금지

---

### [FAQ]

Q. 에러가 화면에는 보이는데 스크린 리더가 못 읽어?
A. aria-describedby와 role alert 연결을 확인해야 한다.

Q. aria-invalid만 있으면 충분해?
A. 아니다. 오류 설명을 aria-describedby로 연결해야 한다.

Q. role alert가 없으면 에러를 못 읽어?
A. 상황에 따라 동적 에러 알림이 약해질 수 있다.

Q. Error id가 중복되면 문제가 돼?
A. 문제가 된다. input이 잘못된 설명을 참조할 수 있다.

---

# 19. React Hook Form and Accessibility Checklist

## 19.1 Implementation Checklist

### [개념]

React Hook Form and Accessibility Checklist는 React Hook Form 적용과 Form Accessibility가 안정적으로 구현되었는지 검수하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] React Hook Form 도입 필요성이 명확한가?
- [ ] 간단한 Form에 과도하게 도입하지 않았는가?
- [ ] useForm defaultValues가 명확한가?
- [ ] 서버 데이터 로딩 후 reset 기준이 있는가?
- [ ] register field name과 Request Mapping key가 일치하는가?
- [ ] register validation message가 명확한가?
- [ ] handleSubmit을 form onSubmit에 올바르게 연결했는가?
- [ ] isSubmitting으로 submit button disabled를 처리하는가?
- [ ] 서버 Field Error를 setError로 mapping하는가?
- [ ] Global Error를 root error 또는 별도 state로 표시하는가?
- [ ] Controller가 필요한 외부 controlled component에만 사용되었는가?
- [ ] Controller field가 defaultValues에 포함되어 있는가?
- [ ] watch를 필요한 field에만 사용하고 있는가?
- [ ] reset 후 isDirty 기준이 안정적인가?
- [ ] label htmlFor와 input id가 연결되어 있는가?
- [ ] placeholder를 label 대체로 사용하지 않는가?
- [ ] 필수 입력 표시와 validation rule이 일치하는가?
- [ ] Field Error에 aria-invalid가 적용되어 있는가?
- [ ] Field Error에 aria-describedby가 연결되어 있는가?
- [ ] Error Message에 role alert가 필요한 곳에 적용되어 있는가?
- [ ] radio / checkbox group에 fieldset / legend를 검토했는가?
- [ ] submit 실패 시 첫 오류 field focus 이동을 검토했는가?
- [ ] keyboard navigation이 가능한가?
- [ ] focus visible을 제거하지 않았는가?
- [ ] 긴 Form에서 Error Summary를 검토했는가?
```

---

### [실무]

검수 Flow:

```text
RHF Need Check
→ useForm / defaultValues Check
→ register / Controller Check
→ Validation Check
→ Server Error Mapping Check
→ reset / dirty Check
→ Label Connection Check
→ Error Accessibility Check
→ Focus Management Check
→ Keyboard Navigation Check
→ Troubleshooting Review
```

---

### [FAQ]

Q. React Hook Form 검수에서 가장 중요한 것은?
A. defaultValues, register name, handleSubmit, setError, reset, Controller 사용 기준이다.

Q. Accessibility 검수에서 가장 중요한 것은?
A. label 연결, aria-invalid, aria-describedby, role alert, focus management, keyboard navigation이다.

Q. React Hook Form 다음에는 무엇을 검토해?
A. Form Component Design, Troubleshooting, Security, Checklist, Retrieval Optimization을 검토한다.

---

# Retrieval Queries

### [FAQ]

Q. React Hook Form이 뭐야?
A. React Form의 입력값, 검증, 에러, 제출 상태를 효율적으로 관리하는 Form Library다.

Q. 모든 Form에 React Hook Form을 써야 해?
A. 아니다. 간단한 Form은 useState로 충분하고 복잡한 Form에서 도입을 검토한다.

Q. React Hook Form은 언제 쓰는 게 좋아?
A. 필드가 많고 검증, touched, dirty, server error 관리가 복잡할 때 좋다.

Q. React Hook Form은 Controlled Component야?
A. 기본적으로 uncontrolled 기반으로 효율적으로 동작하지만 Controller를 통해 controlled component도 연결할 수 있다.

Q. React Hook Form 도입 기준은 뭐야?
A. 필드 수, 검증 복잡도, touched/dirty 필요성, server error 처리 복잡도를 기준으로 판단한다.

Q. 작은 검색 Form에도 React Hook Form이 필요해?
A. 필수는 아니다. keyword 하나 정도는 useState가 더 단순할 수 있다.

Q. 회원가입 Form은 React Hook Form을 써도 좋아?
A. 필드와 검증이 많기 때문에 도입을 검토하기 좋다.

Q. useForm은 뭐야?
A. React Hook Form에서 Form 상태와 제출, 검증을 관리하는 핵심 Hook이다.

Q. useForm에서 defaultValues는 꼭 필요해?
A. 권장한다. 초기값을 명확히 하면 reset과 dirty 관리가 안정적이다.

Q. formState.errors는 뭐야?
A. register validation 또는 setError로 발생한 field error를 담는 객체다.

Q. isSubmitting은 언제 true가 돼?
A. handleSubmit으로 실행된 async submit 함수가 진행 중일 때 true가 된다.

Q. defaultValues는 왜 중요해?
A. 초기값, reset 기준, dirty check 기준이 되기 때문이다.

Q. 서버 데이터가 늦게 오면 defaultValues가 자동으로 바뀌어?
A. 아니다. 보통 reset을 호출해 서버 데이터를 Form에 반영한다.

Q. defaultValues에 undefined를 넣어도 돼?
A. 권장하지 않는다. 빈 문자열, false, [] 같은 명확한 값이 좋다.

Q. 수정 Form 성공 후에는 어떻게 해?
A. 서버 최신값으로 reset해서 defaultValues와 현재 values를 맞추는 것이 좋다.

Q. register는 뭐야?
A. input을 React Hook Form에 등록해 값과 검증 상태를 관리하게 하는 함수다.

Q. register 이름은 무엇과 맞춰야 해?
A. Form Values key, Request DTO mapping, Error Mapping 기준과 맞추는 것이 좋다.

Q. register 안에 validation 규칙을 넣어도 돼?
A. 가능하다. required, minLength, pattern 같은 기본 검증을 넣을 수 있다.

Q. register를 custom component에 그대로 넘겨도 돼?
A. 가능하지만 내부 input에 ref, name, onChange, onBlur가 제대로 전달되어야 한다.

Q. register validation은 언제 적합해?
A. required, minLength, pattern 같은 간단한 field-level validation에 적합하다.

Q. 공백만 입력한 값은 required로 막을 수 있어?
A. required만으로는 부족할 수 있어 validate에서 trim 검증을 추가할 수 있다.

Q. valueAsNumber는 뭐야?
A. input 값을 number로 변환해 Form Values에 저장하는 옵션이다.

Q. handleSubmit은 뭐야?
A. React Hook Form에서 validation 후 submit 함수를 실행하는 submit wrapper다.

Q. handleSubmit은 preventDefault를 대신 해?
A. 기본 submit 이벤트 처리를 포함하므로 별도 preventDefault를 직접 작성하지 않아도 된다.

Q. onSubmit={handleSubmit(submitForm())}은 왜 문제야?
A. submitForm이 렌더링 중 즉시 실행될 수 있으므로 함수 참조를 전달해야 한다.

Q. handleSubmit에서 validation 실패하면 submitForm이 실행돼?
A. 아니다. validation 실패 시 valid submit 함수는 실행되지 않는다.

Q. isSubmitting은 언제 사용해?
A. 제출 중 버튼 비활성화, 로딩 문구, 중복 제출 방지에 사용한다.

Q. isSubmitting을 쓰면 별도 submitting state가 필요 없어?
A. 대부분 handleSubmit 기반 Form에서는 isSubmitting으로 충분하다.

Q. async submit에서 try/catch가 필요해?
A. 필요하다. 서버 에러를 Form UI에 mapping해야 한다.

Q. formState.errors는 뭐야?
A. React Hook Form이 관리하는 Field Error 객체다.

Q. 에러 메시지는 어떻게 꺼내?
A. 보통 `errors.email?.message`처럼 field별 message를 사용한다.

Q. errors를 직접 setState로 바꿔도 돼?
A. React Hook Form에서는 setError, clearErrors 같은 API를 사용한다.

Q. touchedFields는 뭐야?
A. 사용자가 blur 등으로 방문한 field를 나타내는 상태다.

Q. dirtyFields는 뭐야?
A. defaultValues와 달라진 field를 나타내는 상태다.

Q. isDirty는 언제 유용해?
A. 수정 Form에서 변경사항 저장 버튼 활성화나 이탈 경고에 유용하다.

Q. reset하면 isDirty는 어떻게 돼?
A. reset된 값이 새 기준이 되면 isDirty가 false가 된다.

Q. setError는 언제 써?
A. 서버 검증 오류나 수동 검증 오류를 React Hook Form errors에 넣을 때 사용한다.

Q. 서버 Field Error를 setError로 넣을 수 있어?
A. 가능하다. field name과 message를 mapping하면 된다.

Q. setError field name은 무엇과 맞춰야 해?
A. register에 사용한 field name과 맞춰야 한다.

Q. Global Error도 setError로 처리할 수 있어?
A. root error로 처리할 수 있지만 별도 submitError state를 사용하는 방식도 가능하다.

Q. React Hook Form에서 서버 에러는 어떻게 넣어?
A. setError를 사용해 field error 또는 root error로 넣는다.

Q. 서버 errors 객체를 그대로 setError에 넣을 수 있어?
A. 반복문으로 fieldName과 message를 하나씩 setError에 전달해야 한다.

Q. Global Error는 root error가 좋아 별도 state가 좋아?
A. 팀 컨벤션에 따라 선택한다. root error는 RHF 내부 관리, 별도 state는 명시적 관리가 쉽다.

Q. reset은 뭐야?
A. React Hook Form의 값과 formState를 초기화하거나 새 값으로 재설정하는 함수다.

Q. Submit 성공 후 reset해도 돼?
A. 생성 Form은 가능하고 수정 Form은 서버 최신값으로 reset하는 것이 좋다.

Q. Submit 실패 후 reset해도 돼?
A. 보통 하지 않는다. 사용자가 수정 후 다시 제출할 수 있어야 한다.

Q. watch는 뭐야?
A. Form Field의 현재 값을 구독해 UI나 validation에 사용할 수 있는 함수다.

Q. watch는 언제 써?
A. 글자 수 표시, 비밀번호 확인, 조건부 field 표시, 실시간 미리보기에 사용한다.

Q. watch를 많이 쓰면 문제야?
A. re-render가 늘어날 수 있어 필요한 field만 구독하는 것이 좋다.

Q. Controller는 뭐야?
A. React Hook Form에서 controlled custom component를 연결하기 위한 컴포넌트다.

Q. 언제 Controller를 써?
A. register만으로 연결하기 어려운 Custom Select, DatePicker, UI Library Input에 사용한다.

Q. 기본 input에도 Controller를 써야 해?
A. 보통 기본 input은 register로 충분하다.

Q. Controller에서 값이 안 바뀌는 이유는?
A. field.value 또는 field.onChange를 Custom Component에 제대로 전달하지 않았을 수 있다.

Q. Custom Select onChange가 option 객체를 주면 어떻게 해?
A. field.onChange에 option.value처럼 필요한 값만 넘기도록 변환한다.

Q. Controller field도 defaultValues에 넣어야 해?
A. 권장한다. 초기값과 dirty 관리가 안정적이다.

Q. Schema Validation이 뭐야?
A. Zod나 Yup 같은 schema로 Form Validation 규칙을 선언하는 방식이다.

Q. React Hook Form과 schema validation을 같이 쓸 수 있어?
A. 가능하다. resolver를 사용해 연결할 수 있다.

Q. 모든 Form에 Zod를 써야 해?
A. 아니다. 복잡한 Form에서 도입을 검토한다.

Q. Form Accessibility가 뭐야?
A. 모든 사용자가 Form을 이해하고 입력하고 오류를 수정할 수 있도록 만드는 접근성 기준이다.

Q. Form 접근성에서 가장 기본은 뭐야?
A. label과 input을 연결하고 error message를 input과 연결하는 것이다.

Q. placeholder만 있으면 label은 없어도 돼?
A. 권장하지 않는다. placeholder는 label을 대체하기 어렵다.

Q. 에러를 색상만으로 표시해도 돼?
A. 안 된다. 텍스트 메시지와 접근성 속성을 함께 제공해야 한다.

Q. label은 꼭 필요해?
A. 권장한다. input의 목적을 명확히 하고 접근성과 클릭 UX를 개선한다.

Q. htmlFor는 무엇과 맞춰?
A. input의 id와 맞춘다.

Q. id가 중복되면 어떻게 돼?
A. label 연결과 aria-describedby 연결이 잘못될 수 있다.

Q. 필수 입력 표시는 꼭 해야 해?
A. 권장한다. 사용자가 제출 전에 필수값을 알 수 있어야 한다.

Q. * 표시만 하면 충분해?
A. *의 의미를 설명하거나 필수 입력 문구를 함께 제공하는 것이 좋다.

Q. required 표시와 validation 규칙이 달라도 돼?
A. 안 된다. 표시와 실제 검증이 다르면 사용자 혼란이 생긴다.

Q. aria-invalid는 언제 써?
A. 해당 field에 validation error가 있을 때 사용한다.

Q. 서버 에러에도 aria-invalid를 적용해?
A. 적용하는 것이 좋다. 서버 Field Error도 해당 input의 오류이기 때문이다.

Q. aria-invalid만 있으면 에러 설명이 충분해?
A. 아니다. aria-describedby로 에러 메시지도 연결해야 한다.

Q. aria-describedby는 왜 필요해?
A. input과 에러 메시지 또는 설명 문구를 연결해 보조기술이 읽을 수 있게 한다.

Q. helper text와 error를 동시에 연결할 수 있어?
A. 가능하다. 공백으로 여러 id를 연결할 수 있다.

Q. role alert는 언제 써?
A. validation error나 submit error처럼 중요한 동적 메시지를 알릴 때 사용한다.

Q. Field Error에 role alert를 써도 돼?
A. 가능하다. 오류가 동적으로 나타날 때 보조기술에 전달할 수 있다.

Q. radio group에는 fieldset이 필요해?
A. 권장한다. 그룹의 목적을 legend로 전달할 수 있다.

Q. checkbox group도 fieldset을 써야 해?
A. 여러 선택지가 하나의 질문이면 fieldset과 legend를 사용하는 것이 좋다.

Q. group error는 어디에 표시해?
A. fieldset 내부에서 group 선택지 근처에 표시하는 것이 좋다.

Q. submit 실패 시 첫 오류 field로 focus 이동해야 해?
A. 필수는 아니지만 긴 Form에서는 사용자가 오류를 빠르게 수정할 수 있어 좋다.

Q. React Hook Form에서 focus 이동은 어떻게 해?
A. setFocus(fieldName)를 사용할 수 있다.

Q. Modal Form이 열리면 focus를 어디로 보내?
A. Modal 제목 또는 첫 번째 의미 있는 입력 요소로 보내는 것이 좋다.

Q. Modal을 닫으면 focus는 어디로 가야 해?
A. Modal을 연 trigger button으로 돌아가는 것이 좋다.

Q. Form은 키보드만으로 사용할 수 있어야 해?
A. 그렇다. 모든 입력, 선택, 제출이 키보드로 가능해야 한다.

Q. Enter key로 submit이 되어야 해?
A. form onSubmit을 사용하면 자연스럽게 지원된다.

Q. focus outline을 없애도 돼?
A. 그냥 제거하면 안 된다. 대체 focus 표시가 필요하다.

Q. Error Summary는 언제 필요해?
A. field가 많은 긴 Form에서 전체 오류를 한 번에 보여줄 때 유용하다.

Q. Error Summary만 있으면 Field Error는 없어도 돼?
A. 권장하지 않는다. 각 field 근처에도 오류를 표시하는 것이 좋다.

Q. register를 했는데 값이 안 들어와?
A. register props가 실제 input에 전달되는지 확인해야 한다.

Q. Custom Component에서 register가 안 먹는 이유는?
A. 내부 input에 name, onChange, onBlur, ref가 전달되지 않았을 수 있다.

Q. 서버 에러가 React Hook Form에 표시되지 않아?
A. setError field name과 register name이 일치하는지 확인해야 한다.

Q. isDirty가 true가 안 돼?
A. defaultValues가 없거나 field 값 변경이 React Hook Form에 반영되지 않았을 수 있다.

Q. 서버 데이터 로딩 후 isDirty가 이상해?
A. reset으로 서버 데이터를 Form 기준값으로 반영해야 한다.

Q. label을 클릭해도 input focus가 안 가?
A. label htmlFor와 input id가 일치하는지 확인해야 한다.

Q. 에러가 화면에는 보이는데 스크린 리더가 못 읽어?
A. aria-describedby와 role alert 연결을 확인해야 한다.

Q. React Hook Form 다음 문서는 뭐가 좋아?
A. Form Component Design, Troubleshooting, Security, Checklist, Retrieval Optimization 순서가 좋다.
