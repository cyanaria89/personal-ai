# Form Handling & Validation Part06 - Submit Flow & Request Body Mapping

---

# 1. Submit Flow Foundation

## 1.1 Submit Flow Definition

### [개념]

Submit Flow는 사용자가 Form을 제출했을 때 실행되는 전체 처리 흐름이다.

Submit Flow는 `preventDefault`, 이전 에러 초기화, Client Validation, Request Body Mapping, API Request, Server Error Handling, Success Handling, Form Reset까지 포함한다.

---

### [핵심]

Submit Flow 핵심 요소:

- onSubmit
- preventDefault
- clear previous errors
- Client Validation
- stop if invalid
- submitting state
- Request Body Mapping
- API Request
- success handling
- server error handling
- finally
- duplicate submit prevention
- reset
- redirect
- error UI

---

### [실무]

2026 실무 기준 Submit Flow:

```text
Submit Event
→ preventDefault
→ If Submitting Return
→ Clear Previous Errors
→ Client Validation
→ If Invalid Stop
→ Set Submitting True
→ Build Request Body
→ API Request
→ Handle Success
→ Handle Server Error
→ Set Submitting False
```

기본 예:

```javascript
async function handleSubmit(event) {
  event.preventDefault();

  if (submitting) {
    return;
  }

  setErrors({});
  setSubmitError("");

  const nextErrors = validateForm(values);
  setErrors(nextErrors);

  if (Object.keys(nextErrors).length > 0) {
    return;
  }

  setSubmitting(true);

  try {
    const requestBody = toRequestBody(values);

    await submitForm(requestBody);

    handleSuccess();
  } catch (error) {
    const mappedError = mapApiError(error);

    setErrors(mappedError.fieldErrors);
    setSubmitError(mappedError.globalError);
  } finally {
    setSubmitting(false);
  }
}
```

---

### [FAQ]

Q. Submit Flow가 뭐야?
A. Form 제출 시 검증, 요청 생성, API 호출, 성공/실패 처리를 수행하는 전체 흐름이다.

Q. Submit Flow에서 가장 중요한 것은 뭐야?
A. preventDefault, Client Validation, Request Body Mapping, submitting 상태, Server Error Handling이다.

Q. Submit Flow에서 Client Validation은 언제 해?
A. API 요청 전에 수행하고 실패하면 요청을 중단한다.

Q. Submit 실패 후 입력값은 유지해?
A. 보통 유지한다. 사용자가 수정 후 다시 제출할 수 있어야 한다.

---

# 2. Form Submit Event Rules

## 2.1 onSubmit and preventDefault

### [개념]

`onSubmit`은 Form 제출 이벤트를 처리하는 React 이벤트 핸들러다.

React SPA에서는 브라우저 기본 Form 제출 동작을 막기 위해 `event.preventDefault()`를 호출한다.

---

### [핵심]

onSubmit 핵심 요소:

- form onSubmit
- submit event
- event.preventDefault
- Enter key submit
- submit button
- accessibility
- no page refresh
- SPA request flow

---

### [실무]

기본 onSubmit 예:

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
      <button type="submit">검색</button>
    </form>
  );
}
```

권장:

- Form 제출은 `form onSubmit`에서 처리
- submit button은 `type="submit"`
- 일반 button은 `type="button"`
- `event.preventDefault()` 필수
- Enter key 제출 고려
- onClick submit만 사용하는 방식 지양

---

### [FAQ]

Q. onSubmit은 왜 사용해?
A. 버튼 클릭과 Enter key 제출을 일관되게 처리할 수 있기 때문이다.

Q. preventDefault는 왜 필요해?
A. 브라우저 기본 Form 제출과 페이지 새로고침을 막기 위해 필요하다.

Q. onClick으로 submit 처리하면 안 돼?
A. 가능하지만 Enter key 제출과 접근성 측면에서 form onSubmit이 더 적합하다.

Q. preventDefault를 빼면 어떻게 돼?
A. Form 제출 시 페이지가 새로고침될 수 있다.

---

## 2.2 Submit Button Rules

### [개념]

Submit Button은 Form 제출을 발생시키는 버튼이다.

Form 내부 버튼은 기본 submit 동작을 가질 수 있으므로 `type`을 명확히 지정해야 한다.

---

### [핵심]

Submit Button 기준:

- type submit
- type button
- disabled
- loading text
- submitting state
- duplicate submit prevention
- button label
- accessibility

---

### [실무]

Submit Button 예:

```jsx
<button type="submit" disabled={submitting}>
  {submitting ? "저장 중..." : "저장"}
</button>
```

일반 버튼 예:

```jsx
<button type="button" onClick={handleCancel}>
  취소
</button>
```

권장:

- 제출 버튼은 `type="submit"`
- 취소, 닫기, 초기화 버튼은 `type="button"`
- 제출 중 버튼 disabled
- 제출 중 문구 변경
- disabled만 믿지 말고 handler에서도 submitting early return 적용
- button label은 동작을 명확히 표현

---

### [FAQ]

Q. Submit Button type은 뭐야?
A. Form 제출 버튼은 `type="submit"`을 사용한다.

Q. 취소 버튼도 submit이 될 수 있어?
A. type을 명시하지 않으면 의도치 않게 submit될 수 있으므로 `type="button"`을 사용한다.

Q. 제출 중 버튼을 disabled 해야 해?
A. 권장한다. 중복 클릭과 중복 요청을 줄일 수 있다.

Q. disabled만으로 중복 제출이 완전히 막혀?
A. 아니다. handler에서도 submitting 상태를 확인하는 것이 좋다.

---

# 3. Submit Validation Flow Rules

## 3.1 Clear Previous Errors Before Validation

### [개념]

Clear Previous Errors는 새 제출을 시작하기 전에 이전 제출에서 발생한 Field Error와 Global Error를 초기화하는 처리다.

이전 오류가 현재 제출 결과와 섞이는 문제를 방지한다.

---

### [핵심]

초기화 대상:

- errors
- submitError
- globalError
- serverErrors
- stale error
- previous validation result
- previous response message

---

### [실무]

Submit 시작 시 초기화:

```javascript
function handleSubmit(event) {
  event.preventDefault();

  setErrors({});
  setSubmitError("");

  const nextErrors = validateForm(values);

  if (Object.keys(nextErrors).length > 0) {
    setErrors(nextErrors);
    return;
  }

  submitValidForm();
}
```

권장:

- validation 전 errors 초기화
- submitError 초기화
- 새 validation 결과만 표시
- field 수정 시 해당 field error 제거 가능
- 서버 오류도 다음 제출 전 정리

---

### [FAQ]

Q. Submit 전에 에러를 초기화해야 해?
A. 권장한다. 이전 제출의 에러가 현재 제출 결과와 섞일 수 있다.

Q. submitError도 초기화해야 해?
A. 권장한다. 이전 Global Error가 계속 남으면 혼란스럽다.

Q. errors를 지운 뒤 validation을 다시 해도 돼?
A. 가능하다. submit 시점에는 전체 validation 결과를 새로 계산하는 것이 좋다.

Q. Field 수정 시에도 에러를 지워야 해?
A. 해당 field의 이전 에러는 지우는 것이 좋다.

---

## 3.2 Stop Submit If Invalid

### [개념]

Stop Submit If Invalid는 Client Validation 실패 시 API Request를 보내지 않고 Submit Flow를 중단하는 기준이다.

잘못된 요청을 줄이고 사용자에게 즉시 수정 피드백을 제공한다.

---

### [핵심]

중단 기준:

- validation errors exist
- Object.keys(errors).length
- no API request
- setErrors
- show error message
- keep values
- focus invalid field

---

### [실무]

검증 실패 시 중단:

```javascript
const nextErrors = validateForm(values);

setErrors(nextErrors);

if (Object.keys(nextErrors).length > 0) {
  return;
}
```

첫 오류 focus:

```javascript
const firstErrorField = Object.keys(nextErrors)[0];

if (firstErrorField === "email") {
  emailRef.current?.focus();
}
```

권장:

- Client Validation 실패 시 API 요청 금지
- errors state에 메시지 저장
- 입력값 유지
- submit 이후 모든 field error 표시 가능
- 긴 Form은 첫 오류 field focus 고려

---

### [FAQ]

Q. Validation 실패 시 API 요청을 보내도 돼?
A. 보통 보내지 않는다. Client Validation 실패 시 요청을 중단한다.

Q. 검증 실패 후 입력값은 지워?
A. 아니다. 사용자가 수정할 수 있도록 유지한다.

Q. 검증 실패 후 focus 이동은 필수야?
A. 필수는 아니지만 긴 Form에서는 첫 오류 field로 이동하면 좋다.

Q. errors 객체가 비었는지 어떻게 확인해?
A. `Object.keys(errors).length > 0`으로 확인할 수 있다.

---

# 4. Submitting State Rules

## 4.1 Set Submitting State

### [개념]

Submitting State는 API 요청 진행 중 여부를 나타낸다.

Submit Flow에서는 요청 시작 전에 `true`, 성공/실패 후 `false`로 복구한다.

---

### [핵심]

Submitting State 기준:

- submitting
- isSubmitting
- pending
- loading
- disabled
- try catch finally
- submit button state
- duplicate submit prevention

---

### [실무]

Submitting 처리:

```javascript
setSubmitting(true);

try {
  await submitForm(requestBody);
} catch (error) {
  handleSubmitError(error);
} finally {
  setSubmitting(false);
}
```

버튼 UI:

```jsx
<button type="submit" disabled={submitting}>
  {submitting ? "처리 중..." : "제출"}
</button>
```

권장:

- Client Validation 통과 후 submitting true
- API 요청이 시작되기 전에 true 설정
- finally에서 false 복구
- 성공/실패 모두에서 버튼 상태 복구
- React Query mutation 사용 시 `isPending` 활용 가능

---

### [FAQ]

Q. submitting은 언제 true로 바꿔?
A. Client Validation 통과 후 API 요청을 시작하기 직전에 true로 바꾼다.

Q. submitting은 언제 false로 돌려?
A. 성공과 실패 모두에서 finally로 false 처리하는 것이 안전하다.

Q. submitting 상태는 왜 필요해?
A. 중복 제출 방지와 로딩 표시를 위해 필요하다.

Q. React Query를 쓰면 submitting state를 따로 둬야 해?
A. mutation의 `isPending` 같은 상태를 활용할 수 있다.

---

## 4.2 Duplicate Submit Prevention

### [개념]

Duplicate Submit Prevention은 같은 Form 요청이 여러 번 전송되는 것을 방지하는 기준이다.

Frontend에서는 submitting과 disabled로 중복 클릭을 줄이고, 중요한 요청은 Backend에서도 중복 방지해야 한다.

---

### [핵심]

중복 제출 방지 방법:

- submitting early return
- disabled submit button
- loading indicator
- debounce
- throttle
- idempotency key
- backend duplicate check
- payment caution
- order caution

---

### [실무]

handler early return:

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

중요 요청 기준:

```text
결제
→ Frontend disabled
→ Backend idempotency key
→ Payment Provider 중복 요청 처리

예약 / 주문 / 후원
→ Frontend duplicate prevention
→ Backend duplicate validation
```

권장:

- handler 초반에 submitting 확인
- submit button disabled
- 처리 중 문구 표시
- 결제/주문/예약은 Backend idempotency 고려
- 실패 시 다시 제출 가능하게 상태 복구

---

### [FAQ]

Q. 중복 제출은 어떻게 막아?
A. submitting 상태와 disabled 버튼을 사용하고 handler에서 early return 처리한다.

Q. Frontend에서만 막으면 충분해?
A. 아니다. 결제, 주문, 예약 같은 중요한 요청은 Backend 중복 방지도 필요하다.

Q. submitting early return은 왜 필요해?
A. disabled 적용 전이나 빠른 연속 이벤트로 들어오는 중복 요청을 줄이기 위해 필요하다.

Q. 실패 후 버튼은 다시 활성화해야 해?
A. 그렇다. 사용자가 수정 후 다시 제출할 수 있어야 한다.

---

# 5. Request Body Mapping Foundation

## 5.1 Request Body Mapping Definition

### [개념]

Request Body Mapping은 Form Values를 Backend API가 요구하는 Request DTO 구조로 변환하는 과정이다.

Form Values는 화면 입력용 상태이고 Request Body는 API 전송용 데이터다.

---

### [핵심]

Request Body Mapping 핵심 요소:

- Form Values
- Request DTO
- trim
- type conversion
- Number conversion
- boolean mapping
- enum mapping
- date format
- null handling
- optional field
- field name mapping
- FormData
- Backend Contract

---

### [실무]

Form Values 예:

```javascript
const values = {
  rating: "5",
  content: " 좋았어요 ",
};
```

Request Body 예:

```javascript
const requestBody = {
  rating: Number(values.rating),
  content: values.content.trim(),
};
```

Mapper 함수:

```javascript
function toCreateReviewRequest(values) {
  return {
    rating: Number(values.rating),
    content: values.content.trim(),
  };
}
```

권장:

- Form Values와 Request DTO 분리
- mapper 함수 작성
- Backend DTO 필드명과 일치
- 숫자/날짜/enum 변환 기준 명확화
- 빈 문자열/null/제외 기준 명확화

---

### [FAQ]

Q. Request Body Mapping이 뭐야?
A. Form State를 Backend API가 요구하는 Request DTO 구조로 변환하는 과정이다.

Q. Form Values를 그대로 API에 보내도 돼?
A. 간단한 경우 가능하지만 trim, 타입 변환, 필드명 변환이 필요하면 mapper를 사용하는 것이 좋다.

Q. Request Body Mapping은 언제 수행해?
A. Client Validation 통과 후 API 요청 직전에 수행한다.

Q. Form Values와 Request DTO를 왜 분리해?
A. input 값은 문자열일 수 있지만 Backend는 number, boolean, enum, null 등을 요구할 수 있기 때문이다.

---

## 5.2 Mapping Function Rules

### [개념]

Mapping Function은 Form Values를 Request DTO로 변환하는 전용 함수다.

Mapping Function을 분리하면 Submit Flow가 단순해지고 변환 기준을 재사용할 수 있다.

---

### [핵심]

Mapping Function 기준:

- input: form values
- output: request body
- pure function
- no API call
- type conversion
- trim
- field rename
- optional handling
- reusable mapper
- testable mapper

---

### [실무]

회원가입 mapper 예:

```typescript
type SignupFormValues = {
  email: string;
  password: string;
  nickname: string;
  marketingAgreed: boolean;
};

type SignupRequest = {
  email: string;
  password: string;
  nickname: string;
  marketingAgreed: boolean;
};

function toSignupRequest(values: SignupFormValues): SignupRequest {
  return {
    email: values.email.trim(),
    password: values.password,
    nickname: values.nickname.trim(),
    marketingAgreed: values.marketingAgreed,
  };
}
```

필드명 변환 예:

```javascript
function toUpdateProfileRequest(values) {
  return {
    displayName: values.nickname.trim(),
    introduction: values.bio.trim() || null,
  };
}
```

권장:

- API 호출과 mapper 분리
- mapper 내부에서 Form State 직접 변경 금지
- password 임의 trim 주의
- DTO 타입과 함께 관리
- 복잡한 Form은 `mappers` 파일 분리

---

### [FAQ]

Q. Mapping Function은 왜 필요해?
A. trim, Number 변환, null 처리, field rename을 일관되게 처리하기 위해 필요하다.

Q. Mapping Function 안에서 API 호출해도 돼?
A. 권장하지 않는다. mapper는 데이터 변환만 담당하는 것이 좋다.

Q. mapper에서 Form State를 직접 수정해도 돼?
A. 안 된다. 새 Request Body 객체를 반환해야 한다.

Q. mapper 파일은 언제 분리해?
A. 변환 로직이 길어지거나 여러 곳에서 재사용되면 분리한다.

---

# 6. Type Conversion Rules

## 6.1 String to Number Mapping

### [개념]

String to Number Mapping은 문자열 Form Values를 숫자 Request DTO 필드로 변환하는 처리다.

HTML input value는 숫자 input이어도 문자열로 들어올 수 있으므로 명시적 변환이 필요하다.

---

### [핵심]

숫자 변환 대상:

- rating
- price
- amount
- quantity
- age
- count
- page
- size
- categoryId
- festivalId
- Number conversion
- NaN validation

---

### [실무]

숫자 변환 예:

```javascript
function toCreateReviewRequest(values) {
  return {
    rating: Number(values.rating),
    content: values.content.trim(),
  };
}
```

검증 후 변환 Flow:

```text
values.rating === "5"
→ validate Number(values.rating)
→ if valid
→ request.rating = 5
```

주의:

- `Number("")`는 0이 될 수 있음
- 변환 전 Client Validation에서 빈 값과 NaN 확인
- 정수 필요 시 `Number.isInteger()` 검증
- Backend가 number를 기대하면 문자열 그대로 전송하지 않음
- Query Param은 문자열이어도 API 규칙에 맞게 처리

---

### [FAQ]

Q. number input 값은 Request Body에서 변환해야 해?
A. Backend가 숫자를 기대하면 Number 변환이 필요하다.

Q. Number 변환은 Validation 전에 해?
A. 보통 Validation에서 먼저 NaN과 범위를 확인하고 Mapping에서 변환한다.

Q. Number("")는 왜 조심해야 해?
A. 0으로 변환될 수 있어 빈 값 검증을 우회할 수 있다.

Q. 숫자 id도 변환해야 해?
A. Backend Request Body가 number를 기대하면 변환하는 것이 좋다.

---

## 6.2 String to Boolean Mapping

### [개념]

String to Boolean Mapping은 Form 값 또는 select/radio 값으로 들어온 문자열을 boolean Request DTO 필드로 변환하는 처리다.

Checkbox는 보통 boolean 상태로 관리하지만 select/radio는 문자열일 수 있다.

---

### [핵심]

boolean 변환 대상:

- checkbox checked
- agreement
- enabled
- public/private
- true/false string
- yes/no
- boolean DTO
- visibility flag

---

### [실무]

Checkbox boolean 예:

```javascript
function toAgreementRequest(values) {
  return {
    termsAgreed: values.termsAgreed,
    marketingAgreed: values.marketingAgreed,
  };
}
```

Radio string to boolean 예:

```javascript
function toVisibilityRequest(values) {
  return {
    public: values.visibility === "PUBLIC",
  };
}
```

주의:

- `"false"` 문자열은 boolean true로 평가될 수 있음
- `Boolean("false")` 사용 금지
- 명시 비교 사용
- Backend가 enum을 기대하는지 boolean을 기대하는지 확인
- checkbox는 checked 기반 boolean으로 관리

---

### [FAQ]

Q. checkbox 값은 boolean으로 바로 보내도 돼?
A. checked로 관리했다면 boolean으로 보낼 수 있다.

Q. `"false"`를 Boolean으로 변환하면 false야?
A. 아니다. `Boolean("false")`는 true다.

Q. 문자열을 boolean으로 변환할 때는 어떻게 해?
A. `value === "true"`처럼 명시 비교를 사용한다.

Q. 공개 여부는 boolean이 좋아 enum이 좋아?
A. Backend DTO 기준에 맞춘다. PUBLIC/PRIVATE enum이 더 명확할 수 있다.

---

## 6.3 Enum and Code Mapping

### [개념]

Enum and Code Mapping은 select, radio, checkbox group에서 선택된 값을 Backend enum 또는 code 값으로 맞춰 전송하는 처리다.

Frontend label과 Backend value를 분리해야 한다.

---

### [핵심]

Enum / Code Mapping 대상:

- category
- status
- role
- visibility
- regionCode
- themeCode
- postCategory
- enum value
- code value
- label value separation

---

### [실무]

Option 구조:

```javascript
const categoryOptions = [
  { label: "공지", value: "NOTICE" },
  { label: "리뷰", value: "REVIEW" },
];
```

Request Mapping:

```javascript
function toPostRequest(values) {
  return {
    title: values.title.trim(),
    category: values.category,
  };
}
```

다중 code mapping:

```javascript
function toSearchRequest(values) {
  return {
    themeCodes: values.themeCodes,
  };
}
```

권장:

- option value는 Backend enum/code와 일치
- 화면 label과 전송 value 분리
- enum 대소문자 통일
- 빈 값은 optional 처리 기준에 따라 제외
- Backend enum 변경 시 Frontend option도 업데이트

---

### [FAQ]

Q. select option value는 무엇으로 맞춰?
A. Backend enum 또는 code 값과 일치시키는 것이 좋다.

Q. 화면에 보이는 한글 label을 그대로 보내도 돼?
A. 보통 권장하지 않는다. Backend가 기대하는 code나 enum 값을 보내야 한다.

Q. enum 대소문자는 중요해?
A. 중요하다. Backend enum 이름과 정확히 일치해야 한다.

Q. 다중 선택 code는 어떻게 보내?
A. 선택된 code 배열을 Request Body 또는 Query Params 기준에 맞게 보낸다.

---

# 7. String Normalization Rules

## 7.1 Trim Mapping

### [개념]

Trim Mapping은 Request Body 생성 시 문자열 앞뒤 공백을 제거하는 처리다.

검색어, 제목, 닉네임, 내용은 trim할 수 있지만 password는 임의 trim에 주의해야 한다.

---

### [핵심]

Trim 대상:

- keyword
- title
- nickname
- content
- email
- bio
- optional text
- password caution
- Request DTO
- validation sync

---

### [실무]

Trim Mapping 예:

```javascript
function toPostRequest(values) {
  return {
    title: values.title.trim(),
    content: values.content.trim(),
  };
}
```

Email trim:

```javascript
function toLoginRequest(values) {
  return {
    email: values.email.trim(),
    password: values.password,
  };
}
```

주의:

- password는 임의 trim 금지 또는 정책 명확화
- validation에서 trim 기준을 사용했다면 request도 같은 기준 적용
- content 내부 줄바꿈은 보존
- 앞뒤 공백만 제거
- 전체 공백 제거와 trim은 다름

---

### [FAQ]

Q. Request Body 만들 때 trim해야 해?
A. 제목, 이메일, 검색어, 닉네임 등은 보통 trim하는 것이 좋다.

Q. password도 trim해?
A. 임의 trim은 권장하지 않는다. 서비스 정책에 따라 명확히 정해야 한다.

Q. validation에서는 trim했는데 request는 원본을 보내도 돼?
A. 기준이 달라져 혼란이 생길 수 있으므로 일치시키는 것이 좋다.

Q. textarea content를 trim하면 줄바꿈이 사라져?
A. trim은 앞뒤 공백만 제거하고 내부 줄바꿈은 보존한다.

---

## 7.2 Empty String to Null or Omit

### [개념]

Empty String to Null or Omit은 빈 문자열 Form Values를 Request DTO에서 `null`로 보낼지, field를 제외할지, 빈 문자열 그대로 보낼지 결정하는 기준이다.

Backend DTO 계약에 맞춰야 한다.

---

### [핵심]

빈 값 처리 방식:

- empty string
- null
- undefined
- omit field
- optional field
- nullable field
- query param omit
- DTO contract
- partial update

---

### [실무]

null 변환:

```javascript
function toProfileRequest(values) {
  return {
    nickname: values.nickname.trim(),
    bio: values.bio.trim() || null,
  };
}
```

field 제외:

```javascript
function toSearchParams(values) {
  const params = new URLSearchParams();

  if (values.keyword.trim()) {
    params.set("keyword", values.keyword.trim());
  }

  if (values.category) {
    params.set("category", values.category);
  }

  return params;
}
```

부분 수정 Request:

```javascript
function toPatchRequest(values) {
  const request = {};

  if (values.nickname.trim()) {
    request.nickname = values.nickname.trim();
  }

  return request;
}
```

권장:

- Backend DTO가 null 허용인지 확인
- Query Params는 빈 값 제외 권장
- PATCH는 변경된 field만 보낼 수 있음
- 빈 문자열이 의미 있는 값인지 확인
- required field는 mapping 전에 validation으로 차단

---

### [FAQ]

Q. 빈 문자열은 null로 보내야 해?
A. Backend DTO 계약에 따라 다르다.

Q. optional field가 비어 있으면 어떻게 해?
A. null로 보내거나 field를 제외할 수 있다.

Q. Query Param에 빈 문자열을 넣어도 돼?
A. 보통 제외하는 것이 깔끔하다.

Q. PATCH 요청에서는 모든 field를 보내야 해?
A. API 설계에 따라 다르지만 변경된 field만 보낼 수 있다.

---

# 8. Date and Time Mapping Rules

## 8.1 Date Mapping

### [개념]

Date Mapping은 Form의 날짜 값을 Backend DTO가 요구하는 형식으로 변환하는 처리다.

HTML date input은 보통 `yyyy-MM-dd` 문자열을 반환하므로 Backend LocalDate와 맞추기 쉽다.

---

### [핵심]

Date Mapping 요소:

- date input
- yyyy-MM-dd
- LocalDate
- ISO date
- Date object caution
- timezone caution
- request format
- display format

---

### [실무]

LocalDate Request 예:

```javascript
function toEventRequest(values) {
  return {
    startDate: values.startDate,
    endDate: values.endDate,
  };
}
```

검색 기간 Query Param:

```javascript
if (values.startDate) {
  params.set("startDate", values.startDate);
}

if (values.endDate) {
  params.set("endDate", values.endDate);
}
```

주의:

- `yyyy-MM-dd` 문자열을 Date 객체로 변환하면 timezone 이슈가 생길 수 있음
- Backend가 LocalDate면 문자열 그대로 전송하는 방식이 안전
- 표시용 날짜 format과 요청용 날짜 format 구분
- 날짜 범위 validation 후 mapping
- 빈 날짜는 optional 기준에 따라 제외

---

### [FAQ]

Q. date input 값은 Request Body에 어떻게 보내?
A. Backend가 LocalDate를 기대하면 `yyyy-MM-dd` 문자열 그대로 보내는 방식이 일반적이다.

Q. Date 객체로 변환해서 보내야 해?
A. 꼭 필요하지 않다. 오히려 timezone 문제를 만들 수 있다.

Q. 날짜 검색 조건이 비어 있으면?
A. Query Params에서 제외할 수 있다.

Q. 날짜 범위 mapping 전에 무엇을 해야 해?
A. startDate와 endDate 순서 검증을 먼저 해야 한다.

---

## 8.2 DateTime Mapping

### [개념]

DateTime Mapping은 날짜와 시간을 포함하는 Form 값을 Backend DTO 형식에 맞게 전송하는 처리다.

Timezone, UTC, LocalDateTime, ISO 8601 기준을 명확히 해야 한다.

---

### [핵심]

DateTime Mapping 요소:

- datetime-local
- LocalDateTime
- ISO 8601
- timezone
- UTC
- offset
- server timezone
- display timezone
- request timezone

---

### [실무]

datetime-local 값 예:

```javascript
const values = {
  startsAt: "2026-07-04T15:30",
};
```

Request Mapping 예:

```javascript
function toScheduleRequest(values) {
  return {
    startsAt: values.startsAt,
  };
}
```

UTC 변환이 필요한 경우:

```javascript
function toUtcISOString(localDateTime) {
  return new Date(localDateTime).toISOString();
}
```

주의:

- Backend가 LocalDateTime인지 Instant인지 확인
- UTC 변환 필요 여부 확인
- `datetime-local`은 timezone offset을 포함하지 않음
- 사용자 timezone 기준 저장인지 서버 기준 저장인지 명확화
- 날짜/시간 표시와 저장 기준 분리

---

### [FAQ]

Q. datetime-local 값은 timezone을 포함해?
A. 포함하지 않는다. 로컬 날짜/시간 문자열이다.

Q. UTC로 변환해서 보내야 해?
A. Backend DTO와 저장 정책에 따라 다르다.

Q. LocalDateTime을 기대하면 어떻게 보내?
A. 보통 `yyyy-MM-ddTHH:mm` 형식 문자열을 보낼 수 있다.

Q. DateTime Mapping에서 가장 조심할 점은?
A. timezone 기준이 불명확하면 시간이 어긋날 수 있다.

---

# 9. Query Params Mapping Rules

## 9.1 Search Form Query Params

### [개념]

Query Params Mapping은 Search Form Values를 URL Query String 또는 API 요청 params로 변환하는 처리다.

검색어, 필터, 정렬, 페이지 정보는 Query Params로 관리하는 경우가 많다.

---

### [핵심]

Query Params 대상:

- keyword
- category
- regionCode
- themeCode
- startDate
- endDate
- page
- size
- sort
- filters
- URLSearchParams
- empty value omit

---

### [실무]

Search Params 생성:

```javascript
function toFestivalSearchParams(values) {
  const params = new URLSearchParams();

  if (values.keyword.trim()) {
    params.set("keyword", values.keyword.trim());
  }

  if (values.regionCode) {
    params.set("regionCode", values.regionCode);
  }

  if (values.category) {
    params.set("category", values.category);
  }

  params.set("page", "1");

  return params;
}
```

API params 객체 예:

```javascript
function toSearchParamsObject(values) {
  return {
    keyword: values.keyword.trim() || undefined,
    category: values.category || undefined,
    page: 1,
  };
}
```

권장:

- 빈 값은 query param에서 제외
- 검색 조건 변경 시 page reset
- URL 공유가 필요한 검색 조건은 URL State로 관리
- sort/page/size 기본값 명확화
- Backend API parameter 이름과 일치

---

### [FAQ]

Q. 검색 Form 값은 Request Body로 보내?
A. 목록 검색은 보통 Query Params로 보내는 경우가 많다.

Q. 빈 검색어도 query param에 넣어?
A. 보통 제외하는 것이 좋다.

Q. 검색 조건이 바뀌면 page는 어떻게 해?
A. 대부분 1페이지로 reset한다.

Q. Query Params 이름은 무엇과 맞춰?
A. Backend Controller가 받는 parameter 이름과 맞춰야 한다.

---

## 9.2 Array Query Params

### [개념]

Array Query Params는 여러 선택값을 Query String으로 전송하는 방식이다.

Backend API 규칙에 따라 같은 key 반복, comma-separated string, JSON string 중 하나를 선택한다.

---

### [핵심]

Array Query 방식:

- repeated key
- comma separated
- array params
- selected codes
- filters
- backend parsing
- URLSearchParams append
- convention

---

### [실무]

같은 key 반복:

```javascript
const params = new URLSearchParams();

values.themeCodes.forEach((themeCode) => {
  params.append("themeCodes", themeCode);
});
```

comma-separated 방식:

```javascript
if (values.themeCodes.length > 0) {
  params.set("themeCodes", values.themeCodes.join(","));
}
```

권장:

- Backend parsing 방식 확인
- 팀 API 컨벤션 통일
- 배열 값이 없으면 제외
- code 값에 comma가 들어갈 가능성 고려
- Axios params 직렬화 기준 확인

---

### [FAQ]

Q. 배열 Query Param은 어떻게 보내?
A. Backend 규칙에 따라 같은 key 반복 또는 comma-separated string으로 보낸다.

Q. 어떤 방식이 더 좋아?
A. 팀 API 컨벤션과 Backend parsing 기준에 맞추는 것이 중요하다.

Q. 선택값이 없으면 어떻게 해?
A. 보통 해당 query param을 제외한다.

Q. Axios가 배열 params를 어떻게 직렬화해?
A. 설정에 따라 달라질 수 있으므로 paramsSerializer 기준을 확인해야 한다.

---

# 10. FormData Mapping Rules

## 10.1 Multipart FormData Mapping

### [개념]

FormData Mapping은 파일과 일반 Form 값을 함께 전송하기 위해 `FormData` 객체를 생성하는 처리다.

이미지 업로드, 첨부파일 업로드, 프로필 이미지 변경, 리뷰 이미지 등록에 사용한다.

---

### [핵심]

FormData Mapping 요소:

- FormData
- multipart/form-data
- file
- files
- append
- key matching
- Blob
- JSON part
- image upload
- Backend field name

---

### [실무]

단일 파일 FormData:

```javascript
function toProfileImageFormData(values) {
  const formData = new FormData();

  formData.append("nickname", values.nickname.trim());

  if (values.profileImage) {
    formData.append("profileImage", values.profileImage);
  }

  return formData;
}
```

여러 파일 FormData:

```javascript
function toReviewFormData(values) {
  const formData = new FormData();

  formData.append("content", values.content.trim());
  formData.append("rating", String(Number(values.rating)));

  values.images.forEach((image) => {
    formData.append("images", image);
  });

  return formData;
}
```

권장:

- FormData key와 Backend field name 일치
- 파일이 optional이면 존재할 때만 append
- 숫자는 문자열로 append될 수 있음
- 여러 파일은 Backend 규칙에 맞게 append
- JSON part 전송 방식은 Backend와 합의

---

### [FAQ]

Q. 파일 업로드는 Request Body JSON으로 보내?
A. 보통 FormData를 사용해 multipart 요청으로 보낸다.

Q. FormData에 숫자는 어떻게 넣어?
A. FormData append는 문자열 또는 Blob을 사용하므로 숫자는 문자열로 변환될 수 있다.

Q. 여러 파일은 어떻게 append해?
A. 같은 key로 여러 번 append하거나 Backend 규칙에 맞게 처리한다.

Q. FormData key는 무엇과 맞춰?
A. Backend multipart field name과 맞춰야 한다.

---

## 10.2 FormData Content-Type Rules

### [개념]

FormData Content-Type은 multipart 요청의 Content-Type 처리 기준이다.

브라우저나 HTTP client가 boundary를 자동 설정하도록 두는 방식이 일반적으로 안전하다.

---

### [핵심]

Content-Type 기준:

- multipart/form-data
- boundary
- automatic header
- Axios
- fetch
- do not manually set boundary
- Backend multipart parser

---

### [실무]

Axios 예:

```javascript
await api.post("/reviews", formData);
```

주의 예:

```javascript
await api.post("/reviews", formData, {
  headers: {
    "Content-Type": "multipart/form-data",
  },
});
```

주의:

- 수동 Content-Type 설정 시 boundary 누락 문제 가능
- Axios/브라우저가 자동 처리하게 두는 것이 안전한 경우가 많음
- 프로젝트 API client 설정 확인
- Backend multipart 설정 확인
- JSON API와 multipart API 분리

---

### [FAQ]

Q. FormData 요청에서 Content-Type을 직접 설정해야 해?
A. 보통 브라우저나 Axios가 boundary를 포함해 자동 설정하게 두는 것이 안전하다.

Q. boundary가 뭐야?
A. multipart 각 part를 구분하는 문자열이다.

Q. Content-Type을 잘못 설정하면 어떻게 돼?
A. Backend가 multipart 데이터를 제대로 파싱하지 못할 수 있다.

Q. JSON 요청과 multipart 요청은 API 함수에서 구분해야 해?
A. 구분하는 것이 좋다. 요청 생성과 헤더 기준이 다르다.

---

# 11. Success Handling Rules

## 11.1 Submit Success Handling

### [개념]

Submit Success Handling은 API 요청이 성공했을 때 UI를 어떻게 갱신할지 결정하는 처리다.

성공 후 reset, redirect, toast, server state refresh, modal close, optimistic update 등을 선택할 수 있다.

---

### [핵심]

Success Handling 대상:

- reset form
- redirect
- toast message
- close modal
- refresh list
- invalidate query
- update cache
- optimistic update
- success message
- latest server state

---

### [실무]

생성 Form 성공:

```javascript
await createReview(requestBody);

resetForm();
showToast("리뷰가 등록되었습니다.");
```

수정 Form 성공:

```javascript
await updateProfile(requestBody);

await refetchProfile();
showToast("프로필이 수정되었습니다.");
```

Modal Form 성공:

```javascript
await submitForm(requestBody);

closeModal();
refreshList();
```

권장:

- 생성 성공 후 reset 가능
- 수정 성공 후 서버 최신값 반영
- 목록 데이터 refresh 또는 cache invalidation
- 성공 메시지는 짧게 표시
- redirect 여부 명확화
- 성공 후 errors와 submitError 정리

---

### [FAQ]

Q. Submit 성공 후 무엇을 해야 해?
A. reset, redirect, 목록 갱신, toast, modal close 등 UX에 맞는 처리를 수행한다.

Q. 생성 Form은 성공 후 reset해도 돼?
A. 가능하다. 새 입력을 받을 Form이면 reset이 적합하다.

Q. 수정 Form은 성공 후 reset해야 해?
A. 서버 최신값을 다시 반영하고 initialValues를 갱신하는 것이 좋다.

Q. 성공 후 목록을 다시 불러와야 해?
A. 목록에 반영되어야 한다면 refetch 또는 cache invalidation이 필요하다.

---

## 11.2 Form Reset After Success

### [개념]

Form Reset After Success는 제출 성공 후 Form State를 초기값 또는 서버 최신값으로 되돌리는 처리다.

생성 Form과 수정 Form의 reset 기준은 다르다.

---

### [핵심]

Reset 대상:

- values
- errors
- touched
- dirty
- submitted
- submitError
- file input
- preview url
- initialValues
- latest server data

---

### [실무]

생성 Form reset:

```javascript
function resetCreateForm() {
  setValues(initialValues);
  setErrors({});
  setTouched({});
  setSubmitError("");
  setSubmitted(false);
}
```

수정 Form reset:

```javascript
function resetEditForm(latestValues) {
  setInitialValues(latestValues);
  setValues(latestValues);
  setErrors({});
  setTouched({});
  setSubmitError("");
}
```

파일 preview 정리:

```javascript
if (previewUrl) {
  URL.revokeObjectURL(previewUrl);
}
```

권장:

- 성공 후에만 자동 reset
- 실패 후 reset 금지
- 수정 Form은 서버 최신값 기준으로 reset
- file input은 별도 reset 고려
- preview URL 정리 필요

---

### [FAQ]

Q. Submit 성공 후 항상 reset해야 해?
A. 아니다. 생성 Form은 reset할 수 있고 수정 Form은 최신 서버 값 반영이 적합하다.

Q. Submit 실패 후 reset해도 돼?
A. 보통 하지 않는다. 사용자가 수정 후 다시 제출할 수 있어야 한다.

Q. 수정 Form의 reset 기준은 뭐야?
A. 서버에서 저장된 최신 값이 기준이다.

Q. file input reset은 values 초기화만으로 충분해?
A. 아닐 수 있다. ref, key 변경, preview URL 정리가 필요할 수 있다.

---

# 12. Submit Flow Patterns

## 12.1 Create Form Submit Pattern

### [개념]

Create Form Submit Pattern은 새 데이터를 등록하는 Form의 제출 흐름이다.

성공 후 reset, 목록 갱신, 상세 페이지 이동, 모달 닫기 등을 수행한다.

---

### [핵심]

Create Form 요소:

- initial empty values
- required validation
- create request
- reset after success
- list refresh
- detail redirect
- toast
- duplicate submit prevention

---

### [실무]

Create Review 예:

```javascript
async function handleSubmit(event) {
  event.preventDefault();

  if (submitting) {
    return;
  }

  setErrors({});
  setSubmitError("");

  const nextErrors = validateReview(values);
  setErrors(nextErrors);

  if (Object.keys(nextErrors).length > 0) {
    return;
  }

  setSubmitting(true);

  try {
    const requestBody = toCreateReviewRequest(values);

    await createReview(requestBody);

    resetForm();
    refreshReviews();
  } catch (error) {
    const mappedError = mapApiError(error);

    setErrors(mappedError.fieldErrors);
    setSubmitError(mappedError.globalError);
  } finally {
    setSubmitting(false);
  }
}
```

권장:

- 생성 Form 초기값은 명확히 설정
- 성공 후 reset 가능
- 목록 또는 서버 상태 갱신
- 중복 제출 방지
- 실패 후 입력값 유지

---

### [FAQ]

Q. Create Form은 성공 후 reset해도 돼?
A. 가능하다. 새 항목을 계속 입력하는 Form이면 reset이 적합하다.

Q. Create 성공 후 목록은 어떻게 갱신해?
A. refetch, cache invalidation, optimistic update 중 하나를 사용할 수 있다.

Q. Create 실패 후 입력값은 유지해?
A. 보통 유지한다.

Q. Create Form에서 가장 중요한 Submit 기준은?
A. 검증, 중복 제출 방지, Request Body Mapping, 성공 후 상태 갱신이다.

---

## 12.2 Edit Form Submit Pattern

### [개념]

Edit Form Submit Pattern은 기존 데이터를 수정하는 Form의 제출 흐름이다.

Server State에서 초기값을 만들고, 사용자가 수정한 Form State를 Request DTO로 변환해 제출한다.

---

### [핵심]

Edit Form 요소:

- fetch detail
- initialValues
- values copy
- dirty check
- update request
- latest server state
- reset with latest data
- conflict handling
- permission error

---

### [실무]

Edit Profile Flow:

```text
Fetch Profile
→ Build Initial Values
→ Initialize Form Values
→ User Modify
→ Validate
→ Build Update Request
→ API Update
→ Refetch Profile
→ Reset Form with Latest Values
```

Edit Submit 예:

```javascript
async function handleSubmit(event) {
  event.preventDefault();

  if (!isDirty || submitting) {
    return;
  }

  const nextErrors = validateProfile(values);
  setErrors(nextErrors);

  if (Object.keys(nextErrors).length > 0) {
    return;
  }

  setSubmitting(true);

  try {
    const requestBody = toUpdateProfileRequest(values);

    const latestProfile = await updateProfile(requestBody);

    resetEditForm(toProfileFormValues(latestProfile));
  } catch (error) {
    const mappedError = mapApiError(error);

    setErrors(mappedError.fieldErrors);
    setSubmitError(mappedError.globalError);
  } finally {
    setSubmitting(false);
  }
}
```

권장:

- 서버 데이터와 Form State 분리
- 변경사항 없으면 submit 비활성화 가능
- 성공 후 최신 서버 데이터 반영
- 403, 404, 409 처리 기준 포함
- dirty check는 복잡한 값에서 주의

---

### [FAQ]

Q. Edit Form 초기값은 어디서 와?
A. 서버에서 받은 상세 데이터를 Form Values로 변환해 사용한다.

Q. Edit Form에서 Server State를 직접 수정해도 돼?
A. 권장하지 않는다. Form State 복사본으로 관리해야 한다.

Q. 변경사항이 없으면 submit을 막아도 돼?
A. 가능하다. dirty check로 저장 버튼을 비활성화할 수 있다.

Q. Edit 성공 후 Form State는 어떻게 해?
A. 서버 최신값으로 initialValues와 values를 갱신하는 것이 좋다.

---

## 12.3 Search Form Submit Pattern

### [개념]

Search Form Submit Pattern은 검색어와 필터를 제출해 목록 데이터를 조회하는 흐름이다.

입력 중 값은 Local Form State로 두고 제출된 검색 조건은 URL Query Params로 관리할 수 있다.

---

### [핵심]

Search Form 요소:

- keyword
- filters
- local input state
- URL Search Params
- query params mapping
- page reset
- list fetch
- empty query omit
- debounce optional

---

### [실무]

Search Submit Flow:

```text
User Typing
→ Local Form State
→ Submit
→ Trim Keyword
→ Build Query Params
→ Reset Page
→ Update URL
→ Fetch List
```

Search Submit 예:

```javascript
function handleSubmit(event) {
  event.preventDefault();

  const params = toSearchParams(values);

  setSearchParams(params);
}
```

Search Params Mapper:

```javascript
function toSearchParams(values) {
  const params = new URLSearchParams();

  if (values.keyword.trim()) {
    params.set("keyword", values.keyword.trim());
  }

  if (values.category) {
    params.set("category", values.category);
  }

  params.set("page", "1");

  return params;
}
```

권장:

- 검색 submit 시 page reset
- 빈 값은 params에서 제외
- URL 공유가 필요하면 URL Search Params 사용
- 실시간 검색은 debounce 고려
- 목록 fetch는 URL 조건 기준으로 실행 가능

---

### [FAQ]

Q. Search Form은 Request Body를 사용해?
A. 보통 Query Params를 사용한다.

Q. 검색어 입력 중 값은 어디에 둬?
A. Local Form State에 둔다.

Q. 제출된 검색 조건은 어디에 둬?
A. URL Search Params로 관리할 수 있다.

Q. 검색 조건 변경 시 page를 reset해야 해?
A. 대부분 1페이지로 reset하는 것이 좋다.

---

# 13. Submit Flow Troubleshooting

## 13.1 Submit Not Working

### [개념]

Submit Not Working은 Form 제출 이벤트가 발생하지 않거나 API 요청이 실행되지 않는 문제다.

button type, form onSubmit, validation return, disabled 상태, handler 연결 오류가 주요 원인이다.

---

### [핵심]

주요 원인:

- form onSubmit 없음
- button type button
- disabled true
- preventDefault 위치 오류
- validation always fails
- early return
- API function not called
- onSubmit immediate call
- React Hook Form handleSubmit misuse

---

### [실무]

Debug Flow:

```text
Button type 확인
→ form onSubmit 확인
→ handleSubmit 실행 확인
→ disabled 조건 확인
→ validation result 확인
→ early return 확인
→ API function call 확인
→ Network Tab 확인
```

문제 예:

```jsx
<form onSubmit={handleSubmit()}>
```

수정:

```jsx
<form onSubmit={handleSubmit}>
```

문제 예:

```jsx
<button type="button">저장</button>
```

수정:

```jsx
<button type="submit">저장</button>
```

---

### [FAQ]

Q. 버튼을 눌러도 submit이 안 돼?
A. button type, form onSubmit, disabled 상태, validation return을 확인해야 한다.

Q. Network 요청이 안 보여?
A. submit handler가 실행되지 않았거나 validation에서 중단되었을 수 있다.

Q. onSubmit={handleSubmit()}은 왜 문제야?
A. 렌더링 시 함수가 즉시 실행될 수 있으므로 함수 참조를 전달해야 한다.

Q. submit button type이 button이면 어떻게 돼?
A. Form submit이 발생하지 않는다.

---

## 13.2 Request Body Wrong Shape

### [개념]

Request Body Wrong Shape는 Frontend가 Backend DTO와 다른 구조로 데이터를 보내는 문제다.

필드명 불일치, 타입 불일치, nested 구조 불일치, FormData key 오류가 주요 원인이다.

---

### [핵심]

주요 원인:

- field name mismatch
- string instead of number
- missing required field
- extra field
- nested object mismatch
- array format mismatch
- null handling mismatch
- FormData key mismatch

---

### [실무]

문제 예:

```javascript
const requestBody = {
  reviewContent: values.content,
  score: values.rating,
};
```

Backend DTO:

```java
public class ReviewRequest {
  private String content;
  private Integer rating;
}
```

수정:

```javascript
const requestBody = {
  content: values.content.trim(),
  rating: Number(values.rating),
};
```

Debug Flow:

```text
Network Payload 확인
→ Backend DTO 확인
→ field name 확인
→ type 확인
→ null/empty 처리 확인
→ array/multipart key 확인
```

---

### [FAQ]

Q. Request Body가 틀렸는지 어떻게 확인해?
A. 브라우저 Network 탭의 Payload와 Backend DTO를 비교한다.

Q. field name이 다르면 어떻게 돼?
A. Backend에서 값이 null로 들어가거나 validation error가 발생할 수 있다.

Q. 숫자를 문자열로 보내면 문제야?
A. Backend 변환이 가능할 수도 있지만 DTO가 number를 기대하면 명시 변환이 안전하다.

Q. FormData key가 틀리면 어떻게 돼?
A. Backend가 파일이나 값을 받지 못할 수 있다.

---

## 13.3 Submitting Never Ends

### [개념]

Submitting Never Ends는 제출 후 버튼이 계속 loading 또는 disabled 상태로 남는 문제다.

성공/실패 후 `setSubmitting(false)`가 실행되지 않거나 예외 흐름이 누락될 때 발생한다.

---

### [핵심]

주요 원인:

- finally missing
- catch missing
- early return after setSubmitting true
- unhandled promise
- await missing
- navigation before cleanup
- component unmount caution

---

### [실무]

문제 예:

```javascript
setSubmitting(true);

await submitForm(requestBody);

setSubmitting(false);
```

요청이 실패하면 `setSubmitting(false)`가 실행되지 않을 수 있다.

수정:

```javascript
setSubmitting(true);

try {
  await submitForm(requestBody);
} catch (error) {
  handleError(error);
} finally {
  setSubmitting(false);
}
```

주의:

- setSubmitting true 이후 return 경로 주의
- await 누락 시 상태 복구 타이밍 오류 가능
- 페이지 이동 시 cleanup 기준 확인
- React Query mutation 상태 활용 가능

---

### [FAQ]

Q. 제출 버튼이 계속 로딩 중이면?
A. finally에서 submitting false를 처리하는지 확인해야 한다.

Q. catch만 있으면 충분해?
A. 성공과 실패 모두에서 복구하려면 finally가 안전하다.

Q. setSubmitting true 이후 return하면 어떻게 돼?
A. false 복구 없이 loading 상태가 계속될 수 있다.

Q. await를 빼면 문제가 생겨?
A. 요청 완료 전에 다음 코드가 실행되어 상태 처리 순서가 꼬일 수 있다.

---

# 14. Submit Flow Checklist

## 14.1 Implementation Checklist

### [개념]

Submit Flow Checklist는 Form 제출 흐름, Request Body Mapping, API 요청, 성공/실패 처리가 안정적으로 연결되었는지 검수하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] form에 onSubmit이 연결되었는가?
- [ ] submit handler에서 preventDefault를 호출하는가?
- [ ] submit button에 type="submit"이 명시되었는가?
- [ ] 일반 button에 type="button"이 명시되었는가?
- [ ] submitting 상태로 중복 제출을 방지하는가?
- [ ] submit handler 초반에 submitting early return이 있는가?
- [ ] 제출 전 previous errors와 submitError를 초기화하는가?
- [ ] Client Validation을 API 요청 전에 수행하는가?
- [ ] Validation 실패 시 API 요청을 중단하는가?
- [ ] 검증 실패 후 입력값을 유지하는가?
- [ ] Client Validation 통과 후 Request Body Mapping을 수행하는가?
- [ ] Form Values와 Request DTO를 분리했는가?
- [ ] mapper 함수가 trim/type conversion/null handling을 처리하는가?
- [ ] 숫자 문자열을 Number로 변환하는가?
- [ ] Boolean 문자열 변환에 Boolean("false")를 사용하지 않는가?
- [ ] enum/code 값이 Backend DTO와 일치하는가?
- [ ] 빈 문자열/null/omit 기준이 Backend 계약과 일치하는가?
- [ ] date/datetime format이 Backend DTO와 일치하는가?
- [ ] Query Params에서 빈 값 제외 기준이 있는가?
- [ ] 검색 조건 변경 시 page reset 기준이 있는가?
- [ ] FormData key가 Backend multipart field name과 일치하는가?
- [ ] FormData Content-Type 처리 기준이 안전한가?
- [ ] API 요청 성공 후 reset/redirect/refetch 기준이 정의되어 있는가?
- [ ] API 요청 실패 후 Server Error Mapping을 수행하는가?
- [ ] catch/finally에서 submitting 상태를 복구하는가?
- [ ] 실패 후 Form Values를 유지하는가?
```

---

### [실무]

검수 Flow:

```text
Submit Event Check
→ Validation Flow Check
→ Duplicate Submit Check
→ Request Mapping Check
→ Type Conversion Check
→ API Request Check
→ Success Handling Check
→ Error Handling Check
→ Reset / Refetch Check
→ Troubleshooting Review
```

---

### [FAQ]

Q. Submit Flow 검수에서 가장 중요한 것은?
A. preventDefault, validation, duplicate prevention, request mapping, error handling, submitting 복구다.

Q. Request Body Mapping 검수에서 가장 중요한 것은?
A. Backend DTO와 field name, type, null 처리, 날짜 형식이 일치하는지 확인하는 것이다.

Q. Submit Flow 다음에는 무엇을 검토해?
A. React Hook Form, Form Accessibility, Form Component Design, Troubleshooting을 검토한다.

---

# Retrieval Queries

### [FAQ]

Q. Submit Flow가 뭐야?
A. Form 제출 시 검증, 요청 생성, API 호출, 성공/실패 처리를 수행하는 전체 흐름이다.

Q. Submit Flow에서 가장 중요한 것은 뭐야?
A. preventDefault, Client Validation, Request Body Mapping, submitting 상태, Server Error Handling이다.

Q. Submit Flow에서 Client Validation은 언제 해?
A. API 요청 전에 수행하고 실패하면 요청을 중단한다.

Q. Submit 실패 후 입력값은 유지해?
A. 보통 유지한다. 사용자가 수정 후 다시 제출할 수 있어야 한다.

Q. onSubmit은 왜 사용해?
A. 버튼 클릭과 Enter key 제출을 일관되게 처리할 수 있기 때문이다.

Q. preventDefault는 왜 필요해?
A. 브라우저 기본 Form 제출과 페이지 새로고침을 막기 위해 필요하다.

Q. onClick으로 submit 처리하면 안 돼?
A. 가능하지만 Enter key 제출과 접근성 측면에서 form onSubmit이 더 적합하다.

Q. preventDefault를 빼면 어떻게 돼?
A. Form 제출 시 페이지가 새로고침될 수 있다.

Q. Submit Button type은 뭐야?
A. Form 제출 버튼은 `type="submit"`을 사용한다.

Q. 취소 버튼도 submit이 될 수 있어?
A. type을 명시하지 않으면 의도치 않게 submit될 수 있으므로 `type="button"`을 사용한다.

Q. 제출 중 버튼을 disabled 해야 해?
A. 권장한다. 중복 클릭과 중복 요청을 줄일 수 있다.

Q. disabled만으로 중복 제출이 완전히 막혀?
A. 아니다. handler에서도 submitting 상태를 확인하는 것이 좋다.

Q. Submit 전에 에러를 초기화해야 해?
A. 권장한다. 이전 제출의 에러가 현재 제출 결과와 섞일 수 있다.

Q. submitError도 초기화해야 해?
A. 권장한다. 이전 Global Error가 계속 남으면 혼란스럽다.

Q. Validation 실패 시 API 요청을 보내도 돼?
A. 보통 보내지 않는다. Client Validation 실패 시 요청을 중단한다.

Q. 검증 실패 후 입력값은 지워?
A. 아니다. 사용자가 수정할 수 있도록 유지한다.

Q. 검증 실패 후 focus 이동은 필수야?
A. 필수는 아니지만 긴 Form에서는 첫 오류 field로 이동하면 좋다.

Q. submitting은 언제 true로 바꿔?
A. Client Validation 통과 후 API 요청을 시작하기 직전에 true로 바꾼다.

Q. submitting은 언제 false로 돌려?
A. 성공과 실패 모두에서 finally로 false 처리하는 것이 안전하다.

Q. submitting 상태는 왜 필요해?
A. 중복 제출 방지와 로딩 표시를 위해 필요하다.

Q. 중복 제출은 어떻게 막아?
A. submitting 상태와 disabled 버튼을 사용하고 handler에서 early return 처리한다.

Q. Frontend에서만 중복 제출을 막으면 충분해?
A. 아니다. 결제, 주문, 예약 같은 중요한 요청은 Backend 중복 방지도 필요하다.

Q. Request Body Mapping이 뭐야?
A. Form State를 Backend API가 요구하는 Request DTO 구조로 변환하는 과정이다.

Q. Form Values를 그대로 API에 보내도 돼?
A. 간단한 경우 가능하지만 trim, 타입 변환, 필드명 변환이 필요하면 mapper를 사용하는 것이 좋다.

Q. Request Body Mapping은 언제 수행해?
A. Client Validation 통과 후 API 요청 직전에 수행한다.

Q. Form Values와 Request DTO를 왜 분리해?
A. input 값은 문자열일 수 있지만 Backend는 number, boolean, enum, null 등을 요구할 수 있기 때문이다.

Q. Mapping Function은 왜 필요해?
A. trim, Number 변환, null 처리, field rename을 일관되게 처리하기 위해 필요하다.

Q. Mapping Function 안에서 API 호출해도 돼?
A. 권장하지 않는다. mapper는 데이터 변환만 담당하는 것이 좋다.

Q. mapper에서 Form State를 직접 수정해도 돼?
A. 안 된다. 새 Request Body 객체를 반환해야 한다.

Q. number input 값은 Request Body에서 변환해야 해?
A. Backend가 숫자를 기대하면 Number 변환이 필요하다.

Q. Number 변환은 Validation 전에 해?
A. 보통 Validation에서 먼저 NaN과 범위를 확인하고 Mapping에서 변환한다.

Q. Number("")는 왜 조심해야 해?
A. 0으로 변환될 수 있어 빈 값 검증을 우회할 수 있다.

Q. `"false"`를 Boolean으로 변환하면 false야?
A. 아니다. `Boolean("false")`는 true다.

Q. 문자열을 boolean으로 변환할 때는 어떻게 해?
A. `value === "true"`처럼 명시 비교를 사용한다.

Q. select option value는 무엇으로 맞춰?
A. Backend enum 또는 code 값과 일치시키는 것이 좋다.

Q. 화면에 보이는 한글 label을 그대로 보내도 돼?
A. 보통 권장하지 않는다. Backend가 기대하는 code나 enum 값을 보내야 한다.

Q. enum 대소문자는 중요해?
A. 중요하다. Backend enum 이름과 정확히 일치해야 한다.

Q. Request Body 만들 때 trim해야 해?
A. 제목, 이메일, 검색어, 닉네임 등은 보통 trim하는 것이 좋다.

Q. password도 trim해?
A. 임의 trim은 권장하지 않는다. 서비스 정책에 따라 명확히 정해야 한다.

Q. validation에서는 trim했는데 request는 원본을 보내도 돼?
A. 기준이 달라져 혼란이 생길 수 있으므로 일치시키는 것이 좋다.

Q. 빈 문자열은 null로 보내야 해?
A. Backend DTO 계약에 따라 다르다.

Q. optional field가 비어 있으면 어떻게 해?
A. null로 보내거나 field를 제외할 수 있다.

Q. PATCH 요청에서는 모든 field를 보내야 해?
A. API 설계에 따라 다르지만 변경된 field만 보낼 수 있다.

Q. date input 값은 Request Body에 어떻게 보내?
A. Backend가 LocalDate를 기대하면 `yyyy-MM-dd` 문자열 그대로 보내는 방식이 일반적이다.

Q. Date 객체로 변환해서 보내야 해?
A. 꼭 필요하지 않다. 오히려 timezone 문제를 만들 수 있다.

Q. datetime-local 값은 timezone을 포함해?
A. 포함하지 않는다. 로컬 날짜/시간 문자열이다.

Q. UTC로 변환해서 보내야 해?
A. Backend DTO와 저장 정책에 따라 다르다.

Q. 검색 Form 값은 Request Body로 보내?
A. 목록 검색은 보통 Query Params로 보내는 경우가 많다.

Q. 빈 검색어도 query param에 넣어?
A. 보통 제외하는 것이 좋다.

Q. 검색 조건이 바뀌면 page는 어떻게 해?
A. 대부분 1페이지로 reset한다.

Q. 배열 Query Param은 어떻게 보내?
A. Backend 규칙에 따라 같은 key 반복 또는 comma-separated string으로 보낸다.

Q. 파일 업로드는 Request Body JSON으로 보내?
A. 보통 FormData를 사용해 multipart 요청으로 보낸다.

Q. FormData에 숫자는 어떻게 넣어?
A. FormData append는 문자열 또는 Blob을 사용하므로 숫자는 문자열로 변환될 수 있다.

Q. 여러 파일은 어떻게 append해?
A. 같은 key로 여러 번 append하거나 Backend 규칙에 맞게 처리한다.

Q. FormData 요청에서 Content-Type을 직접 설정해야 해?
A. 보통 브라우저나 Axios가 boundary를 포함해 자동 설정하게 두는 것이 안전하다.

Q. boundary가 뭐야?
A. multipart 각 part를 구분하는 문자열이다.

Q. Submit 성공 후 무엇을 해야 해?
A. reset, redirect, 목록 갱신, toast, modal close 등 UX에 맞는 처리를 수행한다.

Q. 생성 Form은 성공 후 reset해도 돼?
A. 가능하다. 새 입력을 받을 Form이면 reset이 적합하다.

Q. 수정 Form은 성공 후 reset해야 해?
A. 서버 최신값을 다시 반영하고 initialValues를 갱신하는 것이 좋다.

Q. Submit 실패 후 reset해도 돼?
A. 보통 하지 않는다. 사용자가 수정 후 다시 제출할 수 있어야 한다.

Q. Create Form에서 가장 중요한 Submit 기준은?
A. 검증, 중복 제출 방지, Request Body Mapping, 성공 후 상태 갱신이다.

Q. Edit Form 초기값은 어디서 와?
A. 서버에서 받은 상세 데이터를 Form Values로 변환해 사용한다.

Q. Edit Form에서 Server State를 직접 수정해도 돼?
A. 권장하지 않는다. Form State 복사본으로 관리해야 한다.

Q. 변경사항이 없으면 submit을 막아도 돼?
A. 가능하다. dirty check로 저장 버튼을 비활성화할 수 있다.

Q. Search Form은 Request Body를 사용해?
A. 보통 Query Params를 사용한다.

Q. 검색어 입력 중 값은 어디에 둬?
A. Local Form State에 둔다.

Q. 제출된 검색 조건은 어디에 둬?
A. URL Search Params로 관리할 수 있다.

Q. 버튼을 눌러도 submit이 안 돼?
A. button type, form onSubmit, disabled 상태, validation return을 확인해야 한다.

Q. Network 요청이 안 보여?
A. submit handler가 실행되지 않았거나 validation에서 중단되었을 수 있다.

Q. onSubmit={handleSubmit()}은 왜 문제야?
A. 렌더링 시 함수가 즉시 실행될 수 있으므로 함수 참조를 전달해야 한다.

Q. Request Body가 틀렸는지 어떻게 확인해?
A. 브라우저 Network 탭의 Payload와 Backend DTO를 비교한다.

Q. field name이 다르면 어떻게 돼?
A. Backend에서 값이 null로 들어가거나 validation error가 발생할 수 있다.

Q. 제출 버튼이 계속 로딩 중이면?
A. finally에서 submitting false를 처리하는지 확인해야 한다.

Q. catch만 있으면 충분해?
A. 성공과 실패 모두에서 복구하려면 finally가 안전하다.

Q. Submit Flow 다음 문서는 뭐가 좋아?
A. React Hook Form, Form Accessibility, Form Component Design, Troubleshooting 순서가 좋다.
