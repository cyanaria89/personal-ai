# Data Fetching & REST API Integration Part02 - fetch and Axios

---

# 1. fetch Overview

## 1.1 fetch 기본 개념

### [개념]

`fetch`는 브라우저가 기본 제공하는 HTTP Request API다.

외부 라이브러리 없이 REST API를 호출할 수 있으며, Promise 기반으로 동작한다.

Frontend Agent는 `fetch`를 사용할 때 Request URL, HTTP Method, Header, Body, Response Parsing, Error Handling을 명시적으로 작성해야 한다.

기본 Flow:

```text
API Function
→ fetch(url, options)
→ HTTP Request
→ Response
→ response.ok Check
→ response.json()
→ Return Data
```

---

### [핵심]

fetch 핵심 키워드:

- fetch
- Promise
- async / await
- Request URL
- Request Options
- method
- headers
- body
- JSON.stringify
- response.ok
- response.status
- response.json()
- try / catch
- Network Error
- HTTP Error
- Content-Type
- Authorization Header

fetch 특징:

- 브라우저 기본 API
- 외부 라이브러리 불필요
- HTTP 400 / 500을 자동 throw하지 않음
- `response.ok` 직접 확인 필요
- JSON Request Body는 `JSON.stringify()` 필요
- JSON Response는 `response.json()` 필요
- 공통 baseURL / token / error handling은 직접 래퍼 필요

---

### [실무]

2026 실무 기준에서 `fetch`는 간단한 API 요청이나 의존성 최소화가 필요한 프로젝트에 사용할 수 있다.

단, 프로젝트 규모가 커지면 다음 문제가 발생할 수 있다.

- baseURL 반복
- Header 반복
- Authorization Header 반복
- response.ok 반복
- response.json 반복
- Error Handling 중복
- 401 / 403 / 500 처리 중복
- Response DTO Mapping 중복

GET 기본 예:

```javascript
export async function getFestivals() {
  const response = await fetch("/api/festivals");

  if (!response.ok) {
    throw new Error("Failed to load festivals");
  }

  return await response.json();
}
```

POST 기본 예:

```javascript
export async function createReview(requestBody) {
  const response = await fetch("/api/reviews", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(requestBody),
  });

  if (!response.ok) {
    throw new Error("Failed to create review");
  }

  return await response.json();
}
```

---

### [FAQ]

Q. fetch는 뭐야?
A. 브라우저가 기본 제공하는 HTTP 요청 API다. 외부 라이브러리 없이 REST API를 호출할 수 있다.

Q. fetch는 언제 쓰면 좋아?
A. 간단한 요청, 의존성 최소화, 브라우저 기본 API만 사용하는 프로젝트에 적합하다.

Q. fetch는 404나 500이면 catch로 바로 가?
A. 아니다. 네트워크 오류가 아니면 catch로 바로 가지 않는다. `response.ok`를 직접 확인해야 한다.

Q. fetch에서 JSON 응답은 어떻게 꺼내?
A. `await response.json()`을 호출해 Response Body를 JavaScript 객체로 변환한다.

---

# 2. fetch GET Rules

## 2.1 fetch GET Request

### [개념]

fetch GET Request는 서버 데이터를 조회할 때 사용하는 기본 요청 방식이다.

조회 조건은 보통 Query Parameter로 전달한다.

GET 요청은 Request Body를 사용하지 않는 것이 원칙이다.

---

### [핵심]

GET 요청 구성 요소:

- Request URL
- Query Parameter
- response.ok
- response.status
- response.json()
- Error Handling
- Empty State 처리
- Response DTO Mapping

GET 요청 주의:

- GET 요청에 body 사용 금지
- Query Parameter는 URL에 포함
- undefined / null parameter 제거
- response.ok 직접 확인
- JSON 응답 여부 확인
- HTML 응답이면 API path / SPA fallback 확인

---

### [실무]

기본 GET:

```javascript
export async function getFestivals() {
  const response = await fetch("/api/festivals");

  if (!response.ok) {
    throw new Error("Failed to load festivals");
  }

  return await response.json();
}
```

Query Parameter 포함 GET:

```javascript
export async function searchFestivals(params) {
  const queryString = new URLSearchParams(params).toString();

  const response = await fetch(`/api/festivals/search?${queryString}`);

  if (!response.ok) {
    throw new Error("Failed to search festivals");
  }

  return await response.json();
}
```

빈 값 제거 후 Query Parameter 생성:

```javascript
function cleanParams(params) {
  return Object.fromEntries(
    Object.entries(params).filter(([, value]) => {
      return value !== undefined && value !== null && value !== "";
    }),
  );
}

export async function searchFestivals(params) {
  const clean = cleanParams(params);
  const queryString = new URLSearchParams(clean).toString();

  const response = await fetch(`/api/festivals/search?${queryString}`);

  if (!response.ok) {
    throw new Error("Failed to search festivals");
  }

  return await response.json();
}
```

---

### [FAQ]

Q. fetch GET 요청은 언제 써?
A. 서버 데이터를 조회할 때 사용한다. 목록 조회, 상세 조회, 검색, 필터 조회에 사용한다.

Q. fetch GET에서 Query Parameter는 어떻게 붙여?
A. `URLSearchParams`를 사용해 `?key=value` 형태의 query string을 만들 수 있다.

Q. GET 요청에 body를 넣어도 돼?
A. 권장하지 않는다. 조회 조건은 Query Parameter로 전달한다.

Q. GET 응답이 HTML이면 뭐가 문제야?
A. API URL이 잘못되었거나 SPA fallback에 걸려 `index.html`을 받은 경우일 수 있다.

---

# 3. fetch POST Rules

## 3.1 fetch POST Request

### [개념]

fetch POST Request는 서버에 새로운 데이터를 생성하거나 명령성 요청을 보낼 때 사용한다.

POST 요청에서는 Request Body를 JSON으로 전달하는 경우가 많다.

---

### [핵심]

POST 요청 구성 요소:

- method: "POST"
- headers
- Content-Type
- application/json
- body
- JSON.stringify
- response.ok
- response.json
- Validation Error Handling

POST 요청 주의:

- JavaScript 객체를 그대로 body에 넣지 않음
- JSON Request Body는 `JSON.stringify()` 필요
- `Content-Type: application/json` 설정
- Backend Request DTO 필드명과 일치
- 필수값 검증 후 요청
- 서버 Validation Error 처리 필요

---

### [실무]

리뷰 작성 POST 예:

```javascript
export async function createReview(requestBody) {
  const response = await fetch("/api/reviews", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(requestBody),
  });

  if (!response.ok) {
    throw new Error("Failed to create review");
  }

  return await response.json();
}
```

로그인 POST 예:

```javascript
export async function login(loginRequest) {
  const response = await fetch("/api/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(loginRequest),
  });

  if (!response.ok) {
    throw new Error("Failed to login");
  }

  return await response.json();
}
```

POST Request Flow:

```text
Form Submit
→ Client Validation
→ Build Request Body
→ JSON.stringify(requestBody)
→ fetch POST
→ Backend Validation
→ Response DTO
→ Success or Error UI
```

---

### [FAQ]

Q. fetch POST는 언제 써?
A. 리뷰 작성, 회원가입, 로그인, 데이터 생성처럼 서버에 데이터를 보낼 때 사용한다.

Q. fetch POST에서 body는 왜 JSON.stringify를 해?
A. JavaScript 객체를 JSON 문자열로 변환해 서버에 보내야 하기 때문이다.

Q. fetch POST에서 Content-Type은 왜 필요해?
A. 서버가 Request Body를 JSON으로 해석할 수 있도록 `application/json`을 알려주기 위해 필요하다.

Q. Request Body 필드명은 어떻게 정해?
A. Backend Request DTO가 기대하는 필드명과 타입에 맞춘다.

---

# 4. fetch PUT / PATCH / DELETE Rules

## 4.1 fetch Update and Delete Request

### [개념]

PUT, PATCH, DELETE는 서버 데이터를 수정하거나 삭제할 때 사용하는 HTTP Method다.

PUT은 전체 수정, PATCH는 부분 수정, DELETE는 삭제에 사용한다.

---

### [핵심]

PUT 기준:

- 전체 수정
- Request Body 사용
- 기존 Resource 전체 교체 의미

PATCH 기준:

- 부분 수정
- Request Body 사용 가능
- 특정 필드만 변경

DELETE 기준:

- Resource 삭제
- Path Variable 중심
- 필요 시 Query Parameter 사용

주의:

- Backend Controller Method와 일치
- Path Variable undefined 방지
- DELETE 요청에서 body 사용은 프로젝트 기준 확인
- 204 No Content 응답 처리
- 성공 후 목록 refetch 또는 cache invalidation 필요

---

### [실무]

PUT 예:

```javascript
export async function updateUserProfile(requestBody) {
  const response = await fetch("/api/users/me", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(requestBody),
  });

  if (!response.ok) {
    throw new Error("Failed to update profile");
  }

  return await response.json();
}
```

PATCH 예:

```javascript
export async function markNotificationRead(notificationId) {
  const response = await fetch(`/api/notifications/${notificationId}/read`, {
    method: "PATCH",
  });

  if (!response.ok) {
    throw new Error("Failed to mark notification read");
  }

  return await response.json();
}
```

DELETE 예:

```javascript
export async function deleteReview(reviewId) {
  const response = await fetch(`/api/reviews/${reviewId}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw new Error("Failed to delete review");
  }

  return await response.json();
}
```

204 No Content 처리 예:

```javascript
export async function deleteFavorite(festivalId) {
  const response = await fetch(`/api/favorites/${festivalId}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw new Error("Failed to delete favorite");
  }

  if (response.status === 204) {
    return null;
  }

  return await response.json();
}
```

---

### [FAQ]

Q. PUT과 PATCH 차이는?
A. PUT은 전체 수정에 가깝고 PATCH는 일부 필드 수정에 가깝다.

Q. DELETE 요청에는 body를 넣어도 돼?
A. 프로젝트 기준에 따라 다르지만 보통 Path Variable로 삭제 대상을 식별한다.

Q. 204 응답은 어떻게 처리해?
A. Response Body가 없을 수 있으므로 `response.json()`을 바로 호출하지 않고 status를 확인한다.

Q. 수정이나 삭제 성공 후에는 뭘 해야 해?
A. 관련 목록을 다시 조회하거나 TanStack Query를 사용한다면 관련 query를 invalidate한다.

---

# 5. fetch Error Handling Rules

## 5.1 fetch Error Handling 기준

### [개념]

fetch Error Handling은 Network Error와 HTTP Error를 구분해 처리해야 한다.

fetch는 서버가 400, 401, 403, 404, 500을 응답해도 자동으로 throw하지 않는다.

따라서 `response.ok`를 직접 확인해야 한다.

---

### [핵심]

fetch 오류 구분:

- Network Error
- HTTP Error
- JSON Parsing Error
- Timeout 직접 구현 필요
- CORS Error
- Response Shape Mismatch

fetch HTTP Error 처리:

```text
Response Received
→ response.ok false
→ response.status 확인
→ Error Message Mapping
→ throw Error
```

주의:

- `catch`는 주로 네트워크 오류, 직접 throw한 오류를 받음
- 401 / 403 / 404 / 500은 response.ok로 확인
- 에러 메시지 원문 그대로 노출 금지
- 서버 에러 응답 Body를 파싱할지 기준 필요
- CORS 실패는 response를 받지 못할 수 있음

---

### [실무]

기본 Error Handling:

```javascript
export async function getFestivals() {
  const response = await fetch("/api/festivals");

  if (!response.ok) {
    throw new Error(`API Error: ${response.status}`);
  }

  return await response.json();
}
```

Status Code별 처리:

```javascript
function getErrorMessage(status) {
  if (status === 400) {
    return "요청 값을 확인해 주세요.";
  }

  if (status === 401) {
    return "로그인이 필요합니다.";
  }

  if (status === 403) {
    return "접근 권한이 없습니다.";
  }

  if (status === 404) {
    return "요청한 데이터를 찾을 수 없습니다.";
  }

  if (status >= 500) {
    return "서버 오류가 발생했습니다.";
  }

  return "요청 처리 중 문제가 발생했습니다.";
}
```

적용 예:

```javascript
export async function requestJson(url, options) {
  const response = await fetch(url, options);

  if (!response.ok) {
    throw new Error(getErrorMessage(response.status));
  }

  return await response.json();
}
```

---

### [FAQ]

Q. fetch는 500이면 자동으로 catch로 가?
A. 아니다. `response.ok`를 확인하고 직접 throw해야 한다.

Q. Network Error와 HTTP Error는 달라?
A. 다르다. Network Error는 응답 자체를 받지 못한 경우이고 HTTP Error는 서버가 오류 상태 코드를 응답한 경우다.

Q. CORS 에러는 response.status로 확인할 수 있어?
A. 대부분 response를 정상적으로 받지 못하므로 Console과 Network 탭의 preflight 요청을 확인해야 한다.

Q. fetch 에러 메시지는 서버 원문 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자 메시지와 개발자 로그를 구분해야 한다.

---

# 6. fetch Wrapper Rules

## 6.1 fetch Wrapper 설계

### [개념]

fetch Wrapper는 baseURL, Header, response.ok, response.json, Error Handling 같은 공통 로직을 함수로 묶는 방식이다.

fetch를 직접 반복 사용하면 중복이 많아지므로 실무에서는 wrapper를 만들 수 있다.

---

### [핵심]

Wrapper 대상:

- baseURL
- Request URL 조합
- Default Header
- Authorization Header
- JSON.stringify
- response.ok
- response.json
- Error Mapping
- 204 No Content 처리
- Common Error Handling

Wrapper 장점:

- 중복 감소
- Error Handling 통일
- Header 처리 통일
- API Layer 코드 간결화

Wrapper 주의:

- 너무 많은 책임 부여 금지
- 인증 refresh 심화 로직은 별도 설계
- 응답 wrapper unwrap 기준 통일
- 에러를 삼키지 말고 throw

---

### [실무]

기본 fetch wrapper:

```javascript
const BASE_URL = process.env.REACT_APP_API_BASE_URL;

export async function apiRequest(path, options = {}) {
  const response = await fetch(`${BASE_URL}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...options.headers,
    },
  });

  if (!response.ok) {
    throw new Error(`API Error: ${response.status}`);
  }

  if (response.status === 204) {
    return null;
  }

  return await response.json();
}
```

POST wrapper 사용 예:

```javascript
export function createReview(requestBody) {
  return apiRequest("/reviews", {
    method: "POST",
    body: JSON.stringify(requestBody),
  });
}
```

Authorization Header 포함 wrapper:

```javascript
export async function authRequest(path, options = {}) {
  const accessToken = localStorage.getItem("accessToken");

  return apiRequest(path, {
    ...options,
    headers: {
      ...options.headers,
      Authorization: accessToken ? `Bearer ${accessToken}` : undefined,
    },
  });
}
```

주의:

- `Authorization: undefined`가 실제 Header로 들어가지 않게 확인
- token이 없으면 Header를 생략하는 방식이 안전
- 더 복잡한 인증 흐름은 Axios Interceptor 또는 Auth Flow 문서에서 관리

---

### [FAQ]

Q. fetch Wrapper는 왜 만들어?
A. baseURL, Header, response.ok, Error Handling 같은 반복 코드를 줄이고 요청 기준을 통일하기 위해 만든다.

Q. fetch Wrapper를 만들면 Axios가 필요 없어?
A. 간단한 프로젝트에서는 가능하다. 하지만 interceptor, error object, 공통 설정이 많으면 Axios가 더 편할 수 있다.

Q. Wrapper에서 에러를 처리하고 끝내도 돼?
A. 대부분 throw해서 호출부에서 Loading / Error UI를 처리할 수 있게 해야 한다.

Q. Wrapper에서 response.data.data까지 풀어도 돼?
A. 가능하지만 프로젝트 전체에서 ApiResponse wrapper 처리 기준을 일관되게 정해야 한다.

---

# 7. Axios Overview

## 7.1 Axios 기본 개념

### [개념]

Axios는 HTTP Request를 쉽게 작성할 수 있는 JavaScript 라이브러리다.

공통 설정, JSON 처리, Error Handling, Interceptor, baseURL 관리가 편리하다.

Frontend REST API Integration에서는 Axios Instance와 API Layer를 함께 사용하는 경우가 많다.

---

### [핵심]

Axios 핵심 키워드:

- axios
- axios.get
- axios.post
- axios.put
- axios.patch
- axios.delete
- axios.create
- baseURL
- timeout
- params
- headers
- data
- response.data
- AxiosError
- interceptor
- request interceptor
- response interceptor
- publicApi
- authApi

Axios 특징:

- JSON Request Body 자동 처리
- JSON Response 자동 parsing
- Query Parameter는 `params` 옵션 사용
- Request Body는 두 번째 인자 사용
- `response.data` 중심 처리
- HTTP Error를 catch에서 처리 가능
- Axios Instance로 공통 설정 가능
- Interceptor로 token header 처리 가능

---

### [실무]

GET 예:

```javascript
import axios from "axios";

export async function getFestivals(params) {
  const response = await axios.get("/api/festivals", {
    params,
  });

  return response.data;
}
```

POST 예:

```javascript
export async function createReview(requestBody) {
  const response = await axios.post("/api/reviews", requestBody);

  return response.data;
}
```

Axios Instance와 함께 사용하는 실무 구조:

```text
src
├ api
│  ├ axiosInstance.js
│  ├ festivalApi.js
│  ├ reviewApi.js
│  └ notificationApi.js
```

---

### [FAQ]

Q. Axios는 뭐야?
A. HTTP 요청을 쉽게 작성할 수 있는 JavaScript 라이브러리다.

Q. Axios는 언제 쓰면 좋아?
A. baseURL, 인증 헤더, interceptor, 공통 에러 처리, API Layer가 필요한 프로젝트에 적합하다.

Q. Axios 응답 데이터는 어디에 있어?
A. 보통 `response.data`에 있다.

Q. Axios는 JSON.stringify를 직접 해야 해?
A. 일반적인 JSON 요청에서는 requestBody 객체를 그대로 전달하면 Axios가 자동 처리한다.

---

# 8. Axios GET Rules

## 8.1 Axios GET Request

### [개념]

Axios GET Request는 서버 데이터를 조회할 때 사용한다.

Query Parameter는 `params` 옵션으로 전달한다.

---

### [핵심]

Axios GET 구성 요소:

- axios.get
- url
- config
- params
- headers
- response.data
- Error Handling
- Query Parameter
- Response DTO Mapping

GET 예:

```javascript
axios.get("/festivals", { params });
```

주의:

- Query Parameter는 `params`에 넣음
- Request Body를 넣지 않음
- `response.data` 구조 확인
- ApiResponse wrapper 여부 확인
- Page / Slice 응답이면 content 위치 확인

---

### [실무]

기본 GET:

```javascript
export async function getFestivals() {
  const response = await publicApi.get("/festivals");
  return response.data;
}
```

Query Parameter 포함 GET:

```javascript
export async function searchFestivals(params) {
  const response = await publicApi.get("/festivals/search", {
    params,
  });

  return response.data;
}
```

상세 조회 GET:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data;
}
```

ApiResponse wrapper unwrap 예:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data.data;
}
```

---

### [FAQ]

Q. Axios에서 query parameter는 어떻게 보내?
A. `axios.get(url, { params: { keyword: "flower" } })` 형태로 보낸다.

Q. Axios GET에서 body를 보내?
A. 권장하지 않는다. 조회 조건은 `params` 옵션으로 보낸다.

Q. Axios GET 응답은 어디에 있어?
A. Axios 응답 객체의 `response.data`에 있다.

Q. response.data.data는 언제 써?
A. Backend가 ApiResponse wrapper로 응답할 때 실제 데이터가 `data` 안에 한 번 더 들어갈 수 있다.

---

# 9. Axios POST Rules

## 9.1 Axios POST Request

### [개념]

Axios POST Request는 서버에 데이터를 생성하거나 명령성 요청을 보낼 때 사용한다.

Request Body는 `axios.post(url, requestBody)`의 두 번째 인자로 전달한다.

---

### [핵심]

Axios POST 구성 요소:

- axios.post
- url
- requestBody
- config
- headers
- response.data
- JSON Body
- DTO Mapping
- Validation Error

POST 예:

```javascript
axios.post("/reviews", requestBody);
```

주의:

- Request Body는 두 번째 인자
- Header config는 세 번째 인자
- Backend Request DTO 필드명과 일치
- JSON.stringify 직접 호출 불필요한 경우 많음
- Validation Error 처리 필요

---

### [실무]

리뷰 작성:

```javascript
export async function createReview(requestBody) {
  const response = await authApi.post("/reviews", requestBody);
  return response.data;
}
```

로그인:

```javascript
export async function login(loginRequest) {
  const response = await publicApi.post("/auth/login", loginRequest);
  return response.data;
}
```

POST + Header config:

```javascript
export async function createReview(requestBody, accessToken) {
  const response = await axios.post("/api/reviews", requestBody, {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });

  return response.data;
}
```

실무에서는 Header를 직접 반복하지 않고 `authApi` Interceptor로 처리한다.

---

### [FAQ]

Q. Axios POST body는 어디에 넣어?
A. `axios.post(url, requestBody)`처럼 두 번째 인자에 넣는다.

Q. Axios POST에서 Header는 어디에 넣어?
A. 세 번째 인자인 config 객체에 `headers`로 넣는다.

Q. Axios POST에서도 JSON.stringify가 필요해?
A. 일반적인 JSON 요청에서는 필요하지 않다. Axios가 객체를 JSON으로 처리한다.

Q. 로그인 API는 publicApi야 authApi야?
A. 로그인 전 요청이므로 보통 publicApi를 사용한다.

---

# 10. Axios PUT / PATCH / DELETE Rules

## 10.1 Axios Update and Delete Request

### [개념]

Axios PUT, PATCH, DELETE는 서버 리소스를 수정하거나 삭제할 때 사용한다.

PUT은 전체 수정, PATCH는 부분 수정, DELETE는 삭제에 사용한다.

---

### [핵심]

Axios Update / Delete 키워드:

- axios.put
- axios.patch
- axios.delete
- requestBody
- config
- Path Variable
- response.data
- 204 No Content
- cache invalidation
- refetch

PUT:

```javascript
axios.put(url, requestBody);
```

PATCH:

```javascript
axios.patch(url, requestBody);
```

DELETE:

```javascript
axios.delete(url);
```

DELETE config:

```javascript
axios.delete(url, config);
```

---

### [실무]

PUT 예:

```javascript
export async function updateUserProfile(requestBody) {
  const response = await authApi.put("/users/me", requestBody);
  return response.data;
}
```

PATCH 예:

```javascript
export async function updateNotificationSetting(requestBody) {
  const response = await authApi.patch("/notifications/settings", requestBody);
  return response.data;
}
```

PATCH Path Variable 예:

```javascript
export async function markNotificationRead(notificationId) {
  const response = await authApi.patch(`/notifications/${notificationId}/read`);
  return response.data;
}
```

DELETE 예:

```javascript
export async function deleteReview(reviewId) {
  const response = await authApi.delete(`/reviews/${reviewId}`);
  return response.data;
}
```

DELETE에서 body가 필요한 경우:

```javascript
export async function deleteSelectedItems(requestBody) {
  const response = await authApi.delete("/items", {
    data: requestBody,
  });

  return response.data;
}
```

주의:

- DELETE body는 프로젝트와 Backend 설정 기준 확인
- 일반 삭제는 Path Variable 중심
- 수정 / 삭제 성공 후 관련 조회 데이터 갱신
- TanStack Query 사용 시 mutation 성공 후 invalidate

---

### [FAQ]

Q. Axios PUT body는 어디에 넣어?
A. `axios.put(url, requestBody)`처럼 두 번째 인자에 넣는다.

Q. Axios PATCH body는 어디에 넣어?
A. `axios.patch(url, requestBody)`처럼 두 번째 인자에 넣는다.

Q. Axios DELETE에서 body를 보내려면 어떻게 해?
A. `axios.delete(url, { data: requestBody })` 형태를 사용한다.

Q. DELETE 성공 후 response.data가 없을 수 있어?
A. 있다. Backend가 204 No Content를 반환하면 응답 body가 없을 수 있다.

---

# 11. Axios Error Handling Rules

## 11.1 Axios Error Handling 기준

### [개념]

Axios Error Handling은 API 실패 시 AxiosError를 기준으로 HTTP Status Code, Response Body, Network Error를 분류하는 작업이다.

Axios는 HTTP Error 상태를 Promise reject로 처리하므로 `try / catch`에서 잡을 수 있다.

---

### [핵심]

Axios Error 확인 대상:

- axios.isAxiosError(error)
- error.response
- error.response.status
- error.response.data
- error.request
- error.message
- Network Error
- Timeout Error
- Validation Error
- 401
- 403
- 404
- 500

Axios Error 구분:

```text
error.response 있음 → 서버가 응답한 HTTP Error
error.request 있음 → 요청은 보냈지만 응답 없음
그 외 → 요청 설정 또는 기타 오류
```

---

### [실무]

기본 Error Mapping:

```javascript
import axios from "axios";

export function getApiErrorMessage(error) {
  if (axios.isAxiosError(error)) {
    const status = error.response?.status;

    if (status === 400) {
      return "요청 값을 확인해 주세요.";
    }

    if (status === 401) {
      return "로그인이 필요합니다.";
    }

    if (status === 403) {
      return "접근 권한이 없습니다.";
    }

    if (status === 404) {
      return "요청한 데이터를 찾을 수 없습니다.";
    }

    if (status >= 500) {
      return "서버 오류가 발생했습니다.";
    }
  }

  return "요청 처리 중 문제가 발생했습니다.";
}
```

API 호출부 예:

```javascript
async function loadFestivals() {
  try {
    const data = await getFestivals();
    setFestivals(data.content);
  } catch (error) {
    setErrorMessage(getApiErrorMessage(error));
  }
}
```

주의:

- error 객체 전체를 사용자 화면에 노출하지 않음
- 401 / 403 구분
- Network Error와 서버 오류 구분
- Validation Error는 field별 메시지 처리 가능
- Interceptor에서 에러를 삼키지 않음

---

### [FAQ]

Q. Axios Error는 어떻게 확인해?
A. `axios.isAxiosError(error)`로 확인하고 `error.response?.status`를 기준으로 분류한다.

Q. error.response가 없으면 뭐야?
A. 서버 응답을 받지 못한 Network Error, CORS 문제, timeout 문제일 수 있다.

Q. 401과 403은 어떻게 처리해?
A. 401은 로그인 필요 또는 토큰 만료, 403은 권한 없음으로 처리한다.

Q. Axios 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자 메시지와 개발자 로그를 분리해야 한다.

---

# 12. fetch vs Axios Comparison

## 12.1 fetch와 Axios 비교

### [개념]

fetch와 Axios는 모두 HTTP Request를 보내는 도구다.

fetch는 브라우저 기본 API이고 Axios는 외부 라이브러리다.

두 방식 모두 REST API Integration에 사용할 수 있지만 공통 처리, 에러 처리, 인증 헤더 처리 방식이 다르다.

---

### [핵심]

비교:

| 비교            | fetch                   | Axios                 |
| --------------- | ----------------------- | --------------------- |
| 성격            | 브라우저 기본 API       | 외부 라이브러리       |
| 설치            | 불필요                  | 필요                  |
| JSON Request    | `JSON.stringify()` 필요 | 자동 처리 편리        |
| JSON Response   | `response.json()` 필요  | `response.data`       |
| HTTP Error      | `response.ok` 직접 확인 | catch에서 처리 가능   |
| baseURL         | 직접 구현               | Axios Instance        |
| Interceptor     | 직접 구현 필요          | 제공                  |
| Timeout         | 직접 구현 필요          | 설정 가능             |
| Query Parameter | URLSearchParams         | `params` 옵션         |
| 인증 Header     | 직접 처리               | Interceptor 처리 가능 |
| 적합            | 단순 요청               | 실무 API Layer        |

선택 기준:

```text
간단한 프로젝트 / 의존성 최소화 → fetch
공통 baseURL / token / error handling 필요 → Axios
Server State 캐싱 필요 → TanStack Query + fetch or Axios
```

---

### [실무]

fetch 방식:

```javascript
export async function getFestivals() {
  const response = await fetch("/api/festivals");

  if (!response.ok) {
    throw new Error("Failed to load festivals");
  }

  return await response.json();
}
```

Axios 방식:

```javascript
export async function getFestivals() {
  const response = await publicApi.get("/festivals");
  return response.data;
}
```

실무 권장:

- 프로젝트에서 fetch와 Axios를 무분별하게 혼용하지 않음
- API Layer 기준을 통일
- Error Handling 방식 통일
- 인증 Header 처리 방식 통일
- Response DTO Mapping 기준 통일
- TanStack Query의 queryFn 내부에서는 fetch 또는 Axios 둘 다 사용 가능

---

### [FAQ]

Q. fetch와 Axios 중 뭐가 좋아?
A. 간단한 요청은 fetch로 충분하고 공통 baseURL, interceptor, 응답 처리, 인증 헤더가 많으면 Axios가 편할 수 있다.

Q. fetch와 Axios를 같이 써도 돼?
A. 가능은 하지만 프로젝트 유지보수를 위해 하나의 API 호출 기준으로 통일하는 것이 좋다.

Q. Axios를 쓰면 TanStack Query를 못 써?
A. 아니다. TanStack Query의 queryFn 내부에서 Axios를 사용할 수 있다.

Q. 실무에서는 fetch보다 Axios를 더 많이 써?
A. 프로젝트마다 다르지만 공통 설정, interceptor, Error Handling이 필요한 경우 Axios가 편한 경우가 많다.

---

# 13. Direct Axios vs Axios Instance

## 13.1 Direct Axios와 Axios Instance 비교

### [개념]

Direct Axios는 `axios.get()`, `axios.post()`를 직접 사용하는 방식이다.

Axios Instance는 `axios.create()`로 baseURL, timeout, headers, interceptor 같은 공통 설정을 가진 객체를 만들어 사용하는 방식이다.

---

### [핵심]

Direct Axios:

- 빠른 테스트 가능
- 설정 반복 발생
- baseURL 반복
- Header 반복
- Error Handling 기준 분산
- 인증 Header 중복 가능

Axios Instance:

- baseURL 통일
- timeout 통일
- publicApi / authApi 분리
- Authorization Header 공통 처리
- Response Error Handling 공통화
- API Layer에 적합

비교:

| 비교        | Direct Axios   | Axios Instance    |
| ----------- | -------------- | ----------------- |
| 사용 방식   | `axios.get()`  | `publicApi.get()` |
| baseURL     | 매번 작성 가능 | 공통 설정         |
| 인증 Header | 매번 작성 가능 | interceptor 처리  |
| 유지보수    | 낮음           | 높음              |
| 실무 적합성 | 단순 테스트    | 실무 API Layer    |

---

### [실무]

Direct Axios 예:

```javascript
export async function getFestivals() {
  const response = await axios.get("http://localhost:8080/api/festivals");
  return response.data;
}
```

Axios Instance 예:

```javascript
export const publicApi = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
  timeout: 10000,
});
```

```javascript
export async function getFestivals() {
  const response = await publicApi.get("/festivals");
  return response.data;
}
```

권장:

- 실무 프로젝트는 Axios Instance 사용
- 공개 요청과 인증 요청 분리
- baseURL은 환경변수로 관리
- token header는 authApi interceptor에서 처리
- API 함수는 instance를 사용해 작성

---

### [FAQ]

Q. Direct Axios를 써도 돼?
A. 간단한 테스트는 가능하지만 실무에서는 baseURL, Header, Error Handling 중복이 생기므로 Axios Instance가 좋다.

Q. Axios Instance는 왜 만들어?
A. baseURL, 인증 헤더, timeout, error handling 같은 공통 설정을 반복하지 않기 위해 만든다.

Q. publicApi와 authApi를 나누는 이유는?
A. 인증이 필요 없는 요청과 Authorization Header가 필요한 요청을 명확히 구분하기 위해서다.

Q. Axios Instance를 쓰면 API 함수가 더 짧아져?
A. 그렇다. 공통 baseURL과 header 설정을 instance가 담당하므로 API 함수는 resource path와 params/body에 집중할 수 있다.

---

# 14. API Layer with fetch and Axios

## 14.1 API Layer 적용 기준

### [개념]

API Layer는 Component에서 직접 fetch나 Axios를 호출하지 않고 API 함수로 분리하는 구조다.

fetch를 쓰든 Axios를 쓰든 API Layer 분리는 유지보수와 Retrieval 품질에 중요하다.

---

### [핵심]

API Layer가 숨기는 정보:

- Request URL
- HTTP Method
- Query Parameter
- Path Variable
- Request Body
- Request Header
- Response DTO Mapping
- Error Handling
- publicApi / authApi 선택

Component가 알아야 하는 정보:

- 어떤 API 함수를 호출할지
- 어떤 parameter를 넘길지
- Loading / Error / Empty를 어떻게 보여줄지
- 성공 후 어떤 UI 상태를 갱신할지

---

### [실무]

fetch API Layer 예:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await fetch(`/api/festivals/${festivalId}`);

  if (!response.ok) {
    throw new Error("Failed to load festival detail");
  }

  return await response.json();
}
```

Axios API Layer 예:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data;
}
```

Component 사용 예:

```javascript
useEffect(() => {
  async function loadFestival() {
    try {
      setLoading(true);
      const data = await getFestivalDetail(festivalId);
      setFestival(data);
    } catch (error) {
      setError(error);
    } finally {
      setLoading(false);
    }
  }

  loadFestival();
}, [festivalId]);
```

권장:

- API 함수 이름은 동작 중심
- Component는 API URL을 직접 작성하지 않음
- API 함수는 response wrapper 처리 기준을 통일
- Error Mapping 위치를 프로젝트 기준으로 통일
- TanStack Query 사용 시 API 함수는 queryFn / mutationFn으로 재사용

---

### [FAQ]

Q. fetch를 써도 API Layer를 만들어야 해?
A. API가 많아질수록 만드는 것이 좋다. URL, Method, Error Handling 중복을 줄일 수 있다.

Q. Axios를 쓰면 Component에서 바로 호출해도 돼?
A. 작은 실습은 가능하지만 실무에서는 API 함수로 분리하는 것이 유지보수에 좋다.

Q. API Layer에서 Error Handling까지 해야 해?
A. 공통 Error Mapping은 가능하지만 화면별 UI 처리는 Component나 custom hook에서 담당하는 경우가 많다.

Q. TanStack Query를 쓰면 API Layer가 필요 없어?
A. 아니다. queryFn과 mutationFn에서 재사용할 API 함수가 필요하다.

---

# 15. Response DTO Mapping with fetch and Axios

## 15.1 응답 구조 처리 기준

### [개념]

Response DTO Mapping은 fetch나 Axios로 받은 Backend 응답을 Frontend에서 사용할 수 있는 구조로 해석하는 작업이다.

fetch와 Axios는 응답 객체 구조가 다르지만 Backend Response Body 구조는 동일하게 확인해야 한다.

---

### [핵심]

fetch 응답 처리:

- response
- response.ok
- response.status
- response.json()
- parsed body

Axios 응답 처리:

- response
- response.status
- response.data
- response.data.data
- error.response.data

공통 확인:

- ApiResponse wrapper
- data field
- content field
- Page Response
- Slice Response
- nullable field
- date string
- enum string
- error response shape

---

### [실무]

Backend ApiResponse 예:

```json
{
  "success": true,
  "message": "조회 성공",
  "data": {
    "festivalId": 1,
    "title": "Spring Festival"
  }
}
```

fetch 처리:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await fetch(`/api/festivals/${festivalId}`);

  if (!response.ok) {
    throw new Error("Failed to load festival");
  }

  const body = await response.json();

  return body.data;
}
```

Axios 처리:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);

  return response.data.data;
}
```

Page Response 예:

```json
{
  "success": true,
  "message": "조회 성공",
  "data": {
    "content": [],
    "number": 0,
    "size": 20,
    "totalPages": 0,
    "totalElements": 0
  }
}
```

목록 content 반환 예:

```javascript
export async function getFestivals(params) {
  const response = await publicApi.get("/festivals", { params });

  return response.data.data.content;
}
```

주의:

- 실제 Response Body를 Network 탭에서 확인
- `response.data`와 Backend `data` 필드 혼동 주의
- wrapper unwrap 위치 통일
- `.map()` 호출 전 배열인지 확인
- null 가능 필드 방어 처리
- TypeScript 사용 시 Response Type과 실제 응답 동기화

---

### [FAQ]

Q. fetch와 Axios의 응답 처리 차이는?
A. fetch는 `response.json()`으로 body를 파싱하고 Axios는 보통 `response.data`에 body가 들어 있다.

Q. response.data.data는 왜 나와?
A. Axios의 `response.data` 안에 Backend ApiResponse의 `data` 필드가 다시 있기 때문이다.

Q. map is not a function은 왜 나?
A. 배열이라고 생각한 값이 실제로는 ApiResponse wrapper 객체이거나 undefined일 수 있다.

Q. 응답 구조는 어디서 확인해야 해?
A. 브라우저 개발자 도구 Network 탭의 Response Body에서 실제 구조를 확인한다.

---

# 16. Common Mistakes

## 16.1 fetch and Axios 공통 실수

### [개념]

fetch와 Axios 사용 실수는 주로 Error Handling, JSON 처리, Response Shape, Header, Query Parameter 처리 방식 차이를 혼동해서 발생한다.

---

### [핵심]

fetch 실수:

- response.ok 확인 누락
- response.json() 호출 누락
- JSON.stringify 누락
- Content-Type 누락
- 400 / 500이 자동 throw된다고 착각
- 204 응답에 response.json() 호출
- 공통 error handling 없이 API마다 중복 처리
- baseURL 반복 하드코딩

Axios 실수:

- response.data 구조 착각
- response.data.data wrapper 혼동
- Query Parameter를 `params`에 넣지 않음
- POST config를 두 번째 인자로 착각
- DELETE body 전달 방식 착각
- AxiosError 구조 확인 누락
- interceptor에서 error를 삼킴
- publicApi / authApi 구분 누락

공통 실수:

- Component마다 API URL 하드코딩
- Authorization Header 누락
- Bearer prefix 누락
- API Layer 미분리
- Network 탭 확인 없이 코드만 수정
- Error State와 Empty State 혼동
- 서버 에러 원문 화면 노출
- Postman 성공을 Browser 성공으로 착각
- CORS를 Frontend 코드만으로 해결하려 함

---

### [실무]

문제 해결 Flow:

```text
API Problem
→ fetch or Axios 사용 방식 확인
→ Request URL 확인
→ Request Method 확인
→ Query Parameter / Body 확인
→ Authorization Header 확인
→ Status Code 확인
→ Response Body 확인
→ Response Mapping 수정
```

fetch 문제 예:

```text
문제: 500 응답인데 catch가 실행되지 않는다고 생각함
원인: fetch는 HTTP Error를 자동 throw하지 않음
해결: response.ok 확인 후 직접 throw
```

Axios 문제 예:

```text
문제: 목록에서 map is not a function
원인: response.data가 배열이 아니라 ApiResponse wrapper
해결: response.data.data.content 구조 확인
```

Header 문제 예:

```text
문제: token은 localStorage에 있는데 401 발생
원인: Authorization Header에 Bearer token이 포함되지 않음
해결: authApi interceptor와 Network Request Headers 확인
```

---

### [FAQ]

Q. fetch에서 가장 흔한 실수는?
A. `response.ok`를 확인하지 않거나 `JSON.stringify()`와 `response.json()`을 누락하는 것이다.

Q. Axios에서 가장 흔한 실수는?
A. `response.data`와 Backend ApiResponse의 `data` 필드를 혼동하는 것이다.

Q. Query Parameter는 fetch와 Axios에서 어떻게 달라?
A. fetch는 URLSearchParams로 직접 URL에 붙이고 Axios는 `{ params }` 옵션을 사용한다.

Q. API 연동 문제는 어떻게 찾는 게 좋아?
A. Network 탭에서 실제 Request URL, Method, Header, Payload, Status Code, Response Body를 먼저 확인한다.

---

# 17. Part02 Checklist

## 17.1 fetch and Axios 검수 기준

### [개념]

Part02 fetch and Axios 문서는 Frontend Agent가 REST API Request Tool을 선택하고, fetch 또는 Axios로 API Layer 코드를 생성할 수 있도록 만드는 문서다.

---

### [핵심]

Checklist:

```md
- [ ] fetch 기본 개념이 포함되었는가?
- [ ] fetch GET 기준이 포함되었는가?
- [ ] fetch POST 기준이 포함되었는가?
- [ ] fetch PUT / PATCH / DELETE 기준이 포함되었는가?
- [ ] fetch Error Handling 기준이 포함되었는가?
- [ ] fetch Wrapper 기준이 포함되었는가?
- [ ] Axios 기본 개념이 포함되었는가?
- [ ] Axios GET 기준이 포함되었는가?
- [ ] Axios POST 기준이 포함되었는가?
- [ ] Axios PUT / PATCH / DELETE 기준이 포함되었는가?
- [ ] Axios Error Handling 기준이 포함되었는가?
- [ ] fetch vs Axios 비교가 포함되었는가?
- [ ] Direct Axios vs Axios Instance 비교가 포함되었는가?
- [ ] API Layer 적용 기준이 포함되었는가?
- [ ] Response DTO Mapping 기준이 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ fetch Request Check
→ fetch Error Handling Check
→ Axios Request Check
→ Axios Error Handling Check
→ Comparison Check
→ API Layer Check
→ Response Mapping Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

최종 기준:

- fetch와 Axios 차이를 구분 가능
- fetch에서 response.ok 필요성을 설명 가능
- Axios에서 response.data 구조를 설명 가능
- Query Parameter 처리 방식을 구분 가능
- POST Body 전달 방식을 구분 가능
- API Layer 분리 기준을 적용 가능
- Response DTO Mapping 오류를 분석 가능
- Frontend Agent가 fetch 또는 Axios API 함수를 생성 가능

---

### [FAQ]

Q. Part02의 목적은 뭐야?
A. Frontend Agent가 fetch와 Axios 사용 기준을 이해하고 API 요청 함수를 정확히 생성하게 만드는 것이다.

Q. Part02에서 가장 중요한 기준은 뭐야?
A. fetch의 response.ok 처리, Axios의 response.data 처리, Query Parameter와 Request Body 전달 방식 차이다.

Q. Part02만 보면 API 연동을 전부 할 수 있어?
A. 기본 요청 함수 작성은 가능하지만 Axios Instance, Interceptor, TanStack Query, Pagination은 후속 Part에서 더 자세히 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. fetch는 뭐야?
A. 브라우저가 기본 제공하는 HTTP 요청 API다. 외부 라이브러리 없이 REST API를 호출할 수 있다.

Q. fetch는 언제 쓰면 좋아?
A. 간단한 요청, 의존성 최소화, 브라우저 기본 API만 사용하는 프로젝트에 적합하다.

Q. fetch는 404나 500이면 catch로 바로 가?
A. 아니다. 네트워크 오류가 아니면 catch로 바로 가지 않는다. `response.ok`를 직접 확인해야 한다.

Q. fetch에서 JSON 응답은 어떻게 꺼내?
A. `await response.json()`을 호출해 Response Body를 JavaScript 객체로 변환한다.

Q. fetch GET 요청은 언제 써?
A. 서버 데이터를 조회할 때 사용한다. 목록 조회, 상세 조회, 검색, 필터 조회에 사용한다.

Q. fetch GET에서 Query Parameter는 어떻게 붙여?
A. `URLSearchParams`를 사용해 `?key=value` 형태의 query string을 만들 수 있다.

Q. GET 요청에 body를 넣어도 돼?
A. 권장하지 않는다. 조회 조건은 Query Parameter로 전달한다.

Q. fetch POST는 언제 써?
A. 리뷰 작성, 회원가입, 로그인, 데이터 생성처럼 서버에 데이터를 보낼 때 사용한다.

Q. fetch POST에서 body는 왜 JSON.stringify를 해?
A. JavaScript 객체를 JSON 문자열로 변환해 서버에 보내야 하기 때문이다.

Q. fetch POST에서 Content-Type은 왜 필요해?
A. 서버가 Request Body를 JSON으로 해석할 수 있도록 `application/json`을 알려주기 위해 필요하다.

Q. PUT과 PATCH 차이는?
A. PUT은 전체 수정에 가깝고 PATCH는 일부 필드 수정에 가깝다.

Q. DELETE 요청에는 body를 넣어도 돼?
A. 프로젝트 기준에 따라 다르지만 보통 Path Variable로 삭제 대상을 식별한다.

Q. 204 응답은 어떻게 처리해?
A. Response Body가 없을 수 있으므로 `response.json()`을 바로 호출하지 않고 status를 확인한다.

Q. Network Error와 HTTP Error는 달라?
A. 다르다. Network Error는 응답 자체를 받지 못한 경우이고 HTTP Error는 서버가 오류 상태 코드를 응답한 경우다.

Q. CORS 에러는 response.status로 확인할 수 있어?
A. 대부분 response를 정상적으로 받지 못하므로 Console과 Network 탭의 preflight 요청을 확인해야 한다.

Q. fetch Wrapper는 왜 만들어?
A. baseURL, Header, response.ok, Error Handling 같은 반복 코드를 줄이고 요청 기준을 통일하기 위해 만든다.

Q. fetch Wrapper를 만들면 Axios가 필요 없어?
A. 간단한 프로젝트에서는 가능하다. 하지만 interceptor, error object, 공통 설정이 많으면 Axios가 더 편할 수 있다.

Q. Axios는 뭐야?
A. HTTP 요청을 쉽게 작성할 수 있는 JavaScript 라이브러리다.

Q. Axios는 언제 쓰면 좋아?
A. baseURL, 인증 헤더, interceptor, 공통 에러 처리, API Layer가 필요한 프로젝트에 적합하다.

Q. Axios 응답 데이터는 어디에 있어?
A. 보통 `response.data`에 있다.

Q. Axios는 JSON.stringify를 직접 해야 해?
A. 일반적인 JSON 요청에서는 requestBody 객체를 그대로 전달하면 Axios가 자동 처리한다.

Q. Axios에서 query parameter는 어떻게 보내?
A. `axios.get(url, { params: { keyword: "flower" } })` 형태로 보낸다.

Q. Axios GET에서 body를 보내?
A. 권장하지 않는다. 조회 조건은 `params` 옵션으로 보낸다.

Q. Axios POST body는 어디에 넣어?
A. `axios.post(url, requestBody)`처럼 두 번째 인자에 넣는다.

Q. Axios POST에서 Header는 어디에 넣어?
A. 세 번째 인자인 config 객체에 `headers`로 넣는다.

Q. 로그인 API는 publicApi야 authApi야?
A. 로그인 전 요청이므로 보통 publicApi를 사용한다.

Q. Axios PUT body는 어디에 넣어?
A. `axios.put(url, requestBody)`처럼 두 번째 인자에 넣는다.

Q. Axios PATCH body는 어디에 넣어?
A. `axios.patch(url, requestBody)`처럼 두 번째 인자에 넣는다.

Q. Axios DELETE에서 body를 보내려면 어떻게 해?
A. `axios.delete(url, { data: requestBody })` 형태를 사용한다.

Q. DELETE 성공 후 response.data가 없을 수 있어?
A. 있다. Backend가 204 No Content를 반환하면 응답 body가 없을 수 있다.

Q. Axios Error는 어떻게 확인해?
A. `axios.isAxiosError(error)`로 확인하고 `error.response?.status`를 기준으로 분류한다.

Q. error.response가 없으면 뭐야?
A. 서버 응답을 받지 못한 Network Error, CORS 문제, timeout 문제일 수 있다.

Q. 401과 403은 어떻게 처리해?
A. 401은 로그인 필요 또는 토큰 만료, 403은 권한 없음으로 처리한다.

Q. Axios 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자 메시지와 개발자 로그를 분리해야 한다.

Q. fetch와 Axios 중 뭐가 좋아?
A. 간단한 요청은 fetch로 충분하고 공통 baseURL, interceptor, 응답 처리, 인증 헤더가 많으면 Axios가 편할 수 있다.

Q. fetch와 Axios를 같이 써도 돼?
A. 가능은 하지만 프로젝트 유지보수를 위해 하나의 API 호출 기준으로 통일하는 것이 좋다.

Q. Axios를 쓰면 TanStack Query를 못 써?
A. 아니다. TanStack Query의 queryFn 내부에서 Axios를 사용할 수 있다.

Q. Direct Axios를 써도 돼?
A. 간단한 테스트는 가능하지만 실무에서는 baseURL, Header, Error Handling 중복이 생기므로 Axios Instance가 좋다.

Q. Axios Instance는 왜 만들어?
A. baseURL, 인증 헤더, timeout, error handling 같은 공통 설정을 반복하지 않기 위해 만든다.

Q. publicApi와 authApi를 나누는 이유는?
A. 인증이 필요 없는 요청과 Authorization Header가 필요한 요청을 명확히 구분하기 위해서다.

Q. fetch를 써도 API Layer를 만들어야 해?
A. API가 많아질수록 만드는 것이 좋다. URL, Method, Error Handling 중복을 줄일 수 있다.

Q. Axios를 쓰면 Component에서 바로 호출해도 돼?
A. 작은 실습은 가능하지만 실무에서는 API 함수로 분리하는 것이 유지보수에 좋다.

Q. API Layer에서 Error Handling까지 해야 해?
A. 공통 Error Mapping은 가능하지만 화면별 UI 처리는 Component나 custom hook에서 담당하는 경우가 많다.

Q. TanStack Query를 쓰면 API Layer가 필요 없어?
A. 아니다. queryFn과 mutationFn에서 재사용할 API 함수가 필요하다.

Q. fetch와 Axios의 응답 처리 차이는?
A. fetch는 `response.json()`으로 body를 파싱하고 Axios는 보통 `response.data`에 body가 들어 있다.

Q. response.data.data는 왜 나와?
A. Axios의 `response.data` 안에 Backend ApiResponse의 `data` 필드가 다시 있기 때문이다.

Q. map is not a function은 왜 나?
A. 배열이라고 생각한 값이 실제로는 ApiResponse wrapper 객체이거나 undefined일 수 있다.

Q. 응답 구조는 어디서 확인해야 해?
A. 브라우저 개발자 도구 Network 탭의 Response Body에서 실제 구조를 확인한다.

Q. fetch에서 가장 흔한 실수는?
A. `response.ok`를 확인하지 않거나 `JSON.stringify()`와 `response.json()`을 누락하는 것이다.

Q. Axios에서 가장 흔한 실수는?
A. `response.data`와 Backend ApiResponse의 `data` 필드를 혼동하는 것이다.

Q. Query Parameter는 fetch와 Axios에서 어떻게 달라?
A. fetch는 URLSearchParams로 직접 URL에 붙이고 Axios는 `{ params }` 옵션을 사용한다.

Q. API 연동 문제는 어떻게 찾는 게 좋아?
A. Network 탭에서 실제 Request URL, Method, Header, Payload, Status Code, Response Body를 먼저 확인한다.

Q. Part02 fetch and Axios의 목적은 뭐야?
A. Frontend Agent가 fetch와 Axios 사용 기준을 이해하고 API 요청 함수를 정확히 생성하게 만드는 것이다.

Q. Part02 다음에는 어떤 문서가 이어지면 좋아?
A. Axios Instance, Interceptor, API Layer Separation, Response Mapping, UI State, TanStack Query 순서로 이어지는 것이 좋다.
