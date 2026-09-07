# JavaScript Foundation Part08 - Fetch API, JSON, and API Response Processing

---

# 1. Fetch API

## 1.1 Fetch API Concept

### [개념]

Fetch API는 Browser JavaScript에서 HTTP 요청을 보내고 서버 응답을 받을 수 있게 해주는 기본 Web API다.

Frontend JavaScript에서는 Backend API와 통신하기 위해 Fetch API를 사용한다.

예:

```javascript
const response = await fetch("/api/festivals");
const data = await response.json();
```

---

### [핵심]

- Fetch API
- fetch
- HTTP Request
- HTTP Response
- GET
- POST
- PUT
- PATCH
- DELETE
- Headers
- JSON Body
- response.ok
- response.status
- response.json
- Error Handling
- API Integration
- Browser JavaScript

---

### [실무]

2026 실무 기준에서 Frontend Agent는 Fetch API를 단순 요청 함수가 아니라 API 연동 흐름 전체로 이해해야 한다.

Fetch API 기본 Flow:

```text
User Action
→ API Function Call
→ fetch Request
→ response.ok Check
→ response.json Parse
→ API Response Normalize
→ UI Update
```

기본 예:

```javascript
async function getFestivals() {
  const response = await fetch("/api/festivals");

  if (!response.ok) {
    throw new Error("Failed to load festivals");
  }

  return await response.json();
}
```

주의:

- fetch는 Promise를 반환한다.
- fetch는 HTTP 404 / 500 상태를 자동 reject하지 않는다.
- HTTP 오류는 `response.ok`로 직접 확인해야 한다.
- `response.json()`도 Promise를 반환하므로 await가 필요하다.
- 요청 실패, 응답 파싱 실패, 서버 오류를 구분해야 한다.
- 민감정보를 console.log로 출력하지 않는다.

---

### [FAQ]

Q. Fetch API가 뭐야?
A. Browser JavaScript에서 HTTP 요청을 보내고 서버 응답을 받을 수 있게 해주는 기본 Web API다.

Q. fetch는 무엇을 반환해?
A. Promise를 반환한다.

Q. fetch 응답은 바로 JSON data야?
A. 아니다. response.json()을 await해서 JSON body를 파싱해야 한다.

Q. fetch는 404나 500에서 자동으로 catch로 가?
A. 아니다. HTTP 오류 상태는 자동 reject되지 않으므로 response.ok를 확인해야 한다.

---

# 2. HTTP Method

## 2.1 GET Request Rules

### [개념]

GET Request는 서버에서 데이터를 조회할 때 사용하는 HTTP Method다.

Frontend에서는 목록 조회, 상세 조회, 검색, 필터 조회에 사용한다.

예:

```javascript
const response = await fetch("/api/festivals");
```

---

### [핵심]

- GET
- data retrieval
- list request
- detail request
- search request
- query parameter
- no request body
- cache caution
- API endpoint

---

### [실무]

목록 조회:

```javascript
async function fetchFestivals() {
  const response = await fetch("/api/festivals");

  if (!response.ok) {
    throw new Error("Festival list request failed");
  }

  return await response.json();
}
```

상세 조회:

```javascript
async function fetchFestivalDetail(festivalId) {
  const response = await fetch(`/api/festivals/${festivalId}`);

  if (!response.ok) {
    throw new Error("Festival detail request failed");
  }

  return await response.json();
}
```

검색 조회:

```javascript
async function searchFestivals(keyword) {
  const query = encodeURIComponent(keyword.trim());
  const response = await fetch(`/api/festivals/search?keyword=${query}`);

  if (!response.ok) {
    throw new Error("Festival search request failed");
  }

  return await response.json();
}
```

주의:

- GET 요청에는 일반적으로 request body를 넣지 않는다.
- 검색 조건은 query parameter로 전달한다.
- 사용자 입력은 `encodeURIComponent()` 처리한다.
- 빈 검색어 요청 여부를 사전에 판단한다.
- query parameter 이름은 Backend API 스펙과 일치해야 한다.

---

### [FAQ]

Q. GET Request는 언제 써?
A. 서버에서 데이터를 조회할 때 사용한다.

Q. GET 요청에 body를 넣어도 돼?
A. 일반적으로 넣지 않는다. 검색 조건은 query parameter로 전달한다.

Q. 검색어를 query parameter로 보낼 때 주의할 점은?
A. encodeURIComponent로 인코딩해야 한다.

Q. 상세 조회 URL은 보통 어떻게 만들어?
A. `/api/festivals/${festivalId}`처럼 id를 path variable로 넣는 방식이 자주 사용된다.

---

## 2.2 POST Request Rules

### [개념]

POST Request는 서버에 새 데이터를 생성하거나 처리를 요청할 때 사용하는 HTTP Method다.

Frontend에서는 회원가입, 로그인, 리뷰 작성, 댓글 작성, 결제 요청 등에 사용한다.

예:

```javascript
const response = await fetch("/api/reviews", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(review),
});
```

---

### [핵심]

- POST
- create resource
- submit data
- request body
- JSON.stringify
- Content-Type
- application/json
- validation
- API request

---

### [실무]

리뷰 작성 예:

```javascript
async function createReview(review) {
  const response = await fetch("/api/reviews", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(review),
  });

  if (!response.ok) {
    throw new Error("Review create request failed");
  }

  return await response.json();
}
```

로그인 예:

```javascript
async function login({ email, password }) {
  const response = await fetch("/api/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      password,
    }),
  });

  if (!response.ok) {
    throw new Error("Login request failed");
  }

  return await response.json();
}
```

주의:

- JSON body는 `JSON.stringify()`로 문자열 변환한다.
- `Content-Type: application/json` Header를 설정한다.
- 입력값 검증 후 요청한다.
- 비밀번호, 토큰 등 민감정보 로그 출력 금지
- submit 중복 요청 방지
- 서버 Validation Error 응답 처리 필요

---

### [FAQ]

Q. POST Request는 언제 써?
A. 서버에 새 데이터를 생성하거나 처리를 요청할 때 사용한다.

Q. POST JSON body는 어떻게 보내?
A. body에 JSON.stringify 결과를 넣고 Content-Type을 application/json으로 설정한다.

Q. JavaScript 객체를 body에 바로 넣어도 돼?
A. 안 된다. JSON 요청에서는 JSON.stringify로 문자열 변환해야 한다.

Q. 로그인 요청에서 주의할 점은?
A. 비밀번호나 토큰 같은 민감정보를 console.log로 출력하면 안 된다.

---

## 2.3 PUT and PATCH Request Rules

### [개념]

PUT과 PATCH는 서버의 기존 데이터를 수정할 때 사용하는 HTTP Method다.

PUT은 리소스 전체 교체 의미로, PATCH는 리소스 일부 수정 의미로 자주 사용된다.

---

### [핵심]

- PUT
- PATCH
- update resource
- full update
- partial update
- JSON body
- Content-Type
- resource id
- request body

---

### [실무]

수정 요청 예:

```javascript
async function updateUserProfile(userId, profile) {
  const response = await fetch(`/api/users/${userId}`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(profile),
  });

  if (!response.ok) {
    throw new Error("User profile update failed");
  }

  return await response.json();
}
```

축제 정보 수정 예:

```javascript
async function updateFestival(festivalId, requestBody) {
  const response = await fetch(`/api/festivals/${festivalId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(requestBody),
  });

  if (!response.ok) {
    throw new Error("Festival update failed");
  }

  return await response.json();
}
```

주의:

- PUT / PATCH 의미는 팀 API 규칙을 따른다.
- path에 수정 대상 id를 명확히 포함한다.
- JSON body는 stringify한다.
- 수정 요청 전 입력값 검증
- 권한 오류 401 / 403 처리
- 성공 후 화면 상태 갱신 필요

---

### [FAQ]

Q. PUT은 언제 써?
A. 기존 리소스를 전체 수정하거나 교체하는 의미로 사용한다.

Q. PATCH는 언제 써?
A. 기존 리소스의 일부 필드만 수정하는 의미로 사용한다.

Q. PUT과 PATCH 차이는 항상 엄격해?
A. 팀 API 설계 규칙에 따라 달라질 수 있으므로 Backend API 스펙을 따른다.

Q. 수정 요청에도 JSON.stringify가 필요해?
A. JSON body를 보내는 경우 필요하다.

---

## 2.4 DELETE Request Rules

### [개념]

DELETE Request는 서버의 기존 데이터를 삭제할 때 사용하는 HTTP Method다.

Frontend에서는 리뷰 삭제, 댓글 삭제, 찜 해제, 알림 삭제 등에 사용할 수 있다.

예:

```javascript
const response = await fetch(`/api/reviews/${reviewId}`, {
  method: "DELETE",
});
```

---

### [핵심]

- DELETE
- delete resource
- resource id
- no body commonly
- status code
- confirmation
- optimistic update caution
- authorization

---

### [실무]

리뷰 삭제 예:

```javascript
async function deleteReview(reviewId) {
  const response = await fetch(`/api/reviews/${reviewId}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw new Error("Review delete failed");
  }

  return true;
}
```

삭제 후 목록 갱신:

```javascript
const nextReviews = reviews.filter((review) => review.id !== deletedReviewId);
```

주의:

- 삭제 전 사용자 확인이 필요할 수 있다.
- 삭제 대상 id를 명확히 전달한다.
- 권한 오류 처리 필요
- 성공 후 화면 목록에서 제거
- Optimistic Update는 실패 시 rollback 필요
- DELETE 응답 body가 없을 수 있으므로 response.json 호출 전 확인 필요

---

### [FAQ]

Q. DELETE Request는 언제 써?
A. 서버의 기존 데이터를 삭제할 때 사용한다.

Q. DELETE 요청 후 항상 response.json을 호출해도 돼?
A. 응답 body가 없을 수 있으므로 API 스펙을 확인해야 한다.

Q. 삭제 성공 후 화면은 어떻게 갱신해?
A. 목록에서 삭제된 id를 filter로 제거하거나 목록을 다시 조회한다.

Q. 삭제 요청에서 주의할 점은?
A. 삭제 대상 id, 권한 오류, 사용자 확인, 실패 시 rollback을 고려해야 한다.

---

# 3. Headers

## 3.1 Content-Type Header Rules

### [개념]

`Content-Type` Header는 요청 body의 데이터 형식을 서버에 알려주는 HTTP Header다.

JSON 요청에서는 일반적으로 `application/json`을 사용한다.

예:

```javascript
headers: {
  "Content-Type": "application/json",
}
```

---

### [핵심]

- Headers
- Content-Type
- application/json
- request body
- JSON request
- server parsing
- fetch option

---

### [실무]

JSON POST 요청:

```javascript
async function createComment(comment) {
  const response = await fetch("/api/comments", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(comment),
  });

  if (!response.ok) {
    throw new Error("Comment create failed");
  }

  return await response.json();
}
```

주의:

- JSON body를 보낼 때 Content-Type 설정
- GET 요청에는 일반적으로 Content-Type이 필요하지 않음
- FormData 전송 시 Content-Type을 직접 설정하지 않는 경우가 많음
- Backend가 기대하는 Content-Type과 일치해야 함
- Header 이름 오타 주의

---

### [FAQ]

Q. Content-Type Header는 뭐야?
A. 요청 body의 데이터 형식을 서버에 알려주는 Header다.

Q. JSON 요청에는 어떤 Content-Type을 써?
A. application/json을 사용한다.

Q. FormData에도 Content-Type을 직접 application/json으로 설정해?
A. 아니다. FormData는 multipart 전송이므로 직접 설정하지 않는 경우가 많다.

---

## 3.2 Authorization Header Rules

### [개념]

Authorization Header는 인증 정보나 Access Token을 서버에 전달하기 위한 HTTP Header다.

JWT 기반 인증에서는 보통 `Bearer Token` 형식을 사용한다.

예:

```javascript
headers: {
  Authorization: `Bearer ${accessToken}`,
}
```

---

### [핵심]

- Authorization Header
- Bearer Token
- JWT
- Access Token
- authenticated request
- 401
- 403
- token handling
- sensitive data caution

---

### [실무]

인증 요청 예:

```javascript
async function fetchMyProfile(accessToken) {
  const response = await fetch("/api/users/me", {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });

  if (!response.ok) {
    throw new Error("Profile request failed");
  }

  return await response.json();
}
```

JSON + Authorization:

```javascript
async function createFavorite(festivalId, accessToken) {
  const response = await fetch("/api/favorites", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${accessToken}`,
    },
    body: JSON.stringify({ festivalId }),
  });

  if (!response.ok) {
    throw new Error("Favorite request failed");
  }

  return await response.json();
}
```

주의:

- Access Token을 console.log로 출력하지 않는다.
- Authorization Header 형식을 Backend와 맞춘다.
- 401 Unauthorized와 403 Forbidden을 구분한다.
- Token 만료 시 재로그인 또는 refresh flow를 고려한다.
- Browser 저장소에 Token 저장 시 보안 위험을 검토한다.

---

### [FAQ]

Q. Authorization Header는 뭐야?
A. 인증 정보나 Access Token을 서버에 전달하기 위한 Header다.

Q. JWT는 보통 Header에 어떻게 넣어?
A. `Authorization: Bearer <token>` 형식으로 넣는다.

Q. 401과 403 차이는 뭐야?
A. 401은 인증되지 않음, 403은 인증되었지만 권한이 없음을 의미한다.

Q. Access Token을 console.log로 출력해도 돼?
A. 안 된다. Token은 민감정보이므로 로그 출력하면 안 된다.

---

# 4. Query Parameter

## 4.1 Query Parameter Rules

### [개념]

Query Parameter는 URL 뒤에 `?key=value` 형태로 붙는 요청 조건이다.

검색어, 페이지 번호, 정렬 기준, 필터 조건을 전달할 때 자주 사용한다.

예:

```text
/api/festivals/search?keyword=music&page=1
```

---

### [핵심]

- Query Parameter
- query string
- key value
- search keyword
- page
- size
- sort
- filter
- encodeURIComponent
- URLSearchParams

---

### [실무]

단일 query parameter:

```javascript
const keyword = encodeURIComponent(rawKeyword.trim());
const url = `/api/festivals/search?keyword=${keyword}`;
```

여러 query parameter:

```javascript
function createFestivalSearchUrl({ keyword, regionCode, page = 1 }) {
  const params = new URLSearchParams();

  if (keyword?.trim()) {
    params.set("keyword", keyword.trim());
  }

  if (regionCode) {
    params.set("regionCode", regionCode);
  }

  params.set("page", String(page));

  return `/api/festivals/search?${params.toString()}`;
}
```

주의:

- 사용자 입력은 인코딩한다.
- 빈 값은 요청에서 제외할지 Backend 규칙에 맞춘다.
- 숫자 값은 문자열로 변환되어 전달된다.
- parameter 이름은 Backend API와 일치해야 한다.
- URL을 문자열 연결만으로 만들면 누락과 오타가 발생하기 쉽다.
- 복잡한 query는 URLSearchParams 사용을 권장한다.

---

### [FAQ]

Q. Query Parameter는 뭐야?
A. URL 뒤에 key-value 형태로 붙는 요청 조건이다.

Q. 검색어 query에는 왜 encodeURIComponent를 써?
A. 공백이나 특수문자로 인한 URL 오류를 막기 위해 사용한다.

Q. URLSearchParams는 언제 써?
A. 여러 query parameter를 안전하게 조합할 때 사용한다.

Q. query parameter 값은 어떤 타입으로 전달돼?
A. URL에서는 문자열로 전달된다.

---

# 5. Request Body

## 5.1 JSON Request Body Rules

### [개념]

Request Body는 POST, PUT, PATCH 요청에서 서버에 전달하는 데이터 본문이다.

JSON 요청에서는 JavaScript Object를 JSON 문자열로 변환해 body에 넣는다.

예:

```javascript
body: JSON.stringify({
  title: "Festival Review",
  rating: 5,
});
```

---

### [핵심]

- Request Body
- JSON body
- JSON.stringify
- POST
- PUT
- PATCH
- Content-Type
- application/json
- DTO mapping
- request payload

---

### [실무]

리뷰 작성 Request Body:

```javascript
function createReviewRequest({ festivalId, rating, content }) {
  return {
    festivalId,
    rating,
    content: content.trim(),
  };
}
```

요청 전송:

```javascript
async function submitReview(reviewForm) {
  const requestBody = createReviewRequest(reviewForm);

  const response = await fetch("/api/reviews", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(requestBody),
  });

  if (!response.ok) {
    throw new Error("Review submit failed");
  }

  return await response.json();
}
```

주의:

- 요청 body 필드명은 Backend DTO와 일치해야 한다.
- 문자열 입력은 trim 처리한다.
- number 값은 명시적으로 변환한다.
- null 허용 여부를 API 스펙에 맞춘다.
- undefined는 JSON.stringify 과정에서 누락될 수 있다.
- 민감정보는 로그 출력하지 않는다.

---

### [FAQ]

Q. Request Body는 뭐야?
A. POST, PUT, PATCH 요청에서 서버에 전달하는 데이터 본문이다.

Q. JSON Request Body는 어떻게 만들어?
A. JavaScript Object를 JSON.stringify로 문자열 변환해 body에 넣는다.

Q. Request Body 필드명은 무엇과 맞춰야 해?
A. Backend DTO 또는 API 스펙의 필드명과 맞춰야 한다.

Q. undefined는 JSON.stringify에서 어떻게 돼?
A. 객체 property 값이 undefined이면 JSON 문자열에서 누락될 수 있다.

---

# 6. Response Object

## 6.1 Response Object Rules

### [개념]

Response Object는 fetch 요청 결과로 반환되는 HTTP 응답 객체다.

Response Object에는 status, ok, headers, body parsing method가 포함된다.

예:

```javascript
const response = await fetch("/api/festivals");

console.log(response.status);
console.log(response.ok);
```

---

### [핵심]

- Response Object
- response
- response.ok
- response.status
- response.headers
- response.json
- response.text
- body parsing
- HTTP status

---

### [실무]

Response Object 처리 기준:

```javascript
async function requestJson(url) {
  const response = await fetch(url);

  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }

  return await response.json();
}
```

Status 확인:

```javascript
if (response.status === 401) {
  redirectToLogin();
}
```

주의:

- `response.ok`는 status 200~299 범위에서 true다.
- `response.status`로 구체적인 상태 코드를 확인할 수 있다.
- response body는 한 번만 읽을 수 있다.
- JSON이 아닌 응답에 response.json을 호출하면 오류가 발생할 수 있다.
- 204 No Content 응답은 body가 없을 수 있다.

---

### [FAQ]

Q. Response Object는 뭐야?
A. fetch 요청 결과로 반환되는 HTTP 응답 객체다.

Q. response.ok는 뭐야?
A. HTTP status가 200~299 범위이면 true를 반환하는 property다.

Q. response.status는 뭐야?
A. HTTP 상태 코드를 나타내는 property다.

Q. response body는 여러 번 읽을 수 있어?
A. 일반적으로 한 번만 읽을 수 있다.

---

# 7. response.ok and status code

## 7.1 response.ok Rules

### [개념]

`response.ok`는 HTTP 응답 상태 코드가 성공 범위인지 확인하는 boolean property다.

status code가 200 이상 299 이하이면 true다.

예:

```javascript
if (!response.ok) {
  throw new Error("Request failed");
}
```

---

### [핵심]

- response.ok
- HTTP success
- status 200
- status 201
- status 204
- error response
- throw Error
- fetch error handling

---

### [실무]

Fetch API에서는 response.ok 확인이 필수다.

예:

```javascript
async function fetchJson(url) {
  const response = await fetch(url);

  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }

  return await response.json();
}
```

주의:

- fetch는 HTTP 오류 상태에서 자동 reject하지 않는다.
- 404 / 500도 response 객체를 반환할 수 있다.
- `response.ok` 확인 후 throw해야 catch에서 처리 가능
- 204 No Content는 ok지만 body가 없을 수 있음
- status별 처리 정책을 분리할 수 있음

---

### [FAQ]

Q. response.ok는 왜 확인해야 해?
A. fetch는 HTTP 오류 상태를 자동 reject하지 않으므로 직접 성공 여부를 확인해야 한다.

Q. response.ok는 언제 true야?
A. HTTP status가 200 이상 299 이하일 때 true다.

Q. 404 응답도 fetch 성공이야?
A. 네트워크 관점에서는 response가 도착한 것이므로 Promise가 fulfilled될 수 있다. HTTP 성공 여부는 response.ok로 확인한다.

---

## 7.2 Status Code Handling Rules

### [개념]

Status Code Handling은 HTTP 상태 코드에 따라 다른 처리 흐름을 적용하는 것이다.

Frontend에서는 400, 401, 403, 404, 500 상태를 자주 처리한다.

---

### [핵심]

- HTTP Status Code
- 200 OK
- 201 Created
- 204 No Content
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 500 Internal Server Error
- error message

---

### [실무]

Status별 처리 예:

```javascript
async function handleApiResponse(response) {
  if (response.ok) {
    return await response.json();
  }

  if (response.status === 401) {
    throw new Error("Unauthorized");
  }

  if (response.status === 403) {
    throw new Error("Forbidden");
  }

  if (response.status === 404) {
    throw new Error("Not Found");
  }

  throw new Error(`Request failed: ${response.status}`);
}
```

실무 처리 기준:

| Status | 의미         | Frontend 처리              |
| ------ | ------------ | -------------------------- |
| 200    | OK           | 데이터 처리                |
| 201    | Created      | 생성 성공 처리             |
| 204    | No Content   | body 없이 성공 처리        |
| 400    | Bad Request  | 입력 오류 메시지           |
| 401    | Unauthorized | 로그인 필요 처리           |
| 403    | Forbidden    | 권한 없음 메시지           |
| 404    | Not Found    | 데이터 없음 또는 경로 오류 |
| 500    | Server Error | 서버 오류 안내             |

주의:

- 204 응답에는 response.json을 호출하지 않는다.
- 401과 403은 구분해서 처리한다.
- 400 Validation Error는 서버 메시지 구조 확인 필요
- 500은 사용자에게 내부 stack trace를 보여주지 않는다.
- 상태 코드 처리 정책은 API Client Layer에서 통일한다.

---

### [FAQ]

Q. HTTP Status Code Handling은 뭐야?
A. 서버 응답 상태 코드에 따라 다른 처리 흐름을 적용하는 것이다.

Q. 401과 403 차이는 뭐야?
A. 401은 인증되지 않음, 403은 인증은 되었지만 권한이 없음을 의미한다.

Q. 204 응답에서 response.json을 호출해도 돼?
A. body가 없을 수 있으므로 호출하지 않는 것이 안전하다.

Q. 500 오류는 사용자에게 어떻게 보여줘?
A. 내부 오류 상세가 아니라 사용자 친화적인 서버 오류 안내 메시지를 보여준다.

---

# 8. JSON

## 8.1 JSON Concept

### [개념]

JSON은 JavaScript Object Notation의 약자다.

Frontend와 Backend가 데이터를 주고받을 때 자주 사용하는 텍스트 기반 데이터 형식이다.

예:

```json
{
  "id": 1,
  "title": "Spring Festival",
  "active": true
}
```

---

### [핵심]

- JSON
- JavaScript Object Notation
- text format
- key-value
- API response
- request body
- JSON.stringify
- JSON.parse
- serialization
- deserialization

---

### [실무]

Frontend API 연동에서 JSON은 Request Body와 Response Body에 사용된다.

JavaScript Object:

```javascript
const review = {
  festivalId: 1,
  rating: 5,
  content: "좋아요",
};
```

JSON 문자열 변환:

```javascript
const body = JSON.stringify(review);
```

응답 JSON 파싱:

```javascript
const data = await response.json();
```

주의:

- JSON key는 문자열이다.
- JSON에는 function을 포함할 수 없다.
- undefined는 JSON 변환 시 누락될 수 있다.
- Date는 문자열로 전달되는 경우가 많다.
- JSON 문자열과 JavaScript Object를 구분해야 한다.

---

### [FAQ]

Q. JSON이 뭐야?
A. Frontend와 Backend가 데이터를 주고받을 때 자주 사용하는 텍스트 기반 데이터 형식이다.

Q. JSON과 JavaScript Object는 같아?
A. 비슷해 보이지만 다르다. JSON은 텍스트 데이터 형식이고 JavaScript Object는 메모리상의 객체다.

Q. JSON key는 어떤 형태야?
A. 문자열 형태다.

Q. JSON에 function을 넣을 수 있어?
A. 없다.

---

## 8.2 JSON.stringify Rules

### [개념]

`JSON.stringify()`는 JavaScript Object를 JSON 문자열로 변환하는 메서드다.

API Request Body를 만들 때 자주 사용한다.

예:

```javascript
const body = JSON.stringify({
  festivalId: 1,
  rating: 5,
});
```

---

### [핵심]

- JSON.stringify
- object to JSON string
- serialization
- request body
- POST
- PUT
- PATCH
- undefined omission
- Content-Type

---

### [실무]

POST 요청에서 사용:

```javascript
async function createReview(review) {
  const response = await fetch("/api/reviews", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(review),
  });

  if (!response.ok) {
    throw new Error("Review create failed");
  }

  return await response.json();
}
```

주의:

- Object를 body에 직접 넣지 않는다.
- JSON.stringify 결과는 문자열이다.
- undefined property는 누락될 수 있다.
- Date 객체는 문자열로 변환될 수 있다.
- circular reference가 있으면 오류 발생
- 민감정보를 stringify 후 로그 출력하지 않는다.

---

### [FAQ]

Q. JSON.stringify는 언제 써?
A. JavaScript Object를 JSON 문자열로 변환해 API Request Body로 보낼 때 사용한다.

Q. JSON.stringify 결과는 어떤 타입이야?
A. string이다.

Q. undefined property는 JSON.stringify에서 어떻게 돼?
A. 객체 property 값이 undefined이면 누락될 수 있다.

Q. circular reference가 있으면 어떻게 돼?
A. JSON.stringify에서 오류가 발생한다.

---

## 8.3 JSON.parse Rules

### [개념]

`JSON.parse()`는 JSON 문자열을 JavaScript Object로 변환하는 메서드다.

예:

```javascript
const object = JSON.parse('{"id":1,"title":"Festival"}');
```

---

### [핵심]

- JSON.parse
- JSON string to object
- deserialization
- localStorage
- parsing error
- try catch
- valid JSON

---

### [실무]

localStorage에서 JSON 읽기:

```javascript
function getSavedUser() {
  const rawValue = localStorage.getItem("user");

  if (!rawValue) {
    return null;
  }

  try {
    return JSON.parse(rawValue);
  } catch (error) {
    console.error("Invalid saved user JSON:", error);
    return null;
  }
}
```

주의:

- 유효하지 않은 JSON 문자열은 오류를 발생시킨다.
- try / catch로 파싱 실패 처리
- response.json()은 내부적으로 JSON parsing을 수행한다.
- localStorage 값은 문자열이므로 JSON.parse가 필요할 수 있다.
- 민감정보를 localStorage에 저장하지 않는다.

---

### [FAQ]

Q. JSON.parse는 언제 써?
A. JSON 문자열을 JavaScript Object로 변환할 때 사용한다.

Q. JSON.parse는 실패할 수 있어?
A. 유효하지 않은 JSON 문자열이면 오류가 발생한다.

Q. response.json과 JSON.parse는 같아?
A. response.json은 HTTP response body를 JSON으로 파싱하는 비동기 메서드이고, JSON.parse는 문자열을 직접 파싱하는 동기 메서드다.

Q. localStorage 값을 객체로 쓰려면 어떻게 해?
A. 문자열로 저장된 JSON을 JSON.parse로 변환해야 한다.

---

# 9. API Response Structure

## 9.1 Common API Response Structure Rules

### [개념]

API Response Structure는 서버가 Frontend에 응답 데이터를 전달하는 구조다.

Frontend Agent는 응답 구조를 확인하고 UI에서 사용하기 좋은 형태로 변환해야 한다.

예:

```javascript
const responseBody = {
  success: true,
  data: {
    content: [],
  },
  message: "success",
};
```

---

### [핵심]

- API Response Structure
- response body
- success
- data
- content
- message
- error
- pagination
- null handling
- normalize response

---

### [실무]

일반적인 응답 구조:

```javascript
const responseBody = {
  data: {
    content: [
      { id: 1, title: "Festival A" },
      { id: 2, title: "Festival B" },
    ],
    page: 1,
    size: 20,
    totalCount: 2,
  },
};
```

목록 추출:

```javascript
function getContent(responseBody) {
  const content = responseBody?.data?.content;

  return Array.isArray(content) ? content : [];
}
```

주의:

- Backend 응답 Wrapper 구조를 확인한다.
- `data.content`가 항상 존재한다고 가정하지 않는다.
- Pagination 필드를 별도로 처리한다.
- Error Response 구조는 성공 응답과 다를 수 있다.
- UI에서 필요한 구조로 Normalize한다.

---

### [FAQ]

Q. API Response Structure가 뭐야?
A. 서버가 Frontend에 응답 데이터를 전달하는 구조다.

Q. data.content는 항상 배열이야?
A. API 스펙에 따라 다르며 null 또는 undefined일 수 있으므로 확인이 필요하다.

Q. 응답 Wrapper가 있으면 어떻게 처리해?
A. responseBody.data.content처럼 구조를 확인하고 안전하게 추출한다.

Q. Error Response도 성공 응답과 같은 구조야?
A. 아닐 수 있다. Error Response 구조를 별도로 확인해야 한다.

---

## 9.2 Pagination Response Rules

### [개념]

Pagination Response는 목록 데이터를 페이지 단위로 나누어 전달하는 API 응답 구조다.

Frontend에서는 content 목록과 page 정보, hasNext 여부를 함께 처리한다.

예:

```javascript
const responseBody = {
  data: {
    content: [],
    page: 1,
    size: 20,
    hasNext: true,
  },
};
```

---

### [핵심]

- Pagination Response
- content
- page
- size
- totalPages
- totalCount
- hasNext
- Slice
- Page
- infinite scroll
- load more

---

### [실무]

Pagination Normalize 예:

```javascript
function normalizePageResponse(responseBody) {
  const data = responseBody?.data ?? {};
  const content = Array.isArray(data.content) ? data.content : [];

  return {
    items: content,
    page: data.page ?? 1,
    size: data.size ?? content.length,
    totalCount: data.totalCount ?? 0,
    hasNext: data.hasNext ?? false,
  };
}
```

Load More 처리:

```javascript
function appendPageItems(currentItems, nextPageResponse) {
  return [...currentItems, ...nextPageResponse.items];
}
```

주의:

- Page와 Slice 응답 구조가 다를 수 있다.
- `totalCount`가 없을 수 있다.
- `hasNext` 기준으로 더보기 버튼 표시
- page index가 0-based인지 1-based인지 확인
- 새 검색 조건에서는 기존 목록을 초기화한다.
- 기존 목록에 추가할 때 중복 id를 고려한다.

---

### [FAQ]

Q. Pagination Response가 뭐야?
A. 목록 데이터를 페이지 단위로 나누어 전달하는 API 응답 구조다.

Q. content와 page 정보는 어떻게 처리해?
A. content는 items로 추출하고 page, size, totalCount, hasNext 같은 정보를 별도 객체로 정규화한다.

Q. hasNext는 어디에 써?
A. 더보기 버튼 표시나 infinite scroll 추가 요청 여부 판단에 사용한다.

Q. page index는 항상 1부터 시작해?
A. 아니다. Backend API가 0-based인지 1-based인지 확인해야 한다.

---

# 10. API Response Processing

## 10.1 Normalize Function Rules

### [개념]

Normalize Function은 API 응답 데이터를 Frontend UI에서 사용하기 좋은 형태로 변환하는 함수다.

API 원본 구조와 UI 데이터 구조를 분리하기 위해 사용한다.

예:

```javascript
function normalizeFestivalList(responseBody) {
  return responseBody?.data?.content ?? [];
}
```

---

### [핵심]

- Normalize Function
- API Response Processing
- data mapping
- UI data
- default value
- null handling
- Array.isArray
- Pure Function
- response adapter

---

### [실무]

목록 Normalize:

```javascript
function normalizeFestivalList(responseBody) {
  const content = responseBody?.data?.content;

  if (!Array.isArray(content)) {
    return [];
  }

  return content.map((festival) => ({
    id: festival.id,
    title: festival.title ?? "제목 없음",
    imageUrl: festival.imageUrl ?? "/default.png",
    regionName: festival.regionName ?? "지역 정보 없음",
    startDate: festival.startDate ?? null,
  }));
}
```

상세 Normalize:

```javascript
function normalizeFestivalDetail(responseBody) {
  const festival = responseBody?.data;

  if (!festival) {
    return null;
  }

  return {
    id: festival.id,
    title: festival.title ?? "제목 없음",
    description: festival.description ?? "",
    imageUrl: festival.imageUrl ?? "/default.png",
    location: festival.location ?? "위치 정보 없음",
  };
}
```

주의:

- Normalize Function은 Pure Function으로 작성한다.
- API 원본 객체를 직접 변경하지 않는다.
- null / undefined 기본값을 지정한다.
- UI에서 필요한 필드만 추출한다.
- 필드명은 Frontend에서 일관되게 유지한다.
- Mapping 규칙은 API 변경 시 한 곳에서 수정 가능하게 한다.

---

### [FAQ]

Q. Normalize Function이 뭐야?
A. API 응답 데이터를 화면에서 사용하기 좋은 형태로 변환하는 함수다.

Q. Normalize Function은 왜 필요해?
A. API 원본 구조와 UI 데이터 구조를 분리해 유지보수성을 높이기 위해 필요하다.

Q. Normalize Function은 Pure Function이 좋아?
A. 좋다. 입력 응답을 받아 변환 결과만 반환하면 테스트와 리뷰가 쉽다.

Q. API 원본 객체를 직접 변경해도 돼?
A. 지양한다. 원본 응답을 유지하고 새 객체로 변환하는 것이 좋다.

---

## 10.2 Null and Default Value Rules

### [개념]

API Response에는 null, undefined, 빈 문자열, 빈 배열이 포함될 수 있다.

Frontend Agent는 화면 오류를 방지하기 위해 기본값 처리 규칙을 적용해야 한다.

---

### [핵심]

- null handling
- undefined handling
- default value
- optional chaining
- nullish coalescing
- empty array
- empty string
- fallback image
- safe rendering

---

### [실무]

기본값 처리 예:

```javascript
const title = festival?.title ?? "제목 없음";
const imageUrl = festival?.imageUrl ?? "/default.png";
const reviewCount = festival?.reviewCount ?? 0;
const isFavorite = festival?.isFavorite ?? false;
```

목록 기본값:

```javascript
const festivals = Array.isArray(responseBody?.data?.content)
  ? responseBody.data.content
  : [];
```

주의:

- `??`는 null / undefined만 기본값 처리한다.
- `||`는 0, false, ""도 기본값으로 처리할 수 있다.
- count, boolean 값에는 `??`가 안전한 경우가 많다.
- 이미지 URL fallback 필요
- 날짜 값이 null일 수 있음
- UI에 undefined가 직접 표시되지 않게 한다.

---

### [FAQ]

Q. API 응답이 null일 수 있으면 어떻게 해?
A. optional chaining과 nullish coalescing으로 기본값을 지정한다.

Q. 목록 응답 기본값은 무엇이 좋아?
A. 빈 배열 `[]`이 안전하다.

Q. count 기본값에는 `||`보다 `??`가 좋은 이유는?
A. count가 0일 때도 유효한 값으로 유지할 수 있기 때문이다.

Q. UI에 undefined가 보이면 왜 문제야?
A. 사용자에게 잘못된 화면이 보이고 데이터 처리 오류를 숨길 수 있기 때문이다.

---

# 11. Error Response Processing

## 11.1 Error Response Rules

### [개념]

Error Response는 API 요청이 실패했을 때 서버가 반환하는 오류 응답이다.

Frontend에서는 Error Response를 사용자 메시지와 개발자 로그로 구분해 처리해야 한다.

예:

```javascript
const errorResponse = {
  message: "Invalid request",
  errors: {
    content: "내용을 입력하세요.",
  },
};
```

---

### [핵심]

- Error Response
- error message
- validation error
- field error
- global error
- status code
- user message
- developer log
- fallback message

---

### [실무]

Error Body 읽기:

```javascript
async function parseErrorMessage(response) {
  try {
    const errorBody = await response.json();

    return errorBody?.message ?? "요청 처리 중 오류가 발생했습니다.";
  } catch {
    return "요청 처리 중 오류가 발생했습니다.";
  }
}
```

API 처리:

```javascript
async function requestJson(url, options) {
  const response = await fetch(url, options);

  if (!response.ok) {
    const message = await parseErrorMessage(response);

    throw new Error(message);
  }

  return await response.json();
}
```

주의:

- Error Response 구조는 API마다 다를 수 있다.
- Error Body가 JSON이 아닐 수 있다.
- 사용자에게 stack trace를 보여주지 않는다.
- 개발자 로그와 사용자 메시지를 구분한다.
- Validation Error는 필드별 표시 가능
- 민감정보를 오류 메시지에 포함하지 않는다.

---

### [FAQ]

Q. Error Response는 뭐야?
A. API 요청 실패 시 서버가 반환하는 오류 응답이다.

Q. Error Response는 항상 JSON이야?
A. 아니다. API 상황에 따라 JSON이 아닐 수 있으므로 파싱 실패를 처리해야 한다.

Q. 사용자에게 서버 오류 상세를 보여줘도 돼?
A. 안 된다. 사용자 친화적 메시지를 보여주고 상세는 개발자 로그로 관리한다.

Q. Validation Error는 어떻게 표시해?
A. 필드별 오류가 있으면 입력 필드 근처에 표시하고, 전체 오류는 global message로 표시한다.

---

# 12. API Client Function

## 12.1 API Client Function Rules

### [개념]

API Client Function은 Fetch API 공통 로직을 재사용하기 위해 분리한 함수다.

요청, 응답 성공 확인, JSON 파싱, 오류 처리를 공통화한다.

---

### [핵심]

- API Client
- requestJson
- fetch wrapper
- base URL
- headers
- response.ok
- error handling
- JSON parse
- reusable request function

---

### [실무]

공통 API Client 예:

```javascript
async function requestJson(url, options = {}) {
  const response = await fetch(url, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...options.headers,
    },
  });

  if (!response.ok) {
    const message = await parseErrorMessage(response);

    throw new Error(message);
  }

  if (response.status === 204) {
    return null;
  }

  return await response.json();
}
```

사용 예:

```javascript
async function fetchFestivals() {
  return await requestJson("/api/festivals");
}

async function createReview(review) {
  return await requestJson("/api/reviews", {
    method: "POST",
    body: JSON.stringify(review),
  });
}
```

주의:

- 공통 Header와 개별 Header 병합 순서 확인
- FormData 요청에는 Content-Type 자동 설정 예외 필요
- 204 No Content 처리 필요
- 인증 Header 주입 위치 결정
- 오류 처리 정책 통일
- 너무 많은 책임을 API Client 하나에 넣지 않는다.

---

### [FAQ]

Q. API Client Function은 뭐야?
A. Fetch API 공통 로직을 재사용하기 위해 분리한 함수다.

Q. API Client를 쓰는 이유는 뭐야?
A. response.ok 확인, JSON 파싱, 오류 처리, Header 설정을 일관되게 관리하기 위해서다.

Q. 204 응답은 API Client에서 어떻게 처리해?
A. body가 없을 수 있으므로 null을 반환하는 방식으로 처리할 수 있다.

Q. FormData 요청도 같은 API Client를 써도 돼?
A. 가능하지만 Content-Type 자동 설정 예외를 고려해야 한다.

---

## 12.2 Domain API Function Rules

### [개념]

Domain API Function은 특정 Domain의 API endpoint를 함수로 분리한 것이다.

예를 들어 festivalApi, reviewApi, authApi처럼 API 책임을 파일 단위로 나눌 수 있다.

---

### [핵심]

- Domain API Function
- festivalApi
- reviewApi
- authApi
- endpoint separation
- request function
- reusable API layer
- file separation

---

### [실무]

festivalApi 예:

```javascript
const festivalApi = {
  fetchList() {
    return requestJson("/api/festivals");
  },

  fetchDetail(festivalId) {
    return requestJson(`/api/festivals/${festivalId}`);
  },

  search(keyword) {
    const query = encodeURIComponent(keyword.trim());

    return requestJson(`/api/festivals/search?keyword=${query}`);
  },
};
```

reviewApi 예:

```javascript
const reviewApi = {
  create(review) {
    return requestJson("/api/reviews", {
      method: "POST",
      body: JSON.stringify(review),
    });
  },

  delete(reviewId) {
    return requestJson(`/api/reviews/${reviewId}`, {
      method: "DELETE",
    });
  },
};
```

주의:

- Domain별 파일 분리
- endpoint 문자열 중복 최소화
- API 함수명은 목적 중심으로 작성
- UI 컴포넌트에서 fetch 직접 호출 남용 금지
- API 응답 Normalize 함수를 별도로 둘 수 있음
- 인증 필요 API와 공개 API 구분 가능

---

### [FAQ]

Q. Domain API Function은 뭐야?
A. 특정 Domain의 API endpoint 호출을 함수로 분리한 것이다.

Q. festivalApi 같은 파일을 왜 만들어?
A. API endpoint와 요청 로직을 한 곳에서 관리해 유지보수성을 높이기 위해서다.

Q. UI 코드에서 fetch를 바로 써도 돼?
A. 가능하지만 규모가 커지면 API 함수로 분리하는 것이 좋다.

Q. 인증 API와 공개 API는 분리해도 돼?
A. 가능하다. Header나 접근 정책이 다르면 분리하는 것이 좋다.

---

# 13. File Upload and FormData Request

## 13.1 FormData Request Rules

### [개념]

FormData Request는 파일이나 multipart form 데이터를 서버에 전송할 때 사용하는 요청 방식이다.

이미지 업로드, 첨부파일 업로드, 복합 Form 제출에 사용할 수 있다.

---

### [핵심]

- FormData Request
- multipart/form-data
- file upload
- image upload
- append
- File
- Content-Type caution
- upload API

---

### [실무]

파일 업로드 예:

```javascript
async function uploadFestivalImage(file) {
  const formData = new FormData();

  formData.append("image", file);

  const response = await fetch("/api/festival-images", {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Image upload failed");
  }

  return await response.json();
}
```

Form 값과 파일 함께 전송:

```javascript
function createFestivalFormData({ title, imageFile }) {
  const formData = new FormData();

  formData.append("title", title.trim());

  if (imageFile) {
    formData.append("image", imageFile);
  }

  return formData;
}
```

주의:

- FormData 요청에서는 Content-Type을 직접 설정하지 않는 경우가 많다.
- Browser가 boundary를 포함한 multipart Content-Type을 자동 설정한다.
- 파일 크기와 확장자 검증 필요
- Backend field name과 FormData key 일치 필요
- 업로드 중 loading 상태 표시
- 민감정보 파일명 또는 파일 내용 로그 출력 금지

---

### [FAQ]

Q. FormData Request는 언제 써?
A. 파일 업로드나 multipart form 데이터를 서버에 보낼 때 사용한다.

Q. FormData 요청에서 Content-Type을 직접 설정해야 해?
A. 보통 직접 설정하지 않는다. Browser가 boundary를 포함해 자동 설정한다.

Q. FormData key는 무엇과 맞춰야 해?
A. Backend가 받는 field name과 맞춰야 한다.

Q. 파일 업로드에서 주의할 점은?
A. 파일 크기, 확장자, loading 상태, 오류 처리, 민감정보 로그를 주의해야 한다.

---

# 14. Authentication API Flow

## 14.1 Token Request Flow Rules

### [개념]

Authentication API Flow는 로그인 요청, Access Token 저장, 인증 Header 포함, 만료 처리로 이어지는 Frontend 인증 흐름이다.

JavaScript Foundation에서는 기본 Fetch 연동 기준만 다룬다.

---

### [핵심]

- Authentication API
- login
- Access Token
- Refresh Token
- Authorization Header
- Bearer Token
- 401 Unauthorized
- token expiration
- sensitive storage caution

---

### [실무]

로그인 요청 예:

```javascript
async function login(loginRequest) {
  const response = await fetch("/api/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(loginRequest),
  });

  if (!response.ok) {
    throw new Error("Login failed");
  }

  return await response.json();
}
```

인증 요청 예:

```javascript
async function fetchMe(accessToken) {
  const response = await fetch("/api/users/me", {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });

  if (!response.ok) {
    throw new Error("Profile request failed");
  }

  return await response.json();
}
```

주의:

- Token을 console.log로 출력하지 않는다.
- Browser 저장소에 Token 저장 시 보안 위험을 검토한다.
- 401 발생 시 로그인 이동 또는 refresh 처리 필요
- 403은 권한 없음으로 처리
- 인증 흐름 심화는 Authentication Frontend Flow 문서에서 다룬다.

---

### [FAQ]

Q. 인증 API 요청에는 무엇이 필요해?
A. 로그인 후 받은 Access Token을 Authorization Header에 넣어 요청한다.

Q. Bearer Token 형식은 어떻게 작성해?
A. `Authorization: Bearer <accessToken>` 형식으로 작성한다.

Q. Token은 console.log로 확인해도 돼?
A. 안 된다. Token은 민감정보이므로 로그 출력하면 안 된다.

Q. 인증 흐름 심화는 이 문서에서 다뤄?
A. 아니다. 이 문서는 Fetch 연동 기준만 다루고 심화는 Authentication Frontend Flow 문서에서 다룬다.

---

# 15. CORS Basics

## 15.1 CORS Error Rules

### [개념]

CORS는 Cross-Origin Resource Sharing의 약자다.

Browser가 다른 Origin으로 API 요청을 보낼 때 보안 정책에 따라 요청을 제한하거나 허용하는 방식이다.

Frontend에서는 CORS 오류가 API 요청 실패처럼 보일 수 있다.

---

### [핵심]

- CORS
- Cross-Origin Resource Sharing
- Origin
- Browser security policy
- preflight
- OPTIONS
- Backend CORS setting
- API request failure
- Network tab

---

### [실무]

CORS 오류 확인 위치:

```text
Browser Console
→ CORS Error Message
→ Network Tab
→ Request URL
→ Method
→ Request Headers
→ Response Headers
→ Backend CORS Setting
```

Frontend 확인 항목:

- 요청 URL이 올바른가?
- API 서버 주소와 포트가 맞는가?
- Method가 Backend와 일치하는가?
- Header가 과도하게 추가되지 않았는가?
- 인증 Header 사용으로 preflight가 발생하는가?

주의:

- CORS는 대부분 Backend 설정 문제다.
- Frontend에서 완전히 해결할 수 없다.
- 개발 환경 proxy 설정으로 우회할 수 있다.
- 운영 환경에서는 Backend CORS 정책이 정확해야 한다.
- 브라우저 보안 정책이므로 Postman에서는 재현되지 않을 수 있다.

---

### [FAQ]

Q. CORS가 뭐야?
A. Browser가 다른 Origin으로 API 요청을 보낼 때 적용하는 보안 정책이다.

Q. CORS 오류는 Frontend에서 고쳐?
A. 대부분 Backend CORS 설정 문제다. Frontend 요청 URL과 Header도 함께 확인해야 한다.

Q. Postman에서는 되는데 Browser에서 안 되는 이유는?
A. CORS는 Browser 보안 정책이므로 Postman에서는 동일하게 적용되지 않을 수 있다.

Q. CORS 오류는 어디서 확인해?
A. Browser Console과 Network 탭에서 확인한다.

---

# 16. Fetch Debugging

## 16.1 Network Tab Debugging Rules

### [개념]

Network Tab Debugging은 Browser DevTools Network 탭에서 API 요청과 응답을 확인하는 과정이다.

Fetch API 오류 분석의 기본 절차다.

---

### [핵심]

- Network Tab
- Request URL
- Method
- Headers
- Payload
- Query Parameters
- Status Code
- Response Body
- Preview
- Timing
- CORS Error

---

### [실무]

API Debug Flow:

```text
Request Trigger
→ Network Tab Open
→ Request URL Check
→ Method Check
→ Query Parameter Check
→ Request Headers Check
→ Payload Check
→ Status Code Check
→ Response Body Check
→ Frontend Error Handling Check
```

확인 항목:

- URL 오타
- Method 불일치
- Query parameter 누락
- Request body 구조 오류
- Content-Type Header 누락
- Authorization Header 누락
- Status Code
- Response Body 구조
- CORS Error
- 서버가 실제로 응답했는지 여부

주의:

- Console Error만 보지 말고 Network를 확인한다.
- Request Payload와 Backend DTO 필드명을 비교한다.
- Response Body 구조와 Normalize Function을 비교한다.
- 204 응답은 body가 없을 수 있다.
- 민감정보가 Network에 노출되는 것은 당연하므로 저장과 로그에 주의한다.

---

### [FAQ]

Q. Fetch API 요청 실패는 어디서 확인해?
A. Browser DevTools Network 탭에서 URL, Method, Headers, Payload, Status Code, Response Body를 확인한다.

Q. Console Error만 보면 충분해?
A. 아니다. Network 탭에서 실제 요청과 응답을 확인해야 한다.

Q. Payload는 왜 확인해?
A. Frontend가 보낸 Request Body가 Backend DTO와 일치하는지 확인하기 위해서다.

Q. Response Body는 왜 확인해?
A. Frontend Normalize Function이 실제 응답 구조와 맞는지 확인하기 위해서다.

---

# 17. Fetch Practical Example

## 17.1 Festival Search API Example

### [개념]

Fetch Practical Example은 Query Parameter 생성, Fetch 요청, response.ok 확인, JSON 파싱, API Response Normalize, Error Handling을 포함해야 한다.

이 예제는 Frontend Agent가 실무형 API 연동 코드를 생성하는 기준이다.

---

### [핵심]

- Fetch API
- Query Parameter
- URLSearchParams
- response.ok
- response.json
- Normalize Function
- Error Handling
- Loading State
- API Response Processing
- Safe Rendering

---

### [실무]

예:

```javascript
function createFestivalSearchUrl({ keyword, regionCode, page = 1 }) {
  const params = new URLSearchParams();

  if (keyword?.trim()) {
    params.set("keyword", keyword.trim());
  }

  if (regionCode) {
    params.set("regionCode", regionCode);
  }

  params.set("page", String(page));

  return `/api/festivals/search?${params.toString()}`;
}

async function requestJson(url, options = {}) {
  const response = await fetch(url, options);

  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }

  if (response.status === 204) {
    return null;
  }

  return await response.json();
}

function normalizeFestivalList(responseBody) {
  const content = responseBody?.data?.content;

  if (!Array.isArray(content)) {
    return [];
  }

  return content.map((festival) => ({
    id: festival.id,
    title: festival.title ?? "제목 없음",
    regionName: festival.regionName ?? "지역 정보 없음",
    imageUrl: festival.imageUrl ?? "/default.png",
    startDate: festival.startDate ?? null,
  }));
}

async function searchFestivals(searchCondition) {
  const url = createFestivalSearchUrl(searchCondition);
  const responseBody = await requestJson(url);

  return normalizeFestivalList(responseBody);
}
```

이 예제의 목적:

- URLSearchParams 사용
- 빈 query condition 제외
- Fetch 공통 함수 분리
- response.ok 확인
- 204 응답 처리
- JSON parsing
- API 응답 배열 검증
- UI용 데이터 Mapping
- 기본값 처리
- Pure Normalize Function 분리

---

### [FAQ]

Q. Festival Search API 예제에서 URLSearchParams를 쓰는 이유는?
A. 여러 query parameter를 안전하고 명확하게 조합하기 위해서다.

Q. requestJson을 분리한 이유는?
A. response.ok 확인, 204 처리, JSON parsing을 공통화하기 위해서다.

Q. normalizeFestivalList를 분리한 이유는?
A. API 원본 구조와 UI 데이터 구조를 분리하기 위해서다.

Q. content가 배열인지 확인하는 이유는?
A. 배열이 아닌 값에 map을 호출해 발생하는 오류를 방지하기 위해서다.

---

# 18. Fetch JSON API Common Mistakes

## 18.1 Common Mistakes

### [개념]

Fetch, JSON, API Response Processing 실수는 API 요청 실패, JSON 파싱 오류, undefined 접근, 인증 실패, 잘못된 화면 렌더링으로 이어질 수 있다.

Review Agent는 response.ok, response.json await, JSON.stringify, Header, Query Parameter, Normalize Function을 우선 검토해야 한다.

---

### [핵심]

자주 발생하는 실수:

- fetch 결과를 await하지 않음
- response.json await 누락
- response.ok 확인 누락
- 404 / 500이 catch로 자동 이동한다고 오해
- JSON body에 JSON.stringify 누락
- Content-Type Header 누락
- Authorization Header 형식 오류
- Token console.log 출력
- query parameter 인코딩 누락
- Backend DTO 필드명과 Request Body 불일치
- 204 응답에 response.json 호출
- Error Response JSON 파싱 실패 미처리
- data.content를 배열로 가정
- 배열이 아닌 값에 map 호출
- API 원본 객체 직접 변경
- CORS 오류를 Frontend 코드만으로 해결하려고 함
- Network Tab 확인 누락

---

### [실무]

Review Flow:

```text
Fetch Review
→ await fetch Check
→ response.ok Check
→ Status Code Handling Check
→ response.json Await Check
→ JSON.stringify Check
→ Header Check
→ Query Parameter Encoding Check
→ Authorization Header Check
→ Error Response Handling Check
→ Normalize Function Check
→ Network Debugging Check
```

나쁜 예:

```javascript
async function createReview(review) {
  const response = fetch("/api/reviews", {
    method: "POST",
    body: review,
  });

  const data = response.json();

  return data.content.map((item) => item.title);
}
```

개선 예:

```javascript
async function createReview(review) {
  const response = await fetch("/api/reviews", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(review),
  });

  if (!response.ok) {
    throw new Error(`Review create failed: ${response.status}`);
  }

  const data = await response.json();
  const content = data?.content;

  return Array.isArray(content) ? content : [];
}
```

주의:

- fetch, response.json 모두 await 필요
- POST JSON body는 stringify 필요
- HTTP 오류는 response.ok로 확인
- 응답 목록은 배열 확인 후 처리
- Header 형식은 Backend와 일치해야 함
- 민감정보 로그 출력 금지

---

### [FAQ]

Q. Fetch API에서 가장 흔한 실수는 뭐야?
A. response.ok 확인 누락, response.json await 누락, JSON.stringify 누락, Header 누락이다.

Q. JSON 처리에서 가장 흔한 실수는 뭐야?
A. JavaScript Object와 JSON 문자열을 혼동하거나 undefined 값 누락을 인지하지 못하는 것이다.

Q. API Response Processing에서 가장 흔한 실수는 뭐야?
A. data.content를 항상 배열로 가정하고 바로 map을 호출하는 것이다.

Q. Review Agent는 Fetch 코드에서 무엇을 우선 확인해야 해?
A. await, response.ok, status code 처리, Header, JSON.stringify, Normalize Function, 민감정보 로그를 우선 확인해야 한다.

---

# 19. Fetch JSON API Checklist

## 19.1 Document Quality Checklist

### [개념]

Fetch, JSON, API Response Processing 문서는 Frontend Agent가 Backend API와 안전하게 연동하고 응답 데이터를 UI에 맞게 변환하도록 지원해야 한다.

Checklist는 RAG Retrieval 품질과 Review Agent 검토 기준을 유지하기 위한 기준이다.

---

### [핵심]

검수 항목:

- [ ] Fetch API 개념이 포함되었는가?
- [ ] GET Request 설명이 포함되었는가?
- [ ] POST Request 설명이 포함되었는가?
- [ ] PUT / PATCH Request 설명이 포함되었는가?
- [ ] DELETE Request 설명이 포함되었는가?
- [ ] Content-Type Header 설명이 포함되었는가?
- [ ] Authorization Header 설명이 포함되었는가?
- [ ] Query Parameter 설명이 포함되었는가?
- [ ] Request Body 설명이 포함되었는가?
- [ ] Response Object 설명이 포함되었는가?
- [ ] response.ok 기준이 포함되었는가?
- [ ] Status Code Handling 기준이 포함되었는가?
- [ ] JSON 개념이 포함되었는가?
- [ ] JSON.stringify 설명이 포함되었는가?
- [ ] JSON.parse 설명이 포함되었는가?
- [ ] API Response Structure 설명이 포함되었는가?
- [ ] Pagination Response 설명이 포함되었는가?
- [ ] Normalize Function 설명이 포함되었는가?
- [ ] Null / Default Value 처리 기준이 포함되었는가?
- [ ] Error Response Processing 기준이 포함되었는가?
- [ ] API Client Function 설명이 포함되었는가?
- [ ] Domain API Function 설명이 포함되었는가?
- [ ] FormData Request 설명이 포함되었는가?
- [ ] Authentication API Flow 기본 기준이 포함되었는가?
- [ ] CORS Basics 설명이 포함되었는가?
- [ ] Network Tab Debugging 기준이 포함되었는가?
- [ ] 실무형 Fetch 예제가 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?

---

### [실무]

검수 Flow:

```text
Draft
→ MASTER_RAG_RULES Section Check
→ JavaScript Domain Scope Check
→ Fetch Method Check
→ Header Check
→ Request Body Check
→ Response Status Check
→ JSON Processing Check
→ API Response Normalize Check
→ Error Handling Check
→ Debugging Check
→ Common Mistakes Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

파일 간 연계:

```text
JavaScript_Foundation_Part07_Async_Promise_AsyncAwait
→ JavaScript_Foundation_Part08_Fetch_JSON_API_Response
→ JavaScript_Foundation_Part09_Module_Error_Debugging
```

---

### [FAQ]

Q. Fetch JSON API 문서 검수에서 가장 중요한 것은 뭐야?
A. response.ok 확인, JSON.stringify, response.json await, Header, Status Code, Normalize Function, Error Response Handling이다.

Q. 이 문서는 React와 어떻게 연결돼?
A. React Data Fetching, API Client Layer, Server State, Loading / Error UI, Form Submit 연동의 기반이 된다.

Q. 다음 Part와 어떻게 연결돼?
A. Part08은 실제 서버 연동 기준을 만들고, Part09는 Module, Error Handling, Browser Debugging으로 코드 분리와 오류 분석을 확장한다.

---

# Retrieval Queries

### [FAQ]

Q. Fetch API가 뭐야?
A. Browser JavaScript에서 HTTP 요청을 보내고 서버 응답을 받을 수 있게 해주는 기본 Web API다.

Q. fetch는 무엇을 반환해?
A. Promise를 반환한다.

Q. fetch 응답은 바로 JSON data야?
A. 아니다. response.json()을 await해서 JSON body를 파싱해야 한다.

Q. fetch는 404나 500에서 자동으로 catch로 가?
A. 아니다. HTTP 오류 상태는 자동 reject되지 않으므로 response.ok를 확인해야 한다.

Q. GET Request는 언제 써?
A. 서버에서 데이터를 조회할 때 사용한다.

Q. GET 요청에 body를 넣어도 돼?
A. 일반적으로 넣지 않는다. 검색 조건은 query parameter로 전달한다.

Q. POST Request는 언제 써?
A. 서버에 새 데이터를 생성하거나 처리를 요청할 때 사용한다.

Q. POST JSON body는 어떻게 보내?
A. body에 JSON.stringify 결과를 넣고 Content-Type을 application/json으로 설정한다.

Q. JavaScript 객체를 body에 바로 넣어도 돼?
A. 안 된다. JSON 요청에서는 JSON.stringify로 문자열 변환해야 한다.

Q. PUT은 언제 써?
A. 기존 리소스를 전체 수정하거나 교체하는 의미로 사용한다.

Q. PATCH는 언제 써?
A. 기존 리소스의 일부 필드만 수정하는 의미로 사용한다.

Q. DELETE Request는 언제 써?
A. 서버의 기존 데이터를 삭제할 때 사용한다.

Q. DELETE 요청 후 항상 response.json을 호출해도 돼?
A. 응답 body가 없을 수 있으므로 API 스펙을 확인해야 한다.

Q. Content-Type Header는 뭐야?
A. 요청 body의 데이터 형식을 서버에 알려주는 Header다.

Q. JSON 요청에는 어떤 Content-Type을 써?
A. application/json을 사용한다.

Q. Authorization Header는 뭐야?
A. 인증 정보나 Access Token을 서버에 전달하기 위한 Header다.

Q. JWT는 보통 Header에 어떻게 넣어?
A. Authorization: Bearer token 형식으로 넣는다.

Q. 401과 403 차이는 뭐야?
A. 401은 인증되지 않음, 403은 인증은 되었지만 권한이 없음을 의미한다.

Q. Access Token을 console.log로 출력해도 돼?
A. 안 된다. Token은 민감정보이므로 로그 출력하면 안 된다.

Q. Query Parameter는 뭐야?
A. URL 뒤에 key-value 형태로 붙는 요청 조건이다.

Q. 검색어 query에는 왜 encodeURIComponent를 써?
A. 공백이나 특수문자로 인한 URL 오류를 막기 위해 사용한다.

Q. URLSearchParams는 언제 써?
A. 여러 query parameter를 안전하게 조합할 때 사용한다.

Q. Request Body는 뭐야?
A. POST, PUT, PATCH 요청에서 서버에 전달하는 데이터 본문이다.

Q. JSON Request Body는 어떻게 만들어?
A. JavaScript Object를 JSON.stringify로 문자열 변환해 body에 넣는다.

Q. Request Body 필드명은 무엇과 맞춰야 해?
A. Backend DTO 또는 API 스펙의 필드명과 맞춰야 한다.

Q. Response Object는 뭐야?
A. fetch 요청 결과로 반환되는 HTTP 응답 객체다.

Q. response.ok는 뭐야?
A. HTTP status가 200~299 범위이면 true를 반환하는 property다.

Q. response.status는 뭐야?
A. HTTP 상태 코드를 나타내는 property다.

Q. response body는 여러 번 읽을 수 있어?
A. 일반적으로 한 번만 읽을 수 있다.

Q. response.ok는 왜 확인해야 해?
A. fetch는 HTTP 오류 상태를 자동 reject하지 않으므로 직접 성공 여부를 확인해야 한다.

Q. response.ok는 언제 true야?
A. HTTP status가 200 이상 299 이하일 때 true다.

Q. HTTP Status Code Handling은 뭐야?
A. 서버 응답 상태 코드에 따라 다른 처리 흐름을 적용하는 것이다.

Q. 204 응답에서 response.json을 호출해도 돼?
A. body가 없을 수 있으므로 호출하지 않는 것이 안전하다.

Q. JSON이 뭐야?
A. Frontend와 Backend가 데이터를 주고받을 때 자주 사용하는 텍스트 기반 데이터 형식이다.

Q. JSON과 JavaScript Object는 같아?
A. 비슷해 보이지만 다르다. JSON은 텍스트 데이터 형식이고 JavaScript Object는 메모리상의 객체다.

Q. JSON.stringify는 언제 써?
A. JavaScript Object를 JSON 문자열로 변환해 API Request Body로 보낼 때 사용한다.

Q. JSON.stringify 결과는 어떤 타입이야?
A. string이다.

Q. undefined property는 JSON.stringify에서 어떻게 돼?
A. 객체 property 값이 undefined이면 누락될 수 있다.

Q. JSON.parse는 언제 써?
A. JSON 문자열을 JavaScript Object로 변환할 때 사용한다.

Q. JSON.parse는 실패할 수 있어?
A. 유효하지 않은 JSON 문자열이면 오류가 발생한다.

Q. response.json과 JSON.parse는 같아?
A. response.json은 HTTP response body를 JSON으로 파싱하는 비동기 메서드이고, JSON.parse는 문자열을 직접 파싱하는 동기 메서드다.

Q. API Response Structure가 뭐야?
A. 서버가 Frontend에 응답 데이터를 전달하는 구조다.

Q. data.content는 항상 배열이야?
A. API 스펙에 따라 다르며 null 또는 undefined일 수 있으므로 확인이 필요하다.

Q. Error Response도 성공 응답과 같은 구조야?
A. 아닐 수 있다. Error Response 구조를 별도로 확인해야 한다.

Q. Pagination Response가 뭐야?
A. 목록 데이터를 페이지 단위로 나누어 전달하는 API 응답 구조다.

Q. hasNext는 어디에 써?
A. 더보기 버튼 표시나 infinite scroll 추가 요청 여부 판단에 사용한다.

Q. page index는 항상 1부터 시작해?
A. 아니다. Backend API가 0-based인지 1-based인지 확인해야 한다.

Q. Normalize Function이 뭐야?
A. API 응답 데이터를 화면에서 사용하기 좋은 형태로 변환하는 함수다.

Q. Normalize Function은 왜 필요해?
A. API 원본 구조와 UI 데이터 구조를 분리해 유지보수성을 높이기 위해 필요하다.

Q. API 원본 객체를 직접 변경해도 돼?
A. 지양한다. 원본 응답을 유지하고 새 객체로 변환하는 것이 좋다.

Q. API 응답이 null일 수 있으면 어떻게 해?
A. optional chaining과 nullish coalescing으로 기본값을 지정한다.

Q. 목록 응답 기본값은 무엇이 좋아?
A. 빈 배열 []이 안전하다.

Q. Error Response는 뭐야?
A. API 요청 실패 시 서버가 반환하는 오류 응답이다.

Q. Error Response는 항상 JSON이야?
A. 아니다. API 상황에 따라 JSON이 아닐 수 있으므로 파싱 실패를 처리해야 한다.

Q. API Client Function은 뭐야?
A. Fetch API 공통 로직을 재사용하기 위해 분리한 함수다.

Q. API Client를 쓰는 이유는 뭐야?
A. response.ok 확인, JSON 파싱, 오류 처리, Header 설정을 일관되게 관리하기 위해서다.

Q. Domain API Function은 뭐야?
A. 특정 Domain의 API endpoint 호출을 함수로 분리한 것이다.

Q. UI 코드에서 fetch를 바로 써도 돼?
A. 가능하지만 규모가 커지면 API 함수로 분리하는 것이 좋다.

Q. FormData Request는 언제 써?
A. 파일 업로드나 multipart form 데이터를 서버에 보낼 때 사용한다.

Q. FormData 요청에서 Content-Type을 직접 설정해야 해?
A. 보통 직접 설정하지 않는다. Browser가 boundary를 포함해 자동 설정한다.

Q. 인증 API 요청에는 무엇이 필요해?
A. 로그인 후 받은 Access Token을 Authorization Header에 넣어 요청한다.

Q. CORS가 뭐야?
A. Browser가 다른 Origin으로 API 요청을 보낼 때 적용하는 보안 정책이다.

Q. CORS 오류는 Frontend에서 고쳐?
A. 대부분 Backend CORS 설정 문제다. Frontend 요청 URL과 Header도 함께 확인해야 한다.

Q. Postman에서는 되는데 Browser에서 안 되는 이유는?
A. CORS는 Browser 보안 정책이므로 Postman에서는 동일하게 적용되지 않을 수 있다.

Q. Fetch API 요청 실패는 어디서 확인해?
A. Browser DevTools Network 탭에서 URL, Method, Headers, Payload, Status Code, Response Body를 확인한다.

Q. Console Error만 보면 충분해?
A. 아니다. Network 탭에서 실제 요청과 응답을 확인해야 한다.

Q. Payload는 왜 확인해?
A. Frontend가 보낸 Request Body가 Backend DTO와 일치하는지 확인하기 위해서다.

Q. Response Body는 왜 확인해?
A. Frontend Normalize Function이 실제 응답 구조와 맞는지 확인하기 위해서다.

Q. Fetch API에서 가장 흔한 실수는 뭐야?
A. response.ok 확인 누락, response.json await 누락, JSON.stringify 누락, Header 누락이다.

Q. JSON 처리에서 가장 흔한 실수는 뭐야?
A. JavaScript Object와 JSON 문자열을 혼동하거나 undefined 값 누락을 인지하지 못하는 것이다.

Q. API Response Processing에서 가장 흔한 실수는 뭐야?
A. data.content를 항상 배열로 가정하고 바로 map을 호출하는 것이다.

Q. Review Agent는 Fetch 코드에서 무엇을 우선 확인해야 해?
A. await, response.ok, status code 처리, Header, JSON.stringify, Normalize Function, 민감정보 로그를 우선 확인해야 한다.

Q. JavaScript Foundation Part08 다음에는 무엇을 다뤄야 해?
A. Module, Error Handling, Browser Debugging을 다루는 Part09로 이어지는 것이 좋다.
