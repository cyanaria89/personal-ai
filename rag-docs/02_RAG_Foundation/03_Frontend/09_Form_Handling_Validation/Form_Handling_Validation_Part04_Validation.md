# Form Handling & Validation Part04 - Validation

---

# 1. Validation Foundation

## 1.1 Validation Definition

### [개념]

Validation은 Form 입력값이 서비스 규칙, Backend DTO 규칙, 데이터 무결성 규칙에 맞는지 확인하는 과정이다.

Frontend Validation은 사용자 경험을 개선하기 위한 사전 검증이고, Backend Validation은 데이터 보호를 위한 최종 검증이다.

---

### [핵심]

Validation 핵심 요소:

- Client Validation
- Server Validation
- Required Validation
- Length Validation
- Format Validation
- Number Range Validation
- Date Range Validation
- Cross Field Validation
- File Validation
- Field Error
- Global Error
- Validation Function
- Error State
- Request DTO Contract

---

### [실무]

2026 실무 기준에서 Validation은 아래 흐름으로 처리한다.

```text
User Input
→ Optional Field Validation
→ Submit
→ Client Validation
→ If Invalid Stop
→ API Request
→ Server Validation
→ Success or Server Error Mapping
```

Validation 책임 분리:

| 구분              | 위치              | 목적                 | 예                  |
| ----------------- | ----------------- | -------------------- | ------------------- |
| Client Validation | Frontend          | UX 개선              | 빈 값, 형식, 길이   |
| Server Validation | Backend           | 데이터 무결성 / 보안 | 중복, 권한, DB 제약 |
| Field Validation  | 특정 Field        | 개별 입력 검증       | email, password     |
| Form Validation   | Form 전체         | 여러 값 조합 검증    | password confirm    |
| Domain Validation | Service / Backend | 비즈니스 규칙        | 소유자, 결제, 예약  |

---

### [FAQ]

Q. Validation이 뭐야?
A. Form 입력값이 서비스 규칙과 Backend DTO 규칙에 맞는지 확인하는 과정이다.

Q. Frontend Validation만 있으면 충분해?
A. 아니다. Frontend Validation은 우회될 수 있으므로 Backend Validation이 반드시 필요하다.

Q. Validation에서 가장 중요한 기준은 뭐야?
A. Client Validation은 UX용, Server Validation은 최종 검증이라는 역할 분리다.

Q. Validation 결과는 어디에 저장해?
A. 보통 errors 객체와 submitError 같은 Error State에 저장한다.

---

# 2. Client Validation Rules

## 2.1 Client Validation Definition

### [개념]

Client Validation은 사용자가 Form을 제출하기 전에 브라우저에서 입력값을 검증하는 과정이다.

Client Validation은 빠른 피드백을 제공하지만 보안과 데이터 무결성의 최종 기준이 될 수 없다.

---

### [핵심]

Client Validation 대상:

- required
- min length
- max length
- email format
- password format
- password confirm
- number range
- date range
- checkbox required
- file size
- file type
- trim
- forbidden characters

---

### [실무]

Validation 함수 예:

```javascript
function validateReview(values) {
  const errors = {};

  if (!values.content.trim()) {
    errors.content = "리뷰 내용을 입력해 주세요.";
  }

  const rating = Number(values.rating);

  if (Number.isNaN(rating) || rating < 1 || rating > 5) {
    errors.rating = "평점은 1점에서 5점 사이여야 합니다.";
  }

  return errors;
}
```

Submit 적용:

```javascript
function handleSubmit(event) {
  event.preventDefault();

  const nextErrors = validateReview(values);
  setErrors(nextErrors);

  if (Object.keys(nextErrors).length > 0) {
    return;
  }

  submitForm();
}
```

권장:

- submit 전 validation 수행
- errors 객체로 field별 메시지 관리
- trim 기준 명확화
- 필수값과 형식 검증 분리
- Validation 함수는 가능하면 순수 함수로 작성
- Server Validation과 규칙 일치

---

### [FAQ]

Q. Client Validation이 뭐야?
A. 사용자가 Form을 제출하기 전에 Frontend에서 입력값을 검증하는 UX용 검증이다.

Q. Client Validation은 왜 필요해?
A. 사용자가 잘못된 입력을 빠르게 수정할 수 있도록 돕기 위해 필요하다.

Q. Client Validation이 있으면 Server Validation은 없어도 돼?
A. 안 된다. Client Validation은 우회 가능하므로 Backend 검증이 반드시 필요하다.

Q. Validation 함수는 Component 안에 둬도 돼?
A. 간단한 Form은 가능하지만 복잡하거나 재사용되면 별도 validator 파일로 분리하는 것이 좋다.

---

## 2.2 Validation Function Rules

### [개념]

Validation Function은 Form Values를 입력받아 Field Error 객체를 반환하는 함수다.

검증 로직을 함수로 분리하면 Submit Flow, 테스트, 재사용, 유지보수가 쉬워진다.

---

### [핵심]

Validation Function 기준:

- input: values
- output: errors object
- pure function
- no API call
- field name key
- empty object if valid
- reusable validator
- predictable result

---

### [실무]

기본 구조:

```javascript
function validateForm(values) {
  const errors = {};

  if (!values.email.trim()) {
    errors.email = "이메일을 입력해 주세요.";
  }

  if (!values.password) {
    errors.password = "비밀번호를 입력해 주세요.";
  }

  return errors;
}
```

TypeScript 예:

```typescript
type LoginFormValues = {
  email: string;
  password: string;
};

type LoginFormErrors = Partial<Record<keyof LoginFormValues, string>>;

function validateLogin(values: LoginFormValues): LoginFormErrors {
  const errors: LoginFormErrors = {};

  if (!values.email.trim()) {
    errors.email = "이메일을 입력해 주세요.";
  }

  if (!values.password) {
    errors.password = "비밀번호를 입력해 주세요.";
  }

  return errors;
}
```

권장:

- field name과 errors key 일치
- 유효하면 빈 객체 반환
- API 요청은 Validation Function 내부에서 수행하지 않음
- 중복 확인 같은 서버 검증은 별도 흐름으로 분리
- 복잡한 검증은 validator 파일로 분리

---

### [FAQ]

Q. Validation Function은 무엇을 반환해야 해?
A. field name을 key로 하는 errors 객체를 반환하는 것이 일반적이다.

Q. 검증 성공이면 무엇을 반환해?
A. 빈 객체 `{}`를 반환한다.

Q. Validation Function 안에서 API 호출해도 돼?
A. 권장하지 않는다. 순수 Client Validation과 Server Validation 흐름을 분리하는 것이 좋다.

Q. errors key는 무엇과 맞춰야 해?
A. Form Values key 또는 input name과 맞춰야 한다.

---

# 3. Required Validation Rules

## 3.1 Required Validation

### [개념]

Required Validation은 필수 입력값이 비어 있는지 확인하는 검증이다.

문자열 입력값은 보통 `trim()` 후 빈 문자열인지 확인한다.

---

### [핵심]

Required Validation 대상:

- email
- password
- title
- content
- nickname
- select required
- radio required
- checkbox agreement
- file required
- whitespace only
- empty string
- null
- undefined

---

### [실무]

문자열 필수값 검증:

```javascript
function validateTitle(title) {
  if (!title.trim()) {
    return "제목을 입력해 주세요.";
  }

  return "";
}
```

Form 검증 예:

```javascript
function validatePost(values) {
  const errors = {};

  if (!values.title.trim()) {
    errors.title = "제목을 입력해 주세요.";
  }

  if (!values.content.trim()) {
    errors.content = "내용을 입력해 주세요.";
  }

  if (!values.category) {
    errors.category = "카테고리를 선택해 주세요.";
  }

  return errors;
}
```

권장:

- 공백만 입력한 문자열은 invalid 처리
- select 빈 값 `""` 검증
- radio 미선택 검증
- checkbox 필수 동의 검증
- file 필수 여부 검증
- Backend `@NotBlank`, `@NotNull` 규칙과 일치

---

### [FAQ]

Q. Required Validation이 뭐야?
A. 필수 입력값이 비어 있는지 확인하는 검증이다.

Q. 공백만 입력해도 값이 있는 걸로 봐?
A. 대부분 trim 후 빈 문자열이면 입력하지 않은 것으로 처리한다.

Q. select 필수값은 어떻게 검증해?
A. value가 빈 문자열인지 확인한다.

Q. Required Validation은 Backend와 맞춰야 해?
A. 맞춰야 한다. Frontend 필수값 기준과 Backend DTO Validation 기준이 다르면 오류가 발생한다.

---

## 3.2 Checkbox Required Validation

### [개념]

Checkbox Required Validation은 필수 약관 동의, 개인정보 동의, 마케팅 선택 동의 여부를 검증하는 기준이다.

필수 checkbox는 `checked === true`인지 확인한다.

---

### [핵심]

Checkbox Required 기준:

- checked
- boolean true
- terms agreement
- privacy agreement
- required consent
- optional consent
- validation message
- server validation

---

### [실무]

약관 동의 검증:

```javascript
function validateAgreement(values) {
  const errors = {};

  if (!values.termsAgreed) {
    errors.termsAgreed = "필수 약관에 동의해 주세요.";
  }

  if (!values.privacyAgreed) {
    errors.privacyAgreed = "개인정보 처리방침에 동의해 주세요.";
  }

  return errors;
}
```

주의:

- 필수 동의와 선택 동의를 구분
- `value`가 아니라 `checked` 기준
- 필수 동의는 Backend에서도 검증
- 약관 버전 또는 동의 시각 저장은 Backend 책임
- 선택 동의는 제출 차단 조건이 아닐 수 있음

---

### [FAQ]

Q. 약관 동의 checkbox는 어떻게 검증해?
A. checked 값이 true인지 확인한다.

Q. 선택 동의도 필수 검증해야 해?
A. 아니다. 선택 동의는 서비스 정책에 따라 제출 차단 조건이 아닐 수 있다.

Q. checkbox required는 Frontend만 확인하면 돼?
A. 아니다. 중요한 동의는 Backend에서도 검증해야 한다.

Q. checkbox 검증에서 value를 확인해도 돼?
A. 보통 선택 여부는 checked로 확인해야 한다.

---

# 4. Length Validation Rules

## 4.1 Min Length Validation

### [개념]

Min Length Validation은 문자열 입력값이 최소 길이 기준을 만족하는지 확인하는 검증이다.

비밀번호, 닉네임, 제목, 리뷰 내용 등에 사용한다.

---

### [핵심]

Min Length 대상:

- password
- nickname
- username
- title
- content
- comment
- review
- trimmed length
- Backend DTO length

---

### [실무]

최소 길이 검증:

```javascript
function validateNickname(nickname) {
  const trimmedNickname = nickname.trim();

  if (trimmedNickname.length < 2) {
    return "닉네임은 2자 이상 입력해 주세요.";
  }

  return "";
}
```

비밀번호 검증:

```javascript
function validatePassword(password) {
  if (password.length < 8) {
    return "비밀번호는 8자 이상이어야 합니다.";
  }

  return "";
}
```

주의:

- trim 후 길이를 볼지 원본 길이를 볼지 결정
- password는 임의 trim하지 않음
- Backend `@Size(min = n)` 기준과 일치
- 다국어 글자 수 기준 주의
- emoji, 조합 문자 길이 처리 주의

---

### [FAQ]

Q. Min Length Validation이 뭐야?
A. 입력값이 최소 글자 수 이상인지 확인하는 검증이다.

Q. 닉네임 길이는 trim 후 검사해?
A. 보통 앞뒤 공백을 제거한 뒤 검사한다.

Q. 비밀번호도 trim 후 길이를 검사해?
A. 일반적으로 비밀번호는 사용자가 입력한 원본 기준으로 검사하고 임의 trim하지 않는다.

Q. Frontend minLength와 Backend Size 기준은 같아야 해?
A. 같아야 한다. 다르면 사용자는 통과했는데 서버에서 실패할 수 있다.

---

## 4.2 Max Length Validation

### [개념]

Max Length Validation은 문자열 입력값이 최대 길이를 초과하지 않는지 확인하는 검증이다.

DB 컬럼 길이, Backend DTO 제한, 화면 UX 기준과 연결된다.

---

### [핵심]

Max Length 대상:

- title
- content
- comment
- review
- nickname
- bio
- search keyword
- textarea
- DB column length
- DTO validation

---

### [실무]

최대 길이 검증:

```javascript
function validateTitle(title) {
  const trimmedTitle = title.trim();

  if (trimmedTitle.length > 50) {
    return "제목은 50자 이하로 입력해 주세요.";
  }

  return "";
}
```

textarea 글자 수 표시:

```jsx
<textarea
  value={values.content}
  maxLength={500}
  onChange={handleChange}
/>
<p>{values.content.length}/500</p>
```

권장:

- `maxLength` 속성으로 UX 보조
- Validation Function에서도 max length 검증
- Backend DTO와 DB column 길이 확인
- 초과 메시지는 명확히 표시
- textarea는 글자 수 표시 가능

---

### [FAQ]

Q. Max Length Validation이 뭐야?
A. 입력값이 최대 글자 수를 초과하지 않는지 확인하는 검증이다.

Q. maxLength 속성만 있으면 충분해?
A. 아니다. Frontend Validation과 Backend Validation도 필요하다.

Q. Backend 제한보다 Frontend 제한이 길면 어떻게 돼?
A. Frontend에서 통과해도 서버에서 실패할 수 있다.

Q. textarea 글자 수는 표시하는 게 좋아?
A. 긴 입력에서는 현재 길이와 최대 길이를 표시하면 UX에 좋다.

---

# 5. Format Validation Rules

## 5.1 Email Validation

### [개념]

Email Validation은 이메일 입력값이 기본적인 이메일 형식을 만족하는지 확인하는 검증이다.

Frontend에서는 과도하게 복잡한 정규식보다 실용적인 기본 형식 검증을 우선한다.

---

### [핵심]

Email Validation 요소:

- required
- trim
- includes @
- email regex
- format message
- duplicate check
- server validation
- normalization
- lowercase policy

---

### [실무]

기초 Email Validation:

```javascript
function validateEmail(email) {
  const trimmedEmail = email.trim();

  if (!trimmedEmail) {
    return "이메일을 입력해 주세요.";
  }

  if (!trimmedEmail.includes("@")) {
    return "이메일 형식이 올바르지 않습니다.";
  }

  return "";
}
```

간단한 정규식 예:

```javascript
const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

if (!emailPattern.test(trimmedEmail)) {
  errors.email = "이메일 형식이 올바르지 않습니다.";
}
```

주의:

- 완벽한 이메일 정규식 지양
- 중복 이메일 검사는 Server Validation 필요
- 이메일 소문자 변환 정책은 서비스 기준에 맞춤
- Backend email validation과 메시지 일치
- 로그인 실패는 Field Error보다 Global Error로 처리 가능

---

### [FAQ]

Q. 이메일 검증은 어떻게 해?
A. 빈 값 확인 후 기본 이메일 형식 또는 간단한 정규식으로 검증한다.

Q. 이메일 정규식은 완벽해야 해?
A. 아니다. 완벽한 정규식보다 기본 형식 확인과 Backend 검증을 함께 사용하는 것이 실용적이다.

Q. 이메일 중복 검사는 Frontend에서 할 수 있어?
A. 실제 중복 여부는 서버 데이터 기준이므로 Backend API 확인이 필요하다.

Q. 이메일을 lowercase로 바꿔도 돼?
A. 서비스 정책에 따라 가능하지만 Backend와 일치해야 한다.

---

## 5.2 Password Format Validation

### [개념]

Password Format Validation은 비밀번호가 서비스 보안 정책을 만족하는지 확인하는 검증이다.

Frontend는 사용자에게 빠른 피드백을 제공하고, Backend는 최종 보안 검증을 수행한다.

---

### [핵심]

Password Validation 대상:

- required
- min length
- max length
- uppercase
- lowercase
- number
- special character
- confirm password
- no console log
- backend policy match

---

### [실무]

기본 비밀번호 검증:

```javascript
function validatePassword(password) {
  if (!password) {
    return "비밀번호를 입력해 주세요.";
  }

  if (password.length < 8) {
    return "비밀번호는 8자 이상이어야 합니다.";
  }

  if (!/[0-9]/.test(password)) {
    return "비밀번호에는 숫자가 포함되어야 합니다.";
  }

  return "";
}
```

주의:

- password를 console.log로 출력 금지
- password 임의 trim 주의
- Backend 정책과 동일하게 검증
- 정책이 복잡하면 안내 문구 제공
- 보안상 너무 구체적인 실패 사유 노출 정책 검토
- confirmPassword는 Cross Field Validation에서 처리

---

### [FAQ]

Q. 비밀번호 검증은 어디 기준으로 맞춰?
A. Backend Validation 정책과 동일하게 맞춰야 한다.

Q. password를 trim해도 돼?
A. 임의 trim은 권장하지 않는다. 서비스 정책에 따라 명확히 결정해야 한다.

Q. password를 console.log로 확인해도 돼?
A. 안 된다. 민감정보는 로그에 남기지 않는 것이 원칙이다.

Q. 비밀번호 정책 메시지는 자세할수록 좋아?
A. 사용성에는 도움이 되지만 보안 정책에 따라 노출 수준을 조정해야 한다.

---

## 5.3 Phone and URL Validation

### [개념]

Phone and URL Validation은 전화번호, 웹사이트 주소, 외부 링크 입력값이 서비스에서 허용하는 형식인지 확인하는 검증이다.

국가, 서비스 정책, Backend 저장 방식에 따라 기준이 달라질 수 있다.

---

### [핵심]

검증 대상:

- phone
- mobile
- url
- website
- protocol
- format normalization
- country format
- optional field
- backend validation

---

### [실무]

전화번호 기초 검증:

```javascript
function validatePhone(phone) {
  const trimmedPhone = phone.trim();

  if (!trimmedPhone) {
    return "";
  }

  if (!/^[0-9-]+$/.test(trimmedPhone)) {
    return "전화번호 형식이 올바르지 않습니다.";
  }

  return "";
}
```

URL 기초 검증:

```javascript
function validateUrl(url) {
  const trimmedUrl = url.trim();

  if (!trimmedUrl) {
    return "";
  }

  try {
    new URL(trimmedUrl);
    return "";
  } catch {
    return "URL 형식이 올바르지 않습니다.";
  }
}
```

주의:

- optional field는 빈 값 허용 가능
- 전화번호는 국가별 포맷 기준 필요
- URL은 `http://` 또는 `https://` 정책 명확화
- 외부 링크는 XSS, open redirect 주의
- 최종 검증은 Backend에서 수행

---

### [FAQ]

Q. 전화번호 검증은 어떻게 해?
A. 서비스 국가와 저장 기준에 맞춰 숫자, 하이픈, 길이 등을 검증한다.

Q. URL 검증은 어떻게 해?
A. 기본적으로 URL 생성자나 정규식으로 형식을 확인하고 Backend에서도 검증한다.

Q. optional 전화번호가 비어 있으면 오류야?
A. 필수값이 아니라면 빈 값은 허용할 수 있다.

Q. URL에는 https만 허용해야 해?
A. 서비스 보안 정책에 따라 http/https 허용 여부를 결정해야 한다.

---

# 6. Number Validation Rules

## 6.1 Number Required and NaN Validation

### [개념]

Number Validation은 숫자 입력값이 숫자로 변환 가능한지, 필수값인지, 허용 범위에 있는지 확인하는 검증이다.

HTML number input의 value도 문자열로 들어올 수 있으므로 Number 변환과 NaN 검증이 필요하다.

---

### [핵심]

Number Validation 요소:

- number input
- string value
- Number conversion
- Number.isNaN
- required number
- empty string
- min
- max
- integer
- decimal
- range validation

---

### [실무]

숫자 필수값 검증:

```javascript
function validateAmount(value) {
  if (value === "") {
    return "금액을 입력해 주세요.";
  }

  const amount = Number(value);

  if (Number.isNaN(amount)) {
    return "숫자만 입력해 주세요.";
  }

  return "";
}
```

주의:

- `Number("")`는 0이 될 수 있으므로 빈 문자열 먼저 확인
- integer가 필요한 경우 `Number.isInteger()` 사용
- 소수 허용 여부 명확화
- min/max 속성은 UX용이며 Backend 검증 필요
- 금액, 수량, 평점은 범위 검증 필수

---

### [FAQ]

Q. number input 값은 숫자로 들어와?
A. 대부분 문자열로 들어오므로 Number 변환이 필요하다.

Q. Number("")는 왜 주의해야 해?
A. 0으로 변환될 수 있어 빈 값 검증을 우회할 수 있다.

Q. 숫자 검증에서 가장 먼저 볼 것은?
A. 빈 값 여부를 먼저 확인하고 그 다음 Number 변환과 NaN 검증을 한다.

Q. min/max 속성만 있으면 충분해?
A. 아니다. Backend에서도 범위 검증이 필요하다.

---

## 6.2 Number Range Validation

### [개념]

Number Range Validation은 숫자 입력값이 최소값과 최대값 사이에 있는지 확인하는 검증이다.

평점, 수량, 가격, 나이, 인원 수, 페이지 크기 등에 사용한다.

---

### [핵심]

Range Validation 대상:

- rating
- quantity
- price
- age
- count
- page size
- min value
- max value
- integer only
- positive number

---

### [실무]

평점 검증:

```javascript
function validateRating(value) {
  const rating = Number(value);

  if (Number.isNaN(rating) || rating < 1 || rating > 5) {
    return "평점은 1점에서 5점 사이여야 합니다.";
  }

  return "";
}
```

수량 검증:

```javascript
function validateQuantity(value) {
  const quantity = Number(value);

  if (!Number.isInteger(quantity) || quantity < 1) {
    return "수량은 1개 이상 정수로 입력해 주세요.";
  }

  return "";
}
```

권장:

- 숫자 변환 후 범위 검증
- 정수 여부 검증 필요 시 `Number.isInteger`
- 음수 허용 여부 명확화
- Backend DTO와 DB 제약 조건 확인
- 에러 메시지에 허용 범위 포함

---

### [FAQ]

Q. 숫자 범위 검증은 어떻게 해?
A. Number 변환 후 최소값과 최대값 조건을 확인한다.

Q. 정수만 허용하려면 어떻게 해?
A. Number.isInteger를 사용해 정수 여부를 확인한다.

Q. 평점 1~5 검증은 Frontend만 하면 돼?
A. 아니다. Backend에서도 동일한 범위 검증이 필요하다.

Q. 음수 입력은 어떻게 막아?
A. Frontend에서 min 속성과 validation을 적용하고 Backend에서도 음수 여부를 검증한다.

---

# 7. Date Validation Rules

## 7.1 Date Required and Format Validation

### [개념]

Date Validation은 날짜 입력값이 비어 있지 않고 서비스가 요구하는 날짜 형식에 맞는지 확인하는 검증이다.

날짜는 format, timezone, 문자열 비교 기준을 명확히 해야 한다.

---

### [핵심]

Date Validation 요소:

- date input
- ISO date
- yyyy-MM-dd
- Date object
- timezone caution
- required date
- invalid date
- date format
- Backend DTO format

---

### [실무]

기본 날짜 검증:

```javascript
function validateDate(value) {
  if (!value) {
    return "날짜를 선택해 주세요.";
  }

  const date = new Date(value);

  if (Number.isNaN(date.getTime())) {
    return "날짜 형식이 올바르지 않습니다.";
  }

  return "";
}
```

주의:

- HTML date input은 보통 `yyyy-MM-dd` 문자열 반환
- Backend LocalDate 형식과 일치 필요
- timezone 변환으로 하루 차이 발생 가능
- Date 객체 변환 없이 문자열 기준 처리 가능
- 날짜 표시용 format과 요청용 format 구분

---

### [FAQ]

Q. date input 값은 어떤 형식이야?
A. 보통 `yyyy-MM-dd` 형식의 문자열이다.

Q. 날짜 검증에서 timezone을 주의해야 해?
A. 그렇다. Date 객체 변환 시 timezone 때문에 날짜가 달라질 수 있다.

Q. Backend LocalDate와 어떻게 맞춰?
A. 보통 `yyyy-MM-dd` 문자열을 그대로 보내는 방식이 안전하다.

Q. 날짜 표시 형식과 요청 형식은 같아야 해?
A. 반드시 같을 필요는 없지만 Request DTO 형식은 Backend와 일치해야 한다.

---

## 7.2 Date Range Validation

### [개념]

Date Range Validation은 시작일과 종료일의 순서가 올바른지 확인하는 Cross Field Validation이다.

기간 검색, 예약, 이벤트 등록, 축제 기간 입력 등에 사용한다.

---

### [핵심]

Date Range 대상:

- startDate
- endDate
- start before end
- end after start
- optional range
- period search
- event date
- reservation date

---

### [실무]

날짜 범위 검증:

```javascript
function validateDateRange(values) {
  const errors = {};

  if (values.startDate && values.endDate && values.startDate > values.endDate) {
    errors.endDate = "종료일은 시작일 이후여야 합니다.";
  }

  return errors;
}
```

기간 검색 검증:

```javascript
function validateSearchPeriod(values) {
  const errors = {};

  if (values.startDate && values.endDate && values.startDate > values.endDate) {
    errors.endDate = "종료일은 시작일보다 빠를 수 없습니다.";
  }

  return errors;
}
```

주의:

- ISO 날짜 문자열은 문자열 비교가 가능할 수 있음
- format이 다르면 문자열 비교 금지
- 하나만 입력했을 때 허용 여부 결정
- 종료일 포함/제외 기준 명확화
- Backend에서도 날짜 순서 검증 필요

---

### [FAQ]

Q. 날짜 범위 검증은 어떻게 해?
A. startDate와 endDate를 비교해 종료일이 시작일보다 빠르지 않은지 확인한다.

Q. 날짜 문자열 비교를 해도 돼?
A. `yyyy-MM-dd` 같은 ISO 형식이면 가능할 수 있지만 format이 다르면 Date 변환 기준이 필요하다.

Q. 시작일만 입력해도 돼?
A. 서비스 정책에 따라 허용할 수 있다. 검색 Form에서는 보통 허용 가능하다.

Q. 날짜 범위 검증은 Backend도 해야 해?
A. 해야 한다. Frontend 검증은 우회될 수 있다.

---

# 8. Cross Field Validation Rules

## 8.1 Cross Field Validation Definition

### [개념]

Cross Field Validation은 하나의 Field만으로 판단할 수 없고 여러 Field 값을 함께 비교해야 하는 검증이다.

회원가입, 기간 검색, 가격 범위, 비밀번호 확인, 조건부 필수값에 사용한다.

---

### [핵심]

Cross Field Validation 대상:

- password confirm
- startDate / endDate
- minPrice / maxPrice
- minAge / maxAge
- conditional required
- dependent select
- agreement group
- related fields

---

### [실무]

기본 Flow:

```text
Read Related Fields
→ Check Empty Cases
→ Compare Values
→ Assign Error to Target Field
→ Return Errors
```

에러 위치 기준:

```text
password !== confirmPassword
→ errors.confirmPassword

startDate > endDate
→ errors.endDate

minPrice > maxPrice
→ errors.maxPrice
```

권장:

- 관련 Field 중 하나가 비어 있을 때 처리 기준 명확화
- 에러를 어느 field에 표시할지 결정
- submit 시 전체 Cross Field Validation 수행
- 입력 중 실시간 검증은 UX 고려
- Backend에서도 동일 검증 수행

---

### [FAQ]

Q. Cross Field Validation이 뭐야?
A. 여러 입력값을 함께 비교해 검증하는 방식이다.

Q. Cross Field Error는 어디에 표시해?
A. 사용자가 수정해야 할 가능성이 큰 field 근처에 표시한다.

Q. Cross Field Validation은 언제 실행해?
A. 보통 submit 시 실행하고 필요한 경우 관련 field 변경 시 실행한다.

Q. Cross Field Validation도 Backend에서 해야 해?
A. 해야 한다. Frontend 검증은 우회될 수 있다.

---

## 8.2 Password Confirm Validation

### [개념]

Password Confirm Validation은 비밀번호와 비밀번호 확인 값이 일치하는지 검증하는 Cross Field Validation이다.

회원가입, 비밀번호 변경 Form에서 사용한다.

---

### [핵심]

Password Confirm 요소:

- password
- confirmPassword
- equality check
- confirm field error
- signup form
- password change form
- no password logging
- backend validation

---

### [실무]

비밀번호 확인 검증:

```javascript
function validateSignup(values) {
  const errors = {};

  if (!values.password) {
    errors.password = "비밀번호를 입력해 주세요.";
  }

  if (!values.confirmPassword) {
    errors.confirmPassword = "비밀번호 확인을 입력해 주세요.";
  }

  if (
    values.password &&
    values.confirmPassword &&
    values.password !== values.confirmPassword
  ) {
    errors.confirmPassword = "비밀번호가 일치하지 않습니다.";
  }

  return errors;
}
```

주의:

- confirmPassword 필드 근처에 에러 표시
- password를 console.log로 출력 금지
- password policy validation과 confirm validation 분리 가능
- 비밀번호 변경 시 현재 비밀번호 검증은 Server Validation
- Backend에서도 비밀번호 확인 또는 정책 검증 필요

---

### [FAQ]

Q. 비밀번호 확인 검증은 어떻게 해?
A. password와 confirmPassword 값이 같은지 비교한다.

Q. 비밀번호 불일치 에러는 어디에 표시해?
A. 보통 confirmPassword 필드 근처에 표시한다.

Q. password가 비어 있어도 불일치 메시지를 보여줘?
A. 보통 필수값 메시지를 먼저 보여주고 둘 다 값이 있을 때 불일치 검증을 한다.

Q. 비밀번호 확인도 Backend에서 해야 해?
A. 요청 구조와 정책에 따라 Backend에서도 검증하는 것이 안전하다.

---

## 8.3 Min Max Range Validation

### [개념]

Min Max Range Validation은 최소값과 최대값의 관계가 올바른지 확인하는 Cross Field Validation이다.

가격 범위, 나이 범위, 인원 수 범위, 날짜 범위에 사용한다.

---

### [핵심]

Min Max Range 대상:

- minPrice
- maxPrice
- minAge
- maxAge
- minCount
- maxCount
- numeric range
- search filter
- range condition

---

### [실무]

가격 범위 검증:

```javascript
function validatePriceRange(values) {
  const errors = {};

  const minPrice = values.minPrice === "" ? null : Number(values.minPrice);
  const maxPrice = values.maxPrice === "" ? null : Number(values.maxPrice);

  if (minPrice !== null && Number.isNaN(minPrice)) {
    errors.minPrice = "최소 가격은 숫자여야 합니다.";
  }

  if (maxPrice !== null && Number.isNaN(maxPrice)) {
    errors.maxPrice = "최대 가격은 숫자여야 합니다.";
  }

  if (
    minPrice !== null &&
    maxPrice !== null &&
    !Number.isNaN(minPrice) &&
    !Number.isNaN(maxPrice) &&
    minPrice > maxPrice
  ) {
    errors.maxPrice = "최대 가격은 최소 가격보다 커야 합니다.";
  }

  return errors;
}
```

주의:

- 빈 값 허용 여부 결정
- 숫자 변환과 NaN 검증 먼저 수행
- min > max 오류는 보통 max field에 표시
- 검색 필터에서는 한쪽 값만 허용 가능
- Backend에서도 range validation 필요

---

### [FAQ]

Q. 최소값과 최대값 검증은 어떻게 해?
A. 숫자로 변환한 뒤 최소값이 최대값보다 큰지 확인한다.

Q. 한쪽 값만 입력해도 돼?
A. 검색 필터에서는 허용할 수 있고, 등록 Form에서는 정책에 따라 다르다.

Q. min > max 에러는 어디에 표시해?
A. 보통 max field 근처에 표시한다.

Q. 숫자 범위 검증 전에 무엇을 해야 해?
A. 빈 값 처리와 NaN 검증을 먼저 해야 한다.

---

# 9. File Validation Rules

## 9.1 File Size Validation

### [개념]

File Size Validation은 사용자가 선택한 파일이 허용된 용량 이하인지 확인하는 검증이다.

Frontend 파일 크기 검증은 UX를 위한 사전 검증이며, Backend 검증이 반드시 필요하다.

---

### [핵심]

File Size Validation 요소:

- file.size
- byte
- KB
- MB
- max file size
- total upload size
- single file
- multiple file
- backend validation

---

### [실무]

단일 파일 크기 검증:

```javascript
const MAX_IMAGE_SIZE = 5 * 1024 * 1024;

function validateImageFile(file) {
  if (file.size > MAX_IMAGE_SIZE) {
    return "이미지는 5MB 이하만 업로드할 수 있습니다.";
  }

  return "";
}
```

여러 파일 총 용량 검증:

```javascript
function validateTotalFileSize(files) {
  const totalSize = files.reduce((sum, file) => sum + file.size, 0);

  if (totalSize > 20 * 1024 * 1024) {
    return "전체 파일 용량은 20MB 이하만 업로드할 수 있습니다.";
  }

  return "";
}
```

권장:

- 단일 파일 크기 제한
- 전체 파일 크기 제한
- 사용자에게 허용 용량 표시
- 업로드 전 사전 차단
- Backend에서도 동일 또는 더 엄격한 제한 적용

---

### [FAQ]

Q. 파일 크기 검증은 어떻게 해?
A. File 객체의 size 값을 기준으로 허용 용량과 비교한다.

Q. file.size 단위는 뭐야?
A. byte 단위다.

Q. 여러 파일은 총 용량도 검증해야 해?
A. 권장한다. 개별 파일과 전체 용량 제한을 함께 검토한다.

Q. Frontend 파일 크기 검증만 있으면 돼?
A. 아니다. Backend에서도 반드시 검증해야 한다.

---

## 9.2 File Type Validation

### [개념]

File Type Validation은 사용자가 선택한 파일의 MIME type 또는 확장자가 허용된 형식인지 확인하는 검증이다.

`accept` 속성은 UX 보조일 뿐 보안 검증이 아니다.

---

### [핵심]

File Type Validation 요소:

- file.type
- MIME type
- extension
- accept
- image/png
- image/jpeg
- allowed types
- upload security
- backend validation

---

### [실무]

이미지 타입 검증:

```javascript
const ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png", "image/webp"];

function validateImageType(file) {
  if (!ALLOWED_IMAGE_TYPES.includes(file.type)) {
    return "jpg, png, webp 이미지만 업로드할 수 있습니다.";
  }

  return "";
}
```

input accept:

```jsx
<input
  type="file"
  accept="image/jpeg,image/png,image/webp"
  onChange={handleFileChange}
/>
```

주의:

- accept는 파일 선택 UI 제한에 가깝다
- file.type은 비어 있거나 조작 가능성이 있음
- Backend MIME sniffing 또는 확장자 검증 필요
- 실행 파일 업로드 금지
- 이미지 업로드도 Backend 보안 검증 필요

---

### [FAQ]

Q. 파일 타입 검증은 어떻게 해?
A. File 객체의 type 값을 허용된 MIME type 목록과 비교한다.

Q. accept 속성만 있으면 충분해?
A. 아니다. accept는 UX 보조이며 Backend 검증이 필요하다.

Q. file.type을 완전히 신뢰해도 돼?
A. 아니다. Backend에서 추가 검증해야 한다.

Q. 이미지 업로드도 보안 검증이 필요해?
A. 필요하다. 파일은 항상 신뢰하지 않고 서버에서 검증해야 한다.

---

# 10. Validation Timing Rules

## 10.1 Submit Validation

### [개념]

Submit Validation은 사용자가 Form을 제출할 때 전체 입력값을 검증하는 방식이다.

가장 기본적이고 안정적인 Validation Timing이다.

---

### [핵심]

Submit Validation 요소:

- onSubmit
- preventDefault
- validate all fields
- setErrors
- stop if invalid
- request only if valid
- show all errors
- submitted state

---

### [실무]

Submit Validation 예:

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

권장:

- 제출 시 전체 Form 검증
- 검증 실패 시 API 요청 중단
- submit 후 모든 field error 표시
- 이전 에러 초기화 후 새 에러 반영
- 첫 번째 invalid field focus 이동 고려

---

### [FAQ]

Q. Submit Validation이 뭐야?
A. Form 제출 시 전체 입력값을 한 번에 검증하는 방식이다.

Q. 검증 실패 시 API 요청을 보내?
A. 아니다. Client Validation 실패 시 요청을 중단한다.

Q. Submit Validation은 모든 Form에 필요해?
A. 대부분 필요하다. 다른 timing을 쓰더라도 최종 제출 전 전체 검증은 권장된다.

Q. submit 후 모든 에러를 보여줘도 돼?
A. 가능하다. 사용자가 수정할 항목을 명확히 알 수 있다.

---

## 10.2 onBlur Validation

### [개념]

onBlur Validation은 사용자가 Field 입력을 마치고 focus를 벗어났을 때 해당 Field를 검증하는 방식이다.

필드별 피드백을 제공하면서 onChange 검증보다 덜 공격적인 UX를 제공한다.

---

### [핵심]

onBlur Validation 요소:

- onBlur
- touched
- field validation
- format check
- duplicate check trigger
- error display after blur
- UX friendly validation

---

### [실무]

onBlur Validation 예:

```javascript
function handleEmailBlur(event) {
  const email = event.target.value;
  const message = validateEmail(email);

  setTouched((prevTouched) => ({
    ...prevTouched,
    email: true,
  }));

  setErrors((prevErrors) => ({
    ...prevErrors,
    email: message,
  }));
}
```

권장:

- email, nickname, URL 같은 format 검증에 적합
- touched와 함께 사용
- API 중복 확인은 debounce 또는 명시 버튼과 비교 검토
- onBlur 검증이 있어도 submit 검증은 유지
- 사용자가 입력 중일 때 과도한 에러 표시 방지

---

### [FAQ]

Q. onBlur Validation은 언제 좋아?
A. 사용자가 입력을 마친 뒤 피드백을 주고 싶을 때 적합하다.

Q. onBlur Validation만 있으면 submit validation은 없어도 돼?
A. 아니다. 최종 제출 전 전체 검증은 권장된다.

Q. 이메일 형식 검증은 onBlur에서 해도 돼?
A. 가능하다. 입력 중 과도한 에러 표시를 줄일 수 있다.

Q. 중복 검사를 onBlur에서 해도 돼?
A. 가능하지만 API 호출 빈도와 UX를 고려해야 한다.

---

## 10.3 onChange Validation

### [개념]

onChange Validation은 사용자가 입력할 때마다 즉시 검증하는 방식이다.

실시간 피드백이 필요한 경우 유용하지만, 과도하면 사용자 경험을 해칠 수 있다.

---

### [핵심]

onChange Validation 요소:

- real-time validation
- instant feedback
- password strength
- character count
- expensive validation caution
- debounce
- aggressive UX caution

---

### [실무]

간단한 onChange Validation:

```javascript
function handleChange(event) {
  const { name, value } = event.target;

  setValues((prevValues) => ({
    ...prevValues,
    [name]: value,
  }));

  if (name === "email") {
    setErrors((prevErrors) => ({
      ...prevErrors,
      email: validateEmail(value),
    }));
  }
}
```

권장 사용:

- 비밀번호 강도 표시
- 글자 수 표시
- 숫자 범위 힌트
- 검색어 실시간 필터
- debounce 가능한 검증

주의:

- 입력 첫 글자부터 에러 표시하면 UX가 나쁠 수 있음
- API 호출 검증은 debounce 필요
- 비싼 검증 로직은 onChange마다 실행 금지
- touched 또는 submitted 조건과 함께 표시

---

### [FAQ]

Q. onChange Validation은 언제 사용해?
A. 실시간 피드백이 필요한 비밀번호 강도, 글자 수, 간단한 형식 힌트에 사용할 수 있다.

Q. 모든 검증을 onChange로 해도 돼?
A. 권장하지 않는다. 사용자 경험이 공격적으로 느껴질 수 있다.

Q. onChange에서 API 검증을 호출해도 돼?
A. 가능하지만 debounce나 명시적 확인 버튼을 고려해야 한다.

Q. onChange Validation에도 submit validation이 필요해?
A. 필요하다. 최종 제출 전 전체 검증은 유지하는 것이 안전하다.

---

# 11. Error Message Rules

## 11.1 Field Error Message

### [개념]

Field Error Message는 특정 Field의 검증 실패 이유를 사용자에게 알려주는 문구다.

명확하고 짧으며 수정 방법을 알 수 있어야 한다.

---

### [핵심]

Field Error Message 기준:

- specific
- short
- actionable
- near input
- field name
- validation reason
- no internal detail
- accessible message
- role alert

---

### [실무]

좋은 메시지:

```text
이메일을 입력해 주세요.
이메일 형식이 올바르지 않습니다.
비밀번호는 8자 이상이어야 합니다.
제목은 50자 이하로 입력해 주세요.
평점은 1점에서 5점 사이여야 합니다.
```

나쁜 메시지:

```text
Invalid input
Error
Bad Request
Validation failed
ConstraintViolationException
```

출력 예:

```jsx
{
  errors.email && (
    <p id="email-error" role="alert">
      {errors.email}
    </p>
  );
}
```

권장:

- input 근처에 표시
- 사용자가 무엇을 고쳐야 하는지 명확히 작성
- Backend 내부 에러명 노출 금지
- aria-describedby로 input과 연결
- 메시지 톤과 용어 통일

---

### [FAQ]

Q. Field Error Message는 어떻게 작성해?
A. 짧고 구체적으로 사용자가 무엇을 수정해야 하는지 알려줘야 한다.

Q. “Invalid input” 같은 메시지는 괜찮아?
A. 권장하지 않는다. 사용자가 무엇을 고쳐야 하는지 알기 어렵다.

Q. Backend 예외명을 그대로 보여줘도 돼?
A. 안 된다. 내부 정보가 노출될 수 있다.

Q. Field Error는 어디에 표시해?
A. 해당 input 근처에 표시한다.

---

## 11.2 Global Error Message

### [개념]

Global Error Message는 Form 전체 실패를 설명하는 메시지다.

로그인 실패, 서버 장애, 네트워크 오류, 권한 오류처럼 특정 Field 하나에 연결하기 어려운 상황에 사용한다.

---

### [핵심]

Global Error Message 대상:

- login failure
- authentication failure
- authorization failure
- network error
- server error
- submit failure
- unknown error
- global validation

---

### [실무]

Global Error 예:

```javascript
setSubmitError("요청을 처리하지 못했습니다. 잠시 후 다시 시도해 주세요.");
```

출력 예:

```jsx
{
  submitError && (
    <p role="alert" className="form-global-error">
      {submitError}
    </p>
  );
}
```

권장:

- Form 상단 또는 submit button 근처에 표시
- 재시도 가능 여부 안내
- 내부 서버 오류 상세 노출 금지
- 로그인 실패는 과도하게 구체적인 원인 노출 주의
- submit 재시도 시 이전 global error 초기화

---

### [FAQ]

Q. Global Error Message는 언제 사용해?
A. 특정 field가 아니라 Form 전체 실패를 나타낼 때 사용한다.

Q. 로그인 실패 메시지는 어디에 표시해?
A. 보통 Form 상단의 Global Error로 표시한다.

Q. 서버 오류 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 정보가 포함될 수 있으므로 사용자 친화 메시지로 변환한다.

Q. Global Error도 role alert를 써도 돼?
A. 가능하다. 중요한 오류를 보조기술에 알릴 수 있다.

---

# 12. Validation Accessibility Rules

## 12.1 Accessible Validation Error

### [개념]

Accessible Validation Error는 스크린 리더와 키보드 사용자가 Form 오류를 이해하고 수정할 수 있도록 만드는 기준이다.

Validation Error는 시각적으로만 표시해서는 안 된다.

---

### [핵심]

접근성 요소:

- aria-invalid
- aria-describedby
- role alert
- error id
- label connection
- focus management
- first invalid field
- required indication
- fieldset
- legend

---

### [실무]

접근성 있는 Field Error:

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

- 모든 input에 label 연결
- 에러 메시지에 id 부여
- input의 aria-describedby와 error id 연결
- invalid 상태는 aria-invalid로 표시
- submit 실패 시 첫 번째 invalid field focus 이동 고려
- 색상만으로 오류 표시 금지

---

### [FAQ]

Q. Validation Error도 접근성이 필요해?
A. 필요하다. 오류를 시각적으로만 표시하면 스크린 리더 사용자가 이해하기 어렵다.

Q. aria-invalid는 언제 써?
A. 해당 field에 오류가 있을 때 true로 설정한다.

Q. aria-describedby는 왜 필요해?
A. input과 error message를 연결해 오류 내용을 보조기술이 읽을 수 있게 한다.

Q. 에러를 색상만으로 표시해도 돼?
A. 안 된다. 텍스트 메시지와 접근성 속성을 함께 제공해야 한다.

---

## 12.2 Focus on Invalid Field

### [개념]

Focus on Invalid Field는 submit 실패 시 사용자가 가장 먼저 수정해야 할 Field로 focus를 이동시키는 UX / Accessibility 패턴이다.

긴 Form이나 회원가입 Form에서 유용하다.

---

### [핵심]

Focus 처리 대상:

- submit failed
- first invalid field
- focus management
- ref
- error summary
- keyboard user
- long form
- modal form

---

### [실무]

기본 Flow:

```text
Submit
→ Validate Form
→ Errors Exist
→ Find First Error Field
→ Focus First Invalid Input
→ Show Error Message
```

구현 기준:

```javascript
const firstErrorField = Object.keys(nextErrors)[0];

if (firstErrorField === "email") {
  emailRef.current?.focus();
}
```

주의:

- focus 이동 남용 금지
- 사용자가 입력 중인 focus를 불필요하게 빼앗지 않음
- submit 실패 시에만 적용하는 것이 일반적
- Custom Component는 ref forwarding 필요 가능
- Error Summary와 함께 사용할 수 있음

---

### [FAQ]

Q. submit 실패 시 focus를 이동해야 해?
A. 필수는 아니지만 긴 Form에서는 첫 오류 field로 이동하면 수정이 쉬워진다.

Q. focus 이동은 언제 하는 게 좋아?
A. submit validation 실패 후 첫 번째 invalid field로 이동하는 방식이 일반적이다.

Q. onChange마다 focus를 이동해도 돼?
A. 권장하지 않는다. 사용자의 입력 흐름을 방해할 수 있다.

Q. Custom Field에서 focus 이동이 안 되면?
A. ref forwarding이 필요할 수 있다.

---

# 13. Validation and Request Mapping

## 13.1 Validate Before Request Mapping

### [개념]

Validate Before Request Mapping은 API Request Body를 만들기 전에 Form Values가 유효한지 확인하는 기준이다.

잘못된 입력값을 Request Body로 변환하기 전에 차단하면 예외와 잘못된 요청을 줄일 수 있다.

---

### [핵심]

흐름 기준:

- validate values
- stop if invalid
- build request body
- type conversion
- trim
- null mapping
- API request
- server validation

---

### [실무]

Submit Flow:

```javascript
function handleSubmit(event) {
  event.preventDefault();

  const nextErrors = validateForm(values);
  setErrors(nextErrors);

  if (Object.keys(nextErrors).length > 0) {
    return;
  }

  const requestBody = toCreateReviewRequest(values);

  createReview(requestBody);
}
```

Request Mapping:

```javascript
function toCreateReviewRequest(values) {
  return {
    rating: Number(values.rating),
    content: values.content.trim(),
  };
}
```

권장:

- Client Validation 통과 후 Request Body 생성
- 숫자 변환 전 NaN 검증
- trim 기준을 validator와 mapper에서 일치
- optional field null/omit 기준 명확화
- Backend DTO 필드명과 일치

---

### [FAQ]

Q. Validation과 Request Mapping 중 무엇이 먼저야?
A. 보통 Validation을 먼저 수행하고 통과하면 Request Body를 생성한다.

Q. Request Body 생성 중 Number 변환 오류가 나면?
A. Validation에서 먼저 NaN과 빈 값을 검증해야 한다.

Q. trim은 Validation과 Mapping 양쪽에서 해야 해?
A. 기준이 일치해야 한다. 보통 검증에도 trim 기준을 쓰고 요청에도 trim된 값을 보낸다.

Q. Form Values를 그대로 API에 보내도 돼?
A. 간단한 경우 가능하지만 타입 변환과 trim이 필요하면 mapper를 사용하는 것이 좋다.

---

# 14. Validation Troubleshooting

## 14.1 Validation Error Not Showing

### [개념]

Validation Error Not Showing은 검증 실패는 발생했지만 사용자에게 에러 메시지가 표시되지 않는 문제다.

대부분 errors key, rendering 조건, touched/submitted 조건, server error mapping 불일치가 원인이다.

---

### [핵심]

주요 원인:

- setErrors 누락
- errors key 불일치
- input name 불일치
- conditional rendering 오류
- touched 조건 때문에 숨김
- submitted 상태 미사용
- server error mapping 실패
- error message 빈 문자열
- role / aria 연결 누락

---

### [실무]

Debug Flow:

```text
Validation Function Result 확인
→ setErrors 호출 확인
→ errors key 확인
→ input name 확인
→ Error Rendering 조건 확인
→ touched/submitted 조건 확인
→ Server Error Mapping 확인
```

문제 예:

```javascript
errors.userEmail = "이메일을 입력해 주세요.";
```

```jsx
{
  errors.email && <p>{errors.email}</p>;
}
```

`errors.userEmail`과 `errors.email` key가 달라 메시지가 표시되지 않는다.

---

### [FAQ]

Q. Validation은 실패했는데 메시지가 안 보여?
A. errors key와 input field name, error rendering 조건을 확인해야 한다.

Q. touched 조건 때문에 에러가 안 보일 수 있어?
A. 가능하다. submit 후에는 submitted 상태로 전체 에러를 표시할 수 있다.

Q. errors 객체에 메시지가 있는데 화면에 안 나와?
A. rendering 조건이나 key 이름이 맞는지 확인해야 한다.

Q. 서버 에러가 Form에 안 붙어?
A. 서버 응답의 errors 구조와 Frontend mapping 함수가 일치하는지 확인해야 한다.

---

## 14.2 Validation Always Fails

### [개념]

Validation Always Fails는 입력값이 정상인데도 Validation이 계속 실패하는 문제다.

타입 변환 오류, trim 기준 오류, name-key 불일치, 초기값 문제, 비교 대상 오류가 원인일 수 있다.

---

### [핵심]

주요 원인:

- number string comparison
- Number("") issue
- stale state
- wrong field name
- trim policy mismatch
- undefined initial value
- date format mismatch
- select option mismatch
- password confirm mismatch

---

### [실무]

Debug Flow:

```text
Check values object
→ Check field name
→ Check value type
→ Check trim result
→ Check Number conversion
→ Check date format
→ Check comparison target
→ Check validation return
```

숫자 검증 문제 예:

```javascript
const amount = Number(values.amount);

if (amount < 1) {
  errors.amount = "금액을 입력해 주세요.";
}
```

`values.amount === ""`이면 `Number("")`가 0이 되어 의도와 다르게 처리될 수 있다.

수정:

```javascript
if (values.amount === "") {
  errors.amount = "금액을 입력해 주세요.";
} else if (Number(values.amount) < 1) {
  errors.amount = "금액은 1 이상이어야 합니다.";
}
```

---

### [FAQ]

Q. 정상 입력인데 Validation이 계속 실패하는 이유는?
A. 값 타입, name-key 불일치, Number 변환, trim 결과, 비교 기준을 확인해야 한다.

Q. 숫자 입력 검증이 이상하면 무엇을 확인해?
A. 빈 문자열 처리와 Number 변환 결과를 먼저 확인한다.

Q. password confirm이 계속 실패하면?
A. password와 confirmPassword 값, 공백 처리, field name을 확인한다.

Q. select validation이 계속 실패하면?
A. select value와 option value가 일치하는지 확인한다.

---

# 15. Validation Checklist

## 15.1 Implementation Checklist

### [개념]

Validation Checklist는 Form Validation이 Client UX, Backend Contract, Error UI, Accessibility 기준을 만족하는지 검수하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] Client Validation과 Server Validation 역할이 분리되었는가?
- [ ] Required Validation이 필요한 field에 적용되었는가?
- [ ] 문자열 필수값은 trim 기준을 검토했는가?
- [ ] password는 임의 trim하지 않는가?
- [ ] Length Validation이 Backend DTO와 일치하는가?
- [ ] Email Format Validation이 적용되었는가?
- [ ] Password Policy가 Backend와 일치하는가?
- [ ] Number input은 빈 문자열과 NaN을 구분하는가?
- [ ] Number Range Validation이 적용되었는가?
- [ ] Date Format과 Backend DTO 형식이 일치하는가?
- [ ] Date Range Validation이 필요한 경우 적용되었는가?
- [ ] Cross Field Validation이 필요한 field를 확인했는가?
- [ ] Checkbox Required Validation이 checked 기준으로 처리되는가?
- [ ] File Size Validation이 적용되었는가?
- [ ] File Type Validation이 적용되었는가?
- [ ] File Validation은 Backend에서도 수행되는가?
- [ ] Validation Function이 errors 객체를 반환하는가?
- [ ] errors key와 input name이 일치하는가?
- [ ] Field Error와 Global Error가 구분되었는가?
- [ ] Error Message가 짧고 수정 가능하게 작성되었는가?
- [ ] Backend 내부 오류 메시지를 노출하지 않는가?
- [ ] aria-invalid와 aria-describedby가 적용되었는가?
- [ ] submit 실패 시 API 요청을 중단하는가?
- [ ] Validation 통과 후 Request Body Mapping을 수행하는가?
```

---

### [실무]

검수 Flow:

```text
Required Check
→ Length Check
→ Format Check
→ Number Check
→ Date Check
→ Cross Field Check
→ File Check
→ Error Message Check
→ Accessibility Check
→ Backend Contract Check
→ Troubleshooting Review
```

---

### [FAQ]

Q. Validation 검수에서 가장 중요한 것은?
A. Client Validation과 Server Validation 분리, Backend DTO 규칙 일치, Error Message 표시, 접근성 적용이다.

Q. Validation 다음에는 무엇을 검토해?
A. Server Validation Error Handling, Submit Flow, Request Body Mapping, React Hook Form 적용 기준을 검토한다.

---

# Retrieval Queries

### [FAQ]

Q. Validation이 뭐야?
A. Form 입력값이 서비스 규칙과 Backend DTO 규칙에 맞는지 확인하는 과정이다.

Q. Frontend Validation만 있으면 충분해?
A. 아니다. Frontend Validation은 우회될 수 있으므로 Backend Validation이 반드시 필요하다.

Q. Validation에서 가장 중요한 기준은 뭐야?
A. Client Validation은 UX용, Server Validation은 최종 검증이라는 역할 분리다.

Q. Validation 결과는 어디에 저장해?
A. 보통 errors 객체와 submitError 같은 Error State에 저장한다.

Q. Client Validation이 뭐야?
A. 사용자가 Form을 제출하기 전에 Frontend에서 입력값을 검증하는 UX용 검증이다.

Q. Client Validation은 왜 필요해?
A. 사용자가 잘못된 입력을 빠르게 수정할 수 있도록 돕기 위해 필요하다.

Q. Client Validation이 있으면 Server Validation은 없어도 돼?
A. 안 된다. Client Validation은 우회 가능하므로 Backend 검증이 반드시 필요하다.

Q. Validation Function은 무엇을 반환해야 해?
A. field name을 key로 하는 errors 객체를 반환하는 것이 일반적이다.

Q. 검증 성공이면 무엇을 반환해?
A. 빈 객체 `{}`를 반환한다.

Q. Validation Function 안에서 API 호출해도 돼?
A. 권장하지 않는다. 순수 Client Validation과 Server Validation 흐름을 분리하는 것이 좋다.

Q. errors key는 무엇과 맞춰야 해?
A. Form Values key 또는 input name과 맞춰야 한다.

Q. Required Validation이 뭐야?
A. 필수 입력값이 비어 있는지 확인하는 검증이다.

Q. 공백만 입력해도 값이 있는 걸로 봐?
A. 대부분 trim 후 빈 문자열이면 입력하지 않은 것으로 처리한다.

Q. select 필수값은 어떻게 검증해?
A. value가 빈 문자열인지 확인한다.

Q. Required Validation은 Backend와 맞춰야 해?
A. 맞춰야 한다. Frontend 필수값 기준과 Backend DTO Validation 기준이 다르면 오류가 발생한다.

Q. 약관 동의 checkbox는 어떻게 검증해?
A. checked 값이 true인지 확인한다.

Q. 선택 동의도 필수 검증해야 해?
A. 아니다. 선택 동의는 서비스 정책에 따라 제출 차단 조건이 아닐 수 있다.

Q. checkbox required는 Frontend만 확인하면 돼?
A. 아니다. 중요한 동의는 Backend에서도 검증해야 한다.

Q. Min Length Validation이 뭐야?
A. 입력값이 최소 글자 수 이상인지 확인하는 검증이다.

Q. 닉네임 길이는 trim 후 검사해?
A. 보통 앞뒤 공백을 제거한 뒤 검사한다.

Q. 비밀번호도 trim 후 길이를 검사해?
A. 일반적으로 비밀번호는 사용자가 입력한 원본 기준으로 검사하고 임의 trim하지 않는다.

Q. Frontend minLength와 Backend Size 기준은 같아야 해?
A. 같아야 한다. 다르면 사용자는 통과했는데 서버에서 실패할 수 있다.

Q. Max Length Validation이 뭐야?
A. 입력값이 최대 글자 수를 초과하지 않는지 확인하는 검증이다.

Q. maxLength 속성만 있으면 충분해?
A. 아니다. Frontend Validation과 Backend Validation도 필요하다.

Q. Backend 제한보다 Frontend 제한이 길면 어떻게 돼?
A. Frontend에서 통과해도 서버에서 실패할 수 있다.

Q. textarea 글자 수는 표시하는 게 좋아?
A. 긴 입력에서는 현재 길이와 최대 길이를 표시하면 UX에 좋다.

Q. 이메일 검증은 어떻게 해?
A. 빈 값 확인 후 기본 이메일 형식 또는 간단한 정규식으로 검증한다.

Q. 이메일 정규식은 완벽해야 해?
A. 아니다. 완벽한 정규식보다 기본 형식 확인과 Backend 검증을 함께 사용하는 것이 실용적이다.

Q. 이메일 중복 검사는 Frontend에서 할 수 있어?
A. 실제 중복 여부는 서버 데이터 기준이므로 Backend API 확인이 필요하다.

Q. 비밀번호 검증은 어디 기준으로 맞춰?
A. Backend Validation 정책과 동일하게 맞춰야 한다.

Q. password를 trim해도 돼?
A. 임의 trim은 권장하지 않는다. 서비스 정책에 따라 명확히 결정해야 한다.

Q. password를 console.log로 확인해도 돼?
A. 안 된다. 민감정보는 로그에 남기지 않는 것이 원칙이다.

Q. 전화번호 검증은 어떻게 해?
A. 서비스 국가와 저장 기준에 맞춰 숫자, 하이픈, 길이 등을 검증한다.

Q. URL 검증은 어떻게 해?
A. 기본적으로 URL 생성자나 정규식으로 형식을 확인하고 Backend에서도 검증한다.

Q. optional 전화번호가 비어 있으면 오류야?
A. 필수값이 아니라면 빈 값은 허용할 수 있다.

Q. number input 값은 숫자로 들어와?
A. 대부분 문자열로 들어오므로 Number 변환이 필요하다.

Q. Number("")는 왜 주의해야 해?
A. 0으로 변환될 수 있어 빈 값 검증을 우회할 수 있다.

Q. 숫자 검증에서 가장 먼저 볼 것은?
A. 빈 값 여부를 먼저 확인하고 그 다음 Number 변환과 NaN 검증을 한다.

Q. 숫자 범위 검증은 어떻게 해?
A. Number 변환 후 최소값과 최대값 조건을 확인한다.

Q. 정수만 허용하려면 어떻게 해?
A. Number.isInteger를 사용해 정수 여부를 확인한다.

Q. 평점 1~5 검증은 Frontend만 하면 돼?
A. 아니다. Backend에서도 동일한 범위 검증이 필요하다.

Q. date input 값은 어떤 형식이야?
A. 보통 `yyyy-MM-dd` 형식의 문자열이다.

Q. 날짜 검증에서 timezone을 주의해야 해?
A. 그렇다. Date 객체 변환 시 timezone 때문에 날짜가 달라질 수 있다.

Q. Backend LocalDate와 어떻게 맞춰?
A. 보통 `yyyy-MM-dd` 문자열을 그대로 보내는 방식이 안전하다.

Q. 날짜 범위 검증은 어떻게 해?
A. startDate와 endDate를 비교해 종료일이 시작일보다 빠르지 않은지 확인한다.

Q. 날짜 문자열 비교를 해도 돼?
A. `yyyy-MM-dd` 같은 ISO 형식이면 가능할 수 있지만 format이 다르면 Date 변환 기준이 필요하다.

Q. Cross Field Validation이 뭐야?
A. 여러 입력값을 함께 비교해 검증하는 방식이다.

Q. Cross Field Error는 어디에 표시해?
A. 사용자가 수정해야 할 가능성이 큰 field 근처에 표시한다.

Q. 비밀번호 확인 검증은 어떻게 해?
A. password와 confirmPassword 값이 같은지 비교한다.

Q. 비밀번호 불일치 에러는 어디에 표시해?
A. 보통 confirmPassword 필드 근처에 표시한다.

Q. 최소값과 최대값 검증은 어떻게 해?
A. 숫자로 변환한 뒤 최소값이 최대값보다 큰지 확인한다.

Q. min > max 에러는 어디에 표시해?
A. 보통 max field 근처에 표시한다.

Q. 파일 크기 검증은 어떻게 해?
A. File 객체의 size 값을 기준으로 허용 용량과 비교한다.

Q. file.size 단위는 뭐야?
A. byte 단위다.

Q. 여러 파일은 총 용량도 검증해야 해?
A. 권장한다. 개별 파일과 전체 용량 제한을 함께 검토한다.

Q. 파일 타입 검증은 어떻게 해?
A. File 객체의 type 값을 허용된 MIME type 목록과 비교한다.

Q. accept 속성만 있으면 충분해?
A. 아니다. accept는 UX 보조이며 Backend 검증이 필요하다.

Q. file.type을 완전히 신뢰해도 돼?
A. 아니다. Backend에서 추가 검증해야 한다.

Q. Submit Validation이 뭐야?
A. Form 제출 시 전체 입력값을 한 번에 검증하는 방식이다.

Q. 검증 실패 시 API 요청을 보내?
A. 아니다. Client Validation 실패 시 요청을 중단한다.

Q. onBlur Validation은 언제 좋아?
A. 사용자가 입력을 마친 뒤 피드백을 주고 싶을 때 적합하다.

Q. onChange Validation은 언제 사용해?
A. 실시간 피드백이 필요한 비밀번호 강도, 글자 수, 간단한 형식 힌트에 사용할 수 있다.

Q. 모든 검증을 onChange로 해도 돼?
A. 권장하지 않는다. 사용자 경험이 공격적으로 느껴질 수 있다.

Q. Field Error Message는 어떻게 작성해?
A. 짧고 구체적으로 사용자가 무엇을 수정해야 하는지 알려줘야 한다.

Q. Backend 예외명을 그대로 보여줘도 돼?
A. 안 된다. 내부 정보가 노출될 수 있다.

Q. Global Error Message는 언제 사용해?
A. 특정 field가 아니라 Form 전체 실패를 나타낼 때 사용한다.

Q. Validation Error도 접근성이 필요해?
A. 필요하다. 오류를 시각적으로만 표시하면 스크린 리더 사용자가 이해하기 어렵다.

Q. aria-invalid는 언제 써?
A. 해당 field에 오류가 있을 때 true로 설정한다.

Q. aria-describedby는 왜 필요해?
A. input과 error message를 연결해 오류 내용을 보조기술이 읽을 수 있게 한다.

Q. Validation과 Request Mapping 중 무엇이 먼저야?
A. 보통 Validation을 먼저 수행하고 통과하면 Request Body를 생성한다.

Q. trim은 Validation과 Mapping 양쪽에서 해야 해?
A. 기준이 일치해야 한다. 보통 검증에도 trim 기준을 쓰고 요청에도 trim된 값을 보낸다.

Q. Validation은 실패했는데 메시지가 안 보여?
A. errors key와 input field name, error rendering 조건을 확인해야 한다.

Q. 정상 입력인데 Validation이 계속 실패하는 이유는?
A. 값 타입, name-key 불일치, Number 변환, trim 결과, 비교 기준을 확인해야 한다.

Q. Validation 다음 문서는 뭐가 좋아?
A. Server Validation Error Handling, Submit Flow, Request Body Mapping 순서가 좋다.
