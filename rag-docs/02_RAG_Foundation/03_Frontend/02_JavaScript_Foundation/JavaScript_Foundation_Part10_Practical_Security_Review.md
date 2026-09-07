# JavaScript Foundation Part10 - Practical Logic, Security, Troubleshooting, and Review Checklist

---

# 1. Frontend Practical Logic

## 1.1 Practical Logic Concept

### [개념]

Frontend Practical Logic은 JavaScript 기본 문법, Array / Object 처리, DOM / Event, Async / Fetch, Error Handling을 실제 화면 기능으로 연결하는 로직이다.

JavaScript Foundation의 최종 목표는 단순 문법 이해가 아니라 Frontend Agent가 안전하고 유지보수 가능한 화면 로직을 생성하고 Review Agent가 문제를 검출할 수 있게 하는 것이다.

Practical Logic은 다음 흐름을 기준으로 작성한다.

```text
User Action
→ Event Handler
→ Validation
→ API Request
→ Response Processing
→ UI State Update
→ Error Handling
```

---

### [핵심]

- Frontend Practical Logic
- UI Logic
- Event Handler
- Form Validation
- API Request
- Response Normalize
- Loading State
- Error State
- Empty State
- Security
- Troubleshooting
- Review Checklist
- React Readiness

---

### [실무]

2026 실무 기준에서 Frontend JavaScript는 아래 단위로 분리하는 것이 좋다.

```text
Input Handling
→ Validation Function
→ API Function
→ Normalize Function
→ Render Function
→ Error Function
```

역할 분리 예:

```javascript
function validateKeyword(keyword) {
  return keyword.trim().length > 0;
}

async function fetchFestivals(keyword) {
  const response = await fetch(
    `/api/festivals/search?keyword=${encodeURIComponent(keyword.trim())}`,
  );

  if (!response.ok) {
    throw new Error("Festival search failed");
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
    imageUrl: festival.imageUrl ?? "/default.png",
  }));
}
```

주의:

- Event Handler에 모든 로직을 넣지 않는다.
- API 요청과 UI 렌더링을 분리한다.
- API 응답 구조와 UI 데이터 구조를 분리한다.
- Loading / Error / Empty 상태를 명확히 구분한다.
- 사용자 입력과 API 응답을 신뢰하지 않는다.
- 보안과 Debugging 기준을 코드 생성 단계부터 반영한다.

---

### [FAQ]

Q. Frontend Practical Logic이 뭐야?
A. JavaScript 문법과 Browser API를 실제 화면 기능으로 연결하는 실무 로직이다.

Q. JavaScript Foundation의 최종 목표는 뭐야?
A. Frontend Agent가 안전한 화면 로직을 생성하고 Review Agent가 오류와 보안 문제를 검출할 수 있게 하는 것이다.

Q. Event Handler에 모든 코드를 넣어도 돼?
A. 지양한다. 입력 처리, 검증, API 요청, 응답 가공, 렌더링, 오류 처리를 분리하는 것이 좋다.

Q. Practical Logic에서 가장 중요한 기준은 뭐야?
A. 역할 분리, null 방어, 비동기 에러 처리, 보안, 사용자 상태 표시다.

---

# 2. UI State Pattern

## 2.1 Loading Error Empty Success Pattern

### [개념]

UI State Pattern은 화면의 상태를 loading, error, empty, success로 나누어 처리하는 방식이다.

API 연동 화면에서는 데이터가 없는 상태와 오류 상태, 로딩 상태를 명확히 구분해야 한다.

---

### [핵심]

- UI State
- loading
- error
- empty
- success
- request status
- list status
- conditional UI
- user feedback
- state priority

---

### [실무]

상태 판단 함수:

```javascript
function getListStatus({ loading, error, items }) {
  if (loading) {
    return "LOADING";
  }

  if (error) {
    return "ERROR";
  }

  if (items.length === 0) {
    return "EMPTY";
  }

  return "SUCCESS";
}
```

상태별 메시지:

```javascript
function getStatusMessage(status) {
  switch (status) {
    case "LOADING":
      return "불러오는 중입니다.";
    case "ERROR":
      return "데이터를 불러오지 못했습니다.";
    case "EMPTY":
      return "표시할 데이터가 없습니다.";
    case "SUCCESS":
      return "";
    default:
      return "알 수 없는 상태입니다.";
  }
}
```

상태 우선순위:

```text
Loading
→ Error
→ Empty
→ Success
```

주의:

- loading 중에는 empty를 먼저 표시하지 않는다.
- error 상태와 empty 상태를 혼동하지 않는다.
- success 상태에서도 목록이 빈 배열일 수 있다.
- 사용자에게 현재 상태를 명확히 보여준다.
- React 전환 시 상태 객체 또는 reducer로 관리할 수 있다.

---

### [FAQ]

Q. UI State Pattern이 뭐야?
A. 화면 상태를 loading, error, empty, success로 구분해 처리하는 방식이다.

Q. loading과 empty 중 무엇을 먼저 판단해?
A. loading을 먼저 판단한다. 요청 중에는 아직 데이터 없음 상태로 확정할 수 없다.

Q. error와 empty는 어떻게 달라?
A. error는 요청 실패이고 empty는 요청은 성공했지만 표시할 데이터가 없는 상태다.

Q. UI State Pattern은 React와 관련 있어?
A. 관련 있다. React 조건부 렌더링과 서버 데이터 상태 관리의 기반이 된다.

---

## 2.2 Request Status Object Rules

### [개념]

Request Status Object는 API 요청 상태를 하나의 객체로 관리하는 방식이다.

loading, error, data를 함께 관리하면 화면 상태 판단이 명확해진다.

예:

```javascript
const listState = {
  loading: false,
  error: null,
  items: [],
};
```

---

### [핵심]

- Request Status Object
- loading
- error
- data
- items
- status
- state object
- API state
- UI condition
- React readiness

---

### [실무]

상태 객체 예:

```javascript
let festivalListState = {
  loading: false,
  error: null,
  items: [],
};
```

상태 업데이트 함수:

```javascript
function setFestivalListState(nextState) {
  festivalListState = {
    ...festivalListState,
    ...nextState,
  };
}
```

API 요청 흐름:

```javascript
async function loadFestivals() {
  setFestivalListState({
    loading: true,
    error: null,
  });

  try {
    const responseBody = await fetchFestivals();
    const items = normalizeFestivalList(responseBody);

    setFestivalListState({
      items,
      error: null,
    });
  } catch (error) {
    console.error("Festival load failed:", error);

    setFestivalListState({
      error: "축제 목록을 불러오지 못했습니다.",
      items: [],
    });
  } finally {
    setFestivalListState({
      loading: false,
    });
  }
}
```

주의:

- loading, error, items를 따로 흩어 관리하면 상태 불일치가 생길 수 있다.
- 실패 시 기존 데이터를 유지할지 비울지 정책을 정한다.
- 상태 객체 업데이트는 immutable update를 고려한다.
- React에서는 useState 또는 useReducer로 전환 가능하다.
- 상태 이름은 Domain을 드러내는 것이 좋다.

---

### [FAQ]

Q. Request Status Object는 뭐야?
A. API 요청 상태를 loading, error, data 같은 값으로 묶어 관리하는 객체다.

Q. loading과 error를 따로 관리하면 안 돼?
A. 가능하지만 상태가 많아지면 하나의 객체로 묶는 것이 흐름을 이해하기 쉽다.

Q. 실패 시 items를 비워야 해?
A. 상황에 따라 다르다. 기존 데이터를 유지할지 비울지 정책을 명확히 해야 한다.

Q. Request Status Object는 React에서 어떻게 연결돼?
A. useState 객체 상태나 useReducer 상태 구조로 전환할 수 있다.

---

# 3. Search Feature Practical Pattern

## 3.1 Search Flow Rules

### [개념]

Search Feature는 사용자 입력을 받아 검증하고 query parameter를 생성해 API 요청을 보내고 결과 목록을 표시하는 대표 Frontend 기능이다.

검색 기능은 JavaScript Foundation 전체 개념을 통합하는 실무 예제다.

---

### [핵심]

- Search Feature
- input value
- trim
- validation
- query parameter
- encodeURIComponent
- URLSearchParams
- fetch
- loading state
- error state
- empty state
- race condition
- debounce

---

### [실무]

검색 Flow:

```text
Input Change
→ Normalize Keyword
→ Validate
→ Debounce
→ Create Query Parameter
→ Fetch Search API
→ Normalize Response
→ Render Result
→ Handle Loading / Error / Empty
```

검색 URL 생성:

```javascript
function createSearchUrl({ keyword, page = 1 }) {
  const params = new URLSearchParams();

  if (keyword?.trim()) {
    params.set("keyword", keyword.trim());
  }

  params.set("page", String(page));

  return `/api/festivals/search?${params.toString()}`;
}
```

검색 실행:

```javascript
async function searchFestivals({ keyword, page = 1 }) {
  const query = keyword.trim();

  if (!query) {
    return [];
  }

  const response = await fetch(createSearchUrl({ keyword: query, page }));

  if (!response.ok) {
    throw new Error("Festival search failed");
  }

  const responseBody = await response.json();

  return normalizeFestivalList(responseBody);
}
```

주의:

- 빈 검색어 요청 여부를 정책으로 정한다.
- 검색어는 trim 처리한다.
- query parameter는 인코딩한다.
- 빠른 입력에는 debounce를 고려한다.
- 최신 요청만 화면에 반영해야 할 수 있다.
- API 오류와 검색 결과 없음은 구분한다.

---

### [FAQ]

Q. Search Feature의 기본 흐름은 뭐야?
A. 입력값 정리, 검증, query parameter 생성, API 요청, 응답 정규화, 결과 렌더링 순서다.

Q. 검색어는 왜 trim 처리해?
A. 공백만 입력된 값을 유효한 검색어로 처리하지 않기 위해서다.

Q. 검색 기능에서 debounce가 필요한 이유는?
A. 입력마다 API 요청이 발생하는 것을 줄이기 위해서다.

Q. 검색 결과 없음과 API 오류는 어떻게 달라?
A. 결과 없음은 요청 성공 후 목록이 빈 상태이고, API 오류는 요청 자체가 실패한 상태다.

---

# 4. Pagination and Load More Pattern

## 4.1 Pagination Rules

### [개념]

Pagination은 목록 데이터를 여러 페이지로 나누어 조회하고 표시하는 방식이다.

Frontend에서는 page, size, hasNext, totalCount 같은 값을 관리한다.

---

### [핵심]

- Pagination
- page
- size
- totalCount
- totalPages
- hasNext
- load more
- infinite scroll
- append list
- reset list
- duplicate item

---

### [실무]

Pagination 상태:

```javascript
const paginationState = {
  page: 1,
  size: 20,
  hasNext: false,
  items: [],
};
```

응답 정규화:

```javascript
function normalizePageResponse(responseBody) {
  const data = responseBody?.data ?? {};
  const content = Array.isArray(data.content) ? data.content : [];

  return {
    items: content,
    page: data.page ?? 1,
    size: data.size ?? content.length,
    hasNext: data.hasNext ?? false,
    totalCount: data.totalCount ?? 0,
  };
}
```

더보기 처리:

```javascript
function appendItems(currentItems, nextItems) {
  return [...currentItems, ...nextItems];
}
```

새 검색 조건 처리:

```javascript
function resetListForNewSearch(items) {
  return {
    page: 1,
    items,
  };
}
```

주의:

- page index가 0-based인지 1-based인지 확인한다.
- 새 검색 조건에서는 기존 목록을 초기화한다.
- load more에서는 기존 목록에 추가한다.
- 중복 id가 섞일 수 있으면 deduplication을 고려한다.
- hasNext가 false이면 추가 요청을 막는다.
- loading 중 중복 더보기 요청을 막는다.

---

### [FAQ]

Q. Pagination이 뭐야?
A. 목록 데이터를 여러 페이지로 나누어 조회하고 표시하는 방식이다.

Q. 새 검색 조건에서는 기존 목록을 어떻게 해야 해?
A. 기존 목록을 초기화하고 첫 페이지부터 다시 조회하는 것이 일반적이다.

Q. 더보기에서는 목록을 어떻게 처리해?
A. 기존 목록 뒤에 다음 페이지 items를 append한다.

Q. hasNext는 왜 필요해?
A. 다음 페이지 요청 가능 여부를 판단하기 위해 필요하다.

---

# 5. Security Basics

## 5.1 Frontend Security Concept

### [개념]

Frontend Security는 Browser에서 실행되는 JavaScript 코드가 사용자 입력, API 응답, 인증 정보, 외부 URL, DOM 조작을 안전하게 처리하도록 하는 기준이다.

Frontend 코드는 사용자에게 노출될 수 있으므로 비밀 값을 숨기는 장소로 사용하면 안 된다.

---

### [핵심]

- Frontend Security
- Browser Security
- XSS
- Token Exposure
- Sensitive Data
- innerHTML Risk
- localStorage Risk
- CORS
- HTTPS
- Input Validation
- Output Encoding
- Secure API Integration

---

### [실무]

Frontend Security 기본 원칙:

```text
Do Not Trust User Input
Do Not Trust API Response Blindly
Do Not Store Secrets in Frontend Code
Do Not Log Sensitive Data
Do Not Insert User Input with innerHTML
```

보안상 금지:

```javascript
console.log(accessToken);
console.log(password);
container.innerHTML = userInput;
```

안전한 방향:

```javascript
container.textContent = userInput;
```

주의:

- API Key, Secret Key, DB Password를 Frontend 코드에 넣지 않는다.
- Browser JavaScript는 사용자에게 노출될 수 있다.
- 사용자 입력은 검증하고 출력은 안전하게 처리한다.
- Frontend Validation은 UX용이고 Backend Validation이 필수다.
- 인증과 권한 검증은 Backend에서 반드시 수행해야 한다.
- 보안 관련 판단은 Frontend만 신뢰하지 않는다.

---

### [FAQ]

Q. Frontend Security가 뭐야?
A. Browser에서 실행되는 JavaScript가 입력, 출력, 인증 정보, DOM 조작을 안전하게 처리하도록 하는 기준이다.

Q. Frontend 코드에 Secret Key를 넣어도 돼?
A. 안 된다. Frontend 코드는 사용자에게 노출될 수 있으므로 Secret을 넣으면 안 된다.

Q. Frontend Validation만으로 보안 검증이 충분해?
A. 아니다. Frontend Validation은 UX용이고 Backend Validation과 권한 검증이 필수다.

Q. 사용자 입력은 신뢰해도 돼?
A. 안 된다. 사용자 입력은 항상 검증하고 안전하게 출력해야 한다.

---

# 6. XSS Prevention

## 6.1 XSS Concept

### [개념]

XSS는 Cross-Site Scripting의 약자다.

공격자가 악성 script를 웹 페이지에 삽입해 사용자의 브라우저에서 실행되게 만드는 취약점이다.

Frontend에서는 사용자 입력이나 API 응답을 HTML로 직접 삽입할 때 XSS 위험이 커진다.

---

### [핵심]

- XSS
- Cross-Site Scripting
- malicious script
- user input
- API response
- innerHTML
- textContent
- output encoding
- DOM injection
- security review

---

### [실무]

위험한 코드:

```javascript
const comment = form.comment.value;

commentContainer.innerHTML = comment;
```

안전한 코드:

```javascript
const comment = form.comment.value;

commentContainer.textContent = comment;
```

동적 목록 안전 렌더링:

```javascript
function createCommentItem(comment) {
  const itemElement = document.createElement("li");

  itemElement.textContent = comment.content ?? "";

  return itemElement;
}
```

주의:

- 사용자 입력을 innerHTML에 직접 넣지 않는다.
- API 응답도 신뢰하지 않는다.
- HTML 렌더링이 꼭 필요하면 sanitize 정책이 필요하다.
- textContent는 HTML을 해석하지 않는다.
- React는 기본적으로 문자열 escape를 수행하지만 dangerouslySetInnerHTML은 위험하다.
- Review Agent는 innerHTML, dangerouslySetInnerHTML, 외부 HTML 삽입을 우선 검토해야 한다.

---

### [FAQ]

Q. XSS가 뭐야?
A. 악성 script가 웹 페이지에 삽입되어 사용자 브라우저에서 실행되는 취약점이다.

Q. innerHTML이 왜 위험해?
A. 문자열을 HTML로 파싱하기 때문에 악성 script가 실행될 수 있다.

Q. 사용자 입력을 출력할 때 무엇을 우선 사용해?
A. textContent를 우선 사용한다.

Q. API 응답은 신뢰해도 돼?
A. 아니다. API 응답도 악의적이거나 오염될 수 있으므로 안전하게 처리해야 한다.

---

# 7. Sensitive Data Handling

## 7.1 Sensitive Data Rules

### [개념]

Sensitive Data는 노출되면 보안 문제나 개인정보 침해가 발생할 수 있는 정보다.

Frontend에서는 Token, Password, 개인정보, 결제정보, Secret Key를 특히 주의해야 한다.

---

### [핵심]

- Sensitive Data
- Access Token
- Refresh Token
- Password
- Personal Information
- Payment Information
- Secret Key
- API Key
- console log
- localStorage
- sessionStorage
- Browser Exposure

---

### [실무]

민감정보 예:

```text
Access Token
Refresh Token
Password
Email
Phone Number
Address
Payment Key
Secret Key
Private API Key
```

금지 예:

```javascript
console.log("token:", accessToken);
console.log("password:", password);
localStorage.setItem("secretKey", secretKey);
```

주의:

- Token을 console.log로 출력하지 않는다.
- Password를 state나 log에 오래 남기지 않는다.
- Secret Key는 Frontend에 포함하지 않는다.
- localStorage는 XSS에 취약할 수 있다.
- sessionStorage도 완전한 보안 저장소가 아니다.
- 민감정보가 포함된 screenshot이나 로그 공유 금지
- 인증 저장 방식은 프로젝트 보안 정책을 따른다.

---

### [FAQ]

Q. Sensitive Data는 뭐야?
A. 노출되면 보안 문제나 개인정보 침해가 발생할 수 있는 정보다.

Q. Access Token을 console.log로 출력해도 돼?
A. 안 된다. Token은 민감정보다.

Q. Secret Key를 Frontend 코드에 넣어도 돼?
A. 절대 안 된다. Frontend 코드는 사용자에게 노출될 수 있다.

Q. localStorage는 안전한 저장소야?
A. XSS에 취약할 수 있으므로 민감정보 저장은 신중해야 한다.

---

# 8. Token Handling Basics

## 8.1 Token Handling Rules

### [개념]

Token Handling은 로그인 후 받은 Access Token을 API 요청에 포함하고, 만료나 인증 오류에 대응하는 Frontend 인증 기본 흐름이다.

JavaScript Foundation에서는 Token Handling의 기초와 보안 주의만 다룬다.

---

### [핵심]

- Token Handling
- Access Token
- Refresh Token
- Authorization Header
- Bearer Token
- 401 Unauthorized
- 403 Forbidden
- token expiration
- logout cleanup
- storage caution

---

### [실무]

인증 Header 생성:

```javascript
function createAuthHeaders(accessToken) {
  if (!accessToken) {
    return {};
  }

  return {
    Authorization: `Bearer ${accessToken}`,
  };
}
```

인증 요청:

```javascript
async function fetchMyProfile(accessToken) {
  const response = await fetch("/api/users/me", {
    headers: {
      ...createAuthHeaders(accessToken),
    },
  });

  if (response.status === 401) {
    throw new Error("Unauthorized");
  }

  if (!response.ok) {
    throw new Error("Profile request failed");
  }

  return await response.json();
}
```

로그아웃 정리 예:

```javascript
function clearAuthStorage() {
  localStorage.removeItem("accessToken");
  sessionStorage.removeItem("accessToken");
}
```

주의:

- Authorization Header 형식을 Backend와 일치시킨다.
- 401과 403을 구분한다.
- Token 만료 시 재로그인 또는 refresh flow를 고려한다.
- Token 저장 위치는 보안 정책을 따른다.
- Token 로그 출력 금지
- 로그아웃 시 저장소 정리 필요
- 인증 심화는 Authentication Frontend Flow 문서에서 다룬다.

---

### [FAQ]

Q. Token Handling이 뭐야?
A. 로그인 후 받은 Token을 API 요청에 포함하고 인증 오류에 대응하는 Frontend 흐름이다.

Q. Authorization Header 형식은 어떻게 작성해?
A. `Authorization: Bearer <accessToken>` 형식으로 작성한다.

Q. 401과 403은 어떻게 달라?
A. 401은 인증되지 않음, 403은 인증되었지만 권한이 없음이다.

Q. Token Handling 심화는 이 문서에서 다뤄?
A. 아니다. 이 문서는 기초만 다루고 심화는 Authentication Frontend Flow 문서에서 다룬다.

---

# 9. Input Validation and Output Handling

## 9.1 Input Validation Rules

### [개념]

Input Validation은 사용자 입력값이 필요한 조건을 만족하는지 확인하는 과정이다.

Frontend Input Validation은 사용자 경험을 위한 1차 방어이며, Backend Validation을 대체하지 않는다.

---

### [핵심]

- Input Validation
- required
- trim
- min length
- max length
- number range
- email format
- file validation
- frontend validation
- backend validation
- user feedback

---

### [실무]

검색어 검증:

```javascript
function validateKeyword(keyword) {
  return keyword.trim().length > 0;
}
```

리뷰 검증:

```javascript
function validateReview({ rating, content }) {
  if (rating < 1 || rating > 5) {
    return "평점은 1점 이상 5점 이하로 입력해야 합니다.";
  }

  if (content.trim().length === 0) {
    return "리뷰 내용을 입력하세요.";
  }

  return null;
}
```

파일 검증:

```javascript
function validateImageFile(file) {
  if (!file) {
    return "이미지를 선택하세요.";
  }

  if (!file.type.startsWith("image/")) {
    return "이미지 파일만 업로드할 수 있습니다.";
  }

  return null;
}
```

주의:

- 입력값은 trim 처리한다.
- number input은 Number 변환 후 검증한다.
- 파일 크기와 타입을 검증한다.
- Frontend 검증을 우회할 수 있으므로 Backend 검증이 필수다.
- 사용자 메시지는 수정 방법을 알려줘야 한다.

---

### [FAQ]

Q. Input Validation은 뭐야?
A. 사용자 입력값이 필요한 조건을 만족하는지 확인하는 과정이다.

Q. Frontend Validation은 왜 필요해?
A. 사용자가 빠르게 오류를 확인하고 수정할 수 있도록 돕기 위해 필요하다.

Q. Frontend Validation만 믿어도 돼?
A. 안 된다. 사용자가 우회할 수 있으므로 Backend Validation이 필수다.

Q. 파일 업로드 검증은 무엇을 확인해야 해?
A. 파일 존재 여부, 타입, 크기, 확장자 정책을 확인해야 한다.

---

## 9.2 Output Handling Rules

### [개념]

Output Handling은 사용자 입력이나 API 응답을 화면에 표시할 때 안전하게 처리하는 과정이다.

HTML로 해석될 수 있는 출력은 XSS 위험을 만들 수 있다.

---

### [핵심]

- Output Handling
- safe rendering
- textContent
- innerHTML caution
- escaping
- XSS prevention
- API response display
- user input display
- fallback value

---

### [실무]

안전한 텍스트 출력:

```javascript
function renderMessage(message) {
  const messageElement = document.querySelector(".message");

  if (!messageElement) {
    return;
  }

  messageElement.textContent = message ?? "";
}
```

API 응답 출력:

```javascript
function renderFestivalTitle(festival) {
  const titleElement = document.querySelector(".festival-title");

  if (!titleElement) {
    return;
  }

  titleElement.textContent = festival?.title ?? "제목 없음";
}
```

주의:

- 사용자 입력은 textContent로 출력한다.
- API 응답도 신뢰하지 않는다.
- innerHTML 사용은 제한한다.
- HTML 렌더링이 필요하면 sanitize 정책 필요
- fallback value를 지정해 undefined 표시를 막는다.
- React에서도 dangerouslySetInnerHTML은 보안 검토가 필요하다.

---

### [FAQ]

Q. Output Handling이 뭐야?
A. 사용자 입력이나 API 응답을 화면에 표시할 때 안전하게 처리하는 과정이다.

Q. 사용자 입력 출력에는 무엇을 써야 해?
A. textContent를 우선 사용한다.

Q. API 응답은 안전하다고 봐도 돼?
A. 아니다. API 응답도 안전하게 출력해야 한다.

Q. undefined가 화면에 보이면 어떻게 해야 해?
A. nullish coalescing으로 fallback value를 지정한다.

---

# 10. Troubleshooting

## 10.1 Troubleshooting Concept

### [개념]

Troubleshooting은 문제가 발생했을 때 증상, 원인 후보, 확인 방법, 수정 방향을 체계적으로 찾는 과정이다.

Frontend Troubleshooting은 Console, Network, Elements, Application, Sources를 함께 사용해야 한다.

---

### [핵심]

- Troubleshooting
- Console
- Network
- Elements
- Application
- Sources
- Error Message
- Reproduce
- Hypothesis
- Verify
- Fix
- Retest

---

### [실무]

기본 Troubleshooting Flow:

```text
Reproduce Problem
→ Read Error Message
→ Check Console
→ Check Network
→ Check Elements
→ Check Storage
→ Trace Source
→ Fix
→ Retest
```

원칙:

- 추측보다 증거를 우선한다.
- 오류 메시지를 끝까지 읽는다.
- Network 탭에서 실제 요청을 확인한다.
- DOM 문제는 Elements 탭에서 확인한다.
- 인증 문제는 Header와 Storage를 함께 확인한다.
- 수정 후 같은 시나리오를 다시 테스트한다.

주의:

- Console만 보고 결론 내리지 않는다.
- 요청이 없는 문제와 요청 실패 문제를 구분한다.
- 사용자 입력, API 응답, 상태 업데이트 흐름을 순서대로 추적한다.
- 에러를 임시로 숨기는 방식으로 해결하지 않는다.

---

### [FAQ]

Q. Troubleshooting이 뭐야?
A. 문제가 발생했을 때 증거를 기반으로 원인을 찾고 수정하는 과정이다.

Q. Frontend Troubleshooting에서 무엇을 먼저 봐?
A. Console 오류와 Network 요청 발생 여부를 먼저 확인한다.

Q. 추측으로 고치면 안 되는 이유는?
A. 실제 원인을 놓치고 다른 오류를 만들 수 있기 때문이다.

Q. 수정 후에는 무엇을 해야 해?
A. 같은 시나리오를 다시 실행해 문제가 해결되었는지 확인한다.

---

# 11. Symptom Based Troubleshooting

## 11.1 API Request Not Sent

### [개념]

API Request Not Sent는 사용자가 버튼 클릭이나 Form Submit을 했지만 Network 탭에 요청이 나타나지 않는 문제다.

이 경우 API 자체보다 Event Handler와 함수 호출 흐름을 먼저 확인해야 한다.

---

### [핵심]

- API Request Not Sent
- Event Handler
- addEventListener
- selector null
- preventDefault
- function call
- button type
- form submit
- Network Tab

---

### [실무]

확인 Flow:

```text
User Action
→ Event Listener Registered?
→ Event Handler Runs?
→ Validation Blocks?
→ API Function Called?
→ Network Request Appears?
```

확인 코드:

```javascript
function handleSubmit(event) {
  event.preventDefault();

  console.log("submit handler called");

  searchFestivals();
}
```

원인 후보:

- DOM selector가 null
- addEventListener 등록 실패
- button type 문제
- Form submit 새로고침
- Validation에서 return
- API 함수 호출 누락
- Event Handler 이름 오타

주의:

- Network 요청이 없으면 Backend 문제가 아닐 가능성이 높다.
- Event Handler 진입 여부를 먼저 확인한다.
- Console log는 임시로 사용하고 민감정보 출력 금지
- DOM 요소 존재 여부를 Elements에서 확인한다.

---

### [FAQ]

Q. 버튼을 눌렀는데 API 요청이 없으면 무엇부터 봐?
A. Event Handler가 실행되는지 확인한다.

Q. Network 요청이 없으면 Backend 문제야?
A. 반드시 그렇지 않다. Frontend Event 연결이나 함수 호출 문제일 수 있다.

Q. selector가 null이면 어떻게 돼?
A. addEventListener 등록이 실패하거나 DOM 조작 오류가 발생할 수 있다.

---

## 11.2 API Request Failed

### [개념]

API Request Failed는 Network 요청은 발생했지만 서버가 오류 status를 반환하거나 CORS / Network Error가 발생한 상태다.

이 경우 Network 탭에서 URL, Method, Header, Payload, Status, Response를 확인한다.

---

### [핵심]

- API Request Failed
- Status Code
- 400
- 401
- 403
- 404
- 500
- CORS
- Payload
- Headers
- Response Body

---

### [실무]

확인 Flow:

```text
Network Request
→ URL
→ Method
→ Query Parameters
→ Request Headers
→ Payload
→ Status Code
→ Response Body
→ Frontend Error Handling
```

상태별 원인:

| Status | 원인 후보                                         |
| ------ | ------------------------------------------------- |
| 400    | Request Body, Query Parameter, Validation         |
| 401    | Token 없음, Token 만료, Authorization Header 누락 |
| 403    | 권한 없음, Role 부족                              |
| 404    | URL 오타, Backend Mapping 없음                    |
| 500    | Backend 예외, 서버 내부 오류                      |
| CORS   | Backend CORS 설정, Origin 불일치                  |

주의:

- 400은 Payload와 DTO 필드명 확인
- 401은 Authorization Header 확인
- 403은 로그인은 되었지만 권한이 없을 수 있음
- 404는 API prefix와 path variable 확인
- 500은 요청 조건과 Backend 로그 확인 필요
- CORS는 Browser 정책이므로 Postman과 다를 수 있다.

---

### [FAQ]

Q. API 요청이 실패하면 무엇을 확인해?
A. Network 탭에서 URL, Method, Headers, Payload, Status Code, Response Body를 확인한다.

Q. 400 오류는 무엇을 의심해?
A. Request Body 필드명, 타입, Query Parameter, Validation 오류를 의심한다.

Q. 401 오류는 무엇을 의심해?
A. Authorization Header 누락, Token 없음, Token 만료를 의심한다.

Q. 404 오류는 무엇을 의심해?
A. 요청 URL, API prefix, Backend Mapping, path variable을 확인한다.

---

## 11.3 UI Not Updating

### [개념]

UI Not Updating은 데이터는 변경되었거나 요청은 성공했지만 화면이 바뀌지 않는 문제다.

DOM 선택, 렌더 함수 호출, 상태 변경, CSS class, async order를 확인해야 한다.

---

### [핵심]

- UI Not Updating
- render function
- DOM selection
- data exists
- classList
- textContent
- CSS hidden
- async order
- state update
- React readiness

---

### [실무]

확인 Flow:

```text
Data Exists?
→ Render Function Called?
→ DOM Element Selected?
→ DOM Update Executed?
→ Elements Tab Shows Change?
→ CSS Visible?
```

확인 코드:

```javascript
console.log("items:", items);
console.log("listElement:", listElement);
```

원인 후보:

- 데이터가 빈 배열
- normalize 경로 오류
- render 함수 미호출
- selector 오류
- DOM 요소 null
- textContent 초기화 순서 문제
- CSS hidden 상태
- async 응답 이전에 render 호출
- React State 직접 변경

주의:

- API 성공과 UI 성공은 다르다.
- Network Response와 render input을 비교한다.
- Elements 탭에서 실제 DOM 변화를 확인한다.
- CSS 문제와 JavaScript 문제를 구분한다.

---

### [FAQ]

Q. API는 성공했는데 화면이 안 바뀌면 무엇을 확인해?
A. 응답 데이터, normalize 결과, render 함수 호출, DOM 선택 성공 여부를 확인한다.

Q. DOM은 바뀌었는데 화면에 안 보이면 무엇을 봐?
A. CSS display, visibility, opacity, class 충돌, computed style을 확인한다.

Q. render 함수가 호출되지 않으면 무엇을 의심해?
A. Event Handler, async await 흐름, 조건문 return, error catch 흐름을 확인한다.

---

## 11.4 Undefined and Null Error

### [개념]

Undefined and Null Error는 존재하지 않는 값에서 property나 method를 읽으려 할 때 발생한다.

대표 오류는 `Cannot read properties of undefined` 또는 `Cannot read properties of null`이다.

---

### [핵심]

- Undefined Error
- Null Error
- Cannot read properties
- optional chaining
- null check
- Array.isArray
- default value
- API response
- DOM selection

---

### [실무]

문제 예:

```javascript
const title = response.data.content[0].title;
```

개선:

```javascript
const title = response?.data?.content?.[0]?.title ?? "제목 없음";
```

DOM 문제 예:

```javascript
document.querySelector(".title").textContent = "Festival";
```

개선:

```javascript
const titleElement = document.querySelector(".title");

if (titleElement) {
  titleElement.textContent = "Festival";
}
```

확인 Flow:

```text
Error Line
→ Access Target
→ Value Exists?
→ API Response Shape?
→ DOM Exists?
→ Guard Needed?
→ Default Value Needed?
```

주의:

- optional chaining은 오류를 줄이지만 원인 분석도 필요하다.
- API 응답 구조는 Network 탭에서 확인한다.
- DOM 요소는 Elements 탭에서 확인한다.
- 배열 여부는 Array.isArray로 확인한다.
- 기본값을 지정해 화면에 undefined가 보이지 않게 한다.

---

### [FAQ]

Q. Cannot read properties of undefined는 왜 발생해?
A. undefined 값에서 property나 method를 읽으려 했기 때문이다.

Q. Cannot read properties of null은 왜 발생해?
A. null 값에서 property나 method를 읽으려 했기 때문이다.

Q. 해결 방법은 뭐야?
A. optional chaining, null check, Array.isArray, default value를 적용한다.

Q. DOM 관련 null 오류는 어떻게 확인해?
A. selector가 실제 HTML 요소와 일치하는지 Elements 탭에서 확인한다.

---

# 12. Review Agent Checklist

## 12.1 JavaScript Code Review Checklist

### [개념]

Review Agent Checklist는 JavaScript 코드 생성 결과를 검토하기 위한 기준이다.

Review Agent는 문법 오류만 보는 것이 아니라 실행 흐름, 비동기 처리, API 연동, 보안, 유지보수성을 함께 검토해야 한다.

---

### [핵심]

Review Categories:

- Syntax
- Variable
- Function
- Array / Object
- DOM
- Event
- Form
- Async
- Fetch
- Error Handling
- Module
- Security
- Debugging
- React Readiness

---

### [실무]

기본 Review Checklist:

```text
1. const / let 사용 기준이 맞는가?
2. var를 사용하지 않았는가?
3. == 대신 ===를 사용하는가?
4. null / undefined 방어가 있는가?
5. 배열 여부를 확인하는가?
6. map callback return이 있는가?
7. sort / splice 원본 변경을 인지하는가?
8. Function 책임이 과도하지 않은가?
9. Event Handler에 로직이 과도하게 몰려 있지 않은가?
10. Form submit에서 preventDefault가 있는가?
11. input value 타입 변환이 필요한가?
12. async function 결과를 await하는가?
13. response.ok를 확인하는가?
14. response.json을 await하는가?
15. try / catch / finally가 적절한가?
16. loading 상태가 실패 시에도 해제되는가?
17. Error Message와 Developer Log가 구분되는가?
18. innerHTML에 사용자 입력을 넣지 않는가?
19. Token이나 Password를 log로 출력하지 않는가?
20. API / UI / Utility Module이 분리되어 있는가?
```

주의:

- Review 결과는 수정 가능한 항목으로 작성한다.
- 보안 문제는 우선순위를 높게 둔다.
- 비동기 오류는 재현 흐름을 함께 확인한다.
- API 오류는 Network 증거를 기준으로 판단한다.
- 코드 스타일 문제와 실제 버그 위험을 구분한다.

---

### [FAQ]

Q. Review Agent는 JavaScript 코드에서 무엇을 봐야 해?
A. 문법, 변수, 함수, 배열, DOM, Event, Async, Fetch, Error Handling, Security, Module 분리를 함께 봐야 한다.

Q. 가장 우선순위가 높은 Review 항목은 뭐야?
A. 보안 문제, 비동기 에러 처리, API 응답 처리, null 방어, 민감정보 로그 출력 여부다.

Q. Review 결과는 어떻게 작성해야 해?
A. 문제 위치, 문제 이유, 수정 방향, 개선 예시를 포함하는 것이 좋다.

Q. 스타일 문제와 버그 위험은 구분해야 해?
A. 구분해야 한다. 버그와 보안 위험을 더 높은 우선순위로 처리한다.

---

## 12.2 Security Review Checklist

### [개념]

Security Review Checklist는 Frontend JavaScript 코드에서 보안상 위험한 패턴을 검출하기 위한 기준이다.

Frontend Security Review는 XSS, 민감정보 노출, Token 처리, 입력 검증, 외부 URL, 로그 보안을 우선 확인한다.

---

### [핵심]

Security Review Items:

- XSS Risk
- innerHTML
- dangerouslySetInnerHTML
- Token Log
- Password Log
- Secret Key Exposure
- localStorage Risk
- Input Validation
- Output Handling
- Authorization Header
- CORS Misunderstanding

---

### [실무]

Security Review Checklist:

```text
1. 사용자 입력을 innerHTML에 직접 삽입하지 않는가?
2. API 응답 HTML을 신뢰하지 않는가?
3. textContent 또는 안전한 렌더링 방식을 사용하는가?
4. Access Token을 console.log로 출력하지 않는가?
5. Password를 console.log로 출력하지 않는가?
6. Secret Key를 Frontend 코드에 포함하지 않았는가?
7. localStorage 저장 값에 민감정보가 포함되어 있는가?
8. 로그아웃 시 인증 저장소를 정리하는가?
9. Frontend Validation만으로 권한을 판단하지 않는가?
10. Backend Validation과 Authorization이 필요함을 전제하는가?
11. URL parameter에 민감정보를 넣지 않는가?
12. Error Message에 민감정보를 포함하지 않는가?
13. 외부 URL 이동이나 파일 업로드 검증을 수행하는가?
14. CORS를 보안 우회 수단으로 오해하지 않는가?
```

위험 코드:

```javascript
container.innerHTML = userInput;
console.log(accessToken);
const secretKey = "private-secret-key";
```

개선 방향:

```javascript
container.textContent = userInput;
```

주의:

- Frontend에서 숨긴 값은 진짜 Secret이 아니다.
- Token 저장 방식은 프로젝트 보안 정책을 따른다.
- 사용자가 조작할 수 있는 값은 신뢰하지 않는다.
- 보안 문제는 기능 정상 동작 여부와 별개로 검토한다.

---

### [FAQ]

Q. Security Review에서 가장 먼저 봐야 하는 것은 뭐야?
A. innerHTML 사용자 입력 삽입, Token 로그 출력, Secret Key 하드코딩, Frontend-only 권한 검증이다.

Q. Frontend 코드에 숨겨둔 Secret은 안전해?
A. 아니다. Frontend 코드는 사용자에게 노출될 수 있다.

Q. 사용자 입력을 출력할 때 가장 안전한 기본 방식은 뭐야?
A. textContent를 사용하는 것이다.

Q. 보안 문제는 기능이 정상 동작하면 넘어가도 돼?
A. 안 된다. 기능이 정상이어도 보안 취약점은 반드시 수정해야 한다.

---

# 13. Frontend Agent Generation Rules

## 13.1 Code Generation Rules

### [개념]

Frontend Agent Generation Rules는 Frontend Agent가 JavaScript 코드를 생성할 때 따라야 하는 기준이다.

Agent는 작동하는 코드뿐 아니라 검토 가능하고 안전한 코드를 생성해야 한다.

---

### [핵심]

- Frontend Agent
- Code Generation
- Safe Default
- Practical Logic
- Function Separation
- Error Handling
- Security
- API Integration
- Review Ready Code
- React Readiness

---

### [실무]

생성 기준:

```text
1. const 우선 사용
2. let은 재할당 필요 시에만 사용
3. var 사용 금지
4. 함수는 단일 책임으로 분리
5. 사용자 입력은 trim / validate
6. API 요청은 response.ok 확인
7. response.json은 await
8. API 응답은 normalize function으로 가공
9. null / undefined 기본값 처리
10. loading / error 상태 포함
11. 사용자 메시지와 개발자 로그 분리
12. innerHTML 사용 금지 또는 제한
13. 민감정보 log 금지
14. Module 분리 가능성 고려
15. Review Agent가 검토하기 쉬운 구조로 작성
```

권장 코드 흐름:

```text
Validation Function
→ API Function
→ Normalize Function
→ Render Function
→ Event Handler
```

주의:

- 한 번에 거대한 함수를 만들지 않는다.
- 임시 console.log를 남기지 않는다.
- 예외 처리를 생략하지 않는다.
- Browser API와 React 방식을 혼동하지 않는다.
- 프로젝트 API 스펙을 모르면 합리적인 placeholder를 명확히 사용한다.

---

### [FAQ]

Q. Frontend Agent는 어떤 JavaScript 코드를 생성해야 해?
A. 작동할 뿐 아니라 역할이 분리되고 에러 처리와 보안 기준이 포함된 코드를 생성해야 한다.

Q. Frontend Agent가 기본으로 포함해야 하는 것은 뭐야?
A. 입력 검증, API 에러 처리, loading / error 상태, null 방어, 안전한 출력이다.

Q. Frontend Agent가 피해야 하는 코드는 뭐야?
A. 거대한 단일 함수, innerHTML 사용자 입력 삽입, await 누락, response.ok 누락, 민감정보 로그 출력이다.

Q. 생성 코드는 Review Agent를 고려해야 해?
A. 그래야 한다. Review 가능한 구조로 작성해야 오류 검출과 수정이 쉽다.

---

# 14. React Readiness

## 14.1 JavaScript to React Connection

### [개념]

React Readiness는 JavaScript Foundation에서 배운 문법과 패턴이 React 학습과 코드 생성으로 이어질 수 있게 준비하는 기준이다.

React는 JavaScript 위에서 동작하므로 Function, Array, Object, Event, Async, Module, Error Handling 이해가 필수다.

---

### [핵심]

- React Readiness
- Function Component
- Props
- State
- Event Handler
- Conditional Rendering
- List Rendering
- useEffect
- Data Fetching
- Module
- Immutability
- Closure

---

### [실무]

JavaScript Foundation과 React 연결:

| JavaScript Foundation | React 연결                        |
| --------------------- | --------------------------------- |
| Function              | Function Component, Event Handler |
| Array.map             | List Rendering                    |
| Object Spread         | State Update                      |
| Destructuring         | Props, Hook Return                |
| Event Handling        | React Synthetic Event             |
| async / await         | Data Fetching                     |
| Loading / Error State | Conditional Rendering             |
| Module                | Component / Hook / API 분리       |
| Closure               | Hook dependency, stale state      |
| Security              | dangerouslySetInnerHTML 주의      |

예:

```javascript
const festivalCards = festivals.map((festival) => ({
  id: festival.id,
  title: festival.title ?? "제목 없음",
}));
```

React에서 연결:

```javascript
const items = festivals.map((festival) => (
  <FestivalCard key={festival.id} festival={festival} />
));
```

주의:

- React에서는 DOM 직접 조작보다 state 기반 렌더링을 우선한다.
- 배열과 객체 state는 immutable update가 중요하다.
- Event Handler는 JavaScript Function 개념을 기반으로 한다.
- useEffect의 비동기 처리에는 async / await와 cleanup 이해가 필요하다.
- React 심화는 React Core 문서에서 다룬다.

---

### [FAQ]

Q. JavaScript Foundation은 React와 어떻게 연결돼?
A. React Component, State, Event, List Rendering, Data Fetching은 모두 JavaScript 개념 위에서 동작한다.

Q. React를 배우기 전에 꼭 알아야 할 JavaScript는 뭐야?
A. Function, Array, Object, Destructuring, Spread, Event, async / await, Module, Closure가 중요하다.

Q. React에서도 DOM을 직접 조작해?
A. 대부분 직접 조작하지 않고 state와 props로 UI를 갱신한다.

Q. React Hook과 Closure는 관련 있어?
A. 관련 있다. Hook dependency와 stale state 문제를 이해하려면 Closure 개념이 필요하다.

---

# 15. JavaScript Foundation Final Troubleshooting Map

## 15.1 Troubleshooting Map

### [개념]

Troubleshooting Map은 JavaScript Foundation 전체 문서에서 다룬 오류 원인을 증상별로 연결한 참조표다.

Agent는 오류 증상에 따라 관련 Part를 검색하고 수정 방향을 결정해야 한다.

---

### [핵심]

- Troubleshooting Map
- Symptom
- Cause
- Related Part
- Debugging
- Review
- Fix Direction
- Retrieval Aid

---

### [실무]

증상별 참조:

| 증상                  | 원인 후보                           | 관련 Part      |
| --------------------- | ----------------------------------- | -------------- |
| 변수 값이 예상과 다름 | Scope, reassignment, var            | Part02, Part04 |
| 조건문이 이상함       | Truthy / Falsy, ==, Type Conversion | Part02, Part03 |
| 배열 map 오류         | 배열 아님, return 누락              | Part05         |
| 화면 요소 null 오류   | selector 오류, DOM 로드 전 접근     | Part06         |
| Form submit 새로고침  | preventDefault 누락                 | Part06         |
| API 응답 undefined    | await 누락, 응답 구조 오류          | Part07, Part08 |
| loading이 안 끝남     | finally 누락                        | Part07, Part09 |
| 401 / 403 오류        | Authorization Header, Token, 권한   | Part08, Part10 |
| import 오류           | export / import 불일치              | Part09         |
| XSS 위험              | innerHTML 사용자 입력 삽입          | Part06, Part10 |
| UI가 안 바뀜          | render 미호출, DOM 선택 실패, CSS   | Part06, Part09 |
| 검색 결과 순서 꼬임   | Race Condition                      | Part07         |

Debugging 기준:

```text
Symptom
→ Related Part Search
→ Root Cause Candidate
→ Console / Network / Elements Evidence
→ Fix
→ Retest
```

주의:

- 오류 증상을 보고 바로 수정하지 않는다.
- 관련 Part를 검색해 원인 후보를 좁힌다.
- Console, Network, Elements 증거를 확인한다.
- 수정 후 동일 시나리오를 재검증한다.

---

### [FAQ]

Q. Troubleshooting Map은 왜 필요해?
A. 오류 증상과 관련 문서를 빠르게 연결해 Agent Retrieval 정확도를 높이기 위해 필요하다.

Q. API 응답 undefined는 어떤 Part를 봐야 해?
A. Part07 Async와 Part08 Fetch / API Response를 우선 확인한다.

Q. XSS 위험은 어떤 Part를 봐야 해?
A. Part06 DOM innerHTML과 Part10 Security / XSS를 확인한다.

Q. import 오류는 어떤 Part를 봐야 해?
A. Part09 Module / Import Export Error를 확인한다.

---

# 16. JavaScript Foundation Completion Checklist

## 16.1 Final Quality Checklist

### [개념]

JavaScript Foundation Completion Checklist는 Part01부터 Part10까지의 문서가 JavaScript Foundation RAG 문서 세트로 완성되었는지 검수하는 기준이다.

이 Checklist는 사람용 학습 완료가 아니라 Agent Retrieval, Code Generation, Review, Debugging 기준 충족 여부를 확인한다.

---

### [핵심]

완성 기준:

- Basic Syntax
- Variable and Data Type
- Operator and Condition
- Function and Scope
- Array and Object
- DOM and Event
- Async and Promise
- Fetch and JSON
- Module and Debugging
- Security and Review
- Retrieval Queries
- FAQ Coverage
- Practical Examples

---

### [실무]

Part별 검수:

```text
Part01 Basic Syntax
→ Statement, Expression, Semicolon, Comment, Basic Example

Part02 Variable and Data Type
→ const, let, var, Scope, Type, null, undefined

Part03 Operator Condition Loop
→ ===, ??, ?., Guard Clause, Array Method

Part04 Function Scope Closure
→ Function, Arrow, Callback, Pure Function, Closure

Part05 Array Object
→ map, filter, find, reduce, Spread, Destructuring, Copy

Part06 DOM Event Form
→ DOM Selection, Event, Form, Validation, Loading

Part07 Async Promise AsyncAwait
→ Promise, async / await, try catch, Race Condition

Part08 Fetch JSON API Response
→ Fetch, Method, Header, JSON, Normalize, Status

Part09 Module Error Debugging
→ export / import, Error Handling, DevTools, ESLint

Part10 Practical Security Review
→ Practical Pattern, Security, Troubleshooting, Review Checklist
```

최종 품질 기준:

- [ ] 각 Part에 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`가 포함되었는가?
- [ ] 각 Part에 Retrieval Queries가 포함되었는가?
- [ ] Frontend Agent가 코드 생성에 사용할 수 있는 예제가 충분한가?
- [ ] Review Agent가 실수 패턴을 검출할 수 있는가?
- [ ] DOM / Event / Fetch / Async 보안 기준이 포함되었는가?
- [ ] API 연동과 React 전환 준비가 가능한가?
- [ ] FAQ가 실제 검색 질문 형태로 작성되었는가?
- [ ] 용어가 전체 Part에서 일관되는가?
- [ ] 오타와 중복이 최소화되었는가?
- [ ] 치명적인 보안 누락이 없는가?

---

### [FAQ]

Q. JavaScript Foundation은 Part10으로 완료돼?
A. 1차 Foundation 기준으로는 Part01부터 Part10까지 작성하면 완료로 볼 수 있다.

Q. Part10의 역할은 뭐야?
A. Practical Logic, Security, Troubleshooting, Review Checklist를 통합해 JavaScript Foundation을 마무리하는 역할이다.

Q. JavaScript Foundation 다음 문서는 뭐가 좋아?
A. TypeScript Foundation 또는 React Core로 이어지는 것이 좋다.

Q. Completed 처리 전에 무엇을 확인해야 해?
A. 각 Part의 구조, FAQ, Retrieval Queries, 실무 예제, 보안 기준, 파일 간 연계를 검수해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Practical Logic이 뭐야?
A. JavaScript 문법과 Browser API를 실제 화면 기능으로 연결하는 실무 로직이다.

Q. JavaScript Foundation의 최종 목표는 뭐야?
A. Frontend Agent가 안전한 화면 로직을 생성하고 Review Agent가 오류와 보안 문제를 검출할 수 있게 하는 것이다.

Q. Practical Logic에서 가장 중요한 기준은 뭐야?
A. 역할 분리, null 방어, 비동기 에러 처리, 보안, 사용자 상태 표시다.

Q. UI State Pattern이 뭐야?
A. 화면 상태를 loading, error, empty, success로 구분해 처리하는 방식이다.

Q. loading과 empty 중 무엇을 먼저 판단해?
A. loading을 먼저 판단한다. 요청 중에는 아직 데이터 없음 상태로 확정할 수 없다.

Q. error와 empty는 어떻게 달라?
A. error는 요청 실패이고 empty는 요청은 성공했지만 표시할 데이터가 없는 상태다.

Q. Request Status Object는 뭐야?
A. API 요청 상태를 loading, error, data 같은 값으로 묶어 관리하는 객체다.

Q. Search Feature의 기본 흐름은 뭐야?
A. 입력값 정리, 검증, query parameter 생성, API 요청, 응답 정규화, 결과 렌더링 순서다.

Q. 검색어는 왜 trim 처리해?
A. 공백만 입력된 값을 유효한 검색어로 처리하지 않기 위해서다.

Q. 검색 기능에서 debounce가 필요한 이유는?
A. 입력마다 API 요청이 발생하는 것을 줄이기 위해서다.

Q. Pagination이 뭐야?
A. 목록 데이터를 여러 페이지로 나누어 조회하고 표시하는 방식이다.

Q. 새 검색 조건에서는 기존 목록을 어떻게 해야 해?
A. 기존 목록을 초기화하고 첫 페이지부터 다시 조회하는 것이 일반적이다.

Q. 더보기에서는 목록을 어떻게 처리해?
A. 기존 목록 뒤에 다음 페이지 items를 append한다.

Q. hasNext는 왜 필요해?
A. 다음 페이지 요청 가능 여부를 판단하기 위해 필요하다.

Q. Frontend Security가 뭐야?
A. Browser에서 실행되는 JavaScript가 입력, 출력, 인증 정보, DOM 조작을 안전하게 처리하도록 하는 기준이다.

Q. Frontend 코드에 Secret Key를 넣어도 돼?
A. 안 된다. Frontend 코드는 사용자에게 노출될 수 있으므로 Secret을 넣으면 안 된다.

Q. Frontend Validation만으로 보안 검증이 충분해?
A. 아니다. Frontend Validation은 UX용이고 Backend Validation과 권한 검증이 필수다.

Q. XSS가 뭐야?
A. 악성 script가 웹 페이지에 삽입되어 사용자 브라우저에서 실행되는 취약점이다.

Q. innerHTML이 왜 위험해?
A. 문자열을 HTML로 파싱하기 때문에 악성 script가 실행될 수 있다.

Q. 사용자 입력을 출력할 때 무엇을 우선 사용해?
A. textContent를 우선 사용한다.

Q. API 응답은 신뢰해도 돼?
A. 아니다. API 응답도 악의적이거나 오염될 수 있으므로 안전하게 처리해야 한다.

Q. Sensitive Data는 뭐야?
A. 노출되면 보안 문제나 개인정보 침해가 발생할 수 있는 정보다.

Q. Access Token을 console.log로 출력해도 돼?
A. 안 된다. Token은 민감정보다.

Q. Secret Key를 Frontend 코드에 넣어도 돼?
A. 절대 안 된다. Frontend 코드는 사용자에게 노출될 수 있다.

Q. localStorage는 안전한 저장소야?
A. XSS에 취약할 수 있으므로 민감정보 저장은 신중해야 한다.

Q. Token Handling이 뭐야?
A. 로그인 후 받은 Token을 API 요청에 포함하고 인증 오류에 대응하는 Frontend 흐름이다.

Q. Authorization Header 형식은 어떻게 작성해?
A. Authorization: Bearer accessToken 형식으로 작성한다.

Q. 401과 403은 어떻게 달라?
A. 401은 인증되지 않음, 403은 인증되었지만 권한이 없음이다.

Q. Input Validation은 뭐야?
A. 사용자 입력값이 필요한 조건을 만족하는지 확인하는 과정이다.

Q. Frontend Validation만 믿어도 돼?
A. 안 된다. 사용자가 우회할 수 있으므로 Backend Validation이 필수다.

Q. Output Handling이 뭐야?
A. 사용자 입력이나 API 응답을 화면에 표시할 때 안전하게 처리하는 과정이다.

Q. 사용자 입력 출력에는 무엇을 써야 해?
A. textContent를 우선 사용한다.

Q. undefined가 화면에 보이면 어떻게 해야 해?
A. nullish coalescing으로 fallback value를 지정한다.

Q. Troubleshooting이 뭐야?
A. 문제가 발생했을 때 증거를 기반으로 원인을 찾고 수정하는 과정이다.

Q. Frontend Troubleshooting에서 무엇을 먼저 봐?
A. Console 오류와 Network 요청 발생 여부를 먼저 확인한다.

Q. 버튼을 눌렀는데 API 요청이 없으면 무엇부터 봐?
A. Event Handler가 실행되는지 확인한다.

Q. Network 요청이 없으면 Backend 문제야?
A. 반드시 그렇지 않다. Frontend Event 연결이나 함수 호출 문제일 수 있다.

Q. API 요청이 실패하면 무엇을 확인해?
A. Network 탭에서 URL, Method, Headers, Payload, Status Code, Response Body를 확인한다.

Q. 400 오류는 무엇을 의심해?
A. Request Body 필드명, 타입, Query Parameter, Validation 오류를 의심한다.

Q. 401 오류는 무엇을 의심해?
A. Authorization Header 누락, Token 없음, Token 만료를 의심한다.

Q. API는 성공했는데 화면이 안 바뀌면 무엇을 확인해?
A. 응답 데이터, normalize 결과, render 함수 호출, DOM 선택 성공 여부를 확인한다.

Q. Cannot read properties of undefined는 왜 발생해?
A. undefined 값에서 property나 method를 읽으려 했기 때문이다.

Q. 해결 방법은 뭐야?
A. optional chaining, null check, Array.isArray, default value를 적용한다.

Q. Review Agent는 JavaScript 코드에서 무엇을 봐야 해?
A. 문법, 변수, 함수, 배열, DOM, Event, Async, Fetch, Error Handling, Security, Module 분리를 함께 봐야 한다.

Q. 가장 우선순위가 높은 Review 항목은 뭐야?
A. 보안 문제, 비동기 에러 처리, API 응답 처리, null 방어, 민감정보 로그 출력 여부다.

Q. Security Review에서 가장 먼저 봐야 하는 것은 뭐야?
A. innerHTML 사용자 입력 삽입, Token 로그 출력, Secret Key 하드코딩, Frontend-only 권한 검증이다.

Q. Frontend Agent는 어떤 JavaScript 코드를 생성해야 해?
A. 작동할 뿐 아니라 역할이 분리되고 에러 처리와 보안 기준이 포함된 코드를 생성해야 한다.

Q. Frontend Agent가 기본으로 포함해야 하는 것은 뭐야?
A. 입력 검증, API 에러 처리, loading / error 상태, null 방어, 안전한 출력이다.

Q. Frontend Agent가 피해야 하는 코드는 뭐야?
A. 거대한 단일 함수, innerHTML 사용자 입력 삽입, await 누락, response.ok 누락, 민감정보 로그 출력이다.

Q. JavaScript Foundation은 React와 어떻게 연결돼?
A. React Component, State, Event, List Rendering, Data Fetching은 모두 JavaScript 개념 위에서 동작한다.

Q. React를 배우기 전에 꼭 알아야 할 JavaScript는 뭐야?
A. Function, Array, Object, Destructuring, Spread, Event, async / await, Module, Closure가 중요하다.

Q. React에서도 DOM을 직접 조작해?
A. 대부분 직접 조작하지 않고 state와 props로 UI를 갱신한다.

Q. Troubleshooting Map은 왜 필요해?
A. 오류 증상과 관련 문서를 빠르게 연결해 Agent Retrieval 정확도를 높이기 위해 필요하다.

Q. API 응답 undefined는 어떤 Part를 봐야 해?
A. Part07 Async와 Part08 Fetch / API Response를 우선 확인한다.

Q. XSS 위험은 어떤 Part를 봐야 해?
A. Part06 DOM innerHTML과 Part10 Security / XSS를 확인한다.

Q. import 오류는 어떤 Part를 봐야 해?
A. Part09 Module / Import Export Error를 확인한다.

Q. JavaScript Foundation은 Part10으로 완료돼?
A. 1차 Foundation 기준으로는 Part01부터 Part10까지 작성하면 완료로 볼 수 있다.

Q. JavaScript Foundation 다음 문서는 뭐가 좋아?
A. TypeScript Foundation 또는 React Core로 이어지는 것이 좋다.

Q. Completed 처리 전에 무엇을 확인해야 해?
A. 각 Part의 구조, FAQ, Retrieval Queries, 실무 예제, 보안 기준, 파일 간 연계를 검수해야 한다.
