# Frontend Code Review Part04 - API Integration and UX State Review

---

# 1. API Integration Review Rules

## 1.1 API Module Review

### [개념]

API Module Review는 프론트엔드 API 호출 코드가 컴포넌트 내부에 흩어지지 않고 일관된 모듈 구조로 분리되어 있는지 검토하는 과정이다.

API 호출이 컴포넌트에 직접 섞이면 endpoint 변경, 인증 header 변경, 에러 처리 변경, baseURL 변경 시 수정 범위가 커진다.

Review Agent는 API 호출 코드가 재사용 가능하고 테스트 가능한 구조인지 검토해야 한다.

---

### [핵심]

API Module Review 검토 항목:

- API 호출 코드가 컴포넌트에 과도하게 섞이지 않았는가?
- Axios instance 또는 fetch wrapper가 있는가?
- baseURL이 환경 변수로 분리되어 있는가?
- 인증 header 처리가 일관적인가?
- public API와 private API가 구분되는가?
- endpoint naming이 명확한가?
- API 함수 이름이 도메인과 동작을 표현하는가?
- 공통 error handling 전략이 있는가?
- response data 접근 방식이 일관적인가?
- API module이 테스트에서 mock 가능한가?

권장 구조:

```text
src/
├─ api/
│  ├─ axiosInstance.js
│  ├─ publicApi.js
│  ├─ authApi.js
│  ├─ festivalApi.js
│  ├─ reviewApi.js
│  └─ notificationApi.js
```

---

### [실무]

API module 예:

```js
export const festivalApi = {
  getFestivalDetail: (festivalId) => {
    return api.get(`/festivals/${festivalId}`);
  },

  searchFestivals: (params) => {
    return api.get("/festivals/search", { params });
  },

  createReview: (festivalId, payload) => {
    return api.post(`/festivals/${festivalId}/reviews`, payload);
  },
};
```

나쁜 예:

```jsx
function FestivalDetailPage() {
  useEffect(() => {
    axios
      .get("http://localhost:8080/festivals/1")
      .then((response) => setFestival(response.data));
  }, []);
}
```

문제:

```text
컴포넌트 내부에 endpoint, baseURL, axios 직접 호출이 섞임
→ 환경 변경 대응 어려움
→ 테스트 mock 어려움
→ 중복 코드 증가
```

리뷰 코멘트 예:

```text
[Medium] 컴포넌트 내부에서 axios.get을 직접 호출하고 있습니다. endpoint와 baseURL 변경 영향을 줄이기 위해 festivalApi 같은 API module로 분리하는 것이 좋습니다.
```

---

### [FAQ]

Q. API Module Review는 왜 필요해?
A. API 호출을 일관된 구조로 분리해야 endpoint 변경, 인증 처리, 테스트 mock, 에러 처리가 쉬워지기 때문이다.

Q. 컴포넌트 안에서 axios.get을 바로 써도 돼?
A. 작은 코드에서는 가능하지만 API가 늘어나면 API module로 분리하는 것이 유지보수에 좋다.

Q. API 함수 이름은 어떻게 지어야 해?
A. getFestivalDetail, searchFestivals, createReview처럼 동작과 도메인이 드러나야 한다.

Q. public API와 private API는 왜 구분해?
A. 인증 header가 필요한 요청과 필요 없는 요청을 분리해야 인증 누락이나 불필요한 token 전송을 줄일 수 있다.

---

## 1.2 Axios Instance Review

### [개념]

Axios Instance Review는 Axios instance가 baseURL, timeout, header, interceptor, error handling을 일관되게 관리하는지 검토하는 과정이다.

Axios instance가 없으면 각 API 호출마다 baseURL, Authorization header, error handling이 반복되어 버그 위험이 커진다.

---

### [핵심]

Axios Instance Review 검토 항목:

- baseURL이 환경 변수로 관리되는가?
- timeout이 설정되어 있는가?
- Content-Type 설정이 적절한가?
- Authorization header가 필요한 요청에만 포함되는가?
- request interceptor가 token을 안전하게 주입하는가?
- response interceptor가 401 / 403 / 500을 적절히 처리하는가?
- public instance와 private instance가 구분되는가?
- refresh token 흐름이 중복 요청을 만들지 않는가?
- interceptor에서 무한 retry가 발생하지 않는가?
- logout 시 token이 제거되는가?

---

### [실무]

권장 구조 예:

```js
const api = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
  timeout: 10000,
});

api.interceptors.request.use((config) => {
  const accessToken = getAccessToken();

  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }

  return config;
});
```

public / private 분리 예:

```js
export const publicApi = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
  timeout: 10000,
});

export const privateApi = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
  timeout: 10000,
});
```

리뷰 코멘트 예:

```text
[High] 인증이 필요한 API와 공개 API가 같은 Axios instance를 사용하고 있어 모든 요청에 Authorization header가 포함될 수 있습니다. publicApi와 privateApi를 분리하는 것이 좋습니다.
```

---

### [FAQ]

Q. Axios instance는 왜 필요해?
A. baseURL, timeout, header, interceptor를 한 곳에서 관리해 API 호출 일관성을 유지하기 위해 필요하다.

Q. timeout 설정은 꼭 필요해?
A. 권장된다. timeout이 없으면 네트워크 문제에서 사용자가 무한 loading 상태를 볼 수 있다.

Q. 모든 요청에 Authorization header를 붙여도 돼?
A. 권장하지 않는다. 공개 API와 인증 API를 구분해 필요한 요청에만 token을 보내는 것이 좋다.

Q. interceptor에서 가장 주의할 점은 뭐야?
A. 401 처리 중 무한 retry, token 갱신 중복 요청, logout 처리 누락을 주의해야 한다.

---

## 1.3 API Endpoint Review

### [개념]

API Endpoint Review는 프론트엔드에서 호출하는 endpoint가 백엔드 API 명세와 일치하는지 검토하는 과정이다.

endpoint 오타, prefix 불일치, path variable 누락, query parameter 이름 불일치는 기능 실패의 주요 원인이다.

---

### [핵심]

API Endpoint Review 검토 항목:

- backend route와 frontend endpoint가 일치하는가?
- `/api` prefix 정책이 일관적인가?
- path variable 이름과 위치가 맞는가?
- query parameter 이름이 백엔드 DTO와 맞는가?
- HTTP method가 맞는가?
- trailing slash 정책이 일관적인가?
- 인증 필요 endpoint와 공개 endpoint 구분이 맞는가?
- route path와 API path가 충돌하지 않는가?
- mock endpoint가 운영 코드에 남아 있지 않은가?
- localhost 또는 임시 URL이 남아 있지 않은가?

---

### [실무]

검토 예:

```text
Backend:
GET /calendar/monthly?targetMonth=2026-07

Frontend:
calendarApi.getMonthlyFestivals(targetMonth)
→ publicApi.get("/calendar/monthly", { params: { targetMonth } })
```

path variable 예:

```text
Backend:
GET /festivals/{festivalId}

Frontend:
festivalApi.getFestivalDetail(festivalId)
→ api.get(`/festivals/${festivalId}`)
```

잘못된 예:

```js
api.get(`/festival/detail/${id}`);
```

문제:

```text
백엔드 명세가 /festivals/{festivalId}인데 프론트는 /festival/detail/{id} 호출
→ 404 발생 가능
```

리뷰 코멘트 예:

```text
[High] 축제 상세 API endpoint가 백엔드 명세와 다릅니다. `/festival/detail/${id}`가 아니라 `/festivals/${festivalId}` 형식인지 확인해야 합니다.
```

---

### [FAQ]

Q. API Endpoint Review는 왜 중요해?
A. endpoint 불일치가 있으면 코드 구조가 맞아도 API 요청이 실패하기 때문이다.

Q. API path와 frontend route path가 같아도 돼?
A. 권장하지 않는다. API는 `/api` prefix 등으로 분리해 SPA route와 충돌을 줄이는 것이 좋다.

Q. query parameter 이름도 리뷰해야 해?
A. 해야 한다. 백엔드 DTO 또는 Controller parameter 이름과 다르면 필터나 검색이 동작하지 않을 수 있다.

Q. HTTP method 불일치는 어떤 문제야?
A. GET / POST / PUT / DELETE가 다르면 405 또는 의도치 않은 서버 동작이 발생할 수 있다.

---

## 1.4 API Response Mapping Review

### [개념]

API Response Mapping Review는 백엔드 응답 구조를 프론트엔드가 올바르게 해석하고 화면 상태로 변환하는지 검토하는 과정이다.

response.data 구조를 잘못 이해하면 undefined 접근, 빈 화면, 잘못된 렌더링이 발생한다.

---

### [핵심]

API Response Mapping Review 검토 항목:

- response wrapper 구조를 이해하고 있는가?
- response.data와 response.data.data 구분이 맞는가?
- list response와 page response 구조가 맞는가?
- Slice / Page 응답 필드가 올바르게 매핑되는가?
- optional field를 안전하게 처리하는가?
- null 응답에 fallback UI가 있는가?
- status / message / data 구조가 일관적으로 처리되는가?
- 날짜 / 숫자 / enum 값 변환이 필요한가?
- 화면에서 필요한 field가 존재하는지 확인하는가?

---

### [실무]

ApiResponse wrapper 예:

```json
{
  "success": true,
  "message": "조회 성공",
  "data": {
    "festivalId": 1,
    "title": "서울 축제"
  }
}
```

올바른 접근:

```js
const response = await festivalApi.getFestivalDetail(festivalId);
setFestival(response.data.data);
```

잘못된 접근:

```js
setFestival(response.data);
```

문제:

```text
festival.title 접근 시 실제 title은 response.data.data.title에 있음
→ 화면에 undefined 표시 또는 런타임 오류 가능
```

Page response 예:

```text
content
totalElements
totalPages
number
size
first
last
```

Slice response 예:

```text
content
number
size
first
last
hasNext
```

리뷰 코멘트 예:

```text
[High] API 응답이 ApiResponse wrapper 구조인데 response.data를 그대로 화면 state에 저장하고 있습니다. 실제 데이터는 response.data.data에 있으므로 mapping을 수정해야 합니다.
```

---

### [FAQ]

Q. API Response Mapping Review는 왜 필요해?
A. 백엔드 응답 구조를 잘못 해석하면 undefined 접근, 빈 화면, 잘못된 렌더링이 발생하기 때문이다.

Q. response.data와 response.data.data는 왜 헷갈려?
A. Axios의 response.data와 백엔드 ApiResponse의 data field가 중첩되기 때문이다.

Q. Page와 Slice 응답은 다르게 처리해야 해?
A. 그렇다. Page는 total count 정보가 있고 Slice는 hasNext 중심으로 무한 스크롤에 적합하다.

Q. optional field는 어떻게 처리해야 해?
A. optional chaining, fallback UI, 기본값을 사용해 null / undefined 접근 오류를 막아야 한다.

---

# 2. API Error Review Rules

## 2.1 API Error Handling Review

### [개념]

API Error Handling Review는 API 실패 상황을 코드와 UI가 적절히 처리하는지 검토하는 과정이다.

프론트엔드에서 API 에러를 console.log만 처리하면 사용자는 실패 원인과 다음 행동을 알 수 없다.

---

### [핵심]

API Error Handling Review 검토 항목:

- try / catch 또는 error boundary가 있는가?
- 사용자에게 에러 메시지가 표시되는가?
- 400 / 401 / 403 / 404 / 409 / 500 처리가 구분되는가?
- 네트워크 실패 처리가 있는가?
- timeout 처리가 있는가?
- Loading이 종료되는가?
- 실패 후 복구 행동이 있는가?
- 재시도 버튼이 필요한가?
- 서버 validation error가 표시되는가?
- raw error 또는 민감 정보가 사용자에게 노출되지 않는가?

---

### [실무]

기본 예:

```js
try {
  const response = await festivalApi.getFestivalDetail(festivalId);
  setFestival(response.data.data);
} catch (error) {
  setError("축제 정보를 불러오지 못했습니다.");
} finally {
  setIsLoading(false);
}
```

나쁜 예:

```js
festivalApi
  .getFestivalDetail(festivalId)
  .then((response) => setFestival(response.data.data))
  .catch((error) => console.log(error));
```

문제:

```text
사용자에게 실패 상태가 표시되지 않음
→ 빈 화면 또는 이전 데이터 유지
→ 복구 행동 없음
```

리뷰 코멘트 예:

```text
[High] API 실패 시 console.log만 실행되고 화면에는 에러 상태가 표시되지 않습니다. 사용자 친화 메시지와 재시도 동작을 추가해야 합니다.
```

---

### [FAQ]

Q. API 에러는 console.log만 해도 돼?
A. 안 된다. 사용자에게 실패 상태와 복구 방법을 제공해야 한다.

Q. API 실패 처리가 없으면 어떤 우선순위야?
A. 주요 사용자 흐름이면 High로 판단할 수 있다.

Q. raw error를 화면에 보여줘도 돼?
A. 권장하지 않는다. 사용자 친화 메시지로 바꾸고 민감 정보는 노출하지 않아야 한다.

Q. finally에서 loading을 종료해야 해?
A. 그렇다. 성공과 실패 모두 loading이 종료되어야 무한 loading을 막을 수 있다.

---

## 2.2 HTTP Status Error Review

### [개념]

HTTP Status Error Review는 API 실패 status code에 따라 적절한 사용자 안내와 복구 흐름을 제공하는지 검토하는 과정이다.

모든 에러를 동일하게 처리하면 인증 만료, 권한 없음, 데이터 없음, 서버 장애를 구분할 수 없다.

---

### [핵심]

Status별 처리 기준:

| Status        | 의미             | UI 처리                         |
| ------------- | ---------------- | ------------------------------- |
| 400           | 잘못된 요청      | 입력값 확인 안내                |
| 401           | 인증 필요 / 만료 | 토큰 갱신 또는 로그인 이동      |
| 403           | 권한 없음        | 접근 불가 메시지                |
| 404           | 데이터 없음      | Not Found 또는 Empty 안내       |
| 409           | 충돌             | 중복 데이터 또는 상태 충돌 안내 |
| 422           | validation 실패  | 필드별 오류 표시                |
| 500           | 서버 오류        | 잠시 후 재시도 안내             |
| Network Error | 연결 실패        | 네트워크 확인 안내              |
| Timeout       | 응답 지연        | 재시도 안내                     |

---

### [실무]

status mapping 예:

```js
function getErrorMessage(error) {
  const status = error.response?.status;

  if (status === 400) return "요청 정보를 확인해 주세요.";
  if (status === 401) return "로그인이 필요합니다.";
  if (status === 403) return "접근 권한이 없습니다.";
  if (status === 404) return "요청한 데이터를 찾을 수 없습니다.";
  if (status >= 500)
    return "서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.";

  return "알 수 없는 오류가 발생했습니다.";
}
```

리뷰 코멘트 예:

```text
[Medium] 모든 API 에러가 동일한 메시지로 표시됩니다. 401, 403, 404, 500은 사용자의 다음 행동이 다르므로 status별 메시지 처리를 검토하는 것이 좋습니다.
```

---

### [FAQ]

Q. 모든 API 에러를 같은 메시지로 처리해도 돼?
A. 가능은 하지만 권장하지 않는다. 인증, 권한, 데이터 없음, 서버 오류는 사용자 행동이 다르다.

Q. 401 에러는 어떻게 처리해야 해?
A. 인증 만료로 보고 refresh token 처리 또는 로그인 페이지 이동을 고려한다.

Q. 403은 어떻게 처리해야 해?
A. 권한 없음 메시지를 보여주고 접근 가능한 페이지로 이동할 수 있게 한다.

Q. 404는 항상 에러야?
A. 상황에 따라 Not Found 상태로 사용자에게 안내해야 하는 정상 흐름일 수 있다.

---

## 2.3 Validation Error Review

### [개념]

Validation Error Review는 서버에서 반환한 validation error가 사용자가 이해할 수 있는 형태로 화면에 표시되는지 검토하는 과정이다.

프론트엔드 validation은 우회 가능하므로 서버 validation 결과를 반드시 처리해야 한다.

---

### [핵심]

Validation Error Review 검토 항목:

- 서버 validation error를 catch하는가?
- field별 error message를 표시하는가?
- global error와 field error를 구분하는가?
- 사용자가 어떤 입력을 수정해야 하는지 알 수 있는가?
- 실패 후 입력값이 유지되는가?
- error message가 input과 시각적으로 연결되는가?
- 접근성 관점에서 error role 또는 aria 연결을 고려하는가?
- raw validation payload를 그대로 노출하지 않는가?

---

### [실무]

서버 validation 응답 예:

```json
{
  "success": false,
  "message": "Validation failed",
  "errors": {
    "email": "올바른 이메일 형식이 아닙니다.",
    "password": "비밀번호는 8자 이상이어야 합니다."
  }
}
```

field error mapping 예:

```js
try {
  await authApi.signUp(formValues);
} catch (error) {
  const fieldErrors = error.response?.data?.errors;

  if (fieldErrors) {
    setErrors(fieldErrors);
    return;
  }

  setGlobalError("회원가입에 실패했습니다.");
}
```

리뷰 코멘트 예:

```text
[High] 회원가입 실패 시 서버 validation error를 화면에 표시하지 않아 사용자가 어떤 입력을 수정해야 하는지 알 수 없습니다. field별 error mapping을 추가해야 합니다.
```

---

### [FAQ]

Q. 프론트엔드 validation이 있으면 서버 validation error 처리가 없어도 돼?
A. 안 된다. 프론트엔드 validation은 우회 가능하므로 서버 validation 결과도 반드시 처리해야 한다.

Q. field별 error는 왜 필요해?
A. 사용자가 어떤 입력값을 수정해야 하는지 즉시 알 수 있기 때문이다.

Q. validation 실패 후 입력값을 지워도 돼?
A. 권장하지 않는다. 사용자가 다시 입력하지 않도록 기존 입력값을 유지하는 것이 좋다.

Q. 서버 error payload를 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자 친화 메시지로 변환해야 한다.

---

## 2.4 Network and Timeout Error Review

### [개념]

Network and Timeout Error Review는 인터넷 연결 문제, 서버 응답 지연, CORS 실패, timeout 상황에서 사용자가 적절한 안내를 받는지 검토하는 과정이다.

네트워크 문제는 status code가 없을 수 있으므로 일반 HTTP error와 별도로 처리해야 한다.

---

### [핵심]

검토 항목:

- error.response가 없는 경우를 처리하는가?
- Network Error 메시지가 있는가?
- timeout 발생 시 안내가 있는가?
- CORS 실패를 개발자 관점에서 확인할 수 있는가?
- 재시도 버튼이 있는가?
- loading이 종료되는가?
- offline 상태를 고려하는가?
- 중복 재시도로 서버 부하를 만들지 않는가?

---

### [실무]

network error 처리 예:

```js
function getApiErrorMessage(error) {
  if (error.code === "ECONNABORTED") {
    return "요청 시간이 초과되었습니다. 다시 시도해 주세요.";
  }

  if (!error.response) {
    return "네트워크 연결을 확인해 주세요.";
  }

  return getStatusErrorMessage(error.response.status);
}
```

리뷰 코멘트 예:

```text
[Medium] error.response.status에 바로 접근하고 있어 네트워크 실패 시 Cannot read properties of undefined 오류가 발생할 수 있습니다. error.response 존재 여부를 먼저 확인해야 합니다.
```

---

### [FAQ]

Q. Network Error는 HTTP status가 있어?
A. 없을 수 있다. 서버 응답 자체를 받지 못한 경우 error.response가 undefined일 수 있다.

Q. timeout 처리는 왜 필요해?
A. 사용자가 무한 loading 상태로 남지 않도록 요청 실패로 안내해야 하기 때문이다.

Q. CORS 에러도 사용자에게 자세히 보여줘야 해?
A. 사용자에게는 일반 연결 실패 메시지를 보여주고 개발자는 콘솔과 네트워크 탭에서 원인을 확인하는 것이 좋다.

Q. error.response.status에 바로 접근해도 돼?
A. 위험하다. 네트워크 실패에서는 error.response가 없을 수 있으므로 optional chaining이 필요하다.

---

# 3. Request Duplication Review Rules

## 3.1 Duplicate Request Review

### [개념]

Duplicate Request Review는 동일한 API 요청이 불필요하게 반복되는지 검토하는 과정이다.

중복 요청은 서버 부하, 중복 저장, 중복 결제, UI 깜빡임, 데이터 불일치를 만들 수 있다.

---

### [핵심]

중복 요청 원인:

- useEffect dependency 오류
- React StrictMode 개발 중 이중 실행
- 이벤트 핸들러 중복 바인딩
- submit 버튼 중복 클릭
- 페이지 진입 시 여러 컴포넌트에서 같은 요청
- cache 전략 없음
- debounce 누락
- pagination refetch 조건 오류
- interceptor retry 무한 반복
- polling cleanup 누락

---

### [실무]

Duplicate Request Review Flow:

```text
Network Tab Check
→ Same Endpoint Repetition Check
→ useEffect Dependency Check
→ Component Mount Position Check
→ Event Handler Binding Check
→ Submit Disabled Check
→ Cache / Query Key Check
→ StrictMode Distinction
→ Review Decision
```

중복 제출 방지:

```jsx
<button type="submit" disabled={isSubmitting}>
  {isSubmitting ? "저장 중..." : "저장"}
</button>
```

리뷰 코멘트 예:

```text
[High] 저장 버튼을 여러 번 클릭할 수 있어 동일한 POST 요청이 중복 전송됩니다. isSubmitting 상태로 버튼 disabled 처리를 추가해야 합니다.
```

---

### [FAQ]

Q. API가 두 번 호출되는 이유는 뭐야?
A. useEffect dependency 오류, StrictMode, 중복 mount, submit 중복 클릭, cache 미사용이 원인일 수 있다.

Q. React StrictMode 때문에 두 번 호출될 수 있어?
A. 개발 환경에서는 side effect 검출을 위해 일부 로직이 두 번 실행될 수 있다. 운영 동작과 구분해야 한다.

Q. 중복 요청은 어떤 우선순위야?
A. GET 중복은 Medium일 수 있지만 POST / 결제 / 저장 중복은 High 또는 Critical이 될 수 있다.

Q. 중복 제출은 어떻게 막아?
A. isSubmitting 상태를 두고 제출 중 버튼 disabled 처리와 handler guard를 함께 사용한다.

---

## 3.2 Search Request Debounce Review

### [개념]

Search Request Debounce Review는 검색 input 입력마다 API 요청이 과도하게 발생하지 않도록 debounce 또는 명시적 submit 전략을 사용하는지 검토하는 과정이다.

검색 요청이 매 key stroke마다 발생하면 서버 부하와 UI 깜빡임이 증가한다.

---

### [핵심]

검토 항목:

- input 변경마다 즉시 API 요청이 발생하지 않는가?
- debounce delay가 있는가?
- 검색 버튼 또는 Enter 제출 방식이 적절한가?
- 이전 요청 취소가 필요한가?
- 마지막 입력 기준 결과만 반영되는가?
- 빈 검색어 요청 정책이 명확한가?
- loading UI가 과도하게 깜빡이지 않는가?

---

### [실무]

debounce 적용 대상:

```text
실시간 검색
자동완성
필터 즉시 반영
주소 검색
사용자 검색
```

명시적 submit이 더 나은 경우:

```text
검색 조건이 많음
서버 부하가 큼
결과 페이지 이동이 필요함
정확한 submit 시점이 중요함
```

리뷰 코멘트 예:

```text
[Medium] 검색 input onChange마다 API 요청이 발생합니다. 실시간 검색이 요구사항이 아니라면 submit 방식으로 변경하거나 debounce를 적용하는 것이 좋습니다.
```

---

### [FAQ]

Q. 검색 input 변경마다 API를 호출해도 돼?
A. 가능하지만 서버 부하와 UX를 고려해 debounce 또는 명시적 submit 방식을 검토해야 한다.

Q. debounce는 언제 필요해?
A. 실시간 검색이나 자동완성처럼 입력 중 API 요청이 발생하는 경우 필요하다.

Q. 검색 버튼 방식이 더 좋은 경우도 있어?
A. 있다. 검색 조건이 많거나 서버 요청 비용이 크면 명시적 submit이 더 적합할 수 있다.

Q. 이전 검색 요청은 취소해야 해?
A. 빠른 입력으로 응답 순서가 바뀔 수 있으면 AbortController나 request id 방식으로 최신 요청만 반영해야 한다.

---

## 3.3 Race Condition Review

### [개념]

Race Condition Review는 여러 비동기 요청의 응답 순서가 예상과 달라져 오래된 데이터가 최신 데이터를 덮어쓰는지 검토하는 과정이다.

검색, 필터, 상세 이동, 자동완성에서 자주 발생한다.

---

### [핵심]

Race Condition 발생 상황:

- 검색어를 빠르게 변경
- filter를 빠르게 변경
- route param이 빠르게 변경
- 이전 요청이 늦게 응답
- 최신 요청보다 오래된 요청 결과가 나중에 반영
- 컴포넌트 unmount 후 state update
- pagination 요청 순서 꼬임

---

### [실무]

문제 예:

```text
keyword = "a" 요청
→ keyword = "ab" 요청
→ "ab" 응답 먼저 도착
→ 화면에 ab 결과 표시
→ "a" 응답 나중 도착
→ 화면이 a 결과로 덮어쓰기 됨
```

해결 전략:

```text
AbortController로 이전 요청 취소
request id로 최신 요청만 반영
React Query query key 사용
loading state와 current parameter 일치 확인
```

리뷰 코멘트 예:

```text
[Medium] 검색어 변경 시 이전 요청을 취소하지 않아 응답 순서가 바뀌면 오래된 검색 결과가 최신 결과를 덮어쓸 수 있습니다. AbortController 또는 최신 request id 검사를 검토해야 합니다.
```

---

### [FAQ]

Q. Race Condition은 언제 생겨?
A. 여러 비동기 요청이 동시에 진행되고 응답 순서가 보장되지 않을 때 발생한다.

Q. 검색 기능에서 Race Condition이 왜 문제야?
A. 오래된 검색 결과가 최신 검색 결과를 덮어써 사용자에게 잘못된 결과를 보여줄 수 있다.

Q. Race Condition은 어떻게 막아?
A. 이전 요청 취소, 최신 request id 확인, query key 기반 server state 도구 사용으로 줄일 수 있다.

Q. 모든 API 요청에 AbortController가 필요해?
A. 아니다. 빠르게 조건이 바뀌는 검색, 필터, route param 기반 요청에서 특히 유용하다.

---

# 4. Loading State Review Rules

## 4.1 Loading State Review

### [개념]

Loading State Review는 API 요청 중 사용자가 대기 상태를 이해할 수 있도록 loading UI가 제공되는지 검토하는 과정이다.

loading 처리가 없으면 사용자는 화면이 멈췄는지, 요청이 진행 중인지 알 수 없다.

---

### [핵심]

Loading State Review 검토 항목:

- 초기 로딩 표시가 있는가?
- 버튼 제출 중 loading 표시가 있는가?
- 제출 중 버튼 disabled 처리가 있는가?
- 중복 클릭이 방지되는가?
- Skeleton / Spinner / Text loading이 적절한가?
- 로딩 종료가 보장되는가?
- 부분 로딩과 전체 로딩이 구분되는가?
- 긴 로딩에서 사용자 피드백이 있는가?
- loading 중 이전 데이터 유지 정책이 명확한가?

---

### [실무]

페이지 초기 loading:

```jsx
if (isLoading) {
  return <p>불러오는 중...</p>;
}
```

버튼 loading:

```jsx
<button type="submit" disabled={isSubmitting}>
  {isSubmitting ? "제출 중..." : "제출"}
</button>
```

잘못된 예:

```jsx
setIsLoading(true);

try {
  await fetchData();
} catch (error) {
  setError(error);
}
```

문제:

```text
finally에서 setIsLoading(false)가 없어 실패 시 loading이 종료되지 않을 수 있음
```

리뷰 코멘트 예:

```text
[High] API 실패 시 loading 상태가 false로 돌아가지 않아 무한 loading이 발생할 수 있습니다. finally에서 loading 종료를 보장해야 합니다.
```

---

### [FAQ]

Q. Loading State는 왜 필요해?
A. API 요청 중 사용자가 화면이 멈춘 것으로 오해하지 않게 하기 위해 필요하다.

Q. 버튼 제출 중 disabled는 왜 필요해?
A. 중복 제출과 중복 API 요청을 막기 위해 필요하다.

Q. loading 종료는 어디서 보장해야 해?
A. 성공과 실패 모두 처리되는 finally 또는 공통 종료 로직에서 보장하는 것이 좋다.

Q. Skeleton과 Spinner 중 뭐가 좋아?
A. 콘텐츠 구조를 예측할 수 있으면 Skeleton, 짧고 단순한 요청이면 Spinner나 text loading도 가능하다.

---

## 4.2 Partial Loading Review

### [개념]

Partial Loading Review는 화면 전체가 아니라 일부 영역만 다시 요청되는 경우 해당 영역에 맞는 loading 상태를 제공하는지 검토하는 과정이다.

모든 요청마다 전체 화면 loading을 표시하면 UX가 끊긴다.

---

### [핵심]

Partial Loading이 필요한 경우:

- 좋아요 버튼 처리
- 찜 버튼 처리
- 댓글 추가
- 리뷰 작성
- 더보기 pagination
- 무한 스크롤 추가 로딩
- 필터 변경 중 목록 영역만 로딩
- 프로필 일부 업데이트
- 알림 읽음 처리

---

### [실무]

좋아요 버튼 loading 예:

```jsx
<button
  type="button"
  disabled={isFavoriteUpdating}
  onClick={handleFavoriteClick}
>
  {isFavoriteUpdating ? "처리 중..." : "찜하기"}
</button>
```

전체 화면 loading이 부적절한 예:

```text
사용자가 좋아요 버튼 클릭
→ 전체 페이지 spinner 표시
→ 상세 내용이 사라짐
→ UX 불안정
```

리뷰 코멘트 예:

```text
[Medium] 좋아요 버튼 처리 중 전체 페이지 loading이 표시되어 사용자 흐름이 끊깁니다. 버튼 단위 partial loading으로 변경하는 것이 좋습니다.
```

---

### [FAQ]

Q. Partial Loading은 언제 필요해?
A. 화면 전체가 아니라 특정 버튼, 목록, 섹션만 업데이트되는 경우 필요하다.

Q. 모든 API 요청에 전체 화면 loading을 보여도 돼?
A. 권장하지 않는다. 작은 액션에는 버튼 또는 섹션 단위 loading이 더 자연스럽다.

Q. 더보기 요청은 어떤 loading이 좋아?
A. 기존 목록을 유지하고 하단에 추가 loading을 보여주는 방식이 좋다.

Q. 좋아요 클릭에 페이지 전체 loading이 필요한가?
A. 일반적으로 필요하지 않다. 버튼 단위 loading 또는 optimistic update가 더 적합하다.

---

# 5. Error State Review Rules

## 5.1 Error State Review

### [개념]

Error State Review는 실패 상황에서 사용자가 문제를 이해하고 다음 행동을 할 수 있도록 error UI가 제공되는지 검토하는 과정이다.

Error State는 단순히 개발자에게 console error를 보여주는 것이 아니라 사용자에게 복구 가능한 정보를 제공해야 한다.

---

### [핵심]

좋은 Error State 기준:

- 무엇이 실패했는지 알려줌
- 사용자 친화적인 문장 사용
- raw error 노출 금지
- 재시도 버튼 제공 가능
- 인증 오류는 로그인 이동 제공
- 권한 오류는 접근 불가 안내
- Not Found는 명확한 안내 제공
- 입력 오류는 field와 연결
- role="alert" 등 접근성 고려
- 실패 후 화면이 완전히 비지 않음

---

### [실무]

Error UI 예:

```jsx
if (error) {
  return (
    <div role="alert">
      <p>데이터를 불러오지 못했습니다.</p>
      <button type="button" onClick={refetch}>
        다시 시도
      </button>
    </div>
  );
}
```

나쁜 예:

```jsx
if (error) {
  return null;
}
```

문제:

```text
사용자가 오류인지 빈 결과인지 알 수 없음
```

리뷰 코멘트 예:

```text
[High] 데이터 조회 실패 시 null을 반환해 빈 화면이 표시됩니다. 사용자가 실패 상태를 이해하고 재시도할 수 있도록 Error State를 추가해야 합니다.
```

---

### [FAQ]

Q. Error State는 왜 필요해?
A. 실패 상황에서 사용자가 문제를 이해하고 복구 행동을 할 수 있게 하기 위해 필요하다.

Q. 에러 메시지에 서버 에러 내용을 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자 친화 메시지로 바꾸고 민감한 정보는 노출하지 않아야 한다.

Q. 에러 상태에는 재시도 버튼이 필요해?
A. 데이터 조회 실패처럼 복구 가능한 경우에는 재시도 버튼이 좋다.

Q. error 상태에서 null을 반환해도 돼?
A. 권장하지 않는다. 사용자는 오류인지 데이터 없음인지 알 수 없다.

---

## 5.2 Error Recovery Review

### [개념]

Error Recovery Review는 사용자가 에러 발생 후 다시 시도하거나 안전한 화면으로 이동할 수 있는 복구 경로가 제공되는지 검토하는 과정이다.

Error State는 안내에서 끝나지 않고 가능한 경우 다음 행동을 제공해야 한다.

---

### [핵심]

Error Recovery 예:

- 다시 시도 버튼
- 입력값 수정 후 재제출
- 로그인 페이지 이동
- 이전 페이지로 이동
- 목록으로 돌아가기
- 새로고침 안내
- 권한 없는 경우 홈 이동
- 파일 업로드 실패 후 파일 다시 선택
- 네트워크 실패 후 재시도

---

### [실무]

Not Found 복구 예:

```jsx
function FestivalNotFound() {
  return (
    <div>
      <p>축제 정보를 찾을 수 없습니다.</p>
      <Link to="/festivals">축제 목록으로 돌아가기</Link>
    </div>
  );
}
```

인증 만료 복구 예:

```text
401 발생
→ token 제거
→ 로그인 페이지 이동
→ 로그인 후 이전 페이지 복귀 가능
```

리뷰 코멘트 예:

```text
[Medium] 축제 상세 404 상태에서 에러 메시지만 표시되고 이동 경로가 없습니다. 목록으로 돌아가기 링크를 제공하면 복구 흐름이 좋아집니다.
```

---

### [FAQ]

Q. Error Recovery는 왜 필요해?
A. 사용자가 실패 상태에서 다음 행동을 할 수 있어야 기능 흐름이 끊기지 않기 때문이다.

Q. 모든 에러에 재시도 버튼이 필요해?
A. 아니다. 네트워크 실패나 조회 실패처럼 재시도가 의미 있는 경우에 적합하다.

Q. 404 에러에는 어떤 복구가 좋아?
A. Not Found 안내와 목록 또는 홈으로 돌아가는 링크가 좋다.

Q. 401 에러에는 어떤 복구가 필요해?
A. 로그인 페이지 이동, token 제거, 가능하면 원래 페이지 복귀 흐름이 필요하다.

---

# 6. Empty State Review Rules

## 6.1 Empty State Review

### [개념]

Empty State Review는 API 요청은 성공했지만 표시할 데이터가 없는 경우 빈 화면 대신 적절한 안내를 제공하는지 검토하는 과정이다.

Empty State는 Error State와 다르다.

---

### [핵심]

Empty State가 필요한 상황:

- 검색 결과 없음
- 알림 없음
- 리뷰 없음
- 즐겨찾기 없음
- 채팅 메시지 없음
- 필터 결과 없음
- 주문 내역 없음
- 업로드 파일 없음
- 댓글 없음
- 북마크 없음

좋은 Empty State 기준:

- 상태 설명
- 이유 또는 조건 안내
- 다음 행동 제안
- Error와 구분
- 화면이 비어 보이지 않음
- 검색 조건 초기화 또는 다른 조건 제안 가능

---

### [실무]

Empty State 예:

```jsx
if (festivals.length === 0) {
  return (
    <div>
      <p>조건에 맞는 축제가 없습니다.</p>
      <button type="button" onClick={resetFilters}>
        필터 초기화
      </button>
    </div>
  );
}
```

나쁜 예:

```jsx
return (
  <ul>
    {festivals.map((festival) => (
      <FestivalItem key={festival.id} festival={festival} />
    ))}
  </ul>
);
```

문제:

```text
festivals가 빈 배열이면 화면에 아무것도 표시되지 않음
→ 사용자는 로딩, 에러, 결과 없음 상태를 구분할 수 없음
```

리뷰 코멘트 예:

```text
[Medium] 검색 결과가 빈 배열일 때 아무 안내가 표시되지 않습니다. Empty State를 추가해 결과가 없음을 명확히 알려야 합니다.
```

---

### [FAQ]

Q. Empty State는 뭐야?
A. 요청은 성공했지만 표시할 데이터가 없는 상태를 사용자에게 안내하는 UI다.

Q. 데이터가 없으면 그냥 빈 화면이면 안 돼?
A. 안 된다. 사용자는 오류인지 결과가 없는지 알 수 없다.

Q. Empty State와 Error State는 달라?
A. 다르다. Empty State는 요청 성공 후 데이터 없음이고 Error State는 요청 실패 상태다.

Q. 검색 결과 없음에는 어떤 안내가 좋아?
A. 결과 없음 메시지와 다른 키워드, 필터 초기화 같은 다음 행동을 제공하는 것이 좋다.

---

## 6.2 Empty State Action Review

### [개념]

Empty State Action Review는 빈 상태에서 사용자가 다음 행동을 할 수 있도록 적절한 CTA 또는 안내가 제공되는지 검토하는 과정이다.

Empty State는 단순 메시지보다 다음 행동이 있을 때 UX 가치가 높다.

---

### [핵심]

Empty State Action 예:

- 필터 초기화
- 검색어 변경 안내
- 새 항목 만들기
- 목록으로 돌아가기
- 로그인 후 추가하기
- 첫 리뷰 작성하기
- 알림 설정하기
- 파일 업로드하기
- 새로고침하기

---

### [실무]

즐겨찾기 Empty State 예:

```jsx
function FavoriteEmptyState() {
  return (
    <div>
      <p>아직 찜한 축제가 없습니다.</p>
      <Link to="/festivals">축제 둘러보기</Link>
    </div>
  );
}
```

리뷰 코멘트 예:

```text
[Low] 즐겨찾기 목록이 비었을 때 메시지만 표시됩니다. 축제 목록으로 이동하는 CTA를 추가하면 사용자가 다음 행동을 이어가기 쉽습니다.
```

---

### [FAQ]

Q. Empty State에 CTA가 꼭 필요해?
A. 필수는 아니지만 사용자가 다음 행동을 할 수 있으면 UX가 좋아진다.

Q. 리뷰 없음 상태에는 어떤 CTA가 좋아?
A. 로그인 상태라면 첫 리뷰 작성하기, 비로그인 상태라면 로그인 후 작성 안내가 적합하다.

Q. 검색 결과 없음에는 어떤 CTA가 좋아?
A. 필터 초기화, 검색어 변경 안내, 전체 목록 보기 등이 적합하다.

Q. Empty State Action은 어떤 우선순위야?
A. 기본 Empty State 누락은 Medium, CTA 개선은 보통 Low 또는 Suggestion이다.

---

# 7. UX State Review Checklist

## 7.1 API and UX State Review Checklist

### [개념]

API and UX State Review Checklist는 Review Agent가 API 연동과 Loading / Error / Empty 상태를 검토할 때 사용하는 최종 점검 목록이다.

이 체크리스트는 API 안정성, 실패 처리, 중복 요청, 사용자 피드백을 빠르게 검토하기 위한 Retrieval 기준이다.

---

### [핵심]

API and UX State Review Checklist:

```md
## API Module

- [ ] API 호출 코드가 module로 분리되어 있는가?
- [ ] Axios instance 또는 fetch wrapper가 있는가?
- [ ] baseURL이 환경 변수로 관리되는가?
- [ ] public API와 private API가 구분되는가?
- [ ] 인증 header 처리가 일관적인가?
- [ ] endpoint 이름과 함수 이름이 명확한가?

## Endpoint

- [ ] frontend endpoint가 backend route와 일치하는가?
- [ ] HTTP method가 맞는가?
- [ ] path variable이 올바른가?
- [ ] query parameter 이름이 백엔드 명세와 일치하는가?
- [ ] localhost 또는 mock URL이 남아 있지 않은가?

## Response Mapping

- [ ] ApiResponse wrapper 구조를 올바르게 처리하는가?
- [ ] response.data와 response.data.data를 구분하는가?
- [ ] Page / Slice 응답 구조를 올바르게 처리하는가?
- [ ] optional field와 null 응답을 안전하게 처리하는가?

## Error Handling

- [ ] API 실패 시 catch 처리가 있는가?
- [ ] 사용자에게 error message가 표시되는가?
- [ ] status별 처리 전략이 있는가?
- [ ] 401 / 403 / 404 / 500 처리가 구분되는가?
- [ ] 네트워크 실패와 timeout을 처리하는가?
- [ ] 서버 validation error를 표시하는가?
- [ ] raw error 또는 민감 정보가 노출되지 않는가?

## Request Duplication

- [ ] useEffect dependency 오류로 중복 요청이 발생하지 않는가?
- [ ] submit 중복 클릭이 방지되는가?
- [ ] debounce가 필요한 검색 요청에 적용되어 있는가?
- [ ] Race Condition 위험이 없는가?
- [ ] interceptor retry 무한 반복이 없는가?

## Loading

- [ ] 초기 loading UI가 있는가?
- [ ] 버튼 제출 중 loading / disabled 처리가 있는가?
- [ ] loading 종료가 finally에서 보장되는가?
- [ ] 부분 loading과 전체 loading이 적절히 구분되는가?

## Error State

- [ ] 실패 상태가 빈 화면으로 처리되지 않는가?
- [ ] 사용자 친화 메시지가 있는가?
- [ ] 재시도 또는 이동 같은 복구 행동이 있는가?
- [ ] 접근성 role이 필요한 경우 제공되는가?

## Empty State

- [ ] 빈 배열 응답에 Empty State가 있는가?
- [ ] Error State와 Empty State가 구분되는가?
- [ ] 검색 결과 없음, 리뷰 없음, 알림 없음 상태가 안내되는가?
- [ ] 다음 행동 CTA가 필요한 경우 제공되는가?
```

---

### [실무]

API and UX State Review 우선순위:

```text
Endpoint Mismatch
→ Response Mapping Error
→ Missing API Error Handling
→ Infinite Loading
→ Duplicate Submit
→ Missing Empty State
→ Missing Recovery Action
→ API Module Refactor
```

우선순위 판단:

```text
endpoint 불일치로 핵심 기능 실패
→ High 또는 Critical

API 실패 처리 없음
→ High

loading 무한 지속
→ High

POST 중복 제출 가능
→ High

Empty State 누락
→ Medium

API module 미분리
→ Medium

검색 debounce 개선
→ Medium 또는 Suggestion
```

---

### [FAQ]

Q. API Review에서 가장 먼저 볼 것은 뭐야?
A. endpoint 일치, response mapping, error handling, loading 종료, 중복 요청 위험을 먼저 본다.

Q. response.data.data 오류는 어떤 우선순위야?
A. 화면이 깨지거나 핵심 데이터가 표시되지 않으면 High로 판단할 수 있다.

Q. API 실패 처리가 없으면 어떤 우선순위야?
A. 주요 사용자 흐름이면 High다.

Q. Empty State 누락은 어떤 우선순위야?
A. 보통 Medium이다. 사용자가 오류인지 데이터 없음인지 구분할 수 없기 때문이다.

---

# Retrieval Queries

### [FAQ]

Q. API Module Review는 뭐야?
A. 프론트엔드 API 호출 코드가 컴포넌트 내부에 흩어지지 않고 일관된 모듈 구조로 분리되어 있는지 검토하는 과정이다.

Q. API 호출 코드는 어디에 두는 게 좋아?
A. 컴포넌트에 직접 흩뿌리기보다 api module이나 custom hook으로 분리하는 것이 좋다.

Q. Axios Instance Review는 뭐야?
A. Axios instance가 baseURL, timeout, header, interceptor, error handling을 일관되게 관리하는지 검토하는 과정이다.

Q. Axios instance는 왜 필요해?
A. baseURL, timeout, header, interceptor를 한 곳에서 관리해 API 호출 일관성을 유지하기 위해 필요하다.

Q. public API와 private API는 왜 구분해?
A. 인증 header가 필요한 요청과 필요 없는 요청을 분리해야 인증 누락이나 불필요한 token 전송을 줄일 수 있다.

Q. API Endpoint Review는 뭐야?
A. 프론트엔드에서 호출하는 endpoint가 백엔드 API 명세와 일치하는지 검토하는 과정이다.

Q. API endpoint가 백엔드와 다르면 어떤 문제야?
A. 404, 405, 필터 미동작, 데이터 조회 실패 같은 문제가 발생할 수 있다.

Q. query parameter 이름도 리뷰해야 해?
A. 해야 한다. 백엔드 DTO 또는 Controller parameter 이름과 다르면 필터나 검색이 동작하지 않을 수 있다.

Q. API Response Mapping Review는 뭐야?
A. 백엔드 응답 구조를 프론트엔드가 올바르게 해석하고 화면 상태로 변환하는지 검토하는 과정이다.

Q. response.data와 response.data.data는 왜 헷갈려?
A. Axios response.data와 백엔드 ApiResponse의 data field가 중첩되기 때문이다.

Q. Page와 Slice 응답은 다르게 처리해야 해?
A. 그렇다. Page는 total count 정보가 있고 Slice는 hasNext 중심으로 무한 스크롤에 적합하다.

Q. API Error Handling Review는 뭐야?
A. API 실패 상황을 코드와 UI가 적절히 처리하는지 검토하는 과정이다.

Q. API 에러는 console.log만 해도 돼?
A. 안 된다. 사용자에게 실패 상태와 복구 방법을 제공해야 한다.

Q. API 실패 처리가 없으면 어떤 우선순위야?
A. 주요 사용자 흐름이면 High로 판단할 수 있다.

Q. HTTP status별 처리는 왜 필요해?
A. 인증, 권한, 데이터 없음, 서버 오류는 사용자의 다음 행동이 다르기 때문이다.

Q. 401 에러는 어떻게 처리해야 해?
A. 인증 만료로 보고 refresh token 처리 또는 로그인 페이지 이동을 고려한다.

Q. 403은 어떻게 처리해야 해?
A. 권한 없음 메시지를 보여주고 접근 가능한 페이지로 이동할 수 있게 한다.

Q. 404는 항상 에러야?
A. 상황에 따라 Not Found 상태로 사용자에게 안내해야 하는 정상 흐름일 수 있다.

Q. Validation Error Review는 뭐야?
A. 서버에서 반환한 validation error가 사용자가 이해할 수 있는 형태로 화면에 표시되는지 검토하는 과정이다.

Q. 프론트엔드 validation만 있으면 서버 validation error 처리가 없어도 돼?
A. 안 된다. 프론트엔드 validation은 우회 가능하므로 서버 validation 결과도 반드시 처리해야 한다.

Q. Network Error는 HTTP status가 있어?
A. 없을 수 있다. 서버 응답 자체를 받지 못한 경우 error.response가 undefined일 수 있다.

Q. error.response.status에 바로 접근해도 돼?
A. 위험하다. 네트워크 실패에서는 error.response가 없을 수 있으므로 optional chaining이 필요하다.

Q. Duplicate Request Review는 뭐야?
A. 동일한 API 요청이 불필요하게 반복되는지 검토하는 과정이다.

Q. API가 두 번 호출되는 이유는 뭐야?
A. useEffect dependency 오류, StrictMode, 중복 mount, submit 중복 클릭, cache 미사용이 원인일 수 있다.

Q. React StrictMode 때문에 두 번 호출될 수 있어?
A. 개발 환경에서는 side effect 검출을 위해 일부 로직이 두 번 실행될 수 있다. 운영 동작과 구분해야 한다.

Q. 중복 제출은 어떻게 막아?
A. isSubmitting 상태를 두고 제출 중 버튼 disabled 처리와 handler guard를 함께 사용한다.

Q. 검색 input 변경마다 API를 호출해도 돼?
A. 가능하지만 서버 부하와 UX를 고려해 debounce 또는 명시적 submit 방식을 검토해야 한다.

Q. Race Condition은 언제 생겨?
A. 여러 비동기 요청이 동시에 진행되고 응답 순서가 보장되지 않을 때 발생한다.

Q. Race Condition은 어떻게 막아?
A. 이전 요청 취소, 최신 request id 확인, query key 기반 server state 도구 사용으로 줄일 수 있다.

Q. Loading State Review는 뭐야?
A. API 요청 중 사용자가 대기 상태를 이해할 수 있도록 loading UI가 제공되는지 검토하는 과정이다.

Q. Loading State는 왜 필요해?
A. API 요청 중 사용자가 화면이 멈춘 것으로 오해하지 않게 하기 위해 필요하다.

Q. loading 종료는 어디서 보장해야 해?
A. 성공과 실패 모두 처리되는 finally 또는 공통 종료 로직에서 보장하는 것이 좋다.

Q. Partial Loading은 언제 필요해?
A. 화면 전체가 아니라 특정 버튼, 목록, 섹션만 업데이트되는 경우 필요하다.

Q. Error State Review는 뭐야?
A. 실패 상황에서 사용자가 문제를 이해하고 다음 행동을 할 수 있도록 error UI가 제공되는지 검토하는 과정이다.

Q. Error State에서 null을 반환해도 돼?
A. 권장하지 않는다. 사용자는 오류인지 데이터 없음인지 알 수 없다.

Q. Error Recovery는 왜 필요해?
A. 사용자가 실패 상태에서 다음 행동을 할 수 있어야 기능 흐름이 끊기지 않기 때문이다.

Q. Empty State Review는 뭐야?
A. API 요청은 성공했지만 표시할 데이터가 없는 경우 빈 화면 대신 적절한 안내를 제공하는지 검토하는 과정이다.

Q. Empty State와 Error State는 달라?
A. 다르다. Empty State는 요청 성공 후 데이터 없음이고 Error State는 요청 실패 상태다.

Q. 데이터가 없으면 그냥 빈 화면이면 안 돼?
A. 안 된다. 사용자는 오류인지 결과가 없는지 알 수 없다.

Q. Empty State에 CTA가 꼭 필요해?
A. 필수는 아니지만 사용자가 다음 행동을 할 수 있으면 UX가 좋아진다.

Q. API and UX State Review에서 가장 먼저 볼 것은 뭐야?
A. endpoint 일치, response mapping, error handling, loading 종료, 중복 요청 위험을 먼저 본다.

Q. API and UX State Review의 최종 목적은 뭐야?
A. 프론트엔드가 API 성공, 실패, 지연, 빈 결과, 중복 요청 상황을 안정적으로 처리하는지 판단하는 것이다.
