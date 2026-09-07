# Frontend Code Review Part05 - Form, Authentication, and Routing Review

---

# 1. Form Review Rules

## 1.1 Form Structure Review

### [개념]

Form Structure Review는 프론트엔드 입력 폼이 의미 있는 HTML 구조, 접근성, 제출 흐름을 갖추었는지 검토하는 과정이다.

Form은 단순 input 모음이 아니라 사용자가 데이터를 입력하고 검증받고 제출하는 사용자 흐름이다.

Review Agent는 form 태그, label, input name, button type, submit event, error message 연결을 함께 검토해야 한다.

---

### [핵심]

Form Structure Review 검토 항목:

- form 태그를 사용하는가?
- onSubmit으로 제출을 처리하는가?
- Enter 제출이 가능한가?
- input에 label이 연결되어 있는가?
- input id와 label htmlFor가 일치하는가?
- input name이 명확한가?
- button type이 명시되어 있는가?
- submit button과 일반 button이 구분되는가?
- placeholder를 label 대체로 사용하지 않는가?
- error message가 입력 필드와 연결되는가?
- required field가 명확히 표시되는가?
- disabled 상태가 적절히 처리되는가?

---

### [실무]

좋은 form 구조:

```jsx
<form onSubmit={handleSubmit}>
  <label htmlFor="email">이메일</label>
  <input
    id="email"
    name="email"
    type="email"
    value={email}
    onChange={handleEmailChange}
  />

  <button type="submit">로그인</button>
</form>
```

나쁜 예:

```jsx
<div>
  <input placeholder="이메일" />
  <input placeholder="비밀번호" />
  <button onClick={handleSubmit}>로그인</button>
</div>
```

문제:

```text
form 태그 없음
→ Enter 제출 불가 가능
label 없음
→ 접근성 저하
button type 없음
→ form 내부에서 의도치 않은 submit 가능
```

리뷰 코멘트 예:

```text
[Medium] 로그인 입력 영역이 form 태그 없이 div와 button click으로만 구성되어 있습니다. Enter 제출과 접근성을 위해 form onSubmit 구조로 변경하는 것이 좋습니다.
```

---

### [FAQ]

Q. Form Structure Review는 왜 필요해?
A. form 구조가 적절해야 Enter 제출, 접근성, validation, error 표시, 테스트가 안정적으로 가능하기 때문이다.

Q. form 태그 없이 div로 만들어도 돼?
A. 가능은 하지만 Enter 제출, 접근성, 브라우저 기본 동작을 고려하면 form 태그가 적합하다.

Q. placeholder를 label 대신 써도 돼?
A. 권장하지 않는다. placeholder는 입력하면 사라지고 스크린 리더 접근성도 떨어질 수 있다.

Q. button type은 꼭 써야 해?
A. form 내부에서는 반드시 명시하는 것이 좋다. 기본 submit 동작 때문에 의도치 않은 제출이 발생할 수 있다.

---

## 1.2 Controlled Input Review

### [개념]

Controlled Input Review는 input, select, textarea 값이 React state와 일관되게 연결되어 있는지 검토하는 과정이다.

Controlled Component는 입력값을 React state가 관리하는 구조이다.

입력 상태가 불명확하면 validation, submit, reset, 서버 error mapping이 어려워진다.

---

### [핵심]

Controlled Input Review 검토 항목:

- value와 onChange가 함께 있는가?
- input name과 state field가 일치하는가?
- 초기값이 undefined가 아닌가?
- null 값이 input value에 직접 들어가지 않는가?
- checkbox는 checked를 사용하는가?
- radio group이 동일 name을 사용하는가?
- select value가 option과 일치하는가?
- textarea value가 state와 연결되는가?
- form reset 동작이 명확한가?
- controlled / uncontrolled warning이 없는가?

---

### [실무]

좋은 예:

```jsx
const [formValues, setFormValues] = useState({
  email: "",
  password: "",
});

function handleChange(event) {
  const { name, value } = event.target;

  setFormValues((prevValues) => ({
    ...prevValues,
    [name]: value,
  }));
}

return (
  <form onSubmit={handleSubmit}>
    <input name="email" value={formValues.email} onChange={handleChange} />

    <input
      name="password"
      type="password"
      value={formValues.password}
      onChange={handleChange}
    />
  </form>
);
```

checkbox 예:

```jsx
<input
  type="checkbox"
  checked={isAgreed}
  onChange={(event) => setIsAgreed(event.target.checked)}
/>
```

리뷰 코멘트 예:

```text
[Medium] input value가 undefined로 시작할 수 있어 controlled / uncontrolled warning이 발생할 수 있습니다. 초기값을 빈 문자열로 설정하는 것이 안전합니다.
```

---

### [FAQ]

Q. Controlled Input은 뭐야?
A. input 값을 React state로 관리하고 value와 onChange를 연결하는 방식이다.

Q. value만 있고 onChange가 없으면 어떻게 돼?
A. read-only input처럼 동작하거나 React warning이 발생할 수 있다.

Q. input 초기값이 undefined면 문제야?
A. controlled / uncontrolled 전환 warning이 발생할 수 있으므로 빈 문자열 등 안전한 기본값을 사용하는 것이 좋다.

Q. checkbox는 value로 관리해?
A. 아니다. checkbox는 checked와 event.target.checked를 사용하는 것이 적절하다.

---

## 1.3 Form Validation Review

### [개념]

Form Validation Review는 사용자 입력값이 제출 전 프론트엔드에서 적절히 검증되고, 서버 validation error도 함께 처리되는지 검토하는 과정이다.

프론트엔드 validation은 빠른 사용자 피드백을 제공하지만 최종 검증은 백엔드에서 반드시 수행해야 한다.

---

### [핵심]

Form Validation Review 검토 항목:

- required 필드 검증이 있는가?
- email 형식 검증이 있는가?
- password 길이와 정책 검증이 있는가?
- 숫자 범위 검증이 있는가?
- 날짜 범위 검증이 있는가?
- 파일 크기 / 확장자 검증이 있는가?
- submit 전 validation이 수행되는가?
- validation message가 명확한가?
- field별 error가 표시되는가?
- 서버 validation error가 표시되는가?
- validation 실패 시 API 요청이 발생하지 않는가?
- validation 실패 후 입력값이 유지되는가?

---

### [실무]

기본 validation 예:

```js
function validateLoginForm(values) {
  const errors = {};

  if (!values.email) {
    errors.email = "이메일을 입력해 주세요.";
  } else if (!values.email.includes("@")) {
    errors.email = "올바른 이메일 형식이 아닙니다.";
  }

  if (!values.password) {
    errors.password = "비밀번호를 입력해 주세요.";
  }

  return errors;
}
```

submit 전 validation:

```js
function handleSubmit(event) {
  event.preventDefault();

  const nextErrors = validateLoginForm(formValues);
  setErrors(nextErrors);

  if (Object.keys(nextErrors).length > 0) {
    return;
  }

  submitLogin(formValues);
}
```

리뷰 코멘트 예:

```text
[High] 회원가입 form에서 필수 입력값 검증 없이 API 요청을 전송하고 있습니다. submit 전 frontend validation을 추가하고 서버 validation error도 field별로 표시해야 합니다.
```

---

### [FAQ]

Q. Form Validation Review는 왜 필요해?
A. 잘못된 입력을 빠르게 안내하고 불필요한 API 요청을 줄이기 위해 필요하다.

Q. 프론트엔드 validation만 있으면 충분해?
A. 아니다. 프론트엔드 검증은 우회 가능하므로 백엔드 validation이 반드시 필요하다.

Q. 서버 validation error도 화면에 보여줘야 해?
A. 보여줘야 한다. 중복 이메일, 권한 없음, 비밀번호 불일치 같은 서버 판단 결과는 사용자에게 필요하다.

Q. validation 실패 시 API 요청을 보내도 돼?
A. 권장하지 않는다. 프론트엔드에서 확인 가능한 오류는 요청 전에 막는 것이 좋다.

---

## 1.4 Form Submit Review

### [개념]

Form Submit Review는 form 제출 흐름이 안정적으로 처리되고 중복 제출, 무한 loading, 입력값 손실, 에러 누락이 없는지 검토하는 과정이다.

Form 제출은 사용자 데이터 변경과 직접 연결되므로 안정성이 중요하다.

---

### [핵심]

Form Submit Review 검토 항목:

- event.preventDefault 처리가 있는가?
- submit 중 중복 제출이 방지되는가?
- isSubmitting guard가 있는가?
- 제출 중 button disabled 처리가 있는가?
- 제출 중 loading text가 표시되는가?
- 성공 후 이동 또는 초기화가 명확한가?
- 실패 후 입력값이 유지되는가?
- 실패 메시지가 표시되는가?
- finally에서 submitting 상태가 종료되는가?
- 파일 업로드 진행 상태가 표시되는가?
- 취소 또는 뒤로가기 시 상태 처리가 안전한가?

---

### [실무]

안전한 submit 예:

```jsx
async function handleSubmit(event) {
  event.preventDefault();

  if (isSubmitting) return;

  const nextErrors = validateForm(formValues);
  setErrors(nextErrors);

  if (Object.keys(nextErrors).length > 0) {
    return;
  }

  setIsSubmitting(true);

  try {
    await submitForm(formValues);
    navigate("/success");
  } catch (error) {
    setSubmitError("저장에 실패했습니다.");
  } finally {
    setIsSubmitting(false);
  }
}
```

button 예:

```jsx
<button type="submit" disabled={isSubmitting}>
  {isSubmitting ? "저장 중..." : "저장"}
</button>
```

리뷰 코멘트 예:

```text
[High] form 제출 중 버튼이 disabled 되지 않아 사용자가 여러 번 클릭하면 중복 저장 요청이 발생할 수 있습니다. isSubmitting guard와 disabled 처리를 추가해야 합니다.
```

---

### [FAQ]

Q. Form Submit Review에서 가장 중요한 것은 뭐야?
A. preventDefault, validation, 중복 제출 방지, loading 종료, 실패 메시지 표시다.

Q. 제출 버튼을 여러 번 누르면 왜 문제야?
A. 중복 API 요청, 중복 저장, 중복 결제 같은 문제가 발생할 수 있다.

Q. 제출 실패 시 입력값을 지워도 돼?
A. 권장하지 않는다. 사용자가 다시 입력하지 않도록 기존 입력값을 유지하는 것이 좋다.

Q. submit 중에는 버튼을 disabled 해야 해?
A. 그렇다. 중복 제출을 막기 위해 필요하다.

---

## 1.5 File Upload Form Review

### [개념]

File Upload Form Review는 파일 업로드 입력이 확장자, 크기, 개수, 미리보기, 진행 상태, 실패 처리 기준을 만족하는지 검토하는 과정이다.

파일 업로드는 보안, 성능, UX 문제가 자주 발생하는 영역이다.

---

### [핵심]

File Upload Review 검토 항목:

- 허용 확장자를 제한하는가?
- MIME type을 검토하는가?
- 파일 크기 제한이 있는가?
- 파일 개수 제한이 있는가?
- 업로드 전 validation이 있는가?
- 미리보기 URL을 정리하는가?
- 업로드 진행 상태가 표시되는가?
- 실패 시 재시도 또는 제거가 가능한가?
- 서버 validation error를 표시하는가?
- 민감 파일 업로드를 제한하는가?
- 프론트엔드 검증만 믿지 않는가?

---

### [실무]

파일 검증 예:

```js
function validateFile(file) {
  const allowedTypes = ["image/jpeg", "image/png", "image/webp"];
  const maxSize = 5 * 1024 * 1024;

  if (!allowedTypes.includes(file.type)) {
    return "jpg, png, webp 파일만 업로드할 수 있습니다.";
  }

  if (file.size > maxSize) {
    return "파일 크기는 5MB 이하만 가능합니다.";
  }

  return null;
}
```

object URL cleanup 예:

```jsx
useEffect(() => {
  if (!previewUrl) return;

  return () => {
    URL.revokeObjectURL(previewUrl);
  };
}, [previewUrl]);
```

리뷰 코멘트 예:

```text
[High] 이미지 업로드에서 파일 크기와 확장자 검증이 없습니다. 대용량 파일이나 허용되지 않은 파일 업로드를 막기 위해 클라이언트 검증과 서버 검증을 함께 적용해야 합니다.
```

---

### [FAQ]

Q. File Upload Form Review는 왜 중요해?
A. 파일 업로드는 보안, 용량, 성능, UX 문제가 자주 발생하기 때문이다.

Q. 프론트엔드 파일 검증만 있으면 충분해?
A. 아니다. 프론트엔드 검증은 우회 가능하므로 서버에서도 반드시 검증해야 한다.

Q. 이미지 미리보기 URL은 정리해야 해?
A. 그렇다. URL.createObjectURL을 사용했다면 URL.revokeObjectURL로 정리하는 것이 좋다.

Q. 파일 크기 제한이 없으면 어떤 문제야?
A. 대용량 업로드로 성능 저하, 서버 부하, 사용자 대기 시간 증가가 발생할 수 있다.

---

# 2. Authentication Review Rules

## 2.1 Auth Flow Review

### [개념]

Auth Flow Review는 로그인, 로그아웃, 토큰 저장, 인증 상태 복원, 인증 만료, 권한별 접근이 올바르게 처리되는지 검토하는 과정이다.

Authentication Flow는 프론트엔드 사용자 경험과 백엔드 보안 검증이 함께 연결되는 영역이다.

프론트엔드 인증 처리는 UX 목적이며 실제 권한 검증은 백엔드에서 반드시 수행해야 한다.

---

### [핵심]

Auth Flow Review 검토 항목:

- 로그인 API 요청이 올바른가?
- 로그인 성공 후 token 저장이 이루어지는가?
- 로그인 성공 후 사용자 상태가 갱신되는가?
- 로그인 성공 후 redirect가 적절한가?
- 인증 필요한 API에 Authorization header가 포함되는가?
- 새로고침 후 인증 상태가 복원되는가?
- 401 발생 시 refresh 또는 로그인 이동이 처리되는가?
- 로그아웃 시 token이 제거되는가?
- 로그아웃 시 사용자 상태가 초기화되는가?
- 로그인 사용자의 로그인 페이지 접근을 redirect하는가?
- 비로그인 사용자의 보호 페이지 접근을 막는가?
- 권한 없는 사용자의 UI 접근을 제한하는가?

---

### [실무]

Auth Flow:

```text
Login Submit
→ Auth API Request
→ Token Save
→ User State Update
→ Authorization Header Ready
→ Redirect
→ Authenticated API Request
→ 401 Handling
→ Logout
→ Token Remove
→ User State Reset
```

로그인 submit 예:

```js
async function handleLogin(values) {
  try {
    const response = await authApi.login(values);
    const { accessToken, user } = response.data.data;

    saveAccessToken(accessToken);
    setCurrentUser(user);
    navigate("/", { replace: true });
  } catch (error) {
    setError("이메일 또는 비밀번호를 확인해 주세요.");
  }
}
```

리뷰 코멘트 예:

```text
[High] 로그인 성공 후 access token은 저장하지만 사용자 상태를 갱신하지 않아 화면의 인증 UI가 즉시 변경되지 않습니다. token 저장과 함께 currentUser 상태를 갱신해야 합니다.
```

---

### [FAQ]

Q. Auth Flow Review는 왜 필요해?
A. 로그인, 인증 API, 새로고침 복원, 로그아웃, 인증 만료 처리가 끊기면 주요 사용자 흐름이 실패하기 때문이다.

Q. 로그인 성공 후 토큰만 저장하면 끝이야?
A. 아니다. 사용자 상태 갱신, 인증 header 설정, redirect, 만료 처리까지 확인해야 한다.

Q. 새로고침하면 로그인이 풀리는 이유는?
A. 토큰 저장 방식과 인증 상태 복원 로직이 없기 때문일 수 있다.

Q. 프론트엔드 인증 처리만으로 보안이 충분해?
A. 아니다. 프론트엔드 인증 처리는 UX 목적이며 실제 권한 검증은 백엔드에서 반드시 수행해야 한다.

---

## 2.2 Token Storage Review

### [개념]

Token Storage Review는 Access Token과 Refresh Token을 어디에 저장하고 어떻게 사용하는지 검토하는 과정이다.

브라우저 저장소는 XSS, CSRF, 새로고침 복원, 만료 처리와 연결되므로 보안 요구사항에 맞게 선택해야 한다.

---

### [핵심]

Token Storage 방식 비교:

| 방식            | 장점                     | 단점                  |
| --------------- | ------------------------ | --------------------- |
| localStorage    | 구현 쉬움, 새로고침 유지 | XSS에 취약            |
| sessionStorage  | 탭 종료 시 제거          | XSS에 취약            |
| memory          | JS 노출 시간 감소        | 새로고침 시 사라짐    |
| httpOnly Cookie | JS 접근 불가             | CSRF / CORS 설정 필요 |

Token Storage Review 검토 항목:

- token 저장 위치가 프로젝트 보안 요구사항에 맞는가?
- logout 시 token이 제거되는가?
- 만료 token 처리 흐름이 있는가?
- Authorization header가 중복 또는 누락되지 않는가?
- token이 console에 출력되지 않는가?
- token이 URL query string에 노출되지 않는가?
- Refresh Token 저장 방식이 안전한가?
- 민감 정보가 localStorage에 과도하게 저장되지 않는가?

---

### [실무]

위험한 예:

```js
console.log("accessToken", accessToken);
```

위험한 예:

```text
/login/callback?accessToken=eyJhbGciOi...
```

logout 처리 예:

```js
function logout() {
  removeAccessToken();
  setCurrentUser(null);
  navigate("/login", { replace: true });
}
```

리뷰 코멘트 예:

```text
[High] access token이 console.log로 출력되고 있습니다. 운영 코드에 남으면 보안 위험이 있으므로 즉시 제거해야 합니다.
```

```text
[Critical] access token이 URL query string에 포함되어 있습니다. 브라우저 기록과 referrer에 노출될 수 있으므로 안전한 전달 방식으로 변경해야 합니다.
```

---

### [FAQ]

Q. JWT를 localStorage에 저장해도 돼?
A. 가능은 하지만 XSS 위험이 있다. 보안 요구사항이 높다면 httpOnly Cookie 방식도 검토해야 한다.

Q. Access Token을 console.log로 찍어도 돼?
A. 권장하지 않는다. 운영 코드에 남으면 보안 위험이다.

Q. token을 URL query string에 넣어도 돼?
A. 안 된다. 브라우저 기록, 서버 로그, referrer에 노출될 수 있어 위험하다.

Q. logout 시 무엇을 해야 해?
A. token 제거, 사용자 상태 초기화, 필요 시 서버 logout API 호출, 로그인 페이지 이동을 처리한다.

---

## 2.3 Refresh Token Review

### [개념]

Refresh Token Review는 Access Token 만료 시 사용자 흐름을 끊지 않고 안전하게 token을 갱신하는지 검토하는 과정이다.

Refresh 흐름이 잘못되면 무한 retry, 중복 refresh 요청, 인증 루프, 강제 로그아웃 문제가 발생한다.

---

### [핵심]

Refresh Token Review 검토 항목:

- 401 발생 시 refresh 흐름이 있는가?
- refresh 성공 후 원래 요청을 재시도하는가?
- refresh 실패 시 logout 처리하는가?
- refresh 요청이 중복으로 여러 번 발생하지 않는가?
- interceptor 무한 retry를 방지하는가?
- refresh token 저장 방식이 안전한가?
- refresh 중 사용자에게 불필요한 오류가 표시되지 않는가?
- refresh 후 Authorization header가 갱신되는가?

---

### [실무]

Refresh Flow:

```text
API Request
→ 401 Unauthorized
→ Refresh Token Request
→ New Access Token Save
→ Original Request Retry
→ Refresh Fail
→ Token Remove
→ Login Redirect
```

무한 retry 방지 개념:

```text
originalRequest._retry 확인
→ 이미 재시도한 요청이면 refresh 반복 금지
```

리뷰 코멘트 예:

```text
[High] 401 응답마다 refresh 요청을 반복하지만 retry guard가 없어 refresh 실패 시 무한 요청 루프가 발생할 수 있습니다. original request에 retry flag를 두고 실패 시 logout 처리해야 합니다.
```

---

### [FAQ]

Q. Refresh Token Review는 왜 필요해?
A. Access Token 만료 시 사용자 흐름을 유지하면서도 무한 retry나 인증 루프를 막기 위해 필요하다.

Q. 401이 발생하면 무조건 로그인 페이지로 보내야 해?
A. refresh token 정책이 있다면 먼저 token 갱신을 시도할 수 있다. refresh 실패 시 로그인 이동이 적절하다.

Q. refresh 요청이 여러 번 동시에 발생하면 문제야?
A. 문제다. 중복 refresh로 race condition과 token 불일치가 발생할 수 있다.

Q. refresh 실패 시 어떻게 해야 해?
A. token을 제거하고 사용자 상태를 초기화한 뒤 로그인 페이지로 이동하는 것이 일반적이다.

---

## 2.4 Protected Route Review

### [개념]

Protected Route Review는 인증이 필요한 페이지에 비로그인 사용자가 접근하지 못하도록 route 수준에서 보호하는지 검토하는 과정이다.

Protected Route는 보안의 최종 수단이 아니라 사용자 경험 보호 장치이다.

실제 권한 검증은 백엔드 API에서 반드시 수행해야 한다.

---

### [핵심]

Protected Route Review 검토 항목:

- 인증 필요 페이지가 보호되는가?
- 비로그인 접근 시 로그인 페이지로 이동하는가?
- 로그인 후 원래 페이지로 복귀할 수 있는가?
- auth loading 중 잘못 redirect하지 않는가?
- 권한별 route 보호가 있는가?
- 로그인 사용자가 login page에 접근하면 redirect하는가?
- token만 있고 user 복원이 안 된 상태를 처리하는가?
- 서버 권한 검증과 병행되는가?

---

### [실무]

Protected Route 예:

```jsx
function ProtectedRoute({ children }) {
  const { isLoggedIn, isAuthLoading } = useAuth();

  if (isAuthLoading) {
    return <p>인증 확인 중...</p>;
  }

  if (!isLoggedIn) {
    return <Navigate to="/login" replace />;
  }

  return children;
}
```

권한 route 예:

```jsx
function AdminRoute({ children }) {
  const { user, isAuthLoading } = useAuth();

  if (isAuthLoading) {
    return <p>인증 확인 중...</p>;
  }

  if (user?.role !== "ROLE_ADMIN") {
    return <Navigate to="/forbidden" replace />;
  }

  return children;
}
```

리뷰 코멘트 예:

```text
[High] 인증 상태 복원 중에도 isLoggedIn이 false로 판단되어 새로고침 직후 로그인 페이지로 redirect될 수 있습니다. auth loading 상태를 분리해 잘못된 redirect를 방지해야 합니다.
```

---

### [FAQ]

Q. Protected Route만 있으면 보안이 충분해?
A. 아니다. 프론트엔드 route 보호는 UX 목적이고 실제 권한 검증은 백엔드에서 반드시 해야 한다.

Q. 인증 확인 중 로그인 페이지로 튕기는 이유는?
A. auth loading 상태를 고려하지 않으면 새로고침 직후 잘못 redirect될 수 있다.

Q. 로그인 후 원래 페이지로 돌아가야 해?
A. 사용자 경험상 권장된다. location state나 redirect query를 사용할 수 있다.

Q. 권한별 route 보호도 필요해?
A. 관리자 페이지처럼 역할에 따라 접근이 다른 화면에는 필요하다. 단, 백엔드 권한 검증도 필수다.

---

## 2.5 Authorization UI Review

### [개념]

Authorization UI Review는 사용자 권한에 따라 버튼, 메뉴, 링크, 페이지 접근 UI가 적절히 표시되는지 검토하는 과정이다.

프론트엔드 권한 UI는 사용자의 혼란을 줄이는 UX 장치이며 보안의 최종 수단이 아니다.

---

### [핵심]

Authorization UI Review 검토 항목:

- 관리자 전용 메뉴가 일반 사용자에게 보이지 않는가?
- 수정 / 삭제 버튼이 권한 사용자에게만 보이는가?
- 비로그인 사용자의 작성 버튼 처리 정책이 명확한가?
- 권한 없음 API 실패 시 메시지가 있는가?
- UI 숨김만으로 권한 검증을 대체하지 않는가?
- role naming이 백엔드와 일치하는가?
- ROLE_USER / ROLE_ADMIN 같은 역할명이 통일되는가?
- 권한 변경 후 UI가 갱신되는가?

---

### [실무]

권한 UI 예:

```jsx
{
  user?.role === "ROLE_ADMIN" && <Link to="/admin">관리자 페이지</Link>;
}
```

작성 버튼 예:

```jsx
{
  isLoggedIn ? (
    <button type="button" onClick={openReviewModal}>
      리뷰 작성
    </button>
  ) : (
    <Link to="/login">로그인 후 리뷰 작성</Link>
  );
}
```

리뷰 코멘트 예:

```text
[High] 삭제 버튼이 모든 사용자에게 노출되고 있습니다. 프론트엔드에서 권한 UI를 제한하고, 백엔드에서도 삭제 권한 검증이 반드시 필요합니다.
```

---

### [FAQ]

Q. 권한 버튼을 숨기면 보안이 되는 거야?
A. 아니다. UI 제한은 UX 목적이고 실제 권한 검증은 백엔드에서 해야 한다.

Q. 일반 사용자에게 관리자 메뉴가 보이면 문제야?
A. UX 혼란과 불필요한 403 요청을 만들 수 있으므로 숨기는 것이 좋다.

Q. role 이름도 리뷰해야 해?
A. 해야 한다. 백엔드의 ROLE_USER, ROLE_ADMIN과 프론트엔드 조건이 일치해야 한다.

Q. 권한 없는 API 요청은 어떻게 처리해?
A. 403 응답을 받고 접근 권한이 없다는 사용자 친화 메시지를 표시해야 한다.

---

# 3. Routing Review Rules

## 3.1 Route Structure Review

### [개념]

Route Structure Review는 React Router 기반 페이지 경로가 명확하고 유지보수 가능하며 API path와 충돌하지 않는지 검토하는 과정이다.

Route 구조가 불명확하면 잘못된 이동, Not Found 누락, 인증 route 누락, 배포 후 새로고침 오류가 발생할 수 있다.

---

### [핵심]

Route Structure Review 검토 항목:

- route path가 명확한가?
- dynamic route가 적절한가?
- nested route 구조가 과하지 않은가?
- NotFound route가 있는가?
- 인증 route와 공개 route가 구분되는가?
- 관리자 route가 분리되어 있는가?
- API path와 frontend route path가 충돌하지 않는가?
- basename이 필요한 배포 환경인가?
- route param 이름이 컴포넌트와 일치하는가?
- route 중복 또는 unreachable route가 없는가?

---

### [실무]

기본 route 예:

```jsx
<Routes>
  <Route path="/" element={<MainPage />} />
  <Route path="/festivals" element={<FestivalListPage />} />
  <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
  <Route path="/login" element={<LoginPage />} />
  <Route path="*" element={<NotFoundPage />} />
</Routes>
```

보호 route 예:

```jsx
<Route
  path="/mypage"
  element={
    <ProtectedRoute>
      <MyPage />
    </ProtectedRoute>
  }
/>
```

리뷰 코멘트 예:

```text
[Medium] route 목록에 wildcard NotFound route가 없어 잘못된 URL 접근 시 빈 화면이 표시될 수 있습니다. path=\"*\" route를 추가하는 것이 좋습니다.
```

---

### [FAQ]

Q. Route Structure Review는 왜 필요해?
A. 경로 구조가 잘못되면 페이지 이동, 새로고침, 인증 보호, Not Found 처리가 실패할 수 있기 때문이다.

Q. NotFoundPage가 꼭 필요해?
A. 권장된다. 잘못된 URL에 대해 사용자가 이해할 수 있는 화면을 제공해야 한다.

Q. API path와 frontend route가 같아도 돼?
A. 권장하지 않는다. API는 `/api` prefix로 분리하는 것이 안전하다.

Q. dynamic route param 이름도 리뷰해야 해?
A. 해야 한다. route의 `:festivalId`와 컴포넌트의 useParams 사용 이름이 일치해야 한다.

---

## 3.2 Navigation Review

### [개념]

Navigation Review는 페이지 이동 방식이 SPA 특성과 사용자 경험에 맞는지 검토하는 과정이다.

내부 이동, 외부 이동, 버튼 동작, redirect, history 처리는 각각 다른 기준으로 사용해야 한다.

---

### [핵심]

Navigation Review 검토 항목:

- 내부 이동에 Link 또는 navigate를 사용하는가?
- 외부 이동에는 a 태그를 사용하는가?
- button과 link 역할이 구분되는가?
- 뒤로가기 동작이 자연스러운가?
- redirect 후 replace 필요 여부를 고려하는가?
- 로그인 후 이동 경로가 적절한가?
- 삭제 / 저장 후 이동이 명확한가?
- 새 탭 외부 링크에 rel 설정이 있는가?
- 클릭 가능한 div를 사용하지 않는가?

---

### [실무]

내부 이동:

```jsx
<Link to="/festivals">축제 목록</Link>
```

프로그래밍 이동:

```js
navigate("/login", { replace: true });
```

외부 이동:

```jsx
<a href="https://example.com" target="_blank" rel="noreferrer">
  외부 사이트
</a>
```

나쁜 예:

```jsx
<a href="/festivals">축제 목록</a>
```

문제:

```text
SPA 내부 이동에서 전체 새로고침이 발생할 수 있음
```

리뷰 코멘트 예:

```text
[Low] 내부 페이지 이동에 a 태그를 사용하고 있습니다. SPA 라우팅을 유지하려면 React Router의 Link를 사용하는 것이 좋습니다.
```

---

### [FAQ]

Q. 내부 페이지 이동에 a 태그를 써도 돼?
A. 가능하지만 SPA에서는 전체 새로고침이 발생할 수 있으므로 React Router의 Link를 권장한다.

Q. 외부 링크에는 무엇을 써야 해?
A. a 태그를 사용하고 target="\_blank"라면 rel="noreferrer" 또는 rel="noopener noreferrer"를 설정한다.

Q. button과 Link는 어떻게 구분해?
A. 페이지 이동이면 Link, 현재 화면에서 동작을 수행하면 button을 사용한다.

Q. 로그인 후 replace는 언제 써?
A. 뒤로가기로 로그인 페이지에 다시 돌아가는 것을 막고 싶을 때 사용할 수 있다.

---

## 3.3 Route Param Review

### [개념]

Route Param Review는 URL path parameter를 안전하게 읽고 검증한 뒤 API 요청과 화면 렌더링에 사용하는지 검토하는 과정이다.

route param은 문자열로 들어오며 누락, 잘못된 형식, 존재하지 않는 id를 고려해야 한다.

---

### [핵심]

Route Param Review 검토 항목:

- useParams에서 올바른 이름을 읽는가?
- param이 undefined일 수 있음을 처리하는가?
- 숫자 id가 필요한 경우 변환하는가?
- 잘못된 param 형식을 처리하는가?
- param 변경 시 API 요청이 다시 실행되는가?
- 404 응답을 Not Found UI로 처리하는가?
- param을 그대로 민감 API에 사용하지 않는가?
- route param과 API path variable이 일치하는가?

---

### [실무]

예:

```jsx
function FestivalDetailPage() {
  const { festivalId } = useParams();

  if (!festivalId) {
    return <NotFoundPage />;
  }

  return <FestivalDetail festivalId={festivalId} />;
}
```

숫자 변환 예:

```js
const numericFestivalId = Number(festivalId);

if (Number.isNaN(numericFestivalId)) {
  return <NotFoundPage />;
}
```

리뷰 코멘트 예:

```text
[High] useEffect에서 festivalId를 사용하지만 dependency array에 포함되어 있지 않아 route param이 변경되어도 이전 상세 데이터가 유지될 수 있습니다.
```

---

### [FAQ]

Q. useParams 값은 숫자야 문자열이야?
A. React Router의 route param은 문자열로 들어온다. 숫자가 필요하면 변환해야 한다.

Q. route param이 없을 수도 있어?
A. route 구조나 잘못된 접근에 따라 undefined일 수 있으므로 방어 처리가 필요하다.

Q. param 변경 시 API를 다시 호출해야 해?
A. 상세 페이지 id처럼 데이터 기준이 되는 param이면 dependency에 포함해 다시 요청해야 한다.

Q. 존재하지 않는 id는 어떻게 처리해?
A. API 404 응답을 Not Found UI로 표시하는 것이 좋다.

---

## 3.4 SPA Refresh Routing Review

### [개념]

SPA Refresh Routing Review는 React Router 기반 SPA가 배포 환경에서 새로고침 또는 직접 URL 접근 시 정상적으로 index.html로 fallback 되는지 검토하는 과정이다.

개발 서버에서는 동작해도 운영 서버에서 fallback 설정이 없으면 404가 발생할 수 있다.

---

### [핵심]

SPA Refresh Routing Review 검토 항목:

- 직접 URL 접근 시 404가 발생하지 않는가?
- 새로고침 시 서버가 index.html을 반환하는가?
- 백엔드 통합 배포 시 forward 설정이 있는가?
- 정적 호스팅 rewrite 설정이 있는가?
- API path는 fallback 대상에서 제외되는가?
- asset path가 올바른가?
- basename 설정이 필요한가?
- BrowserRouter와 HashRouter 선택이 배포 환경과 맞는가?

---

### [실무]

문제 상황:

```text
사용자 /festivals/1 직접 접속
→ 서버가 /festivals/1 파일을 찾음
→ 404 반환
```

필요한 처리:

```text
SPA route 요청
→ 서버에서 index.html 반환
→ React Router가 클라이언트에서 route 해석
```

Spring Boot 통합 배포 개념:

```java
@Controller
public class SpaForwardController {

    @GetMapping(value = {
        "/{path:[^\\.]*}",
        "/**/{path:[^\\.]*}"
    })
    public String forward() {
        return "forward:/index.html";
    }
}
```

주의:

```text
API 경로까지 index.html로 forward하면 API 요청이 깨질 수 있음
→ /api prefix 또는 controller path 분리 필요
→ static asset 요청은 fallback 대상에서 제외해야 함
```

리뷰 코멘트 예:

```text
[High] BrowserRouter를 사용하는 SPA인데 운영 서버 fallback 설정이 확인되지 않습니다. 직접 URL 접근과 새로고침 시 404가 발생할 수 있으므로 index.html fallback 설정을 확인해야 합니다.
```

---

### [FAQ]

Q. SPA에서 새로고침하면 404가 나는 이유는?
A. 서버가 클라이언트 route를 실제 파일 경로로 찾기 때문이다. index.html fallback 설정이 필요하다.

Q. 개발 서버에서는 되는데 배포 후 안 되는 이유는?
A. 개발 서버는 fallback을 자동 처리하지만 운영 서버는 별도 rewrite 또는 forward 설정이 필요할 수 있다.

Q. API path도 index.html로 forward하면 돼?
A. 안 된다. API 요청은 백엔드 controller로 가야 하므로 fallback 대상에서 제외해야 한다.

Q. HashRouter를 쓰면 새로고침 문제가 없어져?
A. 대부분 줄어들지만 URL에 #이 포함된다. 운영 환경 요구사항에 맞게 선택해야 한다.

---

# 4. Form Auth Routing Review Checklist

## 4.1 Form Review Checklist

### [개념]

Form Review Checklist는 Review Agent가 프론트엔드 form 구현을 검토할 때 사용하는 최종 점검 목록이다.

입력 구조, validation, 제출 안정성, 파일 업로드, 에러 표시를 빠르게 검토한다.

---

### [핵심]

Form Review Checklist:

```md
## Structure

- [ ] form 태그를 사용하는가?
- [ ] onSubmit으로 제출을 처리하는가?
- [ ] Enter 제출이 가능한가?
- [ ] input에 label이 연결되어 있는가?
- [ ] input name이 명확한가?
- [ ] button type이 명시되어 있는가?
- [ ] placeholder를 label 대체로 사용하지 않는가?

## Controlled Input

- [ ] value와 onChange가 함께 있는가?
- [ ] 초기값이 undefined가 아닌가?
- [ ] checkbox는 checked를 사용하는가?
- [ ] controlled / uncontrolled warning 위험이 없는가?

## Validation

- [ ] required field 검증이 있는가?
- [ ] email, password, 숫자, 날짜 등 형식 검증이 있는가?
- [ ] submit 전 validation이 실행되는가?
- [ ] validation 실패 시 API 요청을 막는가?
- [ ] field별 error가 표시되는가?
- [ ] 서버 validation error가 표시되는가?

## Submit

- [ ] preventDefault 처리가 있는가?
- [ ] 중복 제출이 방지되는가?
- [ ] 제출 중 button disabled 처리가 있는가?
- [ ] 실패 후 입력값이 유지되는가?
- [ ] finally에서 submitting 상태가 종료되는가?

## File Upload

- [ ] 허용 확장자를 제한하는가?
- [ ] 파일 크기 제한이 있는가?
- [ ] 파일 개수 제한이 있는가?
- [ ] 미리보기 URL cleanup이 있는가?
- [ ] 업로드 실패 처리가 있는가?
```

---

### [실무]

Form Review 우선순위:

```text
Submit Blocking Bug
→ Duplicate Submit
→ Missing Validation
→ Server Error Mapping
→ Accessibility Label
→ Controlled Input Warning
→ File Upload Risk
```

우선순위 판단:

```text
중복 저장 / 중복 결제 가능
→ High 또는 Critical

필수 validation 누락
→ High

서버 validation error 미표시
→ High 또는 Medium

label 누락
→ Medium

button type 누락
→ Medium 또는 Low

파일 검증 누락
→ High
```

---

### [FAQ]

Q. Form Review에서 가장 먼저 볼 것은 뭐야?
A. 제출 흐름, 중복 제출 방지, validation, 서버 error 표시를 먼저 본다.

Q. label 누락은 어떤 우선순위야?
A. 접근성에 영향을 주므로 보통 Medium으로 볼 수 있다.

Q. button type 누락은 어떤 문제야?
A. form 내부에서 의도치 않은 submit을 만들 수 있다.

Q. 파일 업로드 검증 누락은 어떤 우선순위야?
A. 보안과 성능 위험이 있어 High로 판단할 수 있다.

---

## 4.2 Authentication Review Checklist

### [개념]

Authentication Review Checklist는 Review Agent가 로그인, 로그아웃, token, protected route, 권한 UI를 검토할 때 사용하는 최종 점검 목록이다.

인증 흐름은 주요 사용자 흐름과 보안 위험에 직접 연결되므로 High Priority 중심으로 검토한다.

---

### [핵심]

Authentication Review Checklist:

```md
## Login

- [ ] 로그인 API 요청이 올바른가?
- [ ] 로그인 실패 메시지가 표시되는가?
- [ ] 로그인 성공 후 token이 저장되는가?
- [ ] 로그인 성공 후 사용자 상태가 갱신되는가?
- [ ] 로그인 성공 후 redirect가 적절한가?

## Token

- [ ] token 저장 위치가 보안 요구사항에 맞는가?
- [ ] token이 console에 출력되지 않는가?
- [ ] token이 URL query string에 노출되지 않는가?
- [ ] Authorization header가 필요한 요청에만 포함되는가?
- [ ] logout 시 token이 제거되는가?

## Refresh

- [ ] 401 발생 시 refresh 흐름이 있는가?
- [ ] refresh 성공 후 원래 요청을 재시도하는가?
- [ ] refresh 실패 시 logout 처리하는가?
- [ ] refresh 무한 retry를 방지하는가?
- [ ] refresh 중복 요청 위험이 없는가?

## Protected Route

- [ ] 인증 필요 페이지가 보호되는가?
- [ ] auth loading 중 잘못 redirect하지 않는가?
- [ ] 비로그인 접근 시 로그인 페이지로 이동하는가?
- [ ] 로그인 후 원래 페이지 복귀가 가능한가?
- [ ] 권한별 route 보호가 있는가?

## Authorization UI

- [ ] 관리자 메뉴가 권한 사용자에게만 보이는가?
- [ ] 수정 / 삭제 버튼이 권한 사용자에게만 보이는가?
- [ ] 403 응답을 사용자에게 안내하는가?
- [ ] UI 제한만으로 권한 검증을 대체하지 않는가?
```

---

### [실무]

Authentication Review 우선순위:

```text
Login Blocking
→ Token Exposure
→ Protected Route Missing
→ 401 Handling Missing
→ Logout Incomplete
→ Authorization UI Mismatch
→ Role Naming Inconsistency
```

우선순위 판단:

```text
로그인 불가
→ Critical

token URL 노출
→ Critical

token console 출력
→ High

Protected Route 누락
→ High

401 처리 누락
→ High

logout 시 token 미삭제
→ High

권한 UI 불일치
→ High 또는 Medium
```

---

### [FAQ]

Q. Authentication Review에서 가장 위험한 문제는 뭐야?
A. 로그인 불가, token 노출, Protected Route 누락, 401 처리 누락, logout 미완료다.

Q. token console 출력은 어떤 우선순위야?
A. 보통 High 이상이다. 운영 코드에 남으면 보안 위험이다.

Q. Protected Route 누락은 어떤 우선순위야?
A. 인증이 필요한 주요 페이지라면 High로 판단할 수 있다.

Q. logout 시 token을 안 지우면 어떤 문제야?
A. 로그아웃 후에도 인증 API가 호출되거나 사용자 상태가 남아 보안과 UX 문제가 생긴다.

---

## 4.3 Routing Review Checklist

### [개념]

Routing Review Checklist는 Review Agent가 React Router 경로 구조, navigation, route param, SPA refresh fallback을 검토할 때 사용하는 최종 점검 목록이다.

Routing 문제는 개발 환경에서는 숨겨졌다가 배포 후 직접 URL 접근, 새로고침, 인증 이동에서 자주 드러난다.

---

### [핵심]

Routing Review Checklist:

```md
## Route Structure

- [ ] route path가 명확한가?
- [ ] dynamic route가 적절한가?
- [ ] NotFound route가 있는가?
- [ ] 인증 route와 공개 route가 구분되는가?
- [ ] 관리자 route가 분리되어 있는가?
- [ ] API path와 frontend route path가 충돌하지 않는가?

## Navigation

- [ ] 내부 이동에 Link 또는 navigate를 사용하는가?
- [ ] 외부 이동에는 a 태그를 사용하는가?
- [ ] button과 link 역할이 구분되는가?
- [ ] redirect 후 replace 필요 여부를 고려하는가?
- [ ] target="\_blank" 외부 링크에 rel 설정이 있는가?

## Route Param

- [ ] useParams 이름이 route param과 일치하는가?
- [ ] param undefined 처리가 있는가?
- [ ] 숫자 param 변환이 필요한 경우 처리하는가?
- [ ] param 변경 시 API 요청이 다시 실행되는가?
- [ ] 404 응답을 Not Found UI로 처리하는가?

## SPA Refresh

- [ ] 직접 URL 접근 시 404가 발생하지 않는가?
- [ ] 운영 서버 index.html fallback 설정이 있는가?
- [ ] API path는 fallback 대상에서 제외되는가?
- [ ] asset path와 basename 설정이 배포 환경과 맞는가?
```

---

### [실무]

Routing Review 우선순위:

```text
SPA Refresh 404
→ Protected Route Missing
→ Route Param API Bug
→ NotFound Missing
→ Navigation Full Reload
→ External Link rel Missing
```

우선순위 판단:

```text
배포 후 직접 URL 접근 404
→ High

route param 불일치로 상세 조회 실패
→ High

Protected Route 누락
→ High

NotFound route 누락
→ Medium

내부 이동 a 태그 사용
→ Low 또는 Medium

외부 링크 rel 누락
→ Medium
```

---

### [FAQ]

Q. Routing Review에서 가장 먼저 볼 것은 뭐야?
A. 직접 URL 접근, Protected Route, route param, NotFound route, API path 충돌 여부를 먼저 본다.

Q. 배포 후 새로고침 404는 어떤 우선순위야?
A. 주요 페이지 접근을 막으므로 High로 판단할 수 있다.

Q. route param 이름 불일치는 어떤 문제야?
A. API 요청에 undefined가 들어가거나 상세 데이터 조회가 실패할 수 있다.

Q. 내부 이동에 a 태그를 쓰면 어떤 문제야?
A. SPA 전체 새로고침이 발생해 상태가 초기화되고 UX가 끊길 수 있다.

---

# Retrieval Queries

### [FAQ]

Q. Form Structure Review는 뭐야?
A. 프론트엔드 입력 폼이 의미 있는 HTML 구조, 접근성, 제출 흐름을 갖추었는지 검토하는 과정이다.

Q. form 태그 없이 div로 만들어도 돼?
A. 가능은 하지만 Enter 제출, 접근성, 브라우저 기본 동작을 고려하면 form 태그가 적합하다.

Q. placeholder를 label 대신 써도 돼?
A. 권장하지 않는다. placeholder는 입력하면 사라지고 스크린 리더 접근성도 떨어질 수 있다.

Q. button type은 꼭 써야 해?
A. form 내부에서는 반드시 명시하는 것이 좋다. 기본 submit 동작 때문에 의도치 않은 제출이 발생할 수 있다.

Q. Controlled Input은 뭐야?
A. input 값을 React state로 관리하고 value와 onChange를 연결하는 방식이다.

Q. input 초기값이 undefined면 문제야?
A. controlled / uncontrolled 전환 warning이 발생할 수 있으므로 빈 문자열 등 안전한 기본값을 사용하는 것이 좋다.

Q. checkbox는 value로 관리해?
A. 아니다. checkbox는 checked와 event.target.checked를 사용하는 것이 적절하다.

Q. Form Validation Review는 뭐야?
A. 사용자 입력값이 제출 전 프론트엔드에서 적절히 검증되고 서버 validation error도 처리되는지 검토하는 과정이다.

Q. 프론트엔드 validation만 있으면 충분해?
A. 아니다. 프론트엔드 검증은 우회 가능하므로 백엔드 validation이 반드시 필요하다.

Q. 서버 validation error도 화면에 보여줘야 해?
A. 보여줘야 한다. 중복 이메일, 권한 없음, 비밀번호 불일치 같은 서버 판단 결과는 사용자에게 필요하다.

Q. Form Submit Review는 뭐야?
A. form 제출 흐름이 안정적으로 처리되고 중복 제출, 무한 loading, 입력값 손실, 에러 누락이 없는지 검토하는 과정이다.

Q. 제출 버튼을 여러 번 누르면 왜 문제야?
A. 중복 API 요청, 중복 저장, 중복 결제 같은 문제가 발생할 수 있다.

Q. submit 중에는 버튼을 disabled 해야 해?
A. 그렇다. 중복 제출을 막기 위해 필요하다.

Q. 제출 실패 시 입력값을 지워도 돼?
A. 권장하지 않는다. 사용자가 다시 입력하지 않도록 기존 입력값을 유지하는 것이 좋다.

Q. File Upload Form Review는 뭐야?
A. 파일 업로드 입력이 확장자, 크기, 개수, 미리보기, 진행 상태, 실패 처리 기준을 만족하는지 검토하는 과정이다.

Q. 프론트엔드 파일 검증만 있으면 충분해?
A. 아니다. 프론트엔드 검증은 우회 가능하므로 서버에서도 반드시 검증해야 한다.

Q. 이미지 미리보기 URL은 정리해야 해?
A. 그렇다. URL.createObjectURL을 사용했다면 URL.revokeObjectURL로 정리하는 것이 좋다.

Q. Auth Flow Review는 뭐야?
A. 로그인, 로그아웃, 토큰 저장, 인증 상태 복원, 인증 만료, 권한별 접근이 올바르게 처리되는지 검토하는 과정이다.

Q. 로그인 성공 후 토큰만 저장하면 끝이야?
A. 아니다. 사용자 상태 갱신, 인증 header 설정, redirect, 만료 처리까지 확인해야 한다.

Q. 새로고침하면 로그인이 풀리는 이유는?
A. 토큰 저장 방식과 인증 상태 복원 로직이 없기 때문일 수 있다.

Q. Token Storage Review는 뭐야?
A. Access Token과 Refresh Token을 어디에 저장하고 어떻게 사용하는지 검토하는 과정이다.

Q. JWT를 localStorage에 저장해도 돼?
A. 가능은 하지만 XSS 위험이 있다. 보안 요구사항이 높다면 httpOnly Cookie 방식도 검토해야 한다.

Q. Access Token을 console.log로 찍어도 돼?
A. 권장하지 않는다. 운영 코드에 남으면 보안 위험이다.

Q. token을 URL query string에 넣어도 돼?
A. 안 된다. 브라우저 기록, 서버 로그, referrer에 노출될 수 있어 위험하다.

Q. logout 시 무엇을 해야 해?
A. token 제거, 사용자 상태 초기화, 필요 시 서버 logout API 호출, 로그인 페이지 이동을 처리한다.

Q. Refresh Token Review는 뭐야?
A. Access Token 만료 시 사용자 흐름을 끊지 않고 안전하게 token을 갱신하는지 검토하는 과정이다.

Q. 401이 발생하면 무조건 로그인 페이지로 보내야 해?
A. refresh token 정책이 있다면 먼저 token 갱신을 시도할 수 있다. refresh 실패 시 로그인 이동이 적절하다.

Q. refresh 요청이 여러 번 동시에 발생하면 문제야?
A. 문제다. 중복 refresh로 race condition과 token 불일치가 발생할 수 있다.

Q. Protected Route Review는 뭐야?
A. 인증이 필요한 페이지에 비로그인 사용자가 접근하지 못하도록 route 수준에서 보호하는지 검토하는 과정이다.

Q. Protected Route만 있으면 보안이 충분해?
A. 아니다. 프론트엔드 route 보호는 UX 목적이고 실제 권한 검증은 백엔드에서 반드시 해야 한다.

Q. 인증 확인 중 로그인 페이지로 튕기는 이유는?
A. auth loading 상태를 고려하지 않으면 새로고침 직후 잘못 redirect될 수 있다.

Q. Authorization UI Review는 뭐야?
A. 사용자 권한에 따라 버튼, 메뉴, 링크, 페이지 접근 UI가 적절히 표시되는지 검토하는 과정이다.

Q. 권한 버튼을 숨기면 보안이 되는 거야?
A. 아니다. UI 제한은 UX 목적이고 실제 권한 검증은 백엔드에서 해야 한다.

Q. Route Structure Review는 뭐야?
A. React Router 기반 페이지 경로가 명확하고 유지보수 가능하며 API path와 충돌하지 않는지 검토하는 과정이다.

Q. NotFoundPage가 꼭 필요해?
A. 권장된다. 잘못된 URL에 대해 사용자가 이해할 수 있는 화면을 제공해야 한다.

Q. API path와 frontend route가 같아도 돼?
A. 권장하지 않는다. API는 `/api` prefix로 분리하는 것이 안전하다.

Q. Navigation Review는 뭐야?
A. 페이지 이동 방식이 SPA 특성과 사용자 경험에 맞는지 검토하는 과정이다.

Q. 내부 페이지 이동에 a 태그를 써도 돼?
A. 가능하지만 SPA에서는 전체 새로고침이 발생할 수 있으므로 React Router의 Link를 권장한다.

Q. button과 Link는 어떻게 구분해?
A. 페이지 이동이면 Link, 현재 화면에서 동작을 수행하면 button을 사용한다.

Q. Route Param Review는 뭐야?
A. URL path parameter를 안전하게 읽고 검증한 뒤 API 요청과 화면 렌더링에 사용하는지 검토하는 과정이다.

Q. useParams 값은 숫자야 문자열이야?
A. React Router의 route param은 문자열로 들어온다. 숫자가 필요하면 변환해야 한다.

Q. SPA Refresh Routing Review는 뭐야?
A. React Router 기반 SPA가 배포 환경에서 새로고침 또는 직접 URL 접근 시 정상적으로 index.html로 fallback 되는지 검토하는 과정이다.

Q. SPA에서 새로고침하면 404가 나는 이유는?
A. 서버가 클라이언트 route를 실제 파일 경로로 찾기 때문이다. index.html fallback 설정이 필요하다.

Q. API path도 index.html로 forward하면 돼?
A. 안 된다. API 요청은 백엔드 controller로 가야 하므로 fallback 대상에서 제외해야 한다.

Q. Form Auth Routing Review의 최종 목적은 뭐야?
A. 입력, 인증, 권한, 페이지 이동 흐름이 사용자가 실제로 안정적으로 사용할 수 있는 수준인지 판단하는 것이다.
