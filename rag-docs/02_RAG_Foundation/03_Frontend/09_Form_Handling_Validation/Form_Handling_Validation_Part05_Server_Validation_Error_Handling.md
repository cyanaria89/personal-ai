# Form Handling & Validation Part05 - Server Validation Error Handling

---

# 1. Server Validation Error Foundation

## 1.1 Server Validation Error Definition

### [개념]

Server Validation Error는 Backend가 Request Body, Query Params, Path Variable, 인증 정보, 권한, 비즈니스 규칙을 검증한 뒤 실패 결과를 Frontend에 반환하는 오류다.

Frontend는 Server Validation Error를 Field Error 또는 Global Error로 변환해 사용자에게 표시한다.

---

### [핵심]

Server Validation Error 핵심 요소:

- Server Validation
- Backend Validation
- Field Error
- Global Error
- API Error Response
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 409 Conflict
- 422 Unprocessable Entity
- Duplicate Error
- Auth Error
- Permission Error
- Error Mapping
- Error Message
- Request DTO Contract

---

### [실무]

2026 실무 기준에서 Server Validation Error는 아래 흐름으로 처리한다.

```text
API Request
→ Backend Validation
→ Validation Failed
→ Error Response
→ Frontend catch
→ Parse Error Response
→ Map Field Errors
→ Map Global Error
→ Display Error UI
→ Keep Form Values
```

Frontend 처리 기준:

```text
Field Error
→ 특정 input 근처에 표시

Global Error
→ Form 상단 또는 submit button 근처에 표시

Auth Error
→ 로그인 필요 / 세션 만료 처리

Permission Error
→ 접근 권한 없음 메시지 또는 redirect

Network Error
→ 재시도 안내
```

---

### [FAQ]

Q. Server Validation Error가 뭐야?
A. Backend가 요청 데이터를 검증한 뒤 실패 결과를 Frontend에 반환하는 오류다.

Q. Server Validation Error는 Frontend에서 어떻게 처리해?
A. 응답 구조를 파싱해 Field Error 또는 Global Error로 변환해 표시한다.

Q. Client Validation이 있어도 Server Validation Error를 처리해야 해?
A. 해야 한다. Client Validation은 우회될 수 있고 서버에서만 알 수 있는 검증도 많다.

Q. Server Validation Error 처리에서 가장 중요한 것은 뭐야?
A. Backend Error Response 구조와 Frontend Error Mapping 기준을 일치시키는 것이다.

---

# 2. Error Response Structure Rules

## 2.1 Standard Error Response

### [개념]

Standard Error Response는 Backend가 실패 응답을 일정한 구조로 반환하는 API Error Response 형식이다.

Frontend Agent는 이 구조를 기준으로 Server Validation Error를 안정적으로 mapping한다.

---

### [핵심]

표준 Error Response 요소:

- success
- status
- code
- message
- errors
- fieldErrors
- globalError
- timestamp
- path
- traceId
- validation failed
- error code

---

### [실무]

권장 응답 예:

```json
{
  "success": false,
  "status": 400,
  "code": "VALIDATION_FAILED",
  "message": "입력값 검증에 실패했습니다.",
  "errors": {
    "email": "이메일 형식이 올바르지 않습니다.",
    "nickname": "닉네임은 2자 이상이어야 합니다."
  }
}
```

Global Error 응답 예:

```json
{
  "success": false,
  "status": 401,
  "code": "LOGIN_FAILED",
  "message": "이메일 또는 비밀번호가 일치하지 않습니다."
}
```

권장:

- Field Error는 `errors` 객체로 관리
- Global Error는 `message`로 관리
- `code`는 Frontend 분기 처리에 활용
- Backend 내부 예외명 노출 금지
- 응답 구조를 API 전역에서 통일
- Frontend mapping 함수는 이 구조를 기준으로 작성

---

### [FAQ]

Q. Error Response 구조는 왜 통일해야 해?
A. Frontend가 모든 Form에서 동일한 방식으로 오류를 mapping할 수 있기 때문이다.

Q. Field Error는 어떤 구조가 좋아?
A. field name을 key로 하고 message를 value로 갖는 errors 객체가 실무적으로 다루기 쉽다.

Q. code는 왜 필요해?
A. 다국어 메시지, 분기 처리, 인증 만료 처리, 중복 오류 처리에 사용할 수 있다.

Q. Backend 예외명을 그대로 내려줘도 돼?
A. 안 된다. 내부 구현 정보가 노출될 수 있다.

---

## 2.2 Field Error Response

### [개념]

Field Error Response는 특정 Form Field에 연결되는 서버 검증 오류를 나타내는 응답이다.

예:

- email 형식 오류
- nickname 중복
- password 정책 위반
- content 길이 초과
- rating 범위 오류

---

### [핵심]

Field Error Response 기준:

- field name
- errors object
- DTO field matching
- input name matching
- validation message
- server field error
- error mapping
- field-level display

---

### [실무]

Backend 응답 예:

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

Frontend errors 변환 결과:

```javascript
const fieldErrors = {
  email: "이미 사용 중인 이메일입니다.",
  password: "비밀번호는 8자 이상이어야 합니다.",
};
```

Field Error 표시:

```jsx
<input
  name="email"
  value={values.email}
  onChange={handleChange}
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

권장:

- Backend DTO field name과 Frontend Form field name 일치
- Field Error는 해당 input 근처에 표시
- 입력 수정 시 해당 field error 제거 가능
- 서버 field error와 client field error를 같은 errors state에 저장 가능

---

### [FAQ]

Q. Field Error Response는 어디에 표시해?
A. 해당 input 근처에 표시한다.

Q. Backend field name과 Frontend name이 다르면?
A. Error Mapping이 복잡해지고 메시지가 표시되지 않을 수 있다.

Q. 서버 Field Error를 Client Error와 같은 errors state에 넣어도 돼?
A. 가능하다. field name 기준이 같다면 같은 구조로 관리할 수 있다.

Q. Field Error가 표시되지 않으면 무엇을 확인해?
A. Backend errors key, Frontend input name, errors rendering 조건을 확인한다.

---

## 2.3 Global Error Response

### [개념]

Global Error Response는 특정 field 하나에 연결하기 어려운 Form 전체 오류를 나타내는 서버 응답이다.

로그인 실패, 인증 만료, 권한 없음, 서버 장애, 네트워크 오류, 비즈니스 규칙 실패에 사용한다.

---

### [핵심]

Global Error Response 대상:

- login failed
- invalid credentials
- unauthorized
- forbidden
- server error
- network error
- business rule failed
- submit failed
- global message
- submitError

---

### [실무]

Global Error 응답 예:

```json
{
  "success": false,
  "status": 401,
  "code": "LOGIN_FAILED",
  "message": "이메일 또는 비밀번호가 일치하지 않습니다."
}
```

Frontend 처리:

```javascript
setSubmitError(error.response?.data?.message ?? "요청 처리에 실패했습니다.");
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
- 사용자가 재시도할 수 있는 메시지 제공
- 내부 오류 상세 노출 금지
- 로그인 실패는 보안상 과도하게 구체적인 원인 노출 주의
- submit 재시도 시 이전 Global Error 초기화

---

### [FAQ]

Q. Global Error Response는 언제 사용해?
A. 특정 field가 아니라 Form 전체 실패를 나타낼 때 사용한다.

Q. 로그인 실패는 Field Error야 Global Error야?
A. 계정 정보 불일치는 보통 Global Error로 처리한다.

Q. 서버 장애 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 정보가 포함될 수 있으므로 사용자 친화 메시지로 변환한다.

Q. Global Error는 어디에 표시해?
A. Form 상단 또는 submit button 근처에 표시한다.

---

# 3. HTTP Status Mapping Rules

## 3.1 400 Bad Request

### [개념]

400 Bad Request는 요청 형식, Request Body, Query Params, DTO Validation이 잘못되었을 때 사용하는 일반적인 Client Error 상태다.

Form Validation 실패에서 가장 자주 사용된다.

---

### [핵심]

400 발생 상황:

- invalid request body
- DTO validation failed
- required field missing
- invalid format
- invalid type
- bad query param
- field validation error
- malformed request

---

### [실무]

400 응답 예:

```json
{
  "success": false,
  "status": 400,
  "code": "VALIDATION_FAILED",
  "message": "입력값 검증에 실패했습니다.",
  "errors": {
    "title": "제목을 입력해 주세요.",
    "content": "내용은 500자 이하로 입력해 주세요."
  }
}
```

Frontend 처리:

```javascript
if (status === 400 && responseData.errors) {
  setErrors(responseData.errors);
  setSubmitError(responseData.message ?? "");
}
```

권장:

- Field Error 중심 처리
- Request DTO field name과 Form field name 일치
- 사용자 입력값 유지
- 검증 실패 후 API 재요청 가능
- Client Validation과 Backend Validation 기준 동기화

---

### [FAQ]

Q. 400 Bad Request는 언제 발생해?
A. 요청 데이터 형식이나 DTO Validation이 잘못되었을 때 발생한다.

Q. 400 오류는 Field Error로 처리해도 돼?
A. errors 객체가 있으면 Field Error로 처리하는 것이 좋다.

Q. 400 발생 후 입력값을 초기화해야 해?
A. 보통 초기화하지 않는다. 사용자가 수정 후 다시 제출할 수 있어야 한다.

Q. 400이 자주 발생하면 무엇을 확인해?
A. Frontend Request Body와 Backend DTO 필드명, 타입, Validation 기준을 확인한다.

---

## 3.2 401 Unauthorized

### [개념]

401 Unauthorized는 인증되지 않은 사용자가 인증이 필요한 요청을 보냈거나 Access Token이 없거나 만료되었을 때 발생한다.

Form에서는 로그인 필요, 세션 만료, 인증 실패 처리와 연결된다.

---

### [핵심]

401 발생 상황:

- no access token
- expired token
- invalid token
- login required
- invalid credentials
- unauthorized request
- refresh token flow
- redirect login

---

### [실무]

401 처리 Flow:

```text
API Request
→ 401 Unauthorized
→ Check Token Refresh Policy
→ Refresh Success: Retry Request
→ Refresh Failed: Clear Auth State
→ Redirect Login or Show Login Required
```

로그인 실패 예:

```javascript
if (status === 401) {
  setSubmitError("이메일 또는 비밀번호가 일치하지 않습니다.");
}
```

인증 만료 예:

```javascript
if (status === 401 && code === "TOKEN_EXPIRED") {
  clearAuthState();
  navigate("/login");
}
```

주의:

- 로그인 실패와 토큰 만료를 구분
- 토큰 저장과 refresh flow는 Authentication Frontend Flow 문서에서 심화
- password 오류 상세 노출 주의
- 인증 필요 Form은 submit 전 로그인 상태 확인 가능

---

### [FAQ]

Q. 401 Unauthorized는 언제 발생해?
A. 인증 정보가 없거나 유효하지 않을 때 발생한다.

Q. 로그인 실패도 401로 처리해?
A. 가능하다. 로그인 실패는 보통 Global Error로 표시한다.

Q. 토큰 만료 401은 어떻게 처리해?
A. refresh flow를 시도하거나 인증 상태를 초기화하고 로그인 페이지로 이동한다.

Q. 401 처리 로직은 Form마다 작성해야 해?
A. 공통 API layer나 interceptor에서 처리하는 것이 좋다.

---

## 3.3 403 Forbidden

### [개념]

403 Forbidden은 인증은 되었지만 해당 요청을 수행할 권한이 없을 때 발생한다.

Form에서는 수정/삭제 권한 없음, 관리자 권한 필요, 소유자 불일치 같은 상황에 사용한다.

---

### [핵심]

403 발생 상황:

- authenticated but forbidden
- no permission
- role mismatch
- owner mismatch
- admin required
- access denied
- authorization failed

---

### [실무]

403 처리 예:

```javascript
if (status === 403) {
  setSubmitError("이 작업을 수행할 권한이 없습니다.");
}
```

권한 실패 Flow:

```text
Submit Edit Form
→ Backend Owner Check
→ 403 Forbidden
→ Show Permission Error
→ Disable Retry or Redirect
```

권장:

- 권한 오류는 Global Error로 표시
- 필요 시 이전 페이지 또는 상세 페이지로 이동
- Frontend 권한 체크는 UX용
- 최종 권한 검증은 Backend 필수
- 관리자 전용 Form은 접근 단계에서 차단 가능

---

### [FAQ]

Q. 403 Forbidden은 언제 발생해?
A. 로그인은 했지만 해당 작업 권한이 없을 때 발생한다.

Q. 403은 Field Error야 Global Error야?
A. 보통 Form 전체 권한 문제이므로 Global Error로 처리한다.

Q. Frontend에서 버튼을 숨기면 Backend 권한 검사는 없어도 돼?
A. 아니다. Frontend UI 제어는 UX용이고 Backend 권한 검증은 필수다.

Q. 수정 Form에서 403이 발생하면?
A. 권한 없음 메시지를 보여주고 필요하면 이전 페이지로 이동시킨다.

---

## 3.4 404 Not Found

### [개념]

404 Not Found는 요청 대상 리소스를 찾을 수 없을 때 발생한다.

Form에서는 수정 대상, 삭제 대상, 상세 대상이 존재하지 않을 때 사용한다.

---

### [핵심]

404 발생 상황:

- resource not found
- post not found
- user not found
- review not found
- deleted resource
- invalid id
- stale page
- detail fetch failed

---

### [실무]

404 처리 예:

```javascript
if (status === 404) {
  setSubmitError("요청한 대상을 찾을 수 없습니다.");
}
```

수정 Form Flow:

```text
Open Edit Form
→ Fetch Detail
→ 404 Not Found
→ Show Not Found UI
→ Redirect List or Detail Page
```

Submit 중 404:

```text
Submit Update
→ Backend Resource Check
→ Resource Deleted
→ 404
→ Show Global Error
→ Navigate List
```

권장:

- Field Error보다 Global Error 또는 Not Found UI 사용
- 삭제된 데이터 수정 시 목록으로 이동 가능
- stale page 가능성 고려
- invalid id는 routing 단계에서 처리 가능

---

### [FAQ]

Q. 404 Not Found는 Form에서 언제 발생해?
A. 수정하거나 조회하려는 대상이 없을 때 발생한다.

Q. 404는 Field Error로 보여줘?
A. 보통 특정 field가 아니라 대상 리소스 문제이므로 Global Error나 Not Found UI로 처리한다.

Q. 수정 중 대상이 삭제되면 어떻게 해?
A. 요청한 대상을 찾을 수 없다는 메시지를 보여주고 목록이나 이전 페이지로 이동할 수 있다.

Q. 404 발생 후 입력값은 유지해야 해?
A. 대상 자체가 없으면 유지보다 페이지 이동 또는 Not Found UI가 적합할 수 있다.

---

## 3.5 409 Conflict

### [개념]

409 Conflict는 요청이 현재 서버 상태와 충돌할 때 발생한다.

Form에서는 중복 이메일, 중복 닉네임, 이미 처리된 요청, 중복 신청, 동시 수정 충돌에 사용한다.

---

### [핵심]

409 발생 상황:

- duplicate email
- duplicate nickname
- duplicate request
- already exists
- already processed
- optimistic lock conflict
- resource conflict
- idempotency conflict

---

### [실무]

409 응답 예:

```json
{
  "success": false,
  "status": 409,
  "code": "EMAIL_DUPLICATED",
  "message": "이미 사용 중인 이메일입니다.",
  "errors": {
    "email": "이미 사용 중인 이메일입니다."
  }
}
```

Frontend 처리:

```javascript
if (status === 409 && responseData.errors) {
  setErrors(responseData.errors);
} else if (status === 409) {
  setSubmitError(responseData.message);
}
```

권장:

- 중복 field가 명확하면 Field Error로 처리
- 요청 전체 충돌이면 Global Error로 처리
- 중복 확인은 Server Validation 기준
- optimistic locking 충돌은 재조회 안내 가능
- 결제/예약/신청은 중복 요청 방지와 함께 처리

---

### [FAQ]

Q. 409 Conflict는 언제 발생해?
A. 요청이 서버의 현재 상태와 충돌할 때 발생한다.

Q. 중복 이메일은 400이야 409야?
A. 팀 API 규칙에 따라 다르지만 409 Conflict로 처리하는 경우가 많다.

Q. 409는 Field Error로 처리해도 돼?
A. 중복 대상 field가 명확하면 Field Error로 처리할 수 있다.

Q. 이미 처리된 요청이면 어떻게 보여줘?
A. “이미 처리된 요청입니다.” 같은 Global Error 또는 상태 안내 메시지로 표시한다.

---

## 3.6 422 Unprocessable Entity

### [개념]

422 Unprocessable Entity는 요청 형식은 맞지만 의미적으로 처리할 수 없는 경우에 사용할 수 있는 상태다.

일부 API에서는 Validation Error를 400 대신 422로 표현한다.

---

### [핵심]

422 발생 상황:

- semantic validation failed
- business rule validation
- invalid state
- unprocessable request
- domain validation
- validation error alternative

---

### [실무]

422 응답 예:

```json
{
  "success": false,
  "status": 422,
  "code": "INVALID_DATE_RANGE",
  "message": "종료일은 시작일 이후여야 합니다.",
  "errors": {
    "endDate": "종료일은 시작일 이후여야 합니다."
  }
}
```

Frontend 처리:

```javascript
if (status === 400 || status === 422) {
  setErrors(responseData.errors ?? {});
  setSubmitError(responseData.message ?? "");
}
```

권장:

- 팀 API 기준에서 400과 422 사용 범위 통일
- Frontend는 둘 다 validation error로 처리 가능
- Field Error가 있으면 field 근처에 표시
- Global Error만 있으면 Form 상단에 표시

---

### [FAQ]

Q. 422는 언제 사용해?
A. 요청 형식은 맞지만 의미적으로 처리할 수 없는 검증 실패에 사용할 수 있다.

Q. 400과 422 중 무엇을 써야 해?
A. 팀 API 컨벤션에 따라 통일하는 것이 중요하다.

Q. Frontend에서는 422를 어떻게 처리해?
A. 보통 validation error로 보고 Field Error 또는 Global Error로 mapping한다.

Q. 422도 errors 객체를 포함할 수 있어?
A. 가능하다. field별 오류가 있으면 errors 객체로 내려주는 것이 좋다.

---

# 4. Error Mapping Rules

## 4.1 API Error Mapping Function

### [개념]

API Error Mapping Function은 Axios Error 또는 Fetch Error를 Form에서 사용할 수 있는 Field Error와 Global Error 구조로 변환하는 함수다.

Form마다 반복되는 error parsing을 줄이고 일관된 Error UX를 제공한다.

---

### [핵심]

Error Mapping Function 요소:

- axios error
- fetch error
- response data
- status
- code
- message
- errors
- fieldErrors
- submitError
- fallback message
- unknown error

---

### [실무]

Axios Error Mapping 예:

```javascript
function mapApiError(error) {
  if (!axios.isAxiosError(error)) {
    return {
      fieldErrors: {},
      globalError: "알 수 없는 오류가 발생했습니다.",
    };
  }

  const responseData = error.response?.data;

  return {
    status: error.response?.status,
    code: responseData?.code,
    fieldErrors: responseData?.errors ?? {},
    globalError: responseData?.message ?? "요청 처리에 실패했습니다.",
  };
}
```

Submit 적용:

```javascript
try {
  await submitForm(requestBody);
} catch (error) {
  const mappedError = mapApiError(error);

  setErrors(mappedError.fieldErrors);
  setSubmitError(mappedError.globalError);
}
```

권장:

- API Error Mapping 함수 공통화
- Field Error와 Global Error를 분리 반환
- fallback message 제공
- 서버 응답 구조 변경 시 mapping 함수만 수정
- 민감한 error 객체 전체를 화면에 표시하지 않음

---

### [FAQ]

Q. Error Mapping Function은 왜 필요해?
A. 서버 오류 응답을 Form에서 사용할 수 있는 errors와 submitError로 변환하기 위해 필요하다.

Q. Axios Error를 그대로 화면에 보여줘도 돼?
A. 안 된다. 내부 정보가 포함될 수 있으므로 사용자 메시지로 변환해야 한다.

Q. fieldErrors와 globalError를 왜 분리해?
A. 표시 위치와 의미가 다르기 때문이다.

Q. 서버 응답 구조가 바뀌면 어떻게 해?
A. 공통 Error Mapping 함수를 수정하면 Form 전체 영향을 줄일 수 있다.

---

## 4.2 Field Error Mapping

### [개념]

Field Error Mapping은 Backend의 field error 구조를 Frontend Form의 `errors` state로 변환하는 작업이다.

Backend field name과 Frontend field name이 다르면 mapping table이 필요할 수 있다.

---

### [핵심]

Field Error Mapping 기준:

- backend field
- frontend field
- errors object
- field name matching
- mapping table
- nested field
- array field
- DTO mismatch

---

### [실무]

동일 field name mapping:

```javascript
setErrors(responseData.errors ?? {});
```

field name이 다른 경우:

```javascript
const fieldNameMap = {
  userEmail: "email",
  userNickname: "nickname",
};

function mapFieldErrors(serverErrors) {
  return Object.entries(serverErrors ?? {}).reduce(
    (nextErrors, [serverField, message]) => {
      const frontendField = fieldNameMap[serverField] ?? serverField;
      nextErrors[frontendField] = message;
      return nextErrors;
    },
    {},
  );
}
```

권장:

- 가능하면 Backend DTO field와 Frontend Form field 일치
- 불일치 시 mapping table 명시
- nested field는 Form 구조와 errors 구조를 맞춤
- array field error는 표시 위치 기준 필요
- mapping 실패 시 Global Error fallback 제공

---

### [FAQ]

Q. Field Error Mapping이 뭐야?
A. 서버의 field error를 Frontend errors state에 맞게 변환하는 작업이다.

Q. Backend field name과 Frontend field name을 꼭 맞춰야 해?
A. 권장한다. 맞지 않으면 별도 mapping table이 필요하다.

Q. field error mapping이 실패하면 어떻게 해?
A. 해당 field에 표시되지 않으므로 Global Error fallback을 제공하는 것이 좋다.

Q. nested field error는 어떻게 처리해?
A. Form State 구조와 Error State 구조를 맞추거나 path 기반 mapping 규칙을 둔다.

---

## 4.3 Global Error Mapping

### [개념]

Global Error Mapping은 서버 응답의 message, code, status를 Form 전체 오류 메시지로 변환하는 작업이다.

특정 field와 연결하기 어려운 오류를 `submitError`로 관리한다.

---

### [핵심]

Global Error Mapping 요소:

- message
- code
- status
- submitError
- fallback message
- auth error
- permission error
- network error
- server error
- unknown error

---

### [실무]

Global Error Mapping 예:

```javascript
function mapGlobalError(error) {
  if (!axios.isAxiosError(error)) {
    return "알 수 없는 오류가 발생했습니다.";
  }

  if (!error.response) {
    return "네트워크 연결을 확인해 주세요.";
  }

  const { status, data } = error.response;

  if (status === 401) {
    return "로그인이 필요합니다.";
  }

  if (status === 403) {
    return "이 작업을 수행할 권한이 없습니다.";
  }

  return data?.message ?? "요청 처리에 실패했습니다.";
}
```

권장:

- 네트워크 오류와 서버 응답 오류 구분
- 인증/권한 오류 메시지 분리
- fallback message 제공
- code 기반 다국어 메시지 매핑 가능
- 내부 오류 상세 노출 금지

---

### [FAQ]

Q. Global Error Mapping은 언제 필요해?
A. 서버 오류가 특정 field에 연결되지 않을 때 필요하다.

Q. Network Error는 어떻게 처리해?
A. response가 없을 수 있으므로 네트워크 연결 안내 메시지를 표시한다.

Q. 403 오류 메시지는 어떻게 보여줘?
A. “이 작업을 수행할 권한이 없습니다.” 같은 Global Error로 표시한다.

Q. fallback message는 왜 필요해?
A. 서버 응답에 message가 없거나 예상하지 못한 오류가 발생할 수 있기 때문이다.

---

# 5. Server Field Error Handling Rules

## 5.1 Set Server Field Errors

### [개념]

Set Server Field Errors는 서버에서 받은 field error를 Frontend `errors` state에 저장하는 처리다.

이 방식은 Client Validation Error와 Server Validation Error를 같은 UI 구조로 표시할 수 있게 한다.

---

### [핵심]

처리 요소:

- setErrors
- server errors
- field error
- same error state
- input name matching
- display near field
- keep values
- clear on change

---

### [실무]

Submit 실패 처리:

```javascript
try {
  await createUser(requestBody);
} catch (error) {
  const { fieldErrors, globalError } = mapApiError(error);

  setErrors(fieldErrors);
  setSubmitError(globalError);
}
```

Field Error 표시:

```jsx
{
  errors.nickname && (
    <p id="nickname-error" role="alert">
      {errors.nickname}
    </p>
  );
}
```

입력 수정 시 field error 제거:

```javascript
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
```

권장:

- Server Field Error를 기존 errors state에 저장
- 입력값은 유지
- 사용자가 field 수정 시 해당 field error 제거
- Global Error와 Field Error를 동시에 표시 가능
- 서버 field error가 없으면 빈 객체 처리

---

### [FAQ]

Q. 서버 Field Error는 어디에 저장해?
A. 보통 기존 errors state에 저장한다.

Q. 서버 Field Error와 Client Error를 같은 UI로 보여줘도 돼?
A. 가능하다. field name 기준이 같다면 같은 Field Error UI를 사용할 수 있다.

Q. 서버 에러 발생 후 입력값을 지워야 해?
A. 보통 지우지 않는다. 사용자가 수정 후 다시 제출할 수 있어야 한다.

Q. 입력을 수정하면 서버 Field Error를 지워도 돼?
A. 가능하다. 이전 서버 에러가 현재 입력값과 맞지 않을 수 있기 때문이다.

---

## 5.2 Server Field Error Priority

### [개념]

Server Field Error Priority는 Client Error와 Server Error가 동시에 존재할 때 어떤 메시지를 표시할지 결정하는 기준이다.

일반적으로 현재 입력값 기준 Client Error를 우선하거나, submit 직후 서버 응답을 우선할 수 있다.

---

### [핵심]

우선순위 기준:

- client error
- server error
- latest validation result
- field modified
- stale server error
- submit response
- current input state
- error source

---

### [실무]

단일 errors state 사용:

```text
Client Validation 실패
→ setErrors(clientErrors)

Server Validation 실패
→ setErrors(serverFieldErrors)

Field 수정
→ clear errors[fieldName]
```

분리 state 사용:

```javascript
const [clientErrors, setClientErrors] = useState({});
const [serverErrors, setServerErrors] = useState({});

const emailError = clientErrors.email || serverErrors.email;
```

권장:

- 간단한 Form은 단일 errors state 사용
- 복잡한 Form은 clientErrors / serverErrors 분리 가능
- field 수정 시 serverErrors[field] 제거
- submit 직후에는 server error를 표시
- 최신 입력값과 맞지 않는 stale error 제거

---

### [FAQ]

Q. Client Error와 Server Error 중 무엇을 먼저 보여줘?
A. 현재 입력값 기준으로 의미 있는 최신 에러를 보여주는 것이 좋다.

Q. errors state를 하나만 써도 돼?
A. 간단한 Form은 하나로 충분하다.

Q. clientErrors와 serverErrors를 분리해야 해?
A. 복잡한 Form이나 에러 출처를 구분해야 하는 경우 분리할 수 있다.

Q. 서버 에러가 오래 남아 있으면 어떻게 해?
A. 사용자가 해당 field를 수정할 때 제거하는 것이 좋다.

---

# 6. Duplicate Error Handling Rules

## 6.1 Duplicate Field Error

### [개념]

Duplicate Field Error는 이메일, 닉네임, 아이디, 전화번호처럼 고유해야 하는 값이 이미 존재할 때 발생하는 서버 검증 오류다.

중복 여부는 서버 데이터 기준이므로 Backend Validation이 최종 기준이다.

---

### [핵심]

Duplicate Error 대상:

- email duplicated
- nickname duplicated
- username duplicated
- phone duplicated
- unique constraint
- conflict
- 409
- field error
- duplicate check API
- server validation

---

### [실무]

중복 이메일 응답 예:

```json
{
  "success": false,
  "status": 409,
  "code": "EMAIL_DUPLICATED",
  "message": "이미 사용 중인 이메일입니다.",
  "errors": {
    "email": "이미 사용 중인 이메일입니다."
  }
}
```

Frontend 처리:

```javascript
if (code === "EMAIL_DUPLICATED") {
  setErrors((prevErrors) => ({
    ...prevErrors,
    email: "이미 사용 중인 이메일입니다.",
  }));
}
```

권장:

- 중복 대상이 명확하면 Field Error로 표시
- 중복 확인 API가 있어도 submit 시 재검증 필요
- DB unique constraint와 Backend Validation 연결
- 입력 수정 시 중복 에러 제거
- 동시 가입/수정 race condition 고려

---

### [FAQ]

Q. 중복 이메일은 Frontend에서 검증할 수 있어?
A. 입력 형식은 Frontend에서 검증할 수 있지만 실제 중복 여부는 Backend에서 확인해야 한다.

Q. 중복 오류는 Field Error로 보여줘?
A. 이메일이나 닉네임처럼 대상 field가 명확하면 Field Error로 표시한다.

Q. 중복 확인 버튼이 있으면 submit 중복 검증은 필요 없어?
A. 아니다. submit 시점에도 서버에서 다시 검증해야 한다.

Q. 중복 오류는 409로 처리해도 돼?
A. 가능하다. 팀 API 규칙에 따라 400 또는 409 중 하나로 통일하면 된다.

---

## 6.2 Duplicate Check Flow

### [개념]

Duplicate Check Flow는 회원가입이나 프로필 수정에서 사용자가 입력한 값의 중복 여부를 서버에 확인하는 흐름이다.

중복 확인은 onBlur, 버튼 클릭, submit 시점 중 하나 또는 복합 방식으로 처리할 수 있다.

---

### [핵심]

Duplicate Check 방식:

- onBlur duplicate check
- check button
- submit validation
- debounce
- pending state
- checked value
- stale check result
- race condition
- final server validation

---

### [실무]

중복 확인 Flow:

```text
User Input Email
→ Client Format Validation
→ Duplicate Check Request
→ Available / Duplicated Result
→ Store Checked Value
→ User Modifies Email
→ Invalidate Previous Check
→ Submit
→ Backend Final Duplicate Validation
```

중복 확인 상태 예:

```javascript
const [emailCheck, setEmailCheck] = useState({
  checkedValue: "",
  available: false,
  message: "",
});
```

입력 수정 시 기존 확인 무효화:

```javascript
function handleEmailChange(event) {
  const nextEmail = event.target.value;

  setValues((prevValues) => ({
    ...prevValues,
    email: nextEmail,
  }));

  setEmailCheck({
    checkedValue: "",
    available: false,
    message: "",
  });
}
```

권장:

- 중복 확인 전 email format validation
- 중복 확인한 값과 현재 입력값 비교
- 입력이 바뀌면 이전 중복 확인 결과 무효화
- submit 시 서버 최종 검증 유지
- check pending 상태 표시

---

### [FAQ]

Q. 중복 확인은 언제 하는 게 좋아?
A. onBlur, 확인 버튼, submit 시점 중 서비스 UX에 맞게 선택한다.

Q. 중복 확인 후 값을 바꾸면 어떻게 해?
A. 이전 중복 확인 결과를 무효화해야 한다.

Q. 중복 확인 성공이면 submit에서 검증 생략해도 돼?
A. 안 된다. submit 시 서버 최종 검증은 유지해야 한다.

Q. 중복 확인 전에 무엇을 먼저 검증해?
A. 이메일 형식이나 닉네임 길이 같은 Client Validation을 먼저 수행한다.

---

# 7. Authentication Error Handling Rules

## 7.1 Login Error Handling

### [개념]

Login Error Handling은 로그인 Form 제출 실패 시 인증 오류를 사용자에게 표시하는 처리다.

로그인 실패는 보통 특정 field보다 Form 전체 인증 실패이므로 Global Error로 처리한다.

---

### [핵심]

Login Error 대상:

- invalid credentials
- wrong email
- wrong password
- account locked
- account disabled
- email not verified
- 401
- global error
- security message

---

### [실무]

로그인 실패 처리:

```javascript
try {
  await login(requestBody);
} catch (error) {
  const { status, code, globalError } = mapApiError(error);

  if (status === 401) {
    setSubmitError("이메일 또는 비밀번호가 일치하지 않습니다.");
    return;
  }

  setSubmitError(globalError);
}
```

권장:

- 계정 정보 불일치는 Global Error
- 이메일 형식 오류는 Client Field Error
- password console.log 금지
- 과도하게 구체적인 실패 원인 노출 주의
- 로그인 실패 후 입력값 유지
- 제출 중 버튼 disabled 처리

---

### [FAQ]

Q. 로그인 실패는 Field Error야 Global Error야?
A. 계정 정보 불일치는 보통 Global Error로 처리한다.

Q. 이메일 형식 오류는 어디에 표시해?
A. email Field Error로 표시한다.

Q. 비밀번호가 틀렸다고 정확히 알려줘도 돼?
A. 보안 정책에 따라 다르지만 보통 “이메일 또는 비밀번호가 일치하지 않습니다.”처럼 표시한다.

Q. 로그인 실패 후 password를 지워야 해?
A. 서비스 정책에 따라 다르지만 입력값 유지 또는 password만 초기화할 수 있다.

---

## 7.2 Token Expired Error Handling

### [개념]

Token Expired Error Handling은 Access Token이 만료되어 인증 요청이 실패했을 때 처리하는 흐름이다.

Form 자체 오류가 아니라 인증 상태 오류이므로 공통 API Layer 또는 Authentication Flow에서 처리하는 것이 적합하다.

---

### [핵심]

Token Expired 요소:

- access token expired
- refresh token
- 401
- retry request
- clear auth state
- redirect login
- interceptor
- auth state
- session expired message

---

### [실무]

Token Expired Flow:

```text
Submit Authenticated Form
→ 401 TOKEN_EXPIRED
→ Try Refresh Token
→ Refresh Success
→ Retry Original Request
→ Refresh Failed
→ Clear Auth State
→ Redirect Login
```

Form fallback:

```javascript
if (status === 401 && code === "TOKEN_EXPIRED") {
  setSubmitError("로그인 세션이 만료되었습니다. 다시 로그인해 주세요.");
}
```

권장:

- 토큰 만료 처리는 interceptor에서 공통 처리
- Form마다 refresh logic 중복 작성 금지
- refresh 실패 시 Auth State 초기화
- 사용자가 작성 중인 Form Values 보존 여부 검토
- 인증 심화는 Authentication Frontend Flow 문서에서 관리

---

### [FAQ]

Q. Token Expired Error는 Form Error야?
A. Form 입력 오류라기보다 인증 상태 오류다.

Q. token 만료 처리는 어디서 하는 게 좋아?
A. 공통 API layer나 interceptor에서 처리하는 것이 좋다.

Q. refresh 실패하면 어떻게 해?
A. 인증 상태를 초기화하고 로그인 페이지로 이동하거나 세션 만료 메시지를 표시한다.

Q. 작성 중이던 Form 값은 보존해야 해?
A. UX 정책에 따라 다르지만 긴 Form은 보존을 검토할 수 있다.

---

# 8. Permission Error Handling Rules

## 8.1 Forbidden Form Action

### [개념]

Forbidden Form Action은 사용자가 Form을 제출했지만 해당 작업 권한이 없어 서버가 거부하는 상황이다.

예:

- 게시글 수정 권한 없음
- 리뷰 삭제 권한 없음
- 관리자 기능 접근
- 소유자 불일치

---

### [핵심]

Forbidden Error 요소:

- 403
- access denied
- owner mismatch
- role mismatch
- admin required
- permission check
- global error
- redirect
- disable form

---

### [실무]

403 처리:

```javascript
if (status === 403) {
  setSubmitError("이 작업을 수행할 권한이 없습니다.");
}
```

권한 없는 수정 Form Flow:

```text
Open Edit Page
→ Frontend Optional Permission Check
→ Submit
→ Backend Permission Check
→ 403 Forbidden
→ Show Permission Error
→ Disable Submit or Redirect
```

권장:

- Frontend 권한 체크는 UX용
- Backend 권한 체크는 필수
- 권한 오류는 Global Error로 처리
- 반복 제출을 막기 위해 submit button 비활성화 가능
- 권한 없는 페이지는 접근 단계에서 redirect 가능

---

### [FAQ]

Q. 권한 없음 오류는 어떻게 처리해?
A. Global Error로 표시하고 필요하면 이전 페이지나 목록으로 이동시킨다.

Q. Frontend에서 버튼을 숨기면 Backend 권한 검사는 필요 없어?
A. 아니다. Backend 권한 검증은 반드시 필요하다.

Q. 403 에러는 Field Error로 표시해?
A. 보통 Form 전체 권한 문제이므로 Global Error로 표시한다.

Q. 관리자 권한이 필요한 Form은 어떻게 처리해?
A. 접근 단계에서 권한을 확인하고, Backend에서도 최종 검증한다.

---

# 9. Network and Server Error Handling Rules

## 9.1 Network Error Handling

### [개념]

Network Error는 서버 응답을 받지 못한 오류다.

인터넷 연결 문제, CORS 문제, 서버 다운, 요청 timeout 등이 원인일 수 있다.

---

### [핵심]

Network Error 원인:

- no response
- offline
- timeout
- CORS error
- server down
- DNS issue
- connection refused
- retry
- fallback message

---

### [실무]

Axios Network Error 처리:

```javascript
function mapNetworkError(error) {
  if (axios.isAxiosError(error) && !error.response) {
    return "네트워크 연결을 확인해 주세요.";
  }

  return "";
}
```

Submit 적용:

```javascript
catch (error) {
  if (axios.isAxiosError(error) && !error.response) {
    setSubmitError("서버에 연결할 수 없습니다. 잠시 후 다시 시도해 주세요.");
    return;
  }

  const mappedError = mapApiError(error);
  setErrors(mappedError.fieldErrors);
  setSubmitError(mappedError.globalError);
}
```

권장:

- response 없는 오류와 response 있는 오류 구분
- 사용자에게 재시도 가능 메시지 제공
- 입력값 유지
- submit button 복구
- 중요한 요청은 재시도 정책 검토

---

### [FAQ]

Q. Network Error는 서버 Validation Error와 달라?
A. 다르다. 서버 응답 자체를 받지 못한 오류다.

Q. Network Error는 Field Error로 표시해?
A. 보통 Form 전체 문제이므로 Global Error로 표시한다.

Q. Network Error 후 입력값을 지워야 해?
A. 보통 지우지 않는다. 사용자가 다시 제출할 수 있어야 한다.

Q. response가 없으면 무엇을 의미해?
A. 네트워크 문제, 서버 다운, CORS, timeout 등으로 응답을 받지 못했을 수 있다.

---

## 9.2 500 Server Error Handling

### [개념]

500 Server Error는 서버 내부 오류로 요청 처리가 실패한 상황이다.

Frontend는 내부 오류 상세를 노출하지 않고 사용자 친화적인 Global Error를 표시한다.

---

### [핵심]

500 Error 요소:

- internal server error
- unexpected error
- server failure
- global error
- fallback message
- retry later
- no stack trace
- no internal detail
- monitoring

---

### [실무]

500 처리:

```javascript
if (status >= 500) {
  setSubmitError("서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.");
}
```

주의:

- stack trace 노출 금지
- SQL 오류, class name, exception detail 노출 금지
- 입력값 유지
- submit 상태 복구
- 필요 시 오류 추적용 traceId 표시 가능
- 반복 발생 시 운영 로그 확인 필요

---

### [FAQ]

Q. 500 Server Error는 어떻게 보여줘?
A. “서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.” 같은 Global Error로 표시한다.

Q. 서버 stack trace를 보여줘도 돼?
A. 안 된다. 내부 정보 노출 위험이 있다.

Q. 500 오류는 사용자가 수정할 수 있어?
A. 대부분 사용자가 직접 수정할 수 없으므로 재시도 안내가 적합하다.

Q. 500 발생 후 Form 값을 유지해야 해?
A. 보통 유지한다. 서버가 복구되면 다시 제출할 수 있어야 한다.

---

# 10. Submit Failure UX Rules

## 10.1 Keep Values on Submit Failure

### [개념]

Keep Values on Submit Failure는 Form 제출 실패 후 사용자가 입력한 값을 유지하는 UX 기준이다.

Validation 실패, Server Error, Network Error 대부분에서 입력값을 유지하는 것이 좋다.

---

### [핵심]

값 유지 대상:

- validation failed
- server field error
- global error
- network error
- duplicate error
- permission error
- retry possible
- user correction
- no forced reset

---

### [실무]

나쁜 예:

```javascript
catch (error) {
  resetForm();
  setSubmitError("저장에 실패했습니다.");
}
```

좋은 예:

```javascript
catch (error) {
  const mappedError = mapApiError(error);

  setErrors(mappedError.fieldErrors);
  setSubmitError(mappedError.globalError);
}
```

권장:

- 실패 후 입력값 유지
- Field Error 표시 후 사용자가 수정 가능해야 함
- Network Error는 재시도 가능해야 함
- reset은 성공 후 또는 명시적 취소 시 수행
- 민감정보 Form은 정책에 따라 password만 초기화 가능

---

### [FAQ]

Q. Submit 실패 후 입력값은 지워야 해?
A. 보통 지우지 않는다. 사용자가 수정 후 다시 제출할 수 있도록 유지한다.

Q. 서버 오류가 나도 입력값을 유지해?
A. 대부분 유지하는 것이 좋다.

Q. 로그인 실패 후 password는 유지해도 돼?
A. 서비스 정책에 따라 유지하거나 password만 초기화할 수 있다.

Q. 언제 Form을 reset해?
A. 보통 제출 성공 후 또는 사용자가 취소/초기화를 명시했을 때 reset한다.

---

## 10.2 Clear Previous Errors Before Submit

### [개념]

Clear Previous Errors Before Submit은 새 제출을 시작하기 전에 이전 제출에서 발생한 Error State를 정리하는 기준이다.

이전 오류가 새 요청 결과와 섞이는 문제를 방지한다.

---

### [핵심]

초기화 대상:

- field errors
- global error
- submitError
- server errors
- stale errors
- previous response
- before validation
- before API request

---

### [실무]

Submit 시작 시 초기화:

```javascript
async function handleSubmit(event) {
  event.preventDefault();

  setErrors({});
  setSubmitError("");

  const nextErrors = validateForm(values);

  if (Object.keys(nextErrors).length > 0) {
    setErrors(nextErrors);
    return;
  }

  try {
    await submitForm(requestBody);
  } catch (error) {
    const mappedError = mapApiError(error);
    setErrors(mappedError.fieldErrors);
    setSubmitError(mappedError.globalError);
  }
}
```

권장:

- Client Validation 전 이전 errors 초기화
- submitError 초기화
- 새 validation 결과만 표시
- field 수정 시 해당 field error 제거 가능
- API 요청 직전에도 stale error 제거 가능

---

### [FAQ]

Q. Submit 전에 에러를 초기화해야 해?
A. 권장한다. 이전 제출의 에러가 현재 제출 결과와 섞일 수 있기 때문이다.

Q. 모든 errors를 지우고 validation을 다시 해도 돼?
A. 가능하다. submit 시점에는 전체 validation 결과를 새로 계산하는 것이 좋다.

Q. submitError도 초기화해야 해?
A. 권장한다. 이전 Global Error가 남아 있으면 혼란스러울 수 있다.

Q. field 수정 시에도 에러를 지워야 해?
A. 해당 field의 이전 에러는 지우는 것이 좋다.

---

# 11. Backend Contract Alignment Rules

## 11.1 Request DTO and Error Field Alignment

### [개념]

Request DTO and Error Field Alignment는 Frontend Form Field, Request Body Field, Backend DTO Field, Error Response Field 이름을 일치시키는 기준이다.

이름이 일치하면 Validation, Error Mapping, Request Body Mapping이 단순해진다.

---

### [핵심]

정렬 대상:

- Form field name
- values key
- Request DTO field
- Backend DTO field
- Validation field
- Error Response errors key
- Database constraint field
- API documentation

---

### [실무]

권장 정렬 예:

```text
Frontend values.email
→ Request Body email
→ Backend SignUpReqDto.email
→ Validation Error errors.email
→ UI errors.email
```

불일치 예:

```text
Frontend values.email
→ Request Body userEmail
→ Backend SignUpReqDto.loginId
→ Error Response errors.userEmail
```

불일치가 필요한 경우 mapping 함수 작성:

```javascript
function toSignUpRequest(values) {
  return {
    userEmail: values.email.trim(),
    userPassword: values.password,
  };
}
```

권장:

- 가능한 field name 통일
- 다르면 mapper와 error mapping table 작성
- API 문서에 error response field 명시
- Backend DTO 변경 시 Frontend mapping 영향 확인
- RAG 문서에서는 field alignment를 반복 강조

---

### [FAQ]

Q. Frontend field name과 Backend DTO field name을 맞춰야 해?
A. 가능하면 맞추는 것이 좋다. Error Mapping과 Request Mapping이 단순해진다.

Q. field name이 다르면 어떻게 해?
A. Request mapper와 Error Mapping table을 작성해야 한다.

Q. Backend DTO가 바뀌면 Frontend도 확인해야 해?
A. 해야 한다. Request Body와 Error Mapping이 깨질 수 있다.

Q. Error Response field name은 무엇과 맞춰야 해?
A. Frontend errors key 또는 Backend DTO field name과 맞추는 것이 좋다.

---

## 11.2 Backend Validation Rule Sync

### [개념]

Backend Validation Rule Sync는 Frontend Client Validation 기준과 Backend DTO Validation 기준을 일치시키는 작업이다.

Frontend와 Backend 검증 기준이 다르면 사용자 경험과 오류 처리가 불안정해진다.

---

### [핵심]

동기화 대상:

- required
- NotBlank
- NotNull
- Size
- Pattern
- Email
- Min
- Max
- enum
- date format
- file size
- file type
- business rule

---

### [실무]

동기화 예:

```text
Backend:
@NotBlank
@Size(max = 50)
private String title;

Frontend:
title.trim() required
title maxLength 50
validateTitle length <= 50
```

비동기화 문제:

```text
Frontend maxLength 100
Backend @Size(max = 50)
→ Frontend 통과
→ Server Validation Error 발생
→ 사용자 혼란
```

권장:

- Backend DTO 기준을 Frontend Validation에 반영
- Frontend Validation은 UX용
- Backend Validation은 최종 기준
- API 문서 또는 Domain Rules에 제한값 기록
- 변경 시 양쪽 검증 기준 업데이트

---

### [FAQ]

Q. Frontend Validation과 Backend Validation 기준은 같아야 해?
A. 같아야 한다. 다르면 Frontend에서 통과해도 서버에서 실패할 수 있다.

Q. Backend 기준이 최종이야?
A. 그렇다. Frontend는 UX용이고 Backend가 최종 검증 기준이다.

Q. 제한값은 어디 기준으로 관리해?
A. Backend DTO와 API 문서 기준으로 관리하고 Frontend에 반영한다.

Q. Validation 기준이 바뀌면 무엇을 수정해야 해?
A. Frontend validator, input 속성, Request Mapping, Error Message를 함께 확인해야 한다.

---

# 12. Server Validation Troubleshooting

## 12.1 Server Error Not Showing

### [개념]

Server Error Not Showing은 서버에서 오류 응답을 받았지만 Form UI에 에러 메시지가 표시되지 않는 문제다.

응답 구조 불일치, Error Mapping 실패, errors key 불일치, rendering 조건 오류가 주요 원인이다.

---

### [핵심]

주요 원인:

- responseData path mismatch
- errors key mismatch
- field name mismatch
- setErrors not called
- submitError not set
- catch block missing
- axios error check missing
- rendering condition issue
- interceptor swallowed error

---

### [실무]

Debug Flow:

```text
Network Response 확인
→ status 확인
→ response.data 구조 확인
→ mapApiError 결과 확인
→ setErrors 호출 확인
→ errors key와 input name 확인
→ Error UI rendering 확인
→ interceptor throw 여부 확인
```

문제 예:

```javascript
const fieldErrors = error.response?.data?.fieldErrors;
```

서버 응답이 아래 구조라면 mapping 실패:

```json
{
  "errors": {
    "email": "이메일을 입력해 주세요."
  }
}
```

수정:

```javascript
const fieldErrors = error.response?.data?.errors ?? {};
```

---

### [FAQ]

Q. 서버 에러가 화면에 안 보여?
A. 서버 응답 구조와 Frontend Error Mapping 경로가 맞는지 확인해야 한다.

Q. Network 탭에는 errors가 있는데 UI에 안 나와?
A. setErrors 호출과 errors key, rendering 조건을 확인해야 한다.

Q. interceptor 때문에 에러가 안 올 수 있어?
A. 가능하다. interceptor가 error를 처리한 뒤 throw하지 않으면 Form catch에 도달하지 않을 수 있다.

Q. 서버 message는 있는데 Field Error가 없으면?
A. submitError 같은 Global Error로 표시해야 한다.

---

## 12.2 Wrong Error Field Mapping

### [개념]

Wrong Error Field Mapping은 서버 Field Error가 잘못된 input에 표시되거나 전혀 표시되지 않는 문제다.

Backend field name, Request DTO field, Frontend values key가 불일치할 때 자주 발생한다.

---

### [핵심]

주요 원인:

- backend field mismatch
- frontend name mismatch
- mapper missing
- nested field path
- array index path
- typo
- DTO rename
- inconsistent naming

---

### [실무]

문제 예:

```json
{
  "errors": {
    "userEmail": "이미 사용 중인 이메일입니다."
  }
}
```

Frontend UI:

```jsx
{
  errors.email && <p>{errors.email}</p>;
}
```

해결:

```javascript
const fieldNameMap = {
  userEmail: "email",
};

const mappedErrors = mapFieldErrors(responseData.errors, fieldNameMap);
setErrors(mappedErrors);
```

권장:

- field name 통일 우선
- 불일치 시 mapping table 작성
- DTO rename 시 Frontend Error Mapping 검수
- nested field는 path 규칙 통일
- Error Mapping 테스트 작성 가능

---

### [FAQ]

Q. 서버 Field Error가 잘못된 위치에 표시돼?
A. Backend errors key와 Frontend errors key mapping이 잘못되었을 가능성이 크다.

Q. userEmail 에러를 email input에 표시하려면?
A. fieldNameMap을 사용해 userEmail을 email로 변환해야 한다.

Q. field name 통일이 왜 중요해?
A. Request Mapping과 Error Mapping을 단순하게 만들고 오류 가능성을 줄인다.

Q. DTO 이름을 바꾸면 무엇을 확인해야 해?
A. Request Body, Error Response, Frontend values key, Error Mapping을 함께 확인해야 한다.

---

## 12.3 Server Error Overwrites Client Error

### [개념]

Server Error Overwrites Client Error는 서버 오류를 반영하면서 기존 Client Validation Error가 의도치 않게 사라지거나 덮어써지는 문제다.

Error State 관리 기준이 불명확할 때 발생한다.

---

### [핵심]

주요 원인:

- single errors state overwrite
- setErrors server only
- stale client validation
- error source conflict
- field modified
- missing merge strategy
- submit timing

---

### [실무]

덮어쓰기 방식:

```javascript
setErrors(serverErrors);
```

병합 방식:

```javascript
setErrors((prevErrors) => ({
  ...prevErrors,
  ...serverErrors,
}));
```

권장 기준:

```text
Submit 전
→ Client Validation 실행
→ 실패하면 API 요청 안 함

Submit 후
→ Server Error만 반영

Field 수정
→ 해당 field error 제거
→ 필요 시 Client Validation 재실행
```

주의:

- Client Validation 실패 시 서버 요청을 보내지 않음
- 서버 응답은 submit 당시 값 기준
- 입력값 수정 후 server error는 stale error가 될 수 있음
- 복잡한 Form은 clientErrors/serverErrors 분리 가능

---

### [FAQ]

Q. Server Error가 Client Error를 덮어써도 돼?
A. submit 흐름에서는 가능하지만 기준을 명확히 해야 한다.

Q. Client Validation 실패 후에도 서버 요청을 보내야 해?
A. 보통 보내지 않는다. 먼저 Client Error를 수정하게 한다.

Q. Server Error와 Client Error를 병합해야 해?
A. 상황에 따라 다르다. 간단한 Form은 submit 단계별로 덮어쓰는 방식도 충분하다.

Q. 입력을 수정하면 서버 에러는 어떻게 해?
A. 해당 field의 서버 에러는 제거하는 것이 좋다.

---

# 13. Security Rules

## 13.1 Sensitive Error Message Protection

### [개념]

Sensitive Error Message Protection은 서버 오류 메시지에 내부 정보, 보안 정보, 개인정보, 인증 상세 사유가 노출되지 않도록 하는 기준이다.

Form Error UI는 사용자에게 필요한 수준의 정보만 보여줘야 한다.

---

### [핵심]

노출 금지 정보:

- stack trace
- SQL error
- table name
- column name
- class name
- package name
- token value
- password detail
- internal exception
- server path
- infrastructure detail
- personal information

---

### [실무]

나쁜 메시지:

```text
SQLIntegrityConstraintViolationException: Duplicate entry...
NullPointerException at com.example.service.UserService...
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
- Frontend에서 fallback message 적용
- exception detail 직접 표시 금지
- 민감한 인증 실패 사유 노출 최소화
- traceId는 운영 문의용으로 제한적 표시 가능

---

### [FAQ]

Q. 서버 예외 메시지를 그대로 보여줘도 돼?
A. 안 된다. 내부 정보나 보안 정보가 노출될 수 있다.

Q. SQL 오류를 사용자에게 보여줘도 돼?
A. 안 된다. 사용자 친화 메시지로 변환해야 한다.

Q. 로그인 실패 사유를 자세히 알려줘도 돼?
A. 보안 정책에 따라 제한하는 것이 좋다.

Q. traceId는 보여줘도 돼?
A. 운영 문의용으로 제한적으로 표시할 수 있지만 내부 상세 정보는 노출하지 않는다.

---

## 13.2 Sensitive Input Logging

### [개념]

Sensitive Input Logging은 Form 입력값 중 password, token, 개인정보, 파일 정보 등을 console.log나 error message에 남기지 않는 기준이다.

Server Validation Error 디버깅 중 민감정보를 출력하지 않도록 주의한다.

---

### [핵심]

로그 금지 대상:

- password
- confirmPassword
- access token
- refresh token
- personal information
- resident number
- phone number
- address
- payment info
- file content
- authorization header

---

### [실무]

나쁜 예:

```javascript
console.log(values);
console.log(error.config.headers.Authorization);
console.log(values.password);
```

좋은 예:

```javascript
console.log({
  formName: "LoginForm",
  errorCode: error.response?.data?.code,
  status: error.response?.status,
});
```

권장:

- Form 전체 values 로그 금지
- password와 token 로그 금지
- Error 객체 전체 출력 주의
- 개발 중에도 민감정보 마스킹
- 운영 환경 console log 제거
- 요청/응답 로깅 정책 준수

---

### [FAQ]

Q. Server Error 디버깅 중 values를 console.log 해도 돼?
A. 권장하지 않는다. password나 개인정보가 포함될 수 있다.

Q. password를 console.log로 확인해도 돼?
A. 안 된다. 민감정보는 로그에 남기지 않는 것이 원칙이다.

Q. Authorization header를 로그로 찍어도 돼?
A. 안 된다. Access Token이 노출될 수 있다.

Q. 디버깅 로그에는 무엇을 남겨?
A. status, code, form name처럼 민감하지 않은 정보만 남기는 것이 좋다.

---

# 14. Server Validation Error Checklist

## 14.1 Implementation Checklist

### [개념]

Server Validation Error Checklist는 Backend Error Response와 Frontend Form Error Handling이 안정적으로 연결되었는지 검수하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] Backend Error Response 구조가 통일되어 있는가?
- [ ] Field Error와 Global Error가 구분되어 있는가?
- [ ] errors 객체 key가 Frontend input name과 일치하는가?
- [ ] Backend DTO field와 Frontend values key가 정렬되어 있는가?
- [ ] Error Mapping Function이 존재하는가?
- [ ] Axios Error 또는 Fetch Error를 안전하게 파싱하는가?
- [ ] response 없는 Network Error를 별도 처리하는가?
- [ ] 400 Validation Error를 Field Error로 mapping하는가?
- [ ] 401 Auth Error 처리 기준이 있는가?
- [ ] 403 Permission Error를 Global Error로 표시하는가?
- [ ] 404 Resource Not Found 처리 기준이 있는가?
- [ ] 409 Duplicate Error 처리 기준이 있는가?
- [ ] 422 Validation Error 처리 기준이 있는가?
- [ ] 500 Server Error에서 내부 정보를 노출하지 않는가?
- [ ] Submit 실패 후 Form Values를 유지하는가?
- [ ] Submit 전에 이전 errors와 submitError를 초기화하는가?
- [ ] 입력 수정 시 해당 field server error를 제거하는가?
- [ ] 중복 확인 결과가 stale 상태가 되지 않도록 처리하는가?
- [ ] Token Expired 처리는 공통 API Layer에서 관리하는가?
- [ ] Backend Validation Rule과 Frontend Validation Rule이 동기화되어 있는가?
- [ ] password, token, 개인정보를 로그로 남기지 않는가?
- [ ] 서버 예외명, SQL 오류, stack trace를 사용자에게 표시하지 않는가?
```

---

### [실무]

검수 Flow:

```text
Error Response Structure Check
→ HTTP Status Mapping Check
→ Field Error Mapping Check
→ Global Error Mapping Check
→ Auth / Permission Error Check
→ Duplicate Error Check
→ Network / Server Error Check
→ Submit Failure UX Check
→ Security Message Check
→ Troubleshooting Review
```

---

### [FAQ]

Q. Server Validation Error 검수에서 가장 중요한 것은?
A. Error Response 구조 통일, Field Error Mapping, Global Error Mapping, 보안 메시지 보호다.

Q. Server Validation Error 다음에는 무엇을 검토해?
A. Submit Flow, Request Body Mapping, Duplicate Submit Prevention, Form Reset을 검토한다.

---

# Retrieval Queries

### [FAQ]

Q. Server Validation Error가 뭐야?
A. Backend가 요청 데이터를 검증한 뒤 실패 결과를 Frontend에 반환하는 오류다.

Q. Server Validation Error는 Frontend에서 어떻게 처리해?
A. 응답 구조를 파싱해 Field Error 또는 Global Error로 변환해 표시한다.

Q. Client Validation이 있어도 Server Validation Error를 처리해야 해?
A. 해야 한다. Client Validation은 우회될 수 있고 서버에서만 알 수 있는 검증도 많다.

Q. Server Validation Error 처리에서 가장 중요한 것은 뭐야?
A. Backend Error Response 구조와 Frontend Error Mapping 기준을 일치시키는 것이다.

Q. Error Response 구조는 왜 통일해야 해?
A. Frontend가 모든 Form에서 동일한 방식으로 오류를 mapping할 수 있기 때문이다.

Q. Field Error는 어떤 구조가 좋아?
A. field name을 key로 하고 message를 value로 갖는 errors 객체가 실무적으로 다루기 쉽다.

Q. code는 왜 필요해?
A. 다국어 메시지, 분기 처리, 인증 만료 처리, 중복 오류 처리에 사용할 수 있다.

Q. Backend 예외명을 그대로 내려줘도 돼?
A. 안 된다. 내부 구현 정보가 노출될 수 있다.

Q. Field Error Response는 어디에 표시해?
A. 해당 input 근처에 표시한다.

Q. Backend field name과 Frontend name이 다르면?
A. Error Mapping이 복잡해지고 메시지가 표시되지 않을 수 있다.

Q. 서버 Field Error를 Client Error와 같은 errors state에 넣어도 돼?
A. 가능하다. field name 기준이 같다면 같은 구조로 관리할 수 있다.

Q. Field Error가 표시되지 않으면 무엇을 확인해?
A. Backend errors key, Frontend input name, errors rendering 조건을 확인한다.

Q. Global Error Response는 언제 사용해?
A. 특정 field가 아니라 Form 전체 실패를 나타낼 때 사용한다.

Q. 로그인 실패는 Field Error야 Global Error야?
A. 계정 정보 불일치는 보통 Global Error로 처리한다.

Q. 서버 장애 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 정보가 포함될 수 있으므로 사용자 친화 메시지로 변환한다.

Q. Global Error는 어디에 표시해?
A. Form 상단 또는 submit button 근처에 표시한다.

Q. 400 Bad Request는 언제 발생해?
A. 요청 데이터 형식이나 DTO Validation이 잘못되었을 때 발생한다.

Q. 400 오류는 Field Error로 처리해도 돼?
A. errors 객체가 있으면 Field Error로 처리하는 것이 좋다.

Q. 400 발생 후 입력값을 초기화해야 해?
A. 보통 초기화하지 않는다. 사용자가 수정 후 다시 제출할 수 있어야 한다.

Q. 400이 자주 발생하면 무엇을 확인해?
A. Frontend Request Body와 Backend DTO 필드명, 타입, Validation 기준을 확인한다.

Q. 401 Unauthorized는 언제 발생해?
A. 인증 정보가 없거나 유효하지 않을 때 발생한다.

Q. 로그인 실패도 401로 처리해?
A. 가능하다. 로그인 실패는 보통 Global Error로 표시한다.

Q. 토큰 만료 401은 어떻게 처리해?
A. refresh flow를 시도하거나 인증 상태를 초기화하고 로그인 페이지로 이동한다.

Q. 401 처리 로직은 Form마다 작성해야 해?
A. 공통 API layer나 interceptor에서 처리하는 것이 좋다.

Q. 403 Forbidden은 언제 발생해?
A. 로그인은 했지만 해당 작업 권한이 없을 때 발생한다.

Q. 403은 Field Error야 Global Error야?
A. 보통 Form 전체 권한 문제이므로 Global Error로 처리한다.

Q. Frontend에서 버튼을 숨기면 Backend 권한 검사는 없어도 돼?
A. 아니다. Frontend UI 제어는 UX용이고 Backend 권한 검증은 필수다.

Q. 수정 Form에서 403이 발생하면?
A. 권한 없음 메시지를 보여주고 필요하면 이전 페이지로 이동시킨다.

Q. 404 Not Found는 Form에서 언제 발생해?
A. 수정하거나 조회하려는 대상이 없을 때 발생한다.

Q. 404는 Field Error로 보여줘?
A. 보통 특정 field가 아니라 대상 리소스 문제이므로 Global Error나 Not Found UI로 처리한다.

Q. 수정 중 대상이 삭제되면 어떻게 해?
A. 요청한 대상을 찾을 수 없다는 메시지를 보여주고 목록이나 이전 페이지로 이동할 수 있다.

Q. 409 Conflict는 언제 발생해?
A. 요청이 서버의 현재 상태와 충돌할 때 발생한다.

Q. 중복 이메일은 400이야 409야?
A. 팀 API 규칙에 따라 다르지만 409 Conflict로 처리하는 경우가 많다.

Q. 409는 Field Error로 처리해도 돼?
A. 중복 대상 field가 명확하면 Field Error로 처리할 수 있다.

Q. 이미 처리된 요청이면 어떻게 보여줘?
A. “이미 처리된 요청입니다.” 같은 Global Error 또는 상태 안내 메시지로 표시한다.

Q. 422는 언제 사용해?
A. 요청 형식은 맞지만 의미적으로 처리할 수 없는 검증 실패에 사용할 수 있다.

Q. 400과 422 중 무엇을 써야 해?
A. 팀 API 컨벤션에 따라 통일하는 것이 중요하다.

Q. Frontend에서는 422를 어떻게 처리해?
A. 보통 validation error로 보고 Field Error 또는 Global Error로 mapping한다.

Q. Error Mapping Function은 왜 필요해?
A. 서버 오류 응답을 Form에서 사용할 수 있는 errors와 submitError로 변환하기 위해 필요하다.

Q. Axios Error를 그대로 화면에 보여줘도 돼?
A. 안 된다. 내부 정보가 포함될 수 있으므로 사용자 메시지로 변환해야 한다.

Q. fieldErrors와 globalError를 왜 분리해?
A. 표시 위치와 의미가 다르기 때문이다.

Q. 서버 응답 구조가 바뀌면 어떻게 해?
A. 공통 Error Mapping 함수를 수정하면 Form 전체 영향을 줄일 수 있다.

Q. Field Error Mapping이 뭐야?
A. 서버의 field error를 Frontend errors state에 맞게 변환하는 작업이다.

Q. Backend field name과 Frontend field name을 꼭 맞춰야 해?
A. 권장한다. 맞지 않으면 별도 mapping table이 필요하다.

Q. field error mapping이 실패하면 어떻게 해?
A. 해당 field에 표시되지 않으므로 Global Error fallback을 제공하는 것이 좋다.

Q. nested field error는 어떻게 처리해?
A. Form State 구조와 Error State 구조를 맞추거나 path 기반 mapping 규칙을 둔다.

Q. Global Error Mapping은 언제 필요해?
A. 서버 오류가 특정 field에 연결되지 않을 때 필요하다.

Q. Network Error는 어떻게 처리해?
A. response가 없을 수 있으므로 네트워크 연결 안내 메시지를 표시한다.

Q. 403 오류 메시지는 어떻게 보여줘?
A. “이 작업을 수행할 권한이 없습니다.” 같은 Global Error로 표시한다.

Q. fallback message는 왜 필요해?
A. 서버 응답에 message가 없거나 예상하지 못한 오류가 발생할 수 있기 때문이다.

Q. 서버 Field Error는 어디에 저장해?
A. 보통 기존 errors state에 저장한다.

Q. 서버 Field Error와 Client Error를 같은 UI로 보여줘도 돼?
A. 가능하다. field name 기준이 같다면 같은 Field Error UI를 사용할 수 있다.

Q. 서버 에러 발생 후 입력값을 지워야 해?
A. 보통 지우지 않는다. 사용자가 수정 후 다시 제출할 수 있어야 한다.

Q. 입력을 수정하면 서버 Field Error를 지워도 돼?
A. 가능하다. 이전 서버 에러가 현재 입력값과 맞지 않을 수 있기 때문이다.

Q. Client Error와 Server Error 중 무엇을 먼저 보여줘?
A. 현재 입력값 기준으로 의미 있는 최신 에러를 보여주는 것이 좋다.

Q. errors state를 하나만 써도 돼?
A. 간단한 Form은 하나로 충분하다.

Q. clientErrors와 serverErrors를 분리해야 해?
A. 복잡한 Form이나 에러 출처를 구분해야 하는 경우 분리할 수 있다.

Q. 서버 에러가 오래 남아 있으면 어떻게 해?
A. 사용자가 해당 field를 수정할 때 제거하는 것이 좋다.

Q. 중복 이메일은 Frontend에서 검증할 수 있어?
A. 입력 형식은 Frontend에서 검증할 수 있지만 실제 중복 여부는 Backend에서 확인해야 한다.

Q. 중복 오류는 Field Error로 보여줘?
A. 이메일이나 닉네임처럼 대상 field가 명확하면 Field Error로 표시한다.

Q. 중복 확인 버튼이 있으면 submit 중복 검증은 필요 없어?
A. 아니다. submit 시점에도 서버에서 다시 검증해야 한다.

Q. 중복 확인은 언제 하는 게 좋아?
A. onBlur, 확인 버튼, submit 시점 중 서비스 UX에 맞게 선택한다.

Q. 중복 확인 후 값을 바꾸면 어떻게 해?
A. 이전 중복 확인 결과를 무효화해야 한다.

Q. 중복 확인 성공이면 submit에서 검증 생략해도 돼?
A. 안 된다. submit 시 서버 최종 검증은 유지해야 한다.

Q. 중복 확인 전에 무엇을 먼저 검증해?
A. 이메일 형식이나 닉네임 길이 같은 Client Validation을 먼저 수행한다.

Q. 이메일 형식 오류는 어디에 표시해?
A. email Field Error로 표시한다.

Q. 비밀번호가 틀렸다고 정확히 알려줘도 돼?
A. 보안 정책에 따라 다르지만 보통 “이메일 또는 비밀번호가 일치하지 않습니다.”처럼 표시한다.

Q. Token Expired Error는 Form Error야?
A. Form 입력 오류라기보다 인증 상태 오류다.

Q. token 만료 처리는 어디서 하는 게 좋아?
A. 공통 API layer나 interceptor에서 처리하는 것이 좋다.

Q. refresh 실패하면 어떻게 해?
A. 인증 상태를 초기화하고 로그인 페이지로 이동하거나 세션 만료 메시지를 표시한다.

Q. 권한 없음 오류는 어떻게 처리해?
A. Global Error로 표시하고 필요하면 이전 페이지나 목록으로 이동시킨다.

Q. Network Error는 서버 Validation Error와 달라?
A. 다르다. 서버 응답 자체를 받지 못한 오류다.

Q. Network Error는 Field Error로 표시해?
A. 보통 Form 전체 문제이므로 Global Error로 표시한다.

Q. Network Error 후 입력값을 지워야 해?
A. 보통 지우지 않는다. 사용자가 다시 제출할 수 있어야 한다.

Q. 500 Server Error는 어떻게 보여줘?
A. “서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.” 같은 Global Error로 표시한다.

Q. 서버 stack trace를 보여줘도 돼?
A. 안 된다. 내부 정보 노출 위험이 있다.

Q. 500 발생 후 Form 값을 유지해야 해?
A. 보통 유지한다. 서버가 복구되면 다시 제출할 수 있어야 한다.

Q. Submit 실패 후 입력값은 지워야 해?
A. 보통 지우지 않는다. 사용자가 수정 후 다시 제출할 수 있도록 유지한다.

Q. Submit 전에 에러를 초기화해야 해?
A. 권장한다. 이전 제출의 에러가 현재 제출 결과와 섞일 수 있기 때문이다.

Q. Frontend field name과 Backend DTO field name을 맞춰야 해?
A. 가능하면 맞추는 것이 좋다. Error Mapping과 Request Mapping이 단순해진다.

Q. field name이 다르면 어떻게 해?
A. Request mapper와 Error Mapping table을 작성해야 한다.

Q. Frontend Validation과 Backend Validation 기준은 같아야 해?
A. 같아야 한다. 다르면 Frontend에서 통과해도 서버에서 실패할 수 있다.

Q. Backend 기준이 최종이야?
A. 그렇다. Frontend는 UX용이고 Backend가 최종 검증 기준이다.

Q. 서버 에러가 화면에 안 보여?
A. 서버 응답 구조와 Frontend Error Mapping 경로가 맞는지 확인해야 한다.

Q. interceptor 때문에 에러가 안 올 수 있어?
A. 가능하다. interceptor가 error를 처리한 뒤 throw하지 않으면 Form catch에 도달하지 않을 수 있다.

Q. 서버 Field Error가 잘못된 위치에 표시돼?
A. Backend errors key와 Frontend errors key mapping이 잘못되었을 가능성이 크다.

Q. Server Error가 Client Error를 덮어써도 돼?
A. submit 흐름에서는 가능하지만 기준을 명확히 해야 한다.

Q. 서버 예외 메시지를 그대로 보여줘도 돼?
A. 안 된다. 내부 정보나 보안 정보가 노출될 수 있다.

Q. SQL 오류를 사용자에게 보여줘도 돼?
A. 안 된다. 사용자 친화 메시지로 변환해야 한다.

Q. Server Error 디버깅 중 values를 console.log 해도 돼?
A. 권장하지 않는다. password나 개인정보가 포함될 수 있다.

Q. password를 console.log로 확인해도 돼?
A. 안 된다. 민감정보는 로그에 남기지 않는 것이 원칙이다.

Q. Authorization header를 로그로 찍어도 돼?
A. 안 된다. Access Token이 노출될 수 있다.

Q. Server Validation Error 다음 문서는 뭐가 좋아?
A. Submit Flow, Request Body Mapping, Duplicate Submit Prevention, Form Reset 순서가 좋다.
