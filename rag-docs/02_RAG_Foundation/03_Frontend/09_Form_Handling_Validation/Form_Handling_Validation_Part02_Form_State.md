# Form Handling & Validation Part02 - Form State

---

# 1. Form State Foundation

## 1.1 Form State Definition

### [개념]

Form State는 사용자가 Form에 입력한 값과 Form 처리 상태를 React에서 관리하는 상태다.

Form State는 단순 입력값만 의미하지 않는다.

입력값, 에러, 방문 여부, 수정 여부, 제출 상태, 서버 에러, 초기값까지 포함할 수 있다.

---

### [핵심]

Form State 핵심 요소:

- values
- errors
- touched
- dirty
- submitting
- submitError
- fieldError
- globalError
- initialValues
- isValid
- canSubmit
- reset state
- Form State Location
- Local State
- URL State
- Server State

---

### [실무]

2026 실무 기준에서 Form State는 아래처럼 역할을 분리한다.

```text
Form Values
→ 사용자가 입력 중인 값

Error State
→ Client Validation / Server Validation Error

Submit State
→ API 요청 중 여부

Initial Values
→ 수정 Form 또는 reset 기준

Server State
→ 서버에서 받은 원본 데이터
```

기본 Flow:

```text
Initialize Form State
→ User Input
→ Update Values
→ Validate Values
→ Update Errors
→ Submit
→ Update Submitting
→ Success / Failure
→ Reset or Keep Values
```

---

### [FAQ]

Q. Form State가 뭐야?
A. 사용자가 입력한 값과 에러, 제출 상태, 초기값 등을 React에서 관리하는 상태다.

Q. Form State는 입력값만 의미해?
A. 아니다. values, errors, touched, dirty, submitting, submitError 같은 상태를 포함할 수 있다.

Q. Form State에서 가장 중요한 것은 뭐야?
A. 입력값과 에러 상태를 분리하고, 제출 상태를 명확히 관리하는 것이다.

Q. Form State는 Server State와 같아?
A. 아니다. Server State는 서버에서 받은 데이터이고 Form State는 사용자가 수정 중인 임시 입력값이다.

---

# 2. Values State Rules

## 2.1 Values State Design

### [개념]

Values State는 Form Field의 현재 입력값을 저장하는 상태다.

입력 필드가 적으면 개별 useState를 사용할 수 있고, 필드가 많으면 객체 형태의 values를 사용할 수 있다.

---

### [핵심]

Values State 설계 기준:

- 단일 field
- multiple fields
- object values
- initialValues
- name key matching
- string input
- boolean input
- array input
- number input
- enum input
- nested values
- Request Body Mapping

---

### [실무]

단일 입력값 예:

```jsx
const [keyword, setKeyword] = useState("");
```

여러 입력값 예:

```jsx
const initialValues = {
  email: "",
  password: "",
  nickname: "",
  agreed: false,
};

const [values, setValues] = useState(initialValues);
```

공통 handler와 연결:

```jsx
function handleChange(event) {
  const { name, value } = event.target;

  setValues((prevValues) => ({
    ...prevValues,
    [name]: value,
  }));
}
```

권장:

- 문자열 입력값 초기값은 `""`
- checkbox 초기값은 `false`
- 다중 선택 초기값은 `[]`
- input `name`과 values key 일치
- API Request Body와 Form Values를 무조건 동일시하지 않음
- 필요 시 mapper 함수로 변환

---

### [FAQ]

Q. Form 입력값은 각각 useState로 둬야 해?
A. 입력값이 적으면 각각 useState도 가능하다.

Q. 필드가 많으면 Form State는 어떻게 관리해?
A. values 객체로 관리하면 공통 handleChange와 Request Body Mapping에 유리하다.

Q. input name과 values key는 같아야 해?
A. 공통 handleChange를 사용한다면 같게 맞추는 것이 좋다.

Q. Form Values를 그대로 API body로 보내도 돼?
A. 간단한 경우 가능하지만 trim, Number 변환, field mapping이 필요하면 Request DTO로 변환해야 한다.

---

## 2.2 Initial Values Rules

### [개념]

Initial Values는 Form State의 최초 값이자 reset 기준이다.

Controlled Component에서 initialValues가 불명확하면 uncontrolled to controlled warning이 발생할 수 있다.

---

### [핵심]

초기값 기준:

- text: `""`
- textarea: `""`
- select: `""`
- checkbox: `false`
- radio: `""`
- multiple checkbox: `[]`
- number input: `""` 또는 명확한 숫자
- object field: 기본 객체
- optional field: `""` 또는 null 기준 명확화

---

### [실무]

생성 Form 예:

```javascript
const initialValues = {
  title: "",
  content: "",
  category: "",
  agreed: false,
};
```

수정 Form 예:

```javascript
const initialValues = {
  title: post.title ?? "",
  content: post.content ?? "",
  category: post.category ?? "",
};
```

React State 적용:

```jsx
const [values, setValues] = useState(initialValues);
```

주의:

- API 데이터 로딩 전 undefined value 방지
- 수정 Form에서는 서버 원본과 사용자 입력값 구분
- reset 기준으로 initialValues를 재사용 가능
- 초기값 변경 시 Form State 동기화 기준 필요
- defaultValue와 value 혼용 금지

---

### [FAQ]

Q. initialValues가 왜 중요해?
A. Controlled Component 안정성과 Form Reset 기준을 결정하기 때문이다.

Q. 문자열 input 초기값은 무엇이 좋아?
A. 빈 문자열 `""`이 안전하다.

Q. checkbox 초기값은 무엇이 좋아?
A. false가 일반적이다.

Q. API 데이터가 아직 없을 때 Form 초기값은 어떻게 해?
A. undefined가 들어가지 않도록 빈 문자열, false, [] 같은 기본값을 사용한다.

---

# 3. Error State Rules

## 3.1 Error State Definition

### [개념]

Error State는 Form Validation 실패 결과를 저장하는 상태다.

Client Validation Error와 Server Validation Error를 Field Error 또는 Global Error로 나누어 관리한다.

---

### [핵심]

Error State 종류:

- errors
- fieldError
- globalError
- submitError
- client error
- server error
- validation error
- error message
- errors key
- field name matching

---

### [실무]

기본 Error State 예:

```javascript
const [errors, setErrors] = useState({});
const [submitError, setSubmitError] = useState("");
```

Field Error 예:

```javascript
const errors = {
  email: "이메일 형식이 올바르지 않습니다.",
  password: "비밀번호를 입력해 주세요.",
};
```

Global Error 예:

```javascript
const submitError = "이메일 또는 비밀번호가 일치하지 않습니다.";
```

권장:

- field별 오류는 errors 객체로 관리
- Form 전체 오류는 submitError 또는 globalError로 관리
- errors key와 input name 일치
- Client Error와 Server Error를 표시 구조에서 통합 가능
- 민감한 내부 서버 오류 메시지 노출 금지

---

### [FAQ]

Q. Error State가 뭐야?
A. Form 검증 실패 메시지와 서버 오류 메시지를 저장하는 상태다.

Q. Field Error와 Global Error 차이는?
A. Field Error는 특정 input에 연결되고 Global Error는 Form 전체 실패를 나타낸다.

Q. errors 객체 key는 무엇과 맞춰야 해?
A. input name 또는 Form Values key와 맞추는 것이 좋다.

Q. submitError는 언제 사용해?
A. 로그인 실패, 권한 없음, 서버 오류처럼 특정 field가 아닌 Form 전체 오류에 사용한다.

---

## 3.2 Field Error Rules

### [개념]

Field Error는 특정 입력 필드에 연결되는 에러다.

예:

- email 형식 오류
- password 미입력
- nickname 길이 오류
- content 공백 오류
- rating 범위 오류

---

### [핵심]

Field Error 기준:

- specific field
- input name
- errors[fieldName]
- error message near input
- aria-invalid
- aria-describedby
- role alert
- touched condition
- submit condition

---

### [실무]

Field Error 출력 예:

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

- 에러 메시지는 해당 input 근처에 표시
- `aria-invalid`로 오류 여부 전달
- `aria-describedby`로 input과 error message 연결
- submit 후 또는 touched 이후 표시 기준 선택
- Server Field Error도 같은 위치에 표시 가능

---

### [FAQ]

Q. Field Error는 어디에 보여줘?
A. 해당 input 근처에 보여주는 것이 좋다.

Q. Field Error는 어떤 State에 저장해?
A. 보통 errors 객체에 field name을 key로 저장한다.

Q. 에러 메시지를 input과 연결해야 해?
A. 권장한다. aria-describedby를 사용하면 접근성이 좋아진다.

Q. Field Error는 submit 전에도 보여줘야 해?
A. UX에 따라 다르지만 보통 touched 이후 또는 submit 이후 표시한다.

---

## 3.3 Global Error Rules

### [개념]

Global Error는 특정 input 하나에 연결하기 어려운 Form 전체 오류다.

로그인 실패, 서버 장애, 권한 오류, 네트워크 오류, 알 수 없는 제출 실패에 사용한다.

---

### [핵심]

Global Error 사용 대상:

- login failure
- authentication failure
- authorization failure
- network error
- server error
- duplicate submit failure
- unknown error
- global validation failure
- submitError

---

### [실무]

Global Error 출력 예:

```jsx
{
  submitError && (
    <p role="alert" className="form-error">
      {submitError}
    </p>
  );
}
```

로그인 실패 예:

```javascript
setSubmitError("이메일 또는 비밀번호가 일치하지 않습니다.");
```

권장:

- Form 상단 또는 submit button 근처에 표시
- 사용자에게 복구 가능한 메시지 제공
- 서버 내부 정보 노출 금지
- Field Error와 동시에 표시 가능
- submit 재시도 시 이전 Global Error 초기화

---

### [FAQ]

Q. Global Error는 언제 사용해?
A. 특정 field가 아니라 Form 전체 실패를 나타낼 때 사용한다.

Q. 로그인 실패는 Field Error야 Global Error야?
A. 계정 정보 불일치는 보통 Global Error로 처리한다.

Q. 서버 장애 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 정보가 노출되지 않도록 사용자 친화 메시지로 관리한다.

Q. Global Error는 어디에 보여줘?
A. Form 상단 또는 제출 버튼 근처에 보여주는 것이 일반적이다.

---

# 4. Touched State Rules

## 4.1 Touched State Definition

### [개념]

Touched State는 사용자가 특정 Field를 방문하거나 blur한 적이 있는지 나타내는 상태다.

Touched는 에러 메시지를 언제 표시할지 결정하는 데 사용한다.

---

### [핵심]

Touched State 핵심 요소:

- touched
- onBlur
- visited field
- error display timing
- UX validation
- field interaction
- touched[fieldName]

---

### [실무]

Touched State 예:

```javascript
const [touched, setTouched] = useState({});
```

onBlur 처리:

```jsx
function handleBlur(event) {
  const { name } = event.target;

  setTouched((prevTouched) => ({
    ...prevTouched,
    [name]: true,
  }));
}
```

에러 표시 기준:

```jsx
{
  touched.email && errors.email && (
    <p id="email-error" role="alert">
      {errors.email}
    </p>
  );
}
```

권장:

- 사용자가 방문한 field에만 즉시 에러 표시 가능
- submit 후에는 전체 에러 표시 가능
- 입력 전부터 모든 에러를 노출하지 않음
- onBlur 기반 validation과 함께 사용 가능

---

### [FAQ]

Q. touched가 뭐야?
A. 사용자가 해당 field를 방문하거나 blur한 적이 있는지를 나타내는 상태다.

Q. touched는 왜 필요해?
A. 사용자가 입력하기 전부터 에러가 보이는 UX를 방지하기 위해 사용한다.

Q. touched는 언제 true로 바꿔?
A. 보통 input의 onBlur 이벤트에서 true로 바꾼다.

Q. submit 후에는 touched가 없어도 에러를 보여줘?
A. 보통 submit 후에는 전체 validation error를 표시한다.

---

## 4.2 Touched Error Display

### [개념]

Touched Error Display는 사용자가 상호작용한 Field에 대해서만 에러 메시지를 표시하는 방식이다.

불필요하게 빠른 에러 노출을 줄이고 사용성을 개선한다.

---

### [핵심]

표시 기준:

- show after blur
- show after touched
- show after submit
- hide before interaction
- UX-friendly validation
- field-level feedback

---

### [실무]

표시 조건 예:

```javascript
const shouldShowEmailError = touched.email && errors.email;
```

submit 이후 전체 표시 예:

```javascript
const shouldShowError = submitted || touched.email;
```

```jsx
{
  shouldShowError && errors.email && (
    <p id="email-error" role="alert">
      {errors.email}
    </p>
  );
}
```

권장:

- 필수값 오류는 blur 이후 표시
- 형식 오류는 입력 중 또는 blur 이후 표시 가능
- submit 시 모든 invalid field 표시
- UX 정책을 Form 전체에서 일관되게 유지

---

### [FAQ]

Q. 에러 메시지는 언제 보여주는 게 좋아?
A. 보통 touched 이후 또는 submit 이후 보여주는 방식이 좋다.

Q. 입력 시작 전부터 에러를 보여줘도 돼?
A. 권장하지 않는다. 사용자가 부담을 느낄 수 있다.

Q. touched와 submitted를 같이 써도 돼?
A. 가능하다. touched field는 즉시 표시하고 submit 후에는 모든 에러를 표시할 수 있다.

Q. onChange마다 에러를 보여줘도 돼?
A. 가능하지만 UX가 과도하게 공격적으로 느껴질 수 있어 기준이 필요하다.

---

# 5. Dirty State Rules

## 5.1 Dirty State Definition

### [개념]

Dirty State는 Form Field 또는 Form 전체가 초기값에서 변경되었는지 나타내는 상태다.

수정 Form에서 저장 버튼 활성화, 변경사항 경고, reset 가능 여부 판단에 사용한다.

---

### [핵심]

Dirty State 핵심 요소:

- dirty
- isDirty
- initialValues comparison
- changed field
- save button enabled
- unsaved changes
- reset available
- edit form
- form modification

---

### [실무]

Field Dirty 예:

```javascript
const isTitleDirty = values.title !== initialValues.title;
```

Form Dirty 예:

```javascript
const isDirty = JSON.stringify(values) !== JSON.stringify(initialValues);
```

저장 버튼 예:

```jsx
<button type="submit" disabled={!isDirty || submitting}>
  저장
</button>
```

권장:

- 수정 Form에서 dirty 기준 활용
- 변경사항이 없으면 저장 버튼 disabled 가능
- 페이지 이탈 전 변경사항 경고 가능
- 복잡한 객체 비교는 전용 비교 함수 고려
- Form Library의 dirty state 활용 가능

---

### [FAQ]

Q. dirty가 뭐야?
A. 초기값과 현재 입력값이 달라졌는지를 나타내는 상태다.

Q. dirty는 언제 사용해?
A. 수정 Form에서 저장 버튼 활성화, 변경사항 경고, reset 가능 여부 판단에 사용한다.

Q. isDirty는 어떻게 계산해?
A. 현재 values와 initialValues를 비교해서 계산한다.

Q. JSON.stringify로 dirty 비교해도 돼?
A. 단순 객체는 가능하지만 복잡한 값, 순서, Date, File이 있으면 별도 비교 기준이 필요하다.

---

## 5.2 Dirty State Use Cases

### [개념]

Dirty State는 사용자가 실제로 값을 변경했는지 판단하는 Form UX 기준이다.

특히 Edit Form, Profile Form, Settings Form에서 중요하다.

---

### [핵심]

사용 사례:

- edit form
- profile update
- settings form
- save button disabled
- reset button enabled
- unsaved changes warning
- submit optimization
- prevent unnecessary API request

---

### [실무]

저장 버튼 조건:

```javascript
const canSubmit = isDirty && Object.keys(errors).length === 0 && !submitting;
```

```jsx
<button type="submit" disabled={!canSubmit}>
  변경사항 저장
</button>
```

변경사항 경고 Flow:

```text
User Modify Form
→ isDirty true
→ Try Navigate Away
→ Show Unsaved Changes Warning
→ Confirm or Stay
```

주의:

- 생성 Form에서는 dirty가 필수는 아님
- 수정 Form에서는 dirty가 유용
- File input dirty 기준은 별도 처리
- 자동 저장 Form은 dirty와 debounce를 함께 고려

---

### [FAQ]

Q. 생성 Form에도 dirty가 필요해?
A. 필수는 아니다. 주로 수정 Form에서 유용하다.

Q. dirty가 false면 API 요청을 막아도 돼?
A. 수정 Form에서는 변경사항이 없으면 요청을 막을 수 있다.

Q. 파일 input도 dirty 비교가 쉬워?
A. 아니다. File 객체는 별도 선택 여부나 파일 id 기준으로 관리하는 것이 좋다.

Q. dirty와 touched는 같은 개념이야?
A. 아니다. touched는 방문 여부이고 dirty는 값 변경 여부다.

---

# 6. Submit State Rules

## 6.1 Submitting State

### [개념]

Submitting State는 Form 제출 요청이 진행 중인지 나타내는 상태다.

API 요청 중 버튼 비활성화, 로딩 표시, 중복 제출 방지에 사용한다.

---

### [핵심]

Submitting State 핵심 요소:

- submitting
- isSubmitting
- pending
- loading
- disabled
- duplicate submit prevention
- try catch finally
- API request state
- submit button state

---

### [실무]

기본 예:

```javascript
const [submitting, setSubmitting] = useState(false);
```

submit 처리:

```jsx
async function handleSubmit(event) {
  event.preventDefault();

  setSubmitting(true);

  try {
    await createReview(requestBody);
  } catch (error) {
    setSubmitError("저장에 실패했습니다.");
  } finally {
    setSubmitting(false);
  }
}
```

버튼 처리:

```jsx
<button type="submit" disabled={submitting}>
  {submitting ? "저장 중..." : "저장"}
</button>
```

권장:

- API 요청 직전에 submitting true
- finally에서 submitting false
- submit button disabled 처리
- 버튼 문구 또는 spinner 표시
- 실패 시 다시 제출 가능하게 복구

---

### [FAQ]

Q. submitting State가 뭐야?
A. Form 제출 요청이 진행 중인지 나타내는 상태다.

Q. submitting은 왜 필요해?
A. 중복 제출을 줄이고 사용자에게 처리 중임을 알려주기 위해 필요하다.

Q. submitting은 언제 false로 돌려?
A. 성공과 실패 모두에서 finally를 사용해 false로 복구하는 것이 안전하다.

Q. 제출 중 버튼을 disabled 해야 해?
A. 권장한다. 중복 클릭과 중복 요청을 줄일 수 있다.

---

## 6.2 Duplicate Submit Prevention

### [개념]

Duplicate Submit Prevention은 같은 Form 요청이 여러 번 전송되는 것을 방지하는 기준이다.

Frontend에서는 submitting과 disabled로 중복 클릭을 줄이고, 중요한 요청은 Backend에서도 중복 방지해야 한다.

---

### [핵심]

중복 제출 방지 요소:

- submitting state
- disabled submit button
- loading indicator
- early return
- debounce
- idempotency
- backend duplicate check
- payment caution
- order caution

---

### [실무]

중복 제출 방지 예:

```javascript
async function handleSubmit(event) {
  event.preventDefault();

  if (submitting) {
    return;
  }

  setSubmitting(true);

  try {
    await submitForm();
  } finally {
    setSubmitting(false);
  }
}
```

버튼 예:

```jsx
<button type="submit" disabled={submitting}>
  {submitting ? "처리 중..." : "제출"}
</button>
```

주의:

- Frontend disabled만으로 완전한 중복 방지는 불가
- 결제, 주문, 후원, 예약은 Backend idempotency 고려
- 실패 후에는 다시 제출 가능해야 함
- 네트워크 지연 상황에서 중복 요청 주의

---

### [FAQ]

Q. 버튼 disabled만 하면 중복 제출이 완전히 막혀?
A. 아니다. UX상 중복 클릭을 줄일 수 있지만 중요한 요청은 Backend에서도 중복 방지해야 한다.

Q. submitting 상태에서 submit이 다시 들어오면 어떻게 해?
A. early return으로 요청을 중단하는 것이 좋다.

Q. 결제 Form도 Frontend 중복 방지만 하면 돼?
A. 아니다. 결제나 주문은 Backend idempotency 또는 중복 검증이 필요하다.

Q. 실패 후에는 버튼을 다시 활성화해야 해?
A. 그렇다. 사용자가 수정 후 다시 제출할 수 있어야 한다.

---

# 7. Submitted State Rules

## 7.1 Submitted State

### [개념]

Submitted State는 사용자가 Form 제출을 시도했는지 나타내는 상태다.

submit 이후 전체 validation error를 표시할 때 사용할 수 있다.

---

### [핵심]

Submitted State 사용 대상:

- submitted
- submit attempted
- show all errors
- validation display
- first submit
- failed submit
- UX feedback

---

### [실무]

Submitted State 예:

```javascript
const [submitted, setSubmitted] = useState(false);
```

submit 처리:

```javascript
function handleSubmit(event) {
  event.preventDefault();

  setSubmitted(true);

  const nextErrors = validateForm(values);
  setErrors(nextErrors);

  if (Object.keys(nextErrors).length > 0) {
    return;
  }

  submitForm();
}
```

에러 표시:

```jsx
{
  (submitted || touched.email) && errors.email && (
    <p role="alert">{errors.email}</p>
  );
}
```

권장:

- 첫 submit 이후 모든 에러 표시
- touched와 함께 사용 가능
- reset 시 submitted false로 초기화
- submit 성공 후 필요 시 초기화

---

### [FAQ]

Q. submitted State가 뭐야?
A. 사용자가 Form 제출을 시도했는지 나타내는 상태다.

Q. submitted는 왜 필요해?
A. submit 이후 전체 validation error를 보여주기 위해 사용할 수 있다.

Q. touched와 submitted를 같이 써도 돼?
A. 가능하다. touched field는 먼저 보여주고 submit 후에는 전체 에러를 보여줄 수 있다.

Q. reset하면 submitted도 초기화해야 해?
A. 보통 true에서 false로 초기화하는 것이 좋다.

---

# 8. Form State Location

## 8.1 Local Form State

### [개념]

Local Form State는 Form Component 내부에서만 사용하는 입력 상태다.

대부분의 Form 입력값은 Local State로 관리하는 것이 적합하다.

---

### [핵심]

Local State 적합 조건:

- single form
- temporary input
- no cross-page sharing
- no global usage
- local validation
- submit only value
- isolated component

---

### [실무]

Local State 예:

```jsx
function SearchForm({ onSearch }) {
  const [keyword, setKeyword] = useState("");

  function handleSubmit(event) {
    event.preventDefault();
    onSearch(keyword.trim());
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={keyword}
        onChange={(event) => setKeyword(event.target.value)}
      />
    </form>
  );
}
```

권장:

- 임시 입력값은 Local State 우선
- Form 내부에서만 쓰는 값은 전역 상태로 올리지 않음
- 부모에는 제출 결과만 전달 가능
- Form이 사라지면 함께 사라져도 되는 값에 적합

---

### [FAQ]

Q. Form State는 어디에 둬야 해?
A. 단일 Form 내부에서만 필요하면 Local State에 두는 것이 일반적이다.

Q. 모든 Form State를 전역 Store에 넣어도 돼?
A. 권장하지 않는다. 대부분의 입력 중 상태는 Local State로 충분하다.

Q. 부모 Component가 Form 값을 알아야 하면?
A. 제출 시 callback으로 전달하거나 필요한 경우 state를 부모로 올린다.

Q. Local State는 언제 부적합해?
A. 여러 Step, 여러 Component, URL 공유, 페이지 간 유지가 필요한 경우에는 부적합할 수 있다.

---

## 8.2 Lifted Form State

### [개념]

Lifted Form State는 Form 입력값을 부모 Component로 올려 여러 하위 Component가 공유하게 하는 방식이다.

여러 Step Form, 분리된 Field Component, Preview UI가 같은 값을 사용해야 할 때 사용할 수 있다.

---

### [핵심]

Lift State 사용 대상:

- multi step form
- shared preview
- parent submit
- sibling component sharing
- common parent ownership
- controlled child field
- props drilling caution

---

### [실무]

기본 구조:

```text
ParentFormContainer
├ FormFields
├ PreviewPanel
└ SubmitButton
```

예:

```jsx
function ProfileEditContainer() {
  const [values, setValues] = useState({
    nickname: "",
    bio: "",
  });

  return (
    <>
      <ProfileForm values={values} setValues={setValues} />
      <ProfilePreview values={values} />
    </>
  );
}
```

주의:

- 불필요하게 너무 상위로 올리지 않음
- props drilling이 심하면 Form Context 또는 Form Library 검토
- 공유가 필요한 최소 범위까지만 올림
- 서버 데이터와 사용자 입력값 구분

---

### [FAQ]

Q. Form State를 부모로 올리는 기준은 뭐야?
A. 여러 하위 Component가 같은 Form 값을 사용하거나 부모가 제출을 관리해야 할 때 올린다.

Q. 무조건 부모에 두면 좋아?
A. 아니다. 필요 이상으로 올리면 Component 결합도가 높아질 수 있다.

Q. Preview가 Form 값을 실시간으로 보여줘야 하면?
A. 공통 부모에 Form State를 두고 Form과 Preview에 전달할 수 있다.

Q. props 전달이 너무 많으면 어떻게 해?
A. Form Context, custom hook, Form Library를 검토할 수 있다.

---

## 8.3 URL State for Search Form

### [개념]

URL State는 검색 조건, 필터, 페이지 번호처럼 공유 가능한 상태를 URL Query String에 저장하는 방식이다.

Search Form에서는 입력 중 값과 제출된 검색 조건을 분리할 수 있다.

---

### [핵심]

URL State 사용 대상:

- search keyword
- filters
- page
- size
- sort
- category
- region
- shareable state
- browser back forward
- query params

---

### [실무]

Search Form Flow:

```text
User Typing
→ Local Form State
→ Submit
→ Trim Keyword
→ Update URL Search Params
→ Reset Page
→ Fetch List
```

예:

```javascript
const params = new URLSearchParams();

if (keyword.trim()) {
  params.set("keyword", keyword.trim());
}

params.set("page", "1");
```

권장:

- 입력 중 임시값은 Local State
- 제출된 검색 조건은 URL Search Params
- 검색 조건 변경 시 page reset
- 빈 값은 query param에서 제외 가능
- URL 기준으로 목록 fetch 가능

---

### [FAQ]

Q. 검색 Form State는 어디에 둬?
A. 입력 중 값은 Local State, 제출된 검색 조건은 URL Query String으로 관리할 수 있다.

Q. 검색 조건을 URL에 넣는 이유는?
A. 공유, 새로고침 유지, 뒤로가기/앞으로가기 대응에 유리하다.

Q. 검색 조건이 바뀌면 page를 reset해야 해?
A. 대부분 그렇다. 기존 page가 새 검색 결과 범위를 벗어날 수 있다.

Q. 빈 검색어도 query param에 넣어야 해?
A. 보통 빈 값은 제외하는 것이 깔끔하다.

---

## 8.4 Server State vs Form State

### [개념]

Server State는 서버에서 받아온 원본 데이터이고 Form State는 사용자가 수정 중인 임시 입력값이다.

수정 Form에서는 두 상태를 반드시 구분해야 한다.

---

### [핵심]

비교 기준:

| 비교       | Server State              | Form State              |
| ---------- | ------------------------- | ----------------------- |
| 출처       | Backend API               | User Input              |
| 목적       | 원본 데이터 표시          | 수정 중 값 관리         |
| 변경 주체  | 서버 응답                 | 사용자 입력             |
| 예         | post.title                | values.title            |
| 관리 도구  | React Query / fetch state | useState / Form Library |
| reset 기준 | 서버 최신값               | initialValues           |

---

### [실무]

수정 Form Flow:

```text
Fetch Detail Data
→ Build Initial Values
→ Initialize Form State
→ User Modify Values
→ Submit Request
→ Server Update
→ Refresh Server State
→ Reset Form State with Latest Data
```

주의:

- 서버 응답 객체를 직접 수정하지 않음
- Form State는 복사본으로 생성
- submit 성공 후 서버 최신값으로 동기화
- reset은 initialValues 기준
- 서버 로딩 중 value undefined 방지

---

### [FAQ]

Q. 수정 Form의 초기값은 Server State야 Form State야?
A. 서버에서 받은 원본은 Server State이고, 사용자가 수정 중인 값은 Form State다.

Q. 서버 데이터를 그대로 input value에 넣어도 돼?
A. 단순 표시가 아니라 수정 Form이라면 Form State로 복사해서 관리하는 것이 좋다.

Q. submit 성공 후 Form State는 어떻게 해?
A. 서버 최신값을 다시 반영하거나 initialValues를 최신 상태로 갱신한다.

Q. Server State와 Form State를 구분하지 않으면 뭐가 문제야?
A. 원본 데이터와 수정 중 데이터가 섞여 reset, dirty check, submit mapping이 어려워진다.

---

# 9. Form State Update Rules

## 9.1 Immutable Update

### [개념]

Immutable Update는 기존 Form State를 직접 수정하지 않고 새 객체나 배열을 만들어 업데이트하는 방식이다.

React State는 불변 업데이트를 기준으로 변경을 감지한다.

---

### [핵심]

Immutable Update 핵심:

- spread operator
- prev state
- object update
- array update
- no direct mutation
- nested update caution
- state change detection

---

### [실무]

객체 업데이트:

```javascript
setValues((prevValues) => ({
  ...prevValues,
  email: nextEmail,
}));
```

배열 업데이트:

```javascript
setSelectedThemes((prevThemes) => [...prevThemes, themeCode]);
```

배열 제거:

```javascript
setSelectedThemes((prevThemes) =>
  prevThemes.filter((code) => code !== themeCode),
);
```

나쁜 예:

```javascript
values.email = "test@example.com";
setValues(values);
```

권장:

- 이전 state를 직접 수정하지 않음
- setState callback 형태 사용
- 배열은 push 대신 새 배열 생성
- nested object는 깊은 복사 기준 필요
- 복잡한 state는 reducer 검토 가능

---

### [FAQ]

Q. Form State를 직접 수정하면 안 돼?
A. 권장하지 않는다. React가 변경을 감지하지 못하거나 예측 어려운 문제가 생길 수 있다.

Q. 객체 Form State는 어떻게 업데이트해?
A. spread operator와 prev state를 사용해 새 객체를 만든다.

Q. 배열 Form State는 push를 써도 돼?
A. 직접 push보다 새 배열을 만들어 업데이트하는 것이 좋다.

Q. nested Form State는 어떻게 관리해?
A. 깊은 업데이트가 필요하므로 구조를 단순화하거나 helper, reducer, Form Library를 검토한다.

---

## 9.2 Common Change Handler State Update

### [개념]

Common Change Handler는 여러 input의 변경을 하나의 handler로 처리하는 패턴이다.

`name` 속성과 values key를 맞춰 동작한다.

---

### [핵심]

공통 handler 핵심:

- name
- value
- checked
- type
- event.target
- computed property name
- values key matching
- checkbox handling
- number conversion caution

---

### [실무]

기본 공통 handler:

```javascript
function handleChange(event) {
  const { name, value } = event.target;

  setValues((prevValues) => ({
    ...prevValues,
    [name]: value,
  }));
}
```

checkbox 포함:

```javascript
function handleChange(event) {
  const { name, type, value, checked } = event.target;

  setValues((prevValues) => ({
    ...prevValues,
    [name]: type === "checkbox" ? checked : value,
  }));
}
```

주의:

- input name과 values key 일치
- checkbox는 checked 사용
- number input도 value는 문자열일 수 있음
- select도 value 기준
- nested field는 별도 처리 필요

---

### [FAQ]

Q. 여러 input을 하나의 handleChange로 처리할 수 있어?
A. 가능하다. input name과 values 객체 key를 맞추면 된다.

Q. checkbox도 같은 handleChange로 처리할 수 있어?
A. 가능하지만 type이 checkbox일 때 checked를 사용해야 한다.

Q. name과 values key가 다르면 어떻게 돼?
A. 잘못된 key가 업데이트되어 input 값이 바뀌지 않거나 Request Body가 틀어질 수 있다.

Q. number input은 handleChange에서 바로 Number로 바꿔야 해?
A. 상황에 따라 다르다. 입력 중에는 문자열로 두고 submit 시 변환하는 방식도 많이 사용한다.

---

# 10. Form Reset State Rules

## 10.1 Reset State Definition

### [개념]

Form Reset은 Form State를 초기값 또는 서버 최신값으로 되돌리는 작업이다.

생성 Form, 수정 Form, 검색 Form, 파일 Form마다 reset 기준이 다르다.

---

### [핵심]

Reset 대상:

- values
- errors
- touched
- dirty
- submitted
- submitError
- submitting
- file input
- preview url
- URL Search Params
- initialValues

---

### [실무]

생성 Form reset:

```javascript
function resetForm() {
  setValues(initialValues);
  setErrors({});
  setTouched({});
  setSubmitError("");
  setSubmitted(false);
}
```

수정 Form reset:

```javascript
function resetEditForm() {
  setValues(latestServerValues);
  setErrors({});
  setTouched({});
  setSubmitError("");
}
```

주의:

- 생성 성공 후 reset 가능
- 수정 성공 후 서버 최신값으로 reset
- 검색 reset은 URL Search Params도 초기화 가능
- file input은 ref를 통한 별도 reset 필요 가능
- preview URL은 revokeObjectURL 필요 가능

---

### [FAQ]

Q. Form Reset은 무엇을 초기화해야 해?
A. values, errors, touched, submitted, submitError 등을 초기화한다.

Q. 제출 성공 후 항상 reset해야 해?
A. 아니다. 생성 Form은 reset할 수 있고 수정 Form은 서버 최신값으로 갱신하는 것이 좋다.

Q. 검색 Form reset은 URL도 초기화해야 해?
A. 검색 조건을 URL State로 관리한다면 URL Search Params도 함께 초기화해야 한다.

Q. file input reset은 일반 values reset으로 충분해?
A. 아닐 수 있다. file input은 ref 또는 key 변경으로 별도 초기화가 필요할 수 있다.

---

# 11. Form State Comparison

## 11.1 Values vs Errors

### [개념]

Values는 사용자가 입력한 값이고 Errors는 입력값 검증 실패 결과다.

두 상태를 분리해야 Form 처리 흐름이 명확해진다.

---

### [핵심]

비교:

| 비교      | Values        | Errors                  |
| --------- | ------------- | ----------------------- |
| 의미      | 입력값        | 검증 실패 메시지        |
| 예        | values.email  | errors.email            |
| 업데이트  | onChange      | validate / server error |
| 사용 위치 | input value   | error message           |
| 초기값    | 빈 값         | 빈 객체                 |
| reset     | initialValues | `{}`                    |

---

### [실무]

좋은 구조:

```javascript
const [values, setValues] = useState(initialValues);
const [errors, setErrors] = useState({});
```

나쁜 구조:

```javascript
const [formState, setFormState] = useState({
  email: "",
  emailError: "",
});
```

권장:

- 입력값과 에러 메시지 분리
- validation 함수는 errors 객체 반환
- 서버 에러도 errors 구조에 mapping 가능
- Field Component에는 value와 error를 각각 전달

---

### [FAQ]

Q. values와 errors를 왜 분리해?
A. 입력값 변경과 에러 표시의 책임이 다르기 때문이다.

Q. emailError를 values 안에 넣어도 돼?
A. 가능은 하지만 입력값과 에러가 섞여 관리가 복잡해질 수 있다.

Q. errors 초기값은 뭐가 좋아?
A. 빈 객체 `{}`가 일반적이다.

Q. errors는 언제 초기화해?
A. submit 전, reset 시, 특정 field 재입력 시 초기화할 수 있다.

---

## 11.2 Touched vs Dirty

### [개념]

Touched는 사용자가 field를 방문했는지 여부이고 Dirty는 값이 초기값에서 변경되었는지 여부다.

두 상태는 비슷해 보이지만 목적이 다르다.

---

### [핵심]

비교:

| 비교         | Touched                  | Dirty                    |
| ------------ | ------------------------ | ------------------------ |
| 의미         | 방문 여부                | 변경 여부                |
| 기준         | blur / focus interaction | initialValues와 비교     |
| 사용 목적    | 에러 표시 타이밍         | 저장 버튼, 변경사항 경고 |
| 예           | touched.email            | isDirty                  |
| 값 변경 필요 | 필요 없음                | 필요함                   |

---

### [실무]

예:

```text
사용자가 email field 클릭 후 바로 나감
→ touched.email true
→ dirty false

사용자가 email 값을 수정함
→ touched.email true
→ dirty true
```

권장:

- Validation Error 표시에는 touched 활용
- 수정 Form 저장 가능 여부에는 dirty 활용
- 두 상태를 같은 개념으로 사용하지 않음
- React Hook Form 사용 시 formState.touchedFields / dirtyFields 활용 가능

---

### [FAQ]

Q. touched와 dirty는 같은 거야?
A. 아니다. touched는 방문 여부이고 dirty는 값 변경 여부다.

Q. touched는 true인데 dirty는 false일 수 있어?
A. 가능하다. field를 방문했지만 값을 바꾸지 않은 경우다.

Q. dirty는 true인데 touched는 false일 수 있어?
A. 일반 UI에서는 드물지만 프로그램으로 값이 변경되면 가능하다.

Q. 에러 표시에는 touched와 dirty 중 뭐가 좋아?
A. 보통 touched 또는 submitted 기준이 적합하다.

---

## 11.3 Form State vs Global State

### [개념]

Form State는 입력 중인 임시 상태이고 Global State는 앱 전역에서 공유되는 상태다.

대부분의 Form State는 Global State로 올리지 않는 것이 좋다.

---

### [핵심]

비교:

| 비교      | Form State              | Global State              |
| --------- | ----------------------- | ------------------------- |
| 범위      | Form 내부               | 앱 전역                   |
| 생명주기  | 임시                    | 장기 유지 가능            |
| 예        | 로그인 입력값           | 로그인 사용자 정보        |
| 저장 위치 | useState / Form Library | Zustand / Redux / Context |
| 권장 여부 | Form 기본값             | 필요한 경우만             |

---

### [실무]

권장 분리:

```text
Login Form email/password 입력값
→ Local Form State

Login 성공 후 user 정보
→ Global Auth State

검색 input 입력 중 keyword
→ Local Form State

제출된 검색 조건
→ URL State
```

주의:

- password 같은 민감 입력값을 전역 상태에 저장하지 않음
- Form 입력 중 상태를 앱 전체가 알 필요 없음
- 전역 상태는 결과 데이터나 인증 상태에 사용
- Multi Step Form은 예외적으로 상위 상태나 Context 검토 가능

---

### [FAQ]

Q. Form State를 전역 Store에 넣어도 돼?
A. 대부분 권장하지 않는다. 입력 중 임시값은 Local State가 적합하다.

Q. 로그인 Form의 email/password를 Global State에 저장해도 돼?
A. 권장하지 않는다. 특히 password는 전역 상태나 로그에 남기면 안 된다.

Q. Form 제출 결과는 Global State에 넣어도 돼?
A. 로그인 사용자 정보처럼 앱 전체에서 필요한 결과는 Global State에 넣을 수 있다.

Q. Multi Step Form은 Global State가 필요해?
A. 반드시 필요하지는 않다. 공통 부모, Context, Form Library로 관리할 수 있다.

---

# 12. Common Mistakes

## 12.1 Form State Common Mistakes

### [개념]

Form State에서 자주 발생하는 실수는 입력값과 에러 혼합, 초기값 undefined, 직접 mutation, 전역 상태 남용, 서버 상태와 Form 상태 혼동이다.

---

### [핵심]

자주 발생하는 실수:

- input 초기값 undefined
- values와 errors 혼합
- checkbox 초기값 문자열 사용
- number input 즉시 변환으로 빈 값 처리 오류
- name과 values key 불일치
- State 직접 mutation
- errors 초기화 누락
- submitError 초기화 누락
- touched와 dirty 혼동
- Server State 직접 수정
- Form State 전역 저장
- reset 시 errors/touched 미초기화
- submitting false 복구 누락
- file input을 일반 values처럼 처리

---

### [실무]

문제 해결 Flow:

```text
Form State 문제 발생
→ initialValues 확인
→ values / errors 분리 확인
→ name key 일치 확인
→ onChange update 확인
→ direct mutation 확인
→ submit/reset 초기화 확인
→ Server State 혼동 확인
```

나쁜 예:

```javascript
values.email = nextEmail;
setValues(values);
```

좋은 예:

```javascript
setValues((prevValues) => ({
  ...prevValues,
  email: nextEmail,
}));
```

---

### [FAQ]

Q. Form State에서 가장 흔한 실수는 뭐야?
A. 초기값 undefined, values/errors 혼합, name key 불일치, State 직접 mutation이 많다.

Q. input 값이 안 바뀌면 Form State에서 무엇을 확인해?
A. value, onChange, setState, name과 values key, initialValues를 확인한다.

Q. reset했는데 에러가 남아 있으면 왜 그래?
A. values만 reset하고 errors, touched, submitError를 초기화하지 않았을 가능성이 있다.

Q. 수정 Form에서 원본 데이터가 바뀌어버리면 왜 문제야?
A. Server State와 Form State를 구분하지 않고 직접 수정했을 가능성이 있다.

---

# 13. Form State Checklist

## 13.1 Implementation Checklist

### [개념]

Form State Checklist는 Form 입력값, 에러, 제출 상태, 초기화 기준이 안정적으로 설계되었는지 확인하는 검수 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] Form Values 초기값이 명확한가?
- [ ] 문자열 input 초기값이 빈 문자열인가?
- [ ] checkbox 초기값이 false인가?
- [ ] 다중 선택 초기값이 배열인가?
- [ ] values와 errors가 분리되어 있는가?
- [ ] Field Error와 Global Error가 구분되어 있는가?
- [ ] errors key와 input name이 일치하는가?
- [ ] touched 표시 기준이 정의되어 있는가?
- [ ] dirty 기준이 필요한 Form에 정의되어 있는가?
- [ ] submitting 상태가 있는가?
- [ ] submit 중 버튼 disabled 기준이 있는가?
- [ ] submitted 상태가 필요한 경우 정의되어 있는가?
- [ ] Form State 위치가 적절한가?
- [ ] Local State와 Global State를 구분했는가?
- [ ] Search Form은 URL State 적용 여부를 검토했는가?
- [ ] Server State와 Form State를 구분했는가?
- [ ] State 직접 mutation이 없는가?
- [ ] reset 시 values/errors/touched/submitError가 함께 정리되는가?
- [ ] file input 상태를 별도 기준으로 처리하는가?
```

---

### [실무]

검수 Flow:

```text
Initial Values Check
→ Values State Check
→ Error State Check
→ Touched / Dirty Check
→ Submit State Check
→ State Location Check
→ Server State Separation Check
→ Reset Check
→ Common Mistake Review
```

---

### [FAQ]

Q. Form State 검수에서 가장 중요한 것은?
A. 초기값, values/errors 분리, submitting, state 위치, Server State와 Form State 구분이다.

Q. Form State 다음에는 무엇을 검토해?
A. Input Handling, Validation, Server Error Handling, Submit Flow, Request Body Mapping을 검토한다.

---

# Retrieval Queries

### [FAQ]

Q. Form State가 뭐야?
A. 사용자가 입력한 값과 에러, 제출 상태, 초기값 등을 React에서 관리하는 상태다.

Q. Form State는 입력값만 의미해?
A. 아니다. values, errors, touched, dirty, submitting, submitError 같은 상태를 포함할 수 있다.

Q. Form State에서 가장 중요한 것은 뭐야?
A. 입력값과 에러 상태를 분리하고 제출 상태를 명확히 관리하는 것이다.

Q. Values State가 뭐야?
A. Form Field의 현재 입력값을 저장하는 상태다.

Q. Form 입력값은 각각 useState로 둬야 해?
A. 입력값이 적으면 각각 useState도 가능하고 필드가 많으면 values 객체가 편하다.

Q. 필드가 많으면 Form State는 어떻게 관리해?
A. values 객체로 관리하면 공통 handleChange와 Request Body Mapping에 유리하다.

Q. input name과 values key는 같아야 해?
A. 공통 handleChange를 사용한다면 같게 맞추는 것이 좋다.

Q. initialValues가 왜 중요해?
A. Controlled Component 안정성과 Form Reset 기준을 결정하기 때문이다.

Q. 문자열 input 초기값은 무엇이 좋아?
A. 빈 문자열 `""`이 안전하다.

Q. checkbox 초기값은 무엇이 좋아?
A. false가 일반적이다.

Q. API 데이터가 아직 없을 때 Form 초기값은 어떻게 해?
A. undefined가 들어가지 않도록 빈 문자열, false, [] 같은 기본값을 사용한다.

Q. Error State가 뭐야?
A. Form 검증 실패 메시지와 서버 오류 메시지를 저장하는 상태다.

Q. Field Error와 Global Error 차이는?
A. Field Error는 특정 input에 연결되고 Global Error는 Form 전체 실패를 나타낸다.

Q. errors 객체 key는 무엇과 맞춰야 해?
A. input name 또는 Form Values key와 맞추는 것이 좋다.

Q. submitError는 언제 사용해?
A. 로그인 실패, 권한 없음, 서버 오류처럼 특정 field가 아닌 Form 전체 오류에 사용한다.

Q. Field Error는 어디에 보여줘?
A. 해당 input 근처에 보여주는 것이 좋다.

Q. 에러 메시지를 input과 연결해야 해?
A. 권장한다. aria-describedby를 사용하면 접근성이 좋아진다.

Q. Global Error는 언제 사용해?
A. 특정 field가 아니라 Form 전체 실패를 나타낼 때 사용한다.

Q. 로그인 실패는 Field Error야 Global Error야?
A. 계정 정보 불일치는 보통 Global Error로 처리한다.

Q. touched가 뭐야?
A. 사용자가 해당 field를 방문하거나 blur한 적이 있는지를 나타내는 상태다.

Q. touched는 왜 필요해?
A. 사용자가 입력하기 전부터 에러가 보이는 UX를 방지하기 위해 사용한다.

Q. touched는 언제 true로 바꿔?
A. 보통 input의 onBlur 이벤트에서 true로 바꾼다.

Q. 에러 메시지는 언제 보여주는 게 좋아?
A. 보통 touched 이후 또는 submit 이후 보여주는 방식이 좋다.

Q. touched와 submitted를 같이 써도 돼?
A. 가능하다. touched field는 먼저 보여주고 submit 후에는 전체 에러를 보여줄 수 있다.

Q. dirty가 뭐야?
A. 초기값과 현재 입력값이 달라졌는지를 나타내는 상태다.

Q. dirty는 언제 사용해?
A. 수정 Form에서 저장 버튼 활성화, 변경사항 경고, reset 가능 여부 판단에 사용한다.

Q. isDirty는 어떻게 계산해?
A. 현재 values와 initialValues를 비교해서 계산한다.

Q. touched와 dirty는 같은 개념이야?
A. 아니다. touched는 방문 여부이고 dirty는 값 변경 여부다.

Q. touched는 true인데 dirty는 false일 수 있어?
A. 가능하다. field를 방문했지만 값을 바꾸지 않은 경우다.

Q. 생성 Form에도 dirty가 필요해?
A. 필수는 아니다. 주로 수정 Form에서 유용하다.

Q. dirty가 false면 API 요청을 막아도 돼?
A. 수정 Form에서는 변경사항이 없으면 요청을 막을 수 있다.

Q. submitting State가 뭐야?
A. Form 제출 요청이 진행 중인지 나타내는 상태다.

Q. submitting은 왜 필요해?
A. 중복 제출을 줄이고 사용자에게 처리 중임을 알려주기 위해 필요하다.

Q. submitting은 언제 false로 돌려?
A. 성공과 실패 모두에서 finally를 사용해 false로 복구하는 것이 안전하다.

Q. 제출 중 버튼을 disabled 해야 해?
A. 권장한다. 중복 클릭과 중복 요청을 줄일 수 있다.

Q. 버튼 disabled만 하면 중복 제출이 완전히 막혀?
A. 아니다. UX상 중복 클릭을 줄일 수 있지만 중요한 요청은 Backend에서도 중복 방지해야 한다.

Q. submitted State가 뭐야?
A. 사용자가 Form 제출을 시도했는지 나타내는 상태다.

Q. submitted는 왜 필요해?
A. submit 이후 전체 validation error를 보여주기 위해 사용할 수 있다.

Q. reset하면 submitted도 초기화해야 해?
A. 보통 true에서 false로 초기화하는 것이 좋다.

Q. Form State는 어디에 둬야 해?
A. 단일 Form 내부에서만 필요하면 Local State에 두는 것이 일반적이다.

Q. 모든 Form State를 전역 Store에 넣어도 돼?
A. 권장하지 않는다. 대부분의 입력 중 상태는 Local State로 충분하다.

Q. 부모 Component가 Form 값을 알아야 하면?
A. 제출 시 callback으로 전달하거나 필요한 경우 state를 부모로 올린다.

Q. Form State를 부모로 올리는 기준은 뭐야?
A. 여러 하위 Component가 같은 Form 값을 사용하거나 부모가 제출을 관리해야 할 때 올린다.

Q. 검색 Form State는 어디에 둬?
A. 입력 중 값은 Local State, 제출된 검색 조건은 URL Query String으로 관리할 수 있다.

Q. 검색 조건을 URL에 넣는 이유는?
A. 공유, 새로고침 유지, 뒤로가기/앞으로가기 대응에 유리하다.

Q. 검색 조건이 바뀌면 page를 reset해야 해?
A. 대부분 그렇다. 기존 page가 새 검색 결과 범위를 벗어날 수 있다.

Q. 수정 Form의 초기값은 Server State야 Form State야?
A. 서버에서 받은 원본은 Server State이고, 사용자가 수정 중인 값은 Form State다.

Q. 서버 데이터를 그대로 input value에 넣어도 돼?
A. 단순 표시가 아니라 수정 Form이라면 Form State로 복사해서 관리하는 것이 좋다.

Q. Server State와 Form State를 구분하지 않으면 뭐가 문제야?
A. 원본 데이터와 수정 중 데이터가 섞여 reset, dirty check, submit mapping이 어려워진다.

Q. Form State를 직접 수정하면 안 돼?
A. 권장하지 않는다. React가 변경을 감지하지 못하거나 예측 어려운 문제가 생길 수 있다.

Q. 객체 Form State는 어떻게 업데이트해?
A. spread operator와 prev state를 사용해 새 객체를 만든다.

Q. 여러 input을 하나의 handleChange로 처리할 수 있어?
A. 가능하다. input name과 values 객체 key를 맞추면 된다.

Q. checkbox도 같은 handleChange로 처리할 수 있어?
A. 가능하지만 type이 checkbox일 때 checked를 사용해야 한다.

Q. number input은 handleChange에서 바로 Number로 바꿔야 해?
A. 상황에 따라 다르다. 입력 중에는 문자열로 두고 submit 시 변환하는 방식도 많이 사용한다.

Q. Form Reset은 무엇을 초기화해야 해?
A. values, errors, touched, submitted, submitError 등을 초기화한다.

Q. 제출 성공 후 항상 reset해야 해?
A. 아니다. 생성 Form은 reset할 수 있고 수정 Form은 서버 최신값으로 갱신하는 것이 좋다.

Q. 검색 Form reset은 URL도 초기화해야 해?
A. 검색 조건을 URL State로 관리한다면 URL Search Params도 함께 초기화해야 한다.

Q. values와 errors를 왜 분리해?
A. 입력값 변경과 에러 표시의 책임이 다르기 때문이다.

Q. Form State를 전역 Store에 넣어도 돼?
A. 대부분 권장하지 않는다. 입력 중 임시값은 Local State가 적합하다.

Q. 로그인 Form의 email/password를 Global State에 저장해도 돼?
A. 권장하지 않는다. 특히 password는 전역 상태나 로그에 남기면 안 된다.

Q. Form State에서 가장 흔한 실수는 뭐야?
A. 초기값 undefined, values/errors 혼합, name key 불일치, State 직접 mutation이 많다.

Q. reset했는데 에러가 남아 있으면 왜 그래?
A. values만 reset하고 errors, touched, submitError를 초기화하지 않았을 가능성이 있다.

Q. Form State 다음 문서는 뭐가 좋아?
A. Input Handling, Validation, Server Error Handling, Submit Flow, Request Body Mapping 순서가 좋다.
