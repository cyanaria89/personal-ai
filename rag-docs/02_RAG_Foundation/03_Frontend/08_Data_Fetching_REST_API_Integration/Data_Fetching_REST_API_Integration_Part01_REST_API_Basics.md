# Data Fetching & REST API Integration Part01 - REST API Basics

---

# 1. REST API Integration Overview

## 1.1 REST API Integration 개념

### [개념]

REST API Integration은 Frontend가 Backend REST API를 호출하여 서버 데이터를 조회, 생성, 수정, 삭제하고 그 결과를 UI 상태에 반영하는 작업이다.

Frontend는 사용자의 화면 진입, 버튼 클릭, Form 제출, 검색 조건 변경 같은 Trigger를 기준으로 API Request를 생성한다.

REST API Integration의 핵심은 아래 요소를 정확히 연결하는 것이다.

```text
Frontend UI
→ API Function
→ HTTP Request
→ Backend Controller
→ Response DTO
→ Frontend State
→ UI Render
```

---

### [핵심]

REST API Integration 핵심 요소:

- HTTP Method
- URL Path
- Path Variable
- Query Parameter
- Request Header
- Authorization Header
- Request Body
- Response Body
- Response DTO
- Status Code
- JSON
- API Layer
- Loading State
- Error State
- Empty State
- Network Debugging

REST API Integration 목적:

- Backend API 명세 기반 Frontend API 함수 작성
- 요청 URL / Method / Parameter / Body / Header 구성
- 응답 DTO를 Frontend Type 또는 State로 Mapping
- 성공 / 실패 / 빈 데이터 상태 처리
- Network 탭으로 실제 요청과 응답 검증

---

### [실무]

2026 실무 기준에서 REST API Integration은 단순히 `fetch()`나 `axios.get()`을 호출하는 작업이 아니다.

실무 기준:

- Component 안에 API URL을 직접 하드코딩하지 않음
- API 함수는 `api` layer로 분리
- 공개 API와 인증 API를 구분
- `publicApi` / `authApi` Axios Instance 사용
- Query Parameter와 Path Variable을 명확히 구분
- Request Body는 Backend DTO 필드명과 일치
- Response DTO 구조를 실제 응답 기준으로 확인
- Loading / Error / Empty / Success 상태를 분리
- API 오류는 Network 탭에서 Request URL, Method, Status Code, Response Body를 먼저 확인

기본 Flow:

```text
User Action
→ API Function Call
→ Build Request
→ Send HTTP Request
→ Receive Response
→ Map Response DTO
→ Update Server State or Component State
→ Render UI
```

예:

```text
FestivalListPage Mount
→ getFestivals(params)
→ GET /api/festivals?keyword=flower&page=0&size=20
→ Festival Page Response
→ content mapping
→ FestivalList Render
```

---

### [FAQ]

Q. REST API Integration이 뭐야?
A. Frontend가 HTTP Method, URL, Header, Body, Query Parameter를 사용해 Backend API와 데이터를 주고받는 작업이다.

Q. Frontend가 REST API를 왜 알아야 해?
A. 어떤 URL, Method, Parameter, Body, Header로 요청해야 하는지 알아야 Backend와 정상 연동할 수 있기 때문이다.

Q. API 호출 코드는 Component 안에 써도 돼?
A. 간단한 실습은 가능하지만 실무에서는 api 함수, custom hook, TanStack Query 등으로 분리하는 것이 좋다.

Q. API 연동에서 가장 먼저 확인할 것은 뭐야?
A. Backend API 명세의 URL, Method, Query Parameter, Path Variable, Request Body, Response DTO, 인증 필요 여부를 확인한다.

---

# 2. HTTP Method Rules

## 2.1 HTTP Method 기준

### [개념]

HTTP Method는 REST API에서 요청의 목적을 표현하는 방식이다.

Frontend는 Backend API 명세에 맞는 HTTP Method를 사용해야 한다.

주요 HTTP Method:

| Method | 목적      | 예                  |
| ------ | --------- | ------------------- |
| GET    | 조회      | 축제 목록 조회      |
| POST   | 생성      | 리뷰 작성           |
| PUT    | 전체 수정 | 회원 정보 전체 수정 |
| PATCH  | 부분 수정 | 알림 읽음 처리      |
| DELETE | 삭제      | 찜 취소             |

---

### [핵심]

HTTP Method 선택 기준:

- `GET`: 서버 데이터 조회
- `POST`: 서버 데이터 생성
- `PUT`: 리소스 전체 수정
- `PATCH`: 리소스 일부 수정
- `DELETE`: 리소스 삭제

요청 데이터 기준:

- GET → Query Parameter / Path Variable
- POST → Request Body
- PUT → Request Body
- PATCH → Request Body
- DELETE → Path Variable 중심, 필요 시 Query Parameter

주의 키워드:

- GET Request Body 금지
- POST 생성
- PUT 전체 수정
- PATCH 부분 수정
- DELETE 삭제
- Backend Controller Mapping 일치
- HTTP Method 불일치 404 / 405 가능

---

### [실무]

GET 예:

```javascript
export async function getFestivals(params) {
  const response = await publicApi.get("/festivals", { params });
  return response.data;
}
```

POST 예:

```javascript
export async function createReview(requestBody) {
  const response = await authApi.post("/reviews", requestBody);
  return response.data;
}
```

PATCH 예:

```javascript
export async function markNotificationRead(notificationId) {
  const response = await authApi.patch(`/notifications/${notificationId}/read`);
  return response.data;
}
```

DELETE 예:

```javascript
export async function deleteFavorite(festivalId) {
  const response = await authApi.delete(`/favorites/${festivalId}`);
  return response.data;
}
```

실무 검증 기준:

```text
API Error
→ Network Tab
→ Request Method 확인
→ Request URL 확인
→ Backend Controller Mapping 확인
→ Status Code 확인
```

---

### [FAQ]

Q. GET과 POST 차이는?
A. GET은 데이터 조회에 사용하고 POST는 새로운 데이터 생성이나 명령성 요청에 사용한다.

Q. PUT과 PATCH 차이는?
A. PUT은 리소스 전체 수정에 가깝고 PATCH는 특정 필드만 수정하는 부분 수정에 가깝다.

Q. GET 요청에도 body를 넣어도 돼?
A. 권장하지 않는다. 조회 조건은 보통 Query Parameter로 전달한다.

Q. HTTP Method가 틀리면 어떤 문제가 생겨?
A. Backend Mapping과 맞지 않아 404, 405, CORS preflight 실패, 의도하지 않은 API 실패가 발생할 수 있다.

---

# 3. URL Path Rules

## 3.1 URL Path 기본

### [개념]

URL Path는 API Resource의 위치를 표현하는 주소다.

Frontend는 Backend Controller Mapping과 일치하는 URL Path로 요청해야 한다.

예:

```text
GET /api/festivals
GET /api/festivals/1
POST /api/reviews
PATCH /api/notifications/10/read
DELETE /api/favorites/1
```

---

### [핵심]

URL Path 구성 요소:

- baseURL
- API prefix
- resource path
- nested resource
- Path Variable
- Query Parameter
- trailing slash 기준
- plural naming
- Backend Controller Mapping

주의 대상:

- `/festival` vs `/festivals`
- `/api` prefix 누락
- Path Variable undefined
- Frontend Route와 Backend API Route 혼동
- SPA fallback으로 index.html 응답
- 개발 서버 proxy 경로 불일치
- Backend `@RequestMapping`과 Frontend API path 불일치

---

### [실무]

Axios Instance에서 baseURL을 분리한다.

```javascript
export const publicApi = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
  timeout: 10000,
});
```

API 함수에서는 resource path만 관리한다.

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data;
}
```

URL Path Debug Flow:

```text
404 발생
→ Network Tab Request URL 확인
→ baseURL 확인
→ API prefix 확인
→ resource path 확인
→ Path Variable 값 확인
→ Backend Controller Mapping 확인
```

잘못된 예:

```javascript
publicApi.get(`/festivals/${undefined}`);
```

올바른 검증 예:

```javascript
export async function getFestivalDetail(festivalId) {
  if (!festivalId) {
    throw new Error("festivalId is required");
  }

  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data;
}
```

---

### [FAQ]

Q. API 404가 나면 뭘 확인해?
A. Request URL, Method, baseURL, API prefix, Path Variable 값, Backend Controller Mapping을 확인한다.

Q. `/festival`과 `/festivals`가 다르면 문제가 돼?
A. 된다. Backend Mapping과 Frontend 요청 URL이 정확히 일치해야 한다.

Q. JSON을 기대했는데 HTML이 응답돼?
A. API 요청이 SPA fallback에 걸려 index.html을 받은 경우일 수 있다. 요청 URL과 서버 fallback 설정을 확인한다.

Q. Frontend Route와 Backend API Endpoint는 달라?
A. 다르다. Frontend Route는 화면 경로이고 Backend API Endpoint는 서버 데이터 요청 경로다.

---

# 4. Path Variable Rules

## 4.1 Path Variable 기준

### [개념]

Path Variable은 URL Path 일부에 포함되어 특정 Resource를 식별하는 값이다.

예:

```text
GET /api/festivals/1
DELETE /api/reviews/10
PATCH /api/notifications/5/read
```

여기서 `1`, `10`, `5`는 Path Variable이다.

---

### [핵심]

Path Variable 사용 대상:

- festivalId
- reviewId
- userId
- notificationId
- postId
- commentId
- resource id
- nested resource id

Path Variable 특징:

- 특정 Resource 식별
- URL Path에 직접 포함
- 상세 조회 / 수정 / 삭제에 자주 사용
- undefined 전달 시 잘못된 URL 생성
- Route Param과 API Path Variable Mapping 필요

---

### [실무]

기본 예:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data;
}
```

삭제 예:

```javascript
export async function deleteReview(reviewId) {
  const response = await authApi.delete(`/reviews/${reviewId}`);
  return response.data;
}
```

주의:

- `undefined`가 URL에 들어가지 않도록 검증
- 숫자 ID는 필요 시 Number 변환
- 문자열 ID는 URL encoding 검토
- React Router `useParams()` 값은 문자열일 수 있음
- Backend DTO 필드명과 Route Param 이름을 혼동하지 않음

Route Param 연결 예:

```javascript
const { festivalId } = useParams();

useEffect(() => {
  if (!festivalId) {
    return;
  }

  getFestivalDetail(Number(festivalId));
}, [festivalId]);
```

---

### [FAQ]

Q. Path Variable은 언제 써?
A. 특정 리소스를 식별할 때 사용한다. 예: 축제 상세, 리뷰 삭제, 알림 읽음 처리.

Q. URL에 undefined가 들어가는 이유는?
A. Route param이나 함수 인자가 undefined인데 검증 없이 문자열 template에 넣었을 가능성이 있다.

Q. Path Variable과 id는 같은 말이야?
A. 항상 같지는 않지만 실무에서는 특정 Resource ID를 URL Path에 넣는 경우가 많다.

Q. `useParams()` 값은 바로 숫자로 써도 돼?
A. React Router에서 받은 값은 문자열일 수 있으므로 필요한 경우 Number 변환과 검증을 한다.

---

# 5. Query Parameter Rules

## 5.1 Query Parameter 기준

### [개념]

Query Parameter는 URL 뒤에 `?key=value` 형태로 붙는 요청 옵션이다.

검색, 필터, 정렬, 페이지네이션 같은 조회 조건에 사용한다.

예:

```text
GET /api/festivals?keyword=flower&page=0&size=20
GET /api/calendar/monthly?targetMonth=2026-07
```

---

### [핵심]

Query Parameter 사용 대상:

- keyword
- region
- theme
- startDate
- endDate
- page
- size
- sort
- targetMonth
- cursor
- filter

Query Parameter 특징:

- 주로 GET 요청에서 사용
- 조회 조건 전달
- URL에 값이 노출됨
- undefined / null / empty string 처리 기준 필요
- page 0-based / 1-based 확인 필요
- 배열 parameter 직렬화 기준 필요

---

### [실무]

Axios Query Parameter 예:

```javascript
export async function searchFestivals(params) {
  const response = await publicApi.get("/festivals/search", {
    params,
  });

  return response.data;
}
```

요청 결과:

```text
GET /api/festivals/search?keyword=flower&page=0&size=20
```

빈 값 제거 예:

```javascript
function cleanParams(params) {
  return Object.fromEntries(
    Object.entries(params).filter(([, value]) => {
      return value !== undefined && value !== null && value !== "";
    }),
  );
}
```

검색 API 예:

```javascript
export async function searchFestivals(params) {
  const response = await publicApi.get("/festivals/search", {
    params: cleanParams(params),
  });

  return response.data;
}
```

주의:

- 빈 검색어를 보낼지 제거할지 프로젝트 기준 필요
- 날짜 형식은 Backend 기준과 일치
- Spring Pageable은 보통 `page=0`부터 시작
- UI page가 1부터라면 요청 시 `page - 1` 변환
- Query Parameter는 Request Body와 혼동하지 않음

---

### [FAQ]

Q. Query Parameter는 언제 써?
A. 검색, 필터, 정렬, 페이지 번호처럼 리소스 조회 옵션을 전달할 때 사용한다.

Q. Axios에서 query parameter는 어떻게 보내?
A. `axios.get(url, { params: { keyword: "flower" } })` 형태로 보낸다.

Q. page는 0부터 시작해 1부터 시작해?
A. Backend 기준에 따라 다르다. Spring Pageable은 보통 0-based라 Frontend 표시 page와 변환이 필요할 수 있다.

Q. 빈 검색어도 query parameter로 보내야 해?
A. 프로젝트 기준에 따라 다르다. 보통 빈 값은 제거하거나 Backend 기본값을 사용한다.

---

# 6. Path Variable vs Query Parameter

## 6.1 Path Variable과 Query Parameter 비교

### [개념]

Path Variable과 Query Parameter는 모두 URL에 값을 전달하지만 목적이 다르다.

Path Variable은 특정 Resource 식별에 사용한다.

Query Parameter는 조회 옵션, 검색 조건, 필터, 정렬, 페이지네이션에 사용한다.

---

### [핵심]

비교:

| 비교        | Path Variable              | Query Parameter             |
| ----------- | -------------------------- | --------------------------- |
| 목적        | Resource 식별              | 조회 조건                   |
| 위치        | URL Path 내부              | URL 뒤 `?key=value`         |
| 사용 예     | `/festivals/1`             | `/festivals?keyword=flower` |
| 주요 대상   | id                         | keyword, page, size, sort   |
| 사용 Method | GET / PUT / PATCH / DELETE | 주로 GET                    |
| 의미        | 어떤 리소스인가            | 어떤 조건인가               |

선택 기준:

```text
특정 데이터 1개 식별 → Path Variable
검색 / 필터 / 정렬 / 페이지 → Query Parameter
```

---

### [실무]

상세 조회:

```text
GET /api/festivals/1
```

```javascript
getFestivalDetail(1);
```

검색 조회:

```text
GET /api/festivals/search?keyword=flower&page=0
```

```javascript
searchFestivals({ keyword: "flower", page: 0 });
```

혼합 예:

```text
GET /api/festivals/1/reviews?page=0&size=10
```

의미:

```text
festivalId = 1인 축제의 리뷰 목록을 page 조건으로 조회
```

주의:

- `festivalId`는 Path Variable
- `page`, `size`는 Query Parameter
- id를 Query Parameter로 보내는 API도 가능하지만 REST Resource 식별은 Path Variable이 명확한 경우가 많음
- Backend API 명세를 우선한다

---

### [FAQ]

Q. Path Variable과 Query Parameter 차이는?
A. Path Variable은 리소스 식별에 사용하고 Query Parameter는 검색, 필터, 정렬 같은 조회 옵션에 사용한다.

Q. 축제 상세 조회는 Path Variable이 좋아?
A. 보통 `GET /festivals/{festivalId}`처럼 Path Variable을 사용한다.

Q. 검색어는 Path Variable로 보내?
A. 일반적으로 검색어는 Query Parameter로 보낸다.

Q. page와 size는 Path Variable이야?
A. 아니다. page와 size는 보통 Query Parameter로 전달한다.

---

# 7. Request Body Rules

## 7.1 Request Body 기준

### [개념]

Request Body는 POST / PUT / PATCH 요청에서 서버에 전달하는 JSON 데이터다.

Frontend Form 입력값이나 수정 데이터를 Backend DTO 구조에 맞게 전달한다.

예:

```json
{
  "festivalId": 1,
  "rating": 5,
  "content": "좋았어요"
}
```

---

### [핵심]

Request Body 사용 대상:

- login request
- signup request
- create request
- update request
- review request
- form submit
- JSON body
- DTO mapping

Request Body 특징:

- GET 요청에는 사용하지 않음
- POST / PUT / PATCH 중심
- Backend Request DTO 필드명과 일치 필요
- 숫자 / 문자열 / boolean 타입 확인
- 필수값 검증 후 요청
- 날짜 형식 통일 필요
- JSON 요청은 Content-Type 기준 확인

---

### [실무]

POST 예:

```javascript
export async function createReview(requestBody) {
  const response = await authApi.post("/reviews", requestBody);
  return response.data;
}
```

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

Form Submit Flow:

```text
Form Submit
→ Client Validation
→ Build Request Body
→ API Function Call
→ Backend Validation
→ Response DTO
→ Success or Error UI
```

주의:

- Request Body 필드명은 Backend DTO와 맞춘다
- `undefined` 필드를 그대로 보낼지 제거할지 기준 필요
- 서버 Validation Error는 field별 표시 가능
- GET 요청 조회 조건은 Query Parameter 사용
- Request Body와 FormData는 구분

---

### [FAQ]

Q. Request Body는 언제 써?
A. 데이터 생성, 수정, 로그인, 회원가입, 리뷰 작성처럼 서버에 JSON 데이터를 보낼 때 사용한다.

Q. Axios POST body는 어디에 넣어?
A. `axios.post(url, requestBody)`처럼 두 번째 인자에 넣는다.

Q. GET 요청에도 body를 넣어도 돼?
A. 권장하지 않는다. 조회 조건은 보통 Query Parameter로 전달한다.

Q. Request Body 필드명은 Frontend 마음대로 정해도 돼?
A. 아니다. Backend Request DTO가 기대하는 필드명과 타입에 맞춰야 한다.

---

# 8. Request Header Rules

## 8.1 Request Header 기준

### [개념]

Request Header는 HTTP 요청의 부가 정보를 전달하는 영역이다.

Frontend API 요청에서는 인증 토큰, JSON 타입, 파일 업로드 타입 같은 정보가 Header에 포함된다.

---

### [핵심]

주요 Header:

- Authorization
- Bearer Token
- Content-Type
- Accept
- multipart/form-data
- X-Request-ID
- CORS 관련 Header

Authorization Header 형식:

```text
Authorization: Bearer <accessToken>
```

JSON Header 형식:

```text
Content-Type: application/json
```

---

### [실무]

Authorization Header 예:

```javascript
authApi.interceptors.request.use((config) => {
  const accessToken = localStorage.getItem("accessToken");

  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }

  return config;
});
```

JSON 요청 예:

```javascript
await fetch("/api/reviews", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(requestBody),
});
```

Axios는 JSON 요청에서 Content-Type을 자동 처리하는 경우가 많다.

주의:

- Bearer 뒤 공백 필요
- token이 없으면 Authorization Header 생략
- 민감한 Header 값 console.log 금지
- multipart/form-data는 Content-Type 직접 설정을 피하는 경우가 많음
- Authorization Header가 CORS 허용 Header에 포함되어야 함
- 401 발생 시 Header 실제 포함 여부를 Network 탭에서 확인

---

### [FAQ]

Q. Authorization Header는 어떤 형식이야?
A. 일반적으로 `Authorization: Bearer <accessToken>` 형식을 사용한다.

Q. Authorization Header는 매 요청마다 직접 넣어야 해?
A. 가능하지만 interceptor에서 공통 처리하는 것이 유지보수에 좋다.

Q. token은 있는데 401이 나?
A. Authorization Header에 실제로 포함되었는지, Bearer 형식이 맞는지, token이 만료되지 않았는지 확인해야 한다.

Q. Content-Type은 언제 필요해?
A. JSON body를 보낼 때 `application/json`을 사용한다. Axios는 자동 처리하는 경우가 많다.

---

# 9. Response Body and DTO Mapping

## 9.1 Response Body 기준

### [개념]

Response Body는 Backend가 Frontend에 내려주는 응답 데이터다.

Frontend는 Response Body의 실제 구조를 확인하고 화면에 필요한 값으로 Mapping해야 한다.

공통 응답 Wrapper 예:

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

---

### [핵심]

Response Mapping 확인 대상:

- response.data
- response.data.data
- ApiResponse wrapper
- content
- page
- slice
- list
- detail
- nullable field
- enum value
- date string
- error response
- validation error response

주의 오류:

- `response.data.data` 혼동
- `content` 위치 착각
- 배열이 아닌 객체에 `.map()` 호출
- null 가능 필드 미처리
- Backend DTO 변경 후 Frontend Type 미수정
- JSON이 아니라 HTML 응답 수신

---

### [실무]

Axios 기본 응답:

```javascript
const response = await publicApi.get("/festivals/1");
console.log(response.data);
```

ApiResponse Wrapper 처리:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data.data;
}
```

Page Response 처리:

```javascript
export async function getFestivals(params) {
  const response = await publicApi.get("/festivals", { params });
  return response.data.data.content;
}
```

Debug Flow:

```text
UI 데이터 안 나옴
→ Network Response Body 확인
→ response.data 구조 확인
→ ApiResponse wrapper 확인
→ content 위치 확인
→ Component 접근 경로 수정
```

---

### [FAQ]

Q. Axios 응답 데이터는 어디에 있어?
A. 보통 `response.data`에 있다.

Q. response.data.data는 왜 나와?
A. Backend가 ApiResponse 같은 공통 wrapper로 응답하면 Axios response.data 안에 다시 data 필드가 있을 수 있다.

Q. map is not a function 오류는 왜 나?
A. 배열이라고 생각한 값이 실제로는 객체이거나 undefined일 수 있다. 응답 구조와 content 위치를 확인해야 한다.

Q. Backend 응답 필드명이 바뀌면 어떻게 돼?
A. Frontend Type과 mapping 함수, Component에서 사용하는 필드명을 함께 수정해야 한다.

---

# 10. Status Code Rules

## 10.1 HTTP Status Code 기준

### [개념]

HTTP Status Code는 API 요청 결과를 숫자로 표현하는 응답 코드다.

Frontend는 Status Code를 기준으로 성공, 검증 실패, 인증 실패, 권한 없음, 리소스 없음, 서버 오류를 구분한다.

---

### [핵심]

주요 Status Code:

| Status        | 의미           | Frontend 처리           |
| ------------- | -------------- | ----------------------- |
| 200           | 성공           | 데이터 표시             |
| 201           | 생성 성공      | 성공 메시지 / 목록 갱신 |
| 204           | 응답 body 없음 | 성공 처리               |
| 400           | 잘못된 요청    | 입력값 확인             |
| 401           | 인증 실패      | 로그인 유도 / 토큰 갱신 |
| 403           | 권한 없음      | 권한 없음 안내          |
| 404           | 리소스 없음    | Not Found UI            |
| 409           | 충돌           | 중복 / 상태 충돌 안내   |
| 422           | 검증 실패      | Validation Message 표시 |
| 500           | 서버 오류      | 서버 오류 안내          |
| Network Error | 연결 실패      | 네트워크 안내 / 재시도  |

---

### [실무]

Status Code 처리 기준:

```javascript
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

    if (status === 500) {
      return "서버 오류가 발생했습니다.";
    }
  }

  return "요청 처리 중 문제가 발생했습니다.";
}
```

주의:

- 401과 403을 같은 에러로 처리하지 않음
- 404는 API URL 문제와 Resource Not Found를 구분
- 500 상세 메시지는 사용자에게 직접 노출하지 않음
- Network Error와 서버 응답 오류를 구분
- Validation Error는 field별 메시지 표시 가능

---

### [FAQ]

Q. 401과 403은 어떻게 달라?
A. 401은 인증되지 않았거나 토큰이 유효하지 않은 경우이고 403은 인증은 되었지만 권한이 없는 경우다.

Q. 404가 나면 무조건 데이터가 없는 거야?
A. 아니다. API URL 오타, Method 불일치, Controller Mapping 불일치, Resource Not Found를 구분해야 한다.

Q. 500 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자에게는 일반 메시지를 보여주고 상세 내용은 개발 로그로 확인한다.

Q. Network Error와 500은 같아?
A. 다르다. Network Error는 서버 응답을 받지 못한 경우이고 500은 서버가 응답한 내부 오류다.

---

# 11. JSON Rules

## 11.1 JSON Request and Response 기준

### [개념]

JSON은 Frontend와 Backend가 데이터를 주고받을 때 가장 많이 사용하는 데이터 형식이다.

Frontend는 JavaScript 객체를 JSON 문자열로 변환해 보내고, Backend 응답 JSON을 JavaScript 객체로 사용한다.

---

### [핵심]

JSON 핵심:

- JavaScript Object
- JSON.stringify
- response.json
- Content-Type application/json
- Axios automatic JSON handling
- Request Body
- Response Body
- DTO Mapping
- nullable field
- date string
- enum string

fetch JSON 요청:

```javascript
body: JSON.stringify(requestBody);
```

Axios JSON 요청:

```javascript
axios.post("/reviews", requestBody);
```

---

### [실무]

fetch POST 예:

```javascript
async function createReview(requestBody) {
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

Axios POST 예:

```javascript
export async function createReview(requestBody) {
  const response = await authApi.post("/reviews", requestBody);
  return response.data;
}
```

주의:

- fetch는 직접 `JSON.stringify` 필요
- fetch는 직접 `response.json()` 필요
- Axios는 JSON 변환을 자동 처리하는 경우가 많음
- JSON 응답이 아닌 HTML 응답이면 API path 문제 가능
- 날짜는 JSON에서 보통 string으로 전달
- enum도 보통 string으로 전달
- null 가능 필드는 UI에서 방어 처리

---

### [FAQ]

Q. fetch POST에서 body는 왜 JSON.stringify를 해?
A. JavaScript 객체를 JSON 문자열로 변환해 서버에 보내야 하기 때문이다.

Q. Axios도 JSON.stringify를 직접 해야 해?
A. 일반적인 JSON 요청에서는 Axios가 자동 처리하므로 requestBody 객체를 그대로 전달하는 경우가 많다.

Q. 날짜 타입은 Date로 받아?
A. JSON 응답은 보통 문자열로 받는다. 필요하면 Frontend에서 Date 객체나 formatting 함수로 변환한다.

Q. JSON을 기대했는데 HTML이 오면 왜 그래?
A. API 요청 URL이 잘못되었거나 SPA fallback에 걸려 index.html을 받은 경우일 수 있다.

---

# 12. API Request Flow

## 12.1 API Request Flow 기본

### [개념]

API Request Flow는 사용자의 행동이나 화면 상태 변화에 따라 Frontend가 API를 호출하고 응답 결과를 UI에 반영하는 전체 흐름이다.

---

### [핵심]

기본 Flow:

```text
Trigger
→ Validate Input
→ Build Request
→ Send Request
→ Receive Response
→ Handle Success
→ Handle Error
→ Render UI
```

Trigger 예:

- Page Mount
- Button Click
- Form Submit
- Search Submit
- Pagination Change
- Route Param Change
- Login Success
- Refresh Button Click

---

### [실무]

목록 조회 Flow:

```text
FestivalListPage Mount
→ Read Search Params
→ Call getFestivals(params)
→ Set Loading
→ Receive Festival Page Response
→ Map content
→ Render FestivalList
→ Empty State if content length is 0
```

작성 요청 Flow:

```text
ReviewForm Submit
→ Validate Content
→ Build ReviewRequest
→ Call createReview(body)
→ Success
→ Reset Form
→ Invalidate or Refetch Review List
→ Show Success Message
```

상세 조회 Flow:

```text
FestivalDetailPage Mount
→ Read festivalId from Route Param
→ Validate festivalId
→ Call getFestivalDetail(festivalId)
→ Receive FestivalDetailResponse
→ Render Detail UI
```

주의:

- 요청 전 입력값 검증
- 중복 제출 방지
- 실패 시 사용자 메시지 제공
- 성공 후 필요한 데이터 갱신
- Component unmount 후 setState 주의
- 서버 응답 shape 확인
- Loading / Error / Empty State 구분

---

### [FAQ]

Q. API 호출은 언제 발생해?
A. 화면 진입, 사용자 클릭, Form 제출, 검색 조건 변경, 페이지 번호 변경 같은 Trigger에서 발생한다.

Q. API 요청 전에는 뭘 확인해야 해?
A. 필수 입력값, 인증 필요 여부, URL path, query parameter, request body, token header를 확인해야 한다.

Q. API 성공 후에는 뭘 해야 해?
A. 응답 데이터를 mapping하고 필요한 상태를 갱신한 뒤 UI를 다시 렌더링한다.

Q. API 실패 후에는 뭘 해야 해?
A. Status Code와 에러 원인을 분류하고 사용자에게 적절한 Error State를 보여준다.

---

# 13. API Layer Separation Basics

## 13.1 API Function 분리 기준

### [개념]

API Layer Separation은 Component 내부에서 직접 HTTP 요청을 작성하지 않고 API 요청 함수를 별도 파일로 분리하는 설계 방식이다.

Component는 API URL, Method, Header 세부사항을 몰라도 된다.

---

### [핵심]

API Layer 분리 대상:

- URL Path
- HTTP Method
- Query Parameter
- Path Variable
- Request Body
- Request Header
- Response Data
- Error Mapping
- Axios Instance 선택
- DTO Type

폴더 구조 예:

```text
src
├ api
│  ├ axiosInstance.js
│  ├ festivalApi.js
│  ├ reviewApi.js
│  └ notificationApi.js
├ pages
├ components
└ hooks
```

---

### [실무]

API 함수 예:

```javascript
import { publicApi, authApi } from "./axiosInstance";

export async function getFestivals(params) {
  const response = await publicApi.get("/festivals", { params });
  return response.data;
}

export async function createReview(requestBody) {
  const response = await authApi.post("/reviews", requestBody);
  return response.data;
}
```

Component 사용 예:

```javascript
useEffect(() => {
  async function loadFestivals() {
    const data = await getFestivals({ page: 0, size: 20 });
    setFestivals(data.content);
  }

  loadFestivals();
}, []);
```

권장:

- API 함수 이름은 도메인 동작 중심
- `get`, `create`, `update`, `delete`, `search` prefix 사용
- 인증 필요 여부에 따라 `publicApi` / `authApi` 선택
- Response wrapper 처리 위치를 통일
- Component가 API URL을 직접 알지 않도록 설계

---

### [FAQ]

Q. API 함수를 왜 분리해?
A. Component가 URL, Method, Header 세부사항에 의존하지 않게 하고 재사용성과 테스트 가능성을 높이기 위해서다.

Q. API 함수 이름은 어떻게 지어?
A. getFestivals, getFestivalDetail, createReview, updateReview, deleteReview처럼 동작과 리소스가 드러나게 짓는다.

Q. Component에서 axios를 직접 쓰면 안 돼?
A. 작은 실습은 가능하지만 API가 많아질수록 중복, 경로 오류, 에러 처리 불일치가 커진다.

Q. API Layer에서 response.data.data까지 풀어도 돼?
A. 가능하다. 다만 프로젝트 전체에서 wrapper 처리 기준을 일관되게 정해야 한다.

---

# 14. Public API and Auth API Basics

## 14.1 publicApi와 authApi 구분

### [개념]

`publicApi`는 인증이 필요 없는 API 요청에 사용한다.

`authApi`는 Authorization Header가 필요한 로그인 사용자 전용 API 요청에 사용한다.

---

### [핵심]

publicApi 사용 대상:

- 공개 목록 조회
- 공개 상세 조회
- 공개 검색
- 공개 필터 조회
- 로그인 전 접근 가능 API

authApi 사용 대상:

- 내 정보 조회
- 찜 등록 / 취소
- 리뷰 작성 / 수정 / 삭제
- 알림 조회 / 읽음 처리
- 결제 요청
- 사용자 전용 API

구분 기준:

```text
Authorization Header 필요 없음 → publicApi
Authorization Header 필요함 → authApi
```

---

### [실무]

Axios Instance 예:

```javascript
export const publicApi = axios.create({
  baseURL,
  timeout: 10000,
});

export const authApi = axios.create({
  baseURL,
  timeout: 10000,
});
```

authApi Interceptor 예:

```javascript
authApi.interceptors.request.use((config) => {
  const accessToken = localStorage.getItem("accessToken");

  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }

  return config;
});
```

API 함수 예:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data;
}

export async function createReview(requestBody) {
  const response = await authApi.post("/reviews", requestBody);
  return response.data;
}
```

주의:

- 인증이 필요한 API를 publicApi로 호출하면 401 가능
- 공개 API에 불필요한 Authorization Header를 보내지 않도록 기준화
- token 저장 위치와 만료 처리는 Authentication Frontend Flow에서 관리
- Frontend 인증 상태는 UX용이고 Backend 인증/인가가 최종 기준

---

### [FAQ]

Q. publicApi와 authApi 차이는?
A. publicApi는 인증이 필요 없는 요청, authApi는 Authorization Header가 필요한 요청에 사용한다.

Q. 인증 필요한 API는 어떻게 구분해?
A. Backend API 명세에서 Authorization Header가 필요한지 확인하고 authApi를 사용한다.

Q. authApi를 쓰면 자동으로 로그인되는 거야?
A. 아니다. authApi는 저장된 accessToken을 Header에 넣어 요청하는 역할이다.

Q. publicApi로 인증 API를 호출하면 어떻게 돼?
A. Authorization Header가 없어서 401 인증 실패가 발생할 수 있다.

---

# 15. Loading / Error / Empty / Success State Basics

## 15.1 API UI State 기준

### [개념]

API UI State는 API 요청 결과에 따라 화면이 보여줘야 하는 상태다.

Data Fetching에서는 Loading, Error, Empty, Success 상태를 구분해야 한다.

---

### [핵심]

상태 구분:

- Loading State: 요청 중
- Error State: 요청 실패
- Empty State: 요청 성공, 데이터 없음
- Success State: 요청 성공, 데이터 있음

기본 판단:

```text
loading true → Loading UI
error exists → Error UI
data empty → Empty UI
data exists → Success UI
```

주의:

- Empty State와 Error State를 혼동하지 않음
- Loading State 누락 금지
- submit 중 버튼 disabled 처리
- Error 객체 전체를 화면에 노출하지 않음
- 검색 결과 없음은 보통 Error가 아님

---

### [실무]

기본 예:

```jsx
function FestivalListPage() {
  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p role="alert">요청 처리 중 문제가 발생했습니다.</p>;
  }

  if (festivals.length === 0) {
    return <p>검색 결과가 없습니다.</p>;
  }

  return <FestivalList festivals={festivals} />;
}
```

Flow:

```text
API Request Start
→ loading true
→ Success
→ data check
→ Empty or Success UI
```

```text
API Request Start
→ loading true
→ Error
→ error message mapping
→ Error UI
```

권장:

- 최초 로딩과 재조회 로딩 구분 가능
- 제출 중 버튼 중복 클릭 방지
- Error State에 재시도 버튼 제공 가능
- Empty State에 검색 조건 초기화 버튼 제공 가능
- TanStack Query 사용 시 `isLoading`, `isFetching`, `error` 활용

---

### [FAQ]

Q. Loading State는 왜 필요해?
A. API 요청 중 사용자에게 진행 상태를 알려주고 중복 클릭이나 빈 화면 혼란을 줄이기 위해 필요하다.

Q. Empty State와 Error State는 뭐가 달라?
A. Empty State는 요청 성공 후 데이터가 없는 상태이고 Error State는 요청 자체가 실패한 상태다.

Q. 검색 결과가 없을 때는 에러야?
A. 아니다. 보통 정상 응답이지만 content가 비어 있는 Empty State다.

Q. API 에러 메시지는 그대로 보여줘도 돼?
A. 민감한 정보가 포함될 수 있으므로 사용자에게 보여줄 메시지와 개발자 로그를 구분하는 것이 좋다.

---

# 16. Network Debugging Basics

## 16.1 Network Tab 검증 기준

### [개념]

Network Debugging은 브라우저 개발자 도구 Network 탭에서 실제 API 요청과 응답을 확인하는 과정이다.

API 연동 문제는 코드 추측보다 실제 Request / Response 확인이 우선이다.

---

### [핵심]

Network 탭 확인 대상:

- Request URL
- Request Method
- Status Code
- Query String
- Request Payload
- Request Headers
- Authorization Header
- Response Body
- Response Headers
- Content-Type
- Timing
- CORS Error

---

### [실무]

Debug Flow:

```text
API Problem
→ Network Tab Open
→ Request URL Check
→ Request Method Check
→ Status Code Check
→ Request Headers Check
→ Request Payload Check
→ Response Body Check
→ Console Error Check
→ Backend Log Check
```

상황별 확인:

```text
데이터 안 나옴
→ Response Body shape 확인
```

```text
401 발생
→ Authorization Header 확인
```

```text
403 발생
→ 로그인 여부보다 권한 / ROLE 확인
```

```text
404 발생
→ URL / Method / Mapping 확인
```

```text
CORS 발생
→ Origin / preflight / Backend CORS 설정 확인
```

```text
HTML 응답
→ API path가 SPA fallback에 걸렸는지 확인
```

주의:

- Console만 보지 말고 Network 탭 확인
- 실제 요청 URL이 예상과 같은지 확인
- Authorization Header 포함 여부 확인
- JSON 응답인지 HTML 응답인지 확인
- API baseURL / proxy 문제 확인
- 404는 Frontend path인지 Backend path인지 구분

---

### [FAQ]

Q. API 연동이 안 될 때 제일 먼저 뭘 봐?
A. 브라우저 개발자 도구 Network 탭에서 실제 Request URL, Method, Status Code, Payload, Response Body를 확인한다.

Q. token은 localStorage에 있는데 401이 나?
A. Network 탭에서 Authorization Header에 실제로 포함되었는지 확인해야 한다.

Q. 화면에 데이터가 안 나오면 어디부터 봐?
A. Network Response Body에서 실제 응답 구조를 확인하고 Component가 접근하는 경로와 비교한다.

Q. Postman에서는 되는데 브라우저에서만 안 돼?
A. CORS, Authorization Header, credentials, browser origin 정책 문제일 가능성이 있다.

---

# 17. Common Mistakes

## 17.1 REST API Integration 실수

### [개념]

REST API Integration에서 자주 발생하는 실수는 URL, Method, Parameter, Body, Header, Response Shape를 잘못 이해해서 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Component마다 API URL 하드코딩
- publicApi / authApi 구분 없이 사용
- Authorization Header 누락
- Bearer prefix 누락
- fetch에서 response.ok 확인 누락
- Axios response.data 구조 착각
- ApiResponse wrapper 확인 누락
- response.data.data 혼동
- Query Parameter와 Request Body 혼동
- Path Variable에 undefined 전달
- GET 요청에 body 사용
- page 0-based / 1-based 혼동
- Loading State 누락
- Empty State와 Error State 혼동
- 에러 메시지 원문 그대로 노출
- CORS를 Frontend 코드 문제로만 판단
- Postman 성공을 Browser 성공으로 착각
- API 요청이 index.html을 응답하는 문제 방치
- Network 탭 확인 없이 코드만 수정

---

### [실무]

문제 해결 우선순위:

```text
1. Network Tab 확인
2. Request URL 확인
3. Method 확인
4. Header 확인
5. Payload / Query String 확인
6. Status Code 확인
7. Response Body 확인
8. Backend Mapping 확인
9. Frontend Mapping 수정
```

예:

```text
문제: API 요청했는데 index.html이 응답됨
원인: SPA fallback이 API 요청까지 가로챔
해결: API path를 fallback 대상에서 제외하고 `/api` prefix 기준을 명확히 함
```

예:

```text
문제: map is not a function
원인: 배열이라고 생각한 값이 실제로는 ApiResponse wrapper 객체
해결: response.data.data.content 구조 확인 후 mapping 수정
```

예:

```text
문제: token은 있는데 401 발생
원인: Authorization Header에 token이 포함되지 않음
해결: authApi interceptor와 Network Request Headers 확인
```

---

### [FAQ]

Q. Data Fetching 초보가 가장 많이 하는 실수는?
A. response.data 구조를 확인하지 않거나, 인증 헤더를 누락하거나, CORS / 404 / API path 문제를 혼동하는 경우가 많다.

Q. API 연동 문제는 어떻게 찾는 게 좋아?
A. Network 탭에서 실제 Request URL, Method, Header, Payload, Status Code, Response Body를 먼저 확인한다.

Q. Postman에서 되면 Frontend도 무조건 돼?
A. 아니다. Browser는 CORS와 Origin 정책을 적용하므로 Postman 성공과 Browser 성공은 다르다.

Q. API URL은 맞는 것 같은데 404가 나?
A. baseURL, `/api` prefix, Backend Controller Mapping, HTTP Method, Path Variable 값을 함께 확인해야 한다.

---

# 18. Part01 Checklist

## 18.1 REST API Basics 검수 기준

### [개념]

Part01 REST API Basics 문서는 Frontend Agent가 REST API Integration의 기본 요청 구조와 응답 처리 기준을 이해하도록 만드는 기초 문서다.

---

### [핵심]

Checklist:

```md
- [ ] REST API Integration 개념이 포함되었는가?
- [ ] HTTP Method 기준이 포함되었는가?
- [ ] URL Path 기준이 포함되었는가?
- [ ] Path Variable 기준이 포함되었는가?
- [ ] Query Parameter 기준이 포함되었는가?
- [ ] Path Variable vs Query Parameter 비교가 포함되었는가?
- [ ] Request Body 기준이 포함되었는가?
- [ ] Request Header 기준이 포함되었는가?
- [ ] Authorization Header 기본이 포함되었는가?
- [ ] Response Body / DTO Mapping 기준이 포함되었는가?
- [ ] Status Code 기준이 포함되었는가?
- [ ] JSON 요청 / 응답 기준이 포함되었는가?
- [ ] API Request Flow가 포함되었는가?
- [ ] API Layer Separation 기본이 포함되었는가?
- [ ] publicApi / authApi 구분이 포함되었는가?
- [ ] Loading / Error / Empty / Success State 기본이 포함되었는가?
- [ ] Network Debugging 기준이 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ REST Concept Check
→ Request Structure Check
→ Response Mapping Check
→ UI State Check
→ Debugging Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

최종 기준:

- Component 직접 API 하드코딩 방지
- API Function 분리 기준 제공
- Path Variable / Query Parameter / Request Body 구분 가능
- Response Shape Mismatch 분석 가능
- Network Debugging 기준 제공
- Frontend Agent가 REST API Integration 기본 코드를 생성 가능

---

### [FAQ]

Q. Part01의 목적은 뭐야?
A. REST API Integration의 기본 요청 구조, 응답 mapping, 상태 처리, 디버깅 기준을 Frontend Agent가 이해하게 만드는 것이다.

Q. Part01만 보면 API 연동을 전부 할 수 있어?
A. 기본 구조는 가능하지만 Axios Instance, TanStack Query, Pagination, Authentication Flow는 후속 Part에서 더 자세히 다룬다.

Q. Part01에서 가장 중요한 기준은 뭐야?
A. URL, Method, Parameter, Body, Header, Response DTO, Status Code, Network Debugging을 정확히 구분하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. REST API Integration이 뭐야?
A. Frontend가 HTTP Method, URL, Header, Body, Query Parameter를 사용해 Backend API와 데이터를 주고받는 작업이다.

Q. Data Fetching 문서는 왜 필요해?
A. Frontend Agent가 Backend REST API를 호출하고 응답 데이터를 화면과 상태에 연결해야 하기 때문이다.

Q. REST API는 Frontend에서 왜 알아야 해?
A. Frontend가 어떤 URL, Method, Parameter, Body, Header로 요청해야 하는지 알아야 Backend와 정상 연동할 수 있기 때문이다.

Q. API 호출은 어디서 해?
A. 간단한 경우 Component에서 할 수 있지만 실무에서는 api 함수, custom hook, TanStack Query로 분리하는 것이 좋다.

Q. HTTP Method는 어떻게 골라?
A. 조회는 GET, 생성은 POST, 전체 수정은 PUT, 부분 수정은 PATCH, 삭제는 DELETE를 사용한다.

Q. GET과 POST 차이는?
A. GET은 데이터 조회에 사용하고 POST는 새로운 데이터 생성이나 명령성 요청에 사용한다.

Q. PUT과 PATCH 차이는?
A. PUT은 전체 수정에 가깝고 PATCH는 일부 필드 수정에 가깝다.

Q. DELETE 요청은 언제 써?
A. 찜 취소, 리뷰 삭제, 알림 삭제처럼 서버 리소스를 삭제할 때 사용한다.

Q. GET 요청에도 body를 넣어도 돼?
A. 권장하지 않는다. 조회 조건은 보통 Query Parameter로 전달한다.

Q. URL Path는 뭘 기준으로 작성해?
A. Backend Controller Mapping과 API 명세를 기준으로 작성한다.

Q. API 404가 나면 뭘 확인해?
A. Request URL, Method, baseURL, API prefix, Path Variable 값, Backend Controller Mapping을 확인한다.

Q. `/festival`과 `/festivals` 차이가 중요해?
A. 중요하다. Backend Mapping과 Frontend 요청 URL이 정확히 일치해야 한다.

Q. Path Variable은 언제 써?
A. 특정 리소스를 식별할 때 사용한다. 예: 축제 상세, 리뷰 삭제, 알림 읽음 처리.

Q. Query Parameter는 언제 써?
A. 검색, 필터, 정렬, 페이지 번호처럼 리소스 조회 옵션을 전달할 때 사용한다.

Q. Path Variable과 Query Parameter 차이는?
A. Path Variable은 리소스 식별에 사용하고 Query Parameter는 검색, 필터, 정렬 같은 조회 옵션에 사용한다.

Q. URL에 undefined가 들어가는 이유는?
A. Route param이나 함수 인자가 undefined인데 검증 없이 문자열 template에 넣었을 가능성이 있다.

Q. React Router useParams 값은 숫자야?
A. 문자열일 수 있으므로 필요한 경우 Number 변환과 검증을 해야 한다.

Q. Axios에서 query parameter는 어떻게 보내?
A. `axios.get(url, { params: { keyword: "flower" } })` 형태로 보낸다.

Q. page는 0부터 시작해 1부터 시작해?
A. Backend 기준에 따라 다르다. Spring Pageable은 보통 0-based라 Frontend 표시 page와 변환이 필요할 수 있다.

Q. 빈 검색어도 query parameter로 보내야 해?
A. 프로젝트 기준에 따라 다르다. 보통 빈 값은 제거하거나 Backend 기본값을 사용한다.

Q. Request Body는 언제 써?
A. 데이터 생성, 수정, 로그인, 회원가입, 리뷰 작성처럼 서버에 JSON 데이터를 보낼 때 사용한다.

Q. Axios POST body는 어디에 넣어?
A. `axios.post(url, requestBody)`처럼 두 번째 인자에 넣는다.

Q. Request Body 필드명은 어떻게 정해?
A. Backend Request DTO가 기대하는 필드명과 타입에 맞춘다.

Q. Authorization Header는 어떤 형식이야?
A. 일반적으로 `Authorization: Bearer <accessToken>` 형식을 사용한다.

Q. Authorization Header는 매 요청마다 직접 넣어야 해?
A. 가능하지만 interceptor에서 공통 처리하는 것이 유지보수에 좋다.

Q. token은 있는데 401이 나?
A. Authorization Header에 실제로 포함되었는지, Bearer 형식이 맞는지, token이 만료되지 않았는지 확인해야 한다.

Q. Content-Type은 언제 필요해?
A. JSON body를 보낼 때 `application/json`을 사용한다. Axios는 자동 처리하는 경우가 많다.

Q. Axios 응답 데이터는 어디에 있어?
A. 보통 `response.data`에 있다.

Q. response.data.data는 왜 나와?
A. Backend가 ApiResponse 같은 공통 wrapper로 응답하면 Axios response.data 안에 다시 data 필드가 있을 수 있다.

Q. map is not a function 오류는 왜 나?
A. 배열이라고 생각한 값이 실제로는 객체이거나 undefined일 수 있다. 응답 구조와 content 위치를 확인해야 한다.

Q. Backend 응답 필드명이 바뀌면 어떻게 돼?
A. Frontend Type과 mapping 함수, Component에서 사용하는 필드명을 함께 수정해야 한다.

Q. 401과 403은 어떻게 달라?
A. 401은 인증되지 않았거나 토큰이 유효하지 않은 경우이고 403은 인증은 되었지만 권한이 없는 경우다.

Q. 404가 나면 무조건 데이터가 없는 거야?
A. 아니다. API URL 오타, Method 불일치, Controller Mapping 불일치, Resource Not Found를 구분해야 한다.

Q. 500 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자에게는 일반 메시지를 보여주고 상세 내용은 개발 로그로 확인한다.

Q. fetch POST에서 body는 왜 JSON.stringify를 해?
A. JavaScript 객체를 JSON 문자열로 변환해 서버에 보내야 하기 때문이다.

Q. Axios도 JSON.stringify를 직접 해야 해?
A. 일반적인 JSON 요청에서는 Axios가 자동 처리하므로 requestBody 객체를 그대로 전달하는 경우가 많다.

Q. 날짜 타입은 Date로 받아?
A. JSON 응답은 보통 문자열로 받는다. 필요하면 Frontend에서 Date 객체나 formatting 함수로 변환한다.

Q. JSON을 기대했는데 HTML이 응답돼?
A. API 요청이 SPA fallback에 걸려 index.html을 받은 경우일 수 있다. 요청 URL과 서버 fallback 설정을 확인한다.

Q. API 요청 전에는 뭘 확인해야 해?
A. 필수 입력값, 인증 필요 여부, URL path, query parameter, request body, token header를 확인해야 한다.

Q. API 성공 후에는 뭘 해야 해?
A. 응답 데이터를 mapping하고 필요한 상태를 갱신한 뒤 UI를 다시 렌더링한다.

Q. API 실패 후에는 뭘 해야 해?
A. Status Code와 에러 원인을 분류하고 사용자에게 적절한 Error State를 보여준다.

Q. API 함수를 왜 분리해?
A. Component가 URL, Method, Header 세부사항에 의존하지 않게 하고 재사용성과 테스트 가능성을 높이기 위해서다.

Q. API 함수 이름은 어떻게 지어?
A. getFestivals, getFestivalDetail, createReview, updateReview, deleteReview처럼 동작과 리소스가 드러나게 짓는다.

Q. publicApi와 authApi 차이는?
A. publicApi는 인증이 필요 없는 요청, authApi는 Authorization Header가 필요한 요청에 사용한다.

Q. 인증 필요한 API는 어떻게 구분해?
A. Backend API 명세에서 Authorization Header가 필요한지 확인하고 authApi를 사용한다.

Q. publicApi로 인증 API를 호출하면 어떻게 돼?
A. Authorization Header가 없어서 401 인증 실패가 발생할 수 있다.

Q. Loading State는 왜 필요해?
A. API 요청 중 사용자에게 진행 상태를 알려주고 중복 클릭이나 빈 화면 혼란을 줄이기 위해 필요하다.

Q. Empty State와 Error State는 뭐가 달라?
A. Empty State는 요청 성공 후 데이터가 없는 상태이고 Error State는 요청 자체가 실패한 상태다.

Q. 검색 결과가 없을 때는 에러야?
A. 아니다. 보통 정상 응답이지만 content가 비어 있는 Empty State다.

Q. API 에러 메시지는 그대로 보여줘도 돼?
A. 민감한 정보가 포함될 수 있으므로 사용자에게 보여줄 메시지와 개발자 로그를 구분하는 것이 좋다.

Q. API 연동이 안 될 때 제일 먼저 뭘 봐?
A. 브라우저 개발자 도구 Network 탭에서 실제 Request URL, Method, Status Code, Payload, Response Body를 확인한다.

Q. 화면에 데이터가 안 나오면 어디부터 봐?
A. Network Response Body에서 실제 응답 구조를 확인하고 Component가 접근하는 경로와 비교한다.

Q. Postman에서는 되는데 브라우저에서만 안 돼?
A. CORS, Authorization Header, credentials, browser origin 정책 문제일 가능성이 있다.

Q. Postman에서 되면 Frontend도 무조건 돼?
A. 아니다. Browser는 CORS와 Origin 정책을 적용하므로 Postman 성공과 Browser 성공은 다르다.

Q. Data Fetching 초보가 가장 많이 하는 실수는?
A. response.data 구조를 확인하지 않거나, 인증 헤더를 누락하거나, CORS / 404 / API path 문제를 혼동하는 경우가 많다.

Q. API 연동 문제는 어떻게 찾는 게 좋아?
A. Network 탭에서 실제 Request URL, Method, Header, Payload, Status Code, Response Body를 먼저 확인한다.

Q. Part01 REST API Basics의 목적은 뭐야?
A. REST API Integration의 기본 요청 구조, 응답 mapping, 상태 처리, 디버깅 기준을 Frontend Agent가 이해하게 만드는 것이다.

Q. Part01 다음에는 어떤 문서가 이어지면 좋아?
A. fetch and Axios, Axios Instance, API Layer Separation, Response Mapping, UI State, TanStack Query 순서로 이어지는 것이 좋다.
