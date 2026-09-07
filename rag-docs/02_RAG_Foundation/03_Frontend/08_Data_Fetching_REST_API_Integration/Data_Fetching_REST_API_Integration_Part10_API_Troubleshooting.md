# Data Fetching & REST API Integration Part10 - API Troubleshooting

---

# 1. API Troubleshooting Overview

## 1.1 API Troubleshooting 기본 개념

### [개념]

API Troubleshooting은 Frontend와 Backend REST API 연동 중 발생하는 문제를 Request / Response / Network / Console / Backend Log 기준으로 추적하는 과정이다.

Frontend Agent는 API 연동 오류를 추측으로 수정하지 않고, 브라우저 Network 탭의 실제 요청과 응답을 기준으로 원인을 분류해야 한다.

기본 Flow:

```text
API Problem
→ Network Tab 확인
→ Request URL 확인
→ Method 확인
→ Headers 확인
→ Payload 확인
→ Status Code 확인
→ Response Body 확인
→ Frontend Mapping 확인
→ Backend Log 확인
```

---

### [핵심]

API Troubleshooting 핵심 키워드:

- Network Tab
- Request URL
- Request Method
- Status Code
- Query String
- Request Payload
- Request Headers
- Authorization Header
- Response Body
- Response Headers
- CORS
- Preflight
- OPTIONS
- 400
- 401
- 403
- 404
- 405
- 409
- 415
- 422
- 500
- Network Error
- Timeout
- Response Shape Mismatch
- API Route
- Frontend Route
- Backend Mapping

문제 해결 기본 원칙:

- Console만 보지 않음
- Network 탭 우선 확인
- 실제 Request URL 확인
- 실제 Request Method 확인
- 실제 Header 확인
- 실제 Payload 확인
- 실제 Response Body 확인
- API 명세와 비교
- Frontend Mapping과 비교
- Backend Log와 비교

---

### [실무]

2026 실무 기준에서 API 문제는 다음 순서로 좁힌다.

```text
1. 요청이 실제로 나갔는가?
2. 요청 URL이 맞는가?
3. HTTP Method가 맞는가?
4. Query Parameter / Path Variable / Body가 맞는가?
5. Authorization Header가 포함되었는가?
6. Status Code가 무엇인가?
7. Response Body 구조가 예상과 같은가?
8. Frontend API Function return 기준이 맞는가?
9. Component에서 접근하는 경로가 맞는가?
10. Backend Controller / Security / CORS 설정과 일치하는가?
```

Network 탭 확인 항목:

```text
Request URL
Request Method
Status Code
Remote Address
Referrer Policy
Request Headers
Query String Parameters
Request Payload
Form Data
Response Headers
Response Body
Timing
```

---

### [FAQ]

Q. API 연동이 안 될 때 제일 먼저 뭘 봐?
A. 브라우저 개발자 도구 Network 탭에서 실제 Request URL, Method, Headers, Payload, Status Code, Response Body를 확인한다.

Q. Console Error만 보면 안 돼?
A. Console Error는 결과 증상만 보여주는 경우가 많다. 실제 원인은 Network Request / Response에 있는 경우가 많다.

Q. API 오류를 코드부터 고치면 안 돼?
A. 추측으로 고치면 문제가 커질 수 있다. 실제 요청과 응답을 먼저 확인해야 한다.

Q. Postman에서 성공하면 Frontend 문제야?
A. 항상 그렇지 않다. Browser는 CORS, Origin, Authorization Header, Cookie 정책이 적용되므로 Postman과 다를 수 있다.

---

# 2. Network Tab Debugging Rules

## 2.1 Network Tab 확인 기준

### [개념]

Network Tab은 브라우저에서 실제로 발생한 HTTP 요청과 응답을 확인하는 도구다.

Frontend API 연동 문제의 최종 확인 기준은 Network Tab의 실제 Request / Response다.

---

### [핵심]

Network Tab 확인 대상:

- 요청 발생 여부
- Request URL
- Request Method
- Status Code
- Query String Parameters
- Request Payload
- Form Data
- Request Headers
- Authorization Header
- Content-Type
- Accept
- Response Body
- Response Headers
- CORS Header
- Timing

확인 순서:

```text
Network Tab Open
→ Preserve Log Optional
→ API Request Click
→ Headers 확인
→ Payload 확인
→ Response 확인
→ Preview 확인
→ Timing 확인
```

주의:

- Console Error만 보고 판단하지 않음
- Request URL 전체 확인
- baseURL과 path 조합 확인
- Query Parameter 실제 값 확인
- Authorization Header 실제 포함 여부 확인
- Response Body가 JSON인지 HTML인지 확인
- Status Code와 Response Body를 함께 확인

---

### [실무]

Debug Flow:

```text
화면에 데이터 안 나옴
→ Network Tab
→ API 요청 존재 여부 확인
→ Status 200인지 확인
→ Response Body 확인
→ response.data 접근 경로 확인
```

인증 문제:

```text
401 발생
→ Request Headers
→ Authorization Header 확인
→ Bearer prefix 확인
→ token 만료 확인
```

URL 문제:

```text
404 발생
→ Request URL 확인
→ baseURL 확인
→ /api prefix 확인
→ Backend Mapping 확인
```

Payload 문제:

```text
400 발생
→ Request Payload 확인
→ Request DTO 필드명 확인
→ Backend Validation Error 확인
```

---

### [FAQ]

Q. Network 탭에서 가장 먼저 볼 것은 뭐야?
A. Request URL, Method, Status Code를 먼저 확인한다.

Q. Authorization Header는 어디서 확인해?
A. Network 탭에서 해당 요청을 클릭한 뒤 Request Headers에서 확인한다.

Q. Request Body는 어디서 확인해?
A. JSON 요청은 Payload, 파일 업로드는 Form Data에서 확인한다.

Q. Response Body는 왜 봐야 해?
A. 실제 Backend 응답 구조를 확인해야 response.data, response.data.data, content 위치를 정확히 맞출 수 있다.

---

# 3. Request URL Debugging Rules

## 3.1 Request URL 문제

### [개념]

Request URL 문제는 Frontend가 잘못된 API 주소로 요청을 보내서 발생한다.

baseURL, `/api` prefix, resource path, Path Variable, Query Parameter가 모두 Request URL에 영향을 준다.

---

### [핵심]

Request URL 확인 대상:

- baseURL
- `/api` prefix
- resource path
- path variable
- query string
- trailing slash
- singular / plural
- undefined value
- encoded value
- frontend route vs backend endpoint

자주 발생하는 URL 문제:

- `/api/api` 중복
- `/festival` vs `/festivals`
- `/undefined` 포함
- `/null` 포함
- baseURL 누락
- API 서버가 아니라 Frontend 서버로 요청
- Frontend Route와 API Endpoint 혼동
- Query Parameter 누락
- 잘못된 proxy 설정

---

### [실무]

문제 예:

```text
Expected:
GET http://localhost:8080/api/festivals/1

Actual:
GET http://localhost:3000/festivals/1
```

원인:

```text
baseURL 누락 또는 proxy 설정 오류
```

문제 예:

```text
Actual:
GET http://localhost:8080/api/api/festivals
```

원인:

```text
baseURL과 API path 양쪽에 /api prefix 포함
```

문제 예:

```text
Actual:
GET http://localhost:8080/api/festivals/undefined
```

원인:

```text
Path Variable 값 검증 누락
```

URL 검증 코드:

```typescript
function assertRequired(value: unknown, name: string) {
  if (value === undefined || value === null || value === "") {
    throw new Error(`${name} is required`);
  }
}
```

---

### [FAQ]

Q. `/api/api`가 생기는 이유는?
A. baseURL과 API path 양쪽에 `/api` prefix를 넣었기 때문이다.

Q. URL에 undefined가 들어가는 이유는?
A. Path Variable이나 route param이 준비되지 않았는데 API 함수를 호출했기 때문이다.

Q. Frontend Route와 Backend API Endpoint는 달라?
A. 다르다. Frontend Route는 화면 경로이고 Backend API Endpoint는 서버 데이터 요청 경로다.

Q. API 요청이 Frontend 서버로 가는 이유는?
A. baseURL이 없거나 proxy 설정이 잘못되어 상대 경로 요청이 Frontend dev server로 향했을 수 있다.

---

# 4. HTTP Method Debugging Rules

## 4.1 Method 불일치 문제

### [개념]

HTTP Method 불일치 문제는 Backend Controller가 기대하는 Method와 Frontend 요청 Method가 다를 때 발생한다.

예를 들어 Backend는 `POST /reviews`를 기대하는데 Frontend가 `GET /reviews`를 보내면 오류가 발생한다.

---

### [핵심]

확인 대상:

- GET
- POST
- PUT
- PATCH
- DELETE
- OPTIONS
- Backend Mapping
- Swagger Method
- Axios Function
- fetch options.method

자주 발생하는 문제:

- 조회인데 POST 사용
- 생성인데 GET 사용
- 수정인데 POST / PUT / PATCH 혼동
- 삭제인데 POST 사용
- fetch에서 method 누락으로 GET 전송
- CORS preflight OPTIONS를 실제 API 오류로 착각
- 405 Method Not Allowed 발생

---

### [실무]

fetch Method 누락 예:

```typescript
// 잘못된 예: method 누락 시 기본 GET
await fetch("/api/reviews", {
  body: JSON.stringify(requestBody),
});
```

수정:

```typescript
await fetch("/api/reviews", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(requestBody),
});
```

Axios Method 검증:

```typescript
export async function createReview(requestBody: ReviewCreateRequest) {
  const response = await authApi.post("/reviews", requestBody);
  return response.data.data;
}
```

Debug Flow:

```text
405 발생
→ Network Request Method 확인
→ Backend Controller Mapping 확인
→ Swagger API Method 확인
→ API Function 수정
```

---

### [FAQ]

Q. 405 Method Not Allowed는 왜 나?
A. URL은 맞지만 HTTP Method가 Backend Mapping과 맞지 않을 때 발생할 수 있다.

Q. fetch에서 method를 안 쓰면 뭐가 돼?
A. 기본적으로 GET 요청이 된다.

Q. OPTIONS 요청이 보이면 내가 OPTIONS를 보낸 거야?
A. 아닐 수 있다. 브라우저가 CORS preflight로 자동 전송한 요청일 수 있다.

Q. Method 문제는 어디서 확인해?
A. Network 탭의 Request Method와 Backend Controller Mapping을 비교한다.

---

# 5. Query Parameter Debugging Rules

## 5.1 Query Parameter 문제

### [개념]

Query Parameter 문제는 검색 조건, 필터, 정렬, page, size가 실제 요청 URL에 기대한 대로 포함되지 않을 때 발생한다.

---

### [핵심]

확인 대상:

- keyword
- page
- size
- sort
- filter
- targetMonth
- startDate
- endDate
- undefined
- null
- empty string
- array params
- 0-based page
- 1-based UI page

자주 발생하는 문제:

- params 옵션 누락
- undefined 값 포함
- 빈 문자열 전송
- page 변환 오류
- sort format 오류
- targetMonth 형식 오류
- 배열 parameter 직렬화 불일치
- queryKey에는 있는데 실제 params에는 없음

---

### [실무]

Axios params 확인:

```typescript
export async function searchFestivals(params: FestivalSearchParams) {
  const response = await publicApi.get("/festivals/search", {
    params: cleanParams(params),
  });

  return response.data.data;
}
```

cleanParams:

```typescript
export function cleanParams(params: Record<string, unknown>) {
  return Object.fromEntries(
    Object.entries(params).filter(([, value]) => {
      return value !== undefined && value !== null && value !== "";
    }),
  );
}
```

Page 변환:

```typescript
const backendPage = uiPage - 1;

await searchFestivals({
  keyword,
  page: backendPage,
  size: 20,
});
```

Debug Flow:

```text
검색 결과 이상
→ Network Query String Parameters 확인
→ keyword / page / size / sort 확인
→ cleanParams 처리 확인
→ Backend Params 이름 확인
```

---

### [FAQ]

Q. Query Parameter가 안 붙어?
A. Axios에서는 `{ params }` 옵션에 넣었는지 확인해야 한다.

Q. page가 이상하게 조회돼?
A. UI page 1-based와 Backend page 0-based 변환을 확인해야 한다.

Q. 빈 검색어를 보내도 돼?
A. 프로젝트 기준에 따라 다르다. 보통 빈 값은 제거하거나 Backend 기본값을 사용한다.

Q. sort 오류는 어떻게 확인해?
A. Network Query String의 sort 값이 Backend가 기대하는 `field,direction` 형식인지 확인한다.

---

# 6. Request Body Debugging Rules

## 6.1 Request Body 문제

### [개념]

Request Body 문제는 POST / PUT / PATCH 요청에서 Backend가 기대하는 JSON 구조와 Frontend가 보낸 Payload가 다를 때 발생한다.

---

### [핵심]

확인 대상:

- Request Payload
- JSON Body
- Content-Type
- Request DTO field name
- required field
- type mismatch
- null value
- empty string
- number string
- boolean
- nested object
- array
- FormData vs JSON

자주 발생하는 문제:

- 필드명 불일치
- 필수값 누락
- number가 string으로 전달
- 빈 문자열 전송
- Request Body를 params에 넣음
- Query Parameter를 body에 넣음
- GET 요청에 body 사용
- Content-Type 누락
- FormData가 필요한데 JSON 사용

---

### [실무]

Request Payload 확인:

```text
Network Tab
→ Request Click
→ Payload
→ Request Payload 확인
```

예상 Request DTO:

```typescript
export type ReviewCreateRequest = {
  festivalId: number;
  rating: number;
  content: string;
};
```

실제 요청:

```json
{
  "festivalId": 1,
  "rating": 5,
  "content": "좋았어요"
}
```

잘못된 요청:

```json
{
  "festival_id": 1,
  "rating": "5",
  "text": "좋았어요"
}
```

Debug Flow:

```text
400 / 422 발생
→ Request Payload 확인
→ Backend Request DTO 확인
→ 필드명 확인
→ 타입 확인
→ Validation Error Response 확인
```

---

### [FAQ]

Q. Request Body 오류는 어디서 확인해?
A. Network 탭의 Payload에서 실제 Request Body를 확인한다.

Q. 필드명이 조금 달라도 돼?
A. Backend DTO가 별도 alias를 허용하지 않는다면 정확히 맞아야 한다.

Q. rating이 string이면 문제야?
A. Backend가 number를 기대하면 type mismatch나 validation 오류가 발생할 수 있다.

Q. JSON 대신 FormData를 써야 하는 경우는?
A. 파일 업로드처럼 multipart/form-data가 필요한 경우에는 FormData를 사용해야 한다.

---

# 7. Header Debugging Rules

## 7.1 Request Header 문제

### [개념]

Header 문제는 Authorization, Content-Type, Accept 같은 Request Header가 누락되거나 잘못 설정되어 발생한다.

---

### [핵심]

확인 대상:

- Authorization
- Bearer Token
- Content-Type
- Accept
- multipart/form-data boundary
- Cookie
- credentials
- CORS allowed headers
- custom header

자주 발생하는 문제:

- Authorization Header 누락
- Bearer prefix 누락
- Bearer 뒤 공백 누락
- token 만료
- Content-Type 누락
- JSON 요청인데 Content-Type 없음
- multipart 요청에서 Content-Type 수동 고정
- Authorization Header가 CORS 허용 안 됨

---

### [실무]

Authorization Header 확인:

```text
Network Tab
→ Request Click
→ Headers
→ Request Headers
→ Authorization: Bearer <token>
```

authApi interceptor:

```typescript
authApi.interceptors.request.use((config) => {
  const accessToken = localStorage.getItem("accessToken");

  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }

  return config;
});
```

JSON Header:

```typescript
await fetch("/api/reviews", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(requestBody),
});
```

multipart 주의:

```typescript
// FormData 사용 시 Content-Type 직접 고정 주의
await authApi.post("/images", formData);
```

---

### [FAQ]

Q. token은 있는데 401이 나?
A. Network Request Headers에 Authorization Header가 실제 포함되었는지 확인해야 한다.

Q. Bearer 형식은 어떻게 돼?
A. `Authorization: Bearer <accessToken>` 형식이며 Bearer 뒤 공백이 필요하다.

Q. JSON 요청에서 Content-Type은 왜 필요해?
A. Backend가 Request Body를 JSON으로 해석할 수 있게 하기 위해 필요하다.

Q. multipart 요청에서 Content-Type을 직접 설정하면 안 돼?
A. FormData의 boundary가 누락될 수 있으므로 직접 고정하지 않는 방식이 안전한 경우가 많다.

---

# 8. Status Code Debugging Rules

## 8.1 Status Code 기준 Troubleshooting

### [개념]

Status Code는 API 요청 결과를 분류하는 가장 중요한 단서다.

Frontend Agent는 Status Code만 보지 않고 Response Body와 함께 확인해야 한다.

---

### [핵심]

Status Code 분류:

- 200 OK
- 201 Created
- 204 No Content
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 405 Method Not Allowed
- 409 Conflict
- 415 Unsupported Media Type
- 422 Unprocessable Entity
- 500 Internal Server Error
- Network Error

기본 해석:

```text
2xx → 요청 성공
4xx → 클라이언트 요청 / 인증 / 권한 / 리소스 문제
5xx → 서버 처리 중 오류
Network Error → 응답 자체를 받지 못함
```

---

### [실무]

Status별 우선 확인:

| Status        | 우선 확인                                   |
| ------------- | ------------------------------------------- |
| 400           | Request Body / Query Parameter / Validation |
| 401           | Authorization Header / Token                |
| 403           | Role / Permission / Resource Owner          |
| 404           | URL / Path Variable / Resource 존재 여부    |
| 405           | HTTP Method                                 |
| 409           | 중복 / 상태 충돌                            |
| 415           | Content-Type / multipart                    |
| 422           | Validation Error                            |
| 500           | Backend Log / Server Exception              |
| Network Error | CORS / Server Down / DNS / Timeout          |

Debug Flow:

```text
Status Code 확인
→ Response Body 확인
→ Request URL / Method / Payload / Header 확인
→ Frontend API Function 확인
→ Backend Log 확인
```

---

### [FAQ]

Q. Status Code만 보면 원인을 알 수 있어?
A. 대략 분류는 가능하지만 정확한 원인은 Response Body와 Request 정보를 함께 봐야 한다.

Q. 400과 422는 비슷해?
A. 둘 다 요청값 문제일 수 있다. 프로젝트에 따라 400 또는 422로 validation error를 표현할 수 있다.

Q. 500이면 Frontend 문제는 아니야?
A. 대부분 서버 내부 오류지만 Frontend가 잘못된 요청을 보내 서버 예외를 유발했을 수도 있으므로 Request Payload도 확인한다.

Q. Network Error는 Status Code가 있어?
A. 보통 서버 응답을 받지 못한 상태라 명확한 HTTP Status Code가 없을 수 있다.

---

# 9. 400 / 422 Validation Debugging Rules

## 9.1 Bad Request / Validation Error 문제

### [개념]

400 또는 422는 요청 값이 Backend Validation 기준에 맞지 않을 때 자주 발생한다.

Request Body, Query Parameter, Path Variable, Field Error Response를 확인해야 한다.

---

### [핵심]

원인:

- 필수값 누락
- 필드명 불일치
- 타입 불일치
- 길이 제한 초과
- 숫자 범위 오류
- 날짜 형식 오류
- enum 값 오류
- query parameter 형식 오류
- JSON parsing 실패

확인 대상:

- Request Payload
- Query String
- Backend Request DTO
- Validation Annotation
- Error Response Body
- field errors
- global message

---

### [실무]

Validation Error Response 예:

```json
{
  "success": false,
  "message": "입력값을 확인해 주세요.",
  "errors": {
    "rating": "평점은 1점 이상이어야 합니다.",
    "content": "내용은 필수입니다."
  }
}
```

Field Error Mapping:

```typescript
export function getFieldErrors(error: unknown): Record<string, string> {
  if (axios.isAxiosError<ApiErrorResponse>(error)) {
    return error.response?.data?.errors ?? {};
  }

  return {};
}
```

Debug Flow:

```text
400 / 422 발생
→ Request Payload 확인
→ Query String 확인
→ Response Body errors 확인
→ Backend DTO 필드명 확인
→ Form State to Request DTO 변환 확인
```

---

### [FAQ]

Q. 400이 나면 뭘 먼저 봐?
A. Request Payload와 Query Parameter가 Backend DTO와 일치하는지 확인한다.

Q. 422는 언제 나?
A. 요청 구조는 해석됐지만 validation 규칙에 맞지 않을 때 사용할 수 있다.

Q. Field Error는 어디서 확인해?
A. Network Response Body의 errors 필드나 Backend validation 응답 구조에서 확인한다.

Q. Form State를 그대로 보내면 왜 문제가 돼?
A. UI 전용 필드나 문자열 타입 값이 Backend Request DTO와 맞지 않을 수 있다.

---

# 10. 401 Unauthorized Debugging Rules

## 10.1 401 인증 실패 문제

### [개념]

401은 사용자가 인증되지 않았거나 Access Token이 유효하지 않을 때 발생한다.

Authorization Header, Bearer Token 형식, token 만료, authApi 사용 여부를 확인해야 한다.

---

### [핵심]

401 원인:

- Access Token 없음
- Authorization Header 누락
- Bearer prefix 누락
- Bearer 뒤 공백 누락
- token 만료
- token 위조
- token 저장 key 불일치
- authApi 미사용
- refresh 실패
- Backend Security 설정

확인 대상:

- localStorage token 존재 여부
- Request Headers Authorization
- authApi interceptor
- token storage key
- token expiration
- refresh token flow
- Backend Security Log

---

### [실무]

401 Debug Flow:

```text
401 발생
→ localStorage accessToken 확인
→ Network Request Headers 확인
→ Authorization Header 존재 확인
→ Bearer prefix 확인
→ token 만료 확인
→ authApi 사용 여부 확인
→ Backend Security Log 확인
```

Authorization Header 예:

```text
Authorization: Bearer eyJhbGciOi...
```

authApi 사용 확인:

```typescript
export async function createReview(requestBody: ReviewCreateRequest) {
  const response = await authApi.post("/reviews", requestBody);
  return response.data.data;
}
```

잘못된 예:

```typescript
export async function createReview(requestBody: ReviewCreateRequest) {
  const response = await publicApi.post("/reviews", requestBody);
  return response.data.data;
}
```

---

### [FAQ]

Q. 401은 무슨 뜻이야?
A. 인증되지 않았거나 token이 유효하지 않다는 의미다.

Q. token은 localStorage에 있는데 왜 401이 나?
A. 실제 Request Header에 Authorization이 포함되지 않았거나 Bearer 형식이 틀렸거나 token이 만료되었을 수 있다.

Q. 인증 API는 어떤 Instance를 써야 해?
A. Authorization Header가 필요한 API는 authApi를 사용해야 한다.

Q. 401이 나오면 무조건 로그인 페이지로 보내?
A. 프로젝트 기준에 따라 다르다. Refresh Token Flow가 있으면 재발급을 먼저 시도할 수 있다.

---

# 11. 403 Forbidden Debugging Rules

## 11.1 403 권한 문제

### [개념]

403은 인증은 되었지만 요청한 Resource나 API에 접근할 권한이 없을 때 발생한다.

Frontend에서는 401과 403을 구분해 사용자 안내와 권한 UI를 처리해야 한다.

---

### [핵심]

403 원인:

- ROLE 부족
- ROLE_USER / USER naming 불일치
- 관리자 API 접근
- Resource Owner 불일치
- 작성자만 수정 가능 정책
- Backend Method Security
- SecurityConfig 권한 설정
- 인증은 되었지만 인가 실패

확인 대상:

- 로그인 사용자 role
- Backend SecurityConfig
- API 권한 정책
- Resource owner
- token claims
- Backend authorization log
- Frontend route guard

---

### [실무]

403 Debug Flow:

```text
403 발생
→ Authorization Header 존재 확인
→ 401이 아닌 403인지 확인
→ 사용자 Role 확인
→ API 권한 정책 확인
→ Resource Owner 확인
→ Backend Security Log 확인
```

Error Message:

```typescript
if (status === 403) {
  return "접근 권한이 없습니다.";
}
```

주의:

- 403을 무조건 logout 처리하지 않음
- 다시 로그인해도 해결되지 않을 수 있음
- Frontend에서 버튼을 숨겨도 Backend 권한 검증은 필수
- 사용자 role과 Backend 권한 문자열 일치 확인
- Resource owner 정책은 Backend 기준

---

### [FAQ]

Q. 403은 무슨 뜻이야?
A. 인증은 되었지만 해당 API나 Resource에 접근할 권한이 없다는 의미다.

Q. 403이면 다시 로그인하면 해결돼?
A. 항상 그렇지 않다. 권한 자체가 부족하면 다시 로그인해도 해결되지 않는다.

Q. 401과 403 차이는?
A. 401은 인증 실패이고 403은 인증 후 권한 부족이다.

Q. 403은 Frontend에서 버튼만 숨기면 돼?
A. 아니다. Frontend 처리는 UX용이고 실제 권한 검증은 Backend가 해야 한다.

---

# 12. 404 Not Found Debugging Rules

## 12.1 404 문제

### [개념]

404는 요청한 API Endpoint 또는 Resource를 찾을 수 없을 때 발생한다.

Frontend에서는 API 404와 Frontend Route 404를 구분해야 한다.

---

### [핵심]

404 원인:

- URL 오타
- baseURL 오류
- `/api` prefix 누락
- `/api/api` 중복
- resource path 불일치
- singular / plural 불일치
- Path Variable undefined
- Backend Controller Mapping 없음
- Resource 실제 없음
- Frontend SPA fallback
- API 요청이 index.html 응답

확인 대상:

- Request URL
- Request Method
- Backend Mapping
- Path Variable
- Response Body
- Content-Type
- HTML 응답 여부
- Frontend Router

---

### [실무]

404 Debug Flow:

```text
404 발생
→ Request URL 확인
→ Method 확인
→ baseURL 확인
→ /api prefix 확인
→ Path Variable 확인
→ Backend Controller Mapping 확인
→ Resource 존재 여부 확인
```

API 404 예:

```text
GET /api/festivals/99999
→ Resource Not Found
```

Route / Path 문제 예:

```text
GET /festivals/1
→ Frontend 서버로 요청
→ API 서버가 아님
```

HTML 응답 문제:

```text
Expected JSON
Actual text/html index.html
```

원인:

```text
API 요청이 SPA fallback에 걸렸거나 API path가 잘못됨
```

---

### [FAQ]

Q. 404가 나면 무조건 데이터가 없는 거야?
A. 아니다. API URL 오타, Method 불일치, Controller Mapping 불일치, Resource Not Found를 구분해야 한다.

Q. API 404와 화면 Route 404는 달라?
A. 다르다. API 404는 서버 데이터 요청 실패이고 Route 404는 Frontend 화면 경로 문제다.

Q. JSON을 기대했는데 HTML이 응답돼?
A. API 요청이 SPA fallback에 걸려 index.html을 받은 경우일 수 있다.

Q. `/festival`과 `/festivals` 차이가 중요해?
A. 중요하다. Backend Mapping과 정확히 일치해야 한다.

---

# 13. CORS Debugging Rules

## 13.1 CORS 문제

### [개념]

CORS는 브라우저가 다른 Origin으로 요청할 때 적용하는 보안 정책이다.

Postman은 CORS 정책을 적용하지 않기 때문에 Postman 성공과 Browser 성공은 다를 수 있다.

---

### [핵심]

CORS 핵심 키워드:

- Origin
- Same-Origin Policy
- Cross-Origin Request
- Access-Control-Allow-Origin
- Access-Control-Allow-Methods
- Access-Control-Allow-Headers
- Access-Control-Allow-Credentials
- Preflight
- OPTIONS
- Authorization Header
- credentials
- Cookie

CORS 원인:

- Backend CORS 설정 누락
- Origin 허용 누락
- Method 허용 누락
- Authorization Header 허용 누락
- credentials와 wildcard 충돌
- Preflight OPTIONS 실패
- Proxy 설정 오류

---

### [실무]

CORS Debug Flow:

```text
Browser CORS Error
→ Console Message 확인
→ Network OPTIONS 요청 확인
→ Request Origin 확인
→ Response CORS Headers 확인
→ Backend CORS 설정 확인
→ Authorization Header 허용 확인
```

확인 Header:

```text
Access-Control-Allow-Origin
Access-Control-Allow-Methods
Access-Control-Allow-Headers
Access-Control-Allow-Credentials
```

자주 발생:

```text
Authorization Header 사용
→ Preflight OPTIONS 발생
→ Backend가 Authorization header 허용하지 않음
→ CORS Error
```

주의:

- Frontend 코드만으로 CORS를 근본 해결할 수 없음
- Backend CORS 설정이 필요
- 개발 proxy로 우회 가능하지만 운영 CORS 설정은 별도 필요
- `credentials: true`와 wildcard origin은 같이 사용할 수 없음
- CORS Error는 실제 Backend Controller까지 도달하지 않을 수 있음

---

### [FAQ]

Q. CORS는 Frontend 오류야 Backend 오류야?
A. 브라우저 정책이지만 해결은 주로 Backend CORS 설정에서 한다.

Q. Postman에서는 되는데 브라우저에서 안 돼?
A. Postman은 CORS를 적용하지 않기 때문에 브라우저와 다를 수 있다.

Q. Authorization Header를 쓰면 CORS가 더 잘 나?
A. Authorization Header는 preflight를 유발할 수 있으므로 Backend에서 허용해야 한다.

Q. CORS Error는 response.status로 확인할 수 있어?
A. 대부분 정상 response를 받지 못하므로 Console과 Network의 OPTIONS 요청을 확인해야 한다.

---

# 14. Response Shape Debugging Rules

## 14.1 Response Shape 문제

### [개념]

Response Shape 문제는 Backend 응답 구조와 Frontend가 기대한 구조가 달라 발생한다.

화면에 데이터가 안 보이거나 `.map is not a function`, `Cannot read properties of undefined` 같은 오류가 발생할 수 있다.

---

### [핵심]

원인:

- ApiResponse Wrapper 확인 누락
- response.data / response.data.data 혼동
- Page Response content 위치 착각
- Slice Response content 위치 착각
- 배열이 아니라 객체 응답
- 객체가 아니라 배열 응답
- nullable field 미처리
- Interceptor unwrap 기준 혼용
- Mock Data와 실제 API 응답 차이
- Backend DTO 변경

확인 대상:

- Network Response Body
- API Function return
- Interceptor response unwrap
- TypeScript Type
- Component field access
- Initial State

---

### [실무]

Debug Flow:

```text
화면 데이터 오류
→ Network Response Body 확인
→ response.data 구조 확인
→ ApiResponse wrapper 확인
→ content 위치 확인
→ API Function return 확인
→ Component 접근 경로 확인
```

문제 예:

```text
Error: map is not a function
원인: PageResponse 객체를 배열처럼 사용
해결: pageData.content.map 사용
```

문제 예:

```text
Error: Cannot read properties of undefined
원인: data가 아직 undefined인데 필드 접근
해결: Loading State와 optional rendering 처리
```

문제 예:

```text
response.data.data undefined
원인: Response Interceptor에서 이미 response.data를 반환
해결: API Function 반환 기준 확인
```

---

### [FAQ]

Q. map is not a function은 왜 나?
A. 배열이라고 생각한 값이 실제로는 객체이거나 undefined일 때 발생한다.

Q. response.data.data가 undefined면 뭘 봐?
A. ApiResponse Wrapper 여부와 Response Interceptor unwrap 기준을 확인한다.

Q. TypeScript 타입은 맞는데 런타임 오류가 나?
A. 실제 API 응답이 TypeScript 선언과 다를 수 있으므로 Network Response Body를 확인해야 한다.

Q. Response Shape 문제는 어떻게 해결해?
A. 실제 Response Body를 기준으로 API Function return과 Component 접근 경로를 맞춘다.

---

# 15. 500 Server Error Debugging Rules

## 15.1 500 서버 오류 문제

### [개념]

500은 Backend 서버 내부에서 예외가 발생했음을 의미한다.

Frontend는 500을 사용자에게 일반 오류 메시지로 보여주고, 개발자는 Request Payload와 Backend Log를 함께 확인해야 한다.

---

### [핵심]

500 원인:

- Backend NullPointerException
- DB 오류
- DTO mapping 오류
- Validation 처리 누락
- 외부 API 실패
- 권한 처리 예외
- 파일 저장 실패
- 서버 설정 오류
- 잘못된 Request가 서버 예외 유발

Frontend 확인 대상:

- Request URL
- Request Method
- Request Payload
- Request Header
- Response Body
- 재현 조건
- Backend Log 전달 정보

주의:

- 서버 stack trace를 사용자에게 노출하지 않음
- 500이어도 Frontend Request가 원인일 수 있음
- 같은 요청이 Postman에서도 재현되는지 확인 가능
- Backend 개발자에게 Request 정보 전달
- 사용자에게는 일반 오류 메시지 제공

---

### [실무]

500 Debug Flow:

```text
500 발생
→ Request URL 확인
→ Method 확인
→ Payload 확인
→ Header 확인
→ Response Body 확인
→ 같은 요청 재현
→ Backend Log 확인
```

사용자 메시지:

```typescript
if (status && status >= 500) {
  return "서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.";
}
```

개발자 전달 정보:

```text
- Request URL
- Method
- Status Code
- Request Payload
- Query Parameters
- User Role
- 발생 시각
- Response Body
```

주의:

- Access Token 원문 공유 금지
- 개인정보 포함 Payload 공유 주의
- 에러 메시지를 그대로 Alert에 표시하지 않음
- 반복 발생 시 Backend Log 확인 필수

---

### [FAQ]

Q. 500이면 Frontend에서 할 수 있는 게 없어?
A. 서버 오류지만 Request Payload나 Header가 원인을 유발했을 수 있으므로 요청 정보를 확인해야 한다.

Q. 500 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자에게는 일반 메시지를 보여주고 상세 내용은 개발 로그로 확인한다.

Q. 500을 Backend 팀에 전달할 때 뭘 보내?
A. Request URL, Method, Payload, Status Code, Response Body, 발생 시각을 정리해 전달한다.

Q. 500인데 Postman에서는 성공해?
A. Browser 요청의 Header, Payload, CORS, 인증 정보가 Postman과 다른지 확인해야 한다.

---

# 16. Timeout and Network Error Debugging Rules

## 16.1 Timeout / Network Error 문제

### [개념]

Timeout과 Network Error는 서버 응답을 정상적으로 받지 못했을 때 발생한다.

서버가 응답한 500과 다르게 HTTP Status Code가 없거나 AxiosError의 response가 없을 수 있다.

---

### [핵심]

원인:

- 서버 다운
- 네트워크 연결 문제
- API 서버 주소 오류
- DNS 문제
- proxy 문제
- timeout 초과
- CORS 차단
- mixed content
- VPN / 방화벽
- HTTPS 인증서 문제

확인 대상:

- error.response 존재 여부
- error.request 존재 여부
- error.code
- ECONNABORTED
- Request URL
- 서버 실행 여부
- Dev Server proxy
- Network Console
- CORS message

---

### [실무]

Axios Error Mapping:

```typescript
export function getApiErrorMessage(error: unknown): string {
  if (axios.isAxiosError(error)) {
    if (error.code === "ECONNABORTED") {
      return "요청 시간이 초과되었습니다.";
    }

    if (!error.response) {
      return "네트워크 연결을 확인해 주세요.";
    }
  }

  return "요청 처리 중 문제가 발생했습니다.";
}
```

Debug Flow:

```text
Network Error 발생
→ API Server 실행 여부 확인
→ Request URL 확인
→ Browser Console 확인
→ CORS 여부 확인
→ proxy 설정 확인
→ timeout 여부 확인
```

Timeout 설정:

```typescript
export const publicApi = axios.create({
  baseURL,
  timeout: 10000,
});
```

주의:

- Network Error는 서버 응답이 없을 수 있음
- CORS도 Network Error처럼 보일 수 있음
- timeout과 500은 다름
- 로딩 상태를 반드시 종료
- Retry Button 제공 가능

---

### [FAQ]

Q. Network Error는 무슨 뜻이야?
A. 서버 응답을 정상적으로 받지 못했다는 의미다. 서버 다운, CORS, URL 오류, 네트워크 문제 등이 원인일 수 있다.

Q. Timeout과 500은 달라?
A. 다르다. Timeout은 응답을 제시간에 받지 못한 것이고 500은 서버가 내부 오류 응답을 보낸 것이다.

Q. Axios error.response가 없으면 뭐야?
A. 서버 응답을 받지 못한 네트워크 오류, CORS, timeout 문제일 수 있다.

Q. Timeout이 나면 어떻게 보여줘?
A. 요청 시간이 초과되었다는 메시지와 재시도 버튼을 제공할 수 있다.

---

# 17. Debugging Report Rules

## 17.1 API 문제 보고 기준

### [개념]

Debugging Report는 API 연동 문제를 다른 개발자나 Backend Agent에게 전달하기 위한 최소 정보 묶음이다.

문제를 정확히 전달하면 원인 분석과 수정 속도가 빨라진다.

---

### [핵심]

보고에 포함할 내용:

- 발생 화면
- 재현 단계
- Request URL
- Request Method
- Status Code
- Query Parameters
- Request Payload
- Request Headers 요약
- Response Body
- Expected Result
- Actual Result
- 발생 시각
- 관련 API Function
- 관련 Backend Endpoint

주의:

- Access Token 원문 공유 금지
- 개인정보 마스킹
- 비밀번호 / 결제 정보 공유 금지
- 스크린샷보다 텍스트 정보 우선
- Network 정보 기준으로 작성
- Markdown 중첩 코드블록이 깨지지 않도록 JSON 예시는 들여쓰기 또는 별도 블록으로 분리

---

### [실무]

Report Template:

```text
API Issue Report

발생 화면:
- Festival Detail Page

재현 단계:
1. 축제 상세 페이지 접속
2. 리뷰 작성 버튼 클릭
3. 내용 입력 후 제출

Request:
- Method: POST
- URL: /api/reviews
- Query Params: 없음
- Payload: {"festivalId":1,"rating":5,"content":"좋았어요"}

Response:
- Status: 401
- Body: {"message":"Unauthorized"}

Expected:
- 리뷰 작성 성공

Actual:
- 401 발생

확인 내용:
- Authorization Header 없음
- createReview API가 publicApi 사용 중

수정 방향:
- createReview에서 publicApi 대신 authApi 사용
```

문제 보고 시 Payload 예시는 중첩 코드블록 대신 단일 라인 JSON 또는 별도 JSON 블록으로 분리한다.

Payload Example:

```json
{
  "festivalId": 1,
  "rating": 5,
  "content": "좋았어요"
}
```

Response Example:

```json
{
  "message": "Unauthorized"
}
```

수정 방향 예:

```text
createReview에서 publicApi 대신 authApi 사용
```

---

### [FAQ]

Q. API 문제를 보고할 때 뭘 포함해야 해?
A. Request URL, Method, Status Code, Payload, Response Body, 재현 단계를 포함해야 한다.

Q. Access Token도 같이 보내야 해?
A. 안 된다. token 원문은 민감정보이므로 공유하지 않는다.

Q. 스크린샷만 보내도 돼?
A. 부족할 수 있다. Network 탭의 요청 / 응답 정보를 텍스트로 정리하는 것이 좋다.

Q. Backend에게 500을 보고할 때 뭘 줘야 해?
A. Request URL, Method, Payload, Status Code, Response Body, 발생 시각을 전달한다.

---

# 18. Common Mistakes

## 18.1 API Troubleshooting 공통 실수

### [개념]

API Troubleshooting 실수는 Network Request / Response를 확인하지 않고 Console Error나 추측만으로 문제를 수정할 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Network 탭 확인 없이 코드 수정
- Console Error만 보고 판단
- Postman 성공을 Browser 성공으로 착각
- Request URL 전체를 확인하지 않음
- HTTP Method 확인 누락
- Query Parameter 확인 누락
- Request Payload 확인 누락
- Authorization Header 확인 누락
- Bearer prefix 확인 누락
- Status Code와 Response Body를 따로 봄
- 401과 403 혼동
- 404를 무조건 데이터 없음으로 판단
- CORS를 Frontend 코드로만 해결하려 함
- 500을 무조건 Backend 문제로만 판단
- response.data.data 구조 확인 누락
- HTML 응답을 JSON처럼 처리
- FormData key 미확인
- multipart Content-Type boundary 문제 미확인
- token / 개인정보를 로그나 보고서에 노출
- Markdown Report에서 중첩 코드블록을 사용해 문서 파싱 오류 발생

---

### [실무]

문제 예:

```text
문제: 화면에 데이터가 안 나옴
원인: Response Body는 ApiResponse<PageResponse<T>>인데 Component가 배열로 처리
해결: response.data.data.content 기준으로 수정
```

문제 예:

```text
문제: Postman은 성공하지만 Browser 실패
원인: CORS Authorization Header 허용 누락
해결: Backend CORS allowed headers 설정 확인
```

문제 예:

```text
문제: 로그인했는데 401
원인: localStorage token은 있지만 authApi가 아닌 publicApi 사용
해결: API Function에서 authApi 사용
```

문제 예:

```text
문제: 파일 업로드에서 Backend file null
원인: FormData key와 Backend @RequestPart name 불일치
해결: multipart field name 일치
```

해결 우선순위:

```text
Network Request 확인
→ Status Code 확인
→ Response Body 확인
→ API Function 확인
→ DTO Mapping 확인
→ Backend Mapping / Log 확인
```

---

### [FAQ]

Q. API Troubleshooting에서 가장 흔한 실수는?
A. Network 탭의 실제 요청과 응답을 확인하지 않고 추측으로 수정하는 것이다.

Q. Console에 에러가 없는데 화면이 이상해?
A. Response Shape Mismatch나 State Mapping 문제일 수 있으므로 Network Response Body와 Component 접근 경로를 확인한다.

Q. Postman에서는 되는데 Frontend에서 안 되면 뭘 봐?
A. CORS, Authorization Header, baseURL, credentials, Browser Origin 정책을 확인해야 한다.

Q. API 문제 해결 순서는 뭐야?
A. Request URL, Method, Headers, Payload, Status Code, Response Body, Frontend Mapping, Backend Log 순서로 확인한다.

---

# 19. Part10 Checklist

## 19.1 API Troubleshooting 검수 기준

### [개념]

Part10 API Troubleshooting 문서는 Frontend Agent가 REST API 연동 문제를 Network Request / Response 기준으로 분류하고 원인을 빠르게 찾도록 만드는 문서다.

---

### [핵심]

Checklist:

```md
- [ ] API Troubleshooting 기본 개념이 포함되었는가?
- [ ] Network Tab Debugging 기준이 포함되었는가?
- [ ] Request URL Debugging 기준이 포함되었는가?
- [ ] HTTP Method Debugging 기준이 포함되었는가?
- [ ] Query Parameter Debugging 기준이 포함되었는가?
- [ ] Request Body Debugging 기준이 포함되었는가?
- [ ] Header Debugging 기준이 포함되었는가?
- [ ] Status Code Debugging 기준이 포함되었는가?
- [ ] 400 / 422 Validation Debugging 기준이 포함되었는가?
- [ ] 401 Unauthorized Debugging 기준이 포함되었는가?
- [ ] 403 Forbidden Debugging 기준이 포함되었는가?
- [ ] 404 Not Found Debugging 기준이 포함되었는가?
- [ ] CORS Debugging 기준이 포함되었는가?
- [ ] Response Shape Debugging 기준이 포함되었는가?
- [ ] 500 Server Error Debugging 기준이 포함되었는가?
- [ ] Timeout / Network Error Debugging 기준이 포함되었는가?
- [ ] Debugging Report 기준이 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Network Debugging Check
→ URL / Method Check
→ Params / Body / Header Check
→ Status Code Check
→ 400 / 401 / 403 / 404 Check
→ CORS Check
→ Response Shape Check
→ 500 / Network Error Check
→ Report Template Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

최종 기준:

- Network 탭 기준으로 API 문제 분석 가능
- URL / Method / Params / Body / Header 문제 구분 가능
- 400 / 401 / 403 / 404 / 415 / 500 원인 분류 가능
- CORS와 Network Error 구분 가능
- Response Shape Mismatch 분석 가능
- API 문제 보고서 작성 가능
- Markdown 중첩 코드블록 파싱 오류 없음
- Frontend Agent가 API 연동 오류를 추측 없이 진단 가능

---

### [FAQ]

Q. Part10의 목적은 뭐야?
A. Frontend Agent가 REST API 연동 문제를 Network Request / Response 기준으로 진단하고 원인을 분류하게 만드는 것이다.

Q. Part10에서 가장 중요한 기준은 뭐야?
A. Network 탭에서 Request URL, Method, Headers, Payload, Status Code, Response Body를 먼저 확인하는 것이다.

Q. Part10에서 수정된 핵심은 뭐야?
A. Debugging Report Template 구간의 중첩 코드블록 깨짐 가능성을 제거하고 JSON 예시를 별도 블록으로 분리한 것이다.

---

# Retrieval Queries

### [FAQ]

Q. API 연동이 안 될 때 제일 먼저 뭘 봐?
A. 브라우저 개발자 도구 Network 탭에서 실제 Request URL, Method, Headers, Payload, Status Code, Response Body를 확인한다.

Q. Console Error만 보면 안 돼?
A. Console Error는 결과 증상만 보여주는 경우가 많다. 실제 원인은 Network Request / Response에 있는 경우가 많다.

Q. API 오류를 코드부터 고치면 안 돼?
A. 추측으로 고치면 문제가 커질 수 있다. 실제 요청과 응답을 먼저 확인해야 한다.

Q. Postman에서 성공하면 Frontend 문제야?
A. 항상 그렇지 않다. Browser는 CORS, Origin, Authorization Header, Cookie 정책이 적용되므로 Postman과 다를 수 있다.

Q. Network 탭에서 가장 먼저 볼 것은 뭐야?
A. Request URL, Method, Status Code를 먼저 확인한다.

Q. Authorization Header는 어디서 확인해?
A. Network 탭에서 해당 요청을 클릭한 뒤 Request Headers에서 확인한다.

Q. Request Body는 어디서 확인해?
A. JSON 요청은 Payload, 파일 업로드는 Form Data에서 확인한다.

Q. Response Body는 왜 봐야 해?
A. 실제 Backend 응답 구조를 확인해야 response.data, response.data.data, content 위치를 정확히 맞출 수 있다.

Q. `/api/api`가 생기는 이유는?
A. baseURL과 API path 양쪽에 `/api` prefix를 넣었기 때문이다.

Q. URL에 undefined가 들어가는 이유는?
A. Path Variable이나 route param이 준비되지 않았는데 API 함수를 호출했기 때문이다.

Q. Frontend Route와 Backend API Endpoint는 달라?
A. Frontend Route는 화면 경로이고 Backend API Endpoint는 서버 데이터 요청 경로다.

Q. API 요청이 Frontend 서버로 가는 이유는?
A. baseURL이 없거나 proxy 설정이 잘못되어 상대 경로 요청이 Frontend dev server로 향했을 수 있다.

Q. 405 Method Not Allowed는 왜 나?
A. URL은 맞지만 HTTP Method가 Backend Mapping과 맞지 않을 때 발생할 수 있다.

Q. fetch에서 method를 안 쓰면 뭐가 돼?
A. 기본적으로 GET 요청이 된다.

Q. OPTIONS 요청이 보이면 내가 OPTIONS를 보낸 거야?
A. 아닐 수 있다. 브라우저가 CORS preflight로 자동 전송한 요청일 수 있다.

Q. Method 문제는 어디서 확인해?
A. Network 탭의 Request Method와 Backend Controller Mapping을 비교한다.

Q. Query Parameter가 안 붙어?
A. Axios에서는 `{ params }` 옵션에 넣었는지 확인해야 한다.

Q. page가 이상하게 조회돼?
A. UI page 1-based와 Backend page 0-based 변환을 확인해야 한다.

Q. 빈 검색어를 보내도 돼?
A. 프로젝트 기준에 따라 다르다. 보통 빈 값은 제거하거나 Backend 기본값을 사용한다.

Q. sort 오류는 어떻게 확인해?
A. Network Query String의 sort 값이 Backend가 기대하는 `field,direction` 형식인지 확인한다.

Q. Request Body 오류는 어디서 확인해?
A. Network 탭의 Payload에서 실제 Request Body를 확인한다.

Q. 필드명이 조금 달라도 돼?
A. Backend DTO가 별도 alias를 허용하지 않는다면 정확히 맞아야 한다.

Q. rating이 string이면 문제야?
A. Backend가 number를 기대하면 type mismatch나 validation 오류가 발생할 수 있다.

Q. JSON 대신 FormData를 써야 하는 경우는?
A. 파일 업로드처럼 multipart/form-data가 필요한 경우에는 FormData를 사용해야 한다.

Q. token은 있는데 401이 나?
A. Network Request Headers에 Authorization Header가 실제 포함되었는지 확인해야 한다.

Q. Bearer 형식은 어떻게 돼?
A. `Authorization: Bearer <accessToken>` 형식이며 Bearer 뒤 공백이 필요하다.

Q. JSON 요청에서 Content-Type은 왜 필요해?
A. Backend가 Request Body를 JSON으로 해석할 수 있게 하기 위해 필요하다.

Q. multipart 요청에서 Content-Type을 직접 설정하면 안 돼?
A. FormData의 boundary가 누락될 수 있으므로 직접 고정하지 않는 방식이 안전한 경우가 많다.

Q. Status Code만 보면 원인을 알 수 있어?
A. 대략 분류는 가능하지만 정확한 원인은 Response Body와 Request 정보를 함께 봐야 한다.

Q. 400과 422는 비슷해?
A. 둘 다 요청값 문제일 수 있다. 프로젝트에 따라 400 또는 422로 validation error를 표현할 수 있다.

Q. 500이면 Frontend 문제는 아니야?
A. 대부분 서버 내부 오류지만 Frontend가 잘못된 요청을 보내 서버 예외를 유발했을 수도 있으므로 Request Payload도 확인한다.

Q. Network Error는 Status Code가 있어?
A. 보통 서버 응답을 받지 못한 상태라 명확한 HTTP Status Code가 없을 수 있다.

Q. 400이 나면 뭘 먼저 봐?
A. Request Payload와 Query Parameter가 Backend DTO와 일치하는지 확인한다.

Q. 422는 언제 나?
A. 요청 구조는 해석됐지만 validation 규칙에 맞지 않을 때 사용할 수 있다.

Q. Field Error는 어디서 확인해?
A. Network Response Body의 errors 필드나 Backend validation 응답 구조에서 확인한다.

Q. Form State를 그대로 보내면 왜 문제가 돼?
A. UI 전용 필드나 문자열 타입 값이 Backend Request DTO와 맞지 않을 수 있다.

Q. 401은 무슨 뜻이야?
A. 인증되지 않았거나 token이 유효하지 않다는 의미다.

Q. 인증 API는 어떤 Instance를 써야 해?
A. Authorization Header가 필요한 API는 authApi를 사용해야 한다.

Q. 401이 나오면 무조건 로그인 페이지로 보내?
A. 프로젝트 기준에 따라 다르다. Refresh Token Flow가 있으면 재발급을 먼저 시도할 수 있다.

Q. 403은 무슨 뜻이야?
A. 인증은 되었지만 해당 API나 Resource에 접근할 권한이 없다는 의미다.

Q. 403이면 다시 로그인하면 해결돼?
A. 항상 그렇지 않다. 권한 자체가 부족하면 다시 로그인해도 해결되지 않는다.

Q. 401과 403 차이는?
A. 401은 인증 실패이고 403은 인증 후 권한 부족이다.

Q. 403은 Frontend에서 버튼만 숨기면 돼?
A. 아니다. Frontend 처리는 UX용이고 실제 권한 검증은 Backend가 해야 한다.

Q. 404가 나면 무조건 데이터가 없는 거야?
A. 아니다. API URL 오타, Method 불일치, Controller Mapping 불일치, Resource Not Found를 구분해야 한다.

Q. API 404와 화면 Route 404는 달라?
A. 다르다. API 404는 서버 데이터 요청 실패이고 Route 404는 Frontend 화면 경로 문제다.

Q. JSON을 기대했는데 HTML이 응답돼?
A. API 요청이 SPA fallback에 걸려 index.html을 받은 경우일 수 있다.

Q. `/festival`과 `/festivals` 차이가 중요해?
A. 중요하다. Backend Mapping과 정확히 일치해야 한다.

Q. CORS는 Frontend 오류야 Backend 오류야?
A. 브라우저 정책이지만 해결은 주로 Backend CORS 설정에서 한다.

Q. Postman에서는 되는데 브라우저에서 안 돼?
A. Postman은 CORS를 적용하지 않기 때문에 브라우저와 다를 수 있다.

Q. Authorization Header를 쓰면 CORS가 더 잘 나?
A. Authorization Header는 preflight를 유발할 수 있으므로 Backend에서 허용해야 한다.

Q. CORS Error는 response.status로 확인할 수 있어?
A. 대부분 정상 response를 받지 못하므로 Console과 Network의 OPTIONS 요청을 확인해야 한다.

Q. map is not a function은 왜 나?
A. 배열이라고 생각한 값이 실제로는 객체이거나 undefined일 때 발생한다.

Q. response.data.data가 undefined면 뭘 봐?
A. ApiResponse Wrapper 여부와 Response Interceptor unwrap 기준을 확인한다.

Q. TypeScript 타입은 맞는데 런타임 오류가 나?
A. 실제 API 응답이 TypeScript 선언과 다를 수 있으므로 Network Response Body를 확인해야 한다.

Q. Response Shape 문제는 어떻게 해결해?
A. 실제 Response Body를 기준으로 API Function return과 Component 접근 경로를 맞춘다.

Q. 500이면 Frontend에서 할 수 있는 게 없어?
A. 서버 오류지만 Request Payload나 Header가 원인을 유발했을 수 있으므로 요청 정보를 확인해야 한다.

Q. 500 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자에게는 일반 메시지를 보여주고 상세 내용은 개발 로그로 확인한다.

Q. 500을 Backend 팀에 전달할 때 뭘 보내?
A. Request URL, Method, Payload, Status Code, Response Body, 발생 시각을 정리해 전달한다.

Q. 500인데 Postman에서는 성공해?
A. Browser 요청의 Header, Payload, CORS, 인증 정보가 Postman과 다른지 확인해야 한다.

Q. Network Error는 무슨 뜻이야?
A. 서버 응답을 정상적으로 받지 못했다는 의미다. 서버 다운, CORS, URL 오류, 네트워크 문제 등이 원인일 수 있다.

Q. Timeout과 500은 달라?
A. 다르다. Timeout은 응답을 제시간에 받지 못한 것이고 500은 서버가 내부 오류 응답을 보낸 것이다.

Q. Axios error.response가 없으면 뭐야?
A. 서버 응답을 받지 못한 네트워크 오류, CORS, timeout 문제일 수 있다.

Q. Timeout이 나면 어떻게 보여줘?
A. 요청 시간이 초과되었다는 메시지와 재시도 버튼을 제공할 수 있다.

Q. API 문제를 보고할 때 뭘 포함해야 해?
A. Request URL, Method, Status Code, Payload, Response Body, 재현 단계를 포함해야 한다.

Q. Access Token도 같이 보내야 해?
A. 안 된다. token 원문은 민감정보이므로 공유하지 않는다.

Q. 스크린샷만 보내도 돼?
A. 부족할 수 있다. Network 탭의 요청 / 응답 정보를 텍스트로 정리하는 것이 좋다.

Q. Backend에게 500을 보고할 때 뭘 줘야 해?
A. Request URL, Method, Payload, Status Code, Response Body, 발생 시각을 전달한다.

Q. API Troubleshooting에서 가장 흔한 실수는?
A. Network 탭의 실제 요청과 응답을 확인하지 않고 추측으로 수정하는 것이다.

Q. Console에 에러가 없는데 화면이 이상해?
A. Response Shape Mismatch나 State Mapping 문제일 수 있으므로 Network Response Body와 Component 접근 경로를 확인한다.

Q. Postman에서는 되는데 Frontend에서 안 되면 뭘 봐?
A. CORS, Authorization Header, baseURL, credentials, Browser Origin 정책을 확인해야 한다.

Q. API 문제 해결 순서는 뭐야?
A. Request URL, Method, Headers, Payload, Status Code, Response Body, Frontend Mapping, Backend Log 순서로 확인한다.

Q. Part10 API Troubleshooting의 목적은 뭐야?
A. Frontend Agent가 REST API 연동 문제를 Network Request / Response 기준으로 진단하고 원인을 분류하게 만드는 것이다.

Q. Part10에서 수정된 핵심은 뭐야?
A. Debugging Report Template 구간의 중첩 코드블록 깨짐 가능성을 제거하고 JSON 예시를 별도 블록으로 분리한 것이다.
