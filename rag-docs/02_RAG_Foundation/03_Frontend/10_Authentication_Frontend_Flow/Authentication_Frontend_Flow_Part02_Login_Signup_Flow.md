# Authentication Frontend Flow Part02 - Login Flow / Signup Flow / Redirect After Login

---

# 1. Login Flow

## 1.1 Login Form Flow

### [개념]

Login Form Flow는 사용자가 이메일 또는 아이디와 비밀번호를 입력하고 Login API를 호출한 뒤 인증 상태를 갱신하는 흐름이다.

Login Flow는 단순 Form 제출이 아니라 token 처리, user state 갱신, redirect, error handling까지 포함한다.

---

### [핵심]

기본 Flow:

```text
Input Email / Password
→ Client Validation
→ Login API Request
→ Success
→ Store Token / Auth Result
→ Fetch User Profile if Needed
→ Update Auth State
→ Redirect
→ Failure
→ Show Error Message
```

핵심 키워드:

- Login Flow
- Login Form
- Login API Request
- Client Validation
- Submit Loading
- Duplicate Submit Prevention
- Access Token
- Refresh Token
- User Summary
- Auth State Update
- Redirect After Login
- Login Error Message

---

### [실무]

2026 실무 기준 Login Flow는 Form Handling, Data Fetching, Auth State, Routing이 연결된 흐름으로 설계한다.

Login Submit 예:

```tsx
type LoginRequest = {
  email: string;
  password: string;
};

async function handleLogin(values: LoginRequest) {
  try {
    setSubmitError(null);
    setSubmitting(true);

    const response = await login(values);

    setAccessToken(response.accessToken);
    setRefreshToken(response.refreshToken);
    setUser(response.user);
    setAuthenticated(true);

    navigate("/", { replace: true });
  } catch (error) {
    setSubmitError("이메일 또는 비밀번호를 확인해 주세요.");
  } finally {
    setSubmitting(false);
  }
}
```

권장 기준:

- password console.log 금지
- accessToken console.log 금지
- 로그인 실패 메시지는 과도하게 상세하지 않게 처리
- submit loading 처리
- 중복 제출 방지
- 로그인 성공 후 redirect 기준 명확화
- 이전 위치로 돌아가기 지원 가능
- token 저장과 user state 업데이트 분리 가능
- login response wrapper 구조 확인
- 로그인 실패 시 Auth State를 authenticated true로 바꾸지 않음

주의:

```text
Login Form Submit
→ Login API 성공 전 authenticated 변경 금지
→ Token 저장 전 인증 API 호출 금지
→ User State 누락 시 /me API 호출 고려
```

---

### [FAQ]

Q. 로그인 성공 후 바로 메인으로 이동하면 돼?
A. 가능하다. 다만 보호 페이지에서 로그인으로 온 경우 원래 페이지로 돌아가는 redirect flow를 제공할 수 있다.

Q. 로그인 실패 메시지는 어떻게 보여줘?
A. 계정 정보 불일치는 global form error로 표시하는 경우가 많고, 이메일 형식 오류는 field error로 처리한다.

Q. password를 console.log로 확인해도 돼?
A. 안 된다. 비밀번호는 민감정보이므로 로그에 남기지 않는다.

Q. 로그인 API 성공 전에 authenticated를 true로 바꿔도 돼?
A. 권장하지 않는다. Login API 성공 후 token과 user 정보를 처리한 뒤 authenticated를 true로 갱신해야 한다.

---

## 1.2 Login Request Design

### [개념]

Login Request Design은 Frontend가 Backend Login API에 전달하는 요청 DTO와 Form 값을 일관되게 매핑하는 기준이다.

Form Field 이름과 Backend Request Field 이름이 다르면 변환 함수가 필요하다.

---

### [핵심]

요청 필드 후보:

- email
- username
- loginId
- password
- rememberMe
- provider
- redirectUri

확인 대상:

- Backend Login API URL
- HTTP Method
- Request Body 구조
- Content-Type
- Validation Error Response
- Success Response Wrapper
- Failure Status Code

---

### [실무]

Login Request 예:

```tsx
type LoginFormValues = {
  email: string;
  password: string;
};

type LoginRequest = {
  email: string;
  password: string;
};

function toLoginRequest(values: LoginFormValues): LoginRequest {
  return {
    email: values.email.trim(),
    password: values.password,
  };
}

async function login(values: LoginFormValues) {
  const requestBody = toLoginRequest(values);
  const response = await publicApi.post("/auth/login", requestBody);
  return response.data.data;
}
```

주의:

- password는 trim하지 않는 경우가 많음
- email은 trim 가능
- loginId / email / username 필드명 Backend와 통일
- 로그인 API는 보통 publicApi 사용
- 로그인 성공 이후 인증 API는 authApi 사용
- Backend wrapper가 `response.data.data`인지 확인
- 실패 응답 mapping 기준 필요

---

### [FAQ]

Q. Login API는 publicApi로 호출해?
A. 보통 로그인 전에는 token이 없으므로 Login API는 publicApi로 호출한다.

Q. email은 trim해도 돼?
A. 일반적으로 email은 앞뒤 공백을 제거해도 된다. password는 사용자가 입력한 그대로 전달하는 것이 일반적이다.

Q. Frontend Form 필드명과 Backend Request 필드명이 다르면?
A. `toLoginRequest` 같은 변환 함수를 두어 명확히 매핑하는 것이 좋다.

---

## 1.3 Login Response Handling

### [개념]

Login Response Handling은 로그인 API 성공 응답에서 token과 사용자 정보를 어떻게 처리할지 정하는 기준이다.

Frontend는 로그인 응답을 Auth State, Token Storage, Authorization Header 흐름과 연결해야 한다.

---

### [핵심]

응답 후보:

- accessToken
- refreshToken
- tokenType
- expiresIn
- userId
- email
- nickname
- role
- user summary
- redirect target

처리 기준:

```text
accessToken
→ Authorization Header에 사용

refreshToken
→ token refresh flow에 사용

user summary
→ Auth State에 저장

role
→ Role Based UI / Role Based Route에 사용

expiresIn
→ token expired handling 기준에 사용 가능
```

---

### [실무]

응답 예:

```json
{
  "accessToken": "access-token-value",
  "refreshToken": "refresh-token-value",
  "user": {
    "userId": 1,
    "nickname": "jun",
    "role": "ROLE_USER"
  }
}
```

Wrapper 응답 예:

```json
{
  "success": true,
  "message": "로그인 성공",
  "data": {
    "accessToken": "access-token-value",
    "refreshToken": "refresh-token-value",
    "user": {
      "userId": 1,
      "nickname": "jun",
      "role": "ROLE_USER"
    }
  }
}
```

처리 예:

```tsx
async function handleLogin(values: LoginFormValues) {
  const loginResult = await login(values);

  setAccessToken(loginResult.accessToken);
  setRefreshToken(loginResult.refreshToken ?? null);

  if (loginResult.user) {
    setUser(loginResult.user);
    setAuthenticated(true);
    return;
  }

  const me = await getMe();
  setUser(me);
  setAuthenticated(true);
}
```

주의:

- Backend 응답 wrapper 구조 확인
- `response.data.data` 구조 확인
- tokenType이 있으면 Bearer 중복 주의
- 사용자 상세 정보가 부족하면 `/me` API 조회
- 민감한 사용자 정보 저장 최소화
- role naming은 `ROLE_USER`, `ROLE_ADMIN` 등으로 통일
- accessToken이 없는 성공 응답은 인증 처리 불가

---

### [FAQ]

Q. 로그인 응답에 user 정보가 없으면 어떻게 해?
A. 로그인 성공 후 access token으로 `/me` 또는 사용자 정보 조회 API를 호출해 Auth State를 채울 수 있다.

Q. tokenType이 Bearer로 오면 어떻게 해?
A. Authorization Header 생성 시 `Bearer Bearer token`처럼 중복되지 않도록 처리 기준을 통일해야 한다.

Q. 로그인 응답에서 role이 없으면 Role Based UI는 어떻게 해?
A. `/me` API로 role 포함 사용자 정보를 조회하거나 role이 필요한 UI를 loading 또는 fallback 상태로 처리해야 한다.

Q. response.data와 response.data.data 중 무엇을 써야 해?
A. Backend API wrapper 구조에 따라 다르므로 프로젝트 응답 규칙을 확인하고 API 함수에서 unwrap 기준을 통일해야 한다.

---

# 2. Login Error Handling

## 2.1 Login Failure Handling

### [개념]

Login Failure Handling은 로그인 API 실패 시 사용자에게 적절한 오류 메시지를 표시하고 Auth State가 잘못 갱신되지 않도록 처리하는 흐름이다.

로그인 실패는 사용자 입력 오류, 계정 정보 불일치, 계정 잠김, 서버 오류, 네트워크 오류로 나뉠 수 있다.

---

### [핵심]

실패 원인:

- email format invalid
- password missing
- account not found
- password mismatch
- disabled account
- locked account
- server validation error
- 401 Unauthorized
- 400 Bad Request
- 500 Server Error
- network error

처리 기준:

- field error
- global form error
- submit loading reset
- authenticated false 유지
- token 저장 금지
- password log 금지
- 재시도 가능 메시지

---

### [실무]

Login Error Mapping 예:

```tsx
function getLoginErrorMessage(error: unknown) {
  if (isAxiosError(error)) {
    const status = error.response?.status;

    if (status === 400) {
      return "입력값을 확인해 주세요.";
    }

    if (status === 401) {
      return "이메일 또는 비밀번호를 확인해 주세요.";
    }

    if (status === 403) {
      return "로그인할 수 없는 계정입니다.";
    }
  }

  return "일시적인 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.";
}
```

Submit 처리 예:

```tsx
async function handleLogin(values: LoginFormValues) {
  try {
    setSubmitting(true);
    setSubmitError(null);

    const result = await login(values);
    applyLoginResult(result);
  } catch (error) {
    clearAuth();
    setSubmitError(getLoginErrorMessage(error));
  } finally {
    setSubmitting(false);
  }
}
```

주의:

- 로그인 실패 시 token 저장 금지
- 로그인 실패 시 user state 갱신 금지
- 로그인 실패 시 authenticated true 금지
- 서버가 계정 존재 여부를 과도하게 노출하지 않도록 메시지 일반화
- 401 Login Failure와 기존 token 만료 401 처리 구분
- login API 실패를 global 401 interceptor가 무조건 logout redirect하지 않도록 주의

---

### [FAQ]

Q. 로그인 실패도 401이야?
A. Backend 설계에 따라 그럴 수 있다. 로그인 실패 401과 기존 세션 만료 401을 처리 흐름에서 구분해야 한다.

Q. 로그인 실패 시 “없는 이메일입니다”라고 보여줘도 돼?
A. 보안상 계정 존재 여부를 과도하게 노출하지 않도록 “이메일 또는 비밀번호를 확인해 주세요”처럼 일반화하는 경우가 많다.

Q. 로그인 실패했는데 authenticated가 true가 돼?
A. Login API 성공 전에 상태를 갱신했거나 catch에서 Auth State를 정리하지 않았을 가능성이 있다.

---

## 2.2 Submit Loading and Duplicate Submit

### [개념]

Submit Loading은 로그인 요청 처리 중임을 표시하는 상태다.

Duplicate Submit Prevention은 사용자가 로그인 버튼을 여러 번 눌러 중복 요청이 발생하는 것을 막는 기준이다.

---

### [핵심]

필수 상태:

- submitting
- disabled button
- loading text
- error reset
- duplicate submit prevention
- finally reset
- request in progress

---

### [실무]

예:

```tsx
function LoginButton({ submitting }: { submitting: boolean }) {
  return (
    <button type="submit" disabled={submitting}>
      {submitting ? "로그인 중..." : "로그인"}
    </button>
  );
}
```

Submit Guard 예:

```tsx
async function handleLogin(values: LoginFormValues) {
  if (submitting) {
    return;
  }

  try {
    setSubmitting(true);
    await login(values);
  } finally {
    setSubmitting(false);
  }
}
```

주의:

- 요청 시작 시 이전 submit error 제거
- finally에서 submitting false 복원
- 버튼 disabled 처리
- Enter key submit 중복 주의
- 네트워크 지연 중 여러 번 API 호출 방지
- 로그인 성공 후 페이지 이동 시 불필요한 state update warning 주의

---

### [FAQ]

Q. 로그인 버튼을 누른 뒤 또 누를 수 있게 둬도 돼?
A. 권장하지 않는다. 중복 요청을 막기 위해 submitting 상태에서 버튼을 disabled 처리하는 것이 좋다.

Q. loading 상태는 왜 필요해?
A. 사용자가 요청 진행 중임을 알 수 있고 중복 제출과 UX 혼란을 줄일 수 있다.

Q. 로그인 실패 후 버튼이 계속 비활성화돼?
A. finally에서 submitting 상태를 false로 복원하지 않았을 가능성이 있다.

---

# 3. Redirect After Login

## 3.1 Basic Redirect After Login

### [개념]

Redirect After Login은 로그인 성공 후 사용자를 어디로 이동시킬지 결정하는 흐름이다.

직접 로그인한 경우와 보호 페이지 접근 후 로그인한 경우를 구분해야 한다.

---

### [핵심]

사용 상황:

- login page에서 직접 로그인
- protected page 접근 후 login redirect
- token expired 후 login redirect
- signup 후 login
- OAuth2 callback 후 redirect

기본 기준:

- default redirect
- previous location
- replace navigation
- redirect loop prevention
- external URL redirect prevention

---

### [실무]

기본 Flow:

```text
Protected Page Access
→ Save Current Location
→ Redirect Login
→ Login Success
→ Navigate Saved Location
```

React Router 예:

```tsx
const location = useLocation();
const navigate = useNavigate();

const from = location.state?.from ?? "/";

navigate(from, { replace: true });
```

Protected Route에서 이전 위치 전달:

```tsx
return <Navigate to="/login" replace state={{ from: location.pathname }} />;
```

주의:

- redirect loop 방지
- 외부 URL redirect 방지
- redirect target validation 고려
- login page 접근 시 이미 로그인된 사용자는 main으로 이동 가능
- replace 옵션으로 history 정리
- `from`이 login page 자신이면 기본 경로로 이동
- OAuth2 callback과 일반 login redirect 기준 분리 가능

---

### [FAQ]

Q. 로그인 후 원래 보려던 페이지로 돌아가려면?
A. Protected Route에서 location state나 query string에 이전 경로를 저장하고 로그인 성공 후 해당 경로로 navigate한다.

Q. 로그인 후 항상 `/`로 보내도 돼?
A. 가능하지만 보호 페이지 접근 후 로그인한 경우 사용자가 원래 보려던 페이지로 돌아가는 UX가 더 좋을 수 있다.

Q. redirect loop는 왜 생겨?
A. 인증 상태 loading을 기다리지 않거나 login page와 protected page가 서로 redirect 조건에 걸릴 때 발생한다.

---

## 3.2 Redirect Target Validation

### [개념]

Redirect Target Validation은 로그인 성공 후 이동할 경로가 안전한 내부 경로인지 확인하는 기준이다.

외부 URL이나 의도하지 않은 경로로 redirect되면 보안 및 UX 문제가 생길 수 있다.

---

### [핵심]

검증 대상:

- internal path
- external URL
- login path
- callback path
- forbidden path
- previous location
- query parameter redirect
- open redirect prevention

---

### [실무]

간단 검증 예:

```tsx
function getSafeRedirectPath(from: unknown) {
  if (typeof from !== "string") {
    return "/";
  }

  if (!from.startsWith("/")) {
    return "/";
  }

  if (from.startsWith("//")) {
    return "/";
  }

  if (from === "/login" || from === "/signup") {
    return "/";
  }

  return from;
}
```

사용 예:

```tsx
const from = getSafeRedirectPath(location.state?.from);

navigate(from, { replace: true });
```

주의:

- 외부 URL redirect 금지
- `//evil.com` 형태 방지
- login / signup으로 다시 보내는 redirect loop 방지
- OAuth2 callback 경로를 redirect target으로 유지할지 검토
- query string 기반 redirect도 검증 필요

---

### [FAQ]

Q. redirect target 검증이 왜 필요해?
A. 외부 URL로 이동하는 open redirect 문제와 login 페이지 반복 이동 같은 redirect loop를 막기 위해 필요하다.

Q. `location.state.from`은 항상 안전해?
A. 아니다. 프로젝트 구현에 따라 값이 조작될 수 있으므로 내부 경로인지 확인하는 것이 좋다.

Q. 로그인 후 `/login`으로 다시 이동하면?
A. PublicOnlyRoute와 충돌하거나 redirect loop가 생길 수 있으므로 기본 경로로 보정하는 것이 좋다.

---

# 4. Signup Flow

## 4.1 Signup Flow Basics

### [개념]

Signup Flow는 회원가입 Form 입력값을 검증하고 Signup API를 호출한 뒤 후속 이동을 처리하는 흐름이다.

Signup Flow는 계정 생성 요청, validation error 처리, 성공 후 login page redirect 또는 auto login 정책까지 포함한다.

---

### [핵심]

기본 Flow:

```text
Input Signup Fields
→ Client Validation
→ Signup API Request
→ Server Validation
→ Success
→ Login Page Redirect or Auto Login
→ Failure
→ Field Error / Global Error
```

필수 확인:

- email format
- password policy
- confirm password
- nickname
- agreement checkbox
- duplicate email
- duplicate nickname
- server validation error
- signup success redirect
- auto login policy

---

### [실무]

Signup 처리 예:

```tsx
type SignupFormValues = {
  email: string;
  password: string;
  confirmPassword: string;
  nickname: string;
  agreed: boolean;
};

type SignupRequest = {
  email: string;
  password: string;
  nickname: string;
};

function toSignupRequest(values: SignupFormValues): SignupRequest {
  return {
    email: values.email.trim(),
    password: values.password,
    nickname: values.nickname.trim(),
  };
}

async function handleSignup(values: SignupFormValues) {
  const requestBody = toSignupRequest(values);

  try {
    await signup(requestBody);
    navigate("/login", { replace: true });
  } catch (error) {
    setErrors(mapServerValidationErrors(error));
  }
}
```

주의:

- Client Validation만 신뢰하지 않음
- Backend Validation 필수
- password 로그 출력 금지
- 서버 field error mapping 기준 필요
- 회원가입 성공 후 token 발급 여부 확인
- 자동 로그인 시 Login Flow와 동일하게 Auth State 업데이트
- confirmPassword는 Backend에 보낼 필요가 없는 경우가 많음
- 약관 동의 값은 프로젝트 정책에 따라 Backend 전달 여부 결정

---

### [FAQ]

Q. 회원가입 성공 후 자동 로그인해야 해?
A. 프로젝트 정책에 따라 다르다. 자동 로그인하려면 로그인 응답과 동일하게 token과 user state를 처리해야 한다.

Q. 이메일 중복 검사는 Frontend에서 가능해?
A. 형식 검사는 Frontend에서 가능하지만 실제 중복 여부는 Backend API 기준으로 확인해야 한다.

Q. confirmPassword도 Backend에 보내야 해?
A. 보통 confirmPassword는 Frontend 검증용이며 Backend에는 password만 보내는 경우가 많다.

Q. 회원가입 성공 후 login 페이지로 보내면 돼?
A. 가능하다. 자동 로그인 정책이 아니라면 login 페이지로 이동시키는 방식이 일반적이다.

---

## 4.2 Signup Request and Validation

### [개념]

Signup Request and Validation은 회원가입 Form 값과 Backend Signup API 요청 구조를 일치시키는 기준이다.

Frontend Validation은 UX를 위한 1차 검증이고, 최종 검증은 Backend가 수행한다.

---

### [핵심]

Client Validation:

- required
- email format
- password length
- password complexity
- confirm password match
- nickname length
- agreement required

Server Validation:

- duplicate email
- duplicate nickname
- password policy
- banned word
- account policy
- validation error response

---

### [실무]

Validation 예:

```tsx
function validateSignup(values: SignupFormValues) {
  const errors: Partial<Record<keyof SignupFormValues, string>> = {};

  if (!values.email) {
    errors.email = "이메일을 입력해 주세요.";
  }

  if (!values.password) {
    errors.password = "비밀번호를 입력해 주세요.";
  }

  if (values.password !== values.confirmPassword) {
    errors.confirmPassword = "비밀번호가 일치하지 않습니다.";
  }

  if (!values.agreed) {
    errors.agreed = "약관에 동의해 주세요.";
  }

  return errors;
}
```

Server Error Mapping 예:

```tsx
function mapServerValidationErrors(error: unknown) {
  if (!isAxiosError(error)) {
    return { global: "일시적인 오류가 발생했습니다." };
  }

  const fieldErrors = error.response?.data?.errors;

  if (fieldErrors) {
    return fieldErrors;
  }

  return { global: "회원가입에 실패했습니다." };
}
```

주의:

- Frontend 검증은 사용성 개선 목적
- Backend 검증 실패 응답 구조 확인
- field error와 global error 구분
- 중복 확인 API를 별도로 둘지 Signup API에서 처리할지 정책 필요
- password policy 문구는 Backend 정책과 일치
- Client Validation과 Backend Validation 불일치 주의

---

### [FAQ]

Q. Client Validation만 있으면 충분해?
A. 아니다. Client Validation은 UX용이고 최종 검증은 Backend에서 반드시 수행해야 한다.

Q. 중복 이메일 검사는 언제 해?
A. 별도 중복 확인 API로 미리 확인하거나 Signup API 응답의 validation error로 처리할 수 있다.

Q. 회원가입 field error는 어떻게 보여줘?
A. Backend가 내려준 field error를 Form field에 매핑하고, 일반 오류는 global error로 표시한다.

---

## 4.3 Signup Success Handling

### [개념]

Signup Success Handling은 회원가입 성공 후 사용자를 어디로 이동시키고 인증 상태를 어떻게 처리할지 정하는 기준이다.

회원가입 성공 후 자동 로그인 여부는 프로젝트 정책에 따라 결정한다.

---

### [핵심]

성공 후 정책:

- login page redirect
- auto login
- email verification required
- welcome page
- profile setup page
- redirect replace
- success message

---

### [실무]

로그인 페이지 이동 방식:

```tsx
async function handleSignup(values: SignupFormValues) {
  await signup(toSignupRequest(values));

  navigate("/login", {
    replace: true,
    state: { message: "회원가입이 완료되었습니다. 로그인해 주세요." },
  });
}
```

자동 로그인 방식:

```tsx
async function handleSignup(values: SignupFormValues) {
  const result = await signup(toSignupRequest(values));

  setAccessToken(result.accessToken);
  setRefreshToken(result.refreshToken);
  setUser(result.user);
  setAuthenticated(true);

  navigate("/", { replace: true });
}
```

이메일 인증 필요 방식:

```text
Signup Success
→ Show Email Verification Required
→ User Verifies Email
→ Login Enabled
```

주의:

- 자동 로그인 시 Login Response Handling과 동일하게 처리
- 이메일 인증이 필요한 경우 authenticated true 처리 금지
- 회원가입 직후 login page로 보낼 때 메시지 전달 가능
- replace 옵션으로 signup page history 정리 가능
- 성공 후 중복 submit 방지
- Signup API가 token을 반환하는지 확인

---

### [FAQ]

Q. 회원가입 성공 후 자동 로그인과 로그인 페이지 이동 중 뭐가 좋아?
A. 프로젝트 정책에 따라 다르다. 이메일 인증이 필요하면 로그인 페이지 또는 인증 안내로 보내는 것이 일반적이다.

Q. 회원가입 성공 후 token이 오면 바로 로그인 처리해도 돼?
A. 가능하다. 다만 Login Flow와 동일하게 token, user state, authenticated 상태를 일관되게 처리해야 한다.

Q. 이메일 인증이 필요한데 authenticated true로 해도 돼?
A. 권장하지 않는다. 이메일 인증 완료 전 접근 제한 정책이 있다면 인증 완료 후 로그인 상태로 처리해야 한다.

---

# 5. Public Only Route

## 5.1 Login and Signup Page Guard

### [개념]

Public Only Route는 이미 로그인한 사용자가 login, signup 같은 인증 전용 페이지에 접근하지 못하도록 처리하는 Route Guard다.

Protected Route가 비로그인 사용자를 막는다면 Public Only Route는 이미 로그인한 사용자를 login / signup 페이지에서 돌려보내는 UX Guard다.

---

### [핵심]

사용 대상:

- login page
- signup page
- find password page
- OAuth2 callback 예외
- already authenticated redirect
- auth initialized
- redirect loop prevention

---

### [실무]

예:

```tsx
function PublicOnlyRoute({ children }: { children: React.ReactNode }) {
  const { initialized, authenticated } = useAuth();

  if (!initialized) {
    return <p>Loading...</p>;
  }

  if (authenticated) {
    return <Navigate to="/" replace />;
  }

  return children;
}
```

적용 예:

```tsx
<Route
  path="/login"
  element={
    <PublicOnlyRoute>
      <LoginPage />
    </PublicOnlyRoute>
  }
/>

<Route
  path="/signup"
  element={
    <PublicOnlyRoute>
      <SignupPage />
    </PublicOnlyRoute>
  }
/>
```

주의:

- auth initialized 전 redirect 금지
- OAuth2 callback은 PublicOnlyRoute 예외가 필요할 수 있음
- 이미 로그인한 사용자의 login page 접근 기준 통일
- PublicOnlyRoute와 ProtectedRoute 조건 충돌 방지
- redirect target이 다시 PublicOnlyRoute에 걸리지 않도록 주의

---

### [FAQ]

Q. 로그인한 사용자가 login 페이지에 접근하면 어떻게 해?
A. 보통 메인 페이지나 이전 페이지로 redirect한다.

Q. Public Only Route도 꼭 필요해?
A. 필수는 아니지만 로그인/회원가입 페이지 UX를 정리하는 데 유용하다.

Q. OAuth2 callback도 PublicOnlyRoute로 감싸도 돼?
A. 주의해야 한다. callback 처리 전에 authenticated 상태가 바뀌거나 redirect가 발생하면 OAuth2 처리가 중단될 수 있다.

---

# 6. Login / Signup Common Mistakes

## 6.1 Common Mistakes

### [개념]

Login / Signup 구현에서 자주 발생하는 실수는 Auth State 불일치, token 처리 누락, validation error mapping 실패, redirect loop다.

문서에는 구현 실수와 해결 기준을 함께 포함해야 Agent Review 품질이 올라간다.

---

### [핵심]

자주 발생:

- password console.log
- token console.log
- Login API 성공 전 authenticated true
- 로그인 실패 후 user state 유지
- refresh token 저장 누락
- Authorization Header 연결 누락
- response.data.data unwrap 실패
- user 정보 없음에도 role UI 렌더링
- 401 Login Failure와 Token Expired 401 혼동
- submit loading 미처리
- 중복 제출 허용
- field error mapping 실패
- 회원가입 후 자동 로그인 정책 불명확
- confirmPassword를 불필요하게 Backend 전송
- redirect target 검증 누락
- login / signup redirect loop
- PublicOnlyRoute와 ProtectedRoute 충돌

---

### [실무]

Review Flow:

```text
Login / Signup 구현 확인
→ Request DTO 매핑 확인
→ Response unwrap 확인
→ Token Handling 확인
→ User State 확인
→ Auth State 확인
→ Redirect 확인
→ Error Mapping 확인
→ Loading 확인
→ Security Log 확인
```

문제 예:

```text
문제: 로그인 성공했지만 다음 인증 API가 401
원인: token은 저장했지만 Authorization Header에 연결하지 않음
해결: authApi request interceptor에서 Bearer token 추가
```

문제 예:

```text
문제: 로그인 실패 후에도 mypage 접근 가능
원인: Login API 성공 전 authenticated true 처리
해결: Login API 성공 후 token / user 처리 완료 시점에 authenticated true 변경
```

문제 예:

```text
문제: 회원가입 실패 field error가 표시되지 않음
원인: Backend validation response 구조와 Frontend mapping 불일치
해결: field error response schema 확인 후 mapServerValidationErrors 수정
```

---

### [FAQ]

Q. 로그인은 성공했는데 인증 API가 401이 나?
A. token 저장 여부, Authorization Header 포함 여부, Bearer 형식, authApi 사용 여부를 확인해야 한다.

Q. 로그인 실패했는데 로그인 상태로 보여?
A. Login API 성공 전에 authenticated를 true로 바꿨거나 실패 시 Auth State를 정리하지 않았을 가능성이 있다.

Q. 회원가입 에러가 화면에 안 보여?
A. Backend validation response 구조와 Frontend field error mapping이 맞는지 확인해야 한다.

Q. login과 signup 페이지에서 redirect가 반복돼?
A. PublicOnlyRoute, ProtectedRoute, initialized 상태, redirect target 조건이 충돌했을 가능성이 크다.

---

# 7. Part02 Review Checklist

## 7.1 Login / Signup Checklist

### [개념]

Part02 검수는 Login Flow, Signup Flow, Redirect After Login, PublicOnlyRoute가 일관된 인증 흐름으로 연결되는지 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] Login Form Flow가 포함되었는가?
- [ ] Login Request DTO 매핑 기준이 있는가?
- [ ] Login Response Handling 기준이 있는가?
- [ ] accessToken 처리 기준이 있는가?
- [ ] refreshToken 처리 기준이 있는가?
- [ ] user summary 처리 기준이 있는가?
- [ ] login response wrapper unwrap 기준이 있는가?
- [ ] Login Error Handling이 포함되었는가?
- [ ] 401 Login Failure와 Token Expired 401 구분이 있는가?
- [ ] Submit Loading 기준이 있는가?
- [ ] Duplicate Submit Prevention 기준이 있는가?
- [ ] Redirect After Login 기준이 있는가?
- [ ] Redirect Target Validation 기준이 있는가?
- [ ] Signup Flow가 포함되었는가?
- [ ] Signup Request / Validation 기준이 있는가?
- [ ] Signup Success Handling 기준이 있는가?
- [ ] Auto Login 여부 기준이 있는가?
- [ ] PublicOnlyRoute 기준이 있는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

Part02 이후 권장 문서 순서:

```text
Part02 Login Flow / Signup Flow
→ Part03 Auth State / Auth Restore
→ Part04 Token Handling / Token Storage
→ Part05 Axios Auth Integration
→ Part06 Protected Route / Role Based Route
→ Part07 Logout / User Profile Fetch
→ Part08 OAuth2 Frontend Flow
→ Part09 401 / 403 / Troubleshooting
→ Part10 Security / Checklist / Retrieval Optimization
```

검수 기준:

```text
Login Request
→ Login Response
→ Token Handling
→ Auth State
→ Redirect
→ Error Handling
→ Signup Policy
→ PublicOnlyRoute
```

---

### [FAQ]

Q. Part02의 핵심은 뭐야?
A. 로그인과 회원가입 요청, 응답 처리, 에러 처리, redirect, PublicOnlyRoute 기준을 정리하는 것이다.

Q. Part02에서 Token Storage를 깊게 다뤄?
A. 아니다. token을 받는 흐름은 다루지만 저장 위치와 보안 기준은 Token Handling 문서에서 자세히 다룬다.

Q. Part02에서 Protected Route를 깊게 다뤄?
A. 아니다. 로그인 후 redirect와 PublicOnlyRoute는 다루지만 Protected Route 상세 구현은 별도 문서에서 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. Login Flow는 어떻게 구성돼?
A. 입력값 검증, Login API 호출, token 처리, user state 갱신, authenticated 갱신, redirect, 실패 메시지 처리로 구성된다.

Q. 로그인 성공 후 뭘 해야 해?
A. access token과 user 정보를 처리하고 Auth State를 갱신한 뒤 적절한 페이지로 redirect한다.

Q. 로그인 API는 publicApi로 호출해?
A. 보통 로그인 전에는 token이 없으므로 Login API는 publicApi로 호출한다.

Q. 로그인 응답에 user 정보가 없으면 어떻게 해?
A. 로그인 성공 후 access token으로 `/me` 또는 사용자 정보 조회 API를 호출해 Auth State를 채울 수 있다.

Q. tokenType이 Bearer로 오면 어떻게 해?
A. Authorization Header 생성 시 `Bearer Bearer token`처럼 중복되지 않도록 처리 기준을 통일해야 한다.

Q. response.data와 response.data.data 중 무엇을 써야 해?
A. Backend API wrapper 구조에 따라 다르므로 프로젝트 응답 규칙을 확인하고 API 함수에서 unwrap 기준을 통일해야 한다.

Q. 로그인 실패 메시지는 어떻게 보여줘?
A. 계정 정보 불일치는 global form error로 표시하고 이메일 형식 오류 같은 입력 문제는 field error로 처리한다.

Q. password를 console.log로 확인해도 돼?
A. 안 된다. 비밀번호는 민감정보이므로 로그에 남기지 않는다.

Q. 로그인 실패도 401이야?
A. Backend 설계에 따라 그럴 수 있다. 로그인 실패 401과 기존 세션 만료 401을 처리 흐름에서 구분해야 한다.

Q. 로그인 실패 시 “없는 이메일입니다”라고 보여줘도 돼?
A. 보안상 계정 존재 여부를 과도하게 노출하지 않도록 “이메일 또는 비밀번호를 확인해 주세요”처럼 일반화하는 경우가 많다.

Q. 로그인 실패했는데 authenticated가 true가 돼?
A. Login API 성공 전에 상태를 갱신했거나 catch에서 Auth State를 정리하지 않았을 가능성이 있다.

Q. 로그인 버튼을 누른 뒤 또 누를 수 있게 둬도 돼?
A. 권장하지 않는다. 중복 요청을 막기 위해 submitting 상태에서 버튼을 disabled 처리하는 것이 좋다.

Q. 로그인 후 원래 보려던 페이지로 돌아가려면?
A. Protected Route에서 location state나 query string에 이전 경로를 저장하고 로그인 성공 후 해당 경로로 navigate한다.

Q. redirect target 검증이 왜 필요해?
A. 외부 URL로 이동하는 open redirect 문제와 login 페이지 반복 이동 같은 redirect loop를 막기 위해 필요하다.

Q. 회원가입 Flow는 어떻게 구성돼?
A. 입력값 검증, Signup API 호출, 서버 검증, 성공 후 로그인 페이지 이동 또는 자동 로그인, 실패 시 field error 표시로 구성된다.

Q. 회원가입 성공 후 자동 로그인해야 해?
A. 프로젝트 정책에 따라 다르다. 자동 로그인하려면 로그인 응답과 동일하게 token과 user state를 처리해야 한다.

Q. 이메일 중복 검사는 Frontend에서 가능해?
A. 형식 검사는 Frontend에서 가능하지만 실제 중복 여부는 Backend API 기준으로 확인해야 한다.

Q. confirmPassword도 Backend에 보내야 해?
A. 보통 confirmPassword는 Frontend 검증용이며 Backend에는 password만 보내는 경우가 많다.

Q. Client Validation만 있으면 충분해?
A. 아니다. Client Validation은 UX용이고 최종 검증은 Backend에서 반드시 수행해야 한다.

Q. 회원가입 field error는 어떻게 보여줘?
A. Backend가 내려준 field error를 Form field에 매핑하고, 일반 오류는 global error로 표시한다.

Q. 회원가입 성공 후 token이 오면 바로 로그인 처리해도 돼?
A. 가능하다. 다만 Login Flow와 동일하게 token, user state, authenticated 상태를 일관되게 처리해야 한다.

Q. 이메일 인증이 필요한데 authenticated true로 해도 돼?
A. 권장하지 않는다. 이메일 인증 완료 전 접근 제한 정책이 있다면 인증 완료 후 로그인 상태로 처리해야 한다.

Q. 로그인한 사용자가 login 페이지에 접근하면 어떻게 해?
A. 보통 메인 페이지나 이전 페이지로 redirect한다.

Q. Public Only Route는 왜 필요해?
A. 이미 로그인한 사용자가 login, signup 같은 인증 전용 페이지에 접근하지 않도록 UX를 정리하기 위해 필요하다.

Q. OAuth2 callback도 PublicOnlyRoute로 감싸도 돼?
A. 주의해야 한다. callback 처리 전에 authenticated 상태가 바뀌거나 redirect가 발생하면 OAuth2 처리가 중단될 수 있다.

Q. 로그인은 성공했는데 인증 API가 401이 나?
A. token 저장 여부, Authorization Header 포함 여부, Bearer 형식, authApi 사용 여부를 확인해야 한다.

Q. 회원가입 에러가 화면에 안 보여?
A. Backend validation response 구조와 Frontend field error mapping이 맞는지 확인해야 한다.

Q. Part02 다음 문서는 뭐야?
A. Auth State / Auth Restore 문서가 이어지는 것이 좋다.
